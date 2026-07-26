from pipelines.gold.patient_summary_pipeline import PatientSummaryPipeline
from pipelines.gold.provider_summary_pipeline import ProviderSummaryPipeline
from pipelines.gold.organization_summary_pipeline import OrganizationSummaryPipeline

SUMMARIES = {

    "patient_summary": PatientSummaryPipeline(),

    "provider_summary": ProviderSummaryPipeline(),

    "organization_summary": OrganizationSummaryPipeline(),
}