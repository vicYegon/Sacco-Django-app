from django.contrib import admin
from decimal import Decimal
from .models import Member


# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "national_id",
        "phone_number",
        "email",
        "date_registered",
    )

    search_fields = (
        "full_name",
        "national_id",
        "email",
    )