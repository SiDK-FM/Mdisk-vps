import os
import threading
import subprocess
import time

import pyrogram
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton

import mdisk
import extras
import mediainfo
import split
from split import TG_SPLIT_SIZE


# app
bot_token = os.environ.get("TOKEN", "5898894448:AAENSOPOBYktmYtRoy3W37y-8E8jBNPRKqQ") 
api_hash = os.environ.get("HASH", "ad762fe0516f367115ba651d929cf429") 
api_id = os.environ.get("ID", "17737898")
app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)

# preiumum
from split import ss, temp_channel, isPremmium
if isPremmium: acc = Client("myacc", api_id=api_id, api_hash=api_hash, session_string=ss)

# optionals
auth = os.environ.get("AUTH", "623741973,1864861524,5076949930,683684279,306027849,5316294458,5290630238,598394386,5410723702,1303200779,635819536,5135693898,817785442,5020113494,1278611015,5285296040,1335978271,1053140055,1024155122,1667559069,1057959919,1838349598,2083663200,540828579,5072829406,5753750662,910348411,5637860109,5580289036,5069888600,5552151289,5541612283,751366152,5344930478,5715297117,672148918,866545155,1262828639,5749138669,1492398806,5515158923,696401705,981462080,5769418923,1928306010,898811148,5937683464,1222974251,5307413215,1414678142,240296058,1121839250")
ban = os.environ.get("BAN", "")
from mdisk import iswin

# startcommand
@app.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	await message.reply_text(text =f"""
ʜɪ {message.from_user.first_name } 👋
ɪ'ᴍ ᴘᴀɪᴅ ᴍᴅɪsᴋ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ 🚀\nᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ sᴜᴘᴘᴏʀᴛ💯\n
sᴇɴᴅ ᴍᴇ ᴀ ᴍᴅɪsᴋ ʟɪɴᴋ ᴀɴᴅ \nɪ ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ ɪᴛ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ᴀs ᴀ file/video.\n
ᴘʟᴇᴀsᴇ /upgrade ʏᴏᴜʀ sᴜʙsᴄʀɪᴘᴛɪᴏɴ
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👼 𝙳𝙴𝚅𝚂 👼", url='https://t.me/Aaajats')
           ],[
           InlineKeyboardButton('📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂', url='https://t.me/anumitultrabots'),
           InlineKeyboardButton('🍂 𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url='https://t.me/anumitultrabots')
           ],[
           InlineKeyboardButton('🍃 𝙰𝙱𝙾𝚄𝚃', callback_data='about'),
           InlineKeyboardButton('ℹ️ Subscribe 🧐', url='https://youtube.com/@anumitultrabots')
           ]]
          )
       )

# upgrade command
@app.on_message(filters.private & filters.command(["upgrade"]))
async def start(client,message):
	await message.reply_text(text =f"""
	Hello \n
	🛡️ PLAN 🛡️\n
	🌸Daily  Upload  limit Unlimited\n
	🌸Price Rs 40 🇮🇳/🌎 2$  per Month__
	
	💸Pay Using Upi I'd \namitk8270@fbl\n
	💸Pay Using qr code send /qr command\n
	💸After Payment Send Screenshots Of\nPayment To Admin
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Aaajats")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://www.paypal.me/ajak4406")],
		                [InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
       )
	
#plans command
@app.on_message(filters.private & filters.command(["plans"]))
async def start(client,message):
	await message.reply_text("""
	PAID PLANS AVAILABLE\n
	🛡️ PLAN 🛡️\n
	🌸Daily  Upload  limit Unlimited
	🌸Price Rs 40 🇮🇳/🌎 1$  per Month__
	🌸No Timeout\n
Please /upgrade your subscription
	""")
	
# qr code
@app.on_message(filters.private & filters.command(["qr"]))
async def start(client,message):
	await message.reply_photo("https://ibb.co/FBt9sv2"),
    
    
@app.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	await message.reply_text("📛 My Name : @renamerprov2_bot\n\n👨‍💻Creater :- @ajak4405\n\n🧿 Language :Python 3.10.8\n\n📢 Framework :Pyrogram 2.0.63\n\n🤖 Bot Server : VPS")


# check for user access
def checkuser(message):
    if auth != "" or ban != "":
        valid = 1
        if auth != "":
            authusers = auth.split(",")
            if str(message.from_user.id) not in authusers:
                valid = 0
        if ban != "":
            bannedusers = ban.split(",")
            if str(message.from_user.id) in bannedusers:
                valid = 0
        return valid        
    else:
        return 1


