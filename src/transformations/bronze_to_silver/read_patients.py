from spark.session import create_spark_session
from spark.BronzeReader import read_csv


def main():

    spark = create_spark_session("Read Patients")

    df = read_csv(
        spark,
        # "/Users/avinashyerra/Downloads/synthea/output/csv/patients.csv"
        "data/sample/csv/patients.csv"
    )

    print(f"Total Patients: {df.count()}")

    df.printSchema()

    df.show(10, truncate=False)

    spark.stop()


if __name__ == "__main__":
    main()