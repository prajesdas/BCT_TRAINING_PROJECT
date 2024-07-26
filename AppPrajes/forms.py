from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class MyForm(forms.Form):
    name=forms.CharField(label="Prajes Das")
    email=forms.EmailField(label="prajesdas@gmailcom")
    message=forms.CharField(label="Hello This is Prajes Das",widget=forms.Textarea)
    captcha=ReCaptchaField(widget=ReCaptchaV2Checkbox)