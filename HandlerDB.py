# Import mysql for easy db communication
import mysql.connector
import psycopg2

class HandlerDB:
    
    # Init
    def __init__(self):       
        # variable definition
        self.DB = ""
    
    # Function: Connect to Database
    def connectTo(self):
        try:
            # Data
            params = {
            'database': 'xershoxx',
            'user': 'flo.ries',
            'password': 'florian1',
            'host': '37.221.193.30',
            'port': 5432
            }
            self.DB = psycopg2.connect(**params)

            # Establish Connection
            # return success
            return True
        except:
            # Error message
            return False
    
    # Function: Execute SQL Statement and return result
    def Execute(self, sql_statement):
        # Execute SQL Statement
        self.Exec = self.DB.cursor()
        self.Exec.execute(sql_statement)

        # Save result
        result = self.Exec.fetchall()

        # return result
        return result

    # Funtion: Close Connection
    def CloseConnection(self):
        self.DB.close()
