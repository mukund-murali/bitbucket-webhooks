from typing import Callable
from typing import List

import marshmallow_objects as mo

from bitbucket_webhooks import event_schemas


class BaseHandler:
    def __init__(self, schema: mo.Model) -> None:
        self.handlers: List[Callable] = []
        self.schema = schema

    def __call__(self, method: Callable) -> Callable:
        self.handlers.append(method)
        return method

    def handle(self, event_payload: dict) -> list:
        event = self.schema().load(event_payload)
        return [method(event) for method in self.handlers]


repo_push = BaseHandler(event_schemas.RepoPush)
pr_approved = BaseHandler(event_schemas.PullRequestApproved)
pr_unapproved = BaseHandler(event_schemas.PullRequestUnapproved)
pr_created = BaseHandler(event_schemas.PullRequestCreated)
pr_updated = BaseHandler(event_schemas.PullRequestUpdated)
pr_merged = BaseHandler(event_schemas.PullRequestMerged)
pr_declined = BaseHandler(event_schemas.PullRequestDeclined)
pr_comment_created = BaseHandler(event_schemas.PullRequestCommentCreated)
pr_comment_updated = BaseHandler(event_schemas.PullRequestCommentUpdated)
pr_comment_deleted = BaseHandler(event_schemas.PullRequestCommentDeleted)
