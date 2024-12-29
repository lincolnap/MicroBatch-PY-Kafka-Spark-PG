from pyspark.sql import SparkSession
from pyspark.sql.functions import col,from_json
import time
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

schema = StructType([
    StructField("name", StringType(), True),
    StructField("location", StringType(), True),
    StructField("phone", StringType(), True)
])

# Crear algunos datos de ejemplo
data = [
    ("Alice", "New York", "123-456-7890"),
    ("Bob", "Los Angeles", "987-654-3210"),
    ("Charlie", "Chicago", "555-555-5555")
]

spark = SparkSession.builder \
        .master("spark://spark:7077") \
        .appName("Saveparquet") \
        .getOrCreate()
        #.config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.4") \

# Crear el DataFrame
df = spark.createDataFrame(data, schema)

# Mostrar el DataFrame
df.show()

df.write.mode("append").parquet("./output_parquet-test")