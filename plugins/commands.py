import asyncio, os, sys

from pyrogram import Client, filters, enums


@Client.on_message(filters.command('start') & filters.private & filters.user('self'))
async def check_alive(c, m):
    await m.reply(f"{m.from_user.first_name}", quote=True)


@Client.on_message(filters.private & filters.command("restart") & filters.user('self'))
async def restart_bot(b, m):
    await m.reply_text("ʀᴇꜱᴛᴀʀᴛɪɴɢ........")
    os.execl(sys.executable, sys.executable, "bot.py")


@Client.on_message(filters.command("update") & filters.user('self'))
async def update_bot(c, m):
    try:
        os.system("git pull")
        if len(m.command) != 1:
            os.system("pip install -r requirements.txt --force-reinstall")
        await m.reply_text("ᴜᴩᴅᴀᴛᴇᴅ & ʀᴇꜱᴛᴀʀᴛɪɴɢ...")
        os.execl(sys.executable, sys.executable, "bot.py")
    except Exception as e:
        await m.reply(e)


