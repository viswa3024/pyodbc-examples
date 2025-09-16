import pyodbc

# Connection details
server   = ''
database = ''
username = ''
password = ''

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

    # 🔹 Run your query
    cursor.execute("SELECT * FROM testshema.employee")

    # Fetch all rows
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)   # row is a tuple
except Exception as e:
    print("Error:", e)
finally:
    if 'conn' in locals():
        conn.close()
