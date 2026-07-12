from schemas.patient_schema import patient_schema

DATASETS = {
    "patients": {
        "dataset": "patients",
        "primary_key": "Id",
        "schema": patient_schema,
        "input_path": "data/sample/csv/patients.csv",
        "output_path": "data/output/silver/patients"
    }
}

# DATASETS["encounters"] = {
#     "dataset": "encounters",
#     "primary_key": "Id",
#     "schema": encounter_schema,
#     "input_path": "data/sample/csv/encounters.csv",
#     "output_path": "data/output/silver/encounters"
# }