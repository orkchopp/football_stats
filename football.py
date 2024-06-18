import streamlit as st
import datetime
from league_info.league_info import retrieve_data, retrieve_league


def initalise_streamlit() -> None:
    """
    Initalises the Streamlit application with the required configurations
    :return: None
    """
    st.set_page_config(layout='wide')

    st.sidebar.image("https://static-00.iconduck.com/assets.00/soccer-ball-emoji-2048x2048-o1qymrda.png", width=100)
    st.title("⚽ Football Statistics ⚽")
    st.write("")
    st.write("")


def main():
    """
    Houses the logic of the football app, handing the input from the select box and passing it to logic functions in
    league_info.py
    :return: None
    """
    today = datetime.datetime.today()
    current_year = today.year

    initalise_streamlit()
    
    # Sidebar Information For Year and Stat Selection
    st.sidebar.header("Select Information")
    
    selected_year = st.sidebar.selectbox("Select the year", list(reversed(range(2003, current_year))))
    selected_stat = st.sidebar.selectbox("Select the stat", ["League Standings"])
    
    # Sidebar Information for Selecting League
    selected_league = st.sidebar.selectbox("Select the league", ["EPL", "La Liga", "Bundesliga", "Serie A", "Ligue 1", "PSL"])
    
    team_information = retrieve_data(selected_year, selected_stat, selected_league)
    teams = sorted(team_information.Squad.unique())
    
    # Sidebar Information for Selecting Teams
    selected_team = st.sidebar.multiselect('Select Team(s)', teams, teams)
    selected_team_data = team_information[(team_information.Squad.isin(selected_team))]
    
    st.markdown(f"##### Now displaying **{selected_stat}** in **{selected_league}** for the year **{selected_year}**!")    
    st.write(selected_team_data)
    
if __name__ == "__main__":
    main()
