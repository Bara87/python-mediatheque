# Generated by Django 5.1.1 on 2024-09-04 03:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membre', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='artiste',
        ),
        migrations.RemoveField(
            model_name='media',
            name='realisateur',
        ),
        migrations.RemoveField(
            model_name='media',
            name='createur',
        ),
        migrations.RemoveField(
            model_name='media',
            name='auteur',
        ),
        migrations.AlterModelOptions(
            name='media',
            options={},
        ),
        migrations.RemoveField(
            model_name='media',
            name='type_media',
        ),
        migrations.AddField(
            model_name='media',
            name='quantite_disponible',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='media',
            name='nom',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='CD',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='membre.media')),
                ('artiste', models.CharField(max_length=100)),
            ],
            bases=('membre.media',),
        ),
        migrations.CreateModel(
            name='DVD',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='membre.media')),
                ('realisateur', models.CharField(max_length=100)),
            ],
            bases=('membre.media',),
        ),
        migrations.CreateModel(
            name='JeuDePlateau',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='membre.media')),
                ('createur', models.CharField(max_length=100)),
            ],
            bases=('membre.media',),
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='membre.media')),
                ('auteur', models.CharField(max_length=100)),
            ],
            bases=('membre.media',),
        ),
    ]
