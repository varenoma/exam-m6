# Generated by Django 5.2.1 on 2025-05-10 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QatagonClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('birth_date', models.DateField()),
                ('died_date', models.DateField()),
                ('description', models.TextField()),
                ('region', models.CharField()),
                ('ayblov', models.CharField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
