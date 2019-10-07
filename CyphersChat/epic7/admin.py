from django.contrib import admin
from epic7.models import tips, notic
from home.models import projects, project_Img, Kategorie
# Register your models here.
admin.site.register(projects)
admin.site.register(project_Img)
admin.site.register(Kategorie)
admin.site.register(tips)
admin.site.register(notic)