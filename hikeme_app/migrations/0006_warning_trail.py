# Generated by Django 4.1.1 on 2022-09-15 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hikeme_app', '0005_alter_person_auth_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='warning',
            name='trail',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='hikeme_app.trail'),
            preserve_default=False,
        ),
    ]
