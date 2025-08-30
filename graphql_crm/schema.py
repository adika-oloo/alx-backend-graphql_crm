import graphene
from .models import Customer, Order


class CustomerType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()


class OrderType(graphene.ObjectType):
    id = graphene.ID()
    product = graphene.String()
    quantity = graphene.Int()


class Query(graphene.ObjectType):
    all_customers = graphene.List(CustomerType)
    all_orders = graphene.List(OrderType)

    def resolve_all_customers(self, info):
        return Customer.objects.all()

    def resolve_all_orders(self, info):
        return Order.objects.all()


class CreateCustomer(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    customer = graphene.Field(CustomerType)

    def mutate(self, info, name, email):
        customer = Customer.objects.create(name=name, email=email)
        return CreateCustomer(customer=customer)


class Mutation(graphene.ObjectType):
    create_customer = CreateCustomer.Field()
