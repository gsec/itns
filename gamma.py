from hashlib import sha256
from math import log2
from random import choice, getrandbits, randint


def hashme():
    return sha256("{}".format(getrandbits(512)).encode()).hexdigest()


def gamma(t, inverse=False):
    """ Priority function. """
    if inverse:
        return log2(t+1)
    return 2**t - 1


def gamma_tot(path):
    hashtrust = fake_open(path)
    g = {}
    for h, t in hashtrust:
        print(h, t)
        g[h] = g.get(h, 0) + gamma(t)
    return g


def fake_open(name):
    # mock here for now
    RNG = 7
    hashes = [hashme() for i in range(RNG)]

    trusts = []
    for pub in range(RNG):
        mytrust = randint(0, 10)
        trusts.append((choice(hashes), mytrust))

    return trusts


