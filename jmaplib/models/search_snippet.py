from dataclasses import dataclass

from ..serializer import Model


@dataclass
class SearchSnippet(Model):
    email_id: str
    subject: str | None = None
    preview: str | None = None
