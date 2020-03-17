import argparse


def setup_parser(parser):
    subparsers = parser.add_subparsers(help="arguments", dest="command")

    parser_add = subparsers.add_parser(
        name="parser_add", help="parser_add")

    parser_add.set_defaults(func=add)
    parser_add.add_argument(
        "-n", "--name", dest="name", help="name", required=True)

    parser_add.add_argument(
        "-dl", "--deadline", dest="deadline", help="deadline", required=False)

    parser_add.add_argument(
        "-d", "--description", dest="description", help="description", required=False)

    parser_update = subparsers.add_parser(
        name="parser_update", help="parser_add")

    parser_update.set_defaults(func=update)

    parser_update.add_argument(
        "-n", "--name", dest="name", help="name", required=False)

    parser_update.add_argument(
        "-dl", "--deadline", dest="deadline", help="deadline", required=False)

    parser_update.add_argument(
        "-d", "--description", dest="description", help="description", required=False)

    parser_remove = subparsers.add_parser(
        name="parser_remove", help="parser_add")
    parser_remove.set_defaults(func=remove)

    parser_list = subparsers.add_parser(
        name="parser_list", help="parser_add")
    parser_list.set_defaults(func=listing)

def add(args):
    print(args.deadline)


def main():
    parser = argparse.ArgumentParser(
        description="This is default parser")
    setup_parser(parser)
    res = parser.parse_args()
    res.func(res)
