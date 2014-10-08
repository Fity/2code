# -*- coding:utf-8 -*-
'''
Local password manager for Alfred
@Author Fity(imfity@gmail.com)
'''
try:
    import simplejson as json
except ImportError:
    import json
import logging
import os
import plistlib
import sqlite3
import sys
try:
    import xml.etree.cElementTree as et
except ImportError as e:
    import xml.etree.ElementTree as et

from sqlite3 import OperationalError

from Crypto.Cipher import AES
from Crypto import Random

# imports for GUI window, using Tkinter module
import Tkinter as tk


STORAGE_DIR = os.path.join(os.path.expanduser('~'), '''Library/Application Support/Alfred 2/Workflow Data''')


def _get_data_dir():
    plist = plistlib.readPlist('./info.plist')
    bundleid = plist.bundleid
    data_dir = os.path.join(STORAGE_DIR, bundleid)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir, 0755)
    return data_dir
DATA_DIR = _get_data_dir()


PASS_LENS = 14

logging.basicConfig(level=logging.DEBUG, filename=os.path.join(DATA_DIR, 'crypt.log'))
logger = logging.getLogger(__name__)
logger.debug('DATA_DIR: '+DATA_DIR)


def passwd():
    global PASS_LENS
    # return os.urandom(PASS_LENS).encode('hex')
    return os.urandom(10).encode('base-64').strip()


class ItemList(object):
    '''Item list for Alfred
    '''

    def __init__(self):
        self.root = et.Element('items')

    def __str__(self):
        return et.tostring(self.root)

    def add_item(self, action, site, account):
        args = {'action': action, 'site': site, 'account': account}
        item = et.SubElement(self.root, 'item', uid=str(len(self.root)),
                             arg=json.dumps(args), valid='yes', autocomplete='')
        _title = et.SubElement(item, 'title')
        _title.text = site
        _sub = et.SubElement(item, 'subtitle')
        _sub.text = action + ' ' + account
        _icon = et.SubElement(item, 'icon')
        _icon.text = 'favicons/icon.png'


