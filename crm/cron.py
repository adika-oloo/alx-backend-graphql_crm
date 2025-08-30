from datetime import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


def update_low_stock():
    """Executes GraphQL mutation to update low-stock products and logs results"""
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql/",
        verify=False,
        retries=3,
    )

    client = Client(transport=transport, fetch_schema_from_transport=True)

    mutation = gql("""
        mutation {
            updateLowStockProducts {
                success
                message
                updatedProducts {
                    id
                    name
                    stock
                }
            }
        }
    """)

    log_file = "/tmp/low_stock_updates_log.txt"

    try:
        response = client.execute(mutation)
        with open(log_file, "a") as f:
            f.write(f"\n[{datetime.now()}] Mutation Response:\n")
            f.write(str(response) + "\n")
    except Exception as e:
        with open(log_file, "a") as f:
            f.write(f"\n[{datetime.now()}] Mutation failed: {e}\n")




