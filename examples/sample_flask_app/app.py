from flask import Flask
from flask import request

from bitbucket_webhooks_router import router
from bitbucket_webhooks_router import decorators


app = Flask(__name__)

HEADER_EVENT_KEY = 'X-Event-Key'


@app.route('/hooks', methods=["GET", "POST"])
def hello_world():
    event_key = request.headers.get(HEADER_EVENT_KEY)
    router.route(event_key, request.json)
    return ('', 204)


@decorators.handle_repo_push
def push_handler_1(event):
    print("Repo push handler 1")
    print(event.repository.name)


@decorators.handle_repo_push
def push_handler_2(event):
    print("Repo push handler 2")
    print(event.repository.name)