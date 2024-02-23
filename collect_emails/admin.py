import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Supporter

def export_supporters_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="supporters.csv"'

    writer = csv.writer(response)
    fields = ['name', 'email', 'phone_number']  # Define the fields you want to export
    writer.writerow(fields)

    for supporter in queryset:
        writer.writerow([getattr(supporter, field) for field in fields])

    return response

export_supporters_as_csv.short_description = "Export selected supporters as CSV"

class SupporterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')  # Optionally, define how supporter records are displayed in the admin list
    actions = [export_supporters_as_csv]  # Add the custom admin action for exporting supporters as CSV

admin.site.register(Supporter, SupporterAdmin)
