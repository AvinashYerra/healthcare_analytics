from pyspark.sql.functions import (
    col,
    countDistinct,
)


class PatientSummaryTransformer:

    def transform(
        self,
        patients,
        encounters,
        conditions,
    ):

        encounter_counts = (
            encounters
            .groupBy("PATIENT")
            .agg(
                countDistinct("Id").alias("total_encounters")
            )
        )

        condition_counts = (
            conditions
            .groupBy("PATIENT")
            .agg(
                countDistinct("DESCRIPTION").alias("total_conditions")
            )
        )

        summary = (
            patients
            .join(
                encounter_counts,
                patients.Id == encounter_counts.PATIENT,
                "left",
            )
            .join(
                condition_counts,
                patients.Id == condition_counts.PATIENT,
                "left",
            )
            .drop(
                encounter_counts.PATIENT,
                condition_counts.PATIENT,
            )
            .fillna(
                {
                    "total_encounters": 0,
                    "total_conditions": 0,
                }
            )
        )

        return summary