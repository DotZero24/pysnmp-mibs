_D='EfpBridgeStpGroupMacAddressType'
_C='dot1dBasePort'
_B='BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_B,_C)
eltMesFastpath,=mibBuilder.importSymbols('ELTEX-MES-FASTPATH-MIB','eltMesFastpath')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eltFastpathBridgeMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,103,3))
if mibBuilder.loadTexts:eltFastpathBridgeMIB.setRevisions(('2017-09-05 00:00',))
class EfpBridgeStpGroupMacAddressType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dot1d',1),('dot1ad',2),('auto',3)))
_EfpBridgeObjects_ObjectIdentity=ObjectIdentity
efpBridgeObjects=_EfpBridgeObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,103,3,1))
_EfpBridgeConfigs_ObjectIdentity=ObjectIdentity
efpBridgeConfigs=_EfpBridgeConfigs_ObjectIdentity((1,3,6,1,4,1,35265,1,103,3,1,2))
_EfpBridgeConfigsStp_ObjectIdentity=ObjectIdentity
efpBridgeConfigsStp=_EfpBridgeConfigsStp_ObjectIdentity((1,3,6,1,4,1,35265,1,103,3,1,2,1))
_EfpBridgeStpConfigPortTable_Object=MibTable
efpBridgeStpConfigPortTable=_EfpBridgeStpConfigPortTable_Object((1,3,6,1,4,1,35265,1,103,3,1,2,1,1))
if mibBuilder.loadTexts:efpBridgeStpConfigPortTable.setStatus(_A)
_EfpBridgeStpConfigPortEntry_Object=MibTableRow
efpBridgeStpConfigPortEntry=_EfpBridgeStpConfigPortEntry_Object((1,3,6,1,4,1,35265,1,103,3,1,2,1,1,1))
efpBridgeStpConfigPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:efpBridgeStpConfigPortEntry.setStatus(_A)
class _EfpBridgeStpConfigPortGroupMacAddress_Type(EfpBridgeStpGroupMacAddressType):defaultValue=1
_EfpBridgeStpConfigPortGroupMacAddress_Type.__name__=_D
_EfpBridgeStpConfigPortGroupMacAddress_Object=MibTableColumn
efpBridgeStpConfigPortGroupMacAddress=_EfpBridgeStpConfigPortGroupMacAddress_Object((1,3,6,1,4,1,35265,1,103,3,1,2,1,1,1,1),_EfpBridgeStpConfigPortGroupMacAddress_Type())
efpBridgeStpConfigPortGroupMacAddress.setMaxAccess('read-write')
if mibBuilder.loadTexts:efpBridgeStpConfigPortGroupMacAddress.setStatus(_A)
_EfpBridgeNotifications_ObjectIdentity=ObjectIdentity
efpBridgeNotifications=_EfpBridgeNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,103,3,2))
_EfpBridgeNotificationsPrefix_ObjectIdentity=ObjectIdentity
efpBridgeNotificationsPrefix=_EfpBridgeNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35265,1,103,3,2,0))
_EfpBridgeConformance_ObjectIdentity=ObjectIdentity
efpBridgeConformance=_EfpBridgeConformance_ObjectIdentity((1,3,6,1,4,1,35265,1,103,3,3))
mibBuilder.exportSymbols('ELTEX-FASTPATH-BRIDGE-MIB',**{_D:EfpBridgeStpGroupMacAddressType,'eltFastpathBridgeMIB':eltFastpathBridgeMIB,'efpBridgeObjects':efpBridgeObjects,'efpBridgeConfigs':efpBridgeConfigs,'efpBridgeConfigsStp':efpBridgeConfigsStp,'efpBridgeStpConfigPortTable':efpBridgeStpConfigPortTable,'efpBridgeStpConfigPortEntry':efpBridgeStpConfigPortEntry,'efpBridgeStpConfigPortGroupMacAddress':efpBridgeStpConfigPortGroupMacAddress,'efpBridgeNotifications':efpBridgeNotifications,'efpBridgeNotificationsPrefix':efpBridgeNotificationsPrefix,'efpBridgeConformance':efpBridgeConformance})