from bitbucket_webhooks_router import decorators
from bitbucket_webhooks_router import router
from flask import Flask
from flask import request

app = Flask(__name__)

HEADER_EVENT_KEY = "X-Event-Key"


@app.route("/hooks", methods=["GET", "POST"])
def bb_webhooks_handler():
    event_key = request.headers.get(HEADER_EVENT_KEY)
    router.route(event_key, request.json)
    return ("", 204)


@decorators.handle_repo_push
def _handle_repo_push_1(event):
    print("Repo push handler 1")
    print(f"One or more commits to: {event.repository.name}")


@decorators.handle_repo_push
def _handle_repo_push_2(event):
    print("Repo push handler 2")
    print(f"One or more commits to: {event.repository.name}")


@decorators.handle_pr_approval
def _handle_pr_approval(event):
    print(f"Pull request #{event.pullrequest.id} approved")


@decorators.handle_pr_created
def _handle_pr_created(event):
    print(f"Pull request #{event.pullrequest.id} created")


@decorators.handle_pr_updated
def _handle_pr_updated(event):
    print(f"Pull request #{event.pullrequest.id} updated")
