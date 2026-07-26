from analytics.analytics_registry import DATASETS


PATIENT_SUMMARY = f"""
read_parquet('{DATASETS["patients"]}/*.parquet')
"""


TOTAL_PATIENTS = f"""
SELECT COUNT(*) AS total_patients
FROM {PATIENT_SUMMARY}
"""

GENDER_DISTRIBUTION = f"""
SELECT
GENDER,
COUNT(*) AS patients
FROM {PATIENT_SUMMARY}
GROUP BY GENDER
ORDER BY patients DESC
"""

AVERAGE_AGE = f"""
SELECT
ROUND(AVG(age),2) AS average_age
FROM {PATIENT_SUMMARY}
"""

TOP_PATIENTS = f"""
SELECT
FIRST,
LAST,
condition_count
FROM {PATIENT_SUMMARY}
ORDER BY condition_count DESC
LIMIT 10
"""