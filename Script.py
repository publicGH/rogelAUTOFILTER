class script(object):
    START_TXT = """𝐡𝐞𝐥𝐥𝐨 {},
𝐌𝐲 𝐍𝐚𝐦𝐞 𝐢𝐬 <a href=https://t.me/{}>{}</a>, 𝐖𝐡𝐲 𝐚𝐫𝐞 𝐲𝐨𝐮 𝐡𝐞𝐫𝐞, 𝐈 𝐚𝐦 𝐨𝐧𝐥𝐲 𝐟𝐨𝐫 @Malu_movies_group_2 😍"""
    HELP_TXT = """𝐡𝐞𝐥𝐥𝐨 {}
𝐖𝐡𝐲 𝐚𝐫𝐞 𝐲𝐨𝐮 𝐥𝐨𝐨𝐤𝐢𝐧𝐠 𝐟𝐨𝐫 𝐡𝐞𝐥𝐩, 𝐓𝐡𝐢𝐬 𝐛𝐨𝐭 𝐢𝐬 𝐧𝐨𝐭 𝐟𝐨𝐫 𝐲𝐨𝐮 𝐬𝐢𝐫𝐞."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/rokuta_kamado>This Person</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 V2
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: <a href=https://t.me/Power_SERVER>Power Server</a>
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v2.3 [ StaBLe ]"""
 
   #ALERT MSG PMFILTER
    ABT_TXT = """✯ Mʏ Nᴀᴍᴇ: DQ
✯ Cʀᴇᴀᴛᴏʀ: @rokuta_kamado
✯ Lɪʙʀᴀʀʏ: Pyrogram
✯ Lᴀɴɢᴜᴀɢᴇ: Python 3
✯ DᴀᴛᴀBᴀsᴇ: MongoDB
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href=https://t.me/Power_SERVER>Power Server</a>
✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v2.3 [ Sᴛᴀʙʟᴇ ]"""
   
    SOURCE_TXT = """<b>NOTE:</b>
- This repo is not for you sire!!
<b>DEVS:</b>
- <a href=https://t.me/rokuta_kamado>Me</a>"""
    MANUELFILTER_TXT = """𝐓𝐡𝐞𝐫𝐞 𝐢𝐬 𝐧𝐨 𝐦𝐚𝐧𝐮𝐚𝐥 𝐟𝐢𝐥𝐭𝐞𝐫 𝐟𝐨𝐫 𝐲𝐨𝐮 𝐬𝐢𝐫𝐞!! 𝐈 𝐚𝐦 𝐦𝐚𝐝𝐞 𝐨𝐧𝐥𝐲 𝐟𝐨𝐫 @Malu_movies_group_2 """
    BUTTON_TXT = """🐖 Are you a Spammer ! """
    AUTOFILTER_TXT = """𝐖𝐡𝐲 𝐚𝐫𝐞 𝐘𝐨𝐮 𝐥𝐨𝐨𝐤𝐢𝐧𝐠 𝐟𝐨𝐫 𝐡𝐞𝐥𝐩, 𝐀𝐬 𝐈 𝐬𝐚𝐢𝐝 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭 𝐢𝐬 𝐧𝐨𝐭 𝐟𝐨𝐫 𝐲𝐨𝐮 𝐬𝐢𝐫𝐞! """  
    
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    
    STATUS_TXT = """★ Total Files: <code>{}</code>
★ Total Users: <code>{}</code>
★ Total Chats: <code>{}</code>
★ Using Storage: <code>{}</code> MB
★ Free Storage: <code>{}</code> MB"""
    
    ALRT_TXT = """Hello {},
This is Not your Request
Request Yourself...!!"""

    OLD_ALRT_TXT = """Hey {},
You are using one of old message,
Request Again"""

    CHK_MOV_TXT = """ 𝖢𝗁𝖾𝖼𝗄𝗂𝗇𝗀 𝖿𝗈𝗋 𝗊𝗎𝖾𝗋𝗒 𝗂𝗇 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 >>> """
    
    MVE_NT_FND = """❌ <b>𝖨 𝖼𝗈𝗎𝗅𝖽𝗇'𝗍 𝖿𝗂𝗇𝖽 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝗍𝗈 𝗍𝗁𝖺𝗍</b>\n\n‼ <b><i>𝖱𝖾𝗉𝗈𝗋𝗍 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 ▶ @rokuta_kamado</i></b>"""
    
    SPOLL_NOT_FND = """ I Couldn't Find the FILE you requested
Try to do the following...
 
➤ Request with Correct Spelling.
➤ Don't ask movies that are NOT REALEASED in OTT PLATFORM.
➤ Try to ask in [Moviename, Language] this format.
➤Use the Button below to search on Google Or IMDB. """
    
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    RESTART_TXT = """
<b>𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 !</b>

📅 𝖣𝖺𝗍𝖾 : <code>{}</code>
⏰ 𝖳𝗂𝗆𝖾 : <code>{}</code>
🌐 𝖳𝗂𝗆𝖾𝗓𝗈𝗇𝖾 : <code>Asia/Kolkata</code>
🛠️ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : <code>𝗏2.3 [ 𝖲𝗍𝖺𝖻𝗅𝖾 ]</code></b>"""
