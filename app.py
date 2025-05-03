from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import openai

# Step 1: তোমার API Key বসাও
openai.api_key = "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"

# Step 2: AI রিপ্লাই ফাংশন
async def chat_with_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a sweet, romantic girlfriend who replies in a mix of Bengali and English."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

# Step 3: স্টার্ট কমান্ড
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("হ্যালো! আমি তোমার মিষ্টি সঙ্গীনি! কথা বলো আমার সাথে...")

# Step 4: মেসেজ হ্যান্ডলার
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    reply = await chat_with_ai(user_text)
    await update.message.reply_text(reply)

# Step 5: বট রান করাও
app = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
