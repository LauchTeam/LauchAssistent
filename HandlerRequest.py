#Import json library for easy access
import json

#Class: handler to process requests
class HandlerRequest:
    
    #Init
    def __init__(self):       
        #variable definition
        self.var_request = []    
    
    #Function: Load Request
    def LoadRequest(self, var_file):     
        #open file and load into "var_request"
        self.var_request = json.load(open(var_file))
    
    #Function: return "par_country"
    def GetCountry (self):
        #find and return "par_country"
        return self.var_request["queryResult"]["parameters"]["par_country"]
    
    #Function: return "action"
    def GetAction (self):
        #find and return "action"
        return self.var_request["queryResult"]["action"]
