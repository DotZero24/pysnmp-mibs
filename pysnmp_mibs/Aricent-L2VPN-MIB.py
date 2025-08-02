_AH='vplsFwdFullAlarmCleared'
_AG='vplsFwdFullAlarmRaised'
_AF='vplsStatusChanged'
_AE='fsL2VpnPwRedPwRemoteStatus'
_AD='fsL2VpnPwRedPwLocalStatus'
_AC='fsL2VpnPwRedGroupOperActivePw'
_AB='fsL2VpnPwRedGroupAdminActivePw'
_AA='vplsPwBindStorageType'
_A9='vplsPwBindRowStatus'
_A8='vplsPwBindType'
_A7='vplsPwBindConfigType'
_A6='vplsNotificationMaxRate'
_A5='vplsStatusNotifEnable'
_A4='vplsStatusPeerCount'
_A3='vplsConfigSignalingType'
_A2='vplsConfigStorageType'
_A1='vplsConfigMtu'
_A0='vplsConfigIndexNext'
_z='vplsConfigRowStatus'
_y='vplsConfigMacAging'
_x='vplsConfigDiscardUnknownDest'
_w='vplsConfigMacLearning'
_v='vplsConfigDescr'
_u='vplsConfigName'
_t='fsL2VpnPwRedIccpPwRemoteAii'
_s='fsL2VpnPwRedIccpPwRemoteAiiType'
_r='fsL2VpnPwRedIccpPwLocalAii'
_q='fsL2VpnPwRedIccpPwLocalAiiType'
_p='fsL2VpnPwRedIccpPwAgi'
_o='fsL2VpnPwRedIccpPwAgiType'
_n='fsL2VpnPwRedIccpPwId'
_m='fsL2VpnPwRedIccpPwGroup'
_l='fsL2VpnPwRedIccpPwTailLsr'
_k='fsL2VpnPwRedIccpPwFecType'
_j='fsL2VpnPwRedIccpPwHeadLsr'
_i='fsL2VpnPwRedIccpPwRgIndex'
_h='fsL2VpnPwRedPwIndex'
_g='fsL2VpnPwRedNodeAddr'
_f='fsL2VpnPwRedNodeAddrType'
_e='vplsBgpRteTargetIndex'
_d='manual'
_c='percentage'
_b='DisplayString'
_a='pwIndex'
_Z='PW-STD-MIB'
_Y='InetAddress'
_X='vplsNotificationGroup'
_W='vplsPwBindGroup'
_V='vplsGroup'
_U='vplsStatusOperStatus'
_T='vplsConfigAdminStatus'
_S='type1'
_R='SnmpAdminString'
_Q='vplsConfigFwdFullLowWatermark'
_P='vplsConfigFwdFullHighWatermark'
_O='fsL2VpnPwRedGroupIndex'
_N='vplsConfigVpnId'
_M='StorageType'
_L='Bits'
_K='OctetString'
_J='vplsConfigIndex'
_I='TruthValue'
_H='read-write'
_G='Unsigned32'
_F='read-only'
_E='not-accessible'
_D='Integer32'
_C='read-create'
_B='Aricent-L2VPN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_Y,'InetAddressType')
MplsLdpIdentifier,MplsLsrIdentifier=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsLdpIdentifier','MplsLsrIdentifier')
pwIndex,=mibBuilder.importSymbols(_Z,_a)
PwGroupID,PwIDType,PwIndexOrZeroType,PwOperStatusTC=mibBuilder.importSymbols('PW-TC-STD-MIB','PwGroupID','PwIDType','PwIndexOrZeroType','PwOperStatusTC')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_R)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_L,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_b,'PhysAddress','RowStatus',_M,'TextualConvention',_I)
fsL2VpnMIB=ModuleIdentity((1,3,6,1,4,1,29601,2,72))
if mibBuilder.loadTexts:fsL2VpnMIB.setRevisions(('2012-09-05 00:00',))
class VplsBgpRouteDistinguisher(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class VplsBgpRouteTarget(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class VplsBgpRouteTargetType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('import',1),('export',2),('both',3)))
class VPNIdOrZero(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(7,7))
class FsL2VpnPwStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('pwNotForwarding',0),('servicePwRxFault',1),('servicePwTxFault',2),('psnPwRxFault',3),('psnPwTxFault',4),('pwForwardingStandby',5),('pwSwitchoverRequest',6)))
_VplsNotifications_ObjectIdentity=ObjectIdentity
vplsNotifications=_VplsNotifications_ObjectIdentity((1,3,6,1,4,1,29601,2,72,0))
_VplsObjects_ObjectIdentity=ObjectIdentity
vplsObjects=_VplsObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,72,1))
_VplsConfigIndexNext_Type=Unsigned32
_VplsConfigIndexNext_Object=MibScalar
vplsConfigIndexNext=_VplsConfigIndexNext_Object((1,3,6,1,4,1,29601,2,72,1,1),_VplsConfigIndexNext_Type())
vplsConfigIndexNext.setMaxAccess(_F)
if mibBuilder.loadTexts:vplsConfigIndexNext.setStatus(_A)
_VplsConfigTable_Object=MibTable
vplsConfigTable=_VplsConfigTable_Object((1,3,6,1,4,1,29601,2,72,1,2))
if mibBuilder.loadTexts:vplsConfigTable.setStatus(_A)
_VplsConfigEntry_Object=MibTableRow
vplsConfigEntry=_VplsConfigEntry_Object((1,3,6,1,4,1,29601,2,72,1,2,1))
vplsConfigEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:vplsConfigEntry.setStatus(_A)
class _VplsConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VplsConfigIndex_Type.__name__=_G
_VplsConfigIndex_Object=MibTableColumn
vplsConfigIndex=_VplsConfigIndex_Object((1,3,6,1,4,1,29601,2,72,1,2,1,1),_VplsConfigIndex_Type())
vplsConfigIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:vplsConfigIndex.setStatus(_A)
class _VplsConfigName_Type(SnmpAdminString):defaultValue=OctetString('')
_VplsConfigName_Type.__name__=_R
_VplsConfigName_Object=MibTableColumn
vplsConfigName=_VplsConfigName_Object((1,3,6,1,4,1,29601,2,72,1,2,1,2),_VplsConfigName_Type())
vplsConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigName.setStatus(_A)
class _VplsConfigDescr_Type(SnmpAdminString):defaultValue=OctetString('')
_VplsConfigDescr_Type.__name__=_R
_VplsConfigDescr_Object=MibTableColumn
vplsConfigDescr=_VplsConfigDescr_Object((1,3,6,1,4,1,29601,2,72,1,2,1,3),_VplsConfigDescr_Type())
vplsConfigDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigDescr.setStatus(_A)
class _VplsConfigAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_VplsConfigAdminStatus_Type.__name__=_D
_VplsConfigAdminStatus_Object=MibTableColumn
vplsConfigAdminStatus=_VplsConfigAdminStatus_Object((1,3,6,1,4,1,29601,2,72,1,2,1,4),_VplsConfigAdminStatus_Type())
vplsConfigAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigAdminStatus.setStatus(_A)
class _VplsConfigMacLearning_Type(TruthValue):defaultValue=1
_VplsConfigMacLearning_Type.__name__=_I
_VplsConfigMacLearning_Object=MibTableColumn
vplsConfigMacLearning=_VplsConfigMacLearning_Object((1,3,6,1,4,1,29601,2,72,1,2,1,6),_VplsConfigMacLearning_Type())
vplsConfigMacLearning.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigMacLearning.setStatus(_A)
class _VplsConfigDiscardUnknownDest_Type(TruthValue):defaultValue=2
_VplsConfigDiscardUnknownDest_Type.__name__=_I
_VplsConfigDiscardUnknownDest_Object=MibTableColumn
vplsConfigDiscardUnknownDest=_VplsConfigDiscardUnknownDest_Object((1,3,6,1,4,1,29601,2,72,1,2,1,7),_VplsConfigDiscardUnknownDest_Type())
vplsConfigDiscardUnknownDest.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigDiscardUnknownDest.setStatus(_A)
class _VplsConfigMacAging_Type(TruthValue):defaultValue=1
_VplsConfigMacAging_Type.__name__=_I
_VplsConfigMacAging_Object=MibTableColumn
vplsConfigMacAging=_VplsConfigMacAging_Object((1,3,6,1,4,1,29601,2,72,1,2,1,8),_VplsConfigMacAging_Type())
vplsConfigMacAging.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigMacAging.setStatus(_A)
class _VplsConfigFwdFullHighWatermark_Type(Unsigned32):defaultValue=95;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VplsConfigFwdFullHighWatermark_Type.__name__=_G
_VplsConfigFwdFullHighWatermark_Object=MibTableColumn
vplsConfigFwdFullHighWatermark=_VplsConfigFwdFullHighWatermark_Object((1,3,6,1,4,1,29601,2,72,1,2,1,10),_VplsConfigFwdFullHighWatermark_Type())
vplsConfigFwdFullHighWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigFwdFullHighWatermark.setStatus(_A)
if mibBuilder.loadTexts:vplsConfigFwdFullHighWatermark.setUnits(_c)
class _VplsConfigFwdFullLowWatermark_Type(Unsigned32):defaultValue=90;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VplsConfigFwdFullLowWatermark_Type.__name__=_G
_VplsConfigFwdFullLowWatermark_Object=MibTableColumn
vplsConfigFwdFullLowWatermark=_VplsConfigFwdFullLowWatermark_Object((1,3,6,1,4,1,29601,2,72,1,2,1,11),_VplsConfigFwdFullLowWatermark_Type())
vplsConfigFwdFullLowWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigFwdFullLowWatermark.setStatus(_A)
if mibBuilder.loadTexts:vplsConfigFwdFullLowWatermark.setUnits(_c)
_VplsConfigRowStatus_Type=RowStatus
_VplsConfigRowStatus_Object=MibTableColumn
vplsConfigRowStatus=_VplsConfigRowStatus_Object((1,3,6,1,4,1,29601,2,72,1,2,1,12),_VplsConfigRowStatus_Type())
vplsConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigRowStatus.setStatus(_A)
class _VplsConfigMtu_Type(Unsigned32):defaultValue=1518;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1518))
_VplsConfigMtu_Type.__name__=_G
_VplsConfigMtu_Object=MibTableColumn
vplsConfigMtu=_VplsConfigMtu_Object((1,3,6,1,4,1,29601,2,72,1,2,1,13),_VplsConfigMtu_Type())
vplsConfigMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigMtu.setStatus(_A)
_VplsConfigVpnId_Type=VPNIdOrZero
_VplsConfigVpnId_Object=MibTableColumn
vplsConfigVpnId=_VplsConfigVpnId_Object((1,3,6,1,4,1,29601,2,72,1,2,1,14),_VplsConfigVpnId_Type())
vplsConfigVpnId.setMaxAccess(_F)
if mibBuilder.loadTexts:vplsConfigVpnId.setStatus(_A)
class _VplsConfigStorageType_Type(StorageType):defaultValue=2
_VplsConfigStorageType_Type.__name__=_M
_VplsConfigStorageType_Object=MibTableColumn
vplsConfigStorageType=_VplsConfigStorageType_Object((1,3,6,1,4,1,29601,2,72,1,2,1,15),_VplsConfigStorageType_Type())
vplsConfigStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigStorageType.setStatus(_A)
class _VplsConfigSignalingType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ldp',1),('bgp',2),('none',3)))
_VplsConfigSignalingType_Type.__name__=_D
_VplsConfigSignalingType_Object=MibTableColumn
vplsConfigSignalingType=_VplsConfigSignalingType_Object((1,3,6,1,4,1,29601,2,72,1,2,1,16),_VplsConfigSignalingType_Type())
vplsConfigSignalingType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsConfigSignalingType.setStatus(_A)
_VplsStatusTable_Object=MibTable
vplsStatusTable=_VplsStatusTable_Object((1,3,6,1,4,1,29601,2,72,1,3))
if mibBuilder.loadTexts:vplsStatusTable.setStatus(_A)
_VplsStatusEntry_Object=MibTableRow
vplsStatusEntry=_VplsStatusEntry_Object((1,3,6,1,4,1,29601,2,72,1,3,1))
vplsStatusEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:vplsStatusEntry.setStatus(_A)
class _VplsStatusOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('other',0),('up',1),('down',2)))
_VplsStatusOperStatus_Type.__name__=_D
_VplsStatusOperStatus_Object=MibTableColumn
vplsStatusOperStatus=_VplsStatusOperStatus_Object((1,3,6,1,4,1,29601,2,72,1,3,1,1),_VplsStatusOperStatus_Type())
vplsStatusOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:vplsStatusOperStatus.setStatus(_A)
_VplsStatusPeerCount_Type=Counter32
_VplsStatusPeerCount_Object=MibTableColumn
vplsStatusPeerCount=_VplsStatusPeerCount_Object((1,3,6,1,4,1,29601,2,72,1,3,1,2),_VplsStatusPeerCount_Type())
vplsStatusPeerCount.setMaxAccess(_F)
if mibBuilder.loadTexts:vplsStatusPeerCount.setStatus(_A)
_VplsPwBindTable_Object=MibTable
vplsPwBindTable=_VplsPwBindTable_Object((1,3,6,1,4,1,29601,2,72,1,4))
if mibBuilder.loadTexts:vplsPwBindTable.setStatus(_A)
_VplsPwBindEntry_Object=MibTableRow
vplsPwBindEntry=_VplsPwBindEntry_Object((1,3,6,1,4,1,29601,2,72,1,4,1))
vplsPwBindEntry.setIndexNames((0,_B,_J),(0,_Z,_a))
if mibBuilder.loadTexts:vplsPwBindEntry.setStatus(_A)
class _VplsPwBindConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),('autodiscovery',2)))
_VplsPwBindConfigType_Type.__name__=_D
_VplsPwBindConfigType_Object=MibTableColumn
vplsPwBindConfigType=_VplsPwBindConfigType_Object((1,3,6,1,4,1,29601,2,72,1,4,1,1),_VplsPwBindConfigType_Type())
vplsPwBindConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindConfigType.setStatus(_A)
class _VplsPwBindType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mesh',1),('spoke',2)))
_VplsPwBindType_Type.__name__=_D
_VplsPwBindType_Object=MibTableColumn
vplsPwBindType=_VplsPwBindType_Object((1,3,6,1,4,1,29601,2,72,1,4,1,2),_VplsPwBindType_Type())
vplsPwBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindType.setStatus(_A)
_VplsPwBindRowStatus_Type=RowStatus
_VplsPwBindRowStatus_Object=MibTableColumn
vplsPwBindRowStatus=_VplsPwBindRowStatus_Object((1,3,6,1,4,1,29601,2,72,1,4,1,3),_VplsPwBindRowStatus_Type())
vplsPwBindRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindRowStatus.setStatus(_A)
class _VplsPwBindStorageType_Type(StorageType):defaultValue=2
_VplsPwBindStorageType_Type.__name__=_M
_VplsPwBindStorageType_Object=MibTableColumn
vplsPwBindStorageType=_VplsPwBindStorageType_Object((1,3,6,1,4,1,29601,2,72,1,4,1,4),_VplsPwBindStorageType_Type())
vplsPwBindStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsPwBindStorageType.setStatus(_A)
_VplsBgpADConfigTable_Object=MibTable
vplsBgpADConfigTable=_VplsBgpADConfigTable_Object((1,3,6,1,4,1,29601,2,72,1,5))
if mibBuilder.loadTexts:vplsBgpADConfigTable.setStatus(_A)
_VplsBgpADConfigEntry_Object=MibTableRow
vplsBgpADConfigEntry=_VplsBgpADConfigEntry_Object((1,3,6,1,4,1,29601,2,72,1,5,1))
vplsBgpADConfigEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:vplsBgpADConfigEntry.setStatus(_A)
_VplsBgpADConfigRouteDistinguisher_Type=VplsBgpRouteDistinguisher
_VplsBgpADConfigRouteDistinguisher_Object=MibTableColumn
vplsBgpADConfigRouteDistinguisher=_VplsBgpADConfigRouteDistinguisher_Object((1,3,6,1,4,1,29601,2,72,1,5,1,1),_VplsBgpADConfigRouteDistinguisher_Type())
vplsBgpADConfigRouteDistinguisher.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpADConfigRouteDistinguisher.setStatus(_A)
class _VplsBgpADConfigPrefix_Type(Unsigned32):defaultValue=0
_VplsBgpADConfigPrefix_Type.__name__=_G
_VplsBgpADConfigPrefix_Object=MibTableColumn
vplsBgpADConfigPrefix=_VplsBgpADConfigPrefix_Object((1,3,6,1,4,1,29601,2,72,1,5,1,2),_VplsBgpADConfigPrefix_Type())
vplsBgpADConfigPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpADConfigPrefix.setStatus(_A)
_VplsBgpADConfigVplsId_Type=VplsBgpRouteDistinguisher
_VplsBgpADConfigVplsId_Object=MibTableColumn
vplsBgpADConfigVplsId=_VplsBgpADConfigVplsId_Object((1,3,6,1,4,1,29601,2,72,1,5,1,3),_VplsBgpADConfigVplsId_Type())
vplsBgpADConfigVplsId.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpADConfigVplsId.setStatus(_A)
_VplsBgpADConfigRowStatus_Type=RowStatus
_VplsBgpADConfigRowStatus_Object=MibTableColumn
vplsBgpADConfigRowStatus=_VplsBgpADConfigRowStatus_Object((1,3,6,1,4,1,29601,2,72,1,5,1,4),_VplsBgpADConfigRowStatus_Type())
vplsBgpADConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpADConfigRowStatus.setStatus(_A)
class _VplsBgpADConfigStorageType_Type(StorageType):defaultValue=3
_VplsBgpADConfigStorageType_Type.__name__=_M
_VplsBgpADConfigStorageType_Object=MibTableColumn
vplsBgpADConfigStorageType=_VplsBgpADConfigStorageType_Object((1,3,6,1,4,1,29601,2,72,1,5,1,5),_VplsBgpADConfigStorageType_Type())
vplsBgpADConfigStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpADConfigStorageType.setStatus(_A)
_VplsBgpRteTargetTable_Object=MibTable
vplsBgpRteTargetTable=_VplsBgpRteTargetTable_Object((1,3,6,1,4,1,29601,2,72,1,6))
if mibBuilder.loadTexts:vplsBgpRteTargetTable.setStatus(_A)
_VplsBgpRteTargetEntry_Object=MibTableRow
vplsBgpRteTargetEntry=_VplsBgpRteTargetEntry_Object((1,3,6,1,4,1,29601,2,72,1,6,1))
vplsBgpRteTargetEntry.setIndexNames((0,_B,_J),(0,_B,_e))
if mibBuilder.loadTexts:vplsBgpRteTargetEntry.setStatus(_A)
_VplsBgpRteTargetIndex_Type=Unsigned32
_VplsBgpRteTargetIndex_Object=MibTableColumn
vplsBgpRteTargetIndex=_VplsBgpRteTargetIndex_Object((1,3,6,1,4,1,29601,2,72,1,6,1,1),_VplsBgpRteTargetIndex_Type())
vplsBgpRteTargetIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:vplsBgpRteTargetIndex.setStatus(_A)
_VplsBgpRteTargetRTType_Type=VplsBgpRouteTargetType
_VplsBgpRteTargetRTType_Object=MibTableColumn
vplsBgpRteTargetRTType=_VplsBgpRteTargetRTType_Object((1,3,6,1,4,1,29601,2,72,1,6,1,2),_VplsBgpRteTargetRTType_Type())
vplsBgpRteTargetRTType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpRteTargetRTType.setStatus(_A)
_VplsBgpRteTargetRT_Type=VplsBgpRouteTarget
_VplsBgpRteTargetRT_Object=MibTableColumn
vplsBgpRteTargetRT=_VplsBgpRteTargetRT_Object((1,3,6,1,4,1,29601,2,72,1,6,1,3),_VplsBgpRteTargetRT_Type())
vplsBgpRteTargetRT.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpRteTargetRT.setStatus(_A)
_VplsBgpRteTargetRTRowStatus_Type=RowStatus
_VplsBgpRteTargetRTRowStatus_Object=MibTableColumn
vplsBgpRteTargetRTRowStatus=_VplsBgpRteTargetRTRowStatus_Object((1,3,6,1,4,1,29601,2,72,1,6,1,4),_VplsBgpRteTargetRTRowStatus_Type())
vplsBgpRteTargetRTRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpRteTargetRTRowStatus.setStatus(_A)
class _VplsBgpRteTargetStorageType_Type(StorageType):defaultValue=2
_VplsBgpRteTargetStorageType_Type.__name__=_M
_VplsBgpRteTargetStorageType_Object=MibTableColumn
vplsBgpRteTargetStorageType=_VplsBgpRteTargetStorageType_Object((1,3,6,1,4,1,29601,2,72,1,6,1,5),_VplsBgpRteTargetStorageType_Type())
vplsBgpRteTargetStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:vplsBgpRteTargetStorageType.setStatus(_A)
class _VplsStatusNotifEnable_Type(TruthValue):defaultValue=2
_VplsStatusNotifEnable_Type.__name__=_I
_VplsStatusNotifEnable_Object=MibScalar
vplsStatusNotifEnable=_VplsStatusNotifEnable_Object((1,3,6,1,4,1,29601,2,72,1,7),_VplsStatusNotifEnable_Type())
vplsStatusNotifEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:vplsStatusNotifEnable.setStatus(_A)
class _VplsNotificationMaxRate_Type(Unsigned32):defaultValue=0
_VplsNotificationMaxRate_Type.__name__=_G
_VplsNotificationMaxRate_Object=MibScalar
vplsNotificationMaxRate=_VplsNotificationMaxRate_Object((1,3,6,1,4,1,29601,2,72,1,8),_VplsNotificationMaxRate_Type())
vplsNotificationMaxRate.setMaxAccess(_H)
if mibBuilder.loadTexts:vplsNotificationMaxRate.setStatus(_A)
_VplsConformance_ObjectIdentity=ObjectIdentity
vplsConformance=_VplsConformance_ObjectIdentity((1,3,6,1,4,1,29601,2,72,2))
_VplsCompliances_ObjectIdentity=ObjectIdentity
vplsCompliances=_VplsCompliances_ObjectIdentity((1,3,6,1,4,1,29601,2,72,2,1))
_VplsGroups_ObjectIdentity=ObjectIdentity
vplsGroups=_VplsGroups_ObjectIdentity((1,3,6,1,4,1,29601,2,72,2,2))
_PwRedundancyScalar_ObjectIdentity=ObjectIdentity
pwRedundancyScalar=_PwRedundancyScalar_ObjectIdentity((1,3,6,1,4,1,29601,2,72,3))
class _FsL2VpnPwRedundancyStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_FsL2VpnPwRedundancyStatus_Type.__name__=_D
_FsL2VpnPwRedundancyStatus_Object=MibScalar
fsL2VpnPwRedundancyStatus=_FsL2VpnPwRedundancyStatus_Object((1,3,6,1,4,1,29601,2,72,3,1),_FsL2VpnPwRedundancyStatus_Type())
fsL2VpnPwRedundancyStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsL2VpnPwRedundancyStatus.setStatus(_A)
class _FsL2VpnPwRedNegotiationTimeOut_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsL2VpnPwRedNegotiationTimeOut_Type.__name__=_G
_FsL2VpnPwRedNegotiationTimeOut_Object=MibScalar
fsL2VpnPwRedNegotiationTimeOut=_FsL2VpnPwRedNegotiationTimeOut_Object((1,3,6,1,4,1,29601,2,72,3,2),_FsL2VpnPwRedNegotiationTimeOut_Type())
fsL2VpnPwRedNegotiationTimeOut.setMaxAccess(_H)
if mibBuilder.loadTexts:fsL2VpnPwRedNegotiationTimeOut.setStatus(_A)
if mibBuilder.loadTexts:fsL2VpnPwRedNegotiationTimeOut.setUnits('seconds')
class _FsL2VpnPwRedundancySyncFailNotifyEnable_Type(TruthValue):defaultValue=2
_FsL2VpnPwRedundancySyncFailNotifyEnable_Type.__name__=_I
_FsL2VpnPwRedundancySyncFailNotifyEnable_Object=MibScalar
fsL2VpnPwRedundancySyncFailNotifyEnable=_FsL2VpnPwRedundancySyncFailNotifyEnable_Object((1,3,6,1,4,1,29601,2,72,3,3),_FsL2VpnPwRedundancySyncFailNotifyEnable_Type())
fsL2VpnPwRedundancySyncFailNotifyEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:fsL2VpnPwRedundancySyncFailNotifyEnable.setStatus(_A)
class _FsL2VpnPwRedundancyPwStatusNotifyEnable_Type(TruthValue):defaultValue=2
_FsL2VpnPwRedundancyPwStatusNotifyEnable_Type.__name__=_I
_FsL2VpnPwRedundancyPwStatusNotifyEnable_Object=MibScalar
fsL2VpnPwRedundancyPwStatusNotifyEnable=_FsL2VpnPwRedundancyPwStatusNotifyEnable_Object((1,3,6,1,4,1,29601,2,72,3,4),_FsL2VpnPwRedundancyPwStatusNotifyEnable_Type())
fsL2VpnPwRedundancyPwStatusNotifyEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:fsL2VpnPwRedundancyPwStatusNotifyEnable.setStatus(_A)
_PwRedundancyObjects_ObjectIdentity=ObjectIdentity
pwRedundancyObjects=_PwRedundancyObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,72,4))
_FsL2VpnPwRedTraps_ObjectIdentity=ObjectIdentity
fsL2VpnPwRedTraps=_FsL2VpnPwRedTraps_ObjectIdentity((1,3,6,1,4,1,29601,2,72,4,0))
_FsL2VpnPwRedGroupTable_Object=MibTable
fsL2VpnPwRedGroupTable=_FsL2VpnPwRedGroupTable_Object((1,3,6,1,4,1,29601,2,72,4,1))
if mibBuilder.loadTexts:fsL2VpnPwRedGroupTable.setStatus(_A)
_FsL2VpnPwRedGroupEntry_Object=MibTableRow
fsL2VpnPwRedGroupEntry=_FsL2VpnPwRedGroupEntry_Object((1,3,6,1,4,1,29601,2,72,4,1,1))
fsL2VpnPwRedGroupEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:fsL2VpnPwRedGroupEntry.setStatus(_A)
_FsL2VpnPwRedGroupIndex_Type=Unsigned32
_FsL2VpnPwRedGroupIndex_Object=MibTableColumn
fsL2VpnPwRedGroupIndex=_FsL2VpnPwRedGroupIndex_Object((1,3,6,1,4,1,29601,2,72,4,1,1,1),_FsL2VpnPwRedGroupIndex_Type())
fsL2VpnPwRedGroupIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedGroupIndex.setStatus(_A)
class _FsL2VpnPwRedGroupProtType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('onePlusOne',1),('oneIsToOne',2),('oneIsToN',3)))
_FsL2VpnPwRedGroupProtType_Type.__name__=_D
_FsL2VpnPwRedGroupProtType_Object=MibTableColumn
fsL2VpnPwRedGroupProtType=_FsL2VpnPwRedGroupProtType_Object((1,3,6,1,4,1,29601,2,72,4,1,1,2),_FsL2VpnPwRedGroupProtType_Type())
fsL2VpnPwRedGroupProtType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2VpnPwRedGroupProtType.setStatus(_A)
class _FsL2VpnPwRedGroupReversionType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('revertive',1),('nonRevertive',2)))
_FsL2VpnPwRedGroupReversionType_Type.__name__=_D
_FsL2VpnPwRedGroupReversionType_Object=MibTableColumn
fsL2VpnPwRedGroupReversionType=_FsL2VpnPwRedGroupReversionType_Object((1,3,6,1,4,1,29601,2,72,4,1,1,3),_FsL2VpnPwRedGroupReversionType_Type())
fsL2VpnPwRedGroupReversionType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2VpnPwRedGroupReversionType.setStatus(_A)
class _FsL2VpnPwRedGroupContentionResolutionMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('independent',1),('masterslave',2)))
_FsL2VpnPwRedGroupContentionResolutionMethod_Type.__name__=_D
_FsL2VpnPwRedGroupContentionResolutionMethod_Object=MibTableColumn
fsL2VpnPwRedGroupContentionResolutionMethod=_FsL2VpnPwRedGroupContentionResolutionMethod_Object((1,3,6,1,4,1,29601,2,72,4,1,1,4),_FsL2VpnPwRedGroupContentionResolutionMethod_Type())
fsL2VpnPwRedGroupContentionResolutionMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2VpnPwRedGroupContentionResolutionMethod.setStatus(_A)
class _FsL2VpnPwRedGroupLockoutProtection_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_FsL2VpnPwRedGroupLockoutProtection_Type.__name__=_D
_FsL2VpnPwRedGroupLockoutProtection_Object=MibTableColumn
fsL2VpnPwRedGroupLockoutProtection=_FsL2VpnPwRedGroupLockoutProtection_Object((1,3,6,1,4,1,29601,2,72,4,1,1,5),_FsL2VpnPwRedGroupLockoutProtection_Type())
fsL2VpnPwRedGroupLockoutProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2VpnPwRedGroupLockoutProtection.setStatus(_A)
class _FsL2VpnPwRedGroupMasterSlaveMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('slave',2)))
_FsL2VpnPwRedGroupMasterSlaveMode_Type.__name__=_D
_FsL2VpnPwRedGroupMasterSlaveMode_Object=MibTableColumn
fsL2VpnPwRedGroupMasterSlaveMode=_FsL2VpnPwRedGroupMasterSlaveMode_Object((1,3,6,1,4,1,29601,2,72,4,1,1,6),_FsL2VpnPwRedGroupMasterSlaveMode_Type())
fsL2VpnPwRedGroupMasterSlaveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2VpnPwRedGroupMasterSlaveMode.setStatus(_A)
class _FsL2VpnPwRedGroupDualHomeApps_Type(Bits):defaultHexValue='';namedValues=NamedValues(('lagg',0))
_FsL2VpnPwRedGroupDualHomeApps_Type.__name__=_L
_FsL2VpnPwRedGroupDualHomeApps_Object=MibTableColumn
fsL2VpnPwRedGroupDualHomeApps=_FsL2VpnPwRedGroupDualHomeApps_Object((1,3,6,1,4,1,29601,2,72,4,1,1,7),_FsL2VpnPwRedGroupDualHomeApps_Type())
fsL2VpnPwRedGroupDualHomeApps.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2VpnPwRedGroupDualHomeApps.setStatus(_A)
class _FsL2VpnPwRedGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsL2VpnPwRedGroupName_Type.__name__=_b
_FsL2VpnPwRedGroupName_Object=MibTableColumn
fsL2VpnPwRedGroupName=_FsL2VpnPwRedGroupName_Object((1,3,6,1,4,1,29601,2,72,4,1,1,8),_FsL2VpnPwRedGroupName_Type())
fsL2VpnPwRedGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2VpnPwRedGroupName.setStatus(_A)
class _FsL2VpnPwRedGroupStatus_Type(Bits):namedValues=NamedValues(*(('forwardingNegotiaton',0),('switchoverNegotiaton',1),('negotiatonSuccess',2),('waitingToRestore',3),('redundancyUnAvailable',4)))
_FsL2VpnPwRedGroupStatus_Type.__name__=_L
_FsL2VpnPwRedGroupStatus_Object=MibTableColumn
fsL2VpnPwRedGroupStatus=_FsL2VpnPwRedGroupStatus_Object((1,3,6,1,4,1,29601,2,72,4,1,1,9),_FsL2VpnPwRedGroupStatus_Type())
fsL2VpnPwRedGroupStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsL2VpnPwRedGroupStatus.setStatus(_A)
_FsL2VpnPwRedGroupOperActivePw_Type=PwIndexOrZeroType
_FsL2VpnPwRedGroupOperActivePw_Object=MibTableColumn
fsL2VpnPwRedGroupOperActivePw=_FsL2VpnPwRedGroupOperActivePw_Object((1,3,6,1,4,1,29601,2,72,4,1,1,10),_FsL2VpnPwRedGroupOperActivePw_Type())
fsL2VpnPwRedGroupOperActivePw.setMaxAccess(_F)
if mibBuilder.loadTexts:fsL2VpnPwRedGroupOperActivePw.setStatus(_A)
class _FsL2VpnPwRedGroupWtrTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,180))
_FsL2VpnPwRedGroupWtrTimer_Type.__name__=_G
_FsL2VpnPwRedGroupWtrTimer_Object=MibTableColumn
fsL2VpnPwRedGroupWtrTimer=_FsL2VpnPwRedGroupWtrTimer_Object((1,3,6,1,4,1,29601,2,72,4,1,1,11),_FsL2VpnPwRedGroupWtrTimer_Type())
fsL2VpnPwRedGroupWtrTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2VpnPwRedGroupWtrTimer.setStatus(_A)
class _FsL2VpnPwRedGroupAdminCmd_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lockOutProtection',1),('clear',2)))
_FsL2VpnPwRedGroupAdminCmd_Type.__name__=_D
_FsL2VpnPwRedGroupAdminCmd_Object=MibTableColumn
fsL2VpnPwRedGroupAdminCmd=_FsL2VpnPwRedGroupAdminCmd_Object((1,3,6,1,4,1,29601,2,72,4,1,1,12),_FsL2VpnPwRedGroupAdminCmd_Type())
fsL2VpnPwRedGroupAdminCmd.setMaxAccess(_H)
if mibBuilder.loadTexts:fsL2VpnPwRedGroupAdminCmd.setStatus(_A)
_FsL2VpnPwRedGroupAdminActivePw_Type=PwIndexOrZeroType
_FsL2VpnPwRedGroupAdminActivePw_Object=MibTableColumn
fsL2VpnPwRedGroupAdminActivePw=_FsL2VpnPwRedGroupAdminActivePw_Object((1,3,6,1,4,1,29601,2,72,4,1,1,13),_FsL2VpnPwRedGroupAdminActivePw_Type())
fsL2VpnPwRedGroupAdminActivePw.setMaxAccess(_H)
if mibBuilder.loadTexts:fsL2VpnPwRedGroupAdminActivePw.setStatus(_A)
class _FsL2VpnPwRedGroupAdminCmdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('accepted',1),('notApplicable',2),('rejected',3)))
_FsL2VpnPwRedGroupAdminCmdStatus_Type.__name__=_D
_FsL2VpnPwRedGroupAdminCmdStatus_Object=MibTableColumn
fsL2VpnPwRedGroupAdminCmdStatus=_FsL2VpnPwRedGroupAdminCmdStatus_Object((1,3,6,1,4,1,29601,2,72,4,1,1,14),_FsL2VpnPwRedGroupAdminCmdStatus_Type())
fsL2VpnPwRedGroupAdminCmdStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsL2VpnPwRedGroupAdminCmdStatus.setStatus(_A)
_FsL2VpnPwRedGroupRowStatus_Type=RowStatus
_FsL2VpnPwRedGroupRowStatus_Object=MibTableColumn
fsL2VpnPwRedGroupRowStatus=_FsL2VpnPwRedGroupRowStatus_Object((1,3,6,1,4,1,29601,2,72,4,1,1,15),_FsL2VpnPwRedGroupRowStatus_Type())
fsL2VpnPwRedGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2VpnPwRedGroupRowStatus.setStatus(_A)
_FsL2VpnPwRedNodeTable_Object=MibTable
fsL2VpnPwRedNodeTable=_FsL2VpnPwRedNodeTable_Object((1,3,6,1,4,1,29601,2,72,4,2))
if mibBuilder.loadTexts:fsL2VpnPwRedNodeTable.setStatus(_A)
_FsL2VpnPwRedNodeEntry_Object=MibTableRow
fsL2VpnPwRedNodeEntry=_FsL2VpnPwRedNodeEntry_Object((1,3,6,1,4,1,29601,2,72,4,2,1))
fsL2VpnPwRedNodeEntry.setIndexNames((0,_B,_O),(0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:fsL2VpnPwRedNodeEntry.setStatus(_A)
_FsL2VpnPwRedNodeAddrType_Type=InetAddressType
_FsL2VpnPwRedNodeAddrType_Object=MibTableColumn
fsL2VpnPwRedNodeAddrType=_FsL2VpnPwRedNodeAddrType_Object((1,3,6,1,4,1,29601,2,72,4,2,1,1),_FsL2VpnPwRedNodeAddrType_Type())
fsL2VpnPwRedNodeAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedNodeAddrType.setStatus(_A)
class _FsL2VpnPwRedNodeAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_FsL2VpnPwRedNodeAddr_Type.__name__=_Y
_FsL2VpnPwRedNodeAddr_Object=MibTableColumn
fsL2VpnPwRedNodeAddr=_FsL2VpnPwRedNodeAddr_Object((1,3,6,1,4,1,29601,2,72,4,2,1,2),_FsL2VpnPwRedNodeAddr_Type())
fsL2VpnPwRedNodeAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedNodeAddr.setStatus(_A)
_FsL2VpnPwRedNodeLocalLdpID_Type=MplsLdpIdentifier
_FsL2VpnPwRedNodeLocalLdpID_Object=MibTableColumn
fsL2VpnPwRedNodeLocalLdpID=_FsL2VpnPwRedNodeLocalLdpID_Object((1,3,6,1,4,1,29601,2,72,4,2,1,3),_FsL2VpnPwRedNodeLocalLdpID_Type())
fsL2VpnPwRedNodeLocalLdpID.setMaxAccess(_F)
if mibBuilder.loadTexts:fsL2VpnPwRedNodeLocalLdpID.setStatus(_A)
_FsL2VpnPwRedNodeLocalLdpEntityIndex_Type=Unsigned32
_FsL2VpnPwRedNodeLocalLdpEntityIndex_Object=MibTableColumn
fsL2VpnPwRedNodeLocalLdpEntityIndex=_FsL2VpnPwRedNodeLocalLdpEntityIndex_Object((1,3,6,1,4,1,29601,2,72,4,2,1,4),_FsL2VpnPwRedNodeLocalLdpEntityIndex_Type())
fsL2VpnPwRedNodeLocalLdpEntityIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsL2VpnPwRedNodeLocalLdpEntityIndex.setStatus(_A)
_FsL2VpnPwRedNodePeerLdpID_Type=MplsLdpIdentifier
_FsL2VpnPwRedNodePeerLdpID_Object=MibTableColumn
fsL2VpnPwRedNodePeerLdpID=_FsL2VpnPwRedNodePeerLdpID_Object((1,3,6,1,4,1,29601,2,72,4,2,1,5),_FsL2VpnPwRedNodePeerLdpID_Type())
fsL2VpnPwRedNodePeerLdpID.setMaxAccess(_F)
if mibBuilder.loadTexts:fsL2VpnPwRedNodePeerLdpID.setStatus(_A)
class _FsL2VpnPwRedNodeStatus_Type(Bits):namedValues=NamedValues(*(('connected',0),('localSync',1)))
_FsL2VpnPwRedNodeStatus_Type.__name__=_L
_FsL2VpnPwRedNodeStatus_Object=MibTableColumn
fsL2VpnPwRedNodeStatus=_FsL2VpnPwRedNodeStatus_Object((1,3,6,1,4,1,29601,2,72,4,2,1,6),_FsL2VpnPwRedNodeStatus_Type())
fsL2VpnPwRedNodeStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsL2VpnPwRedNodeStatus.setStatus(_A)
_FsL2VpnPwRedNodeRowStatus_Type=RowStatus
_FsL2VpnPwRedNodeRowStatus_Object=MibTableColumn
fsL2VpnPwRedNodeRowStatus=_FsL2VpnPwRedNodeRowStatus_Object((1,3,6,1,4,1,29601,2,72,4,2,1,7),_FsL2VpnPwRedNodeRowStatus_Type())
fsL2VpnPwRedNodeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2VpnPwRedNodeRowStatus.setStatus(_A)
_FsL2VpnPwRedPwTable_Object=MibTable
fsL2VpnPwRedPwTable=_FsL2VpnPwRedPwTable_Object((1,3,6,1,4,1,29601,2,72,4,3))
if mibBuilder.loadTexts:fsL2VpnPwRedPwTable.setStatus(_A)
_FsL2VpnPwRedPwEntry_Object=MibTableRow
fsL2VpnPwRedPwEntry=_FsL2VpnPwRedPwEntry_Object((1,3,6,1,4,1,29601,2,72,4,3,1))
fsL2VpnPwRedPwEntry.setIndexNames((0,_B,_O),(0,_B,_h))
if mibBuilder.loadTexts:fsL2VpnPwRedPwEntry.setStatus(_A)
_FsL2VpnPwRedPwIndex_Type=PwIndexOrZeroType
_FsL2VpnPwRedPwIndex_Object=MibTableColumn
fsL2VpnPwRedPwIndex=_FsL2VpnPwRedPwIndex_Object((1,3,6,1,4,1,29601,2,72,4,3,1,1),_FsL2VpnPwRedPwIndex_Type())
fsL2VpnPwRedPwIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedPwIndex.setStatus(_A)
class _FsL2VpnPwRedPwPreferance_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_FsL2VpnPwRedPwPreferance_Type.__name__=_D
_FsL2VpnPwRedPwPreferance_Object=MibTableColumn
fsL2VpnPwRedPwPreferance=_FsL2VpnPwRedPwPreferance_Object((1,3,6,1,4,1,29601,2,72,4,3,1,2),_FsL2VpnPwRedPwPreferance_Type())
fsL2VpnPwRedPwPreferance.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2VpnPwRedPwPreferance.setStatus(_A)
_FsL2VpnPwRedPwLocalStatus_Type=FsL2VpnPwStatus
_FsL2VpnPwRedPwLocalStatus_Object=MibTableColumn
fsL2VpnPwRedPwLocalStatus=_FsL2VpnPwRedPwLocalStatus_Object((1,3,6,1,4,1,29601,2,72,4,3,1,3),_FsL2VpnPwRedPwLocalStatus_Type())
fsL2VpnPwRedPwLocalStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsL2VpnPwRedPwLocalStatus.setStatus(_A)
_FsL2VpnPwRedPwRemoteStatus_Type=FsL2VpnPwStatus
_FsL2VpnPwRedPwRemoteStatus_Object=MibTableColumn
fsL2VpnPwRedPwRemoteStatus=_FsL2VpnPwRedPwRemoteStatus_Object((1,3,6,1,4,1,29601,2,72,4,3,1,4),_FsL2VpnPwRedPwRemoteStatus_Type())
fsL2VpnPwRedPwRemoteStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsL2VpnPwRedPwRemoteStatus.setStatus(_A)
_FsL2VpnPwRedPwOperStatus_Type=PwOperStatusTC
_FsL2VpnPwRedPwOperStatus_Object=MibTableColumn
fsL2VpnPwRedPwOperStatus=_FsL2VpnPwRedPwOperStatus_Object((1,3,6,1,4,1,29601,2,72,4,3,1,5),_FsL2VpnPwRedPwOperStatus_Type())
fsL2VpnPwRedPwOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsL2VpnPwRedPwOperStatus.setStatus(_A)
_FsL2VpnPwRedPwRowStatus_Type=RowStatus
_FsL2VpnPwRedPwRowStatus_Object=MibTableColumn
fsL2VpnPwRedPwRowStatus=_FsL2VpnPwRedPwRowStatus_Object((1,3,6,1,4,1,29601,2,72,4,3,1,6),_FsL2VpnPwRedPwRowStatus_Type())
fsL2VpnPwRedPwRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2VpnPwRedPwRowStatus.setStatus(_A)
_FsL2VpnPwRedIccpPwTable_Object=MibTable
fsL2VpnPwRedIccpPwTable=_FsL2VpnPwRedIccpPwTable_Object((1,3,6,1,4,1,29601,2,72,4,4))
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwTable.setStatus(_A)
_FsL2VpnPwRedIccpPwEntry_Object=MibTableRow
fsL2VpnPwRedIccpPwEntry=_FsL2VpnPwRedIccpPwEntry_Object((1,3,6,1,4,1,29601,2,72,4,4,1))
fsL2VpnPwRedIccpPwEntry.setIndexNames((0,_B,_i),(0,_B,_j),(0,_B,_k),(0,_B,_l),(0,_B,_m),(0,_B,_n),(0,_B,_o),(0,_B,_p),(0,_B,_q),(0,_B,_r),(0,_B,_s),(0,_B,_t))
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwEntry.setStatus(_A)
_FsL2VpnPwRedIccpPwRgIndex_Type=Unsigned32
_FsL2VpnPwRedIccpPwRgIndex_Object=MibTableColumn
fsL2VpnPwRedIccpPwRgIndex=_FsL2VpnPwRedIccpPwRgIndex_Object((1,3,6,1,4,1,29601,2,72,4,4,1,1),_FsL2VpnPwRedIccpPwRgIndex_Type())
fsL2VpnPwRedIccpPwRgIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwRgIndex.setStatus(_A)
_FsL2VpnPwRedIccpPwHeadLsr_Type=MplsLsrIdentifier
_FsL2VpnPwRedIccpPwHeadLsr_Object=MibTableColumn
fsL2VpnPwRedIccpPwHeadLsr=_FsL2VpnPwRedIccpPwHeadLsr_Object((1,3,6,1,4,1,29601,2,72,4,4,1,2),_FsL2VpnPwRedIccpPwHeadLsr_Type())
fsL2VpnPwRedIccpPwHeadLsr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwHeadLsr.setStatus(_A)
class _FsL2VpnPwRedIccpPwFecType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_d,1),('pwIdFecSignaling',2),('genFecSignaling',3)))
_FsL2VpnPwRedIccpPwFecType_Type.__name__=_D
_FsL2VpnPwRedIccpPwFecType_Object=MibTableColumn
fsL2VpnPwRedIccpPwFecType=_FsL2VpnPwRedIccpPwFecType_Object((1,3,6,1,4,1,29601,2,72,4,4,1,3),_FsL2VpnPwRedIccpPwFecType_Type())
fsL2VpnPwRedIccpPwFecType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwFecType.setStatus(_A)
_FsL2VpnPwRedIccpPwTailLsr_Type=MplsLsrIdentifier
_FsL2VpnPwRedIccpPwTailLsr_Object=MibTableColumn
fsL2VpnPwRedIccpPwTailLsr=_FsL2VpnPwRedIccpPwTailLsr_Object((1,3,6,1,4,1,29601,2,72,4,4,1,4),_FsL2VpnPwRedIccpPwTailLsr_Type())
fsL2VpnPwRedIccpPwTailLsr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwTailLsr.setStatus(_A)
_FsL2VpnPwRedIccpPwGroup_Type=PwGroupID
_FsL2VpnPwRedIccpPwGroup_Object=MibTableColumn
fsL2VpnPwRedIccpPwGroup=_FsL2VpnPwRedIccpPwGroup_Object((1,3,6,1,4,1,29601,2,72,4,4,1,5),_FsL2VpnPwRedIccpPwGroup_Type())
fsL2VpnPwRedIccpPwGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwGroup.setStatus(_A)
_FsL2VpnPwRedIccpPwId_Type=PwIDType
_FsL2VpnPwRedIccpPwId_Object=MibTableColumn
fsL2VpnPwRedIccpPwId=_FsL2VpnPwRedIccpPwId_Object((1,3,6,1,4,1,29601,2,72,4,4,1,6),_FsL2VpnPwRedIccpPwId_Type())
fsL2VpnPwRedIccpPwId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwId.setStatus(_A)
class _FsL2VpnPwRedIccpPwAgiType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_S,1))
_FsL2VpnPwRedIccpPwAgiType_Type.__name__=_D
_FsL2VpnPwRedIccpPwAgiType_Object=MibTableColumn
fsL2VpnPwRedIccpPwAgiType=_FsL2VpnPwRedIccpPwAgiType_Object((1,3,6,1,4,1,29601,2,72,4,4,1,7),_FsL2VpnPwRedIccpPwAgiType_Type())
fsL2VpnPwRedIccpPwAgiType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwAgiType.setStatus(_A)
class _FsL2VpnPwRedIccpPwAgi_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_FsL2VpnPwRedIccpPwAgi_Type.__name__=_K
_FsL2VpnPwRedIccpPwAgi_Object=MibTableColumn
fsL2VpnPwRedIccpPwAgi=_FsL2VpnPwRedIccpPwAgi_Object((1,3,6,1,4,1,29601,2,72,4,4,1,8),_FsL2VpnPwRedIccpPwAgi_Type())
fsL2VpnPwRedIccpPwAgi.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwAgi.setStatus(_A)
class _FsL2VpnPwRedIccpPwLocalAiiType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),('type2',2)))
_FsL2VpnPwRedIccpPwLocalAiiType_Type.__name__=_D
_FsL2VpnPwRedIccpPwLocalAiiType_Object=MibTableColumn
fsL2VpnPwRedIccpPwLocalAiiType=_FsL2VpnPwRedIccpPwLocalAiiType_Object((1,3,6,1,4,1,29601,2,72,4,4,1,9),_FsL2VpnPwRedIccpPwLocalAiiType_Type())
fsL2VpnPwRedIccpPwLocalAiiType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwLocalAiiType.setStatus(_A)
class _FsL2VpnPwRedIccpPwLocalAii_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,12))
_FsL2VpnPwRedIccpPwLocalAii_Type.__name__=_K
_FsL2VpnPwRedIccpPwLocalAii_Object=MibTableColumn
fsL2VpnPwRedIccpPwLocalAii=_FsL2VpnPwRedIccpPwLocalAii_Object((1,3,6,1,4,1,29601,2,72,4,4,1,10),_FsL2VpnPwRedIccpPwLocalAii_Type())
fsL2VpnPwRedIccpPwLocalAii.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwLocalAii.setStatus(_A)
class _FsL2VpnPwRedIccpPwRemoteAiiType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),('type2',2)))
_FsL2VpnPwRedIccpPwRemoteAiiType_Type.__name__=_D
_FsL2VpnPwRedIccpPwRemoteAiiType_Object=MibTableColumn
fsL2VpnPwRedIccpPwRemoteAiiType=_FsL2VpnPwRedIccpPwRemoteAiiType_Object((1,3,6,1,4,1,29601,2,72,4,4,1,11),_FsL2VpnPwRedIccpPwRemoteAiiType_Type())
fsL2VpnPwRedIccpPwRemoteAiiType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwRemoteAiiType.setStatus(_A)
class _FsL2VpnPwRedIccpPwRemoteAii_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,12))
_FsL2VpnPwRedIccpPwRemoteAii_Type.__name__=_K
_FsL2VpnPwRedIccpPwRemoteAii_Object=MibTableColumn
fsL2VpnPwRedIccpPwRemoteAii=_FsL2VpnPwRedIccpPwRemoteAii_Object((1,3,6,1,4,1,29601,2,72,4,4,1,12),_FsL2VpnPwRedIccpPwRemoteAii_Type())
fsL2VpnPwRedIccpPwRemoteAii.setMaxAccess(_E)
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwRemoteAii.setStatus(_A)
class _FsL2VpnPwRedIccpPwRoId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_FsL2VpnPwRedIccpPwRoId_Type.__name__=_K
_FsL2VpnPwRedIccpPwRoId_Object=MibTableColumn
fsL2VpnPwRedIccpPwRoId=_FsL2VpnPwRedIccpPwRoId_Object((1,3,6,1,4,1,29601,2,72,4,4,1,13),_FsL2VpnPwRedIccpPwRoId_Type())
fsL2VpnPwRedIccpPwRoId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwRoId.setStatus(_A)
class _FsL2VpnPwRedIccpPwPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsL2VpnPwRedIccpPwPriority_Type.__name__=_G
_FsL2VpnPwRedIccpPwPriority_Object=MibTableColumn
fsL2VpnPwRedIccpPwPriority=_FsL2VpnPwRedIccpPwPriority_Object((1,3,6,1,4,1,29601,2,72,4,4,1,14),_FsL2VpnPwRedIccpPwPriority_Type())
fsL2VpnPwRedIccpPwPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwPriority.setStatus(_A)
class _FsL2VpnPwRedIccpPwStatus_Type(Bits):namedValues=NamedValues(*(('localForward',0),('localStandby',1),('localSwitchover',2),('remoteSwitchover',3),('remoteAwaited',4),('nodeSwitchover',6),('localUpdated',7)))
_FsL2VpnPwRedIccpPwStatus_Type.__name__=_L
_FsL2VpnPwRedIccpPwStatus_Object=MibTableColumn
fsL2VpnPwRedIccpPwStatus=_FsL2VpnPwRedIccpPwStatus_Object((1,3,6,1,4,1,29601,2,72,4,4,1,15),_FsL2VpnPwRedIccpPwStatus_Type())
fsL2VpnPwRedIccpPwStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsL2VpnPwRedIccpPwStatus.setStatus(_A)
_FsL2VpnPwRedTestObjects_ObjectIdentity=ObjectIdentity
fsL2VpnPwRedTestObjects=_FsL2VpnPwRedTestObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,72,4,5))
class _FsL2VpnPwRedSimulateFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noRgIdTlv',1),('invalidRgIdTlvLen',2),('rqstNumZero',3),('cAndSBitClear',4),('noPwIdOrGenPwIdTlv',5)))
_FsL2VpnPwRedSimulateFailure_Type.__name__=_D
_FsL2VpnPwRedSimulateFailure_Object=MibScalar
fsL2VpnPwRedSimulateFailure=_FsL2VpnPwRedSimulateFailure_Object((1,3,6,1,4,1,29601,2,72,4,5,1),_FsL2VpnPwRedSimulateFailure_Type())
fsL2VpnPwRedSimulateFailure.setMaxAccess(_H)
if mibBuilder.loadTexts:fsL2VpnPwRedSimulateFailure.setStatus(_A)
_FsL2VpnPwRedSimulateFailureForNbr_Type=IpAddress
_FsL2VpnPwRedSimulateFailureForNbr_Object=MibScalar
fsL2VpnPwRedSimulateFailureForNbr=_FsL2VpnPwRedSimulateFailureForNbr_Object((1,3,6,1,4,1,29601,2,72,4,5,2),_FsL2VpnPwRedSimulateFailureForNbr_Type())
fsL2VpnPwRedSimulateFailureForNbr.setMaxAccess(_H)
if mibBuilder.loadTexts:fsL2VpnPwRedSimulateFailureForNbr.setStatus(_A)
vplsGroup=ObjectGroup((1,3,6,1,4,1,29601,2,72,2,2,1))
vplsGroup.setObjects(*((_B,_u),(_B,_v),(_B,_T),(_B,_w),(_B,_x),(_B,_y),(_B,_N),(_B,_P),(_B,_Q),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_U),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:vplsGroup.setStatus(_A)
vplsPwBindGroup=ObjectGroup((1,3,6,1,4,1,29601,2,72,2,2,2))
vplsPwBindGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:vplsPwBindGroup.setStatus(_A)
vplsStatusChanged=NotificationType((1,3,6,1,4,1,29601,2,72,0,1))
vplsStatusChanged.setObjects(*((_B,_N),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:vplsStatusChanged.setStatus(_A)
vplsFwdFullAlarmRaised=NotificationType((1,3,6,1,4,1,29601,2,72,0,2))
vplsFwdFullAlarmRaised.setObjects(*((_B,_N),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:vplsFwdFullAlarmRaised.setStatus(_A)
vplsFwdFullAlarmCleared=NotificationType((1,3,6,1,4,1,29601,2,72,0,3))
vplsFwdFullAlarmCleared.setObjects(*((_B,_N),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:vplsFwdFullAlarmCleared.setStatus(_A)
fsL2VpnPwRedSyncFail=NotificationType((1,3,6,1,4,1,29601,2,72,4,0,1))
fsL2VpnPwRedSyncFail.setObjects(*((_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:fsL2VpnPwRedSyncFail.setStatus(_A)
fsL2VpnPwRedPwStatus=NotificationType((1,3,6,1,4,1,29601,2,72,4,0,2))
fsL2VpnPwRedPwStatus.setObjects(*((_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:fsL2VpnPwRedPwStatus.setStatus(_A)
vplsNotificationGroup=NotificationGroup((1,3,6,1,4,1,29601,2,72,2,2,3))
vplsNotificationGroup.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:vplsNotificationGroup.setStatus(_A)
vplsModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,29601,2,72,2,1,1))
vplsModuleFullCompliance.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:vplsModuleFullCompliance.setStatus(_A)
vplsModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,29601,2,72,2,1,2))
vplsModuleReadOnlyCompliance.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:vplsModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VplsBgpRouteDistinguisher':VplsBgpRouteDistinguisher,'VplsBgpRouteTarget':VplsBgpRouteTarget,'VplsBgpRouteTargetType':VplsBgpRouteTargetType,'VPNIdOrZero':VPNIdOrZero,'FsL2VpnPwStatus':FsL2VpnPwStatus,'fsL2VpnMIB':fsL2VpnMIB,'vplsNotifications':vplsNotifications,_AF:vplsStatusChanged,_AG:vplsFwdFullAlarmRaised,_AH:vplsFwdFullAlarmCleared,'vplsObjects':vplsObjects,_A0:vplsConfigIndexNext,'vplsConfigTable':vplsConfigTable,'vplsConfigEntry':vplsConfigEntry,_J:vplsConfigIndex,_u:vplsConfigName,_v:vplsConfigDescr,_T:vplsConfigAdminStatus,_w:vplsConfigMacLearning,_x:vplsConfigDiscardUnknownDest,_y:vplsConfigMacAging,_P:vplsConfigFwdFullHighWatermark,_Q:vplsConfigFwdFullLowWatermark,_z:vplsConfigRowStatus,_A1:vplsConfigMtu,_N:vplsConfigVpnId,_A2:vplsConfigStorageType,_A3:vplsConfigSignalingType,'vplsStatusTable':vplsStatusTable,'vplsStatusEntry':vplsStatusEntry,_U:vplsStatusOperStatus,_A4:vplsStatusPeerCount,'vplsPwBindTable':vplsPwBindTable,'vplsPwBindEntry':vplsPwBindEntry,_A7:vplsPwBindConfigType,_A8:vplsPwBindType,_A9:vplsPwBindRowStatus,_AA:vplsPwBindStorageType,'vplsBgpADConfigTable':vplsBgpADConfigTable,'vplsBgpADConfigEntry':vplsBgpADConfigEntry,'vplsBgpADConfigRouteDistinguisher':vplsBgpADConfigRouteDistinguisher,'vplsBgpADConfigPrefix':vplsBgpADConfigPrefix,'vplsBgpADConfigVplsId':vplsBgpADConfigVplsId,'vplsBgpADConfigRowStatus':vplsBgpADConfigRowStatus,'vplsBgpADConfigStorageType':vplsBgpADConfigStorageType,'vplsBgpRteTargetTable':vplsBgpRteTargetTable,'vplsBgpRteTargetEntry':vplsBgpRteTargetEntry,_e:vplsBgpRteTargetIndex,'vplsBgpRteTargetRTType':vplsBgpRteTargetRTType,'vplsBgpRteTargetRT':vplsBgpRteTargetRT,'vplsBgpRteTargetRTRowStatus':vplsBgpRteTargetRTRowStatus,'vplsBgpRteTargetStorageType':vplsBgpRteTargetStorageType,_A5:vplsStatusNotifEnable,_A6:vplsNotificationMaxRate,'vplsConformance':vplsConformance,'vplsCompliances':vplsCompliances,'vplsModuleFullCompliance':vplsModuleFullCompliance,'vplsModuleReadOnlyCompliance':vplsModuleReadOnlyCompliance,'vplsGroups':vplsGroups,_V:vplsGroup,_W:vplsPwBindGroup,_X:vplsNotificationGroup,'pwRedundancyScalar':pwRedundancyScalar,'fsL2VpnPwRedundancyStatus':fsL2VpnPwRedundancyStatus,'fsL2VpnPwRedNegotiationTimeOut':fsL2VpnPwRedNegotiationTimeOut,'fsL2VpnPwRedundancySyncFailNotifyEnable':fsL2VpnPwRedundancySyncFailNotifyEnable,'fsL2VpnPwRedundancyPwStatusNotifyEnable':fsL2VpnPwRedundancyPwStatusNotifyEnable,'pwRedundancyObjects':pwRedundancyObjects,'fsL2VpnPwRedTraps':fsL2VpnPwRedTraps,'fsL2VpnPwRedSyncFail':fsL2VpnPwRedSyncFail,'fsL2VpnPwRedPwStatus':fsL2VpnPwRedPwStatus,'fsL2VpnPwRedGroupTable':fsL2VpnPwRedGroupTable,'fsL2VpnPwRedGroupEntry':fsL2VpnPwRedGroupEntry,_O:fsL2VpnPwRedGroupIndex,'fsL2VpnPwRedGroupProtType':fsL2VpnPwRedGroupProtType,'fsL2VpnPwRedGroupReversionType':fsL2VpnPwRedGroupReversionType,'fsL2VpnPwRedGroupContentionResolutionMethod':fsL2VpnPwRedGroupContentionResolutionMethod,'fsL2VpnPwRedGroupLockoutProtection':fsL2VpnPwRedGroupLockoutProtection,'fsL2VpnPwRedGroupMasterSlaveMode':fsL2VpnPwRedGroupMasterSlaveMode,'fsL2VpnPwRedGroupDualHomeApps':fsL2VpnPwRedGroupDualHomeApps,'fsL2VpnPwRedGroupName':fsL2VpnPwRedGroupName,'fsL2VpnPwRedGroupStatus':fsL2VpnPwRedGroupStatus,_AC:fsL2VpnPwRedGroupOperActivePw,'fsL2VpnPwRedGroupWtrTimer':fsL2VpnPwRedGroupWtrTimer,'fsL2VpnPwRedGroupAdminCmd':fsL2VpnPwRedGroupAdminCmd,_AB:fsL2VpnPwRedGroupAdminActivePw,'fsL2VpnPwRedGroupAdminCmdStatus':fsL2VpnPwRedGroupAdminCmdStatus,'fsL2VpnPwRedGroupRowStatus':fsL2VpnPwRedGroupRowStatus,'fsL2VpnPwRedNodeTable':fsL2VpnPwRedNodeTable,'fsL2VpnPwRedNodeEntry':fsL2VpnPwRedNodeEntry,_f:fsL2VpnPwRedNodeAddrType,_g:fsL2VpnPwRedNodeAddr,'fsL2VpnPwRedNodeLocalLdpID':fsL2VpnPwRedNodeLocalLdpID,'fsL2VpnPwRedNodeLocalLdpEntityIndex':fsL2VpnPwRedNodeLocalLdpEntityIndex,'fsL2VpnPwRedNodePeerLdpID':fsL2VpnPwRedNodePeerLdpID,'fsL2VpnPwRedNodeStatus':fsL2VpnPwRedNodeStatus,'fsL2VpnPwRedNodeRowStatus':fsL2VpnPwRedNodeRowStatus,'fsL2VpnPwRedPwTable':fsL2VpnPwRedPwTable,'fsL2VpnPwRedPwEntry':fsL2VpnPwRedPwEntry,_h:fsL2VpnPwRedPwIndex,'fsL2VpnPwRedPwPreferance':fsL2VpnPwRedPwPreferance,_AD:fsL2VpnPwRedPwLocalStatus,_AE:fsL2VpnPwRedPwRemoteStatus,'fsL2VpnPwRedPwOperStatus':fsL2VpnPwRedPwOperStatus,'fsL2VpnPwRedPwRowStatus':fsL2VpnPwRedPwRowStatus,'fsL2VpnPwRedIccpPwTable':fsL2VpnPwRedIccpPwTable,'fsL2VpnPwRedIccpPwEntry':fsL2VpnPwRedIccpPwEntry,_i:fsL2VpnPwRedIccpPwRgIndex,_j:fsL2VpnPwRedIccpPwHeadLsr,_k:fsL2VpnPwRedIccpPwFecType,_l:fsL2VpnPwRedIccpPwTailLsr,_m:fsL2VpnPwRedIccpPwGroup,_n:fsL2VpnPwRedIccpPwId,_o:fsL2VpnPwRedIccpPwAgiType,_p:fsL2VpnPwRedIccpPwAgi,_q:fsL2VpnPwRedIccpPwLocalAiiType,_r:fsL2VpnPwRedIccpPwLocalAii,_s:fsL2VpnPwRedIccpPwRemoteAiiType,_t:fsL2VpnPwRedIccpPwRemoteAii,'fsL2VpnPwRedIccpPwRoId':fsL2VpnPwRedIccpPwRoId,'fsL2VpnPwRedIccpPwPriority':fsL2VpnPwRedIccpPwPriority,'fsL2VpnPwRedIccpPwStatus':fsL2VpnPwRedIccpPwStatus,'fsL2VpnPwRedTestObjects':fsL2VpnPwRedTestObjects,'fsL2VpnPwRedSimulateFailure':fsL2VpnPwRedSimulateFailure,'fsL2VpnPwRedSimulateFailureForNbr':fsL2VpnPwRedSimulateFailureForNbr})