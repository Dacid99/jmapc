from __future__ import annotations

from dataclasses import dataclass

from jmaplib.serializer import Model


@dataclass
class Thread(Model):
    def __len__(self) -> int:
        return len(self.email_ids)

    id: str
    email_ids: list[str]
