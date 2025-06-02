import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from config import Config

FORCE_SUB_CHANNELS = Config.FORCE_SUB_CHANNELS
IMAGE_URL = "https://files.catbox.moe/c9wg0t.jpg"

async def not_subscribed(_, __, message):
    for channel in FORCE_SUB_CHANNELS:
        try:
            user = await message._client.get_chat_member(channel, message.from_user.id)
            if user.status in {"kicked", "left"}:
                return True
        except UserNotParticipant:
            return True
    return False

@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    not_joined_channels = []
    for channel in FORCE_SUB_CHANNELS:
        try:
            user = await client.get_chat_member(channel, message.from_user.id)
            if user.status in {"kicked", "left"}:
                not_joined_channels.append(channel)
        except UserNotParticipant:
            not_joined_channels.append(channel)

    buttons = [
        [
            InlineKeyboardButton(
                text=f"• ᴊᴏɪɴ {channel.capitalize()} •", url=f"https://t.me/{channel}"
            )
        ]
        for channel in not_joined_channels
    ]
    buttons.append(
        [
            InlineKeyboardButton(
                text="• ᴊᴏɪɴᴇᴅ •", callback_data="check_subscription"
            )
        ]
    )

    text = <b>“You haven't yet walked all the paths...<br>
Join the channels if you wish to continue your journey.”</b>
    await message.reply_photo(
        photo=IMAGE_URL,
        caption=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query(filters.regex("check_subscription"))
async def check_subscription(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    not_joined_channels = []

    for channel in FORCE_SUB_CHANNELS:
        try:
            user = await client.get_chat_member(channel, user_id)
            if user.status in {"kicked", "left"}:
                not_joined_channels.append(channel)
        except UserNotParticipant:
            not_joined_channels.append(channel)

    if not not_joined_channels:
        new_text = "ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ ᴀʟʟ ᴛʜᴇ ɴᴇᴄᴇssᴀʀʏ ᴘᴀᴛʜs. ✨ᴛʜᴀɴᴋ ʏᴏᴜ. ɴᴏᴡ, ʏᴏᴜʀ ᴊᴏᴜʀɴᴇʏ ᴄᴏɴᴛɪɴᴜᴇs. 🌿"
        if callback_query.message.caption != new_text:
            await callback_query.message.edit_caption(
                caption=new_text,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("• ɴᴏᴡ ᴄʟɪᴄᴋ ʜᴇʀᴇ •", callback_data='help')]
                ])
            )
    else:
        buttons = [
            [
                InlineKeyboardButton(
                    text=f"• ᴊᴏɪɴ {channel.capitalize()} •",
                    url=f"https://t.me/{channel}",
                )
            ]
            for channel in not_joined_channels
        ]
        buttons.append(
            [
                InlineKeyboardButton(
                    text="• ᴊᴏɪɴᴇᴅ •", callback_data="check_subscription"
                )
            ]
        )

        text = "ʏᴏᴜ'ᴠᴇ ᴊᴏɪɴᴇᴅ ᴀʟʟ ᴛʜᴇ ɴᴇᴄᴇssᴀʀʏ ᴄʜᴀɴɴᴇʟs... ᴛʜᴀɴᴋ ʏᴏᴜ. ᴘʟᴇᴀsᴇ ᴘʀᴏᴄᴇᴇᴅ ᴛᴏ ᴛʜᴇ ᴜᴘᴅᴀᴛᴇs 🌿✨"
        if callback_query.message.caption != text:
            await callback_query.message.edit_caption(
                caption=text,
                reply_markup=InlineKeyboardMarkup(buttons)
            )
