import pandas as pd

URL = "https://fbref.com/en/comps/9"


def retrieve_key(league_dict:dict, val):
    return [key for key, value in league_dict.items() if value == val]


def retrieve_data(year, selected_stat):
    
    url = "https://fbref.com/en/comps/9/" + str(year) + "-" + str(year+1)
    
    league_data = {
        0: "League Standings",
    }
    
    ass_key = retrieve_key(league_data, selected_stat)
    
    if selected_stat == "League Standings":
        html = pd.read_html(url, header=0)
    else:
        html = pd.read_html(url, header=1)
        
    dataframe = html[ass_key[0]]
    # raw = dataframe.reset_index(drop=True)
    # raw = raw.fillna("Stats Missing")
    # playerstats = raw
    
    return dataframe
