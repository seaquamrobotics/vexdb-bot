import bottle
from vexdb_bot.slack import *
from vexdb_bot.utils import *

from vexdb_bot.vexdb.team import get_team

app = bottle.app()


@app.post("/team")
def team():
    req = SlashCommandRequest()

    team_id = find_team_id(req.text)
    if team_id:
        team_info = get_team(team_id)
        resp = BotResponse("Team %s is %s" % (team_id, team_info.team_name))
    else:
        resp = BotResponse("Sorry, I couldn't find a valid team ID in your message :(")

    return resp.prepare_response_json()


if __name__ == "__main__":
    app.run()
