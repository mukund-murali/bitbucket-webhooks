from typing import Optional

from bitbucket_webhooks_router import _handlers

_HANDLER_MAP = {
    handler.event_key: handler for handler in _handlers.EventHandler.__subclasses__()
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
    event = handler.schema().load(event_payload)
    return [method(event) for method in handler.decorator.get_methods()]
