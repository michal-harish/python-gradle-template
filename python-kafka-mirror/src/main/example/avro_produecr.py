from confluent_kafka import KafkaError
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
from confluent_kafka.avro.serializer import SerializerError
import os

KAFKA_BOOTSTRAP_SERVERS = os.environ['KAFKA_BOOTSTRAP_SERVERS']
SCHEMA_REGISTRY_URL = os.environ['SCHEMA_REGISTRY_URL']

SCHEMA=avro.load(os.path.join(os.path.dirname(__file__), '../resources/value_schema.avsc'))
INPUT_TOPIC='test-input'
OUTPUT_TOPIC='test-output'

def main():

    p = AvroProducer({'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS, 'schema.registry.url': SCHEMA_REGISTRY_URL})

    value = {"name": "Value", "favorite_number": 10, "favorite_color": "green", "age": 25}

    p.produce(topic=INPUT_TOPIC, value=value, value_schema=SCHEMA)

    p.flush()

main()