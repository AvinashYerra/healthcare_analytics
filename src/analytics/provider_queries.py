from analytics.analytics_registry import DATASETS


PROVIDER_SUMMARY = f"""
read_parquet('{DATASETS["providers"]}/*.parquet')
"""

TOTAL_PROVIDERS = f"""
SELECT COUNT(*) AS total_providers
FROM {PROVIDER_SUMMARY}
"""

TOP_PROVIDERS = f"""
SELECT
NAME,
total_encounters
FROM {PROVIDER_SUMMARY}
ORDER BY total_encounters DESC
LIMIT 10
"""

