from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Player(models.Model):
    login = models.CharField(max_length=18)
    password = models.CharField(max_length=42)
    data_perso = models.IntegerField()
    cash = models.IntegerField()
    score = models.IntegerField()

    # Technology
    techno_overclock = models.SmallIntegerField()
    techno_spyware = models.SmallIntegerField()
    techno_antispyware = models.SmallIntegerField()
    techno_virus = models.SmallIntegerField()
    techno_antivirus = models.SmallIntegerField()
    techno_scan = models.SmallIntegerField()
    techno_proxy = models.SmallIntegerField()
    techno_firewall = models.SmallIntegerField()
    techno_tcpip = models.SmallIntegerField()
    techno_OS = models.SmallIntegerField()
    techno_data = models.SmallIntegerField()
    techno_parallelization = models.SmallIntegerField()
    techno_crypto = models.SmallIntegerField()

    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Creation date")

    def __str__(self):
        return self.login


class Computer(models.Model):
    ip = models.GenericIPAddressField()
    owner = models.ForeignKey('Player')
    data = models.IntegerField()

    # Hardware
    cooling_system = models.ForeignKey('CoolingSystem')
    power_supply = models.ForeignKey('PowerSupply')
    network_interface = models.ForeignKey('NetworkInterface')
    cpu = models.ForeignKey('CPU')
    ram = models.ForeignKey('RAM')
    hard_drive = models.ForeignKey('HardDrive')
    
    # Software
    anti_virus = models.SmallIntegerField()
    anti_spyware = models.SmallIntegerField()
    firewall = models.SmallIntegerField()

    # Settings
    #   - Hardware
    fan_power = models.SmallIntegerField()
    cpu_power = models.SmallIntegerField()
    ram_power = models.SmallIntegerField()
    hdd_power = models.SmallIntegerField()
    network_interface_activated = models.SmallIntegerField()

    #   - Software
    anti_virus_priority = models.SmallIntegerField()
    anti_spyware_priority = models.SmallIntegerField()
    firewall_priority = models.SmallIntegerField()
    update_priority = models.SmallIntegerField()
    scan_priority = models.SmallIntegerField()

    date_creation = models.DateTimeField(auto_now_add=True, auto_now=False,
                                         verbose_name="Creation date")
    date_update = models.DateTimeField(auto_now_add=False, auto_now=True,
                                       verbose_name="Update date")

    def __str__(self):
        return str(self.ip)


class Process(models.Model):
    name = models.CharField(max_length=10)
    host = models.ForeignKey('Computer',
                             related_name='running_processes')
    owner = models.ForeignKey('Computer',
                              related_name='owned_processes')
    level = models.SmallIntegerField()
    activated = models.BooleanField()
    kind = models.SmallIntegerField()

    def __str__(self):
        return "Process " + str(self.kind)

    
class Link(models.Model):
    computer_from = models.ForeignKey('Computer',
                                      related_name='computer_to')
    computer_to = models.ForeignKey('Computer',
                                    related_name='computer_from')
    activated = models.BooleanField()
    secured = models.BooleanField()
    visible = models.BooleanField()
    
    def __str__(self):
        return "Link"


class PowerSupply(models.Model):
    description = models.TextField
    price = models.SmallIntegerField()
    image = models.ImageField()
    power_max = models.SmallIntegerField()
    level = models.SmallIntegerField()
    upgrade = models.OneToOneField('PowerSupply',
                                   related_name='downgrade')

    def __str__(self):
        return "Power supply : " + self.description


class CoolingSystem(models.Model):
    description = models.TextField()
    price = models.SmallIntegerField()
    image = models.ImageField()
    power_max = models.SmallIntegerField()
    cooling_max = models.SmallIntegerField()
    level = models.SmallIntegerField()
    upgrade_tech = models.OneToOneField('CoolingSystem',
                                        related_name='downgrade_tech')
    upgrade_power = models.OneToOneField('CoolingSystem',
                                         related_name='downgrade_power')

    def __str__(self):
        return "Cooling system : " + self.description


class CPU(models.Model):
    description = models.TextField()
    price = models.SmallIntegerField()
    image = models.ImageField()
    power_max = models.SmallIntegerField()
    frequency_max = models.SmallIntegerField()
    core_count = models.SmallIntegerField()
    upgrade_freq = models.OneToOneField('CPU',
                                        related_name='downgrade_freq')
    upgrade_core = models.OneToOneField('CPU',
                                        related_name='downgrade_core')

    def __str__(self):
        return "CPU : " + self.description


class RAM(models.Model):
    description = models.TextField()
    price = models.SmallIntegerField()
    image = models.ImageField()
    power_max = models.SmallIntegerField()
    frequency_max = models.SmallIntegerField()
    memory_max = models.SmallIntegerField()
    upgrade_freq = models.OneToOneField('RAM',
                                        related_name='downgrade_freq')
    upgrade_memory = models.OneToOneField('RAM',
                                          related_name='downgrade_memory')

    def __str__(self):
        return "RAM : " + self.description


class HardDrive(models.Model):
    description = models.TextField()
    price = models.SmallIntegerField()
    image = models.ImageField()
    power_max = models.SmallIntegerField()
    speed_max = models.SmallIntegerField()
    storage_max = models.SmallIntegerField()
    upgrade_storage = models.OneToOneField('HardDrive',
                                           related_name='downgrade_storage')
    upgrade_speed = models.OneToOneField('HardDrive',
                                         related_name='downgrade_speed')
    upgrade_tech = models.OneToOneField('HardDrive',
                                        related_name='downgrade_tech')

    def __str__(self):
        return "Hard drive : " + self.description


class NetworkInterface(models.Model):
    description = models.TextField()
    price = models.SmallIntegerField()
    image = models.ImageField()
    power_max = models.SmallIntegerField()
    upgrade_bandwidth = models.OneToOneField('NetworkInterface',
                                             related_name='downgrade_bandwith')

    def __str__(self):
        return "Network Interface : " + self.description


