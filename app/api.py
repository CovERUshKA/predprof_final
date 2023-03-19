import sqlite3
import requests
from . import miet_api
from .responses import SuccessResponse, ErrorResponse

from flask import (
    Blueprint, request, abort, current_app
)

bp = Blueprint('api', __name__, url_prefix='/api')

def check_parameters(data, parameters):
    try:
        assert type(data) == dict, ('data', 404)

        for param in parameters:
            types = param[1:]
            if param[0] in data:
                assert type(data.get(param[0])) in types, (param[0], 400)
            else:
                raise AssertionError((param[0], 404))
    except AssertionError as e:
        abort(ErrorResponse(f"field \"{e.args[0][0]}\" incorrect", e.args[0][1]))

# http://127.0.0.1:80/api/calcs
@bp.route('/calcs', methods=['GET'])
def calcs():
    arguments = request.args

    i = arguments.get("i", None, type=int)

    if i == None or (not (i in range(1, 5))):
        return ErrorResponse("i is incorrect", 400)
    
    if i == 4 and current_app.config["CURRENT_PATHS"][3] == None:
        return ErrorResponse("Custom path is not provided", 400)

    return SuccessResponse(current_app.config["CURRENT_PATHS"][i-1]["calcs"])

# http://127.0.0.1:80/api/add_path
@bp.route('/add_path', methods=['POST'])
def add_path():
    data = request.get_json()

    if type(data) != list or len(data) == 0:
        return ErrorResponse("data is incorrect", 400)
    
    ret = []

    #ret = calculate(data)

    if len(current_app.config["CURRENT_PATHS"]) < 4:
        current_app.config["CURRENT_PATHS"].append({"points": data, "data": ret})
    else:
        current_app.config["CURRENT_PATHS"][3] = {"points": data, "data": ret}

    return SuccessResponse({})
