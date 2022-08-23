# coding=gbk
import nonebot
from nonebot.adapters.onebot.v11 import *
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.params import State, CommandArg
import os
import openpyxl
from pathlib import Path
from typing import Optional


async def get(song_name: str) -> Optional[str]:
    str_path = Path(os.getcwd())
    sx = openpyxl.load_workbook(str_path / 'dandan_bot' / 'libraries' / 'song_diff.xlsx')
    phi = sx['phi']
    ret = ''
    for x in range(2, phi.max_row + 1):
        f = 0
        alias = str(phi.cell(row=x, column=9).value).split()
        for i in alias:
            if str(i).title() == song_name.title():
                f = 1
        if str(phi.cell(row=x, column=5).value).title() == song_name.title() or f:
            __lv = str(phi.cell(row=x, column=6).value)
            __diff = str(phi.cell(row=x, column=7).value)
            __n = str(phi.cell(row=x, column=8).value)
            __ver = str(phi.cell(row=x, column=4).value)
            __name = str(phi.cell(row=x, column=5).value)
            ret += __lv + '#' + __diff + '#' + __n + '#' + __ver + '#' + __name + '#@#'
    if ret == '':
        return 'baka'
    return ret


async def alias_(alias: str, name: str) -> Optional[str]:
    str_path = Path(os.getcwd())
    sx = openpyxl.load_workbook(str_path / 'dandan_bot' / 'libraries' / 'song_diff.xlsx')
    phi = sx['phi']
    ret = 'baka'
    for x in range(2, phi.max_row + 1):
        if str(phi.cell(row=x, column=5).value) == name:
            ret = 'ok'
            if phi.cell(row=x, column=9).value == None:
                phi.cell(row=x, column=9).value = alias + ' '
            else:
                phi.cell(row=x, column=9).value = str(phi.cell(row=x, column=9).value) + alias + ' '
    sx.save(str_path / 'dandan_bot' / 'libraries' / 'song_diff.xlsx')
    return ret
