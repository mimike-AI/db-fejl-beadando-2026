from dataclasses import dataclass, field
from enum import StrEnum
from functools import total_ordering


class Sex(StrEnum):
    MALE = "M"
    FEMALE = "F"

    def __repr__(self) -> str:
        return self.name.lower()


@dataclass(unsafe_hash=True)
@total_ordering
class Person:
    id: str = field(hash=True)
    name: str = field(compare=False)
    age: int = field(compare=False)
    sex: Sex = field(compare=False,
                     default=Sex.MALE)

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Person):
            return NotImplemented

        return self.id < o.id