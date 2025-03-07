import pyodbc 



#Connect SQL server

def db_conn():
    conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=MUKESH-JAYKAR;"
    "Database=LINE2_REPORT_3;"
    "UID=sa;"
    "PWD=admin@123;"
    )
   
    # conn = pyodbc.connect(conn_str)
    conn = pyodbc.connect(conn_str)
    return conn