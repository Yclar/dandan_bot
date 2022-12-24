from asyncio import sleep
from nonebot.adapters import Message
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.params import CommandArg, ArgPlainText
from nonebot import logger
from httpx import AsyncClient


music = on_command("音乐", rule=to_me(), priority=5, block=True)


@music.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("type", args)


@music.got("type", prompt="你想要听什么歌？")
async def handle_music(typek: str = ArgPlainText("type")):
    if not typek:
        await music.reject("我没有听说过空白的歌哦~")
    else:
        await music.send("蛋蛋正在查询中……")
        async with AsyncClient() as client:
            try:
                url = 'https://api.ayano.top/music/index.php?api=search&music=netease&search=' + str(typek)
                r = await client.get(url=url, timeout=None)
                print(r.json())
                music_url = r.json()[0]['id']
                global lyc
                lyc = r.json()[0]['lyric']
            except Exception as e:
                logger.error(f' {type(e)}：{e}')
                await music.finish('没有查到相关曲目呢...')
        await music.send(message=MessageSegment.music(type_="163", id_=int(music_url)))
        await sleep(1)
        await music.send('请问需要歌词吗？（如果需要请回复“是”，否则就回复其他的）')


@music.got("ans")
async def get_ans(answer: str = ArgPlainText("ans")):
    if answer.strip() == "是":
        print(1)
        await music.send(lyc)
    await music.finish()