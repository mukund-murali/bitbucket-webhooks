from flask import Flask
from flask import request

from bitbucket_webhooks_router import router


app = Flask(__name__)

HEADER_EVENT_KEY = 'X-Event-Key'


@app.route('/hooks', methods=["GET", "POST"])
def hello_world():
    event_key = request.headers.get(HEADER_EVENT_KEY)
    router.route(event_key, request.json)
    return 'Hello, World!'
