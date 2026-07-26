from config.paths import OUTPUT_DIR

from pipelines.gold.base_summary_pipeline import BaseSummaryPipeline

from transformations.silver_to_gold.organization_summary_transformer import (
    OrganizationSummaryTransformer,
)


class OrganizationSummaryPipeline(BaseSummaryPipeline):

    def __init__(self):

        super().__init__(
            "organization_summary",
            OUTPUT_DIR / "gold/organization_summary",
        )

    def build_summary(
        self,
        reader,
        metrics,
    ):

        organizations = reader.read(
            OUTPUT_DIR / "silver/organizations"
        )

        providers = reader.read(
            OUTPUT_DIR / "silver/providers"
        )

        encounters = reader.read(
            OUTPUT_DIR / "silver/encounters"
        )

        metrics.input_records = organizations.count()

        transformer = OrganizationSummaryTransformer()

        return transformer.transform(
            organizations,
            providers,
            encounters,
        )