from pyrogram import filters
from pyrogram import Client as NaysaBots
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import UserNotParticipant
from NaysaIDBot.Translation import Translation
from NaysaIDBot.config import Config



@NaysaBots.on_message(filters.private & filters.command("id"))
async def id_handler(bot, update):

    
    await update.reply_text(        
        text=Translation.ID_TEXT.format(update.from_user.id),
        disable_web_page_preview=True    
    )

@NaysaBots.on_message(filters.private & filters.command("info"))
async def info_handler(bot, update):


    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "None"

  
    await update.reply_text(  
        text=Translation.INFO_TEXT.format(update.from_user.first_name, last_name, update.from_user.username, update.from_user.id, update.from_user.mention, update.from_user.dc_id, update.from_user.language_code, update.from_user.status),             
        disable_web_page_preview=True
    )
