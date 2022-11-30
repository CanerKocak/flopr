from flask import Flask
from flask import render_template
# from osrs_api import Hiscores

app = Flask(__name__)

# def get_player_skills(player_name):
#     player = Hiscores(player_name)
#     total_level = 0
#     skills = player.skills
#     for skill in skills:
#         skill = skills[skill]
#         total_level += skill.level
#     return total_level

# def get_player_total_xp(player_name):
#     player = Hiscores(player_name)
#     total_xp = 0
#     skills = player.skills
#     for skill in skills:
#         skill = skills[skill]
#         total_xp += skill.xp
#     return total_xp

# class Player:
#     def __init__(self, name):
#         self.name = name

#     @property
#     def total_level(self):
#         return get_player_skills(self.name)

@app.route("/")
# def hello_world():
#     players = [Player("Gimmy Woo"), Player("Stoffell"), Player("GroupQuobii"), Player("DummyNeutron")]   
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
