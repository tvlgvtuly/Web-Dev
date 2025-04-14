from django.contrib import admin
from .models import Company, Vacancy
# Register your models here.
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary', 'company')  # Поля, которые отображаются в списке вакансий
    list_filter = ('company',)  # Фильтрация по компании

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address')  # Поля, которые отображаются в списке компаний
    search_fields = ('name', 'city')  # Поиск по имени компании и городу

# Регистрация моделей с дополнительными настройками
admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)