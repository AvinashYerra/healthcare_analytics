from config.paths import GOLD_DIR
from pipelines.gold.patient_summary_pipeline import PatientSummaryPipeline
from pipelines.gold.provider_summary_pipeline import ProviderSummaryPipeline
from pipelines.gold.organization_summary_pipeline import OrganizationSummaryPipeline

SUMMARIES = {
    "patient_summary": {
        "pipeline": PatientSummaryPipeline(),
        "output_path": GOLD_DIR / "patient_summary",
        "description": "Patient Summary",
    },
    "provider_summary": {
        "pipeline": ProviderSummaryPipeline(),
        "output_path": GOLD_DIR / "provider_summary",
        "description": "Provider Summary",
    },
    "organization_summary": {
        "pipeline": OrganizationSummaryPipeline(),
        "output_path": GOLD_DIR / "organization_summary",
        "description": "Organization Summary",
    },
}