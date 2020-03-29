from typing import Optional

from bitbucket_webhooks import hooks

_EVENT_HOOK_MAP = {hook.event_key: hook for hook in hooks._BaseHook.get_hooks()}


def route(event_key: str, event_payload: dict) -> Optional[list]:
    """Route event payload to the relevant event handlers.

    Returns:
        list: List of return values from the event receivers.
        None: If no hook is available for the given event key.

    """
    hook = _EVENT_HOOK_MAP.get(event_key)
    if not hook:
        return None
    return hook.handle(event_payload)
