from django.contrib import admin

from .models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_opens_at', 'get_closes_at')
    search_fields = ('id', 'name')
    ordering = ('id',)
    list_display_links = list_display

    def get_opens_at(self, obj):
        return obj.opens_at.strftime('%H:%M')
    get_opens_at.short_description = 'Opens At'

    def get_closes_at(self, obj):
        return obj.closes_at.strftime('%H:%M')
    get_closes_at.short_description = 'Closes At'


admin.site.register(Restaurant, RestaurantAdmin)

