_N='fsvplsBgpPwBindRemoteVEId'
_M='fsvplsBgpPwBindLocalVEId'
_L='fsvplsBgpVEPreference'
_K='fsvplsBgpVEindex'
_J='fsvplsPwBindIndex'
_I='fsvplsBgpPwBindGroup'
_H='fsvplsBgpVEGroup'
_G='read-only'
_F='read-create'
_E='fsvplsConfigIndex'
_D='FS-VPLS-GENERIC-MIB'
_C='Unsigned32'
_B='FS-VPLS-BGP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
fsvplsConfigIndex,fsvplsPwBindIndex=mibBuilder.importSymbols(_D,_E,_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso','transmission')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
fsvplsBgpDraft01MIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,79))
if mibBuilder.loadTexts:fsvplsBgpDraft01MIB.setRevisions(('2010-04-28 12:00',))
class FSVplsBgpRouteDistinguisher(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class FSVplsBgpRouteTarget(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_FsvplsBgpObjects_ObjectIdentity=ObjectIdentity
fsvplsBgpObjects=_FsvplsBgpObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,79,1))
_FsvplsBgpVETable_Object=MibTable
fsvplsBgpVETable=_FsvplsBgpVETable_Object((1,3,6,1,4,1,52642,1,1,10,2,79,1,1))
if mibBuilder.loadTexts:fsvplsBgpVETable.setStatus(_A)
_FsvplsBgpVEEntry_Object=MibTableRow
fsvplsBgpVEEntry=_FsvplsBgpVEEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,79,1,1,1))
fsvplsBgpVEEntry.setIndexNames((0,_D,_E),(0,_B,_K))
if mibBuilder.loadTexts:fsvplsBgpVEEntry.setStatus(_A)
class _FsvplsBgpVEindex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsvplsBgpVEindex_Type.__name__=_C
_FsvplsBgpVEindex_Object=MibTableColumn
fsvplsBgpVEindex=_FsvplsBgpVEindex_Object((1,3,6,1,4,1,52642,1,1,10,2,79,1,1,1,1),_FsvplsBgpVEindex_Type())
fsvplsBgpVEindex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsvplsBgpVEindex.setStatus(_A)
class _FsvplsBgpVEId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_FsvplsBgpVEId_Type.__name__=_C
_FsvplsBgpVEId_Object=MibTableColumn
fsvplsBgpVEId=_FsvplsBgpVEId_Object((1,3,6,1,4,1,52642,1,1,10,2,79,1,1,1,2),_FsvplsBgpVEId_Type())
fsvplsBgpVEId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsvplsBgpVEId.setStatus(_A)
class _FsvplsBgpRangeSize_Type(Unsigned32):defaultValue=16;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_FsvplsBgpRangeSize_Type.__name__=_C
_FsvplsBgpRangeSize_Object=MibTableColumn
fsvplsBgpRangeSize=_FsvplsBgpRangeSize_Object((1,3,6,1,4,1,52642,1,1,10,2,79,1,1,1,3),_FsvplsBgpRangeSize_Type())
fsvplsBgpRangeSize.setMaxAccess(_F)
if mibBuilder.loadTexts:fsvplsBgpRangeSize.setStatus(_A)
class _FsvplsBgpVEPreference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_FsvplsBgpVEPreference_Type.__name__=_C
_FsvplsBgpVEPreference_Object=MibTableColumn
fsvplsBgpVEPreference=_FsvplsBgpVEPreference_Object((1,3,6,1,4,1,52642,1,1,10,2,79,1,1,1,4),_FsvplsBgpVEPreference_Type())
fsvplsBgpVEPreference.setMaxAccess(_G)
if mibBuilder.loadTexts:fsvplsBgpVEPreference.setStatus(_A)
_FsvplsBgpVERowStatus_Type=RowStatus
_FsvplsBgpVERowStatus_Object=MibTableColumn
fsvplsBgpVERowStatus=_FsvplsBgpVERowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,79,1,1,1,5),_FsvplsBgpVERowStatus_Type())
fsvplsBgpVERowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsvplsBgpVERowStatus.setStatus(_A)
_FsvplsBgpPwBindTable_Object=MibTable
fsvplsBgpPwBindTable=_FsvplsBgpPwBindTable_Object((1,3,6,1,4,1,52642,1,1,10,2,79,1,2))
if mibBuilder.loadTexts:fsvplsBgpPwBindTable.setStatus(_A)
_FsvplsBgpPwBindEntry_Object=MibTableRow
fsvplsBgpPwBindEntry=_FsvplsBgpPwBindEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,79,1,2,1))
fsvplsBgpPwBindEntry.setIndexNames((0,_D,_E),(0,_D,_J))
if mibBuilder.loadTexts:fsvplsBgpPwBindEntry.setStatus(_A)
class _FsvplsBgpPwBindLocalVEId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_FsvplsBgpPwBindLocalVEId_Type.__name__=_C
_FsvplsBgpPwBindLocalVEId_Object=MibTableColumn
fsvplsBgpPwBindLocalVEId=_FsvplsBgpPwBindLocalVEId_Object((1,3,6,1,4,1,52642,1,1,10,2,79,1,2,1,1),_FsvplsBgpPwBindLocalVEId_Type())
fsvplsBgpPwBindLocalVEId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsvplsBgpPwBindLocalVEId.setStatus(_A)
class _FsvplsBgpPwBindRemoteVEId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_FsvplsBgpPwBindRemoteVEId_Type.__name__=_C
_FsvplsBgpPwBindRemoteVEId_Object=MibTableColumn
fsvplsBgpPwBindRemoteVEId=_FsvplsBgpPwBindRemoteVEId_Object((1,3,6,1,4,1,52642,1,1,10,2,79,1,2,1,2),_FsvplsBgpPwBindRemoteVEId_Type())
fsvplsBgpPwBindRemoteVEId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsvplsBgpPwBindRemoteVEId.setStatus(_A)
_FsvplsBgpConformance_ObjectIdentity=ObjectIdentity
fsvplsBgpConformance=_FsvplsBgpConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,79,2))
_FsvplsBgpCompliances_ObjectIdentity=ObjectIdentity
fsvplsBgpCompliances=_FsvplsBgpCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,79,2,1))
_FsvplsBgpGroups_ObjectIdentity=ObjectIdentity
fsvplsBgpGroups=_FsvplsBgpGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,79,2,2))
fsvplsBgpVEGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,79,2,2,2))
fsvplsBgpVEGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:fsvplsBgpVEGroup.setStatus(_A)
fsvplsBgpPwBindGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,79,2,2,3))
fsvplsBgpPwBindGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:fsvplsBgpPwBindGroup.setStatus(_A)
fsvplsBgpModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,79,2,1,1))
fsvplsBgpModuleFullCompliance.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:fsvplsBgpModuleFullCompliance.setStatus(_A)
fsvplsBgpModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,79,2,1,2))
fsvplsBgpModuleReadOnlyCompliance.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:fsvplsBgpModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'FSVplsBgpRouteDistinguisher':FSVplsBgpRouteDistinguisher,'FSVplsBgpRouteTarget':FSVplsBgpRouteTarget,'fsvplsBgpDraft01MIB':fsvplsBgpDraft01MIB,'fsvplsBgpObjects':fsvplsBgpObjects,'fsvplsBgpVETable':fsvplsBgpVETable,'fsvplsBgpVEEntry':fsvplsBgpVEEntry,_K:fsvplsBgpVEindex,'fsvplsBgpVEId':fsvplsBgpVEId,'fsvplsBgpRangeSize':fsvplsBgpRangeSize,_L:fsvplsBgpVEPreference,'fsvplsBgpVERowStatus':fsvplsBgpVERowStatus,'fsvplsBgpPwBindTable':fsvplsBgpPwBindTable,'fsvplsBgpPwBindEntry':fsvplsBgpPwBindEntry,_M:fsvplsBgpPwBindLocalVEId,_N:fsvplsBgpPwBindRemoteVEId,'fsvplsBgpConformance':fsvplsBgpConformance,'fsvplsBgpCompliances':fsvplsBgpCompliances,'fsvplsBgpModuleFullCompliance':fsvplsBgpModuleFullCompliance,'fsvplsBgpModuleReadOnlyCompliance':fsvplsBgpModuleReadOnlyCompliance,'fsvplsBgpGroups':fsvplsBgpGroups,_H:fsvplsBgpVEGroup,_I:fsvplsBgpPwBindGroup})