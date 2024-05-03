from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, NumberInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date', 'price']

        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Тип животного'}),
            "anons": TextInput(attrs={'class': 'form-control', 'placeholder': 'Порода животного'}),
            "date": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
            "full_text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Вид работ'}),
            "price": NumberInput(attrs={'class': 'form-control', 'placeholder': 'Стоимость работ'}),
        }