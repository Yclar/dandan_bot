#coding=gbk
from nonebot import on_command
from nonebot.rule import to_me


help = on_command("��", rule=to_me(), priority=5, aliases={"ֻ��","����","��","��","��","þ"}, block=True)


@help.handle()
async def send_help():
    await help.finish('�����������������ϡ���')