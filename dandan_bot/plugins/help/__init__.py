# coding=gbk
from nonebot import on_command
from nonebot.rule import to_me


help = on_command("����", rule=to_me(), priority=2, aliases={"help"}, block=True)


@help.handle()
async def send_help():
    await help.finish('������~�����кÿ���Ӵ~��ָʹ���ֲᣩ\n https://www.showdoc.com.cn/dandanyexio/9108972224334355')