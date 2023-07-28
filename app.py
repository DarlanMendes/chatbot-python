from flask import Flask, request, jsonify

app = Flask(__name__)
from flask_cors import CORS
# Rota para trabalhar com vários produtos
CORS(app)
@app.route('/chatbot', methods=['POST'])
def handle_chatbot():
   
        data= request.get_json()
       
        return jsonify(data['msg'])
    
    
#Rota para produto especifico
@app.route('/product', methods=['GET','PATCH','DELETE'])
def get_data():
    if request.method == 'GET':
        return {"teste":"teste"}
    if request.method == 'POST':
        data= request.get_json()
       
        return jsonify(data['data'])
    
    
if __name__ == '__main__':
    app.run()