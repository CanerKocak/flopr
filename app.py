from flask import Flask, render_template, request, redirect, url_for
import pickle

    
app = Flask(__name__)
try:
    with open('players.pickle', 'rb') as f:
        players = pickle.load(f)
except:
    players = {}
    with open('players.pickle', 'wb') as f:
        pickle.dump(players, f)


def add_kill(player, npc, timestamp, price, items):
    if player not in players:
        players[player] = {}
    if npc not in players[player]:
        players[player][npc] = []
    players[player][npc].append({'timestamp': timestamp, 'price': price, 'items': items})
    with open('players.pickle', 'wb') as f:
        pickle.dump(players, f)

@app.route("/")
def hello_world():
    return render_template('index.html', players=players)

@app.route('/<player>/inventory_items/', methods=['POST'])
def inventory_items(player):
    return '', 200

@app.route('/<player>/equipped_items/', methods=['POST'])
def equipped_items(player):
    return '', 200

@app.route('/<player>/npc_kill/', methods=['POST', 'GET'])	
def npc_kill(player):
    data = request.json
    timestamp = data['timestamp']
    data = data['data']
    price =  data['gePrice']
    npcID = data['npcId']
    items = data['items']
    add_kill(player, npcID, timestamp, price, items)
    return '', 200


    
if __name__ == "__main__":
    app.run(debug=True)
    
    
# make html that prints out the players and their kills in a table