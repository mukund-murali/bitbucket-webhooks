from collections import namedtuple

from bitbucket_webhooks_router import _constants
from bitbucket_webhooks_router import decorators
from bitbucket_webhooks_router import event_schemas

Handler = namedtuple("Handler", "schema decorator")

HANDLER_MAP = {
    _constants.EventName.REPO_PUSH.value: Handler(event_schemas.RepoPush, decorators.handle_repo_push),
    _constants.EventName.PULL_REQUEST_APPROVED.value: Handler(event_schemas.PullRequestApproved, decorators.handle_pr_approval),
}

def route(event_key: str, event_payload: dict) -> None:
    handler = HANDLER_MAP.get(event_key)
    if not handler:
        return
    event = handler.schema().load(event_payload)
    for method in handler.decorator.methods:
        method(event)
