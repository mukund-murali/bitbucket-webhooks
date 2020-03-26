from enum import Enum


class EventName(Enum):
    REPO_PUSH = "repo:push"
    PULL_REQUEST_APPROVED = "pullrequest:approved"
