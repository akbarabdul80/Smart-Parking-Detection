import datetime
from dataclasses import dataclass


@dataclass
class DataLocation:
    title: str
    long: str
    lat: str


@dataclass
class DataPattern:
    title: str
    qty: int
    free: int
    last_update: datetime.datetime
    pattern: str
