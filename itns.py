# import subprocess
from ruamel import yaml
import logging
from tree import tree_map
import argparse

logger = logging.getLogger(__name__)
DEFAULT_DIR = "database/testdb.yaml"


def io_write(fname, dct):
    """ Write a dictionary to a yaml file.

    Uses ruamel and the not-default flow style for consistency.
    """
    with open(fname, 'w+') as handler:
        yaml.dump(dct, handler, default_flow_style=False)
    logger.info('Parameter file written to {}'.format(fname))


def io_read(fname):
    """ Read a yaml file and return its content as dictionary.
    """
    with open(fname, 'r') as handler:
        trunk = yaml.safe_load(handler)
    return trunk


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', nargs='?', const=DEFAULT_DIR, default=None)

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-r', nargs='?', const='__current__', default=None)
    group.add_argument('-w', nargs='?', const=DEFAULT_DIR, default=None)

    args = parser.parse_args()
    print(args)

    if args.w:
        io_write(args.w, tree_map())
        print("Written file, output as follows:\n")
        print(io_read(args.w))

    if args.r:
        if args.r == '__current__':
            print(tree_map())
        else:
            print(io_read(args.r))

    if args.s:
        sync_state = io_read(args.s) == tree_map()
        print("SYNC: ", sync_state)


if __name__ == "__main__":
    main()
