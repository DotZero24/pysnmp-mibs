_Aa='alarmUserConfigurable14Trap'
_AZ='alarmUserConfigurable13Trap'
_AY='alarmUserConfigurable12Trap'
_AX='alarmUserConfigurable11Trap'
_AW='alarmUserConfigurable10Trap'
_AV='alarmUserConfigurable9Trap'
_AU='alarmUserConfigurable8Trap'
_AT='alarmUserConfigurable7Trap'
_AS='alarmUserConfigurable6Trap'
_AR='alarmUserConfigurable5Trap'
_AQ='alarmUserConfigurable4Trap'
_AP='alarmUserConfigurable3Trap'
_AO='alarmUserConfigurable2Trap'
_AN='alarmUserConfigurable1Trap'
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
_A2='alarmUserConfigurable14'
_A1='alarmUserConfigurable13'
_A0='alarmUserConfigurable12'
_z='alarmUserConfigurable11'
_y='alarmUserConfigurable10'
_x='alarmUserConfigurable9'
_w='alarmUserConfigurable8'
_v='alarmUserConfigurable7'
_u='alarmUserConfigurable6'
_t='alarmUserConfigurable5'
_s='alarmUserConfigurable4'
_r='alarmUserConfigurable3'
_q='alarmUserConfigurable2'
_p='alarmUserConfigurable1'
_o='alarmBatteryBoostmodeEntered'
_n='alarmBatteryTestmodeEntered'
_m='alarmBatteryLifeEnded'
_l='alarmMinorBatteryMidpoint'
_k='alarmMajorBatteryMidpoint'
_j='alarmMinorRectifier'
_i='alarmMajorRectifier'
_h='alarmDistributionBreakerOpen'
_g='alarmBatteryBreakerOpen'
_f='alarmACmains'
_e='alarmLVD3open'
_d='alarmLVD2open'
_c='alarmLVD1open'
_b='alarmBatteryDisconnectOpen'
_a='alarmMinorBatteryHighTemp'
_Z='alarmMajorBatteryHighTemp'
_Y='alarmMinorLowBattVolt'
_X='alarmMajorLowBattVolt'
_W='alarmMinorHighBattVolt'
_V='alarmMajorHighBattVolt'
_U='rectifierStatusID'
_T='enable'
_S='closed'
_R='Volts AC'
_Q='enabled'
_P='disabled'
_O='batteryMidpointIndex'
_N='pushbutton'
_M='disconnect'
_L='connect'
_K='Amperes; i.e. 20 = 20 Amperes'
_J='disable'
_I='DisplayString'
_H='1/100 Volt; i.e. 5400 = 54.00V'
_G='read-write'
_F='normal'
_E='alarm'
_D='ELTEK_GENERIC-MIB'
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
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
_EltekPlant_ObjectIdentity=ObjectIdentity
eltekPlant=_EltekPlant_ObjectIdentity((1,3,6,1,4,1,12148,7))
_ControlSystem_ObjectIdentity=ObjectIdentity
controlSystem=_ControlSystem_ObjectIdentity((1,3,6,1,4,1,12148,7,1))
_SystemTime_ObjectIdentity=ObjectIdentity
systemTime=_SystemTime_ObjectIdentity((1,3,6,1,4,1,12148,7,1,1))
class _SystemTimeTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SystemTimeTime_Type.__name__=_I
_SystemTimeTime_Object=MibScalar
systemTimeTime=_SystemTimeTime_Object((1,3,6,1,4,1,12148,7,1,1,1),_SystemTimeTime_Type())
systemTimeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTimeTime.setStatus(_A)
class _SystemInfoRefresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),('refreshdata',1)))
_SystemInfoRefresh_Type.__name__=_B
_SystemInfoRefresh_Object=MibScalar
systemInfoRefresh=_SystemInfoRefresh_Object((1,3,6,1,4,1,12148,7,1,2),_SystemInfoRefresh_Type())
systemInfoRefresh.setMaxAccess(_G)
if mibBuilder.loadTexts:systemInfoRefresh.setStatus(_A)
class _SystemTrapRepeatRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_SystemTrapRepeatRate_Type.__name__=_B
_SystemTrapRepeatRate_Object=MibScalar
systemTrapRepeatRate=_SystemTrapRepeatRate_Object((1,3,6,1,4,1,12148,7,1,3),_SystemTrapRepeatRate_Type())
systemTrapRepeatRate.setMaxAccess(_G)
if mibBuilder.loadTexts:systemTrapRepeatRate.setStatus(_A)
class _SystemSendOffTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_SystemSendOffTrap_Type.__name__=_B
_SystemSendOffTrap_Object=MibScalar
systemSendOffTrap=_SystemSendOffTrap_Object((1,3,6,1,4,1,12148,7,1,4),_SystemSendOffTrap_Type())
systemSendOffTrap.setMaxAccess(_G)
if mibBuilder.loadTexts:systemSendOffTrap.setStatus(_A)
_DcSystem_ObjectIdentity=ObjectIdentity
dcSystem=_DcSystem_ObjectIdentity((1,3,6,1,4,1,12148,7,2))
_DcPlant_ObjectIdentity=ObjectIdentity
dcPlant=_DcPlant_ObjectIdentity((1,3,6,1,4,1,12148,7,2,1))
_SystemSiteInfo_ObjectIdentity=ObjectIdentity
systemSiteInfo=_SystemSiteInfo_ObjectIdentity((1,3,6,1,4,1,12148,7,2,1,3))
class _SystemSiteInfoCustomer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SystemSiteInfoCustomer_Type.__name__=_I
_SystemSiteInfoCustomer_Object=MibScalar
systemSiteInfoCustomer=_SystemSiteInfoCustomer_Object((1,3,6,1,4,1,12148,7,2,1,3,1),_SystemSiteInfoCustomer_Type())
systemSiteInfoCustomer.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoCustomer.setStatus(_A)
class _SystemSiteInfoLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SystemSiteInfoLocation_Type.__name__=_I
_SystemSiteInfoLocation_Object=MibScalar
systemSiteInfoLocation=_SystemSiteInfoLocation_Object((1,3,6,1,4,1,12148,7,2,1,3,2),_SystemSiteInfoLocation_Type())
systemSiteInfoLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoLocation.setStatus(_A)
class _SystemSiteInfoMessage1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SystemSiteInfoMessage1_Type.__name__=_I
_SystemSiteInfoMessage1_Object=MibScalar
systemSiteInfoMessage1=_SystemSiteInfoMessage1_Object((1,3,6,1,4,1,12148,7,2,1,3,3),_SystemSiteInfoMessage1_Type())
systemSiteInfoMessage1.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoMessage1.setStatus(_A)
class _SystemSiteInfoMessage2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SystemSiteInfoMessage2_Type.__name__=_I
_SystemSiteInfoMessage2_Object=MibScalar
systemSiteInfoMessage2=_SystemSiteInfoMessage2_Object((1,3,6,1,4,1,12148,7,2,1,3,4),_SystemSiteInfoMessage2_Type())
systemSiteInfoMessage2.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoMessage2.setStatus(_A)
class _SystemSiteInfoInstalledDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SystemSiteInfoInstalledDate_Type.__name__=_I
_SystemSiteInfoInstalledDate_Object=MibScalar
systemSiteInfoInstalledDate=_SystemSiteInfoInstalledDate_Object((1,3,6,1,4,1,12148,7,2,1,3,5),_SystemSiteInfoInstalledDate_Type())
systemSiteInfoInstalledDate.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoInstalledDate.setStatus(_A)
class _SystemSiteInfoControllerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('al175',0),('al4000',1),('al6000',2),('enexus',3)))
_SystemSiteInfoControllerType_Type.__name__=_B
_SystemSiteInfoControllerType_Object=MibScalar
systemSiteInfoControllerType=_SystemSiteInfoControllerType_Object((1,3,6,1,4,1,12148,7,2,1,3,6),_SystemSiteInfoControllerType_Type())
systemSiteInfoControllerType.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoControllerType.setStatus(_A)
class _SystemSiteInfoSystemSeriaNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SystemSiteInfoSystemSeriaNum_Type.__name__=_I
_SystemSiteInfoSystemSeriaNum_Object=MibScalar
systemSiteInfoSystemSeriaNum=_SystemSiteInfoSystemSeriaNum_Object((1,3,6,1,4,1,12148,7,2,1,3,7),_SystemSiteInfoSystemSeriaNum_Type())
systemSiteInfoSystemSeriaNum.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoSystemSeriaNum.setStatus(_A)
class _SystemSiteInfoControllerSeriaNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SystemSiteInfoControllerSeriaNum_Type.__name__=_I
_SystemSiteInfoControllerSeriaNum_Object=MibScalar
systemSiteInfoControllerSeriaNum=_SystemSiteInfoControllerSeriaNum_Object((1,3,6,1,4,1,12148,7,2,1,3,8),_SystemSiteInfoControllerSeriaNum_Type())
systemSiteInfoControllerSeriaNum.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSiteInfoControllerSeriaNum.setStatus(_A)
class _SystemNominalVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('prs48v',0),('prs24v',1),('prs12v',2),('prs26v',3),('prs60v',4)))
_SystemNominalVoltage_Type.__name__=_B
_SystemNominalVoltage_Object=MibScalar
systemNominalVoltage=_SystemNominalVoltage_Object((1,3,6,1,4,1,12148,7,2,1,4),_SystemNominalVoltage_Type())
systemNominalVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:systemNominalVoltage.setStatus(_A)
class _SystemOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('floatvoltreg',0),('floattempcomp',1),('batteryboost',2),('batterytest',3)))
_SystemOperationalStatus_Type.__name__=_B
_SystemOperationalStatus_Object=MibScalar
systemOperationalStatus=_SystemOperationalStatus_Object((1,3,6,1,4,1,12148,7,2,2),_SystemOperationalStatus_Type())
systemOperationalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:systemOperationalStatus.setStatus(_A)
_Battery_ObjectIdentity=ObjectIdentity
battery=_Battery_ObjectIdentity((1,3,6,1,4,1,12148,7,3))
class _BatteryName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_BatteryName_Type.__name__=_I
_BatteryName_Object=MibScalar
batteryName=_BatteryName_Object((1,3,6,1,4,1,12148,7,3,1),_BatteryName_Type())
batteryName.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryName.setStatus(_A)
class _BatteryVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7500))
_BatteryVoltage_Type.__name__=_B
_BatteryVoltage_Object=MibScalar
batteryVoltage=_BatteryVoltage_Object((1,3,6,1,4,1,12148,7,3,2),_BatteryVoltage_Type())
batteryVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryVoltage.setStatus(_A)
if mibBuilder.loadTexts:batteryVoltage.setUnits(_H)
_BatteryCurrent_Type=Integer32
_BatteryCurrent_Object=MibScalar
batteryCurrent=_BatteryCurrent_Object((1,3,6,1,4,1,12148,7,3,3),_BatteryCurrent_Type())
batteryCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryCurrent.setStatus(_A)
if mibBuilder.loadTexts:batteryCurrent.setUnits(_K)
class _BatteryTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_BatteryTemp_Type.__name__=_B
_BatteryTemp_Object=MibScalar
batteryTemp=_BatteryTemp_Object((1,3,6,1,4,1,12148,7,3,4),_BatteryTemp_Type())
batteryTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryTemp.setStatus(_A)
if mibBuilder.loadTexts:batteryTemp.setUnits('1/10 Deg. C; i.e. 250 = 25.0 Deg. C.')
class _BatteryBreakerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),('open',1)))
_BatteryBreakerStatus_Type.__name__=_B
_BatteryBreakerStatus_Object=MibScalar
batteryBreakerStatus=_BatteryBreakerStatus_Object((1,3,6,1,4,1,12148,7,3,5),_BatteryBreakerStatus_Type())
batteryBreakerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryBreakerStatus.setStatus(_A)
class _BatteryChargeCurrentLimitCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('deactivate',0),('activate',1)))
_BatteryChargeCurrentLimitCtrl_Type.__name__=_B
_BatteryChargeCurrentLimitCtrl_Object=MibScalar
batteryChargeCurrentLimitCtrl=_BatteryChargeCurrentLimitCtrl_Object((1,3,6,1,4,1,12148,7,3,6),_BatteryChargeCurrentLimitCtrl_Type())
batteryChargeCurrentLimitCtrl.setMaxAccess(_G)
if mibBuilder.loadTexts:batteryChargeCurrentLimitCtrl.setStatus(_A)
class _BatteryChargeCurrentLimitValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2100))
_BatteryChargeCurrentLimitValue_Type.__name__=_B
_BatteryChargeCurrentLimitValue_Object=MibScalar
batteryChargeCurrentLimitValue=_BatteryChargeCurrentLimitValue_Object((1,3,6,1,4,1,12148,7,3,7),_BatteryChargeCurrentLimitValue_Type())
batteryChargeCurrentLimitValue.setMaxAccess(_G)
if mibBuilder.loadTexts:batteryChargeCurrentLimitValue.setStatus(_A)
if mibBuilder.loadTexts:batteryChargeCurrentLimitValue.setUnits(_K)
class _BatteryTempCompEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_T,1)))
_BatteryTempCompEnable_Type.__name__=_B
_BatteryTempCompEnable_Object=MibScalar
batteryTempCompEnable=_BatteryTempCompEnable_Object((1,3,6,1,4,1,12148,7,3,8),_BatteryTempCompEnable_Type())
batteryTempCompEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:batteryTempCompEnable.setStatus(_A)
class _BatteryFloatVoltConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4300,6000))
_BatteryFloatVoltConfig_Type.__name__=_B
_BatteryFloatVoltConfig_Object=MibScalar
batteryFloatVoltConfig=_BatteryFloatVoltConfig_Object((1,3,6,1,4,1,12148,7,3,9),_BatteryFloatVoltConfig_Type())
batteryFloatVoltConfig.setMaxAccess(_G)
if mibBuilder.loadTexts:batteryFloatVoltConfig.setStatus(_A)
if mibBuilder.loadTexts:batteryFloatVoltConfig.setUnits(_H)
class _BatteryEqualizeVoltConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4300,6000))
_BatteryEqualizeVoltConfig_Type.__name__=_B
_BatteryEqualizeVoltConfig_Object=MibScalar
batteryEqualizeVoltConfig=_BatteryEqualizeVoltConfig_Object((1,3,6,1,4,1,12148,7,3,10),_BatteryEqualizeVoltConfig_Type())
batteryEqualizeVoltConfig.setMaxAccess(_G)
if mibBuilder.loadTexts:batteryEqualizeVoltConfig.setStatus(_A)
if mibBuilder.loadTexts:batteryEqualizeVoltConfig.setUnits(_H)
_BatteryHighMajorAlarmVoltageConfig_Type=Integer32
_BatteryHighMajorAlarmVoltageConfig_Object=MibScalar
batteryHighMajorAlarmVoltageConfig=_BatteryHighMajorAlarmVoltageConfig_Object((1,3,6,1,4,1,12148,7,3,11),_BatteryHighMajorAlarmVoltageConfig_Type())
batteryHighMajorAlarmVoltageConfig.setMaxAccess(_G)
if mibBuilder.loadTexts:batteryHighMajorAlarmVoltageConfig.setStatus(_A)
_BatteryHighMinorAlarmVoltageConfig_Type=Integer32
_BatteryHighMinorAlarmVoltageConfig_Object=MibScalar
batteryHighMinorAlarmVoltageConfig=_BatteryHighMinorAlarmVoltageConfig_Object((1,3,6,1,4,1,12148,7,3,12),_BatteryHighMinorAlarmVoltageConfig_Type())
batteryHighMinorAlarmVoltageConfig.setMaxAccess(_G)
if mibBuilder.loadTexts:batteryHighMinorAlarmVoltageConfig.setStatus(_A)
if mibBuilder.loadTexts:batteryHighMinorAlarmVoltageConfig.setUnits(_H)
_BatteryLowMajorAlarmVoltageConfig_Type=Integer32
_BatteryLowMajorAlarmVoltageConfig_Object=MibScalar
batteryLowMajorAlarmVoltageConfig=_BatteryLowMajorAlarmVoltageConfig_Object((1,3,6,1,4,1,12148,7,3,13),_BatteryLowMajorAlarmVoltageConfig_Type())
batteryLowMajorAlarmVoltageConfig.setMaxAccess(_G)
if mibBuilder.loadTexts:batteryLowMajorAlarmVoltageConfig.setStatus(_A)
if mibBuilder.loadTexts:batteryLowMajorAlarmVoltageConfig.setUnits(_H)
_BatteryLowMinorAlarmVoltageConfig_Type=Integer32
_BatteryLowMinorAlarmVoltageConfig_Object=MibScalar
batteryLowMinorAlarmVoltageConfig=_BatteryLowMinorAlarmVoltageConfig_Object((1,3,6,1,4,1,12148,7,3,14),_BatteryLowMinorAlarmVoltageConfig_Type())
batteryLowMinorAlarmVoltageConfig.setMaxAccess(_G)
if mibBuilder.loadTexts:batteryLowMinorAlarmVoltageConfig.setStatus(_A)
if mibBuilder.loadTexts:batteryLowMinorAlarmVoltageConfig.setUnits(_H)
class _BatteryStartManualTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('starttest',1),('stoptest',2)))
_BatteryStartManualTest_Type.__name__=_B
_BatteryStartManualTest_Object=MibScalar
batteryStartManualTest=_BatteryStartManualTest_Object((1,3,6,1,4,1,12148,7,3,15),_BatteryStartManualTest_Type())
batteryStartManualTest.setMaxAccess(_G)
if mibBuilder.loadTexts:batteryStartManualTest.setStatus(_A)
class _BatteryStartManualBoost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('startboost',1),('stopboost',2)))
_BatteryStartManualBoost_Type.__name__=_B
_BatteryStartManualBoost_Object=MibScalar
batteryStartManualBoost=_BatteryStartManualBoost_Object((1,3,6,1,4,1,12148,7,3,16),_BatteryStartManualBoost_Type())
batteryStartManualBoost.setMaxAccess(_G)
if mibBuilder.loadTexts:batteryStartManualBoost.setStatus(_A)
_BatteryLVD_ObjectIdentity=ObjectIdentity
batteryLVD=_BatteryLVD_ObjectIdentity((1,3,6,1,4,1,12148,7,3,17))
class _BatteryLVDStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_J,2)))
_BatteryLVDStatus_Type.__name__=_B
_BatteryLVDStatus_Object=MibScalar
batteryLVDStatus=_BatteryLVDStatus_Object((1,3,6,1,4,1,12148,7,3,17,1),_BatteryLVDStatus_Type())
batteryLVDStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryLVDStatus.setStatus(_A)
class _BatteryLVDDisconnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_BatteryLVDDisconnectVoltage_Type.__name__=_B
_BatteryLVDDisconnectVoltage_Object=MibScalar
batteryLVDDisconnectVoltage=_BatteryLVDDisconnectVoltage_Object((1,3,6,1,4,1,12148,7,3,17,2),_BatteryLVDDisconnectVoltage_Type())
batteryLVDDisconnectVoltage.setMaxAccess(_G)
if mibBuilder.loadTexts:batteryLVDDisconnectVoltage.setStatus(_A)
if mibBuilder.loadTexts:batteryLVDDisconnectVoltage.setUnits(_H)
class _BatteryLVDConnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_BatteryLVDConnectVoltage_Type.__name__=_B
_BatteryLVDConnectVoltage_Object=MibScalar
batteryLVDConnectVoltage=_BatteryLVDConnectVoltage_Object((1,3,6,1,4,1,12148,7,3,17,3),_BatteryLVDConnectVoltage_Type())
batteryLVDConnectVoltage.setMaxAccess(_G)
if mibBuilder.loadTexts:batteryLVDConnectVoltage.setStatus(_A)
if mibBuilder.loadTexts:batteryLVDConnectVoltage.setUnits(_H)
_BatteryMidpoint_ObjectIdentity=ObjectIdentity
batteryMidpoint=_BatteryMidpoint_ObjectIdentity((1,3,6,1,4,1,12148,7,3,18))
_BatteryMidpointDeltaLimitVoltage_Type=Integer32
_BatteryMidpointDeltaLimitVoltage_Object=MibScalar
batteryMidpointDeltaLimitVoltage=_BatteryMidpointDeltaLimitVoltage_Object((1,3,6,1,4,1,12148,7,3,18,1),_BatteryMidpointDeltaLimitVoltage_Type())
batteryMidpointDeltaLimitVoltage.setMaxAccess(_G)
if mibBuilder.loadTexts:batteryMidpointDeltaLimitVoltage.setStatus(_A)
if mibBuilder.loadTexts:batteryMidpointDeltaLimitVoltage.setUnits('1/100 Volt; i.e. 25 = 2.50V')
class _BatteryMidpointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BatteryMidpointIndex_Type.__name__=_B
_BatteryMidpointIndex_Object=MibScalar
batteryMidpointIndex=_BatteryMidpointIndex_Object((1,3,6,1,4,1,12148,7,3,18,2),_BatteryMidpointIndex_Type())
batteryMidpointIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryMidpointIndex.setStatus(_A)
_BatteryMidpointControlTable_Object=MibTable
batteryMidpointControlTable=_BatteryMidpointControlTable_Object((1,3,6,1,4,1,12148,7,3,18,3))
if mibBuilder.loadTexts:batteryMidpointControlTable.setStatus(_A)
_BatteryMidpointControlEntry_Object=MibTableRow
batteryMidpointControlEntry=_BatteryMidpointControlEntry_Object((1,3,6,1,4,1,12148,7,3,18,3,1))
batteryMidpointControlEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:batteryMidpointControlEntry.setStatus(_A)
class _MidpointEnableID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_MidpointEnableID_Type.__name__=_B
_MidpointEnableID_Object=MibTableColumn
midpointEnableID=_MidpointEnableID_Object((1,3,6,1,4,1,12148,7,3,18,3,1,1),_MidpointEnableID_Type())
midpointEnableID.setMaxAccess(_C)
if mibBuilder.loadTexts:midpointEnableID.setStatus(_A)
class _MidpointEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_T,1)))
_MidpointEnable_Type.__name__=_B
_MidpointEnable_Object=MibTableColumn
midpointEnable=_MidpointEnable_Object((1,3,6,1,4,1,12148,7,3,18,3,1,2),_MidpointEnable_Type())
midpointEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:midpointEnable.setStatus(_A)
_BatteryMidpointStatusTable_Object=MibTable
batteryMidpointStatusTable=_BatteryMidpointStatusTable_Object((1,3,6,1,4,1,12148,7,3,18,4))
if mibBuilder.loadTexts:batteryMidpointStatusTable.setStatus(_A)
_BatteryMidpointStatusEntry_Object=MibTableRow
batteryMidpointStatusEntry=_BatteryMidpointStatusEntry_Object((1,3,6,1,4,1,12148,7,3,18,4,1))
batteryMidpointStatusEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:batteryMidpointStatusEntry.setStatus(_A)
class _MidpointStatusID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_MidpointStatusID_Type.__name__=_B
_MidpointStatusID_Object=MibTableColumn
midpointStatusID=_MidpointStatusID_Object((1,3,6,1,4,1,12148,7,3,18,4,1,1),_MidpointStatusID_Type())
midpointStatusID.setMaxAccess(_C)
if mibBuilder.loadTexts:midpointStatusID.setStatus(_A)
class _MidpointStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ok',0),(_E,1),(_J,2)))
_MidpointStatus_Type.__name__=_B
_MidpointStatus_Object=MibTableColumn
midpointStatus=_MidpointStatus_Object((1,3,6,1,4,1,12148,7,3,18,4,1,2),_MidpointStatus_Type())
midpointStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:midpointStatus.setStatus(_A)
_MidpointDeltaVoltage_Type=Integer32
_MidpointDeltaVoltage_Object=MibTableColumn
midpointDeltaVoltage=_MidpointDeltaVoltage_Object((1,3,6,1,4,1,12148,7,3,18,4,1,3),_MidpointDeltaVoltage_Type())
midpointDeltaVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:midpointDeltaVoltage.setStatus(_A)
if mibBuilder.loadTexts:midpointDeltaVoltage.setUnits('1/100 Volt; i.e. 25 = 2.5V.')
_LoadDistribution_ObjectIdentity=ObjectIdentity
loadDistribution=_LoadDistribution_ObjectIdentity((1,3,6,1,4,1,12148,7,4))
_LoadDistributionCurrent_Type=Integer32
_LoadDistributionCurrent_Object=MibScalar
loadDistributionCurrent=_LoadDistributionCurrent_Object((1,3,6,1,4,1,12148,7,4,1),_LoadDistributionCurrent_Type())
loadDistributionCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:loadDistributionCurrent.setStatus(_A)
if mibBuilder.loadTexts:loadDistributionCurrent.setUnits(_K)
class _LoadDistributionBreakerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),('open',1)))
_LoadDistributionBreakerStatus_Type.__name__=_B
_LoadDistributionBreakerStatus_Object=MibScalar
loadDistributionBreakerStatus=_LoadDistributionBreakerStatus_Object((1,3,6,1,4,1,12148,7,4,2),_LoadDistributionBreakerStatus_Type())
loadDistributionBreakerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:loadDistributionBreakerStatus.setStatus(_A)
_LoadDistributionLVDStatus_ObjectIdentity=ObjectIdentity
loadDistributionLVDStatus=_LoadDistributionLVDStatus_ObjectIdentity((1,3,6,1,4,1,12148,7,4,3))
class _LoadLVD1EnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_LoadLVD1EnableStatus_Type.__name__=_B
_LoadLVD1EnableStatus_Object=MibScalar
loadLVD1EnableStatus=_LoadLVD1EnableStatus_Object((1,3,6,1,4,1,12148,7,4,3,1),_LoadLVD1EnableStatus_Type())
loadLVD1EnableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:loadLVD1EnableStatus.setStatus(_A)
class _LoadLVD1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_J,2)))
_LoadLVD1Status_Type.__name__=_B
_LoadLVD1Status_Object=MibScalar
loadLVD1Status=_LoadLVD1Status_Object((1,3,6,1,4,1,12148,7,4,3,2),_LoadLVD1Status_Type())
loadLVD1Status.setMaxAccess(_C)
if mibBuilder.loadTexts:loadLVD1Status.setStatus(_A)
class _LoadLVD1ConnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_LoadLVD1ConnectVoltage_Type.__name__=_B
_LoadLVD1ConnectVoltage_Object=MibScalar
loadLVD1ConnectVoltage=_LoadLVD1ConnectVoltage_Object((1,3,6,1,4,1,12148,7,4,3,3),_LoadLVD1ConnectVoltage_Type())
loadLVD1ConnectVoltage.setMaxAccess(_G)
if mibBuilder.loadTexts:loadLVD1ConnectVoltage.setStatus(_A)
if mibBuilder.loadTexts:loadLVD1ConnectVoltage.setUnits(_H)
class _LoadLVD1DisconnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_LoadLVD1DisconnectVoltage_Type.__name__=_B
_LoadLVD1DisconnectVoltage_Object=MibScalar
loadLVD1DisconnectVoltage=_LoadLVD1DisconnectVoltage_Object((1,3,6,1,4,1,12148,7,4,3,4),_LoadLVD1DisconnectVoltage_Type())
loadLVD1DisconnectVoltage.setMaxAccess(_G)
if mibBuilder.loadTexts:loadLVD1DisconnectVoltage.setStatus(_A)
if mibBuilder.loadTexts:loadLVD1DisconnectVoltage.setUnits(_H)
class _LoadLVD2EnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_LoadLVD2EnableStatus_Type.__name__=_B
_LoadLVD2EnableStatus_Object=MibScalar
loadLVD2EnableStatus=_LoadLVD2EnableStatus_Object((1,3,6,1,4,1,12148,7,4,3,5),_LoadLVD2EnableStatus_Type())
loadLVD2EnableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:loadLVD2EnableStatus.setStatus(_A)
class _LoadLVD2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_J,2)))
_LoadLVD2Status_Type.__name__=_B
_LoadLVD2Status_Object=MibScalar
loadLVD2Status=_LoadLVD2Status_Object((1,3,6,1,4,1,12148,7,4,3,6),_LoadLVD2Status_Type())
loadLVD2Status.setMaxAccess(_C)
if mibBuilder.loadTexts:loadLVD2Status.setStatus(_A)
class _LoadLVD2ConnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_LoadLVD2ConnectVoltage_Type.__name__=_B
_LoadLVD2ConnectVoltage_Object=MibScalar
loadLVD2ConnectVoltage=_LoadLVD2ConnectVoltage_Object((1,3,6,1,4,1,12148,7,4,3,7),_LoadLVD2ConnectVoltage_Type())
loadLVD2ConnectVoltage.setMaxAccess(_G)
if mibBuilder.loadTexts:loadLVD2ConnectVoltage.setStatus(_A)
if mibBuilder.loadTexts:loadLVD2ConnectVoltage.setUnits(_H)
class _LoadLVD2DisconnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_LoadLVD2DisconnectVoltage_Type.__name__=_B
_LoadLVD2DisconnectVoltage_Object=MibScalar
loadLVD2DisconnectVoltage=_LoadLVD2DisconnectVoltage_Object((1,3,6,1,4,1,12148,7,4,3,8),_LoadLVD2DisconnectVoltage_Type())
loadLVD2DisconnectVoltage.setMaxAccess(_G)
if mibBuilder.loadTexts:loadLVD2DisconnectVoltage.setStatus(_A)
if mibBuilder.loadTexts:loadLVD2DisconnectVoltage.setUnits(_H)
class _LoadLVD3EnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_LoadLVD3EnableStatus_Type.__name__=_B
_LoadLVD3EnableStatus_Object=MibScalar
loadLVD3EnableStatus=_LoadLVD3EnableStatus_Object((1,3,6,1,4,1,12148,7,4,3,9),_LoadLVD3EnableStatus_Type())
loadLVD3EnableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:loadLVD3EnableStatus.setStatus(_A)
class _LoadLVD3Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_J,2)))
_LoadLVD3Status_Type.__name__=_B
_LoadLVD3Status_Object=MibScalar
loadLVD3Status=_LoadLVD3Status_Object((1,3,6,1,4,1,12148,7,4,3,10),_LoadLVD3Status_Type())
loadLVD3Status.setMaxAccess(_C)
if mibBuilder.loadTexts:loadLVD3Status.setStatus(_A)
class _LoadLVD3ConnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_LoadLVD3ConnectVoltage_Type.__name__=_B
_LoadLVD3ConnectVoltage_Object=MibScalar
loadLVD3ConnectVoltage=_LoadLVD3ConnectVoltage_Object((1,3,6,1,4,1,12148,7,4,3,11),_LoadLVD3ConnectVoltage_Type())
loadLVD3ConnectVoltage.setMaxAccess(_G)
if mibBuilder.loadTexts:loadLVD3ConnectVoltage.setStatus(_A)
if mibBuilder.loadTexts:loadLVD3ConnectVoltage.setUnits(_H)
class _LoadLVD3DisconnectVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_LoadLVD3DisconnectVoltage_Type.__name__=_B
_LoadLVD3DisconnectVoltage_Object=MibScalar
loadLVD3DisconnectVoltage=_LoadLVD3DisconnectVoltage_Object((1,3,6,1,4,1,12148,7,4,3,12),_LoadLVD3DisconnectVoltage_Type())
loadLVD3DisconnectVoltage.setMaxAccess(_G)
if mibBuilder.loadTexts:loadLVD3DisconnectVoltage.setStatus(_A)
if mibBuilder.loadTexts:loadLVD3DisconnectVoltage.setUnits(_H)
_Rectifier_ObjectIdentity=ObjectIdentity
rectifier=_Rectifier_ObjectIdentity((1,3,6,1,4,1,12148,7,5))
class _RectifierInstalledRectifiers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,101))
_RectifierInstalledRectifiers_Type.__name__=_B
_RectifierInstalledRectifiers_Object=MibScalar
rectifierInstalledRectifiers=_RectifierInstalledRectifiers_Object((1,3,6,1,4,1,12148,7,5,1),_RectifierInstalledRectifiers_Type())
rectifierInstalledRectifiers.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierInstalledRectifiers.setStatus(_A)
class _RectifierRectifiersActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,101))
_RectifierRectifiersActive_Type.__name__=_B
_RectifierRectifiersActive_Object=MibScalar
rectifierRectifiersActive=_RectifierRectifiersActive_Object((1,3,6,1,4,1,12148,7,5,2),_RectifierRectifiersActive_Type())
rectifierRectifiersActive.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierRectifiersActive.setStatus(_A)
_RectifierTotalCurrent_Type=Integer32
_RectifierTotalCurrent_Object=MibScalar
rectifierTotalCurrent=_RectifierTotalCurrent_Object((1,3,6,1,4,1,12148,7,5,3),_RectifierTotalCurrent_Type())
rectifierTotalCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierTotalCurrent.setStatus(_A)
if mibBuilder.loadTexts:rectifierTotalCurrent.setUnits(_K)
class _RectifierUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RectifierUtilization_Type.__name__=_B
_RectifierUtilization_Object=MibScalar
rectifierUtilization=_RectifierUtilization_Object((1,3,6,1,4,1,12148,7,5,4),_RectifierUtilization_Type())
rectifierUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierUtilization.setStatus(_A)
_RectifierStatus_ObjectIdentity=ObjectIdentity
rectifierStatus=_RectifierStatus_ObjectIdentity((1,3,6,1,4,1,12148,7,5,5))
class _RectifierStatusNoIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_RectifierStatusNoIndex_Type.__name__=_B
_RectifierStatusNoIndex_Object=MibScalar
rectifierStatusNoIndex=_RectifierStatusNoIndex_Object((1,3,6,1,4,1,12148,7,5,5,1),_RectifierStatusNoIndex_Type())
rectifierStatusNoIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rectifierStatusNoIndex.setStatus(_A)
_RectifierStatusTable_Object=MibTable
rectifierStatusTable=_RectifierStatusTable_Object((1,3,6,1,4,1,12148,7,5,5,2))
if mibBuilder.loadTexts:rectifierStatusTable.setStatus(_A)
_RectifierStatusEntry_Object=MibTableRow
rectifierStatusEntry=_RectifierStatusEntry_Object((1,3,6,1,4,1,12148,7,5,5,2,1))
rectifierStatusEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:rectifierStatusEntry.setStatus(_A)
class _RectifierStatusID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RectifierStatusID_Type.__name__=_B
_RectifierStatusID_Object=MibTableColumn
rectifierStatusID=_RectifierStatusID_Object((1,3,6,1,4,1,12148,7,5,5,2,1,1),_RectifierStatusID_Type())
rectifierStatusID.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusID.setStatus(_A)
class _RectifierStatusStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('absent',0),('active',1),('failed',2),('walkin',3),('disabledbycommand',4)))
_RectifierStatusStatus_Type.__name__=_B
_RectifierStatusStatus_Object=MibTableColumn
rectifierStatusStatus=_RectifierStatusStatus_Object((1,3,6,1,4,1,12148,7,5,5,2,1,2),_RectifierStatusStatus_Type())
rectifierStatusStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusStatus.setStatus(_A)
class _RectifierStatusOutputCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RectifierStatusOutputCurrent_Type.__name__=_B
_RectifierStatusOutputCurrent_Object=MibTableColumn
rectifierStatusOutputCurrent=_RectifierStatusOutputCurrent_Object((1,3,6,1,4,1,12148,7,5,5,2,1,3),_RectifierStatusOutputCurrent_Type())
rectifierStatusOutputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusOutputCurrent.setStatus(_A)
if mibBuilder.loadTexts:rectifierStatusOutputCurrent.setUnits('1/10 Amperes; i.e. 200 = 20 Amperes')
class _RectifierStatusOutputVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RectifierStatusOutputVoltage_Type.__name__=_B
_RectifierStatusOutputVoltage_Object=MibTableColumn
rectifierStatusOutputVoltage=_RectifierStatusOutputVoltage_Object((1,3,6,1,4,1,12148,7,5,5,2,1,4),_RectifierStatusOutputVoltage_Type())
rectifierStatusOutputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusOutputVoltage.setStatus(_A)
if mibBuilder.loadTexts:rectifierStatusOutputVoltage.setUnits(_H)
class _RectifierStatusTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RectifierStatusTemp_Type.__name__=_B
_RectifierStatusTemp_Object=MibTableColumn
rectifierStatusTemp=_RectifierStatusTemp_Object((1,3,6,1,4,1,12148,7,5,5,2,1,5),_RectifierStatusTemp_Type())
rectifierStatusTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusTemp.setStatus(_A)
if mibBuilder.loadTexts:rectifierStatusTemp.setUnits('Deg. C/10; i.e. 350 = 35.0 Deg. C')
class _RectifierStatusType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RectifierStatusType_Type.__name__=_I
_RectifierStatusType_Object=MibTableColumn
rectifierStatusType=_RectifierStatusType_Object((1,3,6,1,4,1,12148,7,5,5,2,1,6),_RectifierStatusType_Type())
rectifierStatusType.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusType.setStatus(_A)
class _RectifierStatusSKU_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RectifierStatusSKU_Type.__name__=_I
_RectifierStatusSKU_Object=MibTableColumn
rectifierStatusSKU=_RectifierStatusSKU_Object((1,3,6,1,4,1,12148,7,5,5,2,1,7),_RectifierStatusSKU_Type())
rectifierStatusSKU.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusSKU.setStatus(_A)
class _RectifierStatusSerialNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RectifierStatusSerialNo_Type.__name__=_I
_RectifierStatusSerialNo_Object=MibTableColumn
rectifierStatusSerialNo=_RectifierStatusSerialNo_Object((1,3,6,1,4,1,12148,7,5,5,2,1,8),_RectifierStatusSerialNo_Type())
rectifierStatusSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusSerialNo.setStatus(_A)
class _RectifierStatusRevisionLevel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RectifierStatusRevisionLevel_Type.__name__=_I
_RectifierStatusRevisionLevel_Object=MibTableColumn
rectifierStatusRevisionLevel=_RectifierStatusRevisionLevel_Object((1,3,6,1,4,1,12148,7,5,5,2,1,9),_RectifierStatusRevisionLevel_Type())
rectifierStatusRevisionLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:rectifierStatusRevisionLevel.setStatus(_A)
_AcDistribution_ObjectIdentity=ObjectIdentity
acDistribution=_AcDistribution_ObjectIdentity((1,3,6,1,4,1,12148,7,6))
_AcVoltage1_Type=Integer32
_AcVoltage1_Object=MibScalar
acVoltage1=_AcVoltage1_Object((1,3,6,1,4,1,12148,7,6,1),_AcVoltage1_Type())
acVoltage1.setMaxAccess(_C)
if mibBuilder.loadTexts:acVoltage1.setStatus(_A)
if mibBuilder.loadTexts:acVoltage1.setUnits(_R)
_AcVoltage2_Type=Integer32
_AcVoltage2_Object=MibScalar
acVoltage2=_AcVoltage2_Object((1,3,6,1,4,1,12148,7,6,2),_AcVoltage2_Type())
acVoltage2.setMaxAccess(_C)
if mibBuilder.loadTexts:acVoltage2.setStatus(_A)
if mibBuilder.loadTexts:acVoltage2.setUnits(_R)
_AcVoltage3_Type=Integer32
_AcVoltage3_Object=MibScalar
acVoltage3=_AcVoltage3_Object((1,3,6,1,4,1,12148,7,6,3),_AcVoltage3_Type())
acVoltage3.setMaxAccess(_C)
if mibBuilder.loadTexts:acVoltage3.setStatus(_A)
if mibBuilder.loadTexts:acVoltage3.setUnits(_R)
_AlarmGroup_ObjectIdentity=ObjectIdentity
alarmGroup=_AlarmGroup_ObjectIdentity((1,3,6,1,4,1,12148,7,7))
_AlarmWellknownAlarms_ObjectIdentity=ObjectIdentity
alarmWellknownAlarms=_AlarmWellknownAlarms_ObjectIdentity((1,3,6,1,4,1,12148,7,7,1))
class _AlarmMajorHighBattVolt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmMajorHighBattVolt_Type.__name__=_B
_AlarmMajorHighBattVolt_Object=MibScalar
alarmMajorHighBattVolt=_AlarmMajorHighBattVolt_Object((1,3,6,1,4,1,12148,7,7,1,1),_AlarmMajorHighBattVolt_Type())
alarmMajorHighBattVolt.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMajorHighBattVolt.setStatus(_A)
class _AlarmMinorHighBattVolt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmMinorHighBattVolt_Type.__name__=_B
_AlarmMinorHighBattVolt_Object=MibScalar
alarmMinorHighBattVolt=_AlarmMinorHighBattVolt_Object((1,3,6,1,4,1,12148,7,7,1,2),_AlarmMinorHighBattVolt_Type())
alarmMinorHighBattVolt.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMinorHighBattVolt.setStatus(_A)
class _AlarmMajorLowBattVolt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmMajorLowBattVolt_Type.__name__=_B
_AlarmMajorLowBattVolt_Object=MibScalar
alarmMajorLowBattVolt=_AlarmMajorLowBattVolt_Object((1,3,6,1,4,1,12148,7,7,1,3),_AlarmMajorLowBattVolt_Type())
alarmMajorLowBattVolt.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMajorLowBattVolt.setStatus(_A)
class _AlarmMinorLowBattVolt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmMinorLowBattVolt_Type.__name__=_B
_AlarmMinorLowBattVolt_Object=MibScalar
alarmMinorLowBattVolt=_AlarmMinorLowBattVolt_Object((1,3,6,1,4,1,12148,7,7,1,4),_AlarmMinorLowBattVolt_Type())
alarmMinorLowBattVolt.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMinorLowBattVolt.setStatus(_A)
class _AlarmMajorBatteryHighTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmMajorBatteryHighTemp_Type.__name__=_B
_AlarmMajorBatteryHighTemp_Object=MibScalar
alarmMajorBatteryHighTemp=_AlarmMajorBatteryHighTemp_Object((1,3,6,1,4,1,12148,7,7,1,5),_AlarmMajorBatteryHighTemp_Type())
alarmMajorBatteryHighTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMajorBatteryHighTemp.setStatus(_A)
class _AlarmMinorBatteryHighTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmMinorBatteryHighTemp_Type.__name__=_B
_AlarmMinorBatteryHighTemp_Object=MibScalar
alarmMinorBatteryHighTemp=_AlarmMinorBatteryHighTemp_Object((1,3,6,1,4,1,12148,7,7,1,6),_AlarmMinorBatteryHighTemp_Type())
alarmMinorBatteryHighTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMinorBatteryHighTemp.setStatus(_A)
class _AlarmBatteryDisconnectOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmBatteryDisconnectOpen_Type.__name__=_B
_AlarmBatteryDisconnectOpen_Object=MibScalar
alarmBatteryDisconnectOpen=_AlarmBatteryDisconnectOpen_Object((1,3,6,1,4,1,12148,7,7,1,7),_AlarmBatteryDisconnectOpen_Type())
alarmBatteryDisconnectOpen.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmBatteryDisconnectOpen.setStatus(_A)
class _AlarmLVD1open_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmLVD1open_Type.__name__=_B
_AlarmLVD1open_Object=MibScalar
alarmLVD1open=_AlarmLVD1open_Object((1,3,6,1,4,1,12148,7,7,1,8),_AlarmLVD1open_Type())
alarmLVD1open.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLVD1open.setStatus(_A)
class _AlarmLVD2open_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmLVD2open_Type.__name__=_B
_AlarmLVD2open_Object=MibScalar
alarmLVD2open=_AlarmLVD2open_Object((1,3,6,1,4,1,12148,7,7,1,9),_AlarmLVD2open_Type())
alarmLVD2open.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLVD2open.setStatus(_A)
class _AlarmLVD3open_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmLVD3open_Type.__name__=_B
_AlarmLVD3open_Object=MibScalar
alarmLVD3open=_AlarmLVD3open_Object((1,3,6,1,4,1,12148,7,7,1,10),_AlarmLVD3open_Type())
alarmLVD3open.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLVD3open.setStatus(_A)
class _AlarmACmains_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmACmains_Type.__name__=_B
_AlarmACmains_Object=MibScalar
alarmACmains=_AlarmACmains_Object((1,3,6,1,4,1,12148,7,7,1,11),_AlarmACmains_Type())
alarmACmains.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmACmains.setStatus(_A)
class _AlarmBatteryBreakerOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmBatteryBreakerOpen_Type.__name__=_B
_AlarmBatteryBreakerOpen_Object=MibScalar
alarmBatteryBreakerOpen=_AlarmBatteryBreakerOpen_Object((1,3,6,1,4,1,12148,7,7,1,12),_AlarmBatteryBreakerOpen_Type())
alarmBatteryBreakerOpen.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmBatteryBreakerOpen.setStatus(_A)
class _AlarmDistributionBreakerOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmDistributionBreakerOpen_Type.__name__=_B
_AlarmDistributionBreakerOpen_Object=MibScalar
alarmDistributionBreakerOpen=_AlarmDistributionBreakerOpen_Object((1,3,6,1,4,1,12148,7,7,1,13),_AlarmDistributionBreakerOpen_Type())
alarmDistributionBreakerOpen.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmDistributionBreakerOpen.setStatus(_A)
class _AlarmMajorRectifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmMajorRectifier_Type.__name__=_B
_AlarmMajorRectifier_Object=MibScalar
alarmMajorRectifier=_AlarmMajorRectifier_Object((1,3,6,1,4,1,12148,7,7,1,14),_AlarmMajorRectifier_Type())
alarmMajorRectifier.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMajorRectifier.setStatus(_A)
class _AlarmMinorRectifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmMinorRectifier_Type.__name__=_B
_AlarmMinorRectifier_Object=MibScalar
alarmMinorRectifier=_AlarmMinorRectifier_Object((1,3,6,1,4,1,12148,7,7,1,15),_AlarmMinorRectifier_Type())
alarmMinorRectifier.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMinorRectifier.setStatus(_A)
class _AlarmMajorBatteryMidpoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmMajorBatteryMidpoint_Type.__name__=_B
_AlarmMajorBatteryMidpoint_Object=MibScalar
alarmMajorBatteryMidpoint=_AlarmMajorBatteryMidpoint_Object((1,3,6,1,4,1,12148,7,7,1,16),_AlarmMajorBatteryMidpoint_Type())
alarmMajorBatteryMidpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMajorBatteryMidpoint.setStatus(_A)
class _AlarmMinorBatteryMidpoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmMinorBatteryMidpoint_Type.__name__=_B
_AlarmMinorBatteryMidpoint_Object=MibScalar
alarmMinorBatteryMidpoint=_AlarmMinorBatteryMidpoint_Object((1,3,6,1,4,1,12148,7,7,1,17),_AlarmMinorBatteryMidpoint_Type())
alarmMinorBatteryMidpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMinorBatteryMidpoint.setStatus(_A)
class _AlarmBatteryLifeEnded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmBatteryLifeEnded_Type.__name__=_B
_AlarmBatteryLifeEnded_Object=MibScalar
alarmBatteryLifeEnded=_AlarmBatteryLifeEnded_Object((1,3,6,1,4,1,12148,7,7,1,18),_AlarmBatteryLifeEnded_Type())
alarmBatteryLifeEnded.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmBatteryLifeEnded.setStatus(_A)
class _AlarmBatteryTestmodeEntered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmBatteryTestmodeEntered_Type.__name__=_B
_AlarmBatteryTestmodeEntered_Object=MibScalar
alarmBatteryTestmodeEntered=_AlarmBatteryTestmodeEntered_Object((1,3,6,1,4,1,12148,7,7,1,19),_AlarmBatteryTestmodeEntered_Type())
alarmBatteryTestmodeEntered.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmBatteryTestmodeEntered.setStatus(_A)
class _AlarmBatteryBoostmodeEntered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmBatteryBoostmodeEntered_Type.__name__=_B
_AlarmBatteryBoostmodeEntered_Object=MibScalar
alarmBatteryBoostmodeEntered=_AlarmBatteryBoostmodeEntered_Object((1,3,6,1,4,1,12148,7,7,1,20),_AlarmBatteryBoostmodeEntered_Type())
alarmBatteryBoostmodeEntered.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmBatteryBoostmodeEntered.setStatus(_A)
class _AlarmUserConfigurable1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmUserConfigurable1_Type.__name__=_B
_AlarmUserConfigurable1_Object=MibScalar
alarmUserConfigurable1=_AlarmUserConfigurable1_Object((1,3,6,1,4,1,12148,7,7,1,21),_AlarmUserConfigurable1_Type())
alarmUserConfigurable1.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmUserConfigurable1.setStatus(_A)
class _AlarmUserConfigurable2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmUserConfigurable2_Type.__name__=_B
_AlarmUserConfigurable2_Object=MibScalar
alarmUserConfigurable2=_AlarmUserConfigurable2_Object((1,3,6,1,4,1,12148,7,7,1,22),_AlarmUserConfigurable2_Type())
alarmUserConfigurable2.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmUserConfigurable2.setStatus(_A)
class _AlarmUserConfigurable3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmUserConfigurable3_Type.__name__=_B
_AlarmUserConfigurable3_Object=MibScalar
alarmUserConfigurable3=_AlarmUserConfigurable3_Object((1,3,6,1,4,1,12148,7,7,1,23),_AlarmUserConfigurable3_Type())
alarmUserConfigurable3.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmUserConfigurable3.setStatus(_A)
class _AlarmUserConfigurable4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmUserConfigurable4_Type.__name__=_B
_AlarmUserConfigurable4_Object=MibScalar
alarmUserConfigurable4=_AlarmUserConfigurable4_Object((1,3,6,1,4,1,12148,7,7,1,24),_AlarmUserConfigurable4_Type())
alarmUserConfigurable4.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmUserConfigurable4.setStatus(_A)
class _AlarmUserConfigurable5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmUserConfigurable5_Type.__name__=_B
_AlarmUserConfigurable5_Object=MibScalar
alarmUserConfigurable5=_AlarmUserConfigurable5_Object((1,3,6,1,4,1,12148,7,7,1,25),_AlarmUserConfigurable5_Type())
alarmUserConfigurable5.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmUserConfigurable5.setStatus(_A)
class _AlarmUserConfigurable6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmUserConfigurable6_Type.__name__=_B
_AlarmUserConfigurable6_Object=MibScalar
alarmUserConfigurable6=_AlarmUserConfigurable6_Object((1,3,6,1,4,1,12148,7,7,1,26),_AlarmUserConfigurable6_Type())
alarmUserConfigurable6.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmUserConfigurable6.setStatus(_A)
class _AlarmUserConfigurable7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmUserConfigurable7_Type.__name__=_B
_AlarmUserConfigurable7_Object=MibScalar
alarmUserConfigurable7=_AlarmUserConfigurable7_Object((1,3,6,1,4,1,12148,7,7,1,27),_AlarmUserConfigurable7_Type())
alarmUserConfigurable7.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmUserConfigurable7.setStatus(_A)
class _AlarmUserConfigurable8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmUserConfigurable8_Type.__name__=_B
_AlarmUserConfigurable8_Object=MibScalar
alarmUserConfigurable8=_AlarmUserConfigurable8_Object((1,3,6,1,4,1,12148,7,7,1,28),_AlarmUserConfigurable8_Type())
alarmUserConfigurable8.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmUserConfigurable8.setStatus(_A)
class _AlarmUserConfigurable9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmUserConfigurable9_Type.__name__=_B
_AlarmUserConfigurable9_Object=MibScalar
alarmUserConfigurable9=_AlarmUserConfigurable9_Object((1,3,6,1,4,1,12148,7,7,1,29),_AlarmUserConfigurable9_Type())
alarmUserConfigurable9.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmUserConfigurable9.setStatus(_A)
class _AlarmUserConfigurable10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmUserConfigurable10_Type.__name__=_B
_AlarmUserConfigurable10_Object=MibScalar
alarmUserConfigurable10=_AlarmUserConfigurable10_Object((1,3,6,1,4,1,12148,7,7,1,30),_AlarmUserConfigurable10_Type())
alarmUserConfigurable10.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmUserConfigurable10.setStatus(_A)
class _AlarmUserConfigurable11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmUserConfigurable11_Type.__name__=_B
_AlarmUserConfigurable11_Object=MibScalar
alarmUserConfigurable11=_AlarmUserConfigurable11_Object((1,3,6,1,4,1,12148,7,7,1,31),_AlarmUserConfigurable11_Type())
alarmUserConfigurable11.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmUserConfigurable11.setStatus(_A)
class _AlarmUserConfigurable12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmUserConfigurable12_Type.__name__=_B
_AlarmUserConfigurable12_Object=MibScalar
alarmUserConfigurable12=_AlarmUserConfigurable12_Object((1,3,6,1,4,1,12148,7,7,1,32),_AlarmUserConfigurable12_Type())
alarmUserConfigurable12.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmUserConfigurable12.setStatus(_A)
class _AlarmUserConfigurable13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmUserConfigurable13_Type.__name__=_B
_AlarmUserConfigurable13_Object=MibScalar
alarmUserConfigurable13=_AlarmUserConfigurable13_Object((1,3,6,1,4,1,12148,7,7,1,33),_AlarmUserConfigurable13_Type())
alarmUserConfigurable13.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmUserConfigurable13.setStatus(_A)
class _AlarmUserConfigurable14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_AlarmUserConfigurable14_Type.__name__=_B
_AlarmUserConfigurable14_Object=MibScalar
alarmUserConfigurable14=_AlarmUserConfigurable14_Object((1,3,6,1,4,1,12148,7,7,1,34),_AlarmUserConfigurable14_Type())
alarmUserConfigurable14.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmUserConfigurable14.setStatus(_A)
alarmMajorHighBattVoltTrap=NotificationType((1,3,6,1,4,1,12148,7,8,1))
alarmMajorHighBattVoltTrap.setObjects((_D,_V))
if mibBuilder.loadTexts:alarmMajorHighBattVoltTrap.setStatus(_A)
alarmMinorHighBattVoltTrap=NotificationType((1,3,6,1,4,1,12148,7,8,2))
alarmMinorHighBattVoltTrap.setObjects((_D,_W))
if mibBuilder.loadTexts:alarmMinorHighBattVoltTrap.setStatus(_A)
alarmMajorLowBattVoltTrap=NotificationType((1,3,6,1,4,1,12148,7,8,3))
alarmMajorLowBattVoltTrap.setObjects((_D,_X))
if mibBuilder.loadTexts:alarmMajorLowBattVoltTrap.setStatus(_A)
alarmMinorLowBattVoltTrap=NotificationType((1,3,6,1,4,1,12148,7,8,4))
alarmMinorLowBattVoltTrap.setObjects((_D,_Y))
if mibBuilder.loadTexts:alarmMinorLowBattVoltTrap.setStatus(_A)
alarmMajorBatteryHighTempTrap=NotificationType((1,3,6,1,4,1,12148,7,8,5))
alarmMajorBatteryHighTempTrap.setObjects((_D,_Z))
if mibBuilder.loadTexts:alarmMajorBatteryHighTempTrap.setStatus(_A)
alarmMinorBatteryHighTempTrap=NotificationType((1,3,6,1,4,1,12148,7,8,6))
alarmMinorBatteryHighTempTrap.setObjects((_D,_a))
if mibBuilder.loadTexts:alarmMinorBatteryHighTempTrap.setStatus(_A)
alarmBatteryDisconnectOpenTrap=NotificationType((1,3,6,1,4,1,12148,7,8,7))
alarmBatteryDisconnectOpenTrap.setObjects((_D,_b))
if mibBuilder.loadTexts:alarmBatteryDisconnectOpenTrap.setStatus(_A)
alarmLVD1openTrap=NotificationType((1,3,6,1,4,1,12148,7,8,8))
alarmLVD1openTrap.setObjects((_D,_c))
if mibBuilder.loadTexts:alarmLVD1openTrap.setStatus(_A)
alarmLVD2openTrap=NotificationType((1,3,6,1,4,1,12148,7,8,9))
alarmLVD2openTrap.setObjects((_D,_d))
if mibBuilder.loadTexts:alarmLVD2openTrap.setStatus(_A)
alarmLVD3openTrap=NotificationType((1,3,6,1,4,1,12148,7,8,10))
alarmLVD3openTrap.setObjects((_D,_e))
if mibBuilder.loadTexts:alarmLVD3openTrap.setStatus(_A)
alarmACmainsTrap=NotificationType((1,3,6,1,4,1,12148,7,8,11))
alarmACmainsTrap.setObjects((_D,_f))
if mibBuilder.loadTexts:alarmACmainsTrap.setStatus(_A)
alarmBatteryBreakerOpenTrap=NotificationType((1,3,6,1,4,1,12148,7,8,12))
alarmBatteryBreakerOpenTrap.setObjects((_D,_g))
if mibBuilder.loadTexts:alarmBatteryBreakerOpenTrap.setStatus(_A)
alarmDistributionBreakerOpenTrap=NotificationType((1,3,6,1,4,1,12148,7,8,13))
alarmDistributionBreakerOpenTrap.setObjects((_D,_h))
if mibBuilder.loadTexts:alarmDistributionBreakerOpenTrap.setStatus(_A)
alarmMajorRectifierTrap=NotificationType((1,3,6,1,4,1,12148,7,8,14))
alarmMajorRectifierTrap.setObjects((_D,_i))
if mibBuilder.loadTexts:alarmMajorRectifierTrap.setStatus(_A)
alarmMinorRectifierTrap=NotificationType((1,3,6,1,4,1,12148,7,8,15))
alarmMinorRectifierTrap.setObjects((_D,_j))
if mibBuilder.loadTexts:alarmMinorRectifierTrap.setStatus(_A)
alarmMajorBatteryMidpointTrap=NotificationType((1,3,6,1,4,1,12148,7,8,16))
alarmMajorBatteryMidpointTrap.setObjects((_D,_k))
if mibBuilder.loadTexts:alarmMajorBatteryMidpointTrap.setStatus(_A)
alarmMinorBatteryMidpointTrap=NotificationType((1,3,6,1,4,1,12148,7,8,17))
alarmMinorBatteryMidpointTrap.setObjects((_D,_l))
if mibBuilder.loadTexts:alarmMinorBatteryMidpointTrap.setStatus(_A)
alarmBatteryLifeEndedTrap=NotificationType((1,3,6,1,4,1,12148,7,8,18))
alarmBatteryLifeEndedTrap.setObjects((_D,_m))
if mibBuilder.loadTexts:alarmBatteryLifeEndedTrap.setStatus(_A)
alarmBatteryTestmodeEnteredTrap=NotificationType((1,3,6,1,4,1,12148,7,8,19))
alarmBatteryTestmodeEnteredTrap.setObjects((_D,_n))
if mibBuilder.loadTexts:alarmBatteryTestmodeEnteredTrap.setStatus(_A)
alarmBatteryBoostmodeEnteredTrap=NotificationType((1,3,6,1,4,1,12148,7,8,20))
alarmBatteryBoostmodeEnteredTrap.setObjects((_D,_o))
if mibBuilder.loadTexts:alarmBatteryBoostmodeEnteredTrap.setStatus(_A)
alarmUserConfigurable1Trap=NotificationType((1,3,6,1,4,1,12148,7,8,21))
alarmUserConfigurable1Trap.setObjects((_D,_p))
if mibBuilder.loadTexts:alarmUserConfigurable1Trap.setStatus(_A)
alarmUserConfigurable2Trap=NotificationType((1,3,6,1,4,1,12148,7,8,22))
alarmUserConfigurable2Trap.setObjects((_D,_q))
if mibBuilder.loadTexts:alarmUserConfigurable2Trap.setStatus(_A)
alarmUserConfigurable3Trap=NotificationType((1,3,6,1,4,1,12148,7,8,23))
alarmUserConfigurable3Trap.setObjects((_D,_r))
if mibBuilder.loadTexts:alarmUserConfigurable3Trap.setStatus(_A)
alarmUserConfigurable4Trap=NotificationType((1,3,6,1,4,1,12148,7,8,24))
alarmUserConfigurable4Trap.setObjects((_D,_s))
if mibBuilder.loadTexts:alarmUserConfigurable4Trap.setStatus(_A)
alarmUserConfigurable5Trap=NotificationType((1,3,6,1,4,1,12148,7,8,25))
alarmUserConfigurable5Trap.setObjects((_D,_t))
if mibBuilder.loadTexts:alarmUserConfigurable5Trap.setStatus(_A)
alarmUserConfigurable6Trap=NotificationType((1,3,6,1,4,1,12148,7,8,26))
alarmUserConfigurable6Trap.setObjects((_D,_u))
if mibBuilder.loadTexts:alarmUserConfigurable6Trap.setStatus(_A)
alarmUserConfigurable7Trap=NotificationType((1,3,6,1,4,1,12148,7,8,27))
alarmUserConfigurable7Trap.setObjects((_D,_v))
if mibBuilder.loadTexts:alarmUserConfigurable7Trap.setStatus(_A)
alarmUserConfigurable8Trap=NotificationType((1,3,6,1,4,1,12148,7,8,28))
alarmUserConfigurable8Trap.setObjects((_D,_w))
if mibBuilder.loadTexts:alarmUserConfigurable8Trap.setStatus(_A)
alarmUserConfigurable9Trap=NotificationType((1,3,6,1,4,1,12148,7,8,29))
alarmUserConfigurable9Trap.setObjects((_D,_x))
if mibBuilder.loadTexts:alarmUserConfigurable9Trap.setStatus(_A)
alarmUserConfigurable10Trap=NotificationType((1,3,6,1,4,1,12148,7,8,30))
alarmUserConfigurable10Trap.setObjects((_D,_y))
if mibBuilder.loadTexts:alarmUserConfigurable10Trap.setStatus(_A)
alarmUserConfigurable11Trap=NotificationType((1,3,6,1,4,1,12148,7,8,31))
alarmUserConfigurable11Trap.setObjects((_D,_z))
if mibBuilder.loadTexts:alarmUserConfigurable11Trap.setStatus(_A)
alarmUserConfigurable12Trap=NotificationType((1,3,6,1,4,1,12148,7,8,32))
alarmUserConfigurable12Trap.setObjects((_D,_A0))
if mibBuilder.loadTexts:alarmUserConfigurable12Trap.setStatus(_A)
alarmUserConfigurable13Trap=NotificationType((1,3,6,1,4,1,12148,7,8,33))
alarmUserConfigurable13Trap.setObjects((_D,_A1))
if mibBuilder.loadTexts:alarmUserConfigurable13Trap.setStatus(_A)
alarmUserConfigurable14Trap=NotificationType((1,3,6,1,4,1,12148,7,8,34))
alarmUserConfigurable14Trap.setObjects((_D,_A2))
if mibBuilder.loadTexts:alarmUserConfigurable14Trap.setStatus(_A)
dcSystemTraps=NotificationGroup((1,3,6,1,4,1,12148,7,8))
dcSystemTraps.setObjects(*((_D,_A3),(_D,_A4),(_D,_A5),(_D,_A6),(_D,_A7),(_D,_A8),(_D,_A9),(_D,_AA),(_D,_AB),(_D,_AC),(_D,_AD),(_D,_AE),(_D,_AF),(_D,_AG),(_D,_AH),(_D,_AI),(_D,_AJ),(_D,_AK),(_D,_AL),(_D,_AM),(_D,_AN),(_D,_AO),(_D,_AP),(_D,_AQ),(_D,_AR),(_D,_AS),(_D,_AT),(_D,_AU),(_D,_AV),(_D,_AW),(_D,_AX),(_D,_AY),(_D,_AZ),(_D,_Aa)))
if mibBuilder.loadTexts:dcSystemTraps.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'eltekPlant':eltekPlant,'controlSystem':controlSystem,'systemTime':systemTime,'systemTimeTime':systemTimeTime,'systemInfoRefresh':systemInfoRefresh,'systemTrapRepeatRate':systemTrapRepeatRate,'systemSendOffTrap':systemSendOffTrap,'dcSystem':dcSystem,'dcPlant':dcPlant,'systemSiteInfo':systemSiteInfo,'systemSiteInfoCustomer':systemSiteInfoCustomer,'systemSiteInfoLocation':systemSiteInfoLocation,'systemSiteInfoMessage1':systemSiteInfoMessage1,'systemSiteInfoMessage2':systemSiteInfoMessage2,'systemSiteInfoInstalledDate':systemSiteInfoInstalledDate,'systemSiteInfoControllerType':systemSiteInfoControllerType,'systemSiteInfoSystemSeriaNum':systemSiteInfoSystemSeriaNum,'systemSiteInfoControllerSeriaNum':systemSiteInfoControllerSeriaNum,'systemNominalVoltage':systemNominalVoltage,'systemOperationalStatus':systemOperationalStatus,'battery':battery,'batteryName':batteryName,'batteryVoltage':batteryVoltage,'batteryCurrent':batteryCurrent,'batteryTemp':batteryTemp,'batteryBreakerStatus':batteryBreakerStatus,'batteryChargeCurrentLimitCtrl':batteryChargeCurrentLimitCtrl,'batteryChargeCurrentLimitValue':batteryChargeCurrentLimitValue,'batteryTempCompEnable':batteryTempCompEnable,'batteryFloatVoltConfig':batteryFloatVoltConfig,'batteryEqualizeVoltConfig':batteryEqualizeVoltConfig,'batteryHighMajorAlarmVoltageConfig':batteryHighMajorAlarmVoltageConfig,'batteryHighMinorAlarmVoltageConfig':batteryHighMinorAlarmVoltageConfig,'batteryLowMajorAlarmVoltageConfig':batteryLowMajorAlarmVoltageConfig,'batteryLowMinorAlarmVoltageConfig':batteryLowMinorAlarmVoltageConfig,'batteryStartManualTest':batteryStartManualTest,'batteryStartManualBoost':batteryStartManualBoost,'batteryLVD':batteryLVD,'batteryLVDStatus':batteryLVDStatus,'batteryLVDDisconnectVoltage':batteryLVDDisconnectVoltage,'batteryLVDConnectVoltage':batteryLVDConnectVoltage,'batteryMidpoint':batteryMidpoint,'batteryMidpointDeltaLimitVoltage':batteryMidpointDeltaLimitVoltage,_O:batteryMidpointIndex,'batteryMidpointControlTable':batteryMidpointControlTable,'batteryMidpointControlEntry':batteryMidpointControlEntry,'midpointEnableID':midpointEnableID,'midpointEnable':midpointEnable,'batteryMidpointStatusTable':batteryMidpointStatusTable,'batteryMidpointStatusEntry':batteryMidpointStatusEntry,'midpointStatusID':midpointStatusID,'midpointStatus':midpointStatus,'midpointDeltaVoltage':midpointDeltaVoltage,'loadDistribution':loadDistribution,'loadDistributionCurrent':loadDistributionCurrent,'loadDistributionBreakerStatus':loadDistributionBreakerStatus,'loadDistributionLVDStatus':loadDistributionLVDStatus,'loadLVD1EnableStatus':loadLVD1EnableStatus,'loadLVD1Status':loadLVD1Status,'loadLVD1ConnectVoltage':loadLVD1ConnectVoltage,'loadLVD1DisconnectVoltage':loadLVD1DisconnectVoltage,'loadLVD2EnableStatus':loadLVD2EnableStatus,'loadLVD2Status':loadLVD2Status,'loadLVD2ConnectVoltage':loadLVD2ConnectVoltage,'loadLVD2DisconnectVoltage':loadLVD2DisconnectVoltage,'loadLVD3EnableStatus':loadLVD3EnableStatus,'loadLVD3Status':loadLVD3Status,'loadLVD3ConnectVoltage':loadLVD3ConnectVoltage,'loadLVD3DisconnectVoltage':loadLVD3DisconnectVoltage,'rectifier':rectifier,'rectifierInstalledRectifiers':rectifierInstalledRectifiers,'rectifierRectifiersActive':rectifierRectifiersActive,'rectifierTotalCurrent':rectifierTotalCurrent,'rectifierUtilization':rectifierUtilization,'rectifierStatus':rectifierStatus,'rectifierStatusNoIndex':rectifierStatusNoIndex,'rectifierStatusTable':rectifierStatusTable,'rectifierStatusEntry':rectifierStatusEntry,_U:rectifierStatusID,'rectifierStatusStatus':rectifierStatusStatus,'rectifierStatusOutputCurrent':rectifierStatusOutputCurrent,'rectifierStatusOutputVoltage':rectifierStatusOutputVoltage,'rectifierStatusTemp':rectifierStatusTemp,'rectifierStatusType':rectifierStatusType,'rectifierStatusSKU':rectifierStatusSKU,'rectifierStatusSerialNo':rectifierStatusSerialNo,'rectifierStatusRevisionLevel':rectifierStatusRevisionLevel,'acDistribution':acDistribution,'acVoltage1':acVoltage1,'acVoltage2':acVoltage2,'acVoltage3':acVoltage3,'alarmGroup':alarmGroup,'alarmWellknownAlarms':alarmWellknownAlarms,_V:alarmMajorHighBattVolt,_W:alarmMinorHighBattVolt,_X:alarmMajorLowBattVolt,_Y:alarmMinorLowBattVolt,_Z:alarmMajorBatteryHighTemp,_a:alarmMinorBatteryHighTemp,_b:alarmBatteryDisconnectOpen,_c:alarmLVD1open,_d:alarmLVD2open,_e:alarmLVD3open,_f:alarmACmains,_g:alarmBatteryBreakerOpen,_h:alarmDistributionBreakerOpen,_i:alarmMajorRectifier,_j:alarmMinorRectifier,_k:alarmMajorBatteryMidpoint,_l:alarmMinorBatteryMidpoint,_m:alarmBatteryLifeEnded,_n:alarmBatteryTestmodeEntered,_o:alarmBatteryBoostmodeEntered,_p:alarmUserConfigurable1,_q:alarmUserConfigurable2,_r:alarmUserConfigurable3,_s:alarmUserConfigurable4,_t:alarmUserConfigurable5,_u:alarmUserConfigurable6,_v:alarmUserConfigurable7,_w:alarmUserConfigurable8,_x:alarmUserConfigurable9,_y:alarmUserConfigurable10,_z:alarmUserConfigurable11,_A0:alarmUserConfigurable12,_A1:alarmUserConfigurable13,_A2:alarmUserConfigurable14,'dcSystemTraps':dcSystemTraps,_A3:alarmMajorHighBattVoltTrap,_A4:alarmMinorHighBattVoltTrap,_A5:alarmMajorLowBattVoltTrap,_A6:alarmMinorLowBattVoltTrap,_A7:alarmMajorBatteryHighTempTrap,_A8:alarmMinorBatteryHighTempTrap,_A9:alarmBatteryDisconnectOpenTrap,_AA:alarmLVD1openTrap,_AB:alarmLVD2openTrap,_AC:alarmLVD3openTrap,_AD:alarmACmainsTrap,_AE:alarmBatteryBreakerOpenTrap,_AF:alarmDistributionBreakerOpenTrap,_AG:alarmMajorRectifierTrap,_AH:alarmMinorRectifierTrap,_AI:alarmMajorBatteryMidpointTrap,_AJ:alarmMinorBatteryMidpointTrap,_AK:alarmBatteryLifeEndedTrap,_AL:alarmBatteryTestmodeEnteredTrap,_AM:alarmBatteryBoostmodeEnteredTrap,_AN:alarmUserConfigurable1Trap,_AO:alarmUserConfigurable2Trap,_AP:alarmUserConfigurable3Trap,_AQ:alarmUserConfigurable4Trap,_AR:alarmUserConfigurable5Trap,_AS:alarmUserConfigurable6Trap,_AT:alarmUserConfigurable7Trap,_AU:alarmUserConfigurable8Trap,_AV:alarmUserConfigurable9Trap,_AW:alarmUserConfigurable10Trap,_AX:alarmUserConfigurable11Trap,_AY:alarmUserConfigurable12Trap,_AZ:alarmUserConfigurable13Trap,_Aa:alarmUserConfigurable14Trap})