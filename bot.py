import logging
from telegram import Update
from telegram.ext import ApplicationBuilder
from telegram.ext import ContextTypes, CommandHandler
import config

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text='hi there')

def main() -> None:
    application = ApplicationBuilder().token(config.TOKEN).build()

    application.add_handler(CommandHandler('start', start_command))
    application.run_polling()

if __name__ == '__main__':
    main()
