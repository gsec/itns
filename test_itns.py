# Let us build an api!
import itns


def test_hash():
    myhash = itns.get_hash('that_mysterious_testfile')
    assert myhash ==  "QmNoUw1sQcz68dRpNGgr46C6vHithq2Wwa7HStFzwNRvKj"
    print(myhash)
