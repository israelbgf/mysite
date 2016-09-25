from datetime import date
from json import JSONEncoder

from flask import json


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        return JSONEncoder.default(self, obj)


def jsonify(input):
    return json.dumps(input, cls=CustomJSONEncoder)
