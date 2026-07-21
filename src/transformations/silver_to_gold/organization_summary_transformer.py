from pyspark.sql.functions import countDistinct


class OrganizationSummaryTransformer:

    def transform(
        self,
        organizations,
        providers,
        encounters,
    ):

        provider_summary = (
            providers
            .groupBy("ORGANIZATION")
            .agg(
                countDistinct("Id").alias("provider_count")
            )
        )

        encounter_summary = (
            encounters
            .groupBy("ORGANIZATION")
            .agg(
                countDistinct("Id").alias("total_encounters"),
                countDistinct("PATIENT").alias("unique_patients"),
            )
        )

        summary = (
            organizations
            .join(
                provider_summary,
                organizations.Id == provider_summary.ORGANIZATION,
                "left",
            )
            .join(
                encounter_summary,
                organizations.Id == encounter_summary.ORGANIZATION,
                "left",
            )
            .drop(
                provider_summary.ORGANIZATION,
                encounter_summary.ORGANIZATION,
            )
            .fillna(
                {
                    "provider_count": 0,
                    "total_encounters": 0,
                    "unique_patients": 0,
                }
            )
        )

        return summary