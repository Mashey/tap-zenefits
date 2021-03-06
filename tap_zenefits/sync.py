import singer
from singer import Transformer, metadata
from .client import ZenefitsClient
from .streams import STREAMS

LOGGER = singer.get_logger()

def sync(config, state, catalog):
    client = ZenefitsClient(config['token'])
    company_id = config['company_id']

    with Transformer() as transformer:
        for stream in catalog.get_selected_streams(state):
            tap_stream_id   = stream.tap_stream_id
            stream_obj      = STREAMS[tap_stream_id](client, state)
            replication_key = stream_obj.replication_key
            stream_schema   = stream.schema.to_dict()
            stream_metadata = metadata.to_map(stream.metadata)

            LOGGER.info('Staring sync for stream: %s', tap_stream_id)

            state = singer.set_currently_syncing(state, tap_stream_id)
            singer.write_state(state)

            singer.write_schema(
                tap_stream_id,
                stream_schema,
                stream_obj.key_properties,
                stream.replication_key
            )

            for record in stream_obj.sync(company_id=company_id):
                transformed_record = transformer.transform(record, stream_schema, stream_metadata)
                LOGGER.info(f"Writing record: {transformed_record}")
                singer.write_record(
                    tap_stream_id,
                    transformed_record,
                )
            state = singer.clear_bookmark(state, tap_stream_id, 'cursor')
            singer.write_state(state)

    state = singer.set_currently_syncing(state, None)
    singer.write_state(state)