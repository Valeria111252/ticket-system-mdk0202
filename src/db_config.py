# db_config.py
# Конфигурация подключения к базе данных тикет-системы

SERVER = 'localhost\\SQLEXPRESS'
DATABASE = 'TicketSystem'
DRIVER = '{ODBC Driver 17 for SQL Server}'

# Строка подключения для библиотеки pyodbc
CONNECTION_STRING = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'


def get_connection_string():
    """Возвращает строку подключения к БД (заглушка для первого цикла)"""
    return CONNECTION_STRING


def test_connection_stub():
    """Заглушка функции проверки подключения"""
    print("Попытка подключения к БД...")
    # В следующем цикле разработки здесь будет реальный код через pyodbc
    return True