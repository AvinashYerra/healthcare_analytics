from schemas.patient_schema import patient_schema
from schemas.encounter_schema import encounter_schema
from schemas.organization_schema import organization_schema

DATASETS = {
    "patients": {
        "dataset": "patients",
        "primary_key": "Id",
        "schema": patient_schema,
        "input_path": "data/sample/csv/patients.csv",
        "output_path": "data/output/silver/patients"
    }
}

DATASETS["encounters"] = {
    "dataset": "encounters",
    "primary_key": "Id",
    "schema": encounter_schema,
    "input_path": "data/sample/csv/encounters.csv",
    "output_path": "data/output/silver/encounters"
},

DATASETS["organizations"] = {
    "dataset": "organizations",
    "schema": organization_schema,
    "primary_key": "Id",
    "input_path": "data/sample/csv/organizations.csv",
    "output_path": "data/output/silver/organizations",
}