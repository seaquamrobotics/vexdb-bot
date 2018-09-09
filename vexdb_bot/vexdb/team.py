import requests
from vexdb_bot.settings import VEXDB_URL

from .vexdb import CouldNotFindError


class Team:
    def __init__(self, **kwargs):
        if kwargs["size"] <= 0:
            raise CouldNotFindError()
        result = kwargs["result"][0]

        self.id            = str(result["number"])
        self.program       = str(result["program"])
        self.team_name     = str(result["team_name"])
        self.robot_name    = str(result["robot_name"])
        self.organisation  = str(result["organisation"])
        self.city          = str(result["city"])
        self.region        = str(result["region"])
        self.country       = str(result["country"])
        self.grade         = str(result["grade"])
        self.is_registered = bool(result["is_registered"])


def get_team(team_name):
    """Gets team information from the VexDB API (/get_teams)."""
    resp = requests.get("%s/get_teams?team=%s" % (VEXDB_URL, team_name))
    return Team(**resp.json())
