from config.paths import OUTPUT_DIR

from pipelines.gold.base_summary_pipeline import BaseSummaryPipeline

from transformations.silver_to_gold.patient_summary_transformer import (
    PatientSummaryTransformer,
)


class PatientSummaryPipeline(BaseSummaryPipeline):

    def __init__(self):

        super().__init__(
            "patient_summary",
            OUTPUT_DIR / "gold/patient_summary",
        )

    def build_summary(
        self,
        reader,
        metrics,
    ):

        patients = reader.read(
            OUTPUT_DIR / "silver/patients"
        )

        encounters = reader.read(
            OUTPUT_DIR / "silver/encounters"
        )

        conditions = reader.read(
            OUTPUT_DIR / "silver/conditions"
        )

        metrics.input_records = patients.count()

        transformer = PatientSummaryTransformer()

        return transformer.transform(
            patients,
            encounters,
            conditions,
        )