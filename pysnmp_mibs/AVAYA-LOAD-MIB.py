_e='avLoadAppDynamicFileName'
_d='avLoadApplMemType'
_c='avLoadApplMemLocation'
_b='avLoadApplMemModuleId'
_a='accessible-for-notify'
_Z='bootProm'
_Y='flashBankB'
_X='flashBankA'
_W='announcementFile'
_V='notSupported'
_U='executing'
_T='report'
_S='avGenOpIndex'
_R='OctetString'
_Q='avGenOpLastFailureDisplay'
_P='avGenOpLastFailureIndex'
_O='idle'
_N='read-create'
_M='avLoadSeverity'
_L='avGenAppFileVersionNumber'
_K='avGenAppFileDescription'
_J='avGenAppFileName'
_I='avLoadSysDescription'
_H='avGenAppFileId'
_G='avGenOpModuleId'
_F='DisplayString'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='AVAYA-LOAD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
avGatewayMibs,=mibBuilder.importSymbols('AVAYAGEN-MIB','avGatewayMibs')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
avLoad=ModuleIdentity((1,3,6,1,4,1,6889,2,6,5))
class AvLoadItuPerceivedSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cleared',1),('indeterminate',2),('critical',3),('major',4),('minor',5),('warning',6)))
_AvLoadNotification_ObjectIdentity=ObjectIdentity
avLoadNotification=_AvLoadNotification_ObjectIdentity((1,3,6,1,4,1,6889,2,6,5,0))
_AvGenOperations_ObjectIdentity=ObjectIdentity
avGenOperations=_AvGenOperations_ObjectIdentity((1,3,6,1,4,1,6889,2,6,5,1))
_AvGenLoadNumberOfSession_Type=Integer32
_AvGenLoadNumberOfSession_Object=MibScalar
avGenLoadNumberOfSession=_AvGenLoadNumberOfSession_Object((1,3,6,1,4,1,6889,2,6,5,1,1),_AvGenLoadNumberOfSession_Type())
avGenLoadNumberOfSession.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenLoadNumberOfSession.setStatus(_A)
_AvGenOpTable_Object=MibTable
avGenOpTable=_AvGenOpTable_Object((1,3,6,1,4,1,6889,2,6,5,1,2))
if mibBuilder.loadTexts:avGenOpTable.setStatus(_A)
_AvGenOpEntry_Object=MibTableRow
avGenOpEntry=_AvGenOpEntry_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1))
avGenOpEntry.setIndexNames((0,_B,_G),(0,_B,_S))
if mibBuilder.loadTexts:avGenOpEntry.setStatus(_A)
class _AvGenOpModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AvGenOpModuleId_Type.__name__=_D
_AvGenOpModuleId_Object=MibTableColumn
avGenOpModuleId=_AvGenOpModuleId_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,1),_AvGenOpModuleId_Type())
avGenOpModuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenOpModuleId.setStatus(_A)
class _AvGenOpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48)));namedValues=NamedValues(*(('uploadConfig',1),('downloadConfig',2),(_T,3),('uploadSoftware',4),('downloadSoftware',5),('localConfigFileCopy',6),('localSWFileCopy',7),('uploadLogfile',8),('eraseFile',9),('show',10),('syncStandbyAgent',11),('downloadAuthFile',12),('downloadLicFile',13),('downloadPhoneScriptFile',14),('uploadPhoneScriptFile',15),('downloadPhoneImageFile',16),('uploadDhcpBindingFile',17),('uploadAnnouncements',18),('downloadAnnouncements',19),('renameAnnouncement',20),('eraseAnnouncement',21),('uploadAuthFile',22),('uploadLicFile',23),('uploadSyslogFile',24),('uploadCDRFile',25),('backupConfig',28),('restore',29),('commit',30),('uploadServicePack',31),('downloadServicePack',32),('localServicePackFileCopy',33),('backup',34),('generateFile',35),('downloadCertificate',36),('uploadCertificate',37),('switchPartitions',38),('uploadPhoneImageFile',39),('downloadVoiceMailFile',40),('uploadVoiceMailFile',41),('downloadPhoneMessageFile',42),('uploadPhoneMessageFile',43),('downloadConfigurationWizardTaskFile',44),('uploadConfigurationWizardTaskFile',45),('localSWFileMove',46),('localVoiceMailFileMove',47),('reset',48)))
_AvGenOpIndex_Type.__name__=_D
_AvGenOpIndex_Object=MibTableColumn
avGenOpIndex=_AvGenOpIndex_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,2),_AvGenOpIndex_Type())
avGenOpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenOpIndex.setStatus(_A)
class _AvGenOpRunningState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_O,1),('beginOperation',2),('waitingIp',3),('runningIp',4),('copyingLocal',5),('readingConfiguration',6),(_U,7),('blocked',8),('reset',9)))
_AvGenOpRunningState_Type.__name__=_D
_AvGenOpRunningState_Object=MibTableColumn
avGenOpRunningState=_AvGenOpRunningState_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,3),_AvGenOpRunningState_Type())
avGenOpRunningState.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenOpRunningState.setStatus(_A)
_AvGenOpSourceIndex_Type=Integer32
_AvGenOpSourceIndex_Object=MibTableColumn
avGenOpSourceIndex=_AvGenOpSourceIndex_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,4),_AvGenOpSourceIndex_Type())
avGenOpSourceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenOpSourceIndex.setStatus(_A)
_AvGenOpDestIndex_Type=Integer32
_AvGenOpDestIndex_Object=MibTableColumn
avGenOpDestIndex=_AvGenOpDestIndex_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,5),_AvGenOpDestIndex_Type())
avGenOpDestIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenOpDestIndex.setStatus(_A)
_AvGenOpServerIP_Type=IpAddress
_AvGenOpServerIP_Object=MibTableColumn
avGenOpServerIP=_AvGenOpServerIP_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,6),_AvGenOpServerIP_Type())
avGenOpServerIP.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenOpServerIP.setStatus(_A)
class _AvGenOpUserName_Type(DisplayString):defaultHexValue='00';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AvGenOpUserName_Type.__name__=_F
_AvGenOpUserName_Object=MibTableColumn
avGenOpUserName=_AvGenOpUserName_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,7),_AvGenOpUserName_Type())
avGenOpUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenOpUserName.setStatus(_A)
class _AvGenOpPassword_Type(OctetString):defaultHexValue='00';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AvGenOpPassword_Type.__name__=_R
_AvGenOpPassword_Object=MibTableColumn
avGenOpPassword=_AvGenOpPassword_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,8),_AvGenOpPassword_Type())
avGenOpPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenOpPassword.setStatus(_A)
class _AvGenOpProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('tftp',1),('ftp',2),('localPeerTransport',3),('localServerTransport',4),('scp',5),('sftp',6),('usb',7),('http',8),('https',9),('ftpResume',10)))
_AvGenOpProtocolType_Type.__name__=_D
_AvGenOpProtocolType_Object=MibTableColumn
avGenOpProtocolType=_AvGenOpProtocolType_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,9),_AvGenOpProtocolType_Type())
avGenOpProtocolType.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenOpProtocolType.setStatus(_A)
_AvGenOpFileName_Type=DisplayString
_AvGenOpFileName_Object=MibTableColumn
avGenOpFileName=_AvGenOpFileName_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,10),_AvGenOpFileName_Type())
avGenOpFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenOpFileName.setStatus(_A)
class _AvGenOpRunningStateDisplay_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvGenOpRunningStateDisplay_Type.__name__=_F
_AvGenOpRunningStateDisplay_Object=MibTableColumn
avGenOpRunningStateDisplay=_AvGenOpRunningStateDisplay_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,11),_AvGenOpRunningStateDisplay_Type())
avGenOpRunningStateDisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenOpRunningStateDisplay.setStatus(_A)
class _AvGenOpLastFailureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,100,101,102,103,104,105,106,107,108,109,201,202,203,204,205,206,207,208,210,220,221,222)));namedValues=NamedValues(*(('noError',1),('genError',2),('configError',3),('busy',4),('timeout',5),('cancelled',6),('incompatibleFile',7),('fileTooBig',8),('protocolError',9),('flashWriteError',10),('nvramWriteError',11),('confFileGenErr',12),('confFileParseError',13),('confFileExecError',14),('readOnlyFile',15),('emptyFile',16),('noEnoughFreeMemoryLeft',17),('undefinedError',100),('fileNotFound',101),('accessViolation',102),('outOfMemory',103),('illegalOperation',104),('unknownTransferId',105),('fileAlreadyExists',106),('noSuchUser',107),('sshServerAuth',108),('sshDeviceAuth',109),('badChainOfTrust',201),('badChainOfTrustFormat',202),('notCodeSigningAuthority',203),('illegalDSA',204),('badPublicKeyFormat',205),('illegalDSKeySize',206),('badDSFormat',207),('authDSFailure',208),('configFileSecretIntegrityFault',210),('ftpResumeBadFilename',220),('ftpResumeEmptyFile',221),('ftpResumeNotSupported',222)))
_AvGenOpLastFailureIndex_Type.__name__=_D
_AvGenOpLastFailureIndex_Object=MibTableColumn
avGenOpLastFailureIndex=_AvGenOpLastFailureIndex_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,12),_AvGenOpLastFailureIndex_Type())
avGenOpLastFailureIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenOpLastFailureIndex.setStatus(_A)
class _AvGenOpLastFailureDisplay_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AvGenOpLastFailureDisplay_Type.__name__=_F
_AvGenOpLastFailureDisplay_Object=MibTableColumn
avGenOpLastFailureDisplay=_AvGenOpLastFailureDisplay_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,13),_AvGenOpLastFailureDisplay_Type())
avGenOpLastFailureDisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenOpLastFailureDisplay.setStatus(_A)
class _AvGenOpLastWarningDisplay_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AvGenOpLastWarningDisplay_Type.__name__=_F
_AvGenOpLastWarningDisplay_Object=MibTableColumn
avGenOpLastWarningDisplay=_AvGenOpLastWarningDisplay_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,14),_AvGenOpLastWarningDisplay_Type())
avGenOpLastWarningDisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenOpLastWarningDisplay.setStatus(_A)
_AvGenOpErrorLogIndex_Type=Integer32
_AvGenOpErrorLogIndex_Object=MibTableColumn
avGenOpErrorLogIndex=_AvGenOpErrorLogIndex_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,15),_AvGenOpErrorLogIndex_Type())
avGenOpErrorLogIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenOpErrorLogIndex.setStatus(_A)
class _AvGenOpResetSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('supported',1),(_V,2)))
_AvGenOpResetSupported_Type.__name__=_D
_AvGenOpResetSupported_Object=MibTableColumn
avGenOpResetSupported=_AvGenOpResetSupported_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,16),_AvGenOpResetSupported_Type())
avGenOpResetSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenOpResetSupported.setStatus(_A)
class _AvGenOpEnableReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AvGenOpEnableReset_Type.__name__=_D
_AvGenOpEnableReset_Object=MibTableColumn
avGenOpEnableReset=_AvGenOpEnableReset_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,17),_AvGenOpEnableReset_Type())
avGenOpEnableReset.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenOpEnableReset.setStatus(_A)
_AvGenOpNextBootImageIndex_Type=Integer32
_AvGenOpNextBootImageIndex_Object=MibTableColumn
avGenOpNextBootImageIndex=_AvGenOpNextBootImageIndex_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,18),_AvGenOpNextBootImageIndex_Type())
avGenOpNextBootImageIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenOpNextBootImageIndex.setStatus(_A)
_AvGenOpLastBootImageIndex_Type=Integer32
_AvGenOpLastBootImageIndex_Object=MibTableColumn
avGenOpLastBootImageIndex=_AvGenOpLastBootImageIndex_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,19),_AvGenOpLastBootImageIndex_Type())
avGenOpLastBootImageIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenOpLastBootImageIndex.setStatus(_A)
class _AvGenOpFileSystemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_AvGenOpFileSystemType_Type.__name__=_D
_AvGenOpFileSystemType_Object=MibTableColumn
avGenOpFileSystemType=_AvGenOpFileSystemType_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,20),_AvGenOpFileSystemType_Type())
avGenOpFileSystemType.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenOpFileSystemType.setStatus(_A)
class _AvGenOpReportSpecificFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('fullReport',1),('partialReport',2),(_V,255)))
_AvGenOpReportSpecificFlags_Type.__name__=_D
_AvGenOpReportSpecificFlags_Object=MibTableColumn
avGenOpReportSpecificFlags=_AvGenOpReportSpecificFlags_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,21),_AvGenOpReportSpecificFlags_Type())
avGenOpReportSpecificFlags.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenOpReportSpecificFlags.setStatus(_A)
_AvGenOpOctetsReceived_Type=Integer32
_AvGenOpOctetsReceived_Object=MibTableColumn
avGenOpOctetsReceived=_AvGenOpOctetsReceived_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,22),_AvGenOpOctetsReceived_Type())
avGenOpOctetsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenOpOctetsReceived.setStatus(_A)
_AvGenOpDownloadProxy_Type=Integer32
_AvGenOpDownloadProxy_Object=MibTableColumn
avGenOpDownloadProxy=_AvGenOpDownloadProxy_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,23),_AvGenOpDownloadProxy_Type())
avGenOpDownloadProxy.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenOpDownloadProxy.setStatus(_A)
_AvGenOpServerInetAddressType_Type=InetAddressType
_AvGenOpServerInetAddressType_Object=MibTableColumn
avGenOpServerInetAddressType=_AvGenOpServerInetAddressType_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,24),_AvGenOpServerInetAddressType_Type())
avGenOpServerInetAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenOpServerInetAddressType.setStatus(_A)
_AvGenOpServerInetAddress_Type=InetAddress
_AvGenOpServerInetAddress_Object=MibTableColumn
avGenOpServerInetAddress=_AvGenOpServerInetAddress_Object((1,3,6,1,4,1,6889,2,6,5,1,2,1,25),_AvGenOpServerInetAddress_Type())
avGenOpServerInetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenOpServerInetAddress.setStatus(_A)
_AvGenApplications_ObjectIdentity=ObjectIdentity
avGenApplications=_AvGenApplications_ObjectIdentity((1,3,6,1,4,1,6889,2,6,5,2))
_AvGenAppFileTable_Object=MibTable
avGenAppFileTable=_AvGenAppFileTable_Object((1,3,6,1,4,1,6889,2,6,5,2,1))
if mibBuilder.loadTexts:avGenAppFileTable.setStatus(_A)
_AvGenAppFileEntry_Object=MibTableRow
avGenAppFileEntry=_AvGenAppFileEntry_Object((1,3,6,1,4,1,6889,2,6,5,2,1,1))
avGenAppFileEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:avGenAppFileEntry.setStatus(_A)
class _AvGenAppFileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AvGenAppFileId_Type.__name__=_D
_AvGenAppFileId_Object=MibTableColumn
avGenAppFileId=_AvGenAppFileId_Object((1,3,6,1,4,1,6889,2,6,5,2,1,1,1),_AvGenAppFileId_Type())
avGenAppFileId.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenAppFileId.setStatus(_A)
class _AvGenAppFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvGenAppFileName_Type.__name__=_F
_AvGenAppFileName_Object=MibTableColumn
avGenAppFileName=_AvGenAppFileName_Object((1,3,6,1,4,1,6889,2,6,5,2,1,1,2),_AvGenAppFileName_Type())
avGenAppFileName.setMaxAccess(_N)
if mibBuilder.loadTexts:avGenAppFileName.setStatus(_A)
class _AvGenAppFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34)));namedValues=NamedValues(*(('runningConfiguration',1),('startupConfiguration',2),('defaultConfiguration',3),(_T,4),('genConfigFile',5),('logFile',6),('nvramFile',7),('swRuntimeImage',8),('swBootImage',9),('swComponent',10),('other',11),('swWebImage',12),('swAPImage',13),('swNonDownLoadRunTimeImage',14),('asgAuthFile',15),('licenseFile',16),('phoneScriptFile',17),('phoneImageFile',18),('dhcpBindingFile',19),(_W,20),('backupDatabase',21),('syslogFile',22),('cdrFile',23),('swRuntimeServicePack',24),('swComponentServicePack',25),('trustedCertificate',26),('certificateRequest',27),('serverCertificate',28),('privateKey',29),('staticLanguagePack',30),('phoneAvayaUnicodeMessageFile',31),('phoneCustomUnicodeMessageFile',32),('startupConfigurationWizardTaskFile',33),('genConfigurationWizardTaskFile',34)))
_AvGenAppFileType_Type.__name__=_D
_AvGenAppFileType_Object=MibTableColumn
avGenAppFileType=_AvGenAppFileType_Object((1,3,6,1,4,1,6889,2,6,5,2,1,1,3),_AvGenAppFileType_Type())
avGenAppFileType.setMaxAccess(_N)
if mibBuilder.loadTexts:avGenAppFileType.setStatus(_A)
class _AvGenAppFileDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvGenAppFileDescription_Type.__name__=_F
_AvGenAppFileDescription_Object=MibTableColumn
avGenAppFileDescription=_AvGenAppFileDescription_Object((1,3,6,1,4,1,6889,2,6,5,2,1,1,4),_AvGenAppFileDescription_Type())
avGenAppFileDescription.setMaxAccess(_N)
if mibBuilder.loadTexts:avGenAppFileDescription.setStatus(_A)
_AvGenAppFileSize_Type=Integer32
_AvGenAppFileSize_Object=MibTableColumn
avGenAppFileSize=_AvGenAppFileSize_Object((1,3,6,1,4,1,6889,2,6,5,2,1,1,5),_AvGenAppFileSize_Type())
avGenAppFileSize.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenAppFileSize.setStatus(_A)
_AvGenAppFileVersionNumber_Type=DisplayString
_AvGenAppFileVersionNumber_Object=MibTableColumn
avGenAppFileVersionNumber=_AvGenAppFileVersionNumber_Object((1,3,6,1,4,1,6889,2,6,5,2,1,1,6),_AvGenAppFileVersionNumber_Type())
avGenAppFileVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenAppFileVersionNumber.setStatus(_A)
class _AvGenAppFileLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ram',1),(_X,2),(_Y,3),('nvram',4),(_Z,5),('compactFlash',6),('flash',7)))
_AvGenAppFileLocation_Type.__name__=_D
_AvGenAppFileLocation_Object=MibTableColumn
avGenAppFileLocation=_AvGenAppFileLocation_Object((1,3,6,1,4,1,6889,2,6,5,2,1,1,7),_AvGenAppFileLocation_Type())
avGenAppFileLocation.setMaxAccess(_N)
if mibBuilder.loadTexts:avGenAppFileLocation.setStatus(_A)
class _AvGenAppFileDateStamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvGenAppFileDateStamp_Type.__name__=_F
_AvGenAppFileDateStamp_Object=MibTableColumn
avGenAppFileDateStamp=_AvGenAppFileDateStamp_Object((1,3,6,1,4,1,6889,2,6,5,2,1,1,8),_AvGenAppFileDateStamp_Type())
avGenAppFileDateStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenAppFileDateStamp.setStatus(_A)
_AvGenAppFileRowStatus_Type=RowStatus
_AvGenAppFileRowStatus_Object=MibTableColumn
avGenAppFileRowStatus=_AvGenAppFileRowStatus_Object((1,3,6,1,4,1,6889,2,6,5,2,1,1,9),_AvGenAppFileRowStatus_Type())
avGenAppFileRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:avGenAppFileRowStatus.setStatus(_A)
_AvGenAppFilePortNetwork_Type=Integer32
_AvGenAppFilePortNetwork_Object=MibTableColumn
avGenAppFilePortNetwork=_AvGenAppFilePortNetwork_Object((1,3,6,1,4,1,6889,2,6,5,2,1,1,10),_AvGenAppFilePortNetwork_Type())
avGenAppFilePortNetwork.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenAppFilePortNetwork.setStatus(_A)
class _AvGenAppFileDuplStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('standby',2),('not-administered',3)))
_AvGenAppFileDuplStatus_Type.__name__=_D
_AvGenAppFileDuplStatus_Object=MibTableColumn
avGenAppFileDuplStatus=_AvGenAppFileDuplStatus_Object((1,3,6,1,4,1,6889,2,6,5,2,1,1,11),_AvGenAppFileDuplStatus_Type())
avGenAppFileDuplStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenAppFileDuplStatus.setStatus(_A)
_AvGenAppFileCompatibleVersionNumber_Type=DisplayString
_AvGenAppFileCompatibleVersionNumber_Object=MibTableColumn
avGenAppFileCompatibleVersionNumber=_AvGenAppFileCompatibleVersionNumber_Object((1,3,6,1,4,1,6889,2,6,5,2,1,1,12),_AvGenAppFileCompatibleVersionNumber_Type())
avGenAppFileCompatibleVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenAppFileCompatibleVersionNumber.setStatus(_A)
_AvLoadNotificationDefinitions_ObjectIdentity=ObjectIdentity
avLoadNotificationDefinitions=_AvLoadNotificationDefinitions_ObjectIdentity((1,3,6,1,4,1,6889,2,6,5,3))
_AvLoadSysDescription_Type=DisplayString
_AvLoadSysDescription_Object=MibScalar
avLoadSysDescription=_AvLoadSysDescription_Object((1,3,6,1,4,1,6889,2,6,5,3,1),_AvLoadSysDescription_Type())
avLoadSysDescription.setMaxAccess(_a)
if mibBuilder.loadTexts:avLoadSysDescription.setStatus(_A)
_AvLoadSeverity_Type=AvLoadItuPerceivedSeverity
_AvLoadSeverity_Object=MibScalar
avLoadSeverity=_AvLoadSeverity_Object((1,3,6,1,4,1,6889,2,6,5,3,2),_AvLoadSeverity_Type())
avLoadSeverity.setMaxAccess(_a)
if mibBuilder.loadTexts:avLoadSeverity.setStatus(_A)
_AvLoadGeneralInformation_ObjectIdentity=ObjectIdentity
avLoadGeneralInformation=_AvLoadGeneralInformation_ObjectIdentity((1,3,6,1,4,1,6889,2,6,5,4))
class _AvGenLoadConnectionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('off',2),('down',3),('init',4),('up',5),(_O,6)))
_AvGenLoadConnectionState_Type.__name__=_D
_AvGenLoadConnectionState_Object=MibScalar
avGenLoadConnectionState=_AvGenLoadConnectionState_Object((1,3,6,1,4,1,6889,2,6,5,4,1),_AvGenLoadConnectionState_Type())
avGenLoadConnectionState.setMaxAccess(_E)
if mibBuilder.loadTexts:avGenLoadConnectionState.setStatus(_A)
class _AvGenRestoreOperationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_U,2)))
_AvGenRestoreOperationState_Type.__name__=_D
_AvGenRestoreOperationState_Object=MibScalar
avGenRestoreOperationState=_AvGenRestoreOperationState_Object((1,3,6,1,4,1,6889,2,6,5,4,2),_AvGenRestoreOperationState_Type())
avGenRestoreOperationState.setMaxAccess(_C)
if mibBuilder.loadTexts:avGenRestoreOperationState.setStatus(_A)
_AvLoadApplMemTable_Object=MibTable
avLoadApplMemTable=_AvLoadApplMemTable_Object((1,3,6,1,4,1,6889,2,6,5,5))
if mibBuilder.loadTexts:avLoadApplMemTable.setStatus(_A)
_AvLoadApplMemEntry_Object=MibTableRow
avLoadApplMemEntry=_AvLoadApplMemEntry_Object((1,3,6,1,4,1,6889,2,6,5,5,1))
avLoadApplMemEntry.setIndexNames((0,_B,_b),(0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:avLoadApplMemEntry.setStatus(_A)
_AvLoadApplMemModuleId_Type=Integer32
_AvLoadApplMemModuleId_Object=MibTableColumn
avLoadApplMemModuleId=_AvLoadApplMemModuleId_Object((1,3,6,1,4,1,6889,2,6,5,5,1,1),_AvLoadApplMemModuleId_Type())
avLoadApplMemModuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:avLoadApplMemModuleId.setStatus(_A)
class _AvLoadApplMemLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ram',1),(_X,2),(_Y,3),('nvram',4),(_Z,5)))
_AvLoadApplMemLocation_Type.__name__=_D
_AvLoadApplMemLocation_Object=MibTableColumn
avLoadApplMemLocation=_AvLoadApplMemLocation_Object((1,3,6,1,4,1,6889,2,6,5,5,1,2),_AvLoadApplMemLocation_Type())
avLoadApplMemLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:avLoadApplMemLocation.setStatus(_A)
class _AvLoadApplMemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(20));namedValues=NamedValues((_W,20))
_AvLoadApplMemType_Type.__name__=_D
_AvLoadApplMemType_Object=MibTableColumn
avLoadApplMemType=_AvLoadApplMemType_Object((1,3,6,1,4,1,6889,2,6,5,5,1,3),_AvLoadApplMemType_Type())
avLoadApplMemType.setMaxAccess(_C)
if mibBuilder.loadTexts:avLoadApplMemType.setStatus(_A)
_AvLoadApplMemSize_Type=Integer32
_AvLoadApplMemSize_Object=MibTableColumn
avLoadApplMemSize=_AvLoadApplMemSize_Object((1,3,6,1,4,1,6889,2,6,5,5,1,4),_AvLoadApplMemSize_Type())
avLoadApplMemSize.setMaxAccess(_E)
if mibBuilder.loadTexts:avLoadApplMemSize.setStatus(_A)
_AvLoadApplMemTotalBytesUsed_Type=Integer32
_AvLoadApplMemTotalBytesUsed_Object=MibTableColumn
avLoadApplMemTotalBytesUsed=_AvLoadApplMemTotalBytesUsed_Object((1,3,6,1,4,1,6889,2,6,5,5,1,5),_AvLoadApplMemTotalBytesUsed_Type())
avLoadApplMemTotalBytesUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:avLoadApplMemTotalBytesUsed.setStatus(_A)
_AvLoadApplMemTotalBytesFree_Type=Integer32
_AvLoadApplMemTotalBytesFree_Object=MibTableColumn
avLoadApplMemTotalBytesFree=_AvLoadApplMemTotalBytesFree_Object((1,3,6,1,4,1,6889,2,6,5,5,1,6),_AvLoadApplMemTotalBytesFree_Type())
avLoadApplMemTotalBytesFree.setMaxAccess(_C)
if mibBuilder.loadTexts:avLoadApplMemTotalBytesFree.setStatus(_A)
_AvLoadAppDynamicFileTable_Object=MibTable
avLoadAppDynamicFileTable=_AvLoadAppDynamicFileTable_Object((1,3,6,1,4,1,6889,2,6,5,6))
if mibBuilder.loadTexts:avLoadAppDynamicFileTable.setStatus(_A)
_AvLoadAppDynamicFileEntry_Object=MibTableRow
avLoadAppDynamicFileEntry=_AvLoadAppDynamicFileEntry_Object((1,3,6,1,4,1,6889,2,6,5,6,1))
avLoadAppDynamicFileEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:avLoadAppDynamicFileEntry.setStatus(_A)
class _AvLoadAppDynamicFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AvLoadAppDynamicFileName_Type.__name__=_F
_AvLoadAppDynamicFileName_Object=MibTableColumn
avLoadAppDynamicFileName=_AvLoadAppDynamicFileName_Object((1,3,6,1,4,1,6889,2,6,5,6,1,1),_AvLoadAppDynamicFileName_Type())
avLoadAppDynamicFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:avLoadAppDynamicFileName.setStatus(_A)
class _AvLoadAppDynamicFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('file',1),('directory',2)))
_AvLoadAppDynamicFileType_Type.__name__=_D
_AvLoadAppDynamicFileType_Object=MibTableColumn
avLoadAppDynamicFileType=_AvLoadAppDynamicFileType_Object((1,3,6,1,4,1,6889,2,6,5,6,1,2),_AvLoadAppDynamicFileType_Type())
avLoadAppDynamicFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:avLoadAppDynamicFileType.setStatus(_A)
_AvLoadAppDynamicFileSize_Type=Integer32
_AvLoadAppDynamicFileSize_Object=MibTableColumn
avLoadAppDynamicFileSize=_AvLoadAppDynamicFileSize_Object((1,3,6,1,4,1,6889,2,6,5,6,1,3),_AvLoadAppDynamicFileSize_Type())
avLoadAppDynamicFileSize.setMaxAccess(_C)
if mibBuilder.loadTexts:avLoadAppDynamicFileSize.setStatus(_A)
class _AvLoadAppDynamicFileDateStamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvLoadAppDynamicFileDateStamp_Type.__name__=_F
_AvLoadAppDynamicFileDateStamp_Object=MibTableColumn
avLoadAppDynamicFileDateStamp=_AvLoadAppDynamicFileDateStamp_Object((1,3,6,1,4,1,6889,2,6,5,6,1,4),_AvLoadAppDynamicFileDateStamp_Type())
avLoadAppDynamicFileDateStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:avLoadAppDynamicFileDateStamp.setStatus(_A)
_AvLoadAppDynamicFileRowStatus_Type=RowStatus
_AvLoadAppDynamicFileRowStatus_Object=MibTableColumn
avLoadAppDynamicFileRowStatus=_AvLoadAppDynamicFileRowStatus_Object((1,3,6,1,4,1,6889,2,6,5,6,1,5),_AvLoadAppDynamicFileRowStatus_Type())
avLoadAppDynamicFileRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:avLoadAppDynamicFileRowStatus.setStatus(_A)
avDownloadBegun=NotificationType((1,3,6,1,4,1,6889,2,6,5,0,1))
avDownloadBegun.setObjects(*((_B,_I),(_B,_G),(_B,_H),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:avDownloadBegun.setStatus(_A)
avDownloadSuccess=NotificationType((1,3,6,1,4,1,6889,2,6,5,0,2))
avDownloadSuccess.setObjects(*((_B,_I),(_B,_G),(_B,_H),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:avDownloadSuccess.setStatus(_A)
avDownloadFault=NotificationType((1,3,6,1,4,1,6889,2,6,5,0,3))
avDownloadFault.setObjects(*((_B,_I),(_B,_G),(_B,_H),(_B,_J),(_B,_K),(_B,_L),(_B,_P),(_B,_Q),(_B,_M)))
if mibBuilder.loadTexts:avDownloadFault.setStatus(_A)
avUploadBegun=NotificationType((1,3,6,1,4,1,6889,2,6,5,0,4))
avUploadBegun.setObjects(*((_B,_I),(_B,_G),(_B,_H),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:avUploadBegun.setStatus(_A)
avUploadSuccess=NotificationType((1,3,6,1,4,1,6889,2,6,5,0,5))
avUploadSuccess.setObjects(*((_B,_I),(_B,_G),(_B,_H),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:avUploadSuccess.setStatus(_A)
avUploadFault=NotificationType((1,3,6,1,4,1,6889,2,6,5,0,6))
avUploadFault.setObjects(*((_B,_I),(_B,_G),(_B,_H),(_B,_J),(_B,_K),(_B,_L),(_B,_P),(_B,_Q),(_B,_M)))
if mibBuilder.loadTexts:avUploadFault.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AvLoadItuPerceivedSeverity':AvLoadItuPerceivedSeverity,'avLoad':avLoad,'avLoadNotification':avLoadNotification,'avDownloadBegun':avDownloadBegun,'avDownloadSuccess':avDownloadSuccess,'avDownloadFault':avDownloadFault,'avUploadBegun':avUploadBegun,'avUploadSuccess':avUploadSuccess,'avUploadFault':avUploadFault,'avGenOperations':avGenOperations,'avGenLoadNumberOfSession':avGenLoadNumberOfSession,'avGenOpTable':avGenOpTable,'avGenOpEntry':avGenOpEntry,_G:avGenOpModuleId,_S:avGenOpIndex,'avGenOpRunningState':avGenOpRunningState,'avGenOpSourceIndex':avGenOpSourceIndex,'avGenOpDestIndex':avGenOpDestIndex,'avGenOpServerIP':avGenOpServerIP,'avGenOpUserName':avGenOpUserName,'avGenOpPassword':avGenOpPassword,'avGenOpProtocolType':avGenOpProtocolType,'avGenOpFileName':avGenOpFileName,'avGenOpRunningStateDisplay':avGenOpRunningStateDisplay,_P:avGenOpLastFailureIndex,_Q:avGenOpLastFailureDisplay,'avGenOpLastWarningDisplay':avGenOpLastWarningDisplay,'avGenOpErrorLogIndex':avGenOpErrorLogIndex,'avGenOpResetSupported':avGenOpResetSupported,'avGenOpEnableReset':avGenOpEnableReset,'avGenOpNextBootImageIndex':avGenOpNextBootImageIndex,'avGenOpLastBootImageIndex':avGenOpLastBootImageIndex,'avGenOpFileSystemType':avGenOpFileSystemType,'avGenOpReportSpecificFlags':avGenOpReportSpecificFlags,'avGenOpOctetsReceived':avGenOpOctetsReceived,'avGenOpDownloadProxy':avGenOpDownloadProxy,'avGenOpServerInetAddressType':avGenOpServerInetAddressType,'avGenOpServerInetAddress':avGenOpServerInetAddress,'avGenApplications':avGenApplications,'avGenAppFileTable':avGenAppFileTable,'avGenAppFileEntry':avGenAppFileEntry,_H:avGenAppFileId,_J:avGenAppFileName,'avGenAppFileType':avGenAppFileType,_K:avGenAppFileDescription,'avGenAppFileSize':avGenAppFileSize,_L:avGenAppFileVersionNumber,'avGenAppFileLocation':avGenAppFileLocation,'avGenAppFileDateStamp':avGenAppFileDateStamp,'avGenAppFileRowStatus':avGenAppFileRowStatus,'avGenAppFilePortNetwork':avGenAppFilePortNetwork,'avGenAppFileDuplStatus':avGenAppFileDuplStatus,'avGenAppFileCompatibleVersionNumber':avGenAppFileCompatibleVersionNumber,'avLoadNotificationDefinitions':avLoadNotificationDefinitions,_I:avLoadSysDescription,_M:avLoadSeverity,'avLoadGeneralInformation':avLoadGeneralInformation,'avGenLoadConnectionState':avGenLoadConnectionState,'avGenRestoreOperationState':avGenRestoreOperationState,'avLoadApplMemTable':avLoadApplMemTable,'avLoadApplMemEntry':avLoadApplMemEntry,_b:avLoadApplMemModuleId,_c:avLoadApplMemLocation,_d:avLoadApplMemType,'avLoadApplMemSize':avLoadApplMemSize,'avLoadApplMemTotalBytesUsed':avLoadApplMemTotalBytesUsed,'avLoadApplMemTotalBytesFree':avLoadApplMemTotalBytesFree,'avLoadAppDynamicFileTable':avLoadAppDynamicFileTable,'avLoadAppDynamicFileEntry':avLoadAppDynamicFileEntry,_e:avLoadAppDynamicFileName,'avLoadAppDynamicFileType':avLoadAppDynamicFileType,'avLoadAppDynamicFileSize':avLoadAppDynamicFileSize,'avLoadAppDynamicFileDateStamp':avLoadAppDynamicFileDateStamp,'avLoadAppDynamicFileRowStatus':avLoadAppDynamicFileRowStatus})