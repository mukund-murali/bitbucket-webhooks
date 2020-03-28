from abc import ABCMeta
from abc import abstractmethod

import marshmallow_objects as mm

from bitbucket_webhooks_router import event_schemas
from bitbucket_webhooks_router import hooks


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
    def decorator(self) -> hooks.BaseHandler:
        raise NotImplementedError


class RepoPushHandler(EventHandler):
    event_key = "repo:push"
    schema = event_schemas.RepoPush
    decorator = hooks.repo_push


class PullRequestApprovedHandler(EventHandler):
    event_key = "pullrequest:approved"
    schema = event_schemas.PullRequestApproved
    decorator = hooks.pr_approved


class PullRequestUnapprovedHandler(EventHandler):
    event_key = "pullrequest:unapproved"
    schema = event_schemas.PullRequestUnapproved
    decorator = hooks.pr_unapproved


class PullRequestCreatedHandler(EventHandler):
    event_key = "pullrequest:created"
    schema = event_schemas.PullRequestCreated
    decorator = hooks.pr_created


class PullRequestUpdatedHandler(EventHandler):
    event_key = "pullrequest:updated"
    schema = event_schemas.PullRequestUpdated
    decorator = hooks.pr_updated


class PullRequestMergedHandler(EventHandler):
    event_key = "pullrequest:fulfilled"
    schema = event_schemas.PullRequestMerged
    decorator = hooks.pr_merged


class PullRequestDeclinedHandler(EventHandler):
    event_key = "pullrequest:rejected"
    schema = event_schemas.PullRequestDeclined
    decorator = hooks.pr_declined
