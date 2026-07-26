from pyspark.sql.functions import countDistinct


class ProviderSummaryTransformer:

    def transform(
        self,
        providers,
        encounters,
    ):

        encounter_summary = (
            encounters
            .groupBy("PROVIDER")
            .agg(
                countDistinct("Id").alias("total_encounters"),
                countDistinct("PATIENT").alias("unique_patients"),
            )
        )

        summary = (
            providers
            .join(
                encounter_summary,
                providers.Id == encounter_summary.PROVIDER,
                "left",
            )
            .drop(encounter_summary.PROVIDER)
            .fillna(
                {
                    "total_encounters": 0,
                    "unique_patients": 0,
                }
            )
        )

        return summary
    

