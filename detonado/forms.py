from django import forms
from image_cropping import ImageCropWidget

class MyModelForm(forms.ModelForm):
    class Meta:
        widgets = {
            'image': ImageCropWidget,
        }