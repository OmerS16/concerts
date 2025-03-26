from main import scrape
from aws_upload import upload_to_rds

def lambda_handler(event, context):
    events = scrape()
    
    if not events.empty:
        upload_to_rds(events, table_name='events')
    
    result = events.to_json(orient='records', date_format='iso', default_handler=str, force_ascii=False)
    return {
        'statusCode': 200,
        'body': result
    }

results = lambda_handler('hello', 'hello')