_f='npIoTrapMemo'
_e='npIoTrapLevelIn'
_d='npIoTrapLineN'
_c='npThermoTrapMemo'
_b='npThermoTrapHigh'
_a='npThermoTrapLow'
_Z='npThermoTrapStatus'
_Y='npThermoTrapValue'
_X='npThermoTrapSensorN'
_W='npRelHumSafeRangeLow'
_V='npRelHumSafeRangeHigh'
_U='npRelHumSensorValueH'
_T='npRelHumSensorStatusH'
_S='npSmokeTrapMemo'
_R='npSmokeTrapStatus'
_Q='npSmokeTrapSensorN'
_P='npGsmStrength'
_O='npGsmRegistration'
_N='npGsmFailed'
_M='npIoLineN'
_L='npThermoSensorN'
_K='npSmokeSensorN'
_J='npPwrChannelN'
_I='npRelayN'
_H='ok'
_G='off'
_F='failed'
_E='read-write'
_D='DKSF-PWR-OLD-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
netPing8Pwr=ModuleIdentity((1,3,6,1,4,1,25728,48))
if mibBuilder.loadTexts:netPing8Pwr.setRevisions(('2015-08-13 00:00','2015-06-18 00:00','2015-05-28 00:00','2015-05-06 00:00','2015-03-26 00:00','2013-11-01 00:00','2013-04-11 00:00','2012-05-31 00:00','2012-04-17 00:00','2012-03-23 00:00','2011-09-23 00:00','2011-03-24 00:00','2010-10-14 00:00','2010-09-20 00:00','2010-05-31 00:00','2010-04-14 00:00'))
_Lightcom_ObjectIdentity=ObjectIdentity
lightcom=_Lightcom_ObjectIdentity((1,3,6,1,4,1,25728))
_NpReboot_ObjectIdentity=ObjectIdentity
npReboot=_NpReboot_ObjectIdentity((1,3,6,1,4,1,25728,911))
_NpSoftReboot_Type=Integer32
_NpSoftReboot_Object=MibScalar
npSoftReboot=_NpSoftReboot_Object((1,3,6,1,4,1,25728,911,1),_NpSoftReboot_Type())
npSoftReboot.setMaxAccess(_E)
if mibBuilder.loadTexts:npSoftReboot.setStatus(_A)
_NpResetStack_Type=Integer32
_NpResetStack_Object=MibScalar
npResetStack=_NpResetStack_Object((1,3,6,1,4,1,25728,911,2),_NpResetStack_Type())
npResetStack.setMaxAccess(_E)
if mibBuilder.loadTexts:npResetStack.setStatus(_A)
_NpForcedReboot_Type=Integer32
_NpForcedReboot_Object=MibScalar
npForcedReboot=_NpForcedReboot_Object((1,3,6,1,4,1,25728,911,3),_NpForcedReboot_Type())
npForcedReboot.setMaxAccess(_E)
if mibBuilder.loadTexts:npForcedReboot.setStatus(_A)
_NpGsm_ObjectIdentity=ObjectIdentity
npGsm=_NpGsm_ObjectIdentity((1,3,6,1,4,1,25728,3800))
_NpGsmInfo_ObjectIdentity=ObjectIdentity
npGsmInfo=_NpGsmInfo_ObjectIdentity((1,3,6,1,4,1,25728,3800,1))
class _NpGsmFailed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_F,1),('fatalError',2)))
_NpGsmFailed_Type.__name__=_C
_NpGsmFailed_Object=MibScalar
npGsmFailed=_NpGsmFailed_Object((1,3,6,1,4,1,25728,3800,1,1),_NpGsmFailed_Type())
npGsmFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:npGsmFailed.setStatus(_A)
class _NpGsmRegistration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,255)));namedValues=NamedValues(*(('impossible',0),('homeNetwork',1),('searching',2),('denied',3),('unknown',4),('roaming',5),('infoUpdate',255)))
_NpGsmRegistration_Type.__name__=_C
_NpGsmRegistration_Object=MibScalar
npGsmRegistration=_NpGsmRegistration_Object((1,3,6,1,4,1,25728,3800,1,2),_NpGsmRegistration_Type())
npGsmRegistration.setMaxAccess(_B)
if mibBuilder.loadTexts:npGsmRegistration.setStatus(_A)
class _NpGsmStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NpGsmStrength_Type.__name__=_C
_NpGsmStrength_Object=MibScalar
npGsmStrength=_NpGsmStrength_Object((1,3,6,1,4,1,25728,3800,1,3),_NpGsmStrength_Type())
npGsmStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:npGsmStrength.setStatus(_A)
_NpGsmSendSms_Type=DisplayString
_NpGsmSendSms_Object=MibScalar
npGsmSendSms=_NpGsmSendSms_Object((1,3,6,1,4,1,25728,3800,1,9),_NpGsmSendSms_Type())
npGsmSendSms.setMaxAccess(_E)
if mibBuilder.loadTexts:npGsmSendSms.setStatus(_A)
_NpGsmTraps_ObjectIdentity=ObjectIdentity
npGsmTraps=_NpGsmTraps_ObjectIdentity((1,3,6,1,4,1,25728,3800,2))
_NpGsmTrapPrefix_ObjectIdentity=ObjectIdentity
npGsmTrapPrefix=_NpGsmTrapPrefix_ObjectIdentity((1,3,6,1,4,1,25728,3800,2,0))
_NpBattery_ObjectIdentity=ObjectIdentity
npBattery=_NpBattery_ObjectIdentity((1,3,6,1,4,1,25728,3900))
_NpBatteryInfo_ObjectIdentity=ObjectIdentity
npBatteryInfo=_NpBatteryInfo_ObjectIdentity((1,3,6,1,4,1,25728,3900,1))
class _NpBatteryPok_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('batteryPower',0),('externalPower',1)))
_NpBatteryPok_Type.__name__=_C
_NpBatteryPok_Object=MibScalar
npBatteryPok=_NpBatteryPok_Object((1,3,6,1,4,1,25728,3900,1,1),_NpBatteryPok_Type())
npBatteryPok.setMaxAccess(_B)
if mibBuilder.loadTexts:npBatteryPok.setStatus(_A)
class _NpBatteryLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NpBatteryLevel_Type.__name__=_C
_NpBatteryLevel_Object=MibScalar
npBatteryLevel=_NpBatteryLevel_Object((1,3,6,1,4,1,25728,3900,1,2),_NpBatteryLevel_Type())
npBatteryLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:npBatteryLevel.setStatus(_A)
class _NpBatteryChg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('batteryChargingSuspended',0),('batteryFastCharging',1)))
_NpBatteryChg_Type.__name__=_C
_NpBatteryChg_Object=MibScalar
npBatteryChg=_NpBatteryChg_Object((1,3,6,1,4,1,25728,3900,1,3),_NpBatteryChg_Type())
npBatteryChg.setMaxAccess(_B)
if mibBuilder.loadTexts:npBatteryChg.setStatus(_A)
_NpRelay_ObjectIdentity=ObjectIdentity
npRelay=_NpRelay_ObjectIdentity((1,3,6,1,4,1,25728,5500))
_NpRelayTable_Object=MibTable
npRelayTable=_NpRelayTable_Object((1,3,6,1,4,1,25728,5500,5))
if mibBuilder.loadTexts:npRelayTable.setStatus(_A)
_NpRelayEntry_Object=MibTableRow
npRelayEntry=_NpRelayEntry_Object((1,3,6,1,4,1,25728,5500,5,1))
npRelayEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:npRelayEntry.setStatus(_A)
class _NpRelayN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NpRelayN_Type.__name__=_C
_NpRelayN_Object=MibTableColumn
npRelayN=_NpRelayN_Object((1,3,6,1,4,1,25728,5500,5,1,1),_NpRelayN_Type())
npRelayN.setMaxAccess(_B)
if mibBuilder.loadTexts:npRelayN.setStatus(_A)
class _NpRelayMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3,4,5)));namedValues=NamedValues(*(('flip',-1),(_G,0),('on',1),('watchdog',2),('schedule',3),('scheduleAndWatchdog',4),('logic',5)))
_NpRelayMode_Type.__name__=_C
_NpRelayMode_Object=MibTableColumn
npRelayMode=_NpRelayMode_Object((1,3,6,1,4,1,25728,5500,5,1,2),_NpRelayMode_Type())
npRelayMode.setMaxAccess(_E)
if mibBuilder.loadTexts:npRelayMode.setStatus(_A)
_NpRelayStartReset_Type=Integer32
_NpRelayStartReset_Object=MibTableColumn
npRelayStartReset=_NpRelayStartReset_Object((1,3,6,1,4,1,25728,5500,5,1,3),_NpRelayStartReset_Type())
npRelayStartReset.setMaxAccess(_E)
if mibBuilder.loadTexts:npRelayStartReset.setStatus(_A)
_NpRelayMemo_Type=DisplayString
_NpRelayMemo_Object=MibTableColumn
npRelayMemo=_NpRelayMemo_Object((1,3,6,1,4,1,25728,5500,5,1,6),_NpRelayMemo_Type())
npRelayMemo.setMaxAccess(_B)
if mibBuilder.loadTexts:npRelayMemo.setStatus(_A)
class _NpRelayFlip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-1));namedValues=NamedValues(('flip',-1))
_NpRelayFlip_Type.__name__=_C
_NpRelayFlip_Object=MibTableColumn
npRelayFlip=_NpRelayFlip_Object((1,3,6,1,4,1,25728,5500,5,1,14),_NpRelayFlip_Type())
npRelayFlip.setMaxAccess(_B)
if mibBuilder.loadTexts:npRelayFlip.setStatus(_A)
class _NpRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('on',1)))
_NpRelayState_Type.__name__=_C
_NpRelayState_Object=MibTableColumn
npRelayState=_NpRelayState_Object((1,3,6,1,4,1,25728,5500,5,1,15),_NpRelayState_Type())
npRelayState.setMaxAccess(_B)
if mibBuilder.loadTexts:npRelayState.setStatus(_A)
class _NpRelayPowered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_NpRelayPowered_Type.__name__=_C
_NpRelayPowered_Object=MibTableColumn
npRelayPowered=_NpRelayPowered_Object((1,3,6,1,4,1,25728,5500,5,1,16),_NpRelayPowered_Type())
npRelayPowered.setMaxAccess(_B)
if mibBuilder.loadTexts:npRelayPowered.setStatus(_A)
_NpPwr_ObjectIdentity=ObjectIdentity
npPwr=_NpPwr_ObjectIdentity((1,3,6,1,4,1,25728,5800))
_NpPwrTable_Object=MibTable
npPwrTable=_NpPwrTable_Object((1,3,6,1,4,1,25728,5800,3))
if mibBuilder.loadTexts:npPwrTable.setStatus(_A)
_NpPwrEntry_Object=MibTableRow
npPwrEntry=_NpPwrEntry_Object((1,3,6,1,4,1,25728,5800,3,1))
npPwrEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:npPwrEntry.setStatus(_A)
class _NpPwrChannelN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_NpPwrChannelN_Type.__name__=_C
_NpPwrChannelN_Object=MibTableColumn
npPwrChannelN=_NpPwrChannelN_Object((1,3,6,1,4,1,25728,5800,3,1,1),_NpPwrChannelN_Type())
npPwrChannelN.setMaxAccess(_B)
if mibBuilder.loadTexts:npPwrChannelN.setStatus(_A)
class _NpPwrStartReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_NpPwrStartReset_Type.__name__=_C
_NpPwrStartReset_Object=MibTableColumn
npPwrStartReset=_NpPwrStartReset_Object((1,3,6,1,4,1,25728,5800,3,1,2),_NpPwrStartReset_Type())
npPwrStartReset.setMaxAccess(_B)
if mibBuilder.loadTexts:npPwrStartReset.setStatus('obsolete')
class _NpPwrResetsCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NpPwrResetsCounter_Type.__name__=_C
_NpPwrResetsCounter_Object=MibTableColumn
npPwrResetsCounter=_NpPwrResetsCounter_Object((1,3,6,1,4,1,25728,5800,3,1,4),_NpPwrResetsCounter_Type())
npPwrResetsCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:npPwrResetsCounter.setStatus(_A)
class _NpPwrRepeatingResetsCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NpPwrRepeatingResetsCounter_Type.__name__=_C
_NpPwrRepeatingResetsCounter_Object=MibTableColumn
npPwrRepeatingResetsCounter=_NpPwrRepeatingResetsCounter_Object((1,3,6,1,4,1,25728,5800,3,1,5),_NpPwrRepeatingResetsCounter_Type())
npPwrRepeatingResetsCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:npPwrRepeatingResetsCounter.setStatus(_A)
_NpPwrMemo_Type=DisplayString
_NpPwrMemo_Object=MibTableColumn
npPwrMemo=_NpPwrMemo_Object((1,3,6,1,4,1,25728,5800,3,1,6),_NpPwrMemo_Type())
npPwrMemo.setMaxAccess(_B)
if mibBuilder.loadTexts:npPwrMemo.setStatus(_A)
_NpIr_ObjectIdentity=ObjectIdentity
npIr=_NpIr_ObjectIdentity((1,3,6,1,4,1,25728,7900))
_NpIrCtrl_ObjectIdentity=ObjectIdentity
npIrCtrl=_NpIrCtrl_ObjectIdentity((1,3,6,1,4,1,25728,7900,1))
class _NpIrPlayCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_NpIrPlayCmd_Type.__name__=_C
_NpIrPlayCmd_Object=MibScalar
npIrPlayCmd=_NpIrPlayCmd_Object((1,3,6,1,4,1,25728,7900,1,1),_NpIrPlayCmd_Type())
npIrPlayCmd.setMaxAccess(_E)
if mibBuilder.loadTexts:npIrPlayCmd.setStatus(_A)
class _NpIrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpIrReset_Type.__name__=_C
_NpIrReset_Object=MibScalar
npIrReset=_NpIrReset_Object((1,3,6,1,4,1,25728,7900,1,2),_NpIrReset_Type())
npIrReset.setMaxAccess(_E)
if mibBuilder.loadTexts:npIrReset.setStatus(_A)
class _NpIrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,16,17,18,19,20,21)));namedValues=NamedValues(*(('commandCompleted',0),('protocolError',1),('commandAccepted',2),('errorUnknown',16),('errorBadNumber',17),('errorEmptyRecord',18),('errorFlashChip',19),('errorTimeout',20),('errorExtBusBusy',21)))
_NpIrStatus_Type.__name__=_C
_NpIrStatus_Object=MibScalar
npIrStatus=_NpIrStatus_Object((1,3,6,1,4,1,25728,7900,1,3),_NpIrStatus_Type())
npIrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:npIrStatus.setStatus(_A)
_NpSmoke_ObjectIdentity=ObjectIdentity
npSmoke=_NpSmoke_ObjectIdentity((1,3,6,1,4,1,25728,8200))
_NpSmokeTable_Object=MibTable
npSmokeTable=_NpSmokeTable_Object((1,3,6,1,4,1,25728,8200,1))
if mibBuilder.loadTexts:npSmokeTable.setStatus(_A)
_NpSmokeEntry_Object=MibTableRow
npSmokeEntry=_NpSmokeEntry_Object((1,3,6,1,4,1,25728,8200,1,1))
npSmokeEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:npSmokeEntry.setStatus(_A)
class _NpSmokeSensorN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_NpSmokeSensorN_Type.__name__=_C
_NpSmokeSensorN_Object=MibTableColumn
npSmokeSensorN=_NpSmokeSensorN_Object((1,3,6,1,4,1,25728,8200,1,1,1),_NpSmokeSensorN_Type())
npSmokeSensorN.setMaxAccess(_B)
if mibBuilder.loadTexts:npSmokeSensorN.setStatus(_A)
class _NpSmokeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,5)));namedValues=NamedValues(*((_H,0),('alarm',1),(_G,4),(_F,5)))
_NpSmokeStatus_Type.__name__=_C
_NpSmokeStatus_Object=MibTableColumn
npSmokeStatus=_NpSmokeStatus_Object((1,3,6,1,4,1,25728,8200,1,1,2),_NpSmokeStatus_Type())
npSmokeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:npSmokeStatus.setStatus(_A)
class _NpSmokePower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('on',1)))
_NpSmokePower_Type.__name__=_C
_NpSmokePower_Object=MibTableColumn
npSmokePower=_NpSmokePower_Object((1,3,6,1,4,1,25728,8200,1,1,3),_NpSmokePower_Type())
npSmokePower.setMaxAccess(_E)
if mibBuilder.loadTexts:npSmokePower.setStatus(_A)
_NpSmokeReset_Type=Integer32
_NpSmokeReset_Object=MibTableColumn
npSmokeReset=_NpSmokeReset_Object((1,3,6,1,4,1,25728,8200,1,1,4),_NpSmokeReset_Type())
npSmokeReset.setMaxAccess(_E)
if mibBuilder.loadTexts:npSmokeReset.setStatus(_A)
_NpSmokeMemo_Type=DisplayString
_NpSmokeMemo_Object=MibTableColumn
npSmokeMemo=_NpSmokeMemo_Object((1,3,6,1,4,1,25728,8200,1,1,6),_NpSmokeMemo_Type())
npSmokeMemo.setMaxAccess(_B)
if mibBuilder.loadTexts:npSmokeMemo.setStatus(_A)
_NpSmokeTraps_ObjectIdentity=ObjectIdentity
npSmokeTraps=_NpSmokeTraps_ObjectIdentity((1,3,6,1,4,1,25728,8200,2))
_NpSmokeTrapPrefix_ObjectIdentity=ObjectIdentity
npSmokeTrapPrefix=_NpSmokeTrapPrefix_ObjectIdentity((1,3,6,1,4,1,25728,8200,2,0))
class _NpSmokeTrapSensorN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_NpSmokeTrapSensorN_Type.__name__=_C
_NpSmokeTrapSensorN_Object=MibScalar
npSmokeTrapSensorN=_NpSmokeTrapSensorN_Object((1,3,6,1,4,1,25728,8200,2,1),_NpSmokeTrapSensorN_Type())
npSmokeTrapSensorN.setMaxAccess(_B)
if mibBuilder.loadTexts:npSmokeTrapSensorN.setStatus(_A)
class _NpSmokeTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,5)));namedValues=NamedValues(*((_H,0),('alarm',1),(_G,4),(_F,5)))
_NpSmokeTrapStatus_Type.__name__=_C
_NpSmokeTrapStatus_Object=MibScalar
npSmokeTrapStatus=_NpSmokeTrapStatus_Object((1,3,6,1,4,1,25728,8200,2,2),_NpSmokeTrapStatus_Type())
npSmokeTrapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:npSmokeTrapStatus.setStatus(_A)
_NpSmokeTrapMemo_Type=DisplayString
_NpSmokeTrapMemo_Object=MibScalar
npSmokeTrapMemo=_NpSmokeTrapMemo_Object((1,3,6,1,4,1,25728,8200,2,6),_NpSmokeTrapMemo_Type())
npSmokeTrapMemo.setMaxAccess(_B)
if mibBuilder.loadTexts:npSmokeTrapMemo.setStatus(_A)
_NpRelHumidity_ObjectIdentity=ObjectIdentity
npRelHumidity=_NpRelHumidity_ObjectIdentity((1,3,6,1,4,1,25728,8400))
_NpRelHumSensor_ObjectIdentity=ObjectIdentity
npRelHumSensor=_NpRelHumSensor_ObjectIdentity((1,3,6,1,4,1,25728,8400,2))
class _NpRelHumSensorValueH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NpRelHumSensorValueH_Type.__name__=_C
_NpRelHumSensorValueH_Object=MibScalar
npRelHumSensorValueH=_NpRelHumSensorValueH_Object((1,3,6,1,4,1,25728,8400,2,2),_NpRelHumSensorValueH_Type())
npRelHumSensorValueH.setMaxAccess(_B)
if mibBuilder.loadTexts:npRelHumSensorValueH.setStatus(_A)
class _NpRelHumSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('error',0),(_H,1)))
_NpRelHumSensorStatus_Type.__name__=_C
_NpRelHumSensorStatus_Object=MibScalar
npRelHumSensorStatus=_NpRelHumSensorStatus_Object((1,3,6,1,4,1,25728,8400,2,3),_NpRelHumSensorStatus_Type())
npRelHumSensorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:npRelHumSensorStatus.setStatus(_A)
class _NpRelHumSensorValueT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,200))
_NpRelHumSensorValueT_Type.__name__=_C
_NpRelHumSensorValueT_Object=MibScalar
npRelHumSensorValueT=_NpRelHumSensorValueT_Object((1,3,6,1,4,1,25728,8400,2,4),_NpRelHumSensorValueT_Type())
npRelHumSensorValueT.setMaxAccess(_B)
if mibBuilder.loadTexts:npRelHumSensorValueT.setStatus(_A)
class _NpRelHumSensorStatusH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('sensorFailed',0),('belowSafeRange',1),('inSafeRange',2),('aboveSafeRange',3)))
_NpRelHumSensorStatusH_Type.__name__=_C
_NpRelHumSensorStatusH_Object=MibScalar
npRelHumSensorStatusH=_NpRelHumSensorStatusH_Object((1,3,6,1,4,1,25728,8400,2,5),_NpRelHumSensorStatusH_Type())
npRelHumSensorStatusH.setMaxAccess(_B)
if mibBuilder.loadTexts:npRelHumSensorStatusH.setStatus(_A)
class _NpRelHumSafeRangeHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NpRelHumSafeRangeHigh_Type.__name__=_C
_NpRelHumSafeRangeHigh_Object=MibScalar
npRelHumSafeRangeHigh=_NpRelHumSafeRangeHigh_Object((1,3,6,1,4,1,25728,8400,2,7),_NpRelHumSafeRangeHigh_Type())
npRelHumSafeRangeHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:npRelHumSafeRangeHigh.setStatus(_A)
class _NpRelHumSafeRangeLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NpRelHumSafeRangeLow_Type.__name__=_C
_NpRelHumSafeRangeLow_Object=MibScalar
npRelHumSafeRangeLow=_NpRelHumSafeRangeLow_Object((1,3,6,1,4,1,25728,8400,2,8),_NpRelHumSafeRangeLow_Type())
npRelHumSafeRangeLow.setMaxAccess(_B)
if mibBuilder.loadTexts:npRelHumSafeRangeLow.setStatus(_A)
_NpRelHumSensorValueT100_Type=Integer32
_NpRelHumSensorValueT100_Object=MibScalar
npRelHumSensorValueT100=_NpRelHumSensorValueT100_Object((1,3,6,1,4,1,25728,8400,2,9),_NpRelHumSensorValueT100_Type())
npRelHumSensorValueT100.setMaxAccess(_B)
if mibBuilder.loadTexts:npRelHumSensorValueT100.setStatus(_A)
_NpRelHumTraps_ObjectIdentity=ObjectIdentity
npRelHumTraps=_NpRelHumTraps_ObjectIdentity((1,3,6,1,4,1,25728,8400,9))
_NpRelHumTrapPrefix_ObjectIdentity=ObjectIdentity
npRelHumTrapPrefix=_NpRelHumTrapPrefix_ObjectIdentity((1,3,6,1,4,1,25728,8400,9,0))
_NpThermo_ObjectIdentity=ObjectIdentity
npThermo=_NpThermo_ObjectIdentity((1,3,6,1,4,1,25728,8800))
_NpThermoTable_Object=MibTable
npThermoTable=_NpThermoTable_Object((1,3,6,1,4,1,25728,8800,1))
if mibBuilder.loadTexts:npThermoTable.setStatus(_A)
_NpThermoEntry_Object=MibTableRow
npThermoEntry=_NpThermoEntry_Object((1,3,6,1,4,1,25728,8800,1,1))
npThermoEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:npThermoEntry.setStatus(_A)
class _NpThermoSensorN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NpThermoSensorN_Type.__name__=_C
_NpThermoSensorN_Object=MibTableColumn
npThermoSensorN=_NpThermoSensorN_Object((1,3,6,1,4,1,25728,8800,1,1,1),_NpThermoSensorN_Type())
npThermoSensorN.setMaxAccess(_B)
if mibBuilder.loadTexts:npThermoSensorN.setStatus(_A)
class _NpThermoValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,280))
_NpThermoValue_Type.__name__=_C
_NpThermoValue_Object=MibTableColumn
npThermoValue=_NpThermoValue_Object((1,3,6,1,4,1,25728,8800,1,1,2),_NpThermoValue_Type())
npThermoValue.setMaxAccess(_B)
if mibBuilder.loadTexts:npThermoValue.setStatus(_A)
class _NpThermoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),('low',1),('norm',2),('high',3)))
_NpThermoStatus_Type.__name__=_C
_NpThermoStatus_Object=MibTableColumn
npThermoStatus=_NpThermoStatus_Object((1,3,6,1,4,1,25728,8800,1,1,3),_NpThermoStatus_Type())
npThermoStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:npThermoStatus.setStatus(_A)
class _NpThermoLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,280))
_NpThermoLow_Type.__name__=_C
_NpThermoLow_Object=MibTableColumn
npThermoLow=_NpThermoLow_Object((1,3,6,1,4,1,25728,8800,1,1,4),_NpThermoLow_Type())
npThermoLow.setMaxAccess(_B)
if mibBuilder.loadTexts:npThermoLow.setStatus(_A)
class _NpThermoHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,280))
_NpThermoHigh_Type.__name__=_C
_NpThermoHigh_Object=MibTableColumn
npThermoHigh=_NpThermoHigh_Object((1,3,6,1,4,1,25728,8800,1,1,5),_NpThermoHigh_Type())
npThermoHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:npThermoHigh.setStatus(_A)
_NpThermoMemo_Type=DisplayString
_NpThermoMemo_Object=MibTableColumn
npThermoMemo=_NpThermoMemo_Object((1,3,6,1,4,1,25728,8800,1,1,6),_NpThermoMemo_Type())
npThermoMemo.setMaxAccess(_B)
if mibBuilder.loadTexts:npThermoMemo.setStatus(_A)
_NpThermoTraps_ObjectIdentity=ObjectIdentity
npThermoTraps=_NpThermoTraps_ObjectIdentity((1,3,6,1,4,1,25728,8800,2))
_NpThermoTrapPrefix_ObjectIdentity=ObjectIdentity
npThermoTrapPrefix=_NpThermoTrapPrefix_ObjectIdentity((1,3,6,1,4,1,25728,8800,2,0))
class _NpThermoTrapSensorN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NpThermoTrapSensorN_Type.__name__=_C
_NpThermoTrapSensorN_Object=MibScalar
npThermoTrapSensorN=_NpThermoTrapSensorN_Object((1,3,6,1,4,1,25728,8800,2,1),_NpThermoTrapSensorN_Type())
npThermoTrapSensorN.setMaxAccess(_B)
if mibBuilder.loadTexts:npThermoTrapSensorN.setStatus(_A)
class _NpThermoTrapValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,280))
_NpThermoTrapValue_Type.__name__=_C
_NpThermoTrapValue_Object=MibScalar
npThermoTrapValue=_NpThermoTrapValue_Object((1,3,6,1,4,1,25728,8800,2,2),_NpThermoTrapValue_Type())
npThermoTrapValue.setMaxAccess(_B)
if mibBuilder.loadTexts:npThermoTrapValue.setStatus(_A)
class _NpThermoTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),('low',1),('norm',2),('high',3)))
_NpThermoTrapStatus_Type.__name__=_C
_NpThermoTrapStatus_Object=MibScalar
npThermoTrapStatus=_NpThermoTrapStatus_Object((1,3,6,1,4,1,25728,8800,2,3),_NpThermoTrapStatus_Type())
npThermoTrapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:npThermoTrapStatus.setStatus(_A)
class _NpThermoTrapLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,280))
_NpThermoTrapLow_Type.__name__=_C
_NpThermoTrapLow_Object=MibScalar
npThermoTrapLow=_NpThermoTrapLow_Object((1,3,6,1,4,1,25728,8800,2,4),_NpThermoTrapLow_Type())
npThermoTrapLow.setMaxAccess(_B)
if mibBuilder.loadTexts:npThermoTrapLow.setStatus(_A)
class _NpThermoTrapHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,280))
_NpThermoTrapHigh_Type.__name__=_C
_NpThermoTrapHigh_Object=MibScalar
npThermoTrapHigh=_NpThermoTrapHigh_Object((1,3,6,1,4,1,25728,8800,2,5),_NpThermoTrapHigh_Type())
npThermoTrapHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:npThermoTrapHigh.setStatus(_A)
_NpThermoTrapMemo_Type=DisplayString
_NpThermoTrapMemo_Object=MibScalar
npThermoTrapMemo=_NpThermoTrapMemo_Object((1,3,6,1,4,1,25728,8800,2,6),_NpThermoTrapMemo_Type())
npThermoTrapMemo.setMaxAccess(_B)
if mibBuilder.loadTexts:npThermoTrapMemo.setStatus(_A)
_NpIo_ObjectIdentity=ObjectIdentity
npIo=_NpIo_ObjectIdentity((1,3,6,1,4,1,25728,8900))
_NpIoTable_Object=MibTable
npIoTable=_NpIoTable_Object((1,3,6,1,4,1,25728,8900,1))
if mibBuilder.loadTexts:npIoTable.setStatus(_A)
_NpIoEntry_Object=MibTableRow
npIoEntry=_NpIoEntry_Object((1,3,6,1,4,1,25728,8900,1,1))
npIoEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:npIoEntry.setStatus(_A)
class _NpIoLineN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_NpIoLineN_Type.__name__=_C
_NpIoLineN_Object=MibTableColumn
npIoLineN=_NpIoLineN_Object((1,3,6,1,4,1,25728,8900,1,1,1),_NpIoLineN_Type())
npIoLineN.setMaxAccess(_B)
if mibBuilder.loadTexts:npIoLineN.setStatus(_A)
class _NpIoLevelIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpIoLevelIn_Type.__name__=_C
_NpIoLevelIn_Object=MibTableColumn
npIoLevelIn=_NpIoLevelIn_Object((1,3,6,1,4,1,25728,8900,1,1,2),_NpIoLevelIn_Type())
npIoLevelIn.setMaxAccess(_B)
if mibBuilder.loadTexts:npIoLevelIn.setStatus(_A)
class _NpIoLevelOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpIoLevelOut_Type.__name__=_C
_NpIoLevelOut_Object=MibTableColumn
npIoLevelOut=_NpIoLevelOut_Object((1,3,6,1,4,1,25728,8900,1,1,3),_NpIoLevelOut_Type())
npIoLevelOut.setMaxAccess(_E)
if mibBuilder.loadTexts:npIoLevelOut.setStatus(_A)
_NpIoMemo_Type=DisplayString
_NpIoMemo_Object=MibTableColumn
npIoMemo=_NpIoMemo_Object((1,3,6,1,4,1,25728,8900,1,1,6),_NpIoMemo_Type())
npIoMemo.setMaxAccess(_B)
if mibBuilder.loadTexts:npIoMemo.setStatus(_A)
_NpIoPulseCounter_Type=Counter32
_NpIoPulseCounter_Object=MibTableColumn
npIoPulseCounter=_NpIoPulseCounter_Object((1,3,6,1,4,1,25728,8900,1,1,9),_NpIoPulseCounter_Type())
npIoPulseCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:npIoPulseCounter.setStatus(_A)
class _NpIoSinglePulseDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,25500))
_NpIoSinglePulseDuration_Type.__name__=_C
_NpIoSinglePulseDuration_Object=MibTableColumn
npIoSinglePulseDuration=_NpIoSinglePulseDuration_Object((1,3,6,1,4,1,25728,8900,1,1,12),_NpIoSinglePulseDuration_Type())
npIoSinglePulseDuration.setMaxAccess(_E)
if mibBuilder.loadTexts:npIoSinglePulseDuration.setStatus(_A)
_NpIoSinglePulseStart_Type=Integer32
_NpIoSinglePulseStart_Object=MibTableColumn
npIoSinglePulseStart=_NpIoSinglePulseStart_Object((1,3,6,1,4,1,25728,8900,1,1,13),_NpIoSinglePulseStart_Type())
npIoSinglePulseStart.setMaxAccess(_E)
if mibBuilder.loadTexts:npIoSinglePulseStart.setStatus(_A)
_NpIoTraps_ObjectIdentity=ObjectIdentity
npIoTraps=_NpIoTraps_ObjectIdentity((1,3,6,1,4,1,25728,8900,2))
_NpIoTrapPrefix_ObjectIdentity=ObjectIdentity
npIoTrapPrefix=_NpIoTrapPrefix_ObjectIdentity((1,3,6,1,4,1,25728,8900,2,0))
class _NpIoTrapLineN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_NpIoTrapLineN_Type.__name__=_C
_NpIoTrapLineN_Object=MibScalar
npIoTrapLineN=_NpIoTrapLineN_Object((1,3,6,1,4,1,25728,8900,2,1),_NpIoTrapLineN_Type())
npIoTrapLineN.setMaxAccess(_B)
if mibBuilder.loadTexts:npIoTrapLineN.setStatus(_A)
class _NpIoTrapLevelIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpIoTrapLevelIn_Type.__name__=_C
_NpIoTrapLevelIn_Object=MibScalar
npIoTrapLevelIn=_NpIoTrapLevelIn_Object((1,3,6,1,4,1,25728,8900,2,2),_NpIoTrapLevelIn_Type())
npIoTrapLevelIn.setMaxAccess(_B)
if mibBuilder.loadTexts:npIoTrapLevelIn.setStatus(_A)
_NpIoTrapMemo_Type=DisplayString
_NpIoTrapMemo_Object=MibScalar
npIoTrapMemo=_NpIoTrapMemo_Object((1,3,6,1,4,1,25728,8900,2,6),_NpIoTrapMemo_Type())
npIoTrapMemo.setMaxAccess(_B)
if mibBuilder.loadTexts:npIoTrapMemo.setStatus(_A)
npGsmTrap=NotificationType((1,3,6,1,4,1,25728,3800,2,0,1))
npGsmTrap.setObjects(*((_D,_N),(_D,_O),(_D,_P)))
if mibBuilder.loadTexts:npGsmTrap.setStatus(_A)
npSmokeTrap=NotificationType((1,3,6,1,4,1,25728,8200,2,0,1))
npSmokeTrap.setObjects(*((_D,_Q),(_D,_R),(_D,_S)))
if mibBuilder.loadTexts:npSmokeTrap.setStatus(_A)
npRelHumTrap=NotificationType((1,3,6,1,4,1,25728,8400,9,0,1))
npRelHumTrap.setObjects(*((_D,_T),(_D,_U),(_D,_V),(_D,_W)))
if mibBuilder.loadTexts:npRelHumTrap.setStatus(_A)
npThermoTrap=NotificationType((1,3,6,1,4,1,25728,8800,2,0,1))
npThermoTrap.setObjects(*((_D,_X),(_D,_Y),(_D,_Z),(_D,_a),(_D,_b),(_D,_c)))
if mibBuilder.loadTexts:npThermoTrap.setStatus(_A)
npIoTrap=NotificationType((1,3,6,1,4,1,25728,8900,2,0,1))
npIoTrap.setObjects(*((_D,_d),(_D,_e),(_D,_f)))
if mibBuilder.loadTexts:npIoTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'lightcom':lightcom,'netPing8Pwr':netPing8Pwr,'npReboot':npReboot,'npSoftReboot':npSoftReboot,'npResetStack':npResetStack,'npForcedReboot':npForcedReboot,'npGsm':npGsm,'npGsmInfo':npGsmInfo,_N:npGsmFailed,_O:npGsmRegistration,_P:npGsmStrength,'npGsmSendSms':npGsmSendSms,'npGsmTraps':npGsmTraps,'npGsmTrapPrefix':npGsmTrapPrefix,'npGsmTrap':npGsmTrap,'npBattery':npBattery,'npBatteryInfo':npBatteryInfo,'npBatteryPok':npBatteryPok,'npBatteryLevel':npBatteryLevel,'npBatteryChg':npBatteryChg,'npRelay':npRelay,'npRelayTable':npRelayTable,'npRelayEntry':npRelayEntry,_I:npRelayN,'npRelayMode':npRelayMode,'npRelayStartReset':npRelayStartReset,'npRelayMemo':npRelayMemo,'npRelayFlip':npRelayFlip,'npRelayState':npRelayState,'npRelayPowered':npRelayPowered,'npPwr':npPwr,'npPwrTable':npPwrTable,'npPwrEntry':npPwrEntry,_J:npPwrChannelN,'npPwrStartReset':npPwrStartReset,'npPwrResetsCounter':npPwrResetsCounter,'npPwrRepeatingResetsCounter':npPwrRepeatingResetsCounter,'npPwrMemo':npPwrMemo,'npIr':npIr,'npIrCtrl':npIrCtrl,'npIrPlayCmd':npIrPlayCmd,'npIrReset':npIrReset,'npIrStatus':npIrStatus,'npSmoke':npSmoke,'npSmokeTable':npSmokeTable,'npSmokeEntry':npSmokeEntry,_K:npSmokeSensorN,'npSmokeStatus':npSmokeStatus,'npSmokePower':npSmokePower,'npSmokeReset':npSmokeReset,'npSmokeMemo':npSmokeMemo,'npSmokeTraps':npSmokeTraps,'npSmokeTrapPrefix':npSmokeTrapPrefix,'npSmokeTrap':npSmokeTrap,_Q:npSmokeTrapSensorN,_R:npSmokeTrapStatus,_S:npSmokeTrapMemo,'npRelHumidity':npRelHumidity,'npRelHumSensor':npRelHumSensor,_U:npRelHumSensorValueH,'npRelHumSensorStatus':npRelHumSensorStatus,'npRelHumSensorValueT':npRelHumSensorValueT,_T:npRelHumSensorStatusH,_V:npRelHumSafeRangeHigh,_W:npRelHumSafeRangeLow,'npRelHumSensorValueT100':npRelHumSensorValueT100,'npRelHumTraps':npRelHumTraps,'npRelHumTrapPrefix':npRelHumTrapPrefix,'npRelHumTrap':npRelHumTrap,'npThermo':npThermo,'npThermoTable':npThermoTable,'npThermoEntry':npThermoEntry,_L:npThermoSensorN,'npThermoValue':npThermoValue,'npThermoStatus':npThermoStatus,'npThermoLow':npThermoLow,'npThermoHigh':npThermoHigh,'npThermoMemo':npThermoMemo,'npThermoTraps':npThermoTraps,'npThermoTrapPrefix':npThermoTrapPrefix,'npThermoTrap':npThermoTrap,_X:npThermoTrapSensorN,_Y:npThermoTrapValue,_Z:npThermoTrapStatus,_a:npThermoTrapLow,_b:npThermoTrapHigh,_c:npThermoTrapMemo,'npIo':npIo,'npIoTable':npIoTable,'npIoEntry':npIoEntry,_M:npIoLineN,'npIoLevelIn':npIoLevelIn,'npIoLevelOut':npIoLevelOut,'npIoMemo':npIoMemo,'npIoPulseCounter':npIoPulseCounter,'npIoSinglePulseDuration':npIoSinglePulseDuration,'npIoSinglePulseStart':npIoSinglePulseStart,'npIoTraps':npIoTraps,'npIoTrapPrefix':npIoTrapPrefix,'npIoTrap':npIoTrap,_d:npIoTrapLineN,_e:npIoTrapLevelIn,_f:npIoTrapMemo})