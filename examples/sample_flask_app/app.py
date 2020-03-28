from bitbucket_webhooks_router import event_schemas
from bitbucket_webhooks_router import hooks
from bitbucket_webhooks_router import router
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/hooks", methods=["POST"])
def bb_webhooks_handler():
    router.route(request.headers["X-Event-Key"], request.json)
    return ("", 204)


@hooks.repo_push
def _handle_repo_push_1(event: event_schemas.RepoPush):
    print("Repo push handler 1")
    print(f"One or more commits to: {event.repository.name}")


@hooks.repo_push
def _handle_repo_push_2(event: event_schemas.RepoPush):
    print("Repo push handler 2")
    print(f"One or more commits to: {event.repository.name}")


@hooks.pr_approved
def _handle_pr_approved(event: event_schemas.PullRequestApproved):
    print(f"Pull request #{event.pullrequest.id} approved")


@hooks.pr_unapproved
def _handle_pr_unapproved(event: event_schemas.PullRequestUnapproved):
    print(f"Pull request #{event.pullrequest.id} unapproved")


@hooks.pr_created
def _handle_pr_created(event: event_schemas.PullRequestCreated):
    print(f"Pull request #{event.pullrequest.id} created")


@hooks.pr_updated
def _handle_pr_updated(event: event_schemas.PullRequestUpdated):
    print(f"Pull request #{event.pullrequest.id} updated")


@hooks.pr_merged
def _handle_pr_merged(event: event_schemas.PullRequestMerged):
    print(f"Pull request #{event.pullrequest.id} merged")


@hooks.pr_declined
def _handle_pr_declined(event: event_schemas.PullRequestDeclined):
    print(f"Pull request #{event.pullrequest.id} declined")
