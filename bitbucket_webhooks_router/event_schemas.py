from marshmallow import Schema, fields
from marshmallow import EXCLUDE

from bitbucket_webhooks_router import base_schemas


class RepoPush(Schema):
    class Meta:
        unknown = EXCLUDE

    actor = fields.Nested(base_schemas.User)
    repository = fields.Nested(base_schemas.Repository)
