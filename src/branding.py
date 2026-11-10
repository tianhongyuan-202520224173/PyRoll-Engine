"""应用品牌信息 —— 名称、副标题、版本号与图标路径。

把品牌相关内容集中在一个文件里，改名字只动这一处。
"""

import os
import sys

APP_NAME = "薪酬管家"
APP_NAME_EN = "PayrollPro"
APP_SUBTITLE = "薪资核算与管理"
APP_VERSION = "1.2.0"


def resource_path(relative: str) -> str:
    """返回资源的绝对路径：源码运行和 PyInstaller 打包后都能找到。"""
    base = getattr(
        sys, "_MEIPASS",
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    )
    return os.path.join(base, relative)


ICON_PATH = resource_path("assets/icon.ico")
