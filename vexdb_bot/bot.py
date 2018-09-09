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

        message = "*%s (Team %s)*\n" \
                  "_%s (%s)_\n" \
                  % (team_info.team_name, team_info.id,
                     team_info.organisation, team_info.get_location_str())

        resp = BotResponse(message)
    else:
        resp = BotResponse("Sorry, I couldn't find a valid team ID in your message :(")

    return resp.prepare_response_json()


if __name__ == "__main__":
    app.run()
