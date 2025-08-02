_d='hm2LogEmailNumEmailFailures'
_c='hm2LogHumHistIndex'
_b='hm2LogEmailSmtpAddrIndex'
_a='hm2LogEmailSubjectMessageType'
_Z='hm2LogEmailToAddrMessageIndex'
_Y='hm2LogTempHistIndex'
_X='hm2LogCounterFlashBlock'
_W='hm2LogPersistentFileIndex'
_V='00000000'
_U='hm2LogSyslogServerIndex'
_T='DisplayString'
_S='urgent'
_R='InetPortNumber'
_Q='InetAddressType'
_P='InetAddress'
_O='Hm2TlsVersions'
_N='Hm2TlsCipherSuites'
_M='percent'
_L='non-urgent'
_K='Unsigned32'
_J='not-accessible'
_I='SnmpAdminString'
_H='HmEnabledStatus'
_G='HmAgentLogSeverity'
_F='HM2-LOGGING-MIB'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Hm2TlsCipherSuites,Hm2TlsVersions=mibBuilder.importSymbols('HM2-MGMTACCESS-MIB',_N,_O)
HmEnabledStatus,HmTimeSeconds1970,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_H,'HmTimeSeconds1970','hm2ConfigurationMibs')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_P,_Q,_R)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_T,'PhysAddress','RowStatus','TextualConvention')
hm2LoggingMib=ModuleIdentity((1,3,6,1,4,1,248,11,23))
if mibBuilder.loadTexts:hm2LoggingMib.setRevisions(('2012-08-08 00:00','2011-03-16 00:00'))
class HmAgentLogSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('informational',6),('debug',7)))
_Hm2LoggingMibNotifications_ObjectIdentity=ObjectIdentity
hm2LoggingMibNotifications=_Hm2LoggingMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,23,0))
_Hm2LoggingMibObjects_ObjectIdentity=ObjectIdentity
hm2LoggingMibObjects=_Hm2LoggingMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,23,1))
_Hm2LogSnmpLoggingGroup_ObjectIdentity=ObjectIdentity
hm2LogSnmpLoggingGroup=_Hm2LogSnmpLoggingGroup_ObjectIdentity((1,3,6,1,4,1,248,11,23,1,1))
class _Hm2LogSnmpLogGetRequest_Type(HmEnabledStatus):defaultValue=2
_Hm2LogSnmpLogGetRequest_Type.__name__=_H
_Hm2LogSnmpLogGetRequest_Object=MibScalar
hm2LogSnmpLogGetRequest=_Hm2LogSnmpLogGetRequest_Object((1,3,6,1,4,1,248,11,23,1,1,1),_Hm2LogSnmpLogGetRequest_Type())
hm2LogSnmpLogGetRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogSnmpLogGetRequest.setStatus(_A)
class _Hm2LogSnmpLogSetRequest_Type(HmEnabledStatus):defaultValue=2
_Hm2LogSnmpLogSetRequest_Type.__name__=_H
_Hm2LogSnmpLogSetRequest_Object=MibScalar
hm2LogSnmpLogSetRequest=_Hm2LogSnmpLogSetRequest_Object((1,3,6,1,4,1,248,11,23,1,1,2),_Hm2LogSnmpLogSetRequest_Type())
hm2LogSnmpLogSetRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogSnmpLogSetRequest.setStatus(_A)
class _Hm2LogSnmpLogGetSeverity_Type(HmAgentLogSeverity):defaultValue=5
_Hm2LogSnmpLogGetSeverity_Type.__name__=_G
_Hm2LogSnmpLogGetSeverity_Object=MibScalar
hm2LogSnmpLogGetSeverity=_Hm2LogSnmpLogGetSeverity_Object((1,3,6,1,4,1,248,11,23,1,1,3),_Hm2LogSnmpLogGetSeverity_Type())
hm2LogSnmpLogGetSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogSnmpLogGetSeverity.setStatus(_A)
class _Hm2LogSnmpLogSetSeverity_Type(HmAgentLogSeverity):defaultValue=5
_Hm2LogSnmpLogSetSeverity_Type.__name__=_G
_Hm2LogSnmpLogSetSeverity_Object=MibScalar
hm2LogSnmpLogSetSeverity=_Hm2LogSnmpLogSetSeverity_Object((1,3,6,1,4,1,248,11,23,1,1,4),_Hm2LogSnmpLogSetSeverity_Type())
hm2LogSnmpLogSetSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogSnmpLogSetSeverity.setStatus(_A)
_Hm2LogCliCommandsLoggingGroup_ObjectIdentity=ObjectIdentity
hm2LogCliCommandsLoggingGroup=_Hm2LogCliCommandsLoggingGroup_ObjectIdentity((1,3,6,1,4,1,248,11,23,1,2))
class _Hm2LogCliCommandsAdminStatus_Type(HmEnabledStatus):defaultValue=2
_Hm2LogCliCommandsAdminStatus_Type.__name__=_H
_Hm2LogCliCommandsAdminStatus_Object=MibScalar
hm2LogCliCommandsAdminStatus=_Hm2LogCliCommandsAdminStatus_Object((1,3,6,1,4,1,248,11,23,1,2,1),_Hm2LogCliCommandsAdminStatus_Type())
hm2LogCliCommandsAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogCliCommandsAdminStatus.setStatus(_A)
_Hm2LogConsoleLoggingGroup_ObjectIdentity=ObjectIdentity
hm2LogConsoleLoggingGroup=_Hm2LogConsoleLoggingGroup_ObjectIdentity((1,3,6,1,4,1,248,11,23,1,3))
class _Hm2LogConsoleAdminStatus_Type(HmEnabledStatus):defaultValue=2
_Hm2LogConsoleAdminStatus_Type.__name__=_H
_Hm2LogConsoleAdminStatus_Object=MibScalar
hm2LogConsoleAdminStatus=_Hm2LogConsoleAdminStatus_Object((1,3,6,1,4,1,248,11,23,1,3,1),_Hm2LogConsoleAdminStatus_Type())
hm2LogConsoleAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogConsoleAdminStatus.setStatus(_A)
class _Hm2LogConsoleSeverityFilter_Type(HmAgentLogSeverity):defaultValue=4
_Hm2LogConsoleSeverityFilter_Type.__name__=_G
_Hm2LogConsoleSeverityFilter_Object=MibScalar
hm2LogConsoleSeverityFilter=_Hm2LogConsoleSeverityFilter_Object((1,3,6,1,4,1,248,11,23,1,3,2),_Hm2LogConsoleSeverityFilter_Type())
hm2LogConsoleSeverityFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogConsoleSeverityFilter.setStatus(_A)
_Hm2LogBufferedLoggingGroup_ObjectIdentity=ObjectIdentity
hm2LogBufferedLoggingGroup=_Hm2LogBufferedLoggingGroup_ObjectIdentity((1,3,6,1,4,1,248,11,23,1,4))
class _Hm2LogBufferdLogLevelThreshold_Type(HmAgentLogSeverity):defaultValue=4
_Hm2LogBufferdLogLevelThreshold_Type.__name__=_G
_Hm2LogBufferdLogLevelThreshold_Object=MibScalar
hm2LogBufferdLogLevelThreshold=_Hm2LogBufferdLogLevelThreshold_Object((1,3,6,1,4,1,248,11,23,1,4,1),_Hm2LogBufferdLogLevelThreshold_Type())
hm2LogBufferdLogLevelThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogBufferdLogLevelThreshold.setStatus(_A)
_Hm2LogSyslogGroup_ObjectIdentity=ObjectIdentity
hm2LogSyslogGroup=_Hm2LogSyslogGroup_ObjectIdentity((1,3,6,1,4,1,248,11,23,1,5))
class _Hm2LogSyslogAdminStatus_Type(HmEnabledStatus):defaultValue=2
_Hm2LogSyslogAdminStatus_Type.__name__=_H
_Hm2LogSyslogAdminStatus_Object=MibScalar
hm2LogSyslogAdminStatus=_Hm2LogSyslogAdminStatus_Object((1,3,6,1,4,1,248,11,23,1,5,1),_Hm2LogSyslogAdminStatus_Type())
hm2LogSyslogAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogSyslogAdminStatus.setStatus(_A)
class _Hm2LogSyslogClientTlsVersions_Type(Hm2TlsVersions):defaultBinValue='001'
_Hm2LogSyslogClientTlsVersions_Type.__name__=_O
_Hm2LogSyslogClientTlsVersions_Object=MibScalar
hm2LogSyslogClientTlsVersions=_Hm2LogSyslogClientTlsVersions_Object((1,3,6,1,4,1,248,11,23,1,5,2),_Hm2LogSyslogClientTlsVersions_Type())
hm2LogSyslogClientTlsVersions.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogSyslogClientTlsVersions.setStatus(_A)
class _Hm2LogSyslogClientTlsCipherSuites_Type(Hm2TlsCipherSuites):defaultBinValue='0110101'
_Hm2LogSyslogClientTlsCipherSuites_Type.__name__=_N
_Hm2LogSyslogClientTlsCipherSuites_Object=MibScalar
hm2LogSyslogClientTlsCipherSuites=_Hm2LogSyslogClientTlsCipherSuites_Object((1,3,6,1,4,1,248,11,23,1,5,3),_Hm2LogSyslogClientTlsCipherSuites_Type())
hm2LogSyslogClientTlsCipherSuites.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogSyslogClientTlsCipherSuites.setStatus(_A)
_Hm2LogSyslogServerTable_Object=MibTable
hm2LogSyslogServerTable=_Hm2LogSyslogServerTable_Object((1,3,6,1,4,1,248,11,23,1,5,10))
if mibBuilder.loadTexts:hm2LogSyslogServerTable.setStatus(_A)
_Hm2LogSyslogServerEntry_Object=MibTableRow
hm2LogSyslogServerEntry=_Hm2LogSyslogServerEntry_Object((1,3,6,1,4,1,248,11,23,1,5,10,1))
hm2LogSyslogServerEntry.setIndexNames((0,_F,_U))
if mibBuilder.loadTexts:hm2LogSyslogServerEntry.setStatus(_A)
class _Hm2LogSyslogServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Hm2LogSyslogServerIndex_Type.__name__=_E
_Hm2LogSyslogServerIndex_Object=MibTableColumn
hm2LogSyslogServerIndex=_Hm2LogSyslogServerIndex_Object((1,3,6,1,4,1,248,11,23,1,5,10,1,1),_Hm2LogSyslogServerIndex_Type())
hm2LogSyslogServerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogSyslogServerIndex.setStatus(_A)
class _Hm2LogSyslogServerIPAddrType_Type(InetAddressType):defaultValue=1
_Hm2LogSyslogServerIPAddrType_Type.__name__=_Q
_Hm2LogSyslogServerIPAddrType_Object=MibTableColumn
hm2LogSyslogServerIPAddrType=_Hm2LogSyslogServerIPAddrType_Object((1,3,6,1,4,1,248,11,23,1,5,10,1,2),_Hm2LogSyslogServerIPAddrType_Type())
hm2LogSyslogServerIPAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogSyslogServerIPAddrType.setStatus(_A)
class _Hm2LogSyslogServerIPAddr_Type(InetAddress):defaultHexValue=_V
_Hm2LogSyslogServerIPAddr_Type.__name__=_P
_Hm2LogSyslogServerIPAddr_Object=MibTableColumn
hm2LogSyslogServerIPAddr=_Hm2LogSyslogServerIPAddr_Object((1,3,6,1,4,1,248,11,23,1,5,10,1,3),_Hm2LogSyslogServerIPAddr_Type())
hm2LogSyslogServerIPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogSyslogServerIPAddr.setStatus(_A)
class _Hm2LogSyslogServerUdpPort_Type(InetPortNumber):defaultValue=514
_Hm2LogSyslogServerUdpPort_Type.__name__=_R
_Hm2LogSyslogServerUdpPort_Object=MibTableColumn
hm2LogSyslogServerUdpPort=_Hm2LogSyslogServerUdpPort_Object((1,3,6,1,4,1,248,11,23,1,5,10,1,4),_Hm2LogSyslogServerUdpPort_Type())
hm2LogSyslogServerUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogSyslogServerUdpPort.setStatus(_A)
class _Hm2LogSyslogServerLevelUpto_Type(HmAgentLogSeverity):defaultValue=4
_Hm2LogSyslogServerLevelUpto_Type.__name__=_G
_Hm2LogSyslogServerLevelUpto_Object=MibTableColumn
hm2LogSyslogServerLevelUpto=_Hm2LogSyslogServerLevelUpto_Object((1,3,6,1,4,1,248,11,23,1,5,10,1,5),_Hm2LogSyslogServerLevelUpto_Type())
hm2LogSyslogServerLevelUpto.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogSyslogServerLevelUpto.setStatus(_A)
class _Hm2LogSyslogServerLogType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('systemlog',1),('audittrail',2)))
_Hm2LogSyslogServerLogType_Type.__name__=_E
_Hm2LogSyslogServerLogType_Object=MibTableColumn
hm2LogSyslogServerLogType=_Hm2LogSyslogServerLogType_Object((1,3,6,1,4,1,248,11,23,1,5,10,1,6),_Hm2LogSyslogServerLogType_Type())
hm2LogSyslogServerLogType.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogSyslogServerLogType.setStatus(_A)
_Hm2LogSyslogServerRowStatus_Type=RowStatus
_Hm2LogSyslogServerRowStatus_Object=MibTableColumn
hm2LogSyslogServerRowStatus=_Hm2LogSyslogServerRowStatus_Object((1,3,6,1,4,1,248,11,23,1,5,10,1,7),_Hm2LogSyslogServerRowStatus_Type())
hm2LogSyslogServerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogSyslogServerRowStatus.setStatus(_A)
class _Hm2LogSyslogServerTransportType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('udp',1),('tls',2)))
_Hm2LogSyslogServerTransportType_Type.__name__=_E
_Hm2LogSyslogServerTransportType_Object=MibTableColumn
hm2LogSyslogServerTransportType=_Hm2LogSyslogServerTransportType_Object((1,3,6,1,4,1,248,11,23,1,5,10,1,8),_Hm2LogSyslogServerTransportType_Type())
hm2LogSyslogServerTransportType.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogSyslogServerTransportType.setStatus(_A)
_Hm2LogPersistentGroup_ObjectIdentity=ObjectIdentity
hm2LogPersistentGroup=_Hm2LogPersistentGroup_ObjectIdentity((1,3,6,1,4,1,248,11,23,1,6))
class _Hm2LogPersistAdminStatus_Type(HmEnabledStatus):defaultValue=1
_Hm2LogPersistAdminStatus_Type.__name__=_H
_Hm2LogPersistAdminStatus_Object=MibScalar
hm2LogPersistAdminStatus=_Hm2LogPersistAdminStatus_Object((1,3,6,1,4,1,248,11,23,1,6,1),_Hm2LogPersistAdminStatus_Type())
hm2LogPersistAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogPersistAdminStatus.setStatus(_A)
class _Hm2LogPersistMaxFileSize_Type(Integer32):defaultValue=1024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_Hm2LogPersistMaxFileSize_Type.__name__=_E
_Hm2LogPersistMaxFileSize_Object=MibScalar
hm2LogPersistMaxFileSize=_Hm2LogPersistMaxFileSize_Object((1,3,6,1,4,1,248,11,23,1,6,2),_Hm2LogPersistMaxFileSize_Type())
hm2LogPersistMaxFileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogPersistMaxFileSize.setStatus(_A)
class _Hm2LogPersistFilesMax_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_Hm2LogPersistFilesMax_Type.__name__=_E
_Hm2LogPersistFilesMax_Object=MibScalar
hm2LogPersistFilesMax=_Hm2LogPersistFilesMax_Object((1,3,6,1,4,1,248,11,23,1,6,3),_Hm2LogPersistFilesMax_Type())
hm2LogPersistFilesMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogPersistFilesMax.setStatus(_A)
class _Hm2LogPersistLevelUpto_Type(HmAgentLogSeverity):defaultValue=4
_Hm2LogPersistLevelUpto_Type.__name__=_G
_Hm2LogPersistLevelUpto_Object=MibScalar
hm2LogPersistLevelUpto=_Hm2LogPersistLevelUpto_Object((1,3,6,1,4,1,248,11,23,1,6,4),_Hm2LogPersistLevelUpto_Type())
hm2LogPersistLevelUpto.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogPersistLevelUpto.setStatus(_A)
_Hm2LogPersistentFileTable_Object=MibTable
hm2LogPersistentFileTable=_Hm2LogPersistentFileTable_Object((1,3,6,1,4,1,248,11,23,1,6,5))
if mibBuilder.loadTexts:hm2LogPersistentFileTable.setStatus(_A)
_Hm2LogPersistentFileEntry_Object=MibTableRow
hm2LogPersistentFileEntry=_Hm2LogPersistentFileEntry_Object((1,3,6,1,4,1,248,11,23,1,6,5,1))
hm2LogPersistentFileEntry.setIndexNames((0,_F,_W))
if mibBuilder.loadTexts:hm2LogPersistentFileEntry.setStatus(_A)
_Hm2LogPersistentFileIndex_Type=Integer32
_Hm2LogPersistentFileIndex_Object=MibTableColumn
hm2LogPersistentFileIndex=_Hm2LogPersistentFileIndex_Object((1,3,6,1,4,1,248,11,23,1,6,5,1,1),_Hm2LogPersistentFileIndex_Type())
hm2LogPersistentFileIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hm2LogPersistentFileIndex.setStatus(_A)
_Hm2LogPersistentFileName_Type=DisplayString
_Hm2LogPersistentFileName_Object=MibTableColumn
hm2LogPersistentFileName=_Hm2LogPersistentFileName_Object((1,3,6,1,4,1,248,11,23,1,6,5,1,2),_Hm2LogPersistentFileName_Type())
hm2LogPersistentFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogPersistentFileName.setStatus(_A)
_Hm2LogPersistentFileSize_Type=Integer32
_Hm2LogPersistentFileSize_Object=MibTableColumn
hm2LogPersistentFileSize=_Hm2LogPersistentFileSize_Object((1,3,6,1,4,1,248,11,23,1,6,5,1,3),_Hm2LogPersistentFileSize_Type())
hm2LogPersistentFileSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogPersistentFileSize.setStatus(_A)
_Hm2LogCounterGroup_ObjectIdentity=ObjectIdentity
hm2LogCounterGroup=_Hm2LogCounterGroup_ObjectIdentity((1,3,6,1,4,1,248,11,23,1,7))
_Hm2LogCounterOperatingHours_Type=Integer32
_Hm2LogCounterOperatingHours_Object=MibScalar
hm2LogCounterOperatingHours=_Hm2LogCounterOperatingHours_Object((1,3,6,1,4,1,248,11,23,1,7,1),_Hm2LogCounterOperatingHours_Type())
hm2LogCounterOperatingHours.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogCounterOperatingHours.setStatus(_A)
_Hm2LogCounterFlashTable_Object=MibTable
hm2LogCounterFlashTable=_Hm2LogCounterFlashTable_Object((1,3,6,1,4,1,248,11,23,1,7,10))
if mibBuilder.loadTexts:hm2LogCounterFlashTable.setStatus(_A)
_Hm2LogCounterFlashEntry_Object=MibTableRow
hm2LogCounterFlashEntry=_Hm2LogCounterFlashEntry_Object((1,3,6,1,4,1,248,11,23,1,7,10,1))
hm2LogCounterFlashEntry.setIndexNames((0,_F,_X))
if mibBuilder.loadTexts:hm2LogCounterFlashEntry.setStatus(_A)
class _Hm2LogCounterFlashBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('bootBlock',1),('fileSystem',2),('imageStorage',3),('parameters',4),('formatFs',5),('userFormatFs',6),('dhcpBindings',7),('persistentLog',8)))
_Hm2LogCounterFlashBlock_Type.__name__=_E
_Hm2LogCounterFlashBlock_Object=MibTableColumn
hm2LogCounterFlashBlock=_Hm2LogCounterFlashBlock_Object((1,3,6,1,4,1,248,11,23,1,7,10,1,1),_Hm2LogCounterFlashBlock_Type())
hm2LogCounterFlashBlock.setMaxAccess(_J)
if mibBuilder.loadTexts:hm2LogCounterFlashBlock.setStatus(_A)
_Hm2LogCounterFlashDescription_Type=DisplayString
_Hm2LogCounterFlashDescription_Object=MibTableColumn
hm2LogCounterFlashDescription=_Hm2LogCounterFlashDescription_Object((1,3,6,1,4,1,248,11,23,1,7,10,1,2),_Hm2LogCounterFlashDescription_Type())
hm2LogCounterFlashDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogCounterFlashDescription.setStatus(_A)
_Hm2LogCounterFlashCount_Type=Integer32
_Hm2LogCounterFlashCount_Object=MibTableColumn
hm2LogCounterFlashCount=_Hm2LogCounterFlashCount_Object((1,3,6,1,4,1,248,11,23,1,7,10,1,3),_Hm2LogCounterFlashCount_Type())
hm2LogCounterFlashCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogCounterFlashCount.setStatus(_A)
_Hm2LogCounterFlashValue_Type=Integer32
_Hm2LogCounterFlashValue_Object=MibTableColumn
hm2LogCounterFlashValue=_Hm2LogCounterFlashValue_Object((1,3,6,1,4,1,248,11,23,1,7,10,1,4),_Hm2LogCounterFlashValue_Type())
hm2LogCounterFlashValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogCounterFlashValue.setStatus(_A)
_Hm2LogTemperatureGroup_ObjectIdentity=ObjectIdentity
hm2LogTemperatureGroup=_Hm2LogTemperatureGroup_ObjectIdentity((1,3,6,1,4,1,248,11,23,1,8))
_Hm2LogTempMinimum_Type=Integer32
_Hm2LogTempMinimum_Object=MibScalar
hm2LogTempMinimum=_Hm2LogTempMinimum_Object((1,3,6,1,4,1,248,11,23,1,8,1),_Hm2LogTempMinimum_Type())
hm2LogTempMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogTempMinimum.setStatus(_A)
_Hm2LogTempMaximum_Type=Integer32
_Hm2LogTempMaximum_Object=MibScalar
hm2LogTempMaximum=_Hm2LogTempMaximum_Object((1,3,6,1,4,1,248,11,23,1,8,2),_Hm2LogTempMaximum_Type())
hm2LogTempMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogTempMaximum.setStatus(_A)
_Hm2LogTempVariationCount_Type=Integer32
_Hm2LogTempVariationCount_Object=MibScalar
hm2LogTempVariationCount=_Hm2LogTempVariationCount_Object((1,3,6,1,4,1,248,11,23,1,8,3),_Hm2LogTempVariationCount_Type())
hm2LogTempVariationCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogTempVariationCount.setStatus(_A)
_Hm2LogTempHistTable_Object=MibTable
hm2LogTempHistTable=_Hm2LogTempHistTable_Object((1,3,6,1,4,1,248,11,23,1,8,10))
if mibBuilder.loadTexts:hm2LogTempHistTable.setStatus(_A)
_Hm2LogTempHistEntry_Object=MibTableRow
hm2LogTempHistEntry=_Hm2LogTempHistEntry_Object((1,3,6,1,4,1,248,11,23,1,8,10,1))
hm2LogTempHistEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:hm2LogTempHistEntry.setStatus(_A)
_Hm2LogTempHistIndex_Type=Integer32
_Hm2LogTempHistIndex_Object=MibTableColumn
hm2LogTempHistIndex=_Hm2LogTempHistIndex_Object((1,3,6,1,4,1,248,11,23,1,8,10,1,1),_Hm2LogTempHistIndex_Type())
hm2LogTempHistIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hm2LogTempHistIndex.setStatus(_A)
_Hm2LogTempHistRangeMin_Type=Integer32
_Hm2LogTempHistRangeMin_Object=MibTableColumn
hm2LogTempHistRangeMin=_Hm2LogTempHistRangeMin_Object((1,3,6,1,4,1,248,11,23,1,8,10,1,2),_Hm2LogTempHistRangeMin_Type())
hm2LogTempHistRangeMin.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogTempHistRangeMin.setStatus(_A)
_Hm2LogTempHistRangeMax_Type=Integer32
_Hm2LogTempHistRangeMax_Object=MibTableColumn
hm2LogTempHistRangeMax=_Hm2LogTempHistRangeMax_Object((1,3,6,1,4,1,248,11,23,1,8,10,1,3),_Hm2LogTempHistRangeMax_Type())
hm2LogTempHistRangeMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogTempHistRangeMax.setStatus(_A)
_Hm2LogTempHistTime_Type=Integer32
_Hm2LogTempHistTime_Object=MibTableColumn
hm2LogTempHistTime=_Hm2LogTempHistTime_Object((1,3,6,1,4,1,248,11,23,1,8,10,1,4),_Hm2LogTempHistTime_Type())
hm2LogTempHistTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogTempHistTime.setStatus(_A)
_Hm2LogAuditGroup_ObjectIdentity=ObjectIdentity
hm2LogAuditGroup=_Hm2LogAuditGroup_ObjectIdentity((1,3,6,1,4,1,248,11,23,1,9))
class _Hm2LogAuditTrailComment_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,80))
_Hm2LogAuditTrailComment_Type.__name__=_T
_Hm2LogAuditTrailComment_Object=MibScalar
hm2LogAuditTrailComment=_Hm2LogAuditTrailComment_Object((1,3,6,1,4,1,248,11,23,1,9,1),_Hm2LogAuditTrailComment_Type())
hm2LogAuditTrailComment.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogAuditTrailComment.setStatus(_A)
_Hm2LogEmailAlertGroup_ObjectIdentity=ObjectIdentity
hm2LogEmailAlertGroup=_Hm2LogEmailAlertGroup_ObjectIdentity((1,3,6,1,4,1,248,11,23,1,10))
class _Hm2LogEmailAdminStatus_Type(HmEnabledStatus):defaultValue=2
_Hm2LogEmailAdminStatus_Type.__name__=_H
_Hm2LogEmailAdminStatus_Object=MibScalar
hm2LogEmailAdminStatus=_Hm2LogEmailAdminStatus_Object((1,3,6,1,4,1,248,11,23,1,10,1),_Hm2LogEmailAdminStatus_Type())
hm2LogEmailAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogEmailAdminStatus.setStatus(_A)
class _Hm2LogEmailFromAddress_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2LogEmailFromAddress_Type.__name__=_I
_Hm2LogEmailFromAddress_Object=MibScalar
hm2LogEmailFromAddress=_Hm2LogEmailFromAddress_Object((1,3,6,1,4,1,248,11,23,1,10,2),_Hm2LogEmailFromAddress_Type())
hm2LogEmailFromAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogEmailFromAddress.setStatus(_A)
class _Hm2LogEmailLogDuration_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,1440))
_Hm2LogEmailLogDuration_Type.__name__=_E
_Hm2LogEmailLogDuration_Object=MibScalar
hm2LogEmailLogDuration=_Hm2LogEmailLogDuration_Object((1,3,6,1,4,1,248,11,23,1,10,3),_Hm2LogEmailLogDuration_Type())
hm2LogEmailLogDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogEmailLogDuration.setStatus(_A)
class _Hm2LogEmailUrgentSeverity_Type(HmAgentLogSeverity):defaultValue=1
_Hm2LogEmailUrgentSeverity_Type.__name__=_G
_Hm2LogEmailUrgentSeverity_Object=MibScalar
hm2LogEmailUrgentSeverity=_Hm2LogEmailUrgentSeverity_Object((1,3,6,1,4,1,248,11,23,1,10,4),_Hm2LogEmailUrgentSeverity_Type())
hm2LogEmailUrgentSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogEmailUrgentSeverity.setStatus(_A)
class _Hm2LogEmailNonUrgentSeverity_Type(HmAgentLogSeverity):defaultValue=4
_Hm2LogEmailNonUrgentSeverity_Type.__name__=_G
_Hm2LogEmailNonUrgentSeverity_Object=MibScalar
hm2LogEmailNonUrgentSeverity=_Hm2LogEmailNonUrgentSeverity_Object((1,3,6,1,4,1,248,11,23,1,10,5),_Hm2LogEmailNonUrgentSeverity_Type())
hm2LogEmailNonUrgentSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogEmailNonUrgentSeverity.setStatus(_A)
_Hm2LogEmailNumEmailsSent_Type=Counter32
_Hm2LogEmailNumEmailsSent_Object=MibScalar
hm2LogEmailNumEmailsSent=_Hm2LogEmailNumEmailsSent_Object((1,3,6,1,4,1,248,11,23,1,10,6),_Hm2LogEmailNumEmailsSent_Type())
hm2LogEmailNumEmailsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogEmailNumEmailsSent.setStatus(_A)
_Hm2LogEmailNumEmailFailures_Type=Counter32
_Hm2LogEmailNumEmailFailures_Object=MibScalar
hm2LogEmailNumEmailFailures=_Hm2LogEmailNumEmailFailures_Object((1,3,6,1,4,1,248,11,23,1,10,7),_Hm2LogEmailNumEmailFailures_Type())
hm2LogEmailNumEmailFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogEmailNumEmailFailures.setStatus(_A)
_Hm2LogEmailTimeOfLastMailSent_Type=HmTimeSeconds1970
_Hm2LogEmailTimeOfLastMailSent_Object=MibScalar
hm2LogEmailTimeOfLastMailSent=_Hm2LogEmailTimeOfLastMailSent_Object((1,3,6,1,4,1,248,11,23,1,10,8),_Hm2LogEmailTimeOfLastMailSent_Type())
hm2LogEmailTimeOfLastMailSent.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogEmailTimeOfLastMailSent.setStatus(_A)
class _Hm2LogEmailAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('test',2),(_L,3)))
_Hm2LogEmailAction_Type.__name__=_E
_Hm2LogEmailAction_Object=MibScalar
hm2LogEmailAction=_Hm2LogEmailAction_Object((1,3,6,1,4,1,248,11,23,1,10,9),_Hm2LogEmailAction_Type())
hm2LogEmailAction.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogEmailAction.setStatus(_A)
class _Hm2LogEmailTestMessageType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_L,2)))
_Hm2LogEmailTestMessageType_Type.__name__=_E
_Hm2LogEmailTestMessageType_Object=MibScalar
hm2LogEmailTestMessageType=_Hm2LogEmailTestMessageType_Object((1,3,6,1,4,1,248,11,23,1,10,10),_Hm2LogEmailTestMessageType_Type())
hm2LogEmailTestMessageType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogEmailTestMessageType.setStatus(_A)
class _Hm2LogEmailTestMessageBody_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2LogEmailTestMessageBody_Type.__name__=_I
_Hm2LogEmailTestMessageBody_Object=MibScalar
hm2LogEmailTestMessageBody=_Hm2LogEmailTestMessageBody_Object((1,3,6,1,4,1,248,11,23,1,10,11),_Hm2LogEmailTestMessageBody_Type())
hm2LogEmailTestMessageBody.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogEmailTestMessageBody.setStatus(_A)
_Hm2LogEmailToAddressTable_Object=MibTable
hm2LogEmailToAddressTable=_Hm2LogEmailToAddressTable_Object((1,3,6,1,4,1,248,11,23,1,10,15))
if mibBuilder.loadTexts:hm2LogEmailToAddressTable.setStatus(_A)
_Hm2LogEmailToAddressEntry_Object=MibTableRow
hm2LogEmailToAddressEntry=_Hm2LogEmailToAddressEntry_Object((1,3,6,1,4,1,248,11,23,1,10,15,1))
hm2LogEmailToAddressEntry.setIndexNames((0,_F,_Z))
if mibBuilder.loadTexts:hm2LogEmailToAddressEntry.setStatus(_A)
class _Hm2LogEmailToAddrMessageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Hm2LogEmailToAddrMessageIndex_Type.__name__=_E
_Hm2LogEmailToAddrMessageIndex_Object=MibTableColumn
hm2LogEmailToAddrMessageIndex=_Hm2LogEmailToAddrMessageIndex_Object((1,3,6,1,4,1,248,11,23,1,10,15,1,1),_Hm2LogEmailToAddrMessageIndex_Type())
hm2LogEmailToAddrMessageIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hm2LogEmailToAddrMessageIndex.setStatus(_A)
class _Hm2LogEmailToAddrMessageType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_L,2)))
_Hm2LogEmailToAddrMessageType_Type.__name__=_E
_Hm2LogEmailToAddrMessageType_Object=MibTableColumn
hm2LogEmailToAddrMessageType=_Hm2LogEmailToAddrMessageType_Object((1,3,6,1,4,1,248,11,23,1,10,15,1,2),_Hm2LogEmailToAddrMessageType_Type())
hm2LogEmailToAddrMessageType.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogEmailToAddrMessageType.setStatus(_A)
class _Hm2LogEmailToAddrAddress_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2LogEmailToAddrAddress_Type.__name__=_I
_Hm2LogEmailToAddrAddress_Object=MibTableColumn
hm2LogEmailToAddrAddress=_Hm2LogEmailToAddrAddress_Object((1,3,6,1,4,1,248,11,23,1,10,15,1,3),_Hm2LogEmailToAddrAddress_Type())
hm2LogEmailToAddrAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogEmailToAddrAddress.setStatus(_A)
_Hm2LogEmailToAddrEntryStatus_Type=RowStatus
_Hm2LogEmailToAddrEntryStatus_Object=MibTableColumn
hm2LogEmailToAddrEntryStatus=_Hm2LogEmailToAddrEntryStatus_Object((1,3,6,1,4,1,248,11,23,1,10,15,1,4),_Hm2LogEmailToAddrEntryStatus_Type())
hm2LogEmailToAddrEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogEmailToAddrEntryStatus.setStatus(_A)
_Hm2LogEmailSubjectTable_Object=MibTable
hm2LogEmailSubjectTable=_Hm2LogEmailSubjectTable_Object((1,3,6,1,4,1,248,11,23,1,10,16))
if mibBuilder.loadTexts:hm2LogEmailSubjectTable.setStatus(_A)
_Hm2LogEmailSubjectEntry_Object=MibTableRow
hm2LogEmailSubjectEntry=_Hm2LogEmailSubjectEntry_Object((1,3,6,1,4,1,248,11,23,1,10,16,1))
hm2LogEmailSubjectEntry.setIndexNames((0,_F,_a))
if mibBuilder.loadTexts:hm2LogEmailSubjectEntry.setStatus(_A)
class _Hm2LogEmailSubjectMessageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_L,2)))
_Hm2LogEmailSubjectMessageType_Type.__name__=_E
_Hm2LogEmailSubjectMessageType_Object=MibTableColumn
hm2LogEmailSubjectMessageType=_Hm2LogEmailSubjectMessageType_Object((1,3,6,1,4,1,248,11,23,1,10,16,1,1),_Hm2LogEmailSubjectMessageType_Type())
hm2LogEmailSubjectMessageType.setMaxAccess(_J)
if mibBuilder.loadTexts:hm2LogEmailSubjectMessageType.setStatus(_A)
class _Hm2LogEmailSubject_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2LogEmailSubject_Type.__name__=_I
_Hm2LogEmailSubject_Object=MibTableColumn
hm2LogEmailSubject=_Hm2LogEmailSubject_Object((1,3,6,1,4,1,248,11,23,1,10,16,1,2),_Hm2LogEmailSubject_Type())
hm2LogEmailSubject.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogEmailSubject.setStatus(_A)
_Hm2LogEmailSubjectEntryStatus_Type=RowStatus
_Hm2LogEmailSubjectEntryStatus_Object=MibTableColumn
hm2LogEmailSubjectEntryStatus=_Hm2LogEmailSubjectEntryStatus_Object((1,3,6,1,4,1,248,11,23,1,10,16,1,3),_Hm2LogEmailSubjectEntryStatus_Type())
hm2LogEmailSubjectEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogEmailSubjectEntryStatus.setStatus(_A)
_Hm2LogEmailMailServerTable_Object=MibTable
hm2LogEmailMailServerTable=_Hm2LogEmailMailServerTable_Object((1,3,6,1,4,1,248,11,23,1,10,17))
if mibBuilder.loadTexts:hm2LogEmailMailServerTable.setStatus(_A)
_Hm2LogEmailMailServerEntry_Object=MibTableRow
hm2LogEmailMailServerEntry=_Hm2LogEmailMailServerEntry_Object((1,3,6,1,4,1,248,11,23,1,10,17,1))
hm2LogEmailMailServerEntry.setIndexNames((0,_F,_b))
if mibBuilder.loadTexts:hm2LogEmailMailServerEntry.setStatus(_A)
class _Hm2LogEmailSmtpAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Hm2LogEmailSmtpAddrIndex_Type.__name__=_E
_Hm2LogEmailSmtpAddrIndex_Object=MibTableColumn
hm2LogEmailSmtpAddrIndex=_Hm2LogEmailSmtpAddrIndex_Object((1,3,6,1,4,1,248,11,23,1,10,17,1,1),_Hm2LogEmailSmtpAddrIndex_Type())
hm2LogEmailSmtpAddrIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hm2LogEmailSmtpAddrIndex.setStatus(_A)
class _Hm2LogEmailSmtpAddrDescr_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2LogEmailSmtpAddrDescr_Type.__name__=_I
_Hm2LogEmailSmtpAddrDescr_Object=MibTableColumn
hm2LogEmailSmtpAddrDescr=_Hm2LogEmailSmtpAddrDescr_Object((1,3,6,1,4,1,248,11,23,1,10,17,1,2),_Hm2LogEmailSmtpAddrDescr_Type())
hm2LogEmailSmtpAddrDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogEmailSmtpAddrDescr.setStatus(_A)
class _Hm2LogEmailSmtpAddrType_Type(InetAddressType):defaultValue=1
_Hm2LogEmailSmtpAddrType_Type.__name__=_Q
_Hm2LogEmailSmtpAddrType_Object=MibTableColumn
hm2LogEmailSmtpAddrType=_Hm2LogEmailSmtpAddrType_Object((1,3,6,1,4,1,248,11,23,1,10,17,1,3),_Hm2LogEmailSmtpAddrType_Type())
hm2LogEmailSmtpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogEmailSmtpAddrType.setStatus(_A)
class _Hm2LogEmailSmtpAddr_Type(InetAddress):defaultHexValue=_V
_Hm2LogEmailSmtpAddr_Type.__name__=_P
_Hm2LogEmailSmtpAddr_Object=MibTableColumn
hm2LogEmailSmtpAddr=_Hm2LogEmailSmtpAddr_Object((1,3,6,1,4,1,248,11,23,1,10,17,1,4),_Hm2LogEmailSmtpAddr_Type())
hm2LogEmailSmtpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogEmailSmtpAddr.setStatus(_A)
class _Hm2LogEmailSmtpPort_Type(InetPortNumber):defaultValue=25
_Hm2LogEmailSmtpPort_Type.__name__=_R
_Hm2LogEmailSmtpPort_Object=MibTableColumn
hm2LogEmailSmtpPort=_Hm2LogEmailSmtpPort_Object((1,3,6,1,4,1,248,11,23,1,10,17,1,5),_Hm2LogEmailSmtpPort_Type())
hm2LogEmailSmtpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogEmailSmtpPort.setStatus(_A)
class _Hm2LogEmailSmtpSecurity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('tlsv1',2)))
_Hm2LogEmailSmtpSecurity_Type.__name__=_E
_Hm2LogEmailSmtpSecurity_Object=MibTableColumn
hm2LogEmailSmtpSecurity=_Hm2LogEmailSmtpSecurity_Object((1,3,6,1,4,1,248,11,23,1,10,17,1,6),_Hm2LogEmailSmtpSecurity_Type())
hm2LogEmailSmtpSecurity.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogEmailSmtpSecurity.setStatus(_A)
class _Hm2LogEmailSmtpLoginID_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2LogEmailSmtpLoginID_Type.__name__=_I
_Hm2LogEmailSmtpLoginID_Object=MibTableColumn
hm2LogEmailSmtpLoginID=_Hm2LogEmailSmtpLoginID_Object((1,3,6,1,4,1,248,11,23,1,10,17,1,7),_Hm2LogEmailSmtpLoginID_Type())
hm2LogEmailSmtpLoginID.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogEmailSmtpLoginID.setStatus(_A)
class _Hm2LogEmailSmtpPassword_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2LogEmailSmtpPassword_Type.__name__=_I
_Hm2LogEmailSmtpPassword_Object=MibTableColumn
hm2LogEmailSmtpPassword=_Hm2LogEmailSmtpPassword_Object((1,3,6,1,4,1,248,11,23,1,10,17,1,8),_Hm2LogEmailSmtpPassword_Type())
hm2LogEmailSmtpPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogEmailSmtpPassword.setStatus(_A)
_Hm2LogEmailSmtpEntryStatus_Type=RowStatus
_Hm2LogEmailSmtpEntryStatus_Object=MibTableColumn
hm2LogEmailSmtpEntryStatus=_Hm2LogEmailSmtpEntryStatus_Object((1,3,6,1,4,1,248,11,23,1,10,17,1,9),_Hm2LogEmailSmtpEntryStatus_Type())
hm2LogEmailSmtpEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogEmailSmtpEntryStatus.setStatus(_A)
class _Hm2LogEmailSmtpTimeout_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Hm2LogEmailSmtpTimeout_Type.__name__=_K
_Hm2LogEmailSmtpTimeout_Object=MibTableColumn
hm2LogEmailSmtpTimeout=_Hm2LogEmailSmtpTimeout_Object((1,3,6,1,4,1,248,11,23,1,10,17,1,10),_Hm2LogEmailSmtpTimeout_Type())
hm2LogEmailSmtpTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2LogEmailSmtpTimeout.setStatus(_A)
class _Hm2LogEmailClientTlsVersions_Type(Hm2TlsVersions):defaultBinValue='101'
_Hm2LogEmailClientTlsVersions_Type.__name__=_O
_Hm2LogEmailClientTlsVersions_Object=MibScalar
hm2LogEmailClientTlsVersions=_Hm2LogEmailClientTlsVersions_Object((1,3,6,1,4,1,248,11,23,1,10,18),_Hm2LogEmailClientTlsVersions_Type())
hm2LogEmailClientTlsVersions.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogEmailClientTlsVersions.setStatus(_A)
class _Hm2LogEmailClientTlsCipherSuites_Type(Hm2TlsCipherSuites):defaultBinValue='0010101'
_Hm2LogEmailClientTlsCipherSuites_Type.__name__=_N
_Hm2LogEmailClientTlsCipherSuites_Object=MibScalar
hm2LogEmailClientTlsCipherSuites=_Hm2LogEmailClientTlsCipherSuites_Object((1,3,6,1,4,1,248,11,23,1,10,19),_Hm2LogEmailClientTlsCipherSuites_Type())
hm2LogEmailClientTlsCipherSuites.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LogEmailClientTlsCipherSuites.setStatus(_A)
_Hm2LogHumidityGroup_ObjectIdentity=ObjectIdentity
hm2LogHumidityGroup=_Hm2LogHumidityGroup_ObjectIdentity((1,3,6,1,4,1,248,11,23,1,11))
class _Hm2LogHumMinimum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hm2LogHumMinimum_Type.__name__=_K
_Hm2LogHumMinimum_Object=MibScalar
hm2LogHumMinimum=_Hm2LogHumMinimum_Object((1,3,6,1,4,1,248,11,23,1,11,1),_Hm2LogHumMinimum_Type())
hm2LogHumMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogHumMinimum.setStatus(_A)
if mibBuilder.loadTexts:hm2LogHumMinimum.setUnits(_M)
class _Hm2LogHumMaximum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hm2LogHumMaximum_Type.__name__=_K
_Hm2LogHumMaximum_Object=MibScalar
hm2LogHumMaximum=_Hm2LogHumMaximum_Object((1,3,6,1,4,1,248,11,23,1,11,2),_Hm2LogHumMaximum_Type())
hm2LogHumMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogHumMaximum.setStatus(_A)
if mibBuilder.loadTexts:hm2LogHumMaximum.setUnits(_M)
_Hm2LogHumHistTable_Object=MibTable
hm2LogHumHistTable=_Hm2LogHumHistTable_Object((1,3,6,1,4,1,248,11,23,1,11,10))
if mibBuilder.loadTexts:hm2LogHumHistTable.setStatus(_A)
_Hm2LogHumHistEntry_Object=MibTableRow
hm2LogHumHistEntry=_Hm2LogHumHistEntry_Object((1,3,6,1,4,1,248,11,23,1,11,10,1))
hm2LogHumHistEntry.setIndexNames((0,_F,_c))
if mibBuilder.loadTexts:hm2LogHumHistEntry.setStatus(_A)
_Hm2LogHumHistIndex_Type=Unsigned32
_Hm2LogHumHistIndex_Object=MibTableColumn
hm2LogHumHistIndex=_Hm2LogHumHistIndex_Object((1,3,6,1,4,1,248,11,23,1,11,10,1,1),_Hm2LogHumHistIndex_Type())
hm2LogHumHistIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hm2LogHumHistIndex.setStatus(_A)
class _Hm2LogHumHistRangeMin_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hm2LogHumHistRangeMin_Type.__name__=_K
_Hm2LogHumHistRangeMin_Object=MibTableColumn
hm2LogHumHistRangeMin=_Hm2LogHumHistRangeMin_Object((1,3,6,1,4,1,248,11,23,1,11,10,1,2),_Hm2LogHumHistRangeMin_Type())
hm2LogHumHistRangeMin.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogHumHistRangeMin.setStatus(_A)
if mibBuilder.loadTexts:hm2LogHumHistRangeMin.setUnits(_M)
class _Hm2LogHumHistRangeMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hm2LogHumHistRangeMax_Type.__name__=_K
_Hm2LogHumHistRangeMax_Object=MibTableColumn
hm2LogHumHistRangeMax=_Hm2LogHumHistRangeMax_Object((1,3,6,1,4,1,248,11,23,1,11,10,1,3),_Hm2LogHumHistRangeMax_Type())
hm2LogHumHistRangeMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogHumHistRangeMax.setStatus(_A)
if mibBuilder.loadTexts:hm2LogHumHistRangeMax.setUnits(_M)
_Hm2LogHumHistTime_Type=Unsigned32
_Hm2LogHumHistTime_Object=MibTableColumn
hm2LogHumHistTime=_Hm2LogHumHistTime_Object((1,3,6,1,4,1,248,11,23,1,11,10,1,4),_Hm2LogHumHistTime_Type())
hm2LogHumHistTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LogHumHistTime.setStatus(_A)
if mibBuilder.loadTexts:hm2LogHumHistTime.setUnits('minutes')
_Hm2LogSNMPExtensionGroup_ObjectIdentity=ObjectIdentity
hm2LogSNMPExtensionGroup=_Hm2LogSNMPExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,23,3))
_Hm2LogSNMPSyslogConfigFailed_ObjectIdentity=ObjectIdentity
hm2LogSNMPSyslogConfigFailed=_Hm2LogSNMPSyslogConfigFailed_ObjectIdentity((1,3,6,1,4,1,248,11,23,3,1))
if mibBuilder.loadTexts:hm2LogSNMPSyslogConfigFailed.setStatus(_A)
_Hm2LogSNMPMinSeverityInvalid_ObjectIdentity=ObjectIdentity
hm2LogSNMPMinSeverityInvalid=_Hm2LogSNMPMinSeverityInvalid_ObjectIdentity((1,3,6,1,4,1,248,11,23,3,2))
if mibBuilder.loadTexts:hm2LogSNMPMinSeverityInvalid.setStatus(_A)
hm2LogAuditStartNextSector=NotificationType((1,3,6,1,4,1,248,11,23,0,1))
if mibBuilder.loadTexts:hm2LogAuditStartNextSector.setStatus(_A)
hm2LogEmailSendFailed=NotificationType((1,3,6,1,4,1,248,11,23,0,2))
hm2LogEmailSendFailed.setObjects((_F,_d))
if mibBuilder.loadTexts:hm2LogEmailSendFailed.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_G:HmAgentLogSeverity,'hm2LoggingMib':hm2LoggingMib,'hm2LoggingMibNotifications':hm2LoggingMibNotifications,'hm2LogAuditStartNextSector':hm2LogAuditStartNextSector,'hm2LogEmailSendFailed':hm2LogEmailSendFailed,'hm2LoggingMibObjects':hm2LoggingMibObjects,'hm2LogSnmpLoggingGroup':hm2LogSnmpLoggingGroup,'hm2LogSnmpLogGetRequest':hm2LogSnmpLogGetRequest,'hm2LogSnmpLogSetRequest':hm2LogSnmpLogSetRequest,'hm2LogSnmpLogGetSeverity':hm2LogSnmpLogGetSeverity,'hm2LogSnmpLogSetSeverity':hm2LogSnmpLogSetSeverity,'hm2LogCliCommandsLoggingGroup':hm2LogCliCommandsLoggingGroup,'hm2LogCliCommandsAdminStatus':hm2LogCliCommandsAdminStatus,'hm2LogConsoleLoggingGroup':hm2LogConsoleLoggingGroup,'hm2LogConsoleAdminStatus':hm2LogConsoleAdminStatus,'hm2LogConsoleSeverityFilter':hm2LogConsoleSeverityFilter,'hm2LogBufferedLoggingGroup':hm2LogBufferedLoggingGroup,'hm2LogBufferdLogLevelThreshold':hm2LogBufferdLogLevelThreshold,'hm2LogSyslogGroup':hm2LogSyslogGroup,'hm2LogSyslogAdminStatus':hm2LogSyslogAdminStatus,'hm2LogSyslogClientTlsVersions':hm2LogSyslogClientTlsVersions,'hm2LogSyslogClientTlsCipherSuites':hm2LogSyslogClientTlsCipherSuites,'hm2LogSyslogServerTable':hm2LogSyslogServerTable,'hm2LogSyslogServerEntry':hm2LogSyslogServerEntry,_U:hm2LogSyslogServerIndex,'hm2LogSyslogServerIPAddrType':hm2LogSyslogServerIPAddrType,'hm2LogSyslogServerIPAddr':hm2LogSyslogServerIPAddr,'hm2LogSyslogServerUdpPort':hm2LogSyslogServerUdpPort,'hm2LogSyslogServerLevelUpto':hm2LogSyslogServerLevelUpto,'hm2LogSyslogServerLogType':hm2LogSyslogServerLogType,'hm2LogSyslogServerRowStatus':hm2LogSyslogServerRowStatus,'hm2LogSyslogServerTransportType':hm2LogSyslogServerTransportType,'hm2LogPersistentGroup':hm2LogPersistentGroup,'hm2LogPersistAdminStatus':hm2LogPersistAdminStatus,'hm2LogPersistMaxFileSize':hm2LogPersistMaxFileSize,'hm2LogPersistFilesMax':hm2LogPersistFilesMax,'hm2LogPersistLevelUpto':hm2LogPersistLevelUpto,'hm2LogPersistentFileTable':hm2LogPersistentFileTable,'hm2LogPersistentFileEntry':hm2LogPersistentFileEntry,_W:hm2LogPersistentFileIndex,'hm2LogPersistentFileName':hm2LogPersistentFileName,'hm2LogPersistentFileSize':hm2LogPersistentFileSize,'hm2LogCounterGroup':hm2LogCounterGroup,'hm2LogCounterOperatingHours':hm2LogCounterOperatingHours,'hm2LogCounterFlashTable':hm2LogCounterFlashTable,'hm2LogCounterFlashEntry':hm2LogCounterFlashEntry,_X:hm2LogCounterFlashBlock,'hm2LogCounterFlashDescription':hm2LogCounterFlashDescription,'hm2LogCounterFlashCount':hm2LogCounterFlashCount,'hm2LogCounterFlashValue':hm2LogCounterFlashValue,'hm2LogTemperatureGroup':hm2LogTemperatureGroup,'hm2LogTempMinimum':hm2LogTempMinimum,'hm2LogTempMaximum':hm2LogTempMaximum,'hm2LogTempVariationCount':hm2LogTempVariationCount,'hm2LogTempHistTable':hm2LogTempHistTable,'hm2LogTempHistEntry':hm2LogTempHistEntry,_Y:hm2LogTempHistIndex,'hm2LogTempHistRangeMin':hm2LogTempHistRangeMin,'hm2LogTempHistRangeMax':hm2LogTempHistRangeMax,'hm2LogTempHistTime':hm2LogTempHistTime,'hm2LogAuditGroup':hm2LogAuditGroup,'hm2LogAuditTrailComment':hm2LogAuditTrailComment,'hm2LogEmailAlertGroup':hm2LogEmailAlertGroup,'hm2LogEmailAdminStatus':hm2LogEmailAdminStatus,'hm2LogEmailFromAddress':hm2LogEmailFromAddress,'hm2LogEmailLogDuration':hm2LogEmailLogDuration,'hm2LogEmailUrgentSeverity':hm2LogEmailUrgentSeverity,'hm2LogEmailNonUrgentSeverity':hm2LogEmailNonUrgentSeverity,'hm2LogEmailNumEmailsSent':hm2LogEmailNumEmailsSent,_d:hm2LogEmailNumEmailFailures,'hm2LogEmailTimeOfLastMailSent':hm2LogEmailTimeOfLastMailSent,'hm2LogEmailAction':hm2LogEmailAction,'hm2LogEmailTestMessageType':hm2LogEmailTestMessageType,'hm2LogEmailTestMessageBody':hm2LogEmailTestMessageBody,'hm2LogEmailToAddressTable':hm2LogEmailToAddressTable,'hm2LogEmailToAddressEntry':hm2LogEmailToAddressEntry,_Z:hm2LogEmailToAddrMessageIndex,'hm2LogEmailToAddrMessageType':hm2LogEmailToAddrMessageType,'hm2LogEmailToAddrAddress':hm2LogEmailToAddrAddress,'hm2LogEmailToAddrEntryStatus':hm2LogEmailToAddrEntryStatus,'hm2LogEmailSubjectTable':hm2LogEmailSubjectTable,'hm2LogEmailSubjectEntry':hm2LogEmailSubjectEntry,_a:hm2LogEmailSubjectMessageType,'hm2LogEmailSubject':hm2LogEmailSubject,'hm2LogEmailSubjectEntryStatus':hm2LogEmailSubjectEntryStatus,'hm2LogEmailMailServerTable':hm2LogEmailMailServerTable,'hm2LogEmailMailServerEntry':hm2LogEmailMailServerEntry,_b:hm2LogEmailSmtpAddrIndex,'hm2LogEmailSmtpAddrDescr':hm2LogEmailSmtpAddrDescr,'hm2LogEmailSmtpAddrType':hm2LogEmailSmtpAddrType,'hm2LogEmailSmtpAddr':hm2LogEmailSmtpAddr,'hm2LogEmailSmtpPort':hm2LogEmailSmtpPort,'hm2LogEmailSmtpSecurity':hm2LogEmailSmtpSecurity,'hm2LogEmailSmtpLoginID':hm2LogEmailSmtpLoginID,'hm2LogEmailSmtpPassword':hm2LogEmailSmtpPassword,'hm2LogEmailSmtpEntryStatus':hm2LogEmailSmtpEntryStatus,'hm2LogEmailSmtpTimeout':hm2LogEmailSmtpTimeout,'hm2LogEmailClientTlsVersions':hm2LogEmailClientTlsVersions,'hm2LogEmailClientTlsCipherSuites':hm2LogEmailClientTlsCipherSuites,'hm2LogHumidityGroup':hm2LogHumidityGroup,'hm2LogHumMinimum':hm2LogHumMinimum,'hm2LogHumMaximum':hm2LogHumMaximum,'hm2LogHumHistTable':hm2LogHumHistTable,'hm2LogHumHistEntry':hm2LogHumHistEntry,_c:hm2LogHumHistIndex,'hm2LogHumHistRangeMin':hm2LogHumHistRangeMin,'hm2LogHumHistRangeMax':hm2LogHumHistRangeMax,'hm2LogHumHistTime':hm2LogHumHistTime,'hm2LogSNMPExtensionGroup':hm2LogSNMPExtensionGroup,'hm2LogSNMPSyslogConfigFailed':hm2LogSNMPSyslogConfigFailed,'hm2LogSNMPMinSeverityInvalid':hm2LogSNMPMinSeverityInvalid})