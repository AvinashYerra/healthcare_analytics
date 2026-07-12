from pyspark.sql.functions import col


def duplicate_count(df):
    return df.count() - df.dropDuplicates().count()


def null_count(df, column):
    return df.filter(col(column).isNull()).count()


def remove_duplicates(df):
    return df.dropDuplicates()


def remove_nulls(df, column):
    return df.filter(col(column).isNotNull())