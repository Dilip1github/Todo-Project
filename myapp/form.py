from django import forms

class student_registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
