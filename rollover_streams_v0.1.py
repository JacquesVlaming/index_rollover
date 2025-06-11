from elasticsearch import Elasticsearch
import os

es_host = os.getenv("ES_HOST", "default-prefix")
# api_key = os.getenv("API_KEY", "default-prefix")
es_username = os.getenv("ES_USERNAME", "default-prefix")
es_password = os.getenv("ES_PASSWORD", "default-prefix")



es = Elasticsearch(
    hosts=es_host,
    # api_key=api_key,
    basic_auth=(es_username, es_username),
    verify_certs=False,  # <- disables SSL certificate verification
    ssl_show_warn=False
)

try:
    data_streams = es.indices.get_data_stream(name="*")
    stream_names = [ds["name"] for ds in data_streams["data_streams"]]

    for stream in stream_names:
        print(f"Rolling over data stream: {stream}")
        try:
            response = es.indices.rollover(alias=stream)
            print(f"✅ Rollover response for '{stream}': {response}")
        except Exception as e:
            print('inner error', e)
except Exception as e:
    print(e)
