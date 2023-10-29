import API_token as keys
from telegram.ext import *
import regexmatch
import trade

print('Bot started....')
    
async def handle_message(update, context):
    call=str(update.channel_post.text).lower()
    api_call=regexmatch.handle_call(call)
    trade.execute(api_call)
    print('Trade executed')

def error(update, context):
    print(f'Update {update} caused error {context.error}')

def main():
    application = Application.builder().token(keys.BOT_KEY).build()
    application.add_handler(MessageHandler(filters.Chat(-1001901736871), handle_message))
    
    application.run_polling(1)

main()