from django import forms
from todoapp.models import Task
app_name = 'todoapp'

class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =['name','priority','date']


