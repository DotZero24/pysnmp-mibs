_s='xgs360026fVeriPHYPort'
_r='xgs360026fAccessMgtIndex'
_q='xgs360026fPortSecPortStatusIndex'
_p='xgs360026fPortSecSwitchStatusPort'
_o='xgs360026fPortSecLimitCtrlPort'
_n='xgs360026fDHCPSnoopingStatisticsPort'
_m='xgs360026fDHCPSnoopingPortModeConfigurationPort'
_l='xgs360026fARPInspectionDynamicIndex'
_k='xgs360026fARPInspectionStaticIndex'
_j='xgs360026fARPInspectionConfPortIndex'
_i='xgs360026fIPSourceGuardDynamicIndex'
_h='xgs360026fIPSourceGuardStaticIndex'
_g='xgs360026fIPSourceGuardPortConfigPort'
_f='xgs360026fMRSTPPortStatusPort'
_e='xgs360026fMRSTPPortConfigurationPort'
_d='xgs360026fMRSTPInstanceStatusInstance'
_c='xgs360026fMRSTPInstanceConfigurationInstance'
_b='xgs360026fERPSConfIndex'
_a='xgs360026fACLACEStatusIndex'
_Z='xgs360026fACLACEIndex'
_Y='xgs360026fACLRateLimiterID'
_X='xgs360026fACLPortsConfPort'
_W='xgs360026fMirrorPort'
_V='xgs360026fThermalProtectionPort'
_U='xgs360026fGVRPStatisticsPort'
_T='xgs360026fGVRPConfPort'
_S='xgs360026fGARPStatisticsPort'
_R='xgs360026fGARPConfPort'
_Q='xgs360026fSFPInfoIndex'
_P='xgs360026fPortQoSStatisticsPort'
_O='xgs360026fPortTrafficStatisticsPort'
_N='xgs360026fPortConfPort'
_M='xgs360026fTrapHostConfIndex'
_L='xgs360026fSyslogDetailedInfoIndex'
_K='xgs360026fUserIndex'
_J='xgs360026fSystemTimeNTPIndex'
_I='MacAddress'
_H='xgs360026fInformation'
_G='DisplayString'
_F='not-accessible'
_E='ZYXEL-XGS360026F-FUNCTION-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MacAddress,=mibBuilder.importSymbols('BRIDGE-MIB',_I)
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,_I,'PhysAddress','TextualConvention')
zyxel=ModuleIdentity((1,3,6,1,4,1,890))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,890,1))
_AccessSwitch_ObjectIdentity=ObjectIdentity
accessSwitch=_AccessSwitch_ObjectIdentity((1,3,6,1,4,1,890,1,5))
_EsSeries_ObjectIdentity=ObjectIdentity
esSeries=_EsSeries_ObjectIdentity((1,3,6,1,4,1,890,1,5,8))
_Xgs360026fProductId_ObjectIdentity=ObjectIdentity
xgs360026fProductId=_Xgs360026fProductId_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77))
_Xgs360026fSystem_ObjectIdentity=ObjectIdentity
xgs360026fSystem=_Xgs360026fSystem_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1))
_Xgs360026fSystemInformation_ObjectIdentity=ObjectIdentity
xgs360026fSystemInformation=_Xgs360026fSystemInformation_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,1))
_Xgs360026fModelName_Type=DisplayString
_Xgs360026fModelName_Object=MibScalar
xgs360026fModelName=_Xgs360026fModelName_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,1),_Xgs360026fModelName_Type())
xgs360026fModelName.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fModelName.setStatus(_A)
_Xgs360026fBIOSVersion_Type=DisplayString
_Xgs360026fBIOSVersion_Object=MibScalar
xgs360026fBIOSVersion=_Xgs360026fBIOSVersion_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,2),_Xgs360026fBIOSVersion_Type())
xgs360026fBIOSVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fBIOSVersion.setStatus(_A)
_Xgs360026fFirmwareVersion_Type=DisplayString
_Xgs360026fFirmwareVersion_Object=MibScalar
xgs360026fFirmwareVersion=_Xgs360026fFirmwareVersion_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,3),_Xgs360026fFirmwareVersion_Type())
xgs360026fFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fFirmwareVersion.setStatus(_A)
_Xgs360026fHardwareMechanicalVersion_Type=DisplayString
_Xgs360026fHardwareMechanicalVersion_Object=MibScalar
xgs360026fHardwareMechanicalVersion=_Xgs360026fHardwareMechanicalVersion_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,4),_Xgs360026fHardwareMechanicalVersion_Type())
xgs360026fHardwareMechanicalVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fHardwareMechanicalVersion.setStatus(_A)
_Xgs360026fSeriesNumber_Type=DisplayString
_Xgs360026fSeriesNumber_Object=MibScalar
xgs360026fSeriesNumber=_Xgs360026fSeriesNumber_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,5),_Xgs360026fSeriesNumber_Type())
xgs360026fSeriesNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSeriesNumber.setStatus(_A)
_Xgs360026fHostMACAddress_Type=MacAddress
_Xgs360026fHostMACAddress_Object=MibScalar
xgs360026fHostMACAddress=_Xgs360026fHostMACAddress_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,6),_Xgs360026fHostMACAddress_Type())
xgs360026fHostMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fHostMACAddress.setStatus(_A)
_Xgs360026fConsoleBaudrate_Type=DisplayString
_Xgs360026fConsoleBaudrate_Object=MibScalar
xgs360026fConsoleBaudrate=_Xgs360026fConsoleBaudrate_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,7),_Xgs360026fConsoleBaudrate_Type())
xgs360026fConsoleBaudrate.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fConsoleBaudrate.setStatus(_A)
_Xgs360026fRAMSize_Type=DisplayString
_Xgs360026fRAMSize_Object=MibScalar
xgs360026fRAMSize=_Xgs360026fRAMSize_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,8),_Xgs360026fRAMSize_Type())
xgs360026fRAMSize.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fRAMSize.setStatus(_A)
_Xgs360026fFlashSize_Type=DisplayString
_Xgs360026fFlashSize_Object=MibScalar
xgs360026fFlashSize=_Xgs360026fFlashSize_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,9),_Xgs360026fFlashSize_Type())
xgs360026fFlashSize.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fFlashSize.setStatus(_A)
_Xgs360026fBridgeFBDSize_Type=DisplayString
_Xgs360026fBridgeFBDSize_Object=MibScalar
xgs360026fBridgeFBDSize=_Xgs360026fBridgeFBDSize_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,10),_Xgs360026fBridgeFBDSize_Type())
xgs360026fBridgeFBDSize.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fBridgeFBDSize.setStatus(_A)
_Xgs360026fTransmitQueue_Type=DisplayString
_Xgs360026fTransmitQueue_Object=MibScalar
xgs360026fTransmitQueue=_Xgs360026fTransmitQueue_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,11),_Xgs360026fTransmitQueue_Type())
xgs360026fTransmitQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fTransmitQueue.setStatus(_A)
_Xgs360026fMaximumFrameSize_Type=DisplayString
_Xgs360026fMaximumFrameSize_Object=MibScalar
xgs360026fMaximumFrameSize=_Xgs360026fMaximumFrameSize_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,12),_Xgs360026fMaximumFrameSize_Type())
xgs360026fMaximumFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMaximumFrameSize.setStatus(_A)
_Xgs360026fCPULoad_Type=DisplayString
_Xgs360026fCPULoad_Object=MibScalar
xgs360026fCPULoad=_Xgs360026fCPULoad_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,13),_Xgs360026fCPULoad_Type())
xgs360026fCPULoad.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fCPULoad.setStatus(_A)
_Xgs360026fFanSpeed_Type=DisplayString
_Xgs360026fFanSpeed_Object=MibScalar
xgs360026fFanSpeed=_Xgs360026fFanSpeed_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,14),_Xgs360026fFanSpeed_Type())
xgs360026fFanSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fFanSpeed.setStatus(_A)
_Xgs360026fPowers_Type=DisplayString
_Xgs360026fPowers_Object=MibScalar
xgs360026fPowers=_Xgs360026fPowers_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,15),_Xgs360026fPowers_Type())
xgs360026fPowers.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPowers.setStatus(_A)
_Xgs360026fTemperature1_Type=DisplayString
_Xgs360026fTemperature1_Object=MibScalar
xgs360026fTemperature1=_Xgs360026fTemperature1_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,16),_Xgs360026fTemperature1_Type())
xgs360026fTemperature1.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fTemperature1.setStatus(_A)
_Xgs360026fTemperature2_Type=DisplayString
_Xgs360026fTemperature2_Object=MibScalar
xgs360026fTemperature2=_Xgs360026fTemperature2_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,17),_Xgs360026fTemperature2_Type())
xgs360026fTemperature2.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fTemperature2.setStatus(_A)
_Xgs360026fTemperature3_Type=DisplayString
_Xgs360026fTemperature3_Object=MibScalar
xgs360026fTemperature3=_Xgs360026fTemperature3_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,18),_Xgs360026fTemperature3_Type())
xgs360026fTemperature3.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fTemperature3.setStatus(_A)
_Xgs360026fTemperature4_Type=DisplayString
_Xgs360026fTemperature4_Object=MibScalar
xgs360026fTemperature4=_Xgs360026fTemperature4_Object((1,3,6,1,4,1,890,1,5,8,77,1,1,19),_Xgs360026fTemperature4_Type())
xgs360026fTemperature4.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fTemperature4.setStatus(_A)
_Xgs360026fSystemTime_ObjectIdentity=ObjectIdentity
xgs360026fSystemTime=_Xgs360026fSystemTime_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,2))
_Xgs360026fSystemTimeManual_ObjectIdentity=ObjectIdentity
xgs360026fSystemTimeManual=_Xgs360026fSystemTimeManual_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,2,1))
class _Xgs360026fSystemTimeManualClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fSystemTimeManualClockSource_Type.__name__=_B
_Xgs360026fSystemTimeManualClockSource_Object=MibScalar
xgs360026fSystemTimeManualClockSource=_Xgs360026fSystemTimeManualClockSource_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,1),_Xgs360026fSystemTimeManualClockSource_Type())
xgs360026fSystemTimeManualClockSource.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualClockSource.setStatus(_A)
_Xgs360026fSystemTimeManualLocaltime_Type=DisplayString
_Xgs360026fSystemTimeManualLocaltime_Object=MibScalar
xgs360026fSystemTimeManualLocaltime=_Xgs360026fSystemTimeManualLocaltime_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,2),_Xgs360026fSystemTimeManualLocaltime_Type())
xgs360026fSystemTimeManualLocaltime.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualLocaltime.setStatus(_A)
class _Xgs360026fSystemTimeManualTimeZoneOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-720,780))
_Xgs360026fSystemTimeManualTimeZoneOffset_Type.__name__=_B
_Xgs360026fSystemTimeManualTimeZoneOffset_Object=MibScalar
xgs360026fSystemTimeManualTimeZoneOffset=_Xgs360026fSystemTimeManualTimeZoneOffset_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,3),_Xgs360026fSystemTimeManualTimeZoneOffset_Type())
xgs360026fSystemTimeManualTimeZoneOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualTimeZoneOffset.setStatus(_A)
class _Xgs360026fSystemTimeManualDaylightSavings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fSystemTimeManualDaylightSavings_Type.__name__=_B
_Xgs360026fSystemTimeManualDaylightSavings_Object=MibScalar
xgs360026fSystemTimeManualDaylightSavings=_Xgs360026fSystemTimeManualDaylightSavings_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,4),_Xgs360026fSystemTimeManualDaylightSavings_Type())
xgs360026fSystemTimeManualDaylightSavings.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualDaylightSavings.setStatus(_A)
class _Xgs360026fSystemTimeManualTimeSetOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_Xgs360026fSystemTimeManualTimeSetOffset_Type.__name__=_B
_Xgs360026fSystemTimeManualTimeSetOffset_Object=MibScalar
xgs360026fSystemTimeManualTimeSetOffset=_Xgs360026fSystemTimeManualTimeSetOffset_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,5),_Xgs360026fSystemTimeManualTimeSetOffset_Type())
xgs360026fSystemTimeManualTimeSetOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualTimeSetOffset.setStatus(_A)
class _Xgs360026fSystemTimeManualDaylightSavingsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fSystemTimeManualDaylightSavingsType_Type.__name__=_B
_Xgs360026fSystemTimeManualDaylightSavingsType_Object=MibScalar
xgs360026fSystemTimeManualDaylightSavingsType=_Xgs360026fSystemTimeManualDaylightSavingsType_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,6),_Xgs360026fSystemTimeManualDaylightSavingsType_Type())
xgs360026fSystemTimeManualDaylightSavingsType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualDaylightSavingsType.setStatus(_A)
_Xgs360026fSystemTimeManualDaylightSavingsBydatesFrom_Type=DisplayString
_Xgs360026fSystemTimeManualDaylightSavingsBydatesFrom_Object=MibScalar
xgs360026fSystemTimeManualDaylightSavingsBydatesFrom=_Xgs360026fSystemTimeManualDaylightSavingsBydatesFrom_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,7),_Xgs360026fSystemTimeManualDaylightSavingsBydatesFrom_Type())
xgs360026fSystemTimeManualDaylightSavingsBydatesFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualDaylightSavingsBydatesFrom.setStatus(_A)
_Xgs360026fSystemTimeManualDaylightSavingsBydatesTo_Type=DisplayString
_Xgs360026fSystemTimeManualDaylightSavingsBydatesTo_Object=MibScalar
xgs360026fSystemTimeManualDaylightSavingsBydatesTo=_Xgs360026fSystemTimeManualDaylightSavingsBydatesTo_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,8),_Xgs360026fSystemTimeManualDaylightSavingsBydatesTo_Type())
xgs360026fSystemTimeManualDaylightSavingsBydatesTo.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualDaylightSavingsBydatesTo.setStatus(_A)
class _Xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_Xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom_Type.__name__=_B
_Xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom_Object=MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom=_Xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,9),_Xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom_Type())
xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom.setStatus(_A)
class _Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom_Type.__name__=_B
_Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom_Object=MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom=_Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,10),_Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom_Type())
xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom.setStatus(_A)
class _Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom_Type.__name__=_B
_Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom_Object=MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom=_Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,11),_Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom_Type())
xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom.setStatus(_A)
_Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom_Type=DisplayString
_Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom_Object=MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom=_Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,12),_Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom_Type())
xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom.setStatus(_A)
class _Xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_Xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo_Type.__name__=_B
_Xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo_Object=MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo=_Xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,13),_Xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo_Type())
xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo.setStatus(_A)
class _Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo_Type.__name__=_B
_Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo_Object=MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo=_Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,14),_Xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo_Type())
xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo.setStatus(_A)
class _Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo_Type.__name__=_B
_Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo_Object=MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo=_Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,15),_Xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo_Type())
xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo.setStatus(_A)
_Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo_Type=DisplayString
_Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo_Object=MibScalar
xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo=_Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,1,16),_Xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo_Type())
xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo.setStatus(_A)
_Xgs360026fSystemTimeNTP_ObjectIdentity=ObjectIdentity
xgs360026fSystemTimeNTP=_Xgs360026fSystemTimeNTP_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,2,2))
_Xgs360026fSystemTimeNTPTable_Object=MibTable
xgs360026fSystemTimeNTPTable=_Xgs360026fSystemTimeNTPTable_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,2,1))
if mibBuilder.loadTexts:xgs360026fSystemTimeNTPTable.setStatus(_A)
_Xgs360026fSystemTimeNTPEntry_Object=MibTableRow
xgs360026fSystemTimeNTPEntry=_Xgs360026fSystemTimeNTPEntry_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,2,1,1))
xgs360026fSystemTimeNTPEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:xgs360026fSystemTimeNTPEntry.setStatus(_A)
class _Xgs360026fSystemTimeNTPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360026fSystemTimeNTPIndex_Type.__name__=_B
_Xgs360026fSystemTimeNTPIndex_Object=MibTableColumn
xgs360026fSystemTimeNTPIndex=_Xgs360026fSystemTimeNTPIndex_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,2,1,1,1),_Xgs360026fSystemTimeNTPIndex_Type())
xgs360026fSystemTimeNTPIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fSystemTimeNTPIndex.setStatus(_A)
class _Xgs360026fSystemTimeNTPServerIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fSystemTimeNTPServerIPType_Type.__name__=_B
_Xgs360026fSystemTimeNTPServerIPType_Object=MibTableColumn
xgs360026fSystemTimeNTPServerIPType=_Xgs360026fSystemTimeNTPServerIPType_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,2,1,1,2),_Xgs360026fSystemTimeNTPServerIPType_Type())
xgs360026fSystemTimeNTPServerIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeNTPServerIPType.setStatus(_A)
_Xgs360026fSystemTimeNTPServer_Type=DisplayString
_Xgs360026fSystemTimeNTPServer_Object=MibTableColumn
xgs360026fSystemTimeNTPServer=_Xgs360026fSystemTimeNTPServer_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,2,1,1,3),_Xgs360026fSystemTimeNTPServer_Type())
xgs360026fSystemTimeNTPServer.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeNTPServer.setStatus(_A)
class _Xgs360026fSystemTimeNTPCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360026fSystemTimeNTPCurrentMode_Type.__name__=_B
_Xgs360026fSystemTimeNTPCurrentMode_Object=MibTableColumn
xgs360026fSystemTimeNTPCurrentMode=_Xgs360026fSystemTimeNTPCurrentMode_Object((1,3,6,1,4,1,890,1,5,8,77,1,2,2,1,1,4),_Xgs360026fSystemTimeNTPCurrentMode_Type())
xgs360026fSystemTimeNTPCurrentMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemTimeNTPCurrentMode.setStatus(_A)
_Xgs360026fSystemAccount_ObjectIdentity=ObjectIdentity
xgs360026fSystemAccount=_Xgs360026fSystemAccount_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,3))
_Xgs360026fSystemAccountUsers_ObjectIdentity=ObjectIdentity
xgs360026fSystemAccountUsers=_Xgs360026fSystemAccountUsers_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,3,1))
class _Xgs360026fSystemAccountUserCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fSystemAccountUserCreate_Type.__name__=_B
_Xgs360026fSystemAccountUserCreate_Object=MibScalar
xgs360026fSystemAccountUserCreate=_Xgs360026fSystemAccountUserCreate_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,1,1),_Xgs360026fSystemAccountUserCreate_Type())
xgs360026fSystemAccountUserCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemAccountUserCreate.setStatus(_A)
_Xgs360026fSystemAccountUsersTable_Object=MibTable
xgs360026fSystemAccountUsersTable=_Xgs360026fSystemAccountUsersTable_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,1,2))
if mibBuilder.loadTexts:xgs360026fSystemAccountUsersTable.setStatus(_A)
_Xgs360026fSystemAccountUsersEntry_Object=MibTableRow
xgs360026fSystemAccountUsersEntry=_Xgs360026fSystemAccountUsersEntry_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,1,2,1))
xgs360026fSystemAccountUsersEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:xgs360026fSystemAccountUsersEntry.setStatus(_A)
class _Xgs360026fUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_Xgs360026fUserIndex_Type.__name__=_B
_Xgs360026fUserIndex_Object=MibTableColumn
xgs360026fUserIndex=_Xgs360026fUserIndex_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,1,2,1,1),_Xgs360026fUserIndex_Type())
xgs360026fUserIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fUserIndex.setStatus(_A)
class _Xgs360026fUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Xgs360026fUserName_Type.__name__=_G
_Xgs360026fUserName_Object=MibTableColumn
xgs360026fUserName=_Xgs360026fUserName_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,1,2,1,2),_Xgs360026fUserName_Type())
xgs360026fUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fUserName.setStatus(_A)
class _Xgs360026fPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Xgs360026fPassword_Type.__name__=_G
_Xgs360026fPassword_Object=MibTableColumn
xgs360026fPassword=_Xgs360026fPassword_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,1,2,1,3),_Xgs360026fPassword_Type())
xgs360026fPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPassword.setStatus(_A)
class _Xgs360026fUserPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fUserPrivilegeLevel_Type.__name__=_B
_Xgs360026fUserPrivilegeLevel_Object=MibTableColumn
xgs360026fUserPrivilegeLevel=_Xgs360026fUserPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,1,2,1,4),_Xgs360026fUserPrivilegeLevel_Type())
xgs360026fUserPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fUserPrivilegeLevel.setStatus(_A)
class _Xgs360026fAccountUserRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360026fAccountUserRowStatus_Type.__name__=_B
_Xgs360026fAccountUserRowStatus_Object=MibTableColumn
xgs360026fAccountUserRowStatus=_Xgs360026fAccountUserRowStatus_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,1,2,1,5),_Xgs360026fAccountUserRowStatus_Type())
xgs360026fAccountUserRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fAccountUserRowStatus.setStatus(_A)
_Xgs360026fSystemAccountPrivilegeLevel_ObjectIdentity=ObjectIdentity
xgs360026fSystemAccountPrivilegeLevel=_Xgs360026fSystemAccountPrivilegeLevel_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,3,2))
class _Xgs360026fAccountPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fAccountPrivilegeLevel_Type.__name__=_B
_Xgs360026fAccountPrivilegeLevel_Object=MibScalar
xgs360026fAccountPrivilegeLevel=_Xgs360026fAccountPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,1),_Xgs360026fAccountPrivilegeLevel_Type())
xgs360026fAccountPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fAccountPrivilegeLevel.setStatus(_A)
class _Xgs360026fAggregationPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fAggregationPrivilegeLevel_Type.__name__=_B
_Xgs360026fAggregationPrivilegeLevel_Object=MibScalar
xgs360026fAggregationPrivilegeLevel=_Xgs360026fAggregationPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,2),_Xgs360026fAggregationPrivilegeLevel_Type())
xgs360026fAggregationPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fAggregationPrivilegeLevel.setStatus(_A)
class _Xgs360026fDiagnosticsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fDiagnosticsPrivilegeLevel_Type.__name__=_B
_Xgs360026fDiagnosticsPrivilegeLevel_Object=MibScalar
xgs360026fDiagnosticsPrivilegeLevel=_Xgs360026fDiagnosticsPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,3),_Xgs360026fDiagnosticsPrivilegeLevel_Type())
xgs360026fDiagnosticsPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fDiagnosticsPrivilegeLevel.setStatus(_A)
class _Xgs360026fEPSPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fEPSPrivilegeLevel_Type.__name__=_B
_Xgs360026fEPSPrivilegeLevel_Object=MibScalar
xgs360026fEPSPrivilegeLevel=_Xgs360026fEPSPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,5),_Xgs360026fEPSPrivilegeLevel_Type())
xgs360026fEPSPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fEPSPrivilegeLevel.setStatus(_A)
class _Xgs360026fERPSPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fERPSPrivilegeLevel_Type.__name__=_B
_Xgs360026fERPSPrivilegeLevel_Object=MibScalar
xgs360026fERPSPrivilegeLevel=_Xgs360026fERPSPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,6),_Xgs360026fERPSPrivilegeLevel_Type())
xgs360026fERPSPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSPrivilegeLevel.setStatus(_A)
class _Xgs360026fETHLinkOAMPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fETHLinkOAMPrivilegeLevel_Type.__name__=_B
_Xgs360026fETHLinkOAMPrivilegeLevel_Object=MibScalar
xgs360026fETHLinkOAMPrivilegeLevel=_Xgs360026fETHLinkOAMPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,7),_Xgs360026fETHLinkOAMPrivilegeLevel_Type())
xgs360026fETHLinkOAMPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fETHLinkOAMPrivilegeLevel.setStatus(_A)
class _Xgs360026fEVCPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fEVCPrivilegeLevel_Type.__name__=_B
_Xgs360026fEVCPrivilegeLevel_Object=MibScalar
xgs360026fEVCPrivilegeLevel=_Xgs360026fEVCPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,8),_Xgs360026fEVCPrivilegeLevel_Type())
xgs360026fEVCPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fEVCPrivilegeLevel.setStatus(_A)
class _Xgs360026fGARPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fGARPPrivilegeLevel_Type.__name__=_B
_Xgs360026fGARPPrivilegeLevel_Object=MibScalar
xgs360026fGARPPrivilegeLevel=_Xgs360026fGARPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,10),_Xgs360026fGARPPrivilegeLevel_Type())
xgs360026fGARPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fGARPPrivilegeLevel.setStatus(_A)
class _Xgs360026fGVRPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fGVRPPrivilegeLevel_Type.__name__=_B
_Xgs360026fGVRPPrivilegeLevel_Object=MibScalar
xgs360026fGVRPPrivilegeLevel=_Xgs360026fGVRPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,11),_Xgs360026fGVRPPrivilegeLevel_Type())
xgs360026fGVRPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fGVRPPrivilegeLevel.setStatus(_A)
class _Xgs360026fIPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fIPPrivilegeLevel_Type.__name__=_B
_Xgs360026fIPPrivilegeLevel_Object=MibScalar
xgs360026fIPPrivilegeLevel=_Xgs360026fIPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,12),_Xgs360026fIPPrivilegeLevel_Type())
xgs360026fIPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPPrivilegeLevel.setStatus(_A)
class _Xgs360026fIPMCSnoopingPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fIPMCSnoopingPrivilegeLevel_Type.__name__=_B
_Xgs360026fIPMCSnoopingPrivilegeLevel_Object=MibScalar
xgs360026fIPMCSnoopingPrivilegeLevel=_Xgs360026fIPMCSnoopingPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,13),_Xgs360026fIPMCSnoopingPrivilegeLevel_Type())
xgs360026fIPMCSnoopingPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPMCSnoopingPrivilegeLevel.setStatus(_A)
class _Xgs360026fLACPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fLACPPrivilegeLevel_Type.__name__=_B
_Xgs360026fLACPPrivilegeLevel_Object=MibScalar
xgs360026fLACPPrivilegeLevel=_Xgs360026fLACPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,14),_Xgs360026fLACPPrivilegeLevel_Type())
xgs360026fLACPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fLACPPrivilegeLevel.setStatus(_A)
class _Xgs360026fLLDPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fLLDPPrivilegeLevel_Type.__name__=_B
_Xgs360026fLLDPPrivilegeLevel_Object=MibScalar
xgs360026fLLDPPrivilegeLevel=_Xgs360026fLLDPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,15),_Xgs360026fLLDPPrivilegeLevel_Type())
xgs360026fLLDPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fLLDPPrivilegeLevel.setStatus(_A)
class _Xgs360026fLLDPMEDPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fLLDPMEDPrivilegeLevel_Type.__name__=_B
_Xgs360026fLLDPMEDPrivilegeLevel_Object=MibScalar
xgs360026fLLDPMEDPrivilegeLevel=_Xgs360026fLLDPMEDPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,16),_Xgs360026fLLDPMEDPrivilegeLevel_Type())
xgs360026fLLDPMEDPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fLLDPMEDPrivilegeLevel.setStatus(_A)
class _Xgs360026fLoopProtectPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fLoopProtectPrivilegeLevel_Type.__name__=_B
_Xgs360026fLoopProtectPrivilegeLevel_Object=MibScalar
xgs360026fLoopProtectPrivilegeLevel=_Xgs360026fLoopProtectPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,17),_Xgs360026fLoopProtectPrivilegeLevel_Type())
xgs360026fLoopProtectPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fLoopProtectPrivilegeLevel.setStatus(_A)
class _Xgs360026fMACTablePrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fMACTablePrivilegeLevel_Type.__name__=_B
_Xgs360026fMACTablePrivilegeLevel_Object=MibScalar
xgs360026fMACTablePrivilegeLevel=_Xgs360026fMACTablePrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,18),_Xgs360026fMACTablePrivilegeLevel_Type())
xgs360026fMACTablePrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMACTablePrivilegeLevel.setStatus(_A)
class _Xgs360026fMEPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fMEPPrivilegeLevel_Type.__name__=_B
_Xgs360026fMEPPrivilegeLevel_Object=MibScalar
xgs360026fMEPPrivilegeLevel=_Xgs360026fMEPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,20),_Xgs360026fMEPPrivilegeLevel_Type())
xgs360026fMEPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMEPPrivilegeLevel.setStatus(_A)
class _Xgs360026fMRSTPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fMRSTPPrivilegeLevel_Type.__name__=_B
_Xgs360026fMRSTPPrivilegeLevel_Object=MibScalar
xgs360026fMRSTPPrivilegeLevel=_Xgs360026fMRSTPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,21),_Xgs360026fMRSTPPrivilegeLevel_Type())
xgs360026fMRSTPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMRSTPPrivilegeLevel.setStatus(_A)
class _Xgs360026fMVRPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fMVRPrivilegeLevel_Type.__name__=_B
_Xgs360026fMVRPrivilegeLevel_Object=MibScalar
xgs360026fMVRPrivilegeLevel=_Xgs360026fMVRPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,22),_Xgs360026fMVRPrivilegeLevel_Type())
xgs360026fMVRPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMVRPrivilegeLevel.setStatus(_A)
class _Xgs360026fMaintenancePrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fMaintenancePrivilegeLevel_Type.__name__=_B
_Xgs360026fMaintenancePrivilegeLevel_Object=MibScalar
xgs360026fMaintenancePrivilegeLevel=_Xgs360026fMaintenancePrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,24),_Xgs360026fMaintenancePrivilegeLevel_Type())
xgs360026fMaintenancePrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMaintenancePrivilegeLevel.setStatus(_A)
class _Xgs360026fMirroringPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fMirroringPrivilegeLevel_Type.__name__=_B
_Xgs360026fMirroringPrivilegeLevel_Object=MibScalar
xgs360026fMirroringPrivilegeLevel=_Xgs360026fMirroringPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,25),_Xgs360026fMirroringPrivilegeLevel_Type())
xgs360026fMirroringPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMirroringPrivilegeLevel.setStatus(_A)
class _Xgs360026fPTPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fPTPPrivilegeLevel_Type.__name__=_B
_Xgs360026fPTPPrivilegeLevel_Object=MibScalar
xgs360026fPTPPrivilegeLevel=_Xgs360026fPTPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,26),_Xgs360026fPTPPrivilegeLevel_Type())
xgs360026fPTPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPTPPrivilegeLevel.setStatus(_A)
class _Xgs360026fPortsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fPortsPrivilegeLevel_Type.__name__=_B
_Xgs360026fPortsPrivilegeLevel_Object=MibScalar
xgs360026fPortsPrivilegeLevel=_Xgs360026fPortsPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,27),_Xgs360026fPortsPrivilegeLevel_Type())
xgs360026fPortsPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortsPrivilegeLevel.setStatus(_A)
class _Xgs360026fPrivateVLANsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fPrivateVLANsPrivilegeLevel_Type.__name__=_B
_Xgs360026fPrivateVLANsPrivilegeLevel_Object=MibScalar
xgs360026fPrivateVLANsPrivilegeLevel=_Xgs360026fPrivateVLANsPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,28),_Xgs360026fPrivateVLANsPrivilegeLevel_Type())
xgs360026fPrivateVLANsPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPrivateVLANsPrivilegeLevel.setStatus(_A)
class _Xgs360026fQoSPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fQoSPrivilegeLevel_Type.__name__=_B
_Xgs360026fQoSPrivilegeLevel_Object=MibScalar
xgs360026fQoSPrivilegeLevel=_Xgs360026fQoSPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,29),_Xgs360026fQoSPrivilegeLevel_Type())
xgs360026fQoSPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fQoSPrivilegeLevel.setStatus(_A)
class _Xgs360026fSMTPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fSMTPPrivilegeLevel_Type.__name__=_B
_Xgs360026fSMTPPrivilegeLevel_Object=MibScalar
xgs360026fSMTPPrivilegeLevel=_Xgs360026fSMTPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,31),_Xgs360026fSMTPPrivilegeLevel_Type())
xgs360026fSMTPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSMTPPrivilegeLevel.setStatus(_A)
class _Xgs360026fSNMPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fSNMPPrivilegeLevel_Type.__name__=_B
_Xgs360026fSNMPPrivilegeLevel_Object=MibScalar
xgs360026fSNMPPrivilegeLevel=_Xgs360026fSNMPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,32),_Xgs360026fSNMPPrivilegeLevel_Type())
xgs360026fSNMPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSNMPPrivilegeLevel.setStatus(_A)
class _Xgs360026fSecurityPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fSecurityPrivilegeLevel_Type.__name__=_B
_Xgs360026fSecurityPrivilegeLevel_Object=MibScalar
xgs360026fSecurityPrivilegeLevel=_Xgs360026fSecurityPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,33),_Xgs360026fSecurityPrivilegeLevel_Type())
xgs360026fSecurityPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSecurityPrivilegeLevel.setStatus(_A)
class _Xgs360026fSpanningTreePrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fSpanningTreePrivilegeLevel_Type.__name__=_B
_Xgs360026fSpanningTreePrivilegeLevel_Object=MibScalar
xgs360026fSpanningTreePrivilegeLevel=_Xgs360026fSpanningTreePrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,35),_Xgs360026fSpanningTreePrivilegeLevel_Type())
xgs360026fSpanningTreePrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSpanningTreePrivilegeLevel.setStatus(_A)
class _Xgs360026fSystemPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fSystemPrivilegeLevel_Type.__name__=_B
_Xgs360026fSystemPrivilegeLevel_Object=MibScalar
xgs360026fSystemPrivilegeLevel=_Xgs360026fSystemPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,36),_Xgs360026fSystemPrivilegeLevel_Type())
xgs360026fSystemPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSystemPrivilegeLevel.setStatus(_A)
class _Xgs360026fTrapEventPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fTrapEventPrivilegeLevel_Type.__name__=_B
_Xgs360026fTrapEventPrivilegeLevel_Object=MibScalar
xgs360026fTrapEventPrivilegeLevel=_Xgs360026fTrapEventPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,37),_Xgs360026fTrapEventPrivilegeLevel_Type())
xgs360026fTrapEventPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventPrivilegeLevel.setStatus(_A)
class _Xgs360026fVCLPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fVCLPrivilegeLevel_Type.__name__=_B
_Xgs360026fVCLPrivilegeLevel_Object=MibScalar
xgs360026fVCLPrivilegeLevel=_Xgs360026fVCLPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,39),_Xgs360026fVCLPrivilegeLevel_Type())
xgs360026fVCLPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fVCLPrivilegeLevel.setStatus(_A)
class _Xgs360026fVLANTranslationPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fVLANTranslationPrivilegeLevel_Type.__name__=_B
_Xgs360026fVLANTranslationPrivilegeLevel_Object=MibScalar
xgs360026fVLANTranslationPrivilegeLevel=_Xgs360026fVLANTranslationPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,40),_Xgs360026fVLANTranslationPrivilegeLevel_Type())
xgs360026fVLANTranslationPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fVLANTranslationPrivilegeLevel.setStatus(_A)
class _Xgs360026fVLANsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360026fVLANsPrivilegeLevel_Type.__name__=_B
_Xgs360026fVLANsPrivilegeLevel_Object=MibScalar
xgs360026fVLANsPrivilegeLevel=_Xgs360026fVLANsPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,3,2,41),_Xgs360026fVLANsPrivilegeLevel_Type())
xgs360026fVLANsPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fVLANsPrivilegeLevel.setStatus(_A)
_Xgs360026fIP_ObjectIdentity=ObjectIdentity
xgs360026fIP=_Xgs360026fIP_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,4))
_Xgs360026fIPv4_ObjectIdentity=ObjectIdentity
xgs360026fIPv4=_Xgs360026fIPv4_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,4,1))
_Xgs360026fIPv4Configured_ObjectIdentity=ObjectIdentity
xgs360026fIPv4Configured=_Xgs360026fIPv4Configured_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,4,1,1))
class _Xgs360026fIpv4DHCPClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fIpv4DHCPClient_Type.__name__=_B
_Xgs360026fIpv4DHCPClient_Object=MibScalar
xgs360026fIpv4DHCPClient=_Xgs360026fIpv4DHCPClient_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,1,1,1),_Xgs360026fIpv4DHCPClient_Type())
xgs360026fIpv4DHCPClient.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIpv4DHCPClient.setStatus(_A)
_Xgs360026fIPv4Address_Type=IpAddress
_Xgs360026fIPv4Address_Object=MibScalar
xgs360026fIPv4Address=_Xgs360026fIPv4Address_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,1,1,2),_Xgs360026fIPv4Address_Type())
xgs360026fIPv4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPv4Address.setStatus(_A)
_Xgs360026fIPv4Mask_Type=IpAddress
_Xgs360026fIPv4Mask_Object=MibScalar
xgs360026fIPv4Mask=_Xgs360026fIPv4Mask_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,1,1,3),_Xgs360026fIPv4Mask_Type())
xgs360026fIPv4Mask.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPv4Mask.setStatus(_A)
_Xgs360026fIPv4Router_Type=IpAddress
_Xgs360026fIPv4Router_Object=MibScalar
xgs360026fIPv4Router=_Xgs360026fIPv4Router_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,1,1,4),_Xgs360026fIPv4Router_Type())
xgs360026fIPv4Router.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPv4Router.setStatus(_A)
class _Xgs360026fIPv4VLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Xgs360026fIPv4VLANId_Type.__name__=_B
_Xgs360026fIPv4VLANId_Object=MibScalar
xgs360026fIPv4VLANId=_Xgs360026fIPv4VLANId_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,1,1,5),_Xgs360026fIPv4VLANId_Type())
xgs360026fIPv4VLANId.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPv4VLANId.setStatus(_A)
_Xgs360026fIPv4DNSServer_Type=IpAddress
_Xgs360026fIPv4DNSServer_Object=MibScalar
xgs360026fIPv4DNSServer=_Xgs360026fIPv4DNSServer_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,1,1,6),_Xgs360026fIPv4DNSServer_Type())
xgs360026fIPv4DNSServer.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPv4DNSServer.setStatus(_A)
class _Xgs360026fIPv4DNSProxy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fIPv4DNSProxy_Type.__name__=_B
_Xgs360026fIPv4DNSProxy_Object=MibScalar
xgs360026fIPv4DNSProxy=_Xgs360026fIPv4DNSProxy_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,1,1,7),_Xgs360026fIPv4DNSProxy_Type())
xgs360026fIPv4DNSProxy.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPv4DNSProxy.setStatus(_A)
_Xgs360026fIPv4Current_ObjectIdentity=ObjectIdentity
xgs360026fIPv4Current=_Xgs360026fIPv4Current_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,4,1,2))
class _Xgs360026fIpv4CurrentDHCPClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fIpv4CurrentDHCPClient_Type.__name__=_B
_Xgs360026fIpv4CurrentDHCPClient_Object=MibScalar
xgs360026fIpv4CurrentDHCPClient=_Xgs360026fIpv4CurrentDHCPClient_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,1,2,1),_Xgs360026fIpv4CurrentDHCPClient_Type())
xgs360026fIpv4CurrentDHCPClient.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIpv4CurrentDHCPClient.setStatus(_A)
_Xgs360026fIPv4CurrentAddress_Type=IpAddress
_Xgs360026fIPv4CurrentAddress_Object=MibScalar
xgs360026fIPv4CurrentAddress=_Xgs360026fIPv4CurrentAddress_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,1,2,2),_Xgs360026fIPv4CurrentAddress_Type())
xgs360026fIPv4CurrentAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fIPv4CurrentAddress.setStatus(_A)
_Xgs360026fIPv4CurrentMask_Type=IpAddress
_Xgs360026fIPv4CurrentMask_Object=MibScalar
xgs360026fIPv4CurrentMask=_Xgs360026fIPv4CurrentMask_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,1,2,3),_Xgs360026fIPv4CurrentMask_Type())
xgs360026fIPv4CurrentMask.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fIPv4CurrentMask.setStatus(_A)
_Xgs360026fIPv4CurrentRouter_Type=IpAddress
_Xgs360026fIPv4CurrentRouter_Object=MibScalar
xgs360026fIPv4CurrentRouter=_Xgs360026fIPv4CurrentRouter_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,1,2,4),_Xgs360026fIPv4CurrentRouter_Type())
xgs360026fIPv4CurrentRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fIPv4CurrentRouter.setStatus(_A)
class _Xgs360026fIPv4CurrentVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Xgs360026fIPv4CurrentVLANId_Type.__name__=_B
_Xgs360026fIPv4CurrentVLANId_Object=MibScalar
xgs360026fIPv4CurrentVLANId=_Xgs360026fIPv4CurrentVLANId_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,1,2,5),_Xgs360026fIPv4CurrentVLANId_Type())
xgs360026fIPv4CurrentVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fIPv4CurrentVLANId.setStatus(_A)
_Xgs360026fIPv4CurrentDNSServer_Type=IpAddress
_Xgs360026fIPv4CurrentDNSServer_Object=MibScalar
xgs360026fIPv4CurrentDNSServer=_Xgs360026fIPv4CurrentDNSServer_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,1,2,6),_Xgs360026fIPv4CurrentDNSServer_Type())
xgs360026fIPv4CurrentDNSServer.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fIPv4CurrentDNSServer.setStatus(_A)
_Xgs360026fIPv6_ObjectIdentity=ObjectIdentity
xgs360026fIPv6=_Xgs360026fIPv6_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,4,2))
_Xgs360026fIPv6Configured_ObjectIdentity=ObjectIdentity
xgs360026fIPv6Configured=_Xgs360026fIPv6Configured_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,4,2,1))
class _Xgs360026fIpv6AutoConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fIpv6AutoConfiguration_Type.__name__=_B
_Xgs360026fIpv6AutoConfiguration_Object=MibScalar
xgs360026fIpv6AutoConfiguration=_Xgs360026fIpv6AutoConfiguration_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,2,1,1),_Xgs360026fIpv6AutoConfiguration_Type())
xgs360026fIpv6AutoConfiguration.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIpv6AutoConfiguration.setStatus(_A)
class _Xgs360026fIpv6Address_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Xgs360026fIpv6Address_Type.__name__=_G
_Xgs360026fIpv6Address_Object=MibScalar
xgs360026fIpv6Address=_Xgs360026fIpv6Address_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,2,1,2),_Xgs360026fIpv6Address_Type())
xgs360026fIpv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIpv6Address.setStatus(_A)
class _Xgs360026fIpv6Prefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Xgs360026fIpv6Prefix_Type.__name__=_B
_Xgs360026fIpv6Prefix_Object=MibScalar
xgs360026fIpv6Prefix=_Xgs360026fIpv6Prefix_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,2,1,3),_Xgs360026fIpv6Prefix_Type())
xgs360026fIpv6Prefix.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIpv6Prefix.setStatus(_A)
class _Xgs360026fIpv6Router_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Xgs360026fIpv6Router_Type.__name__=_G
_Xgs360026fIpv6Router_Object=MibScalar
xgs360026fIpv6Router=_Xgs360026fIpv6Router_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,2,1,4),_Xgs360026fIpv6Router_Type())
xgs360026fIpv6Router.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIpv6Router.setStatus(_A)
_Xgs360026fIPv6Current_ObjectIdentity=ObjectIdentity
xgs360026fIPv6Current=_Xgs360026fIPv6Current_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,4,2,2))
class _Xgs360026fIpv6CurrentAutoConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fIpv6CurrentAutoConfiguration_Type.__name__=_B
_Xgs360026fIpv6CurrentAutoConfiguration_Object=MibScalar
xgs360026fIpv6CurrentAutoConfiguration=_Xgs360026fIpv6CurrentAutoConfiguration_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,2,2,1),_Xgs360026fIpv6CurrentAutoConfiguration_Type())
xgs360026fIpv6CurrentAutoConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fIpv6CurrentAutoConfiguration.setStatus(_A)
class _Xgs360026fIpv6CurrentAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Xgs360026fIpv6CurrentAddress_Type.__name__=_G
_Xgs360026fIpv6CurrentAddress_Object=MibScalar
xgs360026fIpv6CurrentAddress=_Xgs360026fIpv6CurrentAddress_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,2,2,2),_Xgs360026fIpv6CurrentAddress_Type())
xgs360026fIpv6CurrentAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fIpv6CurrentAddress.setStatus(_A)
class _Xgs360026fIpv6CurrentLinkLocalAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Xgs360026fIpv6CurrentLinkLocalAddress_Type.__name__=_G
_Xgs360026fIpv6CurrentLinkLocalAddress_Object=MibScalar
xgs360026fIpv6CurrentLinkLocalAddress=_Xgs360026fIpv6CurrentLinkLocalAddress_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,2,2,3),_Xgs360026fIpv6CurrentLinkLocalAddress_Type())
xgs360026fIpv6CurrentLinkLocalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fIpv6CurrentLinkLocalAddress.setStatus(_A)
class _Xgs360026fIpv6CurrentPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Xgs360026fIpv6CurrentPrefix_Type.__name__=_B
_Xgs360026fIpv6CurrentPrefix_Object=MibScalar
xgs360026fIpv6CurrentPrefix=_Xgs360026fIpv6CurrentPrefix_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,2,2,4),_Xgs360026fIpv6CurrentPrefix_Type())
xgs360026fIpv6CurrentPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fIpv6CurrentPrefix.setStatus(_A)
class _Xgs360026fIpv6CurrentRouter_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Xgs360026fIpv6CurrentRouter_Type.__name__=_G
_Xgs360026fIpv6CurrentRouter_Object=MibScalar
xgs360026fIpv6CurrentRouter=_Xgs360026fIpv6CurrentRouter_Object((1,3,6,1,4,1,890,1,5,8,77,1,4,2,2,5),_Xgs360026fIpv6CurrentRouter_Type())
xgs360026fIpv6CurrentRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fIpv6CurrentRouter.setStatus(_A)
_Xgs360026fSyslog_ObjectIdentity=ObjectIdentity
xgs360026fSyslog=_Xgs360026fSyslog_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,5))
_Xgs360026fSyslogConf_ObjectIdentity=ObjectIdentity
xgs360026fSyslogConf=_Xgs360026fSyslogConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,5,1))
class _Xgs360026fServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fServerMode_Type.__name__=_B
_Xgs360026fServerMode_Object=MibScalar
xgs360026fServerMode=_Xgs360026fServerMode_Object((1,3,6,1,4,1,890,1,5,8,77,1,5,1,1),_Xgs360026fServerMode_Type())
xgs360026fServerMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fServerMode.setStatus(_A)
_Xgs360026fServerAddress1_Type=IpAddress
_Xgs360026fServerAddress1_Object=MibScalar
xgs360026fServerAddress1=_Xgs360026fServerAddress1_Object((1,3,6,1,4,1,890,1,5,8,77,1,5,1,2),_Xgs360026fServerAddress1_Type())
xgs360026fServerAddress1.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fServerAddress1.setStatus(_A)
_Xgs360026fServerAddress2_Type=IpAddress
_Xgs360026fServerAddress2_Object=MibScalar
xgs360026fServerAddress2=_Xgs360026fServerAddress2_Object((1,3,6,1,4,1,890,1,5,8,77,1,5,1,3),_Xgs360026fServerAddress2_Type())
xgs360026fServerAddress2.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fServerAddress2.setStatus(_A)
class _Xgs360026fSyslogLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fSyslogLevel_Type.__name__=_B
_Xgs360026fSyslogLevel_Object=MibScalar
xgs360026fSyslogLevel=_Xgs360026fSyslogLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,5,1,4),_Xgs360026fSyslogLevel_Type())
xgs360026fSyslogLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSyslogLevel.setStatus(_A)
_Xgs360026fSyslogDetailedInfo_ObjectIdentity=ObjectIdentity
xgs360026fSyslogDetailedInfo=_Xgs360026fSyslogDetailedInfo_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,5,2))
class _Xgs360026fSyslogDetailedInfoClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fSyslogDetailedInfoClear_Type.__name__=_B
_Xgs360026fSyslogDetailedInfoClear_Object=MibScalar
xgs360026fSyslogDetailedInfoClear=_Xgs360026fSyslogDetailedInfoClear_Object((1,3,6,1,4,1,890,1,5,8,77,1,5,2,1),_Xgs360026fSyslogDetailedInfoClear_Type())
xgs360026fSyslogDetailedInfoClear.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSyslogDetailedInfoClear.setStatus(_A)
_Xgs360026fSyslogDetailedInfoTable_Object=MibTable
xgs360026fSyslogDetailedInfoTable=_Xgs360026fSyslogDetailedInfoTable_Object((1,3,6,1,4,1,890,1,5,8,77,1,5,2,2))
if mibBuilder.loadTexts:xgs360026fSyslogDetailedInfoTable.setStatus(_A)
_Xgs360026fSyslogDetailedInfoEntry_Object=MibTableRow
xgs360026fSyslogDetailedInfoEntry=_Xgs360026fSyslogDetailedInfoEntry_Object((1,3,6,1,4,1,890,1,5,8,77,1,5,2,2,1))
xgs360026fSyslogDetailedInfoEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:xgs360026fSyslogDetailedInfoEntry.setStatus(_A)
class _Xgs360026fSyslogDetailedInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Xgs360026fSyslogDetailedInfoIndex_Type.__name__=_B
_Xgs360026fSyslogDetailedInfoIndex_Object=MibTableColumn
xgs360026fSyslogDetailedInfoIndex=_Xgs360026fSyslogDetailedInfoIndex_Object((1,3,6,1,4,1,890,1,5,8,77,1,5,2,2,1,1),_Xgs360026fSyslogDetailedInfoIndex_Type())
xgs360026fSyslogDetailedInfoIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fSyslogDetailedInfoIndex.setStatus(_A)
_Xgs360026fSyslogDetailedInfoLevel_Type=DisplayString
_Xgs360026fSyslogDetailedInfoLevel_Object=MibTableColumn
xgs360026fSyslogDetailedInfoLevel=_Xgs360026fSyslogDetailedInfoLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,5,2,2,1,2),_Xgs360026fSyslogDetailedInfoLevel_Type())
xgs360026fSyslogDetailedInfoLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSyslogDetailedInfoLevel.setStatus(_A)
class _Xgs360026fSyslogDetailedInfoTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_Xgs360026fSyslogDetailedInfoTime_Type.__name__=_G
_Xgs360026fSyslogDetailedInfoTime_Object=MibTableColumn
xgs360026fSyslogDetailedInfoTime=_Xgs360026fSyslogDetailedInfoTime_Object((1,3,6,1,4,1,890,1,5,8,77,1,5,2,2,1,3),_Xgs360026fSyslogDetailedInfoTime_Type())
xgs360026fSyslogDetailedInfoTime.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSyslogDetailedInfoTime.setStatus(_A)
_Xgs360026fSyslogDetailedInfoMessage_Type=DisplayString
_Xgs360026fSyslogDetailedInfoMessage_Object=MibTableColumn
xgs360026fSyslogDetailedInfoMessage=_Xgs360026fSyslogDetailedInfoMessage_Object((1,3,6,1,4,1,890,1,5,8,77,1,5,2,2,1,4),_Xgs360026fSyslogDetailedInfoMessage_Type())
xgs360026fSyslogDetailedInfoMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSyslogDetailedInfoMessage.setStatus(_A)
_Xgs360026fSnmp_ObjectIdentity=ObjectIdentity
xgs360026fSnmp=_Xgs360026fSnmp_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,6))
_Xgs360026fSnmpConf_ObjectIdentity=ObjectIdentity
xgs360026fSnmpConf=_Xgs360026fSnmpConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,1,6,1))
_Xgs360026fGetCommunity_Type=DisplayString
_Xgs360026fGetCommunity_Object=MibScalar
xgs360026fGetCommunity=_Xgs360026fGetCommunity_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,1),_Xgs360026fGetCommunity_Type())
xgs360026fGetCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fGetCommunity.setStatus(_A)
class _Xgs360026fSetCommunityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fSetCommunityMode_Type.__name__=_B
_Xgs360026fSetCommunityMode_Object=MibScalar
xgs360026fSetCommunityMode=_Xgs360026fSetCommunityMode_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,2),_Xgs360026fSetCommunityMode_Type())
xgs360026fSetCommunityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSetCommunityMode.setStatus(_A)
_Xgs360026fSetCommunity_Type=DisplayString
_Xgs360026fSetCommunity_Object=MibScalar
xgs360026fSetCommunity=_Xgs360026fSetCommunity_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,3),_Xgs360026fSetCommunity_Type())
xgs360026fSetCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSetCommunity.setStatus(_A)
_Xgs360026fTrapHostConfTable_Object=MibTable
xgs360026fTrapHostConfTable=_Xgs360026fTrapHostConfTable_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,4))
if mibBuilder.loadTexts:xgs360026fTrapHostConfTable.setStatus(_A)
_Xgs360026fTrapHostConfEntry_Object=MibTableRow
xgs360026fTrapHostConfEntry=_Xgs360026fTrapHostConfEntry_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,4,1))
xgs360026fTrapHostConfEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:xgs360026fTrapHostConfEntry.setStatus(_A)
class _Xgs360026fTrapHostConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Xgs360026fTrapHostConfIndex_Type.__name__=_B
_Xgs360026fTrapHostConfIndex_Object=MibTableColumn
xgs360026fTrapHostConfIndex=_Xgs360026fTrapHostConfIndex_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,4,1,1),_Xgs360026fTrapHostConfIndex_Type())
xgs360026fTrapHostConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fTrapHostConfIndex.setStatus(_A)
class _Xgs360026fTrapHostConfVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,3))
_Xgs360026fTrapHostConfVersion_Type.__name__=_B
_Xgs360026fTrapHostConfVersion_Object=MibTableColumn
xgs360026fTrapHostConfVersion=_Xgs360026fTrapHostConfVersion_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,4,1,2),_Xgs360026fTrapHostConfVersion_Type())
xgs360026fTrapHostConfVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapHostConfVersion.setStatus(_A)
class _Xgs360026fTrapHostConfIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,4),ValueRangeConstraint(6,6))
_Xgs360026fTrapHostConfIPType_Type.__name__=_B
_Xgs360026fTrapHostConfIPType_Object=MibTableColumn
xgs360026fTrapHostConfIPType=_Xgs360026fTrapHostConfIPType_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,4,1,3),_Xgs360026fTrapHostConfIPType_Type())
xgs360026fTrapHostConfIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapHostConfIPType.setStatus(_A)
_Xgs360026fTrapHostConfIP_Type=DisplayString
_Xgs360026fTrapHostConfIP_Object=MibTableColumn
xgs360026fTrapHostConfIP=_Xgs360026fTrapHostConfIP_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,4,1,4),_Xgs360026fTrapHostConfIP_Type())
xgs360026fTrapHostConfIP.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapHostConfIP.setStatus(_A)
class _Xgs360026fTrapHostConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Xgs360026fTrapHostConfPort_Type.__name__=_B
_Xgs360026fTrapHostConfPort_Object=MibTableColumn
xgs360026fTrapHostConfPort=_Xgs360026fTrapHostConfPort_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,4,1,5),_Xgs360026fTrapHostConfPort_Type())
xgs360026fTrapHostConfPort.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapHostConfPort.setStatus(_A)
class _Xgs360026fTrapHostConfCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Xgs360026fTrapHostConfCommunity_Type.__name__=_G
_Xgs360026fTrapHostConfCommunity_Object=MibTableColumn
xgs360026fTrapHostConfCommunity=_Xgs360026fTrapHostConfCommunity_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,4,1,6),_Xgs360026fTrapHostConfCommunity_Type())
xgs360026fTrapHostConfCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapHostConfCommunity.setStatus(_A)
class _Xgs360026fTrapHostConfSeverityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapHostConfSeverityLevel_Type.__name__=_B
_Xgs360026fTrapHostConfSeverityLevel_Object=MibTableColumn
xgs360026fTrapHostConfSeverityLevel=_Xgs360026fTrapHostConfSeverityLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,4,1,7),_Xgs360026fTrapHostConfSeverityLevel_Type())
xgs360026fTrapHostConfSeverityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapHostConfSeverityLevel.setStatus(_A)
class _Xgs360026fTrapHostConfSecurityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Xgs360026fTrapHostConfSecurityLevel_Type.__name__=_B
_Xgs360026fTrapHostConfSecurityLevel_Object=MibTableColumn
xgs360026fTrapHostConfSecurityLevel=_Xgs360026fTrapHostConfSecurityLevel_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,4,1,8),_Xgs360026fTrapHostConfSecurityLevel_Type())
xgs360026fTrapHostConfSecurityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapHostConfSecurityLevel.setStatus(_A)
class _Xgs360026fTrapHostConfAuthPtc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Xgs360026fTrapHostConfAuthPtc_Type.__name__=_B
_Xgs360026fTrapHostConfAuthPtc_Object=MibTableColumn
xgs360026fTrapHostConfAuthPtc=_Xgs360026fTrapHostConfAuthPtc_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,4,1,9),_Xgs360026fTrapHostConfAuthPtc_Type())
xgs360026fTrapHostConfAuthPtc.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapHostConfAuthPtc.setStatus(_A)
_Xgs360026fTrapHostConfAuthPassword_Type=DisplayString
_Xgs360026fTrapHostConfAuthPassword_Object=MibTableColumn
xgs360026fTrapHostConfAuthPassword=_Xgs360026fTrapHostConfAuthPassword_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,4,1,10),_Xgs360026fTrapHostConfAuthPassword_Type())
xgs360026fTrapHostConfAuthPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapHostConfAuthPassword.setStatus(_A)
class _Xgs360026fTrapHostConfPrivPtc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Xgs360026fTrapHostConfPrivPtc_Type.__name__=_B
_Xgs360026fTrapHostConfPrivPtc_Object=MibTableColumn
xgs360026fTrapHostConfPrivPtc=_Xgs360026fTrapHostConfPrivPtc_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,4,1,11),_Xgs360026fTrapHostConfPrivPtc_Type())
xgs360026fTrapHostConfPrivPtc.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapHostConfPrivPtc.setStatus(_A)
_Xgs360026fTrapHostConfPrivPassword_Type=DisplayString
_Xgs360026fTrapHostConfPrivPassword_Object=MibTableColumn
xgs360026fTrapHostConfPrivPassword=_Xgs360026fTrapHostConfPrivPassword_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,4,1,12),_Xgs360026fTrapHostConfPrivPassword_Type())
xgs360026fTrapHostConfPrivPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapHostConfPrivPassword.setStatus(_A)
class _Xgs360026fTrapHostConfCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fTrapHostConfCurrentMode_Type.__name__=_B
_Xgs360026fTrapHostConfCurrentMode_Object=MibTableColumn
xgs360026fTrapHostConfCurrentMode=_Xgs360026fTrapHostConfCurrentMode_Object((1,3,6,1,4,1,890,1,5,8,77,1,6,1,4,1,13),_Xgs360026fTrapHostConfCurrentMode_Type())
xgs360026fTrapHostConfCurrentMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapHostConfCurrentMode.setStatus(_A)
_Xgs360026fConfiguration_ObjectIdentity=ObjectIdentity
xgs360026fConfiguration=_Xgs360026fConfiguration_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2))
_Xgs360026fPort_ObjectIdentity=ObjectIdentity
xgs360026fPort=_Xgs360026fPort_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,1))
_Xgs360026fPortConfigurationTable_Object=MibTable
xgs360026fPortConfigurationTable=_Xgs360026fPortConfigurationTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,1))
if mibBuilder.loadTexts:xgs360026fPortConfigurationTable.setStatus(_A)
_Xgs360026fPortConfigurationEntry_Object=MibTableRow
xgs360026fPortConfigurationEntry=_Xgs360026fPortConfigurationEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,1,1))
xgs360026fPortConfigurationEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:xgs360026fPortConfigurationEntry.setStatus(_A)
class _Xgs360026fPortConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fPortConfPort_Type.__name__=_B
_Xgs360026fPortConfPort_Object=MibTableColumn
xgs360026fPortConfPort=_Xgs360026fPortConfPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,1,1,1),_Xgs360026fPortConfPort_Type())
xgs360026fPortConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fPortConfPort.setStatus(_A)
class _Xgs360026fPortConfPortMedia_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_Xgs360026fPortConfPortMedia_Type.__name__=_G
_Xgs360026fPortConfPortMedia_Object=MibTableColumn
xgs360026fPortConfPortMedia=_Xgs360026fPortConfPortMedia_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,1,1,2),_Xgs360026fPortConfPortMedia_Type())
xgs360026fPortConfPortMedia.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortConfPortMedia.setStatus(_A)
class _Xgs360026fPortConfLink_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,4))
_Xgs360026fPortConfLink_Type.__name__=_G
_Xgs360026fPortConfLink_Object=MibTableColumn
xgs360026fPortConfLink=_Xgs360026fPortConfLink_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,1,1,3),_Xgs360026fPortConfLink_Type())
xgs360026fPortConfLink.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortConfLink.setStatus(_A)
class _Xgs360026fPortConfCurrentSpeed_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,12))
_Xgs360026fPortConfCurrentSpeed_Type.__name__=_G
_Xgs360026fPortConfCurrentSpeed_Object=MibTableColumn
xgs360026fPortConfCurrentSpeed=_Xgs360026fPortConfCurrentSpeed_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,1,1,4),_Xgs360026fPortConfCurrentSpeed_Type())
xgs360026fPortConfCurrentSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortConfCurrentSpeed.setStatus(_A)
class _Xgs360026fPortConfSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_Xgs360026fPortConfSpeed_Type.__name__=_B
_Xgs360026fPortConfSpeed_Object=MibTableColumn
xgs360026fPortConfSpeed=_Xgs360026fPortConfSpeed_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,1,1,5),_Xgs360026fPortConfSpeed_Type())
xgs360026fPortConfSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortConfSpeed.setStatus(_A)
class _Xgs360026fPortConfCurrentFlowControlRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fPortConfCurrentFlowControlRx_Type.__name__=_B
_Xgs360026fPortConfCurrentFlowControlRx_Object=MibTableColumn
xgs360026fPortConfCurrentFlowControlRx=_Xgs360026fPortConfCurrentFlowControlRx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,1,1,6),_Xgs360026fPortConfCurrentFlowControlRx_Type())
xgs360026fPortConfCurrentFlowControlRx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortConfCurrentFlowControlRx.setStatus(_A)
class _Xgs360026fPortConfCurrentFlowControlTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fPortConfCurrentFlowControlTx_Type.__name__=_B
_Xgs360026fPortConfCurrentFlowControlTx_Object=MibTableColumn
xgs360026fPortConfCurrentFlowControlTx=_Xgs360026fPortConfCurrentFlowControlTx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,1,1,7),_Xgs360026fPortConfCurrentFlowControlTx_Type())
xgs360026fPortConfCurrentFlowControlTx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortConfCurrentFlowControlTx.setStatus(_A)
class _Xgs360026fPortConfFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fPortConfFlowControl_Type.__name__=_B
_Xgs360026fPortConfFlowControl_Object=MibTableColumn
xgs360026fPortConfFlowControl=_Xgs360026fPortConfFlowControl_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,1,1,8),_Xgs360026fPortConfFlowControl_Type())
xgs360026fPortConfFlowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortConfFlowControl.setStatus(_A)
class _Xgs360026fPortConfMaxFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1518,9600))
_Xgs360026fPortConfMaxFrameSize_Type.__name__=_B
_Xgs360026fPortConfMaxFrameSize_Object=MibTableColumn
xgs360026fPortConfMaxFrameSize=_Xgs360026fPortConfMaxFrameSize_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,1,1,9),_Xgs360026fPortConfMaxFrameSize_Type())
xgs360026fPortConfMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortConfMaxFrameSize.setStatus(_A)
class _Xgs360026fPortConfExcessiveCollisionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fPortConfExcessiveCollisionMode_Type.__name__=_B
_Xgs360026fPortConfExcessiveCollisionMode_Object=MibTableColumn
xgs360026fPortConfExcessiveCollisionMode=_Xgs360026fPortConfExcessiveCollisionMode_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,1,1,10),_Xgs360026fPortConfExcessiveCollisionMode_Type())
xgs360026fPortConfExcessiveCollisionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortConfExcessiveCollisionMode.setStatus(_A)
class _Xgs360026fPortConfPowerControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360026fPortConfPowerControl_Type.__name__=_B
_Xgs360026fPortConfPowerControl_Object=MibTableColumn
xgs360026fPortConfPowerControl=_Xgs360026fPortConfPowerControl_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,1,1,11),_Xgs360026fPortConfPowerControl_Type())
xgs360026fPortConfPowerControl.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortConfPowerControl.setStatus(_A)
_Xgs360026fPortConfDescription_Type=DisplayString
_Xgs360026fPortConfDescription_Object=MibTableColumn
xgs360026fPortConfDescription=_Xgs360026fPortConfDescription_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,1,1,12),_Xgs360026fPortConfDescription_Type())
xgs360026fPortConfDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortConfDescription.setStatus(_A)
_Xgs360026fPortTrafficStatisticsTable_Object=MibTable
xgs360026fPortTrafficStatisticsTable=_Xgs360026fPortTrafficStatisticsTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2))
if mibBuilder.loadTexts:xgs360026fPortTrafficStatisticsTable.setStatus(_A)
_Xgs360026fPortTrafficStatisticsEntry_Object=MibTableRow
xgs360026fPortTrafficStatisticsEntry=_Xgs360026fPortTrafficStatisticsEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1))
xgs360026fPortTrafficStatisticsEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:xgs360026fPortTrafficStatisticsEntry.setStatus(_A)
class _Xgs360026fPortTrafficStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fPortTrafficStatisticsPort_Type.__name__=_B
_Xgs360026fPortTrafficStatisticsPort_Object=MibTableColumn
xgs360026fPortTrafficStatisticsPort=_Xgs360026fPortTrafficStatisticsPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,1),_Xgs360026fPortTrafficStatisticsPort_Type())
xgs360026fPortTrafficStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fPortTrafficStatisticsPort.setStatus(_A)
class _Xgs360026fPortTrafficStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fPortTrafficStatisticsClear_Type.__name__=_B
_Xgs360026fPortTrafficStatisticsClear_Object=MibTableColumn
xgs360026fPortTrafficStatisticsClear=_Xgs360026fPortTrafficStatisticsClear_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,2),_Xgs360026fPortTrafficStatisticsClear_Type())
xgs360026fPortTrafficStatisticsClear.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortTrafficStatisticsClear.setStatus(_A)
_Xgs360026fPortTrafficRxPackets_Type=Counter64
_Xgs360026fPortTrafficRxPackets_Object=MibTableColumn
xgs360026fPortTrafficRxPackets=_Xgs360026fPortTrafficRxPackets_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,3),_Xgs360026fPortTrafficRxPackets_Type())
xgs360026fPortTrafficRxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxPackets.setStatus(_A)
_Xgs360026fPortTrafficRxOctets_Type=Counter64
_Xgs360026fPortTrafficRxOctets_Object=MibTableColumn
xgs360026fPortTrafficRxOctets=_Xgs360026fPortTrafficRxOctets_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,4),_Xgs360026fPortTrafficRxOctets_Type())
xgs360026fPortTrafficRxOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxOctets.setStatus(_A)
_Xgs360026fPortTrafficRxUnicast_Type=Counter64
_Xgs360026fPortTrafficRxUnicast_Object=MibTableColumn
xgs360026fPortTrafficRxUnicast=_Xgs360026fPortTrafficRxUnicast_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,5),_Xgs360026fPortTrafficRxUnicast_Type())
xgs360026fPortTrafficRxUnicast.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxUnicast.setStatus(_A)
_Xgs360026fPortTrafficRxMulticast_Type=Counter64
_Xgs360026fPortTrafficRxMulticast_Object=MibTableColumn
xgs360026fPortTrafficRxMulticast=_Xgs360026fPortTrafficRxMulticast_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,6),_Xgs360026fPortTrafficRxMulticast_Type())
xgs360026fPortTrafficRxMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxMulticast.setStatus(_A)
_Xgs360026fPortTrafficRxBroadcast_Type=Counter64
_Xgs360026fPortTrafficRxBroadcast_Object=MibTableColumn
xgs360026fPortTrafficRxBroadcast=_Xgs360026fPortTrafficRxBroadcast_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,7),_Xgs360026fPortTrafficRxBroadcast_Type())
xgs360026fPortTrafficRxBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxBroadcast.setStatus(_A)
_Xgs360026fPortTrafficRxPause_Type=Counter64
_Xgs360026fPortTrafficRxPause_Object=MibTableColumn
xgs360026fPortTrafficRxPause=_Xgs360026fPortTrafficRxPause_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,8),_Xgs360026fPortTrafficRxPause_Type())
xgs360026fPortTrafficRxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxPause.setStatus(_A)
_Xgs360026fPortTrafficRx64Bytes_Type=Counter64
_Xgs360026fPortTrafficRx64Bytes_Object=MibTableColumn
xgs360026fPortTrafficRx64Bytes=_Xgs360026fPortTrafficRx64Bytes_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,9),_Xgs360026fPortTrafficRx64Bytes_Type())
xgs360026fPortTrafficRx64Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRx64Bytes.setStatus(_A)
_Xgs360026fPortTrafficRx65to127Bytes_Type=Counter64
_Xgs360026fPortTrafficRx65to127Bytes_Object=MibTableColumn
xgs360026fPortTrafficRx65to127Bytes=_Xgs360026fPortTrafficRx65to127Bytes_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,10),_Xgs360026fPortTrafficRx65to127Bytes_Type())
xgs360026fPortTrafficRx65to127Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRx65to127Bytes.setStatus(_A)
_Xgs360026fPortTrafficRx128to255Bytes_Type=Counter64
_Xgs360026fPortTrafficRx128to255Bytes_Object=MibTableColumn
xgs360026fPortTrafficRx128to255Bytes=_Xgs360026fPortTrafficRx128to255Bytes_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,11),_Xgs360026fPortTrafficRx128to255Bytes_Type())
xgs360026fPortTrafficRx128to255Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRx128to255Bytes.setStatus(_A)
_Xgs360026fPortTrafficRx256to511Bytes_Type=Counter64
_Xgs360026fPortTrafficRx256to511Bytes_Object=MibTableColumn
xgs360026fPortTrafficRx256to511Bytes=_Xgs360026fPortTrafficRx256to511Bytes_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,12),_Xgs360026fPortTrafficRx256to511Bytes_Type())
xgs360026fPortTrafficRx256to511Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRx256to511Bytes.setStatus(_A)
_Xgs360026fPortTrafficRx512to1023Bytes_Type=Counter64
_Xgs360026fPortTrafficRx512to1023Bytes_Object=MibTableColumn
xgs360026fPortTrafficRx512to1023Bytes=_Xgs360026fPortTrafficRx512to1023Bytes_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,13),_Xgs360026fPortTrafficRx512to1023Bytes_Type())
xgs360026fPortTrafficRx512to1023Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRx512to1023Bytes.setStatus(_A)
_Xgs360026fPortTrafficRx1024to1526Bytes_Type=Counter64
_Xgs360026fPortTrafficRx1024to1526Bytes_Object=MibTableColumn
xgs360026fPortTrafficRx1024to1526Bytes=_Xgs360026fPortTrafficRx1024to1526Bytes_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,14),_Xgs360026fPortTrafficRx1024to1526Bytes_Type())
xgs360026fPortTrafficRx1024to1526Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRx1024to1526Bytes.setStatus(_A)
_Xgs360026fPortTrafficRxExceecd1527Bytes_Type=Counter64
_Xgs360026fPortTrafficRxExceecd1527Bytes_Object=MibTableColumn
xgs360026fPortTrafficRxExceecd1527Bytes=_Xgs360026fPortTrafficRxExceecd1527Bytes_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,15),_Xgs360026fPortTrafficRxExceecd1527Bytes_Type())
xgs360026fPortTrafficRxExceecd1527Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxExceecd1527Bytes.setStatus(_A)
_Xgs360026fPortTrafficRxQ0_Type=Counter64
_Xgs360026fPortTrafficRxQ0_Object=MibTableColumn
xgs360026fPortTrafficRxQ0=_Xgs360026fPortTrafficRxQ0_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,16),_Xgs360026fPortTrafficRxQ0_Type())
xgs360026fPortTrafficRxQ0.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxQ0.setStatus(_A)
_Xgs360026fPortTrafficRxQ1_Type=Counter64
_Xgs360026fPortTrafficRxQ1_Object=MibTableColumn
xgs360026fPortTrafficRxQ1=_Xgs360026fPortTrafficRxQ1_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,17),_Xgs360026fPortTrafficRxQ1_Type())
xgs360026fPortTrafficRxQ1.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxQ1.setStatus(_A)
_Xgs360026fPortTrafficRxQ2_Type=Counter64
_Xgs360026fPortTrafficRxQ2_Object=MibTableColumn
xgs360026fPortTrafficRxQ2=_Xgs360026fPortTrafficRxQ2_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,18),_Xgs360026fPortTrafficRxQ2_Type())
xgs360026fPortTrafficRxQ2.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxQ2.setStatus(_A)
_Xgs360026fPortTrafficRxQ3_Type=Counter64
_Xgs360026fPortTrafficRxQ3_Object=MibTableColumn
xgs360026fPortTrafficRxQ3=_Xgs360026fPortTrafficRxQ3_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,19),_Xgs360026fPortTrafficRxQ3_Type())
xgs360026fPortTrafficRxQ3.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxQ3.setStatus(_A)
_Xgs360026fPortTrafficRxQ4_Type=Counter64
_Xgs360026fPortTrafficRxQ4_Object=MibTableColumn
xgs360026fPortTrafficRxQ4=_Xgs360026fPortTrafficRxQ4_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,20),_Xgs360026fPortTrafficRxQ4_Type())
xgs360026fPortTrafficRxQ4.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxQ4.setStatus(_A)
_Xgs360026fPortTrafficRxQ5_Type=Counter64
_Xgs360026fPortTrafficRxQ5_Object=MibTableColumn
xgs360026fPortTrafficRxQ5=_Xgs360026fPortTrafficRxQ5_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,21),_Xgs360026fPortTrafficRxQ5_Type())
xgs360026fPortTrafficRxQ5.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxQ5.setStatus(_A)
_Xgs360026fPortTrafficRxQ6_Type=Counter64
_Xgs360026fPortTrafficRxQ6_Object=MibTableColumn
xgs360026fPortTrafficRxQ6=_Xgs360026fPortTrafficRxQ6_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,22),_Xgs360026fPortTrafficRxQ6_Type())
xgs360026fPortTrafficRxQ6.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxQ6.setStatus(_A)
_Xgs360026fPortTrafficRxQ7_Type=Counter64
_Xgs360026fPortTrafficRxQ7_Object=MibTableColumn
xgs360026fPortTrafficRxQ7=_Xgs360026fPortTrafficRxQ7_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,23),_Xgs360026fPortTrafficRxQ7_Type())
xgs360026fPortTrafficRxQ7.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxQ7.setStatus(_A)
_Xgs360026fPortTrafficRxDrops_Type=Counter64
_Xgs360026fPortTrafficRxDrops_Object=MibTableColumn
xgs360026fPortTrafficRxDrops=_Xgs360026fPortTrafficRxDrops_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,24),_Xgs360026fPortTrafficRxDrops_Type())
xgs360026fPortTrafficRxDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxDrops.setStatus(_A)
_Xgs360026fPortTrafficRxCRCorAlignment_Type=Counter64
_Xgs360026fPortTrafficRxCRCorAlignment_Object=MibTableColumn
xgs360026fPortTrafficRxCRCorAlignment=_Xgs360026fPortTrafficRxCRCorAlignment_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,25),_Xgs360026fPortTrafficRxCRCorAlignment_Type())
xgs360026fPortTrafficRxCRCorAlignment.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxCRCorAlignment.setStatus(_A)
_Xgs360026fPortTrafficRxUndersize_Type=Counter64
_Xgs360026fPortTrafficRxUndersize_Object=MibTableColumn
xgs360026fPortTrafficRxUndersize=_Xgs360026fPortTrafficRxUndersize_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,26),_Xgs360026fPortTrafficRxUndersize_Type())
xgs360026fPortTrafficRxUndersize.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxUndersize.setStatus(_A)
_Xgs360026fPortTrafficRxOversize_Type=Counter64
_Xgs360026fPortTrafficRxOversize_Object=MibTableColumn
xgs360026fPortTrafficRxOversize=_Xgs360026fPortTrafficRxOversize_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,27),_Xgs360026fPortTrafficRxOversize_Type())
xgs360026fPortTrafficRxOversize.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxOversize.setStatus(_A)
_Xgs360026fPortTrafficRxFragments_Type=Counter64
_Xgs360026fPortTrafficRxFragments_Object=MibTableColumn
xgs360026fPortTrafficRxFragments=_Xgs360026fPortTrafficRxFragments_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,28),_Xgs360026fPortTrafficRxFragments_Type())
xgs360026fPortTrafficRxFragments.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxFragments.setStatus(_A)
_Xgs360026fPortTrafficRxJabber_Type=Counter64
_Xgs360026fPortTrafficRxJabber_Object=MibTableColumn
xgs360026fPortTrafficRxJabber=_Xgs360026fPortTrafficRxJabber_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,29),_Xgs360026fPortTrafficRxJabber_Type())
xgs360026fPortTrafficRxJabber.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxJabber.setStatus(_A)
_Xgs360026fPortTrafficRxFiltered_Type=Counter64
_Xgs360026fPortTrafficRxFiltered_Object=MibTableColumn
xgs360026fPortTrafficRxFiltered=_Xgs360026fPortTrafficRxFiltered_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,30),_Xgs360026fPortTrafficRxFiltered_Type())
xgs360026fPortTrafficRxFiltered.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficRxFiltered.setStatus(_A)
_Xgs360026fPortTrafficTxPackets_Type=Counter64
_Xgs360026fPortTrafficTxPackets_Object=MibTableColumn
xgs360026fPortTrafficTxPackets=_Xgs360026fPortTrafficTxPackets_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,31),_Xgs360026fPortTrafficTxPackets_Type())
xgs360026fPortTrafficTxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxPackets.setStatus(_A)
_Xgs360026fPortTrafficTxOctets_Type=Counter64
_Xgs360026fPortTrafficTxOctets_Object=MibTableColumn
xgs360026fPortTrafficTxOctets=_Xgs360026fPortTrafficTxOctets_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,32),_Xgs360026fPortTrafficTxOctets_Type())
xgs360026fPortTrafficTxOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxOctets.setStatus(_A)
_Xgs360026fPortTrafficTxUnicast_Type=Counter64
_Xgs360026fPortTrafficTxUnicast_Object=MibTableColumn
xgs360026fPortTrafficTxUnicast=_Xgs360026fPortTrafficTxUnicast_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,33),_Xgs360026fPortTrafficTxUnicast_Type())
xgs360026fPortTrafficTxUnicast.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxUnicast.setStatus(_A)
_Xgs360026fPortTrafficTxMulticast_Type=Counter64
_Xgs360026fPortTrafficTxMulticast_Object=MibTableColumn
xgs360026fPortTrafficTxMulticast=_Xgs360026fPortTrafficTxMulticast_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,34),_Xgs360026fPortTrafficTxMulticast_Type())
xgs360026fPortTrafficTxMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxMulticast.setStatus(_A)
_Xgs360026fPortTrafficTxBroadcast_Type=Counter64
_Xgs360026fPortTrafficTxBroadcast_Object=MibTableColumn
xgs360026fPortTrafficTxBroadcast=_Xgs360026fPortTrafficTxBroadcast_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,35),_Xgs360026fPortTrafficTxBroadcast_Type())
xgs360026fPortTrafficTxBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxBroadcast.setStatus(_A)
_Xgs360026fPortTrafficTxPause_Type=Counter64
_Xgs360026fPortTrafficTxPause_Object=MibTableColumn
xgs360026fPortTrafficTxPause=_Xgs360026fPortTrafficTxPause_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,36),_Xgs360026fPortTrafficTxPause_Type())
xgs360026fPortTrafficTxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxPause.setStatus(_A)
_Xgs360026fPortTrafficTx64Bytes_Type=Counter64
_Xgs360026fPortTrafficTx64Bytes_Object=MibTableColumn
xgs360026fPortTrafficTx64Bytes=_Xgs360026fPortTrafficTx64Bytes_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,37),_Xgs360026fPortTrafficTx64Bytes_Type())
xgs360026fPortTrafficTx64Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTx64Bytes.setStatus(_A)
_Xgs360026fPortTrafficTx65to127Bytes_Type=Counter64
_Xgs360026fPortTrafficTx65to127Bytes_Object=MibTableColumn
xgs360026fPortTrafficTx65to127Bytes=_Xgs360026fPortTrafficTx65to127Bytes_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,38),_Xgs360026fPortTrafficTx65to127Bytes_Type())
xgs360026fPortTrafficTx65to127Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTx65to127Bytes.setStatus(_A)
_Xgs360026fPortTrafficTx128to255Bytes_Type=Counter64
_Xgs360026fPortTrafficTx128to255Bytes_Object=MibTableColumn
xgs360026fPortTrafficTx128to255Bytes=_Xgs360026fPortTrafficTx128to255Bytes_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,39),_Xgs360026fPortTrafficTx128to255Bytes_Type())
xgs360026fPortTrafficTx128to255Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTx128to255Bytes.setStatus(_A)
_Xgs360026fPortTrafficTx256to511Bytes_Type=Counter64
_Xgs360026fPortTrafficTx256to511Bytes_Object=MibTableColumn
xgs360026fPortTrafficTx256to511Bytes=_Xgs360026fPortTrafficTx256to511Bytes_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,40),_Xgs360026fPortTrafficTx256to511Bytes_Type())
xgs360026fPortTrafficTx256to511Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTx256to511Bytes.setStatus(_A)
_Xgs360026fPortTrafficTx512to1023Bytes_Type=Counter64
_Xgs360026fPortTrafficTx512to1023Bytes_Object=MibTableColumn
xgs360026fPortTrafficTx512to1023Bytes=_Xgs360026fPortTrafficTx512to1023Bytes_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,41),_Xgs360026fPortTrafficTx512to1023Bytes_Type())
xgs360026fPortTrafficTx512to1023Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTx512to1023Bytes.setStatus(_A)
_Xgs360026fPortTrafficTx1024to1526Bytes_Type=Counter64
_Xgs360026fPortTrafficTx1024to1526Bytes_Object=MibTableColumn
xgs360026fPortTrafficTx1024to1526Bytes=_Xgs360026fPortTrafficTx1024to1526Bytes_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,42),_Xgs360026fPortTrafficTx1024to1526Bytes_Type())
xgs360026fPortTrafficTx1024to1526Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTx1024to1526Bytes.setStatus(_A)
_Xgs360026fPortTrafficTxExceecd1527Bytes_Type=Counter64
_Xgs360026fPortTrafficTxExceecd1527Bytes_Object=MibTableColumn
xgs360026fPortTrafficTxExceecd1527Bytes=_Xgs360026fPortTrafficTxExceecd1527Bytes_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,43),_Xgs360026fPortTrafficTxExceecd1527Bytes_Type())
xgs360026fPortTrafficTxExceecd1527Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxExceecd1527Bytes.setStatus(_A)
_Xgs360026fPortTrafficTxQ0_Type=Counter64
_Xgs360026fPortTrafficTxQ0_Object=MibTableColumn
xgs360026fPortTrafficTxQ0=_Xgs360026fPortTrafficTxQ0_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,44),_Xgs360026fPortTrafficTxQ0_Type())
xgs360026fPortTrafficTxQ0.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxQ0.setStatus(_A)
_Xgs360026fPortTrafficTxQ1_Type=Counter64
_Xgs360026fPortTrafficTxQ1_Object=MibTableColumn
xgs360026fPortTrafficTxQ1=_Xgs360026fPortTrafficTxQ1_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,45),_Xgs360026fPortTrafficTxQ1_Type())
xgs360026fPortTrafficTxQ1.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxQ1.setStatus(_A)
_Xgs360026fPortTrafficTxQ2_Type=Counter64
_Xgs360026fPortTrafficTxQ2_Object=MibTableColumn
xgs360026fPortTrafficTxQ2=_Xgs360026fPortTrafficTxQ2_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,46),_Xgs360026fPortTrafficTxQ2_Type())
xgs360026fPortTrafficTxQ2.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxQ2.setStatus(_A)
_Xgs360026fPortTrafficTxQ3_Type=Counter64
_Xgs360026fPortTrafficTxQ3_Object=MibTableColumn
xgs360026fPortTrafficTxQ3=_Xgs360026fPortTrafficTxQ3_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,47),_Xgs360026fPortTrafficTxQ3_Type())
xgs360026fPortTrafficTxQ3.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxQ3.setStatus(_A)
_Xgs360026fPortTrafficTxQ4_Type=Counter64
_Xgs360026fPortTrafficTxQ4_Object=MibTableColumn
xgs360026fPortTrafficTxQ4=_Xgs360026fPortTrafficTxQ4_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,48),_Xgs360026fPortTrafficTxQ4_Type())
xgs360026fPortTrafficTxQ4.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxQ4.setStatus(_A)
_Xgs360026fPortTrafficTxQ5_Type=Counter64
_Xgs360026fPortTrafficTxQ5_Object=MibTableColumn
xgs360026fPortTrafficTxQ5=_Xgs360026fPortTrafficTxQ5_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,49),_Xgs360026fPortTrafficTxQ5_Type())
xgs360026fPortTrafficTxQ5.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxQ5.setStatus(_A)
_Xgs360026fPortTrafficTxQ6_Type=Counter64
_Xgs360026fPortTrafficTxQ6_Object=MibTableColumn
xgs360026fPortTrafficTxQ6=_Xgs360026fPortTrafficTxQ6_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,50),_Xgs360026fPortTrafficTxQ6_Type())
xgs360026fPortTrafficTxQ6.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxQ6.setStatus(_A)
_Xgs360026fPortTrafficTxQ7_Type=Counter64
_Xgs360026fPortTrafficTxQ7_Object=MibTableColumn
xgs360026fPortTrafficTxQ7=_Xgs360026fPortTrafficTxQ7_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,51),_Xgs360026fPortTrafficTxQ7_Type())
xgs360026fPortTrafficTxQ7.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxQ7.setStatus(_A)
_Xgs360026fPortTrafficTxDrops_Type=Counter64
_Xgs360026fPortTrafficTxDrops_Object=MibTableColumn
xgs360026fPortTrafficTxDrops=_Xgs360026fPortTrafficTxDrops_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,52),_Xgs360026fPortTrafficTxDrops_Type())
xgs360026fPortTrafficTxDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxDrops.setStatus(_A)
_Xgs360026fPortTrafficTxLateOrExcColl_Type=Counter64
_Xgs360026fPortTrafficTxLateOrExcColl_Object=MibTableColumn
xgs360026fPortTrafficTxLateOrExcColl=_Xgs360026fPortTrafficTxLateOrExcColl_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,2,1,53),_Xgs360026fPortTrafficTxLateOrExcColl_Type())
xgs360026fPortTrafficTxLateOrExcColl.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortTrafficTxLateOrExcColl.setStatus(_A)
_Xgs360026fPortQoSStatistics_ObjectIdentity=ObjectIdentity
xgs360026fPortQoSStatistics=_Xgs360026fPortQoSStatistics_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,1,3))
class _Xgs360026fPortQoSStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fPortQoSStatisticsClear_Type.__name__=_B
_Xgs360026fPortQoSStatisticsClear_Object=MibScalar
xgs360026fPortQoSStatisticsClear=_Xgs360026fPortQoSStatisticsClear_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,1),_Xgs360026fPortQoSStatisticsClear_Type())
xgs360026fPortQoSStatisticsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSStatisticsClear.setStatus(_A)
_Xgs360026fPortQoSStatisticsTable_Object=MibTable
xgs360026fPortQoSStatisticsTable=_Xgs360026fPortQoSStatisticsTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2))
if mibBuilder.loadTexts:xgs360026fPortQoSStatisticsTable.setStatus(_A)
_Xgs360026fPortQoSStatisticsEntry_Object=MibTableRow
xgs360026fPortQoSStatisticsEntry=_Xgs360026fPortQoSStatisticsEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1))
xgs360026fPortQoSStatisticsEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:xgs360026fPortQoSStatisticsEntry.setStatus(_A)
class _Xgs360026fPortQoSStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fPortQoSStatisticsPort_Type.__name__=_B
_Xgs360026fPortQoSStatisticsPort_Object=MibTableColumn
xgs360026fPortQoSStatisticsPort=_Xgs360026fPortQoSStatisticsPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,1),_Xgs360026fPortQoSStatisticsPort_Type())
xgs360026fPortQoSStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fPortQoSStatisticsPort.setStatus(_A)
_Xgs360026fPortQoSQ0Rx_Type=Counter64
_Xgs360026fPortQoSQ0Rx_Object=MibTableColumn
xgs360026fPortQoSQ0Rx=_Xgs360026fPortQoSQ0Rx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,2),_Xgs360026fPortQoSQ0Rx_Type())
xgs360026fPortQoSQ0Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ0Rx.setStatus(_A)
_Xgs360026fPortQoSQ0Tx_Type=Counter64
_Xgs360026fPortQoSQ0Tx_Object=MibTableColumn
xgs360026fPortQoSQ0Tx=_Xgs360026fPortQoSQ0Tx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,3),_Xgs360026fPortQoSQ0Tx_Type())
xgs360026fPortQoSQ0Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ0Tx.setStatus(_A)
_Xgs360026fPortQoSQ1Rx_Type=Counter64
_Xgs360026fPortQoSQ1Rx_Object=MibTableColumn
xgs360026fPortQoSQ1Rx=_Xgs360026fPortQoSQ1Rx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,4),_Xgs360026fPortQoSQ1Rx_Type())
xgs360026fPortQoSQ1Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ1Rx.setStatus(_A)
_Xgs360026fPortQoSQ1Tx_Type=Counter64
_Xgs360026fPortQoSQ1Tx_Object=MibTableColumn
xgs360026fPortQoSQ1Tx=_Xgs360026fPortQoSQ1Tx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,5),_Xgs360026fPortQoSQ1Tx_Type())
xgs360026fPortQoSQ1Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ1Tx.setStatus(_A)
_Xgs360026fPortQoSQ2Rx_Type=Counter64
_Xgs360026fPortQoSQ2Rx_Object=MibTableColumn
xgs360026fPortQoSQ2Rx=_Xgs360026fPortQoSQ2Rx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,6),_Xgs360026fPortQoSQ2Rx_Type())
xgs360026fPortQoSQ2Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ2Rx.setStatus(_A)
_Xgs360026fPortQoSQ2Tx_Type=Counter64
_Xgs360026fPortQoSQ2Tx_Object=MibTableColumn
xgs360026fPortQoSQ2Tx=_Xgs360026fPortQoSQ2Tx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,7),_Xgs360026fPortQoSQ2Tx_Type())
xgs360026fPortQoSQ2Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ2Tx.setStatus(_A)
_Xgs360026fPortQoSQ3Rx_Type=Counter64
_Xgs360026fPortQoSQ3Rx_Object=MibTableColumn
xgs360026fPortQoSQ3Rx=_Xgs360026fPortQoSQ3Rx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,8),_Xgs360026fPortQoSQ3Rx_Type())
xgs360026fPortQoSQ3Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ3Rx.setStatus(_A)
_Xgs360026fPortQoSQ3Tx_Type=Counter64
_Xgs360026fPortQoSQ3Tx_Object=MibTableColumn
xgs360026fPortQoSQ3Tx=_Xgs360026fPortQoSQ3Tx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,9),_Xgs360026fPortQoSQ3Tx_Type())
xgs360026fPortQoSQ3Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ3Tx.setStatus(_A)
_Xgs360026fPortQoSQ4Rx_Type=Counter64
_Xgs360026fPortQoSQ4Rx_Object=MibTableColumn
xgs360026fPortQoSQ4Rx=_Xgs360026fPortQoSQ4Rx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,10),_Xgs360026fPortQoSQ4Rx_Type())
xgs360026fPortQoSQ4Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ4Rx.setStatus(_A)
_Xgs360026fPortQoSQ4Tx_Type=Counter64
_Xgs360026fPortQoSQ4Tx_Object=MibTableColumn
xgs360026fPortQoSQ4Tx=_Xgs360026fPortQoSQ4Tx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,11),_Xgs360026fPortQoSQ4Tx_Type())
xgs360026fPortQoSQ4Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ4Tx.setStatus(_A)
_Xgs360026fPortQoSQ5Rx_Type=Counter64
_Xgs360026fPortQoSQ5Rx_Object=MibTableColumn
xgs360026fPortQoSQ5Rx=_Xgs360026fPortQoSQ5Rx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,12),_Xgs360026fPortQoSQ5Rx_Type())
xgs360026fPortQoSQ5Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ5Rx.setStatus(_A)
_Xgs360026fPortQoSQ5Tx_Type=Counter64
_Xgs360026fPortQoSQ5Tx_Object=MibTableColumn
xgs360026fPortQoSQ5Tx=_Xgs360026fPortQoSQ5Tx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,13),_Xgs360026fPortQoSQ5Tx_Type())
xgs360026fPortQoSQ5Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ5Tx.setStatus(_A)
_Xgs360026fPortQoSQ6Rx_Type=Counter64
_Xgs360026fPortQoSQ6Rx_Object=MibTableColumn
xgs360026fPortQoSQ6Rx=_Xgs360026fPortQoSQ6Rx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,14),_Xgs360026fPortQoSQ6Rx_Type())
xgs360026fPortQoSQ6Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ6Rx.setStatus(_A)
_Xgs360026fPortQoSQ6Tx_Type=Counter64
_Xgs360026fPortQoSQ6Tx_Object=MibTableColumn
xgs360026fPortQoSQ6Tx=_Xgs360026fPortQoSQ6Tx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,15),_Xgs360026fPortQoSQ6Tx_Type())
xgs360026fPortQoSQ6Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ6Tx.setStatus(_A)
_Xgs360026fPortQoSQ7Rx_Type=Counter64
_Xgs360026fPortQoSQ7Rx_Object=MibTableColumn
xgs360026fPortQoSQ7Rx=_Xgs360026fPortQoSQ7Rx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,16),_Xgs360026fPortQoSQ7Rx_Type())
xgs360026fPortQoSQ7Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ7Rx.setStatus(_A)
_Xgs360026fPortQoSQ7Tx_Type=Counter64
_Xgs360026fPortQoSQ7Tx_Object=MibTableColumn
xgs360026fPortQoSQ7Tx=_Xgs360026fPortQoSQ7Tx_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,3,2,1,17),_Xgs360026fPortQoSQ7Tx_Type())
xgs360026fPortQoSQ7Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortQoSQ7Tx.setStatus(_A)
_Xgs360026fSFPInfoTable_Object=MibTable
xgs360026fSFPInfoTable=_Xgs360026fSFPInfoTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4))
if mibBuilder.loadTexts:xgs360026fSFPInfoTable.setStatus(_A)
_Xgs360026fSFPInfoEntry_Object=MibTableRow
xgs360026fSFPInfoEntry=_Xgs360026fSFPInfoEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1))
xgs360026fSFPInfoEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:xgs360026fSFPInfoEntry.setStatus(_A)
class _Xgs360026fSFPInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fSFPInfoIndex_Type.__name__=_B
_Xgs360026fSFPInfoIndex_Object=MibTableColumn
xgs360026fSFPInfoIndex=_Xgs360026fSFPInfoIndex_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,1),_Xgs360026fSFPInfoIndex_Type())
xgs360026fSFPInfoIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fSFPInfoIndex.setStatus(_A)
_Xgs360026fSFPInfoPort_Type=DisplayString
_Xgs360026fSFPInfoPort_Object=MibTableColumn
xgs360026fSFPInfoPort=_Xgs360026fSFPInfoPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,2),_Xgs360026fSFPInfoPort_Type())
xgs360026fSFPInfoPort.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPInfoPort.setStatus(_A)
_Xgs360026fSFPConnectorType_Type=DisplayString
_Xgs360026fSFPConnectorType_Object=MibTableColumn
xgs360026fSFPConnectorType=_Xgs360026fSFPConnectorType_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,3),_Xgs360026fSFPConnectorType_Type())
xgs360026fSFPConnectorType.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPConnectorType.setStatus(_A)
_Xgs360026fSFPFiberType_Type=DisplayString
_Xgs360026fSFPFiberType_Object=MibTableColumn
xgs360026fSFPFiberType=_Xgs360026fSFPFiberType_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,4),_Xgs360026fSFPFiberType_Type())
xgs360026fSFPFiberType.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPFiberType.setStatus(_A)
_Xgs360026fSFPTxCentralWavelength_Type=DisplayString
_Xgs360026fSFPTxCentralWavelength_Object=MibTableColumn
xgs360026fSFPTxCentralWavelength=_Xgs360026fSFPTxCentralWavelength_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,5),_Xgs360026fSFPTxCentralWavelength_Type())
xgs360026fSFPTxCentralWavelength.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPTxCentralWavelength.setStatus(_A)
_Xgs360026fSFPBaudRate_Type=DisplayString
_Xgs360026fSFPBaudRate_Object=MibTableColumn
xgs360026fSFPBaudRate=_Xgs360026fSFPBaudRate_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,6),_Xgs360026fSFPBaudRate_Type())
xgs360026fSFPBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPBaudRate.setStatus(_A)
_Xgs360026fSFPVendorOUI_Type=DisplayString
_Xgs360026fSFPVendorOUI_Object=MibTableColumn
xgs360026fSFPVendorOUI=_Xgs360026fSFPVendorOUI_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,7),_Xgs360026fSFPVendorOUI_Type())
xgs360026fSFPVendorOUI.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPVendorOUI.setStatus(_A)
_Xgs360026fSFPVendorName_Type=DisplayString
_Xgs360026fSFPVendorName_Object=MibTableColumn
xgs360026fSFPVendorName=_Xgs360026fSFPVendorName_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,8),_Xgs360026fSFPVendorName_Type())
xgs360026fSFPVendorName.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPVendorName.setStatus(_A)
_Xgs360026fSFPVendorPN_Type=DisplayString
_Xgs360026fSFPVendorPN_Object=MibTableColumn
xgs360026fSFPVendorPN=_Xgs360026fSFPVendorPN_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,9),_Xgs360026fSFPVendorPN_Type())
xgs360026fSFPVendorPN.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPVendorPN.setStatus(_A)
_Xgs360026fSFPVendorRev_Type=DisplayString
_Xgs360026fSFPVendorRev_Object=MibTableColumn
xgs360026fSFPVendorRev=_Xgs360026fSFPVendorRev_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,10),_Xgs360026fSFPVendorRev_Type())
xgs360026fSFPVendorRev.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPVendorRev.setStatus(_A)
_Xgs360026fSFPVendorSN_Type=DisplayString
_Xgs360026fSFPVendorSN_Object=MibTableColumn
xgs360026fSFPVendorSN=_Xgs360026fSFPVendorSN_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,11),_Xgs360026fSFPVendorSN_Type())
xgs360026fSFPVendorSN.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPVendorSN.setStatus(_A)
_Xgs360026fSFPDateCode_Type=DisplayString
_Xgs360026fSFPDateCode_Object=MibTableColumn
xgs360026fSFPDateCode=_Xgs360026fSFPDateCode_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,12),_Xgs360026fSFPDateCode_Type())
xgs360026fSFPDateCode.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPDateCode.setStatus(_A)
_Xgs360026fSFPTemperature_Type=DisplayString
_Xgs360026fSFPTemperature_Object=MibTableColumn
xgs360026fSFPTemperature=_Xgs360026fSFPTemperature_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,13),_Xgs360026fSFPTemperature_Type())
xgs360026fSFPTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPTemperature.setStatus(_A)
_Xgs360026fSFPVcc_Type=DisplayString
_Xgs360026fSFPVcc_Object=MibTableColumn
xgs360026fSFPVcc=_Xgs360026fSFPVcc_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,14),_Xgs360026fSFPVcc_Type())
xgs360026fSFPVcc.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPVcc.setStatus(_A)
_Xgs360026fSFPMon1Bias_Type=DisplayString
_Xgs360026fSFPMon1Bias_Object=MibTableColumn
xgs360026fSFPMon1Bias=_Xgs360026fSFPMon1Bias_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,15),_Xgs360026fSFPMon1Bias_Type())
xgs360026fSFPMon1Bias.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPMon1Bias.setStatus(_A)
_Xgs360026fSFPMon2TxPWR_Type=DisplayString
_Xgs360026fSFPMon2TxPWR_Object=MibTableColumn
xgs360026fSFPMon2TxPWR=_Xgs360026fSFPMon2TxPWR_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,16),_Xgs360026fSFPMon2TxPWR_Type())
xgs360026fSFPMon2TxPWR.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPMon2TxPWR.setStatus(_A)
_Xgs360026fSFPMon3RxPWR_Type=DisplayString
_Xgs360026fSFPMon3RxPWR_Object=MibTableColumn
xgs360026fSFPMon3RxPWR=_Xgs360026fSFPMon3RxPWR_Object((1,3,6,1,4,1,890,1,5,8,77,2,1,4,1,17),_Xgs360026fSFPMon3RxPWR_Type())
xgs360026fSFPMon3RxPWR.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSFPMon3RxPWR.setStatus(_A)
_Xgs360026fGARP_ObjectIdentity=ObjectIdentity
xgs360026fGARP=_Xgs360026fGARP_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,3))
_Xgs360026fGARPConfTable_Object=MibTable
xgs360026fGARPConfTable=_Xgs360026fGARPConfTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,3,1))
if mibBuilder.loadTexts:xgs360026fGARPConfTable.setStatus(_A)
_Xgs360026fGARPConfEntry_Object=MibTableRow
xgs360026fGARPConfEntry=_Xgs360026fGARPConfEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,3,1,1))
xgs360026fGARPConfEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:xgs360026fGARPConfEntry.setStatus(_A)
class _Xgs360026fGARPConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fGARPConfPort_Type.__name__=_B
_Xgs360026fGARPConfPort_Object=MibTableColumn
xgs360026fGARPConfPort=_Xgs360026fGARPConfPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,3,1,1,1),_Xgs360026fGARPConfPort_Type())
xgs360026fGARPConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fGARPConfPort.setStatus(_A)
class _Xgs360026fGARPJoinTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,1000))
_Xgs360026fGARPJoinTimer_Type.__name__=_B
_Xgs360026fGARPJoinTimer_Object=MibTableColumn
xgs360026fGARPJoinTimer=_Xgs360026fGARPJoinTimer_Object((1,3,6,1,4,1,890,1,5,8,77,2,3,1,1,2),_Xgs360026fGARPJoinTimer_Type())
xgs360026fGARPJoinTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fGARPJoinTimer.setStatus(_A)
class _Xgs360026fGARPLeaveTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,3000))
_Xgs360026fGARPLeaveTimer_Type.__name__=_B
_Xgs360026fGARPLeaveTimer_Object=MibTableColumn
xgs360026fGARPLeaveTimer=_Xgs360026fGARPLeaveTimer_Object((1,3,6,1,4,1,890,1,5,8,77,2,3,1,1,3),_Xgs360026fGARPLeaveTimer_Type())
xgs360026fGARPLeaveTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fGARPLeaveTimer.setStatus(_A)
class _Xgs360026fGARPLeaveAllTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10000,50000))
_Xgs360026fGARPLeaveAllTimer_Type.__name__=_B
_Xgs360026fGARPLeaveAllTimer_Object=MibTableColumn
xgs360026fGARPLeaveAllTimer=_Xgs360026fGARPLeaveAllTimer_Object((1,3,6,1,4,1,890,1,5,8,77,2,3,1,1,4),_Xgs360026fGARPLeaveAllTimer_Type())
xgs360026fGARPLeaveAllTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fGARPLeaveAllTimer.setStatus(_A)
class _Xgs360026fGARPApplicantion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Xgs360026fGARPApplicantion_Type.__name__=_B
_Xgs360026fGARPApplicantion_Object=MibTableColumn
xgs360026fGARPApplicantion=_Xgs360026fGARPApplicantion_Object((1,3,6,1,4,1,890,1,5,8,77,2,3,1,1,5),_Xgs360026fGARPApplicantion_Type())
xgs360026fGARPApplicantion.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fGARPApplicantion.setStatus(_A)
class _Xgs360026fGARPAttributeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Xgs360026fGARPAttributeType_Type.__name__=_B
_Xgs360026fGARPAttributeType_Object=MibTableColumn
xgs360026fGARPAttributeType=_Xgs360026fGARPAttributeType_Object((1,3,6,1,4,1,890,1,5,8,77,2,3,1,1,6),_Xgs360026fGARPAttributeType_Type())
xgs360026fGARPAttributeType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fGARPAttributeType.setStatus(_A)
class _Xgs360026fGARPApplicant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fGARPApplicant_Type.__name__=_B
_Xgs360026fGARPApplicant_Object=MibTableColumn
xgs360026fGARPApplicant=_Xgs360026fGARPApplicant_Object((1,3,6,1,4,1,890,1,5,8,77,2,3,1,1,7),_Xgs360026fGARPApplicant_Type())
xgs360026fGARPApplicant.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fGARPApplicant.setStatus(_A)
_Xgs360026fGARPStatisticsTable_Object=MibTable
xgs360026fGARPStatisticsTable=_Xgs360026fGARPStatisticsTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,3,2))
if mibBuilder.loadTexts:xgs360026fGARPStatisticsTable.setStatus(_A)
_Xgs360026fGARPStatisticsEntry_Object=MibTableRow
xgs360026fGARPStatisticsEntry=_Xgs360026fGARPStatisticsEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,3,2,1))
xgs360026fGARPStatisticsEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:xgs360026fGARPStatisticsEntry.setStatus(_A)
class _Xgs360026fGARPStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fGARPStatisticsPort_Type.__name__=_B
_Xgs360026fGARPStatisticsPort_Object=MibTableColumn
xgs360026fGARPStatisticsPort=_Xgs360026fGARPStatisticsPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,3,2,1,1),_Xgs360026fGARPStatisticsPort_Type())
xgs360026fGARPStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fGARPStatisticsPort.setStatus(_A)
_Xgs360026fGARPStatisticsPeerMAC_Type=DisplayString
_Xgs360026fGARPStatisticsPeerMAC_Object=MibTableColumn
xgs360026fGARPStatisticsPeerMAC=_Xgs360026fGARPStatisticsPeerMAC_Object((1,3,6,1,4,1,890,1,5,8,77,2,3,2,1,2),_Xgs360026fGARPStatisticsPeerMAC_Type())
xgs360026fGARPStatisticsPeerMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fGARPStatisticsPeerMAC.setStatus(_A)
_Xgs360026fGARPStatisticsFailedCount_Type=Counter32
_Xgs360026fGARPStatisticsFailedCount_Object=MibTableColumn
xgs360026fGARPStatisticsFailedCount=_Xgs360026fGARPStatisticsFailedCount_Object((1,3,6,1,4,1,890,1,5,8,77,2,3,2,1,3),_Xgs360026fGARPStatisticsFailedCount_Type())
xgs360026fGARPStatisticsFailedCount.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fGARPStatisticsFailedCount.setStatus(_A)
_Xgs360026fGVRP_ObjectIdentity=ObjectIdentity
xgs360026fGVRP=_Xgs360026fGVRP_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,4))
_Xgs360026fGVRPConf_ObjectIdentity=ObjectIdentity
xgs360026fGVRPConf=_Xgs360026fGVRPConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,4,1))
class _Xgs360026fGVRPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fGVRPMode_Type.__name__=_B
_Xgs360026fGVRPMode_Object=MibScalar
xgs360026fGVRPMode=_Xgs360026fGVRPMode_Object((1,3,6,1,4,1,890,1,5,8,77,2,4,1,1),_Xgs360026fGVRPMode_Type())
xgs360026fGVRPMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fGVRPMode.setStatus(_A)
_Xgs360026fGVRPConfTable_Object=MibTable
xgs360026fGVRPConfTable=_Xgs360026fGVRPConfTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,4,1,2))
if mibBuilder.loadTexts:xgs360026fGVRPConfTable.setStatus(_A)
_Xgs360026fGVRPConfEntry_Object=MibTableRow
xgs360026fGVRPConfEntry=_Xgs360026fGVRPConfEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,4,1,2,1))
xgs360026fGVRPConfEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:xgs360026fGVRPConfEntry.setStatus(_A)
class _Xgs360026fGVRPConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fGVRPConfPort_Type.__name__=_B
_Xgs360026fGVRPConfPort_Object=MibTableColumn
xgs360026fGVRPConfPort=_Xgs360026fGVRPConfPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,4,1,2,1,1),_Xgs360026fGVRPConfPort_Type())
xgs360026fGVRPConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fGVRPConfPort.setStatus(_A)
class _Xgs360026fGVRPConfPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fGVRPConfPortMode_Type.__name__=_B
_Xgs360026fGVRPConfPortMode_Object=MibTableColumn
xgs360026fGVRPConfPortMode=_Xgs360026fGVRPConfPortMode_Object((1,3,6,1,4,1,890,1,5,8,77,2,4,1,2,1,2),_Xgs360026fGVRPConfPortMode_Type())
xgs360026fGVRPConfPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fGVRPConfPortMode.setStatus(_A)
class _Xgs360026fGVRPConfPortRRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fGVRPConfPortRRole_Type.__name__=_B
_Xgs360026fGVRPConfPortRRole_Object=MibTableColumn
xgs360026fGVRPConfPortRRole=_Xgs360026fGVRPConfPortRRole_Object((1,3,6,1,4,1,890,1,5,8,77,2,4,1,2,1,3),_Xgs360026fGVRPConfPortRRole_Type())
xgs360026fGVRPConfPortRRole.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fGVRPConfPortRRole.setStatus(_A)
_Xgs360026fGVRPStatisticsTable_Object=MibTable
xgs360026fGVRPStatisticsTable=_Xgs360026fGVRPStatisticsTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,4,2))
if mibBuilder.loadTexts:xgs360026fGVRPStatisticsTable.setStatus(_A)
_Xgs360026fGVRPStatisticsEntry_Object=MibTableRow
xgs360026fGVRPStatisticsEntry=_Xgs360026fGVRPStatisticsEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,4,2,1))
xgs360026fGVRPStatisticsEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:xgs360026fGVRPStatisticsEntry.setStatus(_A)
class _Xgs360026fGVRPStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fGVRPStatisticsPort_Type.__name__=_B
_Xgs360026fGVRPStatisticsPort_Object=MibTableColumn
xgs360026fGVRPStatisticsPort=_Xgs360026fGVRPStatisticsPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,4,2,1,1),_Xgs360026fGVRPStatisticsPort_Type())
xgs360026fGVRPStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fGVRPStatisticsPort.setStatus(_A)
_Xgs360026fGVRPStatisticsJoinTxCnt_Type=Counter32
_Xgs360026fGVRPStatisticsJoinTxCnt_Object=MibTableColumn
xgs360026fGVRPStatisticsJoinTxCnt=_Xgs360026fGVRPStatisticsJoinTxCnt_Object((1,3,6,1,4,1,890,1,5,8,77,2,4,2,1,2),_Xgs360026fGVRPStatisticsJoinTxCnt_Type())
xgs360026fGVRPStatisticsJoinTxCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fGVRPStatisticsJoinTxCnt.setStatus(_A)
_Xgs360026fGVRPStatisticsLeaveTxCnt_Type=Counter32
_Xgs360026fGVRPStatisticsLeaveTxCnt_Object=MibTableColumn
xgs360026fGVRPStatisticsLeaveTxCnt=_Xgs360026fGVRPStatisticsLeaveTxCnt_Object((1,3,6,1,4,1,890,1,5,8,77,2,4,2,1,3),_Xgs360026fGVRPStatisticsLeaveTxCnt_Type())
xgs360026fGVRPStatisticsLeaveTxCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fGVRPStatisticsLeaveTxCnt.setStatus(_A)
_Xgs360026fThermalProtection_ObjectIdentity=ObjectIdentity
xgs360026fThermalProtection=_Xgs360026fThermalProtection_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,5))
class _Xgs360026fPriority0Temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360026fPriority0Temperature_Type.__name__=_B
_Xgs360026fPriority0Temperature_Object=MibScalar
xgs360026fPriority0Temperature=_Xgs360026fPriority0Temperature_Object((1,3,6,1,4,1,890,1,5,8,77,2,5,1),_Xgs360026fPriority0Temperature_Type())
xgs360026fPriority0Temperature.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPriority0Temperature.setStatus(_A)
class _Xgs360026fPriority1Temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360026fPriority1Temperature_Type.__name__=_B
_Xgs360026fPriority1Temperature_Object=MibScalar
xgs360026fPriority1Temperature=_Xgs360026fPriority1Temperature_Object((1,3,6,1,4,1,890,1,5,8,77,2,5,2),_Xgs360026fPriority1Temperature_Type())
xgs360026fPriority1Temperature.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPriority1Temperature.setStatus(_A)
class _Xgs360026fPriority2Temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360026fPriority2Temperature_Type.__name__=_B
_Xgs360026fPriority2Temperature_Object=MibScalar
xgs360026fPriority2Temperature=_Xgs360026fPriority2Temperature_Object((1,3,6,1,4,1,890,1,5,8,77,2,5,3),_Xgs360026fPriority2Temperature_Type())
xgs360026fPriority2Temperature.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPriority2Temperature.setStatus(_A)
class _Xgs360026fPriority3Temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360026fPriority3Temperature_Type.__name__=_B
_Xgs360026fPriority3Temperature_Object=MibScalar
xgs360026fPriority3Temperature=_Xgs360026fPriority3Temperature_Object((1,3,6,1,4,1,890,1,5,8,77,2,5,4),_Xgs360026fPriority3Temperature_Type())
xgs360026fPriority3Temperature.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPriority3Temperature.setStatus(_A)
_Xgs360026fThermalProtectionTable_Object=MibTable
xgs360026fThermalProtectionTable=_Xgs360026fThermalProtectionTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,5,5))
if mibBuilder.loadTexts:xgs360026fThermalProtectionTable.setStatus(_A)
_Xgs360026fThermalProtectionEntry_Object=MibTableRow
xgs360026fThermalProtectionEntry=_Xgs360026fThermalProtectionEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,5,5,1))
xgs360026fThermalProtectionEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:xgs360026fThermalProtectionEntry.setStatus(_A)
class _Xgs360026fThermalProtectionPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fThermalProtectionPort_Type.__name__=_B
_Xgs360026fThermalProtectionPort_Object=MibTableColumn
xgs360026fThermalProtectionPort=_Xgs360026fThermalProtectionPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,5,5,1,1),_Xgs360026fThermalProtectionPort_Type())
xgs360026fThermalProtectionPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fThermalProtectionPort.setStatus(_A)
class _Xgs360026fThermalProtectionPortTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360026fThermalProtectionPortTemperature_Type.__name__=_B
_Xgs360026fThermalProtectionPortTemperature_Object=MibTableColumn
xgs360026fThermalProtectionPortTemperature=_Xgs360026fThermalProtectionPortTemperature_Object((1,3,6,1,4,1,890,1,5,8,77,2,5,5,1,2),_Xgs360026fThermalProtectionPortTemperature_Type())
xgs360026fThermalProtectionPortTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fThermalProtectionPortTemperature.setStatus(_A)
class _Xgs360026fThermalProtectionPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360026fThermalProtectionPortPriority_Type.__name__=_B
_Xgs360026fThermalProtectionPortPriority_Object=MibTableColumn
xgs360026fThermalProtectionPortPriority=_Xgs360026fThermalProtectionPortPriority_Object((1,3,6,1,4,1,890,1,5,8,77,2,5,5,1,3),_Xgs360026fThermalProtectionPortPriority_Type())
xgs360026fThermalProtectionPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fThermalProtectionPortPriority.setStatus(_A)
_Xgs360026fThermalProtectionPortStatus_Type=DisplayString
_Xgs360026fThermalProtectionPortStatus_Object=MibTableColumn
xgs360026fThermalProtectionPortStatus=_Xgs360026fThermalProtectionPortStatus_Object((1,3,6,1,4,1,890,1,5,8,77,2,5,5,1,4),_Xgs360026fThermalProtectionPortStatus_Type())
xgs360026fThermalProtectionPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fThermalProtectionPortStatus.setStatus(_A)
_Xgs360026fMirroring_ObjectIdentity=ObjectIdentity
xgs360026fMirroring=_Xgs360026fMirroring_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,6))
class _Xgs360026fPortToMirrorOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Xgs360026fPortToMirrorOn_Type.__name__=_B
_Xgs360026fPortToMirrorOn_Object=MibScalar
xgs360026fPortToMirrorOn=_Xgs360026fPortToMirrorOn_Object((1,3,6,1,4,1,890,1,5,8,77,2,6,1),_Xgs360026fPortToMirrorOn_Type())
xgs360026fPortToMirrorOn.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortToMirrorOn.setStatus(_A)
_Xgs360026fMirrorTable_Object=MibTable
xgs360026fMirrorTable=_Xgs360026fMirrorTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,6,2))
if mibBuilder.loadTexts:xgs360026fMirrorTable.setStatus(_A)
_Xgs360026fMirrorEntry_Object=MibTableRow
xgs360026fMirrorEntry=_Xgs360026fMirrorEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,6,2,1))
xgs360026fMirrorEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:xgs360026fMirrorEntry.setStatus(_A)
class _Xgs360026fMirrorPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fMirrorPort_Type.__name__=_B
_Xgs360026fMirrorPort_Object=MibTableColumn
xgs360026fMirrorPort=_Xgs360026fMirrorPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,6,2,1,1),_Xgs360026fMirrorPort_Type())
xgs360026fMirrorPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fMirrorPort.setStatus(_A)
class _Xgs360026fMirrorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360026fMirrorMode_Type.__name__=_B
_Xgs360026fMirrorMode_Object=MibTableColumn
xgs360026fMirrorMode=_Xgs360026fMirrorMode_Object((1,3,6,1,4,1,890,1,5,8,77,2,6,2,1,2),_Xgs360026fMirrorMode_Type())
xgs360026fMirrorMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMirrorMode.setStatus(_A)
_Xgs360026fTrapEventSeverity_ObjectIdentity=ObjectIdentity
xgs360026fTrapEventSeverity=_Xgs360026fTrapEventSeverity_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,7))
class _Xgs360026fTrapEventSeverityACL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityACL_Type.__name__=_B
_Xgs360026fTrapEventSeverityACL_Object=MibScalar
xgs360026fTrapEventSeverityACL=_Xgs360026fTrapEventSeverityACL_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,1),_Xgs360026fTrapEventSeverityACL_Type())
xgs360026fTrapEventSeverityACL.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityACL.setStatus(_A)
class _Xgs360026fTrapEventSeverityACLLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityACLLog_Type.__name__=_B
_Xgs360026fTrapEventSeverityACLLog_Object=MibScalar
xgs360026fTrapEventSeverityACLLog=_Xgs360026fTrapEventSeverityACLLog_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,2),_Xgs360026fTrapEventSeverityACLLog_Type())
xgs360026fTrapEventSeverityACLLog.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityACLLog.setStatus(_A)
class _Xgs360026fTrapEventSeverityAccessMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityAccessMgmt_Type.__name__=_B
_Xgs360026fTrapEventSeverityAccessMgmt_Object=MibScalar
xgs360026fTrapEventSeverityAccessMgmt=_Xgs360026fTrapEventSeverityAccessMgmt_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,3),_Xgs360026fTrapEventSeverityAccessMgmt_Type())
xgs360026fTrapEventSeverityAccessMgmt.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityAccessMgmt.setStatus(_A)
class _Xgs360026fTrapEventSeverityAuthFailed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityAuthFailed_Type.__name__=_B
_Xgs360026fTrapEventSeverityAuthFailed_Object=MibScalar
xgs360026fTrapEventSeverityAuthFailed=_Xgs360026fTrapEventSeverityAuthFailed_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,4),_Xgs360026fTrapEventSeverityAuthFailed_Type())
xgs360026fTrapEventSeverityAuthFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityAuthFailed.setStatus(_A)
class _Xgs360026fTrapEventSeverityColdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityColdStart_Type.__name__=_B
_Xgs360026fTrapEventSeverityColdStart_Object=MibScalar
xgs360026fTrapEventSeverityColdStart=_Xgs360026fTrapEventSeverityColdStart_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,5),_Xgs360026fTrapEventSeverityColdStart_Type())
xgs360026fTrapEventSeverityColdStart.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityColdStart.setStatus(_A)
class _Xgs360026fTrapEventSeverityConfigInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityConfigInfo_Type.__name__=_B
_Xgs360026fTrapEventSeverityConfigInfo_Object=MibScalar
xgs360026fTrapEventSeverityConfigInfo=_Xgs360026fTrapEventSeverityConfigInfo_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,6),_Xgs360026fTrapEventSeverityConfigInfo_Type())
xgs360026fTrapEventSeverityConfigInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityConfigInfo.setStatus(_A)
class _Xgs360026fTrapEventSeverityFirmwareUpgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityFirmwareUpgrade_Type.__name__=_B
_Xgs360026fTrapEventSeverityFirmwareUpgrade_Object=MibScalar
xgs360026fTrapEventSeverityFirmwareUpgrade=_Xgs360026fTrapEventSeverityFirmwareUpgrade_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,7),_Xgs360026fTrapEventSeverityFirmwareUpgrade_Type())
xgs360026fTrapEventSeverityFirmwareUpgrade.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityFirmwareUpgrade.setStatus(_A)
class _Xgs360026fTrapEventSeverityImportExport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityImportExport_Type.__name__=_B
_Xgs360026fTrapEventSeverityImportExport_Object=MibScalar
xgs360026fTrapEventSeverityImportExport=_Xgs360026fTrapEventSeverityImportExport_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,8),_Xgs360026fTrapEventSeverityImportExport_Type())
xgs360026fTrapEventSeverityImportExport.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityImportExport.setStatus(_A)
class _Xgs360026fTrapEventSeverityLACP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityLACP_Type.__name__=_B
_Xgs360026fTrapEventSeverityLACP_Object=MibScalar
xgs360026fTrapEventSeverityLACP=_Xgs360026fTrapEventSeverityLACP_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,9),_Xgs360026fTrapEventSeverityLACP_Type())
xgs360026fTrapEventSeverityLACP.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityLACP.setStatus(_A)
class _Xgs360026fTrapEventSeverityLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityLinkStatus_Type.__name__=_B
_Xgs360026fTrapEventSeverityLinkStatus_Object=MibScalar
xgs360026fTrapEventSeverityLinkStatus=_Xgs360026fTrapEventSeverityLinkStatus_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,10),_Xgs360026fTrapEventSeverityLinkStatus_Type())
xgs360026fTrapEventSeverityLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityLinkStatus.setStatus(_A)
class _Xgs360026fTrapEventSeverityLogin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityLogin_Type.__name__=_B
_Xgs360026fTrapEventSeverityLogin_Object=MibScalar
xgs360026fTrapEventSeverityLogin=_Xgs360026fTrapEventSeverityLogin_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,11),_Xgs360026fTrapEventSeverityLogin_Type())
xgs360026fTrapEventSeverityLogin.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityLogin.setStatus(_A)
class _Xgs360026fTrapEventSeverityLogout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityLogout_Type.__name__=_B
_Xgs360026fTrapEventSeverityLogout_Object=MibScalar
xgs360026fTrapEventSeverityLogout=_Xgs360026fTrapEventSeverityLogout_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,12),_Xgs360026fTrapEventSeverityLogout_Type())
xgs360026fTrapEventSeverityLogout.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityLogout.setStatus(_A)
class _Xgs360026fTrapEventSeverityLoopProtect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityLoopProtect_Type.__name__=_B
_Xgs360026fTrapEventSeverityLoopProtect_Object=MibScalar
xgs360026fTrapEventSeverityLoopProtect=_Xgs360026fTrapEventSeverityLoopProtect_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,13),_Xgs360026fTrapEventSeverityLoopProtect_Type())
xgs360026fTrapEventSeverityLoopProtect.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityLoopProtect.setStatus(_A)
class _Xgs360026fTrapEventSeverityMgmtIPChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityMgmtIPChange_Type.__name__=_B
_Xgs360026fTrapEventSeverityMgmtIPChange_Object=MibScalar
xgs360026fTrapEventSeverityMgmtIPChange=_Xgs360026fTrapEventSeverityMgmtIPChange_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,14),_Xgs360026fTrapEventSeverityMgmtIPChange_Type())
xgs360026fTrapEventSeverityMgmtIPChange.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityMgmtIPChange.setStatus(_A)
class _Xgs360026fTrapEventSeverityModuleChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityModuleChange_Type.__name__=_B
_Xgs360026fTrapEventSeverityModuleChange_Object=MibScalar
xgs360026fTrapEventSeverityModuleChange=_Xgs360026fTrapEventSeverityModuleChange_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,15),_Xgs360026fTrapEventSeverityModuleChange_Type())
xgs360026fTrapEventSeverityModuleChange.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityModuleChange.setStatus(_A)
class _Xgs360026fTrapEventSeverityNAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityNAS_Type.__name__=_B
_Xgs360026fTrapEventSeverityNAS_Object=MibScalar
xgs360026fTrapEventSeverityNAS=_Xgs360026fTrapEventSeverityNAS_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,16),_Xgs360026fTrapEventSeverityNAS_Type())
xgs360026fTrapEventSeverityNAS.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityNAS.setStatus(_A)
class _Xgs360026fTrapEventSeverityPasswdChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityPasswdChange_Type.__name__=_B
_Xgs360026fTrapEventSeverityPasswdChange_Object=MibScalar
xgs360026fTrapEventSeverityPasswdChange=_Xgs360026fTrapEventSeverityPasswdChange_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,17),_Xgs360026fTrapEventSeverityPasswdChange_Type())
xgs360026fTrapEventSeverityPasswdChange.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityPasswdChange.setStatus(_A)
class _Xgs360026fTrapEventSeverityPortSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityPortSecurity_Type.__name__=_B
_Xgs360026fTrapEventSeverityPortSecurity_Object=MibScalar
xgs360026fTrapEventSeverityPortSecurity=_Xgs360026fTrapEventSeverityPortSecurity_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,18),_Xgs360026fTrapEventSeverityPortSecurity_Type())
xgs360026fTrapEventSeverityPortSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityPortSecurity.setStatus(_A)
class _Xgs360026fTrapEventSeverityThermalProtect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityThermalProtect_Type.__name__=_B
_Xgs360026fTrapEventSeverityThermalProtect_Object=MibScalar
xgs360026fTrapEventSeverityThermalProtect=_Xgs360026fTrapEventSeverityThermalProtect_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,19),_Xgs360026fTrapEventSeverityThermalProtect_Type())
xgs360026fTrapEventSeverityThermalProtect.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityThermalProtect.setStatus(_A)
class _Xgs360026fTrapEventSeverityVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityVLAN_Type.__name__=_B
_Xgs360026fTrapEventSeverityVLAN_Object=MibScalar
xgs360026fTrapEventSeverityVLAN=_Xgs360026fTrapEventSeverityVLAN_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,20),_Xgs360026fTrapEventSeverityVLAN_Type())
xgs360026fTrapEventSeverityVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityVLAN.setStatus(_A)
class _Xgs360026fTrapEventSeverityWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fTrapEventSeverityWarmStart_Type.__name__=_B
_Xgs360026fTrapEventSeverityWarmStart_Object=MibScalar
xgs360026fTrapEventSeverityWarmStart=_Xgs360026fTrapEventSeverityWarmStart_Object((1,3,6,1,4,1,890,1,5,8,77,2,7,21),_Xgs360026fTrapEventSeverityWarmStart_Type())
xgs360026fTrapEventSeverityWarmStart.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTrapEventSeverityWarmStart.setStatus(_A)
_Xgs360026fSMTP_ObjectIdentity=ObjectIdentity
xgs360026fSMTP=_Xgs360026fSMTP_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,8))
_Xgs360026fSMTPMailServer_Type=DisplayString
_Xgs360026fSMTPMailServer_Object=MibScalar
xgs360026fSMTPMailServer=_Xgs360026fSMTPMailServer_Object((1,3,6,1,4,1,890,1,5,8,77,2,8,1),_Xgs360026fSMTPMailServer_Type())
xgs360026fSMTPMailServer.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSMTPMailServer.setStatus(_A)
_Xgs360026fSMTPUserName_Type=DisplayString
_Xgs360026fSMTPUserName_Object=MibScalar
xgs360026fSMTPUserName=_Xgs360026fSMTPUserName_Object((1,3,6,1,4,1,890,1,5,8,77,2,8,2),_Xgs360026fSMTPUserName_Type())
xgs360026fSMTPUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSMTPUserName.setStatus(_A)
_Xgs360026fSMTPPassword_Type=DisplayString
_Xgs360026fSMTPPassword_Object=MibScalar
xgs360026fSMTPPassword=_Xgs360026fSMTPPassword_Object((1,3,6,1,4,1,890,1,5,8,77,2,8,3),_Xgs360026fSMTPPassword_Type())
xgs360026fSMTPPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSMTPPassword.setStatus(_A)
class _Xgs360026fSMTPServeriryLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360026fSMTPServeriryLevel_Type.__name__=_B
_Xgs360026fSMTPServeriryLevel_Object=MibScalar
xgs360026fSMTPServeriryLevel=_Xgs360026fSMTPServeriryLevel_Object((1,3,6,1,4,1,890,1,5,8,77,2,8,4),_Xgs360026fSMTPServeriryLevel_Type())
xgs360026fSMTPServeriryLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSMTPServeriryLevel.setStatus(_A)
_Xgs360026fSMTPSender_Type=DisplayString
_Xgs360026fSMTPSender_Object=MibScalar
xgs360026fSMTPSender=_Xgs360026fSMTPSender_Object((1,3,6,1,4,1,890,1,5,8,77,2,8,5),_Xgs360026fSMTPSender_Type())
xgs360026fSMTPSender.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSMTPSender.setStatus(_A)
_Xgs360026fSMTPReturnPath_Type=DisplayString
_Xgs360026fSMTPReturnPath_Object=MibScalar
xgs360026fSMTPReturnPath=_Xgs360026fSMTPReturnPath_Object((1,3,6,1,4,1,890,1,5,8,77,2,8,6),_Xgs360026fSMTPReturnPath_Type())
xgs360026fSMTPReturnPath.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSMTPReturnPath.setStatus(_A)
_Xgs360026fSMTPEmailAddress1_Type=DisplayString
_Xgs360026fSMTPEmailAddress1_Object=MibScalar
xgs360026fSMTPEmailAddress1=_Xgs360026fSMTPEmailAddress1_Object((1,3,6,1,4,1,890,1,5,8,77,2,8,7),_Xgs360026fSMTPEmailAddress1_Type())
xgs360026fSMTPEmailAddress1.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSMTPEmailAddress1.setStatus(_A)
_Xgs360026fSMTPEmailAddress2_Type=DisplayString
_Xgs360026fSMTPEmailAddress2_Object=MibScalar
xgs360026fSMTPEmailAddress2=_Xgs360026fSMTPEmailAddress2_Object((1,3,6,1,4,1,890,1,5,8,77,2,8,8),_Xgs360026fSMTPEmailAddress2_Type())
xgs360026fSMTPEmailAddress2.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSMTPEmailAddress2.setStatus(_A)
_Xgs360026fSMTPEmailAddress3_Type=DisplayString
_Xgs360026fSMTPEmailAddress3_Object=MibScalar
xgs360026fSMTPEmailAddress3=_Xgs360026fSMTPEmailAddress3_Object((1,3,6,1,4,1,890,1,5,8,77,2,8,9),_Xgs360026fSMTPEmailAddress3_Type())
xgs360026fSMTPEmailAddress3.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSMTPEmailAddress3.setStatus(_A)
_Xgs360026fSMTPEmailAddress4_Type=DisplayString
_Xgs360026fSMTPEmailAddress4_Object=MibScalar
xgs360026fSMTPEmailAddress4=_Xgs360026fSMTPEmailAddress4_Object((1,3,6,1,4,1,890,1,5,8,77,2,8,10),_Xgs360026fSMTPEmailAddress4_Type())
xgs360026fSMTPEmailAddress4.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSMTPEmailAddress4.setStatus(_A)
_Xgs360026fSMTPEmailAddress5_Type=DisplayString
_Xgs360026fSMTPEmailAddress5_Object=MibScalar
xgs360026fSMTPEmailAddress5=_Xgs360026fSMTPEmailAddress5_Object((1,3,6,1,4,1,890,1,5,8,77,2,8,11),_Xgs360026fSMTPEmailAddress5_Type())
xgs360026fSMTPEmailAddress5.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSMTPEmailAddress5.setStatus(_A)
_Xgs360026fSMTPEmailAddress6_Type=DisplayString
_Xgs360026fSMTPEmailAddress6_Object=MibScalar
xgs360026fSMTPEmailAddress6=_Xgs360026fSMTPEmailAddress6_Object((1,3,6,1,4,1,890,1,5,8,77,2,8,12),_Xgs360026fSMTPEmailAddress6_Type())
xgs360026fSMTPEmailAddress6.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSMTPEmailAddress6.setStatus(_A)
_Xgs360026fACL_ObjectIdentity=ObjectIdentity
xgs360026fACL=_Xgs360026fACL_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,9))
_Xgs360026fACLPortsConfTable_Object=MibTable
xgs360026fACLPortsConfTable=_Xgs360026fACLPortsConfTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,1))
if mibBuilder.loadTexts:xgs360026fACLPortsConfTable.setStatus(_A)
_Xgs360026fACLPortsConfEntry_Object=MibTableRow
xgs360026fACLPortsConfEntry=_Xgs360026fACLPortsConfEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,1,1))
xgs360026fACLPortsConfEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:xgs360026fACLPortsConfEntry.setStatus(_A)
class _Xgs360026fACLPortsConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fACLPortsConfPort_Type.__name__=_B
_Xgs360026fACLPortsConfPort_Object=MibTableColumn
xgs360026fACLPortsConfPort=_Xgs360026fACLPortsConfPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,1,1,1),_Xgs360026fACLPortsConfPort_Type())
xgs360026fACLPortsConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fACLPortsConfPort.setStatus(_A)
class _Xgs360026fACLPortsConfPolicyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360026fACLPortsConfPolicyID_Type.__name__=_B
_Xgs360026fACLPortsConfPolicyID_Object=MibTableColumn
xgs360026fACLPortsConfPolicyID=_Xgs360026fACLPortsConfPolicyID_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,1,1,2),_Xgs360026fACLPortsConfPolicyID_Type())
xgs360026fACLPortsConfPolicyID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLPortsConfPolicyID.setStatus(_A)
class _Xgs360026fACLPortsConfAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fACLPortsConfAction_Type.__name__=_B
_Xgs360026fACLPortsConfAction_Object=MibTableColumn
xgs360026fACLPortsConfAction=_Xgs360026fACLPortsConfAction_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,1,1,3),_Xgs360026fACLPortsConfAction_Type())
xgs360026fACLPortsConfAction.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLPortsConfAction.setStatus(_A)
class _Xgs360026fACLPortsConfRateLimiterID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_Xgs360026fACLPortsConfRateLimiterID_Type.__name__=_B
_Xgs360026fACLPortsConfRateLimiterID_Object=MibTableColumn
xgs360026fACLPortsConfRateLimiterID=_Xgs360026fACLPortsConfRateLimiterID_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,1,1,4),_Xgs360026fACLPortsConfRateLimiterID_Type())
xgs360026fACLPortsConfRateLimiterID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLPortsConfRateLimiterID.setStatus(_A)
class _Xgs360026fACLPortsConfPortRedirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_Xgs360026fACLPortsConfPortRedirect_Type.__name__=_B
_Xgs360026fACLPortsConfPortRedirect_Object=MibTableColumn
xgs360026fACLPortsConfPortRedirect=_Xgs360026fACLPortsConfPortRedirect_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,1,1,5),_Xgs360026fACLPortsConfPortRedirect_Type())
xgs360026fACLPortsConfPortRedirect.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLPortsConfPortRedirect.setStatus(_A)
class _Xgs360026fACLPortsConfLogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fACLPortsConfLogging_Type.__name__=_B
_Xgs360026fACLPortsConfLogging_Object=MibTableColumn
xgs360026fACLPortsConfLogging=_Xgs360026fACLPortsConfLogging_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,1,1,7),_Xgs360026fACLPortsConfLogging_Type())
xgs360026fACLPortsConfLogging.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLPortsConfLogging.setStatus(_A)
class _Xgs360026fACLPortsConfShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fACLPortsConfShutdown_Type.__name__=_B
_Xgs360026fACLPortsConfShutdown_Object=MibTableColumn
xgs360026fACLPortsConfShutdown=_Xgs360026fACLPortsConfShutdown_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,1,1,8),_Xgs360026fACLPortsConfShutdown_Type())
xgs360026fACLPortsConfShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLPortsConfShutdown.setStatus(_A)
class _Xgs360026fACLPortsConfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fACLPortsConfState_Type.__name__=_B
_Xgs360026fACLPortsConfState_Object=MibTableColumn
xgs360026fACLPortsConfState=_Xgs360026fACLPortsConfState_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,1,1,9),_Xgs360026fACLPortsConfState_Type())
xgs360026fACLPortsConfState.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLPortsConfState.setStatus(_A)
_Xgs360026fACLPortsConfCounter_Type=Counter32
_Xgs360026fACLPortsConfCounter_Object=MibTableColumn
xgs360026fACLPortsConfCounter=_Xgs360026fACLPortsConfCounter_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,1,1,10),_Xgs360026fACLPortsConfCounter_Type())
xgs360026fACLPortsConfCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fACLPortsConfCounter.setStatus(_A)
_Xgs360026fACLRateLimiterTable_Object=MibTable
xgs360026fACLRateLimiterTable=_Xgs360026fACLRateLimiterTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,2))
if mibBuilder.loadTexts:xgs360026fACLRateLimiterTable.setStatus(_A)
_Xgs360026fACLRateLimiterEntry_Object=MibTableRow
xgs360026fACLRateLimiterEntry=_Xgs360026fACLRateLimiterEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,2,1))
xgs360026fACLRateLimiterEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:xgs360026fACLRateLimiterEntry.setStatus(_A)
class _Xgs360026fACLRateLimiterID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Xgs360026fACLRateLimiterID_Type.__name__=_B
_Xgs360026fACLRateLimiterID_Object=MibTableColumn
xgs360026fACLRateLimiterID=_Xgs360026fACLRateLimiterID_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,2,1,1),_Xgs360026fACLRateLimiterID_Type())
xgs360026fACLRateLimiterID.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fACLRateLimiterID.setStatus(_A)
class _Xgs360026fACLRateLimiterRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3276700))
_Xgs360026fACLRateLimiterRate_Type.__name__=_B
_Xgs360026fACLRateLimiterRate_Object=MibTableColumn
xgs360026fACLRateLimiterRate=_Xgs360026fACLRateLimiterRate_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,2,1,3),_Xgs360026fACLRateLimiterRate_Type())
xgs360026fACLRateLimiterRate.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLRateLimiterRate.setStatus(_A)
_Xgs360026fACLACE_ObjectIdentity=ObjectIdentity
xgs360026fACLACE=_Xgs360026fACLACE_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,9,3))
class _Xgs360026fACLACECreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fACLACECreate_Type.__name__=_B
_Xgs360026fACLACECreate_Object=MibScalar
xgs360026fACLACECreate=_Xgs360026fACLACECreate_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,1),_Xgs360026fACLACECreate_Type())
xgs360026fACLACECreate.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACECreate.setStatus(_A)
_Xgs360026fACLACETable_Object=MibTable
xgs360026fACLACETable=_Xgs360026fACLACETable_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2))
if mibBuilder.loadTexts:xgs360026fACLACETable.setStatus(_A)
_Xgs360026fACLACEEntry_Object=MibTableRow
xgs360026fACLACEEntry=_Xgs360026fACLACEEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1))
xgs360026fACLACEEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:xgs360026fACLACEEntry.setStatus(_A)
class _Xgs360026fACLACEIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Xgs360026fACLACEIndex_Type.__name__=_B
_Xgs360026fACLACEIndex_Object=MibTableColumn
xgs360026fACLACEIndex=_Xgs360026fACLACEIndex_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,1),_Xgs360026fACLACEIndex_Type())
xgs360026fACLACEIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fACLACEIndex.setStatus(_A)
class _Xgs360026fACLACEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Xgs360026fACLACEID_Type.__name__=_B
_Xgs360026fACLACEID_Object=MibTableColumn
xgs360026fACLACEID=_Xgs360026fACLACEID_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,2),_Xgs360026fACLACEID_Type())
xgs360026fACLACEID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEID.setStatus(_A)
class _Xgs360026fACLACENextID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Xgs360026fACLACENextID_Type.__name__=_B
_Xgs360026fACLACENextID_Object=MibTableColumn
xgs360026fACLACENextID=_Xgs360026fACLACENextID_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,3),_Xgs360026fACLACENextID_Type())
xgs360026fACLACENextID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACENextID.setStatus(_A)
_Xgs360026fACLACEIngressPort_Type=DisplayString
_Xgs360026fACLACEIngressPort_Object=MibTableColumn
xgs360026fACLACEIngressPort=_Xgs360026fACLACEIngressPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,4),_Xgs360026fACLACEIngressPort_Type())
xgs360026fACLACEIngressPort.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEIngressPort.setStatus(_A)
class _Xgs360026fACLACEPortPolicyNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360026fACLACEPortPolicyNumber_Type.__name__=_B
_Xgs360026fACLACEPortPolicyNumber_Object=MibTableColumn
xgs360026fACLACEPortPolicyNumber=_Xgs360026fACLACEPortPolicyNumber_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,5),_Xgs360026fACLACEPortPolicyNumber_Type())
xgs360026fACLACEPortPolicyNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEPortPolicyNumber.setStatus(_A)
class _Xgs360026fACLACEPortPolicyBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360026fACLACEPortPolicyBitmask_Type.__name__=_B
_Xgs360026fACLACEPortPolicyBitmask_Object=MibTableColumn
xgs360026fACLACEPortPolicyBitmask=_Xgs360026fACLACEPortPolicyBitmask_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,6),_Xgs360026fACLACEPortPolicyBitmask_Type())
xgs360026fACLACEPortPolicyBitmask.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEPortPolicyBitmask.setStatus(_A)
class _Xgs360026fACLACEFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_Xgs360026fACLACEFrameType_Type.__name__=_B
_Xgs360026fACLACEFrameType_Object=MibTableColumn
xgs360026fACLACEFrameType=_Xgs360026fACLACEFrameType_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,7),_Xgs360026fACLACEFrameType_Type())
xgs360026fACLACEFrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEFrameType.setStatus(_A)
class _Xgs360026fACLACEAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fACLACEAction_Type.__name__=_B
_Xgs360026fACLACEAction_Object=MibTableColumn
xgs360026fACLACEAction=_Xgs360026fACLACEAction_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,8),_Xgs360026fACLACEAction_Type())
xgs360026fACLACEAction.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEAction.setStatus(_A)
_Xgs360026fACLACEDenyPortRedirect_Type=DisplayString
_Xgs360026fACLACEDenyPortRedirect_Object=MibTableColumn
xgs360026fACLACEDenyPortRedirect=_Xgs360026fACLACEDenyPortRedirect_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,9),_Xgs360026fACLACEDenyPortRedirect_Type())
xgs360026fACLACEDenyPortRedirect.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEDenyPortRedirect.setStatus(_A)
class _Xgs360026fACLACELogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fACLACELogging_Type.__name__=_B
_Xgs360026fACLACELogging_Object=MibTableColumn
xgs360026fACLACELogging=_Xgs360026fACLACELogging_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,10),_Xgs360026fACLACELogging_Type())
xgs360026fACLACELogging.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACELogging.setStatus(_A)
class _Xgs360026fACLACERateLimiter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_Xgs360026fACLACERateLimiter_Type.__name__=_B
_Xgs360026fACLACERateLimiter_Object=MibTableColumn
xgs360026fACLACERateLimiter=_Xgs360026fACLACERateLimiter_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,12),_Xgs360026fACLACERateLimiter_Type())
xgs360026fACLACERateLimiter.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACERateLimiter.setStatus(_A)
class _Xgs360026fACLACEShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fACLACEShutdown_Type.__name__=_B
_Xgs360026fACLACEShutdown_Object=MibTableColumn
xgs360026fACLACEShutdown=_Xgs360026fACLACEShutdown_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,13),_Xgs360026fACLACEShutdown_Type())
xgs360026fACLACEShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEShutdown.setStatus(_A)
class _Xgs360026fACLACEVLANTagPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_Xgs360026fACLACEVLANTagPriority_Type.__name__=_B
_Xgs360026fACLACEVLANTagPriority_Object=MibTableColumn
xgs360026fACLACEVLANTagPriority=_Xgs360026fACLACEVLANTagPriority_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,15),_Xgs360026fACLACEVLANTagPriority_Type())
xgs360026fACLACEVLANTagPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEVLANTagPriority.setStatus(_A)
class _Xgs360026fACLACEVLANVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Xgs360026fACLACEVLANVID_Type.__name__=_B
_Xgs360026fACLACEVLANVID_Object=MibTableColumn
xgs360026fACLACEVLANVID=_Xgs360026fACLACEVLANVID_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,16),_Xgs360026fACLACEVLANVID_Type())
xgs360026fACLACEVLANVID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEVLANVID.setStatus(_A)
class _Xgs360026fACLACEEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Xgs360026fACLACEEtherType_Type.__name__=_B
_Xgs360026fACLACEEtherType_Object=MibTableColumn
xgs360026fACLACEEtherType=_Xgs360026fACLACEEtherType_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,17),_Xgs360026fACLACEEtherType_Type())
xgs360026fACLACEEtherType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEEtherType.setStatus(_A)
_Xgs360026fACLACESMAC_Type=DisplayString
_Xgs360026fACLACESMAC_Object=MibTableColumn
xgs360026fACLACESMAC=_Xgs360026fACLACESMAC_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,18),_Xgs360026fACLACESMAC_Type())
xgs360026fACLACESMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACESMAC.setStatus(_A)
class _Xgs360026fACLACEDMACType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Xgs360026fACLACEDMACType_Type.__name__=_B
_Xgs360026fACLACEDMACType_Object=MibTableColumn
xgs360026fACLACEDMACType=_Xgs360026fACLACEDMACType_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,19),_Xgs360026fACLACEDMACType_Type())
xgs360026fACLACEDMACType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEDMACType.setStatus(_A)
_Xgs360026fACLACEDMAC_Type=DisplayString
_Xgs360026fACLACEDMAC_Object=MibTableColumn
xgs360026fACLACEDMAC=_Xgs360026fACLACEDMAC_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,20),_Xgs360026fACLACEDMAC_Type())
xgs360026fACLACEDMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEDMAC.setStatus(_A)
class _Xgs360026fACLACEArpOpcode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360026fACLACEArpOpcode_Type.__name__=_B
_Xgs360026fACLACEArpOpcode_Object=MibTableColumn
xgs360026fACLACEArpOpcode=_Xgs360026fACLACEArpOpcode_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,21),_Xgs360026fACLACEArpOpcode_Type())
xgs360026fACLACEArpOpcode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEArpOpcode.setStatus(_A)
class _Xgs360026fACLACEArpFlagsRequestReply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fACLACEArpFlagsRequestReply_Type.__name__=_B
_Xgs360026fACLACEArpFlagsRequestReply_Object=MibTableColumn
xgs360026fACLACEArpFlagsRequestReply=_Xgs360026fACLACEArpFlagsRequestReply_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,22),_Xgs360026fACLACEArpFlagsRequestReply_Type())
xgs360026fACLACEArpFlagsRequestReply.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEArpFlagsRequestReply.setStatus(_A)
class _Xgs360026fACLACEArpFlagsArpSmac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fACLACEArpFlagsArpSmac_Type.__name__=_B
_Xgs360026fACLACEArpFlagsArpSmac_Object=MibTableColumn
xgs360026fACLACEArpFlagsArpSmac=_Xgs360026fACLACEArpFlagsArpSmac_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,23),_Xgs360026fACLACEArpFlagsArpSmac_Type())
xgs360026fACLACEArpFlagsArpSmac.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEArpFlagsArpSmac.setStatus(_A)
class _Xgs360026fACLACEArpFlagsRarpDmac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fACLACEArpFlagsRarpDmac_Type.__name__=_B
_Xgs360026fACLACEArpFlagsRarpDmac_Object=MibTableColumn
xgs360026fACLACEArpFlagsRarpDmac=_Xgs360026fACLACEArpFlagsRarpDmac_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,24),_Xgs360026fACLACEArpFlagsRarpDmac_Type())
xgs360026fACLACEArpFlagsRarpDmac.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEArpFlagsRarpDmac.setStatus(_A)
class _Xgs360026fACLACEArpFlagsLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fACLACEArpFlagsLength_Type.__name__=_B
_Xgs360026fACLACEArpFlagsLength_Object=MibTableColumn
xgs360026fACLACEArpFlagsLength=_Xgs360026fACLACEArpFlagsLength_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,25),_Xgs360026fACLACEArpFlagsLength_Type())
xgs360026fACLACEArpFlagsLength.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEArpFlagsLength.setStatus(_A)
class _Xgs360026fACLACEArpFlagsIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fACLACEArpFlagsIp_Type.__name__=_B
_Xgs360026fACLACEArpFlagsIp_Object=MibTableColumn
xgs360026fACLACEArpFlagsIp=_Xgs360026fACLACEArpFlagsIp_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,26),_Xgs360026fACLACEArpFlagsIp_Type())
xgs360026fACLACEArpFlagsIp.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEArpFlagsIp.setStatus(_A)
class _Xgs360026fACLACEArpFlagsEthernet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fACLACEArpFlagsEthernet_Type.__name__=_B
_Xgs360026fACLACEArpFlagsEthernet_Object=MibTableColumn
xgs360026fACLACEArpFlagsEthernet=_Xgs360026fACLACEArpFlagsEthernet_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,27),_Xgs360026fACLACEArpFlagsEthernet_Type())
xgs360026fACLACEArpFlagsEthernet.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEArpFlagsEthernet.setStatus(_A)
class _Xgs360026fACLACESIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fACLACESIPType_Type.__name__=_B
_Xgs360026fACLACESIPType_Object=MibTableColumn
xgs360026fACLACESIPType=_Xgs360026fACLACESIPType_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,28),_Xgs360026fACLACESIPType_Type())
xgs360026fACLACESIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACESIPType.setStatus(_A)
_Xgs360026fACLACESIPIPAddress_Type=IpAddress
_Xgs360026fACLACESIPIPAddress_Object=MibTableColumn
xgs360026fACLACESIPIPAddress=_Xgs360026fACLACESIPIPAddress_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,29),_Xgs360026fACLACESIPIPAddress_Type())
xgs360026fACLACESIPIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACESIPIPAddress.setStatus(_A)
class _Xgs360026fACLACESIPNetworkPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Xgs360026fACLACESIPNetworkPrefix_Type.__name__=_B
_Xgs360026fACLACESIPNetworkPrefix_Object=MibTableColumn
xgs360026fACLACESIPNetworkPrefix=_Xgs360026fACLACESIPNetworkPrefix_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,30),_Xgs360026fACLACESIPNetworkPrefix_Type())
xgs360026fACLACESIPNetworkPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACESIPNetworkPrefix.setStatus(_A)
class _Xgs360026fACLACEDIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fACLACEDIPType_Type.__name__=_B
_Xgs360026fACLACEDIPType_Object=MibTableColumn
xgs360026fACLACEDIPType=_Xgs360026fACLACEDIPType_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,32),_Xgs360026fACLACEDIPType_Type())
xgs360026fACLACEDIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEDIPType.setStatus(_A)
_Xgs360026fACLACEDIPIPAddress_Type=IpAddress
_Xgs360026fACLACEDIPIPAddress_Object=MibTableColumn
xgs360026fACLACEDIPIPAddress=_Xgs360026fACLACEDIPIPAddress_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,33),_Xgs360026fACLACEDIPIPAddress_Type())
xgs360026fACLACEDIPIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEDIPIPAddress.setStatus(_A)
class _Xgs360026fACLACEDIPNetworkPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Xgs360026fACLACEDIPNetworkPrefix_Type.__name__=_B
_Xgs360026fACLACEDIPNetworkPrefix_Object=MibTableColumn
xgs360026fACLACEDIPNetworkPrefix=_Xgs360026fACLACEDIPNetworkPrefix_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,34),_Xgs360026fACLACEDIPNetworkPrefix_Type())
xgs360026fACLACEDIPNetworkPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEDIPNetworkPrefix.setStatus(_A)
class _Xgs360026fACLACEIPProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Xgs360026fACLACEIPProtocol_Type.__name__=_B
_Xgs360026fACLACEIPProtocol_Object=MibTableColumn
xgs360026fACLACEIPProtocol=_Xgs360026fACLACEIPProtocol_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,36),_Xgs360026fACLACEIPProtocol_Type())
xgs360026fACLACEIPProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEIPProtocol.setStatus(_A)
class _Xgs360026fACLACEIPFlagsTTL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fACLACEIPFlagsTTL_Type.__name__=_B
_Xgs360026fACLACEIPFlagsTTL_Object=MibTableColumn
xgs360026fACLACEIPFlagsTTL=_Xgs360026fACLACEIPFlagsTTL_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,37),_Xgs360026fACLACEIPFlagsTTL_Type())
xgs360026fACLACEIPFlagsTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEIPFlagsTTL.setStatus(_A)
class _Xgs360026fACLACEIPFlagsOptions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fACLACEIPFlagsOptions_Type.__name__=_B
_Xgs360026fACLACEIPFlagsOptions_Object=MibTableColumn
xgs360026fACLACEIPFlagsOptions=_Xgs360026fACLACEIPFlagsOptions_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,38),_Xgs360026fACLACEIPFlagsOptions_Type())
xgs360026fACLACEIPFlagsOptions.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEIPFlagsOptions.setStatus(_A)
class _Xgs360026fACLACEIPFlagsFragment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fACLACEIPFlagsFragment_Type.__name__=_B
_Xgs360026fACLACEIPFlagsFragment_Object=MibTableColumn
xgs360026fACLACEIPFlagsFragment=_Xgs360026fACLACEIPFlagsFragment_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,39),_Xgs360026fACLACEIPFlagsFragment_Type())
xgs360026fACLACEIPFlagsFragment.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEIPFlagsFragment.setStatus(_A)
class _Xgs360026fACLACEICMPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Xgs360026fACLACEICMPType_Type.__name__=_B
_Xgs360026fACLACEICMPType_Object=MibTableColumn
xgs360026fACLACEICMPType=_Xgs360026fACLACEICMPType_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,40),_Xgs360026fACLACEICMPType_Type())
xgs360026fACLACEICMPType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEICMPType.setStatus(_A)
class _Xgs360026fACLACEICMPCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Xgs360026fACLACEICMPCode_Type.__name__=_B
_Xgs360026fACLACEICMPCode_Object=MibTableColumn
xgs360026fACLACEICMPCode=_Xgs360026fACLACEICMPCode_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,41),_Xgs360026fACLACEICMPCode_Type())
xgs360026fACLACEICMPCode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEICMPCode.setStatus(_A)
class _Xgs360026fACLACESourcePortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Xgs360026fACLACESourcePortMin_Type.__name__=_B
_Xgs360026fACLACESourcePortMin_Object=MibTableColumn
xgs360026fACLACESourcePortMin=_Xgs360026fACLACESourcePortMin_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,42),_Xgs360026fACLACESourcePortMin_Type())
xgs360026fACLACESourcePortMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACESourcePortMin.setStatus(_A)
class _Xgs360026fACLACESourcePortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Xgs360026fACLACESourcePortMax_Type.__name__=_B
_Xgs360026fACLACESourcePortMax_Object=MibTableColumn
xgs360026fACLACESourcePortMax=_Xgs360026fACLACESourcePortMax_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,43),_Xgs360026fACLACESourcePortMax_Type())
xgs360026fACLACESourcePortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACESourcePortMax.setStatus(_A)
class _Xgs360026fACLACEDestPortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Xgs360026fACLACEDestPortMin_Type.__name__=_B
_Xgs360026fACLACEDestPortMin_Object=MibTableColumn
xgs360026fACLACEDestPortMin=_Xgs360026fACLACEDestPortMin_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,44),_Xgs360026fACLACEDestPortMin_Type())
xgs360026fACLACEDestPortMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEDestPortMin.setStatus(_A)
class _Xgs360026fACLACEDestPortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Xgs360026fACLACEDestPortMax_Type.__name__=_B
_Xgs360026fACLACEDestPortMax_Object=MibTableColumn
xgs360026fACLACEDestPortMax=_Xgs360026fACLACEDestPortMax_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,45),_Xgs360026fACLACEDestPortMax_Type())
xgs360026fACLACEDestPortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEDestPortMax.setStatus(_A)
class _Xgs360026fACLACETCPFlagsFin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fACLACETCPFlagsFin_Type.__name__=_B
_Xgs360026fACLACETCPFlagsFin_Object=MibTableColumn
xgs360026fACLACETCPFlagsFin=_Xgs360026fACLACETCPFlagsFin_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,46),_Xgs360026fACLACETCPFlagsFin_Type())
xgs360026fACLACETCPFlagsFin.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACETCPFlagsFin.setStatus(_A)
class _Xgs360026fACLACETCPFlagsSyn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fACLACETCPFlagsSyn_Type.__name__=_B
_Xgs360026fACLACETCPFlagsSyn_Object=MibTableColumn
xgs360026fACLACETCPFlagsSyn=_Xgs360026fACLACETCPFlagsSyn_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,47),_Xgs360026fACLACETCPFlagsSyn_Type())
xgs360026fACLACETCPFlagsSyn.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACETCPFlagsSyn.setStatus(_A)
class _Xgs360026fACLACETCPFlagsRst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fACLACETCPFlagsRst_Type.__name__=_B
_Xgs360026fACLACETCPFlagsRst_Object=MibTableColumn
xgs360026fACLACETCPFlagsRst=_Xgs360026fACLACETCPFlagsRst_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,48),_Xgs360026fACLACETCPFlagsRst_Type())
xgs360026fACLACETCPFlagsRst.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACETCPFlagsRst.setStatus(_A)
class _Xgs360026fACLACETCPFlagsPsh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fACLACETCPFlagsPsh_Type.__name__=_B
_Xgs360026fACLACETCPFlagsPsh_Object=MibTableColumn
xgs360026fACLACETCPFlagsPsh=_Xgs360026fACLACETCPFlagsPsh_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,49),_Xgs360026fACLACETCPFlagsPsh_Type())
xgs360026fACLACETCPFlagsPsh.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACETCPFlagsPsh.setStatus(_A)
class _Xgs360026fACLACETCPFlagsAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fACLACETCPFlagsAck_Type.__name__=_B
_Xgs360026fACLACETCPFlagsAck_Object=MibTableColumn
xgs360026fACLACETCPFlagsAck=_Xgs360026fACLACETCPFlagsAck_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,50),_Xgs360026fACLACETCPFlagsAck_Type())
xgs360026fACLACETCPFlagsAck.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACETCPFlagsAck.setStatus(_A)
class _Xgs360026fACLACETCPFlagsUrg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fACLACETCPFlagsUrg_Type.__name__=_B
_Xgs360026fACLACETCPFlagsUrg_Object=MibTableColumn
xgs360026fACLACETCPFlagsUrg=_Xgs360026fACLACETCPFlagsUrg_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,51),_Xgs360026fACLACETCPFlagsUrg_Type())
xgs360026fACLACETCPFlagsUrg.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACETCPFlagsUrg.setStatus(_A)
class _Xgs360026fACLACERowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360026fACLACERowStatus_Type.__name__=_B
_Xgs360026fACLACERowStatus_Object=MibTableColumn
xgs360026fACLACERowStatus=_Xgs360026fACLACERowStatus_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,2,1,66),_Xgs360026fACLACERowStatus_Type())
xgs360026fACLACERowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACERowStatus.setStatus(_A)
class _Xgs360026fACLACEClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fACLACEClear_Type.__name__=_B
_Xgs360026fACLACEClear_Object=MibScalar
xgs360026fACLACEClear=_Xgs360026fACLACEClear_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,3),_Xgs360026fACLACEClear_Type())
xgs360026fACLACEClear.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEClear.setStatus(_A)
class _Xgs360026fACLACEMoveACEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Xgs360026fACLACEMoveACEID_Type.__name__=_B
_Xgs360026fACLACEMoveACEID_Object=MibScalar
xgs360026fACLACEMoveACEID=_Xgs360026fACLACEMoveACEID_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,4),_Xgs360026fACLACEMoveACEID_Type())
xgs360026fACLACEMoveACEID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEMoveACEID.setStatus(_A)
class _Xgs360026fACLACEMoveNextACEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Xgs360026fACLACEMoveNextACEID_Type.__name__=_B
_Xgs360026fACLACEMoveNextACEID_Object=MibScalar
xgs360026fACLACEMoveNextACEID=_Xgs360026fACLACEMoveNextACEID_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,5),_Xgs360026fACLACEMoveNextACEID_Type())
xgs360026fACLACEMoveNextACEID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fACLACEMoveNextACEID.setStatus(_A)
_Xgs360026fACLACEStatusTable_Object=MibTable
xgs360026fACLACEStatusTable=_Xgs360026fACLACEStatusTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,6))
if mibBuilder.loadTexts:xgs360026fACLACEStatusTable.setStatus(_A)
_Xgs360026fACLACEStatusEntry_Object=MibTableRow
xgs360026fACLACEStatusEntry=_Xgs360026fACLACEStatusEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,6,1))
xgs360026fACLACEStatusEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:xgs360026fACLACEStatusEntry.setStatus(_A)
class _Xgs360026fACLACEStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Xgs360026fACLACEStatusIndex_Type.__name__=_B
_Xgs360026fACLACEStatusIndex_Object=MibTableColumn
xgs360026fACLACEStatusIndex=_Xgs360026fACLACEStatusIndex_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,6,1,1),_Xgs360026fACLACEStatusIndex_Type())
xgs360026fACLACEStatusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fACLACEStatusIndex.setStatus(_A)
_Xgs360026fACLACEStatusUser_Type=DisplayString
_Xgs360026fACLACEStatusUser_Object=MibTableColumn
xgs360026fACLACEStatusUser=_Xgs360026fACLACEStatusUser_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,6,1,2),_Xgs360026fACLACEStatusUser_Type())
xgs360026fACLACEStatusUser.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fACLACEStatusUser.setStatus(_A)
class _Xgs360026fACLACEStatusID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Xgs360026fACLACEStatusID_Type.__name__=_B
_Xgs360026fACLACEStatusID_Object=MibTableColumn
xgs360026fACLACEStatusID=_Xgs360026fACLACEStatusID_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,6,1,3),_Xgs360026fACLACEStatusID_Type())
xgs360026fACLACEStatusID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fACLACEStatusID.setStatus(_A)
_Xgs360026fACLACEStatusIngressPort_Type=DisplayString
_Xgs360026fACLACEStatusIngressPort_Object=MibTableColumn
xgs360026fACLACEStatusIngressPort=_Xgs360026fACLACEStatusIngressPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,6,1,4),_Xgs360026fACLACEStatusIngressPort_Type())
xgs360026fACLACEStatusIngressPort.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fACLACEStatusIngressPort.setStatus(_A)
_Xgs360026fACLACEStatusFrameType_Type=DisplayString
_Xgs360026fACLACEStatusFrameType_Object=MibTableColumn
xgs360026fACLACEStatusFrameType=_Xgs360026fACLACEStatusFrameType_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,6,1,5),_Xgs360026fACLACEStatusFrameType_Type())
xgs360026fACLACEStatusFrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fACLACEStatusFrameType.setStatus(_A)
_Xgs360026fACLACEStatusAction_Type=DisplayString
_Xgs360026fACLACEStatusAction_Object=MibTableColumn
xgs360026fACLACEStatusAction=_Xgs360026fACLACEStatusAction_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,6,1,6),_Xgs360026fACLACEStatusAction_Type())
xgs360026fACLACEStatusAction.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fACLACEStatusAction.setStatus(_A)
_Xgs360026fACLACEStatusRateLimiter_Type=DisplayString
_Xgs360026fACLACEStatusRateLimiter_Object=MibTableColumn
xgs360026fACLACEStatusRateLimiter=_Xgs360026fACLACEStatusRateLimiter_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,6,1,7),_Xgs360026fACLACEStatusRateLimiter_Type())
xgs360026fACLACEStatusRateLimiter.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fACLACEStatusRateLimiter.setStatus(_A)
_Xgs360026fACLACEStatusPortCopy_Type=DisplayString
_Xgs360026fACLACEStatusPortCopy_Object=MibTableColumn
xgs360026fACLACEStatusPortCopy=_Xgs360026fACLACEStatusPortCopy_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,6,1,8),_Xgs360026fACLACEStatusPortCopy_Type())
xgs360026fACLACEStatusPortCopy.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fACLACEStatusPortCopy.setStatus(_A)
_Xgs360026fACLACEStatusMirror_Type=DisplayString
_Xgs360026fACLACEStatusMirror_Object=MibTableColumn
xgs360026fACLACEStatusMirror=_Xgs360026fACLACEStatusMirror_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,6,1,9),_Xgs360026fACLACEStatusMirror_Type())
xgs360026fACLACEStatusMirror.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fACLACEStatusMirror.setStatus(_A)
_Xgs360026fACLACEStatusCPU_Type=DisplayString
_Xgs360026fACLACEStatusCPU_Object=MibTableColumn
xgs360026fACLACEStatusCPU=_Xgs360026fACLACEStatusCPU_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,6,1,10),_Xgs360026fACLACEStatusCPU_Type())
xgs360026fACLACEStatusCPU.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fACLACEStatusCPU.setStatus(_A)
_Xgs360026fACLACEStatusCounter_Type=Counter32
_Xgs360026fACLACEStatusCounter_Object=MibTableColumn
xgs360026fACLACEStatusCounter=_Xgs360026fACLACEStatusCounter_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,6,1,11),_Xgs360026fACLACEStatusCounter_Type())
xgs360026fACLACEStatusCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fACLACEStatusCounter.setStatus(_A)
_Xgs360026fACLACEStatusConflict_Type=DisplayString
_Xgs360026fACLACEStatusConflict_Object=MibTableColumn
xgs360026fACLACEStatusConflict=_Xgs360026fACLACEStatusConflict_Object((1,3,6,1,4,1,890,1,5,8,77,2,9,3,6,1,12),_Xgs360026fACLACEStatusConflict_Type())
xgs360026fACLACEStatusConflict.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fACLACEStatusConflict.setStatus(_A)
_Xgs360026fERPS_ObjectIdentity=ObjectIdentity
xgs360026fERPS=_Xgs360026fERPS_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,10))
_Xgs360026fERPSConf_ObjectIdentity=ObjectIdentity
xgs360026fERPSConf=_Xgs360026fERPSConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,10,1))
class _Xgs360026fERPSConfCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fERPSConfCreate_Type.__name__=_B
_Xgs360026fERPSConfCreate_Object=MibScalar
xgs360026fERPSConfCreate=_Xgs360026fERPSConfCreate_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,1),_Xgs360026fERPSConfCreate_Type())
xgs360026fERPSConfCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSConfCreate.setStatus(_A)
_Xgs360026fERPSConfTable_Object=MibTable
xgs360026fERPSConfTable=_Xgs360026fERPSConfTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2))
if mibBuilder.loadTexts:xgs360026fERPSConfTable.setStatus(_A)
_Xgs360026fERPSConfEntry_Object=MibTableRow
xgs360026fERPSConfEntry=_Xgs360026fERPSConfEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1))
xgs360026fERPSConfEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:xgs360026fERPSConfEntry.setStatus(_A)
class _Xgs360026fERPSConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Xgs360026fERPSConfIndex_Type.__name__=_B
_Xgs360026fERPSConfIndex_Object=MibTableColumn
xgs360026fERPSConfIndex=_Xgs360026fERPSConfIndex_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,1),_Xgs360026fERPSConfIndex_Type())
xgs360026fERPSConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fERPSConfIndex.setStatus(_A)
class _Xgs360026fERPSConfERPSID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Xgs360026fERPSConfERPSID_Type.__name__=_B
_Xgs360026fERPSConfERPSID_Object=MibTableColumn
xgs360026fERPSConfERPSID=_Xgs360026fERPSConfERPSID_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,2),_Xgs360026fERPSConfERPSID_Type())
xgs360026fERPSConfERPSID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSConfERPSID.setStatus(_A)
class _Xgs360026fERPSConfPort0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Xgs360026fERPSConfPort0_Type.__name__=_B
_Xgs360026fERPSConfPort0_Object=MibTableColumn
xgs360026fERPSConfPort0=_Xgs360026fERPSConfPort0_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,3),_Xgs360026fERPSConfPort0_Type())
xgs360026fERPSConfPort0.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSConfPort0.setStatus(_A)
class _Xgs360026fERPSConfPort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,26))
_Xgs360026fERPSConfPort1_Type.__name__=_B
_Xgs360026fERPSConfPort1_Object=MibTableColumn
xgs360026fERPSConfPort1=_Xgs360026fERPSConfPort1_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,4),_Xgs360026fERPSConfPort1_Type())
xgs360026fERPSConfPort1.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSConfPort1.setStatus(_A)
class _Xgs360026fERPSConfPort0SFMEP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Xgs360026fERPSConfPort0SFMEP_Type.__name__=_B
_Xgs360026fERPSConfPort0SFMEP_Object=MibTableColumn
xgs360026fERPSConfPort0SFMEP=_Xgs360026fERPSConfPort0SFMEP_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,5),_Xgs360026fERPSConfPort0SFMEP_Type())
xgs360026fERPSConfPort0SFMEP.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSConfPort0SFMEP.setStatus(_A)
class _Xgs360026fERPSConfPort1SFMEP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_Xgs360026fERPSConfPort1SFMEP_Type.__name__=_B
_Xgs360026fERPSConfPort1SFMEP_Object=MibTableColumn
xgs360026fERPSConfPort1SFMEP=_Xgs360026fERPSConfPort1SFMEP_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,6),_Xgs360026fERPSConfPort1SFMEP_Type())
xgs360026fERPSConfPort1SFMEP.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSConfPort1SFMEP.setStatus(_A)
class _Xgs360026fERPSConfPort0APSMEP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Xgs360026fERPSConfPort0APSMEP_Type.__name__=_B
_Xgs360026fERPSConfPort0APSMEP_Object=MibTableColumn
xgs360026fERPSConfPort0APSMEP=_Xgs360026fERPSConfPort0APSMEP_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,7),_Xgs360026fERPSConfPort0APSMEP_Type())
xgs360026fERPSConfPort0APSMEP.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSConfPort0APSMEP.setStatus(_A)
class _Xgs360026fERPSConfPort1APSMEP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_Xgs360026fERPSConfPort1APSMEP_Type.__name__=_B
_Xgs360026fERPSConfPort1APSMEP_Object=MibTableColumn
xgs360026fERPSConfPort1APSMEP=_Xgs360026fERPSConfPort1APSMEP_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,8),_Xgs360026fERPSConfPort1APSMEP_Type())
xgs360026fERPSConfPort1APSMEP.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSConfPort1APSMEP.setStatus(_A)
class _Xgs360026fERPSConfRingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fERPSConfRingType_Type.__name__=_B
_Xgs360026fERPSConfRingType_Object=MibTableColumn
xgs360026fERPSConfRingType=_Xgs360026fERPSConfRingType_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,9),_Xgs360026fERPSConfRingType_Type())
xgs360026fERPSConfRingType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSConfRingType.setStatus(_A)
class _Xgs360026fERPSConfInterconnectedNode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fERPSConfInterconnectedNode_Type.__name__=_B
_Xgs360026fERPSConfInterconnectedNode_Object=MibTableColumn
xgs360026fERPSConfInterconnectedNode=_Xgs360026fERPSConfInterconnectedNode_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,10),_Xgs360026fERPSConfInterconnectedNode_Type())
xgs360026fERPSConfInterconnectedNode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSConfInterconnectedNode.setStatus(_A)
class _Xgs360026fERPSConfVirtualChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fERPSConfVirtualChannel_Type.__name__=_B
_Xgs360026fERPSConfVirtualChannel_Object=MibTableColumn
xgs360026fERPSConfVirtualChannel=_Xgs360026fERPSConfVirtualChannel_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,11),_Xgs360026fERPSConfVirtualChannel_Type())
xgs360026fERPSConfVirtualChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSConfVirtualChannel.setStatus(_A)
class _Xgs360026fERPSConfMajorRingID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Xgs360026fERPSConfMajorRingID_Type.__name__=_B
_Xgs360026fERPSConfMajorRingID_Object=MibTableColumn
xgs360026fERPSConfMajorRingID=_Xgs360026fERPSConfMajorRingID_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,12),_Xgs360026fERPSConfMajorRingID_Type())
xgs360026fERPSConfMajorRingID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fERPSConfMajorRingID.setStatus(_A)
class _Xgs360026fERPSConfAlarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Xgs360026fERPSConfAlarm_Type.__name__=_G
_Xgs360026fERPSConfAlarm_Object=MibTableColumn
xgs360026fERPSConfAlarm=_Xgs360026fERPSConfAlarm_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,13),_Xgs360026fERPSConfAlarm_Type())
xgs360026fERPSConfAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fERPSConfAlarm.setStatus(_A)
class _Xgs360026fERPSInstanceConfConfigured_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Xgs360026fERPSInstanceConfConfigured_Type.__name__=_G
_Xgs360026fERPSInstanceConfConfigured_Object=MibTableColumn
xgs360026fERPSInstanceConfConfigured=_Xgs360026fERPSInstanceConfConfigured_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,14),_Xgs360026fERPSInstanceConfConfigured_Type())
xgs360026fERPSInstanceConfConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fERPSInstanceConfConfigured.setStatus(_A)
class _Xgs360026fERPSInstanceConfGuardTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,2000))
_Xgs360026fERPSInstanceConfGuardTime_Type.__name__=_B
_Xgs360026fERPSInstanceConfGuardTime_Object=MibTableColumn
xgs360026fERPSInstanceConfGuardTime=_Xgs360026fERPSInstanceConfGuardTime_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,15),_Xgs360026fERPSInstanceConfGuardTime_Type())
xgs360026fERPSInstanceConfGuardTime.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSInstanceConfGuardTime.setStatus(_A)
class _Xgs360026fERPSInstanceConfWTRTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Xgs360026fERPSInstanceConfWTRTime_Type.__name__=_B
_Xgs360026fERPSInstanceConfWTRTime_Object=MibTableColumn
xgs360026fERPSInstanceConfWTRTime=_Xgs360026fERPSInstanceConfWTRTime_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,16),_Xgs360026fERPSInstanceConfWTRTime_Type())
xgs360026fERPSInstanceConfWTRTime.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSInstanceConfWTRTime.setStatus(_A)
class _Xgs360026fERPSInstanceConfHoldOffTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Xgs360026fERPSInstanceConfHoldOffTime_Type.__name__=_B
_Xgs360026fERPSInstanceConfHoldOffTime_Object=MibTableColumn
xgs360026fERPSInstanceConfHoldOffTime=_Xgs360026fERPSInstanceConfHoldOffTime_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,17),_Xgs360026fERPSInstanceConfHoldOffTime_Type())
xgs360026fERPSInstanceConfHoldOffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSInstanceConfHoldOffTime.setStatus(_A)
class _Xgs360026fERPSInstanceConfVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fERPSInstanceConfVersion_Type.__name__=_B
_Xgs360026fERPSInstanceConfVersion_Object=MibTableColumn
xgs360026fERPSInstanceConfVersion=_Xgs360026fERPSInstanceConfVersion_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,18),_Xgs360026fERPSInstanceConfVersion_Type())
xgs360026fERPSInstanceConfVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSInstanceConfVersion.setStatus(_A)
class _Xgs360026fERPSInstanceConfRevertive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fERPSInstanceConfRevertive_Type.__name__=_B
_Xgs360026fERPSInstanceConfRevertive_Object=MibTableColumn
xgs360026fERPSInstanceConfRevertive=_Xgs360026fERPSInstanceConfRevertive_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,19),_Xgs360026fERPSInstanceConfRevertive_Type())
xgs360026fERPSInstanceConfRevertive.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSInstanceConfRevertive.setStatus(_A)
class _Xgs360026fERPSInstanceConfVLANconfig_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Xgs360026fERPSInstanceConfVLANconfig_Type.__name__=_G
_Xgs360026fERPSInstanceConfVLANconfig_Object=MibTableColumn
xgs360026fERPSInstanceConfVLANconfig=_Xgs360026fERPSInstanceConfVLANconfig_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,20),_Xgs360026fERPSInstanceConfVLANconfig_Type())
xgs360026fERPSInstanceConfVLANconfig.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSInstanceConfVLANconfig.setStatus(_A)
class _Xgs360026fERPSConfRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360026fERPSConfRowStatus_Type.__name__=_B
_Xgs360026fERPSConfRowStatus_Object=MibTableColumn
xgs360026fERPSConfRowStatus=_Xgs360026fERPSConfRowStatus_Object((1,3,6,1,4,1,890,1,5,8,77,2,10,1,2,1,21),_Xgs360026fERPSConfRowStatus_Type())
xgs360026fERPSConfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fERPSConfRowStatus.setStatus(_A)
_Xgs360026fMRSTP_ObjectIdentity=ObjectIdentity
xgs360026fMRSTP=_Xgs360026fMRSTP_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,11))
_Xgs360026fMRSTPInstance_ObjectIdentity=ObjectIdentity
xgs360026fMRSTPInstance=_Xgs360026fMRSTPInstance_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,11,1))
_Xgs360026fMRSTPInstanceConf_ObjectIdentity=ObjectIdentity
xgs360026fMRSTPInstanceConf=_Xgs360026fMRSTPInstanceConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,11,1,1))
class _Xgs360026fMRSTPInstanceConfGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fMRSTPInstanceConfGlobalState_Type.__name__=_B
_Xgs360026fMRSTPInstanceConfGlobalState_Object=MibScalar
xgs360026fMRSTPInstanceConfGlobalState=_Xgs360026fMRSTPInstanceConfGlobalState_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,1,1),_Xgs360026fMRSTPInstanceConfGlobalState_Type())
xgs360026fMRSTPInstanceConfGlobalState.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceConfGlobalState.setStatus(_A)
_Xgs360026fMRSTPInstanceConfigurationTable_Object=MibTable
xgs360026fMRSTPInstanceConfigurationTable=_Xgs360026fMRSTPInstanceConfigurationTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,1,2))
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceConfigurationTable.setStatus(_A)
_Xgs360026fMRSTPInstanceConfigurationEntry_Object=MibTableRow
xgs360026fMRSTPInstanceConfigurationEntry=_Xgs360026fMRSTPInstanceConfigurationEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,1,2,1))
xgs360026fMRSTPInstanceConfigurationEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceConfigurationEntry.setStatus(_A)
class _Xgs360026fMRSTPInstanceConfigurationInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Xgs360026fMRSTPInstanceConfigurationInstance_Type.__name__=_B
_Xgs360026fMRSTPInstanceConfigurationInstance_Object=MibTableColumn
xgs360026fMRSTPInstanceConfigurationInstance=_Xgs360026fMRSTPInstanceConfigurationInstance_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,1,2,1,1),_Xgs360026fMRSTPInstanceConfigurationInstance_Type())
xgs360026fMRSTPInstanceConfigurationInstance.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceConfigurationInstance.setStatus(_A)
class _Xgs360026fMRSTPInstanceConfigurationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fMRSTPInstanceConfigurationState_Type.__name__=_B
_Xgs360026fMRSTPInstanceConfigurationState_Object=MibTableColumn
xgs360026fMRSTPInstanceConfigurationState=_Xgs360026fMRSTPInstanceConfigurationState_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,1,2,1,2),_Xgs360026fMRSTPInstanceConfigurationState_Type())
xgs360026fMRSTPInstanceConfigurationState.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceConfigurationState.setStatus(_A)
class _Xgs360026fMRSTPInstanceConfigurationVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fMRSTPInstanceConfigurationVersion_Type.__name__=_B
_Xgs360026fMRSTPInstanceConfigurationVersion_Object=MibTableColumn
xgs360026fMRSTPInstanceConfigurationVersion=_Xgs360026fMRSTPInstanceConfigurationVersion_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,1,2,1,3),_Xgs360026fMRSTPInstanceConfigurationVersion_Type())
xgs360026fMRSTPInstanceConfigurationVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceConfigurationVersion.setStatus(_A)
class _Xgs360026fMRSTPInstanceConfigurationPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_Xgs360026fMRSTPInstanceConfigurationPriority_Type.__name__=_B
_Xgs360026fMRSTPInstanceConfigurationPriority_Object=MibTableColumn
xgs360026fMRSTPInstanceConfigurationPriority=_Xgs360026fMRSTPInstanceConfigurationPriority_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,1,2,1,4),_Xgs360026fMRSTPInstanceConfigurationPriority_Type())
xgs360026fMRSTPInstanceConfigurationPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceConfigurationPriority.setStatus(_A)
class _Xgs360026fMRSTPInstanceConfigurationHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Xgs360026fMRSTPInstanceConfigurationHelloTime_Type.__name__=_B
_Xgs360026fMRSTPInstanceConfigurationHelloTime_Object=MibTableColumn
xgs360026fMRSTPInstanceConfigurationHelloTime=_Xgs360026fMRSTPInstanceConfigurationHelloTime_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,1,2,1,5),_Xgs360026fMRSTPInstanceConfigurationHelloTime_Type())
xgs360026fMRSTPInstanceConfigurationHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceConfigurationHelloTime.setStatus(_A)
class _Xgs360026fMRSTPInstanceConfigurationMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_Xgs360026fMRSTPInstanceConfigurationMaxAge_Type.__name__=_B
_Xgs360026fMRSTPInstanceConfigurationMaxAge_Object=MibTableColumn
xgs360026fMRSTPInstanceConfigurationMaxAge=_Xgs360026fMRSTPInstanceConfigurationMaxAge_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,1,2,1,6),_Xgs360026fMRSTPInstanceConfigurationMaxAge_Type())
xgs360026fMRSTPInstanceConfigurationMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceConfigurationMaxAge.setStatus(_A)
class _Xgs360026fMRSTPInstanceConfigurationFWDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_Xgs360026fMRSTPInstanceConfigurationFWDelay_Type.__name__=_B
_Xgs360026fMRSTPInstanceConfigurationFWDelay_Object=MibTableColumn
xgs360026fMRSTPInstanceConfigurationFWDelay=_Xgs360026fMRSTPInstanceConfigurationFWDelay_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,1,2,1,7),_Xgs360026fMRSTPInstanceConfigurationFWDelay_Type())
xgs360026fMRSTPInstanceConfigurationFWDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceConfigurationFWDelay.setStatus(_A)
_Xgs360026fMRSTPInstanceStatus_ObjectIdentity=ObjectIdentity
xgs360026fMRSTPInstanceStatus=_Xgs360026fMRSTPInstanceStatus_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2))
_Xgs360026fMRSTPInstanceStatusTable_Object=MibTable
xgs360026fMRSTPInstanceStatusTable=_Xgs360026fMRSTPInstanceStatusTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1))
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusTable.setStatus(_A)
_Xgs360026fMRSTPInstanceStatusEntry_Object=MibTableRow
xgs360026fMRSTPInstanceStatusEntry=_Xgs360026fMRSTPInstanceStatusEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1))
xgs360026fMRSTPInstanceStatusEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusEntry.setStatus(_A)
class _Xgs360026fMRSTPInstanceStatusInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Xgs360026fMRSTPInstanceStatusInstance_Type.__name__=_B
_Xgs360026fMRSTPInstanceStatusInstance_Object=MibTableColumn
xgs360026fMRSTPInstanceStatusInstance=_Xgs360026fMRSTPInstanceStatusInstance_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1,1),_Xgs360026fMRSTPInstanceStatusInstance_Type())
xgs360026fMRSTPInstanceStatusInstance.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusInstance.setStatus(_A)
class _Xgs360026fMRSTPInstanceStatusGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fMRSTPInstanceStatusGlobalState_Type.__name__=_B
_Xgs360026fMRSTPInstanceStatusGlobalState_Object=MibTableColumn
xgs360026fMRSTPInstanceStatusGlobalState=_Xgs360026fMRSTPInstanceStatusGlobalState_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1,2),_Xgs360026fMRSTPInstanceStatusGlobalState_Type())
xgs360026fMRSTPInstanceStatusGlobalState.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusGlobalState.setStatus(_A)
class _Xgs360026fMRSTPInstanceStatusInstanceConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fMRSTPInstanceStatusInstanceConfigState_Type.__name__=_B
_Xgs360026fMRSTPInstanceStatusInstanceConfigState_Object=MibTableColumn
xgs360026fMRSTPInstanceStatusInstanceConfigState=_Xgs360026fMRSTPInstanceStatusInstanceConfigState_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1,3),_Xgs360026fMRSTPInstanceStatusInstanceConfigState_Type())
xgs360026fMRSTPInstanceStatusInstanceConfigState.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusInstanceConfigState.setStatus(_A)
class _Xgs360026fMRSTPInstanceStatusInstanceCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fMRSTPInstanceStatusInstanceCurrentState_Type.__name__=_B
_Xgs360026fMRSTPInstanceStatusInstanceCurrentState_Object=MibTableColumn
xgs360026fMRSTPInstanceStatusInstanceCurrentState=_Xgs360026fMRSTPInstanceStatusInstanceCurrentState_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1,4),_Xgs360026fMRSTPInstanceStatusInstanceCurrentState_Type())
xgs360026fMRSTPInstanceStatusInstanceCurrentState.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusInstanceCurrentState.setStatus(_A)
_Xgs360026fMRSTPInstanceStatusBridgeID_Type=MacAddress
_Xgs360026fMRSTPInstanceStatusBridgeID_Object=MibTableColumn
xgs360026fMRSTPInstanceStatusBridgeID=_Xgs360026fMRSTPInstanceStatusBridgeID_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1,5),_Xgs360026fMRSTPInstanceStatusBridgeID_Type())
xgs360026fMRSTPInstanceStatusBridgeID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusBridgeID.setStatus(_A)
class _Xgs360026fMRSTPInstanceStatusBridgePrioriry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_Xgs360026fMRSTPInstanceStatusBridgePrioriry_Type.__name__=_B
_Xgs360026fMRSTPInstanceStatusBridgePrioriry_Object=MibTableColumn
xgs360026fMRSTPInstanceStatusBridgePrioriry=_Xgs360026fMRSTPInstanceStatusBridgePrioriry_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1,6),_Xgs360026fMRSTPInstanceStatusBridgePrioriry_Type())
xgs360026fMRSTPInstanceStatusBridgePrioriry.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusBridgePrioriry.setStatus(_A)
_Xgs360026fMRSTPInstanceStatusRootID_Type=MacAddress
_Xgs360026fMRSTPInstanceStatusRootID_Object=MibTableColumn
xgs360026fMRSTPInstanceStatusRootID=_Xgs360026fMRSTPInstanceStatusRootID_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1,7),_Xgs360026fMRSTPInstanceStatusRootID_Type())
xgs360026fMRSTPInstanceStatusRootID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusRootID.setStatus(_A)
class _Xgs360026fMRSTPInstanceStatusRootPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_Xgs360026fMRSTPInstanceStatusRootPriority_Type.__name__=_B
_Xgs360026fMRSTPInstanceStatusRootPriority_Object=MibTableColumn
xgs360026fMRSTPInstanceStatusRootPriority=_Xgs360026fMRSTPInstanceStatusRootPriority_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1,8),_Xgs360026fMRSTPInstanceStatusRootPriority_Type())
xgs360026fMRSTPInstanceStatusRootPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusRootPriority.setStatus(_A)
_Xgs360026fMRSTPInstanceStatusRootPort_Type=Integer32
_Xgs360026fMRSTPInstanceStatusRootPort_Object=MibTableColumn
xgs360026fMRSTPInstanceStatusRootPort=_Xgs360026fMRSTPInstanceStatusRootPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1,9),_Xgs360026fMRSTPInstanceStatusRootPort_Type())
xgs360026fMRSTPInstanceStatusRootPort.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusRootPort.setStatus(_A)
_Xgs360026fMRSTPInstanceStatusRootPathCost_Type=Integer32
_Xgs360026fMRSTPInstanceStatusRootPathCost_Object=MibTableColumn
xgs360026fMRSTPInstanceStatusRootPathCost=_Xgs360026fMRSTPInstanceStatusRootPathCost_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1,10),_Xgs360026fMRSTPInstanceStatusRootPathCost_Type())
xgs360026fMRSTPInstanceStatusRootPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusRootPathCost.setStatus(_A)
class _Xgs360026fMRSTPInstanceStatusCurrentMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_Xgs360026fMRSTPInstanceStatusCurrentMaxAge_Type.__name__=_B
_Xgs360026fMRSTPInstanceStatusCurrentMaxAge_Object=MibTableColumn
xgs360026fMRSTPInstanceStatusCurrentMaxAge=_Xgs360026fMRSTPInstanceStatusCurrentMaxAge_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1,11),_Xgs360026fMRSTPInstanceStatusCurrentMaxAge_Type())
xgs360026fMRSTPInstanceStatusCurrentMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusCurrentMaxAge.setStatus(_A)
class _Xgs360026fMRSTPInstanceStatusCurrentForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_Xgs360026fMRSTPInstanceStatusCurrentForwardDelay_Type.__name__=_B
_Xgs360026fMRSTPInstanceStatusCurrentForwardDelay_Object=MibTableColumn
xgs360026fMRSTPInstanceStatusCurrentForwardDelay=_Xgs360026fMRSTPInstanceStatusCurrentForwardDelay_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1,12),_Xgs360026fMRSTPInstanceStatusCurrentForwardDelay_Type())
xgs360026fMRSTPInstanceStatusCurrentForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusCurrentForwardDelay.setStatus(_A)
class _Xgs360026fMRSTPInstanceStatusHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Xgs360026fMRSTPInstanceStatusHelloTime_Type.__name__=_B
_Xgs360026fMRSTPInstanceStatusHelloTime_Object=MibTableColumn
xgs360026fMRSTPInstanceStatusHelloTime=_Xgs360026fMRSTPInstanceStatusHelloTime_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1,13),_Xgs360026fMRSTPInstanceStatusHelloTime_Type())
xgs360026fMRSTPInstanceStatusHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusHelloTime.setStatus(_A)
_Xgs360026fMRSTPInstanceStatusTopologyChangeCount_Type=Integer32
_Xgs360026fMRSTPInstanceStatusTopologyChangeCount_Object=MibTableColumn
xgs360026fMRSTPInstanceStatusTopologyChangeCount=_Xgs360026fMRSTPInstanceStatusTopologyChangeCount_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1,14),_Xgs360026fMRSTPInstanceStatusTopologyChangeCount_Type())
xgs360026fMRSTPInstanceStatusTopologyChangeCount.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusTopologyChangeCount.setStatus(_A)
_Xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange_Type=Integer32
_Xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange_Object=MibTableColumn
xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange=_Xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,1,2,1,1,15),_Xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange_Type())
xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange.setStatus(_A)
_Xgs360026fMRSTPPort_ObjectIdentity=ObjectIdentity
xgs360026fMRSTPPort=_Xgs360026fMRSTPPort_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,11,2))
_Xgs360026fMRSTPPortConfiguration_ObjectIdentity=ObjectIdentity
xgs360026fMRSTPPortConfiguration=_Xgs360026fMRSTPPortConfiguration_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,11,2,1))
_Xgs360026fMRSTPPortConfigurationTable_Object=MibTable
xgs360026fMRSTPPortConfigurationTable=_Xgs360026fMRSTPPortConfigurationTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,1,1))
if mibBuilder.loadTexts:xgs360026fMRSTPPortConfigurationTable.setStatus(_A)
_Xgs360026fMRSTPPortConfigurationEntry_Object=MibTableRow
xgs360026fMRSTPPortConfigurationEntry=_Xgs360026fMRSTPPortConfigurationEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,1,1,1))
xgs360026fMRSTPPortConfigurationEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:xgs360026fMRSTPPortConfigurationEntry.setStatus(_A)
class _Xgs360026fMRSTPPortConfigurationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fMRSTPPortConfigurationPort_Type.__name__=_B
_Xgs360026fMRSTPPortConfigurationPort_Object=MibTableColumn
xgs360026fMRSTPPortConfigurationPort=_Xgs360026fMRSTPPortConfigurationPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,1,1,1,1),_Xgs360026fMRSTPPortConfigurationPort_Type())
xgs360026fMRSTPPortConfigurationPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fMRSTPPortConfigurationPort.setStatus(_A)
class _Xgs360026fMRSTPPortConfigurationInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_Xgs360026fMRSTPPortConfigurationInstance_Type.__name__=_B
_Xgs360026fMRSTPPortConfigurationInstance_Object=MibTableColumn
xgs360026fMRSTPPortConfigurationInstance=_Xgs360026fMRSTPPortConfigurationInstance_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,1,1,1,2),_Xgs360026fMRSTPPortConfigurationInstance_Type())
xgs360026fMRSTPPortConfigurationInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMRSTPPortConfigurationInstance.setStatus(_A)
class _Xgs360026fMRSTPPortConfigurationPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_Xgs360026fMRSTPPortConfigurationPathCost_Type.__name__=_B
_Xgs360026fMRSTPPortConfigurationPathCost_Object=MibTableColumn
xgs360026fMRSTPPortConfigurationPathCost=_Xgs360026fMRSTPPortConfigurationPathCost_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,1,1,1,3),_Xgs360026fMRSTPPortConfigurationPathCost_Type())
xgs360026fMRSTPPortConfigurationPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMRSTPPortConfigurationPathCost.setStatus(_A)
class _Xgs360026fMRSTPPortConfigurationPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_Xgs360026fMRSTPPortConfigurationPriority_Type.__name__=_B
_Xgs360026fMRSTPPortConfigurationPriority_Object=MibTableColumn
xgs360026fMRSTPPortConfigurationPriority=_Xgs360026fMRSTPPortConfigurationPriority_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,1,1,1,4),_Xgs360026fMRSTPPortConfigurationPriority_Type())
xgs360026fMRSTPPortConfigurationPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMRSTPPortConfigurationPriority.setStatus(_A)
class _Xgs360026fMRSTPPortConfigurationAdminEdge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fMRSTPPortConfigurationAdminEdge_Type.__name__=_B
_Xgs360026fMRSTPPortConfigurationAdminEdge_Object=MibTableColumn
xgs360026fMRSTPPortConfigurationAdminEdge=_Xgs360026fMRSTPPortConfigurationAdminEdge_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,1,1,1,5),_Xgs360026fMRSTPPortConfigurationAdminEdge_Type())
xgs360026fMRSTPPortConfigurationAdminEdge.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMRSTPPortConfigurationAdminEdge.setStatus(_A)
class _Xgs360026fMRSTPPortConfigurationAdminP2P_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fMRSTPPortConfigurationAdminP2P_Type.__name__=_B
_Xgs360026fMRSTPPortConfigurationAdminP2P_Object=MibTableColumn
xgs360026fMRSTPPortConfigurationAdminP2P=_Xgs360026fMRSTPPortConfigurationAdminP2P_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,1,1,1,6),_Xgs360026fMRSTPPortConfigurationAdminP2P_Type())
xgs360026fMRSTPPortConfigurationAdminP2P.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMRSTPPortConfigurationAdminP2P.setStatus(_A)
class _Xgs360026fMRSTPPortConfigurationMigrateCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fMRSTPPortConfigurationMigrateCheck_Type.__name__=_B
_Xgs360026fMRSTPPortConfigurationMigrateCheck_Object=MibTableColumn
xgs360026fMRSTPPortConfigurationMigrateCheck=_Xgs360026fMRSTPPortConfigurationMigrateCheck_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,1,1,1,7),_Xgs360026fMRSTPPortConfigurationMigrateCheck_Type())
xgs360026fMRSTPPortConfigurationMigrateCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fMRSTPPortConfigurationMigrateCheck.setStatus(_A)
_Xgs360026fMRSTPPortStatus_ObjectIdentity=ObjectIdentity
xgs360026fMRSTPPortStatus=_Xgs360026fMRSTPPortStatus_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,2,11,2,2))
_Xgs360026fMRSTPPortStatusTable_Object=MibTable
xgs360026fMRSTPPortStatusTable=_Xgs360026fMRSTPPortStatusTable_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,2,1))
if mibBuilder.loadTexts:xgs360026fMRSTPPortStatusTable.setStatus(_A)
_Xgs360026fMRSTPPortStatusEntry_Object=MibTableRow
xgs360026fMRSTPPortStatusEntry=_Xgs360026fMRSTPPortStatusEntry_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,2,1,1))
xgs360026fMRSTPPortStatusEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:xgs360026fMRSTPPortStatusEntry.setStatus(_A)
class _Xgs360026fMRSTPPortStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fMRSTPPortStatusPort_Type.__name__=_B
_Xgs360026fMRSTPPortStatusPort_Object=MibTableColumn
xgs360026fMRSTPPortStatusPort=_Xgs360026fMRSTPPortStatusPort_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,2,1,1,1),_Xgs360026fMRSTPPortStatusPort_Type())
xgs360026fMRSTPPortStatusPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fMRSTPPortStatusPort.setStatus(_A)
_Xgs360026fMRSTPPortStatusInstance_Type=DisplayString
_Xgs360026fMRSTPPortStatusInstance_Object=MibTableColumn
xgs360026fMRSTPPortStatusInstance=_Xgs360026fMRSTPPortStatusInstance_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,2,1,1,2),_Xgs360026fMRSTPPortStatusInstance_Type())
xgs360026fMRSTPPortStatusInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPPortStatusInstance.setStatus(_A)
_Xgs360026fMRSTPPortStatusState_Type=DisplayString
_Xgs360026fMRSTPPortStatusState_Object=MibTableColumn
xgs360026fMRSTPPortStatusState=_Xgs360026fMRSTPPortStatusState_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,2,1,1,3),_Xgs360026fMRSTPPortStatusState_Type())
xgs360026fMRSTPPortStatusState.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPPortStatusState.setStatus(_A)
_Xgs360026fMRSTPPortStatusRole_Type=DisplayString
_Xgs360026fMRSTPPortStatusRole_Object=MibTableColumn
xgs360026fMRSTPPortStatusRole=_Xgs360026fMRSTPPortStatusRole_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,2,1,1,4),_Xgs360026fMRSTPPortStatusRole_Type())
xgs360026fMRSTPPortStatusRole.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPPortStatusRole.setStatus(_A)
class _Xgs360026fMRSTPPortStatusPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_Xgs360026fMRSTPPortStatusPathCost_Type.__name__=_B
_Xgs360026fMRSTPPortStatusPathCost_Object=MibTableColumn
xgs360026fMRSTPPortStatusPathCost=_Xgs360026fMRSTPPortStatusPathCost_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,2,1,1,5),_Xgs360026fMRSTPPortStatusPathCost_Type())
xgs360026fMRSTPPortStatusPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPPortStatusPathCost.setStatus(_A)
class _Xgs360026fMRSTPPortStatusPathCostConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_Xgs360026fMRSTPPortStatusPathCostConfig_Type.__name__=_B
_Xgs360026fMRSTPPortStatusPathCostConfig_Object=MibTableColumn
xgs360026fMRSTPPortStatusPathCostConfig=_Xgs360026fMRSTPPortStatusPathCostConfig_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,2,1,1,6),_Xgs360026fMRSTPPortStatusPathCostConfig_Type())
xgs360026fMRSTPPortStatusPathCostConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPPortStatusPathCostConfig.setStatus(_A)
class _Xgs360026fMRSTPPortStatusPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_Xgs360026fMRSTPPortStatusPriority_Type.__name__=_B
_Xgs360026fMRSTPPortStatusPriority_Object=MibTableColumn
xgs360026fMRSTPPortStatusPriority=_Xgs360026fMRSTPPortStatusPriority_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,2,1,1,7),_Xgs360026fMRSTPPortStatusPriority_Type())
xgs360026fMRSTPPortStatusPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPPortStatusPriority.setStatus(_A)
_Xgs360026fMRSTPPortStatusAdminEdge_Type=DisplayString
_Xgs360026fMRSTPPortStatusAdminEdge_Object=MibTableColumn
xgs360026fMRSTPPortStatusAdminEdge=_Xgs360026fMRSTPPortStatusAdminEdge_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,2,1,1,8),_Xgs360026fMRSTPPortStatusAdminEdge_Type())
xgs360026fMRSTPPortStatusAdminEdge.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPPortStatusAdminEdge.setStatus(_A)
_Xgs360026fMRSTPPortStatusAdminP2P_Type=DisplayString
_Xgs360026fMRSTPPortStatusAdminP2P_Object=MibTableColumn
xgs360026fMRSTPPortStatusAdminP2P=_Xgs360026fMRSTPPortStatusAdminP2P_Object((1,3,6,1,4,1,890,1,5,8,77,2,11,2,2,1,1,9),_Xgs360026fMRSTPPortStatusAdminP2P_Type())
xgs360026fMRSTPPortStatusAdminP2P.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fMRSTPPortStatusAdminP2P.setStatus(_A)
_Xgs360026fSecurity_ObjectIdentity=ObjectIdentity
xgs360026fSecurity=_Xgs360026fSecurity_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3))
_Xgs360026fIPSourceGuard_ObjectIdentity=ObjectIdentity
xgs360026fIPSourceGuard=_Xgs360026fIPSourceGuard_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,1))
_Xgs360026fIPSourceGuardConf_ObjectIdentity=ObjectIdentity
xgs360026fIPSourceGuardConf=_Xgs360026fIPSourceGuardConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,1,1))
class _Xgs360026fIPSourceGuardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fIPSourceGuardMode_Type.__name__=_B
_Xgs360026fIPSourceGuardMode_Object=MibScalar
xgs360026fIPSourceGuardMode=_Xgs360026fIPSourceGuardMode_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,1,1),_Xgs360026fIPSourceGuardMode_Type())
xgs360026fIPSourceGuardMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardMode.setStatus(_A)
_Xgs360026fIPSourceGuardPortConfigTable_Object=MibTable
xgs360026fIPSourceGuardPortConfigTable=_Xgs360026fIPSourceGuardPortConfigTable_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,1,2))
if mibBuilder.loadTexts:xgs360026fIPSourceGuardPortConfigTable.setStatus(_A)
_Xgs360026fIPSourceGuardPortConfigEntry_Object=MibTableRow
xgs360026fIPSourceGuardPortConfigEntry=_Xgs360026fIPSourceGuardPortConfigEntry_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,1,2,1))
xgs360026fIPSourceGuardPortConfigEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:xgs360026fIPSourceGuardPortConfigEntry.setStatus(_A)
class _Xgs360026fIPSourceGuardPortConfigPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fIPSourceGuardPortConfigPort_Type.__name__=_B
_Xgs360026fIPSourceGuardPortConfigPort_Object=MibTableColumn
xgs360026fIPSourceGuardPortConfigPort=_Xgs360026fIPSourceGuardPortConfigPort_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,1,2,1,1),_Xgs360026fIPSourceGuardPortConfigPort_Type())
xgs360026fIPSourceGuardPortConfigPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardPortConfigPort.setStatus(_A)
class _Xgs360026fIPSourceGuardPortConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fIPSourceGuardPortConfigMode_Type.__name__=_B
_Xgs360026fIPSourceGuardPortConfigMode_Object=MibTableColumn
xgs360026fIPSourceGuardPortConfigMode=_Xgs360026fIPSourceGuardPortConfigMode_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,1,2,1,2),_Xgs360026fIPSourceGuardPortConfigMode_Type())
xgs360026fIPSourceGuardPortConfigMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardPortConfigMode.setStatus(_A)
class _Xgs360026fIPSourceGuardPortMaxDynamicClients_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2),ValueRangeConstraint(99,99))
_Xgs360026fIPSourceGuardPortMaxDynamicClients_Type.__name__=_B
_Xgs360026fIPSourceGuardPortMaxDynamicClients_Object=MibTableColumn
xgs360026fIPSourceGuardPortMaxDynamicClients=_Xgs360026fIPSourceGuardPortMaxDynamicClients_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,1,2,1,3),_Xgs360026fIPSourceGuardPortMaxDynamicClients_Type())
xgs360026fIPSourceGuardPortMaxDynamicClients.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardPortMaxDynamicClients.setStatus(_A)
_Xgs360026fIPSourceGuardStatic_ObjectIdentity=ObjectIdentity
xgs360026fIPSourceGuardStatic=_Xgs360026fIPSourceGuardStatic_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,1,2))
class _Xgs360026fIPSourceGuardStaticCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fIPSourceGuardStaticCreate_Type.__name__=_B
_Xgs360026fIPSourceGuardStaticCreate_Object=MibScalar
xgs360026fIPSourceGuardStaticCreate=_Xgs360026fIPSourceGuardStaticCreate_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,2,1),_Xgs360026fIPSourceGuardStaticCreate_Type())
xgs360026fIPSourceGuardStaticCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardStaticCreate.setStatus(_A)
_Xgs360026fIPSourceGuardStaticTable_Object=MibTable
xgs360026fIPSourceGuardStaticTable=_Xgs360026fIPSourceGuardStaticTable_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,2,2))
if mibBuilder.loadTexts:xgs360026fIPSourceGuardStaticTable.setStatus(_A)
_Xgs360026fIPSourceGuardStaticEntry_Object=MibTableRow
xgs360026fIPSourceGuardStaticEntry=_Xgs360026fIPSourceGuardStaticEntry_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,2,2,1))
xgs360026fIPSourceGuardStaticEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:xgs360026fIPSourceGuardStaticEntry.setStatus(_A)
class _Xgs360026fIPSourceGuardStaticIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_Xgs360026fIPSourceGuardStaticIndex_Type.__name__=_B
_Xgs360026fIPSourceGuardStaticIndex_Object=MibTableColumn
xgs360026fIPSourceGuardStaticIndex=_Xgs360026fIPSourceGuardStaticIndex_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,2,2,1,1),_Xgs360026fIPSourceGuardStaticIndex_Type())
xgs360026fIPSourceGuardStaticIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardStaticIndex.setStatus(_A)
class _Xgs360026fIPSourceGuardStaticPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fIPSourceGuardStaticPort_Type.__name__=_B
_Xgs360026fIPSourceGuardStaticPort_Object=MibTableColumn
xgs360026fIPSourceGuardStaticPort=_Xgs360026fIPSourceGuardStaticPort_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,2,2,1,2),_Xgs360026fIPSourceGuardStaticPort_Type())
xgs360026fIPSourceGuardStaticPort.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardStaticPort.setStatus(_A)
class _Xgs360026fIPSourceGuardStaticVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Xgs360026fIPSourceGuardStaticVLANId_Type.__name__=_B
_Xgs360026fIPSourceGuardStaticVLANId_Object=MibTableColumn
xgs360026fIPSourceGuardStaticVLANId=_Xgs360026fIPSourceGuardStaticVLANId_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,2,2,1,3),_Xgs360026fIPSourceGuardStaticVLANId_Type())
xgs360026fIPSourceGuardStaticVLANId.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardStaticVLANId.setStatus(_A)
_Xgs360026fIPSourceGuardStaticIPAddress_Type=IpAddress
_Xgs360026fIPSourceGuardStaticIPAddress_Object=MibTableColumn
xgs360026fIPSourceGuardStaticIPAddress=_Xgs360026fIPSourceGuardStaticIPAddress_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,2,2,1,4),_Xgs360026fIPSourceGuardStaticIPAddress_Type())
xgs360026fIPSourceGuardStaticIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardStaticIPAddress.setStatus(_A)
_Xgs360026fIPSourceGuardStaticMACAddress_Type=MacAddress
_Xgs360026fIPSourceGuardStaticMACAddress_Object=MibTableColumn
xgs360026fIPSourceGuardStaticMACAddress=_Xgs360026fIPSourceGuardStaticMACAddress_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,2,2,1,5),_Xgs360026fIPSourceGuardStaticMACAddress_Type())
xgs360026fIPSourceGuardStaticMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardStaticMACAddress.setStatus(_A)
class _Xgs360026fIPSourceGuardStaticRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360026fIPSourceGuardStaticRowStatus_Type.__name__=_B
_Xgs360026fIPSourceGuardStaticRowStatus_Object=MibTableColumn
xgs360026fIPSourceGuardStaticRowStatus=_Xgs360026fIPSourceGuardStaticRowStatus_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,2,2,1,6),_Xgs360026fIPSourceGuardStaticRowStatus_Type())
xgs360026fIPSourceGuardStaticRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardStaticRowStatus.setStatus(_A)
_Xgs360026fIPSourceGuardDynamicTable_Object=MibTable
xgs360026fIPSourceGuardDynamicTable=_Xgs360026fIPSourceGuardDynamicTable_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,3))
if mibBuilder.loadTexts:xgs360026fIPSourceGuardDynamicTable.setStatus(_A)
_Xgs360026fIPSourceGuardDynamicEntry_Object=MibTableRow
xgs360026fIPSourceGuardDynamicEntry=_Xgs360026fIPSourceGuardDynamicEntry_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,3,1))
xgs360026fIPSourceGuardDynamicEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:xgs360026fIPSourceGuardDynamicEntry.setStatus(_A)
class _Xgs360026fIPSourceGuardDynamicIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fIPSourceGuardDynamicIndex_Type.__name__=_B
_Xgs360026fIPSourceGuardDynamicIndex_Object=MibTableColumn
xgs360026fIPSourceGuardDynamicIndex=_Xgs360026fIPSourceGuardDynamicIndex_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,3,1,1),_Xgs360026fIPSourceGuardDynamicIndex_Type())
xgs360026fIPSourceGuardDynamicIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardDynamicIndex.setStatus(_A)
class _Xgs360026fIPSourceGuardDynamicPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Xgs360026fIPSourceGuardDynamicPort_Type.__name__=_B
_Xgs360026fIPSourceGuardDynamicPort_Object=MibTableColumn
xgs360026fIPSourceGuardDynamicPort=_Xgs360026fIPSourceGuardDynamicPort_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,3,1,2),_Xgs360026fIPSourceGuardDynamicPort_Type())
xgs360026fIPSourceGuardDynamicPort.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardDynamicPort.setStatus(_A)
class _Xgs360026fIPSourceGuardDynamicVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Xgs360026fIPSourceGuardDynamicVLANId_Type.__name__=_B
_Xgs360026fIPSourceGuardDynamicVLANId_Object=MibTableColumn
xgs360026fIPSourceGuardDynamicVLANId=_Xgs360026fIPSourceGuardDynamicVLANId_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,3,1,3),_Xgs360026fIPSourceGuardDynamicVLANId_Type())
xgs360026fIPSourceGuardDynamicVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardDynamicVLANId.setStatus(_A)
_Xgs360026fIPSourceGuardDynamicIPAddress_Type=IpAddress
_Xgs360026fIPSourceGuardDynamicIPAddress_Object=MibTableColumn
xgs360026fIPSourceGuardDynamicIPAddress=_Xgs360026fIPSourceGuardDynamicIPAddress_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,3,1,4),_Xgs360026fIPSourceGuardDynamicIPAddress_Type())
xgs360026fIPSourceGuardDynamicIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardDynamicIPAddress.setStatus(_A)
_Xgs360026fIPSourceGuardDynamicMACAddress_Type=MacAddress
_Xgs360026fIPSourceGuardDynamicMACAddress_Object=MibTableColumn
xgs360026fIPSourceGuardDynamicMACAddress=_Xgs360026fIPSourceGuardDynamicMACAddress_Object((1,3,6,1,4,1,890,1,5,8,77,3,1,3,1,5),_Xgs360026fIPSourceGuardDynamicMACAddress_Type())
xgs360026fIPSourceGuardDynamicMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fIPSourceGuardDynamicMACAddress.setStatus(_A)
_Xgs360026fARPInspection_ObjectIdentity=ObjectIdentity
xgs360026fARPInspection=_Xgs360026fARPInspection_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,2))
_Xgs360026fARPInspectionConf_ObjectIdentity=ObjectIdentity
xgs360026fARPInspectionConf=_Xgs360026fARPInspectionConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,2,1))
class _Xgs360026fARPInspectionConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fARPInspectionConfMode_Type.__name__=_B
_Xgs360026fARPInspectionConfMode_Object=MibScalar
xgs360026fARPInspectionConfMode=_Xgs360026fARPInspectionConfMode_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,1,1),_Xgs360026fARPInspectionConfMode_Type())
xgs360026fARPInspectionConfMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fARPInspectionConfMode.setStatus(_A)
_Xgs360026fARPInspectionConfTable_Object=MibTable
xgs360026fARPInspectionConfTable=_Xgs360026fARPInspectionConfTable_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,1,2))
if mibBuilder.loadTexts:xgs360026fARPInspectionConfTable.setStatus(_A)
_Xgs360026fARPInspectionConfEntry_Object=MibTableRow
xgs360026fARPInspectionConfEntry=_Xgs360026fARPInspectionConfEntry_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,1,2,1))
xgs360026fARPInspectionConfEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:xgs360026fARPInspectionConfEntry.setStatus(_A)
class _Xgs360026fARPInspectionConfPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fARPInspectionConfPortIndex_Type.__name__=_B
_Xgs360026fARPInspectionConfPortIndex_Object=MibTableColumn
xgs360026fARPInspectionConfPortIndex=_Xgs360026fARPInspectionConfPortIndex_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,1,2,1,1),_Xgs360026fARPInspectionConfPortIndex_Type())
xgs360026fARPInspectionConfPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fARPInspectionConfPortIndex.setStatus(_A)
class _Xgs360026fARPInspectionConfPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fARPInspectionConfPortMode_Type.__name__=_B
_Xgs360026fARPInspectionConfPortMode_Object=MibTableColumn
xgs360026fARPInspectionConfPortMode=_Xgs360026fARPInspectionConfPortMode_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,1,2,1,2),_Xgs360026fARPInspectionConfPortMode_Type())
xgs360026fARPInspectionConfPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fARPInspectionConfPortMode.setStatus(_A)
_Xgs360026fARPInspectionStatic_ObjectIdentity=ObjectIdentity
xgs360026fARPInspectionStatic=_Xgs360026fARPInspectionStatic_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,2,2))
class _Xgs360026fARPInspectionStaticCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fARPInspectionStaticCreate_Type.__name__=_B
_Xgs360026fARPInspectionStaticCreate_Object=MibScalar
xgs360026fARPInspectionStaticCreate=_Xgs360026fARPInspectionStaticCreate_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,2,1),_Xgs360026fARPInspectionStaticCreate_Type())
xgs360026fARPInspectionStaticCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fARPInspectionStaticCreate.setStatus(_A)
_Xgs360026fARPInspectionStaticTable_Object=MibTable
xgs360026fARPInspectionStaticTable=_Xgs360026fARPInspectionStaticTable_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,2,2))
if mibBuilder.loadTexts:xgs360026fARPInspectionStaticTable.setStatus(_A)
_Xgs360026fARPInspectionStaticEntry_Object=MibTableRow
xgs360026fARPInspectionStaticEntry=_Xgs360026fARPInspectionStaticEntry_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,2,2,1))
xgs360026fARPInspectionStaticEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:xgs360026fARPInspectionStaticEntry.setStatus(_A)
class _Xgs360026fARPInspectionStaticIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fARPInspectionStaticIndex_Type.__name__=_B
_Xgs360026fARPInspectionStaticIndex_Object=MibTableColumn
xgs360026fARPInspectionStaticIndex=_Xgs360026fARPInspectionStaticIndex_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,2,2,1,1),_Xgs360026fARPInspectionStaticIndex_Type())
xgs360026fARPInspectionStaticIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fARPInspectionStaticIndex.setStatus(_A)
class _Xgs360026fARPInspectionStaticPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fARPInspectionStaticPort_Type.__name__=_B
_Xgs360026fARPInspectionStaticPort_Object=MibTableColumn
xgs360026fARPInspectionStaticPort=_Xgs360026fARPInspectionStaticPort_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,2,2,1,2),_Xgs360026fARPInspectionStaticPort_Type())
xgs360026fARPInspectionStaticPort.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fARPInspectionStaticPort.setStatus(_A)
class _Xgs360026fARPInspectionStaticVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Xgs360026fARPInspectionStaticVLANId_Type.__name__=_B
_Xgs360026fARPInspectionStaticVLANId_Object=MibTableColumn
xgs360026fARPInspectionStaticVLANId=_Xgs360026fARPInspectionStaticVLANId_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,2,2,1,3),_Xgs360026fARPInspectionStaticVLANId_Type())
xgs360026fARPInspectionStaticVLANId.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fARPInspectionStaticVLANId.setStatus(_A)
_Xgs360026fARPInspectionStaticIPAddress_Type=IpAddress
_Xgs360026fARPInspectionStaticIPAddress_Object=MibTableColumn
xgs360026fARPInspectionStaticIPAddress=_Xgs360026fARPInspectionStaticIPAddress_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,2,2,1,4),_Xgs360026fARPInspectionStaticIPAddress_Type())
xgs360026fARPInspectionStaticIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fARPInspectionStaticIPAddress.setStatus(_A)
_Xgs360026fARPInspectionStaticMACAddress_Type=MacAddress
_Xgs360026fARPInspectionStaticMACAddress_Object=MibTableColumn
xgs360026fARPInspectionStaticMACAddress=_Xgs360026fARPInspectionStaticMACAddress_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,2,2,1,5),_Xgs360026fARPInspectionStaticMACAddress_Type())
xgs360026fARPInspectionStaticMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fARPInspectionStaticMACAddress.setStatus(_A)
class _Xgs360026fARPInspectionStaticRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360026fARPInspectionStaticRowStatus_Type.__name__=_B
_Xgs360026fARPInspectionStaticRowStatus_Object=MibTableColumn
xgs360026fARPInspectionStaticRowStatus=_Xgs360026fARPInspectionStaticRowStatus_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,2,2,1,6),_Xgs360026fARPInspectionStaticRowStatus_Type())
xgs360026fARPInspectionStaticRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fARPInspectionStaticRowStatus.setStatus(_A)
_Xgs360026fARPInspectionDynamicTable_Object=MibTable
xgs360026fARPInspectionDynamicTable=_Xgs360026fARPInspectionDynamicTable_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,3))
if mibBuilder.loadTexts:xgs360026fARPInspectionDynamicTable.setStatus(_A)
_Xgs360026fARPInspectionDynamicEntry_Object=MibTableRow
xgs360026fARPInspectionDynamicEntry=_Xgs360026fARPInspectionDynamicEntry_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,3,1))
xgs360026fARPInspectionDynamicEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:xgs360026fARPInspectionDynamicEntry.setStatus(_A)
class _Xgs360026fARPInspectionDynamicIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fARPInspectionDynamicIndex_Type.__name__=_B
_Xgs360026fARPInspectionDynamicIndex_Object=MibTableColumn
xgs360026fARPInspectionDynamicIndex=_Xgs360026fARPInspectionDynamicIndex_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,3,1,1),_Xgs360026fARPInspectionDynamicIndex_Type())
xgs360026fARPInspectionDynamicIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fARPInspectionDynamicIndex.setStatus(_A)
class _Xgs360026fARPInspectionDynamicPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fARPInspectionDynamicPort_Type.__name__=_B
_Xgs360026fARPInspectionDynamicPort_Object=MibTableColumn
xgs360026fARPInspectionDynamicPort=_Xgs360026fARPInspectionDynamicPort_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,3,1,2),_Xgs360026fARPInspectionDynamicPort_Type())
xgs360026fARPInspectionDynamicPort.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fARPInspectionDynamicPort.setStatus(_A)
class _Xgs360026fARPInspectionDynamicVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Xgs360026fARPInspectionDynamicVLANId_Type.__name__=_B
_Xgs360026fARPInspectionDynamicVLANId_Object=MibTableColumn
xgs360026fARPInspectionDynamicVLANId=_Xgs360026fARPInspectionDynamicVLANId_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,3,1,3),_Xgs360026fARPInspectionDynamicVLANId_Type())
xgs360026fARPInspectionDynamicVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fARPInspectionDynamicVLANId.setStatus(_A)
_Xgs360026fARPInspectionDynamicIPAddress_Type=IpAddress
_Xgs360026fARPInspectionDynamicIPAddress_Object=MibTableColumn
xgs360026fARPInspectionDynamicIPAddress=_Xgs360026fARPInspectionDynamicIPAddress_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,3,1,4),_Xgs360026fARPInspectionDynamicIPAddress_Type())
xgs360026fARPInspectionDynamicIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fARPInspectionDynamicIPAddress.setStatus(_A)
_Xgs360026fARPInspectionDynamicMACAddress_Type=MacAddress
_Xgs360026fARPInspectionDynamicMACAddress_Object=MibTableColumn
xgs360026fARPInspectionDynamicMACAddress=_Xgs360026fARPInspectionDynamicMACAddress_Object((1,3,6,1,4,1,890,1,5,8,77,3,2,3,1,5),_Xgs360026fARPInspectionDynamicMACAddress_Type())
xgs360026fARPInspectionDynamicMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fARPInspectionDynamicMACAddress.setStatus(_A)
_Xgs360026fDHCPSnooping_ObjectIdentity=ObjectIdentity
xgs360026fDHCPSnooping=_Xgs360026fDHCPSnooping_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,3))
_Xgs360026fDHCPSnoopingConf_ObjectIdentity=ObjectIdentity
xgs360026fDHCPSnoopingConf=_Xgs360026fDHCPSnoopingConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,3,1))
class _Xgs360026fDHCPSnoopingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fDHCPSnoopingMode_Type.__name__=_B
_Xgs360026fDHCPSnoopingMode_Object=MibScalar
xgs360026fDHCPSnoopingMode=_Xgs360026fDHCPSnoopingMode_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,1,1),_Xgs360026fDHCPSnoopingMode_Type())
xgs360026fDHCPSnoopingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingMode.setStatus(_A)
_Xgs360026fDHCPSnoopingPortModeConfigurationTable_Object=MibTable
xgs360026fDHCPSnoopingPortModeConfigurationTable=_Xgs360026fDHCPSnoopingPortModeConfigurationTable_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,1,2))
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingPortModeConfigurationTable.setStatus(_A)
_Xgs360026fDHCPSnoopingPortModeConfigurationEntry_Object=MibTableRow
xgs360026fDHCPSnoopingPortModeConfigurationEntry=_Xgs360026fDHCPSnoopingPortModeConfigurationEntry_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,1,2,1))
xgs360026fDHCPSnoopingPortModeConfigurationEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingPortModeConfigurationEntry.setStatus(_A)
class _Xgs360026fDHCPSnoopingPortModeConfigurationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fDHCPSnoopingPortModeConfigurationPort_Type.__name__=_B
_Xgs360026fDHCPSnoopingPortModeConfigurationPort_Object=MibTableColumn
xgs360026fDHCPSnoopingPortModeConfigurationPort=_Xgs360026fDHCPSnoopingPortModeConfigurationPort_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,1,2,1,1),_Xgs360026fDHCPSnoopingPortModeConfigurationPort_Type())
xgs360026fDHCPSnoopingPortModeConfigurationPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingPortModeConfigurationPort.setStatus(_A)
class _Xgs360026fDHCPSnoopingPortModeConfigurationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fDHCPSnoopingPortModeConfigurationMode_Type.__name__=_B
_Xgs360026fDHCPSnoopingPortModeConfigurationMode_Object=MibTableColumn
xgs360026fDHCPSnoopingPortModeConfigurationMode=_Xgs360026fDHCPSnoopingPortModeConfigurationMode_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,1,2,1,2),_Xgs360026fDHCPSnoopingPortModeConfigurationMode_Type())
xgs360026fDHCPSnoopingPortModeConfigurationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingPortModeConfigurationMode.setStatus(_A)
_Xgs360026fDHCPSnoopingStatisticsTable_Object=MibTable
xgs360026fDHCPSnoopingStatisticsTable=_Xgs360026fDHCPSnoopingStatisticsTable_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2))
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingStatisticsTable.setStatus(_A)
_Xgs360026fDHCPSnoopingStatisticsEntry_Object=MibTableRow
xgs360026fDHCPSnoopingStatisticsEntry=_Xgs360026fDHCPSnoopingStatisticsEntry_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1))
xgs360026fDHCPSnoopingStatisticsEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingStatisticsEntry.setStatus(_A)
class _Xgs360026fDHCPSnoopingStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fDHCPSnoopingStatisticsPort_Type.__name__=_B
_Xgs360026fDHCPSnoopingStatisticsPort_Object=MibTableColumn
xgs360026fDHCPSnoopingStatisticsPort=_Xgs360026fDHCPSnoopingStatisticsPort_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,1),_Xgs360026fDHCPSnoopingStatisticsPort_Type())
xgs360026fDHCPSnoopingStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingStatisticsPort.setStatus(_A)
class _Xgs360026fDHCPSnoopingStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fDHCPSnoopingStatisticsClear_Type.__name__=_B
_Xgs360026fDHCPSnoopingStatisticsClear_Object=MibTableColumn
xgs360026fDHCPSnoopingStatisticsClear=_Xgs360026fDHCPSnoopingStatisticsClear_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,2),_Xgs360026fDHCPSnoopingStatisticsClear_Type())
xgs360026fDHCPSnoopingStatisticsClear.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingStatisticsClear.setStatus(_A)
_Xgs360026fDHCPSnoopingRxDiscover_Type=Counter32
_Xgs360026fDHCPSnoopingRxDiscover_Object=MibTableColumn
xgs360026fDHCPSnoopingRxDiscover=_Xgs360026fDHCPSnoopingRxDiscover_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,3),_Xgs360026fDHCPSnoopingRxDiscover_Type())
xgs360026fDHCPSnoopingRxDiscover.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingRxDiscover.setStatus(_A)
_Xgs360026fDHCPSnoopingRxOffer_Type=Counter32
_Xgs360026fDHCPSnoopingRxOffer_Object=MibTableColumn
xgs360026fDHCPSnoopingRxOffer=_Xgs360026fDHCPSnoopingRxOffer_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,4),_Xgs360026fDHCPSnoopingRxOffer_Type())
xgs360026fDHCPSnoopingRxOffer.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingRxOffer.setStatus(_A)
_Xgs360026fDHCPSnoopingRxRequest_Type=Counter32
_Xgs360026fDHCPSnoopingRxRequest_Object=MibTableColumn
xgs360026fDHCPSnoopingRxRequest=_Xgs360026fDHCPSnoopingRxRequest_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,5),_Xgs360026fDHCPSnoopingRxRequest_Type())
xgs360026fDHCPSnoopingRxRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingRxRequest.setStatus(_A)
_Xgs360026fDHCPSnoopingRxDecline_Type=Counter32
_Xgs360026fDHCPSnoopingRxDecline_Object=MibTableColumn
xgs360026fDHCPSnoopingRxDecline=_Xgs360026fDHCPSnoopingRxDecline_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,6),_Xgs360026fDHCPSnoopingRxDecline_Type())
xgs360026fDHCPSnoopingRxDecline.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingRxDecline.setStatus(_A)
_Xgs360026fDHCPSnoopingRxACK_Type=Counter32
_Xgs360026fDHCPSnoopingRxACK_Object=MibTableColumn
xgs360026fDHCPSnoopingRxACK=_Xgs360026fDHCPSnoopingRxACK_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,7),_Xgs360026fDHCPSnoopingRxACK_Type())
xgs360026fDHCPSnoopingRxACK.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingRxACK.setStatus(_A)
_Xgs360026fDHCPSnoopingRxNAK_Type=Counter32
_Xgs360026fDHCPSnoopingRxNAK_Object=MibTableColumn
xgs360026fDHCPSnoopingRxNAK=_Xgs360026fDHCPSnoopingRxNAK_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,8),_Xgs360026fDHCPSnoopingRxNAK_Type())
xgs360026fDHCPSnoopingRxNAK.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingRxNAK.setStatus(_A)
_Xgs360026fDHCPSnoopingRxRelease_Type=Counter32
_Xgs360026fDHCPSnoopingRxRelease_Object=MibTableColumn
xgs360026fDHCPSnoopingRxRelease=_Xgs360026fDHCPSnoopingRxRelease_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,9),_Xgs360026fDHCPSnoopingRxRelease_Type())
xgs360026fDHCPSnoopingRxRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingRxRelease.setStatus(_A)
_Xgs360026fDHCPSnoopingRxInform_Type=Counter32
_Xgs360026fDHCPSnoopingRxInform_Object=MibTableColumn
xgs360026fDHCPSnoopingRxInform=_Xgs360026fDHCPSnoopingRxInform_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,10),_Xgs360026fDHCPSnoopingRxInform_Type())
xgs360026fDHCPSnoopingRxInform.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingRxInform.setStatus(_A)
_Xgs360026fDHCPSnoopingRxLeaseQuery_Type=Counter32
_Xgs360026fDHCPSnoopingRxLeaseQuery_Object=MibTableColumn
xgs360026fDHCPSnoopingRxLeaseQuery=_Xgs360026fDHCPSnoopingRxLeaseQuery_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,11),_Xgs360026fDHCPSnoopingRxLeaseQuery_Type())
xgs360026fDHCPSnoopingRxLeaseQuery.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingRxLeaseQuery.setStatus(_A)
_Xgs360026fDHCPSnoopingRxLeaseUnassigned_Type=Counter32
_Xgs360026fDHCPSnoopingRxLeaseUnassigned_Object=MibTableColumn
xgs360026fDHCPSnoopingRxLeaseUnassigned=_Xgs360026fDHCPSnoopingRxLeaseUnassigned_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,12),_Xgs360026fDHCPSnoopingRxLeaseUnassigned_Type())
xgs360026fDHCPSnoopingRxLeaseUnassigned.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingRxLeaseUnassigned.setStatus(_A)
_Xgs360026fDHCPSnoopingRxLeaseUnknown_Type=Counter32
_Xgs360026fDHCPSnoopingRxLeaseUnknown_Object=MibTableColumn
xgs360026fDHCPSnoopingRxLeaseUnknown=_Xgs360026fDHCPSnoopingRxLeaseUnknown_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,13),_Xgs360026fDHCPSnoopingRxLeaseUnknown_Type())
xgs360026fDHCPSnoopingRxLeaseUnknown.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingRxLeaseUnknown.setStatus(_A)
_Xgs360026fDHCPSnoopingRxLeaseActive_Type=Counter32
_Xgs360026fDHCPSnoopingRxLeaseActive_Object=MibTableColumn
xgs360026fDHCPSnoopingRxLeaseActive=_Xgs360026fDHCPSnoopingRxLeaseActive_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,14),_Xgs360026fDHCPSnoopingRxLeaseActive_Type())
xgs360026fDHCPSnoopingRxLeaseActive.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingRxLeaseActive.setStatus(_A)
_Xgs360026fDHCPSnoopingTxDiscover_Type=Counter32
_Xgs360026fDHCPSnoopingTxDiscover_Object=MibTableColumn
xgs360026fDHCPSnoopingTxDiscover=_Xgs360026fDHCPSnoopingTxDiscover_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,15),_Xgs360026fDHCPSnoopingTxDiscover_Type())
xgs360026fDHCPSnoopingTxDiscover.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingTxDiscover.setStatus(_A)
_Xgs360026fDHCPSnoopingTxOffer_Type=Counter32
_Xgs360026fDHCPSnoopingTxOffer_Object=MibTableColumn
xgs360026fDHCPSnoopingTxOffer=_Xgs360026fDHCPSnoopingTxOffer_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,16),_Xgs360026fDHCPSnoopingTxOffer_Type())
xgs360026fDHCPSnoopingTxOffer.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingTxOffer.setStatus(_A)
_Xgs360026fDHCPSnoopingTxRequest_Type=Counter32
_Xgs360026fDHCPSnoopingTxRequest_Object=MibTableColumn
xgs360026fDHCPSnoopingTxRequest=_Xgs360026fDHCPSnoopingTxRequest_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,17),_Xgs360026fDHCPSnoopingTxRequest_Type())
xgs360026fDHCPSnoopingTxRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingTxRequest.setStatus(_A)
_Xgs360026fDHCPSnoopingTxDecline_Type=Counter32
_Xgs360026fDHCPSnoopingTxDecline_Object=MibTableColumn
xgs360026fDHCPSnoopingTxDecline=_Xgs360026fDHCPSnoopingTxDecline_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,18),_Xgs360026fDHCPSnoopingTxDecline_Type())
xgs360026fDHCPSnoopingTxDecline.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingTxDecline.setStatus(_A)
_Xgs360026fDHCPSnoopingTxACK_Type=Counter32
_Xgs360026fDHCPSnoopingTxACK_Object=MibTableColumn
xgs360026fDHCPSnoopingTxACK=_Xgs360026fDHCPSnoopingTxACK_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,19),_Xgs360026fDHCPSnoopingTxACK_Type())
xgs360026fDHCPSnoopingTxACK.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingTxACK.setStatus(_A)
_Xgs360026fDHCPSnoopingTxNAK_Type=Counter32
_Xgs360026fDHCPSnoopingTxNAK_Object=MibTableColumn
xgs360026fDHCPSnoopingTxNAK=_Xgs360026fDHCPSnoopingTxNAK_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,20),_Xgs360026fDHCPSnoopingTxNAK_Type())
xgs360026fDHCPSnoopingTxNAK.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingTxNAK.setStatus(_A)
_Xgs360026fDHCPSnoopingTxRelease_Type=Counter32
_Xgs360026fDHCPSnoopingTxRelease_Object=MibTableColumn
xgs360026fDHCPSnoopingTxRelease=_Xgs360026fDHCPSnoopingTxRelease_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,21),_Xgs360026fDHCPSnoopingTxRelease_Type())
xgs360026fDHCPSnoopingTxRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingTxRelease.setStatus(_A)
_Xgs360026fDHCPSnoopingTxInform_Type=Counter32
_Xgs360026fDHCPSnoopingTxInform_Object=MibTableColumn
xgs360026fDHCPSnoopingTxInform=_Xgs360026fDHCPSnoopingTxInform_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,22),_Xgs360026fDHCPSnoopingTxInform_Type())
xgs360026fDHCPSnoopingTxInform.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingTxInform.setStatus(_A)
_Xgs360026fDHCPSnoopingTxLeaseQuery_Type=Counter32
_Xgs360026fDHCPSnoopingTxLeaseQuery_Object=MibTableColumn
xgs360026fDHCPSnoopingTxLeaseQuery=_Xgs360026fDHCPSnoopingTxLeaseQuery_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,23),_Xgs360026fDHCPSnoopingTxLeaseQuery_Type())
xgs360026fDHCPSnoopingTxLeaseQuery.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingTxLeaseQuery.setStatus(_A)
_Xgs360026fDHCPSnoopingTxLeaseUnassigned_Type=Counter32
_Xgs360026fDHCPSnoopingTxLeaseUnassigned_Object=MibTableColumn
xgs360026fDHCPSnoopingTxLeaseUnassigned=_Xgs360026fDHCPSnoopingTxLeaseUnassigned_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,24),_Xgs360026fDHCPSnoopingTxLeaseUnassigned_Type())
xgs360026fDHCPSnoopingTxLeaseUnassigned.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingTxLeaseUnassigned.setStatus(_A)
_Xgs360026fDHCPSnoopingTxLeaseUnknown_Type=Counter32
_Xgs360026fDHCPSnoopingTxLeaseUnknown_Object=MibTableColumn
xgs360026fDHCPSnoopingTxLeaseUnknown=_Xgs360026fDHCPSnoopingTxLeaseUnknown_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,25),_Xgs360026fDHCPSnoopingTxLeaseUnknown_Type())
xgs360026fDHCPSnoopingTxLeaseUnknown.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingTxLeaseUnknown.setStatus(_A)
_Xgs360026fDHCPSnoopingTxLeaseActive_Type=Counter32
_Xgs360026fDHCPSnoopingTxLeaseActive_Object=MibTableColumn
xgs360026fDHCPSnoopingTxLeaseActive=_Xgs360026fDHCPSnoopingTxLeaseActive_Object((1,3,6,1,4,1,890,1,5,8,77,3,3,2,1,26),_Xgs360026fDHCPSnoopingTxLeaseActive_Type())
xgs360026fDHCPSnoopingTxLeaseActive.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fDHCPSnoopingTxLeaseActive.setStatus(_A)
_Xgs360026fDHCPRelay_ObjectIdentity=ObjectIdentity
xgs360026fDHCPRelay=_Xgs360026fDHCPRelay_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,4))
_Xgs360026fDHCPRelayConfiguration_ObjectIdentity=ObjectIdentity
xgs360026fDHCPRelayConfiguration=_Xgs360026fDHCPRelayConfiguration_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,4,1))
class _Xgs360026fDHCPRelayMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fDHCPRelayMode_Type.__name__=_B
_Xgs360026fDHCPRelayMode_Object=MibScalar
xgs360026fDHCPRelayMode=_Xgs360026fDHCPRelayMode_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,1,1),_Xgs360026fDHCPRelayMode_Type())
xgs360026fDHCPRelayMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fDHCPRelayMode.setStatus(_A)
_Xgs360026fDHCPRelayServer_Type=IpAddress
_Xgs360026fDHCPRelayServer_Object=MibScalar
xgs360026fDHCPRelayServer=_Xgs360026fDHCPRelayServer_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,1,2),_Xgs360026fDHCPRelayServer_Type())
xgs360026fDHCPRelayServer.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fDHCPRelayServer.setStatus(_A)
class _Xgs360026fDHCPRelayInformationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fDHCPRelayInformationMode_Type.__name__=_B
_Xgs360026fDHCPRelayInformationMode_Object=MibScalar
xgs360026fDHCPRelayInformationMode=_Xgs360026fDHCPRelayInformationMode_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,1,3),_Xgs360026fDHCPRelayInformationMode_Type())
xgs360026fDHCPRelayInformationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fDHCPRelayInformationMode.setStatus(_A)
class _Xgs360026fDHCPRelayInformationPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360026fDHCPRelayInformationPolicy_Type.__name__=_B
_Xgs360026fDHCPRelayInformationPolicy_Object=MibScalar
xgs360026fDHCPRelayInformationPolicy=_Xgs360026fDHCPRelayInformationPolicy_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,1,4),_Xgs360026fDHCPRelayInformationPolicy_Type())
xgs360026fDHCPRelayInformationPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fDHCPRelayInformationPolicy.setStatus(_A)
_Xgs360026fDHCPRelayStatistics_ObjectIdentity=ObjectIdentity
xgs360026fDHCPRelayStatistics=_Xgs360026fDHCPRelayStatistics_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,4,2))
_Xgs360026fDHCPRelayServerStatistics_ObjectIdentity=ObjectIdentity
xgs360026fDHCPRelayServerStatistics=_Xgs360026fDHCPRelayServerStatistics_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,4,2,1))
_Xgs360026fServerStatTransmitToServer_Type=Counter32
_Xgs360026fServerStatTransmitToServer_Object=MibScalar
xgs360026fServerStatTransmitToServer=_Xgs360026fServerStatTransmitToServer_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,2,1,1),_Xgs360026fServerStatTransmitToServer_Type())
xgs360026fServerStatTransmitToServer.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fServerStatTransmitToServer.setStatus(_A)
_Xgs360026fServerStatTransmitError_Type=Counter32
_Xgs360026fServerStatTransmitError_Object=MibScalar
xgs360026fServerStatTransmitError=_Xgs360026fServerStatTransmitError_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,2,1,2),_Xgs360026fServerStatTransmitError_Type())
xgs360026fServerStatTransmitError.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fServerStatTransmitError.setStatus(_A)
_Xgs360026fServerStatReceiveFromServer_Type=Counter32
_Xgs360026fServerStatReceiveFromServer_Object=MibScalar
xgs360026fServerStatReceiveFromServer=_Xgs360026fServerStatReceiveFromServer_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,2,1,3),_Xgs360026fServerStatReceiveFromServer_Type())
xgs360026fServerStatReceiveFromServer.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fServerStatReceiveFromServer.setStatus(_A)
_Xgs360026fServerStatReceiveMissingAgentOption_Type=Counter32
_Xgs360026fServerStatReceiveMissingAgentOption_Object=MibScalar
xgs360026fServerStatReceiveMissingAgentOption=_Xgs360026fServerStatReceiveMissingAgentOption_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,2,1,4),_Xgs360026fServerStatReceiveMissingAgentOption_Type())
xgs360026fServerStatReceiveMissingAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fServerStatReceiveMissingAgentOption.setStatus(_A)
_Xgs360026fServerStatReceiveMissingCircuitID_Type=Counter32
_Xgs360026fServerStatReceiveMissingCircuitID_Object=MibScalar
xgs360026fServerStatReceiveMissingCircuitID=_Xgs360026fServerStatReceiveMissingCircuitID_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,2,1,5),_Xgs360026fServerStatReceiveMissingCircuitID_Type())
xgs360026fServerStatReceiveMissingCircuitID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fServerStatReceiveMissingCircuitID.setStatus(_A)
_Xgs360026fServerStatReceiveMissingRemoteID_Type=Counter32
_Xgs360026fServerStatReceiveMissingRemoteID_Object=MibScalar
xgs360026fServerStatReceiveMissingRemoteID=_Xgs360026fServerStatReceiveMissingRemoteID_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,2,1,6),_Xgs360026fServerStatReceiveMissingRemoteID_Type())
xgs360026fServerStatReceiveMissingRemoteID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fServerStatReceiveMissingRemoteID.setStatus(_A)
_Xgs360026fServerStatReceiveBadCircuitID_Type=Counter32
_Xgs360026fServerStatReceiveBadCircuitID_Object=MibScalar
xgs360026fServerStatReceiveBadCircuitID=_Xgs360026fServerStatReceiveBadCircuitID_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,2,1,7),_Xgs360026fServerStatReceiveBadCircuitID_Type())
xgs360026fServerStatReceiveBadCircuitID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fServerStatReceiveBadCircuitID.setStatus(_A)
_Xgs360026fServerStatReceiveBadRemoteID_Type=Counter32
_Xgs360026fServerStatReceiveBadRemoteID_Object=MibScalar
xgs360026fServerStatReceiveBadRemoteID=_Xgs360026fServerStatReceiveBadRemoteID_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,2,1,8),_Xgs360026fServerStatReceiveBadRemoteID_Type())
xgs360026fServerStatReceiveBadRemoteID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fServerStatReceiveBadRemoteID.setStatus(_A)
_Xgs360026fDHCPRelayClientStatistics_ObjectIdentity=ObjectIdentity
xgs360026fDHCPRelayClientStatistics=_Xgs360026fDHCPRelayClientStatistics_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,4,2,2))
_Xgs360026fClientStatTransmitToClient_Type=Counter32
_Xgs360026fClientStatTransmitToClient_Object=MibScalar
xgs360026fClientStatTransmitToClient=_Xgs360026fClientStatTransmitToClient_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,2,2,1),_Xgs360026fClientStatTransmitToClient_Type())
xgs360026fClientStatTransmitToClient.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fClientStatTransmitToClient.setStatus(_A)
_Xgs360026fClientStatTransmitError_Type=Counter32
_Xgs360026fClientStatTransmitError_Object=MibScalar
xgs360026fClientStatTransmitError=_Xgs360026fClientStatTransmitError_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,2,2,2),_Xgs360026fClientStatTransmitError_Type())
xgs360026fClientStatTransmitError.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fClientStatTransmitError.setStatus(_A)
_Xgs360026fClientStatReceivefromClient_Type=Counter32
_Xgs360026fClientStatReceivefromClient_Object=MibScalar
xgs360026fClientStatReceivefromClient=_Xgs360026fClientStatReceivefromClient_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,2,2,3),_Xgs360026fClientStatReceivefromClient_Type())
xgs360026fClientStatReceivefromClient.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fClientStatReceivefromClient.setStatus(_A)
_Xgs360026fClientStatReceiveAgentOption_Type=Counter32
_Xgs360026fClientStatReceiveAgentOption_Object=MibScalar
xgs360026fClientStatReceiveAgentOption=_Xgs360026fClientStatReceiveAgentOption_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,2,2,4),_Xgs360026fClientStatReceiveAgentOption_Type())
xgs360026fClientStatReceiveAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fClientStatReceiveAgentOption.setStatus(_A)
_Xgs360026fClientStatReplaceAgentOption_Type=Counter32
_Xgs360026fClientStatReplaceAgentOption_Object=MibScalar
xgs360026fClientStatReplaceAgentOption=_Xgs360026fClientStatReplaceAgentOption_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,2,2,5),_Xgs360026fClientStatReplaceAgentOption_Type())
xgs360026fClientStatReplaceAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fClientStatReplaceAgentOption.setStatus(_A)
_Xgs360026fClientStatKeepAgentOption_Type=Counter32
_Xgs360026fClientStatKeepAgentOption_Object=MibScalar
xgs360026fClientStatKeepAgentOption=_Xgs360026fClientStatKeepAgentOption_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,2,2,6),_Xgs360026fClientStatKeepAgentOption_Type())
xgs360026fClientStatKeepAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fClientStatKeepAgentOption.setStatus(_A)
_Xgs360026fClientStatDropAgentOption_Type=Counter32
_Xgs360026fClientStatDropAgentOption_Object=MibScalar
xgs360026fClientStatDropAgentOption=_Xgs360026fClientStatDropAgentOption_Object((1,3,6,1,4,1,890,1,5,8,77,3,4,2,2,7),_Xgs360026fClientStatDropAgentOption_Type())
xgs360026fClientStatDropAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fClientStatDropAgentOption.setStatus(_A)
_Xgs360026fPortSecurity_ObjectIdentity=ObjectIdentity
xgs360026fPortSecurity=_Xgs360026fPortSecurity_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,5))
_Xgs360026fPortSecLimitCtrl_ObjectIdentity=ObjectIdentity
xgs360026fPortSecLimitCtrl=_Xgs360026fPortSecLimitCtrl_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,5,1))
_Xgs360026fPortSecLimitCtrlSystemConf_ObjectIdentity=ObjectIdentity
xgs360026fPortSecLimitCtrlSystemConf=_Xgs360026fPortSecLimitCtrlSystemConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,5,1,1))
class _Xgs360026fPortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fPortSecurityMode_Type.__name__=_B
_Xgs360026fPortSecurityMode_Object=MibScalar
xgs360026fPortSecurityMode=_Xgs360026fPortSecurityMode_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,1,1,1),_Xgs360026fPortSecurityMode_Type())
xgs360026fPortSecurityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortSecurityMode.setStatus(_A)
class _Xgs360026fPortSecurityAging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fPortSecurityAging_Type.__name__=_B
_Xgs360026fPortSecurityAging_Object=MibScalar
xgs360026fPortSecurityAging=_Xgs360026fPortSecurityAging_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,1,1,2),_Xgs360026fPortSecurityAging_Type())
xgs360026fPortSecurityAging.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortSecurityAging.setStatus(_A)
class _Xgs360026fPortSecurityAgingPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10000000))
_Xgs360026fPortSecurityAgingPeriod_Type.__name__=_B
_Xgs360026fPortSecurityAgingPeriod_Object=MibScalar
xgs360026fPortSecurityAgingPeriod=_Xgs360026fPortSecurityAgingPeriod_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,1,1,3),_Xgs360026fPortSecurityAgingPeriod_Type())
xgs360026fPortSecurityAgingPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortSecurityAgingPeriod.setStatus(_A)
_Xgs360026fPortSecLimitCtrlTable_Object=MibTable
xgs360026fPortSecLimitCtrlTable=_Xgs360026fPortSecLimitCtrlTable_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,1,2))
if mibBuilder.loadTexts:xgs360026fPortSecLimitCtrlTable.setStatus(_A)
_Xgs360026fPortSecLimitCtrlEntry_Object=MibTableRow
xgs360026fPortSecLimitCtrlEntry=_Xgs360026fPortSecLimitCtrlEntry_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,1,2,1))
xgs360026fPortSecLimitCtrlEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:xgs360026fPortSecLimitCtrlEntry.setStatus(_A)
class _Xgs360026fPortSecLimitCtrlPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fPortSecLimitCtrlPort_Type.__name__=_B
_Xgs360026fPortSecLimitCtrlPort_Object=MibTableColumn
xgs360026fPortSecLimitCtrlPort=_Xgs360026fPortSecLimitCtrlPort_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,1,2,1,1),_Xgs360026fPortSecLimitCtrlPort_Type())
xgs360026fPortSecLimitCtrlPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fPortSecLimitCtrlPort.setStatus(_A)
class _Xgs360026fPortSecLimitCtrlPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fPortSecLimitCtrlPortMode_Type.__name__=_B
_Xgs360026fPortSecLimitCtrlPortMode_Object=MibTableColumn
xgs360026fPortSecLimitCtrlPortMode=_Xgs360026fPortSecLimitCtrlPortMode_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,1,2,1,2),_Xgs360026fPortSecLimitCtrlPortMode_Type())
xgs360026fPortSecLimitCtrlPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortSecLimitCtrlPortMode.setStatus(_A)
class _Xgs360026fPortSecLimitCtrlPortLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Xgs360026fPortSecLimitCtrlPortLimit_Type.__name__=_B
_Xgs360026fPortSecLimitCtrlPortLimit_Object=MibTableColumn
xgs360026fPortSecLimitCtrlPortLimit=_Xgs360026fPortSecLimitCtrlPortLimit_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,1,2,1,3),_Xgs360026fPortSecLimitCtrlPortLimit_Type())
xgs360026fPortSecLimitCtrlPortLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortSecLimitCtrlPortLimit.setStatus(_A)
class _Xgs360026fPortSecLimitCtrlPortAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360026fPortSecLimitCtrlPortAction_Type.__name__=_B
_Xgs360026fPortSecLimitCtrlPortAction_Object=MibTableColumn
xgs360026fPortSecLimitCtrlPortAction=_Xgs360026fPortSecLimitCtrlPortAction_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,1,2,1,4),_Xgs360026fPortSecLimitCtrlPortAction_Type())
xgs360026fPortSecLimitCtrlPortAction.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortSecLimitCtrlPortAction.setStatus(_A)
_Xgs360026fPortSecLimitCtrlPortState_Type=DisplayString
_Xgs360026fPortSecLimitCtrlPortState_Object=MibTableColumn
xgs360026fPortSecLimitCtrlPortState=_Xgs360026fPortSecLimitCtrlPortState_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,1,2,1,5),_Xgs360026fPortSecLimitCtrlPortState_Type())
xgs360026fPortSecLimitCtrlPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortSecLimitCtrlPortState.setStatus(_A)
class _Xgs360026fPortSecLimitCtrlPortReOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fPortSecLimitCtrlPortReOpen_Type.__name__=_B
_Xgs360026fPortSecLimitCtrlPortReOpen_Object=MibTableColumn
xgs360026fPortSecLimitCtrlPortReOpen=_Xgs360026fPortSecLimitCtrlPortReOpen_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,1,2,1,6),_Xgs360026fPortSecLimitCtrlPortReOpen_Type())
xgs360026fPortSecLimitCtrlPortReOpen.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortSecLimitCtrlPortReOpen.setStatus(_A)
_Xgs360026fPortSecSwitchStatusTable_Object=MibTable
xgs360026fPortSecSwitchStatusTable=_Xgs360026fPortSecSwitchStatusTable_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,2))
if mibBuilder.loadTexts:xgs360026fPortSecSwitchStatusTable.setStatus(_A)
_Xgs360026fPortSecSwitchStatusEntry_Object=MibTableRow
xgs360026fPortSecSwitchStatusEntry=_Xgs360026fPortSecSwitchStatusEntry_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,2,1))
xgs360026fPortSecSwitchStatusEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:xgs360026fPortSecSwitchStatusEntry.setStatus(_A)
class _Xgs360026fPortSecSwitchStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fPortSecSwitchStatusPort_Type.__name__=_B
_Xgs360026fPortSecSwitchStatusPort_Object=MibTableColumn
xgs360026fPortSecSwitchStatusPort=_Xgs360026fPortSecSwitchStatusPort_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,2,1,1),_Xgs360026fPortSecSwitchStatusPort_Type())
xgs360026fPortSecSwitchStatusPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fPortSecSwitchStatusPort.setStatus(_A)
_Xgs360026fPortSecSwitchStatusUsers_Type=DisplayString
_Xgs360026fPortSecSwitchStatusUsers_Object=MibTableColumn
xgs360026fPortSecSwitchStatusUsers=_Xgs360026fPortSecSwitchStatusUsers_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,2,1,2),_Xgs360026fPortSecSwitchStatusUsers_Type())
xgs360026fPortSecSwitchStatusUsers.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortSecSwitchStatusUsers.setStatus(_A)
_Xgs360026fPortSecSwitchStatusState_Type=DisplayString
_Xgs360026fPortSecSwitchStatusState_Object=MibTableColumn
xgs360026fPortSecSwitchStatusState=_Xgs360026fPortSecSwitchStatusState_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,2,1,3),_Xgs360026fPortSecSwitchStatusState_Type())
xgs360026fPortSecSwitchStatusState.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortSecSwitchStatusState.setStatus(_A)
class _Xgs360026fPortSecSwitchStatusMACCountCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fPortSecSwitchStatusMACCountCurrent_Type.__name__=_B
_Xgs360026fPortSecSwitchStatusMACCountCurrent_Object=MibTableColumn
xgs360026fPortSecSwitchStatusMACCountCurrent=_Xgs360026fPortSecSwitchStatusMACCountCurrent_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,2,1,4),_Xgs360026fPortSecSwitchStatusMACCountCurrent_Type())
xgs360026fPortSecSwitchStatusMACCountCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortSecSwitchStatusMACCountCurrent.setStatus(_A)
class _Xgs360026fPortSecSwitchStatusMACCountLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fPortSecSwitchStatusMACCountLimit_Type.__name__=_B
_Xgs360026fPortSecSwitchStatusMACCountLimit_Object=MibTableColumn
xgs360026fPortSecSwitchStatusMACCountLimit=_Xgs360026fPortSecSwitchStatusMACCountLimit_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,2,1,5),_Xgs360026fPortSecSwitchStatusMACCountLimit_Type())
xgs360026fPortSecSwitchStatusMACCountLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortSecSwitchStatusMACCountLimit.setStatus(_A)
_Xgs360026fPortSecPortStatus_ObjectIdentity=ObjectIdentity
xgs360026fPortSecPortStatus=_Xgs360026fPortSecPortStatus_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,5,3))
class _Xgs360026fPortSecPortStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fPortSecPortStatusPort_Type.__name__=_B
_Xgs360026fPortSecPortStatusPort_Object=MibScalar
xgs360026fPortSecPortStatusPort=_Xgs360026fPortSecPortStatusPort_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,3,1),_Xgs360026fPortSecPortStatusPort_Type())
xgs360026fPortSecPortStatusPort.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPortSecPortStatusPort.setStatus(_A)
_Xgs360026fPortSecPortStatusTable_Object=MibTable
xgs360026fPortSecPortStatusTable=_Xgs360026fPortSecPortStatusTable_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,3,2))
if mibBuilder.loadTexts:xgs360026fPortSecPortStatusTable.setStatus(_A)
_Xgs360026fPortSecPortStatusEntry_Object=MibTableRow
xgs360026fPortSecPortStatusEntry=_Xgs360026fPortSecPortStatusEntry_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,3,2,1))
xgs360026fPortSecPortStatusEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:xgs360026fPortSecPortStatusEntry.setStatus(_A)
class _Xgs360026fPortSecPortStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fPortSecPortStatusIndex_Type.__name__=_B
_Xgs360026fPortSecPortStatusIndex_Object=MibTableColumn
xgs360026fPortSecPortStatusIndex=_Xgs360026fPortSecPortStatusIndex_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,3,2,1,1),_Xgs360026fPortSecPortStatusIndex_Type())
xgs360026fPortSecPortStatusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fPortSecPortStatusIndex.setStatus(_A)
_Xgs360026fPortSecPortStatusMACAddress_Type=MacAddress
_Xgs360026fPortSecPortStatusMACAddress_Object=MibTableColumn
xgs360026fPortSecPortStatusMACAddress=_Xgs360026fPortSecPortStatusMACAddress_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,3,2,1,2),_Xgs360026fPortSecPortStatusMACAddress_Type())
xgs360026fPortSecPortStatusMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortSecPortStatusMACAddress.setStatus(_A)
class _Xgs360026fPortSecPortStatusVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Xgs360026fPortSecPortStatusVLANId_Type.__name__=_B
_Xgs360026fPortSecPortStatusVLANId_Object=MibTableColumn
xgs360026fPortSecPortStatusVLANId=_Xgs360026fPortSecPortStatusVLANId_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,3,2,1,3),_Xgs360026fPortSecPortStatusVLANId_Type())
xgs360026fPortSecPortStatusVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortSecPortStatusVLANId.setStatus(_A)
_Xgs360026fPortSecPortStatusState_Type=DisplayString
_Xgs360026fPortSecPortStatusState_Object=MibTableColumn
xgs360026fPortSecPortStatusState=_Xgs360026fPortSecPortStatusState_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,3,2,1,4),_Xgs360026fPortSecPortStatusState_Type())
xgs360026fPortSecPortStatusState.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortSecPortStatusState.setStatus(_A)
_Xgs360026fPortSecPortStatusTimeOfAddition_Type=DisplayString
_Xgs360026fPortSecPortStatusTimeOfAddition_Object=MibTableColumn
xgs360026fPortSecPortStatusTimeOfAddition=_Xgs360026fPortSecPortStatusTimeOfAddition_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,3,2,1,5),_Xgs360026fPortSecPortStatusTimeOfAddition_Type())
xgs360026fPortSecPortStatusTimeOfAddition.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortSecPortStatusTimeOfAddition.setStatus(_A)
_Xgs360026fPortSecPortStatusAgeAndHold_Type=DisplayString
_Xgs360026fPortSecPortStatusAgeAndHold_Object=MibTableColumn
xgs360026fPortSecPortStatusAgeAndHold=_Xgs360026fPortSecPortStatusAgeAndHold_Object((1,3,6,1,4,1,890,1,5,8,77,3,5,3,2,1,6),_Xgs360026fPortSecPortStatusAgeAndHold_Type())
xgs360026fPortSecPortStatusAgeAndHold.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPortSecPortStatusAgeAndHold.setStatus(_A)
_Xgs360026fAccessManagement_ObjectIdentity=ObjectIdentity
xgs360026fAccessManagement=_Xgs360026fAccessManagement_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,6))
_Xgs360026fAccessMgtConf_ObjectIdentity=ObjectIdentity
xgs360026fAccessMgtConf=_Xgs360026fAccessMgtConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,6,1))
class _Xgs360026fAccessMgtConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fAccessMgtConfMode_Type.__name__=_B
_Xgs360026fAccessMgtConfMode_Object=MibScalar
xgs360026fAccessMgtConfMode=_Xgs360026fAccessMgtConfMode_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,1,1),_Xgs360026fAccessMgtConfMode_Type())
xgs360026fAccessMgtConfMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fAccessMgtConfMode.setStatus(_A)
class _Xgs360026fAccessMgtConfCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fAccessMgtConfCreate_Type.__name__=_B
_Xgs360026fAccessMgtConfCreate_Object=MibScalar
xgs360026fAccessMgtConfCreate=_Xgs360026fAccessMgtConfCreate_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,1,2),_Xgs360026fAccessMgtConfCreate_Type())
xgs360026fAccessMgtConfCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fAccessMgtConfCreate.setStatus(_A)
_Xgs360026fAccessMgtConfTable_Object=MibTable
xgs360026fAccessMgtConfTable=_Xgs360026fAccessMgtConfTable_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,1,3))
if mibBuilder.loadTexts:xgs360026fAccessMgtConfTable.setStatus(_A)
_Xgs360026fAccessMgtConfEntry_Object=MibTableRow
xgs360026fAccessMgtConfEntry=_Xgs360026fAccessMgtConfEntry_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,1,3,1))
xgs360026fAccessMgtConfEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:xgs360026fAccessMgtConfEntry.setStatus(_A)
class _Xgs360026fAccessMgtIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Xgs360026fAccessMgtIndex_Type.__name__=_B
_Xgs360026fAccessMgtIndex_Object=MibTableColumn
xgs360026fAccessMgtIndex=_Xgs360026fAccessMgtIndex_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,1,3,1,1),_Xgs360026fAccessMgtIndex_Type())
xgs360026fAccessMgtIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fAccessMgtIndex.setStatus(_A)
class _Xgs360026fAccessMgtAddresstype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fAccessMgtAddresstype_Type.__name__=_B
_Xgs360026fAccessMgtAddresstype_Object=MibTableColumn
xgs360026fAccessMgtAddresstype=_Xgs360026fAccessMgtAddresstype_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,1,3,1,2),_Xgs360026fAccessMgtAddresstype_Type())
xgs360026fAccessMgtAddresstype.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fAccessMgtAddresstype.setStatus(_A)
_Xgs360026fAccessMgtStartIpAddress_Type=DisplayString
_Xgs360026fAccessMgtStartIpAddress_Object=MibTableColumn
xgs360026fAccessMgtStartIpAddress=_Xgs360026fAccessMgtStartIpAddress_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,1,3,1,3),_Xgs360026fAccessMgtStartIpAddress_Type())
xgs360026fAccessMgtStartIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fAccessMgtStartIpAddress.setStatus(_A)
_Xgs360026fAccessMgtEndIpAddress_Type=DisplayString
_Xgs360026fAccessMgtEndIpAddress_Object=MibTableColumn
xgs360026fAccessMgtEndIpAddress=_Xgs360026fAccessMgtEndIpAddress_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,1,3,1,4),_Xgs360026fAccessMgtEndIpAddress_Type())
xgs360026fAccessMgtEndIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fAccessMgtEndIpAddress.setStatus(_A)
class _Xgs360026fAccessMgtHttpHttps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fAccessMgtHttpHttps_Type.__name__=_B
_Xgs360026fAccessMgtHttpHttps_Object=MibTableColumn
xgs360026fAccessMgtHttpHttps=_Xgs360026fAccessMgtHttpHttps_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,1,3,1,5),_Xgs360026fAccessMgtHttpHttps_Type())
xgs360026fAccessMgtHttpHttps.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fAccessMgtHttpHttps.setStatus(_A)
class _Xgs360026fAccessMgtSNMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fAccessMgtSNMP_Type.__name__=_B
_Xgs360026fAccessMgtSNMP_Object=MibTableColumn
xgs360026fAccessMgtSNMP=_Xgs360026fAccessMgtSNMP_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,1,3,1,6),_Xgs360026fAccessMgtSNMP_Type())
xgs360026fAccessMgtSNMP.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fAccessMgtSNMP.setStatus(_A)
class _Xgs360026fAccessMgtTelnetSSH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fAccessMgtTelnetSSH_Type.__name__=_B
_Xgs360026fAccessMgtTelnetSSH_Object=MibTableColumn
xgs360026fAccessMgtTelnetSSH=_Xgs360026fAccessMgtTelnetSSH_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,1,3,1,7),_Xgs360026fAccessMgtTelnetSSH_Type())
xgs360026fAccessMgtTelnetSSH.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fAccessMgtTelnetSSH.setStatus(_A)
class _Xgs360026fAccessMgtRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360026fAccessMgtRowStatus_Type.__name__=_B
_Xgs360026fAccessMgtRowStatus_Object=MibTableColumn
xgs360026fAccessMgtRowStatus=_Xgs360026fAccessMgtRowStatus_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,1,3,1,8),_Xgs360026fAccessMgtRowStatus_Type())
xgs360026fAccessMgtRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fAccessMgtRowStatus.setStatus(_A)
_Xgs360026fAccessMgtStatistics_ObjectIdentity=ObjectIdentity
xgs360026fAccessMgtStatistics=_Xgs360026fAccessMgtStatistics_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,6,2))
_Xgs360026fHttpReceivedPkts_Type=Counter32
_Xgs360026fHttpReceivedPkts_Object=MibScalar
xgs360026fHttpReceivedPkts=_Xgs360026fHttpReceivedPkts_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,1),_Xgs360026fHttpReceivedPkts_Type())
xgs360026fHttpReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fHttpReceivedPkts.setStatus(_A)
_Xgs360026fHttpAllowedPkts_Type=Counter32
_Xgs360026fHttpAllowedPkts_Object=MibScalar
xgs360026fHttpAllowedPkts=_Xgs360026fHttpAllowedPkts_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,2),_Xgs360026fHttpAllowedPkts_Type())
xgs360026fHttpAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fHttpAllowedPkts.setStatus(_A)
_Xgs360026fHttpDiscardedPkts_Type=Counter32
_Xgs360026fHttpDiscardedPkts_Object=MibScalar
xgs360026fHttpDiscardedPkts=_Xgs360026fHttpDiscardedPkts_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,3),_Xgs360026fHttpDiscardedPkts_Type())
xgs360026fHttpDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fHttpDiscardedPkts.setStatus(_A)
_Xgs360026fHttpsReceivedPkts_Type=Counter32
_Xgs360026fHttpsReceivedPkts_Object=MibScalar
xgs360026fHttpsReceivedPkts=_Xgs360026fHttpsReceivedPkts_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,4),_Xgs360026fHttpsReceivedPkts_Type())
xgs360026fHttpsReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fHttpsReceivedPkts.setStatus(_A)
_Xgs360026fHttpsAllowedPkts_Type=Counter32
_Xgs360026fHttpsAllowedPkts_Object=MibScalar
xgs360026fHttpsAllowedPkts=_Xgs360026fHttpsAllowedPkts_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,5),_Xgs360026fHttpsAllowedPkts_Type())
xgs360026fHttpsAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fHttpsAllowedPkts.setStatus(_A)
_Xgs360026fHttpsDiscardedPkts_Type=Counter32
_Xgs360026fHttpsDiscardedPkts_Object=MibScalar
xgs360026fHttpsDiscardedPkts=_Xgs360026fHttpsDiscardedPkts_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,6),_Xgs360026fHttpsDiscardedPkts_Type())
xgs360026fHttpsDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fHttpsDiscardedPkts.setStatus(_A)
_Xgs360026fSnmpReceivedPkts_Type=Counter32
_Xgs360026fSnmpReceivedPkts_Object=MibScalar
xgs360026fSnmpReceivedPkts=_Xgs360026fSnmpReceivedPkts_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,7),_Xgs360026fSnmpReceivedPkts_Type())
xgs360026fSnmpReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSnmpReceivedPkts.setStatus(_A)
_Xgs360026fSnmpAllowedPkts_Type=Counter32
_Xgs360026fSnmpAllowedPkts_Object=MibScalar
xgs360026fSnmpAllowedPkts=_Xgs360026fSnmpAllowedPkts_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,8),_Xgs360026fSnmpAllowedPkts_Type())
xgs360026fSnmpAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSnmpAllowedPkts.setStatus(_A)
_Xgs360026fSnmpDiscardedPkts_Type=Counter32
_Xgs360026fSnmpDiscardedPkts_Object=MibScalar
xgs360026fSnmpDiscardedPkts=_Xgs360026fSnmpDiscardedPkts_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,9),_Xgs360026fSnmpDiscardedPkts_Type())
xgs360026fSnmpDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSnmpDiscardedPkts.setStatus(_A)
_Xgs360026fTelnetReceivedPkts_Type=Counter32
_Xgs360026fTelnetReceivedPkts_Object=MibScalar
xgs360026fTelnetReceivedPkts=_Xgs360026fTelnetReceivedPkts_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,10),_Xgs360026fTelnetReceivedPkts_Type())
xgs360026fTelnetReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fTelnetReceivedPkts.setStatus(_A)
_Xgs360026fTelnetAllowedPkts_Type=Counter32
_Xgs360026fTelnetAllowedPkts_Object=MibScalar
xgs360026fTelnetAllowedPkts=_Xgs360026fTelnetAllowedPkts_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,11),_Xgs360026fTelnetAllowedPkts_Type())
xgs360026fTelnetAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fTelnetAllowedPkts.setStatus(_A)
_Xgs360026fTelnetDiscardedPkts_Type=Counter32
_Xgs360026fTelnetDiscardedPkts_Object=MibScalar
xgs360026fTelnetDiscardedPkts=_Xgs360026fTelnetDiscardedPkts_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,12),_Xgs360026fTelnetDiscardedPkts_Type())
xgs360026fTelnetDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fTelnetDiscardedPkts.setStatus(_A)
_Xgs360026fSSHReceivedPkts_Type=Counter32
_Xgs360026fSSHReceivedPkts_Object=MibScalar
xgs360026fSSHReceivedPkts=_Xgs360026fSSHReceivedPkts_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,13),_Xgs360026fSSHReceivedPkts_Type())
xgs360026fSSHReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSSHReceivedPkts.setStatus(_A)
_Xgs360026fSSHAllowedPkts_Type=Counter32
_Xgs360026fSSHAllowedPkts_Object=MibScalar
xgs360026fSSHAllowedPkts=_Xgs360026fSSHAllowedPkts_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,14),_Xgs360026fSSHAllowedPkts_Type())
xgs360026fSSHAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSSHAllowedPkts.setStatus(_A)
_Xgs360026fSSHDiscardedPkts_Type=Counter32
_Xgs360026fSSHDiscardedPkts_Object=MibScalar
xgs360026fSSHDiscardedPkts=_Xgs360026fSSHDiscardedPkts_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,15),_Xgs360026fSSHDiscardedPkts_Type())
xgs360026fSSHDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fSSHDiscardedPkts.setStatus(_A)
class _Xgs360026fAccessMgtStatisticsClearAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fAccessMgtStatisticsClearAll_Type.__name__=_B
_Xgs360026fAccessMgtStatisticsClearAll_Object=MibScalar
xgs360026fAccessMgtStatisticsClearAll=_Xgs360026fAccessMgtStatisticsClearAll_Object((1,3,6,1,4,1,890,1,5,8,77,3,6,2,16),_Xgs360026fAccessMgtStatisticsClearAll_Type())
xgs360026fAccessMgtStatisticsClearAll.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fAccessMgtStatisticsClearAll.setStatus(_A)
_Xgs360026fSSH_ObjectIdentity=ObjectIdentity
xgs360026fSSH=_Xgs360026fSSH_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,7))
class _Xgs360026fSSHMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fSSHMode_Type.__name__=_B
_Xgs360026fSSHMode_Object=MibScalar
xgs360026fSSHMode=_Xgs360026fSSHMode_Object((1,3,6,1,4,1,890,1,5,8,77,3,7,1),_Xgs360026fSSHMode_Type())
xgs360026fSSHMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSSHMode.setStatus(_A)
_Xgs360026fHTTPS_ObjectIdentity=ObjectIdentity
xgs360026fHTTPS=_Xgs360026fHTTPS_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,8))
class _Xgs360026fHTTPSMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fHTTPSMode_Type.__name__=_B
_Xgs360026fHTTPSMode_Object=MibScalar
xgs360026fHTTPSMode=_Xgs360026fHTTPSMode_Object((1,3,6,1,4,1,890,1,5,8,77,3,8,1),_Xgs360026fHTTPSMode_Type())
xgs360026fHTTPSMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fHTTPSMode.setStatus(_A)
class _Xgs360026fHTTPSAutoRedirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fHTTPSAutoRedirect_Type.__name__=_B
_Xgs360026fHTTPSAutoRedirect_Object=MibScalar
xgs360026fHTTPSAutoRedirect=_Xgs360026fHTTPSAutoRedirect_Object((1,3,6,1,4,1,890,1,5,8,77,3,8,2),_Xgs360026fHTTPSAutoRedirect_Type())
xgs360026fHTTPSAutoRedirect.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fHTTPSAutoRedirect.setStatus(_A)
_Xgs360026fAuthMethod_ObjectIdentity=ObjectIdentity
xgs360026fAuthMethod=_Xgs360026fAuthMethod_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,3,9))
class _Xgs360026fConsoleAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360026fConsoleAuthMethod_Type.__name__=_B
_Xgs360026fConsoleAuthMethod_Object=MibScalar
xgs360026fConsoleAuthMethod=_Xgs360026fConsoleAuthMethod_Object((1,3,6,1,4,1,890,1,5,8,77,3,9,1),_Xgs360026fConsoleAuthMethod_Type())
xgs360026fConsoleAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fConsoleAuthMethod.setStatus(_A)
class _Xgs360026fConsoleFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fConsoleFallback_Type.__name__=_B
_Xgs360026fConsoleFallback_Object=MibScalar
xgs360026fConsoleFallback=_Xgs360026fConsoleFallback_Object((1,3,6,1,4,1,890,1,5,8,77,3,9,2),_Xgs360026fConsoleFallback_Type())
xgs360026fConsoleFallback.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fConsoleFallback.setStatus(_A)
class _Xgs360026fTelnetAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360026fTelnetAuthMethod_Type.__name__=_B
_Xgs360026fTelnetAuthMethod_Object=MibScalar
xgs360026fTelnetAuthMethod=_Xgs360026fTelnetAuthMethod_Object((1,3,6,1,4,1,890,1,5,8,77,3,9,3),_Xgs360026fTelnetAuthMethod_Type())
xgs360026fTelnetAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTelnetAuthMethod.setStatus(_A)
class _Xgs360026fTelnetFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fTelnetFallback_Type.__name__=_B
_Xgs360026fTelnetFallback_Object=MibScalar
xgs360026fTelnetFallback=_Xgs360026fTelnetFallback_Object((1,3,6,1,4,1,890,1,5,8,77,3,9,4),_Xgs360026fTelnetFallback_Type())
xgs360026fTelnetFallback.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fTelnetFallback.setStatus(_A)
class _Xgs360026fSshAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360026fSshAuthMethod_Type.__name__=_B
_Xgs360026fSshAuthMethod_Object=MibScalar
xgs360026fSshAuthMethod=_Xgs360026fSshAuthMethod_Object((1,3,6,1,4,1,890,1,5,8,77,3,9,5),_Xgs360026fSshAuthMethod_Type())
xgs360026fSshAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSshAuthMethod.setStatus(_A)
class _Xgs360026fSshFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fSshFallback_Type.__name__=_B
_Xgs360026fSshFallback_Object=MibScalar
xgs360026fSshFallback=_Xgs360026fSshFallback_Object((1,3,6,1,4,1,890,1,5,8,77,3,9,6),_Xgs360026fSshFallback_Type())
xgs360026fSshFallback.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSshFallback.setStatus(_A)
class _Xgs360026fWebAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360026fWebAuthMethod_Type.__name__=_B
_Xgs360026fWebAuthMethod_Object=MibScalar
xgs360026fWebAuthMethod=_Xgs360026fWebAuthMethod_Object((1,3,6,1,4,1,890,1,5,8,77,3,9,7),_Xgs360026fWebAuthMethod_Type())
xgs360026fWebAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fWebAuthMethod.setStatus(_A)
class _Xgs360026fWebFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fWebFallback_Type.__name__=_B
_Xgs360026fWebFallback_Object=MibScalar
xgs360026fWebFallback=_Xgs360026fWebFallback_Object((1,3,6,1,4,1,890,1,5,8,77,3,9,8),_Xgs360026fWebFallback_Type())
xgs360026fWebFallback.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fWebFallback.setStatus(_A)
_Xgs360026fMaintenance_ObjectIdentity=ObjectIdentity
xgs360026fMaintenance=_Xgs360026fMaintenance_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,4))
class _Xgs360026fRestartDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fRestartDevice_Type.__name__=_B
_Xgs360026fRestartDevice_Object=MibScalar
xgs360026fRestartDevice=_Xgs360026fRestartDevice_Object((1,3,6,1,4,1,890,1,5,8,77,4,1),_Xgs360026fRestartDevice_Type())
xgs360026fRestartDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fRestartDevice.setStatus(_A)
_Xgs360026fFirmware_ObjectIdentity=ObjectIdentity
xgs360026fFirmware=_Xgs360026fFirmware_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,4,2))
_Xgs360026fFirmwareIpAddress_Type=IpAddress
_Xgs360026fFirmwareIpAddress_Object=MibScalar
xgs360026fFirmwareIpAddress=_Xgs360026fFirmwareIpAddress_Object((1,3,6,1,4,1,890,1,5,8,77,4,2,1),_Xgs360026fFirmwareIpAddress_Type())
xgs360026fFirmwareIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fFirmwareIpAddress.setStatus(_A)
_Xgs360026fFirmwareFileName_Type=DisplayString
_Xgs360026fFirmwareFileName_Object=MibScalar
xgs360026fFirmwareFileName=_Xgs360026fFirmwareFileName_Object((1,3,6,1,4,1,890,1,5,8,77,4,2,2),_Xgs360026fFirmwareFileName_Type())
xgs360026fFirmwareFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fFirmwareFileName.setStatus(_A)
class _Xgs360026fDoFirmwareUpgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fDoFirmwareUpgrade_Type.__name__=_B
_Xgs360026fDoFirmwareUpgrade_Object=MibScalar
xgs360026fDoFirmwareUpgrade=_Xgs360026fDoFirmwareUpgrade_Object((1,3,6,1,4,1,890,1,5,8,77,4,2,3),_Xgs360026fDoFirmwareUpgrade_Type())
xgs360026fDoFirmwareUpgrade.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fDoFirmwareUpgrade.setStatus(_A)
_Xgs360026fSaveOrRestore_ObjectIdentity=ObjectIdentity
xgs360026fSaveOrRestore=_Xgs360026fSaveOrRestore_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,4,3))
class _Xgs360026fFactoryDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fFactoryDefaults_Type.__name__=_B
_Xgs360026fFactoryDefaults_Object=MibScalar
xgs360026fFactoryDefaults=_Xgs360026fFactoryDefaults_Object((1,3,6,1,4,1,890,1,5,8,77,4,3,1),_Xgs360026fFactoryDefaults_Type())
xgs360026fFactoryDefaults.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fFactoryDefaults.setStatus(_A)
class _Xgs360026fSaveStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fSaveStart_Type.__name__=_B
_Xgs360026fSaveStart_Object=MibScalar
xgs360026fSaveStart=_Xgs360026fSaveStart_Object((1,3,6,1,4,1,890,1,5,8,77,4,3,2),_Xgs360026fSaveStart_Type())
xgs360026fSaveStart.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSaveStart.setStatus(_A)
class _Xgs360026fSaveUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fSaveUser_Type.__name__=_B
_Xgs360026fSaveUser_Object=MibScalar
xgs360026fSaveUser=_Xgs360026fSaveUser_Object((1,3,6,1,4,1,890,1,5,8,77,4,3,3),_Xgs360026fSaveUser_Type())
xgs360026fSaveUser.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fSaveUser.setStatus(_A)
class _Xgs360026fRestoreUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360026fRestoreUser_Type.__name__=_B
_Xgs360026fRestoreUser_Object=MibScalar
xgs360026fRestoreUser=_Xgs360026fRestoreUser_Object((1,3,6,1,4,1,890,1,5,8,77,4,3,4),_Xgs360026fRestoreUser_Type())
xgs360026fRestoreUser.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fRestoreUser.setStatus(_A)
_Xgs360026fExportOrImport_ObjectIdentity=ObjectIdentity
xgs360026fExportOrImport=_Xgs360026fExportOrImport_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,4,4))
_Xgs360026fExportIpAddress_Type=IpAddress
_Xgs360026fExportIpAddress_Object=MibScalar
xgs360026fExportIpAddress=_Xgs360026fExportIpAddress_Object((1,3,6,1,4,1,890,1,5,8,77,4,4,1),_Xgs360026fExportIpAddress_Type())
xgs360026fExportIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fExportIpAddress.setStatus(_A)
_Xgs360026fExportConfigName_Type=DisplayString
_Xgs360026fExportConfigName_Object=MibScalar
xgs360026fExportConfigName=_Xgs360026fExportConfigName_Object((1,3,6,1,4,1,890,1,5,8,77,4,4,2),_Xgs360026fExportConfigName_Type())
xgs360026fExportConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fExportConfigName.setStatus(_A)
class _Xgs360026fDoExportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Xgs360026fDoExportConfig_Type.__name__=_B
_Xgs360026fDoExportConfig_Object=MibScalar
xgs360026fDoExportConfig=_Xgs360026fDoExportConfig_Object((1,3,6,1,4,1,890,1,5,8,77,4,4,3),_Xgs360026fDoExportConfig_Type())
xgs360026fDoExportConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fDoExportConfig.setStatus(_A)
_Xgs360026fImportIpAddress_Type=IpAddress
_Xgs360026fImportIpAddress_Object=MibScalar
xgs360026fImportIpAddress=_Xgs360026fImportIpAddress_Object((1,3,6,1,4,1,890,1,5,8,77,4,4,4),_Xgs360026fImportIpAddress_Type())
xgs360026fImportIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fImportIpAddress.setStatus(_A)
_Xgs360026fImportConfigName_Type=DisplayString
_Xgs360026fImportConfigName_Object=MibScalar
xgs360026fImportConfigName=_Xgs360026fImportConfigName_Object((1,3,6,1,4,1,890,1,5,8,77,4,4,5),_Xgs360026fImportConfigName_Type())
xgs360026fImportConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fImportConfigName.setStatus(_A)
class _Xgs360026fDoImportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Xgs360026fDoImportConfig_Type.__name__=_B
_Xgs360026fDoImportConfig_Object=MibScalar
xgs360026fDoImportConfig=_Xgs360026fDoImportConfig_Object((1,3,6,1,4,1,890,1,5,8,77,4,4,6),_Xgs360026fDoImportConfig_Type())
xgs360026fDoImportConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fDoImportConfig.setStatus(_A)
_Xgs360026fDiagnostics_ObjectIdentity=ObjectIdentity
xgs360026fDiagnostics=_Xgs360026fDiagnostics_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,4,5))
_Xgs360026fPingIpAddress_Type=IpAddress
_Xgs360026fPingIpAddress_Object=MibScalar
xgs360026fPingIpAddress=_Xgs360026fPingIpAddress_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,1),_Xgs360026fPingIpAddress_Type())
xgs360026fPingIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPingIpAddress.setStatus(_A)
class _Xgs360026fPingSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,1400))
_Xgs360026fPingSize_Type.__name__=_B
_Xgs360026fPingSize_Object=MibScalar
xgs360026fPingSize=_Xgs360026fPingSize_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,2),_Xgs360026fPingSize_Type())
xgs360026fPingSize.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPingSize.setStatus(_A)
class _Xgs360026fDoPingConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Xgs360026fDoPingConfig_Type.__name__=_B
_Xgs360026fDoPingConfig_Object=MibScalar
xgs360026fDoPingConfig=_Xgs360026fDoPingConfig_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,3),_Xgs360026fDoPingConfig_Type())
xgs360026fDoPingConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fDoPingConfig.setStatus(_A)
_Xgs360026fPingResult_Type=DisplayString
_Xgs360026fPingResult_Object=MibScalar
xgs360026fPingResult=_Xgs360026fPingResult_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,4),_Xgs360026fPingResult_Type())
xgs360026fPingResult.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPingResult.setStatus(_A)
_Xgs360026fPing6IpAddress_Type=DisplayString
_Xgs360026fPing6IpAddress_Object=MibScalar
xgs360026fPing6IpAddress=_Xgs360026fPing6IpAddress_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,5),_Xgs360026fPing6IpAddress_Type())
xgs360026fPing6IpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPing6IpAddress.setStatus(_A)
class _Xgs360026fPing6Size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,1400))
_Xgs360026fPing6Size_Type.__name__=_B
_Xgs360026fPing6Size_Object=MibScalar
xgs360026fPing6Size=_Xgs360026fPing6Size_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,6),_Xgs360026fPing6Size_Type())
xgs360026fPing6Size.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fPing6Size.setStatus(_A)
class _Xgs360026fDoPing6Config_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Xgs360026fDoPing6Config_Type.__name__=_B
_Xgs360026fDoPing6Config_Object=MibScalar
xgs360026fDoPing6Config=_Xgs360026fDoPing6Config_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,7),_Xgs360026fDoPing6Config_Type())
xgs360026fDoPing6Config.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fDoPing6Config.setStatus(_A)
_Xgs360026fPing6Result_Type=DisplayString
_Xgs360026fPing6Result_Object=MibScalar
xgs360026fPing6Result=_Xgs360026fPing6Result_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,8),_Xgs360026fPing6Result_Type())
xgs360026fPing6Result.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fPing6Result.setStatus(_A)
_Xgs360026fVeriPHY_ObjectIdentity=ObjectIdentity
xgs360026fVeriPHY=_Xgs360026fVeriPHY_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,4,5,9))
class _Xgs360026fVeriPHYTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fVeriPHYTest_Type.__name__=_B
_Xgs360026fVeriPHYTest_Object=MibScalar
xgs360026fVeriPHYTest=_Xgs360026fVeriPHYTest_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,9,1),_Xgs360026fVeriPHYTest_Type())
xgs360026fVeriPHYTest.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360026fVeriPHYTest.setStatus(_A)
_Xgs360026fVeriPHYTable_Object=MibTable
xgs360026fVeriPHYTable=_Xgs360026fVeriPHYTable_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,9,2))
if mibBuilder.loadTexts:xgs360026fVeriPHYTable.setStatus(_A)
_Xgs360026fVeriPHYEntry_Object=MibTableRow
xgs360026fVeriPHYEntry=_Xgs360026fVeriPHYEntry_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,9,2,1))
xgs360026fVeriPHYEntry.setIndexNames((0,_E,_s))
if mibBuilder.loadTexts:xgs360026fVeriPHYEntry.setStatus(_A)
class _Xgs360026fVeriPHYPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360026fVeriPHYPort_Type.__name__=_B
_Xgs360026fVeriPHYPort_Object=MibTableColumn
xgs360026fVeriPHYPort=_Xgs360026fVeriPHYPort_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,9,2,1,1),_Xgs360026fVeriPHYPort_Type())
xgs360026fVeriPHYPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360026fVeriPHYPort.setStatus(_A)
_Xgs360026fVeriPHYPairA_Type=DisplayString
_Xgs360026fVeriPHYPairA_Object=MibTableColumn
xgs360026fVeriPHYPairA=_Xgs360026fVeriPHYPairA_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,9,2,1,2),_Xgs360026fVeriPHYPairA_Type())
xgs360026fVeriPHYPairA.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fVeriPHYPairA.setStatus(_A)
_Xgs360026fVeriPHYLengthA_Type=DisplayString
_Xgs360026fVeriPHYLengthA_Object=MibTableColumn
xgs360026fVeriPHYLengthA=_Xgs360026fVeriPHYLengthA_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,9,2,1,3),_Xgs360026fVeriPHYLengthA_Type())
xgs360026fVeriPHYLengthA.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fVeriPHYLengthA.setStatus(_A)
_Xgs360026fVeriPHYPairB_Type=DisplayString
_Xgs360026fVeriPHYPairB_Object=MibTableColumn
xgs360026fVeriPHYPairB=_Xgs360026fVeriPHYPairB_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,9,2,1,4),_Xgs360026fVeriPHYPairB_Type())
xgs360026fVeriPHYPairB.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fVeriPHYPairB.setStatus(_A)
_Xgs360026fVeriPHYLengthB_Type=DisplayString
_Xgs360026fVeriPHYLengthB_Object=MibTableColumn
xgs360026fVeriPHYLengthB=_Xgs360026fVeriPHYLengthB_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,9,2,1,5),_Xgs360026fVeriPHYLengthB_Type())
xgs360026fVeriPHYLengthB.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fVeriPHYLengthB.setStatus(_A)
_Xgs360026fVeriPHYPairC_Type=DisplayString
_Xgs360026fVeriPHYPairC_Object=MibTableColumn
xgs360026fVeriPHYPairC=_Xgs360026fVeriPHYPairC_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,9,2,1,6),_Xgs360026fVeriPHYPairC_Type())
xgs360026fVeriPHYPairC.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fVeriPHYPairC.setStatus(_A)
_Xgs360026fVeriPHYLengthC_Type=DisplayString
_Xgs360026fVeriPHYLengthC_Object=MibTableColumn
xgs360026fVeriPHYLengthC=_Xgs360026fVeriPHYLengthC_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,9,2,1,7),_Xgs360026fVeriPHYLengthC_Type())
xgs360026fVeriPHYLengthC.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fVeriPHYLengthC.setStatus(_A)
_Xgs360026fVeriPHYPairD_Type=DisplayString
_Xgs360026fVeriPHYPairD_Object=MibTableColumn
xgs360026fVeriPHYPairD=_Xgs360026fVeriPHYPairD_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,9,2,1,8),_Xgs360026fVeriPHYPairD_Type())
xgs360026fVeriPHYPairD.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fVeriPHYPairD.setStatus(_A)
_Xgs360026fVeriPHYLengthD_Type=DisplayString
_Xgs360026fVeriPHYLengthD_Object=MibTableColumn
xgs360026fVeriPHYLengthD=_Xgs360026fVeriPHYLengthD_Object((1,3,6,1,4,1,890,1,5,8,77,4,5,9,2,1,9),_Xgs360026fVeriPHYLengthD_Type())
xgs360026fVeriPHYLengthD.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fVeriPHYLengthD.setStatus(_A)
_Xgs360026fTrap_ObjectIdentity=ObjectIdentity
xgs360026fTrap=_Xgs360026fTrap_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,5))
_Xgs360026fTrapEvent_ObjectIdentity=ObjectIdentity
xgs360026fTrapEvent=_Xgs360026fTrapEvent_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,5,1))
_Xgs360026fTrapVariable_ObjectIdentity=ObjectIdentity
xgs360026fTrapVariable=_Xgs360026fTrapVariable_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,77,5,2))
_Xgs360026fInformation_Type=DisplayString
_Xgs360026fInformation_Object=MibScalar
xgs360026fInformation=_Xgs360026fInformation_Object((1,3,6,1,4,1,890,1,5,8,77,5,2,1),_Xgs360026fInformation_Type())
xgs360026fInformation.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360026fInformation.setStatus(_A)
xgs360026fEmergency=NotificationType((1,3,6,1,4,1,890,1,5,8,77,5,1,1))
xgs360026fEmergency.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360026fEmergency.setStatus(_A)
xgs360026fAlert=NotificationType((1,3,6,1,4,1,890,1,5,8,77,5,1,2))
xgs360026fAlert.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360026fAlert.setStatus(_A)
xgs360026fCritical=NotificationType((1,3,6,1,4,1,890,1,5,8,77,5,1,3))
xgs360026fCritical.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360026fCritical.setStatus(_A)
xgs360026fError=NotificationType((1,3,6,1,4,1,890,1,5,8,77,5,1,4))
xgs360026fError.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360026fError.setStatus(_A)
xgs360026fWarning=NotificationType((1,3,6,1,4,1,890,1,5,8,77,5,1,5))
xgs360026fWarning.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360026fWarning.setStatus(_A)
xgs360026fNotice=NotificationType((1,3,6,1,4,1,890,1,5,8,77,5,1,6))
xgs360026fNotice.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360026fNotice.setStatus(_A)
xgs360026fInformational=NotificationType((1,3,6,1,4,1,890,1,5,8,77,5,1,7))
xgs360026fInformational.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360026fInformational.setStatus(_A)
xgs360026fDebug=NotificationType((1,3,6,1,4,1,890,1,5,8,77,5,1,8))
xgs360026fDebug.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360026fDebug.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zyxel':zyxel,'products':products,'accessSwitch':accessSwitch,'esSeries':esSeries,'xgs360026fProductId':xgs360026fProductId,'xgs360026fSystem':xgs360026fSystem,'xgs360026fSystemInformation':xgs360026fSystemInformation,'xgs360026fModelName':xgs360026fModelName,'xgs360026fBIOSVersion':xgs360026fBIOSVersion,'xgs360026fFirmwareVersion':xgs360026fFirmwareVersion,'xgs360026fHardwareMechanicalVersion':xgs360026fHardwareMechanicalVersion,'xgs360026fSeriesNumber':xgs360026fSeriesNumber,'xgs360026fHostMACAddress':xgs360026fHostMACAddress,'xgs360026fConsoleBaudrate':xgs360026fConsoleBaudrate,'xgs360026fRAMSize':xgs360026fRAMSize,'xgs360026fFlashSize':xgs360026fFlashSize,'xgs360026fBridgeFBDSize':xgs360026fBridgeFBDSize,'xgs360026fTransmitQueue':xgs360026fTransmitQueue,'xgs360026fMaximumFrameSize':xgs360026fMaximumFrameSize,'xgs360026fCPULoad':xgs360026fCPULoad,'xgs360026fFanSpeed':xgs360026fFanSpeed,'xgs360026fPowers':xgs360026fPowers,'xgs360026fTemperature1':xgs360026fTemperature1,'xgs360026fTemperature2':xgs360026fTemperature2,'xgs360026fTemperature3':xgs360026fTemperature3,'xgs360026fTemperature4':xgs360026fTemperature4,'xgs360026fSystemTime':xgs360026fSystemTime,'xgs360026fSystemTimeManual':xgs360026fSystemTimeManual,'xgs360026fSystemTimeManualClockSource':xgs360026fSystemTimeManualClockSource,'xgs360026fSystemTimeManualLocaltime':xgs360026fSystemTimeManualLocaltime,'xgs360026fSystemTimeManualTimeZoneOffset':xgs360026fSystemTimeManualTimeZoneOffset,'xgs360026fSystemTimeManualDaylightSavings':xgs360026fSystemTimeManualDaylightSavings,'xgs360026fSystemTimeManualTimeSetOffset':xgs360026fSystemTimeManualTimeSetOffset,'xgs360026fSystemTimeManualDaylightSavingsType':xgs360026fSystemTimeManualDaylightSavingsType,'xgs360026fSystemTimeManualDaylightSavingsBydatesFrom':xgs360026fSystemTimeManualDaylightSavingsBydatesFrom,'xgs360026fSystemTimeManualDaylightSavingsBydatesTo':xgs360026fSystemTimeManualDaylightSavingsBydatesTo,'xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom':xgs360026fSystemTimeManualDaylightSavingsRecurringDayFrom,'xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom':xgs360026fSystemTimeManualDaylightSavingsRecurringWeekFrom,'xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom':xgs360026fSystemTimeManualDaylightSavingsRecurringMonthFrom,'xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom':xgs360026fSystemTimeManualDaylightSavingsRecurringTimeFrom,'xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo':xgs360026fSystemTimeManualDaylightSavingsRecurringDayTo,'xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo':xgs360026fSystemTimeManualDaylightSavingsRecurringWeekTo,'xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo':xgs360026fSystemTimeManualDaylightSavingsRecurringMonthTo,'xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo':xgs360026fSystemTimeManualDaylightSavingsRecurringTimeTo,'xgs360026fSystemTimeNTP':xgs360026fSystemTimeNTP,'xgs360026fSystemTimeNTPTable':xgs360026fSystemTimeNTPTable,'xgs360026fSystemTimeNTPEntry':xgs360026fSystemTimeNTPEntry,_J:xgs360026fSystemTimeNTPIndex,'xgs360026fSystemTimeNTPServerIPType':xgs360026fSystemTimeNTPServerIPType,'xgs360026fSystemTimeNTPServer':xgs360026fSystemTimeNTPServer,'xgs360026fSystemTimeNTPCurrentMode':xgs360026fSystemTimeNTPCurrentMode,'xgs360026fSystemAccount':xgs360026fSystemAccount,'xgs360026fSystemAccountUsers':xgs360026fSystemAccountUsers,'xgs360026fSystemAccountUserCreate':xgs360026fSystemAccountUserCreate,'xgs360026fSystemAccountUsersTable':xgs360026fSystemAccountUsersTable,'xgs360026fSystemAccountUsersEntry':xgs360026fSystemAccountUsersEntry,_K:xgs360026fUserIndex,'xgs360026fUserName':xgs360026fUserName,'xgs360026fPassword':xgs360026fPassword,'xgs360026fUserPrivilegeLevel':xgs360026fUserPrivilegeLevel,'xgs360026fAccountUserRowStatus':xgs360026fAccountUserRowStatus,'xgs360026fSystemAccountPrivilegeLevel':xgs360026fSystemAccountPrivilegeLevel,'xgs360026fAccountPrivilegeLevel':xgs360026fAccountPrivilegeLevel,'xgs360026fAggregationPrivilegeLevel':xgs360026fAggregationPrivilegeLevel,'xgs360026fDiagnosticsPrivilegeLevel':xgs360026fDiagnosticsPrivilegeLevel,'xgs360026fEPSPrivilegeLevel':xgs360026fEPSPrivilegeLevel,'xgs360026fERPSPrivilegeLevel':xgs360026fERPSPrivilegeLevel,'xgs360026fETHLinkOAMPrivilegeLevel':xgs360026fETHLinkOAMPrivilegeLevel,'xgs360026fEVCPrivilegeLevel':xgs360026fEVCPrivilegeLevel,'xgs360026fGARPPrivilegeLevel':xgs360026fGARPPrivilegeLevel,'xgs360026fGVRPPrivilegeLevel':xgs360026fGVRPPrivilegeLevel,'xgs360026fIPPrivilegeLevel':xgs360026fIPPrivilegeLevel,'xgs360026fIPMCSnoopingPrivilegeLevel':xgs360026fIPMCSnoopingPrivilegeLevel,'xgs360026fLACPPrivilegeLevel':xgs360026fLACPPrivilegeLevel,'xgs360026fLLDPPrivilegeLevel':xgs360026fLLDPPrivilegeLevel,'xgs360026fLLDPMEDPrivilegeLevel':xgs360026fLLDPMEDPrivilegeLevel,'xgs360026fLoopProtectPrivilegeLevel':xgs360026fLoopProtectPrivilegeLevel,'xgs360026fMACTablePrivilegeLevel':xgs360026fMACTablePrivilegeLevel,'xgs360026fMEPPrivilegeLevel':xgs360026fMEPPrivilegeLevel,'xgs360026fMRSTPPrivilegeLevel':xgs360026fMRSTPPrivilegeLevel,'xgs360026fMVRPrivilegeLevel':xgs360026fMVRPrivilegeLevel,'xgs360026fMaintenancePrivilegeLevel':xgs360026fMaintenancePrivilegeLevel,'xgs360026fMirroringPrivilegeLevel':xgs360026fMirroringPrivilegeLevel,'xgs360026fPTPPrivilegeLevel':xgs360026fPTPPrivilegeLevel,'xgs360026fPortsPrivilegeLevel':xgs360026fPortsPrivilegeLevel,'xgs360026fPrivateVLANsPrivilegeLevel':xgs360026fPrivateVLANsPrivilegeLevel,'xgs360026fQoSPrivilegeLevel':xgs360026fQoSPrivilegeLevel,'xgs360026fSMTPPrivilegeLevel':xgs360026fSMTPPrivilegeLevel,'xgs360026fSNMPPrivilegeLevel':xgs360026fSNMPPrivilegeLevel,'xgs360026fSecurityPrivilegeLevel':xgs360026fSecurityPrivilegeLevel,'xgs360026fSpanningTreePrivilegeLevel':xgs360026fSpanningTreePrivilegeLevel,'xgs360026fSystemPrivilegeLevel':xgs360026fSystemPrivilegeLevel,'xgs360026fTrapEventPrivilegeLevel':xgs360026fTrapEventPrivilegeLevel,'xgs360026fVCLPrivilegeLevel':xgs360026fVCLPrivilegeLevel,'xgs360026fVLANTranslationPrivilegeLevel':xgs360026fVLANTranslationPrivilegeLevel,'xgs360026fVLANsPrivilegeLevel':xgs360026fVLANsPrivilegeLevel,'xgs360026fIP':xgs360026fIP,'xgs360026fIPv4':xgs360026fIPv4,'xgs360026fIPv4Configured':xgs360026fIPv4Configured,'xgs360026fIpv4DHCPClient':xgs360026fIpv4DHCPClient,'xgs360026fIPv4Address':xgs360026fIPv4Address,'xgs360026fIPv4Mask':xgs360026fIPv4Mask,'xgs360026fIPv4Router':xgs360026fIPv4Router,'xgs360026fIPv4VLANId':xgs360026fIPv4VLANId,'xgs360026fIPv4DNSServer':xgs360026fIPv4DNSServer,'xgs360026fIPv4DNSProxy':xgs360026fIPv4DNSProxy,'xgs360026fIPv4Current':xgs360026fIPv4Current,'xgs360026fIpv4CurrentDHCPClient':xgs360026fIpv4CurrentDHCPClient,'xgs360026fIPv4CurrentAddress':xgs360026fIPv4CurrentAddress,'xgs360026fIPv4CurrentMask':xgs360026fIPv4CurrentMask,'xgs360026fIPv4CurrentRouter':xgs360026fIPv4CurrentRouter,'xgs360026fIPv4CurrentVLANId':xgs360026fIPv4CurrentVLANId,'xgs360026fIPv4CurrentDNSServer':xgs360026fIPv4CurrentDNSServer,'xgs360026fIPv6':xgs360026fIPv6,'xgs360026fIPv6Configured':xgs360026fIPv6Configured,'xgs360026fIpv6AutoConfiguration':xgs360026fIpv6AutoConfiguration,'xgs360026fIpv6Address':xgs360026fIpv6Address,'xgs360026fIpv6Prefix':xgs360026fIpv6Prefix,'xgs360026fIpv6Router':xgs360026fIpv6Router,'xgs360026fIPv6Current':xgs360026fIPv6Current,'xgs360026fIpv6CurrentAutoConfiguration':xgs360026fIpv6CurrentAutoConfiguration,'xgs360026fIpv6CurrentAddress':xgs360026fIpv6CurrentAddress,'xgs360026fIpv6CurrentLinkLocalAddress':xgs360026fIpv6CurrentLinkLocalAddress,'xgs360026fIpv6CurrentPrefix':xgs360026fIpv6CurrentPrefix,'xgs360026fIpv6CurrentRouter':xgs360026fIpv6CurrentRouter,'xgs360026fSyslog':xgs360026fSyslog,'xgs360026fSyslogConf':xgs360026fSyslogConf,'xgs360026fServerMode':xgs360026fServerMode,'xgs360026fServerAddress1':xgs360026fServerAddress1,'xgs360026fServerAddress2':xgs360026fServerAddress2,'xgs360026fSyslogLevel':xgs360026fSyslogLevel,'xgs360026fSyslogDetailedInfo':xgs360026fSyslogDetailedInfo,'xgs360026fSyslogDetailedInfoClear':xgs360026fSyslogDetailedInfoClear,'xgs360026fSyslogDetailedInfoTable':xgs360026fSyslogDetailedInfoTable,'xgs360026fSyslogDetailedInfoEntry':xgs360026fSyslogDetailedInfoEntry,_L:xgs360026fSyslogDetailedInfoIndex,'xgs360026fSyslogDetailedInfoLevel':xgs360026fSyslogDetailedInfoLevel,'xgs360026fSyslogDetailedInfoTime':xgs360026fSyslogDetailedInfoTime,'xgs360026fSyslogDetailedInfoMessage':xgs360026fSyslogDetailedInfoMessage,'xgs360026fSnmp':xgs360026fSnmp,'xgs360026fSnmpConf':xgs360026fSnmpConf,'xgs360026fGetCommunity':xgs360026fGetCommunity,'xgs360026fSetCommunityMode':xgs360026fSetCommunityMode,'xgs360026fSetCommunity':xgs360026fSetCommunity,'xgs360026fTrapHostConfTable':xgs360026fTrapHostConfTable,'xgs360026fTrapHostConfEntry':xgs360026fTrapHostConfEntry,_M:xgs360026fTrapHostConfIndex,'xgs360026fTrapHostConfVersion':xgs360026fTrapHostConfVersion,'xgs360026fTrapHostConfIPType':xgs360026fTrapHostConfIPType,'xgs360026fTrapHostConfIP':xgs360026fTrapHostConfIP,'xgs360026fTrapHostConfPort':xgs360026fTrapHostConfPort,'xgs360026fTrapHostConfCommunity':xgs360026fTrapHostConfCommunity,'xgs360026fTrapHostConfSeverityLevel':xgs360026fTrapHostConfSeverityLevel,'xgs360026fTrapHostConfSecurityLevel':xgs360026fTrapHostConfSecurityLevel,'xgs360026fTrapHostConfAuthPtc':xgs360026fTrapHostConfAuthPtc,'xgs360026fTrapHostConfAuthPassword':xgs360026fTrapHostConfAuthPassword,'xgs360026fTrapHostConfPrivPtc':xgs360026fTrapHostConfPrivPtc,'xgs360026fTrapHostConfPrivPassword':xgs360026fTrapHostConfPrivPassword,'xgs360026fTrapHostConfCurrentMode':xgs360026fTrapHostConfCurrentMode,'xgs360026fConfiguration':xgs360026fConfiguration,'xgs360026fPort':xgs360026fPort,'xgs360026fPortConfigurationTable':xgs360026fPortConfigurationTable,'xgs360026fPortConfigurationEntry':xgs360026fPortConfigurationEntry,_N:xgs360026fPortConfPort,'xgs360026fPortConfPortMedia':xgs360026fPortConfPortMedia,'xgs360026fPortConfLink':xgs360026fPortConfLink,'xgs360026fPortConfCurrentSpeed':xgs360026fPortConfCurrentSpeed,'xgs360026fPortConfSpeed':xgs360026fPortConfSpeed,'xgs360026fPortConfCurrentFlowControlRx':xgs360026fPortConfCurrentFlowControlRx,'xgs360026fPortConfCurrentFlowControlTx':xgs360026fPortConfCurrentFlowControlTx,'xgs360026fPortConfFlowControl':xgs360026fPortConfFlowControl,'xgs360026fPortConfMaxFrameSize':xgs360026fPortConfMaxFrameSize,'xgs360026fPortConfExcessiveCollisionMode':xgs360026fPortConfExcessiveCollisionMode,'xgs360026fPortConfPowerControl':xgs360026fPortConfPowerControl,'xgs360026fPortConfDescription':xgs360026fPortConfDescription,'xgs360026fPortTrafficStatisticsTable':xgs360026fPortTrafficStatisticsTable,'xgs360026fPortTrafficStatisticsEntry':xgs360026fPortTrafficStatisticsEntry,_O:xgs360026fPortTrafficStatisticsPort,'xgs360026fPortTrafficStatisticsClear':xgs360026fPortTrafficStatisticsClear,'xgs360026fPortTrafficRxPackets':xgs360026fPortTrafficRxPackets,'xgs360026fPortTrafficRxOctets':xgs360026fPortTrafficRxOctets,'xgs360026fPortTrafficRxUnicast':xgs360026fPortTrafficRxUnicast,'xgs360026fPortTrafficRxMulticast':xgs360026fPortTrafficRxMulticast,'xgs360026fPortTrafficRxBroadcast':xgs360026fPortTrafficRxBroadcast,'xgs360026fPortTrafficRxPause':xgs360026fPortTrafficRxPause,'xgs360026fPortTrafficRx64Bytes':xgs360026fPortTrafficRx64Bytes,'xgs360026fPortTrafficRx65to127Bytes':xgs360026fPortTrafficRx65to127Bytes,'xgs360026fPortTrafficRx128to255Bytes':xgs360026fPortTrafficRx128to255Bytes,'xgs360026fPortTrafficRx256to511Bytes':xgs360026fPortTrafficRx256to511Bytes,'xgs360026fPortTrafficRx512to1023Bytes':xgs360026fPortTrafficRx512to1023Bytes,'xgs360026fPortTrafficRx1024to1526Bytes':xgs360026fPortTrafficRx1024to1526Bytes,'xgs360026fPortTrafficRxExceecd1527Bytes':xgs360026fPortTrafficRxExceecd1527Bytes,'xgs360026fPortTrafficRxQ0':xgs360026fPortTrafficRxQ0,'xgs360026fPortTrafficRxQ1':xgs360026fPortTrafficRxQ1,'xgs360026fPortTrafficRxQ2':xgs360026fPortTrafficRxQ2,'xgs360026fPortTrafficRxQ3':xgs360026fPortTrafficRxQ3,'xgs360026fPortTrafficRxQ4':xgs360026fPortTrafficRxQ4,'xgs360026fPortTrafficRxQ5':xgs360026fPortTrafficRxQ5,'xgs360026fPortTrafficRxQ6':xgs360026fPortTrafficRxQ6,'xgs360026fPortTrafficRxQ7':xgs360026fPortTrafficRxQ7,'xgs360026fPortTrafficRxDrops':xgs360026fPortTrafficRxDrops,'xgs360026fPortTrafficRxCRCorAlignment':xgs360026fPortTrafficRxCRCorAlignment,'xgs360026fPortTrafficRxUndersize':xgs360026fPortTrafficRxUndersize,'xgs360026fPortTrafficRxOversize':xgs360026fPortTrafficRxOversize,'xgs360026fPortTrafficRxFragments':xgs360026fPortTrafficRxFragments,'xgs360026fPortTrafficRxJabber':xgs360026fPortTrafficRxJabber,'xgs360026fPortTrafficRxFiltered':xgs360026fPortTrafficRxFiltered,'xgs360026fPortTrafficTxPackets':xgs360026fPortTrafficTxPackets,'xgs360026fPortTrafficTxOctets':xgs360026fPortTrafficTxOctets,'xgs360026fPortTrafficTxUnicast':xgs360026fPortTrafficTxUnicast,'xgs360026fPortTrafficTxMulticast':xgs360026fPortTrafficTxMulticast,'xgs360026fPortTrafficTxBroadcast':xgs360026fPortTrafficTxBroadcast,'xgs360026fPortTrafficTxPause':xgs360026fPortTrafficTxPause,'xgs360026fPortTrafficTx64Bytes':xgs360026fPortTrafficTx64Bytes,'xgs360026fPortTrafficTx65to127Bytes':xgs360026fPortTrafficTx65to127Bytes,'xgs360026fPortTrafficTx128to255Bytes':xgs360026fPortTrafficTx128to255Bytes,'xgs360026fPortTrafficTx256to511Bytes':xgs360026fPortTrafficTx256to511Bytes,'xgs360026fPortTrafficTx512to1023Bytes':xgs360026fPortTrafficTx512to1023Bytes,'xgs360026fPortTrafficTx1024to1526Bytes':xgs360026fPortTrafficTx1024to1526Bytes,'xgs360026fPortTrafficTxExceecd1527Bytes':xgs360026fPortTrafficTxExceecd1527Bytes,'xgs360026fPortTrafficTxQ0':xgs360026fPortTrafficTxQ0,'xgs360026fPortTrafficTxQ1':xgs360026fPortTrafficTxQ1,'xgs360026fPortTrafficTxQ2':xgs360026fPortTrafficTxQ2,'xgs360026fPortTrafficTxQ3':xgs360026fPortTrafficTxQ3,'xgs360026fPortTrafficTxQ4':xgs360026fPortTrafficTxQ4,'xgs360026fPortTrafficTxQ5':xgs360026fPortTrafficTxQ5,'xgs360026fPortTrafficTxQ6':xgs360026fPortTrafficTxQ6,'xgs360026fPortTrafficTxQ7':xgs360026fPortTrafficTxQ7,'xgs360026fPortTrafficTxDrops':xgs360026fPortTrafficTxDrops,'xgs360026fPortTrafficTxLateOrExcColl':xgs360026fPortTrafficTxLateOrExcColl,'xgs360026fPortQoSStatistics':xgs360026fPortQoSStatistics,'xgs360026fPortQoSStatisticsClear':xgs360026fPortQoSStatisticsClear,'xgs360026fPortQoSStatisticsTable':xgs360026fPortQoSStatisticsTable,'xgs360026fPortQoSStatisticsEntry':xgs360026fPortQoSStatisticsEntry,_P:xgs360026fPortQoSStatisticsPort,'xgs360026fPortQoSQ0Rx':xgs360026fPortQoSQ0Rx,'xgs360026fPortQoSQ0Tx':xgs360026fPortQoSQ0Tx,'xgs360026fPortQoSQ1Rx':xgs360026fPortQoSQ1Rx,'xgs360026fPortQoSQ1Tx':xgs360026fPortQoSQ1Tx,'xgs360026fPortQoSQ2Rx':xgs360026fPortQoSQ2Rx,'xgs360026fPortQoSQ2Tx':xgs360026fPortQoSQ2Tx,'xgs360026fPortQoSQ3Rx':xgs360026fPortQoSQ3Rx,'xgs360026fPortQoSQ3Tx':xgs360026fPortQoSQ3Tx,'xgs360026fPortQoSQ4Rx':xgs360026fPortQoSQ4Rx,'xgs360026fPortQoSQ4Tx':xgs360026fPortQoSQ4Tx,'xgs360026fPortQoSQ5Rx':xgs360026fPortQoSQ5Rx,'xgs360026fPortQoSQ5Tx':xgs360026fPortQoSQ5Tx,'xgs360026fPortQoSQ6Rx':xgs360026fPortQoSQ6Rx,'xgs360026fPortQoSQ6Tx':xgs360026fPortQoSQ6Tx,'xgs360026fPortQoSQ7Rx':xgs360026fPortQoSQ7Rx,'xgs360026fPortQoSQ7Tx':xgs360026fPortQoSQ7Tx,'xgs360026fSFPInfoTable':xgs360026fSFPInfoTable,'xgs360026fSFPInfoEntry':xgs360026fSFPInfoEntry,_Q:xgs360026fSFPInfoIndex,'xgs360026fSFPInfoPort':xgs360026fSFPInfoPort,'xgs360026fSFPConnectorType':xgs360026fSFPConnectorType,'xgs360026fSFPFiberType':xgs360026fSFPFiberType,'xgs360026fSFPTxCentralWavelength':xgs360026fSFPTxCentralWavelength,'xgs360026fSFPBaudRate':xgs360026fSFPBaudRate,'xgs360026fSFPVendorOUI':xgs360026fSFPVendorOUI,'xgs360026fSFPVendorName':xgs360026fSFPVendorName,'xgs360026fSFPVendorPN':xgs360026fSFPVendorPN,'xgs360026fSFPVendorRev':xgs360026fSFPVendorRev,'xgs360026fSFPVendorSN':xgs360026fSFPVendorSN,'xgs360026fSFPDateCode':xgs360026fSFPDateCode,'xgs360026fSFPTemperature':xgs360026fSFPTemperature,'xgs360026fSFPVcc':xgs360026fSFPVcc,'xgs360026fSFPMon1Bias':xgs360026fSFPMon1Bias,'xgs360026fSFPMon2TxPWR':xgs360026fSFPMon2TxPWR,'xgs360026fSFPMon3RxPWR':xgs360026fSFPMon3RxPWR,'xgs360026fGARP':xgs360026fGARP,'xgs360026fGARPConfTable':xgs360026fGARPConfTable,'xgs360026fGARPConfEntry':xgs360026fGARPConfEntry,_R:xgs360026fGARPConfPort,'xgs360026fGARPJoinTimer':xgs360026fGARPJoinTimer,'xgs360026fGARPLeaveTimer':xgs360026fGARPLeaveTimer,'xgs360026fGARPLeaveAllTimer':xgs360026fGARPLeaveAllTimer,'xgs360026fGARPApplicantion':xgs360026fGARPApplicantion,'xgs360026fGARPAttributeType':xgs360026fGARPAttributeType,'xgs360026fGARPApplicant':xgs360026fGARPApplicant,'xgs360026fGARPStatisticsTable':xgs360026fGARPStatisticsTable,'xgs360026fGARPStatisticsEntry':xgs360026fGARPStatisticsEntry,_S:xgs360026fGARPStatisticsPort,'xgs360026fGARPStatisticsPeerMAC':xgs360026fGARPStatisticsPeerMAC,'xgs360026fGARPStatisticsFailedCount':xgs360026fGARPStatisticsFailedCount,'xgs360026fGVRP':xgs360026fGVRP,'xgs360026fGVRPConf':xgs360026fGVRPConf,'xgs360026fGVRPMode':xgs360026fGVRPMode,'xgs360026fGVRPConfTable':xgs360026fGVRPConfTable,'xgs360026fGVRPConfEntry':xgs360026fGVRPConfEntry,_T:xgs360026fGVRPConfPort,'xgs360026fGVRPConfPortMode':xgs360026fGVRPConfPortMode,'xgs360026fGVRPConfPortRRole':xgs360026fGVRPConfPortRRole,'xgs360026fGVRPStatisticsTable':xgs360026fGVRPStatisticsTable,'xgs360026fGVRPStatisticsEntry':xgs360026fGVRPStatisticsEntry,_U:xgs360026fGVRPStatisticsPort,'xgs360026fGVRPStatisticsJoinTxCnt':xgs360026fGVRPStatisticsJoinTxCnt,'xgs360026fGVRPStatisticsLeaveTxCnt':xgs360026fGVRPStatisticsLeaveTxCnt,'xgs360026fThermalProtection':xgs360026fThermalProtection,'xgs360026fPriority0Temperature':xgs360026fPriority0Temperature,'xgs360026fPriority1Temperature':xgs360026fPriority1Temperature,'xgs360026fPriority2Temperature':xgs360026fPriority2Temperature,'xgs360026fPriority3Temperature':xgs360026fPriority3Temperature,'xgs360026fThermalProtectionTable':xgs360026fThermalProtectionTable,'xgs360026fThermalProtectionEntry':xgs360026fThermalProtectionEntry,_V:xgs360026fThermalProtectionPort,'xgs360026fThermalProtectionPortTemperature':xgs360026fThermalProtectionPortTemperature,'xgs360026fThermalProtectionPortPriority':xgs360026fThermalProtectionPortPriority,'xgs360026fThermalProtectionPortStatus':xgs360026fThermalProtectionPortStatus,'xgs360026fMirroring':xgs360026fMirroring,'xgs360026fPortToMirrorOn':xgs360026fPortToMirrorOn,'xgs360026fMirrorTable':xgs360026fMirrorTable,'xgs360026fMirrorEntry':xgs360026fMirrorEntry,_W:xgs360026fMirrorPort,'xgs360026fMirrorMode':xgs360026fMirrorMode,'xgs360026fTrapEventSeverity':xgs360026fTrapEventSeverity,'xgs360026fTrapEventSeverityACL':xgs360026fTrapEventSeverityACL,'xgs360026fTrapEventSeverityACLLog':xgs360026fTrapEventSeverityACLLog,'xgs360026fTrapEventSeverityAccessMgmt':xgs360026fTrapEventSeverityAccessMgmt,'xgs360026fTrapEventSeverityAuthFailed':xgs360026fTrapEventSeverityAuthFailed,'xgs360026fTrapEventSeverityColdStart':xgs360026fTrapEventSeverityColdStart,'xgs360026fTrapEventSeverityConfigInfo':xgs360026fTrapEventSeverityConfigInfo,'xgs360026fTrapEventSeverityFirmwareUpgrade':xgs360026fTrapEventSeverityFirmwareUpgrade,'xgs360026fTrapEventSeverityImportExport':xgs360026fTrapEventSeverityImportExport,'xgs360026fTrapEventSeverityLACP':xgs360026fTrapEventSeverityLACP,'xgs360026fTrapEventSeverityLinkStatus':xgs360026fTrapEventSeverityLinkStatus,'xgs360026fTrapEventSeverityLogin':xgs360026fTrapEventSeverityLogin,'xgs360026fTrapEventSeverityLogout':xgs360026fTrapEventSeverityLogout,'xgs360026fTrapEventSeverityLoopProtect':xgs360026fTrapEventSeverityLoopProtect,'xgs360026fTrapEventSeverityMgmtIPChange':xgs360026fTrapEventSeverityMgmtIPChange,'xgs360026fTrapEventSeverityModuleChange':xgs360026fTrapEventSeverityModuleChange,'xgs360026fTrapEventSeverityNAS':xgs360026fTrapEventSeverityNAS,'xgs360026fTrapEventSeverityPasswdChange':xgs360026fTrapEventSeverityPasswdChange,'xgs360026fTrapEventSeverityPortSecurity':xgs360026fTrapEventSeverityPortSecurity,'xgs360026fTrapEventSeverityThermalProtect':xgs360026fTrapEventSeverityThermalProtect,'xgs360026fTrapEventSeverityVLAN':xgs360026fTrapEventSeverityVLAN,'xgs360026fTrapEventSeverityWarmStart':xgs360026fTrapEventSeverityWarmStart,'xgs360026fSMTP':xgs360026fSMTP,'xgs360026fSMTPMailServer':xgs360026fSMTPMailServer,'xgs360026fSMTPUserName':xgs360026fSMTPUserName,'xgs360026fSMTPPassword':xgs360026fSMTPPassword,'xgs360026fSMTPServeriryLevel':xgs360026fSMTPServeriryLevel,'xgs360026fSMTPSender':xgs360026fSMTPSender,'xgs360026fSMTPReturnPath':xgs360026fSMTPReturnPath,'xgs360026fSMTPEmailAddress1':xgs360026fSMTPEmailAddress1,'xgs360026fSMTPEmailAddress2':xgs360026fSMTPEmailAddress2,'xgs360026fSMTPEmailAddress3':xgs360026fSMTPEmailAddress3,'xgs360026fSMTPEmailAddress4':xgs360026fSMTPEmailAddress4,'xgs360026fSMTPEmailAddress5':xgs360026fSMTPEmailAddress5,'xgs360026fSMTPEmailAddress6':xgs360026fSMTPEmailAddress6,'xgs360026fACL':xgs360026fACL,'xgs360026fACLPortsConfTable':xgs360026fACLPortsConfTable,'xgs360026fACLPortsConfEntry':xgs360026fACLPortsConfEntry,_X:xgs360026fACLPortsConfPort,'xgs360026fACLPortsConfPolicyID':xgs360026fACLPortsConfPolicyID,'xgs360026fACLPortsConfAction':xgs360026fACLPortsConfAction,'xgs360026fACLPortsConfRateLimiterID':xgs360026fACLPortsConfRateLimiterID,'xgs360026fACLPortsConfPortRedirect':xgs360026fACLPortsConfPortRedirect,'xgs360026fACLPortsConfLogging':xgs360026fACLPortsConfLogging,'xgs360026fACLPortsConfShutdown':xgs360026fACLPortsConfShutdown,'xgs360026fACLPortsConfState':xgs360026fACLPortsConfState,'xgs360026fACLPortsConfCounter':xgs360026fACLPortsConfCounter,'xgs360026fACLRateLimiterTable':xgs360026fACLRateLimiterTable,'xgs360026fACLRateLimiterEntry':xgs360026fACLRateLimiterEntry,_Y:xgs360026fACLRateLimiterID,'xgs360026fACLRateLimiterRate':xgs360026fACLRateLimiterRate,'xgs360026fACLACE':xgs360026fACLACE,'xgs360026fACLACECreate':xgs360026fACLACECreate,'xgs360026fACLACETable':xgs360026fACLACETable,'xgs360026fACLACEEntry':xgs360026fACLACEEntry,_Z:xgs360026fACLACEIndex,'xgs360026fACLACEID':xgs360026fACLACEID,'xgs360026fACLACENextID':xgs360026fACLACENextID,'xgs360026fACLACEIngressPort':xgs360026fACLACEIngressPort,'xgs360026fACLACEPortPolicyNumber':xgs360026fACLACEPortPolicyNumber,'xgs360026fACLACEPortPolicyBitmask':xgs360026fACLACEPortPolicyBitmask,'xgs360026fACLACEFrameType':xgs360026fACLACEFrameType,'xgs360026fACLACEAction':xgs360026fACLACEAction,'xgs360026fACLACEDenyPortRedirect':xgs360026fACLACEDenyPortRedirect,'xgs360026fACLACELogging':xgs360026fACLACELogging,'xgs360026fACLACERateLimiter':xgs360026fACLACERateLimiter,'xgs360026fACLACEShutdown':xgs360026fACLACEShutdown,'xgs360026fACLACEVLANTagPriority':xgs360026fACLACEVLANTagPriority,'xgs360026fACLACEVLANVID':xgs360026fACLACEVLANVID,'xgs360026fACLACEEtherType':xgs360026fACLACEEtherType,'xgs360026fACLACESMAC':xgs360026fACLACESMAC,'xgs360026fACLACEDMACType':xgs360026fACLACEDMACType,'xgs360026fACLACEDMAC':xgs360026fACLACEDMAC,'xgs360026fACLACEArpOpcode':xgs360026fACLACEArpOpcode,'xgs360026fACLACEArpFlagsRequestReply':xgs360026fACLACEArpFlagsRequestReply,'xgs360026fACLACEArpFlagsArpSmac':xgs360026fACLACEArpFlagsArpSmac,'xgs360026fACLACEArpFlagsRarpDmac':xgs360026fACLACEArpFlagsRarpDmac,'xgs360026fACLACEArpFlagsLength':xgs360026fACLACEArpFlagsLength,'xgs360026fACLACEArpFlagsIp':xgs360026fACLACEArpFlagsIp,'xgs360026fACLACEArpFlagsEthernet':xgs360026fACLACEArpFlagsEthernet,'xgs360026fACLACESIPType':xgs360026fACLACESIPType,'xgs360026fACLACESIPIPAddress':xgs360026fACLACESIPIPAddress,'xgs360026fACLACESIPNetworkPrefix':xgs360026fACLACESIPNetworkPrefix,'xgs360026fACLACEDIPType':xgs360026fACLACEDIPType,'xgs360026fACLACEDIPIPAddress':xgs360026fACLACEDIPIPAddress,'xgs360026fACLACEDIPNetworkPrefix':xgs360026fACLACEDIPNetworkPrefix,'xgs360026fACLACEIPProtocol':xgs360026fACLACEIPProtocol,'xgs360026fACLACEIPFlagsTTL':xgs360026fACLACEIPFlagsTTL,'xgs360026fACLACEIPFlagsOptions':xgs360026fACLACEIPFlagsOptions,'xgs360026fACLACEIPFlagsFragment':xgs360026fACLACEIPFlagsFragment,'xgs360026fACLACEICMPType':xgs360026fACLACEICMPType,'xgs360026fACLACEICMPCode':xgs360026fACLACEICMPCode,'xgs360026fACLACESourcePortMin':xgs360026fACLACESourcePortMin,'xgs360026fACLACESourcePortMax':xgs360026fACLACESourcePortMax,'xgs360026fACLACEDestPortMin':xgs360026fACLACEDestPortMin,'xgs360026fACLACEDestPortMax':xgs360026fACLACEDestPortMax,'xgs360026fACLACETCPFlagsFin':xgs360026fACLACETCPFlagsFin,'xgs360026fACLACETCPFlagsSyn':xgs360026fACLACETCPFlagsSyn,'xgs360026fACLACETCPFlagsRst':xgs360026fACLACETCPFlagsRst,'xgs360026fACLACETCPFlagsPsh':xgs360026fACLACETCPFlagsPsh,'xgs360026fACLACETCPFlagsAck':xgs360026fACLACETCPFlagsAck,'xgs360026fACLACETCPFlagsUrg':xgs360026fACLACETCPFlagsUrg,'xgs360026fACLACERowStatus':xgs360026fACLACERowStatus,'xgs360026fACLACEClear':xgs360026fACLACEClear,'xgs360026fACLACEMoveACEID':xgs360026fACLACEMoveACEID,'xgs360026fACLACEMoveNextACEID':xgs360026fACLACEMoveNextACEID,'xgs360026fACLACEStatusTable':xgs360026fACLACEStatusTable,'xgs360026fACLACEStatusEntry':xgs360026fACLACEStatusEntry,_a:xgs360026fACLACEStatusIndex,'xgs360026fACLACEStatusUser':xgs360026fACLACEStatusUser,'xgs360026fACLACEStatusID':xgs360026fACLACEStatusID,'xgs360026fACLACEStatusIngressPort':xgs360026fACLACEStatusIngressPort,'xgs360026fACLACEStatusFrameType':xgs360026fACLACEStatusFrameType,'xgs360026fACLACEStatusAction':xgs360026fACLACEStatusAction,'xgs360026fACLACEStatusRateLimiter':xgs360026fACLACEStatusRateLimiter,'xgs360026fACLACEStatusPortCopy':xgs360026fACLACEStatusPortCopy,'xgs360026fACLACEStatusMirror':xgs360026fACLACEStatusMirror,'xgs360026fACLACEStatusCPU':xgs360026fACLACEStatusCPU,'xgs360026fACLACEStatusCounter':xgs360026fACLACEStatusCounter,'xgs360026fACLACEStatusConflict':xgs360026fACLACEStatusConflict,'xgs360026fERPS':xgs360026fERPS,'xgs360026fERPSConf':xgs360026fERPSConf,'xgs360026fERPSConfCreate':xgs360026fERPSConfCreate,'xgs360026fERPSConfTable':xgs360026fERPSConfTable,'xgs360026fERPSConfEntry':xgs360026fERPSConfEntry,_b:xgs360026fERPSConfIndex,'xgs360026fERPSConfERPSID':xgs360026fERPSConfERPSID,'xgs360026fERPSConfPort0':xgs360026fERPSConfPort0,'xgs360026fERPSConfPort1':xgs360026fERPSConfPort1,'xgs360026fERPSConfPort0SFMEP':xgs360026fERPSConfPort0SFMEP,'xgs360026fERPSConfPort1SFMEP':xgs360026fERPSConfPort1SFMEP,'xgs360026fERPSConfPort0APSMEP':xgs360026fERPSConfPort0APSMEP,'xgs360026fERPSConfPort1APSMEP':xgs360026fERPSConfPort1APSMEP,'xgs360026fERPSConfRingType':xgs360026fERPSConfRingType,'xgs360026fERPSConfInterconnectedNode':xgs360026fERPSConfInterconnectedNode,'xgs360026fERPSConfVirtualChannel':xgs360026fERPSConfVirtualChannel,'xgs360026fERPSConfMajorRingID':xgs360026fERPSConfMajorRingID,'xgs360026fERPSConfAlarm':xgs360026fERPSConfAlarm,'xgs360026fERPSInstanceConfConfigured':xgs360026fERPSInstanceConfConfigured,'xgs360026fERPSInstanceConfGuardTime':xgs360026fERPSInstanceConfGuardTime,'xgs360026fERPSInstanceConfWTRTime':xgs360026fERPSInstanceConfWTRTime,'xgs360026fERPSInstanceConfHoldOffTime':xgs360026fERPSInstanceConfHoldOffTime,'xgs360026fERPSInstanceConfVersion':xgs360026fERPSInstanceConfVersion,'xgs360026fERPSInstanceConfRevertive':xgs360026fERPSInstanceConfRevertive,'xgs360026fERPSInstanceConfVLANconfig':xgs360026fERPSInstanceConfVLANconfig,'xgs360026fERPSConfRowStatus':xgs360026fERPSConfRowStatus,'xgs360026fMRSTP':xgs360026fMRSTP,'xgs360026fMRSTPInstance':xgs360026fMRSTPInstance,'xgs360026fMRSTPInstanceConf':xgs360026fMRSTPInstanceConf,'xgs360026fMRSTPInstanceConfGlobalState':xgs360026fMRSTPInstanceConfGlobalState,'xgs360026fMRSTPInstanceConfigurationTable':xgs360026fMRSTPInstanceConfigurationTable,'xgs360026fMRSTPInstanceConfigurationEntry':xgs360026fMRSTPInstanceConfigurationEntry,_c:xgs360026fMRSTPInstanceConfigurationInstance,'xgs360026fMRSTPInstanceConfigurationState':xgs360026fMRSTPInstanceConfigurationState,'xgs360026fMRSTPInstanceConfigurationVersion':xgs360026fMRSTPInstanceConfigurationVersion,'xgs360026fMRSTPInstanceConfigurationPriority':xgs360026fMRSTPInstanceConfigurationPriority,'xgs360026fMRSTPInstanceConfigurationHelloTime':xgs360026fMRSTPInstanceConfigurationHelloTime,'xgs360026fMRSTPInstanceConfigurationMaxAge':xgs360026fMRSTPInstanceConfigurationMaxAge,'xgs360026fMRSTPInstanceConfigurationFWDelay':xgs360026fMRSTPInstanceConfigurationFWDelay,'xgs360026fMRSTPInstanceStatus':xgs360026fMRSTPInstanceStatus,'xgs360026fMRSTPInstanceStatusTable':xgs360026fMRSTPInstanceStatusTable,'xgs360026fMRSTPInstanceStatusEntry':xgs360026fMRSTPInstanceStatusEntry,_d:xgs360026fMRSTPInstanceStatusInstance,'xgs360026fMRSTPInstanceStatusGlobalState':xgs360026fMRSTPInstanceStatusGlobalState,'xgs360026fMRSTPInstanceStatusInstanceConfigState':xgs360026fMRSTPInstanceStatusInstanceConfigState,'xgs360026fMRSTPInstanceStatusInstanceCurrentState':xgs360026fMRSTPInstanceStatusInstanceCurrentState,'xgs360026fMRSTPInstanceStatusBridgeID':xgs360026fMRSTPInstanceStatusBridgeID,'xgs360026fMRSTPInstanceStatusBridgePrioriry':xgs360026fMRSTPInstanceStatusBridgePrioriry,'xgs360026fMRSTPInstanceStatusRootID':xgs360026fMRSTPInstanceStatusRootID,'xgs360026fMRSTPInstanceStatusRootPriority':xgs360026fMRSTPInstanceStatusRootPriority,'xgs360026fMRSTPInstanceStatusRootPort':xgs360026fMRSTPInstanceStatusRootPort,'xgs360026fMRSTPInstanceStatusRootPathCost':xgs360026fMRSTPInstanceStatusRootPathCost,'xgs360026fMRSTPInstanceStatusCurrentMaxAge':xgs360026fMRSTPInstanceStatusCurrentMaxAge,'xgs360026fMRSTPInstanceStatusCurrentForwardDelay':xgs360026fMRSTPInstanceStatusCurrentForwardDelay,'xgs360026fMRSTPInstanceStatusHelloTime':xgs360026fMRSTPInstanceStatusHelloTime,'xgs360026fMRSTPInstanceStatusTopologyChangeCount':xgs360026fMRSTPInstanceStatusTopologyChangeCount,'xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange':xgs360026fMRSTPInstanceStatusTimeSinceLastTopologyChange,'xgs360026fMRSTPPort':xgs360026fMRSTPPort,'xgs360026fMRSTPPortConfiguration':xgs360026fMRSTPPortConfiguration,'xgs360026fMRSTPPortConfigurationTable':xgs360026fMRSTPPortConfigurationTable,'xgs360026fMRSTPPortConfigurationEntry':xgs360026fMRSTPPortConfigurationEntry,_e:xgs360026fMRSTPPortConfigurationPort,'xgs360026fMRSTPPortConfigurationInstance':xgs360026fMRSTPPortConfigurationInstance,'xgs360026fMRSTPPortConfigurationPathCost':xgs360026fMRSTPPortConfigurationPathCost,'xgs360026fMRSTPPortConfigurationPriority':xgs360026fMRSTPPortConfigurationPriority,'xgs360026fMRSTPPortConfigurationAdminEdge':xgs360026fMRSTPPortConfigurationAdminEdge,'xgs360026fMRSTPPortConfigurationAdminP2P':xgs360026fMRSTPPortConfigurationAdminP2P,'xgs360026fMRSTPPortConfigurationMigrateCheck':xgs360026fMRSTPPortConfigurationMigrateCheck,'xgs360026fMRSTPPortStatus':xgs360026fMRSTPPortStatus,'xgs360026fMRSTPPortStatusTable':xgs360026fMRSTPPortStatusTable,'xgs360026fMRSTPPortStatusEntry':xgs360026fMRSTPPortStatusEntry,_f:xgs360026fMRSTPPortStatusPort,'xgs360026fMRSTPPortStatusInstance':xgs360026fMRSTPPortStatusInstance,'xgs360026fMRSTPPortStatusState':xgs360026fMRSTPPortStatusState,'xgs360026fMRSTPPortStatusRole':xgs360026fMRSTPPortStatusRole,'xgs360026fMRSTPPortStatusPathCost':xgs360026fMRSTPPortStatusPathCost,'xgs360026fMRSTPPortStatusPathCostConfig':xgs360026fMRSTPPortStatusPathCostConfig,'xgs360026fMRSTPPortStatusPriority':xgs360026fMRSTPPortStatusPriority,'xgs360026fMRSTPPortStatusAdminEdge':xgs360026fMRSTPPortStatusAdminEdge,'xgs360026fMRSTPPortStatusAdminP2P':xgs360026fMRSTPPortStatusAdminP2P,'xgs360026fSecurity':xgs360026fSecurity,'xgs360026fIPSourceGuard':xgs360026fIPSourceGuard,'xgs360026fIPSourceGuardConf':xgs360026fIPSourceGuardConf,'xgs360026fIPSourceGuardMode':xgs360026fIPSourceGuardMode,'xgs360026fIPSourceGuardPortConfigTable':xgs360026fIPSourceGuardPortConfigTable,'xgs360026fIPSourceGuardPortConfigEntry':xgs360026fIPSourceGuardPortConfigEntry,_g:xgs360026fIPSourceGuardPortConfigPort,'xgs360026fIPSourceGuardPortConfigMode':xgs360026fIPSourceGuardPortConfigMode,'xgs360026fIPSourceGuardPortMaxDynamicClients':xgs360026fIPSourceGuardPortMaxDynamicClients,'xgs360026fIPSourceGuardStatic':xgs360026fIPSourceGuardStatic,'xgs360026fIPSourceGuardStaticCreate':xgs360026fIPSourceGuardStaticCreate,'xgs360026fIPSourceGuardStaticTable':xgs360026fIPSourceGuardStaticTable,'xgs360026fIPSourceGuardStaticEntry':xgs360026fIPSourceGuardStaticEntry,_h:xgs360026fIPSourceGuardStaticIndex,'xgs360026fIPSourceGuardStaticPort':xgs360026fIPSourceGuardStaticPort,'xgs360026fIPSourceGuardStaticVLANId':xgs360026fIPSourceGuardStaticVLANId,'xgs360026fIPSourceGuardStaticIPAddress':xgs360026fIPSourceGuardStaticIPAddress,'xgs360026fIPSourceGuardStaticMACAddress':xgs360026fIPSourceGuardStaticMACAddress,'xgs360026fIPSourceGuardStaticRowStatus':xgs360026fIPSourceGuardStaticRowStatus,'xgs360026fIPSourceGuardDynamicTable':xgs360026fIPSourceGuardDynamicTable,'xgs360026fIPSourceGuardDynamicEntry':xgs360026fIPSourceGuardDynamicEntry,_i:xgs360026fIPSourceGuardDynamicIndex,'xgs360026fIPSourceGuardDynamicPort':xgs360026fIPSourceGuardDynamicPort,'xgs360026fIPSourceGuardDynamicVLANId':xgs360026fIPSourceGuardDynamicVLANId,'xgs360026fIPSourceGuardDynamicIPAddress':xgs360026fIPSourceGuardDynamicIPAddress,'xgs360026fIPSourceGuardDynamicMACAddress':xgs360026fIPSourceGuardDynamicMACAddress,'xgs360026fARPInspection':xgs360026fARPInspection,'xgs360026fARPInspectionConf':xgs360026fARPInspectionConf,'xgs360026fARPInspectionConfMode':xgs360026fARPInspectionConfMode,'xgs360026fARPInspectionConfTable':xgs360026fARPInspectionConfTable,'xgs360026fARPInspectionConfEntry':xgs360026fARPInspectionConfEntry,_j:xgs360026fARPInspectionConfPortIndex,'xgs360026fARPInspectionConfPortMode':xgs360026fARPInspectionConfPortMode,'xgs360026fARPInspectionStatic':xgs360026fARPInspectionStatic,'xgs360026fARPInspectionStaticCreate':xgs360026fARPInspectionStaticCreate,'xgs360026fARPInspectionStaticTable':xgs360026fARPInspectionStaticTable,'xgs360026fARPInspectionStaticEntry':xgs360026fARPInspectionStaticEntry,_k:xgs360026fARPInspectionStaticIndex,'xgs360026fARPInspectionStaticPort':xgs360026fARPInspectionStaticPort,'xgs360026fARPInspectionStaticVLANId':xgs360026fARPInspectionStaticVLANId,'xgs360026fARPInspectionStaticIPAddress':xgs360026fARPInspectionStaticIPAddress,'xgs360026fARPInspectionStaticMACAddress':xgs360026fARPInspectionStaticMACAddress,'xgs360026fARPInspectionStaticRowStatus':xgs360026fARPInspectionStaticRowStatus,'xgs360026fARPInspectionDynamicTable':xgs360026fARPInspectionDynamicTable,'xgs360026fARPInspectionDynamicEntry':xgs360026fARPInspectionDynamicEntry,_l:xgs360026fARPInspectionDynamicIndex,'xgs360026fARPInspectionDynamicPort':xgs360026fARPInspectionDynamicPort,'xgs360026fARPInspectionDynamicVLANId':xgs360026fARPInspectionDynamicVLANId,'xgs360026fARPInspectionDynamicIPAddress':xgs360026fARPInspectionDynamicIPAddress,'xgs360026fARPInspectionDynamicMACAddress':xgs360026fARPInspectionDynamicMACAddress,'xgs360026fDHCPSnooping':xgs360026fDHCPSnooping,'xgs360026fDHCPSnoopingConf':xgs360026fDHCPSnoopingConf,'xgs360026fDHCPSnoopingMode':xgs360026fDHCPSnoopingMode,'xgs360026fDHCPSnoopingPortModeConfigurationTable':xgs360026fDHCPSnoopingPortModeConfigurationTable,'xgs360026fDHCPSnoopingPortModeConfigurationEntry':xgs360026fDHCPSnoopingPortModeConfigurationEntry,_m:xgs360026fDHCPSnoopingPortModeConfigurationPort,'xgs360026fDHCPSnoopingPortModeConfigurationMode':xgs360026fDHCPSnoopingPortModeConfigurationMode,'xgs360026fDHCPSnoopingStatisticsTable':xgs360026fDHCPSnoopingStatisticsTable,'xgs360026fDHCPSnoopingStatisticsEntry':xgs360026fDHCPSnoopingStatisticsEntry,_n:xgs360026fDHCPSnoopingStatisticsPort,'xgs360026fDHCPSnoopingStatisticsClear':xgs360026fDHCPSnoopingStatisticsClear,'xgs360026fDHCPSnoopingRxDiscover':xgs360026fDHCPSnoopingRxDiscover,'xgs360026fDHCPSnoopingRxOffer':xgs360026fDHCPSnoopingRxOffer,'xgs360026fDHCPSnoopingRxRequest':xgs360026fDHCPSnoopingRxRequest,'xgs360026fDHCPSnoopingRxDecline':xgs360026fDHCPSnoopingRxDecline,'xgs360026fDHCPSnoopingRxACK':xgs360026fDHCPSnoopingRxACK,'xgs360026fDHCPSnoopingRxNAK':xgs360026fDHCPSnoopingRxNAK,'xgs360026fDHCPSnoopingRxRelease':xgs360026fDHCPSnoopingRxRelease,'xgs360026fDHCPSnoopingRxInform':xgs360026fDHCPSnoopingRxInform,'xgs360026fDHCPSnoopingRxLeaseQuery':xgs360026fDHCPSnoopingRxLeaseQuery,'xgs360026fDHCPSnoopingRxLeaseUnassigned':xgs360026fDHCPSnoopingRxLeaseUnassigned,'xgs360026fDHCPSnoopingRxLeaseUnknown':xgs360026fDHCPSnoopingRxLeaseUnknown,'xgs360026fDHCPSnoopingRxLeaseActive':xgs360026fDHCPSnoopingRxLeaseActive,'xgs360026fDHCPSnoopingTxDiscover':xgs360026fDHCPSnoopingTxDiscover,'xgs360026fDHCPSnoopingTxOffer':xgs360026fDHCPSnoopingTxOffer,'xgs360026fDHCPSnoopingTxRequest':xgs360026fDHCPSnoopingTxRequest,'xgs360026fDHCPSnoopingTxDecline':xgs360026fDHCPSnoopingTxDecline,'xgs360026fDHCPSnoopingTxACK':xgs360026fDHCPSnoopingTxACK,'xgs360026fDHCPSnoopingTxNAK':xgs360026fDHCPSnoopingTxNAK,'xgs360026fDHCPSnoopingTxRelease':xgs360026fDHCPSnoopingTxRelease,'xgs360026fDHCPSnoopingTxInform':xgs360026fDHCPSnoopingTxInform,'xgs360026fDHCPSnoopingTxLeaseQuery':xgs360026fDHCPSnoopingTxLeaseQuery,'xgs360026fDHCPSnoopingTxLeaseUnassigned':xgs360026fDHCPSnoopingTxLeaseUnassigned,'xgs360026fDHCPSnoopingTxLeaseUnknown':xgs360026fDHCPSnoopingTxLeaseUnknown,'xgs360026fDHCPSnoopingTxLeaseActive':xgs360026fDHCPSnoopingTxLeaseActive,'xgs360026fDHCPRelay':xgs360026fDHCPRelay,'xgs360026fDHCPRelayConfiguration':xgs360026fDHCPRelayConfiguration,'xgs360026fDHCPRelayMode':xgs360026fDHCPRelayMode,'xgs360026fDHCPRelayServer':xgs360026fDHCPRelayServer,'xgs360026fDHCPRelayInformationMode':xgs360026fDHCPRelayInformationMode,'xgs360026fDHCPRelayInformationPolicy':xgs360026fDHCPRelayInformationPolicy,'xgs360026fDHCPRelayStatistics':xgs360026fDHCPRelayStatistics,'xgs360026fDHCPRelayServerStatistics':xgs360026fDHCPRelayServerStatistics,'xgs360026fServerStatTransmitToServer':xgs360026fServerStatTransmitToServer,'xgs360026fServerStatTransmitError':xgs360026fServerStatTransmitError,'xgs360026fServerStatReceiveFromServer':xgs360026fServerStatReceiveFromServer,'xgs360026fServerStatReceiveMissingAgentOption':xgs360026fServerStatReceiveMissingAgentOption,'xgs360026fServerStatReceiveMissingCircuitID':xgs360026fServerStatReceiveMissingCircuitID,'xgs360026fServerStatReceiveMissingRemoteID':xgs360026fServerStatReceiveMissingRemoteID,'xgs360026fServerStatReceiveBadCircuitID':xgs360026fServerStatReceiveBadCircuitID,'xgs360026fServerStatReceiveBadRemoteID':xgs360026fServerStatReceiveBadRemoteID,'xgs360026fDHCPRelayClientStatistics':xgs360026fDHCPRelayClientStatistics,'xgs360026fClientStatTransmitToClient':xgs360026fClientStatTransmitToClient,'xgs360026fClientStatTransmitError':xgs360026fClientStatTransmitError,'xgs360026fClientStatReceivefromClient':xgs360026fClientStatReceivefromClient,'xgs360026fClientStatReceiveAgentOption':xgs360026fClientStatReceiveAgentOption,'xgs360026fClientStatReplaceAgentOption':xgs360026fClientStatReplaceAgentOption,'xgs360026fClientStatKeepAgentOption':xgs360026fClientStatKeepAgentOption,'xgs360026fClientStatDropAgentOption':xgs360026fClientStatDropAgentOption,'xgs360026fPortSecurity':xgs360026fPortSecurity,'xgs360026fPortSecLimitCtrl':xgs360026fPortSecLimitCtrl,'xgs360026fPortSecLimitCtrlSystemConf':xgs360026fPortSecLimitCtrlSystemConf,'xgs360026fPortSecurityMode':xgs360026fPortSecurityMode,'xgs360026fPortSecurityAging':xgs360026fPortSecurityAging,'xgs360026fPortSecurityAgingPeriod':xgs360026fPortSecurityAgingPeriod,'xgs360026fPortSecLimitCtrlTable':xgs360026fPortSecLimitCtrlTable,'xgs360026fPortSecLimitCtrlEntry':xgs360026fPortSecLimitCtrlEntry,_o:xgs360026fPortSecLimitCtrlPort,'xgs360026fPortSecLimitCtrlPortMode':xgs360026fPortSecLimitCtrlPortMode,'xgs360026fPortSecLimitCtrlPortLimit':xgs360026fPortSecLimitCtrlPortLimit,'xgs360026fPortSecLimitCtrlPortAction':xgs360026fPortSecLimitCtrlPortAction,'xgs360026fPortSecLimitCtrlPortState':xgs360026fPortSecLimitCtrlPortState,'xgs360026fPortSecLimitCtrlPortReOpen':xgs360026fPortSecLimitCtrlPortReOpen,'xgs360026fPortSecSwitchStatusTable':xgs360026fPortSecSwitchStatusTable,'xgs360026fPortSecSwitchStatusEntry':xgs360026fPortSecSwitchStatusEntry,_p:xgs360026fPortSecSwitchStatusPort,'xgs360026fPortSecSwitchStatusUsers':xgs360026fPortSecSwitchStatusUsers,'xgs360026fPortSecSwitchStatusState':xgs360026fPortSecSwitchStatusState,'xgs360026fPortSecSwitchStatusMACCountCurrent':xgs360026fPortSecSwitchStatusMACCountCurrent,'xgs360026fPortSecSwitchStatusMACCountLimit':xgs360026fPortSecSwitchStatusMACCountLimit,'xgs360026fPortSecPortStatus':xgs360026fPortSecPortStatus,'xgs360026fPortSecPortStatusPort':xgs360026fPortSecPortStatusPort,'xgs360026fPortSecPortStatusTable':xgs360026fPortSecPortStatusTable,'xgs360026fPortSecPortStatusEntry':xgs360026fPortSecPortStatusEntry,_q:xgs360026fPortSecPortStatusIndex,'xgs360026fPortSecPortStatusMACAddress':xgs360026fPortSecPortStatusMACAddress,'xgs360026fPortSecPortStatusVLANId':xgs360026fPortSecPortStatusVLANId,'xgs360026fPortSecPortStatusState':xgs360026fPortSecPortStatusState,'xgs360026fPortSecPortStatusTimeOfAddition':xgs360026fPortSecPortStatusTimeOfAddition,'xgs360026fPortSecPortStatusAgeAndHold':xgs360026fPortSecPortStatusAgeAndHold,'xgs360026fAccessManagement':xgs360026fAccessManagement,'xgs360026fAccessMgtConf':xgs360026fAccessMgtConf,'xgs360026fAccessMgtConfMode':xgs360026fAccessMgtConfMode,'xgs360026fAccessMgtConfCreate':xgs360026fAccessMgtConfCreate,'xgs360026fAccessMgtConfTable':xgs360026fAccessMgtConfTable,'xgs360026fAccessMgtConfEntry':xgs360026fAccessMgtConfEntry,_r:xgs360026fAccessMgtIndex,'xgs360026fAccessMgtAddresstype':xgs360026fAccessMgtAddresstype,'xgs360026fAccessMgtStartIpAddress':xgs360026fAccessMgtStartIpAddress,'xgs360026fAccessMgtEndIpAddress':xgs360026fAccessMgtEndIpAddress,'xgs360026fAccessMgtHttpHttps':xgs360026fAccessMgtHttpHttps,'xgs360026fAccessMgtSNMP':xgs360026fAccessMgtSNMP,'xgs360026fAccessMgtTelnetSSH':xgs360026fAccessMgtTelnetSSH,'xgs360026fAccessMgtRowStatus':xgs360026fAccessMgtRowStatus,'xgs360026fAccessMgtStatistics':xgs360026fAccessMgtStatistics,'xgs360026fHttpReceivedPkts':xgs360026fHttpReceivedPkts,'xgs360026fHttpAllowedPkts':xgs360026fHttpAllowedPkts,'xgs360026fHttpDiscardedPkts':xgs360026fHttpDiscardedPkts,'xgs360026fHttpsReceivedPkts':xgs360026fHttpsReceivedPkts,'xgs360026fHttpsAllowedPkts':xgs360026fHttpsAllowedPkts,'xgs360026fHttpsDiscardedPkts':xgs360026fHttpsDiscardedPkts,'xgs360026fSnmpReceivedPkts':xgs360026fSnmpReceivedPkts,'xgs360026fSnmpAllowedPkts':xgs360026fSnmpAllowedPkts,'xgs360026fSnmpDiscardedPkts':xgs360026fSnmpDiscardedPkts,'xgs360026fTelnetReceivedPkts':xgs360026fTelnetReceivedPkts,'xgs360026fTelnetAllowedPkts':xgs360026fTelnetAllowedPkts,'xgs360026fTelnetDiscardedPkts':xgs360026fTelnetDiscardedPkts,'xgs360026fSSHReceivedPkts':xgs360026fSSHReceivedPkts,'xgs360026fSSHAllowedPkts':xgs360026fSSHAllowedPkts,'xgs360026fSSHDiscardedPkts':xgs360026fSSHDiscardedPkts,'xgs360026fAccessMgtStatisticsClearAll':xgs360026fAccessMgtStatisticsClearAll,'xgs360026fSSH':xgs360026fSSH,'xgs360026fSSHMode':xgs360026fSSHMode,'xgs360026fHTTPS':xgs360026fHTTPS,'xgs360026fHTTPSMode':xgs360026fHTTPSMode,'xgs360026fHTTPSAutoRedirect':xgs360026fHTTPSAutoRedirect,'xgs360026fAuthMethod':xgs360026fAuthMethod,'xgs360026fConsoleAuthMethod':xgs360026fConsoleAuthMethod,'xgs360026fConsoleFallback':xgs360026fConsoleFallback,'xgs360026fTelnetAuthMethod':xgs360026fTelnetAuthMethod,'xgs360026fTelnetFallback':xgs360026fTelnetFallback,'xgs360026fSshAuthMethod':xgs360026fSshAuthMethod,'xgs360026fSshFallback':xgs360026fSshFallback,'xgs360026fWebAuthMethod':xgs360026fWebAuthMethod,'xgs360026fWebFallback':xgs360026fWebFallback,'xgs360026fMaintenance':xgs360026fMaintenance,'xgs360026fRestartDevice':xgs360026fRestartDevice,'xgs360026fFirmware':xgs360026fFirmware,'xgs360026fFirmwareIpAddress':xgs360026fFirmwareIpAddress,'xgs360026fFirmwareFileName':xgs360026fFirmwareFileName,'xgs360026fDoFirmwareUpgrade':xgs360026fDoFirmwareUpgrade,'xgs360026fSaveOrRestore':xgs360026fSaveOrRestore,'xgs360026fFactoryDefaults':xgs360026fFactoryDefaults,'xgs360026fSaveStart':xgs360026fSaveStart,'xgs360026fSaveUser':xgs360026fSaveUser,'xgs360026fRestoreUser':xgs360026fRestoreUser,'xgs360026fExportOrImport':xgs360026fExportOrImport,'xgs360026fExportIpAddress':xgs360026fExportIpAddress,'xgs360026fExportConfigName':xgs360026fExportConfigName,'xgs360026fDoExportConfig':xgs360026fDoExportConfig,'xgs360026fImportIpAddress':xgs360026fImportIpAddress,'xgs360026fImportConfigName':xgs360026fImportConfigName,'xgs360026fDoImportConfig':xgs360026fDoImportConfig,'xgs360026fDiagnostics':xgs360026fDiagnostics,'xgs360026fPingIpAddress':xgs360026fPingIpAddress,'xgs360026fPingSize':xgs360026fPingSize,'xgs360026fDoPingConfig':xgs360026fDoPingConfig,'xgs360026fPingResult':xgs360026fPingResult,'xgs360026fPing6IpAddress':xgs360026fPing6IpAddress,'xgs360026fPing6Size':xgs360026fPing6Size,'xgs360026fDoPing6Config':xgs360026fDoPing6Config,'xgs360026fPing6Result':xgs360026fPing6Result,'xgs360026fVeriPHY':xgs360026fVeriPHY,'xgs360026fVeriPHYTest':xgs360026fVeriPHYTest,'xgs360026fVeriPHYTable':xgs360026fVeriPHYTable,'xgs360026fVeriPHYEntry':xgs360026fVeriPHYEntry,_s:xgs360026fVeriPHYPort,'xgs360026fVeriPHYPairA':xgs360026fVeriPHYPairA,'xgs360026fVeriPHYLengthA':xgs360026fVeriPHYLengthA,'xgs360026fVeriPHYPairB':xgs360026fVeriPHYPairB,'xgs360026fVeriPHYLengthB':xgs360026fVeriPHYLengthB,'xgs360026fVeriPHYPairC':xgs360026fVeriPHYPairC,'xgs360026fVeriPHYLengthC':xgs360026fVeriPHYLengthC,'xgs360026fVeriPHYPairD':xgs360026fVeriPHYPairD,'xgs360026fVeriPHYLengthD':xgs360026fVeriPHYLengthD,'xgs360026fTrap':xgs360026fTrap,'xgs360026fTrapEvent':xgs360026fTrapEvent,'xgs360026fEmergency':xgs360026fEmergency,'xgs360026fAlert':xgs360026fAlert,'xgs360026fCritical':xgs360026fCritical,'xgs360026fError':xgs360026fError,'xgs360026fWarning':xgs360026fWarning,'xgs360026fNotice':xgs360026fNotice,'xgs360026fInformational':xgs360026fInformational,'xgs360026fDebug':xgs360026fDebug,'xgs360026fTrapVariable':xgs360026fTrapVariable,_H:xgs360026fInformation})