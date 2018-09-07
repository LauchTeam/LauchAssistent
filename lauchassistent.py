from flask import Flask, request, Response, json
import handlerdb
app = Flask(__name__)


@app.route('/lauchassistent', methods=['GET', 'POST'])
def hello_world():
    db = handlerdb.HandlerDB()

    data = request.get_json()
    print(data["queryResult"]["parameters"]["par_country"])
    message = db.connectTo()

    answer = {"fulfillmentText": "hello world", "fulfillmentMessages": [{"text": {"text": [message]}}]}
    js = json.dumps(answer)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['test'] = 'Testheader'
    return resp
