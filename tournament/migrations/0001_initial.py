# Generated by Django 5.1.5 on 2025-02-03 17:03

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointsFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('points1', models.IntegerField(default=0)),
                ('points2', models.IntegerField(default=0)),
                ('points3', models.IntegerField(default=0)),
                ('points4', models.IntegerField(default=0)),
                ('points5', models.IntegerField(default=0)),
                ('points6', models.IntegerField(default=0)),
                ('points7', models.IntegerField(default=0)),
                ('points8', models.IntegerField(default=0)),
                ('points9', models.IntegerField(default=0)),
                ('points10', models.IntegerField(default=0)),
                ('points_per_kill', models.IntegerField(default=0)),
                ('lost_points_per_death', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('table_header_name', models.CharField(blank=True, max_length=100, null=True)),
                ('tournament_type', models.CharField(choices=[('LBSB', 'LBSB'), ('SQUADCUP', 'Squad Cup'), ('TREINO_CLAS', '5x5 de clãs')], max_length=20)),
                ('date', models.DateField()),
                ('isFinished', models.BooleanField(default=False)),
                ('clan1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clan1_tournaments', to='core.clan')),
                ('clan2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clan2_tournaments', to='core.clan')),
                ('pointsFormat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tournament.pointsformat')),
            ],
        ),
        migrations.CreateModel(
            name='TournamentMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gems', models.PositiveIntegerField(default=0)),
                ('position', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('clan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.clan')),
                ('killed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='killed_players', to='core.player')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.player')),
                ('tournament_match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournamentmatch')),
            ],
        ),
    ]
