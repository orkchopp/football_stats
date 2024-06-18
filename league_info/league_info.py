import pandas as pd


def retrieve_key(league_dict: dict, selected_stat: str) -> list:
    """
    Performs list comprehension to retrieve the key for a given league.
    :param league_dict: Dictionary of leagues.
    :param selected_stat: Selected stat.
    :return:
    """
    return [key for key, value in league_dict.items() if value == selected_stat]


def retrieve_league(selected_league: str) -> list:
    """
    Retrieves the information from the league_name dictionary based on the selected league
    :param selected_league: The selected league from the checkboxes
    :return: The retrieved league
    """
    league_name = {
        9: "EPL",
        12: "La Liga",
        20: "Bundesliga",
        11: "Serie A",
        13: "Ligue 1",
        52: "PSL"
    }
    
    return retrieve_key(league_name, selected_league)


def retrieve_data(year: str, selected_stat: str, selected_league: str) -> pd.DataFrame:
    """
    Retrieves the data from the league_name dictionary based on the selected league
    :param year:
    :param selected_stat:
    :param selected_league:
    :return:
    """
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