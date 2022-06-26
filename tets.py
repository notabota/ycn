from django.shortcuts import render
from os import walk

year = 2022

images_path = 'static/tech_archives/img/' + str(year)

files_path = 'static/tech_archives/file/' + str(year)

images_list = list(map(lambda x: f'tech_archives/img/{year}/{x}',
                       next(walk(images_path), (None, None, []))[2]))  # [] if no file

files_list = list(map(lambda x: f'tech_archives/img/{year}/{x}',
                      next(walk(files_path), (None, None, []))[2]))  # [] if no file

researchs_list = []
for i in range(len(images_list)):
    researchs_list.append({
        'images': images_list[i],
        'files': files_list[i]
    })
print(researchs_list)
