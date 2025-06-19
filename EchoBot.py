from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Step 1: Echo function — jo user ka message reply karega
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"Tune kaha: {user_message}")

# Step 2: Bot Setup — Token ke saath bot ko initialize karna
app = ApplicationBuilder().token("8014156247:AAEDdPaij7xHYLGijtglxZJlaXafRrt9lkM").build()

# Step 3: Add Message Handler
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Step 4: Run the bot
print("✅ Bot is running...")
app.run_polling()
