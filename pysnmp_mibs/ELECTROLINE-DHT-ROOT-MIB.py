_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
electrolineHardwareProducts,=mibBuilder.importSymbols('ELECTROLINE-GLOBAL-REG','electrolineHardwareProducts')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
electrolineDHT=ModuleIdentity((1,3,6,1,4,1,5802,1,3,1,2))
if mibBuilder.loadTexts:electrolineDHT.setRevisions(('2003-03-20 00:00',))
_DhtInventory_ObjectIdentity=ObjectIdentity
dhtInventory=_DhtInventory_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,1))
if mibBuilder.loadTexts:dhtInventory.setStatus(_A)
_DhtConfiguration_ObjectIdentity=ObjectIdentity
dhtConfiguration=_DhtConfiguration_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,2))
if mibBuilder.loadTexts:dhtConfiguration.setStatus(_A)
_DhtStatus_ObjectIdentity=ObjectIdentity
dhtStatus=_DhtStatus_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,3))
if mibBuilder.loadTexts:dhtStatus.setStatus(_A)
_DhtPrivate_ObjectIdentity=ObjectIdentity
dhtPrivate=_DhtPrivate_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,4))
if mibBuilder.loadTexts:dhtPrivate.setStatus(_A)
_DhtExtensionsMib_ObjectIdentity=ObjectIdentity
dhtExtensionsMib=_DhtExtensionsMib_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,5))
if mibBuilder.loadTexts:dhtExtensionsMib.setStatus(_A)
mibBuilder.exportSymbols('ELECTROLINE-DHT-ROOT-MIB',**{'electrolineDHT':electrolineDHT,'dhtInventory':dhtInventory,'dhtConfiguration':dhtConfiguration,'dhtStatus':dhtStatus,'dhtPrivate':dhtPrivate,'dhtExtensionsMib':dhtExtensionsMib})