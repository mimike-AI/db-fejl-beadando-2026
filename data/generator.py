from faker import Faker
from faker_healthcare import HealthcareProvider
from faker_galactic import SciFiProvider
from data.model_dataclasses import Person, Sex
from data.model_dataclasses import HealthProfile, Diagnosis, GalacticProfile
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


def generate_galactic_profiles(people: list[Person]) -> list[GalacticProfile]:

    fake = Faker()
    fake.add_provider(SciFiProvider)

    profiles = []
    for person in people:
        if person.sex is Sex.MALE:
            scifi_name = (f"{fake.scifi_first_name_male()} "
                          f"{fake.scifi_last_name_male()}")
        else:
            scifi_name = (f"{fake.scifi_first_name_female()} "
                          f"{fake.scifi_last_name_female()}")

        profiles.append(GalacticProfile(
            person.id,
            scifi_name,
            fake.scifi_rank(),
            fake.starship(),
            fake.starship_registry(),
            fake.starship_class(),
            fake.scifi_location(),
            fake.scifi_language()))

    return profiles
