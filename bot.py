import bottle
from slack import *

app = bottle.app()


@app.post("/team")
def get_team():
    req = SlashCommandRequest()

    resp = BotResponse("Hello %s!" % req.user_name)
    return resp.prepare_response_json()


if __name__ == "__main__":
    app.run()
