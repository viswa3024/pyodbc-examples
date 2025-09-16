import pyodbc

# Replace with your details
server   = ''
database = ''
username = ''
password = ''

# ODBC connection string
connection_string = (
    "Driver={ODBC Driver 18 for SQL Server};"
    f"Server=tcp:{server},1433;"
    f"Database={database};"
    f"Uid={username};"
    f"Pwd={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION;")
    row = cursor.fetchone()
    print("Connected to SQL Server!")
    print("SQL Server version:", row[0])
except Exception as e:
    print("Error:", e)
finally:
    if 'conn' in locals():
        conn.close()
