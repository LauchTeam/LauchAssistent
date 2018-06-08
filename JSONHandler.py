#Import json library for easy access
import json

#Function: read json file and return 'par_country'
def ReadJSON (var_path):

    #load document
    var_response = json.load(open(var_path))

    #find and return 'par_country'
    return var_response["queryResult"]["parameters"]["par_country"]
