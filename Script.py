class script(object):
    HELP_TXT = """π·π΄π {}
Κα΄Κα΄ Ιͺκ± α΄Κα΄ Κα΄Κα΄ κ°α΄Κ α΄Κ α΄α΄α΄α΄α΄Ι΄α΄."""
    ABOUT_TXT = """<b>β― πΌπ π½π°πΌπ΄: {}</b>
β― π»πΈπ±ππ°ππ: πΏπππΎπΆππ°πΌ
β― π»π°π½πΆππ°πΆπ΄: πΏπππ·πΎπ½ πΉ
β― π³π°ππ° π±π°ππ΄: πΌπΎπ½πΆπΎ π³π±
β― π±πΎπ ππ΄πππ΄π: ππΏπ
β― π±ππΈπ»π³ πππ°πππ: v4.0.2 [ π±π΄ππ° ]""" 
    SOURCE_TXT = """<b>NOTE:</b>
- <b> bot is a not open source project. 
- contact my Owner</b>

<b>Message:</b>
- <a href=https://t.me/AkshayChand10>Akshay Chand</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- movies house Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/AkshayChand10)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specified user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """ β ππΎππ°π» π΅πΈπ»π΄π: <code>{}</code>
β ππΎππ°π» πππ΄ππ: <code>{}</code>
β ππΎππ°π» π²π·π°ππ: <code>{}</code>
β πππ΄π³ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±
β π΅ππ΄π΄ πππΎππ°πΆπ΄: <code>{}</code> πΌππ± """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    START_TXT = """<b>Κα΄Κ {},

Ιͺ'α΄ β‘οΈ α΄α΄α΄‘α΄Κκ°α΄Κ α΄α΄α΄α΄-κ°ΙͺΚα΄α΄Κ Κα΄α΄...
π Κα΄α΄ α΄α΄Ι΄ α΄κ±α΄ α΄α΄ α΄κ± α΄ α΄α΄α΄α΄-κ°ΙͺΚα΄α΄Κ ΙͺΙ΄ Κα΄α΄Κ Ι’Κα΄α΄α΄ ....
Ιͺα΄κ± α΄α΄κ±Κ α΄α΄ α΄κ±α΄ α΄α΄; α΄α΄κ±α΄ α΄α΄α΄ α΄α΄ α΄α΄ Κα΄α΄Κ Ι’Κα΄α΄α΄ α΄κ± α΄α΄α΄ΙͺΙ΄, α΄Κα΄α΄κ± α΄ΚΚ, Ιͺ α΄‘ΙͺΚΚ α΄Κα΄α΄ Ιͺα΄α΄ α΄α΄α΄ Ιͺα΄κ± α΄Κα΄Κα΄...π
β οΈ α΄α΄Κα΄ Κα΄Κα΄ α΄Κα΄α΄α΄ Κα΄Κα΄ Κα΄α΄α΄α΄Ι΄ Κα΄Κα΄α΄‘</b>"""

    GHHM_TXT = """<b>Β©οΈ Bot Owner's:- 

1} <a href=https://t.me/AkshayChand10>Akshay Chand</a>

2} <a href=https://t.me/Jokar48>ΚΦΣΗΚ</a>

