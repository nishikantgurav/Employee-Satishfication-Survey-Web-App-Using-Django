from django import forms

class ResponseForm(forms.Form):
    job = forms.CharField(label='What do you do for work?', max_length=100)
    satisfaction = forms.IntegerField(label='How satisfied are you with your work (0-10)?', min_value=0, max_value=10)
    email = forms.EmailField(label='What is your email address?')
