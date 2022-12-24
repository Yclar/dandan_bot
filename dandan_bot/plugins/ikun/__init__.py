#coding=gbk
from nonebot import on_command
from nonebot.rule import to_me


help = on_command("鸡", rule=to_me(), priority=5, aliases={"只因","酯铟","激","铌","钛","镁"}, block=True)


@help.handle()
async def send_help():
    await help.finish('你干嘛～～～哈哈～哎呦～～')