3} <a href=https://t.me/LEGEND678AK>ΰΌΊLeΝ₯geΝ£nΝ«dΰΌ»</a></b>"""

    GHHN_TXT = """Extra features"""

    MALIK_TXT =  """<b>Donation</b>
   
   <b>Developer is Super Noob..  Just Learning from Official Docs..  Please Donate the developer for Keeping the Service Alive...</b>


βͺΌ <b>ππ¨π? πππ§ ππ¨π§ππ­π ππ§π² ππ¦π¨π?π§π­ ππ¨π? πππ―π π³. 

Payment Methods

β? ππΌπΌπ΄πΉπ²π£π?π
β? π£π?πππΊ           
β? π£π΅πΌπ»π²π£π²     
β? π£π?ππ£π?πΉ
ππ¨π§π­πππ­ ππ ππ¨π« ππ§π¨π° πππ¨π?π­ ππ‘π πππ²π¦ππ§π­ ππ§ππ¨

<a href=https://t.me/AkshayChand10><b>Akshay Chand</b></a>"""
    DINETTE_TXT =  """<b>Donation</b>

   <b>Developer is Super Noob..  Just Learning from Official Docs..  Please Donate the developer for Keeping the Service Alive...</b>


βͺΌ <b>ππ¨π? πππ§ ππ¨π§ππ­π ππ§π² ππ¦π¨π?π§π­ ππ¨π? πππ―π π³. 

Payment Methods

β? ππΌπΌπ΄πΉπ²π£π?π
β? π£π?πππΊ           
β? π£π΅πΌπ»π²π£π²     
β? π£π?ππ£π?πΉ
ππ¨π§π­πππ­ ππ ππ¨π« ππ§π¨π° πππ¨π?π­ ππ‘π πππ²π¦ππ§π­ ππ§ππ¨ 

<a href=https://t.me/AkshayChand10><b>Akshay Chand</b></a>"""


    URLSHORT_TXT = """<b>β€ πππ₯π©: π΄ππ πππππππΎπ

ππππ πππππππ πππππ π’ππ ππ πππππ π πππ 

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ /short: πππΎ ππππ πΌππππΊππ½ ππππ ππππ ππππ ππ ππΎπ ππππππΎπ½ πππππ

βπ€ππΊππππΎ:
/short https://t.me/+veUIdIW2CQ5GU5</b>"""


    URLSHORTN_TXT = """<b>β€ πππ₯π©: π΄ππ πππππππΎπ

ππππ πππππππ πππππ π’ππ ππ πππππ π πππ 

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ /short: πππΎ ππππ πΌππππΊππ½ ππππ ππππ ππππ ππ ππΎπ ππππππΎπ½ πππππ

βπ€ππΊππππΎ:
/short https://t.me/+veUIdIW25mOGU5</b>"""

    VIDEO_TXT ="""<b>π·π΄π»πΏ ππΎπ ππΎ π³πΎππ½π»πΎπ°π³ ππΈπ³π΄πΎ π΅ππΎπΌ ππΎππππ±π΄.

β’ ππ΄π’π¨π¦
π π°πΆ ππ’π― ππ°πΈπ―π­π°π’π₯ ππ―πΊ ππͺπ₯π¦π° ππ³π°π? π π°πΆπ΅πΆπ£π¦

ππ€π¬ ππ€ ππ¨π
β’ ππΊπ±π¦ /video or /mp4 ππ―π₯ (ππͺπ₯π¦π° Link)
β’ ππΉπ’π?π±π­π¦:
/π?π±4 https://youtu.be/Your Link</b>"""

    VIDEOS_TXT ="""<b>π·π΄π»πΏ ππΎπ ππΎ π³πΎππ½π»πΎπ°π³ ππΈπ³π΄πΎ π΅ππΎπΌ ππΎππππ±π΄.

β’ ππ΄π’π¨π¦
π π°πΆ ππ’π― ππ°πΈπ―π­π°π’π₯ ππ―πΊ ππͺπ₯π¦π° ππ³π°π? π π°πΆπ΅πΆπ£π¦

ππ€π¬ ππ€ ππ¨π
β’ ππΊπ±π¦ /video or /mp4 ππ―π₯ (ππͺπ₯π¦π° Link)
β’ ππΉπ’π?π±π­π¦:
/π?π±4 https://youtu.be/Your Link</b>"""

    YTTHUMB_TXT = """<b>π·π΄π»πΏπ ππΎ π³πΎππ½π»πΎπ°π³ π°π½π ππΎππππ±π΄ ππΈπ³π΄πΎ ππ·ππΌπ±π½π°πΈπ»
    
β­ππ€π¬ ππ€ ππ¨π
ππΊπ±π¦ /ytthumb ππ―π₯ ππͺπ₯π¦π° ππͺπ―π¬

β’ ππΉπ’π?π±π­π¦
/ytthumb https://youtu.be/yourlink</b>"""

    SONG_TXT = """<b>ππΎπ½πΆ π³πΎππ½π»πΎπ°π³ πΌπΎπ³ππ»π΄...

ππΎπ½πΆ π³πΎππ½π»πΎπ°π³ πΌπΎπ³ππ»π΄, π΅πΎπ ππ·πΎππ΄ ππ·πΎ π»πΎππ΄ πΌπππΈπ². ππΎπ π²π°π½ πππ΄ ππ·πΈπ π΅π΄π°πππ΄ π΅πΎπ π³πΎππ½π»πΎπ°π³ π°π½π ππΎπ½πΆ ππΈππ· πππΏπ΄π π΅π°ππ ππΏπ΄π΄π³.ππΎππΊπ πΎπ½π»π πΎπ½ πΆππΎππΏπ..

<π²πΎπΌπΌπ°π½π³π

βΊβΊ  /song ππΎπ½πΆ π½π°πΌπ΄ 

ππΎππΊπ πΎπ½π»π πΎπ½ πΆππΎππΏ"""


    FILESTORE_TXT = """β€ πππ₯π©: ππ’π₯π ππ­π¨π«π ππ¨ππ?π₯π../

<b>π±π πππΈπ½πΆ ππ·πΈπ πΌπΎπ³ππ»π΄ ππΎπ π²π°π½ πππΎππ΄ π΅πΈπ»π΄π πΈπ½ πΌπ π³π°ππ°π±π°ππ΄ π°π½π³ πΈ ππΈπ»π» πΆπΈππ΄ ππΎπ π° πΏπ΄ππΌπ°π½π΄π½π π»πΈπ½πΊ  ππΎ π°π²π²π΄ππ ππ·π΄ ππ°ππ΄π³ π΅πΈπ»π΄π.πΈπ΅ ππΎπ ππ°π½π ππΎ π°π³π³ π΅πΈπ»π΄π π΅ππΎπΌ π° πΏππ±π»πΈπ² π²π·π°π½π½π΄π» ππ΄π½π³ ππ·π΄ π΅πΈπ»π π»πΈπ½πΊ πΎπ½π»π  πΎπ ππΎπ ππ°π½π ππΎ π°π³π³ π΅πΈπ»π΄π π΅ππΎπΌ π°  πΏππΈππ°ππ΄ π²π·π°π½π½π΄π» ππΎπ πΌπππ πΌπ°πΊπ΄ πΌπ΄ π°π³πΌπΈπ½ πΎπ½ ππ·π΄ π²π·π°π½π½π΄π» ππΎ π°π²π²π΄ππ π΅πΈπ»π΄π...//</b>

βͺΌ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π βΊ

βͺ /plink βΊβΊ <b>ππ΄πΏπ»π ππΎ π°π½π πΌπ΄π³πΈπ° ππΎ πΆπ΄π π»πΈπ½πΊ.</b>
βͺ /pbatch βΊβΊ <b>πππ΄ ππΎππ πΌπ΄π³πΈπ° π»πΈπ½πΊ ππΈππ· ππ·πΈπ π²πΎπΌπΌπ°π½π³.</b>
βͺ /batch βΊβΊ <b>ππΎ π²ππ΄π°ππ΄ π»πΈπ½πΊ π΅πΎπ πΌππ»ππΈπΏπ»π΄ π΅πΈπ»π΄π.</b>

βͺΌ ππ±ππ¦π©π₯π βΊ

<code>/batch https://t.me/gjcjknxz/2 https://t.me/jfksucxhb/8</code>"""

    FORCESUB_TXT = """β οΈ Join our updated channel below.  bot will not give you movie until you join from our update channel...

β οΈ ΰ?ΰ―ΰ?΄ΰ― ΰ?ΰ?³ΰ―ΰ?³ ΰ?ΰ?ΰ―ΰ?ΰ?³ΰ― ΰ?ͺΰ―ΰ?€ΰ―ΰ?ͺΰ―ΰ?ͺΰ?Ώΰ?ΰ―ΰ?ΰ?ͺΰ―ΰ?ͺΰ?ΰ―ΰ? ΰ?ΰ―ΰ?©ΰ?²ΰ?Ώΰ?²ΰ― ΰ?ΰ―ΰ?°ΰ?΅ΰ―ΰ??ΰ―.  ΰ?ΰ?ΰ―ΰ?ΰ?³ΰ― ΰ?ͺΰ―ΰ?€ΰ―ΰ?ͺΰ―ΰ?ͺΰ?Ώΰ?ͺΰ―ΰ?ͺΰ― ΰ?ΰ―ΰ?©ΰ?²ΰ?Ώΰ?²ΰ― ΰ?¨ΰ―ΰ?ΰ―ΰ?ΰ?³ΰ― ΰ?ΰ―ΰ?°ΰ―ΰ??ΰ― ΰ?΅ΰ?°ΰ― ΰ?ͺΰ―ΰ?ΰ― ΰ?ΰ?ΰ―ΰ?ΰ?³ΰ―ΰ?ΰ―ΰ?ΰ― ΰ?€ΰ?Ώΰ?°ΰ―ΰ?ͺΰ―ΰ?ͺΰ?ΰ?€ΰ―ΰ?€ΰ― ΰ?΅ΰ?΄ΰ?ΰ―ΰ?ΰ?Ύΰ?€ΰ―... 

β οΈ ΰ¨Ήΰ©ΰ¨ ΰ¨Ύΰ¨ ΰ¨Έΰ¨Ύΰ¨‘ΰ© ΰ¨ΰ¨ͺΰ¨‘ΰ©ΰ¨ ΰ¨ΰ©ΰ¨€ΰ© ΰ¨ΰ©ΰ¨¨ΰ¨² ΰ¨΅ΰ¨Ώΰ©±ΰ¨ ΰ¨Έΰ¨Όΰ¨Ύΰ¨?ΰ¨² ΰ¨Ήΰ©ΰ¨΅ΰ©ΰ₯€  ΰ¨¬ΰ©ΰ¨ ΰ¨€ΰ©ΰ¨Ήΰ¨Ύΰ¨¨ΰ©ΰ©° ΰ¨ΰ¨¦ΰ©ΰ¨ ΰ¨€ΰ©±ΰ¨ ΰ¨?ΰ©ΰ¨΅ΰ© ΰ¨¨ΰ¨Ήΰ©ΰ¨ ΰ¨¦ΰ©ΰ¨΅ΰ©ΰ¨ΰ¨Ύ ΰ¨ΰ¨¦ΰ©ΰ¨ ΰ¨€ΰ©±ΰ¨ ΰ¨€ΰ©ΰ¨Έΰ©ΰ¨ ΰ¨Έΰ¨Ύΰ¨‘ΰ© ΰ¨ΰ¨ͺΰ¨‘ΰ©ΰ¨ ΰ¨ΰ©ΰ¨¨ΰ¨² ΰ¨€ΰ©ΰ¨ ΰ¨Έΰ¨Όΰ¨Ύΰ¨?ΰ¨² ΰ¨¨ΰ¨Ήΰ©ΰ¨ ΰ¨Ήΰ© ΰ¨ΰ¨Ύΰ¨ΰ¨¦ΰ©...

β οΈ ΰ΄ΰ΅ΰ΄΅ΰ΄ΰ΅ΰ΄―ΰ΅ΰ΄³ΰ΅ΰ΄³ ΰ΄ΰ΄ΰ΅ΰ΄ΰ΄³ΰ΅ΰ΄ΰ΅ ΰ΄ΰ΄ͺΰ΅βΰ΄‘ΰ΅ΰ΄±ΰ΅ΰ΄±ΰ΅ ΰ΄ΰ΅ΰ΄―ΰ΅βΰ΄€ ΰ΄ΰ΄Ύΰ΄¨ΰ΄²ΰ΄Ώΰ΅½ ΰ΄ΰ΅ΰ΄°ΰ΅ΰ΄.  ΰ΄ΰ΄ΰ΅ΰ΄ΰ΄³ΰ΅ΰ΄ΰ΅ ΰ΄ΰ΄ͺΰ΅βΰ΄‘ΰ΅ΰ΄±ΰ΅ΰ΄±ΰ΅ ΰ΄ΰ΄Ύΰ΄¨ΰ΄²ΰ΄Ώΰ΅½ ΰ΄¨ΰ΄Ώΰ΄¨ΰ΅ΰ΄¨ΰ΅ ΰ΄¨ΰ΄Ώΰ΄ΰ΅ΰ΄ΰ΅Ύ ΰ΄ΰ΅ΰ΄°ΰ΅ΰ΄¨ΰ΅ΰ΄¨ΰ΄€ΰ΅ ΰ΄΅ΰ΄°ΰ΅ ΰ΄¬ΰ΅ΰ΄ΰ΅ΰ΄ΰ΅ ΰ΄¨ΰ΄Ώΰ΄ΰ΅ΰ΄ΰ΅Ύΰ΄ΰ΅ΰ΄ΰ΅ ΰ΄Έΰ΄Ώΰ΄¨ΰ΄Ώΰ΄? ΰ΄¨ΰ΅½ΰ΄ΰ΄Ώΰ΄²ΰ΅ΰ΄²....

β οΈ ΰ€Ήΰ€?ΰ€Ύΰ€°ΰ₯ ΰ€¨ΰ€Ώΰ€ΰ₯ ΰ€¦ΰ€Ώΰ€ ΰ€ΰ€―ΰ₯ update ΰ€ΰ₯ΰ€¨ΰ€² ΰ€ΰ₯ join ΰ€ΰ€°ΰ₯ ΰ€ΰ€¬ ΰ€€ΰ€ ΰ€ΰ€ͺ ΰ€Ήΰ€?ΰ€Ύΰ€°ΰ₯ update ΰ€ΰ₯ΰ€¨ΰ€² ΰ€ΰ₯ join ΰ€¨ΰ€Ήΰ₯ΰ€ ΰ€ΰ€°ΰ₯ΰ€ΰ€ΰ₯ ΰ€€ΰ€¬ ΰ€€ΰ€ bot ΰ€ΰ€ͺΰ€ΰ₯ ΰ€?ΰ₯ΰ€΅ΰ₯ ΰ€¨ΰ€Ήΰ₯ΰ€ ΰ€¦ΰ₯ΰ€ΰ€Ύ...ππ join new ππ"""

    OWNER_TXT = """<b>
πΉ α΄Κ Ι΄α΄α΄α΄ : α΄α΄κ±Κα΄Κ α΄Κα΄Ι΄α΄
πΉ α΄sα΄ΚΙ΄α΄α΄α΄: @AkshayChand10
πΉ α΄α΄α΄. α΄α΄ ΚΙͺΙ΄α΄: <a href=https://t.me/AkshayChand10>α΄α΄κ±Κα΄Κ α΄Κα΄Ι΄α΄</a>
πΉ α΄Κα΄α΄α΄:| α΄α΄Κα΄Κα΄κ±Κα΄Κα΄ | ΙͺΙ΄α΄Ιͺα΄
πΉ α΄Ι΄α΄α΄‘ Κα΄Ι΄Ι’α΄α΄Ι’α΄: ΚΙͺΙ΄α΄Ιͺ, α΄Ι΄Ι’ΚΙͺκ±Κ
πΉ Κα΄ΚΙͺΙ’Ιͺα΄Ι΄ α΄α΄sα΄: ΚΙͺΙ΄α΄α΄
πΉ α΄α΄Κ: 00 | 04 | 2004
πΉ AΙ’α΄: α΄α΄sα΄ α΄α΄Κα΄α΄Κα΄α΄α΄
πΉ Κα΄α΄ α΄Κ: ?ΚΙͺsα΄ Κα΄α΄Κ Κα΄α΄α΄ α΄α΄α΄
πΉ ?α΄α΄  α΄α΄Κα΄α΄Κ: ΚΚα΄α΄α΄, Κα΄α΄, Ι’Κα΄α΄Ι΄, ΚΚα΄α΄..</b>"""
    GROUP_R_TXT = """<b>GROUP RULES

βοΈ  Search With Correct Spelling..

βοΈ Try to Search movie web series With  Year If The bot is Not Sending You Accurate Result..

βοΈ Search Series In The Given From Example : Gotham S03E01 And S03E10..

βοΈ Search Movies and web series  in The Given From Example:    

π° Movies 

(1) Avengers.. β
(2) Avengers Hindi..β
(3) Avengers 2012 Hindi..β
(4) Don't Tipe Avengers Hindi Dubbed..β
(5) Avengers Hindi movie..β

π° Web Series

(1) Money heist..β
(2) Money heist S01 EP1..β
(3) Money heist Hindi..β
(4) Money heist all season..β
(5) Money heist all Hindi season..β

βοΈDon't Do Any Self Promotion.

βοΈ Don't Send Any Kind Of Photo Video Documents URL ETC.

βοΈ Sending The Above  Mantained Things Will Lead To Permanent Ban.

βοΈDon't Request Any Things Other Than Movie Series Animes.

βοΈ Give and Tak Respect</b>.."""

