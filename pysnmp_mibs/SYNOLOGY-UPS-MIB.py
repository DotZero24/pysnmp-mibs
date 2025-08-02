_BN='upsServerVersion'
_BM='upsServerInfo'
_BL='upsDriverSnmpVersion'
_BK='upsDriverProductID'
_BJ='upsDriverPollFrequency'
_BI='upsDriverPort'
_BH='upsDriverPollInterval'
_BG='upsDriverVersionInternal'
_BF='upsDriverVersionData'
_BE='upsDriverVersion'
_BD='upsDriverName'
_BC='upsAmbientHumidityMin'
_BB='upsAmbientHumidityMax'
_BA='upsAmbientHumidityLow'
_B9='upsAmbientHumidityHigh'
_B8='upsAmbientHumidityAlarm'
_B7='upsAmbientHumidityValue'
_B6='upsAmbientTemperatureMin'
_B5='upsAmbientTemperatureMax'
_B4='upsAmbientTemperatureLow'
_B3='upsAmbientTemperatureHigh'
_B2='upsAmbientTemperatureAlarm'
_B1='upsAmbientTemperatureValue'
_B0='upsOutputCurrentNominal'
_A_='upsOutputCurrentValue'
_Az='upsOutputFrequencyNominal'
_Ay='upsOutputFrequencyValue'
_Ax='upsOutputVoltageNominal'
_Aw='upsOutputVoltageValue'
_Av='upsInputFrequencyExtend'
_Au='upsInputFrequencyHigh'
_At='upsInputFrequencyLow'
_As='upsInputFrequencyNominal'
_Ar='upsInputFrequencyValue'
_Aq='upsInputCurrentNominal'
_Ap='upsInputCurrentValue'
_Ao='upsInputQuality'
_An='upsInputSensitivity'
_Am='upsInputTransferTrimHigh'
_Al='upsInputTransferTrimLow'
_Ak='upsInputTransferBoostHigh'
_Aj='upsInputTransferBoostLow'
_Ai='upsInputTransferHighMax'
_Ah='upsInputTransferHighMin'
_Ag='upsInputTransferLowMax'
_Af='upsInputTransferLowMin'
_Ae='upsInputTransferHigh'
_Ad='upsInputTransferLow'
_Ac='upsInputTransferReason'
_Ab='upsInputVoltageFault'
_Aa='upsInputVoltageExtend'
_AZ='upsInputVoltageNominal'
_AY='upsInputVoltageMin'
_AX='upsInputVoltageMax'
_AW='upsInputVoltageValue'
_AV='upsBatteryEnergySave'
_AU='upsBatteryProtection'
_AT='upsBatteryType'
_AS='upsBatteryPacksBad'
_AR='upsBatteryPacks'
_AQ='upsBatteryMfrDate'
_AP='upsBatteryDate'
_AO='upsBatteryAlarmThreshold'
_AN='upsBatteryRuntimeRestart'
_AM='upsBatteryRuntimeLow'
_AL='upsBatteryRuntimeValue'
_AK='upsBatteryTemperature'
_AJ='upsBatteryCurrent'
_AI='upsBatteryCapacity'
_AH='upsBatteryVoltageHigh'
_AG='upsBatteryVoltageLow'
_AF='upsBatteryVoltageNominal'
_AE='upsBatteryVoltageValue'
_AD='upsBatteryChargeWarning'
_AC='upsBatteryChargeRestart'
_AB='upsBatteryChargeLow'
_AA='upsBatteryChargeValue'
_A9='upsInfoStartReboot'
_A8='upsInfoStartBattery'
_A7='upsInfoStartAuto'
_A6='upsInfoWatchdogStatus'
_A5='upsInfoType'
_A4='upsInfoBeeperStatus'
_A3='upsInfoRealPowerNominal'
_A2='upsInfoRealPowerValue'
_A1='upsInfoPowerNominal'
_A0='upsInfoPowerValue'
_z='upsInfoEffciency'
_y='upsInfoContacts'
_x='upsInfoDisplayLanguage'
_w='upsInfoTestResult'
_v='upsInfoTestInterval'
_u='upsInfoTimerShutdown'
_t='upsInfoTimerReboot'
_s='upsInfoTimerStart'
_r='upsInfoDelayShutdown'
_q='upsInfoDelayReboot'
_p='upsInfoDelayStart'
_o='upsInfoID'
_n='upsInfoLoadHigh'
_m='upsInfoLoadValue'
_l='upsInfoTemperature'
_k='upsInfoFirmwareAux'
_j='upsInfoFirmwareName'
_i='upsInfoProductID'
_h='upsInfoVendorID'
_g='upsInfoSerial'
_f='upsInfoMfrDate'
_e='upsInfoMfrName'
_d='upsInfoModel'
_c='upsInfoDate'
_b='upsInfoTime'
_a='upsInfoAlarm'
_Z='upsInfoStatus'
_Y='upsDeviceMACAddr'
_X='upsDevicePart'
_W='upsDeviceLocation'
_V='upsDeviceContact'
_U='upsDeviceDescription'
_T='upsDeviceType'
_S='upsDeviceSerial'
_R='upsDeviceManufacturer'
_Q='upsDeviceModel'
_P='enabled/disabled'
_O='Volt-Amps'
_N='percentage'
_M='Seconds'
_L='Amp'
_K='Volt DC'
_J='Percent'
_I='Hz'
_H='degrees Centigrade'
_G='percent'
_F='seconds'
_E='Volts'
_D='DisplayString'
_C='read-only'
_B='SYNOLOGY-UPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Float,=mibBuilder.importSymbols('NET-SNMP-TC','Float')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
synoUPS=ModuleIdentity((1,3,6,1,4,1,6574,4))
if mibBuilder.loadTexts:synoUPS.setRevisions(('2013-09-11 00:00',))
class NonNegativeInteger(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_UpsDevice_ObjectIdentity=ObjectIdentity
upsDevice=_UpsDevice_ObjectIdentity((1,3,6,1,4,1,6574,4,1))
class _UpsDeviceModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsDeviceModel_Type.__name__=_D
_UpsDeviceModel_Object=MibScalar
upsDeviceModel=_UpsDeviceModel_Object((1,3,6,1,4,1,6574,4,1,1),_UpsDeviceModel_Type())
upsDeviceModel.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDeviceModel.setStatus(_A)
class _UpsDeviceManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsDeviceManufacturer_Type.__name__=_D
_UpsDeviceManufacturer_Object=MibScalar
upsDeviceManufacturer=_UpsDeviceManufacturer_Object((1,3,6,1,4,1,6574,4,1,2),_UpsDeviceManufacturer_Type())
upsDeviceManufacturer.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDeviceManufacturer.setStatus(_A)
class _UpsDeviceSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsDeviceSerial_Type.__name__=_D
_UpsDeviceSerial_Object=MibScalar
upsDeviceSerial=_UpsDeviceSerial_Object((1,3,6,1,4,1,6574,4,1,3),_UpsDeviceSerial_Type())
upsDeviceSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDeviceSerial.setStatus(_A)
class _UpsDeviceType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsDeviceType_Type.__name__=_D
_UpsDeviceType_Object=MibScalar
upsDeviceType=_UpsDeviceType_Object((1,3,6,1,4,1,6574,4,1,4),_UpsDeviceType_Type())
upsDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDeviceType.setStatus(_A)
class _UpsDeviceDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsDeviceDescription_Type.__name__=_D
_UpsDeviceDescription_Object=MibScalar
upsDeviceDescription=_UpsDeviceDescription_Object((1,3,6,1,4,1,6574,4,1,5),_UpsDeviceDescription_Type())
upsDeviceDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDeviceDescription.setStatus(_A)
class _UpsDeviceContact_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsDeviceContact_Type.__name__=_D
_UpsDeviceContact_Object=MibScalar
upsDeviceContact=_UpsDeviceContact_Object((1,3,6,1,4,1,6574,4,1,6),_UpsDeviceContact_Type())
upsDeviceContact.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDeviceContact.setStatus(_A)
class _UpsDeviceLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsDeviceLocation_Type.__name__=_D
_UpsDeviceLocation_Object=MibScalar
upsDeviceLocation=_UpsDeviceLocation_Object((1,3,6,1,4,1,6574,4,1,7),_UpsDeviceLocation_Type())
upsDeviceLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDeviceLocation.setStatus(_A)
class _UpsDevicePart_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsDevicePart_Type.__name__=_D
_UpsDevicePart_Object=MibScalar
upsDevicePart=_UpsDevicePart_Object((1,3,6,1,4,1,6574,4,1,8),_UpsDevicePart_Type())
upsDevicePart.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDevicePart.setStatus(_A)
class _UpsDeviceMACAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsDeviceMACAddr_Type.__name__=_D
_UpsDeviceMACAddr_Object=MibScalar
upsDeviceMACAddr=_UpsDeviceMACAddr_Object((1,3,6,1,4,1,6574,4,1,9),_UpsDeviceMACAddr_Type())
upsDeviceMACAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDeviceMACAddr.setStatus(_A)
_UpsInfo_ObjectIdentity=ObjectIdentity
upsInfo=_UpsInfo_ObjectIdentity((1,3,6,1,4,1,6574,4,2))
class _UpsInfoStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoStatus_Type.__name__=_D
_UpsInfoStatus_Object=MibScalar
upsInfoStatus=_UpsInfoStatus_Object((1,3,6,1,4,1,6574,4,2,1),_UpsInfoStatus_Type())
upsInfoStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoStatus.setStatus(_A)
class _UpsInfoAlarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoAlarm_Type.__name__=_D
_UpsInfoAlarm_Object=MibScalar
upsInfoAlarm=_UpsInfoAlarm_Object((1,3,6,1,4,1,6574,4,2,2),_UpsInfoAlarm_Type())
upsInfoAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoAlarm.setStatus(_A)
class _UpsInfoTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoTime_Type.__name__=_D
_UpsInfoTime_Object=MibScalar
upsInfoTime=_UpsInfoTime_Object((1,3,6,1,4,1,6574,4,2,3),_UpsInfoTime_Type())
upsInfoTime.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoTime.setStatus(_A)
class _UpsInfoDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoDate_Type.__name__=_D
_UpsInfoDate_Object=MibScalar
upsInfoDate=_UpsInfoDate_Object((1,3,6,1,4,1,6574,4,2,4),_UpsInfoDate_Type())
upsInfoDate.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoDate.setStatus(_A)
class _UpsInfoModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoModel_Type.__name__=_D
_UpsInfoModel_Object=MibScalar
upsInfoModel=_UpsInfoModel_Object((1,3,6,1,4,1,6574,4,2,5),_UpsInfoModel_Type())
upsInfoModel.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoModel.setStatus(_A)
_UpsInfoMfr_ObjectIdentity=ObjectIdentity
upsInfoMfr=_UpsInfoMfr_ObjectIdentity((1,3,6,1,4,1,6574,4,2,6))
class _UpsInfoMfrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoMfrName_Type.__name__=_D
_UpsInfoMfrName_Object=MibScalar
upsInfoMfrName=_UpsInfoMfrName_Object((1,3,6,1,4,1,6574,4,2,6,1),_UpsInfoMfrName_Type())
upsInfoMfrName.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoMfrName.setStatus(_A)
class _UpsInfoMfrDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoMfrDate_Type.__name__=_D
_UpsInfoMfrDate_Object=MibScalar
upsInfoMfrDate=_UpsInfoMfrDate_Object((1,3,6,1,4,1,6574,4,2,6,2),_UpsInfoMfrDate_Type())
upsInfoMfrDate.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoMfrDate.setStatus(_A)
class _UpsInfoSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoSerial_Type.__name__=_D
_UpsInfoSerial_Object=MibScalar
upsInfoSerial=_UpsInfoSerial_Object((1,3,6,1,4,1,6574,4,2,7),_UpsInfoSerial_Type())
upsInfoSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoSerial.setStatus(_A)
class _UpsInfoVendorID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoVendorID_Type.__name__=_D
_UpsInfoVendorID_Object=MibScalar
upsInfoVendorID=_UpsInfoVendorID_Object((1,3,6,1,4,1,6574,4,2,8),_UpsInfoVendorID_Type())
upsInfoVendorID.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoVendorID.setStatus(_A)
class _UpsInfoProductID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoProductID_Type.__name__=_D
_UpsInfoProductID_Object=MibScalar
upsInfoProductID=_UpsInfoProductID_Object((1,3,6,1,4,1,6574,4,2,9),_UpsInfoProductID_Type())
upsInfoProductID.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoProductID.setStatus(_A)
_UpsInfoFirmware_ObjectIdentity=ObjectIdentity
upsInfoFirmware=_UpsInfoFirmware_ObjectIdentity((1,3,6,1,4,1,6574,4,2,10))
class _UpsInfoFirmwareName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoFirmwareName_Type.__name__=_D
_UpsInfoFirmwareName_Object=MibScalar
upsInfoFirmwareName=_UpsInfoFirmwareName_Object((1,3,6,1,4,1,6574,4,2,10,1),_UpsInfoFirmwareName_Type())
upsInfoFirmwareName.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoFirmwareName.setStatus(_A)
class _UpsInfoFirmwareAux_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoFirmwareAux_Type.__name__=_D
_UpsInfoFirmwareAux_Object=MibScalar
upsInfoFirmwareAux=_UpsInfoFirmwareAux_Object((1,3,6,1,4,1,6574,4,2,10,2),_UpsInfoFirmwareAux_Type())
upsInfoFirmwareAux.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoFirmwareAux.setStatus(_A)
_UpsInfoTemperature_Type=Float
_UpsInfoTemperature_Object=MibScalar
upsInfoTemperature=_UpsInfoTemperature_Object((1,3,6,1,4,1,6574,4,2,11),_UpsInfoTemperature_Type())
upsInfoTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoTemperature.setStatus(_A)
if mibBuilder.loadTexts:upsInfoTemperature.setUnits('degree C')
_UpsInfoLoad_ObjectIdentity=ObjectIdentity
upsInfoLoad=_UpsInfoLoad_ObjectIdentity((1,3,6,1,4,1,6574,4,2,12))
_UpsInfoLoadValue_Type=Float
_UpsInfoLoadValue_Object=MibScalar
upsInfoLoadValue=_UpsInfoLoadValue_Object((1,3,6,1,4,1,6574,4,2,12,1),_UpsInfoLoadValue_Type())
upsInfoLoadValue.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoLoadValue.setStatus(_A)
if mibBuilder.loadTexts:upsInfoLoadValue.setUnits(_N)
_UpsInfoLoadHigh_Type=Float
_UpsInfoLoadHigh_Object=MibScalar
upsInfoLoadHigh=_UpsInfoLoadHigh_Object((1,3,6,1,4,1,6574,4,2,12,2),_UpsInfoLoadHigh_Type())
upsInfoLoadHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoLoadHigh.setStatus(_A)
if mibBuilder.loadTexts:upsInfoLoadHigh.setUnits(_N)
class _UpsInfoID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoID_Type.__name__=_D
_UpsInfoID_Object=MibScalar
upsInfoID=_UpsInfoID_Object((1,3,6,1,4,1,6574,4,2,13),_UpsInfoID_Type())
upsInfoID.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoID.setStatus(_A)
_UpsInfoDelay_ObjectIdentity=ObjectIdentity
upsInfoDelay=_UpsInfoDelay_ObjectIdentity((1,3,6,1,4,1,6574,4,2,14))
_UpsInfoDelayStart_Type=NonNegativeInteger
_UpsInfoDelayStart_Object=MibScalar
upsInfoDelayStart=_UpsInfoDelayStart_Object((1,3,6,1,4,1,6574,4,2,14,1),_UpsInfoDelayStart_Type())
upsInfoDelayStart.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoDelayStart.setStatus(_A)
if mibBuilder.loadTexts:upsInfoDelayStart.setUnits(_F)
_UpsInfoDelayReboot_Type=NonNegativeInteger
_UpsInfoDelayReboot_Object=MibScalar
upsInfoDelayReboot=_UpsInfoDelayReboot_Object((1,3,6,1,4,1,6574,4,2,14,2),_UpsInfoDelayReboot_Type())
upsInfoDelayReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoDelayReboot.setStatus(_A)
if mibBuilder.loadTexts:upsInfoDelayReboot.setUnits(_F)
_UpsInfoDelayShutdown_Type=NonNegativeInteger
_UpsInfoDelayShutdown_Object=MibScalar
upsInfoDelayShutdown=_UpsInfoDelayShutdown_Object((1,3,6,1,4,1,6574,4,2,14,3),_UpsInfoDelayShutdown_Type())
upsInfoDelayShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoDelayShutdown.setStatus(_A)
if mibBuilder.loadTexts:upsInfoDelayShutdown.setUnits(_F)
_UpsInfoTimer_ObjectIdentity=ObjectIdentity
upsInfoTimer=_UpsInfoTimer_ObjectIdentity((1,3,6,1,4,1,6574,4,2,15))
_UpsInfoTimerStart_Type=NonNegativeInteger
_UpsInfoTimerStart_Object=MibScalar
upsInfoTimerStart=_UpsInfoTimerStart_Object((1,3,6,1,4,1,6574,4,2,15,1),_UpsInfoTimerStart_Type())
upsInfoTimerStart.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoTimerStart.setStatus(_A)
if mibBuilder.loadTexts:upsInfoTimerStart.setUnits(_F)
_UpsInfoTimerReboot_Type=NonNegativeInteger
_UpsInfoTimerReboot_Object=MibScalar
upsInfoTimerReboot=_UpsInfoTimerReboot_Object((1,3,6,1,4,1,6574,4,2,15,2),_UpsInfoTimerReboot_Type())
upsInfoTimerReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoTimerReboot.setStatus(_A)
if mibBuilder.loadTexts:upsInfoTimerReboot.setUnits(_F)
_UpsInfoTimerShutdown_Type=NonNegativeInteger
_UpsInfoTimerShutdown_Object=MibScalar
upsInfoTimerShutdown=_UpsInfoTimerShutdown_Object((1,3,6,1,4,1,6574,4,2,15,3),_UpsInfoTimerShutdown_Type())
upsInfoTimerShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoTimerShutdown.setStatus(_A)
if mibBuilder.loadTexts:upsInfoTimerShutdown.setUnits(_F)
_UpsInfoTest_ObjectIdentity=ObjectIdentity
upsInfoTest=_UpsInfoTest_ObjectIdentity((1,3,6,1,4,1,6574,4,2,16))
_UpsInfoTestInterval_Type=NonNegativeInteger
_UpsInfoTestInterval_Object=MibScalar
upsInfoTestInterval=_UpsInfoTestInterval_Object((1,3,6,1,4,1,6574,4,2,16,1),_UpsInfoTestInterval_Type())
upsInfoTestInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoTestInterval.setStatus(_A)
if mibBuilder.loadTexts:upsInfoTestInterval.setUnits(_F)
class _UpsInfoTestResult_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoTestResult_Type.__name__=_D
_UpsInfoTestResult_Object=MibScalar
upsInfoTestResult=_UpsInfoTestResult_Object((1,3,6,1,4,1,6574,4,2,16,2),_UpsInfoTestResult_Type())
upsInfoTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoTestResult.setStatus(_A)
class _UpsInfoDisplayLanguage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoDisplayLanguage_Type.__name__=_D
_UpsInfoDisplayLanguage_Object=MibScalar
upsInfoDisplayLanguage=_UpsInfoDisplayLanguage_Object((1,3,6,1,4,1,6574,4,2,17),_UpsInfoDisplayLanguage_Type())
upsInfoDisplayLanguage.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoDisplayLanguage.setStatus(_A)
class _UpsInfoContacts_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoContacts_Type.__name__=_D
_UpsInfoContacts_Object=MibScalar
upsInfoContacts=_UpsInfoContacts_Object((1,3,6,1,4,1,6574,4,2,18),_UpsInfoContacts_Type())
upsInfoContacts.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoContacts.setStatus(_A)
_UpsInfoEffciency_Type=NonNegativeInteger
_UpsInfoEffciency_Object=MibScalar
upsInfoEffciency=_UpsInfoEffciency_Object((1,3,6,1,4,1,6574,4,2,19),_UpsInfoEffciency_Type())
upsInfoEffciency.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoEffciency.setStatus(_A)
if mibBuilder.loadTexts:upsInfoEffciency.setUnits(_G)
_UpsInfoPower_ObjectIdentity=ObjectIdentity
upsInfoPower=_UpsInfoPower_ObjectIdentity((1,3,6,1,4,1,6574,4,2,20))
_UpsInfoPowerValue_Type=Float
_UpsInfoPowerValue_Object=MibScalar
upsInfoPowerValue=_UpsInfoPowerValue_Object((1,3,6,1,4,1,6574,4,2,20,1),_UpsInfoPowerValue_Type())
upsInfoPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoPowerValue.setStatus(_A)
if mibBuilder.loadTexts:upsInfoPowerValue.setUnits(_O)
_UpsInfoPowerNominal_Type=Float
_UpsInfoPowerNominal_Object=MibScalar
upsInfoPowerNominal=_UpsInfoPowerNominal_Object((1,3,6,1,4,1,6574,4,2,20,2),_UpsInfoPowerNominal_Type())
upsInfoPowerNominal.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoPowerNominal.setStatus(_A)
if mibBuilder.loadTexts:upsInfoPowerNominal.setUnits(_O)
_UpsInfoRealPower_ObjectIdentity=ObjectIdentity
upsInfoRealPower=_UpsInfoRealPower_ObjectIdentity((1,3,6,1,4,1,6574,4,2,21))
_UpsInfoRealPowerValue_Type=Float
_UpsInfoRealPowerValue_Object=MibScalar
upsInfoRealPowerValue=_UpsInfoRealPowerValue_Object((1,3,6,1,4,1,6574,4,2,21,1),_UpsInfoRealPowerValue_Type())
upsInfoRealPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoRealPowerValue.setStatus(_A)
if mibBuilder.loadTexts:upsInfoRealPowerValue.setUnits('Watts')
_UpsInfoRealPowerNominal_Type=Float
_UpsInfoRealPowerNominal_Object=MibScalar
upsInfoRealPowerNominal=_UpsInfoRealPowerNominal_Object((1,3,6,1,4,1,6574,4,2,21,2),_UpsInfoRealPowerNominal_Type())
upsInfoRealPowerNominal.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoRealPowerNominal.setStatus(_A)
if mibBuilder.loadTexts:upsInfoRealPowerNominal.setUnits('Watts')
class _UpsInfoBeeperStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoBeeperStatus_Type.__name__=_D
_UpsInfoBeeperStatus_Object=MibScalar
upsInfoBeeperStatus=_UpsInfoBeeperStatus_Object((1,3,6,1,4,1,6574,4,2,22),_UpsInfoBeeperStatus_Type())
upsInfoBeeperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoBeeperStatus.setStatus(_A)
class _UpsInfoType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoType_Type.__name__=_D
_UpsInfoType_Object=MibScalar
upsInfoType=_UpsInfoType_Object((1,3,6,1,4,1,6574,4,2,23),_UpsInfoType_Type())
upsInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoType.setStatus(_A)
class _UpsInfoWatchdogStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoWatchdogStatus_Type.__name__=_D
_UpsInfoWatchdogStatus_Object=MibScalar
upsInfoWatchdogStatus=_UpsInfoWatchdogStatus_Object((1,3,6,1,4,1,6574,4,2,24),_UpsInfoWatchdogStatus_Type())
upsInfoWatchdogStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoWatchdogStatus.setStatus(_A)
_UpsInfoStart_ObjectIdentity=ObjectIdentity
upsInfoStart=_UpsInfoStart_ObjectIdentity((1,3,6,1,4,1,6574,4,2,25))
class _UpsInfoStartAuto_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoStartAuto_Type.__name__=_D
_UpsInfoStartAuto_Object=MibScalar
upsInfoStartAuto=_UpsInfoStartAuto_Object((1,3,6,1,4,1,6574,4,2,25,1),_UpsInfoStartAuto_Type())
upsInfoStartAuto.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoStartAuto.setStatus(_A)
class _UpsInfoStartBattery_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoStartBattery_Type.__name__=_D
_UpsInfoStartBattery_Object=MibScalar
upsInfoStartBattery=_UpsInfoStartBattery_Object((1,3,6,1,4,1,6574,4,2,25,2),_UpsInfoStartBattery_Type())
upsInfoStartBattery.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoStartBattery.setStatus(_A)
class _UpsInfoStartReboot_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UpsInfoStartReboot_Type.__name__=_D
_UpsInfoStartReboot_Object=MibScalar
upsInfoStartReboot=_UpsInfoStartReboot_Object((1,3,6,1,4,1,6574,4,2,25,3),_UpsInfoStartReboot_Type())
upsInfoStartReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInfoStartReboot.setStatus(_A)
_UpsBattery_ObjectIdentity=ObjectIdentity
upsBattery=_UpsBattery_ObjectIdentity((1,3,6,1,4,1,6574,4,3))
_UpsBatteryCharge_ObjectIdentity=ObjectIdentity
upsBatteryCharge=_UpsBatteryCharge_ObjectIdentity((1,3,6,1,4,1,6574,4,3,1))
_UpsBatteryChargeValue_Type=Float
_UpsBatteryChargeValue_Object=MibScalar
upsBatteryChargeValue=_UpsBatteryChargeValue_Object((1,3,6,1,4,1,6574,4,3,1,1),_UpsBatteryChargeValue_Type())
upsBatteryChargeValue.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryChargeValue.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryChargeValue.setUnits(_J)
_UpsBatteryChargeLow_Type=Float
_UpsBatteryChargeLow_Object=MibScalar
upsBatteryChargeLow=_UpsBatteryChargeLow_Object((1,3,6,1,4,1,6574,4,3,1,2),_UpsBatteryChargeLow_Type())
upsBatteryChargeLow.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryChargeLow.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryChargeLow.setUnits(_J)
_UpsBatteryChargeRestart_Type=Float
_UpsBatteryChargeRestart_Object=MibScalar
upsBatteryChargeRestart=_UpsBatteryChargeRestart_Object((1,3,6,1,4,1,6574,4,3,1,3),_UpsBatteryChargeRestart_Type())
upsBatteryChargeRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryChargeRestart.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryChargeRestart.setUnits(_J)
_UpsBatteryChargeWarning_Type=Float
_UpsBatteryChargeWarning_Object=MibScalar
upsBatteryChargeWarning=_UpsBatteryChargeWarning_Object((1,3,6,1,4,1,6574,4,3,1,4),_UpsBatteryChargeWarning_Type())
upsBatteryChargeWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryChargeWarning.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryChargeWarning.setUnits(_J)
_UpsBatteryVoltage_ObjectIdentity=ObjectIdentity
upsBatteryVoltage=_UpsBatteryVoltage_ObjectIdentity((1,3,6,1,4,1,6574,4,3,2))
_UpsBatteryVoltageValue_Type=Float
_UpsBatteryVoltageValue_Object=MibScalar
upsBatteryVoltageValue=_UpsBatteryVoltageValue_Object((1,3,6,1,4,1,6574,4,3,2,1),_UpsBatteryVoltageValue_Type())
upsBatteryVoltageValue.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryVoltageValue.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryVoltageValue.setUnits(_K)
_UpsBatteryVoltageNominal_Type=Float
_UpsBatteryVoltageNominal_Object=MibScalar
upsBatteryVoltageNominal=_UpsBatteryVoltageNominal_Object((1,3,6,1,4,1,6574,4,3,2,2),_UpsBatteryVoltageNominal_Type())
upsBatteryVoltageNominal.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryVoltageNominal.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryVoltageNominal.setUnits(_K)
_UpsBatteryVoltageLow_Type=Float
_UpsBatteryVoltageLow_Object=MibScalar
upsBatteryVoltageLow=_UpsBatteryVoltageLow_Object((1,3,6,1,4,1,6574,4,3,2,3),_UpsBatteryVoltageLow_Type())
upsBatteryVoltageLow.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryVoltageLow.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryVoltageLow.setUnits(_K)
_UpsBatteryVoltageHigh_Type=Float
_UpsBatteryVoltageHigh_Object=MibScalar
upsBatteryVoltageHigh=_UpsBatteryVoltageHigh_Object((1,3,6,1,4,1,6574,4,3,2,4),_UpsBatteryVoltageHigh_Type())
upsBatteryVoltageHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryVoltageHigh.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryVoltageHigh.setUnits(_K)
_UpsBatteryCapacity_Type=Float
_UpsBatteryCapacity_Object=MibScalar
upsBatteryCapacity=_UpsBatteryCapacity_Object((1,3,6,1,4,1,6574,4,3,3),_UpsBatteryCapacity_Type())
upsBatteryCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryCapacity.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryCapacity.setUnits('A')
_UpsBatteryCurrent_Type=Float
_UpsBatteryCurrent_Object=MibScalar
upsBatteryCurrent=_UpsBatteryCurrent_Object((1,3,6,1,4,1,6574,4,3,4),_UpsBatteryCurrent_Type())
upsBatteryCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryCurrent.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryCurrent.setUnits('Amp DC')
_UpsBatteryTemperature_Type=Float
_UpsBatteryTemperature_Object=MibScalar
upsBatteryTemperature=_UpsBatteryTemperature_Object((1,3,6,1,4,1,6574,4,3,5),_UpsBatteryTemperature_Type())
upsBatteryTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryTemperature.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryTemperature.setUnits(_H)
_UpsBatteryRuntime_ObjectIdentity=ObjectIdentity
upsBatteryRuntime=_UpsBatteryRuntime_ObjectIdentity((1,3,6,1,4,1,6574,4,3,6))
_UpsBatteryRuntimeValue_Type=NonNegativeInteger
_UpsBatteryRuntimeValue_Object=MibScalar
upsBatteryRuntimeValue=_UpsBatteryRuntimeValue_Object((1,3,6,1,4,1,6574,4,3,6,1),_UpsBatteryRuntimeValue_Type())
upsBatteryRuntimeValue.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryRuntimeValue.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryRuntimeValue.setUnits(_M)
_UpsBatteryRuntimeLow_Type=NonNegativeInteger
_UpsBatteryRuntimeLow_Object=MibScalar
upsBatteryRuntimeLow=_UpsBatteryRuntimeLow_Object((1,3,6,1,4,1,6574,4,3,6,2),_UpsBatteryRuntimeLow_Type())
upsBatteryRuntimeLow.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryRuntimeLow.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryRuntimeLow.setUnits(_M)
_UpsBatteryRuntimeRestart_Type=NonNegativeInteger
_UpsBatteryRuntimeRestart_Object=MibScalar
upsBatteryRuntimeRestart=_UpsBatteryRuntimeRestart_Object((1,3,6,1,4,1,6574,4,3,6,3),_UpsBatteryRuntimeRestart_Type())
upsBatteryRuntimeRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryRuntimeRestart.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryRuntimeRestart.setUnits(_M)
class _UpsBatteryAlarmThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsBatteryAlarmThreshold_Type.__name__=_D
_UpsBatteryAlarmThreshold_Object=MibScalar
upsBatteryAlarmThreshold=_UpsBatteryAlarmThreshold_Object((1,3,6,1,4,1,6574,4,3,7),_UpsBatteryAlarmThreshold_Type())
upsBatteryAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryAlarmThreshold.setStatus(_A)
class _UpsBatteryDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsBatteryDate_Type.__name__=_D
_UpsBatteryDate_Object=MibScalar
upsBatteryDate=_UpsBatteryDate_Object((1,3,6,1,4,1,6574,4,3,8),_UpsBatteryDate_Type())
upsBatteryDate.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryDate.setStatus(_A)
class _UpsBatteryMfrDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsBatteryMfrDate_Type.__name__=_D
_UpsBatteryMfrDate_Object=MibScalar
upsBatteryMfrDate=_UpsBatteryMfrDate_Object((1,3,6,1,4,1,6574,4,3,9),_UpsBatteryMfrDate_Type())
upsBatteryMfrDate.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryMfrDate.setStatus(_A)
_UpsBatteryPacks_Type=NonNegativeInteger
_UpsBatteryPacks_Object=MibScalar
upsBatteryPacks=_UpsBatteryPacks_Object((1,3,6,1,4,1,6574,4,3,10),_UpsBatteryPacks_Type())
upsBatteryPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryPacks.setStatus(_A)
_UpsBatteryPacksBad_Type=NonNegativeInteger
_UpsBatteryPacksBad_Object=MibScalar
upsBatteryPacksBad=_UpsBatteryPacksBad_Object((1,3,6,1,4,1,6574,4,3,11),_UpsBatteryPacksBad_Type())
upsBatteryPacksBad.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryPacksBad.setStatus(_A)
class _UpsBatteryType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsBatteryType_Type.__name__=_D
_UpsBatteryType_Object=MibScalar
upsBatteryType=_UpsBatteryType_Object((1,3,6,1,4,1,6574,4,3,12),_UpsBatteryType_Type())
upsBatteryType.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryType.setStatus(_A)
class _UpsBatteryProtection_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsBatteryProtection_Type.__name__=_D
_UpsBatteryProtection_Object=MibScalar
upsBatteryProtection=_UpsBatteryProtection_Object((1,3,6,1,4,1,6574,4,3,13),_UpsBatteryProtection_Type())
upsBatteryProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryProtection.setStatus(_A)
class _UpsBatteryEnergySave_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsBatteryEnergySave_Type.__name__=_D
_UpsBatteryEnergySave_Object=MibScalar
upsBatteryEnergySave=_UpsBatteryEnergySave_Object((1,3,6,1,4,1,6574,4,3,14),_UpsBatteryEnergySave_Type())
upsBatteryEnergySave.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryEnergySave.setStatus(_A)
_UpsInput_ObjectIdentity=ObjectIdentity
upsInput=_UpsInput_ObjectIdentity((1,3,6,1,4,1,6574,4,4))
_UpsInputVoltage_ObjectIdentity=ObjectIdentity
upsInputVoltage=_UpsInputVoltage_ObjectIdentity((1,3,6,1,4,1,6574,4,4,1))
_UpsInputVoltageValue_Type=Float
_UpsInputVoltageValue_Object=MibScalar
upsInputVoltageValue=_UpsInputVoltageValue_Object((1,3,6,1,4,1,6574,4,4,1,1),_UpsInputVoltageValue_Type())
upsInputVoltageValue.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputVoltageValue.setStatus(_A)
if mibBuilder.loadTexts:upsInputVoltageValue.setUnits(_E)
_UpsInputVoltageMax_Type=Float
_UpsInputVoltageMax_Object=MibScalar
upsInputVoltageMax=_UpsInputVoltageMax_Object((1,3,6,1,4,1,6574,4,4,1,2),_UpsInputVoltageMax_Type())
upsInputVoltageMax.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputVoltageMax.setStatus(_A)
if mibBuilder.loadTexts:upsInputVoltageMax.setUnits(_E)
_UpsInputVoltageMin_Type=Float
_UpsInputVoltageMin_Object=MibScalar
upsInputVoltageMin=_UpsInputVoltageMin_Object((1,3,6,1,4,1,6574,4,4,1,3),_UpsInputVoltageMin_Type())
upsInputVoltageMin.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputVoltageMin.setStatus(_A)
if mibBuilder.loadTexts:upsInputVoltageMin.setUnits(_E)
_UpsInputVoltageNominal_Type=Float
_UpsInputVoltageNominal_Object=MibScalar
upsInputVoltageNominal=_UpsInputVoltageNominal_Object((1,3,6,1,4,1,6574,4,4,1,4),_UpsInputVoltageNominal_Type())
upsInputVoltageNominal.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputVoltageNominal.setStatus(_A)
if mibBuilder.loadTexts:upsInputVoltageNominal.setUnits(_E)
class _UpsInputVoltageExtend_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsInputVoltageExtend_Type.__name__=_D
_UpsInputVoltageExtend_Object=MibScalar
upsInputVoltageExtend=_UpsInputVoltageExtend_Object((1,3,6,1,4,1,6574,4,4,1,5),_UpsInputVoltageExtend_Type())
upsInputVoltageExtend.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputVoltageExtend.setStatus(_A)
_UpsInputVoltageFault_Type=Float
_UpsInputVoltageFault_Object=MibScalar
upsInputVoltageFault=_UpsInputVoltageFault_Object((1,3,6,1,4,1,6574,4,4,1,6),_UpsInputVoltageFault_Type())
upsInputVoltageFault.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputVoltageFault.setStatus(_A)
if mibBuilder.loadTexts:upsInputVoltageFault.setUnits(_E)
_UpsInputTransfer_ObjectIdentity=ObjectIdentity
upsInputTransfer=_UpsInputTransfer_ObjectIdentity((1,3,6,1,4,1,6574,4,4,2))
class _UpsInputTransferReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsInputTransferReason_Type.__name__=_D
_UpsInputTransferReason_Object=MibScalar
upsInputTransferReason=_UpsInputTransferReason_Object((1,3,6,1,4,1,6574,4,4,2,1),_UpsInputTransferReason_Type())
upsInputTransferReason.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputTransferReason.setStatus(_A)
_UpsInputTransferLow_Type=Float
_UpsInputTransferLow_Object=MibScalar
upsInputTransferLow=_UpsInputTransferLow_Object((1,3,6,1,4,1,6574,4,4,2,2),_UpsInputTransferLow_Type())
upsInputTransferLow.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputTransferLow.setStatus(_A)
if mibBuilder.loadTexts:upsInputTransferLow.setUnits(_E)
_UpsInputTransferHigh_Type=Float
_UpsInputTransferHigh_Object=MibScalar
upsInputTransferHigh=_UpsInputTransferHigh_Object((1,3,6,1,4,1,6574,4,4,2,3),_UpsInputTransferHigh_Type())
upsInputTransferHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputTransferHigh.setStatus(_A)
if mibBuilder.loadTexts:upsInputTransferHigh.setUnits(_E)
_UpsInputTransferLowMin_Type=Float
_UpsInputTransferLowMin_Object=MibScalar
upsInputTransferLowMin=_UpsInputTransferLowMin_Object((1,3,6,1,4,1,6574,4,4,2,4),_UpsInputTransferLowMin_Type())
upsInputTransferLowMin.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputTransferLowMin.setStatus(_A)
if mibBuilder.loadTexts:upsInputTransferLowMin.setUnits(_E)
_UpsInputTransferLowMax_Type=Float
_UpsInputTransferLowMax_Object=MibScalar
upsInputTransferLowMax=_UpsInputTransferLowMax_Object((1,3,6,1,4,1,6574,4,4,2,5),_UpsInputTransferLowMax_Type())
upsInputTransferLowMax.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputTransferLowMax.setStatus(_A)
if mibBuilder.loadTexts:upsInputTransferLowMax.setUnits(_E)
_UpsInputTransferHighMin_Type=Float
_UpsInputTransferHighMin_Object=MibScalar
upsInputTransferHighMin=_UpsInputTransferHighMin_Object((1,3,6,1,4,1,6574,4,4,2,6),_UpsInputTransferHighMin_Type())
upsInputTransferHighMin.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputTransferHighMin.setStatus(_A)
if mibBuilder.loadTexts:upsInputTransferHighMin.setUnits(_E)
_UpsInputTransferHighMax_Type=Float
_UpsInputTransferHighMax_Object=MibScalar
upsInputTransferHighMax=_UpsInputTransferHighMax_Object((1,3,6,1,4,1,6574,4,4,2,7),_UpsInputTransferHighMax_Type())
upsInputTransferHighMax.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputTransferHighMax.setStatus(_A)
if mibBuilder.loadTexts:upsInputTransferHighMax.setUnits(_E)
_UpsInputTransferBoostLow_Type=Float
_UpsInputTransferBoostLow_Object=MibScalar
upsInputTransferBoostLow=_UpsInputTransferBoostLow_Object((1,3,6,1,4,1,6574,4,4,2,8),_UpsInputTransferBoostLow_Type())
upsInputTransferBoostLow.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputTransferBoostLow.setStatus(_A)
if mibBuilder.loadTexts:upsInputTransferBoostLow.setUnits(_E)
_UpsInputTransferBoostHigh_Type=Float
_UpsInputTransferBoostHigh_Object=MibScalar
upsInputTransferBoostHigh=_UpsInputTransferBoostHigh_Object((1,3,6,1,4,1,6574,4,4,2,9),_UpsInputTransferBoostHigh_Type())
upsInputTransferBoostHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputTransferBoostHigh.setStatus(_A)
if mibBuilder.loadTexts:upsInputTransferBoostHigh.setUnits(_E)
_UpsInputTransferTrimLow_Type=Float
_UpsInputTransferTrimLow_Object=MibScalar
upsInputTransferTrimLow=_UpsInputTransferTrimLow_Object((1,3,6,1,4,1,6574,4,4,2,10),_UpsInputTransferTrimLow_Type())
upsInputTransferTrimLow.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputTransferTrimLow.setStatus(_A)
if mibBuilder.loadTexts:upsInputTransferTrimLow.setUnits(_E)
_UpsInputTransferTrimHigh_Type=Float
_UpsInputTransferTrimHigh_Object=MibScalar
upsInputTransferTrimHigh=_UpsInputTransferTrimHigh_Object((1,3,6,1,4,1,6574,4,4,2,11),_UpsInputTransferTrimHigh_Type())
upsInputTransferTrimHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputTransferTrimHigh.setStatus(_A)
if mibBuilder.loadTexts:upsInputTransferTrimHigh.setUnits(_E)
class _UpsInputSensitivity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsInputSensitivity_Type.__name__=_D
_UpsInputSensitivity_Object=MibScalar
upsInputSensitivity=_UpsInputSensitivity_Object((1,3,6,1,4,1,6574,4,4,3),_UpsInputSensitivity_Type())
upsInputSensitivity.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputSensitivity.setStatus(_A)
class _UpsInputQuality_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsInputQuality_Type.__name__=_D
_UpsInputQuality_Object=MibScalar
upsInputQuality=_UpsInputQuality_Object((1,3,6,1,4,1,6574,4,4,4),_UpsInputQuality_Type())
upsInputQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputQuality.setStatus(_A)
_UpsInputCurrent_ObjectIdentity=ObjectIdentity
upsInputCurrent=_UpsInputCurrent_ObjectIdentity((1,3,6,1,4,1,6574,4,4,5))
_UpsInputCurrentValue_Type=Float
_UpsInputCurrentValue_Object=MibScalar
upsInputCurrentValue=_UpsInputCurrentValue_Object((1,3,6,1,4,1,6574,4,4,5,1),_UpsInputCurrentValue_Type())
upsInputCurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputCurrentValue.setStatus(_A)
if mibBuilder.loadTexts:upsInputCurrentValue.setUnits(_L)
_UpsInputCurrentNominal_Type=Float
_UpsInputCurrentNominal_Object=MibScalar
upsInputCurrentNominal=_UpsInputCurrentNominal_Object((1,3,6,1,4,1,6574,4,4,5,2),_UpsInputCurrentNominal_Type())
upsInputCurrentNominal.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputCurrentNominal.setStatus(_A)
if mibBuilder.loadTexts:upsInputCurrentNominal.setUnits(_L)
_UpsInputFrequency_ObjectIdentity=ObjectIdentity
upsInputFrequency=_UpsInputFrequency_ObjectIdentity((1,3,6,1,4,1,6574,4,4,6))
_UpsInputFrequencyValue_Type=Float
_UpsInputFrequencyValue_Object=MibScalar
upsInputFrequencyValue=_UpsInputFrequencyValue_Object((1,3,6,1,4,1,6574,4,4,6,1),_UpsInputFrequencyValue_Type())
upsInputFrequencyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputFrequencyValue.setStatus(_A)
if mibBuilder.loadTexts:upsInputFrequencyValue.setUnits(_I)
_UpsInputFrequencyNominal_Type=Float
_UpsInputFrequencyNominal_Object=MibScalar
upsInputFrequencyNominal=_UpsInputFrequencyNominal_Object((1,3,6,1,4,1,6574,4,4,6,2),_UpsInputFrequencyNominal_Type())
upsInputFrequencyNominal.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputFrequencyNominal.setStatus(_A)
if mibBuilder.loadTexts:upsInputFrequencyNominal.setUnits(_I)
_UpsInputFrequencyLow_Type=Float
_UpsInputFrequencyLow_Object=MibScalar
upsInputFrequencyLow=_UpsInputFrequencyLow_Object((1,3,6,1,4,1,6574,4,4,6,3),_UpsInputFrequencyLow_Type())
upsInputFrequencyLow.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputFrequencyLow.setStatus(_A)
if mibBuilder.loadTexts:upsInputFrequencyLow.setUnits(_I)
_UpsInputFrequencyHigh_Type=Float
_UpsInputFrequencyHigh_Object=MibScalar
upsInputFrequencyHigh=_UpsInputFrequencyHigh_Object((1,3,6,1,4,1,6574,4,4,6,4),_UpsInputFrequencyHigh_Type())
upsInputFrequencyHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputFrequencyHigh.setStatus(_A)
if mibBuilder.loadTexts:upsInputFrequencyHigh.setUnits(_I)
class _UpsInputFrequencyExtend_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsInputFrequencyExtend_Type.__name__=_D
_UpsInputFrequencyExtend_Object=MibScalar
upsInputFrequencyExtend=_UpsInputFrequencyExtend_Object((1,3,6,1,4,1,6574,4,4,6,5),_UpsInputFrequencyExtend_Type())
upsInputFrequencyExtend.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInputFrequencyExtend.setStatus(_A)
_UpsOutput_ObjectIdentity=ObjectIdentity
upsOutput=_UpsOutput_ObjectIdentity((1,3,6,1,4,1,6574,4,5))
_UpsOutputVoltage_ObjectIdentity=ObjectIdentity
upsOutputVoltage=_UpsOutputVoltage_ObjectIdentity((1,3,6,1,4,1,6574,4,5,1))
_UpsOutputVoltageValue_Type=Float
_UpsOutputVoltageValue_Object=MibScalar
upsOutputVoltageValue=_UpsOutputVoltageValue_Object((1,3,6,1,4,1,6574,4,5,1,1),_UpsOutputVoltageValue_Type())
upsOutputVoltageValue.setMaxAccess(_C)
if mibBuilder.loadTexts:upsOutputVoltageValue.setStatus(_A)
if mibBuilder.loadTexts:upsOutputVoltageValue.setUnits(_E)
_UpsOutputVoltageNominal_Type=Float
_UpsOutputVoltageNominal_Object=MibScalar
upsOutputVoltageNominal=_UpsOutputVoltageNominal_Object((1,3,6,1,4,1,6574,4,5,1,2),_UpsOutputVoltageNominal_Type())
upsOutputVoltageNominal.setMaxAccess(_C)
if mibBuilder.loadTexts:upsOutputVoltageNominal.setStatus(_A)
if mibBuilder.loadTexts:upsOutputVoltageNominal.setUnits(_E)
_UpsOutputFrequency_ObjectIdentity=ObjectIdentity
upsOutputFrequency=_UpsOutputFrequency_ObjectIdentity((1,3,6,1,4,1,6574,4,5,2))
_UpsOutputFrequencyValue_Type=Float
_UpsOutputFrequencyValue_Object=MibScalar
upsOutputFrequencyValue=_UpsOutputFrequencyValue_Object((1,3,6,1,4,1,6574,4,5,2,1),_UpsOutputFrequencyValue_Type())
upsOutputFrequencyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:upsOutputFrequencyValue.setStatus(_A)
if mibBuilder.loadTexts:upsOutputFrequencyValue.setUnits(_I)
_UpsOutputFrequencyNominal_Type=Float
_UpsOutputFrequencyNominal_Object=MibScalar
upsOutputFrequencyNominal=_UpsOutputFrequencyNominal_Object((1,3,6,1,4,1,6574,4,5,2,2),_UpsOutputFrequencyNominal_Type())
upsOutputFrequencyNominal.setMaxAccess(_C)
if mibBuilder.loadTexts:upsOutputFrequencyNominal.setStatus(_A)
if mibBuilder.loadTexts:upsOutputFrequencyNominal.setUnits(_I)
_UpsOutputCurrent_ObjectIdentity=ObjectIdentity
upsOutputCurrent=_UpsOutputCurrent_ObjectIdentity((1,3,6,1,4,1,6574,4,5,3))
_UpsOutputCurrentValue_Type=Float
_UpsOutputCurrentValue_Object=MibScalar
upsOutputCurrentValue=_UpsOutputCurrentValue_Object((1,3,6,1,4,1,6574,4,5,3,1),_UpsOutputCurrentValue_Type())
upsOutputCurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:upsOutputCurrentValue.setStatus(_A)
if mibBuilder.loadTexts:upsOutputCurrentValue.setUnits(_L)
_UpsOutputCurrentNominal_Type=Float
_UpsOutputCurrentNominal_Object=MibScalar
upsOutputCurrentNominal=_UpsOutputCurrentNominal_Object((1,3,6,1,4,1,6574,4,5,3,2),_UpsOutputCurrentNominal_Type())
upsOutputCurrentNominal.setMaxAccess(_C)
if mibBuilder.loadTexts:upsOutputCurrentNominal.setStatus(_A)
if mibBuilder.loadTexts:upsOutputCurrentNominal.setUnits(_L)
_UpsAmbient_ObjectIdentity=ObjectIdentity
upsAmbient=_UpsAmbient_ObjectIdentity((1,3,6,1,4,1,6574,4,6))
_UpsAmbientTemperature_ObjectIdentity=ObjectIdentity
upsAmbientTemperature=_UpsAmbientTemperature_ObjectIdentity((1,3,6,1,4,1,6574,4,6,1))
_UpsAmbientTemperatureValue_Type=Float
_UpsAmbientTemperatureValue_Object=MibScalar
upsAmbientTemperatureValue=_UpsAmbientTemperatureValue_Object((1,3,6,1,4,1,6574,4,6,1,1),_UpsAmbientTemperatureValue_Type())
upsAmbientTemperatureValue.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAmbientTemperatureValue.setStatus(_A)
if mibBuilder.loadTexts:upsAmbientTemperatureValue.setUnits(_H)
class _UpsAmbientTemperatureAlarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsAmbientTemperatureAlarm_Type.__name__=_D
_UpsAmbientTemperatureAlarm_Object=MibScalar
upsAmbientTemperatureAlarm=_UpsAmbientTemperatureAlarm_Object((1,3,6,1,4,1,6574,4,6,1,2),_UpsAmbientTemperatureAlarm_Type())
upsAmbientTemperatureAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAmbientTemperatureAlarm.setStatus(_A)
if mibBuilder.loadTexts:upsAmbientTemperatureAlarm.setUnits(_P)
_UpsAmbientTemperatureHigh_Type=Float
_UpsAmbientTemperatureHigh_Object=MibScalar
upsAmbientTemperatureHigh=_UpsAmbientTemperatureHigh_Object((1,3,6,1,4,1,6574,4,6,1,3),_UpsAmbientTemperatureHigh_Type())
upsAmbientTemperatureHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAmbientTemperatureHigh.setStatus(_A)
if mibBuilder.loadTexts:upsAmbientTemperatureHigh.setUnits(_H)
_UpsAmbientTemperatureLow_Type=Float
_UpsAmbientTemperatureLow_Object=MibScalar
upsAmbientTemperatureLow=_UpsAmbientTemperatureLow_Object((1,3,6,1,4,1,6574,4,6,1,4),_UpsAmbientTemperatureLow_Type())
upsAmbientTemperatureLow.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAmbientTemperatureLow.setStatus(_A)
if mibBuilder.loadTexts:upsAmbientTemperatureLow.setUnits(_H)
_UpsAmbientTemperatureMax_Type=Float
_UpsAmbientTemperatureMax_Object=MibScalar
upsAmbientTemperatureMax=_UpsAmbientTemperatureMax_Object((1,3,6,1,4,1,6574,4,6,1,5),_UpsAmbientTemperatureMax_Type())
upsAmbientTemperatureMax.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAmbientTemperatureMax.setStatus(_A)
if mibBuilder.loadTexts:upsAmbientTemperatureMax.setUnits(_H)
_UpsAmbientTemperatureMin_Type=Float
_UpsAmbientTemperatureMin_Object=MibScalar
upsAmbientTemperatureMin=_UpsAmbientTemperatureMin_Object((1,3,6,1,4,1,6574,4,6,1,6),_UpsAmbientTemperatureMin_Type())
upsAmbientTemperatureMin.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAmbientTemperatureMin.setStatus(_A)
if mibBuilder.loadTexts:upsAmbientTemperatureMin.setUnits(_H)
_UpsAmbientHumidity_ObjectIdentity=ObjectIdentity
upsAmbientHumidity=_UpsAmbientHumidity_ObjectIdentity((1,3,6,1,4,1,6574,4,6,2))
_UpsAmbientHumidityValue_Type=Float
_UpsAmbientHumidityValue_Object=MibScalar
upsAmbientHumidityValue=_UpsAmbientHumidityValue_Object((1,3,6,1,4,1,6574,4,6,2,1),_UpsAmbientHumidityValue_Type())
upsAmbientHumidityValue.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAmbientHumidityValue.setStatus(_A)
if mibBuilder.loadTexts:upsAmbientHumidityValue.setUnits(_G)
class _UpsAmbientHumidityAlarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsAmbientHumidityAlarm_Type.__name__=_D
_UpsAmbientHumidityAlarm_Object=MibScalar
upsAmbientHumidityAlarm=_UpsAmbientHumidityAlarm_Object((1,3,6,1,4,1,6574,4,6,2,2),_UpsAmbientHumidityAlarm_Type())
upsAmbientHumidityAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAmbientHumidityAlarm.setStatus(_A)
if mibBuilder.loadTexts:upsAmbientHumidityAlarm.setUnits(_P)
_UpsAmbientHumidityHigh_Type=Float
_UpsAmbientHumidityHigh_Object=MibScalar
upsAmbientHumidityHigh=_UpsAmbientHumidityHigh_Object((1,3,6,1,4,1,6574,4,6,2,3),_UpsAmbientHumidityHigh_Type())
upsAmbientHumidityHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAmbientHumidityHigh.setStatus(_A)
if mibBuilder.loadTexts:upsAmbientHumidityHigh.setUnits(_G)
_UpsAmbientHumidityLow_Type=Float
_UpsAmbientHumidityLow_Object=MibScalar
upsAmbientHumidityLow=_UpsAmbientHumidityLow_Object((1,3,6,1,4,1,6574,4,6,2,4),_UpsAmbientHumidityLow_Type())
upsAmbientHumidityLow.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAmbientHumidityLow.setStatus(_A)
if mibBuilder.loadTexts:upsAmbientHumidityLow.setUnits(_G)
_UpsAmbientHumidityMax_Type=Float
_UpsAmbientHumidityMax_Object=MibScalar
upsAmbientHumidityMax=_UpsAmbientHumidityMax_Object((1,3,6,1,4,1,6574,4,6,2,5),_UpsAmbientHumidityMax_Type())
upsAmbientHumidityMax.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAmbientHumidityMax.setStatus(_A)
if mibBuilder.loadTexts:upsAmbientHumidityMax.setUnits(_G)
_UpsAmbientHumidityMin_Type=Float
_UpsAmbientHumidityMin_Object=MibScalar
upsAmbientHumidityMin=_UpsAmbientHumidityMin_Object((1,3,6,1,4,1,6574,4,6,2,6),_UpsAmbientHumidityMin_Type())
upsAmbientHumidityMin.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAmbientHumidityMin.setStatus(_A)
if mibBuilder.loadTexts:upsAmbientHumidityMin.setUnits(_G)
_UpsDriver_ObjectIdentity=ObjectIdentity
upsDriver=_UpsDriver_ObjectIdentity((1,3,6,1,4,1,6574,4,7))
class _UpsDriverName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsDriverName_Type.__name__=_D
_UpsDriverName_Object=MibScalar
upsDriverName=_UpsDriverName_Object((1,3,6,1,4,1,6574,4,7,1),_UpsDriverName_Type())
upsDriverName.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDriverName.setStatus(_A)
class _UpsDriverVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsDriverVersion_Type.__name__=_D
_UpsDriverVersion_Object=MibScalar
upsDriverVersion=_UpsDriverVersion_Object((1,3,6,1,4,1,6574,4,7,2),_UpsDriverVersion_Type())
upsDriverVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDriverVersion.setStatus(_A)
class _UpsDriverVersionData_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsDriverVersionData_Type.__name__=_D
_UpsDriverVersionData_Object=MibScalar
upsDriverVersionData=_UpsDriverVersionData_Object((1,3,6,1,4,1,6574,4,7,3),_UpsDriverVersionData_Type())
upsDriverVersionData.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDriverVersionData.setStatus(_A)
class _UpsDriverVersionInternal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsDriverVersionInternal_Type.__name__=_D
_UpsDriverVersionInternal_Object=MibScalar
upsDriverVersionInternal=_UpsDriverVersionInternal_Object((1,3,6,1,4,1,6574,4,7,4),_UpsDriverVersionInternal_Type())
upsDriverVersionInternal.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDriverVersionInternal.setStatus(_A)
_UpsDriverPollInterval_Type=Integer32
_UpsDriverPollInterval_Object=MibScalar
upsDriverPollInterval=_UpsDriverPollInterval_Object((1,3,6,1,4,1,6574,4,7,5),_UpsDriverPollInterval_Type())
upsDriverPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDriverPollInterval.setStatus(_A)
if mibBuilder.loadTexts:upsDriverPollInterval.setUnits('second')
class _UpsDriverPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsDriverPort_Type.__name__=_D
_UpsDriverPort_Object=MibScalar
upsDriverPort=_UpsDriverPort_Object((1,3,6,1,4,1,6574,4,7,6),_UpsDriverPort_Type())
upsDriverPort.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDriverPort.setStatus(_A)
_UpsDriverPollFrequency_Type=Integer32
_UpsDriverPollFrequency_Object=MibScalar
upsDriverPollFrequency=_UpsDriverPollFrequency_Object((1,3,6,1,4,1,6574,4,7,7),_UpsDriverPollFrequency_Type())
upsDriverPollFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDriverPollFrequency.setStatus(_A)
class _UpsDriverProductID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsDriverProductID_Type.__name__=_D
_UpsDriverProductID_Object=MibScalar
upsDriverProductID=_UpsDriverProductID_Object((1,3,6,1,4,1,6574,4,7,8),_UpsDriverProductID_Type())
upsDriverProductID.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDriverProductID.setStatus(_A)
class _UpsDriverSnmpVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsDriverSnmpVersion_Type.__name__=_D
_UpsDriverSnmpVersion_Object=MibScalar
upsDriverSnmpVersion=_UpsDriverSnmpVersion_Object((1,3,6,1,4,1,6574,4,7,9),_UpsDriverSnmpVersion_Type())
upsDriverSnmpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:upsDriverSnmpVersion.setStatus(_A)
_UpsServer_ObjectIdentity=ObjectIdentity
upsServer=_UpsServer_ObjectIdentity((1,3,6,1,4,1,6574,4,8))
class _UpsServerInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsServerInfo_Type.__name__=_D
_UpsServerInfo_Object=MibScalar
upsServerInfo=_UpsServerInfo_Object((1,3,6,1,4,1,6574,4,8,1),_UpsServerInfo_Type())
upsServerInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:upsServerInfo.setStatus(_A)
class _UpsServerVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UpsServerVersion_Type.__name__=_D
_UpsServerVersion_Object=MibScalar
upsServerVersion=_UpsServerVersion_Object((1,3,6,1,4,1,6574,4,8,2),_UpsServerVersion_Type())
upsServerVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:upsServerVersion.setStatus(_A)
_UpsConformance_ObjectIdentity=ObjectIdentity
upsConformance=_UpsConformance_ObjectIdentity((1,3,6,1,4,1,6574,4,9))
_UpsCompliances_ObjectIdentity=ObjectIdentity
upsCompliances=_UpsCompliances_ObjectIdentity((1,3,6,1,4,1,6574,4,9,1))
_UpsGroups_ObjectIdentity=ObjectIdentity
upsGroups=_UpsGroups_ObjectIdentity((1,3,6,1,4,1,6574,4,9,2))
upsGroup=ObjectGroup((1,3,6,1,4,1,6574,4,9,2,1))
upsGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB),(_B,_BC),(_B,_BD),(_B,_BE),(_B,_BF),(_B,_BG),(_B,_BH),(_B,_BI),(_B,_BJ),(_B,_BK),(_B,_BL),(_B,_BM),(_B,_BN)))
if mibBuilder.loadTexts:upsGroup.setStatus(_A)
upsCompliance=ModuleCompliance((1,3,6,1,4,1,6574,4,9,1,1))
upsCompliance.setObjects((_B,'upsGroup'))
if mibBuilder.loadTexts:upsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NonNegativeInteger':NonNegativeInteger,'synology':synology,'synoUPS':synoUPS,'upsDevice':upsDevice,_Q:upsDeviceModel,_R:upsDeviceManufacturer,_S:upsDeviceSerial,_T:upsDeviceType,_U:upsDeviceDescription,_V:upsDeviceContact,_W:upsDeviceLocation,_X:upsDevicePart,_Y:upsDeviceMACAddr,'upsInfo':upsInfo,_Z:upsInfoStatus,_a:upsInfoAlarm,_b:upsInfoTime,_c:upsInfoDate,_d:upsInfoModel,'upsInfoMfr':upsInfoMfr,_e:upsInfoMfrName,_f:upsInfoMfrDate,_g:upsInfoSerial,_h:upsInfoVendorID,_i:upsInfoProductID,'upsInfoFirmware':upsInfoFirmware,_j:upsInfoFirmwareName,_k:upsInfoFirmwareAux,_l:upsInfoTemperature,'upsInfoLoad':upsInfoLoad,_m:upsInfoLoadValue,_n:upsInfoLoadHigh,_o:upsInfoID,'upsInfoDelay':upsInfoDelay,_p:upsInfoDelayStart,_q:upsInfoDelayReboot,_r:upsInfoDelayShutdown,'upsInfoTimer':upsInfoTimer,_s:upsInfoTimerStart,_t:upsInfoTimerReboot,_u:upsInfoTimerShutdown,'upsInfoTest':upsInfoTest,_v:upsInfoTestInterval,_w:upsInfoTestResult,_x:upsInfoDisplayLanguage,_y:upsInfoContacts,_z:upsInfoEffciency,'upsInfoPower':upsInfoPower,_A0:upsInfoPowerValue,_A1:upsInfoPowerNominal,'upsInfoRealPower':upsInfoRealPower,_A2:upsInfoRealPowerValue,_A3:upsInfoRealPowerNominal,_A4:upsInfoBeeperStatus,_A5:upsInfoType,_A6:upsInfoWatchdogStatus,'upsInfoStart':upsInfoStart,_A7:upsInfoStartAuto,_A8:upsInfoStartBattery,_A9:upsInfoStartReboot,'upsBattery':upsBattery,'upsBatteryCharge':upsBatteryCharge,_AA:upsBatteryChargeValue,_AB:upsBatteryChargeLow,_AC:upsBatteryChargeRestart,_AD:upsBatteryChargeWarning,'upsBatteryVoltage':upsBatteryVoltage,_AE:upsBatteryVoltageValue,_AF:upsBatteryVoltageNominal,_AG:upsBatteryVoltageLow,_AH:upsBatteryVoltageHigh,_AI:upsBatteryCapacity,_AJ:upsBatteryCurrent,_AK:upsBatteryTemperature,'upsBatteryRuntime':upsBatteryRuntime,_AL:upsBatteryRuntimeValue,_AM:upsBatteryRuntimeLow,_AN:upsBatteryRuntimeRestart,_AO:upsBatteryAlarmThreshold,_AP:upsBatteryDate,_AQ:upsBatteryMfrDate,_AR:upsBatteryPacks,_AS:upsBatteryPacksBad,_AT:upsBatteryType,_AU:upsBatteryProtection,_AV:upsBatteryEnergySave,'upsInput':upsInput,'upsInputVoltage':upsInputVoltage,_AW:upsInputVoltageValue,_AX:upsInputVoltageMax,_AY:upsInputVoltageMin,_AZ:upsInputVoltageNominal,_Aa:upsInputVoltageExtend,_Ab:upsInputVoltageFault,'upsInputTransfer':upsInputTransfer,_Ac:upsInputTransferReason,_Ad:upsInputTransferLow,_Ae:upsInputTransferHigh,_Af:upsInputTransferLowMin,_Ag:upsInputTransferLowMax,_Ah:upsInputTransferHighMin,_Ai:upsInputTransferHighMax,_Aj:upsInputTransferBoostLow,_Ak:upsInputTransferBoostHigh,_Al:upsInputTransferTrimLow,_Am:upsInputTransferTrimHigh,_An:upsInputSensitivity,_Ao:upsInputQuality,'upsInputCurrent':upsInputCurrent,_Ap:upsInputCurrentValue,_Aq:upsInputCurrentNominal,'upsInputFrequency':upsInputFrequency,_Ar:upsInputFrequencyValue,_As:upsInputFrequencyNominal,_At:upsInputFrequencyLow,_Au:upsInputFrequencyHigh,_Av:upsInputFrequencyExtend,'upsOutput':upsOutput,'upsOutputVoltage':upsOutputVoltage,_Aw:upsOutputVoltageValue,_Ax:upsOutputVoltageNominal,'upsOutputFrequency':upsOutputFrequency,_Ay:upsOutputFrequencyValue,_Az:upsOutputFrequencyNominal,'upsOutputCurrent':upsOutputCurrent,_A_:upsOutputCurrentValue,_B0:upsOutputCurrentNominal,'upsAmbient':upsAmbient,'upsAmbientTemperature':upsAmbientTemperature,_B1:upsAmbientTemperatureValue,_B2:upsAmbientTemperatureAlarm,_B3:upsAmbientTemperatureHigh,_B4:upsAmbientTemperatureLow,_B5:upsAmbientTemperatureMax,_B6:upsAmbientTemperatureMin,'upsAmbientHumidity':upsAmbientHumidity,_B7:upsAmbientHumidityValue,_B8:upsAmbientHumidityAlarm,_B9:upsAmbientHumidityHigh,_BA:upsAmbientHumidityLow,_BB:upsAmbientHumidityMax,_BC:upsAmbientHumidityMin,'upsDriver':upsDriver,_BD:upsDriverName,_BE:upsDriverVersion,_BF:upsDriverVersionData,_BG:upsDriverVersionInternal,_BH:upsDriverPollInterval,_BI:upsDriverPort,_BJ:upsDriverPollFrequency,_BK:upsDriverProductID,_BL:upsDriverSnmpVersion,'upsServer':upsServer,_BM:upsServerInfo,_BN:upsServerVersion,'upsConformance':upsConformance,'upsCompliances':upsCompliances,'upsCompliance':upsCompliance,'upsGroups':upsGroups,'upsGroup':upsGroup})