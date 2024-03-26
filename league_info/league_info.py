import pandas as pd

def retrieve_key(league_dict:dict, selected_stat):

    return [key for key, value in league_dict.items() if value == selected_stat]


def retrieve_league(selected_league):
    
    league_name = {
        9: "EPL",
        12: "La Liga",
        20: "Bundesliga",
        11: "Serie A",
        13: "Ligue 1",
        52: "PSL"
    }
    
    return retrieve_key(league_name, selected_league)


def retrieve_data(year, selected_stat, selected_league):
    
    league_key = retrieve_league(selected_league)
    
    url = f"https://fbref.com/en/comps/{league_key[0]}/{year}-{year+1}"
    
    league_data = {
        0: "League Standings",
    }
    
    stats_key = retrieve_key(league_data, selected_stat)
    
    if selected_stat == "League Standings":
        html = pd.read_html(url, header=0)
    else:
        html = pd.read_html(url, header=1)
        
    dataframe = html[stats_key[0]]
    
    raw = dataframe.reset_index(drop=True)
    # Fill Empty Fields with - instead of None
    raw = raw.fillna("-")
    
    dataframe = raw
    return dataframe