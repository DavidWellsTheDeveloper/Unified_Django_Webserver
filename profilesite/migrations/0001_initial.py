# Generated by Django 3.1.2 on 2020-10-05 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('faq_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=300)),
                ('question_short', models.CharField(max_length=100, null=True)),
                ('answer', models.TextField()),
            ],
        ),
    ]
