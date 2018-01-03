from django  import forms

#from django.db.models import fields

class MyForm(forms.Form):
    fc = forms.CharField(max_length=4)
    tc = forms.CharField(max_length=4)
    fields = [tc ,fc ]