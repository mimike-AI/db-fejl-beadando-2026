import json
import os

from data.model_dataclasses import Person, Sex, HealthProfile, Diagnosis, GalacticProfile

def write_people(people: list[Person],
                 path: str,
                 file_name: str = "people",
                 extension: str = ".json",
                 pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w",
              encoding="utf-8") as file:
        json.dump([person.__dict__ for person in people], file,
                  indent=2 if pretty else None, ensure_ascii=False)


def read_people(path: str,
                file_name: str = "people",
                extension: str = ".json") -> list[Person]:
    with open(os.path.join(path, file_name + extension),
              encoding="utf-8") as file:
        people = []
        objects = json.load(file)
        for obj in objects:
            person = Person(obj["id"], obj["name"], obj["age"],
                            Sex(obj["sex"]))
            people.append(person)
        return people


def write_health_profiles(profiles: list[HealthProfile],
                          path: str,
                          file_name: str = "health_profiles",
                          extension: str = ".json",
                          pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w",
              encoding="utf-8") as file:
        json.dump([profile.__dict__ for profile in profiles], file,
                  indent=2 if pretty else None, ensure_ascii=False)


def read_health_profiles(path: str,
                         file_name: str = "health_profiles",
                         extension: str = ".json") -> list[HealthProfile]:
    with open(os.path.join(path, file_name + extension),
              encoding="utf-8") as file:
        profiles = []
        objects = json.load(file)
        for obj in objects:
            profile = HealthProfile(obj["person_id"], obj["blood_type"],
                                    obj["height_cm"], obj["weight_kg"],
                                    obj["bmi"])
            profiles.append(profile)
        return profiles


def write_diagnoses(diagnoses: list[Diagnosis],
                    path: str,
                    file_name: str = "diagnoses",
                    extension: str = ".json",
                    pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w",
              encoding="utf-8") as file:
        json.dump([diagnosis.__dict__ for diagnosis in diagnoses], file,
                  indent=2 if pretty else None, ensure_ascii=False)


def read_diagnoses(path: str,
                   file_name: str = "diagnoses",
                   extension: str = ".json") -> list[Diagnosis]:
    with open(os.path.join(path, file_name + extension),
              encoding="utf-8") as file:
        diagnoses = []
        objects = json.load(file)
        for obj in objects:
            diagnosis = Diagnosis(obj["id"], obj["person_id"],
                                  obj["disease"], obj["icd10"],
                                  obj["specialty"])
            diagnoses.append(diagnosis)
        return diagnoses


def write_galactic_profiles(profiles: list[GalacticProfile],
                            path: str,
                            file_name: str = "galactic_profiles",
                            extension: str = ".json",
                            pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w",
              encoding="utf-8") as file:
        json.dump([profile.__dict__ for profile in profiles], file,
                  indent=2 if pretty else None, ensure_ascii=False)


def read_galactic_profiles(path: str,
                           file_name: str = "galactic_profiles",
                           extension: str = ".json") -> list[GalacticProfile]:
    with open(os.path.join(path, file_name + extension),
              encoding="utf-8") as file:
        profiles = []
        objects = json.load(file)
        for obj in objects:
            profile = GalacticProfile(obj["person_id"], obj["scifi_name"],
                                      obj["rank"], obj["starship"],
                                      obj["starship_registry"],
                                      obj["starship_class"], obj["location"],
                                      obj["language"])
            profiles.append(profile)
        return profiles


def write_characters(people: list[Person],
                     health_profiles: list[HealthProfile],
                     diagnoses: list[Diagnosis],
                     galactic_profiles: list[GalacticProfile],
                     path: str,
                     file_name: str = "characters",
                     extension: str = ".json",
                     pretty: bool = True) -> None:
    health_by_person = {h.person_id: h for h in health_profiles}
    galactic_by_person = {g.person_id: g for g in galactic_profiles}
    diagnoses_by_person = {}
    for d in diagnoses:
        diagnoses_by_person.setdefault(d.person_id, []).append(d)

    characters = []
    for person in people:
        characters.append({
            "person": person.__dict__,
            "galactic_profile": galactic_by_person[person.id].__dict__,
            "health_profile": health_by_person[person.id].__dict__,
            "diagnoses": [d.__dict__
                          for d in diagnoses_by_person.get(person.id, [])]
        })

    with open(os.path.join(path, file_name + extension), "w",
              encoding="utf-8") as file:
        json.dump(characters, file,
                  indent=2 if pretty else None, ensure_ascii=False)


def read_characters(path: str,
                    file_name: str = "characters",
                    extension: str = ".json"
                    ) -> tuple[list[Person], list[HealthProfile],
                               list[Diagnosis], list[GalacticProfile]]:
    with open(os.path.join(path, file_name + extension),
              encoding="utf-8") as file:
        characters = json.load(file)

    people = []
    health_profiles = []
    diagnoses = []
    galactic_profiles = []
    for character in characters:
        p = character["person"]
        people.append(Person(p["id"], p["name"], p["age"], Sex(p["sex"])))

        g = character["galactic_profile"]
        galactic_profiles.append(GalacticProfile(
            g["person_id"], g["scifi_name"], g["rank"], g["starship"],
            g["starship_registry"], g["starship_class"], g["location"],
            g["language"]))

        h = character["health_profile"]
        health_profiles.append(HealthProfile(
            h["person_id"], h["blood_type"], h["height_cm"],
            h["weight_kg"], h["bmi"]))

        for d in character["diagnoses"]:
            diagnoses.append(Diagnosis(
                d["id"], d["person_id"], d["disease"], d["icd10"],
                d["specialty"]))

    return people, health_profiles, diagnoses, galactic_profiles
