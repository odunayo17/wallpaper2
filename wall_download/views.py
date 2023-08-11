from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os


def index(request):
    return render(request, "wall_download/index.html")


def nature(request):
    return render(request, "wall_download/nature.html")


def flowers(request):
    return render(request, "wall_download/flowers.html")


def abstract(request):
    return render(request, "wall_download/abstract.html")


def animals(request):
    return render(request, "wall_download/animal.html")


def dark(request):
    return render(request, "wall_download/photo.html")


# NATURE PICTURES DOWNLOAD


def nature1(request):
    file = os.path.join(settings.BASE_DIR, "static/img/nature 1.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def nature2(request):
    file = os.path.join(settings.BASE_DIR, "static/img/nature 2.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def nature3(request):
    file = os.path.join(settings.BASE_DIR, "static/img/nature 3.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def nature4(request):
    file = os.path.join(settings.BASE_DIR, "static/img/nature 4.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def nature5(request):
    file = os.path.join(settings.BASE_DIR, "static/img/nature 5.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def nature6(request):
    file = os.path.join(settings.BASE_DIR, "static/img/nature 6.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def download2(request):
    file = os.path.join(settings.BASE_DIR, "static/img/Nature.zip")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


# NATURE PICTURES DOWNLOAD


def abstract1(request):
    file = os.path.join(settings.BASE_DIR, "static/img/abstract 1.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def abstract2(request):
    file = os.path.join(settings.BASE_DIR, "static/img/abstract 2.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def abstract3(request):
    file = os.path.join(settings.BASE_DIR, "static/img/abstract 3.jpeg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def abstract4(request):
    file = os.path.join(settings.BASE_DIR, "static/img/abstract 4.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def abstract5(request):
    file = os.path.join(settings.BASE_DIR, "static/img/abstract 5.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def abstract6(request):
    file = os.path.join(settings.BASE_DIR, "static/img/abstract 6.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def download6(request):
    file = os.path.join(settings.BASE_DIR, "static/img/Abstract.zip")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


# ANIMALS PICTURES DOWNLOAD


def ani1(request):
    file = os.path.join(settings.BASE_DIR, "static/img/ani 1.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def ani2(request):
    file = os.path.join(settings.BASE_DIR, "static/img/ani 2.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def ani3(request):
    file = os.path.join(settings.BASE_DIR, "static/img/ani 3.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def ani4(request):
    file = os.path.join(settings.BASE_DIR, "static/img/ani 4.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def ani5(request):
    file = os.path.join(settings.BASE_DIR, "static/img/ani 5.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def ani6(request):
    file = os.path.join(settings.BASE_DIR, "static/img/ani 6.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def download5(request):
    file = os.path.join(settings.BASE_DIR, "static/img/Animals.zip")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


# FLOWERS PICTURES DOWNLOAD


def flower1(request):
    file = os.path.join(settings.BASE_DIR, "static/img/flower 1.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def flower2(request):
    file = os.path.join(settings.BASE_DIR, "static/img/flower 2.png")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def flower3(request):
    file = os.path.join(settings.BASE_DIR, "static/img/flower 3.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def flower4(request):
    file = os.path.join(settings.BASE_DIR, "static/img/flower 4.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def flower5(request):
    file = os.path.join(settings.BASE_DIR, "static/img/flower 5.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def flower6(request):
    file = os.path.join(settings.BASE_DIR, "static/img/flower 6.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def download4(request):
    file = os.path.join(settings.BASE_DIR, "static/img/Flowers.zip")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


# DARK PICTURES DOWNLOAD


def dark1(request):
    file = os.path.join(settings.BASE_DIR, "static/img/photo 1.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def dark2(request):
    file = os.path.join(settings.BASE_DIR, "static/img/photo 2.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def dark3(request):
    file = os.path.join(settings.BASE_DIR, "static/img/photo 3.jpeg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def dark4(request):
    file = os.path.join(settings.BASE_DIR, "static/img/photo 4.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def dark5(request):
    file = os.path.join(settings.BASE_DIR, "static/img/photo 5.png")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def dark6(request):
    file = os.path.join(settings.BASE_DIR, "static/img/photo 6.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def download3(request):
    file = os.path.join(settings.BASE_DIR, "static/img/Dark.zip")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


# HOME PAGE PICTURES DOWNNLOAD


def download(request):
    file = os.path.join(settings.BASE_DIR, "static/img/cool-wallpapers.zip")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def img1(request):
    file = os.path.join(settings.BASE_DIR, "static/img/img1.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def img2(request):
    file = os.path.join(settings.BASE_DIR, "static/img/img2.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def img3(request):
    file = os.path.join(settings.BASE_DIR, "static/img/img3.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def img4(request):
    file = os.path.join(settings.BASE_DIR, "static/img/img4.png")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def img5(request):
    file = os.path.join(settings.BASE_DIR, "static/img/img5.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def img6(request):
    file = os.path.join(settings.BASE_DIR, "static/img/img6.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def img7(request):
    file = os.path.join(settings.BASE_DIR, "static/img/img7.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def img8(request):
    file = os.path.join(settings.BASE_DIR, "static/img/img8.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def img9(request):
    file = os.path.join(settings.BASE_DIR, "static/img/img9.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def img10(request):
    file = os.path.join(settings.BASE_DIR, "static/img/img10.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def img11(request):
    file = os.path.join(settings.BASE_DIR, "static/img/img11.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)


def img12(request):
    file = os.path.join(settings.BASE_DIR, "static/img/img12.jpg")
    fileopened = open(file, "rb")

    return FileResponse(fileopened)
