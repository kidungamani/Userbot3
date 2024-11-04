import time, asyncio, datetime, asyncio, pytz, logging 

from config import Config 
from pyrogram import Client, filters, enums, raw
from pyrogram.errors import FloodWait
from utils import broadcast_messages, get_time

logger = logging.getLogger(__name__)

@Client.on_message(filters.command('broadcast') & filters.reply & filters.private & filters.user('self'))
async def broadcast_none_contact(client, message):
    broadcast_msg = message.reply_to_message
    done = 0
    failed = 0
    success = 0
    sts = await message.reply_text("**ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ꜱᴛᴀʀᴛᴇᴅ ʙᴏᴛ ᴡɪʟʟ ᴜᴘᴅᴀᴛᴇ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴡʜɪʟᴇ. ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ✨**", quote=True)
    start_time = time.time()
    async for dialog in client.get_dialogs():
        if dialog.chat.type != enums.ChatType.PRIVATE: continue
        user = await client.get_users(dialog.chat.id)
        if user.is_contact or user.is_self or user.is_verified: continue
        out = await broadcast_messages(user_id=user.id, message=message.reply_to_message)
        if out: success += 1
        else: 
            failed += 1
            try: await client.invoke(raw.functions.messages.DeleteHistory(peer=await client.resolve_peer(user.id), max_id=0, revoke=True))
            except: pass
        done += 1
        await asyncio.sleep(0.5)
        if done % 20 == 0:  
            try: await sts.edit(f"**!ʙʀᴏᴀᴅᴄᴀꜱᴛ ɪɴ ᴩʀᴏɢʀᴇss:\n\nᴄᴏᴍᴩʟᴇᴛᴇᴅ: `{done}` \nꜱᴜᴄᴄᴇꜱꜱ: `{success}` \nꜰᴀɪʟᴇᴅ: `{failed}`**")    
            except: pass
    await sts.delete()
    await message.reply_text(f"**✓ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴄᴏᴍᴩʟᴇᴛᴇᴅ ɪɴ {get_time(int(time.time() - start_time))}: \n\nᴄᴏᴍᴩʟᴇᴛᴇᴅ: `{done}` \nꜱᴜᴄᴄᴇꜱꜱ: `{success}` \nꜰᴀɪʟᴇᴅ: `{failed}`**", quote=True)    
    

@Client.on_message(filters.command('clear_zombie') & filters.user('self'))
async def clear_zombie(c, m):
    done = 0
    deleted = 0
    start_time = time.time()
    sts = await m.reply('starting....')
    async for dialog in c.get_dialogs():
        if dialog.chat.type != enums.ChatType.PRIVATE: continue
        try:
            user = await c.get_users(dialog.chat.id)
            if user.is_deleted:
                try:
                    await c.invoke(raw.functions.messages.DeleteHistory(peer=await c.resolve_peer(user.id), max_id=0, revoke=True))
                except Exception as e:
                    logger.error(str(e), exc_info=True)
                deleted += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            user = await c.get_users(dialog.chat.id)
            if user.is_deleted:
                try:
                    await c.invoke(raw.functions.messages.DeleteHistory(peer=await c.resolve_peer(user.id), max_id=0, revoke=True))
                except Exception as e:
                    logger.error(str(e), exc_info=True)
                deleted += 1
        done += 1
        if done % 20 == 0:  
            try:
                curr = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                tame = curr.strftime('%I:%M:%S %p')
                await sts.edit(f'In Progress....\ntotal done `{done}`\ndeleted: `{deleted}`\ndate: {date}\ntime: {tame}')
            except:
                pass
    time_taken = datetime.timedelta(seconds=int(time.time() - start_time))
    await sts.reply(f'successful ✅ \ntotal done `{done}`\ndeleted: `{deleted}`\ntaked time {time_taken}')

