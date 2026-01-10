from telebot import TeleBot
from telebot.types import Message,CallbackQuery
from telebot.states import State,StatesGroup
from telebot.storage import StateMemoryStorage
from telebot.custom_filters import StateFilter
from mytoken import TOKEN
from buttons import phone_button,menu_button,food_button,inline_confirm
from database import db

storage = StateMemoryStorage()
bot = TeleBot(TOKEN,state_storage=storage,parse_mode="HTML")
bot.add_custom_filter(StateFilter(bot))

class RegisterState(StatesGroup):
    Name = State()
    Phone = State()
    Food = State()  
    Quantity = State()
    Confirm = State()

@bot.message_handler(commands=["start"])
def start(message: Message):
    chat_id = message.chat.id

    bot.set_state(chat_id,RegisterState.Name)
    bot.send_message(chat_id,"Assalomu alaykum!!\nIsm-Familyangizni kiriting:")
@bot.message_handler(state = RegisterState.Name)
def reaction_to_name(message:Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id

    with bot.retrieve_data(from_user_id,chat_id) as data:
        data["name"] = message.text
    bot.set_state(chat_id, RegisterState.Phone)
    bot.send_message(chat_id,"Telefon raqamni yuboring",reply_markup=phone_button())

@bot.message_handler(state = RegisterState.Phone, content_types=["contact"])
def reaction_to_phone_number(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id

    with bot.retrieve_data(from_user_id,chat_id) as data:
        data["phone"] = message.contact.phone_number

    bot.send_message(chat_id,"Muvaffaqiyatli royxatdan otildi\nAsosiy menu",reply_markup=menu_button())

@bot.message_handler(func=lambda x: x.text == "🛒 Buyurtma berish")
def food(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    bot.set_state(chat_id,RegisterState.Food)
    bot.send_message(chat_id,"qaysi taomni tanlaysiz",reply_markup=food_button())
@bot.message_handler(state = RegisterState.Food)
def foods(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id

    with bot.retrieve_data(from_user_id,chat_id) as data:
        data["food"] = message.text
    bot.set_state(chat_id,RegisterState.Quantity)
    bot.send_message(chat_id,"Nechta buyurtma qilasiz")
@bot.message_handler(state = RegisterState.Quantity)
def soni(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id

    with bot.retrieve_data(from_user_id,chat_id) as data:
        data["soni"] = message.text
        ism = data["full_name"]
        phone = data["phone"]
        quantity = data["soni"]
    bot.set_state(chat_id,RegisterState.Confirm)
    bot.send_message(chat_id,f"Ismi: {ism}\nTel: {phone}\nSoni: {quantity}\nTastiqlaysizmi",reply_markup=inline_confirm())

@bot.callback_query_handler(state = RegisterState.Confirm)
def confirm(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id

    if call.data == "confrim":
        db.insert_users()


if __name__ == "__main__":
    print("bot ishga tushdi")
    db.create_tables()
    bot.infinity_polling()

#vaqtim bolmadi domla kecha uyda emasdim noutbook yogidi sunga