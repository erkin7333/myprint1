# Generated by Django 4.1.1 on 2022-10-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprint', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='type_services',
            name='lazer_price',
            field=models.CharField(blank=True, default=None, max_length=65, null=True, verbose_name='lazer_price'),
        ),
        migrations.AddField(
            model_name='type_services',
            name='lazer_size',
            field=models.CharField(blank=True, default=None, max_length=65, null=True, verbose_name='lazer_size'),
        ),
        migrations.AddField(
            model_name='type_services',
            name='shiroki_name',
            field=models.CharField(blank=True, default=None, max_length=65, null=True, verbose_name='shiroki_name'),
        ),
        migrations.AddField(
            model_name='type_services',
            name='shiroki_price',
            field=models.CharField(blank=True, default=None, max_length=65, null=True, verbose_name='shiroki_price'),
        ),
        migrations.AddField(
            model_name='type_services',
            name='shiroki_size',
            field=models.CharField(blank=True, default=None, max_length=65, null=True, verbose_name='shiroki_size'),
        ),
        migrations.AddField(
            model_name='type_services',
            name='tekstil_price',
            field=models.CharField(blank=True, default=None, max_length=65, null=True, verbose_name='tekstil_price'),
        ),
        migrations.AddField(
            model_name='type_services',
            name='tekstil_size',
            field=models.CharField(blank=True, default=None, max_length=65, null=True, verbose_name='tekstil_size'),
        ),
        migrations.AlterField(
            model_name='type_services',
            name='double_site_print',
            field=models.CharField(blank=True, max_length=65, null=True, verbose_name='ikki tomonlama chop etish'),
        ),
        migrations.AlterField(
            model_name='type_services',
            name='one_site_print',
            field=models.CharField(blank=True, max_length=65, null=True, verbose_name='bir tomonlama chop etish'),
        ),
        migrations.AlterField(
            model_name='type_services',
            name='size',
            field=models.CharField(blank=True, default=None, max_length=65, null=True, verbose_name='razmeri'),
        ),
        migrations.AlterField(
            model_name='type_services',
            name='type_paper',
            field=models.CharField(blank=True, max_length=65, null=True, verbose_name="qog'oz_turi"),
        ),
    ]