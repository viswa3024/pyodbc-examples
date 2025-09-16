from fastapi import FastAPI, HTTPException
import pyodbc

app = FastAPI(title="FastAPI + Azure SQL + pyodbc")

# 🔹 Connection settings
server   = ""
database = ""
username = ""
password = ""

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

def get_connection():
    return pyodbc.connect(connection_string)


@app.get("/")
def root():
    return {"message": "FastAPI with Azure SQL Server (pyodbc) running!"}


@app.get("/employees")
def get_employees():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM testshema.employee")

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return {"employees": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if 'conn' in locals():
            conn.close()


@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM testshema.employee WHERE id = ?", emp_id)

        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Employee not found")

        columns = [column[0] for column in cursor.description]
        return dict(zip(columns, row))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if 'conn' in locals():
            conn.close()
