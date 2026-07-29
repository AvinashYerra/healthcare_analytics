import json

import pandas as pd

from config.paths import METRICS_DIR


class MetricsReader:

    def load(self):

        metrics = []

        for file in sorted(METRICS_DIR.glob("*.json")):

            with open(file) as f:
                metrics.append(json.load(f))

        return pd.DataFrame(metrics)