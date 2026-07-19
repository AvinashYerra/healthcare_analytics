from transformations.bronze_to_silver.patient_transformer import PatientTransformer
from transformations.bronze_to_silver.encounter_transformer import EncounterTransformer
from transformations.bronze_to_silver.organization_transformer import OrganizationTransformer
from transformations.bronze_to_silver.provider_transformer import ProviderTransformer


TRANSFORMERS = {
    "patients": PatientTransformer,
    "encounters": EncounterTransformer,
    "organizations": OrganizationTransformer,
    "providers": ProviderTransformer
}

