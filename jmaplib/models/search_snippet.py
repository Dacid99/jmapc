from __future__ import annotations

from dataclasses import dataclass

from jmaplib.serializer import Model


@dataclass
class SearchSnippet(Model):
    email_id: str
    subject: str | None = None
    preview: str | None = None
