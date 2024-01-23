from django.core.management.base import BaseCommand, CommandParser

from tasks_2.models import User, Product, Order


class Command(BaseCommand):
    help = 'Create order'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('User_id', type=int, help='User id')
        parser.add_argument('product_id', type=int, help='Product id')

    def handle(self, *args, **kwargs) -> None:
        User_id = kwargs['User_id']
        product_id = kwargs['product_id']

        user = User.objects.get(id=User_id)
        product = Product.objects.get(id=product_id)

        order = Order(
            user=user,
            product=product,
            order_sum=product.price * product.quantity
        )
        order.save()
        self.stdout.write(self.style.SUCCESS(f'Added new order: {order}'))
