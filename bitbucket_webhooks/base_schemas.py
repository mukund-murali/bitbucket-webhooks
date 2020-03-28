import marshmallow_objects as mo


class User(mo.Model):
    class Meta:
        unknown = mo.EXCLUDE

    type = mo.fields.String()
    username = mo.fields.String()
    nickname = mo.fields.String()
    display_name = mo.fields.String()
    uuid = mo.fields.String()


class Project(mo.Model):
    class Meta:
        unknown = mo.EXCLUDE

    name = mo.fields.String()
    uuid = mo.fields.String()
    key = mo.fields.String()


class Repository(mo.Model):
    class Meta:
        unknown = mo.EXCLUDE

    name = mo.fields.String()
    full_name = mo.fields.String()
    website = mo.fields.String(allow_none=True)
    uuid = mo.fields.String()
    owner = mo.NestedModel(User)
    project = mo.NestedModel(Project)
    is_private = mo.fields.Boolean()


class Branch(mo.Model):
    class Meta:
        unknown = mo.EXCLUDE

    name = mo.fields.String()


class Commit(mo.Model):
    class Meta:
        unknown = mo.EXCLUDE

    hash = mo.fields.String()


class ChangeLocation(mo.Model):
    class Meta:
        unknown = mo.EXCLUDE

    repository = mo.NestedModel(Repository)
    branch = mo.NestedModel(Branch)
    commit = mo.NestedModel(Commit)


class Participant(mo.Model):
    class Meta:
        unknown = mo.EXCLUDE

    role = mo.fields.String()
    participated_on = mo.fields.DateTime()
    approved = mo.fields.Boolean()
    user = mo.NestedModel(User)


class PullRequest(mo.Model):
    class Meta:
        unknown = mo.EXCLUDE

    id = mo.fields.Int()
    title = mo.fields.String()
    description = mo.fields.String()
    # TODO: Change this to enum.
    state = mo.fields.String()
    author = mo.NestedModel(User)
    source = mo.NestedModel(ChangeLocation)
    destination = mo.NestedModel(ChangeLocation)
    merge_commit = mo.NestedModel(Commit, allow_none=True)
    participants = mo.fields.List(mo.NestedModel(Participant))
    reviewers = mo.fields.List(mo.NestedModel(User))
    closed_by = mo.NestedModel(User, allow_none=True)
    reason = mo.fields.String()
    created_on = mo.fields.DateTime()
    updated_on = mo.fields.DateTime()
    comment_count = mo.fields.Int(allow_none=True)
    task_count = mo.fields.Int(allow_none=True)
    close_source_branch = mo.fields.Boolean(allow_none=True)


class CommentContent(mo.Model):
    class Meta:
        unknown = mo.EXCLUDE

    raw = mo.fields.String()
    markup = mo.fields.String()
    html = mo.fields.String()


class InlineComment(mo.Model):
    class Meta:
        unknown = mo.EXCLUDE

    to_line = mo.fields.Int(data_key="to")
    from_line = mo.fields.Int(allow_none=True, data_key="from")
    path = mo.fields.String()


class ParentComment(mo.Model):
    class Meta:
        unknown = mo.EXCLUDE

    id = mo.fields.Int()


class Comment(mo.Model):
    class Meta:
        unknown = mo.EXCLUDE

    id = mo.fields.Int()
    parent = mo.NestedModel(ParentComment)
    content = mo.NestedModel(CommentContent)
    inline = mo.NestedModel(InlineComment)
    created_on = mo.fields.DateTime()
    updated_on = mo.fields.DateTime()
