from collections import deque

from telegram import Update
from telegram.ext import ContextTypes

from CrocoBot3 import history, user_ids, id_counter


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global id_counter
    user = update.message.from_user


    if user not in user_ids:
        user_ids[user] = id_counter
        id_counter += 1
        history.append([Update])
    else:
        user_id = user_ids[user]
        history[user_id].append(Update)
    user_id = user_ids[user]
    print(history)
    print(user_ids)


    await update.message.reply_text(f'Hello, {update.effective_user.first_name} I am CrocoBot3!')
    await update.message.reply_sticker('CAACAgIAAxkBAAPhZyM38YWFmp4Xh9d_XUdrkv2wcUcAAmtiAALteBBJnaR0rEgQZ2M2BA')
    await update.message.reply_text('choose one of those yummy commands bellow!')

    commands = ['/info - gives you some information about the bot and the author.', '/clear_history - clears the your history with this bot.']

    await update.message.reply_text('\n'.join(commands))