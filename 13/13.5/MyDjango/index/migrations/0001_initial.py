# Generated by Django 2.0.6 on 2018-06-29 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('weight', models.CharField(max_length=20, verbose_name='重量')),
                ('describe', models.CharField(max_length=500, verbose_name='描述')),
            ],
        ),
    ]