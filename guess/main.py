from telethon import events, TelegramClient
import os
import asyncio

api_id = 29107619
api_hash = 'e41eeb9826cda29f3bb1da6a4b28bad0'
guessSolver = TelegramClient('saitama/temp', api_id, api_hash)
chatid = 1002364525862#change
from telethon.tl.types import PhotoStrippedSize
@guessSolver.on(events.NewMessage(from_users=5289069294, pattern=".bin",outgoing=True))
async def guesser(event):
    await guessSolver.send_message(entity=chatid,message='/guess')
    for i in range(1,3000):
        await asyncio.sleep(300)
        await guessSolver.send_message(entity=chatid,message='/guess')
@guessSolver.on(events.NewMessage(from_users=572621020, pattern="Who's that pokemon?",chats=(int(chatid)),incoming=True))
async def guesser(event):
    for size in event.message.photo.sizes:
        if isinstance(size, PhotoStrippedSize):
            size = str(size)
            for file in (os.listdir("cache/")):
                with open(f"cache/{file}", 'r') as f:
                    file_content = f.read()
                if file_content == size:
                     chat = await event.get_chat()
                     Msg = file.split(".txt")[0]
                     await guessSolver.send_message(chat,Msg)
                     await asyncio.sleep(10)
                     await guessSolver.send_message(chat,"/guess")
                     break
            with open("saitama/cache.txt", 'w') as file:
                file.write(size)
            file.close()
                         
@guessSolver.on(events.NewMessage(from_users=572621020, pattern="The pokemon was ",chats=int(chatid)))
async def guesser(event):
    massage = ((event.message.text).split("The pokemon was **")[1]).split("**")[0]
    with open(f"cache/{massage}.txt", 'w') as file:
        with open("saitama/cache.txt",'r') as inf:
            cont = inf.read()
            file.write(cont)
        inf.close()
    file.close()
    os.remove("saitama/cache.txt")
    chat = await event.get_chat()
    await guessSolver.send_message(chat, "/guess")

             
guessSolver.start()
guessSolver.run_until_disconnected()