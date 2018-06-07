import json

def ReadJSON (var_path):

    var_response = json.load(open(var_path))
    return var_response['par_country']