# Generated by Django 4.1.13 on 2024-07-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_user_ctr', '0008_hostelapp_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintbox',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
