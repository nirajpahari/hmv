from django.contrib import admin
from .models import Billing

# Register your models here.
class BillingAdmin(admin.ModelAdmin):
    model = Billing
    list_display = ('room', 'remaining_amount', 'status')
admin.site.register(Billing, BillingAdmin)
