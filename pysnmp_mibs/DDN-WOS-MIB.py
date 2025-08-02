_Ax='wosPrefsGroup'
_Aw='wosPoliciesGroup'
_Av='wosNodesGroup'
_Au='wosZonesGroup'
_At='wosClusterGroup'
_As='wosAlertsGroup'
_Ar='wosStatsGroup'
_Aq='wosNotificationsGroup'
_Ap='wosEventsGroup'
_Ao='wosTrapMessage'
_An='wosPrefSyslogRemoteHost'
_Am='wosPrefSyslogFacility'
_Al='wosPrefClientIpFilter'
_Ak='wosPrefMgmtIpFilter'
_Aj='wosPrefSnmpTrapCommunityName'
_Ai='wosPrefSnmpManager'
_Ah='wosPrefEmailAlertServer'
_Ag='wosPrefEmailAlertRecipient'
_Af='wosPrefEmailAlertFromAddr'
_Ae='wosPrefEmailAlertRmndrInterval'
_Ad='wosPrefEmailAlertNewInterval'
_Ac='wosPrefNodeDownDelay'
_Ab='wosPrefStoreUnderReplObjs'
_Aa='wosPolicyUsedCapacity'
_AZ='wosPolicyNonComplObjCountHigh'
_AY='wosPolicyNonComplObjCountLow'
_AX='wosPolicyObjCountHigh'
_AW='wosPolicyObjCountLow'
_AV='wosPolicyLocalDataProtection'
_AU='wosPolicyReplicationType'
_AT='wosPolicyReplicaCount'
_AS='wosPolicyReplicaZoneName'
_AR='wosPolicyName'
_AQ='wosPolicyId'
_AP='wosNodeDriveCapacity'
_AO='wosNodeDriveStatus'
_AN='wosNodeDriveSerialNbr'
_AM='wosNodeDriveModel'
_AL='wosNodeDriveMfgr'
_AK='wosNodeDriveNodeName'
_AJ='wosPendingNodeStatus'
_AI='wosPendingNodeAddress'
_AH='wosPendingNodeAddressType'
_AG='wosNodePercentFull'
_AF='wosNodeUsedCapacity'
_AE='wosNodeTotalCapacity'
_AD='wosNodeObjectCountHigh'
_AC='wosNodeObjectCountLow'
_AB='wosNodeFwVersion'
_AA='wosNodeStatus'
_A9='wosNodeZoneName'
_A8='wosNodeName'
_A7='wosZoneNodeCount'
_A6='wosZoneName'
_A5='wosClusterFreeCapacity'
_A4='wosClusterUsedCapacity'
_A3='wosClusterUsableCapacity'
_A2='wosClusterObjectCountHigh'
_A1='wosClusterObjectCountLow'
_A0='wosClusterConnectedClientsCount'
_z='wosClusterDisconnectedNodeCount'
_y='wosClusterActiveNodeCount'
_x='wosClusterTotalNodeCount'
_w='wosClusterPrimaryNodeAddress'
_v='wosClusterPrimaryNodeAddressType'
_u='wosClusterStatus'
_t='wosClusterId'
_s='wosClusterName'
_r='wosAlertDesc'
_q='wosAlertLocation'
_p='wosAlertType'
_o='wosAlertTime'
_n='wosAlertSeverity'
_m='wosStatsDeleteCount'
_l='wosStatsWriteCount'
_k='wosStatsReadCount'
_j='wosStatsWriteThroughput'
_i='wosStatsReadThroughput'
_h='wosStatsDeleteLatency'
_g='wosStatsWriteLatency'
_f='wosStatsReadLatency'
_e='wosStatsFDPS'
_d='wosStatsFWPS'
_c='wosStatsFRPS'
_b='wosPrefClientIpFilterIndex'
_a='wosPrefMgmtIpFilterIndex'
_Z='wosPrefSnmpManagerIndex'
_Y='wosPrefEmailAlertServerIndex'
_X='wosPrefEmailAlertRecipientIndex'
_W='wosPolicyReplicaIndex'
_V='wosPolicyIndex'
_U='wosNodeDriveSlotNbr'
_T='wosPendingNodeIndex'
_S='wosNodeIndex'
_R='wosAlertIndex'
_Q='kilobytes per second'
_P='Gauge32'
_O='wosTrapLocation'
_N='wosTrapType'
_M='wosTrapSeverity'
_L='wosTrapDesc'
_K='minutes'
_J='wosNodeAddress'
_I='wosNodeAddressType'
_H='wosZoneId'
_G='milliseconds'
_F='accessible-for-notify'
_E='gigabytes'
_D='not-accessible'
_C='read-only'
_B='DDN-WOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_P,'Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
wosMIB=ModuleIdentity((1,3,6,1,4,1,6894,4,1))
if mibBuilder.loadTexts:wosMIB.setRevisions(('2012-01-04 00:00',))
class WosSeverityLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('emergency',1),('alert',2),('critical',3),('error',4),('warning',5),('notice',6),('informational',7),('debug',8)))
class WosSyslogFacility(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('user',1),('mail',2),('daemon',3),('auth',4),('syslog',5),('lpr',6),('news',7),('uucp',8),('cron',9),('authpriv',10),('ftp',11),('local0',16),('local1',17),('local2',18),('local3',19),('local4',20),('local5',21),('local6',22),('local7',23)))
_Datadirect_ObjectIdentity=ObjectIdentity
datadirect=_Datadirect_ObjectIdentity((1,3,6,1,4,1,6894))
_Wos_ObjectIdentity=ObjectIdentity
wos=_Wos_ObjectIdentity((1,3,6,1,4,1,6894,4))
_WosNotifications_ObjectIdentity=ObjectIdentity
wosNotifications=_WosNotifications_ObjectIdentity((1,3,6,1,4,1,6894,4,1,0))
_WosObjects_ObjectIdentity=ObjectIdentity
wosObjects=_WosObjects_ObjectIdentity((1,3,6,1,4,1,6894,4,1,1))
_WosNotificationInfo_ObjectIdentity=ObjectIdentity
wosNotificationInfo=_WosNotificationInfo_ObjectIdentity((1,3,6,1,4,1,6894,4,1,1,1))
_WosTrapDesc_Type=DisplayString
_WosTrapDesc_Object=MibScalar
wosTrapDesc=_WosTrapDesc_Object((1,3,6,1,4,1,6894,4,1,1,1,1),_WosTrapDesc_Type())
wosTrapDesc.setMaxAccess(_F)
if mibBuilder.loadTexts:wosTrapDesc.setStatus(_A)
_WosTrapSeverity_Type=WosSeverityLevel
_WosTrapSeverity_Object=MibScalar
wosTrapSeverity=_WosTrapSeverity_Object((1,3,6,1,4,1,6894,4,1,1,1,2),_WosTrapSeverity_Type())
wosTrapSeverity.setMaxAccess(_F)
if mibBuilder.loadTexts:wosTrapSeverity.setStatus(_A)
_WosTrapType_Type=DisplayString
_WosTrapType_Object=MibScalar
wosTrapType=_WosTrapType_Object((1,3,6,1,4,1,6894,4,1,1,1,3),_WosTrapType_Type())
wosTrapType.setMaxAccess(_F)
if mibBuilder.loadTexts:wosTrapType.setStatus(_A)
_WosTrapLocation_Type=DisplayString
_WosTrapLocation_Object=MibScalar
wosTrapLocation=_WosTrapLocation_Object((1,3,6,1,4,1,6894,4,1,1,1,4),_WosTrapLocation_Type())
wosTrapLocation.setMaxAccess(_F)
if mibBuilder.loadTexts:wosTrapLocation.setStatus(_A)
_WosStatsInfo_ObjectIdentity=ObjectIdentity
wosStatsInfo=_WosStatsInfo_ObjectIdentity((1,3,6,1,4,1,6894,4,1,1,2))
_WosStatsFRPS_Type=Gauge32
_WosStatsFRPS_Object=MibScalar
wosStatsFRPS=_WosStatsFRPS_Object((1,3,6,1,4,1,6894,4,1,1,2,1),_WosStatsFRPS_Type())
wosStatsFRPS.setMaxAccess(_C)
if mibBuilder.loadTexts:wosStatsFRPS.setStatus(_A)
if mibBuilder.loadTexts:wosStatsFRPS.setUnits('file reads per second')
_WosStatsFWPS_Type=Gauge32
_WosStatsFWPS_Object=MibScalar
wosStatsFWPS=_WosStatsFWPS_Object((1,3,6,1,4,1,6894,4,1,1,2,2),_WosStatsFWPS_Type())
wosStatsFWPS.setMaxAccess(_C)
if mibBuilder.loadTexts:wosStatsFWPS.setStatus(_A)
if mibBuilder.loadTexts:wosStatsFWPS.setUnits('file writes per second')
_WosStatsFDPS_Type=Gauge32
_WosStatsFDPS_Object=MibScalar
wosStatsFDPS=_WosStatsFDPS_Object((1,3,6,1,4,1,6894,4,1,1,2,3),_WosStatsFDPS_Type())
wosStatsFDPS.setMaxAccess(_C)
if mibBuilder.loadTexts:wosStatsFDPS.setStatus(_A)
if mibBuilder.loadTexts:wosStatsFDPS.setUnits('file deletes per second')
_WosStatsReadLatency_Type=Gauge32
_WosStatsReadLatency_Object=MibScalar
wosStatsReadLatency=_WosStatsReadLatency_Object((1,3,6,1,4,1,6894,4,1,1,2,4),_WosStatsReadLatency_Type())
wosStatsReadLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:wosStatsReadLatency.setStatus(_A)
if mibBuilder.loadTexts:wosStatsReadLatency.setUnits(_G)
_WosStatsWriteLatency_Type=Gauge32
_WosStatsWriteLatency_Object=MibScalar
wosStatsWriteLatency=_WosStatsWriteLatency_Object((1,3,6,1,4,1,6894,4,1,1,2,5),_WosStatsWriteLatency_Type())
wosStatsWriteLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:wosStatsWriteLatency.setStatus(_A)
if mibBuilder.loadTexts:wosStatsWriteLatency.setUnits(_G)
_WosStatsDeleteLatency_Type=Gauge32
_WosStatsDeleteLatency_Object=MibScalar
wosStatsDeleteLatency=_WosStatsDeleteLatency_Object((1,3,6,1,4,1,6894,4,1,1,2,6),_WosStatsDeleteLatency_Type())
wosStatsDeleteLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:wosStatsDeleteLatency.setStatus(_A)
if mibBuilder.loadTexts:wosStatsDeleteLatency.setUnits(_G)
_WosStatsReadThroughput_Type=Gauge32
_WosStatsReadThroughput_Object=MibScalar
wosStatsReadThroughput=_WosStatsReadThroughput_Object((1,3,6,1,4,1,6894,4,1,1,2,7),_WosStatsReadThroughput_Type())
wosStatsReadThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:wosStatsReadThroughput.setStatus(_A)
if mibBuilder.loadTexts:wosStatsReadThroughput.setUnits(_Q)
_WosStatsWriteThroughput_Type=Gauge32
_WosStatsWriteThroughput_Object=MibScalar
wosStatsWriteThroughput=_WosStatsWriteThroughput_Object((1,3,6,1,4,1,6894,4,1,1,2,8),_WosStatsWriteThroughput_Type())
wosStatsWriteThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:wosStatsWriteThroughput.setStatus(_A)
if mibBuilder.loadTexts:wosStatsWriteThroughput.setUnits(_Q)
_WosStatsReadCount_Type=Counter64
_WosStatsReadCount_Object=MibScalar
wosStatsReadCount=_WosStatsReadCount_Object((1,3,6,1,4,1,6894,4,1,1,2,9),_WosStatsReadCount_Type())
wosStatsReadCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wosStatsReadCount.setStatus(_A)
_WosStatsWriteCount_Type=Counter64
_WosStatsWriteCount_Object=MibScalar
wosStatsWriteCount=_WosStatsWriteCount_Object((1,3,6,1,4,1,6894,4,1,1,2,10),_WosStatsWriteCount_Type())
wosStatsWriteCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wosStatsWriteCount.setStatus(_A)
_WosStatsDeleteCount_Type=Counter64
_WosStatsDeleteCount_Object=MibScalar
wosStatsDeleteCount=_WosStatsDeleteCount_Object((1,3,6,1,4,1,6894,4,1,1,2,11),_WosStatsDeleteCount_Type())
wosStatsDeleteCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wosStatsDeleteCount.setStatus(_A)
_WosAlertsInfo_ObjectIdentity=ObjectIdentity
wosAlertsInfo=_WosAlertsInfo_ObjectIdentity((1,3,6,1,4,1,6894,4,1,1,3))
_WosAlertTable_Object=MibTable
wosAlertTable=_WosAlertTable_Object((1,3,6,1,4,1,6894,4,1,1,3,1))
if mibBuilder.loadTexts:wosAlertTable.setStatus(_A)
_WosAlertEntry_Object=MibTableRow
wosAlertEntry=_WosAlertEntry_Object((1,3,6,1,4,1,6894,4,1,1,3,1,1))
wosAlertEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:wosAlertEntry.setStatus(_A)
_WosAlertIndex_Type=Unsigned32
_WosAlertIndex_Object=MibTableColumn
wosAlertIndex=_WosAlertIndex_Object((1,3,6,1,4,1,6894,4,1,1,3,1,1,1),_WosAlertIndex_Type())
wosAlertIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wosAlertIndex.setStatus(_A)
_WosAlertSeverity_Type=WosSeverityLevel
_WosAlertSeverity_Object=MibTableColumn
wosAlertSeverity=_WosAlertSeverity_Object((1,3,6,1,4,1,6894,4,1,1,3,1,1,2),_WosAlertSeverity_Type())
wosAlertSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:wosAlertSeverity.setStatus(_A)
_WosAlertTime_Type=DateAndTime
_WosAlertTime_Object=MibTableColumn
wosAlertTime=_WosAlertTime_Object((1,3,6,1,4,1,6894,4,1,1,3,1,1,3),_WosAlertTime_Type())
wosAlertTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wosAlertTime.setStatus(_A)
_WosAlertType_Type=DisplayString
_WosAlertType_Object=MibTableColumn
wosAlertType=_WosAlertType_Object((1,3,6,1,4,1,6894,4,1,1,3,1,1,4),_WosAlertType_Type())
wosAlertType.setMaxAccess(_C)
if mibBuilder.loadTexts:wosAlertType.setStatus(_A)
_WosAlertLocation_Type=DisplayString
_WosAlertLocation_Object=MibTableColumn
wosAlertLocation=_WosAlertLocation_Object((1,3,6,1,4,1,6894,4,1,1,3,1,1,5),_WosAlertLocation_Type())
wosAlertLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:wosAlertLocation.setStatus(_A)
_WosAlertDesc_Type=DisplayString
_WosAlertDesc_Object=MibTableColumn
wosAlertDesc=_WosAlertDesc_Object((1,3,6,1,4,1,6894,4,1,1,3,1,1,6),_WosAlertDesc_Type())
wosAlertDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:wosAlertDesc.setStatus(_A)
_WosClusterInfo_ObjectIdentity=ObjectIdentity
wosClusterInfo=_WosClusterInfo_ObjectIdentity((1,3,6,1,4,1,6894,4,1,1,4))
_WosClusterName_Type=DisplayString
_WosClusterName_Object=MibScalar
wosClusterName=_WosClusterName_Object((1,3,6,1,4,1,6894,4,1,1,4,1),_WosClusterName_Type())
wosClusterName.setMaxAccess(_C)
if mibBuilder.loadTexts:wosClusterName.setStatus(_A)
_WosClusterId_Type=DisplayString
_WosClusterId_Object=MibScalar
wosClusterId=_WosClusterId_Object((1,3,6,1,4,1,6894,4,1,1,4,2),_WosClusterId_Type())
wosClusterId.setMaxAccess(_C)
if mibBuilder.loadTexts:wosClusterId.setStatus(_A)
_WosClusterStatus_Type=DisplayString
_WosClusterStatus_Object=MibScalar
wosClusterStatus=_WosClusterStatus_Object((1,3,6,1,4,1,6894,4,1,1,4,3),_WosClusterStatus_Type())
wosClusterStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wosClusterStatus.setStatus(_A)
_WosClusterPrimaryNodeAddressType_Type=InetAddressType
_WosClusterPrimaryNodeAddressType_Object=MibScalar
wosClusterPrimaryNodeAddressType=_WosClusterPrimaryNodeAddressType_Object((1,3,6,1,4,1,6894,4,1,1,4,4),_WosClusterPrimaryNodeAddressType_Type())
wosClusterPrimaryNodeAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:wosClusterPrimaryNodeAddressType.setStatus(_A)
_WosClusterPrimaryNodeAddress_Type=InetAddress
_WosClusterPrimaryNodeAddress_Object=MibScalar
wosClusterPrimaryNodeAddress=_WosClusterPrimaryNodeAddress_Object((1,3,6,1,4,1,6894,4,1,1,4,5),_WosClusterPrimaryNodeAddress_Type())
wosClusterPrimaryNodeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:wosClusterPrimaryNodeAddress.setStatus(_A)
_WosClusterTotalNodeCount_Type=Unsigned32
_WosClusterTotalNodeCount_Object=MibScalar
wosClusterTotalNodeCount=_WosClusterTotalNodeCount_Object((1,3,6,1,4,1,6894,4,1,1,4,6),_WosClusterTotalNodeCount_Type())
wosClusterTotalNodeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wosClusterTotalNodeCount.setStatus(_A)
_WosClusterActiveNodeCount_Type=Unsigned32
_WosClusterActiveNodeCount_Object=MibScalar
wosClusterActiveNodeCount=_WosClusterActiveNodeCount_Object((1,3,6,1,4,1,6894,4,1,1,4,7),_WosClusterActiveNodeCount_Type())
wosClusterActiveNodeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wosClusterActiveNodeCount.setStatus(_A)
_WosClusterDisconnectedNodeCount_Type=Unsigned32
_WosClusterDisconnectedNodeCount_Object=MibScalar
wosClusterDisconnectedNodeCount=_WosClusterDisconnectedNodeCount_Object((1,3,6,1,4,1,6894,4,1,1,4,8),_WosClusterDisconnectedNodeCount_Type())
wosClusterDisconnectedNodeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wosClusterDisconnectedNodeCount.setStatus(_A)
_WosClusterConnectedClientsCount_Type=Unsigned32
_WosClusterConnectedClientsCount_Object=MibScalar
wosClusterConnectedClientsCount=_WosClusterConnectedClientsCount_Object((1,3,6,1,4,1,6894,4,1,1,4,9),_WosClusterConnectedClientsCount_Type())
wosClusterConnectedClientsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wosClusterConnectedClientsCount.setStatus(_A)
_WosClusterObjectCountLow_Type=Unsigned32
_WosClusterObjectCountLow_Object=MibScalar
wosClusterObjectCountLow=_WosClusterObjectCountLow_Object((1,3,6,1,4,1,6894,4,1,1,4,10),_WosClusterObjectCountLow_Type())
wosClusterObjectCountLow.setMaxAccess(_C)
if mibBuilder.loadTexts:wosClusterObjectCountLow.setStatus(_A)
_WosClusterObjectCountHigh_Type=Unsigned32
_WosClusterObjectCountHigh_Object=MibScalar
wosClusterObjectCountHigh=_WosClusterObjectCountHigh_Object((1,3,6,1,4,1,6894,4,1,1,4,11),_WosClusterObjectCountHigh_Type())
wosClusterObjectCountHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:wosClusterObjectCountHigh.setStatus(_A)
_WosClusterUsableCapacity_Type=Unsigned32
_WosClusterUsableCapacity_Object=MibScalar
wosClusterUsableCapacity=_WosClusterUsableCapacity_Object((1,3,6,1,4,1,6894,4,1,1,4,12),_WosClusterUsableCapacity_Type())
wosClusterUsableCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:wosClusterUsableCapacity.setStatus(_A)
if mibBuilder.loadTexts:wosClusterUsableCapacity.setUnits(_E)
_WosClusterUsedCapacity_Type=Unsigned32
_WosClusterUsedCapacity_Object=MibScalar
wosClusterUsedCapacity=_WosClusterUsedCapacity_Object((1,3,6,1,4,1,6894,4,1,1,4,13),_WosClusterUsedCapacity_Type())
wosClusterUsedCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:wosClusterUsedCapacity.setStatus(_A)
if mibBuilder.loadTexts:wosClusterUsedCapacity.setUnits(_E)
_WosClusterFreeCapacity_Type=Unsigned32
_WosClusterFreeCapacity_Object=MibScalar
wosClusterFreeCapacity=_WosClusterFreeCapacity_Object((1,3,6,1,4,1,6894,4,1,1,4,14),_WosClusterFreeCapacity_Type())
wosClusterFreeCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:wosClusterFreeCapacity.setStatus(_A)
if mibBuilder.loadTexts:wosClusterFreeCapacity.setUnits(_E)
_WosZonesInfo_ObjectIdentity=ObjectIdentity
wosZonesInfo=_WosZonesInfo_ObjectIdentity((1,3,6,1,4,1,6894,4,1,1,5))
_WosZoneTable_Object=MibTable
wosZoneTable=_WosZoneTable_Object((1,3,6,1,4,1,6894,4,1,1,5,1))
if mibBuilder.loadTexts:wosZoneTable.setStatus(_A)
_WosZoneEntry_Object=MibTableRow
wosZoneEntry=_WosZoneEntry_Object((1,3,6,1,4,1,6894,4,1,1,5,1,1))
wosZoneEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:wosZoneEntry.setStatus(_A)
_WosZoneId_Type=Unsigned32
_WosZoneId_Object=MibTableColumn
wosZoneId=_WosZoneId_Object((1,3,6,1,4,1,6894,4,1,1,5,1,1,1),_WosZoneId_Type())
wosZoneId.setMaxAccess(_D)
if mibBuilder.loadTexts:wosZoneId.setStatus(_A)
_WosZoneName_Type=DisplayString
_WosZoneName_Object=MibTableColumn
wosZoneName=_WosZoneName_Object((1,3,6,1,4,1,6894,4,1,1,5,1,1,2),_WosZoneName_Type())
wosZoneName.setMaxAccess(_C)
if mibBuilder.loadTexts:wosZoneName.setStatus(_A)
_WosZoneNodeCount_Type=Unsigned32
_WosZoneNodeCount_Object=MibTableColumn
wosZoneNodeCount=_WosZoneNodeCount_Object((1,3,6,1,4,1,6894,4,1,1,5,1,1,3),_WosZoneNodeCount_Type())
wosZoneNodeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wosZoneNodeCount.setStatus(_A)
_WosNodesInfo_ObjectIdentity=ObjectIdentity
wosNodesInfo=_WosNodesInfo_ObjectIdentity((1,3,6,1,4,1,6894,4,1,1,6))
_WosNodeTable_Object=MibTable
wosNodeTable=_WosNodeTable_Object((1,3,6,1,4,1,6894,4,1,1,6,1))
if mibBuilder.loadTexts:wosNodeTable.setStatus(_A)
_WosNodeEntry_Object=MibTableRow
wosNodeEntry=_WosNodeEntry_Object((1,3,6,1,4,1,6894,4,1,1,6,1,1))
wosNodeEntry.setIndexNames((0,_B,_H),(0,_B,_S))
if mibBuilder.loadTexts:wosNodeEntry.setStatus(_A)
_WosNodeIndex_Type=Unsigned32
_WosNodeIndex_Object=MibTableColumn
wosNodeIndex=_WosNodeIndex_Object((1,3,6,1,4,1,6894,4,1,1,6,1,1,1),_WosNodeIndex_Type())
wosNodeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wosNodeIndex.setStatus(_A)
_WosNodeName_Type=DisplayString
_WosNodeName_Object=MibTableColumn
wosNodeName=_WosNodeName_Object((1,3,6,1,4,1,6894,4,1,1,6,1,1,2),_WosNodeName_Type())
wosNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeName.setStatus(_A)
_WosNodeAddressType_Type=InetAddressType
_WosNodeAddressType_Object=MibTableColumn
wosNodeAddressType=_WosNodeAddressType_Object((1,3,6,1,4,1,6894,4,1,1,6,1,1,3),_WosNodeAddressType_Type())
wosNodeAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeAddressType.setStatus(_A)
_WosNodeAddress_Type=InetAddress
_WosNodeAddress_Object=MibTableColumn
wosNodeAddress=_WosNodeAddress_Object((1,3,6,1,4,1,6894,4,1,1,6,1,1,4),_WosNodeAddress_Type())
wosNodeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeAddress.setStatus(_A)
_WosNodeZoneName_Type=DisplayString
_WosNodeZoneName_Object=MibTableColumn
wosNodeZoneName=_WosNodeZoneName_Object((1,3,6,1,4,1,6894,4,1,1,6,1,1,5),_WosNodeZoneName_Type())
wosNodeZoneName.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeZoneName.setStatus(_A)
_WosNodeStatus_Type=DisplayString
_WosNodeStatus_Object=MibTableColumn
wosNodeStatus=_WosNodeStatus_Object((1,3,6,1,4,1,6894,4,1,1,6,1,1,6),_WosNodeStatus_Type())
wosNodeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeStatus.setStatus(_A)
_WosNodeFwVersion_Type=DisplayString
_WosNodeFwVersion_Object=MibTableColumn
wosNodeFwVersion=_WosNodeFwVersion_Object((1,3,6,1,4,1,6894,4,1,1,6,1,1,7),_WosNodeFwVersion_Type())
wosNodeFwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeFwVersion.setStatus(_A)
_WosNodeObjectCountLow_Type=Unsigned32
_WosNodeObjectCountLow_Object=MibTableColumn
wosNodeObjectCountLow=_WosNodeObjectCountLow_Object((1,3,6,1,4,1,6894,4,1,1,6,1,1,8),_WosNodeObjectCountLow_Type())
wosNodeObjectCountLow.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeObjectCountLow.setStatus(_A)
_WosNodeObjectCountHigh_Type=Unsigned32
_WosNodeObjectCountHigh_Object=MibTableColumn
wosNodeObjectCountHigh=_WosNodeObjectCountHigh_Object((1,3,6,1,4,1,6894,4,1,1,6,1,1,9),_WosNodeObjectCountHigh_Type())
wosNodeObjectCountHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeObjectCountHigh.setStatus(_A)
_WosNodeTotalCapacity_Type=Unsigned32
_WosNodeTotalCapacity_Object=MibTableColumn
wosNodeTotalCapacity=_WosNodeTotalCapacity_Object((1,3,6,1,4,1,6894,4,1,1,6,1,1,10),_WosNodeTotalCapacity_Type())
wosNodeTotalCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeTotalCapacity.setStatus(_A)
if mibBuilder.loadTexts:wosNodeTotalCapacity.setUnits(_E)
_WosNodeUsedCapacity_Type=Unsigned32
_WosNodeUsedCapacity_Object=MibTableColumn
wosNodeUsedCapacity=_WosNodeUsedCapacity_Object((1,3,6,1,4,1,6894,4,1,1,6,1,1,11),_WosNodeUsedCapacity_Type())
wosNodeUsedCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeUsedCapacity.setStatus(_A)
if mibBuilder.loadTexts:wosNodeUsedCapacity.setUnits(_E)
class _WosNodePercentFull_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_WosNodePercentFull_Type.__name__=_P
_WosNodePercentFull_Object=MibTableColumn
wosNodePercentFull=_WosNodePercentFull_Object((1,3,6,1,4,1,6894,4,1,1,6,1,1,12),_WosNodePercentFull_Type())
wosNodePercentFull.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodePercentFull.setStatus(_A)
_WosPendingNodeTable_Object=MibTable
wosPendingNodeTable=_WosPendingNodeTable_Object((1,3,6,1,4,1,6894,4,1,1,6,2))
if mibBuilder.loadTexts:wosPendingNodeTable.setStatus(_A)
_WosPendingNodeEntry_Object=MibTableRow
wosPendingNodeEntry=_WosPendingNodeEntry_Object((1,3,6,1,4,1,6894,4,1,1,6,2,1))
wosPendingNodeEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:wosPendingNodeEntry.setStatus(_A)
_WosPendingNodeIndex_Type=Unsigned32
_WosPendingNodeIndex_Object=MibTableColumn
wosPendingNodeIndex=_WosPendingNodeIndex_Object((1,3,6,1,4,1,6894,4,1,1,6,2,1,1),_WosPendingNodeIndex_Type())
wosPendingNodeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wosPendingNodeIndex.setStatus(_A)
_WosPendingNodeAddressType_Type=InetAddressType
_WosPendingNodeAddressType_Object=MibTableColumn
wosPendingNodeAddressType=_WosPendingNodeAddressType_Object((1,3,6,1,4,1,6894,4,1,1,6,2,1,2),_WosPendingNodeAddressType_Type())
wosPendingNodeAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPendingNodeAddressType.setStatus(_A)
_WosPendingNodeAddress_Type=InetAddress
_WosPendingNodeAddress_Object=MibTableColumn
wosPendingNodeAddress=_WosPendingNodeAddress_Object((1,3,6,1,4,1,6894,4,1,1,6,2,1,3),_WosPendingNodeAddress_Type())
wosPendingNodeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPendingNodeAddress.setStatus(_A)
_WosPendingNodeStatus_Type=DisplayString
_WosPendingNodeStatus_Object=MibTableColumn
wosPendingNodeStatus=_WosPendingNodeStatus_Object((1,3,6,1,4,1,6894,4,1,1,6,2,1,4),_WosPendingNodeStatus_Type())
wosPendingNodeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPendingNodeStatus.setStatus(_A)
_WosNodeDriveTable_Object=MibTable
wosNodeDriveTable=_WosNodeDriveTable_Object((1,3,6,1,4,1,6894,4,1,1,6,3))
if mibBuilder.loadTexts:wosNodeDriveTable.setStatus(_A)
_WosNodeDriveEntry_Object=MibTableRow
wosNodeDriveEntry=_WosNodeDriveEntry_Object((1,3,6,1,4,1,6894,4,1,1,6,3,1))
wosNodeDriveEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_U))
if mibBuilder.loadTexts:wosNodeDriveEntry.setStatus(_A)
_WosNodeDriveSlotNbr_Type=Unsigned32
_WosNodeDriveSlotNbr_Object=MibTableColumn
wosNodeDriveSlotNbr=_WosNodeDriveSlotNbr_Object((1,3,6,1,4,1,6894,4,1,1,6,3,1,1),_WosNodeDriveSlotNbr_Type())
wosNodeDriveSlotNbr.setMaxAccess(_D)
if mibBuilder.loadTexts:wosNodeDriveSlotNbr.setStatus(_A)
_WosNodeDriveNodeName_Type=DisplayString
_WosNodeDriveNodeName_Object=MibTableColumn
wosNodeDriveNodeName=_WosNodeDriveNodeName_Object((1,3,6,1,4,1,6894,4,1,1,6,3,1,2),_WosNodeDriveNodeName_Type())
wosNodeDriveNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeDriveNodeName.setStatus(_A)
_WosNodeDriveMfgr_Type=DisplayString
_WosNodeDriveMfgr_Object=MibTableColumn
wosNodeDriveMfgr=_WosNodeDriveMfgr_Object((1,3,6,1,4,1,6894,4,1,1,6,3,1,3),_WosNodeDriveMfgr_Type())
wosNodeDriveMfgr.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeDriveMfgr.setStatus(_A)
_WosNodeDriveModel_Type=DisplayString
_WosNodeDriveModel_Object=MibTableColumn
wosNodeDriveModel=_WosNodeDriveModel_Object((1,3,6,1,4,1,6894,4,1,1,6,3,1,4),_WosNodeDriveModel_Type())
wosNodeDriveModel.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeDriveModel.setStatus(_A)
_WosNodeDriveSerialNbr_Type=DisplayString
_WosNodeDriveSerialNbr_Object=MibTableColumn
wosNodeDriveSerialNbr=_WosNodeDriveSerialNbr_Object((1,3,6,1,4,1,6894,4,1,1,6,3,1,5),_WosNodeDriveSerialNbr_Type())
wosNodeDriveSerialNbr.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeDriveSerialNbr.setStatus(_A)
_WosNodeDriveStatus_Type=DisplayString
_WosNodeDriveStatus_Object=MibTableColumn
wosNodeDriveStatus=_WosNodeDriveStatus_Object((1,3,6,1,4,1,6894,4,1,1,6,3,1,6),_WosNodeDriveStatus_Type())
wosNodeDriveStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeDriveStatus.setStatus(_A)
_WosNodeDriveCapacity_Type=Unsigned32
_WosNodeDriveCapacity_Object=MibTableColumn
wosNodeDriveCapacity=_WosNodeDriveCapacity_Object((1,3,6,1,4,1,6894,4,1,1,6,3,1,7),_WosNodeDriveCapacity_Type())
wosNodeDriveCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:wosNodeDriveCapacity.setStatus(_A)
if mibBuilder.loadTexts:wosNodeDriveCapacity.setUnits(_E)
_WosPoliciesInfo_ObjectIdentity=ObjectIdentity
wosPoliciesInfo=_WosPoliciesInfo_ObjectIdentity((1,3,6,1,4,1,6894,4,1,1,7))
_WosPolicyTable_Object=MibTable
wosPolicyTable=_WosPolicyTable_Object((1,3,6,1,4,1,6894,4,1,1,7,1))
if mibBuilder.loadTexts:wosPolicyTable.setStatus(_A)
_WosPolicyEntry_Object=MibTableRow
wosPolicyEntry=_WosPolicyEntry_Object((1,3,6,1,4,1,6894,4,1,1,7,1,1))
wosPolicyEntry.setIndexNames((0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:wosPolicyEntry.setStatus(_A)
_WosPolicyIndex_Type=Unsigned32
_WosPolicyIndex_Object=MibTableColumn
wosPolicyIndex=_WosPolicyIndex_Object((1,3,6,1,4,1,6894,4,1,1,7,1,1,1),_WosPolicyIndex_Type())
wosPolicyIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wosPolicyIndex.setStatus(_A)
_WosPolicyReplicaIndex_Type=Unsigned32
_WosPolicyReplicaIndex_Object=MibTableColumn
wosPolicyReplicaIndex=_WosPolicyReplicaIndex_Object((1,3,6,1,4,1,6894,4,1,1,7,1,1,2),_WosPolicyReplicaIndex_Type())
wosPolicyReplicaIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wosPolicyReplicaIndex.setStatus(_A)
_WosPolicyId_Type=DisplayString
_WosPolicyId_Object=MibTableColumn
wosPolicyId=_WosPolicyId_Object((1,3,6,1,4,1,6894,4,1,1,7,1,1,3),_WosPolicyId_Type())
wosPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPolicyId.setStatus(_A)
_WosPolicyName_Type=DisplayString
_WosPolicyName_Object=MibTableColumn
wosPolicyName=_WosPolicyName_Object((1,3,6,1,4,1,6894,4,1,1,7,1,1,4),_WosPolicyName_Type())
wosPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPolicyName.setStatus(_A)
_WosPolicyReplicaZoneName_Type=DisplayString
_WosPolicyReplicaZoneName_Object=MibTableColumn
wosPolicyReplicaZoneName=_WosPolicyReplicaZoneName_Object((1,3,6,1,4,1,6894,4,1,1,7,1,1,5),_WosPolicyReplicaZoneName_Type())
wosPolicyReplicaZoneName.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPolicyReplicaZoneName.setStatus(_A)
_WosPolicyReplicaCount_Type=Unsigned32
_WosPolicyReplicaCount_Object=MibTableColumn
wosPolicyReplicaCount=_WosPolicyReplicaCount_Object((1,3,6,1,4,1,6894,4,1,1,7,1,1,6),_WosPolicyReplicaCount_Type())
wosPolicyReplicaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPolicyReplicaCount.setStatus(_A)
_WosPolicyReplicationType_Type=DisplayString
_WosPolicyReplicationType_Object=MibTableColumn
wosPolicyReplicationType=_WosPolicyReplicationType_Object((1,3,6,1,4,1,6894,4,1,1,7,1,1,7),_WosPolicyReplicationType_Type())
wosPolicyReplicationType.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPolicyReplicationType.setStatus(_A)
_WosPolicyLocalDataProtection_Type=TruthValue
_WosPolicyLocalDataProtection_Object=MibTableColumn
wosPolicyLocalDataProtection=_WosPolicyLocalDataProtection_Object((1,3,6,1,4,1,6894,4,1,1,7,1,1,8),_WosPolicyLocalDataProtection_Type())
wosPolicyLocalDataProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPolicyLocalDataProtection.setStatus(_A)
_WosPolicyObjCountLow_Type=Unsigned32
_WosPolicyObjCountLow_Object=MibTableColumn
wosPolicyObjCountLow=_WosPolicyObjCountLow_Object((1,3,6,1,4,1,6894,4,1,1,7,1,1,9),_WosPolicyObjCountLow_Type())
wosPolicyObjCountLow.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPolicyObjCountLow.setStatus(_A)
_WosPolicyObjCountHigh_Type=Unsigned32
_WosPolicyObjCountHigh_Object=MibTableColumn
wosPolicyObjCountHigh=_WosPolicyObjCountHigh_Object((1,3,6,1,4,1,6894,4,1,1,7,1,1,10),_WosPolicyObjCountHigh_Type())
wosPolicyObjCountHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPolicyObjCountHigh.setStatus(_A)
_WosPolicyNonComplObjCountLow_Type=Unsigned32
_WosPolicyNonComplObjCountLow_Object=MibTableColumn
wosPolicyNonComplObjCountLow=_WosPolicyNonComplObjCountLow_Object((1,3,6,1,4,1,6894,4,1,1,7,1,1,11),_WosPolicyNonComplObjCountLow_Type())
wosPolicyNonComplObjCountLow.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPolicyNonComplObjCountLow.setStatus(_A)
_WosPolicyNonComplObjCountHigh_Type=Unsigned32
_WosPolicyNonComplObjCountHigh_Object=MibTableColumn
wosPolicyNonComplObjCountHigh=_WosPolicyNonComplObjCountHigh_Object((1,3,6,1,4,1,6894,4,1,1,7,1,1,12),_WosPolicyNonComplObjCountHigh_Type())
wosPolicyNonComplObjCountHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPolicyNonComplObjCountHigh.setStatus(_A)
_WosPolicyUsedCapacity_Type=Unsigned32
_WosPolicyUsedCapacity_Object=MibTableColumn
wosPolicyUsedCapacity=_WosPolicyUsedCapacity_Object((1,3,6,1,4,1,6894,4,1,1,7,1,1,13),_WosPolicyUsedCapacity_Type())
wosPolicyUsedCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPolicyUsedCapacity.setStatus(_A)
if mibBuilder.loadTexts:wosPolicyUsedCapacity.setUnits(_E)
_WosPrefsInfo_ObjectIdentity=ObjectIdentity
wosPrefsInfo=_WosPrefsInfo_ObjectIdentity((1,3,6,1,4,1,6894,4,1,1,8))
_WosPrefStoreUnderReplObjs_Type=TruthValue
_WosPrefStoreUnderReplObjs_Object=MibScalar
wosPrefStoreUnderReplObjs=_WosPrefStoreUnderReplObjs_Object((1,3,6,1,4,1,6894,4,1,1,8,1),_WosPrefStoreUnderReplObjs_Type())
wosPrefStoreUnderReplObjs.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPrefStoreUnderReplObjs.setStatus(_A)
_WosPrefNodeDownDelay_Type=Unsigned32
_WosPrefNodeDownDelay_Object=MibScalar
wosPrefNodeDownDelay=_WosPrefNodeDownDelay_Object((1,3,6,1,4,1,6894,4,1,1,8,2),_WosPrefNodeDownDelay_Type())
wosPrefNodeDownDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPrefNodeDownDelay.setStatus(_A)
if mibBuilder.loadTexts:wosPrefNodeDownDelay.setUnits(_K)
_WosPrefEmailAlertNewInterval_Type=Unsigned32
_WosPrefEmailAlertNewInterval_Object=MibScalar
wosPrefEmailAlertNewInterval=_WosPrefEmailAlertNewInterval_Object((1,3,6,1,4,1,6894,4,1,1,8,3),_WosPrefEmailAlertNewInterval_Type())
wosPrefEmailAlertNewInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPrefEmailAlertNewInterval.setStatus(_A)
if mibBuilder.loadTexts:wosPrefEmailAlertNewInterval.setUnits(_K)
_WosPrefEmailAlertRmndrInterval_Type=Unsigned32
_WosPrefEmailAlertRmndrInterval_Object=MibScalar
wosPrefEmailAlertRmndrInterval=_WosPrefEmailAlertRmndrInterval_Object((1,3,6,1,4,1,6894,4,1,1,8,4),_WosPrefEmailAlertRmndrInterval_Type())
wosPrefEmailAlertRmndrInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPrefEmailAlertRmndrInterval.setStatus(_A)
if mibBuilder.loadTexts:wosPrefEmailAlertRmndrInterval.setUnits(_K)
_WosPrefEmailAlertFromAddr_Type=DisplayString
_WosPrefEmailAlertFromAddr_Object=MibScalar
wosPrefEmailAlertFromAddr=_WosPrefEmailAlertFromAddr_Object((1,3,6,1,4,1,6894,4,1,1,8,5),_WosPrefEmailAlertFromAddr_Type())
wosPrefEmailAlertFromAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPrefEmailAlertFromAddr.setStatus(_A)
_WosPrefEmailAlertRecipientTable_Object=MibTable
wosPrefEmailAlertRecipientTable=_WosPrefEmailAlertRecipientTable_Object((1,3,6,1,4,1,6894,4,1,1,8,6))
if mibBuilder.loadTexts:wosPrefEmailAlertRecipientTable.setStatus(_A)
_WosPrefEmailAlertRecipientEntry_Object=MibTableRow
wosPrefEmailAlertRecipientEntry=_WosPrefEmailAlertRecipientEntry_Object((1,3,6,1,4,1,6894,4,1,1,8,6,1))
wosPrefEmailAlertRecipientEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:wosPrefEmailAlertRecipientEntry.setStatus(_A)
_WosPrefEmailAlertRecipientIndex_Type=Unsigned32
_WosPrefEmailAlertRecipientIndex_Object=MibTableColumn
wosPrefEmailAlertRecipientIndex=_WosPrefEmailAlertRecipientIndex_Object((1,3,6,1,4,1,6894,4,1,1,8,6,1,1),_WosPrefEmailAlertRecipientIndex_Type())
wosPrefEmailAlertRecipientIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wosPrefEmailAlertRecipientIndex.setStatus(_A)
_WosPrefEmailAlertRecipient_Type=DisplayString
_WosPrefEmailAlertRecipient_Object=MibTableColumn
wosPrefEmailAlertRecipient=_WosPrefEmailAlertRecipient_Object((1,3,6,1,4,1,6894,4,1,1,8,6,1,2),_WosPrefEmailAlertRecipient_Type())
wosPrefEmailAlertRecipient.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPrefEmailAlertRecipient.setStatus(_A)
_WosPrefEmailAlertServerTable_Object=MibTable
wosPrefEmailAlertServerTable=_WosPrefEmailAlertServerTable_Object((1,3,6,1,4,1,6894,4,1,1,8,7))
if mibBuilder.loadTexts:wosPrefEmailAlertServerTable.setStatus(_A)
_WosPrefEmailAlertServerEntry_Object=MibTableRow
wosPrefEmailAlertServerEntry=_WosPrefEmailAlertServerEntry_Object((1,3,6,1,4,1,6894,4,1,1,8,7,1))
wosPrefEmailAlertServerEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:wosPrefEmailAlertServerEntry.setStatus(_A)
_WosPrefEmailAlertServerIndex_Type=Unsigned32
_WosPrefEmailAlertServerIndex_Object=MibTableColumn
wosPrefEmailAlertServerIndex=_WosPrefEmailAlertServerIndex_Object((1,3,6,1,4,1,6894,4,1,1,8,7,1,1),_WosPrefEmailAlertServerIndex_Type())
wosPrefEmailAlertServerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wosPrefEmailAlertServerIndex.setStatus(_A)
_WosPrefEmailAlertServer_Type=DisplayString
_WosPrefEmailAlertServer_Object=MibTableColumn
wosPrefEmailAlertServer=_WosPrefEmailAlertServer_Object((1,3,6,1,4,1,6894,4,1,1,8,7,1,2),_WosPrefEmailAlertServer_Type())
wosPrefEmailAlertServer.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPrefEmailAlertServer.setStatus(_A)
_WosPrefSnmpManagerTable_Object=MibTable
wosPrefSnmpManagerTable=_WosPrefSnmpManagerTable_Object((1,3,6,1,4,1,6894,4,1,1,8,8))
if mibBuilder.loadTexts:wosPrefSnmpManagerTable.setStatus(_A)
_WosPrefSnmpManagerEntry_Object=MibTableRow
wosPrefSnmpManagerEntry=_WosPrefSnmpManagerEntry_Object((1,3,6,1,4,1,6894,4,1,1,8,8,1))
wosPrefSnmpManagerEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:wosPrefSnmpManagerEntry.setStatus(_A)
_WosPrefSnmpManagerIndex_Type=Unsigned32
_WosPrefSnmpManagerIndex_Object=MibTableColumn
wosPrefSnmpManagerIndex=_WosPrefSnmpManagerIndex_Object((1,3,6,1,4,1,6894,4,1,1,8,8,1,1),_WosPrefSnmpManagerIndex_Type())
wosPrefSnmpManagerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wosPrefSnmpManagerIndex.setStatus(_A)
_WosPrefSnmpManager_Type=DisplayString
_WosPrefSnmpManager_Object=MibTableColumn
wosPrefSnmpManager=_WosPrefSnmpManager_Object((1,3,6,1,4,1,6894,4,1,1,8,8,1,2),_WosPrefSnmpManager_Type())
wosPrefSnmpManager.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPrefSnmpManager.setStatus(_A)
_WosPrefSnmpTrapCommunityName_Type=DisplayString
_WosPrefSnmpTrapCommunityName_Object=MibScalar
wosPrefSnmpTrapCommunityName=_WosPrefSnmpTrapCommunityName_Object((1,3,6,1,4,1,6894,4,1,1,8,9),_WosPrefSnmpTrapCommunityName_Type())
wosPrefSnmpTrapCommunityName.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPrefSnmpTrapCommunityName.setStatus(_A)
_WosPrefMgmtIpFilterTable_Object=MibTable
wosPrefMgmtIpFilterTable=_WosPrefMgmtIpFilterTable_Object((1,3,6,1,4,1,6894,4,1,1,8,10))
if mibBuilder.loadTexts:wosPrefMgmtIpFilterTable.setStatus(_A)
_WosPrefMgmtIpFilterEntry_Object=MibTableRow
wosPrefMgmtIpFilterEntry=_WosPrefMgmtIpFilterEntry_Object((1,3,6,1,4,1,6894,4,1,1,8,10,1))
wosPrefMgmtIpFilterEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:wosPrefMgmtIpFilterEntry.setStatus(_A)
_WosPrefMgmtIpFilterIndex_Type=Unsigned32
_WosPrefMgmtIpFilterIndex_Object=MibTableColumn
wosPrefMgmtIpFilterIndex=_WosPrefMgmtIpFilterIndex_Object((1,3,6,1,4,1,6894,4,1,1,8,10,1,1),_WosPrefMgmtIpFilterIndex_Type())
wosPrefMgmtIpFilterIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wosPrefMgmtIpFilterIndex.setStatus(_A)
_WosPrefMgmtIpFilter_Type=DisplayString
_WosPrefMgmtIpFilter_Object=MibTableColumn
wosPrefMgmtIpFilter=_WosPrefMgmtIpFilter_Object((1,3,6,1,4,1,6894,4,1,1,8,10,1,2),_WosPrefMgmtIpFilter_Type())
wosPrefMgmtIpFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPrefMgmtIpFilter.setStatus(_A)
_WosPrefClientIpFilterTable_Object=MibTable
wosPrefClientIpFilterTable=_WosPrefClientIpFilterTable_Object((1,3,6,1,4,1,6894,4,1,1,8,11))
if mibBuilder.loadTexts:wosPrefClientIpFilterTable.setStatus(_A)
_WosPrefClientIpFilterEntry_Object=MibTableRow
wosPrefClientIpFilterEntry=_WosPrefClientIpFilterEntry_Object((1,3,6,1,4,1,6894,4,1,1,8,11,1))
wosPrefClientIpFilterEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:wosPrefClientIpFilterEntry.setStatus(_A)
_WosPrefClientIpFilterIndex_Type=Unsigned32
_WosPrefClientIpFilterIndex_Object=MibTableColumn
wosPrefClientIpFilterIndex=_WosPrefClientIpFilterIndex_Object((1,3,6,1,4,1,6894,4,1,1,8,11,1,1),_WosPrefClientIpFilterIndex_Type())
wosPrefClientIpFilterIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wosPrefClientIpFilterIndex.setStatus(_A)
_WosPrefClientIpFilter_Type=DisplayString
_WosPrefClientIpFilter_Object=MibTableColumn
wosPrefClientIpFilter=_WosPrefClientIpFilter_Object((1,3,6,1,4,1,6894,4,1,1,8,11,1,2),_WosPrefClientIpFilter_Type())
wosPrefClientIpFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPrefClientIpFilter.setStatus(_A)
_WosPrefSyslogFacility_Type=WosSyslogFacility
_WosPrefSyslogFacility_Object=MibScalar
wosPrefSyslogFacility=_WosPrefSyslogFacility_Object((1,3,6,1,4,1,6894,4,1,1,8,12),_WosPrefSyslogFacility_Type())
wosPrefSyslogFacility.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPrefSyslogFacility.setStatus(_A)
_WosPrefSyslogRemoteHost_Type=DisplayString
_WosPrefSyslogRemoteHost_Object=MibScalar
wosPrefSyslogRemoteHost=_WosPrefSyslogRemoteHost_Object((1,3,6,1,4,1,6894,4,1,1,8,13),_WosPrefSyslogRemoteHost_Type())
wosPrefSyslogRemoteHost.setMaxAccess(_C)
if mibBuilder.loadTexts:wosPrefSyslogRemoteHost.setStatus(_A)
_WosConformance_ObjectIdentity=ObjectIdentity
wosConformance=_WosConformance_ObjectIdentity((1,3,6,1,4,1,6894,4,1,2))
_WosCompliances_ObjectIdentity=ObjectIdentity
wosCompliances=_WosCompliances_ObjectIdentity((1,3,6,1,4,1,6894,4,1,2,1))
_WosGroups_ObjectIdentity=ObjectIdentity
wosGroups=_WosGroups_ObjectIdentity((1,3,6,1,4,1,6894,4,1,2,2))
wosNotificationsGroup=ObjectGroup((1,3,6,1,4,1,6894,4,1,2,2,2))
wosNotificationsGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:wosNotificationsGroup.setStatus(_A)
wosStatsGroup=ObjectGroup((1,3,6,1,4,1,6894,4,1,2,2,3))
wosStatsGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:wosStatsGroup.setStatus(_A)
wosAlertsGroup=ObjectGroup((1,3,6,1,4,1,6894,4,1,2,2,4))
wosAlertsGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:wosAlertsGroup.setStatus(_A)
wosClusterGroup=ObjectGroup((1,3,6,1,4,1,6894,4,1,2,2,5))
wosClusterGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:wosClusterGroup.setStatus(_A)
wosZonesGroup=ObjectGroup((1,3,6,1,4,1,6894,4,1,2,2,6))
wosZonesGroup.setObjects(*((_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:wosZonesGroup.setStatus(_A)
wosNodesGroup=ObjectGroup((1,3,6,1,4,1,6894,4,1,2,2,7))
wosNodesGroup.setObjects(*((_B,_A8),(_B,_I),(_B,_J),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:wosNodesGroup.setStatus(_A)
wosPoliciesGroup=ObjectGroup((1,3,6,1,4,1,6894,4,1,2,2,8))
wosPoliciesGroup.setObjects(*((_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:wosPoliciesGroup.setStatus(_A)
wosPrefsGroup=ObjectGroup((1,3,6,1,4,1,6894,4,1,2,2,9))
wosPrefsGroup.setObjects(*((_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An)))
if mibBuilder.loadTexts:wosPrefsGroup.setStatus(_A)
wosTrapMessage=NotificationType((1,3,6,1,4,1,6894,4,1,0,1))
wosTrapMessage.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_L)))
if mibBuilder.loadTexts:wosTrapMessage.setStatus(_A)
wosEventsGroup=NotificationGroup((1,3,6,1,4,1,6894,4,1,2,2,1))
wosEventsGroup.setObjects((_B,_Ao))
if mibBuilder.loadTexts:wosEventsGroup.setStatus(_A)
wosCompliance=ModuleCompliance((1,3,6,1,4,1,6894,4,1,2,1,1))
wosCompliance.setObjects(*((_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax)))
if mibBuilder.loadTexts:wosCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'WosSeverityLevel':WosSeverityLevel,'WosSyslogFacility':WosSyslogFacility,'datadirect':datadirect,'wos':wos,'wosMIB':wosMIB,'wosNotifications':wosNotifications,_Ao:wosTrapMessage,'wosObjects':wosObjects,'wosNotificationInfo':wosNotificationInfo,_L:wosTrapDesc,_M:wosTrapSeverity,_N:wosTrapType,_O:wosTrapLocation,'wosStatsInfo':wosStatsInfo,_c:wosStatsFRPS,_d:wosStatsFWPS,_e:wosStatsFDPS,_f:wosStatsReadLatency,_g:wosStatsWriteLatency,_h:wosStatsDeleteLatency,_i:wosStatsReadThroughput,_j:wosStatsWriteThroughput,_k:wosStatsReadCount,_l:wosStatsWriteCount,_m:wosStatsDeleteCount,'wosAlertsInfo':wosAlertsInfo,'wosAlertTable':wosAlertTable,'wosAlertEntry':wosAlertEntry,_R:wosAlertIndex,_n:wosAlertSeverity,_o:wosAlertTime,_p:wosAlertType,_q:wosAlertLocation,_r:wosAlertDesc,'wosClusterInfo':wosClusterInfo,_s:wosClusterName,_t:wosClusterId,_u:wosClusterStatus,_v:wosClusterPrimaryNodeAddressType,_w:wosClusterPrimaryNodeAddress,_x:wosClusterTotalNodeCount,_y:wosClusterActiveNodeCount,_z:wosClusterDisconnectedNodeCount,_A0:wosClusterConnectedClientsCount,_A1:wosClusterObjectCountLow,_A2:wosClusterObjectCountHigh,_A3:wosClusterUsableCapacity,_A4:wosClusterUsedCapacity,_A5:wosClusterFreeCapacity,'wosZonesInfo':wosZonesInfo,'wosZoneTable':wosZoneTable,'wosZoneEntry':wosZoneEntry,_H:wosZoneId,_A6:wosZoneName,_A7:wosZoneNodeCount,'wosNodesInfo':wosNodesInfo,'wosNodeTable':wosNodeTable,'wosNodeEntry':wosNodeEntry,_S:wosNodeIndex,_A8:wosNodeName,_I:wosNodeAddressType,_J:wosNodeAddress,_A9:wosNodeZoneName,_AA:wosNodeStatus,_AB:wosNodeFwVersion,_AC:wosNodeObjectCountLow,_AD:wosNodeObjectCountHigh,_AE:wosNodeTotalCapacity,_AF:wosNodeUsedCapacity,_AG:wosNodePercentFull,'wosPendingNodeTable':wosPendingNodeTable,'wosPendingNodeEntry':wosPendingNodeEntry,_T:wosPendingNodeIndex,_AH:wosPendingNodeAddressType,_AI:wosPendingNodeAddress,_AJ:wosPendingNodeStatus,'wosNodeDriveTable':wosNodeDriveTable,'wosNodeDriveEntry':wosNodeDriveEntry,_U:wosNodeDriveSlotNbr,_AK:wosNodeDriveNodeName,_AL:wosNodeDriveMfgr,_AM:wosNodeDriveModel,_AN:wosNodeDriveSerialNbr,_AO:wosNodeDriveStatus,_AP:wosNodeDriveCapacity,'wosPoliciesInfo':wosPoliciesInfo,'wosPolicyTable':wosPolicyTable,'wosPolicyEntry':wosPolicyEntry,_V:wosPolicyIndex,_W:wosPolicyReplicaIndex,_AQ:wosPolicyId,_AR:wosPolicyName,_AS:wosPolicyReplicaZoneName,_AT:wosPolicyReplicaCount,_AU:wosPolicyReplicationType,_AV:wosPolicyLocalDataProtection,_AW:wosPolicyObjCountLow,_AX:wosPolicyObjCountHigh,_AY:wosPolicyNonComplObjCountLow,_AZ:wosPolicyNonComplObjCountHigh,_Aa:wosPolicyUsedCapacity,'wosPrefsInfo':wosPrefsInfo,_Ab:wosPrefStoreUnderReplObjs,_Ac:wosPrefNodeDownDelay,_Ad:wosPrefEmailAlertNewInterval,_Ae:wosPrefEmailAlertRmndrInterval,_Af:wosPrefEmailAlertFromAddr,'wosPrefEmailAlertRecipientTable':wosPrefEmailAlertRecipientTable,'wosPrefEmailAlertRecipientEntry':wosPrefEmailAlertRecipientEntry,_X:wosPrefEmailAlertRecipientIndex,_Ag:wosPrefEmailAlertRecipient,'wosPrefEmailAlertServerTable':wosPrefEmailAlertServerTable,'wosPrefEmailAlertServerEntry':wosPrefEmailAlertServerEntry,_Y:wosPrefEmailAlertServerIndex,_Ah:wosPrefEmailAlertServer,'wosPrefSnmpManagerTable':wosPrefSnmpManagerTable,'wosPrefSnmpManagerEntry':wosPrefSnmpManagerEntry,_Z:wosPrefSnmpManagerIndex,_Ai:wosPrefSnmpManager,_Aj:wosPrefSnmpTrapCommunityName,'wosPrefMgmtIpFilterTable':wosPrefMgmtIpFilterTable,'wosPrefMgmtIpFilterEntry':wosPrefMgmtIpFilterEntry,_a:wosPrefMgmtIpFilterIndex,_Ak:wosPrefMgmtIpFilter,'wosPrefClientIpFilterTable':wosPrefClientIpFilterTable,'wosPrefClientIpFilterEntry':wosPrefClientIpFilterEntry,_b:wosPrefClientIpFilterIndex,_Al:wosPrefClientIpFilter,_Am:wosPrefSyslogFacility,_An:wosPrefSyslogRemoteHost,'wosConformance':wosConformance,'wosCompliances':wosCompliances,'wosCompliance':wosCompliance,'wosGroups':wosGroups,_Ap:wosEventsGroup,_Aq:wosNotificationsGroup,_Ar:wosStatsGroup,_As:wosAlertsGroup,_At:wosClusterGroup,_Au:wosZonesGroup,_Av:wosNodesGroup,_Aw:wosPoliciesGroup,_Ax:wosPrefsGroup})