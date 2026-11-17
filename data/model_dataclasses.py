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


@dataclass
class HealthProfile:
    person_id: str
    blood_type: str
    height_cm: float
    weight_kg: float
    bmi: float


@dataclass
class Diagnosis:
    id: str
    person_id: str
    disease: str
    icd10: str
    specialty: str


@dataclass
class GalacticProfile:
    person_id: str
    scifi_name: str
    rank: str
    starship: str
    starship_registry: str
    starship_class: str
    location: str
    language: str
