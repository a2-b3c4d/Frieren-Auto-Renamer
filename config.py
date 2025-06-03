import re, os, time
from os import environ, getenv
id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "736532225-w") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
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
    
DONATE_TXT = """<i>ᴛʜᴀɴᴋs ғᴏʀ sʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇsᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ</i>

<b><i>💞 ɪꜰ ʏᴏᴜ ʟɪᴋᴇ ᴏᴜʀ ʙᴏᴛ, ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴅᴏɴᴀᴛᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ₹10, ₹20, ₹50, ₹100, ᴇᴛᴄ.</i></b>

ᴅᴏɴᴀᴛɪᴏɴs ᴀʀᴇ ʀᴇᴀʟʟʏ ᴀᴘᴘʀᴇᴄɪᴀᴛᴇᴅ — ɪᴛ ʜᴇʟᴘs ɪɴ ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ.

<u>ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴅᴏɴᴀᴛᴇ ᴛʜʀᴏᴜɢʜ ᴜᴘɪ</u>  
Gmail ɪᴅ: <code>subsquad05@gmail.com</code>"""
PREMIUM_TXT = """<b>ᴜᴘɢʀᴀᴅᴇ ᴛᴏ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ ᴀɴᴅ ᴇɴJᴏʏ ᴇxᴄʟᴜsɪᴠᴇ ғᴇᴀᴛᴜʀᴇs:

○ ᴜɴʟɪᴍɪᴛᴇᴅ ʀᴇɴᴀᴍɪɴɢ: ʀᴇɴᴀᴍᴇ ᴀs ᴍᴀɴʏ ғɪʟᴇs ᴀs ʏᴏᴜ ᴡᴀɴᴛ ᴡɪᴛʜᴏᴜᴛ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.
○ ᴇᴀʀʟʏ ᴀᴄᴄᴇss: ʙᴇ ᴛʜᴇ ғɪʀsᴛ ᴛᴏ ᴛᴇsᴛ ᴀɴᴅ ᴜsᴇ ᴏᴜʀ ʟᴀᴛᴇsᴛ ғᴇᴀᴛᴜʀᴇs.

• ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.

➲ ꜰɪʀsᴛ sᴛᴇᴘ: ᴘᴀʏ ᴀᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴛᴏ: <code>subsquad05@gmail.com</code>
➲ sᴇᴄᴏɴᴅ sᴛᴇᴘ: ᴛᴀᴋᴇ ᴀ sᴄʀᴇᴇɴꜱʜᴏᴛ ᴏғ ᴛʜᴇ ᴘᴀʏᴍᴇɴᴛ ᴀɴᴅ sʜᴀʀᴇ ɪᴛ ʜᴇʀᴇ: @Momo_Ayase_bot
➲ ᴀʟᴛᴇʀɴᴀᴛɪᴠᴇ: ᴏʀ ᴜᴘʟᴏᴀᴅ sᴄʀᴇᴇɴꜱʜᴏᴛ ʜᴇʀᴇ ᴀɴᴅ ʀᴇᴘʟʏ ᴡɪᴛʜ /bought

✅ Yᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴ ᴡɪʟʟ ʙᴇ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴀꜰᴛᴇʀ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.</b>"""

