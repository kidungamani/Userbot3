import os, sys, logging, time, asyncio
from pyrogram import Client, filters, enums
from pyrogram.errors import InputUserDeactivated, FloodWait, UserIsBlocked, PeerIdInvalid
from utils import get_time

logger = logging.getLogger(__name__)


@Client.on_message(filters.command("send_message") & (filters.channel | filters.group) & filters.reply)
async def send_message_for_requests(client, message):
    chat_id = message.chat.id
    done = 0
    failed = 0
    success = 0
    skipped = 0
    start_time = time.time()
    
    sts = await message.reply_text("**ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ꜱᴛᴀʀᴛᴇᴅ. ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ ✨**", quote=True)
    
    # Determine how many users to skip
    skip = 0
    if len(message.command) > 1:
        try:
            skip = int(message.command[1])
        except ValueError:
            return await message.reply_text("**Invalid skip value. Please enter a valid number.**", quote=True)
    
    # Iterate over chat join requests
    tasks = []
    async for request in client.get_chat_join_requests(chat_id):
        if skip > 0:
            skip -= 1
            skipped += 1
            done += 1
            continue
        
        user_id = request.user.id
        tasks.append(broadcast_messages(client, message.reply_to_message, user_id))
        done += 1
        if len(tasks) % 10 == 0:  
            results = await asyncio.gather(*tasks)
            tasks = []
            success += results.count(True)
            failed += results.count(False)
            try: await sts.edit(f"**⟳ ꜱᴇɴᴛ ɪɴ ᴩʀᴏɢʀᴇss:\n\nᴄᴏᴍᴩʟᴇᴛᴇᴅ: `{done}` \nꜱᴜᴄᴄᴇꜱꜱ: `{success}` \nꜰᴀɪʟᴇᴅ: `{failed}` \nꜱᴋɪᴩᴩᴇᴅ: `{skipped}`**")
            except: pass
            await asyncio.sleep(2)
        
    await sts.delete()
    await message.reply_text(f"**✓ ꜱᴇɴᴛ ᴄᴏᴍᴩʟᴇᴛᴇᴅ ɪɴ {get_time(int(time.time() - start_time))}: \n\nᴄᴏᴍᴩʟᴇᴛᴇᴅ: `{done}` \nꜱᴜᴄᴄᴇꜱꜱ: `{success}` \nꜰᴀɪʟᴇᴅ: `{failed}` \nꜱᴋɪᴩᴩᴇᴅ: `{skipped}`**", quote=True)


async def broadcast_messages(client, message, user_id):
    try:
        await message.copy(chat_id=user_id)
        return True       
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await broadcast_messages(user_id, message)
    except InputUserDeactivated:
        logger.info(f"{user_id} - Account is deactivated.")
        return False
    except UserIsBlocked:
        logger.info(f"{user_id} - Blocked the bot.")
        return False
    except PeerIdInvalid:
        logger.info(f"{user_id} - Invalid PeerId.")
        return False
    except Exception as e:
        logger.error(f"Error broadcasting to {user_id}: {str(e)}", exc_info=True)
        return False
        
        
