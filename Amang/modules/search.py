"""
✅ Edit Code Boleh
❌ Hapus Credits Jangan
👤 Telegram: @T0M1_X
"""
# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import random

from pyrogram.types import InputMediaPhoto

from Amang import *
from Amang.utils import *

__MOD__ = "search"
__HELP__ = f"""
 Document for Search

• Command: <code>{cmd[0]}pic</code> [query]
• Function: Untuk gambar secara limit 5.
"""


@ubot.on_message(filters.command(["pic"], cmd) & filters.me)
async def pic_bing_cmd(client, message):
    TM = await eor(message, "<b>Memproses...</b>")
    if len(message.command) < 2:
        return await TM.edit(f"<code>{pic}</code> [query]")
    x = await client.get_inline_bot_results(
        message.command[0], message.text.split(None, 1)[1]
    )
    get_media = []
    for X in range(5):
        try:
            saved = await client.send_inline_bot_result(
                client.me.id, x.query_id, x.results[random.randrange(30)].id
            )
            saved = await client.get_messages(
                client.me.id, int(saved.updates[1].message.id)
            )
            get_media.append(InputMediaPhoto(saved.photo.file_id))
            await saved.delete()
        except:
            await TM.edit(f"<b>❌ Image Photo Ke {X} Tidak Ditemukan</b>")
    await client.send_media_group(
        message.chat.id,
        get_media,
        reply_to_message_id=message.id,
    )
    await TM.delete()


@ubot.on_message(filters.command(["gif"], cmd) & filters.me)
async def gif_cmd(client, message):
    if len(message.command) < 2:
        return await eor(message, f"<code>{gif}</code> [query]")
    TM = await eor(message, "<b>Memproses...</b>")
    x = await client.get_inline_bot_results(
        message.command[0], message.text.split(None, 1)[1]
    )
    try:
        saved = await client.send_inline_bot_result(
            client.me.id, x.query_id, x.results[random.randrange(30)].id
        )
    except:
        await Tm.edit("<b>❌ Gif tidak ditemukan</b>")
        await TM.delete()
    saved = await client.get_messages(client.me.id, int(saved.updates[1].message.id))
    await client.send_animation(
        message.chat.id, saved.animation.file_id, reply_to_message_id=message.id
    )
    await TM.delete()
    await saved.delete()
