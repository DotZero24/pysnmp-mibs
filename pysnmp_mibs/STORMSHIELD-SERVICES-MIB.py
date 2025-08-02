_E='snsServicesIndex'
_D='STORMSHIELD-SERVICES-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
stormshieldMIB,=mibBuilder.importSymbols('STORMSHIELD-SMI-MIB','stormshieldMIB')
snsServices=ModuleIdentity((1,3,6,1,4,1,11256,1,7))
if mibBuilder.loadTexts:snsServices.setRevisions(('2017-02-20 00:00',))
_SnsServicesTable_Object=MibTable
snsServicesTable=_SnsServicesTable_Object((1,3,6,1,4,1,11256,1,7,1))
if mibBuilder.loadTexts:snsServicesTable.setStatus(_A)
_SnsServicesEntry_Object=MibTableRow
snsServicesEntry=_SnsServicesEntry_Object((1,3,6,1,4,1,11256,1,7,1,1))
snsServicesEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:snsServicesEntry.setStatus(_A)
class _SnsServicesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnsServicesIndex_Type.__name__=_C
_SnsServicesIndex_Object=MibTableColumn
snsServicesIndex=_SnsServicesIndex_Object((1,3,6,1,4,1,11256,1,7,1,1,1),_SnsServicesIndex_Type())
snsServicesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snsServicesIndex.setStatus(_A)
_SnsServicesName_Type=SnmpAdminString
_SnsServicesName_Object=MibTableColumn
snsServicesName=_SnsServicesName_Object((1,3,6,1,4,1,11256,1,7,1,1,2),_SnsServicesName_Type())
snsServicesName.setMaxAccess(_B)
if mibBuilder.loadTexts:snsServicesName.setStatus(_A)
_SnsServicesState_Type=Integer32
_SnsServicesState_Object=MibTableColumn
snsServicesState=_SnsServicesState_Object((1,3,6,1,4,1,11256,1,7,1,1,3),_SnsServicesState_Type())
snsServicesState.setMaxAccess(_B)
if mibBuilder.loadTexts:snsServicesState.setStatus(_A)
_SnsServicesUptime_Type=Integer32
_SnsServicesUptime_Object=MibTableColumn
snsServicesUptime=_SnsServicesUptime_Object((1,3,6,1,4,1,11256,1,7,1,1,4),_SnsServicesUptime_Type())
snsServicesUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:snsServicesUptime.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'snsServices':snsServices,'snsServicesTable':snsServicesTable,'snsServicesEntry':snsServicesEntry,_E:snsServicesIndex,'snsServicesName':snsServicesName,'snsServicesState':snsServicesState,'snsServicesUptime':snsServicesUptime})