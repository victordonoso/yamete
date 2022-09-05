# Generated by Django 4.0.6 on 2022-08-30 01:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=50, verbose_name='Title')),
                ('event_description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('event_date', models.DateField(verbose_name='Date')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Slug')),
                ('event_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('match_date', models.DateField(verbose_name='Date')),
                ('match_team_0', models.CharField(max_length=50, verbose_name='Team 0')),
                ('match_team_1', models.CharField(max_length=50, verbose_name='Team 1')),
                ('match_team_0_score', models.IntegerField(blank=True, null=True, verbose_name='Team 0 Score')),
                ('match_team_1_score', models.IntegerField(blank=True, null=True, verbose_name='Team 1 Score')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Slug')),
                ('parent_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='eventmanager.events')),
            ],
            options={
                'verbose_name': 'Matches',
                'verbose_name_plural': 'Matchess',
            },
        ),
    ]