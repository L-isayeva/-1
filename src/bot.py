from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "8901001974:AAH5BtlcQUJniGz9qMh0DtmJRO0keleCCy0"

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["Правила", "Цель игры"],
        ["Подготовка", "Ход игры"],
        ["Здания", "Рабочие"],
        ["Рынок", "Помощь"]
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Привет! Я бот-помощник по игре «Лаборатория успеха».\n\n"
        "Я могу помочь тебе быстро разобраться в правилах, подготовке к игре, "
        "порядке хода и основных игровых элементах.\n\n"
        "Выбери нужный раздел в меню или используй команды:\n"
        "/rules — краткие правила\n"
        "/goal — цель игры\n"
        "/setup — подготовка к игре\n"
        "/turn — порядок хода\n"
        "/buildings — про здания\n"
        "/workers — про рабочих\n"
        "/market — про рынок предложений\n"
        "/help — список команд"
    )
    await update.message.reply_text(text, reply_markup=MAIN_KEYBOARD)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Доступные команды:\n\n"
        "/start — запуск бота\n"
        "/help — список команд\n"
        "/rules — краткие правила\n"
        "/goal — цель игры\n"
        "/setup — подготовка к игре\n"
        "/turn — порядок хода\n"
        "/buildings — информация о зданиях\n"
        "/workers — информация о рабочих\n"
        "/market — информация о рынке предложений"
    )
    await update.message.reply_text(text, reply_markup=MAIN_KEYBOARD)

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "«Лаборатория успеха» — настольная экономическая стратегическая игра "
        "о распределении ресурсов, развитии своей компании и конкуренции с другими игроками.\n\n"
        "Количество игроков: 2–4\n"
        "Время партии: около 90 минут\n\n"
        "Игроки строят предприятия, нанимают рабочих, управляют ресурсами, "
        "используют рынок предложений и стремятся выполнить условия победы раньше остальных."
    )
    await update.message.reply_text(text, reply_markup=MAIN_KEYBOARD)

async def goal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Цель игры — развить свои предприятия и решить глобальные экономические "
        "задачи раньше остальных игроков.\n\n"
        "Победа зависит от того, насколько грамотно игрок управляет ресурсами, "
        "развивает здания, использует рабочих и строит стратегию."
    )
    await update.message.reply_text(text, reply_markup=MAIN_KEYBOARD)

async def setup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Подготовка к игре:\n\n"
        "1. Разместите стартовые здания по регионам.\n"
        "2. Разместите стартовых рабочих.\n"
        "3. Каждый игрок получает стартовый капитал в размере 30.\n"
        "4. Каждый игрок получает карту заданий.\n"
        "5. Выбирается первый игрок.\n\n"
        "После этого партия может начинаться."
    )
    await update.message.reply_text(text, reply_markup=MAIN_KEYBOARD)

async def turn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Порядок хода в игре:\n\n"
        "1. Этап события\n"
        "   - открывается карта события новой недели\n"
        "   - игроки получают ресурсы и применяют эффект карты\n\n"
        "2. Этап обновления\n"
        "   - обновляется рынок предложений\n"
        "   - появляются новые рабочие\n\n"
        "3. Этап действий\n"
        "   - игроки строят здания\n"
        "   - нанимают рабочих\n"
        "   - улучшают здания\n"
        "   - покупают предложения\n"
        "   - торгуют и используют эффекты"
    )
    await update.message.reply_text(text, reply_markup=MAIN_KEYBOARD)

async def buildings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Здания — основные активы игрока, приносящие доход.\n\n"
        "Они делятся на:\n"
        "- производственные\n"
        "- коммерческие\n"
        "- научные\n\n"
        "Здания можно улучшать до 2 и 3 уровня. "
        "При заполнении здания подходящими рабочими оно начинает приносить прибыль."
    )
    await update.message.reply_text(text, reply_markup=MAIN_KEYBOARD)

async def workers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Рабочие — сотрудники ваших предприятий.\n\n"
        "Они делятся по:\n"
        "- уровню квалификации\n"
        "- типу деятельности\n\n"
        "Рабочие нанимаются с рынка труда или через эффекты карт. "
        "Их правильное распределение влияет на эффективность зданий."
    )
    await update.message.reply_text(text, reply_markup=MAIN_KEYBOARD)

async def market(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Рынок предложений — это набор доступных услуг, карт и возможностей, "
        "которые игроки могут использовать для усиления своей стратегии.\n\n"
        "Через рынок можно получать дополнительные эффекты, рабочих и преимущества."
    )
    await update.message.reply_text(text, reply_markup=MAIN_KEYBOARD)

async def text_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()

    if user_text == "правила":
        await rules(update, context)
    elif user_text == "цель игры":
        await goal(update, context)
    elif user_text == "подготовка":
        await setup(update, context)
    elif user_text == "ход игры":
        await turn(update, context)
    elif user_text == "здания":
        await buildings(update, context)
    elif user_text == "рабочие":
        await workers(update, context)
    elif user_text == "рынок":
        await market(update, context)
    elif user_text == "помощь":
        await help_command(update, context)
    else:
        await update.message.reply_text(
            "Я пока не знаю такой команды. Нажми кнопку на клавиатуре или используй /help",
            reply_markup=MAIN_KEYBOARD
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("rules", rules))
    app.add_handler(CommandHandler("goal", goal))
    app.add_handler(CommandHandler("setup", setup))
    app.add_handler(CommandHandler("turn", turn))
    app.add_handler(CommandHandler("buildings", buildings))
    app.add_handler(CommandHandler("workers", workers))
    app.add_handler(CommandHandler("market", market))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_menu))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
