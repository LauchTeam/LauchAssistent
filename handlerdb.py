import psycopg2


class HandlerDB:

    # Init
    def __init__(self):
        # variable definition
        self.DB = ""

    # Function: Connect to Database
    def connect_to(self):
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
    def get_result(self, sql_statement):
        # Execute SQL Statement
        cur = self.DB.cursor()
        cur.execute(sql_statement)

        # Save result
        result = cur.fetchone()[0]

        # return result
        return result

    # Function: Close Connection
    def close_connection(self):
        self.DB.close()