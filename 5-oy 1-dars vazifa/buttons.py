from telebot.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup


def phone_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("Telefon raqamni yuborish",request_contact=True)
    markup.add(btn)
    return markup

def menu_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn = KeyboardButton("🍔 Menyu")
    btn1 = KeyboardButton("🛒 Buyurtma berish")
    btn2 = KeyboardButton("📦 Mening buyurtmalarim")
    btn3 = KeyboardButton("❌ Buyurtmani bekor qilish")
    btn4 = KeyboardButton("👤 Profil")
    btn5 = KeyboardButton("ℹ️ Yordam")
    markup.add(btn,btn1,btn2,btn3,btn4,btn5)
    return markup

def food_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn = KeyboardButton("Burger🍔 - 25_000 So'm")
    btn1 = KeyboardButton("Pizza🍕 - 45_000 so'm")
    btn2 = KeyboardButton("Lavash🌯 - 30_000 so'm")
    btn3 = KeyboardButton("Hot-dog🌭 - 20_000 so'm")
    btn4 = KeyboardButton("Cola - 10_000 so'm")
    markup.add(btn,btn1,btn2,btn3,btn4)
    return markup

def inline_confirm():
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("Tastiqlang",callback_data="confirm")
    btn1 = InlineKeyboardButton("Bekor qilish",callback_data="cancel")
    markup.add(btn,btn1)
    return markup
