_AX='backupSftpUploadMinimalGroupV1'
_AW='backupSftpUploadGroup'
_AV='backupGeneralGroupV8'
_AU='backupGeneralGroupV7'
_AT='backupUploadGroupV2'
_AS='backupGeneralGroupV4'
_AR='backupGeneralGroupV2'
_AQ='backupGeneralGroup'
_AP='backupUploadStatus'
_AO='backupUploadUploadNow'
_AN='backupFileUrl'
_AM='backupPersistentFileDescr'
_AL='backupPersistentFileName'
_AK='backupCommandResult'
_AJ='backupCommandAction'
_AI='backupCommandAdminStatus'
_AH='backupCommandDescr'
_AG='backupCommandName'
_AF='backupGeneralMibImplVersion'
_AE='backupGeneralMibSpecVersion'
_AD='backupGeneralTestAndIncr'
_AC='secondary'
_AB='backupSftpUploadMinimalGroupV2'
_AA='backupSftpUploadGroupV2'
_A9='backupGeneralGroupV9'
_A8='backupGeneralGroupV6'
_A7='backupUploadGroup'
_A6='backupGeneralGroupV5'
_A5='backupSftpUploadRestoreEntityRestoreNow'
_A4='backupGeneralBackupScheme'
_A3='backupUploadLocalFile'
_A2='backupFileRowStatus'
_A1='backupFileOperStatus'
_A0='backupFileAdminStatus'
_z='backupFileLastChangeTime'
_y='backupFileDescr'
_x='backupFileName'
_w='backupPersistentFileIndex'
_v='down'
_u='backupGeneralGroupV3'
_t='backupGeneralSavedConfigurationGenerationId'
_s='backupUploadInstallUploadFile'
_r='backupUploadServerPath'
_q='busy'
_p='backupFileIndex'
_o='backupUploadMinimalGroupV1'
_n='backupGeneralMinimalGroupV1'
_m='backupFileGroup'
_l='backupSftpUploadRestoreEntityFilePath'
_k='backupSftpUploadBackupEntityFilePath'
_j='backupSftpUploadRestoreEntityAction'
_i='backupSftpUploadBackupEntityCrc'
_h='backupSftpUploadBackupEntityCompressionTimestamp'
_g='backupSftpUploadBackupEntityAvailability'
_f='backupGeneralUnsavedChangesAlarm'
_e='backupGeneralWarnUnsavedDelay'
_d='backupGeneralWarnForUnsaved'
_c='backupUploadNextTime'
_b='backupUploadFailure'
_a='backupUploadLastChangeTime'
_Z='backupUploadResult'
_Y='backupUploadAction'
_X='backupUploadTimeHour'
_W='backupUploadServerAddr'
_V='backupGeneralInstallConfigFile'
_U='idle'
_T='backupUploadGroupV3'
_S='backupGeneralPrimaryFileName'
_R='backupGeneralPersistentFileTableSize'
_Q='backupGeneralFileTableSize'
_P='backupGeneralGlobalConfigLastChangeTime'
_O='backupGeneralGlobalStateLastChangeTime'
_N='backupGeneralUnsavedChanges'
_M='Unsigned32'
_L='backupGeneralConfigLastChangeTime'
_K='DisplayString'
_J='backupGeneralLastChangeTime'
_I='backupFileGroupV2'
_H='backupPersistentFileGroup'
_G='backupCommandGroup'
_F='Integer32'
_E='read-write'
_D='deprecated'
_C='read-only'
_B='current'
_A='LUM-BACKUP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumBackupMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumBackupMIB','lumModules')
CommandString,FaultStatus=mibBuilder.importSymbols('LUM-TC','CommandString','FaultStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_K,'PhysAddress','RowStatus','TextualConvention','TestAndIncr','TruthValue')
lumBackupMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,7))
if mibBuilder.loadTexts:lumBackupMIBModule.setRevisions(('2017-12-15 00:00','2017-06-15 00:00','2016-01-11 00:00','2007-01-11 00:00','2005-12-05 00:00','2004-12-21 00:00','2004-12-20 00:00','2004-11-09 00:00','2004-10-28 00:00','2004-09-30 00:00','2004-06-17 00:00','2002-10-29 00:00','2001-10-30 00:00','2001-08-16 00:00','2001-08-01 00:00'))
_LumBackupConfs_ObjectIdentity=ObjectIdentity
lumBackupConfs=_LumBackupConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,5,1))
_LumBackupGroups_ObjectIdentity=ObjectIdentity
lumBackupGroups=_LumBackupGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,5,1,1))
_LumBackupCompl_ObjectIdentity=ObjectIdentity
lumBackupCompl=_LumBackupCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,5,1,2))
_LumBackupMinimalGroups_ObjectIdentity=ObjectIdentity
lumBackupMinimalGroups=_LumBackupMinimalGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,5,1,3))
_LumBackupMinimalCompl_ObjectIdentity=ObjectIdentity
lumBackupMinimalCompl=_LumBackupMinimalCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,5,1,4))
_LumBackupMIBObjects_ObjectIdentity=ObjectIdentity
lumBackupMIBObjects=_LumBackupMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,5,2))
_BackupGeneral_ObjectIdentity=ObjectIdentity
backupGeneral=_BackupGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,5,2,1))
_BackupGeneralTestAndIncr_Type=TestAndIncr
_BackupGeneralTestAndIncr_Object=MibScalar
backupGeneralTestAndIncr=_BackupGeneralTestAndIncr_Object((1,3,6,1,4,1,8708,2,5,2,1,1),_BackupGeneralTestAndIncr_Type())
backupGeneralTestAndIncr.setMaxAccess(_E)
if mibBuilder.loadTexts:backupGeneralTestAndIncr.setStatus(_B)
class _BackupGeneralMibSpecVersion_Type(DisplayString):defaultValue=OctetString('')
_BackupGeneralMibSpecVersion_Type.__name__=_K
_BackupGeneralMibSpecVersion_Object=MibScalar
backupGeneralMibSpecVersion=_BackupGeneralMibSpecVersion_Object((1,3,6,1,4,1,8708,2,5,2,1,2),_BackupGeneralMibSpecVersion_Type())
backupGeneralMibSpecVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:backupGeneralMibSpecVersion.setStatus(_B)
class _BackupGeneralMibImplVersion_Type(DisplayString):defaultValue=OctetString('')
_BackupGeneralMibImplVersion_Type.__name__=_K
_BackupGeneralMibImplVersion_Object=MibScalar
backupGeneralMibImplVersion=_BackupGeneralMibImplVersion_Object((1,3,6,1,4,1,8708,2,5,2,1,3),_BackupGeneralMibImplVersion_Type())
backupGeneralMibImplVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:backupGeneralMibImplVersion.setStatus(_B)
_BackupGeneralLastChangeTime_Type=DateAndTime
_BackupGeneralLastChangeTime_Object=MibScalar
backupGeneralLastChangeTime=_BackupGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,5,2,1,4),_BackupGeneralLastChangeTime_Type())
backupGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:backupGeneralLastChangeTime.setStatus(_B)
_BackupGeneralConfigLastChangeTime_Type=DateAndTime
_BackupGeneralConfigLastChangeTime_Object=MibScalar
backupGeneralConfigLastChangeTime=_BackupGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,5,2,1,5),_BackupGeneralConfigLastChangeTime_Type())
backupGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:backupGeneralConfigLastChangeTime.setStatus(_B)
_BackupGeneralUnsavedChanges_Type=TruthValue
_BackupGeneralUnsavedChanges_Object=MibScalar
backupGeneralUnsavedChanges=_BackupGeneralUnsavedChanges_Object((1,3,6,1,4,1,8708,2,5,2,1,6),_BackupGeneralUnsavedChanges_Type())
backupGeneralUnsavedChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:backupGeneralUnsavedChanges.setStatus(_B)
_BackupGeneralFileTableSize_Type=Unsigned32
_BackupGeneralFileTableSize_Object=MibScalar
backupGeneralFileTableSize=_BackupGeneralFileTableSize_Object((1,3,6,1,4,1,8708,2,5,2,1,7),_BackupGeneralFileTableSize_Type())
backupGeneralFileTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:backupGeneralFileTableSize.setStatus(_B)
_BackupGeneralPersistentFileTableSize_Type=Unsigned32
_BackupGeneralPersistentFileTableSize_Object=MibScalar
backupGeneralPersistentFileTableSize=_BackupGeneralPersistentFileTableSize_Object((1,3,6,1,4,1,8708,2,5,2,1,8),_BackupGeneralPersistentFileTableSize_Type())
backupGeneralPersistentFileTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:backupGeneralPersistentFileTableSize.setStatus(_B)
_BackupGeneralInstallConfigFile_Type=CommandString
_BackupGeneralInstallConfigFile_Object=MibScalar
backupGeneralInstallConfigFile=_BackupGeneralInstallConfigFile_Object((1,3,6,1,4,1,8708,2,5,2,1,9),_BackupGeneralInstallConfigFile_Type())
backupGeneralInstallConfigFile.setMaxAccess(_E)
if mibBuilder.loadTexts:backupGeneralInstallConfigFile.setStatus(_D)
_BackupGeneralGlobalStateLastChangeTime_Type=DateAndTime
_BackupGeneralGlobalStateLastChangeTime_Object=MibScalar
backupGeneralGlobalStateLastChangeTime=_BackupGeneralGlobalStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,5,2,1,10),_BackupGeneralGlobalStateLastChangeTime_Type())
backupGeneralGlobalStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:backupGeneralGlobalStateLastChangeTime.setStatus(_B)
_BackupGeneralGlobalConfigLastChangeTime_Type=DateAndTime
_BackupGeneralGlobalConfigLastChangeTime_Object=MibScalar
backupGeneralGlobalConfigLastChangeTime=_BackupGeneralGlobalConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,5,2,1,11),_BackupGeneralGlobalConfigLastChangeTime_Type())
backupGeneralGlobalConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:backupGeneralGlobalConfigLastChangeTime.setStatus(_B)
_BackupGeneralPrimaryFileName_Type=DisplayString
_BackupGeneralPrimaryFileName_Object=MibScalar
backupGeneralPrimaryFileName=_BackupGeneralPrimaryFileName_Object((1,3,6,1,4,1,8708,2,5,2,1,12),_BackupGeneralPrimaryFileName_Type())
backupGeneralPrimaryFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:backupGeneralPrimaryFileName.setStatus(_B)
class _BackupGeneralWarnForUnsaved_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_BackupGeneralWarnForUnsaved_Type.__name__=_F
_BackupGeneralWarnForUnsaved_Object=MibScalar
backupGeneralWarnForUnsaved=_BackupGeneralWarnForUnsaved_Object((1,3,6,1,4,1,8708,2,5,2,1,13),_BackupGeneralWarnForUnsaved_Type())
backupGeneralWarnForUnsaved.setMaxAccess(_E)
if mibBuilder.loadTexts:backupGeneralWarnForUnsaved.setStatus(_B)
class _BackupGeneralWarnUnsavedDelay_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_BackupGeneralWarnUnsavedDelay_Type.__name__=_M
_BackupGeneralWarnUnsavedDelay_Object=MibScalar
backupGeneralWarnUnsavedDelay=_BackupGeneralWarnUnsavedDelay_Object((1,3,6,1,4,1,8708,2,5,2,1,14),_BackupGeneralWarnUnsavedDelay_Type())
backupGeneralWarnUnsavedDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:backupGeneralWarnUnsavedDelay.setStatus(_B)
_BackupGeneralUnsavedChangesAlarm_Type=FaultStatus
_BackupGeneralUnsavedChangesAlarm_Object=MibScalar
backupGeneralUnsavedChangesAlarm=_BackupGeneralUnsavedChangesAlarm_Object((1,3,6,1,4,1,8708,2,5,2,1,15),_BackupGeneralUnsavedChangesAlarm_Type())
backupGeneralUnsavedChangesAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:backupGeneralUnsavedChangesAlarm.setStatus(_B)
class _BackupGeneralSavedConfigurationGenerationId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_BackupGeneralSavedConfigurationGenerationId_Type.__name__=_M
_BackupGeneralSavedConfigurationGenerationId_Object=MibScalar
backupGeneralSavedConfigurationGenerationId=_BackupGeneralSavedConfigurationGenerationId_Object((1,3,6,1,4,1,8708,2,5,2,1,16),_BackupGeneralSavedConfigurationGenerationId_Type())
backupGeneralSavedConfigurationGenerationId.setMaxAccess(_E)
if mibBuilder.loadTexts:backupGeneralSavedConfigurationGenerationId.setStatus(_B)
class _BackupGeneralBackupScheme_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tftp',1),('sftp',2)))
_BackupGeneralBackupScheme_Type.__name__=_F
_BackupGeneralBackupScheme_Object=MibScalar
backupGeneralBackupScheme=_BackupGeneralBackupScheme_Object((1,3,6,1,4,1,8708,2,5,2,1,17),_BackupGeneralBackupScheme_Type())
backupGeneralBackupScheme.setMaxAccess(_C)
if mibBuilder.loadTexts:backupGeneralBackupScheme.setStatus(_B)
_BackupFileList_ObjectIdentity=ObjectIdentity
backupFileList=_BackupFileList_ObjectIdentity((1,3,6,1,4,1,8708,2,5,2,2))
_BackupFileTable_Object=MibTable
backupFileTable=_BackupFileTable_Object((1,3,6,1,4,1,8708,2,5,2,2,1))
if mibBuilder.loadTexts:backupFileTable.setStatus(_B)
_BackupFileEntry_Object=MibTableRow
backupFileEntry=_BackupFileEntry_Object((1,3,6,1,4,1,8708,2,5,2,2,1,1))
backupFileEntry.setIndexNames((0,_A,_p))
if mibBuilder.loadTexts:backupFileEntry.setStatus(_B)
class _BackupFileIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BackupFileIndex_Type.__name__=_M
_BackupFileIndex_Object=MibTableColumn
backupFileIndex=_BackupFileIndex_Object((1,3,6,1,4,1,8708,2,5,2,2,1,1,1),_BackupFileIndex_Type())
backupFileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:backupFileIndex.setStatus(_B)
_BackupFileName_Type=DisplayString
_BackupFileName_Object=MibTableColumn
backupFileName=_BackupFileName_Object((1,3,6,1,4,1,8708,2,5,2,2,1,1,2),_BackupFileName_Type())
backupFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:backupFileName.setStatus(_B)
class _BackupFileDescr_Type(DisplayString):defaultValue=OctetString('')
_BackupFileDescr_Type.__name__=_K
_BackupFileDescr_Object=MibTableColumn
backupFileDescr=_BackupFileDescr_Object((1,3,6,1,4,1,8708,2,5,2,2,1,1,3),_BackupFileDescr_Type())
backupFileDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:backupFileDescr.setStatus(_B)
_BackupFileLastChangeTime_Type=DateAndTime
_BackupFileLastChangeTime_Object=MibTableColumn
backupFileLastChangeTime=_BackupFileLastChangeTime_Object((1,3,6,1,4,1,8708,2,5,2,2,1,1,4),_BackupFileLastChangeTime_Type())
backupFileLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:backupFileLastChangeTime.setStatus(_B)
class _BackupFileAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_v,1),(_AC,2),('primary',3)))
_BackupFileAdminStatus_Type.__name__=_F
_BackupFileAdminStatus_Object=MibTableColumn
backupFileAdminStatus=_BackupFileAdminStatus_Object((1,3,6,1,4,1,8708,2,5,2,2,1,1,5),_BackupFileAdminStatus_Type())
backupFileAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:backupFileAdminStatus.setStatus(_B)
class _BackupFileOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),('running',2)))
_BackupFileOperStatus_Type.__name__=_F
_BackupFileOperStatus_Object=MibTableColumn
backupFileOperStatus=_BackupFileOperStatus_Object((1,3,6,1,4,1,8708,2,5,2,2,1,1,6),_BackupFileOperStatus_Type())
backupFileOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:backupFileOperStatus.setStatus(_B)
_BackupFileRowStatus_Type=RowStatus
_BackupFileRowStatus_Object=MibTableColumn
backupFileRowStatus=_BackupFileRowStatus_Object((1,3,6,1,4,1,8708,2,5,2,2,1,1,7),_BackupFileRowStatus_Type())
backupFileRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:backupFileRowStatus.setStatus(_B)
_BackupFileUrl_Type=DisplayString
_BackupFileUrl_Object=MibTableColumn
backupFileUrl=_BackupFileUrl_Object((1,3,6,1,4,1,8708,2,5,2,2,1,1,8),_BackupFileUrl_Type())
backupFileUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:backupFileUrl.setStatus(_B)
_BackupCommand_ObjectIdentity=ObjectIdentity
backupCommand=_BackupCommand_ObjectIdentity((1,3,6,1,4,1,8708,2,5,2,3))
class _BackupCommandName_Type(DisplayString):defaultValue=OctetString('')
_BackupCommandName_Type.__name__=_K
_BackupCommandName_Object=MibScalar
backupCommandName=_BackupCommandName_Object((1,3,6,1,4,1,8708,2,5,2,3,1),_BackupCommandName_Type())
backupCommandName.setMaxAccess(_E)
if mibBuilder.loadTexts:backupCommandName.setStatus(_B)
class _BackupCommandDescr_Type(DisplayString):defaultValue=OctetString('')
_BackupCommandDescr_Type.__name__=_K
_BackupCommandDescr_Object=MibScalar
backupCommandDescr=_BackupCommandDescr_Object((1,3,6,1,4,1,8708,2,5,2,3,2),_BackupCommandDescr_Type())
backupCommandDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:backupCommandDescr.setStatus(_B)
class _BackupCommandAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_v,1),(_AC,2),('primary',3)))
_BackupCommandAdminStatus_Type.__name__=_F
_BackupCommandAdminStatus_Object=MibScalar
backupCommandAdminStatus=_BackupCommandAdminStatus_Object((1,3,6,1,4,1,8708,2,5,2,3,3),_BackupCommandAdminStatus_Type())
backupCommandAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:backupCommandAdminStatus.setStatus(_B)
class _BackupCommandAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),('saveTofile',2),(_q,3)))
_BackupCommandAction_Type.__name__=_F
_BackupCommandAction_Object=MibScalar
backupCommandAction=_BackupCommandAction_Object((1,3,6,1,4,1,8708,2,5,2,3,4),_BackupCommandAction_Type())
backupCommandAction.setMaxAccess(_E)
if mibBuilder.loadTexts:backupCommandAction.setStatus(_B)
class _BackupCommandResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),('success',2),('failed',3)))
_BackupCommandResult_Type.__name__=_F
_BackupCommandResult_Object=MibScalar
backupCommandResult=_BackupCommandResult_Object((1,3,6,1,4,1,8708,2,5,2,3,5),_BackupCommandResult_Type())
backupCommandResult.setMaxAccess(_C)
if mibBuilder.loadTexts:backupCommandResult.setStatus(_B)
_BackupPersistentFileList_ObjectIdentity=ObjectIdentity
backupPersistentFileList=_BackupPersistentFileList_ObjectIdentity((1,3,6,1,4,1,8708,2,5,2,4))
_BackupPersistentFileTable_Object=MibTable
backupPersistentFileTable=_BackupPersistentFileTable_Object((1,3,6,1,4,1,8708,2,5,2,4,1))
if mibBuilder.loadTexts:backupPersistentFileTable.setStatus(_B)
_BackupPersistentFileEntry_Object=MibTableRow
backupPersistentFileEntry=_BackupPersistentFileEntry_Object((1,3,6,1,4,1,8708,2,5,2,4,1,1))
backupPersistentFileEntry.setIndexNames((0,_A,_w))
if mibBuilder.loadTexts:backupPersistentFileEntry.setStatus(_B)
class _BackupPersistentFileIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BackupPersistentFileIndex_Type.__name__=_M
_BackupPersistentFileIndex_Object=MibTableColumn
backupPersistentFileIndex=_BackupPersistentFileIndex_Object((1,3,6,1,4,1,8708,2,5,2,4,1,1,1),_BackupPersistentFileIndex_Type())
backupPersistentFileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:backupPersistentFileIndex.setStatus(_B)
_BackupPersistentFileName_Type=DisplayString
_BackupPersistentFileName_Object=MibTableColumn
backupPersistentFileName=_BackupPersistentFileName_Object((1,3,6,1,4,1,8708,2,5,2,4,1,1,2),_BackupPersistentFileName_Type())
backupPersistentFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:backupPersistentFileName.setStatus(_B)
_BackupPersistentFileDescr_Type=DisplayString
_BackupPersistentFileDescr_Object=MibTableColumn
backupPersistentFileDescr=_BackupPersistentFileDescr_Object((1,3,6,1,4,1,8708,2,5,2,4,1,1,3),_BackupPersistentFileDescr_Type())
backupPersistentFileDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:backupPersistentFileDescr.setStatus(_B)
_BackupUpload_ObjectIdentity=ObjectIdentity
backupUpload=_BackupUpload_ObjectIdentity((1,3,6,1,4,1,8708,2,5,2,5))
_BackupUploadServerAddr_Type=IpAddress
_BackupUploadServerAddr_Object=MibScalar
backupUploadServerAddr=_BackupUploadServerAddr_Object((1,3,6,1,4,1,8708,2,5,2,5,1),_BackupUploadServerAddr_Type())
backupUploadServerAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:backupUploadServerAddr.setStatus(_B)
class _BackupUploadServerPath_Type(DisplayString):defaultValue=OctetString('/upload')
_BackupUploadServerPath_Type.__name__=_K
_BackupUploadServerPath_Object=MibScalar
backupUploadServerPath=_BackupUploadServerPath_Object((1,3,6,1,4,1,8708,2,5,2,5,2),_BackupUploadServerPath_Type())
backupUploadServerPath.setMaxAccess(_E)
if mibBuilder.loadTexts:backupUploadServerPath.setStatus(_B)
class _BackupUploadTimeHour_Type(Unsigned32):defaultValue=23;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_BackupUploadTimeHour_Type.__name__=_M
_BackupUploadTimeHour_Object=MibScalar
backupUploadTimeHour=_BackupUploadTimeHour_Object((1,3,6,1,4,1,8708,2,5,2,5,3),_BackupUploadTimeHour_Type())
backupUploadTimeHour.setMaxAccess(_E)
if mibBuilder.loadTexts:backupUploadTimeHour.setStatus(_B)
class _BackupUploadAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),('pending',2),('upload',3),(_q,4)))
_BackupUploadAction_Type.__name__=_F
_BackupUploadAction_Object=MibScalar
backupUploadAction=_BackupUploadAction_Object((1,3,6,1,4,1,8708,2,5,2,5,4),_BackupUploadAction_Type())
backupUploadAction.setMaxAccess(_E)
if mibBuilder.loadTexts:backupUploadAction.setStatus(_B)
class _BackupUploadResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),('success',2),('failed',3)))
_BackupUploadResult_Type.__name__=_F
_BackupUploadResult_Object=MibScalar
backupUploadResult=_BackupUploadResult_Object((1,3,6,1,4,1,8708,2,5,2,5,5),_BackupUploadResult_Type())
backupUploadResult.setMaxAccess(_C)
if mibBuilder.loadTexts:backupUploadResult.setStatus(_B)
_BackupUploadLastChangeTime_Type=DateAndTime
_BackupUploadLastChangeTime_Object=MibScalar
backupUploadLastChangeTime=_BackupUploadLastChangeTime_Object((1,3,6,1,4,1,8708,2,5,2,5,6),_BackupUploadLastChangeTime_Type())
backupUploadLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:backupUploadLastChangeTime.setStatus(_B)
_BackupUploadFailure_Type=FaultStatus
_BackupUploadFailure_Object=MibScalar
backupUploadFailure=_BackupUploadFailure_Object((1,3,6,1,4,1,8708,2,5,2,5,7),_BackupUploadFailure_Type())
backupUploadFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:backupUploadFailure.setStatus(_B)
_BackupUploadNextTime_Type=DateAndTime
_BackupUploadNextTime_Object=MibScalar
backupUploadNextTime=_BackupUploadNextTime_Object((1,3,6,1,4,1,8708,2,5,2,5,8),_BackupUploadNextTime_Type())
backupUploadNextTime.setMaxAccess(_C)
if mibBuilder.loadTexts:backupUploadNextTime.setStatus(_B)
_BackupUploadInstallUploadFile_Type=CommandString
_BackupUploadInstallUploadFile_Object=MibScalar
backupUploadInstallUploadFile=_BackupUploadInstallUploadFile_Object((1,3,6,1,4,1,8708,2,5,2,5,9),_BackupUploadInstallUploadFile_Type())
backupUploadInstallUploadFile.setMaxAccess(_E)
if mibBuilder.loadTexts:backupUploadInstallUploadFile.setStatus(_B)
class _BackupUploadStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),('pending',2),(_q,3)))
_BackupUploadStatus_Type.__name__=_F
_BackupUploadStatus_Object=MibScalar
backupUploadStatus=_BackupUploadStatus_Object((1,3,6,1,4,1,8708,2,5,2,5,10),_BackupUploadStatus_Type())
backupUploadStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:backupUploadStatus.setStatus(_B)
_BackupUploadUploadNow_Type=CommandString
_BackupUploadUploadNow_Object=MibScalar
backupUploadUploadNow=_BackupUploadUploadNow_Object((1,3,6,1,4,1,8708,2,5,2,5,11),_BackupUploadUploadNow_Type())
backupUploadUploadNow.setMaxAccess(_E)
if mibBuilder.loadTexts:backupUploadUploadNow.setStatus(_B)
class _BackupUploadLocalFile_Type(DisplayString):defaultValue=OctetString('')
_BackupUploadLocalFile_Type.__name__=_K
_BackupUploadLocalFile_Object=MibScalar
backupUploadLocalFile=_BackupUploadLocalFile_Object((1,3,6,1,4,1,8708,2,5,2,5,12),_BackupUploadLocalFile_Type())
backupUploadLocalFile.setMaxAccess(_C)
if mibBuilder.loadTexts:backupUploadLocalFile.setStatus(_B)
_BackupSftpUpload_ObjectIdentity=ObjectIdentity
backupSftpUpload=_BackupSftpUpload_ObjectIdentity((1,3,6,1,4,1,8708,2,5,2,6))
class _BackupSftpUploadBackupEntityAvailability_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('available',1),('availableOutdated',2),('notAvailable',3)))
_BackupSftpUploadBackupEntityAvailability_Type.__name__=_F
_BackupSftpUploadBackupEntityAvailability_Object=MibScalar
backupSftpUploadBackupEntityAvailability=_BackupSftpUploadBackupEntityAvailability_Object((1,3,6,1,4,1,8708,2,5,2,6,1),_BackupSftpUploadBackupEntityAvailability_Type())
backupSftpUploadBackupEntityAvailability.setMaxAccess(_C)
if mibBuilder.loadTexts:backupSftpUploadBackupEntityAvailability.setStatus(_B)
_BackupSftpUploadBackupEntityCompressionTimestamp_Type=DateAndTime
_BackupSftpUploadBackupEntityCompressionTimestamp_Object=MibScalar
backupSftpUploadBackupEntityCompressionTimestamp=_BackupSftpUploadBackupEntityCompressionTimestamp_Object((1,3,6,1,4,1,8708,2,5,2,6,2),_BackupSftpUploadBackupEntityCompressionTimestamp_Type())
backupSftpUploadBackupEntityCompressionTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:backupSftpUploadBackupEntityCompressionTimestamp.setStatus(_B)
class _BackupSftpUploadBackupEntityCrc_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BackupSftpUploadBackupEntityCrc_Type.__name__=_M
_BackupSftpUploadBackupEntityCrc_Object=MibScalar
backupSftpUploadBackupEntityCrc=_BackupSftpUploadBackupEntityCrc_Object((1,3,6,1,4,1,8708,2,5,2,6,3),_BackupSftpUploadBackupEntityCrc_Type())
backupSftpUploadBackupEntityCrc.setMaxAccess(_C)
if mibBuilder.loadTexts:backupSftpUploadBackupEntityCrc.setStatus(_B)
class _BackupSftpUploadRestoreEntityAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ready',1),(_q,2),('restoreNow',3)))
_BackupSftpUploadRestoreEntityAction_Type.__name__=_F
_BackupSftpUploadRestoreEntityAction_Object=MibScalar
backupSftpUploadRestoreEntityAction=_BackupSftpUploadRestoreEntityAction_Object((1,3,6,1,4,1,8708,2,5,2,6,5),_BackupSftpUploadRestoreEntityAction_Type())
backupSftpUploadRestoreEntityAction.setMaxAccess(_E)
if mibBuilder.loadTexts:backupSftpUploadRestoreEntityAction.setStatus(_B)
_BackupSftpUploadBackupEntityFilePath_Type=DisplayString
_BackupSftpUploadBackupEntityFilePath_Object=MibScalar
backupSftpUploadBackupEntityFilePath=_BackupSftpUploadBackupEntityFilePath_Object((1,3,6,1,4,1,8708,2,5,2,6,6),_BackupSftpUploadBackupEntityFilePath_Type())
backupSftpUploadBackupEntityFilePath.setMaxAccess(_C)
if mibBuilder.loadTexts:backupSftpUploadBackupEntityFilePath.setStatus(_B)
class _BackupSftpUploadRestoreEntityFilePath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_BackupSftpUploadRestoreEntityFilePath_Type.__name__=_K
_BackupSftpUploadRestoreEntityFilePath_Object=MibScalar
backupSftpUploadRestoreEntityFilePath=_BackupSftpUploadRestoreEntityFilePath_Object((1,3,6,1,4,1,8708,2,5,2,6,7),_BackupSftpUploadRestoreEntityFilePath_Type())
backupSftpUploadRestoreEntityFilePath.setMaxAccess(_E)
if mibBuilder.loadTexts:backupSftpUploadRestoreEntityFilePath.setStatus(_B)
class _BackupSftpUploadRestoreEntityRestoreNow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('restore',2)))
_BackupSftpUploadRestoreEntityRestoreNow_Type.__name__=_F
_BackupSftpUploadRestoreEntityRestoreNow_Object=MibScalar
backupSftpUploadRestoreEntityRestoreNow=_BackupSftpUploadRestoreEntityRestoreNow_Object((1,3,6,1,4,1,8708,2,5,2,6,8),_BackupSftpUploadRestoreEntityRestoreNow_Type())
backupSftpUploadRestoreEntityRestoreNow.setMaxAccess(_E)
if mibBuilder.loadTexts:backupSftpUploadRestoreEntityRestoreNow.setStatus(_B)
backupGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,1))
backupGeneralGroup.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:backupGeneralGroup.setStatus(_D)
backupFileGroup=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,2))
backupFileGroup.setObjects(*((_A,_p),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:backupFileGroup.setStatus(_D)
backupCommandGroup=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,3))
backupCommandGroup.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:backupCommandGroup.setStatus(_B)
backupGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,4))
backupGeneralGroupV2.setObjects((_A,_J))
if mibBuilder.loadTexts:backupGeneralGroupV2.setStatus(_D)
backupGeneralGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,5))
backupGeneralGroupV3.setObjects(*((_A,_J),(_A,_L)))
if mibBuilder.loadTexts:backupGeneralGroupV3.setStatus(_D)
backupPersistentFileGroup=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,6))
backupPersistentFileGroup.setObjects(*((_A,_w),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:backupPersistentFileGroup.setStatus(_B)
backupFileGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,7))
backupFileGroupV2.setObjects(*((_A,_p),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_AN)))
if mibBuilder.loadTexts:backupFileGroupV2.setStatus(_B)
backupGeneralGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,8))
backupGeneralGroupV4.setObjects(*((_A,_J),(_A,_L),(_A,_N)))
if mibBuilder.loadTexts:backupGeneralGroupV4.setStatus(_D)
backupGeneralGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,9))
backupGeneralGroupV5.setObjects(*((_A,_J),(_A,_L),(_A,_N),(_A,_Q),(_A,_R),(_A,_V),(_A,_O),(_A,_P),(_A,_S)))
if mibBuilder.loadTexts:backupGeneralGroupV5.setStatus(_D)
backupUploadGroup=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,10))
backupUploadGroup.setObjects(*((_A,_W),(_A,_r),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_s)))
if mibBuilder.loadTexts:backupUploadGroup.setStatus(_D)
backupGeneralGroupV6=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,11))
backupGeneralGroupV6.setObjects(*((_A,_J),(_A,_L),(_A,_N),(_A,_Q),(_A,_R),(_A,_V),(_A,_O),(_A,_P),(_A,_S),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:backupGeneralGroupV6.setStatus(_D)
backupUploadGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,12))
backupUploadGroupV2.setObjects(*((_A,_W),(_A,_r),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_s)))
if mibBuilder.loadTexts:backupUploadGroupV2.setStatus(_B)
backupUploadGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,13))
backupUploadGroupV3.setObjects(*((_A,_W),(_A,_r),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_s),(_A,_AO),(_A,_AP),(_A,_A3)))
if mibBuilder.loadTexts:backupUploadGroupV3.setStatus(_B)
backupGeneralGroupV7=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,14))
backupGeneralGroupV7.setObjects(*((_A,_J),(_A,_L),(_A,_N),(_A,_Q),(_A,_R),(_A,_V),(_A,_O),(_A,_P),(_A,_S),(_A,_d),(_A,_e),(_A,_f),(_A,_t)))
if mibBuilder.loadTexts:backupGeneralGroupV7.setStatus(_D)
backupGeneralGroupV8=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,15))
backupGeneralGroupV8.setObjects(*((_A,_J),(_A,_L),(_A,_N),(_A,_Q),(_A,_R),(_A,_V),(_A,_O),(_A,_P),(_A,_S),(_A,_d),(_A,_e),(_A,_f),(_A,_t),(_A,_A4)))
if mibBuilder.loadTexts:backupGeneralGroupV8.setStatus(_D)
backupSftpUploadGroup=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,16))
backupSftpUploadGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:backupSftpUploadGroup.setStatus(_D)
backupGeneralGroupV9=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,17))
backupGeneralGroupV9.setObjects(*((_A,_J),(_A,_L),(_A,_N),(_A,_Q),(_A,_R),(_A,_O),(_A,_P),(_A,_S),(_A,_d),(_A,_e),(_A,_f),(_A,_t),(_A,_A4)))
if mibBuilder.loadTexts:backupGeneralGroupV9.setStatus(_B)
backupSftpUploadGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,1,18))
backupSftpUploadGroupV2.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_A5)))
if mibBuilder.loadTexts:backupSftpUploadGroupV2.setStatus(_B)
backupGeneralMinimalGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,3,1))
backupGeneralMinimalGroupV1.setObjects(*((_A,_J),(_A,_L),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:backupGeneralMinimalGroupV1.setStatus(_B)
backupUploadMinimalGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,3,2))
backupUploadMinimalGroupV1.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_A3)))
if mibBuilder.loadTexts:backupUploadMinimalGroupV1.setStatus(_B)
backupSftpUploadMinimalGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,3,3))
backupSftpUploadMinimalGroupV1.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:backupSftpUploadMinimalGroupV1.setStatus(_D)
backupSftpUploadMinimalGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,5,1,3,4))
backupSftpUploadMinimalGroupV2.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_A5)))
if mibBuilder.loadTexts:backupSftpUploadMinimalGroupV2.setStatus(_B)
lumBackupBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,2,1))
lumBackupBasicComplV1.setObjects(*((_A,_AQ),(_A,_m),(_A,_G)))
if mibBuilder.loadTexts:lumBackupBasicComplV1.setStatus(_D)
lumBackupBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,2,2))
lumBackupBasicComplV2.setObjects(*((_A,_AR),(_A,_m)))
if mibBuilder.loadTexts:lumBackupBasicComplV2.setStatus(_D)
lumBackupBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,2,3))
lumBackupBasicComplV3.setObjects(*((_A,_u),(_A,_m),(_A,_G)))
if mibBuilder.loadTexts:lumBackupBasicComplV3.setStatus(_D)
lumBackupBasicComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,2,4))
lumBackupBasicComplV4.setObjects(*((_A,_u),(_A,_m),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:lumBackupBasicComplV4.setStatus(_D)
lumBackupBasicComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,2,5))
lumBackupBasicComplV5.setObjects(*((_A,_u),(_A,_I),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:lumBackupBasicComplV5.setStatus(_D)
lumBackupBasicComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,2,6))
lumBackupBasicComplV6.setObjects(*((_A,_AS),(_A,_I),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:lumBackupBasicComplV6.setStatus(_D)
lumBackupBasicComplV7=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,2,7))
lumBackupBasicComplV7.setObjects(*((_A,_A6),(_A,_I),(_A,_G),(_A,_H),(_A,_A7)))
if mibBuilder.loadTexts:lumBackupBasicComplV7.setStatus(_D)
lumBackupBasicComplV8=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,2,8))
lumBackupBasicComplV8.setObjects(*((_A,_A6),(_A,_I),(_A,_G),(_A,_H),(_A,_A7)))
if mibBuilder.loadTexts:lumBackupBasicComplV8.setStatus(_D)
lumBackupBasicComplV9=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,2,9))
lumBackupBasicComplV9.setObjects(*((_A,_A8),(_A,_I),(_A,_G),(_A,_H),(_A,_AT)))
if mibBuilder.loadTexts:lumBackupBasicComplV9.setStatus(_D)
lumBackupBasicComplV10=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,2,10))
lumBackupBasicComplV10.setObjects(*((_A,_A8),(_A,_I),(_A,_G),(_A,_H),(_A,_T)))
if mibBuilder.loadTexts:lumBackupBasicComplV10.setStatus(_D)
lumBackupBasicComplV11=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,2,11))
lumBackupBasicComplV11.setObjects(*((_A,_AU),(_A,_I),(_A,_G),(_A,_H),(_A,_T)))
if mibBuilder.loadTexts:lumBackupBasicComplV11.setStatus(_D)
lumBackupBasicComplV12=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,2,12))
lumBackupBasicComplV12.setObjects(*((_A,_AV),(_A,_I),(_A,_G),(_A,_H),(_A,_T),(_A,_AW)))
if mibBuilder.loadTexts:lumBackupBasicComplV12.setStatus(_D)
lumBackupBasicComplV13=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,2,13))
lumBackupBasicComplV13.setObjects(*((_A,_A9),(_A,_I),(_A,_G),(_A,_H),(_A,_T),(_A,_AA)))
if mibBuilder.loadTexts:lumBackupBasicComplV13.setStatus(_D)
lumBackupBasicComplV14=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,2,14))
lumBackupBasicComplV14.setObjects(*((_A,_A9),(_A,_I),(_A,_G),(_A,_H),(_A,_T),(_A,_AA)))
if mibBuilder.loadTexts:lumBackupBasicComplV14.setStatus(_B)
lumBackupMinimalComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,4,1))
lumBackupMinimalComplV1.setObjects(*((_A,_n),(_A,_o)))
if mibBuilder.loadTexts:lumBackupMinimalComplV1.setStatus(_D)
lumBackupMinimalComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,4,2))
lumBackupMinimalComplV2.setObjects(*((_A,_n),(_A,_o),(_A,_AX)))
if mibBuilder.loadTexts:lumBackupMinimalComplV2.setStatus(_D)
lumBackupMinimalComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,4,3))
lumBackupMinimalComplV3.setObjects(*((_A,_n),(_A,_o),(_A,_AB)))
if mibBuilder.loadTexts:lumBackupMinimalComplV3.setStatus(_D)
lumBackupMinimalComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,5,1,4,4))
lumBackupMinimalComplV4.setObjects(*((_A,_n),(_A,_o),(_A,_AB)))
if mibBuilder.loadTexts:lumBackupMinimalComplV4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumBackupMIBModule':lumBackupMIBModule,'lumBackupConfs':lumBackupConfs,'lumBackupGroups':lumBackupGroups,_AQ:backupGeneralGroup,_m:backupFileGroup,_G:backupCommandGroup,_AR:backupGeneralGroupV2,_u:backupGeneralGroupV3,_H:backupPersistentFileGroup,_I:backupFileGroupV2,_AS:backupGeneralGroupV4,_A6:backupGeneralGroupV5,_A7:backupUploadGroup,_A8:backupGeneralGroupV6,_AT:backupUploadGroupV2,_T:backupUploadGroupV3,_AU:backupGeneralGroupV7,_AV:backupGeneralGroupV8,_AW:backupSftpUploadGroup,_A9:backupGeneralGroupV9,_AA:backupSftpUploadGroupV2,'lumBackupCompl':lumBackupCompl,'lumBackupBasicComplV1':lumBackupBasicComplV1,'lumBackupBasicComplV2':lumBackupBasicComplV2,'lumBackupBasicComplV3':lumBackupBasicComplV3,'lumBackupBasicComplV4':lumBackupBasicComplV4,'lumBackupBasicComplV5':lumBackupBasicComplV5,'lumBackupBasicComplV6':lumBackupBasicComplV6,'lumBackupBasicComplV7':lumBackupBasicComplV7,'lumBackupBasicComplV8':lumBackupBasicComplV8,'lumBackupBasicComplV9':lumBackupBasicComplV9,'lumBackupBasicComplV10':lumBackupBasicComplV10,'lumBackupBasicComplV11':lumBackupBasicComplV11,'lumBackupBasicComplV12':lumBackupBasicComplV12,'lumBackupBasicComplV13':lumBackupBasicComplV13,'lumBackupBasicComplV14':lumBackupBasicComplV14,'lumBackupMinimalGroups':lumBackupMinimalGroups,_n:backupGeneralMinimalGroupV1,_o:backupUploadMinimalGroupV1,_AX:backupSftpUploadMinimalGroupV1,_AB:backupSftpUploadMinimalGroupV2,'lumBackupMinimalCompl':lumBackupMinimalCompl,'lumBackupMinimalComplV1':lumBackupMinimalComplV1,'lumBackupMinimalComplV2':lumBackupMinimalComplV2,'lumBackupMinimalComplV3':lumBackupMinimalComplV3,'lumBackupMinimalComplV4':lumBackupMinimalComplV4,'lumBackupMIBObjects':lumBackupMIBObjects,'backupGeneral':backupGeneral,_AD:backupGeneralTestAndIncr,_AE:backupGeneralMibSpecVersion,_AF:backupGeneralMibImplVersion,_J:backupGeneralLastChangeTime,_L:backupGeneralConfigLastChangeTime,_N:backupGeneralUnsavedChanges,_Q:backupGeneralFileTableSize,_R:backupGeneralPersistentFileTableSize,_V:backupGeneralInstallConfigFile,_O:backupGeneralGlobalStateLastChangeTime,_P:backupGeneralGlobalConfigLastChangeTime,_S:backupGeneralPrimaryFileName,_d:backupGeneralWarnForUnsaved,_e:backupGeneralWarnUnsavedDelay,_f:backupGeneralUnsavedChangesAlarm,_t:backupGeneralSavedConfigurationGenerationId,_A4:backupGeneralBackupScheme,'backupFileList':backupFileList,'backupFileTable':backupFileTable,'backupFileEntry':backupFileEntry,_p:backupFileIndex,_x:backupFileName,_y:backupFileDescr,_z:backupFileLastChangeTime,_A0:backupFileAdminStatus,_A1:backupFileOperStatus,_A2:backupFileRowStatus,_AN:backupFileUrl,'backupCommand':backupCommand,_AG:backupCommandName,_AH:backupCommandDescr,_AI:backupCommandAdminStatus,_AJ:backupCommandAction,_AK:backupCommandResult,'backupPersistentFileList':backupPersistentFileList,'backupPersistentFileTable':backupPersistentFileTable,'backupPersistentFileEntry':backupPersistentFileEntry,_w:backupPersistentFileIndex,_AL:backupPersistentFileName,_AM:backupPersistentFileDescr,'backupUpload':backupUpload,_W:backupUploadServerAddr,_r:backupUploadServerPath,_X:backupUploadTimeHour,_Y:backupUploadAction,_Z:backupUploadResult,_a:backupUploadLastChangeTime,_b:backupUploadFailure,_c:backupUploadNextTime,_s:backupUploadInstallUploadFile,_AP:backupUploadStatus,_AO:backupUploadUploadNow,_A3:backupUploadLocalFile,'backupSftpUpload':backupSftpUpload,_g:backupSftpUploadBackupEntityAvailability,_h:backupSftpUploadBackupEntityCompressionTimestamp,_i:backupSftpUploadBackupEntityCrc,_j:backupSftpUploadRestoreEntityAction,_k:backupSftpUploadBackupEntityFilePath,_l:backupSftpUploadRestoreEntityFilePath,_A5:backupSftpUploadRestoreEntityRestoreNow})