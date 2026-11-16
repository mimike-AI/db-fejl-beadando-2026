from faker import Faker
from faker_healthcare import HealthcareProvider
from data.model_dataclasses import Person, Sex
from data.model_dataclasses import HealthProfile, Diagnosis
import random


def generate_people(n: int, male_ratio: float = 0.5,
                    locale: str = "hu_HU",
                    unique: bool = False,
                    min_age: int = 18,
                    max_age: int = 100) -> list[Person]:

    assert n > 0
    assert 0 <= male_ratio <= 1
    assert min_age >= 18
    assert min_age <= max_age <= 100

    people = []
    fake = Faker(locale)
    # Faker.seed(0)
    fake = fake if not unique else fake.unique
    for i in range(n):
        sex = Sex.MALE if random.random() < male_ratio else Sex.FEMALE
        person = Person(
            f"P-{str(i + 1).zfill(6)}",
            fake.name_male() if sex is Sex.MALE else fake.name_female(),
            random.randint(min_age, max_age),
            sex)

        people.append(person)

    return people


def generate_health_data(people: list[Person],
                         max_diagnoses: int = 3) -> tuple[list[HealthProfile], list[Diagnosis]]:

    assert max_diagnoses >= 0

    fake = Faker()
    fake.add_provider(HealthcareProvider)

    profiles = []
    diagnoses = []
    for person in people:
        body = fake.body_measurements(sex=person.sex.name.lower(), age=person.age)
        profiles.append(HealthProfile(
            person.id,
            fake.blood_type(),
            body["height_cm"],
            body["weight_kg"],
            body["bmi"]))

        seen = set()
        for _ in range(random.randint(0, max_diagnoses)):
            scenario = fake.patient_scenario()
            if scenario["disease"] in seen:
                continue
            seen.add(scenario["disease"])
            diagnoses.append(Diagnosis(
                f"D-{str(len(diagnoses) + 1).zfill(6)}",
                person.id,
                scenario["disease"],
                scenario["icd10"],
                scenario["medical_specialty"]))

    return profiles, diagnoses
