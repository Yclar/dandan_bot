# coding=gbk
import asyncio
import os
import random
from pathlib import Path
from typing import Type

import openpyxl
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.adapters.onebot.v11 import *
from nonebot.params import Depends
from nonebot.rule import to_me

capso = on_command("抽奖", rule=to_me(), priority=5, aliases={'capso', 'lucky_star'})


class EventChecker:
    def __init__(self, EventClass: Type[MessageEvent]):
        self.event_class = EventClass

    def __call__(self, event: MessageEvent) -> bool:
        return isinstance(event, self.event_class)


checker = EventChecker(GroupMessageEvent)


@capso.handle()
async def first_handle_receive(bot: Bot, event: Event, flag: bool = Depends(checker)):
    str_path = Path(os.getcwd())
    sx = openpyxl.load_workbook(str_path / 'dandan_bot' / 'libraries' / 'user.xlsx')
    sheet = sx['Sheet1']
    for x in range(1, sheet.max_row + 1):
        if sheet.cell(row=x, column=1).value == str(event.get_user_id()):
            if int(sheet.cell(row=x, column=2).value) >= 15:
                sheet.cell(row=x, column=2).value = str(int(sheet.cell(row=x, column=2).value) - 15)
                __id = sheet.cell(row=x, column=1).value
                get = ''
                adder = 0
                fflag = False
                nz_flag = False
                dd_flag = False
                mmmmmmsg = ''
                tmp = random.randint(1, 10000000)
                if tmp <= 1500:
                    get = '超级会员名额!!!'
                elif tmp <= 200001:
                    get = '60璇璇币,但是被蛋蛋吃了一半!'
                    adder = 30
                elif tmp <= 700001:
                    get = '让群主女装的大喇叭（!'
                    nz_flag = True
                elif tmp <= 1200001:
                    get = '进入会员制餐厅的机会！（大喜'
                elif tmp <= 1700001:
                    get = '好友鸠的笑容！\n另有20璇璇币请您收下！'
                    adder = 20
                elif tmp <= 2200001:
                    get = 'EK鲁比的女装一份！\n另有20璇璇币请您收下！'
                    adder = 20
                elif tmp <= 3000001:
                    get = 'バカリ收藏的蛋蛋画像一份！（异瞳控喜\n'
                    dd_flag = True
                elif tmp <= 4000001:
                    get = '去东京的旅游卷,但是过期了!'
                elif tmp <= 5000001:
                    get = '判定线抱枕\n——的概念版！'
                elif tmp <= 6000001:
                    get = '被田所浩二撅的抢先名额！（喜'
                elif tmp <= 6500001:
                    get = '114514个...'
                    fflag = True
                elif tmp <= 8000001:
                    get = '彩梦!'
                    tmp = random.randint(1, 10000000)
                    if tmp <= 5:
                        adder = 9999
                    elif tmp <= 100:
                        adder = 616
                    elif tmp <= 9000000:
                        adder = -random.randint(5, 10)
                    else:
                        adder = 10 * random.randint(1, 10)
                    if adder > 0:
                        mmmmmmsg = '彩梦吐出了' + str(adder) + '个璇璇币!'
                    elif adder < 0:
                        mmmmmmsg = '彩梦吃掉了' + str(-adder) + '个璇璇币!'
                    else:
                        mmmmmmsg = '彩梦正忙着算钱，一个璇璇币都不想给你~'
                else:
                    adder = random.randint(10, 25)
                    get = str(adder) + '个璇璇币!'

                sheet.cell(row=x, column=2).value = str(int(sheet.cell(row=x, column=2).value) + adder)
                if int(sheet.cell(row=x, column=2).value) < 0:
                    sheet.cell(row=x, column=2).value = '0'
                sx.save(str_path / 'dandan_bot' / 'libraries' / 'user.xlsx')
                msg: Message = MessageSegment.at(user_id=__id) + '\n'
                msg1 = '你抽到了' + get
                if flag:
                    print(1)
                    await capso.send(msg + msg1)
                else:
                    await capso.send(msg1)
                if fflag:
                    await asyncio.sleep(2)
                    await capso.finish('仙贝！')
                if dd_flag:
                    image_path: Path = str_path / 'data' / 'images' / 'dandan.png'
                    msg2 = MessageSegment.image(file=image_path)
                    await capso.finish(msg2)
                if nz_flag:
                    await asyncio.sleep(0.5)
                    if flag:
                        __info = await bot.get_group_member_list(group_id=event.group_id)
                        for __user in __info:
                            if (await bot.get_group_member_info(group_id=event.group_id,user_id=__user["user_id"],no_cache=True))["role"] == 'owner':
                                owner_id = __user["user_id"]
                                await capso.finish(MessageSegment.at(int(owner_id)) + '快点女装~')
                    else:
                        await capso.finish("但是我们是私聊欸~算了吧┑(￣Д ￣)┍")
                if mmmmmmsg != '':
                    await asyncio.sleep(0.1)
                    await capso.finish(mmmmmmsg)
                await capso.finish('期待您下次再来~（鞠躬）')
            else:
                await capso.finish('再抽奖就要欠钱啦~')

    await capso.finish('你是谁啊？我好像不太认识你的样子呢……请先注册再来吧~')
