import os, sys, asyncio, time, logging, utils
from pyrogram import Client, idle
from config import Config, Color
 

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

CLIENTS = [Client(
    name=f"UserBot-{client_id}",
    session_string=session,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=dict(root="plugins"),                
    app_version=f'KiduUserBot-{client_id}',
) for client_id, session in enumerate(Config.USER_SESSIONS)]


async def start_clients():
    Success = 0
    for _Id, User in enumerate(CLIENTS):     
        try:
            await User.start() 
            logger.info(Color.bold + f"\n\n{Color.green}ᴄʟɪᴇɴᴛ-{_Id} ɪꜱ ꜱᴛᴀʀᴛᴇᴅ ✓\n\n{Color.reset}")
            await User.send_message('self', '**I am Started ✨**')
            Success += 1
        except Exception as e:
            logger.error(Color.bold + f"\n\n{Color.red}Client-{_Id} Is Failed To Start : {e}️\n\n{Color.reset}")    
            if User.is_connected: await User.send_message('self', e)
            continue
        
    if Success == 0:
        await asyncio.sleep(10)
        os.system('git pull')
        os.execl(sys.executable, sys.executable, "bot.py")
    
    await idle()


logger.info("Bot Started ✅")
loop = asyncio.get_event_loop()
loop.run_until_complete(start_clients())

    
    
    
    
    