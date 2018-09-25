from flask import Flask, request, Response, json
import handlerdb
app = Flask(__name__)


@app.route('/lauchassistent', methods=['GET', 'POST'])
def get_request():
    db = handlerdb.HandlerDB()
    data = request.get_json()

    db.connect_to()

    kpi_name = data["queryResult"]["parameters"]["var_kpi"]
    kpi_value = db.get_result("""SELECT "KPI_VALUE" FROM finance.table_kpi WHERE "KPI_NAME" = '""" + data["queryResult"]["parameters"]["var_kpi"] + """';""")

    message = "Die KPI " + kpi_name + " hat folgenden Wert: " + str(kpi_value)

    answer = {"fulfillmentText": "Answer", "fulfillmentMessages": [{"text": {"text": [message]}}]}
    js = json.dumps(answer)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['test'] = 'Testheader'

    db.close_connection()

    return resp


# if __name__ ==  "__main__":
#    app.run(host='0.0.0.0', port='443', debug=False, ssl_context='adhoc')
