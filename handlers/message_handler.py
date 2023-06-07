from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes
from telegram import Update

from methods.login import LoginManager
from utils.db_cache import db_cache
from cache.cache_session import get_position

loginManager = LoginManager()
     
@db_cache
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, db):
    
    print('---------')
    chat_id = update.effective_chat.id
    pos = get_position(chat_id, db)
    
    messages_pointer = {
        'login': lambda : loginManager.manager(update, context)
    }
    
    if pos.split('_')[0] in messages_pointer:
        await messages_pointer[pos.split('_')[0]]()

    # positions_pointer = {
    #     # 'menu': lambda : menu(update, context),
    # }
    # if update.message.text in messages_pointer:

    #     await messages_pointer[update.message.text]()
    
    # # elif user['pos'] in positions_pointer:

    # #     await positions_pointer[user['pos']]()