class DB(object):
    '''DB Processor
    '''

    validate_line = 'AlfredEncrypFile'
    padding = '0'

    def __init__(self):
        self.db = os.path.join(DATA_DIR, 'crypt.db')
        self.db_file = os.path.join(DATA_DIR, 'cryptdb')
        self.db_pub = os.path.join(DATA_DIR, 'pub.db')
        self.db_table = 'crypt_account'
        self.db_sql = '''create table {0}(site TEXT, account TEXT, pwd TEXT,
                         constraint pk_t2 primary key (site, account))'''.format(self.db_table)
        self.db_sql_pub = '''create table {0}(site TEXT, account TEXT,
                         constraint pk_t2 primary key (site, account))'''.format(self.db_table)
        # self.private_db()
        self.public_db()

    def query(self, site, account):
        db = self.db_pub
        args = [site, ]
        sql = 'select site, account from {0} where site=:1'.format(self.db_table)
        if account:
            account = '%' + account + '%'
            sql += " and account like :2"
            args.append(account)
        conn = sqlite3.connect(db)
        rows = []
        with conn:
            cursor = conn.cursor()
            try:
                cursor.execute(sql, tuple(args))
            except OperationalError as e:
                logger.exception(e)
            else:
                rows = cursor.fetchall()
            finally:
                if cursor:
                    cursor.close()
        return rows

    def get(self, site, account):
        self.decrypt()
        sql = '''select * from {0} where site=:1 and account=:2'''.format(self.db_table)
        row = []
        conn = sqlite3.connect(self.db)
        with conn:
            cursor = conn.cursor()
            try:
                cursor.execute(sql, (site, account))
            except OperationalError as e:
                logger.exception(e)
            else:
                rows = cursor.fetchall()
                logger.debug('rows got: '+str(rows))
                if rows:
                    row = rows[0]
            finally:
                if cursor:
                    cursor.close()
        self.encrypt()
        return row

    def delete(self, site, account):
        rows = self.get(site, account)
        if not rows:
            return
        self.decrypt()
        if self._delete(self.db, site, account) and self._delete(self.db_pub, site, account):
            self.encrypt()
            return True
        else:
            os.unlink(self.db)
            return False

    def _delete(self, db, site, account):
        sql = '''delete from {0} where site=:1 and account=:2'''.format(self.db_table)
        conn = sqlite3.connect(db)
        with conn:
            cursor = conn.cursor()
            try:
                cursor.execute(sql, (site, account))
            except OperationalError as e:
                logger.exception(e)
                return False
            finally:
                if cursor:
                    cursor.close()
        return True

    def insert(self, site, account):
        self.decrypt()
        password = passwd()
        if self._insert(site, account, password) and self._insert(site, account):
            self.encrypt()
        else:
            password = None
            os.unlink(self.db)
        return password

    def _insert(self, site, account, password=None):
        args = [site, account]
        if password is None:
            db = self.db_pub
            sql = '''insert into {0} (site, account) values(:1, :2)'''.format(self.db_table)
        else:
            db = self.db
            sql = '''insert into {0} (site, account, pwd) values(:1, :2, :3)'''.format(self.db_table)
            args.append(password)
        conn = sqlite3.connect(db)
        with conn:
            cursor = conn.cursor()
            try:
                cursor.execute(sql, args)
            except OperationalError as e:
                logger.exception(e)
                logger.error('failed db: '+db+' sql: '+sql+' args: '+','.join(args))
                return False
            else:
                return True
            finally:
                if cursor:
                    cursor.close()

    def private_db(self):
        if os.path.exists(self.db_file):
            return
        if os.path.exists(self.db):
            os.unlink(self.db)
        self._create_db(self.db, self.db_sql)
        import shutil
        # shutil.copy(self.db, os.path.join(os.path.dirname(self.db), 'origin.db'))
        self.encrypt()

    def public_db(self):
        if os.path.exists(self.db_pub):
            return
        first_use = False
        if not os.path.exists(self.db_file):
            self.private_db()
            first_use = True
        self._create_db(self.db_pub, self.db_sql_pub)
        if not first_use:
            self.export_db()

    def export_db(self):
        self.decrypt()
        conn = sqlite3.connect(self.db)
        sql = '''select site, account from {0}'''.format(self.db_table)
        rows = []
        with conn:
            cursor = conn.cursor()
            try:
                cursor.execute(sql)
            except OperationalError as e:
                logger.exception(e)
            else:
                rows = cursor.fetchall()
            finally:
                if cursor:
                    cursor.close()
        conn = sqlite3.connect(self.db_pub)
        sql = '''insert into {0} (site, account) valies(:1, :2)'''.format(self.db_table)
        with conn:
            cursor = conn.cursor()
            try:
                cursor.executemany(sql, rows)
            except OperationalError as e:
                logger.exception(e)
            finally:
                if cursor:
                    cursor.close()
        os.unlink(self.db)

    def encrypt(self):
        key = self.crypt_key()
        logger.debug('encrypt: '+str(key))
        with open(self.db, 'rb') as origin, open(self.db_file, 'wb') as dest:
            iv = Random.new().read(AES.block_size)
            dest.write(iv.encode('hex')+'\n')
            logger.debug('iv generate: '+iv.encode('hex'))
            cipher = AES.new(key, AES.MODE_CBC, iv)
            validate_line = cipher.encrypt(self.validate_line)
            dest.write(validate_line + '\n')

            cipher = AES.new(key, AES.MODE_CBC, iv)
            lines = origin.read()
            cipher_text = cipher.encrypt(self._padding_line(lines))
            dest.write(cipher_text.encode('hex'))
        os.unlink(self.db)
        logger.debug('encrypt ok.')

    def decrypt(self):
        key = self.crypt_key()
        logger.debug('decrypt: '+str(key))
        with open(self.db_file, 'rb') as origin, open(self.db, 'wb') as dest:
            iv = origin.readline().strip('\n').decode('hex')
            logger.debug('iv got is: '+iv.encode('hex'))
            cipher = AES.new(key, AES.MODE_CBC, iv)
            validate_line = cipher.decrypt(origin.readline().strip('\n'))
            if validate_line != self.validate_line:
                logger.error('not the right key to decrypt the db file')
                sys.exit()
            logger.debug('validate passed')

            lines = origin.read()
            cipher = AES.new(key, AES.MODE_CBC, iv)
            plain_text = cipher.decrypt(lines.decode('hex'))
            plain_text = self._unpadding_line(plain_text)
            dest.write(plain_text)

        logger.debug('decrypt ok.')

    def _padding_line(self, line, pad='0'):
        length = len(line)
        tailing = length % 16
        if tailing != 0:
            line += self.padding * (16 - tailing)
        return line

    def _unpadding_line(self, line, pad='0'):
        return line.rstrip(pad)

    def _get_iv(self):
        iv = getattr(self, iv, None)
        if iv:
            return iv
        else:
            iv_file = os.path.join(DATA_DIR, 'iv')
            if os.path.exists(iv_file):
                with open(iv_file, 'rb') as f:
                    iv = f.read().strip()
            else:
                iv = Random.new().read(AES.block_size)
                with open(iv_file, 'wb') as f:
                    f.write(iv)
        setattr(self, 'iv', iv)
        return iv

    def _create_db(self, db, sql):
        logger.debug('db: '+db+' sql: '+sql)
        conn = sqlite3.connect(db)
        with conn:
            cursor = conn.cursor()
            try:
                cursor.execute(sql)
            except OperationalError as e:
                logger.exception(e)
                sys.exit()
            finally:
                if cursor:
                    cursor.close()

    def crypt_key(self):
        password = getattr(self, 'password', None)
        if password:
            return password
        root = tk.Tk()
        app = Application(root, self)
        root.bind("<Return>", app.hit_handler)
        os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        # next line will make the window always be front of others(but not focused, so comment it.)
        # root.attributes("-topmost", True)
        root.mainloop()
        password = getattr(self, 'password', '')
        if not password:
            logger.warn('empty password got')
            sys.exit()
        password = self._padding_line(password, pad='a')
        setattr(self, 'password', password)
        return password


