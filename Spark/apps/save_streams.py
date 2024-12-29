from pyspark.sql import SparkSession
from pyspark.sql.functions import col,from_json
import time
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

schema = StructType([
    StructField("name", StringType(), True),
    StructField("location", StringType(), True),
    StructField("phone", StringType(), True)
])

def kafka_parameters(kafka_bootstrap_servers,kafka_topic):
    # Configuración de lectura desde Kafka
    kafka_bootstrap_servers = "kafka:9092"  # Cambia al host y puerto de tu cluster Kafka
    kafka_topic = "test"  # Nombre del tópico de Kafka
    
    kafkaParams = {
        "kafka.bootstrap.servers": f"{kafka_bootstrap_servers}",  # Replace with your broker addresses
        "subscribe":f"{kafka_topic}",  # Replace with your topic name
        "startingOffsets": "earliest",  # or "earliest"
        "key.deserializer": "org.apache.kafka.common.serialization.StringDeserializer",
        "value.deserializer": "org.apache.kafka.common.serialization.StringDeserializer"
    }
    #        "failOnDataLoss":"false",
    
    return kafkaParams

def read_stream(parameters):
    # Leer datos de Kafka
    kafka_df = spark.readStream \
        .format("kafka") \
        .options(**parameters)\
        .load()
    schema = StructType([
                StructField("name", StringType()),
                StructField("location", StringType()),
                StructField("phone", StringType()),
            ])
    messages_df = kafka_df \
        .select(col("value").cast("string").alias("json_string"))\
        .select(from_json(col("json_string"), schema).alias("data")) \
        .select("data.*") 
    
    # messages_df = kafka_df \
    #     .select(col("value").cast("string").alias("json_string"))\
    #     .select(from_json(col("json_string"), schema).alias("data")) \
    #     .select("data.*") 


    def save_parquet(batch_df, batch_id):
        #output_path = "./output_parquet"
        data = batch_df.collect()
        #batch_df.write.mode("append").parquet(output_path)

    def save_pg(batch_df, batch_id):
        #output_path = "./output_parquet"
        batch_df.write \
            .format("jdbc") \
            .option("url", "jdbc:postgresql://172.19.0.8:5432/streaming") \
            .option("dbtable", "clients") \
            .option("user", "postgres") \
            .option("password", "postgres") \
            .mode("append") \
            .save()
    
    def print_messages(batch_df, batch_id):
        print(f"--- Batch ID: {batch_id} ---")
        batch_df.show()

    query = messages_df.writeStream \
        .option('checkpointLocation', './spark_kafka_checkpoint')\
        .outputMode("update")\
        .foreachBatch(save_pg) \
        .trigger(availableNow=True)\
        .start()
        #.trigger(processingTime="2 seconds") \
    
    query.awaitTermination()

if __name__ == '__main__':
    spark = SparkSession.builder \
        .master("spark://spark-master:7077") \
        .appName("KafkaSparkStreamingExample") \
        .getOrCreate()

x = read_stream(kafka_parameters("kafka:9092","test"))