_A1='vplsFwdFullAlarmCleared'
_A0='vplsFwdFullAlarmRaised'
_z='vplsStatusChanged'
_y='vplsPwBindStorageType'
_x='vplsPwBindRowStatus'
_w='vplsPwBindType'
_v='vplsPwBindConfigType'
_u='vplsNotificationMaxRate'
_t='vplsStatusNotifEnable'
_s='vplsStatusPeerCount'
_r='vplsConfigSignalingType'
_q='vplsConfigStorageType'
_p='vplsConfigMtu'
_o='vplsConfigIndexNext'
_n='vplsConfigRowStatus'
_m='vplsConfigMacAging'
_l='vplsConfigDiscardUnknownDest'
_k='vplsConfigMacLearning'
_j='vplsConfigDescr'
_i='vplsBgpADConfigStorageType'
_h='vplsBgpADConfigRowStatus'
_g='vplsBgpADConfigVplsId'
_f='vplsBgpADConfigPrefix'
_e='vplsBgpRteTargetStorageType'
_d='vplsBgpRteTargetRowStatus'
_c='vplsBgpRteTargetRT'
_b='vplsBgpRteTargetRTType'
_a='vplsBgpADConfigRouteDistinguisher'
_Z='vplsConfigName'
_Y='vplsStatusEntry'
_X='read-write'
_W='vplsBgpRteTargetIndex'
_V='percentage'
_U='not-accessible'
_T='pwIndex'
_S='PW-STD-MIB'
_R='vplsNotificationGroup'
_Q='vplsPwBindGroup'
_P='vplsGroup'
_O='vplsStatusOperStatus'
_N='vplsConfigAdminStatus'
_M='read-only'
_L='SnmpAdminString'
_K='vplsConfigFwdFullLowWatermark'
_J='vplsConfigFwdFullHighWatermark'
_I='vplsConfigVpnId'
_H='vplsConfigIndex'
_G='TruthValue'
_F='StorageType'
_E='Integer32'
_D='Unsigned32'
_C='read-create'
_B='current'
_A='VPLS-GENERIC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pwIndex,=mibBuilder.importSymbols(_S,_T)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso','transmission')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_F,'TextualConvention',_G)
VPNIdOrZero,=mibBuilder.importSymbols('VPN-TC-STD-MIB','VPNIdOrZero')
vplsGenericMIB=ModuleIdentity((1,3,6,1,2,1,10,274))
if mibBuilder.loadTexts:vplsGenericMIB.setRevisions(('2014-05-19 12:00',))
class VplsBgpRouteDistinguisher(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class VplsBgpRouteTarget(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class VplsBgpRouteTargetType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('import',1),('export',2),('both',3)))
_VplsNotifications_ObjectIdentity=ObjectIdentity
vplsNotifications=_VplsNotifications_ObjectIdentity((1,3,6,1,2,1,10,274,0))
_VplsObjects_ObjectIdentity=ObjectIdentity
vplsObjects=_VplsObjects_ObjectIdentity((1,3,6,1,2,1,10,274,1))
_VplsConfigIndexNext_Type=Unsigned32
_VplsConfigIndexNext_Object=MibScalar
vplsConfigIndexNext=_VplsConfigIndexNext_Object((1,3,6,1,2,1,10,274,1,1),_VplsConfigIndexNext_Type())
vplsConfigIndexNext.setMaxAccess(_M)
if mibBuilder.loadTexts:vplsConfigIndexNext.setStatus(_B)
_VplsConfigTable_Object=MibTable
vplsConfigTable=_VplsConfigTable_Object((1,3,6,1,2,1,10,274,1,2))
if mibBuilder.loadTexts:vplsConfigTable.setStatus(_B)
_VplsConfigEntry_Object=MibTableRow
vplsConfigEntry=_VplsConfigEntry_Object((1,3,6,1,2,1,10,274,1,2,1))
vplsConfigEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:vplsConfigEntry.setStatus(_B)
class _VplsConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VplsConfigIndex_Type.__name__=_D
_VplsConfigIndex_Object=MibTableColumn
vplsConfigIndex=_VplsConfigIndex_Object((1,3,6,1,2,1,10,274,1,2,1,1),_VplsConfigIndex_Type())
vplsConfigIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:vplsConfigIndex.setStatus(_B)
class _VplsConfigName_Type(SnmpAdminString):defaultValue=OctetString('')
_VplsConfigName_Type.__name__=_L
_VplsConfigName_Object=MibTableColumn
vplsConfigName=_VplsConfigName_Object((1,3,6,1,2,1,10,274,1,2,1,2),_VplsConfigName_Type())
vplsConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigName.setStatus(_B)
class _VplsConfigDescr_Type(SnmpAdminString):defaultValue=OctetString('')
_VplsConfigDescr_Type.__name__=_L
_VplsConfigDescr_Object=MibTableColumn
vplsConfigDescr=_VplsConfigDescr_Object((1,3,6,1,2,1,10,274,1,2,1,3),_VplsConfigDescr_Type())
vplsConfigDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigDescr.setStatus(_B)
class _VplsConfigAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_VplsConfigAdminStatus_Type.__name__=_E
_VplsConfigAdminStatus_Object=MibTableColumn
vplsConfigAdminStatus=_VplsConfigAdminStatus_Object((1,3,6,1,2,1,10,274,1,2,1,4),_VplsConfigAdminStatus_Type())
vplsConfigAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigAdminStatus.setStatus(_B)
class _VplsConfigMacLearning_Type(TruthValue):defaultValue=1
_VplsConfigMacLearning_Type.__name__=_G
_VplsConfigMacLearning_Object=MibTableColumn
vplsConfigMacLearning=_VplsConfigMacLearning_Object((1,3,6,1,2,1,10,274,1,2,1,6),_VplsConfigMacLearning_Type())
vplsConfigMacLearning.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigMacLearning.setStatus(_B)
class _VplsConfigDiscardUnknownDest_Type(TruthValue):defaultValue=2
_VplsConfigDiscardUnknownDest_Type.__name__=_G
_VplsConfigDiscardUnknownDest_Object=MibTableColumn
vplsConfigDiscardUnknownDest=_VplsConfigDiscardUnknownDest_Object((1,3,6,1,2,1,10,274,1,2,1,7),_VplsConfigDiscardUnknownDest_Type())
vplsConfigDiscardUnknownDest.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigDiscardUnknownDest.setStatus(_B)
class _VplsConfigMacAging_Type(TruthValue):defaultValue=1
_VplsConfigMacAging_Type.__name__=_G
_VplsConfigMacAging_Object=MibTableColumn
vplsConfigMacAging=_VplsConfigMacAging_Object((1,3,6,1,2,1,10,274,1,2,1,8),_VplsConfigMacAging_Type())
vplsConfigMacAging.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigMacAging.setStatus(_B)
class _VplsConfigFwdFullHighWatermark_Type(Unsigned32):defaultValue=95;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VplsConfigFwdFullHighWatermark_Type.__name__=_D
_VplsConfigFwdFullHighWatermark_Object=MibTableColumn
vplsConfigFwdFullHighWatermark=_VplsConfigFwdFullHighWatermark_Object((1,3,6,1,2,1,10,274,1,2,1,10),_VplsConfigFwdFullHighWatermark_Type())
vplsConfigFwdFullHighWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigFwdFullHighWatermark.setStatus(_B)
if mibBuilder.loadTexts:vplsConfigFwdFullHighWatermark.setUnits(_V)
class _VplsConfigFwdFullLowWatermark_Type(Unsigned32):defaultValue=90;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_VplsConfigFwdFullLowWatermark_Type.__name__=_D
_VplsConfigFwdFullLowWatermark_Object=MibTableColumn
vplsConfigFwdFullLowWatermark=_VplsConfigFwdFullLowWatermark_Object((1,3,6,1,2,1,10,274,1,2,1,11),_VplsConfigFwdFullLowWatermark_Type())
vplsConfigFwdFullLowWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigFwdFullLowWatermark.setStatus(_B)
if mibBuilder.loadTexts:vplsConfigFwdFullLowWatermark.setUnits(_V)
_VplsConfigRowStatus_Type=RowStatus
_VplsConfigRowStatus_Object=MibTableColumn
vplsConfigRowStatus=_VplsConfigRowStatus_Object((1,3,6,1,2,1,10,274,1,2,1,12),_VplsConfigRowStatus_Type())
vplsConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigRowStatus.setStatus(_B)
class _VplsConfigMtu_Type(Unsigned32):defaultValue=1518;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,9192))
_VplsConfigMtu_Type.__name__=_D
_VplsConfigMtu_Object=MibTableColumn
vplsConfigMtu=_VplsConfigMtu_Object((1,3,6,1,2,1,10,274,1,2,1,13),_VplsConfigMtu_Type())
vplsConfigMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigMtu.setStatus(_B)
_VplsConfigVpnId_Type=VPNIdOrZero
_VplsConfigVpnId_Object=MibTableColumn
vplsConfigVpnId=_VplsConfigVpnId_Object((1,3,6,1,2,1,10,274,1,2,1,14),_VplsConfigVpnId_Type())
vplsConfigVpnId.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigVpnId.setStatus(_B)
class _VplsConfigStorageType_Type(StorageType):defaultValue=3
_VplsConfigStorageType_Type.__name__=_F
_VplsConfigStorageType_Object=MibTableColumn
vplsConfigStorageType=_VplsConfigStorageType_Object((1,3,6,1,2,1,10,274,1,2,1,15),_VplsConfigStorageType_Type())
vplsConfigStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigStorageType.setStatus(_B)
class _VplsConfigSignalingType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ldp',1),('bgp',2),('none',3)))
_VplsConfigSignalingType_Type.__name__=_E
_VplsConfigSignalingType_Object=MibTableColumn
vplsConfigSignalingType=_VplsConfigSignalingType_Object((1,3,6,1,2,1,10,274,1,2,1,16),_VplsConfigSignalingType_Type())
vplsConfigSignalingType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigSignalingType.setStatus(_B)
_VplsStatusTable_Object=MibTable
vplsStatusTable=_VplsStatusTable_Object((1,3,6,1,2,1,10,274,1,3))
if mibBuilder.loadTexts:vplsStatusTable.setStatus(_B)
_VplsStatusEntry_Object=MibTableRow
vplsStatusEntry=_VplsStatusEntry_Object((1,3,6,1,2,1,10,274,1,3,1))
if mibBuilder.loadTexts:vplsStatusEntry.setStatus(_B)
class _VplsStatusOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('other',0),('up',1),('down',2)))
_VplsStatusOperStatus_Type.__name__=_E
_VplsStatusOperStatus_Object=MibTableColumn
vplsStatusOperStatus=_VplsStatusOperStatus_Object((1,3,6,1,2,1,10,274,1,3,1,1),_VplsStatusOperStatus_Type())
vplsStatusOperStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:vplsStatusOperStatus.setStatus(_B)
_VplsStatusPeerCount_Type=Counter32
_VplsStatusPeerCount_Object=MibTableColumn
vplsStatusPeerCount=_VplsStatusPeerCount_Object((1,3,6,1,2,1,10,274,1,3,1,2),_VplsStatusPeerCount_Type())
vplsStatusPeerCount.setMaxAccess(_M)
if mibBuilder.loadTexts:vplsStatusPeerCount.setStatus(_B)
_VplsPwBindTable_Object=MibTable
vplsPwBindTable=_VplsPwBindTable_Object((1,3,6,1,2,1,10,274,1,4))
if mibBuilder.loadTexts:vplsPwBindTable.setStatus(_B)
_VplsPwBindEntry_Object=MibTableRow
vplsPwBindEntry=_VplsPwBindEntry_Object((1,3,6,1,2,1,10,274,1,4,1))
vplsPwBindEntry.setIndexNames((0,_A,_H),(0,_S,_T))
if mibBuilder.loadTexts:vplsPwBindEntry.setStatus(_B)
class _VplsPwBindConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('autodiscovery',2)))
_VplsPwBindConfigType_Type.__name__=_E
_VplsPwBindConfigType_Object=MibTableColumn
vplsPwBindConfigType=_VplsPwBindConfigType_Object((1,3,6,1,2,1,10,274,1,4,1,1),_VplsPwBindConfigType_Type())
vplsPwBindConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindConfigType.setStatus(_B)
class _VplsPwBindType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mesh',1),('spoke',2)))
_VplsPwBindType_Type.__name__=_E
_VplsPwBindType_Object=MibTableColumn
vplsPwBindType=_VplsPwBindType_Object((1,3,6,1,2,1,10,274,1,4,1,2),_VplsPwBindType_Type())
vplsPwBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindType.setStatus(_B)
_VplsPwBindRowStatus_Type=RowStatus
_VplsPwBindRowStatus_Object=MibTableColumn
vplsPwBindRowStatus=_VplsPwBindRowStatus_Object((1,3,6,1,2,1,10,274,1,4,1,3),_VplsPwBindRowStatus_Type())
vplsPwBindRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindRowStatus.setStatus(_B)
class _VplsPwBindStorageType_Type(StorageType):defaultValue=2
_VplsPwBindStorageType_Type.__name__=_F
_VplsPwBindStorageType_Object=MibTableColumn
vplsPwBindStorageType=_VplsPwBindStorageType_Object((1,3,6,1,2,1,10,274,1,4,1,4),_VplsPwBindStorageType_Type())
vplsPwBindStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindStorageType.setStatus(_B)
_VplsBgpADConfigTable_Object=MibTable
vplsBgpADConfigTable=_VplsBgpADConfigTable_Object((1,3,6,1,2,1,10,274,1,5))
if mibBuilder.loadTexts:vplsBgpADConfigTable.setStatus(_B)
_VplsBgpADConfigEntry_Object=MibTableRow
vplsBgpADConfigEntry=_VplsBgpADConfigEntry_Object((1,3,6,1,2,1,10,274,1,5,1))
vplsBgpADConfigEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:vplsBgpADConfigEntry.setStatus(_B)
_VplsBgpADConfigRouteDistinguisher_Type=VplsBgpRouteDistinguisher
_VplsBgpADConfigRouteDistinguisher_Object=MibTableColumn
vplsBgpADConfigRouteDistinguisher=_VplsBgpADConfigRouteDistinguisher_Object((1,3,6,1,2,1,10,274,1,5,1,1),_VplsBgpADConfigRouteDistinguisher_Type())
vplsBgpADConfigRouteDistinguisher.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpADConfigRouteDistinguisher.setStatus(_B)
class _VplsBgpADConfigPrefix_Type(Unsigned32):defaultValue=0
_VplsBgpADConfigPrefix_Type.__name__=_D
_VplsBgpADConfigPrefix_Object=MibTableColumn
vplsBgpADConfigPrefix=_VplsBgpADConfigPrefix_Object((1,3,6,1,2,1,10,274,1,5,1,2),_VplsBgpADConfigPrefix_Type())
vplsBgpADConfigPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpADConfigPrefix.setStatus(_B)
_VplsBgpADConfigVplsId_Type=VplsBgpRouteDistinguisher
_VplsBgpADConfigVplsId_Object=MibTableColumn
vplsBgpADConfigVplsId=_VplsBgpADConfigVplsId_Object((1,3,6,1,2,1,10,274,1,5,1,3),_VplsBgpADConfigVplsId_Type())
vplsBgpADConfigVplsId.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpADConfigVplsId.setStatus(_B)
_VplsBgpADConfigRowStatus_Type=RowStatus
_VplsBgpADConfigRowStatus_Object=MibTableColumn
vplsBgpADConfigRowStatus=_VplsBgpADConfigRowStatus_Object((1,3,6,1,2,1,10,274,1,5,1,4),_VplsBgpADConfigRowStatus_Type())
vplsBgpADConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpADConfigRowStatus.setStatus(_B)
class _VplsBgpADConfigStorageType_Type(StorageType):defaultValue=3
_VplsBgpADConfigStorageType_Type.__name__=_F
_VplsBgpADConfigStorageType_Object=MibTableColumn
vplsBgpADConfigStorageType=_VplsBgpADConfigStorageType_Object((1,3,6,1,2,1,10,274,1,5,1,5),_VplsBgpADConfigStorageType_Type())
vplsBgpADConfigStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpADConfigStorageType.setStatus(_B)
_VplsBgpRteTargetTable_Object=MibTable
vplsBgpRteTargetTable=_VplsBgpRteTargetTable_Object((1,3,6,1,2,1,10,274,1,6))
if mibBuilder.loadTexts:vplsBgpRteTargetTable.setStatus(_B)
_VplsBgpRteTargetEntry_Object=MibTableRow
vplsBgpRteTargetEntry=_VplsBgpRteTargetEntry_Object((1,3,6,1,2,1,10,274,1,6,1))
vplsBgpRteTargetEntry.setIndexNames((0,_A,_H),(0,_A,_W))
if mibBuilder.loadTexts:vplsBgpRteTargetEntry.setStatus(_B)
_VplsBgpRteTargetIndex_Type=Unsigned32
_VplsBgpRteTargetIndex_Object=MibTableColumn
vplsBgpRteTargetIndex=_VplsBgpRteTargetIndex_Object((1,3,6,1,2,1,10,274,1,6,1,1),_VplsBgpRteTargetIndex_Type())
vplsBgpRteTargetIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:vplsBgpRteTargetIndex.setStatus(_B)
_VplsBgpRteTargetRTType_Type=VplsBgpRouteTargetType
_VplsBgpRteTargetRTType_Object=MibTableColumn
vplsBgpRteTargetRTType=_VplsBgpRteTargetRTType_Object((1,3,6,1,2,1,10,274,1,6,1,2),_VplsBgpRteTargetRTType_Type())
vplsBgpRteTargetRTType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpRteTargetRTType.setStatus(_B)
_VplsBgpRteTargetRT_Type=VplsBgpRouteTarget
_VplsBgpRteTargetRT_Object=MibTableColumn
vplsBgpRteTargetRT=_VplsBgpRteTargetRT_Object((1,3,6,1,2,1,10,274,1,6,1,3),_VplsBgpRteTargetRT_Type())
vplsBgpRteTargetRT.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpRteTargetRT.setStatus(_B)
_VplsBgpRteTargetRowStatus_Type=RowStatus
_VplsBgpRteTargetRowStatus_Object=MibTableColumn
vplsBgpRteTargetRowStatus=_VplsBgpRteTargetRowStatus_Object((1,3,6,1,2,1,10,274,1,6,1,4),_VplsBgpRteTargetRowStatus_Type())
vplsBgpRteTargetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpRteTargetRowStatus.setStatus(_B)
class _VplsBgpRteTargetStorageType_Type(StorageType):defaultValue=2
_VplsBgpRteTargetStorageType_Type.__name__=_F
_VplsBgpRteTargetStorageType_Object=MibTableColumn
vplsBgpRteTargetStorageType=_VplsBgpRteTargetStorageType_Object((1,3,6,1,2,1,10,274,1,6,1,5),_VplsBgpRteTargetStorageType_Type())
vplsBgpRteTargetStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpRteTargetStorageType.setStatus(_B)
class _VplsStatusNotifEnable_Type(TruthValue):defaultValue=2
_VplsStatusNotifEnable_Type.__name__=_G
_VplsStatusNotifEnable_Object=MibScalar
vplsStatusNotifEnable=_VplsStatusNotifEnable_Object((1,3,6,1,2,1,10,274,1,7),_VplsStatusNotifEnable_Type())
vplsStatusNotifEnable.setMaxAccess(_X)
if mibBuilder.loadTexts:vplsStatusNotifEnable.setStatus(_B)
class _VplsNotificationMaxRate_Type(Unsigned32):defaultValue=0
_VplsNotificationMaxRate_Type.__name__=_D
_VplsNotificationMaxRate_Object=MibScalar
vplsNotificationMaxRate=_VplsNotificationMaxRate_Object((1,3,6,1,2,1,10,274,1,8),_VplsNotificationMaxRate_Type())
vplsNotificationMaxRate.setMaxAccess(_X)
if mibBuilder.loadTexts:vplsNotificationMaxRate.setStatus(_B)
_VplsConformance_ObjectIdentity=ObjectIdentity
vplsConformance=_VplsConformance_ObjectIdentity((1,3,6,1,2,1,10,274,2))
_VplsCompliances_ObjectIdentity=ObjectIdentity
vplsCompliances=_VplsCompliances_ObjectIdentity((1,3,6,1,2,1,10,274,2,1))
_VplsGroups_ObjectIdentity=ObjectIdentity
vplsGroups=_VplsGroups_ObjectIdentity((1,3,6,1,2,1,10,274,2,2))
vplsConfigEntry.registerAugmentions((_A,_Y))
vplsStatusEntry.setIndexNames(*vplsConfigEntry.getIndexNames())
vplsGroup=ObjectGroup((1,3,6,1,2,1,10,274,2,2,1))
vplsGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_N),(_A,_k),(_A,_l),(_A,_m),(_A,_I),(_A,_J),(_A,_K),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_O),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:vplsGroup.setStatus(_B)
vplsPwBindGroup=ObjectGroup((1,3,6,1,2,1,10,274,2,2,2))
vplsPwBindGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:vplsPwBindGroup.setStatus(_B)
vplsStatusChanged=NotificationType((1,3,6,1,2,1,10,274,0,1))
vplsStatusChanged.setObjects(*((_A,_I),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vplsStatusChanged.setStatus(_B)
vplsFwdFullAlarmRaised=NotificationType((1,3,6,1,2,1,10,274,0,2))
vplsFwdFullAlarmRaised.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:vplsFwdFullAlarmRaised.setStatus(_B)
vplsFwdFullAlarmCleared=NotificationType((1,3,6,1,2,1,10,274,0,3))
vplsFwdFullAlarmCleared.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:vplsFwdFullAlarmCleared.setStatus(_B)
vplsNotificationGroup=NotificationGroup((1,3,6,1,2,1,10,274,2,2,3))
vplsNotificationGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:vplsNotificationGroup.setStatus(_B)
vplsModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,10,274,2,1,1))
vplsModuleFullCompliance.setObjects(*((_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:vplsModuleFullCompliance.setStatus(_B)
vplsModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,10,274,2,1,2))
vplsModuleReadOnlyCompliance.setObjects(*((_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:vplsModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'VplsBgpRouteDistinguisher':VplsBgpRouteDistinguisher,'VplsBgpRouteTarget':VplsBgpRouteTarget,'VplsBgpRouteTargetType':VplsBgpRouteTargetType,'vplsGenericMIB':vplsGenericMIB,'vplsNotifications':vplsNotifications,_z:vplsStatusChanged,_A0:vplsFwdFullAlarmRaised,_A1:vplsFwdFullAlarmCleared,'vplsObjects':vplsObjects,_o:vplsConfigIndexNext,'vplsConfigTable':vplsConfigTable,'vplsConfigEntry':vplsConfigEntry,_H:vplsConfigIndex,_Z:vplsConfigName,_j:vplsConfigDescr,_N:vplsConfigAdminStatus,_k:vplsConfigMacLearning,_l:vplsConfigDiscardUnknownDest,_m:vplsConfigMacAging,_J:vplsConfigFwdFullHighWatermark,_K:vplsConfigFwdFullLowWatermark,_n:vplsConfigRowStatus,_p:vplsConfigMtu,_I:vplsConfigVpnId,_q:vplsConfigStorageType,_r:vplsConfigSignalingType,'vplsStatusTable':vplsStatusTable,_Y:vplsStatusEntry,_O:vplsStatusOperStatus,_s:vplsStatusPeerCount,'vplsPwBindTable':vplsPwBindTable,'vplsPwBindEntry':vplsPwBindEntry,_v:vplsPwBindConfigType,_w:vplsPwBindType,_x:vplsPwBindRowStatus,_y:vplsPwBindStorageType,'vplsBgpADConfigTable':vplsBgpADConfigTable,'vplsBgpADConfigEntry':vplsBgpADConfigEntry,_a:vplsBgpADConfigRouteDistinguisher,_f:vplsBgpADConfigPrefix,_g:vplsBgpADConfigVplsId,_h:vplsBgpADConfigRowStatus,_i:vplsBgpADConfigStorageType,'vplsBgpRteTargetTable':vplsBgpRteTargetTable,'vplsBgpRteTargetEntry':vplsBgpRteTargetEntry,_W:vplsBgpRteTargetIndex,_b:vplsBgpRteTargetRTType,_c:vplsBgpRteTargetRT,_d:vplsBgpRteTargetRowStatus,_e:vplsBgpRteTargetStorageType,_t:vplsStatusNotifEnable,_u:vplsNotificationMaxRate,'vplsConformance':vplsConformance,'vplsCompliances':vplsCompliances,'vplsModuleFullCompliance':vplsModuleFullCompliance,'vplsModuleReadOnlyCompliance':vplsModuleReadOnlyCompliance,'vplsGroups':vplsGroups,_P:vplsGroup,_Q:vplsPwBindGroup,_R:vplsNotificationGroup})