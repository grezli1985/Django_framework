from django.shortcuts import render
import logging
from django.http import HttpResponse, HttpRequest

logger = logging.getLogger(__name__)


def index(request: HttpRequest):
    html = f"""<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="/static/css/bootstrap.min.css">
    <title> Главная </title>
</head>
<body>
    <div class="container-fluid">
        <ul class="nav nav-pills justify-content-end align-items-end">
            <li class="nav-item"><a href="/" class="nav-link">Главная</a></li>
            <li class="nav-item"><a href="/about/" class="nav-link">Обо мне</a></li>
        </ul>

            <h1>первый Django-сайт</h1>

        <div class="row fixed-bottom modal-footer">
            <hr>
            <p>Все права защищены &copy;</p>
        </div>
    </div>
    <script src="{{ url_for('static', filename='js/bootstrap.bundle.min.js') }}"></script>
</body>
</html>
    """
    logger.debug('Index page requested.')

    return HttpResponse(html)


def about(request: HttpRequest):
    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Обо мне </title>
</head>
<body>
    <div class="container-fluid">
        <ul class="nav nav-pills justify-content-end align-items-end">
            <li class="nav-item"><a href="/" class="nav-link">Главная</a></li>
            <li class="nav-item"><a href="/about/" class="nav-link">Обо мне</a></li>
        </ul>
            
            <h1>Обо мне</h1>

        <div class="row fixed-bottom modal-footer">
            <hr>
            <p>Все права защищены &copy;</p>
        </div>
    </div>
    <script src="{{ url_for('static', filename='js/bootstrap.bundle.min.js') }}"></script>
</body>
</html>
    """
    logger.debug('About page requested.')

    return HttpResponse(html)
