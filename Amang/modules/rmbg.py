import os

from pyrogram import filters
from pyrogram.types import *
from removebg import RemoveBg

from Amang import *
from Amang.config import *
from Amang.utils import *

RMBG_API = os.environ.get("RMBG_API", "4n9xEHXQSZ34sPv4wBZ3H8cw")

DOWN_PATH = "dowloads/"

IMG_PATH = DOWN_PATH + "ubot.jpg"

__MOD__ = "remove bg"
__HELP__ = f"""
 Document for RemoveBG

• Command: <code>{cmd[0]}rbg</code> [reply to photo]
• Function: Untuk menghapus background dari foto.
"""


@ubot.on_message(filters.me & filters.command("rbg", cmd))
async def remove_bg(client, message):
    if not RMBG_API:
        return
    Tm = await eor(message, "Processing...")
    replied = message.reply_to_message
    if replied.photo or replied.document or replied.sticker or replied.animation:
        if os.path.exists(IMG_PATH):
            os.remove(IMG_PATH)
        await client.download_media(message=replied, file_name=IMG_PATH)
        await Tm.edit("Removing Background...")
        try:
            rmbg = RemoveBg(RMBG_API, "rm_bg_error.log")
            rmbg.remove_background_from_img_file(IMG_PATH)
            remove_img = IMG_PATH + "_no_bg.png"
            await client.send_photo(
                chat_id=message.chat.id,
                photo=remove_img,
                reply_to_message_id=message.id,
                disable_notification=True,
            )
            await Tm.delete()
        except Exception as e:
            print(e)
            await Tm.edit("Telah terjadi suatu kesalahan!.")
    else:
        await Tm.edit("Usage: Mohon reply ke gambar yang ingin dihapus backgroundnya!")
