import streamlit as st
import datetime
from league_info.league_info import retrieve_data


def initalise_streamlit():
    
    st.set_page_config(layout='wide')

    st.title("EPL Statistics")
    st.write("This is a simple project that we will build off later on to include data visualisation.")


def main():
    
    today = datetime.datetime.today()
    current_year = today.year

    initalise_streamlit()
    
    # Sidebar Information For Year and Stat Selection
    st.sidebar.header("Select Information")
    
    selected_year = st.sidebar.selectbox("Select the year", list(reversed(range(2003, current_year))))
    selected_stat = st.sidebar.selectbox("Select the stat", ["League Standings"])
    
    team_information = retrieve_data(selected_year, selected_stat)
    teams = sorted(team_information.Squad.unique())
    
    selected_team = st.sidebar.multiselect('Select Team(s)', teams, teams)
    selected_team_data = team_information[(team_information.Squad.isin(selected_team))]
        
    st.write(selected_team_data)
    
if __name__ == "__main__":
    main()
