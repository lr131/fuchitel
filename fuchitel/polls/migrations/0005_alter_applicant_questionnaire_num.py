# Generated by Django 4.1.3 on 2022-11-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0004_alter_applicant_family_alter_applicant_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applicant",
            name="questionnaire_num",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Номер анкеты"
            ),
        ),
    ]
