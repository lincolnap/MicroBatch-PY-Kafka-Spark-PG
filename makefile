kaf_up:
	docker-compose -f Kafka/kafka-tools.yml up -d

kaf_down:
	docker-compose -f PG/pg.yml down

kaf_down_all:  
	docker-compose down -f Kafka/kafka-tools.yml --rmi all

pg_up:
	docker-compose -f PG/pg.yml up -d

pg_down:
	docker-compose -f PG/pg.yml down

pg_down_all:
	docker-compose -f PG/pg.yml down --rmi all

spk_up:
	docker-compose -f Spark/spark-owner.yml up -d

afl_up: 
	docker-compose -f Airflow/docker-compose.yaml up -d

afl_down: 
	docker-compose -f Airflow/docker-compose.yaml down