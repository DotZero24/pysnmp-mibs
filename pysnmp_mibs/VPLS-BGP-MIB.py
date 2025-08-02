_V='vplsBgpPwBindRemoteVEId'
_U='vplsBgpPwBindLocalVEId'
_T='vplsBgpVEStorageType'
_S='vplsBgpVERowStatus'
_R='vplsBgpVEPreference'
_Q='vplsBgpVEName'
_P='vplsBgpConfigVERangeSize'
_O='read-only'
_N='vplsBgpVEId'
_M='StorageType'
_L='SnmpAdminString'
_K='pwIndex'
_J='PW-STD-MIB'
_I='vplsBgpPwBindGroup'
_H='vplsBgpVEGroup'
_G='vplsBgpConfigGroup'
_F='read-create'
_E='vplsConfigIndex'
_D='VPLS-GENERIC-MIB'
_C='Unsigned32'
_B='VPLS-BGP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pwIndex,=mibBuilder.importSymbols(_J,_K)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso','transmission')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_M,'TextualConvention')
vplsConfigIndex,=mibBuilder.importSymbols(_D,_E)
vplsBgpMIB=ModuleIdentity((1,3,6,1,2,1,10,276))
if mibBuilder.loadTexts:vplsBgpMIB.setRevisions(('2014-05-19 12:00',))
_VplsBgpObjects_ObjectIdentity=ObjectIdentity
vplsBgpObjects=_VplsBgpObjects_ObjectIdentity((1,3,6,1,2,1,10,276,1))
_VplsBgpConfigTable_Object=MibTable
vplsBgpConfigTable=_VplsBgpConfigTable_Object((1,3,6,1,2,1,10,276,1,1))
if mibBuilder.loadTexts:vplsBgpConfigTable.setStatus(_A)
_VplsBgpConfigEntry_Object=MibTableRow
vplsBgpConfigEntry=_VplsBgpConfigEntry_Object((1,3,6,1,2,1,10,276,1,1,1))
vplsBgpConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:vplsBgpConfigEntry.setStatus(_A)
class _VplsBgpConfigVERangeSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VplsBgpConfigVERangeSize_Type.__name__=_C
_VplsBgpConfigVERangeSize_Object=MibTableColumn
vplsBgpConfigVERangeSize=_VplsBgpConfigVERangeSize_Object((1,3,6,1,2,1,10,276,1,1,1,1),_VplsBgpConfigVERangeSize_Type())
vplsBgpConfigVERangeSize.setMaxAccess('read-write')
if mibBuilder.loadTexts:vplsBgpConfigVERangeSize.setStatus(_A)
_VplsBgpVETable_Object=MibTable
vplsBgpVETable=_VplsBgpVETable_Object((1,3,6,1,2,1,10,276,1,2))
if mibBuilder.loadTexts:vplsBgpVETable.setStatus(_A)
_VplsBgpVEEntry_Object=MibTableRow
vplsBgpVEEntry=_VplsBgpVEEntry_Object((1,3,6,1,2,1,10,276,1,2,1))
vplsBgpVEEntry.setIndexNames((0,_D,_E),(0,_B,_N))
if mibBuilder.loadTexts:vplsBgpVEEntry.setStatus(_A)
class _VplsBgpVEId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VplsBgpVEId_Type.__name__=_C
_VplsBgpVEId_Object=MibTableColumn
vplsBgpVEId=_VplsBgpVEId_Object((1,3,6,1,2,1,10,276,1,2,1,1),_VplsBgpVEId_Type())
vplsBgpVEId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:vplsBgpVEId.setStatus(_A)
class _VplsBgpVEName_Type(SnmpAdminString):defaultValue=OctetString('')
_VplsBgpVEName_Type.__name__=_L
_VplsBgpVEName_Object=MibTableColumn
vplsBgpVEName=_VplsBgpVEName_Object((1,3,6,1,2,1,10,276,1,2,1,2),_VplsBgpVEName_Type())
vplsBgpVEName.setMaxAccess(_F)
if mibBuilder.loadTexts:vplsBgpVEName.setStatus(_A)
class _VplsBgpVEPreference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VplsBgpVEPreference_Type.__name__=_C
_VplsBgpVEPreference_Object=MibTableColumn
vplsBgpVEPreference=_VplsBgpVEPreference_Object((1,3,6,1,2,1,10,276,1,2,1,3),_VplsBgpVEPreference_Type())
vplsBgpVEPreference.setMaxAccess(_F)
if mibBuilder.loadTexts:vplsBgpVEPreference.setStatus(_A)
_VplsBgpVERowStatus_Type=RowStatus
_VplsBgpVERowStatus_Object=MibTableColumn
vplsBgpVERowStatus=_VplsBgpVERowStatus_Object((1,3,6,1,2,1,10,276,1,2,1,5),_VplsBgpVERowStatus_Type())
vplsBgpVERowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:vplsBgpVERowStatus.setStatus(_A)
class _VplsBgpVEStorageType_Type(StorageType):defaultValue=2
_VplsBgpVEStorageType_Type.__name__=_M
_VplsBgpVEStorageType_Object=MibTableColumn
vplsBgpVEStorageType=_VplsBgpVEStorageType_Object((1,3,6,1,2,1,10,276,1,2,1,6),_VplsBgpVEStorageType_Type())
vplsBgpVEStorageType.setMaxAccess(_F)
if mibBuilder.loadTexts:vplsBgpVEStorageType.setStatus(_A)
_VplsBgpPwBindTable_Object=MibTable
vplsBgpPwBindTable=_VplsBgpPwBindTable_Object((1,3,6,1,2,1,10,276,1,3))
if mibBuilder.loadTexts:vplsBgpPwBindTable.setStatus(_A)
_VplsBgpPwBindEntry_Object=MibTableRow
vplsBgpPwBindEntry=_VplsBgpPwBindEntry_Object((1,3,6,1,2,1,10,276,1,3,1))
vplsBgpPwBindEntry.setIndexNames((0,_D,_E),(0,_J,_K))
if mibBuilder.loadTexts:vplsBgpPwBindEntry.setStatus(_A)
class _VplsBgpPwBindLocalVEId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VplsBgpPwBindLocalVEId_Type.__name__=_C
_VplsBgpPwBindLocalVEId_Object=MibTableColumn
vplsBgpPwBindLocalVEId=_VplsBgpPwBindLocalVEId_Object((1,3,6,1,2,1,10,276,1,3,1,1),_VplsBgpPwBindLocalVEId_Type())
vplsBgpPwBindLocalVEId.setMaxAccess(_O)
if mibBuilder.loadTexts:vplsBgpPwBindLocalVEId.setStatus(_A)
class _VplsBgpPwBindRemoteVEId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VplsBgpPwBindRemoteVEId_Type.__name__=_C
_VplsBgpPwBindRemoteVEId_Object=MibTableColumn
vplsBgpPwBindRemoteVEId=_VplsBgpPwBindRemoteVEId_Object((1,3,6,1,2,1,10,276,1,3,1,2),_VplsBgpPwBindRemoteVEId_Type())
vplsBgpPwBindRemoteVEId.setMaxAccess(_O)
if mibBuilder.loadTexts:vplsBgpPwBindRemoteVEId.setStatus(_A)
_VplsBgpConformance_ObjectIdentity=ObjectIdentity
vplsBgpConformance=_VplsBgpConformance_ObjectIdentity((1,3,6,1,2,1,10,276,2))
_VplsBgpCompliances_ObjectIdentity=ObjectIdentity
vplsBgpCompliances=_VplsBgpCompliances_ObjectIdentity((1,3,6,1,2,1,10,276,2,1))
_VplsBgpGroups_ObjectIdentity=ObjectIdentity
vplsBgpGroups=_VplsBgpGroups_ObjectIdentity((1,3,6,1,2,1,10,276,2,2))
vplsBgpConfigGroup=ObjectGroup((1,3,6,1,2,1,10,276,2,2,1))
vplsBgpConfigGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:vplsBgpConfigGroup.setStatus(_A)
vplsBgpVEGroup=ObjectGroup((1,3,6,1,2,1,10,276,2,2,2))
vplsBgpVEGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:vplsBgpVEGroup.setStatus(_A)
vplsBgpPwBindGroup=ObjectGroup((1,3,6,1,2,1,10,276,2,2,3))
vplsBgpPwBindGroup.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:vplsBgpPwBindGroup.setStatus(_A)
vplsBgpModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,10,276,2,1,1))
vplsBgpModuleFullCompliance.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:vplsBgpModuleFullCompliance.setStatus(_A)
vplsBgpModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,10,276,2,1,2))
vplsBgpModuleReadOnlyCompliance.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:vplsBgpModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vplsBgpMIB':vplsBgpMIB,'vplsBgpObjects':vplsBgpObjects,'vplsBgpConfigTable':vplsBgpConfigTable,'vplsBgpConfigEntry':vplsBgpConfigEntry,_P:vplsBgpConfigVERangeSize,'vplsBgpVETable':vplsBgpVETable,'vplsBgpVEEntry':vplsBgpVEEntry,_N:vplsBgpVEId,_Q:vplsBgpVEName,_R:vplsBgpVEPreference,_S:vplsBgpVERowStatus,_T:vplsBgpVEStorageType,'vplsBgpPwBindTable':vplsBgpPwBindTable,'vplsBgpPwBindEntry':vplsBgpPwBindEntry,_U:vplsBgpPwBindLocalVEId,_V:vplsBgpPwBindRemoteVEId,'vplsBgpConformance':vplsBgpConformance,'vplsBgpCompliances':vplsBgpCompliances,'vplsBgpModuleFullCompliance':vplsBgpModuleFullCompliance,'vplsBgpModuleReadOnlyCompliance':vplsBgpModuleReadOnlyCompliance,'vplsBgpGroups':vplsBgpGroups,_G:vplsBgpConfigGroup,_H:vplsBgpVEGroup,_I:vplsBgpPwBindGroup})