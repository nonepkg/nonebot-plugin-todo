from typing import Optional
from nonebot_plugin_todo.data import get_todo_list
from nonebot.plugin import on_shell_command, require
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import (
    Bot,
    Event,
    Message,
    PrivateMessageEvent,
    GroupMessageEvent,
)
from nonebot import get_bots

from .data import check_time
from .parser import todo_parser

scheduler = require("nonebot_plugin_apscheduler").scheduler

# 注册 shell_like 事件响应器
todo = on_shell_command("todo", parser=todo_parser, priority=5)

# 每分钟进行一次检测
@scheduler.scheduled_job("cron", minute="*", id="todo")
async def _():
    bots = get_bots()
    todo_list = get_todo_list()

    for group_id in todo_list["group"]:
        for job in todo_list["group"][group_id]:
            if check_time(todo_list["group"][group_id][job]):
                for bot in bots:
                    await bots[bot].send_msg(
                        group_id=group_id,
                        message=Message(todo_list["group"][group_id][job]["message"]),
                    )


@todo.handle()
async def _(bot: Bot, event: Event, state: T_State):
    args = state["args"]
    user_id = _get_user_id(event)
    group_id = _get_group_id(event)
    is_admin = _is_admin(event)
    is_superuser = _is_superuser(bot, event)
    if hasattr(args, "handle"):
        await todo.finish(args.handle(args, user_id, group_id, is_admin, is_superuser))


def _get_group_id(event: Event) -> Optional[int]:
    return event.group_id if isinstance(event, GroupMessageEvent) else None


def _get_user_id(event: Event) -> Optional[int]:
    return event.user_id if isinstance(event, PrivateMessageEvent) else None


def _is_admin(event: Event) -> bool:
    return (
        event.sender.role in ["admin", "owner"]
        if isinstance(event, GroupMessageEvent)
        else False
    )


def _is_superuser(bot: Bot, event: Event) -> bool:
    return str(event.user_id) in bot.config.superusers
