# Generated by Django 3.1.7 on 2021-03-01 20:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0003_populate_default_status_records'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphqlQuery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('query', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
