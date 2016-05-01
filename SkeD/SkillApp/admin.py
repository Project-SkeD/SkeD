from django.contrib import admin
from SkillApp.models import *

class ApplicantAdmin(admin.ModelAdmin):
    pass

class CityAdmin(admin.ModelAdmin):
    pass

class JobRoleAdmin(admin.ModelAdmin):
    pass

class QualificationAdmin(admin.ModelAdmin):
    pass

class ExperienceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Applicant,ApplicantAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(JobRole, JobRoleAdmin)
admin.site.register(Qualification,QualificationAdmin)
admin.site.register(Experience,ExperienceAdmin)