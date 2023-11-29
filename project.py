from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler


key_token = "" #Masukkan KEY-TOKEN BOT 
user_bot = "" #Masukkan @user bot


async def  start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Gunakan /help untuk menampilkan apa yang dapat saya berikan..")
    
async def  help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kirim pesan, bot akan membalas pesan..")


async def  text_massage(update: Update, context:ContextTypes.DEFAULT_TYPE):
    text_diterima : str = update.message.text
    print(f"Pesan diterima : {text_diterima}")
    text_lwr_diterima = text_diterima.lower()
    if 'haiiii' in text_lwr_diterima:
        await update.message.reply_text("hai haiii")
    elif 'selamat pagi' in text_lwr_diterima:
        await update.message.reply_text("Selamat pagi..., semangat jalanin aktivitas 😊")
    elif 'siapa kamu ?' in text_lwr_diterima:
        await update.message.reply_text(f" aku adalah  : {user_bot}")
    elif'apakah kamu tau bunyi tikus?'in text_diterima:
        await update.message.reply_text(f"cit cit cit")
    elif'apakah kamu tau suara kambing?'in text_diterima:
        await update.message.reply_text(f"mbekkk mbekkk")
    elif'apakah kamu ngerasa sangat capek?'in text_diterima:
        await update.message.reply_text(f"saya tidak ngerasa sangat capek ")
    else:
        await update.message.reply_text("bot tidak mengerti")


async def photo_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("Gambar kamu bagus")
        
async def  error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"error... : {context.error}")


if __name__ == '__main__':
    print("Mulai")
    app = Application.builder().token(key_token).build()
    #COMMAND :
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    #MESSAGE:
    app.add_handler(MessageHandler(filters.TEXT, text_massage))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))
    #error :
    app.add_error_handler(error)
    #polling :
    app.run_polling(poll_interval=1)