MALIK_PHH = """<b>Hay π {}.... π· β€οΈ

π welcome to Our Group...
  
      π <s>{}</s> π 

π You Can Find π Movies / Series / Animes etc. From Here. Enjoy π...

If you have any question then contact us below  π</b>"""

ALURT_FND = """<b>.

CHECK YOUR MOVIE ON THE GIVEN LIST AND SELECT YOUR MOVIE..</b>"""

ADG = """<b>Hay. {}..\n\nThankyou For Adding Me In.. β£οΈ

             π <s>{}</s> π 

If you have any questions & doubts about using me..\n\n Contact my Owner >> @AkshayChand10</b>"""

ADDG = """<b>Hay {},

I'm β‘οΈ Powerful Auto-Filter Bot...
π You Can Use Me As A Auto-filter in Your Group ....
Its Easy To Use Me; Just Add Me To Your Group As Admin, Thats All, i will Provide Movies There...π
β οΈ More Help Check Help Button Below

Β©οΈMantained BΚ  @AkshayChand10</b>"""

M_NT_FND = """<b>β­οΈ This Movie Not Found my Database. Request to admin..\n\nβ­οΈ Ye movie Hamare database me Available nahi hai Niche admin se request kare... \n\nβ­οΈ Request to admin.. π</b>"""

