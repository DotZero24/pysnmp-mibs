_m='myLogHisStampsMIBGroup'
_l='myLogMIBGroup'
_k='myLogHisStamps'
_j='myLogSyslogSendSrcIp'
_i='myLogSyslogSendSrcIfindex'
_h='myLogSyslogServerIpStatus'
_g='myLogSyslogSeverity'
_f='myLogSyslogFacility'
_e='myLogSyslogRelayGlobalStatus'
_d='myLogTimeStampGlobalStatus'
_c='myLogSequenceGlobalStatus'
_b='myLogHisTime'
_a='myLogHisDescription'
_Z='myLogHisMsgName'
_Y='myLogHisSeverity'
_X='myLogHisRecordMaxNum'
_W='myLogClearBuffer'
_V='myLogSendBufferMaxSeverity'
_U='myLogSendBufferStatus'
_T='myLogFileMaxSize'
_S='myLogFileMaxSeverity'
_R='myLogSaveFileName'
_Q='myLogSendMonitorMaxSeverity'
_P='myLogSendMonitorStatus'
_O='myLogSendConsoleMaxSeverity'
_N='myLogSendConsoleStatus'
_M='myLogGlobalStatus'
_L='LogSyslogFacility'
_K='LogTimeStamp'
_J='Integer32'
_I='myLogSyslogServerIpAddr'
_H='myLogHisIndex'
_G='DisplayString'
_F='LogSeverity'
_E='EnabledStatus'
_D='read-only'
_C='read-write'
_B='DES7200-LOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ConfigStatus,IfIndex,MyTrapType=mibBuilder.importSymbols('DES7200-TC','ConfigStatus','IfIndex','MyTrapType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
myLogMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,4))
if mibBuilder.loadTexts:myLogMIB.setRevisions(('2002-03-20 00:00',))
class LogSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7)))
class LogTimeStamp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('datetime',2),('uptime',3)))
class LogSyslogFacility(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('kernel',0),('user',1),('mail',2),('system',3),('security',4),('syslogd',5),('lineprinter',6),('network',7),('uUCP',8),('clockdaemon',9),('authorization',10),('fTP',11),('nTP',12),('logaudit',13),('logalert',14),('clockdaemon2',15),('localuse0',16),('localuse1',17),('localuse2',18),('localuse3',19),('localuse4',20),('localuse5',21),('localuse6',22),('localuse7',23)))
_MyLogMIBObjects_ObjectIdentity=ObjectIdentity
myLogMIBObjects=_MyLogMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,4,1))
class _MyLogGlobalStatus_Type(EnabledStatus):defaultValue=1
_MyLogGlobalStatus_Type.__name__=_E
_MyLogGlobalStatus_Object=MibScalar
myLogGlobalStatus=_MyLogGlobalStatus_Object((1,3,6,1,4,1,171,10,97,2,4,1,1),_MyLogGlobalStatus_Type())
myLogGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogGlobalStatus.setStatus(_A)
class _MyLogSendConsoleStatus_Type(EnabledStatus):defaultValue=1
_MyLogSendConsoleStatus_Type.__name__=_E
_MyLogSendConsoleStatus_Object=MibScalar
myLogSendConsoleStatus=_MyLogSendConsoleStatus_Object((1,3,6,1,4,1,171,10,97,2,4,1,2),_MyLogSendConsoleStatus_Type())
myLogSendConsoleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogSendConsoleStatus.setStatus(_A)
class _MyLogSendConsoleMaxSeverity_Type(LogSeverity):defaultValue=7
_MyLogSendConsoleMaxSeverity_Type.__name__=_F
_MyLogSendConsoleMaxSeverity_Object=MibScalar
myLogSendConsoleMaxSeverity=_MyLogSendConsoleMaxSeverity_Object((1,3,6,1,4,1,171,10,97,2,4,1,3),_MyLogSendConsoleMaxSeverity_Type())
myLogSendConsoleMaxSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogSendConsoleMaxSeverity.setStatus(_A)
class _MyLogSendMonitorStatus_Type(EnabledStatus):defaultValue=2
_MyLogSendMonitorStatus_Type.__name__=_E
_MyLogSendMonitorStatus_Object=MibScalar
myLogSendMonitorStatus=_MyLogSendMonitorStatus_Object((1,3,6,1,4,1,171,10,97,2,4,1,4),_MyLogSendMonitorStatus_Type())
myLogSendMonitorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogSendMonitorStatus.setStatus(_A)
class _MyLogSendMonitorMaxSeverity_Type(LogSeverity):defaultValue=7
_MyLogSendMonitorMaxSeverity_Type.__name__=_F
_MyLogSendMonitorMaxSeverity_Object=MibScalar
myLogSendMonitorMaxSeverity=_MyLogSendMonitorMaxSeverity_Object((1,3,6,1,4,1,171,10,97,2,4,1,5),_MyLogSendMonitorMaxSeverity_Type())
myLogSendMonitorMaxSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogSendMonitorMaxSeverity.setStatus(_A)
class _MyLogSaveFileName_Type(DisplayString):defaultValue=OctetString('')
_MyLogSaveFileName_Type.__name__=_G
_MyLogSaveFileName_Object=MibScalar
myLogSaveFileName=_MyLogSaveFileName_Object((1,3,6,1,4,1,171,10,97,2,4,1,6),_MyLogSaveFileName_Type())
myLogSaveFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogSaveFileName.setStatus(_A)
class _MyLogFileMaxSeverity_Type(LogSeverity):defaultValue=5
_MyLogFileMaxSeverity_Type.__name__=_F
_MyLogFileMaxSeverity_Object=MibScalar
myLogFileMaxSeverity=_MyLogFileMaxSeverity_Object((1,3,6,1,4,1,171,10,97,2,4,1,7),_MyLogFileMaxSeverity_Type())
myLogFileMaxSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogFileMaxSeverity.setStatus(_A)
class _MyLogFileMaxSize_Type(Integer32):defaultValue=4096;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4096,2000000))
_MyLogFileMaxSize_Type.__name__=_J
_MyLogFileMaxSize_Object=MibScalar
myLogFileMaxSize=_MyLogFileMaxSize_Object((1,3,6,1,4,1,171,10,97,2,4,1,8),_MyLogFileMaxSize_Type())
myLogFileMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogFileMaxSize.setStatus(_A)
class _MyLogSendBufferStatus_Type(EnabledStatus):defaultValue=1
_MyLogSendBufferStatus_Type.__name__=_E
_MyLogSendBufferStatus_Object=MibScalar
myLogSendBufferStatus=_MyLogSendBufferStatus_Object((1,3,6,1,4,1,171,10,97,2,4,1,9),_MyLogSendBufferStatus_Type())
myLogSendBufferStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogSendBufferStatus.setStatus(_A)
class _MyLogSendBufferMaxSeverity_Type(LogSeverity):defaultValue=7
_MyLogSendBufferMaxSeverity_Type.__name__=_F
_MyLogSendBufferMaxSeverity_Object=MibScalar
myLogSendBufferMaxSeverity=_MyLogSendBufferMaxSeverity_Object((1,3,6,1,4,1,171,10,97,2,4,1,10),_MyLogSendBufferMaxSeverity_Type())
myLogSendBufferMaxSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogSendBufferMaxSeverity.setStatus(_A)
_MyLogClearBuffer_Type=Integer32
_MyLogClearBuffer_Object=MibScalar
myLogClearBuffer=_MyLogClearBuffer_Object((1,3,6,1,4,1,171,10,97,2,4,1,11),_MyLogClearBuffer_Type())
myLogClearBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogClearBuffer.setStatus(_A)
_MyLogHisRecordMaxNum_Type=Integer32
_MyLogHisRecordMaxNum_Object=MibScalar
myLogHisRecordMaxNum=_MyLogHisRecordMaxNum_Object((1,3,6,1,4,1,171,10,97,2,4,1,12),_MyLogHisRecordMaxNum_Type())
myLogHisRecordMaxNum.setMaxAccess(_D)
if mibBuilder.loadTexts:myLogHisRecordMaxNum.setStatus(_A)
_MyLogHisTable_Object=MibTable
myLogHisTable=_MyLogHisTable_Object((1,3,6,1,4,1,171,10,97,2,4,1,13))
if mibBuilder.loadTexts:myLogHisTable.setStatus(_A)
_MyLogHisEntry_Object=MibTableRow
myLogHisEntry=_MyLogHisEntry_Object((1,3,6,1,4,1,171,10,97,2,4,1,13,1))
myLogHisEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:myLogHisEntry.setStatus(_A)
_MyLogHisIndex_Type=Integer32
_MyLogHisIndex_Object=MibTableColumn
myLogHisIndex=_MyLogHisIndex_Object((1,3,6,1,4,1,171,10,97,2,4,1,13,1,1),_MyLogHisIndex_Type())
myLogHisIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:myLogHisIndex.setStatus(_A)
_MyLogHisSeverity_Type=LogSeverity
_MyLogHisSeverity_Object=MibTableColumn
myLogHisSeverity=_MyLogHisSeverity_Object((1,3,6,1,4,1,171,10,97,2,4,1,13,1,2),_MyLogHisSeverity_Type())
myLogHisSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:myLogHisSeverity.setStatus(_A)
class _MyLogHisMsgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_MyLogHisMsgName_Type.__name__=_G
_MyLogHisMsgName_Object=MibTableColumn
myLogHisMsgName=_MyLogHisMsgName_Object((1,3,6,1,4,1,171,10,97,2,4,1,13,1,3),_MyLogHisMsgName_Type())
myLogHisMsgName.setMaxAccess(_D)
if mibBuilder.loadTexts:myLogHisMsgName.setStatus(_A)
class _MyLogHisDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_MyLogHisDescription_Type.__name__=_G
_MyLogHisDescription_Object=MibTableColumn
myLogHisDescription=_MyLogHisDescription_Object((1,3,6,1,4,1,171,10,97,2,4,1,13,1,4),_MyLogHisDescription_Type())
myLogHisDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:myLogHisDescription.setStatus(_A)
_MyLogHisTime_Type=DateAndTime
_MyLogHisTime_Object=MibTableColumn
myLogHisTime=_MyLogHisTime_Object((1,3,6,1,4,1,171,10,97,2,4,1,13,1,5),_MyLogHisTime_Type())
myLogHisTime.setMaxAccess(_D)
if mibBuilder.loadTexts:myLogHisTime.setStatus(_A)
_MyLogHisStamps_Type=TimeStamp
_MyLogHisStamps_Object=MibTableColumn
myLogHisStamps=_MyLogHisStamps_Object((1,3,6,1,4,1,171,10,97,2,4,1,13,1,6),_MyLogHisStamps_Type())
myLogHisStamps.setMaxAccess(_D)
if mibBuilder.loadTexts:myLogHisStamps.setStatus(_A)
class _MyLogSequenceGlobalStatus_Type(EnabledStatus):defaultValue=2
_MyLogSequenceGlobalStatus_Type.__name__=_E
_MyLogSequenceGlobalStatus_Object=MibScalar
myLogSequenceGlobalStatus=_MyLogSequenceGlobalStatus_Object((1,3,6,1,4,1,171,10,97,2,4,1,14),_MyLogSequenceGlobalStatus_Type())
myLogSequenceGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogSequenceGlobalStatus.setStatus(_A)
class _MyLogTimeStampGlobalStatus_Type(LogTimeStamp):defaultValue=2
_MyLogTimeStampGlobalStatus_Type.__name__=_K
_MyLogTimeStampGlobalStatus_Object=MibScalar
myLogTimeStampGlobalStatus=_MyLogTimeStampGlobalStatus_Object((1,3,6,1,4,1,171,10,97,2,4,1,15),_MyLogTimeStampGlobalStatus_Type())
myLogTimeStampGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogTimeStampGlobalStatus.setStatus(_A)
class _MyLogSyslogRelayGlobalStatus_Type(EnabledStatus):defaultValue=2
_MyLogSyslogRelayGlobalStatus_Type.__name__=_E
_MyLogSyslogRelayGlobalStatus_Object=MibScalar
myLogSyslogRelayGlobalStatus=_MyLogSyslogRelayGlobalStatus_Object((1,3,6,1,4,1,171,10,97,2,4,1,16),_MyLogSyslogRelayGlobalStatus_Type())
myLogSyslogRelayGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogSyslogRelayGlobalStatus.setStatus(_A)
class _MyLogSyslogFacility_Type(LogSyslogFacility):defaultValue=23
_MyLogSyslogFacility_Type.__name__=_L
_MyLogSyslogFacility_Object=MibScalar
myLogSyslogFacility=_MyLogSyslogFacility_Object((1,3,6,1,4,1,171,10,97,2,4,1,17),_MyLogSyslogFacility_Type())
myLogSyslogFacility.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogSyslogFacility.setStatus(_A)
class _MyLogSyslogSeverity_Type(LogSeverity):defaultValue=7
_MyLogSyslogSeverity_Type.__name__=_F
_MyLogSyslogSeverity_Object=MibScalar
myLogSyslogSeverity=_MyLogSyslogSeverity_Object((1,3,6,1,4,1,171,10,97,2,4,1,18),_MyLogSyslogSeverity_Type())
myLogSyslogSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogSyslogSeverity.setStatus(_A)
_MyLogSyslogServerTable_Object=MibTable
myLogSyslogServerTable=_MyLogSyslogServerTable_Object((1,3,6,1,4,1,171,10,97,2,4,1,19))
if mibBuilder.loadTexts:myLogSyslogServerTable.setStatus(_A)
_MyLogSyslogServerEntry_Object=MibTableRow
myLogSyslogServerEntry=_MyLogSyslogServerEntry_Object((1,3,6,1,4,1,171,10,97,2,4,1,19,1))
myLogSyslogServerEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:myLogSyslogServerEntry.setStatus(_A)
_MyLogSyslogServerIpAddr_Type=IpAddress
_MyLogSyslogServerIpAddr_Object=MibTableColumn
myLogSyslogServerIpAddr=_MyLogSyslogServerIpAddr_Object((1,3,6,1,4,1,171,10,97,2,4,1,19,1,1),_MyLogSyslogServerIpAddr_Type())
myLogSyslogServerIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:myLogSyslogServerIpAddr.setStatus(_A)
_MyLogSyslogServerIpStatus_Type=ConfigStatus
_MyLogSyslogServerIpStatus_Object=MibTableColumn
myLogSyslogServerIpStatus=_MyLogSyslogServerIpStatus_Object((1,3,6,1,4,1,171,10,97,2,4,1,19,1,2),_MyLogSyslogServerIpStatus_Type())
myLogSyslogServerIpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogSyslogServerIpStatus.setStatus(_A)
_MyLogSyslogSendSrcIfindex_Type=IfIndex
_MyLogSyslogSendSrcIfindex_Object=MibScalar
myLogSyslogSendSrcIfindex=_MyLogSyslogSendSrcIfindex_Object((1,3,6,1,4,1,171,10,97,2,4,1,20),_MyLogSyslogSendSrcIfindex_Type())
myLogSyslogSendSrcIfindex.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogSyslogSendSrcIfindex.setStatus(_A)
_MyLogSyslogSendSrcIp_Type=IpAddress
_MyLogSyslogSendSrcIp_Object=MibScalar
myLogSyslogSendSrcIp=_MyLogSyslogSendSrcIp_Object((1,3,6,1,4,1,171,10,97,2,4,1,21),_MyLogSyslogSendSrcIp_Type())
myLogSyslogSendSrcIp.setMaxAccess(_C)
if mibBuilder.loadTexts:myLogSyslogSendSrcIp.setStatus(_A)
_MyLogMIBConformance_ObjectIdentity=ObjectIdentity
myLogMIBConformance=_MyLogMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,4,4))
_MyLogMIBCompliances_ObjectIdentity=ObjectIdentity
myLogMIBCompliances=_MyLogMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,4,4,1))
_MyLogMIBGroups_ObjectIdentity=ObjectIdentity
myLogMIBGroups=_MyLogMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,4,4,2))
myLogMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,4,4,2,1))
myLogMIBGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_H),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_I),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:myLogMIBGroup.setStatus(_A)
myLogHisStampsMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,4,4,2,2))
myLogHisStampsMIBGroup.setObjects((_B,_k))
if mibBuilder.loadTexts:myLogHisStampsMIBGroup.setStatus(_A)
myLogMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,4,4,1,1))
myLogMIBCompliance.setObjects(*((_B,_l),(_B,_m)))
if mibBuilder.loadTexts:myLogMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_F:LogSeverity,_K:LogTimeStamp,_L:LogSyslogFacility,'myLogMIB':myLogMIB,'myLogMIBObjects':myLogMIBObjects,_M:myLogGlobalStatus,_N:myLogSendConsoleStatus,_O:myLogSendConsoleMaxSeverity,_P:myLogSendMonitorStatus,_Q:myLogSendMonitorMaxSeverity,_R:myLogSaveFileName,_S:myLogFileMaxSeverity,_T:myLogFileMaxSize,_U:myLogSendBufferStatus,_V:myLogSendBufferMaxSeverity,_W:myLogClearBuffer,_X:myLogHisRecordMaxNum,'myLogHisTable':myLogHisTable,'myLogHisEntry':myLogHisEntry,_H:myLogHisIndex,_Y:myLogHisSeverity,_Z:myLogHisMsgName,_a:myLogHisDescription,_b:myLogHisTime,_k:myLogHisStamps,_c:myLogSequenceGlobalStatus,_d:myLogTimeStampGlobalStatus,_e:myLogSyslogRelayGlobalStatus,_f:myLogSyslogFacility,_g:myLogSyslogSeverity,'myLogSyslogServerTable':myLogSyslogServerTable,'myLogSyslogServerEntry':myLogSyslogServerEntry,_I:myLogSyslogServerIpAddr,_h:myLogSyslogServerIpStatus,_i:myLogSyslogSendSrcIfindex,_j:myLogSyslogSendSrcIp,'myLogMIBConformance':myLogMIBConformance,'myLogMIBCompliances':myLogMIBCompliances,'myLogMIBCompliance':myLogMIBCompliance,'myLogMIBGroups':myLogMIBGroups,_l:myLogMIBGroup,_m:myLogHisStampsMIBGroup})