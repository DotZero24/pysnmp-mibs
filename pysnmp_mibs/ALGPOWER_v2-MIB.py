_C='DisplayString'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
_Algcom_ObjectIdentity=ObjectIdentity
algcom=_Algcom_ObjectIdentity((1,3,6,1,4,1,49136))
_UpsObjects_ObjectIdentity=ObjectIdentity
upsObjects=_UpsObjects_ObjectIdentity((1,3,6,1,4,1,49136,1))
_Output_ObjectIdentity=ObjectIdentity
output=_Output_ObjectIdentity((1,3,6,1,4,1,49136,1,1))
_OutputVoltage_Type=Integer32
_OutputVoltage_Object=MibScalar
outputVoltage=_OutputVoltage_Object((1,3,6,1,4,1,49136,1,1,1),_OutputVoltage_Type())
outputVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:outputVoltage.setStatus(_B)
_OutputCurrent_Type=Integer32
_OutputCurrent_Object=MibScalar
outputCurrent=_OutputCurrent_Object((1,3,6,1,4,1,49136,1,1,2),_OutputCurrent_Type())
outputCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:outputCurrent.setStatus(_B)
_OidNotUsed0_Type=Integer32
_OidNotUsed0_Object=MibScalar
oidNotUsed0=_OidNotUsed0_Object((1,3,6,1,4,1,49136,1,1,3),_OidNotUsed0_Type())
oidNotUsed0.setMaxAccess(_A)
if mibBuilder.loadTexts:oidNotUsed0.setStatus(_B)
_OidNotUsed1_Type=Integer32
_OidNotUsed1_Object=MibScalar
oidNotUsed1=_OidNotUsed1_Object((1,3,6,1,4,1,49136,1,1,4),_OidNotUsed1_Type())
oidNotUsed1.setMaxAccess(_A)
if mibBuilder.loadTexts:oidNotUsed1.setStatus(_B)
_Battery_ObjectIdentity=ObjectIdentity
battery=_Battery_ObjectIdentity((1,3,6,1,4,1,49136,1,2))
_BatteryVoltage_Type=Integer32
_BatteryVoltage_Object=MibScalar
batteryVoltage=_BatteryVoltage_Object((1,3,6,1,4,1,49136,1,2,1),_BatteryVoltage_Type())
batteryVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:batteryVoltage.setStatus(_B)
_BatteryCurrent_Type=Integer32
_BatteryCurrent_Object=MibScalar
batteryCurrent=_BatteryCurrent_Object((1,3,6,1,4,1,49136,1,2,2),_BatteryCurrent_Type())
batteryCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:batteryCurrent.setStatus(_B)
_ChargerStatus_Type=Integer32
_ChargerStatus_Object=MibScalar
chargerStatus=_ChargerStatus_Object((1,3,6,1,4,1,49136,1,2,3),_ChargerStatus_Type())
chargerStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:chargerStatus.setStatus(_B)
_Input_ObjectIdentity=ObjectIdentity
input=_Input_ObjectIdentity((1,3,6,1,4,1,49136,1,3))
_AlarmOnBattery_Type=Integer32
_AlarmOnBattery_Object=MibScalar
alarmOnBattery=_AlarmOnBattery_Object((1,3,6,1,4,1,49136,1,3,1),_AlarmOnBattery_Type())
alarmOnBattery.setMaxAccess(_A)
if mibBuilder.loadTexts:alarmOnBattery.setStatus(_B)
_AcFail_Type=Integer32
_AcFail_Object=MibScalar
acFail=_AcFail_Object((1,3,6,1,4,1,49136,1,3,2),_AcFail_Type())
acFail.setMaxAccess(_A)
if mibBuilder.loadTexts:acFail.setStatus(_B)
_BatteryCharging_Type=Integer32
_BatteryCharging_Object=MibScalar
batteryCharging=_BatteryCharging_Object((1,3,6,1,4,1,49136,1,3,3),_BatteryCharging_Type())
batteryCharging.setMaxAccess(_A)
if mibBuilder.loadTexts:batteryCharging.setStatus(_B)
_BatteryDischarging_Type=Integer32
_BatteryDischarging_Object=MibScalar
batteryDischarging=_BatteryDischarging_Object((1,3,6,1,4,1,49136,1,3,4),_BatteryDischarging_Type())
batteryDischarging.setMaxAccess(_A)
if mibBuilder.loadTexts:batteryDischarging.setStatus(_B)
_Overheat_Type=Integer32
_Overheat_Object=MibScalar
overheat=_Overheat_Object((1,3,6,1,4,1,49136,1,3,5),_Overheat_Type())
overheat.setMaxAccess(_A)
if mibBuilder.loadTexts:overheat.setStatus(_B)
_Overload_Type=Integer32
_Overload_Object=MibScalar
overload=_Overload_Object((1,3,6,1,4,1,49136,1,3,6),_Overload_Type())
overload.setMaxAccess(_A)
if mibBuilder.loadTexts:overload.setStatus(_B)
_FanAfail_Type=Integer32
_FanAfail_Object=MibScalar
fanAfail=_FanAfail_Object((1,3,6,1,4,1,49136,1,3,7),_FanAfail_Type())
fanAfail.setMaxAccess(_A)
if mibBuilder.loadTexts:fanAfail.setStatus(_B)
_FanBfail_Type=Integer32
_FanBfail_Object=MibScalar
fanBfail=_FanBfail_Object((1,3,6,1,4,1,49136,1,3,8),_FanBfail_Type())
fanBfail.setMaxAccess(_A)
if mibBuilder.loadTexts:fanBfail.setStatus(_B)
_OidNotUsed2_Type=Integer32
_OidNotUsed2_Object=MibScalar
oidNotUsed2=_OidNotUsed2_Object((1,3,6,1,4,1,49136,1,3,9),_OidNotUsed2_Type())
oidNotUsed2.setMaxAccess(_A)
if mibBuilder.loadTexts:oidNotUsed2.setStatus(_B)
_OidNotUsed3_Type=Integer32
_OidNotUsed3_Object=MibScalar
oidNotUsed3=_OidNotUsed3_Object((1,3,6,1,4,1,49136,1,3,10),_OidNotUsed3_Type())
oidNotUsed3.setMaxAccess(_A)
if mibBuilder.loadTexts:oidNotUsed3.setStatus(_B)
_UpTime_Type=Integer32
_UpTime_Object=MibScalar
upTime=_UpTime_Object((1,3,6,1,4,1,49136,1,3,11),_UpTime_Type())
upTime.setMaxAccess(_A)
if mibBuilder.loadTexts:upTime.setStatus(_B)
_Temperature_ObjectIdentity=ObjectIdentity
temperature=_Temperature_ObjectIdentity((1,3,6,1,4,1,49136,1,4))
_InnerTemperature_Type=Integer32
_InnerTemperature_Object=MibScalar
innerTemperature=_InnerTemperature_Object((1,3,6,1,4,1,49136,1,4,1),_InnerTemperature_Type())
innerTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:innerTemperature.setStatus(_B)
_OuterTemperature_Type=Integer32
_OuterTemperature_Object=MibScalar
outerTemperature=_OuterTemperature_Object((1,3,6,1,4,1,49136,1,4,2),_OuterTemperature_Type())
outerTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:outerTemperature.setStatus(_B)
_HeatSinkTemperature_Type=Integer32
_HeatSinkTemperature_Object=MibScalar
heatSinkTemperature=_HeatSinkTemperature_Object((1,3,6,1,4,1,49136,1,4,3),_HeatSinkTemperature_Type())
heatSinkTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:heatSinkTemperature.setStatus(_B)
_Watchdog_ObjectIdentity=ObjectIdentity
watchdog=_Watchdog_ObjectIdentity((1,3,6,1,4,1,49136,1,5))
_WatchdogPing1_Type=Integer32
_WatchdogPing1_Object=MibScalar
watchdogPing1=_WatchdogPing1_Object((1,3,6,1,4,1,49136,1,5,1),_WatchdogPing1_Type())
watchdogPing1.setMaxAccess(_A)
if mibBuilder.loadTexts:watchdogPing1.setStatus(_B)
_WatchdogPing2_Type=Integer32
_WatchdogPing2_Object=MibScalar
watchdogPing2=_WatchdogPing2_Object((1,3,6,1,4,1,49136,1,5,2),_WatchdogPing2_Type())
watchdogPing2.setMaxAccess(_A)
if mibBuilder.loadTexts:watchdogPing2.setStatus(_B)
_WatchdogPing3_Type=Integer32
_WatchdogPing3_Object=MibScalar
watchdogPing3=_WatchdogPing3_Object((1,3,6,1,4,1,49136,1,5,3),_WatchdogPing3_Type())
watchdogPing3.setMaxAccess(_A)
if mibBuilder.loadTexts:watchdogPing3.setStatus(_B)
_WatchdogPing4_Type=Integer32
_WatchdogPing4_Object=MibScalar
watchdogPing4=_WatchdogPing4_Object((1,3,6,1,4,1,49136,1,5,4),_WatchdogPing4_Type())
watchdogPing4.setMaxAccess(_A)
if mibBuilder.loadTexts:watchdogPing4.setStatus(_B)
_WatchdogPing5_Type=Integer32
_WatchdogPing5_Object=MibScalar
watchdogPing5=_WatchdogPing5_Object((1,3,6,1,4,1,49136,1,5,5),_WatchdogPing5_Type())
watchdogPing5.setMaxAccess(_A)
if mibBuilder.loadTexts:watchdogPing5.setStatus(_B)
_WatchdogPing6_Type=Integer32
_WatchdogPing6_Object=MibScalar
watchdogPing6=_WatchdogPing6_Object((1,3,6,1,4,1,49136,1,5,6),_WatchdogPing6_Type())
watchdogPing6.setMaxAccess(_A)
if mibBuilder.loadTexts:watchdogPing6.setStatus(_B)
_WatchdogPing7_Type=Integer32
_WatchdogPing7_Object=MibScalar
watchdogPing7=_WatchdogPing7_Object((1,3,6,1,4,1,49136,1,5,7),_WatchdogPing7_Type())
watchdogPing7.setMaxAccess(_A)
if mibBuilder.loadTexts:watchdogPing7.setStatus(_B)
_WatchdogPing8_Type=Integer32
_WatchdogPing8_Object=MibScalar
watchdogPing8=_WatchdogPing8_Object((1,3,6,1,4,1,49136,1,5,8),_WatchdogPing8_Type())
watchdogPing8.setMaxAccess(_A)
if mibBuilder.loadTexts:watchdogPing8.setStatus(_B)
_WatchdogPing9_Type=Integer32
_WatchdogPing9_Object=MibScalar
watchdogPing9=_WatchdogPing9_Object((1,3,6,1,4,1,49136,1,5,9),_WatchdogPing9_Type())
watchdogPing9.setMaxAccess(_A)
if mibBuilder.loadTexts:watchdogPing9.setStatus(_B)
_WatchdogPing10_Type=Integer32
_WatchdogPing10_Object=MibScalar
watchdogPing10=_WatchdogPing10_Object((1,3,6,1,4,1,49136,1,5,10),_WatchdogPing10_Type())
watchdogPing10.setMaxAccess(_A)
if mibBuilder.loadTexts:watchdogPing10.setStatus(_B)
_Supply_ObjectIdentity=ObjectIdentity
supply=_Supply_ObjectIdentity((1,3,6,1,4,1,49136,1,6))
_SupplyVoltage_Type=Integer32
_SupplyVoltage_Object=MibScalar
supplyVoltage=_SupplyVoltage_Object((1,3,6,1,4,1,49136,1,6,1),_SupplyVoltage_Type())
supplyVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:supplyVoltage.setStatus(_B)
_Installation_ObjectIdentity=ObjectIdentity
installation=_Installation_ObjectIdentity((1,3,6,1,4,1,49136,1,7))
class _PopName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(30,30));fixedLength=30
_PopName_Type.__name__=_C
_PopName_Object=MibScalar
popName=_PopName_Object((1,3,6,1,4,1,49136,1,7,1),_PopName_Type())
popName.setMaxAccess(_A)
if mibBuilder.loadTexts:popName.setStatus(_B)
class _FacilityAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(40,40));fixedLength=40
_FacilityAddr_Type.__name__=_C
_FacilityAddr_Object=MibScalar
facilityAddr=_FacilityAddr_Object((1,3,6,1,4,1,49136,1,7,2),_FacilityAddr_Type())
facilityAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:facilityAddr.setStatus(_B)
class _FacilityCity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(30,30));fixedLength=30
_FacilityCity_Type.__name__=_C
_FacilityCity_Object=MibScalar
facilityCity=_FacilityCity_Object((1,3,6,1,4,1,49136,1,7,3),_FacilityCity_Type())
facilityCity.setMaxAccess(_A)
if mibBuilder.loadTexts:facilityCity.setStatus(_B)
class _InstDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_InstDate_Type.__name__=_C
_InstDate_Object=MibScalar
instDate=_InstDate_Object((1,3,6,1,4,1,49136,1,7,4),_InstDate_Type())
instDate.setMaxAccess(_A)
if mibBuilder.loadTexts:instDate.setStatus(_B)
_BatCapacity_Type=Integer32
_BatCapacity_Object=MibScalar
batCapacity=_BatCapacity_Object((1,3,6,1,4,1,49136,1,7,5),_BatCapacity_Type())
batCapacity.setMaxAccess(_A)
if mibBuilder.loadTexts:batCapacity.setStatus(_B)
class _BatBrand_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(30,30));fixedLength=30
_BatBrand_Type.__name__=_C
_BatBrand_Object=MibScalar
batBrand=_BatBrand_Object((1,3,6,1,4,1,49136,1,7,6),_BatBrand_Type())
batBrand.setMaxAccess(_A)
if mibBuilder.loadTexts:batBrand.setStatus(_B)
class _BatInstDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_BatInstDate_Type.__name__=_C
_BatInstDate_Object=MibScalar
batInstDate=_BatInstDate_Object((1,3,6,1,4,1,49136,1,7,7),_BatInstDate_Type())
batInstDate.setMaxAccess(_A)
if mibBuilder.loadTexts:batInstDate.setStatus(_B)
class _RespPers_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(50,50));fixedLength=50
_RespPers_Type.__name__=_C
_RespPers_Object=MibScalar
respPers=_RespPers_Object((1,3,6,1,4,1,49136,1,7,8),_RespPers_Type())
respPers.setMaxAccess(_A)
if mibBuilder.loadTexts:respPers.setStatus(_B)
_Bat_tst_ObjectIdentity=ObjectIdentity
bat_tst=_Bat_tst_ObjectIdentity((1,3,6,1,4,1,49136,1,8))
class _Btst_date_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Btst_date_Type.__name__=_C
_Btst_date_Object=MibScalar
btst_date=_Btst_date_Object((1,3,6,1,4,1,49136,1,8,1),_Btst_date_Type())
btst_date.setMaxAccess(_A)
if mibBuilder.loadTexts:btst_date.setStatus(_B)
_Btst_status_Type=Integer32
_Btst_status_Object=MibScalar
btst_status=_Btst_status_Object((1,3,6,1,4,1,49136,1,8,2),_Btst_status_Type())
btst_status.setMaxAccess(_A)
if mibBuilder.loadTexts:btst_status.setStatus(_B)
_Btst_duration_Type=Integer32
_Btst_duration_Object=MibScalar
btst_duration=_Btst_duration_Object((1,3,6,1,4,1,49136,1,8,3),_Btst_duration_Type())
btst_duration.setMaxAccess(_A)
if mibBuilder.loadTexts:btst_duration.setStatus(_B)
_Btst_elapsed_Type=Integer32
_Btst_elapsed_Object=MibScalar
btst_elapsed=_Btst_elapsed_Object((1,3,6,1,4,1,49136,1,8,4),_Btst_elapsed_Type())
btst_elapsed.setMaxAccess(_A)
if mibBuilder.loadTexts:btst_elapsed.setStatus(_B)
_Btst_volt_i_Type=Integer32
_Btst_volt_i_Object=MibScalar
btst_volt_i=_Btst_volt_i_Object((1,3,6,1,4,1,49136,1,8,5),_Btst_volt_i_Type())
btst_volt_i.setMaxAccess(_A)
if mibBuilder.loadTexts:btst_volt_i.setStatus(_B)
_Btst_amp_i_Type=Integer32
_Btst_amp_i_Object=MibScalar
btst_amp_i=_Btst_amp_i_Object((1,3,6,1,4,1,49136,1,8,6),_Btst_amp_i_Type())
btst_amp_i.setMaxAccess(_A)
if mibBuilder.loadTexts:btst_amp_i.setStatus(_B)
_Btst_volt_f_Type=Integer32
_Btst_volt_f_Object=MibScalar
btst_volt_f=_Btst_volt_f_Object((1,3,6,1,4,1,49136,1,8,7),_Btst_volt_f_Type())
btst_volt_f.setMaxAccess(_A)
if mibBuilder.loadTexts:btst_volt_f.setStatus(_B)
_Btst_amp_f_Type=Integer32
_Btst_amp_f_Object=MibScalar
btst_amp_f=_Btst_amp_f_Object((1,3,6,1,4,1,49136,1,8,8),_Btst_amp_f_Type())
btst_amp_f.setMaxAccess(_A)
if mibBuilder.loadTexts:btst_amp_f.setStatus(_B)
mibBuilder.exportSymbols('ALGPOWER_v2-MIB',**{'algcom':algcom,'upsObjects':upsObjects,'output':output,'outputVoltage':outputVoltage,'outputCurrent':outputCurrent,'oidNotUsed0':oidNotUsed0,'oidNotUsed1':oidNotUsed1,'battery':battery,'batteryVoltage':batteryVoltage,'batteryCurrent':batteryCurrent,'chargerStatus':chargerStatus,'input':input,'alarmOnBattery':alarmOnBattery,'acFail':acFail,'batteryCharging':batteryCharging,'batteryDischarging':batteryDischarging,'overheat':overheat,'overload':overload,'fanAfail':fanAfail,'fanBfail':fanBfail,'oidNotUsed2':oidNotUsed2,'oidNotUsed3':oidNotUsed3,'upTime':upTime,'temperature':temperature,'innerTemperature':innerTemperature,'outerTemperature':outerTemperature,'heatSinkTemperature':heatSinkTemperature,'watchdog':watchdog,'watchdogPing1':watchdogPing1,'watchdogPing2':watchdogPing2,'watchdogPing3':watchdogPing3,'watchdogPing4':watchdogPing4,'watchdogPing5':watchdogPing5,'watchdogPing6':watchdogPing6,'watchdogPing7':watchdogPing7,'watchdogPing8':watchdogPing8,'watchdogPing9':watchdogPing9,'watchdogPing10':watchdogPing10,'supply':supply,'supplyVoltage':supplyVoltage,'installation':installation,'popName':popName,'facilityAddr':facilityAddr,'facilityCity':facilityCity,'instDate':instDate,'batCapacity':batCapacity,'batBrand':batBrand,'batInstDate':batInstDate,'respPers':respPers,'bat_tst':bat_tst,'btst_date':btst_date,'btst_status':btst_status,'btst_duration':btst_duration,'btst_elapsed':btst_elapsed,'btst_volt_i':btst_volt_i,'btst_amp_i':btst_amp_i,'btst_volt_f':btst_volt_f,'btst_amp_f':btst_amp_f})