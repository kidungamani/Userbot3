import asyncio, os, sys, datetime, pytz, time, re

from utils import get_date
from config import Config 
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait 

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


@Client.on_message(filters.command("link") & filters.private & filters.user('self'))
async def send_link(c, m):
    try:
        id = int(m.text.split(' ', 1)[1])
        chat_id = Config.GROUPS[id]
    except Exception as e:
        return await m.edit(e)
    try:
        link = await c.create_chat_invite_link(int(chat_id), member_limit=1)
    except Exception as e:
        return await m.edit(e)
    await m.edit(f"Here Is Your Link\n\n{link.invite_link}")


@Client.on_message(filters.command("accept") & (filters.channel | filters.group))
async def super_accept(c, m):
    chat_id = m.chat.id
    while True:
        try:
            await c.approve_all_chat_join_requests(chat_id)
        except FloodWait as e:
            asyncio.sleep(e.value)
            await c.approve_all_chat_join_requests(chat_id)
        except Exception as e:
            pass
    await c.send_message(chat_id, "Task Completed ✓")

@Client.on_message(filters.command("expk") & filters.private & filters.user('self'))          
async def expk(c, m):
    try:
        await m.edit(f"""Your Subscription of 🌟Kerala (https://t.me/c/2125433737/10100) Ends Today 😢

Renew now
message now 👍😃""")
    except Exception as e:
        await m.edit(e)

@Client.on_message(filters.command("mention") & filters.private & filters.user('self'))          
async def mention(c, m):
    try:
        await m.edit(f"<a href=tg://user?id={m.chat.id}>{m.chat.full_name}</a>")
    except Exception as e:
        await m.edit(e)

@Client.on_message(filters.command("ifsc") & filters.private & filters.user('self'))          
async def ifsc(c, m):
    try:
        await m.edit(f"""✅𝘼𝘾𝘾𝙊𝙐𝙉𝙏 𝙉𝙐𝙈𝘽𝙀𝙍‼️

𝙉𝘼𝙈𝙀 - JOHNY SIN
𝘼𝘾𝘾 𝙉𝙊 - 39901612117
𝙄𝙁𝙎𝘾 - SBIN0070208
BRANCH - MATTANNUR""")
    except Exception as e:
        await m.edit(e)
        
@Client.on_message(filters.command("add") & filters.private & filters.user('self'))          
async def add_to_contact(c, m):
    try:
        if len(m.command) != 3: return await m.edit('send like  /add 30 name')
        cmd, day, name = m.text.split(' ', 2)
        exp = get_date(int(day))
        title = f"{exp} | {name}"
        await c.add_contact(int(m.chat.id), title)
        await m.delete(True)
    except Exception as e:
        await m.edit(e)
        
@Client.on_message(filters.command("save") & filters.private & filters.user('self'))          
async def save(c, m):
    try:
        await m.edit(f"""Save my CONTACT 

for accessing
🫵🏻 backup group 
🫵🏻 new updates

⚠️If not saved you will be REMOVED⚠️""")
    except Exception as e:
        await m.edit(e)




#send video & photo & audio 


PHOTOS = [
    "https://envs.sh/Tx8.jpg",
    "https://envs.sh/Tx7.jpg",
    "https://envs.sh/Trn.jpg",
    "https://envs.sh/TyS.jpg",
    
    ]
    

VIDEOS = [
    "https://envs.sh/TM3.mp4",
    
    ]
    
    

@Client.on_message(filters.command("photo") & filters.private & filters.user('self'))          
async def photo(c, m):
    try:
        await m.delete()
        for photo in PHOTOS:
            try: await m.reply_photo(photo=photo, view_once=True)
            except: continue
    except Exception as e:
        await m.edit(e)


@Client.on_message(filters.command("video") & filters.private & filters.user('self'))          
async def video(c, m):
    try:
        await m.delete()
        for video in VIDEOS:
            try: await m.reply_video(video=video, ttl_seconds=(1 << 31) - 1)
            except: continue
    except Exception as e:
        await m.edit(e)
        
        
