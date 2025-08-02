_m='fsLogHisStampsMIBGroup'
_l='fsLogMIBGroup'
_k='fsLogHisStamps'
_j='fsLogSyslogSendSrcIp'
_i='fsLogSyslogSendSrcIfindex'
_h='fsLogSyslogServerIpStatus'
_g='fsLogSyslogSeverity'
_f='fsLogSyslogFacility'
_e='fsLogSyslogRelayGlobalStatus'
_d='fsLogTimeStampGlobalStatus'
_c='fsLogSequenceGlobalStatus'
_b='fsLogHisTime'
_a='fsLogHisDescription'
_Z='fsLogHisMsgName'
_Y='fsLogHisSeverity'
_X='fsLogHisRecordMaxNum'
_W='fsLogClearBuffer'
_V='fsLogSendBufferMaxSeverity'
_U='fsLogSendBufferStatus'
_T='fsLogFileMaxSize'
_S='fsLogFileMaxSeverity'
_R='fsLogSaveFileName'
_Q='fsLogSendMonitorMaxSeverity'
_P='fsLogSendMonitorStatus'
_O='fsLogSendConsoleMaxSeverity'
_N='fsLogSendConsoleStatus'
_M='fsLogGlobalStatus'
_L='LogSyslogFacility'
_K='LogTimeStamp'
_J='Integer32'
_I='fsLogSyslogServerIpAddr'
_H='fsLogHisIndex'
_G='DisplayString'
_F='LogSeverity'
_E='EnabledStatus'
_D='read-only'
_C='read-write'
_B='FS-LOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('FS-TC','ConfigStatus','IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'PhysAddress','TextualConvention','TimeStamp')
fsLogMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,4))
if mibBuilder.loadTexts:fsLogMIB.setRevisions(('2002-03-20 00:00',))
class LogSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7)))
class LogTimeStamp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('datetime',2),('uptime',3)))
class LogSyslogFacility(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('kernel',0),('user',1),('mail',2),('system',3),('security',4),('syslogd',5),('lineprinter',6),('network',7),('uUCP',8),('clockdaemon',9),('authorization',10),('fTP',11),('nTP',12),('logaudit',13),('logalert',14),('clockdaemon2',15),('localuse0',16),('localuse1',17),('localuse2',18),('localuse3',19),('localuse4',20),('localuse5',21),('localuse6',22),('localuse7',23)))
_FsLogMIBObjects_ObjectIdentity=ObjectIdentity
fsLogMIBObjects=_FsLogMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,4,1))
class _FsLogGlobalStatus_Type(EnabledStatus):defaultValue=1
_FsLogGlobalStatus_Type.__name__=_E
_FsLogGlobalStatus_Object=MibScalar
fsLogGlobalStatus=_FsLogGlobalStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,1),_FsLogGlobalStatus_Type())
fsLogGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogGlobalStatus.setStatus(_A)
class _FsLogSendConsoleStatus_Type(EnabledStatus):defaultValue=1
_FsLogSendConsoleStatus_Type.__name__=_E
_FsLogSendConsoleStatus_Object=MibScalar
fsLogSendConsoleStatus=_FsLogSendConsoleStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,2),_FsLogSendConsoleStatus_Type())
fsLogSendConsoleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogSendConsoleStatus.setStatus(_A)
class _FsLogSendConsoleMaxSeverity_Type(LogSeverity):defaultValue=7
_FsLogSendConsoleMaxSeverity_Type.__name__=_F
_FsLogSendConsoleMaxSeverity_Object=MibScalar
fsLogSendConsoleMaxSeverity=_FsLogSendConsoleMaxSeverity_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,3),_FsLogSendConsoleMaxSeverity_Type())
fsLogSendConsoleMaxSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogSendConsoleMaxSeverity.setStatus(_A)
class _FsLogSendMonitorStatus_Type(EnabledStatus):defaultValue=2
_FsLogSendMonitorStatus_Type.__name__=_E
_FsLogSendMonitorStatus_Object=MibScalar
fsLogSendMonitorStatus=_FsLogSendMonitorStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,4),_FsLogSendMonitorStatus_Type())
fsLogSendMonitorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogSendMonitorStatus.setStatus(_A)
class _FsLogSendMonitorMaxSeverity_Type(LogSeverity):defaultValue=7
_FsLogSendMonitorMaxSeverity_Type.__name__=_F
_FsLogSendMonitorMaxSeverity_Object=MibScalar
fsLogSendMonitorMaxSeverity=_FsLogSendMonitorMaxSeverity_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,5),_FsLogSendMonitorMaxSeverity_Type())
fsLogSendMonitorMaxSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogSendMonitorMaxSeverity.setStatus(_A)
class _FsLogSaveFileName_Type(DisplayString):defaultValue=OctetString('')
_FsLogSaveFileName_Type.__name__=_G
_FsLogSaveFileName_Object=MibScalar
fsLogSaveFileName=_FsLogSaveFileName_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,6),_FsLogSaveFileName_Type())
fsLogSaveFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogSaveFileName.setStatus(_A)
class _FsLogFileMaxSeverity_Type(LogSeverity):defaultValue=5
_FsLogFileMaxSeverity_Type.__name__=_F
_FsLogFileMaxSeverity_Object=MibScalar
fsLogFileMaxSeverity=_FsLogFileMaxSeverity_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,7),_FsLogFileMaxSeverity_Type())
fsLogFileMaxSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogFileMaxSeverity.setStatus(_A)
class _FsLogFileMaxSize_Type(Integer32):defaultValue=4096;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4096,2000000))
_FsLogFileMaxSize_Type.__name__=_J
_FsLogFileMaxSize_Object=MibScalar
fsLogFileMaxSize=_FsLogFileMaxSize_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,8),_FsLogFileMaxSize_Type())
fsLogFileMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogFileMaxSize.setStatus(_A)
class _FsLogSendBufferStatus_Type(EnabledStatus):defaultValue=1
_FsLogSendBufferStatus_Type.__name__=_E
_FsLogSendBufferStatus_Object=MibScalar
fsLogSendBufferStatus=_FsLogSendBufferStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,9),_FsLogSendBufferStatus_Type())
fsLogSendBufferStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogSendBufferStatus.setStatus(_A)
class _FsLogSendBufferMaxSeverity_Type(LogSeverity):defaultValue=7
_FsLogSendBufferMaxSeverity_Type.__name__=_F
_FsLogSendBufferMaxSeverity_Object=MibScalar
fsLogSendBufferMaxSeverity=_FsLogSendBufferMaxSeverity_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,10),_FsLogSendBufferMaxSeverity_Type())
fsLogSendBufferMaxSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogSendBufferMaxSeverity.setStatus(_A)
_FsLogClearBuffer_Type=Integer32
_FsLogClearBuffer_Object=MibScalar
fsLogClearBuffer=_FsLogClearBuffer_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,11),_FsLogClearBuffer_Type())
fsLogClearBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogClearBuffer.setStatus(_A)
_FsLogHisRecordMaxNum_Type=Integer32
_FsLogHisRecordMaxNum_Object=MibScalar
fsLogHisRecordMaxNum=_FsLogHisRecordMaxNum_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,12),_FsLogHisRecordMaxNum_Type())
fsLogHisRecordMaxNum.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLogHisRecordMaxNum.setStatus(_A)
_FsLogHisTable_Object=MibTable
fsLogHisTable=_FsLogHisTable_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,13))
if mibBuilder.loadTexts:fsLogHisTable.setStatus(_A)
_FsLogHisEntry_Object=MibTableRow
fsLogHisEntry=_FsLogHisEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,13,1))
fsLogHisEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:fsLogHisEntry.setStatus(_A)
_FsLogHisIndex_Type=Integer32
_FsLogHisIndex_Object=MibTableColumn
fsLogHisIndex=_FsLogHisIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,13,1,1),_FsLogHisIndex_Type())
fsLogHisIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLogHisIndex.setStatus(_A)
_FsLogHisSeverity_Type=LogSeverity
_FsLogHisSeverity_Object=MibTableColumn
fsLogHisSeverity=_FsLogHisSeverity_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,13,1,2),_FsLogHisSeverity_Type())
fsLogHisSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLogHisSeverity.setStatus(_A)
class _FsLogHisMsgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_FsLogHisMsgName_Type.__name__=_G
_FsLogHisMsgName_Object=MibTableColumn
fsLogHisMsgName=_FsLogHisMsgName_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,13,1,3),_FsLogHisMsgName_Type())
fsLogHisMsgName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLogHisMsgName.setStatus(_A)
class _FsLogHisDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_FsLogHisDescription_Type.__name__=_G
_FsLogHisDescription_Object=MibTableColumn
fsLogHisDescription=_FsLogHisDescription_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,13,1,4),_FsLogHisDescription_Type())
fsLogHisDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLogHisDescription.setStatus(_A)
_FsLogHisTime_Type=DateAndTime
_FsLogHisTime_Object=MibTableColumn
fsLogHisTime=_FsLogHisTime_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,13,1,5),_FsLogHisTime_Type())
fsLogHisTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLogHisTime.setStatus(_A)
_FsLogHisStamps_Type=TimeStamp
_FsLogHisStamps_Object=MibTableColumn
fsLogHisStamps=_FsLogHisStamps_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,13,1,6),_FsLogHisStamps_Type())
fsLogHisStamps.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLogHisStamps.setStatus(_A)
class _FsLogSequenceGlobalStatus_Type(EnabledStatus):defaultValue=2
_FsLogSequenceGlobalStatus_Type.__name__=_E
_FsLogSequenceGlobalStatus_Object=MibScalar
fsLogSequenceGlobalStatus=_FsLogSequenceGlobalStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,14),_FsLogSequenceGlobalStatus_Type())
fsLogSequenceGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogSequenceGlobalStatus.setStatus(_A)
class _FsLogTimeStampGlobalStatus_Type(LogTimeStamp):defaultValue=2
_FsLogTimeStampGlobalStatus_Type.__name__=_K
_FsLogTimeStampGlobalStatus_Object=MibScalar
fsLogTimeStampGlobalStatus=_FsLogTimeStampGlobalStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,15),_FsLogTimeStampGlobalStatus_Type())
fsLogTimeStampGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogTimeStampGlobalStatus.setStatus(_A)
class _FsLogSyslogRelayGlobalStatus_Type(EnabledStatus):defaultValue=2
_FsLogSyslogRelayGlobalStatus_Type.__name__=_E
_FsLogSyslogRelayGlobalStatus_Object=MibScalar
fsLogSyslogRelayGlobalStatus=_FsLogSyslogRelayGlobalStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,16),_FsLogSyslogRelayGlobalStatus_Type())
fsLogSyslogRelayGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogSyslogRelayGlobalStatus.setStatus(_A)
class _FsLogSyslogFacility_Type(LogSyslogFacility):defaultValue=23
_FsLogSyslogFacility_Type.__name__=_L
_FsLogSyslogFacility_Object=MibScalar
fsLogSyslogFacility=_FsLogSyslogFacility_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,17),_FsLogSyslogFacility_Type())
fsLogSyslogFacility.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogSyslogFacility.setStatus(_A)
class _FsLogSyslogSeverity_Type(LogSeverity):defaultValue=7
_FsLogSyslogSeverity_Type.__name__=_F
_FsLogSyslogSeverity_Object=MibScalar
fsLogSyslogSeverity=_FsLogSyslogSeverity_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,18),_FsLogSyslogSeverity_Type())
fsLogSyslogSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogSyslogSeverity.setStatus(_A)
_FsLogSyslogServerTable_Object=MibTable
fsLogSyslogServerTable=_FsLogSyslogServerTable_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,19))
if mibBuilder.loadTexts:fsLogSyslogServerTable.setStatus(_A)
_FsLogSyslogServerEntry_Object=MibTableRow
fsLogSyslogServerEntry=_FsLogSyslogServerEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,19,1))
fsLogSyslogServerEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:fsLogSyslogServerEntry.setStatus(_A)
_FsLogSyslogServerIpAddr_Type=IpAddress
_FsLogSyslogServerIpAddr_Object=MibTableColumn
fsLogSyslogServerIpAddr=_FsLogSyslogServerIpAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,19,1,1),_FsLogSyslogServerIpAddr_Type())
fsLogSyslogServerIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLogSyslogServerIpAddr.setStatus(_A)
_FsLogSyslogServerIpStatus_Type=ConfigStatus
_FsLogSyslogServerIpStatus_Object=MibTableColumn
fsLogSyslogServerIpStatus=_FsLogSyslogServerIpStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,19,1,2),_FsLogSyslogServerIpStatus_Type())
fsLogSyslogServerIpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogSyslogServerIpStatus.setStatus(_A)
_FsLogSyslogSendSrcIfindex_Type=IfIndex
_FsLogSyslogSendSrcIfindex_Object=MibScalar
fsLogSyslogSendSrcIfindex=_FsLogSyslogSendSrcIfindex_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,20),_FsLogSyslogSendSrcIfindex_Type())
fsLogSyslogSendSrcIfindex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogSyslogSendSrcIfindex.setStatus(_A)
_FsLogSyslogSendSrcIp_Type=IpAddress
_FsLogSyslogSendSrcIp_Object=MibScalar
fsLogSyslogSendSrcIp=_FsLogSyslogSendSrcIp_Object((1,3,6,1,4,1,52642,1,1,10,2,4,1,21),_FsLogSyslogSendSrcIp_Type())
fsLogSyslogSendSrcIp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLogSyslogSendSrcIp.setStatus(_A)
_FsLogMIBConformance_ObjectIdentity=ObjectIdentity
fsLogMIBConformance=_FsLogMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,4,4))
_FsLogMIBCompliances_ObjectIdentity=ObjectIdentity
fsLogMIBCompliances=_FsLogMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,4,4,1))
_FsLogMIBGroups_ObjectIdentity=ObjectIdentity
fsLogMIBGroups=_FsLogMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,4,4,2))
fsLogMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,4,4,2,1))
fsLogMIBGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_H),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_I),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:fsLogMIBGroup.setStatus(_A)
fsLogHisStampsMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,4,4,2,2))
fsLogHisStampsMIBGroup.setObjects((_B,_k))
if mibBuilder.loadTexts:fsLogHisStampsMIBGroup.setStatus(_A)
fsLogMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,4,4,1,1))
fsLogMIBCompliance.setObjects(*((_B,_l),(_B,_m)))
if mibBuilder.loadTexts:fsLogMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_F:LogSeverity,_K:LogTimeStamp,_L:LogSyslogFacility,'fsLogMIB':fsLogMIB,'fsLogMIBObjects':fsLogMIBObjects,_M:fsLogGlobalStatus,_N:fsLogSendConsoleStatus,_O:fsLogSendConsoleMaxSeverity,_P:fsLogSendMonitorStatus,_Q:fsLogSendMonitorMaxSeverity,_R:fsLogSaveFileName,_S:fsLogFileMaxSeverity,_T:fsLogFileMaxSize,_U:fsLogSendBufferStatus,_V:fsLogSendBufferMaxSeverity,_W:fsLogClearBuffer,_X:fsLogHisRecordMaxNum,'fsLogHisTable':fsLogHisTable,'fsLogHisEntry':fsLogHisEntry,_H:fsLogHisIndex,_Y:fsLogHisSeverity,_Z:fsLogHisMsgName,_a:fsLogHisDescription,_b:fsLogHisTime,_k:fsLogHisStamps,_c:fsLogSequenceGlobalStatus,_d:fsLogTimeStampGlobalStatus,_e:fsLogSyslogRelayGlobalStatus,_f:fsLogSyslogFacility,_g:fsLogSyslogSeverity,'fsLogSyslogServerTable':fsLogSyslogServerTable,'fsLogSyslogServerEntry':fsLogSyslogServerEntry,_I:fsLogSyslogServerIpAddr,_h:fsLogSyslogServerIpStatus,_i:fsLogSyslogSendSrcIfindex,_j:fsLogSyslogSendSrcIp,'fsLogMIBConformance':fsLogMIBConformance,'fsLogMIBCompliances':fsLogMIBCompliances,'fsLogMIBCompliance':fsLogMIBCompliance,'fsLogMIBGroups':fsLogMIBGroups,_l:fsLogMIBGroup,_m:fsLogHisStampsMIBGroup})