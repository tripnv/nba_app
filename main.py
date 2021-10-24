from flask import Flask, render_template
from nba_api.stats.endpoints import LeagueStandings
import json

from numpy import log  
app = Flask(__name__)

with open('player_info.json', "r") as f:
    players = json.load(f)

with open('logos.json', "r") as f:
    logos = json.load(f)

def get_standings() -> tuple:
    req = LeagueStandings()
    current_standings = req.get_normalized_dict()
    
    data = []
    for i in range(len(current_standings["Standings"])):
    
        data.append(
        [current_standings['Standings'][i]["TeamName"],\
         current_standings['Standings'][i]["Conference"],\
          current_standings['Standings'][i]["PlayoffRank"],\
           current_standings['Standings'][i]["Record"]])

    east = [(i[2], i[0], i[3] ) for i in data if i[1] == "East"]
    west = [(i[2], i[0], i[3] ) for i in data if i[1] == "West"] 

    return (east, west)



def assign_points(standings:tuple, players:dict) -> None:
    """
    
    """
    east_top = [i[1] for i in standings[0]][:8]
    west_top = [i[1] for i in standings[1]][:8]
    
    for player in players.keys():
        players[player]["points"] = {"east_points":[0] * 8,"west_points":[0] * 8}

     
    for team in east_top:
        team_rank = east_top.index(team)
        for player in players:
            score_e = 0
            if team in players[player]["east"]:
                user_rank = players[player]["east"].index(team)
                score_e = 10
                
                if (user_rank < 4 and team_rank  < 4) or (user_rank >= 4 and team_rank >= 4):
                    score_e += 1
                    if user_rank == team_rank:
                        score_e += 2 
                
                players[player]["points"]["east_points"][user_rank] = score_e

           
    for team in west_top:
        team_rank = west_top.index(team)
        for player in players.keys():
            score_w = 0
            if team in players[player]["west"]:
                user_rank = players[player]["west"].index(team)
                score_w = 10
                
                if (user_rank < 4 and team_rank  < 4) or (user_rank >= 4 and team_rank >= 4):
                    score_w += 1
                    if user_rank == team_rank:
                        score_w += 2 
                
                players[player]["points"]["west_points"][user_rank] = score_w
            

    for player in players.keys():
        players[player]["points_total"] = sum(players[player]["points"]["east_points"]) + sum(players[player]["points"]["west_points"])

@app.before_request()
def before_request_callback():
    standings = get_standings()
    assign_points(standings, players)

@app.route("/")
def home():
    
    return render_template("home.html", players = players, logos = logos)

if __name__=="__main__":
    app.run(debug=True)