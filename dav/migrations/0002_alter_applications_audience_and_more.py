# Generated by Django 4.2.7 on 2023-12-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dav', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='audience',
            field=models.CharField(default='306э', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='applications',
            name='day_lesson',
            field=models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='applications',
            name='time_lesson',
            field=models.IntegerField(choices=[(1, '8-30'), (2, '10-00'), (3, '12-00'), (4, '14-00'), (5, '18-00')], default=1, null=True),
        ),
    ]
