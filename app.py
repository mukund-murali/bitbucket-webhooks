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
    return 'Hello, World!'


@decorators.handle_repo_push
def push_handler_1(event):
    print("Handler 1")
    print(event["repository"]["name"])


@decorators.handle_repo_push
def push_handler_2(event):
    print("Handler 2")
    print(event["repository"]["name"])