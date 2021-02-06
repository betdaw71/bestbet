from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User as UserO


# Unregister the provided model admin

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'location',
                ),
            },
        ),
    )

admin.site.register(User)
