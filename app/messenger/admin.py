from django.contrib import admin

from messenger.models import MMessage


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


@admin.register(MMessage)
class MMessageAdmin(admin.ModelAdmin):
    date_hierarchy = 'sent'
    list_display = ('id', 'sent', 'user_from', 'user_to', 'title', 'body',)
    list_filter = (
        ('user_from__username', custom_titled_filter('• FROM')),
        ('user_to__username', custom_titled_filter('• TO')),
    )
    search_fields = ('title', 'body')
    ordering = ['sent']

