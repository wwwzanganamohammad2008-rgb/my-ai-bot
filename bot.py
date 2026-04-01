import telebot
import google.generativeai as genai
import os

# جلب المفاتيح من الخادم (سنقوم بضبطها لاحقاً في موقع الاستضافة)
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GEMINI_KEY = os.getenv('GEMINI_KEY')

# إعداد ذكاء جيميناي
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# إعداد البوت
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        # إرسال رسالة المستخدم لجيميناي والحصول على رد
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "عذراً، حدث خطأ بسيط، حاول مرة أخرى.")

# تشغيل البوت للأبد
bot.infinity_polling()

