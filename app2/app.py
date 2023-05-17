from flask import request, Flask
import json


app2 = Flask(__name__)


@app2.route('/')
def hello_world():
    return 'Hello AWS-RESTART-2023 from app222222!!!! :)'
if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0')
