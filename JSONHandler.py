import json

def ReadJSON (var_path):

    var_response = json.load(var_path)
    print(var_response["action"])

ReadJSON(open('Request.json')