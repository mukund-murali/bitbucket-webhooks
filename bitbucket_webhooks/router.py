from typing import Optional

from bitbucket_webhooks import hooks

_HANDLER_MAP = {
    "repo:push": hooks.repo_push,
    "pullrequest:approved": hooks.pr_approved,
    "pullrequest:unapproved": hooks.pr_unapproved,
    "pullrequest:created": hooks.pr_created,
    "pullrequest:updated": hooks.pr_updated,
    "pullrequest:fulfilled": hooks.pr_merged,
    "pullrequest:rejected": hooks.pr_declined,
    "pullrequest:comment_created": hooks.pr_comment_created,
    "pullrequest:comment_updated": hooks.pr_comment_updated,
    "pullrequest:comment_deleted": hooks.pr_comment_deleted,
}


def route(event_key: str, event_payload: dict) -> Optional[list]:
    """Routes the given event and payload to the relevant decorator.

    Returns:
        list: List of return values from the event receivers.
        None: If no handler is available for the given event key.

    """
    handler = _HANDLER_MAP.get(event_key)
    if not handler:
        return None
    return handler.handle(event_payload)
