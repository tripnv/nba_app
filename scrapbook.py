#%%
from nba_api.stats.endpoints import LeagueStandings
import pandas as pd
from collections import OrderedDict
import copy
#%%
current_standings = LeagueStandings()
current_standings


# %%
df = current_standings.get_normalized_dict()

# %%
df
# %%
df.keys()
# %%
len(df["Standings"])
empty_df = pd.DataFrame(columns=["Team", "Conference","PlayoffRank", "Record"])
# %%
standings = []
for i in range(len(df["Standings"])):
    
    standings.append([df['Standings'][i]["TeamName"], df['Standings'][i]["Conference"], df['Standings'][i]["PlayoffRank"], df['Standings'][i]["Record"]])
#%%
req = LeagueStandings()
current_standings = req.get_normalized_dict()
    
data = []
for i in range(len(current_standings["Standings"])):
    
        data.append(
        [current_standings['Standings'][i]["TeamName"],\
         current_standings['Standings'][i]["Conference"],\
          current_standings['Standings'][i]["PlayoffRank"],\
           current_standings['Standings'][i]["Record"]])
#%%
type(current_standings)
#%%
for i in range(len(current_standings["Standings"])):
    print(current_standings['Standings'][i]["PlayoffRank"])

#%%
standin = pd.DataFrame(data, columns = ["team", "conf", "rank", "record"])
standin.loc[standin.conf=="East"]
#%%
players = {
    "Albert":{
        "east":["Nets","Bucks","Hawks","76ers","Heat","Bulls","Knicks","Celtics"],
        "west":["Suns" ,"Lakers","Jazz","Mavericks","Warriors","Nuggets","Clippers","Trail Blazers"],
        "points":None,
        "points_total":None,
    },
    "Nandor":{
        "east":["Nets","Bucks","Heat","Bulls","Knicks","76ers","Hawks","Celtics",],
        "west":["Lakers","Jazz","Suns","Mavericks","Nuggets","Clippers","Warriors","Trail Blazers",],
        "points":None,
        "points_total":None,
    },
    "Gellert":{
        "east":["Bucks","Nets","Hawks","Heat","Celtics","Bulls","76ers","Hornets",],
        "west":["Jazz","Suns","Lakers","Nuggets","Mavericks","Warriors","Trail Blazers","Grizzlies"],
        "points":None,
        "points_total":None,
    },
    "Levente":{
        "east":["Bucks","Nets","Hawks","Heat","76ers","Celtics","Knicks","Bulls"],
        "west":["Lakers","Jazz","Suns","Mavericks,"	"Nuggets","Warriors","Clippers","Trail Blazers"],
        "points":None,
        "points_total":None,
    }

}
#%%
players

# %%
east = [(i[2], i[0], i[3] ) for i in data if i[1] == "East"]
west = [(i[2], i[0], i[3] ) for i in data if i[1] == "West"]
#%%
standings = (east, west)
west
#%%
east
# %%
for player in players.keys():
        players[player]["points"] = {"east_points":[0] * 8,"west_points":[0] * 8}
# %%
players
#%%
east_top = [i[1] for i in standings[0]][:8]
west_top = [i[1] for i in standings[1]][:8]

# %%
print(f"\n EAST ___________________")
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
                elif user_rank - team_rank == 1:
                    score_e += 1
            updated_points_e = copy.deepcopy(players[player]["points"]["east_points"])
            updated_points_e[user_rank] = score_e
            players[player]["points"]["east_points"] = updated_points_e
        print(player, players[player]["points"]["east_points"], f"Team - {team} = {score_e} points")
        #print(f"User {player} \n \tTeam: {team} \n \tUser_rank: {user_rank+1} \n \tTeam_rank: {team_rank+1} \n \tPoints: {score_1}\n")

print(f"\n WEST ___________________")        
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
                elif user_rank - team_rank == 1:
                    score_w += 1
            
            updated_points_w = copy.deepcopy(players[player]["points"]["west_points"])
            updated_points_w[user_rank] = score_w 
            players[player]["points"]["west_points"] = updated_points_w
        #print(f"User {player} \n \tTeam: {team} \n \tUser_rank: {user_rank+1} \n \tTeam_rank: {team_rank+1} \n \tPoints: {score_1}")
        print(player, players[player]["points"]["west_points"], f"Team - {team} = {score_w} points")

#%%
print(east_top)
# %%
#for player in players.keys():
#    players[player]["points_total"] = sum(players[player]["points"]["east_points"]) + sum(players[player]["points"]["west_points"])
# %%
players
# %%
player_df = pd.DataFrame(columns = ["Albert_E","Nandor","Gellert", "Levente"])
# %%
