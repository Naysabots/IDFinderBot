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


@NaysaBots.on_message(filters.private & filters.forwarded)
async def info(bot, message):

    if message.forward_from:
        text = "Bot Info 👀 \n\n"
        if message.forward_from["is_bot"]:
            text += "🤖 Forward Info"
        else:
            text += "👤User Info"
        text += f'\n\n👨‍💼 Name : {message.forward_from["first_name"]}'
        if message.forward_from["username"]:
            text += f'\n\n🔗 Username : @{message.forward_from["username"]} \n\n🆔 ID : <code>{message.forward_from["id"]}</code>'
        else:
            text += f'\n\n🆔 ID : `{message.forward_from["id"]}`'
        await message.reply(text, quote=True)
    else:
        hidden = message.forward_sender_name
        if hidden:
            await message.reply(
                f"❌️Error {hidden} ❌️Error",
                quote=True,
            )
        else:
            text = f"Forward Information\n\n"
            if message.forward_from_chat["type"] == "channel":
                text += "📢 Channel"
            if message.forward_from_chat["type"] == "supergroup":
                text += "💬 Group"
            text += f'\n\n📃 Name {msg.forward_from_chat["title"]}'
            if message.forward_from_chat["username"]:
                text += f'\n\n➡️ From : @{message.forward_from_chat["username"]}'
                text += f'\n\n🆔 ID : `{message.forward_from_chat["id"]}`'
            else:
                text += f'\n\n🆔 ID `{message.forward_from_chat["id"]}`\n\n'
            await message.reply(text, quote=True)
