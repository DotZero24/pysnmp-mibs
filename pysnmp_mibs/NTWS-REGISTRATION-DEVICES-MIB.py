if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntwsRegistration,=mibBuilder.importSymbols('NTWS-ROOT-MIB','ntwsRegistration')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntwsRegistrationDevicesMib=ModuleIdentity((1,3,6,1,4,1,45,6,1,3,6))
if mibBuilder.loadTexts:ntwsRegistrationDevicesMib.setRevisions(('2008-08-08 00:01','2007-08-22 00:00'))
_NtwsWirelessSwitch_ObjectIdentity=ObjectIdentity
ntwsWirelessSwitch=_NtwsWirelessSwitch_ObjectIdentity((1,3,6,1,4,1,45,6,1,3,1))
_NtwsSwitch2360_ObjectIdentity=ObjectIdentity
ntwsSwitch2360=_NtwsSwitch2360_ObjectIdentity((1,3,6,1,4,1,45,6,1,3,1,2))
_NtwsSwitch2380_ObjectIdentity=ObjectIdentity
ntwsSwitch2380=_NtwsSwitch2380_ObjectIdentity((1,3,6,1,4,1,45,6,1,3,1,3))
_NtwsSwitch2350_ObjectIdentity=ObjectIdentity
ntwsSwitch2350=_NtwsSwitch2350_ObjectIdentity((1,3,6,1,4,1,45,6,1,3,1,4))
_NtwsSwitch2372_ObjectIdentity=ObjectIdentity
ntwsSwitch2372=_NtwsSwitch2372_ObjectIdentity((1,3,6,1,4,1,45,6,1,3,1,5))
_NtwsSwitch2382_ObjectIdentity=ObjectIdentity
ntwsSwitch2382=_NtwsSwitch2382_ObjectIdentity((1,3,6,1,4,1,45,6,1,3,1,6))
_NtwsSwitch2800_ObjectIdentity=ObjectIdentity
ntwsSwitch2800=_NtwsSwitch2800_ObjectIdentity((1,3,6,1,4,1,45,6,1,3,1,7))
mibBuilder.exportSymbols('NTWS-REGISTRATION-DEVICES-MIB',**{'ntwsWirelessSwitch':ntwsWirelessSwitch,'ntwsSwitch2360':ntwsSwitch2360,'ntwsSwitch2380':ntwsSwitch2380,'ntwsSwitch2350':ntwsSwitch2350,'ntwsSwitch2372':ntwsSwitch2372,'ntwsSwitch2382':ntwsSwitch2382,'ntwsSwitch2800':ntwsSwitch2800,'ntwsRegistrationDevicesMib':ntwsRegistrationDevicesMib})