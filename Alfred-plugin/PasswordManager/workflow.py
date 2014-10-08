#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Generate a random password for specific account.
Get the password by name(site)

@Author Fity(imfity@gmail.com)
'''
import crypt
from crypt import DATA_DIR

import argparse
import logging
import os
import shlex
import sys

logging.basicConfig(level=logging.DEBUG, filename=os.path.join(DATA_DIR, 'crypt.log'))
logger = logging.getLogger(__name__)


def parse(query):
    '''parse the command line args to module args
    '''
    valid_actions = ['get', 'gen', 'del']
    parser = argparse.ArgumentParser()
    parser.add_argument('site')
    parser.add_argument('action', nargs='?')
    parser.add_argument('account', nargs='?')
    args = parser.parse_args(query)
    site = args.site
    action = args.action
    if action is None or action not in valid_actions:
        account = action
        action = 'get'
    else:
        account = args.account
    if not account:
        account = ''
    return (action, site, account)


def query(query):
    logger.debug('query string: '+repr(query))
    args = parse(shlex.split(query.strip()))
    rst = crypt.query(*args)
    print rst


def do(query):
    logger.debug('do in workflow: '+query)
    # query is a json string
    rst = crypt.do(query.strip())
    print rst
    # print repr(query)


if __name__ == '__main__':
    # print 'sys.argv:', sys.argv
    # print '=========='
    # query(' a ')
    query = 'github'
    args = parse([query, ])
    rst = crypt.query(*args)
    print rst
