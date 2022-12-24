#coding=gbk
from nonebot.adapters.onebot.v11 import Message
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.params import State, CommandArg
from . import phigros


song_diff = on_command("�鶨��", aliases={'song_diff', 'ssd'}, rule=to_me(), priority=5, block=True)


@song_diff.handle()
async def first_handle_receive(args: Message = CommandArg(), state: T_State = State()):
    plain_text = args.extract_plain_text()
    if plain_text:
        state["game_type"] = plain_text


@song_diff.got("game_type", prompt="�������ĸ����εĶ����أ�\n���ڿ�ѡ��\nPhigros\nArcaea")
async def get_song(state: T_State = State()):
    game_type = str(state["game_type"]).strip().title()
    if game_type == 'Phigros':
        await song_diff.finish("����������")
        #await song_diff.send('�������������')
    elif game_type == 'Arcaea':
        await song_diff.finish('��ʹ��Arcaea���������arc help�鿴������')
    else:
        print(game_type)
        await song_diff.finish("��֧�ֻ򲻴��������ϷŶ~")


@song_diff.got("song")
async def get_level(state: T_State = State()):
    song_name = str(state["song"]).strip().title()
    game_type = str(state["game_type"]).strip().title()
    if game_type == 'Phigros':
        ret = await phigros.get(song_name)
        if ret != 'baka':
            await song_diff.send('����������Ѷȣ�EZ/HD/IN/AT��')
        else:
            await song_diff.send('����ĳ�����ӵı���������ǵĻ�������"��"�������������~')


@song_diff.got("level")
async def get_diff(state: T_State = State()):
    song_name = str(state["song"]).strip().title()
    game_type = str(state["game_type"]).strip().title()
    level = str(state["level"]).strip().title()
    if game_type == 'Phigros':
        ret = (await phigros.get(song_name)).split('#')
        print(ret)
        if ret[0] == 'baka':
            if level == '��':
                await song_diff.send('�����������أ����������������ƣ�')
            else:
                await song_diff.finish('���������ˣ����û����������QAQ')
        else:
            a = []
            for i in ret:
                if i == '@':
                    print(a)
                    if str(a[0]).title() == level:
                        msg0 = '������' + str(a[4]) + '\n'
                        msg1 = '�Ѷ�Ϊ' + str(a[0]) + 'ʱ��\n'
                        msg2 = '����Ϊ' + str(a[1]) + '��'
                        msg3 = '����Ϊ' + str(a[2]) + '��'
                        msg4 = '����汾Ϊ' + str(a[3])
                        await song_diff.finish(msg0 + msg1 + msg2 + msg3 + msg4)
                    a = []
                else:
                    a.append(i)
            await song_diff.finish('���������ˣ����û������Ѷ�QAQ')


@song_diff.got("name")
async def get_name(state: T_State = State()):
    alias = str(state["song"]).strip().title()
    game_type = str(state["game_type"]).strip().title()
    name = str(state["name"]).strip()
    if game_type == 'Phigros':
        ret = await phigros.alias_(alias, name)
        if ret == 'baka':
            await song_diff.finish('���������ˣ����û����������QAQ')
        else:
            await song_diff.finish('������ӳɹ���')