from nonebot.rule import ArgumentParser

from .handle import *

todo_parser = ArgumentParser("todo")
'''
npm_subparsers = todo_parser.add_subparsers()

list_parser = npm_subparsers.add_parser("list", help="show todo list")
list_parser.add_argument(
    "-s", "--store", action="store_true", help="show todo store list"
)
list_parser.add_argument(
    "-d", "--default", action="store_true", help="show default todo list"
)
list_parser.add_argument("-p", "--private", action="store_true", help="set in private")
list_parser.add_argument("-g", "--group", action="store", help="show group todo list")
list_parser.set_defaults(handle=handle_list)

block_parser = npm_subparsers.add_parser("add", help="block todo")
block_parser.add_argument("todos", nargs="*", help="todos you want to block")
block_parser.add_argument("-d", "--default", action="store_true", help="set default")
block_parser.add_argument("-a", "--all", action="store_true", help="select all todo")
block_parser.add_argument("-g", "--group", action="store", help="set in group")
block_parser.add_argument("-p", "--private", action="store_true", help="set in private")
block_parser.set_defaults(handle=handle_block)

unblock_parser = npm_subparsers.add_parser("remove", help="unblock todo")
unblock_parser.add_argument("todos", nargs="*", help="todos you want to unblock")
unblock_parser.add_argument("-d", "--default", action="store_true", help="set default")
unblock_parser.add_argument(
    "-a", "--all", action="store_true", help="select all todo"
)
unblock_parser.add_argument("-p", "--private", action="store_true", help="set in private")
unblock_parser.add_argument("-g", "--group", action="store", help="set in group")
unblock_parser.set_defaults(handle=handle_unblock)

info_parser = npm_subparsers.add_parser("stop", help="show todo info")
info_parser.add_argument("todo", help="todos you want to know")
info_parser.set_defaults(handle=handle_info)

install_parser = npm_subparsers.add_parser("start", help="install todo")
install_parser.add_argument("todos", nargs="*", help="todos you want to install")
install_parser.add_argument("-i", "--index", action="store", help="point to a mirror")
install_parser.set_defaults(handle=handle_install)
'''