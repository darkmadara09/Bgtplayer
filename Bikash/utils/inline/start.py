from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Bikash import config
from Bikash import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✭ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✭",
                url=f"https://t.me/SHALINI_69BOT?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✭ ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs ✭", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✭ ᴜᴘᴅᴀᴛᴇs ✭", url=f"https://t.me/ShaliniMusicBotSh"
            ),
            InlineKeyboardButton(
                text="✭ sᴜᴘᴘᴏʀᴛ ✭", url=f"https://t.me/music_world_sh"
            )
        ],
        [
            InlineKeyboardButton(
                text="Maintainer", url=f"https://t.me/funny" 
  
            )
        ]
     ]
    return buttons



def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✭ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✭",
                url=f"https://t.me/SHALINI_69BOT?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✭ ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs ✭", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✭ ᴜᴘᴅᴀᴛᴇs ✭", url=f"https://t.me/ShaliniMusicBotSh"
            ),
            InlineKeyboardButton(
                text="✭ sᴜᴘᴘᴏʀᴛ ✭", url=f"https://t.me/music_world_sh"
            )
        ],
        [
            InlineKeyboardButton(
                text="Maintainer", url=f"https://t.me/funny" 
            )
        ]
     ]
    return buttons

