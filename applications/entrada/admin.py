from django.contrib import admin

from .models import Category, Tag, Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title','public','in_home','area_trabajo','in_reciente','marcas','ours')
    search_fields = ('category',)
    list_filter = ('category',)
    ordering = ('area_trabajo',)




admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Entry, EntryAdmin)

