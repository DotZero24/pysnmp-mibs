_c='swPackHandleName'
_b='swPackHandleStatus'
_a='swPackHandleCmd'
_Z='swPackInstallationSlotIdx'
_Y='inProgress'
_X='swPackHandleIdx'
_W='swPackFileIdx'
_V='Unsigned32'
_U='fileSystemValidIndication'
_T='OctetString'
_S='not-accessible'
_R='fileSystemPath'
_Q='fileSystemObjType'
_P='fileSystemObjName'
_O='swPackVersion'
_N='sysName'
_M='SNMPv2-MIB'
_L='alarmEventReason'
_K='alarmEventLogSourceName'
_J='alarmEventLogSeverity'
_I='alarmEventLogDescription'
_H='alarmEventLogDateAndTime'
_G='alarmEventLogAlarmOrEventId'
_F='Integer32'
_E='read-write'
_D='RAD-SwPack-MIB'
_C='read-only'
_B='current'
_A='RAD-GEN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_T,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
agnFiles,alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason,fileSystemObjName,fileSystemObjType,fileSystemPath,fileSystemValidIndication,systemsEvents=mibBuilder.importSymbols(_A,'agnFiles',_G,_H,_I,_J,_K,_L,_P,_Q,_R,_U,'systemsEvents')
FileType,SlotType=mibBuilder.importSymbols('RAD-TC','FileType','SlotType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_M,_N)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_V,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
swPack=ModuleIdentity((1,3,6,1,4,1,164,6,2,67,4))
_SwPackTable_Object=MibTable
swPackTable=_SwPackTable_Object((1,3,6,1,4,1,164,6,2,67,4,1))
if mibBuilder.loadTexts:swPackTable.setStatus(_B)
_SwPackEntry_Object=MibTableRow
swPackEntry=_SwPackEntry_Object((1,3,6,1,4,1,164,6,2,67,4,1,1))
swPackEntry.setIndexNames((0,_A,_R),(0,_A,_Q),(0,_A,_P))
if mibBuilder.loadTexts:swPackEntry.setStatus(_B)
_SwPackVersion_Type=SnmpAdminString
_SwPackVersion_Object=MibTableColumn
swPackVersion=_SwPackVersion_Object((1,3,6,1,4,1,164,6,2,67,4,1,1,1),_SwPackVersion_Type())
swPackVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:swPackVersion.setStatus(_B)
class _SwPackActivityState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('ready',2),('previousActive',3)))
_SwPackActivityState_Type.__name__=_F
_SwPackActivityState_Object=MibTableColumn
swPackActivityState=_SwPackActivityState_Object((1,3,6,1,4,1,164,6,2,67,4,1,1,2),_SwPackActivityState_Type())
swPackActivityState.setMaxAccess(_C)
if mibBuilder.loadTexts:swPackActivityState.setStatus(_B)
_SwPackCreateTime_Type=DateAndTime
_SwPackCreateTime_Object=MibTableColumn
swPackCreateTime=_SwPackCreateTime_Object((1,3,6,1,4,1,164,6,2,67,4,1,1,3),_SwPackCreateTime_Type())
swPackCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swPackCreateTime.setStatus(_B)
_SwPackNumberOfFiles_Type=Unsigned32
_SwPackNumberOfFiles_Object=MibTableColumn
swPackNumberOfFiles=_SwPackNumberOfFiles_Object((1,3,6,1,4,1,164,6,2,67,4,1,1,4),_SwPackNumberOfFiles_Type())
swPackNumberOfFiles.setMaxAccess(_C)
if mibBuilder.loadTexts:swPackNumberOfFiles.setStatus(_B)
_SwPackFileTable_Object=MibTable
swPackFileTable=_SwPackFileTable_Object((1,3,6,1,4,1,164,6,2,67,4,2))
if mibBuilder.loadTexts:swPackFileTable.setStatus(_B)
_SwPackFileEntry_Object=MibTableRow
swPackFileEntry=_SwPackFileEntry_Object((1,3,6,1,4,1,164,6,2,67,4,2,1))
swPackFileEntry.setIndexNames((0,_A,_R),(0,_A,_Q),(0,_A,_P),(0,_D,_W))
if mibBuilder.loadTexts:swPackFileEntry.setStatus(_B)
_SwPackFileIdx_Type=Unsigned32
_SwPackFileIdx_Object=MibTableColumn
swPackFileIdx=_SwPackFileIdx_Object((1,3,6,1,4,1,164,6,2,67,4,2,1,1),_SwPackFileIdx_Type())
swPackFileIdx.setMaxAccess(_S)
if mibBuilder.loadTexts:swPackFileIdx.setStatus(_B)
_SwPackFileType_Type=SnmpAdminString
_SwPackFileType_Object=MibTableColumn
swPackFileType=_SwPackFileType_Object((1,3,6,1,4,1,164,6,2,67,4,2,1,2),_SwPackFileType_Type())
swPackFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:swPackFileType.setStatus(_B)
_SwPackFileName_Type=SnmpAdminString
_SwPackFileName_Object=MibTableColumn
swPackFileName=_SwPackFileName_Object((1,3,6,1,4,1,164,6,2,67,4,2,1,3),_SwPackFileName_Type())
swPackFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:swPackFileName.setStatus(_B)
_SwPackFileVer_Type=SnmpAdminString
_SwPackFileVer_Object=MibTableColumn
swPackFileVer=_SwPackFileVer_Object((1,3,6,1,4,1,164,6,2,67,4,2,1,4),_SwPackFileVer_Type())
swPackFileVer.setMaxAccess(_C)
if mibBuilder.loadTexts:swPackFileVer.setStatus(_B)
_SwPackFileHwVer_Type=SnmpAdminString
_SwPackFileHwVer_Object=MibTableColumn
swPackFileHwVer=_SwPackFileHwVer_Object((1,3,6,1,4,1,164,6,2,67,4,2,1,5),_SwPackFileHwVer_Type())
swPackFileHwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:swPackFileHwVer.setStatus(_B)
_SwPackFileSize_Type=Unsigned32
_SwPackFileSize_Object=MibTableColumn
swPackFileSize=_SwPackFileSize_Object((1,3,6,1,4,1,164,6,2,67,4,2,1,6),_SwPackFileSize_Type())
swPackFileSize.setMaxAccess(_C)
if mibBuilder.loadTexts:swPackFileSize.setStatus(_B)
_SwPackHandleTable_Object=MibTable
swPackHandleTable=_SwPackHandleTable_Object((1,3,6,1,4,1,164,6,2,67,4,3))
if mibBuilder.loadTexts:swPackHandleTable.setStatus(_B)
_SwPackHandleEntry_Object=MibTableRow
swPackHandleEntry=_SwPackHandleEntry_Object((1,3,6,1,4,1,164,6,2,67,4,3,1))
swPackHandleEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:swPackHandleEntry.setStatus(_B)
_SwPackHandleIdx_Type=Unsigned32
_SwPackHandleIdx_Object=MibTableColumn
swPackHandleIdx=_SwPackHandleIdx_Object((1,3,6,1,4,1,164,6,2,67,4,3,1,1),_SwPackHandleIdx_Type())
swPackHandleIdx.setMaxAccess(_S)
if mibBuilder.loadTexts:swPackHandleIdx.setStatus(_B)
_SwPackHandlePath_Type=SnmpAdminString
_SwPackHandlePath_Object=MibTableColumn
swPackHandlePath=_SwPackHandlePath_Object((1,3,6,1,4,1,164,6,2,67,4,3,1,2),_SwPackHandlePath_Type())
swPackHandlePath.setMaxAccess(_E)
if mibBuilder.loadTexts:swPackHandlePath.setStatus(_B)
_SwPackHandleType_Type=FileType
_SwPackHandleType_Object=MibTableColumn
swPackHandleType=_SwPackHandleType_Object((1,3,6,1,4,1,164,6,2,67,4,3,1,3),_SwPackHandleType_Type())
swPackHandleType.setMaxAccess(_E)
if mibBuilder.loadTexts:swPackHandleType.setStatus(_B)
_SwPackHandleName_Type=SnmpAdminString
_SwPackHandleName_Object=MibTableColumn
swPackHandleName=_SwPackHandleName_Object((1,3,6,1,4,1,164,6,2,67,4,3,1,4),_SwPackHandleName_Type())
swPackHandleName.setMaxAccess(_E)
if mibBuilder.loadTexts:swPackHandleName.setStatus(_B)
class _SwPackHandleCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('installIoManualReset',2),('undoInstall',3),('installAndReboot',4),('installAndRebootNoRestore',5)))
_SwPackHandleCmd_Type.__name__=_F
_SwPackHandleCmd_Object=MibTableColumn
swPackHandleCmd=_SwPackHandleCmd_Object((1,3,6,1,4,1,164,6,2,67,4,3,1,5),_SwPackHandleCmd_Type())
swPackHandleCmd.setMaxAccess(_E)
if mibBuilder.loadTexts:swPackHandleCmd.setStatus(_B)
class _SwPackHandleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('idle',1),('endedOk',2),(_Y,3),('slotFailure',4),('mainCardResetFailure',5),('configMigrationError',6),('otherFailure',7),('abortedByUser',8),('swUnconfirmed',9),('swUnconfirmedButUsed',10),('awaitingConfirmation',11),('awaitingIoCardReset',12),('inProgressReset',13),('swInstalledFromBoot',14),('swHwConflict',15)))
_SwPackHandleStatus_Type.__name__=_F
_SwPackHandleStatus_Object=MibTableColumn
swPackHandleStatus=_SwPackHandleStatus_Object((1,3,6,1,4,1,164,6,2,67,4,3,1,6),_SwPackHandleStatus_Type())
swPackHandleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swPackHandleStatus.setStatus(_B)
class _SwPackHandleSlotMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SwPackHandleSlotMap_Type.__name__=_T
_SwPackHandleSlotMap_Object=MibTableColumn
swPackHandleSlotMap=_SwPackHandleSlotMap_Object((1,3,6,1,4,1,164,6,2,67,4,3,1,7),_SwPackHandleSlotMap_Type())
swPackHandleSlotMap.setMaxAccess(_E)
if mibBuilder.loadTexts:swPackHandleSlotMap.setStatus(_B)
class _SwPackHandleConfirmRequestCmd_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('off',2),('on',3)))
_SwPackHandleConfirmRequestCmd_Type.__name__=_F
_SwPackHandleConfirmRequestCmd_Object=MibTableColumn
swPackHandleConfirmRequestCmd=_SwPackHandleConfirmRequestCmd_Object((1,3,6,1,4,1,164,6,2,67,4,3,1,8),_SwPackHandleConfirmRequestCmd_Type())
swPackHandleConfirmRequestCmd.setMaxAccess(_E)
if mibBuilder.loadTexts:swPackHandleConfirmRequestCmd.setStatus(_B)
class _SwPackHandleConfirmCmd_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,5)));namedValues=NamedValues(*(('off',2),('pending',3),('offError',5)))
_SwPackHandleConfirmCmd_Type.__name__=_F
_SwPackHandleConfirmCmd_Object=MibTableColumn
swPackHandleConfirmCmd=_SwPackHandleConfirmCmd_Object((1,3,6,1,4,1,164,6,2,67,4,3,1,9),_SwPackHandleConfirmCmd_Type())
swPackHandleConfirmCmd.setMaxAccess(_E)
if mibBuilder.loadTexts:swPackHandleConfirmCmd.setStatus(_B)
class _SwPackHandleConfirmTimer_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,86400))
_SwPackHandleConfirmTimer_Type.__name__=_V
_SwPackHandleConfirmTimer_Object=MibTableColumn
swPackHandleConfirmTimer=_SwPackHandleConfirmTimer_Object((1,3,6,1,4,1,164,6,2,67,4,3,1,10),_SwPackHandleConfirmTimer_Type())
swPackHandleConfirmTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:swPackHandleConfirmTimer.setStatus(_B)
_SwPackHandleConfirmRemainingTime_Type=Unsigned32
_SwPackHandleConfirmRemainingTime_Object=MibTableColumn
swPackHandleConfirmRemainingTime=_SwPackHandleConfirmRemainingTime_Object((1,3,6,1,4,1,164,6,2,67,4,3,1,11),_SwPackHandleConfirmRemainingTime_Type())
swPackHandleConfirmRemainingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swPackHandleConfirmRemainingTime.setStatus(_B)
_SwPackInstallationTable_Object=MibTable
swPackInstallationTable=_SwPackInstallationTable_Object((1,3,6,1,4,1,164,6,2,67,4,4))
if mibBuilder.loadTexts:swPackInstallationTable.setStatus(_B)
_SwPackInstallationEntry_Object=MibTableRow
swPackInstallationEntry=_SwPackInstallationEntry_Object((1,3,6,1,4,1,164,6,2,67,4,4,1))
swPackInstallationEntry.setIndexNames((0,_D,_Z))
if mibBuilder.loadTexts:swPackInstallationEntry.setStatus(_B)
_SwPackInstallationSlotIdx_Type=SlotType
_SwPackInstallationSlotIdx_Object=MibTableColumn
swPackInstallationSlotIdx=_SwPackInstallationSlotIdx_Object((1,3,6,1,4,1,164,6,2,67,4,4,1,1),_SwPackInstallationSlotIdx_Type())
swPackInstallationSlotIdx.setMaxAccess(_S)
if mibBuilder.loadTexts:swPackInstallationSlotIdx.setStatus(_B)
class _SwPackInstallationSlotStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ready',1),('empty',2),(_Y,3),('manualResetWait',4),('failure',5)))
_SwPackInstallationSlotStatus_Type.__name__=_F
_SwPackInstallationSlotStatus_Object=MibTableColumn
swPackInstallationSlotStatus=_SwPackInstallationSlotStatus_Object((1,3,6,1,4,1,164,6,2,67,4,4,1,2),_SwPackInstallationSlotStatus_Type())
swPackInstallationSlotStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swPackInstallationSlotStatus.setStatus(_B)
systemSoftwareInstallStart=NotificationType((1,3,6,1,4,1,164,6,1,0,42))
systemSoftwareInstallStart.setObjects(*((_A,_K),(_A,_G),(_A,_I),(_A,_J),(_A,_H),(_A,_L),(_M,_N),(_D,_a),(_D,_O)))
if mibBuilder.loadTexts:systemSoftwareInstallStart.setStatus(_B)
systemSoftwareInstallEnd=NotificationType((1,3,6,1,4,1,164,6,1,0,43))
systemSoftwareInstallEnd.setObjects(*((_A,_K),(_A,_G),(_A,_I),(_A,_J),(_A,_H),(_A,_L),(_M,_N),(_A,_U),(_D,_b),(_D,_O)))
if mibBuilder.loadTexts:systemSoftwareInstallEnd.setStatus(_B)
systemSwPackCorrupted=NotificationType((1,3,6,1,4,1,164,6,1,0,61))
systemSwPackCorrupted.setObjects(*((_A,_K),(_A,_G),(_A,_I),(_A,_J),(_A,_H),(_A,_L),(_M,_N),(_D,_c)))
if mibBuilder.loadTexts:systemSwPackCorrupted.setStatus(_B)
systemActiveSoftwareChanged=NotificationType((1,3,6,1,4,1,164,6,1,0,83))
systemActiveSoftwareChanged.setObjects(*((_A,_K),(_A,_G),(_A,_I),(_A,_J),(_A,_H),(_A,_L),(_M,_N),(_D,_O)))
if mibBuilder.loadTexts:systemActiveSoftwareChanged.setStatus(_B)
systemRunningConfigSaved=NotificationType((1,3,6,1,4,1,164,6,1,0,84))
systemRunningConfigSaved.setObjects(*((_A,_K),(_A,_G),(_A,_I),(_A,_J),(_A,_H),(_A,_L),(_M,_N)))
if mibBuilder.loadTexts:systemRunningConfigSaved.setStatus(_B)
mibBuilder.exportSymbols(_D,**{'systemSoftwareInstallStart':systemSoftwareInstallStart,'systemSoftwareInstallEnd':systemSoftwareInstallEnd,'systemSwPackCorrupted':systemSwPackCorrupted,'systemActiveSoftwareChanged':systemActiveSoftwareChanged,'systemRunningConfigSaved':systemRunningConfigSaved,'swPack':swPack,'swPackTable':swPackTable,'swPackEntry':swPackEntry,_O:swPackVersion,'swPackActivityState':swPackActivityState,'swPackCreateTime':swPackCreateTime,'swPackNumberOfFiles':swPackNumberOfFiles,'swPackFileTable':swPackFileTable,'swPackFileEntry':swPackFileEntry,_W:swPackFileIdx,'swPackFileType':swPackFileType,'swPackFileName':swPackFileName,'swPackFileVer':swPackFileVer,'swPackFileHwVer':swPackFileHwVer,'swPackFileSize':swPackFileSize,'swPackHandleTable':swPackHandleTable,'swPackHandleEntry':swPackHandleEntry,_X:swPackHandleIdx,'swPackHandlePath':swPackHandlePath,'swPackHandleType':swPackHandleType,_c:swPackHandleName,_a:swPackHandleCmd,_b:swPackHandleStatus,'swPackHandleSlotMap':swPackHandleSlotMap,'swPackHandleConfirmRequestCmd':swPackHandleConfirmRequestCmd,'swPackHandleConfirmCmd':swPackHandleConfirmCmd,'swPackHandleConfirmTimer':swPackHandleConfirmTimer,'swPackHandleConfirmRemainingTime':swPackHandleConfirmRemainingTime,'swPackInstallationTable':swPackInstallationTable,'swPackInstallationEntry':swPackInstallationEntry,_Z:swPackInstallationSlotIdx,'swPackInstallationSlotStatus':swPackInstallationSlotStatus})