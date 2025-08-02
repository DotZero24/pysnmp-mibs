_Af='cpqCmcStatusLock2Dev'
_Ae='cpqCmcStatusLock1Dev'
_Ad='cpqCmcStatusAlarm2'
_Ac='cpqCmcStatusAlarm1'
_Ab='cpqCmcStatusAux2'
_Aa='cpqCmcStatusAux1'
_AZ='cpqCmcStatusShock'
_AY='cpqCmcStatusSmoke'
_AX='cpqCmcStatusLock2Lock'
_AW='cpqCmcStatusLock1Lock'
_AV='cpqCmcStatusInput4'
_AU='cpqCmcStatusInput3'
_AT='cpqCmcStatusInput2'
_AS='cpqCmcStatusInput1'
_AR='cpqCmcStatusHumidity'
_AQ='cpqCmcStatusVoltage'
_AP='cpqCmcStatusFan2'
_AO='cpqCmcStatusFan1'
_AN='cpqCmcStatusTemp2'
_AM='cpqCmcStatusTemp1'
_AL='cpqCmcLogIndex'
_AK='notSwitched'
_AJ='clearAlarm'
_AI='enableRemoteInput'
_AH='enableKeypad'
_AG='enableBoth'
_AF='openDoorTime'
_AE='noConnect'
_AD='missingBatt'
_AC='replaceBatt'
_AB='lowBattery'
_AA='powerFail'
_A9='configError'
_A8='readyToLock'
_A7='unlockedConnFail'
_A6='unlockedNetFail'
_A5='unlockedBattLow'
_A4='unlockedPwrFail'
_A3='unlockedKey'
_A2='unlockedSmoke'
_A1='unlockedTime'
_A0='unlockedAuto'
_z='manualOn'
_y='manualOff'
_x='autoOn'
_w='autoOff'
_v='warning'
_u='cpqCmcTrapIndex'
_t='normClosed'
_s='normOpen'
_r='closeAtEPO'
_q='openAtAlarm'
_p='closeAtAlarm'
_o='NotificationType'
_n='noLock'
_m='notAvail'
_l='open'
_k='closed'
_j='underMin'
_i='overMax'
_h='normal'
_g='none'
_f='error'
_e='fan2'
_d='fan1'
_c='alarm'
_b='on'
_a='lock2'
_Z='lock1'
_Y='noFan'
_X='manual'
_W='ok'
_V='auto'
_U='noSensor'
_T='notAvailable'
_S='available'
_R='DisplayString'
_Q='sysName'
_P='sysLocation'
_O='sysDescr'
_N='sysContact'
_M='CPQCMC-MIB'
_L='relay2'
_K='relay1'
_J='enabled'
_I='off'
_H='read-only'
_G='both'
_F='disabled'
_E='SNMPv2-MIB'
_D='other'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,=mibBuilder.importSymbols('CPQHOST-MIB','compaq')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysContact,sysDescr,sysLocation,sysName=mibBuilder.importSymbols(_E,_N,_O,_P,_Q)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier',_o,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_o,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_R,'PhysAddress','TextualConvention')
_CpqCmc_ObjectIdentity=ObjectIdentity
cpqCmc=_CpqCmc_ObjectIdentity((1,3,6,1,4,1,232,153))
_CpqCmcMibRev_ObjectIdentity=ObjectIdentity
cpqCmcMibRev=_CpqCmcMibRev_ObjectIdentity((1,3,6,1,4,1,232,153,1))
class _CpqCmcMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqCmcMibRevMajor_Type.__name__=_B
_CpqCmcMibRevMajor_Object=MibScalar
cpqCmcMibRevMajor=_CpqCmcMibRevMajor_Object((1,3,6,1,4,1,232,153,1,1),_CpqCmcMibRevMajor_Type())
cpqCmcMibRevMajor.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcMibRevMajor.setStatus(_A)
class _CpqCmcMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqCmcMibRevMinor_Type.__name__=_B
_CpqCmcMibRevMinor_Object=MibScalar
cpqCmcMibRevMinor=_CpqCmcMibRevMinor_Object((1,3,6,1,4,1,232,153,1,2),_CpqCmcMibRevMinor_Type())
cpqCmcMibRevMinor.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcMibRevMinor.setStatus(_A)
class _CpqCmcMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_W,2),('degraded',3),('failed',4)))
_CpqCmcMibCondition_Type.__name__=_B
_CpqCmcMibCondition_Object=MibScalar
cpqCmcMibCondition=_CpqCmcMibCondition_Object((1,3,6,1,4,1,232,153,1,3),_CpqCmcMibCondition_Type())
cpqCmcMibCondition.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcMibCondition.setStatus(_A)
_CpqCmcComponent_ObjectIdentity=ObjectIdentity
cpqCmcComponent=_CpqCmcComponent_ObjectIdentity((1,3,6,1,4,1,232,153,2))
_CpqCmcInterface_ObjectIdentity=ObjectIdentity
cpqCmcInterface=_CpqCmcInterface_ObjectIdentity((1,3,6,1,4,1,232,153,2,1))
_CpqCmcOsCommon_ObjectIdentity=ObjectIdentity
cpqCmcOsCommon=_CpqCmcOsCommon_ObjectIdentity((1,3,6,1,4,1,232,153,2,1,1))
class _CpqCmcOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqCmcOsCommonPollFreq_Type.__name__=_B
_CpqCmcOsCommonPollFreq_Object=MibScalar
cpqCmcOsCommonPollFreq=_CpqCmcOsCommonPollFreq_Object((1,3,6,1,4,1,232,153,2,1,1,1),_CpqCmcOsCommonPollFreq_Type())
cpqCmcOsCommonPollFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcOsCommonPollFreq.setStatus(_A)
_CpqCmcDevice_ObjectIdentity=ObjectIdentity
cpqCmcDevice=_CpqCmcDevice_ObjectIdentity((1,3,6,1,4,1,232,153,2,2))
class _CpqCmcDeviceCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_W,2),('overloadDC',3),('fuseDC',4)))
_CpqCmcDeviceCondition_Type.__name__=_B
_CpqCmcDeviceCondition_Object=MibScalar
cpqCmcDeviceCondition=_CpqCmcDeviceCondition_Object((1,3,6,1,4,1,232,153,2,2,1),_CpqCmcDeviceCondition_Type())
cpqCmcDeviceCondition.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcDeviceCondition.setStatus(_A)
_CpqCmcSetup_ObjectIdentity=ObjectIdentity
cpqCmcSetup=_CpqCmcSetup_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2))
_CpqCmcSetupConfig_ObjectIdentity=ObjectIdentity
cpqCmcSetupConfig=_CpqCmcSetupConfig_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1))
_CpqCmcSetupGeneral_ObjectIdentity=ObjectIdentity
cpqCmcSetupGeneral=_CpqCmcSetupGeneral_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,1))
class _CpqCmcsetLanguage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_D,1),('english',2),('french',3),('italian',4),('german',5),('spanish',6),('dutch',7),('japanese',8)))
_CpqCmcsetLanguage_Type.__name__=_B
_CpqCmcsetLanguage_Object=MibScalar
cpqCmcsetLanguage=_CpqCmcsetLanguage_Object((1,3,6,1,4,1,232,153,2,2,2,1,1,1),_CpqCmcsetLanguage_Type())
cpqCmcsetLanguage.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcsetLanguage.setStatus(_A)
class _CpqCmcsetTempUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('celsius',2),('fahrenheit',3)))
_CpqCmcsetTempUnit_Type.__name__=_B
_CpqCmcsetTempUnit_Object=MibScalar
cpqCmcsetTempUnit=_CpqCmcsetTempUnit_Object((1,3,6,1,4,1,232,153,2,2,2,1,1,2),_CpqCmcsetTempUnit_Type())
cpqCmcsetTempUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcsetTempUnit.setStatus(_A)
class _CpqCmcsetAudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('enableSilence',2),('disableSilence',3),(_I,4)))
_CpqCmcsetAudibleAlarm_Type.__name__=_B
_CpqCmcsetAudibleAlarm_Object=MibScalar
cpqCmcsetAudibleAlarm=_CpqCmcsetAudibleAlarm_Object((1,3,6,1,4,1,232,153,2,2,2,1,1,3),_CpqCmcsetAudibleAlarm_Type())
cpqCmcsetAudibleAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcsetAudibleAlarm.setStatus(_A)
class _CpqCmcPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_CpqCmcPassword_Type.__name__=_R
_CpqCmcPassword_Object=MibScalar
cpqCmcPassword=_CpqCmcPassword_Object((1,3,6,1,4,1,232,153,2,2,2,1,1,4),_CpqCmcPassword_Type())
cpqCmcPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcPassword.setStatus(_A)
class _CpqCmcPasswordOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcPasswordOption_Type.__name__=_B
_CpqCmcPasswordOption_Object=MibScalar
cpqCmcPasswordOption=_CpqCmcPasswordOption_Object((1,3,6,1,4,1,232,153,2,2,2,1,1,5),_CpqCmcPasswordOption_Type())
cpqCmcPasswordOption.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcPasswordOption.setStatus(_A)
class _CpqCmcquitRelay1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcquitRelay1_Type.__name__=_B
_CpqCmcquitRelay1_Object=MibScalar
cpqCmcquitRelay1=_CpqCmcquitRelay1_Object((1,3,6,1,4,1,232,153,2,2,2,1,1,6),_CpqCmcquitRelay1_Type())
cpqCmcquitRelay1.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcquitRelay1.setStatus(_A)
class _CpqCmcquitRelay2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcquitRelay2_Type.__name__=_B
_CpqCmcquitRelay2_Object=MibScalar
cpqCmcquitRelay2=_CpqCmcquitRelay2_Object((1,3,6,1,4,1,232,153,2,2,2,1,1,7),_CpqCmcquitRelay2_Type())
cpqCmcquitRelay2.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcquitRelay2.setStatus(_A)
class _CpqCmclogicRelay1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_p,2),(_q,3),(_r,4)))
_CpqCmclogicRelay1_Type.__name__=_B
_CpqCmclogicRelay1_Object=MibScalar
cpqCmclogicRelay1=_CpqCmclogicRelay1_Object((1,3,6,1,4,1,232,153,2,2,2,1,1,8),_CpqCmclogicRelay1_Type())
cpqCmclogicRelay1.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmclogicRelay1.setStatus(_A)
class _CpqCmclogicRelay2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_p,2),(_q,3),(_r,4)))
_CpqCmclogicRelay2_Type.__name__=_B
_CpqCmclogicRelay2_Object=MibScalar
cpqCmclogicRelay2=_CpqCmclogicRelay2_Object((1,3,6,1,4,1,232,153,2,2,2,1,1,9),_CpqCmclogicRelay2_Type())
cpqCmclogicRelay2.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmclogicRelay2.setStatus(_A)
_CpqCmcSetupEvents_ObjectIdentity=ObjectIdentity
cpqCmcSetupEvents=_CpqCmcSetupEvents_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2))
_CpqCmcSetupTemp1_ObjectIdentity=ObjectIdentity
cpqCmcSetupTemp1=_CpqCmcSetupTemp1_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,1))
class _CpqCmcSetupTemp1Avail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupTemp1Avail_Type.__name__=_B
_CpqCmcSetupTemp1Avail_Object=MibScalar
cpqCmcSetupTemp1Avail=_CpqCmcSetupTemp1Avail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,1,1),_CpqCmcSetupTemp1Avail_Type())
cpqCmcSetupTemp1Avail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupTemp1Avail.setStatus(_A)
class _CpqCmcSetupTemp1RelaysWarn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupTemp1RelaysWarn_Type.__name__=_B
_CpqCmcSetupTemp1RelaysWarn_Object=MibScalar
cpqCmcSetupTemp1RelaysWarn=_CpqCmcSetupTemp1RelaysWarn_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,1,2),_CpqCmcSetupTemp1RelaysWarn_Type())
cpqCmcSetupTemp1RelaysWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupTemp1RelaysWarn.setStatus(_A)
class _CpqCmcSetupTemp1RelaysMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupTemp1RelaysMax_Type.__name__=_B
_CpqCmcSetupTemp1RelaysMax_Object=MibScalar
cpqCmcSetupTemp1RelaysMax=_CpqCmcSetupTemp1RelaysMax_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,1,3),_CpqCmcSetupTemp1RelaysMax_Type())
cpqCmcSetupTemp1RelaysMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupTemp1RelaysMax.setStatus(_A)
class _CpqCmcSetupTemp1RelaysMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupTemp1RelaysMin_Type.__name__=_B
_CpqCmcSetupTemp1RelaysMin_Object=MibScalar
cpqCmcSetupTemp1RelaysMin=_CpqCmcSetupTemp1RelaysMin_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,1,4),_CpqCmcSetupTemp1RelaysMin_Type())
cpqCmcSetupTemp1RelaysMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupTemp1RelaysMin.setStatus(_A)
class _CpqCmcSetupTemp1AudibleAlarmWarn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupTemp1AudibleAlarmWarn_Type.__name__=_B
_CpqCmcSetupTemp1AudibleAlarmWarn_Object=MibScalar
cpqCmcSetupTemp1AudibleAlarmWarn=_CpqCmcSetupTemp1AudibleAlarmWarn_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,1,5),_CpqCmcSetupTemp1AudibleAlarmWarn_Type())
cpqCmcSetupTemp1AudibleAlarmWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupTemp1AudibleAlarmWarn.setStatus(_A)
class _CpqCmcSetupTemp1AudibleAlarmMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupTemp1AudibleAlarmMax_Type.__name__=_B
_CpqCmcSetupTemp1AudibleAlarmMax_Object=MibScalar
cpqCmcSetupTemp1AudibleAlarmMax=_CpqCmcSetupTemp1AudibleAlarmMax_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,1,6),_CpqCmcSetupTemp1AudibleAlarmMax_Type())
cpqCmcSetupTemp1AudibleAlarmMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupTemp1AudibleAlarmMax.setStatus(_A)
class _CpqCmcSetupTemp1AudibleAlarmMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupTemp1AudibleAlarmMin_Type.__name__=_B
_CpqCmcSetupTemp1AudibleAlarmMin_Object=MibScalar
cpqCmcSetupTemp1AudibleAlarmMin=_CpqCmcSetupTemp1AudibleAlarmMin_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,1,7),_CpqCmcSetupTemp1AudibleAlarmMin_Type())
cpqCmcSetupTemp1AudibleAlarmMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupTemp1AudibleAlarmMin.setStatus(_A)
_CpqCmcSetupTemp2_ObjectIdentity=ObjectIdentity
cpqCmcSetupTemp2=_CpqCmcSetupTemp2_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,2))
class _CpqCmcSetupTemp2Avail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupTemp2Avail_Type.__name__=_B
_CpqCmcSetupTemp2Avail_Object=MibScalar
cpqCmcSetupTemp2Avail=_CpqCmcSetupTemp2Avail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,2,1),_CpqCmcSetupTemp2Avail_Type())
cpqCmcSetupTemp2Avail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupTemp2Avail.setStatus(_A)
class _CpqCmcSetupTemp2RelaysWarn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupTemp2RelaysWarn_Type.__name__=_B
_CpqCmcSetupTemp2RelaysWarn_Object=MibScalar
cpqCmcSetupTemp2RelaysWarn=_CpqCmcSetupTemp2RelaysWarn_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,2,2),_CpqCmcSetupTemp2RelaysWarn_Type())
cpqCmcSetupTemp2RelaysWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupTemp2RelaysWarn.setStatus(_A)
class _CpqCmcSetupTemp2RelaysMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupTemp2RelaysMax_Type.__name__=_B
_CpqCmcSetupTemp2RelaysMax_Object=MibScalar
cpqCmcSetupTemp2RelaysMax=_CpqCmcSetupTemp2RelaysMax_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,2,3),_CpqCmcSetupTemp2RelaysMax_Type())
cpqCmcSetupTemp2RelaysMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupTemp2RelaysMax.setStatus(_A)
class _CpqCmcSetupTemp2RelaysMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupTemp2RelaysMin_Type.__name__=_B
_CpqCmcSetupTemp2RelaysMin_Object=MibScalar
cpqCmcSetupTemp2RelaysMin=_CpqCmcSetupTemp2RelaysMin_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,2,4),_CpqCmcSetupTemp2RelaysMin_Type())
cpqCmcSetupTemp2RelaysMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupTemp2RelaysMin.setStatus(_A)
class _CpqCmcSetupTemp2AudibleAlarmWarn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupTemp2AudibleAlarmWarn_Type.__name__=_B
_CpqCmcSetupTemp2AudibleAlarmWarn_Object=MibScalar
cpqCmcSetupTemp2AudibleAlarmWarn=_CpqCmcSetupTemp2AudibleAlarmWarn_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,2,5),_CpqCmcSetupTemp2AudibleAlarmWarn_Type())
cpqCmcSetupTemp2AudibleAlarmWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupTemp2AudibleAlarmWarn.setStatus(_A)
class _CpqCmcSetupTemp2AudibleAlarmMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupTemp2AudibleAlarmMax_Type.__name__=_B
_CpqCmcSetupTemp2AudibleAlarmMax_Object=MibScalar
cpqCmcSetupTemp2AudibleAlarmMax=_CpqCmcSetupTemp2AudibleAlarmMax_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,2,6),_CpqCmcSetupTemp2AudibleAlarmMax_Type())
cpqCmcSetupTemp2AudibleAlarmMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupTemp2AudibleAlarmMax.setStatus(_A)
class _CpqCmcSetupTemp2AudibleAlarmMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupTemp2AudibleAlarmMin_Type.__name__=_B
_CpqCmcSetupTemp2AudibleAlarmMin_Object=MibScalar
cpqCmcSetupTemp2AudibleAlarmMin=_CpqCmcSetupTemp2AudibleAlarmMin_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,2,7),_CpqCmcSetupTemp2AudibleAlarmMin_Type())
cpqCmcSetupTemp2AudibleAlarmMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupTemp2AudibleAlarmMin.setStatus(_A)
_CpqCmcSetupFan1_ObjectIdentity=ObjectIdentity
cpqCmcSetupFan1=_CpqCmcSetupFan1_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,3))
class _CpqCmcSetupFan1Avail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupFan1Avail_Type.__name__=_B
_CpqCmcSetupFan1Avail_Object=MibScalar
cpqCmcSetupFan1Avail=_CpqCmcSetupFan1Avail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,3,1),_CpqCmcSetupFan1Avail_Type())
cpqCmcSetupFan1Avail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupFan1Avail.setStatus(_A)
class _CpqCmcSetupFan1Relays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupFan1Relays_Type.__name__=_B
_CpqCmcSetupFan1Relays_Object=MibScalar
cpqCmcSetupFan1Relays=_CpqCmcSetupFan1Relays_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,3,2),_CpqCmcSetupFan1Relays_Type())
cpqCmcSetupFan1Relays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupFan1Relays.setStatus(_A)
class _CpqCmcSetupFan1AudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupFan1AudibleAlarm_Type.__name__=_B
_CpqCmcSetupFan1AudibleAlarm_Object=MibScalar
cpqCmcSetupFan1AudibleAlarm=_CpqCmcSetupFan1AudibleAlarm_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,3,3),_CpqCmcSetupFan1AudibleAlarm_Type())
cpqCmcSetupFan1AudibleAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupFan1AudibleAlarm.setStatus(_A)
_CpqCmcSetupFan2_ObjectIdentity=ObjectIdentity
cpqCmcSetupFan2=_CpqCmcSetupFan2_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,4))
class _CpqCmcSetupFan2Avail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupFan2Avail_Type.__name__=_B
_CpqCmcSetupFan2Avail_Object=MibScalar
cpqCmcSetupFan2Avail=_CpqCmcSetupFan2Avail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,4,1),_CpqCmcSetupFan2Avail_Type())
cpqCmcSetupFan2Avail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupFan2Avail.setStatus(_A)
class _CpqCmcSetupFan2Relays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupFan2Relays_Type.__name__=_B
_CpqCmcSetupFan2Relays_Object=MibScalar
cpqCmcSetupFan2Relays=_CpqCmcSetupFan2Relays_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,4,2),_CpqCmcSetupFan2Relays_Type())
cpqCmcSetupFan2Relays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupFan2Relays.setStatus(_A)
class _CpqCmcSetupFan2AudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupFan2AudibleAlarm_Type.__name__=_B
_CpqCmcSetupFan2AudibleAlarm_Object=MibScalar
cpqCmcSetupFan2AudibleAlarm=_CpqCmcSetupFan2AudibleAlarm_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,4,3),_CpqCmcSetupFan2AudibleAlarm_Type())
cpqCmcSetupFan2AudibleAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupFan2AudibleAlarm.setStatus(_A)
_CpqCmcSetupVoltage_ObjectIdentity=ObjectIdentity
cpqCmcSetupVoltage=_CpqCmcSetupVoltage_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,5))
class _CpqCmcSetupVoltageAvail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupVoltageAvail_Type.__name__=_B
_CpqCmcSetupVoltageAvail_Object=MibScalar
cpqCmcSetupVoltageAvail=_CpqCmcSetupVoltageAvail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,5,1),_CpqCmcSetupVoltageAvail_Type())
cpqCmcSetupVoltageAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupVoltageAvail.setStatus(_A)
class _CpqCmcSetupVoltageRelaysMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupVoltageRelaysMax_Type.__name__=_B
_CpqCmcSetupVoltageRelaysMax_Object=MibScalar
cpqCmcSetupVoltageRelaysMax=_CpqCmcSetupVoltageRelaysMax_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,5,2),_CpqCmcSetupVoltageRelaysMax_Type())
cpqCmcSetupVoltageRelaysMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupVoltageRelaysMax.setStatus(_A)
class _CpqCmcSetupVoltageRelaysMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupVoltageRelaysMin_Type.__name__=_B
_CpqCmcSetupVoltageRelaysMin_Object=MibScalar
cpqCmcSetupVoltageRelaysMin=_CpqCmcSetupVoltageRelaysMin_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,5,3),_CpqCmcSetupVoltageRelaysMin_Type())
cpqCmcSetupVoltageRelaysMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupVoltageRelaysMin.setStatus(_A)
class _CpqCmcSetupVoltageAudibleAlarmMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupVoltageAudibleAlarmMax_Type.__name__=_B
_CpqCmcSetupVoltageAudibleAlarmMax_Object=MibScalar
cpqCmcSetupVoltageAudibleAlarmMax=_CpqCmcSetupVoltageAudibleAlarmMax_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,5,4),_CpqCmcSetupVoltageAudibleAlarmMax_Type())
cpqCmcSetupVoltageAudibleAlarmMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupVoltageAudibleAlarmMax.setStatus(_A)
class _CpqCmcSetupVoltageAudibleAlarmMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupVoltageAudibleAlarmMin_Type.__name__=_B
_CpqCmcSetupVoltageAudibleAlarmMin_Object=MibScalar
cpqCmcSetupVoltageAudibleAlarmMin=_CpqCmcSetupVoltageAudibleAlarmMin_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,5,5),_CpqCmcSetupVoltageAudibleAlarmMin_Type())
cpqCmcSetupVoltageAudibleAlarmMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupVoltageAudibleAlarmMin.setStatus(_A)
_CpqCmcSetupHumidity_ObjectIdentity=ObjectIdentity
cpqCmcSetupHumidity=_CpqCmcSetupHumidity_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,6))
class _CpqCmcSetupHumidityAvail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupHumidityAvail_Type.__name__=_B
_CpqCmcSetupHumidityAvail_Object=MibScalar
cpqCmcSetupHumidityAvail=_CpqCmcSetupHumidityAvail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,6,1),_CpqCmcSetupHumidityAvail_Type())
cpqCmcSetupHumidityAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupHumidityAvail.setStatus(_A)
class _CpqCmcSetupHumidityRelaysMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupHumidityRelaysMax_Type.__name__=_B
_CpqCmcSetupHumidityRelaysMax_Object=MibScalar
cpqCmcSetupHumidityRelaysMax=_CpqCmcSetupHumidityRelaysMax_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,6,2),_CpqCmcSetupHumidityRelaysMax_Type())
cpqCmcSetupHumidityRelaysMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupHumidityRelaysMax.setStatus(_A)
class _CpqCmcSetupHumidityRelaysMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupHumidityRelaysMin_Type.__name__=_B
_CpqCmcSetupHumidityRelaysMin_Object=MibScalar
cpqCmcSetupHumidityRelaysMin=_CpqCmcSetupHumidityRelaysMin_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,6,3),_CpqCmcSetupHumidityRelaysMin_Type())
cpqCmcSetupHumidityRelaysMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupHumidityRelaysMin.setStatus(_A)
class _CpqCmcSetupHumidityAudibleAlarmMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupHumidityAudibleAlarmMax_Type.__name__=_B
_CpqCmcSetupHumidityAudibleAlarmMax_Object=MibScalar
cpqCmcSetupHumidityAudibleAlarmMax=_CpqCmcSetupHumidityAudibleAlarmMax_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,6,4),_CpqCmcSetupHumidityAudibleAlarmMax_Type())
cpqCmcSetupHumidityAudibleAlarmMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupHumidityAudibleAlarmMax.setStatus(_A)
class _CpqCmcSetupHumidityAudibleAlarmMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupHumidityAudibleAlarmMin_Type.__name__=_B
_CpqCmcSetupHumidityAudibleAlarmMin_Object=MibScalar
cpqCmcSetupHumidityAudibleAlarmMin=_CpqCmcSetupHumidityAudibleAlarmMin_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,6,5),_CpqCmcSetupHumidityAudibleAlarmMin_Type())
cpqCmcSetupHumidityAudibleAlarmMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupHumidityAudibleAlarmMin.setStatus(_A)
_CpqCmcSetupInput1_ObjectIdentity=ObjectIdentity
cpqCmcSetupInput1=_CpqCmcSetupInput1_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,7))
class _CpqCmcSetupInput1Avail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupInput1Avail_Type.__name__=_B
_CpqCmcSetupInput1Avail_Object=MibScalar
cpqCmcSetupInput1Avail=_CpqCmcSetupInput1Avail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,7,1),_CpqCmcSetupInput1Avail_Type())
cpqCmcSetupInput1Avail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput1Avail.setStatus(_A)
class _CpqCmcSetupInput1Relays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupInput1Relays_Type.__name__=_B
_CpqCmcSetupInput1Relays_Object=MibScalar
cpqCmcSetupInput1Relays=_CpqCmcSetupInput1Relays_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,7,2),_CpqCmcSetupInput1Relays_Type())
cpqCmcSetupInput1Relays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput1Relays.setStatus(_A)
class _CpqCmcSetupInput1AudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupInput1AudibleAlarm_Type.__name__=_B
_CpqCmcSetupInput1AudibleAlarm_Object=MibScalar
cpqCmcSetupInput1AudibleAlarm=_CpqCmcSetupInput1AudibleAlarm_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,7,3),_CpqCmcSetupInput1AudibleAlarm_Type())
cpqCmcSetupInput1AudibleAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput1AudibleAlarm.setStatus(_A)
class _CpqCmcSetupInput1FansOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_G,2),(_d,3),(_e,4),(_Y,5)))
_CpqCmcSetupInput1FansOff_Type.__name__=_B
_CpqCmcSetupInput1FansOff_Object=MibScalar
cpqCmcSetupInput1FansOff=_CpqCmcSetupInput1FansOff_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,7,4),_CpqCmcSetupInput1FansOff_Type())
cpqCmcSetupInput1FansOff.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput1FansOff.setStatus(_A)
class _CpqCmcSetupInput1ShockSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_I,2),(_b,3)))
_CpqCmcSetupInput1ShockSensor_Type.__name__=_B
_CpqCmcSetupInput1ShockSensor_Object=MibScalar
cpqCmcSetupInput1ShockSensor=_CpqCmcSetupInput1ShockSensor_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,7,5),_CpqCmcSetupInput1ShockSensor_Type())
cpqCmcSetupInput1ShockSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput1ShockSensor.setStatus(_A)
class _CpqCmcSetupInput1Description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_CpqCmcSetupInput1Description_Type.__name__=_R
_CpqCmcSetupInput1Description_Object=MibScalar
cpqCmcSetupInput1Description=_CpqCmcSetupInput1Description_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,7,6),_CpqCmcSetupInput1Description_Type())
cpqCmcSetupInput1Description.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput1Description.setStatus(_A)
class _CpqCmcSetupInput1Lock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_g,2),(_Z,3),(_a,4),(_G,5)))
_CpqCmcSetupInput1Lock_Type.__name__=_B
_CpqCmcSetupInput1Lock_Object=MibScalar
cpqCmcSetupInput1Lock=_CpqCmcSetupInput1Lock_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,7,7),_CpqCmcSetupInput1Lock_Type())
cpqCmcSetupInput1Lock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput1Lock.setStatus(_A)
_CpqCmcSetupInput2_ObjectIdentity=ObjectIdentity
cpqCmcSetupInput2=_CpqCmcSetupInput2_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,8))
class _CpqCmcSetupInput2Avail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupInput2Avail_Type.__name__=_B
_CpqCmcSetupInput2Avail_Object=MibScalar
cpqCmcSetupInput2Avail=_CpqCmcSetupInput2Avail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,8,1),_CpqCmcSetupInput2Avail_Type())
cpqCmcSetupInput2Avail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput2Avail.setStatus(_A)
class _CpqCmcSetupInput2Relays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupInput2Relays_Type.__name__=_B
_CpqCmcSetupInput2Relays_Object=MibScalar
cpqCmcSetupInput2Relays=_CpqCmcSetupInput2Relays_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,8,2),_CpqCmcSetupInput2Relays_Type())
cpqCmcSetupInput2Relays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput2Relays.setStatus(_A)
class _CpqCmcSetupInput2AudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupInput2AudibleAlarm_Type.__name__=_B
_CpqCmcSetupInput2AudibleAlarm_Object=MibScalar
cpqCmcSetupInput2AudibleAlarm=_CpqCmcSetupInput2AudibleAlarm_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,8,3),_CpqCmcSetupInput2AudibleAlarm_Type())
cpqCmcSetupInput2AudibleAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput2AudibleAlarm.setStatus(_A)
class _CpqCmcSetupInput2FansOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_G,2),(_d,3),(_e,4),(_Y,5)))
_CpqCmcSetupInput2FansOff_Type.__name__=_B
_CpqCmcSetupInput2FansOff_Object=MibScalar
cpqCmcSetupInput2FansOff=_CpqCmcSetupInput2FansOff_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,8,4),_CpqCmcSetupInput2FansOff_Type())
cpqCmcSetupInput2FansOff.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput2FansOff.setStatus(_A)
class _CpqCmcSetupInput2ShockSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_I,2),(_b,3)))
_CpqCmcSetupInput2ShockSensor_Type.__name__=_B
_CpqCmcSetupInput2ShockSensor_Object=MibScalar
cpqCmcSetupInput2ShockSensor=_CpqCmcSetupInput2ShockSensor_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,8,5),_CpqCmcSetupInput2ShockSensor_Type())
cpqCmcSetupInput2ShockSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput2ShockSensor.setStatus(_A)
class _CpqCmcSetupInput2Description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_CpqCmcSetupInput2Description_Type.__name__=_R
_CpqCmcSetupInput2Description_Object=MibScalar
cpqCmcSetupInput2Description=_CpqCmcSetupInput2Description_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,8,6),_CpqCmcSetupInput2Description_Type())
cpqCmcSetupInput2Description.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput2Description.setStatus(_A)
class _CpqCmcSetupInput2Lock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_g,2),(_Z,3),(_a,4),(_G,5)))
_CpqCmcSetupInput2Lock_Type.__name__=_B
_CpqCmcSetupInput2Lock_Object=MibScalar
cpqCmcSetupInput2Lock=_CpqCmcSetupInput2Lock_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,8,7),_CpqCmcSetupInput2Lock_Type())
cpqCmcSetupInput2Lock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput2Lock.setStatus(_A)
_CpqCmcSetupInput3_ObjectIdentity=ObjectIdentity
cpqCmcSetupInput3=_CpqCmcSetupInput3_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,9))
class _CpqCmcSetupInput3Avail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupInput3Avail_Type.__name__=_B
_CpqCmcSetupInput3Avail_Object=MibScalar
cpqCmcSetupInput3Avail=_CpqCmcSetupInput3Avail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,9,1),_CpqCmcSetupInput3Avail_Type())
cpqCmcSetupInput3Avail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput3Avail.setStatus(_A)
class _CpqCmcSetupInput3Relays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupInput3Relays_Type.__name__=_B
_CpqCmcSetupInput3Relays_Object=MibScalar
cpqCmcSetupInput3Relays=_CpqCmcSetupInput3Relays_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,9,2),_CpqCmcSetupInput3Relays_Type())
cpqCmcSetupInput3Relays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput3Relays.setStatus(_A)
class _CpqCmcSetupInput3AudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupInput3AudibleAlarm_Type.__name__=_B
_CpqCmcSetupInput3AudibleAlarm_Object=MibScalar
cpqCmcSetupInput3AudibleAlarm=_CpqCmcSetupInput3AudibleAlarm_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,9,3),_CpqCmcSetupInput3AudibleAlarm_Type())
cpqCmcSetupInput3AudibleAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput3AudibleAlarm.setStatus(_A)
class _CpqCmcSetupInput3FansOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_G,2),(_d,3),(_e,4),(_Y,5)))
_CpqCmcSetupInput3FansOff_Type.__name__=_B
_CpqCmcSetupInput3FansOff_Object=MibScalar
cpqCmcSetupInput3FansOff=_CpqCmcSetupInput3FansOff_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,9,4),_CpqCmcSetupInput3FansOff_Type())
cpqCmcSetupInput3FansOff.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput3FansOff.setStatus(_A)
class _CpqCmcSetupInput3ShockSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_I,2),(_b,3)))
_CpqCmcSetupInput3ShockSensor_Type.__name__=_B
_CpqCmcSetupInput3ShockSensor_Object=MibScalar
cpqCmcSetupInput3ShockSensor=_CpqCmcSetupInput3ShockSensor_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,9,5),_CpqCmcSetupInput3ShockSensor_Type())
cpqCmcSetupInput3ShockSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput3ShockSensor.setStatus(_A)
class _CpqCmcSetupInput3Description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_CpqCmcSetupInput3Description_Type.__name__=_R
_CpqCmcSetupInput3Description_Object=MibScalar
cpqCmcSetupInput3Description=_CpqCmcSetupInput3Description_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,9,6),_CpqCmcSetupInput3Description_Type())
cpqCmcSetupInput3Description.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput3Description.setStatus(_A)
class _CpqCmcSetupInput3Lock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_g,2),(_Z,3),(_a,4),(_G,5)))
_CpqCmcSetupInput3Lock_Type.__name__=_B
_CpqCmcSetupInput3Lock_Object=MibScalar
cpqCmcSetupInput3Lock=_CpqCmcSetupInput3Lock_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,9,7),_CpqCmcSetupInput3Lock_Type())
cpqCmcSetupInput3Lock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput3Lock.setStatus(_A)
_CpqCmcSetupInput4_ObjectIdentity=ObjectIdentity
cpqCmcSetupInput4=_CpqCmcSetupInput4_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,10))
class _CpqCmcSetupInput4Avail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupInput4Avail_Type.__name__=_B
_CpqCmcSetupInput4Avail_Object=MibScalar
cpqCmcSetupInput4Avail=_CpqCmcSetupInput4Avail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,10,1),_CpqCmcSetupInput4Avail_Type())
cpqCmcSetupInput4Avail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput4Avail.setStatus(_A)
class _CpqCmcSetupInput4Relays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupInput4Relays_Type.__name__=_B
_CpqCmcSetupInput4Relays_Object=MibScalar
cpqCmcSetupInput4Relays=_CpqCmcSetupInput4Relays_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,10,2),_CpqCmcSetupInput4Relays_Type())
cpqCmcSetupInput4Relays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput4Relays.setStatus(_A)
class _CpqCmcSetupInput4AudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupInput4AudibleAlarm_Type.__name__=_B
_CpqCmcSetupInput4AudibleAlarm_Object=MibScalar
cpqCmcSetupInput4AudibleAlarm=_CpqCmcSetupInput4AudibleAlarm_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,10,3),_CpqCmcSetupInput4AudibleAlarm_Type())
cpqCmcSetupInput4AudibleAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput4AudibleAlarm.setStatus(_A)
class _CpqCmcSetupInput4FansOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_G,2),(_d,3),(_e,4),(_Y,5)))
_CpqCmcSetupInput4FansOff_Type.__name__=_B
_CpqCmcSetupInput4FansOff_Object=MibScalar
cpqCmcSetupInput4FansOff=_CpqCmcSetupInput4FansOff_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,10,4),_CpqCmcSetupInput4FansOff_Type())
cpqCmcSetupInput4FansOff.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput4FansOff.setStatus(_A)
class _CpqCmcSetupInput4ShockSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_I,2),(_b,3)))
_CpqCmcSetupInput4ShockSensor_Type.__name__=_B
_CpqCmcSetupInput4ShockSensor_Object=MibScalar
cpqCmcSetupInput4ShockSensor=_CpqCmcSetupInput4ShockSensor_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,10,5),_CpqCmcSetupInput4ShockSensor_Type())
cpqCmcSetupInput4ShockSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput4ShockSensor.setStatus(_A)
class _CpqCmcSetupInput4Description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_CpqCmcSetupInput4Description_Type.__name__=_R
_CpqCmcSetupInput4Description_Object=MibScalar
cpqCmcSetupInput4Description=_CpqCmcSetupInput4Description_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,10,6),_CpqCmcSetupInput4Description_Type())
cpqCmcSetupInput4Description.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput4Description.setStatus(_A)
class _CpqCmcSetupInput4Lock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_g,2),(_Z,3),(_a,4),(_G,5)))
_CpqCmcSetupInput4Lock_Type.__name__=_B
_CpqCmcSetupInput4Lock_Object=MibScalar
cpqCmcSetupInput4Lock=_CpqCmcSetupInput4Lock_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,10,7),_CpqCmcSetupInput4Lock_Type())
cpqCmcSetupInput4Lock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupInput4Lock.setStatus(_A)
_CpqCmcSetupLock1_ObjectIdentity=ObjectIdentity
cpqCmcSetupLock1=_CpqCmcSetupLock1_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,11))
class _CpqCmcSetupLock1Avail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupLock1Avail_Type.__name__=_B
_CpqCmcSetupLock1Avail_Object=MibScalar
cpqCmcSetupLock1Avail=_CpqCmcSetupLock1Avail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,11,1),_CpqCmcSetupLock1Avail_Type())
cpqCmcSetupLock1Avail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock1Avail.setStatus(_A)
class _CpqCmcSetupLock1Relays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupLock1Relays_Type.__name__=_B
_CpqCmcSetupLock1Relays_Object=MibScalar
cpqCmcSetupLock1Relays=_CpqCmcSetupLock1Relays_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,11,2),_CpqCmcSetupLock1Relays_Type())
cpqCmcSetupLock1Relays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock1Relays.setStatus(_A)
class _CpqCmcSetupLock1RelaysDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupLock1RelaysDevice_Type.__name__=_B
_CpqCmcSetupLock1RelaysDevice_Object=MibScalar
cpqCmcSetupLock1RelaysDevice=_CpqCmcSetupLock1RelaysDevice_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,11,3),_CpqCmcSetupLock1RelaysDevice_Type())
cpqCmcSetupLock1RelaysDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock1RelaysDevice.setStatus(_A)
class _CpqCmcSetupLock1AudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupLock1AudibleAlarm_Type.__name__=_B
_CpqCmcSetupLock1AudibleAlarm_Object=MibScalar
cpqCmcSetupLock1AudibleAlarm=_CpqCmcSetupLock1AudibleAlarm_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,11,4),_CpqCmcSetupLock1AudibleAlarm_Type())
cpqCmcSetupLock1AudibleAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock1AudibleAlarm.setStatus(_A)
class _CpqCmcSetupLock1AudibleAlarmDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupLock1AudibleAlarmDevice_Type.__name__=_B
_CpqCmcSetupLock1AudibleAlarmDevice_Object=MibScalar
cpqCmcSetupLock1AudibleAlarmDevice=_CpqCmcSetupLock1AudibleAlarmDevice_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,11,5),_CpqCmcSetupLock1AudibleAlarmDevice_Type())
cpqCmcSetupLock1AudibleAlarmDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock1AudibleAlarmDevice.setStatus(_A)
class _CpqCmcSetupLock1Time_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,600))
_CpqCmcSetupLock1Time_Type.__name__=_B
_CpqCmcSetupLock1Time_Object=MibScalar
cpqCmcSetupLock1Time=_CpqCmcSetupLock1Time_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,11,6),_CpqCmcSetupLock1Time_Type())
cpqCmcSetupLock1Time.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock1Time.setStatus(_A)
class _CpqCmcSetupLock1PwrFailUnlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_F,2),(_V,3),(_X,4)))
_CpqCmcSetupLock1PwrFailUnlock_Type.__name__=_B
_CpqCmcSetupLock1PwrFailUnlock_Object=MibScalar
cpqCmcSetupLock1PwrFailUnlock=_CpqCmcSetupLock1PwrFailUnlock_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,11,7),_CpqCmcSetupLock1PwrFailUnlock_Type())
cpqCmcSetupLock1PwrFailUnlock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock1PwrFailUnlock.setStatus(_A)
class _CpqCmcSetupLock1BattLowUnlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_F,2),(_V,3),(_X,4)))
_CpqCmcSetupLock1BattLowUnlock_Type.__name__=_B
_CpqCmcSetupLock1BattLowUnlock_Object=MibScalar
cpqCmcSetupLock1BattLowUnlock=_CpqCmcSetupLock1BattLowUnlock_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,11,8),_CpqCmcSetupLock1BattLowUnlock_Type())
cpqCmcSetupLock1BattLowUnlock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock1BattLowUnlock.setStatus(_A)
class _CpqCmcSetupLock1NetFailUnlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_F,2),(_V,3),(_X,4)))
_CpqCmcSetupLock1NetFailUnlock_Type.__name__=_B
_CpqCmcSetupLock1NetFailUnlock_Object=MibScalar
cpqCmcSetupLock1NetFailUnlock=_CpqCmcSetupLock1NetFailUnlock_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,11,9),_CpqCmcSetupLock1NetFailUnlock_Type())
cpqCmcSetupLock1NetFailUnlock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock1NetFailUnlock.setStatus(_A)
class _CpqCmcSetupLock1LifeFailUnlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_F,2),(_V,3),(_X,4)))
_CpqCmcSetupLock1LifeFailUnlock_Type.__name__=_B
_CpqCmcSetupLock1LifeFailUnlock_Object=MibScalar
cpqCmcSetupLock1LifeFailUnlock=_CpqCmcSetupLock1LifeFailUnlock_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,11,10),_CpqCmcSetupLock1LifeFailUnlock_Type())
cpqCmcSetupLock1LifeFailUnlock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock1LifeFailUnlock.setStatus(_A)
_CpqCmcSetupLock2_ObjectIdentity=ObjectIdentity
cpqCmcSetupLock2=_CpqCmcSetupLock2_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,12))
class _CpqCmcSetupLock2Avail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupLock2Avail_Type.__name__=_B
_CpqCmcSetupLock2Avail_Object=MibScalar
cpqCmcSetupLock2Avail=_CpqCmcSetupLock2Avail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,12,1),_CpqCmcSetupLock2Avail_Type())
cpqCmcSetupLock2Avail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock2Avail.setStatus(_A)
class _CpqCmcSetupLock2Relays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupLock2Relays_Type.__name__=_B
_CpqCmcSetupLock2Relays_Object=MibScalar
cpqCmcSetupLock2Relays=_CpqCmcSetupLock2Relays_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,12,2),_CpqCmcSetupLock2Relays_Type())
cpqCmcSetupLock2Relays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock2Relays.setStatus(_A)
class _CpqCmcSetupLock2RelaysDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupLock2RelaysDevice_Type.__name__=_B
_CpqCmcSetupLock2RelaysDevice_Object=MibScalar
cpqCmcSetupLock2RelaysDevice=_CpqCmcSetupLock2RelaysDevice_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,12,3),_CpqCmcSetupLock2RelaysDevice_Type())
cpqCmcSetupLock2RelaysDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock2RelaysDevice.setStatus(_A)
class _CpqCmcSetupLock2AudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupLock2AudibleAlarm_Type.__name__=_B
_CpqCmcSetupLock2AudibleAlarm_Object=MibScalar
cpqCmcSetupLock2AudibleAlarm=_CpqCmcSetupLock2AudibleAlarm_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,12,4),_CpqCmcSetupLock2AudibleAlarm_Type())
cpqCmcSetupLock2AudibleAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock2AudibleAlarm.setStatus(_A)
class _CpqCmcSetupLock2AudibleAlarmDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupLock2AudibleAlarmDevice_Type.__name__=_B
_CpqCmcSetupLock2AudibleAlarmDevice_Object=MibScalar
cpqCmcSetupLock2AudibleAlarmDevice=_CpqCmcSetupLock2AudibleAlarmDevice_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,12,5),_CpqCmcSetupLock2AudibleAlarmDevice_Type())
cpqCmcSetupLock2AudibleAlarmDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock2AudibleAlarmDevice.setStatus(_A)
class _CpqCmcSetupLock2Time_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,600))
_CpqCmcSetupLock2Time_Type.__name__=_B
_CpqCmcSetupLock2Time_Object=MibScalar
cpqCmcSetupLock2Time=_CpqCmcSetupLock2Time_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,12,6),_CpqCmcSetupLock2Time_Type())
cpqCmcSetupLock2Time.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock2Time.setStatus(_A)
class _CpqCmcSetupLock2PwrFailUnlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_F,2),(_V,3),(_X,4)))
_CpqCmcSetupLock2PwrFailUnlock_Type.__name__=_B
_CpqCmcSetupLock2PwrFailUnlock_Object=MibScalar
cpqCmcSetupLock2PwrFailUnlock=_CpqCmcSetupLock2PwrFailUnlock_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,12,7),_CpqCmcSetupLock2PwrFailUnlock_Type())
cpqCmcSetupLock2PwrFailUnlock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock2PwrFailUnlock.setStatus(_A)
class _CpqCmcSetupLock2BattLowUnlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_F,2),(_V,3),(_X,4)))
_CpqCmcSetupLock2BattLowUnlock_Type.__name__=_B
_CpqCmcSetupLock2BattLowUnlock_Object=MibScalar
cpqCmcSetupLock2BattLowUnlock=_CpqCmcSetupLock2BattLowUnlock_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,12,8),_CpqCmcSetupLock2BattLowUnlock_Type())
cpqCmcSetupLock2BattLowUnlock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock2BattLowUnlock.setStatus(_A)
class _CpqCmcSetupLock2NetFailUnlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_F,2),(_V,3),(_X,4)))
_CpqCmcSetupLock2NetFailUnlock_Type.__name__=_B
_CpqCmcSetupLock2NetFailUnlock_Object=MibScalar
cpqCmcSetupLock2NetFailUnlock=_CpqCmcSetupLock2NetFailUnlock_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,12,9),_CpqCmcSetupLock2NetFailUnlock_Type())
cpqCmcSetupLock2NetFailUnlock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock2NetFailUnlock.setStatus(_A)
class _CpqCmcSetupLock2LifeFailUnlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_F,2),(_V,3),(_X,4)))
_CpqCmcSetupLock2LifeFailUnlock_Type.__name__=_B
_CpqCmcSetupLock2LifeFailUnlock_Object=MibScalar
cpqCmcSetupLock2LifeFailUnlock=_CpqCmcSetupLock2LifeFailUnlock_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,12,10),_CpqCmcSetupLock2LifeFailUnlock_Type())
cpqCmcSetupLock2LifeFailUnlock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupLock2LifeFailUnlock.setStatus(_A)
_CpqCmcSetupSmoke_ObjectIdentity=ObjectIdentity
cpqCmcSetupSmoke=_CpqCmcSetupSmoke_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,13))
class _CpqCmcSetupSmokeAvail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupSmokeAvail_Type.__name__=_B
_CpqCmcSetupSmokeAvail_Object=MibScalar
cpqCmcSetupSmokeAvail=_CpqCmcSetupSmokeAvail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,13,1),_CpqCmcSetupSmokeAvail_Type())
cpqCmcSetupSmokeAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupSmokeAvail.setStatus(_A)
class _CpqCmcSetupSmokeRelays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupSmokeRelays_Type.__name__=_B
_CpqCmcSetupSmokeRelays_Object=MibScalar
cpqCmcSetupSmokeRelays=_CpqCmcSetupSmokeRelays_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,13,2),_CpqCmcSetupSmokeRelays_Type())
cpqCmcSetupSmokeRelays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupSmokeRelays.setStatus(_A)
class _CpqCmcSetupSmokeAudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupSmokeAudibleAlarm_Type.__name__=_B
_CpqCmcSetupSmokeAudibleAlarm_Object=MibScalar
cpqCmcSetupSmokeAudibleAlarm=_CpqCmcSetupSmokeAudibleAlarm_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,13,3),_CpqCmcSetupSmokeAudibleAlarm_Type())
cpqCmcSetupSmokeAudibleAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupSmokeAudibleAlarm.setStatus(_A)
class _CpqCmcSetupSmokeFansOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_G,2),(_d,3),(_e,4),(_Y,5)))
_CpqCmcSetupSmokeFansOff_Type.__name__=_B
_CpqCmcSetupSmokeFansOff_Object=MibScalar
cpqCmcSetupSmokeFansOff=_CpqCmcSetupSmokeFansOff_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,13,4),_CpqCmcSetupSmokeFansOff_Type())
cpqCmcSetupSmokeFansOff.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupSmokeFansOff.setStatus(_A)
class _CpqCmcSetupSmokeUnlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_G,2),(_Z,3),(_a,4),(_n,5)))
_CpqCmcSetupSmokeUnlock_Type.__name__=_B
_CpqCmcSetupSmokeUnlock_Object=MibScalar
cpqCmcSetupSmokeUnlock=_CpqCmcSetupSmokeUnlock_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,13,5),_CpqCmcSetupSmokeUnlock_Type())
cpqCmcSetupSmokeUnlock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupSmokeUnlock.setStatus(_A)
_CpqCmcSetupShock_ObjectIdentity=ObjectIdentity
cpqCmcSetupShock=_CpqCmcSetupShock_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,14))
class _CpqCmcSetupShockAvail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupShockAvail_Type.__name__=_B
_CpqCmcSetupShockAvail_Object=MibScalar
cpqCmcSetupShockAvail=_CpqCmcSetupShockAvail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,14,1),_CpqCmcSetupShockAvail_Type())
cpqCmcSetupShockAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupShockAvail.setStatus(_A)
class _CpqCmcSetupShockRelays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupShockRelays_Type.__name__=_B
_CpqCmcSetupShockRelays_Object=MibScalar
cpqCmcSetupShockRelays=_CpqCmcSetupShockRelays_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,14,2),_CpqCmcSetupShockRelays_Type())
cpqCmcSetupShockRelays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupShockRelays.setStatus(_A)
class _CpqCmcSetupShockAudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupShockAudibleAlarm_Type.__name__=_B
_CpqCmcSetupShockAudibleAlarm_Object=MibScalar
cpqCmcSetupShockAudibleAlarm=_CpqCmcSetupShockAudibleAlarm_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,14,3),_CpqCmcSetupShockAudibleAlarm_Type())
cpqCmcSetupShockAudibleAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupShockAudibleAlarm.setStatus(_A)
class _CpqCmcSetupShockSensitivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CpqCmcSetupShockSensitivity_Type.__name__=_B
_CpqCmcSetupShockSensitivity_Object=MibScalar
cpqCmcSetupShockSensitivity=_CpqCmcSetupShockSensitivity_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,14,4),_CpqCmcSetupShockSensitivity_Type())
cpqCmcSetupShockSensitivity.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupShockSensitivity.setStatus(_A)
_CpqCmcSetupAux1_ObjectIdentity=ObjectIdentity
cpqCmcSetupAux1=_CpqCmcSetupAux1_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,15))
class _CpqCmcSetupAux1Avail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupAux1Avail_Type.__name__=_B
_CpqCmcSetupAux1Avail_Object=MibScalar
cpqCmcSetupAux1Avail=_CpqCmcSetupAux1Avail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,15,1),_CpqCmcSetupAux1Avail_Type())
cpqCmcSetupAux1Avail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAux1Avail.setStatus(_A)
class _CpqCmcSetupAux1Relays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupAux1Relays_Type.__name__=_B
_CpqCmcSetupAux1Relays_Object=MibScalar
cpqCmcSetupAux1Relays=_CpqCmcSetupAux1Relays_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,15,2),_CpqCmcSetupAux1Relays_Type())
cpqCmcSetupAux1Relays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAux1Relays.setStatus(_A)
class _CpqCmcSetupAux1AudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupAux1AudibleAlarm_Type.__name__=_B
_CpqCmcSetupAux1AudibleAlarm_Object=MibScalar
cpqCmcSetupAux1AudibleAlarm=_CpqCmcSetupAux1AudibleAlarm_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,15,3),_CpqCmcSetupAux1AudibleAlarm_Type())
cpqCmcSetupAux1AudibleAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAux1AudibleAlarm.setStatus(_A)
class _CpqCmcSetupAux1InputType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_s,2),(_t,3)))
_CpqCmcSetupAux1InputType_Type.__name__=_B
_CpqCmcSetupAux1InputType_Object=MibScalar
cpqCmcSetupAux1InputType=_CpqCmcSetupAux1InputType_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,15,4),_CpqCmcSetupAux1InputType_Type())
cpqCmcSetupAux1InputType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAux1InputType.setStatus(_A)
class _CpqCmcSetupAux1Description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_CpqCmcSetupAux1Description_Type.__name__=_R
_CpqCmcSetupAux1Description_Object=MibScalar
cpqCmcSetupAux1Description=_CpqCmcSetupAux1Description_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,15,5),_CpqCmcSetupAux1Description_Type())
cpqCmcSetupAux1Description.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAux1Description.setStatus(_A)
class _CpqCmcSetupAux1Unlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_n,2),(_Z,3),(_a,4),(_G,5)))
_CpqCmcSetupAux1Unlock_Type.__name__=_B
_CpqCmcSetupAux1Unlock_Object=MibScalar
cpqCmcSetupAux1Unlock=_CpqCmcSetupAux1Unlock_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,15,6),_CpqCmcSetupAux1Unlock_Type())
cpqCmcSetupAux1Unlock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAux1Unlock.setStatus(_A)
_CpqCmcSetupAux2_ObjectIdentity=ObjectIdentity
cpqCmcSetupAux2=_CpqCmcSetupAux2_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,16))
class _CpqCmcSetupAux2Avail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_S,2),(_T,3)))
_CpqCmcSetupAux2Avail_Type.__name__=_B
_CpqCmcSetupAux2Avail_Object=MibScalar
cpqCmcSetupAux2Avail=_CpqCmcSetupAux2Avail_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,16,1),_CpqCmcSetupAux2Avail_Type())
cpqCmcSetupAux2Avail.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAux2Avail.setStatus(_A)
class _CpqCmcSetupAux2Relays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupAux2Relays_Type.__name__=_B
_CpqCmcSetupAux2Relays_Object=MibScalar
cpqCmcSetupAux2Relays=_CpqCmcSetupAux2Relays_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,16,2),_CpqCmcSetupAux2Relays_Type())
cpqCmcSetupAux2Relays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAux2Relays.setStatus(_A)
class _CpqCmcSetupAux2AudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupAux2AudibleAlarm_Type.__name__=_B
_CpqCmcSetupAux2AudibleAlarm_Object=MibScalar
cpqCmcSetupAux2AudibleAlarm=_CpqCmcSetupAux2AudibleAlarm_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,16,3),_CpqCmcSetupAux2AudibleAlarm_Type())
cpqCmcSetupAux2AudibleAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAux2AudibleAlarm.setStatus(_A)
class _CpqCmcSetupAux2InputType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_s,2),(_t,3)))
_CpqCmcSetupAux2InputType_Type.__name__=_B
_CpqCmcSetupAux2InputType_Object=MibScalar
cpqCmcSetupAux2InputType=_CpqCmcSetupAux2InputType_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,16,4),_CpqCmcSetupAux2InputType_Type())
cpqCmcSetupAux2InputType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAux2InputType.setStatus(_A)
class _CpqCmcSetupAux2Description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_CpqCmcSetupAux2Description_Type.__name__=_R
_CpqCmcSetupAux2Description_Object=MibScalar
cpqCmcSetupAux2Description=_CpqCmcSetupAux2Description_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,16,5),_CpqCmcSetupAux2Description_Type())
cpqCmcSetupAux2Description.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAux2Description.setStatus(_A)
class _CpqCmcSetupAux2Unlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_n,2),(_Z,3),(_a,4),(_G,5)))
_CpqCmcSetupAux2Unlock_Type.__name__=_B
_CpqCmcSetupAux2Unlock_Object=MibScalar
cpqCmcSetupAux2Unlock=_CpqCmcSetupAux2Unlock_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,16,6),_CpqCmcSetupAux2Unlock_Type())
cpqCmcSetupAux2Unlock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAux2Unlock.setStatus(_A)
_CpqCmcSetupAlarm1_ObjectIdentity=ObjectIdentity
cpqCmcSetupAlarm1=_CpqCmcSetupAlarm1_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,17))
class _CpqCmcSetupAlarm1Relays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupAlarm1Relays_Type.__name__=_B
_CpqCmcSetupAlarm1Relays_Object=MibScalar
cpqCmcSetupAlarm1Relays=_CpqCmcSetupAlarm1Relays_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,17,1),_CpqCmcSetupAlarm1Relays_Type())
cpqCmcSetupAlarm1Relays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAlarm1Relays.setStatus(_A)
class _CpqCmcSetupAlarm1AudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupAlarm1AudibleAlarm_Type.__name__=_B
_CpqCmcSetupAlarm1AudibleAlarm_Object=MibScalar
cpqCmcSetupAlarm1AudibleAlarm=_CpqCmcSetupAlarm1AudibleAlarm_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,17,2),_CpqCmcSetupAlarm1AudibleAlarm_Type())
cpqCmcSetupAlarm1AudibleAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAlarm1AudibleAlarm.setStatus(_A)
class _CpqCmcSetupAlarm1Description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_CpqCmcSetupAlarm1Description_Type.__name__=_R
_CpqCmcSetupAlarm1Description_Object=MibScalar
cpqCmcSetupAlarm1Description=_CpqCmcSetupAlarm1Description_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,17,3),_CpqCmcSetupAlarm1Description_Type())
cpqCmcSetupAlarm1Description.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAlarm1Description.setStatus(_A)
_CpqCmcSetupAlarm2_ObjectIdentity=ObjectIdentity
cpqCmcSetupAlarm2=_CpqCmcSetupAlarm2_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,2,18))
class _CpqCmcSetupAlarm2Relays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_I,2),(_K,3),(_L,4),(_G,5)))
_CpqCmcSetupAlarm2Relays_Type.__name__=_B
_CpqCmcSetupAlarm2Relays_Object=MibScalar
cpqCmcSetupAlarm2Relays=_CpqCmcSetupAlarm2Relays_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,18,1),_CpqCmcSetupAlarm2Relays_Type())
cpqCmcSetupAlarm2Relays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAlarm2Relays.setStatus(_A)
class _CpqCmcSetupAlarm2AudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcSetupAlarm2AudibleAlarm_Type.__name__=_B
_CpqCmcSetupAlarm2AudibleAlarm_Object=MibScalar
cpqCmcSetupAlarm2AudibleAlarm=_CpqCmcSetupAlarm2AudibleAlarm_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,18,2),_CpqCmcSetupAlarm2AudibleAlarm_Type())
cpqCmcSetupAlarm2AudibleAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAlarm2AudibleAlarm.setStatus(_A)
class _CpqCmcSetupAlarm2Description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_CpqCmcSetupAlarm2Description_Type.__name__=_R
_CpqCmcSetupAlarm2Description_Object=MibScalar
cpqCmcSetupAlarm2Description=_CpqCmcSetupAlarm2Description_Object((1,3,6,1,4,1,232,153,2,2,2,1,2,18,3),_CpqCmcSetupAlarm2Description_Type())
cpqCmcSetupAlarm2Description.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupAlarm2Description.setStatus(_A)
_CpqCmcSetupClock_ObjectIdentity=ObjectIdentity
cpqCmcSetupClock=_CpqCmcSetupClock_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,1,3))
class _CpqCmcSetupDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CpqCmcSetupDate_Type.__name__=_R
_CpqCmcSetupDate_Object=MibScalar
cpqCmcSetupDate=_CpqCmcSetupDate_Object((1,3,6,1,4,1,232,153,2,2,2,1,3,1),_CpqCmcSetupDate_Type())
cpqCmcSetupDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupDate.setStatus(_A)
class _CpqCmcSetupTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqCmcSetupTime_Type.__name__=_R
_CpqCmcSetupTime_Object=MibScalar
cpqCmcSetupTime=_CpqCmcSetupTime_Object((1,3,6,1,4,1,232,153,2,2,2,1,3,2),_CpqCmcSetupTime_Type())
cpqCmcSetupTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetupTime.setStatus(_A)
_CpqCmcSetupThreshold_ObjectIdentity=ObjectIdentity
cpqCmcSetupThreshold=_CpqCmcSetupThreshold_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,2))
class _CpqCmcThresholdMaxTemp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_CpqCmcThresholdMaxTemp1_Type.__name__=_B
_CpqCmcThresholdMaxTemp1_Object=MibScalar
cpqCmcThresholdMaxTemp1=_CpqCmcThresholdMaxTemp1_Object((1,3,6,1,4,1,232,153,2,2,2,2,1),_CpqCmcThresholdMaxTemp1_Type())
cpqCmcThresholdMaxTemp1.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcThresholdMaxTemp1.setStatus(_A)
class _CpqCmcThresholdWarningTemp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_CpqCmcThresholdWarningTemp1_Type.__name__=_B
_CpqCmcThresholdWarningTemp1_Object=MibScalar
cpqCmcThresholdWarningTemp1=_CpqCmcThresholdWarningTemp1_Object((1,3,6,1,4,1,232,153,2,2,2,2,2),_CpqCmcThresholdWarningTemp1_Type())
cpqCmcThresholdWarningTemp1.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcThresholdWarningTemp1.setStatus(_A)
class _CpqCmcThresholdMinTemp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpqCmcThresholdMinTemp1_Type.__name__=_B
_CpqCmcThresholdMinTemp1_Object=MibScalar
cpqCmcThresholdMinTemp1=_CpqCmcThresholdMinTemp1_Object((1,3,6,1,4,1,232,153,2,2,2,2,3),_CpqCmcThresholdMinTemp1_Type())
cpqCmcThresholdMinTemp1.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcThresholdMinTemp1.setStatus(_A)
class _CpqCmcThresholdMaxTemp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_CpqCmcThresholdMaxTemp2_Type.__name__=_B
_CpqCmcThresholdMaxTemp2_Object=MibScalar
cpqCmcThresholdMaxTemp2=_CpqCmcThresholdMaxTemp2_Object((1,3,6,1,4,1,232,153,2,2,2,2,4),_CpqCmcThresholdMaxTemp2_Type())
cpqCmcThresholdMaxTemp2.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcThresholdMaxTemp2.setStatus(_A)
class _CpqCmcThresholdWarningTemp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_CpqCmcThresholdWarningTemp2_Type.__name__=_B
_CpqCmcThresholdWarningTemp2_Object=MibScalar
cpqCmcThresholdWarningTemp2=_CpqCmcThresholdWarningTemp2_Object((1,3,6,1,4,1,232,153,2,2,2,2,5),_CpqCmcThresholdWarningTemp2_Type())
cpqCmcThresholdWarningTemp2.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcThresholdWarningTemp2.setStatus(_A)
class _CpqCmcThresholdMinTemp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpqCmcThresholdMinTemp2_Type.__name__=_B
_CpqCmcThresholdMinTemp2_Object=MibScalar
cpqCmcThresholdMinTemp2=_CpqCmcThresholdMinTemp2_Object((1,3,6,1,4,1,232,153,2,2,2,2,6),_CpqCmcThresholdMinTemp2_Type())
cpqCmcThresholdMinTemp2.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcThresholdMinTemp2.setStatus(_A)
class _CpqCmcThresholdFan1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_CpqCmcThresholdFan1_Type.__name__=_B
_CpqCmcThresholdFan1_Object=MibScalar
cpqCmcThresholdFan1=_CpqCmcThresholdFan1_Object((1,3,6,1,4,1,232,153,2,2,2,2,7),_CpqCmcThresholdFan1_Type())
cpqCmcThresholdFan1.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcThresholdFan1.setStatus(_A)
class _CpqCmcThresholdFan1Hysteresis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CpqCmcThresholdFan1Hysteresis_Type.__name__=_B
_CpqCmcThresholdFan1Hysteresis_Object=MibScalar
cpqCmcThresholdFan1Hysteresis=_CpqCmcThresholdFan1Hysteresis_Object((1,3,6,1,4,1,232,153,2,2,2,2,8),_CpqCmcThresholdFan1Hysteresis_Type())
cpqCmcThresholdFan1Hysteresis.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcThresholdFan1Hysteresis.setStatus(_A)
class _CpqCmcThresholdFan2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_CpqCmcThresholdFan2_Type.__name__=_B
_CpqCmcThresholdFan2_Object=MibScalar
cpqCmcThresholdFan2=_CpqCmcThresholdFan2_Object((1,3,6,1,4,1,232,153,2,2,2,2,9),_CpqCmcThresholdFan2_Type())
cpqCmcThresholdFan2.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcThresholdFan2.setStatus(_A)
class _CpqCmcThresholdFan2Hysteresis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CpqCmcThresholdFan2Hysteresis_Type.__name__=_B
_CpqCmcThresholdFan2Hysteresis_Object=MibScalar
cpqCmcThresholdFan2Hysteresis=_CpqCmcThresholdFan2Hysteresis_Object((1,3,6,1,4,1,232,153,2,2,2,2,10),_CpqCmcThresholdFan2Hysteresis_Type())
cpqCmcThresholdFan2Hysteresis.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcThresholdFan2Hysteresis.setStatus(_A)
class _CpqCmcThresholdMaxVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCmcThresholdMaxVoltage_Type.__name__=_B
_CpqCmcThresholdMaxVoltage_Object=MibScalar
cpqCmcThresholdMaxVoltage=_CpqCmcThresholdMaxVoltage_Object((1,3,6,1,4,1,232,153,2,2,2,2,11),_CpqCmcThresholdMaxVoltage_Type())
cpqCmcThresholdMaxVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcThresholdMaxVoltage.setStatus(_A)
class _CpqCmcThresholdMinVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCmcThresholdMinVoltage_Type.__name__=_B
_CpqCmcThresholdMinVoltage_Object=MibScalar
cpqCmcThresholdMinVoltage=_CpqCmcThresholdMinVoltage_Object((1,3,6,1,4,1,232,153,2,2,2,2,12),_CpqCmcThresholdMinVoltage_Type())
cpqCmcThresholdMinVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcThresholdMinVoltage.setStatus(_A)
class _CpqCmcThresholdMaxHumidity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpqCmcThresholdMaxHumidity_Type.__name__=_B
_CpqCmcThresholdMaxHumidity_Object=MibScalar
cpqCmcThresholdMaxHumidity=_CpqCmcThresholdMaxHumidity_Object((1,3,6,1,4,1,232,153,2,2,2,2,13),_CpqCmcThresholdMaxHumidity_Type())
cpqCmcThresholdMaxHumidity.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcThresholdMaxHumidity.setStatus(_A)
class _CpqCmcThresholdMinHumidity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpqCmcThresholdMinHumidity_Type.__name__=_B
_CpqCmcThresholdMinHumidity_Object=MibScalar
cpqCmcThresholdMinHumidity=_CpqCmcThresholdMinHumidity_Object((1,3,6,1,4,1,232,153,2,2,2,2,14),_CpqCmcThresholdMinHumidity_Type())
cpqCmcThresholdMinHumidity.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcThresholdMinHumidity.setStatus(_A)
_CpqCmcTraps_ObjectIdentity=ObjectIdentity
cpqCmcTraps=_CpqCmcTraps_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,2,3))
_CpqCmcTrapTableNumber_Type=Integer32
_CpqCmcTrapTableNumber_Object=MibScalar
cpqCmcTrapTableNumber=_CpqCmcTrapTableNumber_Object((1,3,6,1,4,1,232,153,2,2,2,3,1),_CpqCmcTrapTableNumber_Type())
cpqCmcTrapTableNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcTrapTableNumber.setStatus(_A)
_CpqCmcTrapTable_Object=MibTable
cpqCmcTrapTable=_CpqCmcTrapTable_Object((1,3,6,1,4,1,232,153,2,2,2,3,2))
if mibBuilder.loadTexts:cpqCmcTrapTable.setStatus(_A)
_CpqCmcTrapEntry_Object=MibTableRow
cpqCmcTrapEntry=_CpqCmcTrapEntry_Object((1,3,6,1,4,1,232,153,2,2,2,3,2,1))
cpqCmcTrapEntry.setIndexNames((0,_M,_u))
if mibBuilder.loadTexts:cpqCmcTrapEntry.setStatus(_A)
class _CpqCmcTrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CpqCmcTrapIndex_Type.__name__=_B
_CpqCmcTrapIndex_Object=MibTableColumn
cpqCmcTrapIndex=_CpqCmcTrapIndex_Object((1,3,6,1,4,1,232,153,2,2,2,3,2,1,1),_CpqCmcTrapIndex_Type())
cpqCmcTrapIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcTrapIndex.setStatus(_A)
class _CpqCmcTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_F,3)))
_CpqCmcTrapStatus_Type.__name__=_B
_CpqCmcTrapStatus_Object=MibTableColumn
cpqCmcTrapStatus=_CpqCmcTrapStatus_Object((1,3,6,1,4,1,232,153,2,2,2,3,2,1,2),_CpqCmcTrapStatus_Type())
cpqCmcTrapStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcTrapStatus.setStatus(_A)
class _CpqCmcTrapIPaddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CpqCmcTrapIPaddress_Type.__name__=_R
_CpqCmcTrapIPaddress_Object=MibTableColumn
cpqCmcTrapIPaddress=_CpqCmcTrapIPaddress_Object((1,3,6,1,4,1,232,153,2,2,2,3,2,1,3),_CpqCmcTrapIPaddress_Type())
cpqCmcTrapIPaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcTrapIPaddress.setStatus(_A)
_CpqCmcValues_ObjectIdentity=ObjectIdentity
cpqCmcValues=_CpqCmcValues_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,3))
_CpqCmcValueTemp1_Type=Integer32
_CpqCmcValueTemp1_Object=MibScalar
cpqCmcValueTemp1=_CpqCmcValueTemp1_Object((1,3,6,1,4,1,232,153,2,2,3,1),_CpqCmcValueTemp1_Type())
cpqCmcValueTemp1.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcValueTemp1.setStatus(_A)
_CpqCmcValueTemp2_Type=Integer32
_CpqCmcValueTemp2_Object=MibScalar
cpqCmcValueTemp2=_CpqCmcValueTemp2_Object((1,3,6,1,4,1,232,153,2,2,3,2),_CpqCmcValueTemp2_Type())
cpqCmcValueTemp2.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcValueTemp2.setStatus(_A)
_CpqCmcValueVoltage_Type=Integer32
_CpqCmcValueVoltage_Object=MibScalar
cpqCmcValueVoltage=_CpqCmcValueVoltage_Object((1,3,6,1,4,1,232,153,2,2,3,3),_CpqCmcValueVoltage_Type())
cpqCmcValueVoltage.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcValueVoltage.setStatus(_A)
_CpqCmcValueHumidity_Type=Integer32
_CpqCmcValueHumidity_Object=MibScalar
cpqCmcValueHumidity=_CpqCmcValueHumidity_Object((1,3,6,1,4,1,232,153,2,2,3,4),_CpqCmcValueHumidity_Type())
cpqCmcValueHumidity.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcValueHumidity.setStatus(_A)
class _CpqCmcValueOperatingTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CpqCmcValueOperatingTime_Type.__name__=_R
_CpqCmcValueOperatingTime_Object=MibScalar
cpqCmcValueOperatingTime=_CpqCmcValueOperatingTime_Object((1,3,6,1,4,1,232,153,2,2,3,5),_CpqCmcValueOperatingTime_Type())
cpqCmcValueOperatingTime.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcValueOperatingTime.setStatus(_A)
_CpqCmcStatus_ObjectIdentity=ObjectIdentity
cpqCmcStatus=_CpqCmcStatus_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,4))
class _CpqCmcStatusTemp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,1),(_h,2),(_v,3),(_i,4),(_j,5),(_U,6),(_f,7)))
_CpqCmcStatusTemp1_Type.__name__=_B
_CpqCmcStatusTemp1_Object=MibScalar
cpqCmcStatusTemp1=_CpqCmcStatusTemp1_Object((1,3,6,1,4,1,232,153,2,2,4,1),_CpqCmcStatusTemp1_Type())
cpqCmcStatusTemp1.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusTemp1.setStatus(_A)
class _CpqCmcStatusTemp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,1),(_h,2),(_v,3),(_i,4),(_j,5),(_U,6),(_f,7)))
_CpqCmcStatusTemp2_Type.__name__=_B
_CpqCmcStatusTemp2_Object=MibScalar
cpqCmcStatusTemp2=_CpqCmcStatusTemp2_Object((1,3,6,1,4,1,232,153,2,2,4,2),_CpqCmcStatusTemp2_Type())
cpqCmcStatusTemp2.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusTemp2.setStatus(_A)
class _CpqCmcStatusFan1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_D,1),(_w,2),(_x,3),(_y,4),(_z,5),('smokeOff',6),('doorOff',7),(_Y,8),(_f,9)))
_CpqCmcStatusFan1_Type.__name__=_B
_CpqCmcStatusFan1_Object=MibScalar
cpqCmcStatusFan1=_CpqCmcStatusFan1_Object((1,3,6,1,4,1,232,153,2,2,4,3),_CpqCmcStatusFan1_Type())
cpqCmcStatusFan1.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusFan1.setStatus(_A)
class _CpqCmcStatusFan2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_D,1),(_w,2),(_x,3),(_y,4),(_z,5),('smokeOff',6),('doorOff',7),(_Y,8),(_f,9)))
_CpqCmcStatusFan2_Type.__name__=_B
_CpqCmcStatusFan2_Object=MibScalar
cpqCmcStatusFan2=_CpqCmcStatusFan2_Object((1,3,6,1,4,1,232,153,2,2,4,4),_CpqCmcStatusFan2_Type())
cpqCmcStatusFan2.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusFan2.setStatus(_A)
class _CpqCmcStatusVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_h,2),(_i,3),(_j,4),('noVoltage',5)))
_CpqCmcStatusVoltage_Type.__name__=_B
_CpqCmcStatusVoltage_Object=MibScalar
cpqCmcStatusVoltage=_CpqCmcStatusVoltage_Object((1,3,6,1,4,1,232,153,2,2,4,5),_CpqCmcStatusVoltage_Type())
cpqCmcStatusVoltage.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusVoltage.setStatus(_A)
class _CpqCmcStatusHumidity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),(_h,2),(_i,3),(_j,4),(_U,5),(_f,6)))
_CpqCmcStatusHumidity_Type.__name__=_B
_CpqCmcStatusHumidity_Object=MibScalar
cpqCmcStatusHumidity=_CpqCmcStatusHumidity_Object((1,3,6,1,4,1,232,153,2,2,4,6),_CpqCmcStatusHumidity_Type())
cpqCmcStatusHumidity.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusHumidity.setStatus(_A)
class _CpqCmcStatusInput1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_k,2),(_l,3),(_U,4)))
_CpqCmcStatusInput1_Type.__name__=_B
_CpqCmcStatusInput1_Object=MibScalar
cpqCmcStatusInput1=_CpqCmcStatusInput1_Object((1,3,6,1,4,1,232,153,2,2,4,7),_CpqCmcStatusInput1_Type())
cpqCmcStatusInput1.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusInput1.setStatus(_A)
class _CpqCmcStatusInput2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_k,2),(_l,3),(_U,4)))
_CpqCmcStatusInput2_Type.__name__=_B
_CpqCmcStatusInput2_Object=MibScalar
cpqCmcStatusInput2=_CpqCmcStatusInput2_Object((1,3,6,1,4,1,232,153,2,2,4,8),_CpqCmcStatusInput2_Type())
cpqCmcStatusInput2.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusInput2.setStatus(_A)
class _CpqCmcStatusInput3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_k,2),(_l,3),(_U,4)))
_CpqCmcStatusInput3_Type.__name__=_B
_CpqCmcStatusInput3_Object=MibScalar
cpqCmcStatusInput3=_CpqCmcStatusInput3_Object((1,3,6,1,4,1,232,153,2,2,4,9),_CpqCmcStatusInput3_Type())
cpqCmcStatusInput3.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusInput3.setStatus(_A)
class _CpqCmcStatusInput4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_k,2),(_l,3),(_U,4)))
_CpqCmcStatusInput4_Type.__name__=_B
_CpqCmcStatusInput4_Object=MibScalar
cpqCmcStatusInput4=_CpqCmcStatusInput4_Object((1,3,6,1,4,1,232,153,2,2,4,10),_CpqCmcStatusInput4_Type())
cpqCmcStatusInput4.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusInput4.setStatus(_A)
class _CpqCmcStatusLock1Lock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_D,1),('locked',2),(_A0,3),(_A1,4),(_A2,5),(_A3,6),(_A4,7),(_A5,8),(_A6,9),(_A7,10),(_A8,11),(_c,12),(_A9,13),(_m,14)))
_CpqCmcStatusLock1Lock_Type.__name__=_B
_CpqCmcStatusLock1Lock_Object=MibScalar
cpqCmcStatusLock1Lock=_CpqCmcStatusLock1Lock_Object((1,3,6,1,4,1,232,153,2,2,4,11),_CpqCmcStatusLock1Lock_Type())
cpqCmcStatusLock1Lock.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusLock1Lock.setStatus(_A)
class _CpqCmcStatusLock2Lock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_D,1),('locked',2),(_A0,3),(_A1,4),(_A2,5),(_A3,6),(_A4,7),(_A5,8),(_A6,9),(_A7,10),(_A8,11),(_c,12),(_A9,13),(_m,14)))
_CpqCmcStatusLock2Lock_Type.__name__=_B
_CpqCmcStatusLock2Lock_Object=MibScalar
cpqCmcStatusLock2Lock=_CpqCmcStatusLock2Lock_Object((1,3,6,1,4,1,232,153,2,2,4,12),_CpqCmcStatusLock2Lock_Type())
cpqCmcStatusLock2Lock.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusLock2Lock.setStatus(_A)
class _CpqCmcStatusSmoke_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('cleared',2),('present',3),(_U,4)))
_CpqCmcStatusSmoke_Type.__name__=_B
_CpqCmcStatusSmoke_Object=MibScalar
cpqCmcStatusSmoke=_CpqCmcStatusSmoke_Object((1,3,6,1,4,1,232,153,2,2,4,13),_CpqCmcStatusSmoke_Type())
cpqCmcStatusSmoke.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusSmoke.setStatus(_A)
class _CpqCmcStatusShock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('cleared',2),('present',3),(_U,4)))
_CpqCmcStatusShock_Type.__name__=_B
_CpqCmcStatusShock_Object=MibScalar
cpqCmcStatusShock=_CpqCmcStatusShock_Object((1,3,6,1,4,1,232,153,2,2,4,14),_CpqCmcStatusShock_Type())
cpqCmcStatusShock.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusShock.setStatus(_A)
class _CpqCmcStatusAux1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_W,2),(_c,3),(_U,4)))
_CpqCmcStatusAux1_Type.__name__=_B
_CpqCmcStatusAux1_Object=MibScalar
cpqCmcStatusAux1=_CpqCmcStatusAux1_Object((1,3,6,1,4,1,232,153,2,2,4,15),_CpqCmcStatusAux1_Type())
cpqCmcStatusAux1.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusAux1.setStatus(_A)
class _CpqCmcStatusAux2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_W,2),(_c,3),(_U,4)))
_CpqCmcStatusAux2_Type.__name__=_B
_CpqCmcStatusAux2_Object=MibScalar
cpqCmcStatusAux2=_CpqCmcStatusAux2_Object((1,3,6,1,4,1,232,153,2,2,4,16),_CpqCmcStatusAux2_Type())
cpqCmcStatusAux2.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusAux2.setStatus(_A)
class _CpqCmcStatusAlarm1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_W,2),(_c,3)))
_CpqCmcStatusAlarm1_Type.__name__=_B
_CpqCmcStatusAlarm1_Object=MibScalar
cpqCmcStatusAlarm1=_CpqCmcStatusAlarm1_Object((1,3,6,1,4,1,232,153,2,2,4,17),_CpqCmcStatusAlarm1_Type())
cpqCmcStatusAlarm1.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusAlarm1.setStatus(_A)
class _CpqCmcStatusAlarm2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_W,2),(_c,3)))
_CpqCmcStatusAlarm2_Type.__name__=_B
_CpqCmcStatusAlarm2_Object=MibScalar
cpqCmcStatusAlarm2=_CpqCmcStatusAlarm2_Object((1,3,6,1,4,1,232,153,2,2,4,18),_CpqCmcStatusAlarm2_Type())
cpqCmcStatusAlarm2.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusAlarm2.setStatus(_A)
class _CpqCmcStatusLock1Dev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_D,1),(_W,2),(_AA,3),(_AB,4),(_AC,5),(_AD,6),(_AE,7),(_m,8)))
_CpqCmcStatusLock1Dev_Type.__name__=_B
_CpqCmcStatusLock1Dev_Object=MibScalar
cpqCmcStatusLock1Dev=_CpqCmcStatusLock1Dev_Object((1,3,6,1,4,1,232,153,2,2,4,19),_CpqCmcStatusLock1Dev_Type())
cpqCmcStatusLock1Dev.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusLock1Dev.setStatus(_A)
class _CpqCmcStatusLock2Dev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_D,1),(_W,2),(_AA,3),(_AB,4),(_AC,5),(_AD,6),(_AE,7),(_m,8)))
_CpqCmcStatusLock2Dev_Type.__name__=_B
_CpqCmcStatusLock2Dev_Object=MibScalar
cpqCmcStatusLock2Dev=_CpqCmcStatusLock2Dev_Object((1,3,6,1,4,1,232,153,2,2,4,20),_CpqCmcStatusLock2Dev_Type())
cpqCmcStatusLock2Dev.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcStatusLock2Dev.setStatus(_A)
_CpqCmcControl_ObjectIdentity=ObjectIdentity
cpqCmcControl=_CpqCmcControl_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,5))
class _CpqCmcStatusAccess_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CpqCmcStatusAccess_Type.__name__=_R
_CpqCmcStatusAccess_Object=MibScalar
cpqCmcStatusAccess=_CpqCmcStatusAccess_Object((1,3,6,1,4,1,232,153,2,2,5,1),_CpqCmcStatusAccess_Type())
cpqCmcStatusAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcStatusAccess.setStatus(_A)
class _CpqCmcSetLock1Lock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('lockDoor',2),(_AF,3),('openDoor',4)))
_CpqCmcSetLock1Lock_Type.__name__=_B
_CpqCmcSetLock1Lock_Object=MibScalar
cpqCmcSetLock1Lock=_CpqCmcSetLock1Lock_Object((1,3,6,1,4,1,232,153,2,2,5,2),_CpqCmcSetLock1Lock_Type())
cpqCmcSetLock1Lock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetLock1Lock.setStatus(_A)
class _CpqCmcSetLock1Key_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),('disable',2),(_AG,3),(_AH,4),(_AI,5)))
_CpqCmcSetLock1Key_Type.__name__=_B
_CpqCmcSetLock1Key_Object=MibScalar
cpqCmcSetLock1Key=_CpqCmcSetLock1Key_Object((1,3,6,1,4,1,232,153,2,2,5,3),_CpqCmcSetLock1Key_Type())
cpqCmcSetLock1Key.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetLock1Key.setStatus(_A)
class _CpqCmcSetLock2Lock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('lockDoor',2),(_AF,3),('openDoor',4)))
_CpqCmcSetLock2Lock_Type.__name__=_B
_CpqCmcSetLock2Lock_Object=MibScalar
cpqCmcSetLock2Lock=_CpqCmcSetLock2Lock_Object((1,3,6,1,4,1,232,153,2,2,5,4),_CpqCmcSetLock2Lock_Type())
cpqCmcSetLock2Lock.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetLock2Lock.setStatus(_A)
class _CpqCmcSetLock2Key_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),('disable',2),(_AG,3),(_AH,4),(_AI,5)))
_CpqCmcSetLock2Key_Type.__name__=_B
_CpqCmcSetLock2Key_Object=MibScalar
cpqCmcSetLock2Key=_CpqCmcSetLock2Key_Object((1,3,6,1,4,1,232,153,2,2,5,5),_CpqCmcSetLock2Key_Type())
cpqCmcSetLock2Key.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetLock2Key.setStatus(_A)
class _CpqCmcSetMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CpqCmcSetMessage_Type.__name__=_R
_CpqCmcSetMessage_Object=MibScalar
cpqCmcSetMessage=_CpqCmcSetMessage_Object((1,3,6,1,4,1,232,153,2,2,5,6),_CpqCmcSetMessage_Type())
cpqCmcSetMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetMessage.setStatus(_A)
class _CpqCmcSetAlarm1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_AJ,2),('setAlarm',3)))
_CpqCmcSetAlarm1_Type.__name__=_B
_CpqCmcSetAlarm1_Object=MibScalar
cpqCmcSetAlarm1=_CpqCmcSetAlarm1_Object((1,3,6,1,4,1,232,153,2,2,5,7),_CpqCmcSetAlarm1_Type())
cpqCmcSetAlarm1.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetAlarm1.setStatus(_A)
class _CpqCmcSetAlarm2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_AJ,2),('setAlarm',3)))
_CpqCmcSetAlarm2_Type.__name__=_B
_CpqCmcSetAlarm2_Object=MibScalar
cpqCmcSetAlarm2=_CpqCmcSetAlarm2_Object((1,3,6,1,4,1,232,153,2,2,5,8),_CpqCmcSetAlarm2_Type())
cpqCmcSetAlarm2.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetAlarm2.setStatus(_A)
class _CpqCmcSetFan1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_V,2),(_b,3),(_I,4)))
_CpqCmcSetFan1_Type.__name__=_B
_CpqCmcSetFan1_Object=MibScalar
cpqCmcSetFan1=_CpqCmcSetFan1_Object((1,3,6,1,4,1,232,153,2,2,5,9),_CpqCmcSetFan1_Type())
cpqCmcSetFan1.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetFan1.setStatus(_A)
class _CpqCmcSetFan2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_V,2),(_b,3),(_I,4)))
_CpqCmcSetFan2_Type.__name__=_B
_CpqCmcSetFan2_Object=MibScalar
cpqCmcSetFan2=_CpqCmcSetFan2_Object((1,3,6,1,4,1,232,153,2,2,5,10),_CpqCmcSetFan2_Type())
cpqCmcSetFan2.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetFan2.setStatus(_A)
class _CpqCmcSetQuitRelay1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('switched',2),(_AK,3),('quit',4)))
_CpqCmcSetQuitRelay1_Type.__name__=_B
_CpqCmcSetQuitRelay1_Object=MibScalar
cpqCmcSetQuitRelay1=_CpqCmcSetQuitRelay1_Object((1,3,6,1,4,1,232,153,2,2,5,11),_CpqCmcSetQuitRelay1_Type())
cpqCmcSetQuitRelay1.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetQuitRelay1.setStatus(_A)
class _CpqCmcSetQuitRelay2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('switched',2),(_AK,3),('quit',4)))
_CpqCmcSetQuitRelay2_Type.__name__=_B
_CpqCmcSetQuitRelay2_Object=MibScalar
cpqCmcSetQuitRelay2=_CpqCmcSetQuitRelay2_Object((1,3,6,1,4,1,232,153,2,2,5,12),_CpqCmcSetQuitRelay2_Type())
cpqCmcSetQuitRelay2.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqCmcSetQuitRelay2.setStatus(_A)
_CpqCmcLog_ObjectIdentity=ObjectIdentity
cpqCmcLog=_CpqCmcLog_ObjectIdentity((1,3,6,1,4,1,232,153,2,2,6))
class _CpqCmcLogsNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpqCmcLogsNumber_Type.__name__=_B
_CpqCmcLogsNumber_Object=MibScalar
cpqCmcLogsNumber=_CpqCmcLogsNumber_Object((1,3,6,1,4,1,232,153,2,2,6,1),_CpqCmcLogsNumber_Type())
cpqCmcLogsNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcLogsNumber.setStatus(_A)
_CpqCmcLogTable_Object=MibTable
cpqCmcLogTable=_CpqCmcLogTable_Object((1,3,6,1,4,1,232,153,2,2,6,2))
if mibBuilder.loadTexts:cpqCmcLogTable.setStatus(_A)
_CpqCmcLogEntry_Object=MibTableRow
cpqCmcLogEntry=_CpqCmcLogEntry_Object((1,3,6,1,4,1,232,153,2,2,6,2,1))
cpqCmcLogEntry.setIndexNames((0,_M,_AL))
if mibBuilder.loadTexts:cpqCmcLogEntry.setStatus(_A)
class _CpqCmcLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CpqCmcLogIndex_Type.__name__=_B
_CpqCmcLogIndex_Object=MibTableColumn
cpqCmcLogIndex=_CpqCmcLogIndex_Object((1,3,6,1,4,1,232,153,2,2,6,2,1,1),_CpqCmcLogIndex_Type())
cpqCmcLogIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcLogIndex.setStatus(_A)
class _CpqCmcLogDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_CpqCmcLogDate_Type.__name__=_R
_CpqCmcLogDate_Object=MibTableColumn
cpqCmcLogDate=_CpqCmcLogDate_Object((1,3,6,1,4,1,232,153,2,2,6,2,1,2),_CpqCmcLogDate_Type())
cpqCmcLogDate.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcLogDate.setStatus(_A)
class _CpqCmcLogTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_CpqCmcLogTime_Type.__name__=_R
_CpqCmcLogTime_Object=MibTableColumn
cpqCmcLogTime=_CpqCmcLogTime_Object((1,3,6,1,4,1,232,153,2,2,6,2,1,3),_CpqCmcLogTime_Type())
cpqCmcLogTime.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcLogTime.setStatus(_A)
class _CpqCmcLogText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CpqCmcLogText_Type.__name__=_R
_CpqCmcLogText_Object=MibTableColumn
cpqCmcLogText=_CpqCmcLogText_Object((1,3,6,1,4,1,232,153,2,2,6,2,1,4),_CpqCmcLogText_Type())
cpqCmcLogText.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcLogText.setStatus(_A)
class _CpqCmcLogClass_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CpqCmcLogClass_Type.__name__=_R
_CpqCmcLogClass_Object=MibTableColumn
cpqCmcLogClass=_CpqCmcLogClass_Object((1,3,6,1,4,1,232,153,2,2,6,2,1,5),_CpqCmcLogClass_Type())
cpqCmcLogClass.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqCmcLogClass.setStatus(_A)
cpqCmcalarmTemp1=NotificationType((1,3,6,1,4,1,232,153,0,153001))
cpqCmcalarmTemp1.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_AM)))
if mibBuilder.loadTexts:cpqCmcalarmTemp1.setStatus('')
cpqCmcalarmTemp2=NotificationType((1,3,6,1,4,1,232,153,0,153002))
cpqCmcalarmTemp2.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_AN)))
if mibBuilder.loadTexts:cpqCmcalarmTemp2.setStatus('')
cpqCmcalarmFan1=NotificationType((1,3,6,1,4,1,232,153,0,153003))
cpqCmcalarmFan1.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_AO)))
if mibBuilder.loadTexts:cpqCmcalarmFan1.setStatus('')
cpqCmcalarmFan2=NotificationType((1,3,6,1,4,1,232,153,0,153004))
cpqCmcalarmFan2.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_AP)))
if mibBuilder.loadTexts:cpqCmcalarmFan2.setStatus('')
cpqCmcalarmVoltage=NotificationType((1,3,6,1,4,1,232,153,0,153005))
cpqCmcalarmVoltage.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_AQ)))
if mibBuilder.loadTexts:cpqCmcalarmVoltage.setStatus('')
cpqCmcalarmHumidity=NotificationType((1,3,6,1,4,1,232,153,0,153006))
cpqCmcalarmHumidity.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_AR)))
if mibBuilder.loadTexts:cpqCmcalarmHumidity.setStatus('')
cpqCmcalarmInput1=NotificationType((1,3,6,1,4,1,232,153,0,153007))
cpqCmcalarmInput1.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_AS)))
if mibBuilder.loadTexts:cpqCmcalarmInput1.setStatus('')
cpqCmcalarmInput2=NotificationType((1,3,6,1,4,1,232,153,0,153008))
cpqCmcalarmInput2.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_AT)))
if mibBuilder.loadTexts:cpqCmcalarmInput2.setStatus('')
cpqCmcalarmInput3=NotificationType((1,3,6,1,4,1,232,153,0,153009))
cpqCmcalarmInput3.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_AU)))
if mibBuilder.loadTexts:cpqCmcalarmInput3.setStatus('')
cpqCmcalarmInput4=NotificationType((1,3,6,1,4,1,232,153,0,153010))
cpqCmcalarmInput4.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_AV)))
if mibBuilder.loadTexts:cpqCmcalarmInput4.setStatus('')
cpqCmcalarmLock1=NotificationType((1,3,6,1,4,1,232,153,0,153011))
cpqCmcalarmLock1.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_AW)))
if mibBuilder.loadTexts:cpqCmcalarmLock1.setStatus('')
cpqCmcalarmLock2=NotificationType((1,3,6,1,4,1,232,153,0,153012))
cpqCmcalarmLock2.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_AX)))
if mibBuilder.loadTexts:cpqCmcalarmLock2.setStatus('')
cpqCmcalarmSmoke=NotificationType((1,3,6,1,4,1,232,153,0,153013))
cpqCmcalarmSmoke.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_AY)))
if mibBuilder.loadTexts:cpqCmcalarmSmoke.setStatus('')
cpqCmcalarmShock=NotificationType((1,3,6,1,4,1,232,153,0,153014))
cpqCmcalarmShock.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_AZ)))
if mibBuilder.loadTexts:cpqCmcalarmShock.setStatus('')
cpqCmcalarmAux1=NotificationType((1,3,6,1,4,1,232,153,0,153015))
cpqCmcalarmAux1.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_Aa)))
if mibBuilder.loadTexts:cpqCmcalarmAux1.setStatus('')
cpqCmcalarmAux2=NotificationType((1,3,6,1,4,1,232,153,0,153016))
cpqCmcalarmAux2.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_Ab)))
if mibBuilder.loadTexts:cpqCmcalarmAux2.setStatus('')
cpqCmcalarm1=NotificationType((1,3,6,1,4,1,232,153,0,153017))
cpqCmcalarm1.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_Ac)))
if mibBuilder.loadTexts:cpqCmcalarm1.setStatus('')
cpqCmcalarm2=NotificationType((1,3,6,1,4,1,232,153,0,153018))
cpqCmcalarm2.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_Ad)))
if mibBuilder.loadTexts:cpqCmcalarm2.setStatus('')
cpqCmcalarmLock1Dev=NotificationType((1,3,6,1,4,1,232,153,0,153019))
cpqCmcalarmLock1Dev.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_Ae)))
if mibBuilder.loadTexts:cpqCmcalarmLock1Dev.setStatus('')
cpqCmcalarmLock2Dev=NotificationType((1,3,6,1,4,1,232,153,0,153020))
cpqCmcalarmLock2Dev.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P),(_M,_Af)))
if mibBuilder.loadTexts:cpqCmcalarmLock2Dev.setStatus('')
cpqCmcSetupChanged=NotificationType((1,3,6,1,4,1,232,153,0,153100))
cpqCmcSetupChanged.setObjects(*((_E,_O),(_E,_N),(_E,_Q),(_E,_P)))
if mibBuilder.loadTexts:cpqCmcSetupChanged.setStatus('')
mibBuilder.exportSymbols(_M,**{'cpqCmc':cpqCmc,'cpqCmcalarmTemp1':cpqCmcalarmTemp1,'cpqCmcalarmTemp2':cpqCmcalarmTemp2,'cpqCmcalarmFan1':cpqCmcalarmFan1,'cpqCmcalarmFan2':cpqCmcalarmFan2,'cpqCmcalarmVoltage':cpqCmcalarmVoltage,'cpqCmcalarmHumidity':cpqCmcalarmHumidity,'cpqCmcalarmInput1':cpqCmcalarmInput1,'cpqCmcalarmInput2':cpqCmcalarmInput2,'cpqCmcalarmInput3':cpqCmcalarmInput3,'cpqCmcalarmInput4':cpqCmcalarmInput4,'cpqCmcalarmLock1':cpqCmcalarmLock1,'cpqCmcalarmLock2':cpqCmcalarmLock2,'cpqCmcalarmSmoke':cpqCmcalarmSmoke,'cpqCmcalarmShock':cpqCmcalarmShock,'cpqCmcalarmAux1':cpqCmcalarmAux1,'cpqCmcalarmAux2':cpqCmcalarmAux2,'cpqCmcalarm1':cpqCmcalarm1,'cpqCmcalarm2':cpqCmcalarm2,'cpqCmcalarmLock1Dev':cpqCmcalarmLock1Dev,'cpqCmcalarmLock2Dev':cpqCmcalarmLock2Dev,'cpqCmcSetupChanged':cpqCmcSetupChanged,'cpqCmcMibRev':cpqCmcMibRev,'cpqCmcMibRevMajor':cpqCmcMibRevMajor,'cpqCmcMibRevMinor':cpqCmcMibRevMinor,'cpqCmcMibCondition':cpqCmcMibCondition,'cpqCmcComponent':cpqCmcComponent,'cpqCmcInterface':cpqCmcInterface,'cpqCmcOsCommon':cpqCmcOsCommon,'cpqCmcOsCommonPollFreq':cpqCmcOsCommonPollFreq,'cpqCmcDevice':cpqCmcDevice,'cpqCmcDeviceCondition':cpqCmcDeviceCondition,'cpqCmcSetup':cpqCmcSetup,'cpqCmcSetupConfig':cpqCmcSetupConfig,'cpqCmcSetupGeneral':cpqCmcSetupGeneral,'cpqCmcsetLanguage':cpqCmcsetLanguage,'cpqCmcsetTempUnit':cpqCmcsetTempUnit,'cpqCmcsetAudibleAlarm':cpqCmcsetAudibleAlarm,'cpqCmcPassword':cpqCmcPassword,'cpqCmcPasswordOption':cpqCmcPasswordOption,'cpqCmcquitRelay1':cpqCmcquitRelay1,'cpqCmcquitRelay2':cpqCmcquitRelay2,'cpqCmclogicRelay1':cpqCmclogicRelay1,'cpqCmclogicRelay2':cpqCmclogicRelay2,'cpqCmcSetupEvents':cpqCmcSetupEvents,'cpqCmcSetupTemp1':cpqCmcSetupTemp1,'cpqCmcSetupTemp1Avail':cpqCmcSetupTemp1Avail,'cpqCmcSetupTemp1RelaysWarn':cpqCmcSetupTemp1RelaysWarn,'cpqCmcSetupTemp1RelaysMax':cpqCmcSetupTemp1RelaysMax,'cpqCmcSetupTemp1RelaysMin':cpqCmcSetupTemp1RelaysMin,'cpqCmcSetupTemp1AudibleAlarmWarn':cpqCmcSetupTemp1AudibleAlarmWarn,'cpqCmcSetupTemp1AudibleAlarmMax':cpqCmcSetupTemp1AudibleAlarmMax,'cpqCmcSetupTemp1AudibleAlarmMin':cpqCmcSetupTemp1AudibleAlarmMin,'cpqCmcSetupTemp2':cpqCmcSetupTemp2,'cpqCmcSetupTemp2Avail':cpqCmcSetupTemp2Avail,'cpqCmcSetupTemp2RelaysWarn':cpqCmcSetupTemp2RelaysWarn,'cpqCmcSetupTemp2RelaysMax':cpqCmcSetupTemp2RelaysMax,'cpqCmcSetupTemp2RelaysMin':cpqCmcSetupTemp2RelaysMin,'cpqCmcSetupTemp2AudibleAlarmWarn':cpqCmcSetupTemp2AudibleAlarmWarn,'cpqCmcSetupTemp2AudibleAlarmMax':cpqCmcSetupTemp2AudibleAlarmMax,'cpqCmcSetupTemp2AudibleAlarmMin':cpqCmcSetupTemp2AudibleAlarmMin,'cpqCmcSetupFan1':cpqCmcSetupFan1,'cpqCmcSetupFan1Avail':cpqCmcSetupFan1Avail,'cpqCmcSetupFan1Relays':cpqCmcSetupFan1Relays,'cpqCmcSetupFan1AudibleAlarm':cpqCmcSetupFan1AudibleAlarm,'cpqCmcSetupFan2':cpqCmcSetupFan2,'cpqCmcSetupFan2Avail':cpqCmcSetupFan2Avail,'cpqCmcSetupFan2Relays':cpqCmcSetupFan2Relays,'cpqCmcSetupFan2AudibleAlarm':cpqCmcSetupFan2AudibleAlarm,'cpqCmcSetupVoltage':cpqCmcSetupVoltage,'cpqCmcSetupVoltageAvail':cpqCmcSetupVoltageAvail,'cpqCmcSetupVoltageRelaysMax':cpqCmcSetupVoltageRelaysMax,'cpqCmcSetupVoltageRelaysMin':cpqCmcSetupVoltageRelaysMin,'cpqCmcSetupVoltageAudibleAlarmMax':cpqCmcSetupVoltageAudibleAlarmMax,'cpqCmcSetupVoltageAudibleAlarmMin':cpqCmcSetupVoltageAudibleAlarmMin,'cpqCmcSetupHumidity':cpqCmcSetupHumidity,'cpqCmcSetupHumidityAvail':cpqCmcSetupHumidityAvail,'cpqCmcSetupHumidityRelaysMax':cpqCmcSetupHumidityRelaysMax,'cpqCmcSetupHumidityRelaysMin':cpqCmcSetupHumidityRelaysMin,'cpqCmcSetupHumidityAudibleAlarmMax':cpqCmcSetupHumidityAudibleAlarmMax,'cpqCmcSetupHumidityAudibleAlarmMin':cpqCmcSetupHumidityAudibleAlarmMin,'cpqCmcSetupInput1':cpqCmcSetupInput1,'cpqCmcSetupInput1Avail':cpqCmcSetupInput1Avail,'cpqCmcSetupInput1Relays':cpqCmcSetupInput1Relays,'cpqCmcSetupInput1AudibleAlarm':cpqCmcSetupInput1AudibleAlarm,'cpqCmcSetupInput1FansOff':cpqCmcSetupInput1FansOff,'cpqCmcSetupInput1ShockSensor':cpqCmcSetupInput1ShockSensor,'cpqCmcSetupInput1Description':cpqCmcSetupInput1Description,'cpqCmcSetupInput1Lock':cpqCmcSetupInput1Lock,'cpqCmcSetupInput2':cpqCmcSetupInput2,'cpqCmcSetupInput2Avail':cpqCmcSetupInput2Avail,'cpqCmcSetupInput2Relays':cpqCmcSetupInput2Relays,'cpqCmcSetupInput2AudibleAlarm':cpqCmcSetupInput2AudibleAlarm,'cpqCmcSetupInput2FansOff':cpqCmcSetupInput2FansOff,'cpqCmcSetupInput2ShockSensor':cpqCmcSetupInput2ShockSensor,'cpqCmcSetupInput2Description':cpqCmcSetupInput2Description,'cpqCmcSetupInput2Lock':cpqCmcSetupInput2Lock,'cpqCmcSetupInput3':cpqCmcSetupInput3,'cpqCmcSetupInput3Avail':cpqCmcSetupInput3Avail,'cpqCmcSetupInput3Relays':cpqCmcSetupInput3Relays,'cpqCmcSetupInput3AudibleAlarm':cpqCmcSetupInput3AudibleAlarm,'cpqCmcSetupInput3FansOff':cpqCmcSetupInput3FansOff,'cpqCmcSetupInput3ShockSensor':cpqCmcSetupInput3ShockSensor,'cpqCmcSetupInput3Description':cpqCmcSetupInput3Description,'cpqCmcSetupInput3Lock':cpqCmcSetupInput3Lock,'cpqCmcSetupInput4':cpqCmcSetupInput4,'cpqCmcSetupInput4Avail':cpqCmcSetupInput4Avail,'cpqCmcSetupInput4Relays':cpqCmcSetupInput4Relays,'cpqCmcSetupInput4AudibleAlarm':cpqCmcSetupInput4AudibleAlarm,'cpqCmcSetupInput4FansOff':cpqCmcSetupInput4FansOff,'cpqCmcSetupInput4ShockSensor':cpqCmcSetupInput4ShockSensor,'cpqCmcSetupInput4Description':cpqCmcSetupInput4Description,'cpqCmcSetupInput4Lock':cpqCmcSetupInput4Lock,'cpqCmcSetupLock1':cpqCmcSetupLock1,'cpqCmcSetupLock1Avail':cpqCmcSetupLock1Avail,'cpqCmcSetupLock1Relays':cpqCmcSetupLock1Relays,'cpqCmcSetupLock1RelaysDevice':cpqCmcSetupLock1RelaysDevice,'cpqCmcSetupLock1AudibleAlarm':cpqCmcSetupLock1AudibleAlarm,'cpqCmcSetupLock1AudibleAlarmDevice':cpqCmcSetupLock1AudibleAlarmDevice,'cpqCmcSetupLock1Time':cpqCmcSetupLock1Time,'cpqCmcSetupLock1PwrFailUnlock':cpqCmcSetupLock1PwrFailUnlock,'cpqCmcSetupLock1BattLowUnlock':cpqCmcSetupLock1BattLowUnlock,'cpqCmcSetupLock1NetFailUnlock':cpqCmcSetupLock1NetFailUnlock,'cpqCmcSetupLock1LifeFailUnlock':cpqCmcSetupLock1LifeFailUnlock,'cpqCmcSetupLock2':cpqCmcSetupLock2,'cpqCmcSetupLock2Avail':cpqCmcSetupLock2Avail,'cpqCmcSetupLock2Relays':cpqCmcSetupLock2Relays,'cpqCmcSetupLock2RelaysDevice':cpqCmcSetupLock2RelaysDevice,'cpqCmcSetupLock2AudibleAlarm':cpqCmcSetupLock2AudibleAlarm,'cpqCmcSetupLock2AudibleAlarmDevice':cpqCmcSetupLock2AudibleAlarmDevice,'cpqCmcSetupLock2Time':cpqCmcSetupLock2Time,'cpqCmcSetupLock2PwrFailUnlock':cpqCmcSetupLock2PwrFailUnlock,'cpqCmcSetupLock2BattLowUnlock':cpqCmcSetupLock2BattLowUnlock,'cpqCmcSetupLock2NetFailUnlock':cpqCmcSetupLock2NetFailUnlock,'cpqCmcSetupLock2LifeFailUnlock':cpqCmcSetupLock2LifeFailUnlock,'cpqCmcSetupSmoke':cpqCmcSetupSmoke,'cpqCmcSetupSmokeAvail':cpqCmcSetupSmokeAvail,'cpqCmcSetupSmokeRelays':cpqCmcSetupSmokeRelays,'cpqCmcSetupSmokeAudibleAlarm':cpqCmcSetupSmokeAudibleAlarm,'cpqCmcSetupSmokeFansOff':cpqCmcSetupSmokeFansOff,'cpqCmcSetupSmokeUnlock':cpqCmcSetupSmokeUnlock,'cpqCmcSetupShock':cpqCmcSetupShock,'cpqCmcSetupShockAvail':cpqCmcSetupShockAvail,'cpqCmcSetupShockRelays':cpqCmcSetupShockRelays,'cpqCmcSetupShockAudibleAlarm':cpqCmcSetupShockAudibleAlarm,'cpqCmcSetupShockSensitivity':cpqCmcSetupShockSensitivity,'cpqCmcSetupAux1':cpqCmcSetupAux1,'cpqCmcSetupAux1Avail':cpqCmcSetupAux1Avail,'cpqCmcSetupAux1Relays':cpqCmcSetupAux1Relays,'cpqCmcSetupAux1AudibleAlarm':cpqCmcSetupAux1AudibleAlarm,'cpqCmcSetupAux1InputType':cpqCmcSetupAux1InputType,'cpqCmcSetupAux1Description':cpqCmcSetupAux1Description,'cpqCmcSetupAux1Unlock':cpqCmcSetupAux1Unlock,'cpqCmcSetupAux2':cpqCmcSetupAux2,'cpqCmcSetupAux2Avail':cpqCmcSetupAux2Avail,'cpqCmcSetupAux2Relays':cpqCmcSetupAux2Relays,'cpqCmcSetupAux2AudibleAlarm':cpqCmcSetupAux2AudibleAlarm,'cpqCmcSetupAux2InputType':cpqCmcSetupAux2InputType,'cpqCmcSetupAux2Description':cpqCmcSetupAux2Description,'cpqCmcSetupAux2Unlock':cpqCmcSetupAux2Unlock,'cpqCmcSetupAlarm1':cpqCmcSetupAlarm1,'cpqCmcSetupAlarm1Relays':cpqCmcSetupAlarm1Relays,'cpqCmcSetupAlarm1AudibleAlarm':cpqCmcSetupAlarm1AudibleAlarm,'cpqCmcSetupAlarm1Description':cpqCmcSetupAlarm1Description,'cpqCmcSetupAlarm2':cpqCmcSetupAlarm2,'cpqCmcSetupAlarm2Relays':cpqCmcSetupAlarm2Relays,'cpqCmcSetupAlarm2AudibleAlarm':cpqCmcSetupAlarm2AudibleAlarm,'cpqCmcSetupAlarm2Description':cpqCmcSetupAlarm2Description,'cpqCmcSetupClock':cpqCmcSetupClock,'cpqCmcSetupDate':cpqCmcSetupDate,'cpqCmcSetupTime':cpqCmcSetupTime,'cpqCmcSetupThreshold':cpqCmcSetupThreshold,'cpqCmcThresholdMaxTemp1':cpqCmcThresholdMaxTemp1,'cpqCmcThresholdWarningTemp1':cpqCmcThresholdWarningTemp1,'cpqCmcThresholdMinTemp1':cpqCmcThresholdMinTemp1,'cpqCmcThresholdMaxTemp2':cpqCmcThresholdMaxTemp2,'cpqCmcThresholdWarningTemp2':cpqCmcThresholdWarningTemp2,'cpqCmcThresholdMinTemp2':cpqCmcThresholdMinTemp2,'cpqCmcThresholdFan1':cpqCmcThresholdFan1,'cpqCmcThresholdFan1Hysteresis':cpqCmcThresholdFan1Hysteresis,'cpqCmcThresholdFan2':cpqCmcThresholdFan2,'cpqCmcThresholdFan2Hysteresis':cpqCmcThresholdFan2Hysteresis,'cpqCmcThresholdMaxVoltage':cpqCmcThresholdMaxVoltage,'cpqCmcThresholdMinVoltage':cpqCmcThresholdMinVoltage,'cpqCmcThresholdMaxHumidity':cpqCmcThresholdMaxHumidity,'cpqCmcThresholdMinHumidity':cpqCmcThresholdMinHumidity,'cpqCmcTraps':cpqCmcTraps,'cpqCmcTrapTableNumber':cpqCmcTrapTableNumber,'cpqCmcTrapTable':cpqCmcTrapTable,'cpqCmcTrapEntry':cpqCmcTrapEntry,_u:cpqCmcTrapIndex,'cpqCmcTrapStatus':cpqCmcTrapStatus,'cpqCmcTrapIPaddress':cpqCmcTrapIPaddress,'cpqCmcValues':cpqCmcValues,'cpqCmcValueTemp1':cpqCmcValueTemp1,'cpqCmcValueTemp2':cpqCmcValueTemp2,'cpqCmcValueVoltage':cpqCmcValueVoltage,'cpqCmcValueHumidity':cpqCmcValueHumidity,'cpqCmcValueOperatingTime':cpqCmcValueOperatingTime,'cpqCmcStatus':cpqCmcStatus,_AM:cpqCmcStatusTemp1,_AN:cpqCmcStatusTemp2,_AO:cpqCmcStatusFan1,_AP:cpqCmcStatusFan2,_AQ:cpqCmcStatusVoltage,_AR:cpqCmcStatusHumidity,_AS:cpqCmcStatusInput1,_AT:cpqCmcStatusInput2,_AU:cpqCmcStatusInput3,_AV:cpqCmcStatusInput4,_AW:cpqCmcStatusLock1Lock,_AX:cpqCmcStatusLock2Lock,_AY:cpqCmcStatusSmoke,_AZ:cpqCmcStatusShock,_Aa:cpqCmcStatusAux1,_Ab:cpqCmcStatusAux2,_Ac:cpqCmcStatusAlarm1,_Ad:cpqCmcStatusAlarm2,_Ae:cpqCmcStatusLock1Dev,_Af:cpqCmcStatusLock2Dev,'cpqCmcControl':cpqCmcControl,'cpqCmcStatusAccess':cpqCmcStatusAccess,'cpqCmcSetLock1Lock':cpqCmcSetLock1Lock,'cpqCmcSetLock1Key':cpqCmcSetLock1Key,'cpqCmcSetLock2Lock':cpqCmcSetLock2Lock,'cpqCmcSetLock2Key':cpqCmcSetLock2Key,'cpqCmcSetMessage':cpqCmcSetMessage,'cpqCmcSetAlarm1':cpqCmcSetAlarm1,'cpqCmcSetAlarm2':cpqCmcSetAlarm2,'cpqCmcSetFan1':cpqCmcSetFan1,'cpqCmcSetFan2':cpqCmcSetFan2,'cpqCmcSetQuitRelay1':cpqCmcSetQuitRelay1,'cpqCmcSetQuitRelay2':cpqCmcSetQuitRelay2,'cpqCmcLog':cpqCmcLog,'cpqCmcLogsNumber':cpqCmcLogsNumber,'cpqCmcLogTable':cpqCmcLogTable,'cpqCmcLogEntry':cpqCmcLogEntry,_AL:cpqCmcLogIndex,'cpqCmcLogDate':cpqCmcLogDate,'cpqCmcLogTime':cpqCmcLogTime,'cpqCmcLogText':cpqCmcLogText,'cpqCmcLogClass':cpqCmcLogClass})