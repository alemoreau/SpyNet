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
    data_perso = models.IntegerField()
    score = models.IntegerField()

    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Creation date")

    def __str__(self):
        return str(self.ip)


class CPU(models.Model):
    computer = models.ForeignKey('Computer')
    overclocked = models.BooleanField()
    level = models.SmallIntegerField()  # Core count
    
    def __str__(self):
        return "CPU " + self.level


class Core(models.Model):
    cpu = models.ForeignKey('CPU')
    level = models.SmallIntegerField()
    power_usage = models.SmallIntegerField()

    def __str__(self):
        return "Core " + self.level


class RAM(models.Model):
    computer = models.ForeignKey('Computer')
    overclocked = models.BooleanField()

    def __str__(self):
        return "RAM"


class MemoryStick(models.Model):
    ram = models.ForeignKey('RAM')
    level = models.SmallIntegerField()
    power_usage = models.SmallIntegerField()

    def __str__(self):
        return "Memory Stick " + self.level


class Fan(models.Model):
    computer = models.ForeignKey('Computer')
    level = models.SmallIntegerField()
    power_usage = models.SmallIntegerField()

    def __str__(self):
        return "Fan " + str(self.level)


class Power(models.Model):
    computer = models.ForeignKey('Computer')
    level = models.SmallIntegerField()

    def __str__(self):
        return "Power " + str(self.level)


class NetworkInterface(models.Model):
    computer = models.ForeignKey('Computer')
    level = models.SmallIntegerField()
    power_usage = models.SmallIntegerField()
    enabled = models.BooleanField()

    def __str__(self):
        return "NetworkInterface " + self.level


class HardDrive(models.Model):
    computer = models.Foreign('Computer')
    level = models.SmallIntegerField()
    power_usage = models.SmallIntegerField()

    def __str__(self):
        return "HardDrive " + self.level


class Process(models.Model):
    name = models.CharField(max_length=10)
    core = models.ForeignKey('Core')
    memory_stick = models.ForeignKey('MemoryStick')
    hard_drive = models.ForeignKey('HardDrive')
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
