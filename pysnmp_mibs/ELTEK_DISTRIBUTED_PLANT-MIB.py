_AU='alarmController8proginputTrap'
_AT='alarmController7proginputTrap'
_AS='alarmController6proginputTrap'
_AR='alarmController5proginputTrap'
_AQ='alarmController4proginputTrap'
_AP='alarmController3proginputTrap'
_AO='alarmController2proginputTrap'
_AN='alarmController1proginputTrap'
_AM='alarmBatteryBoostmodeEnteredTrap'
_AL='alarmBatteryTestmodeEnteredTrap'
_AK='alarmBatteryLifeEndedTrap'
_AJ='alarmMinorBatteryMidpointTrap'
_AI='alarmMajorBatteryMidpointTrap'
_AH='alarmMinorRectifierTrap'
_AG='alarmMajorRectifierTrap'
_AF='alarmDistributionBreakerOpenTrap'
_AE='alarmBatteryBreakerOpenTrap'
_AD='alarmACmainsTrap'
_AC='alarmLVD3openTrap'
_AB='alarmLVD2openTrap'
_AA='alarmLVD1openTrap'
_A9='alarmBatteryDisconnectOpenTrap'
_A8='alarmMinorBatteryHighTempTrap'
_A7='alarmMajorBatteryHighTempTrap'
_A6='alarmMinorLowBattVoltTrap'
_A5='alarmMajorLowBattVoltTrap'
_A4='alarmMinorHighBattVoltTrap'
_A3='alarmMajorHighBattVoltTrap'
_A2='inputUserConfigurable8'
_A1='inputUserConfigurable7'
_A0='inputUserConfigurable6'
_z='inputUserConfigurable5'
_y='inputUserConfigurable4'
_x='inputUserConfigurable3'
_w='inputUserConfigurable2'
_v='inputUserConfigurable1'
_u='alarmBatteryBoostmodeEntered'
_t='alarmBatteryTestmodeEntered'
_s='alarmBatteryLifeEnded'
_r='alarmMinorBatteryMidpoint'
_q='alarmMajorBatteryMidpoint'
_p='alarmMinorRectifier'
_o='alarmMajorRectifier'
_n='alarmDistributionBreakerOpen'
_m='alarmBatteryBreakerOpen'
_l='alarmACmains'
_k='alarmLVD3open'
_j='alarmLVD2open'
_i='alarmLVD1open'
_h='alarmBatteryDisconnectOpen'
_g='alarmMinorBatteryHighTemp'
_f='alarmMajorBatteryHighTemp'
_e='alarmMinorLowBattVolt'
_d='alarmMajorLowBattVolt'
_c='alarmMinorHighBattVolt'
_b='alarmMajorHighBattVolt'
_a='rectifierStatusID'
_Z='batteryBanksIndex'
_Y='closed'
_X='systemControlUnitIndex'
_W='accessible-for-notify'
_V='Volts AC'
_U='enabled'
_T='disconnect'
_S='connect'
_R='Amperes; i.e. 20 = 20 Amperes'
_Q='pushbutton'
_P='error'
_O='majorAlarm'
_N='minorAlarm'
_M='ok'
_L='enable'
_K='disabled'
_J='disable'
_I='1/100 Volt; i.e. 5400 = 54.00V'
_H='DisplayString'
_G='alarm'
_F='normal'
_E='read-write'
_D='ELTEK_DISTRIBUTED_PLANT-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltek,=mibBuilder.importSymbols('ELTEK-COMMON-MIB','eltek')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
_EltekDistributedPlant_ObjectIdentity=ObjectIdentity
eltekDistributedPlant=_EltekDistributedPlant_ObjectIdentity((1,3,6,1,4,1,12148,8))
_ControlSystem_ObjectIdentity=ObjectIdentity
controlSystem=_ControlSystem_ObjectIdentity((1,3,6,1,4,1,12148,8,1))
_SystemTime_ObjectIdentity=ObjectIdentity
systemTime=_SystemTime_ObjectIdentity((1,3,6,1,4,1,12148,8,1,1))
class _SystemTimeTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SystemTimeTime_Type.__name__=_H
_SystemTimeTime_Object=MibScalar
systemTimeTime=_SystemTimeTime_Object((1,3,6,1,4,1,12148,8,1,1,1),_SystemTimeTime_Type())
systemTimeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTimeTime.setStatus(_A)
class _SystemInfoRefresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),('refreshdata',1)))
_SystemInfoRefresh_Type.__name__=_B
_SystemInfoRefresh_Object=MibScalar
systemInfoRefresh=_SystemInfoRefresh_Object((1,3,6,1,4,1,12148,8,1,2),_SystemInfoRefresh_Type())
systemInfoRefresh.setMaxAccess(_E)
if mibBuilder.loadTexts:systemInfoRefresh.setStatus(_A)
class _SystemTrapRepeatRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_SystemTrapRepeatRate_Type.__name__=_B
_SystemTrapRepeatRate_Object=MibScalar
systemTrapRepeatRate=_SystemTrapRepeatRate_Object((1,3,6,1,4,1,12148,8,1,3),_SystemTrapRepeatRate_Type())
systemTrapRepeatRate.setMaxAccess(_E)
if mibBuilder.loadTexts:systemTrapRepeatRate.setStatus(_A)
class _SystemSendOffTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_SystemSendOffTrap_Type.__name__=_B
_SystemSendOffTrap_Object=MibScalar
systemSendOffTrap=_SystemSendOffTrap_Object((1,3,6,1,4,1,12148,8,1,4),_SystemSendOffTrap_Type())
systemSendOffTrap.setMaxAccess(_E)
if mibBuilder.loadTexts:systemSendOffTrap.setStatus(_A)
class _SystemNumOfControlUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_SystemNumOfControlUnits_Type.__name__=_B
_SystemNumOfControlUnits_Object=MibScalar
systemNumOfControlUnits=_SystemNumOfControlUnits_Object((1,3,6,1,4,1,12148,8,1,5),_SystemNumOfControlUnits_Type())
systemNumOfControlUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:systemNumOfControlUnits.setStatus(_A)
class _SystemControlUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SystemControlUnitIndex_Type.__name__=_B
_SystemControlUnitIndex_Object=MibScalar
systemControlUnitIndex=_SystemControlUnitIndex_Object((1,3,6,1,4,1,12148,8,1,6),_SystemControlUnitIndex_Type())
systemControlUnitIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:systemControlUnitIndex.setStatus(_A)
_SystemControlUnitTable_Object=MibTable
systemControlUnitTable=_SystemControlUnitTable_Object((1,3,6,1,4,1,12148,8,1,7))
if mibBuilder.loadTexts:systemControlUnitTable.setStatus(_A)
_SystemControlUnitEntry_Object=MibTableRow
systemControlUnitEntry=_SystemControlUnitEntry_Object((1,3,6,1,4,1,12148,8,1,7,1))
systemControlUnitEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:systemControlUnitEntry.setStatus(_A)
class _InputControlUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_InputControlUnitID_Type.__name__=_B
_InputControlUnitID_Object=MibTableColumn
inputControlUnitID=_InputControlUnitID_Object((1,3,6,1,4,1,12148,8,1,7,1,1),_InputControlUnitID_Type())
inputControlUnitID.setMaxAccess(_C)
if mibBuilder.loadTexts:inputControlUnitID.setStatus(_A)
class _InputUserConfigurable1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_InputUserConfigurable1_Type.__name__=_B
_InputUserConfigurable1_Object=MibTableColumn
inputUserConfigurable1=_InputUserConfigurable1_Object((1,3,6,1,4,1,12148,8,1,7,1,2),_InputUserConfigurable1_Type())
inputUserConfigurable1.setMaxAccess(_C)
if mibBuilder.loadTexts:inputUserConfigurable1.setStatus(_A)
class _InputUserConfigurable2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_InputUserConfigurable2_Type.__name__=_B
_InputUserConfigurable2_Object=MibTableColumn
inputUserConfigurable2=_InputUserConfigurable2_Object((1,3,6,1,4,1,12148,8,1,7,1,3),_InputUserConfigurable2_Type())
inputUserConfigurable2.setMaxAccess(_C)
if mibBuilder.loadTexts:inputUserConfigurable2.setStatus(_A)
class _InputUserConfigurable3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_InputUserConfigurable3_Type.__name__=_B
_InputUserConfigurable3_Object=MibTableColumn
inputUserConfigurable3=_InputUserConfigurable3_Object((1,3,6,1,4,1,12148,8,1,7,1,4),_InputUserConfigurable3_Type())
inputUserConfigurable3.setMaxAccess(_C)
if mibBuilder.loadTexts:inputUserConfigurable3.setStatus(_A)
class _InputUserConfigurable4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_InputUserConfigurable4_Type.__name__=_B
_InputUserConfigurable4_Object=MibTableColumn
inputUserConfigurable4=_InputUserConfigurable4_Object((1,3,6,1,4,1,12148,8,1,7,1,5),_InputUserConfigurable4_Type())
inputUserConfigurable4.setMaxAccess(_C)
if mibBuilder.loadTexts:inputUserConfigurable4.setStatus(_A)
class _InputUserConfigurable5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_InputUserConfigurable5_Type.__name__=_B
_InputUserConfigurable5_Object=MibTableColumn
inputUserConfigurable5=_InputUserConfigurable5_Object((1,3,6,1,4,1,12148,8,1,7,1,6),_InputUserConfigurable5_Type())
inputUserConfigurable5.setMaxAccess(_C)
if mibBuilder.loadTexts:inputUserConfigurable5.setStatus(_A)
class _InputUserConfigurable6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_InputUserConfigurable6_Type.__name__=_B
_InputUserConfigurable6_Object=MibTableColumn
inputUserConfigurable6=_InputUserConfigurable6_Object((1,3,6,1,4,1,12148,8,1,7,1,7),_InputUserConfigurable6_Type())
inputUserConfigurable6.setMaxAccess(_C)
if mibBuilder.loadTexts:inputUserConfigurable6.setStatus(_A)
class _InputUserConfigurable7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_InputUserConfigurable7_Type.__name__=_B
_InputUserConfigurable7_Object=MibTableColumn
inputUserConfigurable7=_InputUserConfigurable7_Object((1,3,6,1,4,1,12148,8,1,7,1,8),_InputUserConfigurable7_Type())
inputUserConfigurable7.setMaxAccess(_C)
if mibBuilder.loadTexts:inputUserConfigurable7.setStatus(_A)
class _InputUserConfigurable8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_InputUserConfigurable8_Type.__name__=_B
_InputUserConfigurable8_Object=MibTableColumn
inputUserConfigurable8=_InputUserConfigurable8_Object((1,3,6,1,4,1,12148,8,1,7,1,9),_InputUserConfigurable8_Type())
inputUserConfigurable8.setMaxAccess(_C)
if mibBuilder.loadTexts:inputUserConfigurable8.setStatus(_A)
class _InputUserConfigurable9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_InputUserConfigurable9_Type.__name__=_B
_InputUserConfigurable9_Object=MibTableColumn
inputUserConfigurable9=_InputUserConfigurable9_Object((1,3,6,1,4,1,12148,8,1,7,1,10),_InputUserConfigurable9_Type())
inputUserConfigurable9.setMaxAccess(_C)
if mibBuilder.loadTexts:inputUserConfigurable9.setStatus(_A)
class _InputUserConfigurable10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_InputUserConfigurable10_Type.__name__=_B
_InputUserConfigurable10_Object=MibTableColumn
inputUserConfigurable10=_InputUserConfigurable10_Object((1,3,6,1,4,1,12148,8,1,7,1,11),_InputUserConfigurable10_Type())
inputUserConfigurable10.setMaxAccess(_C)
if mibBuilder.loadTexts:inputUserConfigurable10.setStatus(_A)
class _SystemLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('linkdown',0),('linkup',1)))
_SystemLinkStatus_Type.__name__=_B
_SystemLinkStatus_Object=MibScalar
systemLinkStatus=_SystemLinkStatus_Object((1,3,6,1,4,1,12148,8,1,8),_SystemLinkStatus_Type())
systemLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:systemLinkStatus.setStatus(_A)
class _SystemInitiateEEPROM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),('start',1)))
_SystemInitiateEEPROM_Type.__name__=_B
_SystemInitiateEEPROM_Object=MibScalar
systemInitiateEEPROM=_SystemInitiateEEPROM_Object((1,3,6,1,4,1,12148,8,1,9),_SystemInitiateEEPROM_Type())
systemInitiateEEPROM.setMaxAccess(_E)
if mibBuilder.loadTexts:systemInitiateEEPROM.setStatus('deprecated')
_DcSystem_ObjectIdentity=ObjectIdentity
dcSystem=_DcSystem_ObjectIdentity((1,3,6,1,4,1,12148,8,2))
_DcPlant_ObjectIdentity=ObjectIdentity
dcPlant=_DcPlant_ObjectIdentity((1,3,6,1,4,1,12148,8,2,1))
_SystemSiteInfo_ObjectIdentity=ObjectIdentity
systemSiteInfo=_SystemSiteInfo_ObjectIdentity((1,3,6,1,4,1,12148,8,2,1,3))
class _SystemSiteInfoCustomer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SystemSiteInfoCustomer_Type.__name__=_H
_SystemSiteInfoCustomer_Object=MibScalar
systemSiteInfoCustomer=_SystemSiteInfoCustomer_Object((1,3,6,1,4,1,12148,8,2,1,3,1),_SystemSiteInfoCustomer_Type())
systemSiteInfoCustomer.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoCustomer.setStatus(_A)
class _SystemSiteInfoLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SystemSiteInfoLocation_Type.__name__=_H
_SystemSiteInfoLocation_Object=MibScalar
systemSiteInfoLocation=_SystemSiteInfoLocation_Object((1,3,6,1,4,1,12148,8,2,1,3,2),_SystemSiteInfoLocation_Type())
systemSiteInfoLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoLocation.setStatus(_A)
class _SystemSiteInfoMessage1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SystemSiteInfoMessage1_Type.__name__=_H
_SystemSiteInfoMessage1_Object=MibScalar
systemSiteInfoMessage1=_SystemSiteInfoMessage1_Object((1,3,6,1,4,1,12148,8,2,1,3,3),_SystemSiteInfoMessage1_Type())
systemSiteInfoMessage1.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoMessage1.setStatus(_A)
class _SystemSiteInfoMessage2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SystemSiteInfoMessage2_Type.__name__=_H
_SystemSiteInfoMessage2_Object=MibScalar
systemSiteInfoMessage2=_SystemSiteInfoMessage2_Object((1,3,6,1,4,1,12148,8,2,1,3,4),_SystemSiteInfoMessage2_Type())
systemSiteInfoMessage2.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoMessage2.setStatus(_A)
class _SystemSiteInfoInstalledDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SystemSiteInfoInstalledDate_Type.__name__=_H
_SystemSiteInfoInstalledDate_Object=MibScalar
systemSiteInfoInstalledDate=_SystemSiteInfoInstalledDate_Object((1,3,6,1,4,1,12148,8,2,1,3,5),_SystemSiteInfoInstalledDate_Type())
systemSiteInfoInstalledDate.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoInstalledDate.setStatus(_A)
class _SystemSiteInfoControllerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('al175',0),('al4000',1),('al6000',2),('smartpack',3)))
_SystemSiteInfoControllerType_Type.__name__=_B
_SystemSiteInfoControllerType_Object=MibScalar
systemSiteInfoControllerType=_SystemSiteInfoControllerType_Object((1,3,6,1,4,1,12148,8,2,1,3,6),_SystemSiteInfoControllerType_Type())
systemSiteInfoControllerType.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoControllerType.setStatus(_A)
class _SystemSiteInfoSystemSeriaNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SystemSiteInfoSystemSeriaNum_Type.__name__=_H
_SystemSiteInfoSystemSeriaNum_Object=MibScalar
systemSiteInfoSystemSeriaNum=_SystemSiteInfoSystemSeriaNum_Object((1,3,6,1,4,1,12148,8,2,1,3,7),_SystemSiteInfoSystemSeriaNum_Type())
systemSiteInfoSystemSeriaNum.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoSystemSeriaNum.setStatus(_A)
class _SystemSiteInfoControllerSeriaNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SystemSiteInfoControllerSeriaNum_Type.__name__=_H
_SystemSiteInfoControllerSeriaNum_Object=MibScalar
systemSiteInfoControllerSeriaNum=_SystemSiteInfoControllerSeriaNum_Object((1,3,6,1,4,1,12148,8,2,1,3,8),_SystemSiteInfoControllerSeriaNum_Type())
systemSiteInfoControllerSeriaNum.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoControllerSeriaNum.setStatus(_A)
class _SystemNominalVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('prs48v',0),('prs24v',1),('prs12v',2),('prs26v',3),('prs60v',4)))
_SystemNominalVoltage_Type.__name__=_B
_SystemNominalVoltage_Object=MibScalar
systemNominalVoltage=_SystemNominalVoltage_Object((1,3,6,1,4,1,12148,8,2,1,4),_SystemNominalVoltage_Type())
systemNominalVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:systemNominalVoltage.setStatus(_A)
class _SystemOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('floatvoltreg',0),('floattempcomp',1),('batteryboost',2),('batterytest',3)))
_SystemOperationalStatus_Type.__name__=_B
_SystemOperationalStatus_Object=MibScalar
systemOperationalStatus=_SystemOperationalStatus_Object((1,3,6,1,4,1,12148,8,2,2),_SystemOperationalStatus_Type())
systemOperationalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:systemOperationalStatus.setStatus(_A)
_Battery_ObjectIdentity=ObjectIdentity
battery=_Battery_ObjectIdentity((1,3,6,1,4,1,12148,8,3))
class _BatteryName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_BatteryName_Type.__name__=_H
_BatteryName_Object=MibScalar
batteryName=_BatteryName_Object((1,3,6,1,4,1,12148,8,3,1),_BatteryName_Type())
batteryName.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryName.setStatus(_A)
class _BatteryVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7500))
_BatteryVoltage_Type.__name__=_B
_BatteryVoltage_Object=MibScalar
batteryVoltage=_BatteryVoltage_Object((1,3,6,1,4,1,12148,8,3,2),_BatteryVoltage_Type())
batteryVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryVoltage.setStatus(_A)
if mibBuilder.loadTexts:batteryVoltage.setUnits(_I)
_BatteryCurrent_Type=Integer32
_BatteryCurrent_Object=MibScalar
batteryCurrent=_BatteryCurrent_Object((1,3,6,1,4,1,12148,8,3,3),_BatteryCurrent_Type())
batteryCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryCurrent.setStatus(_A)
if mibBuilder.loadTexts:batteryCurrent.setUnits(_R)
class _BatteryTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_BatteryTemp_Type.__name__=_B
_BatteryTemp_Object=MibScalar
batteryTemp=_BatteryTemp_Object((1,3,6,1,4,1,12148,8,3,4),_BatteryTemp_Type())
batteryTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryTemp.setStatus(_A)
if mibBuilder.loadTexts:batteryTemp.setUnits('1/10 Deg. C; i.e. 250 = 25.0 Deg. C.')
class _BatteryBreakerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),('open',1)))
_BatteryBreakerStatus_Type.__name__=_B
_BatteryBreakerStatus_Object=MibScalar
batteryBreakerStatus=_BatteryBreakerStatus_Object((1,3,6,1,4,1,12148,8,3,5),_BatteryBreakerStatus_Type())
batteryBreakerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBreakerStatus.setStatus(_A)
class _BatteryChargeCurrentLimitCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('deactivate',0),('activate',1)))
_BatteryChargeCurrentLimitCtrl_Type.__name__=_B
_BatteryChargeCurrentLimitCtrl_Object=MibScalar
batteryChargeCurrentLimitCtrl=_BatteryChargeCurrentLimitCtrl_Object((1,3,6,1,4,1,12148,8,3,6),_BatteryChargeCurrentLimitCtrl_Type())
batteryChargeCurrentLimitCtrl.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryChargeCurrentLimitCtrl.setStatus(_A)
class _BatteryChargeCurrentLimitValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2100))
_BatteryChargeCurrentLimitValue_Type.__name__=_B
_BatteryChargeCurrentLimitValue_Object=MibScalar
batteryChargeCurrentLimitValue=_BatteryChargeCurrentLimitValue_Object((1,3,6,1,4,1,12148,8,3,7),_BatteryChargeCurrentLimitValue_Type())
batteryChargeCurrentLimitValue.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryChargeCurrentLimitValue.setStatus(_A)
if mibBuilder.loadTexts:batteryChargeCurrentLimitValue.setUnits(_R)
class _BatteryTempCompEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_L,1)))
_BatteryTempCompEnable_Type.__name__=_B
_BatteryTempCompEnable_Object=MibScalar
batteryTempCompEnable=_BatteryTempCompEnable_Object((1,3,6,1,4,1,12148,8,3,8),_BatteryTempCompEnable_Type())
batteryTempCompEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryTempCompEnable.setStatus(_A)
class _BatteryFloatVoltConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4300,6000))
_BatteryFloatVoltConfig_Type.__name__=_B
_BatteryFloatVoltConfig_Object=MibScalar
batteryFloatVoltConfig=_BatteryFloatVoltConfig_Object((1,3,6,1,4,1,12148,8,3,9),_BatteryFloatVoltConfig_Type())
batteryFloatVoltConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryFloatVoltConfig.setStatus(_A)
if mibBuilder.loadTexts:batteryFloatVoltConfig.setUnits(_I)
class _BatteryEqualizeVoltConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4300,6000))
_BatteryEqualizeVoltConfig_Type.__name__=_B
_BatteryEqualizeVoltConfig_Object=MibScalar
batteryEqualizeVoltConfig=_BatteryEqualizeVoltConfig_Object((1,3,6,1,4,1,12148,8,3,10),_BatteryEqualizeVoltConfig_Type())
batteryEqualizeVoltConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryEqualizeVoltConfig.setStatus(_A)
if mibBuilder.loadTexts:batteryEqualizeVoltConfig.setUnits(_I)
_BatteryHighMajorAlarmVoltageConfig_Type=Integer32
_BatteryHighMajorAlarmVoltageConfig_Object=MibScalar
batteryHighMajorAlarmVoltageConfig=_BatteryHighMajorAlarmVoltageConfig_Object((1,3,6,1,4,1,12148,8,3,11),_BatteryHighMajorAlarmVoltageConfig_Type())
batteryHighMajorAlarmVoltageConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryHighMajorAlarmVoltageConfig.setStatus(_A)
_BatteryHighMinorAlarmVoltageConfig_Type=Integer32
_BatteryHighMinorAlarmVoltageConfig_Object=MibScalar
batteryHighMinorAlarmVoltageConfig=_BatteryHighMinorAlarmVoltageConfig_Object((1,3,6,1,4,1,12148,8,3,12),_BatteryHighMinorAlarmVoltageConfig_Type())
batteryHighMinorAlarmVoltageConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryHighMinorAlarmVoltageConfig.setStatus(_A)
if mibBuilder.loadTexts:batteryHighMinorAlarmVoltageConfig.setUnits(_I)
_BatteryLowMajorAlarmVoltageConfig_Type=Integer32
_BatteryLowMajorAlarmVoltageConfig_Object=MibScalar
batteryLowMajorAlarmVoltageConfig=_BatteryLowMajorAlarmVoltageConfig_Object((1,3,6,1,4,1,12148,8,3,13),_BatteryLowMajorAlarmVoltageConfig_Type())
batteryLowMajorAlarmVoltageConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryLowMajorAlarmVoltageConfig.setStatus(_A)
if mibBuilder.loadTexts:batteryLowMajorAlarmVoltageConfig.setUnits(_I)
_BatteryLowMinorAlarmVoltageConfig_Type=Integer32
_BatteryLowMinorAlarmVoltageConfig_Object=MibScalar
batteryLowMinorAlarmVoltageConfig=_BatteryLowMinorAlarmVoltageConfig_Object((1,3,6,1,4,1,12148,8,3,14),_BatteryLowMinorAlarmVoltageConfig_Type())
batteryLowMinorAlarmVoltageConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryLowMinorAlarmVoltageConfig.setStatus(_A)
if mibBuilder.loadTexts:batteryLowMinorAlarmVoltageConfig.setUnits(_I)
class _BatteryStartManualTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),('starttest',1),('stoptest',2)))
_BatteryStartManualTest_Type.__name__=_B
_BatteryStartManualTest_Object=MibScalar
batteryStartManualTest=_BatteryStartManualTest_Object((1,3,6,1,4,1,12148,8,3,15),_BatteryStartManualTest_Type())
batteryStartManualTest.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryStartManualTest.setStatus(_A)
class _BatteryStartManualBoost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),('startboost',1),('stopboost',2)))
_BatteryStartManualBoost_Type.__name__=_B
_BatteryStartManualBoost_Object=MibScalar
batteryStartManualBoost=_BatteryStartManualBoost_Object((1,3,6,1,4,1,12148,8,3,16),_BatteryStartManualBoost_Type())
batteryStartManualBoost.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryStartManualBoost.setStatus(_A)
_BatteryLVD_ObjectIdentity=ObjectIdentity
batteryLVD=_BatteryLVD_ObjectIdentity((1,3,6,1,4,1,12148,8,3,17))
class _BatteryLVDStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),(_T,1),(_J,2)))
_BatteryLVDStatus_Type.__name__=_B
_BatteryLVDStatus_Object=MibScalar
batteryLVDStatus=_BatteryLVDStatus_Object((1,3,6,1,4,1,12148,8,3,17,1),_BatteryLVDStatus_Type())
batteryLVDStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryLVDStatus.setStatus(_A)
class _BatteryLVDDisconnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_BatteryLVDDisconnectVoltage_Type.__name__=_B
_BatteryLVDDisconnectVoltage_Object=MibScalar
batteryLVDDisconnectVoltage=_BatteryLVDDisconnectVoltage_Object((1,3,6,1,4,1,12148,8,3,17,2),_BatteryLVDDisconnectVoltage_Type())
batteryLVDDisconnectVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryLVDDisconnectVoltage.setStatus(_A)
if mibBuilder.loadTexts:batteryLVDDisconnectVoltage.setUnits(_I)
class _BatteryLVDConnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_BatteryLVDConnectVoltage_Type.__name__=_B
_BatteryLVDConnectVoltage_Object=MibScalar
batteryLVDConnectVoltage=_BatteryLVDConnectVoltage_Object((1,3,6,1,4,1,12148,8,3,17,3),_BatteryLVDConnectVoltage_Type())
batteryLVDConnectVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryLVDConnectVoltage.setStatus(_A)
if mibBuilder.loadTexts:batteryLVDConnectVoltage.setUnits(_I)
_BatteryBanksNumofBanks_Type=Integer32
_BatteryBanksNumofBanks_Object=MibScalar
batteryBanksNumofBanks=_BatteryBanksNumofBanks_Object((1,3,6,1,4,1,12148,8,3,18),_BatteryBanksNumofBanks_Type())
batteryBanksNumofBanks.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksNumofBanks.setStatus(_A)
_BatteryBanks_ObjectIdentity=ObjectIdentity
batteryBanks=_BatteryBanks_ObjectIdentity((1,3,6,1,4,1,12148,8,3,19))
_BatterySymmetryDeltaLimitVoltage_Type=Integer32
_BatterySymmetryDeltaLimitVoltage_Object=MibScalar
batterySymmetryDeltaLimitVoltage=_BatterySymmetryDeltaLimitVoltage_Object((1,3,6,1,4,1,12148,8,3,19,1),_BatterySymmetryDeltaLimitVoltage_Type())
batterySymmetryDeltaLimitVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:batterySymmetryDeltaLimitVoltage.setStatus(_A)
class _BatteryBanksIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_BatteryBanksIndex_Type.__name__=_B
_BatteryBanksIndex_Object=MibScalar
batteryBanksIndex=_BatteryBanksIndex_Object((1,3,6,1,4,1,12148,8,3,19,2),_BatteryBanksIndex_Type())
batteryBanksIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:batteryBanksIndex.setStatus(_A)
_BatteryBanksTable_Object=MibTable
batteryBanksTable=_BatteryBanksTable_Object((1,3,6,1,4,1,12148,8,3,19,3))
if mibBuilder.loadTexts:batteryBanksTable.setStatus(_A)
_BatteryBanksEntry_Object=MibTableRow
batteryBanksEntry=_BatteryBanksEntry_Object((1,3,6,1,4,1,12148,8,3,19,3,1))
batteryBanksEntry.setIndexNames((0,_D,_Z))
if mibBuilder.loadTexts:batteryBanksEntry.setStatus(_A)
class _BatteryBankID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BatteryBankID_Type.__name__=_B
_BatteryBankID_Object=MibTableColumn
batteryBankID=_BatteryBankID_Object((1,3,6,1,4,1,12148,8,3,19,3,1,1),_BatteryBankID_Type())
batteryBankID.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBankID.setStatus(_A)
class _BatteryBanksSymmetry1enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_L,1)))
_BatteryBanksSymmetry1enable_Type.__name__=_B
_BatteryBanksSymmetry1enable_Object=MibTableColumn
batteryBanksSymmetry1enable=_BatteryBanksSymmetry1enable_Object((1,3,6,1,4,1,12148,8,3,19,3,1,2),_BatteryBanksSymmetry1enable_Type())
batteryBanksSymmetry1enable.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryBanksSymmetry1enable.setStatus(_A)
class _BatteryBanksSymmetry1status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2),(_K,3),(_P,4)))
_BatteryBanksSymmetry1status_Type.__name__=_B
_BatteryBanksSymmetry1status_Object=MibTableColumn
batteryBanksSymmetry1status=_BatteryBanksSymmetry1status_Object((1,3,6,1,4,1,12148,8,3,19,3,1,3),_BatteryBanksSymmetry1status_Type())
batteryBanksSymmetry1status.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry1status.setStatus(_A)
_BatteryBanksSymmetry1deltaVoltage_Type=Integer32
_BatteryBanksSymmetry1deltaVoltage_Object=MibTableColumn
batteryBanksSymmetry1deltaVoltage=_BatteryBanksSymmetry1deltaVoltage_Object((1,3,6,1,4,1,12148,8,3,19,3,1,4),_BatteryBanksSymmetry1deltaVoltage_Type())
batteryBanksSymmetry1deltaVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry1deltaVoltage.setStatus(_A)
class _BatteryBanksSymmetry2enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_L,1)))
_BatteryBanksSymmetry2enable_Type.__name__=_B
_BatteryBanksSymmetry2enable_Object=MibTableColumn
batteryBanksSymmetry2enable=_BatteryBanksSymmetry2enable_Object((1,3,6,1,4,1,12148,8,3,19,3,1,5),_BatteryBanksSymmetry2enable_Type())
batteryBanksSymmetry2enable.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryBanksSymmetry2enable.setStatus(_A)
class _BatteryBanksSymmetry2status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2),(_K,3),(_P,4)))
_BatteryBanksSymmetry2status_Type.__name__=_B
_BatteryBanksSymmetry2status_Object=MibTableColumn
batteryBanksSymmetry2status=_BatteryBanksSymmetry2status_Object((1,3,6,1,4,1,12148,8,3,19,3,1,6),_BatteryBanksSymmetry2status_Type())
batteryBanksSymmetry2status.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry2status.setStatus(_A)
_BatteryBanksSymmetry2deltaVoltage_Type=Integer32
_BatteryBanksSymmetry2deltaVoltage_Object=MibTableColumn
batteryBanksSymmetry2deltaVoltage=_BatteryBanksSymmetry2deltaVoltage_Object((1,3,6,1,4,1,12148,8,3,19,3,1,7),_BatteryBanksSymmetry2deltaVoltage_Type())
batteryBanksSymmetry2deltaVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry2deltaVoltage.setStatus(_A)
class _BatteryBanksSymmetry3enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_L,1)))
_BatteryBanksSymmetry3enable_Type.__name__=_B
_BatteryBanksSymmetry3enable_Object=MibTableColumn
batteryBanksSymmetry3enable=_BatteryBanksSymmetry3enable_Object((1,3,6,1,4,1,12148,8,3,19,3,1,8),_BatteryBanksSymmetry3enable_Type())
batteryBanksSymmetry3enable.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryBanksSymmetry3enable.setStatus(_A)
class _BatteryBanksSymmetry3status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2),(_K,3),(_P,4)))
_BatteryBanksSymmetry3status_Type.__name__=_B
_BatteryBanksSymmetry3status_Object=MibTableColumn
batteryBanksSymmetry3status=_BatteryBanksSymmetry3status_Object((1,3,6,1,4,1,12148,8,3,19,3,1,9),_BatteryBanksSymmetry3status_Type())
batteryBanksSymmetry3status.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry3status.setStatus(_A)
_BatteryBanksSymmetry3deltaVoltage_Type=Integer32
_BatteryBanksSymmetry3deltaVoltage_Object=MibTableColumn
batteryBanksSymmetry3deltaVoltage=_BatteryBanksSymmetry3deltaVoltage_Object((1,3,6,1,4,1,12148,8,3,19,3,1,10),_BatteryBanksSymmetry3deltaVoltage_Type())
batteryBanksSymmetry3deltaVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry3deltaVoltage.setStatus(_A)
class _BatteryBanksSymmetry4enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_L,1)))
_BatteryBanksSymmetry4enable_Type.__name__=_B
_BatteryBanksSymmetry4enable_Object=MibTableColumn
batteryBanksSymmetry4enable=_BatteryBanksSymmetry4enable_Object((1,3,6,1,4,1,12148,8,3,19,3,1,11),_BatteryBanksSymmetry4enable_Type())
batteryBanksSymmetry4enable.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryBanksSymmetry4enable.setStatus(_A)
class _BatteryBanksSymmetry4status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2),(_K,3),(_P,4)))
_BatteryBanksSymmetry4status_Type.__name__=_B
_BatteryBanksSymmetry4status_Object=MibTableColumn
batteryBanksSymmetry4status=_BatteryBanksSymmetry4status_Object((1,3,6,1,4,1,12148,8,3,19,3,1,12),_BatteryBanksSymmetry4status_Type())
batteryBanksSymmetry4status.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry4status.setStatus(_A)
_BatteryBanksSymmetry4deltaVoltage_Type=Integer32
_BatteryBanksSymmetry4deltaVoltage_Object=MibTableColumn
batteryBanksSymmetry4deltaVoltage=_BatteryBanksSymmetry4deltaVoltage_Object((1,3,6,1,4,1,12148,8,3,19,3,1,13),_BatteryBanksSymmetry4deltaVoltage_Type())
batteryBanksSymmetry4deltaVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry4deltaVoltage.setStatus(_A)
class _BatteryBanksSymmetry5enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_L,1)))
_BatteryBanksSymmetry5enable_Type.__name__=_B
_BatteryBanksSymmetry5enable_Object=MibTableColumn
batteryBanksSymmetry5enable=_BatteryBanksSymmetry5enable_Object((1,3,6,1,4,1,12148,8,3,19,3,1,14),_BatteryBanksSymmetry5enable_Type())
batteryBanksSymmetry5enable.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryBanksSymmetry5enable.setStatus(_A)
class _BatteryBanksSymmetry5status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2),(_K,3),(_P,4)))
_BatteryBanksSymmetry5status_Type.__name__=_B
_BatteryBanksSymmetry5status_Object=MibTableColumn
batteryBanksSymmetry5status=_BatteryBanksSymmetry5status_Object((1,3,6,1,4,1,12148,8,3,19,3,1,15),_BatteryBanksSymmetry5status_Type())
batteryBanksSymmetry5status.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry5status.setStatus(_A)
_BatteryBanksSymmetry5deltaVoltage_Type=Integer32
_BatteryBanksSymmetry5deltaVoltage_Object=MibTableColumn
batteryBanksSymmetry5deltaVoltage=_BatteryBanksSymmetry5deltaVoltage_Object((1,3,6,1,4,1,12148,8,3,19,3,1,16),_BatteryBanksSymmetry5deltaVoltage_Type())
batteryBanksSymmetry5deltaVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry5deltaVoltage.setStatus(_A)
class _BatteryBanksSymmetry6enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_L,1)))
_BatteryBanksSymmetry6enable_Type.__name__=_B
_BatteryBanksSymmetry6enable_Object=MibTableColumn
batteryBanksSymmetry6enable=_BatteryBanksSymmetry6enable_Object((1,3,6,1,4,1,12148,8,3,19,3,1,17),_BatteryBanksSymmetry6enable_Type())
batteryBanksSymmetry6enable.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryBanksSymmetry6enable.setStatus(_A)
class _BatteryBanksSymmetry6status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2),(_K,3),(_P,4)))
_BatteryBanksSymmetry6status_Type.__name__=_B
_BatteryBanksSymmetry6status_Object=MibTableColumn
batteryBanksSymmetry6status=_BatteryBanksSymmetry6status_Object((1,3,6,1,4,1,12148,8,3,19,3,1,18),_BatteryBanksSymmetry6status_Type())
batteryBanksSymmetry6status.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry6status.setStatus(_A)
_BatteryBanksSymmetry6deltaVoltage_Type=Integer32
_BatteryBanksSymmetry6deltaVoltage_Object=MibTableColumn
batteryBanksSymmetry6deltaVoltage=_BatteryBanksSymmetry6deltaVoltage_Object((1,3,6,1,4,1,12148,8,3,19,3,1,19),_BatteryBanksSymmetry6deltaVoltage_Type())
batteryBanksSymmetry6deltaVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry6deltaVoltage.setStatus(_A)
class _BatteryBanksSymmetry7enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_L,1)))
_BatteryBanksSymmetry7enable_Type.__name__=_B
_BatteryBanksSymmetry7enable_Object=MibTableColumn
batteryBanksSymmetry7enable=_BatteryBanksSymmetry7enable_Object((1,3,6,1,4,1,12148,8,3,19,3,1,20),_BatteryBanksSymmetry7enable_Type())
batteryBanksSymmetry7enable.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryBanksSymmetry7enable.setStatus(_A)
class _BatteryBanksSymmetry7status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2),(_K,3),(_P,4)))
_BatteryBanksSymmetry7status_Type.__name__=_B
_BatteryBanksSymmetry7status_Object=MibTableColumn
batteryBanksSymmetry7status=_BatteryBanksSymmetry7status_Object((1,3,6,1,4,1,12148,8,3,19,3,1,21),_BatteryBanksSymmetry7status_Type())
batteryBanksSymmetry7status.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry7status.setStatus(_A)
_BatteryBanksSymmetry7deltaVoltage_Type=Integer32
_BatteryBanksSymmetry7deltaVoltage_Object=MibTableColumn
batteryBanksSymmetry7deltaVoltage=_BatteryBanksSymmetry7deltaVoltage_Object((1,3,6,1,4,1,12148,8,3,19,3,1,22),_BatteryBanksSymmetry7deltaVoltage_Type())
batteryBanksSymmetry7deltaVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry7deltaVoltage.setStatus(_A)
class _BatteryBanksSymmetry8enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_L,1)))
_BatteryBanksSymmetry8enable_Type.__name__=_B
_BatteryBanksSymmetry8enable_Object=MibTableColumn
batteryBanksSymmetry8enable=_BatteryBanksSymmetry8enable_Object((1,3,6,1,4,1,12148,8,3,19,3,1,23),_BatteryBanksSymmetry8enable_Type())
batteryBanksSymmetry8enable.setMaxAccess(_E)
if mibBuilder.loadTexts:batteryBanksSymmetry8enable.setStatus(_A)
class _BatteryBanksSymmetry8status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2),(_K,3),(_P,4)))
_BatteryBanksSymmetry8status_Type.__name__=_B
_BatteryBanksSymmetry8status_Object=MibTableColumn
batteryBanksSymmetry8status=_BatteryBanksSymmetry8status_Object((1,3,6,1,4,1,12148,8,3,19,3,1,24),_BatteryBanksSymmetry8status_Type())
batteryBanksSymmetry8status.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry8status.setStatus(_A)
_BatteryBanksSymmetry8deltaVoltage_Type=Integer32
_BatteryBanksSymmetry8deltaVoltage_Object=MibTableColumn
batteryBanksSymmetry8deltaVoltage=_BatteryBanksSymmetry8deltaVoltage_Object((1,3,6,1,4,1,12148,8,3,19,3,1,25),_BatteryBanksSymmetry8deltaVoltage_Type())
batteryBanksSymmetry8deltaVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBanksSymmetry8deltaVoltage.setStatus(_A)
_LoadDistribution_ObjectIdentity=ObjectIdentity
loadDistribution=_LoadDistribution_ObjectIdentity((1,3,6,1,4,1,12148,8,4))
_LoadDistributionCurrent_Type=Integer32
_LoadDistributionCurrent_Object=MibScalar
loadDistributionCurrent=_LoadDistributionCurrent_Object((1,3,6,1,4,1,12148,8,4,1),_LoadDistributionCurrent_Type())
loadDistributionCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:loadDistributionCurrent.setStatus(_A)
if mibBuilder.loadTexts:loadDistributionCurrent.setUnits(_R)
class _LoadDistributionBreakerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),('open',1)))
_LoadDistributionBreakerStatus_Type.__name__=_B
_LoadDistributionBreakerStatus_Object=MibScalar
loadDistributionBreakerStatus=_LoadDistributionBreakerStatus_Object((1,3,6,1,4,1,12148,8,4,2),_LoadDistributionBreakerStatus_Type())
loadDistributionBreakerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:loadDistributionBreakerStatus.setStatus(_A)
_LoadDistributionLVDStatus_ObjectIdentity=ObjectIdentity
loadDistributionLVDStatus=_LoadDistributionLVDStatus_ObjectIdentity((1,3,6,1,4,1,12148,8,4,3))
class _LoadLVD1EnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_U,1)))
_LoadLVD1EnableStatus_Type.__name__=_B
_LoadLVD1EnableStatus_Object=MibScalar
loadLVD1EnableStatus=_LoadLVD1EnableStatus_Object((1,3,6,1,4,1,12148,8,4,3,1),_LoadLVD1EnableStatus_Type())
loadLVD1EnableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:loadLVD1EnableStatus.setStatus(_A)
class _LoadLVD1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),(_T,1),(_J,2)))
_LoadLVD1Status_Type.__name__=_B
_LoadLVD1Status_Object=MibScalar
loadLVD1Status=_LoadLVD1Status_Object((1,3,6,1,4,1,12148,8,4,3,2),_LoadLVD1Status_Type())
loadLVD1Status.setMaxAccess(_C)
if mibBuilder.loadTexts:loadLVD1Status.setStatus(_A)
class _LoadLVD1ConnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_LoadLVD1ConnectVoltage_Type.__name__=_B
_LoadLVD1ConnectVoltage_Object=MibScalar
loadLVD1ConnectVoltage=_LoadLVD1ConnectVoltage_Object((1,3,6,1,4,1,12148,8,4,3,3),_LoadLVD1ConnectVoltage_Type())
loadLVD1ConnectVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:loadLVD1ConnectVoltage.setStatus(_A)
if mibBuilder.loadTexts:loadLVD1ConnectVoltage.setUnits(_I)
class _LoadLVD1DisconnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_LoadLVD1DisconnectVoltage_Type.__name__=_B
_LoadLVD1DisconnectVoltage_Object=MibScalar
loadLVD1DisconnectVoltage=_LoadLVD1DisconnectVoltage_Object((1,3,6,1,4,1,12148,8,4,3,4),_LoadLVD1DisconnectVoltage_Type())
loadLVD1DisconnectVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:loadLVD1DisconnectVoltage.setStatus(_A)
if mibBuilder.loadTexts:loadLVD1DisconnectVoltage.setUnits(_I)
class _LoadLVD2EnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_U,1)))
_LoadLVD2EnableStatus_Type.__name__=_B
_LoadLVD2EnableStatus_Object=MibScalar
loadLVD2EnableStatus=_LoadLVD2EnableStatus_Object((1,3,6,1,4,1,12148,8,4,3,5),_LoadLVD2EnableStatus_Type())
loadLVD2EnableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:loadLVD2EnableStatus.setStatus(_A)
class _LoadLVD2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),(_T,1),(_J,2)))
_LoadLVD2Status_Type.__name__=_B
_LoadLVD2Status_Object=MibScalar
loadLVD2Status=_LoadLVD2Status_Object((1,3,6,1,4,1,12148,8,4,3,6),_LoadLVD2Status_Type())
loadLVD2Status.setMaxAccess(_C)
if mibBuilder.loadTexts:loadLVD2Status.setStatus(_A)
class _LoadLVD2ConnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_LoadLVD2ConnectVoltage_Type.__name__=_B
_LoadLVD2ConnectVoltage_Object=MibScalar
loadLVD2ConnectVoltage=_LoadLVD2ConnectVoltage_Object((1,3,6,1,4,1,12148,8,4,3,7),_LoadLVD2ConnectVoltage_Type())
loadLVD2ConnectVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:loadLVD2ConnectVoltage.setStatus(_A)
class _LoadLVD2DisconnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_LoadLVD2DisconnectVoltage_Type.__name__=_B
_LoadLVD2DisconnectVoltage_Object=MibScalar
loadLVD2DisconnectVoltage=_LoadLVD2DisconnectVoltage_Object((1,3,6,1,4,1,12148,8,4,3,8),_LoadLVD2DisconnectVoltage_Type())
loadLVD2DisconnectVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:loadLVD2DisconnectVoltage.setStatus(_A)
if mibBuilder.loadTexts:loadLVD2DisconnectVoltage.setUnits(_I)
class _LoadLVD3EnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_U,1)))
_LoadLVD3EnableStatus_Type.__name__=_B
_LoadLVD3EnableStatus_Object=MibScalar
loadLVD3EnableStatus=_LoadLVD3EnableStatus_Object((1,3,6,1,4,1,12148,8,4,3,9),_LoadLVD3EnableStatus_Type())
loadLVD3EnableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:loadLVD3EnableStatus.setStatus(_A)
class _LoadLVD3Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),(_T,1),(_J,2)))
_LoadLVD3Status_Type.__name__=_B
_LoadLVD3Status_Object=MibScalar
loadLVD3Status=_LoadLVD3Status_Object((1,3,6,1,4,1,12148,8,4,3,10),_LoadLVD3Status_Type())
loadLVD3Status.setMaxAccess(_C)
if mibBuilder.loadTexts:loadLVD3Status.setStatus(_A)
class _LoadLVD3ConnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_LoadLVD3ConnectVoltage_Type.__name__=_B
_LoadLVD3ConnectVoltage_Object=MibScalar
loadLVD3ConnectVoltage=_LoadLVD3ConnectVoltage_Object((1,3,6,1,4,1,12148,8,4,3,11),_LoadLVD3ConnectVoltage_Type())
loadLVD3ConnectVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:loadLVD3ConnectVoltage.setStatus(_A)
class _LoadLVD3DisconnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_LoadLVD3DisconnectVoltage_Type.__name__=_B
_LoadLVD3DisconnectVoltage_Object=MibScalar
loadLVD3DisconnectVoltage=_LoadLVD3DisconnectVoltage_Object((1,3,6,1,4,1,12148,8,4,3,12),_LoadLVD3DisconnectVoltage_Type())
loadLVD3DisconnectVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:loadLVD3DisconnectVoltage.setStatus(_A)
if mibBuilder.loadTexts:loadLVD3DisconnectVoltage.setUnits(_I)
_Rectifier_ObjectIdentity=ObjectIdentity
rectifier=_Rectifier_ObjectIdentity((1,3,6,1,4,1,12148,8,5))
class _RectifierInstalledRectifiers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,101))
_RectifierInstalledRectifiers_Type.__name__=_B
_RectifierInstalledRectifiers_Object=MibScalar
rectifierInstalledRectifiers=_RectifierInstalledRectifiers_Object((1,3,6,1,4,1,12148,8,5,1),_RectifierInstalledRectifiers_Type())
rectifierInstalledRectifiers.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierInstalledRectifiers.setStatus(_A)
class _RectifierRectifiersActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,101))
_RectifierRectifiersActive_Type.__name__=_B
_RectifierRectifiersActive_Object=MibScalar
rectifierRectifiersActive=_RectifierRectifiersActive_Object((1,3,6,1,4,1,12148,8,5,2),_RectifierRectifiersActive_Type())
rectifierRectifiersActive.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierRectifiersActive.setStatus(_A)
_RectifierTotalCurrent_Type=Integer32
_RectifierTotalCurrent_Object=MibScalar
rectifierTotalCurrent=_RectifierTotalCurrent_Object((1,3,6,1,4,1,12148,8,5,3),_RectifierTotalCurrent_Type())
rectifierTotalCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierTotalCurrent.setStatus(_A)
if mibBuilder.loadTexts:rectifierTotalCurrent.setUnits(_R)
class _RectifierUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RectifierUtilization_Type.__name__=_B
_RectifierUtilization_Object=MibScalar
rectifierUtilization=_RectifierUtilization_Object((1,3,6,1,4,1,12148,8,5,4),_RectifierUtilization_Type())
rectifierUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierUtilization.setStatus(_A)
_RectifierStatus_ObjectIdentity=ObjectIdentity
rectifierStatus=_RectifierStatus_ObjectIdentity((1,3,6,1,4,1,12148,8,5,5))
class _RectifierStatusNoIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_RectifierStatusNoIndex_Type.__name__=_B
_RectifierStatusNoIndex_Object=MibScalar
rectifierStatusNoIndex=_RectifierStatusNoIndex_Object((1,3,6,1,4,1,12148,8,5,5,1),_RectifierStatusNoIndex_Type())
rectifierStatusNoIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rectifierStatusNoIndex.setStatus(_A)
_RectifierStatusTable_Object=MibTable
rectifierStatusTable=_RectifierStatusTable_Object((1,3,6,1,4,1,12148,8,5,5,2))
if mibBuilder.loadTexts:rectifierStatusTable.setStatus(_A)
_RectifierStatusEntry_Object=MibTableRow
rectifierStatusEntry=_RectifierStatusEntry_Object((1,3,6,1,4,1,12148,8,5,5,2,1))
rectifierStatusEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:rectifierStatusEntry.setStatus(_A)
class _RectifierStatusID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RectifierStatusID_Type.__name__=_B
_RectifierStatusID_Object=MibTableColumn
rectifierStatusID=_RectifierStatusID_Object((1,3,6,1,4,1,12148,8,5,5,2,1,1),_RectifierStatusID_Type())
rectifierStatusID.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusID.setStatus(_A)
class _RectifierStatusStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('absent',0),('active',1),('failed',2),('walkin',3),('disabledbycommand',4)))
_RectifierStatusStatus_Type.__name__=_B
_RectifierStatusStatus_Object=MibTableColumn
rectifierStatusStatus=_RectifierStatusStatus_Object((1,3,6,1,4,1,12148,8,5,5,2,1,2),_RectifierStatusStatus_Type())
rectifierStatusStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusStatus.setStatus(_A)
class _RectifierStatusOutputCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RectifierStatusOutputCurrent_Type.__name__=_B
_RectifierStatusOutputCurrent_Object=MibTableColumn
rectifierStatusOutputCurrent=_RectifierStatusOutputCurrent_Object((1,3,6,1,4,1,12148,8,5,5,2,1,3),_RectifierStatusOutputCurrent_Type())
rectifierStatusOutputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusOutputCurrent.setStatus(_A)
if mibBuilder.loadTexts:rectifierStatusOutputCurrent.setUnits('1/10 Amperes; i.e. 200 = 20 Amperes')
class _RectifierStatusOutputVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RectifierStatusOutputVoltage_Type.__name__=_B
_RectifierStatusOutputVoltage_Object=MibTableColumn
rectifierStatusOutputVoltage=_RectifierStatusOutputVoltage_Object((1,3,6,1,4,1,12148,8,5,5,2,1,4),_RectifierStatusOutputVoltage_Type())
rectifierStatusOutputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusOutputVoltage.setStatus(_A)
if mibBuilder.loadTexts:rectifierStatusOutputVoltage.setUnits(_I)
class _RectifierStatusTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RectifierStatusTemp_Type.__name__=_B
_RectifierStatusTemp_Object=MibTableColumn
rectifierStatusTemp=_RectifierStatusTemp_Object((1,3,6,1,4,1,12148,8,5,5,2,1,5),_RectifierStatusTemp_Type())
rectifierStatusTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusTemp.setStatus(_A)
if mibBuilder.loadTexts:rectifierStatusTemp.setUnits('Deg. C/10; i.e. 350 = 35.0 Deg. C')
class _RectifierStatusType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RectifierStatusType_Type.__name__=_H
_RectifierStatusType_Object=MibTableColumn
rectifierStatusType=_RectifierStatusType_Object((1,3,6,1,4,1,12148,8,5,5,2,1,6),_RectifierStatusType_Type())
rectifierStatusType.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusType.setStatus(_A)
class _RectifierStatusSKU_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RectifierStatusSKU_Type.__name__=_H
_RectifierStatusSKU_Object=MibTableColumn
rectifierStatusSKU=_RectifierStatusSKU_Object((1,3,6,1,4,1,12148,8,5,5,2,1,7),_RectifierStatusSKU_Type())
rectifierStatusSKU.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusSKU.setStatus(_A)
class _RectifierStatusSerialNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RectifierStatusSerialNo_Type.__name__=_H
_RectifierStatusSerialNo_Object=MibTableColumn
rectifierStatusSerialNo=_RectifierStatusSerialNo_Object((1,3,6,1,4,1,12148,8,5,5,2,1,8),_RectifierStatusSerialNo_Type())
rectifierStatusSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusSerialNo.setStatus(_A)
class _RectifierStatusRevisionLevel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RectifierStatusRevisionLevel_Type.__name__=_H
_RectifierStatusRevisionLevel_Object=MibTableColumn
rectifierStatusRevisionLevel=_RectifierStatusRevisionLevel_Object((1,3,6,1,4,1,12148,8,5,5,2,1,9),_RectifierStatusRevisionLevel_Type())
rectifierStatusRevisionLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusRevisionLevel.setStatus(_A)
_AcDistribution_ObjectIdentity=ObjectIdentity
acDistribution=_AcDistribution_ObjectIdentity((1,3,6,1,4,1,12148,8,6))
_AcVoltage1_Type=Integer32
_AcVoltage1_Object=MibScalar
acVoltage1=_AcVoltage1_Object((1,3,6,1,4,1,12148,8,6,1),_AcVoltage1_Type())
acVoltage1.setMaxAccess(_C)
if mibBuilder.loadTexts:acVoltage1.setStatus(_A)
if mibBuilder.loadTexts:acVoltage1.setUnits(_V)
_AcVoltage2_Type=Integer32
_AcVoltage2_Object=MibScalar
acVoltage2=_AcVoltage2_Object((1,3,6,1,4,1,12148,8,6,2),_AcVoltage2_Type())
acVoltage2.setMaxAccess(_C)
if mibBuilder.loadTexts:acVoltage2.setStatus(_A)
if mibBuilder.loadTexts:acVoltage2.setUnits(_V)
_AcVoltage3_Type=Integer32
_AcVoltage3_Object=MibScalar
acVoltage3=_AcVoltage3_Object((1,3,6,1,4,1,12148,8,6,3),_AcVoltage3_Type())
acVoltage3.setMaxAccess(_C)
if mibBuilder.loadTexts:acVoltage3.setStatus(_A)
if mibBuilder.loadTexts:acVoltage3.setUnits(_V)
_AlarmGroup_ObjectIdentity=ObjectIdentity
alarmGroup=_AlarmGroup_ObjectIdentity((1,3,6,1,4,1,12148,8,7))
_AlarmWellknownAlarms_ObjectIdentity=ObjectIdentity
alarmWellknownAlarms=_AlarmWellknownAlarms_ObjectIdentity((1,3,6,1,4,1,12148,8,7,1))
class _AlarmMajorHighBattVolt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmMajorHighBattVolt_Type.__name__=_B
_AlarmMajorHighBattVolt_Object=MibScalar
alarmMajorHighBattVolt=_AlarmMajorHighBattVolt_Object((1,3,6,1,4,1,12148,8,7,1,1),_AlarmMajorHighBattVolt_Type())
alarmMajorHighBattVolt.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMajorHighBattVolt.setStatus(_A)
class _AlarmMinorHighBattVolt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmMinorHighBattVolt_Type.__name__=_B
_AlarmMinorHighBattVolt_Object=MibScalar
alarmMinorHighBattVolt=_AlarmMinorHighBattVolt_Object((1,3,6,1,4,1,12148,8,7,1,2),_AlarmMinorHighBattVolt_Type())
alarmMinorHighBattVolt.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMinorHighBattVolt.setStatus(_A)
class _AlarmMajorLowBattVolt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmMajorLowBattVolt_Type.__name__=_B
_AlarmMajorLowBattVolt_Object=MibScalar
alarmMajorLowBattVolt=_AlarmMajorLowBattVolt_Object((1,3,6,1,4,1,12148,8,7,1,3),_AlarmMajorLowBattVolt_Type())
alarmMajorLowBattVolt.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMajorLowBattVolt.setStatus(_A)
class _AlarmMinorLowBattVolt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmMinorLowBattVolt_Type.__name__=_B
_AlarmMinorLowBattVolt_Object=MibScalar
alarmMinorLowBattVolt=_AlarmMinorLowBattVolt_Object((1,3,6,1,4,1,12148,8,7,1,4),_AlarmMinorLowBattVolt_Type())
alarmMinorLowBattVolt.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMinorLowBattVolt.setStatus(_A)
class _AlarmMajorBatteryHighTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmMajorBatteryHighTemp_Type.__name__=_B
_AlarmMajorBatteryHighTemp_Object=MibScalar
alarmMajorBatteryHighTemp=_AlarmMajorBatteryHighTemp_Object((1,3,6,1,4,1,12148,8,7,1,5),_AlarmMajorBatteryHighTemp_Type())
alarmMajorBatteryHighTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMajorBatteryHighTemp.setStatus(_A)
class _AlarmMinorBatteryHighTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmMinorBatteryHighTemp_Type.__name__=_B
_AlarmMinorBatteryHighTemp_Object=MibScalar
alarmMinorBatteryHighTemp=_AlarmMinorBatteryHighTemp_Object((1,3,6,1,4,1,12148,8,7,1,6),_AlarmMinorBatteryHighTemp_Type())
alarmMinorBatteryHighTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMinorBatteryHighTemp.setStatus(_A)
class _AlarmBatteryDisconnectOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmBatteryDisconnectOpen_Type.__name__=_B
_AlarmBatteryDisconnectOpen_Object=MibScalar
alarmBatteryDisconnectOpen=_AlarmBatteryDisconnectOpen_Object((1,3,6,1,4,1,12148,8,7,1,7),_AlarmBatteryDisconnectOpen_Type())
alarmBatteryDisconnectOpen.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmBatteryDisconnectOpen.setStatus(_A)
class _AlarmLVD1open_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmLVD1open_Type.__name__=_B
_AlarmLVD1open_Object=MibScalar
alarmLVD1open=_AlarmLVD1open_Object((1,3,6,1,4,1,12148,8,7,1,8),_AlarmLVD1open_Type())
alarmLVD1open.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLVD1open.setStatus(_A)
class _AlarmLVD2open_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmLVD2open_Type.__name__=_B
_AlarmLVD2open_Object=MibScalar
alarmLVD2open=_AlarmLVD2open_Object((1,3,6,1,4,1,12148,8,7,1,9),_AlarmLVD2open_Type())
alarmLVD2open.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLVD2open.setStatus(_A)
class _AlarmLVD3open_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmLVD3open_Type.__name__=_B
_AlarmLVD3open_Object=MibScalar
alarmLVD3open=_AlarmLVD3open_Object((1,3,6,1,4,1,12148,8,7,1,10),_AlarmLVD3open_Type())
alarmLVD3open.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLVD3open.setStatus(_A)
class _AlarmACmains_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmACmains_Type.__name__=_B
_AlarmACmains_Object=MibScalar
alarmACmains=_AlarmACmains_Object((1,3,6,1,4,1,12148,8,7,1,11),_AlarmACmains_Type())
alarmACmains.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmACmains.setStatus(_A)
class _AlarmBatteryBreakerOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmBatteryBreakerOpen_Type.__name__=_B
_AlarmBatteryBreakerOpen_Object=MibScalar
alarmBatteryBreakerOpen=_AlarmBatteryBreakerOpen_Object((1,3,6,1,4,1,12148,8,7,1,12),_AlarmBatteryBreakerOpen_Type())
alarmBatteryBreakerOpen.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmBatteryBreakerOpen.setStatus(_A)
class _AlarmDistributionBreakerOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmDistributionBreakerOpen_Type.__name__=_B
_AlarmDistributionBreakerOpen_Object=MibScalar
alarmDistributionBreakerOpen=_AlarmDistributionBreakerOpen_Object((1,3,6,1,4,1,12148,8,7,1,13),_AlarmDistributionBreakerOpen_Type())
alarmDistributionBreakerOpen.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmDistributionBreakerOpen.setStatus(_A)
class _AlarmMajorRectifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmMajorRectifier_Type.__name__=_B
_AlarmMajorRectifier_Object=MibScalar
alarmMajorRectifier=_AlarmMajorRectifier_Object((1,3,6,1,4,1,12148,8,7,1,14),_AlarmMajorRectifier_Type())
alarmMajorRectifier.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMajorRectifier.setStatus(_A)
class _AlarmMinorRectifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmMinorRectifier_Type.__name__=_B
_AlarmMinorRectifier_Object=MibScalar
alarmMinorRectifier=_AlarmMinorRectifier_Object((1,3,6,1,4,1,12148,8,7,1,15),_AlarmMinorRectifier_Type())
alarmMinorRectifier.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMinorRectifier.setStatus(_A)
class _AlarmMajorBatteryMidpoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmMajorBatteryMidpoint_Type.__name__=_B
_AlarmMajorBatteryMidpoint_Object=MibScalar
alarmMajorBatteryMidpoint=_AlarmMajorBatteryMidpoint_Object((1,3,6,1,4,1,12148,8,7,1,16),_AlarmMajorBatteryMidpoint_Type())
alarmMajorBatteryMidpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMajorBatteryMidpoint.setStatus(_A)
class _AlarmMinorBatteryMidpoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmMinorBatteryMidpoint_Type.__name__=_B
_AlarmMinorBatteryMidpoint_Object=MibScalar
alarmMinorBatteryMidpoint=_AlarmMinorBatteryMidpoint_Object((1,3,6,1,4,1,12148,8,7,1,17),_AlarmMinorBatteryMidpoint_Type())
alarmMinorBatteryMidpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMinorBatteryMidpoint.setStatus(_A)
class _AlarmBatteryLifeEnded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmBatteryLifeEnded_Type.__name__=_B
_AlarmBatteryLifeEnded_Object=MibScalar
alarmBatteryLifeEnded=_AlarmBatteryLifeEnded_Object((1,3,6,1,4,1,12148,8,7,1,18),_AlarmBatteryLifeEnded_Type())
alarmBatteryLifeEnded.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmBatteryLifeEnded.setStatus(_A)
class _AlarmBatteryTestmodeEntered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmBatteryTestmodeEntered_Type.__name__=_B
_AlarmBatteryTestmodeEntered_Object=MibScalar
alarmBatteryTestmodeEntered=_AlarmBatteryTestmodeEntered_Object((1,3,6,1,4,1,12148,8,7,1,19),_AlarmBatteryTestmodeEntered_Type())
alarmBatteryTestmodeEntered.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmBatteryTestmodeEntered.setStatus(_A)
class _AlarmBatteryBoostmodeEntered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlarmBatteryBoostmodeEntered_Type.__name__=_B
_AlarmBatteryBoostmodeEntered_Object=MibScalar
alarmBatteryBoostmodeEntered=_AlarmBatteryBoostmodeEntered_Object((1,3,6,1,4,1,12148,8,7,1,20),_AlarmBatteryBoostmodeEntered_Type())
alarmBatteryBoostmodeEntered.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmBatteryBoostmodeEntered.setStatus(_A)
alarmMajorHighBattVoltTrap=NotificationType((1,3,6,1,4,1,12148,8,8,1))
alarmMajorHighBattVoltTrap.setObjects((_D,_b))
if mibBuilder.loadTexts:alarmMajorHighBattVoltTrap.setStatus(_A)
alarmMinorHighBattVoltTrap=NotificationType((1,3,6,1,4,1,12148,8,8,2))
alarmMinorHighBattVoltTrap.setObjects((_D,_c))
if mibBuilder.loadTexts:alarmMinorHighBattVoltTrap.setStatus(_A)
alarmMajorLowBattVoltTrap=NotificationType((1,3,6,1,4,1,12148,8,8,3))
alarmMajorLowBattVoltTrap.setObjects((_D,_d))
if mibBuilder.loadTexts:alarmMajorLowBattVoltTrap.setStatus(_A)
alarmMinorLowBattVoltTrap=NotificationType((1,3,6,1,4,1,12148,8,8,4))
alarmMinorLowBattVoltTrap.setObjects((_D,_e))
if mibBuilder.loadTexts:alarmMinorLowBattVoltTrap.setStatus(_A)
alarmMajorBatteryHighTempTrap=NotificationType((1,3,6,1,4,1,12148,8,8,5))
alarmMajorBatteryHighTempTrap.setObjects((_D,_f))
if mibBuilder.loadTexts:alarmMajorBatteryHighTempTrap.setStatus(_A)
alarmMinorBatteryHighTempTrap=NotificationType((1,3,6,1,4,1,12148,8,8,6))
alarmMinorBatteryHighTempTrap.setObjects((_D,_g))
if mibBuilder.loadTexts:alarmMinorBatteryHighTempTrap.setStatus(_A)
alarmBatteryDisconnectOpenTrap=NotificationType((1,3,6,1,4,1,12148,8,8,7))
alarmBatteryDisconnectOpenTrap.setObjects((_D,_h))
if mibBuilder.loadTexts:alarmBatteryDisconnectOpenTrap.setStatus(_A)
alarmLVD1openTrap=NotificationType((1,3,6,1,4,1,12148,8,8,8))
alarmLVD1openTrap.setObjects((_D,_i))
if mibBuilder.loadTexts:alarmLVD1openTrap.setStatus(_A)
alarmLVD2openTrap=NotificationType((1,3,6,1,4,1,12148,8,8,9))
alarmLVD2openTrap.setObjects((_D,_j))
if mibBuilder.loadTexts:alarmLVD2openTrap.setStatus(_A)
alarmLVD3openTrap=NotificationType((1,3,6,1,4,1,12148,8,8,10))
alarmLVD3openTrap.setObjects((_D,_k))
if mibBuilder.loadTexts:alarmLVD3openTrap.setStatus(_A)
alarmACmainsTrap=NotificationType((1,3,6,1,4,1,12148,8,8,11))
alarmACmainsTrap.setObjects((_D,_l))
if mibBuilder.loadTexts:alarmACmainsTrap.setStatus(_A)
alarmBatteryBreakerOpenTrap=NotificationType((1,3,6,1,4,1,12148,8,8,12))
alarmBatteryBreakerOpenTrap.setObjects((_D,_m))
if mibBuilder.loadTexts:alarmBatteryBreakerOpenTrap.setStatus(_A)
alarmDistributionBreakerOpenTrap=NotificationType((1,3,6,1,4,1,12148,8,8,13))
alarmDistributionBreakerOpenTrap.setObjects((_D,_n))
if mibBuilder.loadTexts:alarmDistributionBreakerOpenTrap.setStatus(_A)
alarmMajorRectifierTrap=NotificationType((1,3,6,1,4,1,12148,8,8,14))
alarmMajorRectifierTrap.setObjects((_D,_o))
if mibBuilder.loadTexts:alarmMajorRectifierTrap.setStatus(_A)
alarmMinorRectifierTrap=NotificationType((1,3,6,1,4,1,12148,8,8,15))
alarmMinorRectifierTrap.setObjects((_D,_p))
if mibBuilder.loadTexts:alarmMinorRectifierTrap.setStatus(_A)
alarmMajorBatteryMidpointTrap=NotificationType((1,3,6,1,4,1,12148,8,8,16))
alarmMajorBatteryMidpointTrap.setObjects((_D,_q))
if mibBuilder.loadTexts:alarmMajorBatteryMidpointTrap.setStatus(_A)
alarmMinorBatteryMidpointTrap=NotificationType((1,3,6,1,4,1,12148,8,8,17))
alarmMinorBatteryMidpointTrap.setObjects((_D,_r))
if mibBuilder.loadTexts:alarmMinorBatteryMidpointTrap.setStatus(_A)
alarmBatteryLifeEndedTrap=NotificationType((1,3,6,1,4,1,12148,8,8,18))
alarmBatteryLifeEndedTrap.setObjects((_D,_s))
if mibBuilder.loadTexts:alarmBatteryLifeEndedTrap.setStatus(_A)
alarmBatteryTestmodeEnteredTrap=NotificationType((1,3,6,1,4,1,12148,8,8,19))
alarmBatteryTestmodeEnteredTrap.setObjects((_D,_t))
if mibBuilder.loadTexts:alarmBatteryTestmodeEnteredTrap.setStatus(_A)
alarmBatteryBoostmodeEnteredTrap=NotificationType((1,3,6,1,4,1,12148,8,8,20))
alarmBatteryBoostmodeEnteredTrap.setObjects((_D,_u))
if mibBuilder.loadTexts:alarmBatteryBoostmodeEnteredTrap.setStatus(_A)
alarmController1proginputTrap=NotificationType((1,3,6,1,4,1,12148,8,8,21))
alarmController1proginputTrap.setObjects((_D,_v))
if mibBuilder.loadTexts:alarmController1proginputTrap.setStatus(_A)
alarmController2proginputTrap=NotificationType((1,3,6,1,4,1,12148,8,8,22))
alarmController2proginputTrap.setObjects((_D,_w))
if mibBuilder.loadTexts:alarmController2proginputTrap.setStatus(_A)
alarmController3proginputTrap=NotificationType((1,3,6,1,4,1,12148,8,8,23))
alarmController3proginputTrap.setObjects((_D,_x))
if mibBuilder.loadTexts:alarmController3proginputTrap.setStatus(_A)
alarmController4proginputTrap=NotificationType((1,3,6,1,4,1,12148,8,8,24))
alarmController4proginputTrap.setObjects((_D,_y))
if mibBuilder.loadTexts:alarmController4proginputTrap.setStatus(_A)
alarmController5proginputTrap=NotificationType((1,3,6,1,4,1,12148,8,8,25))
alarmController5proginputTrap.setObjects((_D,_z))
if mibBuilder.loadTexts:alarmController5proginputTrap.setStatus(_A)
alarmController6proginputTrap=NotificationType((1,3,6,1,4,1,12148,8,8,26))
alarmController6proginputTrap.setObjects((_D,_A0))
if mibBuilder.loadTexts:alarmController6proginputTrap.setStatus(_A)
alarmController7proginputTrap=NotificationType((1,3,6,1,4,1,12148,8,8,27))
alarmController7proginputTrap.setObjects((_D,_A1))
if mibBuilder.loadTexts:alarmController7proginputTrap.setStatus(_A)
alarmController8proginputTrap=NotificationType((1,3,6,1,4,1,12148,8,8,28))
alarmController8proginputTrap.setObjects((_D,_A2))
if mibBuilder.loadTexts:alarmController8proginputTrap.setStatus(_A)
dcSystemTraps=NotificationGroup((1,3,6,1,4,1,12148,8,8))
dcSystemTraps.setObjects(*((_D,_A3),(_D,_A4),(_D,_A5),(_D,_A6),(_D,_A7),(_D,_A8),(_D,_A9),(_D,_AA),(_D,_AB),(_D,_AC),(_D,_AD),(_D,_AE),(_D,_AF),(_D,_AG),(_D,_AH),(_D,_AI),(_D,_AJ),(_D,_AK),(_D,_AL),(_D,_AM),(_D,_AN),(_D,_AO),(_D,_AP),(_D,_AQ),(_D,_AR),(_D,_AS),(_D,_AT),(_D,_AU)))
if mibBuilder.loadTexts:dcSystemTraps.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'eltekDistributedPlant':eltekDistributedPlant,'controlSystem':controlSystem,'systemTime':systemTime,'systemTimeTime':systemTimeTime,'systemInfoRefresh':systemInfoRefresh,'systemTrapRepeatRate':systemTrapRepeatRate,'systemSendOffTrap':systemSendOffTrap,'systemNumOfControlUnits':systemNumOfControlUnits,_X:systemControlUnitIndex,'systemControlUnitTable':systemControlUnitTable,'systemControlUnitEntry':systemControlUnitEntry,'inputControlUnitID':inputControlUnitID,_v:inputUserConfigurable1,_w:inputUserConfigurable2,_x:inputUserConfigurable3,_y:inputUserConfigurable4,_z:inputUserConfigurable5,_A0:inputUserConfigurable6,_A1:inputUserConfigurable7,_A2:inputUserConfigurable8,'inputUserConfigurable9':inputUserConfigurable9,'inputUserConfigurable10':inputUserConfigurable10,'systemLinkStatus':systemLinkStatus,'systemInitiateEEPROM':systemInitiateEEPROM,'dcSystem':dcSystem,'dcPlant':dcPlant,'systemSiteInfo':systemSiteInfo,'systemSiteInfoCustomer':systemSiteInfoCustomer,'systemSiteInfoLocation':systemSiteInfoLocation,'systemSiteInfoMessage1':systemSiteInfoMessage1,'systemSiteInfoMessage2':systemSiteInfoMessage2,'systemSiteInfoInstalledDate':systemSiteInfoInstalledDate,'systemSiteInfoControllerType':systemSiteInfoControllerType,'systemSiteInfoSystemSeriaNum':systemSiteInfoSystemSeriaNum,'systemSiteInfoControllerSeriaNum':systemSiteInfoControllerSeriaNum,'systemNominalVoltage':systemNominalVoltage,'systemOperationalStatus':systemOperationalStatus,'battery':battery,'batteryName':batteryName,'batteryVoltage':batteryVoltage,'batteryCurrent':batteryCurrent,'batteryTemp':batteryTemp,'batteryBreakerStatus':batteryBreakerStatus,'batteryChargeCurrentLimitCtrl':batteryChargeCurrentLimitCtrl,'batteryChargeCurrentLimitValue':batteryChargeCurrentLimitValue,'batteryTempCompEnable':batteryTempCompEnable,'batteryFloatVoltConfig':batteryFloatVoltConfig,'batteryEqualizeVoltConfig':batteryEqualizeVoltConfig,'batteryHighMajorAlarmVoltageConfig':batteryHighMajorAlarmVoltageConfig,'batteryHighMinorAlarmVoltageConfig':batteryHighMinorAlarmVoltageConfig,'batteryLowMajorAlarmVoltageConfig':batteryLowMajorAlarmVoltageConfig,'batteryLowMinorAlarmVoltageConfig':batteryLowMinorAlarmVoltageConfig,'batteryStartManualTest':batteryStartManualTest,'batteryStartManualBoost':batteryStartManualBoost,'batteryLVD':batteryLVD,'batteryLVDStatus':batteryLVDStatus,'batteryLVDDisconnectVoltage':batteryLVDDisconnectVoltage,'batteryLVDConnectVoltage':batteryLVDConnectVoltage,'batteryBanksNumofBanks':batteryBanksNumofBanks,'batteryBanks':batteryBanks,'batterySymmetryDeltaLimitVoltage':batterySymmetryDeltaLimitVoltage,_Z:batteryBanksIndex,'batteryBanksTable':batteryBanksTable,'batteryBanksEntry':batteryBanksEntry,'batteryBankID':batteryBankID,'batteryBanksSymmetry1enable':batteryBanksSymmetry1enable,'batteryBanksSymmetry1status':batteryBanksSymmetry1status,'batteryBanksSymmetry1deltaVoltage':batteryBanksSymmetry1deltaVoltage,'batteryBanksSymmetry2enable':batteryBanksSymmetry2enable,'batteryBanksSymmetry2status':batteryBanksSymmetry2status,'batteryBanksSymmetry2deltaVoltage':batteryBanksSymmetry2deltaVoltage,'batteryBanksSymmetry3enable':batteryBanksSymmetry3enable,'batteryBanksSymmetry3status':batteryBanksSymmetry3status,'batteryBanksSymmetry3deltaVoltage':batteryBanksSymmetry3deltaVoltage,'batteryBanksSymmetry4enable':batteryBanksSymmetry4enable,'batteryBanksSymmetry4status':batteryBanksSymmetry4status,'batteryBanksSymmetry4deltaVoltage':batteryBanksSymmetry4deltaVoltage,'batteryBanksSymmetry5enable':batteryBanksSymmetry5enable,'batteryBanksSymmetry5status':batteryBanksSymmetry5status,'batteryBanksSymmetry5deltaVoltage':batteryBanksSymmetry5deltaVoltage,'batteryBanksSymmetry6enable':batteryBanksSymmetry6enable,'batteryBanksSymmetry6status':batteryBanksSymmetry6status,'batteryBanksSymmetry6deltaVoltage':batteryBanksSymmetry6deltaVoltage,'batteryBanksSymmetry7enable':batteryBanksSymmetry7enable,'batteryBanksSymmetry7status':batteryBanksSymmetry7status,'batteryBanksSymmetry7deltaVoltage':batteryBanksSymmetry7deltaVoltage,'batteryBanksSymmetry8enable':batteryBanksSymmetry8enable,'batteryBanksSymmetry8status':batteryBanksSymmetry8status,'batteryBanksSymmetry8deltaVoltage':batteryBanksSymmetry8deltaVoltage,'loadDistribution':loadDistribution,'loadDistributionCurrent':loadDistributionCurrent,'loadDistributionBreakerStatus':loadDistributionBreakerStatus,'loadDistributionLVDStatus':loadDistributionLVDStatus,'loadLVD1EnableStatus':loadLVD1EnableStatus,'loadLVD1Status':loadLVD1Status,'loadLVD1ConnectVoltage':loadLVD1ConnectVoltage,'loadLVD1DisconnectVoltage':loadLVD1DisconnectVoltage,'loadLVD2EnableStatus':loadLVD2EnableStatus,'loadLVD2Status':loadLVD2Status,'loadLVD2ConnectVoltage':loadLVD2ConnectVoltage,'loadLVD2DisconnectVoltage':loadLVD2DisconnectVoltage,'loadLVD3EnableStatus':loadLVD3EnableStatus,'loadLVD3Status':loadLVD3Status,'loadLVD3ConnectVoltage':loadLVD3ConnectVoltage,'loadLVD3DisconnectVoltage':loadLVD3DisconnectVoltage,'rectifier':rectifier,'rectifierInstalledRectifiers':rectifierInstalledRectifiers,'rectifierRectifiersActive':rectifierRectifiersActive,'rectifierTotalCurrent':rectifierTotalCurrent,'rectifierUtilization':rectifierUtilization,'rectifierStatus':rectifierStatus,'rectifierStatusNoIndex':rectifierStatusNoIndex,'rectifierStatusTable':rectifierStatusTable,'rectifierStatusEntry':rectifierStatusEntry,_a:rectifierStatusID,'rectifierStatusStatus':rectifierStatusStatus,'rectifierStatusOutputCurrent':rectifierStatusOutputCurrent,'rectifierStatusOutputVoltage':rectifierStatusOutputVoltage,'rectifierStatusTemp':rectifierStatusTemp,'rectifierStatusType':rectifierStatusType,'rectifierStatusSKU':rectifierStatusSKU,'rectifierStatusSerialNo':rectifierStatusSerialNo,'rectifierStatusRevisionLevel':rectifierStatusRevisionLevel,'acDistribution':acDistribution,'acVoltage1':acVoltage1,'acVoltage2':acVoltage2,'acVoltage3':acVoltage3,'alarmGroup':alarmGroup,'alarmWellknownAlarms':alarmWellknownAlarms,_b:alarmMajorHighBattVolt,_c:alarmMinorHighBattVolt,_d:alarmMajorLowBattVolt,_e:alarmMinorLowBattVolt,_f:alarmMajorBatteryHighTemp,_g:alarmMinorBatteryHighTemp,_h:alarmBatteryDisconnectOpen,_i:alarmLVD1open,_j:alarmLVD2open,_k:alarmLVD3open,_l:alarmACmains,_m:alarmBatteryBreakerOpen,_n:alarmDistributionBreakerOpen,_o:alarmMajorRectifier,_p:alarmMinorRectifier,_q:alarmMajorBatteryMidpoint,_r:alarmMinorBatteryMidpoint,_s:alarmBatteryLifeEnded,_t:alarmBatteryTestmodeEntered,_u:alarmBatteryBoostmodeEntered,'dcSystemTraps':dcSystemTraps,_A3:alarmMajorHighBattVoltTrap,_A4:alarmMinorHighBattVoltTrap,_A5:alarmMajorLowBattVoltTrap,_A6:alarmMinorLowBattVoltTrap,_A7:alarmMajorBatteryHighTempTrap,_A8:alarmMinorBatteryHighTempTrap,_A9:alarmBatteryDisconnectOpenTrap,_AA:alarmLVD1openTrap,_AB:alarmLVD2openTrap,_AC:alarmLVD3openTrap,_AD:alarmACmainsTrap,_AE:alarmBatteryBreakerOpenTrap,_AF:alarmDistributionBreakerOpenTrap,_AG:alarmMajorRectifierTrap,_AH:alarmMinorRectifierTrap,_AI:alarmMajorBatteryMidpointTrap,_AJ:alarmMinorBatteryMidpointTrap,_AK:alarmBatteryLifeEndedTrap,_AL:alarmBatteryTestmodeEnteredTrap,_AM:alarmBatteryBoostmodeEnteredTrap,_AN:alarmController1proginputTrap,_AO:alarmController2proginputTrap,_AP:alarmController3proginputTrap,_AQ:alarmController4proginputTrap,_AR:alarmController5proginputTrap,_AS:alarmController6proginputTrap,_AT:alarmController7proginputTrap,_AU:alarmController8proginputTrap})