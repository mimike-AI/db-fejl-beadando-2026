import csv
import os

from data.model_dataclasses import Person, Sex, HealthProfile, Diagnosis, GalacticProfile


def write_people(people: list[Person],
                 path: str,
                 file_name: str = "people",
                 extension: str = ".csv",
                 heading: bool = True,
                 delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name + extension), "w",
              newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, delimiter=delimiter,
                    fieldnames=["id", "name", "age", "sex"])
        if heading:
            writer.writeheader()
        for person in people:
            writer.writerow(person.__dict__)

def read_people(path: str,
                 file_name: str = "people",
                 extension: str = ".csv",
                 delimiter: str = ";") -> list[Person]:
    with open(os.path.join(path, file_name + extension),
              newline="", encoding="utf-8") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        people = []
        for row in rows:
            people.append(
                Person(row["id"], row["name"], int(row["age"]),
                       Sex(row["sex"]))
            )
        return people


def write_health_profiles(profiles: list[HealthProfile],
                          path: str,
                          file_name: str = "health_profiles",
                          extension: str = ".csv",
                          heading: bool = True,
                          delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name + extension), "w",
              newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, delimiter=delimiter,
                    fieldnames=["person_id", "blood_type", "height_cm",
                                "weight_kg", "bmi"])
        if heading:
            writer.writeheader()
        for profile in profiles:
            writer.writerow(profile.__dict__)


def read_health_profiles(path: str,
                         file_name: str = "health_profiles",
                         extension: str = ".csv",
                         delimiter: str = ";") -> list[HealthProfile]:
    with open(os.path.join(path, file_name + extension),
              newline="", encoding="utf-8") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        profiles = []
        for row in rows:
            profiles.append(
                HealthProfile(row["person_id"], row["blood_type"],
                              float(row["height_cm"]),
                              float(row["weight_kg"]),
                              float(row["bmi"]))
            )
        return profiles


def write_diagnoses(diagnoses: list[Diagnosis],
                    path: str,
                    file_name: str = "diagnoses",
                    extension: str = ".csv",
                    heading: bool = True,
                    delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name + extension), "w",
              newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, delimiter=delimiter,
                    fieldnames=["id", "person_id", "disease", "icd10",
                                "specialty"])
        if heading:
            writer.writeheader()
        for diagnosis in diagnoses:
            writer.writerow(diagnosis.__dict__)


def read_diagnoses(path: str,
                   file_name: str = "diagnoses",
                   extension: str = ".csv",
                   delimiter: str = ";") -> list[Diagnosis]:
    with open(os.path.join(path, file_name + extension),
              newline="", encoding="utf-8") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        diagnoses = []
        for row in rows:
            diagnoses.append(
                Diagnosis(row["id"], row["person_id"], row["disease"],
                          row["icd10"], row["specialty"])
            )
        return diagnoses


def write_galactic_profiles(profiles: list[GalacticProfile],
                            path: str,
                            file_name: str = "galactic_profiles",
                            extension: str = ".csv",
                            heading: bool = True,
                            delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name + extension), "w",
              newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, delimiter=delimiter,
                    fieldnames=["person_id", "scifi_name", "rank",
                                "starship", "starship_registry",
                                "starship_class", "location", "language"])
        if heading:
            writer.writeheader()
        for profile in profiles:
            writer.writerow(profile.__dict__)


def read_galactic_profiles(path: str,
                           file_name: str = "galactic_profiles",
                           extension: str = ".csv",
                           delimiter: str = ";") -> list[GalacticProfile]:
    with open(os.path.join(path, file_name + extension),
              newline="", encoding="utf-8") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        profiles = []
        for row in rows:
            profiles.append(
                GalacticProfile(row["person_id"], row["scifi_name"],
                                row["rank"], row["starship"],
                                row["starship_registry"],
                                row["starship_class"], row["location"],
                                row["language"])
            )
        return profiles
