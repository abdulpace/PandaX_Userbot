import time
from platform import python_version, uname

from telethon import version

from Panda import StartTime, pandaub, pandaversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id

CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "🐼 BOT PANDA SUCCESSFULLY 🐼"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "  🤖 "

# ================= CONSTANT =================
DEFAULTUSER = str(Config.ALIVE_NAME) if Config.ALIVE_NAME else uname().node
# ============================================

plugin_category = "mansiez"

ilhammansizzz = "https://github.com/ilhammansiz/PandaUserbot"
support = "https://t.me/TEAMSquadUserbotSupport"


@pandaub.ilhammansiz_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if Config.ALIVE_PIC:
        panda_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        panda_caption += f"**🐼 PANDA USERBOT 🐼** \n"
        panda_caption += f"┏━━━━━━━━━━━━━━━━━\n"
        panda_caption += f"┣|⚡ `Pengguna :` {DEFAULTUSER}\n"
        panda_caption += f"┣|⚡ `Simbol   :`  🐼\n"
        panda_caption += f"┣|⚡ `Telethon :` Ver {version.__version__}\n"
        panda_caption += f"┣|⚡ `Python   :` Ver {python_version()}\n"
        panda_caption += f"┣|⚡ `Branch   :` {Config.UPSTREAM_REPO_BRANCH}\n"
        panda_caption += f"┣|⚡ `Bot Ver  :` {pandaversion}\n"
        panda_caption += f"┣|⚡ `Sudo     :` {Config.SUDO_ENABLED}\n"
        panda_caption += f"┗━━━━━━━━━━━━━━━━━ \n"
        await event.client.send_file(
            event.chat_id, Config.ALIVE_PIC, caption=panda_caption, reply_to=reply_to_id
        )
        await event.delete()
    else:
        await event.delete()
        return
        await edit_or_reply(
            event,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"**🐼 PANDA USERBOT 🐼** \n"
            f"┏━━━━━━━━━━━━━━━━━ \n"
            f"┣|⚡ `Pengguna :` {DEFAULTUSER}\n"
            f"┣|⚡ `Simbol   :` 🐼\n"
            f"┣|⚡ `Telethon :` Ver {version.__version__}\n"
            f"┣|⚡ `Python   :` Ver {python_version()}\n"
            f"┣|⚡ `Branch   :` {Config.UPSTREAM_REPO_BRANCH}\n"
            f"┣|⚡ `Bot Ver  :` {pandaversion}\n"
            f"┣|⚡ `Sudo     :` {Config.SUDO_ENABLED}\n"
            f"┗━━━━━━━━━━━━━━━━━ \n",
        )
