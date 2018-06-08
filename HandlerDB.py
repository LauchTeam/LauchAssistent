# Import mysql for easy db communication
import mysql.connector

class HandlerDB:
    
    # Init
    def __init__(self):       
        #variable definition
        self.DB = ""
    
    # Function: Connect to Database
    def ConntectTo(self, var_user, var_pass, var_host, var_db):
        try:
            # Establish Connection
            self.DB = mysql.connector.connect(user=var_user, password=var_pass, host=var_host, database=var_db)
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