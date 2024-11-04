from telegram import Update
from telegram.ext import ContextTypes

from CrocoBot3 import history

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    if user in history:
        history[user].append('/info')
    else:
        history[user] = ['/info']
    await update.message.reply_text('Bot username  -  @fedi4Bot')
    await update.message.reply_text('This bot is created by @Fedi4Karev. Just for FUN.')
    contacts = ['LeetCode  -  https://leetcode.com/u/fedi41-prog/', 'Github  -  https://github.com/fedi41-prog']
    for i in contacts:
        await update.message.reply_text(i)