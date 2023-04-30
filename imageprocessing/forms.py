from django.forms import forms
from django.forms import ImageField, IntegerField, BooleanField


class ImageForm(forms.Form):
    image = ImageField(label="Image")
    width = IntegerField(min_value=1, label="Width (in pixels)",required=False)
    height = IntegerField(min_value=1, label="Height (in pixels)", required=False)
    rotate = IntegerField(min_value=0, max_value=360, label="Rotate (in degrees)", required=False)
    mirror_horizontally = BooleanField(required=False, label="Flip horizontally", initial=False)
    mirror_vertically = BooleanField(required=False, label="Flip vertically", initial=False)
    top = IntegerField(min_value=0, label="Top coordinate (in pixels)", required=False)
    left = IntegerField(min_value=0, label="Left coordinate (in pixels)", required=False)
    bottom = IntegerField(min_value=0, label="Bottom coordinate (in pixels)", required=False)
    right = IntegerField(min_value=0, label="Right coordinate (in pixels)", required=False)