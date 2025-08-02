_s='xgs360028fVeriPHYPort'
_r='xgs360028fAccessMgtIndex'
_q='xgs360028fPortSecPortStatusIndex'
_p='xgs360028fPortSecSwitchStatusPort'
_o='xgs360028fPortSecLimitCtrlPort'
_n='xgs360028fDHCPSnoopingStatisticsPort'
_m='xgs360028fDHCPSnoopingPortModeConfigurationPort'
_l='xgs360028fARPInspectionDynamicIndex'
_k='xgs360028fARPInspectionStaticIndex'
_j='xgs360028fARPInspectionConfPortIndex'
_i='xgs360028fIPSourceGuardDynamicIndex'
_h='xgs360028fIPSourceGuardStaticIndex'
_g='xgs360028fIPSourceGuardPortConfigPort'
_f='xgs360028fMRSTPPortStatusPort'
_e='xgs360028fMRSTPPortConfigurationPort'
_d='xgs360028fMRSTPInstanceStatusInstance'
_c='xgs360028fMRSTPInstanceConfigurationInstance'
_b='xgs360028fERPSConfIndex'
_a='xgs360028fACLACEStatusIndex'
_Z='xgs360028fACLACEIndex'
_Y='xgs360028fACLRateLimiterID'
_X='xgs360028fACLPortsConfPort'
_W='xgs360028fMirrorPort'
_V='xgs360028fThermalProtectionPort'
_U='xgs360028fGVRPStatisticsPort'
_T='xgs360028fGVRPConfPort'
_S='xgs360028fGARPStatisticsPort'
_R='xgs360028fGARPConfPort'
_Q='xgs360028fSFPInfoIndex'
_P='xgs360028fPortQoSStatisticsPort'
_O='xgs360028fPortTrafficStatisticsPort'
_N='xgs360028fPortConfPort'
_M='xgs360028fTrapHostConfIndex'
_L='xgs360028fSyslogDetailedInfoIndex'
_K='xgs360028fUserIndex'
_J='xgs360028fSystemTimeNTPIndex'
_I='MacAddress'
_H='xgs360028fInformation'
_G='DisplayString'
_F='not-accessible'
_E='ZYXEL-XGS360028F-FUNCTION-MIB'
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
_Xgs360028fProductId_ObjectIdentity=ObjectIdentity
xgs360028fProductId=_Xgs360028fProductId_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78))
_Xgs360028fSystem_ObjectIdentity=ObjectIdentity
xgs360028fSystem=_Xgs360028fSystem_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1))
_Xgs360028fSystemInformation_ObjectIdentity=ObjectIdentity
xgs360028fSystemInformation=_Xgs360028fSystemInformation_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,1))
_Xgs360028fModelName_Type=DisplayString
_Xgs360028fModelName_Object=MibScalar
xgs360028fModelName=_Xgs360028fModelName_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,1),_Xgs360028fModelName_Type())
xgs360028fModelName.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fModelName.setStatus(_A)
_Xgs360028fBIOSVersion_Type=DisplayString
_Xgs360028fBIOSVersion_Object=MibScalar
xgs360028fBIOSVersion=_Xgs360028fBIOSVersion_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,2),_Xgs360028fBIOSVersion_Type())
xgs360028fBIOSVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fBIOSVersion.setStatus(_A)
_Xgs360028fFirmwareVersion_Type=DisplayString
_Xgs360028fFirmwareVersion_Object=MibScalar
xgs360028fFirmwareVersion=_Xgs360028fFirmwareVersion_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,3),_Xgs360028fFirmwareVersion_Type())
xgs360028fFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fFirmwareVersion.setStatus(_A)
_Xgs360028fHardwareMechanicalVersion_Type=DisplayString
_Xgs360028fHardwareMechanicalVersion_Object=MibScalar
xgs360028fHardwareMechanicalVersion=_Xgs360028fHardwareMechanicalVersion_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,4),_Xgs360028fHardwareMechanicalVersion_Type())
xgs360028fHardwareMechanicalVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fHardwareMechanicalVersion.setStatus(_A)
_Xgs360028fSeriesNumber_Type=DisplayString
_Xgs360028fSeriesNumber_Object=MibScalar
xgs360028fSeriesNumber=_Xgs360028fSeriesNumber_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,5),_Xgs360028fSeriesNumber_Type())
xgs360028fSeriesNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSeriesNumber.setStatus(_A)
_Xgs360028fHostMACAddress_Type=MacAddress
_Xgs360028fHostMACAddress_Object=MibScalar
xgs360028fHostMACAddress=_Xgs360028fHostMACAddress_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,6),_Xgs360028fHostMACAddress_Type())
xgs360028fHostMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fHostMACAddress.setStatus(_A)
_Xgs360028fConsoleBaudrate_Type=DisplayString
_Xgs360028fConsoleBaudrate_Object=MibScalar
xgs360028fConsoleBaudrate=_Xgs360028fConsoleBaudrate_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,7),_Xgs360028fConsoleBaudrate_Type())
xgs360028fConsoleBaudrate.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fConsoleBaudrate.setStatus(_A)
_Xgs360028fRAMSize_Type=DisplayString
_Xgs360028fRAMSize_Object=MibScalar
xgs360028fRAMSize=_Xgs360028fRAMSize_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,8),_Xgs360028fRAMSize_Type())
xgs360028fRAMSize.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fRAMSize.setStatus(_A)
_Xgs360028fFlashSize_Type=DisplayString
_Xgs360028fFlashSize_Object=MibScalar
xgs360028fFlashSize=_Xgs360028fFlashSize_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,9),_Xgs360028fFlashSize_Type())
xgs360028fFlashSize.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fFlashSize.setStatus(_A)
_Xgs360028fBridgeFBDSize_Type=DisplayString
_Xgs360028fBridgeFBDSize_Object=MibScalar
xgs360028fBridgeFBDSize=_Xgs360028fBridgeFBDSize_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,10),_Xgs360028fBridgeFBDSize_Type())
xgs360028fBridgeFBDSize.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fBridgeFBDSize.setStatus(_A)
_Xgs360028fTransmitQueue_Type=DisplayString
_Xgs360028fTransmitQueue_Object=MibScalar
xgs360028fTransmitQueue=_Xgs360028fTransmitQueue_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,11),_Xgs360028fTransmitQueue_Type())
xgs360028fTransmitQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fTransmitQueue.setStatus(_A)
_Xgs360028fMaximumFrameSize_Type=DisplayString
_Xgs360028fMaximumFrameSize_Object=MibScalar
xgs360028fMaximumFrameSize=_Xgs360028fMaximumFrameSize_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,12),_Xgs360028fMaximumFrameSize_Type())
xgs360028fMaximumFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMaximumFrameSize.setStatus(_A)
_Xgs360028fCPULoad_Type=DisplayString
_Xgs360028fCPULoad_Object=MibScalar
xgs360028fCPULoad=_Xgs360028fCPULoad_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,13),_Xgs360028fCPULoad_Type())
xgs360028fCPULoad.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fCPULoad.setStatus(_A)
_Xgs360028fFanSpeed_Type=DisplayString
_Xgs360028fFanSpeed_Object=MibScalar
xgs360028fFanSpeed=_Xgs360028fFanSpeed_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,14),_Xgs360028fFanSpeed_Type())
xgs360028fFanSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fFanSpeed.setStatus(_A)
_Xgs360028fPowers_Type=DisplayString
_Xgs360028fPowers_Object=MibScalar
xgs360028fPowers=_Xgs360028fPowers_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,15),_Xgs360028fPowers_Type())
xgs360028fPowers.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPowers.setStatus(_A)
_Xgs360028fTemperature1_Type=DisplayString
_Xgs360028fTemperature1_Object=MibScalar
xgs360028fTemperature1=_Xgs360028fTemperature1_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,16),_Xgs360028fTemperature1_Type())
xgs360028fTemperature1.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fTemperature1.setStatus(_A)
_Xgs360028fTemperature2_Type=DisplayString
_Xgs360028fTemperature2_Object=MibScalar
xgs360028fTemperature2=_Xgs360028fTemperature2_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,17),_Xgs360028fTemperature2_Type())
xgs360028fTemperature2.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fTemperature2.setStatus(_A)
_Xgs360028fTemperature3_Type=DisplayString
_Xgs360028fTemperature3_Object=MibScalar
xgs360028fTemperature3=_Xgs360028fTemperature3_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,18),_Xgs360028fTemperature3_Type())
xgs360028fTemperature3.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fTemperature3.setStatus(_A)
_Xgs360028fTemperature4_Type=DisplayString
_Xgs360028fTemperature4_Object=MibScalar
xgs360028fTemperature4=_Xgs360028fTemperature4_Object((1,3,6,1,4,1,890,1,5,8,78,1,1,19),_Xgs360028fTemperature4_Type())
xgs360028fTemperature4.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fTemperature4.setStatus(_A)
_Xgs360028fSystemTime_ObjectIdentity=ObjectIdentity
xgs360028fSystemTime=_Xgs360028fSystemTime_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,2))
_Xgs360028fSystemTimeManual_ObjectIdentity=ObjectIdentity
xgs360028fSystemTimeManual=_Xgs360028fSystemTimeManual_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,2,1))
class _Xgs360028fSystemTimeManualClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fSystemTimeManualClockSource_Type.__name__=_B
_Xgs360028fSystemTimeManualClockSource_Object=MibScalar
xgs360028fSystemTimeManualClockSource=_Xgs360028fSystemTimeManualClockSource_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,1),_Xgs360028fSystemTimeManualClockSource_Type())
xgs360028fSystemTimeManualClockSource.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualClockSource.setStatus(_A)
_Xgs360028fSystemTimeManualLocaltime_Type=DisplayString
_Xgs360028fSystemTimeManualLocaltime_Object=MibScalar
xgs360028fSystemTimeManualLocaltime=_Xgs360028fSystemTimeManualLocaltime_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,2),_Xgs360028fSystemTimeManualLocaltime_Type())
xgs360028fSystemTimeManualLocaltime.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualLocaltime.setStatus(_A)
class _Xgs360028fSystemTimeManualTimeZoneOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-720,780))
_Xgs360028fSystemTimeManualTimeZoneOffset_Type.__name__=_B
_Xgs360028fSystemTimeManualTimeZoneOffset_Object=MibScalar
xgs360028fSystemTimeManualTimeZoneOffset=_Xgs360028fSystemTimeManualTimeZoneOffset_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,3),_Xgs360028fSystemTimeManualTimeZoneOffset_Type())
xgs360028fSystemTimeManualTimeZoneOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualTimeZoneOffset.setStatus(_A)
class _Xgs360028fSystemTimeManualDaylightSavings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fSystemTimeManualDaylightSavings_Type.__name__=_B
_Xgs360028fSystemTimeManualDaylightSavings_Object=MibScalar
xgs360028fSystemTimeManualDaylightSavings=_Xgs360028fSystemTimeManualDaylightSavings_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,4),_Xgs360028fSystemTimeManualDaylightSavings_Type())
xgs360028fSystemTimeManualDaylightSavings.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualDaylightSavings.setStatus(_A)
class _Xgs360028fSystemTimeManualTimeSetOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_Xgs360028fSystemTimeManualTimeSetOffset_Type.__name__=_B
_Xgs360028fSystemTimeManualTimeSetOffset_Object=MibScalar
xgs360028fSystemTimeManualTimeSetOffset=_Xgs360028fSystemTimeManualTimeSetOffset_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,5),_Xgs360028fSystemTimeManualTimeSetOffset_Type())
xgs360028fSystemTimeManualTimeSetOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualTimeSetOffset.setStatus(_A)
class _Xgs360028fSystemTimeManualDaylightSavingsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fSystemTimeManualDaylightSavingsType_Type.__name__=_B
_Xgs360028fSystemTimeManualDaylightSavingsType_Object=MibScalar
xgs360028fSystemTimeManualDaylightSavingsType=_Xgs360028fSystemTimeManualDaylightSavingsType_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,6),_Xgs360028fSystemTimeManualDaylightSavingsType_Type())
xgs360028fSystemTimeManualDaylightSavingsType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualDaylightSavingsType.setStatus(_A)
_Xgs360028fSystemTimeManualDaylightSavingsBydatesFrom_Type=DisplayString
_Xgs360028fSystemTimeManualDaylightSavingsBydatesFrom_Object=MibScalar
xgs360028fSystemTimeManualDaylightSavingsBydatesFrom=_Xgs360028fSystemTimeManualDaylightSavingsBydatesFrom_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,7),_Xgs360028fSystemTimeManualDaylightSavingsBydatesFrom_Type())
xgs360028fSystemTimeManualDaylightSavingsBydatesFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualDaylightSavingsBydatesFrom.setStatus(_A)
_Xgs360028fSystemTimeManualDaylightSavingsBydatesTo_Type=DisplayString
_Xgs360028fSystemTimeManualDaylightSavingsBydatesTo_Object=MibScalar
xgs360028fSystemTimeManualDaylightSavingsBydatesTo=_Xgs360028fSystemTimeManualDaylightSavingsBydatesTo_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,8),_Xgs360028fSystemTimeManualDaylightSavingsBydatesTo_Type())
xgs360028fSystemTimeManualDaylightSavingsBydatesTo.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualDaylightSavingsBydatesTo.setStatus(_A)
class _Xgs360028fSystemTimeManualDaylightSavingsRecurringDayFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_Xgs360028fSystemTimeManualDaylightSavingsRecurringDayFrom_Type.__name__=_B
_Xgs360028fSystemTimeManualDaylightSavingsRecurringDayFrom_Object=MibScalar
xgs360028fSystemTimeManualDaylightSavingsRecurringDayFrom=_Xgs360028fSystemTimeManualDaylightSavingsRecurringDayFrom_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,9),_Xgs360028fSystemTimeManualDaylightSavingsRecurringDayFrom_Type())
xgs360028fSystemTimeManualDaylightSavingsRecurringDayFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualDaylightSavingsRecurringDayFrom.setStatus(_A)
class _Xgs360028fSystemTimeManualDaylightSavingsRecurringWeekFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360028fSystemTimeManualDaylightSavingsRecurringWeekFrom_Type.__name__=_B
_Xgs360028fSystemTimeManualDaylightSavingsRecurringWeekFrom_Object=MibScalar
xgs360028fSystemTimeManualDaylightSavingsRecurringWeekFrom=_Xgs360028fSystemTimeManualDaylightSavingsRecurringWeekFrom_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,10),_Xgs360028fSystemTimeManualDaylightSavingsRecurringWeekFrom_Type())
xgs360028fSystemTimeManualDaylightSavingsRecurringWeekFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualDaylightSavingsRecurringWeekFrom.setStatus(_A)
class _Xgs360028fSystemTimeManualDaylightSavingsRecurringMonthFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_Xgs360028fSystemTimeManualDaylightSavingsRecurringMonthFrom_Type.__name__=_B
_Xgs360028fSystemTimeManualDaylightSavingsRecurringMonthFrom_Object=MibScalar
xgs360028fSystemTimeManualDaylightSavingsRecurringMonthFrom=_Xgs360028fSystemTimeManualDaylightSavingsRecurringMonthFrom_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,11),_Xgs360028fSystemTimeManualDaylightSavingsRecurringMonthFrom_Type())
xgs360028fSystemTimeManualDaylightSavingsRecurringMonthFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualDaylightSavingsRecurringMonthFrom.setStatus(_A)
_Xgs360028fSystemTimeManualDaylightSavingsRecurringTimeFrom_Type=DisplayString
_Xgs360028fSystemTimeManualDaylightSavingsRecurringTimeFrom_Object=MibScalar
xgs360028fSystemTimeManualDaylightSavingsRecurringTimeFrom=_Xgs360028fSystemTimeManualDaylightSavingsRecurringTimeFrom_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,12),_Xgs360028fSystemTimeManualDaylightSavingsRecurringTimeFrom_Type())
xgs360028fSystemTimeManualDaylightSavingsRecurringTimeFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualDaylightSavingsRecurringTimeFrom.setStatus(_A)
class _Xgs360028fSystemTimeManualDaylightSavingsRecurringDayTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_Xgs360028fSystemTimeManualDaylightSavingsRecurringDayTo_Type.__name__=_B
_Xgs360028fSystemTimeManualDaylightSavingsRecurringDayTo_Object=MibScalar
xgs360028fSystemTimeManualDaylightSavingsRecurringDayTo=_Xgs360028fSystemTimeManualDaylightSavingsRecurringDayTo_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,13),_Xgs360028fSystemTimeManualDaylightSavingsRecurringDayTo_Type())
xgs360028fSystemTimeManualDaylightSavingsRecurringDayTo.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualDaylightSavingsRecurringDayTo.setStatus(_A)
class _Xgs360028fSystemTimeManualDaylightSavingsRecurringWeekTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360028fSystemTimeManualDaylightSavingsRecurringWeekTo_Type.__name__=_B
_Xgs360028fSystemTimeManualDaylightSavingsRecurringWeekTo_Object=MibScalar
xgs360028fSystemTimeManualDaylightSavingsRecurringWeekTo=_Xgs360028fSystemTimeManualDaylightSavingsRecurringWeekTo_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,14),_Xgs360028fSystemTimeManualDaylightSavingsRecurringWeekTo_Type())
xgs360028fSystemTimeManualDaylightSavingsRecurringWeekTo.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualDaylightSavingsRecurringWeekTo.setStatus(_A)
class _Xgs360028fSystemTimeManualDaylightSavingsRecurringMonthTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_Xgs360028fSystemTimeManualDaylightSavingsRecurringMonthTo_Type.__name__=_B
_Xgs360028fSystemTimeManualDaylightSavingsRecurringMonthTo_Object=MibScalar
xgs360028fSystemTimeManualDaylightSavingsRecurringMonthTo=_Xgs360028fSystemTimeManualDaylightSavingsRecurringMonthTo_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,15),_Xgs360028fSystemTimeManualDaylightSavingsRecurringMonthTo_Type())
xgs360028fSystemTimeManualDaylightSavingsRecurringMonthTo.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualDaylightSavingsRecurringMonthTo.setStatus(_A)
_Xgs360028fSystemTimeManualDaylightSavingsRecurringTimeTo_Type=DisplayString
_Xgs360028fSystemTimeManualDaylightSavingsRecurringTimeTo_Object=MibScalar
xgs360028fSystemTimeManualDaylightSavingsRecurringTimeTo=_Xgs360028fSystemTimeManualDaylightSavingsRecurringTimeTo_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,1,16),_Xgs360028fSystemTimeManualDaylightSavingsRecurringTimeTo_Type())
xgs360028fSystemTimeManualDaylightSavingsRecurringTimeTo.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeManualDaylightSavingsRecurringTimeTo.setStatus(_A)
_Xgs360028fSystemTimeNTP_ObjectIdentity=ObjectIdentity
xgs360028fSystemTimeNTP=_Xgs360028fSystemTimeNTP_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,2,2))
_Xgs360028fSystemTimeNTPTable_Object=MibTable
xgs360028fSystemTimeNTPTable=_Xgs360028fSystemTimeNTPTable_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,2,1))
if mibBuilder.loadTexts:xgs360028fSystemTimeNTPTable.setStatus(_A)
_Xgs360028fSystemTimeNTPEntry_Object=MibTableRow
xgs360028fSystemTimeNTPEntry=_Xgs360028fSystemTimeNTPEntry_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,2,1,1))
xgs360028fSystemTimeNTPEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:xgs360028fSystemTimeNTPEntry.setStatus(_A)
class _Xgs360028fSystemTimeNTPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360028fSystemTimeNTPIndex_Type.__name__=_B
_Xgs360028fSystemTimeNTPIndex_Object=MibTableColumn
xgs360028fSystemTimeNTPIndex=_Xgs360028fSystemTimeNTPIndex_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,2,1,1,1),_Xgs360028fSystemTimeNTPIndex_Type())
xgs360028fSystemTimeNTPIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fSystemTimeNTPIndex.setStatus(_A)
class _Xgs360028fSystemTimeNTPServerIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fSystemTimeNTPServerIPType_Type.__name__=_B
_Xgs360028fSystemTimeNTPServerIPType_Object=MibTableColumn
xgs360028fSystemTimeNTPServerIPType=_Xgs360028fSystemTimeNTPServerIPType_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,2,1,1,2),_Xgs360028fSystemTimeNTPServerIPType_Type())
xgs360028fSystemTimeNTPServerIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeNTPServerIPType.setStatus(_A)
_Xgs360028fSystemTimeNTPServer_Type=DisplayString
_Xgs360028fSystemTimeNTPServer_Object=MibTableColumn
xgs360028fSystemTimeNTPServer=_Xgs360028fSystemTimeNTPServer_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,2,1,1,3),_Xgs360028fSystemTimeNTPServer_Type())
xgs360028fSystemTimeNTPServer.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeNTPServer.setStatus(_A)
class _Xgs360028fSystemTimeNTPCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360028fSystemTimeNTPCurrentMode_Type.__name__=_B
_Xgs360028fSystemTimeNTPCurrentMode_Object=MibTableColumn
xgs360028fSystemTimeNTPCurrentMode=_Xgs360028fSystemTimeNTPCurrentMode_Object((1,3,6,1,4,1,890,1,5,8,78,1,2,2,1,1,4),_Xgs360028fSystemTimeNTPCurrentMode_Type())
xgs360028fSystemTimeNTPCurrentMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemTimeNTPCurrentMode.setStatus(_A)
_Xgs360028fSystemAccount_ObjectIdentity=ObjectIdentity
xgs360028fSystemAccount=_Xgs360028fSystemAccount_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,3))
_Xgs360028fSystemAccountUsers_ObjectIdentity=ObjectIdentity
xgs360028fSystemAccountUsers=_Xgs360028fSystemAccountUsers_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,3,1))
class _Xgs360028fSystemAccountUserCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fSystemAccountUserCreate_Type.__name__=_B
_Xgs360028fSystemAccountUserCreate_Object=MibScalar
xgs360028fSystemAccountUserCreate=_Xgs360028fSystemAccountUserCreate_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,1,1),_Xgs360028fSystemAccountUserCreate_Type())
xgs360028fSystemAccountUserCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemAccountUserCreate.setStatus(_A)
_Xgs360028fSystemAccountUsersTable_Object=MibTable
xgs360028fSystemAccountUsersTable=_Xgs360028fSystemAccountUsersTable_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,1,2))
if mibBuilder.loadTexts:xgs360028fSystemAccountUsersTable.setStatus(_A)
_Xgs360028fSystemAccountUsersEntry_Object=MibTableRow
xgs360028fSystemAccountUsersEntry=_Xgs360028fSystemAccountUsersEntry_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,1,2,1))
xgs360028fSystemAccountUsersEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:xgs360028fSystemAccountUsersEntry.setStatus(_A)
class _Xgs360028fUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_Xgs360028fUserIndex_Type.__name__=_B
_Xgs360028fUserIndex_Object=MibTableColumn
xgs360028fUserIndex=_Xgs360028fUserIndex_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,1,2,1,1),_Xgs360028fUserIndex_Type())
xgs360028fUserIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fUserIndex.setStatus(_A)
class _Xgs360028fUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Xgs360028fUserName_Type.__name__=_G
_Xgs360028fUserName_Object=MibTableColumn
xgs360028fUserName=_Xgs360028fUserName_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,1,2,1,2),_Xgs360028fUserName_Type())
xgs360028fUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fUserName.setStatus(_A)
class _Xgs360028fPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Xgs360028fPassword_Type.__name__=_G
_Xgs360028fPassword_Object=MibTableColumn
xgs360028fPassword=_Xgs360028fPassword_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,1,2,1,3),_Xgs360028fPassword_Type())
xgs360028fPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPassword.setStatus(_A)
class _Xgs360028fUserPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fUserPrivilegeLevel_Type.__name__=_B
_Xgs360028fUserPrivilegeLevel_Object=MibTableColumn
xgs360028fUserPrivilegeLevel=_Xgs360028fUserPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,1,2,1,4),_Xgs360028fUserPrivilegeLevel_Type())
xgs360028fUserPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fUserPrivilegeLevel.setStatus(_A)
class _Xgs360028fAccountUserRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360028fAccountUserRowStatus_Type.__name__=_B
_Xgs360028fAccountUserRowStatus_Object=MibTableColumn
xgs360028fAccountUserRowStatus=_Xgs360028fAccountUserRowStatus_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,1,2,1,5),_Xgs360028fAccountUserRowStatus_Type())
xgs360028fAccountUserRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fAccountUserRowStatus.setStatus(_A)
_Xgs360028fSystemAccountPrivilegeLevel_ObjectIdentity=ObjectIdentity
xgs360028fSystemAccountPrivilegeLevel=_Xgs360028fSystemAccountPrivilegeLevel_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,3,2))
class _Xgs360028fAccountPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fAccountPrivilegeLevel_Type.__name__=_B
_Xgs360028fAccountPrivilegeLevel_Object=MibScalar
xgs360028fAccountPrivilegeLevel=_Xgs360028fAccountPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,1),_Xgs360028fAccountPrivilegeLevel_Type())
xgs360028fAccountPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fAccountPrivilegeLevel.setStatus(_A)
class _Xgs360028fAggregationPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fAggregationPrivilegeLevel_Type.__name__=_B
_Xgs360028fAggregationPrivilegeLevel_Object=MibScalar
xgs360028fAggregationPrivilegeLevel=_Xgs360028fAggregationPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,2),_Xgs360028fAggregationPrivilegeLevel_Type())
xgs360028fAggregationPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fAggregationPrivilegeLevel.setStatus(_A)
class _Xgs360028fDiagnosticsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fDiagnosticsPrivilegeLevel_Type.__name__=_B
_Xgs360028fDiagnosticsPrivilegeLevel_Object=MibScalar
xgs360028fDiagnosticsPrivilegeLevel=_Xgs360028fDiagnosticsPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,3),_Xgs360028fDiagnosticsPrivilegeLevel_Type())
xgs360028fDiagnosticsPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fDiagnosticsPrivilegeLevel.setStatus(_A)
class _Xgs360028fEPSPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fEPSPrivilegeLevel_Type.__name__=_B
_Xgs360028fEPSPrivilegeLevel_Object=MibScalar
xgs360028fEPSPrivilegeLevel=_Xgs360028fEPSPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,5),_Xgs360028fEPSPrivilegeLevel_Type())
xgs360028fEPSPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fEPSPrivilegeLevel.setStatus(_A)
class _Xgs360028fERPSPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fERPSPrivilegeLevel_Type.__name__=_B
_Xgs360028fERPSPrivilegeLevel_Object=MibScalar
xgs360028fERPSPrivilegeLevel=_Xgs360028fERPSPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,6),_Xgs360028fERPSPrivilegeLevel_Type())
xgs360028fERPSPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSPrivilegeLevel.setStatus(_A)
class _Xgs360028fETHLinkOAMPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fETHLinkOAMPrivilegeLevel_Type.__name__=_B
_Xgs360028fETHLinkOAMPrivilegeLevel_Object=MibScalar
xgs360028fETHLinkOAMPrivilegeLevel=_Xgs360028fETHLinkOAMPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,7),_Xgs360028fETHLinkOAMPrivilegeLevel_Type())
xgs360028fETHLinkOAMPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fETHLinkOAMPrivilegeLevel.setStatus(_A)
class _Xgs360028fEVCPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fEVCPrivilegeLevel_Type.__name__=_B
_Xgs360028fEVCPrivilegeLevel_Object=MibScalar
xgs360028fEVCPrivilegeLevel=_Xgs360028fEVCPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,8),_Xgs360028fEVCPrivilegeLevel_Type())
xgs360028fEVCPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fEVCPrivilegeLevel.setStatus(_A)
class _Xgs360028fGARPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fGARPPrivilegeLevel_Type.__name__=_B
_Xgs360028fGARPPrivilegeLevel_Object=MibScalar
xgs360028fGARPPrivilegeLevel=_Xgs360028fGARPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,10),_Xgs360028fGARPPrivilegeLevel_Type())
xgs360028fGARPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fGARPPrivilegeLevel.setStatus(_A)
class _Xgs360028fGVRPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fGVRPPrivilegeLevel_Type.__name__=_B
_Xgs360028fGVRPPrivilegeLevel_Object=MibScalar
xgs360028fGVRPPrivilegeLevel=_Xgs360028fGVRPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,11),_Xgs360028fGVRPPrivilegeLevel_Type())
xgs360028fGVRPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fGVRPPrivilegeLevel.setStatus(_A)
class _Xgs360028fIPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fIPPrivilegeLevel_Type.__name__=_B
_Xgs360028fIPPrivilegeLevel_Object=MibScalar
xgs360028fIPPrivilegeLevel=_Xgs360028fIPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,12),_Xgs360028fIPPrivilegeLevel_Type())
xgs360028fIPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPPrivilegeLevel.setStatus(_A)
class _Xgs360028fIPMCSnoopingPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fIPMCSnoopingPrivilegeLevel_Type.__name__=_B
_Xgs360028fIPMCSnoopingPrivilegeLevel_Object=MibScalar
xgs360028fIPMCSnoopingPrivilegeLevel=_Xgs360028fIPMCSnoopingPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,13),_Xgs360028fIPMCSnoopingPrivilegeLevel_Type())
xgs360028fIPMCSnoopingPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPMCSnoopingPrivilegeLevel.setStatus(_A)
class _Xgs360028fLACPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fLACPPrivilegeLevel_Type.__name__=_B
_Xgs360028fLACPPrivilegeLevel_Object=MibScalar
xgs360028fLACPPrivilegeLevel=_Xgs360028fLACPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,14),_Xgs360028fLACPPrivilegeLevel_Type())
xgs360028fLACPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fLACPPrivilegeLevel.setStatus(_A)
class _Xgs360028fLLDPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fLLDPPrivilegeLevel_Type.__name__=_B
_Xgs360028fLLDPPrivilegeLevel_Object=MibScalar
xgs360028fLLDPPrivilegeLevel=_Xgs360028fLLDPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,15),_Xgs360028fLLDPPrivilegeLevel_Type())
xgs360028fLLDPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fLLDPPrivilegeLevel.setStatus(_A)
class _Xgs360028fLLDPMEDPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fLLDPMEDPrivilegeLevel_Type.__name__=_B
_Xgs360028fLLDPMEDPrivilegeLevel_Object=MibScalar
xgs360028fLLDPMEDPrivilegeLevel=_Xgs360028fLLDPMEDPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,16),_Xgs360028fLLDPMEDPrivilegeLevel_Type())
xgs360028fLLDPMEDPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fLLDPMEDPrivilegeLevel.setStatus(_A)
class _Xgs360028fLoopProtectPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fLoopProtectPrivilegeLevel_Type.__name__=_B
_Xgs360028fLoopProtectPrivilegeLevel_Object=MibScalar
xgs360028fLoopProtectPrivilegeLevel=_Xgs360028fLoopProtectPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,17),_Xgs360028fLoopProtectPrivilegeLevel_Type())
xgs360028fLoopProtectPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fLoopProtectPrivilegeLevel.setStatus(_A)
class _Xgs360028fMACTablePrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fMACTablePrivilegeLevel_Type.__name__=_B
_Xgs360028fMACTablePrivilegeLevel_Object=MibScalar
xgs360028fMACTablePrivilegeLevel=_Xgs360028fMACTablePrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,18),_Xgs360028fMACTablePrivilegeLevel_Type())
xgs360028fMACTablePrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMACTablePrivilegeLevel.setStatus(_A)
class _Xgs360028fMEPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fMEPPrivilegeLevel_Type.__name__=_B
_Xgs360028fMEPPrivilegeLevel_Object=MibScalar
xgs360028fMEPPrivilegeLevel=_Xgs360028fMEPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,20),_Xgs360028fMEPPrivilegeLevel_Type())
xgs360028fMEPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMEPPrivilegeLevel.setStatus(_A)
class _Xgs360028fMRSTPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fMRSTPPrivilegeLevel_Type.__name__=_B
_Xgs360028fMRSTPPrivilegeLevel_Object=MibScalar
xgs360028fMRSTPPrivilegeLevel=_Xgs360028fMRSTPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,21),_Xgs360028fMRSTPPrivilegeLevel_Type())
xgs360028fMRSTPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMRSTPPrivilegeLevel.setStatus(_A)
class _Xgs360028fMVRPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fMVRPrivilegeLevel_Type.__name__=_B
_Xgs360028fMVRPrivilegeLevel_Object=MibScalar
xgs360028fMVRPrivilegeLevel=_Xgs360028fMVRPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,22),_Xgs360028fMVRPrivilegeLevel_Type())
xgs360028fMVRPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMVRPrivilegeLevel.setStatus(_A)
class _Xgs360028fMaintenancePrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fMaintenancePrivilegeLevel_Type.__name__=_B
_Xgs360028fMaintenancePrivilegeLevel_Object=MibScalar
xgs360028fMaintenancePrivilegeLevel=_Xgs360028fMaintenancePrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,24),_Xgs360028fMaintenancePrivilegeLevel_Type())
xgs360028fMaintenancePrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMaintenancePrivilegeLevel.setStatus(_A)
class _Xgs360028fMirroringPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fMirroringPrivilegeLevel_Type.__name__=_B
_Xgs360028fMirroringPrivilegeLevel_Object=MibScalar
xgs360028fMirroringPrivilegeLevel=_Xgs360028fMirroringPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,25),_Xgs360028fMirroringPrivilegeLevel_Type())
xgs360028fMirroringPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMirroringPrivilegeLevel.setStatus(_A)
class _Xgs360028fPTPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fPTPPrivilegeLevel_Type.__name__=_B
_Xgs360028fPTPPrivilegeLevel_Object=MibScalar
xgs360028fPTPPrivilegeLevel=_Xgs360028fPTPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,26),_Xgs360028fPTPPrivilegeLevel_Type())
xgs360028fPTPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPTPPrivilegeLevel.setStatus(_A)
class _Xgs360028fPortsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fPortsPrivilegeLevel_Type.__name__=_B
_Xgs360028fPortsPrivilegeLevel_Object=MibScalar
xgs360028fPortsPrivilegeLevel=_Xgs360028fPortsPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,27),_Xgs360028fPortsPrivilegeLevel_Type())
xgs360028fPortsPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortsPrivilegeLevel.setStatus(_A)
class _Xgs360028fPrivateVLANsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fPrivateVLANsPrivilegeLevel_Type.__name__=_B
_Xgs360028fPrivateVLANsPrivilegeLevel_Object=MibScalar
xgs360028fPrivateVLANsPrivilegeLevel=_Xgs360028fPrivateVLANsPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,28),_Xgs360028fPrivateVLANsPrivilegeLevel_Type())
xgs360028fPrivateVLANsPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPrivateVLANsPrivilegeLevel.setStatus(_A)
class _Xgs360028fQoSPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fQoSPrivilegeLevel_Type.__name__=_B
_Xgs360028fQoSPrivilegeLevel_Object=MibScalar
xgs360028fQoSPrivilegeLevel=_Xgs360028fQoSPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,29),_Xgs360028fQoSPrivilegeLevel_Type())
xgs360028fQoSPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fQoSPrivilegeLevel.setStatus(_A)
class _Xgs360028fSMTPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fSMTPPrivilegeLevel_Type.__name__=_B
_Xgs360028fSMTPPrivilegeLevel_Object=MibScalar
xgs360028fSMTPPrivilegeLevel=_Xgs360028fSMTPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,31),_Xgs360028fSMTPPrivilegeLevel_Type())
xgs360028fSMTPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSMTPPrivilegeLevel.setStatus(_A)
class _Xgs360028fSNMPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fSNMPPrivilegeLevel_Type.__name__=_B
_Xgs360028fSNMPPrivilegeLevel_Object=MibScalar
xgs360028fSNMPPrivilegeLevel=_Xgs360028fSNMPPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,32),_Xgs360028fSNMPPrivilegeLevel_Type())
xgs360028fSNMPPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSNMPPrivilegeLevel.setStatus(_A)
class _Xgs360028fSecurityPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fSecurityPrivilegeLevel_Type.__name__=_B
_Xgs360028fSecurityPrivilegeLevel_Object=MibScalar
xgs360028fSecurityPrivilegeLevel=_Xgs360028fSecurityPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,33),_Xgs360028fSecurityPrivilegeLevel_Type())
xgs360028fSecurityPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSecurityPrivilegeLevel.setStatus(_A)
class _Xgs360028fSpanningTreePrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fSpanningTreePrivilegeLevel_Type.__name__=_B
_Xgs360028fSpanningTreePrivilegeLevel_Object=MibScalar
xgs360028fSpanningTreePrivilegeLevel=_Xgs360028fSpanningTreePrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,35),_Xgs360028fSpanningTreePrivilegeLevel_Type())
xgs360028fSpanningTreePrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSpanningTreePrivilegeLevel.setStatus(_A)
class _Xgs360028fSystemPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fSystemPrivilegeLevel_Type.__name__=_B
_Xgs360028fSystemPrivilegeLevel_Object=MibScalar
xgs360028fSystemPrivilegeLevel=_Xgs360028fSystemPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,36),_Xgs360028fSystemPrivilegeLevel_Type())
xgs360028fSystemPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSystemPrivilegeLevel.setStatus(_A)
class _Xgs360028fTrapEventPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fTrapEventPrivilegeLevel_Type.__name__=_B
_Xgs360028fTrapEventPrivilegeLevel_Object=MibScalar
xgs360028fTrapEventPrivilegeLevel=_Xgs360028fTrapEventPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,37),_Xgs360028fTrapEventPrivilegeLevel_Type())
xgs360028fTrapEventPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventPrivilegeLevel.setStatus(_A)
class _Xgs360028fVCLPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fVCLPrivilegeLevel_Type.__name__=_B
_Xgs360028fVCLPrivilegeLevel_Object=MibScalar
xgs360028fVCLPrivilegeLevel=_Xgs360028fVCLPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,39),_Xgs360028fVCLPrivilegeLevel_Type())
xgs360028fVCLPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fVCLPrivilegeLevel.setStatus(_A)
class _Xgs360028fVLANTranslationPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fVLANTranslationPrivilegeLevel_Type.__name__=_B
_Xgs360028fVLANTranslationPrivilegeLevel_Object=MibScalar
xgs360028fVLANTranslationPrivilegeLevel=_Xgs360028fVLANTranslationPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,40),_Xgs360028fVLANTranslationPrivilegeLevel_Type())
xgs360028fVLANTranslationPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fVLANTranslationPrivilegeLevel.setStatus(_A)
class _Xgs360028fVLANsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Xgs360028fVLANsPrivilegeLevel_Type.__name__=_B
_Xgs360028fVLANsPrivilegeLevel_Object=MibScalar
xgs360028fVLANsPrivilegeLevel=_Xgs360028fVLANsPrivilegeLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,3,2,41),_Xgs360028fVLANsPrivilegeLevel_Type())
xgs360028fVLANsPrivilegeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fVLANsPrivilegeLevel.setStatus(_A)
_Xgs360028fIP_ObjectIdentity=ObjectIdentity
xgs360028fIP=_Xgs360028fIP_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,4))
_Xgs360028fIPv4_ObjectIdentity=ObjectIdentity
xgs360028fIPv4=_Xgs360028fIPv4_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,4,1))
_Xgs360028fIPv4Configured_ObjectIdentity=ObjectIdentity
xgs360028fIPv4Configured=_Xgs360028fIPv4Configured_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,4,1,1))
class _Xgs360028fIpv4DHCPClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fIpv4DHCPClient_Type.__name__=_B
_Xgs360028fIpv4DHCPClient_Object=MibScalar
xgs360028fIpv4DHCPClient=_Xgs360028fIpv4DHCPClient_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,1,1,1),_Xgs360028fIpv4DHCPClient_Type())
xgs360028fIpv4DHCPClient.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIpv4DHCPClient.setStatus(_A)
_Xgs360028fIPv4Address_Type=IpAddress
_Xgs360028fIPv4Address_Object=MibScalar
xgs360028fIPv4Address=_Xgs360028fIPv4Address_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,1,1,2),_Xgs360028fIPv4Address_Type())
xgs360028fIPv4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPv4Address.setStatus(_A)
_Xgs360028fIPv4Mask_Type=IpAddress
_Xgs360028fIPv4Mask_Object=MibScalar
xgs360028fIPv4Mask=_Xgs360028fIPv4Mask_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,1,1,3),_Xgs360028fIPv4Mask_Type())
xgs360028fIPv4Mask.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPv4Mask.setStatus(_A)
_Xgs360028fIPv4Router_Type=IpAddress
_Xgs360028fIPv4Router_Object=MibScalar
xgs360028fIPv4Router=_Xgs360028fIPv4Router_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,1,1,4),_Xgs360028fIPv4Router_Type())
xgs360028fIPv4Router.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPv4Router.setStatus(_A)
class _Xgs360028fIPv4VLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Xgs360028fIPv4VLANId_Type.__name__=_B
_Xgs360028fIPv4VLANId_Object=MibScalar
xgs360028fIPv4VLANId=_Xgs360028fIPv4VLANId_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,1,1,5),_Xgs360028fIPv4VLANId_Type())
xgs360028fIPv4VLANId.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPv4VLANId.setStatus(_A)
_Xgs360028fIPv4DNSServer_Type=IpAddress
_Xgs360028fIPv4DNSServer_Object=MibScalar
xgs360028fIPv4DNSServer=_Xgs360028fIPv4DNSServer_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,1,1,6),_Xgs360028fIPv4DNSServer_Type())
xgs360028fIPv4DNSServer.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPv4DNSServer.setStatus(_A)
class _Xgs360028fIPv4DNSProxy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fIPv4DNSProxy_Type.__name__=_B
_Xgs360028fIPv4DNSProxy_Object=MibScalar
xgs360028fIPv4DNSProxy=_Xgs360028fIPv4DNSProxy_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,1,1,7),_Xgs360028fIPv4DNSProxy_Type())
xgs360028fIPv4DNSProxy.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPv4DNSProxy.setStatus(_A)
_Xgs360028fIPv4Current_ObjectIdentity=ObjectIdentity
xgs360028fIPv4Current=_Xgs360028fIPv4Current_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,4,1,2))
class _Xgs360028fIpv4CurrentDHCPClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fIpv4CurrentDHCPClient_Type.__name__=_B
_Xgs360028fIpv4CurrentDHCPClient_Object=MibScalar
xgs360028fIpv4CurrentDHCPClient=_Xgs360028fIpv4CurrentDHCPClient_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,1,2,1),_Xgs360028fIpv4CurrentDHCPClient_Type())
xgs360028fIpv4CurrentDHCPClient.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIpv4CurrentDHCPClient.setStatus(_A)
_Xgs360028fIPv4CurrentAddress_Type=IpAddress
_Xgs360028fIPv4CurrentAddress_Object=MibScalar
xgs360028fIPv4CurrentAddress=_Xgs360028fIPv4CurrentAddress_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,1,2,2),_Xgs360028fIPv4CurrentAddress_Type())
xgs360028fIPv4CurrentAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fIPv4CurrentAddress.setStatus(_A)
_Xgs360028fIPv4CurrentMask_Type=IpAddress
_Xgs360028fIPv4CurrentMask_Object=MibScalar
xgs360028fIPv4CurrentMask=_Xgs360028fIPv4CurrentMask_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,1,2,3),_Xgs360028fIPv4CurrentMask_Type())
xgs360028fIPv4CurrentMask.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fIPv4CurrentMask.setStatus(_A)
_Xgs360028fIPv4CurrentRouter_Type=IpAddress
_Xgs360028fIPv4CurrentRouter_Object=MibScalar
xgs360028fIPv4CurrentRouter=_Xgs360028fIPv4CurrentRouter_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,1,2,4),_Xgs360028fIPv4CurrentRouter_Type())
xgs360028fIPv4CurrentRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fIPv4CurrentRouter.setStatus(_A)
class _Xgs360028fIPv4CurrentVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Xgs360028fIPv4CurrentVLANId_Type.__name__=_B
_Xgs360028fIPv4CurrentVLANId_Object=MibScalar
xgs360028fIPv4CurrentVLANId=_Xgs360028fIPv4CurrentVLANId_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,1,2,5),_Xgs360028fIPv4CurrentVLANId_Type())
xgs360028fIPv4CurrentVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fIPv4CurrentVLANId.setStatus(_A)
_Xgs360028fIPv4CurrentDNSServer_Type=IpAddress
_Xgs360028fIPv4CurrentDNSServer_Object=MibScalar
xgs360028fIPv4CurrentDNSServer=_Xgs360028fIPv4CurrentDNSServer_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,1,2,6),_Xgs360028fIPv4CurrentDNSServer_Type())
xgs360028fIPv4CurrentDNSServer.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fIPv4CurrentDNSServer.setStatus(_A)
_Xgs360028fIPv6_ObjectIdentity=ObjectIdentity
xgs360028fIPv6=_Xgs360028fIPv6_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,4,2))
_Xgs360028fIPv6Configured_ObjectIdentity=ObjectIdentity
xgs360028fIPv6Configured=_Xgs360028fIPv6Configured_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,4,2,1))
class _Xgs360028fIpv6AutoConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fIpv6AutoConfiguration_Type.__name__=_B
_Xgs360028fIpv6AutoConfiguration_Object=MibScalar
xgs360028fIpv6AutoConfiguration=_Xgs360028fIpv6AutoConfiguration_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,2,1,1),_Xgs360028fIpv6AutoConfiguration_Type())
xgs360028fIpv6AutoConfiguration.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIpv6AutoConfiguration.setStatus(_A)
class _Xgs360028fIpv6Address_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Xgs360028fIpv6Address_Type.__name__=_G
_Xgs360028fIpv6Address_Object=MibScalar
xgs360028fIpv6Address=_Xgs360028fIpv6Address_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,2,1,2),_Xgs360028fIpv6Address_Type())
xgs360028fIpv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIpv6Address.setStatus(_A)
class _Xgs360028fIpv6Prefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Xgs360028fIpv6Prefix_Type.__name__=_B
_Xgs360028fIpv6Prefix_Object=MibScalar
xgs360028fIpv6Prefix=_Xgs360028fIpv6Prefix_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,2,1,3),_Xgs360028fIpv6Prefix_Type())
xgs360028fIpv6Prefix.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIpv6Prefix.setStatus(_A)
class _Xgs360028fIpv6Router_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Xgs360028fIpv6Router_Type.__name__=_G
_Xgs360028fIpv6Router_Object=MibScalar
xgs360028fIpv6Router=_Xgs360028fIpv6Router_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,2,1,4),_Xgs360028fIpv6Router_Type())
xgs360028fIpv6Router.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIpv6Router.setStatus(_A)
_Xgs360028fIPv6Current_ObjectIdentity=ObjectIdentity
xgs360028fIPv6Current=_Xgs360028fIPv6Current_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,4,2,2))
class _Xgs360028fIpv6CurrentAutoConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fIpv6CurrentAutoConfiguration_Type.__name__=_B
_Xgs360028fIpv6CurrentAutoConfiguration_Object=MibScalar
xgs360028fIpv6CurrentAutoConfiguration=_Xgs360028fIpv6CurrentAutoConfiguration_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,2,2,1),_Xgs360028fIpv6CurrentAutoConfiguration_Type())
xgs360028fIpv6CurrentAutoConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fIpv6CurrentAutoConfiguration.setStatus(_A)
class _Xgs360028fIpv6CurrentAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Xgs360028fIpv6CurrentAddress_Type.__name__=_G
_Xgs360028fIpv6CurrentAddress_Object=MibScalar
xgs360028fIpv6CurrentAddress=_Xgs360028fIpv6CurrentAddress_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,2,2,2),_Xgs360028fIpv6CurrentAddress_Type())
xgs360028fIpv6CurrentAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fIpv6CurrentAddress.setStatus(_A)
class _Xgs360028fIpv6CurrentLinkLocalAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Xgs360028fIpv6CurrentLinkLocalAddress_Type.__name__=_G
_Xgs360028fIpv6CurrentLinkLocalAddress_Object=MibScalar
xgs360028fIpv6CurrentLinkLocalAddress=_Xgs360028fIpv6CurrentLinkLocalAddress_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,2,2,3),_Xgs360028fIpv6CurrentLinkLocalAddress_Type())
xgs360028fIpv6CurrentLinkLocalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fIpv6CurrentLinkLocalAddress.setStatus(_A)
class _Xgs360028fIpv6CurrentPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Xgs360028fIpv6CurrentPrefix_Type.__name__=_B
_Xgs360028fIpv6CurrentPrefix_Object=MibScalar
xgs360028fIpv6CurrentPrefix=_Xgs360028fIpv6CurrentPrefix_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,2,2,4),_Xgs360028fIpv6CurrentPrefix_Type())
xgs360028fIpv6CurrentPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fIpv6CurrentPrefix.setStatus(_A)
class _Xgs360028fIpv6CurrentRouter_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Xgs360028fIpv6CurrentRouter_Type.__name__=_G
_Xgs360028fIpv6CurrentRouter_Object=MibScalar
xgs360028fIpv6CurrentRouter=_Xgs360028fIpv6CurrentRouter_Object((1,3,6,1,4,1,890,1,5,8,78,1,4,2,2,5),_Xgs360028fIpv6CurrentRouter_Type())
xgs360028fIpv6CurrentRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fIpv6CurrentRouter.setStatus(_A)
_Xgs360028fSyslog_ObjectIdentity=ObjectIdentity
xgs360028fSyslog=_Xgs360028fSyslog_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,5))
_Xgs360028fSyslogConf_ObjectIdentity=ObjectIdentity
xgs360028fSyslogConf=_Xgs360028fSyslogConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,5,1))
class _Xgs360028fServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fServerMode_Type.__name__=_B
_Xgs360028fServerMode_Object=MibScalar
xgs360028fServerMode=_Xgs360028fServerMode_Object((1,3,6,1,4,1,890,1,5,8,78,1,5,1,1),_Xgs360028fServerMode_Type())
xgs360028fServerMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fServerMode.setStatus(_A)
_Xgs360028fServerAddress1_Type=IpAddress
_Xgs360028fServerAddress1_Object=MibScalar
xgs360028fServerAddress1=_Xgs360028fServerAddress1_Object((1,3,6,1,4,1,890,1,5,8,78,1,5,1,2),_Xgs360028fServerAddress1_Type())
xgs360028fServerAddress1.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fServerAddress1.setStatus(_A)
_Xgs360028fServerAddress2_Type=IpAddress
_Xgs360028fServerAddress2_Object=MibScalar
xgs360028fServerAddress2=_Xgs360028fServerAddress2_Object((1,3,6,1,4,1,890,1,5,8,78,1,5,1,3),_Xgs360028fServerAddress2_Type())
xgs360028fServerAddress2.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fServerAddress2.setStatus(_A)
class _Xgs360028fSyslogLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fSyslogLevel_Type.__name__=_B
_Xgs360028fSyslogLevel_Object=MibScalar
xgs360028fSyslogLevel=_Xgs360028fSyslogLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,5,1,4),_Xgs360028fSyslogLevel_Type())
xgs360028fSyslogLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSyslogLevel.setStatus(_A)
_Xgs360028fSyslogDetailedInfo_ObjectIdentity=ObjectIdentity
xgs360028fSyslogDetailedInfo=_Xgs360028fSyslogDetailedInfo_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,5,2))
class _Xgs360028fSyslogDetailedInfoClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fSyslogDetailedInfoClear_Type.__name__=_B
_Xgs360028fSyslogDetailedInfoClear_Object=MibScalar
xgs360028fSyslogDetailedInfoClear=_Xgs360028fSyslogDetailedInfoClear_Object((1,3,6,1,4,1,890,1,5,8,78,1,5,2,1),_Xgs360028fSyslogDetailedInfoClear_Type())
xgs360028fSyslogDetailedInfoClear.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSyslogDetailedInfoClear.setStatus(_A)
_Xgs360028fSyslogDetailedInfoTable_Object=MibTable
xgs360028fSyslogDetailedInfoTable=_Xgs360028fSyslogDetailedInfoTable_Object((1,3,6,1,4,1,890,1,5,8,78,1,5,2,2))
if mibBuilder.loadTexts:xgs360028fSyslogDetailedInfoTable.setStatus(_A)
_Xgs360028fSyslogDetailedInfoEntry_Object=MibTableRow
xgs360028fSyslogDetailedInfoEntry=_Xgs360028fSyslogDetailedInfoEntry_Object((1,3,6,1,4,1,890,1,5,8,78,1,5,2,2,1))
xgs360028fSyslogDetailedInfoEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:xgs360028fSyslogDetailedInfoEntry.setStatus(_A)
class _Xgs360028fSyslogDetailedInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Xgs360028fSyslogDetailedInfoIndex_Type.__name__=_B
_Xgs360028fSyslogDetailedInfoIndex_Object=MibTableColumn
xgs360028fSyslogDetailedInfoIndex=_Xgs360028fSyslogDetailedInfoIndex_Object((1,3,6,1,4,1,890,1,5,8,78,1,5,2,2,1,1),_Xgs360028fSyslogDetailedInfoIndex_Type())
xgs360028fSyslogDetailedInfoIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fSyslogDetailedInfoIndex.setStatus(_A)
_Xgs360028fSyslogDetailedInfoLevel_Type=DisplayString
_Xgs360028fSyslogDetailedInfoLevel_Object=MibTableColumn
xgs360028fSyslogDetailedInfoLevel=_Xgs360028fSyslogDetailedInfoLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,5,2,2,1,2),_Xgs360028fSyslogDetailedInfoLevel_Type())
xgs360028fSyslogDetailedInfoLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSyslogDetailedInfoLevel.setStatus(_A)
class _Xgs360028fSyslogDetailedInfoTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_Xgs360028fSyslogDetailedInfoTime_Type.__name__=_G
_Xgs360028fSyslogDetailedInfoTime_Object=MibTableColumn
xgs360028fSyslogDetailedInfoTime=_Xgs360028fSyslogDetailedInfoTime_Object((1,3,6,1,4,1,890,1,5,8,78,1,5,2,2,1,3),_Xgs360028fSyslogDetailedInfoTime_Type())
xgs360028fSyslogDetailedInfoTime.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSyslogDetailedInfoTime.setStatus(_A)
_Xgs360028fSyslogDetailedInfoMessage_Type=DisplayString
_Xgs360028fSyslogDetailedInfoMessage_Object=MibTableColumn
xgs360028fSyslogDetailedInfoMessage=_Xgs360028fSyslogDetailedInfoMessage_Object((1,3,6,1,4,1,890,1,5,8,78,1,5,2,2,1,4),_Xgs360028fSyslogDetailedInfoMessage_Type())
xgs360028fSyslogDetailedInfoMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSyslogDetailedInfoMessage.setStatus(_A)
_Xgs360028fSnmp_ObjectIdentity=ObjectIdentity
xgs360028fSnmp=_Xgs360028fSnmp_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,6))
_Xgs360028fSnmpConf_ObjectIdentity=ObjectIdentity
xgs360028fSnmpConf=_Xgs360028fSnmpConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,1,6,1))
_Xgs360028fGetCommunity_Type=DisplayString
_Xgs360028fGetCommunity_Object=MibScalar
xgs360028fGetCommunity=_Xgs360028fGetCommunity_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,1),_Xgs360028fGetCommunity_Type())
xgs360028fGetCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fGetCommunity.setStatus(_A)
class _Xgs360028fSetCommunityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fSetCommunityMode_Type.__name__=_B
_Xgs360028fSetCommunityMode_Object=MibScalar
xgs360028fSetCommunityMode=_Xgs360028fSetCommunityMode_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,2),_Xgs360028fSetCommunityMode_Type())
xgs360028fSetCommunityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSetCommunityMode.setStatus(_A)
_Xgs360028fSetCommunity_Type=DisplayString
_Xgs360028fSetCommunity_Object=MibScalar
xgs360028fSetCommunity=_Xgs360028fSetCommunity_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,3),_Xgs360028fSetCommunity_Type())
xgs360028fSetCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSetCommunity.setStatus(_A)
_Xgs360028fTrapHostConfTable_Object=MibTable
xgs360028fTrapHostConfTable=_Xgs360028fTrapHostConfTable_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,4))
if mibBuilder.loadTexts:xgs360028fTrapHostConfTable.setStatus(_A)
_Xgs360028fTrapHostConfEntry_Object=MibTableRow
xgs360028fTrapHostConfEntry=_Xgs360028fTrapHostConfEntry_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,4,1))
xgs360028fTrapHostConfEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:xgs360028fTrapHostConfEntry.setStatus(_A)
class _Xgs360028fTrapHostConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Xgs360028fTrapHostConfIndex_Type.__name__=_B
_Xgs360028fTrapHostConfIndex_Object=MibTableColumn
xgs360028fTrapHostConfIndex=_Xgs360028fTrapHostConfIndex_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,4,1,1),_Xgs360028fTrapHostConfIndex_Type())
xgs360028fTrapHostConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fTrapHostConfIndex.setStatus(_A)
class _Xgs360028fTrapHostConfVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,3))
_Xgs360028fTrapHostConfVersion_Type.__name__=_B
_Xgs360028fTrapHostConfVersion_Object=MibTableColumn
xgs360028fTrapHostConfVersion=_Xgs360028fTrapHostConfVersion_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,4,1,2),_Xgs360028fTrapHostConfVersion_Type())
xgs360028fTrapHostConfVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapHostConfVersion.setStatus(_A)
class _Xgs360028fTrapHostConfIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,4),ValueRangeConstraint(6,6))
_Xgs360028fTrapHostConfIPType_Type.__name__=_B
_Xgs360028fTrapHostConfIPType_Object=MibTableColumn
xgs360028fTrapHostConfIPType=_Xgs360028fTrapHostConfIPType_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,4,1,3),_Xgs360028fTrapHostConfIPType_Type())
xgs360028fTrapHostConfIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapHostConfIPType.setStatus(_A)
_Xgs360028fTrapHostConfIP_Type=DisplayString
_Xgs360028fTrapHostConfIP_Object=MibTableColumn
xgs360028fTrapHostConfIP=_Xgs360028fTrapHostConfIP_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,4,1,4),_Xgs360028fTrapHostConfIP_Type())
xgs360028fTrapHostConfIP.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapHostConfIP.setStatus(_A)
class _Xgs360028fTrapHostConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Xgs360028fTrapHostConfPort_Type.__name__=_B
_Xgs360028fTrapHostConfPort_Object=MibTableColumn
xgs360028fTrapHostConfPort=_Xgs360028fTrapHostConfPort_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,4,1,5),_Xgs360028fTrapHostConfPort_Type())
xgs360028fTrapHostConfPort.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapHostConfPort.setStatus(_A)
class _Xgs360028fTrapHostConfCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Xgs360028fTrapHostConfCommunity_Type.__name__=_G
_Xgs360028fTrapHostConfCommunity_Object=MibTableColumn
xgs360028fTrapHostConfCommunity=_Xgs360028fTrapHostConfCommunity_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,4,1,6),_Xgs360028fTrapHostConfCommunity_Type())
xgs360028fTrapHostConfCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapHostConfCommunity.setStatus(_A)
class _Xgs360028fTrapHostConfSeverityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapHostConfSeverityLevel_Type.__name__=_B
_Xgs360028fTrapHostConfSeverityLevel_Object=MibTableColumn
xgs360028fTrapHostConfSeverityLevel=_Xgs360028fTrapHostConfSeverityLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,4,1,7),_Xgs360028fTrapHostConfSeverityLevel_Type())
xgs360028fTrapHostConfSeverityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapHostConfSeverityLevel.setStatus(_A)
class _Xgs360028fTrapHostConfSecurityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Xgs360028fTrapHostConfSecurityLevel_Type.__name__=_B
_Xgs360028fTrapHostConfSecurityLevel_Object=MibTableColumn
xgs360028fTrapHostConfSecurityLevel=_Xgs360028fTrapHostConfSecurityLevel_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,4,1,8),_Xgs360028fTrapHostConfSecurityLevel_Type())
xgs360028fTrapHostConfSecurityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapHostConfSecurityLevel.setStatus(_A)
class _Xgs360028fTrapHostConfAuthPtc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Xgs360028fTrapHostConfAuthPtc_Type.__name__=_B
_Xgs360028fTrapHostConfAuthPtc_Object=MibTableColumn
xgs360028fTrapHostConfAuthPtc=_Xgs360028fTrapHostConfAuthPtc_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,4,1,9),_Xgs360028fTrapHostConfAuthPtc_Type())
xgs360028fTrapHostConfAuthPtc.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapHostConfAuthPtc.setStatus(_A)
_Xgs360028fTrapHostConfAuthPassword_Type=DisplayString
_Xgs360028fTrapHostConfAuthPassword_Object=MibTableColumn
xgs360028fTrapHostConfAuthPassword=_Xgs360028fTrapHostConfAuthPassword_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,4,1,10),_Xgs360028fTrapHostConfAuthPassword_Type())
xgs360028fTrapHostConfAuthPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapHostConfAuthPassword.setStatus(_A)
class _Xgs360028fTrapHostConfPrivPtc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Xgs360028fTrapHostConfPrivPtc_Type.__name__=_B
_Xgs360028fTrapHostConfPrivPtc_Object=MibTableColumn
xgs360028fTrapHostConfPrivPtc=_Xgs360028fTrapHostConfPrivPtc_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,4,1,11),_Xgs360028fTrapHostConfPrivPtc_Type())
xgs360028fTrapHostConfPrivPtc.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapHostConfPrivPtc.setStatus(_A)
_Xgs360028fTrapHostConfPrivPassword_Type=DisplayString
_Xgs360028fTrapHostConfPrivPassword_Object=MibTableColumn
xgs360028fTrapHostConfPrivPassword=_Xgs360028fTrapHostConfPrivPassword_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,4,1,12),_Xgs360028fTrapHostConfPrivPassword_Type())
xgs360028fTrapHostConfPrivPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapHostConfPrivPassword.setStatus(_A)
class _Xgs360028fTrapHostConfCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fTrapHostConfCurrentMode_Type.__name__=_B
_Xgs360028fTrapHostConfCurrentMode_Object=MibTableColumn
xgs360028fTrapHostConfCurrentMode=_Xgs360028fTrapHostConfCurrentMode_Object((1,3,6,1,4,1,890,1,5,8,78,1,6,1,4,1,13),_Xgs360028fTrapHostConfCurrentMode_Type())
xgs360028fTrapHostConfCurrentMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapHostConfCurrentMode.setStatus(_A)
_Xgs360028fConfiguration_ObjectIdentity=ObjectIdentity
xgs360028fConfiguration=_Xgs360028fConfiguration_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2))
_Xgs360028fPort_ObjectIdentity=ObjectIdentity
xgs360028fPort=_Xgs360028fPort_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,1))
_Xgs360028fPortConfigurationTable_Object=MibTable
xgs360028fPortConfigurationTable=_Xgs360028fPortConfigurationTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,1))
if mibBuilder.loadTexts:xgs360028fPortConfigurationTable.setStatus(_A)
_Xgs360028fPortConfigurationEntry_Object=MibTableRow
xgs360028fPortConfigurationEntry=_Xgs360028fPortConfigurationEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,1,1))
xgs360028fPortConfigurationEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:xgs360028fPortConfigurationEntry.setStatus(_A)
class _Xgs360028fPortConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fPortConfPort_Type.__name__=_B
_Xgs360028fPortConfPort_Object=MibTableColumn
xgs360028fPortConfPort=_Xgs360028fPortConfPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,1,1,1),_Xgs360028fPortConfPort_Type())
xgs360028fPortConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fPortConfPort.setStatus(_A)
class _Xgs360028fPortConfPortMedia_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_Xgs360028fPortConfPortMedia_Type.__name__=_G
_Xgs360028fPortConfPortMedia_Object=MibTableColumn
xgs360028fPortConfPortMedia=_Xgs360028fPortConfPortMedia_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,1,1,2),_Xgs360028fPortConfPortMedia_Type())
xgs360028fPortConfPortMedia.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortConfPortMedia.setStatus(_A)
class _Xgs360028fPortConfLink_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,4))
_Xgs360028fPortConfLink_Type.__name__=_G
_Xgs360028fPortConfLink_Object=MibTableColumn
xgs360028fPortConfLink=_Xgs360028fPortConfLink_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,1,1,3),_Xgs360028fPortConfLink_Type())
xgs360028fPortConfLink.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortConfLink.setStatus(_A)
class _Xgs360028fPortConfCurrentSpeed_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,12))
_Xgs360028fPortConfCurrentSpeed_Type.__name__=_G
_Xgs360028fPortConfCurrentSpeed_Object=MibTableColumn
xgs360028fPortConfCurrentSpeed=_Xgs360028fPortConfCurrentSpeed_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,1,1,4),_Xgs360028fPortConfCurrentSpeed_Type())
xgs360028fPortConfCurrentSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortConfCurrentSpeed.setStatus(_A)
class _Xgs360028fPortConfSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_Xgs360028fPortConfSpeed_Type.__name__=_B
_Xgs360028fPortConfSpeed_Object=MibTableColumn
xgs360028fPortConfSpeed=_Xgs360028fPortConfSpeed_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,1,1,5),_Xgs360028fPortConfSpeed_Type())
xgs360028fPortConfSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortConfSpeed.setStatus(_A)
class _Xgs360028fPortConfCurrentFlowControlRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fPortConfCurrentFlowControlRx_Type.__name__=_B
_Xgs360028fPortConfCurrentFlowControlRx_Object=MibTableColumn
xgs360028fPortConfCurrentFlowControlRx=_Xgs360028fPortConfCurrentFlowControlRx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,1,1,6),_Xgs360028fPortConfCurrentFlowControlRx_Type())
xgs360028fPortConfCurrentFlowControlRx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortConfCurrentFlowControlRx.setStatus(_A)
class _Xgs360028fPortConfCurrentFlowControlTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fPortConfCurrentFlowControlTx_Type.__name__=_B
_Xgs360028fPortConfCurrentFlowControlTx_Object=MibTableColumn
xgs360028fPortConfCurrentFlowControlTx=_Xgs360028fPortConfCurrentFlowControlTx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,1,1,7),_Xgs360028fPortConfCurrentFlowControlTx_Type())
xgs360028fPortConfCurrentFlowControlTx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortConfCurrentFlowControlTx.setStatus(_A)
class _Xgs360028fPortConfFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fPortConfFlowControl_Type.__name__=_B
_Xgs360028fPortConfFlowControl_Object=MibTableColumn
xgs360028fPortConfFlowControl=_Xgs360028fPortConfFlowControl_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,1,1,8),_Xgs360028fPortConfFlowControl_Type())
xgs360028fPortConfFlowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortConfFlowControl.setStatus(_A)
class _Xgs360028fPortConfMaxFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1518,9600))
_Xgs360028fPortConfMaxFrameSize_Type.__name__=_B
_Xgs360028fPortConfMaxFrameSize_Object=MibTableColumn
xgs360028fPortConfMaxFrameSize=_Xgs360028fPortConfMaxFrameSize_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,1,1,9),_Xgs360028fPortConfMaxFrameSize_Type())
xgs360028fPortConfMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortConfMaxFrameSize.setStatus(_A)
class _Xgs360028fPortConfExcessiveCollisionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fPortConfExcessiveCollisionMode_Type.__name__=_B
_Xgs360028fPortConfExcessiveCollisionMode_Object=MibTableColumn
xgs360028fPortConfExcessiveCollisionMode=_Xgs360028fPortConfExcessiveCollisionMode_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,1,1,10),_Xgs360028fPortConfExcessiveCollisionMode_Type())
xgs360028fPortConfExcessiveCollisionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortConfExcessiveCollisionMode.setStatus(_A)
class _Xgs360028fPortConfPowerControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360028fPortConfPowerControl_Type.__name__=_B
_Xgs360028fPortConfPowerControl_Object=MibTableColumn
xgs360028fPortConfPowerControl=_Xgs360028fPortConfPowerControl_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,1,1,11),_Xgs360028fPortConfPowerControl_Type())
xgs360028fPortConfPowerControl.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortConfPowerControl.setStatus(_A)
_Xgs360028fPortConfDescription_Type=DisplayString
_Xgs360028fPortConfDescription_Object=MibTableColumn
xgs360028fPortConfDescription=_Xgs360028fPortConfDescription_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,1,1,12),_Xgs360028fPortConfDescription_Type())
xgs360028fPortConfDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortConfDescription.setStatus(_A)
_Xgs360028fPortTrafficStatisticsTable_Object=MibTable
xgs360028fPortTrafficStatisticsTable=_Xgs360028fPortTrafficStatisticsTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2))
if mibBuilder.loadTexts:xgs360028fPortTrafficStatisticsTable.setStatus(_A)
_Xgs360028fPortTrafficStatisticsEntry_Object=MibTableRow
xgs360028fPortTrafficStatisticsEntry=_Xgs360028fPortTrafficStatisticsEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1))
xgs360028fPortTrafficStatisticsEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:xgs360028fPortTrafficStatisticsEntry.setStatus(_A)
class _Xgs360028fPortTrafficStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fPortTrafficStatisticsPort_Type.__name__=_B
_Xgs360028fPortTrafficStatisticsPort_Object=MibTableColumn
xgs360028fPortTrafficStatisticsPort=_Xgs360028fPortTrafficStatisticsPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,1),_Xgs360028fPortTrafficStatisticsPort_Type())
xgs360028fPortTrafficStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fPortTrafficStatisticsPort.setStatus(_A)
class _Xgs360028fPortTrafficStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fPortTrafficStatisticsClear_Type.__name__=_B
_Xgs360028fPortTrafficStatisticsClear_Object=MibTableColumn
xgs360028fPortTrafficStatisticsClear=_Xgs360028fPortTrafficStatisticsClear_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,2),_Xgs360028fPortTrafficStatisticsClear_Type())
xgs360028fPortTrafficStatisticsClear.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortTrafficStatisticsClear.setStatus(_A)
_Xgs360028fPortTrafficRxPackets_Type=Counter64
_Xgs360028fPortTrafficRxPackets_Object=MibTableColumn
xgs360028fPortTrafficRxPackets=_Xgs360028fPortTrafficRxPackets_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,3),_Xgs360028fPortTrafficRxPackets_Type())
xgs360028fPortTrafficRxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxPackets.setStatus(_A)
_Xgs360028fPortTrafficRxOctets_Type=Counter64
_Xgs360028fPortTrafficRxOctets_Object=MibTableColumn
xgs360028fPortTrafficRxOctets=_Xgs360028fPortTrafficRxOctets_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,4),_Xgs360028fPortTrafficRxOctets_Type())
xgs360028fPortTrafficRxOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxOctets.setStatus(_A)
_Xgs360028fPortTrafficRxUnicast_Type=Counter64
_Xgs360028fPortTrafficRxUnicast_Object=MibTableColumn
xgs360028fPortTrafficRxUnicast=_Xgs360028fPortTrafficRxUnicast_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,5),_Xgs360028fPortTrafficRxUnicast_Type())
xgs360028fPortTrafficRxUnicast.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxUnicast.setStatus(_A)
_Xgs360028fPortTrafficRxMulticast_Type=Counter64
_Xgs360028fPortTrafficRxMulticast_Object=MibTableColumn
xgs360028fPortTrafficRxMulticast=_Xgs360028fPortTrafficRxMulticast_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,6),_Xgs360028fPortTrafficRxMulticast_Type())
xgs360028fPortTrafficRxMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxMulticast.setStatus(_A)
_Xgs360028fPortTrafficRxBroadcast_Type=Counter64
_Xgs360028fPortTrafficRxBroadcast_Object=MibTableColumn
xgs360028fPortTrafficRxBroadcast=_Xgs360028fPortTrafficRxBroadcast_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,7),_Xgs360028fPortTrafficRxBroadcast_Type())
xgs360028fPortTrafficRxBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxBroadcast.setStatus(_A)
_Xgs360028fPortTrafficRxPause_Type=Counter64
_Xgs360028fPortTrafficRxPause_Object=MibTableColumn
xgs360028fPortTrafficRxPause=_Xgs360028fPortTrafficRxPause_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,8),_Xgs360028fPortTrafficRxPause_Type())
xgs360028fPortTrafficRxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxPause.setStatus(_A)
_Xgs360028fPortTrafficRx64Bytes_Type=Counter64
_Xgs360028fPortTrafficRx64Bytes_Object=MibTableColumn
xgs360028fPortTrafficRx64Bytes=_Xgs360028fPortTrafficRx64Bytes_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,9),_Xgs360028fPortTrafficRx64Bytes_Type())
xgs360028fPortTrafficRx64Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRx64Bytes.setStatus(_A)
_Xgs360028fPortTrafficRx65to127Bytes_Type=Counter64
_Xgs360028fPortTrafficRx65to127Bytes_Object=MibTableColumn
xgs360028fPortTrafficRx65to127Bytes=_Xgs360028fPortTrafficRx65to127Bytes_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,10),_Xgs360028fPortTrafficRx65to127Bytes_Type())
xgs360028fPortTrafficRx65to127Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRx65to127Bytes.setStatus(_A)
_Xgs360028fPortTrafficRx128to255Bytes_Type=Counter64
_Xgs360028fPortTrafficRx128to255Bytes_Object=MibTableColumn
xgs360028fPortTrafficRx128to255Bytes=_Xgs360028fPortTrafficRx128to255Bytes_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,11),_Xgs360028fPortTrafficRx128to255Bytes_Type())
xgs360028fPortTrafficRx128to255Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRx128to255Bytes.setStatus(_A)
_Xgs360028fPortTrafficRx256to511Bytes_Type=Counter64
_Xgs360028fPortTrafficRx256to511Bytes_Object=MibTableColumn
xgs360028fPortTrafficRx256to511Bytes=_Xgs360028fPortTrafficRx256to511Bytes_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,12),_Xgs360028fPortTrafficRx256to511Bytes_Type())
xgs360028fPortTrafficRx256to511Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRx256to511Bytes.setStatus(_A)
_Xgs360028fPortTrafficRx512to1023Bytes_Type=Counter64
_Xgs360028fPortTrafficRx512to1023Bytes_Object=MibTableColumn
xgs360028fPortTrafficRx512to1023Bytes=_Xgs360028fPortTrafficRx512to1023Bytes_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,13),_Xgs360028fPortTrafficRx512to1023Bytes_Type())
xgs360028fPortTrafficRx512to1023Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRx512to1023Bytes.setStatus(_A)
_Xgs360028fPortTrafficRx1024to1526Bytes_Type=Counter64
_Xgs360028fPortTrafficRx1024to1526Bytes_Object=MibTableColumn
xgs360028fPortTrafficRx1024to1526Bytes=_Xgs360028fPortTrafficRx1024to1526Bytes_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,14),_Xgs360028fPortTrafficRx1024to1526Bytes_Type())
xgs360028fPortTrafficRx1024to1526Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRx1024to1526Bytes.setStatus(_A)
_Xgs360028fPortTrafficRxExceecd1527Bytes_Type=Counter64
_Xgs360028fPortTrafficRxExceecd1527Bytes_Object=MibTableColumn
xgs360028fPortTrafficRxExceecd1527Bytes=_Xgs360028fPortTrafficRxExceecd1527Bytes_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,15),_Xgs360028fPortTrafficRxExceecd1527Bytes_Type())
xgs360028fPortTrafficRxExceecd1527Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxExceecd1527Bytes.setStatus(_A)
_Xgs360028fPortTrafficRxQ0_Type=Counter64
_Xgs360028fPortTrafficRxQ0_Object=MibTableColumn
xgs360028fPortTrafficRxQ0=_Xgs360028fPortTrafficRxQ0_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,16),_Xgs360028fPortTrafficRxQ0_Type())
xgs360028fPortTrafficRxQ0.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxQ0.setStatus(_A)
_Xgs360028fPortTrafficRxQ1_Type=Counter64
_Xgs360028fPortTrafficRxQ1_Object=MibTableColumn
xgs360028fPortTrafficRxQ1=_Xgs360028fPortTrafficRxQ1_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,17),_Xgs360028fPortTrafficRxQ1_Type())
xgs360028fPortTrafficRxQ1.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxQ1.setStatus(_A)
_Xgs360028fPortTrafficRxQ2_Type=Counter64
_Xgs360028fPortTrafficRxQ2_Object=MibTableColumn
xgs360028fPortTrafficRxQ2=_Xgs360028fPortTrafficRxQ2_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,18),_Xgs360028fPortTrafficRxQ2_Type())
xgs360028fPortTrafficRxQ2.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxQ2.setStatus(_A)
_Xgs360028fPortTrafficRxQ3_Type=Counter64
_Xgs360028fPortTrafficRxQ3_Object=MibTableColumn
xgs360028fPortTrafficRxQ3=_Xgs360028fPortTrafficRxQ3_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,19),_Xgs360028fPortTrafficRxQ3_Type())
xgs360028fPortTrafficRxQ3.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxQ3.setStatus(_A)
_Xgs360028fPortTrafficRxQ4_Type=Counter64
_Xgs360028fPortTrafficRxQ4_Object=MibTableColumn
xgs360028fPortTrafficRxQ4=_Xgs360028fPortTrafficRxQ4_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,20),_Xgs360028fPortTrafficRxQ4_Type())
xgs360028fPortTrafficRxQ4.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxQ4.setStatus(_A)
_Xgs360028fPortTrafficRxQ5_Type=Counter64
_Xgs360028fPortTrafficRxQ5_Object=MibTableColumn
xgs360028fPortTrafficRxQ5=_Xgs360028fPortTrafficRxQ5_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,21),_Xgs360028fPortTrafficRxQ5_Type())
xgs360028fPortTrafficRxQ5.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxQ5.setStatus(_A)
_Xgs360028fPortTrafficRxQ6_Type=Counter64
_Xgs360028fPortTrafficRxQ6_Object=MibTableColumn
xgs360028fPortTrafficRxQ6=_Xgs360028fPortTrafficRxQ6_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,22),_Xgs360028fPortTrafficRxQ6_Type())
xgs360028fPortTrafficRxQ6.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxQ6.setStatus(_A)
_Xgs360028fPortTrafficRxQ7_Type=Counter64
_Xgs360028fPortTrafficRxQ7_Object=MibTableColumn
xgs360028fPortTrafficRxQ7=_Xgs360028fPortTrafficRxQ7_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,23),_Xgs360028fPortTrafficRxQ7_Type())
xgs360028fPortTrafficRxQ7.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxQ7.setStatus(_A)
_Xgs360028fPortTrafficRxDrops_Type=Counter64
_Xgs360028fPortTrafficRxDrops_Object=MibTableColumn
xgs360028fPortTrafficRxDrops=_Xgs360028fPortTrafficRxDrops_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,24),_Xgs360028fPortTrafficRxDrops_Type())
xgs360028fPortTrafficRxDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxDrops.setStatus(_A)
_Xgs360028fPortTrafficRxCRCorAlignment_Type=Counter64
_Xgs360028fPortTrafficRxCRCorAlignment_Object=MibTableColumn
xgs360028fPortTrafficRxCRCorAlignment=_Xgs360028fPortTrafficRxCRCorAlignment_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,25),_Xgs360028fPortTrafficRxCRCorAlignment_Type())
xgs360028fPortTrafficRxCRCorAlignment.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxCRCorAlignment.setStatus(_A)
_Xgs360028fPortTrafficRxUndersize_Type=Counter64
_Xgs360028fPortTrafficRxUndersize_Object=MibTableColumn
xgs360028fPortTrafficRxUndersize=_Xgs360028fPortTrafficRxUndersize_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,26),_Xgs360028fPortTrafficRxUndersize_Type())
xgs360028fPortTrafficRxUndersize.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxUndersize.setStatus(_A)
_Xgs360028fPortTrafficRxOversize_Type=Counter64
_Xgs360028fPortTrafficRxOversize_Object=MibTableColumn
xgs360028fPortTrafficRxOversize=_Xgs360028fPortTrafficRxOversize_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,27),_Xgs360028fPortTrafficRxOversize_Type())
xgs360028fPortTrafficRxOversize.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxOversize.setStatus(_A)
_Xgs360028fPortTrafficRxFragments_Type=Counter64
_Xgs360028fPortTrafficRxFragments_Object=MibTableColumn
xgs360028fPortTrafficRxFragments=_Xgs360028fPortTrafficRxFragments_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,28),_Xgs360028fPortTrafficRxFragments_Type())
xgs360028fPortTrafficRxFragments.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxFragments.setStatus(_A)
_Xgs360028fPortTrafficRxJabber_Type=Counter64
_Xgs360028fPortTrafficRxJabber_Object=MibTableColumn
xgs360028fPortTrafficRxJabber=_Xgs360028fPortTrafficRxJabber_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,29),_Xgs360028fPortTrafficRxJabber_Type())
xgs360028fPortTrafficRxJabber.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxJabber.setStatus(_A)
_Xgs360028fPortTrafficRxFiltered_Type=Counter64
_Xgs360028fPortTrafficRxFiltered_Object=MibTableColumn
xgs360028fPortTrafficRxFiltered=_Xgs360028fPortTrafficRxFiltered_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,30),_Xgs360028fPortTrafficRxFiltered_Type())
xgs360028fPortTrafficRxFiltered.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficRxFiltered.setStatus(_A)
_Xgs360028fPortTrafficTxPackets_Type=Counter64
_Xgs360028fPortTrafficTxPackets_Object=MibTableColumn
xgs360028fPortTrafficTxPackets=_Xgs360028fPortTrafficTxPackets_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,31),_Xgs360028fPortTrafficTxPackets_Type())
xgs360028fPortTrafficTxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxPackets.setStatus(_A)
_Xgs360028fPortTrafficTxOctets_Type=Counter64
_Xgs360028fPortTrafficTxOctets_Object=MibTableColumn
xgs360028fPortTrafficTxOctets=_Xgs360028fPortTrafficTxOctets_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,32),_Xgs360028fPortTrafficTxOctets_Type())
xgs360028fPortTrafficTxOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxOctets.setStatus(_A)
_Xgs360028fPortTrafficTxUnicast_Type=Counter64
_Xgs360028fPortTrafficTxUnicast_Object=MibTableColumn
xgs360028fPortTrafficTxUnicast=_Xgs360028fPortTrafficTxUnicast_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,33),_Xgs360028fPortTrafficTxUnicast_Type())
xgs360028fPortTrafficTxUnicast.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxUnicast.setStatus(_A)
_Xgs360028fPortTrafficTxMulticast_Type=Counter64
_Xgs360028fPortTrafficTxMulticast_Object=MibTableColumn
xgs360028fPortTrafficTxMulticast=_Xgs360028fPortTrafficTxMulticast_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,34),_Xgs360028fPortTrafficTxMulticast_Type())
xgs360028fPortTrafficTxMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxMulticast.setStatus(_A)
_Xgs360028fPortTrafficTxBroadcast_Type=Counter64
_Xgs360028fPortTrafficTxBroadcast_Object=MibTableColumn
xgs360028fPortTrafficTxBroadcast=_Xgs360028fPortTrafficTxBroadcast_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,35),_Xgs360028fPortTrafficTxBroadcast_Type())
xgs360028fPortTrafficTxBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxBroadcast.setStatus(_A)
_Xgs360028fPortTrafficTxPause_Type=Counter64
_Xgs360028fPortTrafficTxPause_Object=MibTableColumn
xgs360028fPortTrafficTxPause=_Xgs360028fPortTrafficTxPause_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,36),_Xgs360028fPortTrafficTxPause_Type())
xgs360028fPortTrafficTxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxPause.setStatus(_A)
_Xgs360028fPortTrafficTx64Bytes_Type=Counter64
_Xgs360028fPortTrafficTx64Bytes_Object=MibTableColumn
xgs360028fPortTrafficTx64Bytes=_Xgs360028fPortTrafficTx64Bytes_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,37),_Xgs360028fPortTrafficTx64Bytes_Type())
xgs360028fPortTrafficTx64Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTx64Bytes.setStatus(_A)
_Xgs360028fPortTrafficTx65to127Bytes_Type=Counter64
_Xgs360028fPortTrafficTx65to127Bytes_Object=MibTableColumn
xgs360028fPortTrafficTx65to127Bytes=_Xgs360028fPortTrafficTx65to127Bytes_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,38),_Xgs360028fPortTrafficTx65to127Bytes_Type())
xgs360028fPortTrafficTx65to127Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTx65to127Bytes.setStatus(_A)
_Xgs360028fPortTrafficTx128to255Bytes_Type=Counter64
_Xgs360028fPortTrafficTx128to255Bytes_Object=MibTableColumn
xgs360028fPortTrafficTx128to255Bytes=_Xgs360028fPortTrafficTx128to255Bytes_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,39),_Xgs360028fPortTrafficTx128to255Bytes_Type())
xgs360028fPortTrafficTx128to255Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTx128to255Bytes.setStatus(_A)
_Xgs360028fPortTrafficTx256to511Bytes_Type=Counter64
_Xgs360028fPortTrafficTx256to511Bytes_Object=MibTableColumn
xgs360028fPortTrafficTx256to511Bytes=_Xgs360028fPortTrafficTx256to511Bytes_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,40),_Xgs360028fPortTrafficTx256to511Bytes_Type())
xgs360028fPortTrafficTx256to511Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTx256to511Bytes.setStatus(_A)
_Xgs360028fPortTrafficTx512to1023Bytes_Type=Counter64
_Xgs360028fPortTrafficTx512to1023Bytes_Object=MibTableColumn
xgs360028fPortTrafficTx512to1023Bytes=_Xgs360028fPortTrafficTx512to1023Bytes_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,41),_Xgs360028fPortTrafficTx512to1023Bytes_Type())
xgs360028fPortTrafficTx512to1023Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTx512to1023Bytes.setStatus(_A)
_Xgs360028fPortTrafficTx1024to1526Bytes_Type=Counter64
_Xgs360028fPortTrafficTx1024to1526Bytes_Object=MibTableColumn
xgs360028fPortTrafficTx1024to1526Bytes=_Xgs360028fPortTrafficTx1024to1526Bytes_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,42),_Xgs360028fPortTrafficTx1024to1526Bytes_Type())
xgs360028fPortTrafficTx1024to1526Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTx1024to1526Bytes.setStatus(_A)
_Xgs360028fPortTrafficTxExceecd1527Bytes_Type=Counter64
_Xgs360028fPortTrafficTxExceecd1527Bytes_Object=MibTableColumn
xgs360028fPortTrafficTxExceecd1527Bytes=_Xgs360028fPortTrafficTxExceecd1527Bytes_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,43),_Xgs360028fPortTrafficTxExceecd1527Bytes_Type())
xgs360028fPortTrafficTxExceecd1527Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxExceecd1527Bytes.setStatus(_A)
_Xgs360028fPortTrafficTxQ0_Type=Counter64
_Xgs360028fPortTrafficTxQ0_Object=MibTableColumn
xgs360028fPortTrafficTxQ0=_Xgs360028fPortTrafficTxQ0_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,44),_Xgs360028fPortTrafficTxQ0_Type())
xgs360028fPortTrafficTxQ0.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxQ0.setStatus(_A)
_Xgs360028fPortTrafficTxQ1_Type=Counter64
_Xgs360028fPortTrafficTxQ1_Object=MibTableColumn
xgs360028fPortTrafficTxQ1=_Xgs360028fPortTrafficTxQ1_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,45),_Xgs360028fPortTrafficTxQ1_Type())
xgs360028fPortTrafficTxQ1.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxQ1.setStatus(_A)
_Xgs360028fPortTrafficTxQ2_Type=Counter64
_Xgs360028fPortTrafficTxQ2_Object=MibTableColumn
xgs360028fPortTrafficTxQ2=_Xgs360028fPortTrafficTxQ2_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,46),_Xgs360028fPortTrafficTxQ2_Type())
xgs360028fPortTrafficTxQ2.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxQ2.setStatus(_A)
_Xgs360028fPortTrafficTxQ3_Type=Counter64
_Xgs360028fPortTrafficTxQ3_Object=MibTableColumn
xgs360028fPortTrafficTxQ3=_Xgs360028fPortTrafficTxQ3_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,47),_Xgs360028fPortTrafficTxQ3_Type())
xgs360028fPortTrafficTxQ3.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxQ3.setStatus(_A)
_Xgs360028fPortTrafficTxQ4_Type=Counter64
_Xgs360028fPortTrafficTxQ4_Object=MibTableColumn
xgs360028fPortTrafficTxQ4=_Xgs360028fPortTrafficTxQ4_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,48),_Xgs360028fPortTrafficTxQ4_Type())
xgs360028fPortTrafficTxQ4.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxQ4.setStatus(_A)
_Xgs360028fPortTrafficTxQ5_Type=Counter64
_Xgs360028fPortTrafficTxQ5_Object=MibTableColumn
xgs360028fPortTrafficTxQ5=_Xgs360028fPortTrafficTxQ5_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,49),_Xgs360028fPortTrafficTxQ5_Type())
xgs360028fPortTrafficTxQ5.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxQ5.setStatus(_A)
_Xgs360028fPortTrafficTxQ6_Type=Counter64
_Xgs360028fPortTrafficTxQ6_Object=MibTableColumn
xgs360028fPortTrafficTxQ6=_Xgs360028fPortTrafficTxQ6_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,50),_Xgs360028fPortTrafficTxQ6_Type())
xgs360028fPortTrafficTxQ6.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxQ6.setStatus(_A)
_Xgs360028fPortTrafficTxQ7_Type=Counter64
_Xgs360028fPortTrafficTxQ7_Object=MibTableColumn
xgs360028fPortTrafficTxQ7=_Xgs360028fPortTrafficTxQ7_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,51),_Xgs360028fPortTrafficTxQ7_Type())
xgs360028fPortTrafficTxQ7.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxQ7.setStatus(_A)
_Xgs360028fPortTrafficTxDrops_Type=Counter64
_Xgs360028fPortTrafficTxDrops_Object=MibTableColumn
xgs360028fPortTrafficTxDrops=_Xgs360028fPortTrafficTxDrops_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,52),_Xgs360028fPortTrafficTxDrops_Type())
xgs360028fPortTrafficTxDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxDrops.setStatus(_A)
_Xgs360028fPortTrafficTxLateOrExcColl_Type=Counter64
_Xgs360028fPortTrafficTxLateOrExcColl_Object=MibTableColumn
xgs360028fPortTrafficTxLateOrExcColl=_Xgs360028fPortTrafficTxLateOrExcColl_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,2,1,53),_Xgs360028fPortTrafficTxLateOrExcColl_Type())
xgs360028fPortTrafficTxLateOrExcColl.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortTrafficTxLateOrExcColl.setStatus(_A)
_Xgs360028fPortQoSStatistics_ObjectIdentity=ObjectIdentity
xgs360028fPortQoSStatistics=_Xgs360028fPortQoSStatistics_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,1,3))
class _Xgs360028fPortQoSStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fPortQoSStatisticsClear_Type.__name__=_B
_Xgs360028fPortQoSStatisticsClear_Object=MibScalar
xgs360028fPortQoSStatisticsClear=_Xgs360028fPortQoSStatisticsClear_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,1),_Xgs360028fPortQoSStatisticsClear_Type())
xgs360028fPortQoSStatisticsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSStatisticsClear.setStatus(_A)
_Xgs360028fPortQoSStatisticsTable_Object=MibTable
xgs360028fPortQoSStatisticsTable=_Xgs360028fPortQoSStatisticsTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2))
if mibBuilder.loadTexts:xgs360028fPortQoSStatisticsTable.setStatus(_A)
_Xgs360028fPortQoSStatisticsEntry_Object=MibTableRow
xgs360028fPortQoSStatisticsEntry=_Xgs360028fPortQoSStatisticsEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1))
xgs360028fPortQoSStatisticsEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:xgs360028fPortQoSStatisticsEntry.setStatus(_A)
class _Xgs360028fPortQoSStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fPortQoSStatisticsPort_Type.__name__=_B
_Xgs360028fPortQoSStatisticsPort_Object=MibTableColumn
xgs360028fPortQoSStatisticsPort=_Xgs360028fPortQoSStatisticsPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,1),_Xgs360028fPortQoSStatisticsPort_Type())
xgs360028fPortQoSStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fPortQoSStatisticsPort.setStatus(_A)
_Xgs360028fPortQoSQ0Rx_Type=Counter64
_Xgs360028fPortQoSQ0Rx_Object=MibTableColumn
xgs360028fPortQoSQ0Rx=_Xgs360028fPortQoSQ0Rx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,2),_Xgs360028fPortQoSQ0Rx_Type())
xgs360028fPortQoSQ0Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ0Rx.setStatus(_A)
_Xgs360028fPortQoSQ0Tx_Type=Counter64
_Xgs360028fPortQoSQ0Tx_Object=MibTableColumn
xgs360028fPortQoSQ0Tx=_Xgs360028fPortQoSQ0Tx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,3),_Xgs360028fPortQoSQ0Tx_Type())
xgs360028fPortQoSQ0Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ0Tx.setStatus(_A)
_Xgs360028fPortQoSQ1Rx_Type=Counter64
_Xgs360028fPortQoSQ1Rx_Object=MibTableColumn
xgs360028fPortQoSQ1Rx=_Xgs360028fPortQoSQ1Rx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,4),_Xgs360028fPortQoSQ1Rx_Type())
xgs360028fPortQoSQ1Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ1Rx.setStatus(_A)
_Xgs360028fPortQoSQ1Tx_Type=Counter64
_Xgs360028fPortQoSQ1Tx_Object=MibTableColumn
xgs360028fPortQoSQ1Tx=_Xgs360028fPortQoSQ1Tx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,5),_Xgs360028fPortQoSQ1Tx_Type())
xgs360028fPortQoSQ1Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ1Tx.setStatus(_A)
_Xgs360028fPortQoSQ2Rx_Type=Counter64
_Xgs360028fPortQoSQ2Rx_Object=MibTableColumn
xgs360028fPortQoSQ2Rx=_Xgs360028fPortQoSQ2Rx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,6),_Xgs360028fPortQoSQ2Rx_Type())
xgs360028fPortQoSQ2Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ2Rx.setStatus(_A)
_Xgs360028fPortQoSQ2Tx_Type=Counter64
_Xgs360028fPortQoSQ2Tx_Object=MibTableColumn
xgs360028fPortQoSQ2Tx=_Xgs360028fPortQoSQ2Tx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,7),_Xgs360028fPortQoSQ2Tx_Type())
xgs360028fPortQoSQ2Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ2Tx.setStatus(_A)
_Xgs360028fPortQoSQ3Rx_Type=Counter64
_Xgs360028fPortQoSQ3Rx_Object=MibTableColumn
xgs360028fPortQoSQ3Rx=_Xgs360028fPortQoSQ3Rx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,8),_Xgs360028fPortQoSQ3Rx_Type())
xgs360028fPortQoSQ3Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ3Rx.setStatus(_A)
_Xgs360028fPortQoSQ3Tx_Type=Counter64
_Xgs360028fPortQoSQ3Tx_Object=MibTableColumn
xgs360028fPortQoSQ3Tx=_Xgs360028fPortQoSQ3Tx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,9),_Xgs360028fPortQoSQ3Tx_Type())
xgs360028fPortQoSQ3Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ3Tx.setStatus(_A)
_Xgs360028fPortQoSQ4Rx_Type=Counter64
_Xgs360028fPortQoSQ4Rx_Object=MibTableColumn
xgs360028fPortQoSQ4Rx=_Xgs360028fPortQoSQ4Rx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,10),_Xgs360028fPortQoSQ4Rx_Type())
xgs360028fPortQoSQ4Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ4Rx.setStatus(_A)
_Xgs360028fPortQoSQ4Tx_Type=Counter64
_Xgs360028fPortQoSQ4Tx_Object=MibTableColumn
xgs360028fPortQoSQ4Tx=_Xgs360028fPortQoSQ4Tx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,11),_Xgs360028fPortQoSQ4Tx_Type())
xgs360028fPortQoSQ4Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ4Tx.setStatus(_A)
_Xgs360028fPortQoSQ5Rx_Type=Counter64
_Xgs360028fPortQoSQ5Rx_Object=MibTableColumn
xgs360028fPortQoSQ5Rx=_Xgs360028fPortQoSQ5Rx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,12),_Xgs360028fPortQoSQ5Rx_Type())
xgs360028fPortQoSQ5Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ5Rx.setStatus(_A)
_Xgs360028fPortQoSQ5Tx_Type=Counter64
_Xgs360028fPortQoSQ5Tx_Object=MibTableColumn
xgs360028fPortQoSQ5Tx=_Xgs360028fPortQoSQ5Tx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,13),_Xgs360028fPortQoSQ5Tx_Type())
xgs360028fPortQoSQ5Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ5Tx.setStatus(_A)
_Xgs360028fPortQoSQ6Rx_Type=Counter64
_Xgs360028fPortQoSQ6Rx_Object=MibTableColumn
xgs360028fPortQoSQ6Rx=_Xgs360028fPortQoSQ6Rx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,14),_Xgs360028fPortQoSQ6Rx_Type())
xgs360028fPortQoSQ6Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ6Rx.setStatus(_A)
_Xgs360028fPortQoSQ6Tx_Type=Counter64
_Xgs360028fPortQoSQ6Tx_Object=MibTableColumn
xgs360028fPortQoSQ6Tx=_Xgs360028fPortQoSQ6Tx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,15),_Xgs360028fPortQoSQ6Tx_Type())
xgs360028fPortQoSQ6Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ6Tx.setStatus(_A)
_Xgs360028fPortQoSQ7Rx_Type=Counter64
_Xgs360028fPortQoSQ7Rx_Object=MibTableColumn
xgs360028fPortQoSQ7Rx=_Xgs360028fPortQoSQ7Rx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,16),_Xgs360028fPortQoSQ7Rx_Type())
xgs360028fPortQoSQ7Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ7Rx.setStatus(_A)
_Xgs360028fPortQoSQ7Tx_Type=Counter64
_Xgs360028fPortQoSQ7Tx_Object=MibTableColumn
xgs360028fPortQoSQ7Tx=_Xgs360028fPortQoSQ7Tx_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,3,2,1,17),_Xgs360028fPortQoSQ7Tx_Type())
xgs360028fPortQoSQ7Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortQoSQ7Tx.setStatus(_A)
_Xgs360028fSFPInfoTable_Object=MibTable
xgs360028fSFPInfoTable=_Xgs360028fSFPInfoTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4))
if mibBuilder.loadTexts:xgs360028fSFPInfoTable.setStatus(_A)
_Xgs360028fSFPInfoEntry_Object=MibTableRow
xgs360028fSFPInfoEntry=_Xgs360028fSFPInfoEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1))
xgs360028fSFPInfoEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:xgs360028fSFPInfoEntry.setStatus(_A)
class _Xgs360028fSFPInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fSFPInfoIndex_Type.__name__=_B
_Xgs360028fSFPInfoIndex_Object=MibTableColumn
xgs360028fSFPInfoIndex=_Xgs360028fSFPInfoIndex_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,1),_Xgs360028fSFPInfoIndex_Type())
xgs360028fSFPInfoIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fSFPInfoIndex.setStatus(_A)
_Xgs360028fSFPInfoPort_Type=DisplayString
_Xgs360028fSFPInfoPort_Object=MibTableColumn
xgs360028fSFPInfoPort=_Xgs360028fSFPInfoPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,2),_Xgs360028fSFPInfoPort_Type())
xgs360028fSFPInfoPort.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPInfoPort.setStatus(_A)
_Xgs360028fSFPConnectorType_Type=DisplayString
_Xgs360028fSFPConnectorType_Object=MibTableColumn
xgs360028fSFPConnectorType=_Xgs360028fSFPConnectorType_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,3),_Xgs360028fSFPConnectorType_Type())
xgs360028fSFPConnectorType.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPConnectorType.setStatus(_A)
_Xgs360028fSFPFiberType_Type=DisplayString
_Xgs360028fSFPFiberType_Object=MibTableColumn
xgs360028fSFPFiberType=_Xgs360028fSFPFiberType_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,4),_Xgs360028fSFPFiberType_Type())
xgs360028fSFPFiberType.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPFiberType.setStatus(_A)
_Xgs360028fSFPTxCentralWavelength_Type=DisplayString
_Xgs360028fSFPTxCentralWavelength_Object=MibTableColumn
xgs360028fSFPTxCentralWavelength=_Xgs360028fSFPTxCentralWavelength_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,5),_Xgs360028fSFPTxCentralWavelength_Type())
xgs360028fSFPTxCentralWavelength.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPTxCentralWavelength.setStatus(_A)
_Xgs360028fSFPBaudRate_Type=DisplayString
_Xgs360028fSFPBaudRate_Object=MibTableColumn
xgs360028fSFPBaudRate=_Xgs360028fSFPBaudRate_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,6),_Xgs360028fSFPBaudRate_Type())
xgs360028fSFPBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPBaudRate.setStatus(_A)
_Xgs360028fSFPVendorOUI_Type=DisplayString
_Xgs360028fSFPVendorOUI_Object=MibTableColumn
xgs360028fSFPVendorOUI=_Xgs360028fSFPVendorOUI_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,7),_Xgs360028fSFPVendorOUI_Type())
xgs360028fSFPVendorOUI.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPVendorOUI.setStatus(_A)
_Xgs360028fSFPVendorName_Type=DisplayString
_Xgs360028fSFPVendorName_Object=MibTableColumn
xgs360028fSFPVendorName=_Xgs360028fSFPVendorName_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,8),_Xgs360028fSFPVendorName_Type())
xgs360028fSFPVendorName.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPVendorName.setStatus(_A)
_Xgs360028fSFPVendorPN_Type=DisplayString
_Xgs360028fSFPVendorPN_Object=MibTableColumn
xgs360028fSFPVendorPN=_Xgs360028fSFPVendorPN_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,9),_Xgs360028fSFPVendorPN_Type())
xgs360028fSFPVendorPN.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPVendorPN.setStatus(_A)
_Xgs360028fSFPVendorRev_Type=DisplayString
_Xgs360028fSFPVendorRev_Object=MibTableColumn
xgs360028fSFPVendorRev=_Xgs360028fSFPVendorRev_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,10),_Xgs360028fSFPVendorRev_Type())
xgs360028fSFPVendorRev.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPVendorRev.setStatus(_A)
_Xgs360028fSFPVendorSN_Type=DisplayString
_Xgs360028fSFPVendorSN_Object=MibTableColumn
xgs360028fSFPVendorSN=_Xgs360028fSFPVendorSN_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,11),_Xgs360028fSFPVendorSN_Type())
xgs360028fSFPVendorSN.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPVendorSN.setStatus(_A)
_Xgs360028fSFPDateCode_Type=DisplayString
_Xgs360028fSFPDateCode_Object=MibTableColumn
xgs360028fSFPDateCode=_Xgs360028fSFPDateCode_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,12),_Xgs360028fSFPDateCode_Type())
xgs360028fSFPDateCode.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPDateCode.setStatus(_A)
_Xgs360028fSFPTemperature_Type=DisplayString
_Xgs360028fSFPTemperature_Object=MibTableColumn
xgs360028fSFPTemperature=_Xgs360028fSFPTemperature_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,13),_Xgs360028fSFPTemperature_Type())
xgs360028fSFPTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPTemperature.setStatus(_A)
_Xgs360028fSFPVcc_Type=DisplayString
_Xgs360028fSFPVcc_Object=MibTableColumn
xgs360028fSFPVcc=_Xgs360028fSFPVcc_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,14),_Xgs360028fSFPVcc_Type())
xgs360028fSFPVcc.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPVcc.setStatus(_A)
_Xgs360028fSFPMon1Bias_Type=DisplayString
_Xgs360028fSFPMon1Bias_Object=MibTableColumn
xgs360028fSFPMon1Bias=_Xgs360028fSFPMon1Bias_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,15),_Xgs360028fSFPMon1Bias_Type())
xgs360028fSFPMon1Bias.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPMon1Bias.setStatus(_A)
_Xgs360028fSFPMon2TxPWR_Type=DisplayString
_Xgs360028fSFPMon2TxPWR_Object=MibTableColumn
xgs360028fSFPMon2TxPWR=_Xgs360028fSFPMon2TxPWR_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,16),_Xgs360028fSFPMon2TxPWR_Type())
xgs360028fSFPMon2TxPWR.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPMon2TxPWR.setStatus(_A)
_Xgs360028fSFPMon3RxPWR_Type=DisplayString
_Xgs360028fSFPMon3RxPWR_Object=MibTableColumn
xgs360028fSFPMon3RxPWR=_Xgs360028fSFPMon3RxPWR_Object((1,3,6,1,4,1,890,1,5,8,78,2,1,4,1,17),_Xgs360028fSFPMon3RxPWR_Type())
xgs360028fSFPMon3RxPWR.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSFPMon3RxPWR.setStatus(_A)
_Xgs360028fGARP_ObjectIdentity=ObjectIdentity
xgs360028fGARP=_Xgs360028fGARP_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,3))
_Xgs360028fGARPConfTable_Object=MibTable
xgs360028fGARPConfTable=_Xgs360028fGARPConfTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,3,1))
if mibBuilder.loadTexts:xgs360028fGARPConfTable.setStatus(_A)
_Xgs360028fGARPConfEntry_Object=MibTableRow
xgs360028fGARPConfEntry=_Xgs360028fGARPConfEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,3,1,1))
xgs360028fGARPConfEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:xgs360028fGARPConfEntry.setStatus(_A)
class _Xgs360028fGARPConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fGARPConfPort_Type.__name__=_B
_Xgs360028fGARPConfPort_Object=MibTableColumn
xgs360028fGARPConfPort=_Xgs360028fGARPConfPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,3,1,1,1),_Xgs360028fGARPConfPort_Type())
xgs360028fGARPConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fGARPConfPort.setStatus(_A)
class _Xgs360028fGARPJoinTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,1000))
_Xgs360028fGARPJoinTimer_Type.__name__=_B
_Xgs360028fGARPJoinTimer_Object=MibTableColumn
xgs360028fGARPJoinTimer=_Xgs360028fGARPJoinTimer_Object((1,3,6,1,4,1,890,1,5,8,78,2,3,1,1,2),_Xgs360028fGARPJoinTimer_Type())
xgs360028fGARPJoinTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fGARPJoinTimer.setStatus(_A)
class _Xgs360028fGARPLeaveTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,3000))
_Xgs360028fGARPLeaveTimer_Type.__name__=_B
_Xgs360028fGARPLeaveTimer_Object=MibTableColumn
xgs360028fGARPLeaveTimer=_Xgs360028fGARPLeaveTimer_Object((1,3,6,1,4,1,890,1,5,8,78,2,3,1,1,3),_Xgs360028fGARPLeaveTimer_Type())
xgs360028fGARPLeaveTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fGARPLeaveTimer.setStatus(_A)
class _Xgs360028fGARPLeaveAllTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10000,50000))
_Xgs360028fGARPLeaveAllTimer_Type.__name__=_B
_Xgs360028fGARPLeaveAllTimer_Object=MibTableColumn
xgs360028fGARPLeaveAllTimer=_Xgs360028fGARPLeaveAllTimer_Object((1,3,6,1,4,1,890,1,5,8,78,2,3,1,1,4),_Xgs360028fGARPLeaveAllTimer_Type())
xgs360028fGARPLeaveAllTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fGARPLeaveAllTimer.setStatus(_A)
class _Xgs360028fGARPApplicantion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Xgs360028fGARPApplicantion_Type.__name__=_B
_Xgs360028fGARPApplicantion_Object=MibTableColumn
xgs360028fGARPApplicantion=_Xgs360028fGARPApplicantion_Object((1,3,6,1,4,1,890,1,5,8,78,2,3,1,1,5),_Xgs360028fGARPApplicantion_Type())
xgs360028fGARPApplicantion.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fGARPApplicantion.setStatus(_A)
class _Xgs360028fGARPAttributeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Xgs360028fGARPAttributeType_Type.__name__=_B
_Xgs360028fGARPAttributeType_Object=MibTableColumn
xgs360028fGARPAttributeType=_Xgs360028fGARPAttributeType_Object((1,3,6,1,4,1,890,1,5,8,78,2,3,1,1,6),_Xgs360028fGARPAttributeType_Type())
xgs360028fGARPAttributeType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fGARPAttributeType.setStatus(_A)
class _Xgs360028fGARPApplicant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fGARPApplicant_Type.__name__=_B
_Xgs360028fGARPApplicant_Object=MibTableColumn
xgs360028fGARPApplicant=_Xgs360028fGARPApplicant_Object((1,3,6,1,4,1,890,1,5,8,78,2,3,1,1,7),_Xgs360028fGARPApplicant_Type())
xgs360028fGARPApplicant.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fGARPApplicant.setStatus(_A)
_Xgs360028fGARPStatisticsTable_Object=MibTable
xgs360028fGARPStatisticsTable=_Xgs360028fGARPStatisticsTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,3,2))
if mibBuilder.loadTexts:xgs360028fGARPStatisticsTable.setStatus(_A)
_Xgs360028fGARPStatisticsEntry_Object=MibTableRow
xgs360028fGARPStatisticsEntry=_Xgs360028fGARPStatisticsEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,3,2,1))
xgs360028fGARPStatisticsEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:xgs360028fGARPStatisticsEntry.setStatus(_A)
class _Xgs360028fGARPStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fGARPStatisticsPort_Type.__name__=_B
_Xgs360028fGARPStatisticsPort_Object=MibTableColumn
xgs360028fGARPStatisticsPort=_Xgs360028fGARPStatisticsPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,3,2,1,1),_Xgs360028fGARPStatisticsPort_Type())
xgs360028fGARPStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fGARPStatisticsPort.setStatus(_A)
_Xgs360028fGARPStatisticsPeerMAC_Type=DisplayString
_Xgs360028fGARPStatisticsPeerMAC_Object=MibTableColumn
xgs360028fGARPStatisticsPeerMAC=_Xgs360028fGARPStatisticsPeerMAC_Object((1,3,6,1,4,1,890,1,5,8,78,2,3,2,1,2),_Xgs360028fGARPStatisticsPeerMAC_Type())
xgs360028fGARPStatisticsPeerMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fGARPStatisticsPeerMAC.setStatus(_A)
_Xgs360028fGARPStatisticsFailedCount_Type=Counter32
_Xgs360028fGARPStatisticsFailedCount_Object=MibTableColumn
xgs360028fGARPStatisticsFailedCount=_Xgs360028fGARPStatisticsFailedCount_Object((1,3,6,1,4,1,890,1,5,8,78,2,3,2,1,3),_Xgs360028fGARPStatisticsFailedCount_Type())
xgs360028fGARPStatisticsFailedCount.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fGARPStatisticsFailedCount.setStatus(_A)
_Xgs360028fGVRP_ObjectIdentity=ObjectIdentity
xgs360028fGVRP=_Xgs360028fGVRP_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,4))
_Xgs360028fGVRPConf_ObjectIdentity=ObjectIdentity
xgs360028fGVRPConf=_Xgs360028fGVRPConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,4,1))
class _Xgs360028fGVRPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fGVRPMode_Type.__name__=_B
_Xgs360028fGVRPMode_Object=MibScalar
xgs360028fGVRPMode=_Xgs360028fGVRPMode_Object((1,3,6,1,4,1,890,1,5,8,78,2,4,1,1),_Xgs360028fGVRPMode_Type())
xgs360028fGVRPMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fGVRPMode.setStatus(_A)
_Xgs360028fGVRPConfTable_Object=MibTable
xgs360028fGVRPConfTable=_Xgs360028fGVRPConfTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,4,1,2))
if mibBuilder.loadTexts:xgs360028fGVRPConfTable.setStatus(_A)
_Xgs360028fGVRPConfEntry_Object=MibTableRow
xgs360028fGVRPConfEntry=_Xgs360028fGVRPConfEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,4,1,2,1))
xgs360028fGVRPConfEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:xgs360028fGVRPConfEntry.setStatus(_A)
class _Xgs360028fGVRPConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fGVRPConfPort_Type.__name__=_B
_Xgs360028fGVRPConfPort_Object=MibTableColumn
xgs360028fGVRPConfPort=_Xgs360028fGVRPConfPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,4,1,2,1,1),_Xgs360028fGVRPConfPort_Type())
xgs360028fGVRPConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fGVRPConfPort.setStatus(_A)
class _Xgs360028fGVRPConfPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fGVRPConfPortMode_Type.__name__=_B
_Xgs360028fGVRPConfPortMode_Object=MibTableColumn
xgs360028fGVRPConfPortMode=_Xgs360028fGVRPConfPortMode_Object((1,3,6,1,4,1,890,1,5,8,78,2,4,1,2,1,2),_Xgs360028fGVRPConfPortMode_Type())
xgs360028fGVRPConfPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fGVRPConfPortMode.setStatus(_A)
class _Xgs360028fGVRPConfPortRRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fGVRPConfPortRRole_Type.__name__=_B
_Xgs360028fGVRPConfPortRRole_Object=MibTableColumn
xgs360028fGVRPConfPortRRole=_Xgs360028fGVRPConfPortRRole_Object((1,3,6,1,4,1,890,1,5,8,78,2,4,1,2,1,3),_Xgs360028fGVRPConfPortRRole_Type())
xgs360028fGVRPConfPortRRole.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fGVRPConfPortRRole.setStatus(_A)
_Xgs360028fGVRPStatisticsTable_Object=MibTable
xgs360028fGVRPStatisticsTable=_Xgs360028fGVRPStatisticsTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,4,2))
if mibBuilder.loadTexts:xgs360028fGVRPStatisticsTable.setStatus(_A)
_Xgs360028fGVRPStatisticsEntry_Object=MibTableRow
xgs360028fGVRPStatisticsEntry=_Xgs360028fGVRPStatisticsEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,4,2,1))
xgs360028fGVRPStatisticsEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:xgs360028fGVRPStatisticsEntry.setStatus(_A)
class _Xgs360028fGVRPStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fGVRPStatisticsPort_Type.__name__=_B
_Xgs360028fGVRPStatisticsPort_Object=MibTableColumn
xgs360028fGVRPStatisticsPort=_Xgs360028fGVRPStatisticsPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,4,2,1,1),_Xgs360028fGVRPStatisticsPort_Type())
xgs360028fGVRPStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fGVRPStatisticsPort.setStatus(_A)
_Xgs360028fGVRPStatisticsJoinTxCnt_Type=Counter32
_Xgs360028fGVRPStatisticsJoinTxCnt_Object=MibTableColumn
xgs360028fGVRPStatisticsJoinTxCnt=_Xgs360028fGVRPStatisticsJoinTxCnt_Object((1,3,6,1,4,1,890,1,5,8,78,2,4,2,1,2),_Xgs360028fGVRPStatisticsJoinTxCnt_Type())
xgs360028fGVRPStatisticsJoinTxCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fGVRPStatisticsJoinTxCnt.setStatus(_A)
_Xgs360028fGVRPStatisticsLeaveTxCnt_Type=Counter32
_Xgs360028fGVRPStatisticsLeaveTxCnt_Object=MibTableColumn
xgs360028fGVRPStatisticsLeaveTxCnt=_Xgs360028fGVRPStatisticsLeaveTxCnt_Object((1,3,6,1,4,1,890,1,5,8,78,2,4,2,1,3),_Xgs360028fGVRPStatisticsLeaveTxCnt_Type())
xgs360028fGVRPStatisticsLeaveTxCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fGVRPStatisticsLeaveTxCnt.setStatus(_A)
_Xgs360028fThermalProtection_ObjectIdentity=ObjectIdentity
xgs360028fThermalProtection=_Xgs360028fThermalProtection_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,5))
class _Xgs360028fPriority0Temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360028fPriority0Temperature_Type.__name__=_B
_Xgs360028fPriority0Temperature_Object=MibScalar
xgs360028fPriority0Temperature=_Xgs360028fPriority0Temperature_Object((1,3,6,1,4,1,890,1,5,8,78,2,5,1),_Xgs360028fPriority0Temperature_Type())
xgs360028fPriority0Temperature.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPriority0Temperature.setStatus(_A)
class _Xgs360028fPriority1Temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360028fPriority1Temperature_Type.__name__=_B
_Xgs360028fPriority1Temperature_Object=MibScalar
xgs360028fPriority1Temperature=_Xgs360028fPriority1Temperature_Object((1,3,6,1,4,1,890,1,5,8,78,2,5,2),_Xgs360028fPriority1Temperature_Type())
xgs360028fPriority1Temperature.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPriority1Temperature.setStatus(_A)
class _Xgs360028fPriority2Temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360028fPriority2Temperature_Type.__name__=_B
_Xgs360028fPriority2Temperature_Object=MibScalar
xgs360028fPriority2Temperature=_Xgs360028fPriority2Temperature_Object((1,3,6,1,4,1,890,1,5,8,78,2,5,3),_Xgs360028fPriority2Temperature_Type())
xgs360028fPriority2Temperature.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPriority2Temperature.setStatus(_A)
class _Xgs360028fPriority3Temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360028fPriority3Temperature_Type.__name__=_B
_Xgs360028fPriority3Temperature_Object=MibScalar
xgs360028fPriority3Temperature=_Xgs360028fPriority3Temperature_Object((1,3,6,1,4,1,890,1,5,8,78,2,5,4),_Xgs360028fPriority3Temperature_Type())
xgs360028fPriority3Temperature.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPriority3Temperature.setStatus(_A)
_Xgs360028fThermalProtectionTable_Object=MibTable
xgs360028fThermalProtectionTable=_Xgs360028fThermalProtectionTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,5,5))
if mibBuilder.loadTexts:xgs360028fThermalProtectionTable.setStatus(_A)
_Xgs360028fThermalProtectionEntry_Object=MibTableRow
xgs360028fThermalProtectionEntry=_Xgs360028fThermalProtectionEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,5,5,1))
xgs360028fThermalProtectionEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:xgs360028fThermalProtectionEntry.setStatus(_A)
class _Xgs360028fThermalProtectionPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fThermalProtectionPort_Type.__name__=_B
_Xgs360028fThermalProtectionPort_Object=MibTableColumn
xgs360028fThermalProtectionPort=_Xgs360028fThermalProtectionPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,5,5,1,1),_Xgs360028fThermalProtectionPort_Type())
xgs360028fThermalProtectionPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fThermalProtectionPort.setStatus(_A)
class _Xgs360028fThermalProtectionPortTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360028fThermalProtectionPortTemperature_Type.__name__=_B
_Xgs360028fThermalProtectionPortTemperature_Object=MibTableColumn
xgs360028fThermalProtectionPortTemperature=_Xgs360028fThermalProtectionPortTemperature_Object((1,3,6,1,4,1,890,1,5,8,78,2,5,5,1,2),_Xgs360028fThermalProtectionPortTemperature_Type())
xgs360028fThermalProtectionPortTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fThermalProtectionPortTemperature.setStatus(_A)
class _Xgs360028fThermalProtectionPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360028fThermalProtectionPortPriority_Type.__name__=_B
_Xgs360028fThermalProtectionPortPriority_Object=MibTableColumn
xgs360028fThermalProtectionPortPriority=_Xgs360028fThermalProtectionPortPriority_Object((1,3,6,1,4,1,890,1,5,8,78,2,5,5,1,3),_Xgs360028fThermalProtectionPortPriority_Type())
xgs360028fThermalProtectionPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fThermalProtectionPortPriority.setStatus(_A)
_Xgs360028fThermalProtectionPortStatus_Type=DisplayString
_Xgs360028fThermalProtectionPortStatus_Object=MibTableColumn
xgs360028fThermalProtectionPortStatus=_Xgs360028fThermalProtectionPortStatus_Object((1,3,6,1,4,1,890,1,5,8,78,2,5,5,1,4),_Xgs360028fThermalProtectionPortStatus_Type())
xgs360028fThermalProtectionPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fThermalProtectionPortStatus.setStatus(_A)
_Xgs360028fMirroring_ObjectIdentity=ObjectIdentity
xgs360028fMirroring=_Xgs360028fMirroring_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,6))
class _Xgs360028fPortToMirrorOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Xgs360028fPortToMirrorOn_Type.__name__=_B
_Xgs360028fPortToMirrorOn_Object=MibScalar
xgs360028fPortToMirrorOn=_Xgs360028fPortToMirrorOn_Object((1,3,6,1,4,1,890,1,5,8,78,2,6,1),_Xgs360028fPortToMirrorOn_Type())
xgs360028fPortToMirrorOn.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortToMirrorOn.setStatus(_A)
_Xgs360028fMirrorTable_Object=MibTable
xgs360028fMirrorTable=_Xgs360028fMirrorTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,6,2))
if mibBuilder.loadTexts:xgs360028fMirrorTable.setStatus(_A)
_Xgs360028fMirrorEntry_Object=MibTableRow
xgs360028fMirrorEntry=_Xgs360028fMirrorEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,6,2,1))
xgs360028fMirrorEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:xgs360028fMirrorEntry.setStatus(_A)
class _Xgs360028fMirrorPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fMirrorPort_Type.__name__=_B
_Xgs360028fMirrorPort_Object=MibTableColumn
xgs360028fMirrorPort=_Xgs360028fMirrorPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,6,2,1,1),_Xgs360028fMirrorPort_Type())
xgs360028fMirrorPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fMirrorPort.setStatus(_A)
class _Xgs360028fMirrorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360028fMirrorMode_Type.__name__=_B
_Xgs360028fMirrorMode_Object=MibTableColumn
xgs360028fMirrorMode=_Xgs360028fMirrorMode_Object((1,3,6,1,4,1,890,1,5,8,78,2,6,2,1,2),_Xgs360028fMirrorMode_Type())
xgs360028fMirrorMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMirrorMode.setStatus(_A)
_Xgs360028fTrapEventSeverity_ObjectIdentity=ObjectIdentity
xgs360028fTrapEventSeverity=_Xgs360028fTrapEventSeverity_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,7))
class _Xgs360028fTrapEventSeverityACL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityACL_Type.__name__=_B
_Xgs360028fTrapEventSeverityACL_Object=MibScalar
xgs360028fTrapEventSeverityACL=_Xgs360028fTrapEventSeverityACL_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,1),_Xgs360028fTrapEventSeverityACL_Type())
xgs360028fTrapEventSeverityACL.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityACL.setStatus(_A)
class _Xgs360028fTrapEventSeverityACLLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityACLLog_Type.__name__=_B
_Xgs360028fTrapEventSeverityACLLog_Object=MibScalar
xgs360028fTrapEventSeverityACLLog=_Xgs360028fTrapEventSeverityACLLog_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,2),_Xgs360028fTrapEventSeverityACLLog_Type())
xgs360028fTrapEventSeverityACLLog.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityACLLog.setStatus(_A)
class _Xgs360028fTrapEventSeverityAccessMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityAccessMgmt_Type.__name__=_B
_Xgs360028fTrapEventSeverityAccessMgmt_Object=MibScalar
xgs360028fTrapEventSeverityAccessMgmt=_Xgs360028fTrapEventSeverityAccessMgmt_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,3),_Xgs360028fTrapEventSeverityAccessMgmt_Type())
xgs360028fTrapEventSeverityAccessMgmt.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityAccessMgmt.setStatus(_A)
class _Xgs360028fTrapEventSeverityAuthFailed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityAuthFailed_Type.__name__=_B
_Xgs360028fTrapEventSeverityAuthFailed_Object=MibScalar
xgs360028fTrapEventSeverityAuthFailed=_Xgs360028fTrapEventSeverityAuthFailed_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,4),_Xgs360028fTrapEventSeverityAuthFailed_Type())
xgs360028fTrapEventSeverityAuthFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityAuthFailed.setStatus(_A)
class _Xgs360028fTrapEventSeverityColdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityColdStart_Type.__name__=_B
_Xgs360028fTrapEventSeverityColdStart_Object=MibScalar
xgs360028fTrapEventSeverityColdStart=_Xgs360028fTrapEventSeverityColdStart_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,5),_Xgs360028fTrapEventSeverityColdStart_Type())
xgs360028fTrapEventSeverityColdStart.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityColdStart.setStatus(_A)
class _Xgs360028fTrapEventSeverityConfigInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityConfigInfo_Type.__name__=_B
_Xgs360028fTrapEventSeverityConfigInfo_Object=MibScalar
xgs360028fTrapEventSeverityConfigInfo=_Xgs360028fTrapEventSeverityConfigInfo_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,6),_Xgs360028fTrapEventSeverityConfigInfo_Type())
xgs360028fTrapEventSeverityConfigInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityConfigInfo.setStatus(_A)
class _Xgs360028fTrapEventSeverityFirmwareUpgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityFirmwareUpgrade_Type.__name__=_B
_Xgs360028fTrapEventSeverityFirmwareUpgrade_Object=MibScalar
xgs360028fTrapEventSeverityFirmwareUpgrade=_Xgs360028fTrapEventSeverityFirmwareUpgrade_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,7),_Xgs360028fTrapEventSeverityFirmwareUpgrade_Type())
xgs360028fTrapEventSeverityFirmwareUpgrade.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityFirmwareUpgrade.setStatus(_A)
class _Xgs360028fTrapEventSeverityImportExport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityImportExport_Type.__name__=_B
_Xgs360028fTrapEventSeverityImportExport_Object=MibScalar
xgs360028fTrapEventSeverityImportExport=_Xgs360028fTrapEventSeverityImportExport_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,8),_Xgs360028fTrapEventSeverityImportExport_Type())
xgs360028fTrapEventSeverityImportExport.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityImportExport.setStatus(_A)
class _Xgs360028fTrapEventSeverityLACP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityLACP_Type.__name__=_B
_Xgs360028fTrapEventSeverityLACP_Object=MibScalar
xgs360028fTrapEventSeverityLACP=_Xgs360028fTrapEventSeverityLACP_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,9),_Xgs360028fTrapEventSeverityLACP_Type())
xgs360028fTrapEventSeverityLACP.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityLACP.setStatus(_A)
class _Xgs360028fTrapEventSeverityLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityLinkStatus_Type.__name__=_B
_Xgs360028fTrapEventSeverityLinkStatus_Object=MibScalar
xgs360028fTrapEventSeverityLinkStatus=_Xgs360028fTrapEventSeverityLinkStatus_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,10),_Xgs360028fTrapEventSeverityLinkStatus_Type())
xgs360028fTrapEventSeverityLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityLinkStatus.setStatus(_A)
class _Xgs360028fTrapEventSeverityLogin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityLogin_Type.__name__=_B
_Xgs360028fTrapEventSeverityLogin_Object=MibScalar
xgs360028fTrapEventSeverityLogin=_Xgs360028fTrapEventSeverityLogin_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,11),_Xgs360028fTrapEventSeverityLogin_Type())
xgs360028fTrapEventSeverityLogin.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityLogin.setStatus(_A)
class _Xgs360028fTrapEventSeverityLogout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityLogout_Type.__name__=_B
_Xgs360028fTrapEventSeverityLogout_Object=MibScalar
xgs360028fTrapEventSeverityLogout=_Xgs360028fTrapEventSeverityLogout_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,12),_Xgs360028fTrapEventSeverityLogout_Type())
xgs360028fTrapEventSeverityLogout.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityLogout.setStatus(_A)
class _Xgs360028fTrapEventSeverityLoopProtect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityLoopProtect_Type.__name__=_B
_Xgs360028fTrapEventSeverityLoopProtect_Object=MibScalar
xgs360028fTrapEventSeverityLoopProtect=_Xgs360028fTrapEventSeverityLoopProtect_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,13),_Xgs360028fTrapEventSeverityLoopProtect_Type())
xgs360028fTrapEventSeverityLoopProtect.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityLoopProtect.setStatus(_A)
class _Xgs360028fTrapEventSeverityMgmtIPChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityMgmtIPChange_Type.__name__=_B
_Xgs360028fTrapEventSeverityMgmtIPChange_Object=MibScalar
xgs360028fTrapEventSeverityMgmtIPChange=_Xgs360028fTrapEventSeverityMgmtIPChange_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,14),_Xgs360028fTrapEventSeverityMgmtIPChange_Type())
xgs360028fTrapEventSeverityMgmtIPChange.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityMgmtIPChange.setStatus(_A)
class _Xgs360028fTrapEventSeverityModuleChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityModuleChange_Type.__name__=_B
_Xgs360028fTrapEventSeverityModuleChange_Object=MibScalar
xgs360028fTrapEventSeverityModuleChange=_Xgs360028fTrapEventSeverityModuleChange_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,15),_Xgs360028fTrapEventSeverityModuleChange_Type())
xgs360028fTrapEventSeverityModuleChange.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityModuleChange.setStatus(_A)
class _Xgs360028fTrapEventSeverityNAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityNAS_Type.__name__=_B
_Xgs360028fTrapEventSeverityNAS_Object=MibScalar
xgs360028fTrapEventSeverityNAS=_Xgs360028fTrapEventSeverityNAS_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,16),_Xgs360028fTrapEventSeverityNAS_Type())
xgs360028fTrapEventSeverityNAS.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityNAS.setStatus(_A)
class _Xgs360028fTrapEventSeverityPasswdChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityPasswdChange_Type.__name__=_B
_Xgs360028fTrapEventSeverityPasswdChange_Object=MibScalar
xgs360028fTrapEventSeverityPasswdChange=_Xgs360028fTrapEventSeverityPasswdChange_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,17),_Xgs360028fTrapEventSeverityPasswdChange_Type())
xgs360028fTrapEventSeverityPasswdChange.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityPasswdChange.setStatus(_A)
class _Xgs360028fTrapEventSeverityPortSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityPortSecurity_Type.__name__=_B
_Xgs360028fTrapEventSeverityPortSecurity_Object=MibScalar
xgs360028fTrapEventSeverityPortSecurity=_Xgs360028fTrapEventSeverityPortSecurity_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,18),_Xgs360028fTrapEventSeverityPortSecurity_Type())
xgs360028fTrapEventSeverityPortSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityPortSecurity.setStatus(_A)
class _Xgs360028fTrapEventSeverityThermalProtect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityThermalProtect_Type.__name__=_B
_Xgs360028fTrapEventSeverityThermalProtect_Object=MibScalar
xgs360028fTrapEventSeverityThermalProtect=_Xgs360028fTrapEventSeverityThermalProtect_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,19),_Xgs360028fTrapEventSeverityThermalProtect_Type())
xgs360028fTrapEventSeverityThermalProtect.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityThermalProtect.setStatus(_A)
class _Xgs360028fTrapEventSeverityVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityVLAN_Type.__name__=_B
_Xgs360028fTrapEventSeverityVLAN_Object=MibScalar
xgs360028fTrapEventSeverityVLAN=_Xgs360028fTrapEventSeverityVLAN_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,20),_Xgs360028fTrapEventSeverityVLAN_Type())
xgs360028fTrapEventSeverityVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityVLAN.setStatus(_A)
class _Xgs360028fTrapEventSeverityWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fTrapEventSeverityWarmStart_Type.__name__=_B
_Xgs360028fTrapEventSeverityWarmStart_Object=MibScalar
xgs360028fTrapEventSeverityWarmStart=_Xgs360028fTrapEventSeverityWarmStart_Object((1,3,6,1,4,1,890,1,5,8,78,2,7,21),_Xgs360028fTrapEventSeverityWarmStart_Type())
xgs360028fTrapEventSeverityWarmStart.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTrapEventSeverityWarmStart.setStatus(_A)
_Xgs360028fSMTP_ObjectIdentity=ObjectIdentity
xgs360028fSMTP=_Xgs360028fSMTP_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,8))
_Xgs360028fSMTPMailServer_Type=DisplayString
_Xgs360028fSMTPMailServer_Object=MibScalar
xgs360028fSMTPMailServer=_Xgs360028fSMTPMailServer_Object((1,3,6,1,4,1,890,1,5,8,78,2,8,1),_Xgs360028fSMTPMailServer_Type())
xgs360028fSMTPMailServer.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSMTPMailServer.setStatus(_A)
_Xgs360028fSMTPUserName_Type=DisplayString
_Xgs360028fSMTPUserName_Object=MibScalar
xgs360028fSMTPUserName=_Xgs360028fSMTPUserName_Object((1,3,6,1,4,1,890,1,5,8,78,2,8,2),_Xgs360028fSMTPUserName_Type())
xgs360028fSMTPUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSMTPUserName.setStatus(_A)
_Xgs360028fSMTPPassword_Type=DisplayString
_Xgs360028fSMTPPassword_Object=MibScalar
xgs360028fSMTPPassword=_Xgs360028fSMTPPassword_Object((1,3,6,1,4,1,890,1,5,8,78,2,8,3),_Xgs360028fSMTPPassword_Type())
xgs360028fSMTPPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSMTPPassword.setStatus(_A)
class _Xgs360028fSMTPServeriryLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Xgs360028fSMTPServeriryLevel_Type.__name__=_B
_Xgs360028fSMTPServeriryLevel_Object=MibScalar
xgs360028fSMTPServeriryLevel=_Xgs360028fSMTPServeriryLevel_Object((1,3,6,1,4,1,890,1,5,8,78,2,8,4),_Xgs360028fSMTPServeriryLevel_Type())
xgs360028fSMTPServeriryLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSMTPServeriryLevel.setStatus(_A)
_Xgs360028fSMTPSender_Type=DisplayString
_Xgs360028fSMTPSender_Object=MibScalar
xgs360028fSMTPSender=_Xgs360028fSMTPSender_Object((1,3,6,1,4,1,890,1,5,8,78,2,8,5),_Xgs360028fSMTPSender_Type())
xgs360028fSMTPSender.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSMTPSender.setStatus(_A)
_Xgs360028fSMTPReturnPath_Type=DisplayString
_Xgs360028fSMTPReturnPath_Object=MibScalar
xgs360028fSMTPReturnPath=_Xgs360028fSMTPReturnPath_Object((1,3,6,1,4,1,890,1,5,8,78,2,8,6),_Xgs360028fSMTPReturnPath_Type())
xgs360028fSMTPReturnPath.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSMTPReturnPath.setStatus(_A)
_Xgs360028fSMTPEmailAddress1_Type=DisplayString
_Xgs360028fSMTPEmailAddress1_Object=MibScalar
xgs360028fSMTPEmailAddress1=_Xgs360028fSMTPEmailAddress1_Object((1,3,6,1,4,1,890,1,5,8,78,2,8,7),_Xgs360028fSMTPEmailAddress1_Type())
xgs360028fSMTPEmailAddress1.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSMTPEmailAddress1.setStatus(_A)
_Xgs360028fSMTPEmailAddress2_Type=DisplayString
_Xgs360028fSMTPEmailAddress2_Object=MibScalar
xgs360028fSMTPEmailAddress2=_Xgs360028fSMTPEmailAddress2_Object((1,3,6,1,4,1,890,1,5,8,78,2,8,8),_Xgs360028fSMTPEmailAddress2_Type())
xgs360028fSMTPEmailAddress2.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSMTPEmailAddress2.setStatus(_A)
_Xgs360028fSMTPEmailAddress3_Type=DisplayString
_Xgs360028fSMTPEmailAddress3_Object=MibScalar
xgs360028fSMTPEmailAddress3=_Xgs360028fSMTPEmailAddress3_Object((1,3,6,1,4,1,890,1,5,8,78,2,8,9),_Xgs360028fSMTPEmailAddress3_Type())
xgs360028fSMTPEmailAddress3.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSMTPEmailAddress3.setStatus(_A)
_Xgs360028fSMTPEmailAddress4_Type=DisplayString
_Xgs360028fSMTPEmailAddress4_Object=MibScalar
xgs360028fSMTPEmailAddress4=_Xgs360028fSMTPEmailAddress4_Object((1,3,6,1,4,1,890,1,5,8,78,2,8,10),_Xgs360028fSMTPEmailAddress4_Type())
xgs360028fSMTPEmailAddress4.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSMTPEmailAddress4.setStatus(_A)
_Xgs360028fSMTPEmailAddress5_Type=DisplayString
_Xgs360028fSMTPEmailAddress5_Object=MibScalar
xgs360028fSMTPEmailAddress5=_Xgs360028fSMTPEmailAddress5_Object((1,3,6,1,4,1,890,1,5,8,78,2,8,11),_Xgs360028fSMTPEmailAddress5_Type())
xgs360028fSMTPEmailAddress5.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSMTPEmailAddress5.setStatus(_A)
_Xgs360028fSMTPEmailAddress6_Type=DisplayString
_Xgs360028fSMTPEmailAddress6_Object=MibScalar
xgs360028fSMTPEmailAddress6=_Xgs360028fSMTPEmailAddress6_Object((1,3,6,1,4,1,890,1,5,8,78,2,8,12),_Xgs360028fSMTPEmailAddress6_Type())
xgs360028fSMTPEmailAddress6.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSMTPEmailAddress6.setStatus(_A)
_Xgs360028fACL_ObjectIdentity=ObjectIdentity
xgs360028fACL=_Xgs360028fACL_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,9))
_Xgs360028fACLPortsConfTable_Object=MibTable
xgs360028fACLPortsConfTable=_Xgs360028fACLPortsConfTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,1))
if mibBuilder.loadTexts:xgs360028fACLPortsConfTable.setStatus(_A)
_Xgs360028fACLPortsConfEntry_Object=MibTableRow
xgs360028fACLPortsConfEntry=_Xgs360028fACLPortsConfEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,1,1))
xgs360028fACLPortsConfEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:xgs360028fACLPortsConfEntry.setStatus(_A)
class _Xgs360028fACLPortsConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fACLPortsConfPort_Type.__name__=_B
_Xgs360028fACLPortsConfPort_Object=MibTableColumn
xgs360028fACLPortsConfPort=_Xgs360028fACLPortsConfPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,1,1,1),_Xgs360028fACLPortsConfPort_Type())
xgs360028fACLPortsConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fACLPortsConfPort.setStatus(_A)
class _Xgs360028fACLPortsConfPolicyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360028fACLPortsConfPolicyID_Type.__name__=_B
_Xgs360028fACLPortsConfPolicyID_Object=MibTableColumn
xgs360028fACLPortsConfPolicyID=_Xgs360028fACLPortsConfPolicyID_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,1,1,2),_Xgs360028fACLPortsConfPolicyID_Type())
xgs360028fACLPortsConfPolicyID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLPortsConfPolicyID.setStatus(_A)
class _Xgs360028fACLPortsConfAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fACLPortsConfAction_Type.__name__=_B
_Xgs360028fACLPortsConfAction_Object=MibTableColumn
xgs360028fACLPortsConfAction=_Xgs360028fACLPortsConfAction_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,1,1,3),_Xgs360028fACLPortsConfAction_Type())
xgs360028fACLPortsConfAction.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLPortsConfAction.setStatus(_A)
class _Xgs360028fACLPortsConfRateLimiterID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_Xgs360028fACLPortsConfRateLimiterID_Type.__name__=_B
_Xgs360028fACLPortsConfRateLimiterID_Object=MibTableColumn
xgs360028fACLPortsConfRateLimiterID=_Xgs360028fACLPortsConfRateLimiterID_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,1,1,4),_Xgs360028fACLPortsConfRateLimiterID_Type())
xgs360028fACLPortsConfRateLimiterID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLPortsConfRateLimiterID.setStatus(_A)
class _Xgs360028fACLPortsConfPortRedirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_Xgs360028fACLPortsConfPortRedirect_Type.__name__=_B
_Xgs360028fACLPortsConfPortRedirect_Object=MibTableColumn
xgs360028fACLPortsConfPortRedirect=_Xgs360028fACLPortsConfPortRedirect_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,1,1,5),_Xgs360028fACLPortsConfPortRedirect_Type())
xgs360028fACLPortsConfPortRedirect.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLPortsConfPortRedirect.setStatus(_A)
class _Xgs360028fACLPortsConfLogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fACLPortsConfLogging_Type.__name__=_B
_Xgs360028fACLPortsConfLogging_Object=MibTableColumn
xgs360028fACLPortsConfLogging=_Xgs360028fACLPortsConfLogging_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,1,1,7),_Xgs360028fACLPortsConfLogging_Type())
xgs360028fACLPortsConfLogging.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLPortsConfLogging.setStatus(_A)
class _Xgs360028fACLPortsConfShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fACLPortsConfShutdown_Type.__name__=_B
_Xgs360028fACLPortsConfShutdown_Object=MibTableColumn
xgs360028fACLPortsConfShutdown=_Xgs360028fACLPortsConfShutdown_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,1,1,8),_Xgs360028fACLPortsConfShutdown_Type())
xgs360028fACLPortsConfShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLPortsConfShutdown.setStatus(_A)
class _Xgs360028fACLPortsConfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fACLPortsConfState_Type.__name__=_B
_Xgs360028fACLPortsConfState_Object=MibTableColumn
xgs360028fACLPortsConfState=_Xgs360028fACLPortsConfState_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,1,1,9),_Xgs360028fACLPortsConfState_Type())
xgs360028fACLPortsConfState.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLPortsConfState.setStatus(_A)
_Xgs360028fACLPortsConfCounter_Type=Counter32
_Xgs360028fACLPortsConfCounter_Object=MibTableColumn
xgs360028fACLPortsConfCounter=_Xgs360028fACLPortsConfCounter_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,1,1,10),_Xgs360028fACLPortsConfCounter_Type())
xgs360028fACLPortsConfCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fACLPortsConfCounter.setStatus(_A)
_Xgs360028fACLRateLimiterTable_Object=MibTable
xgs360028fACLRateLimiterTable=_Xgs360028fACLRateLimiterTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,2))
if mibBuilder.loadTexts:xgs360028fACLRateLimiterTable.setStatus(_A)
_Xgs360028fACLRateLimiterEntry_Object=MibTableRow
xgs360028fACLRateLimiterEntry=_Xgs360028fACLRateLimiterEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,2,1))
xgs360028fACLRateLimiterEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:xgs360028fACLRateLimiterEntry.setStatus(_A)
class _Xgs360028fACLRateLimiterID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Xgs360028fACLRateLimiterID_Type.__name__=_B
_Xgs360028fACLRateLimiterID_Object=MibTableColumn
xgs360028fACLRateLimiterID=_Xgs360028fACLRateLimiterID_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,2,1,1),_Xgs360028fACLRateLimiterID_Type())
xgs360028fACLRateLimiterID.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fACLRateLimiterID.setStatus(_A)
class _Xgs360028fACLRateLimiterRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3276700))
_Xgs360028fACLRateLimiterRate_Type.__name__=_B
_Xgs360028fACLRateLimiterRate_Object=MibTableColumn
xgs360028fACLRateLimiterRate=_Xgs360028fACLRateLimiterRate_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,2,1,3),_Xgs360028fACLRateLimiterRate_Type())
xgs360028fACLRateLimiterRate.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLRateLimiterRate.setStatus(_A)
_Xgs360028fACLACE_ObjectIdentity=ObjectIdentity
xgs360028fACLACE=_Xgs360028fACLACE_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,9,3))
class _Xgs360028fACLACECreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fACLACECreate_Type.__name__=_B
_Xgs360028fACLACECreate_Object=MibScalar
xgs360028fACLACECreate=_Xgs360028fACLACECreate_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,1),_Xgs360028fACLACECreate_Type())
xgs360028fACLACECreate.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACECreate.setStatus(_A)
_Xgs360028fACLACETable_Object=MibTable
xgs360028fACLACETable=_Xgs360028fACLACETable_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2))
if mibBuilder.loadTexts:xgs360028fACLACETable.setStatus(_A)
_Xgs360028fACLACEEntry_Object=MibTableRow
xgs360028fACLACEEntry=_Xgs360028fACLACEEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1))
xgs360028fACLACEEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:xgs360028fACLACEEntry.setStatus(_A)
class _Xgs360028fACLACEIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Xgs360028fACLACEIndex_Type.__name__=_B
_Xgs360028fACLACEIndex_Object=MibTableColumn
xgs360028fACLACEIndex=_Xgs360028fACLACEIndex_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,1),_Xgs360028fACLACEIndex_Type())
xgs360028fACLACEIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fACLACEIndex.setStatus(_A)
class _Xgs360028fACLACEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Xgs360028fACLACEID_Type.__name__=_B
_Xgs360028fACLACEID_Object=MibTableColumn
xgs360028fACLACEID=_Xgs360028fACLACEID_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,2),_Xgs360028fACLACEID_Type())
xgs360028fACLACEID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEID.setStatus(_A)
class _Xgs360028fACLACENextID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Xgs360028fACLACENextID_Type.__name__=_B
_Xgs360028fACLACENextID_Object=MibTableColumn
xgs360028fACLACENextID=_Xgs360028fACLACENextID_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,3),_Xgs360028fACLACENextID_Type())
xgs360028fACLACENextID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACENextID.setStatus(_A)
_Xgs360028fACLACEIngressPort_Type=DisplayString
_Xgs360028fACLACEIngressPort_Object=MibTableColumn
xgs360028fACLACEIngressPort=_Xgs360028fACLACEIngressPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,4),_Xgs360028fACLACEIngressPort_Type())
xgs360028fACLACEIngressPort.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEIngressPort.setStatus(_A)
class _Xgs360028fACLACEPortPolicyNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360028fACLACEPortPolicyNumber_Type.__name__=_B
_Xgs360028fACLACEPortPolicyNumber_Object=MibTableColumn
xgs360028fACLACEPortPolicyNumber=_Xgs360028fACLACEPortPolicyNumber_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,5),_Xgs360028fACLACEPortPolicyNumber_Type())
xgs360028fACLACEPortPolicyNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEPortPolicyNumber.setStatus(_A)
class _Xgs360028fACLACEPortPolicyBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Xgs360028fACLACEPortPolicyBitmask_Type.__name__=_B
_Xgs360028fACLACEPortPolicyBitmask_Object=MibTableColumn
xgs360028fACLACEPortPolicyBitmask=_Xgs360028fACLACEPortPolicyBitmask_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,6),_Xgs360028fACLACEPortPolicyBitmask_Type())
xgs360028fACLACEPortPolicyBitmask.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEPortPolicyBitmask.setStatus(_A)
class _Xgs360028fACLACEFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_Xgs360028fACLACEFrameType_Type.__name__=_B
_Xgs360028fACLACEFrameType_Object=MibTableColumn
xgs360028fACLACEFrameType=_Xgs360028fACLACEFrameType_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,7),_Xgs360028fACLACEFrameType_Type())
xgs360028fACLACEFrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEFrameType.setStatus(_A)
class _Xgs360028fACLACEAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fACLACEAction_Type.__name__=_B
_Xgs360028fACLACEAction_Object=MibTableColumn
xgs360028fACLACEAction=_Xgs360028fACLACEAction_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,8),_Xgs360028fACLACEAction_Type())
xgs360028fACLACEAction.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEAction.setStatus(_A)
_Xgs360028fACLACEDenyPortRedirect_Type=DisplayString
_Xgs360028fACLACEDenyPortRedirect_Object=MibTableColumn
xgs360028fACLACEDenyPortRedirect=_Xgs360028fACLACEDenyPortRedirect_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,9),_Xgs360028fACLACEDenyPortRedirect_Type())
xgs360028fACLACEDenyPortRedirect.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEDenyPortRedirect.setStatus(_A)
class _Xgs360028fACLACELogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fACLACELogging_Type.__name__=_B
_Xgs360028fACLACELogging_Object=MibTableColumn
xgs360028fACLACELogging=_Xgs360028fACLACELogging_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,10),_Xgs360028fACLACELogging_Type())
xgs360028fACLACELogging.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACELogging.setStatus(_A)
class _Xgs360028fACLACERateLimiter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_Xgs360028fACLACERateLimiter_Type.__name__=_B
_Xgs360028fACLACERateLimiter_Object=MibTableColumn
xgs360028fACLACERateLimiter=_Xgs360028fACLACERateLimiter_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,12),_Xgs360028fACLACERateLimiter_Type())
xgs360028fACLACERateLimiter.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACERateLimiter.setStatus(_A)
class _Xgs360028fACLACEShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fACLACEShutdown_Type.__name__=_B
_Xgs360028fACLACEShutdown_Object=MibTableColumn
xgs360028fACLACEShutdown=_Xgs360028fACLACEShutdown_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,13),_Xgs360028fACLACEShutdown_Type())
xgs360028fACLACEShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEShutdown.setStatus(_A)
class _Xgs360028fACLACEVLANTagPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_Xgs360028fACLACEVLANTagPriority_Type.__name__=_B
_Xgs360028fACLACEVLANTagPriority_Object=MibTableColumn
xgs360028fACLACEVLANTagPriority=_Xgs360028fACLACEVLANTagPriority_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,15),_Xgs360028fACLACEVLANTagPriority_Type())
xgs360028fACLACEVLANTagPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEVLANTagPriority.setStatus(_A)
class _Xgs360028fACLACEVLANVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Xgs360028fACLACEVLANVID_Type.__name__=_B
_Xgs360028fACLACEVLANVID_Object=MibTableColumn
xgs360028fACLACEVLANVID=_Xgs360028fACLACEVLANVID_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,16),_Xgs360028fACLACEVLANVID_Type())
xgs360028fACLACEVLANVID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEVLANVID.setStatus(_A)
class _Xgs360028fACLACEEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Xgs360028fACLACEEtherType_Type.__name__=_B
_Xgs360028fACLACEEtherType_Object=MibTableColumn
xgs360028fACLACEEtherType=_Xgs360028fACLACEEtherType_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,17),_Xgs360028fACLACEEtherType_Type())
xgs360028fACLACEEtherType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEEtherType.setStatus(_A)
_Xgs360028fACLACESMAC_Type=DisplayString
_Xgs360028fACLACESMAC_Object=MibTableColumn
xgs360028fACLACESMAC=_Xgs360028fACLACESMAC_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,18),_Xgs360028fACLACESMAC_Type())
xgs360028fACLACESMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACESMAC.setStatus(_A)
class _Xgs360028fACLACEDMACType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Xgs360028fACLACEDMACType_Type.__name__=_B
_Xgs360028fACLACEDMACType_Object=MibTableColumn
xgs360028fACLACEDMACType=_Xgs360028fACLACEDMACType_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,19),_Xgs360028fACLACEDMACType_Type())
xgs360028fACLACEDMACType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEDMACType.setStatus(_A)
_Xgs360028fACLACEDMAC_Type=DisplayString
_Xgs360028fACLACEDMAC_Object=MibTableColumn
xgs360028fACLACEDMAC=_Xgs360028fACLACEDMAC_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,20),_Xgs360028fACLACEDMAC_Type())
xgs360028fACLACEDMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEDMAC.setStatus(_A)
class _Xgs360028fACLACEArpOpcode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360028fACLACEArpOpcode_Type.__name__=_B
_Xgs360028fACLACEArpOpcode_Object=MibTableColumn
xgs360028fACLACEArpOpcode=_Xgs360028fACLACEArpOpcode_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,21),_Xgs360028fACLACEArpOpcode_Type())
xgs360028fACLACEArpOpcode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEArpOpcode.setStatus(_A)
class _Xgs360028fACLACEArpFlagsRequestReply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fACLACEArpFlagsRequestReply_Type.__name__=_B
_Xgs360028fACLACEArpFlagsRequestReply_Object=MibTableColumn
xgs360028fACLACEArpFlagsRequestReply=_Xgs360028fACLACEArpFlagsRequestReply_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,22),_Xgs360028fACLACEArpFlagsRequestReply_Type())
xgs360028fACLACEArpFlagsRequestReply.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEArpFlagsRequestReply.setStatus(_A)
class _Xgs360028fACLACEArpFlagsArpSmac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fACLACEArpFlagsArpSmac_Type.__name__=_B
_Xgs360028fACLACEArpFlagsArpSmac_Object=MibTableColumn
xgs360028fACLACEArpFlagsArpSmac=_Xgs360028fACLACEArpFlagsArpSmac_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,23),_Xgs360028fACLACEArpFlagsArpSmac_Type())
xgs360028fACLACEArpFlagsArpSmac.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEArpFlagsArpSmac.setStatus(_A)
class _Xgs360028fACLACEArpFlagsRarpDmac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fACLACEArpFlagsRarpDmac_Type.__name__=_B
_Xgs360028fACLACEArpFlagsRarpDmac_Object=MibTableColumn
xgs360028fACLACEArpFlagsRarpDmac=_Xgs360028fACLACEArpFlagsRarpDmac_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,24),_Xgs360028fACLACEArpFlagsRarpDmac_Type())
xgs360028fACLACEArpFlagsRarpDmac.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEArpFlagsRarpDmac.setStatus(_A)
class _Xgs360028fACLACEArpFlagsLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fACLACEArpFlagsLength_Type.__name__=_B
_Xgs360028fACLACEArpFlagsLength_Object=MibTableColumn
xgs360028fACLACEArpFlagsLength=_Xgs360028fACLACEArpFlagsLength_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,25),_Xgs360028fACLACEArpFlagsLength_Type())
xgs360028fACLACEArpFlagsLength.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEArpFlagsLength.setStatus(_A)
class _Xgs360028fACLACEArpFlagsIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fACLACEArpFlagsIp_Type.__name__=_B
_Xgs360028fACLACEArpFlagsIp_Object=MibTableColumn
xgs360028fACLACEArpFlagsIp=_Xgs360028fACLACEArpFlagsIp_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,26),_Xgs360028fACLACEArpFlagsIp_Type())
xgs360028fACLACEArpFlagsIp.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEArpFlagsIp.setStatus(_A)
class _Xgs360028fACLACEArpFlagsEthernet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fACLACEArpFlagsEthernet_Type.__name__=_B
_Xgs360028fACLACEArpFlagsEthernet_Object=MibTableColumn
xgs360028fACLACEArpFlagsEthernet=_Xgs360028fACLACEArpFlagsEthernet_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,27),_Xgs360028fACLACEArpFlagsEthernet_Type())
xgs360028fACLACEArpFlagsEthernet.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEArpFlagsEthernet.setStatus(_A)
class _Xgs360028fACLACESIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fACLACESIPType_Type.__name__=_B
_Xgs360028fACLACESIPType_Object=MibTableColumn
xgs360028fACLACESIPType=_Xgs360028fACLACESIPType_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,28),_Xgs360028fACLACESIPType_Type())
xgs360028fACLACESIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACESIPType.setStatus(_A)
_Xgs360028fACLACESIPIPAddress_Type=IpAddress
_Xgs360028fACLACESIPIPAddress_Object=MibTableColumn
xgs360028fACLACESIPIPAddress=_Xgs360028fACLACESIPIPAddress_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,29),_Xgs360028fACLACESIPIPAddress_Type())
xgs360028fACLACESIPIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACESIPIPAddress.setStatus(_A)
class _Xgs360028fACLACESIPNetworkPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Xgs360028fACLACESIPNetworkPrefix_Type.__name__=_B
_Xgs360028fACLACESIPNetworkPrefix_Object=MibTableColumn
xgs360028fACLACESIPNetworkPrefix=_Xgs360028fACLACESIPNetworkPrefix_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,30),_Xgs360028fACLACESIPNetworkPrefix_Type())
xgs360028fACLACESIPNetworkPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACESIPNetworkPrefix.setStatus(_A)
class _Xgs360028fACLACEDIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fACLACEDIPType_Type.__name__=_B
_Xgs360028fACLACEDIPType_Object=MibTableColumn
xgs360028fACLACEDIPType=_Xgs360028fACLACEDIPType_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,32),_Xgs360028fACLACEDIPType_Type())
xgs360028fACLACEDIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEDIPType.setStatus(_A)
_Xgs360028fACLACEDIPIPAddress_Type=IpAddress
_Xgs360028fACLACEDIPIPAddress_Object=MibTableColumn
xgs360028fACLACEDIPIPAddress=_Xgs360028fACLACEDIPIPAddress_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,33),_Xgs360028fACLACEDIPIPAddress_Type())
xgs360028fACLACEDIPIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEDIPIPAddress.setStatus(_A)
class _Xgs360028fACLACEDIPNetworkPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Xgs360028fACLACEDIPNetworkPrefix_Type.__name__=_B
_Xgs360028fACLACEDIPNetworkPrefix_Object=MibTableColumn
xgs360028fACLACEDIPNetworkPrefix=_Xgs360028fACLACEDIPNetworkPrefix_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,34),_Xgs360028fACLACEDIPNetworkPrefix_Type())
xgs360028fACLACEDIPNetworkPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEDIPNetworkPrefix.setStatus(_A)
class _Xgs360028fACLACEIPProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Xgs360028fACLACEIPProtocol_Type.__name__=_B
_Xgs360028fACLACEIPProtocol_Object=MibTableColumn
xgs360028fACLACEIPProtocol=_Xgs360028fACLACEIPProtocol_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,36),_Xgs360028fACLACEIPProtocol_Type())
xgs360028fACLACEIPProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEIPProtocol.setStatus(_A)
class _Xgs360028fACLACEIPFlagsTTL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fACLACEIPFlagsTTL_Type.__name__=_B
_Xgs360028fACLACEIPFlagsTTL_Object=MibTableColumn
xgs360028fACLACEIPFlagsTTL=_Xgs360028fACLACEIPFlagsTTL_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,37),_Xgs360028fACLACEIPFlagsTTL_Type())
xgs360028fACLACEIPFlagsTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEIPFlagsTTL.setStatus(_A)
class _Xgs360028fACLACEIPFlagsOptions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fACLACEIPFlagsOptions_Type.__name__=_B
_Xgs360028fACLACEIPFlagsOptions_Object=MibTableColumn
xgs360028fACLACEIPFlagsOptions=_Xgs360028fACLACEIPFlagsOptions_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,38),_Xgs360028fACLACEIPFlagsOptions_Type())
xgs360028fACLACEIPFlagsOptions.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEIPFlagsOptions.setStatus(_A)
class _Xgs360028fACLACEIPFlagsFragment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fACLACEIPFlagsFragment_Type.__name__=_B
_Xgs360028fACLACEIPFlagsFragment_Object=MibTableColumn
xgs360028fACLACEIPFlagsFragment=_Xgs360028fACLACEIPFlagsFragment_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,39),_Xgs360028fACLACEIPFlagsFragment_Type())
xgs360028fACLACEIPFlagsFragment.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEIPFlagsFragment.setStatus(_A)
class _Xgs360028fACLACEICMPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Xgs360028fACLACEICMPType_Type.__name__=_B
_Xgs360028fACLACEICMPType_Object=MibTableColumn
xgs360028fACLACEICMPType=_Xgs360028fACLACEICMPType_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,40),_Xgs360028fACLACEICMPType_Type())
xgs360028fACLACEICMPType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEICMPType.setStatus(_A)
class _Xgs360028fACLACEICMPCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Xgs360028fACLACEICMPCode_Type.__name__=_B
_Xgs360028fACLACEICMPCode_Object=MibTableColumn
xgs360028fACLACEICMPCode=_Xgs360028fACLACEICMPCode_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,41),_Xgs360028fACLACEICMPCode_Type())
xgs360028fACLACEICMPCode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEICMPCode.setStatus(_A)
class _Xgs360028fACLACESourcePortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Xgs360028fACLACESourcePortMin_Type.__name__=_B
_Xgs360028fACLACESourcePortMin_Object=MibTableColumn
xgs360028fACLACESourcePortMin=_Xgs360028fACLACESourcePortMin_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,42),_Xgs360028fACLACESourcePortMin_Type())
xgs360028fACLACESourcePortMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACESourcePortMin.setStatus(_A)
class _Xgs360028fACLACESourcePortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Xgs360028fACLACESourcePortMax_Type.__name__=_B
_Xgs360028fACLACESourcePortMax_Object=MibTableColumn
xgs360028fACLACESourcePortMax=_Xgs360028fACLACESourcePortMax_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,43),_Xgs360028fACLACESourcePortMax_Type())
xgs360028fACLACESourcePortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACESourcePortMax.setStatus(_A)
class _Xgs360028fACLACEDestPortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Xgs360028fACLACEDestPortMin_Type.__name__=_B
_Xgs360028fACLACEDestPortMin_Object=MibTableColumn
xgs360028fACLACEDestPortMin=_Xgs360028fACLACEDestPortMin_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,44),_Xgs360028fACLACEDestPortMin_Type())
xgs360028fACLACEDestPortMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEDestPortMin.setStatus(_A)
class _Xgs360028fACLACEDestPortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Xgs360028fACLACEDestPortMax_Type.__name__=_B
_Xgs360028fACLACEDestPortMax_Object=MibTableColumn
xgs360028fACLACEDestPortMax=_Xgs360028fACLACEDestPortMax_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,45),_Xgs360028fACLACEDestPortMax_Type())
xgs360028fACLACEDestPortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEDestPortMax.setStatus(_A)
class _Xgs360028fACLACETCPFlagsFin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fACLACETCPFlagsFin_Type.__name__=_B
_Xgs360028fACLACETCPFlagsFin_Object=MibTableColumn
xgs360028fACLACETCPFlagsFin=_Xgs360028fACLACETCPFlagsFin_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,46),_Xgs360028fACLACETCPFlagsFin_Type())
xgs360028fACLACETCPFlagsFin.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACETCPFlagsFin.setStatus(_A)
class _Xgs360028fACLACETCPFlagsSyn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fACLACETCPFlagsSyn_Type.__name__=_B
_Xgs360028fACLACETCPFlagsSyn_Object=MibTableColumn
xgs360028fACLACETCPFlagsSyn=_Xgs360028fACLACETCPFlagsSyn_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,47),_Xgs360028fACLACETCPFlagsSyn_Type())
xgs360028fACLACETCPFlagsSyn.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACETCPFlagsSyn.setStatus(_A)
class _Xgs360028fACLACETCPFlagsRst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fACLACETCPFlagsRst_Type.__name__=_B
_Xgs360028fACLACETCPFlagsRst_Object=MibTableColumn
xgs360028fACLACETCPFlagsRst=_Xgs360028fACLACETCPFlagsRst_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,48),_Xgs360028fACLACETCPFlagsRst_Type())
xgs360028fACLACETCPFlagsRst.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACETCPFlagsRst.setStatus(_A)
class _Xgs360028fACLACETCPFlagsPsh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fACLACETCPFlagsPsh_Type.__name__=_B
_Xgs360028fACLACETCPFlagsPsh_Object=MibTableColumn
xgs360028fACLACETCPFlagsPsh=_Xgs360028fACLACETCPFlagsPsh_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,49),_Xgs360028fACLACETCPFlagsPsh_Type())
xgs360028fACLACETCPFlagsPsh.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACETCPFlagsPsh.setStatus(_A)
class _Xgs360028fACLACETCPFlagsAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fACLACETCPFlagsAck_Type.__name__=_B
_Xgs360028fACLACETCPFlagsAck_Object=MibTableColumn
xgs360028fACLACETCPFlagsAck=_Xgs360028fACLACETCPFlagsAck_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,50),_Xgs360028fACLACETCPFlagsAck_Type())
xgs360028fACLACETCPFlagsAck.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACETCPFlagsAck.setStatus(_A)
class _Xgs360028fACLACETCPFlagsUrg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fACLACETCPFlagsUrg_Type.__name__=_B
_Xgs360028fACLACETCPFlagsUrg_Object=MibTableColumn
xgs360028fACLACETCPFlagsUrg=_Xgs360028fACLACETCPFlagsUrg_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,51),_Xgs360028fACLACETCPFlagsUrg_Type())
xgs360028fACLACETCPFlagsUrg.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACETCPFlagsUrg.setStatus(_A)
class _Xgs360028fACLACERowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360028fACLACERowStatus_Type.__name__=_B
_Xgs360028fACLACERowStatus_Object=MibTableColumn
xgs360028fACLACERowStatus=_Xgs360028fACLACERowStatus_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,2,1,66),_Xgs360028fACLACERowStatus_Type())
xgs360028fACLACERowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACERowStatus.setStatus(_A)
class _Xgs360028fACLACEClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fACLACEClear_Type.__name__=_B
_Xgs360028fACLACEClear_Object=MibScalar
xgs360028fACLACEClear=_Xgs360028fACLACEClear_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,3),_Xgs360028fACLACEClear_Type())
xgs360028fACLACEClear.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEClear.setStatus(_A)
class _Xgs360028fACLACEMoveACEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Xgs360028fACLACEMoveACEID_Type.__name__=_B
_Xgs360028fACLACEMoveACEID_Object=MibScalar
xgs360028fACLACEMoveACEID=_Xgs360028fACLACEMoveACEID_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,4),_Xgs360028fACLACEMoveACEID_Type())
xgs360028fACLACEMoveACEID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEMoveACEID.setStatus(_A)
class _Xgs360028fACLACEMoveNextACEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Xgs360028fACLACEMoveNextACEID_Type.__name__=_B
_Xgs360028fACLACEMoveNextACEID_Object=MibScalar
xgs360028fACLACEMoveNextACEID=_Xgs360028fACLACEMoveNextACEID_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,5),_Xgs360028fACLACEMoveNextACEID_Type())
xgs360028fACLACEMoveNextACEID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fACLACEMoveNextACEID.setStatus(_A)
_Xgs360028fACLACEStatusTable_Object=MibTable
xgs360028fACLACEStatusTable=_Xgs360028fACLACEStatusTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,6))
if mibBuilder.loadTexts:xgs360028fACLACEStatusTable.setStatus(_A)
_Xgs360028fACLACEStatusEntry_Object=MibTableRow
xgs360028fACLACEStatusEntry=_Xgs360028fACLACEStatusEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,6,1))
xgs360028fACLACEStatusEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:xgs360028fACLACEStatusEntry.setStatus(_A)
class _Xgs360028fACLACEStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Xgs360028fACLACEStatusIndex_Type.__name__=_B
_Xgs360028fACLACEStatusIndex_Object=MibTableColumn
xgs360028fACLACEStatusIndex=_Xgs360028fACLACEStatusIndex_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,6,1,1),_Xgs360028fACLACEStatusIndex_Type())
xgs360028fACLACEStatusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fACLACEStatusIndex.setStatus(_A)
_Xgs360028fACLACEStatusUser_Type=DisplayString
_Xgs360028fACLACEStatusUser_Object=MibTableColumn
xgs360028fACLACEStatusUser=_Xgs360028fACLACEStatusUser_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,6,1,2),_Xgs360028fACLACEStatusUser_Type())
xgs360028fACLACEStatusUser.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fACLACEStatusUser.setStatus(_A)
class _Xgs360028fACLACEStatusID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Xgs360028fACLACEStatusID_Type.__name__=_B
_Xgs360028fACLACEStatusID_Object=MibTableColumn
xgs360028fACLACEStatusID=_Xgs360028fACLACEStatusID_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,6,1,3),_Xgs360028fACLACEStatusID_Type())
xgs360028fACLACEStatusID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fACLACEStatusID.setStatus(_A)
_Xgs360028fACLACEStatusIngressPort_Type=DisplayString
_Xgs360028fACLACEStatusIngressPort_Object=MibTableColumn
xgs360028fACLACEStatusIngressPort=_Xgs360028fACLACEStatusIngressPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,6,1,4),_Xgs360028fACLACEStatusIngressPort_Type())
xgs360028fACLACEStatusIngressPort.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fACLACEStatusIngressPort.setStatus(_A)
_Xgs360028fACLACEStatusFrameType_Type=DisplayString
_Xgs360028fACLACEStatusFrameType_Object=MibTableColumn
xgs360028fACLACEStatusFrameType=_Xgs360028fACLACEStatusFrameType_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,6,1,5),_Xgs360028fACLACEStatusFrameType_Type())
xgs360028fACLACEStatusFrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fACLACEStatusFrameType.setStatus(_A)
_Xgs360028fACLACEStatusAction_Type=DisplayString
_Xgs360028fACLACEStatusAction_Object=MibTableColumn
xgs360028fACLACEStatusAction=_Xgs360028fACLACEStatusAction_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,6,1,6),_Xgs360028fACLACEStatusAction_Type())
xgs360028fACLACEStatusAction.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fACLACEStatusAction.setStatus(_A)
_Xgs360028fACLACEStatusRateLimiter_Type=DisplayString
_Xgs360028fACLACEStatusRateLimiter_Object=MibTableColumn
xgs360028fACLACEStatusRateLimiter=_Xgs360028fACLACEStatusRateLimiter_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,6,1,7),_Xgs360028fACLACEStatusRateLimiter_Type())
xgs360028fACLACEStatusRateLimiter.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fACLACEStatusRateLimiter.setStatus(_A)
_Xgs360028fACLACEStatusPortCopy_Type=DisplayString
_Xgs360028fACLACEStatusPortCopy_Object=MibTableColumn
xgs360028fACLACEStatusPortCopy=_Xgs360028fACLACEStatusPortCopy_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,6,1,8),_Xgs360028fACLACEStatusPortCopy_Type())
xgs360028fACLACEStatusPortCopy.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fACLACEStatusPortCopy.setStatus(_A)
_Xgs360028fACLACEStatusMirror_Type=DisplayString
_Xgs360028fACLACEStatusMirror_Object=MibTableColumn
xgs360028fACLACEStatusMirror=_Xgs360028fACLACEStatusMirror_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,6,1,9),_Xgs360028fACLACEStatusMirror_Type())
xgs360028fACLACEStatusMirror.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fACLACEStatusMirror.setStatus(_A)
_Xgs360028fACLACEStatusCPU_Type=DisplayString
_Xgs360028fACLACEStatusCPU_Object=MibTableColumn
xgs360028fACLACEStatusCPU=_Xgs360028fACLACEStatusCPU_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,6,1,10),_Xgs360028fACLACEStatusCPU_Type())
xgs360028fACLACEStatusCPU.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fACLACEStatusCPU.setStatus(_A)
_Xgs360028fACLACEStatusCounter_Type=Counter32
_Xgs360028fACLACEStatusCounter_Object=MibTableColumn
xgs360028fACLACEStatusCounter=_Xgs360028fACLACEStatusCounter_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,6,1,11),_Xgs360028fACLACEStatusCounter_Type())
xgs360028fACLACEStatusCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fACLACEStatusCounter.setStatus(_A)
_Xgs360028fACLACEStatusConflict_Type=DisplayString
_Xgs360028fACLACEStatusConflict_Object=MibTableColumn
xgs360028fACLACEStatusConflict=_Xgs360028fACLACEStatusConflict_Object((1,3,6,1,4,1,890,1,5,8,78,2,9,3,6,1,12),_Xgs360028fACLACEStatusConflict_Type())
xgs360028fACLACEStatusConflict.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fACLACEStatusConflict.setStatus(_A)
_Xgs360028fERPS_ObjectIdentity=ObjectIdentity
xgs360028fERPS=_Xgs360028fERPS_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,10))
_Xgs360028fERPSConf_ObjectIdentity=ObjectIdentity
xgs360028fERPSConf=_Xgs360028fERPSConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,10,1))
class _Xgs360028fERPSConfCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fERPSConfCreate_Type.__name__=_B
_Xgs360028fERPSConfCreate_Object=MibScalar
xgs360028fERPSConfCreate=_Xgs360028fERPSConfCreate_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,1),_Xgs360028fERPSConfCreate_Type())
xgs360028fERPSConfCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSConfCreate.setStatus(_A)
_Xgs360028fERPSConfTable_Object=MibTable
xgs360028fERPSConfTable=_Xgs360028fERPSConfTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2))
if mibBuilder.loadTexts:xgs360028fERPSConfTable.setStatus(_A)
_Xgs360028fERPSConfEntry_Object=MibTableRow
xgs360028fERPSConfEntry=_Xgs360028fERPSConfEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1))
xgs360028fERPSConfEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:xgs360028fERPSConfEntry.setStatus(_A)
class _Xgs360028fERPSConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Xgs360028fERPSConfIndex_Type.__name__=_B
_Xgs360028fERPSConfIndex_Object=MibTableColumn
xgs360028fERPSConfIndex=_Xgs360028fERPSConfIndex_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,1),_Xgs360028fERPSConfIndex_Type())
xgs360028fERPSConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fERPSConfIndex.setStatus(_A)
class _Xgs360028fERPSConfERPSID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Xgs360028fERPSConfERPSID_Type.__name__=_B
_Xgs360028fERPSConfERPSID_Object=MibTableColumn
xgs360028fERPSConfERPSID=_Xgs360028fERPSConfERPSID_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,2),_Xgs360028fERPSConfERPSID_Type())
xgs360028fERPSConfERPSID.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSConfERPSID.setStatus(_A)
class _Xgs360028fERPSConfPort0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Xgs360028fERPSConfPort0_Type.__name__=_B
_Xgs360028fERPSConfPort0_Object=MibTableColumn
xgs360028fERPSConfPort0=_Xgs360028fERPSConfPort0_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,3),_Xgs360028fERPSConfPort0_Type())
xgs360028fERPSConfPort0.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSConfPort0.setStatus(_A)
class _Xgs360028fERPSConfPort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,26))
_Xgs360028fERPSConfPort1_Type.__name__=_B
_Xgs360028fERPSConfPort1_Object=MibTableColumn
xgs360028fERPSConfPort1=_Xgs360028fERPSConfPort1_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,4),_Xgs360028fERPSConfPort1_Type())
xgs360028fERPSConfPort1.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSConfPort1.setStatus(_A)
class _Xgs360028fERPSConfPort0SFMEP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Xgs360028fERPSConfPort0SFMEP_Type.__name__=_B
_Xgs360028fERPSConfPort0SFMEP_Object=MibTableColumn
xgs360028fERPSConfPort0SFMEP=_Xgs360028fERPSConfPort0SFMEP_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,5),_Xgs360028fERPSConfPort0SFMEP_Type())
xgs360028fERPSConfPort0SFMEP.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSConfPort0SFMEP.setStatus(_A)
class _Xgs360028fERPSConfPort1SFMEP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_Xgs360028fERPSConfPort1SFMEP_Type.__name__=_B
_Xgs360028fERPSConfPort1SFMEP_Object=MibTableColumn
xgs360028fERPSConfPort1SFMEP=_Xgs360028fERPSConfPort1SFMEP_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,6),_Xgs360028fERPSConfPort1SFMEP_Type())
xgs360028fERPSConfPort1SFMEP.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSConfPort1SFMEP.setStatus(_A)
class _Xgs360028fERPSConfPort0APSMEP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Xgs360028fERPSConfPort0APSMEP_Type.__name__=_B
_Xgs360028fERPSConfPort0APSMEP_Object=MibTableColumn
xgs360028fERPSConfPort0APSMEP=_Xgs360028fERPSConfPort0APSMEP_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,7),_Xgs360028fERPSConfPort0APSMEP_Type())
xgs360028fERPSConfPort0APSMEP.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSConfPort0APSMEP.setStatus(_A)
class _Xgs360028fERPSConfPort1APSMEP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_Xgs360028fERPSConfPort1APSMEP_Type.__name__=_B
_Xgs360028fERPSConfPort1APSMEP_Object=MibTableColumn
xgs360028fERPSConfPort1APSMEP=_Xgs360028fERPSConfPort1APSMEP_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,8),_Xgs360028fERPSConfPort1APSMEP_Type())
xgs360028fERPSConfPort1APSMEP.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSConfPort1APSMEP.setStatus(_A)
class _Xgs360028fERPSConfRingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fERPSConfRingType_Type.__name__=_B
_Xgs360028fERPSConfRingType_Object=MibTableColumn
xgs360028fERPSConfRingType=_Xgs360028fERPSConfRingType_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,9),_Xgs360028fERPSConfRingType_Type())
xgs360028fERPSConfRingType.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSConfRingType.setStatus(_A)
class _Xgs360028fERPSConfInterconnectedNode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fERPSConfInterconnectedNode_Type.__name__=_B
_Xgs360028fERPSConfInterconnectedNode_Object=MibTableColumn
xgs360028fERPSConfInterconnectedNode=_Xgs360028fERPSConfInterconnectedNode_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,10),_Xgs360028fERPSConfInterconnectedNode_Type())
xgs360028fERPSConfInterconnectedNode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSConfInterconnectedNode.setStatus(_A)
class _Xgs360028fERPSConfVirtualChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fERPSConfVirtualChannel_Type.__name__=_B
_Xgs360028fERPSConfVirtualChannel_Object=MibTableColumn
xgs360028fERPSConfVirtualChannel=_Xgs360028fERPSConfVirtualChannel_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,11),_Xgs360028fERPSConfVirtualChannel_Type())
xgs360028fERPSConfVirtualChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSConfVirtualChannel.setStatus(_A)
class _Xgs360028fERPSConfMajorRingID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Xgs360028fERPSConfMajorRingID_Type.__name__=_B
_Xgs360028fERPSConfMajorRingID_Object=MibTableColumn
xgs360028fERPSConfMajorRingID=_Xgs360028fERPSConfMajorRingID_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,12),_Xgs360028fERPSConfMajorRingID_Type())
xgs360028fERPSConfMajorRingID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fERPSConfMajorRingID.setStatus(_A)
class _Xgs360028fERPSConfAlarm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Xgs360028fERPSConfAlarm_Type.__name__=_G
_Xgs360028fERPSConfAlarm_Object=MibTableColumn
xgs360028fERPSConfAlarm=_Xgs360028fERPSConfAlarm_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,13),_Xgs360028fERPSConfAlarm_Type())
xgs360028fERPSConfAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fERPSConfAlarm.setStatus(_A)
class _Xgs360028fERPSInstanceConfConfigured_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Xgs360028fERPSInstanceConfConfigured_Type.__name__=_G
_Xgs360028fERPSInstanceConfConfigured_Object=MibTableColumn
xgs360028fERPSInstanceConfConfigured=_Xgs360028fERPSInstanceConfConfigured_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,14),_Xgs360028fERPSInstanceConfConfigured_Type())
xgs360028fERPSInstanceConfConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fERPSInstanceConfConfigured.setStatus(_A)
class _Xgs360028fERPSInstanceConfGuardTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,2000))
_Xgs360028fERPSInstanceConfGuardTime_Type.__name__=_B
_Xgs360028fERPSInstanceConfGuardTime_Object=MibTableColumn
xgs360028fERPSInstanceConfGuardTime=_Xgs360028fERPSInstanceConfGuardTime_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,15),_Xgs360028fERPSInstanceConfGuardTime_Type())
xgs360028fERPSInstanceConfGuardTime.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSInstanceConfGuardTime.setStatus(_A)
class _Xgs360028fERPSInstanceConfWTRTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Xgs360028fERPSInstanceConfWTRTime_Type.__name__=_B
_Xgs360028fERPSInstanceConfWTRTime_Object=MibTableColumn
xgs360028fERPSInstanceConfWTRTime=_Xgs360028fERPSInstanceConfWTRTime_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,16),_Xgs360028fERPSInstanceConfWTRTime_Type())
xgs360028fERPSInstanceConfWTRTime.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSInstanceConfWTRTime.setStatus(_A)
class _Xgs360028fERPSInstanceConfHoldOffTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Xgs360028fERPSInstanceConfHoldOffTime_Type.__name__=_B
_Xgs360028fERPSInstanceConfHoldOffTime_Object=MibTableColumn
xgs360028fERPSInstanceConfHoldOffTime=_Xgs360028fERPSInstanceConfHoldOffTime_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,17),_Xgs360028fERPSInstanceConfHoldOffTime_Type())
xgs360028fERPSInstanceConfHoldOffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSInstanceConfHoldOffTime.setStatus(_A)
class _Xgs360028fERPSInstanceConfVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fERPSInstanceConfVersion_Type.__name__=_B
_Xgs360028fERPSInstanceConfVersion_Object=MibTableColumn
xgs360028fERPSInstanceConfVersion=_Xgs360028fERPSInstanceConfVersion_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,18),_Xgs360028fERPSInstanceConfVersion_Type())
xgs360028fERPSInstanceConfVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSInstanceConfVersion.setStatus(_A)
class _Xgs360028fERPSInstanceConfRevertive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fERPSInstanceConfRevertive_Type.__name__=_B
_Xgs360028fERPSInstanceConfRevertive_Object=MibTableColumn
xgs360028fERPSInstanceConfRevertive=_Xgs360028fERPSInstanceConfRevertive_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,19),_Xgs360028fERPSInstanceConfRevertive_Type())
xgs360028fERPSInstanceConfRevertive.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSInstanceConfRevertive.setStatus(_A)
class _Xgs360028fERPSInstanceConfVLANconfig_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Xgs360028fERPSInstanceConfVLANconfig_Type.__name__=_G
_Xgs360028fERPSInstanceConfVLANconfig_Object=MibTableColumn
xgs360028fERPSInstanceConfVLANconfig=_Xgs360028fERPSInstanceConfVLANconfig_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,20),_Xgs360028fERPSInstanceConfVLANconfig_Type())
xgs360028fERPSInstanceConfVLANconfig.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSInstanceConfVLANconfig.setStatus(_A)
class _Xgs360028fERPSConfRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360028fERPSConfRowStatus_Type.__name__=_B
_Xgs360028fERPSConfRowStatus_Object=MibTableColumn
xgs360028fERPSConfRowStatus=_Xgs360028fERPSConfRowStatus_Object((1,3,6,1,4,1,890,1,5,8,78,2,10,1,2,1,21),_Xgs360028fERPSConfRowStatus_Type())
xgs360028fERPSConfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fERPSConfRowStatus.setStatus(_A)
_Xgs360028fMRSTP_ObjectIdentity=ObjectIdentity
xgs360028fMRSTP=_Xgs360028fMRSTP_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,11))
_Xgs360028fMRSTPInstance_ObjectIdentity=ObjectIdentity
xgs360028fMRSTPInstance=_Xgs360028fMRSTPInstance_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,11,1))
_Xgs360028fMRSTPInstanceConf_ObjectIdentity=ObjectIdentity
xgs360028fMRSTPInstanceConf=_Xgs360028fMRSTPInstanceConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,11,1,1))
class _Xgs360028fMRSTPInstanceConfGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fMRSTPInstanceConfGlobalState_Type.__name__=_B
_Xgs360028fMRSTPInstanceConfGlobalState_Object=MibScalar
xgs360028fMRSTPInstanceConfGlobalState=_Xgs360028fMRSTPInstanceConfGlobalState_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,1,1),_Xgs360028fMRSTPInstanceConfGlobalState_Type())
xgs360028fMRSTPInstanceConfGlobalState.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceConfGlobalState.setStatus(_A)
_Xgs360028fMRSTPInstanceConfigurationTable_Object=MibTable
xgs360028fMRSTPInstanceConfigurationTable=_Xgs360028fMRSTPInstanceConfigurationTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,1,2))
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceConfigurationTable.setStatus(_A)
_Xgs360028fMRSTPInstanceConfigurationEntry_Object=MibTableRow
xgs360028fMRSTPInstanceConfigurationEntry=_Xgs360028fMRSTPInstanceConfigurationEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,1,2,1))
xgs360028fMRSTPInstanceConfigurationEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceConfigurationEntry.setStatus(_A)
class _Xgs360028fMRSTPInstanceConfigurationInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Xgs360028fMRSTPInstanceConfigurationInstance_Type.__name__=_B
_Xgs360028fMRSTPInstanceConfigurationInstance_Object=MibTableColumn
xgs360028fMRSTPInstanceConfigurationInstance=_Xgs360028fMRSTPInstanceConfigurationInstance_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,1,2,1,1),_Xgs360028fMRSTPInstanceConfigurationInstance_Type())
xgs360028fMRSTPInstanceConfigurationInstance.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceConfigurationInstance.setStatus(_A)
class _Xgs360028fMRSTPInstanceConfigurationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fMRSTPInstanceConfigurationState_Type.__name__=_B
_Xgs360028fMRSTPInstanceConfigurationState_Object=MibTableColumn
xgs360028fMRSTPInstanceConfigurationState=_Xgs360028fMRSTPInstanceConfigurationState_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,1,2,1,2),_Xgs360028fMRSTPInstanceConfigurationState_Type())
xgs360028fMRSTPInstanceConfigurationState.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceConfigurationState.setStatus(_A)
class _Xgs360028fMRSTPInstanceConfigurationVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fMRSTPInstanceConfigurationVersion_Type.__name__=_B
_Xgs360028fMRSTPInstanceConfigurationVersion_Object=MibTableColumn
xgs360028fMRSTPInstanceConfigurationVersion=_Xgs360028fMRSTPInstanceConfigurationVersion_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,1,2,1,3),_Xgs360028fMRSTPInstanceConfigurationVersion_Type())
xgs360028fMRSTPInstanceConfigurationVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceConfigurationVersion.setStatus(_A)
class _Xgs360028fMRSTPInstanceConfigurationPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_Xgs360028fMRSTPInstanceConfigurationPriority_Type.__name__=_B
_Xgs360028fMRSTPInstanceConfigurationPriority_Object=MibTableColumn
xgs360028fMRSTPInstanceConfigurationPriority=_Xgs360028fMRSTPInstanceConfigurationPriority_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,1,2,1,4),_Xgs360028fMRSTPInstanceConfigurationPriority_Type())
xgs360028fMRSTPInstanceConfigurationPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceConfigurationPriority.setStatus(_A)
class _Xgs360028fMRSTPInstanceConfigurationHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Xgs360028fMRSTPInstanceConfigurationHelloTime_Type.__name__=_B
_Xgs360028fMRSTPInstanceConfigurationHelloTime_Object=MibTableColumn
xgs360028fMRSTPInstanceConfigurationHelloTime=_Xgs360028fMRSTPInstanceConfigurationHelloTime_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,1,2,1,5),_Xgs360028fMRSTPInstanceConfigurationHelloTime_Type())
xgs360028fMRSTPInstanceConfigurationHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceConfigurationHelloTime.setStatus(_A)
class _Xgs360028fMRSTPInstanceConfigurationMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_Xgs360028fMRSTPInstanceConfigurationMaxAge_Type.__name__=_B
_Xgs360028fMRSTPInstanceConfigurationMaxAge_Object=MibTableColumn
xgs360028fMRSTPInstanceConfigurationMaxAge=_Xgs360028fMRSTPInstanceConfigurationMaxAge_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,1,2,1,6),_Xgs360028fMRSTPInstanceConfigurationMaxAge_Type())
xgs360028fMRSTPInstanceConfigurationMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceConfigurationMaxAge.setStatus(_A)
class _Xgs360028fMRSTPInstanceConfigurationFWDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_Xgs360028fMRSTPInstanceConfigurationFWDelay_Type.__name__=_B
_Xgs360028fMRSTPInstanceConfigurationFWDelay_Object=MibTableColumn
xgs360028fMRSTPInstanceConfigurationFWDelay=_Xgs360028fMRSTPInstanceConfigurationFWDelay_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,1,2,1,7),_Xgs360028fMRSTPInstanceConfigurationFWDelay_Type())
xgs360028fMRSTPInstanceConfigurationFWDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceConfigurationFWDelay.setStatus(_A)
_Xgs360028fMRSTPInstanceStatus_ObjectIdentity=ObjectIdentity
xgs360028fMRSTPInstanceStatus=_Xgs360028fMRSTPInstanceStatus_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2))
_Xgs360028fMRSTPInstanceStatusTable_Object=MibTable
xgs360028fMRSTPInstanceStatusTable=_Xgs360028fMRSTPInstanceStatusTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1))
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusTable.setStatus(_A)
_Xgs360028fMRSTPInstanceStatusEntry_Object=MibTableRow
xgs360028fMRSTPInstanceStatusEntry=_Xgs360028fMRSTPInstanceStatusEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1))
xgs360028fMRSTPInstanceStatusEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusEntry.setStatus(_A)
class _Xgs360028fMRSTPInstanceStatusInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Xgs360028fMRSTPInstanceStatusInstance_Type.__name__=_B
_Xgs360028fMRSTPInstanceStatusInstance_Object=MibTableColumn
xgs360028fMRSTPInstanceStatusInstance=_Xgs360028fMRSTPInstanceStatusInstance_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1,1),_Xgs360028fMRSTPInstanceStatusInstance_Type())
xgs360028fMRSTPInstanceStatusInstance.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusInstance.setStatus(_A)
class _Xgs360028fMRSTPInstanceStatusGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fMRSTPInstanceStatusGlobalState_Type.__name__=_B
_Xgs360028fMRSTPInstanceStatusGlobalState_Object=MibTableColumn
xgs360028fMRSTPInstanceStatusGlobalState=_Xgs360028fMRSTPInstanceStatusGlobalState_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1,2),_Xgs360028fMRSTPInstanceStatusGlobalState_Type())
xgs360028fMRSTPInstanceStatusGlobalState.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusGlobalState.setStatus(_A)
class _Xgs360028fMRSTPInstanceStatusInstanceConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fMRSTPInstanceStatusInstanceConfigState_Type.__name__=_B
_Xgs360028fMRSTPInstanceStatusInstanceConfigState_Object=MibTableColumn
xgs360028fMRSTPInstanceStatusInstanceConfigState=_Xgs360028fMRSTPInstanceStatusInstanceConfigState_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1,3),_Xgs360028fMRSTPInstanceStatusInstanceConfigState_Type())
xgs360028fMRSTPInstanceStatusInstanceConfigState.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusInstanceConfigState.setStatus(_A)
class _Xgs360028fMRSTPInstanceStatusInstanceCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fMRSTPInstanceStatusInstanceCurrentState_Type.__name__=_B
_Xgs360028fMRSTPInstanceStatusInstanceCurrentState_Object=MibTableColumn
xgs360028fMRSTPInstanceStatusInstanceCurrentState=_Xgs360028fMRSTPInstanceStatusInstanceCurrentState_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1,4),_Xgs360028fMRSTPInstanceStatusInstanceCurrentState_Type())
xgs360028fMRSTPInstanceStatusInstanceCurrentState.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusInstanceCurrentState.setStatus(_A)
_Xgs360028fMRSTPInstanceStatusBridgeID_Type=MacAddress
_Xgs360028fMRSTPInstanceStatusBridgeID_Object=MibTableColumn
xgs360028fMRSTPInstanceStatusBridgeID=_Xgs360028fMRSTPInstanceStatusBridgeID_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1,5),_Xgs360028fMRSTPInstanceStatusBridgeID_Type())
xgs360028fMRSTPInstanceStatusBridgeID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusBridgeID.setStatus(_A)
class _Xgs360028fMRSTPInstanceStatusBridgePrioriry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_Xgs360028fMRSTPInstanceStatusBridgePrioriry_Type.__name__=_B
_Xgs360028fMRSTPInstanceStatusBridgePrioriry_Object=MibTableColumn
xgs360028fMRSTPInstanceStatusBridgePrioriry=_Xgs360028fMRSTPInstanceStatusBridgePrioriry_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1,6),_Xgs360028fMRSTPInstanceStatusBridgePrioriry_Type())
xgs360028fMRSTPInstanceStatusBridgePrioriry.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusBridgePrioriry.setStatus(_A)
_Xgs360028fMRSTPInstanceStatusRootID_Type=MacAddress
_Xgs360028fMRSTPInstanceStatusRootID_Object=MibTableColumn
xgs360028fMRSTPInstanceStatusRootID=_Xgs360028fMRSTPInstanceStatusRootID_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1,7),_Xgs360028fMRSTPInstanceStatusRootID_Type())
xgs360028fMRSTPInstanceStatusRootID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusRootID.setStatus(_A)
class _Xgs360028fMRSTPInstanceStatusRootPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_Xgs360028fMRSTPInstanceStatusRootPriority_Type.__name__=_B
_Xgs360028fMRSTPInstanceStatusRootPriority_Object=MibTableColumn
xgs360028fMRSTPInstanceStatusRootPriority=_Xgs360028fMRSTPInstanceStatusRootPriority_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1,8),_Xgs360028fMRSTPInstanceStatusRootPriority_Type())
xgs360028fMRSTPInstanceStatusRootPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusRootPriority.setStatus(_A)
_Xgs360028fMRSTPInstanceStatusRootPort_Type=Integer32
_Xgs360028fMRSTPInstanceStatusRootPort_Object=MibTableColumn
xgs360028fMRSTPInstanceStatusRootPort=_Xgs360028fMRSTPInstanceStatusRootPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1,9),_Xgs360028fMRSTPInstanceStatusRootPort_Type())
xgs360028fMRSTPInstanceStatusRootPort.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusRootPort.setStatus(_A)
_Xgs360028fMRSTPInstanceStatusRootPathCost_Type=Integer32
_Xgs360028fMRSTPInstanceStatusRootPathCost_Object=MibTableColumn
xgs360028fMRSTPInstanceStatusRootPathCost=_Xgs360028fMRSTPInstanceStatusRootPathCost_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1,10),_Xgs360028fMRSTPInstanceStatusRootPathCost_Type())
xgs360028fMRSTPInstanceStatusRootPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusRootPathCost.setStatus(_A)
class _Xgs360028fMRSTPInstanceStatusCurrentMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_Xgs360028fMRSTPInstanceStatusCurrentMaxAge_Type.__name__=_B
_Xgs360028fMRSTPInstanceStatusCurrentMaxAge_Object=MibTableColumn
xgs360028fMRSTPInstanceStatusCurrentMaxAge=_Xgs360028fMRSTPInstanceStatusCurrentMaxAge_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1,11),_Xgs360028fMRSTPInstanceStatusCurrentMaxAge_Type())
xgs360028fMRSTPInstanceStatusCurrentMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusCurrentMaxAge.setStatus(_A)
class _Xgs360028fMRSTPInstanceStatusCurrentForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_Xgs360028fMRSTPInstanceStatusCurrentForwardDelay_Type.__name__=_B
_Xgs360028fMRSTPInstanceStatusCurrentForwardDelay_Object=MibTableColumn
xgs360028fMRSTPInstanceStatusCurrentForwardDelay=_Xgs360028fMRSTPInstanceStatusCurrentForwardDelay_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1,12),_Xgs360028fMRSTPInstanceStatusCurrentForwardDelay_Type())
xgs360028fMRSTPInstanceStatusCurrentForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusCurrentForwardDelay.setStatus(_A)
class _Xgs360028fMRSTPInstanceStatusHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Xgs360028fMRSTPInstanceStatusHelloTime_Type.__name__=_B
_Xgs360028fMRSTPInstanceStatusHelloTime_Object=MibTableColumn
xgs360028fMRSTPInstanceStatusHelloTime=_Xgs360028fMRSTPInstanceStatusHelloTime_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1,13),_Xgs360028fMRSTPInstanceStatusHelloTime_Type())
xgs360028fMRSTPInstanceStatusHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusHelloTime.setStatus(_A)
_Xgs360028fMRSTPInstanceStatusTopologyChangeCount_Type=Integer32
_Xgs360028fMRSTPInstanceStatusTopologyChangeCount_Object=MibTableColumn
xgs360028fMRSTPInstanceStatusTopologyChangeCount=_Xgs360028fMRSTPInstanceStatusTopologyChangeCount_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1,14),_Xgs360028fMRSTPInstanceStatusTopologyChangeCount_Type())
xgs360028fMRSTPInstanceStatusTopologyChangeCount.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusTopologyChangeCount.setStatus(_A)
_Xgs360028fMRSTPInstanceStatusTimeSinceLastTopologyChange_Type=Integer32
_Xgs360028fMRSTPInstanceStatusTimeSinceLastTopologyChange_Object=MibTableColumn
xgs360028fMRSTPInstanceStatusTimeSinceLastTopologyChange=_Xgs360028fMRSTPInstanceStatusTimeSinceLastTopologyChange_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,1,2,1,1,15),_Xgs360028fMRSTPInstanceStatusTimeSinceLastTopologyChange_Type())
xgs360028fMRSTPInstanceStatusTimeSinceLastTopologyChange.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPInstanceStatusTimeSinceLastTopologyChange.setStatus(_A)
_Xgs360028fMRSTPPort_ObjectIdentity=ObjectIdentity
xgs360028fMRSTPPort=_Xgs360028fMRSTPPort_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,11,2))
_Xgs360028fMRSTPPortConfiguration_ObjectIdentity=ObjectIdentity
xgs360028fMRSTPPortConfiguration=_Xgs360028fMRSTPPortConfiguration_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,11,2,1))
_Xgs360028fMRSTPPortConfigurationTable_Object=MibTable
xgs360028fMRSTPPortConfigurationTable=_Xgs360028fMRSTPPortConfigurationTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,1,1))
if mibBuilder.loadTexts:xgs360028fMRSTPPortConfigurationTable.setStatus(_A)
_Xgs360028fMRSTPPortConfigurationEntry_Object=MibTableRow
xgs360028fMRSTPPortConfigurationEntry=_Xgs360028fMRSTPPortConfigurationEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,1,1,1))
xgs360028fMRSTPPortConfigurationEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:xgs360028fMRSTPPortConfigurationEntry.setStatus(_A)
class _Xgs360028fMRSTPPortConfigurationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fMRSTPPortConfigurationPort_Type.__name__=_B
_Xgs360028fMRSTPPortConfigurationPort_Object=MibTableColumn
xgs360028fMRSTPPortConfigurationPort=_Xgs360028fMRSTPPortConfigurationPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,1,1,1,1),_Xgs360028fMRSTPPortConfigurationPort_Type())
xgs360028fMRSTPPortConfigurationPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fMRSTPPortConfigurationPort.setStatus(_A)
class _Xgs360028fMRSTPPortConfigurationInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_Xgs360028fMRSTPPortConfigurationInstance_Type.__name__=_B
_Xgs360028fMRSTPPortConfigurationInstance_Object=MibTableColumn
xgs360028fMRSTPPortConfigurationInstance=_Xgs360028fMRSTPPortConfigurationInstance_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,1,1,1,2),_Xgs360028fMRSTPPortConfigurationInstance_Type())
xgs360028fMRSTPPortConfigurationInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMRSTPPortConfigurationInstance.setStatus(_A)
class _Xgs360028fMRSTPPortConfigurationPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_Xgs360028fMRSTPPortConfigurationPathCost_Type.__name__=_B
_Xgs360028fMRSTPPortConfigurationPathCost_Object=MibTableColumn
xgs360028fMRSTPPortConfigurationPathCost=_Xgs360028fMRSTPPortConfigurationPathCost_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,1,1,1,3),_Xgs360028fMRSTPPortConfigurationPathCost_Type())
xgs360028fMRSTPPortConfigurationPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMRSTPPortConfigurationPathCost.setStatus(_A)
class _Xgs360028fMRSTPPortConfigurationPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_Xgs360028fMRSTPPortConfigurationPriority_Type.__name__=_B
_Xgs360028fMRSTPPortConfigurationPriority_Object=MibTableColumn
xgs360028fMRSTPPortConfigurationPriority=_Xgs360028fMRSTPPortConfigurationPriority_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,1,1,1,4),_Xgs360028fMRSTPPortConfigurationPriority_Type())
xgs360028fMRSTPPortConfigurationPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMRSTPPortConfigurationPriority.setStatus(_A)
class _Xgs360028fMRSTPPortConfigurationAdminEdge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fMRSTPPortConfigurationAdminEdge_Type.__name__=_B
_Xgs360028fMRSTPPortConfigurationAdminEdge_Object=MibTableColumn
xgs360028fMRSTPPortConfigurationAdminEdge=_Xgs360028fMRSTPPortConfigurationAdminEdge_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,1,1,1,5),_Xgs360028fMRSTPPortConfigurationAdminEdge_Type())
xgs360028fMRSTPPortConfigurationAdminEdge.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMRSTPPortConfigurationAdminEdge.setStatus(_A)
class _Xgs360028fMRSTPPortConfigurationAdminP2P_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fMRSTPPortConfigurationAdminP2P_Type.__name__=_B
_Xgs360028fMRSTPPortConfigurationAdminP2P_Object=MibTableColumn
xgs360028fMRSTPPortConfigurationAdminP2P=_Xgs360028fMRSTPPortConfigurationAdminP2P_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,1,1,1,6),_Xgs360028fMRSTPPortConfigurationAdminP2P_Type())
xgs360028fMRSTPPortConfigurationAdminP2P.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMRSTPPortConfigurationAdminP2P.setStatus(_A)
class _Xgs360028fMRSTPPortConfigurationMigrateCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fMRSTPPortConfigurationMigrateCheck_Type.__name__=_B
_Xgs360028fMRSTPPortConfigurationMigrateCheck_Object=MibTableColumn
xgs360028fMRSTPPortConfigurationMigrateCheck=_Xgs360028fMRSTPPortConfigurationMigrateCheck_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,1,1,1,7),_Xgs360028fMRSTPPortConfigurationMigrateCheck_Type())
xgs360028fMRSTPPortConfigurationMigrateCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fMRSTPPortConfigurationMigrateCheck.setStatus(_A)
_Xgs360028fMRSTPPortStatus_ObjectIdentity=ObjectIdentity
xgs360028fMRSTPPortStatus=_Xgs360028fMRSTPPortStatus_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,2,11,2,2))
_Xgs360028fMRSTPPortStatusTable_Object=MibTable
xgs360028fMRSTPPortStatusTable=_Xgs360028fMRSTPPortStatusTable_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,2,1))
if mibBuilder.loadTexts:xgs360028fMRSTPPortStatusTable.setStatus(_A)
_Xgs360028fMRSTPPortStatusEntry_Object=MibTableRow
xgs360028fMRSTPPortStatusEntry=_Xgs360028fMRSTPPortStatusEntry_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,2,1,1))
xgs360028fMRSTPPortStatusEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:xgs360028fMRSTPPortStatusEntry.setStatus(_A)
class _Xgs360028fMRSTPPortStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fMRSTPPortStatusPort_Type.__name__=_B
_Xgs360028fMRSTPPortStatusPort_Object=MibTableColumn
xgs360028fMRSTPPortStatusPort=_Xgs360028fMRSTPPortStatusPort_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,2,1,1,1),_Xgs360028fMRSTPPortStatusPort_Type())
xgs360028fMRSTPPortStatusPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fMRSTPPortStatusPort.setStatus(_A)
_Xgs360028fMRSTPPortStatusInstance_Type=DisplayString
_Xgs360028fMRSTPPortStatusInstance_Object=MibTableColumn
xgs360028fMRSTPPortStatusInstance=_Xgs360028fMRSTPPortStatusInstance_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,2,1,1,2),_Xgs360028fMRSTPPortStatusInstance_Type())
xgs360028fMRSTPPortStatusInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPPortStatusInstance.setStatus(_A)
_Xgs360028fMRSTPPortStatusState_Type=DisplayString
_Xgs360028fMRSTPPortStatusState_Object=MibTableColumn
xgs360028fMRSTPPortStatusState=_Xgs360028fMRSTPPortStatusState_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,2,1,1,3),_Xgs360028fMRSTPPortStatusState_Type())
xgs360028fMRSTPPortStatusState.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPPortStatusState.setStatus(_A)
_Xgs360028fMRSTPPortStatusRole_Type=DisplayString
_Xgs360028fMRSTPPortStatusRole_Object=MibTableColumn
xgs360028fMRSTPPortStatusRole=_Xgs360028fMRSTPPortStatusRole_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,2,1,1,4),_Xgs360028fMRSTPPortStatusRole_Type())
xgs360028fMRSTPPortStatusRole.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPPortStatusRole.setStatus(_A)
class _Xgs360028fMRSTPPortStatusPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_Xgs360028fMRSTPPortStatusPathCost_Type.__name__=_B
_Xgs360028fMRSTPPortStatusPathCost_Object=MibTableColumn
xgs360028fMRSTPPortStatusPathCost=_Xgs360028fMRSTPPortStatusPathCost_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,2,1,1,5),_Xgs360028fMRSTPPortStatusPathCost_Type())
xgs360028fMRSTPPortStatusPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPPortStatusPathCost.setStatus(_A)
class _Xgs360028fMRSTPPortStatusPathCostConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_Xgs360028fMRSTPPortStatusPathCostConfig_Type.__name__=_B
_Xgs360028fMRSTPPortStatusPathCostConfig_Object=MibTableColumn
xgs360028fMRSTPPortStatusPathCostConfig=_Xgs360028fMRSTPPortStatusPathCostConfig_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,2,1,1,6),_Xgs360028fMRSTPPortStatusPathCostConfig_Type())
xgs360028fMRSTPPortStatusPathCostConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPPortStatusPathCostConfig.setStatus(_A)
class _Xgs360028fMRSTPPortStatusPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_Xgs360028fMRSTPPortStatusPriority_Type.__name__=_B
_Xgs360028fMRSTPPortStatusPriority_Object=MibTableColumn
xgs360028fMRSTPPortStatusPriority=_Xgs360028fMRSTPPortStatusPriority_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,2,1,1,7),_Xgs360028fMRSTPPortStatusPriority_Type())
xgs360028fMRSTPPortStatusPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPPortStatusPriority.setStatus(_A)
_Xgs360028fMRSTPPortStatusAdminEdge_Type=DisplayString
_Xgs360028fMRSTPPortStatusAdminEdge_Object=MibTableColumn
xgs360028fMRSTPPortStatusAdminEdge=_Xgs360028fMRSTPPortStatusAdminEdge_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,2,1,1,8),_Xgs360028fMRSTPPortStatusAdminEdge_Type())
xgs360028fMRSTPPortStatusAdminEdge.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPPortStatusAdminEdge.setStatus(_A)
_Xgs360028fMRSTPPortStatusAdminP2P_Type=DisplayString
_Xgs360028fMRSTPPortStatusAdminP2P_Object=MibTableColumn
xgs360028fMRSTPPortStatusAdminP2P=_Xgs360028fMRSTPPortStatusAdminP2P_Object((1,3,6,1,4,1,890,1,5,8,78,2,11,2,2,1,1,9),_Xgs360028fMRSTPPortStatusAdminP2P_Type())
xgs360028fMRSTPPortStatusAdminP2P.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fMRSTPPortStatusAdminP2P.setStatus(_A)
_Xgs360028fSecurity_ObjectIdentity=ObjectIdentity
xgs360028fSecurity=_Xgs360028fSecurity_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3))
_Xgs360028fIPSourceGuard_ObjectIdentity=ObjectIdentity
xgs360028fIPSourceGuard=_Xgs360028fIPSourceGuard_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,1))
_Xgs360028fIPSourceGuardConf_ObjectIdentity=ObjectIdentity
xgs360028fIPSourceGuardConf=_Xgs360028fIPSourceGuardConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,1,1))
class _Xgs360028fIPSourceGuardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fIPSourceGuardMode_Type.__name__=_B
_Xgs360028fIPSourceGuardMode_Object=MibScalar
xgs360028fIPSourceGuardMode=_Xgs360028fIPSourceGuardMode_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,1,1),_Xgs360028fIPSourceGuardMode_Type())
xgs360028fIPSourceGuardMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardMode.setStatus(_A)
_Xgs360028fIPSourceGuardPortConfigTable_Object=MibTable
xgs360028fIPSourceGuardPortConfigTable=_Xgs360028fIPSourceGuardPortConfigTable_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,1,2))
if mibBuilder.loadTexts:xgs360028fIPSourceGuardPortConfigTable.setStatus(_A)
_Xgs360028fIPSourceGuardPortConfigEntry_Object=MibTableRow
xgs360028fIPSourceGuardPortConfigEntry=_Xgs360028fIPSourceGuardPortConfigEntry_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,1,2,1))
xgs360028fIPSourceGuardPortConfigEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:xgs360028fIPSourceGuardPortConfigEntry.setStatus(_A)
class _Xgs360028fIPSourceGuardPortConfigPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fIPSourceGuardPortConfigPort_Type.__name__=_B
_Xgs360028fIPSourceGuardPortConfigPort_Object=MibTableColumn
xgs360028fIPSourceGuardPortConfigPort=_Xgs360028fIPSourceGuardPortConfigPort_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,1,2,1,1),_Xgs360028fIPSourceGuardPortConfigPort_Type())
xgs360028fIPSourceGuardPortConfigPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardPortConfigPort.setStatus(_A)
class _Xgs360028fIPSourceGuardPortConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fIPSourceGuardPortConfigMode_Type.__name__=_B
_Xgs360028fIPSourceGuardPortConfigMode_Object=MibTableColumn
xgs360028fIPSourceGuardPortConfigMode=_Xgs360028fIPSourceGuardPortConfigMode_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,1,2,1,2),_Xgs360028fIPSourceGuardPortConfigMode_Type())
xgs360028fIPSourceGuardPortConfigMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardPortConfigMode.setStatus(_A)
class _Xgs360028fIPSourceGuardPortMaxDynamicClients_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2),ValueRangeConstraint(99,99))
_Xgs360028fIPSourceGuardPortMaxDynamicClients_Type.__name__=_B
_Xgs360028fIPSourceGuardPortMaxDynamicClients_Object=MibTableColumn
xgs360028fIPSourceGuardPortMaxDynamicClients=_Xgs360028fIPSourceGuardPortMaxDynamicClients_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,1,2,1,3),_Xgs360028fIPSourceGuardPortMaxDynamicClients_Type())
xgs360028fIPSourceGuardPortMaxDynamicClients.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardPortMaxDynamicClients.setStatus(_A)
_Xgs360028fIPSourceGuardStatic_ObjectIdentity=ObjectIdentity
xgs360028fIPSourceGuardStatic=_Xgs360028fIPSourceGuardStatic_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,1,2))
class _Xgs360028fIPSourceGuardStaticCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fIPSourceGuardStaticCreate_Type.__name__=_B
_Xgs360028fIPSourceGuardStaticCreate_Object=MibScalar
xgs360028fIPSourceGuardStaticCreate=_Xgs360028fIPSourceGuardStaticCreate_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,2,1),_Xgs360028fIPSourceGuardStaticCreate_Type())
xgs360028fIPSourceGuardStaticCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardStaticCreate.setStatus(_A)
_Xgs360028fIPSourceGuardStaticTable_Object=MibTable
xgs360028fIPSourceGuardStaticTable=_Xgs360028fIPSourceGuardStaticTable_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,2,2))
if mibBuilder.loadTexts:xgs360028fIPSourceGuardStaticTable.setStatus(_A)
_Xgs360028fIPSourceGuardStaticEntry_Object=MibTableRow
xgs360028fIPSourceGuardStaticEntry=_Xgs360028fIPSourceGuardStaticEntry_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,2,2,1))
xgs360028fIPSourceGuardStaticEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:xgs360028fIPSourceGuardStaticEntry.setStatus(_A)
class _Xgs360028fIPSourceGuardStaticIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_Xgs360028fIPSourceGuardStaticIndex_Type.__name__=_B
_Xgs360028fIPSourceGuardStaticIndex_Object=MibTableColumn
xgs360028fIPSourceGuardStaticIndex=_Xgs360028fIPSourceGuardStaticIndex_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,2,2,1,1),_Xgs360028fIPSourceGuardStaticIndex_Type())
xgs360028fIPSourceGuardStaticIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardStaticIndex.setStatus(_A)
class _Xgs360028fIPSourceGuardStaticPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fIPSourceGuardStaticPort_Type.__name__=_B
_Xgs360028fIPSourceGuardStaticPort_Object=MibTableColumn
xgs360028fIPSourceGuardStaticPort=_Xgs360028fIPSourceGuardStaticPort_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,2,2,1,2),_Xgs360028fIPSourceGuardStaticPort_Type())
xgs360028fIPSourceGuardStaticPort.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardStaticPort.setStatus(_A)
class _Xgs360028fIPSourceGuardStaticVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Xgs360028fIPSourceGuardStaticVLANId_Type.__name__=_B
_Xgs360028fIPSourceGuardStaticVLANId_Object=MibTableColumn
xgs360028fIPSourceGuardStaticVLANId=_Xgs360028fIPSourceGuardStaticVLANId_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,2,2,1,3),_Xgs360028fIPSourceGuardStaticVLANId_Type())
xgs360028fIPSourceGuardStaticVLANId.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardStaticVLANId.setStatus(_A)
_Xgs360028fIPSourceGuardStaticIPAddress_Type=IpAddress
_Xgs360028fIPSourceGuardStaticIPAddress_Object=MibTableColumn
xgs360028fIPSourceGuardStaticIPAddress=_Xgs360028fIPSourceGuardStaticIPAddress_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,2,2,1,4),_Xgs360028fIPSourceGuardStaticIPAddress_Type())
xgs360028fIPSourceGuardStaticIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardStaticIPAddress.setStatus(_A)
_Xgs360028fIPSourceGuardStaticMACAddress_Type=MacAddress
_Xgs360028fIPSourceGuardStaticMACAddress_Object=MibTableColumn
xgs360028fIPSourceGuardStaticMACAddress=_Xgs360028fIPSourceGuardStaticMACAddress_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,2,2,1,5),_Xgs360028fIPSourceGuardStaticMACAddress_Type())
xgs360028fIPSourceGuardStaticMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardStaticMACAddress.setStatus(_A)
class _Xgs360028fIPSourceGuardStaticRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360028fIPSourceGuardStaticRowStatus_Type.__name__=_B
_Xgs360028fIPSourceGuardStaticRowStatus_Object=MibTableColumn
xgs360028fIPSourceGuardStaticRowStatus=_Xgs360028fIPSourceGuardStaticRowStatus_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,2,2,1,6),_Xgs360028fIPSourceGuardStaticRowStatus_Type())
xgs360028fIPSourceGuardStaticRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardStaticRowStatus.setStatus(_A)
_Xgs360028fIPSourceGuardDynamicTable_Object=MibTable
xgs360028fIPSourceGuardDynamicTable=_Xgs360028fIPSourceGuardDynamicTable_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,3))
if mibBuilder.loadTexts:xgs360028fIPSourceGuardDynamicTable.setStatus(_A)
_Xgs360028fIPSourceGuardDynamicEntry_Object=MibTableRow
xgs360028fIPSourceGuardDynamicEntry=_Xgs360028fIPSourceGuardDynamicEntry_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,3,1))
xgs360028fIPSourceGuardDynamicEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:xgs360028fIPSourceGuardDynamicEntry.setStatus(_A)
class _Xgs360028fIPSourceGuardDynamicIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fIPSourceGuardDynamicIndex_Type.__name__=_B
_Xgs360028fIPSourceGuardDynamicIndex_Object=MibTableColumn
xgs360028fIPSourceGuardDynamicIndex=_Xgs360028fIPSourceGuardDynamicIndex_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,3,1,1),_Xgs360028fIPSourceGuardDynamicIndex_Type())
xgs360028fIPSourceGuardDynamicIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardDynamicIndex.setStatus(_A)
class _Xgs360028fIPSourceGuardDynamicPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Xgs360028fIPSourceGuardDynamicPort_Type.__name__=_B
_Xgs360028fIPSourceGuardDynamicPort_Object=MibTableColumn
xgs360028fIPSourceGuardDynamicPort=_Xgs360028fIPSourceGuardDynamicPort_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,3,1,2),_Xgs360028fIPSourceGuardDynamicPort_Type())
xgs360028fIPSourceGuardDynamicPort.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardDynamicPort.setStatus(_A)
class _Xgs360028fIPSourceGuardDynamicVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Xgs360028fIPSourceGuardDynamicVLANId_Type.__name__=_B
_Xgs360028fIPSourceGuardDynamicVLANId_Object=MibTableColumn
xgs360028fIPSourceGuardDynamicVLANId=_Xgs360028fIPSourceGuardDynamicVLANId_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,3,1,3),_Xgs360028fIPSourceGuardDynamicVLANId_Type())
xgs360028fIPSourceGuardDynamicVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardDynamicVLANId.setStatus(_A)
_Xgs360028fIPSourceGuardDynamicIPAddress_Type=IpAddress
_Xgs360028fIPSourceGuardDynamicIPAddress_Object=MibTableColumn
xgs360028fIPSourceGuardDynamicIPAddress=_Xgs360028fIPSourceGuardDynamicIPAddress_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,3,1,4),_Xgs360028fIPSourceGuardDynamicIPAddress_Type())
xgs360028fIPSourceGuardDynamicIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardDynamicIPAddress.setStatus(_A)
_Xgs360028fIPSourceGuardDynamicMACAddress_Type=MacAddress
_Xgs360028fIPSourceGuardDynamicMACAddress_Object=MibTableColumn
xgs360028fIPSourceGuardDynamicMACAddress=_Xgs360028fIPSourceGuardDynamicMACAddress_Object((1,3,6,1,4,1,890,1,5,8,78,3,1,3,1,5),_Xgs360028fIPSourceGuardDynamicMACAddress_Type())
xgs360028fIPSourceGuardDynamicMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fIPSourceGuardDynamicMACAddress.setStatus(_A)
_Xgs360028fARPInspection_ObjectIdentity=ObjectIdentity
xgs360028fARPInspection=_Xgs360028fARPInspection_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,2))
_Xgs360028fARPInspectionConf_ObjectIdentity=ObjectIdentity
xgs360028fARPInspectionConf=_Xgs360028fARPInspectionConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,2,1))
class _Xgs360028fARPInspectionConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fARPInspectionConfMode_Type.__name__=_B
_Xgs360028fARPInspectionConfMode_Object=MibScalar
xgs360028fARPInspectionConfMode=_Xgs360028fARPInspectionConfMode_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,1,1),_Xgs360028fARPInspectionConfMode_Type())
xgs360028fARPInspectionConfMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fARPInspectionConfMode.setStatus(_A)
_Xgs360028fARPInspectionConfTable_Object=MibTable
xgs360028fARPInspectionConfTable=_Xgs360028fARPInspectionConfTable_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,1,2))
if mibBuilder.loadTexts:xgs360028fARPInspectionConfTable.setStatus(_A)
_Xgs360028fARPInspectionConfEntry_Object=MibTableRow
xgs360028fARPInspectionConfEntry=_Xgs360028fARPInspectionConfEntry_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,1,2,1))
xgs360028fARPInspectionConfEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:xgs360028fARPInspectionConfEntry.setStatus(_A)
class _Xgs360028fARPInspectionConfPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fARPInspectionConfPortIndex_Type.__name__=_B
_Xgs360028fARPInspectionConfPortIndex_Object=MibTableColumn
xgs360028fARPInspectionConfPortIndex=_Xgs360028fARPInspectionConfPortIndex_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,1,2,1,1),_Xgs360028fARPInspectionConfPortIndex_Type())
xgs360028fARPInspectionConfPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fARPInspectionConfPortIndex.setStatus(_A)
class _Xgs360028fARPInspectionConfPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fARPInspectionConfPortMode_Type.__name__=_B
_Xgs360028fARPInspectionConfPortMode_Object=MibTableColumn
xgs360028fARPInspectionConfPortMode=_Xgs360028fARPInspectionConfPortMode_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,1,2,1,2),_Xgs360028fARPInspectionConfPortMode_Type())
xgs360028fARPInspectionConfPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fARPInspectionConfPortMode.setStatus(_A)
_Xgs360028fARPInspectionStatic_ObjectIdentity=ObjectIdentity
xgs360028fARPInspectionStatic=_Xgs360028fARPInspectionStatic_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,2,2))
class _Xgs360028fARPInspectionStaticCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fARPInspectionStaticCreate_Type.__name__=_B
_Xgs360028fARPInspectionStaticCreate_Object=MibScalar
xgs360028fARPInspectionStaticCreate=_Xgs360028fARPInspectionStaticCreate_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,2,1),_Xgs360028fARPInspectionStaticCreate_Type())
xgs360028fARPInspectionStaticCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fARPInspectionStaticCreate.setStatus(_A)
_Xgs360028fARPInspectionStaticTable_Object=MibTable
xgs360028fARPInspectionStaticTable=_Xgs360028fARPInspectionStaticTable_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,2,2))
if mibBuilder.loadTexts:xgs360028fARPInspectionStaticTable.setStatus(_A)
_Xgs360028fARPInspectionStaticEntry_Object=MibTableRow
xgs360028fARPInspectionStaticEntry=_Xgs360028fARPInspectionStaticEntry_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,2,2,1))
xgs360028fARPInspectionStaticEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:xgs360028fARPInspectionStaticEntry.setStatus(_A)
class _Xgs360028fARPInspectionStaticIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fARPInspectionStaticIndex_Type.__name__=_B
_Xgs360028fARPInspectionStaticIndex_Object=MibTableColumn
xgs360028fARPInspectionStaticIndex=_Xgs360028fARPInspectionStaticIndex_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,2,2,1,1),_Xgs360028fARPInspectionStaticIndex_Type())
xgs360028fARPInspectionStaticIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fARPInspectionStaticIndex.setStatus(_A)
class _Xgs360028fARPInspectionStaticPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fARPInspectionStaticPort_Type.__name__=_B
_Xgs360028fARPInspectionStaticPort_Object=MibTableColumn
xgs360028fARPInspectionStaticPort=_Xgs360028fARPInspectionStaticPort_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,2,2,1,2),_Xgs360028fARPInspectionStaticPort_Type())
xgs360028fARPInspectionStaticPort.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fARPInspectionStaticPort.setStatus(_A)
class _Xgs360028fARPInspectionStaticVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Xgs360028fARPInspectionStaticVLANId_Type.__name__=_B
_Xgs360028fARPInspectionStaticVLANId_Object=MibTableColumn
xgs360028fARPInspectionStaticVLANId=_Xgs360028fARPInspectionStaticVLANId_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,2,2,1,3),_Xgs360028fARPInspectionStaticVLANId_Type())
xgs360028fARPInspectionStaticVLANId.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fARPInspectionStaticVLANId.setStatus(_A)
_Xgs360028fARPInspectionStaticIPAddress_Type=IpAddress
_Xgs360028fARPInspectionStaticIPAddress_Object=MibTableColumn
xgs360028fARPInspectionStaticIPAddress=_Xgs360028fARPInspectionStaticIPAddress_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,2,2,1,4),_Xgs360028fARPInspectionStaticIPAddress_Type())
xgs360028fARPInspectionStaticIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fARPInspectionStaticIPAddress.setStatus(_A)
_Xgs360028fARPInspectionStaticMACAddress_Type=MacAddress
_Xgs360028fARPInspectionStaticMACAddress_Object=MibTableColumn
xgs360028fARPInspectionStaticMACAddress=_Xgs360028fARPInspectionStaticMACAddress_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,2,2,1,5),_Xgs360028fARPInspectionStaticMACAddress_Type())
xgs360028fARPInspectionStaticMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fARPInspectionStaticMACAddress.setStatus(_A)
class _Xgs360028fARPInspectionStaticRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360028fARPInspectionStaticRowStatus_Type.__name__=_B
_Xgs360028fARPInspectionStaticRowStatus_Object=MibTableColumn
xgs360028fARPInspectionStaticRowStatus=_Xgs360028fARPInspectionStaticRowStatus_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,2,2,1,6),_Xgs360028fARPInspectionStaticRowStatus_Type())
xgs360028fARPInspectionStaticRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fARPInspectionStaticRowStatus.setStatus(_A)
_Xgs360028fARPInspectionDynamicTable_Object=MibTable
xgs360028fARPInspectionDynamicTable=_Xgs360028fARPInspectionDynamicTable_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,3))
if mibBuilder.loadTexts:xgs360028fARPInspectionDynamicTable.setStatus(_A)
_Xgs360028fARPInspectionDynamicEntry_Object=MibTableRow
xgs360028fARPInspectionDynamicEntry=_Xgs360028fARPInspectionDynamicEntry_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,3,1))
xgs360028fARPInspectionDynamicEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:xgs360028fARPInspectionDynamicEntry.setStatus(_A)
class _Xgs360028fARPInspectionDynamicIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fARPInspectionDynamicIndex_Type.__name__=_B
_Xgs360028fARPInspectionDynamicIndex_Object=MibTableColumn
xgs360028fARPInspectionDynamicIndex=_Xgs360028fARPInspectionDynamicIndex_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,3,1,1),_Xgs360028fARPInspectionDynamicIndex_Type())
xgs360028fARPInspectionDynamicIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fARPInspectionDynamicIndex.setStatus(_A)
class _Xgs360028fARPInspectionDynamicPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fARPInspectionDynamicPort_Type.__name__=_B
_Xgs360028fARPInspectionDynamicPort_Object=MibTableColumn
xgs360028fARPInspectionDynamicPort=_Xgs360028fARPInspectionDynamicPort_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,3,1,2),_Xgs360028fARPInspectionDynamicPort_Type())
xgs360028fARPInspectionDynamicPort.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fARPInspectionDynamicPort.setStatus(_A)
class _Xgs360028fARPInspectionDynamicVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Xgs360028fARPInspectionDynamicVLANId_Type.__name__=_B
_Xgs360028fARPInspectionDynamicVLANId_Object=MibTableColumn
xgs360028fARPInspectionDynamicVLANId=_Xgs360028fARPInspectionDynamicVLANId_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,3,1,3),_Xgs360028fARPInspectionDynamicVLANId_Type())
xgs360028fARPInspectionDynamicVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fARPInspectionDynamicVLANId.setStatus(_A)
_Xgs360028fARPInspectionDynamicIPAddress_Type=IpAddress
_Xgs360028fARPInspectionDynamicIPAddress_Object=MibTableColumn
xgs360028fARPInspectionDynamicIPAddress=_Xgs360028fARPInspectionDynamicIPAddress_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,3,1,4),_Xgs360028fARPInspectionDynamicIPAddress_Type())
xgs360028fARPInspectionDynamicIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fARPInspectionDynamicIPAddress.setStatus(_A)
_Xgs360028fARPInspectionDynamicMACAddress_Type=MacAddress
_Xgs360028fARPInspectionDynamicMACAddress_Object=MibTableColumn
xgs360028fARPInspectionDynamicMACAddress=_Xgs360028fARPInspectionDynamicMACAddress_Object((1,3,6,1,4,1,890,1,5,8,78,3,2,3,1,5),_Xgs360028fARPInspectionDynamicMACAddress_Type())
xgs360028fARPInspectionDynamicMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fARPInspectionDynamicMACAddress.setStatus(_A)
_Xgs360028fDHCPSnooping_ObjectIdentity=ObjectIdentity
xgs360028fDHCPSnooping=_Xgs360028fDHCPSnooping_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,3))
_Xgs360028fDHCPSnoopingConf_ObjectIdentity=ObjectIdentity
xgs360028fDHCPSnoopingConf=_Xgs360028fDHCPSnoopingConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,3,1))
class _Xgs360028fDHCPSnoopingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fDHCPSnoopingMode_Type.__name__=_B
_Xgs360028fDHCPSnoopingMode_Object=MibScalar
xgs360028fDHCPSnoopingMode=_Xgs360028fDHCPSnoopingMode_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,1,1),_Xgs360028fDHCPSnoopingMode_Type())
xgs360028fDHCPSnoopingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingMode.setStatus(_A)
_Xgs360028fDHCPSnoopingPortModeConfigurationTable_Object=MibTable
xgs360028fDHCPSnoopingPortModeConfigurationTable=_Xgs360028fDHCPSnoopingPortModeConfigurationTable_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,1,2))
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingPortModeConfigurationTable.setStatus(_A)
_Xgs360028fDHCPSnoopingPortModeConfigurationEntry_Object=MibTableRow
xgs360028fDHCPSnoopingPortModeConfigurationEntry=_Xgs360028fDHCPSnoopingPortModeConfigurationEntry_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,1,2,1))
xgs360028fDHCPSnoopingPortModeConfigurationEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingPortModeConfigurationEntry.setStatus(_A)
class _Xgs360028fDHCPSnoopingPortModeConfigurationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fDHCPSnoopingPortModeConfigurationPort_Type.__name__=_B
_Xgs360028fDHCPSnoopingPortModeConfigurationPort_Object=MibTableColumn
xgs360028fDHCPSnoopingPortModeConfigurationPort=_Xgs360028fDHCPSnoopingPortModeConfigurationPort_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,1,2,1,1),_Xgs360028fDHCPSnoopingPortModeConfigurationPort_Type())
xgs360028fDHCPSnoopingPortModeConfigurationPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingPortModeConfigurationPort.setStatus(_A)
class _Xgs360028fDHCPSnoopingPortModeConfigurationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fDHCPSnoopingPortModeConfigurationMode_Type.__name__=_B
_Xgs360028fDHCPSnoopingPortModeConfigurationMode_Object=MibTableColumn
xgs360028fDHCPSnoopingPortModeConfigurationMode=_Xgs360028fDHCPSnoopingPortModeConfigurationMode_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,1,2,1,2),_Xgs360028fDHCPSnoopingPortModeConfigurationMode_Type())
xgs360028fDHCPSnoopingPortModeConfigurationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingPortModeConfigurationMode.setStatus(_A)
_Xgs360028fDHCPSnoopingStatisticsTable_Object=MibTable
xgs360028fDHCPSnoopingStatisticsTable=_Xgs360028fDHCPSnoopingStatisticsTable_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2))
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingStatisticsTable.setStatus(_A)
_Xgs360028fDHCPSnoopingStatisticsEntry_Object=MibTableRow
xgs360028fDHCPSnoopingStatisticsEntry=_Xgs360028fDHCPSnoopingStatisticsEntry_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1))
xgs360028fDHCPSnoopingStatisticsEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingStatisticsEntry.setStatus(_A)
class _Xgs360028fDHCPSnoopingStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fDHCPSnoopingStatisticsPort_Type.__name__=_B
_Xgs360028fDHCPSnoopingStatisticsPort_Object=MibTableColumn
xgs360028fDHCPSnoopingStatisticsPort=_Xgs360028fDHCPSnoopingStatisticsPort_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,1),_Xgs360028fDHCPSnoopingStatisticsPort_Type())
xgs360028fDHCPSnoopingStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingStatisticsPort.setStatus(_A)
class _Xgs360028fDHCPSnoopingStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fDHCPSnoopingStatisticsClear_Type.__name__=_B
_Xgs360028fDHCPSnoopingStatisticsClear_Object=MibTableColumn
xgs360028fDHCPSnoopingStatisticsClear=_Xgs360028fDHCPSnoopingStatisticsClear_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,2),_Xgs360028fDHCPSnoopingStatisticsClear_Type())
xgs360028fDHCPSnoopingStatisticsClear.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingStatisticsClear.setStatus(_A)
_Xgs360028fDHCPSnoopingRxDiscover_Type=Counter32
_Xgs360028fDHCPSnoopingRxDiscover_Object=MibTableColumn
xgs360028fDHCPSnoopingRxDiscover=_Xgs360028fDHCPSnoopingRxDiscover_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,3),_Xgs360028fDHCPSnoopingRxDiscover_Type())
xgs360028fDHCPSnoopingRxDiscover.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingRxDiscover.setStatus(_A)
_Xgs360028fDHCPSnoopingRxOffer_Type=Counter32
_Xgs360028fDHCPSnoopingRxOffer_Object=MibTableColumn
xgs360028fDHCPSnoopingRxOffer=_Xgs360028fDHCPSnoopingRxOffer_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,4),_Xgs360028fDHCPSnoopingRxOffer_Type())
xgs360028fDHCPSnoopingRxOffer.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingRxOffer.setStatus(_A)
_Xgs360028fDHCPSnoopingRxRequest_Type=Counter32
_Xgs360028fDHCPSnoopingRxRequest_Object=MibTableColumn
xgs360028fDHCPSnoopingRxRequest=_Xgs360028fDHCPSnoopingRxRequest_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,5),_Xgs360028fDHCPSnoopingRxRequest_Type())
xgs360028fDHCPSnoopingRxRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingRxRequest.setStatus(_A)
_Xgs360028fDHCPSnoopingRxDecline_Type=Counter32
_Xgs360028fDHCPSnoopingRxDecline_Object=MibTableColumn
xgs360028fDHCPSnoopingRxDecline=_Xgs360028fDHCPSnoopingRxDecline_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,6),_Xgs360028fDHCPSnoopingRxDecline_Type())
xgs360028fDHCPSnoopingRxDecline.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingRxDecline.setStatus(_A)
_Xgs360028fDHCPSnoopingRxACK_Type=Counter32
_Xgs360028fDHCPSnoopingRxACK_Object=MibTableColumn
xgs360028fDHCPSnoopingRxACK=_Xgs360028fDHCPSnoopingRxACK_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,7),_Xgs360028fDHCPSnoopingRxACK_Type())
xgs360028fDHCPSnoopingRxACK.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingRxACK.setStatus(_A)
_Xgs360028fDHCPSnoopingRxNAK_Type=Counter32
_Xgs360028fDHCPSnoopingRxNAK_Object=MibTableColumn
xgs360028fDHCPSnoopingRxNAK=_Xgs360028fDHCPSnoopingRxNAK_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,8),_Xgs360028fDHCPSnoopingRxNAK_Type())
xgs360028fDHCPSnoopingRxNAK.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingRxNAK.setStatus(_A)
_Xgs360028fDHCPSnoopingRxRelease_Type=Counter32
_Xgs360028fDHCPSnoopingRxRelease_Object=MibTableColumn
xgs360028fDHCPSnoopingRxRelease=_Xgs360028fDHCPSnoopingRxRelease_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,9),_Xgs360028fDHCPSnoopingRxRelease_Type())
xgs360028fDHCPSnoopingRxRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingRxRelease.setStatus(_A)
_Xgs360028fDHCPSnoopingRxInform_Type=Counter32
_Xgs360028fDHCPSnoopingRxInform_Object=MibTableColumn
xgs360028fDHCPSnoopingRxInform=_Xgs360028fDHCPSnoopingRxInform_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,10),_Xgs360028fDHCPSnoopingRxInform_Type())
xgs360028fDHCPSnoopingRxInform.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingRxInform.setStatus(_A)
_Xgs360028fDHCPSnoopingRxLeaseQuery_Type=Counter32
_Xgs360028fDHCPSnoopingRxLeaseQuery_Object=MibTableColumn
xgs360028fDHCPSnoopingRxLeaseQuery=_Xgs360028fDHCPSnoopingRxLeaseQuery_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,11),_Xgs360028fDHCPSnoopingRxLeaseQuery_Type())
xgs360028fDHCPSnoopingRxLeaseQuery.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingRxLeaseQuery.setStatus(_A)
_Xgs360028fDHCPSnoopingRxLeaseUnassigned_Type=Counter32
_Xgs360028fDHCPSnoopingRxLeaseUnassigned_Object=MibTableColumn
xgs360028fDHCPSnoopingRxLeaseUnassigned=_Xgs360028fDHCPSnoopingRxLeaseUnassigned_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,12),_Xgs360028fDHCPSnoopingRxLeaseUnassigned_Type())
xgs360028fDHCPSnoopingRxLeaseUnassigned.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingRxLeaseUnassigned.setStatus(_A)
_Xgs360028fDHCPSnoopingRxLeaseUnknown_Type=Counter32
_Xgs360028fDHCPSnoopingRxLeaseUnknown_Object=MibTableColumn
xgs360028fDHCPSnoopingRxLeaseUnknown=_Xgs360028fDHCPSnoopingRxLeaseUnknown_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,13),_Xgs360028fDHCPSnoopingRxLeaseUnknown_Type())
xgs360028fDHCPSnoopingRxLeaseUnknown.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingRxLeaseUnknown.setStatus(_A)
_Xgs360028fDHCPSnoopingRxLeaseActive_Type=Counter32
_Xgs360028fDHCPSnoopingRxLeaseActive_Object=MibTableColumn
xgs360028fDHCPSnoopingRxLeaseActive=_Xgs360028fDHCPSnoopingRxLeaseActive_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,14),_Xgs360028fDHCPSnoopingRxLeaseActive_Type())
xgs360028fDHCPSnoopingRxLeaseActive.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingRxLeaseActive.setStatus(_A)
_Xgs360028fDHCPSnoopingTxDiscover_Type=Counter32
_Xgs360028fDHCPSnoopingTxDiscover_Object=MibTableColumn
xgs360028fDHCPSnoopingTxDiscover=_Xgs360028fDHCPSnoopingTxDiscover_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,15),_Xgs360028fDHCPSnoopingTxDiscover_Type())
xgs360028fDHCPSnoopingTxDiscover.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingTxDiscover.setStatus(_A)
_Xgs360028fDHCPSnoopingTxOffer_Type=Counter32
_Xgs360028fDHCPSnoopingTxOffer_Object=MibTableColumn
xgs360028fDHCPSnoopingTxOffer=_Xgs360028fDHCPSnoopingTxOffer_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,16),_Xgs360028fDHCPSnoopingTxOffer_Type())
xgs360028fDHCPSnoopingTxOffer.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingTxOffer.setStatus(_A)
_Xgs360028fDHCPSnoopingTxRequest_Type=Counter32
_Xgs360028fDHCPSnoopingTxRequest_Object=MibTableColumn
xgs360028fDHCPSnoopingTxRequest=_Xgs360028fDHCPSnoopingTxRequest_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,17),_Xgs360028fDHCPSnoopingTxRequest_Type())
xgs360028fDHCPSnoopingTxRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingTxRequest.setStatus(_A)
_Xgs360028fDHCPSnoopingTxDecline_Type=Counter32
_Xgs360028fDHCPSnoopingTxDecline_Object=MibTableColumn
xgs360028fDHCPSnoopingTxDecline=_Xgs360028fDHCPSnoopingTxDecline_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,18),_Xgs360028fDHCPSnoopingTxDecline_Type())
xgs360028fDHCPSnoopingTxDecline.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingTxDecline.setStatus(_A)
_Xgs360028fDHCPSnoopingTxACK_Type=Counter32
_Xgs360028fDHCPSnoopingTxACK_Object=MibTableColumn
xgs360028fDHCPSnoopingTxACK=_Xgs360028fDHCPSnoopingTxACK_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,19),_Xgs360028fDHCPSnoopingTxACK_Type())
xgs360028fDHCPSnoopingTxACK.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingTxACK.setStatus(_A)
_Xgs360028fDHCPSnoopingTxNAK_Type=Counter32
_Xgs360028fDHCPSnoopingTxNAK_Object=MibTableColumn
xgs360028fDHCPSnoopingTxNAK=_Xgs360028fDHCPSnoopingTxNAK_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,20),_Xgs360028fDHCPSnoopingTxNAK_Type())
xgs360028fDHCPSnoopingTxNAK.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingTxNAK.setStatus(_A)
_Xgs360028fDHCPSnoopingTxRelease_Type=Counter32
_Xgs360028fDHCPSnoopingTxRelease_Object=MibTableColumn
xgs360028fDHCPSnoopingTxRelease=_Xgs360028fDHCPSnoopingTxRelease_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,21),_Xgs360028fDHCPSnoopingTxRelease_Type())
xgs360028fDHCPSnoopingTxRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingTxRelease.setStatus(_A)
_Xgs360028fDHCPSnoopingTxInform_Type=Counter32
_Xgs360028fDHCPSnoopingTxInform_Object=MibTableColumn
xgs360028fDHCPSnoopingTxInform=_Xgs360028fDHCPSnoopingTxInform_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,22),_Xgs360028fDHCPSnoopingTxInform_Type())
xgs360028fDHCPSnoopingTxInform.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingTxInform.setStatus(_A)
_Xgs360028fDHCPSnoopingTxLeaseQuery_Type=Counter32
_Xgs360028fDHCPSnoopingTxLeaseQuery_Object=MibTableColumn
xgs360028fDHCPSnoopingTxLeaseQuery=_Xgs360028fDHCPSnoopingTxLeaseQuery_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,23),_Xgs360028fDHCPSnoopingTxLeaseQuery_Type())
xgs360028fDHCPSnoopingTxLeaseQuery.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingTxLeaseQuery.setStatus(_A)
_Xgs360028fDHCPSnoopingTxLeaseUnassigned_Type=Counter32
_Xgs360028fDHCPSnoopingTxLeaseUnassigned_Object=MibTableColumn
xgs360028fDHCPSnoopingTxLeaseUnassigned=_Xgs360028fDHCPSnoopingTxLeaseUnassigned_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,24),_Xgs360028fDHCPSnoopingTxLeaseUnassigned_Type())
xgs360028fDHCPSnoopingTxLeaseUnassigned.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingTxLeaseUnassigned.setStatus(_A)
_Xgs360028fDHCPSnoopingTxLeaseUnknown_Type=Counter32
_Xgs360028fDHCPSnoopingTxLeaseUnknown_Object=MibTableColumn
xgs360028fDHCPSnoopingTxLeaseUnknown=_Xgs360028fDHCPSnoopingTxLeaseUnknown_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,25),_Xgs360028fDHCPSnoopingTxLeaseUnknown_Type())
xgs360028fDHCPSnoopingTxLeaseUnknown.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingTxLeaseUnknown.setStatus(_A)
_Xgs360028fDHCPSnoopingTxLeaseActive_Type=Counter32
_Xgs360028fDHCPSnoopingTxLeaseActive_Object=MibTableColumn
xgs360028fDHCPSnoopingTxLeaseActive=_Xgs360028fDHCPSnoopingTxLeaseActive_Object((1,3,6,1,4,1,890,1,5,8,78,3,3,2,1,26),_Xgs360028fDHCPSnoopingTxLeaseActive_Type())
xgs360028fDHCPSnoopingTxLeaseActive.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fDHCPSnoopingTxLeaseActive.setStatus(_A)
_Xgs360028fDHCPRelay_ObjectIdentity=ObjectIdentity
xgs360028fDHCPRelay=_Xgs360028fDHCPRelay_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,4))
_Xgs360028fDHCPRelayConfiguration_ObjectIdentity=ObjectIdentity
xgs360028fDHCPRelayConfiguration=_Xgs360028fDHCPRelayConfiguration_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,4,1))
class _Xgs360028fDHCPRelayMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fDHCPRelayMode_Type.__name__=_B
_Xgs360028fDHCPRelayMode_Object=MibScalar
xgs360028fDHCPRelayMode=_Xgs360028fDHCPRelayMode_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,1,1),_Xgs360028fDHCPRelayMode_Type())
xgs360028fDHCPRelayMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fDHCPRelayMode.setStatus(_A)
_Xgs360028fDHCPRelayServer_Type=IpAddress
_Xgs360028fDHCPRelayServer_Object=MibScalar
xgs360028fDHCPRelayServer=_Xgs360028fDHCPRelayServer_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,1,2),_Xgs360028fDHCPRelayServer_Type())
xgs360028fDHCPRelayServer.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fDHCPRelayServer.setStatus(_A)
class _Xgs360028fDHCPRelayInformationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fDHCPRelayInformationMode_Type.__name__=_B
_Xgs360028fDHCPRelayInformationMode_Object=MibScalar
xgs360028fDHCPRelayInformationMode=_Xgs360028fDHCPRelayInformationMode_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,1,3),_Xgs360028fDHCPRelayInformationMode_Type())
xgs360028fDHCPRelayInformationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fDHCPRelayInformationMode.setStatus(_A)
class _Xgs360028fDHCPRelayInformationPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Xgs360028fDHCPRelayInformationPolicy_Type.__name__=_B
_Xgs360028fDHCPRelayInformationPolicy_Object=MibScalar
xgs360028fDHCPRelayInformationPolicy=_Xgs360028fDHCPRelayInformationPolicy_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,1,4),_Xgs360028fDHCPRelayInformationPolicy_Type())
xgs360028fDHCPRelayInformationPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fDHCPRelayInformationPolicy.setStatus(_A)
_Xgs360028fDHCPRelayStatistics_ObjectIdentity=ObjectIdentity
xgs360028fDHCPRelayStatistics=_Xgs360028fDHCPRelayStatistics_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,4,2))
_Xgs360028fDHCPRelayServerStatistics_ObjectIdentity=ObjectIdentity
xgs360028fDHCPRelayServerStatistics=_Xgs360028fDHCPRelayServerStatistics_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,4,2,1))
_Xgs360028fServerStatTransmitToServer_Type=Counter32
_Xgs360028fServerStatTransmitToServer_Object=MibScalar
xgs360028fServerStatTransmitToServer=_Xgs360028fServerStatTransmitToServer_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,2,1,1),_Xgs360028fServerStatTransmitToServer_Type())
xgs360028fServerStatTransmitToServer.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fServerStatTransmitToServer.setStatus(_A)
_Xgs360028fServerStatTransmitError_Type=Counter32
_Xgs360028fServerStatTransmitError_Object=MibScalar
xgs360028fServerStatTransmitError=_Xgs360028fServerStatTransmitError_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,2,1,2),_Xgs360028fServerStatTransmitError_Type())
xgs360028fServerStatTransmitError.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fServerStatTransmitError.setStatus(_A)
_Xgs360028fServerStatReceiveFromServer_Type=Counter32
_Xgs360028fServerStatReceiveFromServer_Object=MibScalar
xgs360028fServerStatReceiveFromServer=_Xgs360028fServerStatReceiveFromServer_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,2,1,3),_Xgs360028fServerStatReceiveFromServer_Type())
xgs360028fServerStatReceiveFromServer.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fServerStatReceiveFromServer.setStatus(_A)
_Xgs360028fServerStatReceiveMissingAgentOption_Type=Counter32
_Xgs360028fServerStatReceiveMissingAgentOption_Object=MibScalar
xgs360028fServerStatReceiveMissingAgentOption=_Xgs360028fServerStatReceiveMissingAgentOption_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,2,1,4),_Xgs360028fServerStatReceiveMissingAgentOption_Type())
xgs360028fServerStatReceiveMissingAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fServerStatReceiveMissingAgentOption.setStatus(_A)
_Xgs360028fServerStatReceiveMissingCircuitID_Type=Counter32
_Xgs360028fServerStatReceiveMissingCircuitID_Object=MibScalar
xgs360028fServerStatReceiveMissingCircuitID=_Xgs360028fServerStatReceiveMissingCircuitID_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,2,1,5),_Xgs360028fServerStatReceiveMissingCircuitID_Type())
xgs360028fServerStatReceiveMissingCircuitID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fServerStatReceiveMissingCircuitID.setStatus(_A)
_Xgs360028fServerStatReceiveMissingRemoteID_Type=Counter32
_Xgs360028fServerStatReceiveMissingRemoteID_Object=MibScalar
xgs360028fServerStatReceiveMissingRemoteID=_Xgs360028fServerStatReceiveMissingRemoteID_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,2,1,6),_Xgs360028fServerStatReceiveMissingRemoteID_Type())
xgs360028fServerStatReceiveMissingRemoteID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fServerStatReceiveMissingRemoteID.setStatus(_A)
_Xgs360028fServerStatReceiveBadCircuitID_Type=Counter32
_Xgs360028fServerStatReceiveBadCircuitID_Object=MibScalar
xgs360028fServerStatReceiveBadCircuitID=_Xgs360028fServerStatReceiveBadCircuitID_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,2,1,7),_Xgs360028fServerStatReceiveBadCircuitID_Type())
xgs360028fServerStatReceiveBadCircuitID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fServerStatReceiveBadCircuitID.setStatus(_A)
_Xgs360028fServerStatReceiveBadRemoteID_Type=Counter32
_Xgs360028fServerStatReceiveBadRemoteID_Object=MibScalar
xgs360028fServerStatReceiveBadRemoteID=_Xgs360028fServerStatReceiveBadRemoteID_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,2,1,8),_Xgs360028fServerStatReceiveBadRemoteID_Type())
xgs360028fServerStatReceiveBadRemoteID.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fServerStatReceiveBadRemoteID.setStatus(_A)
_Xgs360028fDHCPRelayClientStatistics_ObjectIdentity=ObjectIdentity
xgs360028fDHCPRelayClientStatistics=_Xgs360028fDHCPRelayClientStatistics_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,4,2,2))
_Xgs360028fClientStatTransmitToClient_Type=Counter32
_Xgs360028fClientStatTransmitToClient_Object=MibScalar
xgs360028fClientStatTransmitToClient=_Xgs360028fClientStatTransmitToClient_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,2,2,1),_Xgs360028fClientStatTransmitToClient_Type())
xgs360028fClientStatTransmitToClient.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fClientStatTransmitToClient.setStatus(_A)
_Xgs360028fClientStatTransmitError_Type=Counter32
_Xgs360028fClientStatTransmitError_Object=MibScalar
xgs360028fClientStatTransmitError=_Xgs360028fClientStatTransmitError_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,2,2,2),_Xgs360028fClientStatTransmitError_Type())
xgs360028fClientStatTransmitError.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fClientStatTransmitError.setStatus(_A)
_Xgs360028fClientStatReceivefromClient_Type=Counter32
_Xgs360028fClientStatReceivefromClient_Object=MibScalar
xgs360028fClientStatReceivefromClient=_Xgs360028fClientStatReceivefromClient_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,2,2,3),_Xgs360028fClientStatReceivefromClient_Type())
xgs360028fClientStatReceivefromClient.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fClientStatReceivefromClient.setStatus(_A)
_Xgs360028fClientStatReceiveAgentOption_Type=Counter32
_Xgs360028fClientStatReceiveAgentOption_Object=MibScalar
xgs360028fClientStatReceiveAgentOption=_Xgs360028fClientStatReceiveAgentOption_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,2,2,4),_Xgs360028fClientStatReceiveAgentOption_Type())
xgs360028fClientStatReceiveAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fClientStatReceiveAgentOption.setStatus(_A)
_Xgs360028fClientStatReplaceAgentOption_Type=Counter32
_Xgs360028fClientStatReplaceAgentOption_Object=MibScalar
xgs360028fClientStatReplaceAgentOption=_Xgs360028fClientStatReplaceAgentOption_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,2,2,5),_Xgs360028fClientStatReplaceAgentOption_Type())
xgs360028fClientStatReplaceAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fClientStatReplaceAgentOption.setStatus(_A)
_Xgs360028fClientStatKeepAgentOption_Type=Counter32
_Xgs360028fClientStatKeepAgentOption_Object=MibScalar
xgs360028fClientStatKeepAgentOption=_Xgs360028fClientStatKeepAgentOption_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,2,2,6),_Xgs360028fClientStatKeepAgentOption_Type())
xgs360028fClientStatKeepAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fClientStatKeepAgentOption.setStatus(_A)
_Xgs360028fClientStatDropAgentOption_Type=Counter32
_Xgs360028fClientStatDropAgentOption_Object=MibScalar
xgs360028fClientStatDropAgentOption=_Xgs360028fClientStatDropAgentOption_Object((1,3,6,1,4,1,890,1,5,8,78,3,4,2,2,7),_Xgs360028fClientStatDropAgentOption_Type())
xgs360028fClientStatDropAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fClientStatDropAgentOption.setStatus(_A)
_Xgs360028fPortSecurity_ObjectIdentity=ObjectIdentity
xgs360028fPortSecurity=_Xgs360028fPortSecurity_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,5))
_Xgs360028fPortSecLimitCtrl_ObjectIdentity=ObjectIdentity
xgs360028fPortSecLimitCtrl=_Xgs360028fPortSecLimitCtrl_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,5,1))
_Xgs360028fPortSecLimitCtrlSystemConf_ObjectIdentity=ObjectIdentity
xgs360028fPortSecLimitCtrlSystemConf=_Xgs360028fPortSecLimitCtrlSystemConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,5,1,1))
class _Xgs360028fPortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fPortSecurityMode_Type.__name__=_B
_Xgs360028fPortSecurityMode_Object=MibScalar
xgs360028fPortSecurityMode=_Xgs360028fPortSecurityMode_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,1,1,1),_Xgs360028fPortSecurityMode_Type())
xgs360028fPortSecurityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortSecurityMode.setStatus(_A)
class _Xgs360028fPortSecurityAging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fPortSecurityAging_Type.__name__=_B
_Xgs360028fPortSecurityAging_Object=MibScalar
xgs360028fPortSecurityAging=_Xgs360028fPortSecurityAging_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,1,1,2),_Xgs360028fPortSecurityAging_Type())
xgs360028fPortSecurityAging.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortSecurityAging.setStatus(_A)
class _Xgs360028fPortSecurityAgingPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10000000))
_Xgs360028fPortSecurityAgingPeriod_Type.__name__=_B
_Xgs360028fPortSecurityAgingPeriod_Object=MibScalar
xgs360028fPortSecurityAgingPeriod=_Xgs360028fPortSecurityAgingPeriod_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,1,1,3),_Xgs360028fPortSecurityAgingPeriod_Type())
xgs360028fPortSecurityAgingPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortSecurityAgingPeriod.setStatus(_A)
_Xgs360028fPortSecLimitCtrlTable_Object=MibTable
xgs360028fPortSecLimitCtrlTable=_Xgs360028fPortSecLimitCtrlTable_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,1,2))
if mibBuilder.loadTexts:xgs360028fPortSecLimitCtrlTable.setStatus(_A)
_Xgs360028fPortSecLimitCtrlEntry_Object=MibTableRow
xgs360028fPortSecLimitCtrlEntry=_Xgs360028fPortSecLimitCtrlEntry_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,1,2,1))
xgs360028fPortSecLimitCtrlEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:xgs360028fPortSecLimitCtrlEntry.setStatus(_A)
class _Xgs360028fPortSecLimitCtrlPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fPortSecLimitCtrlPort_Type.__name__=_B
_Xgs360028fPortSecLimitCtrlPort_Object=MibTableColumn
xgs360028fPortSecLimitCtrlPort=_Xgs360028fPortSecLimitCtrlPort_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,1,2,1,1),_Xgs360028fPortSecLimitCtrlPort_Type())
xgs360028fPortSecLimitCtrlPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fPortSecLimitCtrlPort.setStatus(_A)
class _Xgs360028fPortSecLimitCtrlPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fPortSecLimitCtrlPortMode_Type.__name__=_B
_Xgs360028fPortSecLimitCtrlPortMode_Object=MibTableColumn
xgs360028fPortSecLimitCtrlPortMode=_Xgs360028fPortSecLimitCtrlPortMode_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,1,2,1,2),_Xgs360028fPortSecLimitCtrlPortMode_Type())
xgs360028fPortSecLimitCtrlPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortSecLimitCtrlPortMode.setStatus(_A)
class _Xgs360028fPortSecLimitCtrlPortLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Xgs360028fPortSecLimitCtrlPortLimit_Type.__name__=_B
_Xgs360028fPortSecLimitCtrlPortLimit_Object=MibTableColumn
xgs360028fPortSecLimitCtrlPortLimit=_Xgs360028fPortSecLimitCtrlPortLimit_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,1,2,1,3),_Xgs360028fPortSecLimitCtrlPortLimit_Type())
xgs360028fPortSecLimitCtrlPortLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortSecLimitCtrlPortLimit.setStatus(_A)
class _Xgs360028fPortSecLimitCtrlPortAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360028fPortSecLimitCtrlPortAction_Type.__name__=_B
_Xgs360028fPortSecLimitCtrlPortAction_Object=MibTableColumn
xgs360028fPortSecLimitCtrlPortAction=_Xgs360028fPortSecLimitCtrlPortAction_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,1,2,1,4),_Xgs360028fPortSecLimitCtrlPortAction_Type())
xgs360028fPortSecLimitCtrlPortAction.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortSecLimitCtrlPortAction.setStatus(_A)
_Xgs360028fPortSecLimitCtrlPortState_Type=DisplayString
_Xgs360028fPortSecLimitCtrlPortState_Object=MibTableColumn
xgs360028fPortSecLimitCtrlPortState=_Xgs360028fPortSecLimitCtrlPortState_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,1,2,1,5),_Xgs360028fPortSecLimitCtrlPortState_Type())
xgs360028fPortSecLimitCtrlPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortSecLimitCtrlPortState.setStatus(_A)
class _Xgs360028fPortSecLimitCtrlPortReOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fPortSecLimitCtrlPortReOpen_Type.__name__=_B
_Xgs360028fPortSecLimitCtrlPortReOpen_Object=MibTableColumn
xgs360028fPortSecLimitCtrlPortReOpen=_Xgs360028fPortSecLimitCtrlPortReOpen_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,1,2,1,6),_Xgs360028fPortSecLimitCtrlPortReOpen_Type())
xgs360028fPortSecLimitCtrlPortReOpen.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortSecLimitCtrlPortReOpen.setStatus(_A)
_Xgs360028fPortSecSwitchStatusTable_Object=MibTable
xgs360028fPortSecSwitchStatusTable=_Xgs360028fPortSecSwitchStatusTable_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,2))
if mibBuilder.loadTexts:xgs360028fPortSecSwitchStatusTable.setStatus(_A)
_Xgs360028fPortSecSwitchStatusEntry_Object=MibTableRow
xgs360028fPortSecSwitchStatusEntry=_Xgs360028fPortSecSwitchStatusEntry_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,2,1))
xgs360028fPortSecSwitchStatusEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:xgs360028fPortSecSwitchStatusEntry.setStatus(_A)
class _Xgs360028fPortSecSwitchStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fPortSecSwitchStatusPort_Type.__name__=_B
_Xgs360028fPortSecSwitchStatusPort_Object=MibTableColumn
xgs360028fPortSecSwitchStatusPort=_Xgs360028fPortSecSwitchStatusPort_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,2,1,1),_Xgs360028fPortSecSwitchStatusPort_Type())
xgs360028fPortSecSwitchStatusPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fPortSecSwitchStatusPort.setStatus(_A)
_Xgs360028fPortSecSwitchStatusUsers_Type=DisplayString
_Xgs360028fPortSecSwitchStatusUsers_Object=MibTableColumn
xgs360028fPortSecSwitchStatusUsers=_Xgs360028fPortSecSwitchStatusUsers_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,2,1,2),_Xgs360028fPortSecSwitchStatusUsers_Type())
xgs360028fPortSecSwitchStatusUsers.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortSecSwitchStatusUsers.setStatus(_A)
_Xgs360028fPortSecSwitchStatusState_Type=DisplayString
_Xgs360028fPortSecSwitchStatusState_Object=MibTableColumn
xgs360028fPortSecSwitchStatusState=_Xgs360028fPortSecSwitchStatusState_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,2,1,3),_Xgs360028fPortSecSwitchStatusState_Type())
xgs360028fPortSecSwitchStatusState.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortSecSwitchStatusState.setStatus(_A)
class _Xgs360028fPortSecSwitchStatusMACCountCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fPortSecSwitchStatusMACCountCurrent_Type.__name__=_B
_Xgs360028fPortSecSwitchStatusMACCountCurrent_Object=MibTableColumn
xgs360028fPortSecSwitchStatusMACCountCurrent=_Xgs360028fPortSecSwitchStatusMACCountCurrent_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,2,1,4),_Xgs360028fPortSecSwitchStatusMACCountCurrent_Type())
xgs360028fPortSecSwitchStatusMACCountCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortSecSwitchStatusMACCountCurrent.setStatus(_A)
class _Xgs360028fPortSecSwitchStatusMACCountLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fPortSecSwitchStatusMACCountLimit_Type.__name__=_B
_Xgs360028fPortSecSwitchStatusMACCountLimit_Object=MibTableColumn
xgs360028fPortSecSwitchStatusMACCountLimit=_Xgs360028fPortSecSwitchStatusMACCountLimit_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,2,1,5),_Xgs360028fPortSecSwitchStatusMACCountLimit_Type())
xgs360028fPortSecSwitchStatusMACCountLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortSecSwitchStatusMACCountLimit.setStatus(_A)
_Xgs360028fPortSecPortStatus_ObjectIdentity=ObjectIdentity
xgs360028fPortSecPortStatus=_Xgs360028fPortSecPortStatus_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,5,3))
class _Xgs360028fPortSecPortStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fPortSecPortStatusPort_Type.__name__=_B
_Xgs360028fPortSecPortStatusPort_Object=MibScalar
xgs360028fPortSecPortStatusPort=_Xgs360028fPortSecPortStatusPort_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,3,1),_Xgs360028fPortSecPortStatusPort_Type())
xgs360028fPortSecPortStatusPort.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPortSecPortStatusPort.setStatus(_A)
_Xgs360028fPortSecPortStatusTable_Object=MibTable
xgs360028fPortSecPortStatusTable=_Xgs360028fPortSecPortStatusTable_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,3,2))
if mibBuilder.loadTexts:xgs360028fPortSecPortStatusTable.setStatus(_A)
_Xgs360028fPortSecPortStatusEntry_Object=MibTableRow
xgs360028fPortSecPortStatusEntry=_Xgs360028fPortSecPortStatusEntry_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,3,2,1))
xgs360028fPortSecPortStatusEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:xgs360028fPortSecPortStatusEntry.setStatus(_A)
class _Xgs360028fPortSecPortStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fPortSecPortStatusIndex_Type.__name__=_B
_Xgs360028fPortSecPortStatusIndex_Object=MibTableColumn
xgs360028fPortSecPortStatusIndex=_Xgs360028fPortSecPortStatusIndex_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,3,2,1,1),_Xgs360028fPortSecPortStatusIndex_Type())
xgs360028fPortSecPortStatusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fPortSecPortStatusIndex.setStatus(_A)
_Xgs360028fPortSecPortStatusMACAddress_Type=MacAddress
_Xgs360028fPortSecPortStatusMACAddress_Object=MibTableColumn
xgs360028fPortSecPortStatusMACAddress=_Xgs360028fPortSecPortStatusMACAddress_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,3,2,1,2),_Xgs360028fPortSecPortStatusMACAddress_Type())
xgs360028fPortSecPortStatusMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortSecPortStatusMACAddress.setStatus(_A)
class _Xgs360028fPortSecPortStatusVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Xgs360028fPortSecPortStatusVLANId_Type.__name__=_B
_Xgs360028fPortSecPortStatusVLANId_Object=MibTableColumn
xgs360028fPortSecPortStatusVLANId=_Xgs360028fPortSecPortStatusVLANId_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,3,2,1,3),_Xgs360028fPortSecPortStatusVLANId_Type())
xgs360028fPortSecPortStatusVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortSecPortStatusVLANId.setStatus(_A)
_Xgs360028fPortSecPortStatusState_Type=DisplayString
_Xgs360028fPortSecPortStatusState_Object=MibTableColumn
xgs360028fPortSecPortStatusState=_Xgs360028fPortSecPortStatusState_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,3,2,1,4),_Xgs360028fPortSecPortStatusState_Type())
xgs360028fPortSecPortStatusState.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortSecPortStatusState.setStatus(_A)
_Xgs360028fPortSecPortStatusTimeOfAddition_Type=DisplayString
_Xgs360028fPortSecPortStatusTimeOfAddition_Object=MibTableColumn
xgs360028fPortSecPortStatusTimeOfAddition=_Xgs360028fPortSecPortStatusTimeOfAddition_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,3,2,1,5),_Xgs360028fPortSecPortStatusTimeOfAddition_Type())
xgs360028fPortSecPortStatusTimeOfAddition.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortSecPortStatusTimeOfAddition.setStatus(_A)
_Xgs360028fPortSecPortStatusAgeAndHold_Type=DisplayString
_Xgs360028fPortSecPortStatusAgeAndHold_Object=MibTableColumn
xgs360028fPortSecPortStatusAgeAndHold=_Xgs360028fPortSecPortStatusAgeAndHold_Object((1,3,6,1,4,1,890,1,5,8,78,3,5,3,2,1,6),_Xgs360028fPortSecPortStatusAgeAndHold_Type())
xgs360028fPortSecPortStatusAgeAndHold.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPortSecPortStatusAgeAndHold.setStatus(_A)
_Xgs360028fAccessManagement_ObjectIdentity=ObjectIdentity
xgs360028fAccessManagement=_Xgs360028fAccessManagement_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,6))
_Xgs360028fAccessMgtConf_ObjectIdentity=ObjectIdentity
xgs360028fAccessMgtConf=_Xgs360028fAccessMgtConf_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,6,1))
class _Xgs360028fAccessMgtConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fAccessMgtConfMode_Type.__name__=_B
_Xgs360028fAccessMgtConfMode_Object=MibScalar
xgs360028fAccessMgtConfMode=_Xgs360028fAccessMgtConfMode_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,1,1),_Xgs360028fAccessMgtConfMode_Type())
xgs360028fAccessMgtConfMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fAccessMgtConfMode.setStatus(_A)
class _Xgs360028fAccessMgtConfCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fAccessMgtConfCreate_Type.__name__=_B
_Xgs360028fAccessMgtConfCreate_Object=MibScalar
xgs360028fAccessMgtConfCreate=_Xgs360028fAccessMgtConfCreate_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,1,2),_Xgs360028fAccessMgtConfCreate_Type())
xgs360028fAccessMgtConfCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fAccessMgtConfCreate.setStatus(_A)
_Xgs360028fAccessMgtConfTable_Object=MibTable
xgs360028fAccessMgtConfTable=_Xgs360028fAccessMgtConfTable_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,1,3))
if mibBuilder.loadTexts:xgs360028fAccessMgtConfTable.setStatus(_A)
_Xgs360028fAccessMgtConfEntry_Object=MibTableRow
xgs360028fAccessMgtConfEntry=_Xgs360028fAccessMgtConfEntry_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,1,3,1))
xgs360028fAccessMgtConfEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:xgs360028fAccessMgtConfEntry.setStatus(_A)
class _Xgs360028fAccessMgtIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Xgs360028fAccessMgtIndex_Type.__name__=_B
_Xgs360028fAccessMgtIndex_Object=MibTableColumn
xgs360028fAccessMgtIndex=_Xgs360028fAccessMgtIndex_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,1,3,1,1),_Xgs360028fAccessMgtIndex_Type())
xgs360028fAccessMgtIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fAccessMgtIndex.setStatus(_A)
class _Xgs360028fAccessMgtAddresstype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fAccessMgtAddresstype_Type.__name__=_B
_Xgs360028fAccessMgtAddresstype_Object=MibTableColumn
xgs360028fAccessMgtAddresstype=_Xgs360028fAccessMgtAddresstype_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,1,3,1,2),_Xgs360028fAccessMgtAddresstype_Type())
xgs360028fAccessMgtAddresstype.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fAccessMgtAddresstype.setStatus(_A)
_Xgs360028fAccessMgtStartIpAddress_Type=DisplayString
_Xgs360028fAccessMgtStartIpAddress_Object=MibTableColumn
xgs360028fAccessMgtStartIpAddress=_Xgs360028fAccessMgtStartIpAddress_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,1,3,1,3),_Xgs360028fAccessMgtStartIpAddress_Type())
xgs360028fAccessMgtStartIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fAccessMgtStartIpAddress.setStatus(_A)
_Xgs360028fAccessMgtEndIpAddress_Type=DisplayString
_Xgs360028fAccessMgtEndIpAddress_Object=MibTableColumn
xgs360028fAccessMgtEndIpAddress=_Xgs360028fAccessMgtEndIpAddress_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,1,3,1,4),_Xgs360028fAccessMgtEndIpAddress_Type())
xgs360028fAccessMgtEndIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fAccessMgtEndIpAddress.setStatus(_A)
class _Xgs360028fAccessMgtHttpHttps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fAccessMgtHttpHttps_Type.__name__=_B
_Xgs360028fAccessMgtHttpHttps_Object=MibTableColumn
xgs360028fAccessMgtHttpHttps=_Xgs360028fAccessMgtHttpHttps_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,1,3,1,5),_Xgs360028fAccessMgtHttpHttps_Type())
xgs360028fAccessMgtHttpHttps.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fAccessMgtHttpHttps.setStatus(_A)
class _Xgs360028fAccessMgtSNMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fAccessMgtSNMP_Type.__name__=_B
_Xgs360028fAccessMgtSNMP_Object=MibTableColumn
xgs360028fAccessMgtSNMP=_Xgs360028fAccessMgtSNMP_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,1,3,1,6),_Xgs360028fAccessMgtSNMP_Type())
xgs360028fAccessMgtSNMP.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fAccessMgtSNMP.setStatus(_A)
class _Xgs360028fAccessMgtTelnetSSH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fAccessMgtTelnetSSH_Type.__name__=_B
_Xgs360028fAccessMgtTelnetSSH_Object=MibTableColumn
xgs360028fAccessMgtTelnetSSH=_Xgs360028fAccessMgtTelnetSSH_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,1,3,1,7),_Xgs360028fAccessMgtTelnetSSH_Type())
xgs360028fAccessMgtTelnetSSH.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fAccessMgtTelnetSSH.setStatus(_A)
class _Xgs360028fAccessMgtRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Xgs360028fAccessMgtRowStatus_Type.__name__=_B
_Xgs360028fAccessMgtRowStatus_Object=MibTableColumn
xgs360028fAccessMgtRowStatus=_Xgs360028fAccessMgtRowStatus_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,1,3,1,8),_Xgs360028fAccessMgtRowStatus_Type())
xgs360028fAccessMgtRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fAccessMgtRowStatus.setStatus(_A)
_Xgs360028fAccessMgtStatistics_ObjectIdentity=ObjectIdentity
xgs360028fAccessMgtStatistics=_Xgs360028fAccessMgtStatistics_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,6,2))
_Xgs360028fHttpReceivedPkts_Type=Counter32
_Xgs360028fHttpReceivedPkts_Object=MibScalar
xgs360028fHttpReceivedPkts=_Xgs360028fHttpReceivedPkts_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,1),_Xgs360028fHttpReceivedPkts_Type())
xgs360028fHttpReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fHttpReceivedPkts.setStatus(_A)
_Xgs360028fHttpAllowedPkts_Type=Counter32
_Xgs360028fHttpAllowedPkts_Object=MibScalar
xgs360028fHttpAllowedPkts=_Xgs360028fHttpAllowedPkts_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,2),_Xgs360028fHttpAllowedPkts_Type())
xgs360028fHttpAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fHttpAllowedPkts.setStatus(_A)
_Xgs360028fHttpDiscardedPkts_Type=Counter32
_Xgs360028fHttpDiscardedPkts_Object=MibScalar
xgs360028fHttpDiscardedPkts=_Xgs360028fHttpDiscardedPkts_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,3),_Xgs360028fHttpDiscardedPkts_Type())
xgs360028fHttpDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fHttpDiscardedPkts.setStatus(_A)
_Xgs360028fHttpsReceivedPkts_Type=Counter32
_Xgs360028fHttpsReceivedPkts_Object=MibScalar
xgs360028fHttpsReceivedPkts=_Xgs360028fHttpsReceivedPkts_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,4),_Xgs360028fHttpsReceivedPkts_Type())
xgs360028fHttpsReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fHttpsReceivedPkts.setStatus(_A)
_Xgs360028fHttpsAllowedPkts_Type=Counter32
_Xgs360028fHttpsAllowedPkts_Object=MibScalar
xgs360028fHttpsAllowedPkts=_Xgs360028fHttpsAllowedPkts_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,5),_Xgs360028fHttpsAllowedPkts_Type())
xgs360028fHttpsAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fHttpsAllowedPkts.setStatus(_A)
_Xgs360028fHttpsDiscardedPkts_Type=Counter32
_Xgs360028fHttpsDiscardedPkts_Object=MibScalar
xgs360028fHttpsDiscardedPkts=_Xgs360028fHttpsDiscardedPkts_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,6),_Xgs360028fHttpsDiscardedPkts_Type())
xgs360028fHttpsDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fHttpsDiscardedPkts.setStatus(_A)
_Xgs360028fSnmpReceivedPkts_Type=Counter32
_Xgs360028fSnmpReceivedPkts_Object=MibScalar
xgs360028fSnmpReceivedPkts=_Xgs360028fSnmpReceivedPkts_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,7),_Xgs360028fSnmpReceivedPkts_Type())
xgs360028fSnmpReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSnmpReceivedPkts.setStatus(_A)
_Xgs360028fSnmpAllowedPkts_Type=Counter32
_Xgs360028fSnmpAllowedPkts_Object=MibScalar
xgs360028fSnmpAllowedPkts=_Xgs360028fSnmpAllowedPkts_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,8),_Xgs360028fSnmpAllowedPkts_Type())
xgs360028fSnmpAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSnmpAllowedPkts.setStatus(_A)
_Xgs360028fSnmpDiscardedPkts_Type=Counter32
_Xgs360028fSnmpDiscardedPkts_Object=MibScalar
xgs360028fSnmpDiscardedPkts=_Xgs360028fSnmpDiscardedPkts_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,9),_Xgs360028fSnmpDiscardedPkts_Type())
xgs360028fSnmpDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSnmpDiscardedPkts.setStatus(_A)
_Xgs360028fTelnetReceivedPkts_Type=Counter32
_Xgs360028fTelnetReceivedPkts_Object=MibScalar
xgs360028fTelnetReceivedPkts=_Xgs360028fTelnetReceivedPkts_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,10),_Xgs360028fTelnetReceivedPkts_Type())
xgs360028fTelnetReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fTelnetReceivedPkts.setStatus(_A)
_Xgs360028fTelnetAllowedPkts_Type=Counter32
_Xgs360028fTelnetAllowedPkts_Object=MibScalar
xgs360028fTelnetAllowedPkts=_Xgs360028fTelnetAllowedPkts_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,11),_Xgs360028fTelnetAllowedPkts_Type())
xgs360028fTelnetAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fTelnetAllowedPkts.setStatus(_A)
_Xgs360028fTelnetDiscardedPkts_Type=Counter32
_Xgs360028fTelnetDiscardedPkts_Object=MibScalar
xgs360028fTelnetDiscardedPkts=_Xgs360028fTelnetDiscardedPkts_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,12),_Xgs360028fTelnetDiscardedPkts_Type())
xgs360028fTelnetDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fTelnetDiscardedPkts.setStatus(_A)
_Xgs360028fSSHReceivedPkts_Type=Counter32
_Xgs360028fSSHReceivedPkts_Object=MibScalar
xgs360028fSSHReceivedPkts=_Xgs360028fSSHReceivedPkts_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,13),_Xgs360028fSSHReceivedPkts_Type())
xgs360028fSSHReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSSHReceivedPkts.setStatus(_A)
_Xgs360028fSSHAllowedPkts_Type=Counter32
_Xgs360028fSSHAllowedPkts_Object=MibScalar
xgs360028fSSHAllowedPkts=_Xgs360028fSSHAllowedPkts_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,14),_Xgs360028fSSHAllowedPkts_Type())
xgs360028fSSHAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSSHAllowedPkts.setStatus(_A)
_Xgs360028fSSHDiscardedPkts_Type=Counter32
_Xgs360028fSSHDiscardedPkts_Object=MibScalar
xgs360028fSSHDiscardedPkts=_Xgs360028fSSHDiscardedPkts_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,15),_Xgs360028fSSHDiscardedPkts_Type())
xgs360028fSSHDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fSSHDiscardedPkts.setStatus(_A)
class _Xgs360028fAccessMgtStatisticsClearAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fAccessMgtStatisticsClearAll_Type.__name__=_B
_Xgs360028fAccessMgtStatisticsClearAll_Object=MibScalar
xgs360028fAccessMgtStatisticsClearAll=_Xgs360028fAccessMgtStatisticsClearAll_Object((1,3,6,1,4,1,890,1,5,8,78,3,6,2,16),_Xgs360028fAccessMgtStatisticsClearAll_Type())
xgs360028fAccessMgtStatisticsClearAll.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fAccessMgtStatisticsClearAll.setStatus(_A)
_Xgs360028fSSH_ObjectIdentity=ObjectIdentity
xgs360028fSSH=_Xgs360028fSSH_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,7))
class _Xgs360028fSSHMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fSSHMode_Type.__name__=_B
_Xgs360028fSSHMode_Object=MibScalar
xgs360028fSSHMode=_Xgs360028fSSHMode_Object((1,3,6,1,4,1,890,1,5,8,78,3,7,1),_Xgs360028fSSHMode_Type())
xgs360028fSSHMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSSHMode.setStatus(_A)
_Xgs360028fHTTPS_ObjectIdentity=ObjectIdentity
xgs360028fHTTPS=_Xgs360028fHTTPS_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,8))
class _Xgs360028fHTTPSMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fHTTPSMode_Type.__name__=_B
_Xgs360028fHTTPSMode_Object=MibScalar
xgs360028fHTTPSMode=_Xgs360028fHTTPSMode_Object((1,3,6,1,4,1,890,1,5,8,78,3,8,1),_Xgs360028fHTTPSMode_Type())
xgs360028fHTTPSMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fHTTPSMode.setStatus(_A)
class _Xgs360028fHTTPSAutoRedirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fHTTPSAutoRedirect_Type.__name__=_B
_Xgs360028fHTTPSAutoRedirect_Object=MibScalar
xgs360028fHTTPSAutoRedirect=_Xgs360028fHTTPSAutoRedirect_Object((1,3,6,1,4,1,890,1,5,8,78,3,8,2),_Xgs360028fHTTPSAutoRedirect_Type())
xgs360028fHTTPSAutoRedirect.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fHTTPSAutoRedirect.setStatus(_A)
_Xgs360028fAuthMethod_ObjectIdentity=ObjectIdentity
xgs360028fAuthMethod=_Xgs360028fAuthMethod_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,3,9))
class _Xgs360028fConsoleAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360028fConsoleAuthMethod_Type.__name__=_B
_Xgs360028fConsoleAuthMethod_Object=MibScalar
xgs360028fConsoleAuthMethod=_Xgs360028fConsoleAuthMethod_Object((1,3,6,1,4,1,890,1,5,8,78,3,9,1),_Xgs360028fConsoleAuthMethod_Type())
xgs360028fConsoleAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fConsoleAuthMethod.setStatus(_A)
class _Xgs360028fConsoleFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fConsoleFallback_Type.__name__=_B
_Xgs360028fConsoleFallback_Object=MibScalar
xgs360028fConsoleFallback=_Xgs360028fConsoleFallback_Object((1,3,6,1,4,1,890,1,5,8,78,3,9,2),_Xgs360028fConsoleFallback_Type())
xgs360028fConsoleFallback.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fConsoleFallback.setStatus(_A)
class _Xgs360028fTelnetAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360028fTelnetAuthMethod_Type.__name__=_B
_Xgs360028fTelnetAuthMethod_Object=MibScalar
xgs360028fTelnetAuthMethod=_Xgs360028fTelnetAuthMethod_Object((1,3,6,1,4,1,890,1,5,8,78,3,9,3),_Xgs360028fTelnetAuthMethod_Type())
xgs360028fTelnetAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTelnetAuthMethod.setStatus(_A)
class _Xgs360028fTelnetFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fTelnetFallback_Type.__name__=_B
_Xgs360028fTelnetFallback_Object=MibScalar
xgs360028fTelnetFallback=_Xgs360028fTelnetFallback_Object((1,3,6,1,4,1,890,1,5,8,78,3,9,4),_Xgs360028fTelnetFallback_Type())
xgs360028fTelnetFallback.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fTelnetFallback.setStatus(_A)
class _Xgs360028fSshAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360028fSshAuthMethod_Type.__name__=_B
_Xgs360028fSshAuthMethod_Object=MibScalar
xgs360028fSshAuthMethod=_Xgs360028fSshAuthMethod_Object((1,3,6,1,4,1,890,1,5,8,78,3,9,5),_Xgs360028fSshAuthMethod_Type())
xgs360028fSshAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSshAuthMethod.setStatus(_A)
class _Xgs360028fSshFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fSshFallback_Type.__name__=_B
_Xgs360028fSshFallback_Object=MibScalar
xgs360028fSshFallback=_Xgs360028fSshFallback_Object((1,3,6,1,4,1,890,1,5,8,78,3,9,6),_Xgs360028fSshFallback_Type())
xgs360028fSshFallback.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSshFallback.setStatus(_A)
class _Xgs360028fWebAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Xgs360028fWebAuthMethod_Type.__name__=_B
_Xgs360028fWebAuthMethod_Object=MibScalar
xgs360028fWebAuthMethod=_Xgs360028fWebAuthMethod_Object((1,3,6,1,4,1,890,1,5,8,78,3,9,7),_Xgs360028fWebAuthMethod_Type())
xgs360028fWebAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fWebAuthMethod.setStatus(_A)
class _Xgs360028fWebFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fWebFallback_Type.__name__=_B
_Xgs360028fWebFallback_Object=MibScalar
xgs360028fWebFallback=_Xgs360028fWebFallback_Object((1,3,6,1,4,1,890,1,5,8,78,3,9,8),_Xgs360028fWebFallback_Type())
xgs360028fWebFallback.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fWebFallback.setStatus(_A)
_Xgs360028fMaintenance_ObjectIdentity=ObjectIdentity
xgs360028fMaintenance=_Xgs360028fMaintenance_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,4))
class _Xgs360028fRestartDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fRestartDevice_Type.__name__=_B
_Xgs360028fRestartDevice_Object=MibScalar
xgs360028fRestartDevice=_Xgs360028fRestartDevice_Object((1,3,6,1,4,1,890,1,5,8,78,4,1),_Xgs360028fRestartDevice_Type())
xgs360028fRestartDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fRestartDevice.setStatus(_A)
_Xgs360028fFirmware_ObjectIdentity=ObjectIdentity
xgs360028fFirmware=_Xgs360028fFirmware_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,4,2))
_Xgs360028fFirmwareIpAddress_Type=IpAddress
_Xgs360028fFirmwareIpAddress_Object=MibScalar
xgs360028fFirmwareIpAddress=_Xgs360028fFirmwareIpAddress_Object((1,3,6,1,4,1,890,1,5,8,78,4,2,1),_Xgs360028fFirmwareIpAddress_Type())
xgs360028fFirmwareIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fFirmwareIpAddress.setStatus(_A)
_Xgs360028fFirmwareFileName_Type=DisplayString
_Xgs360028fFirmwareFileName_Object=MibScalar
xgs360028fFirmwareFileName=_Xgs360028fFirmwareFileName_Object((1,3,6,1,4,1,890,1,5,8,78,4,2,2),_Xgs360028fFirmwareFileName_Type())
xgs360028fFirmwareFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fFirmwareFileName.setStatus(_A)
class _Xgs360028fDoFirmwareUpgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fDoFirmwareUpgrade_Type.__name__=_B
_Xgs360028fDoFirmwareUpgrade_Object=MibScalar
xgs360028fDoFirmwareUpgrade=_Xgs360028fDoFirmwareUpgrade_Object((1,3,6,1,4,1,890,1,5,8,78,4,2,3),_Xgs360028fDoFirmwareUpgrade_Type())
xgs360028fDoFirmwareUpgrade.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fDoFirmwareUpgrade.setStatus(_A)
_Xgs360028fSaveOrRestore_ObjectIdentity=ObjectIdentity
xgs360028fSaveOrRestore=_Xgs360028fSaveOrRestore_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,4,3))
class _Xgs360028fFactoryDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fFactoryDefaults_Type.__name__=_B
_Xgs360028fFactoryDefaults_Object=MibScalar
xgs360028fFactoryDefaults=_Xgs360028fFactoryDefaults_Object((1,3,6,1,4,1,890,1,5,8,78,4,3,1),_Xgs360028fFactoryDefaults_Type())
xgs360028fFactoryDefaults.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fFactoryDefaults.setStatus(_A)
class _Xgs360028fSaveStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fSaveStart_Type.__name__=_B
_Xgs360028fSaveStart_Object=MibScalar
xgs360028fSaveStart=_Xgs360028fSaveStart_Object((1,3,6,1,4,1,890,1,5,8,78,4,3,2),_Xgs360028fSaveStart_Type())
xgs360028fSaveStart.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSaveStart.setStatus(_A)
class _Xgs360028fSaveUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fSaveUser_Type.__name__=_B
_Xgs360028fSaveUser_Object=MibScalar
xgs360028fSaveUser=_Xgs360028fSaveUser_Object((1,3,6,1,4,1,890,1,5,8,78,4,3,3),_Xgs360028fSaveUser_Type())
xgs360028fSaveUser.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fSaveUser.setStatus(_A)
class _Xgs360028fRestoreUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Xgs360028fRestoreUser_Type.__name__=_B
_Xgs360028fRestoreUser_Object=MibScalar
xgs360028fRestoreUser=_Xgs360028fRestoreUser_Object((1,3,6,1,4,1,890,1,5,8,78,4,3,4),_Xgs360028fRestoreUser_Type())
xgs360028fRestoreUser.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fRestoreUser.setStatus(_A)
_Xgs360028fExportOrImport_ObjectIdentity=ObjectIdentity
xgs360028fExportOrImport=_Xgs360028fExportOrImport_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,4,4))
_Xgs360028fExportIpAddress_Type=IpAddress
_Xgs360028fExportIpAddress_Object=MibScalar
xgs360028fExportIpAddress=_Xgs360028fExportIpAddress_Object((1,3,6,1,4,1,890,1,5,8,78,4,4,1),_Xgs360028fExportIpAddress_Type())
xgs360028fExportIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fExportIpAddress.setStatus(_A)
_Xgs360028fExportConfigName_Type=DisplayString
_Xgs360028fExportConfigName_Object=MibScalar
xgs360028fExportConfigName=_Xgs360028fExportConfigName_Object((1,3,6,1,4,1,890,1,5,8,78,4,4,2),_Xgs360028fExportConfigName_Type())
xgs360028fExportConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fExportConfigName.setStatus(_A)
class _Xgs360028fDoExportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Xgs360028fDoExportConfig_Type.__name__=_B
_Xgs360028fDoExportConfig_Object=MibScalar
xgs360028fDoExportConfig=_Xgs360028fDoExportConfig_Object((1,3,6,1,4,1,890,1,5,8,78,4,4,3),_Xgs360028fDoExportConfig_Type())
xgs360028fDoExportConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fDoExportConfig.setStatus(_A)
_Xgs360028fImportIpAddress_Type=IpAddress
_Xgs360028fImportIpAddress_Object=MibScalar
xgs360028fImportIpAddress=_Xgs360028fImportIpAddress_Object((1,3,6,1,4,1,890,1,5,8,78,4,4,4),_Xgs360028fImportIpAddress_Type())
xgs360028fImportIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fImportIpAddress.setStatus(_A)
_Xgs360028fImportConfigName_Type=DisplayString
_Xgs360028fImportConfigName_Object=MibScalar
xgs360028fImportConfigName=_Xgs360028fImportConfigName_Object((1,3,6,1,4,1,890,1,5,8,78,4,4,5),_Xgs360028fImportConfigName_Type())
xgs360028fImportConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fImportConfigName.setStatus(_A)
class _Xgs360028fDoImportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Xgs360028fDoImportConfig_Type.__name__=_B
_Xgs360028fDoImportConfig_Object=MibScalar
xgs360028fDoImportConfig=_Xgs360028fDoImportConfig_Object((1,3,6,1,4,1,890,1,5,8,78,4,4,6),_Xgs360028fDoImportConfig_Type())
xgs360028fDoImportConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fDoImportConfig.setStatus(_A)
_Xgs360028fDiagnostics_ObjectIdentity=ObjectIdentity
xgs360028fDiagnostics=_Xgs360028fDiagnostics_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,4,5))
_Xgs360028fPingIpAddress_Type=IpAddress
_Xgs360028fPingIpAddress_Object=MibScalar
xgs360028fPingIpAddress=_Xgs360028fPingIpAddress_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,1),_Xgs360028fPingIpAddress_Type())
xgs360028fPingIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPingIpAddress.setStatus(_A)
class _Xgs360028fPingSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,1400))
_Xgs360028fPingSize_Type.__name__=_B
_Xgs360028fPingSize_Object=MibScalar
xgs360028fPingSize=_Xgs360028fPingSize_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,2),_Xgs360028fPingSize_Type())
xgs360028fPingSize.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPingSize.setStatus(_A)
class _Xgs360028fDoPingConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Xgs360028fDoPingConfig_Type.__name__=_B
_Xgs360028fDoPingConfig_Object=MibScalar
xgs360028fDoPingConfig=_Xgs360028fDoPingConfig_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,3),_Xgs360028fDoPingConfig_Type())
xgs360028fDoPingConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fDoPingConfig.setStatus(_A)
_Xgs360028fPingResult_Type=DisplayString
_Xgs360028fPingResult_Object=MibScalar
xgs360028fPingResult=_Xgs360028fPingResult_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,4),_Xgs360028fPingResult_Type())
xgs360028fPingResult.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPingResult.setStatus(_A)
_Xgs360028fPing6IpAddress_Type=DisplayString
_Xgs360028fPing6IpAddress_Object=MibScalar
xgs360028fPing6IpAddress=_Xgs360028fPing6IpAddress_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,5),_Xgs360028fPing6IpAddress_Type())
xgs360028fPing6IpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPing6IpAddress.setStatus(_A)
class _Xgs360028fPing6Size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,1400))
_Xgs360028fPing6Size_Type.__name__=_B
_Xgs360028fPing6Size_Object=MibScalar
xgs360028fPing6Size=_Xgs360028fPing6Size_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,6),_Xgs360028fPing6Size_Type())
xgs360028fPing6Size.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fPing6Size.setStatus(_A)
class _Xgs360028fDoPing6Config_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Xgs360028fDoPing6Config_Type.__name__=_B
_Xgs360028fDoPing6Config_Object=MibScalar
xgs360028fDoPing6Config=_Xgs360028fDoPing6Config_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,7),_Xgs360028fDoPing6Config_Type())
xgs360028fDoPing6Config.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fDoPing6Config.setStatus(_A)
_Xgs360028fPing6Result_Type=DisplayString
_Xgs360028fPing6Result_Object=MibScalar
xgs360028fPing6Result=_Xgs360028fPing6Result_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,8),_Xgs360028fPing6Result_Type())
xgs360028fPing6Result.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fPing6Result.setStatus(_A)
_Xgs360028fVeriPHY_ObjectIdentity=ObjectIdentity
xgs360028fVeriPHY=_Xgs360028fVeriPHY_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,4,5,9))
class _Xgs360028fVeriPHYTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fVeriPHYTest_Type.__name__=_B
_Xgs360028fVeriPHYTest_Object=MibScalar
xgs360028fVeriPHYTest=_Xgs360028fVeriPHYTest_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,9,1),_Xgs360028fVeriPHYTest_Type())
xgs360028fVeriPHYTest.setMaxAccess(_C)
if mibBuilder.loadTexts:xgs360028fVeriPHYTest.setStatus(_A)
_Xgs360028fVeriPHYTable_Object=MibTable
xgs360028fVeriPHYTable=_Xgs360028fVeriPHYTable_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,9,2))
if mibBuilder.loadTexts:xgs360028fVeriPHYTable.setStatus(_A)
_Xgs360028fVeriPHYEntry_Object=MibTableRow
xgs360028fVeriPHYEntry=_Xgs360028fVeriPHYEntry_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,9,2,1))
xgs360028fVeriPHYEntry.setIndexNames((0,_E,_s))
if mibBuilder.loadTexts:xgs360028fVeriPHYEntry.setStatus(_A)
class _Xgs360028fVeriPHYPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Xgs360028fVeriPHYPort_Type.__name__=_B
_Xgs360028fVeriPHYPort_Object=MibTableColumn
xgs360028fVeriPHYPort=_Xgs360028fVeriPHYPort_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,9,2,1,1),_Xgs360028fVeriPHYPort_Type())
xgs360028fVeriPHYPort.setMaxAccess(_F)
if mibBuilder.loadTexts:xgs360028fVeriPHYPort.setStatus(_A)
_Xgs360028fVeriPHYPairA_Type=DisplayString
_Xgs360028fVeriPHYPairA_Object=MibTableColumn
xgs360028fVeriPHYPairA=_Xgs360028fVeriPHYPairA_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,9,2,1,2),_Xgs360028fVeriPHYPairA_Type())
xgs360028fVeriPHYPairA.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fVeriPHYPairA.setStatus(_A)
_Xgs360028fVeriPHYLengthA_Type=DisplayString
_Xgs360028fVeriPHYLengthA_Object=MibTableColumn
xgs360028fVeriPHYLengthA=_Xgs360028fVeriPHYLengthA_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,9,2,1,3),_Xgs360028fVeriPHYLengthA_Type())
xgs360028fVeriPHYLengthA.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fVeriPHYLengthA.setStatus(_A)
_Xgs360028fVeriPHYPairB_Type=DisplayString
_Xgs360028fVeriPHYPairB_Object=MibTableColumn
xgs360028fVeriPHYPairB=_Xgs360028fVeriPHYPairB_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,9,2,1,4),_Xgs360028fVeriPHYPairB_Type())
xgs360028fVeriPHYPairB.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fVeriPHYPairB.setStatus(_A)
_Xgs360028fVeriPHYLengthB_Type=DisplayString
_Xgs360028fVeriPHYLengthB_Object=MibTableColumn
xgs360028fVeriPHYLengthB=_Xgs360028fVeriPHYLengthB_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,9,2,1,5),_Xgs360028fVeriPHYLengthB_Type())
xgs360028fVeriPHYLengthB.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fVeriPHYLengthB.setStatus(_A)
_Xgs360028fVeriPHYPairC_Type=DisplayString
_Xgs360028fVeriPHYPairC_Object=MibTableColumn
xgs360028fVeriPHYPairC=_Xgs360028fVeriPHYPairC_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,9,2,1,6),_Xgs360028fVeriPHYPairC_Type())
xgs360028fVeriPHYPairC.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fVeriPHYPairC.setStatus(_A)
_Xgs360028fVeriPHYLengthC_Type=DisplayString
_Xgs360028fVeriPHYLengthC_Object=MibTableColumn
xgs360028fVeriPHYLengthC=_Xgs360028fVeriPHYLengthC_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,9,2,1,7),_Xgs360028fVeriPHYLengthC_Type())
xgs360028fVeriPHYLengthC.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fVeriPHYLengthC.setStatus(_A)
_Xgs360028fVeriPHYPairD_Type=DisplayString
_Xgs360028fVeriPHYPairD_Object=MibTableColumn
xgs360028fVeriPHYPairD=_Xgs360028fVeriPHYPairD_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,9,2,1,8),_Xgs360028fVeriPHYPairD_Type())
xgs360028fVeriPHYPairD.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fVeriPHYPairD.setStatus(_A)
_Xgs360028fVeriPHYLengthD_Type=DisplayString
_Xgs360028fVeriPHYLengthD_Object=MibTableColumn
xgs360028fVeriPHYLengthD=_Xgs360028fVeriPHYLengthD_Object((1,3,6,1,4,1,890,1,5,8,78,4,5,9,2,1,9),_Xgs360028fVeriPHYLengthD_Type())
xgs360028fVeriPHYLengthD.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fVeriPHYLengthD.setStatus(_A)
_Xgs360028fTrap_ObjectIdentity=ObjectIdentity
xgs360028fTrap=_Xgs360028fTrap_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,5))
_Xgs360028fTrapEvent_ObjectIdentity=ObjectIdentity
xgs360028fTrapEvent=_Xgs360028fTrapEvent_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,5,1))
_Xgs360028fTrapVariable_ObjectIdentity=ObjectIdentity
xgs360028fTrapVariable=_Xgs360028fTrapVariable_ObjectIdentity((1,3,6,1,4,1,890,1,5,8,78,5,2))
_Xgs360028fInformation_Type=DisplayString
_Xgs360028fInformation_Object=MibScalar
xgs360028fInformation=_Xgs360028fInformation_Object((1,3,6,1,4,1,890,1,5,8,78,5,2,1),_Xgs360028fInformation_Type())
xgs360028fInformation.setMaxAccess(_D)
if mibBuilder.loadTexts:xgs360028fInformation.setStatus(_A)
xgs360028fEmergency=NotificationType((1,3,6,1,4,1,890,1,5,8,78,5,1,1))
xgs360028fEmergency.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360028fEmergency.setStatus(_A)
xgs360028fAlert=NotificationType((1,3,6,1,4,1,890,1,5,8,78,5,1,2))
xgs360028fAlert.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360028fAlert.setStatus(_A)
xgs360028fCritical=NotificationType((1,3,6,1,4,1,890,1,5,8,78,5,1,3))
xgs360028fCritical.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360028fCritical.setStatus(_A)
xgs360028fError=NotificationType((1,3,6,1,4,1,890,1,5,8,78,5,1,4))
xgs360028fError.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360028fError.setStatus(_A)
xgs360028fWarning=NotificationType((1,3,6,1,4,1,890,1,5,8,78,5,1,5))
xgs360028fWarning.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360028fWarning.setStatus(_A)
xgs360028fNotice=NotificationType((1,3,6,1,4,1,890,1,5,8,78,5,1,6))
xgs360028fNotice.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360028fNotice.setStatus(_A)
xgs360028fInformational=NotificationType((1,3,6,1,4,1,890,1,5,8,78,5,1,7))
xgs360028fInformational.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360028fInformational.setStatus(_A)
xgs360028fDebug=NotificationType((1,3,6,1,4,1,890,1,5,8,78,5,1,8))
xgs360028fDebug.setObjects((_E,_H))
if mibBuilder.loadTexts:xgs360028fDebug.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zyxel':zyxel,'products':products,'accessSwitch':accessSwitch,'esSeries':esSeries,'xgs360028fProductId':xgs360028fProductId,'xgs360028fSystem':xgs360028fSystem,'xgs360028fSystemInformation':xgs360028fSystemInformation,'xgs360028fModelName':xgs360028fModelName,'xgs360028fBIOSVersion':xgs360028fBIOSVersion,'xgs360028fFirmwareVersion':xgs360028fFirmwareVersion,'xgs360028fHardwareMechanicalVersion':xgs360028fHardwareMechanicalVersion,'xgs360028fSeriesNumber':xgs360028fSeriesNumber,'xgs360028fHostMACAddress':xgs360028fHostMACAddress,'xgs360028fConsoleBaudrate':xgs360028fConsoleBaudrate,'xgs360028fRAMSize':xgs360028fRAMSize,'xgs360028fFlashSize':xgs360028fFlashSize,'xgs360028fBridgeFBDSize':xgs360028fBridgeFBDSize,'xgs360028fTransmitQueue':xgs360028fTransmitQueue,'xgs360028fMaximumFrameSize':xgs360028fMaximumFrameSize,'xgs360028fCPULoad':xgs360028fCPULoad,'xgs360028fFanSpeed':xgs360028fFanSpeed,'xgs360028fPowers':xgs360028fPowers,'xgs360028fTemperature1':xgs360028fTemperature1,'xgs360028fTemperature2':xgs360028fTemperature2,'xgs360028fTemperature3':xgs360028fTemperature3,'xgs360028fTemperature4':xgs360028fTemperature4,'xgs360028fSystemTime':xgs360028fSystemTime,'xgs360028fSystemTimeManual':xgs360028fSystemTimeManual,'xgs360028fSystemTimeManualClockSource':xgs360028fSystemTimeManualClockSource,'xgs360028fSystemTimeManualLocaltime':xgs360028fSystemTimeManualLocaltime,'xgs360028fSystemTimeManualTimeZoneOffset':xgs360028fSystemTimeManualTimeZoneOffset,'xgs360028fSystemTimeManualDaylightSavings':xgs360028fSystemTimeManualDaylightSavings,'xgs360028fSystemTimeManualTimeSetOffset':xgs360028fSystemTimeManualTimeSetOffset,'xgs360028fSystemTimeManualDaylightSavingsType':xgs360028fSystemTimeManualDaylightSavingsType,'xgs360028fSystemTimeManualDaylightSavingsBydatesFrom':xgs360028fSystemTimeManualDaylightSavingsBydatesFrom,'xgs360028fSystemTimeManualDaylightSavingsBydatesTo':xgs360028fSystemTimeManualDaylightSavingsBydatesTo,'xgs360028fSystemTimeManualDaylightSavingsRecurringDayFrom':xgs360028fSystemTimeManualDaylightSavingsRecurringDayFrom,'xgs360028fSystemTimeManualDaylightSavingsRecurringWeekFrom':xgs360028fSystemTimeManualDaylightSavingsRecurringWeekFrom,'xgs360028fSystemTimeManualDaylightSavingsRecurringMonthFrom':xgs360028fSystemTimeManualDaylightSavingsRecurringMonthFrom,'xgs360028fSystemTimeManualDaylightSavingsRecurringTimeFrom':xgs360028fSystemTimeManualDaylightSavingsRecurringTimeFrom,'xgs360028fSystemTimeManualDaylightSavingsRecurringDayTo':xgs360028fSystemTimeManualDaylightSavingsRecurringDayTo,'xgs360028fSystemTimeManualDaylightSavingsRecurringWeekTo':xgs360028fSystemTimeManualDaylightSavingsRecurringWeekTo,'xgs360028fSystemTimeManualDaylightSavingsRecurringMonthTo':xgs360028fSystemTimeManualDaylightSavingsRecurringMonthTo,'xgs360028fSystemTimeManualDaylightSavingsRecurringTimeTo':xgs360028fSystemTimeManualDaylightSavingsRecurringTimeTo,'xgs360028fSystemTimeNTP':xgs360028fSystemTimeNTP,'xgs360028fSystemTimeNTPTable':xgs360028fSystemTimeNTPTable,'xgs360028fSystemTimeNTPEntry':xgs360028fSystemTimeNTPEntry,_J:xgs360028fSystemTimeNTPIndex,'xgs360028fSystemTimeNTPServerIPType':xgs360028fSystemTimeNTPServerIPType,'xgs360028fSystemTimeNTPServer':xgs360028fSystemTimeNTPServer,'xgs360028fSystemTimeNTPCurrentMode':xgs360028fSystemTimeNTPCurrentMode,'xgs360028fSystemAccount':xgs360028fSystemAccount,'xgs360028fSystemAccountUsers':xgs360028fSystemAccountUsers,'xgs360028fSystemAccountUserCreate':xgs360028fSystemAccountUserCreate,'xgs360028fSystemAccountUsersTable':xgs360028fSystemAccountUsersTable,'xgs360028fSystemAccountUsersEntry':xgs360028fSystemAccountUsersEntry,_K:xgs360028fUserIndex,'xgs360028fUserName':xgs360028fUserName,'xgs360028fPassword':xgs360028fPassword,'xgs360028fUserPrivilegeLevel':xgs360028fUserPrivilegeLevel,'xgs360028fAccountUserRowStatus':xgs360028fAccountUserRowStatus,'xgs360028fSystemAccountPrivilegeLevel':xgs360028fSystemAccountPrivilegeLevel,'xgs360028fAccountPrivilegeLevel':xgs360028fAccountPrivilegeLevel,'xgs360028fAggregationPrivilegeLevel':xgs360028fAggregationPrivilegeLevel,'xgs360028fDiagnosticsPrivilegeLevel':xgs360028fDiagnosticsPrivilegeLevel,'xgs360028fEPSPrivilegeLevel':xgs360028fEPSPrivilegeLevel,'xgs360028fERPSPrivilegeLevel':xgs360028fERPSPrivilegeLevel,'xgs360028fETHLinkOAMPrivilegeLevel':xgs360028fETHLinkOAMPrivilegeLevel,'xgs360028fEVCPrivilegeLevel':xgs360028fEVCPrivilegeLevel,'xgs360028fGARPPrivilegeLevel':xgs360028fGARPPrivilegeLevel,'xgs360028fGVRPPrivilegeLevel':xgs360028fGVRPPrivilegeLevel,'xgs360028fIPPrivilegeLevel':xgs360028fIPPrivilegeLevel,'xgs360028fIPMCSnoopingPrivilegeLevel':xgs360028fIPMCSnoopingPrivilegeLevel,'xgs360028fLACPPrivilegeLevel':xgs360028fLACPPrivilegeLevel,'xgs360028fLLDPPrivilegeLevel':xgs360028fLLDPPrivilegeLevel,'xgs360028fLLDPMEDPrivilegeLevel':xgs360028fLLDPMEDPrivilegeLevel,'xgs360028fLoopProtectPrivilegeLevel':xgs360028fLoopProtectPrivilegeLevel,'xgs360028fMACTablePrivilegeLevel':xgs360028fMACTablePrivilegeLevel,'xgs360028fMEPPrivilegeLevel':xgs360028fMEPPrivilegeLevel,'xgs360028fMRSTPPrivilegeLevel':xgs360028fMRSTPPrivilegeLevel,'xgs360028fMVRPrivilegeLevel':xgs360028fMVRPrivilegeLevel,'xgs360028fMaintenancePrivilegeLevel':xgs360028fMaintenancePrivilegeLevel,'xgs360028fMirroringPrivilegeLevel':xgs360028fMirroringPrivilegeLevel,'xgs360028fPTPPrivilegeLevel':xgs360028fPTPPrivilegeLevel,'xgs360028fPortsPrivilegeLevel':xgs360028fPortsPrivilegeLevel,'xgs360028fPrivateVLANsPrivilegeLevel':xgs360028fPrivateVLANsPrivilegeLevel,'xgs360028fQoSPrivilegeLevel':xgs360028fQoSPrivilegeLevel,'xgs360028fSMTPPrivilegeLevel':xgs360028fSMTPPrivilegeLevel,'xgs360028fSNMPPrivilegeLevel':xgs360028fSNMPPrivilegeLevel,'xgs360028fSecurityPrivilegeLevel':xgs360028fSecurityPrivilegeLevel,'xgs360028fSpanningTreePrivilegeLevel':xgs360028fSpanningTreePrivilegeLevel,'xgs360028fSystemPrivilegeLevel':xgs360028fSystemPrivilegeLevel,'xgs360028fTrapEventPrivilegeLevel':xgs360028fTrapEventPrivilegeLevel,'xgs360028fVCLPrivilegeLevel':xgs360028fVCLPrivilegeLevel,'xgs360028fVLANTranslationPrivilegeLevel':xgs360028fVLANTranslationPrivilegeLevel,'xgs360028fVLANsPrivilegeLevel':xgs360028fVLANsPrivilegeLevel,'xgs360028fIP':xgs360028fIP,'xgs360028fIPv4':xgs360028fIPv4,'xgs360028fIPv4Configured':xgs360028fIPv4Configured,'xgs360028fIpv4DHCPClient':xgs360028fIpv4DHCPClient,'xgs360028fIPv4Address':xgs360028fIPv4Address,'xgs360028fIPv4Mask':xgs360028fIPv4Mask,'xgs360028fIPv4Router':xgs360028fIPv4Router,'xgs360028fIPv4VLANId':xgs360028fIPv4VLANId,'xgs360028fIPv4DNSServer':xgs360028fIPv4DNSServer,'xgs360028fIPv4DNSProxy':xgs360028fIPv4DNSProxy,'xgs360028fIPv4Current':xgs360028fIPv4Current,'xgs360028fIpv4CurrentDHCPClient':xgs360028fIpv4CurrentDHCPClient,'xgs360028fIPv4CurrentAddress':xgs360028fIPv4CurrentAddress,'xgs360028fIPv4CurrentMask':xgs360028fIPv4CurrentMask,'xgs360028fIPv4CurrentRouter':xgs360028fIPv4CurrentRouter,'xgs360028fIPv4CurrentVLANId':xgs360028fIPv4CurrentVLANId,'xgs360028fIPv4CurrentDNSServer':xgs360028fIPv4CurrentDNSServer,'xgs360028fIPv6':xgs360028fIPv6,'xgs360028fIPv6Configured':xgs360028fIPv6Configured,'xgs360028fIpv6AutoConfiguration':xgs360028fIpv6AutoConfiguration,'xgs360028fIpv6Address':xgs360028fIpv6Address,'xgs360028fIpv6Prefix':xgs360028fIpv6Prefix,'xgs360028fIpv6Router':xgs360028fIpv6Router,'xgs360028fIPv6Current':xgs360028fIPv6Current,'xgs360028fIpv6CurrentAutoConfiguration':xgs360028fIpv6CurrentAutoConfiguration,'xgs360028fIpv6CurrentAddress':xgs360028fIpv6CurrentAddress,'xgs360028fIpv6CurrentLinkLocalAddress':xgs360028fIpv6CurrentLinkLocalAddress,'xgs360028fIpv6CurrentPrefix':xgs360028fIpv6CurrentPrefix,'xgs360028fIpv6CurrentRouter':xgs360028fIpv6CurrentRouter,'xgs360028fSyslog':xgs360028fSyslog,'xgs360028fSyslogConf':xgs360028fSyslogConf,'xgs360028fServerMode':xgs360028fServerMode,'xgs360028fServerAddress1':xgs360028fServerAddress1,'xgs360028fServerAddress2':xgs360028fServerAddress2,'xgs360028fSyslogLevel':xgs360028fSyslogLevel,'xgs360028fSyslogDetailedInfo':xgs360028fSyslogDetailedInfo,'xgs360028fSyslogDetailedInfoClear':xgs360028fSyslogDetailedInfoClear,'xgs360028fSyslogDetailedInfoTable':xgs360028fSyslogDetailedInfoTable,'xgs360028fSyslogDetailedInfoEntry':xgs360028fSyslogDetailedInfoEntry,_L:xgs360028fSyslogDetailedInfoIndex,'xgs360028fSyslogDetailedInfoLevel':xgs360028fSyslogDetailedInfoLevel,'xgs360028fSyslogDetailedInfoTime':xgs360028fSyslogDetailedInfoTime,'xgs360028fSyslogDetailedInfoMessage':xgs360028fSyslogDetailedInfoMessage,'xgs360028fSnmp':xgs360028fSnmp,'xgs360028fSnmpConf':xgs360028fSnmpConf,'xgs360028fGetCommunity':xgs360028fGetCommunity,'xgs360028fSetCommunityMode':xgs360028fSetCommunityMode,'xgs360028fSetCommunity':xgs360028fSetCommunity,'xgs360028fTrapHostConfTable':xgs360028fTrapHostConfTable,'xgs360028fTrapHostConfEntry':xgs360028fTrapHostConfEntry,_M:xgs360028fTrapHostConfIndex,'xgs360028fTrapHostConfVersion':xgs360028fTrapHostConfVersion,'xgs360028fTrapHostConfIPType':xgs360028fTrapHostConfIPType,'xgs360028fTrapHostConfIP':xgs360028fTrapHostConfIP,'xgs360028fTrapHostConfPort':xgs360028fTrapHostConfPort,'xgs360028fTrapHostConfCommunity':xgs360028fTrapHostConfCommunity,'xgs360028fTrapHostConfSeverityLevel':xgs360028fTrapHostConfSeverityLevel,'xgs360028fTrapHostConfSecurityLevel':xgs360028fTrapHostConfSecurityLevel,'xgs360028fTrapHostConfAuthPtc':xgs360028fTrapHostConfAuthPtc,'xgs360028fTrapHostConfAuthPassword':xgs360028fTrapHostConfAuthPassword,'xgs360028fTrapHostConfPrivPtc':xgs360028fTrapHostConfPrivPtc,'xgs360028fTrapHostConfPrivPassword':xgs360028fTrapHostConfPrivPassword,'xgs360028fTrapHostConfCurrentMode':xgs360028fTrapHostConfCurrentMode,'xgs360028fConfiguration':xgs360028fConfiguration,'xgs360028fPort':xgs360028fPort,'xgs360028fPortConfigurationTable':xgs360028fPortConfigurationTable,'xgs360028fPortConfigurationEntry':xgs360028fPortConfigurationEntry,_N:xgs360028fPortConfPort,'xgs360028fPortConfPortMedia':xgs360028fPortConfPortMedia,'xgs360028fPortConfLink':xgs360028fPortConfLink,'xgs360028fPortConfCurrentSpeed':xgs360028fPortConfCurrentSpeed,'xgs360028fPortConfSpeed':xgs360028fPortConfSpeed,'xgs360028fPortConfCurrentFlowControlRx':xgs360028fPortConfCurrentFlowControlRx,'xgs360028fPortConfCurrentFlowControlTx':xgs360028fPortConfCurrentFlowControlTx,'xgs360028fPortConfFlowControl':xgs360028fPortConfFlowControl,'xgs360028fPortConfMaxFrameSize':xgs360028fPortConfMaxFrameSize,'xgs360028fPortConfExcessiveCollisionMode':xgs360028fPortConfExcessiveCollisionMode,'xgs360028fPortConfPowerControl':xgs360028fPortConfPowerControl,'xgs360028fPortConfDescription':xgs360028fPortConfDescription,'xgs360028fPortTrafficStatisticsTable':xgs360028fPortTrafficStatisticsTable,'xgs360028fPortTrafficStatisticsEntry':xgs360028fPortTrafficStatisticsEntry,_O:xgs360028fPortTrafficStatisticsPort,'xgs360028fPortTrafficStatisticsClear':xgs360028fPortTrafficStatisticsClear,'xgs360028fPortTrafficRxPackets':xgs360028fPortTrafficRxPackets,'xgs360028fPortTrafficRxOctets':xgs360028fPortTrafficRxOctets,'xgs360028fPortTrafficRxUnicast':xgs360028fPortTrafficRxUnicast,'xgs360028fPortTrafficRxMulticast':xgs360028fPortTrafficRxMulticast,'xgs360028fPortTrafficRxBroadcast':xgs360028fPortTrafficRxBroadcast,'xgs360028fPortTrafficRxPause':xgs360028fPortTrafficRxPause,'xgs360028fPortTrafficRx64Bytes':xgs360028fPortTrafficRx64Bytes,'xgs360028fPortTrafficRx65to127Bytes':xgs360028fPortTrafficRx65to127Bytes,'xgs360028fPortTrafficRx128to255Bytes':xgs360028fPortTrafficRx128to255Bytes,'xgs360028fPortTrafficRx256to511Bytes':xgs360028fPortTrafficRx256to511Bytes,'xgs360028fPortTrafficRx512to1023Bytes':xgs360028fPortTrafficRx512to1023Bytes,'xgs360028fPortTrafficRx1024to1526Bytes':xgs360028fPortTrafficRx1024to1526Bytes,'xgs360028fPortTrafficRxExceecd1527Bytes':xgs360028fPortTrafficRxExceecd1527Bytes,'xgs360028fPortTrafficRxQ0':xgs360028fPortTrafficRxQ0,'xgs360028fPortTrafficRxQ1':xgs360028fPortTrafficRxQ1,'xgs360028fPortTrafficRxQ2':xgs360028fPortTrafficRxQ2,'xgs360028fPortTrafficRxQ3':xgs360028fPortTrafficRxQ3,'xgs360028fPortTrafficRxQ4':xgs360028fPortTrafficRxQ4,'xgs360028fPortTrafficRxQ5':xgs360028fPortTrafficRxQ5,'xgs360028fPortTrafficRxQ6':xgs360028fPortTrafficRxQ6,'xgs360028fPortTrafficRxQ7':xgs360028fPortTrafficRxQ7,'xgs360028fPortTrafficRxDrops':xgs360028fPortTrafficRxDrops,'xgs360028fPortTrafficRxCRCorAlignment':xgs360028fPortTrafficRxCRCorAlignment,'xgs360028fPortTrafficRxUndersize':xgs360028fPortTrafficRxUndersize,'xgs360028fPortTrafficRxOversize':xgs360028fPortTrafficRxOversize,'xgs360028fPortTrafficRxFragments':xgs360028fPortTrafficRxFragments,'xgs360028fPortTrafficRxJabber':xgs360028fPortTrafficRxJabber,'xgs360028fPortTrafficRxFiltered':xgs360028fPortTrafficRxFiltered,'xgs360028fPortTrafficTxPackets':xgs360028fPortTrafficTxPackets,'xgs360028fPortTrafficTxOctets':xgs360028fPortTrafficTxOctets,'xgs360028fPortTrafficTxUnicast':xgs360028fPortTrafficTxUnicast,'xgs360028fPortTrafficTxMulticast':xgs360028fPortTrafficTxMulticast,'xgs360028fPortTrafficTxBroadcast':xgs360028fPortTrafficTxBroadcast,'xgs360028fPortTrafficTxPause':xgs360028fPortTrafficTxPause,'xgs360028fPortTrafficTx64Bytes':xgs360028fPortTrafficTx64Bytes,'xgs360028fPortTrafficTx65to127Bytes':xgs360028fPortTrafficTx65to127Bytes,'xgs360028fPortTrafficTx128to255Bytes':xgs360028fPortTrafficTx128to255Bytes,'xgs360028fPortTrafficTx256to511Bytes':xgs360028fPortTrafficTx256to511Bytes,'xgs360028fPortTrafficTx512to1023Bytes':xgs360028fPortTrafficTx512to1023Bytes,'xgs360028fPortTrafficTx1024to1526Bytes':xgs360028fPortTrafficTx1024to1526Bytes,'xgs360028fPortTrafficTxExceecd1527Bytes':xgs360028fPortTrafficTxExceecd1527Bytes,'xgs360028fPortTrafficTxQ0':xgs360028fPortTrafficTxQ0,'xgs360028fPortTrafficTxQ1':xgs360028fPortTrafficTxQ1,'xgs360028fPortTrafficTxQ2':xgs360028fPortTrafficTxQ2,'xgs360028fPortTrafficTxQ3':xgs360028fPortTrafficTxQ3,'xgs360028fPortTrafficTxQ4':xgs360028fPortTrafficTxQ4,'xgs360028fPortTrafficTxQ5':xgs360028fPortTrafficTxQ5,'xgs360028fPortTrafficTxQ6':xgs360028fPortTrafficTxQ6,'xgs360028fPortTrafficTxQ7':xgs360028fPortTrafficTxQ7,'xgs360028fPortTrafficTxDrops':xgs360028fPortTrafficTxDrops,'xgs360028fPortTrafficTxLateOrExcColl':xgs360028fPortTrafficTxLateOrExcColl,'xgs360028fPortQoSStatistics':xgs360028fPortQoSStatistics,'xgs360028fPortQoSStatisticsClear':xgs360028fPortQoSStatisticsClear,'xgs360028fPortQoSStatisticsTable':xgs360028fPortQoSStatisticsTable,'xgs360028fPortQoSStatisticsEntry':xgs360028fPortQoSStatisticsEntry,_P:xgs360028fPortQoSStatisticsPort,'xgs360028fPortQoSQ0Rx':xgs360028fPortQoSQ0Rx,'xgs360028fPortQoSQ0Tx':xgs360028fPortQoSQ0Tx,'xgs360028fPortQoSQ1Rx':xgs360028fPortQoSQ1Rx,'xgs360028fPortQoSQ1Tx':xgs360028fPortQoSQ1Tx,'xgs360028fPortQoSQ2Rx':xgs360028fPortQoSQ2Rx,'xgs360028fPortQoSQ2Tx':xgs360028fPortQoSQ2Tx,'xgs360028fPortQoSQ3Rx':xgs360028fPortQoSQ3Rx,'xgs360028fPortQoSQ3Tx':xgs360028fPortQoSQ3Tx,'xgs360028fPortQoSQ4Rx':xgs360028fPortQoSQ4Rx,'xgs360028fPortQoSQ4Tx':xgs360028fPortQoSQ4Tx,'xgs360028fPortQoSQ5Rx':xgs360028fPortQoSQ5Rx,'xgs360028fPortQoSQ5Tx':xgs360028fPortQoSQ5Tx,'xgs360028fPortQoSQ6Rx':xgs360028fPortQoSQ6Rx,'xgs360028fPortQoSQ6Tx':xgs360028fPortQoSQ6Tx,'xgs360028fPortQoSQ7Rx':xgs360028fPortQoSQ7Rx,'xgs360028fPortQoSQ7Tx':xgs360028fPortQoSQ7Tx,'xgs360028fSFPInfoTable':xgs360028fSFPInfoTable,'xgs360028fSFPInfoEntry':xgs360028fSFPInfoEntry,_Q:xgs360028fSFPInfoIndex,'xgs360028fSFPInfoPort':xgs360028fSFPInfoPort,'xgs360028fSFPConnectorType':xgs360028fSFPConnectorType,'xgs360028fSFPFiberType':xgs360028fSFPFiberType,'xgs360028fSFPTxCentralWavelength':xgs360028fSFPTxCentralWavelength,'xgs360028fSFPBaudRate':xgs360028fSFPBaudRate,'xgs360028fSFPVendorOUI':xgs360028fSFPVendorOUI,'xgs360028fSFPVendorName':xgs360028fSFPVendorName,'xgs360028fSFPVendorPN':xgs360028fSFPVendorPN,'xgs360028fSFPVendorRev':xgs360028fSFPVendorRev,'xgs360028fSFPVendorSN':xgs360028fSFPVendorSN,'xgs360028fSFPDateCode':xgs360028fSFPDateCode,'xgs360028fSFPTemperature':xgs360028fSFPTemperature,'xgs360028fSFPVcc':xgs360028fSFPVcc,'xgs360028fSFPMon1Bias':xgs360028fSFPMon1Bias,'xgs360028fSFPMon2TxPWR':xgs360028fSFPMon2TxPWR,'xgs360028fSFPMon3RxPWR':xgs360028fSFPMon3RxPWR,'xgs360028fGARP':xgs360028fGARP,'xgs360028fGARPConfTable':xgs360028fGARPConfTable,'xgs360028fGARPConfEntry':xgs360028fGARPConfEntry,_R:xgs360028fGARPConfPort,'xgs360028fGARPJoinTimer':xgs360028fGARPJoinTimer,'xgs360028fGARPLeaveTimer':xgs360028fGARPLeaveTimer,'xgs360028fGARPLeaveAllTimer':xgs360028fGARPLeaveAllTimer,'xgs360028fGARPApplicantion':xgs360028fGARPApplicantion,'xgs360028fGARPAttributeType':xgs360028fGARPAttributeType,'xgs360028fGARPApplicant':xgs360028fGARPApplicant,'xgs360028fGARPStatisticsTable':xgs360028fGARPStatisticsTable,'xgs360028fGARPStatisticsEntry':xgs360028fGARPStatisticsEntry,_S:xgs360028fGARPStatisticsPort,'xgs360028fGARPStatisticsPeerMAC':xgs360028fGARPStatisticsPeerMAC,'xgs360028fGARPStatisticsFailedCount':xgs360028fGARPStatisticsFailedCount,'xgs360028fGVRP':xgs360028fGVRP,'xgs360028fGVRPConf':xgs360028fGVRPConf,'xgs360028fGVRPMode':xgs360028fGVRPMode,'xgs360028fGVRPConfTable':xgs360028fGVRPConfTable,'xgs360028fGVRPConfEntry':xgs360028fGVRPConfEntry,_T:xgs360028fGVRPConfPort,'xgs360028fGVRPConfPortMode':xgs360028fGVRPConfPortMode,'xgs360028fGVRPConfPortRRole':xgs360028fGVRPConfPortRRole,'xgs360028fGVRPStatisticsTable':xgs360028fGVRPStatisticsTable,'xgs360028fGVRPStatisticsEntry':xgs360028fGVRPStatisticsEntry,_U:xgs360028fGVRPStatisticsPort,'xgs360028fGVRPStatisticsJoinTxCnt':xgs360028fGVRPStatisticsJoinTxCnt,'xgs360028fGVRPStatisticsLeaveTxCnt':xgs360028fGVRPStatisticsLeaveTxCnt,'xgs360028fThermalProtection':xgs360028fThermalProtection,'xgs360028fPriority0Temperature':xgs360028fPriority0Temperature,'xgs360028fPriority1Temperature':xgs360028fPriority1Temperature,'xgs360028fPriority2Temperature':xgs360028fPriority2Temperature,'xgs360028fPriority3Temperature':xgs360028fPriority3Temperature,'xgs360028fThermalProtectionTable':xgs360028fThermalProtectionTable,'xgs360028fThermalProtectionEntry':xgs360028fThermalProtectionEntry,_V:xgs360028fThermalProtectionPort,'xgs360028fThermalProtectionPortTemperature':xgs360028fThermalProtectionPortTemperature,'xgs360028fThermalProtectionPortPriority':xgs360028fThermalProtectionPortPriority,'xgs360028fThermalProtectionPortStatus':xgs360028fThermalProtectionPortStatus,'xgs360028fMirroring':xgs360028fMirroring,'xgs360028fPortToMirrorOn':xgs360028fPortToMirrorOn,'xgs360028fMirrorTable':xgs360028fMirrorTable,'xgs360028fMirrorEntry':xgs360028fMirrorEntry,_W:xgs360028fMirrorPort,'xgs360028fMirrorMode':xgs360028fMirrorMode,'xgs360028fTrapEventSeverity':xgs360028fTrapEventSeverity,'xgs360028fTrapEventSeverityACL':xgs360028fTrapEventSeverityACL,'xgs360028fTrapEventSeverityACLLog':xgs360028fTrapEventSeverityACLLog,'xgs360028fTrapEventSeverityAccessMgmt':xgs360028fTrapEventSeverityAccessMgmt,'xgs360028fTrapEventSeverityAuthFailed':xgs360028fTrapEventSeverityAuthFailed,'xgs360028fTrapEventSeverityColdStart':xgs360028fTrapEventSeverityColdStart,'xgs360028fTrapEventSeverityConfigInfo':xgs360028fTrapEventSeverityConfigInfo,'xgs360028fTrapEventSeverityFirmwareUpgrade':xgs360028fTrapEventSeverityFirmwareUpgrade,'xgs360028fTrapEventSeverityImportExport':xgs360028fTrapEventSeverityImportExport,'xgs360028fTrapEventSeverityLACP':xgs360028fTrapEventSeverityLACP,'xgs360028fTrapEventSeverityLinkStatus':xgs360028fTrapEventSeverityLinkStatus,'xgs360028fTrapEventSeverityLogin':xgs360028fTrapEventSeverityLogin,'xgs360028fTrapEventSeverityLogout':xgs360028fTrapEventSeverityLogout,'xgs360028fTrapEventSeverityLoopProtect':xgs360028fTrapEventSeverityLoopProtect,'xgs360028fTrapEventSeverityMgmtIPChange':xgs360028fTrapEventSeverityMgmtIPChange,'xgs360028fTrapEventSeverityModuleChange':xgs360028fTrapEventSeverityModuleChange,'xgs360028fTrapEventSeverityNAS':xgs360028fTrapEventSeverityNAS,'xgs360028fTrapEventSeverityPasswdChange':xgs360028fTrapEventSeverityPasswdChange,'xgs360028fTrapEventSeverityPortSecurity':xgs360028fTrapEventSeverityPortSecurity,'xgs360028fTrapEventSeverityThermalProtect':xgs360028fTrapEventSeverityThermalProtect,'xgs360028fTrapEventSeverityVLAN':xgs360028fTrapEventSeverityVLAN,'xgs360028fTrapEventSeverityWarmStart':xgs360028fTrapEventSeverityWarmStart,'xgs360028fSMTP':xgs360028fSMTP,'xgs360028fSMTPMailServer':xgs360028fSMTPMailServer,'xgs360028fSMTPUserName':xgs360028fSMTPUserName,'xgs360028fSMTPPassword':xgs360028fSMTPPassword,'xgs360028fSMTPServeriryLevel':xgs360028fSMTPServeriryLevel,'xgs360028fSMTPSender':xgs360028fSMTPSender,'xgs360028fSMTPReturnPath':xgs360028fSMTPReturnPath,'xgs360028fSMTPEmailAddress1':xgs360028fSMTPEmailAddress1,'xgs360028fSMTPEmailAddress2':xgs360028fSMTPEmailAddress2,'xgs360028fSMTPEmailAddress3':xgs360028fSMTPEmailAddress3,'xgs360028fSMTPEmailAddress4':xgs360028fSMTPEmailAddress4,'xgs360028fSMTPEmailAddress5':xgs360028fSMTPEmailAddress5,'xgs360028fSMTPEmailAddress6':xgs360028fSMTPEmailAddress6,'xgs360028fACL':xgs360028fACL,'xgs360028fACLPortsConfTable':xgs360028fACLPortsConfTable,'xgs360028fACLPortsConfEntry':xgs360028fACLPortsConfEntry,_X:xgs360028fACLPortsConfPort,'xgs360028fACLPortsConfPolicyID':xgs360028fACLPortsConfPolicyID,'xgs360028fACLPortsConfAction':xgs360028fACLPortsConfAction,'xgs360028fACLPortsConfRateLimiterID':xgs360028fACLPortsConfRateLimiterID,'xgs360028fACLPortsConfPortRedirect':xgs360028fACLPortsConfPortRedirect,'xgs360028fACLPortsConfLogging':xgs360028fACLPortsConfLogging,'xgs360028fACLPortsConfShutdown':xgs360028fACLPortsConfShutdown,'xgs360028fACLPortsConfState':xgs360028fACLPortsConfState,'xgs360028fACLPortsConfCounter':xgs360028fACLPortsConfCounter,'xgs360028fACLRateLimiterTable':xgs360028fACLRateLimiterTable,'xgs360028fACLRateLimiterEntry':xgs360028fACLRateLimiterEntry,_Y:xgs360028fACLRateLimiterID,'xgs360028fACLRateLimiterRate':xgs360028fACLRateLimiterRate,'xgs360028fACLACE':xgs360028fACLACE,'xgs360028fACLACECreate':xgs360028fACLACECreate,'xgs360028fACLACETable':xgs360028fACLACETable,'xgs360028fACLACEEntry':xgs360028fACLACEEntry,_Z:xgs360028fACLACEIndex,'xgs360028fACLACEID':xgs360028fACLACEID,'xgs360028fACLACENextID':xgs360028fACLACENextID,'xgs360028fACLACEIngressPort':xgs360028fACLACEIngressPort,'xgs360028fACLACEPortPolicyNumber':xgs360028fACLACEPortPolicyNumber,'xgs360028fACLACEPortPolicyBitmask':xgs360028fACLACEPortPolicyBitmask,'xgs360028fACLACEFrameType':xgs360028fACLACEFrameType,'xgs360028fACLACEAction':xgs360028fACLACEAction,'xgs360028fACLACEDenyPortRedirect':xgs360028fACLACEDenyPortRedirect,'xgs360028fACLACELogging':xgs360028fACLACELogging,'xgs360028fACLACERateLimiter':xgs360028fACLACERateLimiter,'xgs360028fACLACEShutdown':xgs360028fACLACEShutdown,'xgs360028fACLACEVLANTagPriority':xgs360028fACLACEVLANTagPriority,'xgs360028fACLACEVLANVID':xgs360028fACLACEVLANVID,'xgs360028fACLACEEtherType':xgs360028fACLACEEtherType,'xgs360028fACLACESMAC':xgs360028fACLACESMAC,'xgs360028fACLACEDMACType':xgs360028fACLACEDMACType,'xgs360028fACLACEDMAC':xgs360028fACLACEDMAC,'xgs360028fACLACEArpOpcode':xgs360028fACLACEArpOpcode,'xgs360028fACLACEArpFlagsRequestReply':xgs360028fACLACEArpFlagsRequestReply,'xgs360028fACLACEArpFlagsArpSmac':xgs360028fACLACEArpFlagsArpSmac,'xgs360028fACLACEArpFlagsRarpDmac':xgs360028fACLACEArpFlagsRarpDmac,'xgs360028fACLACEArpFlagsLength':xgs360028fACLACEArpFlagsLength,'xgs360028fACLACEArpFlagsIp':xgs360028fACLACEArpFlagsIp,'xgs360028fACLACEArpFlagsEthernet':xgs360028fACLACEArpFlagsEthernet,'xgs360028fACLACESIPType':xgs360028fACLACESIPType,'xgs360028fACLACESIPIPAddress':xgs360028fACLACESIPIPAddress,'xgs360028fACLACESIPNetworkPrefix':xgs360028fACLACESIPNetworkPrefix,'xgs360028fACLACEDIPType':xgs360028fACLACEDIPType,'xgs360028fACLACEDIPIPAddress':xgs360028fACLACEDIPIPAddress,'xgs360028fACLACEDIPNetworkPrefix':xgs360028fACLACEDIPNetworkPrefix,'xgs360028fACLACEIPProtocol':xgs360028fACLACEIPProtocol,'xgs360028fACLACEIPFlagsTTL':xgs360028fACLACEIPFlagsTTL,'xgs360028fACLACEIPFlagsOptions':xgs360028fACLACEIPFlagsOptions,'xgs360028fACLACEIPFlagsFragment':xgs360028fACLACEIPFlagsFragment,'xgs360028fACLACEICMPType':xgs360028fACLACEICMPType,'xgs360028fACLACEICMPCode':xgs360028fACLACEICMPCode,'xgs360028fACLACESourcePortMin':xgs360028fACLACESourcePortMin,'xgs360028fACLACESourcePortMax':xgs360028fACLACESourcePortMax,'xgs360028fACLACEDestPortMin':xgs360028fACLACEDestPortMin,'xgs360028fACLACEDestPortMax':xgs360028fACLACEDestPortMax,'xgs360028fACLACETCPFlagsFin':xgs360028fACLACETCPFlagsFin,'xgs360028fACLACETCPFlagsSyn':xgs360028fACLACETCPFlagsSyn,'xgs360028fACLACETCPFlagsRst':xgs360028fACLACETCPFlagsRst,'xgs360028fACLACETCPFlagsPsh':xgs360028fACLACETCPFlagsPsh,'xgs360028fACLACETCPFlagsAck':xgs360028fACLACETCPFlagsAck,'xgs360028fACLACETCPFlagsUrg':xgs360028fACLACETCPFlagsUrg,'xgs360028fACLACERowStatus':xgs360028fACLACERowStatus,'xgs360028fACLACEClear':xgs360028fACLACEClear,'xgs360028fACLACEMoveACEID':xgs360028fACLACEMoveACEID,'xgs360028fACLACEMoveNextACEID':xgs360028fACLACEMoveNextACEID,'xgs360028fACLACEStatusTable':xgs360028fACLACEStatusTable,'xgs360028fACLACEStatusEntry':xgs360028fACLACEStatusEntry,_a:xgs360028fACLACEStatusIndex,'xgs360028fACLACEStatusUser':xgs360028fACLACEStatusUser,'xgs360028fACLACEStatusID':xgs360028fACLACEStatusID,'xgs360028fACLACEStatusIngressPort':xgs360028fACLACEStatusIngressPort,'xgs360028fACLACEStatusFrameType':xgs360028fACLACEStatusFrameType,'xgs360028fACLACEStatusAction':xgs360028fACLACEStatusAction,'xgs360028fACLACEStatusRateLimiter':xgs360028fACLACEStatusRateLimiter,'xgs360028fACLACEStatusPortCopy':xgs360028fACLACEStatusPortCopy,'xgs360028fACLACEStatusMirror':xgs360028fACLACEStatusMirror,'xgs360028fACLACEStatusCPU':xgs360028fACLACEStatusCPU,'xgs360028fACLACEStatusCounter':xgs360028fACLACEStatusCounter,'xgs360028fACLACEStatusConflict':xgs360028fACLACEStatusConflict,'xgs360028fERPS':xgs360028fERPS,'xgs360028fERPSConf':xgs360028fERPSConf,'xgs360028fERPSConfCreate':xgs360028fERPSConfCreate,'xgs360028fERPSConfTable':xgs360028fERPSConfTable,'xgs360028fERPSConfEntry':xgs360028fERPSConfEntry,_b:xgs360028fERPSConfIndex,'xgs360028fERPSConfERPSID':xgs360028fERPSConfERPSID,'xgs360028fERPSConfPort0':xgs360028fERPSConfPort0,'xgs360028fERPSConfPort1':xgs360028fERPSConfPort1,'xgs360028fERPSConfPort0SFMEP':xgs360028fERPSConfPort0SFMEP,'xgs360028fERPSConfPort1SFMEP':xgs360028fERPSConfPort1SFMEP,'xgs360028fERPSConfPort0APSMEP':xgs360028fERPSConfPort0APSMEP,'xgs360028fERPSConfPort1APSMEP':xgs360028fERPSConfPort1APSMEP,'xgs360028fERPSConfRingType':xgs360028fERPSConfRingType,'xgs360028fERPSConfInterconnectedNode':xgs360028fERPSConfInterconnectedNode,'xgs360028fERPSConfVirtualChannel':xgs360028fERPSConfVirtualChannel,'xgs360028fERPSConfMajorRingID':xgs360028fERPSConfMajorRingID,'xgs360028fERPSConfAlarm':xgs360028fERPSConfAlarm,'xgs360028fERPSInstanceConfConfigured':xgs360028fERPSInstanceConfConfigured,'xgs360028fERPSInstanceConfGuardTime':xgs360028fERPSInstanceConfGuardTime,'xgs360028fERPSInstanceConfWTRTime':xgs360028fERPSInstanceConfWTRTime,'xgs360028fERPSInstanceConfHoldOffTime':xgs360028fERPSInstanceConfHoldOffTime,'xgs360028fERPSInstanceConfVersion':xgs360028fERPSInstanceConfVersion,'xgs360028fERPSInstanceConfRevertive':xgs360028fERPSInstanceConfRevertive,'xgs360028fERPSInstanceConfVLANconfig':xgs360028fERPSInstanceConfVLANconfig,'xgs360028fERPSConfRowStatus':xgs360028fERPSConfRowStatus,'xgs360028fMRSTP':xgs360028fMRSTP,'xgs360028fMRSTPInstance':xgs360028fMRSTPInstance,'xgs360028fMRSTPInstanceConf':xgs360028fMRSTPInstanceConf,'xgs360028fMRSTPInstanceConfGlobalState':xgs360028fMRSTPInstanceConfGlobalState,'xgs360028fMRSTPInstanceConfigurationTable':xgs360028fMRSTPInstanceConfigurationTable,'xgs360028fMRSTPInstanceConfigurationEntry':xgs360028fMRSTPInstanceConfigurationEntry,_c:xgs360028fMRSTPInstanceConfigurationInstance,'xgs360028fMRSTPInstanceConfigurationState':xgs360028fMRSTPInstanceConfigurationState,'xgs360028fMRSTPInstanceConfigurationVersion':xgs360028fMRSTPInstanceConfigurationVersion,'xgs360028fMRSTPInstanceConfigurationPriority':xgs360028fMRSTPInstanceConfigurationPriority,'xgs360028fMRSTPInstanceConfigurationHelloTime':xgs360028fMRSTPInstanceConfigurationHelloTime,'xgs360028fMRSTPInstanceConfigurationMaxAge':xgs360028fMRSTPInstanceConfigurationMaxAge,'xgs360028fMRSTPInstanceConfigurationFWDelay':xgs360028fMRSTPInstanceConfigurationFWDelay,'xgs360028fMRSTPInstanceStatus':xgs360028fMRSTPInstanceStatus,'xgs360028fMRSTPInstanceStatusTable':xgs360028fMRSTPInstanceStatusTable,'xgs360028fMRSTPInstanceStatusEntry':xgs360028fMRSTPInstanceStatusEntry,_d:xgs360028fMRSTPInstanceStatusInstance,'xgs360028fMRSTPInstanceStatusGlobalState':xgs360028fMRSTPInstanceStatusGlobalState,'xgs360028fMRSTPInstanceStatusInstanceConfigState':xgs360028fMRSTPInstanceStatusInstanceConfigState,'xgs360028fMRSTPInstanceStatusInstanceCurrentState':xgs360028fMRSTPInstanceStatusInstanceCurrentState,'xgs360028fMRSTPInstanceStatusBridgeID':xgs360028fMRSTPInstanceStatusBridgeID,'xgs360028fMRSTPInstanceStatusBridgePrioriry':xgs360028fMRSTPInstanceStatusBridgePrioriry,'xgs360028fMRSTPInstanceStatusRootID':xgs360028fMRSTPInstanceStatusRootID,'xgs360028fMRSTPInstanceStatusRootPriority':xgs360028fMRSTPInstanceStatusRootPriority,'xgs360028fMRSTPInstanceStatusRootPort':xgs360028fMRSTPInstanceStatusRootPort,'xgs360028fMRSTPInstanceStatusRootPathCost':xgs360028fMRSTPInstanceStatusRootPathCost,'xgs360028fMRSTPInstanceStatusCurrentMaxAge':xgs360028fMRSTPInstanceStatusCurrentMaxAge,'xgs360028fMRSTPInstanceStatusCurrentForwardDelay':xgs360028fMRSTPInstanceStatusCurrentForwardDelay,'xgs360028fMRSTPInstanceStatusHelloTime':xgs360028fMRSTPInstanceStatusHelloTime,'xgs360028fMRSTPInstanceStatusTopologyChangeCount':xgs360028fMRSTPInstanceStatusTopologyChangeCount,'xgs360028fMRSTPInstanceStatusTimeSinceLastTopologyChange':xgs360028fMRSTPInstanceStatusTimeSinceLastTopologyChange,'xgs360028fMRSTPPort':xgs360028fMRSTPPort,'xgs360028fMRSTPPortConfiguration':xgs360028fMRSTPPortConfiguration,'xgs360028fMRSTPPortConfigurationTable':xgs360028fMRSTPPortConfigurationTable,'xgs360028fMRSTPPortConfigurationEntry':xgs360028fMRSTPPortConfigurationEntry,_e:xgs360028fMRSTPPortConfigurationPort,'xgs360028fMRSTPPortConfigurationInstance':xgs360028fMRSTPPortConfigurationInstance,'xgs360028fMRSTPPortConfigurationPathCost':xgs360028fMRSTPPortConfigurationPathCost,'xgs360028fMRSTPPortConfigurationPriority':xgs360028fMRSTPPortConfigurationPriority,'xgs360028fMRSTPPortConfigurationAdminEdge':xgs360028fMRSTPPortConfigurationAdminEdge,'xgs360028fMRSTPPortConfigurationAdminP2P':xgs360028fMRSTPPortConfigurationAdminP2P,'xgs360028fMRSTPPortConfigurationMigrateCheck':xgs360028fMRSTPPortConfigurationMigrateCheck,'xgs360028fMRSTPPortStatus':xgs360028fMRSTPPortStatus,'xgs360028fMRSTPPortStatusTable':xgs360028fMRSTPPortStatusTable,'xgs360028fMRSTPPortStatusEntry':xgs360028fMRSTPPortStatusEntry,_f:xgs360028fMRSTPPortStatusPort,'xgs360028fMRSTPPortStatusInstance':xgs360028fMRSTPPortStatusInstance,'xgs360028fMRSTPPortStatusState':xgs360028fMRSTPPortStatusState,'xgs360028fMRSTPPortStatusRole':xgs360028fMRSTPPortStatusRole,'xgs360028fMRSTPPortStatusPathCost':xgs360028fMRSTPPortStatusPathCost,'xgs360028fMRSTPPortStatusPathCostConfig':xgs360028fMRSTPPortStatusPathCostConfig,'xgs360028fMRSTPPortStatusPriority':xgs360028fMRSTPPortStatusPriority,'xgs360028fMRSTPPortStatusAdminEdge':xgs360028fMRSTPPortStatusAdminEdge,'xgs360028fMRSTPPortStatusAdminP2P':xgs360028fMRSTPPortStatusAdminP2P,'xgs360028fSecurity':xgs360028fSecurity,'xgs360028fIPSourceGuard':xgs360028fIPSourceGuard,'xgs360028fIPSourceGuardConf':xgs360028fIPSourceGuardConf,'xgs360028fIPSourceGuardMode':xgs360028fIPSourceGuardMode,'xgs360028fIPSourceGuardPortConfigTable':xgs360028fIPSourceGuardPortConfigTable,'xgs360028fIPSourceGuardPortConfigEntry':xgs360028fIPSourceGuardPortConfigEntry,_g:xgs360028fIPSourceGuardPortConfigPort,'xgs360028fIPSourceGuardPortConfigMode':xgs360028fIPSourceGuardPortConfigMode,'xgs360028fIPSourceGuardPortMaxDynamicClients':xgs360028fIPSourceGuardPortMaxDynamicClients,'xgs360028fIPSourceGuardStatic':xgs360028fIPSourceGuardStatic,'xgs360028fIPSourceGuardStaticCreate':xgs360028fIPSourceGuardStaticCreate,'xgs360028fIPSourceGuardStaticTable':xgs360028fIPSourceGuardStaticTable,'xgs360028fIPSourceGuardStaticEntry':xgs360028fIPSourceGuardStaticEntry,_h:xgs360028fIPSourceGuardStaticIndex,'xgs360028fIPSourceGuardStaticPort':xgs360028fIPSourceGuardStaticPort,'xgs360028fIPSourceGuardStaticVLANId':xgs360028fIPSourceGuardStaticVLANId,'xgs360028fIPSourceGuardStaticIPAddress':xgs360028fIPSourceGuardStaticIPAddress,'xgs360028fIPSourceGuardStaticMACAddress':xgs360028fIPSourceGuardStaticMACAddress,'xgs360028fIPSourceGuardStaticRowStatus':xgs360028fIPSourceGuardStaticRowStatus,'xgs360028fIPSourceGuardDynamicTable':xgs360028fIPSourceGuardDynamicTable,'xgs360028fIPSourceGuardDynamicEntry':xgs360028fIPSourceGuardDynamicEntry,_i:xgs360028fIPSourceGuardDynamicIndex,'xgs360028fIPSourceGuardDynamicPort':xgs360028fIPSourceGuardDynamicPort,'xgs360028fIPSourceGuardDynamicVLANId':xgs360028fIPSourceGuardDynamicVLANId,'xgs360028fIPSourceGuardDynamicIPAddress':xgs360028fIPSourceGuardDynamicIPAddress,'xgs360028fIPSourceGuardDynamicMACAddress':xgs360028fIPSourceGuardDynamicMACAddress,'xgs360028fARPInspection':xgs360028fARPInspection,'xgs360028fARPInspectionConf':xgs360028fARPInspectionConf,'xgs360028fARPInspectionConfMode':xgs360028fARPInspectionConfMode,'xgs360028fARPInspectionConfTable':xgs360028fARPInspectionConfTable,'xgs360028fARPInspectionConfEntry':xgs360028fARPInspectionConfEntry,_j:xgs360028fARPInspectionConfPortIndex,'xgs360028fARPInspectionConfPortMode':xgs360028fARPInspectionConfPortMode,'xgs360028fARPInspectionStatic':xgs360028fARPInspectionStatic,'xgs360028fARPInspectionStaticCreate':xgs360028fARPInspectionStaticCreate,'xgs360028fARPInspectionStaticTable':xgs360028fARPInspectionStaticTable,'xgs360028fARPInspectionStaticEntry':xgs360028fARPInspectionStaticEntry,_k:xgs360028fARPInspectionStaticIndex,'xgs360028fARPInspectionStaticPort':xgs360028fARPInspectionStaticPort,'xgs360028fARPInspectionStaticVLANId':xgs360028fARPInspectionStaticVLANId,'xgs360028fARPInspectionStaticIPAddress':xgs360028fARPInspectionStaticIPAddress,'xgs360028fARPInspectionStaticMACAddress':xgs360028fARPInspectionStaticMACAddress,'xgs360028fARPInspectionStaticRowStatus':xgs360028fARPInspectionStaticRowStatus,'xgs360028fARPInspectionDynamicTable':xgs360028fARPInspectionDynamicTable,'xgs360028fARPInspectionDynamicEntry':xgs360028fARPInspectionDynamicEntry,_l:xgs360028fARPInspectionDynamicIndex,'xgs360028fARPInspectionDynamicPort':xgs360028fARPInspectionDynamicPort,'xgs360028fARPInspectionDynamicVLANId':xgs360028fARPInspectionDynamicVLANId,'xgs360028fARPInspectionDynamicIPAddress':xgs360028fARPInspectionDynamicIPAddress,'xgs360028fARPInspectionDynamicMACAddress':xgs360028fARPInspectionDynamicMACAddress,'xgs360028fDHCPSnooping':xgs360028fDHCPSnooping,'xgs360028fDHCPSnoopingConf':xgs360028fDHCPSnoopingConf,'xgs360028fDHCPSnoopingMode':xgs360028fDHCPSnoopingMode,'xgs360028fDHCPSnoopingPortModeConfigurationTable':xgs360028fDHCPSnoopingPortModeConfigurationTable,'xgs360028fDHCPSnoopingPortModeConfigurationEntry':xgs360028fDHCPSnoopingPortModeConfigurationEntry,_m:xgs360028fDHCPSnoopingPortModeConfigurationPort,'xgs360028fDHCPSnoopingPortModeConfigurationMode':xgs360028fDHCPSnoopingPortModeConfigurationMode,'xgs360028fDHCPSnoopingStatisticsTable':xgs360028fDHCPSnoopingStatisticsTable,'xgs360028fDHCPSnoopingStatisticsEntry':xgs360028fDHCPSnoopingStatisticsEntry,_n:xgs360028fDHCPSnoopingStatisticsPort,'xgs360028fDHCPSnoopingStatisticsClear':xgs360028fDHCPSnoopingStatisticsClear,'xgs360028fDHCPSnoopingRxDiscover':xgs360028fDHCPSnoopingRxDiscover,'xgs360028fDHCPSnoopingRxOffer':xgs360028fDHCPSnoopingRxOffer,'xgs360028fDHCPSnoopingRxRequest':xgs360028fDHCPSnoopingRxRequest,'xgs360028fDHCPSnoopingRxDecline':xgs360028fDHCPSnoopingRxDecline,'xgs360028fDHCPSnoopingRxACK':xgs360028fDHCPSnoopingRxACK,'xgs360028fDHCPSnoopingRxNAK':xgs360028fDHCPSnoopingRxNAK,'xgs360028fDHCPSnoopingRxRelease':xgs360028fDHCPSnoopingRxRelease,'xgs360028fDHCPSnoopingRxInform':xgs360028fDHCPSnoopingRxInform,'xgs360028fDHCPSnoopingRxLeaseQuery':xgs360028fDHCPSnoopingRxLeaseQuery,'xgs360028fDHCPSnoopingRxLeaseUnassigned':xgs360028fDHCPSnoopingRxLeaseUnassigned,'xgs360028fDHCPSnoopingRxLeaseUnknown':xgs360028fDHCPSnoopingRxLeaseUnknown,'xgs360028fDHCPSnoopingRxLeaseActive':xgs360028fDHCPSnoopingRxLeaseActive,'xgs360028fDHCPSnoopingTxDiscover':xgs360028fDHCPSnoopingTxDiscover,'xgs360028fDHCPSnoopingTxOffer':xgs360028fDHCPSnoopingTxOffer,'xgs360028fDHCPSnoopingTxRequest':xgs360028fDHCPSnoopingTxRequest,'xgs360028fDHCPSnoopingTxDecline':xgs360028fDHCPSnoopingTxDecline,'xgs360028fDHCPSnoopingTxACK':xgs360028fDHCPSnoopingTxACK,'xgs360028fDHCPSnoopingTxNAK':xgs360028fDHCPSnoopingTxNAK,'xgs360028fDHCPSnoopingTxRelease':xgs360028fDHCPSnoopingTxRelease,'xgs360028fDHCPSnoopingTxInform':xgs360028fDHCPSnoopingTxInform,'xgs360028fDHCPSnoopingTxLeaseQuery':xgs360028fDHCPSnoopingTxLeaseQuery,'xgs360028fDHCPSnoopingTxLeaseUnassigned':xgs360028fDHCPSnoopingTxLeaseUnassigned,'xgs360028fDHCPSnoopingTxLeaseUnknown':xgs360028fDHCPSnoopingTxLeaseUnknown,'xgs360028fDHCPSnoopingTxLeaseActive':xgs360028fDHCPSnoopingTxLeaseActive,'xgs360028fDHCPRelay':xgs360028fDHCPRelay,'xgs360028fDHCPRelayConfiguration':xgs360028fDHCPRelayConfiguration,'xgs360028fDHCPRelayMode':xgs360028fDHCPRelayMode,'xgs360028fDHCPRelayServer':xgs360028fDHCPRelayServer,'xgs360028fDHCPRelayInformationMode':xgs360028fDHCPRelayInformationMode,'xgs360028fDHCPRelayInformationPolicy':xgs360028fDHCPRelayInformationPolicy,'xgs360028fDHCPRelayStatistics':xgs360028fDHCPRelayStatistics,'xgs360028fDHCPRelayServerStatistics':xgs360028fDHCPRelayServerStatistics,'xgs360028fServerStatTransmitToServer':xgs360028fServerStatTransmitToServer,'xgs360028fServerStatTransmitError':xgs360028fServerStatTransmitError,'xgs360028fServerStatReceiveFromServer':xgs360028fServerStatReceiveFromServer,'xgs360028fServerStatReceiveMissingAgentOption':xgs360028fServerStatReceiveMissingAgentOption,'xgs360028fServerStatReceiveMissingCircuitID':xgs360028fServerStatReceiveMissingCircuitID,'xgs360028fServerStatReceiveMissingRemoteID':xgs360028fServerStatReceiveMissingRemoteID,'xgs360028fServerStatReceiveBadCircuitID':xgs360028fServerStatReceiveBadCircuitID,'xgs360028fServerStatReceiveBadRemoteID':xgs360028fServerStatReceiveBadRemoteID,'xgs360028fDHCPRelayClientStatistics':xgs360028fDHCPRelayClientStatistics,'xgs360028fClientStatTransmitToClient':xgs360028fClientStatTransmitToClient,'xgs360028fClientStatTransmitError':xgs360028fClientStatTransmitError,'xgs360028fClientStatReceivefromClient':xgs360028fClientStatReceivefromClient,'xgs360028fClientStatReceiveAgentOption':xgs360028fClientStatReceiveAgentOption,'xgs360028fClientStatReplaceAgentOption':xgs360028fClientStatReplaceAgentOption,'xgs360028fClientStatKeepAgentOption':xgs360028fClientStatKeepAgentOption,'xgs360028fClientStatDropAgentOption':xgs360028fClientStatDropAgentOption,'xgs360028fPortSecurity':xgs360028fPortSecurity,'xgs360028fPortSecLimitCtrl':xgs360028fPortSecLimitCtrl,'xgs360028fPortSecLimitCtrlSystemConf':xgs360028fPortSecLimitCtrlSystemConf,'xgs360028fPortSecurityMode':xgs360028fPortSecurityMode,'xgs360028fPortSecurityAging':xgs360028fPortSecurityAging,'xgs360028fPortSecurityAgingPeriod':xgs360028fPortSecurityAgingPeriod,'xgs360028fPortSecLimitCtrlTable':xgs360028fPortSecLimitCtrlTable,'xgs360028fPortSecLimitCtrlEntry':xgs360028fPortSecLimitCtrlEntry,_o:xgs360028fPortSecLimitCtrlPort,'xgs360028fPortSecLimitCtrlPortMode':xgs360028fPortSecLimitCtrlPortMode,'xgs360028fPortSecLimitCtrlPortLimit':xgs360028fPortSecLimitCtrlPortLimit,'xgs360028fPortSecLimitCtrlPortAction':xgs360028fPortSecLimitCtrlPortAction,'xgs360028fPortSecLimitCtrlPortState':xgs360028fPortSecLimitCtrlPortState,'xgs360028fPortSecLimitCtrlPortReOpen':xgs360028fPortSecLimitCtrlPortReOpen,'xgs360028fPortSecSwitchStatusTable':xgs360028fPortSecSwitchStatusTable,'xgs360028fPortSecSwitchStatusEntry':xgs360028fPortSecSwitchStatusEntry,_p:xgs360028fPortSecSwitchStatusPort,'xgs360028fPortSecSwitchStatusUsers':xgs360028fPortSecSwitchStatusUsers,'xgs360028fPortSecSwitchStatusState':xgs360028fPortSecSwitchStatusState,'xgs360028fPortSecSwitchStatusMACCountCurrent':xgs360028fPortSecSwitchStatusMACCountCurrent,'xgs360028fPortSecSwitchStatusMACCountLimit':xgs360028fPortSecSwitchStatusMACCountLimit,'xgs360028fPortSecPortStatus':xgs360028fPortSecPortStatus,'xgs360028fPortSecPortStatusPort':xgs360028fPortSecPortStatusPort,'xgs360028fPortSecPortStatusTable':xgs360028fPortSecPortStatusTable,'xgs360028fPortSecPortStatusEntry':xgs360028fPortSecPortStatusEntry,_q:xgs360028fPortSecPortStatusIndex,'xgs360028fPortSecPortStatusMACAddress':xgs360028fPortSecPortStatusMACAddress,'xgs360028fPortSecPortStatusVLANId':xgs360028fPortSecPortStatusVLANId,'xgs360028fPortSecPortStatusState':xgs360028fPortSecPortStatusState,'xgs360028fPortSecPortStatusTimeOfAddition':xgs360028fPortSecPortStatusTimeOfAddition,'xgs360028fPortSecPortStatusAgeAndHold':xgs360028fPortSecPortStatusAgeAndHold,'xgs360028fAccessManagement':xgs360028fAccessManagement,'xgs360028fAccessMgtConf':xgs360028fAccessMgtConf,'xgs360028fAccessMgtConfMode':xgs360028fAccessMgtConfMode,'xgs360028fAccessMgtConfCreate':xgs360028fAccessMgtConfCreate,'xgs360028fAccessMgtConfTable':xgs360028fAccessMgtConfTable,'xgs360028fAccessMgtConfEntry':xgs360028fAccessMgtConfEntry,_r:xgs360028fAccessMgtIndex,'xgs360028fAccessMgtAddresstype':xgs360028fAccessMgtAddresstype,'xgs360028fAccessMgtStartIpAddress':xgs360028fAccessMgtStartIpAddress,'xgs360028fAccessMgtEndIpAddress':xgs360028fAccessMgtEndIpAddress,'xgs360028fAccessMgtHttpHttps':xgs360028fAccessMgtHttpHttps,'xgs360028fAccessMgtSNMP':xgs360028fAccessMgtSNMP,'xgs360028fAccessMgtTelnetSSH':xgs360028fAccessMgtTelnetSSH,'xgs360028fAccessMgtRowStatus':xgs360028fAccessMgtRowStatus,'xgs360028fAccessMgtStatistics':xgs360028fAccessMgtStatistics,'xgs360028fHttpReceivedPkts':xgs360028fHttpReceivedPkts,'xgs360028fHttpAllowedPkts':xgs360028fHttpAllowedPkts,'xgs360028fHttpDiscardedPkts':xgs360028fHttpDiscardedPkts,'xgs360028fHttpsReceivedPkts':xgs360028fHttpsReceivedPkts,'xgs360028fHttpsAllowedPkts':xgs360028fHttpsAllowedPkts,'xgs360028fHttpsDiscardedPkts':xgs360028fHttpsDiscardedPkts,'xgs360028fSnmpReceivedPkts':xgs360028fSnmpReceivedPkts,'xgs360028fSnmpAllowedPkts':xgs360028fSnmpAllowedPkts,'xgs360028fSnmpDiscardedPkts':xgs360028fSnmpDiscardedPkts,'xgs360028fTelnetReceivedPkts':xgs360028fTelnetReceivedPkts,'xgs360028fTelnetAllowedPkts':xgs360028fTelnetAllowedPkts,'xgs360028fTelnetDiscardedPkts':xgs360028fTelnetDiscardedPkts,'xgs360028fSSHReceivedPkts':xgs360028fSSHReceivedPkts,'xgs360028fSSHAllowedPkts':xgs360028fSSHAllowedPkts,'xgs360028fSSHDiscardedPkts':xgs360028fSSHDiscardedPkts,'xgs360028fAccessMgtStatisticsClearAll':xgs360028fAccessMgtStatisticsClearAll,'xgs360028fSSH':xgs360028fSSH,'xgs360028fSSHMode':xgs360028fSSHMode,'xgs360028fHTTPS':xgs360028fHTTPS,'xgs360028fHTTPSMode':xgs360028fHTTPSMode,'xgs360028fHTTPSAutoRedirect':xgs360028fHTTPSAutoRedirect,'xgs360028fAuthMethod':xgs360028fAuthMethod,'xgs360028fConsoleAuthMethod':xgs360028fConsoleAuthMethod,'xgs360028fConsoleFallback':xgs360028fConsoleFallback,'xgs360028fTelnetAuthMethod':xgs360028fTelnetAuthMethod,'xgs360028fTelnetFallback':xgs360028fTelnetFallback,'xgs360028fSshAuthMethod':xgs360028fSshAuthMethod,'xgs360028fSshFallback':xgs360028fSshFallback,'xgs360028fWebAuthMethod':xgs360028fWebAuthMethod,'xgs360028fWebFallback':xgs360028fWebFallback,'xgs360028fMaintenance':xgs360028fMaintenance,'xgs360028fRestartDevice':xgs360028fRestartDevice,'xgs360028fFirmware':xgs360028fFirmware,'xgs360028fFirmwareIpAddress':xgs360028fFirmwareIpAddress,'xgs360028fFirmwareFileName':xgs360028fFirmwareFileName,'xgs360028fDoFirmwareUpgrade':xgs360028fDoFirmwareUpgrade,'xgs360028fSaveOrRestore':xgs360028fSaveOrRestore,'xgs360028fFactoryDefaults':xgs360028fFactoryDefaults,'xgs360028fSaveStart':xgs360028fSaveStart,'xgs360028fSaveUser':xgs360028fSaveUser,'xgs360028fRestoreUser':xgs360028fRestoreUser,'xgs360028fExportOrImport':xgs360028fExportOrImport,'xgs360028fExportIpAddress':xgs360028fExportIpAddress,'xgs360028fExportConfigName':xgs360028fExportConfigName,'xgs360028fDoExportConfig':xgs360028fDoExportConfig,'xgs360028fImportIpAddress':xgs360028fImportIpAddress,'xgs360028fImportConfigName':xgs360028fImportConfigName,'xgs360028fDoImportConfig':xgs360028fDoImportConfig,'xgs360028fDiagnostics':xgs360028fDiagnostics,'xgs360028fPingIpAddress':xgs360028fPingIpAddress,'xgs360028fPingSize':xgs360028fPingSize,'xgs360028fDoPingConfig':xgs360028fDoPingConfig,'xgs360028fPingResult':xgs360028fPingResult,'xgs360028fPing6IpAddress':xgs360028fPing6IpAddress,'xgs360028fPing6Size':xgs360028fPing6Size,'xgs360028fDoPing6Config':xgs360028fDoPing6Config,'xgs360028fPing6Result':xgs360028fPing6Result,'xgs360028fVeriPHY':xgs360028fVeriPHY,'xgs360028fVeriPHYTest':xgs360028fVeriPHYTest,'xgs360028fVeriPHYTable':xgs360028fVeriPHYTable,'xgs360028fVeriPHYEntry':xgs360028fVeriPHYEntry,_s:xgs360028fVeriPHYPort,'xgs360028fVeriPHYPairA':xgs360028fVeriPHYPairA,'xgs360028fVeriPHYLengthA':xgs360028fVeriPHYLengthA,'xgs360028fVeriPHYPairB':xgs360028fVeriPHYPairB,'xgs360028fVeriPHYLengthB':xgs360028fVeriPHYLengthB,'xgs360028fVeriPHYPairC':xgs360028fVeriPHYPairC,'xgs360028fVeriPHYLengthC':xgs360028fVeriPHYLengthC,'xgs360028fVeriPHYPairD':xgs360028fVeriPHYPairD,'xgs360028fVeriPHYLengthD':xgs360028fVeriPHYLengthD,'xgs360028fTrap':xgs360028fTrap,'xgs360028fTrapEvent':xgs360028fTrapEvent,'xgs360028fEmergency':xgs360028fEmergency,'xgs360028fAlert':xgs360028fAlert,'xgs360028fCritical':xgs360028fCritical,'xgs360028fError':xgs360028fError,'xgs360028fWarning':xgs360028fWarning,'xgs360028fNotice':xgs360028fNotice,'xgs360028fInformational':xgs360028fInformational,'xgs360028fDebug':xgs360028fDebug,'xgs360028fTrapVariable':xgs360028fTrapVariable,_H:xgs360028fInformation})