# download status
def status(folder,message,fsize):
    fsize = fsize / pow(2,20)
    length = len(folder)
    # wait for the folder to create
    while True:
        if os.path.exists(folder + "/vid.mp4.part-Frag0") or os.path.exists(folder + "/vid.mp4.part"):
            break
    
    time.sleep(3)
    while os.path.exists(folder + "/" ):
        if iswin == "0":
            result = subprocess.run(["du", "-hs", f"{folder}/"], capture_output=True, text=True)
            size = result.stdout[:-(length+2)]
        else:
            os.system(f"dir /a/s {folder} > tempS-{message.id}.txt")
            size = str(int(open(f"tempS-{message.id}.txt","r").readlines()[-2].split()[2].replace(",","")) // 1000000) + "MB "

        try:
            app.edit_message_text(message.chat.id, message.id, f"__Downloaded__ : **{size} **__of__**  {fsize:.1f}M**")
            time.sleep(10)
        except:
            time.sleep(5)

    if iswin != "0": os.remove(f"tempS-{message.id}.txt")


# upload status
def upstatus(statusfile,message):
    while True:
        if os.path.exists(statusfile):
            break

    time.sleep(3)      
    while os.path.exists(statusfile):
        with open(statusfile,"r") as upread:
            txt = upread.read()
        try:
            app.edit_message_text(message.chat.id, message.id, f"__Uploaded__ : **{txt}**")
            time.sleep(10)
        except:
            time.sleep(5)


# progress writter
def progress(current, total, message):
    with open(f'{message.id}upstatus.txt',"w") as fileup:
        fileup.write(f"{current * 100 / total:.1f}%")


# download and upload
def down(message,link):

    # checking link and download with progress thread
    msg = app.send_message(message.chat.id, '__Downloading__', reply_to_message_id=message.id)
    size = mdisk.getsize(link)
    if size == 0:
        app.edit_message_text(message.chat.id, msg.id,"__**Invalid Link**__")
        return
    sta = threading.Thread(target=lambda:status(str(message.id),msg,size),daemon=True)
    sta.start()

    # checking link and download and merge
    file,check,filename = mdisk.mdow(link,message)
    if file == None:
        app.edit_message_text(message.chat.id, msg.id,"__**Invalid Link**__")
        return

    # checking if its a link returned
    if check == -1:
        app.edit_message_text(message.chat.id, msg.id,f"__**Can't Download File but here is the Download Link : {file}**__")
        os.rmdir(str(message.id))
        return

    # checking size
    size = split.get_path_size(file)
    if(size > TG_SPLIT_SIZE):
        app.edit_message_text(message.chat.id, msg.id, "__Splitting__")
        flist = split.split_file(file,size,file,".", TG_SPLIT_SIZE)
        os.remove(file) 
    else:
        flist = [file]
    app.edit_message_text(message.chat.id, msg.id, "__Uploading__")
    i = 1

    # checking thumbline
    if not os.path.exists(f'{message.from_user.id}-thumb.jpg'):
        thumbfile = None
    else:
        thumbfile = f'{message.from_user.id}-thumb.jpg'

    # upload thread
    upsta = threading.Thread(target=lambda:upstatus(f'{message.id}upstatus.txt',msg),daemon=True)
    upsta.start()
    info = extras.getdata(str(message.from_user.id))

    # uploading
    for ele in flist:

        # checking file existence
        if not os.path.exists(ele):
            app.send_message(message.chat.id,"**Error in Merging File**",reply_to_message_id=message.id)
            return
            
        # check if it's multi part
        if len(flist) == 1:
            partt = ""
        else:
            partt = f"__**part {i}**__\n"
            i = i + 1

        # actuall upload
        if info == "V":
            thumb,duration,width,height = mediainfo.allinfo(ele,thumbfile)
            if not isPremmium : app.send_video(message.chat.id, video=ele, caption=f"{partt}**{filename}**", thumb=thumb, duration=duration, height=height, width=width, reply_to_message_id=message.id, progress=progress, progress_args=[message])
            else:
                with acc: tmsg = acc.send_video(temp_channel, video=ele, caption=f"{partt}**{filename}**", thumb=thumb, duration=duration, height=height, width=width, progress=progress, progress_args=[message])
                app.copy_message(message.chat.id, temp_channel, tmsg.id, reply_to_message_id=message.id)
            if "-thumb.jpg" not in thumb: os.remove(thumb)
        else:
            if not isPremmium : app.send_document(message.chat.id, document=ele, caption=f"{partt}**{filename}**", thumb=thumbfile, force_document=True, reply_to_message_id=message.id, progress=progress, progress_args=[message])
            else:
                with acc: tmsg = acc.send_document(temp_channel, document=ele, thumb=thumbfile, caption=f"{partt}**{filename}**", force_document=True, progress=progress, progress_args=[message])
                app.copy_message(message.chat.id, temp_channel, tmsg.id, reply_to_message_id=message.id)
       
        # deleting uploaded file
        os.remove(ele)
        
    # checking if restriction is removed    
    if check == 0:
        app.send_message(message.chat.id,"__Can't remove the **restriction**, you have to use **MX player** to play this **video**\n\nThis happens because either the **file** length is **too small** or **video** doesn't have separate **audio layer**__",reply_to_message_id=message.id)
    if os.path.exists(f'{message.id}upstatus.txt'):
        os.remove(f'{message.id}upstatus.txt')
    app.delete_messages(message.chat.id,message_ids=[msg.id])


# mdisk command
@app.on_message(filters.private & filters.command(["mdisk"]))
def mdiskdown(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """
	Your ARE NOT A PAID USER\n
Please /upgrade your subscription
	""",reply_to_message_id=message.id)
        return

    try:
        link = message.text.split("mdisk ")[1]
        if "https://mdisk.me/" in link:
            d = threading.Thread(target=lambda:down(message,link),daemon=True)
            d.start()
            return 
    except:
        pass

    app.send_message(message.chat.id, '**Send only __MDisk Link__ with command followed by the link**',reply_to_message_id=message.id)


# thumb command
@app.on_message(filters.private & filters.command(["thumb"]))
def thumb(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """
	Your ARE NOT A PAID USER\n
Please /upgrade your subscription
	""",reply_to_message_id=message.id)
        return

    try:
        if int(message.reply_to_message.document.file_size) > 200000:
            app.send_message(message.chat.id, '**Thumbline size allowed is < 200 KB**',reply_to_message_id=message.id)
            return

        msg = app.get_messages(message.chat.id, int(message.reply_to_message.id))
        file = app.download_media(msg)
        os.rename(file,f'{message.from_user.id}-thumb.jpg')
        app.send_message(message.chat.id, '**Thumbnail is Set**',reply_to_message_id=message.id)

    except:
        app.send_message(message.chat.id, '**reply __/thumb__ to a image document of size less than 200KB**',reply_to_message_id=message.id)


# show thumb command
@app.on_message(filters.private & filters.command(["show"]))
def showthumb(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """
	Your ARE NOT A PAID USER\n
Please /upgrade your subscription
	""",reply_to_message_id=message.id)
        return
    
    if os.path.exists(f'{message.from_user.id}-thumb.jpg'):
        app.send_photo(message.chat.id,photo=f'{message.from_user.id}-thumb.jpg',reply_to_message_id=message.id)
    else:
        app.send_message(message.chat.id, '**Thumbnail is not Set**',reply_to_message_id=message.id)


# remove thumbline command
@app.on_message(filters.private & filters.command(["remove"]))
def removethumb(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """
	Your ARE NOT A PAID USER\n
Please /upgrade your subscription
	""",reply_to_message_id=message.id)
        return
    
    
    if os.path.exists(f'{message.from_user.id}-thumb.jpg'):
        os.remove(f'{message.from_user.id}-thumb.jpg')
        app.send_message(message.chat.id, '**Thumbnail is Removed**',reply_to_message_id=message.id)
    else:
        app.send_message(message.chat.id, '**Thumbnail is not Set**',reply_to_message_id=message.id)


# thumbline
@app.on_message(filters.photo)
def ptumb(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """
	Your ARE NOT A PAID USER\n
Please /upgrade your subscription
	""",reply_to_message_id=message.id)
        return
    
    file = app.download_media(message)
    os.rename(file,f'{message.from_user.id}-thumb.jpg')
    app.send_message(message.chat.id, '**Thumbnail is Set**',reply_to_message_id=message.id)
    

# change mode
@app.on_message(filters.private & filters.command(["change"]))
def change(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """
	Your ARE NOT A PAID USER\n
Please /upgrade your subscription
	""",reply_to_message_id=message.id)
        return
    
    info = extras.getdata(str(message.from_user.id))
    extras.swap(str(message.from_user.id))
    if info == "V":
        app.send_message(message.chat.id, '__Mode changed from **Video** format to **Document** format__',reply_to_message_id=message.id)
    else:
        app.send_message(message.chat.id, '__Mode changed from **Document** format to **Video** format__',reply_to_message_id=message.id)

        
# multiple links handler
def multilinks(message,links):
    for link in links:
        d = threading.Thread(target=lambda:down(message,link),daemon=True)
        d.start()
        d.join()


# mdisk link in text
@app.on_message(filters.text)
def mdisktext(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if isPremmium and message.chat.id == temp_channel: return

    if not checkuser(message):
        app.send_message(message.chat.id, """
	Your ARE NOT A PAID USER\n
Please /upgrade your subscription
	""",reply_to_message_id=message.id)
        return

    if message.text[0] == "/":
        app.send_message(message.chat.id, '**See __/help__**',reply_to_message_id=message.id)
        return

    if "https://mdisk.me/" in message.text:
        links = message.text.split("\n")
        if len(links) == 1:
            d = threading.Thread(target=lambda:down(message,links[0]),daemon=True)
            d.start()
        else:
            d = threading.Thread(target=lambda:multilinks(message,links),daemon=True)
            d.start()   
    else:
        app.send_message(message.chat.id, '**Send only __MDisk Link__**',reply_to_message_id=message.id)


# polling
app.run()
