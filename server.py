from flask import Flask
from flask import request
from flask import jsonify

from yowsup.common.tools import StorageTools, WATools
from yowsup.registration.existsrequest import WAExistsRequest
from yowsup.env import S40YowsupEnv, AndroidYowsupEnv

import random, hashlib, os
from urllib import quote
CURRENT_ENV = AndroidYowsupEnv()

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
  return jsonify(status=200)

@app.route("/token", methods=['GET'])
def token():
  number = request.args.get('number')
  cc = request.args.get('cc')


  if number is not None:
    if cc is not None:

      in_ = number[len(cc):]
      token = CURRENT_ENV.getToken(in_)
      idx = WATools.generateIdentity()

      return jsonify(status=200, number=number, cc=cc, token=token, identity=quote(idx))
    else:
      return jsonify(status=402, error="Country code is required")
  else:
    return jsonify(status=402, error="Number is required")


if __name__ == "__main__":
  app.run(debug=True)