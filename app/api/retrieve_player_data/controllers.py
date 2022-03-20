import requests as reqs
import app.data_manipulation.bs4_functions as scraper

def get_all_current_players_stats():
    nba_stuffer_url = "https://www.nbastuffer.com/2021-2022-nba-player-stats/"

    response = reqs.get(nba_stuffer_url)
    return scraper.nba_stuffer_player_stats_to_json(response.text)