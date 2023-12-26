from django import forms
from .models import Todo

class FormTodo(forms.Form):
    task = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'myclass'}))
    date = forms.DateField(widget=forms.DateInput())
    status = forms.BooleanField(required=False)

class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['id', 'task', 'date', 'status']

class TodoUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'status']