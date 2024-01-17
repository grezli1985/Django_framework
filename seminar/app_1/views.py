from django.shortcuts import render
from django.http import HttpResponse
import logging
from random import randint, choice
from .models import Author, Coin, Post

logger = logging.getLogger(__name__)


def index(request):
    logger.info('index get request')
    return HttpResponse("Hello, world!")


def coin_flip(request):
    coin_sides = [True, False]
    coin_sides_str = ['Tails', 'Heads']
    side = choice(coin_sides)
    coin = Coin(is_heads=side)
    coin.save()

    logger.info(f'Coin flipped at side: {coin_sides_str[side]}')
    return HttpResponse(f'<p>Coin side: {coin_sides_str[side]}</p>')


def coin_stat(request):
    coin_flips = Coin.get_coin_stats(5)
    return HttpResponse(str(coin_flips))


def dice_roll(request):
    dice_side = randint(1, 6)

    logger.info(f'Dice side: {dice_side}')
    return HttpResponse(f'<p>Dice side: {dice_side}</p>')


def random_number(request):
    rand_number = randint(0, 100)

    logger.info(f'Random number from 0 to 100: {rand_number}')
    return HttpResponse(f'<p>Random number from 0 to 100: {rand_number}</p>')


def random_view(request):
    coin_sides = ['Heads', 'Tails']
    dice_side = randint(1, 6)
    rand_number = randint(0, 100)
    logger.info(f'Dice side: {dice_side}')
    logger.info(f'Random number from 0 to 100: {rand_number}')

    return HttpResponse(
        f'<p>Coin side: {choice(coin_sides)}</p><br>\
        <p>Dice side: {dice_side}</p><br><p>Random number from 0 to 100: {rand_number}</p>'
    )


def authors_view(request):
    authors = Author.objects.all()

    res_str = '<br>'.join([str(author) for author in authors])

    return HttpResponse(res_str)


def posts_view(request):
    posts = Post.objects.all()

    res_str = '<br>'.join([str(post) for post in posts])

    return HttpResponse(res_str)
