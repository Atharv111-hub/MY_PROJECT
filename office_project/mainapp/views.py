from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Project, Client
from .forms import ContactForm, SubscriptionForm
from django.http import JsonResponse

def landing(request):
    projects = Project.objects.all().order_by('-created_at')
    clients = Client.objects.all().order_by('-created_at')
    contact_form = ContactForm()
    subscribe_form = SubscriptionForm()
    return render(request, 'mainapp/landing.html', {
        'projects': projects,
        'clients': clients,
        'contact_form': contact_form,
        'subscribe_form': subscribe_form,
    })

from django.views.decorators.http import require_POST

@require_POST
def submit_contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@require_POST
def subscribe(request):
    form = SubscriptionForm(request.POST)
    if form.is_valid():
        try:
            form.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Email already subscribed'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)