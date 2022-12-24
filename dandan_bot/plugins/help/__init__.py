# coding=gbk
from nonebot import on_command
from nonebot.rule import to_me


help = on_command("帮助", rule=to_me(), priority=2, aliases={"help"}, block=True)


@help.handle()
async def send_help():
    await help.finish('来来来~这里有好康的哟~（指使用手册）\n https://www.showdoc.com.cn/dandanyexio/9108972224334355')