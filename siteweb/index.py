from flask import Flask, render_template, request, redirect, url_for, abort, session,json,jsonify
import  script

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/getPrediction',methods=['GET'])
def get_prediction():
    group1 = json.loads(request.args['myParam1'])
    group2 = json.loads(request.args['myParam2'])
    print 'call prediction algo'
    res =  script.get_prediction(group1,group2)
    print type(res), 'res is ', res
    return jsonify(resultats=res)

if __name__ == '__main__':
    app.run()