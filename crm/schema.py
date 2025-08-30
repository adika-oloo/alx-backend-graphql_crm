import graphene
from graphene_django import DjangoObjectType
from crm.models import Product   # assuming you have a Product model


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "stock")


class UpdateLowStockProducts(graphene.Mutation):
    class Arguments:
        # no external args, it operates internally
        pass

    success = graphene.Boolean()
    message = graphene.String()
    updated_products = graphene.List(ProductType)

    @classmethod
    def mutate(cls, root, info):
        low_stock_products = Product.objects.filter(stock__lt=10)

        updated = []
        for product in low_stock_products:
            product.stock += 10  # simulate restocking
            product.save()
            updated.append(product)

        if updated:
            return UpdateLowStockProducts(
                success=True,
                message="Low-stock products restocked successfully.",
                updated_products=updated,
            )
        else:
            return UpdateLowStockProducts(
                success=True,
                message="No products required restocking.",
                updated_products=[],
            )


class Mutation(graphene.ObjectType):
    update_low_stock_products = UpdateLowStockProducts.Field()


schema = graphene.Schema(mutation=Mutation)

