import openpyxl

from data.model_dataclasses import Person, Sex, HealthProfile, Diagnosis

def write_people(people: list[Person],
                 workbook: openpyxl.Workbook,
                 sheet_name: str = "people",
                 heading: bool = True) -> None:
    sheet = workbook.create_sheet(sheet_name)

    if heading:
        field_names = ["id", "name", "age", "sex"]
        for col in range(len(field_names)):
            sheet.cell(row=1, column=col + 1, value=field_names[col])

    offset = 2 if heading else 1
    for row in range(len(people)):
        sheet.cell(row=row + offset, column=1, value=people[row].id)
        sheet.cell(row=row + offset, column=2, value=people[row].name)
        sheet.cell(row=row + offset, column=3, value=people[row].age)
        sheet.cell(row=row + offset, column=4, value=people[row].sex)


def read_people(workbook: openpyxl.Workbook,
                sheet_name: str = "people",
                heading: bool = True) -> list[Person]:
    sheet = workbook[sheet_name]

    people = []
    row = 2 if heading else 1
    while True:
        if sheet.cell(row=row, column=1).value is None:
            break
        person = Person(
            sheet.cell(row=row, column=1).value,
            sheet.cell(row=row, column=2).value,
            int(sheet.cell(row=row, column=3).value),
            Sex(sheet.cell(row=row, column=4).value)
        )
        row += 1
        people.append(person)
    return people


def write_health_profiles(profiles: list[HealthProfile],
                          workbook: openpyxl.Workbook,
                          sheet_name: str = "health_profiles",
                          heading: bool = True) -> None:
    sheet = workbook.create_sheet(sheet_name)

    if heading:
        field_names = ["person_id", "blood_type", "height_cm",
                       "weight_kg", "bmi"]
        for col in range(len(field_names)):
            sheet.cell(row=1, column=col + 1, value=field_names[col])

    offset = 2 if heading else 1
    for row in range(len(profiles)):
        sheet.cell(row=row + offset, column=1, value=profiles[row].person_id)
        sheet.cell(row=row + offset, column=2, value=profiles[row].blood_type)
        sheet.cell(row=row + offset, column=3, value=profiles[row].height_cm)
        sheet.cell(row=row + offset, column=4, value=profiles[row].weight_kg)
        sheet.cell(row=row + offset, column=5, value=profiles[row].bmi)


def read_health_profiles(workbook: openpyxl.Workbook,
                         sheet_name: str = "health_profiles",
                         heading: bool = True) -> list[HealthProfile]:
    sheet = workbook[sheet_name]

    profiles = []
    row = 2 if heading else 1
    while True:
        if sheet.cell(row=row, column=1).value is None:
            break
        profile = HealthProfile(
            sheet.cell(row=row, column=1).value,
            sheet.cell(row=row, column=2).value,
            float(sheet.cell(row=row, column=3).value),
            float(sheet.cell(row=row, column=4).value),
            float(sheet.cell(row=row, column=5).value)
        )
        row += 1
        profiles.append(profile)
    return profiles


def write_diagnoses(diagnoses: list[Diagnosis],
                    workbook: openpyxl.Workbook,
                    sheet_name: str = "diagnoses",
                    heading: bool = True) -> None:
    sheet = workbook.create_sheet(sheet_name)

    if heading:
        field_names = ["id", "person_id", "disease", "icd10", "specialty"]
        for col in range(len(field_names)):
            sheet.cell(row=1, column=col + 1, value=field_names[col])

    offset = 2 if heading else 1
    for row in range(len(diagnoses)):
        sheet.cell(row=row + offset, column=1, value=diagnoses[row].id)
        sheet.cell(row=row + offset, column=2, value=diagnoses[row].person_id)
        sheet.cell(row=row + offset, column=3, value=diagnoses[row].disease)
        sheet.cell(row=row + offset, column=4, value=diagnoses[row].icd10)
        sheet.cell(row=row + offset, column=5, value=diagnoses[row].specialty)


def read_diagnoses(workbook: openpyxl.Workbook,
                   sheet_name: str = "diagnoses",
                   heading: bool = True) -> list[Diagnosis]:
    sheet = workbook[sheet_name]

    diagnoses = []
    row = 2 if heading else 1
    while True:
        if sheet.cell(row=row, column=1).value is None:
            break
        diagnosis = Diagnosis(
            sheet.cell(row=row, column=1).value,
            sheet.cell(row=row, column=2).value,
            sheet.cell(row=row, column=3).value,
            sheet.cell(row=row, column=4).value,
            sheet.cell(row=row, column=5).value
        )
        row += 1
        diagnoses.append(diagnosis)
    return diagnoses
