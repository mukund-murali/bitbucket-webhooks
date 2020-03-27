from abc import ABCMeta
from abc import abstractmethod

import marshmallow_objects as mm

from bitbucket_webhooks_router import decorators
from bitbucket_webhooks_router import event_schemas


class EventHandler(metaclass=ABCMeta):
    @property
    @abstractmethod
    def event_key(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def schema(self) -> mm.Model:
        raise NotImplementedError

    @property
    @abstractmethod
    def decorator(self) -> decorators.BaseHandler:
        raise NotImplementedError


class RepoPushHandler(EventHandler):
    event_key = "repo:push"
    schema = event_schemas.RepoPush
    decorator = decorators.handle_repo_push


class PullRequestApprovedHandler(EventHandler):
    event_key = "pullrequest:approved"
    schema = event_schemas.PullRequestApproved
    decorator = decorators.handle_pr_approval


class PullRequestCreated(EventHandler):
    event_key = "pullrequest:created"
    schema = event_schemas.PullRequestCreated
    decorator = decorators.handle_pr_created


class PullRequestUpdated(EventHandler):
    event_key = "pullrequest:updated"
    schema = event_schemas.PullRequestUpdated
    decorator = decorators.handle_pr_updated
