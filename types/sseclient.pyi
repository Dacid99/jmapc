from typing import Any

class SSEClient:
    def __init__(
        self,
        url: str,
        last_id: str | None = None,
        retry: int = 3000,
        session: Any | None = None,
        chunk_size: int = 1024,
        **kwargs: Any,
    ):
        ...

    def __iter__(self) -> SSEClient:
        ...

    def __next__(self) -> Event:
        ...

class Event:
    def __init__( # noqa: PYI048 # we want to type the members
        self,
        data: str = "",
        event: str = "message",
        id: str | None = None, # noqa: A002 # id builtin not needed here
        retry: str | None = None,
    ):
        self.data: str
        self.event: str
        self.id: str
        self.retry: str
