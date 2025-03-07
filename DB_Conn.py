import pyodbc 



#Connect SQL server

def db_conn():
    conn_str = (
    f"Driver={ODBC Driver 17 for SQL Server};"
    f"Server={os.getenv('MUKESH-JAYKAR')};"
    f"Database={os.getenv('LINE2_REPORT_3')};"
    f"UID={os.getenv('sa')};"
    f"PWD={os.getenv('admin@123')};"
    )
   
    # conn = pyodbc.connect(conn_str)
    conn = pyodbc.connect(conn_str)
    return conn
