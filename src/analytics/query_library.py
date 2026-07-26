QUERIES = {

    "overview": {

        "total_patients": """
        SELECT COUNT(*) total_patients
        FROM patient_summary
        """,

        "total_providers": """
        SELECT COUNT(*) total_providers
        FROM provider_summary
        """,

        "total_organizations": """
        SELECT COUNT(*) total_organizations
        FROM organization_summary
        """,

    },

    "patients": {

        "gender_distribution": """
        SELECT
            GENDER,
            COUNT(*) patients
        FROM patient_summary
        GROUP BY GENDER
        ORDER BY patients DESC
        """,

        "average_age": """
        SELECT
            ROUND(AVG(age),2) average_age
        FROM patient_summary
        """,

    },

    "providers": {

        "top_providers": """
        SELECT
            NAME,
            total_encounters
        FROM provider_summary
        ORDER BY total_encounters DESC
        LIMIT 10
        """,

    },

    "organizations": {

        "top_organizations": """
        SELECT
            NAME,
            total_encounters
        FROM organization_summary
        ORDER BY total_encounters DESC
        LIMIT 10
        """,

    },

}