# Generated by Django 4.1.13 on 2024-07-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_user_ctr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostelapp',
            name='ac_year',
            field=models.CharField(default='2024', max_length=4),
        ),
        migrations.AddField(
            model_name='hostelapp',
            name='address',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='hostelapp',
            name='course',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='hostelapp',
            name='course_year',
            field=models.CharField(default='1', max_length=4),
        ),
        migrations.AddField(
            model_name='hostelapp',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='hostelapp',
            name='father_name',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='hostelapp',
            name='full_name',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='hostelapp',
            name='institution',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='hostelapp',
            name='mobile_no',
            field=models.CharField(default='0000000000', max_length=10),
        ),
        migrations.AddField(
            model_name='hostelapp',
            name='reg_no',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]