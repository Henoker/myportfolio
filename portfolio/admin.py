from django.contrib import admin
from .models import Home, About, Portfolio, Category, Profile, Skills, Blog, Contact

# Register your models here.
admin.site.register(Home)

class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]

# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]


# Portfolio
admin.site.register(Portfolio)

admin.site.register(Blog)


class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "created_at"]
    search_fields = ["name", "email", "subject"]
    list_per_page = 6

admin.site.register(Contact, ContactAdmin)