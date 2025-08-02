_r='gel2esw10gVeriPHYPort'
_q='gel2esw10gAccessMgtIndex'
_p='gel2esw10gPortSecPortStatusIndex'
_o='gel2esw10gPortSecSwitchStatusPort'
_n='gel2esw10gPortSecLimitCtrlPort'
_m='gel2esw10gDHCPSnoopingStatisticsPort'
_l='gel2esw10gDHCPSnoopingPortModeConfigurationPort'
_k='gel2esw10gARPInspectionDynamicIndex'
_j='gel2esw10gARPInspectionStaticIndex'
_i='gel2esw10gARPInspectionConfPortIndex'
_h='gel2esw10gIPSourceGuardDynamicIndex'
_g='gel2esw10gIPSourceGuardStaticIndex'
_f='gel2esw10gIPSourceGuardPortConfigPort'
_e='gel2esw10gACLACEStatusIndex'
_d='gel2esw10gACLACEIndex'
_c='gel2esw10gACLRateLimiterID'
_b='gel2esw10gACLPortsConfPort'
_a='gel2esw10gMirrorPort'
_Z='gel2esw10gThermalProtectionPort'
_Y='gel2esw10gGVRPStatisticsPort'
_X='gel2esw10gGVRPConfPort'
_W='gel2esw10gGARPStatisticsPort'
_V='gel2esw10gGARPConfPort'
_U='gel2esw10gVoiceVLANOUIIndex'
_T='gel2esw10gVoiceVLANPort'
_S='gel2esw10gPortEEEPort'
_R='gel2esw10gSFPInfoIndex'
_Q='gel2esw10gPortQoSStatisticsPort'
_P='gel2esw10gPortTrafficStatisticsPort'
_O='gel2esw10gPortConfPort'
_N='gel2esw10gTrapHostConfIndex'
_M='gel2esw10gSyslogDetailedInfoIndex'
_L='gel2esw10gUserIndex'
_K='gel2esw10gSystemTimeNTPIndex'
_J='MacAddress'
_I='OctetString'
_H='gel2esw10gInformation'
_G='DisplayString'
_F='not-accessible'
_E='PRIVATETECH-GEL2ESW10G-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MacAddress,=mibBuilder.importSymbols('BRIDGE-MIB',_J)
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,_J,'PhysAddress','TextualConvention')
privatetech=ModuleIdentity((1,3,6,1,4,1,5205))
_Switch_ObjectIdentity=ObjectIdentity
switch=_Switch_ObjectIdentity((1,3,6,1,4,1,5205,2))
_Gel2esw10gProductId_ObjectIdentity=ObjectIdentity
gel2esw10gProductId=_Gel2esw10gProductId_ObjectIdentity((1,3,6,1,4,1,5205,2,51))
_Gel2esw10gSystem_ObjectIdentity=ObjectIdentity
gel2esw10gSystem=_Gel2esw10gSystem_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1))
_Gel2esw10gSystemInformation_ObjectIdentity=ObjectIdentity
gel2esw10gSystemInformation=_Gel2esw10gSystemInformation_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,1))
_Gel2esw10gModelName_Type=DisplayString
_Gel2esw10gModelName_Object=MibScalar
gel2esw10gModelName=_Gel2esw10gModelName_Object((1,3,6,1,4,1,5205,2,51,1,1,1),_Gel2esw10gModelName_Type())
gel2esw10gModelName.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gModelName.setStatus(_A)
_Gel2esw10gBIOSVersion_Type=DisplayString
_Gel2esw10gBIOSVersion_Object=MibScalar
gel2esw10gBIOSVersion=_Gel2esw10gBIOSVersion_Object((1,3,6,1,4,1,5205,2,51,1,1,2),_Gel2esw10gBIOSVersion_Type())
gel2esw10gBIOSVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gBIOSVersion.setStatus(_A)
_Gel2esw10gFirmwareVersion_Type=DisplayString
_Gel2esw10gFirmwareVersion_Object=MibScalar
gel2esw10gFirmwareVersion=_Gel2esw10gFirmwareVersion_Object((1,3,6,1,4,1,5205,2,51,1,1,3),_Gel2esw10gFirmwareVersion_Type())
gel2esw10gFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gFirmwareVersion.setStatus(_A)
_Gel2esw10gHardwareMechanicalVersion_Type=DisplayString
_Gel2esw10gHardwareMechanicalVersion_Object=MibScalar
gel2esw10gHardwareMechanicalVersion=_Gel2esw10gHardwareMechanicalVersion_Object((1,3,6,1,4,1,5205,2,51,1,1,4),_Gel2esw10gHardwareMechanicalVersion_Type())
gel2esw10gHardwareMechanicalVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gHardwareMechanicalVersion.setStatus(_A)
_Gel2esw10gSeriesNumber_Type=DisplayString
_Gel2esw10gSeriesNumber_Object=MibScalar
gel2esw10gSeriesNumber=_Gel2esw10gSeriesNumber_Object((1,3,6,1,4,1,5205,2,51,1,1,5),_Gel2esw10gSeriesNumber_Type())
gel2esw10gSeriesNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSeriesNumber.setStatus(_A)
_Gel2esw10gHostMACAddress_Type=MacAddress
_Gel2esw10gHostMACAddress_Object=MibScalar
gel2esw10gHostMACAddress=_Gel2esw10gHostMACAddress_Object((1,3,6,1,4,1,5205,2,51,1,1,6),_Gel2esw10gHostMACAddress_Type())
gel2esw10gHostMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gHostMACAddress.setStatus(_A)
_Gel2esw10gConsoleBaudrate_Type=DisplayString
_Gel2esw10gConsoleBaudrate_Object=MibScalar
gel2esw10gConsoleBaudrate=_Gel2esw10gConsoleBaudrate_Object((1,3,6,1,4,1,5205,2,51,1,1,7),_Gel2esw10gConsoleBaudrate_Type())
gel2esw10gConsoleBaudrate.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gConsoleBaudrate.setStatus(_A)
_Gel2esw10gRAMSize_Type=DisplayString
_Gel2esw10gRAMSize_Object=MibScalar
gel2esw10gRAMSize=_Gel2esw10gRAMSize_Object((1,3,6,1,4,1,5205,2,51,1,1,8),_Gel2esw10gRAMSize_Type())
gel2esw10gRAMSize.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gRAMSize.setStatus(_A)
_Gel2esw10gFlashSize_Type=DisplayString
_Gel2esw10gFlashSize_Object=MibScalar
gel2esw10gFlashSize=_Gel2esw10gFlashSize_Object((1,3,6,1,4,1,5205,2,51,1,1,9),_Gel2esw10gFlashSize_Type())
gel2esw10gFlashSize.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gFlashSize.setStatus(_A)
_Gel2esw10gBridgeFBDSize_Type=DisplayString
_Gel2esw10gBridgeFBDSize_Object=MibScalar
gel2esw10gBridgeFBDSize=_Gel2esw10gBridgeFBDSize_Object((1,3,6,1,4,1,5205,2,51,1,1,10),_Gel2esw10gBridgeFBDSize_Type())
gel2esw10gBridgeFBDSize.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gBridgeFBDSize.setStatus(_A)
_Gel2esw10gTransmitQueue_Type=DisplayString
_Gel2esw10gTransmitQueue_Object=MibScalar
gel2esw10gTransmitQueue=_Gel2esw10gTransmitQueue_Object((1,3,6,1,4,1,5205,2,51,1,1,11),_Gel2esw10gTransmitQueue_Type())
gel2esw10gTransmitQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gTransmitQueue.setStatus(_A)
_Gel2esw10gMaximumFrameSize_Type=DisplayString
_Gel2esw10gMaximumFrameSize_Object=MibScalar
gel2esw10gMaximumFrameSize=_Gel2esw10gMaximumFrameSize_Object((1,3,6,1,4,1,5205,2,51,1,1,12),_Gel2esw10gMaximumFrameSize_Type())
gel2esw10gMaximumFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gMaximumFrameSize.setStatus(_A)
_Gel2esw10gCPULoad_Type=DisplayString
_Gel2esw10gCPULoad_Object=MibScalar
gel2esw10gCPULoad=_Gel2esw10gCPULoad_Object((1,3,6,1,4,1,5205,2,51,1,1,13),_Gel2esw10gCPULoad_Type())
gel2esw10gCPULoad.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gCPULoad.setStatus(_A)
_Gel2esw10gSystemTime_ObjectIdentity=ObjectIdentity
gel2esw10gSystemTime=_Gel2esw10gSystemTime_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,2))
_Gel2esw10gSystemTimeManual_ObjectIdentity=ObjectIdentity
gel2esw10gSystemTimeManual=_Gel2esw10gSystemTimeManual_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,2,1))
class _Gel2esw10gSystemTimeManualClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gSystemTimeManualClockSource_Type.__name__=_C
_Gel2esw10gSystemTimeManualClockSource_Object=MibScalar
gel2esw10gSystemTimeManualClockSource=_Gel2esw10gSystemTimeManualClockSource_Object((1,3,6,1,4,1,5205,2,51,1,2,1,1),_Gel2esw10gSystemTimeManualClockSource_Type())
gel2esw10gSystemTimeManualClockSource.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualClockSource.setStatus(_A)
_Gel2esw10gSystemTimeManualLocaltime_Type=DisplayString
_Gel2esw10gSystemTimeManualLocaltime_Object=MibScalar
gel2esw10gSystemTimeManualLocaltime=_Gel2esw10gSystemTimeManualLocaltime_Object((1,3,6,1,4,1,5205,2,51,1,2,1,2),_Gel2esw10gSystemTimeManualLocaltime_Type())
gel2esw10gSystemTimeManualLocaltime.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualLocaltime.setStatus(_A)
class _Gel2esw10gSystemTimeManualTimeZoneOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-720,780))
_Gel2esw10gSystemTimeManualTimeZoneOffset_Type.__name__=_C
_Gel2esw10gSystemTimeManualTimeZoneOffset_Object=MibScalar
gel2esw10gSystemTimeManualTimeZoneOffset=_Gel2esw10gSystemTimeManualTimeZoneOffset_Object((1,3,6,1,4,1,5205,2,51,1,2,1,3),_Gel2esw10gSystemTimeManualTimeZoneOffset_Type())
gel2esw10gSystemTimeManualTimeZoneOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualTimeZoneOffset.setStatus(_A)
class _Gel2esw10gSystemTimeManualDaylightSavings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gSystemTimeManualDaylightSavings_Type.__name__=_C
_Gel2esw10gSystemTimeManualDaylightSavings_Object=MibScalar
gel2esw10gSystemTimeManualDaylightSavings=_Gel2esw10gSystemTimeManualDaylightSavings_Object((1,3,6,1,4,1,5205,2,51,1,2,1,4),_Gel2esw10gSystemTimeManualDaylightSavings_Type())
gel2esw10gSystemTimeManualDaylightSavings.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualDaylightSavings.setStatus(_A)
class _Gel2esw10gSystemTimeManualTimeSetOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_Gel2esw10gSystemTimeManualTimeSetOffset_Type.__name__=_C
_Gel2esw10gSystemTimeManualTimeSetOffset_Object=MibScalar
gel2esw10gSystemTimeManualTimeSetOffset=_Gel2esw10gSystemTimeManualTimeSetOffset_Object((1,3,6,1,4,1,5205,2,51,1,2,1,5),_Gel2esw10gSystemTimeManualTimeSetOffset_Type())
gel2esw10gSystemTimeManualTimeSetOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualTimeSetOffset.setStatus(_A)
class _Gel2esw10gSystemTimeManualDaylightSavingsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gSystemTimeManualDaylightSavingsType_Type.__name__=_C
_Gel2esw10gSystemTimeManualDaylightSavingsType_Object=MibScalar
gel2esw10gSystemTimeManualDaylightSavingsType=_Gel2esw10gSystemTimeManualDaylightSavingsType_Object((1,3,6,1,4,1,5205,2,51,1,2,1,6),_Gel2esw10gSystemTimeManualDaylightSavingsType_Type())
gel2esw10gSystemTimeManualDaylightSavingsType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualDaylightSavingsType.setStatus(_A)
_Gel2esw10gSystemTimeManualDaylightSavingsBydatesFrom_Type=DisplayString
_Gel2esw10gSystemTimeManualDaylightSavingsBydatesFrom_Object=MibScalar
gel2esw10gSystemTimeManualDaylightSavingsBydatesFrom=_Gel2esw10gSystemTimeManualDaylightSavingsBydatesFrom_Object((1,3,6,1,4,1,5205,2,51,1,2,1,7),_Gel2esw10gSystemTimeManualDaylightSavingsBydatesFrom_Type())
gel2esw10gSystemTimeManualDaylightSavingsBydatesFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualDaylightSavingsBydatesFrom.setStatus(_A)
_Gel2esw10gSystemTimeManualDaylightSavingsBydatesTo_Type=DisplayString
_Gel2esw10gSystemTimeManualDaylightSavingsBydatesTo_Object=MibScalar
gel2esw10gSystemTimeManualDaylightSavingsBydatesTo=_Gel2esw10gSystemTimeManualDaylightSavingsBydatesTo_Object((1,3,6,1,4,1,5205,2,51,1,2,1,8),_Gel2esw10gSystemTimeManualDaylightSavingsBydatesTo_Type())
gel2esw10gSystemTimeManualDaylightSavingsBydatesTo.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualDaylightSavingsBydatesTo.setStatus(_A)
class _Gel2esw10gSystemTimeManualDaylightSavingsRecurringDayFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringDayFrom_Type.__name__=_C
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringDayFrom_Object=MibScalar
gel2esw10gSystemTimeManualDaylightSavingsRecurringDayFrom=_Gel2esw10gSystemTimeManualDaylightSavingsRecurringDayFrom_Object((1,3,6,1,4,1,5205,2,51,1,2,1,9),_Gel2esw10gSystemTimeManualDaylightSavingsRecurringDayFrom_Type())
gel2esw10gSystemTimeManualDaylightSavingsRecurringDayFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualDaylightSavingsRecurringDayFrom.setStatus(_A)
class _Gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekFrom_Type.__name__=_C
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekFrom_Object=MibScalar
gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekFrom=_Gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekFrom_Object((1,3,6,1,4,1,5205,2,51,1,2,1,10),_Gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekFrom_Type())
gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekFrom.setStatus(_A)
class _Gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthFrom_Type.__name__=_C
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthFrom_Object=MibScalar
gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthFrom=_Gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthFrom_Object((1,3,6,1,4,1,5205,2,51,1,2,1,11),_Gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthFrom_Type())
gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthFrom.setStatus(_A)
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeFrom_Type=DisplayString
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeFrom_Object=MibScalar
gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeFrom=_Gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeFrom_Object((1,3,6,1,4,1,5205,2,51,1,2,1,12),_Gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeFrom_Type())
gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeFrom.setStatus(_A)
class _Gel2esw10gSystemTimeManualDaylightSavingsRecurringDayTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringDayTo_Type.__name__=_C
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringDayTo_Object=MibScalar
gel2esw10gSystemTimeManualDaylightSavingsRecurringDayTo=_Gel2esw10gSystemTimeManualDaylightSavingsRecurringDayTo_Object((1,3,6,1,4,1,5205,2,51,1,2,1,13),_Gel2esw10gSystemTimeManualDaylightSavingsRecurringDayTo_Type())
gel2esw10gSystemTimeManualDaylightSavingsRecurringDayTo.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualDaylightSavingsRecurringDayTo.setStatus(_A)
class _Gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekTo_Type.__name__=_C
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekTo_Object=MibScalar
gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekTo=_Gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekTo_Object((1,3,6,1,4,1,5205,2,51,1,2,1,14),_Gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekTo_Type())
gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekTo.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekTo.setStatus(_A)
class _Gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthTo_Type.__name__=_C
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthTo_Object=MibScalar
gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthTo=_Gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthTo_Object((1,3,6,1,4,1,5205,2,51,1,2,1,15),_Gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthTo_Type())
gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthTo.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthTo.setStatus(_A)
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeTo_Type=DisplayString
_Gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeTo_Object=MibScalar
gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeTo=_Gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeTo_Object((1,3,6,1,4,1,5205,2,51,1,2,1,16),_Gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeTo_Type())
gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeTo.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeTo.setStatus(_A)
_Gel2esw10gSystemTimeNTP_ObjectIdentity=ObjectIdentity
gel2esw10gSystemTimeNTP=_Gel2esw10gSystemTimeNTP_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,2,2))
_Gel2esw10gSystemTimeNTPTable_Object=MibTable
gel2esw10gSystemTimeNTPTable=_Gel2esw10gSystemTimeNTPTable_Object((1,3,6,1,4,1,5205,2,51,1,2,2,1))
if mibBuilder.loadTexts:gel2esw10gSystemTimeNTPTable.setStatus(_A)
_Gel2esw10gSystemTimeNTPEntry_Object=MibTableRow
gel2esw10gSystemTimeNTPEntry=_Gel2esw10gSystemTimeNTPEntry_Object((1,3,6,1,4,1,5205,2,51,1,2,2,1,1))
gel2esw10gSystemTimeNTPEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:gel2esw10gSystemTimeNTPEntry.setStatus(_A)
class _Gel2esw10gSystemTimeNTPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw10gSystemTimeNTPIndex_Type.__name__=_C
_Gel2esw10gSystemTimeNTPIndex_Object=MibTableColumn
gel2esw10gSystemTimeNTPIndex=_Gel2esw10gSystemTimeNTPIndex_Object((1,3,6,1,4,1,5205,2,51,1,2,2,1,1,1),_Gel2esw10gSystemTimeNTPIndex_Type())
gel2esw10gSystemTimeNTPIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gSystemTimeNTPIndex.setStatus(_A)
class _Gel2esw10gSystemTimeNTPServerIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gSystemTimeNTPServerIPType_Type.__name__=_C
_Gel2esw10gSystemTimeNTPServerIPType_Object=MibTableColumn
gel2esw10gSystemTimeNTPServerIPType=_Gel2esw10gSystemTimeNTPServerIPType_Object((1,3,6,1,4,1,5205,2,51,1,2,2,1,1,2),_Gel2esw10gSystemTimeNTPServerIPType_Type())
gel2esw10gSystemTimeNTPServerIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeNTPServerIPType.setStatus(_A)
_Gel2esw10gSystemTimeNTPServer_Type=DisplayString
_Gel2esw10gSystemTimeNTPServer_Object=MibTableColumn
gel2esw10gSystemTimeNTPServer=_Gel2esw10gSystemTimeNTPServer_Object((1,3,6,1,4,1,5205,2,51,1,2,2,1,1,3),_Gel2esw10gSystemTimeNTPServer_Type())
gel2esw10gSystemTimeNTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeNTPServer.setStatus(_A)
class _Gel2esw10gSystemTimeNTPCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw10gSystemTimeNTPCurrentMode_Type.__name__=_C
_Gel2esw10gSystemTimeNTPCurrentMode_Object=MibTableColumn
gel2esw10gSystemTimeNTPCurrentMode=_Gel2esw10gSystemTimeNTPCurrentMode_Object((1,3,6,1,4,1,5205,2,51,1,2,2,1,1,4),_Gel2esw10gSystemTimeNTPCurrentMode_Type())
gel2esw10gSystemTimeNTPCurrentMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemTimeNTPCurrentMode.setStatus(_A)
_Gel2esw10gSystemAccount_ObjectIdentity=ObjectIdentity
gel2esw10gSystemAccount=_Gel2esw10gSystemAccount_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,3))
_Gel2esw10gSystemAccountUsers_ObjectIdentity=ObjectIdentity
gel2esw10gSystemAccountUsers=_Gel2esw10gSystemAccountUsers_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,3,1))
class _Gel2esw10gSystemAccountUserCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gSystemAccountUserCreate_Type.__name__=_C
_Gel2esw10gSystemAccountUserCreate_Object=MibScalar
gel2esw10gSystemAccountUserCreate=_Gel2esw10gSystemAccountUserCreate_Object((1,3,6,1,4,1,5205,2,51,1,3,1,1),_Gel2esw10gSystemAccountUserCreate_Type())
gel2esw10gSystemAccountUserCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemAccountUserCreate.setStatus(_A)
_Gel2esw10gSystemAccountUsersTable_Object=MibTable
gel2esw10gSystemAccountUsersTable=_Gel2esw10gSystemAccountUsersTable_Object((1,3,6,1,4,1,5205,2,51,1,3,1,2))
if mibBuilder.loadTexts:gel2esw10gSystemAccountUsersTable.setStatus(_A)
_Gel2esw10gSystemAccountUsersEntry_Object=MibTableRow
gel2esw10gSystemAccountUsersEntry=_Gel2esw10gSystemAccountUsersEntry_Object((1,3,6,1,4,1,5205,2,51,1,3,1,2,1))
gel2esw10gSystemAccountUsersEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:gel2esw10gSystemAccountUsersEntry.setStatus(_A)
class _Gel2esw10gUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_Gel2esw10gUserIndex_Type.__name__=_C
_Gel2esw10gUserIndex_Object=MibTableColumn
gel2esw10gUserIndex=_Gel2esw10gUserIndex_Object((1,3,6,1,4,1,5205,2,51,1,3,1,2,1,1),_Gel2esw10gUserIndex_Type())
gel2esw10gUserIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gUserIndex.setStatus(_A)
class _Gel2esw10gUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Gel2esw10gUserName_Type.__name__=_G
_Gel2esw10gUserName_Object=MibTableColumn
gel2esw10gUserName=_Gel2esw10gUserName_Object((1,3,6,1,4,1,5205,2,51,1,3,1,2,1,2),_Gel2esw10gUserName_Type())
gel2esw10gUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gUserName.setStatus(_A)
class _Gel2esw10gPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Gel2esw10gPassword_Type.__name__=_G
_Gel2esw10gPassword_Object=MibTableColumn
gel2esw10gPassword=_Gel2esw10gPassword_Object((1,3,6,1,4,1,5205,2,51,1,3,1,2,1,3),_Gel2esw10gPassword_Type())
gel2esw10gPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPassword.setStatus(_A)
class _Gel2esw10gUserPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gUserPrivilegeLevel_Type.__name__=_C
_Gel2esw10gUserPrivilegeLevel_Object=MibTableColumn
gel2esw10gUserPrivilegeLevel=_Gel2esw10gUserPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,1,2,1,4),_Gel2esw10gUserPrivilegeLevel_Type())
gel2esw10gUserPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gUserPrivilegeLevel.setStatus(_A)
class _Gel2esw10gAccountUserRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw10gAccountUserRowStatus_Type.__name__=_C
_Gel2esw10gAccountUserRowStatus_Object=MibTableColumn
gel2esw10gAccountUserRowStatus=_Gel2esw10gAccountUserRowStatus_Object((1,3,6,1,4,1,5205,2,51,1,3,1,2,1,5),_Gel2esw10gAccountUserRowStatus_Type())
gel2esw10gAccountUserRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gAccountUserRowStatus.setStatus(_A)
_Gel2esw10gSystemAccountPrivilegeLevel_ObjectIdentity=ObjectIdentity
gel2esw10gSystemAccountPrivilegeLevel=_Gel2esw10gSystemAccountPrivilegeLevel_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,3,2))
class _Gel2esw10gAccountPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gAccountPrivilegeLevel_Type.__name__=_C
_Gel2esw10gAccountPrivilegeLevel_Object=MibScalar
gel2esw10gAccountPrivilegeLevel=_Gel2esw10gAccountPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,1),_Gel2esw10gAccountPrivilegeLevel_Type())
gel2esw10gAccountPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gAccountPrivilegeLevel.setStatus(_A)
class _Gel2esw10gAggregationPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gAggregationPrivilegeLevel_Type.__name__=_C
_Gel2esw10gAggregationPrivilegeLevel_Object=MibScalar
gel2esw10gAggregationPrivilegeLevel=_Gel2esw10gAggregationPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,2),_Gel2esw10gAggregationPrivilegeLevel_Type())
gel2esw10gAggregationPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gAggregationPrivilegeLevel.setStatus(_A)
class _Gel2esw10gDiagnosticsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gDiagnosticsPrivilegeLevel_Type.__name__=_C
_Gel2esw10gDiagnosticsPrivilegeLevel_Object=MibScalar
gel2esw10gDiagnosticsPrivilegeLevel=_Gel2esw10gDiagnosticsPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,3),_Gel2esw10gDiagnosticsPrivilegeLevel_Type())
gel2esw10gDiagnosticsPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gDiagnosticsPrivilegeLevel.setStatus(_A)
class _Gel2esw10gEEEPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gEEEPrivilegeLevel_Type.__name__=_C
_Gel2esw10gEEEPrivilegeLevel_Object=MibScalar
gel2esw10gEEEPrivilegeLevel=_Gel2esw10gEEEPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,4),_Gel2esw10gEEEPrivilegeLevel_Type())
gel2esw10gEEEPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gEEEPrivilegeLevel.setStatus(_A)
class _Gel2esw10gEasyportPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gEasyportPrivilegeLevel_Type.__name__=_C
_Gel2esw10gEasyportPrivilegeLevel_Object=MibScalar
gel2esw10gEasyportPrivilegeLevel=_Gel2esw10gEasyportPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,5),_Gel2esw10gEasyportPrivilegeLevel_Type())
gel2esw10gEasyportPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gEasyportPrivilegeLevel.setStatus(_A)
class _Gel2esw10gGARPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gGARPPrivilegeLevel_Type.__name__=_C
_Gel2esw10gGARPPrivilegeLevel_Object=MibScalar
gel2esw10gGARPPrivilegeLevel=_Gel2esw10gGARPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,6),_Gel2esw10gGARPPrivilegeLevel_Type())
gel2esw10gGARPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gGARPPrivilegeLevel.setStatus(_A)
class _Gel2esw10gGVRPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gGVRPPrivilegeLevel_Type.__name__=_C
_Gel2esw10gGVRPPrivilegeLevel_Object=MibScalar
gel2esw10gGVRPPrivilegeLevel=_Gel2esw10gGVRPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,7),_Gel2esw10gGVRPPrivilegeLevel_Type())
gel2esw10gGVRPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gGVRPPrivilegeLevel.setStatus(_A)
class _Gel2esw10gIPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gIPPrivilegeLevel_Type.__name__=_C
_Gel2esw10gIPPrivilegeLevel_Object=MibScalar
gel2esw10gIPPrivilegeLevel=_Gel2esw10gIPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,8),_Gel2esw10gIPPrivilegeLevel_Type())
gel2esw10gIPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPPrivilegeLevel.setStatus(_A)
class _Gel2esw10gIPMCSnoopingPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gIPMCSnoopingPrivilegeLevel_Type.__name__=_C
_Gel2esw10gIPMCSnoopingPrivilegeLevel_Object=MibScalar
gel2esw10gIPMCSnoopingPrivilegeLevel=_Gel2esw10gIPMCSnoopingPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,9),_Gel2esw10gIPMCSnoopingPrivilegeLevel_Type())
gel2esw10gIPMCSnoopingPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPMCSnoopingPrivilegeLevel.setStatus(_A)
class _Gel2esw10gLACPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gLACPPrivilegeLevel_Type.__name__=_C
_Gel2esw10gLACPPrivilegeLevel_Object=MibScalar
gel2esw10gLACPPrivilegeLevel=_Gel2esw10gLACPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,10),_Gel2esw10gLACPPrivilegeLevel_Type())
gel2esw10gLACPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gLACPPrivilegeLevel.setStatus(_A)
class _Gel2esw10gLLDPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gLLDPPrivilegeLevel_Type.__name__=_C
_Gel2esw10gLLDPPrivilegeLevel_Object=MibScalar
gel2esw10gLLDPPrivilegeLevel=_Gel2esw10gLLDPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,11),_Gel2esw10gLLDPPrivilegeLevel_Type())
gel2esw10gLLDPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gLLDPPrivilegeLevel.setStatus(_A)
class _Gel2esw10gLLDPMEDPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gLLDPMEDPrivilegeLevel_Type.__name__=_C
_Gel2esw10gLLDPMEDPrivilegeLevel_Object=MibScalar
gel2esw10gLLDPMEDPrivilegeLevel=_Gel2esw10gLLDPMEDPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,12),_Gel2esw10gLLDPMEDPrivilegeLevel_Type())
gel2esw10gLLDPMEDPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gLLDPMEDPrivilegeLevel.setStatus(_A)
class _Gel2esw10gMACTablePrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gMACTablePrivilegeLevel_Type.__name__=_C
_Gel2esw10gMACTablePrivilegeLevel_Object=MibScalar
gel2esw10gMACTablePrivilegeLevel=_Gel2esw10gMACTablePrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,13),_Gel2esw10gMACTablePrivilegeLevel_Type())
gel2esw10gMACTablePrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gMACTablePrivilegeLevel.setStatus(_A)
class _Gel2esw10gMRPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gMRPPrivilegeLevel_Type.__name__=_C
_Gel2esw10gMRPPrivilegeLevel_Object=MibScalar
gel2esw10gMRPPrivilegeLevel=_Gel2esw10gMRPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,14),_Gel2esw10gMRPPrivilegeLevel_Type())
gel2esw10gMRPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gMRPPrivilegeLevel.setStatus(_A)
class _Gel2esw10gMVRPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gMVRPrivilegeLevel_Type.__name__=_C
_Gel2esw10gMVRPrivilegeLevel_Object=MibScalar
gel2esw10gMVRPrivilegeLevel=_Gel2esw10gMVRPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,15),_Gel2esw10gMVRPrivilegeLevel_Type())
gel2esw10gMVRPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gMVRPrivilegeLevel.setStatus(_A)
class _Gel2esw10gMVRPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gMVRPPrivilegeLevel_Type.__name__=_C
_Gel2esw10gMVRPPrivilegeLevel_Object=MibScalar
gel2esw10gMVRPPrivilegeLevel=_Gel2esw10gMVRPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,16),_Gel2esw10gMVRPPrivilegeLevel_Type())
gel2esw10gMVRPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gMVRPPrivilegeLevel.setStatus(_A)
class _Gel2esw10gMaintenancePrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gMaintenancePrivilegeLevel_Type.__name__=_C
_Gel2esw10gMaintenancePrivilegeLevel_Object=MibScalar
gel2esw10gMaintenancePrivilegeLevel=_Gel2esw10gMaintenancePrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,17),_Gel2esw10gMaintenancePrivilegeLevel_Type())
gel2esw10gMaintenancePrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gMaintenancePrivilegeLevel.setStatus(_A)
class _Gel2esw10gMirroringPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gMirroringPrivilegeLevel_Type.__name__=_C
_Gel2esw10gMirroringPrivilegeLevel_Object=MibScalar
gel2esw10gMirroringPrivilegeLevel=_Gel2esw10gMirroringPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,18),_Gel2esw10gMirroringPrivilegeLevel_Type())
gel2esw10gMirroringPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gMirroringPrivilegeLevel.setStatus(_A)
class _Gel2esw10gPortsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gPortsPrivilegeLevel_Type.__name__=_C
_Gel2esw10gPortsPrivilegeLevel_Object=MibScalar
gel2esw10gPortsPrivilegeLevel=_Gel2esw10gPortsPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,19),_Gel2esw10gPortsPrivilegeLevel_Type())
gel2esw10gPortsPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortsPrivilegeLevel.setStatus(_A)
class _Gel2esw10gPrivateVLANsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gPrivateVLANsPrivilegeLevel_Type.__name__=_C
_Gel2esw10gPrivateVLANsPrivilegeLevel_Object=MibScalar
gel2esw10gPrivateVLANsPrivilegeLevel=_Gel2esw10gPrivateVLANsPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,20),_Gel2esw10gPrivateVLANsPrivilegeLevel_Type())
gel2esw10gPrivateVLANsPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPrivateVLANsPrivilegeLevel.setStatus(_A)
class _Gel2esw10gQoSPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gQoSPrivilegeLevel_Type.__name__=_C
_Gel2esw10gQoSPrivilegeLevel_Object=MibScalar
gel2esw10gQoSPrivilegeLevel=_Gel2esw10gQoSPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,21),_Gel2esw10gQoSPrivilegeLevel_Type())
gel2esw10gQoSPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gQoSPrivilegeLevel.setStatus(_A)
class _Gel2esw10gSMTPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gSMTPPrivilegeLevel_Type.__name__=_C
_Gel2esw10gSMTPPrivilegeLevel_Object=MibScalar
gel2esw10gSMTPPrivilegeLevel=_Gel2esw10gSMTPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,22),_Gel2esw10gSMTPPrivilegeLevel_Type())
gel2esw10gSMTPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSMTPPrivilegeLevel.setStatus(_A)
class _Gel2esw10gSNMPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gSNMPPrivilegeLevel_Type.__name__=_C
_Gel2esw10gSNMPPrivilegeLevel_Object=MibScalar
gel2esw10gSNMPPrivilegeLevel=_Gel2esw10gSNMPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,23),_Gel2esw10gSNMPPrivilegeLevel_Type())
gel2esw10gSNMPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSNMPPrivilegeLevel.setStatus(_A)
class _Gel2esw10gSecurityPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gSecurityPrivilegeLevel_Type.__name__=_C
_Gel2esw10gSecurityPrivilegeLevel_Object=MibScalar
gel2esw10gSecurityPrivilegeLevel=_Gel2esw10gSecurityPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,24),_Gel2esw10gSecurityPrivilegeLevel_Type())
gel2esw10gSecurityPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSecurityPrivilegeLevel.setStatus(_A)
class _Gel2esw10gSpanningTreePrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gSpanningTreePrivilegeLevel_Type.__name__=_C
_Gel2esw10gSpanningTreePrivilegeLevel_Object=MibScalar
gel2esw10gSpanningTreePrivilegeLevel=_Gel2esw10gSpanningTreePrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,25),_Gel2esw10gSpanningTreePrivilegeLevel_Type())
gel2esw10gSpanningTreePrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSpanningTreePrivilegeLevel.setStatus(_A)
class _Gel2esw10gSystemPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gSystemPrivilegeLevel_Type.__name__=_C
_Gel2esw10gSystemPrivilegeLevel_Object=MibScalar
gel2esw10gSystemPrivilegeLevel=_Gel2esw10gSystemPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,26),_Gel2esw10gSystemPrivilegeLevel_Type())
gel2esw10gSystemPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSystemPrivilegeLevel.setStatus(_A)
class _Gel2esw10gTrapEventPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gTrapEventPrivilegeLevel_Type.__name__=_C
_Gel2esw10gTrapEventPrivilegeLevel_Object=MibScalar
gel2esw10gTrapEventPrivilegeLevel=_Gel2esw10gTrapEventPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,27),_Gel2esw10gTrapEventPrivilegeLevel_Type())
gel2esw10gTrapEventPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventPrivilegeLevel.setStatus(_A)
class _Gel2esw10gVCLPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gVCLPrivilegeLevel_Type.__name__=_C
_Gel2esw10gVCLPrivilegeLevel_Object=MibScalar
gel2esw10gVCLPrivilegeLevel=_Gel2esw10gVCLPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,28),_Gel2esw10gVCLPrivilegeLevel_Type())
gel2esw10gVCLPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gVCLPrivilegeLevel.setStatus(_A)
class _Gel2esw10gVLANsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gVLANsPrivilegeLevel_Type.__name__=_C
_Gel2esw10gVLANsPrivilegeLevel_Object=MibScalar
gel2esw10gVLANsPrivilegeLevel=_Gel2esw10gVLANsPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,29),_Gel2esw10gVLANsPrivilegeLevel_Type())
gel2esw10gVLANsPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gVLANsPrivilegeLevel.setStatus(_A)
class _Gel2esw10gVoiceVLANPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw10gVoiceVLANPrivilegeLevel_Type.__name__=_C
_Gel2esw10gVoiceVLANPrivilegeLevel_Object=MibScalar
gel2esw10gVoiceVLANPrivilegeLevel=_Gel2esw10gVoiceVLANPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,51,1,3,2,30),_Gel2esw10gVoiceVLANPrivilegeLevel_Type())
gel2esw10gVoiceVLANPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gVoiceVLANPrivilegeLevel.setStatus(_A)
_Gel2esw10gIP_ObjectIdentity=ObjectIdentity
gel2esw10gIP=_Gel2esw10gIP_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,4))
_Gel2esw10gIPv4_ObjectIdentity=ObjectIdentity
gel2esw10gIPv4=_Gel2esw10gIPv4_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,4,1))
_Gel2esw10gIPv4Configured_ObjectIdentity=ObjectIdentity
gel2esw10gIPv4Configured=_Gel2esw10gIPv4Configured_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,4,1,1))
class _Gel2esw10gIpv4DHCPClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gIpv4DHCPClient_Type.__name__=_C
_Gel2esw10gIpv4DHCPClient_Object=MibScalar
gel2esw10gIpv4DHCPClient=_Gel2esw10gIpv4DHCPClient_Object((1,3,6,1,4,1,5205,2,51,1,4,1,1,1),_Gel2esw10gIpv4DHCPClient_Type())
gel2esw10gIpv4DHCPClient.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIpv4DHCPClient.setStatus(_A)
_Gel2esw10gIPv4Address_Type=IpAddress
_Gel2esw10gIPv4Address_Object=MibScalar
gel2esw10gIPv4Address=_Gel2esw10gIPv4Address_Object((1,3,6,1,4,1,5205,2,51,1,4,1,1,2),_Gel2esw10gIPv4Address_Type())
gel2esw10gIPv4Address.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPv4Address.setStatus(_A)
_Gel2esw10gIPv4Mask_Type=IpAddress
_Gel2esw10gIPv4Mask_Object=MibScalar
gel2esw10gIPv4Mask=_Gel2esw10gIPv4Mask_Object((1,3,6,1,4,1,5205,2,51,1,4,1,1,3),_Gel2esw10gIPv4Mask_Type())
gel2esw10gIPv4Mask.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPv4Mask.setStatus(_A)
_Gel2esw10gIPv4Router_Type=IpAddress
_Gel2esw10gIPv4Router_Object=MibScalar
gel2esw10gIPv4Router=_Gel2esw10gIPv4Router_Object((1,3,6,1,4,1,5205,2,51,1,4,1,1,4),_Gel2esw10gIPv4Router_Type())
gel2esw10gIPv4Router.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPv4Router.setStatus(_A)
class _Gel2esw10gIPv4VLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw10gIPv4VLANId_Type.__name__=_C
_Gel2esw10gIPv4VLANId_Object=MibScalar
gel2esw10gIPv4VLANId=_Gel2esw10gIPv4VLANId_Object((1,3,6,1,4,1,5205,2,51,1,4,1,1,5),_Gel2esw10gIPv4VLANId_Type())
gel2esw10gIPv4VLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPv4VLANId.setStatus(_A)
_Gel2esw10gIPv4DNSServer_Type=IpAddress
_Gel2esw10gIPv4DNSServer_Object=MibScalar
gel2esw10gIPv4DNSServer=_Gel2esw10gIPv4DNSServer_Object((1,3,6,1,4,1,5205,2,51,1,4,1,1,6),_Gel2esw10gIPv4DNSServer_Type())
gel2esw10gIPv4DNSServer.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPv4DNSServer.setStatus(_A)
class _Gel2esw10gIPv4DNSProxy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gIPv4DNSProxy_Type.__name__=_C
_Gel2esw10gIPv4DNSProxy_Object=MibScalar
gel2esw10gIPv4DNSProxy=_Gel2esw10gIPv4DNSProxy_Object((1,3,6,1,4,1,5205,2,51,1,4,1,1,7),_Gel2esw10gIPv4DNSProxy_Type())
gel2esw10gIPv4DNSProxy.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPv4DNSProxy.setStatus(_A)
_Gel2esw10gIPv4Current_ObjectIdentity=ObjectIdentity
gel2esw10gIPv4Current=_Gel2esw10gIPv4Current_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,4,1,2))
class _Gel2esw10gIpv4CurrentDHCPClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gIpv4CurrentDHCPClient_Type.__name__=_C
_Gel2esw10gIpv4CurrentDHCPClient_Object=MibScalar
gel2esw10gIpv4CurrentDHCPClient=_Gel2esw10gIpv4CurrentDHCPClient_Object((1,3,6,1,4,1,5205,2,51,1,4,1,2,1),_Gel2esw10gIpv4CurrentDHCPClient_Type())
gel2esw10gIpv4CurrentDHCPClient.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIpv4CurrentDHCPClient.setStatus(_A)
_Gel2esw10gIPv4CurrentAddress_Type=IpAddress
_Gel2esw10gIPv4CurrentAddress_Object=MibScalar
gel2esw10gIPv4CurrentAddress=_Gel2esw10gIPv4CurrentAddress_Object((1,3,6,1,4,1,5205,2,51,1,4,1,2,2),_Gel2esw10gIPv4CurrentAddress_Type())
gel2esw10gIPv4CurrentAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gIPv4CurrentAddress.setStatus(_A)
_Gel2esw10gIPv4CurrentMask_Type=IpAddress
_Gel2esw10gIPv4CurrentMask_Object=MibScalar
gel2esw10gIPv4CurrentMask=_Gel2esw10gIPv4CurrentMask_Object((1,3,6,1,4,1,5205,2,51,1,4,1,2,3),_Gel2esw10gIPv4CurrentMask_Type())
gel2esw10gIPv4CurrentMask.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gIPv4CurrentMask.setStatus(_A)
_Gel2esw10gIPv4CurrentRouter_Type=IpAddress
_Gel2esw10gIPv4CurrentRouter_Object=MibScalar
gel2esw10gIPv4CurrentRouter=_Gel2esw10gIPv4CurrentRouter_Object((1,3,6,1,4,1,5205,2,51,1,4,1,2,4),_Gel2esw10gIPv4CurrentRouter_Type())
gel2esw10gIPv4CurrentRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gIPv4CurrentRouter.setStatus(_A)
class _Gel2esw10gIPv4CurrentVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw10gIPv4CurrentVLANId_Type.__name__=_C
_Gel2esw10gIPv4CurrentVLANId_Object=MibScalar
gel2esw10gIPv4CurrentVLANId=_Gel2esw10gIPv4CurrentVLANId_Object((1,3,6,1,4,1,5205,2,51,1,4,1,2,5),_Gel2esw10gIPv4CurrentVLANId_Type())
gel2esw10gIPv4CurrentVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gIPv4CurrentVLANId.setStatus(_A)
_Gel2esw10gIPv4CurrentDNSServer_Type=IpAddress
_Gel2esw10gIPv4CurrentDNSServer_Object=MibScalar
gel2esw10gIPv4CurrentDNSServer=_Gel2esw10gIPv4CurrentDNSServer_Object((1,3,6,1,4,1,5205,2,51,1,4,1,2,6),_Gel2esw10gIPv4CurrentDNSServer_Type())
gel2esw10gIPv4CurrentDNSServer.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gIPv4CurrentDNSServer.setStatus(_A)
_Gel2esw10gIPv6_ObjectIdentity=ObjectIdentity
gel2esw10gIPv6=_Gel2esw10gIPv6_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,4,2))
_Gel2esw10gIPv6Configured_ObjectIdentity=ObjectIdentity
gel2esw10gIPv6Configured=_Gel2esw10gIPv6Configured_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,4,2,1))
class _Gel2esw10gIpv6AutoConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gIpv6AutoConfiguration_Type.__name__=_C
_Gel2esw10gIpv6AutoConfiguration_Object=MibScalar
gel2esw10gIpv6AutoConfiguration=_Gel2esw10gIpv6AutoConfiguration_Object((1,3,6,1,4,1,5205,2,51,1,4,2,1,1),_Gel2esw10gIpv6AutoConfiguration_Type())
gel2esw10gIpv6AutoConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIpv6AutoConfiguration.setStatus(_A)
class _Gel2esw10gIpv6Address_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Gel2esw10gIpv6Address_Type.__name__=_G
_Gel2esw10gIpv6Address_Object=MibScalar
gel2esw10gIpv6Address=_Gel2esw10gIpv6Address_Object((1,3,6,1,4,1,5205,2,51,1,4,2,1,2),_Gel2esw10gIpv6Address_Type())
gel2esw10gIpv6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIpv6Address.setStatus(_A)
class _Gel2esw10gIpv6Prefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Gel2esw10gIpv6Prefix_Type.__name__=_C
_Gel2esw10gIpv6Prefix_Object=MibScalar
gel2esw10gIpv6Prefix=_Gel2esw10gIpv6Prefix_Object((1,3,6,1,4,1,5205,2,51,1,4,2,1,3),_Gel2esw10gIpv6Prefix_Type())
gel2esw10gIpv6Prefix.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIpv6Prefix.setStatus(_A)
class _Gel2esw10gIpv6Router_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Gel2esw10gIpv6Router_Type.__name__=_G
_Gel2esw10gIpv6Router_Object=MibScalar
gel2esw10gIpv6Router=_Gel2esw10gIpv6Router_Object((1,3,6,1,4,1,5205,2,51,1,4,2,1,4),_Gel2esw10gIpv6Router_Type())
gel2esw10gIpv6Router.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIpv6Router.setStatus(_A)
_Gel2esw10gIPv6Current_ObjectIdentity=ObjectIdentity
gel2esw10gIPv6Current=_Gel2esw10gIPv6Current_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,4,2,2))
class _Gel2esw10gIpv6CurrentAutoConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gIpv6CurrentAutoConfiguration_Type.__name__=_C
_Gel2esw10gIpv6CurrentAutoConfiguration_Object=MibScalar
gel2esw10gIpv6CurrentAutoConfiguration=_Gel2esw10gIpv6CurrentAutoConfiguration_Object((1,3,6,1,4,1,5205,2,51,1,4,2,2,1),_Gel2esw10gIpv6CurrentAutoConfiguration_Type())
gel2esw10gIpv6CurrentAutoConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gIpv6CurrentAutoConfiguration.setStatus(_A)
class _Gel2esw10gIpv6CurrentAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Gel2esw10gIpv6CurrentAddress_Type.__name__=_G
_Gel2esw10gIpv6CurrentAddress_Object=MibScalar
gel2esw10gIpv6CurrentAddress=_Gel2esw10gIpv6CurrentAddress_Object((1,3,6,1,4,1,5205,2,51,1,4,2,2,2),_Gel2esw10gIpv6CurrentAddress_Type())
gel2esw10gIpv6CurrentAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gIpv6CurrentAddress.setStatus(_A)
class _Gel2esw10gIpv6CurrentLinkLocalAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Gel2esw10gIpv6CurrentLinkLocalAddress_Type.__name__=_G
_Gel2esw10gIpv6CurrentLinkLocalAddress_Object=MibScalar
gel2esw10gIpv6CurrentLinkLocalAddress=_Gel2esw10gIpv6CurrentLinkLocalAddress_Object((1,3,6,1,4,1,5205,2,51,1,4,2,2,3),_Gel2esw10gIpv6CurrentLinkLocalAddress_Type())
gel2esw10gIpv6CurrentLinkLocalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gIpv6CurrentLinkLocalAddress.setStatus(_A)
class _Gel2esw10gIpv6CurrentPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Gel2esw10gIpv6CurrentPrefix_Type.__name__=_C
_Gel2esw10gIpv6CurrentPrefix_Object=MibScalar
gel2esw10gIpv6CurrentPrefix=_Gel2esw10gIpv6CurrentPrefix_Object((1,3,6,1,4,1,5205,2,51,1,4,2,2,4),_Gel2esw10gIpv6CurrentPrefix_Type())
gel2esw10gIpv6CurrentPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gIpv6CurrentPrefix.setStatus(_A)
class _Gel2esw10gIpv6CurrentRouter_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Gel2esw10gIpv6CurrentRouter_Type.__name__=_G
_Gel2esw10gIpv6CurrentRouter_Object=MibScalar
gel2esw10gIpv6CurrentRouter=_Gel2esw10gIpv6CurrentRouter_Object((1,3,6,1,4,1,5205,2,51,1,4,2,2,5),_Gel2esw10gIpv6CurrentRouter_Type())
gel2esw10gIpv6CurrentRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gIpv6CurrentRouter.setStatus(_A)
_Gel2esw10gSyslog_ObjectIdentity=ObjectIdentity
gel2esw10gSyslog=_Gel2esw10gSyslog_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,5))
_Gel2esw10gSyslogConf_ObjectIdentity=ObjectIdentity
gel2esw10gSyslogConf=_Gel2esw10gSyslogConf_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,5,1))
class _Gel2esw10gServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gServerMode_Type.__name__=_C
_Gel2esw10gServerMode_Object=MibScalar
gel2esw10gServerMode=_Gel2esw10gServerMode_Object((1,3,6,1,4,1,5205,2,51,1,5,1,1),_Gel2esw10gServerMode_Type())
gel2esw10gServerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gServerMode.setStatus(_A)
_Gel2esw10gServerAddress1_Type=IpAddress
_Gel2esw10gServerAddress1_Object=MibScalar
gel2esw10gServerAddress1=_Gel2esw10gServerAddress1_Object((1,3,6,1,4,1,5205,2,51,1,5,1,2),_Gel2esw10gServerAddress1_Type())
gel2esw10gServerAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gServerAddress1.setStatus(_A)
_Gel2esw10gServerAddress2_Type=IpAddress
_Gel2esw10gServerAddress2_Object=MibScalar
gel2esw10gServerAddress2=_Gel2esw10gServerAddress2_Object((1,3,6,1,4,1,5205,2,51,1,5,1,3),_Gel2esw10gServerAddress2_Type())
gel2esw10gServerAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gServerAddress2.setStatus(_A)
class _Gel2esw10gSyslogLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gSyslogLevel_Type.__name__=_C
_Gel2esw10gSyslogLevel_Object=MibScalar
gel2esw10gSyslogLevel=_Gel2esw10gSyslogLevel_Object((1,3,6,1,4,1,5205,2,51,1,5,1,4),_Gel2esw10gSyslogLevel_Type())
gel2esw10gSyslogLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSyslogLevel.setStatus(_A)
_Gel2esw10gSyslogDetailedInfo_ObjectIdentity=ObjectIdentity
gel2esw10gSyslogDetailedInfo=_Gel2esw10gSyslogDetailedInfo_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,5,2))
class _Gel2esw10gSyslogDetailedInfoClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gSyslogDetailedInfoClear_Type.__name__=_C
_Gel2esw10gSyslogDetailedInfoClear_Object=MibScalar
gel2esw10gSyslogDetailedInfoClear=_Gel2esw10gSyslogDetailedInfoClear_Object((1,3,6,1,4,1,5205,2,51,1,5,2,1),_Gel2esw10gSyslogDetailedInfoClear_Type())
gel2esw10gSyslogDetailedInfoClear.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSyslogDetailedInfoClear.setStatus(_A)
_Gel2esw10gSyslogDetailedInfoTable_Object=MibTable
gel2esw10gSyslogDetailedInfoTable=_Gel2esw10gSyslogDetailedInfoTable_Object((1,3,6,1,4,1,5205,2,51,1,5,2,2))
if mibBuilder.loadTexts:gel2esw10gSyslogDetailedInfoTable.setStatus(_A)
_Gel2esw10gSyslogDetailedInfoEntry_Object=MibTableRow
gel2esw10gSyslogDetailedInfoEntry=_Gel2esw10gSyslogDetailedInfoEntry_Object((1,3,6,1,4,1,5205,2,51,1,5,2,2,1))
gel2esw10gSyslogDetailedInfoEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:gel2esw10gSyslogDetailedInfoEntry.setStatus(_A)
class _Gel2esw10gSyslogDetailedInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Gel2esw10gSyslogDetailedInfoIndex_Type.__name__=_C
_Gel2esw10gSyslogDetailedInfoIndex_Object=MibTableColumn
gel2esw10gSyslogDetailedInfoIndex=_Gel2esw10gSyslogDetailedInfoIndex_Object((1,3,6,1,4,1,5205,2,51,1,5,2,2,1,1),_Gel2esw10gSyslogDetailedInfoIndex_Type())
gel2esw10gSyslogDetailedInfoIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gSyslogDetailedInfoIndex.setStatus(_A)
_Gel2esw10gSyslogDetailedInfoLevel_Type=DisplayString
_Gel2esw10gSyslogDetailedInfoLevel_Object=MibTableColumn
gel2esw10gSyslogDetailedInfoLevel=_Gel2esw10gSyslogDetailedInfoLevel_Object((1,3,6,1,4,1,5205,2,51,1,5,2,2,1,2),_Gel2esw10gSyslogDetailedInfoLevel_Type())
gel2esw10gSyslogDetailedInfoLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSyslogDetailedInfoLevel.setStatus(_A)
class _Gel2esw10gSyslogDetailedInfoTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_Gel2esw10gSyslogDetailedInfoTime_Type.__name__=_G
_Gel2esw10gSyslogDetailedInfoTime_Object=MibTableColumn
gel2esw10gSyslogDetailedInfoTime=_Gel2esw10gSyslogDetailedInfoTime_Object((1,3,6,1,4,1,5205,2,51,1,5,2,2,1,3),_Gel2esw10gSyslogDetailedInfoTime_Type())
gel2esw10gSyslogDetailedInfoTime.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSyslogDetailedInfoTime.setStatus(_A)
_Gel2esw10gSyslogDetailedInfoMessage_Type=DisplayString
_Gel2esw10gSyslogDetailedInfoMessage_Object=MibTableColumn
gel2esw10gSyslogDetailedInfoMessage=_Gel2esw10gSyslogDetailedInfoMessage_Object((1,3,6,1,4,1,5205,2,51,1,5,2,2,1,4),_Gel2esw10gSyslogDetailedInfoMessage_Type())
gel2esw10gSyslogDetailedInfoMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSyslogDetailedInfoMessage.setStatus(_A)
_Gel2esw10gSnmp_ObjectIdentity=ObjectIdentity
gel2esw10gSnmp=_Gel2esw10gSnmp_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,6))
_Gel2esw10gSnmpConf_ObjectIdentity=ObjectIdentity
gel2esw10gSnmpConf=_Gel2esw10gSnmpConf_ObjectIdentity((1,3,6,1,4,1,5205,2,51,1,6,1))
_Gel2esw10gGetCommunity_Type=DisplayString
_Gel2esw10gGetCommunity_Object=MibScalar
gel2esw10gGetCommunity=_Gel2esw10gGetCommunity_Object((1,3,6,1,4,1,5205,2,51,1,6,1,1),_Gel2esw10gGetCommunity_Type())
gel2esw10gGetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gGetCommunity.setStatus(_A)
class _Gel2esw10gSetCommunityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gSetCommunityMode_Type.__name__=_C
_Gel2esw10gSetCommunityMode_Object=MibScalar
gel2esw10gSetCommunityMode=_Gel2esw10gSetCommunityMode_Object((1,3,6,1,4,1,5205,2,51,1,6,1,2),_Gel2esw10gSetCommunityMode_Type())
gel2esw10gSetCommunityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSetCommunityMode.setStatus(_A)
_Gel2esw10gSetCommunity_Type=DisplayString
_Gel2esw10gSetCommunity_Object=MibScalar
gel2esw10gSetCommunity=_Gel2esw10gSetCommunity_Object((1,3,6,1,4,1,5205,2,51,1,6,1,3),_Gel2esw10gSetCommunity_Type())
gel2esw10gSetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSetCommunity.setStatus(_A)
_Gel2esw10gTrapHostConfTable_Object=MibTable
gel2esw10gTrapHostConfTable=_Gel2esw10gTrapHostConfTable_Object((1,3,6,1,4,1,5205,2,51,1,6,1,4))
if mibBuilder.loadTexts:gel2esw10gTrapHostConfTable.setStatus(_A)
_Gel2esw10gTrapHostConfEntry_Object=MibTableRow
gel2esw10gTrapHostConfEntry=_Gel2esw10gTrapHostConfEntry_Object((1,3,6,1,4,1,5205,2,51,1,6,1,4,1))
gel2esw10gTrapHostConfEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:gel2esw10gTrapHostConfEntry.setStatus(_A)
class _Gel2esw10gTrapHostConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Gel2esw10gTrapHostConfIndex_Type.__name__=_C
_Gel2esw10gTrapHostConfIndex_Object=MibTableColumn
gel2esw10gTrapHostConfIndex=_Gel2esw10gTrapHostConfIndex_Object((1,3,6,1,4,1,5205,2,51,1,6,1,4,1,1),_Gel2esw10gTrapHostConfIndex_Type())
gel2esw10gTrapHostConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gTrapHostConfIndex.setStatus(_A)
class _Gel2esw10gTrapHostConfVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,3))
_Gel2esw10gTrapHostConfVersion_Type.__name__=_C
_Gel2esw10gTrapHostConfVersion_Object=MibTableColumn
gel2esw10gTrapHostConfVersion=_Gel2esw10gTrapHostConfVersion_Object((1,3,6,1,4,1,5205,2,51,1,6,1,4,1,2),_Gel2esw10gTrapHostConfVersion_Type())
gel2esw10gTrapHostConfVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapHostConfVersion.setStatus(_A)
class _Gel2esw10gTrapHostConfIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,4),ValueRangeConstraint(6,6))
_Gel2esw10gTrapHostConfIPType_Type.__name__=_C
_Gel2esw10gTrapHostConfIPType_Object=MibTableColumn
gel2esw10gTrapHostConfIPType=_Gel2esw10gTrapHostConfIPType_Object((1,3,6,1,4,1,5205,2,51,1,6,1,4,1,3),_Gel2esw10gTrapHostConfIPType_Type())
gel2esw10gTrapHostConfIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapHostConfIPType.setStatus(_A)
_Gel2esw10gTrapHostConfIP_Type=DisplayString
_Gel2esw10gTrapHostConfIP_Object=MibTableColumn
gel2esw10gTrapHostConfIP=_Gel2esw10gTrapHostConfIP_Object((1,3,6,1,4,1,5205,2,51,1,6,1,4,1,4),_Gel2esw10gTrapHostConfIP_Type())
gel2esw10gTrapHostConfIP.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapHostConfIP.setStatus(_A)
class _Gel2esw10gTrapHostConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Gel2esw10gTrapHostConfPort_Type.__name__=_C
_Gel2esw10gTrapHostConfPort_Object=MibTableColumn
gel2esw10gTrapHostConfPort=_Gel2esw10gTrapHostConfPort_Object((1,3,6,1,4,1,5205,2,51,1,6,1,4,1,5),_Gel2esw10gTrapHostConfPort_Type())
gel2esw10gTrapHostConfPort.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapHostConfPort.setStatus(_A)
class _Gel2esw10gTrapHostConfCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Gel2esw10gTrapHostConfCommunity_Type.__name__=_G
_Gel2esw10gTrapHostConfCommunity_Object=MibTableColumn
gel2esw10gTrapHostConfCommunity=_Gel2esw10gTrapHostConfCommunity_Object((1,3,6,1,4,1,5205,2,51,1,6,1,4,1,6),_Gel2esw10gTrapHostConfCommunity_Type())
gel2esw10gTrapHostConfCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapHostConfCommunity.setStatus(_A)
class _Gel2esw10gTrapHostConfSeverityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapHostConfSeverityLevel_Type.__name__=_C
_Gel2esw10gTrapHostConfSeverityLevel_Object=MibTableColumn
gel2esw10gTrapHostConfSeverityLevel=_Gel2esw10gTrapHostConfSeverityLevel_Object((1,3,6,1,4,1,5205,2,51,1,6,1,4,1,7),_Gel2esw10gTrapHostConfSeverityLevel_Type())
gel2esw10gTrapHostConfSeverityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapHostConfSeverityLevel.setStatus(_A)
class _Gel2esw10gTrapHostConfSecurityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Gel2esw10gTrapHostConfSecurityLevel_Type.__name__=_C
_Gel2esw10gTrapHostConfSecurityLevel_Object=MibTableColumn
gel2esw10gTrapHostConfSecurityLevel=_Gel2esw10gTrapHostConfSecurityLevel_Object((1,3,6,1,4,1,5205,2,51,1,6,1,4,1,8),_Gel2esw10gTrapHostConfSecurityLevel_Type())
gel2esw10gTrapHostConfSecurityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapHostConfSecurityLevel.setStatus(_A)
class _Gel2esw10gTrapHostConfAuthPtc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Gel2esw10gTrapHostConfAuthPtc_Type.__name__=_C
_Gel2esw10gTrapHostConfAuthPtc_Object=MibTableColumn
gel2esw10gTrapHostConfAuthPtc=_Gel2esw10gTrapHostConfAuthPtc_Object((1,3,6,1,4,1,5205,2,51,1,6,1,4,1,9),_Gel2esw10gTrapHostConfAuthPtc_Type())
gel2esw10gTrapHostConfAuthPtc.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapHostConfAuthPtc.setStatus(_A)
_Gel2esw10gTrapHostConfAuthPassword_Type=DisplayString
_Gel2esw10gTrapHostConfAuthPassword_Object=MibTableColumn
gel2esw10gTrapHostConfAuthPassword=_Gel2esw10gTrapHostConfAuthPassword_Object((1,3,6,1,4,1,5205,2,51,1,6,1,4,1,10),_Gel2esw10gTrapHostConfAuthPassword_Type())
gel2esw10gTrapHostConfAuthPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapHostConfAuthPassword.setStatus(_A)
class _Gel2esw10gTrapHostConfPrivPtc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Gel2esw10gTrapHostConfPrivPtc_Type.__name__=_C
_Gel2esw10gTrapHostConfPrivPtc_Object=MibTableColumn
gel2esw10gTrapHostConfPrivPtc=_Gel2esw10gTrapHostConfPrivPtc_Object((1,3,6,1,4,1,5205,2,51,1,6,1,4,1,11),_Gel2esw10gTrapHostConfPrivPtc_Type())
gel2esw10gTrapHostConfPrivPtc.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapHostConfPrivPtc.setStatus(_A)
_Gel2esw10gTrapHostConfPrivPassword_Type=DisplayString
_Gel2esw10gTrapHostConfPrivPassword_Object=MibTableColumn
gel2esw10gTrapHostConfPrivPassword=_Gel2esw10gTrapHostConfPrivPassword_Object((1,3,6,1,4,1,5205,2,51,1,6,1,4,1,12),_Gel2esw10gTrapHostConfPrivPassword_Type())
gel2esw10gTrapHostConfPrivPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapHostConfPrivPassword.setStatus(_A)
class _Gel2esw10gTrapHostConfCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gTrapHostConfCurrentMode_Type.__name__=_C
_Gel2esw10gTrapHostConfCurrentMode_Object=MibTableColumn
gel2esw10gTrapHostConfCurrentMode=_Gel2esw10gTrapHostConfCurrentMode_Object((1,3,6,1,4,1,5205,2,51,1,6,1,4,1,13),_Gel2esw10gTrapHostConfCurrentMode_Type())
gel2esw10gTrapHostConfCurrentMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapHostConfCurrentMode.setStatus(_A)
_Gel2esw10gConfiguration_ObjectIdentity=ObjectIdentity
gel2esw10gConfiguration=_Gel2esw10gConfiguration_ObjectIdentity((1,3,6,1,4,1,5205,2,51,2))
_Gel2esw10gPort_ObjectIdentity=ObjectIdentity
gel2esw10gPort=_Gel2esw10gPort_ObjectIdentity((1,3,6,1,4,1,5205,2,51,2,1))
_Gel2esw10gPortConfigurationTable_Object=MibTable
gel2esw10gPortConfigurationTable=_Gel2esw10gPortConfigurationTable_Object((1,3,6,1,4,1,5205,2,51,2,1,1))
if mibBuilder.loadTexts:gel2esw10gPortConfigurationTable.setStatus(_A)
_Gel2esw10gPortConfigurationEntry_Object=MibTableRow
gel2esw10gPortConfigurationEntry=_Gel2esw10gPortConfigurationEntry_Object((1,3,6,1,4,1,5205,2,51,2,1,1,1))
gel2esw10gPortConfigurationEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:gel2esw10gPortConfigurationEntry.setStatus(_A)
class _Gel2esw10gPortConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gPortConfPort_Type.__name__=_C
_Gel2esw10gPortConfPort_Object=MibTableColumn
gel2esw10gPortConfPort=_Gel2esw10gPortConfPort_Object((1,3,6,1,4,1,5205,2,51,2,1,1,1,1),_Gel2esw10gPortConfPort_Type())
gel2esw10gPortConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gPortConfPort.setStatus(_A)
class _Gel2esw10gPortConfPortMedia_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_Gel2esw10gPortConfPortMedia_Type.__name__=_G
_Gel2esw10gPortConfPortMedia_Object=MibTableColumn
gel2esw10gPortConfPortMedia=_Gel2esw10gPortConfPortMedia_Object((1,3,6,1,4,1,5205,2,51,2,1,1,1,2),_Gel2esw10gPortConfPortMedia_Type())
gel2esw10gPortConfPortMedia.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortConfPortMedia.setStatus(_A)
class _Gel2esw10gPortConfLink_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,4))
_Gel2esw10gPortConfLink_Type.__name__=_G
_Gel2esw10gPortConfLink_Object=MibTableColumn
gel2esw10gPortConfLink=_Gel2esw10gPortConfLink_Object((1,3,6,1,4,1,5205,2,51,2,1,1,1,3),_Gel2esw10gPortConfLink_Type())
gel2esw10gPortConfLink.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortConfLink.setStatus(_A)
class _Gel2esw10gPortConfCurrentSpeed_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,12))
_Gel2esw10gPortConfCurrentSpeed_Type.__name__=_G
_Gel2esw10gPortConfCurrentSpeed_Object=MibTableColumn
gel2esw10gPortConfCurrentSpeed=_Gel2esw10gPortConfCurrentSpeed_Object((1,3,6,1,4,1,5205,2,51,2,1,1,1,4),_Gel2esw10gPortConfCurrentSpeed_Type())
gel2esw10gPortConfCurrentSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortConfCurrentSpeed.setStatus(_A)
class _Gel2esw10gPortConfSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_Gel2esw10gPortConfSpeed_Type.__name__=_C
_Gel2esw10gPortConfSpeed_Object=MibTableColumn
gel2esw10gPortConfSpeed=_Gel2esw10gPortConfSpeed_Object((1,3,6,1,4,1,5205,2,51,2,1,1,1,5),_Gel2esw10gPortConfSpeed_Type())
gel2esw10gPortConfSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortConfSpeed.setStatus(_A)
class _Gel2esw10gPortConfCurrentFlowControlRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortConfCurrentFlowControlRx_Type.__name__=_C
_Gel2esw10gPortConfCurrentFlowControlRx_Object=MibTableColumn
gel2esw10gPortConfCurrentFlowControlRx=_Gel2esw10gPortConfCurrentFlowControlRx_Object((1,3,6,1,4,1,5205,2,51,2,1,1,1,6),_Gel2esw10gPortConfCurrentFlowControlRx_Type())
gel2esw10gPortConfCurrentFlowControlRx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortConfCurrentFlowControlRx.setStatus(_A)
class _Gel2esw10gPortConfCurrentFlowControlTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortConfCurrentFlowControlTx_Type.__name__=_C
_Gel2esw10gPortConfCurrentFlowControlTx_Object=MibTableColumn
gel2esw10gPortConfCurrentFlowControlTx=_Gel2esw10gPortConfCurrentFlowControlTx_Object((1,3,6,1,4,1,5205,2,51,2,1,1,1,7),_Gel2esw10gPortConfCurrentFlowControlTx_Type())
gel2esw10gPortConfCurrentFlowControlTx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortConfCurrentFlowControlTx.setStatus(_A)
class _Gel2esw10gPortConfFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortConfFlowControl_Type.__name__=_C
_Gel2esw10gPortConfFlowControl_Object=MibTableColumn
gel2esw10gPortConfFlowControl=_Gel2esw10gPortConfFlowControl_Object((1,3,6,1,4,1,5205,2,51,2,1,1,1,8),_Gel2esw10gPortConfFlowControl_Type())
gel2esw10gPortConfFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortConfFlowControl.setStatus(_A)
class _Gel2esw10gPortConfMaxFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1518,9600))
_Gel2esw10gPortConfMaxFrameSize_Type.__name__=_C
_Gel2esw10gPortConfMaxFrameSize_Object=MibTableColumn
gel2esw10gPortConfMaxFrameSize=_Gel2esw10gPortConfMaxFrameSize_Object((1,3,6,1,4,1,5205,2,51,2,1,1,1,9),_Gel2esw10gPortConfMaxFrameSize_Type())
gel2esw10gPortConfMaxFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortConfMaxFrameSize.setStatus(_A)
class _Gel2esw10gPortConfExcessiveCollisionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortConfExcessiveCollisionMode_Type.__name__=_C
_Gel2esw10gPortConfExcessiveCollisionMode_Object=MibTableColumn
gel2esw10gPortConfExcessiveCollisionMode=_Gel2esw10gPortConfExcessiveCollisionMode_Object((1,3,6,1,4,1,5205,2,51,2,1,1,1,10),_Gel2esw10gPortConfExcessiveCollisionMode_Type())
gel2esw10gPortConfExcessiveCollisionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortConfExcessiveCollisionMode.setStatus(_A)
class _Gel2esw10gPortConfPowerControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw10gPortConfPowerControl_Type.__name__=_C
_Gel2esw10gPortConfPowerControl_Object=MibTableColumn
gel2esw10gPortConfPowerControl=_Gel2esw10gPortConfPowerControl_Object((1,3,6,1,4,1,5205,2,51,2,1,1,1,11),_Gel2esw10gPortConfPowerControl_Type())
gel2esw10gPortConfPowerControl.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortConfPowerControl.setStatus(_A)
_Gel2esw10gPortConfDescription_Type=DisplayString
_Gel2esw10gPortConfDescription_Object=MibTableColumn
gel2esw10gPortConfDescription=_Gel2esw10gPortConfDescription_Object((1,3,6,1,4,1,5205,2,51,2,1,1,1,12),_Gel2esw10gPortConfDescription_Type())
gel2esw10gPortConfDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortConfDescription.setStatus(_A)
_Gel2esw10gPortTrafficStatisticsTable_Object=MibTable
gel2esw10gPortTrafficStatisticsTable=_Gel2esw10gPortTrafficStatisticsTable_Object((1,3,6,1,4,1,5205,2,51,2,1,2))
if mibBuilder.loadTexts:gel2esw10gPortTrafficStatisticsTable.setStatus(_A)
_Gel2esw10gPortTrafficStatisticsEntry_Object=MibTableRow
gel2esw10gPortTrafficStatisticsEntry=_Gel2esw10gPortTrafficStatisticsEntry_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1))
gel2esw10gPortTrafficStatisticsEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:gel2esw10gPortTrafficStatisticsEntry.setStatus(_A)
class _Gel2esw10gPortTrafficStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gPortTrafficStatisticsPort_Type.__name__=_C
_Gel2esw10gPortTrafficStatisticsPort_Object=MibTableColumn
gel2esw10gPortTrafficStatisticsPort=_Gel2esw10gPortTrafficStatisticsPort_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,1),_Gel2esw10gPortTrafficStatisticsPort_Type())
gel2esw10gPortTrafficStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gPortTrafficStatisticsPort.setStatus(_A)
class _Gel2esw10gPortTrafficStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortTrafficStatisticsClear_Type.__name__=_C
_Gel2esw10gPortTrafficStatisticsClear_Object=MibTableColumn
gel2esw10gPortTrafficStatisticsClear=_Gel2esw10gPortTrafficStatisticsClear_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,2),_Gel2esw10gPortTrafficStatisticsClear_Type())
gel2esw10gPortTrafficStatisticsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortTrafficStatisticsClear.setStatus(_A)
_Gel2esw10gPortTrafficRxPackets_Type=Counter64
_Gel2esw10gPortTrafficRxPackets_Object=MibTableColumn
gel2esw10gPortTrafficRxPackets=_Gel2esw10gPortTrafficRxPackets_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,3),_Gel2esw10gPortTrafficRxPackets_Type())
gel2esw10gPortTrafficRxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxPackets.setStatus(_A)
_Gel2esw10gPortTrafficRxOctets_Type=Counter64
_Gel2esw10gPortTrafficRxOctets_Object=MibTableColumn
gel2esw10gPortTrafficRxOctets=_Gel2esw10gPortTrafficRxOctets_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,4),_Gel2esw10gPortTrafficRxOctets_Type())
gel2esw10gPortTrafficRxOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxOctets.setStatus(_A)
_Gel2esw10gPortTrafficRxUnicast_Type=Counter64
_Gel2esw10gPortTrafficRxUnicast_Object=MibTableColumn
gel2esw10gPortTrafficRxUnicast=_Gel2esw10gPortTrafficRxUnicast_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,5),_Gel2esw10gPortTrafficRxUnicast_Type())
gel2esw10gPortTrafficRxUnicast.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxUnicast.setStatus(_A)
_Gel2esw10gPortTrafficRxMulticast_Type=Counter64
_Gel2esw10gPortTrafficRxMulticast_Object=MibTableColumn
gel2esw10gPortTrafficRxMulticast=_Gel2esw10gPortTrafficRxMulticast_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,6),_Gel2esw10gPortTrafficRxMulticast_Type())
gel2esw10gPortTrafficRxMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxMulticast.setStatus(_A)
_Gel2esw10gPortTrafficRxBroadcast_Type=Counter64
_Gel2esw10gPortTrafficRxBroadcast_Object=MibTableColumn
gel2esw10gPortTrafficRxBroadcast=_Gel2esw10gPortTrafficRxBroadcast_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,7),_Gel2esw10gPortTrafficRxBroadcast_Type())
gel2esw10gPortTrafficRxBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxBroadcast.setStatus(_A)
_Gel2esw10gPortTrafficRxPause_Type=Counter64
_Gel2esw10gPortTrafficRxPause_Object=MibTableColumn
gel2esw10gPortTrafficRxPause=_Gel2esw10gPortTrafficRxPause_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,8),_Gel2esw10gPortTrafficRxPause_Type())
gel2esw10gPortTrafficRxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxPause.setStatus(_A)
_Gel2esw10gPortTrafficRx64Bytes_Type=Counter64
_Gel2esw10gPortTrafficRx64Bytes_Object=MibTableColumn
gel2esw10gPortTrafficRx64Bytes=_Gel2esw10gPortTrafficRx64Bytes_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,9),_Gel2esw10gPortTrafficRx64Bytes_Type())
gel2esw10gPortTrafficRx64Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRx64Bytes.setStatus(_A)
_Gel2esw10gPortTrafficRx65to127Bytes_Type=Counter64
_Gel2esw10gPortTrafficRx65to127Bytes_Object=MibTableColumn
gel2esw10gPortTrafficRx65to127Bytes=_Gel2esw10gPortTrafficRx65to127Bytes_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,10),_Gel2esw10gPortTrafficRx65to127Bytes_Type())
gel2esw10gPortTrafficRx65to127Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRx65to127Bytes.setStatus(_A)
_Gel2esw10gPortTrafficRx128to255Bytes_Type=Counter64
_Gel2esw10gPortTrafficRx128to255Bytes_Object=MibTableColumn
gel2esw10gPortTrafficRx128to255Bytes=_Gel2esw10gPortTrafficRx128to255Bytes_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,11),_Gel2esw10gPortTrafficRx128to255Bytes_Type())
gel2esw10gPortTrafficRx128to255Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRx128to255Bytes.setStatus(_A)
_Gel2esw10gPortTrafficRx256to511Bytes_Type=Counter64
_Gel2esw10gPortTrafficRx256to511Bytes_Object=MibTableColumn
gel2esw10gPortTrafficRx256to511Bytes=_Gel2esw10gPortTrafficRx256to511Bytes_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,12),_Gel2esw10gPortTrafficRx256to511Bytes_Type())
gel2esw10gPortTrafficRx256to511Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRx256to511Bytes.setStatus(_A)
_Gel2esw10gPortTrafficRx512to1023Bytes_Type=Counter64
_Gel2esw10gPortTrafficRx512to1023Bytes_Object=MibTableColumn
gel2esw10gPortTrafficRx512to1023Bytes=_Gel2esw10gPortTrafficRx512to1023Bytes_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,13),_Gel2esw10gPortTrafficRx512to1023Bytes_Type())
gel2esw10gPortTrafficRx512to1023Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRx512to1023Bytes.setStatus(_A)
_Gel2esw10gPortTrafficRx1024to1526Bytes_Type=Counter64
_Gel2esw10gPortTrafficRx1024to1526Bytes_Object=MibTableColumn
gel2esw10gPortTrafficRx1024to1526Bytes=_Gel2esw10gPortTrafficRx1024to1526Bytes_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,14),_Gel2esw10gPortTrafficRx1024to1526Bytes_Type())
gel2esw10gPortTrafficRx1024to1526Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRx1024to1526Bytes.setStatus(_A)
_Gel2esw10gPortTrafficRxExceecd1527Bytes_Type=Counter64
_Gel2esw10gPortTrafficRxExceecd1527Bytes_Object=MibTableColumn
gel2esw10gPortTrafficRxExceecd1527Bytes=_Gel2esw10gPortTrafficRxExceecd1527Bytes_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,15),_Gel2esw10gPortTrafficRxExceecd1527Bytes_Type())
gel2esw10gPortTrafficRxExceecd1527Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxExceecd1527Bytes.setStatus(_A)
_Gel2esw10gPortTrafficRxQ0_Type=Counter64
_Gel2esw10gPortTrafficRxQ0_Object=MibTableColumn
gel2esw10gPortTrafficRxQ0=_Gel2esw10gPortTrafficRxQ0_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,16),_Gel2esw10gPortTrafficRxQ0_Type())
gel2esw10gPortTrafficRxQ0.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxQ0.setStatus(_A)
_Gel2esw10gPortTrafficRxQ1_Type=Counter64
_Gel2esw10gPortTrafficRxQ1_Object=MibTableColumn
gel2esw10gPortTrafficRxQ1=_Gel2esw10gPortTrafficRxQ1_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,17),_Gel2esw10gPortTrafficRxQ1_Type())
gel2esw10gPortTrafficRxQ1.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxQ1.setStatus(_A)
_Gel2esw10gPortTrafficRxQ2_Type=Counter64
_Gel2esw10gPortTrafficRxQ2_Object=MibTableColumn
gel2esw10gPortTrafficRxQ2=_Gel2esw10gPortTrafficRxQ2_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,18),_Gel2esw10gPortTrafficRxQ2_Type())
gel2esw10gPortTrafficRxQ2.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxQ2.setStatus(_A)
_Gel2esw10gPortTrafficRxQ3_Type=Counter64
_Gel2esw10gPortTrafficRxQ3_Object=MibTableColumn
gel2esw10gPortTrafficRxQ3=_Gel2esw10gPortTrafficRxQ3_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,19),_Gel2esw10gPortTrafficRxQ3_Type())
gel2esw10gPortTrafficRxQ3.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxQ3.setStatus(_A)
_Gel2esw10gPortTrafficRxQ4_Type=Counter64
_Gel2esw10gPortTrafficRxQ4_Object=MibTableColumn
gel2esw10gPortTrafficRxQ4=_Gel2esw10gPortTrafficRxQ4_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,20),_Gel2esw10gPortTrafficRxQ4_Type())
gel2esw10gPortTrafficRxQ4.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxQ4.setStatus(_A)
_Gel2esw10gPortTrafficRxQ5_Type=Counter64
_Gel2esw10gPortTrafficRxQ5_Object=MibTableColumn
gel2esw10gPortTrafficRxQ5=_Gel2esw10gPortTrafficRxQ5_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,21),_Gel2esw10gPortTrafficRxQ5_Type())
gel2esw10gPortTrafficRxQ5.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxQ5.setStatus(_A)
_Gel2esw10gPortTrafficRxQ6_Type=Counter64
_Gel2esw10gPortTrafficRxQ6_Object=MibTableColumn
gel2esw10gPortTrafficRxQ6=_Gel2esw10gPortTrafficRxQ6_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,22),_Gel2esw10gPortTrafficRxQ6_Type())
gel2esw10gPortTrafficRxQ6.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxQ6.setStatus(_A)
_Gel2esw10gPortTrafficRxQ7_Type=Counter64
_Gel2esw10gPortTrafficRxQ7_Object=MibTableColumn
gel2esw10gPortTrafficRxQ7=_Gel2esw10gPortTrafficRxQ7_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,23),_Gel2esw10gPortTrafficRxQ7_Type())
gel2esw10gPortTrafficRxQ7.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxQ7.setStatus(_A)
_Gel2esw10gPortTrafficRxDrops_Type=Counter64
_Gel2esw10gPortTrafficRxDrops_Object=MibTableColumn
gel2esw10gPortTrafficRxDrops=_Gel2esw10gPortTrafficRxDrops_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,24),_Gel2esw10gPortTrafficRxDrops_Type())
gel2esw10gPortTrafficRxDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxDrops.setStatus(_A)
_Gel2esw10gPortTrafficRxCRCorAlignment_Type=Counter64
_Gel2esw10gPortTrafficRxCRCorAlignment_Object=MibTableColumn
gel2esw10gPortTrafficRxCRCorAlignment=_Gel2esw10gPortTrafficRxCRCorAlignment_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,25),_Gel2esw10gPortTrafficRxCRCorAlignment_Type())
gel2esw10gPortTrafficRxCRCorAlignment.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxCRCorAlignment.setStatus(_A)
_Gel2esw10gPortTrafficRxUndersize_Type=Counter64
_Gel2esw10gPortTrafficRxUndersize_Object=MibTableColumn
gel2esw10gPortTrafficRxUndersize=_Gel2esw10gPortTrafficRxUndersize_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,26),_Gel2esw10gPortTrafficRxUndersize_Type())
gel2esw10gPortTrafficRxUndersize.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxUndersize.setStatus(_A)
_Gel2esw10gPortTrafficRxOversize_Type=Counter64
_Gel2esw10gPortTrafficRxOversize_Object=MibTableColumn
gel2esw10gPortTrafficRxOversize=_Gel2esw10gPortTrafficRxOversize_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,27),_Gel2esw10gPortTrafficRxOversize_Type())
gel2esw10gPortTrafficRxOversize.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxOversize.setStatus(_A)
_Gel2esw10gPortTrafficRxFragments_Type=Counter64
_Gel2esw10gPortTrafficRxFragments_Object=MibTableColumn
gel2esw10gPortTrafficRxFragments=_Gel2esw10gPortTrafficRxFragments_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,28),_Gel2esw10gPortTrafficRxFragments_Type())
gel2esw10gPortTrafficRxFragments.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxFragments.setStatus(_A)
_Gel2esw10gPortTrafficRxJabber_Type=Counter64
_Gel2esw10gPortTrafficRxJabber_Object=MibTableColumn
gel2esw10gPortTrafficRxJabber=_Gel2esw10gPortTrafficRxJabber_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,29),_Gel2esw10gPortTrafficRxJabber_Type())
gel2esw10gPortTrafficRxJabber.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxJabber.setStatus(_A)
_Gel2esw10gPortTrafficRxFiltered_Type=Counter64
_Gel2esw10gPortTrafficRxFiltered_Object=MibTableColumn
gel2esw10gPortTrafficRxFiltered=_Gel2esw10gPortTrafficRxFiltered_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,30),_Gel2esw10gPortTrafficRxFiltered_Type())
gel2esw10gPortTrafficRxFiltered.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficRxFiltered.setStatus(_A)
_Gel2esw10gPortTrafficTxPackets_Type=Counter64
_Gel2esw10gPortTrafficTxPackets_Object=MibTableColumn
gel2esw10gPortTrafficTxPackets=_Gel2esw10gPortTrafficTxPackets_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,31),_Gel2esw10gPortTrafficTxPackets_Type())
gel2esw10gPortTrafficTxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxPackets.setStatus(_A)
_Gel2esw10gPortTrafficTxOctets_Type=Counter64
_Gel2esw10gPortTrafficTxOctets_Object=MibTableColumn
gel2esw10gPortTrafficTxOctets=_Gel2esw10gPortTrafficTxOctets_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,32),_Gel2esw10gPortTrafficTxOctets_Type())
gel2esw10gPortTrafficTxOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxOctets.setStatus(_A)
_Gel2esw10gPortTrafficTxUnicast_Type=Counter64
_Gel2esw10gPortTrafficTxUnicast_Object=MibTableColumn
gel2esw10gPortTrafficTxUnicast=_Gel2esw10gPortTrafficTxUnicast_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,33),_Gel2esw10gPortTrafficTxUnicast_Type())
gel2esw10gPortTrafficTxUnicast.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxUnicast.setStatus(_A)
_Gel2esw10gPortTrafficTxMulticast_Type=Counter64
_Gel2esw10gPortTrafficTxMulticast_Object=MibTableColumn
gel2esw10gPortTrafficTxMulticast=_Gel2esw10gPortTrafficTxMulticast_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,34),_Gel2esw10gPortTrafficTxMulticast_Type())
gel2esw10gPortTrafficTxMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxMulticast.setStatus(_A)
_Gel2esw10gPortTrafficTxBroadcast_Type=Counter64
_Gel2esw10gPortTrafficTxBroadcast_Object=MibTableColumn
gel2esw10gPortTrafficTxBroadcast=_Gel2esw10gPortTrafficTxBroadcast_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,35),_Gel2esw10gPortTrafficTxBroadcast_Type())
gel2esw10gPortTrafficTxBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxBroadcast.setStatus(_A)
_Gel2esw10gPortTrafficTxPause_Type=Counter64
_Gel2esw10gPortTrafficTxPause_Object=MibTableColumn
gel2esw10gPortTrafficTxPause=_Gel2esw10gPortTrafficTxPause_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,36),_Gel2esw10gPortTrafficTxPause_Type())
gel2esw10gPortTrafficTxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxPause.setStatus(_A)
_Gel2esw10gPortTrafficTx64Bytes_Type=Counter64
_Gel2esw10gPortTrafficTx64Bytes_Object=MibTableColumn
gel2esw10gPortTrafficTx64Bytes=_Gel2esw10gPortTrafficTx64Bytes_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,37),_Gel2esw10gPortTrafficTx64Bytes_Type())
gel2esw10gPortTrafficTx64Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTx64Bytes.setStatus(_A)
_Gel2esw10gPortTrafficTx65to127Bytes_Type=Counter64
_Gel2esw10gPortTrafficTx65to127Bytes_Object=MibTableColumn
gel2esw10gPortTrafficTx65to127Bytes=_Gel2esw10gPortTrafficTx65to127Bytes_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,38),_Gel2esw10gPortTrafficTx65to127Bytes_Type())
gel2esw10gPortTrafficTx65to127Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTx65to127Bytes.setStatus(_A)
_Gel2esw10gPortTrafficTx128to255Bytes_Type=Counter64
_Gel2esw10gPortTrafficTx128to255Bytes_Object=MibTableColumn
gel2esw10gPortTrafficTx128to255Bytes=_Gel2esw10gPortTrafficTx128to255Bytes_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,39),_Gel2esw10gPortTrafficTx128to255Bytes_Type())
gel2esw10gPortTrafficTx128to255Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTx128to255Bytes.setStatus(_A)
_Gel2esw10gPortTrafficTx256to511Bytes_Type=Counter64
_Gel2esw10gPortTrafficTx256to511Bytes_Object=MibTableColumn
gel2esw10gPortTrafficTx256to511Bytes=_Gel2esw10gPortTrafficTx256to511Bytes_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,40),_Gel2esw10gPortTrafficTx256to511Bytes_Type())
gel2esw10gPortTrafficTx256to511Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTx256to511Bytes.setStatus(_A)
_Gel2esw10gPortTrafficTx512to1023Bytes_Type=Counter64
_Gel2esw10gPortTrafficTx512to1023Bytes_Object=MibTableColumn
gel2esw10gPortTrafficTx512to1023Bytes=_Gel2esw10gPortTrafficTx512to1023Bytes_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,41),_Gel2esw10gPortTrafficTx512to1023Bytes_Type())
gel2esw10gPortTrafficTx512to1023Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTx512to1023Bytes.setStatus(_A)
_Gel2esw10gPortTrafficTx1024to1526Bytes_Type=Counter64
_Gel2esw10gPortTrafficTx1024to1526Bytes_Object=MibTableColumn
gel2esw10gPortTrafficTx1024to1526Bytes=_Gel2esw10gPortTrafficTx1024to1526Bytes_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,42),_Gel2esw10gPortTrafficTx1024to1526Bytes_Type())
gel2esw10gPortTrafficTx1024to1526Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTx1024to1526Bytes.setStatus(_A)
_Gel2esw10gPortTrafficTxExceecd1527Bytes_Type=Counter64
_Gel2esw10gPortTrafficTxExceecd1527Bytes_Object=MibTableColumn
gel2esw10gPortTrafficTxExceecd1527Bytes=_Gel2esw10gPortTrafficTxExceecd1527Bytes_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,43),_Gel2esw10gPortTrafficTxExceecd1527Bytes_Type())
gel2esw10gPortTrafficTxExceecd1527Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxExceecd1527Bytes.setStatus(_A)
_Gel2esw10gPortTrafficTxQ0_Type=Counter64
_Gel2esw10gPortTrafficTxQ0_Object=MibTableColumn
gel2esw10gPortTrafficTxQ0=_Gel2esw10gPortTrafficTxQ0_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,44),_Gel2esw10gPortTrafficTxQ0_Type())
gel2esw10gPortTrafficTxQ0.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxQ0.setStatus(_A)
_Gel2esw10gPortTrafficTxQ1_Type=Counter64
_Gel2esw10gPortTrafficTxQ1_Object=MibTableColumn
gel2esw10gPortTrafficTxQ1=_Gel2esw10gPortTrafficTxQ1_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,45),_Gel2esw10gPortTrafficTxQ1_Type())
gel2esw10gPortTrafficTxQ1.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxQ1.setStatus(_A)
_Gel2esw10gPortTrafficTxQ2_Type=Counter64
_Gel2esw10gPortTrafficTxQ2_Object=MibTableColumn
gel2esw10gPortTrafficTxQ2=_Gel2esw10gPortTrafficTxQ2_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,46),_Gel2esw10gPortTrafficTxQ2_Type())
gel2esw10gPortTrafficTxQ2.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxQ2.setStatus(_A)
_Gel2esw10gPortTrafficTxQ3_Type=Counter64
_Gel2esw10gPortTrafficTxQ3_Object=MibTableColumn
gel2esw10gPortTrafficTxQ3=_Gel2esw10gPortTrafficTxQ3_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,47),_Gel2esw10gPortTrafficTxQ3_Type())
gel2esw10gPortTrafficTxQ3.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxQ3.setStatus(_A)
_Gel2esw10gPortTrafficTxQ4_Type=Counter64
_Gel2esw10gPortTrafficTxQ4_Object=MibTableColumn
gel2esw10gPortTrafficTxQ4=_Gel2esw10gPortTrafficTxQ4_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,48),_Gel2esw10gPortTrafficTxQ4_Type())
gel2esw10gPortTrafficTxQ4.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxQ4.setStatus(_A)
_Gel2esw10gPortTrafficTxQ5_Type=Counter64
_Gel2esw10gPortTrafficTxQ5_Object=MibTableColumn
gel2esw10gPortTrafficTxQ5=_Gel2esw10gPortTrafficTxQ5_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,49),_Gel2esw10gPortTrafficTxQ5_Type())
gel2esw10gPortTrafficTxQ5.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxQ5.setStatus(_A)
_Gel2esw10gPortTrafficTxQ6_Type=Counter64
_Gel2esw10gPortTrafficTxQ6_Object=MibTableColumn
gel2esw10gPortTrafficTxQ6=_Gel2esw10gPortTrafficTxQ6_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,50),_Gel2esw10gPortTrafficTxQ6_Type())
gel2esw10gPortTrafficTxQ6.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxQ6.setStatus(_A)
_Gel2esw10gPortTrafficTxQ7_Type=Counter64
_Gel2esw10gPortTrafficTxQ7_Object=MibTableColumn
gel2esw10gPortTrafficTxQ7=_Gel2esw10gPortTrafficTxQ7_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,51),_Gel2esw10gPortTrafficTxQ7_Type())
gel2esw10gPortTrafficTxQ7.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxQ7.setStatus(_A)
_Gel2esw10gPortTrafficTxDrops_Type=Counter64
_Gel2esw10gPortTrafficTxDrops_Object=MibTableColumn
gel2esw10gPortTrafficTxDrops=_Gel2esw10gPortTrafficTxDrops_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,52),_Gel2esw10gPortTrafficTxDrops_Type())
gel2esw10gPortTrafficTxDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxDrops.setStatus(_A)
_Gel2esw10gPortTrafficTxLateOrExcColl_Type=Counter64
_Gel2esw10gPortTrafficTxLateOrExcColl_Object=MibTableColumn
gel2esw10gPortTrafficTxLateOrExcColl=_Gel2esw10gPortTrafficTxLateOrExcColl_Object((1,3,6,1,4,1,5205,2,51,2,1,2,1,53),_Gel2esw10gPortTrafficTxLateOrExcColl_Type())
gel2esw10gPortTrafficTxLateOrExcColl.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortTrafficTxLateOrExcColl.setStatus(_A)
_Gel2esw10gPortQoSStatistics_ObjectIdentity=ObjectIdentity
gel2esw10gPortQoSStatistics=_Gel2esw10gPortQoSStatistics_ObjectIdentity((1,3,6,1,4,1,5205,2,51,2,1,3))
class _Gel2esw10gPortQoSStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortQoSStatisticsClear_Type.__name__=_C
_Gel2esw10gPortQoSStatisticsClear_Object=MibScalar
gel2esw10gPortQoSStatisticsClear=_Gel2esw10gPortQoSStatisticsClear_Object((1,3,6,1,4,1,5205,2,51,2,1,3,1),_Gel2esw10gPortQoSStatisticsClear_Type())
gel2esw10gPortQoSStatisticsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSStatisticsClear.setStatus(_A)
_Gel2esw10gPortQoSStatisticsTable_Object=MibTable
gel2esw10gPortQoSStatisticsTable=_Gel2esw10gPortQoSStatisticsTable_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2))
if mibBuilder.loadTexts:gel2esw10gPortQoSStatisticsTable.setStatus(_A)
_Gel2esw10gPortQoSStatisticsEntry_Object=MibTableRow
gel2esw10gPortQoSStatisticsEntry=_Gel2esw10gPortQoSStatisticsEntry_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1))
gel2esw10gPortQoSStatisticsEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:gel2esw10gPortQoSStatisticsEntry.setStatus(_A)
class _Gel2esw10gPortQoSStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gPortQoSStatisticsPort_Type.__name__=_C
_Gel2esw10gPortQoSStatisticsPort_Object=MibTableColumn
gel2esw10gPortQoSStatisticsPort=_Gel2esw10gPortQoSStatisticsPort_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,1),_Gel2esw10gPortQoSStatisticsPort_Type())
gel2esw10gPortQoSStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gPortQoSStatisticsPort.setStatus(_A)
_Gel2esw10gPortQoSQ0Rx_Type=Counter64
_Gel2esw10gPortQoSQ0Rx_Object=MibTableColumn
gel2esw10gPortQoSQ0Rx=_Gel2esw10gPortQoSQ0Rx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,2),_Gel2esw10gPortQoSQ0Rx_Type())
gel2esw10gPortQoSQ0Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ0Rx.setStatus(_A)
_Gel2esw10gPortQoSQ0Tx_Type=Counter64
_Gel2esw10gPortQoSQ0Tx_Object=MibTableColumn
gel2esw10gPortQoSQ0Tx=_Gel2esw10gPortQoSQ0Tx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,3),_Gel2esw10gPortQoSQ0Tx_Type())
gel2esw10gPortQoSQ0Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ0Tx.setStatus(_A)
_Gel2esw10gPortQoSQ1Rx_Type=Counter64
_Gel2esw10gPortQoSQ1Rx_Object=MibTableColumn
gel2esw10gPortQoSQ1Rx=_Gel2esw10gPortQoSQ1Rx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,4),_Gel2esw10gPortQoSQ1Rx_Type())
gel2esw10gPortQoSQ1Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ1Rx.setStatus(_A)
_Gel2esw10gPortQoSQ1Tx_Type=Counter64
_Gel2esw10gPortQoSQ1Tx_Object=MibTableColumn
gel2esw10gPortQoSQ1Tx=_Gel2esw10gPortQoSQ1Tx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,5),_Gel2esw10gPortQoSQ1Tx_Type())
gel2esw10gPortQoSQ1Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ1Tx.setStatus(_A)
_Gel2esw10gPortQoSQ2Rx_Type=Counter64
_Gel2esw10gPortQoSQ2Rx_Object=MibTableColumn
gel2esw10gPortQoSQ2Rx=_Gel2esw10gPortQoSQ2Rx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,6),_Gel2esw10gPortQoSQ2Rx_Type())
gel2esw10gPortQoSQ2Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ2Rx.setStatus(_A)
_Gel2esw10gPortQoSQ2Tx_Type=Counter64
_Gel2esw10gPortQoSQ2Tx_Object=MibTableColumn
gel2esw10gPortQoSQ2Tx=_Gel2esw10gPortQoSQ2Tx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,7),_Gel2esw10gPortQoSQ2Tx_Type())
gel2esw10gPortQoSQ2Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ2Tx.setStatus(_A)
_Gel2esw10gPortQoSQ3Rx_Type=Counter64
_Gel2esw10gPortQoSQ3Rx_Object=MibTableColumn
gel2esw10gPortQoSQ3Rx=_Gel2esw10gPortQoSQ3Rx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,8),_Gel2esw10gPortQoSQ3Rx_Type())
gel2esw10gPortQoSQ3Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ3Rx.setStatus(_A)
_Gel2esw10gPortQoSQ3Tx_Type=Counter64
_Gel2esw10gPortQoSQ3Tx_Object=MibTableColumn
gel2esw10gPortQoSQ3Tx=_Gel2esw10gPortQoSQ3Tx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,9),_Gel2esw10gPortQoSQ3Tx_Type())
gel2esw10gPortQoSQ3Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ3Tx.setStatus(_A)
_Gel2esw10gPortQoSQ4Rx_Type=Counter64
_Gel2esw10gPortQoSQ4Rx_Object=MibTableColumn
gel2esw10gPortQoSQ4Rx=_Gel2esw10gPortQoSQ4Rx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,10),_Gel2esw10gPortQoSQ4Rx_Type())
gel2esw10gPortQoSQ4Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ4Rx.setStatus(_A)
_Gel2esw10gPortQoSQ4Tx_Type=Counter64
_Gel2esw10gPortQoSQ4Tx_Object=MibTableColumn
gel2esw10gPortQoSQ4Tx=_Gel2esw10gPortQoSQ4Tx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,11),_Gel2esw10gPortQoSQ4Tx_Type())
gel2esw10gPortQoSQ4Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ4Tx.setStatus(_A)
_Gel2esw10gPortQoSQ5Rx_Type=Counter64
_Gel2esw10gPortQoSQ5Rx_Object=MibTableColumn
gel2esw10gPortQoSQ5Rx=_Gel2esw10gPortQoSQ5Rx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,12),_Gel2esw10gPortQoSQ5Rx_Type())
gel2esw10gPortQoSQ5Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ5Rx.setStatus(_A)
_Gel2esw10gPortQoSQ5Tx_Type=Counter64
_Gel2esw10gPortQoSQ5Tx_Object=MibTableColumn
gel2esw10gPortQoSQ5Tx=_Gel2esw10gPortQoSQ5Tx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,13),_Gel2esw10gPortQoSQ5Tx_Type())
gel2esw10gPortQoSQ5Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ5Tx.setStatus(_A)
_Gel2esw10gPortQoSQ6Rx_Type=Counter64
_Gel2esw10gPortQoSQ6Rx_Object=MibTableColumn
gel2esw10gPortQoSQ6Rx=_Gel2esw10gPortQoSQ6Rx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,14),_Gel2esw10gPortQoSQ6Rx_Type())
gel2esw10gPortQoSQ6Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ6Rx.setStatus(_A)
_Gel2esw10gPortQoSQ6Tx_Type=Counter64
_Gel2esw10gPortQoSQ6Tx_Object=MibTableColumn
gel2esw10gPortQoSQ6Tx=_Gel2esw10gPortQoSQ6Tx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,15),_Gel2esw10gPortQoSQ6Tx_Type())
gel2esw10gPortQoSQ6Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ6Tx.setStatus(_A)
_Gel2esw10gPortQoSQ7Rx_Type=Counter64
_Gel2esw10gPortQoSQ7Rx_Object=MibTableColumn
gel2esw10gPortQoSQ7Rx=_Gel2esw10gPortQoSQ7Rx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,16),_Gel2esw10gPortQoSQ7Rx_Type())
gel2esw10gPortQoSQ7Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ7Rx.setStatus(_A)
_Gel2esw10gPortQoSQ7Tx_Type=Counter64
_Gel2esw10gPortQoSQ7Tx_Object=MibTableColumn
gel2esw10gPortQoSQ7Tx=_Gel2esw10gPortQoSQ7Tx_Object((1,3,6,1,4,1,5205,2,51,2,1,3,2,1,17),_Gel2esw10gPortQoSQ7Tx_Type())
gel2esw10gPortQoSQ7Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortQoSQ7Tx.setStatus(_A)
_Gel2esw10gSFPInfoTable_Object=MibTable
gel2esw10gSFPInfoTable=_Gel2esw10gSFPInfoTable_Object((1,3,6,1,4,1,5205,2,51,2,1,4))
if mibBuilder.loadTexts:gel2esw10gSFPInfoTable.setStatus(_A)
_Gel2esw10gSFPInfoEntry_Object=MibTableRow
gel2esw10gSFPInfoEntry=_Gel2esw10gSFPInfoEntry_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1))
gel2esw10gSFPInfoEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:gel2esw10gSFPInfoEntry.setStatus(_A)
class _Gel2esw10gSFPInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gSFPInfoIndex_Type.__name__=_C
_Gel2esw10gSFPInfoIndex_Object=MibTableColumn
gel2esw10gSFPInfoIndex=_Gel2esw10gSFPInfoIndex_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,1),_Gel2esw10gSFPInfoIndex_Type())
gel2esw10gSFPInfoIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gSFPInfoIndex.setStatus(_A)
_Gel2esw10gSFPInfoPort_Type=DisplayString
_Gel2esw10gSFPInfoPort_Object=MibTableColumn
gel2esw10gSFPInfoPort=_Gel2esw10gSFPInfoPort_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,2),_Gel2esw10gSFPInfoPort_Type())
gel2esw10gSFPInfoPort.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPInfoPort.setStatus(_A)
_Gel2esw10gSFPConnectorType_Type=DisplayString
_Gel2esw10gSFPConnectorType_Object=MibTableColumn
gel2esw10gSFPConnectorType=_Gel2esw10gSFPConnectorType_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,3),_Gel2esw10gSFPConnectorType_Type())
gel2esw10gSFPConnectorType.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPConnectorType.setStatus(_A)
_Gel2esw10gSFPFiberType_Type=DisplayString
_Gel2esw10gSFPFiberType_Object=MibTableColumn
gel2esw10gSFPFiberType=_Gel2esw10gSFPFiberType_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,4),_Gel2esw10gSFPFiberType_Type())
gel2esw10gSFPFiberType.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPFiberType.setStatus(_A)
_Gel2esw10gSFPTxCentralWavelength_Type=DisplayString
_Gel2esw10gSFPTxCentralWavelength_Object=MibTableColumn
gel2esw10gSFPTxCentralWavelength=_Gel2esw10gSFPTxCentralWavelength_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,5),_Gel2esw10gSFPTxCentralWavelength_Type())
gel2esw10gSFPTxCentralWavelength.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPTxCentralWavelength.setStatus(_A)
_Gel2esw10gSFPBaudRate_Type=DisplayString
_Gel2esw10gSFPBaudRate_Object=MibTableColumn
gel2esw10gSFPBaudRate=_Gel2esw10gSFPBaudRate_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,6),_Gel2esw10gSFPBaudRate_Type())
gel2esw10gSFPBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPBaudRate.setStatus(_A)
_Gel2esw10gSFPVendorOUI_Type=DisplayString
_Gel2esw10gSFPVendorOUI_Object=MibTableColumn
gel2esw10gSFPVendorOUI=_Gel2esw10gSFPVendorOUI_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,7),_Gel2esw10gSFPVendorOUI_Type())
gel2esw10gSFPVendorOUI.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPVendorOUI.setStatus(_A)
_Gel2esw10gSFPVendorName_Type=DisplayString
_Gel2esw10gSFPVendorName_Object=MibTableColumn
gel2esw10gSFPVendorName=_Gel2esw10gSFPVendorName_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,8),_Gel2esw10gSFPVendorName_Type())
gel2esw10gSFPVendorName.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPVendorName.setStatus(_A)
_Gel2esw10gSFPVendorPN_Type=DisplayString
_Gel2esw10gSFPVendorPN_Object=MibTableColumn
gel2esw10gSFPVendorPN=_Gel2esw10gSFPVendorPN_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,9),_Gel2esw10gSFPVendorPN_Type())
gel2esw10gSFPVendorPN.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPVendorPN.setStatus(_A)
_Gel2esw10gSFPVendorRev_Type=DisplayString
_Gel2esw10gSFPVendorRev_Object=MibTableColumn
gel2esw10gSFPVendorRev=_Gel2esw10gSFPVendorRev_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,10),_Gel2esw10gSFPVendorRev_Type())
gel2esw10gSFPVendorRev.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPVendorRev.setStatus(_A)
_Gel2esw10gSFPVendorSN_Type=DisplayString
_Gel2esw10gSFPVendorSN_Object=MibTableColumn
gel2esw10gSFPVendorSN=_Gel2esw10gSFPVendorSN_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,11),_Gel2esw10gSFPVendorSN_Type())
gel2esw10gSFPVendorSN.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPVendorSN.setStatus(_A)
_Gel2esw10gSFPDateCode_Type=DisplayString
_Gel2esw10gSFPDateCode_Object=MibTableColumn
gel2esw10gSFPDateCode=_Gel2esw10gSFPDateCode_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,12),_Gel2esw10gSFPDateCode_Type())
gel2esw10gSFPDateCode.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPDateCode.setStatus(_A)
_Gel2esw10gSFPTemperature_Type=DisplayString
_Gel2esw10gSFPTemperature_Object=MibTableColumn
gel2esw10gSFPTemperature=_Gel2esw10gSFPTemperature_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,13),_Gel2esw10gSFPTemperature_Type())
gel2esw10gSFPTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPTemperature.setStatus(_A)
_Gel2esw10gSFPVcc_Type=DisplayString
_Gel2esw10gSFPVcc_Object=MibTableColumn
gel2esw10gSFPVcc=_Gel2esw10gSFPVcc_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,14),_Gel2esw10gSFPVcc_Type())
gel2esw10gSFPVcc.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPVcc.setStatus(_A)
_Gel2esw10gSFPMon1Bias_Type=DisplayString
_Gel2esw10gSFPMon1Bias_Object=MibTableColumn
gel2esw10gSFPMon1Bias=_Gel2esw10gSFPMon1Bias_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,15),_Gel2esw10gSFPMon1Bias_Type())
gel2esw10gSFPMon1Bias.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPMon1Bias.setStatus(_A)
_Gel2esw10gSFPMon2TxPWR_Type=DisplayString
_Gel2esw10gSFPMon2TxPWR_Object=MibTableColumn
gel2esw10gSFPMon2TxPWR=_Gel2esw10gSFPMon2TxPWR_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,16),_Gel2esw10gSFPMon2TxPWR_Type())
gel2esw10gSFPMon2TxPWR.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPMon2TxPWR.setStatus(_A)
_Gel2esw10gSFPMon3RxPWR_Type=DisplayString
_Gel2esw10gSFPMon3RxPWR_Object=MibTableColumn
gel2esw10gSFPMon3RxPWR=_Gel2esw10gSFPMon3RxPWR_Object((1,3,6,1,4,1,5205,2,51,2,1,4,1,17),_Gel2esw10gSFPMon3RxPWR_Type())
gel2esw10gSFPMon3RxPWR.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSFPMon3RxPWR.setStatus(_A)
_Gel2esw10gPortEEETable_Object=MibTable
gel2esw10gPortEEETable=_Gel2esw10gPortEEETable_Object((1,3,6,1,4,1,5205,2,51,2,1,5))
if mibBuilder.loadTexts:gel2esw10gPortEEETable.setStatus(_A)
_Gel2esw10gPortEEEEntry_Object=MibTableRow
gel2esw10gPortEEEEntry=_Gel2esw10gPortEEEEntry_Object((1,3,6,1,4,1,5205,2,51,2,1,5,1))
gel2esw10gPortEEEEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:gel2esw10gPortEEEEntry.setStatus(_A)
class _Gel2esw10gPortEEEPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gPortEEEPort_Type.__name__=_C
_Gel2esw10gPortEEEPort_Object=MibTableColumn
gel2esw10gPortEEEPort=_Gel2esw10gPortEEEPort_Object((1,3,6,1,4,1,5205,2,51,2,1,5,1,1),_Gel2esw10gPortEEEPort_Type())
gel2esw10gPortEEEPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gPortEEEPort.setStatus(_A)
class _Gel2esw10gPortEEEMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortEEEMode_Type.__name__=_C
_Gel2esw10gPortEEEMode_Object=MibTableColumn
gel2esw10gPortEEEMode=_Gel2esw10gPortEEEMode_Object((1,3,6,1,4,1,5205,2,51,2,1,5,1,2),_Gel2esw10gPortEEEMode_Type())
gel2esw10gPortEEEMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortEEEMode.setStatus(_A)
class _Gel2esw10gPortEEEUrgentQueue1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortEEEUrgentQueue1_Type.__name__=_C
_Gel2esw10gPortEEEUrgentQueue1_Object=MibTableColumn
gel2esw10gPortEEEUrgentQueue1=_Gel2esw10gPortEEEUrgentQueue1_Object((1,3,6,1,4,1,5205,2,51,2,1,5,1,3),_Gel2esw10gPortEEEUrgentQueue1_Type())
gel2esw10gPortEEEUrgentQueue1.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortEEEUrgentQueue1.setStatus(_A)
class _Gel2esw10gPortEEEUrgentQueue2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortEEEUrgentQueue2_Type.__name__=_C
_Gel2esw10gPortEEEUrgentQueue2_Object=MibTableColumn
gel2esw10gPortEEEUrgentQueue2=_Gel2esw10gPortEEEUrgentQueue2_Object((1,3,6,1,4,1,5205,2,51,2,1,5,1,4),_Gel2esw10gPortEEEUrgentQueue2_Type())
gel2esw10gPortEEEUrgentQueue2.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortEEEUrgentQueue2.setStatus(_A)
class _Gel2esw10gPortEEEUrgentQueue3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortEEEUrgentQueue3_Type.__name__=_C
_Gel2esw10gPortEEEUrgentQueue3_Object=MibTableColumn
gel2esw10gPortEEEUrgentQueue3=_Gel2esw10gPortEEEUrgentQueue3_Object((1,3,6,1,4,1,5205,2,51,2,1,5,1,5),_Gel2esw10gPortEEEUrgentQueue3_Type())
gel2esw10gPortEEEUrgentQueue3.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortEEEUrgentQueue3.setStatus(_A)
class _Gel2esw10gPortEEEUrgentQueue4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortEEEUrgentQueue4_Type.__name__=_C
_Gel2esw10gPortEEEUrgentQueue4_Object=MibTableColumn
gel2esw10gPortEEEUrgentQueue4=_Gel2esw10gPortEEEUrgentQueue4_Object((1,3,6,1,4,1,5205,2,51,2,1,5,1,6),_Gel2esw10gPortEEEUrgentQueue4_Type())
gel2esw10gPortEEEUrgentQueue4.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortEEEUrgentQueue4.setStatus(_A)
class _Gel2esw10gPortEEEUrgentQueue5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortEEEUrgentQueue5_Type.__name__=_C
_Gel2esw10gPortEEEUrgentQueue5_Object=MibTableColumn
gel2esw10gPortEEEUrgentQueue5=_Gel2esw10gPortEEEUrgentQueue5_Object((1,3,6,1,4,1,5205,2,51,2,1,5,1,7),_Gel2esw10gPortEEEUrgentQueue5_Type())
gel2esw10gPortEEEUrgentQueue5.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortEEEUrgentQueue5.setStatus(_A)
class _Gel2esw10gPortEEEUrgentQueue6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortEEEUrgentQueue6_Type.__name__=_C
_Gel2esw10gPortEEEUrgentQueue6_Object=MibTableColumn
gel2esw10gPortEEEUrgentQueue6=_Gel2esw10gPortEEEUrgentQueue6_Object((1,3,6,1,4,1,5205,2,51,2,1,5,1,8),_Gel2esw10gPortEEEUrgentQueue6_Type())
gel2esw10gPortEEEUrgentQueue6.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortEEEUrgentQueue6.setStatus(_A)
class _Gel2esw10gPortEEEUrgentQueue7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortEEEUrgentQueue7_Type.__name__=_C
_Gel2esw10gPortEEEUrgentQueue7_Object=MibTableColumn
gel2esw10gPortEEEUrgentQueue7=_Gel2esw10gPortEEEUrgentQueue7_Object((1,3,6,1,4,1,5205,2,51,2,1,5,1,9),_Gel2esw10gPortEEEUrgentQueue7_Type())
gel2esw10gPortEEEUrgentQueue7.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortEEEUrgentQueue7.setStatus(_A)
class _Gel2esw10gPortEEEUrgentQueue8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortEEEUrgentQueue8_Type.__name__=_C
_Gel2esw10gPortEEEUrgentQueue8_Object=MibTableColumn
gel2esw10gPortEEEUrgentQueue8=_Gel2esw10gPortEEEUrgentQueue8_Object((1,3,6,1,4,1,5205,2,51,2,1,5,1,10),_Gel2esw10gPortEEEUrgentQueue8_Type())
gel2esw10gPortEEEUrgentQueue8.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortEEEUrgentQueue8.setStatus(_A)
_Gel2esw10gVoiceVLAN_ObjectIdentity=ObjectIdentity
gel2esw10gVoiceVLAN=_Gel2esw10gVoiceVLAN_ObjectIdentity((1,3,6,1,4,1,5205,2,51,2,2))
_Gel2esw10gVoiceVLANConf_ObjectIdentity=ObjectIdentity
gel2esw10gVoiceVLANConf=_Gel2esw10gVoiceVLANConf_ObjectIdentity((1,3,6,1,4,1,5205,2,51,2,2,1))
class _Gel2esw10gVoiceVLANMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gVoiceVLANMode_Type.__name__=_C
_Gel2esw10gVoiceVLANMode_Object=MibScalar
gel2esw10gVoiceVLANMode=_Gel2esw10gVoiceVLANMode_Object((1,3,6,1,4,1,5205,2,51,2,2,1,1),_Gel2esw10gVoiceVLANMode_Type())
gel2esw10gVoiceVLANMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gVoiceVLANMode.setStatus(_A)
class _Gel2esw10gVoiceVLANVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw10gVoiceVLANVLANId_Type.__name__=_C
_Gel2esw10gVoiceVLANVLANId_Object=MibScalar
gel2esw10gVoiceVLANVLANId=_Gel2esw10gVoiceVLANVLANId_Object((1,3,6,1,4,1,5205,2,51,2,2,1,2),_Gel2esw10gVoiceVLANVLANId_Type())
gel2esw10gVoiceVLANVLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gVoiceVLANVLANId.setStatus(_A)
class _Gel2esw10gVoiceVLANAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_Gel2esw10gVoiceVLANAgingTime_Type.__name__=_C
_Gel2esw10gVoiceVLANAgingTime_Object=MibScalar
gel2esw10gVoiceVLANAgingTime=_Gel2esw10gVoiceVLANAgingTime_Object((1,3,6,1,4,1,5205,2,51,2,2,1,3),_Gel2esw10gVoiceVLANAgingTime_Type())
gel2esw10gVoiceVLANAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gVoiceVLANAgingTime.setStatus(_A)
class _Gel2esw10gVoiceVLANTrafficClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gVoiceVLANTrafficClass_Type.__name__=_C
_Gel2esw10gVoiceVLANTrafficClass_Object=MibScalar
gel2esw10gVoiceVLANTrafficClass=_Gel2esw10gVoiceVLANTrafficClass_Object((1,3,6,1,4,1,5205,2,51,2,2,1,4),_Gel2esw10gVoiceVLANTrafficClass_Type())
gel2esw10gVoiceVLANTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gVoiceVLANTrafficClass.setStatus(_A)
_Gel2esw10gVoiceVLANPortTable_Object=MibTable
gel2esw10gVoiceVLANPortTable=_Gel2esw10gVoiceVLANPortTable_Object((1,3,6,1,4,1,5205,2,51,2,2,1,5))
if mibBuilder.loadTexts:gel2esw10gVoiceVLANPortTable.setStatus(_A)
_Gel2esw10gVoiceVLANPortEntry_Object=MibTableRow
gel2esw10gVoiceVLANPortEntry=_Gel2esw10gVoiceVLANPortEntry_Object((1,3,6,1,4,1,5205,2,51,2,2,1,5,1))
gel2esw10gVoiceVLANPortEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:gel2esw10gVoiceVLANPortEntry.setStatus(_A)
class _Gel2esw10gVoiceVLANPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gVoiceVLANPort_Type.__name__=_C
_Gel2esw10gVoiceVLANPort_Object=MibTableColumn
gel2esw10gVoiceVLANPort=_Gel2esw10gVoiceVLANPort_Object((1,3,6,1,4,1,5205,2,51,2,2,1,5,1,1),_Gel2esw10gVoiceVLANPort_Type())
gel2esw10gVoiceVLANPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gVoiceVLANPort.setStatus(_A)
class _Gel2esw10gVoiceVLANPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gVoiceVLANPortMode_Type.__name__=_C
_Gel2esw10gVoiceVLANPortMode_Object=MibTableColumn
gel2esw10gVoiceVLANPortMode=_Gel2esw10gVoiceVLANPortMode_Object((1,3,6,1,4,1,5205,2,51,2,2,1,5,1,2),_Gel2esw10gVoiceVLANPortMode_Type())
gel2esw10gVoiceVLANPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gVoiceVLANPortMode.setStatus(_A)
class _Gel2esw10gVoiceVLANPortSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gVoiceVLANPortSecurity_Type.__name__=_C
_Gel2esw10gVoiceVLANPortSecurity_Object=MibTableColumn
gel2esw10gVoiceVLANPortSecurity=_Gel2esw10gVoiceVLANPortSecurity_Object((1,3,6,1,4,1,5205,2,51,2,2,1,5,1,3),_Gel2esw10gVoiceVLANPortSecurity_Type())
gel2esw10gVoiceVLANPortSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gVoiceVLANPortSecurity.setStatus(_A)
class _Gel2esw10gVoiceVLANPortDiscoveryProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gVoiceVLANPortDiscoveryProtocol_Type.__name__=_C
_Gel2esw10gVoiceVLANPortDiscoveryProtocol_Object=MibTableColumn
gel2esw10gVoiceVLANPortDiscoveryProtocol=_Gel2esw10gVoiceVLANPortDiscoveryProtocol_Object((1,3,6,1,4,1,5205,2,51,2,2,1,5,1,4),_Gel2esw10gVoiceVLANPortDiscoveryProtocol_Type())
gel2esw10gVoiceVLANPortDiscoveryProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gVoiceVLANPortDiscoveryProtocol.setStatus(_A)
_Gel2esw10gVoiceVLANOUI_ObjectIdentity=ObjectIdentity
gel2esw10gVoiceVLANOUI=_Gel2esw10gVoiceVLANOUI_ObjectIdentity((1,3,6,1,4,1,5205,2,51,2,2,2))
class _Gel2esw10gVoiceVLANOUICreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gVoiceVLANOUICreate_Type.__name__=_C
_Gel2esw10gVoiceVLANOUICreate_Object=MibScalar
gel2esw10gVoiceVLANOUICreate=_Gel2esw10gVoiceVLANOUICreate_Object((1,3,6,1,4,1,5205,2,51,2,2,2,1),_Gel2esw10gVoiceVLANOUICreate_Type())
gel2esw10gVoiceVLANOUICreate.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gVoiceVLANOUICreate.setStatus(_A)
_Gel2esw10gVoiceVLANOUITable_Object=MibTable
gel2esw10gVoiceVLANOUITable=_Gel2esw10gVoiceVLANOUITable_Object((1,3,6,1,4,1,5205,2,51,2,2,2,2))
if mibBuilder.loadTexts:gel2esw10gVoiceVLANOUITable.setStatus(_A)
_Gel2esw10gVoiceVLANOUIEntry_Object=MibTableRow
gel2esw10gVoiceVLANOUIEntry=_Gel2esw10gVoiceVLANOUIEntry_Object((1,3,6,1,4,1,5205,2,51,2,2,2,2,1))
gel2esw10gVoiceVLANOUIEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:gel2esw10gVoiceVLANOUIEntry.setStatus(_A)
class _Gel2esw10gVoiceVLANOUIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Gel2esw10gVoiceVLANOUIIndex_Type.__name__=_C
_Gel2esw10gVoiceVLANOUIIndex_Object=MibTableColumn
gel2esw10gVoiceVLANOUIIndex=_Gel2esw10gVoiceVLANOUIIndex_Object((1,3,6,1,4,1,5205,2,51,2,2,2,2,1,1),_Gel2esw10gVoiceVLANOUIIndex_Type())
gel2esw10gVoiceVLANOUIIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gVoiceVLANOUIIndex.setStatus(_A)
class _Gel2esw10gVoiceVLANTelephonyOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Gel2esw10gVoiceVLANTelephonyOUI_Type.__name__=_I
_Gel2esw10gVoiceVLANTelephonyOUI_Object=MibTableColumn
gel2esw10gVoiceVLANTelephonyOUI=_Gel2esw10gVoiceVLANTelephonyOUI_Object((1,3,6,1,4,1,5205,2,51,2,2,2,2,1,2),_Gel2esw10gVoiceVLANTelephonyOUI_Type())
gel2esw10gVoiceVLANTelephonyOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gVoiceVLANTelephonyOUI.setStatus(_A)
class _Gel2esw10gVoiceVLANDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Gel2esw10gVoiceVLANDescription_Type.__name__=_G
_Gel2esw10gVoiceVLANDescription_Object=MibTableColumn
gel2esw10gVoiceVLANDescription=_Gel2esw10gVoiceVLANDescription_Object((1,3,6,1,4,1,5205,2,51,2,2,2,2,1,3),_Gel2esw10gVoiceVLANDescription_Type())
gel2esw10gVoiceVLANDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gVoiceVLANDescription.setStatus(_A)
class _Gel2esw10gVoiceVLANOUIRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw10gVoiceVLANOUIRowStatus_Type.__name__=_C
_Gel2esw10gVoiceVLANOUIRowStatus_Object=MibTableColumn
gel2esw10gVoiceVLANOUIRowStatus=_Gel2esw10gVoiceVLANOUIRowStatus_Object((1,3,6,1,4,1,5205,2,51,2,2,2,2,1,4),_Gel2esw10gVoiceVLANOUIRowStatus_Type())
gel2esw10gVoiceVLANOUIRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gVoiceVLANOUIRowStatus.setStatus(_A)
_Gel2esw10gGARP_ObjectIdentity=ObjectIdentity
gel2esw10gGARP=_Gel2esw10gGARP_ObjectIdentity((1,3,6,1,4,1,5205,2,51,2,3))
_Gel2esw10gGARPConfTable_Object=MibTable
gel2esw10gGARPConfTable=_Gel2esw10gGARPConfTable_Object((1,3,6,1,4,1,5205,2,51,2,3,1))
if mibBuilder.loadTexts:gel2esw10gGARPConfTable.setStatus(_A)
_Gel2esw10gGARPConfEntry_Object=MibTableRow
gel2esw10gGARPConfEntry=_Gel2esw10gGARPConfEntry_Object((1,3,6,1,4,1,5205,2,51,2,3,1,1))
gel2esw10gGARPConfEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:gel2esw10gGARPConfEntry.setStatus(_A)
class _Gel2esw10gGARPConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gGARPConfPort_Type.__name__=_C
_Gel2esw10gGARPConfPort_Object=MibTableColumn
gel2esw10gGARPConfPort=_Gel2esw10gGARPConfPort_Object((1,3,6,1,4,1,5205,2,51,2,3,1,1,1),_Gel2esw10gGARPConfPort_Type())
gel2esw10gGARPConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gGARPConfPort.setStatus(_A)
class _Gel2esw10gGARPJoinTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,1000))
_Gel2esw10gGARPJoinTimer_Type.__name__=_C
_Gel2esw10gGARPJoinTimer_Object=MibTableColumn
gel2esw10gGARPJoinTimer=_Gel2esw10gGARPJoinTimer_Object((1,3,6,1,4,1,5205,2,51,2,3,1,1,2),_Gel2esw10gGARPJoinTimer_Type())
gel2esw10gGARPJoinTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gGARPJoinTimer.setStatus(_A)
class _Gel2esw10gGARPLeaveTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,3000))
_Gel2esw10gGARPLeaveTimer_Type.__name__=_C
_Gel2esw10gGARPLeaveTimer_Object=MibTableColumn
gel2esw10gGARPLeaveTimer=_Gel2esw10gGARPLeaveTimer_Object((1,3,6,1,4,1,5205,2,51,2,3,1,1,3),_Gel2esw10gGARPLeaveTimer_Type())
gel2esw10gGARPLeaveTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gGARPLeaveTimer.setStatus(_A)
class _Gel2esw10gGARPLeaveAllTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10000,50000))
_Gel2esw10gGARPLeaveAllTimer_Type.__name__=_C
_Gel2esw10gGARPLeaveAllTimer_Object=MibTableColumn
gel2esw10gGARPLeaveAllTimer=_Gel2esw10gGARPLeaveAllTimer_Object((1,3,6,1,4,1,5205,2,51,2,3,1,1,4),_Gel2esw10gGARPLeaveAllTimer_Type())
gel2esw10gGARPLeaveAllTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gGARPLeaveAllTimer.setStatus(_A)
class _Gel2esw10gGARPApplicantion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Gel2esw10gGARPApplicantion_Type.__name__=_C
_Gel2esw10gGARPApplicantion_Object=MibTableColumn
gel2esw10gGARPApplicantion=_Gel2esw10gGARPApplicantion_Object((1,3,6,1,4,1,5205,2,51,2,3,1,1,5),_Gel2esw10gGARPApplicantion_Type())
gel2esw10gGARPApplicantion.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gGARPApplicantion.setStatus(_A)
class _Gel2esw10gGARPAttributeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Gel2esw10gGARPAttributeType_Type.__name__=_C
_Gel2esw10gGARPAttributeType_Object=MibTableColumn
gel2esw10gGARPAttributeType=_Gel2esw10gGARPAttributeType_Object((1,3,6,1,4,1,5205,2,51,2,3,1,1,6),_Gel2esw10gGARPAttributeType_Type())
gel2esw10gGARPAttributeType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gGARPAttributeType.setStatus(_A)
class _Gel2esw10gGARPApplicant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gGARPApplicant_Type.__name__=_C
_Gel2esw10gGARPApplicant_Object=MibTableColumn
gel2esw10gGARPApplicant=_Gel2esw10gGARPApplicant_Object((1,3,6,1,4,1,5205,2,51,2,3,1,1,7),_Gel2esw10gGARPApplicant_Type())
gel2esw10gGARPApplicant.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gGARPApplicant.setStatus(_A)
_Gel2esw10gGARPStatisticsTable_Object=MibTable
gel2esw10gGARPStatisticsTable=_Gel2esw10gGARPStatisticsTable_Object((1,3,6,1,4,1,5205,2,51,2,3,2))
if mibBuilder.loadTexts:gel2esw10gGARPStatisticsTable.setStatus(_A)
_Gel2esw10gGARPStatisticsEntry_Object=MibTableRow
gel2esw10gGARPStatisticsEntry=_Gel2esw10gGARPStatisticsEntry_Object((1,3,6,1,4,1,5205,2,51,2,3,2,1))
gel2esw10gGARPStatisticsEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:gel2esw10gGARPStatisticsEntry.setStatus(_A)
class _Gel2esw10gGARPStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gGARPStatisticsPort_Type.__name__=_C
_Gel2esw10gGARPStatisticsPort_Object=MibTableColumn
gel2esw10gGARPStatisticsPort=_Gel2esw10gGARPStatisticsPort_Object((1,3,6,1,4,1,5205,2,51,2,3,2,1,1),_Gel2esw10gGARPStatisticsPort_Type())
gel2esw10gGARPStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gGARPStatisticsPort.setStatus(_A)
_Gel2esw10gGARPStatisticsPeerMAC_Type=DisplayString
_Gel2esw10gGARPStatisticsPeerMAC_Object=MibTableColumn
gel2esw10gGARPStatisticsPeerMAC=_Gel2esw10gGARPStatisticsPeerMAC_Object((1,3,6,1,4,1,5205,2,51,2,3,2,1,2),_Gel2esw10gGARPStatisticsPeerMAC_Type())
gel2esw10gGARPStatisticsPeerMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gGARPStatisticsPeerMAC.setStatus(_A)
_Gel2esw10gGARPStatisticsFailedCount_Type=Counter32
_Gel2esw10gGARPStatisticsFailedCount_Object=MibTableColumn
gel2esw10gGARPStatisticsFailedCount=_Gel2esw10gGARPStatisticsFailedCount_Object((1,3,6,1,4,1,5205,2,51,2,3,2,1,3),_Gel2esw10gGARPStatisticsFailedCount_Type())
gel2esw10gGARPStatisticsFailedCount.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gGARPStatisticsFailedCount.setStatus(_A)
_Gel2esw10gGVRP_ObjectIdentity=ObjectIdentity
gel2esw10gGVRP=_Gel2esw10gGVRP_ObjectIdentity((1,3,6,1,4,1,5205,2,51,2,4))
_Gel2esw10gGVRPConf_ObjectIdentity=ObjectIdentity
gel2esw10gGVRPConf=_Gel2esw10gGVRPConf_ObjectIdentity((1,3,6,1,4,1,5205,2,51,2,4,1))
class _Gel2esw10gGVRPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gGVRPMode_Type.__name__=_C
_Gel2esw10gGVRPMode_Object=MibScalar
gel2esw10gGVRPMode=_Gel2esw10gGVRPMode_Object((1,3,6,1,4,1,5205,2,51,2,4,1,1),_Gel2esw10gGVRPMode_Type())
gel2esw10gGVRPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gGVRPMode.setStatus(_A)
_Gel2esw10gGVRPConfTable_Object=MibTable
gel2esw10gGVRPConfTable=_Gel2esw10gGVRPConfTable_Object((1,3,6,1,4,1,5205,2,51,2,4,1,2))
if mibBuilder.loadTexts:gel2esw10gGVRPConfTable.setStatus(_A)
_Gel2esw10gGVRPConfEntry_Object=MibTableRow
gel2esw10gGVRPConfEntry=_Gel2esw10gGVRPConfEntry_Object((1,3,6,1,4,1,5205,2,51,2,4,1,2,1))
gel2esw10gGVRPConfEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:gel2esw10gGVRPConfEntry.setStatus(_A)
class _Gel2esw10gGVRPConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gGVRPConfPort_Type.__name__=_C
_Gel2esw10gGVRPConfPort_Object=MibTableColumn
gel2esw10gGVRPConfPort=_Gel2esw10gGVRPConfPort_Object((1,3,6,1,4,1,5205,2,51,2,4,1,2,1,1),_Gel2esw10gGVRPConfPort_Type())
gel2esw10gGVRPConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gGVRPConfPort.setStatus(_A)
class _Gel2esw10gGVRPConfPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gGVRPConfPortMode_Type.__name__=_C
_Gel2esw10gGVRPConfPortMode_Object=MibTableColumn
gel2esw10gGVRPConfPortMode=_Gel2esw10gGVRPConfPortMode_Object((1,3,6,1,4,1,5205,2,51,2,4,1,2,1,2),_Gel2esw10gGVRPConfPortMode_Type())
gel2esw10gGVRPConfPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gGVRPConfPortMode.setStatus(_A)
class _Gel2esw10gGVRPConfPortRRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gGVRPConfPortRRole_Type.__name__=_C
_Gel2esw10gGVRPConfPortRRole_Object=MibTableColumn
gel2esw10gGVRPConfPortRRole=_Gel2esw10gGVRPConfPortRRole_Object((1,3,6,1,4,1,5205,2,51,2,4,1,2,1,3),_Gel2esw10gGVRPConfPortRRole_Type())
gel2esw10gGVRPConfPortRRole.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gGVRPConfPortRRole.setStatus(_A)
_Gel2esw10gGVRPStatisticsTable_Object=MibTable
gel2esw10gGVRPStatisticsTable=_Gel2esw10gGVRPStatisticsTable_Object((1,3,6,1,4,1,5205,2,51,2,4,2))
if mibBuilder.loadTexts:gel2esw10gGVRPStatisticsTable.setStatus(_A)
_Gel2esw10gGVRPStatisticsEntry_Object=MibTableRow
gel2esw10gGVRPStatisticsEntry=_Gel2esw10gGVRPStatisticsEntry_Object((1,3,6,1,4,1,5205,2,51,2,4,2,1))
gel2esw10gGVRPStatisticsEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:gel2esw10gGVRPStatisticsEntry.setStatus(_A)
class _Gel2esw10gGVRPStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gGVRPStatisticsPort_Type.__name__=_C
_Gel2esw10gGVRPStatisticsPort_Object=MibTableColumn
gel2esw10gGVRPStatisticsPort=_Gel2esw10gGVRPStatisticsPort_Object((1,3,6,1,4,1,5205,2,51,2,4,2,1,1),_Gel2esw10gGVRPStatisticsPort_Type())
gel2esw10gGVRPStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gGVRPStatisticsPort.setStatus(_A)
_Gel2esw10gGVRPStatisticsJoinTxCnt_Type=Counter32
_Gel2esw10gGVRPStatisticsJoinTxCnt_Object=MibTableColumn
gel2esw10gGVRPStatisticsJoinTxCnt=_Gel2esw10gGVRPStatisticsJoinTxCnt_Object((1,3,6,1,4,1,5205,2,51,2,4,2,1,2),_Gel2esw10gGVRPStatisticsJoinTxCnt_Type())
gel2esw10gGVRPStatisticsJoinTxCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gGVRPStatisticsJoinTxCnt.setStatus(_A)
_Gel2esw10gGVRPStatisticsLeaveTxCnt_Type=Counter32
_Gel2esw10gGVRPStatisticsLeaveTxCnt_Object=MibTableColumn
gel2esw10gGVRPStatisticsLeaveTxCnt=_Gel2esw10gGVRPStatisticsLeaveTxCnt_Object((1,3,6,1,4,1,5205,2,51,2,4,2,1,3),_Gel2esw10gGVRPStatisticsLeaveTxCnt_Type())
gel2esw10gGVRPStatisticsLeaveTxCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gGVRPStatisticsLeaveTxCnt.setStatus(_A)
_Gel2esw10gThermalProtection_ObjectIdentity=ObjectIdentity
gel2esw10gThermalProtection=_Gel2esw10gThermalProtection_ObjectIdentity((1,3,6,1,4,1,5205,2,51,2,5))
class _Gel2esw10gPriority0Temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Gel2esw10gPriority0Temperature_Type.__name__=_C
_Gel2esw10gPriority0Temperature_Object=MibScalar
gel2esw10gPriority0Temperature=_Gel2esw10gPriority0Temperature_Object((1,3,6,1,4,1,5205,2,51,2,5,1),_Gel2esw10gPriority0Temperature_Type())
gel2esw10gPriority0Temperature.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPriority0Temperature.setStatus(_A)
class _Gel2esw10gPriority1Temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Gel2esw10gPriority1Temperature_Type.__name__=_C
_Gel2esw10gPriority1Temperature_Object=MibScalar
gel2esw10gPriority1Temperature=_Gel2esw10gPriority1Temperature_Object((1,3,6,1,4,1,5205,2,51,2,5,2),_Gel2esw10gPriority1Temperature_Type())
gel2esw10gPriority1Temperature.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPriority1Temperature.setStatus(_A)
class _Gel2esw10gPriority2Temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Gel2esw10gPriority2Temperature_Type.__name__=_C
_Gel2esw10gPriority2Temperature_Object=MibScalar
gel2esw10gPriority2Temperature=_Gel2esw10gPriority2Temperature_Object((1,3,6,1,4,1,5205,2,51,2,5,3),_Gel2esw10gPriority2Temperature_Type())
gel2esw10gPriority2Temperature.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPriority2Temperature.setStatus(_A)
class _Gel2esw10gPriority3Temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Gel2esw10gPriority3Temperature_Type.__name__=_C
_Gel2esw10gPriority3Temperature_Object=MibScalar
gel2esw10gPriority3Temperature=_Gel2esw10gPriority3Temperature_Object((1,3,6,1,4,1,5205,2,51,2,5,4),_Gel2esw10gPriority3Temperature_Type())
gel2esw10gPriority3Temperature.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPriority3Temperature.setStatus(_A)
_Gel2esw10gThermalProtectionTable_Object=MibTable
gel2esw10gThermalProtectionTable=_Gel2esw10gThermalProtectionTable_Object((1,3,6,1,4,1,5205,2,51,2,5,5))
if mibBuilder.loadTexts:gel2esw10gThermalProtectionTable.setStatus(_A)
_Gel2esw10gThermalProtectionEntry_Object=MibTableRow
gel2esw10gThermalProtectionEntry=_Gel2esw10gThermalProtectionEntry_Object((1,3,6,1,4,1,5205,2,51,2,5,5,1))
gel2esw10gThermalProtectionEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:gel2esw10gThermalProtectionEntry.setStatus(_A)
class _Gel2esw10gThermalProtectionPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gThermalProtectionPort_Type.__name__=_C
_Gel2esw10gThermalProtectionPort_Object=MibTableColumn
gel2esw10gThermalProtectionPort=_Gel2esw10gThermalProtectionPort_Object((1,3,6,1,4,1,5205,2,51,2,5,5,1,1),_Gel2esw10gThermalProtectionPort_Type())
gel2esw10gThermalProtectionPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gThermalProtectionPort.setStatus(_A)
class _Gel2esw10gThermalProtectionPortTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Gel2esw10gThermalProtectionPortTemperature_Type.__name__=_C
_Gel2esw10gThermalProtectionPortTemperature_Object=MibTableColumn
gel2esw10gThermalProtectionPortTemperature=_Gel2esw10gThermalProtectionPortTemperature_Object((1,3,6,1,4,1,5205,2,51,2,5,5,1,2),_Gel2esw10gThermalProtectionPortTemperature_Type())
gel2esw10gThermalProtectionPortTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gThermalProtectionPortTemperature.setStatus(_A)
class _Gel2esw10gThermalProtectionPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw10gThermalProtectionPortPriority_Type.__name__=_C
_Gel2esw10gThermalProtectionPortPriority_Object=MibTableColumn
gel2esw10gThermalProtectionPortPriority=_Gel2esw10gThermalProtectionPortPriority_Object((1,3,6,1,4,1,5205,2,51,2,5,5,1,3),_Gel2esw10gThermalProtectionPortPriority_Type())
gel2esw10gThermalProtectionPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gThermalProtectionPortPriority.setStatus(_A)
_Gel2esw10gThermalProtectionPortStatus_Type=DisplayString
_Gel2esw10gThermalProtectionPortStatus_Object=MibTableColumn
gel2esw10gThermalProtectionPortStatus=_Gel2esw10gThermalProtectionPortStatus_Object((1,3,6,1,4,1,5205,2,51,2,5,5,1,4),_Gel2esw10gThermalProtectionPortStatus_Type())
gel2esw10gThermalProtectionPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gThermalProtectionPortStatus.setStatus(_A)
_Gel2esw10gMirroring_ObjectIdentity=ObjectIdentity
gel2esw10gMirroring=_Gel2esw10gMirroring_ObjectIdentity((1,3,6,1,4,1,5205,2,51,2,6))
class _Gel2esw10gPortToMirrorOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Gel2esw10gPortToMirrorOn_Type.__name__=_C
_Gel2esw10gPortToMirrorOn_Object=MibScalar
gel2esw10gPortToMirrorOn=_Gel2esw10gPortToMirrorOn_Object((1,3,6,1,4,1,5205,2,51,2,6,1),_Gel2esw10gPortToMirrorOn_Type())
gel2esw10gPortToMirrorOn.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortToMirrorOn.setStatus(_A)
_Gel2esw10gMirrorTable_Object=MibTable
gel2esw10gMirrorTable=_Gel2esw10gMirrorTable_Object((1,3,6,1,4,1,5205,2,51,2,6,2))
if mibBuilder.loadTexts:gel2esw10gMirrorTable.setStatus(_A)
_Gel2esw10gMirrorEntry_Object=MibTableRow
gel2esw10gMirrorEntry=_Gel2esw10gMirrorEntry_Object((1,3,6,1,4,1,5205,2,51,2,6,2,1))
gel2esw10gMirrorEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:gel2esw10gMirrorEntry.setStatus(_A)
class _Gel2esw10gMirrorPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gMirrorPort_Type.__name__=_C
_Gel2esw10gMirrorPort_Object=MibTableColumn
gel2esw10gMirrorPort=_Gel2esw10gMirrorPort_Object((1,3,6,1,4,1,5205,2,51,2,6,2,1,1),_Gel2esw10gMirrorPort_Type())
gel2esw10gMirrorPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gMirrorPort.setStatus(_A)
class _Gel2esw10gMirrorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw10gMirrorMode_Type.__name__=_C
_Gel2esw10gMirrorMode_Object=MibTableColumn
gel2esw10gMirrorMode=_Gel2esw10gMirrorMode_Object((1,3,6,1,4,1,5205,2,51,2,6,2,1,2),_Gel2esw10gMirrorMode_Type())
gel2esw10gMirrorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gMirrorMode.setStatus(_A)
_Gel2esw10gTrapEventSeverity_ObjectIdentity=ObjectIdentity
gel2esw10gTrapEventSeverity=_Gel2esw10gTrapEventSeverity_ObjectIdentity((1,3,6,1,4,1,5205,2,51,2,7))
class _Gel2esw10gTrapEventSeverityACL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityACL_Type.__name__=_C
_Gel2esw10gTrapEventSeverityACL_Object=MibScalar
gel2esw10gTrapEventSeverityACL=_Gel2esw10gTrapEventSeverityACL_Object((1,3,6,1,4,1,5205,2,51,2,7,1),_Gel2esw10gTrapEventSeverityACL_Type())
gel2esw10gTrapEventSeverityACL.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityACL.setStatus(_A)
class _Gel2esw10gTrapEventSeverityACLLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityACLLog_Type.__name__=_C
_Gel2esw10gTrapEventSeverityACLLog_Object=MibScalar
gel2esw10gTrapEventSeverityACLLog=_Gel2esw10gTrapEventSeverityACLLog_Object((1,3,6,1,4,1,5205,2,51,2,7,2),_Gel2esw10gTrapEventSeverityACLLog_Type())
gel2esw10gTrapEventSeverityACLLog.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityACLLog.setStatus(_A)
class _Gel2esw10gTrapEventSeverityAccessMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityAccessMgmt_Type.__name__=_C
_Gel2esw10gTrapEventSeverityAccessMgmt_Object=MibScalar
gel2esw10gTrapEventSeverityAccessMgmt=_Gel2esw10gTrapEventSeverityAccessMgmt_Object((1,3,6,1,4,1,5205,2,51,2,7,3),_Gel2esw10gTrapEventSeverityAccessMgmt_Type())
gel2esw10gTrapEventSeverityAccessMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityAccessMgmt.setStatus(_A)
class _Gel2esw10gTrapEventSeverityAuthFailed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityAuthFailed_Type.__name__=_C
_Gel2esw10gTrapEventSeverityAuthFailed_Object=MibScalar
gel2esw10gTrapEventSeverityAuthFailed=_Gel2esw10gTrapEventSeverityAuthFailed_Object((1,3,6,1,4,1,5205,2,51,2,7,4),_Gel2esw10gTrapEventSeverityAuthFailed_Type())
gel2esw10gTrapEventSeverityAuthFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityAuthFailed.setStatus(_A)
class _Gel2esw10gTrapEventSeverityColdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityColdStart_Type.__name__=_C
_Gel2esw10gTrapEventSeverityColdStart_Object=MibScalar
gel2esw10gTrapEventSeverityColdStart=_Gel2esw10gTrapEventSeverityColdStart_Object((1,3,6,1,4,1,5205,2,51,2,7,5),_Gel2esw10gTrapEventSeverityColdStart_Type())
gel2esw10gTrapEventSeverityColdStart.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityColdStart.setStatus(_A)
class _Gel2esw10gTrapEventSeverityConfigInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityConfigInfo_Type.__name__=_C
_Gel2esw10gTrapEventSeverityConfigInfo_Object=MibScalar
gel2esw10gTrapEventSeverityConfigInfo=_Gel2esw10gTrapEventSeverityConfigInfo_Object((1,3,6,1,4,1,5205,2,51,2,7,6),_Gel2esw10gTrapEventSeverityConfigInfo_Type())
gel2esw10gTrapEventSeverityConfigInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityConfigInfo.setStatus(_A)
class _Gel2esw10gTrapEventSeverityFirmwareUpgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityFirmwareUpgrade_Type.__name__=_C
_Gel2esw10gTrapEventSeverityFirmwareUpgrade_Object=MibScalar
gel2esw10gTrapEventSeverityFirmwareUpgrade=_Gel2esw10gTrapEventSeverityFirmwareUpgrade_Object((1,3,6,1,4,1,5205,2,51,2,7,7),_Gel2esw10gTrapEventSeverityFirmwareUpgrade_Type())
gel2esw10gTrapEventSeverityFirmwareUpgrade.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityFirmwareUpgrade.setStatus(_A)
class _Gel2esw10gTrapEventSeverityImportExport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityImportExport_Type.__name__=_C
_Gel2esw10gTrapEventSeverityImportExport_Object=MibScalar
gel2esw10gTrapEventSeverityImportExport=_Gel2esw10gTrapEventSeverityImportExport_Object((1,3,6,1,4,1,5205,2,51,2,7,8),_Gel2esw10gTrapEventSeverityImportExport_Type())
gel2esw10gTrapEventSeverityImportExport.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityImportExport.setStatus(_A)
class _Gel2esw10gTrapEventSeverityLACP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityLACP_Type.__name__=_C
_Gel2esw10gTrapEventSeverityLACP_Object=MibScalar
gel2esw10gTrapEventSeverityLACP=_Gel2esw10gTrapEventSeverityLACP_Object((1,3,6,1,4,1,5205,2,51,2,7,9),_Gel2esw10gTrapEventSeverityLACP_Type())
gel2esw10gTrapEventSeverityLACP.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityLACP.setStatus(_A)
class _Gel2esw10gTrapEventSeverityLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityLinkStatus_Type.__name__=_C
_Gel2esw10gTrapEventSeverityLinkStatus_Object=MibScalar
gel2esw10gTrapEventSeverityLinkStatus=_Gel2esw10gTrapEventSeverityLinkStatus_Object((1,3,6,1,4,1,5205,2,51,2,7,10),_Gel2esw10gTrapEventSeverityLinkStatus_Type())
gel2esw10gTrapEventSeverityLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityLinkStatus.setStatus(_A)
class _Gel2esw10gTrapEventSeverityLogin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityLogin_Type.__name__=_C
_Gel2esw10gTrapEventSeverityLogin_Object=MibScalar
gel2esw10gTrapEventSeverityLogin=_Gel2esw10gTrapEventSeverityLogin_Object((1,3,6,1,4,1,5205,2,51,2,7,11),_Gel2esw10gTrapEventSeverityLogin_Type())
gel2esw10gTrapEventSeverityLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityLogin.setStatus(_A)
class _Gel2esw10gTrapEventSeverityLogout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityLogout_Type.__name__=_C
_Gel2esw10gTrapEventSeverityLogout_Object=MibScalar
gel2esw10gTrapEventSeverityLogout=_Gel2esw10gTrapEventSeverityLogout_Object((1,3,6,1,4,1,5205,2,51,2,7,12),_Gel2esw10gTrapEventSeverityLogout_Type())
gel2esw10gTrapEventSeverityLogout.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityLogout.setStatus(_A)
class _Gel2esw10gTrapEventSeverityLoopProtect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityLoopProtect_Type.__name__=_C
_Gel2esw10gTrapEventSeverityLoopProtect_Object=MibScalar
gel2esw10gTrapEventSeverityLoopProtect=_Gel2esw10gTrapEventSeverityLoopProtect_Object((1,3,6,1,4,1,5205,2,51,2,7,13),_Gel2esw10gTrapEventSeverityLoopProtect_Type())
gel2esw10gTrapEventSeverityLoopProtect.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityLoopProtect.setStatus(_A)
class _Gel2esw10gTrapEventSeverityMgmtIPChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityMgmtIPChange_Type.__name__=_C
_Gel2esw10gTrapEventSeverityMgmtIPChange_Object=MibScalar
gel2esw10gTrapEventSeverityMgmtIPChange=_Gel2esw10gTrapEventSeverityMgmtIPChange_Object((1,3,6,1,4,1,5205,2,51,2,7,14),_Gel2esw10gTrapEventSeverityMgmtIPChange_Type())
gel2esw10gTrapEventSeverityMgmtIPChange.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityMgmtIPChange.setStatus(_A)
class _Gel2esw10gTrapEventSeverityModuleChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityModuleChange_Type.__name__=_C
_Gel2esw10gTrapEventSeverityModuleChange_Object=MibScalar
gel2esw10gTrapEventSeverityModuleChange=_Gel2esw10gTrapEventSeverityModuleChange_Object((1,3,6,1,4,1,5205,2,51,2,7,15),_Gel2esw10gTrapEventSeverityModuleChange_Type())
gel2esw10gTrapEventSeverityModuleChange.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityModuleChange.setStatus(_A)
class _Gel2esw10gTrapEventSeverityNAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityNAS_Type.__name__=_C
_Gel2esw10gTrapEventSeverityNAS_Object=MibScalar
gel2esw10gTrapEventSeverityNAS=_Gel2esw10gTrapEventSeverityNAS_Object((1,3,6,1,4,1,5205,2,51,2,7,16),_Gel2esw10gTrapEventSeverityNAS_Type())
gel2esw10gTrapEventSeverityNAS.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityNAS.setStatus(_A)
class _Gel2esw10gTrapEventSeverityPasswdChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityPasswdChange_Type.__name__=_C
_Gel2esw10gTrapEventSeverityPasswdChange_Object=MibScalar
gel2esw10gTrapEventSeverityPasswdChange=_Gel2esw10gTrapEventSeverityPasswdChange_Object((1,3,6,1,4,1,5205,2,51,2,7,17),_Gel2esw10gTrapEventSeverityPasswdChange_Type())
gel2esw10gTrapEventSeverityPasswdChange.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityPasswdChange.setStatus(_A)
class _Gel2esw10gTrapEventSeverityPortSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityPortSecurity_Type.__name__=_C
_Gel2esw10gTrapEventSeverityPortSecurity_Object=MibScalar
gel2esw10gTrapEventSeverityPortSecurity=_Gel2esw10gTrapEventSeverityPortSecurity_Object((1,3,6,1,4,1,5205,2,51,2,7,18),_Gel2esw10gTrapEventSeverityPortSecurity_Type())
gel2esw10gTrapEventSeverityPortSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityPortSecurity.setStatus(_A)
class _Gel2esw10gTrapEventSeverityThermalProtect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityThermalProtect_Type.__name__=_C
_Gel2esw10gTrapEventSeverityThermalProtect_Object=MibScalar
gel2esw10gTrapEventSeverityThermalProtect=_Gel2esw10gTrapEventSeverityThermalProtect_Object((1,3,6,1,4,1,5205,2,51,2,7,19),_Gel2esw10gTrapEventSeverityThermalProtect_Type())
gel2esw10gTrapEventSeverityThermalProtect.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityThermalProtect.setStatus(_A)
class _Gel2esw10gTrapEventSeverityVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityVLAN_Type.__name__=_C
_Gel2esw10gTrapEventSeverityVLAN_Object=MibScalar
gel2esw10gTrapEventSeverityVLAN=_Gel2esw10gTrapEventSeverityVLAN_Object((1,3,6,1,4,1,5205,2,51,2,7,20),_Gel2esw10gTrapEventSeverityVLAN_Type())
gel2esw10gTrapEventSeverityVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityVLAN.setStatus(_A)
class _Gel2esw10gTrapEventSeverityWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gTrapEventSeverityWarmStart_Type.__name__=_C
_Gel2esw10gTrapEventSeverityWarmStart_Object=MibScalar
gel2esw10gTrapEventSeverityWarmStart=_Gel2esw10gTrapEventSeverityWarmStart_Object((1,3,6,1,4,1,5205,2,51,2,7,21),_Gel2esw10gTrapEventSeverityWarmStart_Type())
gel2esw10gTrapEventSeverityWarmStart.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTrapEventSeverityWarmStart.setStatus(_A)
_Gel2esw10gSMTP_ObjectIdentity=ObjectIdentity
gel2esw10gSMTP=_Gel2esw10gSMTP_ObjectIdentity((1,3,6,1,4,1,5205,2,51,2,8))
_Gel2esw10gSMTPMailServer_Type=DisplayString
_Gel2esw10gSMTPMailServer_Object=MibScalar
gel2esw10gSMTPMailServer=_Gel2esw10gSMTPMailServer_Object((1,3,6,1,4,1,5205,2,51,2,8,1),_Gel2esw10gSMTPMailServer_Type())
gel2esw10gSMTPMailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSMTPMailServer.setStatus(_A)
_Gel2esw10gSMTPUserName_Type=DisplayString
_Gel2esw10gSMTPUserName_Object=MibScalar
gel2esw10gSMTPUserName=_Gel2esw10gSMTPUserName_Object((1,3,6,1,4,1,5205,2,51,2,8,2),_Gel2esw10gSMTPUserName_Type())
gel2esw10gSMTPUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSMTPUserName.setStatus(_A)
_Gel2esw10gSMTPPassword_Type=DisplayString
_Gel2esw10gSMTPPassword_Object=MibScalar
gel2esw10gSMTPPassword=_Gel2esw10gSMTPPassword_Object((1,3,6,1,4,1,5205,2,51,2,8,3),_Gel2esw10gSMTPPassword_Type())
gel2esw10gSMTPPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSMTPPassword.setStatus(_A)
class _Gel2esw10gSMTPServeriryLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw10gSMTPServeriryLevel_Type.__name__=_C
_Gel2esw10gSMTPServeriryLevel_Object=MibScalar
gel2esw10gSMTPServeriryLevel=_Gel2esw10gSMTPServeriryLevel_Object((1,3,6,1,4,1,5205,2,51,2,8,4),_Gel2esw10gSMTPServeriryLevel_Type())
gel2esw10gSMTPServeriryLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSMTPServeriryLevel.setStatus(_A)
_Gel2esw10gSMTPSender_Type=DisplayString
_Gel2esw10gSMTPSender_Object=MibScalar
gel2esw10gSMTPSender=_Gel2esw10gSMTPSender_Object((1,3,6,1,4,1,5205,2,51,2,8,5),_Gel2esw10gSMTPSender_Type())
gel2esw10gSMTPSender.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSMTPSender.setStatus(_A)
_Gel2esw10gSMTPReturnPath_Type=DisplayString
_Gel2esw10gSMTPReturnPath_Object=MibScalar
gel2esw10gSMTPReturnPath=_Gel2esw10gSMTPReturnPath_Object((1,3,6,1,4,1,5205,2,51,2,8,6),_Gel2esw10gSMTPReturnPath_Type())
gel2esw10gSMTPReturnPath.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSMTPReturnPath.setStatus(_A)
_Gel2esw10gSMTPEmailAddress1_Type=DisplayString
_Gel2esw10gSMTPEmailAddress1_Object=MibScalar
gel2esw10gSMTPEmailAddress1=_Gel2esw10gSMTPEmailAddress1_Object((1,3,6,1,4,1,5205,2,51,2,8,7),_Gel2esw10gSMTPEmailAddress1_Type())
gel2esw10gSMTPEmailAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSMTPEmailAddress1.setStatus(_A)
_Gel2esw10gSMTPEmailAddress2_Type=DisplayString
_Gel2esw10gSMTPEmailAddress2_Object=MibScalar
gel2esw10gSMTPEmailAddress2=_Gel2esw10gSMTPEmailAddress2_Object((1,3,6,1,4,1,5205,2,51,2,8,8),_Gel2esw10gSMTPEmailAddress2_Type())
gel2esw10gSMTPEmailAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSMTPEmailAddress2.setStatus(_A)
_Gel2esw10gSMTPEmailAddress3_Type=DisplayString
_Gel2esw10gSMTPEmailAddress3_Object=MibScalar
gel2esw10gSMTPEmailAddress3=_Gel2esw10gSMTPEmailAddress3_Object((1,3,6,1,4,1,5205,2,51,2,8,9),_Gel2esw10gSMTPEmailAddress3_Type())
gel2esw10gSMTPEmailAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSMTPEmailAddress3.setStatus(_A)
_Gel2esw10gSMTPEmailAddress4_Type=DisplayString
_Gel2esw10gSMTPEmailAddress4_Object=MibScalar
gel2esw10gSMTPEmailAddress4=_Gel2esw10gSMTPEmailAddress4_Object((1,3,6,1,4,1,5205,2,51,2,8,10),_Gel2esw10gSMTPEmailAddress4_Type())
gel2esw10gSMTPEmailAddress4.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSMTPEmailAddress4.setStatus(_A)
_Gel2esw10gSMTPEmailAddress5_Type=DisplayString
_Gel2esw10gSMTPEmailAddress5_Object=MibScalar
gel2esw10gSMTPEmailAddress5=_Gel2esw10gSMTPEmailAddress5_Object((1,3,6,1,4,1,5205,2,51,2,8,11),_Gel2esw10gSMTPEmailAddress5_Type())
gel2esw10gSMTPEmailAddress5.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSMTPEmailAddress5.setStatus(_A)
_Gel2esw10gSMTPEmailAddress6_Type=DisplayString
_Gel2esw10gSMTPEmailAddress6_Object=MibScalar
gel2esw10gSMTPEmailAddress6=_Gel2esw10gSMTPEmailAddress6_Object((1,3,6,1,4,1,5205,2,51,2,8,12),_Gel2esw10gSMTPEmailAddress6_Type())
gel2esw10gSMTPEmailAddress6.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSMTPEmailAddress6.setStatus(_A)
_Gel2esw10gACL_ObjectIdentity=ObjectIdentity
gel2esw10gACL=_Gel2esw10gACL_ObjectIdentity((1,3,6,1,4,1,5205,2,51,2,9))
_Gel2esw10gACLPortsConfTable_Object=MibTable
gel2esw10gACLPortsConfTable=_Gel2esw10gACLPortsConfTable_Object((1,3,6,1,4,1,5205,2,51,2,9,1))
if mibBuilder.loadTexts:gel2esw10gACLPortsConfTable.setStatus(_A)
_Gel2esw10gACLPortsConfEntry_Object=MibTableRow
gel2esw10gACLPortsConfEntry=_Gel2esw10gACLPortsConfEntry_Object((1,3,6,1,4,1,5205,2,51,2,9,1,1))
gel2esw10gACLPortsConfEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:gel2esw10gACLPortsConfEntry.setStatus(_A)
class _Gel2esw10gACLPortsConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gACLPortsConfPort_Type.__name__=_C
_Gel2esw10gACLPortsConfPort_Object=MibTableColumn
gel2esw10gACLPortsConfPort=_Gel2esw10gACLPortsConfPort_Object((1,3,6,1,4,1,5205,2,51,2,9,1,1,1),_Gel2esw10gACLPortsConfPort_Type())
gel2esw10gACLPortsConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gACLPortsConfPort.setStatus(_A)
class _Gel2esw10gACLPortsConfPolicyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Gel2esw10gACLPortsConfPolicyID_Type.__name__=_C
_Gel2esw10gACLPortsConfPolicyID_Object=MibTableColumn
gel2esw10gACLPortsConfPolicyID=_Gel2esw10gACLPortsConfPolicyID_Object((1,3,6,1,4,1,5205,2,51,2,9,1,1,2),_Gel2esw10gACLPortsConfPolicyID_Type())
gel2esw10gACLPortsConfPolicyID.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLPortsConfPolicyID.setStatus(_A)
class _Gel2esw10gACLPortsConfAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gACLPortsConfAction_Type.__name__=_C
_Gel2esw10gACLPortsConfAction_Object=MibTableColumn
gel2esw10gACLPortsConfAction=_Gel2esw10gACLPortsConfAction_Object((1,3,6,1,4,1,5205,2,51,2,9,1,1,3),_Gel2esw10gACLPortsConfAction_Type())
gel2esw10gACLPortsConfAction.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLPortsConfAction.setStatus(_A)
class _Gel2esw10gACLPortsConfRateLimiterID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_Gel2esw10gACLPortsConfRateLimiterID_Type.__name__=_C
_Gel2esw10gACLPortsConfRateLimiterID_Object=MibTableColumn
gel2esw10gACLPortsConfRateLimiterID=_Gel2esw10gACLPortsConfRateLimiterID_Object((1,3,6,1,4,1,5205,2,51,2,9,1,1,4),_Gel2esw10gACLPortsConfRateLimiterID_Type())
gel2esw10gACLPortsConfRateLimiterID.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLPortsConfRateLimiterID.setStatus(_A)
class _Gel2esw10gACLPortsConfPortRedirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_Gel2esw10gACLPortsConfPortRedirect_Type.__name__=_C
_Gel2esw10gACLPortsConfPortRedirect_Object=MibTableColumn
gel2esw10gACLPortsConfPortRedirect=_Gel2esw10gACLPortsConfPortRedirect_Object((1,3,6,1,4,1,5205,2,51,2,9,1,1,5),_Gel2esw10gACLPortsConfPortRedirect_Type())
gel2esw10gACLPortsConfPortRedirect.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLPortsConfPortRedirect.setStatus(_A)
class _Gel2esw10gACLPortsConfMirror_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gACLPortsConfMirror_Type.__name__=_C
_Gel2esw10gACLPortsConfMirror_Object=MibTableColumn
gel2esw10gACLPortsConfMirror=_Gel2esw10gACLPortsConfMirror_Object((1,3,6,1,4,1,5205,2,51,2,9,1,1,6),_Gel2esw10gACLPortsConfMirror_Type())
gel2esw10gACLPortsConfMirror.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLPortsConfMirror.setStatus(_A)
class _Gel2esw10gACLPortsConfLogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gACLPortsConfLogging_Type.__name__=_C
_Gel2esw10gACLPortsConfLogging_Object=MibTableColumn
gel2esw10gACLPortsConfLogging=_Gel2esw10gACLPortsConfLogging_Object((1,3,6,1,4,1,5205,2,51,2,9,1,1,7),_Gel2esw10gACLPortsConfLogging_Type())
gel2esw10gACLPortsConfLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLPortsConfLogging.setStatus(_A)
class _Gel2esw10gACLPortsConfShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gACLPortsConfShutdown_Type.__name__=_C
_Gel2esw10gACLPortsConfShutdown_Object=MibTableColumn
gel2esw10gACLPortsConfShutdown=_Gel2esw10gACLPortsConfShutdown_Object((1,3,6,1,4,1,5205,2,51,2,9,1,1,8),_Gel2esw10gACLPortsConfShutdown_Type())
gel2esw10gACLPortsConfShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLPortsConfShutdown.setStatus(_A)
class _Gel2esw10gACLPortsConfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gACLPortsConfState_Type.__name__=_C
_Gel2esw10gACLPortsConfState_Object=MibTableColumn
gel2esw10gACLPortsConfState=_Gel2esw10gACLPortsConfState_Object((1,3,6,1,4,1,5205,2,51,2,9,1,1,9),_Gel2esw10gACLPortsConfState_Type())
gel2esw10gACLPortsConfState.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLPortsConfState.setStatus(_A)
_Gel2esw10gACLPortsConfCounter_Type=Counter32
_Gel2esw10gACLPortsConfCounter_Object=MibTableColumn
gel2esw10gACLPortsConfCounter=_Gel2esw10gACLPortsConfCounter_Object((1,3,6,1,4,1,5205,2,51,2,9,1,1,10),_Gel2esw10gACLPortsConfCounter_Type())
gel2esw10gACLPortsConfCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gACLPortsConfCounter.setStatus(_A)
_Gel2esw10gACLRateLimiterTable_Object=MibTable
gel2esw10gACLRateLimiterTable=_Gel2esw10gACLRateLimiterTable_Object((1,3,6,1,4,1,5205,2,51,2,9,2))
if mibBuilder.loadTexts:gel2esw10gACLRateLimiterTable.setStatus(_A)
_Gel2esw10gACLRateLimiterEntry_Object=MibTableRow
gel2esw10gACLRateLimiterEntry=_Gel2esw10gACLRateLimiterEntry_Object((1,3,6,1,4,1,5205,2,51,2,9,2,1))
gel2esw10gACLRateLimiterEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:gel2esw10gACLRateLimiterEntry.setStatus(_A)
class _Gel2esw10gACLRateLimiterID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Gel2esw10gACLRateLimiterID_Type.__name__=_C
_Gel2esw10gACLRateLimiterID_Object=MibTableColumn
gel2esw10gACLRateLimiterID=_Gel2esw10gACLRateLimiterID_Object((1,3,6,1,4,1,5205,2,51,2,9,2,1,1),_Gel2esw10gACLRateLimiterID_Type())
gel2esw10gACLRateLimiterID.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gACLRateLimiterID.setStatus(_A)
class _Gel2esw10gACLRateLimiterUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gACLRateLimiterUnit_Type.__name__=_C
_Gel2esw10gACLRateLimiterUnit_Object=MibTableColumn
gel2esw10gACLRateLimiterUnit=_Gel2esw10gACLRateLimiterUnit_Object((1,3,6,1,4,1,5205,2,51,2,9,2,1,2),_Gel2esw10gACLRateLimiterUnit_Type())
gel2esw10gACLRateLimiterUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLRateLimiterUnit.setStatus(_A)
class _Gel2esw10gACLRateLimiterRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3276700))
_Gel2esw10gACLRateLimiterRate_Type.__name__=_C
_Gel2esw10gACLRateLimiterRate_Object=MibTableColumn
gel2esw10gACLRateLimiterRate=_Gel2esw10gACLRateLimiterRate_Object((1,3,6,1,4,1,5205,2,51,2,9,2,1,3),_Gel2esw10gACLRateLimiterRate_Type())
gel2esw10gACLRateLimiterRate.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLRateLimiterRate.setStatus(_A)
_Gel2esw10gACLACE_ObjectIdentity=ObjectIdentity
gel2esw10gACLACE=_Gel2esw10gACLACE_ObjectIdentity((1,3,6,1,4,1,5205,2,51,2,9,3))
class _Gel2esw10gACLACECreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gACLACECreate_Type.__name__=_C
_Gel2esw10gACLACECreate_Object=MibScalar
gel2esw10gACLACECreate=_Gel2esw10gACLACECreate_Object((1,3,6,1,4,1,5205,2,51,2,9,3,1),_Gel2esw10gACLACECreate_Type())
gel2esw10gACLACECreate.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACECreate.setStatus(_A)
_Gel2esw10gACLACETable_Object=MibTable
gel2esw10gACLACETable=_Gel2esw10gACLACETable_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2))
if mibBuilder.loadTexts:gel2esw10gACLACETable.setStatus(_A)
_Gel2esw10gACLACEEntry_Object=MibTableRow
gel2esw10gACLACEEntry=_Gel2esw10gACLACEEntry_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1))
gel2esw10gACLACEEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:gel2esw10gACLACEEntry.setStatus(_A)
class _Gel2esw10gACLACEIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Gel2esw10gACLACEIndex_Type.__name__=_C
_Gel2esw10gACLACEIndex_Object=MibTableColumn
gel2esw10gACLACEIndex=_Gel2esw10gACLACEIndex_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,1),_Gel2esw10gACLACEIndex_Type())
gel2esw10gACLACEIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gACLACEIndex.setStatus(_A)
class _Gel2esw10gACLACEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Gel2esw10gACLACEID_Type.__name__=_C
_Gel2esw10gACLACEID_Object=MibTableColumn
gel2esw10gACLACEID=_Gel2esw10gACLACEID_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,2),_Gel2esw10gACLACEID_Type())
gel2esw10gACLACEID.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEID.setStatus(_A)
class _Gel2esw10gACLACENextID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Gel2esw10gACLACENextID_Type.__name__=_C
_Gel2esw10gACLACENextID_Object=MibTableColumn
gel2esw10gACLACENextID=_Gel2esw10gACLACENextID_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,3),_Gel2esw10gACLACENextID_Type())
gel2esw10gACLACENextID.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACENextID.setStatus(_A)
_Gel2esw10gACLACEIngressPort_Type=DisplayString
_Gel2esw10gACLACEIngressPort_Object=MibTableColumn
gel2esw10gACLACEIngressPort=_Gel2esw10gACLACEIngressPort_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,4),_Gel2esw10gACLACEIngressPort_Type())
gel2esw10gACLACEIngressPort.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEIngressPort.setStatus(_A)
class _Gel2esw10gACLACEPortPolicyNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Gel2esw10gACLACEPortPolicyNumber_Type.__name__=_C
_Gel2esw10gACLACEPortPolicyNumber_Object=MibTableColumn
gel2esw10gACLACEPortPolicyNumber=_Gel2esw10gACLACEPortPolicyNumber_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,5),_Gel2esw10gACLACEPortPolicyNumber_Type())
gel2esw10gACLACEPortPolicyNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEPortPolicyNumber.setStatus(_A)
class _Gel2esw10gACLACEPortPolicyBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Gel2esw10gACLACEPortPolicyBitmask_Type.__name__=_C
_Gel2esw10gACLACEPortPolicyBitmask_Object=MibTableColumn
gel2esw10gACLACEPortPolicyBitmask=_Gel2esw10gACLACEPortPolicyBitmask_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,6),_Gel2esw10gACLACEPortPolicyBitmask_Type())
gel2esw10gACLACEPortPolicyBitmask.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEPortPolicyBitmask.setStatus(_A)
class _Gel2esw10gACLACEFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_Gel2esw10gACLACEFrameType_Type.__name__=_C
_Gel2esw10gACLACEFrameType_Object=MibTableColumn
gel2esw10gACLACEFrameType=_Gel2esw10gACLACEFrameType_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,7),_Gel2esw10gACLACEFrameType_Type())
gel2esw10gACLACEFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEFrameType.setStatus(_A)
class _Gel2esw10gACLACEAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gACLACEAction_Type.__name__=_C
_Gel2esw10gACLACEAction_Object=MibTableColumn
gel2esw10gACLACEAction=_Gel2esw10gACLACEAction_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,8),_Gel2esw10gACLACEAction_Type())
gel2esw10gACLACEAction.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEAction.setStatus(_A)
_Gel2esw10gACLACEDenyPortRedirect_Type=DisplayString
_Gel2esw10gACLACEDenyPortRedirect_Object=MibTableColumn
gel2esw10gACLACEDenyPortRedirect=_Gel2esw10gACLACEDenyPortRedirect_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,9),_Gel2esw10gACLACEDenyPortRedirect_Type())
gel2esw10gACLACEDenyPortRedirect.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEDenyPortRedirect.setStatus(_A)
class _Gel2esw10gACLACELogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gACLACELogging_Type.__name__=_C
_Gel2esw10gACLACELogging_Object=MibTableColumn
gel2esw10gACLACELogging=_Gel2esw10gACLACELogging_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,10),_Gel2esw10gACLACELogging_Type())
gel2esw10gACLACELogging.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACELogging.setStatus(_A)
class _Gel2esw10gACLACEMirror_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gACLACEMirror_Type.__name__=_C
_Gel2esw10gACLACEMirror_Object=MibTableColumn
gel2esw10gACLACEMirror=_Gel2esw10gACLACEMirror_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,11),_Gel2esw10gACLACEMirror_Type())
gel2esw10gACLACEMirror.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEMirror.setStatus(_A)
class _Gel2esw10gACLACERateLimiter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_Gel2esw10gACLACERateLimiter_Type.__name__=_C
_Gel2esw10gACLACERateLimiter_Object=MibTableColumn
gel2esw10gACLACERateLimiter=_Gel2esw10gACLACERateLimiter_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,12),_Gel2esw10gACLACERateLimiter_Type())
gel2esw10gACLACERateLimiter.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACERateLimiter.setStatus(_A)
class _Gel2esw10gACLACEShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gACLACEShutdown_Type.__name__=_C
_Gel2esw10gACLACEShutdown_Object=MibTableColumn
gel2esw10gACLACEShutdown=_Gel2esw10gACLACEShutdown_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,13),_Gel2esw10gACLACEShutdown_Type())
gel2esw10gACLACEShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEShutdown.setStatus(_A)
class _Gel2esw10gACLACEVLAN8021QTagged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACEVLAN8021QTagged_Type.__name__=_C
_Gel2esw10gACLACEVLAN8021QTagged_Object=MibTableColumn
gel2esw10gACLACEVLAN8021QTagged=_Gel2esw10gACLACEVLAN8021QTagged_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,14),_Gel2esw10gACLACEVLAN8021QTagged_Type())
gel2esw10gACLACEVLAN8021QTagged.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEVLAN8021QTagged.setStatus(_A)
class _Gel2esw10gACLACEVLANTagPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_Gel2esw10gACLACEVLANTagPriority_Type.__name__=_C
_Gel2esw10gACLACEVLANTagPriority_Object=MibTableColumn
gel2esw10gACLACEVLANTagPriority=_Gel2esw10gACLACEVLANTagPriority_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,15),_Gel2esw10gACLACEVLANTagPriority_Type())
gel2esw10gACLACEVLANTagPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEVLANTagPriority.setStatus(_A)
class _Gel2esw10gACLACEVLANVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Gel2esw10gACLACEVLANVID_Type.__name__=_C
_Gel2esw10gACLACEVLANVID_Object=MibTableColumn
gel2esw10gACLACEVLANVID=_Gel2esw10gACLACEVLANVID_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,16),_Gel2esw10gACLACEVLANVID_Type())
gel2esw10gACLACEVLANVID.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEVLANVID.setStatus(_A)
class _Gel2esw10gACLACEEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Gel2esw10gACLACEEtherType_Type.__name__=_C
_Gel2esw10gACLACEEtherType_Object=MibTableColumn
gel2esw10gACLACEEtherType=_Gel2esw10gACLACEEtherType_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,17),_Gel2esw10gACLACEEtherType_Type())
gel2esw10gACLACEEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEEtherType.setStatus(_A)
_Gel2esw10gACLACESMAC_Type=DisplayString
_Gel2esw10gACLACESMAC_Object=MibTableColumn
gel2esw10gACLACESMAC=_Gel2esw10gACLACESMAC_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,18),_Gel2esw10gACLACESMAC_Type())
gel2esw10gACLACESMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACESMAC.setStatus(_A)
class _Gel2esw10gACLACEDMACType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Gel2esw10gACLACEDMACType_Type.__name__=_C
_Gel2esw10gACLACEDMACType_Object=MibTableColumn
gel2esw10gACLACEDMACType=_Gel2esw10gACLACEDMACType_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,19),_Gel2esw10gACLACEDMACType_Type())
gel2esw10gACLACEDMACType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEDMACType.setStatus(_A)
_Gel2esw10gACLACEDMAC_Type=DisplayString
_Gel2esw10gACLACEDMAC_Object=MibTableColumn
gel2esw10gACLACEDMAC=_Gel2esw10gACLACEDMAC_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,20),_Gel2esw10gACLACEDMAC_Type())
gel2esw10gACLACEDMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEDMAC.setStatus(_A)
class _Gel2esw10gACLACEArpOpcode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw10gACLACEArpOpcode_Type.__name__=_C
_Gel2esw10gACLACEArpOpcode_Object=MibTableColumn
gel2esw10gACLACEArpOpcode=_Gel2esw10gACLACEArpOpcode_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,21),_Gel2esw10gACLACEArpOpcode_Type())
gel2esw10gACLACEArpOpcode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEArpOpcode.setStatus(_A)
class _Gel2esw10gACLACEArpFlagsRequestReply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACEArpFlagsRequestReply_Type.__name__=_C
_Gel2esw10gACLACEArpFlagsRequestReply_Object=MibTableColumn
gel2esw10gACLACEArpFlagsRequestReply=_Gel2esw10gACLACEArpFlagsRequestReply_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,22),_Gel2esw10gACLACEArpFlagsRequestReply_Type())
gel2esw10gACLACEArpFlagsRequestReply.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEArpFlagsRequestReply.setStatus(_A)
class _Gel2esw10gACLACEArpFlagsArpSmac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACEArpFlagsArpSmac_Type.__name__=_C
_Gel2esw10gACLACEArpFlagsArpSmac_Object=MibTableColumn
gel2esw10gACLACEArpFlagsArpSmac=_Gel2esw10gACLACEArpFlagsArpSmac_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,23),_Gel2esw10gACLACEArpFlagsArpSmac_Type())
gel2esw10gACLACEArpFlagsArpSmac.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEArpFlagsArpSmac.setStatus(_A)
class _Gel2esw10gACLACEArpFlagsRarpDmac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACEArpFlagsRarpDmac_Type.__name__=_C
_Gel2esw10gACLACEArpFlagsRarpDmac_Object=MibTableColumn
gel2esw10gACLACEArpFlagsRarpDmac=_Gel2esw10gACLACEArpFlagsRarpDmac_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,24),_Gel2esw10gACLACEArpFlagsRarpDmac_Type())
gel2esw10gACLACEArpFlagsRarpDmac.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEArpFlagsRarpDmac.setStatus(_A)
class _Gel2esw10gACLACEArpFlagsLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACEArpFlagsLength_Type.__name__=_C
_Gel2esw10gACLACEArpFlagsLength_Object=MibTableColumn
gel2esw10gACLACEArpFlagsLength=_Gel2esw10gACLACEArpFlagsLength_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,25),_Gel2esw10gACLACEArpFlagsLength_Type())
gel2esw10gACLACEArpFlagsLength.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEArpFlagsLength.setStatus(_A)
class _Gel2esw10gACLACEArpFlagsIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACEArpFlagsIp_Type.__name__=_C
_Gel2esw10gACLACEArpFlagsIp_Object=MibTableColumn
gel2esw10gACLACEArpFlagsIp=_Gel2esw10gACLACEArpFlagsIp_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,26),_Gel2esw10gACLACEArpFlagsIp_Type())
gel2esw10gACLACEArpFlagsIp.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEArpFlagsIp.setStatus(_A)
class _Gel2esw10gACLACEArpFlagsEthernet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACEArpFlagsEthernet_Type.__name__=_C
_Gel2esw10gACLACEArpFlagsEthernet_Object=MibTableColumn
gel2esw10gACLACEArpFlagsEthernet=_Gel2esw10gACLACEArpFlagsEthernet_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,27),_Gel2esw10gACLACEArpFlagsEthernet_Type())
gel2esw10gACLACEArpFlagsEthernet.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEArpFlagsEthernet.setStatus(_A)
class _Gel2esw10gACLACESIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gACLACESIPType_Type.__name__=_C
_Gel2esw10gACLACESIPType_Object=MibTableColumn
gel2esw10gACLACESIPType=_Gel2esw10gACLACESIPType_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,28),_Gel2esw10gACLACESIPType_Type())
gel2esw10gACLACESIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACESIPType.setStatus(_A)
_Gel2esw10gACLACESIPIPAddress_Type=IpAddress
_Gel2esw10gACLACESIPIPAddress_Object=MibTableColumn
gel2esw10gACLACESIPIPAddress=_Gel2esw10gACLACESIPIPAddress_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,29),_Gel2esw10gACLACESIPIPAddress_Type())
gel2esw10gACLACESIPIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACESIPIPAddress.setStatus(_A)
class _Gel2esw10gACLACESIPNetworkPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Gel2esw10gACLACESIPNetworkPrefix_Type.__name__=_C
_Gel2esw10gACLACESIPNetworkPrefix_Object=MibTableColumn
gel2esw10gACLACESIPNetworkPrefix=_Gel2esw10gACLACESIPNetworkPrefix_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,30),_Gel2esw10gACLACESIPNetworkPrefix_Type())
gel2esw10gACLACESIPNetworkPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACESIPNetworkPrefix.setStatus(_A)
class _Gel2esw10gACLACEDIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gACLACEDIPType_Type.__name__=_C
_Gel2esw10gACLACEDIPType_Object=MibTableColumn
gel2esw10gACLACEDIPType=_Gel2esw10gACLACEDIPType_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,32),_Gel2esw10gACLACEDIPType_Type())
gel2esw10gACLACEDIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEDIPType.setStatus(_A)
_Gel2esw10gACLACEDIPIPAddress_Type=IpAddress
_Gel2esw10gACLACEDIPIPAddress_Object=MibTableColumn
gel2esw10gACLACEDIPIPAddress=_Gel2esw10gACLACEDIPIPAddress_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,33),_Gel2esw10gACLACEDIPIPAddress_Type())
gel2esw10gACLACEDIPIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEDIPIPAddress.setStatus(_A)
class _Gel2esw10gACLACEDIPNetworkPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Gel2esw10gACLACEDIPNetworkPrefix_Type.__name__=_C
_Gel2esw10gACLACEDIPNetworkPrefix_Object=MibTableColumn
gel2esw10gACLACEDIPNetworkPrefix=_Gel2esw10gACLACEDIPNetworkPrefix_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,34),_Gel2esw10gACLACEDIPNetworkPrefix_Type())
gel2esw10gACLACEDIPNetworkPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEDIPNetworkPrefix.setStatus(_A)
class _Gel2esw10gACLACEIPProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Gel2esw10gACLACEIPProtocol_Type.__name__=_C
_Gel2esw10gACLACEIPProtocol_Object=MibTableColumn
gel2esw10gACLACEIPProtocol=_Gel2esw10gACLACEIPProtocol_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,36),_Gel2esw10gACLACEIPProtocol_Type())
gel2esw10gACLACEIPProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEIPProtocol.setStatus(_A)
class _Gel2esw10gACLACEIPFlagsTTL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACEIPFlagsTTL_Type.__name__=_C
_Gel2esw10gACLACEIPFlagsTTL_Object=MibTableColumn
gel2esw10gACLACEIPFlagsTTL=_Gel2esw10gACLACEIPFlagsTTL_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,37),_Gel2esw10gACLACEIPFlagsTTL_Type())
gel2esw10gACLACEIPFlagsTTL.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEIPFlagsTTL.setStatus(_A)
class _Gel2esw10gACLACEIPFlagsOptions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACEIPFlagsOptions_Type.__name__=_C
_Gel2esw10gACLACEIPFlagsOptions_Object=MibTableColumn
gel2esw10gACLACEIPFlagsOptions=_Gel2esw10gACLACEIPFlagsOptions_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,38),_Gel2esw10gACLACEIPFlagsOptions_Type())
gel2esw10gACLACEIPFlagsOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEIPFlagsOptions.setStatus(_A)
class _Gel2esw10gACLACEIPFlagsFragment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACEIPFlagsFragment_Type.__name__=_C
_Gel2esw10gACLACEIPFlagsFragment_Object=MibTableColumn
gel2esw10gACLACEIPFlagsFragment=_Gel2esw10gACLACEIPFlagsFragment_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,39),_Gel2esw10gACLACEIPFlagsFragment_Type())
gel2esw10gACLACEIPFlagsFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEIPFlagsFragment.setStatus(_A)
class _Gel2esw10gACLACEICMPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Gel2esw10gACLACEICMPType_Type.__name__=_C
_Gel2esw10gACLACEICMPType_Object=MibTableColumn
gel2esw10gACLACEICMPType=_Gel2esw10gACLACEICMPType_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,40),_Gel2esw10gACLACEICMPType_Type())
gel2esw10gACLACEICMPType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEICMPType.setStatus(_A)
class _Gel2esw10gACLACEICMPCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Gel2esw10gACLACEICMPCode_Type.__name__=_C
_Gel2esw10gACLACEICMPCode_Object=MibTableColumn
gel2esw10gACLACEICMPCode=_Gel2esw10gACLACEICMPCode_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,41),_Gel2esw10gACLACEICMPCode_Type())
gel2esw10gACLACEICMPCode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEICMPCode.setStatus(_A)
class _Gel2esw10gACLACESourcePortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Gel2esw10gACLACESourcePortMin_Type.__name__=_C
_Gel2esw10gACLACESourcePortMin_Object=MibTableColumn
gel2esw10gACLACESourcePortMin=_Gel2esw10gACLACESourcePortMin_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,42),_Gel2esw10gACLACESourcePortMin_Type())
gel2esw10gACLACESourcePortMin.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACESourcePortMin.setStatus(_A)
class _Gel2esw10gACLACESourcePortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Gel2esw10gACLACESourcePortMax_Type.__name__=_C
_Gel2esw10gACLACESourcePortMax_Object=MibTableColumn
gel2esw10gACLACESourcePortMax=_Gel2esw10gACLACESourcePortMax_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,43),_Gel2esw10gACLACESourcePortMax_Type())
gel2esw10gACLACESourcePortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACESourcePortMax.setStatus(_A)
class _Gel2esw10gACLACEDestPortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Gel2esw10gACLACEDestPortMin_Type.__name__=_C
_Gel2esw10gACLACEDestPortMin_Object=MibTableColumn
gel2esw10gACLACEDestPortMin=_Gel2esw10gACLACEDestPortMin_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,44),_Gel2esw10gACLACEDestPortMin_Type())
gel2esw10gACLACEDestPortMin.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEDestPortMin.setStatus(_A)
class _Gel2esw10gACLACEDestPortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Gel2esw10gACLACEDestPortMax_Type.__name__=_C
_Gel2esw10gACLACEDestPortMax_Object=MibTableColumn
gel2esw10gACLACEDestPortMax=_Gel2esw10gACLACEDestPortMax_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,45),_Gel2esw10gACLACEDestPortMax_Type())
gel2esw10gACLACEDestPortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEDestPortMax.setStatus(_A)
class _Gel2esw10gACLACETCPFlagsFin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACETCPFlagsFin_Type.__name__=_C
_Gel2esw10gACLACETCPFlagsFin_Object=MibTableColumn
gel2esw10gACLACETCPFlagsFin=_Gel2esw10gACLACETCPFlagsFin_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,46),_Gel2esw10gACLACETCPFlagsFin_Type())
gel2esw10gACLACETCPFlagsFin.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACETCPFlagsFin.setStatus(_A)
class _Gel2esw10gACLACETCPFlagsSyn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACETCPFlagsSyn_Type.__name__=_C
_Gel2esw10gACLACETCPFlagsSyn_Object=MibTableColumn
gel2esw10gACLACETCPFlagsSyn=_Gel2esw10gACLACETCPFlagsSyn_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,47),_Gel2esw10gACLACETCPFlagsSyn_Type())
gel2esw10gACLACETCPFlagsSyn.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACETCPFlagsSyn.setStatus(_A)
class _Gel2esw10gACLACETCPFlagsRst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACETCPFlagsRst_Type.__name__=_C
_Gel2esw10gACLACETCPFlagsRst_Object=MibTableColumn
gel2esw10gACLACETCPFlagsRst=_Gel2esw10gACLACETCPFlagsRst_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,48),_Gel2esw10gACLACETCPFlagsRst_Type())
gel2esw10gACLACETCPFlagsRst.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACETCPFlagsRst.setStatus(_A)
class _Gel2esw10gACLACETCPFlagsPsh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACETCPFlagsPsh_Type.__name__=_C
_Gel2esw10gACLACETCPFlagsPsh_Object=MibTableColumn
gel2esw10gACLACETCPFlagsPsh=_Gel2esw10gACLACETCPFlagsPsh_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,49),_Gel2esw10gACLACETCPFlagsPsh_Type())
gel2esw10gACLACETCPFlagsPsh.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACETCPFlagsPsh.setStatus(_A)
class _Gel2esw10gACLACETCPFlagsAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACETCPFlagsAck_Type.__name__=_C
_Gel2esw10gACLACETCPFlagsAck_Object=MibTableColumn
gel2esw10gACLACETCPFlagsAck=_Gel2esw10gACLACETCPFlagsAck_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,50),_Gel2esw10gACLACETCPFlagsAck_Type())
gel2esw10gACLACETCPFlagsAck.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACETCPFlagsAck.setStatus(_A)
class _Gel2esw10gACLACETCPFlagsUrg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gACLACETCPFlagsUrg_Type.__name__=_C
_Gel2esw10gACLACETCPFlagsUrg_Object=MibTableColumn
gel2esw10gACLACETCPFlagsUrg=_Gel2esw10gACLACETCPFlagsUrg_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,51),_Gel2esw10gACLACETCPFlagsUrg_Type())
gel2esw10gACLACETCPFlagsUrg.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACETCPFlagsUrg.setStatus(_A)
class _Gel2esw10gACLACERowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw10gACLACERowStatus_Type.__name__=_C
_Gel2esw10gACLACERowStatus_Object=MibTableColumn
gel2esw10gACLACERowStatus=_Gel2esw10gACLACERowStatus_Object((1,3,6,1,4,1,5205,2,51,2,9,3,2,1,66),_Gel2esw10gACLACERowStatus_Type())
gel2esw10gACLACERowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACERowStatus.setStatus(_A)
class _Gel2esw10gACLACEClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gACLACEClear_Type.__name__=_C
_Gel2esw10gACLACEClear_Object=MibScalar
gel2esw10gACLACEClear=_Gel2esw10gACLACEClear_Object((1,3,6,1,4,1,5205,2,51,2,9,3,3),_Gel2esw10gACLACEClear_Type())
gel2esw10gACLACEClear.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEClear.setStatus(_A)
class _Gel2esw10gACLACEMoveACEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Gel2esw10gACLACEMoveACEID_Type.__name__=_C
_Gel2esw10gACLACEMoveACEID_Object=MibScalar
gel2esw10gACLACEMoveACEID=_Gel2esw10gACLACEMoveACEID_Object((1,3,6,1,4,1,5205,2,51,2,9,3,4),_Gel2esw10gACLACEMoveACEID_Type())
gel2esw10gACLACEMoveACEID.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEMoveACEID.setStatus(_A)
class _Gel2esw10gACLACEMoveNextACEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Gel2esw10gACLACEMoveNextACEID_Type.__name__=_C
_Gel2esw10gACLACEMoveNextACEID_Object=MibScalar
gel2esw10gACLACEMoveNextACEID=_Gel2esw10gACLACEMoveNextACEID_Object((1,3,6,1,4,1,5205,2,51,2,9,3,5),_Gel2esw10gACLACEMoveNextACEID_Type())
gel2esw10gACLACEMoveNextACEID.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gACLACEMoveNextACEID.setStatus(_A)
_Gel2esw10gACLACEStatusTable_Object=MibTable
gel2esw10gACLACEStatusTable=_Gel2esw10gACLACEStatusTable_Object((1,3,6,1,4,1,5205,2,51,2,9,3,6))
if mibBuilder.loadTexts:gel2esw10gACLACEStatusTable.setStatus(_A)
_Gel2esw10gACLACEStatusEntry_Object=MibTableRow
gel2esw10gACLACEStatusEntry=_Gel2esw10gACLACEStatusEntry_Object((1,3,6,1,4,1,5205,2,51,2,9,3,6,1))
gel2esw10gACLACEStatusEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:gel2esw10gACLACEStatusEntry.setStatus(_A)
class _Gel2esw10gACLACEStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Gel2esw10gACLACEStatusIndex_Type.__name__=_C
_Gel2esw10gACLACEStatusIndex_Object=MibTableColumn
gel2esw10gACLACEStatusIndex=_Gel2esw10gACLACEStatusIndex_Object((1,3,6,1,4,1,5205,2,51,2,9,3,6,1,1),_Gel2esw10gACLACEStatusIndex_Type())
gel2esw10gACLACEStatusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gACLACEStatusIndex.setStatus(_A)
_Gel2esw10gACLACEStatusUser_Type=DisplayString
_Gel2esw10gACLACEStatusUser_Object=MibTableColumn
gel2esw10gACLACEStatusUser=_Gel2esw10gACLACEStatusUser_Object((1,3,6,1,4,1,5205,2,51,2,9,3,6,1,2),_Gel2esw10gACLACEStatusUser_Type())
gel2esw10gACLACEStatusUser.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gACLACEStatusUser.setStatus(_A)
class _Gel2esw10gACLACEStatusID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Gel2esw10gACLACEStatusID_Type.__name__=_C
_Gel2esw10gACLACEStatusID_Object=MibTableColumn
gel2esw10gACLACEStatusID=_Gel2esw10gACLACEStatusID_Object((1,3,6,1,4,1,5205,2,51,2,9,3,6,1,3),_Gel2esw10gACLACEStatusID_Type())
gel2esw10gACLACEStatusID.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gACLACEStatusID.setStatus(_A)
_Gel2esw10gACLACEStatusIngressPort_Type=DisplayString
_Gel2esw10gACLACEStatusIngressPort_Object=MibTableColumn
gel2esw10gACLACEStatusIngressPort=_Gel2esw10gACLACEStatusIngressPort_Object((1,3,6,1,4,1,5205,2,51,2,9,3,6,1,4),_Gel2esw10gACLACEStatusIngressPort_Type())
gel2esw10gACLACEStatusIngressPort.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gACLACEStatusIngressPort.setStatus(_A)
_Gel2esw10gACLACEStatusFrameType_Type=DisplayString
_Gel2esw10gACLACEStatusFrameType_Object=MibTableColumn
gel2esw10gACLACEStatusFrameType=_Gel2esw10gACLACEStatusFrameType_Object((1,3,6,1,4,1,5205,2,51,2,9,3,6,1,5),_Gel2esw10gACLACEStatusFrameType_Type())
gel2esw10gACLACEStatusFrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gACLACEStatusFrameType.setStatus(_A)
_Gel2esw10gACLACEStatusAction_Type=DisplayString
_Gel2esw10gACLACEStatusAction_Object=MibTableColumn
gel2esw10gACLACEStatusAction=_Gel2esw10gACLACEStatusAction_Object((1,3,6,1,4,1,5205,2,51,2,9,3,6,1,6),_Gel2esw10gACLACEStatusAction_Type())
gel2esw10gACLACEStatusAction.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gACLACEStatusAction.setStatus(_A)
_Gel2esw10gACLACEStatusRateLimiter_Type=DisplayString
_Gel2esw10gACLACEStatusRateLimiter_Object=MibTableColumn
gel2esw10gACLACEStatusRateLimiter=_Gel2esw10gACLACEStatusRateLimiter_Object((1,3,6,1,4,1,5205,2,51,2,9,3,6,1,7),_Gel2esw10gACLACEStatusRateLimiter_Type())
gel2esw10gACLACEStatusRateLimiter.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gACLACEStatusRateLimiter.setStatus(_A)
_Gel2esw10gACLACEStatusPortCopy_Type=DisplayString
_Gel2esw10gACLACEStatusPortCopy_Object=MibTableColumn
gel2esw10gACLACEStatusPortCopy=_Gel2esw10gACLACEStatusPortCopy_Object((1,3,6,1,4,1,5205,2,51,2,9,3,6,1,8),_Gel2esw10gACLACEStatusPortCopy_Type())
gel2esw10gACLACEStatusPortCopy.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gACLACEStatusPortCopy.setStatus(_A)
_Gel2esw10gACLACEStatusMirror_Type=DisplayString
_Gel2esw10gACLACEStatusMirror_Object=MibTableColumn
gel2esw10gACLACEStatusMirror=_Gel2esw10gACLACEStatusMirror_Object((1,3,6,1,4,1,5205,2,51,2,9,3,6,1,9),_Gel2esw10gACLACEStatusMirror_Type())
gel2esw10gACLACEStatusMirror.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gACLACEStatusMirror.setStatus(_A)
_Gel2esw10gACLACEStatusCPU_Type=DisplayString
_Gel2esw10gACLACEStatusCPU_Object=MibTableColumn
gel2esw10gACLACEStatusCPU=_Gel2esw10gACLACEStatusCPU_Object((1,3,6,1,4,1,5205,2,51,2,9,3,6,1,10),_Gel2esw10gACLACEStatusCPU_Type())
gel2esw10gACLACEStatusCPU.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gACLACEStatusCPU.setStatus(_A)
_Gel2esw10gACLACEStatusCounter_Type=Counter32
_Gel2esw10gACLACEStatusCounter_Object=MibTableColumn
gel2esw10gACLACEStatusCounter=_Gel2esw10gACLACEStatusCounter_Object((1,3,6,1,4,1,5205,2,51,2,9,3,6,1,11),_Gel2esw10gACLACEStatusCounter_Type())
gel2esw10gACLACEStatusCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gACLACEStatusCounter.setStatus(_A)
_Gel2esw10gACLACEStatusConflict_Type=DisplayString
_Gel2esw10gACLACEStatusConflict_Object=MibTableColumn
gel2esw10gACLACEStatusConflict=_Gel2esw10gACLACEStatusConflict_Object((1,3,6,1,4,1,5205,2,51,2,9,3,6,1,12),_Gel2esw10gACLACEStatusConflict_Type())
gel2esw10gACLACEStatusConflict.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gACLACEStatusConflict.setStatus(_A)
_Gel2esw10gSecurity_ObjectIdentity=ObjectIdentity
gel2esw10gSecurity=_Gel2esw10gSecurity_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3))
_Gel2esw10gIPSourceGuard_ObjectIdentity=ObjectIdentity
gel2esw10gIPSourceGuard=_Gel2esw10gIPSourceGuard_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,1))
_Gel2esw10gIPSourceGuardConf_ObjectIdentity=ObjectIdentity
gel2esw10gIPSourceGuardConf=_Gel2esw10gIPSourceGuardConf_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,1,1))
class _Gel2esw10gIPSourceGuardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gIPSourceGuardMode_Type.__name__=_C
_Gel2esw10gIPSourceGuardMode_Object=MibScalar
gel2esw10gIPSourceGuardMode=_Gel2esw10gIPSourceGuardMode_Object((1,3,6,1,4,1,5205,2,51,3,1,1,1),_Gel2esw10gIPSourceGuardMode_Type())
gel2esw10gIPSourceGuardMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardMode.setStatus(_A)
_Gel2esw10gIPSourceGuardPortConfigTable_Object=MibTable
gel2esw10gIPSourceGuardPortConfigTable=_Gel2esw10gIPSourceGuardPortConfigTable_Object((1,3,6,1,4,1,5205,2,51,3,1,1,2))
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardPortConfigTable.setStatus(_A)
_Gel2esw10gIPSourceGuardPortConfigEntry_Object=MibTableRow
gel2esw10gIPSourceGuardPortConfigEntry=_Gel2esw10gIPSourceGuardPortConfigEntry_Object((1,3,6,1,4,1,5205,2,51,3,1,1,2,1))
gel2esw10gIPSourceGuardPortConfigEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardPortConfigEntry.setStatus(_A)
class _Gel2esw10gIPSourceGuardPortConfigPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gIPSourceGuardPortConfigPort_Type.__name__=_C
_Gel2esw10gIPSourceGuardPortConfigPort_Object=MibTableColumn
gel2esw10gIPSourceGuardPortConfigPort=_Gel2esw10gIPSourceGuardPortConfigPort_Object((1,3,6,1,4,1,5205,2,51,3,1,1,2,1,1),_Gel2esw10gIPSourceGuardPortConfigPort_Type())
gel2esw10gIPSourceGuardPortConfigPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardPortConfigPort.setStatus(_A)
class _Gel2esw10gIPSourceGuardPortConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gIPSourceGuardPortConfigMode_Type.__name__=_C
_Gel2esw10gIPSourceGuardPortConfigMode_Object=MibTableColumn
gel2esw10gIPSourceGuardPortConfigMode=_Gel2esw10gIPSourceGuardPortConfigMode_Object((1,3,6,1,4,1,5205,2,51,3,1,1,2,1,2),_Gel2esw10gIPSourceGuardPortConfigMode_Type())
gel2esw10gIPSourceGuardPortConfigMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardPortConfigMode.setStatus(_A)
class _Gel2esw10gIPSourceGuardPortMaxDynamicClients_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2),ValueRangeConstraint(99,99))
_Gel2esw10gIPSourceGuardPortMaxDynamicClients_Type.__name__=_C
_Gel2esw10gIPSourceGuardPortMaxDynamicClients_Object=MibTableColumn
gel2esw10gIPSourceGuardPortMaxDynamicClients=_Gel2esw10gIPSourceGuardPortMaxDynamicClients_Object((1,3,6,1,4,1,5205,2,51,3,1,1,2,1,3),_Gel2esw10gIPSourceGuardPortMaxDynamicClients_Type())
gel2esw10gIPSourceGuardPortMaxDynamicClients.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardPortMaxDynamicClients.setStatus(_A)
_Gel2esw10gIPSourceGuardStatic_ObjectIdentity=ObjectIdentity
gel2esw10gIPSourceGuardStatic=_Gel2esw10gIPSourceGuardStatic_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,1,2))
class _Gel2esw10gIPSourceGuardStaticCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gIPSourceGuardStaticCreate_Type.__name__=_C
_Gel2esw10gIPSourceGuardStaticCreate_Object=MibScalar
gel2esw10gIPSourceGuardStaticCreate=_Gel2esw10gIPSourceGuardStaticCreate_Object((1,3,6,1,4,1,5205,2,51,3,1,2,1),_Gel2esw10gIPSourceGuardStaticCreate_Type())
gel2esw10gIPSourceGuardStaticCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardStaticCreate.setStatus(_A)
_Gel2esw10gIPSourceGuardStaticTable_Object=MibTable
gel2esw10gIPSourceGuardStaticTable=_Gel2esw10gIPSourceGuardStaticTable_Object((1,3,6,1,4,1,5205,2,51,3,1,2,2))
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardStaticTable.setStatus(_A)
_Gel2esw10gIPSourceGuardStaticEntry_Object=MibTableRow
gel2esw10gIPSourceGuardStaticEntry=_Gel2esw10gIPSourceGuardStaticEntry_Object((1,3,6,1,4,1,5205,2,51,3,1,2,2,1))
gel2esw10gIPSourceGuardStaticEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardStaticEntry.setStatus(_A)
class _Gel2esw10gIPSourceGuardStaticIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_Gel2esw10gIPSourceGuardStaticIndex_Type.__name__=_C
_Gel2esw10gIPSourceGuardStaticIndex_Object=MibTableColumn
gel2esw10gIPSourceGuardStaticIndex=_Gel2esw10gIPSourceGuardStaticIndex_Object((1,3,6,1,4,1,5205,2,51,3,1,2,2,1,1),_Gel2esw10gIPSourceGuardStaticIndex_Type())
gel2esw10gIPSourceGuardStaticIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardStaticIndex.setStatus(_A)
class _Gel2esw10gIPSourceGuardStaticPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gIPSourceGuardStaticPort_Type.__name__=_C
_Gel2esw10gIPSourceGuardStaticPort_Object=MibTableColumn
gel2esw10gIPSourceGuardStaticPort=_Gel2esw10gIPSourceGuardStaticPort_Object((1,3,6,1,4,1,5205,2,51,3,1,2,2,1,2),_Gel2esw10gIPSourceGuardStaticPort_Type())
gel2esw10gIPSourceGuardStaticPort.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardStaticPort.setStatus(_A)
class _Gel2esw10gIPSourceGuardStaticVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw10gIPSourceGuardStaticVLANId_Type.__name__=_C
_Gel2esw10gIPSourceGuardStaticVLANId_Object=MibTableColumn
gel2esw10gIPSourceGuardStaticVLANId=_Gel2esw10gIPSourceGuardStaticVLANId_Object((1,3,6,1,4,1,5205,2,51,3,1,2,2,1,3),_Gel2esw10gIPSourceGuardStaticVLANId_Type())
gel2esw10gIPSourceGuardStaticVLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardStaticVLANId.setStatus(_A)
_Gel2esw10gIPSourceGuardStaticIPAddress_Type=IpAddress
_Gel2esw10gIPSourceGuardStaticIPAddress_Object=MibTableColumn
gel2esw10gIPSourceGuardStaticIPAddress=_Gel2esw10gIPSourceGuardStaticIPAddress_Object((1,3,6,1,4,1,5205,2,51,3,1,2,2,1,4),_Gel2esw10gIPSourceGuardStaticIPAddress_Type())
gel2esw10gIPSourceGuardStaticIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardStaticIPAddress.setStatus(_A)
_Gel2esw10gIPSourceGuardStaticMACAddress_Type=MacAddress
_Gel2esw10gIPSourceGuardStaticMACAddress_Object=MibTableColumn
gel2esw10gIPSourceGuardStaticMACAddress=_Gel2esw10gIPSourceGuardStaticMACAddress_Object((1,3,6,1,4,1,5205,2,51,3,1,2,2,1,5),_Gel2esw10gIPSourceGuardStaticMACAddress_Type())
gel2esw10gIPSourceGuardStaticMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardStaticMACAddress.setStatus(_A)
class _Gel2esw10gIPSourceGuardStaticRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw10gIPSourceGuardStaticRowStatus_Type.__name__=_C
_Gel2esw10gIPSourceGuardStaticRowStatus_Object=MibTableColumn
gel2esw10gIPSourceGuardStaticRowStatus=_Gel2esw10gIPSourceGuardStaticRowStatus_Object((1,3,6,1,4,1,5205,2,51,3,1,2,2,1,6),_Gel2esw10gIPSourceGuardStaticRowStatus_Type())
gel2esw10gIPSourceGuardStaticRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardStaticRowStatus.setStatus(_A)
_Gel2esw10gIPSourceGuardDynamicTable_Object=MibTable
gel2esw10gIPSourceGuardDynamicTable=_Gel2esw10gIPSourceGuardDynamicTable_Object((1,3,6,1,4,1,5205,2,51,3,1,3))
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardDynamicTable.setStatus(_A)
_Gel2esw10gIPSourceGuardDynamicEntry_Object=MibTableRow
gel2esw10gIPSourceGuardDynamicEntry=_Gel2esw10gIPSourceGuardDynamicEntry_Object((1,3,6,1,4,1,5205,2,51,3,1,3,1))
gel2esw10gIPSourceGuardDynamicEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardDynamicEntry.setStatus(_A)
class _Gel2esw10gIPSourceGuardDynamicIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gIPSourceGuardDynamicIndex_Type.__name__=_C
_Gel2esw10gIPSourceGuardDynamicIndex_Object=MibTableColumn
gel2esw10gIPSourceGuardDynamicIndex=_Gel2esw10gIPSourceGuardDynamicIndex_Object((1,3,6,1,4,1,5205,2,51,3,1,3,1,1),_Gel2esw10gIPSourceGuardDynamicIndex_Type())
gel2esw10gIPSourceGuardDynamicIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardDynamicIndex.setStatus(_A)
class _Gel2esw10gIPSourceGuardDynamicPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Gel2esw10gIPSourceGuardDynamicPort_Type.__name__=_C
_Gel2esw10gIPSourceGuardDynamicPort_Object=MibTableColumn
gel2esw10gIPSourceGuardDynamicPort=_Gel2esw10gIPSourceGuardDynamicPort_Object((1,3,6,1,4,1,5205,2,51,3,1,3,1,2),_Gel2esw10gIPSourceGuardDynamicPort_Type())
gel2esw10gIPSourceGuardDynamicPort.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardDynamicPort.setStatus(_A)
class _Gel2esw10gIPSourceGuardDynamicVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw10gIPSourceGuardDynamicVLANId_Type.__name__=_C
_Gel2esw10gIPSourceGuardDynamicVLANId_Object=MibTableColumn
gel2esw10gIPSourceGuardDynamicVLANId=_Gel2esw10gIPSourceGuardDynamicVLANId_Object((1,3,6,1,4,1,5205,2,51,3,1,3,1,3),_Gel2esw10gIPSourceGuardDynamicVLANId_Type())
gel2esw10gIPSourceGuardDynamicVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardDynamicVLANId.setStatus(_A)
_Gel2esw10gIPSourceGuardDynamicIPAddress_Type=IpAddress
_Gel2esw10gIPSourceGuardDynamicIPAddress_Object=MibTableColumn
gel2esw10gIPSourceGuardDynamicIPAddress=_Gel2esw10gIPSourceGuardDynamicIPAddress_Object((1,3,6,1,4,1,5205,2,51,3,1,3,1,4),_Gel2esw10gIPSourceGuardDynamicIPAddress_Type())
gel2esw10gIPSourceGuardDynamicIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardDynamicIPAddress.setStatus(_A)
_Gel2esw10gIPSourceGuardDynamicMACAddress_Type=MacAddress
_Gel2esw10gIPSourceGuardDynamicMACAddress_Object=MibTableColumn
gel2esw10gIPSourceGuardDynamicMACAddress=_Gel2esw10gIPSourceGuardDynamicMACAddress_Object((1,3,6,1,4,1,5205,2,51,3,1,3,1,5),_Gel2esw10gIPSourceGuardDynamicMACAddress_Type())
gel2esw10gIPSourceGuardDynamicMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gIPSourceGuardDynamicMACAddress.setStatus(_A)
_Gel2esw10gARPInspection_ObjectIdentity=ObjectIdentity
gel2esw10gARPInspection=_Gel2esw10gARPInspection_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,2))
_Gel2esw10gARPInspectionConf_ObjectIdentity=ObjectIdentity
gel2esw10gARPInspectionConf=_Gel2esw10gARPInspectionConf_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,2,1))
class _Gel2esw10gARPInspectionConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gARPInspectionConfMode_Type.__name__=_C
_Gel2esw10gARPInspectionConfMode_Object=MibScalar
gel2esw10gARPInspectionConfMode=_Gel2esw10gARPInspectionConfMode_Object((1,3,6,1,4,1,5205,2,51,3,2,1,1),_Gel2esw10gARPInspectionConfMode_Type())
gel2esw10gARPInspectionConfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gARPInspectionConfMode.setStatus(_A)
_Gel2esw10gARPInspectionConfTable_Object=MibTable
gel2esw10gARPInspectionConfTable=_Gel2esw10gARPInspectionConfTable_Object((1,3,6,1,4,1,5205,2,51,3,2,1,2))
if mibBuilder.loadTexts:gel2esw10gARPInspectionConfTable.setStatus(_A)
_Gel2esw10gARPInspectionConfEntry_Object=MibTableRow
gel2esw10gARPInspectionConfEntry=_Gel2esw10gARPInspectionConfEntry_Object((1,3,6,1,4,1,5205,2,51,3,2,1,2,1))
gel2esw10gARPInspectionConfEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:gel2esw10gARPInspectionConfEntry.setStatus(_A)
class _Gel2esw10gARPInspectionConfPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gARPInspectionConfPortIndex_Type.__name__=_C
_Gel2esw10gARPInspectionConfPortIndex_Object=MibTableColumn
gel2esw10gARPInspectionConfPortIndex=_Gel2esw10gARPInspectionConfPortIndex_Object((1,3,6,1,4,1,5205,2,51,3,2,1,2,1,1),_Gel2esw10gARPInspectionConfPortIndex_Type())
gel2esw10gARPInspectionConfPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gARPInspectionConfPortIndex.setStatus(_A)
class _Gel2esw10gARPInspectionConfPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gARPInspectionConfPortMode_Type.__name__=_C
_Gel2esw10gARPInspectionConfPortMode_Object=MibTableColumn
gel2esw10gARPInspectionConfPortMode=_Gel2esw10gARPInspectionConfPortMode_Object((1,3,6,1,4,1,5205,2,51,3,2,1,2,1,2),_Gel2esw10gARPInspectionConfPortMode_Type())
gel2esw10gARPInspectionConfPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gARPInspectionConfPortMode.setStatus(_A)
_Gel2esw10gARPInspectionStatic_ObjectIdentity=ObjectIdentity
gel2esw10gARPInspectionStatic=_Gel2esw10gARPInspectionStatic_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,2,2))
class _Gel2esw10gARPInspectionStaticCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gARPInspectionStaticCreate_Type.__name__=_C
_Gel2esw10gARPInspectionStaticCreate_Object=MibScalar
gel2esw10gARPInspectionStaticCreate=_Gel2esw10gARPInspectionStaticCreate_Object((1,3,6,1,4,1,5205,2,51,3,2,2,1),_Gel2esw10gARPInspectionStaticCreate_Type())
gel2esw10gARPInspectionStaticCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gARPInspectionStaticCreate.setStatus(_A)
_Gel2esw10gARPInspectionStaticTable_Object=MibTable
gel2esw10gARPInspectionStaticTable=_Gel2esw10gARPInspectionStaticTable_Object((1,3,6,1,4,1,5205,2,51,3,2,2,2))
if mibBuilder.loadTexts:gel2esw10gARPInspectionStaticTable.setStatus(_A)
_Gel2esw10gARPInspectionStaticEntry_Object=MibTableRow
gel2esw10gARPInspectionStaticEntry=_Gel2esw10gARPInspectionStaticEntry_Object((1,3,6,1,4,1,5205,2,51,3,2,2,2,1))
gel2esw10gARPInspectionStaticEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:gel2esw10gARPInspectionStaticEntry.setStatus(_A)
class _Gel2esw10gARPInspectionStaticIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gARPInspectionStaticIndex_Type.__name__=_C
_Gel2esw10gARPInspectionStaticIndex_Object=MibTableColumn
gel2esw10gARPInspectionStaticIndex=_Gel2esw10gARPInspectionStaticIndex_Object((1,3,6,1,4,1,5205,2,51,3,2,2,2,1,1),_Gel2esw10gARPInspectionStaticIndex_Type())
gel2esw10gARPInspectionStaticIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gARPInspectionStaticIndex.setStatus(_A)
class _Gel2esw10gARPInspectionStaticPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gARPInspectionStaticPort_Type.__name__=_C
_Gel2esw10gARPInspectionStaticPort_Object=MibTableColumn
gel2esw10gARPInspectionStaticPort=_Gel2esw10gARPInspectionStaticPort_Object((1,3,6,1,4,1,5205,2,51,3,2,2,2,1,2),_Gel2esw10gARPInspectionStaticPort_Type())
gel2esw10gARPInspectionStaticPort.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gARPInspectionStaticPort.setStatus(_A)
class _Gel2esw10gARPInspectionStaticVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw10gARPInspectionStaticVLANId_Type.__name__=_C
_Gel2esw10gARPInspectionStaticVLANId_Object=MibTableColumn
gel2esw10gARPInspectionStaticVLANId=_Gel2esw10gARPInspectionStaticVLANId_Object((1,3,6,1,4,1,5205,2,51,3,2,2,2,1,3),_Gel2esw10gARPInspectionStaticVLANId_Type())
gel2esw10gARPInspectionStaticVLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gARPInspectionStaticVLANId.setStatus(_A)
_Gel2esw10gARPInspectionStaticIPAddress_Type=IpAddress
_Gel2esw10gARPInspectionStaticIPAddress_Object=MibTableColumn
gel2esw10gARPInspectionStaticIPAddress=_Gel2esw10gARPInspectionStaticIPAddress_Object((1,3,6,1,4,1,5205,2,51,3,2,2,2,1,4),_Gel2esw10gARPInspectionStaticIPAddress_Type())
gel2esw10gARPInspectionStaticIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gARPInspectionStaticIPAddress.setStatus(_A)
_Gel2esw10gARPInspectionStaticMACAddress_Type=MacAddress
_Gel2esw10gARPInspectionStaticMACAddress_Object=MibTableColumn
gel2esw10gARPInspectionStaticMACAddress=_Gel2esw10gARPInspectionStaticMACAddress_Object((1,3,6,1,4,1,5205,2,51,3,2,2,2,1,5),_Gel2esw10gARPInspectionStaticMACAddress_Type())
gel2esw10gARPInspectionStaticMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gARPInspectionStaticMACAddress.setStatus(_A)
class _Gel2esw10gARPInspectionStaticRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw10gARPInspectionStaticRowStatus_Type.__name__=_C
_Gel2esw10gARPInspectionStaticRowStatus_Object=MibTableColumn
gel2esw10gARPInspectionStaticRowStatus=_Gel2esw10gARPInspectionStaticRowStatus_Object((1,3,6,1,4,1,5205,2,51,3,2,2,2,1,6),_Gel2esw10gARPInspectionStaticRowStatus_Type())
gel2esw10gARPInspectionStaticRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gARPInspectionStaticRowStatus.setStatus(_A)
_Gel2esw10gARPInspectionDynamicTable_Object=MibTable
gel2esw10gARPInspectionDynamicTable=_Gel2esw10gARPInspectionDynamicTable_Object((1,3,6,1,4,1,5205,2,51,3,2,3))
if mibBuilder.loadTexts:gel2esw10gARPInspectionDynamicTable.setStatus(_A)
_Gel2esw10gARPInspectionDynamicEntry_Object=MibTableRow
gel2esw10gARPInspectionDynamicEntry=_Gel2esw10gARPInspectionDynamicEntry_Object((1,3,6,1,4,1,5205,2,51,3,2,3,1))
gel2esw10gARPInspectionDynamicEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:gel2esw10gARPInspectionDynamicEntry.setStatus(_A)
class _Gel2esw10gARPInspectionDynamicIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gARPInspectionDynamicIndex_Type.__name__=_C
_Gel2esw10gARPInspectionDynamicIndex_Object=MibTableColumn
gel2esw10gARPInspectionDynamicIndex=_Gel2esw10gARPInspectionDynamicIndex_Object((1,3,6,1,4,1,5205,2,51,3,2,3,1,1),_Gel2esw10gARPInspectionDynamicIndex_Type())
gel2esw10gARPInspectionDynamicIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gARPInspectionDynamicIndex.setStatus(_A)
class _Gel2esw10gARPInspectionDynamicPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gARPInspectionDynamicPort_Type.__name__=_C
_Gel2esw10gARPInspectionDynamicPort_Object=MibTableColumn
gel2esw10gARPInspectionDynamicPort=_Gel2esw10gARPInspectionDynamicPort_Object((1,3,6,1,4,1,5205,2,51,3,2,3,1,2),_Gel2esw10gARPInspectionDynamicPort_Type())
gel2esw10gARPInspectionDynamicPort.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gARPInspectionDynamicPort.setStatus(_A)
class _Gel2esw10gARPInspectionDynamicVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw10gARPInspectionDynamicVLANId_Type.__name__=_C
_Gel2esw10gARPInspectionDynamicVLANId_Object=MibTableColumn
gel2esw10gARPInspectionDynamicVLANId=_Gel2esw10gARPInspectionDynamicVLANId_Object((1,3,6,1,4,1,5205,2,51,3,2,3,1,3),_Gel2esw10gARPInspectionDynamicVLANId_Type())
gel2esw10gARPInspectionDynamicVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gARPInspectionDynamicVLANId.setStatus(_A)
_Gel2esw10gARPInspectionDynamicIPAddress_Type=IpAddress
_Gel2esw10gARPInspectionDynamicIPAddress_Object=MibTableColumn
gel2esw10gARPInspectionDynamicIPAddress=_Gel2esw10gARPInspectionDynamicIPAddress_Object((1,3,6,1,4,1,5205,2,51,3,2,3,1,4),_Gel2esw10gARPInspectionDynamicIPAddress_Type())
gel2esw10gARPInspectionDynamicIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gARPInspectionDynamicIPAddress.setStatus(_A)
_Gel2esw10gARPInspectionDynamicMACAddress_Type=MacAddress
_Gel2esw10gARPInspectionDynamicMACAddress_Object=MibTableColumn
gel2esw10gARPInspectionDynamicMACAddress=_Gel2esw10gARPInspectionDynamicMACAddress_Object((1,3,6,1,4,1,5205,2,51,3,2,3,1,5),_Gel2esw10gARPInspectionDynamicMACAddress_Type())
gel2esw10gARPInspectionDynamicMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gARPInspectionDynamicMACAddress.setStatus(_A)
_Gel2esw10gDHCPSnooping_ObjectIdentity=ObjectIdentity
gel2esw10gDHCPSnooping=_Gel2esw10gDHCPSnooping_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,3))
_Gel2esw10gDHCPSnoopingConf_ObjectIdentity=ObjectIdentity
gel2esw10gDHCPSnoopingConf=_Gel2esw10gDHCPSnoopingConf_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,3,1))
class _Gel2esw10gDHCPSnoopingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gDHCPSnoopingMode_Type.__name__=_C
_Gel2esw10gDHCPSnoopingMode_Object=MibScalar
gel2esw10gDHCPSnoopingMode=_Gel2esw10gDHCPSnoopingMode_Object((1,3,6,1,4,1,5205,2,51,3,3,1,1),_Gel2esw10gDHCPSnoopingMode_Type())
gel2esw10gDHCPSnoopingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingMode.setStatus(_A)
_Gel2esw10gDHCPSnoopingPortModeConfigurationTable_Object=MibTable
gel2esw10gDHCPSnoopingPortModeConfigurationTable=_Gel2esw10gDHCPSnoopingPortModeConfigurationTable_Object((1,3,6,1,4,1,5205,2,51,3,3,1,2))
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingPortModeConfigurationTable.setStatus(_A)
_Gel2esw10gDHCPSnoopingPortModeConfigurationEntry_Object=MibTableRow
gel2esw10gDHCPSnoopingPortModeConfigurationEntry=_Gel2esw10gDHCPSnoopingPortModeConfigurationEntry_Object((1,3,6,1,4,1,5205,2,51,3,3,1,2,1))
gel2esw10gDHCPSnoopingPortModeConfigurationEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingPortModeConfigurationEntry.setStatus(_A)
class _Gel2esw10gDHCPSnoopingPortModeConfigurationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gDHCPSnoopingPortModeConfigurationPort_Type.__name__=_C
_Gel2esw10gDHCPSnoopingPortModeConfigurationPort_Object=MibTableColumn
gel2esw10gDHCPSnoopingPortModeConfigurationPort=_Gel2esw10gDHCPSnoopingPortModeConfigurationPort_Object((1,3,6,1,4,1,5205,2,51,3,3,1,2,1,1),_Gel2esw10gDHCPSnoopingPortModeConfigurationPort_Type())
gel2esw10gDHCPSnoopingPortModeConfigurationPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingPortModeConfigurationPort.setStatus(_A)
class _Gel2esw10gDHCPSnoopingPortModeConfigurationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gDHCPSnoopingPortModeConfigurationMode_Type.__name__=_C
_Gel2esw10gDHCPSnoopingPortModeConfigurationMode_Object=MibTableColumn
gel2esw10gDHCPSnoopingPortModeConfigurationMode=_Gel2esw10gDHCPSnoopingPortModeConfigurationMode_Object((1,3,6,1,4,1,5205,2,51,3,3,1,2,1,2),_Gel2esw10gDHCPSnoopingPortModeConfigurationMode_Type())
gel2esw10gDHCPSnoopingPortModeConfigurationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingPortModeConfigurationMode.setStatus(_A)
_Gel2esw10gDHCPSnoopingStatisticsTable_Object=MibTable
gel2esw10gDHCPSnoopingStatisticsTable=_Gel2esw10gDHCPSnoopingStatisticsTable_Object((1,3,6,1,4,1,5205,2,51,3,3,2))
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingStatisticsTable.setStatus(_A)
_Gel2esw10gDHCPSnoopingStatisticsEntry_Object=MibTableRow
gel2esw10gDHCPSnoopingStatisticsEntry=_Gel2esw10gDHCPSnoopingStatisticsEntry_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1))
gel2esw10gDHCPSnoopingStatisticsEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingStatisticsEntry.setStatus(_A)
class _Gel2esw10gDHCPSnoopingStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gDHCPSnoopingStatisticsPort_Type.__name__=_C
_Gel2esw10gDHCPSnoopingStatisticsPort_Object=MibTableColumn
gel2esw10gDHCPSnoopingStatisticsPort=_Gel2esw10gDHCPSnoopingStatisticsPort_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,1),_Gel2esw10gDHCPSnoopingStatisticsPort_Type())
gel2esw10gDHCPSnoopingStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingStatisticsPort.setStatus(_A)
class _Gel2esw10gDHCPSnoopingStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gDHCPSnoopingStatisticsClear_Type.__name__=_C
_Gel2esw10gDHCPSnoopingStatisticsClear_Object=MibTableColumn
gel2esw10gDHCPSnoopingStatisticsClear=_Gel2esw10gDHCPSnoopingStatisticsClear_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,2),_Gel2esw10gDHCPSnoopingStatisticsClear_Type())
gel2esw10gDHCPSnoopingStatisticsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingStatisticsClear.setStatus(_A)
_Gel2esw10gDHCPSnoopingRxDiscover_Type=Counter32
_Gel2esw10gDHCPSnoopingRxDiscover_Object=MibTableColumn
gel2esw10gDHCPSnoopingRxDiscover=_Gel2esw10gDHCPSnoopingRxDiscover_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,3),_Gel2esw10gDHCPSnoopingRxDiscover_Type())
gel2esw10gDHCPSnoopingRxDiscover.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingRxDiscover.setStatus(_A)
_Gel2esw10gDHCPSnoopingRxOffer_Type=Counter32
_Gel2esw10gDHCPSnoopingRxOffer_Object=MibTableColumn
gel2esw10gDHCPSnoopingRxOffer=_Gel2esw10gDHCPSnoopingRxOffer_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,4),_Gel2esw10gDHCPSnoopingRxOffer_Type())
gel2esw10gDHCPSnoopingRxOffer.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingRxOffer.setStatus(_A)
_Gel2esw10gDHCPSnoopingRxRequest_Type=Counter32
_Gel2esw10gDHCPSnoopingRxRequest_Object=MibTableColumn
gel2esw10gDHCPSnoopingRxRequest=_Gel2esw10gDHCPSnoopingRxRequest_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,5),_Gel2esw10gDHCPSnoopingRxRequest_Type())
gel2esw10gDHCPSnoopingRxRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingRxRequest.setStatus(_A)
_Gel2esw10gDHCPSnoopingRxDecline_Type=Counter32
_Gel2esw10gDHCPSnoopingRxDecline_Object=MibTableColumn
gel2esw10gDHCPSnoopingRxDecline=_Gel2esw10gDHCPSnoopingRxDecline_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,6),_Gel2esw10gDHCPSnoopingRxDecline_Type())
gel2esw10gDHCPSnoopingRxDecline.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingRxDecline.setStatus(_A)
_Gel2esw10gDHCPSnoopingRxACK_Type=Counter32
_Gel2esw10gDHCPSnoopingRxACK_Object=MibTableColumn
gel2esw10gDHCPSnoopingRxACK=_Gel2esw10gDHCPSnoopingRxACK_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,7),_Gel2esw10gDHCPSnoopingRxACK_Type())
gel2esw10gDHCPSnoopingRxACK.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingRxACK.setStatus(_A)
_Gel2esw10gDHCPSnoopingRxNAK_Type=Counter32
_Gel2esw10gDHCPSnoopingRxNAK_Object=MibTableColumn
gel2esw10gDHCPSnoopingRxNAK=_Gel2esw10gDHCPSnoopingRxNAK_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,8),_Gel2esw10gDHCPSnoopingRxNAK_Type())
gel2esw10gDHCPSnoopingRxNAK.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingRxNAK.setStatus(_A)
_Gel2esw10gDHCPSnoopingRxRelease_Type=Counter32
_Gel2esw10gDHCPSnoopingRxRelease_Object=MibTableColumn
gel2esw10gDHCPSnoopingRxRelease=_Gel2esw10gDHCPSnoopingRxRelease_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,9),_Gel2esw10gDHCPSnoopingRxRelease_Type())
gel2esw10gDHCPSnoopingRxRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingRxRelease.setStatus(_A)
_Gel2esw10gDHCPSnoopingRxInform_Type=Counter32
_Gel2esw10gDHCPSnoopingRxInform_Object=MibTableColumn
gel2esw10gDHCPSnoopingRxInform=_Gel2esw10gDHCPSnoopingRxInform_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,10),_Gel2esw10gDHCPSnoopingRxInform_Type())
gel2esw10gDHCPSnoopingRxInform.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingRxInform.setStatus(_A)
_Gel2esw10gDHCPSnoopingRxLeaseQuery_Type=Counter32
_Gel2esw10gDHCPSnoopingRxLeaseQuery_Object=MibTableColumn
gel2esw10gDHCPSnoopingRxLeaseQuery=_Gel2esw10gDHCPSnoopingRxLeaseQuery_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,11),_Gel2esw10gDHCPSnoopingRxLeaseQuery_Type())
gel2esw10gDHCPSnoopingRxLeaseQuery.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingRxLeaseQuery.setStatus(_A)
_Gel2esw10gDHCPSnoopingRxLeaseUnassigned_Type=Counter32
_Gel2esw10gDHCPSnoopingRxLeaseUnassigned_Object=MibTableColumn
gel2esw10gDHCPSnoopingRxLeaseUnassigned=_Gel2esw10gDHCPSnoopingRxLeaseUnassigned_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,12),_Gel2esw10gDHCPSnoopingRxLeaseUnassigned_Type())
gel2esw10gDHCPSnoopingRxLeaseUnassigned.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingRxLeaseUnassigned.setStatus(_A)
_Gel2esw10gDHCPSnoopingRxLeaseUnknown_Type=Counter32
_Gel2esw10gDHCPSnoopingRxLeaseUnknown_Object=MibTableColumn
gel2esw10gDHCPSnoopingRxLeaseUnknown=_Gel2esw10gDHCPSnoopingRxLeaseUnknown_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,13),_Gel2esw10gDHCPSnoopingRxLeaseUnknown_Type())
gel2esw10gDHCPSnoopingRxLeaseUnknown.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingRxLeaseUnknown.setStatus(_A)
_Gel2esw10gDHCPSnoopingRxLeaseActive_Type=Counter32
_Gel2esw10gDHCPSnoopingRxLeaseActive_Object=MibTableColumn
gel2esw10gDHCPSnoopingRxLeaseActive=_Gel2esw10gDHCPSnoopingRxLeaseActive_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,14),_Gel2esw10gDHCPSnoopingRxLeaseActive_Type())
gel2esw10gDHCPSnoopingRxLeaseActive.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingRxLeaseActive.setStatus(_A)
_Gel2esw10gDHCPSnoopingTxDiscover_Type=Counter32
_Gel2esw10gDHCPSnoopingTxDiscover_Object=MibTableColumn
gel2esw10gDHCPSnoopingTxDiscover=_Gel2esw10gDHCPSnoopingTxDiscover_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,15),_Gel2esw10gDHCPSnoopingTxDiscover_Type())
gel2esw10gDHCPSnoopingTxDiscover.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingTxDiscover.setStatus(_A)
_Gel2esw10gDHCPSnoopingTxOffer_Type=Counter32
_Gel2esw10gDHCPSnoopingTxOffer_Object=MibTableColumn
gel2esw10gDHCPSnoopingTxOffer=_Gel2esw10gDHCPSnoopingTxOffer_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,16),_Gel2esw10gDHCPSnoopingTxOffer_Type())
gel2esw10gDHCPSnoopingTxOffer.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingTxOffer.setStatus(_A)
_Gel2esw10gDHCPSnoopingTxRequest_Type=Counter32
_Gel2esw10gDHCPSnoopingTxRequest_Object=MibTableColumn
gel2esw10gDHCPSnoopingTxRequest=_Gel2esw10gDHCPSnoopingTxRequest_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,17),_Gel2esw10gDHCPSnoopingTxRequest_Type())
gel2esw10gDHCPSnoopingTxRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingTxRequest.setStatus(_A)
_Gel2esw10gDHCPSnoopingTxDecline_Type=Counter32
_Gel2esw10gDHCPSnoopingTxDecline_Object=MibTableColumn
gel2esw10gDHCPSnoopingTxDecline=_Gel2esw10gDHCPSnoopingTxDecline_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,18),_Gel2esw10gDHCPSnoopingTxDecline_Type())
gel2esw10gDHCPSnoopingTxDecline.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingTxDecline.setStatus(_A)
_Gel2esw10gDHCPSnoopingTxACK_Type=Counter32
_Gel2esw10gDHCPSnoopingTxACK_Object=MibTableColumn
gel2esw10gDHCPSnoopingTxACK=_Gel2esw10gDHCPSnoopingTxACK_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,19),_Gel2esw10gDHCPSnoopingTxACK_Type())
gel2esw10gDHCPSnoopingTxACK.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingTxACK.setStatus(_A)
_Gel2esw10gDHCPSnoopingTxNAK_Type=Counter32
_Gel2esw10gDHCPSnoopingTxNAK_Object=MibTableColumn
gel2esw10gDHCPSnoopingTxNAK=_Gel2esw10gDHCPSnoopingTxNAK_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,20),_Gel2esw10gDHCPSnoopingTxNAK_Type())
gel2esw10gDHCPSnoopingTxNAK.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingTxNAK.setStatus(_A)
_Gel2esw10gDHCPSnoopingTxRelease_Type=Counter32
_Gel2esw10gDHCPSnoopingTxRelease_Object=MibTableColumn
gel2esw10gDHCPSnoopingTxRelease=_Gel2esw10gDHCPSnoopingTxRelease_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,21),_Gel2esw10gDHCPSnoopingTxRelease_Type())
gel2esw10gDHCPSnoopingTxRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingTxRelease.setStatus(_A)
_Gel2esw10gDHCPSnoopingTxInform_Type=Counter32
_Gel2esw10gDHCPSnoopingTxInform_Object=MibTableColumn
gel2esw10gDHCPSnoopingTxInform=_Gel2esw10gDHCPSnoopingTxInform_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,22),_Gel2esw10gDHCPSnoopingTxInform_Type())
gel2esw10gDHCPSnoopingTxInform.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingTxInform.setStatus(_A)
_Gel2esw10gDHCPSnoopingTxLeaseQuery_Type=Counter32
_Gel2esw10gDHCPSnoopingTxLeaseQuery_Object=MibTableColumn
gel2esw10gDHCPSnoopingTxLeaseQuery=_Gel2esw10gDHCPSnoopingTxLeaseQuery_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,23),_Gel2esw10gDHCPSnoopingTxLeaseQuery_Type())
gel2esw10gDHCPSnoopingTxLeaseQuery.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingTxLeaseQuery.setStatus(_A)
_Gel2esw10gDHCPSnoopingTxLeaseUnassigned_Type=Counter32
_Gel2esw10gDHCPSnoopingTxLeaseUnassigned_Object=MibTableColumn
gel2esw10gDHCPSnoopingTxLeaseUnassigned=_Gel2esw10gDHCPSnoopingTxLeaseUnassigned_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,24),_Gel2esw10gDHCPSnoopingTxLeaseUnassigned_Type())
gel2esw10gDHCPSnoopingTxLeaseUnassigned.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingTxLeaseUnassigned.setStatus(_A)
_Gel2esw10gDHCPSnoopingTxLeaseUnknown_Type=Counter32
_Gel2esw10gDHCPSnoopingTxLeaseUnknown_Object=MibTableColumn
gel2esw10gDHCPSnoopingTxLeaseUnknown=_Gel2esw10gDHCPSnoopingTxLeaseUnknown_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,25),_Gel2esw10gDHCPSnoopingTxLeaseUnknown_Type())
gel2esw10gDHCPSnoopingTxLeaseUnknown.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingTxLeaseUnknown.setStatus(_A)
_Gel2esw10gDHCPSnoopingTxLeaseActive_Type=Counter32
_Gel2esw10gDHCPSnoopingTxLeaseActive_Object=MibTableColumn
gel2esw10gDHCPSnoopingTxLeaseActive=_Gel2esw10gDHCPSnoopingTxLeaseActive_Object((1,3,6,1,4,1,5205,2,51,3,3,2,1,26),_Gel2esw10gDHCPSnoopingTxLeaseActive_Type())
gel2esw10gDHCPSnoopingTxLeaseActive.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gDHCPSnoopingTxLeaseActive.setStatus(_A)
_Gel2esw10gDHCPRelay_ObjectIdentity=ObjectIdentity
gel2esw10gDHCPRelay=_Gel2esw10gDHCPRelay_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,4))
_Gel2esw10gDHCPRelayConfiguration_ObjectIdentity=ObjectIdentity
gel2esw10gDHCPRelayConfiguration=_Gel2esw10gDHCPRelayConfiguration_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,4,1))
class _Gel2esw10gDHCPRelayMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gDHCPRelayMode_Type.__name__=_C
_Gel2esw10gDHCPRelayMode_Object=MibScalar
gel2esw10gDHCPRelayMode=_Gel2esw10gDHCPRelayMode_Object((1,3,6,1,4,1,5205,2,51,3,4,1,1),_Gel2esw10gDHCPRelayMode_Type())
gel2esw10gDHCPRelayMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gDHCPRelayMode.setStatus(_A)
_Gel2esw10gDHCPRelayServer_Type=IpAddress
_Gel2esw10gDHCPRelayServer_Object=MibScalar
gel2esw10gDHCPRelayServer=_Gel2esw10gDHCPRelayServer_Object((1,3,6,1,4,1,5205,2,51,3,4,1,2),_Gel2esw10gDHCPRelayServer_Type())
gel2esw10gDHCPRelayServer.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gDHCPRelayServer.setStatus(_A)
class _Gel2esw10gDHCPRelayInformationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gDHCPRelayInformationMode_Type.__name__=_C
_Gel2esw10gDHCPRelayInformationMode_Object=MibScalar
gel2esw10gDHCPRelayInformationMode=_Gel2esw10gDHCPRelayInformationMode_Object((1,3,6,1,4,1,5205,2,51,3,4,1,3),_Gel2esw10gDHCPRelayInformationMode_Type())
gel2esw10gDHCPRelayInformationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gDHCPRelayInformationMode.setStatus(_A)
class _Gel2esw10gDHCPRelayInformationPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw10gDHCPRelayInformationPolicy_Type.__name__=_C
_Gel2esw10gDHCPRelayInformationPolicy_Object=MibScalar
gel2esw10gDHCPRelayInformationPolicy=_Gel2esw10gDHCPRelayInformationPolicy_Object((1,3,6,1,4,1,5205,2,51,3,4,1,4),_Gel2esw10gDHCPRelayInformationPolicy_Type())
gel2esw10gDHCPRelayInformationPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gDHCPRelayInformationPolicy.setStatus(_A)
_Gel2esw10gDHCPRelayStatistics_ObjectIdentity=ObjectIdentity
gel2esw10gDHCPRelayStatistics=_Gel2esw10gDHCPRelayStatistics_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,4,2))
_Gel2esw10gDHCPRelayServerStatistics_ObjectIdentity=ObjectIdentity
gel2esw10gDHCPRelayServerStatistics=_Gel2esw10gDHCPRelayServerStatistics_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,4,2,1))
_Gel2esw10gServerStatTransmitToServer_Type=Counter32
_Gel2esw10gServerStatTransmitToServer_Object=MibScalar
gel2esw10gServerStatTransmitToServer=_Gel2esw10gServerStatTransmitToServer_Object((1,3,6,1,4,1,5205,2,51,3,4,2,1,1),_Gel2esw10gServerStatTransmitToServer_Type())
gel2esw10gServerStatTransmitToServer.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gServerStatTransmitToServer.setStatus(_A)
_Gel2esw10gServerStatTransmitError_Type=Counter32
_Gel2esw10gServerStatTransmitError_Object=MibScalar
gel2esw10gServerStatTransmitError=_Gel2esw10gServerStatTransmitError_Object((1,3,6,1,4,1,5205,2,51,3,4,2,1,2),_Gel2esw10gServerStatTransmitError_Type())
gel2esw10gServerStatTransmitError.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gServerStatTransmitError.setStatus(_A)
_Gel2esw10gServerStatReceiveFromServer_Type=Counter32
_Gel2esw10gServerStatReceiveFromServer_Object=MibScalar
gel2esw10gServerStatReceiveFromServer=_Gel2esw10gServerStatReceiveFromServer_Object((1,3,6,1,4,1,5205,2,51,3,4,2,1,3),_Gel2esw10gServerStatReceiveFromServer_Type())
gel2esw10gServerStatReceiveFromServer.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gServerStatReceiveFromServer.setStatus(_A)
_Gel2esw10gServerStatReceiveMissingAgentOption_Type=Counter32
_Gel2esw10gServerStatReceiveMissingAgentOption_Object=MibScalar
gel2esw10gServerStatReceiveMissingAgentOption=_Gel2esw10gServerStatReceiveMissingAgentOption_Object((1,3,6,1,4,1,5205,2,51,3,4,2,1,4),_Gel2esw10gServerStatReceiveMissingAgentOption_Type())
gel2esw10gServerStatReceiveMissingAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gServerStatReceiveMissingAgentOption.setStatus(_A)
_Gel2esw10gServerStatReceiveMissingCircuitID_Type=Counter32
_Gel2esw10gServerStatReceiveMissingCircuitID_Object=MibScalar
gel2esw10gServerStatReceiveMissingCircuitID=_Gel2esw10gServerStatReceiveMissingCircuitID_Object((1,3,6,1,4,1,5205,2,51,3,4,2,1,5),_Gel2esw10gServerStatReceiveMissingCircuitID_Type())
gel2esw10gServerStatReceiveMissingCircuitID.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gServerStatReceiveMissingCircuitID.setStatus(_A)
_Gel2esw10gServerStatReceiveMissingRemoteID_Type=Counter32
_Gel2esw10gServerStatReceiveMissingRemoteID_Object=MibScalar
gel2esw10gServerStatReceiveMissingRemoteID=_Gel2esw10gServerStatReceiveMissingRemoteID_Object((1,3,6,1,4,1,5205,2,51,3,4,2,1,6),_Gel2esw10gServerStatReceiveMissingRemoteID_Type())
gel2esw10gServerStatReceiveMissingRemoteID.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gServerStatReceiveMissingRemoteID.setStatus(_A)
_Gel2esw10gServerStatReceiveBadCircuitID_Type=Counter32
_Gel2esw10gServerStatReceiveBadCircuitID_Object=MibScalar
gel2esw10gServerStatReceiveBadCircuitID=_Gel2esw10gServerStatReceiveBadCircuitID_Object((1,3,6,1,4,1,5205,2,51,3,4,2,1,7),_Gel2esw10gServerStatReceiveBadCircuitID_Type())
gel2esw10gServerStatReceiveBadCircuitID.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gServerStatReceiveBadCircuitID.setStatus(_A)
_Gel2esw10gServerStatReceiveBadRemoteID_Type=Counter32
_Gel2esw10gServerStatReceiveBadRemoteID_Object=MibScalar
gel2esw10gServerStatReceiveBadRemoteID=_Gel2esw10gServerStatReceiveBadRemoteID_Object((1,3,6,1,4,1,5205,2,51,3,4,2,1,8),_Gel2esw10gServerStatReceiveBadRemoteID_Type())
gel2esw10gServerStatReceiveBadRemoteID.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gServerStatReceiveBadRemoteID.setStatus(_A)
_Gel2esw10gDHCPRelayClientStatistics_ObjectIdentity=ObjectIdentity
gel2esw10gDHCPRelayClientStatistics=_Gel2esw10gDHCPRelayClientStatistics_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,4,2,2))
_Gel2esw10gClientStatTransmitToClient_Type=Counter32
_Gel2esw10gClientStatTransmitToClient_Object=MibScalar
gel2esw10gClientStatTransmitToClient=_Gel2esw10gClientStatTransmitToClient_Object((1,3,6,1,4,1,5205,2,51,3,4,2,2,1),_Gel2esw10gClientStatTransmitToClient_Type())
gel2esw10gClientStatTransmitToClient.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gClientStatTransmitToClient.setStatus(_A)
_Gel2esw10gClientStatTransmitError_Type=Counter32
_Gel2esw10gClientStatTransmitError_Object=MibScalar
gel2esw10gClientStatTransmitError=_Gel2esw10gClientStatTransmitError_Object((1,3,6,1,4,1,5205,2,51,3,4,2,2,2),_Gel2esw10gClientStatTransmitError_Type())
gel2esw10gClientStatTransmitError.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gClientStatTransmitError.setStatus(_A)
_Gel2esw10gClientStatReceivefromClient_Type=Counter32
_Gel2esw10gClientStatReceivefromClient_Object=MibScalar
gel2esw10gClientStatReceivefromClient=_Gel2esw10gClientStatReceivefromClient_Object((1,3,6,1,4,1,5205,2,51,3,4,2,2,3),_Gel2esw10gClientStatReceivefromClient_Type())
gel2esw10gClientStatReceivefromClient.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gClientStatReceivefromClient.setStatus(_A)
_Gel2esw10gClientStatReceiveAgentOption_Type=Counter32
_Gel2esw10gClientStatReceiveAgentOption_Object=MibScalar
gel2esw10gClientStatReceiveAgentOption=_Gel2esw10gClientStatReceiveAgentOption_Object((1,3,6,1,4,1,5205,2,51,3,4,2,2,4),_Gel2esw10gClientStatReceiveAgentOption_Type())
gel2esw10gClientStatReceiveAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gClientStatReceiveAgentOption.setStatus(_A)
_Gel2esw10gClientStatReplaceAgentOption_Type=Counter32
_Gel2esw10gClientStatReplaceAgentOption_Object=MibScalar
gel2esw10gClientStatReplaceAgentOption=_Gel2esw10gClientStatReplaceAgentOption_Object((1,3,6,1,4,1,5205,2,51,3,4,2,2,5),_Gel2esw10gClientStatReplaceAgentOption_Type())
gel2esw10gClientStatReplaceAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gClientStatReplaceAgentOption.setStatus(_A)
_Gel2esw10gClientStatKeepAgentOption_Type=Counter32
_Gel2esw10gClientStatKeepAgentOption_Object=MibScalar
gel2esw10gClientStatKeepAgentOption=_Gel2esw10gClientStatKeepAgentOption_Object((1,3,6,1,4,1,5205,2,51,3,4,2,2,6),_Gel2esw10gClientStatKeepAgentOption_Type())
gel2esw10gClientStatKeepAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gClientStatKeepAgentOption.setStatus(_A)
_Gel2esw10gClientStatDropAgentOption_Type=Counter32
_Gel2esw10gClientStatDropAgentOption_Object=MibScalar
gel2esw10gClientStatDropAgentOption=_Gel2esw10gClientStatDropAgentOption_Object((1,3,6,1,4,1,5205,2,51,3,4,2,2,7),_Gel2esw10gClientStatDropAgentOption_Type())
gel2esw10gClientStatDropAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gClientStatDropAgentOption.setStatus(_A)
_Gel2esw10gPortSecurity_ObjectIdentity=ObjectIdentity
gel2esw10gPortSecurity=_Gel2esw10gPortSecurity_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,5))
_Gel2esw10gPortSecLimitCtrl_ObjectIdentity=ObjectIdentity
gel2esw10gPortSecLimitCtrl=_Gel2esw10gPortSecLimitCtrl_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,5,1))
_Gel2esw10gPortSecLimitCtrlSystemConf_ObjectIdentity=ObjectIdentity
gel2esw10gPortSecLimitCtrlSystemConf=_Gel2esw10gPortSecLimitCtrlSystemConf_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,5,1,1))
class _Gel2esw10gPortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortSecurityMode_Type.__name__=_C
_Gel2esw10gPortSecurityMode_Object=MibScalar
gel2esw10gPortSecurityMode=_Gel2esw10gPortSecurityMode_Object((1,3,6,1,4,1,5205,2,51,3,5,1,1,1),_Gel2esw10gPortSecurityMode_Type())
gel2esw10gPortSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortSecurityMode.setStatus(_A)
class _Gel2esw10gPortSecurityAging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortSecurityAging_Type.__name__=_C
_Gel2esw10gPortSecurityAging_Object=MibScalar
gel2esw10gPortSecurityAging=_Gel2esw10gPortSecurityAging_Object((1,3,6,1,4,1,5205,2,51,3,5,1,1,2),_Gel2esw10gPortSecurityAging_Type())
gel2esw10gPortSecurityAging.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortSecurityAging.setStatus(_A)
class _Gel2esw10gPortSecurityAgingPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10000000))
_Gel2esw10gPortSecurityAgingPeriod_Type.__name__=_C
_Gel2esw10gPortSecurityAgingPeriod_Object=MibScalar
gel2esw10gPortSecurityAgingPeriod=_Gel2esw10gPortSecurityAgingPeriod_Object((1,3,6,1,4,1,5205,2,51,3,5,1,1,3),_Gel2esw10gPortSecurityAgingPeriod_Type())
gel2esw10gPortSecurityAgingPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortSecurityAgingPeriod.setStatus(_A)
_Gel2esw10gPortSecLimitCtrlTable_Object=MibTable
gel2esw10gPortSecLimitCtrlTable=_Gel2esw10gPortSecLimitCtrlTable_Object((1,3,6,1,4,1,5205,2,51,3,5,1,2))
if mibBuilder.loadTexts:gel2esw10gPortSecLimitCtrlTable.setStatus(_A)
_Gel2esw10gPortSecLimitCtrlEntry_Object=MibTableRow
gel2esw10gPortSecLimitCtrlEntry=_Gel2esw10gPortSecLimitCtrlEntry_Object((1,3,6,1,4,1,5205,2,51,3,5,1,2,1))
gel2esw10gPortSecLimitCtrlEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:gel2esw10gPortSecLimitCtrlEntry.setStatus(_A)
class _Gel2esw10gPortSecLimitCtrlPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gPortSecLimitCtrlPort_Type.__name__=_C
_Gel2esw10gPortSecLimitCtrlPort_Object=MibTableColumn
gel2esw10gPortSecLimitCtrlPort=_Gel2esw10gPortSecLimitCtrlPort_Object((1,3,6,1,4,1,5205,2,51,3,5,1,2,1,1),_Gel2esw10gPortSecLimitCtrlPort_Type())
gel2esw10gPortSecLimitCtrlPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gPortSecLimitCtrlPort.setStatus(_A)
class _Gel2esw10gPortSecLimitCtrlPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortSecLimitCtrlPortMode_Type.__name__=_C
_Gel2esw10gPortSecLimitCtrlPortMode_Object=MibTableColumn
gel2esw10gPortSecLimitCtrlPortMode=_Gel2esw10gPortSecLimitCtrlPortMode_Object((1,3,6,1,4,1,5205,2,51,3,5,1,2,1,2),_Gel2esw10gPortSecLimitCtrlPortMode_Type())
gel2esw10gPortSecLimitCtrlPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortSecLimitCtrlPortMode.setStatus(_A)
class _Gel2esw10gPortSecLimitCtrlPortLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Gel2esw10gPortSecLimitCtrlPortLimit_Type.__name__=_C
_Gel2esw10gPortSecLimitCtrlPortLimit_Object=MibTableColumn
gel2esw10gPortSecLimitCtrlPortLimit=_Gel2esw10gPortSecLimitCtrlPortLimit_Object((1,3,6,1,4,1,5205,2,51,3,5,1,2,1,3),_Gel2esw10gPortSecLimitCtrlPortLimit_Type())
gel2esw10gPortSecLimitCtrlPortLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortSecLimitCtrlPortLimit.setStatus(_A)
class _Gel2esw10gPortSecLimitCtrlPortAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw10gPortSecLimitCtrlPortAction_Type.__name__=_C
_Gel2esw10gPortSecLimitCtrlPortAction_Object=MibTableColumn
gel2esw10gPortSecLimitCtrlPortAction=_Gel2esw10gPortSecLimitCtrlPortAction_Object((1,3,6,1,4,1,5205,2,51,3,5,1,2,1,4),_Gel2esw10gPortSecLimitCtrlPortAction_Type())
gel2esw10gPortSecLimitCtrlPortAction.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortSecLimitCtrlPortAction.setStatus(_A)
_Gel2esw10gPortSecLimitCtrlPortState_Type=DisplayString
_Gel2esw10gPortSecLimitCtrlPortState_Object=MibTableColumn
gel2esw10gPortSecLimitCtrlPortState=_Gel2esw10gPortSecLimitCtrlPortState_Object((1,3,6,1,4,1,5205,2,51,3,5,1,2,1,5),_Gel2esw10gPortSecLimitCtrlPortState_Type())
gel2esw10gPortSecLimitCtrlPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortSecLimitCtrlPortState.setStatus(_A)
class _Gel2esw10gPortSecLimitCtrlPortReOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gPortSecLimitCtrlPortReOpen_Type.__name__=_C
_Gel2esw10gPortSecLimitCtrlPortReOpen_Object=MibTableColumn
gel2esw10gPortSecLimitCtrlPortReOpen=_Gel2esw10gPortSecLimitCtrlPortReOpen_Object((1,3,6,1,4,1,5205,2,51,3,5,1,2,1,6),_Gel2esw10gPortSecLimitCtrlPortReOpen_Type())
gel2esw10gPortSecLimitCtrlPortReOpen.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortSecLimitCtrlPortReOpen.setStatus(_A)
_Gel2esw10gPortSecSwitchStatusTable_Object=MibTable
gel2esw10gPortSecSwitchStatusTable=_Gel2esw10gPortSecSwitchStatusTable_Object((1,3,6,1,4,1,5205,2,51,3,5,2))
if mibBuilder.loadTexts:gel2esw10gPortSecSwitchStatusTable.setStatus(_A)
_Gel2esw10gPortSecSwitchStatusEntry_Object=MibTableRow
gel2esw10gPortSecSwitchStatusEntry=_Gel2esw10gPortSecSwitchStatusEntry_Object((1,3,6,1,4,1,5205,2,51,3,5,2,1))
gel2esw10gPortSecSwitchStatusEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:gel2esw10gPortSecSwitchStatusEntry.setStatus(_A)
class _Gel2esw10gPortSecSwitchStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gPortSecSwitchStatusPort_Type.__name__=_C
_Gel2esw10gPortSecSwitchStatusPort_Object=MibTableColumn
gel2esw10gPortSecSwitchStatusPort=_Gel2esw10gPortSecSwitchStatusPort_Object((1,3,6,1,4,1,5205,2,51,3,5,2,1,1),_Gel2esw10gPortSecSwitchStatusPort_Type())
gel2esw10gPortSecSwitchStatusPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gPortSecSwitchStatusPort.setStatus(_A)
_Gel2esw10gPortSecSwitchStatusUsers_Type=DisplayString
_Gel2esw10gPortSecSwitchStatusUsers_Object=MibTableColumn
gel2esw10gPortSecSwitchStatusUsers=_Gel2esw10gPortSecSwitchStatusUsers_Object((1,3,6,1,4,1,5205,2,51,3,5,2,1,2),_Gel2esw10gPortSecSwitchStatusUsers_Type())
gel2esw10gPortSecSwitchStatusUsers.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortSecSwitchStatusUsers.setStatus(_A)
_Gel2esw10gPortSecSwitchStatusState_Type=DisplayString
_Gel2esw10gPortSecSwitchStatusState_Object=MibTableColumn
gel2esw10gPortSecSwitchStatusState=_Gel2esw10gPortSecSwitchStatusState_Object((1,3,6,1,4,1,5205,2,51,3,5,2,1,3),_Gel2esw10gPortSecSwitchStatusState_Type())
gel2esw10gPortSecSwitchStatusState.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortSecSwitchStatusState.setStatus(_A)
class _Gel2esw10gPortSecSwitchStatusMACCountCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gPortSecSwitchStatusMACCountCurrent_Type.__name__=_C
_Gel2esw10gPortSecSwitchStatusMACCountCurrent_Object=MibTableColumn
gel2esw10gPortSecSwitchStatusMACCountCurrent=_Gel2esw10gPortSecSwitchStatusMACCountCurrent_Object((1,3,6,1,4,1,5205,2,51,3,5,2,1,4),_Gel2esw10gPortSecSwitchStatusMACCountCurrent_Type())
gel2esw10gPortSecSwitchStatusMACCountCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortSecSwitchStatusMACCountCurrent.setStatus(_A)
class _Gel2esw10gPortSecSwitchStatusMACCountLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gPortSecSwitchStatusMACCountLimit_Type.__name__=_C
_Gel2esw10gPortSecSwitchStatusMACCountLimit_Object=MibTableColumn
gel2esw10gPortSecSwitchStatusMACCountLimit=_Gel2esw10gPortSecSwitchStatusMACCountLimit_Object((1,3,6,1,4,1,5205,2,51,3,5,2,1,5),_Gel2esw10gPortSecSwitchStatusMACCountLimit_Type())
gel2esw10gPortSecSwitchStatusMACCountLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortSecSwitchStatusMACCountLimit.setStatus(_A)
_Gel2esw10gPortSecPortStatus_ObjectIdentity=ObjectIdentity
gel2esw10gPortSecPortStatus=_Gel2esw10gPortSecPortStatus_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,5,3))
class _Gel2esw10gPortSecPortStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gPortSecPortStatusPort_Type.__name__=_C
_Gel2esw10gPortSecPortStatusPort_Object=MibScalar
gel2esw10gPortSecPortStatusPort=_Gel2esw10gPortSecPortStatusPort_Object((1,3,6,1,4,1,5205,2,51,3,5,3,1),_Gel2esw10gPortSecPortStatusPort_Type())
gel2esw10gPortSecPortStatusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPortSecPortStatusPort.setStatus(_A)
_Gel2esw10gPortSecPortStatusTable_Object=MibTable
gel2esw10gPortSecPortStatusTable=_Gel2esw10gPortSecPortStatusTable_Object((1,3,6,1,4,1,5205,2,51,3,5,3,2))
if mibBuilder.loadTexts:gel2esw10gPortSecPortStatusTable.setStatus(_A)
_Gel2esw10gPortSecPortStatusEntry_Object=MibTableRow
gel2esw10gPortSecPortStatusEntry=_Gel2esw10gPortSecPortStatusEntry_Object((1,3,6,1,4,1,5205,2,51,3,5,3,2,1))
gel2esw10gPortSecPortStatusEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:gel2esw10gPortSecPortStatusEntry.setStatus(_A)
class _Gel2esw10gPortSecPortStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gPortSecPortStatusIndex_Type.__name__=_C
_Gel2esw10gPortSecPortStatusIndex_Object=MibTableColumn
gel2esw10gPortSecPortStatusIndex=_Gel2esw10gPortSecPortStatusIndex_Object((1,3,6,1,4,1,5205,2,51,3,5,3,2,1,1),_Gel2esw10gPortSecPortStatusIndex_Type())
gel2esw10gPortSecPortStatusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gPortSecPortStatusIndex.setStatus(_A)
_Gel2esw10gPortSecPortStatusMACAddress_Type=MacAddress
_Gel2esw10gPortSecPortStatusMACAddress_Object=MibTableColumn
gel2esw10gPortSecPortStatusMACAddress=_Gel2esw10gPortSecPortStatusMACAddress_Object((1,3,6,1,4,1,5205,2,51,3,5,3,2,1,2),_Gel2esw10gPortSecPortStatusMACAddress_Type())
gel2esw10gPortSecPortStatusMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortSecPortStatusMACAddress.setStatus(_A)
class _Gel2esw10gPortSecPortStatusVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw10gPortSecPortStatusVLANId_Type.__name__=_C
_Gel2esw10gPortSecPortStatusVLANId_Object=MibTableColumn
gel2esw10gPortSecPortStatusVLANId=_Gel2esw10gPortSecPortStatusVLANId_Object((1,3,6,1,4,1,5205,2,51,3,5,3,2,1,3),_Gel2esw10gPortSecPortStatusVLANId_Type())
gel2esw10gPortSecPortStatusVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortSecPortStatusVLANId.setStatus(_A)
_Gel2esw10gPortSecPortStatusState_Type=DisplayString
_Gel2esw10gPortSecPortStatusState_Object=MibTableColumn
gel2esw10gPortSecPortStatusState=_Gel2esw10gPortSecPortStatusState_Object((1,3,6,1,4,1,5205,2,51,3,5,3,2,1,4),_Gel2esw10gPortSecPortStatusState_Type())
gel2esw10gPortSecPortStatusState.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortSecPortStatusState.setStatus(_A)
_Gel2esw10gPortSecPortStatusTimeOfAddition_Type=DisplayString
_Gel2esw10gPortSecPortStatusTimeOfAddition_Object=MibTableColumn
gel2esw10gPortSecPortStatusTimeOfAddition=_Gel2esw10gPortSecPortStatusTimeOfAddition_Object((1,3,6,1,4,1,5205,2,51,3,5,3,2,1,5),_Gel2esw10gPortSecPortStatusTimeOfAddition_Type())
gel2esw10gPortSecPortStatusTimeOfAddition.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortSecPortStatusTimeOfAddition.setStatus(_A)
_Gel2esw10gPortSecPortStatusAgeAndHold_Type=DisplayString
_Gel2esw10gPortSecPortStatusAgeAndHold_Object=MibTableColumn
gel2esw10gPortSecPortStatusAgeAndHold=_Gel2esw10gPortSecPortStatusAgeAndHold_Object((1,3,6,1,4,1,5205,2,51,3,5,3,2,1,6),_Gel2esw10gPortSecPortStatusAgeAndHold_Type())
gel2esw10gPortSecPortStatusAgeAndHold.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPortSecPortStatusAgeAndHold.setStatus(_A)
_Gel2esw10gAccessManagement_ObjectIdentity=ObjectIdentity
gel2esw10gAccessManagement=_Gel2esw10gAccessManagement_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,6))
_Gel2esw10gAccessMgtConf_ObjectIdentity=ObjectIdentity
gel2esw10gAccessMgtConf=_Gel2esw10gAccessMgtConf_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,6,1))
class _Gel2esw10gAccessMgtConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gAccessMgtConfMode_Type.__name__=_C
_Gel2esw10gAccessMgtConfMode_Object=MibScalar
gel2esw10gAccessMgtConfMode=_Gel2esw10gAccessMgtConfMode_Object((1,3,6,1,4,1,5205,2,51,3,6,1,1),_Gel2esw10gAccessMgtConfMode_Type())
gel2esw10gAccessMgtConfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gAccessMgtConfMode.setStatus(_A)
class _Gel2esw10gAccessMgtConfCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gAccessMgtConfCreate_Type.__name__=_C
_Gel2esw10gAccessMgtConfCreate_Object=MibScalar
gel2esw10gAccessMgtConfCreate=_Gel2esw10gAccessMgtConfCreate_Object((1,3,6,1,4,1,5205,2,51,3,6,1,2),_Gel2esw10gAccessMgtConfCreate_Type())
gel2esw10gAccessMgtConfCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gAccessMgtConfCreate.setStatus(_A)
_Gel2esw10gAccessMgtConfTable_Object=MibTable
gel2esw10gAccessMgtConfTable=_Gel2esw10gAccessMgtConfTable_Object((1,3,6,1,4,1,5205,2,51,3,6,1,3))
if mibBuilder.loadTexts:gel2esw10gAccessMgtConfTable.setStatus(_A)
_Gel2esw10gAccessMgtConfEntry_Object=MibTableRow
gel2esw10gAccessMgtConfEntry=_Gel2esw10gAccessMgtConfEntry_Object((1,3,6,1,4,1,5205,2,51,3,6,1,3,1))
gel2esw10gAccessMgtConfEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:gel2esw10gAccessMgtConfEntry.setStatus(_A)
class _Gel2esw10gAccessMgtIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Gel2esw10gAccessMgtIndex_Type.__name__=_C
_Gel2esw10gAccessMgtIndex_Object=MibTableColumn
gel2esw10gAccessMgtIndex=_Gel2esw10gAccessMgtIndex_Object((1,3,6,1,4,1,5205,2,51,3,6,1,3,1,1),_Gel2esw10gAccessMgtIndex_Type())
gel2esw10gAccessMgtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gAccessMgtIndex.setStatus(_A)
class _Gel2esw10gAccessMgtAddresstype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gAccessMgtAddresstype_Type.__name__=_C
_Gel2esw10gAccessMgtAddresstype_Object=MibTableColumn
gel2esw10gAccessMgtAddresstype=_Gel2esw10gAccessMgtAddresstype_Object((1,3,6,1,4,1,5205,2,51,3,6,1,3,1,2),_Gel2esw10gAccessMgtAddresstype_Type())
gel2esw10gAccessMgtAddresstype.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gAccessMgtAddresstype.setStatus(_A)
_Gel2esw10gAccessMgtStartIpAddress_Type=DisplayString
_Gel2esw10gAccessMgtStartIpAddress_Object=MibTableColumn
gel2esw10gAccessMgtStartIpAddress=_Gel2esw10gAccessMgtStartIpAddress_Object((1,3,6,1,4,1,5205,2,51,3,6,1,3,1,3),_Gel2esw10gAccessMgtStartIpAddress_Type())
gel2esw10gAccessMgtStartIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gAccessMgtStartIpAddress.setStatus(_A)
_Gel2esw10gAccessMgtEndIpAddress_Type=DisplayString
_Gel2esw10gAccessMgtEndIpAddress_Object=MibTableColumn
gel2esw10gAccessMgtEndIpAddress=_Gel2esw10gAccessMgtEndIpAddress_Object((1,3,6,1,4,1,5205,2,51,3,6,1,3,1,4),_Gel2esw10gAccessMgtEndIpAddress_Type())
gel2esw10gAccessMgtEndIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gAccessMgtEndIpAddress.setStatus(_A)
class _Gel2esw10gAccessMgtHttpHttps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gAccessMgtHttpHttps_Type.__name__=_C
_Gel2esw10gAccessMgtHttpHttps_Object=MibTableColumn
gel2esw10gAccessMgtHttpHttps=_Gel2esw10gAccessMgtHttpHttps_Object((1,3,6,1,4,1,5205,2,51,3,6,1,3,1,5),_Gel2esw10gAccessMgtHttpHttps_Type())
gel2esw10gAccessMgtHttpHttps.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gAccessMgtHttpHttps.setStatus(_A)
class _Gel2esw10gAccessMgtSNMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gAccessMgtSNMP_Type.__name__=_C
_Gel2esw10gAccessMgtSNMP_Object=MibTableColumn
gel2esw10gAccessMgtSNMP=_Gel2esw10gAccessMgtSNMP_Object((1,3,6,1,4,1,5205,2,51,3,6,1,3,1,6),_Gel2esw10gAccessMgtSNMP_Type())
gel2esw10gAccessMgtSNMP.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gAccessMgtSNMP.setStatus(_A)
class _Gel2esw10gAccessMgtTelnetSSH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gAccessMgtTelnetSSH_Type.__name__=_C
_Gel2esw10gAccessMgtTelnetSSH_Object=MibTableColumn
gel2esw10gAccessMgtTelnetSSH=_Gel2esw10gAccessMgtTelnetSSH_Object((1,3,6,1,4,1,5205,2,51,3,6,1,3,1,7),_Gel2esw10gAccessMgtTelnetSSH_Type())
gel2esw10gAccessMgtTelnetSSH.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gAccessMgtTelnetSSH.setStatus(_A)
class _Gel2esw10gAccessMgtRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw10gAccessMgtRowStatus_Type.__name__=_C
_Gel2esw10gAccessMgtRowStatus_Object=MibTableColumn
gel2esw10gAccessMgtRowStatus=_Gel2esw10gAccessMgtRowStatus_Object((1,3,6,1,4,1,5205,2,51,3,6,1,3,1,8),_Gel2esw10gAccessMgtRowStatus_Type())
gel2esw10gAccessMgtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gAccessMgtRowStatus.setStatus(_A)
_Gel2esw10gAccessMgtStatistics_ObjectIdentity=ObjectIdentity
gel2esw10gAccessMgtStatistics=_Gel2esw10gAccessMgtStatistics_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,6,2))
_Gel2esw10gHttpReceivedPkts_Type=Counter32
_Gel2esw10gHttpReceivedPkts_Object=MibScalar
gel2esw10gHttpReceivedPkts=_Gel2esw10gHttpReceivedPkts_Object((1,3,6,1,4,1,5205,2,51,3,6,2,1),_Gel2esw10gHttpReceivedPkts_Type())
gel2esw10gHttpReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gHttpReceivedPkts.setStatus(_A)
_Gel2esw10gHttpAllowedPkts_Type=Counter32
_Gel2esw10gHttpAllowedPkts_Object=MibScalar
gel2esw10gHttpAllowedPkts=_Gel2esw10gHttpAllowedPkts_Object((1,3,6,1,4,1,5205,2,51,3,6,2,2),_Gel2esw10gHttpAllowedPkts_Type())
gel2esw10gHttpAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gHttpAllowedPkts.setStatus(_A)
_Gel2esw10gHttpDiscardedPkts_Type=Counter32
_Gel2esw10gHttpDiscardedPkts_Object=MibScalar
gel2esw10gHttpDiscardedPkts=_Gel2esw10gHttpDiscardedPkts_Object((1,3,6,1,4,1,5205,2,51,3,6,2,3),_Gel2esw10gHttpDiscardedPkts_Type())
gel2esw10gHttpDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gHttpDiscardedPkts.setStatus(_A)
_Gel2esw10gHttpsReceivedPkts_Type=Counter32
_Gel2esw10gHttpsReceivedPkts_Object=MibScalar
gel2esw10gHttpsReceivedPkts=_Gel2esw10gHttpsReceivedPkts_Object((1,3,6,1,4,1,5205,2,51,3,6,2,4),_Gel2esw10gHttpsReceivedPkts_Type())
gel2esw10gHttpsReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gHttpsReceivedPkts.setStatus(_A)
_Gel2esw10gHttpsAllowedPkts_Type=Counter32
_Gel2esw10gHttpsAllowedPkts_Object=MibScalar
gel2esw10gHttpsAllowedPkts=_Gel2esw10gHttpsAllowedPkts_Object((1,3,6,1,4,1,5205,2,51,3,6,2,5),_Gel2esw10gHttpsAllowedPkts_Type())
gel2esw10gHttpsAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gHttpsAllowedPkts.setStatus(_A)
_Gel2esw10gHttpsDiscardedPkts_Type=Counter32
_Gel2esw10gHttpsDiscardedPkts_Object=MibScalar
gel2esw10gHttpsDiscardedPkts=_Gel2esw10gHttpsDiscardedPkts_Object((1,3,6,1,4,1,5205,2,51,3,6,2,6),_Gel2esw10gHttpsDiscardedPkts_Type())
gel2esw10gHttpsDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gHttpsDiscardedPkts.setStatus(_A)
_Gel2esw10gSnmpReceivedPkts_Type=Counter32
_Gel2esw10gSnmpReceivedPkts_Object=MibScalar
gel2esw10gSnmpReceivedPkts=_Gel2esw10gSnmpReceivedPkts_Object((1,3,6,1,4,1,5205,2,51,3,6,2,7),_Gel2esw10gSnmpReceivedPkts_Type())
gel2esw10gSnmpReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSnmpReceivedPkts.setStatus(_A)
_Gel2esw10gSnmpAllowedPkts_Type=Counter32
_Gel2esw10gSnmpAllowedPkts_Object=MibScalar
gel2esw10gSnmpAllowedPkts=_Gel2esw10gSnmpAllowedPkts_Object((1,3,6,1,4,1,5205,2,51,3,6,2,8),_Gel2esw10gSnmpAllowedPkts_Type())
gel2esw10gSnmpAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSnmpAllowedPkts.setStatus(_A)
_Gel2esw10gSnmpDiscardedPkts_Type=Counter32
_Gel2esw10gSnmpDiscardedPkts_Object=MibScalar
gel2esw10gSnmpDiscardedPkts=_Gel2esw10gSnmpDiscardedPkts_Object((1,3,6,1,4,1,5205,2,51,3,6,2,9),_Gel2esw10gSnmpDiscardedPkts_Type())
gel2esw10gSnmpDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSnmpDiscardedPkts.setStatus(_A)
_Gel2esw10gTelnetReceivedPkts_Type=Counter32
_Gel2esw10gTelnetReceivedPkts_Object=MibScalar
gel2esw10gTelnetReceivedPkts=_Gel2esw10gTelnetReceivedPkts_Object((1,3,6,1,4,1,5205,2,51,3,6,2,10),_Gel2esw10gTelnetReceivedPkts_Type())
gel2esw10gTelnetReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gTelnetReceivedPkts.setStatus(_A)
_Gel2esw10gTelnetAllowedPkts_Type=Counter32
_Gel2esw10gTelnetAllowedPkts_Object=MibScalar
gel2esw10gTelnetAllowedPkts=_Gel2esw10gTelnetAllowedPkts_Object((1,3,6,1,4,1,5205,2,51,3,6,2,11),_Gel2esw10gTelnetAllowedPkts_Type())
gel2esw10gTelnetAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gTelnetAllowedPkts.setStatus(_A)
_Gel2esw10gTelnetDiscardedPkts_Type=Counter32
_Gel2esw10gTelnetDiscardedPkts_Object=MibScalar
gel2esw10gTelnetDiscardedPkts=_Gel2esw10gTelnetDiscardedPkts_Object((1,3,6,1,4,1,5205,2,51,3,6,2,12),_Gel2esw10gTelnetDiscardedPkts_Type())
gel2esw10gTelnetDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gTelnetDiscardedPkts.setStatus(_A)
_Gel2esw10gSSHReceivedPkts_Type=Counter32
_Gel2esw10gSSHReceivedPkts_Object=MibScalar
gel2esw10gSSHReceivedPkts=_Gel2esw10gSSHReceivedPkts_Object((1,3,6,1,4,1,5205,2,51,3,6,2,13),_Gel2esw10gSSHReceivedPkts_Type())
gel2esw10gSSHReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSSHReceivedPkts.setStatus(_A)
_Gel2esw10gSSHAllowedPkts_Type=Counter32
_Gel2esw10gSSHAllowedPkts_Object=MibScalar
gel2esw10gSSHAllowedPkts=_Gel2esw10gSSHAllowedPkts_Object((1,3,6,1,4,1,5205,2,51,3,6,2,14),_Gel2esw10gSSHAllowedPkts_Type())
gel2esw10gSSHAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSSHAllowedPkts.setStatus(_A)
_Gel2esw10gSSHDiscardedPkts_Type=Counter32
_Gel2esw10gSSHDiscardedPkts_Object=MibScalar
gel2esw10gSSHDiscardedPkts=_Gel2esw10gSSHDiscardedPkts_Object((1,3,6,1,4,1,5205,2,51,3,6,2,15),_Gel2esw10gSSHDiscardedPkts_Type())
gel2esw10gSSHDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gSSHDiscardedPkts.setStatus(_A)
class _Gel2esw10gAccessMgtStatisticsClearAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gAccessMgtStatisticsClearAll_Type.__name__=_C
_Gel2esw10gAccessMgtStatisticsClearAll_Object=MibScalar
gel2esw10gAccessMgtStatisticsClearAll=_Gel2esw10gAccessMgtStatisticsClearAll_Object((1,3,6,1,4,1,5205,2,51,3,6,2,16),_Gel2esw10gAccessMgtStatisticsClearAll_Type())
gel2esw10gAccessMgtStatisticsClearAll.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gAccessMgtStatisticsClearAll.setStatus(_A)
_Gel2esw10gSSH_ObjectIdentity=ObjectIdentity
gel2esw10gSSH=_Gel2esw10gSSH_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,7))
class _Gel2esw10gSSHMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gSSHMode_Type.__name__=_C
_Gel2esw10gSSHMode_Object=MibScalar
gel2esw10gSSHMode=_Gel2esw10gSSHMode_Object((1,3,6,1,4,1,5205,2,51,3,7,1),_Gel2esw10gSSHMode_Type())
gel2esw10gSSHMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSSHMode.setStatus(_A)
_Gel2esw10gHTTPS_ObjectIdentity=ObjectIdentity
gel2esw10gHTTPS=_Gel2esw10gHTTPS_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,8))
class _Gel2esw10gHTTPSMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gHTTPSMode_Type.__name__=_C
_Gel2esw10gHTTPSMode_Object=MibScalar
gel2esw10gHTTPSMode=_Gel2esw10gHTTPSMode_Object((1,3,6,1,4,1,5205,2,51,3,8,1),_Gel2esw10gHTTPSMode_Type())
gel2esw10gHTTPSMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gHTTPSMode.setStatus(_A)
class _Gel2esw10gHTTPSAutoRedirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gHTTPSAutoRedirect_Type.__name__=_C
_Gel2esw10gHTTPSAutoRedirect_Object=MibScalar
gel2esw10gHTTPSAutoRedirect=_Gel2esw10gHTTPSAutoRedirect_Object((1,3,6,1,4,1,5205,2,51,3,8,2),_Gel2esw10gHTTPSAutoRedirect_Type())
gel2esw10gHTTPSAutoRedirect.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gHTTPSAutoRedirect.setStatus(_A)
_Gel2esw10gAuthMethod_ObjectIdentity=ObjectIdentity
gel2esw10gAuthMethod=_Gel2esw10gAuthMethod_ObjectIdentity((1,3,6,1,4,1,5205,2,51,3,9))
class _Gel2esw10gConsoleAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw10gConsoleAuthMethod_Type.__name__=_C
_Gel2esw10gConsoleAuthMethod_Object=MibScalar
gel2esw10gConsoleAuthMethod=_Gel2esw10gConsoleAuthMethod_Object((1,3,6,1,4,1,5205,2,51,3,9,1),_Gel2esw10gConsoleAuthMethod_Type())
gel2esw10gConsoleAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gConsoleAuthMethod.setStatus(_A)
class _Gel2esw10gConsoleFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gConsoleFallback_Type.__name__=_C
_Gel2esw10gConsoleFallback_Object=MibScalar
gel2esw10gConsoleFallback=_Gel2esw10gConsoleFallback_Object((1,3,6,1,4,1,5205,2,51,3,9,2),_Gel2esw10gConsoleFallback_Type())
gel2esw10gConsoleFallback.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gConsoleFallback.setStatus(_A)
class _Gel2esw10gTelnetAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw10gTelnetAuthMethod_Type.__name__=_C
_Gel2esw10gTelnetAuthMethod_Object=MibScalar
gel2esw10gTelnetAuthMethod=_Gel2esw10gTelnetAuthMethod_Object((1,3,6,1,4,1,5205,2,51,3,9,3),_Gel2esw10gTelnetAuthMethod_Type())
gel2esw10gTelnetAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTelnetAuthMethod.setStatus(_A)
class _Gel2esw10gTelnetFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gTelnetFallback_Type.__name__=_C
_Gel2esw10gTelnetFallback_Object=MibScalar
gel2esw10gTelnetFallback=_Gel2esw10gTelnetFallback_Object((1,3,6,1,4,1,5205,2,51,3,9,4),_Gel2esw10gTelnetFallback_Type())
gel2esw10gTelnetFallback.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gTelnetFallback.setStatus(_A)
class _Gel2esw10gSshAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw10gSshAuthMethod_Type.__name__=_C
_Gel2esw10gSshAuthMethod_Object=MibScalar
gel2esw10gSshAuthMethod=_Gel2esw10gSshAuthMethod_Object((1,3,6,1,4,1,5205,2,51,3,9,5),_Gel2esw10gSshAuthMethod_Type())
gel2esw10gSshAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSshAuthMethod.setStatus(_A)
class _Gel2esw10gSshFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gSshFallback_Type.__name__=_C
_Gel2esw10gSshFallback_Object=MibScalar
gel2esw10gSshFallback=_Gel2esw10gSshFallback_Object((1,3,6,1,4,1,5205,2,51,3,9,6),_Gel2esw10gSshFallback_Type())
gel2esw10gSshFallback.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSshFallback.setStatus(_A)
class _Gel2esw10gWebAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw10gWebAuthMethod_Type.__name__=_C
_Gel2esw10gWebAuthMethod_Object=MibScalar
gel2esw10gWebAuthMethod=_Gel2esw10gWebAuthMethod_Object((1,3,6,1,4,1,5205,2,51,3,9,7),_Gel2esw10gWebAuthMethod_Type())
gel2esw10gWebAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gWebAuthMethod.setStatus(_A)
class _Gel2esw10gWebFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gWebFallback_Type.__name__=_C
_Gel2esw10gWebFallback_Object=MibScalar
gel2esw10gWebFallback=_Gel2esw10gWebFallback_Object((1,3,6,1,4,1,5205,2,51,3,9,8),_Gel2esw10gWebFallback_Type())
gel2esw10gWebFallback.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gWebFallback.setStatus(_A)
_Gel2esw10gMaintenance_ObjectIdentity=ObjectIdentity
gel2esw10gMaintenance=_Gel2esw10gMaintenance_ObjectIdentity((1,3,6,1,4,1,5205,2,51,4))
class _Gel2esw10gRestartDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gRestartDevice_Type.__name__=_C
_Gel2esw10gRestartDevice_Object=MibScalar
gel2esw10gRestartDevice=_Gel2esw10gRestartDevice_Object((1,3,6,1,4,1,5205,2,51,4,1),_Gel2esw10gRestartDevice_Type())
gel2esw10gRestartDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gRestartDevice.setStatus(_A)
_Gel2esw10gFirmware_ObjectIdentity=ObjectIdentity
gel2esw10gFirmware=_Gel2esw10gFirmware_ObjectIdentity((1,3,6,1,4,1,5205,2,51,4,2))
_Gel2esw10gFirmwareIpAddress_Type=IpAddress
_Gel2esw10gFirmwareIpAddress_Object=MibScalar
gel2esw10gFirmwareIpAddress=_Gel2esw10gFirmwareIpAddress_Object((1,3,6,1,4,1,5205,2,51,4,2,1),_Gel2esw10gFirmwareIpAddress_Type())
gel2esw10gFirmwareIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gFirmwareIpAddress.setStatus(_A)
_Gel2esw10gFirmwareFileName_Type=DisplayString
_Gel2esw10gFirmwareFileName_Object=MibScalar
gel2esw10gFirmwareFileName=_Gel2esw10gFirmwareFileName_Object((1,3,6,1,4,1,5205,2,51,4,2,2),_Gel2esw10gFirmwareFileName_Type())
gel2esw10gFirmwareFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gFirmwareFileName.setStatus(_A)
class _Gel2esw10gDoFirmwareUpgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gDoFirmwareUpgrade_Type.__name__=_C
_Gel2esw10gDoFirmwareUpgrade_Object=MibScalar
gel2esw10gDoFirmwareUpgrade=_Gel2esw10gDoFirmwareUpgrade_Object((1,3,6,1,4,1,5205,2,51,4,2,3),_Gel2esw10gDoFirmwareUpgrade_Type())
gel2esw10gDoFirmwareUpgrade.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gDoFirmwareUpgrade.setStatus(_A)
_Gel2esw10gSaveOrRestore_ObjectIdentity=ObjectIdentity
gel2esw10gSaveOrRestore=_Gel2esw10gSaveOrRestore_ObjectIdentity((1,3,6,1,4,1,5205,2,51,4,3))
class _Gel2esw10gFactoryDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gFactoryDefaults_Type.__name__=_C
_Gel2esw10gFactoryDefaults_Object=MibScalar
gel2esw10gFactoryDefaults=_Gel2esw10gFactoryDefaults_Object((1,3,6,1,4,1,5205,2,51,4,3,1),_Gel2esw10gFactoryDefaults_Type())
gel2esw10gFactoryDefaults.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gFactoryDefaults.setStatus(_A)
class _Gel2esw10gSaveStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gSaveStart_Type.__name__=_C
_Gel2esw10gSaveStart_Object=MibScalar
gel2esw10gSaveStart=_Gel2esw10gSaveStart_Object((1,3,6,1,4,1,5205,2,51,4,3,2),_Gel2esw10gSaveStart_Type())
gel2esw10gSaveStart.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSaveStart.setStatus(_A)
class _Gel2esw10gSaveUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gSaveUser_Type.__name__=_C
_Gel2esw10gSaveUser_Object=MibScalar
gel2esw10gSaveUser=_Gel2esw10gSaveUser_Object((1,3,6,1,4,1,5205,2,51,4,3,3),_Gel2esw10gSaveUser_Type())
gel2esw10gSaveUser.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gSaveUser.setStatus(_A)
class _Gel2esw10gRestoreUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw10gRestoreUser_Type.__name__=_C
_Gel2esw10gRestoreUser_Object=MibScalar
gel2esw10gRestoreUser=_Gel2esw10gRestoreUser_Object((1,3,6,1,4,1,5205,2,51,4,3,4),_Gel2esw10gRestoreUser_Type())
gel2esw10gRestoreUser.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gRestoreUser.setStatus(_A)
_Gel2esw10gExportOrImport_ObjectIdentity=ObjectIdentity
gel2esw10gExportOrImport=_Gel2esw10gExportOrImport_ObjectIdentity((1,3,6,1,4,1,5205,2,51,4,4))
_Gel2esw10gExportIpAddress_Type=IpAddress
_Gel2esw10gExportIpAddress_Object=MibScalar
gel2esw10gExportIpAddress=_Gel2esw10gExportIpAddress_Object((1,3,6,1,4,1,5205,2,51,4,4,1),_Gel2esw10gExportIpAddress_Type())
gel2esw10gExportIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gExportIpAddress.setStatus(_A)
_Gel2esw10gExportConfigName_Type=DisplayString
_Gel2esw10gExportConfigName_Object=MibScalar
gel2esw10gExportConfigName=_Gel2esw10gExportConfigName_Object((1,3,6,1,4,1,5205,2,51,4,4,2),_Gel2esw10gExportConfigName_Type())
gel2esw10gExportConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gExportConfigName.setStatus(_A)
class _Gel2esw10gDoExportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Gel2esw10gDoExportConfig_Type.__name__=_C
_Gel2esw10gDoExportConfig_Object=MibScalar
gel2esw10gDoExportConfig=_Gel2esw10gDoExportConfig_Object((1,3,6,1,4,1,5205,2,51,4,4,3),_Gel2esw10gDoExportConfig_Type())
gel2esw10gDoExportConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gDoExportConfig.setStatus(_A)
_Gel2esw10gImportIpAddress_Type=IpAddress
_Gel2esw10gImportIpAddress_Object=MibScalar
gel2esw10gImportIpAddress=_Gel2esw10gImportIpAddress_Object((1,3,6,1,4,1,5205,2,51,4,4,4),_Gel2esw10gImportIpAddress_Type())
gel2esw10gImportIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gImportIpAddress.setStatus(_A)
_Gel2esw10gImportConfigName_Type=DisplayString
_Gel2esw10gImportConfigName_Object=MibScalar
gel2esw10gImportConfigName=_Gel2esw10gImportConfigName_Object((1,3,6,1,4,1,5205,2,51,4,4,5),_Gel2esw10gImportConfigName_Type())
gel2esw10gImportConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gImportConfigName.setStatus(_A)
class _Gel2esw10gDoImportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Gel2esw10gDoImportConfig_Type.__name__=_C
_Gel2esw10gDoImportConfig_Object=MibScalar
gel2esw10gDoImportConfig=_Gel2esw10gDoImportConfig_Object((1,3,6,1,4,1,5205,2,51,4,4,6),_Gel2esw10gDoImportConfig_Type())
gel2esw10gDoImportConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gDoImportConfig.setStatus(_A)
_Gel2esw10gDiagnostics_ObjectIdentity=ObjectIdentity
gel2esw10gDiagnostics=_Gel2esw10gDiagnostics_ObjectIdentity((1,3,6,1,4,1,5205,2,51,4,5))
_Gel2esw10gPingIpAddress_Type=IpAddress
_Gel2esw10gPingIpAddress_Object=MibScalar
gel2esw10gPingIpAddress=_Gel2esw10gPingIpAddress_Object((1,3,6,1,4,1,5205,2,51,4,5,1),_Gel2esw10gPingIpAddress_Type())
gel2esw10gPingIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPingIpAddress.setStatus(_A)
class _Gel2esw10gPingSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,1400))
_Gel2esw10gPingSize_Type.__name__=_C
_Gel2esw10gPingSize_Object=MibScalar
gel2esw10gPingSize=_Gel2esw10gPingSize_Object((1,3,6,1,4,1,5205,2,51,4,5,2),_Gel2esw10gPingSize_Type())
gel2esw10gPingSize.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPingSize.setStatus(_A)
class _Gel2esw10gDoPingConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Gel2esw10gDoPingConfig_Type.__name__=_C
_Gel2esw10gDoPingConfig_Object=MibScalar
gel2esw10gDoPingConfig=_Gel2esw10gDoPingConfig_Object((1,3,6,1,4,1,5205,2,51,4,5,3),_Gel2esw10gDoPingConfig_Type())
gel2esw10gDoPingConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gDoPingConfig.setStatus(_A)
_Gel2esw10gPingResult_Type=DisplayString
_Gel2esw10gPingResult_Object=MibScalar
gel2esw10gPingResult=_Gel2esw10gPingResult_Object((1,3,6,1,4,1,5205,2,51,4,5,4),_Gel2esw10gPingResult_Type())
gel2esw10gPingResult.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPingResult.setStatus(_A)
_Gel2esw10gPing6IpAddress_Type=DisplayString
_Gel2esw10gPing6IpAddress_Object=MibScalar
gel2esw10gPing6IpAddress=_Gel2esw10gPing6IpAddress_Object((1,3,6,1,4,1,5205,2,51,4,5,5),_Gel2esw10gPing6IpAddress_Type())
gel2esw10gPing6IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPing6IpAddress.setStatus(_A)
class _Gel2esw10gPing6Size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,1400))
_Gel2esw10gPing6Size_Type.__name__=_C
_Gel2esw10gPing6Size_Object=MibScalar
gel2esw10gPing6Size=_Gel2esw10gPing6Size_Object((1,3,6,1,4,1,5205,2,51,4,5,6),_Gel2esw10gPing6Size_Type())
gel2esw10gPing6Size.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gPing6Size.setStatus(_A)
class _Gel2esw10gDoPing6Config_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Gel2esw10gDoPing6Config_Type.__name__=_C
_Gel2esw10gDoPing6Config_Object=MibScalar
gel2esw10gDoPing6Config=_Gel2esw10gDoPing6Config_Object((1,3,6,1,4,1,5205,2,51,4,5,7),_Gel2esw10gDoPing6Config_Type())
gel2esw10gDoPing6Config.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gDoPing6Config.setStatus(_A)
_Gel2esw10gPing6Result_Type=DisplayString
_Gel2esw10gPing6Result_Object=MibScalar
gel2esw10gPing6Result=_Gel2esw10gPing6Result_Object((1,3,6,1,4,1,5205,2,51,4,5,8),_Gel2esw10gPing6Result_Type())
gel2esw10gPing6Result.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gPing6Result.setStatus(_A)
_Gel2esw10gVeriPHY_ObjectIdentity=ObjectIdentity
gel2esw10gVeriPHY=_Gel2esw10gVeriPHY_ObjectIdentity((1,3,6,1,4,1,5205,2,51,4,5,9))
class _Gel2esw10gVeriPHYTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gVeriPHYTest_Type.__name__=_C
_Gel2esw10gVeriPHYTest_Object=MibScalar
gel2esw10gVeriPHYTest=_Gel2esw10gVeriPHYTest_Object((1,3,6,1,4,1,5205,2,51,4,5,9,1),_Gel2esw10gVeriPHYTest_Type())
gel2esw10gVeriPHYTest.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw10gVeriPHYTest.setStatus(_A)
_Gel2esw10gVeriPHYTable_Object=MibTable
gel2esw10gVeriPHYTable=_Gel2esw10gVeriPHYTable_Object((1,3,6,1,4,1,5205,2,51,4,5,9,2))
if mibBuilder.loadTexts:gel2esw10gVeriPHYTable.setStatus(_A)
_Gel2esw10gVeriPHYEntry_Object=MibTableRow
gel2esw10gVeriPHYEntry=_Gel2esw10gVeriPHYEntry_Object((1,3,6,1,4,1,5205,2,51,4,5,9,2,1))
gel2esw10gVeriPHYEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:gel2esw10gVeriPHYEntry.setStatus(_A)
class _Gel2esw10gVeriPHYPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw10gVeriPHYPort_Type.__name__=_C
_Gel2esw10gVeriPHYPort_Object=MibTableColumn
gel2esw10gVeriPHYPort=_Gel2esw10gVeriPHYPort_Object((1,3,6,1,4,1,5205,2,51,4,5,9,2,1,1),_Gel2esw10gVeriPHYPort_Type())
gel2esw10gVeriPHYPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw10gVeriPHYPort.setStatus(_A)
_Gel2esw10gVeriPHYPairA_Type=DisplayString
_Gel2esw10gVeriPHYPairA_Object=MibTableColumn
gel2esw10gVeriPHYPairA=_Gel2esw10gVeriPHYPairA_Object((1,3,6,1,4,1,5205,2,51,4,5,9,2,1,2),_Gel2esw10gVeriPHYPairA_Type())
gel2esw10gVeriPHYPairA.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gVeriPHYPairA.setStatus(_A)
_Gel2esw10gVeriPHYLengthA_Type=DisplayString
_Gel2esw10gVeriPHYLengthA_Object=MibTableColumn
gel2esw10gVeriPHYLengthA=_Gel2esw10gVeriPHYLengthA_Object((1,3,6,1,4,1,5205,2,51,4,5,9,2,1,3),_Gel2esw10gVeriPHYLengthA_Type())
gel2esw10gVeriPHYLengthA.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gVeriPHYLengthA.setStatus(_A)
_Gel2esw10gVeriPHYPairB_Type=DisplayString
_Gel2esw10gVeriPHYPairB_Object=MibTableColumn
gel2esw10gVeriPHYPairB=_Gel2esw10gVeriPHYPairB_Object((1,3,6,1,4,1,5205,2,51,4,5,9,2,1,4),_Gel2esw10gVeriPHYPairB_Type())
gel2esw10gVeriPHYPairB.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gVeriPHYPairB.setStatus(_A)
_Gel2esw10gVeriPHYLengthB_Type=DisplayString
_Gel2esw10gVeriPHYLengthB_Object=MibTableColumn
gel2esw10gVeriPHYLengthB=_Gel2esw10gVeriPHYLengthB_Object((1,3,6,1,4,1,5205,2,51,4,5,9,2,1,5),_Gel2esw10gVeriPHYLengthB_Type())
gel2esw10gVeriPHYLengthB.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gVeriPHYLengthB.setStatus(_A)
_Gel2esw10gVeriPHYPairC_Type=DisplayString
_Gel2esw10gVeriPHYPairC_Object=MibTableColumn
gel2esw10gVeriPHYPairC=_Gel2esw10gVeriPHYPairC_Object((1,3,6,1,4,1,5205,2,51,4,5,9,2,1,6),_Gel2esw10gVeriPHYPairC_Type())
gel2esw10gVeriPHYPairC.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gVeriPHYPairC.setStatus(_A)
_Gel2esw10gVeriPHYLengthC_Type=DisplayString
_Gel2esw10gVeriPHYLengthC_Object=MibTableColumn
gel2esw10gVeriPHYLengthC=_Gel2esw10gVeriPHYLengthC_Object((1,3,6,1,4,1,5205,2,51,4,5,9,2,1,7),_Gel2esw10gVeriPHYLengthC_Type())
gel2esw10gVeriPHYLengthC.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gVeriPHYLengthC.setStatus(_A)
_Gel2esw10gVeriPHYPairD_Type=DisplayString
_Gel2esw10gVeriPHYPairD_Object=MibTableColumn
gel2esw10gVeriPHYPairD=_Gel2esw10gVeriPHYPairD_Object((1,3,6,1,4,1,5205,2,51,4,5,9,2,1,8),_Gel2esw10gVeriPHYPairD_Type())
gel2esw10gVeriPHYPairD.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gVeriPHYPairD.setStatus(_A)
_Gel2esw10gVeriPHYLengthD_Type=DisplayString
_Gel2esw10gVeriPHYLengthD_Object=MibTableColumn
gel2esw10gVeriPHYLengthD=_Gel2esw10gVeriPHYLengthD_Object((1,3,6,1,4,1,5205,2,51,4,5,9,2,1,9),_Gel2esw10gVeriPHYLengthD_Type())
gel2esw10gVeriPHYLengthD.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gVeriPHYLengthD.setStatus(_A)
_Gel2esw10gTrap_ObjectIdentity=ObjectIdentity
gel2esw10gTrap=_Gel2esw10gTrap_ObjectIdentity((1,3,6,1,4,1,5205,2,51,5))
_Gel2esw10gTrapEvent_ObjectIdentity=ObjectIdentity
gel2esw10gTrapEvent=_Gel2esw10gTrapEvent_ObjectIdentity((1,3,6,1,4,1,5205,2,51,5,1))
_Gel2esw10gTrapVariable_ObjectIdentity=ObjectIdentity
gel2esw10gTrapVariable=_Gel2esw10gTrapVariable_ObjectIdentity((1,3,6,1,4,1,5205,2,51,5,2))
_Gel2esw10gInformation_Type=DisplayString
_Gel2esw10gInformation_Object=MibScalar
gel2esw10gInformation=_Gel2esw10gInformation_Object((1,3,6,1,4,1,5205,2,51,5,2,1),_Gel2esw10gInformation_Type())
gel2esw10gInformation.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw10gInformation.setStatus(_A)
gel2esw10gEmergency=NotificationType((1,3,6,1,4,1,5205,2,51,5,1,1))
gel2esw10gEmergency.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw10gEmergency.setStatus(_A)
gel2esw10gAlert=NotificationType((1,3,6,1,4,1,5205,2,51,5,1,2))
gel2esw10gAlert.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw10gAlert.setStatus(_A)
gel2esw10gCritical=NotificationType((1,3,6,1,4,1,5205,2,51,5,1,3))
gel2esw10gCritical.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw10gCritical.setStatus(_A)
gel2esw10gError=NotificationType((1,3,6,1,4,1,5205,2,51,5,1,4))
gel2esw10gError.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw10gError.setStatus(_A)
gel2esw10gWarning=NotificationType((1,3,6,1,4,1,5205,2,51,5,1,5))
gel2esw10gWarning.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw10gWarning.setStatus(_A)
gel2esw10gNotice=NotificationType((1,3,6,1,4,1,5205,2,51,5,1,6))
gel2esw10gNotice.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw10gNotice.setStatus(_A)
gel2esw10gInformational=NotificationType((1,3,6,1,4,1,5205,2,51,5,1,7))
gel2esw10gInformational.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw10gInformational.setStatus(_A)
gel2esw10gDebug=NotificationType((1,3,6,1,4,1,5205,2,51,5,1,8))
gel2esw10gDebug.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw10gDebug.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'privatetech':privatetech,'switch':switch,'gel2esw10gProductId':gel2esw10gProductId,'gel2esw10gSystem':gel2esw10gSystem,'gel2esw10gSystemInformation':gel2esw10gSystemInformation,'gel2esw10gModelName':gel2esw10gModelName,'gel2esw10gBIOSVersion':gel2esw10gBIOSVersion,'gel2esw10gFirmwareVersion':gel2esw10gFirmwareVersion,'gel2esw10gHardwareMechanicalVersion':gel2esw10gHardwareMechanicalVersion,'gel2esw10gSeriesNumber':gel2esw10gSeriesNumber,'gel2esw10gHostMACAddress':gel2esw10gHostMACAddress,'gel2esw10gConsoleBaudrate':gel2esw10gConsoleBaudrate,'gel2esw10gRAMSize':gel2esw10gRAMSize,'gel2esw10gFlashSize':gel2esw10gFlashSize,'gel2esw10gBridgeFBDSize':gel2esw10gBridgeFBDSize,'gel2esw10gTransmitQueue':gel2esw10gTransmitQueue,'gel2esw10gMaximumFrameSize':gel2esw10gMaximumFrameSize,'gel2esw10gCPULoad':gel2esw10gCPULoad,'gel2esw10gSystemTime':gel2esw10gSystemTime,'gel2esw10gSystemTimeManual':gel2esw10gSystemTimeManual,'gel2esw10gSystemTimeManualClockSource':gel2esw10gSystemTimeManualClockSource,'gel2esw10gSystemTimeManualLocaltime':gel2esw10gSystemTimeManualLocaltime,'gel2esw10gSystemTimeManualTimeZoneOffset':gel2esw10gSystemTimeManualTimeZoneOffset,'gel2esw10gSystemTimeManualDaylightSavings':gel2esw10gSystemTimeManualDaylightSavings,'gel2esw10gSystemTimeManualTimeSetOffset':gel2esw10gSystemTimeManualTimeSetOffset,'gel2esw10gSystemTimeManualDaylightSavingsType':gel2esw10gSystemTimeManualDaylightSavingsType,'gel2esw10gSystemTimeManualDaylightSavingsBydatesFrom':gel2esw10gSystemTimeManualDaylightSavingsBydatesFrom,'gel2esw10gSystemTimeManualDaylightSavingsBydatesTo':gel2esw10gSystemTimeManualDaylightSavingsBydatesTo,'gel2esw10gSystemTimeManualDaylightSavingsRecurringDayFrom':gel2esw10gSystemTimeManualDaylightSavingsRecurringDayFrom,'gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekFrom':gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekFrom,'gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthFrom':gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthFrom,'gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeFrom':gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeFrom,'gel2esw10gSystemTimeManualDaylightSavingsRecurringDayTo':gel2esw10gSystemTimeManualDaylightSavingsRecurringDayTo,'gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekTo':gel2esw10gSystemTimeManualDaylightSavingsRecurringWeekTo,'gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthTo':gel2esw10gSystemTimeManualDaylightSavingsRecurringMonthTo,'gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeTo':gel2esw10gSystemTimeManualDaylightSavingsRecurringTimeTo,'gel2esw10gSystemTimeNTP':gel2esw10gSystemTimeNTP,'gel2esw10gSystemTimeNTPTable':gel2esw10gSystemTimeNTPTable,'gel2esw10gSystemTimeNTPEntry':gel2esw10gSystemTimeNTPEntry,_K:gel2esw10gSystemTimeNTPIndex,'gel2esw10gSystemTimeNTPServerIPType':gel2esw10gSystemTimeNTPServerIPType,'gel2esw10gSystemTimeNTPServer':gel2esw10gSystemTimeNTPServer,'gel2esw10gSystemTimeNTPCurrentMode':gel2esw10gSystemTimeNTPCurrentMode,'gel2esw10gSystemAccount':gel2esw10gSystemAccount,'gel2esw10gSystemAccountUsers':gel2esw10gSystemAccountUsers,'gel2esw10gSystemAccountUserCreate':gel2esw10gSystemAccountUserCreate,'gel2esw10gSystemAccountUsersTable':gel2esw10gSystemAccountUsersTable,'gel2esw10gSystemAccountUsersEntry':gel2esw10gSystemAccountUsersEntry,_L:gel2esw10gUserIndex,'gel2esw10gUserName':gel2esw10gUserName,'gel2esw10gPassword':gel2esw10gPassword,'gel2esw10gUserPrivilegeLevel':gel2esw10gUserPrivilegeLevel,'gel2esw10gAccountUserRowStatus':gel2esw10gAccountUserRowStatus,'gel2esw10gSystemAccountPrivilegeLevel':gel2esw10gSystemAccountPrivilegeLevel,'gel2esw10gAccountPrivilegeLevel':gel2esw10gAccountPrivilegeLevel,'gel2esw10gAggregationPrivilegeLevel':gel2esw10gAggregationPrivilegeLevel,'gel2esw10gDiagnosticsPrivilegeLevel':gel2esw10gDiagnosticsPrivilegeLevel,'gel2esw10gEEEPrivilegeLevel':gel2esw10gEEEPrivilegeLevel,'gel2esw10gEasyportPrivilegeLevel':gel2esw10gEasyportPrivilegeLevel,'gel2esw10gGARPPrivilegeLevel':gel2esw10gGARPPrivilegeLevel,'gel2esw10gGVRPPrivilegeLevel':gel2esw10gGVRPPrivilegeLevel,'gel2esw10gIPPrivilegeLevel':gel2esw10gIPPrivilegeLevel,'gel2esw10gIPMCSnoopingPrivilegeLevel':gel2esw10gIPMCSnoopingPrivilegeLevel,'gel2esw10gLACPPrivilegeLevel':gel2esw10gLACPPrivilegeLevel,'gel2esw10gLLDPPrivilegeLevel':gel2esw10gLLDPPrivilegeLevel,'gel2esw10gLLDPMEDPrivilegeLevel':gel2esw10gLLDPMEDPrivilegeLevel,'gel2esw10gMACTablePrivilegeLevel':gel2esw10gMACTablePrivilegeLevel,'gel2esw10gMRPPrivilegeLevel':gel2esw10gMRPPrivilegeLevel,'gel2esw10gMVRPrivilegeLevel':gel2esw10gMVRPrivilegeLevel,'gel2esw10gMVRPPrivilegeLevel':gel2esw10gMVRPPrivilegeLevel,'gel2esw10gMaintenancePrivilegeLevel':gel2esw10gMaintenancePrivilegeLevel,'gel2esw10gMirroringPrivilegeLevel':gel2esw10gMirroringPrivilegeLevel,'gel2esw10gPortsPrivilegeLevel':gel2esw10gPortsPrivilegeLevel,'gel2esw10gPrivateVLANsPrivilegeLevel':gel2esw10gPrivateVLANsPrivilegeLevel,'gel2esw10gQoSPrivilegeLevel':gel2esw10gQoSPrivilegeLevel,'gel2esw10gSMTPPrivilegeLevel':gel2esw10gSMTPPrivilegeLevel,'gel2esw10gSNMPPrivilegeLevel':gel2esw10gSNMPPrivilegeLevel,'gel2esw10gSecurityPrivilegeLevel':gel2esw10gSecurityPrivilegeLevel,'gel2esw10gSpanningTreePrivilegeLevel':gel2esw10gSpanningTreePrivilegeLevel,'gel2esw10gSystemPrivilegeLevel':gel2esw10gSystemPrivilegeLevel,'gel2esw10gTrapEventPrivilegeLevel':gel2esw10gTrapEventPrivilegeLevel,'gel2esw10gVCLPrivilegeLevel':gel2esw10gVCLPrivilegeLevel,'gel2esw10gVLANsPrivilegeLevel':gel2esw10gVLANsPrivilegeLevel,'gel2esw10gVoiceVLANPrivilegeLevel':gel2esw10gVoiceVLANPrivilegeLevel,'gel2esw10gIP':gel2esw10gIP,'gel2esw10gIPv4':gel2esw10gIPv4,'gel2esw10gIPv4Configured':gel2esw10gIPv4Configured,'gel2esw10gIpv4DHCPClient':gel2esw10gIpv4DHCPClient,'gel2esw10gIPv4Address':gel2esw10gIPv4Address,'gel2esw10gIPv4Mask':gel2esw10gIPv4Mask,'gel2esw10gIPv4Router':gel2esw10gIPv4Router,'gel2esw10gIPv4VLANId':gel2esw10gIPv4VLANId,'gel2esw10gIPv4DNSServer':gel2esw10gIPv4DNSServer,'gel2esw10gIPv4DNSProxy':gel2esw10gIPv4DNSProxy,'gel2esw10gIPv4Current':gel2esw10gIPv4Current,'gel2esw10gIpv4CurrentDHCPClient':gel2esw10gIpv4CurrentDHCPClient,'gel2esw10gIPv4CurrentAddress':gel2esw10gIPv4CurrentAddress,'gel2esw10gIPv4CurrentMask':gel2esw10gIPv4CurrentMask,'gel2esw10gIPv4CurrentRouter':gel2esw10gIPv4CurrentRouter,'gel2esw10gIPv4CurrentVLANId':gel2esw10gIPv4CurrentVLANId,'gel2esw10gIPv4CurrentDNSServer':gel2esw10gIPv4CurrentDNSServer,'gel2esw10gIPv6':gel2esw10gIPv6,'gel2esw10gIPv6Configured':gel2esw10gIPv6Configured,'gel2esw10gIpv6AutoConfiguration':gel2esw10gIpv6AutoConfiguration,'gel2esw10gIpv6Address':gel2esw10gIpv6Address,'gel2esw10gIpv6Prefix':gel2esw10gIpv6Prefix,'gel2esw10gIpv6Router':gel2esw10gIpv6Router,'gel2esw10gIPv6Current':gel2esw10gIPv6Current,'gel2esw10gIpv6CurrentAutoConfiguration':gel2esw10gIpv6CurrentAutoConfiguration,'gel2esw10gIpv6CurrentAddress':gel2esw10gIpv6CurrentAddress,'gel2esw10gIpv6CurrentLinkLocalAddress':gel2esw10gIpv6CurrentLinkLocalAddress,'gel2esw10gIpv6CurrentPrefix':gel2esw10gIpv6CurrentPrefix,'gel2esw10gIpv6CurrentRouter':gel2esw10gIpv6CurrentRouter,'gel2esw10gSyslog':gel2esw10gSyslog,'gel2esw10gSyslogConf':gel2esw10gSyslogConf,'gel2esw10gServerMode':gel2esw10gServerMode,'gel2esw10gServerAddress1':gel2esw10gServerAddress1,'gel2esw10gServerAddress2':gel2esw10gServerAddress2,'gel2esw10gSyslogLevel':gel2esw10gSyslogLevel,'gel2esw10gSyslogDetailedInfo':gel2esw10gSyslogDetailedInfo,'gel2esw10gSyslogDetailedInfoClear':gel2esw10gSyslogDetailedInfoClear,'gel2esw10gSyslogDetailedInfoTable':gel2esw10gSyslogDetailedInfoTable,'gel2esw10gSyslogDetailedInfoEntry':gel2esw10gSyslogDetailedInfoEntry,_M:gel2esw10gSyslogDetailedInfoIndex,'gel2esw10gSyslogDetailedInfoLevel':gel2esw10gSyslogDetailedInfoLevel,'gel2esw10gSyslogDetailedInfoTime':gel2esw10gSyslogDetailedInfoTime,'gel2esw10gSyslogDetailedInfoMessage':gel2esw10gSyslogDetailedInfoMessage,'gel2esw10gSnmp':gel2esw10gSnmp,'gel2esw10gSnmpConf':gel2esw10gSnmpConf,'gel2esw10gGetCommunity':gel2esw10gGetCommunity,'gel2esw10gSetCommunityMode':gel2esw10gSetCommunityMode,'gel2esw10gSetCommunity':gel2esw10gSetCommunity,'gel2esw10gTrapHostConfTable':gel2esw10gTrapHostConfTable,'gel2esw10gTrapHostConfEntry':gel2esw10gTrapHostConfEntry,_N:gel2esw10gTrapHostConfIndex,'gel2esw10gTrapHostConfVersion':gel2esw10gTrapHostConfVersion,'gel2esw10gTrapHostConfIPType':gel2esw10gTrapHostConfIPType,'gel2esw10gTrapHostConfIP':gel2esw10gTrapHostConfIP,'gel2esw10gTrapHostConfPort':gel2esw10gTrapHostConfPort,'gel2esw10gTrapHostConfCommunity':gel2esw10gTrapHostConfCommunity,'gel2esw10gTrapHostConfSeverityLevel':gel2esw10gTrapHostConfSeverityLevel,'gel2esw10gTrapHostConfSecurityLevel':gel2esw10gTrapHostConfSecurityLevel,'gel2esw10gTrapHostConfAuthPtc':gel2esw10gTrapHostConfAuthPtc,'gel2esw10gTrapHostConfAuthPassword':gel2esw10gTrapHostConfAuthPassword,'gel2esw10gTrapHostConfPrivPtc':gel2esw10gTrapHostConfPrivPtc,'gel2esw10gTrapHostConfPrivPassword':gel2esw10gTrapHostConfPrivPassword,'gel2esw10gTrapHostConfCurrentMode':gel2esw10gTrapHostConfCurrentMode,'gel2esw10gConfiguration':gel2esw10gConfiguration,'gel2esw10gPort':gel2esw10gPort,'gel2esw10gPortConfigurationTable':gel2esw10gPortConfigurationTable,'gel2esw10gPortConfigurationEntry':gel2esw10gPortConfigurationEntry,_O:gel2esw10gPortConfPort,'gel2esw10gPortConfPortMedia':gel2esw10gPortConfPortMedia,'gel2esw10gPortConfLink':gel2esw10gPortConfLink,'gel2esw10gPortConfCurrentSpeed':gel2esw10gPortConfCurrentSpeed,'gel2esw10gPortConfSpeed':gel2esw10gPortConfSpeed,'gel2esw10gPortConfCurrentFlowControlRx':gel2esw10gPortConfCurrentFlowControlRx,'gel2esw10gPortConfCurrentFlowControlTx':gel2esw10gPortConfCurrentFlowControlTx,'gel2esw10gPortConfFlowControl':gel2esw10gPortConfFlowControl,'gel2esw10gPortConfMaxFrameSize':gel2esw10gPortConfMaxFrameSize,'gel2esw10gPortConfExcessiveCollisionMode':gel2esw10gPortConfExcessiveCollisionMode,'gel2esw10gPortConfPowerControl':gel2esw10gPortConfPowerControl,'gel2esw10gPortConfDescription':gel2esw10gPortConfDescription,'gel2esw10gPortTrafficStatisticsTable':gel2esw10gPortTrafficStatisticsTable,'gel2esw10gPortTrafficStatisticsEntry':gel2esw10gPortTrafficStatisticsEntry,_P:gel2esw10gPortTrafficStatisticsPort,'gel2esw10gPortTrafficStatisticsClear':gel2esw10gPortTrafficStatisticsClear,'gel2esw10gPortTrafficRxPackets':gel2esw10gPortTrafficRxPackets,'gel2esw10gPortTrafficRxOctets':gel2esw10gPortTrafficRxOctets,'gel2esw10gPortTrafficRxUnicast':gel2esw10gPortTrafficRxUnicast,'gel2esw10gPortTrafficRxMulticast':gel2esw10gPortTrafficRxMulticast,'gel2esw10gPortTrafficRxBroadcast':gel2esw10gPortTrafficRxBroadcast,'gel2esw10gPortTrafficRxPause':gel2esw10gPortTrafficRxPause,'gel2esw10gPortTrafficRx64Bytes':gel2esw10gPortTrafficRx64Bytes,'gel2esw10gPortTrafficRx65to127Bytes':gel2esw10gPortTrafficRx65to127Bytes,'gel2esw10gPortTrafficRx128to255Bytes':gel2esw10gPortTrafficRx128to255Bytes,'gel2esw10gPortTrafficRx256to511Bytes':gel2esw10gPortTrafficRx256to511Bytes,'gel2esw10gPortTrafficRx512to1023Bytes':gel2esw10gPortTrafficRx512to1023Bytes,'gel2esw10gPortTrafficRx1024to1526Bytes':gel2esw10gPortTrafficRx1024to1526Bytes,'gel2esw10gPortTrafficRxExceecd1527Bytes':gel2esw10gPortTrafficRxExceecd1527Bytes,'gel2esw10gPortTrafficRxQ0':gel2esw10gPortTrafficRxQ0,'gel2esw10gPortTrafficRxQ1':gel2esw10gPortTrafficRxQ1,'gel2esw10gPortTrafficRxQ2':gel2esw10gPortTrafficRxQ2,'gel2esw10gPortTrafficRxQ3':gel2esw10gPortTrafficRxQ3,'gel2esw10gPortTrafficRxQ4':gel2esw10gPortTrafficRxQ4,'gel2esw10gPortTrafficRxQ5':gel2esw10gPortTrafficRxQ5,'gel2esw10gPortTrafficRxQ6':gel2esw10gPortTrafficRxQ6,'gel2esw10gPortTrafficRxQ7':gel2esw10gPortTrafficRxQ7,'gel2esw10gPortTrafficRxDrops':gel2esw10gPortTrafficRxDrops,'gel2esw10gPortTrafficRxCRCorAlignment':gel2esw10gPortTrafficRxCRCorAlignment,'gel2esw10gPortTrafficRxUndersize':gel2esw10gPortTrafficRxUndersize,'gel2esw10gPortTrafficRxOversize':gel2esw10gPortTrafficRxOversize,'gel2esw10gPortTrafficRxFragments':gel2esw10gPortTrafficRxFragments,'gel2esw10gPortTrafficRxJabber':gel2esw10gPortTrafficRxJabber,'gel2esw10gPortTrafficRxFiltered':gel2esw10gPortTrafficRxFiltered,'gel2esw10gPortTrafficTxPackets':gel2esw10gPortTrafficTxPackets,'gel2esw10gPortTrafficTxOctets':gel2esw10gPortTrafficTxOctets,'gel2esw10gPortTrafficTxUnicast':gel2esw10gPortTrafficTxUnicast,'gel2esw10gPortTrafficTxMulticast':gel2esw10gPortTrafficTxMulticast,'gel2esw10gPortTrafficTxBroadcast':gel2esw10gPortTrafficTxBroadcast,'gel2esw10gPortTrafficTxPause':gel2esw10gPortTrafficTxPause,'gel2esw10gPortTrafficTx64Bytes':gel2esw10gPortTrafficTx64Bytes,'gel2esw10gPortTrafficTx65to127Bytes':gel2esw10gPortTrafficTx65to127Bytes,'gel2esw10gPortTrafficTx128to255Bytes':gel2esw10gPortTrafficTx128to255Bytes,'gel2esw10gPortTrafficTx256to511Bytes':gel2esw10gPortTrafficTx256to511Bytes,'gel2esw10gPortTrafficTx512to1023Bytes':gel2esw10gPortTrafficTx512to1023Bytes,'gel2esw10gPortTrafficTx1024to1526Bytes':gel2esw10gPortTrafficTx1024to1526Bytes,'gel2esw10gPortTrafficTxExceecd1527Bytes':gel2esw10gPortTrafficTxExceecd1527Bytes,'gel2esw10gPortTrafficTxQ0':gel2esw10gPortTrafficTxQ0,'gel2esw10gPortTrafficTxQ1':gel2esw10gPortTrafficTxQ1,'gel2esw10gPortTrafficTxQ2':gel2esw10gPortTrafficTxQ2,'gel2esw10gPortTrafficTxQ3':gel2esw10gPortTrafficTxQ3,'gel2esw10gPortTrafficTxQ4':gel2esw10gPortTrafficTxQ4,'gel2esw10gPortTrafficTxQ5':gel2esw10gPortTrafficTxQ5,'gel2esw10gPortTrafficTxQ6':gel2esw10gPortTrafficTxQ6,'gel2esw10gPortTrafficTxQ7':gel2esw10gPortTrafficTxQ7,'gel2esw10gPortTrafficTxDrops':gel2esw10gPortTrafficTxDrops,'gel2esw10gPortTrafficTxLateOrExcColl':gel2esw10gPortTrafficTxLateOrExcColl,'gel2esw10gPortQoSStatistics':gel2esw10gPortQoSStatistics,'gel2esw10gPortQoSStatisticsClear':gel2esw10gPortQoSStatisticsClear,'gel2esw10gPortQoSStatisticsTable':gel2esw10gPortQoSStatisticsTable,'gel2esw10gPortQoSStatisticsEntry':gel2esw10gPortQoSStatisticsEntry,_Q:gel2esw10gPortQoSStatisticsPort,'gel2esw10gPortQoSQ0Rx':gel2esw10gPortQoSQ0Rx,'gel2esw10gPortQoSQ0Tx':gel2esw10gPortQoSQ0Tx,'gel2esw10gPortQoSQ1Rx':gel2esw10gPortQoSQ1Rx,'gel2esw10gPortQoSQ1Tx':gel2esw10gPortQoSQ1Tx,'gel2esw10gPortQoSQ2Rx':gel2esw10gPortQoSQ2Rx,'gel2esw10gPortQoSQ2Tx':gel2esw10gPortQoSQ2Tx,'gel2esw10gPortQoSQ3Rx':gel2esw10gPortQoSQ3Rx,'gel2esw10gPortQoSQ3Tx':gel2esw10gPortQoSQ3Tx,'gel2esw10gPortQoSQ4Rx':gel2esw10gPortQoSQ4Rx,'gel2esw10gPortQoSQ4Tx':gel2esw10gPortQoSQ4Tx,'gel2esw10gPortQoSQ5Rx':gel2esw10gPortQoSQ5Rx,'gel2esw10gPortQoSQ5Tx':gel2esw10gPortQoSQ5Tx,'gel2esw10gPortQoSQ6Rx':gel2esw10gPortQoSQ6Rx,'gel2esw10gPortQoSQ6Tx':gel2esw10gPortQoSQ6Tx,'gel2esw10gPortQoSQ7Rx':gel2esw10gPortQoSQ7Rx,'gel2esw10gPortQoSQ7Tx':gel2esw10gPortQoSQ7Tx,'gel2esw10gSFPInfoTable':gel2esw10gSFPInfoTable,'gel2esw10gSFPInfoEntry':gel2esw10gSFPInfoEntry,_R:gel2esw10gSFPInfoIndex,'gel2esw10gSFPInfoPort':gel2esw10gSFPInfoPort,'gel2esw10gSFPConnectorType':gel2esw10gSFPConnectorType,'gel2esw10gSFPFiberType':gel2esw10gSFPFiberType,'gel2esw10gSFPTxCentralWavelength':gel2esw10gSFPTxCentralWavelength,'gel2esw10gSFPBaudRate':gel2esw10gSFPBaudRate,'gel2esw10gSFPVendorOUI':gel2esw10gSFPVendorOUI,'gel2esw10gSFPVendorName':gel2esw10gSFPVendorName,'gel2esw10gSFPVendorPN':gel2esw10gSFPVendorPN,'gel2esw10gSFPVendorRev':gel2esw10gSFPVendorRev,'gel2esw10gSFPVendorSN':gel2esw10gSFPVendorSN,'gel2esw10gSFPDateCode':gel2esw10gSFPDateCode,'gel2esw10gSFPTemperature':gel2esw10gSFPTemperature,'gel2esw10gSFPVcc':gel2esw10gSFPVcc,'gel2esw10gSFPMon1Bias':gel2esw10gSFPMon1Bias,'gel2esw10gSFPMon2TxPWR':gel2esw10gSFPMon2TxPWR,'gel2esw10gSFPMon3RxPWR':gel2esw10gSFPMon3RxPWR,'gel2esw10gPortEEETable':gel2esw10gPortEEETable,'gel2esw10gPortEEEEntry':gel2esw10gPortEEEEntry,_S:gel2esw10gPortEEEPort,'gel2esw10gPortEEEMode':gel2esw10gPortEEEMode,'gel2esw10gPortEEEUrgentQueue1':gel2esw10gPortEEEUrgentQueue1,'gel2esw10gPortEEEUrgentQueue2':gel2esw10gPortEEEUrgentQueue2,'gel2esw10gPortEEEUrgentQueue3':gel2esw10gPortEEEUrgentQueue3,'gel2esw10gPortEEEUrgentQueue4':gel2esw10gPortEEEUrgentQueue4,'gel2esw10gPortEEEUrgentQueue5':gel2esw10gPortEEEUrgentQueue5,'gel2esw10gPortEEEUrgentQueue6':gel2esw10gPortEEEUrgentQueue6,'gel2esw10gPortEEEUrgentQueue7':gel2esw10gPortEEEUrgentQueue7,'gel2esw10gPortEEEUrgentQueue8':gel2esw10gPortEEEUrgentQueue8,'gel2esw10gVoiceVLAN':gel2esw10gVoiceVLAN,'gel2esw10gVoiceVLANConf':gel2esw10gVoiceVLANConf,'gel2esw10gVoiceVLANMode':gel2esw10gVoiceVLANMode,'gel2esw10gVoiceVLANVLANId':gel2esw10gVoiceVLANVLANId,'gel2esw10gVoiceVLANAgingTime':gel2esw10gVoiceVLANAgingTime,'gel2esw10gVoiceVLANTrafficClass':gel2esw10gVoiceVLANTrafficClass,'gel2esw10gVoiceVLANPortTable':gel2esw10gVoiceVLANPortTable,'gel2esw10gVoiceVLANPortEntry':gel2esw10gVoiceVLANPortEntry,_T:gel2esw10gVoiceVLANPort,'gel2esw10gVoiceVLANPortMode':gel2esw10gVoiceVLANPortMode,'gel2esw10gVoiceVLANPortSecurity':gel2esw10gVoiceVLANPortSecurity,'gel2esw10gVoiceVLANPortDiscoveryProtocol':gel2esw10gVoiceVLANPortDiscoveryProtocol,'gel2esw10gVoiceVLANOUI':gel2esw10gVoiceVLANOUI,'gel2esw10gVoiceVLANOUICreate':gel2esw10gVoiceVLANOUICreate,'gel2esw10gVoiceVLANOUITable':gel2esw10gVoiceVLANOUITable,'gel2esw10gVoiceVLANOUIEntry':gel2esw10gVoiceVLANOUIEntry,_U:gel2esw10gVoiceVLANOUIIndex,'gel2esw10gVoiceVLANTelephonyOUI':gel2esw10gVoiceVLANTelephonyOUI,'gel2esw10gVoiceVLANDescription':gel2esw10gVoiceVLANDescription,'gel2esw10gVoiceVLANOUIRowStatus':gel2esw10gVoiceVLANOUIRowStatus,'gel2esw10gGARP':gel2esw10gGARP,'gel2esw10gGARPConfTable':gel2esw10gGARPConfTable,'gel2esw10gGARPConfEntry':gel2esw10gGARPConfEntry,_V:gel2esw10gGARPConfPort,'gel2esw10gGARPJoinTimer':gel2esw10gGARPJoinTimer,'gel2esw10gGARPLeaveTimer':gel2esw10gGARPLeaveTimer,'gel2esw10gGARPLeaveAllTimer':gel2esw10gGARPLeaveAllTimer,'gel2esw10gGARPApplicantion':gel2esw10gGARPApplicantion,'gel2esw10gGARPAttributeType':gel2esw10gGARPAttributeType,'gel2esw10gGARPApplicant':gel2esw10gGARPApplicant,'gel2esw10gGARPStatisticsTable':gel2esw10gGARPStatisticsTable,'gel2esw10gGARPStatisticsEntry':gel2esw10gGARPStatisticsEntry,_W:gel2esw10gGARPStatisticsPort,'gel2esw10gGARPStatisticsPeerMAC':gel2esw10gGARPStatisticsPeerMAC,'gel2esw10gGARPStatisticsFailedCount':gel2esw10gGARPStatisticsFailedCount,'gel2esw10gGVRP':gel2esw10gGVRP,'gel2esw10gGVRPConf':gel2esw10gGVRPConf,'gel2esw10gGVRPMode':gel2esw10gGVRPMode,'gel2esw10gGVRPConfTable':gel2esw10gGVRPConfTable,'gel2esw10gGVRPConfEntry':gel2esw10gGVRPConfEntry,_X:gel2esw10gGVRPConfPort,'gel2esw10gGVRPConfPortMode':gel2esw10gGVRPConfPortMode,'gel2esw10gGVRPConfPortRRole':gel2esw10gGVRPConfPortRRole,'gel2esw10gGVRPStatisticsTable':gel2esw10gGVRPStatisticsTable,'gel2esw10gGVRPStatisticsEntry':gel2esw10gGVRPStatisticsEntry,_Y:gel2esw10gGVRPStatisticsPort,'gel2esw10gGVRPStatisticsJoinTxCnt':gel2esw10gGVRPStatisticsJoinTxCnt,'gel2esw10gGVRPStatisticsLeaveTxCnt':gel2esw10gGVRPStatisticsLeaveTxCnt,'gel2esw10gThermalProtection':gel2esw10gThermalProtection,'gel2esw10gPriority0Temperature':gel2esw10gPriority0Temperature,'gel2esw10gPriority1Temperature':gel2esw10gPriority1Temperature,'gel2esw10gPriority2Temperature':gel2esw10gPriority2Temperature,'gel2esw10gPriority3Temperature':gel2esw10gPriority3Temperature,'gel2esw10gThermalProtectionTable':gel2esw10gThermalProtectionTable,'gel2esw10gThermalProtectionEntry':gel2esw10gThermalProtectionEntry,_Z:gel2esw10gThermalProtectionPort,'gel2esw10gThermalProtectionPortTemperature':gel2esw10gThermalProtectionPortTemperature,'gel2esw10gThermalProtectionPortPriority':gel2esw10gThermalProtectionPortPriority,'gel2esw10gThermalProtectionPortStatus':gel2esw10gThermalProtectionPortStatus,'gel2esw10gMirroring':gel2esw10gMirroring,'gel2esw10gPortToMirrorOn':gel2esw10gPortToMirrorOn,'gel2esw10gMirrorTable':gel2esw10gMirrorTable,'gel2esw10gMirrorEntry':gel2esw10gMirrorEntry,_a:gel2esw10gMirrorPort,'gel2esw10gMirrorMode':gel2esw10gMirrorMode,'gel2esw10gTrapEventSeverity':gel2esw10gTrapEventSeverity,'gel2esw10gTrapEventSeverityACL':gel2esw10gTrapEventSeverityACL,'gel2esw10gTrapEventSeverityACLLog':gel2esw10gTrapEventSeverityACLLog,'gel2esw10gTrapEventSeverityAccessMgmt':gel2esw10gTrapEventSeverityAccessMgmt,'gel2esw10gTrapEventSeverityAuthFailed':gel2esw10gTrapEventSeverityAuthFailed,'gel2esw10gTrapEventSeverityColdStart':gel2esw10gTrapEventSeverityColdStart,'gel2esw10gTrapEventSeverityConfigInfo':gel2esw10gTrapEventSeverityConfigInfo,'gel2esw10gTrapEventSeverityFirmwareUpgrade':gel2esw10gTrapEventSeverityFirmwareUpgrade,'gel2esw10gTrapEventSeverityImportExport':gel2esw10gTrapEventSeverityImportExport,'gel2esw10gTrapEventSeverityLACP':gel2esw10gTrapEventSeverityLACP,'gel2esw10gTrapEventSeverityLinkStatus':gel2esw10gTrapEventSeverityLinkStatus,'gel2esw10gTrapEventSeverityLogin':gel2esw10gTrapEventSeverityLogin,'gel2esw10gTrapEventSeverityLogout':gel2esw10gTrapEventSeverityLogout,'gel2esw10gTrapEventSeverityLoopProtect':gel2esw10gTrapEventSeverityLoopProtect,'gel2esw10gTrapEventSeverityMgmtIPChange':gel2esw10gTrapEventSeverityMgmtIPChange,'gel2esw10gTrapEventSeverityModuleChange':gel2esw10gTrapEventSeverityModuleChange,'gel2esw10gTrapEventSeverityNAS':gel2esw10gTrapEventSeverityNAS,'gel2esw10gTrapEventSeverityPasswdChange':gel2esw10gTrapEventSeverityPasswdChange,'gel2esw10gTrapEventSeverityPortSecurity':gel2esw10gTrapEventSeverityPortSecurity,'gel2esw10gTrapEventSeverityThermalProtect':gel2esw10gTrapEventSeverityThermalProtect,'gel2esw10gTrapEventSeverityVLAN':gel2esw10gTrapEventSeverityVLAN,'gel2esw10gTrapEventSeverityWarmStart':gel2esw10gTrapEventSeverityWarmStart,'gel2esw10gSMTP':gel2esw10gSMTP,'gel2esw10gSMTPMailServer':gel2esw10gSMTPMailServer,'gel2esw10gSMTPUserName':gel2esw10gSMTPUserName,'gel2esw10gSMTPPassword':gel2esw10gSMTPPassword,'gel2esw10gSMTPServeriryLevel':gel2esw10gSMTPServeriryLevel,'gel2esw10gSMTPSender':gel2esw10gSMTPSender,'gel2esw10gSMTPReturnPath':gel2esw10gSMTPReturnPath,'gel2esw10gSMTPEmailAddress1':gel2esw10gSMTPEmailAddress1,'gel2esw10gSMTPEmailAddress2':gel2esw10gSMTPEmailAddress2,'gel2esw10gSMTPEmailAddress3':gel2esw10gSMTPEmailAddress3,'gel2esw10gSMTPEmailAddress4':gel2esw10gSMTPEmailAddress4,'gel2esw10gSMTPEmailAddress5':gel2esw10gSMTPEmailAddress5,'gel2esw10gSMTPEmailAddress6':gel2esw10gSMTPEmailAddress6,'gel2esw10gACL':gel2esw10gACL,'gel2esw10gACLPortsConfTable':gel2esw10gACLPortsConfTable,'gel2esw10gACLPortsConfEntry':gel2esw10gACLPortsConfEntry,_b:gel2esw10gACLPortsConfPort,'gel2esw10gACLPortsConfPolicyID':gel2esw10gACLPortsConfPolicyID,'gel2esw10gACLPortsConfAction':gel2esw10gACLPortsConfAction,'gel2esw10gACLPortsConfRateLimiterID':gel2esw10gACLPortsConfRateLimiterID,'gel2esw10gACLPortsConfPortRedirect':gel2esw10gACLPortsConfPortRedirect,'gel2esw10gACLPortsConfMirror':gel2esw10gACLPortsConfMirror,'gel2esw10gACLPortsConfLogging':gel2esw10gACLPortsConfLogging,'gel2esw10gACLPortsConfShutdown':gel2esw10gACLPortsConfShutdown,'gel2esw10gACLPortsConfState':gel2esw10gACLPortsConfState,'gel2esw10gACLPortsConfCounter':gel2esw10gACLPortsConfCounter,'gel2esw10gACLRateLimiterTable':gel2esw10gACLRateLimiterTable,'gel2esw10gACLRateLimiterEntry':gel2esw10gACLRateLimiterEntry,_c:gel2esw10gACLRateLimiterID,'gel2esw10gACLRateLimiterUnit':gel2esw10gACLRateLimiterUnit,'gel2esw10gACLRateLimiterRate':gel2esw10gACLRateLimiterRate,'gel2esw10gACLACE':gel2esw10gACLACE,'gel2esw10gACLACECreate':gel2esw10gACLACECreate,'gel2esw10gACLACETable':gel2esw10gACLACETable,'gel2esw10gACLACEEntry':gel2esw10gACLACEEntry,_d:gel2esw10gACLACEIndex,'gel2esw10gACLACEID':gel2esw10gACLACEID,'gel2esw10gACLACENextID':gel2esw10gACLACENextID,'gel2esw10gACLACEIngressPort':gel2esw10gACLACEIngressPort,'gel2esw10gACLACEPortPolicyNumber':gel2esw10gACLACEPortPolicyNumber,'gel2esw10gACLACEPortPolicyBitmask':gel2esw10gACLACEPortPolicyBitmask,'gel2esw10gACLACEFrameType':gel2esw10gACLACEFrameType,'gel2esw10gACLACEAction':gel2esw10gACLACEAction,'gel2esw10gACLACEDenyPortRedirect':gel2esw10gACLACEDenyPortRedirect,'gel2esw10gACLACELogging':gel2esw10gACLACELogging,'gel2esw10gACLACEMirror':gel2esw10gACLACEMirror,'gel2esw10gACLACERateLimiter':gel2esw10gACLACERateLimiter,'gel2esw10gACLACEShutdown':gel2esw10gACLACEShutdown,'gel2esw10gACLACEVLAN8021QTagged':gel2esw10gACLACEVLAN8021QTagged,'gel2esw10gACLACEVLANTagPriority':gel2esw10gACLACEVLANTagPriority,'gel2esw10gACLACEVLANVID':gel2esw10gACLACEVLANVID,'gel2esw10gACLACEEtherType':gel2esw10gACLACEEtherType,'gel2esw10gACLACESMAC':gel2esw10gACLACESMAC,'gel2esw10gACLACEDMACType':gel2esw10gACLACEDMACType,'gel2esw10gACLACEDMAC':gel2esw10gACLACEDMAC,'gel2esw10gACLACEArpOpcode':gel2esw10gACLACEArpOpcode,'gel2esw10gACLACEArpFlagsRequestReply':gel2esw10gACLACEArpFlagsRequestReply,'gel2esw10gACLACEArpFlagsArpSmac':gel2esw10gACLACEArpFlagsArpSmac,'gel2esw10gACLACEArpFlagsRarpDmac':gel2esw10gACLACEArpFlagsRarpDmac,'gel2esw10gACLACEArpFlagsLength':gel2esw10gACLACEArpFlagsLength,'gel2esw10gACLACEArpFlagsIp':gel2esw10gACLACEArpFlagsIp,'gel2esw10gACLACEArpFlagsEthernet':gel2esw10gACLACEArpFlagsEthernet,'gel2esw10gACLACESIPType':gel2esw10gACLACESIPType,'gel2esw10gACLACESIPIPAddress':gel2esw10gACLACESIPIPAddress,'gel2esw10gACLACESIPNetworkPrefix':gel2esw10gACLACESIPNetworkPrefix,'gel2esw10gACLACEDIPType':gel2esw10gACLACEDIPType,'gel2esw10gACLACEDIPIPAddress':gel2esw10gACLACEDIPIPAddress,'gel2esw10gACLACEDIPNetworkPrefix':gel2esw10gACLACEDIPNetworkPrefix,'gel2esw10gACLACEIPProtocol':gel2esw10gACLACEIPProtocol,'gel2esw10gACLACEIPFlagsTTL':gel2esw10gACLACEIPFlagsTTL,'gel2esw10gACLACEIPFlagsOptions':gel2esw10gACLACEIPFlagsOptions,'gel2esw10gACLACEIPFlagsFragment':gel2esw10gACLACEIPFlagsFragment,'gel2esw10gACLACEICMPType':gel2esw10gACLACEICMPType,'gel2esw10gACLACEICMPCode':gel2esw10gACLACEICMPCode,'gel2esw10gACLACESourcePortMin':gel2esw10gACLACESourcePortMin,'gel2esw10gACLACESourcePortMax':gel2esw10gACLACESourcePortMax,'gel2esw10gACLACEDestPortMin':gel2esw10gACLACEDestPortMin,'gel2esw10gACLACEDestPortMax':gel2esw10gACLACEDestPortMax,'gel2esw10gACLACETCPFlagsFin':gel2esw10gACLACETCPFlagsFin,'gel2esw10gACLACETCPFlagsSyn':gel2esw10gACLACETCPFlagsSyn,'gel2esw10gACLACETCPFlagsRst':gel2esw10gACLACETCPFlagsRst,'gel2esw10gACLACETCPFlagsPsh':gel2esw10gACLACETCPFlagsPsh,'gel2esw10gACLACETCPFlagsAck':gel2esw10gACLACETCPFlagsAck,'gel2esw10gACLACETCPFlagsUrg':gel2esw10gACLACETCPFlagsUrg,'gel2esw10gACLACERowStatus':gel2esw10gACLACERowStatus,'gel2esw10gACLACEClear':gel2esw10gACLACEClear,'gel2esw10gACLACEMoveACEID':gel2esw10gACLACEMoveACEID,'gel2esw10gACLACEMoveNextACEID':gel2esw10gACLACEMoveNextACEID,'gel2esw10gACLACEStatusTable':gel2esw10gACLACEStatusTable,'gel2esw10gACLACEStatusEntry':gel2esw10gACLACEStatusEntry,_e:gel2esw10gACLACEStatusIndex,'gel2esw10gACLACEStatusUser':gel2esw10gACLACEStatusUser,'gel2esw10gACLACEStatusID':gel2esw10gACLACEStatusID,'gel2esw10gACLACEStatusIngressPort':gel2esw10gACLACEStatusIngressPort,'gel2esw10gACLACEStatusFrameType':gel2esw10gACLACEStatusFrameType,'gel2esw10gACLACEStatusAction':gel2esw10gACLACEStatusAction,'gel2esw10gACLACEStatusRateLimiter':gel2esw10gACLACEStatusRateLimiter,'gel2esw10gACLACEStatusPortCopy':gel2esw10gACLACEStatusPortCopy,'gel2esw10gACLACEStatusMirror':gel2esw10gACLACEStatusMirror,'gel2esw10gACLACEStatusCPU':gel2esw10gACLACEStatusCPU,'gel2esw10gACLACEStatusCounter':gel2esw10gACLACEStatusCounter,'gel2esw10gACLACEStatusConflict':gel2esw10gACLACEStatusConflict,'gel2esw10gSecurity':gel2esw10gSecurity,'gel2esw10gIPSourceGuard':gel2esw10gIPSourceGuard,'gel2esw10gIPSourceGuardConf':gel2esw10gIPSourceGuardConf,'gel2esw10gIPSourceGuardMode':gel2esw10gIPSourceGuardMode,'gel2esw10gIPSourceGuardPortConfigTable':gel2esw10gIPSourceGuardPortConfigTable,'gel2esw10gIPSourceGuardPortConfigEntry':gel2esw10gIPSourceGuardPortConfigEntry,_f:gel2esw10gIPSourceGuardPortConfigPort,'gel2esw10gIPSourceGuardPortConfigMode':gel2esw10gIPSourceGuardPortConfigMode,'gel2esw10gIPSourceGuardPortMaxDynamicClients':gel2esw10gIPSourceGuardPortMaxDynamicClients,'gel2esw10gIPSourceGuardStatic':gel2esw10gIPSourceGuardStatic,'gel2esw10gIPSourceGuardStaticCreate':gel2esw10gIPSourceGuardStaticCreate,'gel2esw10gIPSourceGuardStaticTable':gel2esw10gIPSourceGuardStaticTable,'gel2esw10gIPSourceGuardStaticEntry':gel2esw10gIPSourceGuardStaticEntry,_g:gel2esw10gIPSourceGuardStaticIndex,'gel2esw10gIPSourceGuardStaticPort':gel2esw10gIPSourceGuardStaticPort,'gel2esw10gIPSourceGuardStaticVLANId':gel2esw10gIPSourceGuardStaticVLANId,'gel2esw10gIPSourceGuardStaticIPAddress':gel2esw10gIPSourceGuardStaticIPAddress,'gel2esw10gIPSourceGuardStaticMACAddress':gel2esw10gIPSourceGuardStaticMACAddress,'gel2esw10gIPSourceGuardStaticRowStatus':gel2esw10gIPSourceGuardStaticRowStatus,'gel2esw10gIPSourceGuardDynamicTable':gel2esw10gIPSourceGuardDynamicTable,'gel2esw10gIPSourceGuardDynamicEntry':gel2esw10gIPSourceGuardDynamicEntry,_h:gel2esw10gIPSourceGuardDynamicIndex,'gel2esw10gIPSourceGuardDynamicPort':gel2esw10gIPSourceGuardDynamicPort,'gel2esw10gIPSourceGuardDynamicVLANId':gel2esw10gIPSourceGuardDynamicVLANId,'gel2esw10gIPSourceGuardDynamicIPAddress':gel2esw10gIPSourceGuardDynamicIPAddress,'gel2esw10gIPSourceGuardDynamicMACAddress':gel2esw10gIPSourceGuardDynamicMACAddress,'gel2esw10gARPInspection':gel2esw10gARPInspection,'gel2esw10gARPInspectionConf':gel2esw10gARPInspectionConf,'gel2esw10gARPInspectionConfMode':gel2esw10gARPInspectionConfMode,'gel2esw10gARPInspectionConfTable':gel2esw10gARPInspectionConfTable,'gel2esw10gARPInspectionConfEntry':gel2esw10gARPInspectionConfEntry,_i:gel2esw10gARPInspectionConfPortIndex,'gel2esw10gARPInspectionConfPortMode':gel2esw10gARPInspectionConfPortMode,'gel2esw10gARPInspectionStatic':gel2esw10gARPInspectionStatic,'gel2esw10gARPInspectionStaticCreate':gel2esw10gARPInspectionStaticCreate,'gel2esw10gARPInspectionStaticTable':gel2esw10gARPInspectionStaticTable,'gel2esw10gARPInspectionStaticEntry':gel2esw10gARPInspectionStaticEntry,_j:gel2esw10gARPInspectionStaticIndex,'gel2esw10gARPInspectionStaticPort':gel2esw10gARPInspectionStaticPort,'gel2esw10gARPInspectionStaticVLANId':gel2esw10gARPInspectionStaticVLANId,'gel2esw10gARPInspectionStaticIPAddress':gel2esw10gARPInspectionStaticIPAddress,'gel2esw10gARPInspectionStaticMACAddress':gel2esw10gARPInspectionStaticMACAddress,'gel2esw10gARPInspectionStaticRowStatus':gel2esw10gARPInspectionStaticRowStatus,'gel2esw10gARPInspectionDynamicTable':gel2esw10gARPInspectionDynamicTable,'gel2esw10gARPInspectionDynamicEntry':gel2esw10gARPInspectionDynamicEntry,_k:gel2esw10gARPInspectionDynamicIndex,'gel2esw10gARPInspectionDynamicPort':gel2esw10gARPInspectionDynamicPort,'gel2esw10gARPInspectionDynamicVLANId':gel2esw10gARPInspectionDynamicVLANId,'gel2esw10gARPInspectionDynamicIPAddress':gel2esw10gARPInspectionDynamicIPAddress,'gel2esw10gARPInspectionDynamicMACAddress':gel2esw10gARPInspectionDynamicMACAddress,'gel2esw10gDHCPSnooping':gel2esw10gDHCPSnooping,'gel2esw10gDHCPSnoopingConf':gel2esw10gDHCPSnoopingConf,'gel2esw10gDHCPSnoopingMode':gel2esw10gDHCPSnoopingMode,'gel2esw10gDHCPSnoopingPortModeConfigurationTable':gel2esw10gDHCPSnoopingPortModeConfigurationTable,'gel2esw10gDHCPSnoopingPortModeConfigurationEntry':gel2esw10gDHCPSnoopingPortModeConfigurationEntry,_l:gel2esw10gDHCPSnoopingPortModeConfigurationPort,'gel2esw10gDHCPSnoopingPortModeConfigurationMode':gel2esw10gDHCPSnoopingPortModeConfigurationMode,'gel2esw10gDHCPSnoopingStatisticsTable':gel2esw10gDHCPSnoopingStatisticsTable,'gel2esw10gDHCPSnoopingStatisticsEntry':gel2esw10gDHCPSnoopingStatisticsEntry,_m:gel2esw10gDHCPSnoopingStatisticsPort,'gel2esw10gDHCPSnoopingStatisticsClear':gel2esw10gDHCPSnoopingStatisticsClear,'gel2esw10gDHCPSnoopingRxDiscover':gel2esw10gDHCPSnoopingRxDiscover,'gel2esw10gDHCPSnoopingRxOffer':gel2esw10gDHCPSnoopingRxOffer,'gel2esw10gDHCPSnoopingRxRequest':gel2esw10gDHCPSnoopingRxRequest,'gel2esw10gDHCPSnoopingRxDecline':gel2esw10gDHCPSnoopingRxDecline,'gel2esw10gDHCPSnoopingRxACK':gel2esw10gDHCPSnoopingRxACK,'gel2esw10gDHCPSnoopingRxNAK':gel2esw10gDHCPSnoopingRxNAK,'gel2esw10gDHCPSnoopingRxRelease':gel2esw10gDHCPSnoopingRxRelease,'gel2esw10gDHCPSnoopingRxInform':gel2esw10gDHCPSnoopingRxInform,'gel2esw10gDHCPSnoopingRxLeaseQuery':gel2esw10gDHCPSnoopingRxLeaseQuery,'gel2esw10gDHCPSnoopingRxLeaseUnassigned':gel2esw10gDHCPSnoopingRxLeaseUnassigned,'gel2esw10gDHCPSnoopingRxLeaseUnknown':gel2esw10gDHCPSnoopingRxLeaseUnknown,'gel2esw10gDHCPSnoopingRxLeaseActive':gel2esw10gDHCPSnoopingRxLeaseActive,'gel2esw10gDHCPSnoopingTxDiscover':gel2esw10gDHCPSnoopingTxDiscover,'gel2esw10gDHCPSnoopingTxOffer':gel2esw10gDHCPSnoopingTxOffer,'gel2esw10gDHCPSnoopingTxRequest':gel2esw10gDHCPSnoopingTxRequest,'gel2esw10gDHCPSnoopingTxDecline':gel2esw10gDHCPSnoopingTxDecline,'gel2esw10gDHCPSnoopingTxACK':gel2esw10gDHCPSnoopingTxACK,'gel2esw10gDHCPSnoopingTxNAK':gel2esw10gDHCPSnoopingTxNAK,'gel2esw10gDHCPSnoopingTxRelease':gel2esw10gDHCPSnoopingTxRelease,'gel2esw10gDHCPSnoopingTxInform':gel2esw10gDHCPSnoopingTxInform,'gel2esw10gDHCPSnoopingTxLeaseQuery':gel2esw10gDHCPSnoopingTxLeaseQuery,'gel2esw10gDHCPSnoopingTxLeaseUnassigned':gel2esw10gDHCPSnoopingTxLeaseUnassigned,'gel2esw10gDHCPSnoopingTxLeaseUnknown':gel2esw10gDHCPSnoopingTxLeaseUnknown,'gel2esw10gDHCPSnoopingTxLeaseActive':gel2esw10gDHCPSnoopingTxLeaseActive,'gel2esw10gDHCPRelay':gel2esw10gDHCPRelay,'gel2esw10gDHCPRelayConfiguration':gel2esw10gDHCPRelayConfiguration,'gel2esw10gDHCPRelayMode':gel2esw10gDHCPRelayMode,'gel2esw10gDHCPRelayServer':gel2esw10gDHCPRelayServer,'gel2esw10gDHCPRelayInformationMode':gel2esw10gDHCPRelayInformationMode,'gel2esw10gDHCPRelayInformationPolicy':gel2esw10gDHCPRelayInformationPolicy,'gel2esw10gDHCPRelayStatistics':gel2esw10gDHCPRelayStatistics,'gel2esw10gDHCPRelayServerStatistics':gel2esw10gDHCPRelayServerStatistics,'gel2esw10gServerStatTransmitToServer':gel2esw10gServerStatTransmitToServer,'gel2esw10gServerStatTransmitError':gel2esw10gServerStatTransmitError,'gel2esw10gServerStatReceiveFromServer':gel2esw10gServerStatReceiveFromServer,'gel2esw10gServerStatReceiveMissingAgentOption':gel2esw10gServerStatReceiveMissingAgentOption,'gel2esw10gServerStatReceiveMissingCircuitID':gel2esw10gServerStatReceiveMissingCircuitID,'gel2esw10gServerStatReceiveMissingRemoteID':gel2esw10gServerStatReceiveMissingRemoteID,'gel2esw10gServerStatReceiveBadCircuitID':gel2esw10gServerStatReceiveBadCircuitID,'gel2esw10gServerStatReceiveBadRemoteID':gel2esw10gServerStatReceiveBadRemoteID,'gel2esw10gDHCPRelayClientStatistics':gel2esw10gDHCPRelayClientStatistics,'gel2esw10gClientStatTransmitToClient':gel2esw10gClientStatTransmitToClient,'gel2esw10gClientStatTransmitError':gel2esw10gClientStatTransmitError,'gel2esw10gClientStatReceivefromClient':gel2esw10gClientStatReceivefromClient,'gel2esw10gClientStatReceiveAgentOption':gel2esw10gClientStatReceiveAgentOption,'gel2esw10gClientStatReplaceAgentOption':gel2esw10gClientStatReplaceAgentOption,'gel2esw10gClientStatKeepAgentOption':gel2esw10gClientStatKeepAgentOption,'gel2esw10gClientStatDropAgentOption':gel2esw10gClientStatDropAgentOption,'gel2esw10gPortSecurity':gel2esw10gPortSecurity,'gel2esw10gPortSecLimitCtrl':gel2esw10gPortSecLimitCtrl,'gel2esw10gPortSecLimitCtrlSystemConf':gel2esw10gPortSecLimitCtrlSystemConf,'gel2esw10gPortSecurityMode':gel2esw10gPortSecurityMode,'gel2esw10gPortSecurityAging':gel2esw10gPortSecurityAging,'gel2esw10gPortSecurityAgingPeriod':gel2esw10gPortSecurityAgingPeriod,'gel2esw10gPortSecLimitCtrlTable':gel2esw10gPortSecLimitCtrlTable,'gel2esw10gPortSecLimitCtrlEntry':gel2esw10gPortSecLimitCtrlEntry,_n:gel2esw10gPortSecLimitCtrlPort,'gel2esw10gPortSecLimitCtrlPortMode':gel2esw10gPortSecLimitCtrlPortMode,'gel2esw10gPortSecLimitCtrlPortLimit':gel2esw10gPortSecLimitCtrlPortLimit,'gel2esw10gPortSecLimitCtrlPortAction':gel2esw10gPortSecLimitCtrlPortAction,'gel2esw10gPortSecLimitCtrlPortState':gel2esw10gPortSecLimitCtrlPortState,'gel2esw10gPortSecLimitCtrlPortReOpen':gel2esw10gPortSecLimitCtrlPortReOpen,'gel2esw10gPortSecSwitchStatusTable':gel2esw10gPortSecSwitchStatusTable,'gel2esw10gPortSecSwitchStatusEntry':gel2esw10gPortSecSwitchStatusEntry,_o:gel2esw10gPortSecSwitchStatusPort,'gel2esw10gPortSecSwitchStatusUsers':gel2esw10gPortSecSwitchStatusUsers,'gel2esw10gPortSecSwitchStatusState':gel2esw10gPortSecSwitchStatusState,'gel2esw10gPortSecSwitchStatusMACCountCurrent':gel2esw10gPortSecSwitchStatusMACCountCurrent,'gel2esw10gPortSecSwitchStatusMACCountLimit':gel2esw10gPortSecSwitchStatusMACCountLimit,'gel2esw10gPortSecPortStatus':gel2esw10gPortSecPortStatus,'gel2esw10gPortSecPortStatusPort':gel2esw10gPortSecPortStatusPort,'gel2esw10gPortSecPortStatusTable':gel2esw10gPortSecPortStatusTable,'gel2esw10gPortSecPortStatusEntry':gel2esw10gPortSecPortStatusEntry,_p:gel2esw10gPortSecPortStatusIndex,'gel2esw10gPortSecPortStatusMACAddress':gel2esw10gPortSecPortStatusMACAddress,'gel2esw10gPortSecPortStatusVLANId':gel2esw10gPortSecPortStatusVLANId,'gel2esw10gPortSecPortStatusState':gel2esw10gPortSecPortStatusState,'gel2esw10gPortSecPortStatusTimeOfAddition':gel2esw10gPortSecPortStatusTimeOfAddition,'gel2esw10gPortSecPortStatusAgeAndHold':gel2esw10gPortSecPortStatusAgeAndHold,'gel2esw10gAccessManagement':gel2esw10gAccessManagement,'gel2esw10gAccessMgtConf':gel2esw10gAccessMgtConf,'gel2esw10gAccessMgtConfMode':gel2esw10gAccessMgtConfMode,'gel2esw10gAccessMgtConfCreate':gel2esw10gAccessMgtConfCreate,'gel2esw10gAccessMgtConfTable':gel2esw10gAccessMgtConfTable,'gel2esw10gAccessMgtConfEntry':gel2esw10gAccessMgtConfEntry,_q:gel2esw10gAccessMgtIndex,'gel2esw10gAccessMgtAddresstype':gel2esw10gAccessMgtAddresstype,'gel2esw10gAccessMgtStartIpAddress':gel2esw10gAccessMgtStartIpAddress,'gel2esw10gAccessMgtEndIpAddress':gel2esw10gAccessMgtEndIpAddress,'gel2esw10gAccessMgtHttpHttps':gel2esw10gAccessMgtHttpHttps,'gel2esw10gAccessMgtSNMP':gel2esw10gAccessMgtSNMP,'gel2esw10gAccessMgtTelnetSSH':gel2esw10gAccessMgtTelnetSSH,'gel2esw10gAccessMgtRowStatus':gel2esw10gAccessMgtRowStatus,'gel2esw10gAccessMgtStatistics':gel2esw10gAccessMgtStatistics,'gel2esw10gHttpReceivedPkts':gel2esw10gHttpReceivedPkts,'gel2esw10gHttpAllowedPkts':gel2esw10gHttpAllowedPkts,'gel2esw10gHttpDiscardedPkts':gel2esw10gHttpDiscardedPkts,'gel2esw10gHttpsReceivedPkts':gel2esw10gHttpsReceivedPkts,'gel2esw10gHttpsAllowedPkts':gel2esw10gHttpsAllowedPkts,'gel2esw10gHttpsDiscardedPkts':gel2esw10gHttpsDiscardedPkts,'gel2esw10gSnmpReceivedPkts':gel2esw10gSnmpReceivedPkts,'gel2esw10gSnmpAllowedPkts':gel2esw10gSnmpAllowedPkts,'gel2esw10gSnmpDiscardedPkts':gel2esw10gSnmpDiscardedPkts,'gel2esw10gTelnetReceivedPkts':gel2esw10gTelnetReceivedPkts,'gel2esw10gTelnetAllowedPkts':gel2esw10gTelnetAllowedPkts,'gel2esw10gTelnetDiscardedPkts':gel2esw10gTelnetDiscardedPkts,'gel2esw10gSSHReceivedPkts':gel2esw10gSSHReceivedPkts,'gel2esw10gSSHAllowedPkts':gel2esw10gSSHAllowedPkts,'gel2esw10gSSHDiscardedPkts':gel2esw10gSSHDiscardedPkts,'gel2esw10gAccessMgtStatisticsClearAll':gel2esw10gAccessMgtStatisticsClearAll,'gel2esw10gSSH':gel2esw10gSSH,'gel2esw10gSSHMode':gel2esw10gSSHMode,'gel2esw10gHTTPS':gel2esw10gHTTPS,'gel2esw10gHTTPSMode':gel2esw10gHTTPSMode,'gel2esw10gHTTPSAutoRedirect':gel2esw10gHTTPSAutoRedirect,'gel2esw10gAuthMethod':gel2esw10gAuthMethod,'gel2esw10gConsoleAuthMethod':gel2esw10gConsoleAuthMethod,'gel2esw10gConsoleFallback':gel2esw10gConsoleFallback,'gel2esw10gTelnetAuthMethod':gel2esw10gTelnetAuthMethod,'gel2esw10gTelnetFallback':gel2esw10gTelnetFallback,'gel2esw10gSshAuthMethod':gel2esw10gSshAuthMethod,'gel2esw10gSshFallback':gel2esw10gSshFallback,'gel2esw10gWebAuthMethod':gel2esw10gWebAuthMethod,'gel2esw10gWebFallback':gel2esw10gWebFallback,'gel2esw10gMaintenance':gel2esw10gMaintenance,'gel2esw10gRestartDevice':gel2esw10gRestartDevice,'gel2esw10gFirmware':gel2esw10gFirmware,'gel2esw10gFirmwareIpAddress':gel2esw10gFirmwareIpAddress,'gel2esw10gFirmwareFileName':gel2esw10gFirmwareFileName,'gel2esw10gDoFirmwareUpgrade':gel2esw10gDoFirmwareUpgrade,'gel2esw10gSaveOrRestore':gel2esw10gSaveOrRestore,'gel2esw10gFactoryDefaults':gel2esw10gFactoryDefaults,'gel2esw10gSaveStart':gel2esw10gSaveStart,'gel2esw10gSaveUser':gel2esw10gSaveUser,'gel2esw10gRestoreUser':gel2esw10gRestoreUser,'gel2esw10gExportOrImport':gel2esw10gExportOrImport,'gel2esw10gExportIpAddress':gel2esw10gExportIpAddress,'gel2esw10gExportConfigName':gel2esw10gExportConfigName,'gel2esw10gDoExportConfig':gel2esw10gDoExportConfig,'gel2esw10gImportIpAddress':gel2esw10gImportIpAddress,'gel2esw10gImportConfigName':gel2esw10gImportConfigName,'gel2esw10gDoImportConfig':gel2esw10gDoImportConfig,'gel2esw10gDiagnostics':gel2esw10gDiagnostics,'gel2esw10gPingIpAddress':gel2esw10gPingIpAddress,'gel2esw10gPingSize':gel2esw10gPingSize,'gel2esw10gDoPingConfig':gel2esw10gDoPingConfig,'gel2esw10gPingResult':gel2esw10gPingResult,'gel2esw10gPing6IpAddress':gel2esw10gPing6IpAddress,'gel2esw10gPing6Size':gel2esw10gPing6Size,'gel2esw10gDoPing6Config':gel2esw10gDoPing6Config,'gel2esw10gPing6Result':gel2esw10gPing6Result,'gel2esw10gVeriPHY':gel2esw10gVeriPHY,'gel2esw10gVeriPHYTest':gel2esw10gVeriPHYTest,'gel2esw10gVeriPHYTable':gel2esw10gVeriPHYTable,'gel2esw10gVeriPHYEntry':gel2esw10gVeriPHYEntry,_r:gel2esw10gVeriPHYPort,'gel2esw10gVeriPHYPairA':gel2esw10gVeriPHYPairA,'gel2esw10gVeriPHYLengthA':gel2esw10gVeriPHYLengthA,'gel2esw10gVeriPHYPairB':gel2esw10gVeriPHYPairB,'gel2esw10gVeriPHYLengthB':gel2esw10gVeriPHYLengthB,'gel2esw10gVeriPHYPairC':gel2esw10gVeriPHYPairC,'gel2esw10gVeriPHYLengthC':gel2esw10gVeriPHYLengthC,'gel2esw10gVeriPHYPairD':gel2esw10gVeriPHYPairD,'gel2esw10gVeriPHYLengthD':gel2esw10gVeriPHYLengthD,'gel2esw10gTrap':gel2esw10gTrap,'gel2esw10gTrapEvent':gel2esw10gTrapEvent,'gel2esw10gEmergency':gel2esw10gEmergency,'gel2esw10gAlert':gel2esw10gAlert,'gel2esw10gCritical':gel2esw10gCritical,'gel2esw10gError':gel2esw10gError,'gel2esw10gWarning':gel2esw10gWarning,'gel2esw10gNotice':gel2esw10gNotice,'gel2esw10gInformational':gel2esw10gInformational,'gel2esw10gDebug':gel2esw10gDebug,'gel2esw10gTrapVariable':gel2esw10gTrapVariable,_H:gel2esw10gInformation})