class Application(tk.Frame):

    def __init__(self, parent, caller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.caller = caller
        self.initUI()

    def initUI(self):
        self.parent.title('Encrypt Key')
        self.parent.geometry("220x60+470+300")
        self.label = tk.Label(self.parent, text='密码:')
        self.label.grid(row=0, column=0)
        self.entry = tk.Entry(self.parent, show='*')
        self.entry.grid(row=0, column=1)
        self.entry.focus()
        frame = tk.Frame(self.parent)
        self.confirm = tk.Button(frame, text='确认', command=self.get)
        self.confirm.grid(row=0, column=1)
        self.cancel = tk.Button(frame, text='取消', command=self.quit)
        self.cancel.grid(row=0, column=0)
        frame.grid(row=1,column=1)

    def hit_handler(self, event):
        self.get()

    def get(self):
        v = self.entry.get()
        setattr(self.caller, 'password', v)
        logger.debug('password got is: '+v)
        self.quit()


def query(action, site, account):
    logger.debug('args: '+','.join((action, site, account)))
    items = ItemList()
    if action == 'gen':
        items.add_item(action, site, account)
        return items
    db = DB()
    rows = db.query(site, account)
    logger.debug('rows: '+str(rows))
    if not account:
        account = 'default'
    if (site, account) not in rows:
        items.add_item('gen', site, account)
    for site, account in rows:
        items.add_item(action, site, account)
    return items


def do(query_str):
    query = json.loads(query_str)
    logger.debug('do query_str: '+str(query))
    action = query['action']
    site = query['site']
    account = query['account']

    db = DB()
    if action == 'get':
        row = db.get(site, account)
        password = None
        logger.debug('get password: '+str(row))
        if row:
            password = row[2]
        return password
    elif action == 'del':
        ok = db.delete(site, account)
        logger.debug('delete account: '+'***'.join([site, account]))
        return 'success' if ok else 'failed'
    else:
        # generate
        logger.debug('generate new password')
        password = db.insert(site, account)
        logger.debug('generate new password: '+str(password))
        return password


if __name__ == '__main__':
    print 'gen:', do(json.dumps({'action': 'gen', 'account': 'default', 'site': 'github'}))
    print 'get:', str(do(json.dumps({'action': 'get', 'account': 'default', 'site': 'github'})))
    # db = DB()
    # db.decrypt()
