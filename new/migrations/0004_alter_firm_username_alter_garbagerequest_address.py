# Generated by Django 4.0.5 on 2022-07-21 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0003_alter_garbagerequest_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firm',
            name='username',
            field=models.ForeignKey(null=b'I00\n', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='garbagerequest',
            name='Address',
            field=models.ForeignKey(null=b'I00\n', on_delete=django.db.models.deletion.CASCADE, to='new.firm'),
        ),
    ]
