from google.cloud import bigquery


BASE_URL="https://etherscan.io/name-lookup-search?id="      
PROJECT_ID="token-filters"   
DATASET_ID="etherescan_ens"          
TABLE_ID="ens_wallet_address"    
SCHEMA = [
    bigquery.SchemaField('contract', 'STRING'),
    bigquery.SchemaField('reverse_record', 'RECORD', mode='NULLABLE', fields=[
        bigquery.SchemaField('resolved_address', 'STRING'),
        bigquery.SchemaField('expiration_date', 'STRING'),
        bigquery.SchemaField('registrant', 'STRING'),
        bigquery.SchemaField('parent', 'STRING'),
        bigquery.SchemaField('controller', 'STRING'),
        bigquery.SchemaField('token_id', 'STRING'),
        bigquery.SchemaField('other_addresses', 'STRING', mode='REPEATED'),
        bigquery.SchemaField('content', 'STRING'),
        bigquery.SchemaField('text_records', 'STRING', mode='REPEATED'),
        bigquery.SchemaField('owner', 'STRING'),
        bigquery.SchemaField('single_chain_records', 'STRING', mode='REPEATED'),
        bigquery.SchemaField('multi_chain_records', 'STRING', mode='REPEATED'),
        bigquery.SchemaField('other_records', 'STRING', mode='REPEATED')
    ]),
    bigquery.SchemaField('domain_names', 'RECORD', mode='REPEATED', fields=[
        bigquery.SchemaField('domain_name', 'STRING'),
        bigquery.SchemaField('resolved_address', 'STRING'),
        bigquery.SchemaField('expiration_date', 'STRING'),
        bigquery.SchemaField('registrant', 'STRING'),
        bigquery.SchemaField('parent', 'STRING'),
        bigquery.SchemaField('controller', 'STRING'),
        bigquery.SchemaField('token_id', 'STRING'),
        bigquery.SchemaField('other_addresses', 'STRING', mode='REPEATED'),
        bigquery.SchemaField('content', 'STRING'),
        bigquery.SchemaField('text_records', 'STRING', mode='REPEATED'),
        bigquery.SchemaField('owner', 'STRING'),
        bigquery.SchemaField('single_chain_records', 'STRING', mode='REPEATED'),
        bigquery.SchemaField('multi_chain_records', 'STRING', mode='REPEATED'),
        bigquery.SchemaField('other_records', 'STRING', mode='REPEATED')
    ])
]