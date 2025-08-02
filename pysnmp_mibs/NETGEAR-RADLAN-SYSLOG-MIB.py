_L='rlSyslogCountersPerSeverityIndex'
_K='rlSyslogLogCacheCounter'
_J='rlSyslogLogCounter'
_I='Unsigned32'
_H='NETGEAR-RADLAN-SYSLOG-MIB'
_G='TruthValue'
_F='Integer32'
_E='RlSyslogSeverity'
_D='read-write'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention',_G)
rlSyslog=ModuleIdentity((1,3,6,1,4,1,4526,17,82))
if mibBuilder.loadTexts:rlSyslog.setRevisions(('2006-02-12 00:00','2003-09-22 00:00'))
class RlSyslogSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7),('notActive',8)))
_RlSyslogPrivate_ObjectIdentity=ObjectIdentity
rlSyslogPrivate=_RlSyslogPrivate_ObjectIdentity((1,3,6,1,4,1,4526,17,82,2))
class _RlSyslogGlobalEnable_Type(TruthValue):defaultValue=1
_RlSyslogGlobalEnable_Type.__name__=_G
_RlSyslogGlobalEnable_Object=MibScalar
rlSyslogGlobalEnable=_RlSyslogGlobalEnable_Object((1,3,6,1,4,1,4526,17,82,2,1),_RlSyslogGlobalEnable_Type())
rlSyslogGlobalEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSyslogGlobalEnable.setStatus(_A)
class _RlSyslogMinLogToConsoleSeverity_Type(RlSyslogSeverity):defaultValue=6
_RlSyslogMinLogToConsoleSeverity_Type.__name__=_E
_RlSyslogMinLogToConsoleSeverity_Object=MibScalar
rlSyslogMinLogToConsoleSeverity=_RlSyslogMinLogToConsoleSeverity_Object((1,3,6,1,4,1,4526,17,82,2,2),_RlSyslogMinLogToConsoleSeverity_Type())
rlSyslogMinLogToConsoleSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSyslogMinLogToConsoleSeverity.setStatus(_A)
class _RlSyslogMinLogToFileSeverity_Type(RlSyslogSeverity):defaultValue=3
_RlSyslogMinLogToFileSeverity_Type.__name__=_E
_RlSyslogMinLogToFileSeverity_Object=MibScalar
rlSyslogMinLogToFileSeverity=_RlSyslogMinLogToFileSeverity_Object((1,3,6,1,4,1,4526,17,82,2,3),_RlSyslogMinLogToFileSeverity_Type())
rlSyslogMinLogToFileSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSyslogMinLogToFileSeverity.setStatus(_A)
class _RlSyslogMinLogToCacheSeverity_Type(RlSyslogSeverity):defaultValue=6
_RlSyslogMinLogToCacheSeverity_Type.__name__=_E
_RlSyslogMinLogToCacheSeverity_Object=MibScalar
rlSyslogMinLogToCacheSeverity=_RlSyslogMinLogToCacheSeverity_Object((1,3,6,1,4,1,4526,17,82,2,4),_RlSyslogMinLogToCacheSeverity_Type())
rlSyslogMinLogToCacheSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSyslogMinLogToCacheSeverity.setStatus(_A)
_RlSyslogClearLogfile_Type=Unsigned32
_RlSyslogClearLogfile_Object=MibScalar
rlSyslogClearLogfile=_RlSyslogClearLogfile_Object((1,3,6,1,4,1,4526,17,82,2,5),_RlSyslogClearLogfile_Type())
rlSyslogClearLogfile.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSyslogClearLogfile.setStatus(_A)
_RlSyslogClearCache_Type=Unsigned32
_RlSyslogClearCache_Object=MibScalar
rlSyslogClearCache=_RlSyslogClearCache_Object((1,3,6,1,4,1,4526,17,82,2,6),_RlSyslogClearCache_Type())
rlSyslogClearCache.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSyslogClearCache.setStatus(_A)
_RlSyslogMibVersion_Type=Integer32
_RlSyslogMibVersion_Object=MibScalar
rlSyslogMibVersion=_RlSyslogMibVersion_Object((1,3,6,1,4,1,4526,17,82,2,7),_RlSyslogMibVersion_Type())
rlSyslogMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogMibVersion.setStatus(_A)
_RlSyslogLogTable_Object=MibTable
rlSyslogLogTable=_RlSyslogLogTable_Object((1,3,6,1,4,1,4526,17,82,2,8))
if mibBuilder.loadTexts:rlSyslogLogTable.setStatus(_A)
_RlSyslogLogEntry_Object=MibTableRow
rlSyslogLogEntry=_RlSyslogLogEntry_Object((1,3,6,1,4,1,4526,17,82,2,8,1))
rlSyslogLogEntry.setIndexNames((0,_H,_J))
if mibBuilder.loadTexts:rlSyslogLogEntry.setStatus(_A)
_RlSyslogLogCounter_Type=Unsigned32
_RlSyslogLogCounter_Object=MibTableColumn
rlSyslogLogCounter=_RlSyslogLogCounter_Object((1,3,6,1,4,1,4526,17,82,2,8,1,1),_RlSyslogLogCounter_Type())
rlSyslogLogCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogCounter.setStatus(_A)
class _RlSyslogLogDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlSyslogLogDateTime_Type.__name__=_C
_RlSyslogLogDateTime_Object=MibTableColumn
rlSyslogLogDateTime=_RlSyslogLogDateTime_Object((1,3,6,1,4,1,4526,17,82,2,8,1,2),_RlSyslogLogDateTime_Type())
rlSyslogLogDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogDateTime.setStatus(_A)
class _RlSyslogLogAppMnemonic_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_RlSyslogLogAppMnemonic_Type.__name__=_C
_RlSyslogLogAppMnemonic_Object=MibTableColumn
rlSyslogLogAppMnemonic=_RlSyslogLogAppMnemonic_Object((1,3,6,1,4,1,4526,17,82,2,8,1,3),_RlSyslogLogAppMnemonic_Type())
rlSyslogLogAppMnemonic.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogAppMnemonic.setStatus(_A)
_RlSyslogLogSeverity_Type=RlSyslogSeverity
_RlSyslogLogSeverity_Object=MibTableColumn
rlSyslogLogSeverity=_RlSyslogLogSeverity_Object((1,3,6,1,4,1,4526,17,82,2,8,1,4),_RlSyslogLogSeverity_Type())
rlSyslogLogSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogSeverity.setStatus(_A)
class _RlSyslogLogMessageMnemonic_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlSyslogLogMessageMnemonic_Type.__name__=_C
_RlSyslogLogMessageMnemonic_Object=MibTableColumn
rlSyslogLogMessageMnemonic=_RlSyslogLogMessageMnemonic_Object((1,3,6,1,4,1,4526,17,82,2,8,1,5),_RlSyslogLogMessageMnemonic_Type())
rlSyslogLogMessageMnemonic.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogMessageMnemonic.setStatus(_A)
class _RlSyslogLogText1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlSyslogLogText1_Type.__name__=_C
_RlSyslogLogText1_Object=MibTableColumn
rlSyslogLogText1=_RlSyslogLogText1_Object((1,3,6,1,4,1,4526,17,82,2,8,1,6),_RlSyslogLogText1_Type())
rlSyslogLogText1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogText1.setStatus(_A)
class _RlSyslogLogText2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlSyslogLogText2_Type.__name__=_C
_RlSyslogLogText2_Object=MibTableColumn
rlSyslogLogText2=_RlSyslogLogText2_Object((1,3,6,1,4,1,4526,17,82,2,8,1,7),_RlSyslogLogText2_Type())
rlSyslogLogText2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogText2.setStatus(_A)
class _RlSyslogLogText3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlSyslogLogText3_Type.__name__=_C
_RlSyslogLogText3_Object=MibTableColumn
rlSyslogLogText3=_RlSyslogLogText3_Object((1,3,6,1,4,1,4526,17,82,2,8,1,8),_RlSyslogLogText3_Type())
rlSyslogLogText3.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogText3.setStatus(_A)
class _RlSyslogLogText4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlSyslogLogText4_Type.__name__=_C
_RlSyslogLogText4_Object=MibTableColumn
rlSyslogLogText4=_RlSyslogLogText4_Object((1,3,6,1,4,1,4526,17,82,2,8,1,9),_RlSyslogLogText4_Type())
rlSyslogLogText4.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogText4.setStatus(_A)
_RlSyslogLogCacheTable_Object=MibTable
rlSyslogLogCacheTable=_RlSyslogLogCacheTable_Object((1,3,6,1,4,1,4526,17,82,2,9))
if mibBuilder.loadTexts:rlSyslogLogCacheTable.setStatus(_A)
_RlSyslogLogCacheEntry_Object=MibTableRow
rlSyslogLogCacheEntry=_RlSyslogLogCacheEntry_Object((1,3,6,1,4,1,4526,17,82,2,9,1))
rlSyslogLogCacheEntry.setIndexNames((0,_H,_K))
if mibBuilder.loadTexts:rlSyslogLogCacheEntry.setStatus(_A)
_RlSyslogLogCacheCounter_Type=Unsigned32
_RlSyslogLogCacheCounter_Object=MibTableColumn
rlSyslogLogCacheCounter=_RlSyslogLogCacheCounter_Object((1,3,6,1,4,1,4526,17,82,2,9,1,1),_RlSyslogLogCacheCounter_Type())
rlSyslogLogCacheCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogCacheCounter.setStatus(_A)
class _RlSyslogLogCacheDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlSyslogLogCacheDateTime_Type.__name__=_C
_RlSyslogLogCacheDateTime_Object=MibTableColumn
rlSyslogLogCacheDateTime=_RlSyslogLogCacheDateTime_Object((1,3,6,1,4,1,4526,17,82,2,9,1,2),_RlSyslogLogCacheDateTime_Type())
rlSyslogLogCacheDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogCacheDateTime.setStatus(_A)
class _RlSyslogLogCacheAppMnemonic_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_RlSyslogLogCacheAppMnemonic_Type.__name__=_C
_RlSyslogLogCacheAppMnemonic_Object=MibTableColumn
rlSyslogLogCacheAppMnemonic=_RlSyslogLogCacheAppMnemonic_Object((1,3,6,1,4,1,4526,17,82,2,9,1,3),_RlSyslogLogCacheAppMnemonic_Type())
rlSyslogLogCacheAppMnemonic.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogCacheAppMnemonic.setStatus(_A)
_RlSyslogLogCacheSeverity_Type=RlSyslogSeverity
_RlSyslogLogCacheSeverity_Object=MibTableColumn
rlSyslogLogCacheSeverity=_RlSyslogLogCacheSeverity_Object((1,3,6,1,4,1,4526,17,82,2,9,1,4),_RlSyslogLogCacheSeverity_Type())
rlSyslogLogCacheSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogCacheSeverity.setStatus(_A)
class _RlSyslogLogCacheMessageMnemonic_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlSyslogLogCacheMessageMnemonic_Type.__name__=_C
_RlSyslogLogCacheMessageMnemonic_Object=MibTableColumn
rlSyslogLogCacheMessageMnemonic=_RlSyslogLogCacheMessageMnemonic_Object((1,3,6,1,4,1,4526,17,82,2,9,1,5),_RlSyslogLogCacheMessageMnemonic_Type())
rlSyslogLogCacheMessageMnemonic.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogCacheMessageMnemonic.setStatus(_A)
class _RlSyslogLogCacheText1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,160))
_RlSyslogLogCacheText1_Type.__name__=_C
_RlSyslogLogCacheText1_Object=MibTableColumn
rlSyslogLogCacheText1=_RlSyslogLogCacheText1_Object((1,3,6,1,4,1,4526,17,82,2,9,1,6),_RlSyslogLogCacheText1_Type())
rlSyslogLogCacheText1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogCacheText1.setStatus(_A)
class _RlSyslogLogCacheText2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,160))
_RlSyslogLogCacheText2_Type.__name__=_C
_RlSyslogLogCacheText2_Object=MibTableColumn
rlSyslogLogCacheText2=_RlSyslogLogCacheText2_Object((1,3,6,1,4,1,4526,17,82,2,9,1,7),_RlSyslogLogCacheText2_Type())
rlSyslogLogCacheText2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogCacheText2.setStatus(_A)
class _RlSyslogLogCacheText3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,160))
_RlSyslogLogCacheText3_Type.__name__=_C
_RlSyslogLogCacheText3_Object=MibTableColumn
rlSyslogLogCacheText3=_RlSyslogLogCacheText3_Object((1,3,6,1,4,1,4526,17,82,2,9,1,8),_RlSyslogLogCacheText3_Type())
rlSyslogLogCacheText3.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogCacheText3.setStatus(_A)
class _RlSyslogLogCacheText4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,160))
_RlSyslogLogCacheText4_Type.__name__=_C
_RlSyslogLogCacheText4_Object=MibTableColumn
rlSyslogLogCacheText4=_RlSyslogLogCacheText4_Object((1,3,6,1,4,1,4526,17,82,2,9,1,9),_RlSyslogLogCacheText4_Type())
rlSyslogLogCacheText4.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogLogCacheText4.setStatus(_A)
_RlSyslogConsoleMessagesIgnored_Type=Counter32
_RlSyslogConsoleMessagesIgnored_Object=MibScalar
rlSyslogConsoleMessagesIgnored=_RlSyslogConsoleMessagesIgnored_Object((1,3,6,1,4,1,4526,17,82,2,10),_RlSyslogConsoleMessagesIgnored_Type())
rlSyslogConsoleMessagesIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogConsoleMessagesIgnored.setStatus(_A)
_RlSyslogFileMessagesIgnored_Type=Counter32
_RlSyslogFileMessagesIgnored_Object=MibScalar
rlSyslogFileMessagesIgnored=_RlSyslogFileMessagesIgnored_Object((1,3,6,1,4,1,4526,17,82,2,11),_RlSyslogFileMessagesIgnored_Type())
rlSyslogFileMessagesIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogFileMessagesIgnored.setStatus(_A)
_RlSyslogFileMessagesLogged_Type=Counter32
_RlSyslogFileMessagesLogged_Object=MibScalar
rlSyslogFileMessagesLogged=_RlSyslogFileMessagesLogged_Object((1,3,6,1,4,1,4526,17,82,2,12),_RlSyslogFileMessagesLogged_Type())
rlSyslogFileMessagesLogged.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogFileMessagesLogged.setStatus(_A)
_RlSyslogCacheTotalMessages_Type=Counter32
_RlSyslogCacheTotalMessages_Object=MibScalar
rlSyslogCacheTotalMessages=_RlSyslogCacheTotalMessages_Object((1,3,6,1,4,1,4526,17,82,2,13),_RlSyslogCacheTotalMessages_Type())
rlSyslogCacheTotalMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogCacheTotalMessages.setStatus(_A)
_RlSyslogAggregationEnable_Type=TruthValue
_RlSyslogAggregationEnable_Object=MibScalar
rlSyslogAggregationEnable=_RlSyslogAggregationEnable_Object((1,3,6,1,4,1,4526,17,82,2,14),_RlSyslogAggregationEnable_Type())
rlSyslogAggregationEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSyslogAggregationEnable.setStatus(_A)
class _RlSyslogAggregationAgingTime_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,3600))
_RlSyslogAggregationAgingTime_Type.__name__=_I
_RlSyslogAggregationAgingTime_Object=MibScalar
rlSyslogAggregationAgingTime=_RlSyslogAggregationAgingTime_Object((1,3,6,1,4,1,4526,17,82,2,15),_RlSyslogAggregationAgingTime_Type())
rlSyslogAggregationAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSyslogAggregationAgingTime.setStatus(_A)
class _RlSyslogMinLogToWebSeverity_Type(RlSyslogSeverity):defaultValue=6
_RlSyslogMinLogToWebSeverity_Type.__name__=_E
_RlSyslogMinLogToWebSeverity_Object=MibScalar
rlSyslogMinLogToWebSeverity=_RlSyslogMinLogToWebSeverity_Object((1,3,6,1,4,1,4526,17,82,2,16),_RlSyslogMinLogToWebSeverity_Type())
rlSyslogMinLogToWebSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSyslogMinLogToWebSeverity.setStatus(_A)
class _RlSyslogAlarmFlag_Type(TruthValue):defaultValue=2
_RlSyslogAlarmFlag_Type.__name__=_G
_RlSyslogAlarmFlag_Object=MibScalar
rlSyslogAlarmFlag=_RlSyslogAlarmFlag_Object((1,3,6,1,4,1,4526,17,82,2,17),_RlSyslogAlarmFlag_Type())
rlSyslogAlarmFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSyslogAlarmFlag.setStatus(_A)
class _RlSyslogOriginId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('default',1),('hostname',2),('ip',3),('ipv6',4),('string',5)))
_RlSyslogOriginId_Type.__name__=_F
_RlSyslogOriginId_Object=MibScalar
rlSyslogOriginId=_RlSyslogOriginId_Object((1,3,6,1,4,1,4526,17,82,2,18),_RlSyslogOriginId_Type())
rlSyslogOriginId.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSyslogOriginId.setStatus(_A)
class _RlSyslogOriginIdString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlSyslogOriginIdString_Type.__name__=_C
_RlSyslogOriginIdString_Object=MibScalar
rlSyslogOriginIdString=_RlSyslogOriginIdString_Object((1,3,6,1,4,1,4526,17,82,2,19),_RlSyslogOriginIdString_Type())
rlSyslogOriginIdString.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSyslogOriginIdString.setStatus(_A)
class _RlSyslogHeaderSendingEnabled_Type(TruthValue):defaultValue=1
_RlSyslogHeaderSendingEnabled_Type.__name__=_G
_RlSyslogHeaderSendingEnabled_Object=MibScalar
rlSyslogHeaderSendingEnabled=_RlSyslogHeaderSendingEnabled_Object((1,3,6,1,4,1,4526,17,82,2,20),_RlSyslogHeaderSendingEnabled_Type())
rlSyslogHeaderSendingEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSyslogHeaderSendingEnabled.setStatus(_A)
_RlSyslogCountersPerSeverityTable_Object=MibTable
rlSyslogCountersPerSeverityTable=_RlSyslogCountersPerSeverityTable_Object((1,3,6,1,4,1,4526,17,82,2,21))
if mibBuilder.loadTexts:rlSyslogCountersPerSeverityTable.setStatus(_A)
_RlSyslogCountersPerSeverityEntry_Object=MibTableRow
rlSyslogCountersPerSeverityEntry=_RlSyslogCountersPerSeverityEntry_Object((1,3,6,1,4,1,4526,17,82,2,21,1))
rlSyslogCountersPerSeverityEntry.setIndexNames((0,_H,_L))
if mibBuilder.loadTexts:rlSyslogCountersPerSeverityEntry.setStatus(_A)
class _RlSyslogCountersPerSeverityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('static',1))
_RlSyslogCountersPerSeverityIndex_Type.__name__=_F
_RlSyslogCountersPerSeverityIndex_Object=MibTableColumn
rlSyslogCountersPerSeverityIndex=_RlSyslogCountersPerSeverityIndex_Object((1,3,6,1,4,1,4526,17,82,2,21,1,1),_RlSyslogCountersPerSeverityIndex_Type())
rlSyslogCountersPerSeverityIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rlSyslogCountersPerSeverityIndex.setStatus(_A)
_RlSyslogCountersPerSeverityEmergencyCounter_Type=Counter32
_RlSyslogCountersPerSeverityEmergencyCounter_Object=MibTableColumn
rlSyslogCountersPerSeverityEmergencyCounter=_RlSyslogCountersPerSeverityEmergencyCounter_Object((1,3,6,1,4,1,4526,17,82,2,21,1,2),_RlSyslogCountersPerSeverityEmergencyCounter_Type())
rlSyslogCountersPerSeverityEmergencyCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogCountersPerSeverityEmergencyCounter.setStatus(_A)
_RlSyslogCountersPerSeverityAlertCounter_Type=Counter32
_RlSyslogCountersPerSeverityAlertCounter_Object=MibTableColumn
rlSyslogCountersPerSeverityAlertCounter=_RlSyslogCountersPerSeverityAlertCounter_Object((1,3,6,1,4,1,4526,17,82,2,21,1,3),_RlSyslogCountersPerSeverityAlertCounter_Type())
rlSyslogCountersPerSeverityAlertCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogCountersPerSeverityAlertCounter.setStatus(_A)
_RlSyslogCountersPerSeverityCriticalCounter_Type=Counter32
_RlSyslogCountersPerSeverityCriticalCounter_Object=MibTableColumn
rlSyslogCountersPerSeverityCriticalCounter=_RlSyslogCountersPerSeverityCriticalCounter_Object((1,3,6,1,4,1,4526,17,82,2,21,1,4),_RlSyslogCountersPerSeverityCriticalCounter_Type())
rlSyslogCountersPerSeverityCriticalCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogCountersPerSeverityCriticalCounter.setStatus(_A)
_RlSyslogCountersPerSeverityErrorCounter_Type=Counter32
_RlSyslogCountersPerSeverityErrorCounter_Object=MibTableColumn
rlSyslogCountersPerSeverityErrorCounter=_RlSyslogCountersPerSeverityErrorCounter_Object((1,3,6,1,4,1,4526,17,82,2,21,1,5),_RlSyslogCountersPerSeverityErrorCounter_Type())
rlSyslogCountersPerSeverityErrorCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogCountersPerSeverityErrorCounter.setStatus(_A)
_RlSyslogCountersPerSeverityWarningCounter_Type=Counter32
_RlSyslogCountersPerSeverityWarningCounter_Object=MibTableColumn
rlSyslogCountersPerSeverityWarningCounter=_RlSyslogCountersPerSeverityWarningCounter_Object((1,3,6,1,4,1,4526,17,82,2,21,1,6),_RlSyslogCountersPerSeverityWarningCounter_Type())
rlSyslogCountersPerSeverityWarningCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogCountersPerSeverityWarningCounter.setStatus(_A)
_RlSyslogCountersPerSeverityNoticeCounter_Type=Counter32
_RlSyslogCountersPerSeverityNoticeCounter_Object=MibTableColumn
rlSyslogCountersPerSeverityNoticeCounter=_RlSyslogCountersPerSeverityNoticeCounter_Object((1,3,6,1,4,1,4526,17,82,2,21,1,7),_RlSyslogCountersPerSeverityNoticeCounter_Type())
rlSyslogCountersPerSeverityNoticeCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogCountersPerSeverityNoticeCounter.setStatus(_A)
_RlSyslogCountersPerSeverityInfoCounter_Type=Counter32
_RlSyslogCountersPerSeverityInfoCounter_Object=MibTableColumn
rlSyslogCountersPerSeverityInfoCounter=_RlSyslogCountersPerSeverityInfoCounter_Object((1,3,6,1,4,1,4526,17,82,2,21,1,8),_RlSyslogCountersPerSeverityInfoCounter_Type())
rlSyslogCountersPerSeverityInfoCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogCountersPerSeverityInfoCounter.setStatus(_A)
_RlSyslogCountersPerSeverityDebugCounter_Type=Counter32
_RlSyslogCountersPerSeverityDebugCounter_Object=MibTableColumn
rlSyslogCountersPerSeverityDebugCounter=_RlSyslogCountersPerSeverityDebugCounter_Object((1,3,6,1,4,1,4526,17,82,2,21,1,9),_RlSyslogCountersPerSeverityDebugCounter_Type())
rlSyslogCountersPerSeverityDebugCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSyslogCountersPerSeverityDebugCounter.setStatus(_A)
_RlSyslogPhaseOneTests_ObjectIdentity=ObjectIdentity
rlSyslogPhaseOneTests=_RlSyslogPhaseOneTests_ObjectIdentity((1,3,6,1,4,1,4526,17,82,3))
class _RlSyslogPhaseOneTestGenerator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(11,12,13,14,15,16,17,21,22,23,24,25,31,32,33,34,35,36,41,42,43,47,62)));namedValues=NamedValues(*(('successfulRegistration',11),('regTheSameComponentTwice',12),('regWithInvalidComponentID',13),('regWithInvalidApplicationID',14),('regWithInvalidMessageString',15),('regWithInvalidMessageList',16),('regWithInvalidApplicationList',17),('successfulLoggingWithNoParams',21),('logWithUnregisteredComponentID',22),('logWithInvalidComponentID',23),('logWithBadApplicationID',24),('logWithBadMessageID',25),('paramFormatting',31),('insufficientParams',32),('incorrectParams',33),('tooManyParams',34),('oversizedParams',35),('trapParams',36),('successfulFatalError',41),('fatalErrorThroughNonFatalInterface',42),('nonFatalErrorThroughFatalInterface',43),('nestedFatalErrors',47),('snmpAccessToLongMessage',62)))
_RlSyslogPhaseOneTestGenerator_Type.__name__=_F
_RlSyslogPhaseOneTestGenerator_Object=MibScalar
rlSyslogPhaseOneTestGenerator=_RlSyslogPhaseOneTestGenerator_Object((1,3,6,1,4,1,4526,17,82,3,1),_RlSyslogPhaseOneTestGenerator_Type())
rlSyslogPhaseOneTestGenerator.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSyslogPhaseOneTestGenerator.setStatus(_A)
mibBuilder.exportSymbols(_H,**{_E:RlSyslogSeverity,'rlSyslog':rlSyslog,'rlSyslogPrivate':rlSyslogPrivate,'rlSyslogGlobalEnable':rlSyslogGlobalEnable,'rlSyslogMinLogToConsoleSeverity':rlSyslogMinLogToConsoleSeverity,'rlSyslogMinLogToFileSeverity':rlSyslogMinLogToFileSeverity,'rlSyslogMinLogToCacheSeverity':rlSyslogMinLogToCacheSeverity,'rlSyslogClearLogfile':rlSyslogClearLogfile,'rlSyslogClearCache':rlSyslogClearCache,'rlSyslogMibVersion':rlSyslogMibVersion,'rlSyslogLogTable':rlSyslogLogTable,'rlSyslogLogEntry':rlSyslogLogEntry,_J:rlSyslogLogCounter,'rlSyslogLogDateTime':rlSyslogLogDateTime,'rlSyslogLogAppMnemonic':rlSyslogLogAppMnemonic,'rlSyslogLogSeverity':rlSyslogLogSeverity,'rlSyslogLogMessageMnemonic':rlSyslogLogMessageMnemonic,'rlSyslogLogText1':rlSyslogLogText1,'rlSyslogLogText2':rlSyslogLogText2,'rlSyslogLogText3':rlSyslogLogText3,'rlSyslogLogText4':rlSyslogLogText4,'rlSyslogLogCacheTable':rlSyslogLogCacheTable,'rlSyslogLogCacheEntry':rlSyslogLogCacheEntry,_K:rlSyslogLogCacheCounter,'rlSyslogLogCacheDateTime':rlSyslogLogCacheDateTime,'rlSyslogLogCacheAppMnemonic':rlSyslogLogCacheAppMnemonic,'rlSyslogLogCacheSeverity':rlSyslogLogCacheSeverity,'rlSyslogLogCacheMessageMnemonic':rlSyslogLogCacheMessageMnemonic,'rlSyslogLogCacheText1':rlSyslogLogCacheText1,'rlSyslogLogCacheText2':rlSyslogLogCacheText2,'rlSyslogLogCacheText3':rlSyslogLogCacheText3,'rlSyslogLogCacheText4':rlSyslogLogCacheText4,'rlSyslogConsoleMessagesIgnored':rlSyslogConsoleMessagesIgnored,'rlSyslogFileMessagesIgnored':rlSyslogFileMessagesIgnored,'rlSyslogFileMessagesLogged':rlSyslogFileMessagesLogged,'rlSyslogCacheTotalMessages':rlSyslogCacheTotalMessages,'rlSyslogAggregationEnable':rlSyslogAggregationEnable,'rlSyslogAggregationAgingTime':rlSyslogAggregationAgingTime,'rlSyslogMinLogToWebSeverity':rlSyslogMinLogToWebSeverity,'rlSyslogAlarmFlag':rlSyslogAlarmFlag,'rlSyslogOriginId':rlSyslogOriginId,'rlSyslogOriginIdString':rlSyslogOriginIdString,'rlSyslogHeaderSendingEnabled':rlSyslogHeaderSendingEnabled,'rlSyslogCountersPerSeverityTable':rlSyslogCountersPerSeverityTable,'rlSyslogCountersPerSeverityEntry':rlSyslogCountersPerSeverityEntry,_L:rlSyslogCountersPerSeverityIndex,'rlSyslogCountersPerSeverityEmergencyCounter':rlSyslogCountersPerSeverityEmergencyCounter,'rlSyslogCountersPerSeverityAlertCounter':rlSyslogCountersPerSeverityAlertCounter,'rlSyslogCountersPerSeverityCriticalCounter':rlSyslogCountersPerSeverityCriticalCounter,'rlSyslogCountersPerSeverityErrorCounter':rlSyslogCountersPerSeverityErrorCounter,'rlSyslogCountersPerSeverityWarningCounter':rlSyslogCountersPerSeverityWarningCounter,'rlSyslogCountersPerSeverityNoticeCounter':rlSyslogCountersPerSeverityNoticeCounter,'rlSyslogCountersPerSeverityInfoCounter':rlSyslogCountersPerSeverityInfoCounter,'rlSyslogCountersPerSeverityDebugCounter':rlSyslogCountersPerSeverityDebugCounter,'rlSyslogPhaseOneTests':rlSyslogPhaseOneTests,'rlSyslogPhaseOneTestGenerator':rlSyslogPhaseOneTestGenerator})