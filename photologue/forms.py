from django import forms

class AjaxRequestForm(forms.Form):
    type = forms.CharField()