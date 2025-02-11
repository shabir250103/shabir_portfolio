

# Register your models here.
from django.contrib import admin
from .models import Projects, ProjectImage,Contact

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Projects, ProjectsAdmin)



admin.site.register(Contact)
