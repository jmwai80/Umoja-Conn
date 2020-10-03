
from django import forms
from .models import Gallery, GalleryImage


class ImageForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ["image","eventName", "eventDate"]

class ImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ["images"]
