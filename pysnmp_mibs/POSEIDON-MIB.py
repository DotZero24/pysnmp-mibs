_Z='sensUnit'
_Y='sensValue'
_X='sensState'
_W='sensID'
_V='sensName'
_U='inpAlarmState'
_T='inpValue'
_S='inpName'
_R='sensSetupIndex'
_Q='tsAlarmIdx'
_P='sensIndex'
_O='outIndex'
_N='inpIndex'
_M='normal'
_L='DisplayString'
_K='Integer32'
_J='tsAlarmDescr'
_I='tsAlarmId'
_H='infoAddressMAC'
_G='not-accessible'
_F='sysName'
_E='SNMPv2-MIB'
_D='read-write'
_C='read-only'
_B='POSEIDON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_E,_F)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention')
class PositiveInteger(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class OnOff(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
class OutputType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('onOff',0),('rts',1),('dtr',2)))
class OutputMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('manual',0),('autoAlarm',1),('autoTriggerEq',2),('autoTriggerHi',3),('autoTriggerLo',4)))
class UnitType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('celsius',0),('fahrenheit',1),('kelvin',2),('percent',3),('volt',4),('miliAmper',5),('noUnit',6),('pulse',7),('switch',8),('dewPoint',9),('absoluteHumidity',10),('pressure',11),('universal',12)))
class InputAlarmSetup(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('inactive',0),('activeOff',1),('activeOn',2)))
class InputAlarmState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),('alarm',1)))
class SensorState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('invalid',0),(_M,1),('alarmstate',2),('alarm',3)))
class SensorID(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class IOName(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
class SensorName(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
class SensorValue(Integer32):0
class SensorString(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
class SensorUnitString(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
class SensorFlags(Integer32):0
class TimeStamp(TimeTicks):0
_Hwgroup_ObjectIdentity=ObjectIdentity
hwgroup=_Hwgroup_ObjectIdentity((1,3,6,1,4,1,21796))
_CharonII_ObjectIdentity=ObjectIdentity
charonII=_CharonII_ObjectIdentity((1,3,6,1,4,1,21796,3))
_Poseidon_ObjectIdentity=ObjectIdentity
poseidon=_Poseidon_ObjectIdentity((1,3,6,1,4,1,21796,3,3))
_InpTable_Object=MibTable
inpTable=_InpTable_Object((1,3,6,1,4,1,21796,3,3,1))
if mibBuilder.loadTexts:inpTable.setStatus(_A)
_InpEntry_Object=MibTableRow
inpEntry=_InpEntry_Object((1,3,6,1,4,1,21796,3,3,1,1))
inpEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:inpEntry.setStatus(_A)
_InpIndex_Type=PositiveInteger
_InpIndex_Object=MibTableColumn
inpIndex=_InpIndex_Object((1,3,6,1,4,1,21796,3,3,1,1,1),_InpIndex_Type())
inpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:inpIndex.setStatus(_A)
_InpValue_Type=OnOff
_InpValue_Object=MibTableColumn
inpValue=_InpValue_Object((1,3,6,1,4,1,21796,3,3,1,1,2),_InpValue_Type())
inpValue.setMaxAccess(_C)
if mibBuilder.loadTexts:inpValue.setStatus(_A)
_InpName_Type=IOName
_InpName_Object=MibTableColumn
inpName=_InpName_Object((1,3,6,1,4,1,21796,3,3,1,1,3),_InpName_Type())
inpName.setMaxAccess(_D)
if mibBuilder.loadTexts:inpName.setStatus(_A)
_InpAlarmSetup_Type=InputAlarmSetup
_InpAlarmSetup_Object=MibTableColumn
inpAlarmSetup=_InpAlarmSetup_Object((1,3,6,1,4,1,21796,3,3,1,1,4),_InpAlarmSetup_Type())
inpAlarmSetup.setMaxAccess(_D)
if mibBuilder.loadTexts:inpAlarmSetup.setStatus(_A)
_InpAlarmState_Type=InputAlarmState
_InpAlarmState_Object=MibTableColumn
inpAlarmState=_InpAlarmState_Object((1,3,6,1,4,1,21796,3,3,1,1,5),_InpAlarmState_Type())
inpAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:inpAlarmState.setStatus(_A)
_OutTable_Object=MibTable
outTable=_OutTable_Object((1,3,6,1,4,1,21796,3,3,2))
if mibBuilder.loadTexts:outTable.setStatus(_A)
_OutEntry_Object=MibTableRow
outEntry=_OutEntry_Object((1,3,6,1,4,1,21796,3,3,2,1))
outEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:outEntry.setStatus(_A)
_OutIndex_Type=PositiveInteger
_OutIndex_Object=MibTableColumn
outIndex=_OutIndex_Object((1,3,6,1,4,1,21796,3,3,2,1,1),_OutIndex_Type())
outIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:outIndex.setStatus(_A)
_OutValue_Type=OnOff
_OutValue_Object=MibTableColumn
outValue=_OutValue_Object((1,3,6,1,4,1,21796,3,3,2,1,2),_OutValue_Type())
outValue.setMaxAccess(_D)
if mibBuilder.loadTexts:outValue.setStatus(_A)
_OutName_Type=IOName
_OutName_Object=MibTableColumn
outName=_OutName_Object((1,3,6,1,4,1,21796,3,3,2,1,3),_OutName_Type())
outName.setMaxAccess(_D)
if mibBuilder.loadTexts:outName.setStatus(_A)
_OutType_Type=OutputType
_OutType_Object=MibTableColumn
outType=_OutType_Object((1,3,6,1,4,1,21796,3,3,2,1,4),_OutType_Type())
outType.setMaxAccess(_C)
if mibBuilder.loadTexts:outType.setStatus(_A)
_OutMode_Type=OutputMode
_OutMode_Object=MibTableColumn
outMode=_OutMode_Object((1,3,6,1,4,1,21796,3,3,2,1,5),_OutMode_Type())
outMode.setMaxAccess(_D)
if mibBuilder.loadTexts:outMode.setStatus(_A)
_SensTable_Object=MibTable
sensTable=_SensTable_Object((1,3,6,1,4,1,21796,3,3,3))
if mibBuilder.loadTexts:sensTable.setStatus(_A)
_SensEntry_Object=MibTableRow
sensEntry=_SensEntry_Object((1,3,6,1,4,1,21796,3,3,3,1))
sensEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:sensEntry.setStatus(_A)
_SensIndex_Type=PositiveInteger
_SensIndex_Object=MibTableColumn
sensIndex=_SensIndex_Object((1,3,6,1,4,1,21796,3,3,3,1,1),_SensIndex_Type())
sensIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:sensIndex.setStatus(_A)
_SensName_Type=SensorName
_SensName_Object=MibTableColumn
sensName=_SensName_Object((1,3,6,1,4,1,21796,3,3,3,1,2),_SensName_Type())
sensName.setMaxAccess(_C)
if mibBuilder.loadTexts:sensName.setStatus(_A)
_SensState_Type=SensorState
_SensState_Object=MibTableColumn
sensState=_SensState_Object((1,3,6,1,4,1,21796,3,3,3,1,4),_SensState_Type())
sensState.setMaxAccess(_C)
if mibBuilder.loadTexts:sensState.setStatus(_A)
_SensString_Type=SensorString
_SensString_Object=MibTableColumn
sensString=_SensString_Object((1,3,6,1,4,1,21796,3,3,3,1,5),_SensString_Type())
sensString.setMaxAccess(_C)
if mibBuilder.loadTexts:sensString.setStatus(_A)
_SensValue_Type=SensorValue
_SensValue_Object=MibTableColumn
sensValue=_SensValue_Object((1,3,6,1,4,1,21796,3,3,3,1,6),_SensValue_Type())
sensValue.setMaxAccess(_C)
if mibBuilder.loadTexts:sensValue.setStatus(_A)
_SensValueRaw_Type=SensorValue
_SensValueRaw_Object=MibTableColumn
sensValueRaw=_SensValueRaw_Object((1,3,6,1,4,1,21796,3,3,3,1,7),_SensValueRaw_Type())
sensValueRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:sensValueRaw.setStatus(_A)
_SensID_Type=SensorID
_SensID_Object=MibTableColumn
sensID=_SensID_Object((1,3,6,1,4,1,21796,3,3,3,1,8),_SensID_Type())
sensID.setMaxAccess(_C)
if mibBuilder.loadTexts:sensID.setStatus(_A)
_SensUnit_Type=UnitType
_SensUnit_Object=MibTableColumn
sensUnit=_SensUnit_Object((1,3,6,1,4,1,21796,3,3,3,1,9),_SensUnit_Type())
sensUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:sensUnit.setStatus(_A)
_SensUnitString_Type=SensorUnitString
_SensUnitString_Object=MibTableColumn
sensUnitString=_SensUnitString_Object((1,3,6,1,4,1,21796,3,3,3,1,10),_SensUnitString_Type())
sensUnitString.setMaxAccess(_C)
if mibBuilder.loadTexts:sensUnitString.setStatus(_A)
_SensPortID_Type=Integer32
_SensPortID_Object=MibTableColumn
sensPortID=_SensPortID_Object((1,3,6,1,4,1,21796,3,3,3,1,11),_SensPortID_Type())
sensPortID.setMaxAccess(_C)
if mibBuilder.loadTexts:sensPortID.setStatus(_A)
_TsAlarm_ObjectIdentity=ObjectIdentity
tsAlarm=_TsAlarm_ObjectIdentity((1,3,6,1,4,1,21796,3,3,50))
_TsAlarmsPresent_Type=Gauge32
_TsAlarmsPresent_Object=MibScalar
tsAlarmsPresent=_TsAlarmsPresent_Object((1,3,6,1,4,1,21796,3,3,50,1),_TsAlarmsPresent_Type())
tsAlarmsPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:tsAlarmsPresent.setStatus(_A)
_TsAlarmTable_Object=MibTable
tsAlarmTable=_TsAlarmTable_Object((1,3,6,1,4,1,21796,3,3,50,2))
if mibBuilder.loadTexts:tsAlarmTable.setStatus(_A)
_TsAlarmEntry_Object=MibTableRow
tsAlarmEntry=_TsAlarmEntry_Object((1,3,6,1,4,1,21796,3,3,50,2,1))
tsAlarmEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:tsAlarmEntry.setStatus(_A)
_TsAlarmIdx_Type=PositiveInteger
_TsAlarmIdx_Object=MibTableColumn
tsAlarmIdx=_TsAlarmIdx_Object((1,3,6,1,4,1,21796,3,3,50,2,1,1),_TsAlarmIdx_Type())
tsAlarmIdx.setMaxAccess(_G)
if mibBuilder.loadTexts:tsAlarmIdx.setStatus(_A)
_TsAlarmId_Type=PositiveInteger
_TsAlarmId_Object=MibTableColumn
tsAlarmId=_TsAlarmId_Object((1,3,6,1,4,1,21796,3,3,50,2,1,2),_TsAlarmId_Type())
tsAlarmId.setMaxAccess(_C)
if mibBuilder.loadTexts:tsAlarmId.setStatus(_A)
class _TsAlarmDescr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inputStateAlarm',1),('temperatureOutOfRange',2)))
_TsAlarmDescr_Type.__name__=_K
_TsAlarmDescr_Object=MibTableColumn
tsAlarmDescr=_TsAlarmDescr_Object((1,3,6,1,4,1,21796,3,3,50,2,1,3),_TsAlarmDescr_Type())
tsAlarmDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:tsAlarmDescr.setStatus(_A)
_TsAlarmSensName_Type=SensorName
_TsAlarmSensName_Object=MibTableColumn
tsAlarmSensName=_TsAlarmSensName_Object((1,3,6,1,4,1,21796,3,3,50,2,1,4),_TsAlarmSensName_Type())
tsAlarmSensName.setMaxAccess(_C)
if mibBuilder.loadTexts:tsAlarmSensName.setStatus(_A)
_TsAlarmTime_Type=TimeStamp
_TsAlarmTime_Object=MibTableColumn
tsAlarmTime=_TsAlarmTime_Object((1,3,6,1,4,1,21796,3,3,50,2,1,5),_TsAlarmTime_Type())
tsAlarmTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tsAlarmTime.setStatus(_A)
_Info_ObjectIdentity=ObjectIdentity
info=_Info_ObjectIdentity((1,3,6,1,4,1,21796,3,3,70))
class _InfoAddressMAC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_InfoAddressMAC_Type.__name__=_L
_InfoAddressMAC_Object=MibScalar
infoAddressMAC=_InfoAddressMAC_Object((1,3,6,1,4,1,21796,3,3,70,1),_InfoAddressMAC_Type())
infoAddressMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:infoAddressMAC.setStatus(_A)
_Setup_ObjectIdentity=ObjectIdentity
setup=_Setup_ObjectIdentity((1,3,6,1,4,1,21796,3,3,99))
_SensSetup_ObjectIdentity=ObjectIdentity
sensSetup=_SensSetup_ObjectIdentity((1,3,6,1,4,1,21796,3,3,99,1))
_UnitType_Type=UnitType
_UnitType_Object=MibScalar
unitType=_UnitType_Object((1,3,6,1,4,1,21796,3,3,99,1,1),_UnitType_Type())
unitType.setMaxAccess(_D)
if mibBuilder.loadTexts:unitType.setStatus(_A)
_SensSetupTable_Object=MibTable
sensSetupTable=_SensSetupTable_Object((1,3,6,1,4,1,21796,3,3,99,1,2))
if mibBuilder.loadTexts:sensSetupTable.setStatus(_A)
_SensSetupEntry_Object=MibTableRow
sensSetupEntry=_SensSetupEntry_Object((1,3,6,1,4,1,21796,3,3,99,1,2,1))
sensSetupEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:sensSetupEntry.setStatus(_A)
_SensSetupIndex_Type=PositiveInteger
_SensSetupIndex_Object=MibTableColumn
sensSetupIndex=_SensSetupIndex_Object((1,3,6,1,4,1,21796,3,3,99,1,2,1,1),_SensSetupIndex_Type())
sensSetupIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:sensSetupIndex.setStatus(_A)
_SensSetupName_Type=SensorName
_SensSetupName_Object=MibTableColumn
sensSetupName=_SensSetupName_Object((1,3,6,1,4,1,21796,3,3,99,1,2,1,2),_SensSetupName_Type())
sensSetupName.setMaxAccess(_D)
if mibBuilder.loadTexts:sensSetupName.setStatus(_A)
_SensFlags_Type=SensorFlags
_SensFlags_Object=MibTableColumn
sensFlags=_SensFlags_Object((1,3,6,1,4,1,21796,3,3,99,1,2,1,5),_SensFlags_Type())
sensFlags.setMaxAccess(_D)
if mibBuilder.loadTexts:sensFlags.setStatus(_A)
_SensLimitMin_Type=SensorValue
_SensLimitMin_Object=MibTableColumn
sensLimitMin=_SensLimitMin_Object((1,3,6,1,4,1,21796,3,3,99,1,2,1,6),_SensLimitMin_Type())
sensLimitMin.setMaxAccess(_D)
if mibBuilder.loadTexts:sensLimitMin.setStatus(_A)
_SensLimitMax_Type=SensorValue
_SensLimitMax_Object=MibTableColumn
sensLimitMax=_SensLimitMax_Object((1,3,6,1,4,1,21796,3,3,99,1,2,1,7),_SensLimitMax_Type())
sensLimitMax.setMaxAccess(_D)
if mibBuilder.loadTexts:sensLimitMax.setStatus(_A)
_SensHysteresis_Type=SensorValue
_SensHysteresis_Object=MibTableColumn
sensHysteresis=_SensHysteresis_Object((1,3,6,1,4,1,21796,3,3,99,1,2,1,8),_SensHysteresis_Type())
sensHysteresis.setMaxAccess(_D)
if mibBuilder.loadTexts:sensHysteresis.setStatus(_A)
inpAlarmStateChanged=NotificationType((1,3,6,1,4,1,21796,3,3,0,1))
inpAlarmStateChanged.setObjects(*((_E,_F),(_B,_H),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:inpAlarmStateChanged.setStatus('')
sensAlarmStateChanged=NotificationType((1,3,6,1,4,1,21796,3,3,0,2))
sensAlarmStateChanged.setObjects(*((_E,_F),(_B,_H),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:sensAlarmStateChanged.setStatus('')
tsTrapAlarmStart=NotificationType((1,3,6,1,4,1,21796,3,3,0,3))
tsTrapAlarmStart.setObjects(*((_E,_F),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:tsTrapAlarmStart.setStatus('')
tsTrapAlarmEnd=NotificationType((1,3,6,1,4,1,21796,3,3,0,4))
tsTrapAlarmEnd.setObjects(*((_E,_F),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:tsTrapAlarmEnd.setStatus('')
mibBuilder.exportSymbols(_B,**{'PositiveInteger':PositiveInteger,'OnOff':OnOff,'OutputType':OutputType,'OutputMode':OutputMode,'UnitType':UnitType,'InputAlarmSetup':InputAlarmSetup,'InputAlarmState':InputAlarmState,'SensorState':SensorState,'SensorID':SensorID,'IOName':IOName,'SensorName':SensorName,'SensorValue':SensorValue,'SensorString':SensorString,'SensorUnitString':SensorUnitString,'SensorFlags':SensorFlags,'TimeStamp':TimeStamp,'hwgroup':hwgroup,'charonII':charonII,'poseidon':poseidon,'inpAlarmStateChanged':inpAlarmStateChanged,'sensAlarmStateChanged':sensAlarmStateChanged,'tsTrapAlarmStart':tsTrapAlarmStart,'tsTrapAlarmEnd':tsTrapAlarmEnd,'inpTable':inpTable,'inpEntry':inpEntry,_N:inpIndex,_T:inpValue,_S:inpName,'inpAlarmSetup':inpAlarmSetup,_U:inpAlarmState,'outTable':outTable,'outEntry':outEntry,_O:outIndex,'outValue':outValue,'outName':outName,'outType':outType,'outMode':outMode,'sensTable':sensTable,'sensEntry':sensEntry,_P:sensIndex,_V:sensName,_X:sensState,'sensString':sensString,_Y:sensValue,'sensValueRaw':sensValueRaw,_W:sensID,_Z:sensUnit,'sensUnitString':sensUnitString,'sensPortID':sensPortID,'tsAlarm':tsAlarm,'tsAlarmsPresent':tsAlarmsPresent,'tsAlarmTable':tsAlarmTable,'tsAlarmEntry':tsAlarmEntry,_Q:tsAlarmIdx,_I:tsAlarmId,_J:tsAlarmDescr,'tsAlarmSensName':tsAlarmSensName,'tsAlarmTime':tsAlarmTime,'info':info,_H:infoAddressMAC,'setup':setup,'sensSetup':sensSetup,'unitType':unitType,'sensSetupTable':sensSetupTable,'sensSetupEntry':sensSetupEntry,_R:sensSetupIndex,'sensSetupName':sensSetupName,'sensFlags':sensFlags,'sensLimitMin':sensLimitMin,'sensLimitMax':sensLimitMax,'sensHysteresis':sensHysteresis})