# Generated by Django 4.2.1 on 2024-01-27 21:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("testdb", "0003_employee_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="image_filename",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]