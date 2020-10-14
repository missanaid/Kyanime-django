# Generated by Django 3.1.2 on 2020-10-14 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_anime', models.CharField(max_length=200)),
                ('episodios', models.IntegerField(help_text='Cantidad de Capítulos del Anime')),
                ('sinopsis', models.CharField(help_text='Descripción del Anime', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('primer_nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(help_text='Email de Usuario', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateField(blank=True, null=True)),
                ('rating_general', models.FloatField(help_text='Valoración General del Anime')),
                ('rating_animacion', models.FloatField(help_text='Valoración de la Animación')),
                ('rating_traduccion', models.FloatField(help_text='Valoración de la Traducción del Anime')),
                ('rating_personajes', models.FloatField(help_text='Valoración de los Personajes del Anime')),
                ('nombre_anime', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='anime.anime')),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='genero',
            field=models.ManyToManyField(to='anime.Genero'),
        ),
        migrations.AddField(
            model_name='anime',
            name='rating_general',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='anime.review'),
        ),
    ]