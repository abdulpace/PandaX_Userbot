"""
💐 Commands Available -
• `{i}deez <search query (| flac)>`
    Download songs from Deezer
"""
import os
import time
from json.decoder import JSONDecodeError
from urllib.request import urlretrieve

import requests as r
from telethon.tl.types import DocumentAttributeAudio

from . import *


@ilhammansiz_cmd(
    pattern="deez ?(.*)",
)
async def siesace(e):
    song = e.pattern_match.group(1)
    if not song:
        return await eod(e, "Give me Something to Search")
    quality = "mp3"
    if "| flac" in song:
        try:
            song = song.split("|")[0]
            quality = "flac"
        except Exception as ex:
            await eod(e, f"`{str(ex)}`")
    hmm = time.time()
    lol = await eor(e, "`Searching on Deezer...`")
    sung = song.replace(" ", "%20")
    url = f"https://jostapi.herokuapp.com/deezer?query={sung}&quality={quality}&count=1"
    try:
        k = (r.get(url)).json()[0]
    except IndexError:
        return await eod(lol, "`Song Not Found.. `")
    except JSONDecodeError:
        return await eod(
            lol, f"`Tell `[sɪᴘᴀᴋ](tg://user?id=1303895686)`to turn on API.`"
        )
    try:
        title = k["title"]
        urrl = k["raw_link"]
        img = k["album"]["cover_xl"]
        duration = k["duration"]
        singers = k["artist"]["name"]
    except Exception as ex:
        return await eod(lol, f"`{str(ex)}`")
    urlretrieve(urrl, title + "." + quality)
    urlretrieve(img, title + ".jpg")
    okk = await uploader(
        title + "." + quality,
        title + "." + quality,
        hmm,
        lol,
        "Uploading " + title + "...",
    )
    await petercordpanda_bot.send_file(
        e.chat_id,
        okk,
        caption="`" + title + "`" + "\n`From Deezer`",
        attributes=[
            DocumentAttributeAudio(
                duration=int(duration),
                title=title,
                performer=singers,
            )
        ],
        supports_streaming=True,
        thumb=title + ".jpg",
    )
    await lol.delete()
    os.remove(title + "." + quality)
    os.remove(title + ".jpg")
