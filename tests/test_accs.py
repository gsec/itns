#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:sts=4:expandtab

import sys

sys.path.append("/repos/global/itns")

from autocrypt import account

import accs
from settings import TEST_PATH


def testrun():
    handler = account.Account(TEST_PATH)

    idct =  {'id_name': 'itns',     'email_regex': '*@ix'}
    bob =   {'id_name': 'bob',      'email_regex': 'bob@*'}
    alice = {'id_name': 'alice',    'email_regex': 'alice@*'}

    print("Clearing test path: {}".format(TEST_PATH))
    accs.init(path= TEST_PATH, clear=True, handler=handler)

    print("Initializing users...")
    for user in (idct, bob, alice):
        accs.create_user(user, handler=handler)
        print(handler.get_identity(user['id_name']))


if __name__ == '__main__':
    testrun()
