# Generated by Django 3.0 on 2023-02-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0003_formdata_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formdata',
            name='course',
        ),
        migrations.RemoveField(
            model_name='formdata',
            name='username',
        ),
        migrations.AddField(
            model_name='formdata',
            name='name',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formdata',
            name='email',
            field=models.EmailField(max_length=70),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='phone',
            field=models.CharField(max_length=70),
        ),
    ]