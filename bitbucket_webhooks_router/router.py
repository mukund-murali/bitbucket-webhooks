from bitbucket_webhooks_router import _exceptions
from bitbucket_webhooks_router import _handlers

_HANDLER_MAP = {
    handler.event_key: handler for handler in _handlers.EventHandler.__subclasses__()
}


def route(event_key: str, event_payload: dict) -> list:
    handler = _HANDLER_MAP.get(event_key)
    if not handler:
        raise _exceptions.NoHandlerError
    event = handler.schema().load(event_payload)
    return [method(event) for method in handler.decorator.methods]
