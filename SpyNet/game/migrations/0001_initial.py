# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 00:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('data', models.IntegerField()),
                ('anti_virus', models.SmallIntegerField()),
                ('anti_spyware', models.SmallIntegerField()),
                ('firewall', models.SmallIntegerField()),
                ('fan_power', models.SmallIntegerField()),
                ('cpu_power', models.SmallIntegerField()),
                ('ram_power', models.SmallIntegerField()),
                ('hdd_power', models.SmallIntegerField()),
                ('network_interface_activated', models.SmallIntegerField()),
                ('anti_virus_priority', models.SmallIntegerField()),
                ('anti_spyware_priority', models.SmallIntegerField()),
                ('firewall_priority', models.SmallIntegerField()),
                ('update_priority', models.SmallIntegerField()),
                ('scan_priority', models.SmallIntegerField()),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Update date')),
            ],
        ),
        migrations.CreateModel(
            name='CoolingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('price', models.SmallIntegerField()),
                ('image', models.ImageField(upload_to=b'')),
                ('power_max', models.SmallIntegerField()),
                ('cooling_max', models.SmallIntegerField()),
                ('level', models.SmallIntegerField()),
                ('upgrade_power', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='downgrade_power', to='game.CoolingSystem')),
                ('upgrade_tech', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='downgrade_tech', to='game.CoolingSystem')),
            ],
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('price', models.SmallIntegerField()),
                ('image', models.ImageField(upload_to=b'')),
                ('power_max', models.SmallIntegerField()),
                ('frequency_max', models.SmallIntegerField()),
                ('core_count', models.SmallIntegerField()),
                ('upgrade_core', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='downgrade_core', to='game.CPU')),
                ('upgrade_freq', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='downgrade_freq', to='game.CPU')),
            ],
        ),
        migrations.CreateModel(
            name='HardDrive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('price', models.SmallIntegerField()),
                ('image', models.ImageField(upload_to=b'')),
                ('power_max', models.SmallIntegerField()),
                ('speed_max', models.SmallIntegerField()),
                ('storage_max', models.SmallIntegerField()),
                ('upgrade_speed', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='downgrade_speed', to='game.HardDrive')),
                ('upgrade_storage', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='downgrade_storage', to='game.HardDrive')),
                ('upgrade_tech', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='downgrade_tech', to='game.HardDrive')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activated', models.BooleanField()),
                ('secured', models.BooleanField()),
                ('visible', models.BooleanField()),
                ('computer_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='computer_to', to='game.Computer')),
                ('computer_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='computer_from', to='game.Computer')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkInterface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('price', models.SmallIntegerField()),
                ('image', models.ImageField(upload_to=b'')),
                ('power_max', models.SmallIntegerField()),
                ('upgrade_bandwidth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='downgrade_bandwith', to='game.NetworkInterface')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=18)),
                ('password', models.CharField(max_length=42)),
                ('data_perso', models.IntegerField()),
                ('cash', models.IntegerField()),
                ('score', models.IntegerField()),
                ('techno_overclock', models.SmallIntegerField()),
                ('techno_spyware', models.SmallIntegerField()),
                ('techno_antispyware', models.SmallIntegerField()),
                ('techno_virus', models.SmallIntegerField()),
                ('techno_antivirus', models.SmallIntegerField()),
                ('techno_scan', models.SmallIntegerField()),
                ('techno_proxy', models.SmallIntegerField()),
                ('techno_firewall', models.SmallIntegerField()),
                ('techno_tcpip', models.SmallIntegerField()),
                ('techno_OS', models.SmallIntegerField()),
                ('techno_data', models.SmallIntegerField()),
                ('techno_parallelization', models.SmallIntegerField()),
                ('techno_crypto', models.SmallIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
            ],
        ),
        migrations.CreateModel(
            name='PowerSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.SmallIntegerField()),
                ('image', models.ImageField(upload_to=b'')),
                ('power_max', models.SmallIntegerField()),
                ('level', models.SmallIntegerField()),
                ('upgrade', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='downgrade', to='game.PowerSupply')),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('level', models.SmallIntegerField()),
                ('activated', models.BooleanField()),
                ('kind', models.SmallIntegerField()),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='running_processes', to='game.Computer')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_processes', to='game.Computer')),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('price', models.SmallIntegerField()),
                ('image', models.ImageField(upload_to=b'')),
                ('power_max', models.SmallIntegerField()),
                ('frequency_max', models.SmallIntegerField()),
                ('memory_max', models.SmallIntegerField()),
                ('upgrade_freq', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='downgrade_freq', to='game.RAM')),
                ('upgrade_memory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='downgrade_memory', to='game.RAM')),
            ],
        ),
        migrations.AddField(
            model_name='computer',
            name='cooling_system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.CoolingSystem'),
        ),
        migrations.AddField(
            model_name='computer',
            name='cpu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.CPU'),
        ),
        migrations.AddField(
            model_name='computer',
            name='hard_drive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.HardDrive'),
        ),
        migrations.AddField(
            model_name='computer',
            name='network_interface',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.NetworkInterface'),
        ),
        migrations.AddField(
            model_name='computer',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Player'),
        ),
        migrations.AddField(
            model_name='computer',
            name='power_supply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.PowerSupply'),
        ),
        migrations.AddField(
            model_name='computer',
            name='ram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.RAM'),
        ),
    ]