import os, sys, asyncio, logging, time
from datetime import timedelta, date, datetime 
from pyrogram import Client, filters, enums
from pyrogram.errors import InputUserDeactivated, FloodWait, UserIsBlocked, PeerIdInvalid

logger = logging.getLogger(__name__)


async def broadcast_messages(user_id, message):
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
        
        
def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

def get_time(seconds):
    periods = [('ᴅ', 86400), ('ʜ', 3600), ('ᴍ', 60), ('ꜱ', 1)]
    result = ''
    for period_name, period_seconds in periods:
        if seconds >= period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            result += f'{int(period_value)}{period_name}'
    return result        
        
        
def get_date(days):
    today = date.today()
    ex_date = today + timedelta(days=int(days))
    pattern = '%Y-%m-%d'
    epcho = int(time.mktime(time.strptime(str(ex_date), pattern)))
    normal_date = datetime.fromtimestamp(epcho).strftime('%B-%d-%Y')
    return normal_date
        
        