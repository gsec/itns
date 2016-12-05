# Let us build an api! -------
# we already have an api...
import ipfsapi


def test_local_handler():
    try:
        handler = ipfsapi.connect(host='localhost', port=5001)
        print("imokay")
    except:
        handler = None
        print("failed to create handler!")
    return handler


def test_hash():
    handler = test_local_handler()
    test_obj = handler.add('that_mysterious_testfile')
    print(test_obj)
    assert test_obj['Hash'] == "QmNU5J9iouoKLhnFMJHfZoa4yHEsfbRrLVGMqw9Nh2Ugw6"
