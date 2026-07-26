from config.paths import OUTPUT_DIR

from pipelines.gold.base_summary_pipeline import BaseSummaryPipeline

from transformations.silver_to_gold.provider_summary_transformer import (
    ProviderSummaryTransformer,
)


class ProviderSummaryPipeline(BaseSummaryPipeline):

    def __init__(self):

        super().__init__(
            "provider_summary",
            OUTPUT_DIR / "gold/provider_summary",
        )

    def build_summary(
        self,
        reader,
        metrics,
    ):

        providers = reader.read(
            OUTPUT_DIR / "silver/providers"
        )

        encounters = reader.read(
            OUTPUT_DIR / "silver/encounters"
        )

        metrics.input_records = providers.count()

        transformer = ProviderSummaryTransformer()

        return transformer.transform(
            providers,
            encounters,
        )