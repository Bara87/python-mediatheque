# Generated by Django 5.1 on 2024-09-02 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('disponible', models.BooleanField(default=True)),
                ('date_emprunt', models.DateTimeField(blank=True, null=True)),
                ('date_retour', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emprunteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('bloque', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CD',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bibliothecaire.media')),
                ('artiste', models.CharField(max_length=100)),
            ],
            bases=('bibliothecaire.media',),
        ),
        migrations.CreateModel(
            name='DVD',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bibliothecaire.media')),
                ('realisateur', models.CharField(max_length=100)),
            ],
            bases=('bibliothecaire.media',),
        ),
        migrations.CreateModel(
            name='JeuDePlateau',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bibliothecaire.media')),
                ('createur', models.CharField(max_length=100)),
            ],
            bases=('bibliothecaire.media',),
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bibliothecaire.media')),
                ('auteur', models.CharField(max_length=100)),
            ],
            bases=('bibliothecaire.media',),
        ),
        migrations.AddField(
            model_name='media',
            name='emprunteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bibliothecaire.emprunteur'),
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateTimeField(auto_now_add=True)),
                ('date_retour', models.DateTimeField(blank=True, null=True)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire.media')),
                ('emprunteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire.emprunteur')),
            ],
        ),
    ]
