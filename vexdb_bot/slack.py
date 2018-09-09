import json
from bottle import request, response


class SlashCommandRequest:
    def __init__(self):
        self.command   = str(request.forms.get("command"))
        self.text      = str(request.forms.get("text"))
        self.user_id   = str(request.forms.get("user_id"))
        self.user_name = str(request.forms.get("user_name"))
        self.response_url = str(request.forms.get("response_url"))
        self.trigger_id   = str(request.forms.get("trigger_id"))


class BotResponse:
    def __init__(self, text, response_type="in_channel"):
        self.text = text
        self.response_type = response_type

    def prepare_response_json(self):
        response.add_header("content-type", "application/json")
        return json.dumps({
            "response_type": self.response_type,
            "text": self.text
        })
