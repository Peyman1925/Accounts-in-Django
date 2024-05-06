from django import forms
# from .models import Choice

# class QuestionForm(forms.Form):
#     choice = forms.ModelChoiceField(queryset=Choice.objects.all(), widget=forms.RadioSelect)
from .models import *

# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ['question_text', 'correct_answer']