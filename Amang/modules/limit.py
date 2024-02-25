from asyncio import sleep

from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from Amang import *
from Amang.utils import *


@ubot.on_message(filters.command("limit", cmd) & filters.me)
async def _(client, message):
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    msg = await eor(message, "<code>Processing . . .</code>")
    response = await client.invoke(
        StartBot(
            bot=bot_info,
            peer=bot_info,
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    await sleep(1)
    status = await client.get_messages("SpamBot", response.updates[1].message.id + 1)
    await msg.edit(status.text)
    return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))


__MOD__ = "limit"
__HELP__ = f"""
 Document for Limited

• Command: <code>{cmd[0]}limit</code>
• Function: Untuk mengecek akun anda terbatas atau tidak.
"""
