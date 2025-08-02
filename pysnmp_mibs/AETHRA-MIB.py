_e='genericError'
_d='usTermDectIndex'
_c='usTermISDNIndex'
_b='usTermPotsIndex'
_a='trunkFxoIndex'
_Z='trunkIsdnIndex'
_Y='trunkIndex'
_X='shdslIndex'
_W='xdslIndex'
_V='NotificationType'
_U='ifIndex'
_T='mgmtPrivilege'
_S='trunkName'
_R='ifDescr'
_Q='mgmtAddress'
_P='mgmtType'
_O='mgmtTime'
_N='mgmtUser'
_M='on'
_L='off'
_K='noaction'
_J='IF-MIB'
_I='disable'
_H='enable'
_G='DisplayString'
_F='current'
_E='AETHRA-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
ifDescr,ifIndex=mibBuilder.importSymbols(_J,_R,_U)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_V,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_V,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_Aethra_ObjectIdentity=ObjectIdentity
aethra=_Aethra_ObjectIdentity((1,3,6,1,4,1,7745))
_Atosnt_ObjectIdentity=ObjectIdentity
atosnt=_Atosnt_ObjectIdentity((1,3,6,1,4,1,7745,5))
_Tools_ObjectIdentity=ObjectIdentity
tools=_Tools_ObjectIdentity((1,3,6,1,4,1,7745,5,1))
_FileTransfer_ObjectIdentity=ObjectIdentity
fileTransfer=_FileTransfer_ObjectIdentity((1,3,6,1,4,1,7745,5,1,1))
class _FileTransferProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('tftp',1),('ftp',2),('http',3),('file',4),('scp',5)))
_FileTransferProtocol_Type.__name__=_D
_FileTransferProtocol_Object=MibScalar
fileTransferProtocol=_FileTransferProtocol_Object((1,3,6,1,4,1,7745,5,1,1,1),_FileTransferProtocol_Type())
fileTransferProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:fileTransferProtocol.setStatus(_A)
_FileTransferFileName_Type=DisplayString
_FileTransferFileName_Object=MibScalar
fileTransferFileName=_FileTransferFileName_Object((1,3,6,1,4,1,7745,5,1,1,2),_FileTransferFileName_Type())
fileTransferFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:fileTransferFileName.setStatus(_A)
_FileTransferServerName_Type=DisplayString
_FileTransferServerName_Object=MibScalar
fileTransferServerName=_FileTransferServerName_Object((1,3,6,1,4,1,7745,5,1,1,3),_FileTransferServerName_Type())
fileTransferServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:fileTransferServerName.setStatus(_A)
class _FileTransferOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('firmware',1),('boot',2),('userconf',3),('logs',4),('package',5),('localfile',6),('welcome',7),('license',8),('certificate',9),('defaultconf',10),('bannerPre',11),('bannerPost',12)))
_FileTransferOption_Type.__name__=_D
_FileTransferOption_Object=MibScalar
fileTransferOption=_FileTransferOption_Object((1,3,6,1,4,1,7745,5,1,1,4),_FileTransferOption_Type())
fileTransferOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fileTransferOption.setStatus(_A)
_FileTransferStorageFileName_Type=DisplayString
_FileTransferStorageFileName_Object=MibScalar
fileTransferStorageFileName=_FileTransferStorageFileName_Object((1,3,6,1,4,1,7745,5,1,1,5),_FileTransferStorageFileName_Type())
fileTransferStorageFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:fileTransferStorageFileName.setStatus(_A)
class _FileTransferExec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),('download',1),('upload',2)))
_FileTransferExec_Type.__name__=_D
_FileTransferExec_Object=MibScalar
fileTransferExec=_FileTransferExec_Object((1,3,6,1,4,1,7745,5,1,1,6),_FileTransferExec_Type())
fileTransferExec.setMaxAccess(_C)
if mibBuilder.loadTexts:fileTransferExec.setStatus(_A)
_FileTransferStatus_Type=DisplayString
_FileTransferStatus_Object=MibScalar
fileTransferStatus=_FileTransferStatus_Object((1,3,6,1,4,1,7745,5,1,1,7),_FileTransferStatus_Type())
fileTransferStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fileTransferStatus.setStatus(_A)
_Ping_ObjectIdentity=ObjectIdentity
ping=_Ping_ObjectIdentity((1,3,6,1,4,1,7745,5,1,2))
_PingParameters_ObjectIdentity=ObjectIdentity
pingParameters=_PingParameters_ObjectIdentity((1,3,6,1,4,1,7745,5,1,2,1))
_PingHost_Type=DisplayString
_PingHost_Object=MibScalar
pingHost=_PingHost_Object((1,3,6,1,4,1,7745,5,1,2,1,1),_PingHost_Type())
pingHost.setMaxAccess(_C)
if mibBuilder.loadTexts:pingHost.setStatus(_A)
class _PingSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_PingSize_Type.__name__=_D
_PingSize_Object=MibScalar
pingSize=_PingSize_Object((1,3,6,1,4,1,7745,5,1,2,1,2),_PingSize_Type())
pingSize.setMaxAccess(_C)
if mibBuilder.loadTexts:pingSize.setStatus(_A)
class _PingTries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PingTries_Type.__name__=_D
_PingTries_Object=MibScalar
pingTries=_PingTries_Object((1,3,6,1,4,1,7745,5,1,2,1,3),_PingTries_Type())
pingTries.setMaxAccess(_C)
if mibBuilder.loadTexts:pingTries.setStatus(_A)
class _PingTTL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PingTTL_Type.__name__=_D
_PingTTL_Object=MibScalar
pingTTL=_PingTTL_Object((1,3,6,1,4,1,7745,5,1,2,1,4),_PingTTL_Type())
pingTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:pingTTL.setStatus(_A)
class _PingTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PingTimeOut_Type.__name__=_D
_PingTimeOut_Object=MibScalar
pingTimeOut=_PingTimeOut_Object((1,3,6,1,4,1,7745,5,1,2,1,5),_PingTimeOut_Type())
pingTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:pingTimeOut.setStatus(_A)
_PingSource_Type=DisplayString
_PingSource_Object=MibScalar
pingSource=_PingSource_Object((1,3,6,1,4,1,7745,5,1,2,1,6),_PingSource_Type())
pingSource.setMaxAccess(_C)
if mibBuilder.loadTexts:pingSource.setStatus(_A)
class _PingStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),('start',1)))
_PingStart_Type.__name__=_D
_PingStart_Object=MibScalar
pingStart=_PingStart_Object((1,3,6,1,4,1,7745,5,1,2,1,7),_PingStart_Type())
pingStart.setMaxAccess(_C)
if mibBuilder.loadTexts:pingStart.setStatus(_A)
_PingStatus_Type=DisplayString
_PingStatus_Object=MibScalar
pingStatus=_PingStatus_Object((1,3,6,1,4,1,7745,5,1,2,1,8),_PingStatus_Type())
pingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pingStatus.setStatus(_A)
_PingStatistics_ObjectIdentity=ObjectIdentity
pingStatistics=_PingStatistics_ObjectIdentity((1,3,6,1,4,1,7745,5,1,2,2))
_PingTXpacket_Type=Integer32
_PingTXpacket_Object=MibScalar
pingTXpacket=_PingTXpacket_Object((1,3,6,1,4,1,7745,5,1,2,2,1),_PingTXpacket_Type())
pingTXpacket.setMaxAccess(_B)
if mibBuilder.loadTexts:pingTXpacket.setStatus(_A)
_PingRXpacket_Type=Integer32
_PingRXpacket_Object=MibScalar
pingRXpacket=_PingRXpacket_Object((1,3,6,1,4,1,7745,5,1,2,2,2),_PingRXpacket_Type())
pingRXpacket.setMaxAccess(_B)
if mibBuilder.loadTexts:pingRXpacket.setStatus(_A)
_PingLOSTpacket_Type=Integer32
_PingLOSTpacket_Object=MibScalar
pingLOSTpacket=_PingLOSTpacket_Object((1,3,6,1,4,1,7745,5,1,2,2,3),_PingLOSTpacket_Type())
pingLOSTpacket.setMaxAccess(_B)
if mibBuilder.loadTexts:pingLOSTpacket.setStatus(_A)
_PingMinRTT_Type=Integer32
_PingMinRTT_Object=MibScalar
pingMinRTT=_PingMinRTT_Object((1,3,6,1,4,1,7745,5,1,2,2,4),_PingMinRTT_Type())
pingMinRTT.setMaxAccess(_B)
if mibBuilder.loadTexts:pingMinRTT.setStatus(_A)
_PingMaxRTT_Type=Integer32
_PingMaxRTT_Object=MibScalar
pingMaxRTT=_PingMaxRTT_Object((1,3,6,1,4,1,7745,5,1,2,2,5),_PingMaxRTT_Type())
pingMaxRTT.setMaxAccess(_B)
if mibBuilder.loadTexts:pingMaxRTT.setStatus(_A)
_PingAvgRTT_Type=Integer32
_PingAvgRTT_Object=MibScalar
pingAvgRTT=_PingAvgRTT_Object((1,3,6,1,4,1,7745,5,1,2,2,6),_PingAvgRTT_Type())
pingAvgRTT.setMaxAccess(_B)
if mibBuilder.loadTexts:pingAvgRTT.setStatus(_A)
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,4,1,7745,5,2))
class _SystemLoglevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_SystemLoglevel_Type.__name__=_D
_SystemLoglevel_Object=MibScalar
systemLoglevel=_SystemLoglevel_Object((1,3,6,1,4,1,7745,5,2,1),_SystemLoglevel_Type())
systemLoglevel.setMaxAccess(_C)
if mibBuilder.loadTexts:systemLoglevel.setStatus(_A)
_SystemDescription_Type=DisplayString
_SystemDescription_Object=MibScalar
systemDescription=_SystemDescription_Object((1,3,6,1,4,1,7745,5,2,2),_SystemDescription_Type())
systemDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:systemDescription.setStatus(_A)
_SystemName_Type=DisplayString
_SystemName_Object=MibScalar
systemName=_SystemName_Object((1,3,6,1,4,1,7745,5,2,3),_SystemName_Type())
systemName.setMaxAccess(_C)
if mibBuilder.loadTexts:systemName.setStatus(_A)
_SystemLocalDomain_Type=DisplayString
_SystemLocalDomain_Object=MibScalar
systemLocalDomain=_SystemLocalDomain_Object((1,3,6,1,4,1,7745,5,2,4),_SystemLocalDomain_Type())
systemLocalDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:systemLocalDomain.setStatus(_A)
_SystemDefaultTftpServer_Type=DisplayString
_SystemDefaultTftpServer_Object=MibScalar
systemDefaultTftpServer=_SystemDefaultTftpServer_Object((1,3,6,1,4,1,7745,5,2,5),_SystemDefaultTftpServer_Type())
systemDefaultTftpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:systemDefaultTftpServer.setStatus(_A)
_SystemTftpLocalAdd_Type=IpAddress
_SystemTftpLocalAdd_Object=MibScalar
systemTftpLocalAdd=_SystemTftpLocalAdd_Object((1,3,6,1,4,1,7745,5,2,6),_SystemTftpLocalAdd_Type())
systemTftpLocalAdd.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTftpLocalAdd.setStatus(_A)
_SystemDefaultFtpServer_Type=DisplayString
_SystemDefaultFtpServer_Object=MibScalar
systemDefaultFtpServer=_SystemDefaultFtpServer_Object((1,3,6,1,4,1,7745,5,2,7),_SystemDefaultFtpServer_Type())
systemDefaultFtpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:systemDefaultFtpServer.setStatus(_A)
_SystemFtpLocalAdd_Type=IpAddress
_SystemFtpLocalAdd_Object=MibScalar
systemFtpLocalAdd=_SystemFtpLocalAdd_Object((1,3,6,1,4,1,7745,5,2,8),_SystemFtpLocalAdd_Type())
systemFtpLocalAdd.setMaxAccess(_C)
if mibBuilder.loadTexts:systemFtpLocalAdd.setStatus(_A)
_SystemFtpUsername_Type=DisplayString
_SystemFtpUsername_Object=MibScalar
systemFtpUsername=_SystemFtpUsername_Object((1,3,6,1,4,1,7745,5,2,9),_SystemFtpUsername_Type())
systemFtpUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:systemFtpUsername.setStatus(_A)
_SystemFtpPassword_Type=DisplayString
_SystemFtpPassword_Object=MibScalar
systemFtpPassword=_SystemFtpPassword_Object((1,3,6,1,4,1,7745,5,2,10),_SystemFtpPassword_Type())
systemFtpPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:systemFtpPassword.setStatus(_A)
_SystemAAAProfile_Type=DisplayString
_SystemAAAProfile_Object=MibScalar
systemAAAProfile=_SystemAAAProfile_Object((1,3,6,1,4,1,7745,5,2,11),_SystemAAAProfile_Type())
systemAAAProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:systemAAAProfile.setStatus(_A)
class _SystemAAALogTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_SystemAAALogTimeout_Type.__name__=_D
_SystemAAALogTimeout_Object=MibScalar
systemAAALogTimeout=_SystemAAALogTimeout_Object((1,3,6,1,4,1,7745,5,2,12),_SystemAAALogTimeout_Type())
systemAAALogTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:systemAAALogTimeout.setStatus(_A)
class _SystemBackupAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_SystemBackupAuth_Type.__name__=_D
_SystemBackupAuth_Object=MibScalar
systemBackupAuth=_SystemBackupAuth_Object((1,3,6,1,4,1,7745,5,2,13),_SystemBackupAuth_Type())
systemBackupAuth.setMaxAccess(_C)
if mibBuilder.loadTexts:systemBackupAuth.setStatus(_A)
class _SystemScrollLine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SystemScrollLine_Type.__name__=_D
_SystemScrollLine_Object=MibScalar
systemScrollLine=_SystemScrollLine_Object((1,3,6,1,4,1,7745,5,2,14),_SystemScrollLine_Type())
systemScrollLine.setMaxAccess(_C)
if mibBuilder.loadTexts:systemScrollLine.setStatus(_A)
class _SystemKernelLogs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_SystemKernelLogs_Type.__name__=_D
_SystemKernelLogs_Object=MibScalar
systemKernelLogs=_SystemKernelLogs_Object((1,3,6,1,4,1,7745,5,2,15),_SystemKernelLogs_Type())
systemKernelLogs.setMaxAccess(_C)
if mibBuilder.loadTexts:systemKernelLogs.setStatus(_A)
class _SystemCryptedPassword_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_SystemCryptedPassword_Type.__name__=_D
_SystemCryptedPassword_Object=MibScalar
systemCryptedPassword=_SystemCryptedPassword_Object((1,3,6,1,4,1,7745,5,2,16),_SystemCryptedPassword_Type())
systemCryptedPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:systemCryptedPassword.setStatus(_A)
class _SystemSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),('save',1)))
_SystemSave_Type.__name__=_D
_SystemSave_Object=MibScalar
systemSave=_SystemSave_Object((1,3,6,1,4,1,7745,5,2,17),_SystemSave_Type())
systemSave.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSave.setStatus(_A)
_SystemRestart_ObjectIdentity=ObjectIdentity
systemRestart=_SystemRestart_ObjectIdentity((1,3,6,1,4,1,7745,5,2,18))
class _RestartOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('saveConf',0),('notSaveConf',1),('restoreDefaultConf',2),('restoreFactoryDefault',3)))
_RestartOption_Type.__name__=_D
_RestartOption_Object=MibScalar
restartOption=_RestartOption_Object((1,3,6,1,4,1,7745,5,2,18,1),_RestartOption_Type())
restartOption.setMaxAccess(_C)
if mibBuilder.loadTexts:restartOption.setStatus(_A)
class _RestartDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_RestartDelay_Type.__name__=_D
_RestartDelay_Object=MibScalar
restartDelay=_RestartDelay_Object((1,3,6,1,4,1,7745,5,2,18,2),_RestartDelay_Type())
restartDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:restartDelay.setStatus(_A)
class _RestartExec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),('restart',1)))
_RestartExec_Type.__name__=_D
_RestartExec_Object=MibScalar
restartExec=_RestartExec_Object((1,3,6,1,4,1,7745,5,2,18,3),_RestartExec_Type())
restartExec.setMaxAccess(_C)
if mibBuilder.loadTexts:restartExec.setStatus(_A)
_RestartStatus_Type=DisplayString
_RestartStatus_Object=MibScalar
restartStatus=_RestartStatus_Object((1,3,6,1,4,1,7745,5,2,18,4),_RestartStatus_Type())
restartStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:restartStatus.setStatus(_A)
_Performance_ObjectIdentity=ObjectIdentity
performance=_Performance_ObjectIdentity((1,3,6,1,4,1,7745,5,2,19))
_PerformanceCpuAvg1min_Type=Integer32
_PerformanceCpuAvg1min_Object=MibScalar
performanceCpuAvg1min=_PerformanceCpuAvg1min_Object((1,3,6,1,4,1,7745,5,2,19,1),_PerformanceCpuAvg1min_Type())
performanceCpuAvg1min.setMaxAccess(_B)
if mibBuilder.loadTexts:performanceCpuAvg1min.setStatus(_A)
_PerformanceCpuAvg5min_Type=Integer32
_PerformanceCpuAvg5min_Object=MibScalar
performanceCpuAvg5min=_PerformanceCpuAvg5min_Object((1,3,6,1,4,1,7745,5,2,19,2),_PerformanceCpuAvg5min_Type())
performanceCpuAvg5min.setMaxAccess(_B)
if mibBuilder.loadTexts:performanceCpuAvg5min.setStatus(_A)
_PerformanceCpuAvg15min_Type=Integer32
_PerformanceCpuAvg15min_Object=MibScalar
performanceCpuAvg15min=_PerformanceCpuAvg15min_Object((1,3,6,1,4,1,7745,5,2,19,3),_PerformanceCpuAvg15min_Type())
performanceCpuAvg15min.setMaxAccess(_B)
if mibBuilder.loadTexts:performanceCpuAvg15min.setStatus(_A)
_PerformanceDynMemLoad_Type=Integer32
_PerformanceDynMemLoad_Object=MibScalar
performanceDynMemLoad=_PerformanceDynMemLoad_Object((1,3,6,1,4,1,7745,5,2,19,4),_PerformanceDynMemLoad_Type())
performanceDynMemLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:performanceDynMemLoad.setStatus(_A)
_PerformanceDynMemTotal_Type=Integer32
_PerformanceDynMemTotal_Object=MibScalar
performanceDynMemTotal=_PerformanceDynMemTotal_Object((1,3,6,1,4,1,7745,5,2,19,5),_PerformanceDynMemTotal_Type())
performanceDynMemTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:performanceDynMemTotal.setStatus(_A)
_PerformanceDynMemFree_Type=Integer32
_PerformanceDynMemFree_Object=MibScalar
performanceDynMemFree=_PerformanceDynMemFree_Object((1,3,6,1,4,1,7745,5,2,19,6),_PerformanceDynMemFree_Type())
performanceDynMemFree.setMaxAccess(_B)
if mibBuilder.loadTexts:performanceDynMemFree.setStatus(_A)
_SystemDefaultScpServer_Type=DisplayString
_SystemDefaultScpServer_Object=MibScalar
systemDefaultScpServer=_SystemDefaultScpServer_Object((1,3,6,1,4,1,7745,5,2,20),_SystemDefaultScpServer_Type())
systemDefaultScpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:systemDefaultScpServer.setStatus(_A)
_SystemScpUsername_Type=DisplayString
_SystemScpUsername_Object=MibScalar
systemScpUsername=_SystemScpUsername_Object((1,3,6,1,4,1,7745,5,2,21),_SystemScpUsername_Type())
systemScpUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:systemScpUsername.setStatus(_A)
_SystemScpPassword_Type=DisplayString
_SystemScpPassword_Object=MibScalar
systemScpPassword=_SystemScpPassword_Object((1,3,6,1,4,1,7745,5,2,22),_SystemScpPassword_Type())
systemScpPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:systemScpPassword.setStatus(_A)
class _SystemConsoleEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_SystemConsoleEnable_Type.__name__=_D
_SystemConsoleEnable_Object=MibScalar
systemConsoleEnable=_SystemConsoleEnable_Object((1,3,6,1,4,1,7745,5,2,23),_SystemConsoleEnable_Type())
systemConsoleEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:systemConsoleEnable.setStatus(_A)
class _SystemLogMsgRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_SystemLogMsgRate_Type.__name__=_D
_SystemLogMsgRate_Object=MibScalar
systemLogMsgRate=_SystemLogMsgRate_Object((1,3,6,1,4,1,7745,5,2,24),_SystemLogMsgRate_Type())
systemLogMsgRate.setMaxAccess(_C)
if mibBuilder.loadTexts:systemLogMsgRate.setStatus(_A)
_Dsl_ObjectIdentity=ObjectIdentity
dsl=_Dsl_ObjectIdentity((1,3,6,1,4,1,7745,5,3))
_Xdsl_ObjectIdentity=ObjectIdentity
xdsl=_Xdsl_ObjectIdentity((1,3,6,1,4,1,7745,5,3,1))
_XdslTable_Object=MibTable
xdslTable=_XdslTable_Object((1,3,6,1,4,1,7745,5,3,1,1))
if mibBuilder.loadTexts:xdslTable.setStatus(_A)
_XdslEntry_Object=MibTableRow
xdslEntry=_XdslEntry_Object((1,3,6,1,4,1,7745,5,3,1,1,1))
xdslEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:xdslEntry.setStatus(_A)
class _XdslIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_XdslIndex_Type.__name__=_D
_XdslIndex_Object=MibTableColumn
xdslIndex=_XdslIndex_Object((1,3,6,1,4,1,7745,5,3,1,1,1,1),_XdslIndex_Type())
xdslIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslIndex.setStatus(_A)
_XdslLinkStatus_Type=DisplayString
_XdslLinkStatus_Object=MibTableColumn
xdslLinkStatus=_XdslLinkStatus_Object((1,3,6,1,4,1,7745,5,3,1,1,1,2),_XdslLinkStatus_Type())
xdslLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslLinkStatus.setStatus(_A)
_XdslTc_Type=DisplayString
_XdslTc_Object=MibTableColumn
xdslTc=_XdslTc_Object((1,3,6,1,4,1,7745,5,3,1,1,1,3),_XdslTc_Type())
xdslTc.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslTc.setStatus(_A)
_XdslUsAttenuation_Type=Integer32
_XdslUsAttenuation_Object=MibTableColumn
xdslUsAttenuation=_XdslUsAttenuation_Object((1,3,6,1,4,1,7745,5,3,1,1,1,4),_XdslUsAttenuation_Type())
xdslUsAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslUsAttenuation.setStatus(_A)
_XdslDsAttenuation_Type=Integer32
_XdslDsAttenuation_Object=MibTableColumn
xdslDsAttenuation=_XdslDsAttenuation_Object((1,3,6,1,4,1,7745,5,3,1,1,1,5),_XdslDsAttenuation_Type())
xdslDsAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslDsAttenuation.setStatus(_A)
_XdslUsNoiseMargin_Type=Integer32
_XdslUsNoiseMargin_Object=MibTableColumn
xdslUsNoiseMargin=_XdslUsNoiseMargin_Object((1,3,6,1,4,1,7745,5,3,1,1,1,6),_XdslUsNoiseMargin_Type())
xdslUsNoiseMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslUsNoiseMargin.setStatus(_A)
_XdslDsNoiseMargin_Type=Integer32
_XdslDsNoiseMargin_Object=MibTableColumn
xdslDsNoiseMargin=_XdslDsNoiseMargin_Object((1,3,6,1,4,1,7745,5,3,1,1,1,7),_XdslDsNoiseMargin_Type())
xdslDsNoiseMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslDsNoiseMargin.setStatus(_A)
_XdslUsCurrRate_Type=Integer32
_XdslUsCurrRate_Object=MibTableColumn
xdslUsCurrRate=_XdslUsCurrRate_Object((1,3,6,1,4,1,7745,5,3,1,1,1,8),_XdslUsCurrRate_Type())
xdslUsCurrRate.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslUsCurrRate.setStatus(_A)
_XdslDsCurrRate_Type=Integer32
_XdslDsCurrRate_Object=MibTableColumn
xdslDsCurrRate=_XdslDsCurrRate_Object((1,3,6,1,4,1,7745,5,3,1,1,1,9),_XdslDsCurrRate_Type())
xdslDsCurrRate.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslDsCurrRate.setStatus(_A)
_XdslModulationType_Type=DisplayString
_XdslModulationType_Object=MibTableColumn
xdslModulationType=_XdslModulationType_Object((1,3,6,1,4,1,7745,5,3,1,1,1,10),_XdslModulationType_Type())
xdslModulationType.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslModulationType.setStatus(_A)
_XdslUsMaxTheorRate_Type=Integer32
_XdslUsMaxTheorRate_Object=MibTableColumn
xdslUsMaxTheorRate=_XdslUsMaxTheorRate_Object((1,3,6,1,4,1,7745,5,3,1,1,1,11),_XdslUsMaxTheorRate_Type())
xdslUsMaxTheorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslUsMaxTheorRate.setStatus(_A)
_XdslDsMaxTheorRate_Type=Integer32
_XdslDsMaxTheorRate_Object=MibTableColumn
xdslDsMaxTheorRate=_XdslDsMaxTheorRate_Object((1,3,6,1,4,1,7745,5,3,1,1,1,12),_XdslDsMaxTheorRate_Type())
xdslDsMaxTheorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslDsMaxTheorRate.setStatus(_A)
_XdslUsTotBytes_Type=Integer32
_XdslUsTotBytes_Object=MibTableColumn
xdslUsTotBytes=_XdslUsTotBytes_Object((1,3,6,1,4,1,7745,5,3,1,1,1,13),_XdslUsTotBytes_Type())
xdslUsTotBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslUsTotBytes.setStatus(_A)
_XdslDsTotBytes_Type=Integer32
_XdslDsTotBytes_Object=MibTableColumn
xdslDsTotBytes=_XdslDsTotBytes_Object((1,3,6,1,4,1,7745,5,3,1,1,1,14),_XdslDsTotBytes_Type())
xdslDsTotBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslDsTotBytes.setStatus(_A)
_XdslNeTotCrcErr_Type=Integer32
_XdslNeTotCrcErr_Object=MibTableColumn
xdslNeTotCrcErr=_XdslNeTotCrcErr_Object((1,3,6,1,4,1,7745,5,3,1,1,1,15),_XdslNeTotCrcErr_Type())
xdslNeTotCrcErr.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslNeTotCrcErr.setStatus(_A)
_XdslNeShowtimeCrcErr_Type=Integer32
_XdslNeShowtimeCrcErr_Object=MibTableColumn
xdslNeShowtimeCrcErr=_XdslNeShowtimeCrcErr_Object((1,3,6,1,4,1,7745,5,3,1,1,1,16),_XdslNeShowtimeCrcErr_Type())
xdslNeShowtimeCrcErr.setMaxAccess(_B)
if mibBuilder.loadTexts:xdslNeShowtimeCrcErr.setStatus(_A)
_Shdsl_ObjectIdentity=ObjectIdentity
shdsl=_Shdsl_ObjectIdentity((1,3,6,1,4,1,7745,5,3,2))
_ShdslTable_Object=MibTable
shdslTable=_ShdslTable_Object((1,3,6,1,4,1,7745,5,3,2,1))
if mibBuilder.loadTexts:shdslTable.setStatus(_A)
_ShdslEntry_Object=MibTableRow
shdslEntry=_ShdslEntry_Object((1,3,6,1,4,1,7745,5,3,2,1,1))
shdslEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:shdslEntry.setStatus(_A)
class _ShdslIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ShdslIndex_Type.__name__=_D
_ShdslIndex_Object=MibTableColumn
shdslIndex=_ShdslIndex_Object((1,3,6,1,4,1,7745,5,3,2,1,1,1),_ShdslIndex_Type())
shdslIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslIndex.setStatus(_A)
_ShdslPhyStatus_Type=DisplayString
_ShdslPhyStatus_Object=MibTableColumn
shdslPhyStatus=_ShdslPhyStatus_Object((1,3,6,1,4,1,7745,5,3,2,1,1,2),_ShdslPhyStatus_Type())
shdslPhyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslPhyStatus.setStatus(_A)
_ShdslTc_Type=DisplayString
_ShdslTc_Object=MibTableColumn
shdslTc=_ShdslTc_Object((1,3,6,1,4,1,7745,5,3,2,1,1,3),_ShdslTc_Type())
shdslTc.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslTc.setStatus(_A)
_ShdslUsAttenuation_Type=Integer32
_ShdslUsAttenuation_Object=MibTableColumn
shdslUsAttenuation=_ShdslUsAttenuation_Object((1,3,6,1,4,1,7745,5,3,2,1,1,4),_ShdslUsAttenuation_Type())
shdslUsAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslUsAttenuation.setStatus(_A)
_ShdslDsAttenuation_Type=Integer32
_ShdslDsAttenuation_Object=MibTableColumn
shdslDsAttenuation=_ShdslDsAttenuation_Object((1,3,6,1,4,1,7745,5,3,2,1,1,5),_ShdslDsAttenuation_Type())
shdslDsAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslDsAttenuation.setStatus(_A)
_ShdslUsNoiseMargin_Type=Integer32
_ShdslUsNoiseMargin_Object=MibTableColumn
shdslUsNoiseMargin=_ShdslUsNoiseMargin_Object((1,3,6,1,4,1,7745,5,3,2,1,1,6),_ShdslUsNoiseMargin_Type())
shdslUsNoiseMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslUsNoiseMargin.setStatus(_A)
_ShdslDsNoiseMargin_Type=Integer32
_ShdslDsNoiseMargin_Object=MibTableColumn
shdslDsNoiseMargin=_ShdslDsNoiseMargin_Object((1,3,6,1,4,1,7745,5,3,2,1,1,7),_ShdslDsNoiseMargin_Type())
shdslDsNoiseMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslDsNoiseMargin.setStatus(_A)
_ShdslUsCurrRate_Type=Integer32
_ShdslUsCurrRate_Object=MibTableColumn
shdslUsCurrRate=_ShdslUsCurrRate_Object((1,3,6,1,4,1,7745,5,3,2,1,1,8),_ShdslUsCurrRate_Type())
shdslUsCurrRate.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslUsCurrRate.setStatus(_A)
_ShdslDsCurrRate_Type=Integer32
_ShdslDsCurrRate_Object=MibTableColumn
shdslDsCurrRate=_ShdslDsCurrRate_Object((1,3,6,1,4,1,7745,5,3,2,1,1,9),_ShdslDsCurrRate_Type())
shdslDsCurrRate.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslDsCurrRate.setStatus(_A)
_ShdslModulationType_Type=DisplayString
_ShdslModulationType_Object=MibTableColumn
shdslModulationType=_ShdslModulationType_Object((1,3,6,1,4,1,7745,5,3,2,1,1,10),_ShdslModulationType_Type())
shdslModulationType.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslModulationType.setStatus(_A)
_ShdslUsMaxTheorRate_Type=Integer32
_ShdslUsMaxTheorRate_Object=MibTableColumn
shdslUsMaxTheorRate=_ShdslUsMaxTheorRate_Object((1,3,6,1,4,1,7745,5,3,2,1,1,11),_ShdslUsMaxTheorRate_Type())
shdslUsMaxTheorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslUsMaxTheorRate.setStatus(_A)
_ShdslDsMaxTheorRate_Type=Integer32
_ShdslDsMaxTheorRate_Object=MibTableColumn
shdslDsMaxTheorRate=_ShdslDsMaxTheorRate_Object((1,3,6,1,4,1,7745,5,3,2,1,1,12),_ShdslDsMaxTheorRate_Type())
shdslDsMaxTheorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslDsMaxTheorRate.setStatus(_A)
_ShdslUsTotBytes_Type=Integer32
_ShdslUsTotBytes_Object=MibTableColumn
shdslUsTotBytes=_ShdslUsTotBytes_Object((1,3,6,1,4,1,7745,5,3,2,1,1,13),_ShdslUsTotBytes_Type())
shdslUsTotBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslUsTotBytes.setStatus(_A)
_ShdslDsTotBytes_Type=Integer32
_ShdslDsTotBytes_Object=MibTableColumn
shdslDsTotBytes=_ShdslDsTotBytes_Object((1,3,6,1,4,1,7745,5,3,2,1,1,14),_ShdslDsTotBytes_Type())
shdslDsTotBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslDsTotBytes.setStatus(_A)
_ShdslNeTotCrcErr_Type=Integer32
_ShdslNeTotCrcErr_Object=MibTableColumn
shdslNeTotCrcErr=_ShdslNeTotCrcErr_Object((1,3,6,1,4,1,7745,5,3,2,1,1,15),_ShdslNeTotCrcErr_Type())
shdslNeTotCrcErr.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslNeTotCrcErr.setStatus(_A)
_ShdslNeShowtimeCrcErr_Type=Integer32
_ShdslNeShowtimeCrcErr_Object=MibTableColumn
shdslNeShowtimeCrcErr=_ShdslNeShowtimeCrcErr_Object((1,3,6,1,4,1,7745,5,3,2,1,1,16),_ShdslNeShowtimeCrcErr_Type())
shdslNeShowtimeCrcErr.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslNeShowtimeCrcErr.setStatus(_A)
_ShdslUsPower_Type=Integer32
_ShdslUsPower_Object=MibTableColumn
shdslUsPower=_ShdslUsPower_Object((1,3,6,1,4,1,7745,5,3,2,1,1,17),_ShdslUsPower_Type())
shdslUsPower.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslUsPower.setStatus(_A)
_ShdslDsPower_Type=Integer32
_ShdslDsPower_Object=MibTableColumn
shdslDsPower=_ShdslDsPower_Object((1,3,6,1,4,1,7745,5,3,2,1,1,18),_ShdslDsPower_Type())
shdslDsPower.setMaxAccess(_B)
if mibBuilder.loadTexts:shdslDsPower.setStatus(_A)
_Voip_ObjectIdentity=ObjectIdentity
voip=_Voip_ObjectIdentity((1,3,6,1,4,1,7745,5,4))
_Trunk_ObjectIdentity=ObjectIdentity
trunk=_Trunk_ObjectIdentity((1,3,6,1,4,1,7745,5,4,1))
_TrunkTable_Object=MibTable
trunkTable=_TrunkTable_Object((1,3,6,1,4,1,7745,5,4,1,1))
if mibBuilder.loadTexts:trunkTable.setStatus(_A)
_TrunkEntry_Object=MibTableRow
trunkEntry=_TrunkEntry_Object((1,3,6,1,4,1,7745,5,4,1,1,1))
trunkEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:trunkEntry.setStatus(_A)
class _TrunkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TrunkIndex_Type.__name__=_D
_TrunkIndex_Object=MibTableColumn
trunkIndex=_TrunkIndex_Object((1,3,6,1,4,1,7745,5,4,1,1,1,1),_TrunkIndex_Type())
trunkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkIndex.setStatus(_A)
_TrunkName_Type=DisplayString
_TrunkName_Object=MibTableColumn
trunkName=_TrunkName_Object((1,3,6,1,4,1,7745,5,4,1,1,1,2),_TrunkName_Type())
trunkName.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkName.setStatus(_A)
_TrunkType_Type=DisplayString
_TrunkType_Object=MibTableColumn
trunkType=_TrunkType_Object((1,3,6,1,4,1,7745,5,4,1,1,1,3),_TrunkType_Type())
trunkType.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkType.setStatus(_A)
class _TrunkEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('registered',1),('unregistered',2)))
_TrunkEnable_Type.__name__=_D
_TrunkEnable_Object=MibTableColumn
trunkEnable=_TrunkEnable_Object((1,3,6,1,4,1,7745,5,4,1,1,1,4),_TrunkEnable_Type())
trunkEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:trunkEnable.setStatus(_A)
_TrunkDescription_Type=DisplayString
_TrunkDescription_Object=MibTableColumn
trunkDescription=_TrunkDescription_Object((1,3,6,1,4,1,7745,5,4,1,1,1,5),_TrunkDescription_Type())
trunkDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkDescription.setStatus(_A)
_TrunkUserName_Type=DisplayString
_TrunkUserName_Object=MibTableColumn
trunkUserName=_TrunkUserName_Object((1,3,6,1,4,1,7745,5,4,1,1,1,6),_TrunkUserName_Type())
trunkUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkUserName.setStatus(_A)
_TrunkRegHost_Type=DisplayString
_TrunkRegHost_Object=MibTableColumn
trunkRegHost=_TrunkRegHost_Object((1,3,6,1,4,1,7745,5,4,1,1,1,7),_TrunkRegHost_Type())
trunkRegHost.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkRegHost.setStatus(_A)
_TrunkProxyHost_Type=DisplayString
_TrunkProxyHost_Object=MibTableColumn
trunkProxyHost=_TrunkProxyHost_Object((1,3,6,1,4,1,7745,5,4,1,1,1,8),_TrunkProxyHost_Type())
trunkProxyHost.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkProxyHost.setStatus(_A)
_TrunkIfcStatus_Type=DisplayString
_TrunkIfcStatus_Object=MibTableColumn
trunkIfcStatus=_TrunkIfcStatus_Object((1,3,6,1,4,1,7745,5,4,1,1,1,9),_TrunkIfcStatus_Type())
trunkIfcStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkIfcStatus.setStatus(_A)
_TrunkRegStatus_Type=DisplayString
_TrunkRegStatus_Object=MibTableColumn
trunkRegStatus=_TrunkRegStatus_Object((1,3,6,1,4,1,7745,5,4,1,1,1,10),_TrunkRegStatus_Type())
trunkRegStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkRegStatus.setStatus(_A)
_TrunkMsgWait_Type=DisplayString
_TrunkMsgWait_Object=MibTableColumn
trunkMsgWait=_TrunkMsgWait_Object((1,3,6,1,4,1,7745,5,4,1,1,1,11),_TrunkMsgWait_Type())
trunkMsgWait.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkMsgWait.setStatus(_A)
_TrunkIsdnTable_Object=MibTable
trunkIsdnTable=_TrunkIsdnTable_Object((1,3,6,1,4,1,7745,5,4,1,2))
if mibBuilder.loadTexts:trunkIsdnTable.setStatus(_A)
_TrunkIsdnEntry_Object=MibTableRow
trunkIsdnEntry=_TrunkIsdnEntry_Object((1,3,6,1,4,1,7745,5,4,1,2,1))
trunkIsdnEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:trunkIsdnEntry.setStatus(_A)
class _TrunkIsdnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TrunkIsdnIndex_Type.__name__=_D
_TrunkIsdnIndex_Object=MibTableColumn
trunkIsdnIndex=_TrunkIsdnIndex_Object((1,3,6,1,4,1,7745,5,4,1,2,1,1),_TrunkIsdnIndex_Type())
trunkIsdnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkIsdnIndex.setStatus(_A)
_TrunkIsdnName_Type=DisplayString
_TrunkIsdnName_Object=MibTableColumn
trunkIsdnName=_TrunkIsdnName_Object((1,3,6,1,4,1,7745,5,4,1,2,1,2),_TrunkIsdnName_Type())
trunkIsdnName.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkIsdnName.setStatus(_A)
_TrunkIsdnType_Type=DisplayString
_TrunkIsdnType_Object=MibTableColumn
trunkIsdnType=_TrunkIsdnType_Object((1,3,6,1,4,1,7745,5,4,1,2,1,3),_TrunkIsdnType_Type())
trunkIsdnType.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkIsdnType.setStatus(_A)
class _TrunkIsdnEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_TrunkIsdnEnable_Type.__name__=_D
_TrunkIsdnEnable_Object=MibTableColumn
trunkIsdnEnable=_TrunkIsdnEnable_Object((1,3,6,1,4,1,7745,5,4,1,2,1,4),_TrunkIsdnEnable_Type())
trunkIsdnEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:trunkIsdnEnable.setStatus(_A)
_TrunkIsdnDescription_Type=DisplayString
_TrunkIsdnDescription_Object=MibTableColumn
trunkIsdnDescription=_TrunkIsdnDescription_Object((1,3,6,1,4,1,7745,5,4,1,2,1,5),_TrunkIsdnDescription_Type())
trunkIsdnDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkIsdnDescription.setStatus(_A)
_TrunkIsdnB1Status_Type=DisplayString
_TrunkIsdnB1Status_Object=MibTableColumn
trunkIsdnB1Status=_TrunkIsdnB1Status_Object((1,3,6,1,4,1,7745,5,4,1,2,1,6),_TrunkIsdnB1Status_Type())
trunkIsdnB1Status.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkIsdnB1Status.setStatus(_A)
_TrunkIsdnB2Status_Type=DisplayString
_TrunkIsdnB2Status_Object=MibTableColumn
trunkIsdnB2Status=_TrunkIsdnB2Status_Object((1,3,6,1,4,1,7745,5,4,1,2,1,7),_TrunkIsdnB2Status_Type())
trunkIsdnB2Status.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkIsdnB2Status.setStatus(_A)
_TrunkFxoTable_Object=MibTable
trunkFxoTable=_TrunkFxoTable_Object((1,3,6,1,4,1,7745,5,4,1,3))
if mibBuilder.loadTexts:trunkFxoTable.setStatus(_A)
_TrunkFxoEntry_Object=MibTableRow
trunkFxoEntry=_TrunkFxoEntry_Object((1,3,6,1,4,1,7745,5,4,1,3,1))
trunkFxoEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:trunkFxoEntry.setStatus(_A)
class _TrunkFxoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TrunkFxoIndex_Type.__name__=_D
_TrunkFxoIndex_Object=MibTableColumn
trunkFxoIndex=_TrunkFxoIndex_Object((1,3,6,1,4,1,7745,5,4,1,3,1,1),_TrunkFxoIndex_Type())
trunkFxoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkFxoIndex.setStatus(_A)
_TrunkFxoName_Type=DisplayString
_TrunkFxoName_Object=MibTableColumn
trunkFxoName=_TrunkFxoName_Object((1,3,6,1,4,1,7745,5,4,1,3,1,2),_TrunkFxoName_Type())
trunkFxoName.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkFxoName.setStatus(_A)
_TrunkFxoType_Type=DisplayString
_TrunkFxoType_Object=MibTableColumn
trunkFxoType=_TrunkFxoType_Object((1,3,6,1,4,1,7745,5,4,1,3,1,3),_TrunkFxoType_Type())
trunkFxoType.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkFxoType.setStatus(_A)
class _TrunkFxoEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_TrunkFxoEnable_Type.__name__=_D
_TrunkFxoEnable_Object=MibTableColumn
trunkFxoEnable=_TrunkFxoEnable_Object((1,3,6,1,4,1,7745,5,4,1,3,1,4),_TrunkFxoEnable_Type())
trunkFxoEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:trunkFxoEnable.setStatus(_A)
_TrunkFxoDescription_Type=DisplayString
_TrunkFxoDescription_Object=MibTableColumn
trunkFxoDescription=_TrunkFxoDescription_Object((1,3,6,1,4,1,7745,5,4,1,3,1,5),_TrunkFxoDescription_Type())
trunkFxoDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkFxoDescription.setStatus(_A)
_TrunkFxoStatus_Type=DisplayString
_TrunkFxoStatus_Object=MibTableColumn
trunkFxoStatus=_TrunkFxoStatus_Object((1,3,6,1,4,1,7745,5,4,1,3,1,6),_TrunkFxoStatus_Type())
trunkFxoStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkFxoStatus.setStatus(_A)
_UserTerminal_ObjectIdentity=ObjectIdentity
userTerminal=_UserTerminal_ObjectIdentity((1,3,6,1,4,1,7745,5,4,2))
_UsTermPotsTable_Object=MibTable
usTermPotsTable=_UsTermPotsTable_Object((1,3,6,1,4,1,7745,5,4,2,1))
if mibBuilder.loadTexts:usTermPotsTable.setStatus(_A)
_UsTermPotsEntry_Object=MibTableRow
usTermPotsEntry=_UsTermPotsEntry_Object((1,3,6,1,4,1,7745,5,4,2,1,1))
usTermPotsEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:usTermPotsEntry.setStatus(_A)
class _UsTermPotsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_UsTermPotsIndex_Type.__name__=_D
_UsTermPotsIndex_Object=MibTableColumn
usTermPotsIndex=_UsTermPotsIndex_Object((1,3,6,1,4,1,7745,5,4,2,1,1,1),_UsTermPotsIndex_Type())
usTermPotsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:usTermPotsIndex.setStatus(_A)
class _UsTermPotsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_UsTermPotsEnable_Type.__name__=_D
_UsTermPotsEnable_Object=MibTableColumn
usTermPotsEnable=_UsTermPotsEnable_Object((1,3,6,1,4,1,7745,5,4,2,1,1,2),_UsTermPotsEnable_Type())
usTermPotsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:usTermPotsEnable.setStatus(_A)
_UsTermPotsDescription_Type=DisplayString
_UsTermPotsDescription_Object=MibTableColumn
usTermPotsDescription=_UsTermPotsDescription_Object((1,3,6,1,4,1,7745,5,4,2,1,1,3),_UsTermPotsDescription_Type())
usTermPotsDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:usTermPotsDescription.setStatus(_A)
_UsTermPotsStatus_Type=DisplayString
_UsTermPotsStatus_Object=MibTableColumn
usTermPotsStatus=_UsTermPotsStatus_Object((1,3,6,1,4,1,7745,5,4,2,1,1,4),_UsTermPotsStatus_Type())
usTermPotsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:usTermPotsStatus.setStatus(_A)
_UsTermPotsDspSlic_Type=DisplayString
_UsTermPotsDspSlic_Object=MibTableColumn
usTermPotsDspSlic=_UsTermPotsDspSlic_Object((1,3,6,1,4,1,7745,5,4,2,1,1,5),_UsTermPotsDspSlic_Type())
usTermPotsDspSlic.setMaxAccess(_B)
if mibBuilder.loadTexts:usTermPotsDspSlic.setStatus(_A)
_UsTermISDNTable_Object=MibTable
usTermISDNTable=_UsTermISDNTable_Object((1,3,6,1,4,1,7745,5,4,2,2))
if mibBuilder.loadTexts:usTermISDNTable.setStatus(_A)
_UsTermISDNEntry_Object=MibTableRow
usTermISDNEntry=_UsTermISDNEntry_Object((1,3,6,1,4,1,7745,5,4,2,2,1))
usTermISDNEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:usTermISDNEntry.setStatus(_A)
class _UsTermISDNIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_UsTermISDNIndex_Type.__name__=_D
_UsTermISDNIndex_Object=MibTableColumn
usTermISDNIndex=_UsTermISDNIndex_Object((1,3,6,1,4,1,7745,5,4,2,2,1,1),_UsTermISDNIndex_Type())
usTermISDNIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:usTermISDNIndex.setStatus(_A)
class _UsTermISDNEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_UsTermISDNEnable_Type.__name__=_D
_UsTermISDNEnable_Object=MibTableColumn
usTermISDNEnable=_UsTermISDNEnable_Object((1,3,6,1,4,1,7745,5,4,2,2,1,2),_UsTermISDNEnable_Type())
usTermISDNEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:usTermISDNEnable.setStatus(_A)
_UsTermISDNDescription_Type=DisplayString
_UsTermISDNDescription_Object=MibTableColumn
usTermISDNDescription=_UsTermISDNDescription_Object((1,3,6,1,4,1,7745,5,4,2,2,1,3),_UsTermISDNDescription_Type())
usTermISDNDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:usTermISDNDescription.setStatus(_A)
_UsTermIsdnStatusB1_Type=DisplayString
_UsTermIsdnStatusB1_Object=MibTableColumn
usTermIsdnStatusB1=_UsTermIsdnStatusB1_Object((1,3,6,1,4,1,7745,5,4,2,2,1,4),_UsTermIsdnStatusB1_Type())
usTermIsdnStatusB1.setMaxAccess(_B)
if mibBuilder.loadTexts:usTermIsdnStatusB1.setStatus(_A)
_UsTermIsdnStatusB2_Type=DisplayString
_UsTermIsdnStatusB2_Object=MibTableColumn
usTermIsdnStatusB2=_UsTermIsdnStatusB2_Object((1,3,6,1,4,1,7745,5,4,2,2,1,5),_UsTermIsdnStatusB2_Type())
usTermIsdnStatusB2.setMaxAccess(_B)
if mibBuilder.loadTexts:usTermIsdnStatusB2.setStatus(_A)
_UsTermDectTable_Object=MibTable
usTermDectTable=_UsTermDectTable_Object((1,3,6,1,4,1,7745,5,4,2,3))
if mibBuilder.loadTexts:usTermDectTable.setStatus(_A)
_UsTermDectEntry_Object=MibTableRow
usTermDectEntry=_UsTermDectEntry_Object((1,3,6,1,4,1,7745,5,4,2,3,1))
usTermDectEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:usTermDectEntry.setStatus(_A)
class _UsTermDectIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_UsTermDectIndex_Type.__name__=_D
_UsTermDectIndex_Object=MibTableColumn
usTermDectIndex=_UsTermDectIndex_Object((1,3,6,1,4,1,7745,5,4,2,3,1,1),_UsTermDectIndex_Type())
usTermDectIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:usTermDectIndex.setStatus(_A)
class _UsTermDectEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_UsTermDectEnable_Type.__name__=_D
_UsTermDectEnable_Object=MibTableColumn
usTermDectEnable=_UsTermDectEnable_Object((1,3,6,1,4,1,7745,5,4,2,3,1,2),_UsTermDectEnable_Type())
usTermDectEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:usTermDectEnable.setStatus(_A)
_UsTermDectDescription_Type=DisplayString
_UsTermDectDescription_Object=MibTableColumn
usTermDectDescription=_UsTermDectDescription_Object((1,3,6,1,4,1,7745,5,4,2,3,1,3),_UsTermDectDescription_Type())
usTermDectDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:usTermDectDescription.setStatus(_A)
_UsTermDectStatus_Type=DisplayString
_UsTermDectStatus_Object=MibTableColumn
usTermDectStatus=_UsTermDectStatus_Object((1,3,6,1,4,1,7745,5,4,2,3,1,4),_UsTermDectStatus_Type())
usTermDectStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:usTermDectStatus.setStatus(_A)
_UsTermDectDspSlic_Type=DisplayString
_UsTermDectDspSlic_Object=MibTableColumn
usTermDectDspSlic=_UsTermDectDspSlic_Object((1,3,6,1,4,1,7745,5,4,2,3,1,5),_UsTermDectDspSlic_Type())
usTermDectDspSlic.setMaxAccess(_B)
if mibBuilder.loadTexts:usTermDectDspSlic.setStatus(_A)
class _VoipMaxConnection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_VoipMaxConnection_Type.__name__=_D
_VoipMaxConnection_Object=MibScalar
voipMaxConnection=_VoipMaxConnection_Object((1,3,6,1,4,1,7745,5,4,3),_VoipMaxConnection_Type())
voipMaxConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:voipMaxConnection.setStatus(_A)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,7745,5,5))
_GenericError_Type=DisplayString
_GenericError_Object=MibScalar
genericError=_GenericError_Object((1,3,6,1,4,1,7745,5,5,2),_GenericError_Type())
genericError.setMaxAccess(_B)
if mibBuilder.loadTexts:genericError.setStatus(_A)
_MgmtAccesses_ObjectIdentity=ObjectIdentity
mgmtAccesses=_MgmtAccesses_ObjectIdentity((1,3,6,1,4,1,7745,5,5,7))
class _MgmtUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MgmtUser_Type.__name__=_G
_MgmtUser_Object=MibScalar
mgmtUser=_MgmtUser_Object((1,3,6,1,4,1,7745,5,5,7,1),_MgmtUser_Type())
mgmtUser.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmtUser.setStatus(_A)
class _MgmtPrivilege_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MgmtPrivilege_Type.__name__=_G
_MgmtPrivilege_Object=MibScalar
mgmtPrivilege=_MgmtPrivilege_Object((1,3,6,1,4,1,7745,5,5,7,2),_MgmtPrivilege_Type())
mgmtPrivilege.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmtPrivilege.setStatus(_A)
class _MgmtTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MgmtTime_Type.__name__=_G
_MgmtTime_Object=MibScalar
mgmtTime=_MgmtTime_Object((1,3,6,1,4,1,7745,5,5,7,3),_MgmtTime_Type())
mgmtTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmtTime.setStatus(_A)
class _MgmtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('console',1),('telnet',2),('web',3),('snmp',4),('ssh',5),('tr069',6),('unknown',7)))
_MgmtType_Type.__name__=_D
_MgmtType_Object=MibScalar
mgmtType=_MgmtType_Object((1,3,6,1,4,1,7745,5,5,7,4),_MgmtType_Type())
mgmtType.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmtType.setStatus(_A)
class _MgmtAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MgmtAddress_Type.__name__=_G
_MgmtAddress_Object=MibScalar
mgmtAddress=_MgmtAddress_Object((1,3,6,1,4,1,7745,5,5,7,5),_MgmtAddress_Type())
mgmtAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmtAddress.setStatus(_A)
_Ifc_ObjectIdentity=ObjectIdentity
ifc=_Ifc_ObjectIdentity((1,3,6,1,4,1,7745,5,6))
_IfcTable_Object=MibTable
ifcTable=_IfcTable_Object((1,3,6,1,4,1,7745,5,6,1))
if mibBuilder.loadTexts:ifcTable.setStatus(_A)
_IfcEntry_Object=MibTableRow
ifcEntry=_IfcEntry_Object((1,3,6,1,4,1,7745,5,6,1,1))
ifcEntry.setIndexNames((0,_J,_U))
if mibBuilder.loadTexts:ifcEntry.setStatus(_A)
class _IfcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IfcName_Type.__name__=_G
_IfcName_Object=MibTableColumn
ifcName=_IfcName_Object((1,3,6,1,4,1,7745,5,6,1,1,1),_IfcName_Type())
ifcName.setMaxAccess(_B)
if mibBuilder.loadTexts:ifcName.setStatus(_A)
class _IfcDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IfcDescr_Type.__name__=_G
_IfcDescr_Object=MibTableColumn
ifcDescr=_IfcDescr_Object((1,3,6,1,4,1,7745,5,6,1,1,2),_IfcDescr_Type())
ifcDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:ifcDescr.setStatus(_A)
_IfcType_Type=IANAifType
_IfcType_Object=MibTableColumn
ifcType=_IfcType_Object((1,3,6,1,4,1,7745,5,6,1,1,3),_IfcType_Type())
ifcType.setMaxAccess(_B)
if mibBuilder.loadTexts:ifcType.setStatus(_A)
_IfcPhysAddress_Type=PhysAddress
_IfcPhysAddress_Object=MibTableColumn
ifcPhysAddress=_IfcPhysAddress_Object((1,3,6,1,4,1,7745,5,6,1,1,4),_IfcPhysAddress_Type())
ifcPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ifcPhysAddress.setStatus(_A)
_IfcMtu_Type=Integer32
_IfcMtu_Object=MibTableColumn
ifcMtu=_IfcMtu_Object((1,3,6,1,4,1,7745,5,6,1,1,5),_IfcMtu_Type())
ifcMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:ifcMtu.setStatus(_A)
_IfcSpeed_Type=Gauge32
_IfcSpeed_Object=MibTableColumn
ifcSpeed=_IfcSpeed_Object((1,3,6,1,4,1,7745,5,6,1,1,6),_IfcSpeed_Type())
ifcSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ifcSpeed.setStatus(_A)
_IfcRxRate_Type=Counter32
_IfcRxRate_Object=MibTableColumn
ifcRxRate=_IfcRxRate_Object((1,3,6,1,4,1,7745,5,6,1,1,7),_IfcRxRate_Type())
ifcRxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifcRxRate.setStatus(_A)
_IfcTxRate_Type=Counter32
_IfcTxRate_Object=MibTableColumn
ifcTxRate=_IfcTxRate_Object((1,3,6,1,4,1,7745,5,6,1,1,8),_IfcTxRate_Type())
ifcTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifcTxRate.setStatus(_A)
genericTrap=NotificationType((1,3,6,1,4,1,7745,5,5,1))
genericTrap.setObjects((_E,_e))
if mibBuilder.loadTexts:genericTrap.setStatus(_F)
interfaceUp=NotificationType((1,3,6,1,4,1,7745,5,5,3))
interfaceUp.setObjects((_J,_R))
if mibBuilder.loadTexts:interfaceUp.setStatus(_F)
interfaceDown=NotificationType((1,3,6,1,4,1,7745,5,5,4))
interfaceDown.setObjects((_J,_R))
if mibBuilder.loadTexts:interfaceDown.setStatus(_F)
trunkRegistered=NotificationType((1,3,6,1,4,1,7745,5,5,5))
trunkRegistered.setObjects((_E,_S))
if mibBuilder.loadTexts:trunkRegistered.setStatus(_F)
trunkUnregistered=NotificationType((1,3,6,1,4,1,7745,5,5,6))
trunkUnregistered.setObjects((_E,_S))
if mibBuilder.loadTexts:trunkUnregistered.setStatus(_F)
mgmtLogin=NotificationType((1,3,6,1,4,1,7745,5,5,7,6))
mgmtLogin.setObjects(*((_E,_N),(_E,_T),(_E,_O),(_E,_P),(_E,_Q)))
if mibBuilder.loadTexts:mgmtLogin.setStatus(_F)
mgmtLogout=NotificationType((1,3,6,1,4,1,7745,5,5,7,7))
mgmtLogout.setObjects(*((_E,_N),(_E,_T),(_E,_O),(_E,_P),(_E,_Q)))
if mibBuilder.loadTexts:mgmtLogout.setStatus(_F)
mgmtChange=NotificationType((1,3,6,1,4,1,7745,5,5,7,8))
mgmtChange.setObjects(*((_E,_N),(_E,_O),(_E,_P),(_E,_Q)))
if mibBuilder.loadTexts:mgmtChange.setStatus(_F)
mibBuilder.exportSymbols(_E,**{'aethra':aethra,'atosnt':atosnt,'tools':tools,'fileTransfer':fileTransfer,'fileTransferProtocol':fileTransferProtocol,'fileTransferFileName':fileTransferFileName,'fileTransferServerName':fileTransferServerName,'fileTransferOption':fileTransferOption,'fileTransferStorageFileName':fileTransferStorageFileName,'fileTransferExec':fileTransferExec,'fileTransferStatus':fileTransferStatus,'ping':ping,'pingParameters':pingParameters,'pingHost':pingHost,'pingSize':pingSize,'pingTries':pingTries,'pingTTL':pingTTL,'pingTimeOut':pingTimeOut,'pingSource':pingSource,'pingStart':pingStart,'pingStatus':pingStatus,'pingStatistics':pingStatistics,'pingTXpacket':pingTXpacket,'pingRXpacket':pingRXpacket,'pingLOSTpacket':pingLOSTpacket,'pingMinRTT':pingMinRTT,'pingMaxRTT':pingMaxRTT,'pingAvgRTT':pingAvgRTT,'system':system,'systemLoglevel':systemLoglevel,'systemDescription':systemDescription,'systemName':systemName,'systemLocalDomain':systemLocalDomain,'systemDefaultTftpServer':systemDefaultTftpServer,'systemTftpLocalAdd':systemTftpLocalAdd,'systemDefaultFtpServer':systemDefaultFtpServer,'systemFtpLocalAdd':systemFtpLocalAdd,'systemFtpUsername':systemFtpUsername,'systemFtpPassword':systemFtpPassword,'systemAAAProfile':systemAAAProfile,'systemAAALogTimeout':systemAAALogTimeout,'systemBackupAuth':systemBackupAuth,'systemScrollLine':systemScrollLine,'systemKernelLogs':systemKernelLogs,'systemCryptedPassword':systemCryptedPassword,'systemSave':systemSave,'systemRestart':systemRestart,'restartOption':restartOption,'restartDelay':restartDelay,'restartExec':restartExec,'restartStatus':restartStatus,'performance':performance,'performanceCpuAvg1min':performanceCpuAvg1min,'performanceCpuAvg5min':performanceCpuAvg5min,'performanceCpuAvg15min':performanceCpuAvg15min,'performanceDynMemLoad':performanceDynMemLoad,'performanceDynMemTotal':performanceDynMemTotal,'performanceDynMemFree':performanceDynMemFree,'systemDefaultScpServer':systemDefaultScpServer,'systemScpUsername':systemScpUsername,'systemScpPassword':systemScpPassword,'systemConsoleEnable':systemConsoleEnable,'systemLogMsgRate':systemLogMsgRate,'dsl':dsl,'xdsl':xdsl,'xdslTable':xdslTable,'xdslEntry':xdslEntry,_W:xdslIndex,'xdslLinkStatus':xdslLinkStatus,'xdslTc':xdslTc,'xdslUsAttenuation':xdslUsAttenuation,'xdslDsAttenuation':xdslDsAttenuation,'xdslUsNoiseMargin':xdslUsNoiseMargin,'xdslDsNoiseMargin':xdslDsNoiseMargin,'xdslUsCurrRate':xdslUsCurrRate,'xdslDsCurrRate':xdslDsCurrRate,'xdslModulationType':xdslModulationType,'xdslUsMaxTheorRate':xdslUsMaxTheorRate,'xdslDsMaxTheorRate':xdslDsMaxTheorRate,'xdslUsTotBytes':xdslUsTotBytes,'xdslDsTotBytes':xdslDsTotBytes,'xdslNeTotCrcErr':xdslNeTotCrcErr,'xdslNeShowtimeCrcErr':xdslNeShowtimeCrcErr,'shdsl':shdsl,'shdslTable':shdslTable,'shdslEntry':shdslEntry,_X:shdslIndex,'shdslPhyStatus':shdslPhyStatus,'shdslTc':shdslTc,'shdslUsAttenuation':shdslUsAttenuation,'shdslDsAttenuation':shdslDsAttenuation,'shdslUsNoiseMargin':shdslUsNoiseMargin,'shdslDsNoiseMargin':shdslDsNoiseMargin,'shdslUsCurrRate':shdslUsCurrRate,'shdslDsCurrRate':shdslDsCurrRate,'shdslModulationType':shdslModulationType,'shdslUsMaxTheorRate':shdslUsMaxTheorRate,'shdslDsMaxTheorRate':shdslDsMaxTheorRate,'shdslUsTotBytes':shdslUsTotBytes,'shdslDsTotBytes':shdslDsTotBytes,'shdslNeTotCrcErr':shdslNeTotCrcErr,'shdslNeShowtimeCrcErr':shdslNeShowtimeCrcErr,'shdslUsPower':shdslUsPower,'shdslDsPower':shdslDsPower,'voip':voip,'trunk':trunk,'trunkTable':trunkTable,'trunkEntry':trunkEntry,_Y:trunkIndex,_S:trunkName,'trunkType':trunkType,'trunkEnable':trunkEnable,'trunkDescription':trunkDescription,'trunkUserName':trunkUserName,'trunkRegHost':trunkRegHost,'trunkProxyHost':trunkProxyHost,'trunkIfcStatus':trunkIfcStatus,'trunkRegStatus':trunkRegStatus,'trunkMsgWait':trunkMsgWait,'trunkIsdnTable':trunkIsdnTable,'trunkIsdnEntry':trunkIsdnEntry,_Z:trunkIsdnIndex,'trunkIsdnName':trunkIsdnName,'trunkIsdnType':trunkIsdnType,'trunkIsdnEnable':trunkIsdnEnable,'trunkIsdnDescription':trunkIsdnDescription,'trunkIsdnB1Status':trunkIsdnB1Status,'trunkIsdnB2Status':trunkIsdnB2Status,'trunkFxoTable':trunkFxoTable,'trunkFxoEntry':trunkFxoEntry,_a:trunkFxoIndex,'trunkFxoName':trunkFxoName,'trunkFxoType':trunkFxoType,'trunkFxoEnable':trunkFxoEnable,'trunkFxoDescription':trunkFxoDescription,'trunkFxoStatus':trunkFxoStatus,'userTerminal':userTerminal,'usTermPotsTable':usTermPotsTable,'usTermPotsEntry':usTermPotsEntry,_b:usTermPotsIndex,'usTermPotsEnable':usTermPotsEnable,'usTermPotsDescription':usTermPotsDescription,'usTermPotsStatus':usTermPotsStatus,'usTermPotsDspSlic':usTermPotsDspSlic,'usTermISDNTable':usTermISDNTable,'usTermISDNEntry':usTermISDNEntry,_c:usTermISDNIndex,'usTermISDNEnable':usTermISDNEnable,'usTermISDNDescription':usTermISDNDescription,'usTermIsdnStatusB1':usTermIsdnStatusB1,'usTermIsdnStatusB2':usTermIsdnStatusB2,'usTermDectTable':usTermDectTable,'usTermDectEntry':usTermDectEntry,_d:usTermDectIndex,'usTermDectEnable':usTermDectEnable,'usTermDectDescription':usTermDectDescription,'usTermDectStatus':usTermDectStatus,'usTermDectDspSlic':usTermDectDspSlic,'voipMaxConnection':voipMaxConnection,'traps':traps,'genericTrap':genericTrap,_e:genericError,'interfaceUp':interfaceUp,'interfaceDown':interfaceDown,'trunkRegistered':trunkRegistered,'trunkUnregistered':trunkUnregistered,'mgmtAccesses':mgmtAccesses,_N:mgmtUser,_T:mgmtPrivilege,_O:mgmtTime,_P:mgmtType,_Q:mgmtAddress,'mgmtLogin':mgmtLogin,'mgmtLogout':mgmtLogout,'mgmtChange':mgmtChange,'ifc':ifc,'ifcTable':ifcTable,'ifcEntry':ifcEntry,'ifcName':ifcName,'ifcDescr':ifcDescr,'ifcType':ifcType,'ifcPhysAddress':ifcPhysAddress,'ifcMtu':ifcMtu,'ifcSpeed':ifcSpeed,'ifcRxRate':ifcRxRate,'ifcTxRate':ifcTxRate})