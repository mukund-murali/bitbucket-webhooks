"""Decorators that have to be extended by the hook handlers.

.. module:: hooks

"""
from typing import Callable
from typing import List

import marshmallow_objects as mo

from bitbucket_webhooks import event_schemas


class _BaseHook:
    """The base hook that creates the decorators."""

    def __init__(self, schema: mo.Model) -> None:
        self.handlers: List[Callable] = []
        self.schema = schema

    def __call__(self, method: Callable) -> Callable:
        self.handlers.append(method)
        return method

    def handle(self, event_payload: dict) -> list:
        """Make function calls to all handlers registered with this hook.

        Returns:
            list: List of return values from the handlers.

        """
        event = self.schema().load(event_payload)
        return [method(event) for method in self.handlers]


repo_push = _BaseHook(event_schemas.RepoPush)
"""
Decorator for repo:push events with the first argument as
:class:`bitbucket_webhooks.event_schemas.RepoPush`
"""

pr_approved = _BaseHook(event_schemas.PullRequestApproved)
pr_unapproved = _BaseHook(event_schemas.PullRequestUnapproved)
pr_created = _BaseHook(event_schemas.PullRequestCreated)
pr_updated = _BaseHook(event_schemas.PullRequestUpdated)
pr_merged = _BaseHook(event_schemas.PullRequestMerged)
pr_declined = _BaseHook(event_schemas.PullRequestDeclined)
pr_comment_created = _BaseHook(event_schemas.PullRequestCommentCreated)
pr_comment_updated = _BaseHook(event_schemas.PullRequestCommentUpdated)
pr_comment_deleted = _BaseHook(event_schemas.PullRequestCommentDeleted)