INST = """α΄α΄α΄ Ιͺα΄ Κα΄Η«α΄α΄sα΄ ?α΄Κα΄α΄α΄ 

α΄xα΄α΄α΄Κα΄ : α΄α΄ α΄Ι΄Ι’α΄Κs α΄Κ α΄α΄ α΄Ι΄Ι’α΄Κs πΈπΆπ·πΈ: 

sα΄ΚΙͺα΄s Κα΄Η«α΄α΄sα΄ ?α΄Κα΄α΄α΄: 

α΄xα΄α΄α΄Κα΄ : Κα΄α΄Ιͺ s01α΄01 α΄Κ Κα΄α΄Ιͺ s01α΄10,Β  

α΄α΄Ι΄'α΄ α΄sα΄ ' : ( ! , . / ) """

MQTT = """<b>β οΈ πππ², {}!..</b> 

sα΄ΚΚΚ Ι΄α΄ κ°ΙͺΚα΄s π α΄‘α΄Κα΄ κ°α΄α΄Ι΄α΄

α΄Κα΄α΄α΄ Κα΄α΄Κ sα΄α΄ΚΚΙͺΙ΄Ι’ ΙͺΙ΄ Ι’α΄α΄Ι’Κα΄ π α΄Ι΄α΄ α΄ΚΚ α΄Ι’α΄ΙͺΙ΄

sα΄α΄Κα΄Κ α΄α΄α΄ Ιͺα΄s κ°Κα΄α΄ Ι’α΄α΄Ι’Κα΄ π α΄α΄α΄Κ α΄Κα΄ Ι΄α΄α΄α΄ α΄Ι΄α΄ α΄α΄sα΄α΄ Ιͺα΄

Κα΄α΄Κ α΄α΄α΄ Ιͺα΄ Ι΄α΄α΄ α΄α΄ α΄ΙͺΚα΄ΚΚα΄ ΙͺΙ΄ α΄Κ α΄α΄α΄α΄Κα΄sα΄ π

Ι΄α΄α΄ Κα΄Κα΄α΄sα΄ α΄α΄α΄ Κα΄α΄ β οΈ

Ιͺκ° Κα΄α΄Κ α΄α΄α΄ Ιͺα΄ Ιͺs Κα΄Κα΄α΄sα΄α΄ α΄Ι΄ α΄α΄α΄ α΄Κα΄Ι΄ Ι΄α΄α΄ α΄α΄α΄ α΄Κ α΄α΄α΄α΄Κα΄sα΄ π sα΄Ι΄α΄ Κα΄Η«α΄α΄sα΄ α΄α΄ α΄α΄α΄ΙͺΙ΄ α΄α΄ α΄α΄α΄ Κα΄α΄Κ α΄α΄α΄ Ιͺα΄..

π <b>sα΄Ι΄α΄ Κα΄Η«α΄α΄sα΄ π©</b>"""




