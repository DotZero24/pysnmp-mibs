_Ae='softwareCuRepGroup'
_Ad='softwareExpectedSwGroup'
_Ac='softwareCommandGroupV2'
_Ab='softwareGeneralGroupV2'
_Aa='softwareCommandGroup'
_AZ='softwareGeneralGroup'
_AY='softwareCommandSubrackSlotExpr'
_AX='softwareCuRepSupportedReplacements'
_AW='softwareCuRepSwNotDistributed'
_AV='softwareExpectedSwPresent'
_AU='softwareGeneralSoftwareExpectedSwTableSize'
_AT='softwareSpareConfigure'
_AS='softwareSpareCommentString'
_AR='softwareSpareResult'
_AQ='softwareSpareState'
_AP='softwareSpareBackupFile'
_AO='softwareSpareBackupServer'
_AN='softwareSpareMode'
_AM='softwareSpareMasterAddr'
_AL='softwareSpareBoardMask'
_AK='softwareSpareBoardAddr'
_AJ='softwareLogString'
_AI='softwareLogTransaction'
_AH='softwareLogName'
_AG='softwareVersionStatus'
_AF='softwareVersionVersion'
_AE='softwareVersionCategory'
_AD='softwareVersionSlot'
_AC='softwareVersionSubrack'
_AB='softwareVersionName'
_AA='activating'
_A9='TestAndIncr'
_A8='BoardOrInterfaceAdminStatus'
_A7='softwareCommandGroupV4'
_A6='softwareCuRepSwPackagesMissing'
_A5='softwareCuRepOkConfigure'
_A4='softwareCuRepRebootCu'
_A3='softwareCuRepSystemMode'
_A2='softwareCuRepUnSaved'
_A1='softwareCuRepAdminStatus'
_A0='softwareExpectedSwFileName'
_z='softwareExpectedSwBoardType'
_y='softwareExpectedSwCategory'
_x='softwareExpectedSwName'
_w='softwareCommandEnmRelease'
_v='softwareCommandWarningCount'
_u='softwareCommandLocalFtpDirectory'
_t='softwareGeneralSoftwareLogTableSize'
_s='softwareGeneralSoftwareVersionTableSize'
_r='softwareLogIndex'
_q='none'
_p='softwareVersionIndex'
_o='softwareCuRepGroupV2'
_n='softwareCommandTftpTimeout'
_m='softwareCommandSendTraps'
_l='softwareCommandReleaseAfterOperation'
_k='softwareCommandPassword'
_j='softwareGeneralConfigLastChangeTime'
_i='softwareGeneralLastChangeTime'
_h='softwareExpectedSwIndex'
_g='softwareCommandGroupV3'
_f='softwareCommandClientOperationId'
_e='softwareCommandNewPassword'
_d='softwareCommandProgressMax'
_c='softwareCommandSemaphore'
_b='softwareCommandTestAndIncr'
_a='softwareCommandOperationTimeout'
_Z='softwareCommandOperation'
_Y='softwareCommandForce'
_X='softwareCommandCleanFirst'
_W='softwareCommandIncludeFs'
_V='softwareCommandEnmFile'
_U='softwareCommandServerIp'
_T='DisplayString'
_S='softwareExpectedSwGroupV2'
_R='softwareCommandErrorCount'
_Q='softwareCommandEnmState'
_P='softwareCommandResult'
_O='softwareCommandProgressCounter'
_N='softwareCommandOperationState'
_M='false'
_L='true'
_K='softwareGeneralGroupV3'
_J='softwareSpareGroup'
_I='softwareLogGroup'
_H='softwareVersionGroup'
_G='Unsigned32'
_F='deprecated'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='LUM-SOFTWARE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumSoftwareMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumSoftwareMIB')
BoardOrInterfaceAdminStatus,CommandString,FaultStatus=mibBuilder.importSymbols('LUM-TC',_A8,'CommandString','FaultStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TestAndIncr=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_T,'PhysAddress','TextualConvention',_A9)
lumSoftwareMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,28))
if mibBuilder.loadTexts:lumSoftwareMIBModule.setRevisions(('2018-09-28 00:00','2017-06-15 00:00','2015-04-28 00:00','2013-12-22 00:00','2013-11-12 00:00','2011-12-20 00:00','2010-01-29 00:00','2004-11-22 00:00','2004-06-15 00:00'))
_LumSoftwareConfs_ObjectIdentity=ObjectIdentity
lumSoftwareConfs=_LumSoftwareConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,28,1))
_LumSoftwareGroups_ObjectIdentity=ObjectIdentity
lumSoftwareGroups=_LumSoftwareGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,28,1,1))
_LumSoftwareCompl_ObjectIdentity=ObjectIdentity
lumSoftwareCompl=_LumSoftwareCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,28,1,2))
_LumSoftwareMIBObjects_ObjectIdentity=ObjectIdentity
lumSoftwareMIBObjects=_LumSoftwareMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,28,2))
_SoftwareGeneral_ObjectIdentity=ObjectIdentity
softwareGeneral=_SoftwareGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,28,2,1))
_SoftwareGeneralLastChangeTime_Type=DateAndTime
_SoftwareGeneralLastChangeTime_Object=MibScalar
softwareGeneralLastChangeTime=_SoftwareGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,28,2,1,1),_SoftwareGeneralLastChangeTime_Type())
softwareGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareGeneralLastChangeTime.setStatus(_B)
_SoftwareGeneralConfigLastChangeTime_Type=DateAndTime
_SoftwareGeneralConfigLastChangeTime_Object=MibScalar
softwareGeneralConfigLastChangeTime=_SoftwareGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,28,2,1,2),_SoftwareGeneralConfigLastChangeTime_Type())
softwareGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareGeneralConfigLastChangeTime.setStatus(_B)
_SoftwareGeneralSoftwareVersionTableSize_Type=Unsigned32
_SoftwareGeneralSoftwareVersionTableSize_Object=MibScalar
softwareGeneralSoftwareVersionTableSize=_SoftwareGeneralSoftwareVersionTableSize_Object((1,3,6,1,4,1,8708,2,28,2,1,3),_SoftwareGeneralSoftwareVersionTableSize_Type())
softwareGeneralSoftwareVersionTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareGeneralSoftwareVersionTableSize.setStatus(_B)
_SoftwareGeneralSoftwareLogTableSize_Type=Unsigned32
_SoftwareGeneralSoftwareLogTableSize_Object=MibScalar
softwareGeneralSoftwareLogTableSize=_SoftwareGeneralSoftwareLogTableSize_Object((1,3,6,1,4,1,8708,2,28,2,1,4),_SoftwareGeneralSoftwareLogTableSize_Type())
softwareGeneralSoftwareLogTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareGeneralSoftwareLogTableSize.setStatus(_B)
_SoftwareGeneralSoftwareExpectedSwTableSize_Type=Unsigned32
_SoftwareGeneralSoftwareExpectedSwTableSize_Object=MibScalar
softwareGeneralSoftwareExpectedSwTableSize=_SoftwareGeneralSoftwareExpectedSwTableSize_Object((1,3,6,1,4,1,8708,2,28,2,1,5),_SoftwareGeneralSoftwareExpectedSwTableSize_Type())
softwareGeneralSoftwareExpectedSwTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareGeneralSoftwareExpectedSwTableSize.setStatus(_B)
_SoftwareVersionList_ObjectIdentity=ObjectIdentity
softwareVersionList=_SoftwareVersionList_ObjectIdentity((1,3,6,1,4,1,8708,2,28,2,2))
_SoftwareVersionTable_Object=MibTable
softwareVersionTable=_SoftwareVersionTable_Object((1,3,6,1,4,1,8708,2,28,2,2,1))
if mibBuilder.loadTexts:softwareVersionTable.setStatus(_B)
_SoftwareVersionEntry_Object=MibTableRow
softwareVersionEntry=_SoftwareVersionEntry_Object((1,3,6,1,4,1,8708,2,28,2,2,1,1))
softwareVersionEntry.setIndexNames((0,_A,_p))
if mibBuilder.loadTexts:softwareVersionEntry.setStatus(_B)
class _SoftwareVersionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SoftwareVersionIndex_Type.__name__=_G
_SoftwareVersionIndex_Object=MibTableColumn
softwareVersionIndex=_SoftwareVersionIndex_Object((1,3,6,1,4,1,8708,2,28,2,2,1,1,1),_SoftwareVersionIndex_Type())
softwareVersionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareVersionIndex.setStatus(_B)
_SoftwareVersionName_Type=DisplayString
_SoftwareVersionName_Object=MibTableColumn
softwareVersionName=_SoftwareVersionName_Object((1,3,6,1,4,1,8708,2,28,2,2,1,1,2),_SoftwareVersionName_Type())
softwareVersionName.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareVersionName.setStatus(_B)
_SoftwareVersionSubrack_Type=Unsigned32
_SoftwareVersionSubrack_Object=MibTableColumn
softwareVersionSubrack=_SoftwareVersionSubrack_Object((1,3,6,1,4,1,8708,2,28,2,2,1,1,3),_SoftwareVersionSubrack_Type())
softwareVersionSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareVersionSubrack.setStatus(_B)
_SoftwareVersionSlot_Type=Unsigned32
_SoftwareVersionSlot_Object=MibTableColumn
softwareVersionSlot=_SoftwareVersionSlot_Object((1,3,6,1,4,1,8708,2,28,2,2,1,1,4),_SoftwareVersionSlot_Type())
softwareVersionSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareVersionSlot.setStatus(_B)
class _SoftwareVersionCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('boot',0),('kernel',1),('appl',2),('fs',3)))
_SoftwareVersionCategory_Type.__name__=_E
_SoftwareVersionCategory_Object=MibTableColumn
softwareVersionCategory=_SoftwareVersionCategory_Object((1,3,6,1,4,1,8708,2,28,2,2,1,1,5),_SoftwareVersionCategory_Type())
softwareVersionCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareVersionCategory.setStatus(_B)
_SoftwareVersionVersion_Type=DisplayString
_SoftwareVersionVersion_Object=MibTableColumn
softwareVersionVersion=_SoftwareVersionVersion_Object((1,3,6,1,4,1,8708,2,28,2,2,1,1,6),_SoftwareVersionVersion_Type())
softwareVersionVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareVersionVersion.setStatus(_B)
_SoftwareVersionStatus_Type=Unsigned32
_SoftwareVersionStatus_Object=MibTableColumn
softwareVersionStatus=_SoftwareVersionStatus_Object((1,3,6,1,4,1,8708,2,28,2,2,1,1,7),_SoftwareVersionStatus_Type())
softwareVersionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareVersionStatus.setStatus(_B)
_SoftwareCommand_ObjectIdentity=ObjectIdentity
softwareCommand=_SoftwareCommand_ObjectIdentity((1,3,6,1,4,1,8708,2,28,2,3))
_SoftwareCommandServerIp_Type=IpAddress
_SoftwareCommandServerIp_Object=MibScalar
softwareCommandServerIp=_SoftwareCommandServerIp_Object((1,3,6,1,4,1,8708,2,28,2,3,1),_SoftwareCommandServerIp_Type())
softwareCommandServerIp.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCommandServerIp.setStatus(_B)
class _SoftwareCommandEnmFile_Type(DisplayString):defaultValue=OctetString('')
_SoftwareCommandEnmFile_Type.__name__=_T
_SoftwareCommandEnmFile_Object=MibScalar
softwareCommandEnmFile=_SoftwareCommandEnmFile_Object((1,3,6,1,4,1,8708,2,28,2,3,2),_SoftwareCommandEnmFile_Type())
softwareCommandEnmFile.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCommandEnmFile.setStatus(_B)
class _SoftwareCommandIncludeFs_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SoftwareCommandIncludeFs_Type.__name__=_E
_SoftwareCommandIncludeFs_Object=MibScalar
softwareCommandIncludeFs=_SoftwareCommandIncludeFs_Object((1,3,6,1,4,1,8708,2,28,2,3,3),_SoftwareCommandIncludeFs_Type())
softwareCommandIncludeFs.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCommandIncludeFs.setStatus(_B)
class _SoftwareCommandCleanFirst_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noClean',1),('normalClean',2),('culessClean',3)))
_SoftwareCommandCleanFirst_Type.__name__=_E
_SoftwareCommandCleanFirst_Object=MibScalar
softwareCommandCleanFirst=_SoftwareCommandCleanFirst_Object((1,3,6,1,4,1,8708,2,28,2,3,4),_SoftwareCommandCleanFirst_Type())
softwareCommandCleanFirst.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCommandCleanFirst.setStatus(_B)
class _SoftwareCommandForce_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SoftwareCommandForce_Type.__name__=_E
_SoftwareCommandForce_Object=MibScalar
softwareCommandForce=_SoftwareCommandForce_Object((1,3,6,1,4,1,8708,2,28,2,3,5),_SoftwareCommandForce_Type())
softwareCommandForce.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCommandForce.setStatus(_B)
class _SoftwareCommandOperation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('test',1),('check',2),('install',3),('upgrade',4),('rebootAfter',5),('rebootCu',6),('rebootAll',7),('revert',8),('abort',9),('unlock',10),('clean',11),('forcedUnlock',12),('rebootAllCold',13),('rebootExpr',14),('rebootCold',15),('rebootPendingBoards',16)))
_SoftwareCommandOperation_Type.__name__=_E
_SoftwareCommandOperation_Object=MibScalar
softwareCommandOperation=_SoftwareCommandOperation_Object((1,3,6,1,4,1,8708,2,28,2,3,6),_SoftwareCommandOperation_Type())
softwareCommandOperation.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCommandOperation.setStatus(_B)
class _SoftwareCommandOperationTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_SoftwareCommandOperationTimeout_Type.__name__=_G
_SoftwareCommandOperationTimeout_Object=MibScalar
softwareCommandOperationTimeout=_SoftwareCommandOperationTimeout_Object((1,3,6,1,4,1,8708,2,28,2,3,7),_SoftwareCommandOperationTimeout_Type())
softwareCommandOperationTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCommandOperationTimeout.setStatus(_B)
class _SoftwareCommandTestAndIncr_Type(TestAndIncr):defaultValue=0
_SoftwareCommandTestAndIncr_Type.__name__=_A9
_SoftwareCommandTestAndIncr_Object=MibScalar
softwareCommandTestAndIncr=_SoftwareCommandTestAndIncr_Object((1,3,6,1,4,1,8708,2,28,2,3,8),_SoftwareCommandTestAndIncr_Type())
softwareCommandTestAndIncr.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCommandTestAndIncr.setStatus(_B)
class _SoftwareCommandSemaphore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),('locked',2)))
_SoftwareCommandSemaphore_Type.__name__=_E
_SoftwareCommandSemaphore_Object=MibScalar
softwareCommandSemaphore=_SoftwareCommandSemaphore_Object((1,3,6,1,4,1,8708,2,28,2,3,9),_SoftwareCommandSemaphore_Type())
softwareCommandSemaphore.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareCommandSemaphore.setStatus(_B)
class _SoftwareCommandOperationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('idle',1),('pending',2),('cleaning',3),('checking',4),('downloading',5),('installing',6),('preparing',7),(_AA,8),('installingFs',9),('reverting',10),('rebooting',11)))
_SoftwareCommandOperationState_Type.__name__=_E
_SoftwareCommandOperationState_Object=MibScalar
softwareCommandOperationState=_SoftwareCommandOperationState_Object((1,3,6,1,4,1,8708,2,28,2,3,10),_SoftwareCommandOperationState_Type())
softwareCommandOperationState.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareCommandOperationState.setStatus(_B)
_SoftwareCommandProgressMax_Type=Unsigned32
_SoftwareCommandProgressMax_Object=MibScalar
softwareCommandProgressMax=_SoftwareCommandProgressMax_Object((1,3,6,1,4,1,8708,2,28,2,3,11),_SoftwareCommandProgressMax_Type())
softwareCommandProgressMax.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareCommandProgressMax.setStatus(_B)
class _SoftwareCommandResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_q,1),('success',2),('failed',3)))
_SoftwareCommandResult_Type.__name__=_E
_SoftwareCommandResult_Object=MibScalar
softwareCommandResult=_SoftwareCommandResult_Object((1,3,6,1,4,1,8708,2,28,2,3,12),_SoftwareCommandResult_Type())
softwareCommandResult.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareCommandResult.setStatus(_B)
class _SoftwareCommandEnmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_q,1),('upToDate',2),('rebootNeeded',3),('activateNeeded',4),('upgradeNeeded',5),('done',6),('filesNeeded',7),('upgradeWithoutRebootNeeded',8),('removeBoardNeeded',9)))
_SoftwareCommandEnmState_Type.__name__=_E
_SoftwareCommandEnmState_Object=MibScalar
softwareCommandEnmState=_SoftwareCommandEnmState_Object((1,3,6,1,4,1,8708,2,28,2,3,13),_SoftwareCommandEnmState_Type())
softwareCommandEnmState.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareCommandEnmState.setStatus(_B)
_SoftwareCommandErrorCount_Type=Unsigned32
_SoftwareCommandErrorCount_Object=MibScalar
softwareCommandErrorCount=_SoftwareCommandErrorCount_Object((1,3,6,1,4,1,8708,2,28,2,3,14),_SoftwareCommandErrorCount_Type())
softwareCommandErrorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareCommandErrorCount.setStatus(_B)
_SoftwareCommandProgressCounter_Type=Unsigned32
_SoftwareCommandProgressCounter_Object=MibScalar
softwareCommandProgressCounter=_SoftwareCommandProgressCounter_Object((1,3,6,1,4,1,8708,2,28,2,3,15),_SoftwareCommandProgressCounter_Type())
softwareCommandProgressCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareCommandProgressCounter.setStatus(_B)
class _SoftwareCommandNewPassword_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_SoftwareCommandNewPassword_Type.__name__=_G
_SoftwareCommandNewPassword_Object=MibScalar
softwareCommandNewPassword=_SoftwareCommandNewPassword_Object((1,3,6,1,4,1,8708,2,28,2,3,16),_SoftwareCommandNewPassword_Type())
softwareCommandNewPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCommandNewPassword.setStatus(_B)
class _SoftwareCommandPassword_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_SoftwareCommandPassword_Type.__name__=_G
_SoftwareCommandPassword_Object=MibScalar
softwareCommandPassword=_SoftwareCommandPassword_Object((1,3,6,1,4,1,8708,2,28,2,3,17),_SoftwareCommandPassword_Type())
softwareCommandPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCommandPassword.setStatus(_B)
class _SoftwareCommandReleaseAfterOperation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SoftwareCommandReleaseAfterOperation_Type.__name__=_E
_SoftwareCommandReleaseAfterOperation_Object=MibScalar
softwareCommandReleaseAfterOperation=_SoftwareCommandReleaseAfterOperation_Object((1,3,6,1,4,1,8708,2,28,2,3,18),_SoftwareCommandReleaseAfterOperation_Type())
softwareCommandReleaseAfterOperation.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCommandReleaseAfterOperation.setStatus(_B)
class _SoftwareCommandSendTraps_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SoftwareCommandSendTraps_Type.__name__=_E
_SoftwareCommandSendTraps_Object=MibScalar
softwareCommandSendTraps=_SoftwareCommandSendTraps_Object((1,3,6,1,4,1,8708,2,28,2,3,19),_SoftwareCommandSendTraps_Type())
softwareCommandSendTraps.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCommandSendTraps.setStatus(_B)
class _SoftwareCommandClientOperationId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_SoftwareCommandClientOperationId_Type.__name__=_G
_SoftwareCommandClientOperationId_Object=MibScalar
softwareCommandClientOperationId=_SoftwareCommandClientOperationId_Object((1,3,6,1,4,1,8708,2,28,2,3,20),_SoftwareCommandClientOperationId_Type())
softwareCommandClientOperationId.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCommandClientOperationId.setStatus(_B)
class _SoftwareCommandTftpTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000))
_SoftwareCommandTftpTimeout_Type.__name__=_G
_SoftwareCommandTftpTimeout_Object=MibScalar
softwareCommandTftpTimeout=_SoftwareCommandTftpTimeout_Object((1,3,6,1,4,1,8708,2,28,2,3,21),_SoftwareCommandTftpTimeout_Type())
softwareCommandTftpTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCommandTftpTimeout.setStatus(_B)
class _SoftwareCommandLocalFtpDirectory_Type(DisplayString):defaultValue=OctetString('')
_SoftwareCommandLocalFtpDirectory_Type.__name__=_T
_SoftwareCommandLocalFtpDirectory_Object=MibScalar
softwareCommandLocalFtpDirectory=_SoftwareCommandLocalFtpDirectory_Object((1,3,6,1,4,1,8708,2,28,2,3,22),_SoftwareCommandLocalFtpDirectory_Type())
softwareCommandLocalFtpDirectory.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareCommandLocalFtpDirectory.setStatus(_B)
_SoftwareCommandWarningCount_Type=Unsigned32
_SoftwareCommandWarningCount_Object=MibScalar
softwareCommandWarningCount=_SoftwareCommandWarningCount_Object((1,3,6,1,4,1,8708,2,28,2,3,23),_SoftwareCommandWarningCount_Type())
softwareCommandWarningCount.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareCommandWarningCount.setStatus(_B)
class _SoftwareCommandEnmRelease_Type(DisplayString):defaultValue=OctetString('')
_SoftwareCommandEnmRelease_Type.__name__=_T
_SoftwareCommandEnmRelease_Object=MibScalar
softwareCommandEnmRelease=_SoftwareCommandEnmRelease_Object((1,3,6,1,4,1,8708,2,28,2,3,24),_SoftwareCommandEnmRelease_Type())
softwareCommandEnmRelease.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareCommandEnmRelease.setStatus(_B)
class _SoftwareCommandSubrackSlotExpr_Type(DisplayString):defaultValue=OctetString('')
_SoftwareCommandSubrackSlotExpr_Type.__name__=_T
_SoftwareCommandSubrackSlotExpr_Object=MibScalar
softwareCommandSubrackSlotExpr=_SoftwareCommandSubrackSlotExpr_Object((1,3,6,1,4,1,8708,2,28,2,3,25),_SoftwareCommandSubrackSlotExpr_Type())
softwareCommandSubrackSlotExpr.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCommandSubrackSlotExpr.setStatus(_B)
_SoftwareLogList_ObjectIdentity=ObjectIdentity
softwareLogList=_SoftwareLogList_ObjectIdentity((1,3,6,1,4,1,8708,2,28,2,4))
_SoftwareLogTable_Object=MibTable
softwareLogTable=_SoftwareLogTable_Object((1,3,6,1,4,1,8708,2,28,2,4,1))
if mibBuilder.loadTexts:softwareLogTable.setStatus(_B)
_SoftwareLogEntry_Object=MibTableRow
softwareLogEntry=_SoftwareLogEntry_Object((1,3,6,1,4,1,8708,2,28,2,4,1,1))
softwareLogEntry.setIndexNames((0,_A,_r))
if mibBuilder.loadTexts:softwareLogEntry.setStatus(_B)
class _SoftwareLogIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SoftwareLogIndex_Type.__name__=_G
_SoftwareLogIndex_Object=MibTableColumn
softwareLogIndex=_SoftwareLogIndex_Object((1,3,6,1,4,1,8708,2,28,2,4,1,1,1),_SoftwareLogIndex_Type())
softwareLogIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareLogIndex.setStatus(_B)
_SoftwareLogName_Type=DisplayString
_SoftwareLogName_Object=MibTableColumn
softwareLogName=_SoftwareLogName_Object((1,3,6,1,4,1,8708,2,28,2,4,1,1,2),_SoftwareLogName_Type())
softwareLogName.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareLogName.setStatus(_B)
_SoftwareLogTransaction_Type=Unsigned32
_SoftwareLogTransaction_Object=MibTableColumn
softwareLogTransaction=_SoftwareLogTransaction_Object((1,3,6,1,4,1,8708,2,28,2,4,1,1,3),_SoftwareLogTransaction_Type())
softwareLogTransaction.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareLogTransaction.setStatus(_B)
_SoftwareLogString_Type=DisplayString
_SoftwareLogString_Object=MibTableColumn
softwareLogString=_SoftwareLogString_Object((1,3,6,1,4,1,8708,2,28,2,4,1,1,4),_SoftwareLogString_Type())
softwareLogString.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareLogString.setStatus(_B)
_LumentisSoftwareNotifications_ObjectIdentity=ObjectIdentity
lumentisSoftwareNotifications=_LumentisSoftwareNotifications_ObjectIdentity((1,3,6,1,4,1,8708,2,28,2,5))
_SoftwareNotifyPrefix_ObjectIdentity=ObjectIdentity
softwareNotifyPrefix=_SoftwareNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,8708,2,28,2,5,0))
_SoftwareSpare_ObjectIdentity=ObjectIdentity
softwareSpare=_SoftwareSpare_ObjectIdentity((1,3,6,1,4,1,8708,2,28,2,6))
_SoftwareSpareBoardAddr_Type=IpAddress
_SoftwareSpareBoardAddr_Object=MibScalar
softwareSpareBoardAddr=_SoftwareSpareBoardAddr_Object((1,3,6,1,4,1,8708,2,28,2,6,1),_SoftwareSpareBoardAddr_Type())
softwareSpareBoardAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareSpareBoardAddr.setStatus(_B)
_SoftwareSpareBoardMask_Type=IpAddress
_SoftwareSpareBoardMask_Object=MibScalar
softwareSpareBoardMask=_SoftwareSpareBoardMask_Object((1,3,6,1,4,1,8708,2,28,2,6,2),_SoftwareSpareBoardMask_Type())
softwareSpareBoardMask.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareSpareBoardMask.setStatus(_B)
_SoftwareSpareMasterAddr_Type=IpAddress
_SoftwareSpareMasterAddr_Object=MibScalar
softwareSpareMasterAddr=_SoftwareSpareMasterAddr_Object((1,3,6,1,4,1,8708,2,28,2,6,3),_SoftwareSpareMasterAddr_Type())
softwareSpareMasterAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareSpareMasterAddr.setStatus(_B)
class _SoftwareSpareMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('undef',0),('tu',1),('standalone',2),('slave',3)))
_SoftwareSpareMode_Type.__name__=_E
_SoftwareSpareMode_Object=MibScalar
softwareSpareMode=_SoftwareSpareMode_Object((1,3,6,1,4,1,8708,2,28,2,6,4),_SoftwareSpareMode_Type())
softwareSpareMode.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareSpareMode.setStatus(_B)
_SoftwareSpareBackupServer_Type=IpAddress
_SoftwareSpareBackupServer_Object=MibScalar
softwareSpareBackupServer=_SoftwareSpareBackupServer_Object((1,3,6,1,4,1,8708,2,28,2,6,5),_SoftwareSpareBackupServer_Type())
softwareSpareBackupServer.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareSpareBackupServer.setStatus(_B)
_SoftwareSpareBackupFile_Type=DisplayString
_SoftwareSpareBackupFile_Object=MibScalar
softwareSpareBackupFile=_SoftwareSpareBackupFile_Object((1,3,6,1,4,1,8708,2,28,2,6,6),_SoftwareSpareBackupFile_Type())
softwareSpareBackupFile.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareSpareBackupFile.setStatus(_B)
class _SoftwareSpareState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('undef',0),('waiting',1),('contactingCu',2),('installBoot',3),('installKernel',4),('installAppl',5),('installFs',6),(_AA,7),('clearSparepart',8),('done',9),('publicAddress',10)))
_SoftwareSpareState_Type.__name__=_E
_SoftwareSpareState_Object=MibScalar
softwareSpareState=_SoftwareSpareState_Object((1,3,6,1,4,1,8708,2,28,2,6,7),_SoftwareSpareState_Type())
softwareSpareState.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareSpareState.setStatus(_B)
class _SoftwareSpareResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_q,1),('ok',2),('cuNotFound',3),('autoUpgradeNotSupported',4),('bootNotFound',5),('kernelNotFound',6),('applNotFound',7),('fsNotFound',8),('bootActivateFailed',9),('kernelActivateFailed',10),('applActivateFailed',11),('flashUpdateFailed',12)))
_SoftwareSpareResult_Type.__name__=_E
_SoftwareSpareResult_Object=MibScalar
softwareSpareResult=_SoftwareSpareResult_Object((1,3,6,1,4,1,8708,2,28,2,6,8),_SoftwareSpareResult_Type())
softwareSpareResult.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareSpareResult.setStatus(_B)
_SoftwareSpareCommentString_Type=DisplayString
_SoftwareSpareCommentString_Object=MibScalar
softwareSpareCommentString=_SoftwareSpareCommentString_Object((1,3,6,1,4,1,8708,2,28,2,6,9),_SoftwareSpareCommentString_Type())
softwareSpareCommentString.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareSpareCommentString.setStatus(_B)
_SoftwareSpareConfigure_Type=CommandString
_SoftwareSpareConfigure_Object=MibScalar
softwareSpareConfigure=_SoftwareSpareConfigure_Object((1,3,6,1,4,1,8708,2,28,2,6,10),_SoftwareSpareConfigure_Type())
softwareSpareConfigure.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareSpareConfigure.setStatus(_B)
_SoftwareExpectedSwList_ObjectIdentity=ObjectIdentity
softwareExpectedSwList=_SoftwareExpectedSwList_ObjectIdentity((1,3,6,1,4,1,8708,2,28,2,7))
_SoftwareExpectedSwTable_Object=MibTable
softwareExpectedSwTable=_SoftwareExpectedSwTable_Object((1,3,6,1,4,1,8708,2,28,2,7,1))
if mibBuilder.loadTexts:softwareExpectedSwTable.setStatus(_B)
_SoftwareExpectedSwEntry_Object=MibTableRow
softwareExpectedSwEntry=_SoftwareExpectedSwEntry_Object((1,3,6,1,4,1,8708,2,28,2,7,1,1))
softwareExpectedSwEntry.setIndexNames((0,_A,_h))
if mibBuilder.loadTexts:softwareExpectedSwEntry.setStatus(_B)
class _SoftwareExpectedSwIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SoftwareExpectedSwIndex_Type.__name__=_G
_SoftwareExpectedSwIndex_Object=MibTableColumn
softwareExpectedSwIndex=_SoftwareExpectedSwIndex_Object((1,3,6,1,4,1,8708,2,28,2,7,1,1,1),_SoftwareExpectedSwIndex_Type())
softwareExpectedSwIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareExpectedSwIndex.setStatus(_B)
_SoftwareExpectedSwName_Type=DisplayString
_SoftwareExpectedSwName_Object=MibTableColumn
softwareExpectedSwName=_SoftwareExpectedSwName_Object((1,3,6,1,4,1,8708,2,28,2,7,1,1,2),_SoftwareExpectedSwName_Type())
softwareExpectedSwName.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareExpectedSwName.setStatus(_B)
class _SoftwareExpectedSwCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('boot',0),('kernel',1),('appl',2),('fs',3)))
_SoftwareExpectedSwCategory_Type.__name__=_E
_SoftwareExpectedSwCategory_Object=MibTableColumn
softwareExpectedSwCategory=_SoftwareExpectedSwCategory_Object((1,3,6,1,4,1,8708,2,28,2,7,1,1,3),_SoftwareExpectedSwCategory_Type())
softwareExpectedSwCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareExpectedSwCategory.setStatus(_B)
class _SoftwareExpectedSwBoardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('cu',0),('tu',1),('all',2)))
_SoftwareExpectedSwBoardType_Type.__name__=_E
_SoftwareExpectedSwBoardType_Object=MibTableColumn
softwareExpectedSwBoardType=_SoftwareExpectedSwBoardType_Object((1,3,6,1,4,1,8708,2,28,2,7,1,1,4),_SoftwareExpectedSwBoardType_Type())
softwareExpectedSwBoardType.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareExpectedSwBoardType.setStatus(_B)
_SoftwareExpectedSwFileName_Type=DisplayString
_SoftwareExpectedSwFileName_Object=MibTableColumn
softwareExpectedSwFileName=_SoftwareExpectedSwFileName_Object((1,3,6,1,4,1,8708,2,28,2,7,1,1,5),_SoftwareExpectedSwFileName_Type())
softwareExpectedSwFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareExpectedSwFileName.setStatus(_B)
class _SoftwareExpectedSwPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_SoftwareExpectedSwPresent_Type.__name__=_E
_SoftwareExpectedSwPresent_Object=MibTableColumn
softwareExpectedSwPresent=_SoftwareExpectedSwPresent_Object((1,3,6,1,4,1,8708,2,28,2,7,1,1,6),_SoftwareExpectedSwPresent_Type())
softwareExpectedSwPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareExpectedSwPresent.setStatus(_B)
_SoftwareCuRep_ObjectIdentity=ObjectIdentity
softwareCuRep=_SoftwareCuRep_ObjectIdentity((1,3,6,1,4,1,8708,2,28,2,8))
class _SoftwareCuRepAdminStatus_Type(BoardOrInterfaceAdminStatus):defaultValue=3
_SoftwareCuRepAdminStatus_Type.__name__=_A8
_SoftwareCuRepAdminStatus_Object=MibScalar
softwareCuRepAdminStatus=_SoftwareCuRepAdminStatus_Object((1,3,6,1,4,1,8708,2,28,2,8,1),_SoftwareCuRepAdminStatus_Type())
softwareCuRepAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCuRepAdminStatus.setStatus(_B)
class _SoftwareCuRepUnSaved_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SoftwareCuRepUnSaved_Type.__name__=_E
_SoftwareCuRepUnSaved_Object=MibScalar
softwareCuRepUnSaved=_SoftwareCuRepUnSaved_Object((1,3,6,1,4,1,8708,2,28,2,8,2),_SoftwareCuRepUnSaved_Type())
softwareCuRepUnSaved.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareCuRepUnSaved.setStatus(_B)
class _SoftwareCuRepSystemMode_Type(Unsigned32):defaultValue=1
_SoftwareCuRepSystemMode_Type.__name__=_G
_SoftwareCuRepSystemMode_Object=MibScalar
softwareCuRepSystemMode=_SoftwareCuRepSystemMode_Object((1,3,6,1,4,1,8708,2,28,2,8,3),_SoftwareCuRepSystemMode_Type())
softwareCuRepSystemMode.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareCuRepSystemMode.setStatus(_B)
class _SoftwareCuRepRebootCu_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SoftwareCuRepRebootCu_Type.__name__=_E
_SoftwareCuRepRebootCu_Object=MibScalar
softwareCuRepRebootCu=_SoftwareCuRepRebootCu_Object((1,3,6,1,4,1,8708,2,28,2,8,4),_SoftwareCuRepRebootCu_Type())
softwareCuRepRebootCu.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCuRepRebootCu.setStatus(_B)
_SoftwareCuRepOkConfigure_Type=CommandString
_SoftwareCuRepOkConfigure_Object=MibScalar
softwareCuRepOkConfigure=_SoftwareCuRepOkConfigure_Object((1,3,6,1,4,1,8708,2,28,2,8,5),_SoftwareCuRepOkConfigure_Type())
softwareCuRepOkConfigure.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCuRepOkConfigure.setStatus(_B)
_SoftwareCuRepSwPackagesMissing_Type=FaultStatus
_SoftwareCuRepSwPackagesMissing_Object=MibScalar
softwareCuRepSwPackagesMissing=_SoftwareCuRepSwPackagesMissing_Object((1,3,6,1,4,1,8708,2,28,2,8,6),_SoftwareCuRepSwPackagesMissing_Type())
softwareCuRepSwPackagesMissing.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareCuRepSwPackagesMissing.setStatus(_B)
_SoftwareCuRepSwNotDistributed_Type=FaultStatus
_SoftwareCuRepSwNotDistributed_Object=MibScalar
softwareCuRepSwNotDistributed=_SoftwareCuRepSwNotDistributed_Object((1,3,6,1,4,1,8708,2,28,2,8,7),_SoftwareCuRepSwNotDistributed_Type())
softwareCuRepSwNotDistributed.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareCuRepSwNotDistributed.setStatus(_B)
class _SoftwareCuRepSupportedReplacements_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('all',1),('cuSfp',2),('cuSfpii',3),('cuSfpiii',4)))
_SoftwareCuRepSupportedReplacements_Type.__name__=_E
_SoftwareCuRepSupportedReplacements_Object=MibScalar
softwareCuRepSupportedReplacements=_SoftwareCuRepSupportedReplacements_Object((1,3,6,1,4,1,8708,2,28,2,8,8),_SoftwareCuRepSupportedReplacements_Type())
softwareCuRepSupportedReplacements.setMaxAccess(_D)
if mibBuilder.loadTexts:softwareCuRepSupportedReplacements.setStatus(_B)
softwareGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,28,1,1,1))
softwareGeneralGroup.setObjects(*((_A,_i),(_A,_j)))
if mibBuilder.loadTexts:softwareGeneralGroup.setStatus(_F)
softwareVersionGroup=ObjectGroup((1,3,6,1,4,1,8708,2,28,1,1,2))
softwareVersionGroup.setObjects(*((_A,_p),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:softwareVersionGroup.setStatus(_B)
softwareCommandGroup=ObjectGroup((1,3,6,1,4,1,8708,2,28,1,1,3))
softwareCommandGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:softwareCommandGroup.setStatus(_F)
softwareLogGroup=ObjectGroup((1,3,6,1,4,1,8708,2,28,1,1,4))
softwareLogGroup.setObjects(*((_A,_r),(_A,_AH),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:softwareLogGroup.setStatus(_B)
softwareCommandGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,28,1,1,5))
softwareCommandGroupV2.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_N),(_A,_d),(_A,_P),(_A,_Q),(_A,_R),(_A,_O),(_A,_e),(_A,_k),(_A,_l),(_A,_m),(_A,_f),(_A,_n)))
if mibBuilder.loadTexts:softwareCommandGroupV2.setStatus(_F)
softwareSpareGroup=ObjectGroup((1,3,6,1,4,1,8708,2,28,1,1,6))
softwareSpareGroup.setObjects(*((_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:softwareSpareGroup.setStatus(_B)
softwareGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,28,1,1,7))
softwareGeneralGroupV2.setObjects(*((_A,_i),(_A,_j),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:softwareGeneralGroupV2.setStatus(_F)
softwareGeneralGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,28,1,1,8))
softwareGeneralGroupV3.setObjects(*((_A,_i),(_A,_j),(_A,_s),(_A,_t),(_A,_AU)))
if mibBuilder.loadTexts:softwareGeneralGroupV3.setStatus(_B)
softwareCommandGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,28,1,1,9))
softwareCommandGroupV3.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_N),(_A,_d),(_A,_P),(_A,_Q),(_A,_R),(_A,_O),(_A,_e),(_A,_k),(_A,_l),(_A,_m),(_A,_f),(_A,_n),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:softwareCommandGroupV3.setStatus(_F)
softwareExpectedSwGroup=ObjectGroup((1,3,6,1,4,1,8708,2,28,1,1,10))
softwareExpectedSwGroup.setObjects(*((_A,_h),(_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:softwareExpectedSwGroup.setStatus(_F)
softwareExpectedSwGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,28,1,1,11))
softwareExpectedSwGroupV2.setObjects(*((_A,_h),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_AV)))
if mibBuilder.loadTexts:softwareExpectedSwGroupV2.setStatus(_B)
softwareCuRepGroup=ObjectGroup((1,3,6,1,4,1,8708,2,28,1,1,12))
softwareCuRepGroup.setObjects(*((_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:softwareCuRepGroup.setStatus(_F)
softwareCuRepGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,28,1,1,13))
softwareCuRepGroupV2.setObjects(*((_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:softwareCuRepGroupV2.setStatus(_B)
softwareCommandGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,28,1,1,14))
softwareCommandGroupV4.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_N),(_A,_d),(_A,_P),(_A,_Q),(_A,_R),(_A,_O),(_A,_e),(_A,_k),(_A,_l),(_A,_m),(_A,_f),(_A,_n),(_A,_u),(_A,_v),(_A,_w),(_A,_AY)))
if mibBuilder.loadTexts:softwareCommandGroupV4.setStatus(_B)
softwareResultTrap=NotificationType((1,3,6,1,4,1,8708,2,28,2,5,0,1))
softwareResultTrap.setObjects(*((_A,_N),(_A,_d),(_A,_P),(_A,_Q),(_A,_R),(_A,_O),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:softwareResultTrap.setStatus(_B)
lumSoftwareBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,28,1,2,1))
lumSoftwareBasicComplV1.setObjects(*((_A,_AZ),(_A,_H),(_A,_Aa),(_A,_I)))
if mibBuilder.loadTexts:lumSoftwareBasicComplV1.setStatus(_F)
lumSoftwareBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,28,1,2,2))
lumSoftwareBasicComplV2.setObjects(*((_A,_Ab),(_A,_H),(_A,_Ac),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:lumSoftwareBasicComplV2.setStatus(_F)
lumSoftwareBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,28,1,2,3))
lumSoftwareBasicComplV3.setObjects(*((_A,_K),(_A,_H),(_A,_g),(_A,_I),(_A,_J),(_A,_Ad)))
if mibBuilder.loadTexts:lumSoftwareBasicComplV3.setStatus(_F)
lumSoftwareBasicComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,28,1,2,4))
lumSoftwareBasicComplV4.setObjects(*((_A,_K),(_A,_H),(_A,_g),(_A,_I),(_A,_J),(_A,_S)))
if mibBuilder.loadTexts:lumSoftwareBasicComplV4.setStatus(_F)
lumSoftwareBasicComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,28,1,2,5))
lumSoftwareBasicComplV5.setObjects(*((_A,_K),(_A,_H),(_A,_g),(_A,_I),(_A,_J),(_A,_S),(_A,_Ae)))
if mibBuilder.loadTexts:lumSoftwareBasicComplV5.setStatus(_F)
lumSoftwareBasicComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,28,1,2,6))
lumSoftwareBasicComplV6.setObjects(*((_A,_K),(_A,_H),(_A,_g),(_A,_I),(_A,_J),(_A,_S),(_A,_o)))
if mibBuilder.loadTexts:lumSoftwareBasicComplV6.setStatus(_F)
lumSoftwareBasicComplV7=ModuleCompliance((1,3,6,1,4,1,8708,2,28,1,2,7))
lumSoftwareBasicComplV7.setObjects(*((_A,_K),(_A,_H),(_A,_A7),(_A,_I),(_A,_J),(_A,_S),(_A,_o)))
if mibBuilder.loadTexts:lumSoftwareBasicComplV7.setStatus(_F)
lumSoftwareBasicComplV8=ModuleCompliance((1,3,6,1,4,1,8708,2,28,1,2,8))
lumSoftwareBasicComplV8.setObjects(*((_A,_K),(_A,_H),(_A,_A7),(_A,_I),(_A,_J),(_A,_S),(_A,_o)))
if mibBuilder.loadTexts:lumSoftwareBasicComplV8.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumSoftwareMIBModule':lumSoftwareMIBModule,'lumSoftwareConfs':lumSoftwareConfs,'lumSoftwareGroups':lumSoftwareGroups,_AZ:softwareGeneralGroup,_H:softwareVersionGroup,_Aa:softwareCommandGroup,_I:softwareLogGroup,_Ac:softwareCommandGroupV2,_J:softwareSpareGroup,_Ab:softwareGeneralGroupV2,_K:softwareGeneralGroupV3,_g:softwareCommandGroupV3,_Ad:softwareExpectedSwGroup,_S:softwareExpectedSwGroupV2,_Ae:softwareCuRepGroup,_o:softwareCuRepGroupV2,_A7:softwareCommandGroupV4,'lumSoftwareCompl':lumSoftwareCompl,'lumSoftwareBasicComplV1':lumSoftwareBasicComplV1,'lumSoftwareBasicComplV2':lumSoftwareBasicComplV2,'lumSoftwareBasicComplV3':lumSoftwareBasicComplV3,'lumSoftwareBasicComplV4':lumSoftwareBasicComplV4,'lumSoftwareBasicComplV5':lumSoftwareBasicComplV5,'lumSoftwareBasicComplV6':lumSoftwareBasicComplV6,'lumSoftwareBasicComplV7':lumSoftwareBasicComplV7,'lumSoftwareBasicComplV8':lumSoftwareBasicComplV8,'lumSoftwareMIBObjects':lumSoftwareMIBObjects,'softwareGeneral':softwareGeneral,_i:softwareGeneralLastChangeTime,_j:softwareGeneralConfigLastChangeTime,_s:softwareGeneralSoftwareVersionTableSize,_t:softwareGeneralSoftwareLogTableSize,_AU:softwareGeneralSoftwareExpectedSwTableSize,'softwareVersionList':softwareVersionList,'softwareVersionTable':softwareVersionTable,'softwareVersionEntry':softwareVersionEntry,_p:softwareVersionIndex,_AB:softwareVersionName,_AC:softwareVersionSubrack,_AD:softwareVersionSlot,_AE:softwareVersionCategory,_AF:softwareVersionVersion,_AG:softwareVersionStatus,'softwareCommand':softwareCommand,_U:softwareCommandServerIp,_V:softwareCommandEnmFile,_W:softwareCommandIncludeFs,_X:softwareCommandCleanFirst,_Y:softwareCommandForce,_Z:softwareCommandOperation,_a:softwareCommandOperationTimeout,_b:softwareCommandTestAndIncr,_c:softwareCommandSemaphore,_N:softwareCommandOperationState,_d:softwareCommandProgressMax,_P:softwareCommandResult,_Q:softwareCommandEnmState,_R:softwareCommandErrorCount,_O:softwareCommandProgressCounter,_e:softwareCommandNewPassword,_k:softwareCommandPassword,_l:softwareCommandReleaseAfterOperation,_m:softwareCommandSendTraps,_f:softwareCommandClientOperationId,_n:softwareCommandTftpTimeout,_u:softwareCommandLocalFtpDirectory,_v:softwareCommandWarningCount,_w:softwareCommandEnmRelease,_AY:softwareCommandSubrackSlotExpr,'softwareLogList':softwareLogList,'softwareLogTable':softwareLogTable,'softwareLogEntry':softwareLogEntry,_r:softwareLogIndex,_AH:softwareLogName,_AI:softwareLogTransaction,_AJ:softwareLogString,'lumentisSoftwareNotifications':lumentisSoftwareNotifications,'softwareNotifyPrefix':softwareNotifyPrefix,'softwareResultTrap':softwareResultTrap,'softwareSpare':softwareSpare,_AK:softwareSpareBoardAddr,_AL:softwareSpareBoardMask,_AM:softwareSpareMasterAddr,_AN:softwareSpareMode,_AO:softwareSpareBackupServer,_AP:softwareSpareBackupFile,_AQ:softwareSpareState,_AR:softwareSpareResult,_AS:softwareSpareCommentString,_AT:softwareSpareConfigure,'softwareExpectedSwList':softwareExpectedSwList,'softwareExpectedSwTable':softwareExpectedSwTable,'softwareExpectedSwEntry':softwareExpectedSwEntry,_h:softwareExpectedSwIndex,_x:softwareExpectedSwName,_y:softwareExpectedSwCategory,_z:softwareExpectedSwBoardType,_A0:softwareExpectedSwFileName,_AV:softwareExpectedSwPresent,'softwareCuRep':softwareCuRep,_A1:softwareCuRepAdminStatus,_A2:softwareCuRepUnSaved,_A3:softwareCuRepSystemMode,_A4:softwareCuRepRebootCu,_A5:softwareCuRepOkConfigure,_A6:softwareCuRepSwPackagesMissing,_AW:softwareCuRepSwNotDistributed,_AX:softwareCuRepSupportedReplacements})