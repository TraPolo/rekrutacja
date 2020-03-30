import argparse
import pandas as pd
import os
from datetime import datetime

# in progress

def setup_parser(parser):
    subparsers = parser.add_subparsers(help="description of all parsers:", dest="command")

    parser_add = subparsers.add_parser(name="add", help="""Provide task to list ,example(task2.py add -n name1 -dl 2020-02-15 -d exemplary task),
                                                        remember about proper format of date YYYY-MM-DD,and that each string having more than one word
                                                        must be inside quotation mark """)
    parser_add.set_defaults(func=add)
    parser_add.add_argument("-n", "--name", dest="name", help="name", required=True)
    parser_add.add_argument("-dl", "--deadline", dest="deadline", help="deadline YYYY-MM_DD", required=False, type=lambda d: datetime.strptime(d, '%Y-%m-%d'))
    parser_add.add_argument("-d", "--description", dest="description", help="description", required=False)

    parser_update = subparsers.add_parser(name="update", help="""Update chosen task by its  hash value(visible using list function),remember about proper format of date YYYY-MM-DD,
                                                                and that each string having more than one word must be inside quotation mark """)
    parser_update.set_defaults(func=update)
    parser_update.add_argument("-n", "--name", dest="name", help="name", required=False)
    parser_update.add_argument("-dl", "--deadline", dest="deadline", help="deadline YYYY-MM_DD", required=False, type=lambda d: datetime.strptime(d, '%Y-%m-%d'))
    parser_update.add_argument("-d", "--description", dest="description", help="description", required=False)
    parser_update.add_argument("-hs", "--hash", dest="hash", help="hash made by index value", required=True, type=int)

    parser_remove = subparsers.add_parser(name="remove", help="remove task from list using hash value(hash value "
                                                              "visible using list function)")
    parser_remove.add_argument('hash', help='hash value of the task intended for removing ')
    parser_remove.set_defaults(func=remove)

    parser_list = subparsers.add_parser(name="list", help="display tasks in list,options to choose:-all (displaying "
                                                          "all tasks),-today(displaying tasks with today's date)  ")
    parser_list.set_defaults(func=listing)
    parser_list.add_argument("-all", "--all", action='store_true')
    parser_list.add_argument("-today", "--today", action='store_true')


def add(args):
    df = pd.DataFrame({'name': [args.name], 'deadline': [args.deadline], 'description': [args.description]})
    df['hash'] = hash(str(args.name) + str(args.deadline) + str(args.description))
    df.set_index('hash', inplace=True, drop=False)
    with open('task.csv', 'a'):
        if os.path.getsize('task.csv') == 0:
            df.to_csv('task.csv', header=True, index=False)
        else:
            df.to_csv('task.csv', mode='a', header=False, index=False)


def update(args):
    df2 = pd.read_csv('task.csv')
    df2.set_index('hash', inplace=True, drop=False)
    if args.name != None:
        df2.at[args.hash, 'name'] = args.name
    if args.deadline != None:
        df2.at[args.hash, 'deadline'] = args.deadline.date()
    if args.deadline != None:
        df2.at[args.hash, 'description'] = args.description

    df2.to_csv('task.csv', header=True, index=False)


def listing(args):
    if args.all:
        print(pd.read_csv('task.csv'))
    if args.today:
        df = pd.read_csv('task.csv')
        df2 = df[(df['deadline']==str(datetime.today().date()))]
        df2.reset_index(drop=True,inplace=True)
        print(df2)


def remove(args):
    df = pd.read_csv('task.csv')
    df = df[df.hash != int(args.hash)]
    df.to_csv('task.csv',header=True, index=False)


def main():
    parser = argparse.ArgumentParser(description="List of tasks")
    setup_parser(parser)
    res = parser.parse_args()
    res.func(res)


main()
