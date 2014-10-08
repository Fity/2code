Password Manager for Alfred
===========================

Baseed on Python and sqlite3.  
Encrypted by the python [pycrypto](https://www.dlitz.net/software/pycrypto/) library, using the AES algorithm.


Usage
=====
The key code is `pwd`.  
Using `pwd site [action] [account]` to query/generate/delete account for specific site.
Keyword for actions is `get`, `del`, `gen`.
If action is not given, it will be treat as `get` and the account will be `default` if not given.

Examples
=========
`pwd github`  
`pwd github fity`  
`pwd github get fity`

TODO
====
* Add custom password.
* Improve the init step, or isolate it from the query step.
* Improve the Encryption process of the sqlite db file.
