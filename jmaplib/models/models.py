from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import TypeVar, Union

from dataclasses_json import config

from jmaplib.ref import Ref, ResultReference
from jmaplib.serializer import Model

T = TypeVar("T")
StrOrRef = Union[str, ResultReference, Ref]
ListOrRef = Union[list[T], ResultReference, Ref]
TypeOrRef = Union[T, ResultReference, Ref]


@dataclass
class Blob(Model):
    id: str = field(metadata=config(field_name="blobId"))
    type: str
    size: int


@dataclass
class AddedItem(Model):
    id: str = field(metadata=config(field_name="id"))
    index: int


@dataclass
class EmailAddress(Model):
    name: str | None = None
    email: str | None = None


@dataclass
class Comparator(Model):
    property: str
    is_ascending: bool = True
    collation: str | None = None
    anchor: str | None = None
    anchor_offset: int = 0
    limit: int | None = None
    calculate_total: bool = False
    position: int = 0


@dataclass
class FilterOperator(Model):
    operator: Operator


class Operator(Enum):
    AND = "AND"
    OR = "OR"
    NOT = "NOT"


@dataclass
class SetError(Model):
    type: str
    description: str | None = None
    already_exists: str | None = None
    not_found: list[str] | None = None
    properties: list[str] | None = None
