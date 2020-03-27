from abc import ABCMeta
from abc import abstractmethod
from typing import Callable
from typing import List


class BaseHandler(metaclass=ABCMeta):
    def __init__(self, method: Callable) -> None:
        type(self).methods.append(method)  # type: ignore

    @property
    @abstractmethod
    def methods(self) -> List[Callable]:
        raise NotImplementedError


class handle_repo_push(BaseHandler):
    methods: List[Callable] = []

    def __init__(self, method: Callable) -> None:
        super(handle_repo_push, self).__init__(method)


class handle_pr_approval(BaseHandler):
    methods: List[Callable] = []

    def __init__(self, method: Callable) -> None:
        super(handle_pr_approval, self).__init__(method)


class handle_pr_created(BaseHandler):
    methods: List[Callable] = []

    def __init__(self, method: Callable) -> None:
        super(handle_pr_created, self).__init__(method)


class handle_pr_updated(BaseHandler):
    methods: List[Callable] = []

    def __init__(self, method: Callable) -> None:
        super(handle_pr_updated, self).__init__(method)
