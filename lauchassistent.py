from flask import Flask, request, Response, json
app = Flask(__name__)


@app.route('/lauchassistent', methods=['GET', 'POST'])
def hello_world():
    data = request.get_json()
    print(data["queryResult"]["parameters"]["par_country"])
    message = "Schland"

    answer = {"fulfillmentText": "hello world", "fulfillmentMessages": [{"text": {"text": [message]}}]}
    js = json.dumps(answer)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['test'] = 'Testheader'
    return resp
