# Generated by Django 4.2 on 2023-04-09 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adresa', '0009_remove_uliza_naseleni_punkt_uliza_rayon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='naselenipunkt',
            name='okrug',
        ),
        migrations.RemoveField(
            model_name='rayon',
            name='naseleni_punkt',
        ),
        migrations.RemoveField(
            model_name='uliza',
            name='rayon',
        ),
        migrations.AddField(
            model_name='naselenipunkt',
            name='rayon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adresa.rayon', verbose_name='Район'),
        ),
        migrations.AddField(
            model_name='rayon',
            name='okrug',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adresa.okrug', verbose_name='Округ'),
        ),
        migrations.AddField(
            model_name='uliza',
            name='naseleni_punkt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adresa.naselenipunkt', verbose_name='Населенный пункт'),
        ),
    ]