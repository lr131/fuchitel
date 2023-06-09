# Generated by Django 4.1.3 on 2022-11-20 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Districts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Район",
                "verbose_name_plural": "Районы",
                "db_table": "district",
            },
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Образование",
                "verbose_name_plural": "Виды образования",
                "db_table": "education",
            },
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("answer", models.BooleanField(verbose_name="Ответ")),
                ("description", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "График работы",
                "verbose_name_plural": "Виды графика работы",
                "db_table": "schedule",
            },
        ),
        migrations.CreateModel(
            name="Applicant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("questionnaire_num", models.IntegerField(verbose_name="Номер анкеты")),
                ("family", models.CharField(max_length=100, verbose_name="Фамилия")),
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                (
                    "patr",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Отчество"
                    ),
                ),
                ("note", models.TextField(null=True, verbose_name="Примечания")),
                (
                    "black_list",
                    models.BooleanField(default=False, verbose_name="Черный список"),
                ),
                (
                    "position",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Соискатель на место",
                    ),
                ),
                (
                    "registration",
                    models.CharField(
                        blank=True, max_length=2000, null=True, verbose_name="Прописка"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        max_length=2000,
                        null=True,
                        verbose_name="Фактический адрес",
                    ),
                ),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                ("bdate", models.DateField(blank=True, null=True)),
                (
                    "education_descr",
                    models.TextField(blank=True, null=True, verbose_name="Образование"),
                ),
                (
                    "experience",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Общ. Пед/мед. стаж",
                    ),
                ),
                (
                    "work_activity",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Трудовая деят/время",
                    ),
                ),
                (
                    "child_age",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Возраст детей, наиболее симпатичный для работы",
                    ),
                ),
                (
                    "marital_status",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Семейное положение",
                    ),
                ),
                (
                    "international_passport",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Загранпаспорт"
                    ),
                ),
                (
                    "driver_license",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Водительские права"
                    ),
                ),
                (
                    "hobby",
                    models.TextField(
                        blank=True, null=True, verbose_name="Хобби, увлечения"
                    ),
                ),
                (
                    "nationality",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Национальность",
                    ),
                ),
                (
                    "religion",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Вероисповедание",
                    ),
                ),
                (
                    "addictions",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Вредные привычки",
                    ),
                ),
                (
                    "doc_type",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "паспорт"),
                            (1, "загран. паспорт"),
                            (2, "удостоверение личности (военный, мвд, моряк)"),
                            (3, "свидетельство о рождении"),
                            (4, "справка об освобождении"),
                            (5, "военный билет"),
                        ],
                        default=0,
                        null=True,
                        verbose_name="Вид документа",
                    ),
                ),
                (
                    "doc_ser",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Серия"
                    ),
                ),
                (
                    "doc_num",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Номер"
                    ),
                ),
                (
                    "doc_by",
                    models.CharField(
                        blank=True, max_length=80, null=True, verbose_name="Кем выдан"
                    ),
                ),
                (
                    "minimum_wage",
                    models.IntegerField(
                        default=0, verbose_name="Минимальный уровень зарплаты"
                    ),
                ),
                (
                    "cdate",
                    models.DateField(
                        auto_now_add=True, null=True, verbose_name="Дата заполнения"
                    ),
                ),
                (
                    "district",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="polls.districts",
                        verbose_name="Район проживания",
                    ),
                ),
                (
                    "education",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="polls.education",
                        verbose_name="Вид образования",
                    ),
                ),
                (
                    "schedule",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="polls.schedule",
                        verbose_name="Желаемый график работы",
                    ),
                ),
            ],
            options={
                "verbose_name": "Соискатель",
                "verbose_name_plural": "Соискатели",
                "db_table": "applicant",
            },
        ),
    ]
