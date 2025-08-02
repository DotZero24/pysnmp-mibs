_k='zxAnDataBackuptrapsGroup'
_j='zxAnDataBackupStatusGroup'
_i='zxAnDataManualBackupConfGroup'
_h='zxAnDataAutoBackupConfGroup'
_g='zxAnDataBackupFinished'
_f='zxAnDataBackupSuccessFiles'
_e='zxAnDataBackupTotalFiles'
_d='zxAnDataBackupCurrFileProgress'
_c='zxAnDataBackupCurrFileSize'
_b='zxAnDataBackupCurrFileName'
_a='zxAnDataManualBackupAction'
_Z='zxAnDataAutoBackupMaxHoldOffTime'
_Y='zxAnDataAutoBackupHoldOffTime'
_X='zxAnDataAutoBackupInterval'
_W='zxAnDataAutoBackupStartTime'
_V='zxAnDataAutoBackupEnable'
_U='zxAnDataBackupType'
_T='manualBackupSoftware'
_S='manualBackupLog'
_R='manualBackupConfiguration'
_Q='zxAnDataManualBackupType'
_P='backupConfigurationWhenChanged'
_O='periodBackupSoftware'
_N='periodBackupLog'
_M='periodBackupConfiguration'
_L='zxAnDataAutoBackupType'
_K='DisplayString'
_J='zxAnDataBackupFailedReason'
_I='zxAnDataBackupStatus'
_H='zxAnDataBackupCurrStartTime'
_G='hours'
_F='not-accessible'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='ZTE-AN-DATA-BACKUP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_K,'PhysAddress','TextualConvention')
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnDataBackupMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,18))
if mibBuilder.loadTexts:zxAnDataBackupMib.setRevisions(('2011-05-26 00:00',))
_ZxAnDataBackupObjects_ObjectIdentity=ObjectIdentity
zxAnDataBackupObjects=_ZxAnDataBackupObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,18,2))
_ZxAnDataAutoBackupConfTable_Object=MibTable
zxAnDataAutoBackupConfTable=_ZxAnDataAutoBackupConfTable_Object((1,3,6,1,4,1,3902,1015,18,2,5))
if mibBuilder.loadTexts:zxAnDataAutoBackupConfTable.setStatus(_A)
_ZxAnDataAutoBackupConfEntry_Object=MibTableRow
zxAnDataAutoBackupConfEntry=_ZxAnDataAutoBackupConfEntry_Object((1,3,6,1,4,1,3902,1015,18,2,5,1))
zxAnDataAutoBackupConfEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:zxAnDataAutoBackupConfEntry.setStatus(_A)
class _ZxAnDataAutoBackupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,5,31)));namedValues=NamedValues(*((_M,1),(_N,3),(_O,5),(_P,31)))
_ZxAnDataAutoBackupType_Type.__name__=_C
_ZxAnDataAutoBackupType_Object=MibTableColumn
zxAnDataAutoBackupType=_ZxAnDataAutoBackupType_Object((1,3,6,1,4,1,3902,1015,18,2,5,1,1),_ZxAnDataAutoBackupType_Type())
zxAnDataAutoBackupType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDataAutoBackupType.setStatus(_A)
class _ZxAnDataAutoBackupEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ZxAnDataAutoBackupEnable_Type.__name__=_C
_ZxAnDataAutoBackupEnable_Object=MibTableColumn
zxAnDataAutoBackupEnable=_ZxAnDataAutoBackupEnable_Object((1,3,6,1,4,1,3902,1015,18,2,5,1,2),_ZxAnDataAutoBackupEnable_Type())
zxAnDataAutoBackupEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDataAutoBackupEnable.setStatus(_A)
_ZxAnDataAutoBackupStartTime_Type=DateAndTime
_ZxAnDataAutoBackupStartTime_Object=MibTableColumn
zxAnDataAutoBackupStartTime=_ZxAnDataAutoBackupStartTime_Object((1,3,6,1,4,1,3902,1015,18,2,5,1,3),_ZxAnDataAutoBackupStartTime_Type())
zxAnDataAutoBackupStartTime.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDataAutoBackupStartTime.setStatus(_A)
class _ZxAnDataAutoBackupInterval_Type(Integer32):defaultValue=24;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8760))
_ZxAnDataAutoBackupInterval_Type.__name__=_C
_ZxAnDataAutoBackupInterval_Object=MibTableColumn
zxAnDataAutoBackupInterval=_ZxAnDataAutoBackupInterval_Object((1,3,6,1,4,1,3902,1015,18,2,5,1,4),_ZxAnDataAutoBackupInterval_Type())
zxAnDataAutoBackupInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDataAutoBackupInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnDataAutoBackupInterval.setUnits(_G)
class _ZxAnDataAutoBackupHoldOffTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8760))
_ZxAnDataAutoBackupHoldOffTime_Type.__name__=_C
_ZxAnDataAutoBackupHoldOffTime_Object=MibTableColumn
zxAnDataAutoBackupHoldOffTime=_ZxAnDataAutoBackupHoldOffTime_Object((1,3,6,1,4,1,3902,1015,18,2,5,1,5),_ZxAnDataAutoBackupHoldOffTime_Type())
zxAnDataAutoBackupHoldOffTime.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDataAutoBackupHoldOffTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnDataAutoBackupHoldOffTime.setUnits(_G)
class _ZxAnDataAutoBackupMaxHoldOffTime_Type(Integer32):defaultValue=24;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8760))
_ZxAnDataAutoBackupMaxHoldOffTime_Type.__name__=_C
_ZxAnDataAutoBackupMaxHoldOffTime_Object=MibTableColumn
zxAnDataAutoBackupMaxHoldOffTime=_ZxAnDataAutoBackupMaxHoldOffTime_Object((1,3,6,1,4,1,3902,1015,18,2,5,1,6),_ZxAnDataAutoBackupMaxHoldOffTime_Type())
zxAnDataAutoBackupMaxHoldOffTime.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDataAutoBackupMaxHoldOffTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnDataAutoBackupMaxHoldOffTime.setUnits(_G)
_ZxAnDataManualBackupConfTable_Object=MibTable
zxAnDataManualBackupConfTable=_ZxAnDataManualBackupConfTable_Object((1,3,6,1,4,1,3902,1015,18,2,6))
if mibBuilder.loadTexts:zxAnDataManualBackupConfTable.setStatus(_A)
_ZxAnDataManualBackupConfEntry_Object=MibTableRow
zxAnDataManualBackupConfEntry=_ZxAnDataManualBackupConfEntry_Object((1,3,6,1,4,1,3902,1015,18,2,6,1))
zxAnDataManualBackupConfEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:zxAnDataManualBackupConfEntry.setStatus(_A)
class _ZxAnDataManualBackupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4,6)));namedValues=NamedValues(*((_R,2),(_S,4),(_T,6)))
_ZxAnDataManualBackupType_Type.__name__=_C
_ZxAnDataManualBackupType_Object=MibTableColumn
zxAnDataManualBackupType=_ZxAnDataManualBackupType_Object((1,3,6,1,4,1,3902,1015,18,2,6,1,1),_ZxAnDataManualBackupType_Type())
zxAnDataManualBackupType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDataManualBackupType.setStatus(_A)
class _ZxAnDataManualBackupAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('start',1))
_ZxAnDataManualBackupAction_Type.__name__=_C
_ZxAnDataManualBackupAction_Object=MibTableColumn
zxAnDataManualBackupAction=_ZxAnDataManualBackupAction_Object((1,3,6,1,4,1,3902,1015,18,2,6,1,2),_ZxAnDataManualBackupAction_Type())
zxAnDataManualBackupAction.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDataManualBackupAction.setStatus(_A)
_ZxAnDataBackupStatusTable_Object=MibTable
zxAnDataBackupStatusTable=_ZxAnDataBackupStatusTable_Object((1,3,6,1,4,1,3902,1015,18,2,7))
if mibBuilder.loadTexts:zxAnDataBackupStatusTable.setStatus(_A)
_ZxAnDataBackupStatusEntry_Object=MibTableRow
zxAnDataBackupStatusEntry=_ZxAnDataBackupStatusEntry_Object((1,3,6,1,4,1,3902,1015,18,2,7,1))
zxAnDataBackupStatusEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:zxAnDataBackupStatusEntry.setStatus(_A)
class _ZxAnDataBackupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,31)));namedValues=NamedValues(*((_M,1),(_R,2),(_N,3),(_S,4),(_O,5),(_T,6),(_P,31)))
_ZxAnDataBackupType_Type.__name__=_C
_ZxAnDataBackupType_Object=MibTableColumn
zxAnDataBackupType=_ZxAnDataBackupType_Object((1,3,6,1,4,1,3902,1015,18,2,7,1,1),_ZxAnDataBackupType_Type())
zxAnDataBackupType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDataBackupType.setStatus(_A)
_ZxAnDataBackupCurrStartTime_Type=DateAndTime
_ZxAnDataBackupCurrStartTime_Object=MibTableColumn
zxAnDataBackupCurrStartTime=_ZxAnDataBackupCurrStartTime_Object((1,3,6,1,4,1,3902,1015,18,2,7,1,2),_ZxAnDataBackupCurrStartTime_Type())
zxAnDataBackupCurrStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDataBackupCurrStartTime.setStatus(_A)
class _ZxAnDataBackupCurrFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxAnDataBackupCurrFileName_Type.__name__=_K
_ZxAnDataBackupCurrFileName_Object=MibTableColumn
zxAnDataBackupCurrFileName=_ZxAnDataBackupCurrFileName_Object((1,3,6,1,4,1,3902,1015,18,2,7,1,3),_ZxAnDataBackupCurrFileName_Type())
zxAnDataBackupCurrFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDataBackupCurrFileName.setStatus(_A)
_ZxAnDataBackupCurrFileSize_Type=Integer32
_ZxAnDataBackupCurrFileSize_Object=MibTableColumn
zxAnDataBackupCurrFileSize=_ZxAnDataBackupCurrFileSize_Object((1,3,6,1,4,1,3902,1015,18,2,7,1,4),_ZxAnDataBackupCurrFileSize_Type())
zxAnDataBackupCurrFileSize.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDataBackupCurrFileSize.setStatus(_A)
if mibBuilder.loadTexts:zxAnDataBackupCurrFileSize.setUnits('bytes')
class _ZxAnDataBackupCurrFileProgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnDataBackupCurrFileProgress_Type.__name__=_C
_ZxAnDataBackupCurrFileProgress_Object=MibTableColumn
zxAnDataBackupCurrFileProgress=_ZxAnDataBackupCurrFileProgress_Object((1,3,6,1,4,1,3902,1015,18,2,7,1,5),_ZxAnDataBackupCurrFileProgress_Type())
zxAnDataBackupCurrFileProgress.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDataBackupCurrFileProgress.setStatus(_A)
if mibBuilder.loadTexts:zxAnDataBackupCurrFileProgress.setUnits('percent')
_ZxAnDataBackupTotalFiles_Type=Integer32
_ZxAnDataBackupTotalFiles_Object=MibTableColumn
zxAnDataBackupTotalFiles=_ZxAnDataBackupTotalFiles_Object((1,3,6,1,4,1,3902,1015,18,2,7,1,6),_ZxAnDataBackupTotalFiles_Type())
zxAnDataBackupTotalFiles.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDataBackupTotalFiles.setStatus(_A)
_ZxAnDataBackupSuccessFiles_Type=Integer32
_ZxAnDataBackupSuccessFiles_Object=MibTableColumn
zxAnDataBackupSuccessFiles=_ZxAnDataBackupSuccessFiles_Object((1,3,6,1,4,1,3902,1015,18,2,7,1,7),_ZxAnDataBackupSuccessFiles_Type())
zxAnDataBackupSuccessFiles.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDataBackupSuccessFiles.setStatus(_A)
class _ZxAnDataBackupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notStarted',1),('inProgress',2),('success',3),('failed',4)))
_ZxAnDataBackupStatus_Type.__name__=_C
_ZxAnDataBackupStatus_Object=MibTableColumn
zxAnDataBackupStatus=_ZxAnDataBackupStatus_Object((1,3,6,1,4,1,3902,1015,18,2,7,1,8),_ZxAnDataBackupStatus_Type())
zxAnDataBackupStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDataBackupStatus.setStatus(_A)
class _ZxAnDataBackupFailedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,255)));namedValues=NamedValues(*(('noError',1),('configSaving',2),('backupInProgress',3),('fileServerUnconfigured',4),('fileServerConnectFailed',5),('fileServerLoginFailed',6),('fileServerPathError',7),('fileServerProtocolTypeError',8),('fileAccessError',9),('otherErrors',255)))
_ZxAnDataBackupFailedReason_Type.__name__=_C
_ZxAnDataBackupFailedReason_Object=MibTableColumn
zxAnDataBackupFailedReason=_ZxAnDataBackupFailedReason_Object((1,3,6,1,4,1,3902,1015,18,2,7,1,9),_ZxAnDataBackupFailedReason_Type())
zxAnDataBackupFailedReason.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDataBackupFailedReason.setStatus(_A)
_ZxAnDataBackupNotifications_ObjectIdentity=ObjectIdentity
zxAnDataBackupNotifications=_ZxAnDataBackupNotifications_ObjectIdentity((1,3,6,1,4,1,3902,1015,18,3))
_ZxAnDataBackupConformance_ObjectIdentity=ObjectIdentity
zxAnDataBackupConformance=_ZxAnDataBackupConformance_ObjectIdentity((1,3,6,1,4,1,3902,1015,18,4))
_ZxAnDataBackupCompliances_ObjectIdentity=ObjectIdentity
zxAnDataBackupCompliances=_ZxAnDataBackupCompliances_ObjectIdentity((1,3,6,1,4,1,3902,1015,18,4,1))
_ZxAnDataBackupGroups_ObjectIdentity=ObjectIdentity
zxAnDataBackupGroups=_ZxAnDataBackupGroups_ObjectIdentity((1,3,6,1,4,1,3902,1015,18,4,2))
zxAnDataAutoBackupConfGroup=ObjectGroup((1,3,6,1,4,1,3902,1015,18,4,2,1))
zxAnDataAutoBackupConfGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:zxAnDataAutoBackupConfGroup.setStatus(_A)
zxAnDataManualBackupConfGroup=ObjectGroup((1,3,6,1,4,1,3902,1015,18,4,2,2))
zxAnDataManualBackupConfGroup.setObjects((_B,_a))
if mibBuilder.loadTexts:zxAnDataManualBackupConfGroup.setStatus(_A)
zxAnDataBackupStatusGroup=ObjectGroup((1,3,6,1,4,1,3902,1015,18,4,2,3))
zxAnDataBackupStatusGroup.setObjects(*((_B,_H),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:zxAnDataBackupStatusGroup.setStatus(_A)
zxAnDataBackuptrapsGroup=ObjectGroup((1,3,6,1,4,1,3902,1015,18,4,2,4))
zxAnDataBackuptrapsGroup.setObjects((_B,_g))
if mibBuilder.loadTexts:zxAnDataBackuptrapsGroup.setStatus(_A)
zxAnDataBackupFinished=NotificationType((1,3,6,1,4,1,3902,1015,18,3,1))
zxAnDataBackupFinished.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:zxAnDataBackupFinished.setStatus(_A)
zxAnDataBackupCompliance=ModuleCompliance((1,3,6,1,4,1,3902,1015,18,4,1,1))
zxAnDataBackupCompliance.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:zxAnDataBackupCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zxAnDataBackupMib':zxAnDataBackupMib,'zxAnDataBackupObjects':zxAnDataBackupObjects,'zxAnDataAutoBackupConfTable':zxAnDataAutoBackupConfTable,'zxAnDataAutoBackupConfEntry':zxAnDataAutoBackupConfEntry,_L:zxAnDataAutoBackupType,_V:zxAnDataAutoBackupEnable,_W:zxAnDataAutoBackupStartTime,_X:zxAnDataAutoBackupInterval,_Y:zxAnDataAutoBackupHoldOffTime,_Z:zxAnDataAutoBackupMaxHoldOffTime,'zxAnDataManualBackupConfTable':zxAnDataManualBackupConfTable,'zxAnDataManualBackupConfEntry':zxAnDataManualBackupConfEntry,_Q:zxAnDataManualBackupType,_a:zxAnDataManualBackupAction,'zxAnDataBackupStatusTable':zxAnDataBackupStatusTable,'zxAnDataBackupStatusEntry':zxAnDataBackupStatusEntry,_U:zxAnDataBackupType,_H:zxAnDataBackupCurrStartTime,_b:zxAnDataBackupCurrFileName,_c:zxAnDataBackupCurrFileSize,_d:zxAnDataBackupCurrFileProgress,_e:zxAnDataBackupTotalFiles,_f:zxAnDataBackupSuccessFiles,_I:zxAnDataBackupStatus,_J:zxAnDataBackupFailedReason,'zxAnDataBackupNotifications':zxAnDataBackupNotifications,_g:zxAnDataBackupFinished,'zxAnDataBackupConformance':zxAnDataBackupConformance,'zxAnDataBackupCompliances':zxAnDataBackupCompliances,'zxAnDataBackupCompliance':zxAnDataBackupCompliance,'zxAnDataBackupGroups':zxAnDataBackupGroups,_h:zxAnDataAutoBackupConfGroup,_i:zxAnDataManualBackupConfGroup,_j:zxAnDataBackupStatusGroup,_k:zxAnDataBackuptrapsGroup})