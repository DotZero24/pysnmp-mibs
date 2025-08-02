_s='gel2esw26kVeriPHYPort'
_r='gel2esw26kAccessMgtIndex'
_q='gel2esw26kPortSecPortStatusIndex'
_p='gel2esw26kPortSecSwitchStatusPort'
_o='gel2esw26kPortSecLimitCtrlPort'
_n='gel2esw26kDHCPSnoopingStatisticsPort'
_m='gel2esw26kDHCPSnoopingPortModeConfigurationPort'
_l='gel2esw26kARPInspectionDynamicIndex'
_k='gel2esw26kARPInspectionStaticIndex'
_j='gel2esw26kARPInspectionConfPortIndex'
_i='gel2esw26kIPSourceGuardDynamicIndex'
_h='gel2esw26kIPSourceGuardStaticIndex'
_g='gel2esw26kIPSourceGuardPortConfigPort'
_f='gel2esw26kLoopProtectionStatusPort'
_e='gel2esw26kLoopProtectionConfPort'
_d='gel2esw26kACLACEStatusIndex'
_c='gel2esw26kACLACEIndex'
_b='gel2esw26kACLRateLimiterID'
_a='gel2esw26kACLPortsConfPort'
_Z='gel2esw26kMirrorPort'
_Y='gel2esw26kGVRPStatisticsPort'
_X='gel2esw26kGVRPConfPort'
_W='gel2esw26kGARPStatisticsPort'
_V='gel2esw26kGARPConfPort'
_U='gel2esw26kVoiceVLANOUIIndex'
_T='gel2esw26kVoiceVLANPort'
_S='gel2esw26kPortEEEPort'
_R='gel2esw26kSFPInfoIndex'
_Q='gel2esw26kPortQoSStatisticsPort'
_P='gel2esw26kPortTrafficStatisticsPort'
_O='gel2esw26kPortConfPort'
_N='gel2esw26kTrapHostConfIndex'
_M='gel2esw26kSyslogDetailedInfoIndex'
_L='gel2esw26kUserIndex'
_K='gel2esw26kSystemTimeNTPIndex'
_J='MacAddress'
_I='OctetString'
_H='gel2esw26kInformation'
_G='DisplayString'
_F='not-accessible'
_E='PRIVATETECH-GEL2ESW26K-MIB'
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
_Gel2esw26kProductId_ObjectIdentity=ObjectIdentity
gel2esw26kProductId=_Gel2esw26kProductId_ObjectIdentity((1,3,6,1,4,1,5205,2,54))
_Gel2esw26kSystem_ObjectIdentity=ObjectIdentity
gel2esw26kSystem=_Gel2esw26kSystem_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1))
_Gel2esw26kSystemInformation_ObjectIdentity=ObjectIdentity
gel2esw26kSystemInformation=_Gel2esw26kSystemInformation_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,1))
_Gel2esw26kModelName_Type=DisplayString
_Gel2esw26kModelName_Object=MibScalar
gel2esw26kModelName=_Gel2esw26kModelName_Object((1,3,6,1,4,1,5205,2,54,1,1,1),_Gel2esw26kModelName_Type())
gel2esw26kModelName.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kModelName.setStatus(_A)
_Gel2esw26kBIOSVersion_Type=DisplayString
_Gel2esw26kBIOSVersion_Object=MibScalar
gel2esw26kBIOSVersion=_Gel2esw26kBIOSVersion_Object((1,3,6,1,4,1,5205,2,54,1,1,2),_Gel2esw26kBIOSVersion_Type())
gel2esw26kBIOSVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kBIOSVersion.setStatus(_A)
_Gel2esw26kFirmwareVersion_Type=DisplayString
_Gel2esw26kFirmwareVersion_Object=MibScalar
gel2esw26kFirmwareVersion=_Gel2esw26kFirmwareVersion_Object((1,3,6,1,4,1,5205,2,54,1,1,3),_Gel2esw26kFirmwareVersion_Type())
gel2esw26kFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kFirmwareVersion.setStatus(_A)
_Gel2esw26kHardwareMechanicalVersion_Type=DisplayString
_Gel2esw26kHardwareMechanicalVersion_Object=MibScalar
gel2esw26kHardwareMechanicalVersion=_Gel2esw26kHardwareMechanicalVersion_Object((1,3,6,1,4,1,5205,2,54,1,1,4),_Gel2esw26kHardwareMechanicalVersion_Type())
gel2esw26kHardwareMechanicalVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kHardwareMechanicalVersion.setStatus(_A)
_Gel2esw26kSeriesNumber_Type=DisplayString
_Gel2esw26kSeriesNumber_Object=MibScalar
gel2esw26kSeriesNumber=_Gel2esw26kSeriesNumber_Object((1,3,6,1,4,1,5205,2,54,1,1,5),_Gel2esw26kSeriesNumber_Type())
gel2esw26kSeriesNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSeriesNumber.setStatus(_A)
_Gel2esw26kHostMACAddress_Type=MacAddress
_Gel2esw26kHostMACAddress_Object=MibScalar
gel2esw26kHostMACAddress=_Gel2esw26kHostMACAddress_Object((1,3,6,1,4,1,5205,2,54,1,1,6),_Gel2esw26kHostMACAddress_Type())
gel2esw26kHostMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kHostMACAddress.setStatus(_A)
_Gel2esw26kConsoleBaudrate_Type=DisplayString
_Gel2esw26kConsoleBaudrate_Object=MibScalar
gel2esw26kConsoleBaudrate=_Gel2esw26kConsoleBaudrate_Object((1,3,6,1,4,1,5205,2,54,1,1,7),_Gel2esw26kConsoleBaudrate_Type())
gel2esw26kConsoleBaudrate.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kConsoleBaudrate.setStatus(_A)
_Gel2esw26kRAMSize_Type=DisplayString
_Gel2esw26kRAMSize_Object=MibScalar
gel2esw26kRAMSize=_Gel2esw26kRAMSize_Object((1,3,6,1,4,1,5205,2,54,1,1,8),_Gel2esw26kRAMSize_Type())
gel2esw26kRAMSize.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kRAMSize.setStatus(_A)
_Gel2esw26kFlashSize_Type=DisplayString
_Gel2esw26kFlashSize_Object=MibScalar
gel2esw26kFlashSize=_Gel2esw26kFlashSize_Object((1,3,6,1,4,1,5205,2,54,1,1,9),_Gel2esw26kFlashSize_Type())
gel2esw26kFlashSize.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kFlashSize.setStatus(_A)
_Gel2esw26kBridgeFBDSize_Type=DisplayString
_Gel2esw26kBridgeFBDSize_Object=MibScalar
gel2esw26kBridgeFBDSize=_Gel2esw26kBridgeFBDSize_Object((1,3,6,1,4,1,5205,2,54,1,1,10),_Gel2esw26kBridgeFBDSize_Type())
gel2esw26kBridgeFBDSize.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kBridgeFBDSize.setStatus(_A)
_Gel2esw26kTransmitQueue_Type=DisplayString
_Gel2esw26kTransmitQueue_Object=MibScalar
gel2esw26kTransmitQueue=_Gel2esw26kTransmitQueue_Object((1,3,6,1,4,1,5205,2,54,1,1,11),_Gel2esw26kTransmitQueue_Type())
gel2esw26kTransmitQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kTransmitQueue.setStatus(_A)
_Gel2esw26kMaximumFrameSize_Type=DisplayString
_Gel2esw26kMaximumFrameSize_Object=MibScalar
gel2esw26kMaximumFrameSize=_Gel2esw26kMaximumFrameSize_Object((1,3,6,1,4,1,5205,2,54,1,1,12),_Gel2esw26kMaximumFrameSize_Type())
gel2esw26kMaximumFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kMaximumFrameSize.setStatus(_A)
_Gel2esw26kCPULoad_Type=DisplayString
_Gel2esw26kCPULoad_Object=MibScalar
gel2esw26kCPULoad=_Gel2esw26kCPULoad_Object((1,3,6,1,4,1,5205,2,54,1,1,13),_Gel2esw26kCPULoad_Type())
gel2esw26kCPULoad.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kCPULoad.setStatus(_A)
_Gel2esw26kSystemTime_ObjectIdentity=ObjectIdentity
gel2esw26kSystemTime=_Gel2esw26kSystemTime_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,2))
_Gel2esw26kSystemTimeManual_ObjectIdentity=ObjectIdentity
gel2esw26kSystemTimeManual=_Gel2esw26kSystemTimeManual_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,2,1))
class _Gel2esw26kSystemTimeManualClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kSystemTimeManualClockSource_Type.__name__=_C
_Gel2esw26kSystemTimeManualClockSource_Object=MibScalar
gel2esw26kSystemTimeManualClockSource=_Gel2esw26kSystemTimeManualClockSource_Object((1,3,6,1,4,1,5205,2,54,1,2,1,1),_Gel2esw26kSystemTimeManualClockSource_Type())
gel2esw26kSystemTimeManualClockSource.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualClockSource.setStatus(_A)
_Gel2esw26kSystemTimeManualLocaltime_Type=DisplayString
_Gel2esw26kSystemTimeManualLocaltime_Object=MibScalar
gel2esw26kSystemTimeManualLocaltime=_Gel2esw26kSystemTimeManualLocaltime_Object((1,3,6,1,4,1,5205,2,54,1,2,1,2),_Gel2esw26kSystemTimeManualLocaltime_Type())
gel2esw26kSystemTimeManualLocaltime.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualLocaltime.setStatus(_A)
class _Gel2esw26kSystemTimeManualTimeZoneOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-720,780))
_Gel2esw26kSystemTimeManualTimeZoneOffset_Type.__name__=_C
_Gel2esw26kSystemTimeManualTimeZoneOffset_Object=MibScalar
gel2esw26kSystemTimeManualTimeZoneOffset=_Gel2esw26kSystemTimeManualTimeZoneOffset_Object((1,3,6,1,4,1,5205,2,54,1,2,1,3),_Gel2esw26kSystemTimeManualTimeZoneOffset_Type())
gel2esw26kSystemTimeManualTimeZoneOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualTimeZoneOffset.setStatus(_A)
class _Gel2esw26kSystemTimeManualDaylightSavings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kSystemTimeManualDaylightSavings_Type.__name__=_C
_Gel2esw26kSystemTimeManualDaylightSavings_Object=MibScalar
gel2esw26kSystemTimeManualDaylightSavings=_Gel2esw26kSystemTimeManualDaylightSavings_Object((1,3,6,1,4,1,5205,2,54,1,2,1,4),_Gel2esw26kSystemTimeManualDaylightSavings_Type())
gel2esw26kSystemTimeManualDaylightSavings.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualDaylightSavings.setStatus(_A)
class _Gel2esw26kSystemTimeManualTimeSetOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_Gel2esw26kSystemTimeManualTimeSetOffset_Type.__name__=_C
_Gel2esw26kSystemTimeManualTimeSetOffset_Object=MibScalar
gel2esw26kSystemTimeManualTimeSetOffset=_Gel2esw26kSystemTimeManualTimeSetOffset_Object((1,3,6,1,4,1,5205,2,54,1,2,1,5),_Gel2esw26kSystemTimeManualTimeSetOffset_Type())
gel2esw26kSystemTimeManualTimeSetOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualTimeSetOffset.setStatus(_A)
class _Gel2esw26kSystemTimeManualDaylightSavingsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kSystemTimeManualDaylightSavingsType_Type.__name__=_C
_Gel2esw26kSystemTimeManualDaylightSavingsType_Object=MibScalar
gel2esw26kSystemTimeManualDaylightSavingsType=_Gel2esw26kSystemTimeManualDaylightSavingsType_Object((1,3,6,1,4,1,5205,2,54,1,2,1,6),_Gel2esw26kSystemTimeManualDaylightSavingsType_Type())
gel2esw26kSystemTimeManualDaylightSavingsType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualDaylightSavingsType.setStatus(_A)
_Gel2esw26kSystemTimeManualDaylightSavingsBydatesFrom_Type=DisplayString
_Gel2esw26kSystemTimeManualDaylightSavingsBydatesFrom_Object=MibScalar
gel2esw26kSystemTimeManualDaylightSavingsBydatesFrom=_Gel2esw26kSystemTimeManualDaylightSavingsBydatesFrom_Object((1,3,6,1,4,1,5205,2,54,1,2,1,7),_Gel2esw26kSystemTimeManualDaylightSavingsBydatesFrom_Type())
gel2esw26kSystemTimeManualDaylightSavingsBydatesFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualDaylightSavingsBydatesFrom.setStatus(_A)
_Gel2esw26kSystemTimeManualDaylightSavingsBydatesTo_Type=DisplayString
_Gel2esw26kSystemTimeManualDaylightSavingsBydatesTo_Object=MibScalar
gel2esw26kSystemTimeManualDaylightSavingsBydatesTo=_Gel2esw26kSystemTimeManualDaylightSavingsBydatesTo_Object((1,3,6,1,4,1,5205,2,54,1,2,1,8),_Gel2esw26kSystemTimeManualDaylightSavingsBydatesTo_Type())
gel2esw26kSystemTimeManualDaylightSavingsBydatesTo.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualDaylightSavingsBydatesTo.setStatus(_A)
class _Gel2esw26kSystemTimeManualDaylightSavingsRecurringDayFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringDayFrom_Type.__name__=_C
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringDayFrom_Object=MibScalar
gel2esw26kSystemTimeManualDaylightSavingsRecurringDayFrom=_Gel2esw26kSystemTimeManualDaylightSavingsRecurringDayFrom_Object((1,3,6,1,4,1,5205,2,54,1,2,1,9),_Gel2esw26kSystemTimeManualDaylightSavingsRecurringDayFrom_Type())
gel2esw26kSystemTimeManualDaylightSavingsRecurringDayFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualDaylightSavingsRecurringDayFrom.setStatus(_A)
class _Gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekFrom_Type.__name__=_C
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekFrom_Object=MibScalar
gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekFrom=_Gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekFrom_Object((1,3,6,1,4,1,5205,2,54,1,2,1,10),_Gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekFrom_Type())
gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekFrom.setStatus(_A)
class _Gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthFrom_Type.__name__=_C
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthFrom_Object=MibScalar
gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthFrom=_Gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthFrom_Object((1,3,6,1,4,1,5205,2,54,1,2,1,11),_Gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthFrom_Type())
gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthFrom.setStatus(_A)
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeFrom_Type=DisplayString
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeFrom_Object=MibScalar
gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeFrom=_Gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeFrom_Object((1,3,6,1,4,1,5205,2,54,1,2,1,12),_Gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeFrom_Type())
gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeFrom.setStatus(_A)
class _Gel2esw26kSystemTimeManualDaylightSavingsRecurringDayTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringDayTo_Type.__name__=_C
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringDayTo_Object=MibScalar
gel2esw26kSystemTimeManualDaylightSavingsRecurringDayTo=_Gel2esw26kSystemTimeManualDaylightSavingsRecurringDayTo_Object((1,3,6,1,4,1,5205,2,54,1,2,1,13),_Gel2esw26kSystemTimeManualDaylightSavingsRecurringDayTo_Type())
gel2esw26kSystemTimeManualDaylightSavingsRecurringDayTo.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualDaylightSavingsRecurringDayTo.setStatus(_A)
class _Gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekTo_Type.__name__=_C
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekTo_Object=MibScalar
gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekTo=_Gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekTo_Object((1,3,6,1,4,1,5205,2,54,1,2,1,14),_Gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekTo_Type())
gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekTo.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekTo.setStatus(_A)
class _Gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthTo_Type.__name__=_C
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthTo_Object=MibScalar
gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthTo=_Gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthTo_Object((1,3,6,1,4,1,5205,2,54,1,2,1,15),_Gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthTo_Type())
gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthTo.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthTo.setStatus(_A)
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeTo_Type=DisplayString
_Gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeTo_Object=MibScalar
gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeTo=_Gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeTo_Object((1,3,6,1,4,1,5205,2,54,1,2,1,16),_Gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeTo_Type())
gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeTo.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeTo.setStatus(_A)
_Gel2esw26kSystemTimeNTP_ObjectIdentity=ObjectIdentity
gel2esw26kSystemTimeNTP=_Gel2esw26kSystemTimeNTP_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,2,2))
_Gel2esw26kSystemTimeNTPTable_Object=MibTable
gel2esw26kSystemTimeNTPTable=_Gel2esw26kSystemTimeNTPTable_Object((1,3,6,1,4,1,5205,2,54,1,2,2,1))
if mibBuilder.loadTexts:gel2esw26kSystemTimeNTPTable.setStatus(_A)
_Gel2esw26kSystemTimeNTPEntry_Object=MibTableRow
gel2esw26kSystemTimeNTPEntry=_Gel2esw26kSystemTimeNTPEntry_Object((1,3,6,1,4,1,5205,2,54,1,2,2,1,1))
gel2esw26kSystemTimeNTPEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:gel2esw26kSystemTimeNTPEntry.setStatus(_A)
class _Gel2esw26kSystemTimeNTPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw26kSystemTimeNTPIndex_Type.__name__=_C
_Gel2esw26kSystemTimeNTPIndex_Object=MibTableColumn
gel2esw26kSystemTimeNTPIndex=_Gel2esw26kSystemTimeNTPIndex_Object((1,3,6,1,4,1,5205,2,54,1,2,2,1,1,1),_Gel2esw26kSystemTimeNTPIndex_Type())
gel2esw26kSystemTimeNTPIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kSystemTimeNTPIndex.setStatus(_A)
class _Gel2esw26kSystemTimeNTPServerIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kSystemTimeNTPServerIPType_Type.__name__=_C
_Gel2esw26kSystemTimeNTPServerIPType_Object=MibTableColumn
gel2esw26kSystemTimeNTPServerIPType=_Gel2esw26kSystemTimeNTPServerIPType_Object((1,3,6,1,4,1,5205,2,54,1,2,2,1,1,2),_Gel2esw26kSystemTimeNTPServerIPType_Type())
gel2esw26kSystemTimeNTPServerIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeNTPServerIPType.setStatus(_A)
_Gel2esw26kSystemTimeNTPServer_Type=DisplayString
_Gel2esw26kSystemTimeNTPServer_Object=MibTableColumn
gel2esw26kSystemTimeNTPServer=_Gel2esw26kSystemTimeNTPServer_Object((1,3,6,1,4,1,5205,2,54,1,2,2,1,1,3),_Gel2esw26kSystemTimeNTPServer_Type())
gel2esw26kSystemTimeNTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeNTPServer.setStatus(_A)
class _Gel2esw26kSystemTimeNTPCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw26kSystemTimeNTPCurrentMode_Type.__name__=_C
_Gel2esw26kSystemTimeNTPCurrentMode_Object=MibTableColumn
gel2esw26kSystemTimeNTPCurrentMode=_Gel2esw26kSystemTimeNTPCurrentMode_Object((1,3,6,1,4,1,5205,2,54,1,2,2,1,1,4),_Gel2esw26kSystemTimeNTPCurrentMode_Type())
gel2esw26kSystemTimeNTPCurrentMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemTimeNTPCurrentMode.setStatus(_A)
_Gel2esw26kSystemAccount_ObjectIdentity=ObjectIdentity
gel2esw26kSystemAccount=_Gel2esw26kSystemAccount_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,3))
_Gel2esw26kSystemAccountUsers_ObjectIdentity=ObjectIdentity
gel2esw26kSystemAccountUsers=_Gel2esw26kSystemAccountUsers_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,3,1))
class _Gel2esw26kSystemAccountUserCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kSystemAccountUserCreate_Type.__name__=_C
_Gel2esw26kSystemAccountUserCreate_Object=MibScalar
gel2esw26kSystemAccountUserCreate=_Gel2esw26kSystemAccountUserCreate_Object((1,3,6,1,4,1,5205,2,54,1,3,1,1),_Gel2esw26kSystemAccountUserCreate_Type())
gel2esw26kSystemAccountUserCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemAccountUserCreate.setStatus(_A)
_Gel2esw26kSystemAccountUsersTable_Object=MibTable
gel2esw26kSystemAccountUsersTable=_Gel2esw26kSystemAccountUsersTable_Object((1,3,6,1,4,1,5205,2,54,1,3,1,2))
if mibBuilder.loadTexts:gel2esw26kSystemAccountUsersTable.setStatus(_A)
_Gel2esw26kSystemAccountUsersEntry_Object=MibTableRow
gel2esw26kSystemAccountUsersEntry=_Gel2esw26kSystemAccountUsersEntry_Object((1,3,6,1,4,1,5205,2,54,1,3,1,2,1))
gel2esw26kSystemAccountUsersEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:gel2esw26kSystemAccountUsersEntry.setStatus(_A)
class _Gel2esw26kUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_Gel2esw26kUserIndex_Type.__name__=_C
_Gel2esw26kUserIndex_Object=MibTableColumn
gel2esw26kUserIndex=_Gel2esw26kUserIndex_Object((1,3,6,1,4,1,5205,2,54,1,3,1,2,1,1),_Gel2esw26kUserIndex_Type())
gel2esw26kUserIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kUserIndex.setStatus(_A)
class _Gel2esw26kUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Gel2esw26kUserName_Type.__name__=_G
_Gel2esw26kUserName_Object=MibTableColumn
gel2esw26kUserName=_Gel2esw26kUserName_Object((1,3,6,1,4,1,5205,2,54,1,3,1,2,1,2),_Gel2esw26kUserName_Type())
gel2esw26kUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kUserName.setStatus(_A)
class _Gel2esw26kPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Gel2esw26kPassword_Type.__name__=_G
_Gel2esw26kPassword_Object=MibTableColumn
gel2esw26kPassword=_Gel2esw26kPassword_Object((1,3,6,1,4,1,5205,2,54,1,3,1,2,1,3),_Gel2esw26kPassword_Type())
gel2esw26kPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPassword.setStatus(_A)
class _Gel2esw26kUserPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kUserPrivilegeLevel_Type.__name__=_C
_Gel2esw26kUserPrivilegeLevel_Object=MibTableColumn
gel2esw26kUserPrivilegeLevel=_Gel2esw26kUserPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,1,2,1,4),_Gel2esw26kUserPrivilegeLevel_Type())
gel2esw26kUserPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kUserPrivilegeLevel.setStatus(_A)
class _Gel2esw26kAccountUserRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw26kAccountUserRowStatus_Type.__name__=_C
_Gel2esw26kAccountUserRowStatus_Object=MibTableColumn
gel2esw26kAccountUserRowStatus=_Gel2esw26kAccountUserRowStatus_Object((1,3,6,1,4,1,5205,2,54,1,3,1,2,1,5),_Gel2esw26kAccountUserRowStatus_Type())
gel2esw26kAccountUserRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kAccountUserRowStatus.setStatus(_A)
_Gel2esw26kSystemAccountPrivilegeLevel_ObjectIdentity=ObjectIdentity
gel2esw26kSystemAccountPrivilegeLevel=_Gel2esw26kSystemAccountPrivilegeLevel_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,3,2))
class _Gel2esw26kAccountPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kAccountPrivilegeLevel_Type.__name__=_C
_Gel2esw26kAccountPrivilegeLevel_Object=MibScalar
gel2esw26kAccountPrivilegeLevel=_Gel2esw26kAccountPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,1),_Gel2esw26kAccountPrivilegeLevel_Type())
gel2esw26kAccountPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kAccountPrivilegeLevel.setStatus(_A)
class _Gel2esw26kAggregationPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kAggregationPrivilegeLevel_Type.__name__=_C
_Gel2esw26kAggregationPrivilegeLevel_Object=MibScalar
gel2esw26kAggregationPrivilegeLevel=_Gel2esw26kAggregationPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,2),_Gel2esw26kAggregationPrivilegeLevel_Type())
gel2esw26kAggregationPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kAggregationPrivilegeLevel.setStatus(_A)
class _Gel2esw26kDiagnosticsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kDiagnosticsPrivilegeLevel_Type.__name__=_C
_Gel2esw26kDiagnosticsPrivilegeLevel_Object=MibScalar
gel2esw26kDiagnosticsPrivilegeLevel=_Gel2esw26kDiagnosticsPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,3),_Gel2esw26kDiagnosticsPrivilegeLevel_Type())
gel2esw26kDiagnosticsPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kDiagnosticsPrivilegeLevel.setStatus(_A)
class _Gel2esw26kEEEPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kEEEPrivilegeLevel_Type.__name__=_C
_Gel2esw26kEEEPrivilegeLevel_Object=MibScalar
gel2esw26kEEEPrivilegeLevel=_Gel2esw26kEEEPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,4),_Gel2esw26kEEEPrivilegeLevel_Type())
gel2esw26kEEEPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kEEEPrivilegeLevel.setStatus(_A)
class _Gel2esw26kEasyportPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kEasyportPrivilegeLevel_Type.__name__=_C
_Gel2esw26kEasyportPrivilegeLevel_Object=MibScalar
gel2esw26kEasyportPrivilegeLevel=_Gel2esw26kEasyportPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,9),_Gel2esw26kEasyportPrivilegeLevel_Type())
gel2esw26kEasyportPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kEasyportPrivilegeLevel.setStatus(_A)
class _Gel2esw26kGARPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kGARPPrivilegeLevel_Type.__name__=_C
_Gel2esw26kGARPPrivilegeLevel_Object=MibScalar
gel2esw26kGARPPrivilegeLevel=_Gel2esw26kGARPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,10),_Gel2esw26kGARPPrivilegeLevel_Type())
gel2esw26kGARPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kGARPPrivilegeLevel.setStatus(_A)
class _Gel2esw26kGVRPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kGVRPPrivilegeLevel_Type.__name__=_C
_Gel2esw26kGVRPPrivilegeLevel_Object=MibScalar
gel2esw26kGVRPPrivilegeLevel=_Gel2esw26kGVRPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,11),_Gel2esw26kGVRPPrivilegeLevel_Type())
gel2esw26kGVRPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kGVRPPrivilegeLevel.setStatus(_A)
class _Gel2esw26kIPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kIPPrivilegeLevel_Type.__name__=_C
_Gel2esw26kIPPrivilegeLevel_Object=MibScalar
gel2esw26kIPPrivilegeLevel=_Gel2esw26kIPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,12),_Gel2esw26kIPPrivilegeLevel_Type())
gel2esw26kIPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPPrivilegeLevel.setStatus(_A)
class _Gel2esw26kIPMCSnoopingPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kIPMCSnoopingPrivilegeLevel_Type.__name__=_C
_Gel2esw26kIPMCSnoopingPrivilegeLevel_Object=MibScalar
gel2esw26kIPMCSnoopingPrivilegeLevel=_Gel2esw26kIPMCSnoopingPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,13),_Gel2esw26kIPMCSnoopingPrivilegeLevel_Type())
gel2esw26kIPMCSnoopingPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPMCSnoopingPrivilegeLevel.setStatus(_A)
class _Gel2esw26kLACPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kLACPPrivilegeLevel_Type.__name__=_C
_Gel2esw26kLACPPrivilegeLevel_Object=MibScalar
gel2esw26kLACPPrivilegeLevel=_Gel2esw26kLACPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,14),_Gel2esw26kLACPPrivilegeLevel_Type())
gel2esw26kLACPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kLACPPrivilegeLevel.setStatus(_A)
class _Gel2esw26kLLDPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kLLDPPrivilegeLevel_Type.__name__=_C
_Gel2esw26kLLDPPrivilegeLevel_Object=MibScalar
gel2esw26kLLDPPrivilegeLevel=_Gel2esw26kLLDPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,15),_Gel2esw26kLLDPPrivilegeLevel_Type())
gel2esw26kLLDPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kLLDPPrivilegeLevel.setStatus(_A)
class _Gel2esw26kLLDPMEDPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kLLDPMEDPrivilegeLevel_Type.__name__=_C
_Gel2esw26kLLDPMEDPrivilegeLevel_Object=MibScalar
gel2esw26kLLDPMEDPrivilegeLevel=_Gel2esw26kLLDPMEDPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,16),_Gel2esw26kLLDPMEDPrivilegeLevel_Type())
gel2esw26kLLDPMEDPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kLLDPMEDPrivilegeLevel.setStatus(_A)
class _Gel2esw26kLoopProtectPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kLoopProtectPrivilegeLevel_Type.__name__=_C
_Gel2esw26kLoopProtectPrivilegeLevel_Object=MibScalar
gel2esw26kLoopProtectPrivilegeLevel=_Gel2esw26kLoopProtectPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,17),_Gel2esw26kLoopProtectPrivilegeLevel_Type())
gel2esw26kLoopProtectPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kLoopProtectPrivilegeLevel.setStatus(_A)
class _Gel2esw26kMACTablePrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kMACTablePrivilegeLevel_Type.__name__=_C
_Gel2esw26kMACTablePrivilegeLevel_Object=MibScalar
gel2esw26kMACTablePrivilegeLevel=_Gel2esw26kMACTablePrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,18),_Gel2esw26kMACTablePrivilegeLevel_Type())
gel2esw26kMACTablePrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kMACTablePrivilegeLevel.setStatus(_A)
class _Gel2esw26kMVRPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kMVRPrivilegeLevel_Type.__name__=_C
_Gel2esw26kMVRPrivilegeLevel_Object=MibScalar
gel2esw26kMVRPrivilegeLevel=_Gel2esw26kMVRPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,22),_Gel2esw26kMVRPrivilegeLevel_Type())
gel2esw26kMVRPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kMVRPrivilegeLevel.setStatus(_A)
class _Gel2esw26kMaintenancePrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kMaintenancePrivilegeLevel_Type.__name__=_C
_Gel2esw26kMaintenancePrivilegeLevel_Object=MibScalar
gel2esw26kMaintenancePrivilegeLevel=_Gel2esw26kMaintenancePrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,24),_Gel2esw26kMaintenancePrivilegeLevel_Type())
gel2esw26kMaintenancePrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kMaintenancePrivilegeLevel.setStatus(_A)
class _Gel2esw26kMirroringPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kMirroringPrivilegeLevel_Type.__name__=_C
_Gel2esw26kMirroringPrivilegeLevel_Object=MibScalar
gel2esw26kMirroringPrivilegeLevel=_Gel2esw26kMirroringPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,25),_Gel2esw26kMirroringPrivilegeLevel_Type())
gel2esw26kMirroringPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kMirroringPrivilegeLevel.setStatus(_A)
class _Gel2esw26kPortsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kPortsPrivilegeLevel_Type.__name__=_C
_Gel2esw26kPortsPrivilegeLevel_Object=MibScalar
gel2esw26kPortsPrivilegeLevel=_Gel2esw26kPortsPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,27),_Gel2esw26kPortsPrivilegeLevel_Type())
gel2esw26kPortsPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortsPrivilegeLevel.setStatus(_A)
class _Gel2esw26kPrivateVLANsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kPrivateVLANsPrivilegeLevel_Type.__name__=_C
_Gel2esw26kPrivateVLANsPrivilegeLevel_Object=MibScalar
gel2esw26kPrivateVLANsPrivilegeLevel=_Gel2esw26kPrivateVLANsPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,28),_Gel2esw26kPrivateVLANsPrivilegeLevel_Type())
gel2esw26kPrivateVLANsPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPrivateVLANsPrivilegeLevel.setStatus(_A)
class _Gel2esw26kQoSPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kQoSPrivilegeLevel_Type.__name__=_C
_Gel2esw26kQoSPrivilegeLevel_Object=MibScalar
gel2esw26kQoSPrivilegeLevel=_Gel2esw26kQoSPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,29),_Gel2esw26kQoSPrivilegeLevel_Type())
gel2esw26kQoSPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kQoSPrivilegeLevel.setStatus(_A)
class _Gel2esw26kSFlowPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kSFlowPrivilegeLevel_Type.__name__=_C
_Gel2esw26kSFlowPrivilegeLevel_Object=MibScalar
gel2esw26kSFlowPrivilegeLevel=_Gel2esw26kSFlowPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,30),_Gel2esw26kSFlowPrivilegeLevel_Type())
gel2esw26kSFlowPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSFlowPrivilegeLevel.setStatus(_A)
class _Gel2esw26kSMTPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kSMTPPrivilegeLevel_Type.__name__=_C
_Gel2esw26kSMTPPrivilegeLevel_Object=MibScalar
gel2esw26kSMTPPrivilegeLevel=_Gel2esw26kSMTPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,31),_Gel2esw26kSMTPPrivilegeLevel_Type())
gel2esw26kSMTPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSMTPPrivilegeLevel.setStatus(_A)
class _Gel2esw26kSNMPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kSNMPPrivilegeLevel_Type.__name__=_C
_Gel2esw26kSNMPPrivilegeLevel_Object=MibScalar
gel2esw26kSNMPPrivilegeLevel=_Gel2esw26kSNMPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,32),_Gel2esw26kSNMPPrivilegeLevel_Type())
gel2esw26kSNMPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSNMPPrivilegeLevel.setStatus(_A)
class _Gel2esw26kSecurityPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kSecurityPrivilegeLevel_Type.__name__=_C
_Gel2esw26kSecurityPrivilegeLevel_Object=MibScalar
gel2esw26kSecurityPrivilegeLevel=_Gel2esw26kSecurityPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,33),_Gel2esw26kSecurityPrivilegeLevel_Type())
gel2esw26kSecurityPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSecurityPrivilegeLevel.setStatus(_A)
class _Gel2esw26kSingleIPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kSingleIPPrivilegeLevel_Type.__name__=_C
_Gel2esw26kSingleIPPrivilegeLevel_Object=MibScalar
gel2esw26kSingleIPPrivilegeLevel=_Gel2esw26kSingleIPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,34),_Gel2esw26kSingleIPPrivilegeLevel_Type())
gel2esw26kSingleIPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSingleIPPrivilegeLevel.setStatus(_A)
class _Gel2esw26kSpanningTreePrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kSpanningTreePrivilegeLevel_Type.__name__=_C
_Gel2esw26kSpanningTreePrivilegeLevel_Object=MibScalar
gel2esw26kSpanningTreePrivilegeLevel=_Gel2esw26kSpanningTreePrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,35),_Gel2esw26kSpanningTreePrivilegeLevel_Type())
gel2esw26kSpanningTreePrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSpanningTreePrivilegeLevel.setStatus(_A)
class _Gel2esw26kSystemPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kSystemPrivilegeLevel_Type.__name__=_C
_Gel2esw26kSystemPrivilegeLevel_Object=MibScalar
gel2esw26kSystemPrivilegeLevel=_Gel2esw26kSystemPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,36),_Gel2esw26kSystemPrivilegeLevel_Type())
gel2esw26kSystemPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSystemPrivilegeLevel.setStatus(_A)
class _Gel2esw26kTrapEventPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kTrapEventPrivilegeLevel_Type.__name__=_C
_Gel2esw26kTrapEventPrivilegeLevel_Object=MibScalar
gel2esw26kTrapEventPrivilegeLevel=_Gel2esw26kTrapEventPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,37),_Gel2esw26kTrapEventPrivilegeLevel_Type())
gel2esw26kTrapEventPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventPrivilegeLevel.setStatus(_A)
class _Gel2esw26kUPnPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kUPnPPrivilegeLevel_Type.__name__=_C
_Gel2esw26kUPnPPrivilegeLevel_Object=MibScalar
gel2esw26kUPnPPrivilegeLevel=_Gel2esw26kUPnPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,38),_Gel2esw26kUPnPPrivilegeLevel_Type())
gel2esw26kUPnPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kUPnPPrivilegeLevel.setStatus(_A)
class _Gel2esw26kVCLPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kVCLPrivilegeLevel_Type.__name__=_C
_Gel2esw26kVCLPrivilegeLevel_Object=MibScalar
gel2esw26kVCLPrivilegeLevel=_Gel2esw26kVCLPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,39),_Gel2esw26kVCLPrivilegeLevel_Type())
gel2esw26kVCLPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kVCLPrivilegeLevel.setStatus(_A)
class _Gel2esw26kVLANsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kVLANsPrivilegeLevel_Type.__name__=_C
_Gel2esw26kVLANsPrivilegeLevel_Object=MibScalar
gel2esw26kVLANsPrivilegeLevel=_Gel2esw26kVLANsPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,41),_Gel2esw26kVLANsPrivilegeLevel_Type())
gel2esw26kVLANsPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kVLANsPrivilegeLevel.setStatus(_A)
class _Gel2esw26kVoiceVLANPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Gel2esw26kVoiceVLANPrivilegeLevel_Type.__name__=_C
_Gel2esw26kVoiceVLANPrivilegeLevel_Object=MibScalar
gel2esw26kVoiceVLANPrivilegeLevel=_Gel2esw26kVoiceVLANPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,54,1,3,2,42),_Gel2esw26kVoiceVLANPrivilegeLevel_Type())
gel2esw26kVoiceVLANPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kVoiceVLANPrivilegeLevel.setStatus(_A)
_Gel2esw26kIP_ObjectIdentity=ObjectIdentity
gel2esw26kIP=_Gel2esw26kIP_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,4))
_Gel2esw26kIPv4_ObjectIdentity=ObjectIdentity
gel2esw26kIPv4=_Gel2esw26kIPv4_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,4,1))
_Gel2esw26kIPv4Configured_ObjectIdentity=ObjectIdentity
gel2esw26kIPv4Configured=_Gel2esw26kIPv4Configured_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,4,1,1))
class _Gel2esw26kIpv4DHCPClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kIpv4DHCPClient_Type.__name__=_C
_Gel2esw26kIpv4DHCPClient_Object=MibScalar
gel2esw26kIpv4DHCPClient=_Gel2esw26kIpv4DHCPClient_Object((1,3,6,1,4,1,5205,2,54,1,4,1,1,1),_Gel2esw26kIpv4DHCPClient_Type())
gel2esw26kIpv4DHCPClient.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIpv4DHCPClient.setStatus(_A)
_Gel2esw26kIPv4Address_Type=IpAddress
_Gel2esw26kIPv4Address_Object=MibScalar
gel2esw26kIPv4Address=_Gel2esw26kIPv4Address_Object((1,3,6,1,4,1,5205,2,54,1,4,1,1,2),_Gel2esw26kIPv4Address_Type())
gel2esw26kIPv4Address.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPv4Address.setStatus(_A)
_Gel2esw26kIPv4Mask_Type=IpAddress
_Gel2esw26kIPv4Mask_Object=MibScalar
gel2esw26kIPv4Mask=_Gel2esw26kIPv4Mask_Object((1,3,6,1,4,1,5205,2,54,1,4,1,1,3),_Gel2esw26kIPv4Mask_Type())
gel2esw26kIPv4Mask.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPv4Mask.setStatus(_A)
_Gel2esw26kIPv4Gateway_Type=IpAddress
_Gel2esw26kIPv4Gateway_Object=MibScalar
gel2esw26kIPv4Gateway=_Gel2esw26kIPv4Gateway_Object((1,3,6,1,4,1,5205,2,54,1,4,1,1,4),_Gel2esw26kIPv4Gateway_Type())
gel2esw26kIPv4Gateway.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPv4Gateway.setStatus(_A)
class _Gel2esw26kIPv4VLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw26kIPv4VLANId_Type.__name__=_C
_Gel2esw26kIPv4VLANId_Object=MibScalar
gel2esw26kIPv4VLANId=_Gel2esw26kIPv4VLANId_Object((1,3,6,1,4,1,5205,2,54,1,4,1,1,5),_Gel2esw26kIPv4VLANId_Type())
gel2esw26kIPv4VLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPv4VLANId.setStatus(_A)
_Gel2esw26kIPv4DNSServer_Type=IpAddress
_Gel2esw26kIPv4DNSServer_Object=MibScalar
gel2esw26kIPv4DNSServer=_Gel2esw26kIPv4DNSServer_Object((1,3,6,1,4,1,5205,2,54,1,4,1,1,6),_Gel2esw26kIPv4DNSServer_Type())
gel2esw26kIPv4DNSServer.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPv4DNSServer.setStatus(_A)
class _Gel2esw26kIPv4DNSProxy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kIPv4DNSProxy_Type.__name__=_C
_Gel2esw26kIPv4DNSProxy_Object=MibScalar
gel2esw26kIPv4DNSProxy=_Gel2esw26kIPv4DNSProxy_Object((1,3,6,1,4,1,5205,2,54,1,4,1,1,7),_Gel2esw26kIPv4DNSProxy_Type())
gel2esw26kIPv4DNSProxy.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPv4DNSProxy.setStatus(_A)
_Gel2esw26kIPv4Current_ObjectIdentity=ObjectIdentity
gel2esw26kIPv4Current=_Gel2esw26kIPv4Current_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,4,1,2))
class _Gel2esw26kIpv4CurrentDHCPClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kIpv4CurrentDHCPClient_Type.__name__=_C
_Gel2esw26kIpv4CurrentDHCPClient_Object=MibScalar
gel2esw26kIpv4CurrentDHCPClient=_Gel2esw26kIpv4CurrentDHCPClient_Object((1,3,6,1,4,1,5205,2,54,1,4,1,2,1),_Gel2esw26kIpv4CurrentDHCPClient_Type())
gel2esw26kIpv4CurrentDHCPClient.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIpv4CurrentDHCPClient.setStatus(_A)
_Gel2esw26kIPv4CurrentAddress_Type=IpAddress
_Gel2esw26kIPv4CurrentAddress_Object=MibScalar
gel2esw26kIPv4CurrentAddress=_Gel2esw26kIPv4CurrentAddress_Object((1,3,6,1,4,1,5205,2,54,1,4,1,2,2),_Gel2esw26kIPv4CurrentAddress_Type())
gel2esw26kIPv4CurrentAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kIPv4CurrentAddress.setStatus(_A)
_Gel2esw26kIPv4CurrentMask_Type=IpAddress
_Gel2esw26kIPv4CurrentMask_Object=MibScalar
gel2esw26kIPv4CurrentMask=_Gel2esw26kIPv4CurrentMask_Object((1,3,6,1,4,1,5205,2,54,1,4,1,2,3),_Gel2esw26kIPv4CurrentMask_Type())
gel2esw26kIPv4CurrentMask.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kIPv4CurrentMask.setStatus(_A)
_Gel2esw26kIPv4CurrentGateway_Type=IpAddress
_Gel2esw26kIPv4CurrentGateway_Object=MibScalar
gel2esw26kIPv4CurrentGateway=_Gel2esw26kIPv4CurrentGateway_Object((1,3,6,1,4,1,5205,2,54,1,4,1,2,4),_Gel2esw26kIPv4CurrentGateway_Type())
gel2esw26kIPv4CurrentGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kIPv4CurrentGateway.setStatus(_A)
class _Gel2esw26kIPv4CurrentVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw26kIPv4CurrentVLANId_Type.__name__=_C
_Gel2esw26kIPv4CurrentVLANId_Object=MibScalar
gel2esw26kIPv4CurrentVLANId=_Gel2esw26kIPv4CurrentVLANId_Object((1,3,6,1,4,1,5205,2,54,1,4,1,2,5),_Gel2esw26kIPv4CurrentVLANId_Type())
gel2esw26kIPv4CurrentVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kIPv4CurrentVLANId.setStatus(_A)
_Gel2esw26kIPv4CurrentDNSServer_Type=IpAddress
_Gel2esw26kIPv4CurrentDNSServer_Object=MibScalar
gel2esw26kIPv4CurrentDNSServer=_Gel2esw26kIPv4CurrentDNSServer_Object((1,3,6,1,4,1,5205,2,54,1,4,1,2,6),_Gel2esw26kIPv4CurrentDNSServer_Type())
gel2esw26kIPv4CurrentDNSServer.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kIPv4CurrentDNSServer.setStatus(_A)
_Gel2esw26kIPv6_ObjectIdentity=ObjectIdentity
gel2esw26kIPv6=_Gel2esw26kIPv6_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,4,2))
_Gel2esw26kIPv6Configured_ObjectIdentity=ObjectIdentity
gel2esw26kIPv6Configured=_Gel2esw26kIPv6Configured_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,4,2,1))
class _Gel2esw26kIpv6AutoConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kIpv6AutoConfiguration_Type.__name__=_C
_Gel2esw26kIpv6AutoConfiguration_Object=MibScalar
gel2esw26kIpv6AutoConfiguration=_Gel2esw26kIpv6AutoConfiguration_Object((1,3,6,1,4,1,5205,2,54,1,4,2,1,1),_Gel2esw26kIpv6AutoConfiguration_Type())
gel2esw26kIpv6AutoConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIpv6AutoConfiguration.setStatus(_A)
class _Gel2esw26kIpv6Address_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Gel2esw26kIpv6Address_Type.__name__=_G
_Gel2esw26kIpv6Address_Object=MibScalar
gel2esw26kIpv6Address=_Gel2esw26kIpv6Address_Object((1,3,6,1,4,1,5205,2,54,1,4,2,1,2),_Gel2esw26kIpv6Address_Type())
gel2esw26kIpv6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIpv6Address.setStatus(_A)
class _Gel2esw26kIpv6Prefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Gel2esw26kIpv6Prefix_Type.__name__=_C
_Gel2esw26kIpv6Prefix_Object=MibScalar
gel2esw26kIpv6Prefix=_Gel2esw26kIpv6Prefix_Object((1,3,6,1,4,1,5205,2,54,1,4,2,1,3),_Gel2esw26kIpv6Prefix_Type())
gel2esw26kIpv6Prefix.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIpv6Prefix.setStatus(_A)
class _Gel2esw26kIpv6Gateway_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Gel2esw26kIpv6Gateway_Type.__name__=_G
_Gel2esw26kIpv6Gateway_Object=MibScalar
gel2esw26kIpv6Gateway=_Gel2esw26kIpv6Gateway_Object((1,3,6,1,4,1,5205,2,54,1,4,2,1,4),_Gel2esw26kIpv6Gateway_Type())
gel2esw26kIpv6Gateway.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIpv6Gateway.setStatus(_A)
_Gel2esw26kIPv6Current_ObjectIdentity=ObjectIdentity
gel2esw26kIPv6Current=_Gel2esw26kIPv6Current_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,4,2,2))
class _Gel2esw26kIpv6CurrentAutoConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kIpv6CurrentAutoConfiguration_Type.__name__=_C
_Gel2esw26kIpv6CurrentAutoConfiguration_Object=MibScalar
gel2esw26kIpv6CurrentAutoConfiguration=_Gel2esw26kIpv6CurrentAutoConfiguration_Object((1,3,6,1,4,1,5205,2,54,1,4,2,2,1),_Gel2esw26kIpv6CurrentAutoConfiguration_Type())
gel2esw26kIpv6CurrentAutoConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kIpv6CurrentAutoConfiguration.setStatus(_A)
class _Gel2esw26kIpv6CurrentAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Gel2esw26kIpv6CurrentAddress_Type.__name__=_G
_Gel2esw26kIpv6CurrentAddress_Object=MibScalar
gel2esw26kIpv6CurrentAddress=_Gel2esw26kIpv6CurrentAddress_Object((1,3,6,1,4,1,5205,2,54,1,4,2,2,2),_Gel2esw26kIpv6CurrentAddress_Type())
gel2esw26kIpv6CurrentAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kIpv6CurrentAddress.setStatus(_A)
class _Gel2esw26kIpv6CurrentLinkLocalAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Gel2esw26kIpv6CurrentLinkLocalAddress_Type.__name__=_G
_Gel2esw26kIpv6CurrentLinkLocalAddress_Object=MibScalar
gel2esw26kIpv6CurrentLinkLocalAddress=_Gel2esw26kIpv6CurrentLinkLocalAddress_Object((1,3,6,1,4,1,5205,2,54,1,4,2,2,3),_Gel2esw26kIpv6CurrentLinkLocalAddress_Type())
gel2esw26kIpv6CurrentLinkLocalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kIpv6CurrentLinkLocalAddress.setStatus(_A)
class _Gel2esw26kIpv6CurrentPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Gel2esw26kIpv6CurrentPrefix_Type.__name__=_C
_Gel2esw26kIpv6CurrentPrefix_Object=MibScalar
gel2esw26kIpv6CurrentPrefix=_Gel2esw26kIpv6CurrentPrefix_Object((1,3,6,1,4,1,5205,2,54,1,4,2,2,4),_Gel2esw26kIpv6CurrentPrefix_Type())
gel2esw26kIpv6CurrentPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kIpv6CurrentPrefix.setStatus(_A)
class _Gel2esw26kIpv6CurrentGateway_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Gel2esw26kIpv6CurrentGateway_Type.__name__=_G
_Gel2esw26kIpv6CurrentGateway_Object=MibScalar
gel2esw26kIpv6CurrentGateway=_Gel2esw26kIpv6CurrentGateway_Object((1,3,6,1,4,1,5205,2,54,1,4,2,2,5),_Gel2esw26kIpv6CurrentGateway_Type())
gel2esw26kIpv6CurrentGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kIpv6CurrentGateway.setStatus(_A)
_Gel2esw26kSyslog_ObjectIdentity=ObjectIdentity
gel2esw26kSyslog=_Gel2esw26kSyslog_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,5))
_Gel2esw26kSyslogConf_ObjectIdentity=ObjectIdentity
gel2esw26kSyslogConf=_Gel2esw26kSyslogConf_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,5,1))
class _Gel2esw26kServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kServerMode_Type.__name__=_C
_Gel2esw26kServerMode_Object=MibScalar
gel2esw26kServerMode=_Gel2esw26kServerMode_Object((1,3,6,1,4,1,5205,2,54,1,5,1,1),_Gel2esw26kServerMode_Type())
gel2esw26kServerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kServerMode.setStatus(_A)
_Gel2esw26kServerAddress1_Type=IpAddress
_Gel2esw26kServerAddress1_Object=MibScalar
gel2esw26kServerAddress1=_Gel2esw26kServerAddress1_Object((1,3,6,1,4,1,5205,2,54,1,5,1,2),_Gel2esw26kServerAddress1_Type())
gel2esw26kServerAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kServerAddress1.setStatus(_A)
_Gel2esw26kServerAddress2_Type=IpAddress
_Gel2esw26kServerAddress2_Object=MibScalar
gel2esw26kServerAddress2=_Gel2esw26kServerAddress2_Object((1,3,6,1,4,1,5205,2,54,1,5,1,3),_Gel2esw26kServerAddress2_Type())
gel2esw26kServerAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kServerAddress2.setStatus(_A)
class _Gel2esw26kSyslogLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kSyslogLevel_Type.__name__=_C
_Gel2esw26kSyslogLevel_Object=MibScalar
gel2esw26kSyslogLevel=_Gel2esw26kSyslogLevel_Object((1,3,6,1,4,1,5205,2,54,1,5,1,4),_Gel2esw26kSyslogLevel_Type())
gel2esw26kSyslogLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSyslogLevel.setStatus(_A)
_Gel2esw26kSyslogDetailedInfo_ObjectIdentity=ObjectIdentity
gel2esw26kSyslogDetailedInfo=_Gel2esw26kSyslogDetailedInfo_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,5,2))
class _Gel2esw26kSyslogDetailedInfoClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kSyslogDetailedInfoClear_Type.__name__=_C
_Gel2esw26kSyslogDetailedInfoClear_Object=MibScalar
gel2esw26kSyslogDetailedInfoClear=_Gel2esw26kSyslogDetailedInfoClear_Object((1,3,6,1,4,1,5205,2,54,1,5,2,1),_Gel2esw26kSyslogDetailedInfoClear_Type())
gel2esw26kSyslogDetailedInfoClear.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSyslogDetailedInfoClear.setStatus(_A)
_Gel2esw26kSyslogDetailedInfoTable_Object=MibTable
gel2esw26kSyslogDetailedInfoTable=_Gel2esw26kSyslogDetailedInfoTable_Object((1,3,6,1,4,1,5205,2,54,1,5,2,2))
if mibBuilder.loadTexts:gel2esw26kSyslogDetailedInfoTable.setStatus(_A)
_Gel2esw26kSyslogDetailedInfoEntry_Object=MibTableRow
gel2esw26kSyslogDetailedInfoEntry=_Gel2esw26kSyslogDetailedInfoEntry_Object((1,3,6,1,4,1,5205,2,54,1,5,2,2,1))
gel2esw26kSyslogDetailedInfoEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:gel2esw26kSyslogDetailedInfoEntry.setStatus(_A)
class _Gel2esw26kSyslogDetailedInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Gel2esw26kSyslogDetailedInfoIndex_Type.__name__=_C
_Gel2esw26kSyslogDetailedInfoIndex_Object=MibTableColumn
gel2esw26kSyslogDetailedInfoIndex=_Gel2esw26kSyslogDetailedInfoIndex_Object((1,3,6,1,4,1,5205,2,54,1,5,2,2,1,1),_Gel2esw26kSyslogDetailedInfoIndex_Type())
gel2esw26kSyslogDetailedInfoIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kSyslogDetailedInfoIndex.setStatus(_A)
_Gel2esw26kSyslogDetailedInfoLevel_Type=DisplayString
_Gel2esw26kSyslogDetailedInfoLevel_Object=MibTableColumn
gel2esw26kSyslogDetailedInfoLevel=_Gel2esw26kSyslogDetailedInfoLevel_Object((1,3,6,1,4,1,5205,2,54,1,5,2,2,1,2),_Gel2esw26kSyslogDetailedInfoLevel_Type())
gel2esw26kSyslogDetailedInfoLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSyslogDetailedInfoLevel.setStatus(_A)
class _Gel2esw26kSyslogDetailedInfoTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_Gel2esw26kSyslogDetailedInfoTime_Type.__name__=_G
_Gel2esw26kSyslogDetailedInfoTime_Object=MibTableColumn
gel2esw26kSyslogDetailedInfoTime=_Gel2esw26kSyslogDetailedInfoTime_Object((1,3,6,1,4,1,5205,2,54,1,5,2,2,1,3),_Gel2esw26kSyslogDetailedInfoTime_Type())
gel2esw26kSyslogDetailedInfoTime.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSyslogDetailedInfoTime.setStatus(_A)
_Gel2esw26kSyslogDetailedInfoMessage_Type=DisplayString
_Gel2esw26kSyslogDetailedInfoMessage_Object=MibTableColumn
gel2esw26kSyslogDetailedInfoMessage=_Gel2esw26kSyslogDetailedInfoMessage_Object((1,3,6,1,4,1,5205,2,54,1,5,2,2,1,4),_Gel2esw26kSyslogDetailedInfoMessage_Type())
gel2esw26kSyslogDetailedInfoMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSyslogDetailedInfoMessage.setStatus(_A)
_Gel2esw26kSnmp_ObjectIdentity=ObjectIdentity
gel2esw26kSnmp=_Gel2esw26kSnmp_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,6))
_Gel2esw26kSnmpConf_ObjectIdentity=ObjectIdentity
gel2esw26kSnmpConf=_Gel2esw26kSnmpConf_ObjectIdentity((1,3,6,1,4,1,5205,2,54,1,6,1))
_Gel2esw26kGetCommunity_Type=DisplayString
_Gel2esw26kGetCommunity_Object=MibScalar
gel2esw26kGetCommunity=_Gel2esw26kGetCommunity_Object((1,3,6,1,4,1,5205,2,54,1,6,1,1),_Gel2esw26kGetCommunity_Type())
gel2esw26kGetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kGetCommunity.setStatus(_A)
class _Gel2esw26kSetCommunityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kSetCommunityMode_Type.__name__=_C
_Gel2esw26kSetCommunityMode_Object=MibScalar
gel2esw26kSetCommunityMode=_Gel2esw26kSetCommunityMode_Object((1,3,6,1,4,1,5205,2,54,1,6,1,2),_Gel2esw26kSetCommunityMode_Type())
gel2esw26kSetCommunityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSetCommunityMode.setStatus(_A)
_Gel2esw26kSetCommunity_Type=DisplayString
_Gel2esw26kSetCommunity_Object=MibScalar
gel2esw26kSetCommunity=_Gel2esw26kSetCommunity_Object((1,3,6,1,4,1,5205,2,54,1,6,1,3),_Gel2esw26kSetCommunity_Type())
gel2esw26kSetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSetCommunity.setStatus(_A)
_Gel2esw26kTrapHostConfTable_Object=MibTable
gel2esw26kTrapHostConfTable=_Gel2esw26kTrapHostConfTable_Object((1,3,6,1,4,1,5205,2,54,1,6,1,4))
if mibBuilder.loadTexts:gel2esw26kTrapHostConfTable.setStatus(_A)
_Gel2esw26kTrapHostConfEntry_Object=MibTableRow
gel2esw26kTrapHostConfEntry=_Gel2esw26kTrapHostConfEntry_Object((1,3,6,1,4,1,5205,2,54,1,6,1,4,1))
gel2esw26kTrapHostConfEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:gel2esw26kTrapHostConfEntry.setStatus(_A)
class _Gel2esw26kTrapHostConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Gel2esw26kTrapHostConfIndex_Type.__name__=_C
_Gel2esw26kTrapHostConfIndex_Object=MibTableColumn
gel2esw26kTrapHostConfIndex=_Gel2esw26kTrapHostConfIndex_Object((1,3,6,1,4,1,5205,2,54,1,6,1,4,1,1),_Gel2esw26kTrapHostConfIndex_Type())
gel2esw26kTrapHostConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kTrapHostConfIndex.setStatus(_A)
class _Gel2esw26kTrapHostConfVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,3))
_Gel2esw26kTrapHostConfVersion_Type.__name__=_C
_Gel2esw26kTrapHostConfVersion_Object=MibTableColumn
gel2esw26kTrapHostConfVersion=_Gel2esw26kTrapHostConfVersion_Object((1,3,6,1,4,1,5205,2,54,1,6,1,4,1,2),_Gel2esw26kTrapHostConfVersion_Type())
gel2esw26kTrapHostConfVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapHostConfVersion.setStatus(_A)
class _Gel2esw26kTrapHostConfIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,4),ValueRangeConstraint(6,6))
_Gel2esw26kTrapHostConfIPType_Type.__name__=_C
_Gel2esw26kTrapHostConfIPType_Object=MibTableColumn
gel2esw26kTrapHostConfIPType=_Gel2esw26kTrapHostConfIPType_Object((1,3,6,1,4,1,5205,2,54,1,6,1,4,1,3),_Gel2esw26kTrapHostConfIPType_Type())
gel2esw26kTrapHostConfIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapHostConfIPType.setStatus(_A)
_Gel2esw26kTrapHostConfIP_Type=DisplayString
_Gel2esw26kTrapHostConfIP_Object=MibTableColumn
gel2esw26kTrapHostConfIP=_Gel2esw26kTrapHostConfIP_Object((1,3,6,1,4,1,5205,2,54,1,6,1,4,1,4),_Gel2esw26kTrapHostConfIP_Type())
gel2esw26kTrapHostConfIP.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapHostConfIP.setStatus(_A)
class _Gel2esw26kTrapHostConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Gel2esw26kTrapHostConfPort_Type.__name__=_C
_Gel2esw26kTrapHostConfPort_Object=MibTableColumn
gel2esw26kTrapHostConfPort=_Gel2esw26kTrapHostConfPort_Object((1,3,6,1,4,1,5205,2,54,1,6,1,4,1,5),_Gel2esw26kTrapHostConfPort_Type())
gel2esw26kTrapHostConfPort.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapHostConfPort.setStatus(_A)
class _Gel2esw26kTrapHostConfCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Gel2esw26kTrapHostConfCommunity_Type.__name__=_G
_Gel2esw26kTrapHostConfCommunity_Object=MibTableColumn
gel2esw26kTrapHostConfCommunity=_Gel2esw26kTrapHostConfCommunity_Object((1,3,6,1,4,1,5205,2,54,1,6,1,4,1,6),_Gel2esw26kTrapHostConfCommunity_Type())
gel2esw26kTrapHostConfCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapHostConfCommunity.setStatus(_A)
class _Gel2esw26kTrapHostConfSeverityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapHostConfSeverityLevel_Type.__name__=_C
_Gel2esw26kTrapHostConfSeverityLevel_Object=MibTableColumn
gel2esw26kTrapHostConfSeverityLevel=_Gel2esw26kTrapHostConfSeverityLevel_Object((1,3,6,1,4,1,5205,2,54,1,6,1,4,1,7),_Gel2esw26kTrapHostConfSeverityLevel_Type())
gel2esw26kTrapHostConfSeverityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapHostConfSeverityLevel.setStatus(_A)
class _Gel2esw26kTrapHostConfSecurityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Gel2esw26kTrapHostConfSecurityLevel_Type.__name__=_C
_Gel2esw26kTrapHostConfSecurityLevel_Object=MibTableColumn
gel2esw26kTrapHostConfSecurityLevel=_Gel2esw26kTrapHostConfSecurityLevel_Object((1,3,6,1,4,1,5205,2,54,1,6,1,4,1,8),_Gel2esw26kTrapHostConfSecurityLevel_Type())
gel2esw26kTrapHostConfSecurityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapHostConfSecurityLevel.setStatus(_A)
class _Gel2esw26kTrapHostConfAuthPtc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Gel2esw26kTrapHostConfAuthPtc_Type.__name__=_C
_Gel2esw26kTrapHostConfAuthPtc_Object=MibTableColumn
gel2esw26kTrapHostConfAuthPtc=_Gel2esw26kTrapHostConfAuthPtc_Object((1,3,6,1,4,1,5205,2,54,1,6,1,4,1,9),_Gel2esw26kTrapHostConfAuthPtc_Type())
gel2esw26kTrapHostConfAuthPtc.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapHostConfAuthPtc.setStatus(_A)
_Gel2esw26kTrapHostConfAuthPassword_Type=DisplayString
_Gel2esw26kTrapHostConfAuthPassword_Object=MibTableColumn
gel2esw26kTrapHostConfAuthPassword=_Gel2esw26kTrapHostConfAuthPassword_Object((1,3,6,1,4,1,5205,2,54,1,6,1,4,1,10),_Gel2esw26kTrapHostConfAuthPassword_Type())
gel2esw26kTrapHostConfAuthPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapHostConfAuthPassword.setStatus(_A)
class _Gel2esw26kTrapHostConfPrivPtc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Gel2esw26kTrapHostConfPrivPtc_Type.__name__=_C
_Gel2esw26kTrapHostConfPrivPtc_Object=MibTableColumn
gel2esw26kTrapHostConfPrivPtc=_Gel2esw26kTrapHostConfPrivPtc_Object((1,3,6,1,4,1,5205,2,54,1,6,1,4,1,11),_Gel2esw26kTrapHostConfPrivPtc_Type())
gel2esw26kTrapHostConfPrivPtc.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapHostConfPrivPtc.setStatus(_A)
_Gel2esw26kTrapHostConfPrivPassword_Type=DisplayString
_Gel2esw26kTrapHostConfPrivPassword_Object=MibTableColumn
gel2esw26kTrapHostConfPrivPassword=_Gel2esw26kTrapHostConfPrivPassword_Object((1,3,6,1,4,1,5205,2,54,1,6,1,4,1,12),_Gel2esw26kTrapHostConfPrivPassword_Type())
gel2esw26kTrapHostConfPrivPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapHostConfPrivPassword.setStatus(_A)
class _Gel2esw26kTrapHostConfCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kTrapHostConfCurrentMode_Type.__name__=_C
_Gel2esw26kTrapHostConfCurrentMode_Object=MibTableColumn
gel2esw26kTrapHostConfCurrentMode=_Gel2esw26kTrapHostConfCurrentMode_Object((1,3,6,1,4,1,5205,2,54,1,6,1,4,1,13),_Gel2esw26kTrapHostConfCurrentMode_Type())
gel2esw26kTrapHostConfCurrentMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapHostConfCurrentMode.setStatus(_A)
_Gel2esw26kConfiguration_ObjectIdentity=ObjectIdentity
gel2esw26kConfiguration=_Gel2esw26kConfiguration_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2))
_Gel2esw26kPort_ObjectIdentity=ObjectIdentity
gel2esw26kPort=_Gel2esw26kPort_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2,1))
_Gel2esw26kPortConfigurationTable_Object=MibTable
gel2esw26kPortConfigurationTable=_Gel2esw26kPortConfigurationTable_Object((1,3,6,1,4,1,5205,2,54,2,1,1))
if mibBuilder.loadTexts:gel2esw26kPortConfigurationTable.setStatus(_A)
_Gel2esw26kPortConfigurationEntry_Object=MibTableRow
gel2esw26kPortConfigurationEntry=_Gel2esw26kPortConfigurationEntry_Object((1,3,6,1,4,1,5205,2,54,2,1,1,1))
gel2esw26kPortConfigurationEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:gel2esw26kPortConfigurationEntry.setStatus(_A)
class _Gel2esw26kPortConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kPortConfPort_Type.__name__=_C
_Gel2esw26kPortConfPort_Object=MibTableColumn
gel2esw26kPortConfPort=_Gel2esw26kPortConfPort_Object((1,3,6,1,4,1,5205,2,54,2,1,1,1,1),_Gel2esw26kPortConfPort_Type())
gel2esw26kPortConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kPortConfPort.setStatus(_A)
class _Gel2esw26kPortConfPortMedia_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_Gel2esw26kPortConfPortMedia_Type.__name__=_G
_Gel2esw26kPortConfPortMedia_Object=MibTableColumn
gel2esw26kPortConfPortMedia=_Gel2esw26kPortConfPortMedia_Object((1,3,6,1,4,1,5205,2,54,2,1,1,1,2),_Gel2esw26kPortConfPortMedia_Type())
gel2esw26kPortConfPortMedia.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortConfPortMedia.setStatus(_A)
class _Gel2esw26kPortConfLink_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,4))
_Gel2esw26kPortConfLink_Type.__name__=_G
_Gel2esw26kPortConfLink_Object=MibTableColumn
gel2esw26kPortConfLink=_Gel2esw26kPortConfLink_Object((1,3,6,1,4,1,5205,2,54,2,1,1,1,3),_Gel2esw26kPortConfLink_Type())
gel2esw26kPortConfLink.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortConfLink.setStatus(_A)
class _Gel2esw26kPortConfCurrentSpeed_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,12))
_Gel2esw26kPortConfCurrentSpeed_Type.__name__=_G
_Gel2esw26kPortConfCurrentSpeed_Object=MibTableColumn
gel2esw26kPortConfCurrentSpeed=_Gel2esw26kPortConfCurrentSpeed_Object((1,3,6,1,4,1,5205,2,54,2,1,1,1,4),_Gel2esw26kPortConfCurrentSpeed_Type())
gel2esw26kPortConfCurrentSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortConfCurrentSpeed.setStatus(_A)
class _Gel2esw26kPortConfSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_Gel2esw26kPortConfSpeed_Type.__name__=_C
_Gel2esw26kPortConfSpeed_Object=MibTableColumn
gel2esw26kPortConfSpeed=_Gel2esw26kPortConfSpeed_Object((1,3,6,1,4,1,5205,2,54,2,1,1,1,5),_Gel2esw26kPortConfSpeed_Type())
gel2esw26kPortConfSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortConfSpeed.setStatus(_A)
class _Gel2esw26kPortConfCurrentFlowControlRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortConfCurrentFlowControlRx_Type.__name__=_C
_Gel2esw26kPortConfCurrentFlowControlRx_Object=MibTableColumn
gel2esw26kPortConfCurrentFlowControlRx=_Gel2esw26kPortConfCurrentFlowControlRx_Object((1,3,6,1,4,1,5205,2,54,2,1,1,1,6),_Gel2esw26kPortConfCurrentFlowControlRx_Type())
gel2esw26kPortConfCurrentFlowControlRx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortConfCurrentFlowControlRx.setStatus(_A)
class _Gel2esw26kPortConfCurrentFlowControlTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortConfCurrentFlowControlTx_Type.__name__=_C
_Gel2esw26kPortConfCurrentFlowControlTx_Object=MibTableColumn
gel2esw26kPortConfCurrentFlowControlTx=_Gel2esw26kPortConfCurrentFlowControlTx_Object((1,3,6,1,4,1,5205,2,54,2,1,1,1,7),_Gel2esw26kPortConfCurrentFlowControlTx_Type())
gel2esw26kPortConfCurrentFlowControlTx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortConfCurrentFlowControlTx.setStatus(_A)
class _Gel2esw26kPortConfFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortConfFlowControl_Type.__name__=_C
_Gel2esw26kPortConfFlowControl_Object=MibTableColumn
gel2esw26kPortConfFlowControl=_Gel2esw26kPortConfFlowControl_Object((1,3,6,1,4,1,5205,2,54,2,1,1,1,8),_Gel2esw26kPortConfFlowControl_Type())
gel2esw26kPortConfFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortConfFlowControl.setStatus(_A)
class _Gel2esw26kPortConfMaxFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1518,9600))
_Gel2esw26kPortConfMaxFrameSize_Type.__name__=_C
_Gel2esw26kPortConfMaxFrameSize_Object=MibTableColumn
gel2esw26kPortConfMaxFrameSize=_Gel2esw26kPortConfMaxFrameSize_Object((1,3,6,1,4,1,5205,2,54,2,1,1,1,9),_Gel2esw26kPortConfMaxFrameSize_Type())
gel2esw26kPortConfMaxFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortConfMaxFrameSize.setStatus(_A)
class _Gel2esw26kPortConfExcessiveCollisionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortConfExcessiveCollisionMode_Type.__name__=_C
_Gel2esw26kPortConfExcessiveCollisionMode_Object=MibTableColumn
gel2esw26kPortConfExcessiveCollisionMode=_Gel2esw26kPortConfExcessiveCollisionMode_Object((1,3,6,1,4,1,5205,2,54,2,1,1,1,10),_Gel2esw26kPortConfExcessiveCollisionMode_Type())
gel2esw26kPortConfExcessiveCollisionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortConfExcessiveCollisionMode.setStatus(_A)
class _Gel2esw26kPortConfPowerControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw26kPortConfPowerControl_Type.__name__=_C
_Gel2esw26kPortConfPowerControl_Object=MibTableColumn
gel2esw26kPortConfPowerControl=_Gel2esw26kPortConfPowerControl_Object((1,3,6,1,4,1,5205,2,54,2,1,1,1,11),_Gel2esw26kPortConfPowerControl_Type())
gel2esw26kPortConfPowerControl.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortConfPowerControl.setStatus(_A)
_Gel2esw26kPortConfDescription_Type=DisplayString
_Gel2esw26kPortConfDescription_Object=MibTableColumn
gel2esw26kPortConfDescription=_Gel2esw26kPortConfDescription_Object((1,3,6,1,4,1,5205,2,54,2,1,1,1,12),_Gel2esw26kPortConfDescription_Type())
gel2esw26kPortConfDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortConfDescription.setStatus(_A)
_Gel2esw26kPortTrafficStatisticsTable_Object=MibTable
gel2esw26kPortTrafficStatisticsTable=_Gel2esw26kPortTrafficStatisticsTable_Object((1,3,6,1,4,1,5205,2,54,2,1,2))
if mibBuilder.loadTexts:gel2esw26kPortTrafficStatisticsTable.setStatus(_A)
_Gel2esw26kPortTrafficStatisticsEntry_Object=MibTableRow
gel2esw26kPortTrafficStatisticsEntry=_Gel2esw26kPortTrafficStatisticsEntry_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1))
gel2esw26kPortTrafficStatisticsEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:gel2esw26kPortTrafficStatisticsEntry.setStatus(_A)
class _Gel2esw26kPortTrafficStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kPortTrafficStatisticsPort_Type.__name__=_C
_Gel2esw26kPortTrafficStatisticsPort_Object=MibTableColumn
gel2esw26kPortTrafficStatisticsPort=_Gel2esw26kPortTrafficStatisticsPort_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,1),_Gel2esw26kPortTrafficStatisticsPort_Type())
gel2esw26kPortTrafficStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kPortTrafficStatisticsPort.setStatus(_A)
class _Gel2esw26kPortTrafficStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortTrafficStatisticsClear_Type.__name__=_C
_Gel2esw26kPortTrafficStatisticsClear_Object=MibTableColumn
gel2esw26kPortTrafficStatisticsClear=_Gel2esw26kPortTrafficStatisticsClear_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,2),_Gel2esw26kPortTrafficStatisticsClear_Type())
gel2esw26kPortTrafficStatisticsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortTrafficStatisticsClear.setStatus(_A)
_Gel2esw26kPortTrafficRxPackets_Type=Counter64
_Gel2esw26kPortTrafficRxPackets_Object=MibTableColumn
gel2esw26kPortTrafficRxPackets=_Gel2esw26kPortTrafficRxPackets_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,3),_Gel2esw26kPortTrafficRxPackets_Type())
gel2esw26kPortTrafficRxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxPackets.setStatus(_A)
_Gel2esw26kPortTrafficRxOctets_Type=Counter64
_Gel2esw26kPortTrafficRxOctets_Object=MibTableColumn
gel2esw26kPortTrafficRxOctets=_Gel2esw26kPortTrafficRxOctets_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,4),_Gel2esw26kPortTrafficRxOctets_Type())
gel2esw26kPortTrafficRxOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxOctets.setStatus(_A)
_Gel2esw26kPortTrafficRxUnicast_Type=Counter64
_Gel2esw26kPortTrafficRxUnicast_Object=MibTableColumn
gel2esw26kPortTrafficRxUnicast=_Gel2esw26kPortTrafficRxUnicast_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,5),_Gel2esw26kPortTrafficRxUnicast_Type())
gel2esw26kPortTrafficRxUnicast.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxUnicast.setStatus(_A)
_Gel2esw26kPortTrafficRxMulticast_Type=Counter64
_Gel2esw26kPortTrafficRxMulticast_Object=MibTableColumn
gel2esw26kPortTrafficRxMulticast=_Gel2esw26kPortTrafficRxMulticast_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,6),_Gel2esw26kPortTrafficRxMulticast_Type())
gel2esw26kPortTrafficRxMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxMulticast.setStatus(_A)
_Gel2esw26kPortTrafficRxBroadcast_Type=Counter64
_Gel2esw26kPortTrafficRxBroadcast_Object=MibTableColumn
gel2esw26kPortTrafficRxBroadcast=_Gel2esw26kPortTrafficRxBroadcast_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,7),_Gel2esw26kPortTrafficRxBroadcast_Type())
gel2esw26kPortTrafficRxBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxBroadcast.setStatus(_A)
_Gel2esw26kPortTrafficRxPause_Type=Counter64
_Gel2esw26kPortTrafficRxPause_Object=MibTableColumn
gel2esw26kPortTrafficRxPause=_Gel2esw26kPortTrafficRxPause_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,8),_Gel2esw26kPortTrafficRxPause_Type())
gel2esw26kPortTrafficRxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxPause.setStatus(_A)
_Gel2esw26kPortTrafficRx64Bytes_Type=Counter64
_Gel2esw26kPortTrafficRx64Bytes_Object=MibTableColumn
gel2esw26kPortTrafficRx64Bytes=_Gel2esw26kPortTrafficRx64Bytes_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,9),_Gel2esw26kPortTrafficRx64Bytes_Type())
gel2esw26kPortTrafficRx64Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRx64Bytes.setStatus(_A)
_Gel2esw26kPortTrafficRx65to127Bytes_Type=Counter64
_Gel2esw26kPortTrafficRx65to127Bytes_Object=MibTableColumn
gel2esw26kPortTrafficRx65to127Bytes=_Gel2esw26kPortTrafficRx65to127Bytes_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,10),_Gel2esw26kPortTrafficRx65to127Bytes_Type())
gel2esw26kPortTrafficRx65to127Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRx65to127Bytes.setStatus(_A)
_Gel2esw26kPortTrafficRx128to255Bytes_Type=Counter64
_Gel2esw26kPortTrafficRx128to255Bytes_Object=MibTableColumn
gel2esw26kPortTrafficRx128to255Bytes=_Gel2esw26kPortTrafficRx128to255Bytes_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,11),_Gel2esw26kPortTrafficRx128to255Bytes_Type())
gel2esw26kPortTrafficRx128to255Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRx128to255Bytes.setStatus(_A)
_Gel2esw26kPortTrafficRx256to511Bytes_Type=Counter64
_Gel2esw26kPortTrafficRx256to511Bytes_Object=MibTableColumn
gel2esw26kPortTrafficRx256to511Bytes=_Gel2esw26kPortTrafficRx256to511Bytes_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,12),_Gel2esw26kPortTrafficRx256to511Bytes_Type())
gel2esw26kPortTrafficRx256to511Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRx256to511Bytes.setStatus(_A)
_Gel2esw26kPortTrafficRx512to1023Bytes_Type=Counter64
_Gel2esw26kPortTrafficRx512to1023Bytes_Object=MibTableColumn
gel2esw26kPortTrafficRx512to1023Bytes=_Gel2esw26kPortTrafficRx512to1023Bytes_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,13),_Gel2esw26kPortTrafficRx512to1023Bytes_Type())
gel2esw26kPortTrafficRx512to1023Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRx512to1023Bytes.setStatus(_A)
_Gel2esw26kPortTrafficRx1024to1526Bytes_Type=Counter64
_Gel2esw26kPortTrafficRx1024to1526Bytes_Object=MibTableColumn
gel2esw26kPortTrafficRx1024to1526Bytes=_Gel2esw26kPortTrafficRx1024to1526Bytes_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,14),_Gel2esw26kPortTrafficRx1024to1526Bytes_Type())
gel2esw26kPortTrafficRx1024to1526Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRx1024to1526Bytes.setStatus(_A)
_Gel2esw26kPortTrafficRxExceecd1527Bytes_Type=Counter64
_Gel2esw26kPortTrafficRxExceecd1527Bytes_Object=MibTableColumn
gel2esw26kPortTrafficRxExceecd1527Bytes=_Gel2esw26kPortTrafficRxExceecd1527Bytes_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,15),_Gel2esw26kPortTrafficRxExceecd1527Bytes_Type())
gel2esw26kPortTrafficRxExceecd1527Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxExceecd1527Bytes.setStatus(_A)
_Gel2esw26kPortTrafficRxQ0_Type=Counter64
_Gel2esw26kPortTrafficRxQ0_Object=MibTableColumn
gel2esw26kPortTrafficRxQ0=_Gel2esw26kPortTrafficRxQ0_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,16),_Gel2esw26kPortTrafficRxQ0_Type())
gel2esw26kPortTrafficRxQ0.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxQ0.setStatus(_A)
_Gel2esw26kPortTrafficRxQ1_Type=Counter64
_Gel2esw26kPortTrafficRxQ1_Object=MibTableColumn
gel2esw26kPortTrafficRxQ1=_Gel2esw26kPortTrafficRxQ1_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,17),_Gel2esw26kPortTrafficRxQ1_Type())
gel2esw26kPortTrafficRxQ1.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxQ1.setStatus(_A)
_Gel2esw26kPortTrafficRxQ2_Type=Counter64
_Gel2esw26kPortTrafficRxQ2_Object=MibTableColumn
gel2esw26kPortTrafficRxQ2=_Gel2esw26kPortTrafficRxQ2_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,18),_Gel2esw26kPortTrafficRxQ2_Type())
gel2esw26kPortTrafficRxQ2.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxQ2.setStatus(_A)
_Gel2esw26kPortTrafficRxQ3_Type=Counter64
_Gel2esw26kPortTrafficRxQ3_Object=MibTableColumn
gel2esw26kPortTrafficRxQ3=_Gel2esw26kPortTrafficRxQ3_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,19),_Gel2esw26kPortTrafficRxQ3_Type())
gel2esw26kPortTrafficRxQ3.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxQ3.setStatus(_A)
_Gel2esw26kPortTrafficRxQ4_Type=Counter64
_Gel2esw26kPortTrafficRxQ4_Object=MibTableColumn
gel2esw26kPortTrafficRxQ4=_Gel2esw26kPortTrafficRxQ4_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,20),_Gel2esw26kPortTrafficRxQ4_Type())
gel2esw26kPortTrafficRxQ4.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxQ4.setStatus(_A)
_Gel2esw26kPortTrafficRxQ5_Type=Counter64
_Gel2esw26kPortTrafficRxQ5_Object=MibTableColumn
gel2esw26kPortTrafficRxQ5=_Gel2esw26kPortTrafficRxQ5_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,21),_Gel2esw26kPortTrafficRxQ5_Type())
gel2esw26kPortTrafficRxQ5.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxQ5.setStatus(_A)
_Gel2esw26kPortTrafficRxQ6_Type=Counter64
_Gel2esw26kPortTrafficRxQ6_Object=MibTableColumn
gel2esw26kPortTrafficRxQ6=_Gel2esw26kPortTrafficRxQ6_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,22),_Gel2esw26kPortTrafficRxQ6_Type())
gel2esw26kPortTrafficRxQ6.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxQ6.setStatus(_A)
_Gel2esw26kPortTrafficRxQ7_Type=Counter64
_Gel2esw26kPortTrafficRxQ7_Object=MibTableColumn
gel2esw26kPortTrafficRxQ7=_Gel2esw26kPortTrafficRxQ7_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,23),_Gel2esw26kPortTrafficRxQ7_Type())
gel2esw26kPortTrafficRxQ7.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxQ7.setStatus(_A)
_Gel2esw26kPortTrafficRxDrops_Type=Counter64
_Gel2esw26kPortTrafficRxDrops_Object=MibTableColumn
gel2esw26kPortTrafficRxDrops=_Gel2esw26kPortTrafficRxDrops_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,24),_Gel2esw26kPortTrafficRxDrops_Type())
gel2esw26kPortTrafficRxDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxDrops.setStatus(_A)
_Gel2esw26kPortTrafficRxCRCorAlignment_Type=Counter64
_Gel2esw26kPortTrafficRxCRCorAlignment_Object=MibTableColumn
gel2esw26kPortTrafficRxCRCorAlignment=_Gel2esw26kPortTrafficRxCRCorAlignment_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,25),_Gel2esw26kPortTrafficRxCRCorAlignment_Type())
gel2esw26kPortTrafficRxCRCorAlignment.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxCRCorAlignment.setStatus(_A)
_Gel2esw26kPortTrafficRxUndersize_Type=Counter64
_Gel2esw26kPortTrafficRxUndersize_Object=MibTableColumn
gel2esw26kPortTrafficRxUndersize=_Gel2esw26kPortTrafficRxUndersize_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,26),_Gel2esw26kPortTrafficRxUndersize_Type())
gel2esw26kPortTrafficRxUndersize.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxUndersize.setStatus(_A)
_Gel2esw26kPortTrafficRxOversize_Type=Counter64
_Gel2esw26kPortTrafficRxOversize_Object=MibTableColumn
gel2esw26kPortTrafficRxOversize=_Gel2esw26kPortTrafficRxOversize_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,27),_Gel2esw26kPortTrafficRxOversize_Type())
gel2esw26kPortTrafficRxOversize.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxOversize.setStatus(_A)
_Gel2esw26kPortTrafficRxFragments_Type=Counter64
_Gel2esw26kPortTrafficRxFragments_Object=MibTableColumn
gel2esw26kPortTrafficRxFragments=_Gel2esw26kPortTrafficRxFragments_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,28),_Gel2esw26kPortTrafficRxFragments_Type())
gel2esw26kPortTrafficRxFragments.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxFragments.setStatus(_A)
_Gel2esw26kPortTrafficRxJabber_Type=Counter64
_Gel2esw26kPortTrafficRxJabber_Object=MibTableColumn
gel2esw26kPortTrafficRxJabber=_Gel2esw26kPortTrafficRxJabber_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,29),_Gel2esw26kPortTrafficRxJabber_Type())
gel2esw26kPortTrafficRxJabber.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxJabber.setStatus(_A)
_Gel2esw26kPortTrafficRxFiltered_Type=Counter64
_Gel2esw26kPortTrafficRxFiltered_Object=MibTableColumn
gel2esw26kPortTrafficRxFiltered=_Gel2esw26kPortTrafficRxFiltered_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,30),_Gel2esw26kPortTrafficRxFiltered_Type())
gel2esw26kPortTrafficRxFiltered.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficRxFiltered.setStatus(_A)
_Gel2esw26kPortTrafficTxPackets_Type=Counter64
_Gel2esw26kPortTrafficTxPackets_Object=MibTableColumn
gel2esw26kPortTrafficTxPackets=_Gel2esw26kPortTrafficTxPackets_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,31),_Gel2esw26kPortTrafficTxPackets_Type())
gel2esw26kPortTrafficTxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxPackets.setStatus(_A)
_Gel2esw26kPortTrafficTxOctets_Type=Counter64
_Gel2esw26kPortTrafficTxOctets_Object=MibTableColumn
gel2esw26kPortTrafficTxOctets=_Gel2esw26kPortTrafficTxOctets_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,32),_Gel2esw26kPortTrafficTxOctets_Type())
gel2esw26kPortTrafficTxOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxOctets.setStatus(_A)
_Gel2esw26kPortTrafficTxUnicast_Type=Counter64
_Gel2esw26kPortTrafficTxUnicast_Object=MibTableColumn
gel2esw26kPortTrafficTxUnicast=_Gel2esw26kPortTrafficTxUnicast_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,33),_Gel2esw26kPortTrafficTxUnicast_Type())
gel2esw26kPortTrafficTxUnicast.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxUnicast.setStatus(_A)
_Gel2esw26kPortTrafficTxMulticast_Type=Counter64
_Gel2esw26kPortTrafficTxMulticast_Object=MibTableColumn
gel2esw26kPortTrafficTxMulticast=_Gel2esw26kPortTrafficTxMulticast_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,34),_Gel2esw26kPortTrafficTxMulticast_Type())
gel2esw26kPortTrafficTxMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxMulticast.setStatus(_A)
_Gel2esw26kPortTrafficTxBroadcast_Type=Counter64
_Gel2esw26kPortTrafficTxBroadcast_Object=MibTableColumn
gel2esw26kPortTrafficTxBroadcast=_Gel2esw26kPortTrafficTxBroadcast_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,35),_Gel2esw26kPortTrafficTxBroadcast_Type())
gel2esw26kPortTrafficTxBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxBroadcast.setStatus(_A)
_Gel2esw26kPortTrafficTxPause_Type=Counter64
_Gel2esw26kPortTrafficTxPause_Object=MibTableColumn
gel2esw26kPortTrafficTxPause=_Gel2esw26kPortTrafficTxPause_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,36),_Gel2esw26kPortTrafficTxPause_Type())
gel2esw26kPortTrafficTxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxPause.setStatus(_A)
_Gel2esw26kPortTrafficTx64Bytes_Type=Counter64
_Gel2esw26kPortTrafficTx64Bytes_Object=MibTableColumn
gel2esw26kPortTrafficTx64Bytes=_Gel2esw26kPortTrafficTx64Bytes_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,37),_Gel2esw26kPortTrafficTx64Bytes_Type())
gel2esw26kPortTrafficTx64Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTx64Bytes.setStatus(_A)
_Gel2esw26kPortTrafficTx65to127Bytes_Type=Counter64
_Gel2esw26kPortTrafficTx65to127Bytes_Object=MibTableColumn
gel2esw26kPortTrafficTx65to127Bytes=_Gel2esw26kPortTrafficTx65to127Bytes_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,38),_Gel2esw26kPortTrafficTx65to127Bytes_Type())
gel2esw26kPortTrafficTx65to127Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTx65to127Bytes.setStatus(_A)
_Gel2esw26kPortTrafficTx128to255Bytes_Type=Counter64
_Gel2esw26kPortTrafficTx128to255Bytes_Object=MibTableColumn
gel2esw26kPortTrafficTx128to255Bytes=_Gel2esw26kPortTrafficTx128to255Bytes_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,39),_Gel2esw26kPortTrafficTx128to255Bytes_Type())
gel2esw26kPortTrafficTx128to255Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTx128to255Bytes.setStatus(_A)
_Gel2esw26kPortTrafficTx256to511Bytes_Type=Counter64
_Gel2esw26kPortTrafficTx256to511Bytes_Object=MibTableColumn
gel2esw26kPortTrafficTx256to511Bytes=_Gel2esw26kPortTrafficTx256to511Bytes_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,40),_Gel2esw26kPortTrafficTx256to511Bytes_Type())
gel2esw26kPortTrafficTx256to511Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTx256to511Bytes.setStatus(_A)
_Gel2esw26kPortTrafficTx512to1023Bytes_Type=Counter64
_Gel2esw26kPortTrafficTx512to1023Bytes_Object=MibTableColumn
gel2esw26kPortTrafficTx512to1023Bytes=_Gel2esw26kPortTrafficTx512to1023Bytes_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,41),_Gel2esw26kPortTrafficTx512to1023Bytes_Type())
gel2esw26kPortTrafficTx512to1023Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTx512to1023Bytes.setStatus(_A)
_Gel2esw26kPortTrafficTx1024to1526Bytes_Type=Counter64
_Gel2esw26kPortTrafficTx1024to1526Bytes_Object=MibTableColumn
gel2esw26kPortTrafficTx1024to1526Bytes=_Gel2esw26kPortTrafficTx1024to1526Bytes_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,42),_Gel2esw26kPortTrafficTx1024to1526Bytes_Type())
gel2esw26kPortTrafficTx1024to1526Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTx1024to1526Bytes.setStatus(_A)
_Gel2esw26kPortTrafficTxExceecd1527Bytes_Type=Counter64
_Gel2esw26kPortTrafficTxExceecd1527Bytes_Object=MibTableColumn
gel2esw26kPortTrafficTxExceecd1527Bytes=_Gel2esw26kPortTrafficTxExceecd1527Bytes_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,43),_Gel2esw26kPortTrafficTxExceecd1527Bytes_Type())
gel2esw26kPortTrafficTxExceecd1527Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxExceecd1527Bytes.setStatus(_A)
_Gel2esw26kPortTrafficTxQ0_Type=Counter64
_Gel2esw26kPortTrafficTxQ0_Object=MibTableColumn
gel2esw26kPortTrafficTxQ0=_Gel2esw26kPortTrafficTxQ0_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,44),_Gel2esw26kPortTrafficTxQ0_Type())
gel2esw26kPortTrafficTxQ0.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxQ0.setStatus(_A)
_Gel2esw26kPortTrafficTxQ1_Type=Counter64
_Gel2esw26kPortTrafficTxQ1_Object=MibTableColumn
gel2esw26kPortTrafficTxQ1=_Gel2esw26kPortTrafficTxQ1_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,45),_Gel2esw26kPortTrafficTxQ1_Type())
gel2esw26kPortTrafficTxQ1.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxQ1.setStatus(_A)
_Gel2esw26kPortTrafficTxQ2_Type=Counter64
_Gel2esw26kPortTrafficTxQ2_Object=MibTableColumn
gel2esw26kPortTrafficTxQ2=_Gel2esw26kPortTrafficTxQ2_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,46),_Gel2esw26kPortTrafficTxQ2_Type())
gel2esw26kPortTrafficTxQ2.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxQ2.setStatus(_A)
_Gel2esw26kPortTrafficTxQ3_Type=Counter64
_Gel2esw26kPortTrafficTxQ3_Object=MibTableColumn
gel2esw26kPortTrafficTxQ3=_Gel2esw26kPortTrafficTxQ3_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,47),_Gel2esw26kPortTrafficTxQ3_Type())
gel2esw26kPortTrafficTxQ3.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxQ3.setStatus(_A)
_Gel2esw26kPortTrafficTxQ4_Type=Counter64
_Gel2esw26kPortTrafficTxQ4_Object=MibTableColumn
gel2esw26kPortTrafficTxQ4=_Gel2esw26kPortTrafficTxQ4_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,48),_Gel2esw26kPortTrafficTxQ4_Type())
gel2esw26kPortTrafficTxQ4.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxQ4.setStatus(_A)
_Gel2esw26kPortTrafficTxQ5_Type=Counter64
_Gel2esw26kPortTrafficTxQ5_Object=MibTableColumn
gel2esw26kPortTrafficTxQ5=_Gel2esw26kPortTrafficTxQ5_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,49),_Gel2esw26kPortTrafficTxQ5_Type())
gel2esw26kPortTrafficTxQ5.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxQ5.setStatus(_A)
_Gel2esw26kPortTrafficTxQ6_Type=Counter64
_Gel2esw26kPortTrafficTxQ6_Object=MibTableColumn
gel2esw26kPortTrafficTxQ6=_Gel2esw26kPortTrafficTxQ6_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,50),_Gel2esw26kPortTrafficTxQ6_Type())
gel2esw26kPortTrafficTxQ6.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxQ6.setStatus(_A)
_Gel2esw26kPortTrafficTxQ7_Type=Counter64
_Gel2esw26kPortTrafficTxQ7_Object=MibTableColumn
gel2esw26kPortTrafficTxQ7=_Gel2esw26kPortTrafficTxQ7_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,51),_Gel2esw26kPortTrafficTxQ7_Type())
gel2esw26kPortTrafficTxQ7.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxQ7.setStatus(_A)
_Gel2esw26kPortTrafficTxDrops_Type=Counter64
_Gel2esw26kPortTrafficTxDrops_Object=MibTableColumn
gel2esw26kPortTrafficTxDrops=_Gel2esw26kPortTrafficTxDrops_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,52),_Gel2esw26kPortTrafficTxDrops_Type())
gel2esw26kPortTrafficTxDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxDrops.setStatus(_A)
_Gel2esw26kPortTrafficTxLateOrExcColl_Type=Counter64
_Gel2esw26kPortTrafficTxLateOrExcColl_Object=MibTableColumn
gel2esw26kPortTrafficTxLateOrExcColl=_Gel2esw26kPortTrafficTxLateOrExcColl_Object((1,3,6,1,4,1,5205,2,54,2,1,2,1,53),_Gel2esw26kPortTrafficTxLateOrExcColl_Type())
gel2esw26kPortTrafficTxLateOrExcColl.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortTrafficTxLateOrExcColl.setStatus(_A)
_Gel2esw26kPortQoSStatistics_ObjectIdentity=ObjectIdentity
gel2esw26kPortQoSStatistics=_Gel2esw26kPortQoSStatistics_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2,1,3))
class _Gel2esw26kPortQoSStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortQoSStatisticsClear_Type.__name__=_C
_Gel2esw26kPortQoSStatisticsClear_Object=MibScalar
gel2esw26kPortQoSStatisticsClear=_Gel2esw26kPortQoSStatisticsClear_Object((1,3,6,1,4,1,5205,2,54,2,1,3,1),_Gel2esw26kPortQoSStatisticsClear_Type())
gel2esw26kPortQoSStatisticsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSStatisticsClear.setStatus(_A)
_Gel2esw26kPortQoSStatisticsTable_Object=MibTable
gel2esw26kPortQoSStatisticsTable=_Gel2esw26kPortQoSStatisticsTable_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2))
if mibBuilder.loadTexts:gel2esw26kPortQoSStatisticsTable.setStatus(_A)
_Gel2esw26kPortQoSStatisticsEntry_Object=MibTableRow
gel2esw26kPortQoSStatisticsEntry=_Gel2esw26kPortQoSStatisticsEntry_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1))
gel2esw26kPortQoSStatisticsEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:gel2esw26kPortQoSStatisticsEntry.setStatus(_A)
class _Gel2esw26kPortQoSStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kPortQoSStatisticsPort_Type.__name__=_C
_Gel2esw26kPortQoSStatisticsPort_Object=MibTableColumn
gel2esw26kPortQoSStatisticsPort=_Gel2esw26kPortQoSStatisticsPort_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,1),_Gel2esw26kPortQoSStatisticsPort_Type())
gel2esw26kPortQoSStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kPortQoSStatisticsPort.setStatus(_A)
_Gel2esw26kPortQoSQ0Rx_Type=Counter64
_Gel2esw26kPortQoSQ0Rx_Object=MibTableColumn
gel2esw26kPortQoSQ0Rx=_Gel2esw26kPortQoSQ0Rx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,2),_Gel2esw26kPortQoSQ0Rx_Type())
gel2esw26kPortQoSQ0Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ0Rx.setStatus(_A)
_Gel2esw26kPortQoSQ0Tx_Type=Counter64
_Gel2esw26kPortQoSQ0Tx_Object=MibTableColumn
gel2esw26kPortQoSQ0Tx=_Gel2esw26kPortQoSQ0Tx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,3),_Gel2esw26kPortQoSQ0Tx_Type())
gel2esw26kPortQoSQ0Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ0Tx.setStatus(_A)
_Gel2esw26kPortQoSQ1Rx_Type=Counter64
_Gel2esw26kPortQoSQ1Rx_Object=MibTableColumn
gel2esw26kPortQoSQ1Rx=_Gel2esw26kPortQoSQ1Rx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,4),_Gel2esw26kPortQoSQ1Rx_Type())
gel2esw26kPortQoSQ1Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ1Rx.setStatus(_A)
_Gel2esw26kPortQoSQ1Tx_Type=Counter64
_Gel2esw26kPortQoSQ1Tx_Object=MibTableColumn
gel2esw26kPortQoSQ1Tx=_Gel2esw26kPortQoSQ1Tx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,5),_Gel2esw26kPortQoSQ1Tx_Type())
gel2esw26kPortQoSQ1Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ1Tx.setStatus(_A)
_Gel2esw26kPortQoSQ2Rx_Type=Counter64
_Gel2esw26kPortQoSQ2Rx_Object=MibTableColumn
gel2esw26kPortQoSQ2Rx=_Gel2esw26kPortQoSQ2Rx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,6),_Gel2esw26kPortQoSQ2Rx_Type())
gel2esw26kPortQoSQ2Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ2Rx.setStatus(_A)
_Gel2esw26kPortQoSQ2Tx_Type=Counter64
_Gel2esw26kPortQoSQ2Tx_Object=MibTableColumn
gel2esw26kPortQoSQ2Tx=_Gel2esw26kPortQoSQ2Tx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,7),_Gel2esw26kPortQoSQ2Tx_Type())
gel2esw26kPortQoSQ2Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ2Tx.setStatus(_A)
_Gel2esw26kPortQoSQ3Rx_Type=Counter64
_Gel2esw26kPortQoSQ3Rx_Object=MibTableColumn
gel2esw26kPortQoSQ3Rx=_Gel2esw26kPortQoSQ3Rx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,8),_Gel2esw26kPortQoSQ3Rx_Type())
gel2esw26kPortQoSQ3Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ3Rx.setStatus(_A)
_Gel2esw26kPortQoSQ3Tx_Type=Counter64
_Gel2esw26kPortQoSQ3Tx_Object=MibTableColumn
gel2esw26kPortQoSQ3Tx=_Gel2esw26kPortQoSQ3Tx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,9),_Gel2esw26kPortQoSQ3Tx_Type())
gel2esw26kPortQoSQ3Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ3Tx.setStatus(_A)
_Gel2esw26kPortQoSQ4Rx_Type=Counter64
_Gel2esw26kPortQoSQ4Rx_Object=MibTableColumn
gel2esw26kPortQoSQ4Rx=_Gel2esw26kPortQoSQ4Rx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,10),_Gel2esw26kPortQoSQ4Rx_Type())
gel2esw26kPortQoSQ4Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ4Rx.setStatus(_A)
_Gel2esw26kPortQoSQ4Tx_Type=Counter64
_Gel2esw26kPortQoSQ4Tx_Object=MibTableColumn
gel2esw26kPortQoSQ4Tx=_Gel2esw26kPortQoSQ4Tx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,11),_Gel2esw26kPortQoSQ4Tx_Type())
gel2esw26kPortQoSQ4Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ4Tx.setStatus(_A)
_Gel2esw26kPortQoSQ5Rx_Type=Counter64
_Gel2esw26kPortQoSQ5Rx_Object=MibTableColumn
gel2esw26kPortQoSQ5Rx=_Gel2esw26kPortQoSQ5Rx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,12),_Gel2esw26kPortQoSQ5Rx_Type())
gel2esw26kPortQoSQ5Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ5Rx.setStatus(_A)
_Gel2esw26kPortQoSQ5Tx_Type=Counter64
_Gel2esw26kPortQoSQ5Tx_Object=MibTableColumn
gel2esw26kPortQoSQ5Tx=_Gel2esw26kPortQoSQ5Tx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,13),_Gel2esw26kPortQoSQ5Tx_Type())
gel2esw26kPortQoSQ5Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ5Tx.setStatus(_A)
_Gel2esw26kPortQoSQ6Rx_Type=Counter64
_Gel2esw26kPortQoSQ6Rx_Object=MibTableColumn
gel2esw26kPortQoSQ6Rx=_Gel2esw26kPortQoSQ6Rx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,14),_Gel2esw26kPortQoSQ6Rx_Type())
gel2esw26kPortQoSQ6Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ6Rx.setStatus(_A)
_Gel2esw26kPortQoSQ6Tx_Type=Counter64
_Gel2esw26kPortQoSQ6Tx_Object=MibTableColumn
gel2esw26kPortQoSQ6Tx=_Gel2esw26kPortQoSQ6Tx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,15),_Gel2esw26kPortQoSQ6Tx_Type())
gel2esw26kPortQoSQ6Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ6Tx.setStatus(_A)
_Gel2esw26kPortQoSQ7Rx_Type=Counter64
_Gel2esw26kPortQoSQ7Rx_Object=MibTableColumn
gel2esw26kPortQoSQ7Rx=_Gel2esw26kPortQoSQ7Rx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,16),_Gel2esw26kPortQoSQ7Rx_Type())
gel2esw26kPortQoSQ7Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ7Rx.setStatus(_A)
_Gel2esw26kPortQoSQ7Tx_Type=Counter64
_Gel2esw26kPortQoSQ7Tx_Object=MibTableColumn
gel2esw26kPortQoSQ7Tx=_Gel2esw26kPortQoSQ7Tx_Object((1,3,6,1,4,1,5205,2,54,2,1,3,2,1,17),_Gel2esw26kPortQoSQ7Tx_Type())
gel2esw26kPortQoSQ7Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortQoSQ7Tx.setStatus(_A)
_Gel2esw26kSFPInfoTable_Object=MibTable
gel2esw26kSFPInfoTable=_Gel2esw26kSFPInfoTable_Object((1,3,6,1,4,1,5205,2,54,2,1,4))
if mibBuilder.loadTexts:gel2esw26kSFPInfoTable.setStatus(_A)
_Gel2esw26kSFPInfoEntry_Object=MibTableRow
gel2esw26kSFPInfoEntry=_Gel2esw26kSFPInfoEntry_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1))
gel2esw26kSFPInfoEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:gel2esw26kSFPInfoEntry.setStatus(_A)
class _Gel2esw26kSFPInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kSFPInfoIndex_Type.__name__=_C
_Gel2esw26kSFPInfoIndex_Object=MibTableColumn
gel2esw26kSFPInfoIndex=_Gel2esw26kSFPInfoIndex_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,1),_Gel2esw26kSFPInfoIndex_Type())
gel2esw26kSFPInfoIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kSFPInfoIndex.setStatus(_A)
_Gel2esw26kSFPInfoPort_Type=DisplayString
_Gel2esw26kSFPInfoPort_Object=MibTableColumn
gel2esw26kSFPInfoPort=_Gel2esw26kSFPInfoPort_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,2),_Gel2esw26kSFPInfoPort_Type())
gel2esw26kSFPInfoPort.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPInfoPort.setStatus(_A)
_Gel2esw26kSFPConnectorType_Type=DisplayString
_Gel2esw26kSFPConnectorType_Object=MibTableColumn
gel2esw26kSFPConnectorType=_Gel2esw26kSFPConnectorType_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,3),_Gel2esw26kSFPConnectorType_Type())
gel2esw26kSFPConnectorType.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPConnectorType.setStatus(_A)
_Gel2esw26kSFPFiberType_Type=DisplayString
_Gel2esw26kSFPFiberType_Object=MibTableColumn
gel2esw26kSFPFiberType=_Gel2esw26kSFPFiberType_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,4),_Gel2esw26kSFPFiberType_Type())
gel2esw26kSFPFiberType.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPFiberType.setStatus(_A)
_Gel2esw26kSFPTxCentralWavelength_Type=DisplayString
_Gel2esw26kSFPTxCentralWavelength_Object=MibTableColumn
gel2esw26kSFPTxCentralWavelength=_Gel2esw26kSFPTxCentralWavelength_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,5),_Gel2esw26kSFPTxCentralWavelength_Type())
gel2esw26kSFPTxCentralWavelength.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPTxCentralWavelength.setStatus(_A)
_Gel2esw26kSFPBaudRate_Type=DisplayString
_Gel2esw26kSFPBaudRate_Object=MibTableColumn
gel2esw26kSFPBaudRate=_Gel2esw26kSFPBaudRate_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,6),_Gel2esw26kSFPBaudRate_Type())
gel2esw26kSFPBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPBaudRate.setStatus(_A)
_Gel2esw26kSFPVendorOUI_Type=DisplayString
_Gel2esw26kSFPVendorOUI_Object=MibTableColumn
gel2esw26kSFPVendorOUI=_Gel2esw26kSFPVendorOUI_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,7),_Gel2esw26kSFPVendorOUI_Type())
gel2esw26kSFPVendorOUI.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPVendorOUI.setStatus(_A)
_Gel2esw26kSFPVendorName_Type=DisplayString
_Gel2esw26kSFPVendorName_Object=MibTableColumn
gel2esw26kSFPVendorName=_Gel2esw26kSFPVendorName_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,8),_Gel2esw26kSFPVendorName_Type())
gel2esw26kSFPVendorName.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPVendorName.setStatus(_A)
_Gel2esw26kSFPVendorPN_Type=DisplayString
_Gel2esw26kSFPVendorPN_Object=MibTableColumn
gel2esw26kSFPVendorPN=_Gel2esw26kSFPVendorPN_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,9),_Gel2esw26kSFPVendorPN_Type())
gel2esw26kSFPVendorPN.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPVendorPN.setStatus(_A)
_Gel2esw26kSFPVendorRev_Type=DisplayString
_Gel2esw26kSFPVendorRev_Object=MibTableColumn
gel2esw26kSFPVendorRev=_Gel2esw26kSFPVendorRev_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,10),_Gel2esw26kSFPVendorRev_Type())
gel2esw26kSFPVendorRev.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPVendorRev.setStatus(_A)
_Gel2esw26kSFPVendorSN_Type=DisplayString
_Gel2esw26kSFPVendorSN_Object=MibTableColumn
gel2esw26kSFPVendorSN=_Gel2esw26kSFPVendorSN_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,11),_Gel2esw26kSFPVendorSN_Type())
gel2esw26kSFPVendorSN.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPVendorSN.setStatus(_A)
_Gel2esw26kSFPDateCode_Type=DisplayString
_Gel2esw26kSFPDateCode_Object=MibTableColumn
gel2esw26kSFPDateCode=_Gel2esw26kSFPDateCode_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,12),_Gel2esw26kSFPDateCode_Type())
gel2esw26kSFPDateCode.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPDateCode.setStatus(_A)
_Gel2esw26kSFPTemperature_Type=DisplayString
_Gel2esw26kSFPTemperature_Object=MibTableColumn
gel2esw26kSFPTemperature=_Gel2esw26kSFPTemperature_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,13),_Gel2esw26kSFPTemperature_Type())
gel2esw26kSFPTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPTemperature.setStatus(_A)
_Gel2esw26kSFPVcc_Type=DisplayString
_Gel2esw26kSFPVcc_Object=MibTableColumn
gel2esw26kSFPVcc=_Gel2esw26kSFPVcc_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,14),_Gel2esw26kSFPVcc_Type())
gel2esw26kSFPVcc.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPVcc.setStatus(_A)
_Gel2esw26kSFPMon1Bias_Type=DisplayString
_Gel2esw26kSFPMon1Bias_Object=MibTableColumn
gel2esw26kSFPMon1Bias=_Gel2esw26kSFPMon1Bias_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,15),_Gel2esw26kSFPMon1Bias_Type())
gel2esw26kSFPMon1Bias.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPMon1Bias.setStatus(_A)
_Gel2esw26kSFPMon2TxPWR_Type=DisplayString
_Gel2esw26kSFPMon2TxPWR_Object=MibTableColumn
gel2esw26kSFPMon2TxPWR=_Gel2esw26kSFPMon2TxPWR_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,16),_Gel2esw26kSFPMon2TxPWR_Type())
gel2esw26kSFPMon2TxPWR.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPMon2TxPWR.setStatus(_A)
_Gel2esw26kSFPMon3RxPWR_Type=DisplayString
_Gel2esw26kSFPMon3RxPWR_Object=MibTableColumn
gel2esw26kSFPMon3RxPWR=_Gel2esw26kSFPMon3RxPWR_Object((1,3,6,1,4,1,5205,2,54,2,1,4,1,17),_Gel2esw26kSFPMon3RxPWR_Type())
gel2esw26kSFPMon3RxPWR.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSFPMon3RxPWR.setStatus(_A)
_Gel2esw26kPortEEETable_Object=MibTable
gel2esw26kPortEEETable=_Gel2esw26kPortEEETable_Object((1,3,6,1,4,1,5205,2,54,2,1,5))
if mibBuilder.loadTexts:gel2esw26kPortEEETable.setStatus(_A)
_Gel2esw26kPortEEEEntry_Object=MibTableRow
gel2esw26kPortEEEEntry=_Gel2esw26kPortEEEEntry_Object((1,3,6,1,4,1,5205,2,54,2,1,5,1))
gel2esw26kPortEEEEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:gel2esw26kPortEEEEntry.setStatus(_A)
class _Gel2esw26kPortEEEPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kPortEEEPort_Type.__name__=_C
_Gel2esw26kPortEEEPort_Object=MibTableColumn
gel2esw26kPortEEEPort=_Gel2esw26kPortEEEPort_Object((1,3,6,1,4,1,5205,2,54,2,1,5,1,1),_Gel2esw26kPortEEEPort_Type())
gel2esw26kPortEEEPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kPortEEEPort.setStatus(_A)
class _Gel2esw26kPortEEEMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortEEEMode_Type.__name__=_C
_Gel2esw26kPortEEEMode_Object=MibTableColumn
gel2esw26kPortEEEMode=_Gel2esw26kPortEEEMode_Object((1,3,6,1,4,1,5205,2,54,2,1,5,1,2),_Gel2esw26kPortEEEMode_Type())
gel2esw26kPortEEEMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortEEEMode.setStatus(_A)
class _Gel2esw26kPortEEEUrgentQueue1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortEEEUrgentQueue1_Type.__name__=_C
_Gel2esw26kPortEEEUrgentQueue1_Object=MibTableColumn
gel2esw26kPortEEEUrgentQueue1=_Gel2esw26kPortEEEUrgentQueue1_Object((1,3,6,1,4,1,5205,2,54,2,1,5,1,3),_Gel2esw26kPortEEEUrgentQueue1_Type())
gel2esw26kPortEEEUrgentQueue1.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortEEEUrgentQueue1.setStatus(_A)
class _Gel2esw26kPortEEEUrgentQueue2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortEEEUrgentQueue2_Type.__name__=_C
_Gel2esw26kPortEEEUrgentQueue2_Object=MibTableColumn
gel2esw26kPortEEEUrgentQueue2=_Gel2esw26kPortEEEUrgentQueue2_Object((1,3,6,1,4,1,5205,2,54,2,1,5,1,4),_Gel2esw26kPortEEEUrgentQueue2_Type())
gel2esw26kPortEEEUrgentQueue2.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortEEEUrgentQueue2.setStatus(_A)
class _Gel2esw26kPortEEEUrgentQueue3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortEEEUrgentQueue3_Type.__name__=_C
_Gel2esw26kPortEEEUrgentQueue3_Object=MibTableColumn
gel2esw26kPortEEEUrgentQueue3=_Gel2esw26kPortEEEUrgentQueue3_Object((1,3,6,1,4,1,5205,2,54,2,1,5,1,5),_Gel2esw26kPortEEEUrgentQueue3_Type())
gel2esw26kPortEEEUrgentQueue3.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortEEEUrgentQueue3.setStatus(_A)
class _Gel2esw26kPortEEEUrgentQueue4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortEEEUrgentQueue4_Type.__name__=_C
_Gel2esw26kPortEEEUrgentQueue4_Object=MibTableColumn
gel2esw26kPortEEEUrgentQueue4=_Gel2esw26kPortEEEUrgentQueue4_Object((1,3,6,1,4,1,5205,2,54,2,1,5,1,6),_Gel2esw26kPortEEEUrgentQueue4_Type())
gel2esw26kPortEEEUrgentQueue4.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortEEEUrgentQueue4.setStatus(_A)
class _Gel2esw26kPortEEEUrgentQueue5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortEEEUrgentQueue5_Type.__name__=_C
_Gel2esw26kPortEEEUrgentQueue5_Object=MibTableColumn
gel2esw26kPortEEEUrgentQueue5=_Gel2esw26kPortEEEUrgentQueue5_Object((1,3,6,1,4,1,5205,2,54,2,1,5,1,7),_Gel2esw26kPortEEEUrgentQueue5_Type())
gel2esw26kPortEEEUrgentQueue5.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortEEEUrgentQueue5.setStatus(_A)
class _Gel2esw26kPortEEEUrgentQueue6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortEEEUrgentQueue6_Type.__name__=_C
_Gel2esw26kPortEEEUrgentQueue6_Object=MibTableColumn
gel2esw26kPortEEEUrgentQueue6=_Gel2esw26kPortEEEUrgentQueue6_Object((1,3,6,1,4,1,5205,2,54,2,1,5,1,8),_Gel2esw26kPortEEEUrgentQueue6_Type())
gel2esw26kPortEEEUrgentQueue6.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortEEEUrgentQueue6.setStatus(_A)
class _Gel2esw26kPortEEEUrgentQueue7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortEEEUrgentQueue7_Type.__name__=_C
_Gel2esw26kPortEEEUrgentQueue7_Object=MibTableColumn
gel2esw26kPortEEEUrgentQueue7=_Gel2esw26kPortEEEUrgentQueue7_Object((1,3,6,1,4,1,5205,2,54,2,1,5,1,9),_Gel2esw26kPortEEEUrgentQueue7_Type())
gel2esw26kPortEEEUrgentQueue7.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortEEEUrgentQueue7.setStatus(_A)
class _Gel2esw26kPortEEEUrgentQueue8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortEEEUrgentQueue8_Type.__name__=_C
_Gel2esw26kPortEEEUrgentQueue8_Object=MibTableColumn
gel2esw26kPortEEEUrgentQueue8=_Gel2esw26kPortEEEUrgentQueue8_Object((1,3,6,1,4,1,5205,2,54,2,1,5,1,10),_Gel2esw26kPortEEEUrgentQueue8_Type())
gel2esw26kPortEEEUrgentQueue8.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortEEEUrgentQueue8.setStatus(_A)
_Gel2esw26kVoiceVLAN_ObjectIdentity=ObjectIdentity
gel2esw26kVoiceVLAN=_Gel2esw26kVoiceVLAN_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2,2))
_Gel2esw26kVoiceVLANConf_ObjectIdentity=ObjectIdentity
gel2esw26kVoiceVLANConf=_Gel2esw26kVoiceVLANConf_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2,2,1))
class _Gel2esw26kVoiceVLANMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kVoiceVLANMode_Type.__name__=_C
_Gel2esw26kVoiceVLANMode_Object=MibScalar
gel2esw26kVoiceVLANMode=_Gel2esw26kVoiceVLANMode_Object((1,3,6,1,4,1,5205,2,54,2,2,1,1),_Gel2esw26kVoiceVLANMode_Type())
gel2esw26kVoiceVLANMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kVoiceVLANMode.setStatus(_A)
class _Gel2esw26kVoiceVLANVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw26kVoiceVLANVLANId_Type.__name__=_C
_Gel2esw26kVoiceVLANVLANId_Object=MibScalar
gel2esw26kVoiceVLANVLANId=_Gel2esw26kVoiceVLANVLANId_Object((1,3,6,1,4,1,5205,2,54,2,2,1,2),_Gel2esw26kVoiceVLANVLANId_Type())
gel2esw26kVoiceVLANVLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kVoiceVLANVLANId.setStatus(_A)
class _Gel2esw26kVoiceVLANAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_Gel2esw26kVoiceVLANAgingTime_Type.__name__=_C
_Gel2esw26kVoiceVLANAgingTime_Object=MibScalar
gel2esw26kVoiceVLANAgingTime=_Gel2esw26kVoiceVLANAgingTime_Object((1,3,6,1,4,1,5205,2,54,2,2,1,3),_Gel2esw26kVoiceVLANAgingTime_Type())
gel2esw26kVoiceVLANAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kVoiceVLANAgingTime.setStatus(_A)
class _Gel2esw26kVoiceVLANTrafficClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kVoiceVLANTrafficClass_Type.__name__=_C
_Gel2esw26kVoiceVLANTrafficClass_Object=MibScalar
gel2esw26kVoiceVLANTrafficClass=_Gel2esw26kVoiceVLANTrafficClass_Object((1,3,6,1,4,1,5205,2,54,2,2,1,4),_Gel2esw26kVoiceVLANTrafficClass_Type())
gel2esw26kVoiceVLANTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kVoiceVLANTrafficClass.setStatus(_A)
_Gel2esw26kVoiceVLANPortTable_Object=MibTable
gel2esw26kVoiceVLANPortTable=_Gel2esw26kVoiceVLANPortTable_Object((1,3,6,1,4,1,5205,2,54,2,2,1,5))
if mibBuilder.loadTexts:gel2esw26kVoiceVLANPortTable.setStatus(_A)
_Gel2esw26kVoiceVLANPortEntry_Object=MibTableRow
gel2esw26kVoiceVLANPortEntry=_Gel2esw26kVoiceVLANPortEntry_Object((1,3,6,1,4,1,5205,2,54,2,2,1,5,1))
gel2esw26kVoiceVLANPortEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:gel2esw26kVoiceVLANPortEntry.setStatus(_A)
class _Gel2esw26kVoiceVLANPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kVoiceVLANPort_Type.__name__=_C
_Gel2esw26kVoiceVLANPort_Object=MibTableColumn
gel2esw26kVoiceVLANPort=_Gel2esw26kVoiceVLANPort_Object((1,3,6,1,4,1,5205,2,54,2,2,1,5,1,1),_Gel2esw26kVoiceVLANPort_Type())
gel2esw26kVoiceVLANPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kVoiceVLANPort.setStatus(_A)
class _Gel2esw26kVoiceVLANPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kVoiceVLANPortMode_Type.__name__=_C
_Gel2esw26kVoiceVLANPortMode_Object=MibTableColumn
gel2esw26kVoiceVLANPortMode=_Gel2esw26kVoiceVLANPortMode_Object((1,3,6,1,4,1,5205,2,54,2,2,1,5,1,2),_Gel2esw26kVoiceVLANPortMode_Type())
gel2esw26kVoiceVLANPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kVoiceVLANPortMode.setStatus(_A)
class _Gel2esw26kVoiceVLANPortSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kVoiceVLANPortSecurity_Type.__name__=_C
_Gel2esw26kVoiceVLANPortSecurity_Object=MibTableColumn
gel2esw26kVoiceVLANPortSecurity=_Gel2esw26kVoiceVLANPortSecurity_Object((1,3,6,1,4,1,5205,2,54,2,2,1,5,1,3),_Gel2esw26kVoiceVLANPortSecurity_Type())
gel2esw26kVoiceVLANPortSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kVoiceVLANPortSecurity.setStatus(_A)
class _Gel2esw26kVoiceVLANPortDiscoveryProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kVoiceVLANPortDiscoveryProtocol_Type.__name__=_C
_Gel2esw26kVoiceVLANPortDiscoveryProtocol_Object=MibTableColumn
gel2esw26kVoiceVLANPortDiscoveryProtocol=_Gel2esw26kVoiceVLANPortDiscoveryProtocol_Object((1,3,6,1,4,1,5205,2,54,2,2,1,5,1,4),_Gel2esw26kVoiceVLANPortDiscoveryProtocol_Type())
gel2esw26kVoiceVLANPortDiscoveryProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kVoiceVLANPortDiscoveryProtocol.setStatus(_A)
_Gel2esw26kVoiceVLANOUI_ObjectIdentity=ObjectIdentity
gel2esw26kVoiceVLANOUI=_Gel2esw26kVoiceVLANOUI_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2,2,2))
class _Gel2esw26kVoiceVLANOUICreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kVoiceVLANOUICreate_Type.__name__=_C
_Gel2esw26kVoiceVLANOUICreate_Object=MibScalar
gel2esw26kVoiceVLANOUICreate=_Gel2esw26kVoiceVLANOUICreate_Object((1,3,6,1,4,1,5205,2,54,2,2,2,1),_Gel2esw26kVoiceVLANOUICreate_Type())
gel2esw26kVoiceVLANOUICreate.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kVoiceVLANOUICreate.setStatus(_A)
_Gel2esw26kVoiceVLANOUITable_Object=MibTable
gel2esw26kVoiceVLANOUITable=_Gel2esw26kVoiceVLANOUITable_Object((1,3,6,1,4,1,5205,2,54,2,2,2,2))
if mibBuilder.loadTexts:gel2esw26kVoiceVLANOUITable.setStatus(_A)
_Gel2esw26kVoiceVLANOUIEntry_Object=MibTableRow
gel2esw26kVoiceVLANOUIEntry=_Gel2esw26kVoiceVLANOUIEntry_Object((1,3,6,1,4,1,5205,2,54,2,2,2,2,1))
gel2esw26kVoiceVLANOUIEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:gel2esw26kVoiceVLANOUIEntry.setStatus(_A)
class _Gel2esw26kVoiceVLANOUIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Gel2esw26kVoiceVLANOUIIndex_Type.__name__=_C
_Gel2esw26kVoiceVLANOUIIndex_Object=MibTableColumn
gel2esw26kVoiceVLANOUIIndex=_Gel2esw26kVoiceVLANOUIIndex_Object((1,3,6,1,4,1,5205,2,54,2,2,2,2,1,1),_Gel2esw26kVoiceVLANOUIIndex_Type())
gel2esw26kVoiceVLANOUIIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kVoiceVLANOUIIndex.setStatus(_A)
class _Gel2esw26kVoiceVLANTelephonyOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Gel2esw26kVoiceVLANTelephonyOUI_Type.__name__=_I
_Gel2esw26kVoiceVLANTelephonyOUI_Object=MibTableColumn
gel2esw26kVoiceVLANTelephonyOUI=_Gel2esw26kVoiceVLANTelephonyOUI_Object((1,3,6,1,4,1,5205,2,54,2,2,2,2,1,2),_Gel2esw26kVoiceVLANTelephonyOUI_Type())
gel2esw26kVoiceVLANTelephonyOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kVoiceVLANTelephonyOUI.setStatus(_A)
class _Gel2esw26kVoiceVLANDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Gel2esw26kVoiceVLANDescription_Type.__name__=_G
_Gel2esw26kVoiceVLANDescription_Object=MibTableColumn
gel2esw26kVoiceVLANDescription=_Gel2esw26kVoiceVLANDescription_Object((1,3,6,1,4,1,5205,2,54,2,2,2,2,1,3),_Gel2esw26kVoiceVLANDescription_Type())
gel2esw26kVoiceVLANDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kVoiceVLANDescription.setStatus(_A)
class _Gel2esw26kVoiceVLANOUIRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw26kVoiceVLANOUIRowStatus_Type.__name__=_C
_Gel2esw26kVoiceVLANOUIRowStatus_Object=MibTableColumn
gel2esw26kVoiceVLANOUIRowStatus=_Gel2esw26kVoiceVLANOUIRowStatus_Object((1,3,6,1,4,1,5205,2,54,2,2,2,2,1,4),_Gel2esw26kVoiceVLANOUIRowStatus_Type())
gel2esw26kVoiceVLANOUIRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kVoiceVLANOUIRowStatus.setStatus(_A)
_Gel2esw26kGARP_ObjectIdentity=ObjectIdentity
gel2esw26kGARP=_Gel2esw26kGARP_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2,3))
_Gel2esw26kGARPConfTable_Object=MibTable
gel2esw26kGARPConfTable=_Gel2esw26kGARPConfTable_Object((1,3,6,1,4,1,5205,2,54,2,3,1))
if mibBuilder.loadTexts:gel2esw26kGARPConfTable.setStatus(_A)
_Gel2esw26kGARPConfEntry_Object=MibTableRow
gel2esw26kGARPConfEntry=_Gel2esw26kGARPConfEntry_Object((1,3,6,1,4,1,5205,2,54,2,3,1,1))
gel2esw26kGARPConfEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:gel2esw26kGARPConfEntry.setStatus(_A)
class _Gel2esw26kGARPConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kGARPConfPort_Type.__name__=_C
_Gel2esw26kGARPConfPort_Object=MibTableColumn
gel2esw26kGARPConfPort=_Gel2esw26kGARPConfPort_Object((1,3,6,1,4,1,5205,2,54,2,3,1,1,1),_Gel2esw26kGARPConfPort_Type())
gel2esw26kGARPConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kGARPConfPort.setStatus(_A)
class _Gel2esw26kGARPJoinTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,1000))
_Gel2esw26kGARPJoinTimer_Type.__name__=_C
_Gel2esw26kGARPJoinTimer_Object=MibTableColumn
gel2esw26kGARPJoinTimer=_Gel2esw26kGARPJoinTimer_Object((1,3,6,1,4,1,5205,2,54,2,3,1,1,2),_Gel2esw26kGARPJoinTimer_Type())
gel2esw26kGARPJoinTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kGARPJoinTimer.setStatus(_A)
class _Gel2esw26kGARPLeaveTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,3000))
_Gel2esw26kGARPLeaveTimer_Type.__name__=_C
_Gel2esw26kGARPLeaveTimer_Object=MibTableColumn
gel2esw26kGARPLeaveTimer=_Gel2esw26kGARPLeaveTimer_Object((1,3,6,1,4,1,5205,2,54,2,3,1,1,3),_Gel2esw26kGARPLeaveTimer_Type())
gel2esw26kGARPLeaveTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kGARPLeaveTimer.setStatus(_A)
class _Gel2esw26kGARPLeaveAllTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10000,50000))
_Gel2esw26kGARPLeaveAllTimer_Type.__name__=_C
_Gel2esw26kGARPLeaveAllTimer_Object=MibTableColumn
gel2esw26kGARPLeaveAllTimer=_Gel2esw26kGARPLeaveAllTimer_Object((1,3,6,1,4,1,5205,2,54,2,3,1,1,4),_Gel2esw26kGARPLeaveAllTimer_Type())
gel2esw26kGARPLeaveAllTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kGARPLeaveAllTimer.setStatus(_A)
class _Gel2esw26kGARPApplicantion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Gel2esw26kGARPApplicantion_Type.__name__=_C
_Gel2esw26kGARPApplicantion_Object=MibTableColumn
gel2esw26kGARPApplicantion=_Gel2esw26kGARPApplicantion_Object((1,3,6,1,4,1,5205,2,54,2,3,1,1,5),_Gel2esw26kGARPApplicantion_Type())
gel2esw26kGARPApplicantion.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kGARPApplicantion.setStatus(_A)
class _Gel2esw26kGARPAttributeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Gel2esw26kGARPAttributeType_Type.__name__=_C
_Gel2esw26kGARPAttributeType_Object=MibTableColumn
gel2esw26kGARPAttributeType=_Gel2esw26kGARPAttributeType_Object((1,3,6,1,4,1,5205,2,54,2,3,1,1,6),_Gel2esw26kGARPAttributeType_Type())
gel2esw26kGARPAttributeType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kGARPAttributeType.setStatus(_A)
class _Gel2esw26kGARPApplicant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kGARPApplicant_Type.__name__=_C
_Gel2esw26kGARPApplicant_Object=MibTableColumn
gel2esw26kGARPApplicant=_Gel2esw26kGARPApplicant_Object((1,3,6,1,4,1,5205,2,54,2,3,1,1,7),_Gel2esw26kGARPApplicant_Type())
gel2esw26kGARPApplicant.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kGARPApplicant.setStatus(_A)
_Gel2esw26kGARPStatisticsTable_Object=MibTable
gel2esw26kGARPStatisticsTable=_Gel2esw26kGARPStatisticsTable_Object((1,3,6,1,4,1,5205,2,54,2,3,2))
if mibBuilder.loadTexts:gel2esw26kGARPStatisticsTable.setStatus(_A)
_Gel2esw26kGARPStatisticsEntry_Object=MibTableRow
gel2esw26kGARPStatisticsEntry=_Gel2esw26kGARPStatisticsEntry_Object((1,3,6,1,4,1,5205,2,54,2,3,2,1))
gel2esw26kGARPStatisticsEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:gel2esw26kGARPStatisticsEntry.setStatus(_A)
class _Gel2esw26kGARPStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kGARPStatisticsPort_Type.__name__=_C
_Gel2esw26kGARPStatisticsPort_Object=MibTableColumn
gel2esw26kGARPStatisticsPort=_Gel2esw26kGARPStatisticsPort_Object((1,3,6,1,4,1,5205,2,54,2,3,2,1,1),_Gel2esw26kGARPStatisticsPort_Type())
gel2esw26kGARPStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kGARPStatisticsPort.setStatus(_A)
_Gel2esw26kGARPStatisticsPeerMAC_Type=DisplayString
_Gel2esw26kGARPStatisticsPeerMAC_Object=MibTableColumn
gel2esw26kGARPStatisticsPeerMAC=_Gel2esw26kGARPStatisticsPeerMAC_Object((1,3,6,1,4,1,5205,2,54,2,3,2,1,2),_Gel2esw26kGARPStatisticsPeerMAC_Type())
gel2esw26kGARPStatisticsPeerMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kGARPStatisticsPeerMAC.setStatus(_A)
_Gel2esw26kGARPStatisticsFailedCount_Type=Counter32
_Gel2esw26kGARPStatisticsFailedCount_Object=MibTableColumn
gel2esw26kGARPStatisticsFailedCount=_Gel2esw26kGARPStatisticsFailedCount_Object((1,3,6,1,4,1,5205,2,54,2,3,2,1,3),_Gel2esw26kGARPStatisticsFailedCount_Type())
gel2esw26kGARPStatisticsFailedCount.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kGARPStatisticsFailedCount.setStatus(_A)
_Gel2esw26kGVRP_ObjectIdentity=ObjectIdentity
gel2esw26kGVRP=_Gel2esw26kGVRP_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2,4))
_Gel2esw26kGVRPConf_ObjectIdentity=ObjectIdentity
gel2esw26kGVRPConf=_Gel2esw26kGVRPConf_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2,4,1))
class _Gel2esw26kGVRPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kGVRPMode_Type.__name__=_C
_Gel2esw26kGVRPMode_Object=MibScalar
gel2esw26kGVRPMode=_Gel2esw26kGVRPMode_Object((1,3,6,1,4,1,5205,2,54,2,4,1,1),_Gel2esw26kGVRPMode_Type())
gel2esw26kGVRPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kGVRPMode.setStatus(_A)
_Gel2esw26kGVRPConfTable_Object=MibTable
gel2esw26kGVRPConfTable=_Gel2esw26kGVRPConfTable_Object((1,3,6,1,4,1,5205,2,54,2,4,1,2))
if mibBuilder.loadTexts:gel2esw26kGVRPConfTable.setStatus(_A)
_Gel2esw26kGVRPConfEntry_Object=MibTableRow
gel2esw26kGVRPConfEntry=_Gel2esw26kGVRPConfEntry_Object((1,3,6,1,4,1,5205,2,54,2,4,1,2,1))
gel2esw26kGVRPConfEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:gel2esw26kGVRPConfEntry.setStatus(_A)
class _Gel2esw26kGVRPConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kGVRPConfPort_Type.__name__=_C
_Gel2esw26kGVRPConfPort_Object=MibTableColumn
gel2esw26kGVRPConfPort=_Gel2esw26kGVRPConfPort_Object((1,3,6,1,4,1,5205,2,54,2,4,1,2,1,1),_Gel2esw26kGVRPConfPort_Type())
gel2esw26kGVRPConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kGVRPConfPort.setStatus(_A)
class _Gel2esw26kGVRPConfPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kGVRPConfPortMode_Type.__name__=_C
_Gel2esw26kGVRPConfPortMode_Object=MibTableColumn
gel2esw26kGVRPConfPortMode=_Gel2esw26kGVRPConfPortMode_Object((1,3,6,1,4,1,5205,2,54,2,4,1,2,1,2),_Gel2esw26kGVRPConfPortMode_Type())
gel2esw26kGVRPConfPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kGVRPConfPortMode.setStatus(_A)
class _Gel2esw26kGVRPConfPortRRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kGVRPConfPortRRole_Type.__name__=_C
_Gel2esw26kGVRPConfPortRRole_Object=MibTableColumn
gel2esw26kGVRPConfPortRRole=_Gel2esw26kGVRPConfPortRRole_Object((1,3,6,1,4,1,5205,2,54,2,4,1,2,1,3),_Gel2esw26kGVRPConfPortRRole_Type())
gel2esw26kGVRPConfPortRRole.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kGVRPConfPortRRole.setStatus(_A)
_Gel2esw26kGVRPStatisticsTable_Object=MibTable
gel2esw26kGVRPStatisticsTable=_Gel2esw26kGVRPStatisticsTable_Object((1,3,6,1,4,1,5205,2,54,2,4,2))
if mibBuilder.loadTexts:gel2esw26kGVRPStatisticsTable.setStatus(_A)
_Gel2esw26kGVRPStatisticsEntry_Object=MibTableRow
gel2esw26kGVRPStatisticsEntry=_Gel2esw26kGVRPStatisticsEntry_Object((1,3,6,1,4,1,5205,2,54,2,4,2,1))
gel2esw26kGVRPStatisticsEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:gel2esw26kGVRPStatisticsEntry.setStatus(_A)
class _Gel2esw26kGVRPStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kGVRPStatisticsPort_Type.__name__=_C
_Gel2esw26kGVRPStatisticsPort_Object=MibTableColumn
gel2esw26kGVRPStatisticsPort=_Gel2esw26kGVRPStatisticsPort_Object((1,3,6,1,4,1,5205,2,54,2,4,2,1,1),_Gel2esw26kGVRPStatisticsPort_Type())
gel2esw26kGVRPStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kGVRPStatisticsPort.setStatus(_A)
_Gel2esw26kGVRPStatisticsJoinTxCnt_Type=Counter32
_Gel2esw26kGVRPStatisticsJoinTxCnt_Object=MibTableColumn
gel2esw26kGVRPStatisticsJoinTxCnt=_Gel2esw26kGVRPStatisticsJoinTxCnt_Object((1,3,6,1,4,1,5205,2,54,2,4,2,1,2),_Gel2esw26kGVRPStatisticsJoinTxCnt_Type())
gel2esw26kGVRPStatisticsJoinTxCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kGVRPStatisticsJoinTxCnt.setStatus(_A)
_Gel2esw26kGVRPStatisticsLeaveTxCnt_Type=Counter32
_Gel2esw26kGVRPStatisticsLeaveTxCnt_Object=MibTableColumn
gel2esw26kGVRPStatisticsLeaveTxCnt=_Gel2esw26kGVRPStatisticsLeaveTxCnt_Object((1,3,6,1,4,1,5205,2,54,2,4,2,1,3),_Gel2esw26kGVRPStatisticsLeaveTxCnt_Type())
gel2esw26kGVRPStatisticsLeaveTxCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kGVRPStatisticsLeaveTxCnt.setStatus(_A)
_Gel2esw26kMirroring_ObjectIdentity=ObjectIdentity
gel2esw26kMirroring=_Gel2esw26kMirroring_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2,6))
class _Gel2esw26kPortToMirrorOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Gel2esw26kPortToMirrorOn_Type.__name__=_C
_Gel2esw26kPortToMirrorOn_Object=MibScalar
gel2esw26kPortToMirrorOn=_Gel2esw26kPortToMirrorOn_Object((1,3,6,1,4,1,5205,2,54,2,6,1),_Gel2esw26kPortToMirrorOn_Type())
gel2esw26kPortToMirrorOn.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortToMirrorOn.setStatus(_A)
_Gel2esw26kMirrorTable_Object=MibTable
gel2esw26kMirrorTable=_Gel2esw26kMirrorTable_Object((1,3,6,1,4,1,5205,2,54,2,6,2))
if mibBuilder.loadTexts:gel2esw26kMirrorTable.setStatus(_A)
_Gel2esw26kMirrorEntry_Object=MibTableRow
gel2esw26kMirrorEntry=_Gel2esw26kMirrorEntry_Object((1,3,6,1,4,1,5205,2,54,2,6,2,1))
gel2esw26kMirrorEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:gel2esw26kMirrorEntry.setStatus(_A)
class _Gel2esw26kMirrorPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kMirrorPort_Type.__name__=_C
_Gel2esw26kMirrorPort_Object=MibTableColumn
gel2esw26kMirrorPort=_Gel2esw26kMirrorPort_Object((1,3,6,1,4,1,5205,2,54,2,6,2,1,1),_Gel2esw26kMirrorPort_Type())
gel2esw26kMirrorPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kMirrorPort.setStatus(_A)
class _Gel2esw26kMirrorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw26kMirrorMode_Type.__name__=_C
_Gel2esw26kMirrorMode_Object=MibTableColumn
gel2esw26kMirrorMode=_Gel2esw26kMirrorMode_Object((1,3,6,1,4,1,5205,2,54,2,6,2,1,2),_Gel2esw26kMirrorMode_Type())
gel2esw26kMirrorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kMirrorMode.setStatus(_A)
_Gel2esw26kTrapEventSeverity_ObjectIdentity=ObjectIdentity
gel2esw26kTrapEventSeverity=_Gel2esw26kTrapEventSeverity_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2,7))
class _Gel2esw26kTrapEventSeverityACL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityACL_Type.__name__=_C
_Gel2esw26kTrapEventSeverityACL_Object=MibScalar
gel2esw26kTrapEventSeverityACL=_Gel2esw26kTrapEventSeverityACL_Object((1,3,6,1,4,1,5205,2,54,2,7,1),_Gel2esw26kTrapEventSeverityACL_Type())
gel2esw26kTrapEventSeverityACL.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityACL.setStatus(_A)
class _Gel2esw26kTrapEventSeverityACLLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityACLLog_Type.__name__=_C
_Gel2esw26kTrapEventSeverityACLLog_Object=MibScalar
gel2esw26kTrapEventSeverityACLLog=_Gel2esw26kTrapEventSeverityACLLog_Object((1,3,6,1,4,1,5205,2,54,2,7,2),_Gel2esw26kTrapEventSeverityACLLog_Type())
gel2esw26kTrapEventSeverityACLLog.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityACLLog.setStatus(_A)
class _Gel2esw26kTrapEventSeverityAccessMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityAccessMgmt_Type.__name__=_C
_Gel2esw26kTrapEventSeverityAccessMgmt_Object=MibScalar
gel2esw26kTrapEventSeverityAccessMgmt=_Gel2esw26kTrapEventSeverityAccessMgmt_Object((1,3,6,1,4,1,5205,2,54,2,7,3),_Gel2esw26kTrapEventSeverityAccessMgmt_Type())
gel2esw26kTrapEventSeverityAccessMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityAccessMgmt.setStatus(_A)
class _Gel2esw26kTrapEventSeverityAuthFailed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityAuthFailed_Type.__name__=_C
_Gel2esw26kTrapEventSeverityAuthFailed_Object=MibScalar
gel2esw26kTrapEventSeverityAuthFailed=_Gel2esw26kTrapEventSeverityAuthFailed_Object((1,3,6,1,4,1,5205,2,54,2,7,4),_Gel2esw26kTrapEventSeverityAuthFailed_Type())
gel2esw26kTrapEventSeverityAuthFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityAuthFailed.setStatus(_A)
class _Gel2esw26kTrapEventSeverityColdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityColdStart_Type.__name__=_C
_Gel2esw26kTrapEventSeverityColdStart_Object=MibScalar
gel2esw26kTrapEventSeverityColdStart=_Gel2esw26kTrapEventSeverityColdStart_Object((1,3,6,1,4,1,5205,2,54,2,7,5),_Gel2esw26kTrapEventSeverityColdStart_Type())
gel2esw26kTrapEventSeverityColdStart.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityColdStart.setStatus(_A)
class _Gel2esw26kTrapEventSeverityConfigInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityConfigInfo_Type.__name__=_C
_Gel2esw26kTrapEventSeverityConfigInfo_Object=MibScalar
gel2esw26kTrapEventSeverityConfigInfo=_Gel2esw26kTrapEventSeverityConfigInfo_Object((1,3,6,1,4,1,5205,2,54,2,7,6),_Gel2esw26kTrapEventSeverityConfigInfo_Type())
gel2esw26kTrapEventSeverityConfigInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityConfigInfo.setStatus(_A)
class _Gel2esw26kTrapEventSeverityFirmwareUpgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityFirmwareUpgrade_Type.__name__=_C
_Gel2esw26kTrapEventSeverityFirmwareUpgrade_Object=MibScalar
gel2esw26kTrapEventSeverityFirmwareUpgrade=_Gel2esw26kTrapEventSeverityFirmwareUpgrade_Object((1,3,6,1,4,1,5205,2,54,2,7,7),_Gel2esw26kTrapEventSeverityFirmwareUpgrade_Type())
gel2esw26kTrapEventSeverityFirmwareUpgrade.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityFirmwareUpgrade.setStatus(_A)
class _Gel2esw26kTrapEventSeverityImportExport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityImportExport_Type.__name__=_C
_Gel2esw26kTrapEventSeverityImportExport_Object=MibScalar
gel2esw26kTrapEventSeverityImportExport=_Gel2esw26kTrapEventSeverityImportExport_Object((1,3,6,1,4,1,5205,2,54,2,7,8),_Gel2esw26kTrapEventSeverityImportExport_Type())
gel2esw26kTrapEventSeverityImportExport.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityImportExport.setStatus(_A)
class _Gel2esw26kTrapEventSeverityLACP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityLACP_Type.__name__=_C
_Gel2esw26kTrapEventSeverityLACP_Object=MibScalar
gel2esw26kTrapEventSeverityLACP=_Gel2esw26kTrapEventSeverityLACP_Object((1,3,6,1,4,1,5205,2,54,2,7,9),_Gel2esw26kTrapEventSeverityLACP_Type())
gel2esw26kTrapEventSeverityLACP.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityLACP.setStatus(_A)
class _Gel2esw26kTrapEventSeverityLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityLinkStatus_Type.__name__=_C
_Gel2esw26kTrapEventSeverityLinkStatus_Object=MibScalar
gel2esw26kTrapEventSeverityLinkStatus=_Gel2esw26kTrapEventSeverityLinkStatus_Object((1,3,6,1,4,1,5205,2,54,2,7,10),_Gel2esw26kTrapEventSeverityLinkStatus_Type())
gel2esw26kTrapEventSeverityLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityLinkStatus.setStatus(_A)
class _Gel2esw26kTrapEventSeverityLogin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityLogin_Type.__name__=_C
_Gel2esw26kTrapEventSeverityLogin_Object=MibScalar
gel2esw26kTrapEventSeverityLogin=_Gel2esw26kTrapEventSeverityLogin_Object((1,3,6,1,4,1,5205,2,54,2,7,11),_Gel2esw26kTrapEventSeverityLogin_Type())
gel2esw26kTrapEventSeverityLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityLogin.setStatus(_A)
class _Gel2esw26kTrapEventSeverityLogout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityLogout_Type.__name__=_C
_Gel2esw26kTrapEventSeverityLogout_Object=MibScalar
gel2esw26kTrapEventSeverityLogout=_Gel2esw26kTrapEventSeverityLogout_Object((1,3,6,1,4,1,5205,2,54,2,7,12),_Gel2esw26kTrapEventSeverityLogout_Type())
gel2esw26kTrapEventSeverityLogout.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityLogout.setStatus(_A)
class _Gel2esw26kTrapEventSeverityLoopProtect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityLoopProtect_Type.__name__=_C
_Gel2esw26kTrapEventSeverityLoopProtect_Object=MibScalar
gel2esw26kTrapEventSeverityLoopProtect=_Gel2esw26kTrapEventSeverityLoopProtect_Object((1,3,6,1,4,1,5205,2,54,2,7,13),_Gel2esw26kTrapEventSeverityLoopProtect_Type())
gel2esw26kTrapEventSeverityLoopProtect.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityLoopProtect.setStatus(_A)
class _Gel2esw26kTrapEventSeverityMgmtIPChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityMgmtIPChange_Type.__name__=_C
_Gel2esw26kTrapEventSeverityMgmtIPChange_Object=MibScalar
gel2esw26kTrapEventSeverityMgmtIPChange=_Gel2esw26kTrapEventSeverityMgmtIPChange_Object((1,3,6,1,4,1,5205,2,54,2,7,14),_Gel2esw26kTrapEventSeverityMgmtIPChange_Type())
gel2esw26kTrapEventSeverityMgmtIPChange.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityMgmtIPChange.setStatus(_A)
class _Gel2esw26kTrapEventSeverityModuleChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityModuleChange_Type.__name__=_C
_Gel2esw26kTrapEventSeverityModuleChange_Object=MibScalar
gel2esw26kTrapEventSeverityModuleChange=_Gel2esw26kTrapEventSeverityModuleChange_Object((1,3,6,1,4,1,5205,2,54,2,7,15),_Gel2esw26kTrapEventSeverityModuleChange_Type())
gel2esw26kTrapEventSeverityModuleChange.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityModuleChange.setStatus(_A)
class _Gel2esw26kTrapEventSeverityNAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityNAS_Type.__name__=_C
_Gel2esw26kTrapEventSeverityNAS_Object=MibScalar
gel2esw26kTrapEventSeverityNAS=_Gel2esw26kTrapEventSeverityNAS_Object((1,3,6,1,4,1,5205,2,54,2,7,16),_Gel2esw26kTrapEventSeverityNAS_Type())
gel2esw26kTrapEventSeverityNAS.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityNAS.setStatus(_A)
class _Gel2esw26kTrapEventSeverityPasswordChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityPasswordChange_Type.__name__=_C
_Gel2esw26kTrapEventSeverityPasswordChange_Object=MibScalar
gel2esw26kTrapEventSeverityPasswordChange=_Gel2esw26kTrapEventSeverityPasswordChange_Object((1,3,6,1,4,1,5205,2,54,2,7,17),_Gel2esw26kTrapEventSeverityPasswordChange_Type())
gel2esw26kTrapEventSeverityPasswordChange.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityPasswordChange.setStatus(_A)
class _Gel2esw26kTrapEventSeverityPortSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityPortSecurity_Type.__name__=_C
_Gel2esw26kTrapEventSeverityPortSecurity_Object=MibScalar
gel2esw26kTrapEventSeverityPortSecurity=_Gel2esw26kTrapEventSeverityPortSecurity_Object((1,3,6,1,4,1,5205,2,54,2,7,18),_Gel2esw26kTrapEventSeverityPortSecurity_Type())
gel2esw26kTrapEventSeverityPortSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityPortSecurity.setStatus(_A)
class _Gel2esw26kTrapEventSeverityThermalProtect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityThermalProtect_Type.__name__=_C
_Gel2esw26kTrapEventSeverityThermalProtect_Object=MibScalar
gel2esw26kTrapEventSeverityThermalProtect=_Gel2esw26kTrapEventSeverityThermalProtect_Object((1,3,6,1,4,1,5205,2,54,2,7,19),_Gel2esw26kTrapEventSeverityThermalProtect_Type())
gel2esw26kTrapEventSeverityThermalProtect.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityThermalProtect.setStatus(_A)
class _Gel2esw26kTrapEventSeverityVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityVLAN_Type.__name__=_C
_Gel2esw26kTrapEventSeverityVLAN_Object=MibScalar
gel2esw26kTrapEventSeverityVLAN=_Gel2esw26kTrapEventSeverityVLAN_Object((1,3,6,1,4,1,5205,2,54,2,7,20),_Gel2esw26kTrapEventSeverityVLAN_Type())
gel2esw26kTrapEventSeverityVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityVLAN.setStatus(_A)
class _Gel2esw26kTrapEventSeverityWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kTrapEventSeverityWarmStart_Type.__name__=_C
_Gel2esw26kTrapEventSeverityWarmStart_Object=MibScalar
gel2esw26kTrapEventSeverityWarmStart=_Gel2esw26kTrapEventSeverityWarmStart_Object((1,3,6,1,4,1,5205,2,54,2,7,21),_Gel2esw26kTrapEventSeverityWarmStart_Type())
gel2esw26kTrapEventSeverityWarmStart.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTrapEventSeverityWarmStart.setStatus(_A)
_Gel2esw26kSMTP_ObjectIdentity=ObjectIdentity
gel2esw26kSMTP=_Gel2esw26kSMTP_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2,8))
_Gel2esw26kSMTPMailServer_Type=DisplayString
_Gel2esw26kSMTPMailServer_Object=MibScalar
gel2esw26kSMTPMailServer=_Gel2esw26kSMTPMailServer_Object((1,3,6,1,4,1,5205,2,54,2,8,1),_Gel2esw26kSMTPMailServer_Type())
gel2esw26kSMTPMailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSMTPMailServer.setStatus(_A)
_Gel2esw26kSMTPUserName_Type=DisplayString
_Gel2esw26kSMTPUserName_Object=MibScalar
gel2esw26kSMTPUserName=_Gel2esw26kSMTPUserName_Object((1,3,6,1,4,1,5205,2,54,2,8,2),_Gel2esw26kSMTPUserName_Type())
gel2esw26kSMTPUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSMTPUserName.setStatus(_A)
_Gel2esw26kSMTPPassword_Type=DisplayString
_Gel2esw26kSMTPPassword_Object=MibScalar
gel2esw26kSMTPPassword=_Gel2esw26kSMTPPassword_Object((1,3,6,1,4,1,5205,2,54,2,8,3),_Gel2esw26kSMTPPassword_Type())
gel2esw26kSMTPPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSMTPPassword.setStatus(_A)
class _Gel2esw26kSMTPServeriryLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Gel2esw26kSMTPServeriryLevel_Type.__name__=_C
_Gel2esw26kSMTPServeriryLevel_Object=MibScalar
gel2esw26kSMTPServeriryLevel=_Gel2esw26kSMTPServeriryLevel_Object((1,3,6,1,4,1,5205,2,54,2,8,4),_Gel2esw26kSMTPServeriryLevel_Type())
gel2esw26kSMTPServeriryLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSMTPServeriryLevel.setStatus(_A)
_Gel2esw26kSMTPSender_Type=DisplayString
_Gel2esw26kSMTPSender_Object=MibScalar
gel2esw26kSMTPSender=_Gel2esw26kSMTPSender_Object((1,3,6,1,4,1,5205,2,54,2,8,5),_Gel2esw26kSMTPSender_Type())
gel2esw26kSMTPSender.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSMTPSender.setStatus(_A)
_Gel2esw26kSMTPReturnPath_Type=DisplayString
_Gel2esw26kSMTPReturnPath_Object=MibScalar
gel2esw26kSMTPReturnPath=_Gel2esw26kSMTPReturnPath_Object((1,3,6,1,4,1,5205,2,54,2,8,6),_Gel2esw26kSMTPReturnPath_Type())
gel2esw26kSMTPReturnPath.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSMTPReturnPath.setStatus(_A)
_Gel2esw26kSMTPEmailAddress1_Type=DisplayString
_Gel2esw26kSMTPEmailAddress1_Object=MibScalar
gel2esw26kSMTPEmailAddress1=_Gel2esw26kSMTPEmailAddress1_Object((1,3,6,1,4,1,5205,2,54,2,8,7),_Gel2esw26kSMTPEmailAddress1_Type())
gel2esw26kSMTPEmailAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSMTPEmailAddress1.setStatus(_A)
_Gel2esw26kSMTPEmailAddress2_Type=DisplayString
_Gel2esw26kSMTPEmailAddress2_Object=MibScalar
gel2esw26kSMTPEmailAddress2=_Gel2esw26kSMTPEmailAddress2_Object((1,3,6,1,4,1,5205,2,54,2,8,8),_Gel2esw26kSMTPEmailAddress2_Type())
gel2esw26kSMTPEmailAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSMTPEmailAddress2.setStatus(_A)
_Gel2esw26kSMTPEmailAddress3_Type=DisplayString
_Gel2esw26kSMTPEmailAddress3_Object=MibScalar
gel2esw26kSMTPEmailAddress3=_Gel2esw26kSMTPEmailAddress3_Object((1,3,6,1,4,1,5205,2,54,2,8,9),_Gel2esw26kSMTPEmailAddress3_Type())
gel2esw26kSMTPEmailAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSMTPEmailAddress3.setStatus(_A)
_Gel2esw26kSMTPEmailAddress4_Type=DisplayString
_Gel2esw26kSMTPEmailAddress4_Object=MibScalar
gel2esw26kSMTPEmailAddress4=_Gel2esw26kSMTPEmailAddress4_Object((1,3,6,1,4,1,5205,2,54,2,8,10),_Gel2esw26kSMTPEmailAddress4_Type())
gel2esw26kSMTPEmailAddress4.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSMTPEmailAddress4.setStatus(_A)
_Gel2esw26kSMTPEmailAddress5_Type=DisplayString
_Gel2esw26kSMTPEmailAddress5_Object=MibScalar
gel2esw26kSMTPEmailAddress5=_Gel2esw26kSMTPEmailAddress5_Object((1,3,6,1,4,1,5205,2,54,2,8,11),_Gel2esw26kSMTPEmailAddress5_Type())
gel2esw26kSMTPEmailAddress5.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSMTPEmailAddress5.setStatus(_A)
_Gel2esw26kSMTPEmailAddress6_Type=DisplayString
_Gel2esw26kSMTPEmailAddress6_Object=MibScalar
gel2esw26kSMTPEmailAddress6=_Gel2esw26kSMTPEmailAddress6_Object((1,3,6,1,4,1,5205,2,54,2,8,12),_Gel2esw26kSMTPEmailAddress6_Type())
gel2esw26kSMTPEmailAddress6.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSMTPEmailAddress6.setStatus(_A)
_Gel2esw26kACL_ObjectIdentity=ObjectIdentity
gel2esw26kACL=_Gel2esw26kACL_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2,9))
_Gel2esw26kACLPortsConfTable_Object=MibTable
gel2esw26kACLPortsConfTable=_Gel2esw26kACLPortsConfTable_Object((1,3,6,1,4,1,5205,2,54,2,9,1))
if mibBuilder.loadTexts:gel2esw26kACLPortsConfTable.setStatus(_A)
_Gel2esw26kACLPortsConfEntry_Object=MibTableRow
gel2esw26kACLPortsConfEntry=_Gel2esw26kACLPortsConfEntry_Object((1,3,6,1,4,1,5205,2,54,2,9,1,1))
gel2esw26kACLPortsConfEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:gel2esw26kACLPortsConfEntry.setStatus(_A)
class _Gel2esw26kACLPortsConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kACLPortsConfPort_Type.__name__=_C
_Gel2esw26kACLPortsConfPort_Object=MibTableColumn
gel2esw26kACLPortsConfPort=_Gel2esw26kACLPortsConfPort_Object((1,3,6,1,4,1,5205,2,54,2,9,1,1,1),_Gel2esw26kACLPortsConfPort_Type())
gel2esw26kACLPortsConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kACLPortsConfPort.setStatus(_A)
class _Gel2esw26kACLPortsConfPolicyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Gel2esw26kACLPortsConfPolicyID_Type.__name__=_C
_Gel2esw26kACLPortsConfPolicyID_Object=MibTableColumn
gel2esw26kACLPortsConfPolicyID=_Gel2esw26kACLPortsConfPolicyID_Object((1,3,6,1,4,1,5205,2,54,2,9,1,1,2),_Gel2esw26kACLPortsConfPolicyID_Type())
gel2esw26kACLPortsConfPolicyID.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLPortsConfPolicyID.setStatus(_A)
class _Gel2esw26kACLPortsConfAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kACLPortsConfAction_Type.__name__=_C
_Gel2esw26kACLPortsConfAction_Object=MibTableColumn
gel2esw26kACLPortsConfAction=_Gel2esw26kACLPortsConfAction_Object((1,3,6,1,4,1,5205,2,54,2,9,1,1,3),_Gel2esw26kACLPortsConfAction_Type())
gel2esw26kACLPortsConfAction.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLPortsConfAction.setStatus(_A)
class _Gel2esw26kACLPortsConfRateLimiterID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_Gel2esw26kACLPortsConfRateLimiterID_Type.__name__=_C
_Gel2esw26kACLPortsConfRateLimiterID_Object=MibTableColumn
gel2esw26kACLPortsConfRateLimiterID=_Gel2esw26kACLPortsConfRateLimiterID_Object((1,3,6,1,4,1,5205,2,54,2,9,1,1,4),_Gel2esw26kACLPortsConfRateLimiterID_Type())
gel2esw26kACLPortsConfRateLimiterID.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLPortsConfRateLimiterID.setStatus(_A)
class _Gel2esw26kACLPortsConfPortRedirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_Gel2esw26kACLPortsConfPortRedirect_Type.__name__=_C
_Gel2esw26kACLPortsConfPortRedirect_Object=MibTableColumn
gel2esw26kACLPortsConfPortRedirect=_Gel2esw26kACLPortsConfPortRedirect_Object((1,3,6,1,4,1,5205,2,54,2,9,1,1,5),_Gel2esw26kACLPortsConfPortRedirect_Type())
gel2esw26kACLPortsConfPortRedirect.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLPortsConfPortRedirect.setStatus(_A)
class _Gel2esw26kACLPortsConfMirror_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kACLPortsConfMirror_Type.__name__=_C
_Gel2esw26kACLPortsConfMirror_Object=MibTableColumn
gel2esw26kACLPortsConfMirror=_Gel2esw26kACLPortsConfMirror_Object((1,3,6,1,4,1,5205,2,54,2,9,1,1,6),_Gel2esw26kACLPortsConfMirror_Type())
gel2esw26kACLPortsConfMirror.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLPortsConfMirror.setStatus(_A)
class _Gel2esw26kACLPortsConfLogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kACLPortsConfLogging_Type.__name__=_C
_Gel2esw26kACLPortsConfLogging_Object=MibTableColumn
gel2esw26kACLPortsConfLogging=_Gel2esw26kACLPortsConfLogging_Object((1,3,6,1,4,1,5205,2,54,2,9,1,1,7),_Gel2esw26kACLPortsConfLogging_Type())
gel2esw26kACLPortsConfLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLPortsConfLogging.setStatus(_A)
class _Gel2esw26kACLPortsConfShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kACLPortsConfShutdown_Type.__name__=_C
_Gel2esw26kACLPortsConfShutdown_Object=MibTableColumn
gel2esw26kACLPortsConfShutdown=_Gel2esw26kACLPortsConfShutdown_Object((1,3,6,1,4,1,5205,2,54,2,9,1,1,8),_Gel2esw26kACLPortsConfShutdown_Type())
gel2esw26kACLPortsConfShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLPortsConfShutdown.setStatus(_A)
class _Gel2esw26kACLPortsConfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kACLPortsConfState_Type.__name__=_C
_Gel2esw26kACLPortsConfState_Object=MibTableColumn
gel2esw26kACLPortsConfState=_Gel2esw26kACLPortsConfState_Object((1,3,6,1,4,1,5205,2,54,2,9,1,1,9),_Gel2esw26kACLPortsConfState_Type())
gel2esw26kACLPortsConfState.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLPortsConfState.setStatus(_A)
_Gel2esw26kACLPortsConfCounter_Type=Counter32
_Gel2esw26kACLPortsConfCounter_Object=MibTableColumn
gel2esw26kACLPortsConfCounter=_Gel2esw26kACLPortsConfCounter_Object((1,3,6,1,4,1,5205,2,54,2,9,1,1,10),_Gel2esw26kACLPortsConfCounter_Type())
gel2esw26kACLPortsConfCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kACLPortsConfCounter.setStatus(_A)
_Gel2esw26kACLRateLimiterTable_Object=MibTable
gel2esw26kACLRateLimiterTable=_Gel2esw26kACLRateLimiterTable_Object((1,3,6,1,4,1,5205,2,54,2,9,2))
if mibBuilder.loadTexts:gel2esw26kACLRateLimiterTable.setStatus(_A)
_Gel2esw26kACLRateLimiterEntry_Object=MibTableRow
gel2esw26kACLRateLimiterEntry=_Gel2esw26kACLRateLimiterEntry_Object((1,3,6,1,4,1,5205,2,54,2,9,2,1))
gel2esw26kACLRateLimiterEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:gel2esw26kACLRateLimiterEntry.setStatus(_A)
class _Gel2esw26kACLRateLimiterID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Gel2esw26kACLRateLimiterID_Type.__name__=_C
_Gel2esw26kACLRateLimiterID_Object=MibTableColumn
gel2esw26kACLRateLimiterID=_Gel2esw26kACLRateLimiterID_Object((1,3,6,1,4,1,5205,2,54,2,9,2,1,1),_Gel2esw26kACLRateLimiterID_Type())
gel2esw26kACLRateLimiterID.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kACLRateLimiterID.setStatus(_A)
class _Gel2esw26kACLRateLimiterUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kACLRateLimiterUnit_Type.__name__=_C
_Gel2esw26kACLRateLimiterUnit_Object=MibTableColumn
gel2esw26kACLRateLimiterUnit=_Gel2esw26kACLRateLimiterUnit_Object((1,3,6,1,4,1,5205,2,54,2,9,2,1,2),_Gel2esw26kACLRateLimiterUnit_Type())
gel2esw26kACLRateLimiterUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLRateLimiterUnit.setStatus(_A)
class _Gel2esw26kACLRateLimiterRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3276700))
_Gel2esw26kACLRateLimiterRate_Type.__name__=_C
_Gel2esw26kACLRateLimiterRate_Object=MibTableColumn
gel2esw26kACLRateLimiterRate=_Gel2esw26kACLRateLimiterRate_Object((1,3,6,1,4,1,5205,2,54,2,9,2,1,3),_Gel2esw26kACLRateLimiterRate_Type())
gel2esw26kACLRateLimiterRate.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLRateLimiterRate.setStatus(_A)
_Gel2esw26kACLACE_ObjectIdentity=ObjectIdentity
gel2esw26kACLACE=_Gel2esw26kACLACE_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2,9,3))
class _Gel2esw26kACLACECreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kACLACECreate_Type.__name__=_C
_Gel2esw26kACLACECreate_Object=MibScalar
gel2esw26kACLACECreate=_Gel2esw26kACLACECreate_Object((1,3,6,1,4,1,5205,2,54,2,9,3,1),_Gel2esw26kACLACECreate_Type())
gel2esw26kACLACECreate.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACECreate.setStatus(_A)
_Gel2esw26kACLACETable_Object=MibTable
gel2esw26kACLACETable=_Gel2esw26kACLACETable_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2))
if mibBuilder.loadTexts:gel2esw26kACLACETable.setStatus(_A)
_Gel2esw26kACLACEEntry_Object=MibTableRow
gel2esw26kACLACEEntry=_Gel2esw26kACLACEEntry_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1))
gel2esw26kACLACEEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:gel2esw26kACLACEEntry.setStatus(_A)
class _Gel2esw26kACLACEIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Gel2esw26kACLACEIndex_Type.__name__=_C
_Gel2esw26kACLACEIndex_Object=MibTableColumn
gel2esw26kACLACEIndex=_Gel2esw26kACLACEIndex_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,1),_Gel2esw26kACLACEIndex_Type())
gel2esw26kACLACEIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kACLACEIndex.setStatus(_A)
class _Gel2esw26kACLACEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Gel2esw26kACLACEID_Type.__name__=_C
_Gel2esw26kACLACEID_Object=MibTableColumn
gel2esw26kACLACEID=_Gel2esw26kACLACEID_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,2),_Gel2esw26kACLACEID_Type())
gel2esw26kACLACEID.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEID.setStatus(_A)
class _Gel2esw26kACLACENextID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Gel2esw26kACLACENextID_Type.__name__=_C
_Gel2esw26kACLACENextID_Object=MibTableColumn
gel2esw26kACLACENextID=_Gel2esw26kACLACENextID_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,3),_Gel2esw26kACLACENextID_Type())
gel2esw26kACLACENextID.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACENextID.setStatus(_A)
_Gel2esw26kACLACEIngressPort_Type=DisplayString
_Gel2esw26kACLACEIngressPort_Object=MibTableColumn
gel2esw26kACLACEIngressPort=_Gel2esw26kACLACEIngressPort_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,4),_Gel2esw26kACLACEIngressPort_Type())
gel2esw26kACLACEIngressPort.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEIngressPort.setStatus(_A)
class _Gel2esw26kACLACEPortPolicyNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Gel2esw26kACLACEPortPolicyNumber_Type.__name__=_C
_Gel2esw26kACLACEPortPolicyNumber_Object=MibTableColumn
gel2esw26kACLACEPortPolicyNumber=_Gel2esw26kACLACEPortPolicyNumber_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,5),_Gel2esw26kACLACEPortPolicyNumber_Type())
gel2esw26kACLACEPortPolicyNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEPortPolicyNumber.setStatus(_A)
class _Gel2esw26kACLACEPortPolicyBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Gel2esw26kACLACEPortPolicyBitmask_Type.__name__=_C
_Gel2esw26kACLACEPortPolicyBitmask_Object=MibTableColumn
gel2esw26kACLACEPortPolicyBitmask=_Gel2esw26kACLACEPortPolicyBitmask_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,6),_Gel2esw26kACLACEPortPolicyBitmask_Type())
gel2esw26kACLACEPortPolicyBitmask.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEPortPolicyBitmask.setStatus(_A)
class _Gel2esw26kACLACEFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_Gel2esw26kACLACEFrameType_Type.__name__=_C
_Gel2esw26kACLACEFrameType_Object=MibTableColumn
gel2esw26kACLACEFrameType=_Gel2esw26kACLACEFrameType_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,7),_Gel2esw26kACLACEFrameType_Type())
gel2esw26kACLACEFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEFrameType.setStatus(_A)
class _Gel2esw26kACLACEAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kACLACEAction_Type.__name__=_C
_Gel2esw26kACLACEAction_Object=MibTableColumn
gel2esw26kACLACEAction=_Gel2esw26kACLACEAction_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,8),_Gel2esw26kACLACEAction_Type())
gel2esw26kACLACEAction.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEAction.setStatus(_A)
_Gel2esw26kACLACEDenyPortRedirect_Type=DisplayString
_Gel2esw26kACLACEDenyPortRedirect_Object=MibTableColumn
gel2esw26kACLACEDenyPortRedirect=_Gel2esw26kACLACEDenyPortRedirect_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,9),_Gel2esw26kACLACEDenyPortRedirect_Type())
gel2esw26kACLACEDenyPortRedirect.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEDenyPortRedirect.setStatus(_A)
class _Gel2esw26kACLACELogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kACLACELogging_Type.__name__=_C
_Gel2esw26kACLACELogging_Object=MibTableColumn
gel2esw26kACLACELogging=_Gel2esw26kACLACELogging_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,10),_Gel2esw26kACLACELogging_Type())
gel2esw26kACLACELogging.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACELogging.setStatus(_A)
class _Gel2esw26kACLACEMirror_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kACLACEMirror_Type.__name__=_C
_Gel2esw26kACLACEMirror_Object=MibTableColumn
gel2esw26kACLACEMirror=_Gel2esw26kACLACEMirror_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,11),_Gel2esw26kACLACEMirror_Type())
gel2esw26kACLACEMirror.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEMirror.setStatus(_A)
class _Gel2esw26kACLACERateLimiter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_Gel2esw26kACLACERateLimiter_Type.__name__=_C
_Gel2esw26kACLACERateLimiter_Object=MibTableColumn
gel2esw26kACLACERateLimiter=_Gel2esw26kACLACERateLimiter_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,12),_Gel2esw26kACLACERateLimiter_Type())
gel2esw26kACLACERateLimiter.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACERateLimiter.setStatus(_A)
class _Gel2esw26kACLACEShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kACLACEShutdown_Type.__name__=_C
_Gel2esw26kACLACEShutdown_Object=MibTableColumn
gel2esw26kACLACEShutdown=_Gel2esw26kACLACEShutdown_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,13),_Gel2esw26kACLACEShutdown_Type())
gel2esw26kACLACEShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEShutdown.setStatus(_A)
class _Gel2esw26kACLACEVLAN8021QTagged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACEVLAN8021QTagged_Type.__name__=_C
_Gel2esw26kACLACEVLAN8021QTagged_Object=MibTableColumn
gel2esw26kACLACEVLAN8021QTagged=_Gel2esw26kACLACEVLAN8021QTagged_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,14),_Gel2esw26kACLACEVLAN8021QTagged_Type())
gel2esw26kACLACEVLAN8021QTagged.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEVLAN8021QTagged.setStatus(_A)
class _Gel2esw26kACLACEVLANTagPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_Gel2esw26kACLACEVLANTagPriority_Type.__name__=_C
_Gel2esw26kACLACEVLANTagPriority_Object=MibTableColumn
gel2esw26kACLACEVLANTagPriority=_Gel2esw26kACLACEVLANTagPriority_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,15),_Gel2esw26kACLACEVLANTagPriority_Type())
gel2esw26kACLACEVLANTagPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEVLANTagPriority.setStatus(_A)
class _Gel2esw26kACLACEVLANVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Gel2esw26kACLACEVLANVID_Type.__name__=_C
_Gel2esw26kACLACEVLANVID_Object=MibTableColumn
gel2esw26kACLACEVLANVID=_Gel2esw26kACLACEVLANVID_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,16),_Gel2esw26kACLACEVLANVID_Type())
gel2esw26kACLACEVLANVID.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEVLANVID.setStatus(_A)
class _Gel2esw26kACLACEEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Gel2esw26kACLACEEtherType_Type.__name__=_C
_Gel2esw26kACLACEEtherType_Object=MibTableColumn
gel2esw26kACLACEEtherType=_Gel2esw26kACLACEEtherType_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,17),_Gel2esw26kACLACEEtherType_Type())
gel2esw26kACLACEEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEEtherType.setStatus(_A)
_Gel2esw26kACLACESMAC_Type=DisplayString
_Gel2esw26kACLACESMAC_Object=MibTableColumn
gel2esw26kACLACESMAC=_Gel2esw26kACLACESMAC_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,18),_Gel2esw26kACLACESMAC_Type())
gel2esw26kACLACESMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACESMAC.setStatus(_A)
class _Gel2esw26kACLACEDMACType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Gel2esw26kACLACEDMACType_Type.__name__=_C
_Gel2esw26kACLACEDMACType_Object=MibTableColumn
gel2esw26kACLACEDMACType=_Gel2esw26kACLACEDMACType_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,19),_Gel2esw26kACLACEDMACType_Type())
gel2esw26kACLACEDMACType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEDMACType.setStatus(_A)
_Gel2esw26kACLACEDMAC_Type=DisplayString
_Gel2esw26kACLACEDMAC_Object=MibTableColumn
gel2esw26kACLACEDMAC=_Gel2esw26kACLACEDMAC_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,20),_Gel2esw26kACLACEDMAC_Type())
gel2esw26kACLACEDMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEDMAC.setStatus(_A)
class _Gel2esw26kACLACEArpOpcode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw26kACLACEArpOpcode_Type.__name__=_C
_Gel2esw26kACLACEArpOpcode_Object=MibTableColumn
gel2esw26kACLACEArpOpcode=_Gel2esw26kACLACEArpOpcode_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,21),_Gel2esw26kACLACEArpOpcode_Type())
gel2esw26kACLACEArpOpcode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEArpOpcode.setStatus(_A)
class _Gel2esw26kACLACEArpFlagsRequestReply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACEArpFlagsRequestReply_Type.__name__=_C
_Gel2esw26kACLACEArpFlagsRequestReply_Object=MibTableColumn
gel2esw26kACLACEArpFlagsRequestReply=_Gel2esw26kACLACEArpFlagsRequestReply_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,22),_Gel2esw26kACLACEArpFlagsRequestReply_Type())
gel2esw26kACLACEArpFlagsRequestReply.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEArpFlagsRequestReply.setStatus(_A)
class _Gel2esw26kACLACEArpFlagsArpSmac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACEArpFlagsArpSmac_Type.__name__=_C
_Gel2esw26kACLACEArpFlagsArpSmac_Object=MibTableColumn
gel2esw26kACLACEArpFlagsArpSmac=_Gel2esw26kACLACEArpFlagsArpSmac_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,23),_Gel2esw26kACLACEArpFlagsArpSmac_Type())
gel2esw26kACLACEArpFlagsArpSmac.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEArpFlagsArpSmac.setStatus(_A)
class _Gel2esw26kACLACEArpFlagsRarpDmac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACEArpFlagsRarpDmac_Type.__name__=_C
_Gel2esw26kACLACEArpFlagsRarpDmac_Object=MibTableColumn
gel2esw26kACLACEArpFlagsRarpDmac=_Gel2esw26kACLACEArpFlagsRarpDmac_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,24),_Gel2esw26kACLACEArpFlagsRarpDmac_Type())
gel2esw26kACLACEArpFlagsRarpDmac.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEArpFlagsRarpDmac.setStatus(_A)
class _Gel2esw26kACLACEArpFlagsLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACEArpFlagsLength_Type.__name__=_C
_Gel2esw26kACLACEArpFlagsLength_Object=MibTableColumn
gel2esw26kACLACEArpFlagsLength=_Gel2esw26kACLACEArpFlagsLength_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,25),_Gel2esw26kACLACEArpFlagsLength_Type())
gel2esw26kACLACEArpFlagsLength.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEArpFlagsLength.setStatus(_A)
class _Gel2esw26kACLACEArpFlagsIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACEArpFlagsIp_Type.__name__=_C
_Gel2esw26kACLACEArpFlagsIp_Object=MibTableColumn
gel2esw26kACLACEArpFlagsIp=_Gel2esw26kACLACEArpFlagsIp_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,26),_Gel2esw26kACLACEArpFlagsIp_Type())
gel2esw26kACLACEArpFlagsIp.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEArpFlagsIp.setStatus(_A)
class _Gel2esw26kACLACEArpFlagsEthernet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACEArpFlagsEthernet_Type.__name__=_C
_Gel2esw26kACLACEArpFlagsEthernet_Object=MibTableColumn
gel2esw26kACLACEArpFlagsEthernet=_Gel2esw26kACLACEArpFlagsEthernet_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,27),_Gel2esw26kACLACEArpFlagsEthernet_Type())
gel2esw26kACLACEArpFlagsEthernet.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEArpFlagsEthernet.setStatus(_A)
class _Gel2esw26kACLACESIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kACLACESIPType_Type.__name__=_C
_Gel2esw26kACLACESIPType_Object=MibTableColumn
gel2esw26kACLACESIPType=_Gel2esw26kACLACESIPType_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,28),_Gel2esw26kACLACESIPType_Type())
gel2esw26kACLACESIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACESIPType.setStatus(_A)
_Gel2esw26kACLACESIPIPAddress_Type=IpAddress
_Gel2esw26kACLACESIPIPAddress_Object=MibTableColumn
gel2esw26kACLACESIPIPAddress=_Gel2esw26kACLACESIPIPAddress_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,29),_Gel2esw26kACLACESIPIPAddress_Type())
gel2esw26kACLACESIPIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACESIPIPAddress.setStatus(_A)
class _Gel2esw26kACLACESIPNetworkPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Gel2esw26kACLACESIPNetworkPrefix_Type.__name__=_C
_Gel2esw26kACLACESIPNetworkPrefix_Object=MibTableColumn
gel2esw26kACLACESIPNetworkPrefix=_Gel2esw26kACLACESIPNetworkPrefix_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,30),_Gel2esw26kACLACESIPNetworkPrefix_Type())
gel2esw26kACLACESIPNetworkPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACESIPNetworkPrefix.setStatus(_A)
class _Gel2esw26kACLACEDIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kACLACEDIPType_Type.__name__=_C
_Gel2esw26kACLACEDIPType_Object=MibTableColumn
gel2esw26kACLACEDIPType=_Gel2esw26kACLACEDIPType_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,32),_Gel2esw26kACLACEDIPType_Type())
gel2esw26kACLACEDIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEDIPType.setStatus(_A)
_Gel2esw26kACLACEDIPIPAddress_Type=IpAddress
_Gel2esw26kACLACEDIPIPAddress_Object=MibTableColumn
gel2esw26kACLACEDIPIPAddress=_Gel2esw26kACLACEDIPIPAddress_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,33),_Gel2esw26kACLACEDIPIPAddress_Type())
gel2esw26kACLACEDIPIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEDIPIPAddress.setStatus(_A)
class _Gel2esw26kACLACEDIPNetworkPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Gel2esw26kACLACEDIPNetworkPrefix_Type.__name__=_C
_Gel2esw26kACLACEDIPNetworkPrefix_Object=MibTableColumn
gel2esw26kACLACEDIPNetworkPrefix=_Gel2esw26kACLACEDIPNetworkPrefix_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,34),_Gel2esw26kACLACEDIPNetworkPrefix_Type())
gel2esw26kACLACEDIPNetworkPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEDIPNetworkPrefix.setStatus(_A)
class _Gel2esw26kACLACEIPProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Gel2esw26kACLACEIPProtocol_Type.__name__=_C
_Gel2esw26kACLACEIPProtocol_Object=MibTableColumn
gel2esw26kACLACEIPProtocol=_Gel2esw26kACLACEIPProtocol_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,36),_Gel2esw26kACLACEIPProtocol_Type())
gel2esw26kACLACEIPProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEIPProtocol.setStatus(_A)
class _Gel2esw26kACLACEIPFlagsTTL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACEIPFlagsTTL_Type.__name__=_C
_Gel2esw26kACLACEIPFlagsTTL_Object=MibTableColumn
gel2esw26kACLACEIPFlagsTTL=_Gel2esw26kACLACEIPFlagsTTL_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,37),_Gel2esw26kACLACEIPFlagsTTL_Type())
gel2esw26kACLACEIPFlagsTTL.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEIPFlagsTTL.setStatus(_A)
class _Gel2esw26kACLACEIPFlagsOptions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACEIPFlagsOptions_Type.__name__=_C
_Gel2esw26kACLACEIPFlagsOptions_Object=MibTableColumn
gel2esw26kACLACEIPFlagsOptions=_Gel2esw26kACLACEIPFlagsOptions_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,38),_Gel2esw26kACLACEIPFlagsOptions_Type())
gel2esw26kACLACEIPFlagsOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEIPFlagsOptions.setStatus(_A)
class _Gel2esw26kACLACEIPFlagsFragment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACEIPFlagsFragment_Type.__name__=_C
_Gel2esw26kACLACEIPFlagsFragment_Object=MibTableColumn
gel2esw26kACLACEIPFlagsFragment=_Gel2esw26kACLACEIPFlagsFragment_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,39),_Gel2esw26kACLACEIPFlagsFragment_Type())
gel2esw26kACLACEIPFlagsFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEIPFlagsFragment.setStatus(_A)
class _Gel2esw26kACLACEICMPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Gel2esw26kACLACEICMPType_Type.__name__=_C
_Gel2esw26kACLACEICMPType_Object=MibTableColumn
gel2esw26kACLACEICMPType=_Gel2esw26kACLACEICMPType_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,40),_Gel2esw26kACLACEICMPType_Type())
gel2esw26kACLACEICMPType.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEICMPType.setStatus(_A)
class _Gel2esw26kACLACEICMPCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Gel2esw26kACLACEICMPCode_Type.__name__=_C
_Gel2esw26kACLACEICMPCode_Object=MibTableColumn
gel2esw26kACLACEICMPCode=_Gel2esw26kACLACEICMPCode_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,41),_Gel2esw26kACLACEICMPCode_Type())
gel2esw26kACLACEICMPCode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEICMPCode.setStatus(_A)
class _Gel2esw26kACLACESourcePortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Gel2esw26kACLACESourcePortMin_Type.__name__=_C
_Gel2esw26kACLACESourcePortMin_Object=MibTableColumn
gel2esw26kACLACESourcePortMin=_Gel2esw26kACLACESourcePortMin_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,42),_Gel2esw26kACLACESourcePortMin_Type())
gel2esw26kACLACESourcePortMin.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACESourcePortMin.setStatus(_A)
class _Gel2esw26kACLACESourcePortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Gel2esw26kACLACESourcePortMax_Type.__name__=_C
_Gel2esw26kACLACESourcePortMax_Object=MibTableColumn
gel2esw26kACLACESourcePortMax=_Gel2esw26kACLACESourcePortMax_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,43),_Gel2esw26kACLACESourcePortMax_Type())
gel2esw26kACLACESourcePortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACESourcePortMax.setStatus(_A)
class _Gel2esw26kACLACEDestPortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Gel2esw26kACLACEDestPortMin_Type.__name__=_C
_Gel2esw26kACLACEDestPortMin_Object=MibTableColumn
gel2esw26kACLACEDestPortMin=_Gel2esw26kACLACEDestPortMin_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,44),_Gel2esw26kACLACEDestPortMin_Type())
gel2esw26kACLACEDestPortMin.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEDestPortMin.setStatus(_A)
class _Gel2esw26kACLACEDestPortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Gel2esw26kACLACEDestPortMax_Type.__name__=_C
_Gel2esw26kACLACEDestPortMax_Object=MibTableColumn
gel2esw26kACLACEDestPortMax=_Gel2esw26kACLACEDestPortMax_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,45),_Gel2esw26kACLACEDestPortMax_Type())
gel2esw26kACLACEDestPortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEDestPortMax.setStatus(_A)
class _Gel2esw26kACLACETCPFlagsFin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACETCPFlagsFin_Type.__name__=_C
_Gel2esw26kACLACETCPFlagsFin_Object=MibTableColumn
gel2esw26kACLACETCPFlagsFin=_Gel2esw26kACLACETCPFlagsFin_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,46),_Gel2esw26kACLACETCPFlagsFin_Type())
gel2esw26kACLACETCPFlagsFin.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACETCPFlagsFin.setStatus(_A)
class _Gel2esw26kACLACETCPFlagsSyn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACETCPFlagsSyn_Type.__name__=_C
_Gel2esw26kACLACETCPFlagsSyn_Object=MibTableColumn
gel2esw26kACLACETCPFlagsSyn=_Gel2esw26kACLACETCPFlagsSyn_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,47),_Gel2esw26kACLACETCPFlagsSyn_Type())
gel2esw26kACLACETCPFlagsSyn.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACETCPFlagsSyn.setStatus(_A)
class _Gel2esw26kACLACETCPFlagsRst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACETCPFlagsRst_Type.__name__=_C
_Gel2esw26kACLACETCPFlagsRst_Object=MibTableColumn
gel2esw26kACLACETCPFlagsRst=_Gel2esw26kACLACETCPFlagsRst_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,48),_Gel2esw26kACLACETCPFlagsRst_Type())
gel2esw26kACLACETCPFlagsRst.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACETCPFlagsRst.setStatus(_A)
class _Gel2esw26kACLACETCPFlagsPsh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACETCPFlagsPsh_Type.__name__=_C
_Gel2esw26kACLACETCPFlagsPsh_Object=MibTableColumn
gel2esw26kACLACETCPFlagsPsh=_Gel2esw26kACLACETCPFlagsPsh_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,49),_Gel2esw26kACLACETCPFlagsPsh_Type())
gel2esw26kACLACETCPFlagsPsh.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACETCPFlagsPsh.setStatus(_A)
class _Gel2esw26kACLACETCPFlagsAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACETCPFlagsAck_Type.__name__=_C
_Gel2esw26kACLACETCPFlagsAck_Object=MibTableColumn
gel2esw26kACLACETCPFlagsAck=_Gel2esw26kACLACETCPFlagsAck_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,50),_Gel2esw26kACLACETCPFlagsAck_Type())
gel2esw26kACLACETCPFlagsAck.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACETCPFlagsAck.setStatus(_A)
class _Gel2esw26kACLACETCPFlagsUrg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kACLACETCPFlagsUrg_Type.__name__=_C
_Gel2esw26kACLACETCPFlagsUrg_Object=MibTableColumn
gel2esw26kACLACETCPFlagsUrg=_Gel2esw26kACLACETCPFlagsUrg_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,51),_Gel2esw26kACLACETCPFlagsUrg_Type())
gel2esw26kACLACETCPFlagsUrg.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACETCPFlagsUrg.setStatus(_A)
class _Gel2esw26kACLACERowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw26kACLACERowStatus_Type.__name__=_C
_Gel2esw26kACLACERowStatus_Object=MibTableColumn
gel2esw26kACLACERowStatus=_Gel2esw26kACLACERowStatus_Object((1,3,6,1,4,1,5205,2,54,2,9,3,2,1,66),_Gel2esw26kACLACERowStatus_Type())
gel2esw26kACLACERowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACERowStatus.setStatus(_A)
class _Gel2esw26kACLACEClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kACLACEClear_Type.__name__=_C
_Gel2esw26kACLACEClear_Object=MibScalar
gel2esw26kACLACEClear=_Gel2esw26kACLACEClear_Object((1,3,6,1,4,1,5205,2,54,2,9,3,3),_Gel2esw26kACLACEClear_Type())
gel2esw26kACLACEClear.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEClear.setStatus(_A)
class _Gel2esw26kACLACEMoveACEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Gel2esw26kACLACEMoveACEID_Type.__name__=_C
_Gel2esw26kACLACEMoveACEID_Object=MibScalar
gel2esw26kACLACEMoveACEID=_Gel2esw26kACLACEMoveACEID_Object((1,3,6,1,4,1,5205,2,54,2,9,3,4),_Gel2esw26kACLACEMoveACEID_Type())
gel2esw26kACLACEMoveACEID.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEMoveACEID.setStatus(_A)
class _Gel2esw26kACLACEMoveNextACEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Gel2esw26kACLACEMoveNextACEID_Type.__name__=_C
_Gel2esw26kACLACEMoveNextACEID_Object=MibScalar
gel2esw26kACLACEMoveNextACEID=_Gel2esw26kACLACEMoveNextACEID_Object((1,3,6,1,4,1,5205,2,54,2,9,3,5),_Gel2esw26kACLACEMoveNextACEID_Type())
gel2esw26kACLACEMoveNextACEID.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kACLACEMoveNextACEID.setStatus(_A)
_Gel2esw26kACLACEStatusTable_Object=MibTable
gel2esw26kACLACEStatusTable=_Gel2esw26kACLACEStatusTable_Object((1,3,6,1,4,1,5205,2,54,2,9,3,6))
if mibBuilder.loadTexts:gel2esw26kACLACEStatusTable.setStatus(_A)
_Gel2esw26kACLACEStatusEntry_Object=MibTableRow
gel2esw26kACLACEStatusEntry=_Gel2esw26kACLACEStatusEntry_Object((1,3,6,1,4,1,5205,2,54,2,9,3,6,1))
gel2esw26kACLACEStatusEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:gel2esw26kACLACEStatusEntry.setStatus(_A)
class _Gel2esw26kACLACEStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Gel2esw26kACLACEStatusIndex_Type.__name__=_C
_Gel2esw26kACLACEStatusIndex_Object=MibTableColumn
gel2esw26kACLACEStatusIndex=_Gel2esw26kACLACEStatusIndex_Object((1,3,6,1,4,1,5205,2,54,2,9,3,6,1,1),_Gel2esw26kACLACEStatusIndex_Type())
gel2esw26kACLACEStatusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kACLACEStatusIndex.setStatus(_A)
_Gel2esw26kACLACEStatusUser_Type=DisplayString
_Gel2esw26kACLACEStatusUser_Object=MibTableColumn
gel2esw26kACLACEStatusUser=_Gel2esw26kACLACEStatusUser_Object((1,3,6,1,4,1,5205,2,54,2,9,3,6,1,2),_Gel2esw26kACLACEStatusUser_Type())
gel2esw26kACLACEStatusUser.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kACLACEStatusUser.setStatus(_A)
class _Gel2esw26kACLACEStatusID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Gel2esw26kACLACEStatusID_Type.__name__=_C
_Gel2esw26kACLACEStatusID_Object=MibTableColumn
gel2esw26kACLACEStatusID=_Gel2esw26kACLACEStatusID_Object((1,3,6,1,4,1,5205,2,54,2,9,3,6,1,3),_Gel2esw26kACLACEStatusID_Type())
gel2esw26kACLACEStatusID.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kACLACEStatusID.setStatus(_A)
_Gel2esw26kACLACEStatusIngressPort_Type=DisplayString
_Gel2esw26kACLACEStatusIngressPort_Object=MibTableColumn
gel2esw26kACLACEStatusIngressPort=_Gel2esw26kACLACEStatusIngressPort_Object((1,3,6,1,4,1,5205,2,54,2,9,3,6,1,4),_Gel2esw26kACLACEStatusIngressPort_Type())
gel2esw26kACLACEStatusIngressPort.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kACLACEStatusIngressPort.setStatus(_A)
_Gel2esw26kACLACEStatusFrameType_Type=DisplayString
_Gel2esw26kACLACEStatusFrameType_Object=MibTableColumn
gel2esw26kACLACEStatusFrameType=_Gel2esw26kACLACEStatusFrameType_Object((1,3,6,1,4,1,5205,2,54,2,9,3,6,1,5),_Gel2esw26kACLACEStatusFrameType_Type())
gel2esw26kACLACEStatusFrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kACLACEStatusFrameType.setStatus(_A)
_Gel2esw26kACLACEStatusAction_Type=DisplayString
_Gel2esw26kACLACEStatusAction_Object=MibTableColumn
gel2esw26kACLACEStatusAction=_Gel2esw26kACLACEStatusAction_Object((1,3,6,1,4,1,5205,2,54,2,9,3,6,1,6),_Gel2esw26kACLACEStatusAction_Type())
gel2esw26kACLACEStatusAction.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kACLACEStatusAction.setStatus(_A)
_Gel2esw26kACLACEStatusRateLimiter_Type=DisplayString
_Gel2esw26kACLACEStatusRateLimiter_Object=MibTableColumn
gel2esw26kACLACEStatusRateLimiter=_Gel2esw26kACLACEStatusRateLimiter_Object((1,3,6,1,4,1,5205,2,54,2,9,3,6,1,7),_Gel2esw26kACLACEStatusRateLimiter_Type())
gel2esw26kACLACEStatusRateLimiter.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kACLACEStatusRateLimiter.setStatus(_A)
_Gel2esw26kACLACEStatusPortCopy_Type=DisplayString
_Gel2esw26kACLACEStatusPortCopy_Object=MibTableColumn
gel2esw26kACLACEStatusPortCopy=_Gel2esw26kACLACEStatusPortCopy_Object((1,3,6,1,4,1,5205,2,54,2,9,3,6,1,8),_Gel2esw26kACLACEStatusPortCopy_Type())
gel2esw26kACLACEStatusPortCopy.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kACLACEStatusPortCopy.setStatus(_A)
_Gel2esw26kACLACEStatusMirror_Type=DisplayString
_Gel2esw26kACLACEStatusMirror_Object=MibTableColumn
gel2esw26kACLACEStatusMirror=_Gel2esw26kACLACEStatusMirror_Object((1,3,6,1,4,1,5205,2,54,2,9,3,6,1,9),_Gel2esw26kACLACEStatusMirror_Type())
gel2esw26kACLACEStatusMirror.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kACLACEStatusMirror.setStatus(_A)
_Gel2esw26kACLACEStatusCPU_Type=DisplayString
_Gel2esw26kACLACEStatusCPU_Object=MibTableColumn
gel2esw26kACLACEStatusCPU=_Gel2esw26kACLACEStatusCPU_Object((1,3,6,1,4,1,5205,2,54,2,9,3,6,1,10),_Gel2esw26kACLACEStatusCPU_Type())
gel2esw26kACLACEStatusCPU.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kACLACEStatusCPU.setStatus(_A)
_Gel2esw26kACLACEStatusCounter_Type=Counter32
_Gel2esw26kACLACEStatusCounter_Object=MibTableColumn
gel2esw26kACLACEStatusCounter=_Gel2esw26kACLACEStatusCounter_Object((1,3,6,1,4,1,5205,2,54,2,9,3,6,1,11),_Gel2esw26kACLACEStatusCounter_Type())
gel2esw26kACLACEStatusCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kACLACEStatusCounter.setStatus(_A)
_Gel2esw26kACLACEStatusConflict_Type=DisplayString
_Gel2esw26kACLACEStatusConflict_Object=MibTableColumn
gel2esw26kACLACEStatusConflict=_Gel2esw26kACLACEStatusConflict_Object((1,3,6,1,4,1,5205,2,54,2,9,3,6,1,12),_Gel2esw26kACLACEStatusConflict_Type())
gel2esw26kACLACEStatusConflict.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kACLACEStatusConflict.setStatus(_A)
_Gel2esw26kLoopProtection_ObjectIdentity=ObjectIdentity
gel2esw26kLoopProtection=_Gel2esw26kLoopProtection_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2,12))
_Gel2esw26kLoopProtectionConfig_ObjectIdentity=ObjectIdentity
gel2esw26kLoopProtectionConfig=_Gel2esw26kLoopProtectionConfig_ObjectIdentity((1,3,6,1,4,1,5205,2,54,2,12,1))
class _Gel2esw26kLoopProtectionGlobalEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kLoopProtectionGlobalEnable_Type.__name__=_C
_Gel2esw26kLoopProtectionGlobalEnable_Object=MibScalar
gel2esw26kLoopProtectionGlobalEnable=_Gel2esw26kLoopProtectionGlobalEnable_Object((1,3,6,1,4,1,5205,2,54,2,12,1,1),_Gel2esw26kLoopProtectionGlobalEnable_Type())
gel2esw26kLoopProtectionGlobalEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kLoopProtectionGlobalEnable.setStatus(_A)
class _Gel2esw26kLoopProtectionTranmisstionTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Gel2esw26kLoopProtectionTranmisstionTime_Type.__name__=_C
_Gel2esw26kLoopProtectionTranmisstionTime_Object=MibScalar
gel2esw26kLoopProtectionTranmisstionTime=_Gel2esw26kLoopProtectionTranmisstionTime_Object((1,3,6,1,4,1,5205,2,54,2,12,1,2),_Gel2esw26kLoopProtectionTranmisstionTime_Type())
gel2esw26kLoopProtectionTranmisstionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kLoopProtectionTranmisstionTime.setStatus(_A)
class _Gel2esw26kLoopProtectionShutdownTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_Gel2esw26kLoopProtectionShutdownTime_Type.__name__=_C
_Gel2esw26kLoopProtectionShutdownTime_Object=MibScalar
gel2esw26kLoopProtectionShutdownTime=_Gel2esw26kLoopProtectionShutdownTime_Object((1,3,6,1,4,1,5205,2,54,2,12,1,3),_Gel2esw26kLoopProtectionShutdownTime_Type())
gel2esw26kLoopProtectionShutdownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kLoopProtectionShutdownTime.setStatus(_A)
_Gel2esw26kLoopProtectionConfigurationTable_Object=MibTable
gel2esw26kLoopProtectionConfigurationTable=_Gel2esw26kLoopProtectionConfigurationTable_Object((1,3,6,1,4,1,5205,2,54,2,12,1,4))
if mibBuilder.loadTexts:gel2esw26kLoopProtectionConfigurationTable.setStatus(_A)
_Gel2esw26kLoopProtectionConfigurationEntry_Object=MibTableRow
gel2esw26kLoopProtectionConfigurationEntry=_Gel2esw26kLoopProtectionConfigurationEntry_Object((1,3,6,1,4,1,5205,2,54,2,12,1,4,1))
gel2esw26kLoopProtectionConfigurationEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:gel2esw26kLoopProtectionConfigurationEntry.setStatus(_A)
class _Gel2esw26kLoopProtectionConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kLoopProtectionConfPort_Type.__name__=_C
_Gel2esw26kLoopProtectionConfPort_Object=MibTableColumn
gel2esw26kLoopProtectionConfPort=_Gel2esw26kLoopProtectionConfPort_Object((1,3,6,1,4,1,5205,2,54,2,12,1,4,1,1),_Gel2esw26kLoopProtectionConfPort_Type())
gel2esw26kLoopProtectionConfPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kLoopProtectionConfPort.setStatus(_A)
class _Gel2esw26kLoopProtectionConfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kLoopProtectionConfEnable_Type.__name__=_C
_Gel2esw26kLoopProtectionConfEnable_Object=MibTableColumn
gel2esw26kLoopProtectionConfEnable=_Gel2esw26kLoopProtectionConfEnable_Object((1,3,6,1,4,1,5205,2,54,2,12,1,4,1,2),_Gel2esw26kLoopProtectionConfEnable_Type())
gel2esw26kLoopProtectionConfEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kLoopProtectionConfEnable.setStatus(_A)
class _Gel2esw26kLoopProtectionConfAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kLoopProtectionConfAction_Type.__name__=_C
_Gel2esw26kLoopProtectionConfAction_Object=MibTableColumn
gel2esw26kLoopProtectionConfAction=_Gel2esw26kLoopProtectionConfAction_Object((1,3,6,1,4,1,5205,2,54,2,12,1,4,1,3),_Gel2esw26kLoopProtectionConfAction_Type())
gel2esw26kLoopProtectionConfAction.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kLoopProtectionConfAction.setStatus(_A)
class _Gel2esw26kLoopProtectionConfTxmode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kLoopProtectionConfTxmode_Type.__name__=_C
_Gel2esw26kLoopProtectionConfTxmode_Object=MibTableColumn
gel2esw26kLoopProtectionConfTxmode=_Gel2esw26kLoopProtectionConfTxmode_Object((1,3,6,1,4,1,5205,2,54,2,12,1,4,1,4),_Gel2esw26kLoopProtectionConfTxmode_Type())
gel2esw26kLoopProtectionConfTxmode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kLoopProtectionConfTxmode.setStatus(_A)
_Gel2esw26kLoopProtectionStatusTable_Object=MibTable
gel2esw26kLoopProtectionStatusTable=_Gel2esw26kLoopProtectionStatusTable_Object((1,3,6,1,4,1,5205,2,54,2,12,2))
if mibBuilder.loadTexts:gel2esw26kLoopProtectionStatusTable.setStatus(_A)
_Gel2esw26kLoopProtectionStatusEntry_Object=MibTableRow
gel2esw26kLoopProtectionStatusEntry=_Gel2esw26kLoopProtectionStatusEntry_Object((1,3,6,1,4,1,5205,2,54,2,12,2,1))
gel2esw26kLoopProtectionStatusEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:gel2esw26kLoopProtectionStatusEntry.setStatus(_A)
class _Gel2esw26kLoopProtectionStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kLoopProtectionStatusPort_Type.__name__=_C
_Gel2esw26kLoopProtectionStatusPort_Object=MibTableColumn
gel2esw26kLoopProtectionStatusPort=_Gel2esw26kLoopProtectionStatusPort_Object((1,3,6,1,4,1,5205,2,54,2,12,2,1,1),_Gel2esw26kLoopProtectionStatusPort_Type())
gel2esw26kLoopProtectionStatusPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kLoopProtectionStatusPort.setStatus(_A)
_Gel2esw26kLoopProtectionStatusAction_Type=DisplayString
_Gel2esw26kLoopProtectionStatusAction_Object=MibTableColumn
gel2esw26kLoopProtectionStatusAction=_Gel2esw26kLoopProtectionStatusAction_Object((1,3,6,1,4,1,5205,2,54,2,12,2,1,2),_Gel2esw26kLoopProtectionStatusAction_Type())
gel2esw26kLoopProtectionStatusAction.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kLoopProtectionStatusAction.setStatus(_A)
_Gel2esw26kLoopProtectionStatusTransmit_Type=DisplayString
_Gel2esw26kLoopProtectionStatusTransmit_Object=MibTableColumn
gel2esw26kLoopProtectionStatusTransmit=_Gel2esw26kLoopProtectionStatusTransmit_Object((1,3,6,1,4,1,5205,2,54,2,12,2,1,3),_Gel2esw26kLoopProtectionStatusTransmit_Type())
gel2esw26kLoopProtectionStatusTransmit.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kLoopProtectionStatusTransmit.setStatus(_A)
class _Gel2esw26kLoopProtectionStatusLoops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_Gel2esw26kLoopProtectionStatusLoops_Type.__name__=_C
_Gel2esw26kLoopProtectionStatusLoops_Object=MibTableColumn
gel2esw26kLoopProtectionStatusLoops=_Gel2esw26kLoopProtectionStatusLoops_Object((1,3,6,1,4,1,5205,2,54,2,12,2,1,4),_Gel2esw26kLoopProtectionStatusLoops_Type())
gel2esw26kLoopProtectionStatusLoops.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kLoopProtectionStatusLoops.setStatus(_A)
_Gel2esw26kLoopProtectionStatusStatus_Type=DisplayString
_Gel2esw26kLoopProtectionStatusStatus_Object=MibTableColumn
gel2esw26kLoopProtectionStatusStatus=_Gel2esw26kLoopProtectionStatusStatus_Object((1,3,6,1,4,1,5205,2,54,2,12,2,1,5),_Gel2esw26kLoopProtectionStatusStatus_Type())
gel2esw26kLoopProtectionStatusStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kLoopProtectionStatusStatus.setStatus(_A)
_Gel2esw26kLoopProtectionStatusLoop_Type=DisplayString
_Gel2esw26kLoopProtectionStatusLoop_Object=MibTableColumn
gel2esw26kLoopProtectionStatusLoop=_Gel2esw26kLoopProtectionStatusLoop_Object((1,3,6,1,4,1,5205,2,54,2,12,2,1,6),_Gel2esw26kLoopProtectionStatusLoop_Type())
gel2esw26kLoopProtectionStatusLoop.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kLoopProtectionStatusLoop.setStatus(_A)
_Gel2esw26kLoopProtectionStatusTimeLastLoop_Type=DisplayString
_Gel2esw26kLoopProtectionStatusTimeLastLoop_Object=MibTableColumn
gel2esw26kLoopProtectionStatusTimeLastLoop=_Gel2esw26kLoopProtectionStatusTimeLastLoop_Object((1,3,6,1,4,1,5205,2,54,2,12,2,1,7),_Gel2esw26kLoopProtectionStatusTimeLastLoop_Type())
gel2esw26kLoopProtectionStatusTimeLastLoop.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kLoopProtectionStatusTimeLastLoop.setStatus(_A)
_Gel2esw26kSecurity_ObjectIdentity=ObjectIdentity
gel2esw26kSecurity=_Gel2esw26kSecurity_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3))
_Gel2esw26kIPSourceGuard_ObjectIdentity=ObjectIdentity
gel2esw26kIPSourceGuard=_Gel2esw26kIPSourceGuard_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,1))
_Gel2esw26kIPSourceGuardConf_ObjectIdentity=ObjectIdentity
gel2esw26kIPSourceGuardConf=_Gel2esw26kIPSourceGuardConf_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,1,1))
class _Gel2esw26kIPSourceGuardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kIPSourceGuardMode_Type.__name__=_C
_Gel2esw26kIPSourceGuardMode_Object=MibScalar
gel2esw26kIPSourceGuardMode=_Gel2esw26kIPSourceGuardMode_Object((1,3,6,1,4,1,5205,2,54,3,1,1,1),_Gel2esw26kIPSourceGuardMode_Type())
gel2esw26kIPSourceGuardMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardMode.setStatus(_A)
_Gel2esw26kIPSourceGuardPortConfigTable_Object=MibTable
gel2esw26kIPSourceGuardPortConfigTable=_Gel2esw26kIPSourceGuardPortConfigTable_Object((1,3,6,1,4,1,5205,2,54,3,1,1,2))
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardPortConfigTable.setStatus(_A)
_Gel2esw26kIPSourceGuardPortConfigEntry_Object=MibTableRow
gel2esw26kIPSourceGuardPortConfigEntry=_Gel2esw26kIPSourceGuardPortConfigEntry_Object((1,3,6,1,4,1,5205,2,54,3,1,1,2,1))
gel2esw26kIPSourceGuardPortConfigEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardPortConfigEntry.setStatus(_A)
class _Gel2esw26kIPSourceGuardPortConfigPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kIPSourceGuardPortConfigPort_Type.__name__=_C
_Gel2esw26kIPSourceGuardPortConfigPort_Object=MibTableColumn
gel2esw26kIPSourceGuardPortConfigPort=_Gel2esw26kIPSourceGuardPortConfigPort_Object((1,3,6,1,4,1,5205,2,54,3,1,1,2,1,1),_Gel2esw26kIPSourceGuardPortConfigPort_Type())
gel2esw26kIPSourceGuardPortConfigPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardPortConfigPort.setStatus(_A)
class _Gel2esw26kIPSourceGuardPortConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kIPSourceGuardPortConfigMode_Type.__name__=_C
_Gel2esw26kIPSourceGuardPortConfigMode_Object=MibTableColumn
gel2esw26kIPSourceGuardPortConfigMode=_Gel2esw26kIPSourceGuardPortConfigMode_Object((1,3,6,1,4,1,5205,2,54,3,1,1,2,1,2),_Gel2esw26kIPSourceGuardPortConfigMode_Type())
gel2esw26kIPSourceGuardPortConfigMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardPortConfigMode.setStatus(_A)
class _Gel2esw26kIPSourceGuardPortMaxDynamicClients_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2),ValueRangeConstraint(99,99))
_Gel2esw26kIPSourceGuardPortMaxDynamicClients_Type.__name__=_C
_Gel2esw26kIPSourceGuardPortMaxDynamicClients_Object=MibTableColumn
gel2esw26kIPSourceGuardPortMaxDynamicClients=_Gel2esw26kIPSourceGuardPortMaxDynamicClients_Object((1,3,6,1,4,1,5205,2,54,3,1,1,2,1,3),_Gel2esw26kIPSourceGuardPortMaxDynamicClients_Type())
gel2esw26kIPSourceGuardPortMaxDynamicClients.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardPortMaxDynamicClients.setStatus(_A)
_Gel2esw26kIPSourceGuardStatic_ObjectIdentity=ObjectIdentity
gel2esw26kIPSourceGuardStatic=_Gel2esw26kIPSourceGuardStatic_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,1,2))
class _Gel2esw26kIPSourceGuardStaticCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kIPSourceGuardStaticCreate_Type.__name__=_C
_Gel2esw26kIPSourceGuardStaticCreate_Object=MibScalar
gel2esw26kIPSourceGuardStaticCreate=_Gel2esw26kIPSourceGuardStaticCreate_Object((1,3,6,1,4,1,5205,2,54,3,1,2,1),_Gel2esw26kIPSourceGuardStaticCreate_Type())
gel2esw26kIPSourceGuardStaticCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardStaticCreate.setStatus(_A)
_Gel2esw26kIPSourceGuardStaticTable_Object=MibTable
gel2esw26kIPSourceGuardStaticTable=_Gel2esw26kIPSourceGuardStaticTable_Object((1,3,6,1,4,1,5205,2,54,3,1,2,2))
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardStaticTable.setStatus(_A)
_Gel2esw26kIPSourceGuardStaticEntry_Object=MibTableRow
gel2esw26kIPSourceGuardStaticEntry=_Gel2esw26kIPSourceGuardStaticEntry_Object((1,3,6,1,4,1,5205,2,54,3,1,2,2,1))
gel2esw26kIPSourceGuardStaticEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardStaticEntry.setStatus(_A)
class _Gel2esw26kIPSourceGuardStaticIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_Gel2esw26kIPSourceGuardStaticIndex_Type.__name__=_C
_Gel2esw26kIPSourceGuardStaticIndex_Object=MibTableColumn
gel2esw26kIPSourceGuardStaticIndex=_Gel2esw26kIPSourceGuardStaticIndex_Object((1,3,6,1,4,1,5205,2,54,3,1,2,2,1,1),_Gel2esw26kIPSourceGuardStaticIndex_Type())
gel2esw26kIPSourceGuardStaticIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardStaticIndex.setStatus(_A)
class _Gel2esw26kIPSourceGuardStaticPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kIPSourceGuardStaticPort_Type.__name__=_C
_Gel2esw26kIPSourceGuardStaticPort_Object=MibTableColumn
gel2esw26kIPSourceGuardStaticPort=_Gel2esw26kIPSourceGuardStaticPort_Object((1,3,6,1,4,1,5205,2,54,3,1,2,2,1,2),_Gel2esw26kIPSourceGuardStaticPort_Type())
gel2esw26kIPSourceGuardStaticPort.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardStaticPort.setStatus(_A)
class _Gel2esw26kIPSourceGuardStaticVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw26kIPSourceGuardStaticVLANId_Type.__name__=_C
_Gel2esw26kIPSourceGuardStaticVLANId_Object=MibTableColumn
gel2esw26kIPSourceGuardStaticVLANId=_Gel2esw26kIPSourceGuardStaticVLANId_Object((1,3,6,1,4,1,5205,2,54,3,1,2,2,1,3),_Gel2esw26kIPSourceGuardStaticVLANId_Type())
gel2esw26kIPSourceGuardStaticVLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardStaticVLANId.setStatus(_A)
_Gel2esw26kIPSourceGuardStaticIPAddress_Type=IpAddress
_Gel2esw26kIPSourceGuardStaticIPAddress_Object=MibTableColumn
gel2esw26kIPSourceGuardStaticIPAddress=_Gel2esw26kIPSourceGuardStaticIPAddress_Object((1,3,6,1,4,1,5205,2,54,3,1,2,2,1,4),_Gel2esw26kIPSourceGuardStaticIPAddress_Type())
gel2esw26kIPSourceGuardStaticIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardStaticIPAddress.setStatus(_A)
_Gel2esw26kIPSourceGuardStaticMACAddress_Type=MacAddress
_Gel2esw26kIPSourceGuardStaticMACAddress_Object=MibTableColumn
gel2esw26kIPSourceGuardStaticMACAddress=_Gel2esw26kIPSourceGuardStaticMACAddress_Object((1,3,6,1,4,1,5205,2,54,3,1,2,2,1,5),_Gel2esw26kIPSourceGuardStaticMACAddress_Type())
gel2esw26kIPSourceGuardStaticMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardStaticMACAddress.setStatus(_A)
class _Gel2esw26kIPSourceGuardStaticRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw26kIPSourceGuardStaticRowStatus_Type.__name__=_C
_Gel2esw26kIPSourceGuardStaticRowStatus_Object=MibTableColumn
gel2esw26kIPSourceGuardStaticRowStatus=_Gel2esw26kIPSourceGuardStaticRowStatus_Object((1,3,6,1,4,1,5205,2,54,3,1,2,2,1,6),_Gel2esw26kIPSourceGuardStaticRowStatus_Type())
gel2esw26kIPSourceGuardStaticRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardStaticRowStatus.setStatus(_A)
_Gel2esw26kIPSourceGuardDynamicTable_Object=MibTable
gel2esw26kIPSourceGuardDynamicTable=_Gel2esw26kIPSourceGuardDynamicTable_Object((1,3,6,1,4,1,5205,2,54,3,1,3))
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardDynamicTable.setStatus(_A)
_Gel2esw26kIPSourceGuardDynamicEntry_Object=MibTableRow
gel2esw26kIPSourceGuardDynamicEntry=_Gel2esw26kIPSourceGuardDynamicEntry_Object((1,3,6,1,4,1,5205,2,54,3,1,3,1))
gel2esw26kIPSourceGuardDynamicEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardDynamicEntry.setStatus(_A)
class _Gel2esw26kIPSourceGuardDynamicIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kIPSourceGuardDynamicIndex_Type.__name__=_C
_Gel2esw26kIPSourceGuardDynamicIndex_Object=MibTableColumn
gel2esw26kIPSourceGuardDynamicIndex=_Gel2esw26kIPSourceGuardDynamicIndex_Object((1,3,6,1,4,1,5205,2,54,3,1,3,1,1),_Gel2esw26kIPSourceGuardDynamicIndex_Type())
gel2esw26kIPSourceGuardDynamicIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardDynamicIndex.setStatus(_A)
class _Gel2esw26kIPSourceGuardDynamicPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Gel2esw26kIPSourceGuardDynamicPort_Type.__name__=_C
_Gel2esw26kIPSourceGuardDynamicPort_Object=MibTableColumn
gel2esw26kIPSourceGuardDynamicPort=_Gel2esw26kIPSourceGuardDynamicPort_Object((1,3,6,1,4,1,5205,2,54,3,1,3,1,2),_Gel2esw26kIPSourceGuardDynamicPort_Type())
gel2esw26kIPSourceGuardDynamicPort.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardDynamicPort.setStatus(_A)
class _Gel2esw26kIPSourceGuardDynamicVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw26kIPSourceGuardDynamicVLANId_Type.__name__=_C
_Gel2esw26kIPSourceGuardDynamicVLANId_Object=MibTableColumn
gel2esw26kIPSourceGuardDynamicVLANId=_Gel2esw26kIPSourceGuardDynamicVLANId_Object((1,3,6,1,4,1,5205,2,54,3,1,3,1,3),_Gel2esw26kIPSourceGuardDynamicVLANId_Type())
gel2esw26kIPSourceGuardDynamicVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardDynamicVLANId.setStatus(_A)
_Gel2esw26kIPSourceGuardDynamicIPAddress_Type=IpAddress
_Gel2esw26kIPSourceGuardDynamicIPAddress_Object=MibTableColumn
gel2esw26kIPSourceGuardDynamicIPAddress=_Gel2esw26kIPSourceGuardDynamicIPAddress_Object((1,3,6,1,4,1,5205,2,54,3,1,3,1,4),_Gel2esw26kIPSourceGuardDynamicIPAddress_Type())
gel2esw26kIPSourceGuardDynamicIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardDynamicIPAddress.setStatus(_A)
_Gel2esw26kIPSourceGuardDynamicMACAddress_Type=MacAddress
_Gel2esw26kIPSourceGuardDynamicMACAddress_Object=MibTableColumn
gel2esw26kIPSourceGuardDynamicMACAddress=_Gel2esw26kIPSourceGuardDynamicMACAddress_Object((1,3,6,1,4,1,5205,2,54,3,1,3,1,5),_Gel2esw26kIPSourceGuardDynamicMACAddress_Type())
gel2esw26kIPSourceGuardDynamicMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kIPSourceGuardDynamicMACAddress.setStatus(_A)
_Gel2esw26kARPInspection_ObjectIdentity=ObjectIdentity
gel2esw26kARPInspection=_Gel2esw26kARPInspection_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,2))
_Gel2esw26kARPInspectionConf_ObjectIdentity=ObjectIdentity
gel2esw26kARPInspectionConf=_Gel2esw26kARPInspectionConf_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,2,1))
class _Gel2esw26kARPInspectionConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kARPInspectionConfMode_Type.__name__=_C
_Gel2esw26kARPInspectionConfMode_Object=MibScalar
gel2esw26kARPInspectionConfMode=_Gel2esw26kARPInspectionConfMode_Object((1,3,6,1,4,1,5205,2,54,3,2,1,1),_Gel2esw26kARPInspectionConfMode_Type())
gel2esw26kARPInspectionConfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kARPInspectionConfMode.setStatus(_A)
_Gel2esw26kARPInspectionConfTable_Object=MibTable
gel2esw26kARPInspectionConfTable=_Gel2esw26kARPInspectionConfTable_Object((1,3,6,1,4,1,5205,2,54,3,2,1,2))
if mibBuilder.loadTexts:gel2esw26kARPInspectionConfTable.setStatus(_A)
_Gel2esw26kARPInspectionConfEntry_Object=MibTableRow
gel2esw26kARPInspectionConfEntry=_Gel2esw26kARPInspectionConfEntry_Object((1,3,6,1,4,1,5205,2,54,3,2,1,2,1))
gel2esw26kARPInspectionConfEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:gel2esw26kARPInspectionConfEntry.setStatus(_A)
class _Gel2esw26kARPInspectionConfPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kARPInspectionConfPortIndex_Type.__name__=_C
_Gel2esw26kARPInspectionConfPortIndex_Object=MibTableColumn
gel2esw26kARPInspectionConfPortIndex=_Gel2esw26kARPInspectionConfPortIndex_Object((1,3,6,1,4,1,5205,2,54,3,2,1,2,1,1),_Gel2esw26kARPInspectionConfPortIndex_Type())
gel2esw26kARPInspectionConfPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kARPInspectionConfPortIndex.setStatus(_A)
class _Gel2esw26kARPInspectionConfPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kARPInspectionConfPortMode_Type.__name__=_C
_Gel2esw26kARPInspectionConfPortMode_Object=MibTableColumn
gel2esw26kARPInspectionConfPortMode=_Gel2esw26kARPInspectionConfPortMode_Object((1,3,6,1,4,1,5205,2,54,3,2,1,2,1,2),_Gel2esw26kARPInspectionConfPortMode_Type())
gel2esw26kARPInspectionConfPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kARPInspectionConfPortMode.setStatus(_A)
_Gel2esw26kARPInspectionStatic_ObjectIdentity=ObjectIdentity
gel2esw26kARPInspectionStatic=_Gel2esw26kARPInspectionStatic_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,2,2))
class _Gel2esw26kARPInspectionStaticCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kARPInspectionStaticCreate_Type.__name__=_C
_Gel2esw26kARPInspectionStaticCreate_Object=MibScalar
gel2esw26kARPInspectionStaticCreate=_Gel2esw26kARPInspectionStaticCreate_Object((1,3,6,1,4,1,5205,2,54,3,2,2,1),_Gel2esw26kARPInspectionStaticCreate_Type())
gel2esw26kARPInspectionStaticCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kARPInspectionStaticCreate.setStatus(_A)
_Gel2esw26kARPInspectionStaticTable_Object=MibTable
gel2esw26kARPInspectionStaticTable=_Gel2esw26kARPInspectionStaticTable_Object((1,3,6,1,4,1,5205,2,54,3,2,2,2))
if mibBuilder.loadTexts:gel2esw26kARPInspectionStaticTable.setStatus(_A)
_Gel2esw26kARPInspectionStaticEntry_Object=MibTableRow
gel2esw26kARPInspectionStaticEntry=_Gel2esw26kARPInspectionStaticEntry_Object((1,3,6,1,4,1,5205,2,54,3,2,2,2,1))
gel2esw26kARPInspectionStaticEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:gel2esw26kARPInspectionStaticEntry.setStatus(_A)
class _Gel2esw26kARPInspectionStaticIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kARPInspectionStaticIndex_Type.__name__=_C
_Gel2esw26kARPInspectionStaticIndex_Object=MibTableColumn
gel2esw26kARPInspectionStaticIndex=_Gel2esw26kARPInspectionStaticIndex_Object((1,3,6,1,4,1,5205,2,54,3,2,2,2,1,1),_Gel2esw26kARPInspectionStaticIndex_Type())
gel2esw26kARPInspectionStaticIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kARPInspectionStaticIndex.setStatus(_A)
class _Gel2esw26kARPInspectionStaticPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kARPInspectionStaticPort_Type.__name__=_C
_Gel2esw26kARPInspectionStaticPort_Object=MibTableColumn
gel2esw26kARPInspectionStaticPort=_Gel2esw26kARPInspectionStaticPort_Object((1,3,6,1,4,1,5205,2,54,3,2,2,2,1,2),_Gel2esw26kARPInspectionStaticPort_Type())
gel2esw26kARPInspectionStaticPort.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kARPInspectionStaticPort.setStatus(_A)
class _Gel2esw26kARPInspectionStaticVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw26kARPInspectionStaticVLANId_Type.__name__=_C
_Gel2esw26kARPInspectionStaticVLANId_Object=MibTableColumn
gel2esw26kARPInspectionStaticVLANId=_Gel2esw26kARPInspectionStaticVLANId_Object((1,3,6,1,4,1,5205,2,54,3,2,2,2,1,3),_Gel2esw26kARPInspectionStaticVLANId_Type())
gel2esw26kARPInspectionStaticVLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kARPInspectionStaticVLANId.setStatus(_A)
_Gel2esw26kARPInspectionStaticIPAddress_Type=IpAddress
_Gel2esw26kARPInspectionStaticIPAddress_Object=MibTableColumn
gel2esw26kARPInspectionStaticIPAddress=_Gel2esw26kARPInspectionStaticIPAddress_Object((1,3,6,1,4,1,5205,2,54,3,2,2,2,1,4),_Gel2esw26kARPInspectionStaticIPAddress_Type())
gel2esw26kARPInspectionStaticIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kARPInspectionStaticIPAddress.setStatus(_A)
_Gel2esw26kARPInspectionStaticMACAddress_Type=MacAddress
_Gel2esw26kARPInspectionStaticMACAddress_Object=MibTableColumn
gel2esw26kARPInspectionStaticMACAddress=_Gel2esw26kARPInspectionStaticMACAddress_Object((1,3,6,1,4,1,5205,2,54,3,2,2,2,1,5),_Gel2esw26kARPInspectionStaticMACAddress_Type())
gel2esw26kARPInspectionStaticMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kARPInspectionStaticMACAddress.setStatus(_A)
class _Gel2esw26kARPInspectionStaticRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw26kARPInspectionStaticRowStatus_Type.__name__=_C
_Gel2esw26kARPInspectionStaticRowStatus_Object=MibTableColumn
gel2esw26kARPInspectionStaticRowStatus=_Gel2esw26kARPInspectionStaticRowStatus_Object((1,3,6,1,4,1,5205,2,54,3,2,2,2,1,6),_Gel2esw26kARPInspectionStaticRowStatus_Type())
gel2esw26kARPInspectionStaticRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kARPInspectionStaticRowStatus.setStatus(_A)
_Gel2esw26kARPInspectionDynamicTable_Object=MibTable
gel2esw26kARPInspectionDynamicTable=_Gel2esw26kARPInspectionDynamicTable_Object((1,3,6,1,4,1,5205,2,54,3,2,3))
if mibBuilder.loadTexts:gel2esw26kARPInspectionDynamicTable.setStatus(_A)
_Gel2esw26kARPInspectionDynamicEntry_Object=MibTableRow
gel2esw26kARPInspectionDynamicEntry=_Gel2esw26kARPInspectionDynamicEntry_Object((1,3,6,1,4,1,5205,2,54,3,2,3,1))
gel2esw26kARPInspectionDynamicEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:gel2esw26kARPInspectionDynamicEntry.setStatus(_A)
class _Gel2esw26kARPInspectionDynamicIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kARPInspectionDynamicIndex_Type.__name__=_C
_Gel2esw26kARPInspectionDynamicIndex_Object=MibTableColumn
gel2esw26kARPInspectionDynamicIndex=_Gel2esw26kARPInspectionDynamicIndex_Object((1,3,6,1,4,1,5205,2,54,3,2,3,1,1),_Gel2esw26kARPInspectionDynamicIndex_Type())
gel2esw26kARPInspectionDynamicIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kARPInspectionDynamicIndex.setStatus(_A)
class _Gel2esw26kARPInspectionDynamicPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kARPInspectionDynamicPort_Type.__name__=_C
_Gel2esw26kARPInspectionDynamicPort_Object=MibTableColumn
gel2esw26kARPInspectionDynamicPort=_Gel2esw26kARPInspectionDynamicPort_Object((1,3,6,1,4,1,5205,2,54,3,2,3,1,2),_Gel2esw26kARPInspectionDynamicPort_Type())
gel2esw26kARPInspectionDynamicPort.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kARPInspectionDynamicPort.setStatus(_A)
class _Gel2esw26kARPInspectionDynamicVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw26kARPInspectionDynamicVLANId_Type.__name__=_C
_Gel2esw26kARPInspectionDynamicVLANId_Object=MibTableColumn
gel2esw26kARPInspectionDynamicVLANId=_Gel2esw26kARPInspectionDynamicVLANId_Object((1,3,6,1,4,1,5205,2,54,3,2,3,1,3),_Gel2esw26kARPInspectionDynamicVLANId_Type())
gel2esw26kARPInspectionDynamicVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kARPInspectionDynamicVLANId.setStatus(_A)
_Gel2esw26kARPInspectionDynamicIPAddress_Type=IpAddress
_Gel2esw26kARPInspectionDynamicIPAddress_Object=MibTableColumn
gel2esw26kARPInspectionDynamicIPAddress=_Gel2esw26kARPInspectionDynamicIPAddress_Object((1,3,6,1,4,1,5205,2,54,3,2,3,1,4),_Gel2esw26kARPInspectionDynamicIPAddress_Type())
gel2esw26kARPInspectionDynamicIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kARPInspectionDynamicIPAddress.setStatus(_A)
_Gel2esw26kARPInspectionDynamicMACAddress_Type=MacAddress
_Gel2esw26kARPInspectionDynamicMACAddress_Object=MibTableColumn
gel2esw26kARPInspectionDynamicMACAddress=_Gel2esw26kARPInspectionDynamicMACAddress_Object((1,3,6,1,4,1,5205,2,54,3,2,3,1,5),_Gel2esw26kARPInspectionDynamicMACAddress_Type())
gel2esw26kARPInspectionDynamicMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kARPInspectionDynamicMACAddress.setStatus(_A)
_Gel2esw26kDHCPSnooping_ObjectIdentity=ObjectIdentity
gel2esw26kDHCPSnooping=_Gel2esw26kDHCPSnooping_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,3))
_Gel2esw26kDHCPSnoopingConf_ObjectIdentity=ObjectIdentity
gel2esw26kDHCPSnoopingConf=_Gel2esw26kDHCPSnoopingConf_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,3,1))
class _Gel2esw26kDHCPSnoopingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kDHCPSnoopingMode_Type.__name__=_C
_Gel2esw26kDHCPSnoopingMode_Object=MibScalar
gel2esw26kDHCPSnoopingMode=_Gel2esw26kDHCPSnoopingMode_Object((1,3,6,1,4,1,5205,2,54,3,3,1,1),_Gel2esw26kDHCPSnoopingMode_Type())
gel2esw26kDHCPSnoopingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingMode.setStatus(_A)
_Gel2esw26kDHCPSnoopingPortModeConfigurationTable_Object=MibTable
gel2esw26kDHCPSnoopingPortModeConfigurationTable=_Gel2esw26kDHCPSnoopingPortModeConfigurationTable_Object((1,3,6,1,4,1,5205,2,54,3,3,1,2))
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingPortModeConfigurationTable.setStatus(_A)
_Gel2esw26kDHCPSnoopingPortModeConfigurationEntry_Object=MibTableRow
gel2esw26kDHCPSnoopingPortModeConfigurationEntry=_Gel2esw26kDHCPSnoopingPortModeConfigurationEntry_Object((1,3,6,1,4,1,5205,2,54,3,3,1,2,1))
gel2esw26kDHCPSnoopingPortModeConfigurationEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingPortModeConfigurationEntry.setStatus(_A)
class _Gel2esw26kDHCPSnoopingPortModeConfigurationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kDHCPSnoopingPortModeConfigurationPort_Type.__name__=_C
_Gel2esw26kDHCPSnoopingPortModeConfigurationPort_Object=MibTableColumn
gel2esw26kDHCPSnoopingPortModeConfigurationPort=_Gel2esw26kDHCPSnoopingPortModeConfigurationPort_Object((1,3,6,1,4,1,5205,2,54,3,3,1,2,1,1),_Gel2esw26kDHCPSnoopingPortModeConfigurationPort_Type())
gel2esw26kDHCPSnoopingPortModeConfigurationPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingPortModeConfigurationPort.setStatus(_A)
class _Gel2esw26kDHCPSnoopingPortModeConfigurationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kDHCPSnoopingPortModeConfigurationMode_Type.__name__=_C
_Gel2esw26kDHCPSnoopingPortModeConfigurationMode_Object=MibTableColumn
gel2esw26kDHCPSnoopingPortModeConfigurationMode=_Gel2esw26kDHCPSnoopingPortModeConfigurationMode_Object((1,3,6,1,4,1,5205,2,54,3,3,1,2,1,2),_Gel2esw26kDHCPSnoopingPortModeConfigurationMode_Type())
gel2esw26kDHCPSnoopingPortModeConfigurationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingPortModeConfigurationMode.setStatus(_A)
_Gel2esw26kDHCPSnoopingStatisticsTable_Object=MibTable
gel2esw26kDHCPSnoopingStatisticsTable=_Gel2esw26kDHCPSnoopingStatisticsTable_Object((1,3,6,1,4,1,5205,2,54,3,3,2))
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingStatisticsTable.setStatus(_A)
_Gel2esw26kDHCPSnoopingStatisticsEntry_Object=MibTableRow
gel2esw26kDHCPSnoopingStatisticsEntry=_Gel2esw26kDHCPSnoopingStatisticsEntry_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1))
gel2esw26kDHCPSnoopingStatisticsEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingStatisticsEntry.setStatus(_A)
class _Gel2esw26kDHCPSnoopingStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kDHCPSnoopingStatisticsPort_Type.__name__=_C
_Gel2esw26kDHCPSnoopingStatisticsPort_Object=MibTableColumn
gel2esw26kDHCPSnoopingStatisticsPort=_Gel2esw26kDHCPSnoopingStatisticsPort_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,1),_Gel2esw26kDHCPSnoopingStatisticsPort_Type())
gel2esw26kDHCPSnoopingStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingStatisticsPort.setStatus(_A)
class _Gel2esw26kDHCPSnoopingStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kDHCPSnoopingStatisticsClear_Type.__name__=_C
_Gel2esw26kDHCPSnoopingStatisticsClear_Object=MibTableColumn
gel2esw26kDHCPSnoopingStatisticsClear=_Gel2esw26kDHCPSnoopingStatisticsClear_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,2),_Gel2esw26kDHCPSnoopingStatisticsClear_Type())
gel2esw26kDHCPSnoopingStatisticsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingStatisticsClear.setStatus(_A)
_Gel2esw26kDHCPSnoopingRxDiscover_Type=Counter32
_Gel2esw26kDHCPSnoopingRxDiscover_Object=MibTableColumn
gel2esw26kDHCPSnoopingRxDiscover=_Gel2esw26kDHCPSnoopingRxDiscover_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,3),_Gel2esw26kDHCPSnoopingRxDiscover_Type())
gel2esw26kDHCPSnoopingRxDiscover.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingRxDiscover.setStatus(_A)
_Gel2esw26kDHCPSnoopingRxOffer_Type=Counter32
_Gel2esw26kDHCPSnoopingRxOffer_Object=MibTableColumn
gel2esw26kDHCPSnoopingRxOffer=_Gel2esw26kDHCPSnoopingRxOffer_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,4),_Gel2esw26kDHCPSnoopingRxOffer_Type())
gel2esw26kDHCPSnoopingRxOffer.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingRxOffer.setStatus(_A)
_Gel2esw26kDHCPSnoopingRxRequest_Type=Counter32
_Gel2esw26kDHCPSnoopingRxRequest_Object=MibTableColumn
gel2esw26kDHCPSnoopingRxRequest=_Gel2esw26kDHCPSnoopingRxRequest_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,5),_Gel2esw26kDHCPSnoopingRxRequest_Type())
gel2esw26kDHCPSnoopingRxRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingRxRequest.setStatus(_A)
_Gel2esw26kDHCPSnoopingRxDecline_Type=Counter32
_Gel2esw26kDHCPSnoopingRxDecline_Object=MibTableColumn
gel2esw26kDHCPSnoopingRxDecline=_Gel2esw26kDHCPSnoopingRxDecline_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,6),_Gel2esw26kDHCPSnoopingRxDecline_Type())
gel2esw26kDHCPSnoopingRxDecline.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingRxDecline.setStatus(_A)
_Gel2esw26kDHCPSnoopingRxACK_Type=Counter32
_Gel2esw26kDHCPSnoopingRxACK_Object=MibTableColumn
gel2esw26kDHCPSnoopingRxACK=_Gel2esw26kDHCPSnoopingRxACK_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,7),_Gel2esw26kDHCPSnoopingRxACK_Type())
gel2esw26kDHCPSnoopingRxACK.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingRxACK.setStatus(_A)
_Gel2esw26kDHCPSnoopingRxNAK_Type=Counter32
_Gel2esw26kDHCPSnoopingRxNAK_Object=MibTableColumn
gel2esw26kDHCPSnoopingRxNAK=_Gel2esw26kDHCPSnoopingRxNAK_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,8),_Gel2esw26kDHCPSnoopingRxNAK_Type())
gel2esw26kDHCPSnoopingRxNAK.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingRxNAK.setStatus(_A)
_Gel2esw26kDHCPSnoopingRxRelease_Type=Counter32
_Gel2esw26kDHCPSnoopingRxRelease_Object=MibTableColumn
gel2esw26kDHCPSnoopingRxRelease=_Gel2esw26kDHCPSnoopingRxRelease_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,9),_Gel2esw26kDHCPSnoopingRxRelease_Type())
gel2esw26kDHCPSnoopingRxRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingRxRelease.setStatus(_A)
_Gel2esw26kDHCPSnoopingRxInform_Type=Counter32
_Gel2esw26kDHCPSnoopingRxInform_Object=MibTableColumn
gel2esw26kDHCPSnoopingRxInform=_Gel2esw26kDHCPSnoopingRxInform_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,10),_Gel2esw26kDHCPSnoopingRxInform_Type())
gel2esw26kDHCPSnoopingRxInform.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingRxInform.setStatus(_A)
_Gel2esw26kDHCPSnoopingRxLeaseQuery_Type=Counter32
_Gel2esw26kDHCPSnoopingRxLeaseQuery_Object=MibTableColumn
gel2esw26kDHCPSnoopingRxLeaseQuery=_Gel2esw26kDHCPSnoopingRxLeaseQuery_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,11),_Gel2esw26kDHCPSnoopingRxLeaseQuery_Type())
gel2esw26kDHCPSnoopingRxLeaseQuery.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingRxLeaseQuery.setStatus(_A)
_Gel2esw26kDHCPSnoopingRxLeaseUnassigned_Type=Counter32
_Gel2esw26kDHCPSnoopingRxLeaseUnassigned_Object=MibTableColumn
gel2esw26kDHCPSnoopingRxLeaseUnassigned=_Gel2esw26kDHCPSnoopingRxLeaseUnassigned_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,12),_Gel2esw26kDHCPSnoopingRxLeaseUnassigned_Type())
gel2esw26kDHCPSnoopingRxLeaseUnassigned.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingRxLeaseUnassigned.setStatus(_A)
_Gel2esw26kDHCPSnoopingRxLeaseUnknown_Type=Counter32
_Gel2esw26kDHCPSnoopingRxLeaseUnknown_Object=MibTableColumn
gel2esw26kDHCPSnoopingRxLeaseUnknown=_Gel2esw26kDHCPSnoopingRxLeaseUnknown_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,13),_Gel2esw26kDHCPSnoopingRxLeaseUnknown_Type())
gel2esw26kDHCPSnoopingRxLeaseUnknown.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingRxLeaseUnknown.setStatus(_A)
_Gel2esw26kDHCPSnoopingRxLeaseActive_Type=Counter32
_Gel2esw26kDHCPSnoopingRxLeaseActive_Object=MibTableColumn
gel2esw26kDHCPSnoopingRxLeaseActive=_Gel2esw26kDHCPSnoopingRxLeaseActive_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,14),_Gel2esw26kDHCPSnoopingRxLeaseActive_Type())
gel2esw26kDHCPSnoopingRxLeaseActive.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingRxLeaseActive.setStatus(_A)
_Gel2esw26kDHCPSnoopingTxDiscover_Type=Counter32
_Gel2esw26kDHCPSnoopingTxDiscover_Object=MibTableColumn
gel2esw26kDHCPSnoopingTxDiscover=_Gel2esw26kDHCPSnoopingTxDiscover_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,15),_Gel2esw26kDHCPSnoopingTxDiscover_Type())
gel2esw26kDHCPSnoopingTxDiscover.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingTxDiscover.setStatus(_A)
_Gel2esw26kDHCPSnoopingTxOffer_Type=Counter32
_Gel2esw26kDHCPSnoopingTxOffer_Object=MibTableColumn
gel2esw26kDHCPSnoopingTxOffer=_Gel2esw26kDHCPSnoopingTxOffer_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,16),_Gel2esw26kDHCPSnoopingTxOffer_Type())
gel2esw26kDHCPSnoopingTxOffer.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingTxOffer.setStatus(_A)
_Gel2esw26kDHCPSnoopingTxRequest_Type=Counter32
_Gel2esw26kDHCPSnoopingTxRequest_Object=MibTableColumn
gel2esw26kDHCPSnoopingTxRequest=_Gel2esw26kDHCPSnoopingTxRequest_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,17),_Gel2esw26kDHCPSnoopingTxRequest_Type())
gel2esw26kDHCPSnoopingTxRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingTxRequest.setStatus(_A)
_Gel2esw26kDHCPSnoopingTxDecline_Type=Counter32
_Gel2esw26kDHCPSnoopingTxDecline_Object=MibTableColumn
gel2esw26kDHCPSnoopingTxDecline=_Gel2esw26kDHCPSnoopingTxDecline_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,18),_Gel2esw26kDHCPSnoopingTxDecline_Type())
gel2esw26kDHCPSnoopingTxDecline.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingTxDecline.setStatus(_A)
_Gel2esw26kDHCPSnoopingTxACK_Type=Counter32
_Gel2esw26kDHCPSnoopingTxACK_Object=MibTableColumn
gel2esw26kDHCPSnoopingTxACK=_Gel2esw26kDHCPSnoopingTxACK_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,19),_Gel2esw26kDHCPSnoopingTxACK_Type())
gel2esw26kDHCPSnoopingTxACK.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingTxACK.setStatus(_A)
_Gel2esw26kDHCPSnoopingTxNAK_Type=Counter32
_Gel2esw26kDHCPSnoopingTxNAK_Object=MibTableColumn
gel2esw26kDHCPSnoopingTxNAK=_Gel2esw26kDHCPSnoopingTxNAK_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,20),_Gel2esw26kDHCPSnoopingTxNAK_Type())
gel2esw26kDHCPSnoopingTxNAK.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingTxNAK.setStatus(_A)
_Gel2esw26kDHCPSnoopingTxRelease_Type=Counter32
_Gel2esw26kDHCPSnoopingTxRelease_Object=MibTableColumn
gel2esw26kDHCPSnoopingTxRelease=_Gel2esw26kDHCPSnoopingTxRelease_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,21),_Gel2esw26kDHCPSnoopingTxRelease_Type())
gel2esw26kDHCPSnoopingTxRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingTxRelease.setStatus(_A)
_Gel2esw26kDHCPSnoopingTxInform_Type=Counter32
_Gel2esw26kDHCPSnoopingTxInform_Object=MibTableColumn
gel2esw26kDHCPSnoopingTxInform=_Gel2esw26kDHCPSnoopingTxInform_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,22),_Gel2esw26kDHCPSnoopingTxInform_Type())
gel2esw26kDHCPSnoopingTxInform.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingTxInform.setStatus(_A)
_Gel2esw26kDHCPSnoopingTxLeaseQuery_Type=Counter32
_Gel2esw26kDHCPSnoopingTxLeaseQuery_Object=MibTableColumn
gel2esw26kDHCPSnoopingTxLeaseQuery=_Gel2esw26kDHCPSnoopingTxLeaseQuery_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,23),_Gel2esw26kDHCPSnoopingTxLeaseQuery_Type())
gel2esw26kDHCPSnoopingTxLeaseQuery.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingTxLeaseQuery.setStatus(_A)
_Gel2esw26kDHCPSnoopingTxLeaseUnassigned_Type=Counter32
_Gel2esw26kDHCPSnoopingTxLeaseUnassigned_Object=MibTableColumn
gel2esw26kDHCPSnoopingTxLeaseUnassigned=_Gel2esw26kDHCPSnoopingTxLeaseUnassigned_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,24),_Gel2esw26kDHCPSnoopingTxLeaseUnassigned_Type())
gel2esw26kDHCPSnoopingTxLeaseUnassigned.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingTxLeaseUnassigned.setStatus(_A)
_Gel2esw26kDHCPSnoopingTxLeaseUnknown_Type=Counter32
_Gel2esw26kDHCPSnoopingTxLeaseUnknown_Object=MibTableColumn
gel2esw26kDHCPSnoopingTxLeaseUnknown=_Gel2esw26kDHCPSnoopingTxLeaseUnknown_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,25),_Gel2esw26kDHCPSnoopingTxLeaseUnknown_Type())
gel2esw26kDHCPSnoopingTxLeaseUnknown.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingTxLeaseUnknown.setStatus(_A)
_Gel2esw26kDHCPSnoopingTxLeaseActive_Type=Counter32
_Gel2esw26kDHCPSnoopingTxLeaseActive_Object=MibTableColumn
gel2esw26kDHCPSnoopingTxLeaseActive=_Gel2esw26kDHCPSnoopingTxLeaseActive_Object((1,3,6,1,4,1,5205,2,54,3,3,2,1,26),_Gel2esw26kDHCPSnoopingTxLeaseActive_Type())
gel2esw26kDHCPSnoopingTxLeaseActive.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kDHCPSnoopingTxLeaseActive.setStatus(_A)
_Gel2esw26kDHCPRelay_ObjectIdentity=ObjectIdentity
gel2esw26kDHCPRelay=_Gel2esw26kDHCPRelay_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,4))
_Gel2esw26kDHCPRelayConfiguration_ObjectIdentity=ObjectIdentity
gel2esw26kDHCPRelayConfiguration=_Gel2esw26kDHCPRelayConfiguration_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,4,1))
class _Gel2esw26kDHCPRelayMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kDHCPRelayMode_Type.__name__=_C
_Gel2esw26kDHCPRelayMode_Object=MibScalar
gel2esw26kDHCPRelayMode=_Gel2esw26kDHCPRelayMode_Object((1,3,6,1,4,1,5205,2,54,3,4,1,1),_Gel2esw26kDHCPRelayMode_Type())
gel2esw26kDHCPRelayMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kDHCPRelayMode.setStatus(_A)
_Gel2esw26kDHCPRelayServer_Type=IpAddress
_Gel2esw26kDHCPRelayServer_Object=MibScalar
gel2esw26kDHCPRelayServer=_Gel2esw26kDHCPRelayServer_Object((1,3,6,1,4,1,5205,2,54,3,4,1,2),_Gel2esw26kDHCPRelayServer_Type())
gel2esw26kDHCPRelayServer.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kDHCPRelayServer.setStatus(_A)
class _Gel2esw26kDHCPRelayInformationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kDHCPRelayInformationMode_Type.__name__=_C
_Gel2esw26kDHCPRelayInformationMode_Object=MibScalar
gel2esw26kDHCPRelayInformationMode=_Gel2esw26kDHCPRelayInformationMode_Object((1,3,6,1,4,1,5205,2,54,3,4,1,3),_Gel2esw26kDHCPRelayInformationMode_Type())
gel2esw26kDHCPRelayInformationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kDHCPRelayInformationMode.setStatus(_A)
class _Gel2esw26kDHCPRelayInformationPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Gel2esw26kDHCPRelayInformationPolicy_Type.__name__=_C
_Gel2esw26kDHCPRelayInformationPolicy_Object=MibScalar
gel2esw26kDHCPRelayInformationPolicy=_Gel2esw26kDHCPRelayInformationPolicy_Object((1,3,6,1,4,1,5205,2,54,3,4,1,4),_Gel2esw26kDHCPRelayInformationPolicy_Type())
gel2esw26kDHCPRelayInformationPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kDHCPRelayInformationPolicy.setStatus(_A)
_Gel2esw26kDHCPRelayStatistics_ObjectIdentity=ObjectIdentity
gel2esw26kDHCPRelayStatistics=_Gel2esw26kDHCPRelayStatistics_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,4,2))
_Gel2esw26kDHCPRelayServerStatistics_ObjectIdentity=ObjectIdentity
gel2esw26kDHCPRelayServerStatistics=_Gel2esw26kDHCPRelayServerStatistics_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,4,2,1))
_Gel2esw26kServerStatTransmitToServer_Type=Counter32
_Gel2esw26kServerStatTransmitToServer_Object=MibScalar
gel2esw26kServerStatTransmitToServer=_Gel2esw26kServerStatTransmitToServer_Object((1,3,6,1,4,1,5205,2,54,3,4,2,1,1),_Gel2esw26kServerStatTransmitToServer_Type())
gel2esw26kServerStatTransmitToServer.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kServerStatTransmitToServer.setStatus(_A)
_Gel2esw26kServerStatTransmitError_Type=Counter32
_Gel2esw26kServerStatTransmitError_Object=MibScalar
gel2esw26kServerStatTransmitError=_Gel2esw26kServerStatTransmitError_Object((1,3,6,1,4,1,5205,2,54,3,4,2,1,2),_Gel2esw26kServerStatTransmitError_Type())
gel2esw26kServerStatTransmitError.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kServerStatTransmitError.setStatus(_A)
_Gel2esw26kServerStatReceiveFromServer_Type=Counter32
_Gel2esw26kServerStatReceiveFromServer_Object=MibScalar
gel2esw26kServerStatReceiveFromServer=_Gel2esw26kServerStatReceiveFromServer_Object((1,3,6,1,4,1,5205,2,54,3,4,2,1,3),_Gel2esw26kServerStatReceiveFromServer_Type())
gel2esw26kServerStatReceiveFromServer.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kServerStatReceiveFromServer.setStatus(_A)
_Gel2esw26kServerStatReceiveMissingAgentOption_Type=Counter32
_Gel2esw26kServerStatReceiveMissingAgentOption_Object=MibScalar
gel2esw26kServerStatReceiveMissingAgentOption=_Gel2esw26kServerStatReceiveMissingAgentOption_Object((1,3,6,1,4,1,5205,2,54,3,4,2,1,4),_Gel2esw26kServerStatReceiveMissingAgentOption_Type())
gel2esw26kServerStatReceiveMissingAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kServerStatReceiveMissingAgentOption.setStatus(_A)
_Gel2esw26kServerStatReceiveMissingCircuitID_Type=Counter32
_Gel2esw26kServerStatReceiveMissingCircuitID_Object=MibScalar
gel2esw26kServerStatReceiveMissingCircuitID=_Gel2esw26kServerStatReceiveMissingCircuitID_Object((1,3,6,1,4,1,5205,2,54,3,4,2,1,5),_Gel2esw26kServerStatReceiveMissingCircuitID_Type())
gel2esw26kServerStatReceiveMissingCircuitID.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kServerStatReceiveMissingCircuitID.setStatus(_A)
_Gel2esw26kServerStatReceiveMissingRemoteID_Type=Counter32
_Gel2esw26kServerStatReceiveMissingRemoteID_Object=MibScalar
gel2esw26kServerStatReceiveMissingRemoteID=_Gel2esw26kServerStatReceiveMissingRemoteID_Object((1,3,6,1,4,1,5205,2,54,3,4,2,1,6),_Gel2esw26kServerStatReceiveMissingRemoteID_Type())
gel2esw26kServerStatReceiveMissingRemoteID.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kServerStatReceiveMissingRemoteID.setStatus(_A)
_Gel2esw26kServerStatReceiveBadCircuitID_Type=Counter32
_Gel2esw26kServerStatReceiveBadCircuitID_Object=MibScalar
gel2esw26kServerStatReceiveBadCircuitID=_Gel2esw26kServerStatReceiveBadCircuitID_Object((1,3,6,1,4,1,5205,2,54,3,4,2,1,7),_Gel2esw26kServerStatReceiveBadCircuitID_Type())
gel2esw26kServerStatReceiveBadCircuitID.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kServerStatReceiveBadCircuitID.setStatus(_A)
_Gel2esw26kServerStatReceiveBadRemoteID_Type=Counter32
_Gel2esw26kServerStatReceiveBadRemoteID_Object=MibScalar
gel2esw26kServerStatReceiveBadRemoteID=_Gel2esw26kServerStatReceiveBadRemoteID_Object((1,3,6,1,4,1,5205,2,54,3,4,2,1,8),_Gel2esw26kServerStatReceiveBadRemoteID_Type())
gel2esw26kServerStatReceiveBadRemoteID.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kServerStatReceiveBadRemoteID.setStatus(_A)
_Gel2esw26kDHCPRelayClientStatistics_ObjectIdentity=ObjectIdentity
gel2esw26kDHCPRelayClientStatistics=_Gel2esw26kDHCPRelayClientStatistics_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,4,2,2))
_Gel2esw26kClientStatTransmitToClient_Type=Counter32
_Gel2esw26kClientStatTransmitToClient_Object=MibScalar
gel2esw26kClientStatTransmitToClient=_Gel2esw26kClientStatTransmitToClient_Object((1,3,6,1,4,1,5205,2,54,3,4,2,2,1),_Gel2esw26kClientStatTransmitToClient_Type())
gel2esw26kClientStatTransmitToClient.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kClientStatTransmitToClient.setStatus(_A)
_Gel2esw26kClientStatTransmitError_Type=Counter32
_Gel2esw26kClientStatTransmitError_Object=MibScalar
gel2esw26kClientStatTransmitError=_Gel2esw26kClientStatTransmitError_Object((1,3,6,1,4,1,5205,2,54,3,4,2,2,2),_Gel2esw26kClientStatTransmitError_Type())
gel2esw26kClientStatTransmitError.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kClientStatTransmitError.setStatus(_A)
_Gel2esw26kClientStatReceivefromClient_Type=Counter32
_Gel2esw26kClientStatReceivefromClient_Object=MibScalar
gel2esw26kClientStatReceivefromClient=_Gel2esw26kClientStatReceivefromClient_Object((1,3,6,1,4,1,5205,2,54,3,4,2,2,3),_Gel2esw26kClientStatReceivefromClient_Type())
gel2esw26kClientStatReceivefromClient.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kClientStatReceivefromClient.setStatus(_A)
_Gel2esw26kClientStatReceiveAgentOption_Type=Counter32
_Gel2esw26kClientStatReceiveAgentOption_Object=MibScalar
gel2esw26kClientStatReceiveAgentOption=_Gel2esw26kClientStatReceiveAgentOption_Object((1,3,6,1,4,1,5205,2,54,3,4,2,2,4),_Gel2esw26kClientStatReceiveAgentOption_Type())
gel2esw26kClientStatReceiveAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kClientStatReceiveAgentOption.setStatus(_A)
_Gel2esw26kClientStatReplaceAgentOption_Type=Counter32
_Gel2esw26kClientStatReplaceAgentOption_Object=MibScalar
gel2esw26kClientStatReplaceAgentOption=_Gel2esw26kClientStatReplaceAgentOption_Object((1,3,6,1,4,1,5205,2,54,3,4,2,2,5),_Gel2esw26kClientStatReplaceAgentOption_Type())
gel2esw26kClientStatReplaceAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kClientStatReplaceAgentOption.setStatus(_A)
_Gel2esw26kClientStatKeepAgentOption_Type=Counter32
_Gel2esw26kClientStatKeepAgentOption_Object=MibScalar
gel2esw26kClientStatKeepAgentOption=_Gel2esw26kClientStatKeepAgentOption_Object((1,3,6,1,4,1,5205,2,54,3,4,2,2,6),_Gel2esw26kClientStatKeepAgentOption_Type())
gel2esw26kClientStatKeepAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kClientStatKeepAgentOption.setStatus(_A)
_Gel2esw26kClientStatDropAgentOption_Type=Counter32
_Gel2esw26kClientStatDropAgentOption_Object=MibScalar
gel2esw26kClientStatDropAgentOption=_Gel2esw26kClientStatDropAgentOption_Object((1,3,6,1,4,1,5205,2,54,3,4,2,2,7),_Gel2esw26kClientStatDropAgentOption_Type())
gel2esw26kClientStatDropAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kClientStatDropAgentOption.setStatus(_A)
_Gel2esw26kPortSecurity_ObjectIdentity=ObjectIdentity
gel2esw26kPortSecurity=_Gel2esw26kPortSecurity_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,5))
_Gel2esw26kPortSecLimitCtrl_ObjectIdentity=ObjectIdentity
gel2esw26kPortSecLimitCtrl=_Gel2esw26kPortSecLimitCtrl_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,5,1))
_Gel2esw26kPortSecLimitCtrlSystemConf_ObjectIdentity=ObjectIdentity
gel2esw26kPortSecLimitCtrlSystemConf=_Gel2esw26kPortSecLimitCtrlSystemConf_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,5,1,1))
class _Gel2esw26kPortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortSecurityMode_Type.__name__=_C
_Gel2esw26kPortSecurityMode_Object=MibScalar
gel2esw26kPortSecurityMode=_Gel2esw26kPortSecurityMode_Object((1,3,6,1,4,1,5205,2,54,3,5,1,1,1),_Gel2esw26kPortSecurityMode_Type())
gel2esw26kPortSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortSecurityMode.setStatus(_A)
class _Gel2esw26kPortSecurityAging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortSecurityAging_Type.__name__=_C
_Gel2esw26kPortSecurityAging_Object=MibScalar
gel2esw26kPortSecurityAging=_Gel2esw26kPortSecurityAging_Object((1,3,6,1,4,1,5205,2,54,3,5,1,1,2),_Gel2esw26kPortSecurityAging_Type())
gel2esw26kPortSecurityAging.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortSecurityAging.setStatus(_A)
class _Gel2esw26kPortSecurityAgingPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10000000))
_Gel2esw26kPortSecurityAgingPeriod_Type.__name__=_C
_Gel2esw26kPortSecurityAgingPeriod_Object=MibScalar
gel2esw26kPortSecurityAgingPeriod=_Gel2esw26kPortSecurityAgingPeriod_Object((1,3,6,1,4,1,5205,2,54,3,5,1,1,3),_Gel2esw26kPortSecurityAgingPeriod_Type())
gel2esw26kPortSecurityAgingPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortSecurityAgingPeriod.setStatus(_A)
_Gel2esw26kPortSecLimitCtrlTable_Object=MibTable
gel2esw26kPortSecLimitCtrlTable=_Gel2esw26kPortSecLimitCtrlTable_Object((1,3,6,1,4,1,5205,2,54,3,5,1,2))
if mibBuilder.loadTexts:gel2esw26kPortSecLimitCtrlTable.setStatus(_A)
_Gel2esw26kPortSecLimitCtrlEntry_Object=MibTableRow
gel2esw26kPortSecLimitCtrlEntry=_Gel2esw26kPortSecLimitCtrlEntry_Object((1,3,6,1,4,1,5205,2,54,3,5,1,2,1))
gel2esw26kPortSecLimitCtrlEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:gel2esw26kPortSecLimitCtrlEntry.setStatus(_A)
class _Gel2esw26kPortSecLimitCtrlPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kPortSecLimitCtrlPort_Type.__name__=_C
_Gel2esw26kPortSecLimitCtrlPort_Object=MibTableColumn
gel2esw26kPortSecLimitCtrlPort=_Gel2esw26kPortSecLimitCtrlPort_Object((1,3,6,1,4,1,5205,2,54,3,5,1,2,1,1),_Gel2esw26kPortSecLimitCtrlPort_Type())
gel2esw26kPortSecLimitCtrlPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kPortSecLimitCtrlPort.setStatus(_A)
class _Gel2esw26kPortSecLimitCtrlPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortSecLimitCtrlPortMode_Type.__name__=_C
_Gel2esw26kPortSecLimitCtrlPortMode_Object=MibTableColumn
gel2esw26kPortSecLimitCtrlPortMode=_Gel2esw26kPortSecLimitCtrlPortMode_Object((1,3,6,1,4,1,5205,2,54,3,5,1,2,1,2),_Gel2esw26kPortSecLimitCtrlPortMode_Type())
gel2esw26kPortSecLimitCtrlPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortSecLimitCtrlPortMode.setStatus(_A)
class _Gel2esw26kPortSecLimitCtrlPortLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Gel2esw26kPortSecLimitCtrlPortLimit_Type.__name__=_C
_Gel2esw26kPortSecLimitCtrlPortLimit_Object=MibTableColumn
gel2esw26kPortSecLimitCtrlPortLimit=_Gel2esw26kPortSecLimitCtrlPortLimit_Object((1,3,6,1,4,1,5205,2,54,3,5,1,2,1,3),_Gel2esw26kPortSecLimitCtrlPortLimit_Type())
gel2esw26kPortSecLimitCtrlPortLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortSecLimitCtrlPortLimit.setStatus(_A)
class _Gel2esw26kPortSecLimitCtrlPortAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw26kPortSecLimitCtrlPortAction_Type.__name__=_C
_Gel2esw26kPortSecLimitCtrlPortAction_Object=MibTableColumn
gel2esw26kPortSecLimitCtrlPortAction=_Gel2esw26kPortSecLimitCtrlPortAction_Object((1,3,6,1,4,1,5205,2,54,3,5,1,2,1,4),_Gel2esw26kPortSecLimitCtrlPortAction_Type())
gel2esw26kPortSecLimitCtrlPortAction.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortSecLimitCtrlPortAction.setStatus(_A)
_Gel2esw26kPortSecLimitCtrlPortState_Type=DisplayString
_Gel2esw26kPortSecLimitCtrlPortState_Object=MibTableColumn
gel2esw26kPortSecLimitCtrlPortState=_Gel2esw26kPortSecLimitCtrlPortState_Object((1,3,6,1,4,1,5205,2,54,3,5,1,2,1,5),_Gel2esw26kPortSecLimitCtrlPortState_Type())
gel2esw26kPortSecLimitCtrlPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortSecLimitCtrlPortState.setStatus(_A)
class _Gel2esw26kPortSecLimitCtrlPortReOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kPortSecLimitCtrlPortReOpen_Type.__name__=_C
_Gel2esw26kPortSecLimitCtrlPortReOpen_Object=MibTableColumn
gel2esw26kPortSecLimitCtrlPortReOpen=_Gel2esw26kPortSecLimitCtrlPortReOpen_Object((1,3,6,1,4,1,5205,2,54,3,5,1,2,1,6),_Gel2esw26kPortSecLimitCtrlPortReOpen_Type())
gel2esw26kPortSecLimitCtrlPortReOpen.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortSecLimitCtrlPortReOpen.setStatus(_A)
_Gel2esw26kPortSecSwitchStatusTable_Object=MibTable
gel2esw26kPortSecSwitchStatusTable=_Gel2esw26kPortSecSwitchStatusTable_Object((1,3,6,1,4,1,5205,2,54,3,5,2))
if mibBuilder.loadTexts:gel2esw26kPortSecSwitchStatusTable.setStatus(_A)
_Gel2esw26kPortSecSwitchStatusEntry_Object=MibTableRow
gel2esw26kPortSecSwitchStatusEntry=_Gel2esw26kPortSecSwitchStatusEntry_Object((1,3,6,1,4,1,5205,2,54,3,5,2,1))
gel2esw26kPortSecSwitchStatusEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:gel2esw26kPortSecSwitchStatusEntry.setStatus(_A)
class _Gel2esw26kPortSecSwitchStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kPortSecSwitchStatusPort_Type.__name__=_C
_Gel2esw26kPortSecSwitchStatusPort_Object=MibTableColumn
gel2esw26kPortSecSwitchStatusPort=_Gel2esw26kPortSecSwitchStatusPort_Object((1,3,6,1,4,1,5205,2,54,3,5,2,1,1),_Gel2esw26kPortSecSwitchStatusPort_Type())
gel2esw26kPortSecSwitchStatusPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kPortSecSwitchStatusPort.setStatus(_A)
_Gel2esw26kPortSecSwitchStatusUsers_Type=DisplayString
_Gel2esw26kPortSecSwitchStatusUsers_Object=MibTableColumn
gel2esw26kPortSecSwitchStatusUsers=_Gel2esw26kPortSecSwitchStatusUsers_Object((1,3,6,1,4,1,5205,2,54,3,5,2,1,2),_Gel2esw26kPortSecSwitchStatusUsers_Type())
gel2esw26kPortSecSwitchStatusUsers.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortSecSwitchStatusUsers.setStatus(_A)
_Gel2esw26kPortSecSwitchStatusState_Type=DisplayString
_Gel2esw26kPortSecSwitchStatusState_Object=MibTableColumn
gel2esw26kPortSecSwitchStatusState=_Gel2esw26kPortSecSwitchStatusState_Object((1,3,6,1,4,1,5205,2,54,3,5,2,1,3),_Gel2esw26kPortSecSwitchStatusState_Type())
gel2esw26kPortSecSwitchStatusState.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortSecSwitchStatusState.setStatus(_A)
class _Gel2esw26kPortSecSwitchStatusMACCountCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kPortSecSwitchStatusMACCountCurrent_Type.__name__=_C
_Gel2esw26kPortSecSwitchStatusMACCountCurrent_Object=MibTableColumn
gel2esw26kPortSecSwitchStatusMACCountCurrent=_Gel2esw26kPortSecSwitchStatusMACCountCurrent_Object((1,3,6,1,4,1,5205,2,54,3,5,2,1,4),_Gel2esw26kPortSecSwitchStatusMACCountCurrent_Type())
gel2esw26kPortSecSwitchStatusMACCountCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortSecSwitchStatusMACCountCurrent.setStatus(_A)
class _Gel2esw26kPortSecSwitchStatusMACCountLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kPortSecSwitchStatusMACCountLimit_Type.__name__=_C
_Gel2esw26kPortSecSwitchStatusMACCountLimit_Object=MibTableColumn
gel2esw26kPortSecSwitchStatusMACCountLimit=_Gel2esw26kPortSecSwitchStatusMACCountLimit_Object((1,3,6,1,4,1,5205,2,54,3,5,2,1,5),_Gel2esw26kPortSecSwitchStatusMACCountLimit_Type())
gel2esw26kPortSecSwitchStatusMACCountLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortSecSwitchStatusMACCountLimit.setStatus(_A)
_Gel2esw26kPortSecPortStatus_ObjectIdentity=ObjectIdentity
gel2esw26kPortSecPortStatus=_Gel2esw26kPortSecPortStatus_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,5,3))
class _Gel2esw26kPortSecPortStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kPortSecPortStatusPort_Type.__name__=_C
_Gel2esw26kPortSecPortStatusPort_Object=MibScalar
gel2esw26kPortSecPortStatusPort=_Gel2esw26kPortSecPortStatusPort_Object((1,3,6,1,4,1,5205,2,54,3,5,3,1),_Gel2esw26kPortSecPortStatusPort_Type())
gel2esw26kPortSecPortStatusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPortSecPortStatusPort.setStatus(_A)
_Gel2esw26kPortSecPortStatusTable_Object=MibTable
gel2esw26kPortSecPortStatusTable=_Gel2esw26kPortSecPortStatusTable_Object((1,3,6,1,4,1,5205,2,54,3,5,3,2))
if mibBuilder.loadTexts:gel2esw26kPortSecPortStatusTable.setStatus(_A)
_Gel2esw26kPortSecPortStatusEntry_Object=MibTableRow
gel2esw26kPortSecPortStatusEntry=_Gel2esw26kPortSecPortStatusEntry_Object((1,3,6,1,4,1,5205,2,54,3,5,3,2,1))
gel2esw26kPortSecPortStatusEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:gel2esw26kPortSecPortStatusEntry.setStatus(_A)
class _Gel2esw26kPortSecPortStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kPortSecPortStatusIndex_Type.__name__=_C
_Gel2esw26kPortSecPortStatusIndex_Object=MibTableColumn
gel2esw26kPortSecPortStatusIndex=_Gel2esw26kPortSecPortStatusIndex_Object((1,3,6,1,4,1,5205,2,54,3,5,3,2,1,1),_Gel2esw26kPortSecPortStatusIndex_Type())
gel2esw26kPortSecPortStatusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kPortSecPortStatusIndex.setStatus(_A)
_Gel2esw26kPortSecPortStatusMACAddress_Type=MacAddress
_Gel2esw26kPortSecPortStatusMACAddress_Object=MibTableColumn
gel2esw26kPortSecPortStatusMACAddress=_Gel2esw26kPortSecPortStatusMACAddress_Object((1,3,6,1,4,1,5205,2,54,3,5,3,2,1,2),_Gel2esw26kPortSecPortStatusMACAddress_Type())
gel2esw26kPortSecPortStatusMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortSecPortStatusMACAddress.setStatus(_A)
class _Gel2esw26kPortSecPortStatusVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Gel2esw26kPortSecPortStatusVLANId_Type.__name__=_C
_Gel2esw26kPortSecPortStatusVLANId_Object=MibTableColumn
gel2esw26kPortSecPortStatusVLANId=_Gel2esw26kPortSecPortStatusVLANId_Object((1,3,6,1,4,1,5205,2,54,3,5,3,2,1,3),_Gel2esw26kPortSecPortStatusVLANId_Type())
gel2esw26kPortSecPortStatusVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortSecPortStatusVLANId.setStatus(_A)
_Gel2esw26kPortSecPortStatusState_Type=DisplayString
_Gel2esw26kPortSecPortStatusState_Object=MibTableColumn
gel2esw26kPortSecPortStatusState=_Gel2esw26kPortSecPortStatusState_Object((1,3,6,1,4,1,5205,2,54,3,5,3,2,1,4),_Gel2esw26kPortSecPortStatusState_Type())
gel2esw26kPortSecPortStatusState.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortSecPortStatusState.setStatus(_A)
_Gel2esw26kPortSecPortStatusTimeOfAddition_Type=DisplayString
_Gel2esw26kPortSecPortStatusTimeOfAddition_Object=MibTableColumn
gel2esw26kPortSecPortStatusTimeOfAddition=_Gel2esw26kPortSecPortStatusTimeOfAddition_Object((1,3,6,1,4,1,5205,2,54,3,5,3,2,1,5),_Gel2esw26kPortSecPortStatusTimeOfAddition_Type())
gel2esw26kPortSecPortStatusTimeOfAddition.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortSecPortStatusTimeOfAddition.setStatus(_A)
_Gel2esw26kPortSecPortStatusAgeAndHold_Type=DisplayString
_Gel2esw26kPortSecPortStatusAgeAndHold_Object=MibTableColumn
gel2esw26kPortSecPortStatusAgeAndHold=_Gel2esw26kPortSecPortStatusAgeAndHold_Object((1,3,6,1,4,1,5205,2,54,3,5,3,2,1,6),_Gel2esw26kPortSecPortStatusAgeAndHold_Type())
gel2esw26kPortSecPortStatusAgeAndHold.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPortSecPortStatusAgeAndHold.setStatus(_A)
_Gel2esw26kAccessManagement_ObjectIdentity=ObjectIdentity
gel2esw26kAccessManagement=_Gel2esw26kAccessManagement_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,6))
_Gel2esw26kAccessMgtConf_ObjectIdentity=ObjectIdentity
gel2esw26kAccessMgtConf=_Gel2esw26kAccessMgtConf_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,6,1))
class _Gel2esw26kAccessMgtConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kAccessMgtConfMode_Type.__name__=_C
_Gel2esw26kAccessMgtConfMode_Object=MibScalar
gel2esw26kAccessMgtConfMode=_Gel2esw26kAccessMgtConfMode_Object((1,3,6,1,4,1,5205,2,54,3,6,1,1),_Gel2esw26kAccessMgtConfMode_Type())
gel2esw26kAccessMgtConfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kAccessMgtConfMode.setStatus(_A)
class _Gel2esw26kAccessMgtConfCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kAccessMgtConfCreate_Type.__name__=_C
_Gel2esw26kAccessMgtConfCreate_Object=MibScalar
gel2esw26kAccessMgtConfCreate=_Gel2esw26kAccessMgtConfCreate_Object((1,3,6,1,4,1,5205,2,54,3,6,1,2),_Gel2esw26kAccessMgtConfCreate_Type())
gel2esw26kAccessMgtConfCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kAccessMgtConfCreate.setStatus(_A)
_Gel2esw26kAccessMgtConfTable_Object=MibTable
gel2esw26kAccessMgtConfTable=_Gel2esw26kAccessMgtConfTable_Object((1,3,6,1,4,1,5205,2,54,3,6,1,3))
if mibBuilder.loadTexts:gel2esw26kAccessMgtConfTable.setStatus(_A)
_Gel2esw26kAccessMgtConfEntry_Object=MibTableRow
gel2esw26kAccessMgtConfEntry=_Gel2esw26kAccessMgtConfEntry_Object((1,3,6,1,4,1,5205,2,54,3,6,1,3,1))
gel2esw26kAccessMgtConfEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:gel2esw26kAccessMgtConfEntry.setStatus(_A)
class _Gel2esw26kAccessMgtIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Gel2esw26kAccessMgtIndex_Type.__name__=_C
_Gel2esw26kAccessMgtIndex_Object=MibTableColumn
gel2esw26kAccessMgtIndex=_Gel2esw26kAccessMgtIndex_Object((1,3,6,1,4,1,5205,2,54,3,6,1,3,1,1),_Gel2esw26kAccessMgtIndex_Type())
gel2esw26kAccessMgtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kAccessMgtIndex.setStatus(_A)
class _Gel2esw26kAccessMgtAddresstype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kAccessMgtAddresstype_Type.__name__=_C
_Gel2esw26kAccessMgtAddresstype_Object=MibTableColumn
gel2esw26kAccessMgtAddresstype=_Gel2esw26kAccessMgtAddresstype_Object((1,3,6,1,4,1,5205,2,54,3,6,1,3,1,2),_Gel2esw26kAccessMgtAddresstype_Type())
gel2esw26kAccessMgtAddresstype.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kAccessMgtAddresstype.setStatus(_A)
_Gel2esw26kAccessMgtStartIpAddress_Type=DisplayString
_Gel2esw26kAccessMgtStartIpAddress_Object=MibTableColumn
gel2esw26kAccessMgtStartIpAddress=_Gel2esw26kAccessMgtStartIpAddress_Object((1,3,6,1,4,1,5205,2,54,3,6,1,3,1,3),_Gel2esw26kAccessMgtStartIpAddress_Type())
gel2esw26kAccessMgtStartIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kAccessMgtStartIpAddress.setStatus(_A)
_Gel2esw26kAccessMgtEndIpAddress_Type=DisplayString
_Gel2esw26kAccessMgtEndIpAddress_Object=MibTableColumn
gel2esw26kAccessMgtEndIpAddress=_Gel2esw26kAccessMgtEndIpAddress_Object((1,3,6,1,4,1,5205,2,54,3,6,1,3,1,4),_Gel2esw26kAccessMgtEndIpAddress_Type())
gel2esw26kAccessMgtEndIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kAccessMgtEndIpAddress.setStatus(_A)
class _Gel2esw26kAccessMgtHttpHttps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kAccessMgtHttpHttps_Type.__name__=_C
_Gel2esw26kAccessMgtHttpHttps_Object=MibTableColumn
gel2esw26kAccessMgtHttpHttps=_Gel2esw26kAccessMgtHttpHttps_Object((1,3,6,1,4,1,5205,2,54,3,6,1,3,1,5),_Gel2esw26kAccessMgtHttpHttps_Type())
gel2esw26kAccessMgtHttpHttps.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kAccessMgtHttpHttps.setStatus(_A)
class _Gel2esw26kAccessMgtSNMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kAccessMgtSNMP_Type.__name__=_C
_Gel2esw26kAccessMgtSNMP_Object=MibTableColumn
gel2esw26kAccessMgtSNMP=_Gel2esw26kAccessMgtSNMP_Object((1,3,6,1,4,1,5205,2,54,3,6,1,3,1,6),_Gel2esw26kAccessMgtSNMP_Type())
gel2esw26kAccessMgtSNMP.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kAccessMgtSNMP.setStatus(_A)
class _Gel2esw26kAccessMgtTelnetSSH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kAccessMgtTelnetSSH_Type.__name__=_C
_Gel2esw26kAccessMgtTelnetSSH_Object=MibTableColumn
gel2esw26kAccessMgtTelnetSSH=_Gel2esw26kAccessMgtTelnetSSH_Object((1,3,6,1,4,1,5205,2,54,3,6,1,3,1,7),_Gel2esw26kAccessMgtTelnetSSH_Type())
gel2esw26kAccessMgtTelnetSSH.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kAccessMgtTelnetSSH.setStatus(_A)
class _Gel2esw26kAccessMgtRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Gel2esw26kAccessMgtRowStatus_Type.__name__=_C
_Gel2esw26kAccessMgtRowStatus_Object=MibTableColumn
gel2esw26kAccessMgtRowStatus=_Gel2esw26kAccessMgtRowStatus_Object((1,3,6,1,4,1,5205,2,54,3,6,1,3,1,8),_Gel2esw26kAccessMgtRowStatus_Type())
gel2esw26kAccessMgtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kAccessMgtRowStatus.setStatus(_A)
_Gel2esw26kAccessMgtStatistics_ObjectIdentity=ObjectIdentity
gel2esw26kAccessMgtStatistics=_Gel2esw26kAccessMgtStatistics_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,6,2))
_Gel2esw26kHttpReceivedPkts_Type=Counter32
_Gel2esw26kHttpReceivedPkts_Object=MibScalar
gel2esw26kHttpReceivedPkts=_Gel2esw26kHttpReceivedPkts_Object((1,3,6,1,4,1,5205,2,54,3,6,2,1),_Gel2esw26kHttpReceivedPkts_Type())
gel2esw26kHttpReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kHttpReceivedPkts.setStatus(_A)
_Gel2esw26kHttpAllowedPkts_Type=Counter32
_Gel2esw26kHttpAllowedPkts_Object=MibScalar
gel2esw26kHttpAllowedPkts=_Gel2esw26kHttpAllowedPkts_Object((1,3,6,1,4,1,5205,2,54,3,6,2,2),_Gel2esw26kHttpAllowedPkts_Type())
gel2esw26kHttpAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kHttpAllowedPkts.setStatus(_A)
_Gel2esw26kHttpDiscardedPkts_Type=Counter32
_Gel2esw26kHttpDiscardedPkts_Object=MibScalar
gel2esw26kHttpDiscardedPkts=_Gel2esw26kHttpDiscardedPkts_Object((1,3,6,1,4,1,5205,2,54,3,6,2,3),_Gel2esw26kHttpDiscardedPkts_Type())
gel2esw26kHttpDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kHttpDiscardedPkts.setStatus(_A)
_Gel2esw26kHttpsReceivedPkts_Type=Counter32
_Gel2esw26kHttpsReceivedPkts_Object=MibScalar
gel2esw26kHttpsReceivedPkts=_Gel2esw26kHttpsReceivedPkts_Object((1,3,6,1,4,1,5205,2,54,3,6,2,4),_Gel2esw26kHttpsReceivedPkts_Type())
gel2esw26kHttpsReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kHttpsReceivedPkts.setStatus(_A)
_Gel2esw26kHttpsAllowedPkts_Type=Counter32
_Gel2esw26kHttpsAllowedPkts_Object=MibScalar
gel2esw26kHttpsAllowedPkts=_Gel2esw26kHttpsAllowedPkts_Object((1,3,6,1,4,1,5205,2,54,3,6,2,5),_Gel2esw26kHttpsAllowedPkts_Type())
gel2esw26kHttpsAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kHttpsAllowedPkts.setStatus(_A)
_Gel2esw26kHttpsDiscardedPkts_Type=Counter32
_Gel2esw26kHttpsDiscardedPkts_Object=MibScalar
gel2esw26kHttpsDiscardedPkts=_Gel2esw26kHttpsDiscardedPkts_Object((1,3,6,1,4,1,5205,2,54,3,6,2,6),_Gel2esw26kHttpsDiscardedPkts_Type())
gel2esw26kHttpsDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kHttpsDiscardedPkts.setStatus(_A)
_Gel2esw26kSnmpReceivedPkts_Type=Counter32
_Gel2esw26kSnmpReceivedPkts_Object=MibScalar
gel2esw26kSnmpReceivedPkts=_Gel2esw26kSnmpReceivedPkts_Object((1,3,6,1,4,1,5205,2,54,3,6,2,7),_Gel2esw26kSnmpReceivedPkts_Type())
gel2esw26kSnmpReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSnmpReceivedPkts.setStatus(_A)
_Gel2esw26kSnmpAllowedPkts_Type=Counter32
_Gel2esw26kSnmpAllowedPkts_Object=MibScalar
gel2esw26kSnmpAllowedPkts=_Gel2esw26kSnmpAllowedPkts_Object((1,3,6,1,4,1,5205,2,54,3,6,2,8),_Gel2esw26kSnmpAllowedPkts_Type())
gel2esw26kSnmpAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSnmpAllowedPkts.setStatus(_A)
_Gel2esw26kSnmpDiscardedPkts_Type=Counter32
_Gel2esw26kSnmpDiscardedPkts_Object=MibScalar
gel2esw26kSnmpDiscardedPkts=_Gel2esw26kSnmpDiscardedPkts_Object((1,3,6,1,4,1,5205,2,54,3,6,2,9),_Gel2esw26kSnmpDiscardedPkts_Type())
gel2esw26kSnmpDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSnmpDiscardedPkts.setStatus(_A)
_Gel2esw26kTelnetReceivedPkts_Type=Counter32
_Gel2esw26kTelnetReceivedPkts_Object=MibScalar
gel2esw26kTelnetReceivedPkts=_Gel2esw26kTelnetReceivedPkts_Object((1,3,6,1,4,1,5205,2,54,3,6,2,10),_Gel2esw26kTelnetReceivedPkts_Type())
gel2esw26kTelnetReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kTelnetReceivedPkts.setStatus(_A)
_Gel2esw26kTelnetAllowedPkts_Type=Counter32
_Gel2esw26kTelnetAllowedPkts_Object=MibScalar
gel2esw26kTelnetAllowedPkts=_Gel2esw26kTelnetAllowedPkts_Object((1,3,6,1,4,1,5205,2,54,3,6,2,11),_Gel2esw26kTelnetAllowedPkts_Type())
gel2esw26kTelnetAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kTelnetAllowedPkts.setStatus(_A)
_Gel2esw26kTelnetDiscardedPkts_Type=Counter32
_Gel2esw26kTelnetDiscardedPkts_Object=MibScalar
gel2esw26kTelnetDiscardedPkts=_Gel2esw26kTelnetDiscardedPkts_Object((1,3,6,1,4,1,5205,2,54,3,6,2,12),_Gel2esw26kTelnetDiscardedPkts_Type())
gel2esw26kTelnetDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kTelnetDiscardedPkts.setStatus(_A)
_Gel2esw26kSSHReceivedPkts_Type=Counter32
_Gel2esw26kSSHReceivedPkts_Object=MibScalar
gel2esw26kSSHReceivedPkts=_Gel2esw26kSSHReceivedPkts_Object((1,3,6,1,4,1,5205,2,54,3,6,2,13),_Gel2esw26kSSHReceivedPkts_Type())
gel2esw26kSSHReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSSHReceivedPkts.setStatus(_A)
_Gel2esw26kSSHAllowedPkts_Type=Counter32
_Gel2esw26kSSHAllowedPkts_Object=MibScalar
gel2esw26kSSHAllowedPkts=_Gel2esw26kSSHAllowedPkts_Object((1,3,6,1,4,1,5205,2,54,3,6,2,14),_Gel2esw26kSSHAllowedPkts_Type())
gel2esw26kSSHAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSSHAllowedPkts.setStatus(_A)
_Gel2esw26kSSHDiscardedPkts_Type=Counter32
_Gel2esw26kSSHDiscardedPkts_Object=MibScalar
gel2esw26kSSHDiscardedPkts=_Gel2esw26kSSHDiscardedPkts_Object((1,3,6,1,4,1,5205,2,54,3,6,2,15),_Gel2esw26kSSHDiscardedPkts_Type())
gel2esw26kSSHDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kSSHDiscardedPkts.setStatus(_A)
class _Gel2esw26kAccessMgtStatisticsClearAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kAccessMgtStatisticsClearAll_Type.__name__=_C
_Gel2esw26kAccessMgtStatisticsClearAll_Object=MibScalar
gel2esw26kAccessMgtStatisticsClearAll=_Gel2esw26kAccessMgtStatisticsClearAll_Object((1,3,6,1,4,1,5205,2,54,3,6,2,16),_Gel2esw26kAccessMgtStatisticsClearAll_Type())
gel2esw26kAccessMgtStatisticsClearAll.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kAccessMgtStatisticsClearAll.setStatus(_A)
_Gel2esw26kSSH_ObjectIdentity=ObjectIdentity
gel2esw26kSSH=_Gel2esw26kSSH_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,7))
class _Gel2esw26kSSHMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kSSHMode_Type.__name__=_C
_Gel2esw26kSSHMode_Object=MibScalar
gel2esw26kSSHMode=_Gel2esw26kSSHMode_Object((1,3,6,1,4,1,5205,2,54,3,7,1),_Gel2esw26kSSHMode_Type())
gel2esw26kSSHMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSSHMode.setStatus(_A)
_Gel2esw26kHTTPS_ObjectIdentity=ObjectIdentity
gel2esw26kHTTPS=_Gel2esw26kHTTPS_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,8))
class _Gel2esw26kHTTPSMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kHTTPSMode_Type.__name__=_C
_Gel2esw26kHTTPSMode_Object=MibScalar
gel2esw26kHTTPSMode=_Gel2esw26kHTTPSMode_Object((1,3,6,1,4,1,5205,2,54,3,8,1),_Gel2esw26kHTTPSMode_Type())
gel2esw26kHTTPSMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kHTTPSMode.setStatus(_A)
class _Gel2esw26kHTTPSAutoRedirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kHTTPSAutoRedirect_Type.__name__=_C
_Gel2esw26kHTTPSAutoRedirect_Object=MibScalar
gel2esw26kHTTPSAutoRedirect=_Gel2esw26kHTTPSAutoRedirect_Object((1,3,6,1,4,1,5205,2,54,3,8,2),_Gel2esw26kHTTPSAutoRedirect_Type())
gel2esw26kHTTPSAutoRedirect.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kHTTPSAutoRedirect.setStatus(_A)
_Gel2esw26kAuthMethod_ObjectIdentity=ObjectIdentity
gel2esw26kAuthMethod=_Gel2esw26kAuthMethod_ObjectIdentity((1,3,6,1,4,1,5205,2,54,3,9))
class _Gel2esw26kConsoleAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw26kConsoleAuthMethod_Type.__name__=_C
_Gel2esw26kConsoleAuthMethod_Object=MibScalar
gel2esw26kConsoleAuthMethod=_Gel2esw26kConsoleAuthMethod_Object((1,3,6,1,4,1,5205,2,54,3,9,1),_Gel2esw26kConsoleAuthMethod_Type())
gel2esw26kConsoleAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kConsoleAuthMethod.setStatus(_A)
class _Gel2esw26kConsoleFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kConsoleFallback_Type.__name__=_C
_Gel2esw26kConsoleFallback_Object=MibScalar
gel2esw26kConsoleFallback=_Gel2esw26kConsoleFallback_Object((1,3,6,1,4,1,5205,2,54,3,9,2),_Gel2esw26kConsoleFallback_Type())
gel2esw26kConsoleFallback.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kConsoleFallback.setStatus(_A)
class _Gel2esw26kTelnetAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw26kTelnetAuthMethod_Type.__name__=_C
_Gel2esw26kTelnetAuthMethod_Object=MibScalar
gel2esw26kTelnetAuthMethod=_Gel2esw26kTelnetAuthMethod_Object((1,3,6,1,4,1,5205,2,54,3,9,3),_Gel2esw26kTelnetAuthMethod_Type())
gel2esw26kTelnetAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTelnetAuthMethod.setStatus(_A)
class _Gel2esw26kTelnetFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kTelnetFallback_Type.__name__=_C
_Gel2esw26kTelnetFallback_Object=MibScalar
gel2esw26kTelnetFallback=_Gel2esw26kTelnetFallback_Object((1,3,6,1,4,1,5205,2,54,3,9,4),_Gel2esw26kTelnetFallback_Type())
gel2esw26kTelnetFallback.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kTelnetFallback.setStatus(_A)
class _Gel2esw26kSshAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw26kSshAuthMethod_Type.__name__=_C
_Gel2esw26kSshAuthMethod_Object=MibScalar
gel2esw26kSshAuthMethod=_Gel2esw26kSshAuthMethod_Object((1,3,6,1,4,1,5205,2,54,3,9,5),_Gel2esw26kSshAuthMethod_Type())
gel2esw26kSshAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSshAuthMethod.setStatus(_A)
class _Gel2esw26kSshFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kSshFallback_Type.__name__=_C
_Gel2esw26kSshFallback_Object=MibScalar
gel2esw26kSshFallback=_Gel2esw26kSshFallback_Object((1,3,6,1,4,1,5205,2,54,3,9,6),_Gel2esw26kSshFallback_Type())
gel2esw26kSshFallback.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSshFallback.setStatus(_A)
class _Gel2esw26kWebAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Gel2esw26kWebAuthMethod_Type.__name__=_C
_Gel2esw26kWebAuthMethod_Object=MibScalar
gel2esw26kWebAuthMethod=_Gel2esw26kWebAuthMethod_Object((1,3,6,1,4,1,5205,2,54,3,9,7),_Gel2esw26kWebAuthMethod_Type())
gel2esw26kWebAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kWebAuthMethod.setStatus(_A)
class _Gel2esw26kWebFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kWebFallback_Type.__name__=_C
_Gel2esw26kWebFallback_Object=MibScalar
gel2esw26kWebFallback=_Gel2esw26kWebFallback_Object((1,3,6,1,4,1,5205,2,54,3,9,8),_Gel2esw26kWebFallback_Type())
gel2esw26kWebFallback.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kWebFallback.setStatus(_A)
_Gel2esw26kMaintenance_ObjectIdentity=ObjectIdentity
gel2esw26kMaintenance=_Gel2esw26kMaintenance_ObjectIdentity((1,3,6,1,4,1,5205,2,54,4))
class _Gel2esw26kRestartDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kRestartDevice_Type.__name__=_C
_Gel2esw26kRestartDevice_Object=MibScalar
gel2esw26kRestartDevice=_Gel2esw26kRestartDevice_Object((1,3,6,1,4,1,5205,2,54,4,1),_Gel2esw26kRestartDevice_Type())
gel2esw26kRestartDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kRestartDevice.setStatus(_A)
_Gel2esw26kFirmware_ObjectIdentity=ObjectIdentity
gel2esw26kFirmware=_Gel2esw26kFirmware_ObjectIdentity((1,3,6,1,4,1,5205,2,54,4,2))
_Gel2esw26kFirmwareIpAddress_Type=IpAddress
_Gel2esw26kFirmwareIpAddress_Object=MibScalar
gel2esw26kFirmwareIpAddress=_Gel2esw26kFirmwareIpAddress_Object((1,3,6,1,4,1,5205,2,54,4,2,1),_Gel2esw26kFirmwareIpAddress_Type())
gel2esw26kFirmwareIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kFirmwareIpAddress.setStatus(_A)
_Gel2esw26kFirmwareFileName_Type=DisplayString
_Gel2esw26kFirmwareFileName_Object=MibScalar
gel2esw26kFirmwareFileName=_Gel2esw26kFirmwareFileName_Object((1,3,6,1,4,1,5205,2,54,4,2,2),_Gel2esw26kFirmwareFileName_Type())
gel2esw26kFirmwareFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kFirmwareFileName.setStatus(_A)
class _Gel2esw26kDoFirmwareUpgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kDoFirmwareUpgrade_Type.__name__=_C
_Gel2esw26kDoFirmwareUpgrade_Object=MibScalar
gel2esw26kDoFirmwareUpgrade=_Gel2esw26kDoFirmwareUpgrade_Object((1,3,6,1,4,1,5205,2,54,4,2,3),_Gel2esw26kDoFirmwareUpgrade_Type())
gel2esw26kDoFirmwareUpgrade.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kDoFirmwareUpgrade.setStatus(_A)
_Gel2esw26kSaveOrRestore_ObjectIdentity=ObjectIdentity
gel2esw26kSaveOrRestore=_Gel2esw26kSaveOrRestore_ObjectIdentity((1,3,6,1,4,1,5205,2,54,4,3))
class _Gel2esw26kFactoryDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kFactoryDefaults_Type.__name__=_C
_Gel2esw26kFactoryDefaults_Object=MibScalar
gel2esw26kFactoryDefaults=_Gel2esw26kFactoryDefaults_Object((1,3,6,1,4,1,5205,2,54,4,3,1),_Gel2esw26kFactoryDefaults_Type())
gel2esw26kFactoryDefaults.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kFactoryDefaults.setStatus(_A)
class _Gel2esw26kSaveStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kSaveStart_Type.__name__=_C
_Gel2esw26kSaveStart_Object=MibScalar
gel2esw26kSaveStart=_Gel2esw26kSaveStart_Object((1,3,6,1,4,1,5205,2,54,4,3,2),_Gel2esw26kSaveStart_Type())
gel2esw26kSaveStart.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSaveStart.setStatus(_A)
class _Gel2esw26kSaveUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kSaveUser_Type.__name__=_C
_Gel2esw26kSaveUser_Object=MibScalar
gel2esw26kSaveUser=_Gel2esw26kSaveUser_Object((1,3,6,1,4,1,5205,2,54,4,3,3),_Gel2esw26kSaveUser_Type())
gel2esw26kSaveUser.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kSaveUser.setStatus(_A)
class _Gel2esw26kRestoreUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Gel2esw26kRestoreUser_Type.__name__=_C
_Gel2esw26kRestoreUser_Object=MibScalar
gel2esw26kRestoreUser=_Gel2esw26kRestoreUser_Object((1,3,6,1,4,1,5205,2,54,4,3,4),_Gel2esw26kRestoreUser_Type())
gel2esw26kRestoreUser.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kRestoreUser.setStatus(_A)
_Gel2esw26kExportOrImport_ObjectIdentity=ObjectIdentity
gel2esw26kExportOrImport=_Gel2esw26kExportOrImport_ObjectIdentity((1,3,6,1,4,1,5205,2,54,4,4))
_Gel2esw26kExportIpAddress_Type=IpAddress
_Gel2esw26kExportIpAddress_Object=MibScalar
gel2esw26kExportIpAddress=_Gel2esw26kExportIpAddress_Object((1,3,6,1,4,1,5205,2,54,4,4,1),_Gel2esw26kExportIpAddress_Type())
gel2esw26kExportIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kExportIpAddress.setStatus(_A)
_Gel2esw26kExportConfigName_Type=DisplayString
_Gel2esw26kExportConfigName_Object=MibScalar
gel2esw26kExportConfigName=_Gel2esw26kExportConfigName_Object((1,3,6,1,4,1,5205,2,54,4,4,2),_Gel2esw26kExportConfigName_Type())
gel2esw26kExportConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kExportConfigName.setStatus(_A)
class _Gel2esw26kDoExportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Gel2esw26kDoExportConfig_Type.__name__=_C
_Gel2esw26kDoExportConfig_Object=MibScalar
gel2esw26kDoExportConfig=_Gel2esw26kDoExportConfig_Object((1,3,6,1,4,1,5205,2,54,4,4,3),_Gel2esw26kDoExportConfig_Type())
gel2esw26kDoExportConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kDoExportConfig.setStatus(_A)
_Gel2esw26kImportIpAddress_Type=IpAddress
_Gel2esw26kImportIpAddress_Object=MibScalar
gel2esw26kImportIpAddress=_Gel2esw26kImportIpAddress_Object((1,3,6,1,4,1,5205,2,54,4,4,4),_Gel2esw26kImportIpAddress_Type())
gel2esw26kImportIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kImportIpAddress.setStatus(_A)
_Gel2esw26kImportConfigName_Type=DisplayString
_Gel2esw26kImportConfigName_Object=MibScalar
gel2esw26kImportConfigName=_Gel2esw26kImportConfigName_Object((1,3,6,1,4,1,5205,2,54,4,4,5),_Gel2esw26kImportConfigName_Type())
gel2esw26kImportConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kImportConfigName.setStatus(_A)
class _Gel2esw26kDoImportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Gel2esw26kDoImportConfig_Type.__name__=_C
_Gel2esw26kDoImportConfig_Object=MibScalar
gel2esw26kDoImportConfig=_Gel2esw26kDoImportConfig_Object((1,3,6,1,4,1,5205,2,54,4,4,6),_Gel2esw26kDoImportConfig_Type())
gel2esw26kDoImportConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kDoImportConfig.setStatus(_A)
_Gel2esw26kDiagnostics_ObjectIdentity=ObjectIdentity
gel2esw26kDiagnostics=_Gel2esw26kDiagnostics_ObjectIdentity((1,3,6,1,4,1,5205,2,54,4,5))
_Gel2esw26kPingIpAddress_Type=IpAddress
_Gel2esw26kPingIpAddress_Object=MibScalar
gel2esw26kPingIpAddress=_Gel2esw26kPingIpAddress_Object((1,3,6,1,4,1,5205,2,54,4,5,1),_Gel2esw26kPingIpAddress_Type())
gel2esw26kPingIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPingIpAddress.setStatus(_A)
class _Gel2esw26kPingSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,1400))
_Gel2esw26kPingSize_Type.__name__=_C
_Gel2esw26kPingSize_Object=MibScalar
gel2esw26kPingSize=_Gel2esw26kPingSize_Object((1,3,6,1,4,1,5205,2,54,4,5,2),_Gel2esw26kPingSize_Type())
gel2esw26kPingSize.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPingSize.setStatus(_A)
class _Gel2esw26kDoPingConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Gel2esw26kDoPingConfig_Type.__name__=_C
_Gel2esw26kDoPingConfig_Object=MibScalar
gel2esw26kDoPingConfig=_Gel2esw26kDoPingConfig_Object((1,3,6,1,4,1,5205,2,54,4,5,3),_Gel2esw26kDoPingConfig_Type())
gel2esw26kDoPingConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kDoPingConfig.setStatus(_A)
_Gel2esw26kPingResult_Type=DisplayString
_Gel2esw26kPingResult_Object=MibScalar
gel2esw26kPingResult=_Gel2esw26kPingResult_Object((1,3,6,1,4,1,5205,2,54,4,5,4),_Gel2esw26kPingResult_Type())
gel2esw26kPingResult.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPingResult.setStatus(_A)
_Gel2esw26kPing6IpAddress_Type=DisplayString
_Gel2esw26kPing6IpAddress_Object=MibScalar
gel2esw26kPing6IpAddress=_Gel2esw26kPing6IpAddress_Object((1,3,6,1,4,1,5205,2,54,4,5,5),_Gel2esw26kPing6IpAddress_Type())
gel2esw26kPing6IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPing6IpAddress.setStatus(_A)
class _Gel2esw26kPing6Size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,1400))
_Gel2esw26kPing6Size_Type.__name__=_C
_Gel2esw26kPing6Size_Object=MibScalar
gel2esw26kPing6Size=_Gel2esw26kPing6Size_Object((1,3,6,1,4,1,5205,2,54,4,5,6),_Gel2esw26kPing6Size_Type())
gel2esw26kPing6Size.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kPing6Size.setStatus(_A)
class _Gel2esw26kDoPing6Config_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Gel2esw26kDoPing6Config_Type.__name__=_C
_Gel2esw26kDoPing6Config_Object=MibScalar
gel2esw26kDoPing6Config=_Gel2esw26kDoPing6Config_Object((1,3,6,1,4,1,5205,2,54,4,5,7),_Gel2esw26kDoPing6Config_Type())
gel2esw26kDoPing6Config.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kDoPing6Config.setStatus(_A)
_Gel2esw26kPing6Result_Type=DisplayString
_Gel2esw26kPing6Result_Object=MibScalar
gel2esw26kPing6Result=_Gel2esw26kPing6Result_Object((1,3,6,1,4,1,5205,2,54,4,5,8),_Gel2esw26kPing6Result_Type())
gel2esw26kPing6Result.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kPing6Result.setStatus(_A)
_Gel2esw26kVeriPHY_ObjectIdentity=ObjectIdentity
gel2esw26kVeriPHY=_Gel2esw26kVeriPHY_ObjectIdentity((1,3,6,1,4,1,5205,2,54,4,5,9))
class _Gel2esw26kVeriPHYTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kVeriPHYTest_Type.__name__=_C
_Gel2esw26kVeriPHYTest_Object=MibScalar
gel2esw26kVeriPHYTest=_Gel2esw26kVeriPHYTest_Object((1,3,6,1,4,1,5205,2,54,4,5,9,1),_Gel2esw26kVeriPHYTest_Type())
gel2esw26kVeriPHYTest.setMaxAccess(_B)
if mibBuilder.loadTexts:gel2esw26kVeriPHYTest.setStatus(_A)
_Gel2esw26kVeriPHYTable_Object=MibTable
gel2esw26kVeriPHYTable=_Gel2esw26kVeriPHYTable_Object((1,3,6,1,4,1,5205,2,54,4,5,9,2))
if mibBuilder.loadTexts:gel2esw26kVeriPHYTable.setStatus(_A)
_Gel2esw26kVeriPHYEntry_Object=MibTableRow
gel2esw26kVeriPHYEntry=_Gel2esw26kVeriPHYEntry_Object((1,3,6,1,4,1,5205,2,54,4,5,9,2,1))
gel2esw26kVeriPHYEntry.setIndexNames((0,_E,_s))
if mibBuilder.loadTexts:gel2esw26kVeriPHYEntry.setStatus(_A)
class _Gel2esw26kVeriPHYPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Gel2esw26kVeriPHYPort_Type.__name__=_C
_Gel2esw26kVeriPHYPort_Object=MibTableColumn
gel2esw26kVeriPHYPort=_Gel2esw26kVeriPHYPort_Object((1,3,6,1,4,1,5205,2,54,4,5,9,2,1,1),_Gel2esw26kVeriPHYPort_Type())
gel2esw26kVeriPHYPort.setMaxAccess(_F)
if mibBuilder.loadTexts:gel2esw26kVeriPHYPort.setStatus(_A)
_Gel2esw26kVeriPHYPairA_Type=DisplayString
_Gel2esw26kVeriPHYPairA_Object=MibTableColumn
gel2esw26kVeriPHYPairA=_Gel2esw26kVeriPHYPairA_Object((1,3,6,1,4,1,5205,2,54,4,5,9,2,1,2),_Gel2esw26kVeriPHYPairA_Type())
gel2esw26kVeriPHYPairA.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kVeriPHYPairA.setStatus(_A)
_Gel2esw26kVeriPHYLengthA_Type=DisplayString
_Gel2esw26kVeriPHYLengthA_Object=MibTableColumn
gel2esw26kVeriPHYLengthA=_Gel2esw26kVeriPHYLengthA_Object((1,3,6,1,4,1,5205,2,54,4,5,9,2,1,3),_Gel2esw26kVeriPHYLengthA_Type())
gel2esw26kVeriPHYLengthA.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kVeriPHYLengthA.setStatus(_A)
_Gel2esw26kVeriPHYPairB_Type=DisplayString
_Gel2esw26kVeriPHYPairB_Object=MibTableColumn
gel2esw26kVeriPHYPairB=_Gel2esw26kVeriPHYPairB_Object((1,3,6,1,4,1,5205,2,54,4,5,9,2,1,4),_Gel2esw26kVeriPHYPairB_Type())
gel2esw26kVeriPHYPairB.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kVeriPHYPairB.setStatus(_A)
_Gel2esw26kVeriPHYLengthB_Type=DisplayString
_Gel2esw26kVeriPHYLengthB_Object=MibTableColumn
gel2esw26kVeriPHYLengthB=_Gel2esw26kVeriPHYLengthB_Object((1,3,6,1,4,1,5205,2,54,4,5,9,2,1,5),_Gel2esw26kVeriPHYLengthB_Type())
gel2esw26kVeriPHYLengthB.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kVeriPHYLengthB.setStatus(_A)
_Gel2esw26kVeriPHYPairC_Type=DisplayString
_Gel2esw26kVeriPHYPairC_Object=MibTableColumn
gel2esw26kVeriPHYPairC=_Gel2esw26kVeriPHYPairC_Object((1,3,6,1,4,1,5205,2,54,4,5,9,2,1,6),_Gel2esw26kVeriPHYPairC_Type())
gel2esw26kVeriPHYPairC.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kVeriPHYPairC.setStatus(_A)
_Gel2esw26kVeriPHYLengthC_Type=DisplayString
_Gel2esw26kVeriPHYLengthC_Object=MibTableColumn
gel2esw26kVeriPHYLengthC=_Gel2esw26kVeriPHYLengthC_Object((1,3,6,1,4,1,5205,2,54,4,5,9,2,1,7),_Gel2esw26kVeriPHYLengthC_Type())
gel2esw26kVeriPHYLengthC.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kVeriPHYLengthC.setStatus(_A)
_Gel2esw26kVeriPHYPairD_Type=DisplayString
_Gel2esw26kVeriPHYPairD_Object=MibTableColumn
gel2esw26kVeriPHYPairD=_Gel2esw26kVeriPHYPairD_Object((1,3,6,1,4,1,5205,2,54,4,5,9,2,1,8),_Gel2esw26kVeriPHYPairD_Type())
gel2esw26kVeriPHYPairD.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kVeriPHYPairD.setStatus(_A)
_Gel2esw26kVeriPHYLengthD_Type=DisplayString
_Gel2esw26kVeriPHYLengthD_Object=MibTableColumn
gel2esw26kVeriPHYLengthD=_Gel2esw26kVeriPHYLengthD_Object((1,3,6,1,4,1,5205,2,54,4,5,9,2,1,9),_Gel2esw26kVeriPHYLengthD_Type())
gel2esw26kVeriPHYLengthD.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kVeriPHYLengthD.setStatus(_A)
_Gel2esw26kTrap_ObjectIdentity=ObjectIdentity
gel2esw26kTrap=_Gel2esw26kTrap_ObjectIdentity((1,3,6,1,4,1,5205,2,54,5))
_Gel2esw26kTrapEvent_ObjectIdentity=ObjectIdentity
gel2esw26kTrapEvent=_Gel2esw26kTrapEvent_ObjectIdentity((1,3,6,1,4,1,5205,2,54,5,1))
_Gel2esw26kTrapVariable_ObjectIdentity=ObjectIdentity
gel2esw26kTrapVariable=_Gel2esw26kTrapVariable_ObjectIdentity((1,3,6,1,4,1,5205,2,54,5,2))
_Gel2esw26kInformation_Type=DisplayString
_Gel2esw26kInformation_Object=MibScalar
gel2esw26kInformation=_Gel2esw26kInformation_Object((1,3,6,1,4,1,5205,2,54,5,2,1),_Gel2esw26kInformation_Type())
gel2esw26kInformation.setMaxAccess(_D)
if mibBuilder.loadTexts:gel2esw26kInformation.setStatus(_A)
gel2esw26kEmergency=NotificationType((1,3,6,1,4,1,5205,2,54,5,1,1))
gel2esw26kEmergency.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw26kEmergency.setStatus(_A)
gel2esw26kAlert=NotificationType((1,3,6,1,4,1,5205,2,54,5,1,2))
gel2esw26kAlert.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw26kAlert.setStatus(_A)
gel2esw26kCritical=NotificationType((1,3,6,1,4,1,5205,2,54,5,1,3))
gel2esw26kCritical.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw26kCritical.setStatus(_A)
gel2esw26kError=NotificationType((1,3,6,1,4,1,5205,2,54,5,1,4))
gel2esw26kError.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw26kError.setStatus(_A)
gel2esw26kWarning=NotificationType((1,3,6,1,4,1,5205,2,54,5,1,5))
gel2esw26kWarning.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw26kWarning.setStatus(_A)
gel2esw26kNotice=NotificationType((1,3,6,1,4,1,5205,2,54,5,1,6))
gel2esw26kNotice.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw26kNotice.setStatus(_A)
gel2esw26kInformational=NotificationType((1,3,6,1,4,1,5205,2,54,5,1,7))
gel2esw26kInformational.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw26kInformational.setStatus(_A)
gel2esw26kDebug=NotificationType((1,3,6,1,4,1,5205,2,54,5,1,8))
gel2esw26kDebug.setObjects((_E,_H))
if mibBuilder.loadTexts:gel2esw26kDebug.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'privatetech':privatetech,'switch':switch,'gel2esw26kProductId':gel2esw26kProductId,'gel2esw26kSystem':gel2esw26kSystem,'gel2esw26kSystemInformation':gel2esw26kSystemInformation,'gel2esw26kModelName':gel2esw26kModelName,'gel2esw26kBIOSVersion':gel2esw26kBIOSVersion,'gel2esw26kFirmwareVersion':gel2esw26kFirmwareVersion,'gel2esw26kHardwareMechanicalVersion':gel2esw26kHardwareMechanicalVersion,'gel2esw26kSeriesNumber':gel2esw26kSeriesNumber,'gel2esw26kHostMACAddress':gel2esw26kHostMACAddress,'gel2esw26kConsoleBaudrate':gel2esw26kConsoleBaudrate,'gel2esw26kRAMSize':gel2esw26kRAMSize,'gel2esw26kFlashSize':gel2esw26kFlashSize,'gel2esw26kBridgeFBDSize':gel2esw26kBridgeFBDSize,'gel2esw26kTransmitQueue':gel2esw26kTransmitQueue,'gel2esw26kMaximumFrameSize':gel2esw26kMaximumFrameSize,'gel2esw26kCPULoad':gel2esw26kCPULoad,'gel2esw26kSystemTime':gel2esw26kSystemTime,'gel2esw26kSystemTimeManual':gel2esw26kSystemTimeManual,'gel2esw26kSystemTimeManualClockSource':gel2esw26kSystemTimeManualClockSource,'gel2esw26kSystemTimeManualLocaltime':gel2esw26kSystemTimeManualLocaltime,'gel2esw26kSystemTimeManualTimeZoneOffset':gel2esw26kSystemTimeManualTimeZoneOffset,'gel2esw26kSystemTimeManualDaylightSavings':gel2esw26kSystemTimeManualDaylightSavings,'gel2esw26kSystemTimeManualTimeSetOffset':gel2esw26kSystemTimeManualTimeSetOffset,'gel2esw26kSystemTimeManualDaylightSavingsType':gel2esw26kSystemTimeManualDaylightSavingsType,'gel2esw26kSystemTimeManualDaylightSavingsBydatesFrom':gel2esw26kSystemTimeManualDaylightSavingsBydatesFrom,'gel2esw26kSystemTimeManualDaylightSavingsBydatesTo':gel2esw26kSystemTimeManualDaylightSavingsBydatesTo,'gel2esw26kSystemTimeManualDaylightSavingsRecurringDayFrom':gel2esw26kSystemTimeManualDaylightSavingsRecurringDayFrom,'gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekFrom':gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekFrom,'gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthFrom':gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthFrom,'gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeFrom':gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeFrom,'gel2esw26kSystemTimeManualDaylightSavingsRecurringDayTo':gel2esw26kSystemTimeManualDaylightSavingsRecurringDayTo,'gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekTo':gel2esw26kSystemTimeManualDaylightSavingsRecurringWeekTo,'gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthTo':gel2esw26kSystemTimeManualDaylightSavingsRecurringMonthTo,'gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeTo':gel2esw26kSystemTimeManualDaylightSavingsRecurringTimeTo,'gel2esw26kSystemTimeNTP':gel2esw26kSystemTimeNTP,'gel2esw26kSystemTimeNTPTable':gel2esw26kSystemTimeNTPTable,'gel2esw26kSystemTimeNTPEntry':gel2esw26kSystemTimeNTPEntry,_K:gel2esw26kSystemTimeNTPIndex,'gel2esw26kSystemTimeNTPServerIPType':gel2esw26kSystemTimeNTPServerIPType,'gel2esw26kSystemTimeNTPServer':gel2esw26kSystemTimeNTPServer,'gel2esw26kSystemTimeNTPCurrentMode':gel2esw26kSystemTimeNTPCurrentMode,'gel2esw26kSystemAccount':gel2esw26kSystemAccount,'gel2esw26kSystemAccountUsers':gel2esw26kSystemAccountUsers,'gel2esw26kSystemAccountUserCreate':gel2esw26kSystemAccountUserCreate,'gel2esw26kSystemAccountUsersTable':gel2esw26kSystemAccountUsersTable,'gel2esw26kSystemAccountUsersEntry':gel2esw26kSystemAccountUsersEntry,_L:gel2esw26kUserIndex,'gel2esw26kUserName':gel2esw26kUserName,'gel2esw26kPassword':gel2esw26kPassword,'gel2esw26kUserPrivilegeLevel':gel2esw26kUserPrivilegeLevel,'gel2esw26kAccountUserRowStatus':gel2esw26kAccountUserRowStatus,'gel2esw26kSystemAccountPrivilegeLevel':gel2esw26kSystemAccountPrivilegeLevel,'gel2esw26kAccountPrivilegeLevel':gel2esw26kAccountPrivilegeLevel,'gel2esw26kAggregationPrivilegeLevel':gel2esw26kAggregationPrivilegeLevel,'gel2esw26kDiagnosticsPrivilegeLevel':gel2esw26kDiagnosticsPrivilegeLevel,'gel2esw26kEEEPrivilegeLevel':gel2esw26kEEEPrivilegeLevel,'gel2esw26kEasyportPrivilegeLevel':gel2esw26kEasyportPrivilegeLevel,'gel2esw26kGARPPrivilegeLevel':gel2esw26kGARPPrivilegeLevel,'gel2esw26kGVRPPrivilegeLevel':gel2esw26kGVRPPrivilegeLevel,'gel2esw26kIPPrivilegeLevel':gel2esw26kIPPrivilegeLevel,'gel2esw26kIPMCSnoopingPrivilegeLevel':gel2esw26kIPMCSnoopingPrivilegeLevel,'gel2esw26kLACPPrivilegeLevel':gel2esw26kLACPPrivilegeLevel,'gel2esw26kLLDPPrivilegeLevel':gel2esw26kLLDPPrivilegeLevel,'gel2esw26kLLDPMEDPrivilegeLevel':gel2esw26kLLDPMEDPrivilegeLevel,'gel2esw26kLoopProtectPrivilegeLevel':gel2esw26kLoopProtectPrivilegeLevel,'gel2esw26kMACTablePrivilegeLevel':gel2esw26kMACTablePrivilegeLevel,'gel2esw26kMVRPrivilegeLevel':gel2esw26kMVRPrivilegeLevel,'gel2esw26kMaintenancePrivilegeLevel':gel2esw26kMaintenancePrivilegeLevel,'gel2esw26kMirroringPrivilegeLevel':gel2esw26kMirroringPrivilegeLevel,'gel2esw26kPortsPrivilegeLevel':gel2esw26kPortsPrivilegeLevel,'gel2esw26kPrivateVLANsPrivilegeLevel':gel2esw26kPrivateVLANsPrivilegeLevel,'gel2esw26kQoSPrivilegeLevel':gel2esw26kQoSPrivilegeLevel,'gel2esw26kSFlowPrivilegeLevel':gel2esw26kSFlowPrivilegeLevel,'gel2esw26kSMTPPrivilegeLevel':gel2esw26kSMTPPrivilegeLevel,'gel2esw26kSNMPPrivilegeLevel':gel2esw26kSNMPPrivilegeLevel,'gel2esw26kSecurityPrivilegeLevel':gel2esw26kSecurityPrivilegeLevel,'gel2esw26kSingleIPPrivilegeLevel':gel2esw26kSingleIPPrivilegeLevel,'gel2esw26kSpanningTreePrivilegeLevel':gel2esw26kSpanningTreePrivilegeLevel,'gel2esw26kSystemPrivilegeLevel':gel2esw26kSystemPrivilegeLevel,'gel2esw26kTrapEventPrivilegeLevel':gel2esw26kTrapEventPrivilegeLevel,'gel2esw26kUPnPPrivilegeLevel':gel2esw26kUPnPPrivilegeLevel,'gel2esw26kVCLPrivilegeLevel':gel2esw26kVCLPrivilegeLevel,'gel2esw26kVLANsPrivilegeLevel':gel2esw26kVLANsPrivilegeLevel,'gel2esw26kVoiceVLANPrivilegeLevel':gel2esw26kVoiceVLANPrivilegeLevel,'gel2esw26kIP':gel2esw26kIP,'gel2esw26kIPv4':gel2esw26kIPv4,'gel2esw26kIPv4Configured':gel2esw26kIPv4Configured,'gel2esw26kIpv4DHCPClient':gel2esw26kIpv4DHCPClient,'gel2esw26kIPv4Address':gel2esw26kIPv4Address,'gel2esw26kIPv4Mask':gel2esw26kIPv4Mask,'gel2esw26kIPv4Gateway':gel2esw26kIPv4Gateway,'gel2esw26kIPv4VLANId':gel2esw26kIPv4VLANId,'gel2esw26kIPv4DNSServer':gel2esw26kIPv4DNSServer,'gel2esw26kIPv4DNSProxy':gel2esw26kIPv4DNSProxy,'gel2esw26kIPv4Current':gel2esw26kIPv4Current,'gel2esw26kIpv4CurrentDHCPClient':gel2esw26kIpv4CurrentDHCPClient,'gel2esw26kIPv4CurrentAddress':gel2esw26kIPv4CurrentAddress,'gel2esw26kIPv4CurrentMask':gel2esw26kIPv4CurrentMask,'gel2esw26kIPv4CurrentGateway':gel2esw26kIPv4CurrentGateway,'gel2esw26kIPv4CurrentVLANId':gel2esw26kIPv4CurrentVLANId,'gel2esw26kIPv4CurrentDNSServer':gel2esw26kIPv4CurrentDNSServer,'gel2esw26kIPv6':gel2esw26kIPv6,'gel2esw26kIPv6Configured':gel2esw26kIPv6Configured,'gel2esw26kIpv6AutoConfiguration':gel2esw26kIpv6AutoConfiguration,'gel2esw26kIpv6Address':gel2esw26kIpv6Address,'gel2esw26kIpv6Prefix':gel2esw26kIpv6Prefix,'gel2esw26kIpv6Gateway':gel2esw26kIpv6Gateway,'gel2esw26kIPv6Current':gel2esw26kIPv6Current,'gel2esw26kIpv6CurrentAutoConfiguration':gel2esw26kIpv6CurrentAutoConfiguration,'gel2esw26kIpv6CurrentAddress':gel2esw26kIpv6CurrentAddress,'gel2esw26kIpv6CurrentLinkLocalAddress':gel2esw26kIpv6CurrentLinkLocalAddress,'gel2esw26kIpv6CurrentPrefix':gel2esw26kIpv6CurrentPrefix,'gel2esw26kIpv6CurrentGateway':gel2esw26kIpv6CurrentGateway,'gel2esw26kSyslog':gel2esw26kSyslog,'gel2esw26kSyslogConf':gel2esw26kSyslogConf,'gel2esw26kServerMode':gel2esw26kServerMode,'gel2esw26kServerAddress1':gel2esw26kServerAddress1,'gel2esw26kServerAddress2':gel2esw26kServerAddress2,'gel2esw26kSyslogLevel':gel2esw26kSyslogLevel,'gel2esw26kSyslogDetailedInfo':gel2esw26kSyslogDetailedInfo,'gel2esw26kSyslogDetailedInfoClear':gel2esw26kSyslogDetailedInfoClear,'gel2esw26kSyslogDetailedInfoTable':gel2esw26kSyslogDetailedInfoTable,'gel2esw26kSyslogDetailedInfoEntry':gel2esw26kSyslogDetailedInfoEntry,_M:gel2esw26kSyslogDetailedInfoIndex,'gel2esw26kSyslogDetailedInfoLevel':gel2esw26kSyslogDetailedInfoLevel,'gel2esw26kSyslogDetailedInfoTime':gel2esw26kSyslogDetailedInfoTime,'gel2esw26kSyslogDetailedInfoMessage':gel2esw26kSyslogDetailedInfoMessage,'gel2esw26kSnmp':gel2esw26kSnmp,'gel2esw26kSnmpConf':gel2esw26kSnmpConf,'gel2esw26kGetCommunity':gel2esw26kGetCommunity,'gel2esw26kSetCommunityMode':gel2esw26kSetCommunityMode,'gel2esw26kSetCommunity':gel2esw26kSetCommunity,'gel2esw26kTrapHostConfTable':gel2esw26kTrapHostConfTable,'gel2esw26kTrapHostConfEntry':gel2esw26kTrapHostConfEntry,_N:gel2esw26kTrapHostConfIndex,'gel2esw26kTrapHostConfVersion':gel2esw26kTrapHostConfVersion,'gel2esw26kTrapHostConfIPType':gel2esw26kTrapHostConfIPType,'gel2esw26kTrapHostConfIP':gel2esw26kTrapHostConfIP,'gel2esw26kTrapHostConfPort':gel2esw26kTrapHostConfPort,'gel2esw26kTrapHostConfCommunity':gel2esw26kTrapHostConfCommunity,'gel2esw26kTrapHostConfSeverityLevel':gel2esw26kTrapHostConfSeverityLevel,'gel2esw26kTrapHostConfSecurityLevel':gel2esw26kTrapHostConfSecurityLevel,'gel2esw26kTrapHostConfAuthPtc':gel2esw26kTrapHostConfAuthPtc,'gel2esw26kTrapHostConfAuthPassword':gel2esw26kTrapHostConfAuthPassword,'gel2esw26kTrapHostConfPrivPtc':gel2esw26kTrapHostConfPrivPtc,'gel2esw26kTrapHostConfPrivPassword':gel2esw26kTrapHostConfPrivPassword,'gel2esw26kTrapHostConfCurrentMode':gel2esw26kTrapHostConfCurrentMode,'gel2esw26kConfiguration':gel2esw26kConfiguration,'gel2esw26kPort':gel2esw26kPort,'gel2esw26kPortConfigurationTable':gel2esw26kPortConfigurationTable,'gel2esw26kPortConfigurationEntry':gel2esw26kPortConfigurationEntry,_O:gel2esw26kPortConfPort,'gel2esw26kPortConfPortMedia':gel2esw26kPortConfPortMedia,'gel2esw26kPortConfLink':gel2esw26kPortConfLink,'gel2esw26kPortConfCurrentSpeed':gel2esw26kPortConfCurrentSpeed,'gel2esw26kPortConfSpeed':gel2esw26kPortConfSpeed,'gel2esw26kPortConfCurrentFlowControlRx':gel2esw26kPortConfCurrentFlowControlRx,'gel2esw26kPortConfCurrentFlowControlTx':gel2esw26kPortConfCurrentFlowControlTx,'gel2esw26kPortConfFlowControl':gel2esw26kPortConfFlowControl,'gel2esw26kPortConfMaxFrameSize':gel2esw26kPortConfMaxFrameSize,'gel2esw26kPortConfExcessiveCollisionMode':gel2esw26kPortConfExcessiveCollisionMode,'gel2esw26kPortConfPowerControl':gel2esw26kPortConfPowerControl,'gel2esw26kPortConfDescription':gel2esw26kPortConfDescription,'gel2esw26kPortTrafficStatisticsTable':gel2esw26kPortTrafficStatisticsTable,'gel2esw26kPortTrafficStatisticsEntry':gel2esw26kPortTrafficStatisticsEntry,_P:gel2esw26kPortTrafficStatisticsPort,'gel2esw26kPortTrafficStatisticsClear':gel2esw26kPortTrafficStatisticsClear,'gel2esw26kPortTrafficRxPackets':gel2esw26kPortTrafficRxPackets,'gel2esw26kPortTrafficRxOctets':gel2esw26kPortTrafficRxOctets,'gel2esw26kPortTrafficRxUnicast':gel2esw26kPortTrafficRxUnicast,'gel2esw26kPortTrafficRxMulticast':gel2esw26kPortTrafficRxMulticast,'gel2esw26kPortTrafficRxBroadcast':gel2esw26kPortTrafficRxBroadcast,'gel2esw26kPortTrafficRxPause':gel2esw26kPortTrafficRxPause,'gel2esw26kPortTrafficRx64Bytes':gel2esw26kPortTrafficRx64Bytes,'gel2esw26kPortTrafficRx65to127Bytes':gel2esw26kPortTrafficRx65to127Bytes,'gel2esw26kPortTrafficRx128to255Bytes':gel2esw26kPortTrafficRx128to255Bytes,'gel2esw26kPortTrafficRx256to511Bytes':gel2esw26kPortTrafficRx256to511Bytes,'gel2esw26kPortTrafficRx512to1023Bytes':gel2esw26kPortTrafficRx512to1023Bytes,'gel2esw26kPortTrafficRx1024to1526Bytes':gel2esw26kPortTrafficRx1024to1526Bytes,'gel2esw26kPortTrafficRxExceecd1527Bytes':gel2esw26kPortTrafficRxExceecd1527Bytes,'gel2esw26kPortTrafficRxQ0':gel2esw26kPortTrafficRxQ0,'gel2esw26kPortTrafficRxQ1':gel2esw26kPortTrafficRxQ1,'gel2esw26kPortTrafficRxQ2':gel2esw26kPortTrafficRxQ2,'gel2esw26kPortTrafficRxQ3':gel2esw26kPortTrafficRxQ3,'gel2esw26kPortTrafficRxQ4':gel2esw26kPortTrafficRxQ4,'gel2esw26kPortTrafficRxQ5':gel2esw26kPortTrafficRxQ5,'gel2esw26kPortTrafficRxQ6':gel2esw26kPortTrafficRxQ6,'gel2esw26kPortTrafficRxQ7':gel2esw26kPortTrafficRxQ7,'gel2esw26kPortTrafficRxDrops':gel2esw26kPortTrafficRxDrops,'gel2esw26kPortTrafficRxCRCorAlignment':gel2esw26kPortTrafficRxCRCorAlignment,'gel2esw26kPortTrafficRxUndersize':gel2esw26kPortTrafficRxUndersize,'gel2esw26kPortTrafficRxOversize':gel2esw26kPortTrafficRxOversize,'gel2esw26kPortTrafficRxFragments':gel2esw26kPortTrafficRxFragments,'gel2esw26kPortTrafficRxJabber':gel2esw26kPortTrafficRxJabber,'gel2esw26kPortTrafficRxFiltered':gel2esw26kPortTrafficRxFiltered,'gel2esw26kPortTrafficTxPackets':gel2esw26kPortTrafficTxPackets,'gel2esw26kPortTrafficTxOctets':gel2esw26kPortTrafficTxOctets,'gel2esw26kPortTrafficTxUnicast':gel2esw26kPortTrafficTxUnicast,'gel2esw26kPortTrafficTxMulticast':gel2esw26kPortTrafficTxMulticast,'gel2esw26kPortTrafficTxBroadcast':gel2esw26kPortTrafficTxBroadcast,'gel2esw26kPortTrafficTxPause':gel2esw26kPortTrafficTxPause,'gel2esw26kPortTrafficTx64Bytes':gel2esw26kPortTrafficTx64Bytes,'gel2esw26kPortTrafficTx65to127Bytes':gel2esw26kPortTrafficTx65to127Bytes,'gel2esw26kPortTrafficTx128to255Bytes':gel2esw26kPortTrafficTx128to255Bytes,'gel2esw26kPortTrafficTx256to511Bytes':gel2esw26kPortTrafficTx256to511Bytes,'gel2esw26kPortTrafficTx512to1023Bytes':gel2esw26kPortTrafficTx512to1023Bytes,'gel2esw26kPortTrafficTx1024to1526Bytes':gel2esw26kPortTrafficTx1024to1526Bytes,'gel2esw26kPortTrafficTxExceecd1527Bytes':gel2esw26kPortTrafficTxExceecd1527Bytes,'gel2esw26kPortTrafficTxQ0':gel2esw26kPortTrafficTxQ0,'gel2esw26kPortTrafficTxQ1':gel2esw26kPortTrafficTxQ1,'gel2esw26kPortTrafficTxQ2':gel2esw26kPortTrafficTxQ2,'gel2esw26kPortTrafficTxQ3':gel2esw26kPortTrafficTxQ3,'gel2esw26kPortTrafficTxQ4':gel2esw26kPortTrafficTxQ4,'gel2esw26kPortTrafficTxQ5':gel2esw26kPortTrafficTxQ5,'gel2esw26kPortTrafficTxQ6':gel2esw26kPortTrafficTxQ6,'gel2esw26kPortTrafficTxQ7':gel2esw26kPortTrafficTxQ7,'gel2esw26kPortTrafficTxDrops':gel2esw26kPortTrafficTxDrops,'gel2esw26kPortTrafficTxLateOrExcColl':gel2esw26kPortTrafficTxLateOrExcColl,'gel2esw26kPortQoSStatistics':gel2esw26kPortQoSStatistics,'gel2esw26kPortQoSStatisticsClear':gel2esw26kPortQoSStatisticsClear,'gel2esw26kPortQoSStatisticsTable':gel2esw26kPortQoSStatisticsTable,'gel2esw26kPortQoSStatisticsEntry':gel2esw26kPortQoSStatisticsEntry,_Q:gel2esw26kPortQoSStatisticsPort,'gel2esw26kPortQoSQ0Rx':gel2esw26kPortQoSQ0Rx,'gel2esw26kPortQoSQ0Tx':gel2esw26kPortQoSQ0Tx,'gel2esw26kPortQoSQ1Rx':gel2esw26kPortQoSQ1Rx,'gel2esw26kPortQoSQ1Tx':gel2esw26kPortQoSQ1Tx,'gel2esw26kPortQoSQ2Rx':gel2esw26kPortQoSQ2Rx,'gel2esw26kPortQoSQ2Tx':gel2esw26kPortQoSQ2Tx,'gel2esw26kPortQoSQ3Rx':gel2esw26kPortQoSQ3Rx,'gel2esw26kPortQoSQ3Tx':gel2esw26kPortQoSQ3Tx,'gel2esw26kPortQoSQ4Rx':gel2esw26kPortQoSQ4Rx,'gel2esw26kPortQoSQ4Tx':gel2esw26kPortQoSQ4Tx,'gel2esw26kPortQoSQ5Rx':gel2esw26kPortQoSQ5Rx,'gel2esw26kPortQoSQ5Tx':gel2esw26kPortQoSQ5Tx,'gel2esw26kPortQoSQ6Rx':gel2esw26kPortQoSQ6Rx,'gel2esw26kPortQoSQ6Tx':gel2esw26kPortQoSQ6Tx,'gel2esw26kPortQoSQ7Rx':gel2esw26kPortQoSQ7Rx,'gel2esw26kPortQoSQ7Tx':gel2esw26kPortQoSQ7Tx,'gel2esw26kSFPInfoTable':gel2esw26kSFPInfoTable,'gel2esw26kSFPInfoEntry':gel2esw26kSFPInfoEntry,_R:gel2esw26kSFPInfoIndex,'gel2esw26kSFPInfoPort':gel2esw26kSFPInfoPort,'gel2esw26kSFPConnectorType':gel2esw26kSFPConnectorType,'gel2esw26kSFPFiberType':gel2esw26kSFPFiberType,'gel2esw26kSFPTxCentralWavelength':gel2esw26kSFPTxCentralWavelength,'gel2esw26kSFPBaudRate':gel2esw26kSFPBaudRate,'gel2esw26kSFPVendorOUI':gel2esw26kSFPVendorOUI,'gel2esw26kSFPVendorName':gel2esw26kSFPVendorName,'gel2esw26kSFPVendorPN':gel2esw26kSFPVendorPN,'gel2esw26kSFPVendorRev':gel2esw26kSFPVendorRev,'gel2esw26kSFPVendorSN':gel2esw26kSFPVendorSN,'gel2esw26kSFPDateCode':gel2esw26kSFPDateCode,'gel2esw26kSFPTemperature':gel2esw26kSFPTemperature,'gel2esw26kSFPVcc':gel2esw26kSFPVcc,'gel2esw26kSFPMon1Bias':gel2esw26kSFPMon1Bias,'gel2esw26kSFPMon2TxPWR':gel2esw26kSFPMon2TxPWR,'gel2esw26kSFPMon3RxPWR':gel2esw26kSFPMon3RxPWR,'gel2esw26kPortEEETable':gel2esw26kPortEEETable,'gel2esw26kPortEEEEntry':gel2esw26kPortEEEEntry,_S:gel2esw26kPortEEEPort,'gel2esw26kPortEEEMode':gel2esw26kPortEEEMode,'gel2esw26kPortEEEUrgentQueue1':gel2esw26kPortEEEUrgentQueue1,'gel2esw26kPortEEEUrgentQueue2':gel2esw26kPortEEEUrgentQueue2,'gel2esw26kPortEEEUrgentQueue3':gel2esw26kPortEEEUrgentQueue3,'gel2esw26kPortEEEUrgentQueue4':gel2esw26kPortEEEUrgentQueue4,'gel2esw26kPortEEEUrgentQueue5':gel2esw26kPortEEEUrgentQueue5,'gel2esw26kPortEEEUrgentQueue6':gel2esw26kPortEEEUrgentQueue6,'gel2esw26kPortEEEUrgentQueue7':gel2esw26kPortEEEUrgentQueue7,'gel2esw26kPortEEEUrgentQueue8':gel2esw26kPortEEEUrgentQueue8,'gel2esw26kVoiceVLAN':gel2esw26kVoiceVLAN,'gel2esw26kVoiceVLANConf':gel2esw26kVoiceVLANConf,'gel2esw26kVoiceVLANMode':gel2esw26kVoiceVLANMode,'gel2esw26kVoiceVLANVLANId':gel2esw26kVoiceVLANVLANId,'gel2esw26kVoiceVLANAgingTime':gel2esw26kVoiceVLANAgingTime,'gel2esw26kVoiceVLANTrafficClass':gel2esw26kVoiceVLANTrafficClass,'gel2esw26kVoiceVLANPortTable':gel2esw26kVoiceVLANPortTable,'gel2esw26kVoiceVLANPortEntry':gel2esw26kVoiceVLANPortEntry,_T:gel2esw26kVoiceVLANPort,'gel2esw26kVoiceVLANPortMode':gel2esw26kVoiceVLANPortMode,'gel2esw26kVoiceVLANPortSecurity':gel2esw26kVoiceVLANPortSecurity,'gel2esw26kVoiceVLANPortDiscoveryProtocol':gel2esw26kVoiceVLANPortDiscoveryProtocol,'gel2esw26kVoiceVLANOUI':gel2esw26kVoiceVLANOUI,'gel2esw26kVoiceVLANOUICreate':gel2esw26kVoiceVLANOUICreate,'gel2esw26kVoiceVLANOUITable':gel2esw26kVoiceVLANOUITable,'gel2esw26kVoiceVLANOUIEntry':gel2esw26kVoiceVLANOUIEntry,_U:gel2esw26kVoiceVLANOUIIndex,'gel2esw26kVoiceVLANTelephonyOUI':gel2esw26kVoiceVLANTelephonyOUI,'gel2esw26kVoiceVLANDescription':gel2esw26kVoiceVLANDescription,'gel2esw26kVoiceVLANOUIRowStatus':gel2esw26kVoiceVLANOUIRowStatus,'gel2esw26kGARP':gel2esw26kGARP,'gel2esw26kGARPConfTable':gel2esw26kGARPConfTable,'gel2esw26kGARPConfEntry':gel2esw26kGARPConfEntry,_V:gel2esw26kGARPConfPort,'gel2esw26kGARPJoinTimer':gel2esw26kGARPJoinTimer,'gel2esw26kGARPLeaveTimer':gel2esw26kGARPLeaveTimer,'gel2esw26kGARPLeaveAllTimer':gel2esw26kGARPLeaveAllTimer,'gel2esw26kGARPApplicantion':gel2esw26kGARPApplicantion,'gel2esw26kGARPAttributeType':gel2esw26kGARPAttributeType,'gel2esw26kGARPApplicant':gel2esw26kGARPApplicant,'gel2esw26kGARPStatisticsTable':gel2esw26kGARPStatisticsTable,'gel2esw26kGARPStatisticsEntry':gel2esw26kGARPStatisticsEntry,_W:gel2esw26kGARPStatisticsPort,'gel2esw26kGARPStatisticsPeerMAC':gel2esw26kGARPStatisticsPeerMAC,'gel2esw26kGARPStatisticsFailedCount':gel2esw26kGARPStatisticsFailedCount,'gel2esw26kGVRP':gel2esw26kGVRP,'gel2esw26kGVRPConf':gel2esw26kGVRPConf,'gel2esw26kGVRPMode':gel2esw26kGVRPMode,'gel2esw26kGVRPConfTable':gel2esw26kGVRPConfTable,'gel2esw26kGVRPConfEntry':gel2esw26kGVRPConfEntry,_X:gel2esw26kGVRPConfPort,'gel2esw26kGVRPConfPortMode':gel2esw26kGVRPConfPortMode,'gel2esw26kGVRPConfPortRRole':gel2esw26kGVRPConfPortRRole,'gel2esw26kGVRPStatisticsTable':gel2esw26kGVRPStatisticsTable,'gel2esw26kGVRPStatisticsEntry':gel2esw26kGVRPStatisticsEntry,_Y:gel2esw26kGVRPStatisticsPort,'gel2esw26kGVRPStatisticsJoinTxCnt':gel2esw26kGVRPStatisticsJoinTxCnt,'gel2esw26kGVRPStatisticsLeaveTxCnt':gel2esw26kGVRPStatisticsLeaveTxCnt,'gel2esw26kMirroring':gel2esw26kMirroring,'gel2esw26kPortToMirrorOn':gel2esw26kPortToMirrorOn,'gel2esw26kMirrorTable':gel2esw26kMirrorTable,'gel2esw26kMirrorEntry':gel2esw26kMirrorEntry,_Z:gel2esw26kMirrorPort,'gel2esw26kMirrorMode':gel2esw26kMirrorMode,'gel2esw26kTrapEventSeverity':gel2esw26kTrapEventSeverity,'gel2esw26kTrapEventSeverityACL':gel2esw26kTrapEventSeverityACL,'gel2esw26kTrapEventSeverityACLLog':gel2esw26kTrapEventSeverityACLLog,'gel2esw26kTrapEventSeverityAccessMgmt':gel2esw26kTrapEventSeverityAccessMgmt,'gel2esw26kTrapEventSeverityAuthFailed':gel2esw26kTrapEventSeverityAuthFailed,'gel2esw26kTrapEventSeverityColdStart':gel2esw26kTrapEventSeverityColdStart,'gel2esw26kTrapEventSeverityConfigInfo':gel2esw26kTrapEventSeverityConfigInfo,'gel2esw26kTrapEventSeverityFirmwareUpgrade':gel2esw26kTrapEventSeverityFirmwareUpgrade,'gel2esw26kTrapEventSeverityImportExport':gel2esw26kTrapEventSeverityImportExport,'gel2esw26kTrapEventSeverityLACP':gel2esw26kTrapEventSeverityLACP,'gel2esw26kTrapEventSeverityLinkStatus':gel2esw26kTrapEventSeverityLinkStatus,'gel2esw26kTrapEventSeverityLogin':gel2esw26kTrapEventSeverityLogin,'gel2esw26kTrapEventSeverityLogout':gel2esw26kTrapEventSeverityLogout,'gel2esw26kTrapEventSeverityLoopProtect':gel2esw26kTrapEventSeverityLoopProtect,'gel2esw26kTrapEventSeverityMgmtIPChange':gel2esw26kTrapEventSeverityMgmtIPChange,'gel2esw26kTrapEventSeverityModuleChange':gel2esw26kTrapEventSeverityModuleChange,'gel2esw26kTrapEventSeverityNAS':gel2esw26kTrapEventSeverityNAS,'gel2esw26kTrapEventSeverityPasswordChange':gel2esw26kTrapEventSeverityPasswordChange,'gel2esw26kTrapEventSeverityPortSecurity':gel2esw26kTrapEventSeverityPortSecurity,'gel2esw26kTrapEventSeverityThermalProtect':gel2esw26kTrapEventSeverityThermalProtect,'gel2esw26kTrapEventSeverityVLAN':gel2esw26kTrapEventSeverityVLAN,'gel2esw26kTrapEventSeverityWarmStart':gel2esw26kTrapEventSeverityWarmStart,'gel2esw26kSMTP':gel2esw26kSMTP,'gel2esw26kSMTPMailServer':gel2esw26kSMTPMailServer,'gel2esw26kSMTPUserName':gel2esw26kSMTPUserName,'gel2esw26kSMTPPassword':gel2esw26kSMTPPassword,'gel2esw26kSMTPServeriryLevel':gel2esw26kSMTPServeriryLevel,'gel2esw26kSMTPSender':gel2esw26kSMTPSender,'gel2esw26kSMTPReturnPath':gel2esw26kSMTPReturnPath,'gel2esw26kSMTPEmailAddress1':gel2esw26kSMTPEmailAddress1,'gel2esw26kSMTPEmailAddress2':gel2esw26kSMTPEmailAddress2,'gel2esw26kSMTPEmailAddress3':gel2esw26kSMTPEmailAddress3,'gel2esw26kSMTPEmailAddress4':gel2esw26kSMTPEmailAddress4,'gel2esw26kSMTPEmailAddress5':gel2esw26kSMTPEmailAddress5,'gel2esw26kSMTPEmailAddress6':gel2esw26kSMTPEmailAddress6,'gel2esw26kACL':gel2esw26kACL,'gel2esw26kACLPortsConfTable':gel2esw26kACLPortsConfTable,'gel2esw26kACLPortsConfEntry':gel2esw26kACLPortsConfEntry,_a:gel2esw26kACLPortsConfPort,'gel2esw26kACLPortsConfPolicyID':gel2esw26kACLPortsConfPolicyID,'gel2esw26kACLPortsConfAction':gel2esw26kACLPortsConfAction,'gel2esw26kACLPortsConfRateLimiterID':gel2esw26kACLPortsConfRateLimiterID,'gel2esw26kACLPortsConfPortRedirect':gel2esw26kACLPortsConfPortRedirect,'gel2esw26kACLPortsConfMirror':gel2esw26kACLPortsConfMirror,'gel2esw26kACLPortsConfLogging':gel2esw26kACLPortsConfLogging,'gel2esw26kACLPortsConfShutdown':gel2esw26kACLPortsConfShutdown,'gel2esw26kACLPortsConfState':gel2esw26kACLPortsConfState,'gel2esw26kACLPortsConfCounter':gel2esw26kACLPortsConfCounter,'gel2esw26kACLRateLimiterTable':gel2esw26kACLRateLimiterTable,'gel2esw26kACLRateLimiterEntry':gel2esw26kACLRateLimiterEntry,_b:gel2esw26kACLRateLimiterID,'gel2esw26kACLRateLimiterUnit':gel2esw26kACLRateLimiterUnit,'gel2esw26kACLRateLimiterRate':gel2esw26kACLRateLimiterRate,'gel2esw26kACLACE':gel2esw26kACLACE,'gel2esw26kACLACECreate':gel2esw26kACLACECreate,'gel2esw26kACLACETable':gel2esw26kACLACETable,'gel2esw26kACLACEEntry':gel2esw26kACLACEEntry,_c:gel2esw26kACLACEIndex,'gel2esw26kACLACEID':gel2esw26kACLACEID,'gel2esw26kACLACENextID':gel2esw26kACLACENextID,'gel2esw26kACLACEIngressPort':gel2esw26kACLACEIngressPort,'gel2esw26kACLACEPortPolicyNumber':gel2esw26kACLACEPortPolicyNumber,'gel2esw26kACLACEPortPolicyBitmask':gel2esw26kACLACEPortPolicyBitmask,'gel2esw26kACLACEFrameType':gel2esw26kACLACEFrameType,'gel2esw26kACLACEAction':gel2esw26kACLACEAction,'gel2esw26kACLACEDenyPortRedirect':gel2esw26kACLACEDenyPortRedirect,'gel2esw26kACLACELogging':gel2esw26kACLACELogging,'gel2esw26kACLACEMirror':gel2esw26kACLACEMirror,'gel2esw26kACLACERateLimiter':gel2esw26kACLACERateLimiter,'gel2esw26kACLACEShutdown':gel2esw26kACLACEShutdown,'gel2esw26kACLACEVLAN8021QTagged':gel2esw26kACLACEVLAN8021QTagged,'gel2esw26kACLACEVLANTagPriority':gel2esw26kACLACEVLANTagPriority,'gel2esw26kACLACEVLANVID':gel2esw26kACLACEVLANVID,'gel2esw26kACLACEEtherType':gel2esw26kACLACEEtherType,'gel2esw26kACLACESMAC':gel2esw26kACLACESMAC,'gel2esw26kACLACEDMACType':gel2esw26kACLACEDMACType,'gel2esw26kACLACEDMAC':gel2esw26kACLACEDMAC,'gel2esw26kACLACEArpOpcode':gel2esw26kACLACEArpOpcode,'gel2esw26kACLACEArpFlagsRequestReply':gel2esw26kACLACEArpFlagsRequestReply,'gel2esw26kACLACEArpFlagsArpSmac':gel2esw26kACLACEArpFlagsArpSmac,'gel2esw26kACLACEArpFlagsRarpDmac':gel2esw26kACLACEArpFlagsRarpDmac,'gel2esw26kACLACEArpFlagsLength':gel2esw26kACLACEArpFlagsLength,'gel2esw26kACLACEArpFlagsIp':gel2esw26kACLACEArpFlagsIp,'gel2esw26kACLACEArpFlagsEthernet':gel2esw26kACLACEArpFlagsEthernet,'gel2esw26kACLACESIPType':gel2esw26kACLACESIPType,'gel2esw26kACLACESIPIPAddress':gel2esw26kACLACESIPIPAddress,'gel2esw26kACLACESIPNetworkPrefix':gel2esw26kACLACESIPNetworkPrefix,'gel2esw26kACLACEDIPType':gel2esw26kACLACEDIPType,'gel2esw26kACLACEDIPIPAddress':gel2esw26kACLACEDIPIPAddress,'gel2esw26kACLACEDIPNetworkPrefix':gel2esw26kACLACEDIPNetworkPrefix,'gel2esw26kACLACEIPProtocol':gel2esw26kACLACEIPProtocol,'gel2esw26kACLACEIPFlagsTTL':gel2esw26kACLACEIPFlagsTTL,'gel2esw26kACLACEIPFlagsOptions':gel2esw26kACLACEIPFlagsOptions,'gel2esw26kACLACEIPFlagsFragment':gel2esw26kACLACEIPFlagsFragment,'gel2esw26kACLACEICMPType':gel2esw26kACLACEICMPType,'gel2esw26kACLACEICMPCode':gel2esw26kACLACEICMPCode,'gel2esw26kACLACESourcePortMin':gel2esw26kACLACESourcePortMin,'gel2esw26kACLACESourcePortMax':gel2esw26kACLACESourcePortMax,'gel2esw26kACLACEDestPortMin':gel2esw26kACLACEDestPortMin,'gel2esw26kACLACEDestPortMax':gel2esw26kACLACEDestPortMax,'gel2esw26kACLACETCPFlagsFin':gel2esw26kACLACETCPFlagsFin,'gel2esw26kACLACETCPFlagsSyn':gel2esw26kACLACETCPFlagsSyn,'gel2esw26kACLACETCPFlagsRst':gel2esw26kACLACETCPFlagsRst,'gel2esw26kACLACETCPFlagsPsh':gel2esw26kACLACETCPFlagsPsh,'gel2esw26kACLACETCPFlagsAck':gel2esw26kACLACETCPFlagsAck,'gel2esw26kACLACETCPFlagsUrg':gel2esw26kACLACETCPFlagsUrg,'gel2esw26kACLACERowStatus':gel2esw26kACLACERowStatus,'gel2esw26kACLACEClear':gel2esw26kACLACEClear,'gel2esw26kACLACEMoveACEID':gel2esw26kACLACEMoveACEID,'gel2esw26kACLACEMoveNextACEID':gel2esw26kACLACEMoveNextACEID,'gel2esw26kACLACEStatusTable':gel2esw26kACLACEStatusTable,'gel2esw26kACLACEStatusEntry':gel2esw26kACLACEStatusEntry,_d:gel2esw26kACLACEStatusIndex,'gel2esw26kACLACEStatusUser':gel2esw26kACLACEStatusUser,'gel2esw26kACLACEStatusID':gel2esw26kACLACEStatusID,'gel2esw26kACLACEStatusIngressPort':gel2esw26kACLACEStatusIngressPort,'gel2esw26kACLACEStatusFrameType':gel2esw26kACLACEStatusFrameType,'gel2esw26kACLACEStatusAction':gel2esw26kACLACEStatusAction,'gel2esw26kACLACEStatusRateLimiter':gel2esw26kACLACEStatusRateLimiter,'gel2esw26kACLACEStatusPortCopy':gel2esw26kACLACEStatusPortCopy,'gel2esw26kACLACEStatusMirror':gel2esw26kACLACEStatusMirror,'gel2esw26kACLACEStatusCPU':gel2esw26kACLACEStatusCPU,'gel2esw26kACLACEStatusCounter':gel2esw26kACLACEStatusCounter,'gel2esw26kACLACEStatusConflict':gel2esw26kACLACEStatusConflict,'gel2esw26kLoopProtection':gel2esw26kLoopProtection,'gel2esw26kLoopProtectionConfig':gel2esw26kLoopProtectionConfig,'gel2esw26kLoopProtectionGlobalEnable':gel2esw26kLoopProtectionGlobalEnable,'gel2esw26kLoopProtectionTranmisstionTime':gel2esw26kLoopProtectionTranmisstionTime,'gel2esw26kLoopProtectionShutdownTime':gel2esw26kLoopProtectionShutdownTime,'gel2esw26kLoopProtectionConfigurationTable':gel2esw26kLoopProtectionConfigurationTable,'gel2esw26kLoopProtectionConfigurationEntry':gel2esw26kLoopProtectionConfigurationEntry,_e:gel2esw26kLoopProtectionConfPort,'gel2esw26kLoopProtectionConfEnable':gel2esw26kLoopProtectionConfEnable,'gel2esw26kLoopProtectionConfAction':gel2esw26kLoopProtectionConfAction,'gel2esw26kLoopProtectionConfTxmode':gel2esw26kLoopProtectionConfTxmode,'gel2esw26kLoopProtectionStatusTable':gel2esw26kLoopProtectionStatusTable,'gel2esw26kLoopProtectionStatusEntry':gel2esw26kLoopProtectionStatusEntry,_f:gel2esw26kLoopProtectionStatusPort,'gel2esw26kLoopProtectionStatusAction':gel2esw26kLoopProtectionStatusAction,'gel2esw26kLoopProtectionStatusTransmit':gel2esw26kLoopProtectionStatusTransmit,'gel2esw26kLoopProtectionStatusLoops':gel2esw26kLoopProtectionStatusLoops,'gel2esw26kLoopProtectionStatusStatus':gel2esw26kLoopProtectionStatusStatus,'gel2esw26kLoopProtectionStatusLoop':gel2esw26kLoopProtectionStatusLoop,'gel2esw26kLoopProtectionStatusTimeLastLoop':gel2esw26kLoopProtectionStatusTimeLastLoop,'gel2esw26kSecurity':gel2esw26kSecurity,'gel2esw26kIPSourceGuard':gel2esw26kIPSourceGuard,'gel2esw26kIPSourceGuardConf':gel2esw26kIPSourceGuardConf,'gel2esw26kIPSourceGuardMode':gel2esw26kIPSourceGuardMode,'gel2esw26kIPSourceGuardPortConfigTable':gel2esw26kIPSourceGuardPortConfigTable,'gel2esw26kIPSourceGuardPortConfigEntry':gel2esw26kIPSourceGuardPortConfigEntry,_g:gel2esw26kIPSourceGuardPortConfigPort,'gel2esw26kIPSourceGuardPortConfigMode':gel2esw26kIPSourceGuardPortConfigMode,'gel2esw26kIPSourceGuardPortMaxDynamicClients':gel2esw26kIPSourceGuardPortMaxDynamicClients,'gel2esw26kIPSourceGuardStatic':gel2esw26kIPSourceGuardStatic,'gel2esw26kIPSourceGuardStaticCreate':gel2esw26kIPSourceGuardStaticCreate,'gel2esw26kIPSourceGuardStaticTable':gel2esw26kIPSourceGuardStaticTable,'gel2esw26kIPSourceGuardStaticEntry':gel2esw26kIPSourceGuardStaticEntry,_h:gel2esw26kIPSourceGuardStaticIndex,'gel2esw26kIPSourceGuardStaticPort':gel2esw26kIPSourceGuardStaticPort,'gel2esw26kIPSourceGuardStaticVLANId':gel2esw26kIPSourceGuardStaticVLANId,'gel2esw26kIPSourceGuardStaticIPAddress':gel2esw26kIPSourceGuardStaticIPAddress,'gel2esw26kIPSourceGuardStaticMACAddress':gel2esw26kIPSourceGuardStaticMACAddress,'gel2esw26kIPSourceGuardStaticRowStatus':gel2esw26kIPSourceGuardStaticRowStatus,'gel2esw26kIPSourceGuardDynamicTable':gel2esw26kIPSourceGuardDynamicTable,'gel2esw26kIPSourceGuardDynamicEntry':gel2esw26kIPSourceGuardDynamicEntry,_i:gel2esw26kIPSourceGuardDynamicIndex,'gel2esw26kIPSourceGuardDynamicPort':gel2esw26kIPSourceGuardDynamicPort,'gel2esw26kIPSourceGuardDynamicVLANId':gel2esw26kIPSourceGuardDynamicVLANId,'gel2esw26kIPSourceGuardDynamicIPAddress':gel2esw26kIPSourceGuardDynamicIPAddress,'gel2esw26kIPSourceGuardDynamicMACAddress':gel2esw26kIPSourceGuardDynamicMACAddress,'gel2esw26kARPInspection':gel2esw26kARPInspection,'gel2esw26kARPInspectionConf':gel2esw26kARPInspectionConf,'gel2esw26kARPInspectionConfMode':gel2esw26kARPInspectionConfMode,'gel2esw26kARPInspectionConfTable':gel2esw26kARPInspectionConfTable,'gel2esw26kARPInspectionConfEntry':gel2esw26kARPInspectionConfEntry,_j:gel2esw26kARPInspectionConfPortIndex,'gel2esw26kARPInspectionConfPortMode':gel2esw26kARPInspectionConfPortMode,'gel2esw26kARPInspectionStatic':gel2esw26kARPInspectionStatic,'gel2esw26kARPInspectionStaticCreate':gel2esw26kARPInspectionStaticCreate,'gel2esw26kARPInspectionStaticTable':gel2esw26kARPInspectionStaticTable,'gel2esw26kARPInspectionStaticEntry':gel2esw26kARPInspectionStaticEntry,_k:gel2esw26kARPInspectionStaticIndex,'gel2esw26kARPInspectionStaticPort':gel2esw26kARPInspectionStaticPort,'gel2esw26kARPInspectionStaticVLANId':gel2esw26kARPInspectionStaticVLANId,'gel2esw26kARPInspectionStaticIPAddress':gel2esw26kARPInspectionStaticIPAddress,'gel2esw26kARPInspectionStaticMACAddress':gel2esw26kARPInspectionStaticMACAddress,'gel2esw26kARPInspectionStaticRowStatus':gel2esw26kARPInspectionStaticRowStatus,'gel2esw26kARPInspectionDynamicTable':gel2esw26kARPInspectionDynamicTable,'gel2esw26kARPInspectionDynamicEntry':gel2esw26kARPInspectionDynamicEntry,_l:gel2esw26kARPInspectionDynamicIndex,'gel2esw26kARPInspectionDynamicPort':gel2esw26kARPInspectionDynamicPort,'gel2esw26kARPInspectionDynamicVLANId':gel2esw26kARPInspectionDynamicVLANId,'gel2esw26kARPInspectionDynamicIPAddress':gel2esw26kARPInspectionDynamicIPAddress,'gel2esw26kARPInspectionDynamicMACAddress':gel2esw26kARPInspectionDynamicMACAddress,'gel2esw26kDHCPSnooping':gel2esw26kDHCPSnooping,'gel2esw26kDHCPSnoopingConf':gel2esw26kDHCPSnoopingConf,'gel2esw26kDHCPSnoopingMode':gel2esw26kDHCPSnoopingMode,'gel2esw26kDHCPSnoopingPortModeConfigurationTable':gel2esw26kDHCPSnoopingPortModeConfigurationTable,'gel2esw26kDHCPSnoopingPortModeConfigurationEntry':gel2esw26kDHCPSnoopingPortModeConfigurationEntry,_m:gel2esw26kDHCPSnoopingPortModeConfigurationPort,'gel2esw26kDHCPSnoopingPortModeConfigurationMode':gel2esw26kDHCPSnoopingPortModeConfigurationMode,'gel2esw26kDHCPSnoopingStatisticsTable':gel2esw26kDHCPSnoopingStatisticsTable,'gel2esw26kDHCPSnoopingStatisticsEntry':gel2esw26kDHCPSnoopingStatisticsEntry,_n:gel2esw26kDHCPSnoopingStatisticsPort,'gel2esw26kDHCPSnoopingStatisticsClear':gel2esw26kDHCPSnoopingStatisticsClear,'gel2esw26kDHCPSnoopingRxDiscover':gel2esw26kDHCPSnoopingRxDiscover,'gel2esw26kDHCPSnoopingRxOffer':gel2esw26kDHCPSnoopingRxOffer,'gel2esw26kDHCPSnoopingRxRequest':gel2esw26kDHCPSnoopingRxRequest,'gel2esw26kDHCPSnoopingRxDecline':gel2esw26kDHCPSnoopingRxDecline,'gel2esw26kDHCPSnoopingRxACK':gel2esw26kDHCPSnoopingRxACK,'gel2esw26kDHCPSnoopingRxNAK':gel2esw26kDHCPSnoopingRxNAK,'gel2esw26kDHCPSnoopingRxRelease':gel2esw26kDHCPSnoopingRxRelease,'gel2esw26kDHCPSnoopingRxInform':gel2esw26kDHCPSnoopingRxInform,'gel2esw26kDHCPSnoopingRxLeaseQuery':gel2esw26kDHCPSnoopingRxLeaseQuery,'gel2esw26kDHCPSnoopingRxLeaseUnassigned':gel2esw26kDHCPSnoopingRxLeaseUnassigned,'gel2esw26kDHCPSnoopingRxLeaseUnknown':gel2esw26kDHCPSnoopingRxLeaseUnknown,'gel2esw26kDHCPSnoopingRxLeaseActive':gel2esw26kDHCPSnoopingRxLeaseActive,'gel2esw26kDHCPSnoopingTxDiscover':gel2esw26kDHCPSnoopingTxDiscover,'gel2esw26kDHCPSnoopingTxOffer':gel2esw26kDHCPSnoopingTxOffer,'gel2esw26kDHCPSnoopingTxRequest':gel2esw26kDHCPSnoopingTxRequest,'gel2esw26kDHCPSnoopingTxDecline':gel2esw26kDHCPSnoopingTxDecline,'gel2esw26kDHCPSnoopingTxACK':gel2esw26kDHCPSnoopingTxACK,'gel2esw26kDHCPSnoopingTxNAK':gel2esw26kDHCPSnoopingTxNAK,'gel2esw26kDHCPSnoopingTxRelease':gel2esw26kDHCPSnoopingTxRelease,'gel2esw26kDHCPSnoopingTxInform':gel2esw26kDHCPSnoopingTxInform,'gel2esw26kDHCPSnoopingTxLeaseQuery':gel2esw26kDHCPSnoopingTxLeaseQuery,'gel2esw26kDHCPSnoopingTxLeaseUnassigned':gel2esw26kDHCPSnoopingTxLeaseUnassigned,'gel2esw26kDHCPSnoopingTxLeaseUnknown':gel2esw26kDHCPSnoopingTxLeaseUnknown,'gel2esw26kDHCPSnoopingTxLeaseActive':gel2esw26kDHCPSnoopingTxLeaseActive,'gel2esw26kDHCPRelay':gel2esw26kDHCPRelay,'gel2esw26kDHCPRelayConfiguration':gel2esw26kDHCPRelayConfiguration,'gel2esw26kDHCPRelayMode':gel2esw26kDHCPRelayMode,'gel2esw26kDHCPRelayServer':gel2esw26kDHCPRelayServer,'gel2esw26kDHCPRelayInformationMode':gel2esw26kDHCPRelayInformationMode,'gel2esw26kDHCPRelayInformationPolicy':gel2esw26kDHCPRelayInformationPolicy,'gel2esw26kDHCPRelayStatistics':gel2esw26kDHCPRelayStatistics,'gel2esw26kDHCPRelayServerStatistics':gel2esw26kDHCPRelayServerStatistics,'gel2esw26kServerStatTransmitToServer':gel2esw26kServerStatTransmitToServer,'gel2esw26kServerStatTransmitError':gel2esw26kServerStatTransmitError,'gel2esw26kServerStatReceiveFromServer':gel2esw26kServerStatReceiveFromServer,'gel2esw26kServerStatReceiveMissingAgentOption':gel2esw26kServerStatReceiveMissingAgentOption,'gel2esw26kServerStatReceiveMissingCircuitID':gel2esw26kServerStatReceiveMissingCircuitID,'gel2esw26kServerStatReceiveMissingRemoteID':gel2esw26kServerStatReceiveMissingRemoteID,'gel2esw26kServerStatReceiveBadCircuitID':gel2esw26kServerStatReceiveBadCircuitID,'gel2esw26kServerStatReceiveBadRemoteID':gel2esw26kServerStatReceiveBadRemoteID,'gel2esw26kDHCPRelayClientStatistics':gel2esw26kDHCPRelayClientStatistics,'gel2esw26kClientStatTransmitToClient':gel2esw26kClientStatTransmitToClient,'gel2esw26kClientStatTransmitError':gel2esw26kClientStatTransmitError,'gel2esw26kClientStatReceivefromClient':gel2esw26kClientStatReceivefromClient,'gel2esw26kClientStatReceiveAgentOption':gel2esw26kClientStatReceiveAgentOption,'gel2esw26kClientStatReplaceAgentOption':gel2esw26kClientStatReplaceAgentOption,'gel2esw26kClientStatKeepAgentOption':gel2esw26kClientStatKeepAgentOption,'gel2esw26kClientStatDropAgentOption':gel2esw26kClientStatDropAgentOption,'gel2esw26kPortSecurity':gel2esw26kPortSecurity,'gel2esw26kPortSecLimitCtrl':gel2esw26kPortSecLimitCtrl,'gel2esw26kPortSecLimitCtrlSystemConf':gel2esw26kPortSecLimitCtrlSystemConf,'gel2esw26kPortSecurityMode':gel2esw26kPortSecurityMode,'gel2esw26kPortSecurityAging':gel2esw26kPortSecurityAging,'gel2esw26kPortSecurityAgingPeriod':gel2esw26kPortSecurityAgingPeriod,'gel2esw26kPortSecLimitCtrlTable':gel2esw26kPortSecLimitCtrlTable,'gel2esw26kPortSecLimitCtrlEntry':gel2esw26kPortSecLimitCtrlEntry,_o:gel2esw26kPortSecLimitCtrlPort,'gel2esw26kPortSecLimitCtrlPortMode':gel2esw26kPortSecLimitCtrlPortMode,'gel2esw26kPortSecLimitCtrlPortLimit':gel2esw26kPortSecLimitCtrlPortLimit,'gel2esw26kPortSecLimitCtrlPortAction':gel2esw26kPortSecLimitCtrlPortAction,'gel2esw26kPortSecLimitCtrlPortState':gel2esw26kPortSecLimitCtrlPortState,'gel2esw26kPortSecLimitCtrlPortReOpen':gel2esw26kPortSecLimitCtrlPortReOpen,'gel2esw26kPortSecSwitchStatusTable':gel2esw26kPortSecSwitchStatusTable,'gel2esw26kPortSecSwitchStatusEntry':gel2esw26kPortSecSwitchStatusEntry,_p:gel2esw26kPortSecSwitchStatusPort,'gel2esw26kPortSecSwitchStatusUsers':gel2esw26kPortSecSwitchStatusUsers,'gel2esw26kPortSecSwitchStatusState':gel2esw26kPortSecSwitchStatusState,'gel2esw26kPortSecSwitchStatusMACCountCurrent':gel2esw26kPortSecSwitchStatusMACCountCurrent,'gel2esw26kPortSecSwitchStatusMACCountLimit':gel2esw26kPortSecSwitchStatusMACCountLimit,'gel2esw26kPortSecPortStatus':gel2esw26kPortSecPortStatus,'gel2esw26kPortSecPortStatusPort':gel2esw26kPortSecPortStatusPort,'gel2esw26kPortSecPortStatusTable':gel2esw26kPortSecPortStatusTable,'gel2esw26kPortSecPortStatusEntry':gel2esw26kPortSecPortStatusEntry,_q:gel2esw26kPortSecPortStatusIndex,'gel2esw26kPortSecPortStatusMACAddress':gel2esw26kPortSecPortStatusMACAddress,'gel2esw26kPortSecPortStatusVLANId':gel2esw26kPortSecPortStatusVLANId,'gel2esw26kPortSecPortStatusState':gel2esw26kPortSecPortStatusState,'gel2esw26kPortSecPortStatusTimeOfAddition':gel2esw26kPortSecPortStatusTimeOfAddition,'gel2esw26kPortSecPortStatusAgeAndHold':gel2esw26kPortSecPortStatusAgeAndHold,'gel2esw26kAccessManagement':gel2esw26kAccessManagement,'gel2esw26kAccessMgtConf':gel2esw26kAccessMgtConf,'gel2esw26kAccessMgtConfMode':gel2esw26kAccessMgtConfMode,'gel2esw26kAccessMgtConfCreate':gel2esw26kAccessMgtConfCreate,'gel2esw26kAccessMgtConfTable':gel2esw26kAccessMgtConfTable,'gel2esw26kAccessMgtConfEntry':gel2esw26kAccessMgtConfEntry,_r:gel2esw26kAccessMgtIndex,'gel2esw26kAccessMgtAddresstype':gel2esw26kAccessMgtAddresstype,'gel2esw26kAccessMgtStartIpAddress':gel2esw26kAccessMgtStartIpAddress,'gel2esw26kAccessMgtEndIpAddress':gel2esw26kAccessMgtEndIpAddress,'gel2esw26kAccessMgtHttpHttps':gel2esw26kAccessMgtHttpHttps,'gel2esw26kAccessMgtSNMP':gel2esw26kAccessMgtSNMP,'gel2esw26kAccessMgtTelnetSSH':gel2esw26kAccessMgtTelnetSSH,'gel2esw26kAccessMgtRowStatus':gel2esw26kAccessMgtRowStatus,'gel2esw26kAccessMgtStatistics':gel2esw26kAccessMgtStatistics,'gel2esw26kHttpReceivedPkts':gel2esw26kHttpReceivedPkts,'gel2esw26kHttpAllowedPkts':gel2esw26kHttpAllowedPkts,'gel2esw26kHttpDiscardedPkts':gel2esw26kHttpDiscardedPkts,'gel2esw26kHttpsReceivedPkts':gel2esw26kHttpsReceivedPkts,'gel2esw26kHttpsAllowedPkts':gel2esw26kHttpsAllowedPkts,'gel2esw26kHttpsDiscardedPkts':gel2esw26kHttpsDiscardedPkts,'gel2esw26kSnmpReceivedPkts':gel2esw26kSnmpReceivedPkts,'gel2esw26kSnmpAllowedPkts':gel2esw26kSnmpAllowedPkts,'gel2esw26kSnmpDiscardedPkts':gel2esw26kSnmpDiscardedPkts,'gel2esw26kTelnetReceivedPkts':gel2esw26kTelnetReceivedPkts,'gel2esw26kTelnetAllowedPkts':gel2esw26kTelnetAllowedPkts,'gel2esw26kTelnetDiscardedPkts':gel2esw26kTelnetDiscardedPkts,'gel2esw26kSSHReceivedPkts':gel2esw26kSSHReceivedPkts,'gel2esw26kSSHAllowedPkts':gel2esw26kSSHAllowedPkts,'gel2esw26kSSHDiscardedPkts':gel2esw26kSSHDiscardedPkts,'gel2esw26kAccessMgtStatisticsClearAll':gel2esw26kAccessMgtStatisticsClearAll,'gel2esw26kSSH':gel2esw26kSSH,'gel2esw26kSSHMode':gel2esw26kSSHMode,'gel2esw26kHTTPS':gel2esw26kHTTPS,'gel2esw26kHTTPSMode':gel2esw26kHTTPSMode,'gel2esw26kHTTPSAutoRedirect':gel2esw26kHTTPSAutoRedirect,'gel2esw26kAuthMethod':gel2esw26kAuthMethod,'gel2esw26kConsoleAuthMethod':gel2esw26kConsoleAuthMethod,'gel2esw26kConsoleFallback':gel2esw26kConsoleFallback,'gel2esw26kTelnetAuthMethod':gel2esw26kTelnetAuthMethod,'gel2esw26kTelnetFallback':gel2esw26kTelnetFallback,'gel2esw26kSshAuthMethod':gel2esw26kSshAuthMethod,'gel2esw26kSshFallback':gel2esw26kSshFallback,'gel2esw26kWebAuthMethod':gel2esw26kWebAuthMethod,'gel2esw26kWebFallback':gel2esw26kWebFallback,'gel2esw26kMaintenance':gel2esw26kMaintenance,'gel2esw26kRestartDevice':gel2esw26kRestartDevice,'gel2esw26kFirmware':gel2esw26kFirmware,'gel2esw26kFirmwareIpAddress':gel2esw26kFirmwareIpAddress,'gel2esw26kFirmwareFileName':gel2esw26kFirmwareFileName,'gel2esw26kDoFirmwareUpgrade':gel2esw26kDoFirmwareUpgrade,'gel2esw26kSaveOrRestore':gel2esw26kSaveOrRestore,'gel2esw26kFactoryDefaults':gel2esw26kFactoryDefaults,'gel2esw26kSaveStart':gel2esw26kSaveStart,'gel2esw26kSaveUser':gel2esw26kSaveUser,'gel2esw26kRestoreUser':gel2esw26kRestoreUser,'gel2esw26kExportOrImport':gel2esw26kExportOrImport,'gel2esw26kExportIpAddress':gel2esw26kExportIpAddress,'gel2esw26kExportConfigName':gel2esw26kExportConfigName,'gel2esw26kDoExportConfig':gel2esw26kDoExportConfig,'gel2esw26kImportIpAddress':gel2esw26kImportIpAddress,'gel2esw26kImportConfigName':gel2esw26kImportConfigName,'gel2esw26kDoImportConfig':gel2esw26kDoImportConfig,'gel2esw26kDiagnostics':gel2esw26kDiagnostics,'gel2esw26kPingIpAddress':gel2esw26kPingIpAddress,'gel2esw26kPingSize':gel2esw26kPingSize,'gel2esw26kDoPingConfig':gel2esw26kDoPingConfig,'gel2esw26kPingResult':gel2esw26kPingResult,'gel2esw26kPing6IpAddress':gel2esw26kPing6IpAddress,'gel2esw26kPing6Size':gel2esw26kPing6Size,'gel2esw26kDoPing6Config':gel2esw26kDoPing6Config,'gel2esw26kPing6Result':gel2esw26kPing6Result,'gel2esw26kVeriPHY':gel2esw26kVeriPHY,'gel2esw26kVeriPHYTest':gel2esw26kVeriPHYTest,'gel2esw26kVeriPHYTable':gel2esw26kVeriPHYTable,'gel2esw26kVeriPHYEntry':gel2esw26kVeriPHYEntry,_s:gel2esw26kVeriPHYPort,'gel2esw26kVeriPHYPairA':gel2esw26kVeriPHYPairA,'gel2esw26kVeriPHYLengthA':gel2esw26kVeriPHYLengthA,'gel2esw26kVeriPHYPairB':gel2esw26kVeriPHYPairB,'gel2esw26kVeriPHYLengthB':gel2esw26kVeriPHYLengthB,'gel2esw26kVeriPHYPairC':gel2esw26kVeriPHYPairC,'gel2esw26kVeriPHYLengthC':gel2esw26kVeriPHYLengthC,'gel2esw26kVeriPHYPairD':gel2esw26kVeriPHYPairD,'gel2esw26kVeriPHYLengthD':gel2esw26kVeriPHYLengthD,'gel2esw26kTrap':gel2esw26kTrap,'gel2esw26kTrapEvent':gel2esw26kTrapEvent,'gel2esw26kEmergency':gel2esw26kEmergency,'gel2esw26kAlert':gel2esw26kAlert,'gel2esw26kCritical':gel2esw26kCritical,'gel2esw26kError':gel2esw26kError,'gel2esw26kWarning':gel2esw26kWarning,'gel2esw26kNotice':gel2esw26kNotice,'gel2esw26kInformational':gel2esw26kInformational,'gel2esw26kDebug':gel2esw26kDebug,'gel2esw26kTrapVariable':gel2esw26kTrapVariable,_H:gel2esw26kInformation})