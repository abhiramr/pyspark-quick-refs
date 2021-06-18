# Read CSV
df = spark.read.option("header", "true").option("inferSchema", "false").parquet("./Desktop/000.csv")
df.printSchema()
