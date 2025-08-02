_M='agentLogMsgPersistentMsgIndex'
_L='agentLogInMemoryMsgIndex'
_K='agentLogHostTableIndex'
_J='not-accessible'
_I='Unsigned32'
_H='FASTPATH-LOGGING-MIB'
_G='read-create'
_F='disable'
_E='enable'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('BROADCOM-REF-MIB','fastPath')
agentInventoryComponentIndex,=mibBuilder.importSymbols('FASTPATH-INVENTORY-MIB','agentInventoryComponentIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
fastPathLogging=ModuleIdentity((1,3,6,1,4,1,4413,1,1,14))
if mibBuilder.loadTexts:fastPathLogging.setRevisions(('2007-05-23 00:00','2004-10-26 13:03'))
class AgentLogFacility(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('kernel',0),('user',1),('mail',2),('system',3),('security',4),('syslog',5),('lpr',6),('nntp',7),('uucp',8),('cron',9),('auth',10),('ftp',11),('ntp',12),('audit',13),('alert',14),('clock',15),('local0',16),('local1',17),('local2',18),('local3',19),('local4',20),('local5',21),('local6',22),('local7',23)))
class AgentLogSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('informational',6),('debug',7)))
_AgentLogConfigGroup_ObjectIdentity=ObjectIdentity
agentLogConfigGroup=_AgentLogConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,14,1))
_AgentLogInMemoryConfigGroup_ObjectIdentity=ObjectIdentity
agentLogInMemoryConfigGroup=_AgentLogInMemoryConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,14,1,1))
class _AgentLogInMemoryAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentLogInMemoryAdminStatus_Type.__name__=_D
_AgentLogInMemoryAdminStatus_Object=MibScalar
agentLogInMemoryAdminStatus=_AgentLogInMemoryAdminStatus_Object((1,3,6,1,4,1,4413,1,1,14,1,1,1),_AgentLogInMemoryAdminStatus_Type())
agentLogInMemoryAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentLogInMemoryAdminStatus.setStatus(_A)
class _AgentLogInMemoryBehavior_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wrap',1),('stop-on-full',2)))
_AgentLogInMemoryBehavior_Type.__name__=_D
_AgentLogInMemoryBehavior_Object=MibScalar
agentLogInMemoryBehavior=_AgentLogInMemoryBehavior_Object((1,3,6,1,4,1,4413,1,1,14,1,1,4),_AgentLogInMemoryBehavior_Type())
agentLogInMemoryBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:agentLogInMemoryBehavior.setStatus(_A)
_AgentLogConsoleConfigGroup_ObjectIdentity=ObjectIdentity
agentLogConsoleConfigGroup=_AgentLogConsoleConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,14,1,2))
class _AgentLogConsoleAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentLogConsoleAdminStatus_Type.__name__=_D
_AgentLogConsoleAdminStatus_Object=MibScalar
agentLogConsoleAdminStatus=_AgentLogConsoleAdminStatus_Object((1,3,6,1,4,1,4413,1,1,14,1,2,1),_AgentLogConsoleAdminStatus_Type())
agentLogConsoleAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentLogConsoleAdminStatus.setStatus(_A)
_AgentLogConsoleSeverityFilter_Type=AgentLogSeverity
_AgentLogConsoleSeverityFilter_Object=MibScalar
agentLogConsoleSeverityFilter=_AgentLogConsoleSeverityFilter_Object((1,3,6,1,4,1,4413,1,1,14,1,2,2),_AgentLogConsoleSeverityFilter_Type())
agentLogConsoleSeverityFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:agentLogConsoleSeverityFilter.setStatus(_A)
_AgentLogPersistentConfigGroup_ObjectIdentity=ObjectIdentity
agentLogPersistentConfigGroup=_AgentLogPersistentConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,14,1,3))
class _AgentLogPersistentAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentLogPersistentAdminStatus_Type.__name__=_D
_AgentLogPersistentAdminStatus_Object=MibScalar
agentLogPersistentAdminStatus=_AgentLogPersistentAdminStatus_Object((1,3,6,1,4,1,4413,1,1,14,1,3,1),_AgentLogPersistentAdminStatus_Type())
agentLogPersistentAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentLogPersistentAdminStatus.setStatus(_A)
_AgentLogPersistentSeverityFilter_Type=AgentLogSeverity
_AgentLogPersistentSeverityFilter_Object=MibScalar
agentLogPersistentSeverityFilter=_AgentLogPersistentSeverityFilter_Object((1,3,6,1,4,1,4413,1,1,14,1,3,2),_AgentLogPersistentSeverityFilter_Type())
agentLogPersistentSeverityFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:agentLogPersistentSeverityFilter.setStatus(_A)
_AgentLogSysLogConfigGroup_ObjectIdentity=ObjectIdentity
agentLogSysLogConfigGroup=_AgentLogSysLogConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,14,1,4))
class _AgentLogSyslogAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentLogSyslogAdminStatus_Type.__name__=_D
_AgentLogSyslogAdminStatus_Object=MibScalar
agentLogSyslogAdminStatus=_AgentLogSyslogAdminStatus_Object((1,3,6,1,4,1,4413,1,1,14,1,4,1),_AgentLogSyslogAdminStatus_Type())
agentLogSyslogAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentLogSyslogAdminStatus.setStatus(_A)
class _AgentLogSyslogLocalPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentLogSyslogLocalPort_Type.__name__=_I
_AgentLogSyslogLocalPort_Object=MibScalar
agentLogSyslogLocalPort=_AgentLogSyslogLocalPort_Object((1,3,6,1,4,1,4413,1,1,14,1,4,3),_AgentLogSyslogLocalPort_Type())
agentLogSyslogLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:agentLogSyslogLocalPort.setStatus(_A)
_AgentLogSyslogMaxHosts_Type=Unsigned32
_AgentLogSyslogMaxHosts_Object=MibScalar
agentLogSyslogMaxHosts=_AgentLogSyslogMaxHosts_Object((1,3,6,1,4,1,4413,1,1,14,1,4,4),_AgentLogSyslogMaxHosts_Type())
agentLogSyslogMaxHosts.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLogSyslogMaxHosts.setStatus(_A)
_AgentLogSyslogHostTable_Object=MibTable
agentLogSyslogHostTable=_AgentLogSyslogHostTable_Object((1,3,6,1,4,1,4413,1,1,14,1,4,5))
if mibBuilder.loadTexts:agentLogSyslogHostTable.setStatus(_A)
_AgentLogSyslogHostEntry_Object=MibTableRow
agentLogSyslogHostEntry=_AgentLogSyslogHostEntry_Object((1,3,6,1,4,1,4413,1,1,14,1,4,5,1))
agentLogSyslogHostEntry.setIndexNames((0,_H,_K))
if mibBuilder.loadTexts:agentLogSyslogHostEntry.setStatus(_A)
_AgentLogHostTableIndex_Type=Unsigned32
_AgentLogHostTableIndex_Object=MibTableColumn
agentLogHostTableIndex=_AgentLogHostTableIndex_Object((1,3,6,1,4,1,4413,1,1,14,1,4,5,1,1),_AgentLogHostTableIndex_Type())
agentLogHostTableIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:agentLogHostTableIndex.setStatus(_A)
_AgentLogHostTableIpAddressType_Type=InetAddressType
_AgentLogHostTableIpAddressType_Object=MibTableColumn
agentLogHostTableIpAddressType=_AgentLogHostTableIpAddressType_Object((1,3,6,1,4,1,4413,1,1,14,1,4,5,1,2),_AgentLogHostTableIpAddressType_Type())
agentLogHostTableIpAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:agentLogHostTableIpAddressType.setStatus(_A)
_AgentLogHostTableIpAddress_Type=InetAddress
_AgentLogHostTableIpAddress_Object=MibTableColumn
agentLogHostTableIpAddress=_AgentLogHostTableIpAddress_Object((1,3,6,1,4,1,4413,1,1,14,1,4,5,1,3),_AgentLogHostTableIpAddress_Type())
agentLogHostTableIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:agentLogHostTableIpAddress.setStatus(_A)
class _AgentLogHostTablePort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentLogHostTablePort_Type.__name__=_I
_AgentLogHostTablePort_Object=MibTableColumn
agentLogHostTablePort=_AgentLogHostTablePort_Object((1,3,6,1,4,1,4413,1,1,14,1,4,5,1,4),_AgentLogHostTablePort_Type())
agentLogHostTablePort.setMaxAccess(_G)
if mibBuilder.loadTexts:agentLogHostTablePort.setStatus(_A)
_AgentLogHostTableSeverityFilter_Type=AgentLogSeverity
_AgentLogHostTableSeverityFilter_Object=MibTableColumn
agentLogHostTableSeverityFilter=_AgentLogHostTableSeverityFilter_Object((1,3,6,1,4,1,4413,1,1,14,1,4,5,1,5),_AgentLogHostTableSeverityFilter_Type())
agentLogHostTableSeverityFilter.setMaxAccess(_G)
if mibBuilder.loadTexts:agentLogHostTableSeverityFilter.setStatus(_A)
_AgentLogHostTableRowStatus_Type=RowStatus
_AgentLogHostTableRowStatus_Object=MibTableColumn
agentLogHostTableRowStatus=_AgentLogHostTableRowStatus_Object((1,3,6,1,4,1,4413,1,1,14,1,4,5,1,7),_AgentLogHostTableRowStatus_Type())
agentLogHostTableRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:agentLogHostTableRowStatus.setStatus(_A)
_AgentLogCliCommandsConfigGroup_ObjectIdentity=ObjectIdentity
agentLogCliCommandsConfigGroup=_AgentLogCliCommandsConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,14,1,5))
class _AgentLogCliCommandsAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentLogCliCommandsAdminStatus_Type.__name__=_D
_AgentLogCliCommandsAdminStatus_Object=MibScalar
agentLogCliCommandsAdminStatus=_AgentLogCliCommandsAdminStatus_Object((1,3,6,1,4,1,4413,1,1,14,1,5,1),_AgentLogCliCommandsAdminStatus_Type())
agentLogCliCommandsAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentLogCliCommandsAdminStatus.setStatus(_A)
_AgentLogStatisticsGroup_ObjectIdentity=ObjectIdentity
agentLogStatisticsGroup=_AgentLogStatisticsGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,14,2))
_AgentLogMessagesReceived_Type=Counter32
_AgentLogMessagesReceived_Object=MibScalar
agentLogMessagesReceived=_AgentLogMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,14,2,1),_AgentLogMessagesReceived_Type())
agentLogMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLogMessagesReceived.setStatus(_A)
_AgentLogMessagesDropped_Type=Counter32
_AgentLogMessagesDropped_Object=MibScalar
agentLogMessagesDropped=_AgentLogMessagesDropped_Object((1,3,6,1,4,1,4413,1,1,14,2,2),_AgentLogMessagesDropped_Type())
agentLogMessagesDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLogMessagesDropped.setStatus(_A)
_AgentLogSyslogMessagesRelayed_Type=Counter32
_AgentLogSyslogMessagesRelayed_Object=MibScalar
agentLogSyslogMessagesRelayed=_AgentLogSyslogMessagesRelayed_Object((1,3,6,1,4,1,4413,1,1,14,2,3),_AgentLogSyslogMessagesRelayed_Type())
agentLogSyslogMessagesRelayed.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLogSyslogMessagesRelayed.setStatus(_A)
_AgentLogSyslogMessagesIgnored_Type=Counter32
_AgentLogSyslogMessagesIgnored_Object=MibScalar
agentLogSyslogMessagesIgnored=_AgentLogSyslogMessagesIgnored_Object((1,3,6,1,4,1,4413,1,1,14,2,4),_AgentLogSyslogMessagesIgnored_Type())
agentLogSyslogMessagesIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLogSyslogMessagesIgnored.setStatus('deprecated')
_AgentLogMessageReceivedTime_Type=DateAndTime
_AgentLogMessageReceivedTime_Object=MibScalar
agentLogMessageReceivedTime=_AgentLogMessageReceivedTime_Object((1,3,6,1,4,1,4413,1,1,14,2,5),_AgentLogMessageReceivedTime_Type())
agentLogMessageReceivedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLogMessageReceivedTime.setStatus(_A)
_AgentLogSyslogMessageDeliveredTime_Type=DateAndTime
_AgentLogSyslogMessageDeliveredTime_Object=MibScalar
agentLogSyslogMessageDeliveredTime=_AgentLogSyslogMessageDeliveredTime_Object((1,3,6,1,4,1,4413,1,1,14,2,6),_AgentLogSyslogMessageDeliveredTime_Type())
agentLogSyslogMessageDeliveredTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLogSyslogMessageDeliveredTime.setStatus(_A)
_AgentLogInMemoryGroup_ObjectIdentity=ObjectIdentity
agentLogInMemoryGroup=_AgentLogInMemoryGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,14,3))
_AgentLogInMemoryLogCount_Type=Gauge32
_AgentLogInMemoryLogCount_Object=MibScalar
agentLogInMemoryLogCount=_AgentLogInMemoryLogCount_Object((1,3,6,1,4,1,4413,1,1,14,3,1),_AgentLogInMemoryLogCount_Type())
agentLogInMemoryLogCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLogInMemoryLogCount.setStatus(_A)
_AgentLogInMemoryTable_Object=MibTable
agentLogInMemoryTable=_AgentLogInMemoryTable_Object((1,3,6,1,4,1,4413,1,1,14,3,2))
if mibBuilder.loadTexts:agentLogInMemoryTable.setStatus(_A)
_AgentLogInMemoryEntry_Object=MibTableRow
agentLogInMemoryEntry=_AgentLogInMemoryEntry_Object((1,3,6,1,4,1,4413,1,1,14,3,2,1))
agentLogInMemoryEntry.setIndexNames((0,_H,_L))
if mibBuilder.loadTexts:agentLogInMemoryEntry.setStatus(_A)
_AgentLogInMemoryMsgIndex_Type=Unsigned32
_AgentLogInMemoryMsgIndex_Object=MibTableColumn
agentLogInMemoryMsgIndex=_AgentLogInMemoryMsgIndex_Object((1,3,6,1,4,1,4413,1,1,14,3,2,1,1),_AgentLogInMemoryMsgIndex_Type())
agentLogInMemoryMsgIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:agentLogInMemoryMsgIndex.setStatus(_A)
_AgentLogInMemoryMsgText_Type=DisplayString
_AgentLogInMemoryMsgText_Object=MibTableColumn
agentLogInMemoryMsgText=_AgentLogInMemoryMsgText_Object((1,3,6,1,4,1,4413,1,1,14,3,2,1,2),_AgentLogInMemoryMsgText_Type())
agentLogInMemoryMsgText.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLogInMemoryMsgText.setStatus(_A)
_AgentLogPersistentGroup_ObjectIdentity=ObjectIdentity
agentLogPersistentGroup=_AgentLogPersistentGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,14,4))
_AgentLogPersistentLogCount_Type=Counter32
_AgentLogPersistentLogCount_Object=MibScalar
agentLogPersistentLogCount=_AgentLogPersistentLogCount_Object((1,3,6,1,4,1,4413,1,1,14,4,1),_AgentLogPersistentLogCount_Type())
agentLogPersistentLogCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLogPersistentLogCount.setStatus(_A)
_AgentLogPersistentTable_Object=MibTable
agentLogPersistentTable=_AgentLogPersistentTable_Object((1,3,6,1,4,1,4413,1,1,14,4,4))
if mibBuilder.loadTexts:agentLogPersistentTable.setStatus(_A)
_AgentLogPersistentEntry_Object=MibTableRow
agentLogPersistentEntry=_AgentLogPersistentEntry_Object((1,3,6,1,4,1,4413,1,1,14,4,4,1))
agentLogPersistentEntry.setIndexNames((0,_H,_M))
if mibBuilder.loadTexts:agentLogPersistentEntry.setStatus(_A)
_AgentLogMsgPersistentMsgIndex_Type=Unsigned32
_AgentLogMsgPersistentMsgIndex_Object=MibTableColumn
agentLogMsgPersistentMsgIndex=_AgentLogMsgPersistentMsgIndex_Object((1,3,6,1,4,1,4413,1,1,14,4,4,1,1),_AgentLogMsgPersistentMsgIndex_Type())
agentLogMsgPersistentMsgIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:agentLogMsgPersistentMsgIndex.setStatus(_A)
_AgentLogMsgPersistentMsgText_Type=DisplayString
_AgentLogMsgPersistentMsgText_Object=MibTableColumn
agentLogMsgPersistentMsgText=_AgentLogMsgPersistentMsgText_Object((1,3,6,1,4,1,4413,1,1,14,4,4,1,2),_AgentLogMsgPersistentMsgText_Type())
agentLogMsgPersistentMsgText.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLogMsgPersistentMsgText.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'AgentLogFacility':AgentLogFacility,'AgentLogSeverity':AgentLogSeverity,'fastPathLogging':fastPathLogging,'agentLogConfigGroup':agentLogConfigGroup,'agentLogInMemoryConfigGroup':agentLogInMemoryConfigGroup,'agentLogInMemoryAdminStatus':agentLogInMemoryAdminStatus,'agentLogInMemoryBehavior':agentLogInMemoryBehavior,'agentLogConsoleConfigGroup':agentLogConsoleConfigGroup,'agentLogConsoleAdminStatus':agentLogConsoleAdminStatus,'agentLogConsoleSeverityFilter':agentLogConsoleSeverityFilter,'agentLogPersistentConfigGroup':agentLogPersistentConfigGroup,'agentLogPersistentAdminStatus':agentLogPersistentAdminStatus,'agentLogPersistentSeverityFilter':agentLogPersistentSeverityFilter,'agentLogSysLogConfigGroup':agentLogSysLogConfigGroup,'agentLogSyslogAdminStatus':agentLogSyslogAdminStatus,'agentLogSyslogLocalPort':agentLogSyslogLocalPort,'agentLogSyslogMaxHosts':agentLogSyslogMaxHosts,'agentLogSyslogHostTable':agentLogSyslogHostTable,'agentLogSyslogHostEntry':agentLogSyslogHostEntry,_K:agentLogHostTableIndex,'agentLogHostTableIpAddressType':agentLogHostTableIpAddressType,'agentLogHostTableIpAddress':agentLogHostTableIpAddress,'agentLogHostTablePort':agentLogHostTablePort,'agentLogHostTableSeverityFilter':agentLogHostTableSeverityFilter,'agentLogHostTableRowStatus':agentLogHostTableRowStatus,'agentLogCliCommandsConfigGroup':agentLogCliCommandsConfigGroup,'agentLogCliCommandsAdminStatus':agentLogCliCommandsAdminStatus,'agentLogStatisticsGroup':agentLogStatisticsGroup,'agentLogMessagesReceived':agentLogMessagesReceived,'agentLogMessagesDropped':agentLogMessagesDropped,'agentLogSyslogMessagesRelayed':agentLogSyslogMessagesRelayed,'agentLogSyslogMessagesIgnored':agentLogSyslogMessagesIgnored,'agentLogMessageReceivedTime':agentLogMessageReceivedTime,'agentLogSyslogMessageDeliveredTime':agentLogSyslogMessageDeliveredTime,'agentLogInMemoryGroup':agentLogInMemoryGroup,'agentLogInMemoryLogCount':agentLogInMemoryLogCount,'agentLogInMemoryTable':agentLogInMemoryTable,'agentLogInMemoryEntry':agentLogInMemoryEntry,_L:agentLogInMemoryMsgIndex,'agentLogInMemoryMsgText':agentLogInMemoryMsgText,'agentLogPersistentGroup':agentLogPersistentGroup,'agentLogPersistentLogCount':agentLogPersistentLogCount,'agentLogPersistentTable':agentLogPersistentTable,'agentLogPersistentEntry':agentLogPersistentEntry,_M:agentLogMsgPersistentMsgIndex,'agentLogMsgPersistentMsgText':agentLogMsgPersistentMsgText})