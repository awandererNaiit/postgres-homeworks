import csv
import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    host='local',
    database='north',
    user='postgres',
    password='Levis501',
)
cursor = conn.cursor()


# Функция для загрузки данных из CSV файла в таблицу
def load_data_from_csv(file_path, table_name):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if table_name == 'employees':
                cursor.execute(
                    "INSERT INTO employees (first_name, last_name, position, hire_date) VALUES (%s, %s, %s, %s)",
                    row
                )
            elif table_name == 'customers':
                cursor.execute(
                    "INSERT INTO customers (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)",
                    row
                )
            elif table_name == 'orders':
                cursor.execute(
                    "INSERT INTO orders (order_date, customer_id, total_amount, employee_id) VALUES (%s, %s, %s, %s)",
                    row
            )
    conn.commit()


# Загрузка данных в каждую таблицу
load_data_from_csv('path_to_employees_data.csv', 'employees')
load_data_from_csv('path_to_customers_data.csv', 'customers')
load_data_from_csv('path_to_orders_data.csv', 'orders')

# Закрытие соединения с базой данных
cursor.close()
conn.close()
