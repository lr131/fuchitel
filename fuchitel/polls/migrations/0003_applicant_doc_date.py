# Generated by Django 4.1.3 on 2022-11-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_applicant_work_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="applicant",
            name="doc_date",
            field=models.DateField(blank=True, null=True, verbose_name="П/Дыты выдачи"),
        ),
    ]
