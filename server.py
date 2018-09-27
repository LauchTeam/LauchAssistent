from flask import Flask, request, Response, json
import handlerdb
import lauchassistent
app = Flask(__name__)


@app.route('/lauchassistent', methods=['GET', 'POST'])
def get_request():

    data = request.get_json()
    lauch = lauchassistent.LauchAssistent()

    message = lauch.process_request(data)

    answer = {"fulfillmentText": "Answer", "fulfillmentMessages": [{"text": {"text": [message]}}]}
    js = json.dumps(answer)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['test'] = 'Testheader'

    return resp


# if __name__ ==  "__main__":
#    app.run(host='0.0.0.0', port='443', debug=False, ssl_context='adhoc')
