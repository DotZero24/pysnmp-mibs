if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rbtwsRegistration,=mibBuilder.importSymbols('RBTWS-ROOT-MIB','rbtwsRegistration')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbtwsRegistrationDevicesMib=ModuleIdentity((1,3,6,1,4,1,52,4,15,1,3,6))
if mibBuilder.loadTexts:rbtwsRegistrationDevicesMib.setRevisions(('2007-08-22 00:00',))
_RbtwsWirelessSwitch_ObjectIdentity=ObjectIdentity
rbtwsWirelessSwitch=_RbtwsWirelessSwitch_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,3,1))
_RbtwsSwitch8100_ObjectIdentity=ObjectIdentity
rbtwsSwitch8100=_RbtwsSwitch8100_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,3,1,1))
_RbtwsSwitch8200_ObjectIdentity=ObjectIdentity
rbtwsSwitch8200=_RbtwsSwitch8200_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,3,1,2))
_RbtwsSwitch8400_ObjectIdentity=ObjectIdentity
rbtwsSwitch8400=_RbtwsSwitch8400_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,3,1,3))
_RbtwsSwitch8110_ObjectIdentity=ObjectIdentity
rbtwsSwitch8110=_RbtwsSwitch8110_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,3,1,4))
_RbtwsSwitch8500_ObjectIdentity=ObjectIdentity
rbtwsSwitch8500=_RbtwsSwitch8500_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,3,1,5))
mibBuilder.exportSymbols('RBTWS-REGISTRATION-DEVICES-MIB',**{'rbtwsWirelessSwitch':rbtwsWirelessSwitch,'rbtwsSwitch8100':rbtwsSwitch8100,'rbtwsSwitch8200':rbtwsSwitch8200,'rbtwsSwitch8400':rbtwsSwitch8400,'rbtwsSwitch8110':rbtwsSwitch8110,'rbtwsSwitch8500':rbtwsSwitch8500,'rbtwsRegistrationDevicesMib':rbtwsRegistrationDevicesMib})