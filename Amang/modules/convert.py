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

• Command: <code>{cmd[0]}toimg</code> [balas stikers]
• Function: Untuk membuat nya menjadi foto.

• Command: <code>{cmd[0]}efek</code> [efek_code - reply to voice note]
• Function: Untuk mengubah suara voice note.

<b>efek_code:</b>  <code>bengek</code> <code>robot</code> <code>jedug</code> <code>fast</code> <code>echo</code>
"""


@ubot.on_message(filters.me & filters.command("mp3", cmd))
async def _(client, message):
    replied = message.reply_to_message
    Tm = await eor(message, "<b>wait a sec. . .</b>")
    if not replied:
        await Tm.edit("<b>mohon reply ke video</b>")
        return
    if replied.media == MessageMediaType.VIDEO:
        await Tm.edit("<b>downloading video . . .</b>")
        file = await client.download_media(
            message=replied,
            file_name="song",
        )
        out_file = file + ".mp3"
        try:
            await Tm.edit("<b>mengekstrak audio. . .</b>")
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
        await Tm.edit("<b>reply vid nya goblok</b>")
        return

@ubot.on_message(filters.me & filters.command("vn", cmd))
async def _(client, message):
    replied = message.reply_to_message
    Tm = await eor(message, "<b>wait a sec. . .</b>")
    if not replied:
        await Tm.edit("<b>reply file nya tod</b>")
        return
    if replied.media == MessageMediaType.AUDIO:
        await Tm.edit("<b>downloading audio</b>")
        file = await client.download_media(
            message=replied,
        )
        out_file = ".opus"
        try:
            await Tm.edit("<b>mengconvert pesan suara. . .</b>")
            cmd = f"ffmpeg -i {file} -map 0:a -codec:a libopus -b:a 100k -vbr on {out_file}"
            await run_cmd(cmd)
            await client.send_voice(
                message.chat.id,
                voice=out_file,
                reply_to_message_id=message.id,
            )
            await Tm.delete()
        except BaseException as e:
            await Tm.edit(f"<b>INFO:</b> {e}")
    else:
        await Tm.edit("<b>reply file nya tod</b>")
        return
