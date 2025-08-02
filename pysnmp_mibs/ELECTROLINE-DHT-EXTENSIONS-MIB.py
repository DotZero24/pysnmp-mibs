if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
electrolineDHT,=mibBuilder.importSymbols('ELECTROLINE-DHT-ROOT-MIB','electrolineDHT')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dhtExtensionsMib=ModuleIdentity((1,3,6,1,4,1,5802,1,3,1,2,5))
if mibBuilder.loadTexts:dhtExtensionsMib.setRevisions(('2004-12-09 00:00',))
_DhtExtensionsMibObjects_ObjectIdentity=ObjectIdentity
dhtExtensionsMibObjects=_DhtExtensionsMibObjects_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1))
_DhtExtensionsSupported_Type=Integer32
_DhtExtensionsSupported_Object=MibScalar
dhtExtensionsSupported=_DhtExtensionsSupported_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,1),_DhtExtensionsSupported_Type())
dhtExtensionsSupported.setMaxAccess('read-only')
if mibBuilder.loadTexts:dhtExtensionsSupported.setStatus('current')
mibBuilder.exportSymbols('ELECTROLINE-DHT-EXTENSIONS-MIB',**{'dhtExtensionsMib':dhtExtensionsMib,'dhtExtensionsMibObjects':dhtExtensionsMibObjects,'dhtExtensionsSupported':dhtExtensionsSupported})