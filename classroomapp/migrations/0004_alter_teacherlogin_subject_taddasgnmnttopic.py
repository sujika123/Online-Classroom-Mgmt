# Generated by Django 4.1.1 on 2022-10-21 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroomapp', '0003_alter_teacherlogin_subject_addnotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherlogin',
            name='subject',
            field=models.CharField(choices=[('ENGLISH', 'ENGLISH'), ('DBMS', 'DBMS'), ('SP', 'SP'), ('DCS', 'DCS'), ('MATHS', 'MATHS'), ('MBD', 'MBD')], max_length=30),
        ),
        migrations.CreateModel(
            name='taddAsgnmnttopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
