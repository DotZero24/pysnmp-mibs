_o='vplsFwdFullAlarmCleared'
_n='vplsFwdFullAlarmRaised'
_m='vplsStatusChanged'
_l='vplsPwBindStorageType'
_k='vplsPwBindRowStatus'
_j='vplsPwBindType'
_i='vplsPwBindConfigType'
_h='vplsNotificationMaxRate'
_g='vplsStatusNotifEnable'
_f='vplsStatusPeerCount'
_e='vplsConfigStorageType'
_d='vplsConfigMtu'
_c='vplsConfigIndexNext'
_b='vplsConfigRowStatus'
_a='vplsConfigMacAging'
_Z='vplsConfigDiscardUnknownDest'
_Y='vplsConfigMacLearning'
_X='vplsConfigDescr'
_W='vplsConfigName'
_V='read-write'
_U='percentage'
_T='pwIndex'
_S='PW-STD-MIB'
_R='vplsNotificationGroup'
_Q='vplsPwBindGroup'
_P='vplsGroup'
_O='vplsStatusOperStatus'
_N='vplsConfigAdminStatus'
_M='StorageType'
_L='SnmpAdminString'
_K='vplsConfigFwdFullLowWatermark'
_J='vplsConfigFwdFullHighWatermark'
_I='read-only'
_H='vplsConfigVpnId'
_G='vplsConfigIndex'
_F='TruthValue'
_E='Integer32'
_D='Unsigned32'
_C='read-create'
_B='DGS-6600-VPLS-GENERIC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dgs6600_mpls,=mibBuilder.importSymbols('DGS-6600-ID-MIB','dgs6600-mpls')
pwIndex,=mibBuilder.importSymbols(_S,_T)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso','transmission')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_M,'TextualConvention',_F)
VPNIdOrZero,=mibBuilder.importSymbols('VPN-TC-STD-MIB','VPNIdOrZero')
dgs6600VplsGenericMIB=ModuleIdentity((1,3,6,1,4,1,171,10,120,100,4,1))
if mibBuilder.loadTexts:dgs6600VplsGenericMIB.setRevisions(('2012-09-29 12:00','2006-06-04 12:00'))
class VplsBgpRouteDistinguisher(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class VplsBgpRouteTarget(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class VplsBgpRouteTargetType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('import',1),('export',2),('both',3)))
_VplsNotifications_ObjectIdentity=ObjectIdentity
vplsNotifications=_VplsNotifications_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,4,1,0))
_VplsObjects_ObjectIdentity=ObjectIdentity
vplsObjects=_VplsObjects_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,4,1,1))
_VplsConfigIndexNext_Type=Unsigned32
_VplsConfigIndexNext_Object=MibScalar
vplsConfigIndexNext=_VplsConfigIndexNext_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,1),_VplsConfigIndexNext_Type())
vplsConfigIndexNext.setMaxAccess(_I)
if mibBuilder.loadTexts:vplsConfigIndexNext.setStatus(_A)
_VplsConfigTable_Object=MibTable
vplsConfigTable=_VplsConfigTable_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,2))
if mibBuilder.loadTexts:vplsConfigTable.setStatus(_A)
_VplsConfigEntry_Object=MibTableRow
vplsConfigEntry=_VplsConfigEntry_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,2,1))
vplsConfigEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:vplsConfigEntry.setStatus(_A)
class _VplsConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VplsConfigIndex_Type.__name__=_D
_VplsConfigIndex_Object=MibTableColumn
vplsConfigIndex=_VplsConfigIndex_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,2,1,1),_VplsConfigIndex_Type())
vplsConfigIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:vplsConfigIndex.setStatus(_A)
class _VplsConfigName_Type(SnmpAdminString):defaultValue=OctetString('')
_VplsConfigName_Type.__name__=_L
_VplsConfigName_Object=MibTableColumn
vplsConfigName=_VplsConfigName_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,2,1,2),_VplsConfigName_Type())
vplsConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigName.setStatus(_A)
class _VplsConfigDescr_Type(SnmpAdminString):defaultValue=OctetString('')
_VplsConfigDescr_Type.__name__=_L
_VplsConfigDescr_Object=MibTableColumn
vplsConfigDescr=_VplsConfigDescr_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,2,1,3),_VplsConfigDescr_Type())
vplsConfigDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigDescr.setStatus(_A)
class _VplsConfigAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_VplsConfigAdminStatus_Type.__name__=_E
_VplsConfigAdminStatus_Object=MibTableColumn
vplsConfigAdminStatus=_VplsConfigAdminStatus_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,2,1,4),_VplsConfigAdminStatus_Type())
vplsConfigAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigAdminStatus.setStatus(_A)
class _VplsConfigMacLearning_Type(TruthValue):defaultValue=1
_VplsConfigMacLearning_Type.__name__=_F
_VplsConfigMacLearning_Object=MibTableColumn
vplsConfigMacLearning=_VplsConfigMacLearning_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,2,1,6),_VplsConfigMacLearning_Type())
vplsConfigMacLearning.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigMacLearning.setStatus(_A)
class _VplsConfigDiscardUnknownDest_Type(TruthValue):defaultValue=2
_VplsConfigDiscardUnknownDest_Type.__name__=_F
_VplsConfigDiscardUnknownDest_Object=MibTableColumn
vplsConfigDiscardUnknownDest=_VplsConfigDiscardUnknownDest_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,2,1,7),_VplsConfigDiscardUnknownDest_Type())
vplsConfigDiscardUnknownDest.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigDiscardUnknownDest.setStatus(_A)
class _VplsConfigMacAging_Type(TruthValue):defaultValue=1
_VplsConfigMacAging_Type.__name__=_F
_VplsConfigMacAging_Object=MibTableColumn
vplsConfigMacAging=_VplsConfigMacAging_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,2,1,8),_VplsConfigMacAging_Type())
vplsConfigMacAging.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigMacAging.setStatus(_A)
class _VplsConfigFwdFullHighWatermark_Type(Unsigned32):defaultValue=95;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VplsConfigFwdFullHighWatermark_Type.__name__=_D
_VplsConfigFwdFullHighWatermark_Object=MibTableColumn
vplsConfigFwdFullHighWatermark=_VplsConfigFwdFullHighWatermark_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,2,1,10),_VplsConfigFwdFullHighWatermark_Type())
vplsConfigFwdFullHighWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigFwdFullHighWatermark.setStatus(_A)
if mibBuilder.loadTexts:vplsConfigFwdFullHighWatermark.setUnits(_U)
class _VplsConfigFwdFullLowWatermark_Type(Unsigned32):defaultValue=90;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VplsConfigFwdFullLowWatermark_Type.__name__=_D
_VplsConfigFwdFullLowWatermark_Object=MibTableColumn
vplsConfigFwdFullLowWatermark=_VplsConfigFwdFullLowWatermark_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,2,1,11),_VplsConfigFwdFullLowWatermark_Type())
vplsConfigFwdFullLowWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigFwdFullLowWatermark.setStatus(_A)
if mibBuilder.loadTexts:vplsConfigFwdFullLowWatermark.setUnits(_U)
_VplsConfigRowStatus_Type=RowStatus
_VplsConfigRowStatus_Object=MibTableColumn
vplsConfigRowStatus=_VplsConfigRowStatus_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,2,1,12),_VplsConfigRowStatus_Type())
vplsConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigRowStatus.setStatus(_A)
class _VplsConfigMtu_Type(Unsigned32):defaultValue=1518;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,9192))
_VplsConfigMtu_Type.__name__=_D
_VplsConfigMtu_Object=MibTableColumn
vplsConfigMtu=_VplsConfigMtu_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,2,1,13),_VplsConfigMtu_Type())
vplsConfigMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigMtu.setStatus(_A)
_VplsConfigVpnId_Type=VPNIdOrZero
_VplsConfigVpnId_Object=MibTableColumn
vplsConfigVpnId=_VplsConfigVpnId_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,2,1,14),_VplsConfigVpnId_Type())
vplsConfigVpnId.setMaxAccess(_I)
if mibBuilder.loadTexts:vplsConfigVpnId.setStatus(_A)
class _VplsConfigStorageType_Type(StorageType):defaultValue=3
_VplsConfigStorageType_Type.__name__=_M
_VplsConfigStorageType_Object=MibTableColumn
vplsConfigStorageType=_VplsConfigStorageType_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,2,1,15),_VplsConfigStorageType_Type())
vplsConfigStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigStorageType.setStatus(_A)
_VplsStatusTable_Object=MibTable
vplsStatusTable=_VplsStatusTable_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,3))
if mibBuilder.loadTexts:vplsStatusTable.setStatus(_A)
_VplsStatusEntry_Object=MibTableRow
vplsStatusEntry=_VplsStatusEntry_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,3,1))
vplsStatusEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:vplsStatusEntry.setStatus(_A)
class _VplsStatusOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('other',0),('up',1),('down',2)))
_VplsStatusOperStatus_Type.__name__=_E
_VplsStatusOperStatus_Object=MibTableColumn
vplsStatusOperStatus=_VplsStatusOperStatus_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,3,1,1),_VplsStatusOperStatus_Type())
vplsStatusOperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:vplsStatusOperStatus.setStatus(_A)
_VplsStatusPeerCount_Type=Counter32
_VplsStatusPeerCount_Object=MibTableColumn
vplsStatusPeerCount=_VplsStatusPeerCount_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,3,1,2),_VplsStatusPeerCount_Type())
vplsStatusPeerCount.setMaxAccess(_I)
if mibBuilder.loadTexts:vplsStatusPeerCount.setStatus(_A)
_VplsPwBindTable_Object=MibTable
vplsPwBindTable=_VplsPwBindTable_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,4))
if mibBuilder.loadTexts:vplsPwBindTable.setStatus(_A)
_VplsPwBindEntry_Object=MibTableRow
vplsPwBindEntry=_VplsPwBindEntry_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,4,1))
vplsPwBindEntry.setIndexNames((0,_B,_G),(0,_S,_T))
if mibBuilder.loadTexts:vplsPwBindEntry.setStatus(_A)
class _VplsPwBindConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('autodiscovery',2)))
_VplsPwBindConfigType_Type.__name__=_E
_VplsPwBindConfigType_Object=MibTableColumn
vplsPwBindConfigType=_VplsPwBindConfigType_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,4,1,1),_VplsPwBindConfigType_Type())
vplsPwBindConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindConfigType.setStatus(_A)
class _VplsPwBindType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mesh',1),('spoke',2)))
_VplsPwBindType_Type.__name__=_E
_VplsPwBindType_Object=MibTableColumn
vplsPwBindType=_VplsPwBindType_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,4,1,2),_VplsPwBindType_Type())
vplsPwBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindType.setStatus(_A)
_VplsPwBindRowStatus_Type=RowStatus
_VplsPwBindRowStatus_Object=MibTableColumn
vplsPwBindRowStatus=_VplsPwBindRowStatus_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,4,1,3),_VplsPwBindRowStatus_Type())
vplsPwBindRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindRowStatus.setStatus(_A)
class _VplsPwBindStorageType_Type(StorageType):defaultValue=2
_VplsPwBindStorageType_Type.__name__=_M
_VplsPwBindStorageType_Object=MibTableColumn
vplsPwBindStorageType=_VplsPwBindStorageType_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,4,1,4),_VplsPwBindStorageType_Type())
vplsPwBindStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindStorageType.setStatus(_A)
_VplsBgpADConfigTable_Object=MibTable
vplsBgpADConfigTable=_VplsBgpADConfigTable_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,5))
if mibBuilder.loadTexts:vplsBgpADConfigTable.setStatus(_A)
_VplsBgpADConfigEntry_Object=MibTableRow
vplsBgpADConfigEntry=_VplsBgpADConfigEntry_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,5,1))
vplsBgpADConfigEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:vplsBgpADConfigEntry.setStatus(_A)
_VplsBgpADConfigRouteDistinguisher_Type=VplsBgpRouteDistinguisher
_VplsBgpADConfigRouteDistinguisher_Object=MibTableColumn
vplsBgpADConfigRouteDistinguisher=_VplsBgpADConfigRouteDistinguisher_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,5,1,1),_VplsBgpADConfigRouteDistinguisher_Type())
vplsBgpADConfigRouteDistinguisher.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpADConfigRouteDistinguisher.setStatus(_A)
class _VplsBgpADConfigPrefix_Type(Unsigned32):defaultValue=0
_VplsBgpADConfigPrefix_Type.__name__=_D
_VplsBgpADConfigPrefix_Object=MibTableColumn
vplsBgpADConfigPrefix=_VplsBgpADConfigPrefix_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,5,1,2),_VplsBgpADConfigPrefix_Type())
vplsBgpADConfigPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpADConfigPrefix.setStatus(_A)
_VplsBgpADConfigVplsId_Type=VplsBgpRouteDistinguisher
_VplsBgpADConfigVplsId_Object=MibTableColumn
vplsBgpADConfigVplsId=_VplsBgpADConfigVplsId_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,5,1,3),_VplsBgpADConfigVplsId_Type())
vplsBgpADConfigVplsId.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpADConfigVplsId.setStatus(_A)
_VplsBgpADConfigRowStatus_Type=RowStatus
_VplsBgpADConfigRowStatus_Object=MibTableColumn
vplsBgpADConfigRowStatus=_VplsBgpADConfigRowStatus_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,5,1,4),_VplsBgpADConfigRowStatus_Type())
vplsBgpADConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpADConfigRowStatus.setStatus(_A)
class _VplsStatusNotifEnable_Type(TruthValue):defaultValue=2
_VplsStatusNotifEnable_Type.__name__=_F
_VplsStatusNotifEnable_Object=MibScalar
vplsStatusNotifEnable=_VplsStatusNotifEnable_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,7),_VplsStatusNotifEnable_Type())
vplsStatusNotifEnable.setMaxAccess(_V)
if mibBuilder.loadTexts:vplsStatusNotifEnable.setStatus(_A)
class _VplsNotificationMaxRate_Type(Unsigned32):defaultValue=0
_VplsNotificationMaxRate_Type.__name__=_D
_VplsNotificationMaxRate_Object=MibScalar
vplsNotificationMaxRate=_VplsNotificationMaxRate_Object((1,3,6,1,4,1,171,10,120,100,4,1,1,8),_VplsNotificationMaxRate_Type())
vplsNotificationMaxRate.setMaxAccess(_V)
if mibBuilder.loadTexts:vplsNotificationMaxRate.setStatus(_A)
_VplsConformance_ObjectIdentity=ObjectIdentity
vplsConformance=_VplsConformance_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,4,1,2))
_VplsCompliances_ObjectIdentity=ObjectIdentity
vplsCompliances=_VplsCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,4,1,2,1))
_VplsGroups_ObjectIdentity=ObjectIdentity
vplsGroups=_VplsGroups_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,4,1,2,2))
vplsGroup=ObjectGroup((1,3,6,1,4,1,171,10,120,100,4,1,2,2,1))
vplsGroup.setObjects(*((_B,_W),(_B,_X),(_B,_N),(_B,_Y),(_B,_Z),(_B,_a),(_B,_H),(_B,_J),(_B,_K),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_O),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:vplsGroup.setStatus(_A)
vplsPwBindGroup=ObjectGroup((1,3,6,1,4,1,171,10,120,100,4,1,2,2,2))
vplsPwBindGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:vplsPwBindGroup.setStatus(_A)
vplsStatusChanged=NotificationType((1,3,6,1,4,1,171,10,120,100,4,1,0,1))
vplsStatusChanged.setObjects(*((_B,_H),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:vplsStatusChanged.setStatus(_A)
vplsFwdFullAlarmRaised=NotificationType((1,3,6,1,4,1,171,10,120,100,4,1,0,2))
vplsFwdFullAlarmRaised.setObjects(*((_B,_H),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:vplsFwdFullAlarmRaised.setStatus(_A)
vplsFwdFullAlarmCleared=NotificationType((1,3,6,1,4,1,171,10,120,100,4,1,0,3))
vplsFwdFullAlarmCleared.setObjects(*((_B,_H),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:vplsFwdFullAlarmCleared.setStatus(_A)
vplsNotificationGroup=NotificationGroup((1,3,6,1,4,1,171,10,120,100,4,1,2,2,3))
vplsNotificationGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:vplsNotificationGroup.setStatus(_A)
vplsModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,120,100,4,1,2,1,1))
vplsModuleFullCompliance.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:vplsModuleFullCompliance.setStatus(_A)
vplsModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,120,100,4,1,2,1,2))
vplsModuleReadOnlyCompliance.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:vplsModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VplsBgpRouteDistinguisher':VplsBgpRouteDistinguisher,'VplsBgpRouteTarget':VplsBgpRouteTarget,'VplsBgpRouteTargetType':VplsBgpRouteTargetType,'dgs6600VplsGenericMIB':dgs6600VplsGenericMIB,'vplsNotifications':vplsNotifications,_m:vplsStatusChanged,_n:vplsFwdFullAlarmRaised,_o:vplsFwdFullAlarmCleared,'vplsObjects':vplsObjects,_c:vplsConfigIndexNext,'vplsConfigTable':vplsConfigTable,'vplsConfigEntry':vplsConfigEntry,_G:vplsConfigIndex,_W:vplsConfigName,_X:vplsConfigDescr,_N:vplsConfigAdminStatus,_Y:vplsConfigMacLearning,_Z:vplsConfigDiscardUnknownDest,_a:vplsConfigMacAging,_J:vplsConfigFwdFullHighWatermark,_K:vplsConfigFwdFullLowWatermark,_b:vplsConfigRowStatus,_d:vplsConfigMtu,_H:vplsConfigVpnId,_e:vplsConfigStorageType,'vplsStatusTable':vplsStatusTable,'vplsStatusEntry':vplsStatusEntry,_O:vplsStatusOperStatus,_f:vplsStatusPeerCount,'vplsPwBindTable':vplsPwBindTable,'vplsPwBindEntry':vplsPwBindEntry,_i:vplsPwBindConfigType,_j:vplsPwBindType,_k:vplsPwBindRowStatus,_l:vplsPwBindStorageType,'vplsBgpADConfigTable':vplsBgpADConfigTable,'vplsBgpADConfigEntry':vplsBgpADConfigEntry,'vplsBgpADConfigRouteDistinguisher':vplsBgpADConfigRouteDistinguisher,'vplsBgpADConfigPrefix':vplsBgpADConfigPrefix,'vplsBgpADConfigVplsId':vplsBgpADConfigVplsId,'vplsBgpADConfigRowStatus':vplsBgpADConfigRowStatus,_g:vplsStatusNotifEnable,_h:vplsNotificationMaxRate,'vplsConformance':vplsConformance,'vplsCompliances':vplsCompliances,'vplsModuleFullCompliance':vplsModuleFullCompliance,'vplsModuleReadOnlyCompliance':vplsModuleReadOnlyCompliance,'vplsGroups':vplsGroups,_P:vplsGroup,_Q:vplsPwBindGroup,_R:vplsNotificationGroup})