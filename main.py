from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)

# CORS configuration
cors = CORS(
  app,
  resources={r"*": {"origins": ["http://localhost:4200"]}},
)

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
