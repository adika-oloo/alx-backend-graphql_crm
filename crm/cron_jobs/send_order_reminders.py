#!/usr/bin/env python3
import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

LOG_FILE = "/tmp/order_reminders_log.txt"

def main():
    # Define transport (GraphQL endpoint)
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql",
        verify=True,
        retries=3,
    )

    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Define query: orders within last 7 days
    query = gql("""
        query GetRecentOrders($cutoff: DateTime!) {
            orders(filter: {orderDate_Gte: $cutoff}) {
                id
                customer {
                    email
                }
            }
        }
    """)

    # Calculate cutoff (7 days ago)
    cutoff_date = (datetime.datetime.now() - datetime.timedelta(days=7)).isoformat()

    # Execute query
    result = client.execute(query, variable_values={"cutoff": cutoff_date})
    orders = result.get("orders", [])

    # Log each order
    with open(LOG_FILE, "a") as f:
        for order in orders:
            order_id = order["id"]
            customer_email = order["customer"]["email"]
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - Order {order_id}, Customer: {customer_email}\n")

    print("Order reminders processed!")

if __name__ == "__main__":
    main()
