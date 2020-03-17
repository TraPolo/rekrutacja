import argparse
import logging
import re
import sys
def setup_parser( parser ):
    subparsers = parser.add_subparsers(help="arguments", dest="command")

    parser_add = subparsers.add_parser(
        name="parser", help="parser")
    parser_add.set_defaults(func=add)
    parser_add.add_argument(
        "-n", "--name", dest="name", help="name", required=True)

    parser_add.add_argument(
        "-dl", "--deadline", dest="deadline", help="deadline", required=False)

    parser_add.add_argument(
        "-d", "--description", dest="description", help="description", required=False)

def add(args):
    print(args.deadline)


def main():
    parser = argparse.ArgumentParser(
        description="This is default parser")
    setup_parser(parser)
    res=parser.parse_args()
    res.func(res)


main()



