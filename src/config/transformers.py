from transformations.bronze_to_silver.patient_transformer import PatientTransformer
from transformations.bronze_to_silver.encounter_transformer import EncounterTransformer
from transformations.bronze_to_silver.organization_transformer import OrganizationTransformer

TRANSFORMERS = {
    "patients": PatientTransformer,
    "encounters": EncounterTransformer,
    "organizations": OrganizationTransformer
}

