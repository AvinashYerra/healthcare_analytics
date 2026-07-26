from analytics.analytics_registry import DATASETS


ORGANIZATION_SUMMARY = f"""
read_parquet('{DATASETS["organizations"]}/*.parquet')
"""

TOP_ORGANIZATIONS = f"""
SELECT
NAME,
provider_count,
total_encounters
FROM {ORGANIZATION_SUMMARY}
ORDER BY total_encounters DESC
LIMIT 10
"""

TOTAL_ORGANIZATIONS = f"""
SELECT COUNT(*) AS organizations
FROM {ORGANIZATION_SUMMARY}
"""