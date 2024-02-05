from django.db import models


class Coin(models.Model):
    is_heads = models.BooleanField()
    flip_time = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_coin_stats(number: int) -> dict:
        last_flips = Coin.objects.all()[:number]
        flips_stats = {
            'Орел': [],
            'Решка': []
        }

        for coin in last_flips:
            if coin.is_heads:
                flips_stats['Орел'].append(coin.flip_time)
            else:
                flips_stats['Решка'].append(coin.flip_time)

        return flips_stats

    def __str__(self):
        return f'Coin flip at {self.flip_time}: heads: {self.is_heads}'


class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def get_full_name(self):
        return f'{self.name} {self.last_name}'

    def __str__(self):
        return f'Author: {self.name} {self.last_name}, birthday: {self.birthday}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'Post: {self.title}, Author: {self.author}'
