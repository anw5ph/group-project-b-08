# Generated by Django 3.2.12 on 2022-03-20 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=30)),
                ('attendees', models.ManyToManyField(related_name='student_attendees', to='study.Student')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.student')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('class_number', models.CharField(max_length=30)),
                ('sessions', models.ManyToManyField(related_name='study_sessions', to='study.Study')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=30)),
                ('sections', models.ManyToManyField(related_name='course_section', to='study.Section')),
            ],
        ),
    ]
