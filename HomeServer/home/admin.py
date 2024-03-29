from django.contrib import admin
import home.models as Models

class KategorieAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name','kate']
class ProjectIMGAdmin(admin.ModelAdmin):
    list_display = ['projects_id']
admin.site.register(Models.projects,ProjectsAdmin)
admin.site.register(Models.project_Img,ProjectIMGAdmin)
admin.site.register(Models.Kategorie,KategorieAdmin)

class CareerList(admin.ModelAdmin):
    list_display =['projectName','duration']
class Skill(admin.ModelAdmin):
    list_display = ['skillName']
admin.site.register(Models.show_pro)
admin.site.register(Models.careers, CareerList)

admin.site.register(Models.myInfo)

admin.site.register(Models.skill,Skill )

admin.site.register(Models.usableLanguages)
admin.site.register(Models.history)