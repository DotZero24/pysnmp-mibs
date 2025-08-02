_m='qtechLogHisStampsMIBGroup'
_l='qtechLogMIBGroup'
_k='qtechLogHisStamps'
_j='qtechLogSyslogSendSrcIp'
_i='qtechLogSyslogSendSrcIfindex'
_h='qtechLogSyslogServerIpStatus'
_g='qtechLogSyslogSeverity'
_f='qtechLogSyslogFacility'
_e='qtechLogSyslogRelayGlobalStatus'
_d='qtechLogTimeStampGlobalStatus'
_c='qtechLogSequenceGlobalStatus'
_b='qtechLogHisTime'
_a='qtechLogHisDescription'
_Z='qtechLogHisMsgName'
_Y='qtechLogHisSeverity'
_X='qtechLogHisRecordMaxNum'
_W='qtechLogClearBuffer'
_V='qtechLogSendBufferMaxSeverity'
_U='qtechLogSendBufferStatus'
_T='qtechLogFileMaxSize'
_S='qtechLogFileMaxSeverity'
_R='qtechLogSaveFileName'
_Q='qtechLogSendMonitorMaxSeverity'
_P='qtechLogSendMonitorStatus'
_O='qtechLogSendConsoleMaxSeverity'
_N='qtechLogSendConsoleStatus'
_M='qtechLogGlobalStatus'
_L='LogSyslogFacility'
_K='LogTimeStamp'
_J='Integer32'
_I='qtechLogSyslogServerIpAddr'
_H='qtechLogHisIndex'
_G='DisplayString'
_F='LogSeverity'
_E='EnabledStatus'
_D='read-only'
_C='read-write'
_B='QTECH-LOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_E)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('QTECH-TC','ConfigStatus','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'PhysAddress','TextualConvention','TimeStamp')
qtechLogMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,4))
if mibBuilder.loadTexts:qtechLogMIB.setRevisions(('2002-03-20 00:00',))
class LogSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7)))
class LogTimeStamp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('datetime',2),('uptime',3)))
class LogSyslogFacility(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('kernel',0),('user',1),('mail',2),('system',3),('security',4),('syslogd',5),('lineprinter',6),('network',7),('uUCP',8),('clockdaemon',9),('authorization',10),('fTP',11),('nTP',12),('logaudit',13),('logalert',14),('clockdaemon2',15),('localuse0',16),('localuse1',17),('localuse2',18),('localuse3',19),('localuse4',20),('localuse5',21),('localuse6',22),('localuse7',23)))
_QtechLogMIBObjects_ObjectIdentity=ObjectIdentity
qtechLogMIBObjects=_QtechLogMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,4,1))
class _QtechLogGlobalStatus_Type(EnabledStatus):defaultValue=1
_QtechLogGlobalStatus_Type.__name__=_E
_QtechLogGlobalStatus_Object=MibScalar
qtechLogGlobalStatus=_QtechLogGlobalStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,1),_QtechLogGlobalStatus_Type())
qtechLogGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogGlobalStatus.setStatus(_A)
class _QtechLogSendConsoleStatus_Type(EnabledStatus):defaultValue=1
_QtechLogSendConsoleStatus_Type.__name__=_E
_QtechLogSendConsoleStatus_Object=MibScalar
qtechLogSendConsoleStatus=_QtechLogSendConsoleStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,2),_QtechLogSendConsoleStatus_Type())
qtechLogSendConsoleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogSendConsoleStatus.setStatus(_A)
class _QtechLogSendConsoleMaxSeverity_Type(LogSeverity):defaultValue=7
_QtechLogSendConsoleMaxSeverity_Type.__name__=_F
_QtechLogSendConsoleMaxSeverity_Object=MibScalar
qtechLogSendConsoleMaxSeverity=_QtechLogSendConsoleMaxSeverity_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,3),_QtechLogSendConsoleMaxSeverity_Type())
qtechLogSendConsoleMaxSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogSendConsoleMaxSeverity.setStatus(_A)
class _QtechLogSendMonitorStatus_Type(EnabledStatus):defaultValue=2
_QtechLogSendMonitorStatus_Type.__name__=_E
_QtechLogSendMonitorStatus_Object=MibScalar
qtechLogSendMonitorStatus=_QtechLogSendMonitorStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,4),_QtechLogSendMonitorStatus_Type())
qtechLogSendMonitorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogSendMonitorStatus.setStatus(_A)
class _QtechLogSendMonitorMaxSeverity_Type(LogSeverity):defaultValue=7
_QtechLogSendMonitorMaxSeverity_Type.__name__=_F
_QtechLogSendMonitorMaxSeverity_Object=MibScalar
qtechLogSendMonitorMaxSeverity=_QtechLogSendMonitorMaxSeverity_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,5),_QtechLogSendMonitorMaxSeverity_Type())
qtechLogSendMonitorMaxSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogSendMonitorMaxSeverity.setStatus(_A)
class _QtechLogSaveFileName_Type(DisplayString):defaultValue=OctetString('')
_QtechLogSaveFileName_Type.__name__=_G
_QtechLogSaveFileName_Object=MibScalar
qtechLogSaveFileName=_QtechLogSaveFileName_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,6),_QtechLogSaveFileName_Type())
qtechLogSaveFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogSaveFileName.setStatus(_A)
class _QtechLogFileMaxSeverity_Type(LogSeverity):defaultValue=5
_QtechLogFileMaxSeverity_Type.__name__=_F
_QtechLogFileMaxSeverity_Object=MibScalar
qtechLogFileMaxSeverity=_QtechLogFileMaxSeverity_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,7),_QtechLogFileMaxSeverity_Type())
qtechLogFileMaxSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogFileMaxSeverity.setStatus(_A)
class _QtechLogFileMaxSize_Type(Integer32):defaultValue=4096;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4096,2000000))
_QtechLogFileMaxSize_Type.__name__=_J
_QtechLogFileMaxSize_Object=MibScalar
qtechLogFileMaxSize=_QtechLogFileMaxSize_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,8),_QtechLogFileMaxSize_Type())
qtechLogFileMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogFileMaxSize.setStatus(_A)
class _QtechLogSendBufferStatus_Type(EnabledStatus):defaultValue=1
_QtechLogSendBufferStatus_Type.__name__=_E
_QtechLogSendBufferStatus_Object=MibScalar
qtechLogSendBufferStatus=_QtechLogSendBufferStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,9),_QtechLogSendBufferStatus_Type())
qtechLogSendBufferStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogSendBufferStatus.setStatus(_A)
class _QtechLogSendBufferMaxSeverity_Type(LogSeverity):defaultValue=7
_QtechLogSendBufferMaxSeverity_Type.__name__=_F
_QtechLogSendBufferMaxSeverity_Object=MibScalar
qtechLogSendBufferMaxSeverity=_QtechLogSendBufferMaxSeverity_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,10),_QtechLogSendBufferMaxSeverity_Type())
qtechLogSendBufferMaxSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogSendBufferMaxSeverity.setStatus(_A)
_QtechLogClearBuffer_Type=Integer32
_QtechLogClearBuffer_Object=MibScalar
qtechLogClearBuffer=_QtechLogClearBuffer_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,11),_QtechLogClearBuffer_Type())
qtechLogClearBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogClearBuffer.setStatus(_A)
_QtechLogHisRecordMaxNum_Type=Integer32
_QtechLogHisRecordMaxNum_Object=MibScalar
qtechLogHisRecordMaxNum=_QtechLogHisRecordMaxNum_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,12),_QtechLogHisRecordMaxNum_Type())
qtechLogHisRecordMaxNum.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLogHisRecordMaxNum.setStatus(_A)
_QtechLogHisTable_Object=MibTable
qtechLogHisTable=_QtechLogHisTable_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,13))
if mibBuilder.loadTexts:qtechLogHisTable.setStatus(_A)
_QtechLogHisEntry_Object=MibTableRow
qtechLogHisEntry=_QtechLogHisEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,13,1))
qtechLogHisEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:qtechLogHisEntry.setStatus(_A)
_QtechLogHisIndex_Type=Integer32
_QtechLogHisIndex_Object=MibTableColumn
qtechLogHisIndex=_QtechLogHisIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,13,1,1),_QtechLogHisIndex_Type())
qtechLogHisIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLogHisIndex.setStatus(_A)
_QtechLogHisSeverity_Type=LogSeverity
_QtechLogHisSeverity_Object=MibTableColumn
qtechLogHisSeverity=_QtechLogHisSeverity_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,13,1,2),_QtechLogHisSeverity_Type())
qtechLogHisSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLogHisSeverity.setStatus(_A)
class _QtechLogHisMsgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_QtechLogHisMsgName_Type.__name__=_G
_QtechLogHisMsgName_Object=MibTableColumn
qtechLogHisMsgName=_QtechLogHisMsgName_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,13,1,3),_QtechLogHisMsgName_Type())
qtechLogHisMsgName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLogHisMsgName.setStatus(_A)
class _QtechLogHisDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_QtechLogHisDescription_Type.__name__=_G
_QtechLogHisDescription_Object=MibTableColumn
qtechLogHisDescription=_QtechLogHisDescription_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,13,1,4),_QtechLogHisDescription_Type())
qtechLogHisDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLogHisDescription.setStatus(_A)
_QtechLogHisTime_Type=DateAndTime
_QtechLogHisTime_Object=MibTableColumn
qtechLogHisTime=_QtechLogHisTime_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,13,1,5),_QtechLogHisTime_Type())
qtechLogHisTime.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLogHisTime.setStatus(_A)
_QtechLogHisStamps_Type=TimeStamp
_QtechLogHisStamps_Object=MibTableColumn
qtechLogHisStamps=_QtechLogHisStamps_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,13,1,6),_QtechLogHisStamps_Type())
qtechLogHisStamps.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLogHisStamps.setStatus(_A)
class _QtechLogSequenceGlobalStatus_Type(EnabledStatus):defaultValue=2
_QtechLogSequenceGlobalStatus_Type.__name__=_E
_QtechLogSequenceGlobalStatus_Object=MibScalar
qtechLogSequenceGlobalStatus=_QtechLogSequenceGlobalStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,14),_QtechLogSequenceGlobalStatus_Type())
qtechLogSequenceGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogSequenceGlobalStatus.setStatus(_A)
class _QtechLogTimeStampGlobalStatus_Type(LogTimeStamp):defaultValue=2
_QtechLogTimeStampGlobalStatus_Type.__name__=_K
_QtechLogTimeStampGlobalStatus_Object=MibScalar
qtechLogTimeStampGlobalStatus=_QtechLogTimeStampGlobalStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,15),_QtechLogTimeStampGlobalStatus_Type())
qtechLogTimeStampGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogTimeStampGlobalStatus.setStatus(_A)
class _QtechLogSyslogRelayGlobalStatus_Type(EnabledStatus):defaultValue=2
_QtechLogSyslogRelayGlobalStatus_Type.__name__=_E
_QtechLogSyslogRelayGlobalStatus_Object=MibScalar
qtechLogSyslogRelayGlobalStatus=_QtechLogSyslogRelayGlobalStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,16),_QtechLogSyslogRelayGlobalStatus_Type())
qtechLogSyslogRelayGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogSyslogRelayGlobalStatus.setStatus(_A)
class _QtechLogSyslogFacility_Type(LogSyslogFacility):defaultValue=23
_QtechLogSyslogFacility_Type.__name__=_L
_QtechLogSyslogFacility_Object=MibScalar
qtechLogSyslogFacility=_QtechLogSyslogFacility_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,17),_QtechLogSyslogFacility_Type())
qtechLogSyslogFacility.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogSyslogFacility.setStatus(_A)
class _QtechLogSyslogSeverity_Type(LogSeverity):defaultValue=7
_QtechLogSyslogSeverity_Type.__name__=_F
_QtechLogSyslogSeverity_Object=MibScalar
qtechLogSyslogSeverity=_QtechLogSyslogSeverity_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,18),_QtechLogSyslogSeverity_Type())
qtechLogSyslogSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogSyslogSeverity.setStatus(_A)
_QtechLogSyslogServerTable_Object=MibTable
qtechLogSyslogServerTable=_QtechLogSyslogServerTable_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,19))
if mibBuilder.loadTexts:qtechLogSyslogServerTable.setStatus(_A)
_QtechLogSyslogServerEntry_Object=MibTableRow
qtechLogSyslogServerEntry=_QtechLogSyslogServerEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,19,1))
qtechLogSyslogServerEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:qtechLogSyslogServerEntry.setStatus(_A)
_QtechLogSyslogServerIpAddr_Type=IpAddress
_QtechLogSyslogServerIpAddr_Object=MibTableColumn
qtechLogSyslogServerIpAddr=_QtechLogSyslogServerIpAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,19,1,1),_QtechLogSyslogServerIpAddr_Type())
qtechLogSyslogServerIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLogSyslogServerIpAddr.setStatus(_A)
_QtechLogSyslogServerIpStatus_Type=ConfigStatus
_QtechLogSyslogServerIpStatus_Object=MibTableColumn
qtechLogSyslogServerIpStatus=_QtechLogSyslogServerIpStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,19,1,2),_QtechLogSyslogServerIpStatus_Type())
qtechLogSyslogServerIpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogSyslogServerIpStatus.setStatus(_A)
_QtechLogSyslogSendSrcIfindex_Type=IfIndex
_QtechLogSyslogSendSrcIfindex_Object=MibScalar
qtechLogSyslogSendSrcIfindex=_QtechLogSyslogSendSrcIfindex_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,20),_QtechLogSyslogSendSrcIfindex_Type())
qtechLogSyslogSendSrcIfindex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogSyslogSendSrcIfindex.setStatus(_A)
_QtechLogSyslogSendSrcIp_Type=IpAddress
_QtechLogSyslogSendSrcIp_Object=MibScalar
qtechLogSyslogSendSrcIp=_QtechLogSyslogSendSrcIp_Object((1,3,6,1,4,1,27514,1,1,10,2,4,1,21),_QtechLogSyslogSendSrcIp_Type())
qtechLogSyslogSendSrcIp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLogSyslogSendSrcIp.setStatus(_A)
_QtechLogMIBConformance_ObjectIdentity=ObjectIdentity
qtechLogMIBConformance=_QtechLogMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,4,4))
_QtechLogMIBCompliances_ObjectIdentity=ObjectIdentity
qtechLogMIBCompliances=_QtechLogMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,4,4,1))
_QtechLogMIBGroups_ObjectIdentity=ObjectIdentity
qtechLogMIBGroups=_QtechLogMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,4,4,2))
qtechLogMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,4,4,2,1))
qtechLogMIBGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_H),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_I),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:qtechLogMIBGroup.setStatus(_A)
qtechLogHisStampsMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,4,4,2,2))
qtechLogHisStampsMIBGroup.setObjects((_B,_k))
if mibBuilder.loadTexts:qtechLogHisStampsMIBGroup.setStatus(_A)
qtechLogMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,4,4,1,1))
qtechLogMIBCompliance.setObjects(*((_B,_l),(_B,_m)))
if mibBuilder.loadTexts:qtechLogMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_F:LogSeverity,_K:LogTimeStamp,_L:LogSyslogFacility,'qtechLogMIB':qtechLogMIB,'qtechLogMIBObjects':qtechLogMIBObjects,_M:qtechLogGlobalStatus,_N:qtechLogSendConsoleStatus,_O:qtechLogSendConsoleMaxSeverity,_P:qtechLogSendMonitorStatus,_Q:qtechLogSendMonitorMaxSeverity,_R:qtechLogSaveFileName,_S:qtechLogFileMaxSeverity,_T:qtechLogFileMaxSize,_U:qtechLogSendBufferStatus,_V:qtechLogSendBufferMaxSeverity,_W:qtechLogClearBuffer,_X:qtechLogHisRecordMaxNum,'qtechLogHisTable':qtechLogHisTable,'qtechLogHisEntry':qtechLogHisEntry,_H:qtechLogHisIndex,_Y:qtechLogHisSeverity,_Z:qtechLogHisMsgName,_a:qtechLogHisDescription,_b:qtechLogHisTime,_k:qtechLogHisStamps,_c:qtechLogSequenceGlobalStatus,_d:qtechLogTimeStampGlobalStatus,_e:qtechLogSyslogRelayGlobalStatus,_f:qtechLogSyslogFacility,_g:qtechLogSyslogSeverity,'qtechLogSyslogServerTable':qtechLogSyslogServerTable,'qtechLogSyslogServerEntry':qtechLogSyslogServerEntry,_I:qtechLogSyslogServerIpAddr,_h:qtechLogSyslogServerIpStatus,_i:qtechLogSyslogSendSrcIfindex,_j:qtechLogSyslogSendSrcIp,'qtechLogMIBConformance':qtechLogMIBConformance,'qtechLogMIBCompliances':qtechLogMIBCompliances,'qtechLogMIBCompliance':qtechLogMIBCompliance,'qtechLogMIBGroups':qtechLogMIBGroups,_l:qtechLogMIBGroup,_m:qtechLogHisStampsMIBGroup})