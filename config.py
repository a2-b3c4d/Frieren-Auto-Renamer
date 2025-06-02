import re, os, time
from os import environ, getenv
id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "736532225-w") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Yato")     
    DB_URL  = os.environ.get("DB_URL","mongodb")
    PORT = os.environ.get("PORT", "8080")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://files.catbox.moe/75frrs.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6586630448').split()]
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'AniHorizon').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "1002656577472"))
    DUMP_CHANNEL = int(os.environ.get("DUMP_CHANNEL", "-1002538016577"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """<b>❄️ ʜᴇʏ, {}... </b>  

<b>⤷ ɪ ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ʀᴇɴᴀᴍᴇ ʙᴏᴛ — ᴛɪᴍᴇʟᴇssʟʏ ʜᴀɴᴅʟɪɴɢ ʏᴏᴜʀ ғɪʟᴇs.</b>  
<b>⤷ ɪ ᴄᴀɴ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʀᴇɴᴀᴍᴇ, ᴄᴀᴘᴛɪᴏɴ, ᴀɴᴅ sᴇǫᴜᴇɴᴄᴇ ᴛʜᴇᴍ ᴡɪᴛʜ ᴘᴇʀғᴇᴄᴛ ᴘʀᴇᴄɪsɪᴏɴ. ✨</b>

<blockquote>
<b>🧩 <u>sᴇᴛᴛɪɴɢ ᴛʜᴇ ғᴏʀᴍᴀᴛ</u></b>

<b>⏳ ᴠᴀʀɪᴀʙʟᴇꜱ:</b>  
➤ <code>ᴇᴘɪꜱᴏᴅᴇ</code> — ʀᴇᴘʟᴀᴄᴇꜱ ᴇᴘɪꜱᴏᴅᴇ ɴᴜᴍʙᴇʀ  
➤ <code>ꜱᴇᴀꜱᴏɴ</code> — ʀᴇᴘʟᴀᴄᴇꜱ ꜱᴇᴀꜱᴏɴ ɴᴜᴍʙᴇʀ  
➤ <code>ǫᴜᴀʟɪᴛʏ</code> — ʀᴇᴘʟᴀᴄᴇꜱ ǫᴜᴀʟɪᴛʏ ᴛᴀɢ

<b>📌 ᴇxᴀᴍᴘʟᴇ:</b>  
<code>/autorename Oᴠᴇʀғʟᴏᴡ [Sseason Eepisode] - [Dual] quality</code>

<b>🔁 ᴜsᴇ `/autorename` ᴛᴏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ,</b>  
<b>ᴀɴᴅ ᴇxᴛʀᴀᴄᴛ ᴇᴘɪꜱᴏᴅᴇ/ǫᴜᴀʟɪᴛʏ ꜰʀᴏᴍ ᴏʀɪɢɪɴᴀʟ ғɪʟᴇ ɴᴀᴍᴇ.</b>
</blockquote>"""
    
    ABOUT_TXT = f"""<b>🌙 ᴇᴠᴇʀʟᴀsᴛɪɴɢ ɪɴ ᴛʜᴇ ᴛᴡɪʟɪɢʜᴛ, ᴍʏ ɴᴀᴍᴇ :</b> <a href="https://t.me/AniHorizon">ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ</a>  
<b>✨ ᴡɪᴛʜ ᴍᴀɢɪᴄ ᴛʜᴀᴛ ɴᴇᴠᴇʀ ᴄᴏɴᴅᴇsᴄᴇɴᴅs, ᴅᴇᴠᴇʟᴏᴩᴇʀ :</b> <a href="https://t.me/Tharun_stryker">🇸 🇹 🇷 🇾 🇰 🇪 🇷</a>  
<b>🔥 ᴡʜᴏ ᴡᴇᴀᴠᴇs ᴄᴏᴅᴇ ɪɴ ᴛʜᴇ ʙʟᴀᴢᴇ, ɢɪᴛʜᴜʙ :</b> <a href="https://t.me/+JBlEWX_WzR45MTc9">ꜰʀɪᴇʀᴇɴ</a>  
<b>🌿 ᴡɪᴛʜ ᴛʜᴇ ᴡɪsᴅᴏᴍ ᴏғ ᴛʜᴇ ᴏʟᴅ ʜɪʟʟs, ʟᴀɴɢᴜᴀɢᴇ :</b> <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ</a>  
<b>💧 ᴅᴇᴇᴘ ᴀs ᴛʜᴇ ᴏᴄᴇᴀɴ ᴅᴀᴛᴀʙᴀꜱᴇ :</b> <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a>  
<b>⚡ ɪɴ ᴛʜᴇ ɴᴇᴠᴇʀ-ʙʟɪɴᴋɪɴɢ ᴅᴀᴛᴀ sᴛʀᴇᴀᴍ, ʜᴏꜱᴛᴇᴅ ᴏɴ :</b> <a href="https://t.me/AniHorizon">Koyeb</a>  
<b>🌌 ᴀᴛ ᴛʜᴇ ᴄᴇɴᴛᴇʀ ᴏғ ᴛʜᴇ ᴍᴀɢɪᴄ, ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ :</b> <a href="https://t.me/+zxDRVmhYnGQyZDA1">AniHorizon</a>

<b>🌟 ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ʜᴇʟᴘ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴍᴇ.</b>"""

    
    THUMBNAIL_TXT = """<b><u>❄️ » ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ</u></b>
    
✨ ➲ /start: ᴡʜᴇɴ ᴛʜᴇ ʟɪɢʜᴛ ᴍᴇᴇᴛs ᴘɪxᴇʟ, ꜱᴇɴᴅ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ꜱᴇᴛ ɪᴛ ᴀꜱ ᴀ ᴛʜᴜᴍʙɴᴀɪʟ..
🔥 ➲ /del_thumb: ᴄʟᴇᴀʀ ᴛʜᴇ ᴍɪsᴛ ᴏғ ᴏʟᴅ ɪᴍᴀɢᴇꜱ, ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴏʟᴅ ᴛʜᴜᴍʙɴᴀɪʟ.
🌿 ➲ /view_thumb: ᴘᴇᴇʀ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴍᴇᴍᴏʀɪᴇꜱ, ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.

🌌 ɴᴏᴛᴇ: ɪꜰ ɴᴏ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ ɪɴ ʙᴏᴛ, ɪᴛ ᴡɪʟʟ ᴜꜱᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ᴛʜᴇ ᴏʀɪɢɪɴᴀʟ ꜰɪʟᴇ ᴛᴏ ꜱᴇᴛ ɪɴ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟᴇ."""


CAPTION_TXT = """<b><u>❄️ » ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ</u></b>
    
✨ <b>ᴠᴀʀɪᴀʙʟᴇꜱ :</b>         
🌿 ꜱɪᴢᴇ: {ꜰɪʟᴇꜱɪᴢᴇ}
💧 ᴅᴜʀᴀᴛɪᴏɴ: {duration}
🔥 ꜰɪʟᴇɴᴀᴍᴇ: {ꜰɪʟᴇɴᴀᴍᴇ}

⚡ ➲ /set_caption: ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
🌌 ➲ /see_caption: ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
🌙 ➲ /del_caption: ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.

✨ » ꜰᴏʀ ᴇx:- /set_caption ꜰɪʟᴇ ɴᴀᴍᴇ: {ꜰɪʟᴇɴᴀᴍᴇ}"""


PROGRESS_BAR = """\n
🌙 <b>» Size</b> : {1} | {2}
✨ <b>» Done</b> : {0}%
🔥 <b>» Speed</b> : {3}/s
⚡ <b>» ETA</b> : {4} """
    
    
    DONATE_TXT = """<blockquote>ᴛʜᴀɴᴋs ғᴏʀ sʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇsᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ</blockquote>

<b><i>💞 ɪꜰ ʏᴏᴜ ʟɪᴋᴇ ᴏᴜʀ ʙᴏᴛ, ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴅᴏɴᴀᴛᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ₹10, ₹20, ₹50, ₹100, ᴇᴛᴄ.</i></b>

ᴅᴏɴᴀᴛɪᴏɴs ᴀʀᴇ ʀᴇᴀʟʟʏ ᴀᴘᴘʀᴇᴄɪᴀᴛᴇᴅ — ɪᴛ ʜᴇʟᴘs ɪɴ ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ.

<u>ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴅᴏɴᴀᴛᴇ ᴛʜʀᴏᴜɢʜ ᴜᴘɪ</u>  
Gmail ɪᴅ: <code>tharunfitfun204@gmail.com</code>"""

PREMIUM_TXT = """<b>ᴜᴘɢʀᴀᴅᴇ ᴛᴏ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ ᴀɴᴅ ᴇɴJᴏʏ ᴇxᴄʟᴜsɪᴠᴇ ғᴇᴀᴛᴜʀᴇs:

○ ᴜɴʟɪᴍɪᴛᴇᴅ ʀᴇɴᴀᴍɪɴɢ: ʀᴇɴᴀᴍᴇ ᴀs ᴍᴀɴʏ ғɪʟᴇs ᴀs ʏᴏᴜ ᴡᴀɴᴛ ᴡɪᴛʜᴏᴜᴛ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.
○ ᴇᴀʀʟʏ ᴀᴄᴄᴇss: ʙᴇ ᴛʜᴇ ғɪʀsᴛ ᴛᴏ ᴛᴇsᴛ ᴀɴᴅ ᴜsᴇ ᴏᴜʀ ʟᴀᴛᴇsᴛ ғᴇᴀᴛᴜʀᴇs.

• ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.

➲ ꜰɪʀsᴛ sᴛᴇᴘ: ᴘᴀʏ ᴀᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴛᴏ: <code>tharunfitfun204@gmail.com</code>
➲ sᴇᴄᴏɴᴅ sᴛᴇᴘ: ᴛᴀᴋᴇ ᴀ sᴄʀᴇᴇɴꜱʜᴏᴛ ᴏғ ᴛʜᴇ ᴘᴀʏᴍᴇɴᴛ ᴀɴᴅ sʜᴀʀᴇ ɪᴛ ʜᴇʀᴇ: @Momo_Ayase_bot
➲ ᴀʟᴛᴇʀɴᴀᴛɪᴠᴇ: ᴏʀ ᴜᴘʟᴏᴀᴅ sᴄʀᴇᴇɴꜱʜᴏᴛ ʜᴇʀᴇ ᴀɴᴅ ʀᴇᴘʟʏ ᴡɪᴛʜ /bought

✅ Yᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴ ᴡɪʟʟ ʙᴇ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴀꜰᴛᴇʀ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.</b>"""

PREPLANS_TXT = """<b>👋 ʙʀᴏ,

🎖️ <u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u> :

Pʀɪᴄɪɴɢ:
➜ ᴍᴏɴᴛʜʟʏ ᴘʀᴇᴍɪᴜᴍ: ₹50/ᴍᴏɴᴛʜ  
➜ ᴅᴀɪʟʏ ᴘʀᴇᴍɪᴜᴍ: ₹5/ᴅᴀʏ  
➜ ʙᴏᴛ ʜᴏsᴛɪɴɢ: ᴄᴏɴᴛᴀᴄᴛ @Tharun_Stryker

➲ Gmail ɪᴅ - <code>tharunfitfun204@gmail.com</code>

‼️ Uᴘʟᴏᴀᴅ ᴘᴀʏᴍᴇɴᴛ sᴄʀᴇᴇɴꜱʜᴏᴛ ʜᴇʀᴇ ᴀɴᴅ ʀᴇᴘʟʏ ᴡɪᴛʜ /bought.</b>"""

HELP_TXT = """<b>🤖 ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴡɪᴛʜ ɪᴍᴘᴏʀᴛᴀɴᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:

✨ ᴀᴡᴇꜱᴏᴍᴇ ғᴇᴀᴛᴜʀᴇꜱ:
• /autorename – ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ.
• /metadata – ᴛᴜʀɴ ᴏɴ/ᴏꜰꜰ ᴍᴇᴛᴀᴅᴀᴛᴀ sᴇᴛᴛɪɴɢꜱ.
• /help – ǫᴜɪᴄᴋ ᴀꜱꜱɪꜱᴛᴀɴᴄᴇ.</b>"""

SEND_METADATA = """<b>--Metadata Settings:--</b>

➜ /metadata: Turn on or off metadata.

<b>Description</b>: Metadata will change MKV video files including all audio, streams, and subtitle titles."""

SOURCE_TXT = """<b>ʜᴇʏ,  
ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ʙᴏᴛ,  
ᴀɴ ᴏᴘᴇɴ-sᴏᴜʀᴄᴇ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴡʀɪᴛᴛᴇɴ ɪɴ ᴘʏᴛʜᴏɴ.</b>"""
    META_TXT = """
**ᴍᴀɴᴀɢɪɴɢ ᴍᴇᴛᴀᴅᴀᴛᴀ ғᴏʀ ʏᴏᴜʀ ᴠɪᴅᴇᴏs ᴀɴᴅ ғɪʟᴇs**

**ᴠᴀʀɪᴏᴜꜱ ᴍᴇᴛᴀᴅᴀᴛᴀ:**

- **ᴛɪᴛʟᴇ**: Descriptive title of the media.
- **ᴀᴜᴛʜᴏʀ**: The creator or owner of the media.
- **ᴀʀᴛɪꜱᴛ**: The artist associated with the media.
- **ᴀᴜᴅɪᴏ**: Title or description of audio content.
- **ꜱᴜʙᴛɪᴛʟᴇ**: Title of subtitle content.
- **ᴠɪᴅᴇᴏ**: Title or description of video content.

**ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ᴛᴜʀɴ ᴏɴ ᴏғғ ᴍᴇᴛᴀᴅᴀᴛᴀ:**
➜ /metadata: Turn on or off metadata.

**ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ꜱᴇᴛ ᴍᴇᴛᴀᴅᴀᴛᴀ:**

➜ /settitle: Set a custom title of media.
➜ /setauthor: Set the author.
➜ /setartist: Set the artist.
➜ /setaudio: Set audio title.
➜ /setsubtitle: Set subtitle title.
➜ /setvideo: Set video title.

**ᴇxᴀᴍᴘʟᴇ:** /settitle Your Title Here

**ᴜꜱᴇ ᴛʜᴇꜱᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ᴇɴʀɪᴄʜ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ᴡɪᴛʜ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ᴍᴇᴛᴀᴅᴀᴛᴀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ!**
"""
