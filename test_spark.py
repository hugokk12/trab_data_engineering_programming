from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SanityCheck") \
    .master("local[*]") \
    .getOrCreate()

df = spark.createDataFrame([(1, "Teste PySpark OK")], ["id", "mensagem"])
df.show()

spark.stop()
