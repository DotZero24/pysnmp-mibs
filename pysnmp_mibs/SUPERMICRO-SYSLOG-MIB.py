_W='sysLogSrvrUnreachMessage'
_V='sysLogSrvrUnreachEventTime'
_U='accessible-for-notify'
_T='fsSyslogMailServAdd'
_S='fsSyslogMailServAddType'
_R='fsSyslogMailPriority'
_Q='fsSyslogFwdServerIP'
_P='fsSyslogFwdAddressType'
_O='fsSyslogFwdPriority'
_N='fsSyslogFileName'
_M='fsSyslogFilePriority'
_L='fsSyslogConfigModule'
_K='TruthValue'
_J='InetAddress'
_I='deprecated'
_H='disable'
_G='enable'
_F='not-accessible'
_E='DisplayString'
_D='SUPERMICRO-SYSLOG-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_J,'InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention',_K)
fsSyslog=ModuleIdentity((1,3,6,1,4,1,10876,101,1,89))
if mibBuilder.loadTexts:fsSyslog.setRevisions(('2012-09-05 00:00',))
_FsSyslogGeneralGroup_ObjectIdentity=ObjectIdentity
fsSyslogGeneralGroup=_FsSyslogGeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,89,1))
class _FsSyslogLogging_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSyslogLogging_Type.__name__=_C
_FsSyslogLogging_Object=MibScalar
fsSyslogLogging=_FsSyslogLogging_Object((1,3,6,1,4,1,10876,101,1,89,1,1),_FsSyslogLogging_Type())
fsSyslogLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogLogging.setStatus(_A)
class _FsSyslogTimeStamp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSyslogTimeStamp_Type.__name__=_C
_FsSyslogTimeStamp_Object=MibScalar
fsSyslogTimeStamp=_FsSyslogTimeStamp_Object((1,3,6,1,4,1,10876,101,1,89,1,2),_FsSyslogTimeStamp_Type())
fsSyslogTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogTimeStamp.setStatus(_I)
class _FsSyslogConsoleLog_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSyslogConsoleLog_Type.__name__=_C
_FsSyslogConsoleLog_Object=MibScalar
fsSyslogConsoleLog=_FsSyslogConsoleLog_Object((1,3,6,1,4,1,10876,101,1,89,1,3),_FsSyslogConsoleLog_Type())
fsSyslogConsoleLog.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogConsoleLog.setStatus(_A)
class _FsSyslogSysBuffers_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_FsSyslogSysBuffers_Type.__name__=_C
_FsSyslogSysBuffers_Object=MibScalar
fsSyslogSysBuffers=_FsSyslogSysBuffers_Object((1,3,6,1,4,1,10876,101,1,89,1,4),_FsSyslogSysBuffers_Type())
fsSyslogSysBuffers.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogSysBuffers.setStatus(_A)
class _FsSyslogClearLog_Type(TruthValue):defaultValue=2
_FsSyslogClearLog_Type.__name__=_K
_FsSyslogClearLog_Object=MibScalar
fsSyslogClearLog=_FsSyslogClearLog_Object((1,3,6,1,4,1,10876,101,1,89,1,5),_FsSyslogClearLog_Type())
fsSyslogClearLog.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogClearLog.setStatus(_A)
_FsSyslogConfigTable_Object=MibTable
fsSyslogConfigTable=_FsSyslogConfigTable_Object((1,3,6,1,4,1,10876,101,1,89,1,6))
if mibBuilder.loadTexts:fsSyslogConfigTable.setStatus(_A)
_FsSyslogConfigEntry_Object=MibTableRow
fsSyslogConfigEntry=_FsSyslogConfigEntry_Object((1,3,6,1,4,1,10876,101,1,89,1,6,1))
fsSyslogConfigEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:fsSyslogConfigEntry.setStatus(_A)
class _FsSyslogConfigModule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('web',1),('msr',2),('tftp',3),('cli',4)))
_FsSyslogConfigModule_Type.__name__=_C
_FsSyslogConfigModule_Object=MibTableColumn
fsSyslogConfigModule=_FsSyslogConfigModule_Object((1,3,6,1,4,1,10876,101,1,89,1,6,1,1),_FsSyslogConfigModule_Type())
fsSyslogConfigModule.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSyslogConfigModule.setStatus(_A)
class _FsSyslogConfigLogLevel_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7)))
_FsSyslogConfigLogLevel_Type.__name__=_C
_FsSyslogConfigLogLevel_Object=MibTableColumn
fsSyslogConfigLogLevel=_FsSyslogConfigLogLevel_Object((1,3,6,1,4,1,10876,101,1,89,1,6,1,2),_FsSyslogConfigLogLevel_Type())
fsSyslogConfigLogLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogConfigLogLevel.setStatus(_A)
class _FsSyslogFacility_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(128,136,144,152,160,168,176,184)));namedValues=NamedValues(*(('local0',128),('local1',136),('local2',144),('local3',152),('local4',160),('local5',168),('local6',176),('local7',184)))
_FsSyslogFacility_Type.__name__=_C
_FsSyslogFacility_Object=MibScalar
fsSyslogFacility=_FsSyslogFacility_Object((1,3,6,1,4,1,10876,101,1,89,1,7),_FsSyslogFacility_Type())
fsSyslogFacility.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogFacility.setStatus(_A)
class _FsSyslogRole_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('device',1),('relay',2)))
_FsSyslogRole_Type.__name__=_C
_FsSyslogRole_Object=MibScalar
fsSyslogRole=_FsSyslogRole_Object((1,3,6,1,4,1,10876,101,1,89,1,8),_FsSyslogRole_Type())
fsSyslogRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogRole.setStatus(_A)
class _FsSyslogLogFile_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSyslogLogFile_Type.__name__=_C
_FsSyslogLogFile_Object=MibScalar
fsSyslogLogFile=_FsSyslogLogFile_Object((1,3,6,1,4,1,10876,101,1,89,1,9),_FsSyslogLogFile_Type())
fsSyslogLogFile.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogLogFile.setStatus(_A)
class _FsSyslogMail_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSyslogMail_Type.__name__=_C
_FsSyslogMail_Object=MibScalar
fsSyslogMail=_FsSyslogMail_Object((1,3,6,1,4,1,10876,101,1,89,1,10),_FsSyslogMail_Type())
fsSyslogMail.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogMail.setStatus(_A)
class _FsSyslogProfile_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('raw',1),('cooked',2)))
_FsSyslogProfile_Type.__name__=_C
_FsSyslogProfile_Object=MibScalar
fsSyslogProfile=_FsSyslogProfile_Object((1,3,6,1,4,1,10876,101,1,89,1,11),_FsSyslogProfile_Type())
fsSyslogProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogProfile.setStatus(_A)
class _FsSyslogRelayPort_Type(Integer32):defaultValue=514;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsSyslogRelayPort_Type.__name__=_C
_FsSyslogRelayPort_Object=MibScalar
fsSyslogRelayPort=_FsSyslogRelayPort_Object((1,3,6,1,4,1,10876,101,1,89,1,12),_FsSyslogRelayPort_Type())
fsSyslogRelayPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogRelayPort.setStatus(_A)
class _FsSyslogRelayTransType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('udp',1),('tcp',2)))
_FsSyslogRelayTransType_Type.__name__=_C
_FsSyslogRelayTransType_Object=MibScalar
fsSyslogRelayTransType=_FsSyslogRelayTransType_Object((1,3,6,1,4,1,10876,101,1,89,1,13),_FsSyslogRelayTransType_Type())
fsSyslogRelayTransType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogRelayTransType.setStatus(_A)
class _FsSyslogFileNameOne_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsSyslogFileNameOne_Type.__name__=_E
_FsSyslogFileNameOne_Object=MibScalar
fsSyslogFileNameOne=_FsSyslogFileNameOne_Object((1,3,6,1,4,1,10876,101,1,89,1,14),_FsSyslogFileNameOne_Type())
fsSyslogFileNameOne.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogFileNameOne.setStatus(_A)
class _FsSyslogFileNameTwo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsSyslogFileNameTwo_Type.__name__=_E
_FsSyslogFileNameTwo_Object=MibScalar
fsSyslogFileNameTwo=_FsSyslogFileNameTwo_Object((1,3,6,1,4,1,10876,101,1,89,1,15),_FsSyslogFileNameTwo_Type())
fsSyslogFileNameTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogFileNameTwo.setStatus(_A)
class _FsSyslogFileNameThree_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsSyslogFileNameThree_Type.__name__=_E
_FsSyslogFileNameThree_Object=MibScalar
fsSyslogFileNameThree=_FsSyslogFileNameThree_Object((1,3,6,1,4,1,10876,101,1,89,1,16),_FsSyslogFileNameThree_Type())
fsSyslogFileNameThree.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogFileNameThree.setStatus(_A)
_FsSyslogFileTable_Object=MibTable
fsSyslogFileTable=_FsSyslogFileTable_Object((1,3,6,1,4,1,10876,101,1,89,1,17))
if mibBuilder.loadTexts:fsSyslogFileTable.setStatus(_A)
_FsSyslogFileEntry_Object=MibTableRow
fsSyslogFileEntry=_FsSyslogFileEntry_Object((1,3,6,1,4,1,10876,101,1,89,1,17,1))
fsSyslogFileEntry.setIndexNames((0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:fsSyslogFileEntry.setStatus(_A)
class _FsSyslogFilePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,191))
_FsSyslogFilePriority_Type.__name__=_C
_FsSyslogFilePriority_Object=MibTableColumn
fsSyslogFilePriority=_FsSyslogFilePriority_Object((1,3,6,1,4,1,10876,101,1,89,1,17,1,1),_FsSyslogFilePriority_Type())
fsSyslogFilePriority.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSyslogFilePriority.setStatus(_A)
class _FsSyslogFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsSyslogFileName_Type.__name__=_E
_FsSyslogFileName_Object=MibTableColumn
fsSyslogFileName=_FsSyslogFileName_Object((1,3,6,1,4,1,10876,101,1,89,1,17,1,2),_FsSyslogFileName_Type())
fsSyslogFileName.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSyslogFileName.setStatus(_A)
_FsSyslogFileRowStatus_Type=RowStatus
_FsSyslogFileRowStatus_Object=MibTableColumn
fsSyslogFileRowStatus=_FsSyslogFileRowStatus_Object((1,3,6,1,4,1,10876,101,1,89,1,17,1,3),_FsSyslogFileRowStatus_Type())
fsSyslogFileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogFileRowStatus.setStatus(_A)
class _FsSyslogServerUpDownTrap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsSyslogServerUpDownTrap_Type.__name__=_C
_FsSyslogServerUpDownTrap_Object=MibScalar
fsSyslogServerUpDownTrap=_FsSyslogServerUpDownTrap_Object((1,3,6,1,4,1,10876,101,1,89,1,18),_FsSyslogServerUpDownTrap_Type())
fsSyslogServerUpDownTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogServerUpDownTrap.setStatus(_A)
_FsSyslogLogs_ObjectIdentity=ObjectIdentity
fsSyslogLogs=_FsSyslogLogs_ObjectIdentity((1,3,6,1,4,1,10876,101,1,89,2))
_FsSyslogLogSrvAddr_Type=IpAddress
_FsSyslogLogSrvAddr_Object=MibScalar
fsSyslogLogSrvAddr=_FsSyslogLogSrvAddr_Object((1,3,6,1,4,1,10876,101,1,89,2,1),_FsSyslogLogSrvAddr_Type())
fsSyslogLogSrvAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogLogSrvAddr.setStatus(_I)
_FsSyslogLogNoLogServer_Type=TruthValue
_FsSyslogLogNoLogServer_Object=MibScalar
fsSyslogLogNoLogServer=_FsSyslogLogNoLogServer_Object((1,3,6,1,4,1,10876,101,1,89,2,2),_FsSyslogLogNoLogServer_Type())
fsSyslogLogNoLogServer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogLogNoLogServer.setStatus(_I)
_FsSyslogFwdTable_Object=MibTable
fsSyslogFwdTable=_FsSyslogFwdTable_Object((1,3,6,1,4,1,10876,101,1,89,2,3))
if mibBuilder.loadTexts:fsSyslogFwdTable.setStatus(_A)
_FsSyslogFwdEntry_Object=MibTableRow
fsSyslogFwdEntry=_FsSyslogFwdEntry_Object((1,3,6,1,4,1,10876,101,1,89,2,3,1))
fsSyslogFwdEntry.setIndexNames((0,_D,_O),(0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:fsSyslogFwdEntry.setStatus(_A)
class _FsSyslogFwdPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,191))
_FsSyslogFwdPriority_Type.__name__=_C
_FsSyslogFwdPriority_Object=MibTableColumn
fsSyslogFwdPriority=_FsSyslogFwdPriority_Object((1,3,6,1,4,1,10876,101,1,89,2,3,1,1),_FsSyslogFwdPriority_Type())
fsSyslogFwdPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSyslogFwdPriority.setStatus(_A)
_FsSyslogFwdAddressType_Type=InetAddressType
_FsSyslogFwdAddressType_Object=MibTableColumn
fsSyslogFwdAddressType=_FsSyslogFwdAddressType_Object((1,3,6,1,4,1,10876,101,1,89,2,3,1,2),_FsSyslogFwdAddressType_Type())
fsSyslogFwdAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSyslogFwdAddressType.setStatus(_A)
class _FsSyslogFwdServerIP_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_FsSyslogFwdServerIP_Type.__name__=_J
_FsSyslogFwdServerIP_Object=MibTableColumn
fsSyslogFwdServerIP=_FsSyslogFwdServerIP_Object((1,3,6,1,4,1,10876,101,1,89,2,3,1,3),_FsSyslogFwdServerIP_Type())
fsSyslogFwdServerIP.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSyslogFwdServerIP.setStatus(_A)
class _FsSyslogFwdPort_Type(Integer32):defaultValue=514;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsSyslogFwdPort_Type.__name__=_C
_FsSyslogFwdPort_Object=MibTableColumn
fsSyslogFwdPort=_FsSyslogFwdPort_Object((1,3,6,1,4,1,10876,101,1,89,2,3,1,4),_FsSyslogFwdPort_Type())
fsSyslogFwdPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogFwdPort.setStatus(_A)
class _FsSyslogFwdTransType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('udp',0),('tcp',1),('beep',2)))
_FsSyslogFwdTransType_Type.__name__=_C
_FsSyslogFwdTransType_Object=MibTableColumn
fsSyslogFwdTransType=_FsSyslogFwdTransType_Object((1,3,6,1,4,1,10876,101,1,89,2,3,1,5),_FsSyslogFwdTransType_Type())
fsSyslogFwdTransType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogFwdTransType.setStatus(_A)
_FsSyslogFwdRowStatus_Type=RowStatus
_FsSyslogFwdRowStatus_Object=MibTableColumn
fsSyslogFwdRowStatus=_FsSyslogFwdRowStatus_Object((1,3,6,1,4,1,10876,101,1,89,2,3,1,6),_FsSyslogFwdRowStatus_Type())
fsSyslogFwdRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogFwdRowStatus.setStatus(_A)
_FsSyslogSmtp_ObjectIdentity=ObjectIdentity
fsSyslogSmtp=_FsSyslogSmtp_ObjectIdentity((1,3,6,1,4,1,10876,101,1,89,3))
_FsSyslogSmtpSrvAddr_Type=IpAddress
_FsSyslogSmtpSrvAddr_Object=MibScalar
fsSyslogSmtpSrvAddr=_FsSyslogSmtpSrvAddr_Object((1,3,6,1,4,1,10876,101,1,89,3,1),_FsSyslogSmtpSrvAddr_Type())
fsSyslogSmtpSrvAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogSmtpSrvAddr.setStatus(_I)
class _FsSyslogSmtpRcvrMailId_Type(DisplayString):defaultValue=OctetString('admin@email.com');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_FsSyslogSmtpRcvrMailId_Type.__name__=_E
_FsSyslogSmtpRcvrMailId_Object=MibScalar
fsSyslogSmtpRcvrMailId=_FsSyslogSmtpRcvrMailId_Object((1,3,6,1,4,1,10876,101,1,89,3,2),_FsSyslogSmtpRcvrMailId_Type())
fsSyslogSmtpRcvrMailId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogSmtpRcvrMailId.setStatus(_I)
class _FsSyslogSmtpSenderMailId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_FsSyslogSmtpSenderMailId_Type.__name__=_E
_FsSyslogSmtpSenderMailId_Object=MibScalar
fsSyslogSmtpSenderMailId=_FsSyslogSmtpSenderMailId_Object((1,3,6,1,4,1,10876,101,1,89,3,3),_FsSyslogSmtpSenderMailId_Type())
fsSyslogSmtpSenderMailId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogSmtpSenderMailId.setStatus(_A)
_FsSyslogMailTable_Object=MibTable
fsSyslogMailTable=_FsSyslogMailTable_Object((1,3,6,1,4,1,10876,101,1,89,3,4))
if mibBuilder.loadTexts:fsSyslogMailTable.setStatus(_A)
_FsSyslogMailEntry_Object=MibTableRow
fsSyslogMailEntry=_FsSyslogMailEntry_Object((1,3,6,1,4,1,10876,101,1,89,3,4,1))
fsSyslogMailEntry.setIndexNames((0,_D,_R),(0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:fsSyslogMailEntry.setStatus(_A)
class _FsSyslogMailPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,191))
_FsSyslogMailPriority_Type.__name__=_C
_FsSyslogMailPriority_Object=MibTableColumn
fsSyslogMailPriority=_FsSyslogMailPriority_Object((1,3,6,1,4,1,10876,101,1,89,3,4,1,1),_FsSyslogMailPriority_Type())
fsSyslogMailPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSyslogMailPriority.setStatus(_A)
_FsSyslogMailServAddType_Type=InetAddressType
_FsSyslogMailServAddType_Object=MibTableColumn
fsSyslogMailServAddType=_FsSyslogMailServAddType_Object((1,3,6,1,4,1,10876,101,1,89,3,4,1,2),_FsSyslogMailServAddType_Type())
fsSyslogMailServAddType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSyslogMailServAddType.setStatus(_A)
class _FsSyslogMailServAdd_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_FsSyslogMailServAdd_Type.__name__=_J
_FsSyslogMailServAdd_Object=MibTableColumn
fsSyslogMailServAdd=_FsSyslogMailServAdd_Object((1,3,6,1,4,1,10876,101,1,89,3,4,1,3),_FsSyslogMailServAdd_Type())
fsSyslogMailServAdd.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSyslogMailServAdd.setStatus(_A)
class _FsSyslogRxMailId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_FsSyslogRxMailId_Type.__name__=_E
_FsSyslogRxMailId_Object=MibTableColumn
fsSyslogRxMailId=_FsSyslogRxMailId_Object((1,3,6,1,4,1,10876,101,1,89,3,4,1,4),_FsSyslogRxMailId_Type())
fsSyslogRxMailId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogRxMailId.setStatus(_A)
_FsSyslogMailRowStatus_Type=RowStatus
_FsSyslogMailRowStatus_Object=MibTableColumn
fsSyslogMailRowStatus=_FsSyslogMailRowStatus_Object((1,3,6,1,4,1,10876,101,1,89,3,4,1,5),_FsSyslogMailRowStatus_Type())
fsSyslogMailRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogMailRowStatus.setStatus(_A)
class _FsSyslogMailServUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsSyslogMailServUserName_Type.__name__=_E
_FsSyslogMailServUserName_Object=MibTableColumn
fsSyslogMailServUserName=_FsSyslogMailServUserName_Object((1,3,6,1,4,1,10876,101,1,89,3,4,1,6),_FsSyslogMailServUserName_Type())
fsSyslogMailServUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogMailServUserName.setStatus(_A)
class _FsSyslogMailServPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsSyslogMailServPassword_Type.__name__=_E
_FsSyslogMailServPassword_Object=MibTableColumn
fsSyslogMailServPassword=_FsSyslogMailServPassword_Object((1,3,6,1,4,1,10876,101,1,89,3,4,1,7),_FsSyslogMailServPassword_Type())
fsSyslogMailServPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogMailServPassword.setStatus(_A)
class _FsSyslogSmtpAuthMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noAuthenticate',1),('authLogin',2),('authPlain',3),('crammd5',4),('digestmd5',5)))
_FsSyslogSmtpAuthMethod_Type.__name__=_C
_FsSyslogSmtpAuthMethod_Object=MibScalar
fsSyslogSmtpAuthMethod=_FsSyslogSmtpAuthMethod_Object((1,3,6,1,4,1,10876,101,1,89,3,5),_FsSyslogSmtpAuthMethod_Type())
fsSyslogSmtpAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSyslogSmtpAuthMethod.setStatus(_A)
_FsSyslogSrvrUnreachableNotifications_ObjectIdentity=ObjectIdentity
fsSyslogSrvrUnreachableNotifications=_FsSyslogSrvrUnreachableNotifications_ObjectIdentity((1,3,6,1,4,1,10876,101,1,89,4))
_SysLogTraps_ObjectIdentity=ObjectIdentity
sysLogTraps=_SysLogTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,89,4,0))
_SysLogTrapObjects_ObjectIdentity=ObjectIdentity
sysLogTrapObjects=_SysLogTrapObjects_ObjectIdentity((1,3,6,1,4,1,10876,101,1,89,4,1))
class _SysLogSrvrUnreachEventTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(24,24));fixedLength=24
_SysLogSrvrUnreachEventTime_Type.__name__=_E
_SysLogSrvrUnreachEventTime_Object=MibScalar
sysLogSrvrUnreachEventTime=_SysLogSrvrUnreachEventTime_Object((1,3,6,1,4,1,10876,101,1,89,4,1,1),_SysLogSrvrUnreachEventTime_Type())
sysLogSrvrUnreachEventTime.setMaxAccess(_U)
if mibBuilder.loadTexts:sysLogSrvrUnreachEventTime.setStatus(_A)
_SysLogSrvrUnreachMessage_Type=DisplayString
_SysLogSrvrUnreachMessage_Object=MibScalar
sysLogSrvrUnreachMessage=_SysLogSrvrUnreachMessage_Object((1,3,6,1,4,1,10876,101,1,89,4,1,2),_SysLogSrvrUnreachMessage_Type())
sysLogSrvrUnreachMessage.setMaxAccess(_U)
if mibBuilder.loadTexts:sysLogSrvrUnreachMessage.setStatus(_A)
sysLogSrvrUnreachable=NotificationType((1,3,6,1,4,1,10876,101,1,89,4,0,1))
sysLogSrvrUnreachable.setObjects(*((_D,_V),(_D,_W)))
if mibBuilder.loadTexts:sysLogSrvrUnreachable.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fsSyslog':fsSyslog,'fsSyslogGeneralGroup':fsSyslogGeneralGroup,'fsSyslogLogging':fsSyslogLogging,'fsSyslogTimeStamp':fsSyslogTimeStamp,'fsSyslogConsoleLog':fsSyslogConsoleLog,'fsSyslogSysBuffers':fsSyslogSysBuffers,'fsSyslogClearLog':fsSyslogClearLog,'fsSyslogConfigTable':fsSyslogConfigTable,'fsSyslogConfigEntry':fsSyslogConfigEntry,_L:fsSyslogConfigModule,'fsSyslogConfigLogLevel':fsSyslogConfigLogLevel,'fsSyslogFacility':fsSyslogFacility,'fsSyslogRole':fsSyslogRole,'fsSyslogLogFile':fsSyslogLogFile,'fsSyslogMail':fsSyslogMail,'fsSyslogProfile':fsSyslogProfile,'fsSyslogRelayPort':fsSyslogRelayPort,'fsSyslogRelayTransType':fsSyslogRelayTransType,'fsSyslogFileNameOne':fsSyslogFileNameOne,'fsSyslogFileNameTwo':fsSyslogFileNameTwo,'fsSyslogFileNameThree':fsSyslogFileNameThree,'fsSyslogFileTable':fsSyslogFileTable,'fsSyslogFileEntry':fsSyslogFileEntry,_M:fsSyslogFilePriority,_N:fsSyslogFileName,'fsSyslogFileRowStatus':fsSyslogFileRowStatus,'fsSyslogServerUpDownTrap':fsSyslogServerUpDownTrap,'fsSyslogLogs':fsSyslogLogs,'fsSyslogLogSrvAddr':fsSyslogLogSrvAddr,'fsSyslogLogNoLogServer':fsSyslogLogNoLogServer,'fsSyslogFwdTable':fsSyslogFwdTable,'fsSyslogFwdEntry':fsSyslogFwdEntry,_O:fsSyslogFwdPriority,_P:fsSyslogFwdAddressType,_Q:fsSyslogFwdServerIP,'fsSyslogFwdPort':fsSyslogFwdPort,'fsSyslogFwdTransType':fsSyslogFwdTransType,'fsSyslogFwdRowStatus':fsSyslogFwdRowStatus,'fsSyslogSmtp':fsSyslogSmtp,'fsSyslogSmtpSrvAddr':fsSyslogSmtpSrvAddr,'fsSyslogSmtpRcvrMailId':fsSyslogSmtpRcvrMailId,'fsSyslogSmtpSenderMailId':fsSyslogSmtpSenderMailId,'fsSyslogMailTable':fsSyslogMailTable,'fsSyslogMailEntry':fsSyslogMailEntry,_R:fsSyslogMailPriority,_S:fsSyslogMailServAddType,_T:fsSyslogMailServAdd,'fsSyslogRxMailId':fsSyslogRxMailId,'fsSyslogMailRowStatus':fsSyslogMailRowStatus,'fsSyslogMailServUserName':fsSyslogMailServUserName,'fsSyslogMailServPassword':fsSyslogMailServPassword,'fsSyslogSmtpAuthMethod':fsSyslogSmtpAuthMethod,'fsSyslogSrvrUnreachableNotifications':fsSyslogSrvrUnreachableNotifications,'sysLogTraps':sysLogTraps,'sysLogSrvrUnreachable':sysLogSrvrUnreachable,'sysLogTrapObjects':sysLogTrapObjects,_V:sysLogSrvrUnreachEventTime,_W:sysLogSrvrUnreachMessage})