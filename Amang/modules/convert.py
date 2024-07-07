import asyncio
import os
from io import BytesIO

from pyrogram import filters
from pyrogram.enums import MessageMediaType
from pyrogram.raw.functions.messages import DeleteHistory

from Amang import *
from Amang.config import *
from Amang.utils import eor, run_cmd

__MOD__ = "convert"
__HELP__ = f"""
 Document for Convert

• Command: <code>{cmd[0]}toaudio</code> [reply to video]
• Function: Untuk merubah video menjadi audio mp3.
           
• Command: <code>{cmd[0]}toanime</code> [reply to photo]
• Function: Untuk merubah foto menjadi anime.

• Command: <code>{cmd[0]}toimg</code> [balas stikers]
• Function: Untuk membuat nya menjadi foto.

• Command: <code>{cmd[0]}efek</code> [efek_code - reply to voice note]
• Function: Untuk mengubah suara voice note.

<b>efek_code:</b>  <code>bengek</code> <code>robot</code> <code>jedug</code> <code>fast</code> <code>echo</code>
"""


@ubot.on_message(filters.me & filters.command("toanime", cmd))
async def _(client, message):
    Tm = await eor(message, "<b>wait a sec...</b>")
    if message.reply_to_message:
        if len(message.command) < 2:
            if message.reply_to_message.photo:
                type = "Foto"
                get_photo = message.reply_to_message.photo.file_id
            if message.reply_to_message.sticker:
                type = "Stiker"
            if message.reply_to_message.animation:
                type = "Animasi"
            path = await client.download_media(message.reply_to_message)
            with open(path, "rb") as f:
                content = f.read()
            os.remove(path)
            get_photo = BytesIO(content)
        else:
            if message.command[1] in ["foto", "profil", "photo"]:
                chat = (
                    message.reply_to_message.from_user
                    or message.reply_to_message.sender_chat
                )
                type = "Foto"
                get = await client.get_chat(chat.id)
                photo = get.photo.big_file_id
                get_photo = await client.download_media(photo)
    else:
        if len(message.command) < 2:
            return await Tm.edit(
                "Balas ke foto dan saya akan merubah foto anda menjadi anime"
            )
        else:
            type = "Foto"
            get = await client.get_chat(message.command[1])
            photo = get.photo.big_file_id
            get_photo = await client.download_media(photo)
    await client.unblock_user("@qq_neural_anime_bot")
    Tm_S = await client.send_photo("@qq_neural_anime_bot", get_photo)
    await Tm.edit("<b>Sedang diproses...</b>")
    await Tm_S.delete()
    await asyncio.sleep(30)
    async for anime in client.search_messages("@qq_neural_anime_bot"):
        try:
            if anime.photo:
                await client.copy_media_group(
                    message.chat.id,
                    "@qq_neural_anime_bot",
                    anime.id,
                    captions=[f"@{bot.me.username}", f"@{bot.me.username}"],
                    reply_to_message_id=message.id,
                )
                await Tm.delete()
            elif "Failed" in anime.text:
                await Tm.edit(anime.text)
            elif "You're" in anime.text:
                await Tm.edit(anime.text)
        except:
            await Tm.edit(
                f"<b>Gagal merubah {type} menjadi anime,\nSilahkan ulangi beberapa saat lagi</b>"
            )
        user_info = await client.resolve_peer("@qq_neural_anime_bot")
        return await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))


@ubot.on_message(filters.me & filters.command("toaudio", cmd))
async def _(client, message):
    replied = message.reply_to_message
    Tm = await eor(message, "<b>wait a sec. . .</b>")
    if not replied:
        await Tm.edit("<b>mohon reply ke video</b>")
        return
    if replied.media == MessageMediaType.VIDEO:
        await Tm.edit("<b>Downloading Video . . .</b>")
        file = await client.download_media(
            message=replied,
            file_name="logs/",
        )
        out_file = file + ".mp3"
        try:
            await Tm.edit("<b>Mencoba Ekstrak Audio. . .</b>")
            cmd = f"ffmpeg -i {file} -q:a 0 -map a {out_file}"
            await run_cmd(cmd)
            await Tm.edit("<b>Uploading Audio . . .</b>")
            await client.send_audio(
                message.chat.id,
                audio=out_file,
                reply_to_message_id=message.id,
            )
            await Tm.delete()
        except BaseException as e:
            await Tm.edit(f"<b>INFO:</b> {e}")
    else:
        await Tm.edit("<b>Mohon Balas Ke Video</b>")
        return

@ubot.on_message(filters.me & filters.command("vn", cmd))
async def makevoice(event):
    if not event.reply_to:
        return await eor(event, "**Reply ke media video atau suara dulu tod..**")
    msg = await event.reply_to_message()
    if not event.edit or not (msg.audio or msg.video):
        return await eor(event, "**Lu reply ke pesan atau audio dulu tolol..**")
    xxnx = await eor(event, "`Bentar tod...`")
    dl = msg.file.name
    file = await msg.download_media(dl)
    await xxnx.edit("`Sedang mengconvert Pesan Suara...`")
    await run_cmd(
        f"ffmpeg -i '{file}' -map 0:a -codec:a libopus -b:a 100k -vbr on man.opus"
    )
    await event.client.send_message(
        event.chat_id, file="ram.opus", force_document=False, reply_to=msg
    )
    await xxnx.delete()
    os.remove(file)
    os.remove("ram.opus")
