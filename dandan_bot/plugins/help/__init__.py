# coding=gbk
from nonebot.adapters.onebot.v11 import MessageSegment, Event
from nonebot import on_command
from nonebot.rule import to_me


help = on_command("����", rule=to_me(), priority=1, aliases={"help"})


@help.handle()
async def send_help():
    await help.finish('������~�����кÿ���Ӵ~��ָʹ���ֲᣩ\n https://www.showdoc.com.cn/dandanyexio/9108972224334355')