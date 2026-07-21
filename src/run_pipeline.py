import sys

from pipelines.generic_pipeline import GenericPipeline
from pipelines.patient_summary_pipeline import PatientSummaryPipeline
from pipelines.provider_summary_pipeline import ProviderSummaryPipeline
from pipelines.organization_summary_pipeline import OrganizationSummaryPipeline
from config.dataset_registry import DATASETS


def run_pipeline(dataset):

    if dataset not in DATASETS:
        raise ValueError(
            f"Unknown dataset: {dataset}\n"
            f"Available datasets: {list(DATASETS.keys())}"
        )

    if dataset == "patient_summary":
        pipeline = PatientSummaryPipeline()
        
    elif dataset == "provider_summary":
        pipeline = ProviderSummaryPipeline()
        
    elif dataset == "organization_summary":
        pipeline = OrganizationSummaryPipeline()
    else:

        config = DATASETS[dataset]
        print(f"\nRunning {dataset} pipeline...\n")
        pipeline = GenericPipeline(
            dataset_name=dataset,
            config=config,
        )

    pipeline.run()


def main():

    if len(sys.argv) != 2:
        print("Usage:")
        print("python src/run_pipeline.py <dataset>")
        return

    run_pipeline(sys.argv[1])


if __name__ == "__main__":
    main()