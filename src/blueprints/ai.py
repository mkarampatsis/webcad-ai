import json
# import os
# from bson import ObjectId,json_util
from flask import Blueprint, Response, request, jsonify

# from src.blueprints.utils import debug_print, dict2string
# from datetime import datetime

ai = Blueprint("ai", __name__)


@ai.route("/agent", methods=["POST"])
def agent():
    body = request.json
    print(body)

    temp = {
        "operations": [
            {
                "type": "add_floor",
                "parameters": {"width": 8, "length": 10, "elevation": 3},
            }
            # {
            #   "type": "add_floor",
            #   "settings": {
            #     "units": {
            #       "length": "m",
            #       "force": "kN",
            #       "moment": "kNm",
            #       "stress": "MPa",
            #       "density": "kg/m3"
            #     }
            #   },
            #   "nodes": {
            #     "1": {"x": 0, "y": 3, "z": 0},
            #     "2": {"x": 5, "y": 3, "z": 0},
            #     "3": {"x": 5, "y": 3, "z": 5},
            #     "4": {"x": 0, "y": 3, "z": 5}
            #   },
            #   "members": {
            #     "1": {"node_A": 1, "node_B": 2, "section_id": 1, "fixity_A": "FFFFFF", "fixity_B": "FFFFFF"},
            #     "2": {"node_A": 2, "node_B": 3, "section_id": 1, "fixity_A": "FFFFFF", "fixity_B": "FFFFFF"},
            #     "3": {"node_A": 3, "node_B": 4, "section_id": 1, "fixity_A": "FFFFFF", "fixity_B": "FFFFFF"},
            #     "4": {"node_A": 4, "node_B": 1, "section_id": 1, "fixity_A": "FFFFFF", "fixity_B": "FFFFFF"}
            #   },
            #   "plates": {
            #     "1": {
            #       "node_A": 1,
            #       "node_B": 2,
            #       "node_C": 3,
            #       "node_D": 4,
            #       "material_id": 1,
            #       "thickness": 200,
            #       "rotZ": 0,
            #       "type": "plate"
            #     }
            #   },
            #   "materials": {
            #     "1": {
            #       "name": "Concrete",
            #       "E": 30000,
            #       "poisson": 0.2,
            #       "density": 2500,
            #       "class": "concrete"
            #     }
            #   },
            #   "sections": {
            #     "1": {
            #       "name": "Concrete Beam",
            #       "area": 0.12,
            #       "iz": 0.0016,
            #       "iy": 0.0009,
            #       "j": 0.002,
            #       "material_id": 1
            #     }
            #   }
            # }
        ]
    }

    # return Response(
    #     json.dumps(temp),
    #     mimetype="application/json",
    #     status=200,
    # )
    return jsonify(temp)

@ai.route("/execute", methods=["POST"])
def execute():

    print("aaaaaaa")
    request_json = request.get_json()
    prompt = request_json["prompt"]

    print(prompt)
    temp = jsonify(
        {
            "operations": [
                {
                    "type": "CREATE_LEVEL",
                    "parameters": {
                        "name": "Level 1", 
                        "elevation": 0
                    },
                },
                {
                    "type": "CREATE_COLUMN",
                    "parameters": {
                        "name": "C1",
                        "levelName": "Level 1",
                        "materialId": "WOOD",
                        "sectionId": "RECT200",
                        "base": {"x": 0, "y": 0, "z": 0},
                        "top": {"x": 0, "y": 0, "z": 3},
                    },
                },
                {
                    "type": "CREATE_COLUMN",
                    "parameters": {
                        "name": "C2",
                        "levelName": "Level 1",
                        "materialId": "WOOD",
                        "sectionId": "RECT200",
                        "base": {"x": 6, "y": 0, "z": 0},
                        "top": {"x": 6, "y": 0, "z": 3},
                    },
                },
                {
                    "type": "CREATE_COLUMN",
                    "parameters": {
                        "name": "C3",
                        "levelName": "Level 1",
                        "materialId": "WOOD",
                        "sectionId": "RECT200",
                        "base": {"x": 6, "y": 6, "z": 0},
                        "top": {"x": 6, "y": 6, "z": 3},
                    },
                },
                {
                    "type": "CREATE_COLUMN",
                    "parameters": {
                        "name": "C4",
                        "levelName": "Level 1",
                        "materialId": "WOOD",
                        "sectionId": "RECT200",
                        "base": {"x": 0, "y": 6, "z": 0},
                        "top": {"x": 0, "y": 6, "z": 3},
                    },
                },
            ]
        }
    )
    
    # return Response(
    #     temp,
    #     mimetype="application/json",
    #     status=200,
    # )
    return temp
