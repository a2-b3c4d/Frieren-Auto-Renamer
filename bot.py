import aiohttp, asyncio, warnings, pytz
from datetime import datetime, timedelta
from pytz import timezone
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from aiohttp import web
from route import web_server
import pyrogram.utils
import pyromod
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import time

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

# Setting SUPPORT_CHAT directly here
SUPPORT_CHAT = int(os.environ.get("SUPPORT_CHAT", "-1002154446015"))

PORT = Config.PORT

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="codeflixbots",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )
        # Initialize the bot's start time for uptime calculation
        self.start_time = time.time()

    async def start(self, *args, **kwargs):
        await super().start(*args, **kwargs)
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username  
        self.uptime = Config.BOT_UPTIME     
        if Config.WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()       
            await web.TCPSite(app, "0.0.0.0", PORT).start()     
        print(f"{me.first_name} ɪᴛ ʜᴀs ʙᴇɢᴜɴ... ✨
𝘓𝘪𝘬𝘦 𝘵𝘪𝘮𝘦 𝘧𝘭𝘰𝘸𝘪𝘯𝘨 𝘰𝘯𝘤𝘦 𝘮𝘰𝘳𝘦...")

        # Calculate uptime using timedelta
        uptime_seconds = int(time.time() - self.start_time)
        uptime_string = str(timedelta(seconds=uptime_seconds))

        for chat_id in [Config.LOG_CHANNEL, SUPPORT_CHAT]:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time_str = curr.strftime('%I:%M:%S %p')
                
                # Send the message with the photo
                await self.send_photo(
                    chat_id=chat_id,
                    photo=Config.START_PIC,
                    caption=(
                        "**ꜰʀɪᴇʀᴇɴ ɪs ʙᴇɢɪɴɴɪɴɢ ᴀɢᴀɪɴ...
𝘐𝘵'𝘴 𝘢 𝘴𝘵𝘳𝘢𝘯𝘨𝘦 𝘧𝘦𝘦𝘭𝘪𝘯𝘨, 𝘳𝘦𝘵𝘶𝘳𝘯𝘪𝘯𝘨 𝘵𝘰 𝘰𝘭𝘥 𝘮𝘰𝘮𝘦𝘯𝘵𝘴...

ɪ ʜᴀᴠᴇɴ'ᴛ sʟᴇᴘᴛ sɪɴᴄᴇ: `{uptime_string}`"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/AniHorizon")
                        ]]
                    )
                )

            except Exception as e:
                print(f"Failed to send message in chat {chat_id}: {e}")

Bot().run()
