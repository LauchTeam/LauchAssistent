from flask import Flask, request, Response, json
import handlerdb
app = Flask(__name__)


@app.route('/lauchassistent', methods=['GET', 'POST'])
def hello_world():
    db = handlerdb.HandlerDB()
    data = request.get_json()

    kpi_name = data["queryResult"]["parameters"]["par_country"]
    kpi_value = db.Execute("SELECT kpi_value FROM finance.table_kpi WHERE kpi_name = '" + data["queryResult"]["parameters"]["var_kpi"] + "';")

    # print(data["queryResult"]["parameters"]["par_country"])
    message = "Die KPI " + kpi_name + "hat folgenden Wert: " + kpi_value

    answer = {"fulfillmentText": "hello world", "fulfillmentMessages": [{"text": {"text": [message]}}]}
    js = json.dumps(answer)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['test'] = 'Testheader'
    return resp
