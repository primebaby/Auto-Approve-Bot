from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Script import text
from config import ADMIN

@Client.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    if query.data == "start":
        await query.message.edit_caption(
            caption=text.START.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('⇆ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ⇆', url="https://telegram.me/QuickAcceptBot?startgroup=true&admin=invite_users")],
                [InlineKeyboardButton('ℹ️ 𝖠𝖻𝗈𝗎𝗍', callback_data='about'),
                 InlineKeyboardButton('📚 𝖧𝖾𝗅𝗉', callback_data='help')],
                [InlineKeyboardButton('⇆ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 ⇆', url="https://telegram.me/QuickAcceptBot?startchannel=true&admin=invite_users")]
            ])
        )

    elif query.data == "help":
        await query.message.edit_caption(
            caption=text.HELP.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('📢 𝖴𝗉𝖽𝖺𝗍𝖾𝗌', url='https://telegram.me/movie_loverzz'),
                 InlineKeyboardButton('💬 𝖲𝗎𝗉𝗉𝗈𝗋𝗍', url='https://telegram.me/mladminbot')],
                [InlineKeyboardButton('↩️ 𝖡𝖺𝖼𝗄', callback_data="start"),
                 InlineKeyboardButton('❌ 𝖢𝗅𝗈𝗌𝖾', callback_data="close")]
            ])
        )

    elif query.data == "about":
        try:
            await query.message.edit_caption(
                caption=text.ABOUT,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton('👨‍💻 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 👨‍💻', url='https://t.me/mladminbot')],
                    [InlineKeyboardButton("↩️ 𝖡𝖺𝖼𝗄", callback_data="start"),
                     InlineKeyboardButton("❌ 𝖢𝗅𝗈𝗌𝖾", callback_data="close")]
                ])
            )
        except Exception as e:
            if "BUTTON_USER_PRIVACY_RESTRICTED" in str(e):
                await query.message.edit_caption(
                    caption=text.ABOUT + "\n\n👨‍💻 Developer: @mladminbot",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("↩️ 𝖡𝖺𝖼𝗄", callback_data="start"),
                         InlineKeyboardButton("❌ 𝖢𝗅𝗈𝗌𝖾", callback_data="close")]
                    ])
                )
            else:
                raise

    elif query.data == "close":
        await query.message.delete()
