from django  import forms

#from django.db.models import fields

class MyForm(forms.Form):
    fc = forms.CharField(max_length=3)
    tc = forms.CharField(max_length=3)
    fields = [tc ,fc ]