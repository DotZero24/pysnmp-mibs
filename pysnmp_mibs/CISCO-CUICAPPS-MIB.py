_Al='cuicEnvInfoGroup'
_Ak='cuicThreadPoolInfoGroup'
_Aj='ciscoCuicappsMIBEventGroup'
_Ai='cuicNotificationInfoGroup'
_Ah='cuicSecurityTableGroup'
_Ag='cuicDatasourceInfoTableGroup'
_Af='cuicClusterInfoTableGroup'
_Ae='cuicDbInfoTableGroup'
_Ad='cuicReportSchedulerTableGroup'
_Ac='cuicReportingTableGroup'
_Ab='cuicLicenseInfoTableGroup'
_Aa='cuicGeneralInfoTableGroup'
_AZ='ciscoCuicappsMIBEvent'
_AY='cuicTomcatThreadsMax'
_AX='cuicTomcatThreadsTotal'
_AW='cuicTomcatThreadsBusy'
_AV='cuicJvmMemoryMax'
_AU='cuicJvmMemoryTotal'
_AT='cuicJvmMemoryFree'
_AS='cuicJvmPercentCPUTime'
_AR='cuicWaSessionsActive'
_AQ='cuicWaErrors'
_AP='cuicQueuedTasksMax'
_AO='cuicQueuedTasks'
_AN='cuicThreadsRunning'
_AM='cuicThreadsMaxAvailable'
_AL='cuicSecurityGroupsConfigured'
_AK='cuicSecurityLoginFailedAttempts'
_AJ='cuicSecurityUsersLoggedIn'
_AI='cuicSecurityUsersConfigured'
_AH='cuicDatasourceType'
_AG='cuicDatasourceHost'
_AF='cuicDatasourceStatus'
_AE='cuicDatasourceName'
_AD='cuicClusterFirstNodeName'
_AC='cuicClusterServerCount'
_AB='cuicClusterName'
_AA='cuicDbInfoSpaceUsed'
_A9='cuicDbInfoTmpSpaceUsed'
_A8='cuicDbInfoReplicationStatus'
_A7='cuicDbInfoStatus'
_A6='cuicSchedulerJobsFailedCount'
_A5='cuicSchedulerJobsRunningCount'
_A4='cuicSchedulerJobsCompletedCount'
_A3='cuicSchedulerEmailServerStatus'
_A2='cuicSchedulerStatus'
_A1='cuicReportingRealTimeReportWaiting'
_A0='cuicReportingTotalKickedOffRealTimeReports'
_z='cuicReportingRealTimeReportRunning'
_y='cuicReportingTotalKickedOffHistoricalReports'
_x='cuicReportingHistoricalReportWaiting'
_w='cuicReportingHistoricalReportRunning'
_v='cuicReportingRealTimeReportDefinitionCount'
_u='cuicReportingHistoricalReportDefinitionCount'
_t='cuicReportingEngineStatus'
_s='cuicReportingDataSourceCount'
_r='cuicLicenseInfoHost'
_q='cuicLicenseInfoExpirationTime'
_p='cuicLicenseInfoStartTime'
_o='cuicLicenseInfoType'
_n='cuicGeneralInfoEnableNotifications'
_m='cuicGeneralInfoOpsConsoleURL'
_l='cuicGeneralInfoSystemStatus'
_k='cuicGeneralInfoTimeZoneName'
_j='cuicGeneralInfoStartTime'
_i='cuicGeneralInfoVersion'
_h='cuicGeneralInfoServerDescription'
_g='cuicGeneralInfoServerName'
_f='cuicSecurityIndex'
_e='cuicDatasourceIndex'
_d='cuicClusterIndex'
_c='cuicDbInfoIndex'
_b='cuicSchedulerIndex'
_a='report definitions'
_Z='cuicReportingIndex'
_Y='cuicLicenseInfoIndex'
_X='cuicGeneralInfoIndex'
_W='TruthValue'
_V='Unsigned32'
_U='cuicEventText'
_T='cuicEventTimestamp'
_S='cuicEventSeverity'
_R='cuicEventState'
_Q='cuicEventName'
_P='cuicEventAppName'
_O='cuicEventHostName'
_N='cuicEventId'
_M='kilo bytes'
_L='percent'
_K='jobs'
_J='unknown'
_I='Gauge32'
_H='threads'
_G='reports'
_F='Integer32'
_E='accessible-for-notify'
_D='not-accessible'
_C='read-only'
_B='CISCO-CUICAPPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoURLString,=mibBuilder.importSymbols('CISCO-TC','CiscoURLString')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_I,_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_V,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_W)
ciscoCuicappsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,718))
if mibBuilder.loadTexts:ciscoCuicappsMIB.setRevisions(('2010-01-23 00:00',))
class CuicServiceStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inService',1),('partialService',2),('notResponding',3),(_J,4)))
class CuicSubsystemId(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoCuicappsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCuicappsMIBNotifs=_CiscoCuicappsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,718,0))
_CiscoCuicappsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCuicappsMIBObjects=_CiscoCuicappsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,718,1))
_CuicGeneralInfoTable_Object=MibTable
cuicGeneralInfoTable=_CuicGeneralInfoTable_Object((1,3,6,1,4,1,9,9,718,1,1))
if mibBuilder.loadTexts:cuicGeneralInfoTable.setStatus(_A)
_CuicGeneralInfoEntry_Object=MibTableRow
cuicGeneralInfoEntry=_CuicGeneralInfoEntry_Object((1,3,6,1,4,1,9,9,718,1,1,1))
cuicGeneralInfoEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:cuicGeneralInfoEntry.setStatus(_A)
_CuicGeneralInfoIndex_Type=CuicSubsystemId
_CuicGeneralInfoIndex_Object=MibTableColumn
cuicGeneralInfoIndex=_CuicGeneralInfoIndex_Object((1,3,6,1,4,1,9,9,718,1,1,1,1),_CuicGeneralInfoIndex_Type())
cuicGeneralInfoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cuicGeneralInfoIndex.setStatus(_A)
_CuicGeneralInfoServerName_Type=SnmpAdminString
_CuicGeneralInfoServerName_Object=MibTableColumn
cuicGeneralInfoServerName=_CuicGeneralInfoServerName_Object((1,3,6,1,4,1,9,9,718,1,1,1,2),_CuicGeneralInfoServerName_Type())
cuicGeneralInfoServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicGeneralInfoServerName.setStatus(_A)
_CuicGeneralInfoServerDescription_Type=SnmpAdminString
_CuicGeneralInfoServerDescription_Object=MibTableColumn
cuicGeneralInfoServerDescription=_CuicGeneralInfoServerDescription_Object((1,3,6,1,4,1,9,9,718,1,1,1,3),_CuicGeneralInfoServerDescription_Type())
cuicGeneralInfoServerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicGeneralInfoServerDescription.setStatus(_A)
_CuicGeneralInfoVersion_Type=SnmpAdminString
_CuicGeneralInfoVersion_Object=MibTableColumn
cuicGeneralInfoVersion=_CuicGeneralInfoVersion_Object((1,3,6,1,4,1,9,9,718,1,1,1,4),_CuicGeneralInfoVersion_Type())
cuicGeneralInfoVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicGeneralInfoVersion.setStatus(_A)
_CuicGeneralInfoStartTime_Type=DateAndTime
_CuicGeneralInfoStartTime_Object=MibTableColumn
cuicGeneralInfoStartTime=_CuicGeneralInfoStartTime_Object((1,3,6,1,4,1,9,9,718,1,1,1,5),_CuicGeneralInfoStartTime_Type())
cuicGeneralInfoStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicGeneralInfoStartTime.setStatus(_A)
_CuicGeneralInfoTimeZoneName_Type=SnmpAdminString
_CuicGeneralInfoTimeZoneName_Object=MibTableColumn
cuicGeneralInfoTimeZoneName=_CuicGeneralInfoTimeZoneName_Object((1,3,6,1,4,1,9,9,718,1,1,1,6),_CuicGeneralInfoTimeZoneName_Type())
cuicGeneralInfoTimeZoneName.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicGeneralInfoTimeZoneName.setStatus(_A)
_CuicGeneralInfoSystemStatus_Type=CuicServiceStatus
_CuicGeneralInfoSystemStatus_Object=MibTableColumn
cuicGeneralInfoSystemStatus=_CuicGeneralInfoSystemStatus_Object((1,3,6,1,4,1,9,9,718,1,1,1,7),_CuicGeneralInfoSystemStatus_Type())
cuicGeneralInfoSystemStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicGeneralInfoSystemStatus.setStatus(_A)
_CuicGeneralInfoOpsConsoleURL_Type=CiscoURLString
_CuicGeneralInfoOpsConsoleURL_Object=MibTableColumn
cuicGeneralInfoOpsConsoleURL=_CuicGeneralInfoOpsConsoleURL_Object((1,3,6,1,4,1,9,9,718,1,1,1,8),_CuicGeneralInfoOpsConsoleURL_Type())
cuicGeneralInfoOpsConsoleURL.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicGeneralInfoOpsConsoleURL.setStatus(_A)
class _CuicGeneralInfoEnableNotifications_Type(TruthValue):defaultValue=1
_CuicGeneralInfoEnableNotifications_Type.__name__=_W
_CuicGeneralInfoEnableNotifications_Object=MibTableColumn
cuicGeneralInfoEnableNotifications=_CuicGeneralInfoEnableNotifications_Object((1,3,6,1,4,1,9,9,718,1,1,1,9),_CuicGeneralInfoEnableNotifications_Type())
cuicGeneralInfoEnableNotifications.setMaxAccess('read-write')
if mibBuilder.loadTexts:cuicGeneralInfoEnableNotifications.setStatus(_A)
_CuicLicenseInfoTable_Object=MibTable
cuicLicenseInfoTable=_CuicLicenseInfoTable_Object((1,3,6,1,4,1,9,9,718,1,2))
if mibBuilder.loadTexts:cuicLicenseInfoTable.setStatus(_A)
_CuicLicenseInfoEntry_Object=MibTableRow
cuicLicenseInfoEntry=_CuicLicenseInfoEntry_Object((1,3,6,1,4,1,9,9,718,1,2,1))
cuicLicenseInfoEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:cuicLicenseInfoEntry.setStatus(_A)
_CuicLicenseInfoIndex_Type=CuicSubsystemId
_CuicLicenseInfoIndex_Object=MibTableColumn
cuicLicenseInfoIndex=_CuicLicenseInfoIndex_Object((1,3,6,1,4,1,9,9,718,1,2,1,1),_CuicLicenseInfoIndex_Type())
cuicLicenseInfoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cuicLicenseInfoIndex.setStatus(_A)
class _CuicLicenseInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('trial',2),('standard',3),('premium',4)))
_CuicLicenseInfoType_Type.__name__=_F
_CuicLicenseInfoType_Object=MibTableColumn
cuicLicenseInfoType=_CuicLicenseInfoType_Object((1,3,6,1,4,1,9,9,718,1,2,1,2),_CuicLicenseInfoType_Type())
cuicLicenseInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicLicenseInfoType.setStatus(_A)
_CuicLicenseInfoStartTime_Type=DateAndTime
_CuicLicenseInfoStartTime_Object=MibTableColumn
cuicLicenseInfoStartTime=_CuicLicenseInfoStartTime_Object((1,3,6,1,4,1,9,9,718,1,2,1,3),_CuicLicenseInfoStartTime_Type())
cuicLicenseInfoStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicLicenseInfoStartTime.setStatus(_A)
_CuicLicenseInfoExpirationTime_Type=DateAndTime
_CuicLicenseInfoExpirationTime_Object=MibTableColumn
cuicLicenseInfoExpirationTime=_CuicLicenseInfoExpirationTime_Object((1,3,6,1,4,1,9,9,718,1,2,1,4),_CuicLicenseInfoExpirationTime_Type())
cuicLicenseInfoExpirationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicLicenseInfoExpirationTime.setStatus(_A)
_CuicLicenseInfoHost_Type=SnmpAdminString
_CuicLicenseInfoHost_Object=MibTableColumn
cuicLicenseInfoHost=_CuicLicenseInfoHost_Object((1,3,6,1,4,1,9,9,718,1,2,1,5),_CuicLicenseInfoHost_Type())
cuicLicenseInfoHost.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicLicenseInfoHost.setStatus(_A)
_CuicReportingTable_Object=MibTable
cuicReportingTable=_CuicReportingTable_Object((1,3,6,1,4,1,9,9,718,1,3))
if mibBuilder.loadTexts:cuicReportingTable.setStatus(_A)
_CuicReportingEntry_Object=MibTableRow
cuicReportingEntry=_CuicReportingEntry_Object((1,3,6,1,4,1,9,9,718,1,3,1))
cuicReportingEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:cuicReportingEntry.setStatus(_A)
_CuicReportingIndex_Type=CuicSubsystemId
_CuicReportingIndex_Object=MibTableColumn
cuicReportingIndex=_CuicReportingIndex_Object((1,3,6,1,4,1,9,9,718,1,3,1,1),_CuicReportingIndex_Type())
cuicReportingIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cuicReportingIndex.setStatus(_A)
_CuicReportingDataSourceCount_Type=Gauge32
_CuicReportingDataSourceCount_Object=MibTableColumn
cuicReportingDataSourceCount=_CuicReportingDataSourceCount_Object((1,3,6,1,4,1,9,9,718,1,3,1,2),_CuicReportingDataSourceCount_Type())
cuicReportingDataSourceCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicReportingDataSourceCount.setStatus(_A)
if mibBuilder.loadTexts:cuicReportingDataSourceCount.setUnits('data sources')
_CuicReportingEngineStatus_Type=CuicServiceStatus
_CuicReportingEngineStatus_Object=MibTableColumn
cuicReportingEngineStatus=_CuicReportingEngineStatus_Object((1,3,6,1,4,1,9,9,718,1,3,1,3),_CuicReportingEngineStatus_Type())
cuicReportingEngineStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicReportingEngineStatus.setStatus(_A)
_CuicReportingHistoricalReportDefinitionCount_Type=Gauge32
_CuicReportingHistoricalReportDefinitionCount_Object=MibTableColumn
cuicReportingHistoricalReportDefinitionCount=_CuicReportingHistoricalReportDefinitionCount_Object((1,3,6,1,4,1,9,9,718,1,3,1,4),_CuicReportingHistoricalReportDefinitionCount_Type())
cuicReportingHistoricalReportDefinitionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicReportingHistoricalReportDefinitionCount.setStatus(_A)
if mibBuilder.loadTexts:cuicReportingHistoricalReportDefinitionCount.setUnits(_a)
_CuicReportingRealTimeReportDefinitionCount_Type=Gauge32
_CuicReportingRealTimeReportDefinitionCount_Object=MibTableColumn
cuicReportingRealTimeReportDefinitionCount=_CuicReportingRealTimeReportDefinitionCount_Object((1,3,6,1,4,1,9,9,718,1,3,1,5),_CuicReportingRealTimeReportDefinitionCount_Type())
cuicReportingRealTimeReportDefinitionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicReportingRealTimeReportDefinitionCount.setStatus(_A)
if mibBuilder.loadTexts:cuicReportingRealTimeReportDefinitionCount.setUnits(_a)
_CuicReportingHistoricalReportRunning_Type=Gauge32
_CuicReportingHistoricalReportRunning_Object=MibTableColumn
cuicReportingHistoricalReportRunning=_CuicReportingHistoricalReportRunning_Object((1,3,6,1,4,1,9,9,718,1,3,1,6),_CuicReportingHistoricalReportRunning_Type())
cuicReportingHistoricalReportRunning.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicReportingHistoricalReportRunning.setStatus(_A)
if mibBuilder.loadTexts:cuicReportingHistoricalReportRunning.setUnits(_G)
_CuicReportingHistoricalReportWaiting_Type=Gauge32
_CuicReportingHistoricalReportWaiting_Object=MibTableColumn
cuicReportingHistoricalReportWaiting=_CuicReportingHistoricalReportWaiting_Object((1,3,6,1,4,1,9,9,718,1,3,1,7),_CuicReportingHistoricalReportWaiting_Type())
cuicReportingHistoricalReportWaiting.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicReportingHistoricalReportWaiting.setStatus(_A)
if mibBuilder.loadTexts:cuicReportingHistoricalReportWaiting.setUnits(_G)
_CuicReportingTotalKickedOffHistoricalReports_Type=Counter32
_CuicReportingTotalKickedOffHistoricalReports_Object=MibTableColumn
cuicReportingTotalKickedOffHistoricalReports=_CuicReportingTotalKickedOffHistoricalReports_Object((1,3,6,1,4,1,9,9,718,1,3,1,8),_CuicReportingTotalKickedOffHistoricalReports_Type())
cuicReportingTotalKickedOffHistoricalReports.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicReportingTotalKickedOffHistoricalReports.setStatus(_A)
if mibBuilder.loadTexts:cuicReportingTotalKickedOffHistoricalReports.setUnits(_G)
_CuicReportingRealTimeReportRunning_Type=Gauge32
_CuicReportingRealTimeReportRunning_Object=MibTableColumn
cuicReportingRealTimeReportRunning=_CuicReportingRealTimeReportRunning_Object((1,3,6,1,4,1,9,9,718,1,3,1,9),_CuicReportingRealTimeReportRunning_Type())
cuicReportingRealTimeReportRunning.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicReportingRealTimeReportRunning.setStatus(_A)
if mibBuilder.loadTexts:cuicReportingRealTimeReportRunning.setUnits(_G)
_CuicReportingTotalKickedOffRealTimeReports_Type=Counter32
_CuicReportingTotalKickedOffRealTimeReports_Object=MibTableColumn
cuicReportingTotalKickedOffRealTimeReports=_CuicReportingTotalKickedOffRealTimeReports_Object((1,3,6,1,4,1,9,9,718,1,3,1,10),_CuicReportingTotalKickedOffRealTimeReports_Type())
cuicReportingTotalKickedOffRealTimeReports.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicReportingTotalKickedOffRealTimeReports.setStatus(_A)
if mibBuilder.loadTexts:cuicReportingTotalKickedOffRealTimeReports.setUnits(_G)
_CuicReportingRealTimeReportWaiting_Type=Gauge32
_CuicReportingRealTimeReportWaiting_Object=MibTableColumn
cuicReportingRealTimeReportWaiting=_CuicReportingRealTimeReportWaiting_Object((1,3,6,1,4,1,9,9,718,1,3,1,11),_CuicReportingRealTimeReportWaiting_Type())
cuicReportingRealTimeReportWaiting.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicReportingRealTimeReportWaiting.setStatus(_A)
if mibBuilder.loadTexts:cuicReportingRealTimeReportWaiting.setUnits(_G)
_CuicSchedulerTable_Object=MibTable
cuicSchedulerTable=_CuicSchedulerTable_Object((1,3,6,1,4,1,9,9,718,1,4))
if mibBuilder.loadTexts:cuicSchedulerTable.setStatus(_A)
_CuicSchedulerEntry_Object=MibTableRow
cuicSchedulerEntry=_CuicSchedulerEntry_Object((1,3,6,1,4,1,9,9,718,1,4,1))
cuicSchedulerEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:cuicSchedulerEntry.setStatus(_A)
_CuicSchedulerIndex_Type=CuicSubsystemId
_CuicSchedulerIndex_Object=MibTableColumn
cuicSchedulerIndex=_CuicSchedulerIndex_Object((1,3,6,1,4,1,9,9,718,1,4,1,1),_CuicSchedulerIndex_Type())
cuicSchedulerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cuicSchedulerIndex.setStatus(_A)
_CuicSchedulerStatus_Type=CuicServiceStatus
_CuicSchedulerStatus_Object=MibTableColumn
cuicSchedulerStatus=_CuicSchedulerStatus_Object((1,3,6,1,4,1,9,9,718,1,4,1,2),_CuicSchedulerStatus_Type())
cuicSchedulerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicSchedulerStatus.setStatus(_A)
_CuicSchedulerEmailServerStatus_Type=CuicServiceStatus
_CuicSchedulerEmailServerStatus_Object=MibTableColumn
cuicSchedulerEmailServerStatus=_CuicSchedulerEmailServerStatus_Object((1,3,6,1,4,1,9,9,718,1,4,1,3),_CuicSchedulerEmailServerStatus_Type())
cuicSchedulerEmailServerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicSchedulerEmailServerStatus.setStatus(_A)
_CuicSchedulerJobsCompletedCount_Type=Counter32
_CuicSchedulerJobsCompletedCount_Object=MibTableColumn
cuicSchedulerJobsCompletedCount=_CuicSchedulerJobsCompletedCount_Object((1,3,6,1,4,1,9,9,718,1,4,1,4),_CuicSchedulerJobsCompletedCount_Type())
cuicSchedulerJobsCompletedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicSchedulerJobsCompletedCount.setStatus(_A)
if mibBuilder.loadTexts:cuicSchedulerJobsCompletedCount.setUnits(_K)
_CuicSchedulerJobsRunningCount_Type=Gauge32
_CuicSchedulerJobsRunningCount_Object=MibTableColumn
cuicSchedulerJobsRunningCount=_CuicSchedulerJobsRunningCount_Object((1,3,6,1,4,1,9,9,718,1,4,1,5),_CuicSchedulerJobsRunningCount_Type())
cuicSchedulerJobsRunningCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicSchedulerJobsRunningCount.setStatus(_A)
if mibBuilder.loadTexts:cuicSchedulerJobsRunningCount.setUnits(_K)
_CuicSchedulerJobsFailedCount_Type=Counter32
_CuicSchedulerJobsFailedCount_Object=MibTableColumn
cuicSchedulerJobsFailedCount=_CuicSchedulerJobsFailedCount_Object((1,3,6,1,4,1,9,9,718,1,4,1,6),_CuicSchedulerJobsFailedCount_Type())
cuicSchedulerJobsFailedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicSchedulerJobsFailedCount.setStatus(_A)
if mibBuilder.loadTexts:cuicSchedulerJobsFailedCount.setUnits(_K)
_CuicDbInfoTable_Object=MibTable
cuicDbInfoTable=_CuicDbInfoTable_Object((1,3,6,1,4,1,9,9,718,1,5))
if mibBuilder.loadTexts:cuicDbInfoTable.setStatus(_A)
_CuicDbInfoEntry_Object=MibTableRow
cuicDbInfoEntry=_CuicDbInfoEntry_Object((1,3,6,1,4,1,9,9,718,1,5,1))
cuicDbInfoEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:cuicDbInfoEntry.setStatus(_A)
_CuicDbInfoIndex_Type=CuicSubsystemId
_CuicDbInfoIndex_Object=MibTableColumn
cuicDbInfoIndex=_CuicDbInfoIndex_Object((1,3,6,1,4,1,9,9,718,1,5,1,1),_CuicDbInfoIndex_Type())
cuicDbInfoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cuicDbInfoIndex.setStatus(_A)
_CuicDbInfoStatus_Type=CuicServiceStatus
_CuicDbInfoStatus_Object=MibTableColumn
cuicDbInfoStatus=_CuicDbInfoStatus_Object((1,3,6,1,4,1,9,9,718,1,5,1,2),_CuicDbInfoStatus_Type())
cuicDbInfoStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicDbInfoStatus.setStatus(_A)
_CuicDbInfoReplicationStatus_Type=CuicServiceStatus
_CuicDbInfoReplicationStatus_Object=MibTableColumn
cuicDbInfoReplicationStatus=_CuicDbInfoReplicationStatus_Object((1,3,6,1,4,1,9,9,718,1,5,1,3),_CuicDbInfoReplicationStatus_Type())
cuicDbInfoReplicationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicDbInfoReplicationStatus.setStatus(_A)
class _CuicDbInfoTmpSpaceUsed_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CuicDbInfoTmpSpaceUsed_Type.__name__=_I
_CuicDbInfoTmpSpaceUsed_Object=MibTableColumn
cuicDbInfoTmpSpaceUsed=_CuicDbInfoTmpSpaceUsed_Object((1,3,6,1,4,1,9,9,718,1,5,1,4),_CuicDbInfoTmpSpaceUsed_Type())
cuicDbInfoTmpSpaceUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicDbInfoTmpSpaceUsed.setStatus(_A)
if mibBuilder.loadTexts:cuicDbInfoTmpSpaceUsed.setUnits(_L)
class _CuicDbInfoSpaceUsed_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CuicDbInfoSpaceUsed_Type.__name__=_I
_CuicDbInfoSpaceUsed_Object=MibTableColumn
cuicDbInfoSpaceUsed=_CuicDbInfoSpaceUsed_Object((1,3,6,1,4,1,9,9,718,1,5,1,5),_CuicDbInfoSpaceUsed_Type())
cuicDbInfoSpaceUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicDbInfoSpaceUsed.setStatus(_A)
if mibBuilder.loadTexts:cuicDbInfoSpaceUsed.setUnits(_L)
_CuicClusterTable_Object=MibTable
cuicClusterTable=_CuicClusterTable_Object((1,3,6,1,4,1,9,9,718,1,6))
if mibBuilder.loadTexts:cuicClusterTable.setStatus(_A)
_CuicClusterEntry_Object=MibTableRow
cuicClusterEntry=_CuicClusterEntry_Object((1,3,6,1,4,1,9,9,718,1,6,1))
cuicClusterEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:cuicClusterEntry.setStatus(_A)
_CuicClusterIndex_Type=CuicSubsystemId
_CuicClusterIndex_Object=MibTableColumn
cuicClusterIndex=_CuicClusterIndex_Object((1,3,6,1,4,1,9,9,718,1,6,1,1),_CuicClusterIndex_Type())
cuicClusterIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cuicClusterIndex.setStatus(_A)
_CuicClusterName_Type=SnmpAdminString
_CuicClusterName_Object=MibTableColumn
cuicClusterName=_CuicClusterName_Object((1,3,6,1,4,1,9,9,718,1,6,1,2),_CuicClusterName_Type())
cuicClusterName.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicClusterName.setStatus(_A)
_CuicClusterServerCount_Type=Gauge32
_CuicClusterServerCount_Object=MibTableColumn
cuicClusterServerCount=_CuicClusterServerCount_Object((1,3,6,1,4,1,9,9,718,1,6,1,3),_CuicClusterServerCount_Type())
cuicClusterServerCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicClusterServerCount.setStatus(_A)
if mibBuilder.loadTexts:cuicClusterServerCount.setUnits('servers')
_CuicClusterFirstNodeName_Type=SnmpAdminString
_CuicClusterFirstNodeName_Object=MibTableColumn
cuicClusterFirstNodeName=_CuicClusterFirstNodeName_Object((1,3,6,1,4,1,9,9,718,1,6,1,4),_CuicClusterFirstNodeName_Type())
cuicClusterFirstNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicClusterFirstNodeName.setStatus(_A)
_CuicDatasourceTable_Object=MibTable
cuicDatasourceTable=_CuicDatasourceTable_Object((1,3,6,1,4,1,9,9,718,1,7))
if mibBuilder.loadTexts:cuicDatasourceTable.setStatus(_A)
_CuicDatasourceEntry_Object=MibTableRow
cuicDatasourceEntry=_CuicDatasourceEntry_Object((1,3,6,1,4,1,9,9,718,1,7,1))
cuicDatasourceEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:cuicDatasourceEntry.setStatus(_A)
class _CuicDatasourceIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CuicDatasourceIndex_Type.__name__=_V
_CuicDatasourceIndex_Object=MibTableColumn
cuicDatasourceIndex=_CuicDatasourceIndex_Object((1,3,6,1,4,1,9,9,718,1,7,1,1),_CuicDatasourceIndex_Type())
cuicDatasourceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cuicDatasourceIndex.setStatus(_A)
_CuicDatasourceName_Type=SnmpAdminString
_CuicDatasourceName_Object=MibTableColumn
cuicDatasourceName=_CuicDatasourceName_Object((1,3,6,1,4,1,9,9,718,1,7,1,2),_CuicDatasourceName_Type())
cuicDatasourceName.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicDatasourceName.setStatus(_A)
class _CuicDatasourceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('online',1),('offline',2),(_J,3)))
_CuicDatasourceStatus_Type.__name__=_F
_CuicDatasourceStatus_Object=MibTableColumn
cuicDatasourceStatus=_CuicDatasourceStatus_Object((1,3,6,1,4,1,9,9,718,1,7,1,3),_CuicDatasourceStatus_Type())
cuicDatasourceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicDatasourceStatus.setStatus(_A)
_CuicDatasourceHost_Type=SnmpAdminString
_CuicDatasourceHost_Object=MibTableColumn
cuicDatasourceHost=_CuicDatasourceHost_Object((1,3,6,1,4,1,9,9,718,1,7,1,4),_CuicDatasourceHost_Type())
cuicDatasourceHost.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicDatasourceHost.setStatus(_A)
class _CuicDatasourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('mssql',2),('informix',3)))
_CuicDatasourceType_Type.__name__=_F
_CuicDatasourceType_Object=MibTableColumn
cuicDatasourceType=_CuicDatasourceType_Object((1,3,6,1,4,1,9,9,718,1,7,1,5),_CuicDatasourceType_Type())
cuicDatasourceType.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicDatasourceType.setStatus(_A)
_CuicSecurityTable_Object=MibTable
cuicSecurityTable=_CuicSecurityTable_Object((1,3,6,1,4,1,9,9,718,1,8))
if mibBuilder.loadTexts:cuicSecurityTable.setStatus(_A)
_CuicSecurityEntry_Object=MibTableRow
cuicSecurityEntry=_CuicSecurityEntry_Object((1,3,6,1,4,1,9,9,718,1,8,1))
cuicSecurityEntry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:cuicSecurityEntry.setStatus(_A)
_CuicSecurityIndex_Type=CuicSubsystemId
_CuicSecurityIndex_Object=MibTableColumn
cuicSecurityIndex=_CuicSecurityIndex_Object((1,3,6,1,4,1,9,9,718,1,8,1,1),_CuicSecurityIndex_Type())
cuicSecurityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cuicSecurityIndex.setStatus(_A)
_CuicSecurityUsersConfigured_Type=Gauge32
_CuicSecurityUsersConfigured_Object=MibTableColumn
cuicSecurityUsersConfigured=_CuicSecurityUsersConfigured_Object((1,3,6,1,4,1,9,9,718,1,8,1,2),_CuicSecurityUsersConfigured_Type())
cuicSecurityUsersConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicSecurityUsersConfigured.setStatus(_A)
if mibBuilder.loadTexts:cuicSecurityUsersConfigured.setUnits('users')
_CuicSecurityUsersLoggedIn_Type=Gauge32
_CuicSecurityUsersLoggedIn_Object=MibTableColumn
cuicSecurityUsersLoggedIn=_CuicSecurityUsersLoggedIn_Object((1,3,6,1,4,1,9,9,718,1,8,1,3),_CuicSecurityUsersLoggedIn_Type())
cuicSecurityUsersLoggedIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicSecurityUsersLoggedIn.setStatus(_A)
if mibBuilder.loadTexts:cuicSecurityUsersLoggedIn.setUnits('users')
_CuicSecurityLoginFailedAttempts_Type=Counter32
_CuicSecurityLoginFailedAttempts_Object=MibTableColumn
cuicSecurityLoginFailedAttempts=_CuicSecurityLoginFailedAttempts_Object((1,3,6,1,4,1,9,9,718,1,8,1,4),_CuicSecurityLoginFailedAttempts_Type())
cuicSecurityLoginFailedAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicSecurityLoginFailedAttempts.setStatus(_A)
_CuicSecurityGroupsConfigured_Type=Gauge32
_CuicSecurityGroupsConfigured_Object=MibTableColumn
cuicSecurityGroupsConfigured=_CuicSecurityGroupsConfigured_Object((1,3,6,1,4,1,9,9,718,1,8,1,5),_CuicSecurityGroupsConfigured_Type())
cuicSecurityGroupsConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicSecurityGroupsConfigured.setStatus(_A)
if mibBuilder.loadTexts:cuicSecurityGroupsConfigured.setUnits('groups')
_CuicThreadPoolInfo_ObjectIdentity=ObjectIdentity
cuicThreadPoolInfo=_CuicThreadPoolInfo_ObjectIdentity((1,3,6,1,4,1,9,9,718,1,9))
_CuicThreadsMaxAvailable_Type=Gauge32
_CuicThreadsMaxAvailable_Object=MibScalar
cuicThreadsMaxAvailable=_CuicThreadsMaxAvailable_Object((1,3,6,1,4,1,9,9,718,1,9,1),_CuicThreadsMaxAvailable_Type())
cuicThreadsMaxAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicThreadsMaxAvailable.setStatus(_A)
if mibBuilder.loadTexts:cuicThreadsMaxAvailable.setUnits(_H)
_CuicThreadsRunning_Type=Gauge32
_CuicThreadsRunning_Object=MibScalar
cuicThreadsRunning=_CuicThreadsRunning_Object((1,3,6,1,4,1,9,9,718,1,9,2),_CuicThreadsRunning_Type())
cuicThreadsRunning.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicThreadsRunning.setStatus(_A)
if mibBuilder.loadTexts:cuicThreadsRunning.setUnits(_H)
_CuicQueuedTasks_Type=Gauge32
_CuicQueuedTasks_Object=MibScalar
cuicQueuedTasks=_CuicQueuedTasks_Object((1,3,6,1,4,1,9,9,718,1,9,3),_CuicQueuedTasks_Type())
cuicQueuedTasks.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicQueuedTasks.setStatus(_A)
if mibBuilder.loadTexts:cuicQueuedTasks.setUnits('tasks')
_CuicQueuedTasksMax_Type=Gauge32
_CuicQueuedTasksMax_Object=MibScalar
cuicQueuedTasksMax=_CuicQueuedTasksMax_Object((1,3,6,1,4,1,9,9,718,1,9,4),_CuicQueuedTasksMax_Type())
cuicQueuedTasksMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicQueuedTasksMax.setStatus(_A)
if mibBuilder.loadTexts:cuicQueuedTasksMax.setUnits('tasks')
_CuicEnvInfo_ObjectIdentity=ObjectIdentity
cuicEnvInfo=_CuicEnvInfo_ObjectIdentity((1,3,6,1,4,1,9,9,718,1,10))
_CuicWaErrors_Type=Counter32
_CuicWaErrors_Object=MibScalar
cuicWaErrors=_CuicWaErrors_Object((1,3,6,1,4,1,9,9,718,1,10,1),_CuicWaErrors_Type())
cuicWaErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicWaErrors.setStatus(_A)
if mibBuilder.loadTexts:cuicWaErrors.setUnits('errors')
_CuicWaSessionsActive_Type=Gauge32
_CuicWaSessionsActive_Object=MibScalar
cuicWaSessionsActive=_CuicWaSessionsActive_Object((1,3,6,1,4,1,9,9,718,1,10,2),_CuicWaSessionsActive_Type())
cuicWaSessionsActive.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicWaSessionsActive.setStatus(_A)
if mibBuilder.loadTexts:cuicWaSessionsActive.setUnits('sessions')
class _CuicJvmPercentCPUTime_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CuicJvmPercentCPUTime_Type.__name__=_I
_CuicJvmPercentCPUTime_Object=MibScalar
cuicJvmPercentCPUTime=_CuicJvmPercentCPUTime_Object((1,3,6,1,4,1,9,9,718,1,10,3),_CuicJvmPercentCPUTime_Type())
cuicJvmPercentCPUTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicJvmPercentCPUTime.setStatus(_A)
if mibBuilder.loadTexts:cuicJvmPercentCPUTime.setUnits(_L)
_CuicJvmMemoryFree_Type=Gauge32
_CuicJvmMemoryFree_Object=MibScalar
cuicJvmMemoryFree=_CuicJvmMemoryFree_Object((1,3,6,1,4,1,9,9,718,1,10,4),_CuicJvmMemoryFree_Type())
cuicJvmMemoryFree.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicJvmMemoryFree.setStatus(_A)
if mibBuilder.loadTexts:cuicJvmMemoryFree.setUnits(_M)
_CuicJvmMemoryTotal_Type=Gauge32
_CuicJvmMemoryTotal_Object=MibScalar
cuicJvmMemoryTotal=_CuicJvmMemoryTotal_Object((1,3,6,1,4,1,9,9,718,1,10,5),_CuicJvmMemoryTotal_Type())
cuicJvmMemoryTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicJvmMemoryTotal.setStatus(_A)
if mibBuilder.loadTexts:cuicJvmMemoryTotal.setUnits(_M)
_CuicJvmMemoryMax_Type=Gauge32
_CuicJvmMemoryMax_Object=MibScalar
cuicJvmMemoryMax=_CuicJvmMemoryMax_Object((1,3,6,1,4,1,9,9,718,1,10,6),_CuicJvmMemoryMax_Type())
cuicJvmMemoryMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicJvmMemoryMax.setStatus(_A)
if mibBuilder.loadTexts:cuicJvmMemoryMax.setUnits(_M)
_CuicTomcatThreadsBusy_Type=Gauge32
_CuicTomcatThreadsBusy_Object=MibScalar
cuicTomcatThreadsBusy=_CuicTomcatThreadsBusy_Object((1,3,6,1,4,1,9,9,718,1,10,7),_CuicTomcatThreadsBusy_Type())
cuicTomcatThreadsBusy.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicTomcatThreadsBusy.setStatus(_A)
if mibBuilder.loadTexts:cuicTomcatThreadsBusy.setUnits(_H)
_CuicTomcatThreadsTotal_Type=Gauge32
_CuicTomcatThreadsTotal_Object=MibScalar
cuicTomcatThreadsTotal=_CuicTomcatThreadsTotal_Object((1,3,6,1,4,1,9,9,718,1,10,8),_CuicTomcatThreadsTotal_Type())
cuicTomcatThreadsTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicTomcatThreadsTotal.setStatus(_A)
if mibBuilder.loadTexts:cuicTomcatThreadsTotal.setUnits(_H)
_CuicTomcatThreadsMax_Type=Gauge32
_CuicTomcatThreadsMax_Object=MibScalar
cuicTomcatThreadsMax=_CuicTomcatThreadsMax_Object((1,3,6,1,4,1,9,9,718,1,10,9),_CuicTomcatThreadsMax_Type())
cuicTomcatThreadsMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cuicTomcatThreadsMax.setStatus(_A)
if mibBuilder.loadTexts:cuicTomcatThreadsMax.setUnits(_H)
_CuicNotificationInfo_ObjectIdentity=ObjectIdentity
cuicNotificationInfo=_CuicNotificationInfo_ObjectIdentity((1,3,6,1,4,1,9,9,718,1,11))
_CuicEventId_Type=Unsigned32
_CuicEventId_Object=MibScalar
cuicEventId=_CuicEventId_Object((1,3,6,1,4,1,9,9,718,1,11,1),_CuicEventId_Type())
cuicEventId.setMaxAccess(_E)
if mibBuilder.loadTexts:cuicEventId.setStatus(_A)
_CuicEventHostName_Type=SnmpAdminString
_CuicEventHostName_Object=MibScalar
cuicEventHostName=_CuicEventHostName_Object((1,3,6,1,4,1,9,9,718,1,11,2),_CuicEventHostName_Type())
cuicEventHostName.setMaxAccess(_E)
if mibBuilder.loadTexts:cuicEventHostName.setStatus(_A)
_CuicEventAppName_Type=SnmpAdminString
_CuicEventAppName_Object=MibScalar
cuicEventAppName=_CuicEventAppName_Object((1,3,6,1,4,1,9,9,718,1,11,3),_CuicEventAppName_Type())
cuicEventAppName.setMaxAccess(_E)
if mibBuilder.loadTexts:cuicEventAppName.setStatus(_A)
_CuicEventName_Type=SnmpAdminString
_CuicEventName_Object=MibScalar
cuicEventName=_CuicEventName_Object((1,3,6,1,4,1,9,9,718,1,11,4),_CuicEventName_Type())
cuicEventName.setMaxAccess(_E)
if mibBuilder.loadTexts:cuicEventName.setStatus(_A)
class _CuicEventState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('raise',1),('clear',2)))
_CuicEventState_Type.__name__=_F
_CuicEventState_Object=MibScalar
cuicEventState=_CuicEventState_Object((1,3,6,1,4,1,9,9,718,1,11,5),_CuicEventState_Type())
cuicEventState.setMaxAccess(_E)
if mibBuilder.loadTexts:cuicEventState.setStatus(_A)
class _CuicEventSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('emergency',1),('alert',2),('critical',3),('error',4),('warning',5),('notice',6),('informational',7),('debug',8)))
_CuicEventSeverity_Type.__name__=_F
_CuicEventSeverity_Object=MibScalar
cuicEventSeverity=_CuicEventSeverity_Object((1,3,6,1,4,1,9,9,718,1,11,6),_CuicEventSeverity_Type())
cuicEventSeverity.setMaxAccess(_E)
if mibBuilder.loadTexts:cuicEventSeverity.setStatus(_A)
_CuicEventTimestamp_Type=DateAndTime
_CuicEventTimestamp_Object=MibScalar
cuicEventTimestamp=_CuicEventTimestamp_Object((1,3,6,1,4,1,9,9,718,1,11,7),_CuicEventTimestamp_Type())
cuicEventTimestamp.setMaxAccess(_E)
if mibBuilder.loadTexts:cuicEventTimestamp.setStatus(_A)
_CuicEventText_Type=SnmpAdminString
_CuicEventText_Object=MibScalar
cuicEventText=_CuicEventText_Object((1,3,6,1,4,1,9,9,718,1,11,8),_CuicEventText_Type())
cuicEventText.setMaxAccess(_E)
if mibBuilder.loadTexts:cuicEventText.setStatus(_A)
_CiscoCuicappsMIBConform_ObjectIdentity=ObjectIdentity
ciscoCuicappsMIBConform=_CiscoCuicappsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,718,2))
_CiscoCuicappsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCuicappsMIBCompliances=_CiscoCuicappsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,718,2,1))
_CiscoCuicappsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCuicappsMIBGroups=_CiscoCuicappsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,718,2,2))
cuicGeneralInfoTableGroup=ObjectGroup((1,3,6,1,4,1,9,9,718,2,2,1))
cuicGeneralInfoTableGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:cuicGeneralInfoTableGroup.setStatus(_A)
cuicLicenseInfoTableGroup=ObjectGroup((1,3,6,1,4,1,9,9,718,2,2,2))
cuicLicenseInfoTableGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:cuicLicenseInfoTableGroup.setStatus(_A)
cuicReportingTableGroup=ObjectGroup((1,3,6,1,4,1,9,9,718,2,2,3))
cuicReportingTableGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:cuicReportingTableGroup.setStatus(_A)
cuicReportSchedulerTableGroup=ObjectGroup((1,3,6,1,4,1,9,9,718,2,2,4))
cuicReportSchedulerTableGroup.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:cuicReportSchedulerTableGroup.setStatus(_A)
cuicDbInfoTableGroup=ObjectGroup((1,3,6,1,4,1,9,9,718,2,2,5))
cuicDbInfoTableGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:cuicDbInfoTableGroup.setStatus(_A)
cuicClusterInfoTableGroup=ObjectGroup((1,3,6,1,4,1,9,9,718,2,2,6))
cuicClusterInfoTableGroup.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:cuicClusterInfoTableGroup.setStatus(_A)
cuicDatasourceInfoTableGroup=ObjectGroup((1,3,6,1,4,1,9,9,718,2,2,7))
cuicDatasourceInfoTableGroup.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:cuicDatasourceInfoTableGroup.setStatus(_A)
cuicSecurityTableGroup=ObjectGroup((1,3,6,1,4,1,9,9,718,2,2,8))
cuicSecurityTableGroup.setObjects(*((_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:cuicSecurityTableGroup.setStatus(_A)
cuicNotificationInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,718,2,2,9))
cuicNotificationInfoGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cuicNotificationInfoGroup.setStatus(_A)
cuicThreadPoolInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,718,2,2,11))
cuicThreadPoolInfoGroup.setObjects(*((_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:cuicThreadPoolInfoGroup.setStatus(_A)
cuicEnvInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,718,2,2,12))
cuicEnvInfoGroup.setObjects(*((_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:cuicEnvInfoGroup.setStatus(_A)
ciscoCuicappsMIBEvent=NotificationType((1,3,6,1,4,1,9,9,718,0,1))
ciscoCuicappsMIBEvent.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciscoCuicappsMIBEvent.setStatus(_A)
ciscoCuicappsMIBEventGroup=NotificationGroup((1,3,6,1,4,1,9,9,718,2,2,10))
ciscoCuicappsMIBEventGroup.setObjects((_B,_AZ))
if mibBuilder.loadTexts:ciscoCuicappsMIBEventGroup.setStatus(_A)
ciscoCuicAppsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,718,2,1,1))
ciscoCuicAppsMIBCompliance.setObjects(*((_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al)))
if mibBuilder.loadTexts:ciscoCuicAppsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CuicServiceStatus':CuicServiceStatus,'CuicSubsystemId':CuicSubsystemId,'ciscoCuicappsMIB':ciscoCuicappsMIB,'ciscoCuicappsMIBNotifs':ciscoCuicappsMIBNotifs,_AZ:ciscoCuicappsMIBEvent,'ciscoCuicappsMIBObjects':ciscoCuicappsMIBObjects,'cuicGeneralInfoTable':cuicGeneralInfoTable,'cuicGeneralInfoEntry':cuicGeneralInfoEntry,_X:cuicGeneralInfoIndex,_g:cuicGeneralInfoServerName,_h:cuicGeneralInfoServerDescription,_i:cuicGeneralInfoVersion,_j:cuicGeneralInfoStartTime,_k:cuicGeneralInfoTimeZoneName,_l:cuicGeneralInfoSystemStatus,_m:cuicGeneralInfoOpsConsoleURL,_n:cuicGeneralInfoEnableNotifications,'cuicLicenseInfoTable':cuicLicenseInfoTable,'cuicLicenseInfoEntry':cuicLicenseInfoEntry,_Y:cuicLicenseInfoIndex,_o:cuicLicenseInfoType,_p:cuicLicenseInfoStartTime,_q:cuicLicenseInfoExpirationTime,_r:cuicLicenseInfoHost,'cuicReportingTable':cuicReportingTable,'cuicReportingEntry':cuicReportingEntry,_Z:cuicReportingIndex,_s:cuicReportingDataSourceCount,_t:cuicReportingEngineStatus,_u:cuicReportingHistoricalReportDefinitionCount,_v:cuicReportingRealTimeReportDefinitionCount,_w:cuicReportingHistoricalReportRunning,_x:cuicReportingHistoricalReportWaiting,_y:cuicReportingTotalKickedOffHistoricalReports,_z:cuicReportingRealTimeReportRunning,_A0:cuicReportingTotalKickedOffRealTimeReports,_A1:cuicReportingRealTimeReportWaiting,'cuicSchedulerTable':cuicSchedulerTable,'cuicSchedulerEntry':cuicSchedulerEntry,_b:cuicSchedulerIndex,_A2:cuicSchedulerStatus,_A3:cuicSchedulerEmailServerStatus,_A4:cuicSchedulerJobsCompletedCount,_A5:cuicSchedulerJobsRunningCount,_A6:cuicSchedulerJobsFailedCount,'cuicDbInfoTable':cuicDbInfoTable,'cuicDbInfoEntry':cuicDbInfoEntry,_c:cuicDbInfoIndex,_A7:cuicDbInfoStatus,_A8:cuicDbInfoReplicationStatus,_A9:cuicDbInfoTmpSpaceUsed,_AA:cuicDbInfoSpaceUsed,'cuicClusterTable':cuicClusterTable,'cuicClusterEntry':cuicClusterEntry,_d:cuicClusterIndex,_AB:cuicClusterName,_AC:cuicClusterServerCount,_AD:cuicClusterFirstNodeName,'cuicDatasourceTable':cuicDatasourceTable,'cuicDatasourceEntry':cuicDatasourceEntry,_e:cuicDatasourceIndex,_AE:cuicDatasourceName,_AF:cuicDatasourceStatus,_AG:cuicDatasourceHost,_AH:cuicDatasourceType,'cuicSecurityTable':cuicSecurityTable,'cuicSecurityEntry':cuicSecurityEntry,_f:cuicSecurityIndex,_AI:cuicSecurityUsersConfigured,_AJ:cuicSecurityUsersLoggedIn,_AK:cuicSecurityLoginFailedAttempts,_AL:cuicSecurityGroupsConfigured,'cuicThreadPoolInfo':cuicThreadPoolInfo,_AM:cuicThreadsMaxAvailable,_AN:cuicThreadsRunning,_AO:cuicQueuedTasks,_AP:cuicQueuedTasksMax,'cuicEnvInfo':cuicEnvInfo,_AQ:cuicWaErrors,_AR:cuicWaSessionsActive,_AS:cuicJvmPercentCPUTime,_AT:cuicJvmMemoryFree,_AU:cuicJvmMemoryTotal,_AV:cuicJvmMemoryMax,_AW:cuicTomcatThreadsBusy,_AX:cuicTomcatThreadsTotal,_AY:cuicTomcatThreadsMax,'cuicNotificationInfo':cuicNotificationInfo,_N:cuicEventId,_O:cuicEventHostName,_P:cuicEventAppName,_Q:cuicEventName,_R:cuicEventState,_S:cuicEventSeverity,_T:cuicEventTimestamp,_U:cuicEventText,'ciscoCuicappsMIBConform':ciscoCuicappsMIBConform,'ciscoCuicappsMIBCompliances':ciscoCuicappsMIBCompliances,'ciscoCuicAppsMIBCompliance':ciscoCuicAppsMIBCompliance,'ciscoCuicappsMIBGroups':ciscoCuicappsMIBGroups,_Aa:cuicGeneralInfoTableGroup,_Ab:cuicLicenseInfoTableGroup,_Ac:cuicReportingTableGroup,_Ad:cuicReportSchedulerTableGroup,_Ae:cuicDbInfoTableGroup,_Af:cuicClusterInfoTableGroup,_Ag:cuicDatasourceInfoTableGroup,_Ah:cuicSecurityTableGroup,_Ai:cuicNotificationInfoGroup,_Aj:ciscoCuicappsMIBEventGroup,_Ak:cuicThreadPoolInfoGroup,_Al:cuicEnvInfoGroup})