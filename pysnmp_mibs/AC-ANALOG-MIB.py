_b='acAnalogCommonChannelIndex'
_a='acAnalogFxsLineTestIndex'
_Z='reversePolarity'
_Y='normalPolarity'
_X='testFailed'
_W='lineTestDone'
_V='runLineTest'
_U='noTestActivated'
_T='acAnalogFxoLineTestIndex'
_S='acAnalogLegsLegIndex'
_R='acAnalogFxsFxoIndex'
_Q='notAvailable'
_P='acAnalogFxoFarEndDisconnectToneIndex'
_O='offHookState'
_N='onHookState'
_M='unitedStates'
_L='europe'
_K='SnmpAdminString'
_J='obsolete'
_I='not-accessible'
_H='AC-ANALOG-MIB'
_G='enable'
_F='disable'
_E='Unsigned32'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acBoardMibs,acGeneric,acProducts,acRegistrations,audioCodes=mibBuilder.importSymbols('AUDIOCODES-TYPES-MIB','acBoardMibs','acGeneric','acProducts','acRegistrations','audioCodes')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TAddress','TextualConvention')
acAnalog=ModuleIdentity((1,3,6,1,4,1,5003,9,10,8))
_AcAnalogConfiguration_ObjectIdentity=ObjectIdentity
acAnalogConfiguration=_AcAnalogConfiguration_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,1))
_AcAnalogConfig_ObjectIdentity=ObjectIdentity
acAnalogConfig=_AcAnalogConfig_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,1,1))
_AcAnalogMisc_ObjectIdentity=ObjectIdentity
acAnalogMisc=_AcAnalogMisc_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,1,1,1))
class _AcAnalogMiscCurrentDisconnectDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,1500))
_AcAnalogMiscCurrentDisconnectDuration_Type.__name__=_E
_AcAnalogMiscCurrentDisconnectDuration_Object=MibScalar
acAnalogMiscCurrentDisconnectDuration=_AcAnalogMiscCurrentDisconnectDuration_Object((1,3,6,1,4,1,5003,9,10,8,1,1,1,1),_AcAnalogMiscCurrentDisconnectDuration_Type())
acAnalogMiscCurrentDisconnectDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogMiscCurrentDisconnectDuration.setStatus(_A)
class _AcAnalogMiscFlashHookPeriod_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,3000))
_AcAnalogMiscFlashHookPeriod_Type.__name__=_E
_AcAnalogMiscFlashHookPeriod_Object=MibScalar
acAnalogMiscFlashHookPeriod=_AcAnalogMiscFlashHookPeriod_Object((1,3,6,1,4,1,5003,9,10,8,1,1,1,2),_AcAnalogMiscFlashHookPeriod_Type())
acAnalogMiscFlashHookPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogMiscFlashHookPeriod.setStatus(_A)
class _AcAnalogMiscGroundKeyDetection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AcAnalogMiscGroundKeyDetection_Type.__name__=_B
_AcAnalogMiscGroundKeyDetection_Object=MibScalar
acAnalogMiscGroundKeyDetection=_AcAnalogMiscGroundKeyDetection_Object((1,3,6,1,4,1,5003,9,10,8,1,1,1,3),_AcAnalogMiscGroundKeyDetection_Type())
acAnalogMiscGroundKeyDetection.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogMiscGroundKeyDetection.setStatus(_A)
_AcAuxiliaryFiles_ObjectIdentity=ObjectIdentity
acAuxiliaryFiles=_AcAuxiliaryFiles_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,1,1,2))
class _AcAuxiliaryFilesFxsCoefficients_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_AcAuxiliaryFilesFxsCoefficients_Type.__name__=_K
_AcAuxiliaryFilesFxsCoefficients_Object=MibScalar
acAuxiliaryFilesFxsCoefficients=_AcAuxiliaryFilesFxsCoefficients_Object((1,3,6,1,4,1,5003,9,10,8,1,1,2,1),_AcAuxiliaryFilesFxsCoefficients_Type())
acAuxiliaryFilesFxsCoefficients.setMaxAccess(_D)
if mibBuilder.loadTexts:acAuxiliaryFilesFxsCoefficients.setStatus(_A)
class _AcAuxiliaryFilesFxoCoefficients_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_AcAuxiliaryFilesFxoCoefficients_Type.__name__=_K
_AcAuxiliaryFilesFxoCoefficients_Object=MibScalar
acAuxiliaryFilesFxoCoefficients=_AcAuxiliaryFilesFxoCoefficients_Object((1,3,6,1,4,1,5003,9,10,8,1,1,2,2),_AcAuxiliaryFilesFxoCoefficients_Type())
acAuxiliaryFilesFxoCoefficients.setMaxAccess(_D)
if mibBuilder.loadTexts:acAuxiliaryFilesFxoCoefficients.setStatus(_A)
_AcAnalogFxoConfig_ObjectIdentity=ObjectIdentity
acAnalogFxoConfig=_AcAnalogFxoConfig_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,1,2))
_AcAnalogFxo_ObjectIdentity=ObjectIdentity
acAnalogFxo=_AcAnalogFxo_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,1,2,1))
class _AcAnalogFxoFarEndDisconnectType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AcAnalogFxoFarEndDisconnectType_Type.__name__=_E
_AcAnalogFxoFarEndDisconnectType_Object=MibScalar
acAnalogFxoFarEndDisconnectType=_AcAnalogFxoFarEndDisconnectType_Object((1,3,6,1,4,1,5003,9,10,8,1,2,1,1),_AcAnalogFxoFarEndDisconnectType_Type())
acAnalogFxoFarEndDisconnectType.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxoFarEndDisconnectType.setStatus(_A)
class _AcAnalogFxoCountryCoefficients_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(66,70)));namedValues=NamedValues(*((_L,66),(_M,70)))
_AcAnalogFxoCountryCoefficients_Type.__name__=_B
_AcAnalogFxoCountryCoefficients_Object=MibScalar
acAnalogFxoCountryCoefficients=_AcAnalogFxoCountryCoefficients_Object((1,3,6,1,4,1,5003,9,10,8,1,2,1,2),_AcAnalogFxoCountryCoefficients_Type())
acAnalogFxoCountryCoefficients.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxoCountryCoefficients.setStatus(_A)
class _AcAnalogFxoDCRemover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AcAnalogFxoDCRemover_Type.__name__=_B
_AcAnalogFxoDCRemover_Object=MibScalar
acAnalogFxoDCRemover=_AcAnalogFxoDCRemover_Object((1,3,6,1,4,1,5003,9,10,8,1,2,1,3),_AcAnalogFxoDCRemover_Type())
acAnalogFxoDCRemover.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxoDCRemover.setStatus(_A)
class _AcAnalogFxoDefaultLinePolarityState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('positive-polarity',0),('negative-polarity',1),('polarity-auto-detect',2)))
_AcAnalogFxoDefaultLinePolarityState_Type.__name__=_B
_AcAnalogFxoDefaultLinePolarityState_Object=MibScalar
acAnalogFxoDefaultLinePolarityState=_AcAnalogFxoDefaultLinePolarityState_Object((1,3,6,1,4,1,5003,9,10,8,1,2,1,4),_AcAnalogFxoDefaultLinePolarityState_Type())
acAnalogFxoDefaultLinePolarityState.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxoDefaultLinePolarityState.setStatus(_A)
class _AcAnalogFxoTxGainControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-15,12))
_AcAnalogFxoTxGainControl_Type.__name__=_B
_AcAnalogFxoTxGainControl_Object=MibScalar
acAnalogFxoTxGainControl=_AcAnalogFxoTxGainControl_Object((1,3,6,1,4,1,5003,9,10,8,1,2,1,5),_AcAnalogFxoTxGainControl_Type())
acAnalogFxoTxGainControl.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxoTxGainControl.setStatus(_A)
class _AcAnalogFxoRxGainControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-15,12))
_AcAnalogFxoRxGainControl_Type.__name__=_B
_AcAnalogFxoRxGainControl_Object=MibScalar
acAnalogFxoRxGainControl=_AcAnalogFxoRxGainControl_Object((1,3,6,1,4,1,5003,9,10,8,1,2,1,6),_AcAnalogFxoRxGainControl_Type())
acAnalogFxoRxGainControl.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxoRxGainControl.setStatus(_A)
_AcAnalogFxoFarEndDisconnectToneTable_Object=MibTable
acAnalogFxoFarEndDisconnectToneTable=_AcAnalogFxoFarEndDisconnectToneTable_Object((1,3,6,1,4,1,5003,9,10,8,1,2,1,21))
if mibBuilder.loadTexts:acAnalogFxoFarEndDisconnectToneTable.setStatus(_A)
_AcAnalogFxoFarEndDisconnectToneEntry_Object=MibTableRow
acAnalogFxoFarEndDisconnectToneEntry=_AcAnalogFxoFarEndDisconnectToneEntry_Object((1,3,6,1,4,1,5003,9,10,8,1,2,1,21,1))
acAnalogFxoFarEndDisconnectToneEntry.setIndexNames((0,_H,_P))
if mibBuilder.loadTexts:acAnalogFxoFarEndDisconnectToneEntry.setStatus(_A)
class _AcAnalogFxoFarEndDisconnectToneRowStatus_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AcAnalogFxoFarEndDisconnectToneRowStatus_Type.__name__=_E
_AcAnalogFxoFarEndDisconnectToneRowStatus_Object=MibTableColumn
acAnalogFxoFarEndDisconnectToneRowStatus=_AcAnalogFxoFarEndDisconnectToneRowStatus_Object((1,3,6,1,4,1,5003,9,10,8,1,2,1,21,1,1),_AcAnalogFxoFarEndDisconnectToneRowStatus_Type())
acAnalogFxoFarEndDisconnectToneRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxoFarEndDisconnectToneRowStatus.setStatus(_A)
class _AcAnalogFxoFarEndDisconnectToneAction_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_AcAnalogFxoFarEndDisconnectToneAction_Type.__name__=_E
_AcAnalogFxoFarEndDisconnectToneAction_Object=MibTableColumn
acAnalogFxoFarEndDisconnectToneAction=_AcAnalogFxoFarEndDisconnectToneAction_Object((1,3,6,1,4,1,5003,9,10,8,1,2,1,21,1,2),_AcAnalogFxoFarEndDisconnectToneAction_Type())
acAnalogFxoFarEndDisconnectToneAction.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxoFarEndDisconnectToneAction.setStatus(_A)
class _AcAnalogFxoFarEndDisconnectToneActionResult_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_AcAnalogFxoFarEndDisconnectToneActionResult_Type.__name__=_E
_AcAnalogFxoFarEndDisconnectToneActionResult_Object=MibTableColumn
acAnalogFxoFarEndDisconnectToneActionResult=_AcAnalogFxoFarEndDisconnectToneActionResult_Object((1,3,6,1,4,1,5003,9,10,8,1,2,1,21,1,3),_AcAnalogFxoFarEndDisconnectToneActionResult_Type())
acAnalogFxoFarEndDisconnectToneActionResult.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxoFarEndDisconnectToneActionResult.setStatus(_A)
class _AcAnalogFxoFarEndDisconnectToneIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_AcAnalogFxoFarEndDisconnectToneIndex_Type.__name__=_E
_AcAnalogFxoFarEndDisconnectToneIndex_Object=MibTableColumn
acAnalogFxoFarEndDisconnectToneIndex=_AcAnalogFxoFarEndDisconnectToneIndex_Object((1,3,6,1,4,1,5003,9,10,8,1,2,1,21,1,4),_AcAnalogFxoFarEndDisconnectToneIndex_Type())
acAnalogFxoFarEndDisconnectToneIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxoFarEndDisconnectToneIndex.setStatus(_A)
class _AcAnalogFxoFarEndDisconnectToneType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,298,299)));namedValues=NamedValues(*(('acNullTone',0),('acDialTone',1),('acRingingTone',2),('acBusyTone',3),('acCongestionTone',4),('acSpecialInfoTone',5),('acWarningTone',6),('acReorderTone',7),('acConfirmationTone',8),('acWaitingTone',9),('acCallProgressCo1Tone',10),('acCallProgressCo2Tone',11),('acOldMilliwattTone',12),('acNewMilliwattTone',13),('acMessageWaitingIndicator',14),('acStutterDialTone',15),('acStutterOffHookWarningTone',16),('acWaitingTone1',17),('acComfortTone',18),('acNAKTone',19),('acVacantNumberTone',20),('acSpecialConditionTone',21),('acDialTone2',22),('acOnHoldTone',23),('acCallTransferDialTone',24),('acCallForwardTone',25),('acCreditCardServiceTone',26),('acSpecialRecallDialTone',27),('acAlertingTone',28),('acNetworkCongestionTone',29),('acWaitingTone2',30),('acWaitingTone3',31),('acWaitingTone4',32),('acConfEnterTone',33),('acConfExitTone',34),('acConfLockTone',35),('acConfUnlockTone',36),('acConfTimeLimitTone',37),('acPayphoneRecognitionTone',38),('acCallerWaitingTone',39),('acCNGFaxTone',40),('acPrecConfNotifyType',41),('acPresConfNotifyType',42),('acPrecPreemptType',43),('acPrecRTType',44),('acR15reqOfANItone',45),('acCo1Tone',200),('acCo2Tone',201),('acPlayRecordBeepTone',202),('acTrunkTestingTestProgressTone',203),('acTrunkTestingTestTone',204),('acTrunkTestingGuardTone',205),('acFSKTrunkTestingTone',206),('acGeneralTrunkTestingTone1',207),('acGeneralTrunkTestingTone2',208),('acGeneralTrunkTestingTone3',209),('acSpecialInfoToneFirst',210),('acSpecialInfoToneSecond',211),('acSpecialInfoToneThird',212),('acTTYTone',213),('acTT904ContinuityTone',214),('acTTMilliwattLossMeasureTone',215),('acCarrierDialTone',216),('acCarrierAnswerTone',217),('acCarrierChargingTone',218),('acLongDistanceIndicatorTone',219),('acSTUModemFirstTone',298),('acSTUModemSecondTone',299)))
_AcAnalogFxoFarEndDisconnectToneType_Type.__name__=_B
_AcAnalogFxoFarEndDisconnectToneType_Object=MibTableColumn
acAnalogFxoFarEndDisconnectToneType=_AcAnalogFxoFarEndDisconnectToneType_Object((1,3,6,1,4,1,5003,9,10,8,1,2,1,21,1,5),_AcAnalogFxoFarEndDisconnectToneType_Type())
acAnalogFxoFarEndDisconnectToneType.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxoFarEndDisconnectToneType.setStatus(_A)
_AcAnalogFxsConfig_ObjectIdentity=ObjectIdentity
acAnalogFxsConfig=_AcAnalogFxsConfig_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,1,3))
_AcAnalogFxs_ObjectIdentity=ObjectIdentity
acAnalogFxs=_AcAnalogFxs_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,1,3,1))
class _AcAnalogFxsPolarityReversalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('soft',0),('hard',1)))
_AcAnalogFxsPolarityReversalType_Type.__name__=_B
_AcAnalogFxsPolarityReversalType_Object=MibScalar
acAnalogFxsPolarityReversalType=_AcAnalogFxsPolarityReversalType_Object((1,3,6,1,4,1,5003,9,10,8,1,3,1,1),_AcAnalogFxsPolarityReversalType_Type())
acAnalogFxsPolarityReversalType.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxsPolarityReversalType.setStatus(_A)
class _AcAnalogFxsMeteringType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('mt12kHz',0),('mt16kHz',1),('mtPolarityReversal',2)))
_AcAnalogFxsMeteringType_Type.__name__=_B
_AcAnalogFxsMeteringType_Object=MibScalar
acAnalogFxsMeteringType=_AcAnalogFxsMeteringType_Object((1,3,6,1,4,1,5003,9,10,8,1,3,1,2),_AcAnalogFxsMeteringType_Type())
acAnalogFxsMeteringType.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxsMeteringType.setStatus(_A)
class _AcAnalogFxsLifeLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('acLifeLineType-Hardware-Only',0),('acLifeLineTypeHardware-And-Link-Detection',1),('acLifeLineType-Hardware-And-Link-And-Network-Detection',2)))
_AcAnalogFxsLifeLineType_Type.__name__=_B
_AcAnalogFxsLifeLineType_Object=MibScalar
acAnalogFxsLifeLineType=_AcAnalogFxsLifeLineType_Object((1,3,6,1,4,1,5003,9,10,8,1,3,1,3),_AcAnalogFxsLifeLineType_Type())
acAnalogFxsLifeLineType.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxsLifeLineType.setStatus(_A)
class _AcAnalogFxsMinFlashHookTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,300))
_AcAnalogFxsMinFlashHookTime_Type.__name__=_E
_AcAnalogFxsMinFlashHookTime_Object=MibScalar
acAnalogFxsMinFlashHookTime=_AcAnalogFxsMinFlashHookTime_Object((1,3,6,1,4,1,5003,9,10,8,1,3,1,4),_AcAnalogFxsMinFlashHookTime_Type())
acAnalogFxsMinFlashHookTime.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxsMinFlashHookTime.setStatus(_A)
class _AcAnalogFxsCallerIDTimingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AcAnalogFxsCallerIDTimingMode_Type.__name__=_B
_AcAnalogFxsCallerIDTimingMode_Object=MibScalar
acAnalogFxsCallerIDTimingMode=_AcAnalogFxsCallerIDTimingMode_Object((1,3,6,1,4,1,5003,9,10,8,1,3,1,5),_AcAnalogFxsCallerIDTimingMode_Type())
acAnalogFxsCallerIDTimingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxsCallerIDTimingMode.setStatus(_A)
class _AcAnalogFxsBellcoreCallerIDTypeOneSubStandard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('bellcore-Between-Rings',0),('bellcore-Not-Ring-Related',1),('bellcore-Before-Ring-RP-AS',2)))
_AcAnalogFxsBellcoreCallerIDTypeOneSubStandard_Type.__name__=_B
_AcAnalogFxsBellcoreCallerIDTypeOneSubStandard_Object=MibScalar
acAnalogFxsBellcoreCallerIDTypeOneSubStandard=_AcAnalogFxsBellcoreCallerIDTypeOneSubStandard_Object((1,3,6,1,4,1,5003,9,10,8,1,3,1,6),_AcAnalogFxsBellcoreCallerIDTypeOneSubStandard_Type())
acAnalogFxsBellcoreCallerIDTypeOneSubStandard.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxsBellcoreCallerIDTypeOneSubStandard.setStatus(_A)
class _AcAnalogFxsETSICallerIDTypeOneSubStandard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('eTSI-Between-Rings',0),('eTSI-Before-Ring-DT-AS',1),('eTSI-Before-Ring-RP-AS',2),('eTSI-Before-Ring-LR-DT-AS',3),('eTSI-Not-Ring-Related-DT-AS',4),('eTSI-Not-Ring-Related-RP-AS',5),('eTSI-Not-Ring-Related-LR-DT-AS',6)))
_AcAnalogFxsETSICallerIDTypeOneSubStandard_Type.__name__=_B
_AcAnalogFxsETSICallerIDTypeOneSubStandard_Object=MibScalar
acAnalogFxsETSICallerIDTypeOneSubStandard=_AcAnalogFxsETSICallerIDTypeOneSubStandard_Object((1,3,6,1,4,1,5003,9,10,8,1,3,1,7),_AcAnalogFxsETSICallerIDTypeOneSubStandard_Type())
acAnalogFxsETSICallerIDTypeOneSubStandard.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxsETSICallerIDTypeOneSubStandard.setStatus(_A)
class _AcAnalogFxsETSIVMWITypeOneStandard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('eTSI-VMWI-Between-Rings',0),('eTSI-VMWI-Before-Ring-DT-AS',1),('eTSI-VMWI-Before-Ring-RP-AS',2),('eTSI-VMWI-Before-Ring-LR-DT-AS',3),('eTSI-VMWI-Not-Ring-Related-DT-AS',4),('eTSI-VMWI-Not-Ring-Related-RP-AS',5),('eTSI-VMWI-Not-Ring-Related-LR-DT-AS',6)))
_AcAnalogFxsETSIVMWITypeOneStandard_Type.__name__=_B
_AcAnalogFxsETSIVMWITypeOneStandard_Object=MibScalar
acAnalogFxsETSIVMWITypeOneStandard=_AcAnalogFxsETSIVMWITypeOneStandard_Object((1,3,6,1,4,1,5003,9,10,8,1,3,1,8),_AcAnalogFxsETSIVMWITypeOneStandard_Type())
acAnalogFxsETSIVMWITypeOneStandard.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxsETSIVMWITypeOneStandard.setStatus(_A)
class _AcAnalogFxsBellcoreVMWITypeOneStandard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('bellcore-VMWI-Between-Rings',0),('bellcore-VMWI-Not-Ring-Related',1)))
_AcAnalogFxsBellcoreVMWITypeOneStandard_Type.__name__=_B
_AcAnalogFxsBellcoreVMWITypeOneStandard_Object=MibScalar
acAnalogFxsBellcoreVMWITypeOneStandard=_AcAnalogFxsBellcoreVMWITypeOneStandard_Object((1,3,6,1,4,1,5003,9,10,8,1,3,1,9),_AcAnalogFxsBellcoreVMWITypeOneStandard_Type())
acAnalogFxsBellcoreVMWITypeOneStandard.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxsBellcoreVMWITypeOneStandard.setStatus(_A)
_AcAnalogFxsDisableAutoCalibration_Type=Unsigned32
_AcAnalogFxsDisableAutoCalibration_Object=MibScalar
acAnalogFxsDisableAutoCalibration=_AcAnalogFxsDisableAutoCalibration_Object((1,3,6,1,4,1,5003,9,10,8,1,3,1,10),_AcAnalogFxsDisableAutoCalibration_Type())
acAnalogFxsDisableAutoCalibration.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxsDisableAutoCalibration.setStatus(_A)
class _AcAnalogFxsExternalLifeLinePorts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_AcAnalogFxsExternalLifeLinePorts_Type.__name__=_E
_AcAnalogFxsExternalLifeLinePorts_Object=MibScalar
acAnalogFxsExternalLifeLinePorts=_AcAnalogFxsExternalLifeLinePorts_Object((1,3,6,1,4,1,5003,9,10,8,1,3,1,11),_AcAnalogFxsExternalLifeLinePorts_Type())
acAnalogFxsExternalLifeLinePorts.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxsExternalLifeLinePorts.setStatus(_A)
class _AcAnalogFxsCountryCoefficients_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(66,70)));namedValues=NamedValues(*((_L,66),(_M,70)))
_AcAnalogFxsCountryCoefficients_Type.__name__=_B
_AcAnalogFxsCountryCoefficients_Object=MibScalar
acAnalogFxsCountryCoefficients=_AcAnalogFxsCountryCoefficients_Object((1,3,6,1,4,1,5003,9,10,8,1,3,1,12),_AcAnalogFxsCountryCoefficients_Type())
acAnalogFxsCountryCoefficients.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxsCountryCoefficients.setStatus(_A)
class _AcAnalogFxsTTXVoltageLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2)));namedValues=NamedValues(*((_Q,-1),('ttxVoltageLevel0V',0),('ttxVoltageLevel05',1),('ttxVoltageLevel1V',2)))
_AcAnalogFxsTTXVoltageLevel_Type.__name__=_B
_AcAnalogFxsTTXVoltageLevel_Object=MibScalar
acAnalogFxsTTXVoltageLevel=_AcAnalogFxsTTXVoltageLevel_Object((1,3,6,1,4,1,5003,9,10,8,1,3,1,13),_AcAnalogFxsTTXVoltageLevel_Type())
acAnalogFxsTTXVoltageLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxsTTXVoltageLevel.setStatus(_A)
_AcAnalogEMConfig_ObjectIdentity=ObjectIdentity
acAnalogEMConfig=_AcAnalogEMConfig_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,1,4))
_AcAnalogEM_ObjectIdentity=ObjectIdentity
acAnalogEM=_AcAnalogEM_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,1,4,1))
class _AcAnalogEMVoiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('twoWire',0),('fourWire',1)))
_AcAnalogEMVoiceType_Type.__name__=_B
_AcAnalogEMVoiceType_Object=MibScalar
acAnalogEMVoiceType=_AcAnalogEMVoiceType_Object((1,3,6,1,4,1,5003,9,10,8,1,4,1,1),_AcAnalogEMVoiceType_Type())
acAnalogEMVoiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogEMVoiceType.setStatus(_A)
class _AcAnalogEMInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('signaling',0),('trunking',1)))
_AcAnalogEMInterfaceType_Type.__name__=_B
_AcAnalogEMInterfaceType_Object=MibScalar
acAnalogEMInterfaceType=_AcAnalogEMInterfaceType_Object((1,3,6,1,4,1,5003,9,10,8,1,4,1,2),_AcAnalogEMInterfaceType_Type())
acAnalogEMInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogEMInterfaceType.setStatus(_A)
class _AcAnalogEMSignalingType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_AcAnalogEMSignalingType_Type.__name__=_E
_AcAnalogEMSignalingType_Object=MibScalar
acAnalogEMSignalingType=_AcAnalogEMSignalingType_Object((1,3,6,1,4,1,5003,9,10,8,1,4,1,3),_AcAnalogEMSignalingType_Type())
acAnalogEMSignalingType.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogEMSignalingType.setStatus(_A)
class _AcAnalogEMPortRXGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AcAnalogEMPortRXGain_Type.__name__=_B
_AcAnalogEMPortRXGain_Object=MibScalar
acAnalogEMPortRXGain=_AcAnalogEMPortRXGain_Object((1,3,6,1,4,1,5003,9,10,8,1,4,1,4),_AcAnalogEMPortRXGain_Type())
acAnalogEMPortRXGain.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogEMPortRXGain.setStatus(_A)
class _AcAnalogEMPortTXGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AcAnalogEMPortTXGain_Type.__name__=_B
_AcAnalogEMPortTXGain_Object=MibScalar
acAnalogEMPortTXGain=_AcAnalogEMPortTXGain_Object((1,3,6,1,4,1,5003,9,10,8,1,4,1,5),_AcAnalogEMPortTXGain_Type())
acAnalogEMPortTXGain.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogEMPortTXGain.setStatus(_A)
class _AcAnalogEMCountryCoefficients_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_L,1)))
_AcAnalogEMCountryCoefficients_Type.__name__=_B
_AcAnalogEMCountryCoefficients_Object=MibScalar
acAnalogEMCountryCoefficients=_AcAnalogEMCountryCoefficients_Object((1,3,6,1,4,1,5003,9,10,8,1,4,1,6),_AcAnalogEMCountryCoefficients_Type())
acAnalogEMCountryCoefficients.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogEMCountryCoefficients.setStatus(_A)
class _AcAnalogEMHookDebounceTiming_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,150))
_AcAnalogEMHookDebounceTiming_Type.__name__=_E
_AcAnalogEMHookDebounceTiming_Object=MibScalar
acAnalogEMHookDebounceTiming=_AcAnalogEMHookDebounceTiming_Object((1,3,6,1,4,1,5003,9,10,8,1,4,1,7),_AcAnalogEMHookDebounceTiming_Type())
acAnalogEMHookDebounceTiming.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogEMHookDebounceTiming.setStatus(_A)
class _AcAnalogEMOffHookGlareEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AcAnalogEMOffHookGlareEnable_Type.__name__=_B
_AcAnalogEMOffHookGlareEnable_Object=MibScalar
acAnalogEMOffHookGlareEnable=_AcAnalogEMOffHookGlareEnable_Object((1,3,6,1,4,1,5003,9,10,8,1,4,1,8),_AcAnalogEMOffHookGlareEnable_Type())
acAnalogEMOffHookGlareEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogEMOffHookGlareEnable.setStatus(_A)
_AcAnalogStatus_ObjectIdentity=ObjectIdentity
acAnalogStatus=_AcAnalogStatus_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,2))
_AcAnalogStatusMisc_ObjectIdentity=ObjectIdentity
acAnalogStatusMisc=_AcAnalogStatusMisc_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,2,1))
class _AcAnalogStatusMiscFxsOrFxo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,5,6,7)));namedValues=NamedValues(*(('fXO',0),('fXS',1),('eANDm',2),('fXOandFXS',3),('fXOandFXSandEM',5),('fXOandEM',6),('fXSandEM',7)))
_AcAnalogStatusMiscFxsOrFxo_Type.__name__=_B
_AcAnalogStatusMiscFxsOrFxo_Object=MibScalar
acAnalogStatusMiscFxsOrFxo=_AcAnalogStatusMiscFxsOrFxo_Object((1,3,6,1,4,1,5003,9,10,8,2,1,1),_AcAnalogStatusMiscFxsOrFxo_Type())
acAnalogStatusMiscFxsOrFxo.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogStatusMiscFxsOrFxo.setStatus(_A)
class _AcAnalogStatusMiscBoardTemperature_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AcAnalogStatusMiscBoardTemperature_Type.__name__=_E
_AcAnalogStatusMiscBoardTemperature_Object=MibScalar
acAnalogStatusMiscBoardTemperature=_AcAnalogStatusMiscBoardTemperature_Object((1,3,6,1,4,1,5003,9,10,8,2,1,2),_AcAnalogStatusMiscBoardTemperature_Type())
acAnalogStatusMiscBoardTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogStatusMiscBoardTemperature.setStatus(_A)
class _AcAnalogStatusMiscAnalogChannelsCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_AcAnalogStatusMiscAnalogChannelsCount_Type.__name__=_E
_AcAnalogStatusMiscAnalogChannelsCount_Object=MibScalar
acAnalogStatusMiscAnalogChannelsCount=_AcAnalogStatusMiscAnalogChannelsCount_Object((1,3,6,1,4,1,5003,9,10,8,2,1,3),_AcAnalogStatusMiscAnalogChannelsCount_Type())
acAnalogStatusMiscAnalogChannelsCount.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogStatusMiscAnalogChannelsCount.setStatus(_A)
_AcAnalogFxsFxo_ObjectIdentity=ObjectIdentity
acAnalogFxsFxo=_AcAnalogFxsFxo_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,2,20))
_AcAnalogFxsFxoTable_Object=MibTable
acAnalogFxsFxoTable=_AcAnalogFxsFxoTable_Object((1,3,6,1,4,1,5003,9,10,8,2,20,1))
if mibBuilder.loadTexts:acAnalogFxsFxoTable.setStatus(_A)
_AcAnalogFxsFxoEntry_Object=MibTableRow
acAnalogFxsFxoEntry=_AcAnalogFxsFxoEntry_Object((1,3,6,1,4,1,5003,9,10,8,2,20,1,1))
acAnalogFxsFxoEntry.setIndexNames((0,_H,_R))
if mibBuilder.loadTexts:acAnalogFxsFxoEntry.setStatus(_A)
class _AcAnalogFxsFxoIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_AcAnalogFxsFxoIndex_Type.__name__=_E
_AcAnalogFxsFxoIndex_Object=MibTableColumn
acAnalogFxsFxoIndex=_AcAnalogFxsFxoIndex_Object((1,3,6,1,4,1,5003,9,10,8,2,20,1,1,1),_AcAnalogFxsFxoIndex_Type())
acAnalogFxsFxoIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acAnalogFxsFxoIndex.setStatus(_A)
class _AcAnalogFxsFxoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('fXO',0),('fXS',1),('eM',2)))
_AcAnalogFxsFxoType_Type.__name__=_B
_AcAnalogFxsFxoType_Object=MibTableColumn
acAnalogFxsFxoType=_AcAnalogFxsFxoType_Object((1,3,6,1,4,1,5003,9,10,8,2,20,1,1,2),_AcAnalogFxsFxoType_Type())
acAnalogFxsFxoType.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxsFxoType.setStatus(_A)
class _AcAnalogFxsFxoChipRevNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcAnalogFxsFxoChipRevNum_Type.__name__=_E
_AcAnalogFxsFxoChipRevNum_Object=MibTableColumn
acAnalogFxsFxoChipRevNum=_AcAnalogFxsFxoChipRevNum_Object((1,3,6,1,4,1,5003,9,10,8,2,20,1,1,3),_AcAnalogFxsFxoChipRevNum_Type())
acAnalogFxsFxoChipRevNum.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxsFxoChipRevNum.setStatus(_A)
class _AcAnalogFxsFxoHookState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_AcAnalogFxsFxoHookState_Type.__name__=_B
_AcAnalogFxsFxoHookState_Object=MibTableColumn
acAnalogFxsFxoHookState=_AcAnalogFxsFxoHookState_Object((1,3,6,1,4,1,5003,9,10,8,2,20,1,1,4),_AcAnalogFxsFxoHookState_Type())
acAnalogFxsFxoHookState.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxsFxoHookState.setStatus(_A)
_AcAnalogLegs_ObjectIdentity=ObjectIdentity
acAnalogLegs=_AcAnalogLegs_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,2,21))
_AcAnalogLegsTable_Object=MibTable
acAnalogLegsTable=_AcAnalogLegsTable_Object((1,3,6,1,4,1,5003,9,10,8,2,21,1))
if mibBuilder.loadTexts:acAnalogLegsTable.setStatus(_A)
_AcAnalogLegsEntry_Object=MibTableRow
acAnalogLegsEntry=_AcAnalogLegsEntry_Object((1,3,6,1,4,1,5003,9,10,8,2,21,1,1))
acAnalogLegsEntry.setIndexNames((0,_H,_S))
if mibBuilder.loadTexts:acAnalogLegsEntry.setStatus(_A)
class _AcAnalogLegsLegIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_AcAnalogLegsLegIndex_Type.__name__=_E
_AcAnalogLegsLegIndex_Object=MibTableColumn
acAnalogLegsLegIndex=_AcAnalogLegsLegIndex_Object((1,3,6,1,4,1,5003,9,10,8,2,21,1,1,1),_AcAnalogLegsLegIndex_Type())
acAnalogLegsLegIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acAnalogLegsLegIndex.setStatus(_A)
class _AcAnalogLegsCallIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_AcAnalogLegsCallIndex_Type.__name__=_E
_AcAnalogLegsCallIndex_Object=MibTableColumn
acAnalogLegsCallIndex=_AcAnalogLegsCallIndex_Object((1,3,6,1,4,1,5003,9,10,8,2,21,1,1,2),_AcAnalogLegsCallIndex_Type())
acAnalogLegsCallIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogLegsCallIndex.setStatus(_A)
class _AcAnalogLegsAnalogType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fxs',1),('fxo',2)))
_AcAnalogLegsAnalogType_Type.__name__=_B
_AcAnalogLegsAnalogType_Object=MibTableColumn
acAnalogLegsAnalogType=_AcAnalogLegsAnalogType_Object((1,3,6,1,4,1,5003,9,10,8,2,21,1,1,3),_AcAnalogLegsAnalogType_Type())
acAnalogLegsAnalogType.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogLegsAnalogType.setStatus(_A)
class _AcAnalogLegsEchoCanceller_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AcAnalogLegsEchoCanceller_Type.__name__=_B
_AcAnalogLegsEchoCanceller_Object=MibTableColumn
acAnalogLegsEchoCanceller=_AcAnalogLegsEchoCanceller_Object((1,3,6,1,4,1,5003,9,10,8,2,21,1,1,4),_AcAnalogLegsEchoCanceller_Type())
acAnalogLegsEchoCanceller.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogLegsEchoCanceller.setStatus(_A)
class _AcAnalogLegsHighPassFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AcAnalogLegsHighPassFilter_Type.__name__=_B
_AcAnalogLegsHighPassFilter_Object=MibTableColumn
acAnalogLegsHighPassFilter=_AcAnalogLegsHighPassFilter_Object((1,3,6,1,4,1,5003,9,10,8,2,21,1,1,5),_AcAnalogLegsHighPassFilter_Type())
acAnalogLegsHighPassFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogLegsHighPassFilter.setStatus(_A)
class _AcAnalogLegsDTMFDetection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AcAnalogLegsDTMFDetection_Type.__name__=_B
_AcAnalogLegsDTMFDetection_Object=MibTableColumn
acAnalogLegsDTMFDetection=_AcAnalogLegsDTMFDetection_Object((1,3,6,1,4,1,5003,9,10,8,2,21,1,1,6),_AcAnalogLegsDTMFDetection_Type())
acAnalogLegsDTMFDetection.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogLegsDTMFDetection.setStatus(_A)
class _AcAnalogLegsVoiceVolume_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000))
_AcAnalogLegsVoiceVolume_Type.__name__=_E
_AcAnalogLegsVoiceVolume_Object=MibTableColumn
acAnalogLegsVoiceVolume=_AcAnalogLegsVoiceVolume_Object((1,3,6,1,4,1,5003,9,10,8,2,21,1,1,7),_AcAnalogLegsVoiceVolume_Type())
acAnalogLegsVoiceVolume.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogLegsVoiceVolume.setStatus(_A)
class _AcAnalogLegsInputGain_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000))
_AcAnalogLegsInputGain_Type.__name__=_E
_AcAnalogLegsInputGain_Object=MibTableColumn
acAnalogLegsInputGain=_AcAnalogLegsInputGain_Object((1,3,6,1,4,1,5003,9,10,8,2,21,1,1,8),_AcAnalogLegsInputGain_Type())
acAnalogLegsInputGain.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogLegsInputGain.setStatus(_A)
class _AcAnalogLegsLegName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AcAnalogLegsLegName_Type.__name__=_K
_AcAnalogLegsLegName_Object=MibTableColumn
acAnalogLegsLegName=_AcAnalogLegsLegName_Object((1,3,6,1,4,1,5003,9,10,8,2,21,1,1,9),_AcAnalogLegsLegName_Type())
acAnalogLegsLegName.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogLegsLegName.setStatus(_A)
_AcAnalogAction_ObjectIdentity=ObjectIdentity
acAnalogAction=_AcAnalogAction_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,3))
_AcAnalogFxoAction_ObjectIdentity=ObjectIdentity
acAnalogFxoAction=_AcAnalogFxoAction_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,3,1))
_AcAnalogFxoLineTestTable_Object=MibTable
acAnalogFxoLineTestTable=_AcAnalogFxoLineTestTable_Object((1,3,6,1,4,1,5003,9,10,8,3,1,1))
if mibBuilder.loadTexts:acAnalogFxoLineTestTable.setStatus(_A)
_AcAnalogFxoLineTestEntry_Object=MibTableRow
acAnalogFxoLineTestEntry=_AcAnalogFxoLineTestEntry_Object((1,3,6,1,4,1,5003,9,10,8,3,1,1,1))
acAnalogFxoLineTestEntry.setIndexNames((0,_H,_T))
if mibBuilder.loadTexts:acAnalogFxoLineTestEntry.setStatus(_A)
class _AcAnalogFxoLineTestIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_AcAnalogFxoLineTestIndex_Type.__name__=_E
_AcAnalogFxoLineTestIndex_Object=MibTableColumn
acAnalogFxoLineTestIndex=_AcAnalogFxoLineTestIndex_Object((1,3,6,1,4,1,5003,9,10,8,3,1,1,1,1),_AcAnalogFxoLineTestIndex_Type())
acAnalogFxoLineTestIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acAnalogFxoLineTestIndex.setStatus(_A)
class _AcAnalogFxoLineTestActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_U,0),(_V,1),(_W,2),(_X,3)))
_AcAnalogFxoLineTestActivate_Type.__name__=_B
_AcAnalogFxoLineTestActivate_Object=MibTableColumn
acAnalogFxoLineTestActivate=_AcAnalogFxoLineTestActivate_Object((1,3,6,1,4,1,5003,9,10,8,3,1,1,1,2),_AcAnalogFxoLineTestActivate_Type())
acAnalogFxoLineTestActivate.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxoLineTestActivate.setStatus(_A)
class _AcAnalogFxoLineTestHookState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_AcAnalogFxoLineTestHookState_Type.__name__=_B
_AcAnalogFxoLineTestHookState_Object=MibTableColumn
acAnalogFxoLineTestHookState=_AcAnalogFxoLineTestHookState_Object((1,3,6,1,4,1,5003,9,10,8,3,1,1,1,3),_AcAnalogFxoLineTestHookState_Type())
acAnalogFxoLineTestHookState.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxoLineTestHookState.setStatus(_A)
class _AcAnalogFxoLineTestPolarityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_Q,3)))
_AcAnalogFxoLineTestPolarityStatus_Type.__name__=_B
_AcAnalogFxoLineTestPolarityStatus_Object=MibTableColumn
acAnalogFxoLineTestPolarityStatus=_AcAnalogFxoLineTestPolarityStatus_Object((1,3,6,1,4,1,5003,9,10,8,3,1,1,1,4),_AcAnalogFxoLineTestPolarityStatus_Type())
acAnalogFxoLineTestPolarityStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxoLineTestPolarityStatus.setStatus(_A)
class _AcAnalogFxoLineTestLineConnectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lineDisconnected',1),('lineConnected',2)))
_AcAnalogFxoLineTestLineConnectionStatus_Type.__name__=_B
_AcAnalogFxoLineTestLineConnectionStatus_Object=MibTableColumn
acAnalogFxoLineTestLineConnectionStatus=_AcAnalogFxoLineTestLineConnectionStatus_Object((1,3,6,1,4,1,5003,9,10,8,3,1,1,1,5),_AcAnalogFxoLineTestLineConnectionStatus_Type())
acAnalogFxoLineTestLineConnectionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxoLineTestLineConnectionStatus.setStatus(_A)
class _AcAnalogFxoLineTestLineCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,24))
_AcAnalogFxoLineTestLineCurrent_Type.__name__=_B
_AcAnalogFxoLineTestLineCurrent_Object=MibTableColumn
acAnalogFxoLineTestLineCurrent=_AcAnalogFxoLineTestLineCurrent_Object((1,3,6,1,4,1,5003,9,10,8,3,1,1,1,6),_AcAnalogFxoLineTestLineCurrent_Type())
acAnalogFxoLineTestLineCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxoLineTestLineCurrent.setStatus(_A)
class _AcAnalogFxoLineTestLineVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,128))
_AcAnalogFxoLineTestLineVoltage_Type.__name__=_B
_AcAnalogFxoLineTestLineVoltage_Object=MibTableColumn
acAnalogFxoLineTestLineVoltage=_AcAnalogFxoLineTestLineVoltage_Object((1,3,6,1,4,1,5003,9,10,8,3,1,1,1,7),_AcAnalogFxoLineTestLineVoltage_Type())
acAnalogFxoLineTestLineVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxoLineTestLineVoltage.setStatus(_A)
class _AcAnalogFxoLineTestRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_AcAnalogFxoLineTestRingState_Type.__name__=_B
_AcAnalogFxoLineTestRingState_Object=MibTableColumn
acAnalogFxoLineTestRingState=_AcAnalogFxoLineTestRingState_Object((1,3,6,1,4,1,5003,9,10,8,3,1,1,1,8),_AcAnalogFxoLineTestRingState_Type())
acAnalogFxoLineTestRingState.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxoLineTestRingState.setStatus(_A)
class _AcAnalogFxoLineTestLinePolarity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('positive',1),('negative',2)))
_AcAnalogFxoLineTestLinePolarity_Type.__name__=_B
_AcAnalogFxoLineTestLinePolarity_Object=MibTableColumn
acAnalogFxoLineTestLinePolarity=_AcAnalogFxoLineTestLinePolarity_Object((1,3,6,1,4,1,5003,9,10,8,3,1,1,1,9),_AcAnalogFxoLineTestLinePolarity_Type())
acAnalogFxoLineTestLinePolarity.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxoLineTestLinePolarity.setStatus(_A)
class _AcAnalogFxoLineTestMwiState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_AcAnalogFxoLineTestMwiState_Type.__name__=_B
_AcAnalogFxoLineTestMwiState_Object=MibTableColumn
acAnalogFxoLineTestMwiState=_AcAnalogFxoLineTestMwiState_Object((1,3,6,1,4,1,5003,9,10,8,3,1,1,1,10),_AcAnalogFxoLineTestMwiState_Type())
acAnalogFxoLineTestMwiState.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxoLineTestMwiState.setStatus(_A)
class _AcAnalogFxoLineTestLastCurrentDisconnectDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcAnalogFxoLineTestLastCurrentDisconnectDuration_Type.__name__=_E
_AcAnalogFxoLineTestLastCurrentDisconnectDuration_Object=MibTableColumn
acAnalogFxoLineTestLastCurrentDisconnectDuration=_AcAnalogFxoLineTestLastCurrentDisconnectDuration_Object((1,3,6,1,4,1,5003,9,10,8,3,1,1,1,11),_AcAnalogFxoLineTestLastCurrentDisconnectDuration_Type())
acAnalogFxoLineTestLastCurrentDisconnectDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxoLineTestLastCurrentDisconnectDuration.setStatus(_A)
_AcAnalogFxsAction_ObjectIdentity=ObjectIdentity
acAnalogFxsAction=_AcAnalogFxsAction_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,3,2))
_AcAnalogFxsLineTestTable_Object=MibTable
acAnalogFxsLineTestTable=_AcAnalogFxsLineTestTable_Object((1,3,6,1,4,1,5003,9,10,8,3,2,1))
if mibBuilder.loadTexts:acAnalogFxsLineTestTable.setStatus(_A)
_AcAnalogFxsLineTestEntry_Object=MibTableRow
acAnalogFxsLineTestEntry=_AcAnalogFxsLineTestEntry_Object((1,3,6,1,4,1,5003,9,10,8,3,2,1,1))
acAnalogFxsLineTestEntry.setIndexNames((0,_H,_a))
if mibBuilder.loadTexts:acAnalogFxsLineTestEntry.setStatus(_A)
class _AcAnalogFxsLineTestIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_AcAnalogFxsLineTestIndex_Type.__name__=_E
_AcAnalogFxsLineTestIndex_Object=MibTableColumn
acAnalogFxsLineTestIndex=_AcAnalogFxsLineTestIndex_Object((1,3,6,1,4,1,5003,9,10,8,3,2,1,1,1),_AcAnalogFxsLineTestIndex_Type())
acAnalogFxsLineTestIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acAnalogFxsLineTestIndex.setStatus(_A)
class _AcAnalogFxsLineTestActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_U,0),(_V,1),(_W,2),(_X,3)))
_AcAnalogFxsLineTestActivate_Type.__name__=_B
_AcAnalogFxsLineTestActivate_Object=MibTableColumn
acAnalogFxsLineTestActivate=_AcAnalogFxsLineTestActivate_Object((1,3,6,1,4,1,5003,9,10,8,3,2,1,1,2),_AcAnalogFxsLineTestActivate_Type())
acAnalogFxsLineTestActivate.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogFxsLineTestActivate.setStatus(_A)
class _AcAnalogFxsLineTestHookState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_AcAnalogFxsLineTestHookState_Type.__name__=_B
_AcAnalogFxsLineTestHookState_Object=MibTableColumn
acAnalogFxsLineTestHookState=_AcAnalogFxsLineTestHookState_Object((1,3,6,1,4,1,5003,9,10,8,3,2,1,1,3),_AcAnalogFxsLineTestHookState_Type())
acAnalogFxsLineTestHookState.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxsLineTestHookState.setStatus(_A)
class _AcAnalogFxsLineTestRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('offRingState',1),('onRingState',2)))
_AcAnalogFxsLineTestRingState_Type.__name__=_B
_AcAnalogFxsLineTestRingState_Object=MibTableColumn
acAnalogFxsLineTestRingState=_AcAnalogFxsLineTestRingState_Object((1,3,6,1,4,1,5003,9,10,8,3,2,1,1,4),_AcAnalogFxsLineTestRingState_Type())
acAnalogFxsLineTestRingState.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxsLineTestRingState.setStatus(_A)
class _AcAnalogFxsLineTestPolarityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_AcAnalogFxsLineTestPolarityStatus_Type.__name__=_B
_AcAnalogFxsLineTestPolarityStatus_Object=MibTableColumn
acAnalogFxsLineTestPolarityStatus=_AcAnalogFxsLineTestPolarityStatus_Object((1,3,6,1,4,1,5003,9,10,8,3,2,1,1,5),_AcAnalogFxsLineTestPolarityStatus_Type())
acAnalogFxsLineTestPolarityStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxsLineTestPolarityStatus.setStatus(_A)
class _AcAnalogFxsLineTestMessageWaitingIndication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noWaitingMessage',1),('waitingMessage',2)))
_AcAnalogFxsLineTestMessageWaitingIndication_Type.__name__=_B
_AcAnalogFxsLineTestMessageWaitingIndication_Object=MibTableColumn
acAnalogFxsLineTestMessageWaitingIndication=_AcAnalogFxsLineTestMessageWaitingIndication_Object((1,3,6,1,4,1,5003,9,10,8,3,2,1,1,6),_AcAnalogFxsLineTestMessageWaitingIndication_Type())
acAnalogFxsLineTestMessageWaitingIndication.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxsLineTestMessageWaitingIndication.setStatus(_A)
class _AcAnalogFxsLineTestLineCurrentReading_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3000))
_AcAnalogFxsLineTestLineCurrentReading_Type.__name__=_E
_AcAnalogFxsLineTestLineCurrentReading_Object=MibTableColumn
acAnalogFxsLineTestLineCurrentReading=_AcAnalogFxsLineTestLineCurrentReading_Object((1,3,6,1,4,1,5003,9,10,8,3,2,1,1,7),_AcAnalogFxsLineTestLineCurrentReading_Type())
acAnalogFxsLineTestLineCurrentReading.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxsLineTestLineCurrentReading.setStatus(_J)
class _AcAnalogFxsLineTestLineVoltageReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-6000,6000))
_AcAnalogFxsLineTestLineVoltageReading_Type.__name__=_B
_AcAnalogFxsLineTestLineVoltageReading_Object=MibTableColumn
acAnalogFxsLineTestLineVoltageReading=_AcAnalogFxsLineTestLineVoltageReading_Object((1,3,6,1,4,1,5003,9,10,8,3,2,1,1,8),_AcAnalogFxsLineTestLineVoltageReading_Type())
acAnalogFxsLineTestLineVoltageReading.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxsLineTestLineVoltageReading.setStatus(_J)
class _AcAnalogFxsLineTestAnalogVoltageReading_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,340))
_AcAnalogFxsLineTestAnalogVoltageReading_Type.__name__=_E
_AcAnalogFxsLineTestAnalogVoltageReading_Object=MibTableColumn
acAnalogFxsLineTestAnalogVoltageReading=_AcAnalogFxsLineTestAnalogVoltageReading_Object((1,3,6,1,4,1,5003,9,10,8,3,2,1,1,9),_AcAnalogFxsLineTestAnalogVoltageReading_Type())
acAnalogFxsLineTestAnalogVoltageReading.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxsLineTestAnalogVoltageReading.setStatus(_J)
class _AcAnalogFxsLineTestRingVoltageReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-13000,13000))
_AcAnalogFxsLineTestRingVoltageReading_Type.__name__=_B
_AcAnalogFxsLineTestRingVoltageReading_Object=MibTableColumn
acAnalogFxsLineTestRingVoltageReading=_AcAnalogFxsLineTestRingVoltageReading_Object((1,3,6,1,4,1,5003,9,10,8,3,2,1,1,10),_AcAnalogFxsLineTestRingVoltageReading_Type())
acAnalogFxsLineTestRingVoltageReading.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxsLineTestRingVoltageReading.setStatus(_J)
class _AcAnalogFxsLineTestLongLineCurrentReading_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4000))
_AcAnalogFxsLineTestLongLineCurrentReading_Type.__name__=_E
_AcAnalogFxsLineTestLongLineCurrentReading_Object=MibTableColumn
acAnalogFxsLineTestLongLineCurrentReading=_AcAnalogFxsLineTestLongLineCurrentReading_Object((1,3,6,1,4,1,5003,9,10,8,3,2,1,1,11),_AcAnalogFxsLineTestLongLineCurrentReading_Type())
acAnalogFxsLineTestLongLineCurrentReading.setMaxAccess(_D)
if mibBuilder.loadTexts:acAnalogFxsLineTestLongLineCurrentReading.setStatus(_J)
_AcAnalogCommonAction_ObjectIdentity=ObjectIdentity
acAnalogCommonAction=_AcAnalogCommonAction_ObjectIdentity((1,3,6,1,4,1,5003,9,10,8,3,3))
_AcAnalogCommonChannelTable_Object=MibTable
acAnalogCommonChannelTable=_AcAnalogCommonChannelTable_Object((1,3,6,1,4,1,5003,9,10,8,3,3,1))
if mibBuilder.loadTexts:acAnalogCommonChannelTable.setStatus(_A)
_AcAnalogCommonChannelEntry_Object=MibTableRow
acAnalogCommonChannelEntry=_AcAnalogCommonChannelEntry_Object((1,3,6,1,4,1,5003,9,10,8,3,3,1,1))
acAnalogCommonChannelEntry.setIndexNames((0,_H,_b))
if mibBuilder.loadTexts:acAnalogCommonChannelEntry.setStatus(_A)
class _AcAnalogCommonChannelIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_AcAnalogCommonChannelIndex_Type.__name__=_E
_AcAnalogCommonChannelIndex_Object=MibTableColumn
acAnalogCommonChannelIndex=_AcAnalogCommonChannelIndex_Object((1,3,6,1,4,1,5003,9,10,8,3,3,1,1,1),_AcAnalogCommonChannelIndex_Type())
acAnalogCommonChannelIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acAnalogCommonChannelIndex.setStatus(_A)
class _AcAnalogCommonChannelAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noAction',0),('reset',1)))
_AcAnalogCommonChannelAction_Type.__name__=_B
_AcAnalogCommonChannelAction_Object=MibTableColumn
acAnalogCommonChannelAction=_AcAnalogCommonChannelAction_Object((1,3,6,1,4,1,5003,9,10,8,3,3,1,1,2),_AcAnalogCommonChannelAction_Type())
acAnalogCommonChannelAction.setMaxAccess(_C)
if mibBuilder.loadTexts:acAnalogCommonChannelAction.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'acAnalog':acAnalog,'acAnalogConfiguration':acAnalogConfiguration,'acAnalogConfig':acAnalogConfig,'acAnalogMisc':acAnalogMisc,'acAnalogMiscCurrentDisconnectDuration':acAnalogMiscCurrentDisconnectDuration,'acAnalogMiscFlashHookPeriod':acAnalogMiscFlashHookPeriod,'acAnalogMiscGroundKeyDetection':acAnalogMiscGroundKeyDetection,'acAuxiliaryFiles':acAuxiliaryFiles,'acAuxiliaryFilesFxsCoefficients':acAuxiliaryFilesFxsCoefficients,'acAuxiliaryFilesFxoCoefficients':acAuxiliaryFilesFxoCoefficients,'acAnalogFxoConfig':acAnalogFxoConfig,'acAnalogFxo':acAnalogFxo,'acAnalogFxoFarEndDisconnectType':acAnalogFxoFarEndDisconnectType,'acAnalogFxoCountryCoefficients':acAnalogFxoCountryCoefficients,'acAnalogFxoDCRemover':acAnalogFxoDCRemover,'acAnalogFxoDefaultLinePolarityState':acAnalogFxoDefaultLinePolarityState,'acAnalogFxoTxGainControl':acAnalogFxoTxGainControl,'acAnalogFxoRxGainControl':acAnalogFxoRxGainControl,'acAnalogFxoFarEndDisconnectToneTable':acAnalogFxoFarEndDisconnectToneTable,'acAnalogFxoFarEndDisconnectToneEntry':acAnalogFxoFarEndDisconnectToneEntry,'acAnalogFxoFarEndDisconnectToneRowStatus':acAnalogFxoFarEndDisconnectToneRowStatus,'acAnalogFxoFarEndDisconnectToneAction':acAnalogFxoFarEndDisconnectToneAction,'acAnalogFxoFarEndDisconnectToneActionResult':acAnalogFxoFarEndDisconnectToneActionResult,_P:acAnalogFxoFarEndDisconnectToneIndex,'acAnalogFxoFarEndDisconnectToneType':acAnalogFxoFarEndDisconnectToneType,'acAnalogFxsConfig':acAnalogFxsConfig,'acAnalogFxs':acAnalogFxs,'acAnalogFxsPolarityReversalType':acAnalogFxsPolarityReversalType,'acAnalogFxsMeteringType':acAnalogFxsMeteringType,'acAnalogFxsLifeLineType':acAnalogFxsLifeLineType,'acAnalogFxsMinFlashHookTime':acAnalogFxsMinFlashHookTime,'acAnalogFxsCallerIDTimingMode':acAnalogFxsCallerIDTimingMode,'acAnalogFxsBellcoreCallerIDTypeOneSubStandard':acAnalogFxsBellcoreCallerIDTypeOneSubStandard,'acAnalogFxsETSICallerIDTypeOneSubStandard':acAnalogFxsETSICallerIDTypeOneSubStandard,'acAnalogFxsETSIVMWITypeOneStandard':acAnalogFxsETSIVMWITypeOneStandard,'acAnalogFxsBellcoreVMWITypeOneStandard':acAnalogFxsBellcoreVMWITypeOneStandard,'acAnalogFxsDisableAutoCalibration':acAnalogFxsDisableAutoCalibration,'acAnalogFxsExternalLifeLinePorts':acAnalogFxsExternalLifeLinePorts,'acAnalogFxsCountryCoefficients':acAnalogFxsCountryCoefficients,'acAnalogFxsTTXVoltageLevel':acAnalogFxsTTXVoltageLevel,'acAnalogEMConfig':acAnalogEMConfig,'acAnalogEM':acAnalogEM,'acAnalogEMVoiceType':acAnalogEMVoiceType,'acAnalogEMInterfaceType':acAnalogEMInterfaceType,'acAnalogEMSignalingType':acAnalogEMSignalingType,'acAnalogEMPortRXGain':acAnalogEMPortRXGain,'acAnalogEMPortTXGain':acAnalogEMPortTXGain,'acAnalogEMCountryCoefficients':acAnalogEMCountryCoefficients,'acAnalogEMHookDebounceTiming':acAnalogEMHookDebounceTiming,'acAnalogEMOffHookGlareEnable':acAnalogEMOffHookGlareEnable,'acAnalogStatus':acAnalogStatus,'acAnalogStatusMisc':acAnalogStatusMisc,'acAnalogStatusMiscFxsOrFxo':acAnalogStatusMiscFxsOrFxo,'acAnalogStatusMiscBoardTemperature':acAnalogStatusMiscBoardTemperature,'acAnalogStatusMiscAnalogChannelsCount':acAnalogStatusMiscAnalogChannelsCount,'acAnalogFxsFxo':acAnalogFxsFxo,'acAnalogFxsFxoTable':acAnalogFxsFxoTable,'acAnalogFxsFxoEntry':acAnalogFxsFxoEntry,_R:acAnalogFxsFxoIndex,'acAnalogFxsFxoType':acAnalogFxsFxoType,'acAnalogFxsFxoChipRevNum':acAnalogFxsFxoChipRevNum,'acAnalogFxsFxoHookState':acAnalogFxsFxoHookState,'acAnalogLegs':acAnalogLegs,'acAnalogLegsTable':acAnalogLegsTable,'acAnalogLegsEntry':acAnalogLegsEntry,_S:acAnalogLegsLegIndex,'acAnalogLegsCallIndex':acAnalogLegsCallIndex,'acAnalogLegsAnalogType':acAnalogLegsAnalogType,'acAnalogLegsEchoCanceller':acAnalogLegsEchoCanceller,'acAnalogLegsHighPassFilter':acAnalogLegsHighPassFilter,'acAnalogLegsDTMFDetection':acAnalogLegsDTMFDetection,'acAnalogLegsVoiceVolume':acAnalogLegsVoiceVolume,'acAnalogLegsInputGain':acAnalogLegsInputGain,'acAnalogLegsLegName':acAnalogLegsLegName,'acAnalogAction':acAnalogAction,'acAnalogFxoAction':acAnalogFxoAction,'acAnalogFxoLineTestTable':acAnalogFxoLineTestTable,'acAnalogFxoLineTestEntry':acAnalogFxoLineTestEntry,_T:acAnalogFxoLineTestIndex,'acAnalogFxoLineTestActivate':acAnalogFxoLineTestActivate,'acAnalogFxoLineTestHookState':acAnalogFxoLineTestHookState,'acAnalogFxoLineTestPolarityStatus':acAnalogFxoLineTestPolarityStatus,'acAnalogFxoLineTestLineConnectionStatus':acAnalogFxoLineTestLineConnectionStatus,'acAnalogFxoLineTestLineCurrent':acAnalogFxoLineTestLineCurrent,'acAnalogFxoLineTestLineVoltage':acAnalogFxoLineTestLineVoltage,'acAnalogFxoLineTestRingState':acAnalogFxoLineTestRingState,'acAnalogFxoLineTestLinePolarity':acAnalogFxoLineTestLinePolarity,'acAnalogFxoLineTestMwiState':acAnalogFxoLineTestMwiState,'acAnalogFxoLineTestLastCurrentDisconnectDuration':acAnalogFxoLineTestLastCurrentDisconnectDuration,'acAnalogFxsAction':acAnalogFxsAction,'acAnalogFxsLineTestTable':acAnalogFxsLineTestTable,'acAnalogFxsLineTestEntry':acAnalogFxsLineTestEntry,_a:acAnalogFxsLineTestIndex,'acAnalogFxsLineTestActivate':acAnalogFxsLineTestActivate,'acAnalogFxsLineTestHookState':acAnalogFxsLineTestHookState,'acAnalogFxsLineTestRingState':acAnalogFxsLineTestRingState,'acAnalogFxsLineTestPolarityStatus':acAnalogFxsLineTestPolarityStatus,'acAnalogFxsLineTestMessageWaitingIndication':acAnalogFxsLineTestMessageWaitingIndication,'acAnalogFxsLineTestLineCurrentReading':acAnalogFxsLineTestLineCurrentReading,'acAnalogFxsLineTestLineVoltageReading':acAnalogFxsLineTestLineVoltageReading,'acAnalogFxsLineTestAnalogVoltageReading':acAnalogFxsLineTestAnalogVoltageReading,'acAnalogFxsLineTestRingVoltageReading':acAnalogFxsLineTestRingVoltageReading,'acAnalogFxsLineTestLongLineCurrentReading':acAnalogFxsLineTestLongLineCurrentReading,'acAnalogCommonAction':acAnalogCommonAction,'acAnalogCommonChannelTable':acAnalogCommonChannelTable,'acAnalogCommonChannelEntry':acAnalogCommonChannelEntry,_b:acAnalogCommonChannelIndex,'acAnalogCommonChannelAction':acAnalogCommonChannelAction})