# cradit: Tomi Setiawan > @T0M1_X
# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

"""
from pyrogram.enums import MessagesFilter

from Amang import *


@ubot.on_message(filters.me & filters.command(["take"], cmd))
async def _(client, message):
    results = {
        "photo": MessagesFilter.PHOTO,
        "audio": MessagesFilter.AUDIO,
        "video": MessagesFilter.VIDEO,
        "dokumen": MessagesFilter.DOCUMENT,
    }
    TM = await message.reply("Tunggu Sebentar")
    if len(message.command) < 3:
        return await TM.edit(
            f"<code><b>{message.text} from_chat msg_filter msg_limit to_chat</code></b>"
        )
    else:
        if message.command[2] in results:
            msg_ = results[message.command[2]]
        else:
            return await TM.edit(
                f"❌ msg_filter {message.command[2]} tidak bisa diproses\n\n✅ msg_filter yang tersedia adalah: <code>dokumen</code> <code>photo</code> <code>audio</code> <code>video</code>"
            )
    await TM.edit("Sedang Memproses")
    try:
        done = 0
        async for msg in client.search_messages(
            message.command[1], filter=msg_, limit=int(message.command[3])
        ):
            await msg.copy(message.command[4])
            done += 1
            await asyncio.sleep(3)
    except Exception as error:
        return await TM.edit(error)
    await TM.delete()
    return await message.reply(
        f"✅ {done}/{message.command[3]} {message.command[2]} telah berhasil diambil"
    )


__MOD__ = "take"
__HELP__ = f"
 Document for Take

• Command: <code>{cmd[0]}take</code> [foto/video][jumlah][username grup(contoh : amwangsupport)]
• Function: Mengambil Pesan Dari Grup/Channel.
"
"""
