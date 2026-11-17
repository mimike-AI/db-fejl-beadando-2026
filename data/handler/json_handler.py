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
