import argparse
import pandas as pd


#in progress

def setup_parser(parser):
    subparsers = parser.add_subparsers(help="arguments", dest="command")

    parser_add = subparsers.add_parser(name="add", help="Provide task to list ")
    parser_add.set_defaults(func=add)
    parser_add.add_argument("-n", "--name", dest="name", help="name", required=True)
    parser_add.add_argument("-dl", "--deadline", dest="deadline", help="deadline", required=False)
    parser_add.add_argument("-d", "--description", dest="description", help="description", required=False)

    parser_update = subparsers.add_parser(name="update", help="update chosen task")
    parser_update.set_defaults(func=update)
    parser_update.add_argument("-n", "--name", dest="name", help="name", required=False)
    parser_update.add_argument( "-dl", "--deadline", dest="deadline", help="deadline", required=False)
    parser_update.add_argument("-d", "--description", dest="description", help="description", required=False)
    parser_update.add_argument("-hs", "--hash", dest="hash", help="hash", required=True)

    parser_remove = subparsers.add_parser(name="remove", help="remove task from list")
    parser_remove.add_argument('hash', help='hash value of the task intended for removing ')
    parser_remove.set_defaults(func=remove)

    parser_list = subparsers.add_parser(name="list", help="display tasks in list")
    parser_list.set_defaults(func=listing)
    parser_list.add_argument("-all", "--all", action='store_true')
    parser_list.add_argument("-today", "--today", action='store_true')

def add(args):
    df = pd.DataFrame({'name': [args.name], 'deadline': [args.deadline], 'description': [args.description]})
    df.to_csv('task.csv', mode='a',header=False, index=False)

def update(args):
    print(args.name)

def listing(args):
    print(args.all)
    print(args.today)

def remove(args):
    print(args.hash)


def main():
    parser = argparse.ArgumentParser(description="This is default parser")
    setup_parser(parser)
    res = parser.parse_args()
    res.func(res)


main()

