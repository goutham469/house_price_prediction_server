from flask import Flask,jsonify,request
import json

app=Flask(__name__)


names=[
    {
        "name":"goutham reddy",
        "age":19,
        "class":"IT-c"
    },
    {
        "name":"a",
        "age":12,
        "class":"IT-c"
    }
]


@app.route('/')
def index():
    return "Hi this is my first python API"

@app.route('/getInfo')
def getInfo():
    return "this server is running on port : http://127.0.0.1:5000"

@app.route('/getNames')
def getNames():
    return jsonify(names)

@app.route('/postData',methods=['POST'])
def postData():
    if request.method == 'POST' :
        data = request.get_json()
        print()
        print(data)
        # data = json.loads(data)
        # print(data)

        #print(type(data)) = dictionary
        print(data['name'])
        return "data received successfully"
    
@app.route('/add',methods=['POST'])
def add():
    if request.method == 'POST':
        data = request.get_json()
        n1 = float(data['number1'])
        n2 = float(data['number2'])
        obj={
            "sum":(n1+n2),
            "add":(n1-n2),
            "mul":n1*n2
        }
        return jsonify(obj)
    else:
        return "invalid method"

if __name__ == '__main__':
    app.run(debug=True)