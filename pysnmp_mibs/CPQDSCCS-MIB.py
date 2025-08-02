_R='read-write'
_Q='NotificationType'
_P='Integer32'
_O='trapDescription'
_N='trapEventId'
_M='csSoftwareVersion'
_L='csSerialNumber'
_K='csProductId'
_J='csProductName'
_I='csContactPhoneNumber'
_H='csContactName'
_G='csRoomName'
_F='sysName'
_E='SNMPv2-MIB'
_D='read-only'
_C='mandatory'
_B='DisplayString'
_A='CPQDSCCS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,=mibBuilder.importSymbols('CPQHOST-MIB','compaq')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysContact,sysDescr,sysLocation,sysName=mibBuilder.importSymbols(_E,'sysContact','sysDescr','sysLocation',_F)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_P,'IpAddress','ModuleIdentity','MibIdentifier',_Q,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_Q,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','TextualConvention')
_CpqDsccs_ObjectIdentity=ObjectIdentity
cpqDsccs=_CpqDsccs_ObjectIdentity((1,3,6,1,4,1,232,171))
_DsccsTrapInfo_ObjectIdentity=ObjectIdentity
dsccsTrapInfo=_DsccsTrapInfo_ObjectIdentity((1,3,6,1,4,1,232,171,1))
class _CsRoomName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CsRoomName_Type.__name__=_B
_CsRoomName_Object=MibScalar
csRoomName=_CsRoomName_Object((1,3,6,1,4,1,232,171,1,1),_CsRoomName_Type())
csRoomName.setMaxAccess(_D)
if mibBuilder.loadTexts:csRoomName.setStatus(_C)
class _CsContactName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CsContactName_Type.__name__=_B
_CsContactName_Object=MibScalar
csContactName=_CsContactName_Object((1,3,6,1,4,1,232,171,1,2),_CsContactName_Type())
csContactName.setMaxAccess(_D)
if mibBuilder.loadTexts:csContactName.setStatus(_C)
class _CsContactPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CsContactPhoneNumber_Type.__name__=_B
_CsContactPhoneNumber_Object=MibScalar
csContactPhoneNumber=_CsContactPhoneNumber_Object((1,3,6,1,4,1,232,171,1,3),_CsContactPhoneNumber_Type())
csContactPhoneNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:csContactPhoneNumber.setStatus(_C)
class _CsProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_CsProductName_Type.__name__=_B
_CsProductName_Object=MibScalar
csProductName=_CsProductName_Object((1,3,6,1,4,1,232,171,1,4),_CsProductName_Type())
csProductName.setMaxAccess(_R)
if mibBuilder.loadTexts:csProductName.setStatus(_C)
class _CsProductId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CsProductId_Type.__name__=_B
_CsProductId_Object=MibScalar
csProductId=_CsProductId_Object((1,3,6,1,4,1,232,171,1,5),_CsProductId_Type())
csProductId.setMaxAccess(_R)
if mibBuilder.loadTexts:csProductId.setStatus(_C)
class _CsSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CsSerialNumber_Type.__name__=_B
_CsSerialNumber_Object=MibScalar
csSerialNumber=_CsSerialNumber_Object((1,3,6,1,4,1,232,171,1,6),_CsSerialNumber_Type())
csSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:csSerialNumber.setStatus(_C)
class _CsSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CsSoftwareVersion_Type.__name__=_B
_CsSoftwareVersion_Object=MibScalar
csSoftwareVersion=_CsSoftwareVersion_Object((1,3,6,1,4,1,232,171,1,7),_CsSoftwareVersion_Type())
csSoftwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:csSoftwareVersion.setStatus(_C)
class _TrapEventId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1001,1002,1003,1004,1005,1006,1007,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,6001,7001)));namedValues=NamedValues(*(('webGuiDscAutoMode',1001),('webGuiDscMonitoringMode',1002),('webGuiDscEmergencyOverrideMode',1003),('webGuiDscOff',1004),('webGuiUserLoggedIn',1005),('webGuiUserLoggedOut',1006),('webGuiUserSessionExpired',1007),('ctrlMasterSensorTempAboveAcceptBand',2001),('ctrlOrphanSensorTempAboveAcceptBand',2002),('ctrlTempSensorAboveAcceptBand',2003),('ctrlRegionInfluenceAhuNoSensors',2004),('ctrlNoTciDataForSensorAndAhu',2005),('ctrlTciDataExistsForSensorsRemovedFromDsc',2006),('ctrlSensorTimestampOld',2007),('ctrlAhuOff',2008),('ctrlStarted',2009),('ctrlStopped',2010),('commisFullStartedByUser',3001),('commisPartialStartedByUserForAhu',3002),('commisAbortedByUseer',3003),('commisFinishedSuccessfully',3004),('commisFailedSupplyAirTempForAhuDidNotChange',3005),('commisFailedCouldNotChangeAhuSetPoint',3006),('commisFailedDataCenterTempExceedThresholdLimit',3007),('commisCannotPerformOperation',3008),('commisLoadingConfigProfile',3009),('commisLoadingPropertiesForConfigProfile',3010),('commisLoadingConfigParamForProfile',3011),('commisPerformCheckForAhusInConfigProfile',3012),('commisInitSubsystemForConfigProfile',3013),('commisInitSubsystemForCOnfigProfileAndInstance',3014),('commisStartingForConfigProfile',3015),('commisBeginInitCycle',3016),('commisProcessCompletedSuccessfullyForConfiguration',3017),('commisHaltActiveCommmissioningExecution',3018),('commisExecutionFailedForConfiguration',3019),('commisPerformPerturbationForInitDistributionLevel',3020),('commisPerformPerturbationForAhu',3021),('commisAttestSystemPerturbationForAhu',3022),('commisAssertionFailedForAhuFeedbackOnTest',3023),('commisWaitingForSystemSteadinessFromSensorNetwork',3024),('commisValidatingAhuSupplyAirTempHasChanged',3025),('commisStoreSensorNetworkStateAndDataForPerturbation',3026),('commisStoreBasecaseSensorTempAndData',3027),('commisStoreSystemPerturbationSensorTempAndData',3028),('commisMergeDataForConfig',3029),('commisRollbackAndCleanFromDatabaseChanges',3030),('commisInitDefaultConfigProfiles',3031),('commisAhuPerturbationWithinConfig',3032),('commisCannotPerformMergeOpWhenRunningCommissioning',3033),('commisCannotHaltCommissioningNoActiveInstanceRunning',3034),('commisBeginExecutionCycleSettingAhuToConfiguredLevels',3035),('commisSettingAhusToUniformDistributionLevel',3036),('commuOpcCommunicationsLost',4001),('commuMbcHostIsUnreachablePingFailed',4002),('commuOpcStatus',4003),('commuTempForSensorOutOfRange',4004),('commuFailsafeDeviceHeartbeatNotPresent',4005),('commuReverseAirFlowDetectedInRack',4006),('commuAhuSupplyAirTempReachedHighLimit',4007),('commuAhuSupplyAirTempReachedLowLimit',4008),('commuAhuReturnAirTempReachedHighLimit',4009),('commuAhuReturnAirTempReachedLowLimit',4010),('commuAhuPoweredOff',4011),('commuAhuFluidLeakDetected',4012),('commuAhuSwitchedToLocalControl',4013),('commuSensorTimestampOld',4014),('internalSoftwareUnhandledException',6001),('other',7001)))
_TrapEventId_Type.__name__=_P
_TrapEventId_Object=MibScalar
trapEventId=_TrapEventId_Object((1,3,6,1,4,1,232,171,1,8),_TrapEventId_Type())
trapEventId.setMaxAccess(_D)
if mibBuilder.loadTexts:trapEventId.setStatus(_C)
class _TrapDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TrapDescription_Type.__name__=_B
_TrapDescription_Object=MibScalar
trapDescription=_TrapDescription_Object((1,3,6,1,4,1,232,171,1,9),_TrapDescription_Type())
trapDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:trapDescription.setStatus(_C)
trapDscTest=NotificationType((1,3,6,1,4,1,232,171,0,1))
trapDscTest.setObjects(*((_E,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:trapDscTest.setStatus('')
trapDscCritical=NotificationType((1,3,6,1,4,1,232,171,0,2))
trapDscCritical.setObjects(*((_E,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:trapDscCritical.setStatus('')
trapDscWarning=NotificationType((1,3,6,1,4,1,232,171,0,3))
trapDscWarning.setObjects(*((_E,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:trapDscWarning.setStatus('')
trapDscInformation=NotificationType((1,3,6,1,4,1,232,171,0,4))
trapDscInformation.setObjects(*((_E,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:trapDscInformation.setStatus('')
mibBuilder.exportSymbols(_A,**{'cpqDsccs':cpqDsccs,'trapDscTest':trapDscTest,'trapDscCritical':trapDscCritical,'trapDscWarning':trapDscWarning,'trapDscInformation':trapDscInformation,'dsccsTrapInfo':dsccsTrapInfo,_G:csRoomName,_H:csContactName,_I:csContactPhoneNumber,_J:csProductName,_K:csProductId,_L:csSerialNumber,_M:csSoftwareVersion,_N:trapEventId,_O:trapDescription})