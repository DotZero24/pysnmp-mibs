_O='qtechvplsBgpConfigGroup'
_N='qtechvplsBgpPwBindRemoteVEId'
_M='qtechvplsBgpPwBindLocalVEId'
_L='qtechvplsBgpVEPreference'
_K='qtechvplsBgpVEindex'
_J='qtechvplsPwBindIndex'
_I='qtechvplsBgpPwBindGroup'
_H='qtechvplsBgpVEGroup'
_G='read-only'
_F='read-create'
_E='qtechvplsConfigIndex'
_D='QTECH-VPLS-GENERIC-MIB'
_C='Unsigned32'
_B='QTECH-VPLS-BGP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
qtechvplsConfigIndex,qtechvplsPwBindIndex=mibBuilder.importSymbols(_D,_E,_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso','transmission')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
qtechvplsBgpDraft01MIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,79))
if mibBuilder.loadTexts:qtechvplsBgpDraft01MIB.setRevisions(('2010-04-28 12:00',))
class QtechVplsBgpRouteDistinguisher(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class QtechVplsBgpRouteTarget(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_QtechvplsBgpObjects_ObjectIdentity=ObjectIdentity
qtechvplsBgpObjects=_QtechvplsBgpObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,79,1))
_QtechvplsBgpVETable_Object=MibTable
qtechvplsBgpVETable=_QtechvplsBgpVETable_Object((1,3,6,1,4,1,27514,1,1,10,2,79,1,1))
if mibBuilder.loadTexts:qtechvplsBgpVETable.setStatus(_A)
_QtechvplsBgpVEEntry_Object=MibTableRow
qtechvplsBgpVEEntry=_QtechvplsBgpVEEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,79,1,1,1))
qtechvplsBgpVEEntry.setIndexNames((0,_D,_E),(0,_B,_K))
if mibBuilder.loadTexts:qtechvplsBgpVEEntry.setStatus(_A)
class _QtechvplsBgpVEindex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechvplsBgpVEindex_Type.__name__=_C
_QtechvplsBgpVEindex_Object=MibTableColumn
qtechvplsBgpVEindex=_QtechvplsBgpVEindex_Object((1,3,6,1,4,1,27514,1,1,10,2,79,1,1,1,1),_QtechvplsBgpVEindex_Type())
qtechvplsBgpVEindex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:qtechvplsBgpVEindex.setStatus(_A)
class _QtechvplsBgpVEId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_QtechvplsBgpVEId_Type.__name__=_C
_QtechvplsBgpVEId_Object=MibTableColumn
qtechvplsBgpVEId=_QtechvplsBgpVEId_Object((1,3,6,1,4,1,27514,1,1,10,2,79,1,1,1,2),_QtechvplsBgpVEId_Type())
qtechvplsBgpVEId.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechvplsBgpVEId.setStatus(_A)
class _QtechvplsBgpRangeSize_Type(Unsigned32):defaultValue=16;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_QtechvplsBgpRangeSize_Type.__name__=_C
_QtechvplsBgpRangeSize_Object=MibTableColumn
qtechvplsBgpRangeSize=_QtechvplsBgpRangeSize_Object((1,3,6,1,4,1,27514,1,1,10,2,79,1,1,1,3),_QtechvplsBgpRangeSize_Type())
qtechvplsBgpRangeSize.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechvplsBgpRangeSize.setStatus(_A)
class _QtechvplsBgpVEPreference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_QtechvplsBgpVEPreference_Type.__name__=_C
_QtechvplsBgpVEPreference_Object=MibTableColumn
qtechvplsBgpVEPreference=_QtechvplsBgpVEPreference_Object((1,3,6,1,4,1,27514,1,1,10,2,79,1,1,1,4),_QtechvplsBgpVEPreference_Type())
qtechvplsBgpVEPreference.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechvplsBgpVEPreference.setStatus(_A)
_QtechvplsBgpVERowStatus_Type=RowStatus
_QtechvplsBgpVERowStatus_Object=MibTableColumn
qtechvplsBgpVERowStatus=_QtechvplsBgpVERowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,79,1,1,1,5),_QtechvplsBgpVERowStatus_Type())
qtechvplsBgpVERowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechvplsBgpVERowStatus.setStatus(_A)
_QtechvplsBgpPwBindTable_Object=MibTable
qtechvplsBgpPwBindTable=_QtechvplsBgpPwBindTable_Object((1,3,6,1,4,1,27514,1,1,10,2,79,1,2))
if mibBuilder.loadTexts:qtechvplsBgpPwBindTable.setStatus(_A)
_QtechvplsBgpPwBindEntry_Object=MibTableRow
qtechvplsBgpPwBindEntry=_QtechvplsBgpPwBindEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,79,1,2,1))
qtechvplsBgpPwBindEntry.setIndexNames((0,_D,_E),(0,_D,_J))
if mibBuilder.loadTexts:qtechvplsBgpPwBindEntry.setStatus(_A)
class _QtechvplsBgpPwBindLocalVEId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_QtechvplsBgpPwBindLocalVEId_Type.__name__=_C
_QtechvplsBgpPwBindLocalVEId_Object=MibTableColumn
qtechvplsBgpPwBindLocalVEId=_QtechvplsBgpPwBindLocalVEId_Object((1,3,6,1,4,1,27514,1,1,10,2,79,1,2,1,1),_QtechvplsBgpPwBindLocalVEId_Type())
qtechvplsBgpPwBindLocalVEId.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechvplsBgpPwBindLocalVEId.setStatus(_A)
class _QtechvplsBgpPwBindRemoteVEId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_QtechvplsBgpPwBindRemoteVEId_Type.__name__=_C
_QtechvplsBgpPwBindRemoteVEId_Object=MibTableColumn
qtechvplsBgpPwBindRemoteVEId=_QtechvplsBgpPwBindRemoteVEId_Object((1,3,6,1,4,1,27514,1,1,10,2,79,1,2,1,2),_QtechvplsBgpPwBindRemoteVEId_Type())
qtechvplsBgpPwBindRemoteVEId.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechvplsBgpPwBindRemoteVEId.setStatus(_A)
_QtechvplsBgpConformance_ObjectIdentity=ObjectIdentity
qtechvplsBgpConformance=_QtechvplsBgpConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,79,2))
_QtechvplsBgpCompliances_ObjectIdentity=ObjectIdentity
qtechvplsBgpCompliances=_QtechvplsBgpCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,79,2,1))
_QtechvplsBgpGroups_ObjectIdentity=ObjectIdentity
qtechvplsBgpGroups=_QtechvplsBgpGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,79,2,2))
qtechvplsBgpVEGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,79,2,2,2))
qtechvplsBgpVEGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:qtechvplsBgpVEGroup.setStatus(_A)
qtechvplsBgpPwBindGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,79,2,2,3))
qtechvplsBgpPwBindGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:qtechvplsBgpPwBindGroup.setStatus(_A)
qtechvplsBgpModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,79,2,1,1))
qtechvplsBgpModuleFullCompliance.setObjects(*((_B,_O),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:qtechvplsBgpModuleFullCompliance.setStatus(_A)
qtechvplsBgpModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,79,2,1,2))
qtechvplsBgpModuleReadOnlyCompliance.setObjects(*((_B,_O),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:qtechvplsBgpModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'QtechVplsBgpRouteDistinguisher':QtechVplsBgpRouteDistinguisher,'QtechVplsBgpRouteTarget':QtechVplsBgpRouteTarget,'qtechvplsBgpDraft01MIB':qtechvplsBgpDraft01MIB,'qtechvplsBgpObjects':qtechvplsBgpObjects,'qtechvplsBgpVETable':qtechvplsBgpVETable,'qtechvplsBgpVEEntry':qtechvplsBgpVEEntry,_K:qtechvplsBgpVEindex,'qtechvplsBgpVEId':qtechvplsBgpVEId,'qtechvplsBgpRangeSize':qtechvplsBgpRangeSize,_L:qtechvplsBgpVEPreference,'qtechvplsBgpVERowStatus':qtechvplsBgpVERowStatus,'qtechvplsBgpPwBindTable':qtechvplsBgpPwBindTable,'qtechvplsBgpPwBindEntry':qtechvplsBgpPwBindEntry,_M:qtechvplsBgpPwBindLocalVEId,_N:qtechvplsBgpPwBindRemoteVEId,'qtechvplsBgpConformance':qtechvplsBgpConformance,'qtechvplsBgpCompliances':qtechvplsBgpCompliances,'qtechvplsBgpModuleFullCompliance':qtechvplsBgpModuleFullCompliance,'qtechvplsBgpModuleReadOnlyCompliance':qtechvplsBgpModuleReadOnlyCompliance,'qtechvplsBgpGroups':qtechvplsBgpGroups,_H:qtechvplsBgpVEGroup,_I:qtechvplsBgpPwBindGroup})