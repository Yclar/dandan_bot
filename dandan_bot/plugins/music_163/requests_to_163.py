import httpx
from typing import Optional
from nonebot import logger


async def get(music: str)->Optional[str]:
    async with httpx.AsyncClient() as client:
        try:
            url = 'https://api.ayano.top/music/index.php?api=search&music=netease&search=' + str(music)
            r = await client.get(url=url)
            music_url = r.json()[0]['id']
            return music_url
        except Exception as e:
            logger.error(f' {type(e)}：{e}')
            return None