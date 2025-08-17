import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Customer, Product, Order
from .filters import CustomerFilter, ProductFilter, OrderFilter

# Types
class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        filterset_class = CustomerFilter

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        filterset_class = ProductFilter

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        filterset_class = OrderFilter

# Query with filters
class Query(graphene.ObjectType):
    all_customers = DjangoFilterConnectionField(CustomerType)
    all_products = DjangoFilterConnectionField(ProductType)
    all_orders = DjangoFilterConnectionField(OrderType)

    hello = graphene.String(default_value="Hello, GraphQL!")

    def resolve_all_customers(root, info, **kwargs):
        return Customer.objects.all()

    def resolve_all_products(root, info, **kwargs):
        return Product.objects.all()

    def resolve_all_orders(root, info, **kwargs):
        return Order.objects.all()
