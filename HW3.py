import sqlite3
import telebot

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'


connection = sqlite3.connect('tickets.db')
cursor = connection.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS tickets
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   destination TEXT,
                   price REAL,
                   available INTEGER)''')


cursor.execute("INSERT INTO tickets (destination, price, available) VALUES ('London', 200.0, 5)")
cursor.execute("INSERT INTO tickets (destination, price, available) VALUES ('Paris', 150.0, 3)")
cursor.execute("INSERT INTO tickets (destination, price, available) VALUES ('New York', 500.0, 2)")

connection.commit()


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Чтобы увидеть доступные билеты, отправьте команду /tickets.")


@bot.message_handler(commands=['tickets'])
def send_tickets(message):
    cursor.execute("SELECT * FROM tickets WHERE available > 0")
    tickets = cursor.fetchall()

    if not tickets:
        bot.reply_to(message, "Извините, в данный момент нет доступных билетов.")
    else:
        response = "Доступные билеты:\n"
        for ticket in tickets:
            ticket_id, destination, price, available = ticket
            response += f"ID: {ticket_id}, Место: {destination}, Цена: {price}$, Доступно: {available}\n"

        bot.reply_to(message, response)


@bot.message_handler(commands=['buy'])
def buy_ticket(message):
    try:
        _, ticket_id = message.text.split()
        ticket_id = int(ticket_id)

        cursor.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,))
        ticket = cursor.fetchone()

        if ticket:
            _, destination, price, available = ticket
            if available > 0:
                cursor.execute("UPDATE tickets SET available = available - 1 WHERE id = ?", (ticket_id,))
                connection.commit()
                bot.reply_to(message, f"Вы успешно приобрели билет на {destination} за {price}$.")
            else:
                bot.reply_to(message, "Извините, этот билет уже распродан.")
        else:
            bot.reply_to(message, "Билет с указанным ID не найден.")
    except:
        bot.reply_to(message, "Неправильный формат команды. Используйте /buy <ID билета>.")



bot.polling()


connection.close()

