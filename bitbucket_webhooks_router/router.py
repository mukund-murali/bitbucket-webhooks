from bitbucket_webhooks_router import _constants
from bitbucket_webhooks_router import decorators
from bitbucket_webhooks_router import event_schemas


def route(event_key: str, event_payload: dict) -> None:
    if event_key == _constants.EventName.REPO_PUSH.value:
        _handle_repo_push(event_payload)


def _handle_repo_push(event_payload: dict) -> None:
    push_event = event_schemas.RepoPush().load(event_payload)
    for method in decorators.handle_repo_push.methods:
        method(push_event)
