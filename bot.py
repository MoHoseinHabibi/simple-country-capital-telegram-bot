import logging
from telegram import Update
from telegram.ext import ApplicationBuilder
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
import config
import sqlite3

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# connecting to databse
con = sqlite3.connect('country.db')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = 'به ربات خوش آمدید\n برای دریافت اطلاعات پایخت کشور و جمعیت آن نام کشور را به فارسی ارسال کنید.\n تعداد 244 کشور ثبت شده.'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def search_country(text: str) -> tuple[str, int] | None:
    cur = con.cursor()
    res = cur.execute("SELECT capital, capital_population FROM country WHERE country_name = ?", (text,))
    return res.fetchone()


async def search_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    res = search_country(update.message.text)
    if res is None:
        await update.message.reply_text('کشور مورد نظر یافت نشد.')
    await update.message.reply_text(f'کشور: {update.message.text}\n پایتخت: {res[0]}\n جمعیت پایتخت: {res[1]}', quote=True)


def main() -> None:
    application = ApplicationBuilder().token(config.TOKEN).build()

    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(MessageHandler(filters.TEXT, search_handler))
    application.run_polling()


if __name__ == '__main__':
    main()
