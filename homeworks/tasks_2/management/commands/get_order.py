from django.core.management.base import BaseCommand

from tasks_2.models import Order


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Orders data:'))
        orders = Order.objects.all()

        for order in orders:
            self.stdout.write(f'{self.style.ERROR(order.pk)}: {order}')
