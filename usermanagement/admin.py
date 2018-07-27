from django.contrib import admin

from usermanagement.models import Company, UserProfile


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
