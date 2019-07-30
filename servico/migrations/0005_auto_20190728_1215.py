# Generated by Django 2.2.3 on 2019-07-28 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0004_auto_20190728_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicos',
            name='Valor',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
