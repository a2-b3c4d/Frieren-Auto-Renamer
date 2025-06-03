from pyrogram import Client, filters
from helper.database import codeflixbots

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
        return await message.reply_text(
            "**…You forgot to include the caption.**\n\n"
            "_Try this:_\n"
            "`/set_caption 📕 Name ➠ : {filename}\n\n🔗 Size ➠ : {filesize}\n\n⏰ Duration ➠ : {duration}`"
        )
    caption = message.text.split(" ", 1)[1]
    await codeflixbots.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("**I’ve saved your caption… It’s done. ✅**")

@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await codeflixbots.get_caption(message.from_user.id)
    if not caption:
        return await message.reply_text("**There’s nothing here… No caption to delete. ❌**")
    await codeflixbots.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**It’s gone now… Caption deleted. 🗑️**")

@Client.on_message(filters.private & filters.command(['see_caption', 'view_caption']))
async def see_caption(client, message):
    caption = await codeflixbots.get_caption(message.from_user.id)
    if caption:
        await message.reply_text(f"**Here’s what you set…**\n\n`{caption}`")
    else:
        await message.reply_text("**I searched... But there’s no caption yet. ❌**")

@Client.on_message(filters.private & filters.command(['view_thumb', 'viewthumb']))
async def viewthumb(client, message):
    thumb = await codeflixbots.get_thumbnail(message.from_user.id)
    if thumb:
        await client.send_photo(chat_id=message.chat.id, photo=thumb)
    else:
        await message.reply_text("**Your thumbnail… it’s missing. ❌**")

@Client.on_message(filters.private & filters.command(['del_thumb', 'delthumb']))
async def removethumb(client, message):
    await codeflixbots.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("**The memory is cleared. Thumbnail deleted. 🗑️**")

@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    mkn = await message.reply_text("…Saving it. Just a moment.")
    await codeflixbots.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)
    await mkn.edit("**It’s been saved. Thumbnail is set. ✅**")
