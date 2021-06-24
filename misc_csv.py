# Read Parquet
df = spark.read.option("header", "true").option("inferSchema", "false").parquet("./Desktop/000.parquet")
df.printSchema()


# Read CSV
df = spark.read.option("header", "true").option("inferSchema", "false").csv("./Desktop/000.csv")
df.printSchema()
