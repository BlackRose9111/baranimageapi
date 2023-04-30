from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse, HttpRequest, FileResponse
from django.shortcuts import render
from . import forms, imageprocessor
from django.conf import settings

# Create your views here.

def index(request : HttpRequest):
    import os



    form = forms.ImageForm(request.POST, request.FILES)
    if form.is_valid():
        image = form.cleaned_data['image']
        print(type(image))
        #check if the user entered any rotate degrees
        if form.cleaned_data['rotate']:
            image = imageprocessor.rotate(image, form.cleaned_data['rotate'])
        #check if the user ticked the mirror checkbox
        print(form.cleaned_data['mirror_horizontally'])
        if form.cleaned_data['mirror_horizontally']:
            image = imageprocessor.mirror(image)
        if form.cleaned_data['mirror_vertically']:
            image = imageprocessor.mirror_v(image)
        #check if the user entered any resize dimensions, if they left one blank, it will be the same as the original image
        if form.cleaned_data['width'] and form.cleaned_data['height']:
            width = form.cleaned_data['width']
            if width is None:
                width = image.width
            height = form.cleaned_data['height']
            if height is None:
                height = image.height
            image = imageprocessor.resize(image, width, height)
        #check if the user entered any crop coordinates, if they left one blank, it will be the same as the original image
        if form.cleaned_data['top'] and form.cleaned_data['left'] and form.cleaned_data['bottom'] and form.cleaned_data['right']:
            top = form.cleaned_data['top']
            if top is None:
                top = 0
            left = form.cleaned_data['left']
            if left is None:
                left = 0
            bottom = form.cleaned_data['bottom']
            if bottom is None:
                bottom = image.height
            right = form.cleaned_data['right']
            if right is None:
                right = image.width
            image = imageprocessor.crop(image, top, left, bottom, right)


        return FileResponse(image, as_attachment=True, filename="image.png")


    context = {"form": form}
    return render(request, "imageprocessing/index.html", context)