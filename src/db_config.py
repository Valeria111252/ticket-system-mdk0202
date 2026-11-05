SERVER = "localhost\\SQLEXPRESS"
DATABASE = "TicketSystem"
DRIVER = "{ODBC Driver 17 for SQL Server}"

CONNECTION_STRING = (
    f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;"
)


def get_connection_string():
    return CONNECTION_STRING


def test_connection_stub():
    print("Попытка подключения к БД...")
    return True
