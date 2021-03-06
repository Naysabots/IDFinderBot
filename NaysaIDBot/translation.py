from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
๐ Hey {} โก \n
I am Telegram Simple Bot For Finding IDs\n
Use Help Command to Know How to Use me\n
Maintained By : [Tellybots](t.me/tellybots)\n
"""

    HELP_TEXT = """
  โฎ Forward A Message From Any Group To Get Group ID

  โฎ Forward Me A Message From Any Channel To Get Channel ID

  โฎ Sent /ID To Get Telegram ID

  โฎ Click /Info To  Get Telegram INFO 
"""

    ABOUT_TEXT = """
๐ค My Name : <a href='https://t.me/{}'>NaysaIDFinderBot</a>\n
  
๐ Language : <a href='https://www.python.org/'>Python3</a>\n

๐ Library : <a href='https://github.com/pyrogram/pyrogram'>Pyrogram</a>\n

๐ดโโ๏ธ Developer : <a href='t.me/{}'>@Tellybots</a>\n

"""

    JOIN_TEXT = """
๐ข Plz Join My Update Channel To Use Me
"""
 
    TRY_TEXT = """
๐ Restart Now ๐
"""

    FSUB_TEXT = """
๐ข Join My Update Channel To Use Me
"""

    ID_TEXT = """
๐ Your Telegram ID ๐ข๐ฌ :- <code>{}</code>
"""

    INFO_TEXT = """
 ๐ซ Telegram Information

 ๐คน First Name : <b>{}</b>

 ๐ดโโ๏ธ Second Name : <b>{}</b>

 ๐ง๐ปโ๐ Username : <b>@{}</b>

 ๐ Telegram Id : <code>{}</code>

 ๐ Profile Link : <b>{}</b>

 ๐ก Dc : <b>{}</b>

 ๐ Language : <b>{}</b>

 ๐ฒ Status : <b>{}</b>
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('๐ก๏ธ Update', url='https://telegram.me/tellybots'),
        InlineKeyboardButton('๐ฐ Support', url='https://telegram.me/tellybots_support')
        ],[
        InlineKeyboardButton('โ Help', callback_data='help'),
        InlineKeyboardButton('โจ๏ธ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('๐ก Home', callback_data='home'),
        InlineKeyboardButton('๐จโ๐ About', callback_data='about'),
        InlineKeyboardButton('โจ๏ธ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('๐ก Home', callback_data='home'),
        InlineKeyboardButton('โ Help', callback_data='help'),
        InlineKeyboardButton('โจ๏ธ Close', callback_data='close')
        ]]
    )

