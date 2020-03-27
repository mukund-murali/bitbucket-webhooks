from collections import defaultdict
from typing import Callable
from typing import Dict
from typing import List


class BaseHandler(object):
    _cls_methods_map: Dict[str, List[Callable]] = defaultdict(list)

    def __init__(self, method: Callable) -> None:
        BaseHandler._cls_methods_map[type(self).__name__].append(method)

    @classmethod
    def get_methods(cls) -> List[Callable]:
        return BaseHandler._cls_methods_map[cls.__name__]


class handle_repo_push(BaseHandler):
    def __init__(self, method: Callable) -> None:
        super(handle_repo_push, self).__init__(method)


class handle_pr_approved(BaseHandler):
    def __init__(self, method: Callable) -> None:
        super(handle_pr_approved, self).__init__(method)


class handle_pr_unapproved(BaseHandler):
    def __init__(self, method: Callable) -> None:
        super(handle_pr_unapproved, self).__init__(method)


class handle_pr_created(BaseHandler):
    def __init__(self, method: Callable) -> None:
        super(handle_pr_created, self).__init__(method)


class handle_pr_updated(BaseHandler):
    def __init__(self, method: Callable) -> None:
        super(handle_pr_updated, self).__init__(method)


class handle_pr_merged(BaseHandler):
    def __init__(self, method: Callable) -> None:
        super(handle_pr_merged, self).__init__(method)


class handle_pr_declined(BaseHandler):
    def __init__(self, method: Callable) -> None:
        super(handle_pr_declined, self).__init__(method)
