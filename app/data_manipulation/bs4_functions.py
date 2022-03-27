from bs4 import BeautifulSoup
import pandas as pd


def nba_stuffer_player_stats_to_df(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    tbl = soup.find("table")
    column_names = []
    for th in tbl.find('thead').find('tr').find_all('th'):
        if th.find('a'):
            a = th.find('a')
            for span in a.find_all('span'):
                span.decompose()
            column_names.append(a.text)
        else:
            column_names.append(th.text)
    df = pd.read_html(str(tbl))[0].transpose()
    df = df.drop('RANK', 1)

    return df.to_json()