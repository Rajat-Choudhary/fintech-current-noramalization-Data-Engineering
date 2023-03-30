from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Source process").getOrCreate()
df = spark.read.option("header",True).csv("/home/rajat/Documents/data-file-for-practice-Data-Engineering/banktxn.csv")


