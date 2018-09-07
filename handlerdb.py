import psycopg2


class HandlerDB:

    # Init
    def __init__(self):
        # variable definition
        self.DB = ""

    # Function: Connect to Database
    def connectto(self):
        try:

            # Parameter for DB connection
            params = {
                'dbname': 'lauchassistent',
                'user': 'lauchassistent',
                'password': 'Lauchistsuper18!',
                'host': 'localhost',
                'port': 5432
            }

            # Establish Connection
            self.DB = psycopg2.connect(**params)

            # return success
            return True

        except:
            # Error message
            return False

    # Function: Execute SQL Statement and return result
    def execute(self, sql_statement):
        # Execute SQL Statement
        exe = self.DB.
        exe.execute(sql_statement)

        # Save result
        result = exe.fetchall()

        # return result
        return result

    # Funtion: Close Connection
    def closeconnection(self):
        self.DB.close()