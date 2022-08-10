from .models import Task_2
from django.forms import ModelForm
from .models import Comment


class Task_2_Form(ModelForm):
    class Meta:
        model = Task_2
        fields = ["title", "task", "float_field"]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "message"]
