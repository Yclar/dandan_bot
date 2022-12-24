from nonebot.rule import to_me
from nonebot import on_message, on_request
from nonebot.adapters import Event, Bot

async def waht_checker(event: Event):
    return str(event.sub_type) == 'group'

wahttttt = on_message(rule = waht_checker, priority=1, block=True)
waht = on_message(rule = to_me(), priority=114514)
auto_accept = on_request(priority=1)

@waht.handle()
async def send_waht(bot: Bot):
    await waht.finish('这是什么啊？是什么暗号吗？我不懂欸~')

@wahttttt.handle()
async def send_wahttttt():
    await wahttttt.finish('你还不是蛋蛋的好友哦~ (验证问题答案为 whvwlib )')
'''
@auto_accept.handle()
async def accept(event: Event, bot: Bot):
    print(event.comment[11:])
    if str(event.comment)[11:] == 'whvwlib':
        print(1)
        await bot.set_friend_add_request(flag=str(event.flag))
'''