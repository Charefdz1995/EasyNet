from django.db import models


class Topology(models.Model):
    TopologyName = models.CharField(max_length=45)
    TopologyDescription = models.CharField(max_length=200)
    NetworkAddress = models.CharField(max_length=45)
    DomainName = models.CharField(max_length=45)

class Device(models.Model):
    Router,Layer2Switch,Layer3Switch = "R" , "L2S" , "L3S"
    Type = (
        (Router,"Router"),
        (Layer2Switch,"Layer2Switch"),
        (Layer3Switch,"Layer3Switch")
    )
    Core,Aggregation,Access = "C" , "Agg" , "Acc"
    Location = (
        (Core,"Core"),
        (Aggregation,"Aggregation"),
        (Access,"Access")
    )
    Hostname = models.CharField(max_length=45)
    UserName = models.CharField(max_length=45)
    Password = models.CharField(max_length=45)
    Secret   = models.CharField(max_length=45)
    DeviceType = models.CharField(max_length=20,choices=Type)
    DeviceLocation = models.CharField(max_length=20,choices=Location)
    TopologyRef = models.ForeignKey(Topology, on_delete=models.CASCADE)
class Link(models.Model):
    # FirstEdge= models.ForeignKey(Port,on_delete=models.CASCADE)
    # SecondEdge = models.ForeignKey(Port, on_delete=models.CASCADE)
    TopologyRef = models.ForeignKey(Topology, on_delete=models.CASCADE)

class Port(models.Model):
    Ipv4Address = models.CharField(max_length=45)
    InterfaceDescription = models.CharField(max_length=100)
    InterfaceStatus = models.BooleanField(default=False)
    DeviceRef= models.ForeignKey(Device, on_delete=models.CASCADE)
    LinkRef = models.ForeignKey(Link,on_delete=models.CASCADE)


class Interface(Port):
    FastEthernet, GigabitEthernet, Ethernet, Serial= "Fa" , "Gi" , "Eth", "Se"
    Type = (
        (FastEthernet,"FastEthernet"),
        (GigabitEthernet,"GigabitEtherne"),
        (Ethernet,"Ethernet"),
        (Serial,"Serial"),
    )
    InterfacePort = models.CharField(max_length=5)
    InterfaceSlot = models.CharField(max_length=5)
    Switchport = models.BooleanField(default=False)
    InterfaceType = models.CharField(max_length=20,choices=Type)


class SubInterface(Port):
    SubIntNum = models.IntegerField
    InterfaceRef = models.ForeignKey(Interface, on_delete=models.CASCADE)


class LoopBack(Port):
    LoNum = models.IntegerField

class InterfaceVlan(Port):
    VlanNum = models.IntegerField

#TODO : EtherChannel
