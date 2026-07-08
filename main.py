from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.post("/agent")
def agent():
    body = request.json
    print(body)
    return jsonify({
      "operations": [
        {
          "type": "add_floor",
          "parameters": {"width": 8, "length": 10, "elevation": 3},
        }
      ]
    })


app.run(debug=True)
