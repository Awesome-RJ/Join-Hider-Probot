import os

from pyrogram import Client, filters
from pyrogram.types import Message, User

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

pgram = Client(
        "hide",
        bot_token=BOT_TOKEN,
	      api_hash=API_HASH,
        api_id=API_ID
    )

@pgram.on_message(filters.command('start'))
async def start(bot, message):
	text = 'Hey, Im a Join Hider Probot\n\n I Can Delete A Member joined Message.\n\n Add Me To Your Group And Give permission Of delete message.'
	await message.reply(text, quote=True)

@pgram.on_message(filters.new_chat_members)
async def welcome(bot, message):
	await message.delete()	
	
@pgram.on_message(filters.left_chat_member)
async def goodbye(bot, message):
	await message.delete()	
	
pgram.run()
