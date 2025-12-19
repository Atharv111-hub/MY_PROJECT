from django import forms
from .models import ContactSubmission, Subscription, Project, Client

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['full_name', 'email', 'mobile', 'city']

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'image']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'designation', 'description', 'image']