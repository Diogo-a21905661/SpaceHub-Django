from django.forms import ModelForm

from .models import *

# Formulário inspirado na tarefa
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

# Formulário inspirado no quiz
class Quiz(ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'

class Commentary(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'