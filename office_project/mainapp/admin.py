from django.contrib import admin
from .models import Project, Client, ContactSubmission, Subscription

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'created_at')
    search_fields = ('name', 'designation')

@admin.register(ContactSubmission)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile', 'city', 'submitted_at')
    readonly_fields = ('submitted_at',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    readonly_fields = ('subscribed_at',)