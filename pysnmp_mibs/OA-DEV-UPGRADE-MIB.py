_A6='oaDevUpgrNotificationsGroup'
_A5='oaDevUpgrGroup'
_A4='oaDevConfigAuditCompleted'
_A3='oaDevUpgradeCompletedOk'
_A2='oaDevUpgradeFailed'
_A1='oaDevUpgradeStarted'
_A0='oaAuditMinSchedulePeriod'
_z='oaAuditScheduleError'
_y='oaAuditScheduleStatus'
_x='oaAuditSchedulePeriod'
_w='oaAuditScheduleStart'
_v='oaAuditLastError'
_u='oaAuditValidChecksumTime'
_t='oaAuditValidChecksum'
_s='oaAuditChecksumTime'
_r='oaAuditChecksum'
_q='oaAuditOperStatus'
_p='oaAuditAdminStatus'
_o='oaDevConfigAuditTrapMode'
_n='oaDevConfigAuditSchedulerStatus'
_m='oaDevConfigAuditStartTime'
_l='oaDevConfigAuditPeriodicity'
_k='oaDevUpgrResetDelay'
_j='oaDevUpgrPassword'
_i='oaDevUpgrUsername'
_h='oaDevUpgrAdminStatus'
_g='oaDevUpgrOperStatus'
_f='oaDevUpgrResetDevice'
_e='oaDevUpgrPeriodDateTime'
_d='oaDevUpgrPeriodicity'
_c='oaDevUpgrServerAddress'
_b='oaDevUpgrServerAddressType'
_a='oaDevUpgrGenSupport'
_Z='minutes'
_Y='oaAuditSubType'
_X='operationNotPermitted'
_W='actionCompletedOk'
_V='actionInProcess'
_U='everyDay'
_T='everyWeek'
_S='everyMonth'
_R='InetAddressType'
_Q='InetAddress'
_P='oaDevConfigAuditErrorStatus'
_O='oaDevConfigAuditOperStatus'
_N='oaDevConfigAuditAdminStatus'
_M='oaDevUpgrErrorStatus'
_L='DisplayString'
_K='oaDevUpgrServerAddressText'
_J='oaDevUpgrRemoteFileName'
_I='oaDevUpgrRemoteDir'
_H='oaDevUpgrProtocolApp'
_G='oaDevUpgrType'
_F='none'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='current'
_A='OA-DEV-UPGRADE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_Q,_R)
nbSwitchG1Il,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','nbSwitchG1Il')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_L,'PhysAddress','TextualConvention')
oaDevUpgrade=ModuleIdentity((1,3,6,1,4,1,629,1,50,11,1,20))
if mibBuilder.loadTexts:oaDevUpgrade.setRevisions(('2010-11-25 00:00','2010-04-26 00:00','2009-04-22 00:00','2006-11-08 00:00'))
class PeriodicityDateAndTime(TextualConvention,OctetString):status=_B;displayHint='2d-1d-1d,1d:1d,1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(7,7))
_NbDeviceConfig_ObjectIdentity=ObjectIdentity
nbDeviceConfig=_NbDeviceConfig_ObjectIdentity((1,3,6,1,4,1,629,1,50,11))
_NbDevGen_ObjectIdentity=ObjectIdentity
nbDevGen=_NbDevGen_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1))
_OaDevUpgrNotifications_ObjectIdentity=ObjectIdentity
oaDevUpgrNotifications=_OaDevUpgrNotifications_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,20,0))
class _OaDevUpgrGenSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_OaDevUpgrGenSupport_Type.__name__=_C
_OaDevUpgrGenSupport_Object=MibScalar
oaDevUpgrGenSupport=_OaDevUpgrGenSupport_Object((1,3,6,1,4,1,629,1,50,11,1,20,1),_OaDevUpgrGenSupport_Type())
oaDevUpgrGenSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevUpgrGenSupport.setStatus(_B)
_OaDevUpgrTable_Object=MibTable
oaDevUpgrTable=_OaDevUpgrTable_Object((1,3,6,1,4,1,629,1,50,11,1,20,2))
if mibBuilder.loadTexts:oaDevUpgrTable.setStatus(_B)
_OaDevUpgrEntry_Object=MibTableRow
oaDevUpgrEntry=_OaDevUpgrEntry_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1))
oaDevUpgrEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:oaDevUpgrEntry.setStatus(_B)
class _OaDevUpgrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('upgradeSoftware',1),('getStartupConfig',2),('putStartupConfig',3),('getRunningConfig',4),('putRunningConfig',5),('resetDevice',6),('upgradeFpga',7)))
_OaDevUpgrType_Type.__name__=_C
_OaDevUpgrType_Object=MibTableColumn
oaDevUpgrType=_OaDevUpgrType_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,1),_OaDevUpgrType_Type())
oaDevUpgrType.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:oaDevUpgrType.setStatus(_B)
class _OaDevUpgrProtocolApp_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('tftpClient',2),('ftpClient',3),('scpClient',4),('sftpClient',5),('localFile',6)))
_OaDevUpgrProtocolApp_Type.__name__=_C
_OaDevUpgrProtocolApp_Object=MibTableColumn
oaDevUpgrProtocolApp=_OaDevUpgrProtocolApp_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,2),_OaDevUpgrProtocolApp_Type())
oaDevUpgrProtocolApp.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevUpgrProtocolApp.setStatus(_B)
class _OaDevUpgrServerAddressType_Type(InetAddressType):defaultValue=0
_OaDevUpgrServerAddressType_Type.__name__=_R
_OaDevUpgrServerAddressType_Object=MibTableColumn
oaDevUpgrServerAddressType=_OaDevUpgrServerAddressType_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,3),_OaDevUpgrServerAddressType_Type())
oaDevUpgrServerAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevUpgrServerAddressType.setStatus(_B)
class _OaDevUpgrServerAddress_Type(InetAddress):defaultHexValue=''
_OaDevUpgrServerAddress_Type.__name__=_Q
_OaDevUpgrServerAddress_Object=MibTableColumn
oaDevUpgrServerAddress=_OaDevUpgrServerAddress_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,4),_OaDevUpgrServerAddress_Type())
oaDevUpgrServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevUpgrServerAddress.setStatus(_B)
_OaDevUpgrRemoteDir_Type=DisplayString
_OaDevUpgrRemoteDir_Object=MibTableColumn
oaDevUpgrRemoteDir=_OaDevUpgrRemoteDir_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,5),_OaDevUpgrRemoteDir_Type())
oaDevUpgrRemoteDir.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevUpgrRemoteDir.setStatus(_B)
_OaDevUpgrRemoteFileName_Type=DisplayString
_OaDevUpgrRemoteFileName_Object=MibTableColumn
oaDevUpgrRemoteFileName=_OaDevUpgrRemoteFileName_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,6),_OaDevUpgrRemoteFileName_Type())
oaDevUpgrRemoteFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevUpgrRemoteFileName.setStatus(_B)
class _OaDevUpgrPeriodicity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('once',1),(_S,2),(_T,3),(_U,4)))
_OaDevUpgrPeriodicity_Type.__name__=_C
_OaDevUpgrPeriodicity_Object=MibTableColumn
oaDevUpgrPeriodicity=_OaDevUpgrPeriodicity_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,7),_OaDevUpgrPeriodicity_Type())
oaDevUpgrPeriodicity.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevUpgrPeriodicity.setStatus(_B)
_OaDevUpgrPeriodDateTime_Type=PeriodicityDateAndTime
_OaDevUpgrPeriodDateTime_Object=MibTableColumn
oaDevUpgrPeriodDateTime=_OaDevUpgrPeriodDateTime_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,8),_OaDevUpgrPeriodDateTime_Type())
oaDevUpgrPeriodDateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevUpgrPeriodDateTime.setStatus(_B)
class _OaDevUpgrResetDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('resetDeviceAfterAction',2),('dontResetDeviceAfterAction',3),('resetDeviceWithDelay',4)))
_OaDevUpgrResetDevice_Type.__name__=_C
_OaDevUpgrResetDevice_Object=MibTableColumn
oaDevUpgrResetDevice=_OaDevUpgrResetDevice_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,9),_OaDevUpgrResetDevice_Type())
oaDevUpgrResetDevice.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevUpgrResetDevice.setStatus(_B)
class _OaDevUpgrOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),('waitForSchedule',2),(_V,3),(_W,4),('actionError',5),('actionCanceled',6)))
_OaDevUpgrOperStatus_Type.__name__=_C
_OaDevUpgrOperStatus_Object=MibTableColumn
oaDevUpgrOperStatus=_OaDevUpgrOperStatus_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,10),_OaDevUpgrOperStatus_Type())
oaDevUpgrOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevUpgrOperStatus.setStatus(_B)
class _OaDevUpgrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('startNow',2),('scheduleAction',3),('cancelScheduledAction',4),('removeLocalFile',5)))
_OaDevUpgrAdminStatus_Type.__name__=_C
_OaDevUpgrAdminStatus_Object=MibTableColumn
oaDevUpgrAdminStatus=_OaDevUpgrAdminStatus_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,11),_OaDevUpgrAdminStatus_Type())
oaDevUpgrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevUpgrAdminStatus.setStatus(_B)
_OaDevUpgrUsername_Type=DisplayString
_OaDevUpgrUsername_Object=MibTableColumn
oaDevUpgrUsername=_OaDevUpgrUsername_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,12),_OaDevUpgrUsername_Type())
oaDevUpgrUsername.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevUpgrUsername.setStatus(_B)
_OaDevUpgrPassword_Type=DisplayString
_OaDevUpgrPassword_Object=MibTableColumn
oaDevUpgrPassword=_OaDevUpgrPassword_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,13),_OaDevUpgrPassword_Type())
oaDevUpgrPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevUpgrPassword.setStatus(_B)
_OaDevUpgrServerAddressText_Type=DisplayString
_OaDevUpgrServerAddressText_Object=MibTableColumn
oaDevUpgrServerAddressText=_OaDevUpgrServerAddressText_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,14),_OaDevUpgrServerAddressText_Type())
oaDevUpgrServerAddressText.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevUpgrServerAddressText.setStatus(_B)
class _OaDevUpgrErrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34)));namedValues=NamedValues(*((_F,1),(_X,2),('invalidBootPartition',3),('mergeScriptFailure',4),('mergeScriptMissing',5),('invalidAction',6),('missingParameters',7),('serverUnavailable',8),('cannotGetGateway',9),('cannotGetNetworkMask',10),('invalidGetMethod',11),('fileTransferFailure',12),('invalidSoftwareVersionType',13),('mupgradeScriptMissing',14),('invalidConfigFileType',15),('missingRemoteUserParameter',16),('loginFailure',17),('noSuchFile',18),('cannotSetBootpart',19),('cannotGetBootpart',20),('resetFailure',21),('postResetFailure',22),('wrongUpgrType',23),('emptyFileName',24),('unknownError',25),('startProcessFailed',26),('getPartitionToogleFlagFailed',27),('setPartitionToogleFlagFailed',28),('tooLongCommandError',29),('backupCurrentStartupConfigError',30),('unsupportedAppProtocol',31),('invalidFileFormat',32),('writeRunningConfigFileFailed',33),('downloadFpgaImageFailed',34)))
_OaDevUpgrErrorStatus_Type.__name__=_C
_OaDevUpgrErrorStatus_Object=MibTableColumn
oaDevUpgrErrorStatus=_OaDevUpgrErrorStatus_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,15),_OaDevUpgrErrorStatus_Type())
oaDevUpgrErrorStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevUpgrErrorStatus.setStatus(_B)
class _OaDevUpgrResetDelay_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_OaDevUpgrResetDelay_Type.__name__=_C
_OaDevUpgrResetDelay_Object=MibTableColumn
oaDevUpgrResetDelay=_OaDevUpgrResetDelay_Object((1,3,6,1,4,1,629,1,50,11,1,20,2,1,16),_OaDevUpgrResetDelay_Type())
oaDevUpgrResetDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevUpgrResetDelay.setStatus(_B)
if mibBuilder.loadTexts:oaDevUpgrResetDelay.setUnits('Seconds')
_OaDevConfigAudit_ObjectIdentity=ObjectIdentity
oaDevConfigAudit=_OaDevConfigAudit_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,20,10))
class _OaDevConfigAuditAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('markCurrentConfigAsValid',2),('compareWithValidConfig',3),('scheduleCompare',4),('cancelScheduledCompare',5)))
_OaDevConfigAuditAdminStatus_Type.__name__=_C
_OaDevConfigAuditAdminStatus_Object=MibScalar
oaDevConfigAuditAdminStatus=_OaDevConfigAuditAdminStatus_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,1),_OaDevConfigAuditAdminStatus_Type())
oaDevConfigAuditAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevConfigAuditAdminStatus.setStatus(_B)
class _OaDevConfigAuditOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_V,2),(_W,3),('actionCompletedWithDiff',4),('actionCouldNotCompleted',5)))
_OaDevConfigAuditOperStatus_Type.__name__=_C
_OaDevConfigAuditOperStatus_Object=MibScalar
oaDevConfigAuditOperStatus=_OaDevConfigAuditOperStatus_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,2),_OaDevConfigAuditOperStatus_Type())
oaDevConfigAuditOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevConfigAuditOperStatus.setStatus(_B)
class _OaDevConfigAuditErrorStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_F,1),(_X,2),('operationCanceledByUser',3),('getCurrentConfigFailure',4),('compareFailure',5),('configurationChanged',6),('noValidConfiguration',7),('operationInProcess',8),('anotherSchedulerAlreadyActive',9),('noActiveScheduler',10),('addSchedulerError',11),('deleteSchedulerError',12)))
_OaDevConfigAuditErrorStatus_Type.__name__=_C
_OaDevConfigAuditErrorStatus_Object=MibScalar
oaDevConfigAuditErrorStatus=_OaDevConfigAuditErrorStatus_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,3),_OaDevConfigAuditErrorStatus_Type())
oaDevConfigAuditErrorStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevConfigAuditErrorStatus.setStatus(_B)
class _OaDevConfigAuditPeriodicity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('once',1),(_S,2),(_T,3),(_U,4),('every12Hours',5),('every8Hours',6),('every6Hours',7),('every4Hours',8),('every2Hours',9),('everyHour',10),('every30Minutes',11),('every15Minutes',12)))
_OaDevConfigAuditPeriodicity_Type.__name__=_C
_OaDevConfigAuditPeriodicity_Object=MibScalar
oaDevConfigAuditPeriodicity=_OaDevConfigAuditPeriodicity_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,4),_OaDevConfigAuditPeriodicity_Type())
oaDevConfigAuditPeriodicity.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevConfigAuditPeriodicity.setStatus(_B)
_OaDevConfigAuditStartTime_Type=PeriodicityDateAndTime
_OaDevConfigAuditStartTime_Object=MibScalar
oaDevConfigAuditStartTime=_OaDevConfigAuditStartTime_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,5),_OaDevConfigAuditStartTime_Type())
oaDevConfigAuditStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevConfigAuditStartTime.setStatus(_B)
class _OaDevConfigAuditSchedulerStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notActive',1),('active',2)))
_OaDevConfigAuditSchedulerStatus_Type.__name__=_C
_OaDevConfigAuditSchedulerStatus_Object=MibScalar
oaDevConfigAuditSchedulerStatus=_OaDevConfigAuditSchedulerStatus_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,6),_OaDevConfigAuditSchedulerStatus_Type())
oaDevConfigAuditSchedulerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevConfigAuditSchedulerStatus.setStatus(_B)
class _OaDevConfigAuditTrapMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noSendConfigAuditTrap',1),('sendConfAuditTrapOnChangeOnly',2),('sendConfAuditTrapOnChangeOrDiff',3),('sendConfAuditTrapForEachCompare',4)))
_OaDevConfigAuditTrapMode_Type.__name__=_C
_OaDevConfigAuditTrapMode_Object=MibScalar
oaDevConfigAuditTrapMode=_OaDevConfigAuditTrapMode_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,7),_OaDevConfigAuditTrapMode_Type())
oaDevConfigAuditTrapMode.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevConfigAuditTrapMode.setStatus(_B)
_OaAuditTable_Object=MibTable
oaAuditTable=_OaAuditTable_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,10))
if mibBuilder.loadTexts:oaAuditTable.setStatus(_B)
_OaAuditEntry_Object=MibTableRow
oaAuditEntry=_OaAuditEntry_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,10,1))
oaAuditEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:oaAuditEntry.setStatus(_B)
class _OaAuditSubType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('osEthServTable',1),('osEthServFlowTable',2),('osEthServClassTable',3)))
_OaAuditSubType_Type.__name__=_C
_OaAuditSubType_Object=MibTableColumn
oaAuditSubType=_OaAuditSubType_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,10,1,1),_OaAuditSubType_Type())
oaAuditSubType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:oaAuditSubType.setStatus(_B)
class _OaAuditAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('computeNow',2),('computeValid',3)))
_OaAuditAdminStatus_Type.__name__=_C
_OaAuditAdminStatus_Object=MibTableColumn
oaAuditAdminStatus=_OaAuditAdminStatus_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,10,1,2),_OaAuditAdminStatus_Type())
oaAuditAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:oaAuditAdminStatus.setStatus(_B)
class _OaAuditOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('computeInProcess',2),('computeFinishedOK',3),('computeError',4)))
_OaAuditOperStatus_Type.__name__=_C
_OaAuditOperStatus_Object=MibTableColumn
oaAuditOperStatus=_OaAuditOperStatus_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,10,1,4),_OaAuditOperStatus_Type())
oaAuditOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:oaAuditOperStatus.setStatus(_B)
_OaAuditChecksum_Type=Unsigned32
_OaAuditChecksum_Object=MibTableColumn
oaAuditChecksum=_OaAuditChecksum_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,10,1,5),_OaAuditChecksum_Type())
oaAuditChecksum.setMaxAccess(_E)
if mibBuilder.loadTexts:oaAuditChecksum.setStatus(_B)
_OaAuditChecksumTime_Type=DateAndTime
_OaAuditChecksumTime_Object=MibTableColumn
oaAuditChecksumTime=_OaAuditChecksumTime_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,10,1,6),_OaAuditChecksumTime_Type())
oaAuditChecksumTime.setMaxAccess(_E)
if mibBuilder.loadTexts:oaAuditChecksumTime.setStatus(_B)
_OaAuditValidChecksum_Type=Unsigned32
_OaAuditValidChecksum_Object=MibTableColumn
oaAuditValidChecksum=_OaAuditValidChecksum_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,10,1,7),_OaAuditValidChecksum_Type())
oaAuditValidChecksum.setMaxAccess(_E)
if mibBuilder.loadTexts:oaAuditValidChecksum.setStatus(_B)
_OaAuditValidChecksumTime_Type=DateAndTime
_OaAuditValidChecksumTime_Object=MibTableColumn
oaAuditValidChecksumTime=_OaAuditValidChecksumTime_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,10,1,8),_OaAuditValidChecksumTime_Type())
oaAuditValidChecksumTime.setMaxAccess(_E)
if mibBuilder.loadTexts:oaAuditValidChecksumTime.setStatus(_B)
class _OaAuditLastError_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,160))
_OaAuditLastError_Type.__name__=_L
_OaAuditLastError_Object=MibTableColumn
oaAuditLastError=_OaAuditLastError_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,10,1,100),_OaAuditLastError_Type())
oaAuditLastError.setMaxAccess(_E)
if mibBuilder.loadTexts:oaAuditLastError.setStatus(_B)
_OaAuditScheduleParams_ObjectIdentity=ObjectIdentity
oaAuditScheduleParams=_OaAuditScheduleParams_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,20,10,11))
_OaAuditScheduleStart_Type=PeriodicityDateAndTime
_OaAuditScheduleStart_Object=MibScalar
oaAuditScheduleStart=_OaAuditScheduleStart_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,11,1),_OaAuditScheduleStart_Type())
oaAuditScheduleStart.setMaxAccess(_D)
if mibBuilder.loadTexts:oaAuditScheduleStart.setStatus(_B)
class _OaAuditSchedulePeriod_Type(Integer32):defaultValue=1440;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,44640))
_OaAuditSchedulePeriod_Type.__name__=_C
_OaAuditSchedulePeriod_Object=MibScalar
oaAuditSchedulePeriod=_OaAuditSchedulePeriod_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,11,2),_OaAuditSchedulePeriod_Type())
oaAuditSchedulePeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:oaAuditSchedulePeriod.setStatus(_B)
if mibBuilder.loadTexts:oaAuditSchedulePeriod.setUnits(_Z)
class _OaAuditScheduleStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_OaAuditScheduleStatus_Type.__name__=_C
_OaAuditScheduleStatus_Object=MibScalar
oaAuditScheduleStatus=_OaAuditScheduleStatus_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,11,3),_OaAuditScheduleStatus_Type())
oaAuditScheduleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:oaAuditScheduleStatus.setStatus(_B)
class _OaAuditScheduleError_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,160))
_OaAuditScheduleError_Type.__name__=_L
_OaAuditScheduleError_Object=MibScalar
oaAuditScheduleError=_OaAuditScheduleError_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,11,4),_OaAuditScheduleError_Type())
oaAuditScheduleError.setMaxAccess(_E)
if mibBuilder.loadTexts:oaAuditScheduleError.setStatus(_B)
class _OaAuditMinSchedulePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,44640))
_OaAuditMinSchedulePeriod_Type.__name__=_C
_OaAuditMinSchedulePeriod_Object=MibScalar
oaAuditMinSchedulePeriod=_OaAuditMinSchedulePeriod_Object((1,3,6,1,4,1,629,1,50,11,1,20,10,11,5),_OaAuditMinSchedulePeriod_Type())
oaAuditMinSchedulePeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:oaAuditMinSchedulePeriod.setStatus(_B)
if mibBuilder.loadTexts:oaAuditMinSchedulePeriod.setUnits(_Z)
_OaDevUpgrConformance_ObjectIdentity=ObjectIdentity
oaDevUpgrConformance=_OaDevUpgrConformance_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,20,101))
_OaDevUpgrMIBCompliances_ObjectIdentity=ObjectIdentity
oaDevUpgrMIBCompliances=_OaDevUpgrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,20,101,1))
_OaDevUpgrMIBGroups_ObjectIdentity=ObjectIdentity
oaDevUpgrMIBGroups=_OaDevUpgrMIBGroups_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,20,101,2))
oaDevUpgrGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,11,1,20,101,2,1))
oaDevUpgrGroup.setObjects(*((_A,_a),(_A,_G),(_A,_H),(_A,_b),(_A,_c),(_A,_I),(_A,_J),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_K),(_A,_M),(_A,_k),(_A,_N),(_A,_O),(_A,_P),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:oaDevUpgrGroup.setStatus(_B)
oaDevConfigAuditCompleted=NotificationType((1,3,6,1,4,1,629,1,50,11,1,20,0,94))
oaDevConfigAuditCompleted.setObjects(*((_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:oaDevConfigAuditCompleted.setStatus(_B)
oaDevUpgradeStarted=NotificationType((1,3,6,1,4,1,629,1,50,11,1,20,0,101))
oaDevUpgradeStarted.setObjects(*((_A,_G),(_A,_H),(_A,_K),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:oaDevUpgradeStarted.setStatus(_B)
oaDevUpgradeFailed=NotificationType((1,3,6,1,4,1,629,1,50,11,1,20,0,102))
oaDevUpgradeFailed.setObjects(*((_A,_G),(_A,_H),(_A,_K),(_A,_I),(_A,_J),(_A,_M)))
if mibBuilder.loadTexts:oaDevUpgradeFailed.setStatus(_B)
oaDevUpgradeCompletedOk=NotificationType((1,3,6,1,4,1,629,1,50,11,1,20,0,103))
oaDevUpgradeCompletedOk.setObjects(*((_A,_G),(_A,_H),(_A,_K),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:oaDevUpgradeCompletedOk.setStatus(_B)
oaDevUpgrNotificationsGroup=NotificationGroup((1,3,6,1,4,1,629,1,50,11,1,20,101,2,2))
oaDevUpgrNotificationsGroup.setObjects(*((_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:oaDevUpgrNotificationsGroup.setStatus(_B)
oaDevUpgrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,629,1,50,11,1,20,101,1,1))
oaDevUpgrMIBCompliance.setObjects(*((_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:oaDevUpgrMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'PeriodicityDateAndTime':PeriodicityDateAndTime,'nbDeviceConfig':nbDeviceConfig,'nbDevGen':nbDevGen,'oaDevUpgrade':oaDevUpgrade,'oaDevUpgrNotifications':oaDevUpgrNotifications,_A4:oaDevConfigAuditCompleted,_A1:oaDevUpgradeStarted,_A2:oaDevUpgradeFailed,_A3:oaDevUpgradeCompletedOk,_a:oaDevUpgrGenSupport,'oaDevUpgrTable':oaDevUpgrTable,'oaDevUpgrEntry':oaDevUpgrEntry,_G:oaDevUpgrType,_H:oaDevUpgrProtocolApp,_b:oaDevUpgrServerAddressType,_c:oaDevUpgrServerAddress,_I:oaDevUpgrRemoteDir,_J:oaDevUpgrRemoteFileName,_d:oaDevUpgrPeriodicity,_e:oaDevUpgrPeriodDateTime,_f:oaDevUpgrResetDevice,_g:oaDevUpgrOperStatus,_h:oaDevUpgrAdminStatus,_i:oaDevUpgrUsername,_j:oaDevUpgrPassword,_K:oaDevUpgrServerAddressText,_M:oaDevUpgrErrorStatus,_k:oaDevUpgrResetDelay,'oaDevConfigAudit':oaDevConfigAudit,_N:oaDevConfigAuditAdminStatus,_O:oaDevConfigAuditOperStatus,_P:oaDevConfigAuditErrorStatus,_l:oaDevConfigAuditPeriodicity,_m:oaDevConfigAuditStartTime,_n:oaDevConfigAuditSchedulerStatus,_o:oaDevConfigAuditTrapMode,'oaAuditTable':oaAuditTable,'oaAuditEntry':oaAuditEntry,_Y:oaAuditSubType,_p:oaAuditAdminStatus,_q:oaAuditOperStatus,_r:oaAuditChecksum,_s:oaAuditChecksumTime,_t:oaAuditValidChecksum,_u:oaAuditValidChecksumTime,_v:oaAuditLastError,'oaAuditScheduleParams':oaAuditScheduleParams,_w:oaAuditScheduleStart,_x:oaAuditSchedulePeriod,_y:oaAuditScheduleStatus,_z:oaAuditScheduleError,_A0:oaAuditMinSchedulePeriod,'oaDevUpgrConformance':oaDevUpgrConformance,'oaDevUpgrMIBCompliances':oaDevUpgrMIBCompliances,'oaDevUpgrMIBCompliance':oaDevUpgrMIBCompliance,'oaDevUpgrMIBGroups':oaDevUpgrMIBGroups,_A5:oaDevUpgrGroup,_A6:oaDevUpgrNotificationsGroup})