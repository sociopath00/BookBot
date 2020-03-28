import asyncio
import json
from flask import Flask, request
from flask_cors import CORS
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.utils import EndpointConfig


app = Flask(__name__)
CORS(app)


# load NLU model and dialogue model
# nlu_interpreter = RasaNLUInterpreter("./models/current/nlu")
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load("./models/20200328-121754.tar.gz", action_endpoint=action_endpoint)


@app.route("/chatbot", methods=["POST"])
def main():
    global agent

    # load received data into json
    data = json.loads(request.data)
    msg = data["message"]
    user = data["sender"]

    if agent.is_ready():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(parse_message(msg, user))
        return json.dumps(response[0]["custom"])

    return {"msg": "ERROR 00: Unable to complete the request"}


async def parse_message(text, sid):
    global agent
    response = await agent.handle_text(text, sender_id=sid)
    return response


if __name__ == "__main__":
    app.run("0.0.0.0", 6000, debug=False, threaded=True)

