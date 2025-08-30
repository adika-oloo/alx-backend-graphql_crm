from datetime import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


def log_crm_heartbeat():
    """Logs a heartbeat timestamp to /tmp/crm_heartbeat_log.txt and queries GraphQL hello field"""
    # Log heartbeat
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"CRM heartbeat at {datetime.now()}\n")

    # GraphQL transport (adjust URL if your endpoint differs)
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql/",
        verify=False,
        retries=3,
    )

    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Simple query to test hello field
    query = gql("""
        query {
            hello
        }
    """)

    try:
        response = client.execute(query)
        with open("/tmp/crm_heartbeat_log.txt", "a") as f:
            f.write(f"GraphQL hello response: {response}\n")
    except Exception as e:
        with open("/tmp/crm_heartbeat_log.txt", "a") as f:
            f.write(f"GraphQL hello query failed: {e}\n")



