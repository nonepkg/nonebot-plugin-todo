# Nonebot Plugin ToDo

基于 [nonebot2](https://github.com/nonebot/nonebot2) 和 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 的待办事项提醒插件

[![License](https://img.shields.io/github/license/Jigsaw111/nonebot_plugin_todo)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.7.3+-blue.svg)
![NoneBot Version](https://img.shields.io/badge/nonebot-2.0.0a11+-red.svg)
![Pypi Version](https://img.shields.io/pypi/v/nonebot-plugin-todo.svg)

### 安装

#### 从 PyPI 安装（推荐）

- 使用 nb-cli  

```
nb plugin install nonebot_plugin_todo
```

- 使用 poetry

```
poetry add nonebot_plugin_todo
```

- 使用 pip

```
pip install nonebot_plugin_todo
```

#### 从 GitHub 安装（不推荐）

```
git clone https://github.com/Jigsaw111/nonebot_plugin_todo.git
```

### 使用

**不推荐使用此插件进行隐私相关的待办事项提醒！**

**使用前请先确保命令前缀为空，否则请在以下命令前加上命令前缀 (默认为 `/` )。**

- `todo list` 查看当前会话（群/私聊）的待办事项列表

- `todo add job cron message` 新增待办事项

- - `job` 作业名，每个会话不能存在两个相同的作业名
- - `cron` crond 表达式，需用 "" 包裹，例如 "\* \* \* \* \*" 表示每分钟
- - `message` 要定时发送的消息，支持 CQ 码，必要时需用 "" 包裹

- `todo remove job` 删除待办事项

- `todo pause job` 暂停待办事项

- `todo resume job` 恢复待办事项

### Q&A

- **这是什么？**  
  待办事项提醒，简称**闹钟**。
- **有什么用？**  
  **没有用**。这个项目不像 [nonebot_plugin_manager](https://github.com/Jigsaw111/nonebot_plugin_manager) 一样希望对他人有所帮助，只是我有个同学希望我每天晚上九点提醒他去跑步，就写了这玩意儿。

<details>
<summary>展开更多</summary>

### Bug



### Changelog

- 210414，完成基本功能，发布 0.1.0 版本。
- 210412，创建项目。

</details>
