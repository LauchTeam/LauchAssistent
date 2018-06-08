# import mysql for easy db communication
import mysql.connector

class HandlerDB:
    
    #Init
    def __init__(self):       
        #variable definition
        self.DB = ""
    
    def ConntectTo(self, var_user, var_pass, var_host, var_db):
        try:
            self.DB = mysql.connector.connect(user=var_user, password=var_pass, host=var_host, database=var_db)
            return "Successful connected"
        except:
            return "No Connection"
        
    def Execute(self, sql_statement):
        self.Exec = self.DB.cursor()
        self.Exec.execute(sql_statement)

        result = self.Exec.fetchall()

        return result

    def CloseConnection(self):
        self.DB.close()