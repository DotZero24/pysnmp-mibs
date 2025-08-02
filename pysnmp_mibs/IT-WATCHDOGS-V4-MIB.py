_w='rpmSensorIndex'
_v='thdSensorIndex'
_u='t3hdSensorIndex'
_t='ccatSensorIndex'
_s='dewPointSensorIndex'
_r='airFlowSensorIndex'
_q='tempSensorIndex'
_p='internalIndex'
_o='rpmSensorPowerFactor'
_n='rpmSensorApparentPower'
_m='rpmSensorRealPower'
_l='rpmSensorCurrent'
_k='rpmSensorVoltagePeak'
_j='rpmSensorVoltageMin'
_i='rpmSensorVoltageMax'
_h='rpmSensorVoltage'
_g='rpmSensorEnergy'
_f='thdSensorDewPoint'
_e='thdSensorHumidity'
_d='thdSensorTemp'
_c='t3hdSensorExtBTemp'
_b='t3hdSensorExtATemp'
_a='t3hdSensorIntDewPoint'
_Z='t3hdSensorIntHumidity'
_Y='t3hdSensorIntTemp'
_X='ccatSensorType'
_W='ccatSensorValue'
_V='dewPointSensorDewPoint'
_U='dewPointSensorHumidity'
_T='dewPointSensorTemp'
_S='airFlowSensorDewPoint'
_R='airFlowSensorHumidity'
_Q='airFlowSensorFlow'
_P='airFlowSensorTemp'
_O='tempSensorTemp'
_N='internalIO4'
_M='internalIO3'
_L='internalIO2'
_K='internalIO1'
_J='internalDewPoint'
_I='internalHumidity'
_H='internalTemp'
_G='Volts (rms)'
_F='0.1 Degrees'
_E='temperatureUnits'
_D='Integer32'
_C='read-only'
_B='IT-WATCHDOGS-V4-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
itwatchdogs=ModuleIdentity((1,3,6,1,4,1,17373))
if mibBuilder.loadTexts:itwatchdogs.setRevisions(('2012-09-11 00:00',))
_Blackbird_ObjectIdentity=ObjectIdentity
blackbird=_Blackbird_ObjectIdentity((1,3,6,1,4,1,17373,4))
_Watchdog100_ObjectIdentity=ObjectIdentity
watchdog100=_Watchdog100_ObjectIdentity((1,3,6,1,4,1,17373,4,1))
_DeviceInfo_ObjectIdentity=ObjectIdentity
deviceInfo=_DeviceInfo_ObjectIdentity((1,3,6,1,4,1,17373,4,1,1))
_ProductTitle_Type=DisplayString
_ProductTitle_Object=MibScalar
productTitle=_ProductTitle_Object((1,3,6,1,4,1,17373,4,1,1,1),_ProductTitle_Type())
productTitle.setMaxAccess(_C)
if mibBuilder.loadTexts:productTitle.setStatus(_A)
_ProductVersion_Type=DisplayString
_ProductVersion_Object=MibScalar
productVersion=_ProductVersion_Object((1,3,6,1,4,1,17373,4,1,1,2),_ProductVersion_Type())
productVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:productVersion.setStatus(_A)
_ProductFriendlyName_Type=DisplayString
_ProductFriendlyName_Object=MibScalar
productFriendlyName=_ProductFriendlyName_Object((1,3,6,1,4,1,17373,4,1,1,3),_ProductFriendlyName_Type())
productFriendlyName.setMaxAccess(_C)
if mibBuilder.loadTexts:productFriendlyName.setStatus(_A)
_ProductMacAddress_Type=OctetString
_ProductMacAddress_Object=MibScalar
productMacAddress=_ProductMacAddress_Object((1,3,6,1,4,1,17373,4,1,1,4),_ProductMacAddress_Type())
productMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:productMacAddress.setStatus(_A)
_ProductUrl_Type=IpAddress
_ProductUrl_Object=MibScalar
productUrl=_ProductUrl_Object((1,3,6,1,4,1,17373,4,1,1,5),_ProductUrl_Type())
productUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:productUrl.setStatus(_A)
class _DeviceCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DeviceCount_Type.__name__=_D
_DeviceCount_Object=MibScalar
deviceCount=_DeviceCount_Object((1,3,6,1,4,1,17373,4,1,1,6),_DeviceCount_Type())
deviceCount.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceCount.setStatus(_A)
class _TemperatureUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_TemperatureUnits_Type.__name__=_D
_TemperatureUnits_Object=MibScalar
temperatureUnits=_TemperatureUnits_Object((1,3,6,1,4,1,17373,4,1,1,7),_TemperatureUnits_Type())
temperatureUnits.setMaxAccess('read-write')
if mibBuilder.loadTexts:temperatureUnits.setStatus(_A)
_InternalTable_Object=MibTable
internalTable=_InternalTable_Object((1,3,6,1,4,1,17373,4,1,2))
if mibBuilder.loadTexts:internalTable.setStatus(_A)
_InternalEntry_Object=MibTableRow
internalEntry=_InternalEntry_Object((1,3,6,1,4,1,17373,4,1,2,1))
internalEntry.setIndexNames((0,_B,_p))
if mibBuilder.loadTexts:internalEntry.setStatus(_A)
class _InternalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_InternalIndex_Type.__name__=_D
_InternalIndex_Object=MibTableColumn
internalIndex=_InternalIndex_Object((1,3,6,1,4,1,17373,4,1,2,1,1),_InternalIndex_Type())
internalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:internalIndex.setStatus(_A)
_InternalSerial_Type=DisplayString
_InternalSerial_Object=MibTableColumn
internalSerial=_InternalSerial_Object((1,3,6,1,4,1,17373,4,1,2,1,2),_InternalSerial_Type())
internalSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:internalSerial.setStatus(_A)
_InternalName_Type=DisplayString
_InternalName_Object=MibTableColumn
internalName=_InternalName_Object((1,3,6,1,4,1,17373,4,1,2,1,3),_InternalName_Type())
internalName.setMaxAccess(_C)
if mibBuilder.loadTexts:internalName.setStatus(_A)
_InternalAvail_Type=Gauge32
_InternalAvail_Object=MibTableColumn
internalAvail=_InternalAvail_Object((1,3,6,1,4,1,17373,4,1,2,1,4),_InternalAvail_Type())
internalAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:internalAvail.setStatus(_A)
class _InternalTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,200))
_InternalTemp_Type.__name__=_D
_InternalTemp_Object=MibTableColumn
internalTemp=_InternalTemp_Object((1,3,6,1,4,1,17373,4,1,2,1,5),_InternalTemp_Type())
internalTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:internalTemp.setStatus(_A)
if mibBuilder.loadTexts:internalTemp.setUnits(_F)
class _InternalHumidity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_InternalHumidity_Type.__name__=_D
_InternalHumidity_Object=MibTableColumn
internalHumidity=_InternalHumidity_Object((1,3,6,1,4,1,17373,4,1,2,1,6),_InternalHumidity_Type())
internalHumidity.setMaxAccess(_C)
if mibBuilder.loadTexts:internalHumidity.setStatus(_A)
if mibBuilder.loadTexts:internalHumidity.setUnits('%')
class _InternalDewPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,200))
_InternalDewPoint_Type.__name__=_D
_InternalDewPoint_Object=MibTableColumn
internalDewPoint=_InternalDewPoint_Object((1,3,6,1,4,1,17373,4,1,2,1,7),_InternalDewPoint_Type())
internalDewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:internalDewPoint.setStatus(_A)
if mibBuilder.loadTexts:internalDewPoint.setUnits(_F)
class _InternalIO1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_InternalIO1_Type.__name__=_D
_InternalIO1_Object=MibTableColumn
internalIO1=_InternalIO1_Object((1,3,6,1,4,1,17373,4,1,2,1,8),_InternalIO1_Type())
internalIO1.setMaxAccess(_C)
if mibBuilder.loadTexts:internalIO1.setStatus(_A)
class _InternalIO2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_InternalIO2_Type.__name__=_D
_InternalIO2_Object=MibTableColumn
internalIO2=_InternalIO2_Object((1,3,6,1,4,1,17373,4,1,2,1,9),_InternalIO2_Type())
internalIO2.setMaxAccess(_C)
if mibBuilder.loadTexts:internalIO2.setStatus(_A)
class _InternalIO3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_InternalIO3_Type.__name__=_D
_InternalIO3_Object=MibTableColumn
internalIO3=_InternalIO3_Object((1,3,6,1,4,1,17373,4,1,2,1,10),_InternalIO3_Type())
internalIO3.setMaxAccess(_C)
if mibBuilder.loadTexts:internalIO3.setStatus(_A)
class _InternalIO4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_InternalIO4_Type.__name__=_D
_InternalIO4_Object=MibTableColumn
internalIO4=_InternalIO4_Object((1,3,6,1,4,1,17373,4,1,2,1,11),_InternalIO4_Type())
internalIO4.setMaxAccess(_C)
if mibBuilder.loadTexts:internalIO4.setStatus(_A)
_InternalRelayState_Type=Gauge32
_InternalRelayState_Object=MibTableColumn
internalRelayState=_InternalRelayState_Object((1,3,6,1,4,1,17373,4,1,2,1,12),_InternalRelayState_Type())
internalRelayState.setMaxAccess(_C)
if mibBuilder.loadTexts:internalRelayState.setStatus(_A)
_TempSensorTable_Object=MibTable
tempSensorTable=_TempSensorTable_Object((1,3,6,1,4,1,17373,4,1,4))
if mibBuilder.loadTexts:tempSensorTable.setStatus(_A)
_TempSensorEntry_Object=MibTableRow
tempSensorEntry=_TempSensorEntry_Object((1,3,6,1,4,1,17373,4,1,4,1))
tempSensorEntry.setIndexNames((0,_B,_q))
if mibBuilder.loadTexts:tempSensorEntry.setStatus(_A)
class _TempSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_TempSensorIndex_Type.__name__=_D
_TempSensorIndex_Object=MibTableColumn
tempSensorIndex=_TempSensorIndex_Object((1,3,6,1,4,1,17373,4,1,4,1,1),_TempSensorIndex_Type())
tempSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tempSensorIndex.setStatus(_A)
_TempSensorSerial_Type=DisplayString
_TempSensorSerial_Object=MibTableColumn
tempSensorSerial=_TempSensorSerial_Object((1,3,6,1,4,1,17373,4,1,4,1,2),_TempSensorSerial_Type())
tempSensorSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:tempSensorSerial.setStatus(_A)
_TempSensorName_Type=DisplayString
_TempSensorName_Object=MibTableColumn
tempSensorName=_TempSensorName_Object((1,3,6,1,4,1,17373,4,1,4,1,3),_TempSensorName_Type())
tempSensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:tempSensorName.setStatus(_A)
_TempSensorAvail_Type=Gauge32
_TempSensorAvail_Object=MibTableColumn
tempSensorAvail=_TempSensorAvail_Object((1,3,6,1,4,1,17373,4,1,4,1,4),_TempSensorAvail_Type())
tempSensorAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:tempSensorAvail.setStatus(_A)
class _TempSensorTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,200))
_TempSensorTemp_Type.__name__=_D
_TempSensorTemp_Object=MibTableColumn
tempSensorTemp=_TempSensorTemp_Object((1,3,6,1,4,1,17373,4,1,4,1,5),_TempSensorTemp_Type())
tempSensorTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:tempSensorTemp.setStatus(_A)
if mibBuilder.loadTexts:tempSensorTemp.setUnits(_F)
_AirFlowSensorTable_Object=MibTable
airFlowSensorTable=_AirFlowSensorTable_Object((1,3,6,1,4,1,17373,4,1,5))
if mibBuilder.loadTexts:airFlowSensorTable.setStatus(_A)
_AirFlowSensorEntry_Object=MibTableRow
airFlowSensorEntry=_AirFlowSensorEntry_Object((1,3,6,1,4,1,17373,4,1,5,1))
airFlowSensorEntry.setIndexNames((0,_B,_r))
if mibBuilder.loadTexts:airFlowSensorEntry.setStatus(_A)
class _AirFlowSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AirFlowSensorIndex_Type.__name__=_D
_AirFlowSensorIndex_Object=MibTableColumn
airFlowSensorIndex=_AirFlowSensorIndex_Object((1,3,6,1,4,1,17373,4,1,5,1,1),_AirFlowSensorIndex_Type())
airFlowSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:airFlowSensorIndex.setStatus(_A)
_AirFlowSensorSerial_Type=DisplayString
_AirFlowSensorSerial_Object=MibTableColumn
airFlowSensorSerial=_AirFlowSensorSerial_Object((1,3,6,1,4,1,17373,4,1,5,1,2),_AirFlowSensorSerial_Type())
airFlowSensorSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:airFlowSensorSerial.setStatus(_A)
_AirFlowSensorName_Type=DisplayString
_AirFlowSensorName_Object=MibTableColumn
airFlowSensorName=_AirFlowSensorName_Object((1,3,6,1,4,1,17373,4,1,5,1,3),_AirFlowSensorName_Type())
airFlowSensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:airFlowSensorName.setStatus(_A)
_AirFlowSensorAvail_Type=Gauge32
_AirFlowSensorAvail_Object=MibTableColumn
airFlowSensorAvail=_AirFlowSensorAvail_Object((1,3,6,1,4,1,17373,4,1,5,1,4),_AirFlowSensorAvail_Type())
airFlowSensorAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:airFlowSensorAvail.setStatus(_A)
class _AirFlowSensorTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,200))
_AirFlowSensorTemp_Type.__name__=_D
_AirFlowSensorTemp_Object=MibTableColumn
airFlowSensorTemp=_AirFlowSensorTemp_Object((1,3,6,1,4,1,17373,4,1,5,1,5),_AirFlowSensorTemp_Type())
airFlowSensorTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:airFlowSensorTemp.setStatus(_A)
if mibBuilder.loadTexts:airFlowSensorTemp.setUnits(_F)
class _AirFlowSensorFlow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AirFlowSensorFlow_Type.__name__=_D
_AirFlowSensorFlow_Object=MibTableColumn
airFlowSensorFlow=_AirFlowSensorFlow_Object((1,3,6,1,4,1,17373,4,1,5,1,6),_AirFlowSensorFlow_Type())
airFlowSensorFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:airFlowSensorFlow.setStatus(_A)
class _AirFlowSensorHumidity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AirFlowSensorHumidity_Type.__name__=_D
_AirFlowSensorHumidity_Object=MibTableColumn
airFlowSensorHumidity=_AirFlowSensorHumidity_Object((1,3,6,1,4,1,17373,4,1,5,1,7),_AirFlowSensorHumidity_Type())
airFlowSensorHumidity.setMaxAccess(_C)
if mibBuilder.loadTexts:airFlowSensorHumidity.setStatus(_A)
if mibBuilder.loadTexts:airFlowSensorHumidity.setUnits('%')
class _AirFlowSensorDewPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,200))
_AirFlowSensorDewPoint_Type.__name__=_D
_AirFlowSensorDewPoint_Object=MibTableColumn
airFlowSensorDewPoint=_AirFlowSensorDewPoint_Object((1,3,6,1,4,1,17373,4,1,5,1,8),_AirFlowSensorDewPoint_Type())
airFlowSensorDewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:airFlowSensorDewPoint.setStatus(_A)
if mibBuilder.loadTexts:airFlowSensorDewPoint.setUnits(_F)
_DewPointSensorTable_Object=MibTable
dewPointSensorTable=_DewPointSensorTable_Object((1,3,6,1,4,1,17373,4,1,6))
if mibBuilder.loadTexts:dewPointSensorTable.setStatus(_A)
_DewPointSensorEntry_Object=MibTableRow
dewPointSensorEntry=_DewPointSensorEntry_Object((1,3,6,1,4,1,17373,4,1,6,1))
dewPointSensorEntry.setIndexNames((0,_B,_s))
if mibBuilder.loadTexts:dewPointSensorEntry.setStatus(_A)
class _DewPointSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_DewPointSensorIndex_Type.__name__=_D
_DewPointSensorIndex_Object=MibTableColumn
dewPointSensorIndex=_DewPointSensorIndex_Object((1,3,6,1,4,1,17373,4,1,6,1,1),_DewPointSensorIndex_Type())
dewPointSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dewPointSensorIndex.setStatus(_A)
_DewPointSensorSerial_Type=DisplayString
_DewPointSensorSerial_Object=MibTableColumn
dewPointSensorSerial=_DewPointSensorSerial_Object((1,3,6,1,4,1,17373,4,1,6,1,2),_DewPointSensorSerial_Type())
dewPointSensorSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:dewPointSensorSerial.setStatus(_A)
_DewPointSensorName_Type=DisplayString
_DewPointSensorName_Object=MibTableColumn
dewPointSensorName=_DewPointSensorName_Object((1,3,6,1,4,1,17373,4,1,6,1,3),_DewPointSensorName_Type())
dewPointSensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:dewPointSensorName.setStatus(_A)
_DewPointSensorAvail_Type=Gauge32
_DewPointSensorAvail_Object=MibTableColumn
dewPointSensorAvail=_DewPointSensorAvail_Object((1,3,6,1,4,1,17373,4,1,6,1,4),_DewPointSensorAvail_Type())
dewPointSensorAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:dewPointSensorAvail.setStatus(_A)
class _DewPointSensorTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,200))
_DewPointSensorTemp_Type.__name__=_D
_DewPointSensorTemp_Object=MibTableColumn
dewPointSensorTemp=_DewPointSensorTemp_Object((1,3,6,1,4,1,17373,4,1,6,1,5),_DewPointSensorTemp_Type())
dewPointSensorTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:dewPointSensorTemp.setStatus(_A)
if mibBuilder.loadTexts:dewPointSensorTemp.setUnits(_F)
class _DewPointSensorHumidity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DewPointSensorHumidity_Type.__name__=_D
_DewPointSensorHumidity_Object=MibTableColumn
dewPointSensorHumidity=_DewPointSensorHumidity_Object((1,3,6,1,4,1,17373,4,1,6,1,6),_DewPointSensorHumidity_Type())
dewPointSensorHumidity.setMaxAccess(_C)
if mibBuilder.loadTexts:dewPointSensorHumidity.setStatus(_A)
if mibBuilder.loadTexts:dewPointSensorHumidity.setUnits('%')
class _DewPointSensorDewPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,200))
_DewPointSensorDewPoint_Type.__name__=_D
_DewPointSensorDewPoint_Object=MibTableColumn
dewPointSensorDewPoint=_DewPointSensorDewPoint_Object((1,3,6,1,4,1,17373,4,1,6,1,7),_DewPointSensorDewPoint_Type())
dewPointSensorDewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:dewPointSensorDewPoint.setStatus(_A)
if mibBuilder.loadTexts:dewPointSensorDewPoint.setUnits(_F)
_CcatSensorTable_Object=MibTable
ccatSensorTable=_CcatSensorTable_Object((1,3,6,1,4,1,17373,4,1,7))
if mibBuilder.loadTexts:ccatSensorTable.setStatus(_A)
_CcatSensorEntry_Object=MibTableRow
ccatSensorEntry=_CcatSensorEntry_Object((1,3,6,1,4,1,17373,4,1,7,1))
ccatSensorEntry.setIndexNames((0,_B,_t))
if mibBuilder.loadTexts:ccatSensorEntry.setStatus(_A)
class _CcatSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CcatSensorIndex_Type.__name__=_D
_CcatSensorIndex_Object=MibTableColumn
ccatSensorIndex=_CcatSensorIndex_Object((1,3,6,1,4,1,17373,4,1,7,1,1),_CcatSensorIndex_Type())
ccatSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ccatSensorIndex.setStatus(_A)
_CcatSensorSerial_Type=DisplayString
_CcatSensorSerial_Object=MibTableColumn
ccatSensorSerial=_CcatSensorSerial_Object((1,3,6,1,4,1,17373,4,1,7,1,2),_CcatSensorSerial_Type())
ccatSensorSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:ccatSensorSerial.setStatus(_A)
_CcatSensorName_Type=DisplayString
_CcatSensorName_Object=MibTableColumn
ccatSensorName=_CcatSensorName_Object((1,3,6,1,4,1,17373,4,1,7,1,3),_CcatSensorName_Type())
ccatSensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:ccatSensorName.setStatus(_A)
_CcatSensorAvail_Type=Gauge32
_CcatSensorAvail_Object=MibTableColumn
ccatSensorAvail=_CcatSensorAvail_Object((1,3,6,1,4,1,17373,4,1,7,1,4),_CcatSensorAvail_Type())
ccatSensorAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:ccatSensorAvail.setStatus(_A)
class _CcatSensorValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,5000))
_CcatSensorValue_Type.__name__=_D
_CcatSensorValue_Object=MibTableColumn
ccatSensorValue=_CcatSensorValue_Object((1,3,6,1,4,1,17373,4,1,7,1,5),_CcatSensorValue_Type())
ccatSensorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ccatSensorValue.setStatus(_A)
_CcatSensorType_Type=DisplayString
_CcatSensorType_Object=MibTableColumn
ccatSensorType=_CcatSensorType_Object((1,3,6,1,4,1,17373,4,1,7,1,6),_CcatSensorType_Type())
ccatSensorType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccatSensorType.setStatus(_A)
_CcatSensorDescription_Type=DisplayString
_CcatSensorDescription_Object=MibTableColumn
ccatSensorDescription=_CcatSensorDescription_Object((1,3,6,1,4,1,17373,4,1,7,1,7),_CcatSensorDescription_Type())
ccatSensorDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ccatSensorDescription.setStatus(_A)
_T3hdSensorTable_Object=MibTable
t3hdSensorTable=_T3hdSensorTable_Object((1,3,6,1,4,1,17373,4,1,8))
if mibBuilder.loadTexts:t3hdSensorTable.setStatus(_A)
_T3hdSensorEntry_Object=MibTableRow
t3hdSensorEntry=_T3hdSensorEntry_Object((1,3,6,1,4,1,17373,4,1,8,1))
t3hdSensorEntry.setIndexNames((0,_B,_u))
if mibBuilder.loadTexts:t3hdSensorEntry.setStatus(_A)
class _T3hdSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_T3hdSensorIndex_Type.__name__=_D
_T3hdSensorIndex_Object=MibTableColumn
t3hdSensorIndex=_T3hdSensorIndex_Object((1,3,6,1,4,1,17373,4,1,8,1,1),_T3hdSensorIndex_Type())
t3hdSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdSensorIndex.setStatus(_A)
_T3hdSensorSerial_Type=DisplayString
_T3hdSensorSerial_Object=MibTableColumn
t3hdSensorSerial=_T3hdSensorSerial_Object((1,3,6,1,4,1,17373,4,1,8,1,2),_T3hdSensorSerial_Type())
t3hdSensorSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdSensorSerial.setStatus(_A)
_T3hdSensorName_Type=DisplayString
_T3hdSensorName_Object=MibTableColumn
t3hdSensorName=_T3hdSensorName_Object((1,3,6,1,4,1,17373,4,1,8,1,3),_T3hdSensorName_Type())
t3hdSensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdSensorName.setStatus(_A)
_T3hdSensorAvail_Type=Gauge32
_T3hdSensorAvail_Object=MibTableColumn
t3hdSensorAvail=_T3hdSensorAvail_Object((1,3,6,1,4,1,17373,4,1,8,1,4),_T3hdSensorAvail_Type())
t3hdSensorAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdSensorAvail.setStatus(_A)
_T3hdSensorIntName_Type=DisplayString
_T3hdSensorIntName_Object=MibTableColumn
t3hdSensorIntName=_T3hdSensorIntName_Object((1,3,6,1,4,1,17373,4,1,8,1,5),_T3hdSensorIntName_Type())
t3hdSensorIntName.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdSensorIntName.setStatus(_A)
class _T3hdSensorIntTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,200))
_T3hdSensorIntTemp_Type.__name__=_D
_T3hdSensorIntTemp_Object=MibTableColumn
t3hdSensorIntTemp=_T3hdSensorIntTemp_Object((1,3,6,1,4,1,17373,4,1,8,1,6),_T3hdSensorIntTemp_Type())
t3hdSensorIntTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdSensorIntTemp.setStatus(_A)
if mibBuilder.loadTexts:t3hdSensorIntTemp.setUnits(_F)
class _T3hdSensorIntHumidity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_T3hdSensorIntHumidity_Type.__name__=_D
_T3hdSensorIntHumidity_Object=MibTableColumn
t3hdSensorIntHumidity=_T3hdSensorIntHumidity_Object((1,3,6,1,4,1,17373,4,1,8,1,7),_T3hdSensorIntHumidity_Type())
t3hdSensorIntHumidity.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdSensorIntHumidity.setStatus(_A)
if mibBuilder.loadTexts:t3hdSensorIntHumidity.setUnits('%')
class _T3hdSensorIntDewPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,200))
_T3hdSensorIntDewPoint_Type.__name__=_D
_T3hdSensorIntDewPoint_Object=MibTableColumn
t3hdSensorIntDewPoint=_T3hdSensorIntDewPoint_Object((1,3,6,1,4,1,17373,4,1,8,1,8),_T3hdSensorIntDewPoint_Type())
t3hdSensorIntDewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdSensorIntDewPoint.setStatus(_A)
if mibBuilder.loadTexts:t3hdSensorIntDewPoint.setUnits(_F)
_T3hdSensorExtAAvail_Type=Gauge32
_T3hdSensorExtAAvail_Object=MibTableColumn
t3hdSensorExtAAvail=_T3hdSensorExtAAvail_Object((1,3,6,1,4,1,17373,4,1,8,1,9),_T3hdSensorExtAAvail_Type())
t3hdSensorExtAAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdSensorExtAAvail.setStatus(_A)
_T3hdSensorExtAName_Type=DisplayString
_T3hdSensorExtAName_Object=MibTableColumn
t3hdSensorExtAName=_T3hdSensorExtAName_Object((1,3,6,1,4,1,17373,4,1,8,1,10),_T3hdSensorExtAName_Type())
t3hdSensorExtAName.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdSensorExtAName.setStatus(_A)
class _T3hdSensorExtATemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,200))
_T3hdSensorExtATemp_Type.__name__=_D
_T3hdSensorExtATemp_Object=MibTableColumn
t3hdSensorExtATemp=_T3hdSensorExtATemp_Object((1,3,6,1,4,1,17373,4,1,8,1,11),_T3hdSensorExtATemp_Type())
t3hdSensorExtATemp.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdSensorExtATemp.setStatus(_A)
if mibBuilder.loadTexts:t3hdSensorExtATemp.setUnits(_F)
_T3hdSensorExtBAvail_Type=Gauge32
_T3hdSensorExtBAvail_Object=MibTableColumn
t3hdSensorExtBAvail=_T3hdSensorExtBAvail_Object((1,3,6,1,4,1,17373,4,1,8,1,12),_T3hdSensorExtBAvail_Type())
t3hdSensorExtBAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdSensorExtBAvail.setStatus(_A)
_T3hdSensorExtBName_Type=DisplayString
_T3hdSensorExtBName_Object=MibTableColumn
t3hdSensorExtBName=_T3hdSensorExtBName_Object((1,3,6,1,4,1,17373,4,1,8,1,13),_T3hdSensorExtBName_Type())
t3hdSensorExtBName.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdSensorExtBName.setStatus(_A)
class _T3hdSensorExtBTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,200))
_T3hdSensorExtBTemp_Type.__name__=_D
_T3hdSensorExtBTemp_Object=MibTableColumn
t3hdSensorExtBTemp=_T3hdSensorExtBTemp_Object((1,3,6,1,4,1,17373,4,1,8,1,14),_T3hdSensorExtBTemp_Type())
t3hdSensorExtBTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:t3hdSensorExtBTemp.setStatus(_A)
if mibBuilder.loadTexts:t3hdSensorExtBTemp.setUnits(_F)
_ThdSensorTable_Object=MibTable
thdSensorTable=_ThdSensorTable_Object((1,3,6,1,4,1,17373,4,1,9))
if mibBuilder.loadTexts:thdSensorTable.setStatus(_A)
_ThdSensorEntry_Object=MibTableRow
thdSensorEntry=_ThdSensorEntry_Object((1,3,6,1,4,1,17373,4,1,9,1))
thdSensorEntry.setIndexNames((0,_B,_v))
if mibBuilder.loadTexts:thdSensorEntry.setStatus(_A)
class _ThdSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ThdSensorIndex_Type.__name__=_D
_ThdSensorIndex_Object=MibTableColumn
thdSensorIndex=_ThdSensorIndex_Object((1,3,6,1,4,1,17373,4,1,9,1,1),_ThdSensorIndex_Type())
thdSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:thdSensorIndex.setStatus(_A)
_ThdSensorSerial_Type=DisplayString
_ThdSensorSerial_Object=MibTableColumn
thdSensorSerial=_ThdSensorSerial_Object((1,3,6,1,4,1,17373,4,1,9,1,2),_ThdSensorSerial_Type())
thdSensorSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:thdSensorSerial.setStatus(_A)
_ThdSensorName_Type=DisplayString
_ThdSensorName_Object=MibTableColumn
thdSensorName=_ThdSensorName_Object((1,3,6,1,4,1,17373,4,1,9,1,3),_ThdSensorName_Type())
thdSensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:thdSensorName.setStatus(_A)
_ThdSensorAvail_Type=Gauge32
_ThdSensorAvail_Object=MibTableColumn
thdSensorAvail=_ThdSensorAvail_Object((1,3,6,1,4,1,17373,4,1,9,1,4),_ThdSensorAvail_Type())
thdSensorAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:thdSensorAvail.setStatus(_A)
class _ThdSensorTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,200))
_ThdSensorTemp_Type.__name__=_D
_ThdSensorTemp_Object=MibTableColumn
thdSensorTemp=_ThdSensorTemp_Object((1,3,6,1,4,1,17373,4,1,9,1,5),_ThdSensorTemp_Type())
thdSensorTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:thdSensorTemp.setStatus(_A)
if mibBuilder.loadTexts:thdSensorTemp.setUnits(_F)
class _ThdSensorHumidity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ThdSensorHumidity_Type.__name__=_D
_ThdSensorHumidity_Object=MibTableColumn
thdSensorHumidity=_ThdSensorHumidity_Object((1,3,6,1,4,1,17373,4,1,9,1,6),_ThdSensorHumidity_Type())
thdSensorHumidity.setMaxAccess(_C)
if mibBuilder.loadTexts:thdSensorHumidity.setStatus(_A)
if mibBuilder.loadTexts:thdSensorHumidity.setUnits('%')
class _ThdSensorDewPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,200))
_ThdSensorDewPoint_Type.__name__=_D
_ThdSensorDewPoint_Object=MibTableColumn
thdSensorDewPoint=_ThdSensorDewPoint_Object((1,3,6,1,4,1,17373,4,1,9,1,7),_ThdSensorDewPoint_Type())
thdSensorDewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:thdSensorDewPoint.setStatus(_A)
if mibBuilder.loadTexts:thdSensorDewPoint.setUnits(_F)
_RpmSensorTable_Object=MibTable
rpmSensorTable=_RpmSensorTable_Object((1,3,6,1,4,1,17373,4,1,10))
if mibBuilder.loadTexts:rpmSensorTable.setStatus(_A)
_RpmSensorEntry_Object=MibTableRow
rpmSensorEntry=_RpmSensorEntry_Object((1,3,6,1,4,1,17373,4,1,10,1))
rpmSensorEntry.setIndexNames((0,_B,_w))
if mibBuilder.loadTexts:rpmSensorEntry.setStatus(_A)
class _RpmSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RpmSensorIndex_Type.__name__=_D
_RpmSensorIndex_Object=MibTableColumn
rpmSensorIndex=_RpmSensorIndex_Object((1,3,6,1,4,1,17373,4,1,10,1,1),_RpmSensorIndex_Type())
rpmSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmSensorIndex.setStatus(_A)
_RpmSensorSerial_Type=DisplayString
_RpmSensorSerial_Object=MibTableColumn
rpmSensorSerial=_RpmSensorSerial_Object((1,3,6,1,4,1,17373,4,1,10,1,2),_RpmSensorSerial_Type())
rpmSensorSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmSensorSerial.setStatus(_A)
_RpmSensorName_Type=DisplayString
_RpmSensorName_Object=MibTableColumn
rpmSensorName=_RpmSensorName_Object((1,3,6,1,4,1,17373,4,1,10,1,3),_RpmSensorName_Type())
rpmSensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmSensorName.setStatus(_A)
_RpmSensorAvail_Type=Gauge32
_RpmSensorAvail_Object=MibTableColumn
rpmSensorAvail=_RpmSensorAvail_Object((1,3,6,1,4,1,17373,4,1,10,1,4),_RpmSensorAvail_Type())
rpmSensorAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmSensorAvail.setStatus(_A)
_RpmSensorEnergy_Type=Gauge32
_RpmSensorEnergy_Object=MibTableColumn
rpmSensorEnergy=_RpmSensorEnergy_Object((1,3,6,1,4,1,17373,4,1,10,1,5),_RpmSensorEnergy_Type())
rpmSensorEnergy.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmSensorEnergy.setStatus(_A)
if mibBuilder.loadTexts:rpmSensorEnergy.setUnits('kWh')
_RpmSensorVoltage_Type=Gauge32
_RpmSensorVoltage_Object=MibTableColumn
rpmSensorVoltage=_RpmSensorVoltage_Object((1,3,6,1,4,1,17373,4,1,10,1,6),_RpmSensorVoltage_Type())
rpmSensorVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmSensorVoltage.setStatus(_A)
if mibBuilder.loadTexts:rpmSensorVoltage.setUnits(_G)
_RpmSensorVoltageMax_Type=Gauge32
_RpmSensorVoltageMax_Object=MibTableColumn
rpmSensorVoltageMax=_RpmSensorVoltageMax_Object((1,3,6,1,4,1,17373,4,1,10,1,7),_RpmSensorVoltageMax_Type())
rpmSensorVoltageMax.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmSensorVoltageMax.setStatus(_A)
if mibBuilder.loadTexts:rpmSensorVoltageMax.setUnits(_G)
_RpmSensorVoltageMin_Type=Gauge32
_RpmSensorVoltageMin_Object=MibTableColumn
rpmSensorVoltageMin=_RpmSensorVoltageMin_Object((1,3,6,1,4,1,17373,4,1,10,1,8),_RpmSensorVoltageMin_Type())
rpmSensorVoltageMin.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmSensorVoltageMin.setStatus(_A)
if mibBuilder.loadTexts:rpmSensorVoltageMin.setUnits(_G)
_RpmSensorVoltagePeak_Type=Gauge32
_RpmSensorVoltagePeak_Object=MibTableColumn
rpmSensorVoltagePeak=_RpmSensorVoltagePeak_Object((1,3,6,1,4,1,17373,4,1,10,1,9),_RpmSensorVoltagePeak_Type())
rpmSensorVoltagePeak.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmSensorVoltagePeak.setStatus(_A)
if mibBuilder.loadTexts:rpmSensorVoltagePeak.setUnits('Volts')
_RpmSensorCurrent_Type=Gauge32
_RpmSensorCurrent_Object=MibTableColumn
rpmSensorCurrent=_RpmSensorCurrent_Object((1,3,6,1,4,1,17373,4,1,10,1,10),_RpmSensorCurrent_Type())
rpmSensorCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmSensorCurrent.setStatus(_A)
if mibBuilder.loadTexts:rpmSensorCurrent.setUnits('0.1 Amps (rms)')
_RpmSensorRealPower_Type=Gauge32
_RpmSensorRealPower_Object=MibTableColumn
rpmSensorRealPower=_RpmSensorRealPower_Object((1,3,6,1,4,1,17373,4,1,10,1,11),_RpmSensorRealPower_Type())
rpmSensorRealPower.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmSensorRealPower.setStatus(_A)
if mibBuilder.loadTexts:rpmSensorRealPower.setUnits('Watts')
_RpmSensorApparentPower_Type=Gauge32
_RpmSensorApparentPower_Object=MibTableColumn
rpmSensorApparentPower=_RpmSensorApparentPower_Object((1,3,6,1,4,1,17373,4,1,10,1,12),_RpmSensorApparentPower_Type())
rpmSensorApparentPower.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmSensorApparentPower.setStatus(_A)
if mibBuilder.loadTexts:rpmSensorApparentPower.setUnits('Volt-Amps')
_RpmSensorPowerFactor_Type=Gauge32
_RpmSensorPowerFactor_Object=MibTableColumn
rpmSensorPowerFactor=_RpmSensorPowerFactor_Object((1,3,6,1,4,1,17373,4,1,10,1,13),_RpmSensorPowerFactor_Type())
rpmSensorPowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmSensorPowerFactor.setStatus(_A)
if mibBuilder.loadTexts:rpmSensorPowerFactor.setUnits('%')
_RpmSensorOutlet1_Type=Gauge32
_RpmSensorOutlet1_Object=MibTableColumn
rpmSensorOutlet1=_RpmSensorOutlet1_Object((1,3,6,1,4,1,17373,4,1,10,1,14),_RpmSensorOutlet1_Type())
rpmSensorOutlet1.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmSensorOutlet1.setStatus(_A)
_RpmSensorOutlet2_Type=Gauge32
_RpmSensorOutlet2_Object=MibTableColumn
rpmSensorOutlet2=_RpmSensorOutlet2_Object((1,3,6,1,4,1,17373,4,1,10,1,15),_RpmSensorOutlet2_Type())
rpmSensorOutlet2.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmSensorOutlet2.setStatus(_A)
_Trap_ObjectIdentity=ObjectIdentity
trap=_Trap_ObjectIdentity((1,3,6,1,4,1,17373,4,1,32767))
_TrapPrefix_ObjectIdentity=ObjectIdentity
trapPrefix=_TrapPrefix_ObjectIdentity((1,3,6,1,4,1,17373,4,1,32767,0))
internalTestNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10101))
if mibBuilder.loadTexts:internalTestNOTIFY.setStatus(_A)
internalTempNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10205))
internalTempNOTIFY.setObjects(*((_B,_H),(_B,_E)))
if mibBuilder.loadTexts:internalTempNOTIFY.setStatus(_A)
internalHumidityNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10206))
internalHumidityNOTIFY.setObjects((_B,_I))
if mibBuilder.loadTexts:internalHumidityNOTIFY.setStatus(_A)
internalDewPointNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10207))
internalDewPointNOTIFY.setObjects(*((_B,_J),(_B,_E)))
if mibBuilder.loadTexts:internalDewPointNOTIFY.setStatus(_A)
internalIO1NOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10208))
internalIO1NOTIFY.setObjects((_B,_K))
if mibBuilder.loadTexts:internalIO1NOTIFY.setStatus(_A)
internalIO2NOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10209))
internalIO2NOTIFY.setObjects((_B,_L))
if mibBuilder.loadTexts:internalIO2NOTIFY.setStatus(_A)
internalIO3NOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10210))
internalIO3NOTIFY.setObjects((_B,_M))
if mibBuilder.loadTexts:internalIO3NOTIFY.setStatus(_A)
internalIO4NOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10211))
internalIO4NOTIFY.setObjects((_B,_N))
if mibBuilder.loadTexts:internalIO4NOTIFY.setStatus(_A)
tempSensorTempNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10405))
tempSensorTempNOTIFY.setObjects(*((_B,_O),(_B,_E)))
if mibBuilder.loadTexts:tempSensorTempNOTIFY.setStatus(_A)
airFlowSensorTempNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10505))
airFlowSensorTempNOTIFY.setObjects(*((_B,_P),(_B,_E)))
if mibBuilder.loadTexts:airFlowSensorTempNOTIFY.setStatus(_A)
airFlowSensorFlowNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10506))
airFlowSensorFlowNOTIFY.setObjects((_B,_Q))
if mibBuilder.loadTexts:airFlowSensorFlowNOTIFY.setStatus(_A)
airFlowSensorHumidityNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10507))
airFlowSensorHumidityNOTIFY.setObjects((_B,_R))
if mibBuilder.loadTexts:airFlowSensorHumidityNOTIFY.setStatus(_A)
airFlowSensorDewPointNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10508))
airFlowSensorDewPointNOTIFY.setObjects(*((_B,_S),(_B,_E)))
if mibBuilder.loadTexts:airFlowSensorDewPointNOTIFY.setStatus(_A)
dewPointSensorTempNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10605))
dewPointSensorTempNOTIFY.setObjects(*((_B,_T),(_B,_E)))
if mibBuilder.loadTexts:dewPointSensorTempNOTIFY.setStatus(_A)
dewPointSensorHumidityNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10606))
dewPointSensorHumidityNOTIFY.setObjects((_B,_U))
if mibBuilder.loadTexts:dewPointSensorHumidityNOTIFY.setStatus(_A)
dewPointSensorDewPointNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10607))
dewPointSensorDewPointNOTIFY.setObjects(*((_B,_V),(_B,_E)))
if mibBuilder.loadTexts:dewPointSensorDewPointNOTIFY.setStatus(_A)
ccatSensorValueNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10705))
ccatSensorValueNOTIFY.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ccatSensorValueNOTIFY.setStatus(_A)
t3hdSensorIntTempNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10806))
t3hdSensorIntTempNOTIFY.setObjects(*((_B,_Y),(_B,_E)))
if mibBuilder.loadTexts:t3hdSensorIntTempNOTIFY.setStatus(_A)
t3hdSensorIntHumidityNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10807))
t3hdSensorIntHumidityNOTIFY.setObjects((_B,_Z))
if mibBuilder.loadTexts:t3hdSensorIntHumidityNOTIFY.setStatus(_A)
t3hdSensorIntDewPointNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10808))
t3hdSensorIntDewPointNOTIFY.setObjects(*((_B,_a),(_B,_E)))
if mibBuilder.loadTexts:t3hdSensorIntDewPointNOTIFY.setStatus(_A)
t3hdSensorExtATempNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10811))
t3hdSensorExtATempNOTIFY.setObjects(*((_B,_b),(_B,_E)))
if mibBuilder.loadTexts:t3hdSensorExtATempNOTIFY.setStatus(_A)
t3hdSensorExtBTempNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10814))
t3hdSensorExtBTempNOTIFY.setObjects(*((_B,_c),(_B,_E)))
if mibBuilder.loadTexts:t3hdSensorExtBTempNOTIFY.setStatus(_A)
thdSensorTempNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10905))
thdSensorTempNOTIFY.setObjects(*((_B,_d),(_B,_E)))
if mibBuilder.loadTexts:thdSensorTempNOTIFY.setStatus(_A)
thdSensorHumidityNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10906))
thdSensorHumidityNOTIFY.setObjects((_B,_e))
if mibBuilder.loadTexts:thdSensorHumidityNOTIFY.setStatus(_A)
thdSensorDewPointNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,10907))
thdSensorDewPointNOTIFY.setObjects(*((_B,_f),(_B,_E)))
if mibBuilder.loadTexts:thdSensorDewPointNOTIFY.setStatus(_A)
rpmSensorEnergyNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,11005))
rpmSensorEnergyNOTIFY.setObjects((_B,_g))
if mibBuilder.loadTexts:rpmSensorEnergyNOTIFY.setStatus(_A)
rpmSensorVoltageNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,11006))
rpmSensorVoltageNOTIFY.setObjects((_B,_h))
if mibBuilder.loadTexts:rpmSensorVoltageNOTIFY.setStatus(_A)
rpmSensorVoltageMaxNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,11007))
rpmSensorVoltageMaxNOTIFY.setObjects((_B,_i))
if mibBuilder.loadTexts:rpmSensorVoltageMaxNOTIFY.setStatus(_A)
rpmSensorVoltageMinNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,11008))
rpmSensorVoltageMinNOTIFY.setObjects((_B,_j))
if mibBuilder.loadTexts:rpmSensorVoltageMinNOTIFY.setStatus(_A)
rpmSensorVoltagePeakNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,11009))
rpmSensorVoltagePeakNOTIFY.setObjects((_B,_k))
if mibBuilder.loadTexts:rpmSensorVoltagePeakNOTIFY.setStatus(_A)
rpmSensorCurrentNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,11010))
rpmSensorCurrentNOTIFY.setObjects((_B,_l))
if mibBuilder.loadTexts:rpmSensorCurrentNOTIFY.setStatus(_A)
rpmSensorRealPowerNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,11011))
rpmSensorRealPowerNOTIFY.setObjects((_B,_m))
if mibBuilder.loadTexts:rpmSensorRealPowerNOTIFY.setStatus(_A)
rpmSensorApparentPowerNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,11012))
rpmSensorApparentPowerNOTIFY.setObjects((_B,_n))
if mibBuilder.loadTexts:rpmSensorApparentPowerNOTIFY.setStatus(_A)
rpmSensorPowerFactorNOTIFY=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,11013))
rpmSensorPowerFactorNOTIFY.setObjects((_B,_o))
if mibBuilder.loadTexts:rpmSensorPowerFactorNOTIFY.setStatus(_A)
internalTempCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20205))
internalTempCLEAR.setObjects(*((_B,_H),(_B,_E)))
if mibBuilder.loadTexts:internalTempCLEAR.setStatus(_A)
internalHumidityCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20206))
internalHumidityCLEAR.setObjects((_B,_I))
if mibBuilder.loadTexts:internalHumidityCLEAR.setStatus(_A)
internalDewPointCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20207))
internalDewPointCLEAR.setObjects(*((_B,_J),(_B,_E)))
if mibBuilder.loadTexts:internalDewPointCLEAR.setStatus(_A)
internalIO1CLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20208))
internalIO1CLEAR.setObjects((_B,_K))
if mibBuilder.loadTexts:internalIO1CLEAR.setStatus(_A)
internalIO2CLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20209))
internalIO2CLEAR.setObjects((_B,_L))
if mibBuilder.loadTexts:internalIO2CLEAR.setStatus(_A)
internalIO3CLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20210))
internalIO3CLEAR.setObjects((_B,_M))
if mibBuilder.loadTexts:internalIO3CLEAR.setStatus(_A)
internalIO4CLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20211))
internalIO4CLEAR.setObjects((_B,_N))
if mibBuilder.loadTexts:internalIO4CLEAR.setStatus(_A)
tempSensorTempCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20405))
tempSensorTempCLEAR.setObjects(*((_B,_O),(_B,_E)))
if mibBuilder.loadTexts:tempSensorTempCLEAR.setStatus(_A)
airFlowSensorTempCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20505))
airFlowSensorTempCLEAR.setObjects(*((_B,_P),(_B,_E)))
if mibBuilder.loadTexts:airFlowSensorTempCLEAR.setStatus(_A)
airFlowSensorFlowCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20506))
airFlowSensorFlowCLEAR.setObjects((_B,_Q))
if mibBuilder.loadTexts:airFlowSensorFlowCLEAR.setStatus(_A)
airFlowSensorHumidityCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20507))
airFlowSensorHumidityCLEAR.setObjects((_B,_R))
if mibBuilder.loadTexts:airFlowSensorHumidityCLEAR.setStatus(_A)
airFlowSensorDewPointCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20508))
airFlowSensorDewPointCLEAR.setObjects(*((_B,_S),(_B,_E)))
if mibBuilder.loadTexts:airFlowSensorDewPointCLEAR.setStatus(_A)
dewPointSensorTempCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20605))
dewPointSensorTempCLEAR.setObjects(*((_B,_T),(_B,_E)))
if mibBuilder.loadTexts:dewPointSensorTempCLEAR.setStatus(_A)
dewPointSensorHumidityCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20606))
dewPointSensorHumidityCLEAR.setObjects((_B,_U))
if mibBuilder.loadTexts:dewPointSensorHumidityCLEAR.setStatus(_A)
dewPointSensorDewPointCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20607))
dewPointSensorDewPointCLEAR.setObjects(*((_B,_V),(_B,_E)))
if mibBuilder.loadTexts:dewPointSensorDewPointCLEAR.setStatus(_A)
ccatSensorValueCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20705))
ccatSensorValueCLEAR.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ccatSensorValueCLEAR.setStatus(_A)
t3hdSensorIntTempCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20806))
t3hdSensorIntTempCLEAR.setObjects(*((_B,_Y),(_B,_E)))
if mibBuilder.loadTexts:t3hdSensorIntTempCLEAR.setStatus(_A)
t3hdSensorIntHumidityCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20807))
t3hdSensorIntHumidityCLEAR.setObjects((_B,_Z))
if mibBuilder.loadTexts:t3hdSensorIntHumidityCLEAR.setStatus(_A)
t3hdSensorIntDewPointCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20808))
t3hdSensorIntDewPointCLEAR.setObjects(*((_B,_a),(_B,_E)))
if mibBuilder.loadTexts:t3hdSensorIntDewPointCLEAR.setStatus(_A)
t3hdSensorExtATempCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20811))
t3hdSensorExtATempCLEAR.setObjects(*((_B,_b),(_B,_E)))
if mibBuilder.loadTexts:t3hdSensorExtATempCLEAR.setStatus(_A)
t3hdSensorExtBTempCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20814))
t3hdSensorExtBTempCLEAR.setObjects(*((_B,_c),(_B,_E)))
if mibBuilder.loadTexts:t3hdSensorExtBTempCLEAR.setStatus(_A)
thdSensorTempCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20905))
thdSensorTempCLEAR.setObjects(*((_B,_d),(_B,_E)))
if mibBuilder.loadTexts:thdSensorTempCLEAR.setStatus(_A)
thdSensorHumidityCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20906))
thdSensorHumidityCLEAR.setObjects((_B,_e))
if mibBuilder.loadTexts:thdSensorHumidityCLEAR.setStatus(_A)
thdSensorDewPointCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,20907))
thdSensorDewPointCLEAR.setObjects(*((_B,_f),(_B,_E)))
if mibBuilder.loadTexts:thdSensorDewPointCLEAR.setStatus(_A)
rpmSensorEnergyCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,21005))
rpmSensorEnergyCLEAR.setObjects((_B,_g))
if mibBuilder.loadTexts:rpmSensorEnergyCLEAR.setStatus(_A)
rpmSensorVoltageCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,21006))
rpmSensorVoltageCLEAR.setObjects((_B,_h))
if mibBuilder.loadTexts:rpmSensorVoltageCLEAR.setStatus(_A)
rpmSensorVoltageMaxCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,21007))
rpmSensorVoltageMaxCLEAR.setObjects((_B,_i))
if mibBuilder.loadTexts:rpmSensorVoltageMaxCLEAR.setStatus(_A)
rpmSensorVoltageMinCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,21008))
rpmSensorVoltageMinCLEAR.setObjects((_B,_j))
if mibBuilder.loadTexts:rpmSensorVoltageMinCLEAR.setStatus(_A)
rpmSensorVoltagePeakCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,21009))
rpmSensorVoltagePeakCLEAR.setObjects((_B,_k))
if mibBuilder.loadTexts:rpmSensorVoltagePeakCLEAR.setStatus(_A)
rpmSensorCurrentCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,21010))
rpmSensorCurrentCLEAR.setObjects((_B,_l))
if mibBuilder.loadTexts:rpmSensorCurrentCLEAR.setStatus(_A)
rpmSensorRealPowerCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,21011))
rpmSensorRealPowerCLEAR.setObjects((_B,_m))
if mibBuilder.loadTexts:rpmSensorRealPowerCLEAR.setStatus(_A)
rpmSensorApparentPowerCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,21012))
rpmSensorApparentPowerCLEAR.setObjects((_B,_n))
if mibBuilder.loadTexts:rpmSensorApparentPowerCLEAR.setStatus(_A)
rpmSensorPowerFactorCLEAR=NotificationType((1,3,6,1,4,1,17373,4,1,32767,0,21013))
rpmSensorPowerFactorCLEAR.setObjects((_B,_o))
if mibBuilder.loadTexts:rpmSensorPowerFactorCLEAR.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'itwatchdogs':itwatchdogs,'blackbird':blackbird,'watchdog100':watchdog100,'deviceInfo':deviceInfo,'productTitle':productTitle,'productVersion':productVersion,'productFriendlyName':productFriendlyName,'productMacAddress':productMacAddress,'productUrl':productUrl,'deviceCount':deviceCount,_E:temperatureUnits,'internalTable':internalTable,'internalEntry':internalEntry,_p:internalIndex,'internalSerial':internalSerial,'internalName':internalName,'internalAvail':internalAvail,_H:internalTemp,_I:internalHumidity,_J:internalDewPoint,_K:internalIO1,_L:internalIO2,_M:internalIO3,_N:internalIO4,'internalRelayState':internalRelayState,'tempSensorTable':tempSensorTable,'tempSensorEntry':tempSensorEntry,_q:tempSensorIndex,'tempSensorSerial':tempSensorSerial,'tempSensorName':tempSensorName,'tempSensorAvail':tempSensorAvail,_O:tempSensorTemp,'airFlowSensorTable':airFlowSensorTable,'airFlowSensorEntry':airFlowSensorEntry,_r:airFlowSensorIndex,'airFlowSensorSerial':airFlowSensorSerial,'airFlowSensorName':airFlowSensorName,'airFlowSensorAvail':airFlowSensorAvail,_P:airFlowSensorTemp,_Q:airFlowSensorFlow,_R:airFlowSensorHumidity,_S:airFlowSensorDewPoint,'dewPointSensorTable':dewPointSensorTable,'dewPointSensorEntry':dewPointSensorEntry,_s:dewPointSensorIndex,'dewPointSensorSerial':dewPointSensorSerial,'dewPointSensorName':dewPointSensorName,'dewPointSensorAvail':dewPointSensorAvail,_T:dewPointSensorTemp,_U:dewPointSensorHumidity,_V:dewPointSensorDewPoint,'ccatSensorTable':ccatSensorTable,'ccatSensorEntry':ccatSensorEntry,_t:ccatSensorIndex,'ccatSensorSerial':ccatSensorSerial,'ccatSensorName':ccatSensorName,'ccatSensorAvail':ccatSensorAvail,_W:ccatSensorValue,_X:ccatSensorType,'ccatSensorDescription':ccatSensorDescription,'t3hdSensorTable':t3hdSensorTable,'t3hdSensorEntry':t3hdSensorEntry,_u:t3hdSensorIndex,'t3hdSensorSerial':t3hdSensorSerial,'t3hdSensorName':t3hdSensorName,'t3hdSensorAvail':t3hdSensorAvail,'t3hdSensorIntName':t3hdSensorIntName,_Y:t3hdSensorIntTemp,_Z:t3hdSensorIntHumidity,_a:t3hdSensorIntDewPoint,'t3hdSensorExtAAvail':t3hdSensorExtAAvail,'t3hdSensorExtAName':t3hdSensorExtAName,_b:t3hdSensorExtATemp,'t3hdSensorExtBAvail':t3hdSensorExtBAvail,'t3hdSensorExtBName':t3hdSensorExtBName,_c:t3hdSensorExtBTemp,'thdSensorTable':thdSensorTable,'thdSensorEntry':thdSensorEntry,_v:thdSensorIndex,'thdSensorSerial':thdSensorSerial,'thdSensorName':thdSensorName,'thdSensorAvail':thdSensorAvail,_d:thdSensorTemp,_e:thdSensorHumidity,_f:thdSensorDewPoint,'rpmSensorTable':rpmSensorTable,'rpmSensorEntry':rpmSensorEntry,_w:rpmSensorIndex,'rpmSensorSerial':rpmSensorSerial,'rpmSensorName':rpmSensorName,'rpmSensorAvail':rpmSensorAvail,_g:rpmSensorEnergy,_h:rpmSensorVoltage,_i:rpmSensorVoltageMax,_j:rpmSensorVoltageMin,_k:rpmSensorVoltagePeak,_l:rpmSensorCurrent,_m:rpmSensorRealPower,_n:rpmSensorApparentPower,_o:rpmSensorPowerFactor,'rpmSensorOutlet1':rpmSensorOutlet1,'rpmSensorOutlet2':rpmSensorOutlet2,'trap':trap,'trapPrefix':trapPrefix,'internalTestNOTIFY':internalTestNOTIFY,'internalTempNOTIFY':internalTempNOTIFY,'internalHumidityNOTIFY':internalHumidityNOTIFY,'internalDewPointNOTIFY':internalDewPointNOTIFY,'internalIO1NOTIFY':internalIO1NOTIFY,'internalIO2NOTIFY':internalIO2NOTIFY,'internalIO3NOTIFY':internalIO3NOTIFY,'internalIO4NOTIFY':internalIO4NOTIFY,'tempSensorTempNOTIFY':tempSensorTempNOTIFY,'airFlowSensorTempNOTIFY':airFlowSensorTempNOTIFY,'airFlowSensorFlowNOTIFY':airFlowSensorFlowNOTIFY,'airFlowSensorHumidityNOTIFY':airFlowSensorHumidityNOTIFY,'airFlowSensorDewPointNOTIFY':airFlowSensorDewPointNOTIFY,'dewPointSensorTempNOTIFY':dewPointSensorTempNOTIFY,'dewPointSensorHumidityNOTIFY':dewPointSensorHumidityNOTIFY,'dewPointSensorDewPointNOTIFY':dewPointSensorDewPointNOTIFY,'ccatSensorValueNOTIFY':ccatSensorValueNOTIFY,'t3hdSensorIntTempNOTIFY':t3hdSensorIntTempNOTIFY,'t3hdSensorIntHumidityNOTIFY':t3hdSensorIntHumidityNOTIFY,'t3hdSensorIntDewPointNOTIFY':t3hdSensorIntDewPointNOTIFY,'t3hdSensorExtATempNOTIFY':t3hdSensorExtATempNOTIFY,'t3hdSensorExtBTempNOTIFY':t3hdSensorExtBTempNOTIFY,'thdSensorTempNOTIFY':thdSensorTempNOTIFY,'thdSensorHumidityNOTIFY':thdSensorHumidityNOTIFY,'thdSensorDewPointNOTIFY':thdSensorDewPointNOTIFY,'rpmSensorEnergyNOTIFY':rpmSensorEnergyNOTIFY,'rpmSensorVoltageNOTIFY':rpmSensorVoltageNOTIFY,'rpmSensorVoltageMaxNOTIFY':rpmSensorVoltageMaxNOTIFY,'rpmSensorVoltageMinNOTIFY':rpmSensorVoltageMinNOTIFY,'rpmSensorVoltagePeakNOTIFY':rpmSensorVoltagePeakNOTIFY,'rpmSensorCurrentNOTIFY':rpmSensorCurrentNOTIFY,'rpmSensorRealPowerNOTIFY':rpmSensorRealPowerNOTIFY,'rpmSensorApparentPowerNOTIFY':rpmSensorApparentPowerNOTIFY,'rpmSensorPowerFactorNOTIFY':rpmSensorPowerFactorNOTIFY,'internalTempCLEAR':internalTempCLEAR,'internalHumidityCLEAR':internalHumidityCLEAR,'internalDewPointCLEAR':internalDewPointCLEAR,'internalIO1CLEAR':internalIO1CLEAR,'internalIO2CLEAR':internalIO2CLEAR,'internalIO3CLEAR':internalIO3CLEAR,'internalIO4CLEAR':internalIO4CLEAR,'tempSensorTempCLEAR':tempSensorTempCLEAR,'airFlowSensorTempCLEAR':airFlowSensorTempCLEAR,'airFlowSensorFlowCLEAR':airFlowSensorFlowCLEAR,'airFlowSensorHumidityCLEAR':airFlowSensorHumidityCLEAR,'airFlowSensorDewPointCLEAR':airFlowSensorDewPointCLEAR,'dewPointSensorTempCLEAR':dewPointSensorTempCLEAR,'dewPointSensorHumidityCLEAR':dewPointSensorHumidityCLEAR,'dewPointSensorDewPointCLEAR':dewPointSensorDewPointCLEAR,'ccatSensorValueCLEAR':ccatSensorValueCLEAR,'t3hdSensorIntTempCLEAR':t3hdSensorIntTempCLEAR,'t3hdSensorIntHumidityCLEAR':t3hdSensorIntHumidityCLEAR,'t3hdSensorIntDewPointCLEAR':t3hdSensorIntDewPointCLEAR,'t3hdSensorExtATempCLEAR':t3hdSensorExtATempCLEAR,'t3hdSensorExtBTempCLEAR':t3hdSensorExtBTempCLEAR,'thdSensorTempCLEAR':thdSensorTempCLEAR,'thdSensorHumidityCLEAR':thdSensorHumidityCLEAR,'thdSensorDewPointCLEAR':thdSensorDewPointCLEAR,'rpmSensorEnergyCLEAR':rpmSensorEnergyCLEAR,'rpmSensorVoltageCLEAR':rpmSensorVoltageCLEAR,'rpmSensorVoltageMaxCLEAR':rpmSensorVoltageMaxCLEAR,'rpmSensorVoltageMinCLEAR':rpmSensorVoltageMinCLEAR,'rpmSensorVoltagePeakCLEAR':rpmSensorVoltagePeakCLEAR,'rpmSensorCurrentCLEAR':rpmSensorCurrentCLEAR,'rpmSensorRealPowerCLEAR':rpmSensorRealPowerCLEAR,'rpmSensorApparentPowerCLEAR':rpmSensorApparentPowerCLEAR,'rpmSensorPowerFactorCLEAR':rpmSensorPowerFactorCLEAR})