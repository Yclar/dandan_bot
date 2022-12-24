# coding=utf-8
from nonebot.adapters.onebot.v11 import Message
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.params import State, CommandArg
from . import phigros


song_diff = on_command("查定数", aliases={'song_diff', 'ssd'}, rule=to_me(), priority=5, block=True)


@song_diff.handle()
async def first_handle_receive(args: Message = CommandArg(), state: T_State = State()):
    plain_text = args.extract_plain_text()
    if plain_text:
        state["game_type"] = plain_text


@song_diff.got("game_type", prompt="请问是哪个音游的定数呢？\n现在可选：\nPhigros\nArcaea")
async def get_song(state: T_State = State()):
    game_type = str(state["game_type"]).strip().title()
    if game_type == 'Phigros':
        await song_diff.finish("功能升级中")
        #await song_diff.send('请输入歌曲名称')
    elif game_type == 'Arcaea':
        await song_diff.finish('请使用Arcaea插件（输入arc help查看帮助）')
    else:
        print(game_type)
        await song_diff.finish("不支持或不存在这个游戏哦~")


@song_diff.got("song")
async def get_level(state: T_State = State()):
    song_name = str(state["song"]).strip().title()
    game_type = str(state["game_type"]).strip().title()
    if game_type == 'Phigros':
        ret = await phigros.get(song_name)
        if ret != 'baka':
            await song_diff.send('请输入歌曲难度（EZ/HD/IN/AT）')
        else:
            await song_diff.send('这是某首曲子的别名吗？如果是的话请输入"是"，否则就输入别的~')


@song_diff.got("level")
async def get_diff(state: T_State = State()):
    song_name = str(state["song"]).strip().title()
    game_type = str(state["game_type"]).strip().title()
    level = str(state["level"]).strip().title()
    if game_type == 'Phigros':
        ret = (await phigros.get(song_name)).split('#')
        print(ret)
        if ret[0] == 'baka':
            if level == '是':
                await song_diff.send('是哪首曲子呢？（请输入完整名称）')
            else:
                await song_diff.finish('蛋蛋尽力了，真的没有这首曲子QAQ')
        else:
            a = []
            for i in ret:
                if i == '@':
                    print(a)
                    if str(a[0]).title() == level:
                        msg0 = '曲名：' + str(a[4]) + '\n'
                        msg1 = '难度为' + str(a[0]) + '时：\n'
                        msg2 = '定数为' + str(a[1]) + '，'
                        msg3 = '物量为' + str(a[2]) + '，'
                        msg4 = '加入版本为' + str(a[3])
                        await song_diff.finish(msg0 + msg1 + msg2 + msg3 + msg4)
                    a = []
                else:
                    a.append(i)
            await song_diff.finish('蛋蛋尽力了，真的没有这个难度QAQ')


@song_diff.got("name")
async def get_name(state: T_State = State()):
    alias = str(state["song"]).strip().title()
    game_type = str(state["game_type"]).strip().title()
    name = str(state["name"]).strip()
    if game_type == 'Phigros':
        ret = await phigros.alias_(alias, name)
        if ret == 'baka':
            await song_diff.finish('蛋蛋尽力了，真的没有这首曲子QAQ')
        else:
            await song_diff.finish('别名添加成功！')