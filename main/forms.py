from .models import Task_2
from django.forms import ModelForm, widgets, TextInput
from .models import Comment


class Task_2_Form(ModelForm):
    class Meta:
        model = Task_2
        fields = ["title", "task", "float_field"]
        widgets = {
            'title': TextInput(attrs={'class':'form-control', "placeholder":"Введите название"}),
            'task': TextInput(attrs={'class':'form-control', "placeholder":"Введите описание"}),
            'float_field': TextInput(attrs={'class':'form-control','placeholder':"Введите рейтинг(0-10, где 10 наивысший)"})
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "message"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', "placeholder": "Enter name"}),
            'message': TextInput(attrs={'class': 'form-control', "placeholder": "Enter message"}),

        }
