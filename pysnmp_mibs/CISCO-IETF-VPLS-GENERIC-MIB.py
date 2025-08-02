_p='cvplsFwdFullAlarmCleared'
_o='cvplsFwdFullAlarmRaised'
_n='cvplsStatusChanged'
_m='cvplsPwBindStorageType'
_l='cvplsPwBindRowStatus'
_k='cvplsPwBindType'
_j='cvplsPwBindConfigType'
_i='cvplsNotificationMaxRate'
_h='cvplsStatusNotifEnable'
_g='cvplsStatusPeerCount'
_f='cvplsConfigStorageType'
_e='cvplsConfigServiceType'
_d='cvplsConfigMtu'
_c='cvplsConfigIndexNext'
_b='cvplsConfigRowStatus'
_a='cvplsConfigMacAging'
_Z='cvplsConfigDiscardUnknownDest'
_Y='cvplsConfigMacLearning'
_X='cvplsConfigDescr'
_W='cvplsConfigName'
_V='read-write'
_U='cvplsPwBindIndex'
_T='percentage'
_S='not-accessible'
_R='cvplsNotificationGroup'
_Q='cvplsPwBindGroup'
_P='cvplsGroup'
_O='cvplsStatusOperStatus'
_N='cvplsConfigAdminStatus'
_M='StorageType'
_L='SnmpAdminString'
_K='cvplsConfigFwdFullLowWatermark'
_J='cvplsConfigFwdFullHighWatermark'
_I='cvplsConfigIndex'
_H='read-only'
_G='cvplsConfigVpnId'
_F='TruthValue'
_E='Unsigned32'
_D='Integer32'
_C='read-create'
_B='current'
_A='CISCO-IETF-VPLS-GENERIC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CpwVcIndexType,=mibBuilder.importSymbols('CISCO-IETF-PW-TC-MIB','CpwVcIndexType')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_M,'TextualConvention',_F)
VPNIdOrZero,=mibBuilder.importSymbols('VPN-TC-STD-MIB','VPNIdOrZero')
cvplsGenericMIB=ModuleIdentity((1,3,6,1,4,1,9,10,138))
if mibBuilder.loadTexts:cvplsGenericMIB.setRevisions(('2007-10-22 12:00',))
_CvplsNotifications_ObjectIdentity=ObjectIdentity
cvplsNotifications=_CvplsNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,138,0))
_CvplsObjects_ObjectIdentity=ObjectIdentity
cvplsObjects=_CvplsObjects_ObjectIdentity((1,3,6,1,4,1,9,10,138,1))
_CvplsConfigIndexNext_Type=Unsigned32
_CvplsConfigIndexNext_Object=MibScalar
cvplsConfigIndexNext=_CvplsConfigIndexNext_Object((1,3,6,1,4,1,9,10,138,1,1),_CvplsConfigIndexNext_Type())
cvplsConfigIndexNext.setMaxAccess(_H)
if mibBuilder.loadTexts:cvplsConfigIndexNext.setStatus(_B)
_CvplsConfigTable_Object=MibTable
cvplsConfigTable=_CvplsConfigTable_Object((1,3,6,1,4,1,9,10,138,1,2))
if mibBuilder.loadTexts:cvplsConfigTable.setStatus(_B)
_CvplsConfigEntry_Object=MibTableRow
cvplsConfigEntry=_CvplsConfigEntry_Object((1,3,6,1,4,1,9,10,138,1,2,1))
cvplsConfigEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:cvplsConfigEntry.setStatus(_B)
class _CvplsConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvplsConfigIndex_Type.__name__=_E
_CvplsConfigIndex_Object=MibTableColumn
cvplsConfigIndex=_CvplsConfigIndex_Object((1,3,6,1,4,1,9,10,138,1,2,1,1),_CvplsConfigIndex_Type())
cvplsConfigIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:cvplsConfigIndex.setStatus(_B)
class _CvplsConfigName_Type(SnmpAdminString):defaultValue=OctetString('')
_CvplsConfigName_Type.__name__=_L
_CvplsConfigName_Object=MibTableColumn
cvplsConfigName=_CvplsConfigName_Object((1,3,6,1,4,1,9,10,138,1,2,1,2),_CvplsConfigName_Type())
cvplsConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsConfigName.setStatus(_B)
class _CvplsConfigDescr_Type(SnmpAdminString):defaultValue=OctetString('')
_CvplsConfigDescr_Type.__name__=_L
_CvplsConfigDescr_Object=MibTableColumn
cvplsConfigDescr=_CvplsConfigDescr_Object((1,3,6,1,4,1,9,10,138,1,2,1,3),_CvplsConfigDescr_Type())
cvplsConfigDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsConfigDescr.setStatus(_B)
class _CvplsConfigAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_CvplsConfigAdminStatus_Type.__name__=_D
_CvplsConfigAdminStatus_Object=MibTableColumn
cvplsConfigAdminStatus=_CvplsConfigAdminStatus_Object((1,3,6,1,4,1,9,10,138,1,2,1,4),_CvplsConfigAdminStatus_Type())
cvplsConfigAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsConfigAdminStatus.setStatus(_B)
class _CvplsConfigMacLearning_Type(TruthValue):defaultValue=1
_CvplsConfigMacLearning_Type.__name__=_F
_CvplsConfigMacLearning_Object=MibTableColumn
cvplsConfigMacLearning=_CvplsConfigMacLearning_Object((1,3,6,1,4,1,9,10,138,1,2,1,6),_CvplsConfigMacLearning_Type())
cvplsConfigMacLearning.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsConfigMacLearning.setStatus(_B)
class _CvplsConfigDiscardUnknownDest_Type(TruthValue):defaultValue=2
_CvplsConfigDiscardUnknownDest_Type.__name__=_F
_CvplsConfigDiscardUnknownDest_Object=MibTableColumn
cvplsConfigDiscardUnknownDest=_CvplsConfigDiscardUnknownDest_Object((1,3,6,1,4,1,9,10,138,1,2,1,7),_CvplsConfigDiscardUnknownDest_Type())
cvplsConfigDiscardUnknownDest.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsConfigDiscardUnknownDest.setStatus(_B)
class _CvplsConfigMacAging_Type(TruthValue):defaultValue=1
_CvplsConfigMacAging_Type.__name__=_F
_CvplsConfigMacAging_Object=MibTableColumn
cvplsConfigMacAging=_CvplsConfigMacAging_Object((1,3,6,1,4,1,9,10,138,1,2,1,8),_CvplsConfigMacAging_Type())
cvplsConfigMacAging.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsConfigMacAging.setStatus(_B)
class _CvplsConfigFwdFullHighWatermark_Type(Unsigned32):defaultValue=95;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CvplsConfigFwdFullHighWatermark_Type.__name__=_E
_CvplsConfigFwdFullHighWatermark_Object=MibTableColumn
cvplsConfigFwdFullHighWatermark=_CvplsConfigFwdFullHighWatermark_Object((1,3,6,1,4,1,9,10,138,1,2,1,10),_CvplsConfigFwdFullHighWatermark_Type())
cvplsConfigFwdFullHighWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsConfigFwdFullHighWatermark.setStatus(_B)
if mibBuilder.loadTexts:cvplsConfigFwdFullHighWatermark.setUnits(_T)
class _CvplsConfigFwdFullLowWatermark_Type(Unsigned32):defaultValue=90;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CvplsConfigFwdFullLowWatermark_Type.__name__=_E
_CvplsConfigFwdFullLowWatermark_Object=MibTableColumn
cvplsConfigFwdFullLowWatermark=_CvplsConfigFwdFullLowWatermark_Object((1,3,6,1,4,1,9,10,138,1,2,1,11),_CvplsConfigFwdFullLowWatermark_Type())
cvplsConfigFwdFullLowWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsConfigFwdFullLowWatermark.setStatus(_B)
if mibBuilder.loadTexts:cvplsConfigFwdFullLowWatermark.setUnits(_T)
_CvplsConfigRowStatus_Type=RowStatus
_CvplsConfigRowStatus_Object=MibTableColumn
cvplsConfigRowStatus=_CvplsConfigRowStatus_Object((1,3,6,1,4,1,9,10,138,1,2,1,12),_CvplsConfigRowStatus_Type())
cvplsConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsConfigRowStatus.setStatus(_B)
class _CvplsConfigMtu_Type(Unsigned32):defaultValue=1518;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1518))
_CvplsConfigMtu_Type.__name__=_E
_CvplsConfigMtu_Object=MibTableColumn
cvplsConfigMtu=_CvplsConfigMtu_Object((1,3,6,1,4,1,9,10,138,1,2,1,13),_CvplsConfigMtu_Type())
cvplsConfigMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsConfigMtu.setStatus(_B)
_CvplsConfigVpnId_Type=VPNIdOrZero
_CvplsConfigVpnId_Object=MibTableColumn
cvplsConfigVpnId=_CvplsConfigVpnId_Object((1,3,6,1,4,1,9,10,138,1,2,1,14),_CvplsConfigVpnId_Type())
cvplsConfigVpnId.setMaxAccess(_H)
if mibBuilder.loadTexts:cvplsConfigVpnId.setStatus(_B)
class _CvplsConfigServiceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan',1),('ethernet',2)))
_CvplsConfigServiceType_Type.__name__=_D
_CvplsConfigServiceType_Object=MibTableColumn
cvplsConfigServiceType=_CvplsConfigServiceType_Object((1,3,6,1,4,1,9,10,138,1,2,1,15),_CvplsConfigServiceType_Type())
cvplsConfigServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsConfigServiceType.setStatus(_B)
class _CvplsConfigStorageType_Type(StorageType):defaultValue=2
_CvplsConfigStorageType_Type.__name__=_M
_CvplsConfigStorageType_Object=MibTableColumn
cvplsConfigStorageType=_CvplsConfigStorageType_Object((1,3,6,1,4,1,9,10,138,1,2,1,16),_CvplsConfigStorageType_Type())
cvplsConfigStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsConfigStorageType.setStatus(_B)
_CvplsStatusTable_Object=MibTable
cvplsStatusTable=_CvplsStatusTable_Object((1,3,6,1,4,1,9,10,138,1,3))
if mibBuilder.loadTexts:cvplsStatusTable.setStatus(_B)
_CvplsStatusEntry_Object=MibTableRow
cvplsStatusEntry=_CvplsStatusEntry_Object((1,3,6,1,4,1,9,10,138,1,3,1))
cvplsStatusEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:cvplsStatusEntry.setStatus(_B)
class _CvplsStatusOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('other',0),('up',1),('down',2)))
_CvplsStatusOperStatus_Type.__name__=_D
_CvplsStatusOperStatus_Object=MibTableColumn
cvplsStatusOperStatus=_CvplsStatusOperStatus_Object((1,3,6,1,4,1,9,10,138,1,3,1,1),_CvplsStatusOperStatus_Type())
cvplsStatusOperStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:cvplsStatusOperStatus.setStatus(_B)
_CvplsStatusPeerCount_Type=Counter32
_CvplsStatusPeerCount_Object=MibTableColumn
cvplsStatusPeerCount=_CvplsStatusPeerCount_Object((1,3,6,1,4,1,9,10,138,1,3,1,2),_CvplsStatusPeerCount_Type())
cvplsStatusPeerCount.setMaxAccess(_H)
if mibBuilder.loadTexts:cvplsStatusPeerCount.setStatus(_B)
_CvplsPwBindTable_Object=MibTable
cvplsPwBindTable=_CvplsPwBindTable_Object((1,3,6,1,4,1,9,10,138,1,4))
if mibBuilder.loadTexts:cvplsPwBindTable.setStatus(_B)
_CvplsPwBindEntry_Object=MibTableRow
cvplsPwBindEntry=_CvplsPwBindEntry_Object((1,3,6,1,4,1,9,10,138,1,4,1))
cvplsPwBindEntry.setIndexNames((0,_A,_I),(0,_A,_U))
if mibBuilder.loadTexts:cvplsPwBindEntry.setStatus(_B)
_CvplsPwBindIndex_Type=CpwVcIndexType
_CvplsPwBindIndex_Object=MibTableColumn
cvplsPwBindIndex=_CvplsPwBindIndex_Object((1,3,6,1,4,1,9,10,138,1,4,1,1),_CvplsPwBindIndex_Type())
cvplsPwBindIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:cvplsPwBindIndex.setStatus(_B)
class _CvplsPwBindConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('autodiscovery',2)))
_CvplsPwBindConfigType_Type.__name__=_D
_CvplsPwBindConfigType_Object=MibTableColumn
cvplsPwBindConfigType=_CvplsPwBindConfigType_Object((1,3,6,1,4,1,9,10,138,1,4,1,2),_CvplsPwBindConfigType_Type())
cvplsPwBindConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsPwBindConfigType.setStatus(_B)
class _CvplsPwBindType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mesh',1),('spoke',2)))
_CvplsPwBindType_Type.__name__=_D
_CvplsPwBindType_Object=MibTableColumn
cvplsPwBindType=_CvplsPwBindType_Object((1,3,6,1,4,1,9,10,138,1,4,1,3),_CvplsPwBindType_Type())
cvplsPwBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsPwBindType.setStatus(_B)
_CvplsPwBindRowStatus_Type=RowStatus
_CvplsPwBindRowStatus_Object=MibTableColumn
cvplsPwBindRowStatus=_CvplsPwBindRowStatus_Object((1,3,6,1,4,1,9,10,138,1,4,1,4),_CvplsPwBindRowStatus_Type())
cvplsPwBindRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsPwBindRowStatus.setStatus(_B)
class _CvplsPwBindStorageType_Type(StorageType):defaultValue=2
_CvplsPwBindStorageType_Type.__name__=_M
_CvplsPwBindStorageType_Object=MibTableColumn
cvplsPwBindStorageType=_CvplsPwBindStorageType_Object((1,3,6,1,4,1,9,10,138,1,4,1,5),_CvplsPwBindStorageType_Type())
cvplsPwBindStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvplsPwBindStorageType.setStatus(_B)
class _CvplsStatusNotifEnable_Type(TruthValue):defaultValue=2
_CvplsStatusNotifEnable_Type.__name__=_F
_CvplsStatusNotifEnable_Object=MibScalar
cvplsStatusNotifEnable=_CvplsStatusNotifEnable_Object((1,3,6,1,4,1,9,10,138,1,5),_CvplsStatusNotifEnable_Type())
cvplsStatusNotifEnable.setMaxAccess(_V)
if mibBuilder.loadTexts:cvplsStatusNotifEnable.setStatus(_B)
class _CvplsNotificationMaxRate_Type(Unsigned32):defaultValue=0
_CvplsNotificationMaxRate_Type.__name__=_E
_CvplsNotificationMaxRate_Object=MibScalar
cvplsNotificationMaxRate=_CvplsNotificationMaxRate_Object((1,3,6,1,4,1,9,10,138,1,6),_CvplsNotificationMaxRate_Type())
cvplsNotificationMaxRate.setMaxAccess(_V)
if mibBuilder.loadTexts:cvplsNotificationMaxRate.setStatus(_B)
_CvplsConformance_ObjectIdentity=ObjectIdentity
cvplsConformance=_CvplsConformance_ObjectIdentity((1,3,6,1,4,1,9,10,138,2))
_CvplsCompliances_ObjectIdentity=ObjectIdentity
cvplsCompliances=_CvplsCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,138,2,1))
_CvplsGroups_ObjectIdentity=ObjectIdentity
cvplsGroups=_CvplsGroups_ObjectIdentity((1,3,6,1,4,1,9,10,138,2,2))
cvplsGroup=ObjectGroup((1,3,6,1,4,1,9,10,138,2,2,1))
cvplsGroup.setObjects(*((_A,_W),(_A,_X),(_A,_N),(_A,_Y),(_A,_Z),(_A,_a),(_A,_G),(_A,_J),(_A,_K),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_O),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:cvplsGroup.setStatus(_B)
cvplsPwBindGroup=ObjectGroup((1,3,6,1,4,1,9,10,138,2,2,2))
cvplsPwBindGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:cvplsPwBindGroup.setStatus(_B)
cvplsStatusChanged=NotificationType((1,3,6,1,4,1,9,10,138,0,1))
cvplsStatusChanged.setObjects(*((_A,_G),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:cvplsStatusChanged.setStatus(_B)
cvplsFwdFullAlarmRaised=NotificationType((1,3,6,1,4,1,9,10,138,0,2))
cvplsFwdFullAlarmRaised.setObjects(*((_A,_G),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:cvplsFwdFullAlarmRaised.setStatus(_B)
cvplsFwdFullAlarmCleared=NotificationType((1,3,6,1,4,1,9,10,138,0,3))
cvplsFwdFullAlarmCleared.setObjects(*((_A,_G),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:cvplsFwdFullAlarmCleared.setStatus(_B)
cvplsNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,10,138,2,2,3))
cvplsNotificationGroup.setObjects(*((_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:cvplsNotificationGroup.setStatus(_B)
cvplsModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,138,2,1,1))
cvplsModuleFullCompliance.setObjects(*((_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:cvplsModuleFullCompliance.setStatus(_B)
cvplsModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,138,2,1,2))
cvplsModuleReadOnlyCompliance.setObjects(*((_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:cvplsModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'cvplsGenericMIB':cvplsGenericMIB,'cvplsNotifications':cvplsNotifications,_n:cvplsStatusChanged,_o:cvplsFwdFullAlarmRaised,_p:cvplsFwdFullAlarmCleared,'cvplsObjects':cvplsObjects,_c:cvplsConfigIndexNext,'cvplsConfigTable':cvplsConfigTable,'cvplsConfigEntry':cvplsConfigEntry,_I:cvplsConfigIndex,_W:cvplsConfigName,_X:cvplsConfigDescr,_N:cvplsConfigAdminStatus,_Y:cvplsConfigMacLearning,_Z:cvplsConfigDiscardUnknownDest,_a:cvplsConfigMacAging,_J:cvplsConfigFwdFullHighWatermark,_K:cvplsConfigFwdFullLowWatermark,_b:cvplsConfigRowStatus,_d:cvplsConfigMtu,_G:cvplsConfigVpnId,_e:cvplsConfigServiceType,_f:cvplsConfigStorageType,'cvplsStatusTable':cvplsStatusTable,'cvplsStatusEntry':cvplsStatusEntry,_O:cvplsStatusOperStatus,_g:cvplsStatusPeerCount,'cvplsPwBindTable':cvplsPwBindTable,'cvplsPwBindEntry':cvplsPwBindEntry,_U:cvplsPwBindIndex,_j:cvplsPwBindConfigType,_k:cvplsPwBindType,_l:cvplsPwBindRowStatus,_m:cvplsPwBindStorageType,_h:cvplsStatusNotifEnable,_i:cvplsNotificationMaxRate,'cvplsConformance':cvplsConformance,'cvplsCompliances':cvplsCompliances,'cvplsModuleFullCompliance':cvplsModuleFullCompliance,'cvplsModuleReadOnlyCompliance':cvplsModuleReadOnlyCompliance,'cvplsGroups':cvplsGroups,_P:cvplsGroup,_Q:cvplsPwBindGroup,_R:cvplsNotificationGroup})