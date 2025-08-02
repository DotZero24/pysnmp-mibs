_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lenovo=ModuleIdentity((1,3,6,1,4,1,19046))
if mibBuilder.loadTexts:lenovo.setRevisions(('2016-10-27 18:30',))
_LenovoProducts_ObjectIdentity=ObjectIdentity
lenovoProducts=_LenovoProducts_ObjectIdentity((1,3,6,1,4,1,19046,1))
if mibBuilder.loadTexts:lenovoProducts.setStatus(_A)
_LenovoNetworkMibs_ObjectIdentity=ObjectIdentity
lenovoNetworkMibs=_LenovoNetworkMibs_ObjectIdentity((1,3,6,1,4,1,19046,2))
if mibBuilder.loadTexts:lenovoNetworkMibs.setStatus(_A)
_Network_mibs_ObjectIdentity=ObjectIdentity
network_mibs=_Network_mibs_ObjectIdentity((1,3,6,1,4,1,19046,2,3))
if mibBuilder.loadTexts:network_mibs.setStatus(_A)
_Tor_mibs_ObjectIdentity=ObjectIdentity
tor_mibs=_Tor_mibs_ObjectIdentity((1,3,6,1,4,1,19046,2,7))
if mibBuilder.loadTexts:tor_mibs.setStatus(_A)
_Flex_mibs_ObjectIdentity=ObjectIdentity
flex_mibs=_Flex_mibs_ObjectIdentity((1,3,6,1,4,1,19046,2,18))
if mibBuilder.loadTexts:flex_mibs.setStatus(_A)
_LenovoModules_ObjectIdentity=ObjectIdentity
lenovoModules=_LenovoModules_ObjectIdentity((1,3,6,1,4,1,19046,4))
if mibBuilder.loadTexts:lenovoModules.setStatus(_A)
_LenovoServerMibs_ObjectIdentity=ObjectIdentity
lenovoServerMibs=_LenovoServerMibs_ObjectIdentity((1,3,6,1,4,1,19046,11))
if mibBuilder.loadTexts:lenovoServerMibs.setStatus(_A)
mibBuilder.exportSymbols('LENOVO-SMI-MIB',**{'lenovo':lenovo,'lenovoProducts':lenovoProducts,'lenovoNetworkMibs':lenovoNetworkMibs,'network-mibs':network_mibs,'tor-mibs':tor_mibs,'flex-mibs':flex_mibs,'lenovoModules':lenovoModules,'lenovoServerMibs':lenovoServerMibs})