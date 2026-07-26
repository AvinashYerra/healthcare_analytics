from analytics.analytics_service import AnalyticsService


def main():

    service = AnalyticsService()

    print("\nPatients\n")
    print(
        service.execute(
            "overview",
            "total_patients",
        )
    )

    print("\nProviders\n")
    print(
        service.execute(
            "overview",
            "total_providers",
        )
    )

    print("\nOrganizations\n")
    print(
        service.execute(
            "overview",
            "total_organizations",
        )
    )

    service.close()


if __name__ == "__main__":
    main()