PREPLANS_TXT = """<b>👋 ʙʀᴏ,

🎖️ <u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u> :

Pʀɪᴄɪɴɢ:
➜ ᴍᴏɴᴛʜʟʏ ᴘʀᴇᴍɪᴜᴍ: ₹50/ᴍᴏɴᴛʜ  
➜ ᴅᴀɪʟʏ ᴘʀᴇᴍɪᴜᴍ: ₹5/ᴅᴀʏ  
➜ ʙᴏᴛ ʜᴏsᴛɪɴɢ: ᴄᴏɴᴛᴀᴄᴛ @Tharun_Stryker

➲ Gmail ɪᴅ - <code>subsquad05@gmail.com</code>

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
✨ 𝙼𝙴𝚃𝙰𝙳𝙰𝚃𝙰 𝙶𝚄𝙸𝙳𝙴 ✨

𖦹 𝐸𝓃𝒽𝒶𝓃𝒸𝑒 𝓎𝑜𝓊𝓇 𝓋𝒾𝒹𝑒𝑜𝓈 & 𝒻𝒾𝓁𝑒𝓈 𝓌𝒾𝓉𝒽 𝒷𝑒𝒶𝓊𝓉𝒾𝒻𝓊𝓁 𝓂𝑒𝓉𝒶𝒹𝒶𝓉𝒶 ✨

• 𝙏𝙞𝙩𝙡𝙚: 𝘾𝙧𝙚𝙖𝙩𝙚 𝙖 𝙘𝙝𝙖𝙧𝙢𝙞𝙣𝙜 𝙩𝙞𝙩𝙡𝙚 𝙛𝙤𝙧 𝙮𝙤𝙪𝙧 𝙢𝙚𝙙𝙞𝙖  
• 𝘼𝙪𝙩𝙝𝙤𝙧: 𝙉𝙖𝙢𝙚 𝙤𝙛 𝙩𝙝𝙚 𝙘𝙧𝙚𝙖𝙩𝙤𝙧  
• 𝘼𝙧𝙩𝙞𝙨𝙩: 𝘼𝙧𝙩𝙞𝙨𝙩’𝙨 𝙣𝙖𝙢𝙚  
• 𝘼𝙪𝙙𝙞𝙤: 𝙏𝙞𝙩𝙡𝙚 𝙤𝙛 𝙩𝙝𝙚 𝙖𝙪𝙙𝙞𝙤 𝙘𝙤𝙣𝙩𝙚𝙣𝙩  
• 𝙎𝙪𝙗𝙩𝙞𝙩𝙡𝙚: 𝙎𝙪𝙗𝙩𝙞𝙩𝙡𝙚 𝙩𝙞𝙩𝙡𝙚  
• 𝙑𝙞𝙙𝙚𝙤: 𝙏𝙞𝙩𝙡𝙚 𝙤𝙛 𝙩𝙝𝙚 𝙫𝙞𝙙𝙚𝙤

🔁 𝙏𝙤𝙜𝙜𝙡𝙚 𝙢𝙚𝙩𝙖𝙙𝙖𝙩𝙖:  
➤ /metadata

🛠️ 𝙎𝙚𝙩 𝙢𝙚𝙩𝙖𝙙𝙖𝙩𝙖 𝙛𝙞𝙚𝙡𝙙𝙨:  
➤ /settitle — 𝘾𝙪𝙨𝙩𝙤𝙢 𝙩𝙞𝙩𝙡𝙚  
➤ /setauthor — 𝘼𝙪𝙩𝙝𝙤𝙧 𝙣𝙖𝙢𝙚  
➤ /setartist — 𝘼𝙧𝙩𝙞𝙨𝙩 𝙣𝙖𝙢𝙚  
➤ /setaudio — 𝘼𝙪𝙙𝙞𝙤 𝙩𝙞𝙩𝙡𝙚  
➤ /setsubtitle — 𝙎𝙪𝙗𝙩𝙞𝙩𝙡𝙚 𝙩𝙞𝙩𝙡𝙚  
➤ /setvideo — 𝙑𝙞𝙙𝙚𝙤 𝙩𝙞𝙩𝙡𝙚

🧿 𝙀𝙭𝙖𝙢𝙥𝙡𝙚: `/settitle Your Title Here`

➺ 𝑀𝒶𝓀𝑒 𝓎𝑜𝓊𝓇 𝒻𝒾𝓁𝑒𝓈 𝒻𝑒𝑒𝓁 𝓁𝒾𝓀𝑒 𝓉𝒽𝑒𝓎 𝒷𝑒𝓁𝑜𝓃𝑔 𝒾𝓃 𝒶 𝓂𝒶𝑔𝒾𝒸𝒶𝓁 𝒿𝑜𝓊𝓇𝓃𝑒𝓎 🌙
"""
