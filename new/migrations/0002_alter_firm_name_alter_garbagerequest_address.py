# Generated by Django 4.0.5 on 2022-07-19 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firm',
            name='Name',
            field=models.CharField(blank=b'I01\n', max_length=50, null=b'I01\n', unique=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='garbagerequest',
            name='Address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='new.firm'),
        ),
    ]
