# Generated by Django 2.0.4 on 2018-07-13 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shortstorylife', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
