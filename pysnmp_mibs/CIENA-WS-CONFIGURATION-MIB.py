_T='cienaWsConfigurationGroup'
_S='cwsConfigurationZtpStateLastConfigFile'
_R='cwsConfigurationZtpStateLastCommandFile'
_Q='cwsConfigurationZtpStateLastFailure'
_P='cwsConfigurationZtpStateOperationalState'
_O='cwsConfigurationZtpStateAdminState'
_N='cwsConfigurationDefaultFilesBackupLoadFilename'
_M='cwsConfigurationDefaultFilesLoadFilename'
_L='cwsConfigurationDefaultFilesSaveFilename'
_K='cwsConfigurationZtpStateTableSnmpKey'
_J='cwsConfigurationDefaultFilesTableSnmpKey'
_I='cwsConfigurationFileListTableSnmpKey'
_H='unknown'
_G='not-accessible'
_F='cwsConfigurationConfigurationFilesTableSnmpKey'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CIENA-WS-CONFIGURATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaWsConfig,=mibBuilder.importSymbols('CIENA-WS-MIB','cienaWsConfig')
EnabledDisabledEnum,StringMaxl128,StringMaxl254=mibBuilder.importSymbols('CIENA-WS-TYPEDEFS-MIB','EnabledDisabledEnum','StringMaxl128','StringMaxl254')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cienaWsConfigurationMIB=ModuleIdentity((1,3,6,1,4,1,1271,3,4,19))
if mibBuilder.loadTexts:cienaWsConfigurationMIB.setRevisions(('2017-04-05 00:00','2017-03-02 00:00','2016-12-12 00:00','2016-06-15 00:00','2015-09-23 00:00'))
class ZtpError(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)));namedValues=NamedValues(*((_H,0),('none',1),('bootFileDownloadFailed',2),('bootFileParseError',3),('ftpConfigError',4),('ftpLicenseFileError',5),('ftpSoftwareLoadFileError',6),('sshKeyError',7),('licenseIdError',8),('licenseDownloadError',9),('licenseInstallError',10),('licenseHostIdMismatchError',11),('licenseWarmRebootRequired',12),('licenseUnsupportedFileType',13),('expiredLicenseFile',14),('systemTimeNotSet',15),('loginBannerError',16),('welcomeBannerError',17),('configFileDownloadFailed',18),('configFileApplyFailed',19),('softwareUpgradeFailed',20),('softwareServerSetFailed',21),('softwareDownloadFailed',22),('softwareRepositoryRemountFailed',23),('softwareUnzipFailed',24),('softwareAlreadyRunning',25),('scriptFileDownloadFailed',26),('scriptFileApplyFailed',27)))
class ZtpOperationalState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*((_H,0),('idle',1),('start',2),('restarting',3),('waitingForDhcpLease',4),('downloadingBootFile',5),('parsingBootFile',6),('processingBootFile',7),('processingFtpConfigFile',8),('processingFtpLicenseFile',9),('processingFtpSoftwareLoadFile',10),('processingSshKeys',11),('processingLicenseId',12),('installingLicenses',13),('downloadingLoginBanner',14),('downloadingWelcomeBanner',15),('downloadingConfigFile',16),('applyingConfigFile',17),('processingConfigFile',18),('processingSoftwarePackage',19),('requestingReboot',20),('upgradingSoftware',21),('booting',22),('completed',23),('failed',24),('downloadingScriptFile',25),('downloadingLicenses',26)))
_CienaWsConfigurationObjects_ObjectIdentity=ObjectIdentity
cienaWsConfigurationObjects=_CienaWsConfigurationObjects_ObjectIdentity((1,3,6,1,4,1,1271,3,4,19,1))
_CienaWsConfigurationConformance_ObjectIdentity=ObjectIdentity
cienaWsConfigurationConformance=_CienaWsConfigurationConformance_ObjectIdentity((1,3,6,1,4,1,1271,3,4,19,2))
_CienaWsConfigurationGroups_ObjectIdentity=ObjectIdentity
cienaWsConfigurationGroups=_CienaWsConfigurationGroups_ObjectIdentity((1,3,6,1,4,1,1271,3,4,19,2,1))
_CienaWsConfigurationCompliances_ObjectIdentity=ObjectIdentity
cienaWsConfigurationCompliances=_CienaWsConfigurationCompliances_ObjectIdentity((1,3,6,1,4,1,1271,3,4,19,2,2))
_CwsConfigurationFileListTable_Object=MibTable
cwsConfigurationFileListTable=_CwsConfigurationFileListTable_Object((1,3,6,1,4,1,1271,3,4,19,3))
if mibBuilder.loadTexts:cwsConfigurationFileListTable.setStatus(_A)
_CwsConfigurationFileListEntry_Object=MibTableRow
cwsConfigurationFileListEntry=_CwsConfigurationFileListEntry_Object((1,3,6,1,4,1,1271,3,4,19,3,1))
cwsConfigurationFileListEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:cwsConfigurationFileListEntry.setStatus(_A)
class _CwsConfigurationFileListTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsConfigurationFileListTableSnmpKey_Type.__name__=_D
_CwsConfigurationFileListTableSnmpKey_Object=MibTableColumn
cwsConfigurationFileListTableSnmpKey=_CwsConfigurationFileListTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,19,3,1,1),_CwsConfigurationFileListTableSnmpKey_Type())
cwsConfigurationFileListTableSnmpKey.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsConfigurationFileListTableSnmpKey.setStatus(_A)
_CwsConfigurationFileList_Type=StringMaxl254
_CwsConfigurationFileList_Object=MibTableColumn
cwsConfigurationFileList=_CwsConfigurationFileList_Object((1,3,6,1,4,1,1271,3,4,19,3,1,2),_CwsConfigurationFileList_Type())
cwsConfigurationFileList.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsConfigurationFileList.setStatus(_A)
_CwsConfigurationConfigurationFilesTable_Object=MibTable
cwsConfigurationConfigurationFilesTable=_CwsConfigurationConfigurationFilesTable_Object((1,3,6,1,4,1,1271,3,4,19,4))
if mibBuilder.loadTexts:cwsConfigurationConfigurationFilesTable.setStatus(_A)
_CwsConfigurationConfigurationFilesEntry_Object=MibTableRow
cwsConfigurationConfigurationFilesEntry=_CwsConfigurationConfigurationFilesEntry_Object((1,3,6,1,4,1,1271,3,4,19,4,1))
cwsConfigurationConfigurationFilesEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cwsConfigurationConfigurationFilesEntry.setStatus(_A)
class _CwsConfigurationConfigurationFilesTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsConfigurationConfigurationFilesTableSnmpKey_Type.__name__=_D
_CwsConfigurationConfigurationFilesTableSnmpKey_Object=MibTableColumn
cwsConfigurationConfigurationFilesTableSnmpKey=_CwsConfigurationConfigurationFilesTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,19,4,1,1),_CwsConfigurationConfigurationFilesTableSnmpKey_Type())
cwsConfigurationConfigurationFilesTableSnmpKey.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsConfigurationConfigurationFilesTableSnmpKey.setStatus(_A)
_CwsConfigurationDefaultFilesTable_Object=MibTable
cwsConfigurationDefaultFilesTable=_CwsConfigurationDefaultFilesTable_Object((1,3,6,1,4,1,1271,3,4,19,5))
if mibBuilder.loadTexts:cwsConfigurationDefaultFilesTable.setStatus(_A)
_CwsConfigurationDefaultFilesEntry_Object=MibTableRow
cwsConfigurationDefaultFilesEntry=_CwsConfigurationDefaultFilesEntry_Object((1,3,6,1,4,1,1271,3,4,19,5,1))
cwsConfigurationDefaultFilesEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cwsConfigurationDefaultFilesEntry.setStatus(_A)
class _CwsConfigurationDefaultFilesTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsConfigurationDefaultFilesTableSnmpKey_Type.__name__=_D
_CwsConfigurationDefaultFilesTableSnmpKey_Object=MibTableColumn
cwsConfigurationDefaultFilesTableSnmpKey=_CwsConfigurationDefaultFilesTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,19,5,1,1),_CwsConfigurationDefaultFilesTableSnmpKey_Type())
cwsConfigurationDefaultFilesTableSnmpKey.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsConfigurationDefaultFilesTableSnmpKey.setStatus(_A)
_CwsConfigurationDefaultFilesSaveFilename_Type=StringMaxl254
_CwsConfigurationDefaultFilesSaveFilename_Object=MibTableColumn
cwsConfigurationDefaultFilesSaveFilename=_CwsConfigurationDefaultFilesSaveFilename_Object((1,3,6,1,4,1,1271,3,4,19,5,1,2),_CwsConfigurationDefaultFilesSaveFilename_Type())
cwsConfigurationDefaultFilesSaveFilename.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsConfigurationDefaultFilesSaveFilename.setStatus(_A)
_CwsConfigurationDefaultFilesLoadFilename_Type=StringMaxl254
_CwsConfigurationDefaultFilesLoadFilename_Object=MibTableColumn
cwsConfigurationDefaultFilesLoadFilename=_CwsConfigurationDefaultFilesLoadFilename_Object((1,3,6,1,4,1,1271,3,4,19,5,1,3),_CwsConfigurationDefaultFilesLoadFilename_Type())
cwsConfigurationDefaultFilesLoadFilename.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsConfigurationDefaultFilesLoadFilename.setStatus(_A)
_CwsConfigurationDefaultFilesBackupLoadFilename_Type=StringMaxl254
_CwsConfigurationDefaultFilesBackupLoadFilename_Object=MibTableColumn
cwsConfigurationDefaultFilesBackupLoadFilename=_CwsConfigurationDefaultFilesBackupLoadFilename_Object((1,3,6,1,4,1,1271,3,4,19,5,1,4),_CwsConfigurationDefaultFilesBackupLoadFilename_Type())
cwsConfigurationDefaultFilesBackupLoadFilename.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsConfigurationDefaultFilesBackupLoadFilename.setStatus(_A)
_CwsConfigurationZtpStateTable_Object=MibTable
cwsConfigurationZtpStateTable=_CwsConfigurationZtpStateTable_Object((1,3,6,1,4,1,1271,3,4,19,7))
if mibBuilder.loadTexts:cwsConfigurationZtpStateTable.setStatus(_A)
_CwsConfigurationZtpStateEntry_Object=MibTableRow
cwsConfigurationZtpStateEntry=_CwsConfigurationZtpStateEntry_Object((1,3,6,1,4,1,1271,3,4,19,7,1))
cwsConfigurationZtpStateEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:cwsConfigurationZtpStateEntry.setStatus(_A)
class _CwsConfigurationZtpStateTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsConfigurationZtpStateTableSnmpKey_Type.__name__=_D
_CwsConfigurationZtpStateTableSnmpKey_Object=MibTableColumn
cwsConfigurationZtpStateTableSnmpKey=_CwsConfigurationZtpStateTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,19,7,1,1),_CwsConfigurationZtpStateTableSnmpKey_Type())
cwsConfigurationZtpStateTableSnmpKey.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsConfigurationZtpStateTableSnmpKey.setStatus(_A)
_CwsConfigurationZtpStateAdminState_Type=EnabledDisabledEnum
_CwsConfigurationZtpStateAdminState_Object=MibTableColumn
cwsConfigurationZtpStateAdminState=_CwsConfigurationZtpStateAdminState_Object((1,3,6,1,4,1,1271,3,4,19,7,1,2),_CwsConfigurationZtpStateAdminState_Type())
cwsConfigurationZtpStateAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsConfigurationZtpStateAdminState.setStatus(_A)
_CwsConfigurationZtpStateOperationalState_Type=ZtpOperationalState
_CwsConfigurationZtpStateOperationalState_Object=MibTableColumn
cwsConfigurationZtpStateOperationalState=_CwsConfigurationZtpStateOperationalState_Object((1,3,6,1,4,1,1271,3,4,19,7,1,3),_CwsConfigurationZtpStateOperationalState_Type())
cwsConfigurationZtpStateOperationalState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsConfigurationZtpStateOperationalState.setStatus(_A)
_CwsConfigurationZtpStateLastFailure_Type=ZtpError
_CwsConfigurationZtpStateLastFailure_Object=MibTableColumn
cwsConfigurationZtpStateLastFailure=_CwsConfigurationZtpStateLastFailure_Object((1,3,6,1,4,1,1271,3,4,19,7,1,4),_CwsConfigurationZtpStateLastFailure_Type())
cwsConfigurationZtpStateLastFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsConfigurationZtpStateLastFailure.setStatus(_A)
_CwsConfigurationZtpStateLastCommandFile_Type=StringMaxl128
_CwsConfigurationZtpStateLastCommandFile_Object=MibTableColumn
cwsConfigurationZtpStateLastCommandFile=_CwsConfigurationZtpStateLastCommandFile_Object((1,3,6,1,4,1,1271,3,4,19,7,1,5),_CwsConfigurationZtpStateLastCommandFile_Type())
cwsConfigurationZtpStateLastCommandFile.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsConfigurationZtpStateLastCommandFile.setStatus(_A)
_CwsConfigurationZtpStateLastConfigFile_Type=StringMaxl128
_CwsConfigurationZtpStateLastConfigFile_Object=MibTableColumn
cwsConfigurationZtpStateLastConfigFile=_CwsConfigurationZtpStateLastConfigFile_Object((1,3,6,1,4,1,1271,3,4,19,7,1,6),_CwsConfigurationZtpStateLastConfigFile_Type())
cwsConfigurationZtpStateLastConfigFile.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsConfigurationZtpStateLastConfigFile.setStatus(_A)
cienaWsConfigurationGroup=ObjectGroup((1,3,6,1,4,1,1271,3,4,19,2,1,1))
cienaWsConfigurationGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:cienaWsConfigurationGroup.setStatus(_A)
cienaWsConfigurationCompliance=ModuleCompliance((1,3,6,1,4,1,1271,3,4,19,2,2,1))
cienaWsConfigurationCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:cienaWsConfigurationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ZtpError':ZtpError,'ZtpOperationalState':ZtpOperationalState,'cienaWsConfigurationMIB':cienaWsConfigurationMIB,'cienaWsConfigurationObjects':cienaWsConfigurationObjects,'cienaWsConfigurationConformance':cienaWsConfigurationConformance,'cienaWsConfigurationGroups':cienaWsConfigurationGroups,_T:cienaWsConfigurationGroup,'cienaWsConfigurationCompliances':cienaWsConfigurationCompliances,'cienaWsConfigurationCompliance':cienaWsConfigurationCompliance,'cwsConfigurationFileListTable':cwsConfigurationFileListTable,'cwsConfigurationFileListEntry':cwsConfigurationFileListEntry,_I:cwsConfigurationFileListTableSnmpKey,'cwsConfigurationFileList':cwsConfigurationFileList,'cwsConfigurationConfigurationFilesTable':cwsConfigurationConfigurationFilesTable,'cwsConfigurationConfigurationFilesEntry':cwsConfigurationConfigurationFilesEntry,_F:cwsConfigurationConfigurationFilesTableSnmpKey,'cwsConfigurationDefaultFilesTable':cwsConfigurationDefaultFilesTable,'cwsConfigurationDefaultFilesEntry':cwsConfigurationDefaultFilesEntry,_J:cwsConfigurationDefaultFilesTableSnmpKey,_L:cwsConfigurationDefaultFilesSaveFilename,_M:cwsConfigurationDefaultFilesLoadFilename,_N:cwsConfigurationDefaultFilesBackupLoadFilename,'cwsConfigurationZtpStateTable':cwsConfigurationZtpStateTable,'cwsConfigurationZtpStateEntry':cwsConfigurationZtpStateEntry,_K:cwsConfigurationZtpStateTableSnmpKey,_O:cwsConfigurationZtpStateAdminState,_P:cwsConfigurationZtpStateOperationalState,_Q:cwsConfigurationZtpStateLastFailure,_R:cwsConfigurationZtpStateLastCommandFile,_S:cwsConfigurationZtpStateLastConfigFile})