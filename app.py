from flask import Flask, render_template, request, redirect, url_for
import pickle
from osrsreboxed import monsters_api
import datetime
from OSRS_Hiscores import Hiscores

monsters = monsters_api.load()

def get_monster_name(monster_id):
    monster_id = int(monster_id)
    for monster in monsters:
        if monster.id == monster_id:
            return monster.name
    return None
        

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

def get_date(timestamp):
    date = datetime.datetime.fromtimestamp(timestamp)
    return date.strftime('%Y-%m-%d %H:%M:%S')

@app.route('/<player>/npc_kill/', methods=['POST', 'GET'])	
def npc_kill(player):
    data = request.json
    print(data)
    timestamp = data['timestamp']
    data = data['data']
    price =  data['gePrice']
    npcID = data['npcId']
    items = data['items']
    add_kill(player, get_monster_name(npcID), get_date(timestamp), price, items)
    return '', 200

@app.route('/player_stats/<player>')
def player_stats(player):
    username = player
    user = Hiscores(username)
    total = user.skill('total')
    xp = 0
    for stat in user.stats:
        xp += int(user.stats[stat]['experience'])
 
    return render_template('player_stats.html', player=player, total=total, xp=xp)


@app.route('/<player>/npc_kill/<npc>', methods=['GET'])
def npc_kill_get(player, npc):
    all_kills = players[player]
    kills = [kill for kill in all_kills[npc]]
    print(kills)
    return render_template('npc.html', kills=kills, npc_name = npc)
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
# make the html for the npc.html use the following code
