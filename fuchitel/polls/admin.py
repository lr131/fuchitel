from django.contrib import admin

from .models import Applicant, Education, Districts, Schedule

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('get_fio', 'get_age', 'is_black', 'phone', 
                    'position', 'get_education', 
                    'get_experience', 'get_work', 
                    'get_about', 'get_docs')
    # list_display = ('get_fio', )
    ordering = ['id', 'family', 'name',]
    search_fields = ('family','name', 'questionnaire_num', 'id',
                     'district', 'age', 'phone', 'education',
                     'nationality', 'religion', 'minimum_wage',
                     'cdate')

admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Education)
admin.site.register(Districts)
admin.site.register(Schedule)