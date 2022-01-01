from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
✮ Hey {}\n
✮ I am Telegram Simple Bot For Finding IDs\n
✮ Use Help Command to Know How to Use me\n
✮ Made With 💕 By @NaysaBots\n
"""

    HELP_TEXT = """
  ✮ Forward A Message From Any Group To Get Group ID

  ✮ Forward Me A Message From Any Channel To Get Channel ID

  ✮ Sent /ID To Get Telegram ID

  ✮ Click /Info To  Get Telegram INFO
"""

    ABOUT_TEXT = """
🤖 My Name : <a href='https://t.me/{}'>NaysaIDFinderBot</a> 
  
📝 Language : <a href='https://www.python.org/'>Python3</a>

📑 Library : <a href='https://github.com/pyrogram/pyrogram'>Pyrogram</a>

🚴‍♂️ Developer : <a href='t.me/{}'>@Tellybots_4u</a>

"""

    JOIN_TEXT = """
📢 Plz Join My Update Channel To Use Me
"""
 
    TRY_TEXT = """
🔃 Restart Now 🔃
"""

    FSUB_TEXT = """
📢 Join My Update Channel To Use Me
"""

    ID_TEXT = """
🆔 Your Telegram ID 𝐢𝐬 :- <code>{}</code>
"""

    INFO_TEXT = """
 💫 Telegram Information

 🤹 First Name : <b>{}</b>

 🚴‍♂️ Second Name : <b>{}</b>

 🧑🏻‍🎓 Username : <b>@{}</b>

 🆔 Telegram Id : <code>{}</code>

 📇 Profile Link : <b>{}</b>

 📡 Dc : <b>{}</b>

 📑 Language : <b>{}</b>

 👲 Status : <b>{}</b>
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Update Channel', url='https://telegram.me/tellybots_4u'),
        InlineKeyboardButton('Support Group', url='https://telegram.me/tellybots_support')
        ],[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )

