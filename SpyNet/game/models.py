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
    techno_ranconware = models.SmallIntegerField()
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
    cooling_system = models.SmallIntegerField('CoolingSystem')
    power_supply = models.SmallIntegerField('PowerSupply')
    network_interface = models.SmallIntegerField('NetworkInterface')
    cpu = models.SmallIntegerField('CPU')
    core_count = models.SmallIntegerField()
    ram = models.SmallIntegerField('RAM')
    memory_stick = models.SmallIntegerField('MemoryStick')
    hard_drive = models.SmallIntegerField('HardDrive')
    
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
    date_update = models.DateTimeField(auto_now_add=True, auto_now=True,
                                       verbose_name="Update date")

    def __str__(self):
        return str(self.ip)


class Process(models.Model):
    name = models.CharField(max_length=10)
    host = models.ForeignKey('Computer')
    owner = models.ForeignKey('Computer')
    level = models.SmallIntegerField()
    activated = models.SmallBooleanField()
    kind = models.SmallIntegerField()

    def __str__(self):
        return "Process " + str(self.kind)

    
class Link(models.Model):
    computer_from = models.Foreign('Computer')
    computer_to = models.Foreign('Computer')
    activated = models.BooleanField()

    def __str__(self):
        return "Link"
