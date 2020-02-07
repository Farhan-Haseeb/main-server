import json
from flask import Flask, jsonify, request
from uuid import uuid4
from urllib.parse import urlparse

# Resgistering node

class Particle:
    def __init__(self):
        self.nodes = []

    def add_node(self, data):
        print(self.exists(self.nodes, data['node_id']))
        if self.exists(self.nodes, data['node_id']): return "No is already connected"
        else: self.nodes.append(data); return self.nodes

    def exists(self, arr, node_id):
        if arr is None or arr is []: return 'Empty list'
        for i in range(len(arr)):
            if node_id == arr[i]['node_id']: return True ; break
            else: return False



# Creating a Web App
app = Flask(__name__)

particle = Particle()

#Creating an address for the node on Port 5000
node_address = str(uuid4()).replace('-', '')


@app.route('/',  methods = ['GET'])
def index_route():
    return 'You can register at http://localhost:5000/handshake/'



# Connecting new nodes
@app.route('/connect_node', methods = ['POST'])
def connect_node():
    json_data = request.get_json()
    if json_data is not None:
        particle.add_node(json_data)
        response = {'message': "The node is connected", 'total_nodes': particle.nodes}
        return jsonify(response), 201
    else:
        return "No data", 400


@app.route('/hook', methods = ['POST'])
def hook():
    # this will get data from particle
    return 'this will get data from particle'

@app.route('/api/data', methods = ['GET'])
def send_data():
    # This route will send data to front end
    return 'This route will send data to front end'



if __name__ == '__main__':
    app.run(port= 5000)
