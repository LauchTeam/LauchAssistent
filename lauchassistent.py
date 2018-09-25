import handlerdb


class LauchAssistent:

    # Init
    def __init__(self):
        # variable definition
        self.database = handlerdb.HandlerDB()
        self.database.connect_to()

    def get_kpi(self, request):
        print("test")

    def process_request(self, request):

        action = request["queryResult"]["parameters"]["var_kpi"]

        if action == "EBIT":
            self.get_kpi(request)