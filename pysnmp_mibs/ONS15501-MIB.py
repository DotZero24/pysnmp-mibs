_AU='ons15501PowerSupplyLevelGroup'
_AT='ons15501PowerSupplyStatusGroup'
_AS='ons15501CoreAttrGroup'
_AR='ons15501SysInfoGroup2'
_AQ='ons15501FinalAttrGroup'
_AP='ons15501SysInfoGroup'
_AO='ons15501GenericNotificationTrap'
_AN='ons15501SysDateAndTime'
_AM='ons15501PowerSupply2Status'
_AL='ons15501PowerSupply1Status'
_AK='ons15501TrapSeverity'
_AJ='ons15501TrapDescription'
_AI='ons15501ActAlarmSeverity'
_AH='ons15501ActAlarmDateAndTime'
_AG='ons15501ActAlarmTimeStamp'
_AF='ons15501ActAlarmPhyIndex'
_AE='ons15501TrapLogEntryDateAndTime'
_AD='ons15501TrapLogEntryTimeStamp'
_AC='ons15501TrapTypeValue'
_AB='ons15501ActAlarmType'
_AA='ons15501TrapLogEntryIndex'
_A9='ons15501FinalNotificationsGroup'
_A8='ons15501TrapDescriptionGroup'
_A7='ons15501ActiveAlarmGroup'
_A6='ons15501TrapLogGroup'
_A5='ons15501GainTrigger'
_A4='ons15501LaserStatus'
_A3='ons15501DevAmbTempTrigger'
_A2='ons15501DevAmbTempMean'
_A1='ons15501DevAmbTemp'
_A0='ons15501PowerSupply2Level'
_z='ons15501PowerSupply1Level'
_y='ons15501OpticalPowerGain'
_x='ons15501ConfigOpticalGain'
_w='ons15501OutputSignalPowerTrigger'
_v='ons15501OutputSignalPowerMean'
_u='ons15501OutputSignalPower'
_t='ons15501OutputOpticalPower'
_s='ons15501InputOpticalPowerTrigger'
_r='ons15501InputOpticalPowerMean'
_q='ons15501InputOpticalPower'
_p='ons15501TrapLogEntrySeverity'
_o='ons15501TrapLogEntryPhyIndex'
_n='ons15501TrapLogEntryDirection'
_m='ons15501TrapLogEntryTrapType'
_l='ons15501LastTrapIndex'
_k='deprecated'
_j='ons15501SysDeviceManagerList'
_i='ons15501ActiveSoftwareVer'
_h='ons15501LastConfigChangeTime'
_g='ons15501OutRemoteAgentIpAddr'
_f='ons15501OutRemotePortName'
_e='ons15501OutRemoteChassisName'
_d='ons15501OutRemoteInfoUpdateTime'
_c='ons15501InRemoteAgentIpAddr'
_b='ons15501InRemotePortName'
_a='ons15501InRemoteChassisName'
_Z='ons15501InRemoteInfoUpdateTime'
_Y='ons15501CLEICode'
_X='ons15501NTPOperationalStatus'
_W='ons15501NTPAdminStatus'
_V='ons15501SecondaryNTP'
_U='ons15501PrimaryNTP'
_T='ons15501SysAlarmStatus'
_S='ons15501SysDevActiveImage'
_R='ons15501SysConfiguredImage'
_Q='ons15501SysSwDownloadStatus'
_P='ons15501SysSwDownload'
_O='ons15501SysDevFlash3Image'
_N='ons15501SysDevFlash2Image'
_M='ons15501SysDevFlash1Image'
_L='not-accessible'
_K='Ons15501TenthCentigrade'
_J='degrees C'
_I='d-1'
_H='dB'
_G='dBm'
_F='Unsigned32'
_E='Ons15501TenthdB'
_D='read-write'
_C='read-only'
_B='current'
_A='ONS15501-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ons15501MIB=ModuleIdentity((1,3,6,1,4,1,1869,11,11))
if mibBuilder.loadTexts:ons15501MIB.setRevisions(('2002-08-29 16:00','2002-03-18 12:30'))
class Ons15501ImageDnLoadStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('notInitiated',1),('inProgress',2),('failedUnknownErr',3),('failedFileNotFound',4),('failedAccessDenied',5),('failedTimedOut',6),('completedSuccessfully',7),('failedInDownload',8),('failedTimeoutInDownload',9),('failedToConnectToServer',10),('failedWhileWritingToFlash',11),('failedIllegalOperation',12),('failedFileExists',13),('failedUnknownTransferId',14),('failedUnknownUser',15)))
class Ons15501AdminStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
class Ons15501NTPStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('disabled',1),('bothServersBad',2),('usingPrimary',3),('usingSecondary',4),('unknown',5)))
class Ons15501TenthVolt(TextualConvention,Integer32):status=_B;displayHint=_I;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000,0))
class Ons15501TenthdB(TextualConvention,Integer32):status=_B;displayHint=_I;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000,500))
class Ons15501TenthCentigrade(TextualConvention,Integer32):status=_B;displayHint=_I;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,1000))
class Ons15501AlarmStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('critical',1),('major',2),('minor',3),('info',4),('noAlarm',5)))
class Ons15501TrapTypeEnumeration(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,32767)));namedValues=NamedValues(*(('unacceptableAmbientTemperature',1),('unacceptableElectricalPower',2),('inputSignalPowerTooLow',3),('unacceptableOutputSignalPower',4),('embeddedControllerCommFailure',5),('softwareUpgradeInitiated',6),('softwareUpgradeFailed',7),('softwareUpgradeCompleted',8),('softwareRebootInitiated',9),('softwareRolledBack',10),('configurationChanged',11),('unacceptableGain',12),('laserPumpBad',13),('eEPROMBad',14),('unknown',32767)))
class Ons15501TrapDirectionEnumeration(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dontCare',1),('asserted',2),('cleared',3)))
_Synchronous_ObjectIdentity=ObjectIdentity
synchronous=_Synchronous_ObjectIdentity((1,3,6,1,4,1,1869))
_SynEmbLx_ObjectIdentity=ObjectIdentity
synEmbLx=_SynEmbLx_ObjectIdentity((1,3,6,1,4,1,1869,11))
_Ons15501Sys_ObjectIdentity=ObjectIdentity
ons15501Sys=_Ons15501Sys_ObjectIdentity((1,3,6,1,4,1,1869,11,11,1))
_Ons15501SysDevFlash1Image_Type=DisplayString
_Ons15501SysDevFlash1Image_Object=MibScalar
ons15501SysDevFlash1Image=_Ons15501SysDevFlash1Image_Object((1,3,6,1,4,1,1869,11,11,1,1),_Ons15501SysDevFlash1Image_Type())
ons15501SysDevFlash1Image.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501SysDevFlash1Image.setStatus(_B)
_Ons15501SysDevFlash2Image_Type=DisplayString
_Ons15501SysDevFlash2Image_Object=MibScalar
ons15501SysDevFlash2Image=_Ons15501SysDevFlash2Image_Object((1,3,6,1,4,1,1869,11,11,1,2),_Ons15501SysDevFlash2Image_Type())
ons15501SysDevFlash2Image.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501SysDevFlash2Image.setStatus(_B)
_Ons15501SysDevFlash3Image_Type=DisplayString
_Ons15501SysDevFlash3Image_Object=MibScalar
ons15501SysDevFlash3Image=_Ons15501SysDevFlash3Image_Object((1,3,6,1,4,1,1869,11,11,1,3),_Ons15501SysDevFlash3Image_Type())
ons15501SysDevFlash3Image.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501SysDevFlash3Image.setStatus(_B)
_Ons15501SysSwDownload_Type=DisplayString
_Ons15501SysSwDownload_Object=MibScalar
ons15501SysSwDownload=_Ons15501SysSwDownload_Object((1,3,6,1,4,1,1869,11,11,1,4),_Ons15501SysSwDownload_Type())
ons15501SysSwDownload.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501SysSwDownload.setStatus(_B)
class _Ons15501SysDevActiveImage_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Ons15501SysDevActiveImage_Type.__name__=_F
_Ons15501SysDevActiveImage_Object=MibScalar
ons15501SysDevActiveImage=_Ons15501SysDevActiveImage_Object((1,3,6,1,4,1,1869,11,11,1,5),_Ons15501SysDevActiveImage_Type())
ons15501SysDevActiveImage.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501SysDevActiveImage.setStatus(_B)
_Ons15501SysDeviceManagerList_Type=DisplayString
_Ons15501SysDeviceManagerList_Object=MibScalar
ons15501SysDeviceManagerList=_Ons15501SysDeviceManagerList_Object((1,3,6,1,4,1,1869,11,11,1,6),_Ons15501SysDeviceManagerList_Type())
ons15501SysDeviceManagerList.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501SysDeviceManagerList.setStatus(_B)
_Ons15501SysSwDownloadStatus_Type=Ons15501ImageDnLoadStatus
_Ons15501SysSwDownloadStatus_Object=MibScalar
ons15501SysSwDownloadStatus=_Ons15501SysSwDownloadStatus_Object((1,3,6,1,4,1,1869,11,11,1,7),_Ons15501SysSwDownloadStatus_Type())
ons15501SysSwDownloadStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501SysSwDownloadStatus.setStatus(_B)
class _Ons15501SysConfiguredImage_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Ons15501SysConfiguredImage_Type.__name__=_F
_Ons15501SysConfiguredImage_Object=MibScalar
ons15501SysConfiguredImage=_Ons15501SysConfiguredImage_Object((1,3,6,1,4,1,1869,11,11,1,8),_Ons15501SysConfiguredImage_Type())
ons15501SysConfiguredImage.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501SysConfiguredImage.setStatus(_B)
_Ons15501CLEICode_Type=DisplayString
_Ons15501CLEICode_Object=MibScalar
ons15501CLEICode=_Ons15501CLEICode_Object((1,3,6,1,4,1,1869,11,11,1,9),_Ons15501CLEICode_Type())
ons15501CLEICode.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501CLEICode.setStatus(_B)
_Ons15501PrimaryNTP_Type=IpAddress
_Ons15501PrimaryNTP_Object=MibScalar
ons15501PrimaryNTP=_Ons15501PrimaryNTP_Object((1,3,6,1,4,1,1869,11,11,1,10),_Ons15501PrimaryNTP_Type())
ons15501PrimaryNTP.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501PrimaryNTP.setStatus(_B)
_Ons15501SecondaryNTP_Type=IpAddress
_Ons15501SecondaryNTP_Object=MibScalar
ons15501SecondaryNTP=_Ons15501SecondaryNTP_Object((1,3,6,1,4,1,1869,11,11,1,11),_Ons15501SecondaryNTP_Type())
ons15501SecondaryNTP.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501SecondaryNTP.setStatus(_B)
_Ons15501NTPAdminStatus_Type=Ons15501AdminStatus
_Ons15501NTPAdminStatus_Object=MibScalar
ons15501NTPAdminStatus=_Ons15501NTPAdminStatus_Object((1,3,6,1,4,1,1869,11,11,1,12),_Ons15501NTPAdminStatus_Type())
ons15501NTPAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501NTPAdminStatus.setStatus(_B)
_Ons15501NTPOperationalStatus_Type=Ons15501NTPStatus
_Ons15501NTPOperationalStatus_Object=MibScalar
ons15501NTPOperationalStatus=_Ons15501NTPOperationalStatus_Object((1,3,6,1,4,1,1869,11,11,1,13),_Ons15501NTPOperationalStatus_Type())
ons15501NTPOperationalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501NTPOperationalStatus.setStatus(_B)
_Ons15501ActiveSoftwareVer_Type=DisplayString
_Ons15501ActiveSoftwareVer_Object=MibScalar
ons15501ActiveSoftwareVer=_Ons15501ActiveSoftwareVer_Object((1,3,6,1,4,1,1869,11,11,1,14),_Ons15501ActiveSoftwareVer_Type())
ons15501ActiveSoftwareVer.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501ActiveSoftwareVer.setStatus(_B)
_Ons15501LastConfigChangeTime_Type=TimeStamp
_Ons15501LastConfigChangeTime_Object=MibScalar
ons15501LastConfigChangeTime=_Ons15501LastConfigChangeTime_Object((1,3,6,1,4,1,1869,11,11,1,15),_Ons15501LastConfigChangeTime_Type())
ons15501LastConfigChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501LastConfigChangeTime.setStatus(_B)
_Ons15501InRemoteInfoUpdateTime_Type=TimeStamp
_Ons15501InRemoteInfoUpdateTime_Object=MibScalar
ons15501InRemoteInfoUpdateTime=_Ons15501InRemoteInfoUpdateTime_Object((1,3,6,1,4,1,1869,11,11,1,16),_Ons15501InRemoteInfoUpdateTime_Type())
ons15501InRemoteInfoUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501InRemoteInfoUpdateTime.setStatus(_B)
_Ons15501InRemoteChassisName_Type=DisplayString
_Ons15501InRemoteChassisName_Object=MibScalar
ons15501InRemoteChassisName=_Ons15501InRemoteChassisName_Object((1,3,6,1,4,1,1869,11,11,1,17),_Ons15501InRemoteChassisName_Type())
ons15501InRemoteChassisName.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501InRemoteChassisName.setStatus(_B)
_Ons15501InRemotePortName_Type=DisplayString
_Ons15501InRemotePortName_Object=MibScalar
ons15501InRemotePortName=_Ons15501InRemotePortName_Object((1,3,6,1,4,1,1869,11,11,1,18),_Ons15501InRemotePortName_Type())
ons15501InRemotePortName.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501InRemotePortName.setStatus(_B)
_Ons15501InRemoteAgentIpAddr_Type=IpAddress
_Ons15501InRemoteAgentIpAddr_Object=MibScalar
ons15501InRemoteAgentIpAddr=_Ons15501InRemoteAgentIpAddr_Object((1,3,6,1,4,1,1869,11,11,1,19),_Ons15501InRemoteAgentIpAddr_Type())
ons15501InRemoteAgentIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501InRemoteAgentIpAddr.setStatus(_B)
_Ons15501OutRemoteInfoUpdateTime_Type=TimeStamp
_Ons15501OutRemoteInfoUpdateTime_Object=MibScalar
ons15501OutRemoteInfoUpdateTime=_Ons15501OutRemoteInfoUpdateTime_Object((1,3,6,1,4,1,1869,11,11,1,20),_Ons15501OutRemoteInfoUpdateTime_Type())
ons15501OutRemoteInfoUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501OutRemoteInfoUpdateTime.setStatus(_B)
_Ons15501OutRemoteChassisName_Type=DisplayString
_Ons15501OutRemoteChassisName_Object=MibScalar
ons15501OutRemoteChassisName=_Ons15501OutRemoteChassisName_Object((1,3,6,1,4,1,1869,11,11,1,21),_Ons15501OutRemoteChassisName_Type())
ons15501OutRemoteChassisName.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501OutRemoteChassisName.setStatus(_B)
_Ons15501OutRemotePortName_Type=DisplayString
_Ons15501OutRemotePortName_Object=MibScalar
ons15501OutRemotePortName=_Ons15501OutRemotePortName_Object((1,3,6,1,4,1,1869,11,11,1,22),_Ons15501OutRemotePortName_Type())
ons15501OutRemotePortName.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501OutRemotePortName.setStatus(_B)
_Ons15501OutRemoteAgentIpAddr_Type=IpAddress
_Ons15501OutRemoteAgentIpAddr_Object=MibScalar
ons15501OutRemoteAgentIpAddr=_Ons15501OutRemoteAgentIpAddr_Object((1,3,6,1,4,1,1869,11,11,1,23),_Ons15501OutRemoteAgentIpAddr_Type())
ons15501OutRemoteAgentIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501OutRemoteAgentIpAddr.setStatus(_B)
_Ons15501SysAlarmStatus_Type=Ons15501AlarmStatus
_Ons15501SysAlarmStatus_Object=MibScalar
ons15501SysAlarmStatus=_Ons15501SysAlarmStatus_Object((1,3,6,1,4,1,1869,11,11,1,24),_Ons15501SysAlarmStatus_Type())
ons15501SysAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501SysAlarmStatus.setStatus(_B)
_Ons15501SysDateAndTime_Type=DateAndTime
_Ons15501SysDateAndTime_Object=MibScalar
ons15501SysDateAndTime=_Ons15501SysDateAndTime_Object((1,3,6,1,4,1,1869,11,11,1,25),_Ons15501SysDateAndTime_Type())
ons15501SysDateAndTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501SysDateAndTime.setStatus(_B)
_Ons15501Attr_ObjectIdentity=ObjectIdentity
ons15501Attr=_Ons15501Attr_ObjectIdentity((1,3,6,1,4,1,1869,11,11,2))
_Ons15501InputOpticalPower_Type=Ons15501TenthdB
_Ons15501InputOpticalPower_Object=MibScalar
ons15501InputOpticalPower=_Ons15501InputOpticalPower_Object((1,3,6,1,4,1,1869,11,11,2,1),_Ons15501InputOpticalPower_Type())
ons15501InputOpticalPower.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501InputOpticalPower.setStatus(_B)
if mibBuilder.loadTexts:ons15501InputOpticalPower.setUnits(_G)
class _Ons15501InputOpticalPowerMean_Type(Ons15501TenthdB):subtypeSpec=Ons15501TenthdB.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,0))
_Ons15501InputOpticalPowerMean_Type.__name__=_E
_Ons15501InputOpticalPowerMean_Object=MibScalar
ons15501InputOpticalPowerMean=_Ons15501InputOpticalPowerMean_Object((1,3,6,1,4,1,1869,11,11,2,2),_Ons15501InputOpticalPowerMean_Type())
ons15501InputOpticalPowerMean.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501InputOpticalPowerMean.setStatus(_B)
if mibBuilder.loadTexts:ons15501InputOpticalPowerMean.setUnits(_G)
class _Ons15501InputOpticalPowerTrigger_Type(Ons15501TenthdB):subtypeSpec=Ons15501TenthdB.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Ons15501InputOpticalPowerTrigger_Type.__name__=_E
_Ons15501InputOpticalPowerTrigger_Object=MibScalar
ons15501InputOpticalPowerTrigger=_Ons15501InputOpticalPowerTrigger_Object((1,3,6,1,4,1,1869,11,11,2,3),_Ons15501InputOpticalPowerTrigger_Type())
ons15501InputOpticalPowerTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501InputOpticalPowerTrigger.setStatus(_B)
if mibBuilder.loadTexts:ons15501InputOpticalPowerTrigger.setUnits(_H)
_Ons15501OutputOpticalPower_Type=Ons15501TenthdB
_Ons15501OutputOpticalPower_Object=MibScalar
ons15501OutputOpticalPower=_Ons15501OutputOpticalPower_Object((1,3,6,1,4,1,1869,11,11,2,4),_Ons15501OutputOpticalPower_Type())
ons15501OutputOpticalPower.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501OutputOpticalPower.setStatus(_B)
if mibBuilder.loadTexts:ons15501OutputOpticalPower.setUnits(_G)
_Ons15501OutputSignalPower_Type=Ons15501TenthdB
_Ons15501OutputSignalPower_Object=MibScalar
ons15501OutputSignalPower=_Ons15501OutputSignalPower_Object((1,3,6,1,4,1,1869,11,11,2,5),_Ons15501OutputSignalPower_Type())
ons15501OutputSignalPower.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501OutputSignalPower.setStatus(_B)
if mibBuilder.loadTexts:ons15501OutputSignalPower.setUnits(_G)
class _Ons15501OutputSignalPowerMean_Type(Ons15501TenthdB):subtypeSpec=Ons15501TenthdB.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,0))
_Ons15501OutputSignalPowerMean_Type.__name__=_E
_Ons15501OutputSignalPowerMean_Object=MibScalar
ons15501OutputSignalPowerMean=_Ons15501OutputSignalPowerMean_Object((1,3,6,1,4,1,1869,11,11,2,6),_Ons15501OutputSignalPowerMean_Type())
ons15501OutputSignalPowerMean.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501OutputSignalPowerMean.setStatus(_B)
if mibBuilder.loadTexts:ons15501OutputSignalPowerMean.setUnits(_G)
class _Ons15501OutputSignalPowerTrigger_Type(Ons15501TenthdB):subtypeSpec=Ons15501TenthdB.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_Ons15501OutputSignalPowerTrigger_Type.__name__=_E
_Ons15501OutputSignalPowerTrigger_Object=MibScalar
ons15501OutputSignalPowerTrigger=_Ons15501OutputSignalPowerTrigger_Object((1,3,6,1,4,1,1869,11,11,2,7),_Ons15501OutputSignalPowerTrigger_Type())
ons15501OutputSignalPowerTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501OutputSignalPowerTrigger.setStatus(_B)
if mibBuilder.loadTexts:ons15501OutputSignalPowerTrigger.setUnits(_H)
class _Ons15501ConfigOpticalGain_Type(Ons15501TenthdB):subtypeSpec=Ons15501TenthdB.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(70,175))
_Ons15501ConfigOpticalGain_Type.__name__=_E
_Ons15501ConfigOpticalGain_Object=MibScalar
ons15501ConfigOpticalGain=_Ons15501ConfigOpticalGain_Object((1,3,6,1,4,1,1869,11,11,2,8),_Ons15501ConfigOpticalGain_Type())
ons15501ConfigOpticalGain.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501ConfigOpticalGain.setStatus(_B)
if mibBuilder.loadTexts:ons15501ConfigOpticalGain.setUnits(_H)
_Ons15501OpticalPowerGain_Type=Ons15501TenthdB
_Ons15501OpticalPowerGain_Object=MibScalar
ons15501OpticalPowerGain=_Ons15501OpticalPowerGain_Object((1,3,6,1,4,1,1869,11,11,2,9),_Ons15501OpticalPowerGain_Type())
ons15501OpticalPowerGain.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501OpticalPowerGain.setStatus(_B)
if mibBuilder.loadTexts:ons15501OpticalPowerGain.setUnits(_H)
class _Ons15501GainTrigger_Type(Ons15501TenthdB):subtypeSpec=Ons15501TenthdB.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_Ons15501GainTrigger_Type.__name__=_E
_Ons15501GainTrigger_Object=MibScalar
ons15501GainTrigger=_Ons15501GainTrigger_Object((1,3,6,1,4,1,1869,11,11,2,10),_Ons15501GainTrigger_Type())
ons15501GainTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501GainTrigger.setStatus(_B)
if mibBuilder.loadTexts:ons15501GainTrigger.setUnits(_H)
_Ons15501PowerSupply1Level_Type=Ons15501TenthVolt
_Ons15501PowerSupply1Level_Object=MibScalar
ons15501PowerSupply1Level=_Ons15501PowerSupply1Level_Object((1,3,6,1,4,1,1869,11,11,2,11),_Ons15501PowerSupply1Level_Type())
ons15501PowerSupply1Level.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501PowerSupply1Level.setStatus(_B)
if mibBuilder.loadTexts:ons15501PowerSupply1Level.setUnits('volts')
_Ons15501PowerSupply2Level_Type=Ons15501TenthVolt
_Ons15501PowerSupply2Level_Object=MibScalar
ons15501PowerSupply2Level=_Ons15501PowerSupply2Level_Object((1,3,6,1,4,1,1869,11,11,2,12),_Ons15501PowerSupply2Level_Type())
ons15501PowerSupply2Level.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501PowerSupply2Level.setStatus(_B)
if mibBuilder.loadTexts:ons15501PowerSupply2Level.setUnits('volts')
_Ons15501LaserStatus_Type=Ons15501AlarmStatus
_Ons15501LaserStatus_Object=MibScalar
ons15501LaserStatus=_Ons15501LaserStatus_Object((1,3,6,1,4,1,1869,11,11,2,13),_Ons15501LaserStatus_Type())
ons15501LaserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501LaserStatus.setStatus(_B)
_Ons15501DevAmbTemp_Type=Ons15501TenthCentigrade
_Ons15501DevAmbTemp_Object=MibScalar
ons15501DevAmbTemp=_Ons15501DevAmbTemp_Object((1,3,6,1,4,1,1869,11,11,2,14),_Ons15501DevAmbTemp_Type())
ons15501DevAmbTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501DevAmbTemp.setStatus(_B)
if mibBuilder.loadTexts:ons15501DevAmbTemp.setUnits(_J)
class _Ons15501DevAmbTempMean_Type(Ons15501TenthCentigrade):subtypeSpec=Ons15501TenthCentigrade.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,400))
_Ons15501DevAmbTempMean_Type.__name__=_K
_Ons15501DevAmbTempMean_Object=MibScalar
ons15501DevAmbTempMean=_Ons15501DevAmbTempMean_Object((1,3,6,1,4,1,1869,11,11,2,15),_Ons15501DevAmbTempMean_Type())
ons15501DevAmbTempMean.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501DevAmbTempMean.setStatus(_B)
if mibBuilder.loadTexts:ons15501DevAmbTempMean.setUnits(_J)
class _Ons15501DevAmbTempTrigger_Type(Ons15501TenthCentigrade):subtypeSpec=Ons15501TenthCentigrade.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,300))
_Ons15501DevAmbTempTrigger_Type.__name__=_K
_Ons15501DevAmbTempTrigger_Object=MibScalar
ons15501DevAmbTempTrigger=_Ons15501DevAmbTempTrigger_Object((1,3,6,1,4,1,1869,11,11,2,16),_Ons15501DevAmbTempTrigger_Type())
ons15501DevAmbTempTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:ons15501DevAmbTempTrigger.setStatus(_B)
if mibBuilder.loadTexts:ons15501DevAmbTempTrigger.setUnits(_J)
_Ons15501PowerSupply1Status_Type=Ons15501AlarmStatus
_Ons15501PowerSupply1Status_Object=MibScalar
ons15501PowerSupply1Status=_Ons15501PowerSupply1Status_Object((1,3,6,1,4,1,1869,11,11,2,17),_Ons15501PowerSupply1Status_Type())
ons15501PowerSupply1Status.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501PowerSupply1Status.setStatus(_B)
_Ons15501PowerSupply2Status_Type=Ons15501AlarmStatus
_Ons15501PowerSupply2Status_Object=MibScalar
ons15501PowerSupply2Status=_Ons15501PowerSupply2Status_Object((1,3,6,1,4,1,1869,11,11,2,18),_Ons15501PowerSupply2Status_Type())
ons15501PowerSupply2Status.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501PowerSupply2Status.setStatus(_B)
_Ons15501Alarms_ObjectIdentity=ObjectIdentity
ons15501Alarms=_Ons15501Alarms_ObjectIdentity((1,3,6,1,4,1,1869,11,11,3))
class _Ons15501LastTrapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_Ons15501LastTrapIndex_Type.__name__=_F
_Ons15501LastTrapIndex_Object=MibScalar
ons15501LastTrapIndex=_Ons15501LastTrapIndex_Object((1,3,6,1,4,1,1869,11,11,3,1),_Ons15501LastTrapIndex_Type())
ons15501LastTrapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501LastTrapIndex.setStatus(_B)
_Ons15501TrapLogTable_Object=MibTable
ons15501TrapLogTable=_Ons15501TrapLogTable_Object((1,3,6,1,4,1,1869,11,11,3,2))
if mibBuilder.loadTexts:ons15501TrapLogTable.setStatus(_B)
_Ons15501TrapLogEntry_Object=MibTableRow
ons15501TrapLogEntry=_Ons15501TrapLogEntry_Object((1,3,6,1,4,1,1869,11,11,3,2,1))
ons15501TrapLogEntry.setIndexNames((0,_A,_AA))
if mibBuilder.loadTexts:ons15501TrapLogEntry.setStatus(_B)
class _Ons15501TrapLogEntryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_Ons15501TrapLogEntryIndex_Type.__name__=_F
_Ons15501TrapLogEntryIndex_Object=MibTableColumn
ons15501TrapLogEntryIndex=_Ons15501TrapLogEntryIndex_Object((1,3,6,1,4,1,1869,11,11,3,2,1,1),_Ons15501TrapLogEntryIndex_Type())
ons15501TrapLogEntryIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:ons15501TrapLogEntryIndex.setStatus(_B)
_Ons15501TrapLogEntryTrapType_Type=Ons15501TrapTypeEnumeration
_Ons15501TrapLogEntryTrapType_Object=MibTableColumn
ons15501TrapLogEntryTrapType=_Ons15501TrapLogEntryTrapType_Object((1,3,6,1,4,1,1869,11,11,3,2,1,2),_Ons15501TrapLogEntryTrapType_Type())
ons15501TrapLogEntryTrapType.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501TrapLogEntryTrapType.setStatus(_B)
_Ons15501TrapLogEntryDirection_Type=Ons15501TrapDirectionEnumeration
_Ons15501TrapLogEntryDirection_Object=MibTableColumn
ons15501TrapLogEntryDirection=_Ons15501TrapLogEntryDirection_Object((1,3,6,1,4,1,1869,11,11,3,2,1,3),_Ons15501TrapLogEntryDirection_Type())
ons15501TrapLogEntryDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501TrapLogEntryDirection.setStatus(_B)
_Ons15501TrapLogEntryTimeStamp_Type=TimeStamp
_Ons15501TrapLogEntryTimeStamp_Object=MibTableColumn
ons15501TrapLogEntryTimeStamp=_Ons15501TrapLogEntryTimeStamp_Object((1,3,6,1,4,1,1869,11,11,3,2,1,4),_Ons15501TrapLogEntryTimeStamp_Type())
ons15501TrapLogEntryTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501TrapLogEntryTimeStamp.setStatus(_B)
_Ons15501TrapLogEntryDateAndTime_Type=DateAndTime
_Ons15501TrapLogEntryDateAndTime_Object=MibTableColumn
ons15501TrapLogEntryDateAndTime=_Ons15501TrapLogEntryDateAndTime_Object((1,3,6,1,4,1,1869,11,11,3,2,1,5),_Ons15501TrapLogEntryDateAndTime_Type())
ons15501TrapLogEntryDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501TrapLogEntryDateAndTime.setStatus(_B)
_Ons15501TrapLogEntryPhyIndex_Type=PhysicalIndex
_Ons15501TrapLogEntryPhyIndex_Object=MibTableColumn
ons15501TrapLogEntryPhyIndex=_Ons15501TrapLogEntryPhyIndex_Object((1,3,6,1,4,1,1869,11,11,3,2,1,6),_Ons15501TrapLogEntryPhyIndex_Type())
ons15501TrapLogEntryPhyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501TrapLogEntryPhyIndex.setStatus(_B)
_Ons15501TrapLogEntrySeverity_Type=Ons15501AlarmStatus
_Ons15501TrapLogEntrySeverity_Object=MibTableColumn
ons15501TrapLogEntrySeverity=_Ons15501TrapLogEntrySeverity_Object((1,3,6,1,4,1,1869,11,11,3,2,1,7),_Ons15501TrapLogEntrySeverity_Type())
ons15501TrapLogEntrySeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501TrapLogEntrySeverity.setStatus(_B)
_Ons15501ActiveAlarmTable_Object=MibTable
ons15501ActiveAlarmTable=_Ons15501ActiveAlarmTable_Object((1,3,6,1,4,1,1869,11,11,3,3))
if mibBuilder.loadTexts:ons15501ActiveAlarmTable.setStatus(_B)
_Ons15501ActiveAlarmEntry_Object=MibTableRow
ons15501ActiveAlarmEntry=_Ons15501ActiveAlarmEntry_Object((1,3,6,1,4,1,1869,11,11,3,3,1))
ons15501ActiveAlarmEntry.setIndexNames((0,_A,_AB))
if mibBuilder.loadTexts:ons15501ActiveAlarmEntry.setStatus(_B)
_Ons15501ActAlarmType_Type=Ons15501TrapTypeEnumeration
_Ons15501ActAlarmType_Object=MibTableColumn
ons15501ActAlarmType=_Ons15501ActAlarmType_Object((1,3,6,1,4,1,1869,11,11,3,3,1,1),_Ons15501ActAlarmType_Type())
ons15501ActAlarmType.setMaxAccess(_L)
if mibBuilder.loadTexts:ons15501ActAlarmType.setStatus(_B)
_Ons15501ActAlarmTimeStamp_Type=TimeStamp
_Ons15501ActAlarmTimeStamp_Object=MibTableColumn
ons15501ActAlarmTimeStamp=_Ons15501ActAlarmTimeStamp_Object((1,3,6,1,4,1,1869,11,11,3,3,1,2),_Ons15501ActAlarmTimeStamp_Type())
ons15501ActAlarmTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501ActAlarmTimeStamp.setStatus(_B)
_Ons15501ActAlarmDateAndTime_Type=DateAndTime
_Ons15501ActAlarmDateAndTime_Object=MibTableColumn
ons15501ActAlarmDateAndTime=_Ons15501ActAlarmDateAndTime_Object((1,3,6,1,4,1,1869,11,11,3,3,1,3),_Ons15501ActAlarmDateAndTime_Type())
ons15501ActAlarmDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501ActAlarmDateAndTime.setStatus(_B)
_Ons15501ActAlarmPhyIndex_Type=PhysicalIndex
_Ons15501ActAlarmPhyIndex_Object=MibTableColumn
ons15501ActAlarmPhyIndex=_Ons15501ActAlarmPhyIndex_Object((1,3,6,1,4,1,1869,11,11,3,3,1,4),_Ons15501ActAlarmPhyIndex_Type())
ons15501ActAlarmPhyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501ActAlarmPhyIndex.setStatus(_B)
_Ons15501ActAlarmSeverity_Type=Ons15501AlarmStatus
_Ons15501ActAlarmSeverity_Object=MibTableColumn
ons15501ActAlarmSeverity=_Ons15501ActAlarmSeverity_Object((1,3,6,1,4,1,1869,11,11,3,3,1,5),_Ons15501ActAlarmSeverity_Type())
ons15501ActAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501ActAlarmSeverity.setStatus(_B)
_Ons15501TrapDescriptionTable_Object=MibTable
ons15501TrapDescriptionTable=_Ons15501TrapDescriptionTable_Object((1,3,6,1,4,1,1869,11,11,3,4))
if mibBuilder.loadTexts:ons15501TrapDescriptionTable.setStatus(_B)
_Ons15501TrapDescriptionEntry_Object=MibTableRow
ons15501TrapDescriptionEntry=_Ons15501TrapDescriptionEntry_Object((1,3,6,1,4,1,1869,11,11,3,4,1))
ons15501TrapDescriptionEntry.setIndexNames((0,_A,_AC))
if mibBuilder.loadTexts:ons15501TrapDescriptionEntry.setStatus(_B)
_Ons15501TrapTypeValue_Type=Ons15501TrapTypeEnumeration
_Ons15501TrapTypeValue_Object=MibTableColumn
ons15501TrapTypeValue=_Ons15501TrapTypeValue_Object((1,3,6,1,4,1,1869,11,11,3,4,1,1),_Ons15501TrapTypeValue_Type())
ons15501TrapTypeValue.setMaxAccess(_L)
if mibBuilder.loadTexts:ons15501TrapTypeValue.setStatus(_B)
_Ons15501TrapDescription_Type=DisplayString
_Ons15501TrapDescription_Object=MibTableColumn
ons15501TrapDescription=_Ons15501TrapDescription_Object((1,3,6,1,4,1,1869,11,11,3,4,1,2),_Ons15501TrapDescription_Type())
ons15501TrapDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501TrapDescription.setStatus(_B)
_Ons15501TrapSeverity_Type=Ons15501AlarmStatus
_Ons15501TrapSeverity_Object=MibTableColumn
ons15501TrapSeverity=_Ons15501TrapSeverity_Object((1,3,6,1,4,1,1869,11,11,3,4,1,3),_Ons15501TrapSeverity_Type())
ons15501TrapSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:ons15501TrapSeverity.setStatus(_B)
_Ons15501Notification_ObjectIdentity=ObjectIdentity
ons15501Notification=_Ons15501Notification_ObjectIdentity((1,3,6,1,4,1,1869,11,11,4))
_Ons15501NotificationPrefix_ObjectIdentity=ObjectIdentity
ons15501NotificationPrefix=_Ons15501NotificationPrefix_ObjectIdentity((1,3,6,1,4,1,1869,11,11,4,0))
_Ons15501OIDs_ObjectIdentity=ObjectIdentity
ons15501OIDs=_Ons15501OIDs_ObjectIdentity((1,3,6,1,4,1,1869,11,11,5))
_Ons15501OIDSystem_ObjectIdentity=ObjectIdentity
ons15501OIDSystem=_Ons15501OIDSystem_ObjectIdentity((1,3,6,1,4,1,1869,11,11,5,1))
_Ons15501OIDEntity_ObjectIdentity=ObjectIdentity
ons15501OIDEntity=_Ons15501OIDEntity_ObjectIdentity((1,3,6,1,4,1,1869,11,11,5,2))
_Ons15501OIDChasiss_ObjectIdentity=ObjectIdentity
ons15501OIDChasiss=_Ons15501OIDChasiss_ObjectIdentity((1,3,6,1,4,1,1869,11,11,5,2,1))
_Ons15501OIDInPort_ObjectIdentity=ObjectIdentity
ons15501OIDInPort=_Ons15501OIDInPort_ObjectIdentity((1,3,6,1,4,1,1869,11,11,5,2,2))
_Ons15501OIDOutPort_ObjectIdentity=ObjectIdentity
ons15501OIDOutPort=_Ons15501OIDOutPort_ObjectIdentity((1,3,6,1,4,1,1869,11,11,5,2,3))
_Ons15501OIDPowerSupply_ObjectIdentity=ObjectIdentity
ons15501OIDPowerSupply=_Ons15501OIDPowerSupply_ObjectIdentity((1,3,6,1,4,1,1869,11,11,5,2,4))
_Ons15501OIDChassisAC_ObjectIdentity=ObjectIdentity
ons15501OIDChassisAC=_Ons15501OIDChassisAC_ObjectIdentity((1,3,6,1,4,1,1869,11,11,5,2,5))
_Ons15501OIDPowerSupplyAC_ObjectIdentity=ObjectIdentity
ons15501OIDPowerSupplyAC=_Ons15501OIDPowerSupplyAC_ObjectIdentity((1,3,6,1,4,1,1869,11,11,5,2,6))
_Ons15501OIDSystemAC_ObjectIdentity=ObjectIdentity
ons15501OIDSystemAC=_Ons15501OIDSystemAC_ObjectIdentity((1,3,6,1,4,1,1869,11,11,5,3))
_Ons15501MIBConformance_ObjectIdentity=ObjectIdentity
ons15501MIBConformance=_Ons15501MIBConformance_ObjectIdentity((1,3,6,1,4,1,1869,11,11,6))
_Ons15501MIBCompliances_ObjectIdentity=ObjectIdentity
ons15501MIBCompliances=_Ons15501MIBCompliances_ObjectIdentity((1,3,6,1,4,1,1869,11,11,6,1))
_Ons15501MIBGroups_ObjectIdentity=ObjectIdentity
ons15501MIBGroups=_Ons15501MIBGroups_ObjectIdentity((1,3,6,1,4,1,1869,11,11,6,2))
ons15501SysInfoGroup=ObjectGroup((1,3,6,1,4,1,1869,11,11,6,2,1))
ons15501SysInfoGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ons15501SysInfoGroup.setStatus(_k)
ons15501TrapLogGroup=ObjectGroup((1,3,6,1,4,1,1869,11,11,6,2,2))
ons15501TrapLogGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_AD),(_A,_AE),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:ons15501TrapLogGroup.setStatus(_B)
ons15501ActiveAlarmGroup=ObjectGroup((1,3,6,1,4,1,1869,11,11,6,2,3))
ons15501ActiveAlarmGroup.setObjects(*((_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:ons15501ActiveAlarmGroup.setStatus(_B)
ons15501TrapDescriptionGroup=ObjectGroup((1,3,6,1,4,1,1869,11,11,6,2,4))
ons15501TrapDescriptionGroup.setObjects(*((_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:ons15501TrapDescriptionGroup.setStatus(_B)
ons15501FinalAttrGroup=ObjectGroup((1,3,6,1,4,1,1869,11,11,6,2,5))
ons15501FinalAttrGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:ons15501FinalAttrGroup.setStatus(_k)
ons15501CoreAttrGroup=ObjectGroup((1,3,6,1,4,1,1869,11,11,6,2,7))
ons15501CoreAttrGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:ons15501CoreAttrGroup.setStatus(_B)
ons15501PowerSupplyStatusGroup=ObjectGroup((1,3,6,1,4,1,1869,11,11,6,2,8))
ons15501PowerSupplyStatusGroup.setObjects(*((_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:ons15501PowerSupplyStatusGroup.setStatus(_B)
ons15501PowerSupplyLevelGroup=ObjectGroup((1,3,6,1,4,1,1869,11,11,6,2,9))
ons15501PowerSupplyLevelGroup.setObjects(*((_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:ons15501PowerSupplyLevelGroup.setStatus(_B)
ons15501SysInfoGroup2=ObjectGroup((1,3,6,1,4,1,1869,11,11,6,2,10))
ons15501SysInfoGroup2.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_AN)))
if mibBuilder.loadTexts:ons15501SysInfoGroup2.setStatus(_B)
ons15501GenericNotificationTrap=NotificationType((1,3,6,1,4,1,1869,11,11,4,0,1))
ons15501GenericNotificationTrap.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:ons15501GenericNotificationTrap.setStatus(_B)
ons15501FinalNotificationsGroup=NotificationGroup((1,3,6,1,4,1,1869,11,11,6,2,6))
ons15501FinalNotificationsGroup.setObjects((_A,_AO))
if mibBuilder.loadTexts:ons15501FinalNotificationsGroup.setStatus(_B)
ons15501FinalCompliance=ModuleCompliance((1,3,6,1,4,1,1869,11,11,6,1,1))
ons15501FinalCompliance.setObjects(*((_A,_AP),(_A,_AQ),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:ons15501FinalCompliance.setStatus(_k)
ons15501Rel4Compliance=ModuleCompliance((1,3,6,1,4,1,1869,11,11,6,1,2))
ons15501Rel4Compliance.setObjects(*((_A,_AR),(_A,_AS),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AT),(_A,_AU)))
if mibBuilder.loadTexts:ons15501Rel4Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'Ons15501ImageDnLoadStatus':Ons15501ImageDnLoadStatus,'Ons15501AdminStatus':Ons15501AdminStatus,'Ons15501NTPStatus':Ons15501NTPStatus,'Ons15501TenthVolt':Ons15501TenthVolt,_E:Ons15501TenthdB,_K:Ons15501TenthCentigrade,'Ons15501AlarmStatus':Ons15501AlarmStatus,'Ons15501TrapTypeEnumeration':Ons15501TrapTypeEnumeration,'Ons15501TrapDirectionEnumeration':Ons15501TrapDirectionEnumeration,'synchronous':synchronous,'synEmbLx':synEmbLx,'ons15501MIB':ons15501MIB,'ons15501Sys':ons15501Sys,_M:ons15501SysDevFlash1Image,_N:ons15501SysDevFlash2Image,_O:ons15501SysDevFlash3Image,_P:ons15501SysSwDownload,_S:ons15501SysDevActiveImage,_j:ons15501SysDeviceManagerList,_Q:ons15501SysSwDownloadStatus,_R:ons15501SysConfiguredImage,_Y:ons15501CLEICode,_U:ons15501PrimaryNTP,_V:ons15501SecondaryNTP,_W:ons15501NTPAdminStatus,_X:ons15501NTPOperationalStatus,_i:ons15501ActiveSoftwareVer,_h:ons15501LastConfigChangeTime,_Z:ons15501InRemoteInfoUpdateTime,_a:ons15501InRemoteChassisName,_b:ons15501InRemotePortName,_c:ons15501InRemoteAgentIpAddr,_d:ons15501OutRemoteInfoUpdateTime,_e:ons15501OutRemoteChassisName,_f:ons15501OutRemotePortName,_g:ons15501OutRemoteAgentIpAddr,_T:ons15501SysAlarmStatus,_AN:ons15501SysDateAndTime,'ons15501Attr':ons15501Attr,_q:ons15501InputOpticalPower,_r:ons15501InputOpticalPowerMean,_s:ons15501InputOpticalPowerTrigger,_t:ons15501OutputOpticalPower,_u:ons15501OutputSignalPower,_v:ons15501OutputSignalPowerMean,_w:ons15501OutputSignalPowerTrigger,_x:ons15501ConfigOpticalGain,_y:ons15501OpticalPowerGain,_A5:ons15501GainTrigger,_z:ons15501PowerSupply1Level,_A0:ons15501PowerSupply2Level,_A4:ons15501LaserStatus,_A1:ons15501DevAmbTemp,_A2:ons15501DevAmbTempMean,_A3:ons15501DevAmbTempTrigger,_AL:ons15501PowerSupply1Status,_AM:ons15501PowerSupply2Status,'ons15501Alarms':ons15501Alarms,_l:ons15501LastTrapIndex,'ons15501TrapLogTable':ons15501TrapLogTable,'ons15501TrapLogEntry':ons15501TrapLogEntry,_AA:ons15501TrapLogEntryIndex,_m:ons15501TrapLogEntryTrapType,_n:ons15501TrapLogEntryDirection,_AD:ons15501TrapLogEntryTimeStamp,_AE:ons15501TrapLogEntryDateAndTime,_o:ons15501TrapLogEntryPhyIndex,_p:ons15501TrapLogEntrySeverity,'ons15501ActiveAlarmTable':ons15501ActiveAlarmTable,'ons15501ActiveAlarmEntry':ons15501ActiveAlarmEntry,_AB:ons15501ActAlarmType,_AG:ons15501ActAlarmTimeStamp,_AH:ons15501ActAlarmDateAndTime,_AF:ons15501ActAlarmPhyIndex,_AI:ons15501ActAlarmSeverity,'ons15501TrapDescriptionTable':ons15501TrapDescriptionTable,'ons15501TrapDescriptionEntry':ons15501TrapDescriptionEntry,_AC:ons15501TrapTypeValue,_AJ:ons15501TrapDescription,_AK:ons15501TrapSeverity,'ons15501Notification':ons15501Notification,'ons15501NotificationPrefix':ons15501NotificationPrefix,_AO:ons15501GenericNotificationTrap,'ons15501OIDs':ons15501OIDs,'ons15501OIDSystem':ons15501OIDSystem,'ons15501OIDEntity':ons15501OIDEntity,'ons15501OIDChasiss':ons15501OIDChasiss,'ons15501OIDInPort':ons15501OIDInPort,'ons15501OIDOutPort':ons15501OIDOutPort,'ons15501OIDPowerSupply':ons15501OIDPowerSupply,'ons15501OIDChassisAC':ons15501OIDChassisAC,'ons15501OIDPowerSupplyAC':ons15501OIDPowerSupplyAC,'ons15501OIDSystemAC':ons15501OIDSystemAC,'ons15501MIBConformance':ons15501MIBConformance,'ons15501MIBCompliances':ons15501MIBCompliances,'ons15501FinalCompliance':ons15501FinalCompliance,'ons15501Rel4Compliance':ons15501Rel4Compliance,'ons15501MIBGroups':ons15501MIBGroups,_AP:ons15501SysInfoGroup,_A6:ons15501TrapLogGroup,_A7:ons15501ActiveAlarmGroup,_A8:ons15501TrapDescriptionGroup,_AQ:ons15501FinalAttrGroup,_A9:ons15501FinalNotificationsGroup,_AS:ons15501CoreAttrGroup,_AT:ons15501PowerSupplyStatusGroup,_AU:ons15501PowerSupplyLevelGroup,_AR:ons15501SysInfoGroup2})