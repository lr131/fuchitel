from django.db import models
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import const

class Education(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Виды образования'
        db_table = 'education'
        
    def __str__(self):
        return f"{self.name}"
    
class Schedule(models.Model):
    """График работы"""
    answer = models.BooleanField(verbose_name='Ответ')
    description = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'Виды графика работы'
        db_table = 'schedule'
        
    def __str__(self):
        return f"{self.description}"
    
class Districts(models.Model):
    """Районы города"""
    name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'
        db_table = 'district'
        
    def __str__(self):
        return f"{self.name}" 
    
class Applicant(models.Model):
    """Соискатель"""
    questionnaire_num = models.IntegerField(verbose_name="Номер анкеты",
                                            null=True, blank=True)
    family = models.CharField(max_length=100, verbose_name="Фамилия", null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Имя", null=True, blank=True)
    patr = models.CharField(max_length=100, verbose_name="Отчество",
                                 null=True, blank=True)
    note = models.TextField(verbose_name="Примечания", null=True,  blank=True)
    black_list = models.BooleanField(default=False, verbose_name="Черный список")
    position = models.CharField(max_length=200, verbose_name="Соискатель на место",
                                 null=True, blank=True)
    registration = models.CharField(max_length=2000, verbose_name="Прописка",
                                 null=True, blank=True)
    address = models.CharField(max_length=2000, verbose_name="Фактический адрес",
                                 null=True, blank=True)
    district = models.ForeignKey(Districts, on_delete = models.SET_NULL, 
                                 verbose_name="Район проживания",
                                 null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Телефон")
    bdate = models.DateField(null=True, blank=True, verbose_name="Дата рождения",)
    education = models.ForeignKey(Education, verbose_name="Вид образования",
                                  on_delete=models.SET_NULL, 
                                  null=True, blank=True)
    education_descr = models.TextField(verbose_name="Образование",
                                 null=True, blank=True)
    experience = models.CharField(max_length=100, verbose_name="Общий пед./мед. стаж",
                                 null=True, blank=True)
    work_activity = models.CharField(max_length=100, verbose_name="Трудовая деят/время",
                                 null=True, blank=True)
    work_experience = models.CharField(max_length=100, verbose_name="Опыт работы в семьях",
                                 null=True, blank=True)
    child_age = models.CharField(max_length=100, verbose_name="Возраст детей, наиболее симпатичный для работы",
                                 null=True, blank=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL,
                                 verbose_name="Желаемый график работы",
                                 null=True, blank=True)
    marital_status = models.CharField(max_length=100, verbose_name="Семейное положение",
                                      null=True, blank=True)

    international_passport = models.BooleanField(null=True, blank=True, verbose_name="Загранпаспорт")
    driver_license = models.BooleanField(null=True, blank=True, verbose_name="Водительские права")
    hobby = models.TextField(verbose_name="Хобби, увлечения", null=True, blank=True)
    nationality = models.CharField(max_length=100, verbose_name="Национальность", null=True, blank=True)
    religion = models.CharField(max_length=100, verbose_name="Вероисповедание", null=True, blank=True)
    addictions = models.CharField(max_length=50, verbose_name="Вредные привычки", null=True, blank=True)
    doc_type = models.IntegerField(default=0, choices=const.DOC_TYPE_CHOICES,
                               verbose_name="Вид документа",
                                 null=True, blank=True)
    doc_ser = models.CharField(max_length=20, verbose_name="Серия",
                                 null=True, blank=True)
    doc_num = models.CharField(max_length=20, verbose_name="Номер",
                                 null=True, blank=True)
    doc_date = models.DateField(verbose_name="Дата выдачи", null=True,  blank=True)
    doc_by = models.CharField(max_length=80, verbose_name="Кем выдан",
                                 null=True, blank=True)
    minimum_wage = models.IntegerField(default=0, verbose_name="Мин. уровень зарплаты")
    cdate = models.DateField(verbose_name="Дата заполнения", null=True, auto_now_add=True)
    image = models.ImageField(upload_to='applicants', blank=True, null=True, verbose_name='Фото')
    
    @admin.display(description='ФИО')
    def get_fio(self):
        return ' '.join((f"{self.family} " if self.family else "",
                f"{self.name} " if self.name else "",
                f"{self.patr}" if self.patr else ""))
        
    @property
    def fio(self):
        return (' '.join((f"{self.family} " if self.family else "",
                f"{self.name} " if self.name else "",
                f"{self.patr}" if self.patr else "")))
    
    @admin.display(description='Черный список')
    def is_black(self):
        return "ДА" if self.black_list else ""
    
    @admin.display(description='Возраст')
    def get_age(self):
        return f"{self.age} ({self.bdate})"
    
    @admin.display(description='Адрес')
    def get_addresses(self):
        return (f"Прописка: {self.registration}\n"
                f"Факт.адрес: {self.address}\n"
                f"Район: {self.district}\n")
        
    @admin.display(description='Адрес')
    def get_docs(self):
        return (f"Документ: {self.registration}\n"
                f"Серия: {self.doc_ser}\n"
                f"Номер: {self.doc_num}\n"
                f"Дата выдачи: {self.doc_date}\n"
                f"Выдан: {self.doc_by}\n"
                f"Загранпаспорт: {self.international_passport}"
                f"Водительские права: {self.driver_license}\n")
        
    @admin.display(description='Образование')
    def get_education(self):
        return (f"Вид образования: {self.education}\n"
                f"Образование: {self.education_descr}\n")
        
    @admin.display(description='Опыт')
    def get_experience(self):
        return (f"Общий пед/мед стаж: {self.experience}\n"
                f"Трудовая деятельность/время: {self.work_activity}\n"
                f"Опыт работы в семьях: {self.work_experience}\n")   
        
    @admin.display(description='Пожелания к работе')
    def get_work(self):
        return (f"Возраст детей, наиболее симпат/для работы: {self.child_age}\n"
                f"Желаемый график работы: {self.schedule}\n"
                f"Минимальная з/п: {self.minimum_wage}\n")
        
    @admin.display(description='О себе')
    def get_about(self):
        return (f"Семейное положение: {self.marital_status}\n"
                f"Национальность: {self.nationality}\n"
                f"Вероисповедание: {self.religion}\n"
                f"Хобби, увлечения: {self.hobby}\n"
                f"Вредные привычки: {self.addictions}\n")      
    
        
    @property
    def age(self):
        if self.bdate:
            from datetime import datetime, date
            now = datetime.now().date()
            full = now.year - self.bdate.year
            bdate_now = date(now.year, self.bdate.month, self.bdate.day)
            
            if bdate_now > now:
                return full - 1
            else:
                return full        
             
        return None
    
    def get_doc_model(self):
        
        if self.international_passport is not None:
            international_passport = "Да" if self.international_passport else "Нет"
        else:
            international_passport = "Не указано"
            
        if self.driver_license is not None:
            driver_license = "Да" if self.driver_license else "Нет"
        else:
            driver_license = "Не указано"
        
        return {
            "Фактический адрес": f"{self.address}" if self.address else "Не указан",
            "Образование": '\n'.join((f"{self.education.name}\n" if self.education else "", 
                                     f"{self.education_descr}" if self.education_descr else "Не указано")),
            "Опыт работы": f"{self.work_experience}" if self.work_experience else "Не указан",
            "Соискатель на место": f"{self.position}" if self.position else "Няня",
            "Семейное положение": f"{self.marital_status}" if self.marital_status else "Не указано",
            "Желаемый график работы": f"{self.schedule.description}" if self.schedule else "Не указан",
            "Загран.паспорт": international_passport,
            "Водительские права": driver_license,
            "Вредные привычки": f"{self.addictions}" if self.addictions else "Не указаны",
            "Доп.сведения":
                '\n\n'.join(
                    tuple(
                        map(
                            lambda x: ': '.join(x), 
                            {
                                "Хобби, увлечения": f"{self.hobby}" if self.hobby else "Не указано",
                                "Национальность": f"{self.nationality}" if self.nationality else "Не указана"
                            }.items())
                    )
                )
        }
    
    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатели'
        db_table = 'applicant'
        
    def __str__(self):
        return (f"{self.family} " if self.family else "" 
                f"{self.name} " if self.name else "" 
                f"{self.patr}" if self.patr else "")

    
@receiver(post_save, sender=Applicant)
def create_questionnaire_num(sender, instance, created, **kwargs):
    if created:
        questionnaire_num = instance.pk + const.DIFF
        instance.questionnaire_num = questionnaire_num
        instance.save()
