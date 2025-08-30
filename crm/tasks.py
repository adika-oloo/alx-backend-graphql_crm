import datetime
from celery import shared_task
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

@shared_task
def generate_crm_report():
    # GraphQL transport
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql/",
        verify=True,
        retries=3,
    )
    client = Client(transport=transport, fetch_schema_from_transport=True)

    query = gql("""
    query {
        customersCount
        ordersCount
        totalRevenue
    }
    """)

    try:
        response = client.execute(query)

        customers = response.get("customersCount", 0)
        orders = response.get("ordersCount", 0)
        revenue = response.get("totalRevenue", 0)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{timestamp} - Report: {customers} customers, {orders} orders, {revenue} revenue\n"

        with open("/tmp/crm_report_log.txt", "a") as f:
            f.write(log_message)

    except Exception as e:
        with open("/tmp/crm_report_log.txt", "a") as f:
            f.write(f"Error generating report: {str(e)}\n")
