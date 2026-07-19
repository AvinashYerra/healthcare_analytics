from config.paths import SAMPLE_DATA_DIR, SILVER_DIR

from schemas.patient_schema import patient_schema
from schemas.organization_schema import organization_schema
from schemas.provider_schema import provider_schema
from schemas.encounter_schema import encounter_schema
from schemas.condition_schema import condition_schema

from transformations.bronze_to_silver.patient_transformer import PatientTransformer
from transformations.bronze_to_silver.organization_transformer import OrganizationTransformer
from transformations.bronze_to_silver.provider_transformer import ProviderTransformer
from transformations.bronze_to_silver.encounter_transformer import EncounterTransformer
from transformations.bronze_to_silver.condition_transformer import ConditionTransformer


DATASETS = {

    "patients": {

        "schema": patient_schema,
        "transformer": PatientTransformer(),
        "primary_key": "Id",
        "input_format": "csv",
        "bronze_path": SAMPLE_DATA_DIR / "patients.csv",
        "silver_path": SILVER_DIR / "patients",
        "partition_columns": [],
        "description": "Patient Master"
    },

    "organizations": {
        "schema": organization_schema,
        "transformer": OrganizationTransformer(),
        "primary_key": "Id",
        "input_format": "csv",
        "bronze_path": SAMPLE_DATA_DIR / "organizations.csv",
        "silver_path": SILVER_DIR / "organizations",
        "partition_columns": [],
        "description": "Organization Master"
    },

    "providers": {
        "schema": provider_schema,
        "transformer": ProviderTransformer(),
        "primary_key": "Id",
        "input_format": "csv",
        "bronze_path": SAMPLE_DATA_DIR / "providers.csv",
        "silver_path": SILVER_DIR / "providers",
        "partition_columns": [],
        "description": "Provider Master"
    },

    "encounters": {
        "schema": encounter_schema,
        "transformer": EncounterTransformer(),
        "primary_key": "Id",
        "input_format": "csv",
        "bronze_path": SAMPLE_DATA_DIR / "encounters.csv",
        "silver_path": SILVER_DIR / "encounters",
        "partition_columns": [],
        "description": "Encounter Master"
    },

    "conditions": {
        "schema": condition_schema,
        "transformer": ConditionTransformer(),
        "primary_key": "Id",
        "input_format": "csv",
        "bronze_path": SAMPLE_DATA_DIR / "conditions.csv",
        "silver_path": SILVER_DIR / "conditions",
        "partition_columns": [],
        "description": "Condition Master"
    },
}