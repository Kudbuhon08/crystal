from django.contrib import admin
from apps.base.models import Setting, Giv, Questions, Сonfigurations, СonfigurationsImage
# Register your models here.

admin.site.register(Setting)
admin.site.register(Giv)
admin.site.register(Questions)

class СonfigurationsInline(admin.TabularInline):
    model = Сonfigurations
    extra = 1

class СonfigurationsImageAdmin(admin.ModelAdmin):
    list_display = ('id', )
    inlines = [СonfigurationsInline]

admin.site.register(СonfigurationsImage, СonfigurationsImageAdmin)