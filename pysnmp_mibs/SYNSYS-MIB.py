_L='mpiAcKwhStartEPOCH'
_K='mpiAcKwh'
_J='outletIndex'
_I='outletStatus'
_H='outletName'
_G='read-write'
_F='systemName'
_E='Integer32'
_D='SYNSYS-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
synSys=ModuleIdentity((1,3,6,1,4,1,21728,3))
if mibBuilder.loadTexts:synSys.setRevisions(('2020-03-20 00:00','2015-05-10 00:00'))
_Synaccess_ObjectIdentity=ObjectIdentity
synaccess=_Synaccess_ObjectIdentity((1,3,6,1,4,1,21728))
_SystemDescr_ObjectIdentity=ObjectIdentity
systemDescr=_SystemDescr_ObjectIdentity((1,3,6,1,4,1,21728,3,1))
class _SystemModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SystemModel_Type.__name__=_C
_SystemModel_Object=MibScalar
systemModel=_SystemModel_Object((1,3,6,1,4,1,21728,3,1,1),_SystemModel_Type())
systemModel.setMaxAccess(_B)
if mibBuilder.loadTexts:systemModel.setStatus(_A)
class _SystemName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SystemName_Type.__name__=_C
_SystemName_Object=MibScalar
systemName=_SystemName_Object((1,3,6,1,4,1,21728,3,1,2),_SystemName_Type())
systemName.setMaxAccess(_B)
if mibBuilder.loadTexts:systemName.setStatus(_A)
class _PowerOutletNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PowerOutletNum_Type.__name__=_E
_PowerOutletNum_Object=MibScalar
powerOutletNum=_PowerOutletNum_Object((1,3,6,1,4,1,21728,3,1,3),_PowerOutletNum_Type())
powerOutletNum.setMaxAccess(_B)
if mibBuilder.loadTexts:powerOutletNum.setStatus(_A)
class _SerialPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_SerialPortNum_Type.__name__=_E
_SerialPortNum_Object=MibScalar
serialPortNum=_SerialPortNum_Object((1,3,6,1,4,1,21728,3,1,4),_SerialPortNum_Type())
serialPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:serialPortNum.setStatus(_A)
_SystemUpTime_Type=Integer32
_SystemUpTime_Object=MibScalar
systemUpTime=_SystemUpTime_Object((1,3,6,1,4,1,21728,3,1,5),_SystemUpTime_Type())
systemUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:systemUpTime.setStatus(_A)
class _SwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SwVersion_Type.__name__=_C
_SwVersion_Object=MibScalar
swVersion=_SwVersion_Object((1,3,6,1,4,1,21728,3,1,6),_SwVersion_Type())
swVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:swVersion.setStatus(_A)
class _AcCurrentSensorNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_AcCurrentSensorNumber_Type.__name__=_E
_AcCurrentSensorNumber_Object=MibScalar
acCurrentSensorNumber=_AcCurrentSensorNumber_Object((1,3,6,1,4,1,21728,3,1,7),_AcCurrentSensorNumber_Type())
acCurrentSensorNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:acCurrentSensorNumber.setStatus(_A)
class _TemperatureProbe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_TemperatureProbe_Type.__name__=_E
_TemperatureProbe_Object=MibScalar
temperatureProbe=_TemperatureProbe_Object((1,3,6,1,4,1,21728,3,1,8),_TemperatureProbe_Type())
temperatureProbe.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureProbe.setStatus(_A)
class _AcMPIModNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_AcMPIModNumber_Type.__name__=_E
_AcMPIModNumber_Object=MibScalar
acMPIModNumber=_AcMPIModNumber_Object((1,3,6,1,4,1,21728,3,1,9),_AcMPIModNumber_Type())
acMPIModNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:acMPIModNumber.setStatus(_A)
_OutletOpTables_ObjectIdentity=ObjectIdentity
outletOpTables=_OutletOpTables_ObjectIdentity((1,3,6,1,4,1,21728,3,2))
_OutletTable_Object=MibTable
outletTable=_OutletTable_Object((1,3,6,1,4,1,21728,3,2,1))
if mibBuilder.loadTexts:outletTable.setStatus(_A)
_OutletEntry_Object=MibTableRow
outletEntry=_OutletEntry_Object((1,3,6,1,4,1,21728,3,2,1,1))
outletEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:outletEntry.setStatus(_A)
class _OutletIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_OutletIndex_Type.__name__=_E
_OutletIndex_Object=MibTableColumn
outletIndex=_OutletIndex_Object((1,3,6,1,4,1,21728,3,2,1,1,1),_OutletIndex_Type())
outletIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:outletIndex.setStatus(_A)
class _OutletName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_OutletName_Type.__name__=_C
_OutletName_Object=MibTableColumn
outletName=_OutletName_Object((1,3,6,1,4,1,21728,3,2,1,1,2),_OutletName_Type())
outletName.setMaxAccess(_B)
if mibBuilder.loadTexts:outletName.setStatus(_A)
class _OutletStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_OutletStatus_Type.__name__=_E
_OutletStatus_Object=MibTableColumn
outletStatus=_OutletStatus_Object((1,3,6,1,4,1,21728,3,2,1,1,3),_OutletStatus_Type())
outletStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:outletStatus.setStatus(_A)
class _OutletAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('on',1),('off',2),('reboot',3)))
_OutletAction_Type.__name__=_E
_OutletAction_Object=MibTableColumn
outletAction=_OutletAction_Object((1,3,6,1,4,1,21728,3,2,1,1,4),_OutletAction_Type())
outletAction.setMaxAccess(_G)
if mibBuilder.loadTexts:outletAction.setStatus(_A)
class _OutletCurrentDraw_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_OutletCurrentDraw_Type.__name__=_C
_OutletCurrentDraw_Object=MibTableColumn
outletCurrentDraw=_OutletCurrentDraw_Object((1,3,6,1,4,1,21728,3,2,1,1,5),_OutletCurrentDraw_Type())
outletCurrentDraw.setMaxAccess(_B)
if mibBuilder.loadTexts:outletCurrentDraw.setStatus(_A)
_EnviroTable_ObjectIdentity=ObjectIdentity
enviroTable=_EnviroTable_ObjectIdentity((1,3,6,1,4,1,21728,3,3))
class _CurrentAlarmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,35))
_CurrentAlarmThreshold_Type.__name__=_E
_CurrentAlarmThreshold_Object=MibScalar
currentAlarmThreshold=_CurrentAlarmThreshold_Object((1,3,6,1,4,1,21728,3,3,1),_CurrentAlarmThreshold_Type())
currentAlarmThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:currentAlarmThreshold.setStatus(_A)
class _CurrentDrawStatus1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_CurrentDrawStatus1_Type.__name__=_C
_CurrentDrawStatus1_Object=MibScalar
currentDrawStatus1=_CurrentDrawStatus1_Object((1,3,6,1,4,1,21728,3,3,2),_CurrentDrawStatus1_Type())
currentDrawStatus1.setMaxAccess(_B)
if mibBuilder.loadTexts:currentDrawStatus1.setStatus(_A)
class _CurrentDrawStatus2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_CurrentDrawStatus2_Type.__name__=_C
_CurrentDrawStatus2_Object=MibScalar
currentDrawStatus2=_CurrentDrawStatus2_Object((1,3,6,1,4,1,21728,3,3,3),_CurrentDrawStatus2_Type())
currentDrawStatus2.setMaxAccess(_B)
if mibBuilder.loadTexts:currentDrawStatus2.setStatus(_A)
class _CurrentDrawMax1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_CurrentDrawMax1_Type.__name__=_C
_CurrentDrawMax1_Object=MibScalar
currentDrawMax1=_CurrentDrawMax1_Object((1,3,6,1,4,1,21728,3,3,4),_CurrentDrawMax1_Type())
currentDrawMax1.setMaxAccess(_B)
if mibBuilder.loadTexts:currentDrawMax1.setStatus(_A)
class _CurrentDrawMax2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_CurrentDrawMax2_Type.__name__=_C
_CurrentDrawMax2_Object=MibScalar
currentDrawMax2=_CurrentDrawMax2_Object((1,3,6,1,4,1,21728,3,3,5),_CurrentDrawMax2_Type())
currentDrawMax2.setMaxAccess(_B)
if mibBuilder.loadTexts:currentDrawMax2.setStatus(_A)
class _TemperatureUpThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,100))
_TemperatureUpThreshold_Type.__name__=_E
_TemperatureUpThreshold_Object=MibScalar
temperatureUpThreshold=_TemperatureUpThreshold_Object((1,3,6,1,4,1,21728,3,3,6),_TemperatureUpThreshold_Type())
temperatureUpThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureUpThreshold.setStatus(_A)
class _TemperatureLowThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,100))
_TemperatureLowThreshold_Type.__name__=_E
_TemperatureLowThreshold_Object=MibScalar
temperatureLowThreshold=_TemperatureLowThreshold_Object((1,3,6,1,4,1,21728,3,3,7),_TemperatureLowThreshold_Type())
temperatureLowThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureLowThreshold.setStatus(_A)
class _TemperatureReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,100))
_TemperatureReading_Type.__name__=_E
_TemperatureReading_Object=MibScalar
temperatureReading=_TemperatureReading_Object((1,3,6,1,4,1,21728,3,3,8),_TemperatureReading_Type())
temperatureReading.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureReading.setStatus(_A)
_TrapSetting_ObjectIdentity=ObjectIdentity
trapSetting=_TrapSetting_ObjectIdentity((1,3,6,1,4,1,21728,3,4))
class _TrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_TrapEnable_Type.__name__=_E
_TrapEnable_Object=MibScalar
trapEnable=_TrapEnable_Object((1,3,6,1,4,1,21728,3,4,1),_TrapEnable_Type())
trapEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:trapEnable.setStatus(_A)
_TrapRcvIP_Type=IpAddress
_TrapRcvIP_Object=MibScalar
trapRcvIP=_TrapRcvIP_Object((1,3,6,1,4,1,21728,3,4,2),_TrapRcvIP_Type())
trapRcvIP.setMaxAccess(_G)
if mibBuilder.loadTexts:trapRcvIP.setStatus(_A)
class _TrapCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_TrapCommunity_Type.__name__=_C
_TrapCommunity_Object=MibScalar
trapCommunity=_TrapCommunity_Object((1,3,6,1,4,1,21728,3,4,3),_TrapCommunity_Type())
trapCommunity.setMaxAccess(_G)
if mibBuilder.loadTexts:trapCommunity.setStatus(_A)
_EnergyStatus_ObjectIdentity=ObjectIdentity
energyStatus=_EnergyStatus_ObjectIdentity((1,3,6,1,4,1,21728,3,5))
class _MpiCurrent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MpiCurrent_Type.__name__=_C
_MpiCurrent_Object=MibScalar
mpiCurrent=_MpiCurrent_Object((1,3,6,1,4,1,21728,3,5,1),_MpiCurrent_Type())
mpiCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:mpiCurrent.setStatus(_A)
class _MpiVolt_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MpiVolt_Type.__name__=_C
_MpiVolt_Object=MibScalar
mpiVolt=_MpiVolt_Object((1,3,6,1,4,1,21728,3,5,2),_MpiVolt_Type())
mpiVolt.setMaxAccess(_B)
if mibBuilder.loadTexts:mpiVolt.setStatus(_A)
class _MpiActivePower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MpiActivePower_Type.__name__=_C
_MpiActivePower_Object=MibScalar
mpiActivePower=_MpiActivePower_Object((1,3,6,1,4,1,21728,3,5,3),_MpiActivePower_Type())
mpiActivePower.setMaxAccess(_B)
if mibBuilder.loadTexts:mpiActivePower.setStatus(_A)
class _MpiApparentPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MpiApparentPower_Type.__name__=_C
_MpiApparentPower_Object=MibScalar
mpiApparentPower=_MpiApparentPower_Object((1,3,6,1,4,1,21728,3,5,4),_MpiApparentPower_Type())
mpiApparentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:mpiApparentPower.setStatus(_A)
class _MpiPowerFactor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MpiPowerFactor_Type.__name__=_C
_MpiPowerFactor_Object=MibScalar
mpiPowerFactor=_MpiPowerFactor_Object((1,3,6,1,4,1,21728,3,5,5),_MpiPowerFactor_Type())
mpiPowerFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:mpiPowerFactor.setStatus(_A)
class _MpiAcFrequency_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MpiAcFrequency_Type.__name__=_C
_MpiAcFrequency_Object=MibScalar
mpiAcFrequency=_MpiAcFrequency_Object((1,3,6,1,4,1,21728,3,5,6),_MpiAcFrequency_Type())
mpiAcFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:mpiAcFrequency.setStatus(_A)
class _MpiAcKwh_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MpiAcKwh_Type.__name__=_C
_MpiAcKwh_Object=MibScalar
mpiAcKwh=_MpiAcKwh_Object((1,3,6,1,4,1,21728,3,5,7),_MpiAcKwh_Type())
mpiAcKwh.setMaxAccess(_B)
if mibBuilder.loadTexts:mpiAcKwh.setStatus(_A)
class _MpiAcKwhStartEPOCH_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MpiAcKwhStartEPOCH_Type.__name__=_C
_MpiAcKwhStartEPOCH_Object=MibScalar
mpiAcKwhStartEPOCH=_MpiAcKwhStartEPOCH_Object((1,3,6,1,4,1,21728,3,5,8),_MpiAcKwhStartEPOCH_Type())
mpiAcKwhStartEPOCH.setMaxAccess(_B)
if mibBuilder.loadTexts:mpiAcKwhStartEPOCH.setStatus(_A)
_TrapEvent_ObjectIdentity=ObjectIdentity
trapEvent=_TrapEvent_ObjectIdentity((1,3,6,1,4,1,21728,3,100))
_Event_ObjectIdentity=ObjectIdentity
event=_Event_ObjectIdentity((1,3,6,1,4,1,21728,3,100,0))
outletStatusEvent=NotificationType((1,3,6,1,4,1,21728,3,100,0,1))
outletStatusEvent.setObjects(*((_D,_F),(_D,_H),(_D,_I)))
if mibBuilder.loadTexts:outletStatusEvent.setStatus(_A)
outletGroupStatusEvent=NotificationType((1,3,6,1,4,1,21728,3,100,0,2))
outletGroupStatusEvent.setObjects(*((_D,_F),(_D,_I)))
if mibBuilder.loadTexts:outletGroupStatusEvent.setStatus(_A)
autoPingRebootEvent=NotificationType((1,3,6,1,4,1,21728,3,100,0,3))
autoPingRebootEvent.setObjects(*((_D,_F),(_D,_H)))
if mibBuilder.loadTexts:autoPingRebootEvent.setStatus(_A)
temperatureAlarmEvent=NotificationType((1,3,6,1,4,1,21728,3,100,0,4))
temperatureAlarmEvent.setObjects((_D,_F))
if mibBuilder.loadTexts:temperatureAlarmEvent.setStatus(_A)
temperatureControlledOutletEvent=NotificationType((1,3,6,1,4,1,21728,3,100,0,5))
temperatureControlledOutletEvent.setObjects(*((_D,_F),(_D,_H)))
if mibBuilder.loadTexts:temperatureControlledOutletEvent.setStatus(_A)
systemPowerUpEvent=NotificationType((1,3,6,1,4,1,21728,3,100,0,6))
systemPowerUpEvent.setObjects((_D,_F))
if mibBuilder.loadTexts:systemPowerUpEvent.setStatus(_A)
kwhOverLimitEvent=NotificationType((1,3,6,1,4,1,21728,3,100,0,7))
kwhOverLimitEvent.setObjects(*((_D,_F),(_D,_H),(_D,_K),(_D,_L)))
if mibBuilder.loadTexts:kwhOverLimitEvent.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'synaccess':synaccess,'synSys':synSys,'systemDescr':systemDescr,'systemModel':systemModel,_F:systemName,'powerOutletNum':powerOutletNum,'serialPortNum':serialPortNum,'systemUpTime':systemUpTime,'swVersion':swVersion,'acCurrentSensorNumber':acCurrentSensorNumber,'temperatureProbe':temperatureProbe,'acMPIModNumber':acMPIModNumber,'outletOpTables':outletOpTables,'outletTable':outletTable,'outletEntry':outletEntry,_J:outletIndex,_H:outletName,_I:outletStatus,'outletAction':outletAction,'outletCurrentDraw':outletCurrentDraw,'enviroTable':enviroTable,'currentAlarmThreshold':currentAlarmThreshold,'currentDrawStatus1':currentDrawStatus1,'currentDrawStatus2':currentDrawStatus2,'currentDrawMax1':currentDrawMax1,'currentDrawMax2':currentDrawMax2,'temperatureUpThreshold':temperatureUpThreshold,'temperatureLowThreshold':temperatureLowThreshold,'temperatureReading':temperatureReading,'trapSetting':trapSetting,'trapEnable':trapEnable,'trapRcvIP':trapRcvIP,'trapCommunity':trapCommunity,'energyStatus':energyStatus,'mpiCurrent':mpiCurrent,'mpiVolt':mpiVolt,'mpiActivePower':mpiActivePower,'mpiApparentPower':mpiApparentPower,'mpiPowerFactor':mpiPowerFactor,'mpiAcFrequency':mpiAcFrequency,_K:mpiAcKwh,_L:mpiAcKwhStartEPOCH,'trapEvent':trapEvent,'event':event,'outletStatusEvent':outletStatusEvent,'outletGroupStatusEvent':outletGroupStatusEvent,'autoPingRebootEvent':autoPingRebootEvent,'temperatureAlarmEvent':temperatureAlarmEvent,'temperatureControlledOutletEvent':temperatureControlledOutletEvent,'systemPowerUpEvent':systemPowerUpEvent,'kwhOverLimitEvent':kwhOverLimitEvent})