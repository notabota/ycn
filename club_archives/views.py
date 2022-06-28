from django.http import HttpResponseNotFound
from django.shortcuts import render
from os import walk


def index(request, year):
    if year > 2022 or year < 2019:
        return HttpResponseNotFound("Dude")

    images_path = 'static/club_archives/img/activities/' + str(year)

    images_list = list(map(lambda x: f'club_archives/img/activities/{year}/{x}',
                           next(walk(images_path), (None, None, []))[2]))  # [] if no file

    return render(request, 'club_archives/index.html', {'year': year, 'images_list': images_list})
