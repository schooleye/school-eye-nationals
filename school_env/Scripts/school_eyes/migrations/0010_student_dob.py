# Generated by Django 4.0.5 on 2022-06-17 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_eyes', '0009_student_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='DOB',
            field=models.CharField(default=18, max_length=15),
        ),
    ]
