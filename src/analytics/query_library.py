QUERIES = {

    "overview": {

        "total_patients": """
        SELECT COUNT(*) total_patients
        FROM patient_summary
        WHERE 1=1
        """,

        "total_providers": """
        SELECT COUNT(*) total_providers
        FROM provider_summary
        WHERE 1=1
        """,

        "total_organizations": """
        SELECT COUNT(*) total_organizations
        FROM organization_summary
        WHERE 1=1
        """,

    },

    "patients": {

        "gender_distribution": """
        SELECT
            GENDER,
            COUNT(*) patients
        FROM patient_summary
        WHERE 1=1
        GROUP BY GENDER
        ORDER BY patients DESC
        """,

        "average_age": """
        SELECT
            ROUND(AVG(age),2) average_age
        FROM patient_summary
        WHERE 1=1
        """,

    },

    "providers": {

        "top_providers": """
        SELECT
            NAME,
            total_encounters
        FROM provider_summary
        WHERE 1=1
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
        WHERE 1=1
        ORDER BY total_encounters DESC
        LIMIT 10
        """,

    },

}

QUERIES["patients"]["available_genders"] = """
SELECT DISTINCT
    GENDER
FROM patient_summary
WHERE 1=1
ORDER BY GENDER
"""

QUERIES["organizations"]["available_organizations"] = """
SELECT
    NAME
FROM organization_summary
WHERE 1=1
ORDER BY NAME
"""