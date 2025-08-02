_Q='historyRecordsIndex'
_P='recentLogsIndex'
_O='statisticsIndex'
_N='historyConfigIndex'
_M='emergency'
_L='critical'
_K='warning'
_J='notice'
_I='targetIndex'
_H='enabled'
_G='not-accessible'
_F='G6-LOGGING-MIB'
_E='disabled'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
management=ModuleIdentity((1,3,6,1,4,1,3181,10,6,3))
if mibBuilder.loadTexts:management.setRevisions(('2018-02-12 16:19',))
_Logging_ObjectIdentity=ObjectIdentity
logging=_Logging_ObjectIdentity((1,3,6,1,4,1,3181,10,6,3,71))
_LoggingSendTestEvent_Type=DisplayString
_LoggingSendTestEvent_Object=MibScalar
loggingSendTestEvent=_LoggingSendTestEvent_Object((1,3,6,1,4,1,3181,10,6,3,71,1),_LoggingSendTestEvent_Type())
loggingSendTestEvent.setMaxAccess(_D)
if mibBuilder.loadTexts:loggingSendTestEvent.setStatus(_A)
class _LoggingLogFileStorage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ramDisk',0),('sdCard',1)))
_LoggingLogFileStorage_Type.__name__=_C
_LoggingLogFileStorage_Object=MibScalar
loggingLogFileStorage=_LoggingLogFileStorage_Object((1,3,6,1,4,1,3181,10,6,3,71,2),_LoggingLogFileStorage_Type())
loggingLogFileStorage.setMaxAccess(_D)
if mibBuilder.loadTexts:loggingLogFileStorage.setStatus(_A)
_TargetTable_Object=MibTable
targetTable=_TargetTable_Object((1,3,6,1,4,1,3181,10,6,3,71,3))
if mibBuilder.loadTexts:targetTable.setStatus(_A)
_TargetEntry_Object=MibTableRow
targetEntry=_TargetEntry_Object((1,3,6,1,4,1,3181,10,6,3,71,3,1))
targetEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:targetEntry.setStatus(_A)
class _TargetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_TargetIndex_Type.__name__=_C
_TargetIndex_Object=MibTableColumn
targetIndex=_TargetIndex_Object((1,3,6,1,4,1,3181,10,6,3,71,3,1,1),_TargetIndex_Type())
targetIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:targetIndex.setStatus(_A)
_TargetAlias_Type=DisplayString
_TargetAlias_Object=MibTableColumn
targetAlias=_TargetAlias_Object((1,3,6,1,4,1,3181,10,6,3,71,3,1,2),_TargetAlias_Type())
targetAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:targetAlias.setStatus(_A)
_TargetHostAddress_Type=DisplayString
_TargetHostAddress_Object=MibTableColumn
targetHostAddress=_TargetHostAddress_Object((1,3,6,1,4,1,3181,10,6,3,71,3,1,3),_TargetHostAddress_Type())
targetHostAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:targetHostAddress.setStatus(_A)
class _TargetLogType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,0),('syslog',1),('snmpTrapV1',2),('snmpTrapV2c',3),('snmpTrapV3',4),('snmpInformV2c',5),('snmpInformV3',6),('displayInCli',7),('recentLogs',8)))
_TargetLogType_Type.__name__=_C
_TargetLogType_Object=MibTableColumn
targetLogType=_TargetLogType_Object((1,3,6,1,4,1,3181,10,6,3,71,3,1,4),_TargetLogType_Type())
targetLogType.setMaxAccess(_D)
if mibBuilder.loadTexts:targetLogType.setStatus(_A)
class _TargetDetailLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('concise',0),('verbose',1),('extended',2)))
_TargetDetailLevel_Type.__name__=_C
_TargetDetailLevel_Object=MibTableColumn
targetDetailLevel=_TargetDetailLevel_Object((1,3,6,1,4,1,3181,10,6,3,71,3,1,5),_TargetDetailLevel_Type())
targetDetailLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:targetDetailLevel.setStatus(_A)
class _TargetMessageFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('standard',0),('preferCustom',1),('customOnly',2)))
_TargetMessageFormat_Type.__name__=_C
_TargetMessageFormat_Object=MibTableColumn
targetMessageFormat=_TargetMessageFormat_Object((1,3,6,1,4,1,3181,10,6,3,71,3,1,6),_TargetMessageFormat_Type())
targetMessageFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:targetMessageFormat.setStatus(_A)
class _TargetTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('public',0),('preferPublic',1),('private',2),('both',3)))
_TargetTrapType_Type.__name__=_C
_TargetTrapType_Object=MibTableColumn
targetTrapType=_TargetTrapType_Object((1,3,6,1,4,1,3181,10,6,3,71,3,1,7),_TargetTrapType_Type())
targetTrapType.setMaxAccess(_D)
if mibBuilder.loadTexts:targetTrapType.setStatus(_A)
_TargetTrapCommunity_Type=DisplayString
_TargetTrapCommunity_Object=MibTableColumn
targetTrapCommunity=_TargetTrapCommunity_Object((1,3,6,1,4,1,3181,10,6,3,71,3,1,8),_TargetTrapCommunity_Type())
targetTrapCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:targetTrapCommunity.setStatus(_A)
_TargetSnmpV3Username_Type=DisplayString
_TargetSnmpV3Username_Object=MibTableColumn
targetSnmpV3Username=_TargetSnmpV3Username_Object((1,3,6,1,4,1,3181,10,6,3,71,3,1,9),_TargetSnmpV3Username_Type())
targetSnmpV3Username.setMaxAccess(_D)
if mibBuilder.loadTexts:targetSnmpV3Username.setStatus(_A)
class _TargetMinimumSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,0),('debug',1),('info',2),(_J,3),(_K,4),('error',5),(_L,6),('alert',7),(_M,8)))
_TargetMinimumSeverity_Type.__name__=_C
_TargetMinimumSeverity_Object=MibTableColumn
targetMinimumSeverity=_TargetMinimumSeverity_Object((1,3,6,1,4,1,3181,10,6,3,71,3,1,10),_TargetMinimumSeverity_Type())
targetMinimumSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:targetMinimumSeverity.setStatus(_A)
class _TargetRequiredRelevance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('any',0),('negOnly',1)))
_TargetRequiredRelevance_Type.__name__=_C
_TargetRequiredRelevance_Object=MibTableColumn
targetRequiredRelevance=_TargetRequiredRelevance_Object((1,3,6,1,4,1,3181,10,6,3,71,3,1,11),_TargetRequiredRelevance_Type())
targetRequiredRelevance.setMaxAccess(_D)
if mibBuilder.loadTexts:targetRequiredRelevance.setStatus(_A)
class _TargetRequiredSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('any',0),('portOnly',1),('unitOnly',2)))
_TargetRequiredSource_Type.__name__=_C
_TargetRequiredSource_Object=MibTableColumn
targetRequiredSource=_TargetRequiredSource_Object((1,3,6,1,4,1,3181,10,6,3,71,3,1,12),_TargetRequiredSource_Type())
targetRequiredSource.setMaxAccess(_D)
if mibBuilder.loadTexts:targetRequiredSource.setStatus(_A)
class _TargetLogConfigChanges_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_TargetLogConfigChanges_Type.__name__=_C
_TargetLogConfigChanges_Object=MibTableColumn
targetLogConfigChanges=_TargetLogConfigChanges_Object((1,3,6,1,4,1,3181,10,6,3,71,3,1,13),_TargetLogConfigChanges_Type())
targetLogConfigChanges.setMaxAccess(_D)
if mibBuilder.loadTexts:targetLogConfigChanges.setStatus(_A)
class _TargetLogDebugEventsOnly_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_TargetLogDebugEventsOnly_Type.__name__=_C
_TargetLogDebugEventsOnly_Object=MibTableColumn
targetLogDebugEventsOnly=_TargetLogDebugEventsOnly_Object((1,3,6,1,4,1,3181,10,6,3,71,3,1,14),_TargetLogDebugEventsOnly_Type())
targetLogDebugEventsOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:targetLogDebugEventsOnly.setStatus(_A)
_HistoryConfigTable_Object=MibTable
historyConfigTable=_HistoryConfigTable_Object((1,3,6,1,4,1,3181,10,6,3,71,4))
if mibBuilder.loadTexts:historyConfigTable.setStatus(_A)
_HistoryConfigEntry_Object=MibTableRow
historyConfigEntry=_HistoryConfigEntry_Object((1,3,6,1,4,1,3181,10,6,3,71,4,1))
historyConfigEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:historyConfigEntry.setStatus(_A)
class _HistoryConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_HistoryConfigIndex_Type.__name__=_C
_HistoryConfigIndex_Object=MibTableColumn
historyConfigIndex=_HistoryConfigIndex_Object((1,3,6,1,4,1,3181,10,6,3,71,4,1,1),_HistoryConfigIndex_Type())
historyConfigIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:historyConfigIndex.setStatus(_A)
_HistoryConfigName_Type=DisplayString
_HistoryConfigName_Object=MibTableColumn
historyConfigName=_HistoryConfigName_Object((1,3,6,1,4,1,3181,10,6,3,71,4,1,2),_HistoryConfigName_Type())
historyConfigName.setMaxAccess(_D)
if mibBuilder.loadTexts:historyConfigName.setStatus(_A)
class _HistoryConfigRecordMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_HistoryConfigRecordMode_Type.__name__=_C
_HistoryConfigRecordMode_Object=MibTableColumn
historyConfigRecordMode=_HistoryConfigRecordMode_Object((1,3,6,1,4,1,3181,10,6,3,71,4,1,3),_HistoryConfigRecordMode_Type())
historyConfigRecordMode.setMaxAccess(_D)
if mibBuilder.loadTexts:historyConfigRecordMode.setStatus(_A)
class _HistoryConfigHistoryFileMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('hourly',1),('daily',2)))
_HistoryConfigHistoryFileMode_Type.__name__=_C
_HistoryConfigHistoryFileMode_Object=MibTableColumn
historyConfigHistoryFileMode=_HistoryConfigHistoryFileMode_Object((1,3,6,1,4,1,3181,10,6,3,71,4,1,4),_HistoryConfigHistoryFileMode_Type())
historyConfigHistoryFileMode.setMaxAccess(_D)
if mibBuilder.loadTexts:historyConfigHistoryFileMode.setStatus(_A)
_HistoryConfigDotstring_Type=DisplayString
_HistoryConfigDotstring_Object=MibTableColumn
historyConfigDotstring=_HistoryConfigDotstring_Object((1,3,6,1,4,1,3181,10,6,3,71,4,1,5),_HistoryConfigDotstring_Type())
historyConfigDotstring.setMaxAccess(_D)
if mibBuilder.loadTexts:historyConfigDotstring.setStatus(_A)
_HistoryConfigRestart_Type=DisplayString
_HistoryConfigRestart_Object=MibTableColumn
historyConfigRestart=_HistoryConfigRestart_Object((1,3,6,1,4,1,3181,10,6,3,71,4,1,6),_HistoryConfigRestart_Type())
historyConfigRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:historyConfigRestart.setStatus(_A)
_StatisticsTable_Object=MibTable
statisticsTable=_StatisticsTable_Object((1,3,6,1,4,1,3181,10,6,3,71,100))
if mibBuilder.loadTexts:statisticsTable.setStatus(_A)
_StatisticsEntry_Object=MibTableRow
statisticsEntry=_StatisticsEntry_Object((1,3,6,1,4,1,3181,10,6,3,71,100,1))
statisticsEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:statisticsEntry.setStatus(_A)
class _StatisticsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_StatisticsIndex_Type.__name__=_C
_StatisticsIndex_Object=MibTableColumn
statisticsIndex=_StatisticsIndex_Object((1,3,6,1,4,1,3181,10,6,3,71,100,1,1),_StatisticsIndex_Type())
statisticsIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:statisticsIndex.setStatus(_A)
_StatisticsNumberOfTargets_Type=Unsigned32
_StatisticsNumberOfTargets_Object=MibTableColumn
statisticsNumberOfTargets=_StatisticsNumberOfTargets_Object((1,3,6,1,4,1,3181,10,6,3,71,100,1,2),_StatisticsNumberOfTargets_Type())
statisticsNumberOfTargets.setMaxAccess(_B)
if mibBuilder.loadTexts:statisticsNumberOfTargets.setStatus(_A)
_StatisticsLogfileCounter_Type=Unsigned32
_StatisticsLogfileCounter_Object=MibTableColumn
statisticsLogfileCounter=_StatisticsLogfileCounter_Object((1,3,6,1,4,1,3181,10,6,3,71,100,1,3),_StatisticsLogfileCounter_Type())
statisticsLogfileCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:statisticsLogfileCounter.setStatus(_A)
_StatisticsSyslogCounter_Type=Unsigned32
_StatisticsSyslogCounter_Object=MibTableColumn
statisticsSyslogCounter=_StatisticsSyslogCounter_Object((1,3,6,1,4,1,3181,10,6,3,71,100,1,4),_StatisticsSyslogCounter_Type())
statisticsSyslogCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:statisticsSyslogCounter.setStatus(_A)
_StatisticsSyslogErrorCounter_Type=Unsigned32
_StatisticsSyslogErrorCounter_Object=MibTableColumn
statisticsSyslogErrorCounter=_StatisticsSyslogErrorCounter_Object((1,3,6,1,4,1,3181,10,6,3,71,100,1,5),_StatisticsSyslogErrorCounter_Type())
statisticsSyslogErrorCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:statisticsSyslogErrorCounter.setStatus(_A)
_StatisticsLastSyslogResponse_Type=DisplayString
_StatisticsLastSyslogResponse_Object=MibTableColumn
statisticsLastSyslogResponse=_StatisticsLastSyslogResponse_Object((1,3,6,1,4,1,3181,10,6,3,71,100,1,6),_StatisticsLastSyslogResponse_Type())
statisticsLastSyslogResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:statisticsLastSyslogResponse.setStatus(_A)
_StatisticsTrapCounter_Type=Unsigned32
_StatisticsTrapCounter_Object=MibTableColumn
statisticsTrapCounter=_StatisticsTrapCounter_Object((1,3,6,1,4,1,3181,10,6,3,71,100,1,7),_StatisticsTrapCounter_Type())
statisticsTrapCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:statisticsTrapCounter.setStatus(_A)
_StatisticsTrapErrorCounter_Type=Unsigned32
_StatisticsTrapErrorCounter_Object=MibTableColumn
statisticsTrapErrorCounter=_StatisticsTrapErrorCounter_Object((1,3,6,1,4,1,3181,10,6,3,71,100,1,8),_StatisticsTrapErrorCounter_Type())
statisticsTrapErrorCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:statisticsTrapErrorCounter.setStatus(_A)
_StatisticsActiveLogfileIndex_Type=Unsigned32
_StatisticsActiveLogfileIndex_Object=MibTableColumn
statisticsActiveLogfileIndex=_StatisticsActiveLogfileIndex_Object((1,3,6,1,4,1,3181,10,6,3,71,100,1,9),_StatisticsActiveLogfileIndex_Type())
statisticsActiveLogfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:statisticsActiveLogfileIndex.setStatus(_A)
_StatisticsLogfile1Size_Type=Unsigned32
_StatisticsLogfile1Size_Object=MibTableColumn
statisticsLogfile1Size=_StatisticsLogfile1Size_Object((1,3,6,1,4,1,3181,10,6,3,71,100,1,10),_StatisticsLogfile1Size_Type())
statisticsLogfile1Size.setMaxAccess(_B)
if mibBuilder.loadTexts:statisticsLogfile1Size.setStatus(_A)
_StatisticsLogfile2Size_Type=Unsigned32
_StatisticsLogfile2Size_Object=MibTableColumn
statisticsLogfile2Size=_StatisticsLogfile2Size_Object((1,3,6,1,4,1,3181,10,6,3,71,100,1,11),_StatisticsLogfile2Size_Type())
statisticsLogfile2Size.setMaxAccess(_B)
if mibBuilder.loadTexts:statisticsLogfile2Size.setStatus(_A)
_RecentLogsTable_Object=MibTable
recentLogsTable=_RecentLogsTable_Object((1,3,6,1,4,1,3181,10,6,3,71,101))
if mibBuilder.loadTexts:recentLogsTable.setStatus(_A)
_RecentLogsEntry_Object=MibTableRow
recentLogsEntry=_RecentLogsEntry_Object((1,3,6,1,4,1,3181,10,6,3,71,101,1))
recentLogsEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:recentLogsEntry.setStatus(_A)
class _RecentLogsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_RecentLogsIndex_Type.__name__=_C
_RecentLogsIndex_Object=MibTableColumn
recentLogsIndex=_RecentLogsIndex_Object((1,3,6,1,4,1,3181,10,6,3,71,101,1,1),_RecentLogsIndex_Type())
recentLogsIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:recentLogsIndex.setStatus(_A)
_RecentLogsTimeStamp_Type=Counter32
_RecentLogsTimeStamp_Object=MibTableColumn
recentLogsTimeStamp=_RecentLogsTimeStamp_Object((1,3,6,1,4,1,3181,10,6,3,71,101,1,2),_RecentLogsTimeStamp_Type())
recentLogsTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:recentLogsTimeStamp.setStatus(_A)
class _RecentLogsSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,0),('debug',1),('info',2),(_J,3),(_K,4),('error',5),(_L,6),('alert',7),(_M,8)))
_RecentLogsSeverity_Type.__name__=_C
_RecentLogsSeverity_Object=MibTableColumn
recentLogsSeverity=_RecentLogsSeverity_Object((1,3,6,1,4,1,3181,10,6,3,71,101,1,3),_RecentLogsSeverity_Type())
recentLogsSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:recentLogsSeverity.setStatus(_A)
_RecentLogsSource_Type=DisplayString
_RecentLogsSource_Object=MibTableColumn
recentLogsSource=_RecentLogsSource_Object((1,3,6,1,4,1,3181,10,6,3,71,101,1,4),_RecentLogsSource_Type())
recentLogsSource.setMaxAccess(_B)
if mibBuilder.loadTexts:recentLogsSource.setStatus(_A)
_RecentLogsMessage_Type=DisplayString
_RecentLogsMessage_Object=MibTableColumn
recentLogsMessage=_RecentLogsMessage_Object((1,3,6,1,4,1,3181,10,6,3,71,101,1,5),_RecentLogsMessage_Type())
recentLogsMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:recentLogsMessage.setStatus(_A)
_HistoryRecordsTable_Object=MibTable
historyRecordsTable=_HistoryRecordsTable_Object((1,3,6,1,4,1,3181,10,6,3,71,102))
if mibBuilder.loadTexts:historyRecordsTable.setStatus(_A)
_HistoryRecordsEntry_Object=MibTableRow
historyRecordsEntry=_HistoryRecordsEntry_Object((1,3,6,1,4,1,3181,10,6,3,71,102,1))
historyRecordsEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:historyRecordsEntry.setStatus(_A)
class _HistoryRecordsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_HistoryRecordsIndex_Type.__name__=_C
_HistoryRecordsIndex_Object=MibTableColumn
historyRecordsIndex=_HistoryRecordsIndex_Object((1,3,6,1,4,1,3181,10,6,3,71,102,1,1),_HistoryRecordsIndex_Type())
historyRecordsIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:historyRecordsIndex.setStatus(_A)
_HistoryRecordsName_Type=DisplayString
_HistoryRecordsName_Object=MibTableColumn
historyRecordsName=_HistoryRecordsName_Object((1,3,6,1,4,1,3181,10,6,3,71,102,1,2),_HistoryRecordsName_Type())
historyRecordsName.setMaxAccess(_B)
if mibBuilder.loadTexts:historyRecordsName.setStatus(_A)
class _HistoryRecordsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),('invalid',1),('normal',2),('updating',3)))
_HistoryRecordsState_Type.__name__=_C
_HistoryRecordsState_Object=MibTableColumn
historyRecordsState=_HistoryRecordsState_Object((1,3,6,1,4,1,3181,10,6,3,71,102,1,3),_HistoryRecordsState_Type())
historyRecordsState.setMaxAccess(_B)
if mibBuilder.loadTexts:historyRecordsState.setStatus(_A)
_HistoryRecordsLastValue_Type=DisplayString
_HistoryRecordsLastValue_Object=MibTableColumn
historyRecordsLastValue=_HistoryRecordsLastValue_Object((1,3,6,1,4,1,3181,10,6,3,71,102,1,4),_HistoryRecordsLastValue_Type())
historyRecordsLastValue.setMaxAccess(_B)
if mibBuilder.loadTexts:historyRecordsLastValue.setStatus(_A)
_HistoryRecordsAverageLastMinute_Type=DisplayString
_HistoryRecordsAverageLastMinute_Object=MibTableColumn
historyRecordsAverageLastMinute=_HistoryRecordsAverageLastMinute_Object((1,3,6,1,4,1,3181,10,6,3,71,102,1,5),_HistoryRecordsAverageLastMinute_Type())
historyRecordsAverageLastMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:historyRecordsAverageLastMinute.setStatus(_A)
_HistoryRecordsAverageLastHour_Type=DisplayString
_HistoryRecordsAverageLastHour_Object=MibTableColumn
historyRecordsAverageLastHour=_HistoryRecordsAverageLastHour_Object((1,3,6,1,4,1,3181,10,6,3,71,102,1,6),_HistoryRecordsAverageLastHour_Type())
historyRecordsAverageLastHour.setMaxAccess(_B)
if mibBuilder.loadTexts:historyRecordsAverageLastHour.setStatus(_A)
_HistoryRecordsLastMinute_Type=DisplayString
_HistoryRecordsLastMinute_Object=MibTableColumn
historyRecordsLastMinute=_HistoryRecordsLastMinute_Object((1,3,6,1,4,1,3181,10,6,3,71,102,1,7),_HistoryRecordsLastMinute_Type())
historyRecordsLastMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:historyRecordsLastMinute.setStatus(_A)
_HistoryRecordsLastHour_Type=DisplayString
_HistoryRecordsLastHour_Object=MibTableColumn
historyRecordsLastHour=_HistoryRecordsLastHour_Object((1,3,6,1,4,1,3181,10,6,3,71,102,1,8),_HistoryRecordsLastHour_Type())
historyRecordsLastHour.setMaxAccess(_B)
if mibBuilder.loadTexts:historyRecordsLastHour.setStatus(_A)
_HistoryRecordsLastDay_Type=DisplayString
_HistoryRecordsLastDay_Object=MibTableColumn
historyRecordsLastDay=_HistoryRecordsLastDay_Object((1,3,6,1,4,1,3181,10,6,3,71,102,1,9),_HistoryRecordsLastDay_Type())
historyRecordsLastDay.setMaxAccess(_B)
if mibBuilder.loadTexts:historyRecordsLastDay.setStatus(_A)
_HistoryRecordsLastUpdate_Type=Counter32
_HistoryRecordsLastUpdate_Object=MibTableColumn
historyRecordsLastUpdate=_HistoryRecordsLastUpdate_Object((1,3,6,1,4,1,3181,10,6,3,71,102,1,10),_HistoryRecordsLastUpdate_Type())
historyRecordsLastUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:historyRecordsLastUpdate.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'management':management,'logging':logging,'loggingSendTestEvent':loggingSendTestEvent,'loggingLogFileStorage':loggingLogFileStorage,'targetTable':targetTable,'targetEntry':targetEntry,_I:targetIndex,'targetAlias':targetAlias,'targetHostAddress':targetHostAddress,'targetLogType':targetLogType,'targetDetailLevel':targetDetailLevel,'targetMessageFormat':targetMessageFormat,'targetTrapType':targetTrapType,'targetTrapCommunity':targetTrapCommunity,'targetSnmpV3Username':targetSnmpV3Username,'targetMinimumSeverity':targetMinimumSeverity,'targetRequiredRelevance':targetRequiredRelevance,'targetRequiredSource':targetRequiredSource,'targetLogConfigChanges':targetLogConfigChanges,'targetLogDebugEventsOnly':targetLogDebugEventsOnly,'historyConfigTable':historyConfigTable,'historyConfigEntry':historyConfigEntry,_N:historyConfigIndex,'historyConfigName':historyConfigName,'historyConfigRecordMode':historyConfigRecordMode,'historyConfigHistoryFileMode':historyConfigHistoryFileMode,'historyConfigDotstring':historyConfigDotstring,'historyConfigRestart':historyConfigRestart,'statisticsTable':statisticsTable,'statisticsEntry':statisticsEntry,_O:statisticsIndex,'statisticsNumberOfTargets':statisticsNumberOfTargets,'statisticsLogfileCounter':statisticsLogfileCounter,'statisticsSyslogCounter':statisticsSyslogCounter,'statisticsSyslogErrorCounter':statisticsSyslogErrorCounter,'statisticsLastSyslogResponse':statisticsLastSyslogResponse,'statisticsTrapCounter':statisticsTrapCounter,'statisticsTrapErrorCounter':statisticsTrapErrorCounter,'statisticsActiveLogfileIndex':statisticsActiveLogfileIndex,'statisticsLogfile1Size':statisticsLogfile1Size,'statisticsLogfile2Size':statisticsLogfile2Size,'recentLogsTable':recentLogsTable,'recentLogsEntry':recentLogsEntry,_P:recentLogsIndex,'recentLogsTimeStamp':recentLogsTimeStamp,'recentLogsSeverity':recentLogsSeverity,'recentLogsSource':recentLogsSource,'recentLogsMessage':recentLogsMessage,'historyRecordsTable':historyRecordsTable,'historyRecordsEntry':historyRecordsEntry,_Q:historyRecordsIndex,'historyRecordsName':historyRecordsName,'historyRecordsState':historyRecordsState,'historyRecordsLastValue':historyRecordsLastValue,'historyRecordsAverageLastMinute':historyRecordsAverageLastMinute,'historyRecordsAverageLastHour':historyRecordsAverageLastHour,'historyRecordsLastMinute':historyRecordsLastMinute,'historyRecordsLastHour':historyRecordsLastHour,'historyRecordsLastDay':historyRecordsLastDay,'historyRecordsLastUpdate':historyRecordsLastUpdate})