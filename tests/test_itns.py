#!/usr/bin/env python
# Let us build an api! -------
# we already have an api...
import json
import logging
import os
import sys

import ipfsapi

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

TEST_DB = "tests/test_db.temp.json"


def test_local_handler():
    # First we want to create an api handler connected to our local running IPFS daemon
    handler = ipfsapi.connect(host='localhost', port=5001)
    return handler


def test_hash():
    # This handler gets passed and used to interact with the API
    handler = test_local_handler()

    # by adding an object to our ipfs database we get an ipfs object containing the name
    # and the hash of that file
    test_obj = handler.add('tests/that_mysterious_testfile')
    logger.debug("Test object:\t", test_obj)
    assert test_obj['Hash'] == "QmNU5J9iouoKLhnFMJHfZoa4yHEsfbRrLVGMqw9Nh2Ugw6"
    return test_obj


def test_export():
    # now we want to store that in some kind of local database to retrieve and append to
    # it later on
    obj = test_hash()
    with open(TEST_DB, 'w') as f:
        json.dump(obj, f)


def test_import():
    # lets check if this was sucessfull by retrieving that object again
    with open(TEST_DB, 'r') as f:
        print("Content of DB file:\n", json.load(f))


if __name__ == '__main__':
    try:
        test_export()
        test_import()
        logger.info("All tests sucessfull!")
    except Exception as e:
        print(e)
        logger.warn("Test Failed!")
        sys.exit(1)
    finally:
        if os.path.isfile(TEST_DB):
            os.remove(TEST_DB)
