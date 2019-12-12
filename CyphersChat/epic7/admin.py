from django.contrib import admin
import epic7.models as Models
# Register your models here.

#admin.site.register(tips)
class TipsTable(admin.ModelAdmin):
    list_display = ['writer','name','important']
admin.site.register(Models.tips,TipsTable)
class NoticTable(admin.ModelAdmin):
    list_display = ['writer','name','important']
admin.site.register(Models.notic,NoticTable)
