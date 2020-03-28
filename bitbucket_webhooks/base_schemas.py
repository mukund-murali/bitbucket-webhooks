import marshmallow_objects as mm


class User(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    type = mm.fields.String()
    username = mm.fields.String()
    nickname = mm.fields.String()
    display_name = mm.fields.String()
    uuid = mm.fields.String()


class Project(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    name = mm.fields.String()
    uuid = mm.fields.String()
    key = mm.fields.String()


class Repository(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    name = mm.fields.String()
    full_name = mm.fields.String()
    website = mm.fields.String(allow_none=True)
    uuid = mm.fields.String()
    owner = mm.NestedModel(User)
    project = mm.NestedModel(Project)
    is_private = mm.fields.Boolean()


class Branch(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    name = mm.fields.String()


class Commit(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    hash = mm.fields.String()


class ChangeLocation(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    repository = mm.NestedModel(Repository)
    branch = mm.NestedModel(Branch)
    commit = mm.NestedModel(Commit)


class Participant(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    role = mm.fields.String()
    participated_on = mm.fields.DateTime()
    approved = mm.fields.Boolean()
    user = mm.NestedModel(User)


class PullRequest(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    id = mm.fields.Int()
    title = mm.fields.String()
    description = mm.fields.String()
    # TODO: Change this to enum.
    state = mm.fields.String()
    author = mm.NestedModel(User)
    source = mm.NestedModel(ChangeLocation)
    destination = mm.NestedModel(ChangeLocation)
    merge_commit = mm.NestedModel(Commit, allow_none=True)
    participants = mm.fields.List(mm.NestedModel(Participant))
    reviewers = mm.fields.List(mm.NestedModel(User))
    closed_by = mm.NestedModel(User, allow_none=True)
    reason = mm.fields.String()
    created_on = mm.fields.DateTime()
    updated_on = mm.fields.DateTime()
    comment_count = mm.fields.Int(allow_none=True)
    task_count = mm.fields.Int(allow_none=True)
    close_source_branch = mm.fields.Boolean(allow_none=True)


class CommentContent(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    raw = mm.fields.String()
    markup = mm.fields.String()
    html = mm.fields.String()


class InlineComment(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    to_line = mm.fields.Int(data_key="to")
    from_line = mm.fields.Int(allow_none=True, data_key="from")
    path = mm.fields.String()


class ParentComment(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    id = mm.fields.Int()


class Comment(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    id = mm.fields.Int()
    parent = mm.NestedModel(ParentComment)
    content = mm.NestedModel(CommentContent)
    inline = mm.NestedModel(InlineComment)
    created_on = mm.fields.DateTime()
    updated_on = mm.fields.DateTime()
