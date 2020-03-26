"""Holds Marshmallow schemas."""
import marshmallow_objects as mm


class User(mm.Model):
    """
    https://confluence.atlassian.com/bitbucket/event-payloads-740262817.html#EventPayloads-entity_user
    """
    class Meta:
        unknown = mm.EXCLUDE

    type = mm.fields.String()
    username = mm.fields.String()
    nickname = mm.fields.String()
    display_name = mm.fields.String()
    uuid = mm.fields.String()


class Project(mm.Model):
    """
    """
    class Meta:
        unknown = mm.EXCLUDE

    name = mm.fields.String()
    uuid = mm.fields.String()
    key = mm.fields.String()


class Repository(mm.Model):
    """
    """
    class Meta:
        unknown = mm.EXCLUDE

    name = mm.fields.String()
    full_name = mm.fields.String()
    website = mm.fields.String(allow_none=True)
    uuid = mm.fields.String()
    owner = mm.NestedModel(User)
    project = mm.NestedModel(Project)
    is_private = mm.fields.Boolean()


class PullRequest(mm.Model):
    """
    """
    class Meta:
        unknown = mm.EXCLUDE

    id = mm.fields.Int()
    title = mm.fields.String()
    description = mm.fields.String()
    # TODO: Change this to enum.
    state = mm.fields.String()
    author = mm.NestedModel(User)
    participants = mm.fields.List(mm.NestedModel(User))
    reviewers = mm.fields.List(mm.NestedModel(User))
    closed_by = mm.NestedModel(User)
    reason = mm.fields.String()
    created_on = mm.fields.DateTime()
    updated_on = mm.fields.DateTime()
