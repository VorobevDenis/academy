# Generated by Django 4.2 on 2023-06-05 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_employee_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='boss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='boss_department', to='main.employee', verbose_name='Руководитель департамента'),
        ),
    ]