from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
# from django.http import HttpResponse
import logging
# from .models import Author, Coin, Post
from .forms import ImageForm

logger = logging.getLogger(__name__)


def index(request):
    context = {
        'title': 'Главная'
    }
    logger.info('index get request')
    return render(request, "tasks_2/index.html", context=context)


def about(request):
    context = {
        'title': 'Обо мне'
    }
    logger.info('about get request')
    return render(request, "tasks_2/about.html", context=context)


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'tasks_2/upload_image.html', {'form': form})
