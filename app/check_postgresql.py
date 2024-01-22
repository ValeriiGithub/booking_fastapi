"""
Для проверки получения данных из PostgreSQL
"""

import psycopg2

# Создайте соединение с вашей базой данных
conn = psycopg2.connect(
    dbname="your_database_name",
    user="your_username",
    password="your_password",
    host="localhost",  # Или другой хост, если ваша база данных расположена на удаленном сервере
    port="5432"  # Или другой порт, если он отличается от порта по умолчанию
)

# Создайте курсор для выполнения запросов к базе данных
cur = conn.cursor()

# Выполните SQL-запрос
cur.execute("SELECT * FROM your_table_name")

# Получите результаты запроса
rows = cur.fetchall()

# Выведите результаты
for row in rows:
    print(row)

# Закройте соединение с базой данных
cur.close()
conn.close()
