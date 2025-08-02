_Ao='tptNgfwClusterNotificationGroup'
_An='tptNgfwClusterHaGroup'
_Am='tptNgfwClusterTrafficGroup'
_Al='tptNgfwClusterGroup'
_Ak='tptNgfwClusterConstChkFailedNotify'
_Aj='tptNgfwClusterCmpStateChangeNotify'
_Ai='tptNgfwClusterHaFgStateChangeNotify'
_Ah='tptNgfwClusterHealthChangeNotify'
_Ag='tptNgfwClusterHaStateSyncQueueFullNotify'
_Af='tptNgfwClusterHaStateSyncMessageLossNotify'
_Ae='tptNgfwClusterMemberRejectNotify'
_Ad='tptNgfwClusterMemberLeaveNotify'
_Ac='tptNgfwClusterMemberJoinNotify'
_Ab='tptNgfwClusterHaFeatSyncStatusDelEntries'
_Aa='tptNgfwClusterHaFeatSyncStatusAddEntries'
_AZ='tptNgfwClusterHaFeatSyncStatusTotalEntries'
_AY='tptNgfwClusterHaFeatSyncStatusSyncStateReason'
_AX='tptNgfwClusterHaFeatSyncStatusSyncState'
_AW='tptNgfwClusterHaFeatSyncStatusEnabled'
_AV='tptNgfwClusterHaFgMemberName'
_AU='tptNgfwClusterHaFgMemberId'
_AT='tptNgfwClusterHaFgMode'
_AS='tptNgfwClusterHaFgBaseMac'
_AR='tptNgfwClusterHaFeatSyncLogSeverity'
_AQ='tptNgfwClusterHaFeatSyncEnabled'
_AP='tptNgfwClusterHaMode'
_AO='tptNgfwClusterHaGlobalStateSyncEnabled'
_AN='tptNgfwClusterHaEnabled'
_AM='tptNgfwClusterTctEncryptionEnabled'
_AL='tptNgfwClusterTctLinkState'
_AK='tptNgfwClusterTctPortAutoNeg'
_AJ='tptNgfwClusterTctPortDuplex'
_AI='tptNgfwClusterTctPortSpeed'
_AH='tptNgfwClusterTctRetries'
_AG='tptNgfwClusterTctTimeout'
_AF='tptNgfwClusterTctMtu'
_AE='tptNgfwClusterTctTtl'
_AD='tptNgfwClusterTctPort'
_AC='tptNgfwClusterTctMulticastAddr'
_AB='tptNgfwClusterTctMulticastAddrType'
_AA='tptNgfwClusterMemberStatusMaster'
_A9='tptNgfwClusterMemberStatusHealthScore'
_A8='tptNgfwClusterMemberStatusHealthState'
_A7='tptNgfwClusterMemberStatusHaState'
_A6='tptNgfwClusterMemberStatusEnabled'
_A5='tptNgfwClusterMemberStatusCfgStateSync'
_A4='tptNgfwClusterMemberStatusCfgControl'
_A3='tptNgfwClusterMemberStatusSmsManaged'
_A2='tptNgfwClusterMemberStatusJoinTime'
_A1='tptNgfwClusterMemberStatusUptime'
_A0='tptNgfwClusterMemberStatusSwVersion'
_z='tptNgfwClusterMemberStatusHwModel'
_y='tptNgfwClusterMemberStatusSerialNo'
_x='tptNgfwClusterMemberStatusName'
_w='tptNgfwClusterCfgConstChecks'
_v='tptNgfwClusterHwConstChecks'
_u='tptNgfwClusterSwConstChecks'
_t='tptNgfwClusterStandby'
_s='tptNgfwClusterEnabled'
_r='tptNgfwClusterHaFeatSyncStatusFeature'
_q='tptNgfwClusterHaFgIndex'
_p='tptNgfwClusterHaFeatSyncFeature'
_o='tptNgfwClusterMemberStatusId'
_n='unknown'
_m='remote'
_l='disabled'
_k='tptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId'
_j='tptNgfwClusterHaFgStateChangeNotifyActiveDeviceId'
_i='tptNgfwClusterHaFgStateChangeNotifyState'
_h='tptNgfwClusterHaFgName'
_g='tptNgfwClusterConstChkFailedNotifyMaster'
_f='tptNgfwClusterConstChkFailedNotifyType'
_e='tptNgfwClusterCmpStateChangeNotifyRelation'
_d='tptNgfwClusterCmpStateChangeNotifyLimitType'
_c='tptNgfwClusterCmpStateChangeNotifyThreshold'
_b='tptNgfwClusterCmpStateChangeNotifyUnits'
_a='tptNgfwClusterCmpStateChangeNotifyValue'
_Z='tptNgfwClusterCmpStateChangeNotifyState'
_Y='tptNgfwClusterCmpStateChangeNotifyName'
_X='tptNgfwClusterCmpStateChangeNotifyType'
_W='tptNgfwClusterHealthChangeNotifyStateLowerLimit'
_V='tptNgfwClusterHealthChangeNotifyStateUpperLimit'
_U='tptNgfwClusterHealthChangeNotifyScore'
_T='tptNgfwClusterHealthChangeNotifyState'
_S='tptNgfwClusterMemberRejectNotifyReason'
_R='tptNgfwClusterHaStateSyncNotifyFeature'
_Q='tptNgfwClusterMemberName'
_P='tptNgfwClusterName'
_O='tptNgfwClusterHaFgId'
_N='not-accessible'
_M='tptNgfwClusterTctIpAddr'
_L='tptNgfwClusterTctIpAddrType'
_K='tptNgfwClusterMemberId'
_J='tptNgfwSystemSerial'
_I='TPT-NGFW-SYSTEM-INFO-MIB'
_H='tptNgfwNotifySeverity'
_G='TPT-NGFW-REG-MIB'
_F='Unsigned32'
_E='SnmpAdminString'
_D='accessible-for-notify'
_C='read-only'
_B='current'
_A='TPT-NGFW-CLUSTER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
Severity,tpt_ngfw_compls,tpt_ngfw_eventsV2,tpt_ngfw_groups,tpt_ngfw_objs,tpt_ngfw_params,tptNgfwNotifySeverity=mibBuilder.importSymbols(_G,'Severity','tpt-ngfw-compls','tpt-ngfw-eventsV2','tpt-ngfw-groups','tpt-ngfw-objs','tpt-ngfw-params',_H)
tptNgfwSystemSerial,=mibBuilder.importSymbols(_I,_J)
AutoNegotiation,DuplexSetting,LineSpeed=mibBuilder.importSymbols('TPT-PORT-CONFIG-MIB','AutoNegotiation','DuplexSetting','LineSpeed')
tptNgfwCluster=ModuleIdentity((1,3,6,1,4,1,10734,3,9,2,2))
if mibBuilder.loadTexts:tptNgfwCluster.setRevisions(('2016-05-25 18:54','2015-03-19 09:30','2013-01-17 10:30'))
class FailoverGrpMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('activePassive',1),('activeActive',2)))
class LinkState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
class CfgControl(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_l,1),('none',2),('local',3),(_m,4)))
class SyncState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inSync',1),('outOfSync',2),('notInit',3),('error',4),('pending',5)))
class HaState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('active',1),('passive',2),('failed',3),('standby',4),(_l,5),(_n,6),('activeNoPartner',7),('starting',8),('stopping',9)))
class HealthState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('warning',2),('critical',3)))
class ClusterMemberRejectReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('duplicateNodeId',1))
class FailoverGroupState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('running',1),('degraded',2),('stopped',3)))
class ComponentType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('swSal',1),('cpu',2),('memory',3),('swDisk',4),('swLink',5),('hwFan',6),('hwTmp',7),('hwVol',8),('hwVid',9),('hwAny',10),('hwPsu',11),(_n,12)))
class ThresholdLimitType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upper',1),('lower',2)))
class ThresholdRelation(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('above',1),('below',2)))
class ConsistencyCheckType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('configuration',1),('software',2),('hardware',3)))
class MasterLocation(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),(_m,2)))
class _TptNgfwClusterName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_TptNgfwClusterName_Type.__name__=_E
_TptNgfwClusterName_Object=MibScalar
tptNgfwClusterName=_TptNgfwClusterName_Object((1,3,6,1,4,1,10734,3,9,2,2,1),_TptNgfwClusterName_Type())
tptNgfwClusterName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterName.setStatus(_B)
_TptNgfwClusterEnabled_Type=TruthValue
_TptNgfwClusterEnabled_Object=MibScalar
tptNgfwClusterEnabled=_TptNgfwClusterEnabled_Object((1,3,6,1,4,1,10734,3,9,2,2,2),_TptNgfwClusterEnabled_Type())
tptNgfwClusterEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterEnabled.setStatus(_B)
class _TptNgfwClusterMemberId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_TptNgfwClusterMemberId_Type.__name__=_F
_TptNgfwClusterMemberId_Object=MibScalar
tptNgfwClusterMemberId=_TptNgfwClusterMemberId_Object((1,3,6,1,4,1,10734,3,9,2,2,3),_TptNgfwClusterMemberId_Type())
tptNgfwClusterMemberId.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberId.setStatus(_B)
class _TptNgfwClusterMemberName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_TptNgfwClusterMemberName_Type.__name__=_E
_TptNgfwClusterMemberName_Object=MibScalar
tptNgfwClusterMemberName=_TptNgfwClusterMemberName_Object((1,3,6,1,4,1,10734,3,9,2,2,4),_TptNgfwClusterMemberName_Type())
tptNgfwClusterMemberName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberName.setStatus(_B)
_TptNgfwClusterStandby_Type=TruthValue
_TptNgfwClusterStandby_Object=MibScalar
tptNgfwClusterStandby=_TptNgfwClusterStandby_Object((1,3,6,1,4,1,10734,3,9,2,2,5),_TptNgfwClusterStandby_Type())
tptNgfwClusterStandby.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterStandby.setStatus(_B)
_TptNgfwClusterSwConstChecks_Type=TruthValue
_TptNgfwClusterSwConstChecks_Object=MibScalar
tptNgfwClusterSwConstChecks=_TptNgfwClusterSwConstChecks_Object((1,3,6,1,4,1,10734,3,9,2,2,6),_TptNgfwClusterSwConstChecks_Type())
tptNgfwClusterSwConstChecks.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterSwConstChecks.setStatus(_B)
_TptNgfwClusterHwConstChecks_Type=TruthValue
_TptNgfwClusterHwConstChecks_Object=MibScalar
tptNgfwClusterHwConstChecks=_TptNgfwClusterHwConstChecks_Object((1,3,6,1,4,1,10734,3,9,2,2,7),_TptNgfwClusterHwConstChecks_Type())
tptNgfwClusterHwConstChecks.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHwConstChecks.setStatus(_B)
_TptNgfwClusterCfgConstChecks_Type=TruthValue
_TptNgfwClusterCfgConstChecks_Object=MibScalar
tptNgfwClusterCfgConstChecks=_TptNgfwClusterCfgConstChecks_Object((1,3,6,1,4,1,10734,3,9,2,2,8),_TptNgfwClusterCfgConstChecks_Type())
tptNgfwClusterCfgConstChecks.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterCfgConstChecks.setStatus(_B)
_TptNgfwClusterMemberStatusTable_Object=MibTable
tptNgfwClusterMemberStatusTable=_TptNgfwClusterMemberStatusTable_Object((1,3,6,1,4,1,10734,3,9,2,2,9))
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusTable.setStatus(_B)
_TptNgfwClusterMemberStatusTableEntry_Object=MibTableRow
tptNgfwClusterMemberStatusTableEntry=_TptNgfwClusterMemberStatusTableEntry_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1))
tptNgfwClusterMemberStatusTableEntry.setIndexNames((0,_A,_o))
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusTableEntry.setStatus(_B)
class _TptNgfwClusterMemberStatusId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_TptNgfwClusterMemberStatusId_Type.__name__=_F
_TptNgfwClusterMemberStatusId_Object=MibTableColumn
tptNgfwClusterMemberStatusId=_TptNgfwClusterMemberStatusId_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1,1),_TptNgfwClusterMemberStatusId_Type())
tptNgfwClusterMemberStatusId.setMaxAccess(_N)
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusId.setStatus(_B)
class _TptNgfwClusterMemberStatusName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_TptNgfwClusterMemberStatusName_Type.__name__=_E
_TptNgfwClusterMemberStatusName_Object=MibTableColumn
tptNgfwClusterMemberStatusName=_TptNgfwClusterMemberStatusName_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1,2),_TptNgfwClusterMemberStatusName_Type())
tptNgfwClusterMemberStatusName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusName.setStatus(_B)
class _TptNgfwClusterMemberStatusSerialNo_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TptNgfwClusterMemberStatusSerialNo_Type.__name__=_E
_TptNgfwClusterMemberStatusSerialNo_Object=MibTableColumn
tptNgfwClusterMemberStatusSerialNo=_TptNgfwClusterMemberStatusSerialNo_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1,3),_TptNgfwClusterMemberStatusSerialNo_Type())
tptNgfwClusterMemberStatusSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusSerialNo.setStatus(_B)
class _TptNgfwClusterMemberStatusHwModel_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TptNgfwClusterMemberStatusHwModel_Type.__name__=_E
_TptNgfwClusterMemberStatusHwModel_Object=MibTableColumn
tptNgfwClusterMemberStatusHwModel=_TptNgfwClusterMemberStatusHwModel_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1,4),_TptNgfwClusterMemberStatusHwModel_Type())
tptNgfwClusterMemberStatusHwModel.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusHwModel.setStatus(_B)
class _TptNgfwClusterMemberStatusSwVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TptNgfwClusterMemberStatusSwVersion_Type.__name__=_E
_TptNgfwClusterMemberStatusSwVersion_Object=MibTableColumn
tptNgfwClusterMemberStatusSwVersion=_TptNgfwClusterMemberStatusSwVersion_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1,5),_TptNgfwClusterMemberStatusSwVersion_Type())
tptNgfwClusterMemberStatusSwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusSwVersion.setStatus(_B)
_TptNgfwClusterMemberStatusUptime_Type=TimeTicks
_TptNgfwClusterMemberStatusUptime_Object=MibTableColumn
tptNgfwClusterMemberStatusUptime=_TptNgfwClusterMemberStatusUptime_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1,6),_TptNgfwClusterMemberStatusUptime_Type())
tptNgfwClusterMemberStatusUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusUptime.setStatus(_B)
_TptNgfwClusterMemberStatusJoinTime_Type=DateAndTime
_TptNgfwClusterMemberStatusJoinTime_Object=MibTableColumn
tptNgfwClusterMemberStatusJoinTime=_TptNgfwClusterMemberStatusJoinTime_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1,7),_TptNgfwClusterMemberStatusJoinTime_Type())
tptNgfwClusterMemberStatusJoinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusJoinTime.setStatus(_B)
_TptNgfwClusterMemberStatusSmsManaged_Type=TruthValue
_TptNgfwClusterMemberStatusSmsManaged_Object=MibTableColumn
tptNgfwClusterMemberStatusSmsManaged=_TptNgfwClusterMemberStatusSmsManaged_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1,8),_TptNgfwClusterMemberStatusSmsManaged_Type())
tptNgfwClusterMemberStatusSmsManaged.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusSmsManaged.setStatus(_B)
_TptNgfwClusterMemberStatusCfgControl_Type=CfgControl
_TptNgfwClusterMemberStatusCfgControl_Object=MibTableColumn
tptNgfwClusterMemberStatusCfgControl=_TptNgfwClusterMemberStatusCfgControl_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1,9),_TptNgfwClusterMemberStatusCfgControl_Type())
tptNgfwClusterMemberStatusCfgControl.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusCfgControl.setStatus(_B)
_TptNgfwClusterMemberStatusCfgStateSync_Type=SyncState
_TptNgfwClusterMemberStatusCfgStateSync_Object=MibTableColumn
tptNgfwClusterMemberStatusCfgStateSync=_TptNgfwClusterMemberStatusCfgStateSync_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1,10),_TptNgfwClusterMemberStatusCfgStateSync_Type())
tptNgfwClusterMemberStatusCfgStateSync.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusCfgStateSync.setStatus(_B)
_TptNgfwClusterMemberStatusEnabled_Type=TruthValue
_TptNgfwClusterMemberStatusEnabled_Object=MibTableColumn
tptNgfwClusterMemberStatusEnabled=_TptNgfwClusterMemberStatusEnabled_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1,11),_TptNgfwClusterMemberStatusEnabled_Type())
tptNgfwClusterMemberStatusEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusEnabled.setStatus(_B)
_TptNgfwClusterMemberStatusHaState_Type=HaState
_TptNgfwClusterMemberStatusHaState_Object=MibTableColumn
tptNgfwClusterMemberStatusHaState=_TptNgfwClusterMemberStatusHaState_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1,12),_TptNgfwClusterMemberStatusHaState_Type())
tptNgfwClusterMemberStatusHaState.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusHaState.setStatus(_B)
_TptNgfwClusterMemberStatusHealthState_Type=HealthState
_TptNgfwClusterMemberStatusHealthState_Object=MibTableColumn
tptNgfwClusterMemberStatusHealthState=_TptNgfwClusterMemberStatusHealthState_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1,13),_TptNgfwClusterMemberStatusHealthState_Type())
tptNgfwClusterMemberStatusHealthState.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusHealthState.setStatus(_B)
class _TptNgfwClusterMemberStatusHealthScore_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TptNgfwClusterMemberStatusHealthScore_Type.__name__=_F
_TptNgfwClusterMemberStatusHealthScore_Object=MibTableColumn
tptNgfwClusterMemberStatusHealthScore=_TptNgfwClusterMemberStatusHealthScore_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1,14),_TptNgfwClusterMemberStatusHealthScore_Type())
tptNgfwClusterMemberStatusHealthScore.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusHealthScore.setStatus(_B)
_TptNgfwClusterMemberStatusMaster_Type=TruthValue
_TptNgfwClusterMemberStatusMaster_Object=MibTableColumn
tptNgfwClusterMemberStatusMaster=_TptNgfwClusterMemberStatusMaster_Object((1,3,6,1,4,1,10734,3,9,2,2,9,1,15),_TptNgfwClusterMemberStatusMaster_Type())
tptNgfwClusterMemberStatusMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterMemberStatusMaster.setStatus(_B)
_TptNgfwClusterTraffic_ObjectIdentity=ObjectIdentity
tptNgfwClusterTraffic=_TptNgfwClusterTraffic_ObjectIdentity((1,3,6,1,4,1,10734,3,9,2,2,10))
_TptNgfwClusterTctIpAddrType_Type=InetAddressType
_TptNgfwClusterTctIpAddrType_Object=MibScalar
tptNgfwClusterTctIpAddrType=_TptNgfwClusterTctIpAddrType_Object((1,3,6,1,4,1,10734,3,9,2,2,10,1),_TptNgfwClusterTctIpAddrType_Type())
tptNgfwClusterTctIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterTctIpAddrType.setStatus(_B)
_TptNgfwClusterTctIpAddr_Type=InetAddress
_TptNgfwClusterTctIpAddr_Object=MibScalar
tptNgfwClusterTctIpAddr=_TptNgfwClusterTctIpAddr_Object((1,3,6,1,4,1,10734,3,9,2,2,10,2),_TptNgfwClusterTctIpAddr_Type())
tptNgfwClusterTctIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterTctIpAddr.setStatus(_B)
_TptNgfwClusterTctMulticastAddrType_Type=InetAddressType
_TptNgfwClusterTctMulticastAddrType_Object=MibScalar
tptNgfwClusterTctMulticastAddrType=_TptNgfwClusterTctMulticastAddrType_Object((1,3,6,1,4,1,10734,3,9,2,2,10,3),_TptNgfwClusterTctMulticastAddrType_Type())
tptNgfwClusterTctMulticastAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterTctMulticastAddrType.setStatus(_B)
_TptNgfwClusterTctMulticastAddr_Type=InetAddress
_TptNgfwClusterTctMulticastAddr_Object=MibScalar
tptNgfwClusterTctMulticastAddr=_TptNgfwClusterTctMulticastAddr_Object((1,3,6,1,4,1,10734,3,9,2,2,10,4),_TptNgfwClusterTctMulticastAddr_Type())
tptNgfwClusterTctMulticastAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterTctMulticastAddr.setStatus(_B)
class _TptNgfwClusterTctPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_TptNgfwClusterTctPort_Type.__name__=_F
_TptNgfwClusterTctPort_Object=MibScalar
tptNgfwClusterTctPort=_TptNgfwClusterTctPort_Object((1,3,6,1,4,1,10734,3,9,2,2,10,5),_TptNgfwClusterTctPort_Type())
tptNgfwClusterTctPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterTctPort.setStatus(_B)
class _TptNgfwClusterTctTtl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TptNgfwClusterTctTtl_Type.__name__=_F
_TptNgfwClusterTctTtl_Object=MibScalar
tptNgfwClusterTctTtl=_TptNgfwClusterTctTtl_Object((1,3,6,1,4,1,10734,3,9,2,2,10,6),_TptNgfwClusterTctTtl_Type())
tptNgfwClusterTctTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterTctTtl.setStatus(_B)
class _TptNgfwClusterTctMtu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(576,9216))
_TptNgfwClusterTctMtu_Type.__name__=_F
_TptNgfwClusterTctMtu_Object=MibScalar
tptNgfwClusterTctMtu=_TptNgfwClusterTctMtu_Object((1,3,6,1,4,1,10734,3,9,2,2,10,7),_TptNgfwClusterTctMtu_Type())
tptNgfwClusterTctMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterTctMtu.setStatus(_B)
class _TptNgfwClusterTctTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_TptNgfwClusterTctTimeout_Type.__name__=_F
_TptNgfwClusterTctTimeout_Object=MibScalar
tptNgfwClusterTctTimeout=_TptNgfwClusterTctTimeout_Object((1,3,6,1,4,1,10734,3,9,2,2,10,8),_TptNgfwClusterTctTimeout_Type())
tptNgfwClusterTctTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterTctTimeout.setStatus(_B)
class _TptNgfwClusterTctRetries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TptNgfwClusterTctRetries_Type.__name__=_F
_TptNgfwClusterTctRetries_Object=MibScalar
tptNgfwClusterTctRetries=_TptNgfwClusterTctRetries_Object((1,3,6,1,4,1,10734,3,9,2,2,10,9),_TptNgfwClusterTctRetries_Type())
tptNgfwClusterTctRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterTctRetries.setStatus(_B)
_TptNgfwClusterTctPortSpeed_Type=LineSpeed
_TptNgfwClusterTctPortSpeed_Object=MibScalar
tptNgfwClusterTctPortSpeed=_TptNgfwClusterTctPortSpeed_Object((1,3,6,1,4,1,10734,3,9,2,2,10,10),_TptNgfwClusterTctPortSpeed_Type())
tptNgfwClusterTctPortSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterTctPortSpeed.setStatus(_B)
_TptNgfwClusterTctPortDuplex_Type=DuplexSetting
_TptNgfwClusterTctPortDuplex_Object=MibScalar
tptNgfwClusterTctPortDuplex=_TptNgfwClusterTctPortDuplex_Object((1,3,6,1,4,1,10734,3,9,2,2,10,11),_TptNgfwClusterTctPortDuplex_Type())
tptNgfwClusterTctPortDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterTctPortDuplex.setStatus(_B)
_TptNgfwClusterTctPortAutoNeg_Type=AutoNegotiation
_TptNgfwClusterTctPortAutoNeg_Object=MibScalar
tptNgfwClusterTctPortAutoNeg=_TptNgfwClusterTctPortAutoNeg_Object((1,3,6,1,4,1,10734,3,9,2,2,10,12),_TptNgfwClusterTctPortAutoNeg_Type())
tptNgfwClusterTctPortAutoNeg.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterTctPortAutoNeg.setStatus(_B)
_TptNgfwClusterTctLinkState_Type=LinkState
_TptNgfwClusterTctLinkState_Object=MibScalar
tptNgfwClusterTctLinkState=_TptNgfwClusterTctLinkState_Object((1,3,6,1,4,1,10734,3,9,2,2,10,13),_TptNgfwClusterTctLinkState_Type())
tptNgfwClusterTctLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterTctLinkState.setStatus(_B)
_TptNgfwClusterTctEncryptionEnabled_Type=TruthValue
_TptNgfwClusterTctEncryptionEnabled_Object=MibScalar
tptNgfwClusterTctEncryptionEnabled=_TptNgfwClusterTctEncryptionEnabled_Object((1,3,6,1,4,1,10734,3,9,2,2,10,14),_TptNgfwClusterTctEncryptionEnabled_Type())
tptNgfwClusterTctEncryptionEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterTctEncryptionEnabled.setStatus(_B)
_TptNgfwClusterHa_ObjectIdentity=ObjectIdentity
tptNgfwClusterHa=_TptNgfwClusterHa_ObjectIdentity((1,3,6,1,4,1,10734,3,9,2,2,11))
_TptNgfwClusterHaEnabled_Type=TruthValue
_TptNgfwClusterHaEnabled_Object=MibScalar
tptNgfwClusterHaEnabled=_TptNgfwClusterHaEnabled_Object((1,3,6,1,4,1,10734,3,9,2,2,11,1),_TptNgfwClusterHaEnabled_Type())
tptNgfwClusterHaEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaEnabled.setStatus(_B)
_TptNgfwClusterHaGlobalStateSyncEnabled_Type=TruthValue
_TptNgfwClusterHaGlobalStateSyncEnabled_Object=MibScalar
tptNgfwClusterHaGlobalStateSyncEnabled=_TptNgfwClusterHaGlobalStateSyncEnabled_Object((1,3,6,1,4,1,10734,3,9,2,2,11,2),_TptNgfwClusterHaGlobalStateSyncEnabled_Type())
tptNgfwClusterHaGlobalStateSyncEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaGlobalStateSyncEnabled.setStatus(_B)
_TptNgfwClusterHaMode_Type=HaState
_TptNgfwClusterHaMode_Object=MibScalar
tptNgfwClusterHaMode=_TptNgfwClusterHaMode_Object((1,3,6,1,4,1,10734,3,9,2,2,11,3),_TptNgfwClusterHaMode_Type())
tptNgfwClusterHaMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaMode.setStatus(_B)
_TptNgfwClusterHaFeatSyncTable_Object=MibTable
tptNgfwClusterHaFeatSyncTable=_TptNgfwClusterHaFeatSyncTable_Object((1,3,6,1,4,1,10734,3,9,2,2,11,4))
if mibBuilder.loadTexts:tptNgfwClusterHaFeatSyncTable.setStatus(_B)
_TptNgfwClusterHaFeatSyncTableEntry_Object=MibTableRow
tptNgfwClusterHaFeatSyncTableEntry=_TptNgfwClusterHaFeatSyncTableEntry_Object((1,3,6,1,4,1,10734,3,9,2,2,11,4,1))
tptNgfwClusterHaFeatSyncTableEntry.setIndexNames((0,_A,_p))
if mibBuilder.loadTexts:tptNgfwClusterHaFeatSyncTableEntry.setStatus(_B)
class _TptNgfwClusterHaFeatSyncFeature_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TptNgfwClusterHaFeatSyncFeature_Type.__name__=_E
_TptNgfwClusterHaFeatSyncFeature_Object=MibTableColumn
tptNgfwClusterHaFeatSyncFeature=_TptNgfwClusterHaFeatSyncFeature_Object((1,3,6,1,4,1,10734,3,9,2,2,11,4,1,1),_TptNgfwClusterHaFeatSyncFeature_Type())
tptNgfwClusterHaFeatSyncFeature.setMaxAccess(_N)
if mibBuilder.loadTexts:tptNgfwClusterHaFeatSyncFeature.setStatus(_B)
_TptNgfwClusterHaFeatSyncEnabled_Type=TruthValue
_TptNgfwClusterHaFeatSyncEnabled_Object=MibTableColumn
tptNgfwClusterHaFeatSyncEnabled=_TptNgfwClusterHaFeatSyncEnabled_Object((1,3,6,1,4,1,10734,3,9,2,2,11,4,1,2),_TptNgfwClusterHaFeatSyncEnabled_Type())
tptNgfwClusterHaFeatSyncEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaFeatSyncEnabled.setStatus(_B)
_TptNgfwClusterHaFeatSyncLogSeverity_Type=Severity
_TptNgfwClusterHaFeatSyncLogSeverity_Object=MibTableColumn
tptNgfwClusterHaFeatSyncLogSeverity=_TptNgfwClusterHaFeatSyncLogSeverity_Object((1,3,6,1,4,1,10734,3,9,2,2,11,4,1,3),_TptNgfwClusterHaFeatSyncLogSeverity_Type())
tptNgfwClusterHaFeatSyncLogSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaFeatSyncLogSeverity.setStatus(_B)
_TptNgfwClusterHaFgTable_Object=MibTable
tptNgfwClusterHaFgTable=_TptNgfwClusterHaFgTable_Object((1,3,6,1,4,1,10734,3,9,2,2,11,5))
if mibBuilder.loadTexts:tptNgfwClusterHaFgTable.setStatus(_B)
_TptNgfwClusterHaFgEntry_Object=MibTableRow
tptNgfwClusterHaFgEntry=_TptNgfwClusterHaFgEntry_Object((1,3,6,1,4,1,10734,3,9,2,2,11,5,1))
tptNgfwClusterHaFgEntry.setIndexNames((0,_A,_q))
if mibBuilder.loadTexts:tptNgfwClusterHaFgEntry.setStatus(_B)
_TptNgfwClusterHaFgIndex_Type=Unsigned32
_TptNgfwClusterHaFgIndex_Object=MibTableColumn
tptNgfwClusterHaFgIndex=_TptNgfwClusterHaFgIndex_Object((1,3,6,1,4,1,10734,3,9,2,2,11,5,1,1),_TptNgfwClusterHaFgIndex_Type())
tptNgfwClusterHaFgIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:tptNgfwClusterHaFgIndex.setStatus(_B)
class _TptNgfwClusterHaFgId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TptNgfwClusterHaFgId_Type.__name__=_F
_TptNgfwClusterHaFgId_Object=MibTableColumn
tptNgfwClusterHaFgId=_TptNgfwClusterHaFgId_Object((1,3,6,1,4,1,10734,3,9,2,2,11,5,1,2),_TptNgfwClusterHaFgId_Type())
tptNgfwClusterHaFgId.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaFgId.setStatus(_B)
class _TptNgfwClusterHaFgName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TptNgfwClusterHaFgName_Type.__name__=_E
_TptNgfwClusterHaFgName_Object=MibTableColumn
tptNgfwClusterHaFgName=_TptNgfwClusterHaFgName_Object((1,3,6,1,4,1,10734,3,9,2,2,11,5,1,3),_TptNgfwClusterHaFgName_Type())
tptNgfwClusterHaFgName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaFgName.setStatus(_B)
_TptNgfwClusterHaFgBaseMac_Type=MacAddress
_TptNgfwClusterHaFgBaseMac_Object=MibTableColumn
tptNgfwClusterHaFgBaseMac=_TptNgfwClusterHaFgBaseMac_Object((1,3,6,1,4,1,10734,3,9,2,2,11,5,1,4),_TptNgfwClusterHaFgBaseMac_Type())
tptNgfwClusterHaFgBaseMac.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaFgBaseMac.setStatus(_B)
_TptNgfwClusterHaFgMode_Type=FailoverGrpMode
_TptNgfwClusterHaFgMode_Object=MibTableColumn
tptNgfwClusterHaFgMode=_TptNgfwClusterHaFgMode_Object((1,3,6,1,4,1,10734,3,9,2,2,11,5,1,5),_TptNgfwClusterHaFgMode_Type())
tptNgfwClusterHaFgMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaFgMode.setStatus(_B)
_TptNgfwClusterHaFgMemberTable_Object=MibTable
tptNgfwClusterHaFgMemberTable=_TptNgfwClusterHaFgMemberTable_Object((1,3,6,1,4,1,10734,3,9,2,2,11,6))
if mibBuilder.loadTexts:tptNgfwClusterHaFgMemberTable.setStatus(_B)
_TptNgfwClusterHaFgMemberEntry_Object=MibTableRow
tptNgfwClusterHaFgMemberEntry=_TptNgfwClusterHaFgMemberEntry_Object((1,3,6,1,4,1,10734,3,9,2,2,11,6,1))
tptNgfwClusterHaFgMemberEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:tptNgfwClusterHaFgMemberEntry.setStatus(_B)
class _TptNgfwClusterHaFgMemberId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_TptNgfwClusterHaFgMemberId_Type.__name__=_F
_TptNgfwClusterHaFgMemberId_Object=MibTableColumn
tptNgfwClusterHaFgMemberId=_TptNgfwClusterHaFgMemberId_Object((1,3,6,1,4,1,10734,3,9,2,2,11,6,1,1),_TptNgfwClusterHaFgMemberId_Type())
tptNgfwClusterHaFgMemberId.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaFgMemberId.setStatus(_B)
class _TptNgfwClusterHaFgMemberName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TptNgfwClusterHaFgMemberName_Type.__name__=_E
_TptNgfwClusterHaFgMemberName_Object=MibTableColumn
tptNgfwClusterHaFgMemberName=_TptNgfwClusterHaFgMemberName_Object((1,3,6,1,4,1,10734,3,9,2,2,11,6,1,2),_TptNgfwClusterHaFgMemberName_Type())
tptNgfwClusterHaFgMemberName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaFgMemberName.setStatus(_B)
_TptNgfwClusterHaFeatSyncStatusTable_Object=MibTable
tptNgfwClusterHaFeatSyncStatusTable=_TptNgfwClusterHaFeatSyncStatusTable_Object((1,3,6,1,4,1,10734,3,9,2,2,11,7))
if mibBuilder.loadTexts:tptNgfwClusterHaFeatSyncStatusTable.setStatus(_B)
_TptNgfwClusterHaFeatSyncStatusTableEntry_Object=MibTableRow
tptNgfwClusterHaFeatSyncStatusTableEntry=_TptNgfwClusterHaFeatSyncStatusTableEntry_Object((1,3,6,1,4,1,10734,3,9,2,2,11,7,1))
tptNgfwClusterHaFeatSyncStatusTableEntry.setIndexNames((0,_A,_r))
if mibBuilder.loadTexts:tptNgfwClusterHaFeatSyncStatusTableEntry.setStatus(_B)
class _TptNgfwClusterHaFeatSyncStatusFeature_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TptNgfwClusterHaFeatSyncStatusFeature_Type.__name__=_E
_TptNgfwClusterHaFeatSyncStatusFeature_Object=MibTableColumn
tptNgfwClusterHaFeatSyncStatusFeature=_TptNgfwClusterHaFeatSyncStatusFeature_Object((1,3,6,1,4,1,10734,3,9,2,2,11,7,1,1),_TptNgfwClusterHaFeatSyncStatusFeature_Type())
tptNgfwClusterHaFeatSyncStatusFeature.setMaxAccess(_N)
if mibBuilder.loadTexts:tptNgfwClusterHaFeatSyncStatusFeature.setStatus(_B)
_TptNgfwClusterHaFeatSyncStatusEnabled_Type=TruthValue
_TptNgfwClusterHaFeatSyncStatusEnabled_Object=MibTableColumn
tptNgfwClusterHaFeatSyncStatusEnabled=_TptNgfwClusterHaFeatSyncStatusEnabled_Object((1,3,6,1,4,1,10734,3,9,2,2,11,7,1,2),_TptNgfwClusterHaFeatSyncStatusEnabled_Type())
tptNgfwClusterHaFeatSyncStatusEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaFeatSyncStatusEnabled.setStatus(_B)
_TptNgfwClusterHaFeatSyncStatusSyncState_Type=SyncState
_TptNgfwClusterHaFeatSyncStatusSyncState_Object=MibTableColumn
tptNgfwClusterHaFeatSyncStatusSyncState=_TptNgfwClusterHaFeatSyncStatusSyncState_Object((1,3,6,1,4,1,10734,3,9,2,2,11,7,1,3),_TptNgfwClusterHaFeatSyncStatusSyncState_Type())
tptNgfwClusterHaFeatSyncStatusSyncState.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaFeatSyncStatusSyncState.setStatus(_B)
class _TptNgfwClusterHaFeatSyncStatusSyncStateReason_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TptNgfwClusterHaFeatSyncStatusSyncStateReason_Type.__name__=_E
_TptNgfwClusterHaFeatSyncStatusSyncStateReason_Object=MibTableColumn
tptNgfwClusterHaFeatSyncStatusSyncStateReason=_TptNgfwClusterHaFeatSyncStatusSyncStateReason_Object((1,3,6,1,4,1,10734,3,9,2,2,11,7,1,4),_TptNgfwClusterHaFeatSyncStatusSyncStateReason_Type())
tptNgfwClusterHaFeatSyncStatusSyncStateReason.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaFeatSyncStatusSyncStateReason.setStatus(_B)
_TptNgfwClusterHaFeatSyncStatusTotalEntries_Type=Counter64
_TptNgfwClusterHaFeatSyncStatusTotalEntries_Object=MibTableColumn
tptNgfwClusterHaFeatSyncStatusTotalEntries=_TptNgfwClusterHaFeatSyncStatusTotalEntries_Object((1,3,6,1,4,1,10734,3,9,2,2,11,7,1,5),_TptNgfwClusterHaFeatSyncStatusTotalEntries_Type())
tptNgfwClusterHaFeatSyncStatusTotalEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaFeatSyncStatusTotalEntries.setStatus(_B)
_TptNgfwClusterHaFeatSyncStatusAddEntries_Type=Counter64
_TptNgfwClusterHaFeatSyncStatusAddEntries_Object=MibTableColumn
tptNgfwClusterHaFeatSyncStatusAddEntries=_TptNgfwClusterHaFeatSyncStatusAddEntries_Object((1,3,6,1,4,1,10734,3,9,2,2,11,7,1,6),_TptNgfwClusterHaFeatSyncStatusAddEntries_Type())
tptNgfwClusterHaFeatSyncStatusAddEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaFeatSyncStatusAddEntries.setStatus(_B)
_TptNgfwClusterHaFeatSyncStatusDelEntries_Type=Counter64
_TptNgfwClusterHaFeatSyncStatusDelEntries_Object=MibTableColumn
tptNgfwClusterHaFeatSyncStatusDelEntries=_TptNgfwClusterHaFeatSyncStatusDelEntries_Object((1,3,6,1,4,1,10734,3,9,2,2,11,7,1,7),_TptNgfwClusterHaFeatSyncStatusDelEntries_Type())
tptNgfwClusterHaFeatSyncStatusDelEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwClusterHaFeatSyncStatusDelEntries.setStatus(_B)
_TptNgfwClusterMemberRejectNotifyReason_Type=ClusterMemberRejectReason
_TptNgfwClusterMemberRejectNotifyReason_Object=MibScalar
tptNgfwClusterMemberRejectNotifyReason=_TptNgfwClusterMemberRejectNotifyReason_Object((1,3,6,1,4,1,10734,3,9,3,1,1),_TptNgfwClusterMemberRejectNotifyReason_Type())
tptNgfwClusterMemberRejectNotifyReason.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterMemberRejectNotifyReason.setStatus(_B)
class _TptNgfwClusterHaStateSyncNotifyFeature_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TptNgfwClusterHaStateSyncNotifyFeature_Type.__name__=_E
_TptNgfwClusterHaStateSyncNotifyFeature_Object=MibScalar
tptNgfwClusterHaStateSyncNotifyFeature=_TptNgfwClusterHaStateSyncNotifyFeature_Object((1,3,6,1,4,1,10734,3,9,3,1,2),_TptNgfwClusterHaStateSyncNotifyFeature_Type())
tptNgfwClusterHaStateSyncNotifyFeature.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterHaStateSyncNotifyFeature.setStatus(_B)
_TptNgfwClusterHealthChangeNotifyState_Type=HealthState
_TptNgfwClusterHealthChangeNotifyState_Object=MibScalar
tptNgfwClusterHealthChangeNotifyState=_TptNgfwClusterHealthChangeNotifyState_Object((1,3,6,1,4,1,10734,3,9,3,1,3),_TptNgfwClusterHealthChangeNotifyState_Type())
tptNgfwClusterHealthChangeNotifyState.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterHealthChangeNotifyState.setStatus(_B)
class _TptNgfwClusterHealthChangeNotifyScore_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TptNgfwClusterHealthChangeNotifyScore_Type.__name__=_F
_TptNgfwClusterHealthChangeNotifyScore_Object=MibScalar
tptNgfwClusterHealthChangeNotifyScore=_TptNgfwClusterHealthChangeNotifyScore_Object((1,3,6,1,4,1,10734,3,9,3,1,4),_TptNgfwClusterHealthChangeNotifyScore_Type())
tptNgfwClusterHealthChangeNotifyScore.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterHealthChangeNotifyScore.setStatus(_B)
class _TptNgfwClusterHealthChangeNotifyStateUpperLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TptNgfwClusterHealthChangeNotifyStateUpperLimit_Type.__name__=_F
_TptNgfwClusterHealthChangeNotifyStateUpperLimit_Object=MibScalar
tptNgfwClusterHealthChangeNotifyStateUpperLimit=_TptNgfwClusterHealthChangeNotifyStateUpperLimit_Object((1,3,6,1,4,1,10734,3,9,3,1,5),_TptNgfwClusterHealthChangeNotifyStateUpperLimit_Type())
tptNgfwClusterHealthChangeNotifyStateUpperLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterHealthChangeNotifyStateUpperLimit.setStatus(_B)
class _TptNgfwClusterHealthChangeNotifyStateLowerLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TptNgfwClusterHealthChangeNotifyStateLowerLimit_Type.__name__=_F
_TptNgfwClusterHealthChangeNotifyStateLowerLimit_Object=MibScalar
tptNgfwClusterHealthChangeNotifyStateLowerLimit=_TptNgfwClusterHealthChangeNotifyStateLowerLimit_Object((1,3,6,1,4,1,10734,3,9,3,1,6),_TptNgfwClusterHealthChangeNotifyStateLowerLimit_Type())
tptNgfwClusterHealthChangeNotifyStateLowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterHealthChangeNotifyStateLowerLimit.setStatus(_B)
_TptNgfwClusterHaFgStateChangeNotifyState_Type=FailoverGroupState
_TptNgfwClusterHaFgStateChangeNotifyState_Object=MibScalar
tptNgfwClusterHaFgStateChangeNotifyState=_TptNgfwClusterHaFgStateChangeNotifyState_Object((1,3,6,1,4,1,10734,3,9,3,1,7),_TptNgfwClusterHaFgStateChangeNotifyState_Type())
tptNgfwClusterHaFgStateChangeNotifyState.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterHaFgStateChangeNotifyState.setStatus(_B)
class _TptNgfwClusterHaFgStateChangeNotifyActiveDeviceId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TptNgfwClusterHaFgStateChangeNotifyActiveDeviceId_Type.__name__=_F
_TptNgfwClusterHaFgStateChangeNotifyActiveDeviceId_Object=MibScalar
tptNgfwClusterHaFgStateChangeNotifyActiveDeviceId=_TptNgfwClusterHaFgStateChangeNotifyActiveDeviceId_Object((1,3,6,1,4,1,10734,3,9,3,1,8),_TptNgfwClusterHaFgStateChangeNotifyActiveDeviceId_Type())
tptNgfwClusterHaFgStateChangeNotifyActiveDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterHaFgStateChangeNotifyActiveDeviceId.setStatus(_B)
class _TptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_TptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId_Type.__name__=_F
_TptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId_Object=MibScalar
tptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId=_TptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId_Object((1,3,6,1,4,1,10734,3,9,3,1,9),_TptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId_Type())
tptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId.setStatus(_B)
_TptNgfwClusterCmpStateChangeNotifyType_Type=ComponentType
_TptNgfwClusterCmpStateChangeNotifyType_Object=MibScalar
tptNgfwClusterCmpStateChangeNotifyType=_TptNgfwClusterCmpStateChangeNotifyType_Object((1,3,6,1,4,1,10734,3,9,3,1,10),_TptNgfwClusterCmpStateChangeNotifyType_Type())
tptNgfwClusterCmpStateChangeNotifyType.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterCmpStateChangeNotifyType.setStatus(_B)
class _TptNgfwClusterCmpStateChangeNotifyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TptNgfwClusterCmpStateChangeNotifyName_Type.__name__=_E
_TptNgfwClusterCmpStateChangeNotifyName_Object=MibScalar
tptNgfwClusterCmpStateChangeNotifyName=_TptNgfwClusterCmpStateChangeNotifyName_Object((1,3,6,1,4,1,10734,3,9,3,1,11),_TptNgfwClusterCmpStateChangeNotifyName_Type())
tptNgfwClusterCmpStateChangeNotifyName.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterCmpStateChangeNotifyName.setStatus(_B)
_TptNgfwClusterCmpStateChangeNotifyState_Type=HealthState
_TptNgfwClusterCmpStateChangeNotifyState_Object=MibScalar
tptNgfwClusterCmpStateChangeNotifyState=_TptNgfwClusterCmpStateChangeNotifyState_Object((1,3,6,1,4,1,10734,3,9,3,1,12),_TptNgfwClusterCmpStateChangeNotifyState_Type())
tptNgfwClusterCmpStateChangeNotifyState.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterCmpStateChangeNotifyState.setStatus(_B)
class _TptNgfwClusterCmpStateChangeNotifyValue_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TptNgfwClusterCmpStateChangeNotifyValue_Type.__name__=_E
_TptNgfwClusterCmpStateChangeNotifyValue_Object=MibScalar
tptNgfwClusterCmpStateChangeNotifyValue=_TptNgfwClusterCmpStateChangeNotifyValue_Object((1,3,6,1,4,1,10734,3,9,3,1,13),_TptNgfwClusterCmpStateChangeNotifyValue_Type())
tptNgfwClusterCmpStateChangeNotifyValue.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterCmpStateChangeNotifyValue.setStatus(_B)
class _TptNgfwClusterCmpStateChangeNotifyUnits_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_TptNgfwClusterCmpStateChangeNotifyUnits_Type.__name__=_E
_TptNgfwClusterCmpStateChangeNotifyUnits_Object=MibScalar
tptNgfwClusterCmpStateChangeNotifyUnits=_TptNgfwClusterCmpStateChangeNotifyUnits_Object((1,3,6,1,4,1,10734,3,9,3,1,14),_TptNgfwClusterCmpStateChangeNotifyUnits_Type())
tptNgfwClusterCmpStateChangeNotifyUnits.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterCmpStateChangeNotifyUnits.setStatus(_B)
class _TptNgfwClusterCmpStateChangeNotifyThreshold_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TptNgfwClusterCmpStateChangeNotifyThreshold_Type.__name__=_E
_TptNgfwClusterCmpStateChangeNotifyThreshold_Object=MibScalar
tptNgfwClusterCmpStateChangeNotifyThreshold=_TptNgfwClusterCmpStateChangeNotifyThreshold_Object((1,3,6,1,4,1,10734,3,9,3,1,15),_TptNgfwClusterCmpStateChangeNotifyThreshold_Type())
tptNgfwClusterCmpStateChangeNotifyThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterCmpStateChangeNotifyThreshold.setStatus(_B)
_TptNgfwClusterCmpStateChangeNotifyLimitType_Type=ThresholdLimitType
_TptNgfwClusterCmpStateChangeNotifyLimitType_Object=MibScalar
tptNgfwClusterCmpStateChangeNotifyLimitType=_TptNgfwClusterCmpStateChangeNotifyLimitType_Object((1,3,6,1,4,1,10734,3,9,3,1,16),_TptNgfwClusterCmpStateChangeNotifyLimitType_Type())
tptNgfwClusterCmpStateChangeNotifyLimitType.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterCmpStateChangeNotifyLimitType.setStatus(_B)
_TptNgfwClusterCmpStateChangeNotifyRelation_Type=ThresholdRelation
_TptNgfwClusterCmpStateChangeNotifyRelation_Object=MibScalar
tptNgfwClusterCmpStateChangeNotifyRelation=_TptNgfwClusterCmpStateChangeNotifyRelation_Object((1,3,6,1,4,1,10734,3,9,3,1,17),_TptNgfwClusterCmpStateChangeNotifyRelation_Type())
tptNgfwClusterCmpStateChangeNotifyRelation.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterCmpStateChangeNotifyRelation.setStatus(_B)
_TptNgfwClusterConstChkFailedNotifyType_Type=ConsistencyCheckType
_TptNgfwClusterConstChkFailedNotifyType_Object=MibScalar
tptNgfwClusterConstChkFailedNotifyType=_TptNgfwClusterConstChkFailedNotifyType_Object((1,3,6,1,4,1,10734,3,9,3,1,18),_TptNgfwClusterConstChkFailedNotifyType_Type())
tptNgfwClusterConstChkFailedNotifyType.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterConstChkFailedNotifyType.setStatus(_B)
_TptNgfwClusterConstChkFailedNotifyMaster_Type=MasterLocation
_TptNgfwClusterConstChkFailedNotifyMaster_Object=MibScalar
tptNgfwClusterConstChkFailedNotifyMaster=_TptNgfwClusterConstChkFailedNotifyMaster_Object((1,3,6,1,4,1,10734,3,9,3,1,19),_TptNgfwClusterConstChkFailedNotifyMaster_Type())
tptNgfwClusterConstChkFailedNotifyMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:tptNgfwClusterConstChkFailedNotifyMaster.setStatus(_B)
tptNgfwClusterGroup=ObjectGroup((1,3,6,1,4,1,10734,3,9,1,1,2))
tptNgfwClusterGroup.setObjects(*((_A,_P),(_A,_s),(_A,_K),(_A,_Q),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:tptNgfwClusterGroup.setStatus(_B)
tptNgfwClusterTrafficGroup=ObjectGroup((1,3,6,1,4,1,10734,3,9,1,1,3))
tptNgfwClusterTrafficGroup.setObjects(*((_A,_L),(_A,_M),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:tptNgfwClusterTrafficGroup.setStatus(_B)
tptNgfwClusterHaGroup=ObjectGroup((1,3,6,1,4,1,10734,3,9,1,1,4))
tptNgfwClusterHaGroup.setObjects(*((_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_O),(_A,_h),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_R),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:tptNgfwClusterHaGroup.setStatus(_B)
tptNgfwClusterMemberJoinNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,1))
tptNgfwClusterMemberJoinNotify.setObjects(*((_I,_J),(_A,_P),(_A,_K),(_A,_Q),(_A,_L),(_A,_M),(_G,_H)))
if mibBuilder.loadTexts:tptNgfwClusterMemberJoinNotify.setStatus(_B)
tptNgfwClusterMemberLeaveNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,2))
tptNgfwClusterMemberLeaveNotify.setObjects(*((_I,_J),(_A,_P),(_A,_K),(_A,_Q),(_A,_L),(_A,_M),(_G,_H)))
if mibBuilder.loadTexts:tptNgfwClusterMemberLeaveNotify.setStatus(_B)
tptNgfwClusterMemberRejectNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,3))
tptNgfwClusterMemberRejectNotify.setObjects(*((_I,_J),(_A,_L),(_A,_M),(_A,_K),(_A,_S),(_G,_H)))
if mibBuilder.loadTexts:tptNgfwClusterMemberRejectNotify.setStatus(_B)
tptNgfwClusterHaStateSyncMessageLossNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,4))
tptNgfwClusterHaStateSyncMessageLossNotify.setObjects(*((_I,_J),(_A,_R),(_G,_H)))
if mibBuilder.loadTexts:tptNgfwClusterHaStateSyncMessageLossNotify.setStatus(_B)
tptNgfwClusterHaStateSyncQueueFullNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,5))
tptNgfwClusterHaStateSyncQueueFullNotify.setObjects(*((_I,_J),(_A,_R),(_G,_H)))
if mibBuilder.loadTexts:tptNgfwClusterHaStateSyncQueueFullNotify.setStatus(_B)
tptNgfwClusterHealthChangeNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,6))
tptNgfwClusterHealthChangeNotify.setObjects(*((_I,_J),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_G,_H)))
if mibBuilder.loadTexts:tptNgfwClusterHealthChangeNotify.setStatus(_B)
tptNgfwClusterHaFgStateChangeNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,7))
tptNgfwClusterHaFgStateChangeNotify.setObjects(*((_I,_J),(_A,_h),(_A,_O),(_A,_i),(_A,_j),(_A,_k),(_G,_H)))
if mibBuilder.loadTexts:tptNgfwClusterHaFgStateChangeNotify.setStatus(_B)
tptNgfwClusterCmpStateChangeNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,8))
tptNgfwClusterCmpStateChangeNotify.setObjects(*((_I,_J),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_G,_H)))
if mibBuilder.loadTexts:tptNgfwClusterCmpStateChangeNotify.setStatus(_B)
tptNgfwClusterConstChkFailedNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,9))
tptNgfwClusterConstChkFailedNotify.setObjects(*((_I,_J),(_A,_f),(_A,_g),(_G,_H)))
if mibBuilder.loadTexts:tptNgfwClusterConstChkFailedNotify.setStatus(_B)
tptNgfwClusterNotificationGroup=NotificationGroup((1,3,6,1,4,1,10734,3,9,1,1,5))
tptNgfwClusterNotificationGroup.setObjects(*((_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak)))
if mibBuilder.loadTexts:tptNgfwClusterNotificationGroup.setStatus(_B)
tptNgfwClusterCfgCompl=ModuleCompliance((1,3,6,1,4,1,10734,3,9,1,2,2))
tptNgfwClusterCfgCompl.setObjects(*((_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao)))
if mibBuilder.loadTexts:tptNgfwClusterCfgCompl.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'FailoverGrpMode':FailoverGrpMode,'LinkState':LinkState,'CfgControl':CfgControl,'SyncState':SyncState,'HaState':HaState,'HealthState':HealthState,'ClusterMemberRejectReason':ClusterMemberRejectReason,'FailoverGroupState':FailoverGroupState,'ComponentType':ComponentType,'ThresholdLimitType':ThresholdLimitType,'ThresholdRelation':ThresholdRelation,'ConsistencyCheckType':ConsistencyCheckType,'MasterLocation':MasterLocation,_Al:tptNgfwClusterGroup,_Am:tptNgfwClusterTrafficGroup,_An:tptNgfwClusterHaGroup,_Ao:tptNgfwClusterNotificationGroup,'tptNgfwClusterCfgCompl':tptNgfwClusterCfgCompl,'tptNgfwCluster':tptNgfwCluster,_P:tptNgfwClusterName,_s:tptNgfwClusterEnabled,_K:tptNgfwClusterMemberId,_Q:tptNgfwClusterMemberName,_t:tptNgfwClusterStandby,_u:tptNgfwClusterSwConstChecks,_v:tptNgfwClusterHwConstChecks,_w:tptNgfwClusterCfgConstChecks,'tptNgfwClusterMemberStatusTable':tptNgfwClusterMemberStatusTable,'tptNgfwClusterMemberStatusTableEntry':tptNgfwClusterMemberStatusTableEntry,_o:tptNgfwClusterMemberStatusId,_x:tptNgfwClusterMemberStatusName,_y:tptNgfwClusterMemberStatusSerialNo,_z:tptNgfwClusterMemberStatusHwModel,_A0:tptNgfwClusterMemberStatusSwVersion,_A1:tptNgfwClusterMemberStatusUptime,_A2:tptNgfwClusterMemberStatusJoinTime,_A3:tptNgfwClusterMemberStatusSmsManaged,_A4:tptNgfwClusterMemberStatusCfgControl,_A5:tptNgfwClusterMemberStatusCfgStateSync,_A6:tptNgfwClusterMemberStatusEnabled,_A7:tptNgfwClusterMemberStatusHaState,_A8:tptNgfwClusterMemberStatusHealthState,_A9:tptNgfwClusterMemberStatusHealthScore,_AA:tptNgfwClusterMemberStatusMaster,'tptNgfwClusterTraffic':tptNgfwClusterTraffic,_L:tptNgfwClusterTctIpAddrType,_M:tptNgfwClusterTctIpAddr,_AB:tptNgfwClusterTctMulticastAddrType,_AC:tptNgfwClusterTctMulticastAddr,_AD:tptNgfwClusterTctPort,_AE:tptNgfwClusterTctTtl,_AF:tptNgfwClusterTctMtu,_AG:tptNgfwClusterTctTimeout,_AH:tptNgfwClusterTctRetries,_AI:tptNgfwClusterTctPortSpeed,_AJ:tptNgfwClusterTctPortDuplex,_AK:tptNgfwClusterTctPortAutoNeg,_AL:tptNgfwClusterTctLinkState,_AM:tptNgfwClusterTctEncryptionEnabled,'tptNgfwClusterHa':tptNgfwClusterHa,_AN:tptNgfwClusterHaEnabled,_AO:tptNgfwClusterHaGlobalStateSyncEnabled,_AP:tptNgfwClusterHaMode,'tptNgfwClusterHaFeatSyncTable':tptNgfwClusterHaFeatSyncTable,'tptNgfwClusterHaFeatSyncTableEntry':tptNgfwClusterHaFeatSyncTableEntry,_p:tptNgfwClusterHaFeatSyncFeature,_AQ:tptNgfwClusterHaFeatSyncEnabled,_AR:tptNgfwClusterHaFeatSyncLogSeverity,'tptNgfwClusterHaFgTable':tptNgfwClusterHaFgTable,'tptNgfwClusterHaFgEntry':tptNgfwClusterHaFgEntry,_q:tptNgfwClusterHaFgIndex,_O:tptNgfwClusterHaFgId,_h:tptNgfwClusterHaFgName,_AS:tptNgfwClusterHaFgBaseMac,_AT:tptNgfwClusterHaFgMode,'tptNgfwClusterHaFgMemberTable':tptNgfwClusterHaFgMemberTable,'tptNgfwClusterHaFgMemberEntry':tptNgfwClusterHaFgMemberEntry,_AU:tptNgfwClusterHaFgMemberId,_AV:tptNgfwClusterHaFgMemberName,'tptNgfwClusterHaFeatSyncStatusTable':tptNgfwClusterHaFeatSyncStatusTable,'tptNgfwClusterHaFeatSyncStatusTableEntry':tptNgfwClusterHaFeatSyncStatusTableEntry,_r:tptNgfwClusterHaFeatSyncStatusFeature,_AW:tptNgfwClusterHaFeatSyncStatusEnabled,_AX:tptNgfwClusterHaFeatSyncStatusSyncState,_AY:tptNgfwClusterHaFeatSyncStatusSyncStateReason,_AZ:tptNgfwClusterHaFeatSyncStatusTotalEntries,_Aa:tptNgfwClusterHaFeatSyncStatusAddEntries,_Ab:tptNgfwClusterHaFeatSyncStatusDelEntries,_Ac:tptNgfwClusterMemberJoinNotify,_Ad:tptNgfwClusterMemberLeaveNotify,_Ae:tptNgfwClusterMemberRejectNotify,_Af:tptNgfwClusterHaStateSyncMessageLossNotify,_Ag:tptNgfwClusterHaStateSyncQueueFullNotify,_Ah:tptNgfwClusterHealthChangeNotify,_Ai:tptNgfwClusterHaFgStateChangeNotify,_Aj:tptNgfwClusterCmpStateChangeNotify,_Ak:tptNgfwClusterConstChkFailedNotify,_S:tptNgfwClusterMemberRejectNotifyReason,_R:tptNgfwClusterHaStateSyncNotifyFeature,_T:tptNgfwClusterHealthChangeNotifyState,_U:tptNgfwClusterHealthChangeNotifyScore,_V:tptNgfwClusterHealthChangeNotifyStateUpperLimit,_W:tptNgfwClusterHealthChangeNotifyStateLowerLimit,_i:tptNgfwClusterHaFgStateChangeNotifyState,_j:tptNgfwClusterHaFgStateChangeNotifyActiveDeviceId,_k:tptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId,_X:tptNgfwClusterCmpStateChangeNotifyType,_Y:tptNgfwClusterCmpStateChangeNotifyName,_Z:tptNgfwClusterCmpStateChangeNotifyState,_a:tptNgfwClusterCmpStateChangeNotifyValue,_b:tptNgfwClusterCmpStateChangeNotifyUnits,_c:tptNgfwClusterCmpStateChangeNotifyThreshold,_d:tptNgfwClusterCmpStateChangeNotifyLimitType,_e:tptNgfwClusterCmpStateChangeNotifyRelation,_f:tptNgfwClusterConstChkFailedNotifyType,_g:tptNgfwClusterConstChkFailedNotifyMaster})