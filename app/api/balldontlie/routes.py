from app.api.balldontlie.blueprint import BP
from flask import make_response
from .controllers import get_all_current_players_stats

# Was sudo only
@BP.route('', methods=['GET'])
def get_all_players():
    """
    Returns an array of all stores
    old:cms/stores
    old:client/stores
    """
    return make_response(get_all_current_players_stats(), 200)
