from flask import Flask
from flask import request
from flask import jsonify
import random, hashlib, os

app = Flask(__name__)

@app.route("/token", methods=['GET'])
def req():
  number = request.args.get('number')
  cc = request.args.get('cc')

  if number is not None:
    if cc is not None:
      # 
      return jsonify(status=200, number=number, cc=cc)
    else:
      return jsonify(status=402, error="Country code is required")
  else:
    return jsonify(status=402, error="Number is required")


if __name__ == "__main__":
  app.run(debug=True)