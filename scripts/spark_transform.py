from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Weather Transformation")
    .getOrCreate()
)

print("Spark Started Successfully")

spark.stop()