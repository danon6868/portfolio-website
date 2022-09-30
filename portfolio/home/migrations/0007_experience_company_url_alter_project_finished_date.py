# Generated by Django 4.1.1 on 2022-09-29 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_rename_name_homepage_first_name_homepage_second_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="experience",
            name="company_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="finished_date",
            field=models.DateField(blank=True, null=True, verbose_name="Finished date"),
        ),
    ]