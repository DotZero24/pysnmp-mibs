_BY='cfmNotifyGroup'
_BX='cfmNotifySupportGroup'
_BW='cfmAlarmHistoryGroup'
_BV='cfmAlarmAggregationGroup'
_BU='cfmFlowConditionsGroup'
_BT='cfmFlowMetricsGroup'
_BS='cfmFlowGroup'
_BR='cfmFlowMonitorGroup'
_BQ='cfmNotifyAlarm'
_BP='cfmNotifyEnable'
_BO='cfmAlarmHistoryLastId'
_BN='cfmAlarmHistorySize'
_BM='cfmAlarmGroupFlowTableChanged'
_BL='cfmAlarmGroupTableChanged'
_BK='cfmAlarmGroupCurrentCount'
_BJ='cfmAlarmGroupRaised'
_BI='cfmAlarmGroupThreshold'
_BH='cfmAlarmGroupThresholdUnits'
_BG='cfmAlarmGroupFlowCount'
_BF='cfmAlarmGroupFlowSet'
_BE='cfmAlarmGroupConditionId'
_BD='cfmAlarmGroupConditionsProfile'
_BC='cfmAlarmGroupDescr'
_BB='cfmConditionTableChanged'
_BA='cfmConditionAlarmGroup'
_B9='cfmConditionAlarmSeverity'
_B8='cfmConditionAlarmActions'
_B7='cfmConditionAlarm'
_B6='cfmConditionSampleWindow'
_B5='cfmConditionSampleType'
_B4='cfmConditionThreshFall'
_B3='cfmConditionThreshFallPrecision'
_B2='cfmConditionThreshFallScale'
_B1='cfmConditionThreshRise'
_B0='cfmConditionThreshRisePrecision'
_A_='cfmConditionThreshRiseScale'
_Az='cfmConditionType'
_Ay='cfmConditionMonitoredElement'
_Ax='cfmConditionDescr'
_Aw='cfmFlowMetricsIntPktRate'
_Av='cfmFlowMetricsIntBitRate'
_Au='cfmFlowMetricsIntBitRateUnits'
_At='cfmFlowMetricsIntOctets'
_As='cfmFlowMetricsIntPkts'
_Ar='cfmFlowMetricsIntAlarmSeverity'
_Aq='cfmFlowMetricsIntAlarms'
_Ap='cfmFlowMetricsIntConditions'
_Ao='cfmFlowMetricsIntTime'
_An='cfmFlowMetricsIntValid'
_Am='cfmFlowMetricsTableChanged'
_Al='cfmFlowMetricsPktRate'
_Ak='cfmFlowMetricsBitRate'
_Aj='cfmFlowMetricsBitRateUnits'
_Ai='cfmFlowMetricsOctets'
_Ah='cfmFlowMetricsPkts'
_Ag='cfmFlowMetricsAlarmSeverity'
_Af='cfmFlowMetricsAlarms'
_Ae='cfmFlowMetricsConditions'
_Ad='cfmFlowMetricsConditionsProfile'
_Ac='cfmFlowMetricsInvalidIntervals'
_Ab='cfmFlowMetricsIntervals'
_Aa='cfmFlowMetricsElapsedTime'
_AZ='cfmFlowMetricsMaxIntervals'
_AY='cfmFlowMetricsIntervalTime'
_AX='cfmFlowMetricsCollected'
_AW='cfmFlowRtpTableChanged'
_AV='cfmFlowRtpPayloadType'
_AU='cfmFlowRtpSsrc'
_AT='cfmFlowRtpVersion'
_AS='cfmFlowRtpNext'
_AR='cfmFlowTcpTableChanged'
_AQ='cfmFlowTcpPortDst'
_AP='cfmFlowTcpPortSrc'
_AO='cfmFlowTcpNext'
_AN='cfmFlowUdpTableChanged'
_AM='cfmFlowUdpPortDst'
_AL='cfmFlowUdpPortSrc'
_AK='cfmFlowUdpNext'
_AJ='cfmFlowIpTableChanged'
_AI='cfmFlowIpHopLimit'
_AH='cfmFlowIpTrafficClass'
_AG='cfmFlowIpValid'
_AF='cfmFlowIpAddrDst'
_AE='cfmFlowIpAddrSrc'
_AD='cfmFlowIpAddrType'
_AC='cfmFlowIpNext'
_AB='cfmFlowL2VlanTableChanged'
_AA='cfmFlowL2VlanCos'
_A9='cfmFlowL2VlanId'
_A8='cfmFlowL2VlanNext'
_A7='cfmFlowTableChanged'
_A6='cfmFlowEgress'
_A5='cfmFlowEgressType'
_A4='cfmFlowIngress'
_A3='cfmFlowIngressType'
_A2='cfmFlowOperStatus'
_A1='cfmFlowAdminStatus'
_A0='cfmFlowDirection'
_z='cfmFlowExpirationTime'
_y='cfmFlowDiscontinuityTime'
_x='cfmFlowCreateTime'
_w='cfmFlowNext'
_v='cfmFlowDescr'
_u='cfmFlowMonitorTableChanged'
_t='cfmFlowMonitorAlarmInfoCount'
_s='cfmFlowMonitorAlarmWarningCount'
_r='cfmFlowMonitorAlarmMinorCount'
_q='cfmFlowMonitorAlarmMajorCount'
_p='cfmFlowMonitorAlarmCriticalCount'
_o='cfmFlowMonitorAlarmSeverity'
_n='cfmFlowMonitorAlarms'
_m='cfmFlowMonitorConditions'
_l='cfmFlowMonitorConditionsProfile'
_k='cfmFlowMonitorFlowCount'
_j='cfmFlowMonitorCaps'
_i='cfmFlowMonitorDescr'
_h='cfmAlarmHistoryId'
_g='cfmAlarmGroupFlowMonitorId'
_f='cfmAlarmGroupFlowSetId'
_e='cfmAlarmGroupId'
_d='cfmConditionId'
_c='cfmConditionProfile'
_b='cfmFlowMetricsIntNumber'
_a='packets per second'
_Z='octets'
_Y='packets'
_X='disabled'
_W='enabled'
_V='cfmAlarmHistoryTime'
_U='cfmAlarmHistorySeverity'
_T='cfmAlarmHistoryConditionId'
_S='cfmAlarmHistoryConditionsProfile'
_R='cfmAlarmHistoryEntity'
_Q='cfmAlarmHistoryType'
_P='cfmAlarmGroupFlowId'
_O='other'
_N='intervals'
_M='read-write'
_L='seconds'
_K='traffic flows'
_J='Bits'
_I='alarms'
_H='cfmFlowId'
_G='not-accessible'
_F='Integer32'
_E='cfmFlowMonitorId'
_D='Unsigned32'
_C='read-only'
_B='CISCO-FLOW-MONITOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
FlowBitRateUnits,FlowIdentifier,FlowMetricPrecision,FlowMetricScale,FlowMetricValue,FlowMetrics,FlowMonitorAlarmGroupIdentifier,FlowMonitorConditionIdentifier,FlowMonitorConditions,FlowMonitorConditionsProfile,FlowMonitorConditionsProfileOrZero,FlowMonitorIdentifier,FlowPointIdentifier,FlowPointType,FlowSetIdentifier=mibBuilder.importSymbols('CISCO-FLOW-MONITOR-TC-MIB','FlowBitRateUnits','FlowIdentifier','FlowMetricPrecision','FlowMetricScale','FlowMetricValue','FlowMetrics','FlowMonitorAlarmGroupIdentifier','FlowMonitorConditionIdentifier','FlowMonitorConditions','FlowMonitorConditionsProfile','FlowMonitorConditionsProfileOrZero','FlowMonitorIdentifier','FlowPointIdentifier','FlowPointType','FlowSetIdentifier')
ReportIntervalCount,=mibBuilder.importSymbols('CISCO-REPORT-INTERVAL-TC-MIB','ReportIntervalCount')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,Layer2Cos=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','Layer2Cos')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
AutonomousType,DisplayString,PhysAddress,RowPointer,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','RowPointer','TextualConvention','TimeStamp','TruthValue')
ciscoFlowMonitorMIB=ModuleIdentity((1,3,6,1,4,1,9,9,692))
if mibBuilder.loadTexts:ciscoFlowMonitorMIB.setRevisions(('2009-04-08 00:00',))
_CiscoFlowMonitorMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoFlowMonitorMIBNotifs=_CiscoFlowMonitorMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,692,0))
_CiscoFlowMonitorMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFlowMonitorMIBObjects=_CiscoFlowMonitorMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,692,1))
_CfmFlowMonitors_ObjectIdentity=ObjectIdentity
cfmFlowMonitors=_CfmFlowMonitors_ObjectIdentity((1,3,6,1,4,1,9,9,692,1,1))
_CfmFlowMonitorTable_Object=MibTable
cfmFlowMonitorTable=_CfmFlowMonitorTable_Object((1,3,6,1,4,1,9,9,692,1,1,1))
if mibBuilder.loadTexts:cfmFlowMonitorTable.setStatus(_A)
_CfmFlowMonitorEntry_Object=MibTableRow
cfmFlowMonitorEntry=_CfmFlowMonitorEntry_Object((1,3,6,1,4,1,9,9,692,1,1,1,1))
cfmFlowMonitorEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cfmFlowMonitorEntry.setStatus(_A)
_CfmFlowMonitorId_Type=FlowMonitorIdentifier
_CfmFlowMonitorId_Object=MibTableColumn
cfmFlowMonitorId=_CfmFlowMonitorId_Object((1,3,6,1,4,1,9,9,692,1,1,1,1,1),_CfmFlowMonitorId_Type())
cfmFlowMonitorId.setMaxAccess(_G)
if mibBuilder.loadTexts:cfmFlowMonitorId.setStatus(_A)
_CfmFlowMonitorDescr_Type=SnmpAdminString
_CfmFlowMonitorDescr_Object=MibTableColumn
cfmFlowMonitorDescr=_CfmFlowMonitorDescr_Object((1,3,6,1,4,1,9,9,692,1,1,1,1,2),_CfmFlowMonitorDescr_Type())
cfmFlowMonitorDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMonitorDescr.setStatus(_A)
_CfmFlowMonitorCaps_Type=FlowMetrics
_CfmFlowMonitorCaps_Object=MibTableColumn
cfmFlowMonitorCaps=_CfmFlowMonitorCaps_Object((1,3,6,1,4,1,9,9,692,1,1,1,1,3),_CfmFlowMonitorCaps_Type())
cfmFlowMonitorCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMonitorCaps.setStatus(_A)
_CfmFlowMonitorFlowCount_Type=Gauge32
_CfmFlowMonitorFlowCount_Object=MibTableColumn
cfmFlowMonitorFlowCount=_CfmFlowMonitorFlowCount_Object((1,3,6,1,4,1,9,9,692,1,1,1,1,4),_CfmFlowMonitorFlowCount_Type())
cfmFlowMonitorFlowCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMonitorFlowCount.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMonitorFlowCount.setUnits(_K)
_CfmFlowMonitorConditionsProfile_Type=FlowMonitorConditionsProfileOrZero
_CfmFlowMonitorConditionsProfile_Object=MibTableColumn
cfmFlowMonitorConditionsProfile=_CfmFlowMonitorConditionsProfile_Object((1,3,6,1,4,1,9,9,692,1,1,1,1,5),_CfmFlowMonitorConditionsProfile_Type())
cfmFlowMonitorConditionsProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMonitorConditionsProfile.setStatus(_A)
_CfmFlowMonitorConditions_Type=FlowMonitorConditions
_CfmFlowMonitorConditions_Object=MibTableColumn
cfmFlowMonitorConditions=_CfmFlowMonitorConditions_Object((1,3,6,1,4,1,9,9,692,1,1,1,1,6),_CfmFlowMonitorConditions_Type())
cfmFlowMonitorConditions.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMonitorConditions.setStatus(_A)
_CfmFlowMonitorAlarms_Type=FlowMonitorConditions
_CfmFlowMonitorAlarms_Object=MibTableColumn
cfmFlowMonitorAlarms=_CfmFlowMonitorAlarms_Object((1,3,6,1,4,1,9,9,692,1,1,1,1,7),_CfmFlowMonitorAlarms_Type())
cfmFlowMonitorAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMonitorAlarms.setStatus(_A)
_CfmFlowMonitorAlarmSeverity_Type=CiscoAlarmSeverity
_CfmFlowMonitorAlarmSeverity_Object=MibTableColumn
cfmFlowMonitorAlarmSeverity=_CfmFlowMonitorAlarmSeverity_Object((1,3,6,1,4,1,9,9,692,1,1,1,1,8),_CfmFlowMonitorAlarmSeverity_Type())
cfmFlowMonitorAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMonitorAlarmSeverity.setStatus(_A)
_CfmFlowMonitorAlarmCriticalCount_Type=Gauge32
_CfmFlowMonitorAlarmCriticalCount_Object=MibTableColumn
cfmFlowMonitorAlarmCriticalCount=_CfmFlowMonitorAlarmCriticalCount_Object((1,3,6,1,4,1,9,9,692,1,1,1,1,9),_CfmFlowMonitorAlarmCriticalCount_Type())
cfmFlowMonitorAlarmCriticalCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMonitorAlarmCriticalCount.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMonitorAlarmCriticalCount.setUnits(_I)
_CfmFlowMonitorAlarmMajorCount_Type=Gauge32
_CfmFlowMonitorAlarmMajorCount_Object=MibTableColumn
cfmFlowMonitorAlarmMajorCount=_CfmFlowMonitorAlarmMajorCount_Object((1,3,6,1,4,1,9,9,692,1,1,1,1,10),_CfmFlowMonitorAlarmMajorCount_Type())
cfmFlowMonitorAlarmMajorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMonitorAlarmMajorCount.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMonitorAlarmMajorCount.setUnits(_I)
_CfmFlowMonitorAlarmMinorCount_Type=Gauge32
_CfmFlowMonitorAlarmMinorCount_Object=MibTableColumn
cfmFlowMonitorAlarmMinorCount=_CfmFlowMonitorAlarmMinorCount_Object((1,3,6,1,4,1,9,9,692,1,1,1,1,11),_CfmFlowMonitorAlarmMinorCount_Type())
cfmFlowMonitorAlarmMinorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMonitorAlarmMinorCount.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMonitorAlarmMinorCount.setUnits(_I)
_CfmFlowMonitorAlarmWarningCount_Type=Gauge32
_CfmFlowMonitorAlarmWarningCount_Object=MibTableColumn
cfmFlowMonitorAlarmWarningCount=_CfmFlowMonitorAlarmWarningCount_Object((1,3,6,1,4,1,9,9,692,1,1,1,1,12),_CfmFlowMonitorAlarmWarningCount_Type())
cfmFlowMonitorAlarmWarningCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMonitorAlarmWarningCount.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMonitorAlarmWarningCount.setUnits(_I)
_CfmFlowMonitorAlarmInfoCount_Type=Gauge32
_CfmFlowMonitorAlarmInfoCount_Object=MibTableColumn
cfmFlowMonitorAlarmInfoCount=_CfmFlowMonitorAlarmInfoCount_Object((1,3,6,1,4,1,9,9,692,1,1,1,1,13),_CfmFlowMonitorAlarmInfoCount_Type())
cfmFlowMonitorAlarmInfoCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMonitorAlarmInfoCount.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMonitorAlarmInfoCount.setUnits(_I)
_CfmFlowMonitorTableChanged_Type=TimeStamp
_CfmFlowMonitorTableChanged_Object=MibScalar
cfmFlowMonitorTableChanged=_CfmFlowMonitorTableChanged_Object((1,3,6,1,4,1,9,9,692,1,1,2),_CfmFlowMonitorTableChanged_Type())
cfmFlowMonitorTableChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMonitorTableChanged.setStatus(_A)
_CfmFlows_ObjectIdentity=ObjectIdentity
cfmFlows=_CfmFlows_ObjectIdentity((1,3,6,1,4,1,9,9,692,1,2))
_CfmFlowTable_Object=MibTable
cfmFlowTable=_CfmFlowTable_Object((1,3,6,1,4,1,9,9,692,1,2,1))
if mibBuilder.loadTexts:cfmFlowTable.setStatus(_A)
_CfmFlowEntry_Object=MibTableRow
cfmFlowEntry=_CfmFlowEntry_Object((1,3,6,1,4,1,9,9,692,1,2,1,1))
cfmFlowEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:cfmFlowEntry.setStatus(_A)
_CfmFlowId_Type=FlowIdentifier
_CfmFlowId_Object=MibTableColumn
cfmFlowId=_CfmFlowId_Object((1,3,6,1,4,1,9,9,692,1,2,1,1,1),_CfmFlowId_Type())
cfmFlowId.setMaxAccess(_G)
if mibBuilder.loadTexts:cfmFlowId.setStatus(_A)
_CfmFlowDescr_Type=SnmpAdminString
_CfmFlowDescr_Object=MibTableColumn
cfmFlowDescr=_CfmFlowDescr_Object((1,3,6,1,4,1,9,9,692,1,2,1,1,2),_CfmFlowDescr_Type())
cfmFlowDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowDescr.setStatus(_A)
_CfmFlowNext_Type=RowPointer
_CfmFlowNext_Object=MibTableColumn
cfmFlowNext=_CfmFlowNext_Object((1,3,6,1,4,1,9,9,692,1,2,1,1,3),_CfmFlowNext_Type())
cfmFlowNext.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowNext.setStatus(_A)
_CfmFlowCreateTime_Type=TimeStamp
_CfmFlowCreateTime_Object=MibTableColumn
cfmFlowCreateTime=_CfmFlowCreateTime_Object((1,3,6,1,4,1,9,9,692,1,2,1,1,4),_CfmFlowCreateTime_Type())
cfmFlowCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowCreateTime.setStatus(_A)
_CfmFlowDiscontinuityTime_Type=TimeStamp
_CfmFlowDiscontinuityTime_Object=MibTableColumn
cfmFlowDiscontinuityTime=_CfmFlowDiscontinuityTime_Object((1,3,6,1,4,1,9,9,692,1,2,1,1,5),_CfmFlowDiscontinuityTime_Type())
cfmFlowDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowDiscontinuityTime.setStatus(_A)
class _CfmFlowExpirationTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CfmFlowExpirationTime_Type.__name__=_D
_CfmFlowExpirationTime_Object=MibTableColumn
cfmFlowExpirationTime=_CfmFlowExpirationTime_Object((1,3,6,1,4,1,9,9,692,1,2,1,1,6),_CfmFlowExpirationTime_Type())
cfmFlowExpirationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowExpirationTime.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowExpirationTime.setUnits(_L)
class _CfmFlowDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('ingress',2),('egress',3)))
_CfmFlowDirection_Type.__name__=_F
_CfmFlowDirection_Object=MibTableColumn
cfmFlowDirection=_CfmFlowDirection_Object((1,3,6,1,4,1,9,9,692,1,2,1,1,7),_CfmFlowDirection_Type())
cfmFlowDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowDirection.setStatus(_A)
class _CfmFlowAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),('expire',3)))
_CfmFlowAdminStatus_Type.__name__=_F
_CfmFlowAdminStatus_Object=MibTableColumn
cfmFlowAdminStatus=_CfmFlowAdminStatus_Object((1,3,6,1,4,1,9,9,692,1,2,1,1,8),_CfmFlowAdminStatus_Type())
cfmFlowAdminStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:cfmFlowAdminStatus.setStatus(_A)
class _CfmFlowOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_CfmFlowOperStatus_Type.__name__=_F
_CfmFlowOperStatus_Object=MibTableColumn
cfmFlowOperStatus=_CfmFlowOperStatus_Object((1,3,6,1,4,1,9,9,692,1,2,1,1,9),_CfmFlowOperStatus_Type())
cfmFlowOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowOperStatus.setStatus(_A)
_CfmFlowIngressType_Type=FlowPointType
_CfmFlowIngressType_Object=MibTableColumn
cfmFlowIngressType=_CfmFlowIngressType_Object((1,3,6,1,4,1,9,9,692,1,2,1,1,10),_CfmFlowIngressType_Type())
cfmFlowIngressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowIngressType.setStatus(_A)
_CfmFlowIngress_Type=FlowPointIdentifier
_CfmFlowIngress_Object=MibTableColumn
cfmFlowIngress=_CfmFlowIngress_Object((1,3,6,1,4,1,9,9,692,1,2,1,1,11),_CfmFlowIngress_Type())
cfmFlowIngress.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowIngress.setStatus(_A)
_CfmFlowEgressType_Type=FlowPointType
_CfmFlowEgressType_Object=MibTableColumn
cfmFlowEgressType=_CfmFlowEgressType_Object((1,3,6,1,4,1,9,9,692,1,2,1,1,12),_CfmFlowEgressType_Type())
cfmFlowEgressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowEgressType.setStatus(_A)
_CfmFlowEgress_Type=FlowPointIdentifier
_CfmFlowEgress_Object=MibTableColumn
cfmFlowEgress=_CfmFlowEgress_Object((1,3,6,1,4,1,9,9,692,1,2,1,1,13),_CfmFlowEgress_Type())
cfmFlowEgress.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowEgress.setStatus(_A)
_CfmFlowTableChanged_Type=TimeStamp
_CfmFlowTableChanged_Object=MibScalar
cfmFlowTableChanged=_CfmFlowTableChanged_Object((1,3,6,1,4,1,9,9,692,1,2,2),_CfmFlowTableChanged_Type())
cfmFlowTableChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowTableChanged.setStatus(_A)
_CfmFlowL2VlanTable_Object=MibTable
cfmFlowL2VlanTable=_CfmFlowL2VlanTable_Object((1,3,6,1,4,1,9,9,692,1,2,3))
if mibBuilder.loadTexts:cfmFlowL2VlanTable.setStatus(_A)
_CfmFlowL2VlanEntry_Object=MibTableRow
cfmFlowL2VlanEntry=_CfmFlowL2VlanEntry_Object((1,3,6,1,4,1,9,9,692,1,2,3,1))
cfmFlowL2VlanEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:cfmFlowL2VlanEntry.setStatus(_A)
_CfmFlowL2VlanNext_Type=RowPointer
_CfmFlowL2VlanNext_Object=MibTableColumn
cfmFlowL2VlanNext=_CfmFlowL2VlanNext_Object((1,3,6,1,4,1,9,9,692,1,2,3,1,1),_CfmFlowL2VlanNext_Type())
cfmFlowL2VlanNext.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowL2VlanNext.setStatus(_A)
_CfmFlowL2VlanId_Type=VlanId
_CfmFlowL2VlanId_Object=MibTableColumn
cfmFlowL2VlanId=_CfmFlowL2VlanId_Object((1,3,6,1,4,1,9,9,692,1,2,3,1,2),_CfmFlowL2VlanId_Type())
cfmFlowL2VlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowL2VlanId.setStatus(_A)
_CfmFlowL2VlanCos_Type=Layer2Cos
_CfmFlowL2VlanCos_Object=MibTableColumn
cfmFlowL2VlanCos=_CfmFlowL2VlanCos_Object((1,3,6,1,4,1,9,9,692,1,2,3,1,3),_CfmFlowL2VlanCos_Type())
cfmFlowL2VlanCos.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowL2VlanCos.setStatus(_A)
_CfmFlowL2VlanTableChanged_Type=TimeStamp
_CfmFlowL2VlanTableChanged_Object=MibScalar
cfmFlowL2VlanTableChanged=_CfmFlowL2VlanTableChanged_Object((1,3,6,1,4,1,9,9,692,1,2,4),_CfmFlowL2VlanTableChanged_Type())
cfmFlowL2VlanTableChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowL2VlanTableChanged.setStatus(_A)
_CfmFlowIpTable_Object=MibTable
cfmFlowIpTable=_CfmFlowIpTable_Object((1,3,6,1,4,1,9,9,692,1,2,5))
if mibBuilder.loadTexts:cfmFlowIpTable.setStatus(_A)
_CfmFlowIpEntry_Object=MibTableRow
cfmFlowIpEntry=_CfmFlowIpEntry_Object((1,3,6,1,4,1,9,9,692,1,2,5,1))
cfmFlowIpEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:cfmFlowIpEntry.setStatus(_A)
_CfmFlowIpNext_Type=RowPointer
_CfmFlowIpNext_Object=MibTableColumn
cfmFlowIpNext=_CfmFlowIpNext_Object((1,3,6,1,4,1,9,9,692,1,2,5,1,1),_CfmFlowIpNext_Type())
cfmFlowIpNext.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowIpNext.setStatus(_A)
_CfmFlowIpAddrType_Type=InetAddressType
_CfmFlowIpAddrType_Object=MibTableColumn
cfmFlowIpAddrType=_CfmFlowIpAddrType_Object((1,3,6,1,4,1,9,9,692,1,2,5,1,2),_CfmFlowIpAddrType_Type())
cfmFlowIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowIpAddrType.setStatus(_A)
_CfmFlowIpAddrSrc_Type=InetAddress
_CfmFlowIpAddrSrc_Object=MibTableColumn
cfmFlowIpAddrSrc=_CfmFlowIpAddrSrc_Object((1,3,6,1,4,1,9,9,692,1,2,5,1,3),_CfmFlowIpAddrSrc_Type())
cfmFlowIpAddrSrc.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowIpAddrSrc.setStatus(_A)
_CfmFlowIpAddrDst_Type=InetAddress
_CfmFlowIpAddrDst_Object=MibTableColumn
cfmFlowIpAddrDst=_CfmFlowIpAddrDst_Object((1,3,6,1,4,1,9,9,692,1,2,5,1,4),_CfmFlowIpAddrDst_Type())
cfmFlowIpAddrDst.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowIpAddrDst.setStatus(_A)
class _CfmFlowIpValid_Type(Bits):namedValues=NamedValues(*(('trafficClass',0),('hopLimit',1)))
_CfmFlowIpValid_Type.__name__=_J
_CfmFlowIpValid_Object=MibTableColumn
cfmFlowIpValid=_CfmFlowIpValid_Object((1,3,6,1,4,1,9,9,692,1,2,5,1,5),_CfmFlowIpValid_Type())
cfmFlowIpValid.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowIpValid.setStatus(_A)
class _CfmFlowIpTrafficClass_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CfmFlowIpTrafficClass_Type.__name__=_D
_CfmFlowIpTrafficClass_Object=MibTableColumn
cfmFlowIpTrafficClass=_CfmFlowIpTrafficClass_Object((1,3,6,1,4,1,9,9,692,1,2,5,1,6),_CfmFlowIpTrafficClass_Type())
cfmFlowIpTrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowIpTrafficClass.setStatus(_A)
class _CfmFlowIpHopLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CfmFlowIpHopLimit_Type.__name__=_D
_CfmFlowIpHopLimit_Object=MibTableColumn
cfmFlowIpHopLimit=_CfmFlowIpHopLimit_Object((1,3,6,1,4,1,9,9,692,1,2,5,1,7),_CfmFlowIpHopLimit_Type())
cfmFlowIpHopLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowIpHopLimit.setStatus(_A)
_CfmFlowIpTableChanged_Type=TimeStamp
_CfmFlowIpTableChanged_Object=MibScalar
cfmFlowIpTableChanged=_CfmFlowIpTableChanged_Object((1,3,6,1,4,1,9,9,692,1,2,6),_CfmFlowIpTableChanged_Type())
cfmFlowIpTableChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowIpTableChanged.setStatus(_A)
_CfmFlowUdpTable_Object=MibTable
cfmFlowUdpTable=_CfmFlowUdpTable_Object((1,3,6,1,4,1,9,9,692,1,2,7))
if mibBuilder.loadTexts:cfmFlowUdpTable.setStatus(_A)
_CfmFlowUdpEntry_Object=MibTableRow
cfmFlowUdpEntry=_CfmFlowUdpEntry_Object((1,3,6,1,4,1,9,9,692,1,2,7,1))
cfmFlowUdpEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:cfmFlowUdpEntry.setStatus(_A)
_CfmFlowUdpNext_Type=RowPointer
_CfmFlowUdpNext_Object=MibTableColumn
cfmFlowUdpNext=_CfmFlowUdpNext_Object((1,3,6,1,4,1,9,9,692,1,2,7,1,1),_CfmFlowUdpNext_Type())
cfmFlowUdpNext.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowUdpNext.setStatus(_A)
_CfmFlowUdpPortSrc_Type=InetPortNumber
_CfmFlowUdpPortSrc_Object=MibTableColumn
cfmFlowUdpPortSrc=_CfmFlowUdpPortSrc_Object((1,3,6,1,4,1,9,9,692,1,2,7,1,2),_CfmFlowUdpPortSrc_Type())
cfmFlowUdpPortSrc.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowUdpPortSrc.setStatus(_A)
_CfmFlowUdpPortDst_Type=InetPortNumber
_CfmFlowUdpPortDst_Object=MibTableColumn
cfmFlowUdpPortDst=_CfmFlowUdpPortDst_Object((1,3,6,1,4,1,9,9,692,1,2,7,1,3),_CfmFlowUdpPortDst_Type())
cfmFlowUdpPortDst.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowUdpPortDst.setStatus(_A)
_CfmFlowUdpTableChanged_Type=TimeStamp
_CfmFlowUdpTableChanged_Object=MibScalar
cfmFlowUdpTableChanged=_CfmFlowUdpTableChanged_Object((1,3,6,1,4,1,9,9,692,1,2,8),_CfmFlowUdpTableChanged_Type())
cfmFlowUdpTableChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowUdpTableChanged.setStatus(_A)
_CfmFlowTcpTable_Object=MibTable
cfmFlowTcpTable=_CfmFlowTcpTable_Object((1,3,6,1,4,1,9,9,692,1,2,9))
if mibBuilder.loadTexts:cfmFlowTcpTable.setStatus(_A)
_CfmFlowTcpEntry_Object=MibTableRow
cfmFlowTcpEntry=_CfmFlowTcpEntry_Object((1,3,6,1,4,1,9,9,692,1,2,9,1))
cfmFlowTcpEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:cfmFlowTcpEntry.setStatus(_A)
_CfmFlowTcpNext_Type=RowPointer
_CfmFlowTcpNext_Object=MibTableColumn
cfmFlowTcpNext=_CfmFlowTcpNext_Object((1,3,6,1,4,1,9,9,692,1,2,9,1,1),_CfmFlowTcpNext_Type())
cfmFlowTcpNext.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowTcpNext.setStatus(_A)
_CfmFlowTcpPortSrc_Type=InetPortNumber
_CfmFlowTcpPortSrc_Object=MibTableColumn
cfmFlowTcpPortSrc=_CfmFlowTcpPortSrc_Object((1,3,6,1,4,1,9,9,692,1,2,9,1,2),_CfmFlowTcpPortSrc_Type())
cfmFlowTcpPortSrc.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowTcpPortSrc.setStatus(_A)
_CfmFlowTcpPortDst_Type=InetPortNumber
_CfmFlowTcpPortDst_Object=MibTableColumn
cfmFlowTcpPortDst=_CfmFlowTcpPortDst_Object((1,3,6,1,4,1,9,9,692,1,2,9,1,3),_CfmFlowTcpPortDst_Type())
cfmFlowTcpPortDst.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowTcpPortDst.setStatus(_A)
_CfmFlowTcpTableChanged_Type=TimeStamp
_CfmFlowTcpTableChanged_Object=MibScalar
cfmFlowTcpTableChanged=_CfmFlowTcpTableChanged_Object((1,3,6,1,4,1,9,9,692,1,2,10),_CfmFlowTcpTableChanged_Type())
cfmFlowTcpTableChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowTcpTableChanged.setStatus(_A)
_CfmFlowRtpTable_Object=MibTable
cfmFlowRtpTable=_CfmFlowRtpTable_Object((1,3,6,1,4,1,9,9,692,1,2,11))
if mibBuilder.loadTexts:cfmFlowRtpTable.setStatus(_A)
_CfmFlowRtpEntry_Object=MibTableRow
cfmFlowRtpEntry=_CfmFlowRtpEntry_Object((1,3,6,1,4,1,9,9,692,1,2,11,1))
cfmFlowRtpEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:cfmFlowRtpEntry.setStatus(_A)
_CfmFlowRtpNext_Type=RowPointer
_CfmFlowRtpNext_Object=MibTableColumn
cfmFlowRtpNext=_CfmFlowRtpNext_Object((1,3,6,1,4,1,9,9,692,1,2,11,1,1),_CfmFlowRtpNext_Type())
cfmFlowRtpNext.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowRtpNext.setStatus(_A)
class _CfmFlowRtpVersion_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_CfmFlowRtpVersion_Type.__name__=_D
_CfmFlowRtpVersion_Object=MibTableColumn
cfmFlowRtpVersion=_CfmFlowRtpVersion_Object((1,3,6,1,4,1,9,9,692,1,2,11,1,2),_CfmFlowRtpVersion_Type())
cfmFlowRtpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowRtpVersion.setStatus(_A)
class _CfmFlowRtpSsrc_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CfmFlowRtpSsrc_Type.__name__=_D
_CfmFlowRtpSsrc_Object=MibTableColumn
cfmFlowRtpSsrc=_CfmFlowRtpSsrc_Object((1,3,6,1,4,1,9,9,692,1,2,11,1,3),_CfmFlowRtpSsrc_Type())
cfmFlowRtpSsrc.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowRtpSsrc.setStatus(_A)
class _CfmFlowRtpPayloadType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_CfmFlowRtpPayloadType_Type.__name__=_D
_CfmFlowRtpPayloadType_Object=MibTableColumn
cfmFlowRtpPayloadType=_CfmFlowRtpPayloadType_Object((1,3,6,1,4,1,9,9,692,1,2,11,1,4),_CfmFlowRtpPayloadType_Type())
cfmFlowRtpPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowRtpPayloadType.setStatus(_A)
_CfmFlowRtpTableChanged_Type=TimeStamp
_CfmFlowRtpTableChanged_Object=MibScalar
cfmFlowRtpTableChanged=_CfmFlowRtpTableChanged_Object((1,3,6,1,4,1,9,9,692,1,2,12),_CfmFlowRtpTableChanged_Type())
cfmFlowRtpTableChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowRtpTableChanged.setStatus(_A)
_CfmFlowMetrics_ObjectIdentity=ObjectIdentity
cfmFlowMetrics=_CfmFlowMetrics_ObjectIdentity((1,3,6,1,4,1,9,9,692,1,3))
_CfmFlowMetricsTable_Object=MibTable
cfmFlowMetricsTable=_CfmFlowMetricsTable_Object((1,3,6,1,4,1,9,9,692,1,3,1))
if mibBuilder.loadTexts:cfmFlowMetricsTable.setStatus(_A)
_CfmFlowMetricsEntry_Object=MibTableRow
cfmFlowMetricsEntry=_CfmFlowMetricsEntry_Object((1,3,6,1,4,1,9,9,692,1,3,1,1))
cfmFlowMetricsEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:cfmFlowMetricsEntry.setStatus(_A)
_CfmFlowMetricsCollected_Type=FlowMetrics
_CfmFlowMetricsCollected_Object=MibTableColumn
cfmFlowMetricsCollected=_CfmFlowMetricsCollected_Object((1,3,6,1,4,1,9,9,692,1,3,1,1,1),_CfmFlowMetricsCollected_Type())
cfmFlowMetricsCollected.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsCollected.setStatus(_A)
class _CfmFlowMetricsIntervalTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_CfmFlowMetricsIntervalTime_Type.__name__=_D
_CfmFlowMetricsIntervalTime_Object=MibTableColumn
cfmFlowMetricsIntervalTime=_CfmFlowMetricsIntervalTime_Object((1,3,6,1,4,1,9,9,692,1,3,1,1,2),_CfmFlowMetricsIntervalTime_Type())
cfmFlowMetricsIntervalTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsIntervalTime.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMetricsIntervalTime.setUnits(_L)
class _CfmFlowMetricsMaxIntervals_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CfmFlowMetricsMaxIntervals_Type.__name__=_D
_CfmFlowMetricsMaxIntervals_Object=MibTableColumn
cfmFlowMetricsMaxIntervals=_CfmFlowMetricsMaxIntervals_Object((1,3,6,1,4,1,9,9,692,1,3,1,1,3),_CfmFlowMetricsMaxIntervals_Type())
cfmFlowMetricsMaxIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsMaxIntervals.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMetricsMaxIntervals.setUnits(_N)
_CfmFlowMetricsElapsedTime_Type=Gauge32
_CfmFlowMetricsElapsedTime_Object=MibTableColumn
cfmFlowMetricsElapsedTime=_CfmFlowMetricsElapsedTime_Object((1,3,6,1,4,1,9,9,692,1,3,1,1,4),_CfmFlowMetricsElapsedTime_Type())
cfmFlowMetricsElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMetricsElapsedTime.setUnits(_L)
_CfmFlowMetricsIntervals_Type=Gauge32
_CfmFlowMetricsIntervals_Object=MibTableColumn
cfmFlowMetricsIntervals=_CfmFlowMetricsIntervals_Object((1,3,6,1,4,1,9,9,692,1,3,1,1,5),_CfmFlowMetricsIntervals_Type())
cfmFlowMetricsIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsIntervals.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMetricsIntervals.setUnits(_N)
_CfmFlowMetricsInvalidIntervals_Type=Gauge32
_CfmFlowMetricsInvalidIntervals_Object=MibTableColumn
cfmFlowMetricsInvalidIntervals=_CfmFlowMetricsInvalidIntervals_Object((1,3,6,1,4,1,9,9,692,1,3,1,1,6),_CfmFlowMetricsInvalidIntervals_Type())
cfmFlowMetricsInvalidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsInvalidIntervals.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMetricsInvalidIntervals.setUnits(_N)
_CfmFlowMetricsConditionsProfile_Type=FlowMonitorConditionsProfileOrZero
_CfmFlowMetricsConditionsProfile_Object=MibTableColumn
cfmFlowMetricsConditionsProfile=_CfmFlowMetricsConditionsProfile_Object((1,3,6,1,4,1,9,9,692,1,3,1,1,7),_CfmFlowMetricsConditionsProfile_Type())
cfmFlowMetricsConditionsProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsConditionsProfile.setStatus(_A)
_CfmFlowMetricsConditions_Type=FlowMonitorConditions
_CfmFlowMetricsConditions_Object=MibTableColumn
cfmFlowMetricsConditions=_CfmFlowMetricsConditions_Object((1,3,6,1,4,1,9,9,692,1,3,1,1,8),_CfmFlowMetricsConditions_Type())
cfmFlowMetricsConditions.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsConditions.setStatus(_A)
_CfmFlowMetricsAlarms_Type=FlowMonitorConditions
_CfmFlowMetricsAlarms_Object=MibTableColumn
cfmFlowMetricsAlarms=_CfmFlowMetricsAlarms_Object((1,3,6,1,4,1,9,9,692,1,3,1,1,9),_CfmFlowMetricsAlarms_Type())
cfmFlowMetricsAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsAlarms.setStatus(_A)
_CfmFlowMetricsAlarmSeverity_Type=CiscoAlarmSeverity
_CfmFlowMetricsAlarmSeverity_Object=MibTableColumn
cfmFlowMetricsAlarmSeverity=_CfmFlowMetricsAlarmSeverity_Object((1,3,6,1,4,1,9,9,692,1,3,1,1,10),_CfmFlowMetricsAlarmSeverity_Type())
cfmFlowMetricsAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsAlarmSeverity.setStatus(_A)
_CfmFlowMetricsPkts_Type=Counter64
_CfmFlowMetricsPkts_Object=MibTableColumn
cfmFlowMetricsPkts=_CfmFlowMetricsPkts_Object((1,3,6,1,4,1,9,9,692,1,3,1,1,11),_CfmFlowMetricsPkts_Type())
cfmFlowMetricsPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsPkts.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMetricsPkts.setUnits(_Y)
_CfmFlowMetricsOctets_Type=Counter64
_CfmFlowMetricsOctets_Object=MibTableColumn
cfmFlowMetricsOctets=_CfmFlowMetricsOctets_Object((1,3,6,1,4,1,9,9,692,1,3,1,1,12),_CfmFlowMetricsOctets_Type())
cfmFlowMetricsOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsOctets.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMetricsOctets.setUnits(_Z)
_CfmFlowMetricsBitRateUnits_Type=FlowBitRateUnits
_CfmFlowMetricsBitRateUnits_Object=MibTableColumn
cfmFlowMetricsBitRateUnits=_CfmFlowMetricsBitRateUnits_Object((1,3,6,1,4,1,9,9,692,1,3,1,1,13),_CfmFlowMetricsBitRateUnits_Type())
cfmFlowMetricsBitRateUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsBitRateUnits.setStatus(_A)
_CfmFlowMetricsBitRate_Type=Gauge32
_CfmFlowMetricsBitRate_Object=MibTableColumn
cfmFlowMetricsBitRate=_CfmFlowMetricsBitRate_Object((1,3,6,1,4,1,9,9,692,1,3,1,1,14),_CfmFlowMetricsBitRate_Type())
cfmFlowMetricsBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsBitRate.setStatus(_A)
_CfmFlowMetricsPktRate_Type=Gauge32
_CfmFlowMetricsPktRate_Object=MibTableColumn
cfmFlowMetricsPktRate=_CfmFlowMetricsPktRate_Object((1,3,6,1,4,1,9,9,692,1,3,1,1,15),_CfmFlowMetricsPktRate_Type())
cfmFlowMetricsPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsPktRate.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMetricsPktRate.setUnits(_a)
_CfmFlowMetricsTableChanged_Type=TimeStamp
_CfmFlowMetricsTableChanged_Object=MibScalar
cfmFlowMetricsTableChanged=_CfmFlowMetricsTableChanged_Object((1,3,6,1,4,1,9,9,692,1,3,2),_CfmFlowMetricsTableChanged_Type())
cfmFlowMetricsTableChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsTableChanged.setStatus(_A)
_CfmFlowMetricsIntTable_Object=MibTable
cfmFlowMetricsIntTable=_CfmFlowMetricsIntTable_Object((1,3,6,1,4,1,9,9,692,1,3,3))
if mibBuilder.loadTexts:cfmFlowMetricsIntTable.setStatus(_A)
_CfmFlowMetricsIntEntry_Object=MibTableRow
cfmFlowMetricsIntEntry=_CfmFlowMetricsIntEntry_Object((1,3,6,1,4,1,9,9,692,1,3,3,1))
cfmFlowMetricsIntEntry.setIndexNames((0,_B,_E),(0,_B,_H),(0,_B,_b))
if mibBuilder.loadTexts:cfmFlowMetricsIntEntry.setStatus(_A)
class _CfmFlowMetricsIntNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CfmFlowMetricsIntNumber_Type.__name__=_D
_CfmFlowMetricsIntNumber_Object=MibTableColumn
cfmFlowMetricsIntNumber=_CfmFlowMetricsIntNumber_Object((1,3,6,1,4,1,9,9,692,1,3,3,1,1),_CfmFlowMetricsIntNumber_Type())
cfmFlowMetricsIntNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:cfmFlowMetricsIntNumber.setStatus(_A)
_CfmFlowMetricsIntValid_Type=TruthValue
_CfmFlowMetricsIntValid_Object=MibTableColumn
cfmFlowMetricsIntValid=_CfmFlowMetricsIntValid_Object((1,3,6,1,4,1,9,9,692,1,3,3,1,2),_CfmFlowMetricsIntValid_Type())
cfmFlowMetricsIntValid.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsIntValid.setStatus(_A)
_CfmFlowMetricsIntTime_Type=TimeStamp
_CfmFlowMetricsIntTime_Object=MibTableColumn
cfmFlowMetricsIntTime=_CfmFlowMetricsIntTime_Object((1,3,6,1,4,1,9,9,692,1,3,3,1,3),_CfmFlowMetricsIntTime_Type())
cfmFlowMetricsIntTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsIntTime.setStatus(_A)
_CfmFlowMetricsIntConditions_Type=FlowMonitorConditions
_CfmFlowMetricsIntConditions_Object=MibTableColumn
cfmFlowMetricsIntConditions=_CfmFlowMetricsIntConditions_Object((1,3,6,1,4,1,9,9,692,1,3,3,1,4),_CfmFlowMetricsIntConditions_Type())
cfmFlowMetricsIntConditions.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsIntConditions.setStatus(_A)
_CfmFlowMetricsIntAlarms_Type=FlowMonitorConditions
_CfmFlowMetricsIntAlarms_Object=MibTableColumn
cfmFlowMetricsIntAlarms=_CfmFlowMetricsIntAlarms_Object((1,3,6,1,4,1,9,9,692,1,3,3,1,5),_CfmFlowMetricsIntAlarms_Type())
cfmFlowMetricsIntAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsIntAlarms.setStatus(_A)
_CfmFlowMetricsIntAlarmSeverity_Type=CiscoAlarmSeverity
_CfmFlowMetricsIntAlarmSeverity_Object=MibTableColumn
cfmFlowMetricsIntAlarmSeverity=_CfmFlowMetricsIntAlarmSeverity_Object((1,3,6,1,4,1,9,9,692,1,3,3,1,6),_CfmFlowMetricsIntAlarmSeverity_Type())
cfmFlowMetricsIntAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsIntAlarmSeverity.setStatus(_A)
_CfmFlowMetricsIntPkts_Type=ReportIntervalCount
_CfmFlowMetricsIntPkts_Object=MibTableColumn
cfmFlowMetricsIntPkts=_CfmFlowMetricsIntPkts_Object((1,3,6,1,4,1,9,9,692,1,3,3,1,7),_CfmFlowMetricsIntPkts_Type())
cfmFlowMetricsIntPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsIntPkts.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMetricsIntPkts.setUnits(_Y)
_CfmFlowMetricsIntOctets_Type=ReportIntervalCount
_CfmFlowMetricsIntOctets_Object=MibTableColumn
cfmFlowMetricsIntOctets=_CfmFlowMetricsIntOctets_Object((1,3,6,1,4,1,9,9,692,1,3,3,1,8),_CfmFlowMetricsIntOctets_Type())
cfmFlowMetricsIntOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsIntOctets.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMetricsIntOctets.setUnits(_Z)
_CfmFlowMetricsIntBitRateUnits_Type=FlowBitRateUnits
_CfmFlowMetricsIntBitRateUnits_Object=MibTableColumn
cfmFlowMetricsIntBitRateUnits=_CfmFlowMetricsIntBitRateUnits_Object((1,3,6,1,4,1,9,9,692,1,3,3,1,9),_CfmFlowMetricsIntBitRateUnits_Type())
cfmFlowMetricsIntBitRateUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsIntBitRateUnits.setStatus(_A)
_CfmFlowMetricsIntBitRate_Type=ReportIntervalCount
_CfmFlowMetricsIntBitRate_Object=MibTableColumn
cfmFlowMetricsIntBitRate=_CfmFlowMetricsIntBitRate_Object((1,3,6,1,4,1,9,9,692,1,3,3,1,10),_CfmFlowMetricsIntBitRate_Type())
cfmFlowMetricsIntBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsIntBitRate.setStatus(_A)
_CfmFlowMetricsIntPktRate_Type=ReportIntervalCount
_CfmFlowMetricsIntPktRate_Object=MibTableColumn
cfmFlowMetricsIntPktRate=_CfmFlowMetricsIntPktRate_Object((1,3,6,1,4,1,9,9,692,1,3,3,1,11),_CfmFlowMetricsIntPktRate_Type())
cfmFlowMetricsIntPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmFlowMetricsIntPktRate.setStatus(_A)
if mibBuilder.loadTexts:cfmFlowMetricsIntPktRate.setUnits(_a)
_CfmConditions_ObjectIdentity=ObjectIdentity
cfmConditions=_CfmConditions_ObjectIdentity((1,3,6,1,4,1,9,9,692,1,4))
_CfmConditionTable_Object=MibTable
cfmConditionTable=_CfmConditionTable_Object((1,3,6,1,4,1,9,9,692,1,4,1))
if mibBuilder.loadTexts:cfmConditionTable.setStatus(_A)
_CfmConditionEntry_Object=MibTableRow
cfmConditionEntry=_CfmConditionEntry_Object((1,3,6,1,4,1,9,9,692,1,4,1,1))
cfmConditionEntry.setIndexNames((0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:cfmConditionEntry.setStatus(_A)
_CfmConditionProfile_Type=FlowMonitorConditionsProfile
_CfmConditionProfile_Object=MibTableColumn
cfmConditionProfile=_CfmConditionProfile_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,1),_CfmConditionProfile_Type())
cfmConditionProfile.setMaxAccess(_G)
if mibBuilder.loadTexts:cfmConditionProfile.setStatus(_A)
_CfmConditionId_Type=FlowMonitorConditionIdentifier
_CfmConditionId_Object=MibTableColumn
cfmConditionId=_CfmConditionId_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,2),_CfmConditionId_Type())
cfmConditionId.setMaxAccess(_G)
if mibBuilder.loadTexts:cfmConditionId.setStatus(_A)
_CfmConditionDescr_Type=SnmpAdminString
_CfmConditionDescr_Object=MibTableColumn
cfmConditionDescr=_CfmConditionDescr_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,3),_CfmConditionDescr_Type())
cfmConditionDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionDescr.setStatus(_A)
_CfmConditionMonitoredElement_Type=AutonomousType
_CfmConditionMonitoredElement_Object=MibTableColumn
cfmConditionMonitoredElement=_CfmConditionMonitoredElement_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,4),_CfmConditionMonitoredElement_Type())
cfmConditionMonitoredElement.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionMonitoredElement.setStatus(_A)
class _CfmConditionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),('boolean',2),('risingThreshold',3),('fallingThreshold',4),('risingAndFallingThreshold',5)))
_CfmConditionType_Type.__name__=_F
_CfmConditionType_Object=MibTableColumn
cfmConditionType=_CfmConditionType_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,5),_CfmConditionType_Type())
cfmConditionType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionType.setStatus(_A)
_CfmConditionThreshRiseScale_Type=FlowMetricScale
_CfmConditionThreshRiseScale_Object=MibTableColumn
cfmConditionThreshRiseScale=_CfmConditionThreshRiseScale_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,6),_CfmConditionThreshRiseScale_Type())
cfmConditionThreshRiseScale.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionThreshRiseScale.setStatus(_A)
_CfmConditionThreshRisePrecision_Type=FlowMetricPrecision
_CfmConditionThreshRisePrecision_Object=MibTableColumn
cfmConditionThreshRisePrecision=_CfmConditionThreshRisePrecision_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,7),_CfmConditionThreshRisePrecision_Type())
cfmConditionThreshRisePrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionThreshRisePrecision.setStatus(_A)
_CfmConditionThreshRise_Type=FlowMetricValue
_CfmConditionThreshRise_Object=MibTableColumn
cfmConditionThreshRise=_CfmConditionThreshRise_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,8),_CfmConditionThreshRise_Type())
cfmConditionThreshRise.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionThreshRise.setStatus(_A)
_CfmConditionThreshFallScale_Type=FlowMetricScale
_CfmConditionThreshFallScale_Object=MibTableColumn
cfmConditionThreshFallScale=_CfmConditionThreshFallScale_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,9),_CfmConditionThreshFallScale_Type())
cfmConditionThreshFallScale.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionThreshFallScale.setStatus(_A)
_CfmConditionThreshFallPrecision_Type=FlowMetricPrecision
_CfmConditionThreshFallPrecision_Object=MibTableColumn
cfmConditionThreshFallPrecision=_CfmConditionThreshFallPrecision_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,10),_CfmConditionThreshFallPrecision_Type())
cfmConditionThreshFallPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionThreshFallPrecision.setStatus(_A)
_CfmConditionThreshFall_Type=FlowMetricValue
_CfmConditionThreshFall_Object=MibTableColumn
cfmConditionThreshFall=_CfmConditionThreshFall_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,11),_CfmConditionThreshFall_Type())
cfmConditionThreshFall.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionThreshFall.setStatus(_A)
class _CfmConditionSampleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),('raw',2),('slidingWindowAvg',3),('expDecayingAvg',4)))
_CfmConditionSampleType_Type.__name__=_F
_CfmConditionSampleType_Object=MibTableColumn
cfmConditionSampleType=_CfmConditionSampleType_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,13),_CfmConditionSampleType_Type())
cfmConditionSampleType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionSampleType.setStatus(_A)
class _CfmConditionSampleWindow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CfmConditionSampleWindow_Type.__name__=_D
_CfmConditionSampleWindow_Object=MibTableColumn
cfmConditionSampleWindow=_CfmConditionSampleWindow_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,14),_CfmConditionSampleWindow_Type())
cfmConditionSampleWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionSampleWindow.setStatus(_A)
class _CfmConditionAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('discrete',2),('grouped',3)))
_CfmConditionAlarm_Type.__name__=_F
_CfmConditionAlarm_Object=MibTableColumn
cfmConditionAlarm=_CfmConditionAlarm_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,15),_CfmConditionAlarm_Type())
cfmConditionAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionAlarm.setStatus(_A)
class _CfmConditionAlarmActions_Type(Bits):namedValues=NamedValues(*(('syslog',0),('snmp',1)))
_CfmConditionAlarmActions_Type.__name__=_J
_CfmConditionAlarmActions_Object=MibTableColumn
cfmConditionAlarmActions=_CfmConditionAlarmActions_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,16),_CfmConditionAlarmActions_Type())
cfmConditionAlarmActions.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionAlarmActions.setStatus(_A)
_CfmConditionAlarmSeverity_Type=CiscoAlarmSeverity
_CfmConditionAlarmSeverity_Object=MibTableColumn
cfmConditionAlarmSeverity=_CfmConditionAlarmSeverity_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,17),_CfmConditionAlarmSeverity_Type())
cfmConditionAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionAlarmSeverity.setStatus(_A)
_CfmConditionAlarmGroup_Type=FlowMonitorAlarmGroupIdentifier
_CfmConditionAlarmGroup_Object=MibTableColumn
cfmConditionAlarmGroup=_CfmConditionAlarmGroup_Object((1,3,6,1,4,1,9,9,692,1,4,1,1,18),_CfmConditionAlarmGroup_Type())
cfmConditionAlarmGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionAlarmGroup.setStatus(_A)
_CfmConditionTableChanged_Type=TimeStamp
_CfmConditionTableChanged_Object=MibScalar
cfmConditionTableChanged=_CfmConditionTableChanged_Object((1,3,6,1,4,1,9,9,692,1,4,2),_CfmConditionTableChanged_Type())
cfmConditionTableChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmConditionTableChanged.setStatus(_A)
_CfmAlarmGroups_ObjectIdentity=ObjectIdentity
cfmAlarmGroups=_CfmAlarmGroups_ObjectIdentity((1,3,6,1,4,1,9,9,692,1,5))
_CfmAlarmGroupTable_Object=MibTable
cfmAlarmGroupTable=_CfmAlarmGroupTable_Object((1,3,6,1,4,1,9,9,692,1,5,1))
if mibBuilder.loadTexts:cfmAlarmGroupTable.setStatus(_A)
_CfmAlarmGroupEntry_Object=MibTableRow
cfmAlarmGroupEntry=_CfmAlarmGroupEntry_Object((1,3,6,1,4,1,9,9,692,1,5,1,1))
cfmAlarmGroupEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:cfmAlarmGroupEntry.setStatus(_A)
_CfmAlarmGroupId_Type=FlowMonitorAlarmGroupIdentifier
_CfmAlarmGroupId_Object=MibTableColumn
cfmAlarmGroupId=_CfmAlarmGroupId_Object((1,3,6,1,4,1,9,9,692,1,5,1,1,1),_CfmAlarmGroupId_Type())
cfmAlarmGroupId.setMaxAccess(_G)
if mibBuilder.loadTexts:cfmAlarmGroupId.setStatus(_A)
_CfmAlarmGroupDescr_Type=SnmpAdminString
_CfmAlarmGroupDescr_Object=MibTableColumn
cfmAlarmGroupDescr=_CfmAlarmGroupDescr_Object((1,3,6,1,4,1,9,9,692,1,5,1,1,2),_CfmAlarmGroupDescr_Type())
cfmAlarmGroupDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmGroupDescr.setStatus(_A)
_CfmAlarmGroupConditionsProfile_Type=FlowMonitorConditionsProfile
_CfmAlarmGroupConditionsProfile_Object=MibTableColumn
cfmAlarmGroupConditionsProfile=_CfmAlarmGroupConditionsProfile_Object((1,3,6,1,4,1,9,9,692,1,5,1,1,3),_CfmAlarmGroupConditionsProfile_Type())
cfmAlarmGroupConditionsProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmGroupConditionsProfile.setStatus(_A)
_CfmAlarmGroupConditionId_Type=FlowMonitorConditionIdentifier
_CfmAlarmGroupConditionId_Object=MibTableColumn
cfmAlarmGroupConditionId=_CfmAlarmGroupConditionId_Object((1,3,6,1,4,1,9,9,692,1,5,1,1,4),_CfmAlarmGroupConditionId_Type())
cfmAlarmGroupConditionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmGroupConditionId.setStatus(_A)
_CfmAlarmGroupFlowSet_Type=FlowSetIdentifier
_CfmAlarmGroupFlowSet_Object=MibTableColumn
cfmAlarmGroupFlowSet=_CfmAlarmGroupFlowSet_Object((1,3,6,1,4,1,9,9,692,1,5,1,1,5),_CfmAlarmGroupFlowSet_Type())
cfmAlarmGroupFlowSet.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmGroupFlowSet.setStatus(_A)
_CfmAlarmGroupFlowCount_Type=Gauge32
_CfmAlarmGroupFlowCount_Object=MibTableColumn
cfmAlarmGroupFlowCount=_CfmAlarmGroupFlowCount_Object((1,3,6,1,4,1,9,9,692,1,5,1,1,6),_CfmAlarmGroupFlowCount_Type())
cfmAlarmGroupFlowCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmGroupFlowCount.setStatus(_A)
if mibBuilder.loadTexts:cfmAlarmGroupFlowCount.setUnits(_K)
class _CfmAlarmGroupThresholdUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('flows',2),('percent',3)))
_CfmAlarmGroupThresholdUnits_Type.__name__=_F
_CfmAlarmGroupThresholdUnits_Object=MibTableColumn
cfmAlarmGroupThresholdUnits=_CfmAlarmGroupThresholdUnits_Object((1,3,6,1,4,1,9,9,692,1,5,1,1,7),_CfmAlarmGroupThresholdUnits_Type())
cfmAlarmGroupThresholdUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmGroupThresholdUnits.setStatus(_A)
class _CfmAlarmGroupThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CfmAlarmGroupThreshold_Type.__name__=_D
_CfmAlarmGroupThreshold_Object=MibTableColumn
cfmAlarmGroupThreshold=_CfmAlarmGroupThreshold_Object((1,3,6,1,4,1,9,9,692,1,5,1,1,8),_CfmAlarmGroupThreshold_Type())
cfmAlarmGroupThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmGroupThreshold.setStatus(_A)
_CfmAlarmGroupRaised_Type=TruthValue
_CfmAlarmGroupRaised_Object=MibTableColumn
cfmAlarmGroupRaised=_CfmAlarmGroupRaised_Object((1,3,6,1,4,1,9,9,692,1,5,1,1,9),_CfmAlarmGroupRaised_Type())
cfmAlarmGroupRaised.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmGroupRaised.setStatus(_A)
_CfmAlarmGroupCurrentCount_Type=Gauge32
_CfmAlarmGroupCurrentCount_Object=MibTableColumn
cfmAlarmGroupCurrentCount=_CfmAlarmGroupCurrentCount_Object((1,3,6,1,4,1,9,9,692,1,5,1,1,10),_CfmAlarmGroupCurrentCount_Type())
cfmAlarmGroupCurrentCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmGroupCurrentCount.setStatus(_A)
if mibBuilder.loadTexts:cfmAlarmGroupCurrentCount.setUnits(_K)
_CfmAlarmGroupTableChanged_Type=TimeStamp
_CfmAlarmGroupTableChanged_Object=MibScalar
cfmAlarmGroupTableChanged=_CfmAlarmGroupTableChanged_Object((1,3,6,1,4,1,9,9,692,1,5,2),_CfmAlarmGroupTableChanged_Type())
cfmAlarmGroupTableChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmGroupTableChanged.setStatus(_A)
_CfmAlarmGroupFlowTable_Object=MibTable
cfmAlarmGroupFlowTable=_CfmAlarmGroupFlowTable_Object((1,3,6,1,4,1,9,9,692,1,5,3))
if mibBuilder.loadTexts:cfmAlarmGroupFlowTable.setStatus(_A)
_CfmAlarmGroupFlowEntry_Object=MibTableRow
cfmAlarmGroupFlowEntry=_CfmAlarmGroupFlowEntry_Object((1,3,6,1,4,1,9,9,692,1,5,3,1))
cfmAlarmGroupFlowEntry.setIndexNames((0,_B,_f),(0,_B,_g),(0,_B,_P))
if mibBuilder.loadTexts:cfmAlarmGroupFlowEntry.setStatus(_A)
_CfmAlarmGroupFlowSetId_Type=FlowSetIdentifier
_CfmAlarmGroupFlowSetId_Object=MibTableColumn
cfmAlarmGroupFlowSetId=_CfmAlarmGroupFlowSetId_Object((1,3,6,1,4,1,9,9,692,1,5,3,1,1),_CfmAlarmGroupFlowSetId_Type())
cfmAlarmGroupFlowSetId.setMaxAccess(_G)
if mibBuilder.loadTexts:cfmAlarmGroupFlowSetId.setStatus(_A)
_CfmAlarmGroupFlowMonitorId_Type=FlowMonitorIdentifier
_CfmAlarmGroupFlowMonitorId_Object=MibTableColumn
cfmAlarmGroupFlowMonitorId=_CfmAlarmGroupFlowMonitorId_Object((1,3,6,1,4,1,9,9,692,1,5,3,1,2),_CfmAlarmGroupFlowMonitorId_Type())
cfmAlarmGroupFlowMonitorId.setMaxAccess(_G)
if mibBuilder.loadTexts:cfmAlarmGroupFlowMonitorId.setStatus(_A)
_CfmAlarmGroupFlowId_Type=FlowIdentifier
_CfmAlarmGroupFlowId_Object=MibTableColumn
cfmAlarmGroupFlowId=_CfmAlarmGroupFlowId_Object((1,3,6,1,4,1,9,9,692,1,5,3,1,3),_CfmAlarmGroupFlowId_Type())
cfmAlarmGroupFlowId.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmGroupFlowId.setStatus(_A)
_CfmAlarmGroupFlowTableChanged_Type=TimeStamp
_CfmAlarmGroupFlowTableChanged_Object=MibScalar
cfmAlarmGroupFlowTableChanged=_CfmAlarmGroupFlowTableChanged_Object((1,3,6,1,4,1,9,9,692,1,5,4),_CfmAlarmGroupFlowTableChanged_Type())
cfmAlarmGroupFlowTableChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmGroupFlowTableChanged.setStatus(_A)
_CfmAlarmHistory_ObjectIdentity=ObjectIdentity
cfmAlarmHistory=_CfmAlarmHistory_ObjectIdentity((1,3,6,1,4,1,9,9,692,1,6))
class _CfmAlarmHistorySize_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CfmAlarmHistorySize_Type.__name__=_D
_CfmAlarmHistorySize_Object=MibScalar
cfmAlarmHistorySize=_CfmAlarmHistorySize_Object((1,3,6,1,4,1,9,9,692,1,6,1),_CfmAlarmHistorySize_Type())
cfmAlarmHistorySize.setMaxAccess(_M)
if mibBuilder.loadTexts:cfmAlarmHistorySize.setStatus(_A)
class _CfmAlarmHistoryLastId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CfmAlarmHistoryLastId_Type.__name__=_D
_CfmAlarmHistoryLastId_Object=MibScalar
cfmAlarmHistoryLastId=_CfmAlarmHistoryLastId_Object((1,3,6,1,4,1,9,9,692,1,6,2),_CfmAlarmHistoryLastId_Type())
cfmAlarmHistoryLastId.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmHistoryLastId.setStatus(_A)
_CfmAlarmHistoryTable_Object=MibTable
cfmAlarmHistoryTable=_CfmAlarmHistoryTable_Object((1,3,6,1,4,1,9,9,692,1,6,3))
if mibBuilder.loadTexts:cfmAlarmHistoryTable.setStatus(_A)
_CfmAlarmHistoryEntry_Object=MibTableRow
cfmAlarmHistoryEntry=_CfmAlarmHistoryEntry_Object((1,3,6,1,4,1,9,9,692,1,6,3,1))
cfmAlarmHistoryEntry.setIndexNames((0,_B,_h))
if mibBuilder.loadTexts:cfmAlarmHistoryEntry.setStatus(_A)
class _CfmAlarmHistoryId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CfmAlarmHistoryId_Type.__name__=_D
_CfmAlarmHistoryId_Object=MibTableColumn
cfmAlarmHistoryId=_CfmAlarmHistoryId_Object((1,3,6,1,4,1,9,9,692,1,6,3,1,1),_CfmAlarmHistoryId_Type())
cfmAlarmHistoryId.setMaxAccess(_G)
if mibBuilder.loadTexts:cfmAlarmHistoryId.setStatus(_A)
class _CfmAlarmHistoryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cleared',1),('raised',2)))
_CfmAlarmHistoryType_Type.__name__=_F
_CfmAlarmHistoryType_Object=MibTableColumn
cfmAlarmHistoryType=_CfmAlarmHistoryType_Object((1,3,6,1,4,1,9,9,692,1,6,3,1,2),_CfmAlarmHistoryType_Type())
cfmAlarmHistoryType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmHistoryType.setStatus(_A)
_CfmAlarmHistoryEntity_Type=RowPointer
_CfmAlarmHistoryEntity_Object=MibTableColumn
cfmAlarmHistoryEntity=_CfmAlarmHistoryEntity_Object((1,3,6,1,4,1,9,9,692,1,6,3,1,3),_CfmAlarmHistoryEntity_Type())
cfmAlarmHistoryEntity.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmHistoryEntity.setStatus(_A)
_CfmAlarmHistoryConditionsProfile_Type=FlowMonitorConditionsProfile
_CfmAlarmHistoryConditionsProfile_Object=MibTableColumn
cfmAlarmHistoryConditionsProfile=_CfmAlarmHistoryConditionsProfile_Object((1,3,6,1,4,1,9,9,692,1,6,3,1,4),_CfmAlarmHistoryConditionsProfile_Type())
cfmAlarmHistoryConditionsProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmHistoryConditionsProfile.setStatus(_A)
_CfmAlarmHistoryConditionId_Type=FlowMonitorConditionIdentifier
_CfmAlarmHistoryConditionId_Object=MibTableColumn
cfmAlarmHistoryConditionId=_CfmAlarmHistoryConditionId_Object((1,3,6,1,4,1,9,9,692,1,6,3,1,5),_CfmAlarmHistoryConditionId_Type())
cfmAlarmHistoryConditionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmHistoryConditionId.setStatus(_A)
_CfmAlarmHistorySeverity_Type=CiscoAlarmSeverity
_CfmAlarmHistorySeverity_Object=MibTableColumn
cfmAlarmHistorySeverity=_CfmAlarmHistorySeverity_Object((1,3,6,1,4,1,9,9,692,1,6,3,1,6),_CfmAlarmHistorySeverity_Type())
cfmAlarmHistorySeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmHistorySeverity.setStatus(_A)
_CfmAlarmHistoryTime_Type=TimeStamp
_CfmAlarmHistoryTime_Object=MibTableColumn
cfmAlarmHistoryTime=_CfmAlarmHistoryTime_Object((1,3,6,1,4,1,9,9,692,1,6,3,1,7),_CfmAlarmHistoryTime_Type())
cfmAlarmHistoryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmAlarmHistoryTime.setStatus(_A)
_CfmNotify_ObjectIdentity=ObjectIdentity
cfmNotify=_CfmNotify_ObjectIdentity((1,3,6,1,4,1,9,9,692,1,7))
_CfmNotifyEnable_Type=TruthValue
_CfmNotifyEnable_Object=MibScalar
cfmNotifyEnable=_CfmNotifyEnable_Object((1,3,6,1,4,1,9,9,692,1,7,1),_CfmNotifyEnable_Type())
cfmNotifyEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:cfmNotifyEnable.setStatus(_A)
_CiscoFlowMonitorMIBConform_ObjectIdentity=ObjectIdentity
ciscoFlowMonitorMIBConform=_CiscoFlowMonitorMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,692,2))
_CiscoFlowMonitorMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFlowMonitorMIBCompliances=_CiscoFlowMonitorMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,692,2,1))
_CiscoFlowMonitorMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFlowMonitorMIBGroups=_CiscoFlowMonitorMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,692,2,2))
_CiscoFlowMonitorMIBIds_ObjectIdentity=ObjectIdentity
ciscoFlowMonitorMIBIds=_CiscoFlowMonitorMIBIds_ObjectIdentity((1,3,6,1,4,1,9,9,692,3))
_CfmMonitoredElements_ObjectIdentity=ObjectIdentity
cfmMonitoredElements=_CfmMonitoredElements_ObjectIdentity((1,3,6,1,4,1,9,9,692,3,1))
_CfmeOther_ObjectIdentity=ObjectIdentity
cfmeOther=_CfmeOther_ObjectIdentity((1,3,6,1,4,1,9,9,692,3,1,1))
if mibBuilder.loadTexts:cfmeOther.setStatus(_A)
_CfmeFlowCount_ObjectIdentity=ObjectIdentity
cfmeFlowCount=_CfmeFlowCount_ObjectIdentity((1,3,6,1,4,1,9,9,692,3,1,2))
if mibBuilder.loadTexts:cfmeFlowCount.setStatus(_A)
_CfmeFlowTimeouts_ObjectIdentity=ObjectIdentity
cfmeFlowTimeouts=_CfmeFlowTimeouts_ObjectIdentity((1,3,6,1,4,1,9,9,692,3,1,3))
if mibBuilder.loadTexts:cfmeFlowTimeouts.setStatus(_A)
_CfmeFlowStop_ObjectIdentity=ObjectIdentity
cfmeFlowStop=_CfmeFlowStop_ObjectIdentity((1,3,6,1,4,1,9,9,692,3,1,4))
if mibBuilder.loadTexts:cfmeFlowStop.setStatus(_A)
_CfmeFlowCumulativeBitRate_ObjectIdentity=ObjectIdentity
cfmeFlowCumulativeBitRate=_CfmeFlowCumulativeBitRate_ObjectIdentity((1,3,6,1,4,1,9,9,692,3,1,5))
if mibBuilder.loadTexts:cfmeFlowCumulativeBitRate.setStatus(_A)
_CfmeFlowCumulativePktRate_ObjectIdentity=ObjectIdentity
cfmeFlowCumulativePktRate=_CfmeFlowCumulativePktRate_ObjectIdentity((1,3,6,1,4,1,9,9,692,3,1,6))
if mibBuilder.loadTexts:cfmeFlowCumulativePktRate.setStatus(_A)
_CfmeFlowBitRate_ObjectIdentity=ObjectIdentity
cfmeFlowBitRate=_CfmeFlowBitRate_ObjectIdentity((1,3,6,1,4,1,9,9,692,3,1,7))
if mibBuilder.loadTexts:cfmeFlowBitRate.setStatus(_A)
_CfmeFlowPktRate_ObjectIdentity=ObjectIdentity
cfmeFlowPktRate=_CfmeFlowPktRate_ObjectIdentity((1,3,6,1,4,1,9,9,692,3,1,8))
if mibBuilder.loadTexts:cfmeFlowPktRate.setStatus(_A)
cfmFlowMonitorGroup=ObjectGroup((1,3,6,1,4,1,9,9,692,2,2,1))
cfmFlowMonitorGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:cfmFlowMonitorGroup.setStatus(_A)
cfmFlowGroup=ObjectGroup((1,3,6,1,4,1,9,9,692,2,2,2))
cfmFlowGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:cfmFlowGroup.setStatus(_A)
cfmFlowMetricsGroup=ObjectGroup((1,3,6,1,4,1,9,9,692,2,2,3))
cfmFlowMetricsGroup.setObjects(*((_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw)))
if mibBuilder.loadTexts:cfmFlowMetricsGroup.setStatus(_A)
cfmFlowConditionsGroup=ObjectGroup((1,3,6,1,4,1,9,9,692,2,2,4))
cfmFlowConditionsGroup.setObjects(*((_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB)))
if mibBuilder.loadTexts:cfmFlowConditionsGroup.setStatus(_A)
cfmAlarmAggregationGroup=ObjectGroup((1,3,6,1,4,1,9,9,692,2,2,5))
cfmAlarmAggregationGroup.setObjects(*((_B,_BC),(_B,_BD),(_B,_BE),(_B,_BF),(_B,_BG),(_B,_BH),(_B,_BI),(_B,_BJ),(_B,_BK),(_B,_BL),(_B,_P),(_B,_BM)))
if mibBuilder.loadTexts:cfmAlarmAggregationGroup.setStatus(_A)
cfmAlarmHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,692,2,2,6))
cfmAlarmHistoryGroup.setObjects(*((_B,_BN),(_B,_BO),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:cfmAlarmHistoryGroup.setStatus(_A)
cfmNotifySupportGroup=ObjectGroup((1,3,6,1,4,1,9,9,692,2,2,7))
cfmNotifySupportGroup.setObjects((_B,_BP))
if mibBuilder.loadTexts:cfmNotifySupportGroup.setStatus(_A)
cfmNotifyAlarm=NotificationType((1,3,6,1,4,1,9,9,692,0,1))
cfmNotifyAlarm.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:cfmNotifyAlarm.setStatus(_A)
cfmNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,9,692,2,2,8))
cfmNotifyGroup.setObjects((_B,_BQ))
if mibBuilder.loadTexts:cfmNotifyGroup.setStatus(_A)
ciscoFlowMonitorCompliance01=ModuleCompliance((1,3,6,1,4,1,9,9,692,2,1,1))
ciscoFlowMonitorCompliance01.setObjects(*((_B,_BR),(_B,_BS),(_B,_BT),(_B,_BU),(_B,_BV),(_B,_BW),(_B,_BX),(_B,_BY)))
if mibBuilder.loadTexts:ciscoFlowMonitorCompliance01.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoFlowMonitorMIB':ciscoFlowMonitorMIB,'ciscoFlowMonitorMIBNotifs':ciscoFlowMonitorMIBNotifs,_BQ:cfmNotifyAlarm,'ciscoFlowMonitorMIBObjects':ciscoFlowMonitorMIBObjects,'cfmFlowMonitors':cfmFlowMonitors,'cfmFlowMonitorTable':cfmFlowMonitorTable,'cfmFlowMonitorEntry':cfmFlowMonitorEntry,_E:cfmFlowMonitorId,_i:cfmFlowMonitorDescr,_j:cfmFlowMonitorCaps,_k:cfmFlowMonitorFlowCount,_l:cfmFlowMonitorConditionsProfile,_m:cfmFlowMonitorConditions,_n:cfmFlowMonitorAlarms,_o:cfmFlowMonitorAlarmSeverity,_p:cfmFlowMonitorAlarmCriticalCount,_q:cfmFlowMonitorAlarmMajorCount,_r:cfmFlowMonitorAlarmMinorCount,_s:cfmFlowMonitorAlarmWarningCount,_t:cfmFlowMonitorAlarmInfoCount,_u:cfmFlowMonitorTableChanged,'cfmFlows':cfmFlows,'cfmFlowTable':cfmFlowTable,'cfmFlowEntry':cfmFlowEntry,_H:cfmFlowId,_v:cfmFlowDescr,_w:cfmFlowNext,_x:cfmFlowCreateTime,_y:cfmFlowDiscontinuityTime,_z:cfmFlowExpirationTime,_A0:cfmFlowDirection,_A1:cfmFlowAdminStatus,_A2:cfmFlowOperStatus,_A3:cfmFlowIngressType,_A4:cfmFlowIngress,_A5:cfmFlowEgressType,_A6:cfmFlowEgress,_A7:cfmFlowTableChanged,'cfmFlowL2VlanTable':cfmFlowL2VlanTable,'cfmFlowL2VlanEntry':cfmFlowL2VlanEntry,_A8:cfmFlowL2VlanNext,_A9:cfmFlowL2VlanId,_AA:cfmFlowL2VlanCos,_AB:cfmFlowL2VlanTableChanged,'cfmFlowIpTable':cfmFlowIpTable,'cfmFlowIpEntry':cfmFlowIpEntry,_AC:cfmFlowIpNext,_AD:cfmFlowIpAddrType,_AE:cfmFlowIpAddrSrc,_AF:cfmFlowIpAddrDst,_AG:cfmFlowIpValid,_AH:cfmFlowIpTrafficClass,_AI:cfmFlowIpHopLimit,_AJ:cfmFlowIpTableChanged,'cfmFlowUdpTable':cfmFlowUdpTable,'cfmFlowUdpEntry':cfmFlowUdpEntry,_AK:cfmFlowUdpNext,_AL:cfmFlowUdpPortSrc,_AM:cfmFlowUdpPortDst,_AN:cfmFlowUdpTableChanged,'cfmFlowTcpTable':cfmFlowTcpTable,'cfmFlowTcpEntry':cfmFlowTcpEntry,_AO:cfmFlowTcpNext,_AP:cfmFlowTcpPortSrc,_AQ:cfmFlowTcpPortDst,_AR:cfmFlowTcpTableChanged,'cfmFlowRtpTable':cfmFlowRtpTable,'cfmFlowRtpEntry':cfmFlowRtpEntry,_AS:cfmFlowRtpNext,_AT:cfmFlowRtpVersion,_AU:cfmFlowRtpSsrc,_AV:cfmFlowRtpPayloadType,_AW:cfmFlowRtpTableChanged,'cfmFlowMetrics':cfmFlowMetrics,'cfmFlowMetricsTable':cfmFlowMetricsTable,'cfmFlowMetricsEntry':cfmFlowMetricsEntry,_AX:cfmFlowMetricsCollected,_AY:cfmFlowMetricsIntervalTime,_AZ:cfmFlowMetricsMaxIntervals,_Aa:cfmFlowMetricsElapsedTime,_Ab:cfmFlowMetricsIntervals,_Ac:cfmFlowMetricsInvalidIntervals,_Ad:cfmFlowMetricsConditionsProfile,_Ae:cfmFlowMetricsConditions,_Af:cfmFlowMetricsAlarms,_Ag:cfmFlowMetricsAlarmSeverity,_Ah:cfmFlowMetricsPkts,_Ai:cfmFlowMetricsOctets,_Aj:cfmFlowMetricsBitRateUnits,_Ak:cfmFlowMetricsBitRate,_Al:cfmFlowMetricsPktRate,_Am:cfmFlowMetricsTableChanged,'cfmFlowMetricsIntTable':cfmFlowMetricsIntTable,'cfmFlowMetricsIntEntry':cfmFlowMetricsIntEntry,_b:cfmFlowMetricsIntNumber,_An:cfmFlowMetricsIntValid,_Ao:cfmFlowMetricsIntTime,_Ap:cfmFlowMetricsIntConditions,_Aq:cfmFlowMetricsIntAlarms,_Ar:cfmFlowMetricsIntAlarmSeverity,_As:cfmFlowMetricsIntPkts,_At:cfmFlowMetricsIntOctets,_Au:cfmFlowMetricsIntBitRateUnits,_Av:cfmFlowMetricsIntBitRate,_Aw:cfmFlowMetricsIntPktRate,'cfmConditions':cfmConditions,'cfmConditionTable':cfmConditionTable,'cfmConditionEntry':cfmConditionEntry,_c:cfmConditionProfile,_d:cfmConditionId,_Ax:cfmConditionDescr,_Ay:cfmConditionMonitoredElement,_Az:cfmConditionType,_A_:cfmConditionThreshRiseScale,_B0:cfmConditionThreshRisePrecision,_B1:cfmConditionThreshRise,_B2:cfmConditionThreshFallScale,_B3:cfmConditionThreshFallPrecision,_B4:cfmConditionThreshFall,_B5:cfmConditionSampleType,_B6:cfmConditionSampleWindow,_B7:cfmConditionAlarm,_B8:cfmConditionAlarmActions,_B9:cfmConditionAlarmSeverity,_BA:cfmConditionAlarmGroup,_BB:cfmConditionTableChanged,'cfmAlarmGroups':cfmAlarmGroups,'cfmAlarmGroupTable':cfmAlarmGroupTable,'cfmAlarmGroupEntry':cfmAlarmGroupEntry,_e:cfmAlarmGroupId,_BC:cfmAlarmGroupDescr,_BD:cfmAlarmGroupConditionsProfile,_BE:cfmAlarmGroupConditionId,_BF:cfmAlarmGroupFlowSet,_BG:cfmAlarmGroupFlowCount,_BH:cfmAlarmGroupThresholdUnits,_BI:cfmAlarmGroupThreshold,_BJ:cfmAlarmGroupRaised,_BK:cfmAlarmGroupCurrentCount,_BL:cfmAlarmGroupTableChanged,'cfmAlarmGroupFlowTable':cfmAlarmGroupFlowTable,'cfmAlarmGroupFlowEntry':cfmAlarmGroupFlowEntry,_f:cfmAlarmGroupFlowSetId,_g:cfmAlarmGroupFlowMonitorId,_P:cfmAlarmGroupFlowId,_BM:cfmAlarmGroupFlowTableChanged,'cfmAlarmHistory':cfmAlarmHistory,_BN:cfmAlarmHistorySize,_BO:cfmAlarmHistoryLastId,'cfmAlarmHistoryTable':cfmAlarmHistoryTable,'cfmAlarmHistoryEntry':cfmAlarmHistoryEntry,_h:cfmAlarmHistoryId,_Q:cfmAlarmHistoryType,_R:cfmAlarmHistoryEntity,_S:cfmAlarmHistoryConditionsProfile,_T:cfmAlarmHistoryConditionId,_U:cfmAlarmHistorySeverity,_V:cfmAlarmHistoryTime,'cfmNotify':cfmNotify,_BP:cfmNotifyEnable,'ciscoFlowMonitorMIBConform':ciscoFlowMonitorMIBConform,'ciscoFlowMonitorMIBCompliances':ciscoFlowMonitorMIBCompliances,'ciscoFlowMonitorCompliance01':ciscoFlowMonitorCompliance01,'ciscoFlowMonitorMIBGroups':ciscoFlowMonitorMIBGroups,_BR:cfmFlowMonitorGroup,_BS:cfmFlowGroup,_BT:cfmFlowMetricsGroup,_BU:cfmFlowConditionsGroup,_BV:cfmAlarmAggregationGroup,_BW:cfmAlarmHistoryGroup,_BX:cfmNotifySupportGroup,_BY:cfmNotifyGroup,'ciscoFlowMonitorMIBIds':ciscoFlowMonitorMIBIds,'cfmMonitoredElements':cfmMonitoredElements,'cfmeOther':cfmeOther,'cfmeFlowCount':cfmeFlowCount,'cfmeFlowTimeouts':cfmeFlowTimeouts,'cfmeFlowStop':cfmeFlowStop,'cfmeFlowCumulativeBitRate':cfmeFlowCumulativeBitRate,'cfmeFlowCumulativePktRate':cfmeFlowCumulativePktRate,'cfmeFlowBitRate':cfmeFlowBitRate,'cfmeFlowPktRate':cfmeFlowPktRate})