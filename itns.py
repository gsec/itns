import argparse
import logging
import pprint

from datadiff import diff
from ruamel import yaml

from tree import tree_map

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEFAULT_DIR = "tests/database/testdb.yaml"
printer = pprint.PrettyPrinter(indent=1, width=90, compact=True)


def io_write(fname, dct):
    """ Write a dictionary to a yaml file.

    Uses ruamel and the not-default flow style for consistency.
    """
    try:
        with open(fname, 'x') as handler:
            yaml.dump(dct, handler, default_flow_style=False)
        logger.info('Database written to {}'.format(fname))
    except FileExistsError as e:
        print(e)


def io_read(fname):
    """ Read a yaml file and return its content as dictionary.
    """
    with open(fname, 'r') as handler:
        trunk = yaml.safe_load(handler)
    return trunk


def main():
    """ Read, write or check sync status.

    Reads/writes from/to yaml files or compares to current status.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', nargs='?', const=DEFAULT_DIR, default=None)

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-r', nargs='?', const='__current__', default=None)
    group.add_argument('-w', nargs='?', const=DEFAULT_DIR, default=None)

    args = parser.parse_args()

    if args.w:
        io_write(args.w, tree_map())

    if args.r:
        if args.r == '__current__':
            printer.pprint(tree_map())
        else:
            printer.pprint(io_read(args.r))

    if args.s:
        logger.info("\nReading from: {}".format(args.s))
        filelst, currlst = io_read(args.s), tree_map()
        sync_state = filelst == currlst
        print("\n::  ==SYNC==  ::  [{}] ".format(sync_state))

        if not sync_state:
            print("\na:Stored:---  <<[DIFFS]>>  b:Etheral:+++")
            print(diff(filelst, currlst, context=0, depth=15))


if __name__ == "__main__":
    main()
