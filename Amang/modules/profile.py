# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import os
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from Amang import *
from Amang.config import *
from Amang.utils.utils import *

__MOD__ = "profile"
__HELP__ = f"""
 Document for Profile

• Command: <code>{cmd[0]}setgpic</code> [balas media]
• Function: Untuk mengubah foto grup.

• Command: <code>{cmd[0]}setbio</code> [query]
• Function: Untuk mengubah bio Anda.

• Command: <code>{cmd[0]}setname</code> [query]
• Function: Untuk mengubah Nama Anda.

• Command: <code>{cmd[0]}setpp</code> [balas media]
• Function: Untuk mengubah Foto Akun Anda.

• Command: <code>{cmd[0]}block</code> [balas pengguna]
• Function: Untuk blokir pengguna.

• Command: <code>{cmd[0]}unblock</code> [query]
• Function: Untuk buka blokir pengguna.
"""


@ubot.on_message(filters.command(["unblock"], cmd) & filters.me)
async def unblock_user_func(client, message):
    user_id = await extract_user(message)
    tex = await eor(message, "<code>Processing . . .</code>")
    if not user_id:
        return await eor(
            message, "Berikan username atau reply pesan untuk membuka blokir."
        )
    if user_id == client.me.id:
        return await tex.edit("Ok done ✅.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await eor(message, f"<b>Berhasil membuka blokir</b> {umention}")


@ubot.on_message(filters.command(["block"], cmd) & filters.me)
async def block_user_func(client, message):
    user_id = await extract_user(message)
    tex = await eor(message, "<code>Processing . . .</code>")
    if not user_id:
        return await eor(message, "Berikan username untuk di blok.")
    if user_id == client.me.id:
        return await tex.edit("Ok ✅.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"<b>Berhasil MemBlokir</b> {umention}")


@ubot.on_message(filters.command(["setname"], cmd) & filters.me)
async def setname(client: Client, message: Message):
    tex = await eor(message, "<code>Processing . . .</code>")
    if len(message.command) == 1:
        return await tex.edit("Berikan text untuk diatur sebagai nama anda.")
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(
                f"<b>Berhasil mengganti nama menjadi</b> <code>{name}</code>"
            )
        except Exception as e:
            await tex.edit(f"<b>ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit("Berikan text untuk diatur sebagai nama anda.")


@ubot.on_message(filters.command(["setbio"], cmd) & filters.me)
async def set_bio(client: Client, message: Message):
    tex = await eor(message, "<code>Processing . . .</code>")
    if len(message.command) == 1:
        return await tex.edit("Berikan text untuk diatur sebagai bio.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"<b>Berhasil mengganti bio menjadi</b> <code>{bio}</code>")
        except Exception as e:
            await tex.edit(f"<b>ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit("Berikan text untuk diatur sebagai bio.")


@ubot.on_message(filters.command(["setpp"], cmd) & filters.me)
async def set_pfp(client, message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo_or_video
            or (
                replied.document
                and "image" in replied.document.mime_type
                or "video" in replied.document.mime_type
            )
        )
    ):
        profile_photo = "pfp.jpg"
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await eor(message, "<b>Foto profil berhasil di ganti.</b>")
    else:
        await eor(message, "Balas ke media untuk atur sebagai foto profil")
        await sleep(3)
        await message.delete()
