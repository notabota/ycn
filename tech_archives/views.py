from django.shortcuts import render
from os import walk
import json


def index(request, year):
    with open('static/tech_archives/content/' + str(year) + '/content.json', 'r', encoding='utf-8') as content_file:
        content = json.loads(content_file.read())
        for i in range(len(content)):
            print(content[i])
            content[i]["file"] = f'tech_archives/file/{str(year)}/{content[i]["file"]}'
            content[i]["img"] = f'tech_archives/img/{str(year)}/{content[i]["img"]}'

    print(content)

    # print(content)

    return render(request, 'tech_archives/index.html',
                  {'year': year, 'researchs_list': content})
