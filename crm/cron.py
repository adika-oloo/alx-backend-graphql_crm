# crm/cron.py
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def order_reminder():
    transport = RequestsHTTPTransport(
        url="http://127.0.0.1:8000/graphql/",  # Adjust if different
        verify=True,
        retries=3,
    )

    client = Client(transport=transport, fetch_schema_from_transport=True)

    query = gql("""
        query {
            hello
        }
    """)

    try:
        result = client.execute(query)
        print("GraphQL response:", result)
    except Exception as e:
        print("Error executing GraphQL query:", e)

