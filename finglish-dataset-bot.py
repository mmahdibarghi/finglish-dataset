import logging
import io
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

global counting
counting = 0
global file1
global Lines
users=[]
file1 = file1 = io.open("persian.txt", mode="r", encoding="utf-8")

Lines = file1.readlines()
from win_unicode_console import enable

enable()
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
         'سلام خیلی ممنون که با تیم ما همکاری می کنین ممنون میشیم در ادامه هر جمله فارسی که نمایش داده شد رو به فینگلیش برای ما ارسال بفرمایید')
    update.message.reply_text("خیلی ممنون از همراهی شما به کمک شما تعداد 2851 تکست فارسی به فینگلیش تبدیل شد به زودی تمامی این دیتاست به صورت اپن سورس در اکانت گیت هاب mmahdibarghi قرار خواهد گرفت!")
    global users
    users.append(update.message.chat.username)



def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'سلام خیلی ممنون که با تیم ما همکاری می کنین ممنون میشیم در ادامه هر جمله فارسی که نمایش داده شد رو به فینگلیش برای ما ارسال بفرمایید')
    print(users)

def echo(update, context):
    """Echo the user message."""
    global counting
    print(counting,update.message.text)

    counting+=1
    update.message.reply_text("خیلی ممنون از همراهی شما به کمک شما تعداد 2851 تکست فارسی به فینگلیش تبدیل شد به زودی تمامی این دیتاست به صورت اپن سورس در اکانت گیت هاب mmahdibarghi قرار خواهد گرفت!")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("YOURBOTTOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()


