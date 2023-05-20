from typing import Final

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final = '6115974222:AAGrSQXYhLBDOeaJ7kozITYr9UOMW3SwqE0'
BOT_USERNAME: Final = '@DrBanana520_Bot'


# create a start command

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m Dr.Banana520_Bot')


# Lets us use the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text('Do you feel like something wrong with your body, I am here to diagnose you')


# Lets us use the /custom command
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')



#handling responses

def handling_response(text: str) -> str:
    # Create your own response logic
    user_message = str(text).lower()


    greetings = ["hello", "sup", "hey ", "good", 'hi']

    if any( [greet in user_message for greet in greetings] ):
        return 'Hey there, my name is Banana520_Bot!'
    
    sos = ['help', 'save']

    if any( [help in user_message for help in sos] ):
        return "Let me help you to diagnose and type down your symptoms"
    
    panic = ['panicking', 'quickly']

    if any( [calm in user_message for calm in panic] ):
        return "Please calm down, I\'m here to help you"
    


    return 'I don\'t understand'


#handle messaging
async def handling_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text


    print(f' User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handling_response(new_text)
        else:
            return 
    else:
        response: str = handling_response(text)
    
    print('Bot: ', response)
    await update.message.reply_text(response)

#errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))


    #messages
    app.add_handler(MessageHandler(filters.TEXT, handling_message))

    #error
    app.add_error_handler(error)


    #polls the bot
    print('Polling....')
    app.run_polling(poll_interval=5)
     


