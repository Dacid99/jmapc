from __future__ import annotations

from dataclasses import dataclass, field

from dataclasses_json import config

from .. import constants
from ..models import Thread
from .base import Changes, ChangesResponse, Get, GetResponse


class ThreadBase:
    method_namespace: str | None = "Thread"
    using = {constants.JMAP_URN_MAIL}


@dataclass
class ThreadChanges(ThreadBase, Changes):
    pass


@dataclass
class ThreadChangesResponse(ThreadBase, ChangesResponse):
    pass


@dataclass
class ThreadGet(ThreadBase, Get):
    pass


@dataclass
class ThreadGetResponse(ThreadBase, GetResponse):
    data: list[Thread] = field(metadata=config(field_name="list"))
