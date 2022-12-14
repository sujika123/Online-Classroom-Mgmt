# Generated by Django 4.1.1 on 2022-10-19 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroomapp', '0002_alter_teacherlogin_subject_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherlogin',
            name='subject',
            field=models.CharField(choices=[('MBD', 'MBD'), ('MATHS', 'MATHS'), ('DCS', 'DCS'), ('ENGLISH', 'ENGLISH'), ('SP', 'SP'), ('DBMS', 'DBMS')], max_length=30),
        ),
        migrations.CreateModel(
            name='addnotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(max_length=254, upload_to=None)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
