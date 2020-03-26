class handle_repo_push(object):
    methods = []
    def __init__(self, method):
        handle_repo_push.methods.append(method)


class handle_pr_approval(object):
    methods = []
    def __init__(self, method):
        handle_pr_approval.methods.append(method)
