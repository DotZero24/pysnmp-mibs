_p='vplsFwdFullAlarmCleared'
_o='vplsFwdFullAlarmRaised'
_n='vplsStatusChanged'
_m='vplsPwBindStorageType'
_l='vplsPwBindRowStatus'
_k='vplsPwBindType'
_j='vplsPwBindConfigType'
_i='vplsNotificationMaxRate'
_h='vplsStatusNotifEnable'
_g='vplsStatusPeerCount'
_f='vplsConfigStorageType'
_e='vplsConfigServiceType'
_d='vplsConfigMtu'
_c='vplsConfigIndexNext'
_b='vplsConfigRowStatus'
_a='vplsConfigMacAging'
_Z='vplsConfigDiscardUnknownDest'
_Y='vplsConfigMacLearning'
_X='vplsConfigDescr'
_W='vplsConfigName'
_V='read-write'
_U='vplsPwBindIndex'
_T='percentage'
_S='not-accessible'
_R='vplsNotificationGroup'
_Q='vplsPwBindGroup'
_P='vplsGroup'
_O='vplsStatusOperStatus'
_N='vplsConfigAdminStatus'
_M='StorageType'
_L='SnmpAdminString'
_K='vplsConfigFwdFullLowWatermark'
_J='vplsConfigFwdFullHighWatermark'
_I='vplsConfigIndex'
_H='read-only'
_G='vplsConfigVpnId'
_F='TruthValue'
_E='Unsigned32'
_D='Integer32'
_C='read-create'
_B='current'
_A='VPLS-GENERIC-DRAFT-01-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PwIndexType,=mibBuilder.importSymbols('FOUNDRY-PW-TC-STD-MIB','PwIndexType')
vplsRoot,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','vplsRoot')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_M,'TextualConvention',_F)
VPNIdOrZero,=mibBuilder.importSymbols('VPN-TC-STD-MIB','VPNIdOrZero')
vplsGenericDraft01MIB=ModuleIdentity((1,3,6,1,4,1,1991,3,4,1))
if mibBuilder.loadTexts:vplsGenericDraft01MIB.setRevisions(('2006-08-30 12:00','2006-06-04 12:00'))
_VplsNotifications_ObjectIdentity=ObjectIdentity
vplsNotifications=_VplsNotifications_ObjectIdentity((1,3,6,1,4,1,1991,3,4,1,0))
_VplsObjects_ObjectIdentity=ObjectIdentity
vplsObjects=_VplsObjects_ObjectIdentity((1,3,6,1,4,1,1991,3,4,1,1))
_VplsConfigIndexNext_Type=Unsigned32
_VplsConfigIndexNext_Object=MibScalar
vplsConfigIndexNext=_VplsConfigIndexNext_Object((1,3,6,1,4,1,1991,3,4,1,1,1),_VplsConfigIndexNext_Type())
vplsConfigIndexNext.setMaxAccess(_H)
if mibBuilder.loadTexts:vplsConfigIndexNext.setStatus(_B)
_VplsConfigTable_Object=MibTable
vplsConfigTable=_VplsConfigTable_Object((1,3,6,1,4,1,1991,3,4,1,1,2))
if mibBuilder.loadTexts:vplsConfigTable.setStatus(_B)
_VplsConfigEntry_Object=MibTableRow
vplsConfigEntry=_VplsConfigEntry_Object((1,3,6,1,4,1,1991,3,4,1,1,2,1))
vplsConfigEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:vplsConfigEntry.setStatus(_B)
class _VplsConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VplsConfigIndex_Type.__name__=_E
_VplsConfigIndex_Object=MibTableColumn
vplsConfigIndex=_VplsConfigIndex_Object((1,3,6,1,4,1,1991,3,4,1,1,2,1,1),_VplsConfigIndex_Type())
vplsConfigIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:vplsConfigIndex.setStatus(_B)
class _VplsConfigName_Type(SnmpAdminString):defaultValue=OctetString('')
_VplsConfigName_Type.__name__=_L
_VplsConfigName_Object=MibTableColumn
vplsConfigName=_VplsConfigName_Object((1,3,6,1,4,1,1991,3,4,1,1,2,1,2),_VplsConfigName_Type())
vplsConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigName.setStatus(_B)
class _VplsConfigDescr_Type(SnmpAdminString):defaultValue=OctetString('')
_VplsConfigDescr_Type.__name__=_L
_VplsConfigDescr_Object=MibTableColumn
vplsConfigDescr=_VplsConfigDescr_Object((1,3,6,1,4,1,1991,3,4,1,1,2,1,3),_VplsConfigDescr_Type())
vplsConfigDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigDescr.setStatus(_B)
class _VplsConfigAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_VplsConfigAdminStatus_Type.__name__=_D
_VplsConfigAdminStatus_Object=MibTableColumn
vplsConfigAdminStatus=_VplsConfigAdminStatus_Object((1,3,6,1,4,1,1991,3,4,1,1,2,1,4),_VplsConfigAdminStatus_Type())
vplsConfigAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigAdminStatus.setStatus(_B)
class _VplsConfigMacLearning_Type(TruthValue):defaultValue=1
_VplsConfigMacLearning_Type.__name__=_F
_VplsConfigMacLearning_Object=MibTableColumn
vplsConfigMacLearning=_VplsConfigMacLearning_Object((1,3,6,1,4,1,1991,3,4,1,1,2,1,6),_VplsConfigMacLearning_Type())
vplsConfigMacLearning.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigMacLearning.setStatus(_B)
class _VplsConfigDiscardUnknownDest_Type(TruthValue):defaultValue=2
_VplsConfigDiscardUnknownDest_Type.__name__=_F
_VplsConfigDiscardUnknownDest_Object=MibTableColumn
vplsConfigDiscardUnknownDest=_VplsConfigDiscardUnknownDest_Object((1,3,6,1,4,1,1991,3,4,1,1,2,1,7),_VplsConfigDiscardUnknownDest_Type())
vplsConfigDiscardUnknownDest.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigDiscardUnknownDest.setStatus(_B)
class _VplsConfigMacAging_Type(TruthValue):defaultValue=1
_VplsConfigMacAging_Type.__name__=_F
_VplsConfigMacAging_Object=MibTableColumn
vplsConfigMacAging=_VplsConfigMacAging_Object((1,3,6,1,4,1,1991,3,4,1,1,2,1,8),_VplsConfigMacAging_Type())
vplsConfigMacAging.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigMacAging.setStatus(_B)
class _VplsConfigFwdFullHighWatermark_Type(Unsigned32):defaultValue=95;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VplsConfigFwdFullHighWatermark_Type.__name__=_E
_VplsConfigFwdFullHighWatermark_Object=MibTableColumn
vplsConfigFwdFullHighWatermark=_VplsConfigFwdFullHighWatermark_Object((1,3,6,1,4,1,1991,3,4,1,1,2,1,10),_VplsConfigFwdFullHighWatermark_Type())
vplsConfigFwdFullHighWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigFwdFullHighWatermark.setStatus(_B)
if mibBuilder.loadTexts:vplsConfigFwdFullHighWatermark.setUnits(_T)
class _VplsConfigFwdFullLowWatermark_Type(Unsigned32):defaultValue=90;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VplsConfigFwdFullLowWatermark_Type.__name__=_E
_VplsConfigFwdFullLowWatermark_Object=MibTableColumn
vplsConfigFwdFullLowWatermark=_VplsConfigFwdFullLowWatermark_Object((1,3,6,1,4,1,1991,3,4,1,1,2,1,11),_VplsConfigFwdFullLowWatermark_Type())
vplsConfigFwdFullLowWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigFwdFullLowWatermark.setStatus(_B)
if mibBuilder.loadTexts:vplsConfigFwdFullLowWatermark.setUnits(_T)
_VplsConfigRowStatus_Type=RowStatus
_VplsConfigRowStatus_Object=MibTableColumn
vplsConfigRowStatus=_VplsConfigRowStatus_Object((1,3,6,1,4,1,1991,3,4,1,1,2,1,12),_VplsConfigRowStatus_Type())
vplsConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigRowStatus.setStatus(_B)
class _VplsConfigMtu_Type(Unsigned32):defaultValue=1518;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1518))
_VplsConfigMtu_Type.__name__=_E
_VplsConfigMtu_Object=MibTableColumn
vplsConfigMtu=_VplsConfigMtu_Object((1,3,6,1,4,1,1991,3,4,1,1,2,1,13),_VplsConfigMtu_Type())
vplsConfigMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigMtu.setStatus(_B)
_VplsConfigVpnId_Type=VPNIdOrZero
_VplsConfigVpnId_Object=MibTableColumn
vplsConfigVpnId=_VplsConfigVpnId_Object((1,3,6,1,4,1,1991,3,4,1,1,2,1,14),_VplsConfigVpnId_Type())
vplsConfigVpnId.setMaxAccess(_H)
if mibBuilder.loadTexts:vplsConfigVpnId.setStatus(_B)
class _VplsConfigServiceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan',1),('ethernet',2)))
_VplsConfigServiceType_Type.__name__=_D
_VplsConfigServiceType_Object=MibTableColumn
vplsConfigServiceType=_VplsConfigServiceType_Object((1,3,6,1,4,1,1991,3,4,1,1,2,1,15),_VplsConfigServiceType_Type())
vplsConfigServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigServiceType.setStatus(_B)
class _VplsConfigStorageType_Type(StorageType):defaultValue=2
_VplsConfigStorageType_Type.__name__=_M
_VplsConfigStorageType_Object=MibTableColumn
vplsConfigStorageType=_VplsConfigStorageType_Object((1,3,6,1,4,1,1991,3,4,1,1,2,1,16),_VplsConfigStorageType_Type())
vplsConfigStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigStorageType.setStatus(_B)
_VplsStatusTable_Object=MibTable
vplsStatusTable=_VplsStatusTable_Object((1,3,6,1,4,1,1991,3,4,1,1,3))
if mibBuilder.loadTexts:vplsStatusTable.setStatus(_B)
_VplsStatusEntry_Object=MibTableRow
vplsStatusEntry=_VplsStatusEntry_Object((1,3,6,1,4,1,1991,3,4,1,1,3,1))
vplsStatusEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:vplsStatusEntry.setStatus(_B)
class _VplsStatusOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('other',0),('up',1),('down',2)))
_VplsStatusOperStatus_Type.__name__=_D
_VplsStatusOperStatus_Object=MibTableColumn
vplsStatusOperStatus=_VplsStatusOperStatus_Object((1,3,6,1,4,1,1991,3,4,1,1,3,1,1),_VplsStatusOperStatus_Type())
vplsStatusOperStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:vplsStatusOperStatus.setStatus(_B)
_VplsStatusPeerCount_Type=Counter32
_VplsStatusPeerCount_Object=MibTableColumn
vplsStatusPeerCount=_VplsStatusPeerCount_Object((1,3,6,1,4,1,1991,3,4,1,1,3,1,2),_VplsStatusPeerCount_Type())
vplsStatusPeerCount.setMaxAccess(_H)
if mibBuilder.loadTexts:vplsStatusPeerCount.setStatus(_B)
_VplsPwBindTable_Object=MibTable
vplsPwBindTable=_VplsPwBindTable_Object((1,3,6,1,4,1,1991,3,4,1,1,4))
if mibBuilder.loadTexts:vplsPwBindTable.setStatus(_B)
_VplsPwBindEntry_Object=MibTableRow
vplsPwBindEntry=_VplsPwBindEntry_Object((1,3,6,1,4,1,1991,3,4,1,1,4,1))
vplsPwBindEntry.setIndexNames((0,_A,_I),(0,_A,_U))
if mibBuilder.loadTexts:vplsPwBindEntry.setStatus(_B)
_VplsPwBindIndex_Type=PwIndexType
_VplsPwBindIndex_Object=MibTableColumn
vplsPwBindIndex=_VplsPwBindIndex_Object((1,3,6,1,4,1,1991,3,4,1,1,4,1,1),_VplsPwBindIndex_Type())
vplsPwBindIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:vplsPwBindIndex.setStatus(_B)
class _VplsPwBindConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('autodiscovery',2)))
_VplsPwBindConfigType_Type.__name__=_D
_VplsPwBindConfigType_Object=MibTableColumn
vplsPwBindConfigType=_VplsPwBindConfigType_Object((1,3,6,1,4,1,1991,3,4,1,1,4,1,2),_VplsPwBindConfigType_Type())
vplsPwBindConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindConfigType.setStatus(_B)
class _VplsPwBindType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mesh',1),('spoke',2)))
_VplsPwBindType_Type.__name__=_D
_VplsPwBindType_Object=MibTableColumn
vplsPwBindType=_VplsPwBindType_Object((1,3,6,1,4,1,1991,3,4,1,1,4,1,3),_VplsPwBindType_Type())
vplsPwBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindType.setStatus(_B)
_VplsPwBindRowStatus_Type=RowStatus
_VplsPwBindRowStatus_Object=MibTableColumn
vplsPwBindRowStatus=_VplsPwBindRowStatus_Object((1,3,6,1,4,1,1991,3,4,1,1,4,1,4),_VplsPwBindRowStatus_Type())
vplsPwBindRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindRowStatus.setStatus(_B)
class _VplsPwBindStorageType_Type(StorageType):defaultValue=2
_VplsPwBindStorageType_Type.__name__=_M
_VplsPwBindStorageType_Object=MibTableColumn
vplsPwBindStorageType=_VplsPwBindStorageType_Object((1,3,6,1,4,1,1991,3,4,1,1,4,1,5),_VplsPwBindStorageType_Type())
vplsPwBindStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindStorageType.setStatus(_B)
class _VplsStatusNotifEnable_Type(TruthValue):defaultValue=2
_VplsStatusNotifEnable_Type.__name__=_F
_VplsStatusNotifEnable_Object=MibScalar
vplsStatusNotifEnable=_VplsStatusNotifEnable_Object((1,3,6,1,4,1,1991,3,4,1,1,5),_VplsStatusNotifEnable_Type())
vplsStatusNotifEnable.setMaxAccess(_V)
if mibBuilder.loadTexts:vplsStatusNotifEnable.setStatus(_B)
class _VplsNotificationMaxRate_Type(Unsigned32):defaultValue=0
_VplsNotificationMaxRate_Type.__name__=_E
_VplsNotificationMaxRate_Object=MibScalar
vplsNotificationMaxRate=_VplsNotificationMaxRate_Object((1,3,6,1,4,1,1991,3,4,1,1,6),_VplsNotificationMaxRate_Type())
vplsNotificationMaxRate.setMaxAccess(_V)
if mibBuilder.loadTexts:vplsNotificationMaxRate.setStatus(_B)
_VplsConformance_ObjectIdentity=ObjectIdentity
vplsConformance=_VplsConformance_ObjectIdentity((1,3,6,1,4,1,1991,3,4,1,2))
_VplsCompliances_ObjectIdentity=ObjectIdentity
vplsCompliances=_VplsCompliances_ObjectIdentity((1,3,6,1,4,1,1991,3,4,1,2,1))
_VplsGroups_ObjectIdentity=ObjectIdentity
vplsGroups=_VplsGroups_ObjectIdentity((1,3,6,1,4,1,1991,3,4,1,2,2))
vplsGroup=ObjectGroup((1,3,6,1,4,1,1991,3,4,1,2,2,1))
vplsGroup.setObjects(*((_A,_W),(_A,_X),(_A,_N),(_A,_Y),(_A,_Z),(_A,_a),(_A,_G),(_A,_J),(_A,_K),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_O),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:vplsGroup.setStatus(_B)
vplsPwBindGroup=ObjectGroup((1,3,6,1,4,1,1991,3,4,1,2,2,2))
vplsPwBindGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:vplsPwBindGroup.setStatus(_B)
vplsStatusChanged=NotificationType((1,3,6,1,4,1,1991,3,4,1,0,1))
vplsStatusChanged.setObjects(*((_A,_G),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vplsStatusChanged.setStatus(_B)
vplsFwdFullAlarmRaised=NotificationType((1,3,6,1,4,1,1991,3,4,1,0,2))
vplsFwdFullAlarmRaised.setObjects(*((_A,_G),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:vplsFwdFullAlarmRaised.setStatus(_B)
vplsFwdFullAlarmCleared=NotificationType((1,3,6,1,4,1,1991,3,4,1,0,3))
vplsFwdFullAlarmCleared.setObjects(*((_A,_G),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:vplsFwdFullAlarmCleared.setStatus(_B)
vplsNotificationGroup=NotificationGroup((1,3,6,1,4,1,1991,3,4,1,2,2,3))
vplsNotificationGroup.setObjects(*((_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:vplsNotificationGroup.setStatus(_B)
vplsModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,1991,3,4,1,2,1,1))
vplsModuleFullCompliance.setObjects(*((_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:vplsModuleFullCompliance.setStatus(_B)
vplsModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,1991,3,4,1,2,1,2))
vplsModuleReadOnlyCompliance.setObjects(*((_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:vplsModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'vplsGenericDraft01MIB':vplsGenericDraft01MIB,'vplsNotifications':vplsNotifications,_n:vplsStatusChanged,_o:vplsFwdFullAlarmRaised,_p:vplsFwdFullAlarmCleared,'vplsObjects':vplsObjects,_c:vplsConfigIndexNext,'vplsConfigTable':vplsConfigTable,'vplsConfigEntry':vplsConfigEntry,_I:vplsConfigIndex,_W:vplsConfigName,_X:vplsConfigDescr,_N:vplsConfigAdminStatus,_Y:vplsConfigMacLearning,_Z:vplsConfigDiscardUnknownDest,_a:vplsConfigMacAging,_J:vplsConfigFwdFullHighWatermark,_K:vplsConfigFwdFullLowWatermark,_b:vplsConfigRowStatus,_d:vplsConfigMtu,_G:vplsConfigVpnId,_e:vplsConfigServiceType,_f:vplsConfigStorageType,'vplsStatusTable':vplsStatusTable,'vplsStatusEntry':vplsStatusEntry,_O:vplsStatusOperStatus,_g:vplsStatusPeerCount,'vplsPwBindTable':vplsPwBindTable,'vplsPwBindEntry':vplsPwBindEntry,_U:vplsPwBindIndex,_j:vplsPwBindConfigType,_k:vplsPwBindType,_l:vplsPwBindRowStatus,_m:vplsPwBindStorageType,_h:vplsStatusNotifEnable,_i:vplsNotificationMaxRate,'vplsConformance':vplsConformance,'vplsCompliances':vplsCompliances,'vplsModuleFullCompliance':vplsModuleFullCompliance,'vplsModuleReadOnlyCompliance':vplsModuleReadOnlyCompliance,'vplsGroups':vplsGroups,_P:vplsGroup,_Q:vplsPwBindGroup,_R:vplsNotificationGroup})