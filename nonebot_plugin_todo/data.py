import time
import yaml
from pathlib import Path
from typing import Optional, Union, Any, List, Dict

_DATA_PATH = Path() / "data" / "todo" / "todo_list.yml"


def format_crontab(crontab: str, default: List[int]) -> List[int]:
    if crontab == "*":
        return default
    elif "," in crontab:
        return list(int(i) for i in crontab.split(","))
    elif "-" in crontab:
        return list(range(int(crontab.split("-")[0]), int(crontab.split("-")[0]) + 1))
    elif "/" in crontab:
        return list(filter(lambda x: x % int(crontab[3:]) == 0, default))
    else:
        return [int(crontab)]


def check_time(job: Dict[str, Any]) -> bool:

    localtime = time.localtime(time.time())

    cron = job["cron"].split()
    minute = format_crontab(cron[0], list(range(60)))
    hour = format_crontab(cron[1], list(range(24)))
    day = format_crontab(cron[2], list(range(1, 31)))
    month = format_crontab(cron[3], list(range(1, 13)))
    day_of_week = format_crontab(cron[4], list(range(7)))

    if (
        job["enable"]
        and localtime.tm_min in minute
        and localtime.tm_hour in hour
        and localtime.tm_mday in day
        and localtime.tm_mon in month
        and localtime.tm_wday in day_of_week
    ):
        return True
    else:
        return False


def get_todo_list(
    user_id: Optional[int] = None, group_id: Optional[int] = None
) -> Optional[Dict[str, Any]]:

    todo_list = _load_todo_list()

    if user_id:
        if user_id not in todo_list["user"]:
            todo_list["user"][user_id] = {}
        tmp_todo_list = todo_list["user"][user_id]
    elif group_id:
        if group_id not in todo_list["group"]:
            todo_list["group"][group_id] = {}
        tmp_todo_list = todo_list["group"][group_id]
    else:
        tmp_todo_list = todo_list

    _dump_todo_list(todo_list)

    return tmp_todo_list


def add_todo_list(
    job: Dict[str, Any],
    user_id: Optional[int] = None,
    group_id: Optional[int] = None,
):
    _update_todo_list("add", job, user_id, group_id)


def remove_todo_list(
    job: str,
    user_id: Optional[int] = None,
    group_id: Optional[int] = None,
):
    _update_todo_list("remove", job, user_id, group_id)


def pause_todo_list(
    job: str,
    user_id: Optional[int] = None,
    group_id: Optional[int] = None,
):
    _update_todo_list("pause", job, user_id, group_id)


def resume_todo_list(
    job: str,
    user_id: Optional[int] = None,
    group_id: Optional[int] = None,
):
    _update_todo_list("resume", job, user_id, group_id)


# 更新待办事项列表
def _update_todo_list(
    type: str,
    job: Union[str, Dict[str, Any]],
    user_id: Optional[int] = None,
    group_id: Optional[int] = None,
):

    tmp_todo_list = get_todo_list(user_id, group_id)

    todo_list = get_todo_list()

    if type == "add":
        tmp_todo_list.update(job)
    elif type == "remove":
        tmp_todo_list.pop(job)
    elif type == "pause":
        tmp_todo_list[job]["enbale"] = False
    elif type == "resume":
        tmp_todo_list[job]["enbale"] = True

    if user_id:
        todo_list["user"][user_id].update(tmp_todo_list)
    elif group_id:
        todo_list["group"][group_id].update(tmp_todo_list)

    _dump_todo_list(todo_list)


# 保存待办事项列表
def _load_todo_list() -> Dict[str, Any]:
    try:
        return yaml.safe_load(_DATA_PATH.open("r", encoding="utf-8"))
    except FileNotFoundError:
        return {"user": {}, "group": {}}


# 保存待办事项列表
def _dump_todo_list(todo_list: Dict[str, Any]):
    _DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    yaml.dump(
        todo_list,
        _DATA_PATH.open("w", encoding="utf-8"),
    )
