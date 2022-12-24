from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import MessageEvent, GroupMessageEvent
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.params import Depends
from typing import Type
from random import randint
from asyncio import sleep


hit_on = on_command('打我', aliases={'hit', 'hit_me', '蛋蛋打我'}, priority=5, rule=to_me(), block=True)


class EventChecker:
    def __init__(self, EventClass: Type[MessageEvent]):
        self.event_class = EventClass

    def __call__(self, event: MessageEvent) -> bool:
        return isinstance(event, self.event_class)


checker = EventChecker(GroupMessageEvent)


@hit_on.handle()
async def check_and_send(bot: Bot, event: Event, flag: bool = Depends(checker)):
    if flag:
        my_role = (await bot.get_group_member_info(group_id=event.group_id, user_id=event.self_id, no_cache=True))["role"]
        user_role = (await bot.get_group_member_info(group_id=event.group_id, user_id=event.user_id, no_cache=True))["role"]
        if (my_role == 'owner') or (my_role == 'admin' and user_role == 'member'):
            base = randint(7, 10)
            await hit_on.send('一拳！')
            await sleep(1)
            await bot.set_group_ban(group_id=event.group_id, user_id=event.user_id,
                                    duration=randint(1, base) * 60)
            await sleep(1)
            await hit_on.send("两拳!")
            await sleep(1)
            await bot.set_group_ban(group_id=event.group_id, user_id=event.user_id,
                                    duration=(randint(1, base - 1) + base) * 60)
            await sleep(1)
            await hit_on.send("三拳!")
            await sleep(1)
            await bot.set_group_ban(group_id=event.group_id, user_id=event.user_id,
                                    duration=(randint(1, base - 1) + 2 * base) * 60)
            await sleep(1)
            await hit_on.finish("够了吗!")
        else:
            await hit_on.finish('打不起，打不起，溜了~')
    else:
        await hit_on.finish('打你个蛋蛋！')