from django.core.validators import RegexValidator
from django.db import models

'''
Поля модели "Клиент":
○ имя клиента
○ электронная почта клиента
○ номер телефона клиента
○ адрес клиента
○ дата регистрации клиента
'''
for_phone_number_validation = \
    RegexValidator(
        regex=r"^[0-9]{3,11}$",
        message="Номер телефона должен быть в длину от 3 до 11 символов и состоять только из цифр.")


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(validators=[for_phone_number_validation], max_length=11)
    address = models.CharField(max_length=200)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, ' \
               f'email: {self.email}, ' \
               f'registration_date: {self.registration_date}'


'''
Поля модели "Товар":
○ название товара
○ описание товара
○ цена товара
○ количество товара
○ дата добавления товара
'''


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=3)
    quantity = models.IntegerField()

    def __str__(self):
        return f'title: {self.title}, ' \
               f'price: {self.price}, ' \
               f'quantity: {self.quantity}'


'''
Поля модели "Заказ":
○ связь с моделью "Клиент", указывает на клиента, сделавшего заказ
○ связь с моделью "Товар", указывает на товары, входящие в заказ
○ общая сумма заказа
○ дата оформления заказа 
'''


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.customer.name} ' \
               f'ordered {self.product} = {self.total_price}, ' \
               f'order date: {self.date_ordered}'
