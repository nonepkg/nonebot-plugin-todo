import nonebot
import yaml
from pathlib import Path
from typing import Optional

_DATA_PATH = Path() / "data" / "todo" / "todo_list.yml"

def get_todo_list(user_id: Optional[str] = None, group_id: Optional[str] = None) -> dict:
    todo_list = _load_todo_list()

    if user_id:
        return todo_list["user"][user_id]
    elif group_id:
        return todo_list["group"][group_id]
    else:
        return todo_list


# 更新待办事项列表
def _update_todo_list(group_id: str, block: bool, *plugins: str) -> str:
    todo_list = _load_todo_list()
    message = "结果如下："
    operate = "屏蔽" if block else "启用"
    for plugin in plugins:
        message += "\n"
        if plugin in todo_list:
            if (
                not group_id in todo_list[plugin]
                or todo_list[plugin][group_id] == block
            ):
                todo_list[plugin][group_id] = not block
                message += f"插件{plugin}{operate}成功！"
            else:
                message += f"插件{plugin}已经{operate}！"
        else:
            message += f"插件{plugin}不存在！"
    _dump_todo_list(todo_list)
    return message


# 保存待办事项列表
def _load_todo_list() -> dict:
    try:
        return yaml.load(_DATA_PATH.open("r", encoding="utf-8"))
    except FileNotFoundError:
        return {}


# 保存待办事项列表
def _dump_todo_list(todo_list: dict):
    _DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    yaml.dump(
        todo_list,
        _DATA_PATH.open("w", encoding="utf-8"),
        indent=4,
        separators=(",", ": "),
    )
