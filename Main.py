# import needed classes
import datetime
import HandlerRequest
import HandlerDB

class HandlerAction():

    # Init
    def __init__(self):       
        # variable definition
        self.handler_request = HandlerRequest.HandlerRequest()
        self.handler_db = HandlerDB.HandlerDB()
        self.var_country = ""
        self.var_date = ""
        self.var_action = ""

        # connect to DB
        self.handler_db.connectTo()

    def GetCountry(self):
        # Get Country from Request-File
        self.var_country = self.handler_request.GetCountry()

    def GetDate(self):
        # get date from database
        tmp_date = self.handler_db.Execute("SELECT * FROM lauchdb.table_test WHERE test_name = '" + self.var_country + "';")
        # TODO: change format of tmp_date
        self.var_date = tmp_date

    def ChooseAction(self, request):
        # load request
        self.handler_request.LoadRequest(request)
        # get the requested action
        self.var_action = self.handler_request.GetAction()

        # choose code to fulfill action
        if self.var_action == "act_country":
            # get next game data
            self.GetCountry()
            self.GetDate()
            # print next game
            print(self.var_country + "s next match: " + str(self.var_date))
        # action not known yet
        else:
            print("Can't handle that action yet.")

# test code
test = HandlerAction()
test.ChooseAction("Request.json")

