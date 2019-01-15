# Generated by Django 2.1.1 on 2019-01-15 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('duration', models.TimeField(blank=True)),
                ('statistics', models.TextField(default='{}')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('statistics', models.TextField(default='{}')),
                ('achievements', models.TextField(default='[]')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='match',
            name='players',
            field=models.ManyToManyField(to='profiles.Profile'),
        ),
    ]
