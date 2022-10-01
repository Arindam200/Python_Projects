import logging

from decouple import config

from telethon import TelegramClient, events

# initializing logger
logging.basicConfig(
    level=logging.INFO, format="[%(levelname)s] %(asctime)s - %(message)s"
)
log = logging.getLogger("TG_ECHO_BOT")

# fetching variales from env
try:
    BOT_TOKEN = config("BOT_TOKEN")
except Exception as ex:
    log.info(ex)

log.info("Connecting bot.")
try:
    bot = TelegramClient(None, 6, "eb06d4abfb49dc3eeb1aeb98ae0f581e").start(
        bot_token=BOT_TOKEN
    )
except BaseException as e:
    log.warning(e)
    exit(1)


# functions
@bot.on(events.NewMessage(pattern="/start$", func=lambda e: e.is_private))
async def on_start(event):
    await event.reply("I'm an echobot!")


@bot.on(events.NewMessage(func=lambda e: not e.text.startswith("/") and e.is_private))
async def new_echo(event):
    await event.reply(event.text, file=event.media, buttons=event.buttons)


log.info("\nBot has started.\n")
bot.run_until_disconnected()
