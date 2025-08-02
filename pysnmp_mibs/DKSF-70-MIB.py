_Al='npVoltageTrapPeakStatus'
_Ak='npVoltageTrapSagStatus'
_Aj='npVoltageTrapSagCounter'
_Ai='npVoltageTrapMemo'
_Ah='npVoltageTrapFreqStatus'
_Ag='npVoltageTrapFreq'
_Af='npVoltageTrapStatus'
_Ae='npVoltageTrapRMS'
_Ad='npVoltageTrapN'
_Ac='npIoTrapLevelLegend'
_Ab='npIoTrapMemo'
_Aa='npIoTrapLevelIn'
_AZ='npIoTrapLineN'
_AY='npThermoTrapMemo'
_AX='npThermoTrapHigh'
_AW='npThermoTrapLow'
_AV='npThermoTrapStatus'
_AU='npThermoTrapValue'
_AT='npThermoTrapSensorN'
_AS='npTrapEmailTo'
_AR='npCurLoopTrapPower'
_AQ='npCurLoopTrapR'
_AP='npCurLoopTrapV'
_AO='npCurLoopTrapI'
_AN='npCurLoopTrapStatus'
_AM='npCurLoopTrapN'
_AL='npInputAnalogTrapWorkRangeLow'
_AK='npInputAnalogTrapSafeRangeLow'
_AJ='npInputAnalogTrapSafeRangeHigh'
_AI='npInputAnalogTrapWorkRangeHigh'
_AH='npInputAnalogTrapPower'
_AG='npInputAnalogTrapMemo'
_AF='npInputAnalogTrapResistance'
_AE='npInputAnalogTrapVoltage'
_AD='npInputAnalogTrapCurrent'
_AC='npInputAnalogTrapStatus'
_AB='npInputAnalogTrapSensorN'
_AA='npGsmUnparsedRxSmsUtf8'
_A9='npGsmUnparsedRxSms'
_A8='npGsmUnparsedRxSmsFrom'
_A7='npGsmStrength'
_A6='npGsmRegistration'
_A5='npGsmFailed'
_A4='dangerous'
_A3='npVoltageN'
_A2='npIoLineN'
_A1='npThermoSensorN'
_A0='npRelHumN'
_z='notPowered'
_y='npCurLoopN'
_x='failureAnalog'
_w='aboveSafe'
_v='belowSafe'
_u='failure1w'
_t='npInputAnalogSensorN'
_s='npExtRelayN'
_r='npRelayN'
_q='schedule'
_p='watchdog'
_o='httpApi'
_n='webInterface'
_m='low'
_l='aboveSafeRange'
_k='inSafeRange'
_j='belowSafeRange'
_i='unknown'
_h='failed'
_g='good'
_f='warn'
_e='bad'
_d='high'
_c='flip'
_b='npExtRelayTrapDateTime'
_a='npExtRelayTrapCmdSrc'
_Z='npExtRelayTrapState'
_Y='npExtRelayTrapMemo'
_X='npExtRelayTrapMode'
_W='npExtRelayTrapN'
_V='npRelayTrapDateTime'
_U='npRelayTrapCmdSrc'
_T='npRelayTrapState'
_S='npRelayTrapMemo'
_R='npRelayTrapMode'
_Q='npRelayTrapN'
_P='noVoltage'
_O='npRelHumTrapDataSafeRangeLow'
_N='npRelHumTrapDataSafeRangeHigh'
_M='npRelHumTrapDataMemo'
_L='npRelHumTrapDataValue'
_K='npRelHumTrapDataStatus'
_J='npRelHumTrapDataN'
_I='sensorFailed'
_H='on'
_G='off'
_F='accessible-for-notify'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='DKSF-70-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
uniPingServerSolutionV3=ModuleIdentity((1,3,6,1,4,1,25728,70))
if mibBuilder.loadTexts:uniPingServerSolutionV3.setRevisions(('2022-07-01 00:00','2020-08-19 00:00','2020-06-12 00:00','2019-10-13 00:00','2018-07-01 00:00','2016-08-24 00:00','2015-07-14 00:00','2015-05-29 00:00','2014-12-03 00:00','2014-11-26 00:00','2014-02-02 00:00','2014-01-29 00:00','2014-01-21 00:00','2013-04-11 00:00','2012-05-31 00:00','2012-04-17 00:00','2012-03-23 00:00','2011-09-23 00:00','2011-03-24 00:00','2010-10-14 00:00','2010-09-20 00:00','2010-05-31 00:00','2010-04-14 00:00'))
class FixedPoint1000(TextualConvention,Integer32):status=_A;displayHint='d-3'
_Lightcom_ObjectIdentity=ObjectIdentity
lightcom=_Lightcom_ObjectIdentity((1,3,6,1,4,1,25728))
_NpTrapInfo_ObjectIdentity=ObjectIdentity
npTrapInfo=_NpTrapInfo_ObjectIdentity((1,3,6,1,4,1,25728,90))
_NpTrapEmailTo_Type=DisplayString
_NpTrapEmailTo_Object=MibScalar
npTrapEmailTo=_NpTrapEmailTo_Object((1,3,6,1,4,1,25728,90,1),_NpTrapEmailTo_Type())
npTrapEmailTo.setMaxAccess(_C)
if mibBuilder.loadTexts:npTrapEmailTo.setStatus(_A)
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
class _NpGsmFailed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ok',0),(_h,1),('fatalError',2)))
_NpGsmFailed_Type.__name__=_D
_NpGsmFailed_Object=MibScalar
npGsmFailed=_NpGsmFailed_Object((1,3,6,1,4,1,25728,3800,1,1),_NpGsmFailed_Type())
npGsmFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:npGsmFailed.setStatus(_A)
class _NpGsmRegistration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,255)));namedValues=NamedValues(*(('impossible',0),('homeNetwork',1),('searching',2),('denied',3),(_i,4),('roaming',5),('infoUpdate',255)))
_NpGsmRegistration_Type.__name__=_D
_NpGsmRegistration_Object=MibScalar
npGsmRegistration=_NpGsmRegistration_Object((1,3,6,1,4,1,25728,3800,1,2),_NpGsmRegistration_Type())
npGsmRegistration.setMaxAccess(_C)
if mibBuilder.loadTexts:npGsmRegistration.setStatus(_A)
class _NpGsmStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NpGsmStrength_Type.__name__=_D
_NpGsmStrength_Object=MibScalar
npGsmStrength=_NpGsmStrength_Object((1,3,6,1,4,1,25728,3800,1,3),_NpGsmStrength_Type())
npGsmStrength.setMaxAccess(_C)
if mibBuilder.loadTexts:npGsmStrength.setStatus(_A)
_NpGsmSendSmsUtf8_Type=DisplayString
_NpGsmSendSmsUtf8_Object=MibScalar
npGsmSendSmsUtf8=_NpGsmSendSmsUtf8_Object((1,3,6,1,4,1,25728,3800,1,9),_NpGsmSendSmsUtf8_Type())
npGsmSendSmsUtf8.setMaxAccess(_E)
if mibBuilder.loadTexts:npGsmSendSmsUtf8.setStatus(_A)
_NpGsmSendSmsWin1251_Type=DisplayString
_NpGsmSendSmsWin1251_Object=MibScalar
npGsmSendSmsWin1251=_NpGsmSendSmsWin1251_Object((1,3,6,1,4,1,25728,3800,1,10),_NpGsmSendSmsWin1251_Type())
npGsmSendSmsWin1251.setMaxAccess(_E)
if mibBuilder.loadTexts:npGsmSendSmsWin1251.setStatus(_A)
_NpGsmUnparsedRxSmsFrom_Type=DisplayString
_NpGsmUnparsedRxSmsFrom_Object=MibScalar
npGsmUnparsedRxSmsFrom=_NpGsmUnparsedRxSmsFrom_Object((1,3,6,1,4,1,25728,3800,1,11),_NpGsmUnparsedRxSmsFrom_Type())
npGsmUnparsedRxSmsFrom.setMaxAccess(_F)
if mibBuilder.loadTexts:npGsmUnparsedRxSmsFrom.setStatus(_A)
_NpGsmUnparsedRxSms_Type=DisplayString
_NpGsmUnparsedRxSms_Object=MibScalar
npGsmUnparsedRxSms=_NpGsmUnparsedRxSms_Object((1,3,6,1,4,1,25728,3800,1,12),_NpGsmUnparsedRxSms_Type())
npGsmUnparsedRxSms.setMaxAccess(_F)
if mibBuilder.loadTexts:npGsmUnparsedRxSms.setStatus(_A)
_NpGsmUnparsedRxSmsUtf8_Type=DisplayString
_NpGsmUnparsedRxSmsUtf8_Object=MibScalar
npGsmUnparsedRxSmsUtf8=_NpGsmUnparsedRxSmsUtf8_Object((1,3,6,1,4,1,25728,3800,1,13),_NpGsmUnparsedRxSmsUtf8_Type())
npGsmUnparsedRxSmsUtf8.setMaxAccess(_F)
if mibBuilder.loadTexts:npGsmUnparsedRxSmsUtf8.setStatus(_A)
_NpGsmTraps_ObjectIdentity=ObjectIdentity
npGsmTraps=_NpGsmTraps_ObjectIdentity((1,3,6,1,4,1,25728,3800,2))
_NpGsmTrapPrefix_ObjectIdentity=ObjectIdentity
npGsmTrapPrefix=_NpGsmTrapPrefix_ObjectIdentity((1,3,6,1,4,1,25728,3800,2,0))
_NpRelay_ObjectIdentity=ObjectIdentity
npRelay=_NpRelay_ObjectIdentity((1,3,6,1,4,1,25728,5500))
_NpRelayTrapData_ObjectIdentity=ObjectIdentity
npRelayTrapData=_NpRelayTrapData_ObjectIdentity((1,3,6,1,4,1,25728,5500,3))
class _NpRelayTrapN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_NpRelayTrapN_Type.__name__=_D
_NpRelayTrapN_Object=MibScalar
npRelayTrapN=_NpRelayTrapN_Object((1,3,6,1,4,1,25728,5500,3,1),_NpRelayTrapN_Type())
npRelayTrapN.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelayTrapN.setStatus(_A)
class _NpRelayTrapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_NpRelayTrapMode_Type.__name__=_D
_NpRelayTrapMode_Object=MibScalar
npRelayTrapMode=_NpRelayTrapMode_Object((1,3,6,1,4,1,25728,5500,3,2),_NpRelayTrapMode_Type())
npRelayTrapMode.setMaxAccess(_E)
if mibBuilder.loadTexts:npRelayTrapMode.setStatus(_A)
_NpRelayTrapMemo_Type=DisplayString
_NpRelayTrapMemo_Object=MibScalar
npRelayTrapMemo=_NpRelayTrapMemo_Object((1,3,6,1,4,1,25728,5500,3,6),_NpRelayTrapMemo_Type())
npRelayTrapMemo.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelayTrapMemo.setStatus(_A)
class _NpRelayTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_NpRelayTrapState_Type.__name__=_D
_NpRelayTrapState_Object=MibScalar
npRelayTrapState=_NpRelayTrapState_Object((1,3,6,1,4,1,25728,5500,3,15),_NpRelayTrapState_Type())
npRelayTrapState.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelayTrapState.setStatus(_A)
class _NpRelayTrapCmdSrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_i,-1),(_n,1),('snmp',2),('sms',3),(_o,4),(_p,5),(_q,6),('logic',7)))
_NpRelayTrapCmdSrc_Type.__name__=_D
_NpRelayTrapCmdSrc_Object=MibScalar
npRelayTrapCmdSrc=_NpRelayTrapCmdSrc_Object((1,3,6,1,4,1,25728,5500,3,18),_NpRelayTrapCmdSrc_Type())
npRelayTrapCmdSrc.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelayTrapCmdSrc.setStatus(_A)
_NpRelayTrapDateTime_Type=DisplayString
_NpRelayTrapDateTime_Object=MibScalar
npRelayTrapDateTime=_NpRelayTrapDateTime_Object((1,3,6,1,4,1,25728,5500,3,19),_NpRelayTrapDateTime_Type())
npRelayTrapDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelayTrapDateTime.setStatus(_A)
_NpRelayTable_Object=MibTable
npRelayTable=_NpRelayTable_Object((1,3,6,1,4,1,25728,5500,5))
if mibBuilder.loadTexts:npRelayTable.setStatus(_A)
_NpRelayEntry_Object=MibTableRow
npRelayEntry=_NpRelayEntry_Object((1,3,6,1,4,1,25728,5500,5,1))
npRelayEntry.setIndexNames((0,_B,_r))
if mibBuilder.loadTexts:npRelayEntry.setStatus(_A)
class _NpRelayN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_NpRelayN_Type.__name__=_D
_NpRelayN_Object=MibTableColumn
npRelayN=_NpRelayN_Object((1,3,6,1,4,1,25728,5500,5,1,1),_NpRelayN_Type())
npRelayN.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelayN.setStatus(_A)
class _NpRelayMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*((_c,-1),(_G,0),(_H,1)))
_NpRelayMode_Type.__name__=_D
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
npRelayMemo.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelayMemo.setStatus(_A)
class _NpRelayFlip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-1));namedValues=NamedValues((_c,-1))
_NpRelayFlip_Type.__name__=_D
_NpRelayFlip_Object=MibTableColumn
npRelayFlip=_NpRelayFlip_Object((1,3,6,1,4,1,25728,5500,5,1,14),_NpRelayFlip_Type())
npRelayFlip.setMaxAccess(_E)
if mibBuilder.loadTexts:npRelayFlip.setStatus(_A)
class _NpRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_NpRelayState_Type.__name__=_D
_NpRelayState_Object=MibTableColumn
npRelayState=_NpRelayState_Object((1,3,6,1,4,1,25728,5500,5,1,15),_NpRelayState_Type())
npRelayState.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelayState.setStatus(_A)
_NpRelayTrap_ObjectIdentity=ObjectIdentity
npRelayTrap=_NpRelayTrap_ObjectIdentity((1,3,6,1,4,1,25728,5500,6))
_NpRelayTrapAllEvents_ObjectIdentity=ObjectIdentity
npRelayTrapAllEvents=_NpRelayTrapAllEvents_ObjectIdentity((1,3,6,1,4,1,25728,5500,6,127))
_NpExtRelay_ObjectIdentity=ObjectIdentity
npExtRelay=_NpExtRelay_ObjectIdentity((1,3,6,1,4,1,25728,5600))
_NpExtRelayTrapData_ObjectIdentity=ObjectIdentity
npExtRelayTrapData=_NpExtRelayTrapData_ObjectIdentity((1,3,6,1,4,1,25728,5600,3))
class _NpExtRelayTrapN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NpExtRelayTrapN_Type.__name__=_D
_NpExtRelayTrapN_Object=MibScalar
npExtRelayTrapN=_NpExtRelayTrapN_Object((1,3,6,1,4,1,25728,5600,3,1),_NpExtRelayTrapN_Type())
npExtRelayTrapN.setMaxAccess(_C)
if mibBuilder.loadTexts:npExtRelayTrapN.setStatus(_A)
class _NpExtRelayTrapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_NpExtRelayTrapMode_Type.__name__=_D
_NpExtRelayTrapMode_Object=MibScalar
npExtRelayTrapMode=_NpExtRelayTrapMode_Object((1,3,6,1,4,1,25728,5600,3,2),_NpExtRelayTrapMode_Type())
npExtRelayTrapMode.setMaxAccess(_E)
if mibBuilder.loadTexts:npExtRelayTrapMode.setStatus(_A)
_NpExtRelayTrapMemo_Type=DisplayString
_NpExtRelayTrapMemo_Object=MibScalar
npExtRelayTrapMemo=_NpExtRelayTrapMemo_Object((1,3,6,1,4,1,25728,5600,3,6),_NpExtRelayTrapMemo_Type())
npExtRelayTrapMemo.setMaxAccess(_C)
if mibBuilder.loadTexts:npExtRelayTrapMemo.setStatus(_A)
class _NpExtRelayTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_NpExtRelayTrapState_Type.__name__=_D
_NpExtRelayTrapState_Object=MibScalar
npExtRelayTrapState=_NpExtRelayTrapState_Object((1,3,6,1,4,1,25728,5600,3,15),_NpExtRelayTrapState_Type())
npExtRelayTrapState.setMaxAccess(_C)
if mibBuilder.loadTexts:npExtRelayTrapState.setStatus(_A)
class _NpExtRelayTrapCmdSrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_i,-1),(_n,1),('snmp',2),('sms',3),(_o,4),(_p,5),(_q,6),('logic',7),('button',8)))
_NpExtRelayTrapCmdSrc_Type.__name__=_D
_NpExtRelayTrapCmdSrc_Object=MibScalar
npExtRelayTrapCmdSrc=_NpExtRelayTrapCmdSrc_Object((1,3,6,1,4,1,25728,5600,3,18),_NpExtRelayTrapCmdSrc_Type())
npExtRelayTrapCmdSrc.setMaxAccess(_C)
if mibBuilder.loadTexts:npExtRelayTrapCmdSrc.setStatus(_A)
_NpExtRelayTrapDateTime_Type=DisplayString
_NpExtRelayTrapDateTime_Object=MibScalar
npExtRelayTrapDateTime=_NpExtRelayTrapDateTime_Object((1,3,6,1,4,1,25728,5600,3,19),_NpExtRelayTrapDateTime_Type())
npExtRelayTrapDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:npExtRelayTrapDateTime.setStatus(_A)
_NpExtRelayTable_Object=MibTable
npExtRelayTable=_NpExtRelayTable_Object((1,3,6,1,4,1,25728,5600,5))
if mibBuilder.loadTexts:npExtRelayTable.setStatus(_A)
_NpExtRelayEntry_Object=MibTableRow
npExtRelayEntry=_NpExtRelayEntry_Object((1,3,6,1,4,1,25728,5600,5,1))
npExtRelayEntry.setIndexNames((0,_B,_s))
if mibBuilder.loadTexts:npExtRelayEntry.setStatus(_A)
class _NpExtRelayN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NpExtRelayN_Type.__name__=_D
_NpExtRelayN_Object=MibTableColumn
npExtRelayN=_NpExtRelayN_Object((1,3,6,1,4,1,25728,5600,5,1,1),_NpExtRelayN_Type())
npExtRelayN.setMaxAccess(_C)
if mibBuilder.loadTexts:npExtRelayN.setStatus(_A)
class _NpExtRelayMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*((_c,-1),(_G,0),(_H,1)))
_NpExtRelayMode_Type.__name__=_D
_NpExtRelayMode_Object=MibTableColumn
npExtRelayMode=_NpExtRelayMode_Object((1,3,6,1,4,1,25728,5600,5,1,2),_NpExtRelayMode_Type())
npExtRelayMode.setMaxAccess(_E)
if mibBuilder.loadTexts:npExtRelayMode.setStatus(_A)
_NpExtRelayStartReset_Type=Integer32
_NpExtRelayStartReset_Object=MibTableColumn
npExtRelayStartReset=_NpExtRelayStartReset_Object((1,3,6,1,4,1,25728,5600,5,1,3),_NpExtRelayStartReset_Type())
npExtRelayStartReset.setMaxAccess(_E)
if mibBuilder.loadTexts:npExtRelayStartReset.setStatus(_A)
_NpExtRelayMemo_Type=DisplayString
_NpExtRelayMemo_Object=MibTableColumn
npExtRelayMemo=_NpExtRelayMemo_Object((1,3,6,1,4,1,25728,5600,5,1,6),_NpExtRelayMemo_Type())
npExtRelayMemo.setMaxAccess(_C)
if mibBuilder.loadTexts:npExtRelayMemo.setStatus(_A)
class _NpExtRelayFlip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-1));namedValues=NamedValues((_c,-1))
_NpExtRelayFlip_Type.__name__=_D
_NpExtRelayFlip_Object=MibTableColumn
npExtRelayFlip=_NpExtRelayFlip_Object((1,3,6,1,4,1,25728,5600,5,1,14),_NpExtRelayFlip_Type())
npExtRelayFlip.setMaxAccess(_E)
if mibBuilder.loadTexts:npExtRelayFlip.setStatus(_A)
class _NpExtRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_NpExtRelayState_Type.__name__=_D
_NpExtRelayState_Object=MibTableColumn
npExtRelayState=_NpExtRelayState_Object((1,3,6,1,4,1,25728,5600,5,1,15),_NpExtRelayState_Type())
npExtRelayState.setMaxAccess(_C)
if mibBuilder.loadTexts:npExtRelayState.setStatus(_A)
_NpExtRelayTrap_ObjectIdentity=ObjectIdentity
npExtRelayTrap=_NpExtRelayTrap_ObjectIdentity((1,3,6,1,4,1,25728,5600,6))
_NpExtRelayTrapAllEvents_ObjectIdentity=ObjectIdentity
npExtRelayTrapAllEvents=_NpExtRelayTrapAllEvents_ObjectIdentity((1,3,6,1,4,1,25728,5600,6,127))
_NpIr_ObjectIdentity=ObjectIdentity
npIr=_NpIr_ObjectIdentity((1,3,6,1,4,1,25728,7900))
_NpIrCtrl_ObjectIdentity=ObjectIdentity
npIrCtrl=_NpIrCtrl_ObjectIdentity((1,3,6,1,4,1,25728,7900,1))
class _NpIrPlayCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_NpIrPlayCmd_Type.__name__=_D
_NpIrPlayCmd_Object=MibScalar
npIrPlayCmd=_NpIrPlayCmd_Object((1,3,6,1,4,1,25728,7900,1,1),_NpIrPlayCmd_Type())
npIrPlayCmd.setMaxAccess(_E)
if mibBuilder.loadTexts:npIrPlayCmd.setStatus(_A)
class _NpIrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpIrReset_Type.__name__=_D
_NpIrReset_Object=MibScalar
npIrReset=_NpIrReset_Object((1,3,6,1,4,1,25728,7900,1,2),_NpIrReset_Type())
npIrReset.setMaxAccess(_E)
if mibBuilder.loadTexts:npIrReset.setStatus(_A)
class _NpIrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,16,17,18,19,20,21)));namedValues=NamedValues(*(('commandCompleted',0),('protocolError',1),('commandAccepted',2),('errorUnknown',16),('errorBadNumber',17),('errorEmptyRecord',18),('errorFlashChip',19),('errorTimeout',20),('errorExtBusBusy',21)))
_NpIrStatus_Type.__name__=_D
_NpIrStatus_Object=MibScalar
npIrStatus=_NpIrStatus_Object((1,3,6,1,4,1,25728,7900,1,3),_NpIrStatus_Type())
npIrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npIrStatus.setStatus(_A)
_NpInputAnalog_ObjectIdentity=ObjectIdentity
npInputAnalog=_NpInputAnalog_ObjectIdentity((1,3,6,1,4,1,25728,8200))
_NpInputAnalogTable_Object=MibTable
npInputAnalogTable=_NpInputAnalogTable_Object((1,3,6,1,4,1,25728,8200,1))
if mibBuilder.loadTexts:npInputAnalogTable.setStatus(_A)
_NpInputAnalogEntry_Object=MibTableRow
npInputAnalogEntry=_NpInputAnalogEntry_Object((1,3,6,1,4,1,25728,8200,1,1))
npInputAnalogEntry.setIndexNames((0,_B,_t))
if mibBuilder.loadTexts:npInputAnalogEntry.setStatus(_A)
class _NpInputAnalogSensorN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_NpInputAnalogSensorN_Type.__name__=_D
_NpInputAnalogSensorN_Object=MibTableColumn
npInputAnalogSensorN=_NpInputAnalogSensorN_Object((1,3,6,1,4,1,25728,8200,1,1,1),_NpInputAnalogSensorN_Type())
npInputAnalogSensorN.setMaxAccess(_C)
if mibBuilder.loadTexts:npInputAnalogSensorN.setStatus(_A)
class _NpInputAnalogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,5)));namedValues=NamedValues(*((_u,0),(_v,1),('safe',2),(_w,3),(_x,5)))
_NpInputAnalogStatus_Type.__name__=_D
_NpInputAnalogStatus_Object=MibTableColumn
npInputAnalogStatus=_NpInputAnalogStatus_Object((1,3,6,1,4,1,25728,8200,1,1,2),_NpInputAnalogStatus_Type())
npInputAnalogStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npInputAnalogStatus.setStatus(_A)
_NpInputAnalogCurrent_Type=Integer32
_NpInputAnalogCurrent_Object=MibTableColumn
npInputAnalogCurrent=_NpInputAnalogCurrent_Object((1,3,6,1,4,1,25728,8200,1,1,3),_NpInputAnalogCurrent_Type())
npInputAnalogCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:npInputAnalogCurrent.setStatus(_A)
_NpInputAnalogVoltage_Type=Integer32
_NpInputAnalogVoltage_Object=MibTableColumn
npInputAnalogVoltage=_NpInputAnalogVoltage_Object((1,3,6,1,4,1,25728,8200,1,1,4),_NpInputAnalogVoltage_Type())
npInputAnalogVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:npInputAnalogVoltage.setStatus(_A)
_NpInputAnalogResistance_Type=Unsigned32
_NpInputAnalogResistance_Object=MibTableColumn
npInputAnalogResistance=_NpInputAnalogResistance_Object((1,3,6,1,4,1,25728,8200,1,1,5),_NpInputAnalogResistance_Type())
npInputAnalogResistance.setMaxAccess(_C)
if mibBuilder.loadTexts:npInputAnalogResistance.setStatus(_A)
_NpInputAnalogMemo_Type=DisplayString
_NpInputAnalogMemo_Object=MibTableColumn
npInputAnalogMemo=_NpInputAnalogMemo_Object((1,3,6,1,4,1,25728,8200,1,1,6),_NpInputAnalogMemo_Type())
npInputAnalogMemo.setMaxAccess(_C)
if mibBuilder.loadTexts:npInputAnalogMemo.setStatus(_A)
class _NpInputAnalogPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_NpInputAnalogPower_Type.__name__=_D
_NpInputAnalogPower_Object=MibTableColumn
npInputAnalogPower=_NpInputAnalogPower_Object((1,3,6,1,4,1,25728,8200,1,1,7),_NpInputAnalogPower_Type())
npInputAnalogPower.setMaxAccess(_E)
if mibBuilder.loadTexts:npInputAnalogPower.setStatus(_A)
_NpInputAnalogReset_Type=Integer32
_NpInputAnalogReset_Object=MibTableColumn
npInputAnalogReset=_NpInputAnalogReset_Object((1,3,6,1,4,1,25728,8200,1,1,8),_NpInputAnalogReset_Type())
npInputAnalogReset.setMaxAccess(_E)
if mibBuilder.loadTexts:npInputAnalogReset.setStatus(_A)
_NpInputAnalogWorkRangeHigh_Type=Integer32
_NpInputAnalogWorkRangeHigh_Object=MibTableColumn
npInputAnalogWorkRangeHigh=_NpInputAnalogWorkRangeHigh_Object((1,3,6,1,4,1,25728,8200,1,1,11),_NpInputAnalogWorkRangeHigh_Type())
npInputAnalogWorkRangeHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:npInputAnalogWorkRangeHigh.setStatus(_A)
_NpInputAnalogSafeRangeHigh_Type=Integer32
_NpInputAnalogSafeRangeHigh_Object=MibTableColumn
npInputAnalogSafeRangeHigh=_NpInputAnalogSafeRangeHigh_Object((1,3,6,1,4,1,25728,8200,1,1,12),_NpInputAnalogSafeRangeHigh_Type())
npInputAnalogSafeRangeHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:npInputAnalogSafeRangeHigh.setStatus(_A)
_NpInputAnalogSafeRangeLow_Type=Integer32
_NpInputAnalogSafeRangeLow_Object=MibTableColumn
npInputAnalogSafeRangeLow=_NpInputAnalogSafeRangeLow_Object((1,3,6,1,4,1,25728,8200,1,1,13),_NpInputAnalogSafeRangeLow_Type())
npInputAnalogSafeRangeLow.setMaxAccess(_C)
if mibBuilder.loadTexts:npInputAnalogSafeRangeLow.setStatus(_A)
_NpInputAnalogWorkRangeLow_Type=Integer32
_NpInputAnalogWorkRangeLow_Object=MibTableColumn
npInputAnalogWorkRangeLow=_NpInputAnalogWorkRangeLow_Object((1,3,6,1,4,1,25728,8200,1,1,14),_NpInputAnalogWorkRangeLow_Type())
npInputAnalogWorkRangeLow.setMaxAccess(_C)
if mibBuilder.loadTexts:npInputAnalogWorkRangeLow.setStatus(_A)
_NpInputAnalogTraps_ObjectIdentity=ObjectIdentity
npInputAnalogTraps=_NpInputAnalogTraps_ObjectIdentity((1,3,6,1,4,1,25728,8200,2))
_NpInputAnalogTrapPrefix_ObjectIdentity=ObjectIdentity
npInputAnalogTrapPrefix=_NpInputAnalogTrapPrefix_ObjectIdentity((1,3,6,1,4,1,25728,8200,2,0))
class _NpInputAnalogTrapSensorN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_NpInputAnalogTrapSensorN_Type.__name__=_D
_NpInputAnalogTrapSensorN_Object=MibScalar
npInputAnalogTrapSensorN=_NpInputAnalogTrapSensorN_Object((1,3,6,1,4,1,25728,8200,2,1),_NpInputAnalogTrapSensorN_Type())
npInputAnalogTrapSensorN.setMaxAccess(_F)
if mibBuilder.loadTexts:npInputAnalogTrapSensorN.setStatus(_A)
class _NpInputAnalogTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,5)));namedValues=NamedValues(*((_u,0),(_v,1),('safe',2),(_w,3),(_x,5)))
_NpInputAnalogTrapStatus_Type.__name__=_D
_NpInputAnalogTrapStatus_Object=MibScalar
npInputAnalogTrapStatus=_NpInputAnalogTrapStatus_Object((1,3,6,1,4,1,25728,8200,2,2),_NpInputAnalogTrapStatus_Type())
npInputAnalogTrapStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:npInputAnalogTrapStatus.setStatus(_A)
_NpInputAnalogTrapCurrent_Type=Integer32
_NpInputAnalogTrapCurrent_Object=MibScalar
npInputAnalogTrapCurrent=_NpInputAnalogTrapCurrent_Object((1,3,6,1,4,1,25728,8200,2,3),_NpInputAnalogTrapCurrent_Type())
npInputAnalogTrapCurrent.setMaxAccess(_F)
if mibBuilder.loadTexts:npInputAnalogTrapCurrent.setStatus(_A)
_NpInputAnalogTrapVoltage_Type=Integer32
_NpInputAnalogTrapVoltage_Object=MibScalar
npInputAnalogTrapVoltage=_NpInputAnalogTrapVoltage_Object((1,3,6,1,4,1,25728,8200,2,4),_NpInputAnalogTrapVoltage_Type())
npInputAnalogTrapVoltage.setMaxAccess(_F)
if mibBuilder.loadTexts:npInputAnalogTrapVoltage.setStatus(_A)
_NpInputAnalogTrapResistance_Type=Unsigned32
_NpInputAnalogTrapResistance_Object=MibScalar
npInputAnalogTrapResistance=_NpInputAnalogTrapResistance_Object((1,3,6,1,4,1,25728,8200,2,5),_NpInputAnalogTrapResistance_Type())
npInputAnalogTrapResistance.setMaxAccess(_F)
if mibBuilder.loadTexts:npInputAnalogTrapResistance.setStatus(_A)
_NpInputAnalogTrapMemo_Type=DisplayString
_NpInputAnalogTrapMemo_Object=MibScalar
npInputAnalogTrapMemo=_NpInputAnalogTrapMemo_Object((1,3,6,1,4,1,25728,8200,2,6),_NpInputAnalogTrapMemo_Type())
npInputAnalogTrapMemo.setMaxAccess(_F)
if mibBuilder.loadTexts:npInputAnalogTrapMemo.setStatus(_A)
class _NpInputAnalogTrapPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_G,0),(_H,1),('temporaryOff',3)))
_NpInputAnalogTrapPower_Type.__name__=_D
_NpInputAnalogTrapPower_Object=MibScalar
npInputAnalogTrapPower=_NpInputAnalogTrapPower_Object((1,3,6,1,4,1,25728,8200,2,7),_NpInputAnalogTrapPower_Type())
npInputAnalogTrapPower.setMaxAccess(_F)
if mibBuilder.loadTexts:npInputAnalogTrapPower.setStatus(_A)
_NpInputAnalogTrapWorkRangeHigh_Type=Integer32
_NpInputAnalogTrapWorkRangeHigh_Object=MibScalar
npInputAnalogTrapWorkRangeHigh=_NpInputAnalogTrapWorkRangeHigh_Object((1,3,6,1,4,1,25728,8200,2,11),_NpInputAnalogTrapWorkRangeHigh_Type())
npInputAnalogTrapWorkRangeHigh.setMaxAccess(_F)
if mibBuilder.loadTexts:npInputAnalogTrapWorkRangeHigh.setStatus(_A)
_NpInputAnalogTrapSafeRangeHigh_Type=Integer32
_NpInputAnalogTrapSafeRangeHigh_Object=MibScalar
npInputAnalogTrapSafeRangeHigh=_NpInputAnalogTrapSafeRangeHigh_Object((1,3,6,1,4,1,25728,8200,2,12),_NpInputAnalogTrapSafeRangeHigh_Type())
npInputAnalogTrapSafeRangeHigh.setMaxAccess(_F)
if mibBuilder.loadTexts:npInputAnalogTrapSafeRangeHigh.setStatus(_A)
_NpInputAnalogTrapSafeRangeLow_Type=Integer32
_NpInputAnalogTrapSafeRangeLow_Object=MibScalar
npInputAnalogTrapSafeRangeLow=_NpInputAnalogTrapSafeRangeLow_Object((1,3,6,1,4,1,25728,8200,2,13),_NpInputAnalogTrapSafeRangeLow_Type())
npInputAnalogTrapSafeRangeLow.setMaxAccess(_F)
if mibBuilder.loadTexts:npInputAnalogTrapSafeRangeLow.setStatus(_A)
_NpInputAnalogTrapWorkRangeLow_Type=Integer32
_NpInputAnalogTrapWorkRangeLow_Object=MibScalar
npInputAnalogTrapWorkRangeLow=_NpInputAnalogTrapWorkRangeLow_Object((1,3,6,1,4,1,25728,8200,2,14),_NpInputAnalogTrapWorkRangeLow_Type())
npInputAnalogTrapWorkRangeLow.setMaxAccess(_F)
if mibBuilder.loadTexts:npInputAnalogTrapWorkRangeLow.setStatus(_A)
_NpCurLoop_ObjectIdentity=ObjectIdentity
npCurLoop=_NpCurLoop_ObjectIdentity((1,3,6,1,4,1,25728,8300))
_NpCurLoopTable_Object=MibTable
npCurLoopTable=_NpCurLoopTable_Object((1,3,6,1,4,1,25728,8300,1))
if mibBuilder.loadTexts:npCurLoopTable.setStatus(_A)
_NpCurLoopEntry_Object=MibTableRow
npCurLoopEntry=_NpCurLoopEntry_Object((1,3,6,1,4,1,25728,8300,1,1))
npCurLoopEntry.setIndexNames((0,_B,_y))
if mibBuilder.loadTexts:npCurLoopEntry.setStatus(_A)
class _NpCurLoopN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NpCurLoopN_Type.__name__=_D
_NpCurLoopN_Object=MibTableColumn
npCurLoopN=_NpCurLoopN_Object((1,3,6,1,4,1,25728,8300,1,1,1),_NpCurLoopN_Type())
npCurLoopN.setMaxAccess(_C)
if mibBuilder.loadTexts:npCurLoopN.setStatus(_A)
class _NpCurLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('ok',0),('alert',1),('cut',2),('short',3),(_z,4)))
_NpCurLoopStatus_Type.__name__=_D
_NpCurLoopStatus_Object=MibTableColumn
npCurLoopStatus=_NpCurLoopStatus_Object((1,3,6,1,4,1,25728,8300,1,1,2),_NpCurLoopStatus_Type())
npCurLoopStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npCurLoopStatus.setStatus(_A)
class _NpCurLoopI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_NpCurLoopI_Type.__name__=_D
_NpCurLoopI_Object=MibTableColumn
npCurLoopI=_NpCurLoopI_Object((1,3,6,1,4,1,25728,8300,1,1,3),_NpCurLoopI_Type())
npCurLoopI.setMaxAccess(_C)
if mibBuilder.loadTexts:npCurLoopI.setStatus(_A)
class _NpCurLoopV_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_NpCurLoopV_Type.__name__=_D
_NpCurLoopV_Object=MibTableColumn
npCurLoopV=_NpCurLoopV_Object((1,3,6,1,4,1,25728,8300,1,1,4),_NpCurLoopV_Type())
npCurLoopV.setMaxAccess(_C)
if mibBuilder.loadTexts:npCurLoopV.setStatus(_A)
class _NpCurLoopR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_NpCurLoopR_Type.__name__=_D
_NpCurLoopR_Object=MibTableColumn
npCurLoopR=_NpCurLoopR_Object((1,3,6,1,4,1,25728,8300,1,1,5),_NpCurLoopR_Type())
npCurLoopR.setMaxAccess(_C)
if mibBuilder.loadTexts:npCurLoopR.setStatus(_A)
class _NpCurLoopPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_H,1),('cyclePower',2)))
_NpCurLoopPower_Type.__name__=_D
_NpCurLoopPower_Object=MibTableColumn
npCurLoopPower=_NpCurLoopPower_Object((1,3,6,1,4,1,25728,8300,1,1,7),_NpCurLoopPower_Type())
npCurLoopPower.setMaxAccess(_E)
if mibBuilder.loadTexts:npCurLoopPower.setStatus(_A)
_NpCurLoopTraps_ObjectIdentity=ObjectIdentity
npCurLoopTraps=_NpCurLoopTraps_ObjectIdentity((1,3,6,1,4,1,25728,8300,2))
_NpCurLoopTrapPrefix_ObjectIdentity=ObjectIdentity
npCurLoopTrapPrefix=_NpCurLoopTrapPrefix_ObjectIdentity((1,3,6,1,4,1,25728,8300,2,0))
class _NpCurLoopTrapN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NpCurLoopTrapN_Type.__name__=_D
_NpCurLoopTrapN_Object=MibScalar
npCurLoopTrapN=_NpCurLoopTrapN_Object((1,3,6,1,4,1,25728,8300,2,1),_NpCurLoopTrapN_Type())
npCurLoopTrapN.setMaxAccess(_C)
if mibBuilder.loadTexts:npCurLoopTrapN.setStatus(_A)
class _NpCurLoopTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('ok',0),('alert',1),('cut',2),('short',3),(_z,4)))
_NpCurLoopTrapStatus_Type.__name__=_D
_NpCurLoopTrapStatus_Object=MibScalar
npCurLoopTrapStatus=_NpCurLoopTrapStatus_Object((1,3,6,1,4,1,25728,8300,2,2),_NpCurLoopTrapStatus_Type())
npCurLoopTrapStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npCurLoopTrapStatus.setStatus(_A)
class _NpCurLoopTrapI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_NpCurLoopTrapI_Type.__name__=_D
_NpCurLoopTrapI_Object=MibScalar
npCurLoopTrapI=_NpCurLoopTrapI_Object((1,3,6,1,4,1,25728,8300,2,3),_NpCurLoopTrapI_Type())
npCurLoopTrapI.setMaxAccess(_C)
if mibBuilder.loadTexts:npCurLoopTrapI.setStatus(_A)
class _NpCurLoopTrapV_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_NpCurLoopTrapV_Type.__name__=_D
_NpCurLoopTrapV_Object=MibScalar
npCurLoopTrapV=_NpCurLoopTrapV_Object((1,3,6,1,4,1,25728,8300,2,4),_NpCurLoopTrapV_Type())
npCurLoopTrapV.setMaxAccess(_C)
if mibBuilder.loadTexts:npCurLoopTrapV.setStatus(_A)
class _NpCurLoopTrapR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_NpCurLoopTrapR_Type.__name__=_D
_NpCurLoopTrapR_Object=MibScalar
npCurLoopTrapR=_NpCurLoopTrapR_Object((1,3,6,1,4,1,25728,8300,2,5),_NpCurLoopTrapR_Type())
npCurLoopTrapR.setMaxAccess(_C)
if mibBuilder.loadTexts:npCurLoopTrapR.setStatus(_A)
class _NpCurLoopTrapPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_NpCurLoopTrapPower_Type.__name__=_D
_NpCurLoopTrapPower_Object=MibScalar
npCurLoopTrapPower=_NpCurLoopTrapPower_Object((1,3,6,1,4,1,25728,8300,2,7),_NpCurLoopTrapPower_Type())
npCurLoopTrapPower.setMaxAccess(_E)
if mibBuilder.loadTexts:npCurLoopTrapPower.setStatus(_A)
_NpRelHumidity_ObjectIdentity=ObjectIdentity
npRelHumidity=_NpRelHumidity_ObjectIdentity((1,3,6,1,4,1,25728,8400))
_NpRelHumTable_Object=MibTable
npRelHumTable=_NpRelHumTable_Object((1,3,6,1,4,1,25728,8400,1))
if mibBuilder.loadTexts:npRelHumTable.setStatus(_A)
_NpRelHumEntry_Object=MibTableRow
npRelHumEntry=_NpRelHumEntry_Object((1,3,6,1,4,1,25728,8400,1,1))
npRelHumEntry.setIndexNames((0,_B,_A0))
if mibBuilder.loadTexts:npRelHumEntry.setStatus(_A)
class _NpRelHumN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_NpRelHumN_Type.__name__=_D
_NpRelHumN_Object=MibTableColumn
npRelHumN=_NpRelHumN_Object((1,3,6,1,4,1,25728,8400,1,1,1),_NpRelHumN_Type())
npRelHumN.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumN.setStatus(_A)
class _NpRelHumValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NpRelHumValue_Type.__name__=_D
_NpRelHumValue_Object=MibTableColumn
npRelHumValue=_NpRelHumValue_Object((1,3,6,1,4,1,25728,8400,1,1,2),_NpRelHumValue_Type())
npRelHumValue.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumValue.setStatus(_A)
class _NpRelHumStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_j,1),(_k,2),(_l,3)))
_NpRelHumStatus_Type.__name__=_D
_NpRelHumStatus_Object=MibTableColumn
npRelHumStatus=_NpRelHumStatus_Object((1,3,6,1,4,1,25728,8400,1,1,3),_NpRelHumStatus_Type())
npRelHumStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumStatus.setStatus(_A)
class _NpRelHumTempValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,200))
_NpRelHumTempValue_Type.__name__=_D
_NpRelHumTempValue_Object=MibTableColumn
npRelHumTempValue=_NpRelHumTempValue_Object((1,3,6,1,4,1,25728,8400,1,1,4),_NpRelHumTempValue_Type())
npRelHumTempValue.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumTempValue.setStatus(_A)
class _NpRelHumTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_j,1),(_k,2),(_l,3)))
_NpRelHumTempStatus_Type.__name__=_D
_NpRelHumTempStatus_Object=MibTableColumn
npRelHumTempStatus=_NpRelHumTempStatus_Object((1,3,6,1,4,1,25728,8400,1,1,5),_NpRelHumTempStatus_Type())
npRelHumTempStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumTempStatus.setStatus(_A)
_NpRelHumMemo_Type=DisplayString
_NpRelHumMemo_Object=MibTableColumn
npRelHumMemo=_NpRelHumMemo_Object((1,3,6,1,4,1,25728,8400,1,1,6),_NpRelHumMemo_Type())
npRelHumMemo.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumMemo.setStatus(_A)
class _NpRelHumSafeRangeHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NpRelHumSafeRangeHigh_Type.__name__=_D
_NpRelHumSafeRangeHigh_Object=MibTableColumn
npRelHumSafeRangeHigh=_NpRelHumSafeRangeHigh_Object((1,3,6,1,4,1,25728,8400,1,1,7),_NpRelHumSafeRangeHigh_Type())
npRelHumSafeRangeHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumSafeRangeHigh.setStatus(_A)
class _NpRelHumSafeRangeLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NpRelHumSafeRangeLow_Type.__name__=_D
_NpRelHumSafeRangeLow_Object=MibTableColumn
npRelHumSafeRangeLow=_NpRelHumSafeRangeLow_Object((1,3,6,1,4,1,25728,8400,1,1,8),_NpRelHumSafeRangeLow_Type())
npRelHumSafeRangeLow.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumSafeRangeLow.setStatus(_A)
class _NpRelHumTempSafeRangeHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-55,150))
_NpRelHumTempSafeRangeHigh_Type.__name__=_D
_NpRelHumTempSafeRangeHigh_Object=MibTableColumn
npRelHumTempSafeRangeHigh=_NpRelHumTempSafeRangeHigh_Object((1,3,6,1,4,1,25728,8400,1,1,9),_NpRelHumTempSafeRangeHigh_Type())
npRelHumTempSafeRangeHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumTempSafeRangeHigh.setStatus(_A)
class _NpRelHumTempSafeRangeLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-55,150))
_NpRelHumTempSafeRangeLow_Type.__name__=_D
_NpRelHumTempSafeRangeLow_Object=MibTableColumn
npRelHumTempSafeRangeLow=_NpRelHumTempSafeRangeLow_Object((1,3,6,1,4,1,25728,8400,1,1,10),_NpRelHumTempSafeRangeLow_Type())
npRelHumTempSafeRangeLow.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumTempSafeRangeLow.setStatus(_A)
_NpRelHumTrapData_ObjectIdentity=ObjectIdentity
npRelHumTrapData=_NpRelHumTrapData_ObjectIdentity((1,3,6,1,4,1,25728,8400,3))
class _NpRelHumTrapDataN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_NpRelHumTrapDataN_Type.__name__=_D
_NpRelHumTrapDataN_Object=MibScalar
npRelHumTrapDataN=_NpRelHumTrapDataN_Object((1,3,6,1,4,1,25728,8400,3,1),_NpRelHumTrapDataN_Type())
npRelHumTrapDataN.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumTrapDataN.setStatus(_A)
_NpRelHumTrapDataValue_Type=Integer32
_NpRelHumTrapDataValue_Object=MibScalar
npRelHumTrapDataValue=_NpRelHumTrapDataValue_Object((1,3,6,1,4,1,25728,8400,3,2),_NpRelHumTrapDataValue_Type())
npRelHumTrapDataValue.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumTrapDataValue.setStatus(_A)
class _NpRelHumTrapDataStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_j,1),(_k,2),(_l,3)))
_NpRelHumTrapDataStatus_Type.__name__=_D
_NpRelHumTrapDataStatus_Object=MibScalar
npRelHumTrapDataStatus=_NpRelHumTrapDataStatus_Object((1,3,6,1,4,1,25728,8400,3,4),_NpRelHumTrapDataStatus_Type())
npRelHumTrapDataStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumTrapDataStatus.setStatus(_A)
_NpRelHumTrapDataMemo_Type=DisplayString
_NpRelHumTrapDataMemo_Object=MibScalar
npRelHumTrapDataMemo=_NpRelHumTrapDataMemo_Object((1,3,6,1,4,1,25728,8400,3,6),_NpRelHumTrapDataMemo_Type())
npRelHumTrapDataMemo.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumTrapDataMemo.setStatus(_A)
_NpRelHumTrapDataSafeRangeHigh_Type=Integer32
_NpRelHumTrapDataSafeRangeHigh_Object=MibScalar
npRelHumTrapDataSafeRangeHigh=_NpRelHumTrapDataSafeRangeHigh_Object((1,3,6,1,4,1,25728,8400,3,7),_NpRelHumTrapDataSafeRangeHigh_Type())
npRelHumTrapDataSafeRangeHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumTrapDataSafeRangeHigh.setStatus(_A)
_NpRelHumTrapDataSafeRangeLow_Type=Integer32
_NpRelHumTrapDataSafeRangeLow_Object=MibScalar
npRelHumTrapDataSafeRangeLow=_NpRelHumTrapDataSafeRangeLow_Object((1,3,6,1,4,1,25728,8400,3,8),_NpRelHumTrapDataSafeRangeLow_Type())
npRelHumTrapDataSafeRangeLow.setMaxAccess(_C)
if mibBuilder.loadTexts:npRelHumTrapDataSafeRangeLow.setStatus(_A)
_NpRelHumTrap_ObjectIdentity=ObjectIdentity
npRelHumTrap=_NpRelHumTrap_ObjectIdentity((1,3,6,1,4,1,25728,8400,6))
_NpRelHumTrapAllEvents_ObjectIdentity=ObjectIdentity
npRelHumTrapAllEvents=_NpRelHumTrapAllEvents_ObjectIdentity((1,3,6,1,4,1,25728,8400,6,127))
_NpRelHumTrapTemp_ObjectIdentity=ObjectIdentity
npRelHumTrapTemp=_NpRelHumTrapTemp_ObjectIdentity((1,3,6,1,4,1,25728,8400,7))
_NpRelHumTrapTempAllEvents_ObjectIdentity=ObjectIdentity
npRelHumTrapTempAllEvents=_NpRelHumTrapTempAllEvents_ObjectIdentity((1,3,6,1,4,1,25728,8400,7,127))
_NpThermo_ObjectIdentity=ObjectIdentity
npThermo=_NpThermo_ObjectIdentity((1,3,6,1,4,1,25728,8800))
_NpThermoTable_Object=MibTable
npThermoTable=_NpThermoTable_Object((1,3,6,1,4,1,25728,8800,1))
if mibBuilder.loadTexts:npThermoTable.setStatus(_A)
_NpThermoEntry_Object=MibTableRow
npThermoEntry=_NpThermoEntry_Object((1,3,6,1,4,1,25728,8800,1,1))
npThermoEntry.setIndexNames((0,_B,_A1))
if mibBuilder.loadTexts:npThermoEntry.setStatus(_A)
class _NpThermoSensorN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NpThermoSensorN_Type.__name__=_D
_NpThermoSensorN_Object=MibTableColumn
npThermoSensorN=_NpThermoSensorN_Object((1,3,6,1,4,1,25728,8800,1,1,1),_NpThermoSensorN_Type())
npThermoSensorN.setMaxAccess(_C)
if mibBuilder.loadTexts:npThermoSensorN.setStatus(_A)
class _NpThermoValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,280))
_NpThermoValue_Type.__name__=_D
_NpThermoValue_Object=MibTableColumn
npThermoValue=_NpThermoValue_Object((1,3,6,1,4,1,25728,8800,1,1,2),_NpThermoValue_Type())
npThermoValue.setMaxAccess(_C)
if mibBuilder.loadTexts:npThermoValue.setStatus(_A)
class _NpThermoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_h,0),(_m,1),('norm',2),(_d,3)))
_NpThermoStatus_Type.__name__=_D
_NpThermoStatus_Object=MibTableColumn
npThermoStatus=_NpThermoStatus_Object((1,3,6,1,4,1,25728,8800,1,1,3),_NpThermoStatus_Type())
npThermoStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npThermoStatus.setStatus(_A)
class _NpThermoLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,280))
_NpThermoLow_Type.__name__=_D
_NpThermoLow_Object=MibTableColumn
npThermoLow=_NpThermoLow_Object((1,3,6,1,4,1,25728,8800,1,1,4),_NpThermoLow_Type())
npThermoLow.setMaxAccess(_C)
if mibBuilder.loadTexts:npThermoLow.setStatus(_A)
class _NpThermoHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,280))
_NpThermoHigh_Type.__name__=_D
_NpThermoHigh_Object=MibTableColumn
npThermoHigh=_NpThermoHigh_Object((1,3,6,1,4,1,25728,8800,1,1,5),_NpThermoHigh_Type())
npThermoHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:npThermoHigh.setStatus(_A)
_NpThermoMemo_Type=DisplayString
_NpThermoMemo_Object=MibTableColumn
npThermoMemo=_NpThermoMemo_Object((1,3,6,1,4,1,25728,8800,1,1,6),_NpThermoMemo_Type())
npThermoMemo.setMaxAccess(_C)
if mibBuilder.loadTexts:npThermoMemo.setStatus(_A)
_NpThermoValuePrecise_Type=FixedPoint1000
_NpThermoValuePrecise_Object=MibTableColumn
npThermoValuePrecise=_NpThermoValuePrecise_Object((1,3,6,1,4,1,25728,8800,1,1,7),_NpThermoValuePrecise_Type())
npThermoValuePrecise.setMaxAccess(_C)
if mibBuilder.loadTexts:npThermoValuePrecise.setStatus(_A)
_NpThermoTraps_ObjectIdentity=ObjectIdentity
npThermoTraps=_NpThermoTraps_ObjectIdentity((1,3,6,1,4,1,25728,8800,2))
_NpThermoTrapPrefix_ObjectIdentity=ObjectIdentity
npThermoTrapPrefix=_NpThermoTrapPrefix_ObjectIdentity((1,3,6,1,4,1,25728,8800,2,0))
class _NpThermoTrapSensorN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NpThermoTrapSensorN_Type.__name__=_D
_NpThermoTrapSensorN_Object=MibScalar
npThermoTrapSensorN=_NpThermoTrapSensorN_Object((1,3,6,1,4,1,25728,8800,2,1),_NpThermoTrapSensorN_Type())
npThermoTrapSensorN.setMaxAccess(_C)
if mibBuilder.loadTexts:npThermoTrapSensorN.setStatus(_A)
class _NpThermoTrapValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,280))
_NpThermoTrapValue_Type.__name__=_D
_NpThermoTrapValue_Object=MibScalar
npThermoTrapValue=_NpThermoTrapValue_Object((1,3,6,1,4,1,25728,8800,2,2),_NpThermoTrapValue_Type())
npThermoTrapValue.setMaxAccess(_C)
if mibBuilder.loadTexts:npThermoTrapValue.setStatus(_A)
class _NpThermoTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_h,0),(_m,1),('norm',2),(_d,3)))
_NpThermoTrapStatus_Type.__name__=_D
_NpThermoTrapStatus_Object=MibScalar
npThermoTrapStatus=_NpThermoTrapStatus_Object((1,3,6,1,4,1,25728,8800,2,3),_NpThermoTrapStatus_Type())
npThermoTrapStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npThermoTrapStatus.setStatus(_A)
class _NpThermoTrapLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,280))
_NpThermoTrapLow_Type.__name__=_D
_NpThermoTrapLow_Object=MibScalar
npThermoTrapLow=_NpThermoTrapLow_Object((1,3,6,1,4,1,25728,8800,2,4),_NpThermoTrapLow_Type())
npThermoTrapLow.setMaxAccess(_C)
if mibBuilder.loadTexts:npThermoTrapLow.setStatus(_A)
class _NpThermoTrapHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,280))
_NpThermoTrapHigh_Type.__name__=_D
_NpThermoTrapHigh_Object=MibScalar
npThermoTrapHigh=_NpThermoTrapHigh_Object((1,3,6,1,4,1,25728,8800,2,5),_NpThermoTrapHigh_Type())
npThermoTrapHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:npThermoTrapHigh.setStatus(_A)
_NpThermoTrapMemo_Type=DisplayString
_NpThermoTrapMemo_Object=MibScalar
npThermoTrapMemo=_NpThermoTrapMemo_Object((1,3,6,1,4,1,25728,8800,2,6),_NpThermoTrapMemo_Type())
npThermoTrapMemo.setMaxAccess(_C)
if mibBuilder.loadTexts:npThermoTrapMemo.setStatus(_A)
_NpIo_ObjectIdentity=ObjectIdentity
npIo=_NpIo_ObjectIdentity((1,3,6,1,4,1,25728,8900))
_NpIoTable_Object=MibTable
npIoTable=_NpIoTable_Object((1,3,6,1,4,1,25728,8900,1))
if mibBuilder.loadTexts:npIoTable.setStatus(_A)
_NpIoEntry_Object=MibTableRow
npIoEntry=_NpIoEntry_Object((1,3,6,1,4,1,25728,8900,1,1))
npIoEntry.setIndexNames((0,_B,_A2))
if mibBuilder.loadTexts:npIoEntry.setStatus(_A)
class _NpIoLineN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NpIoLineN_Type.__name__=_D
_NpIoLineN_Object=MibTableColumn
npIoLineN=_NpIoLineN_Object((1,3,6,1,4,1,25728,8900,1,1,1),_NpIoLineN_Type())
npIoLineN.setMaxAccess(_C)
if mibBuilder.loadTexts:npIoLineN.setStatus(_A)
class _NpIoLevelIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpIoLevelIn_Type.__name__=_D
_NpIoLevelIn_Object=MibTableColumn
npIoLevelIn=_NpIoLevelIn_Object((1,3,6,1,4,1,25728,8900,1,1,2),_NpIoLevelIn_Type())
npIoLevelIn.setMaxAccess(_C)
if mibBuilder.loadTexts:npIoLevelIn.setStatus(_A)
class _NpIoLevelOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*((_c,-1),(_m,0),(_d,1)))
_NpIoLevelOut_Type.__name__=_D
_NpIoLevelOut_Object=MibTableColumn
npIoLevelOut=_NpIoLevelOut_Object((1,3,6,1,4,1,25728,8900,1,1,3),_NpIoLevelOut_Type())
npIoLevelOut.setMaxAccess(_E)
if mibBuilder.loadTexts:npIoLevelOut.setStatus(_A)
_NpIoMemo_Type=DisplayString
_NpIoMemo_Object=MibTableColumn
npIoMemo=_NpIoMemo_Object((1,3,6,1,4,1,25728,8900,1,1,6),_NpIoMemo_Type())
npIoMemo.setMaxAccess(_C)
if mibBuilder.loadTexts:npIoMemo.setStatus(_A)
_NpIoPulseCounter_Type=Counter32
_NpIoPulseCounter_Object=MibTableColumn
npIoPulseCounter=_NpIoPulseCounter_Object((1,3,6,1,4,1,25728,8900,1,1,9),_NpIoPulseCounter_Type())
npIoPulseCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:npIoPulseCounter.setStatus(_A)
class _NpIoSinglePulseDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,25500))
_NpIoSinglePulseDuration_Type.__name__=_D
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
_NpIoTrapLineN_Type.__name__=_D
_NpIoTrapLineN_Object=MibScalar
npIoTrapLineN=_NpIoTrapLineN_Object((1,3,6,1,4,1,25728,8900,2,1),_NpIoTrapLineN_Type())
npIoTrapLineN.setMaxAccess(_C)
if mibBuilder.loadTexts:npIoTrapLineN.setStatus(_A)
class _NpIoTrapLevelIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpIoTrapLevelIn_Type.__name__=_D
_NpIoTrapLevelIn_Object=MibScalar
npIoTrapLevelIn=_NpIoTrapLevelIn_Object((1,3,6,1,4,1,25728,8900,2,2),_NpIoTrapLevelIn_Type())
npIoTrapLevelIn.setMaxAccess(_C)
if mibBuilder.loadTexts:npIoTrapLevelIn.setStatus(_A)
_NpIoTrapMemo_Type=DisplayString
_NpIoTrapMemo_Object=MibScalar
npIoTrapMemo=_NpIoTrapMemo_Object((1,3,6,1,4,1,25728,8900,2,6),_NpIoTrapMemo_Type())
npIoTrapMemo.setMaxAccess(_C)
if mibBuilder.loadTexts:npIoTrapMemo.setStatus(_A)
_NpIoTrapLevelLegend_Type=DisplayString
_NpIoTrapLevelLegend_Object=MibScalar
npIoTrapLevelLegend=_NpIoTrapLevelLegend_Object((1,3,6,1,4,1,25728,8900,2,7),_NpIoTrapLevelLegend_Type())
npIoTrapLevelLegend.setMaxAccess(_C)
if mibBuilder.loadTexts:npIoTrapLevelLegend.setStatus(_A)
_NpVoltage_ObjectIdentity=ObjectIdentity
npVoltage=_NpVoltage_ObjectIdentity((1,3,6,1,4,1,25728,9000))
_NpVoltageTable_Object=MibTable
npVoltageTable=_NpVoltageTable_Object((1,3,6,1,4,1,25728,9000,1))
if mibBuilder.loadTexts:npVoltageTable.setStatus(_A)
_NpVoltageEntry_Object=MibTableRow
npVoltageEntry=_NpVoltageEntry_Object((1,3,6,1,4,1,25728,9000,1,1))
npVoltageEntry.setIndexNames((0,_B,_A3))
if mibBuilder.loadTexts:npVoltageEntry.setStatus(_A)
class _NpVoltageN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_NpVoltageN_Type.__name__=_D
_NpVoltageN_Object=MibTableColumn
npVoltageN=_NpVoltageN_Object((1,3,6,1,4,1,25728,9000,1,1,1),_NpVoltageN_Type())
npVoltageN.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageN.setStatus(_A)
class _NpVoltageRMS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_NpVoltageRMS_Type.__name__=_D
_NpVoltageRMS_Object=MibTableColumn
npVoltageRMS=_NpVoltageRMS_Object((1,3,6,1,4,1,25728,9000,1,1,2),_NpVoltageRMS_Type())
npVoltageRMS.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageRMS.setStatus(_A)
class _NpVoltageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_P,1),(_e,2),(_f,3),(_g,4)))
_NpVoltageStatus_Type.__name__=_D
_NpVoltageStatus_Object=MibTableColumn
npVoltageStatus=_NpVoltageStatus_Object((1,3,6,1,4,1,25728,9000,1,1,3),_NpVoltageStatus_Type())
npVoltageStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageStatus.setStatus(_A)
class _NpVoltageFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_NpVoltageFreq_Type.__name__=_D
_NpVoltageFreq_Object=MibTableColumn
npVoltageFreq=_NpVoltageFreq_Object((1,3,6,1,4,1,25728,9000,1,1,4),_NpVoltageFreq_Type())
npVoltageFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageFreq.setStatus(_A)
class _NpVoltageFreqStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_P,1),(_e,2),(_f,3),(_g,4)))
_NpVoltageFreqStatus_Type.__name__=_D
_NpVoltageFreqStatus_Object=MibTableColumn
npVoltageFreqStatus=_NpVoltageFreqStatus_Object((1,3,6,1,4,1,25728,9000,1,1,5),_NpVoltageFreqStatus_Type())
npVoltageFreqStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageFreqStatus.setStatus(_A)
_NpVoltageMemo_Type=DisplayString
_NpVoltageMemo_Object=MibTableColumn
npVoltageMemo=_NpVoltageMemo_Object((1,3,6,1,4,1,25728,9000,1,1,6),_NpVoltageMemo_Type())
npVoltageMemo.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageMemo.setStatus(_A)
_NpVoltageSagCounter_Type=Counter32
_NpVoltageSagCounter_Object=MibTableColumn
npVoltageSagCounter=_NpVoltageSagCounter_Object((1,3,6,1,4,1,25728,9000,1,1,10),_NpVoltageSagCounter_Type())
npVoltageSagCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:npVoltageSagCounter.setStatus(_A)
class _NpVoltageSagStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),(_P,1),(_d,2),('medium',3),('small',4),('noSags',5)))
_NpVoltageSagStatus_Type.__name__=_D
_NpVoltageSagStatus_Object=MibTableColumn
npVoltageSagStatus=_NpVoltageSagStatus_Object((1,3,6,1,4,1,25728,9000,1,1,11),_NpVoltageSagStatus_Type())
npVoltageSagStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageSagStatus.setStatus(_A)
class _NpVoltageSagSmallThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NpVoltageSagSmallThreshold_Type.__name__=_D
_NpVoltageSagSmallThreshold_Object=MibTableColumn
npVoltageSagSmallThreshold=_NpVoltageSagSmallThreshold_Object((1,3,6,1,4,1,25728,9000,1,1,12),_NpVoltageSagSmallThreshold_Type())
npVoltageSagSmallThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:npVoltageSagSmallThreshold.setStatus(_A)
class _NpVoltageSagMediumThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NpVoltageSagMediumThreshold_Type.__name__=_D
_NpVoltageSagMediumThreshold_Object=MibTableColumn
npVoltageSagMediumThreshold=_NpVoltageSagMediumThreshold_Object((1,3,6,1,4,1,25728,9000,1,1,13),_NpVoltageSagMediumThreshold_Type())
npVoltageSagMediumThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:npVoltageSagMediumThreshold.setStatus(_A)
class _NpVoltageSagBigThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NpVoltageSagBigThreshold_Type.__name__=_D
_NpVoltageSagBigThreshold_Object=MibTableColumn
npVoltageSagBigThreshold=_NpVoltageSagBigThreshold_Object((1,3,6,1,4,1,25728,9000,1,1,14),_NpVoltageSagBigThreshold_Type())
npVoltageSagBigThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:npVoltageSagBigThreshold.setStatus(_A)
class _NpVoltageStandard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,240))
_NpVoltageStandard_Type.__name__=_D
_NpVoltageStandard_Object=MibTableColumn
npVoltageStandard=_NpVoltageStandard_Object((1,3,6,1,4,1,25728,9000,1,1,20),_NpVoltageStandard_Type())
npVoltageStandard.setMaxAccess(_E)
if mibBuilder.loadTexts:npVoltageStandard.setStatus(_A)
class _NpVoltagePeak_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_NpVoltagePeak_Type.__name__=_D
_NpVoltagePeak_Object=MibTableColumn
npVoltagePeak=_NpVoltagePeak_Object((1,3,6,1,4,1,25728,9000,1,1,30),_NpVoltagePeak_Type())
npVoltagePeak.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltagePeak.setStatus(_A)
class _NpVoltagePeakStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_P,1),(_A4,2),('noPeaks',3)))
_NpVoltagePeakStatus_Type.__name__=_D
_NpVoltagePeakStatus_Object=MibTableColumn
npVoltagePeakStatus=_NpVoltagePeakStatus_Object((1,3,6,1,4,1,25728,9000,1,1,31),_NpVoltagePeakStatus_Type())
npVoltagePeakStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltagePeakStatus.setStatus(_A)
_NpVoltageTraps_ObjectIdentity=ObjectIdentity
npVoltageTraps=_NpVoltageTraps_ObjectIdentity((1,3,6,1,4,1,25728,9000,2))
_NpVoltageTrapPrefix_ObjectIdentity=ObjectIdentity
npVoltageTrapPrefix=_NpVoltageTrapPrefix_ObjectIdentity((1,3,6,1,4,1,25728,9000,2,0))
class _NpVoltageTrapN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_NpVoltageTrapN_Type.__name__=_D
_NpVoltageTrapN_Object=MibScalar
npVoltageTrapN=_NpVoltageTrapN_Object((1,3,6,1,4,1,25728,9000,2,1),_NpVoltageTrapN_Type())
npVoltageTrapN.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageTrapN.setStatus(_A)
class _NpVoltageTrapRMS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_NpVoltageTrapRMS_Type.__name__=_D
_NpVoltageTrapRMS_Object=MibScalar
npVoltageTrapRMS=_NpVoltageTrapRMS_Object((1,3,6,1,4,1,25728,9000,2,2),_NpVoltageTrapRMS_Type())
npVoltageTrapRMS.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageTrapRMS.setStatus(_A)
class _NpVoltageTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_P,1),(_e,2),(_f,3),(_g,4)))
_NpVoltageTrapStatus_Type.__name__=_D
_NpVoltageTrapStatus_Object=MibScalar
npVoltageTrapStatus=_NpVoltageTrapStatus_Object((1,3,6,1,4,1,25728,9000,2,3),_NpVoltageTrapStatus_Type())
npVoltageTrapStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageTrapStatus.setStatus(_A)
class _NpVoltageTrapFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_NpVoltageTrapFreq_Type.__name__=_D
_NpVoltageTrapFreq_Object=MibScalar
npVoltageTrapFreq=_NpVoltageTrapFreq_Object((1,3,6,1,4,1,25728,9000,2,4),_NpVoltageTrapFreq_Type())
npVoltageTrapFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageTrapFreq.setStatus(_A)
class _NpVoltageTrapFreqStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_P,1),(_e,2),(_f,3),(_g,4)))
_NpVoltageTrapFreqStatus_Type.__name__=_D
_NpVoltageTrapFreqStatus_Object=MibScalar
npVoltageTrapFreqStatus=_NpVoltageTrapFreqStatus_Object((1,3,6,1,4,1,25728,9000,2,5),_NpVoltageTrapFreqStatus_Type())
npVoltageTrapFreqStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageTrapFreqStatus.setStatus(_A)
_NpVoltageTrapMemo_Type=DisplayString
_NpVoltageTrapMemo_Object=MibScalar
npVoltageTrapMemo=_NpVoltageTrapMemo_Object((1,3,6,1,4,1,25728,9000,2,6),_NpVoltageTrapMemo_Type())
npVoltageTrapMemo.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageTrapMemo.setStatus(_A)
_NpVoltageTrapSagCounter_Type=Counter32
_NpVoltageTrapSagCounter_Object=MibScalar
npVoltageTrapSagCounter=_NpVoltageTrapSagCounter_Object((1,3,6,1,4,1,25728,9000,2,10),_NpVoltageTrapSagCounter_Type())
npVoltageTrapSagCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageTrapSagCounter.setStatus(_A)
class _NpVoltageTrapSagStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),(_P,1),(_d,2),('medium',3),('small',4),('noSags',5)))
_NpVoltageTrapSagStatus_Type.__name__=_D
_NpVoltageTrapSagStatus_Object=MibScalar
npVoltageTrapSagStatus=_NpVoltageTrapSagStatus_Object((1,3,6,1,4,1,25728,9000,2,11),_NpVoltageTrapSagStatus_Type())
npVoltageTrapSagStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageTrapSagStatus.setStatus(_A)
class _NpVoltageTrapPeak_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_NpVoltageTrapPeak_Type.__name__=_D
_NpVoltageTrapPeak_Object=MibScalar
npVoltageTrapPeak=_NpVoltageTrapPeak_Object((1,3,6,1,4,1,25728,9000,2,30),_NpVoltageTrapPeak_Type())
npVoltageTrapPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageTrapPeak.setStatus(_A)
class _NpVoltageTrapPeakStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_P,1),(_A4,2),('noPeaks',3)))
_NpVoltageTrapPeakStatus_Type.__name__=_D
_NpVoltageTrapPeakStatus_Object=MibScalar
npVoltageTrapPeakStatus=_NpVoltageTrapPeakStatus_Object((1,3,6,1,4,1,25728,9000,2,31),_NpVoltageTrapPeakStatus_Type())
npVoltageTrapPeakStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npVoltageTrapPeakStatus.setStatus(_A)
npGsmTrap=NotificationType((1,3,6,1,4,1,25728,3800,2,0,1))
npGsmTrap.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:npGsmTrap.setStatus(_A)
npGsmTrapUnparsedSms=NotificationType((1,3,6,1,4,1,25728,3800,2,0,2))
npGsmTrapUnparsedSms.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:npGsmTrapUnparsedSms.setStatus(_A)
npRelayTrapOff=NotificationType((1,3,6,1,4,1,25728,5500,6,100))
npRelayTrapOff.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:npRelayTrapOff.setStatus(_A)
npRelayTrapOn=NotificationType((1,3,6,1,4,1,25728,5500,6,101))
npRelayTrapOn.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:npRelayTrapOn.setStatus(_A)
npRelayTrapModeChange=NotificationType((1,3,6,1,4,1,25728,5500,6,102))
npRelayTrapModeChange.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:npRelayTrapModeChange.setStatus(_A)
npRelayTrapReset=NotificationType((1,3,6,1,4,1,25728,5500,6,103))
npRelayTrapReset.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:npRelayTrapReset.setStatus(_A)
npRelayTrapAllChannels=NotificationType((1,3,6,1,4,1,25728,5500,6,127,99))
npRelayTrapAllChannels.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:npRelayTrapAllChannels.setStatus(_A)
npExtRelayTrapOff=NotificationType((1,3,6,1,4,1,25728,5600,6,100))
npExtRelayTrapOff.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:npExtRelayTrapOff.setStatus(_A)
npExtRelayTrapOn=NotificationType((1,3,6,1,4,1,25728,5600,6,101))
npExtRelayTrapOn.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:npExtRelayTrapOn.setStatus(_A)
npExtRelayTrapModeChange=NotificationType((1,3,6,1,4,1,25728,5600,6,102))
npExtRelayTrapModeChange.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:npExtRelayTrapModeChange.setStatus(_A)
npExtRelayTrapReset=NotificationType((1,3,6,1,4,1,25728,5600,6,103))
npExtRelayTrapReset.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:npExtRelayTrapReset.setStatus(_A)
npExtRelayTrapAllChannels=NotificationType((1,3,6,1,4,1,25728,5600,6,127,99))
npExtRelayTrapAllChannels.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:npExtRelayTrapAllChannels.setStatus(_A)
npInputAnalogTrap=NotificationType((1,3,6,1,4,1,25728,8200,2,0,1))
npInputAnalogTrap.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:npInputAnalogTrap.setStatus(_A)
npCurLoopTrap=NotificationType((1,3,6,1,4,1,25728,8300,2,0,1))
npCurLoopTrap.setObjects(*((_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:npCurLoopTrap.setStatus(_A)
npRelHumTrapFail=NotificationType((1,3,6,1,4,1,25728,8400,6,100))
npRelHumTrapFail.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:npRelHumTrapFail.setStatus(_A)
npRelHumTrapBelowSafe=NotificationType((1,3,6,1,4,1,25728,8400,6,101))
npRelHumTrapBelowSafe.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:npRelHumTrapBelowSafe.setStatus(_A)
npRelHumTrapSafe=NotificationType((1,3,6,1,4,1,25728,8400,6,102))
npRelHumTrapSafe.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:npRelHumTrapSafe.setStatus(_A)
npRelHumTrapAboveSafe=NotificationType((1,3,6,1,4,1,25728,8400,6,103))
npRelHumTrapAboveSafe.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:npRelHumTrapAboveSafe.setStatus(_A)
npRelHumTrapAllChannels=NotificationType((1,3,6,1,4,1,25728,8400,6,127,99))
npRelHumTrapAllChannels.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:npRelHumTrapAllChannels.setStatus(_A)
npRelHumTrapTempFail=NotificationType((1,3,6,1,4,1,25728,8400,7,100))
npRelHumTrapTempFail.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:npRelHumTrapTempFail.setStatus(_A)
npRelHumTrapTempBelowSafe=NotificationType((1,3,6,1,4,1,25728,8400,7,101))
npRelHumTrapTempBelowSafe.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:npRelHumTrapTempBelowSafe.setStatus(_A)
npRelHumTrapTempSafe=NotificationType((1,3,6,1,4,1,25728,8400,7,102))
npRelHumTrapTempSafe.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:npRelHumTrapTempSafe.setStatus(_A)
npRelHumTrapTempAboveSafe=NotificationType((1,3,6,1,4,1,25728,8400,7,103))
npRelHumTrapTempAboveSafe.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:npRelHumTrapTempAboveSafe.setStatus(_A)
npRelHumTrapTempAllChannels=NotificationType((1,3,6,1,4,1,25728,8400,7,127,99))
npRelHumTrapTempAllChannels.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:npRelHumTrapTempAllChannels.setStatus(_A)
npThermoTrap=NotificationType((1,3,6,1,4,1,25728,8800,2,0,1))
npThermoTrap.setObjects(*((_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:npThermoTrap.setStatus(_A)
npIoTrap=NotificationType((1,3,6,1,4,1,25728,8900,2,0,1))
npIoTrap.setObjects(*((_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac)))
if mibBuilder.loadTexts:npIoTrap.setStatus(_A)
npVoltageTrap=NotificationType((1,3,6,1,4,1,25728,9000,2,0,1))
npVoltageTrap.setObjects(*((_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al)))
if mibBuilder.loadTexts:npVoltageTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'FixedPoint1000':FixedPoint1000,'lightcom':lightcom,'uniPingServerSolutionV3':uniPingServerSolutionV3,'npTrapInfo':npTrapInfo,_AS:npTrapEmailTo,'npReboot':npReboot,'npSoftReboot':npSoftReboot,'npResetStack':npResetStack,'npForcedReboot':npForcedReboot,'npGsm':npGsm,'npGsmInfo':npGsmInfo,_A5:npGsmFailed,_A6:npGsmRegistration,_A7:npGsmStrength,'npGsmSendSmsUtf8':npGsmSendSmsUtf8,'npGsmSendSmsWin1251':npGsmSendSmsWin1251,_A8:npGsmUnparsedRxSmsFrom,_A9:npGsmUnparsedRxSms,_AA:npGsmUnparsedRxSmsUtf8,'npGsmTraps':npGsmTraps,'npGsmTrapPrefix':npGsmTrapPrefix,'npGsmTrap':npGsmTrap,'npGsmTrapUnparsedSms':npGsmTrapUnparsedSms,'npRelay':npRelay,'npRelayTrapData':npRelayTrapData,_Q:npRelayTrapN,_R:npRelayTrapMode,_S:npRelayTrapMemo,_T:npRelayTrapState,_U:npRelayTrapCmdSrc,_V:npRelayTrapDateTime,'npRelayTable':npRelayTable,'npRelayEntry':npRelayEntry,_r:npRelayN,'npRelayMode':npRelayMode,'npRelayStartReset':npRelayStartReset,'npRelayMemo':npRelayMemo,'npRelayFlip':npRelayFlip,'npRelayState':npRelayState,'npRelayTrap':npRelayTrap,'npRelayTrapOff':npRelayTrapOff,'npRelayTrapOn':npRelayTrapOn,'npRelayTrapModeChange':npRelayTrapModeChange,'npRelayTrapReset':npRelayTrapReset,'npRelayTrapAllEvents':npRelayTrapAllEvents,'npRelayTrapAllChannels':npRelayTrapAllChannels,'npExtRelay':npExtRelay,'npExtRelayTrapData':npExtRelayTrapData,_W:npExtRelayTrapN,_X:npExtRelayTrapMode,_Y:npExtRelayTrapMemo,_Z:npExtRelayTrapState,_a:npExtRelayTrapCmdSrc,_b:npExtRelayTrapDateTime,'npExtRelayTable':npExtRelayTable,'npExtRelayEntry':npExtRelayEntry,_s:npExtRelayN,'npExtRelayMode':npExtRelayMode,'npExtRelayStartReset':npExtRelayStartReset,'npExtRelayMemo':npExtRelayMemo,'npExtRelayFlip':npExtRelayFlip,'npExtRelayState':npExtRelayState,'npExtRelayTrap':npExtRelayTrap,'npExtRelayTrapOff':npExtRelayTrapOff,'npExtRelayTrapOn':npExtRelayTrapOn,'npExtRelayTrapModeChange':npExtRelayTrapModeChange,'npExtRelayTrapReset':npExtRelayTrapReset,'npExtRelayTrapAllEvents':npExtRelayTrapAllEvents,'npExtRelayTrapAllChannels':npExtRelayTrapAllChannels,'npIr':npIr,'npIrCtrl':npIrCtrl,'npIrPlayCmd':npIrPlayCmd,'npIrReset':npIrReset,'npIrStatus':npIrStatus,'npInputAnalog':npInputAnalog,'npInputAnalogTable':npInputAnalogTable,'npInputAnalogEntry':npInputAnalogEntry,_t:npInputAnalogSensorN,'npInputAnalogStatus':npInputAnalogStatus,'npInputAnalogCurrent':npInputAnalogCurrent,'npInputAnalogVoltage':npInputAnalogVoltage,'npInputAnalogResistance':npInputAnalogResistance,'npInputAnalogMemo':npInputAnalogMemo,'npInputAnalogPower':npInputAnalogPower,'npInputAnalogReset':npInputAnalogReset,'npInputAnalogWorkRangeHigh':npInputAnalogWorkRangeHigh,'npInputAnalogSafeRangeHigh':npInputAnalogSafeRangeHigh,'npInputAnalogSafeRangeLow':npInputAnalogSafeRangeLow,'npInputAnalogWorkRangeLow':npInputAnalogWorkRangeLow,'npInputAnalogTraps':npInputAnalogTraps,'npInputAnalogTrapPrefix':npInputAnalogTrapPrefix,'npInputAnalogTrap':npInputAnalogTrap,_AB:npInputAnalogTrapSensorN,_AC:npInputAnalogTrapStatus,_AD:npInputAnalogTrapCurrent,_AE:npInputAnalogTrapVoltage,_AF:npInputAnalogTrapResistance,_AG:npInputAnalogTrapMemo,_AH:npInputAnalogTrapPower,_AI:npInputAnalogTrapWorkRangeHigh,_AJ:npInputAnalogTrapSafeRangeHigh,_AK:npInputAnalogTrapSafeRangeLow,_AL:npInputAnalogTrapWorkRangeLow,'npCurLoop':npCurLoop,'npCurLoopTable':npCurLoopTable,'npCurLoopEntry':npCurLoopEntry,_y:npCurLoopN,'npCurLoopStatus':npCurLoopStatus,'npCurLoopI':npCurLoopI,'npCurLoopV':npCurLoopV,'npCurLoopR':npCurLoopR,'npCurLoopPower':npCurLoopPower,'npCurLoopTraps':npCurLoopTraps,'npCurLoopTrapPrefix':npCurLoopTrapPrefix,'npCurLoopTrap':npCurLoopTrap,_AM:npCurLoopTrapN,_AN:npCurLoopTrapStatus,_AO:npCurLoopTrapI,_AP:npCurLoopTrapV,_AQ:npCurLoopTrapR,_AR:npCurLoopTrapPower,'npRelHumidity':npRelHumidity,'npRelHumTable':npRelHumTable,'npRelHumEntry':npRelHumEntry,_A0:npRelHumN,'npRelHumValue':npRelHumValue,'npRelHumStatus':npRelHumStatus,'npRelHumTempValue':npRelHumTempValue,'npRelHumTempStatus':npRelHumTempStatus,'npRelHumMemo':npRelHumMemo,'npRelHumSafeRangeHigh':npRelHumSafeRangeHigh,'npRelHumSafeRangeLow':npRelHumSafeRangeLow,'npRelHumTempSafeRangeHigh':npRelHumTempSafeRangeHigh,'npRelHumTempSafeRangeLow':npRelHumTempSafeRangeLow,'npRelHumTrapData':npRelHumTrapData,_J:npRelHumTrapDataN,_L:npRelHumTrapDataValue,_K:npRelHumTrapDataStatus,_M:npRelHumTrapDataMemo,_N:npRelHumTrapDataSafeRangeHigh,_O:npRelHumTrapDataSafeRangeLow,'npRelHumTrap':npRelHumTrap,'npRelHumTrapFail':npRelHumTrapFail,'npRelHumTrapBelowSafe':npRelHumTrapBelowSafe,'npRelHumTrapSafe':npRelHumTrapSafe,'npRelHumTrapAboveSafe':npRelHumTrapAboveSafe,'npRelHumTrapAllEvents':npRelHumTrapAllEvents,'npRelHumTrapAllChannels':npRelHumTrapAllChannels,'npRelHumTrapTemp':npRelHumTrapTemp,'npRelHumTrapTempFail':npRelHumTrapTempFail,'npRelHumTrapTempBelowSafe':npRelHumTrapTempBelowSafe,'npRelHumTrapTempSafe':npRelHumTrapTempSafe,'npRelHumTrapTempAboveSafe':npRelHumTrapTempAboveSafe,'npRelHumTrapTempAllEvents':npRelHumTrapTempAllEvents,'npRelHumTrapTempAllChannels':npRelHumTrapTempAllChannels,'npThermo':npThermo,'npThermoTable':npThermoTable,'npThermoEntry':npThermoEntry,_A1:npThermoSensorN,'npThermoValue':npThermoValue,'npThermoStatus':npThermoStatus,'npThermoLow':npThermoLow,'npThermoHigh':npThermoHigh,'npThermoMemo':npThermoMemo,'npThermoValuePrecise':npThermoValuePrecise,'npThermoTraps':npThermoTraps,'npThermoTrapPrefix':npThermoTrapPrefix,'npThermoTrap':npThermoTrap,_AT:npThermoTrapSensorN,_AU:npThermoTrapValue,_AV:npThermoTrapStatus,_AW:npThermoTrapLow,_AX:npThermoTrapHigh,_AY:npThermoTrapMemo,'npIo':npIo,'npIoTable':npIoTable,'npIoEntry':npIoEntry,_A2:npIoLineN,'npIoLevelIn':npIoLevelIn,'npIoLevelOut':npIoLevelOut,'npIoMemo':npIoMemo,'npIoPulseCounter':npIoPulseCounter,'npIoSinglePulseDuration':npIoSinglePulseDuration,'npIoSinglePulseStart':npIoSinglePulseStart,'npIoTraps':npIoTraps,'npIoTrapPrefix':npIoTrapPrefix,'npIoTrap':npIoTrap,_AZ:npIoTrapLineN,_Aa:npIoTrapLevelIn,_Ab:npIoTrapMemo,_Ac:npIoTrapLevelLegend,'npVoltage':npVoltage,'npVoltageTable':npVoltageTable,'npVoltageEntry':npVoltageEntry,_A3:npVoltageN,'npVoltageRMS':npVoltageRMS,'npVoltageStatus':npVoltageStatus,'npVoltageFreq':npVoltageFreq,'npVoltageFreqStatus':npVoltageFreqStatus,'npVoltageMemo':npVoltageMemo,'npVoltageSagCounter':npVoltageSagCounter,'npVoltageSagStatus':npVoltageSagStatus,'npVoltageSagSmallThreshold':npVoltageSagSmallThreshold,'npVoltageSagMediumThreshold':npVoltageSagMediumThreshold,'npVoltageSagBigThreshold':npVoltageSagBigThreshold,'npVoltageStandard':npVoltageStandard,'npVoltagePeak':npVoltagePeak,'npVoltagePeakStatus':npVoltagePeakStatus,'npVoltageTraps':npVoltageTraps,'npVoltageTrapPrefix':npVoltageTrapPrefix,'npVoltageTrap':npVoltageTrap,_Ad:npVoltageTrapN,_Ae:npVoltageTrapRMS,_Af:npVoltageTrapStatus,_Ag:npVoltageTrapFreq,_Ah:npVoltageTrapFreqStatus,_Ai:npVoltageTrapMemo,_Aj:npVoltageTrapSagCounter,_Ak:npVoltageTrapSagStatus,'npVoltageTrapPeak':npVoltageTrapPeak,_Al:npVoltageTrapPeakStatus})