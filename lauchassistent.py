import handlerdb


class LauchAssistent:

    # Init
    def __init__(self):
        # variable definition
        self.database = handlerdb.HandlerDB()
        self.database.connect_to()

    def __del__(self):
        self.database.close_connection()

    def get_kpi(self, request):
        kpi_name = request["queryResult"]["parameters"]["var_kpi"]
        kpi_value = self.database.get_result(
            """SELECT "KPI_VALUE" FROM finance.table_kpi WHERE "KPI_NAME" = '""" + request["queryResult"]["parameters"][
                "var_kpi"] + """';""")

        message = "Die KPI " + kpi_name + " hat folgenden Wert: " + str(kpi_value)

        return message

    def get_country(self, request):
        country_name = request["queryResult"]["parameters"]["var_country"]
        date = self.database.get_result(
            """SELECT "KPI_VALUE" FROM football.table_kpi WHERE "KPI_NAME" = '""" + request["queryResult"]["parameters"][
                "var_country"] + """';""")

        message = country_name + " spielt das nächste mal: " + str(date)

        return message

    def process_request(self, request):
        action = request["queryResult"]["action"]

        if action == "act_kpi":
            return self.get_kpi(request)
        elif action == "act_country":
            return self.get_country(request)