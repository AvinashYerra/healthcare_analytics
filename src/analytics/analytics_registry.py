from config.paths import GOLD_DIR

ANALYTICS = {

    "patient_summary": {
        "path": GOLD_DIR / "patient_summary",
        "table": "patient_summary",
    },

    "provider_summary": {
        "path": GOLD_DIR / "provider_summary",
        "table": "provider_summary",
    },

    "organization_summary": {
        "path": GOLD_DIR / "organization_summary",
        "table": "organization_summary",
    },

}