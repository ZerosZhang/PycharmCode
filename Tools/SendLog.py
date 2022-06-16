"""
日志类，导入后即可使用
用法： logging.info(f"保存数据到{_path}中...")
"""

import logging
import coloredlogs

# 此处可以屏蔽某种类型的日志消息
logging.disable(logging.DEBUG)
# logging.disable(logging.INFO)
# logging.disable(logging.WARNING)
# logging.disable(logging.ERROR)
# logging.disable(logging.CRITICAL)

# 每个日志消息中不同字段的颜色
FIELD_STYLES = dict(
    asctime=dict(color='blue'),
    hostname=dict(color='magenta'),
    levelname=dict(color='green'),
    filename=dict(color='magenta'),
    name=dict(color='blue'),
    threadName=dict(color='green')
)

# 各种类型的日志消息的颜色
LEVEL_STYLES = dict(
    debug=dict(color='blue'),
    info=dict(color='white'),
    warning=dict(color='yellow'),
    error=dict(color='cyan'),
    critical=dict(color='red')
)

# 使用coloredlogs设置日志的输出形式
coloredlogs.install(level="DEBUG",
                    fmt="[%(asctime)s] 【%(levelname)s】 %(message)s",
                    level_styles=LEVEL_STYLES,
                    field_styles=FIELD_STYLES)


def PrintDebug(_message):
    logging.debug(_message)


def PrintInfo(_message):
    logging.info(_message)


def PrintWarning(_message):
    logging.warning(_message)


def PrintError(_message):
    logging.error(_message)


def PrintCritical(_message):
    logging.critical(_message)


if __name__ == '__main__':
    # 使用彩色日志
    PrintDebug("这是一个debug消息")
    PrintInfo("这是一个info消息")
    PrintWarning("这是一个warning消息")
    PrintError("这是一个error消息")
    PrintCritical("这是一个critical消息")
