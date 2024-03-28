from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'date']


        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Form name"
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Anons"
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',  
                'placeholder': 'Publication date'  
            }),  
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Article text"
            }),
        }
            

        