_j='e5AlarmTime'
_i='e5AlarmText'
_h='e5AlarmServiceAffecting'
_g='e5AlarmTimeStamp'
_f='e5AlarmSeverity'
_e='sysMacAntiSpoofMAC'
_d='sysMacAntiSpoofNew'
_c='sysMacAntiSpoofOrig'
_b='unknown'
_a='e5AlarmObjectInstance8'
_Z='e5AlarmObjectInstance7'
_Y='e5AlarmObjectInstance6'
_X='e5AlarmObjectInstance5'
_W='OctetString'
_V='voipCount'
_U='voipBatType'
_T='e5AlarmType'
_S='e5AlarmObjectInstance4'
_R='e5AlarmObjectInstance3'
_Q='e5AlarmObjectInstance2'
_P='e5AlarmObjectInstance1'
_O='e5AlarmObjectClass'
_N='minor'
_M='major'
_L='critical'
_K='voipDevId'
_J='voipPhoneState'
_I='ifIndex'
_H='IF-MIB'
_G='Integer32'
_F='iesSlotId'
_E='iesChassisId'
_D='E5-111-IESCOMMON-MIB'
_C='read-only'
_B='E5-111-TRAPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_W,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iesChassisId,iesSlotId=mibBuilder.importSymbols(_D,_E,_F)
e5x111,=mibBuilder.importSymbols('E5-111-MIB','e5x111')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Trap_ObjectIdentity=ObjectIdentity
trap=_Trap_ObjectIdentity((1,3,6,1,4,1,6321,1,2,3,2,12))
_Object_ObjectIdentity=ObjectIdentity
object=_Object_ObjectIdentity((1,3,6,1,4,1,6321,1,2,3,2,12,1))
_EqptAlarmInputIndex_Type=Integer32
_EqptAlarmInputIndex_Object=MibScalar
eqptAlarmInputIndex=_EqptAlarmInputIndex_Object((1,3,6,1,4,1,6321,1,2,3,2,12,1,2),_EqptAlarmInputIndex_Type())
eqptAlarmInputIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptAlarmInputIndex.setStatus(_A)
_EqptAlarmInputName_Type=DisplayString
_EqptAlarmInputName_Object=MibScalar
eqptAlarmInputName=_EqptAlarmInputName_Object((1,3,6,1,4,1,6321,1,2,3,2,12,1,8),_EqptAlarmInputName_Type())
eqptAlarmInputName.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptAlarmInputName.setStatus(_A)
_SysMacAntiSpoofOrig_Type=Integer32
_SysMacAntiSpoofOrig_Object=MibScalar
sysMacAntiSpoofOrig=_SysMacAntiSpoofOrig_Object((1,3,6,1,4,1,6321,1,2,3,2,12,1,9),_SysMacAntiSpoofOrig_Type())
sysMacAntiSpoofOrig.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMacAntiSpoofOrig.setStatus(_A)
_SysMacAntiSpoofNew_Type=Integer32
_SysMacAntiSpoofNew_Object=MibScalar
sysMacAntiSpoofNew=_SysMacAntiSpoofNew_Object((1,3,6,1,4,1,6321,1,2,3,2,12,1,10),_SysMacAntiSpoofNew_Type())
sysMacAntiSpoofNew.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMacAntiSpoofNew.setStatus(_A)
_SysMacAntiSpoofMAC_Type=DisplayString
_SysMacAntiSpoofMAC_Object=MibScalar
sysMacAntiSpoofMAC=_SysMacAntiSpoofMAC_Object((1,3,6,1,4,1,6321,1,2,3,2,12,1,11),_SysMacAntiSpoofMAC_Type())
sysMacAntiSpoofMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMacAntiSpoofMAC.setStatus(_A)
class _SysAlarmOrigSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),('info',4)))
_SysAlarmOrigSeverity_Type.__name__=_G
_SysAlarmOrigSeverity_Object=MibScalar
sysAlarmOrigSeverity=_SysAlarmOrigSeverity_Object((1,3,6,1,4,1,6321,1,2,3,2,12,1,12),_SysAlarmOrigSeverity_Type())
sysAlarmOrigSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAlarmOrigSeverity.setStatus(_A)
class _SysAlarmNewSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),('info',4)))
_SysAlarmNewSeverity_Type.__name__=_G
_SysAlarmNewSeverity_Object=MibScalar
sysAlarmNewSeverity=_SysAlarmNewSeverity_Object((1,3,6,1,4,1,6321,1,2,3,2,12,1,13),_SysAlarmNewSeverity_Type())
sysAlarmNewSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAlarmNewSeverity.setStatus(_A)
_SysAlarmConfId_Type=Integer32
_SysAlarmConfId_Object=MibScalar
sysAlarmConfId=_SysAlarmConfId_Object((1,3,6,1,4,1,6321,1,2,3,2,12,1,14),_SysAlarmConfId_Type())
sysAlarmConfId.setMaxAccess(_C)
if mibBuilder.loadTexts:sysAlarmConfId.setStatus(_A)
class _VoipDevId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('p25-p48',0),('p1-p24',1)))
_VoipDevId_Type.__name__=_G
_VoipDevId_Object=MibScalar
voipDevId=_VoipDevId_Object((1,3,6,1,4,1,6321,1,2,3,2,12,1,51),_VoipDevId_Type())
voipDevId.setMaxAccess(_C)
if mibBuilder.loadTexts:voipDevId.setStatus(_A)
_VoipCount_Type=Integer32
_VoipCount_Object=MibScalar
voipCount=_VoipCount_Object((1,3,6,1,4,1,6321,1,2,3,2,12,1,52),_VoipCount_Type())
voipCount.setMaxAccess(_C)
if mibBuilder.loadTexts:voipCount.setStatus(_A)
class _VoipPhoneState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('disable',1),('onHook',2),('offHook',3),('ringing',4),('powerCutDown',5),('testing',6),('fault',7),('bad',8),('uninitialized',9)))
_VoipPhoneState_Type.__name__=_G
_VoipPhoneState_Object=MibScalar
voipPhoneState=_VoipPhoneState_Object((1,3,6,1,4,1,6321,1,2,3,2,12,1,53),_VoipPhoneState_Type())
voipPhoneState.setMaxAccess(_C)
if mibBuilder.loadTexts:voipPhoneState.setStatus(_A)
class _VoipBatType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('batteryLow',0),('batteryHigh',1)))
_VoipBatType_Type.__name__=_G
_VoipBatType_Object=MibScalar
voipBatType=_VoipBatType_Object((1,3,6,1,4,1,6321,1,2,3,2,12,1,54),_VoipBatType_Type())
voipBatType.setMaxAccess(_C)
if mibBuilder.loadTexts:voipBatType.setStatus(_A)
_Equipment_ObjectIdentity=ObjectIdentity
equipment=_Equipment_ObjectIdentity((1,3,6,1,4,1,6321,1,2,3,2,12,3))
_Systrap_ObjectIdentity=ObjectIdentity
systrap=_Systrap_ObjectIdentity((1,3,6,1,4,1,6321,1,2,3,2,12,4))
_Voiptrap_ObjectIdentity=ObjectIdentity
voiptrap=_Voiptrap_ObjectIdentity((1,3,6,1,4,1,6321,1,2,3,2,12,7))
_Interface_ObjectIdentity=ObjectIdentity
interface=_Interface_ObjectIdentity((1,3,6,1,4,1,6321,1,2,3,2,12,8))
_E5Alarm_ObjectIdentity=ObjectIdentity
e5Alarm=_E5Alarm_ObjectIdentity((1,3,6,1,4,1,6321,1,2,3,2,12,9))
_E5AlarmTable_Object=MibTable
e5AlarmTable=_E5AlarmTable_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1))
if mibBuilder.loadTexts:e5AlarmTable.setStatus(_A)
_E5AlarmEntry_Object=MibTableRow
e5AlarmEntry=_E5AlarmEntry_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1))
e5AlarmEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q),(0,_B,_R),(0,_B,_S),(0,_B,_X),(0,_B,_Y),(0,_B,_Z),(0,_B,_a),(0,_B,_T))
if mibBuilder.loadTexts:e5AlarmEntry.setStatus(_A)
class _E5AlarmObjectClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('dsl',1),('eqpt',2),('sys',3),('enet',4),('vop',5),('intf',6),(_b,7)))
_E5AlarmObjectClass_Type.__name__=_G
_E5AlarmObjectClass_Object=MibTableColumn
e5AlarmObjectClass=_E5AlarmObjectClass_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,1),_E5AlarmObjectClass_Type())
e5AlarmObjectClass.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmObjectClass.setStatus(_A)
_E5AlarmObjectInstance1_Type=Integer32
_E5AlarmObjectInstance1_Object=MibTableColumn
e5AlarmObjectInstance1=_E5AlarmObjectInstance1_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,2),_E5AlarmObjectInstance1_Type())
e5AlarmObjectInstance1.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmObjectInstance1.setStatus(_A)
_E5AlarmObjectInstance2_Type=Integer32
_E5AlarmObjectInstance2_Object=MibTableColumn
e5AlarmObjectInstance2=_E5AlarmObjectInstance2_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,3),_E5AlarmObjectInstance2_Type())
e5AlarmObjectInstance2.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmObjectInstance2.setStatus(_A)
_E5AlarmObjectInstance3_Type=Integer32
_E5AlarmObjectInstance3_Object=MibTableColumn
e5AlarmObjectInstance3=_E5AlarmObjectInstance3_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,4),_E5AlarmObjectInstance3_Type())
e5AlarmObjectInstance3.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmObjectInstance3.setStatus(_A)
_E5AlarmObjectInstance4_Type=Integer32
_E5AlarmObjectInstance4_Object=MibTableColumn
e5AlarmObjectInstance4=_E5AlarmObjectInstance4_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,5),_E5AlarmObjectInstance4_Type())
e5AlarmObjectInstance4.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmObjectInstance4.setStatus(_A)
_E5AlarmObjectInstance5_Type=Integer32
_E5AlarmObjectInstance5_Object=MibTableColumn
e5AlarmObjectInstance5=_E5AlarmObjectInstance5_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,6),_E5AlarmObjectInstance5_Type())
e5AlarmObjectInstance5.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmObjectInstance5.setStatus(_A)
_E5AlarmObjectInstance6_Type=Integer32
_E5AlarmObjectInstance6_Object=MibTableColumn
e5AlarmObjectInstance6=_E5AlarmObjectInstance6_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,7),_E5AlarmObjectInstance6_Type())
e5AlarmObjectInstance6.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmObjectInstance6.setStatus(_A)
_E5AlarmObjectInstance7_Type=Integer32
_E5AlarmObjectInstance7_Object=MibTableColumn
e5AlarmObjectInstance7=_E5AlarmObjectInstance7_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,8),_E5AlarmObjectInstance7_Type())
e5AlarmObjectInstance7.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmObjectInstance7.setStatus(_A)
_E5AlarmObjectInstance8_Type=Integer32
_E5AlarmObjectInstance8_Object=MibTableColumn
e5AlarmObjectInstance8=_E5AlarmObjectInstance8_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,9),_E5AlarmObjectInstance8_Type())
e5AlarmObjectInstance8.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmObjectInstance8.setStatus(_A)
_E5AlarmType_Type=Integer32
_E5AlarmType_Object=MibTableColumn
e5AlarmType=_E5AlarmType_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,10),_E5AlarmType_Type())
e5AlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmType.setStatus(_A)
class _E5AlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('clear',0),(_L,1),(_M,2),(_N,3),('warning',4),(_b,5)))
_E5AlarmSeverity_Type.__name__=_G
_E5AlarmSeverity_Object=MibTableColumn
e5AlarmSeverity=_E5AlarmSeverity_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,11),_E5AlarmSeverity_Type())
e5AlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmSeverity.setStatus(_A)
class _E5AlarmTimeStamp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_E5AlarmTimeStamp_Type.__name__=_W
_E5AlarmTimeStamp_Object=MibTableColumn
e5AlarmTimeStamp=_E5AlarmTimeStamp_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,12),_E5AlarmTimeStamp_Type())
e5AlarmTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmTimeStamp.setStatus(_A)
class _E5AlarmServiceAffecting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_E5AlarmServiceAffecting_Type.__name__=_G
_E5AlarmServiceAffecting_Object=MibTableColumn
e5AlarmServiceAffecting=_E5AlarmServiceAffecting_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,13),_E5AlarmServiceAffecting_Type())
e5AlarmServiceAffecting.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmServiceAffecting.setStatus(_A)
class _E5AlarmLocationInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('nearEnd',1))
_E5AlarmLocationInfo_Type.__name__=_G
_E5AlarmLocationInfo_Object=MibTableColumn
e5AlarmLocationInfo=_E5AlarmLocationInfo_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,14),_E5AlarmLocationInfo_Type())
e5AlarmLocationInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmLocationInfo.setStatus(_A)
_E5AlarmText_Type=OctetString
_E5AlarmText_Object=MibTableColumn
e5AlarmText=_E5AlarmText_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,15),_E5AlarmText_Type())
e5AlarmText.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmText.setStatus(_A)
_E5AlarmTime_Type=Integer32
_E5AlarmTime_Object=MibTableColumn
e5AlarmTime=_E5AlarmTime_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,16),_E5AlarmTime_Type())
e5AlarmTime.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmTime.setStatus(_A)
_E5AlarmCliObject_Type=OctetString
_E5AlarmCliObject_Object=MibTableColumn
e5AlarmCliObject=_E5AlarmCliObject_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,17),_E5AlarmCliObject_Type())
e5AlarmCliObject.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmCliObject.setStatus(_A)
_E5AlarmSecObjectClass_Type=Integer32
_E5AlarmSecObjectClass_Object=MibTableColumn
e5AlarmSecObjectClass=_E5AlarmSecObjectClass_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,18),_E5AlarmSecObjectClass_Type())
e5AlarmSecObjectClass.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmSecObjectClass.setStatus(_A)
_E5AlarmSecObjectInstance1_Type=Integer32
_E5AlarmSecObjectInstance1_Object=MibTableColumn
e5AlarmSecObjectInstance1=_E5AlarmSecObjectInstance1_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,19),_E5AlarmSecObjectInstance1_Type())
e5AlarmSecObjectInstance1.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmSecObjectInstance1.setStatus(_A)
_E5AlarmSecObjectInstance2_Type=Integer32
_E5AlarmSecObjectInstance2_Object=MibTableColumn
e5AlarmSecObjectInstance2=_E5AlarmSecObjectInstance2_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,20),_E5AlarmSecObjectInstance2_Type())
e5AlarmSecObjectInstance2.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmSecObjectInstance2.setStatus(_A)
_E5AlarmSecObjectInstance3_Type=Integer32
_E5AlarmSecObjectInstance3_Object=MibTableColumn
e5AlarmSecObjectInstance3=_E5AlarmSecObjectInstance3_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,21),_E5AlarmSecObjectInstance3_Type())
e5AlarmSecObjectInstance3.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmSecObjectInstance3.setStatus(_A)
_E5AlarmSecObjectInstance4_Type=Integer32
_E5AlarmSecObjectInstance4_Object=MibTableColumn
e5AlarmSecObjectInstance4=_E5AlarmSecObjectInstance4_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,22),_E5AlarmSecObjectInstance4_Type())
e5AlarmSecObjectInstance4.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmSecObjectInstance4.setStatus(_A)
_E5AlarmSecObjectInstance5_Type=Integer32
_E5AlarmSecObjectInstance5_Object=MibTableColumn
e5AlarmSecObjectInstance5=_E5AlarmSecObjectInstance5_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,23),_E5AlarmSecObjectInstance5_Type())
e5AlarmSecObjectInstance5.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmSecObjectInstance5.setStatus(_A)
_E5AlarmSecObjectInstance6_Type=Integer32
_E5AlarmSecObjectInstance6_Object=MibTableColumn
e5AlarmSecObjectInstance6=_E5AlarmSecObjectInstance6_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,24),_E5AlarmSecObjectInstance6_Type())
e5AlarmSecObjectInstance6.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmSecObjectInstance6.setStatus(_A)
_E5AlarmSecObjectInstance7_Type=Integer32
_E5AlarmSecObjectInstance7_Object=MibTableColumn
e5AlarmSecObjectInstance7=_E5AlarmSecObjectInstance7_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,25),_E5AlarmSecObjectInstance7_Type())
e5AlarmSecObjectInstance7.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmSecObjectInstance7.setStatus(_A)
_E5AlarmSecObjectInstance8_Type=Integer32
_E5AlarmSecObjectInstance8_Object=MibTableColumn
e5AlarmSecObjectInstance8=_E5AlarmSecObjectInstance8_Object((1,3,6,1,4,1,6321,1,2,3,2,12,9,1,1,26),_E5AlarmSecObjectInstance8_Type())
e5AlarmSecObjectInstance8.setMaxAccess(_C)
if mibBuilder.loadTexts:e5AlarmSecObjectInstance8.setStatus(_A)
eqptHWMonitorFailure=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,3,1))
if mibBuilder.loadTexts:eqptHWMonitorFailure.setStatus(_A)
sysMacAntiSpoofing=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,4,1))
sysMacAntiSpoofing.setObjects(*((_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:sysMacAntiSpoofing.setStatus(_A)
sysAlarmCutoffEnable=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,4,2))
if mibBuilder.loadTexts:sysAlarmCutoffEnable.setStatus(_A)
sysAlarmClearEnable=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,4,3))
if mibBuilder.loadTexts:sysAlarmClearEnable.setStatus(_A)
sysLoginFailure=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,4,4))
if mibBuilder.loadTexts:sysLoginFailure.setStatus(_A)
sysAlarmSvrtyChange=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,4,5))
if mibBuilder.loadTexts:sysAlarmSvrtyChange.setStatus(_A)
voipBatteryFail=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,7,1))
voipBatteryFail.setObjects(*((_D,_E),(_D,_F),(_B,_K),(_B,_U)))
if mibBuilder.loadTexts:voipBatteryFail.setStatus(_A)
voipBatteryClear=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,7,2))
voipBatteryClear.setObjects(*((_D,_E),(_D,_F),(_B,_K),(_B,_U)))
if mibBuilder.loadTexts:voipBatteryClear.setStatus(_A)
voipClockFail=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,7,3))
voipClockFail.setObjects(*((_D,_E),(_D,_F),(_B,_K)))
if mibBuilder.loadTexts:voipClockFail.setStatus(_A)
voipClockClear=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,7,4))
voipClockClear.setObjects(*((_D,_E),(_D,_F),(_B,_K)))
if mibBuilder.loadTexts:voipClockClear.setStatus(_A)
voipRingerFault=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,7,5))
voipRingerFault.setObjects(*((_D,_E),(_D,_F),(_B,_V)))
if mibBuilder.loadTexts:voipRingerFault.setStatus(_A)
voipRingerClear=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,7,6))
voipRingerClear.setObjects(*((_D,_E),(_D,_F),(_B,_V)))
if mibBuilder.loadTexts:voipRingerClear.setStatus(_A)
voipTempError=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,7,7))
voipTempError.setObjects(*((_D,_E),(_D,_F),(_H,_I),(_B,_J)))
if mibBuilder.loadTexts:voipTempError.setStatus(_A)
voipTempClear=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,7,8))
voipTempClear.setObjects(*((_D,_E),(_D,_F),(_H,_I),(_B,_J)))
if mibBuilder.loadTexts:voipTempClear.setStatus(_A)
voipDcPowerFail=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,7,9))
voipDcPowerFail.setObjects(*((_D,_E),(_D,_F),(_H,_I),(_B,_J)))
if mibBuilder.loadTexts:voipDcPowerFail.setStatus(_A)
voipDcPowerClear=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,7,10))
voipDcPowerClear.setObjects(*((_D,_E),(_D,_F),(_H,_I),(_B,_J)))
if mibBuilder.loadTexts:voipDcPowerClear.setStatus(_A)
voipAcPowerFail=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,7,11))
voipAcPowerFail.setObjects(*((_D,_E),(_D,_F),(_H,_I),(_B,_J)))
if mibBuilder.loadTexts:voipAcPowerFail.setStatus(_A)
voipAcPowerClear=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,7,12))
voipAcPowerClear.setObjects(*((_D,_E),(_D,_F),(_H,_I),(_B,_J)))
if mibBuilder.loadTexts:voipAcPowerClear.setStatus(_A)
e5AlarmNotify=NotificationType((1,3,6,1,4,1,6321,1,2,3,2,12,9,2))
e5AlarmNotify.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:e5AlarmNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'trap':trap,'object':object,'eqptAlarmInputIndex':eqptAlarmInputIndex,'eqptAlarmInputName':eqptAlarmInputName,_c:sysMacAntiSpoofOrig,_d:sysMacAntiSpoofNew,_e:sysMacAntiSpoofMAC,'sysAlarmOrigSeverity':sysAlarmOrigSeverity,'sysAlarmNewSeverity':sysAlarmNewSeverity,'sysAlarmConfId':sysAlarmConfId,_K:voipDevId,_V:voipCount,_J:voipPhoneState,_U:voipBatType,'equipment':equipment,'eqptHWMonitorFailure':eqptHWMonitorFailure,'systrap':systrap,'sysMacAntiSpoofing':sysMacAntiSpoofing,'sysAlarmCutoffEnable':sysAlarmCutoffEnable,'sysAlarmClearEnable':sysAlarmClearEnable,'sysLoginFailure':sysLoginFailure,'sysAlarmSvrtyChange':sysAlarmSvrtyChange,'voiptrap':voiptrap,'voipBatteryFail':voipBatteryFail,'voipBatteryClear':voipBatteryClear,'voipClockFail':voipClockFail,'voipClockClear':voipClockClear,'voipRingerFault':voipRingerFault,'voipRingerClear':voipRingerClear,'voipTempError':voipTempError,'voipTempClear':voipTempClear,'voipDcPowerFail':voipDcPowerFail,'voipDcPowerClear':voipDcPowerClear,'voipAcPowerFail':voipAcPowerFail,'voipAcPowerClear':voipAcPowerClear,'interface':interface,'e5Alarm':e5Alarm,'e5AlarmTable':e5AlarmTable,'e5AlarmEntry':e5AlarmEntry,_O:e5AlarmObjectClass,_P:e5AlarmObjectInstance1,_Q:e5AlarmObjectInstance2,_R:e5AlarmObjectInstance3,_S:e5AlarmObjectInstance4,_X:e5AlarmObjectInstance5,_Y:e5AlarmObjectInstance6,_Z:e5AlarmObjectInstance7,_a:e5AlarmObjectInstance8,_T:e5AlarmType,_f:e5AlarmSeverity,_g:e5AlarmTimeStamp,_h:e5AlarmServiceAffecting,'e5AlarmLocationInfo':e5AlarmLocationInfo,_i:e5AlarmText,_j:e5AlarmTime,'e5AlarmCliObject':e5AlarmCliObject,'e5AlarmSecObjectClass':e5AlarmSecObjectClass,'e5AlarmSecObjectInstance1':e5AlarmSecObjectInstance1,'e5AlarmSecObjectInstance2':e5AlarmSecObjectInstance2,'e5AlarmSecObjectInstance3':e5AlarmSecObjectInstance3,'e5AlarmSecObjectInstance4':e5AlarmSecObjectInstance4,'e5AlarmSecObjectInstance5':e5AlarmSecObjectInstance5,'e5AlarmSecObjectInstance6':e5AlarmSecObjectInstance6,'e5AlarmSecObjectInstance7':e5AlarmSecObjectInstance7,'e5AlarmSecObjectInstance8':e5AlarmSecObjectInstance8,'e5AlarmNotify':e5AlarmNotify})