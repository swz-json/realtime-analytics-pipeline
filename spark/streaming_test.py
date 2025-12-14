from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("StreamingTest") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

df = spark.readStream \
    .format("rate") \
    .option("rowsPerSecond", 5) \
    .load()

query = df.writeStream \
    .format("console") \
    .outputMode("append") \
    .start()

query.awaitTermination()
