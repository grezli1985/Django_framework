from django.shortcuts import render
from django.http import HttpResponse
import logging
from random import randint, choice
from .models import Author, Coin, Post
from .forms import GameTypeForm, AuthorAddForm, PostAddFormWidget

logger = logging.getLogger(__name__)


def index1(request):
    logger.info('index get request')
    return HttpResponse("Hello, world!")


def index(request):
    context = {
        'title': 'Главная'
    }
    logger.info('index get request')
    return render(request, "app_1/index.html", context=context)


def about(request):
    context = {
        'title': 'Обо мне',
        'name': 'grezli'
    }
    logger.info('about get request')
    return render(request, "app_1/about.html", context=context)


def coin_flip(request, count):
    result = []
    for i in range(count):
        result.append(choice(['Решка', 'Орел']))
    context = {
        'title': 'Орел или решка',
        'result': result
    }
    logger.info(f'Coin flipped at side: {result}')
    return render(request, 'app_1/game.html', context=context)


# def coin_flip(request):
#     coin_sides = [True, False]
#     coin_sides_str = ['Решка', 'Орел']
#     side = choice(coin_sides)
#     coin = Coin(is_heads=side)
#     coin.save()
#
#     logger.info(f'Coin flipped at side: {coin_sides_str[side]}')
#     return HttpResponse(f'<p>Coin side: {coin_sides_str[side]}</p>')


def coin_stat(request):
    coin_flips = Coin.get_coin_stats(5)
    return HttpResponse(str(coin_flips))


def cube(request, count):
    result = []
    for i in range(count):
        result.append(randint(1, 6))
    context = {
        'title': 'кубик',
        'result': result
    }
    logger.info(f'Сторона кубика: {result}')
    return render(request, 'app_1/game.html', context=context)


# def dice_roll(request):
#     dice_side = randint(1, 6)
#
#     logger.info(f'Dice side: {dice_side}')
#     return HttpResponse(f'<p>Dice side: {dice_side}</p>')


def digit(request, count):
    result = []
    for i in range(count):
        result.append(randint(0, 100))
    context = {
        'title': 'генерировать случайное число',
        'result': result
    }
    logger.info(f'Сторона кубика: {result}')
    return render(request, 'app_1/game.html', context=context)


# def random_number(request):
#     rand_number = randint(0, 100)
#
#     logger.info(f'Random number from 0 to 100: {rand_number}')
#     return HttpResponse(f'<p>Random number from 0 to 100: {rand_number}</p>')


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


def authors_post(request, author_id):
    author = Author.objects.get(id=author_id)
    posts = Post.objects.filter(author=author)

    context = {'author': author, 'posts': posts}
    logger.info(f'Автор: {author} - Посты: {posts}')
    return render(request, 'app_1/author_post.html', context=context)


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'app_1/post.html', context=context)


def authors_view(request):
    authors = Author.objects.all()

    res_str = '<br>'.join([str(author) for author in authors])

    return HttpResponse(res_str)


def posts_view(request):
    posts = Post.objects.all()

    res_str = '<br>'.join([str(post) for post in posts])

    return HttpResponse(res_str)


# Доработаем задачу 1. Создайте представление, которое выводит форму выбора.
# В зависимости от переданных значений представление вызывает одно из трёх представлений,
# созданных на прошлом семинаре (если данные прошли проверку, конечно же).

def choose_game(request):
    if request.method == 'POST':
        form = GameTypeForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['game_type']
            throws_number = form.cleaned_data['throws_number']
            logger.info(f'Получили {game_type=}, {throws_number=}.')
            if game_type == 'C':
                return coin_flip(request, throws_number)
            elif game_type == 'D':
                return cube(request, throws_number)
            else:
                return digit(request, throws_number)
    else:
        form = GameTypeForm()
    return render(request, 'app_1/games.html', {'form': form})


def author_add(request):
    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            birthday = form.cleaned_data['birthday']
            logger.info(f'Получили {name=}, {last_name=}, {email=}, {bio=}, {birthday=}')
            author = Author(name=name,
                            last_name=last_name,
                            email=email,
                            bio=bio,
                            birthday=birthday)
            author.save()
            message = 'Пользователь сохранен'
    else:
        form = AuthorAddForm()
        message = 'Заполните форму'
    return render(request, 'app_1/author_form.html', {'form': form, 'message': message})


def post_add(request):
    if request.method == 'POST':
        form = PostAddFormWidget(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            publish_date = form.cleaned_data['publish_date']
            author = form.cleaned_data['author']
            is_published = form.cleaned_data['is_published']
            logger.info(f'Получили {title=}, '
                        f'{content=}, '
                        f'{publish_date=}, '
                        f'{author=}, '
                        f'{is_published=}')
            post = Post(title=title,
                        content=content,
                        publish_date=publish_date,
                        author=author,
                        is_published=is_published)
            post.save()
            message = 'Статья сохранена'
    else:
        form = PostAddFormWidget()
        message = 'Заполните форму'
    return render(request, 'app_1/post_form.html', {'form': form, 'message': message})
