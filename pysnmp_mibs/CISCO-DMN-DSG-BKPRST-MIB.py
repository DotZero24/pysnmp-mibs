_E='Integer32'
_D='read-only'
_C='read-write'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','TextualConvention')
ciscoDSGBKPRST=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,3))
if mibBuilder.loadTexts:ciscoDSGBKPRST.setRevisions(('2012-03-26 17:00','2010-08-30 05:00','2010-06-17 06:00','2010-03-22 05:00','2010-02-12 15:00','2009-11-22 15:00'))
_BackupRestoreInfo_ObjectIdentity=ObjectIdentity
backupRestoreInfo=_BackupRestoreInfo_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,3,1))
class _BackupRestoreOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('backup',1),('restore',2),('writeOnly',3)))
_BackupRestoreOperation_Type.__name__=_E
_BackupRestoreOperation_Object=MibScalar
backupRestoreOperation=_BackupRestoreOperation_Object((1,3,6,1,4,1,1429,2,2,5,3,1,1),_BackupRestoreOperation_Type())
backupRestoreOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:backupRestoreOperation.setStatus(_A)
class _BackupRestoreType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standard',1),('extended',2),('full',3)))
_BackupRestoreType_Type.__name__=_E
_BackupRestoreType_Object=MibScalar
backupRestoreType=_BackupRestoreType_Object((1,3,6,1,4,1,1429,2,2,5,3,1,2),_BackupRestoreType_Type())
backupRestoreType.setMaxAccess(_C)
if mibBuilder.loadTexts:backupRestoreType.setStatus(_A)
class _BackupRestoreFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,119))
_BackupRestoreFileName_Type.__name__=_B
_BackupRestoreFileName_Object=MibScalar
backupRestoreFileName=_BackupRestoreFileName_Object((1,3,6,1,4,1,1429,2,2,5,3,1,3),_BackupRestoreFileName_Type())
backupRestoreFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:backupRestoreFileName.setStatus(_A)
_BackupRestoreFtpServerIp_Type=IpAddress
_BackupRestoreFtpServerIp_Object=MibScalar
backupRestoreFtpServerIp=_BackupRestoreFtpServerIp_Object((1,3,6,1,4,1,1429,2,2,5,3,1,4),_BackupRestoreFtpServerIp_Type())
backupRestoreFtpServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:backupRestoreFtpServerIp.setStatus(_A)
class _BackupRestoreFtpUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BackupRestoreFtpUsername_Type.__name__=_B
_BackupRestoreFtpUsername_Object=MibScalar
backupRestoreFtpUsername=_BackupRestoreFtpUsername_Object((1,3,6,1,4,1,1429,2,2,5,3,1,5),_BackupRestoreFtpUsername_Type())
backupRestoreFtpUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:backupRestoreFtpUsername.setStatus(_A)
class _BackupRestoreFtpPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BackupRestoreFtpPassword_Type.__name__=_B
_BackupRestoreFtpPassword_Object=MibScalar
backupRestoreFtpPassword=_BackupRestoreFtpPassword_Object((1,3,6,1,4,1,1429,2,2,5,3,1,6),_BackupRestoreFtpPassword_Type())
backupRestoreFtpPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:backupRestoreFtpPassword.setStatus(_A)
class _BackupRestoreFtpPortno_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BackupRestoreFtpPortno_Type.__name__=_E
_BackupRestoreFtpPortno_Object=MibScalar
backupRestoreFtpPortno=_BackupRestoreFtpPortno_Object((1,3,6,1,4,1,1429,2,2,5,3,1,7),_BackupRestoreFtpPortno_Type())
backupRestoreFtpPortno.setMaxAccess(_C)
if mibBuilder.loadTexts:backupRestoreFtpPortno.setStatus(_A)
class _BackupRestoreLastBackupFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,119))
_BackupRestoreLastBackupFile_Type.__name__=_B
_BackupRestoreLastBackupFile_Object=MibScalar
backupRestoreLastBackupFile=_BackupRestoreLastBackupFile_Object((1,3,6,1,4,1,1429,2,2,5,3,1,8),_BackupRestoreLastBackupFile_Type())
backupRestoreLastBackupFile.setMaxAccess(_D)
if mibBuilder.loadTexts:backupRestoreLastBackupFile.setStatus(_A)
class _BackupRestoreLastBackupTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BackupRestoreLastBackupTime_Type.__name__=_B
_BackupRestoreLastBackupTime_Object=MibScalar
backupRestoreLastBackupTime=_BackupRestoreLastBackupTime_Object((1,3,6,1,4,1,1429,2,2,5,3,1,9),_BackupRestoreLastBackupTime_Type())
backupRestoreLastBackupTime.setMaxAccess(_D)
if mibBuilder.loadTexts:backupRestoreLastBackupTime.setStatus(_A)
class _BackupRestoreLastRestoreFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,119))
_BackupRestoreLastRestoreFile_Type.__name__=_B
_BackupRestoreLastRestoreFile_Object=MibScalar
backupRestoreLastRestoreFile=_BackupRestoreLastRestoreFile_Object((1,3,6,1,4,1,1429,2,2,5,3,1,10),_BackupRestoreLastRestoreFile_Type())
backupRestoreLastRestoreFile.setMaxAccess(_D)
if mibBuilder.loadTexts:backupRestoreLastRestoreFile.setStatus(_A)
class _BackupRestoreLastRestoreTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BackupRestoreLastRestoreTime_Type.__name__=_B
_BackupRestoreLastRestoreTime_Object=MibScalar
backupRestoreLastRestoreTime=_BackupRestoreLastRestoreTime_Object((1,3,6,1,4,1,1429,2,2,5,3,1,11),_BackupRestoreLastRestoreTime_Type())
backupRestoreLastRestoreTime.setMaxAccess(_D)
if mibBuilder.loadTexts:backupRestoreLastRestoreTime.setStatus(_A)
class _BackupRestoreOperationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inprogress',1),('pass',2),('fail',3)))
_BackupRestoreOperationStatus_Type.__name__=_E
_BackupRestoreOperationStatus_Object=MibScalar
backupRestoreOperationStatus=_BackupRestoreOperationStatus_Object((1,3,6,1,4,1,1429,2,2,5,3,1,12),_BackupRestoreOperationStatus_Type())
backupRestoreOperationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:backupRestoreOperationStatus.setStatus(_A)
class _BackupRestoreDetailedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*(('idle',1),('backupProcessing',2),('backupConnecting',3),('backupSendingFile',4),('backupDone',5),('backupFailed',6),('restoreConnecting',7),('restoreWaitingFile',8),('restoreReceivingFile',9),('restoreProcessing',10),('restoreDone',11),('restoreFailed',12),('ftpFileTransferError',13),('restoreFileCorrupted',14),('restoreFileDesignationCodeMismatch',15),('restoreFilePlatformTypeMismatch',16),('restoreFileMissingFileInformation',17),('restoreFileMissingPlatformType',18),('restoreFileMissingDesignation',19),('restoreFileMissingContents',20),('restoreFileMissingRoot',21)))
_BackupRestoreDetailedStatus_Type.__name__=_E
_BackupRestoreDetailedStatus_Object=MibScalar
backupRestoreDetailedStatus=_BackupRestoreDetailedStatus_Object((1,3,6,1,4,1,1429,2,2,5,3,1,13),_BackupRestoreDetailedStatus_Type())
backupRestoreDetailedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:backupRestoreDetailedStatus.setStatus(_A)
class _BackupRestorePercentageComp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BackupRestorePercentageComp_Type.__name__=_B
_BackupRestorePercentageComp_Object=MibScalar
backupRestorePercentageComp=_BackupRestorePercentageComp_Object((1,3,6,1,4,1,1429,2,2,5,3,1,14),_BackupRestorePercentageComp_Type())
backupRestorePercentageComp.setMaxAccess(_D)
if mibBuilder.loadTexts:backupRestorePercentageComp.setStatus(_A)
mibBuilder.exportSymbols('CISCO-DMN-DSG-BKPRST-MIB',**{'ciscoDSGBKPRST':ciscoDSGBKPRST,'backupRestoreInfo':backupRestoreInfo,'backupRestoreOperation':backupRestoreOperation,'backupRestoreType':backupRestoreType,'backupRestoreFileName':backupRestoreFileName,'backupRestoreFtpServerIp':backupRestoreFtpServerIp,'backupRestoreFtpUsername':backupRestoreFtpUsername,'backupRestoreFtpPassword':backupRestoreFtpPassword,'backupRestoreFtpPortno':backupRestoreFtpPortno,'backupRestoreLastBackupFile':backupRestoreLastBackupFile,'backupRestoreLastBackupTime':backupRestoreLastBackupTime,'backupRestoreLastRestoreFile':backupRestoreLastRestoreFile,'backupRestoreLastRestoreTime':backupRestoreLastRestoreTime,'backupRestoreOperationStatus':backupRestoreOperationStatus,'backupRestoreDetailedStatus':backupRestoreDetailedStatus,'backupRestorePercentageComp':backupRestorePercentageComp})