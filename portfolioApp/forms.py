from django import forms
from portfolioApp.models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    name = forms.CharField(
        min_length=1,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'input-field',
                'id': 'email-field',
                'placeholder': 'Name'
            }),
        label="")

    email = forms.EmailField(
        min_length=1,
        widget=forms.TextInput(
            attrs={
                'class': 'input-field',
                'id': 'email-field',
                'placeholder': 'Email'
            }),
        label="")

    topic = forms.CharField(
        min_length=1,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'input-field',
                'id': 'topic-field',
                'placeholder': 'Topic'
            }),
        label="")

    message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'class': 'input-field',
                'id': 'message-field',
                'placeholder': 'Message',
                'rows': 6, 'cols': 40
            }),
        label="")

    class Meta:
        model = ContactMessage
        fields = ("name", "email", "topic", "message")
