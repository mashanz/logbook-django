# Generated by Django 3.2.6 on 2021-09-06 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CashFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateTimeField(verbose_name='Tanggal Transaksi')),
                ('nama_item', models.CharField(max_length=200)),
                ('qty', models.IntegerField(default=1)),
                ('harga_satuan', models.FloatField(default=0.0)),
                ('harga_total', models.FloatField(default=0.0)),
            ],
        ),
    ]