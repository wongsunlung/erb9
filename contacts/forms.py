from django import forms
from .models import Contact


class ContactForm (forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['message']
        widgets ={
            "messags" : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Enter Your message here',
                    'rows': 5
                }
            )
        }