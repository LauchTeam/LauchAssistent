from flask import Flask, request, Response, json
import handlerdb
app = Flask(__name__)


@app.route('/lauchassistent', methods=['GET', 'POST'])
def hello_world():
    db = handlerdb.HandlerDB()
    data = request.get_json()

    db.connectto()

    kpi_name = data["queryResult"]["parameters"]["var_kpi"]
    # kpi_value = db.getresult("SELECT kpi_value FROM finance.table_kpi WHERE kpi_name = '" + data["queryResult"]["parameters"]["var_kpi"] + "';")
    kpi_value = db.getresult("""SELECT "KPI_VALUE" FROM finance.table_kpi WHERE "KPI_NAME" = '""" + data["queryResult"]["parameters"]["var_kpi"] + """';""")

    message = "Die KPI " + kpi_name + " hat folgenden Wert: " + str(kpi_value)

    print(kpi_value)
    print(str(kpi_value))

    answer = {"fulfillmentText": "hello world", "fulfillmentMessages": [{"text": {"text": [message]}}]}
    js = json.dumps(answer)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['test'] = 'Testheader'

    db.closeconnection()

    return resp
