from django import forms


class ContactForm(forms.Form):
	full_name = forms.CharField(label="Full name", max_length=255)
	email = forms.EmailField()
	subject = forms.CharField(label="Subject", max_length=255)
	message = forms.CharField(widget=forms.Textarea)
