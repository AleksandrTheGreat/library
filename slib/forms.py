from django import forms

class search(forms.Form):
    poisk = forms.CharField(label='',max_length=100)