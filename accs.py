# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:sts=4:expandtab

""" Handling of keys and accounts by autocrypt.

Lots of testing and playing around to see if this could be used for identity
management in itns.

Here we must provide a handler of autocrypts account.Account(<path>) instance!!!
"""
import os
from shutil import rmtree


def init(path=None, clear=False, handler=None):
    if clear:
        clearpath(path)

    try:
        os.makedirs(path)
        handler.init()
    except FileExistsError:
        pass


def create_user(dct=None, handler=None):
    if not dct:
        dct = {'id_name': 'default'}

    if dct['id_name'] in handler.list_identity_names():
        print("[{}] already in databse.\n{}".format(dct['id_name'], handler.list_identities()))
    else:
        handler.add_identity(**dct)


def clearpath(path):
    """ Watch out! This deletes the given path completely.
    """
    ans = input("This will delete the following directory: {}\n"
                "Are you sure? [y/n]".format(path))
    if ans not in 'yY':
        print("Aborting...")
        return
    else:
        for each in os.listdir(path):
            reach = os.path.abspath(os.path.join(path, each))
            if os.path.isfile(reach):
                os.remove(reach)
            elif os.path.isdir(reach):
                rmtree(reach)
