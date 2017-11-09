# maxins must come first
from cms.admin.placeholderadmin import FrontendEditableAdminMixin
from django.contrib import admin
from .models import *

class AppAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'icon', 'privacy', 'tutorial', 'url', 'testimonial', 'is_avaiable' )
    ordering = ('id',)

admin.site.register(App, AppAdmin)

admin.site.register(AppType)
admin.site.register(AppFormat)
admin.site.register(AppFunction)
admin.site.register(AppPrice)
admin.site.register(AppSupport)
