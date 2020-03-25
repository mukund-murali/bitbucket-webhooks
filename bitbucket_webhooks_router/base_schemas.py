"""Holds Marshmallow schemas."""
from marshmallow import Schema, fields
from marshmallow import EXCLUDE


class User(Schema):
    """
    https://confluence.atlassian.com/bitbucket/event-payloads-740262817.html#EventPayloads-entity_user
    """
    class Meta:
        unknown = EXCLUDE

    type = fields.String()
    username = fields.String()
    nickname = fields.String()
    display_name = fields.String()
    uuid = fields.String()


class Project(Schema):
    """
    """
    class Meta:
        unknown = EXCLUDE

    name = fields.String()
    uuid = fields.String()
    key = fields.String()


class Repository(Schema):
    """
    """
    class Meta:
        unknown = EXCLUDE

    name = fields.String()
    full_name = fields.String()
    website = fields.String(allow_none=True)
    uuid = fields.String()
    owner = fields.Nested(User)
    project = fields.Nested(Project)
    is_private = fields.Boolean()


class PullRequest(Schema):
    """
    """
    class Meta:
        unknown = EXCLUDE

    id = fields.Int()
    title = fields.String()
    description = fields.String()
    # TODO: Change this to enum.
    state = fields.String()
    author = fields.Nested(User)
    participants = fields.List(fields.Nested(User))
    reviewers = fields.List(fields.Nested(User))
    closed_by = fields.Nested(User)
    reason = fields.String()
    created_on = fields.DateTime()
    updated_on = fields.DateTime()
