_At='opmen99810bAccessMgtIndex'
_As='opmen99810bPortSecPortStatusIndex'
_Ar='opmen99810bPortSecSwitchStatusPort'
_Aq='opmen99810bPortSecLimitCtrlPort'
_Ap='opmen99810bDHCPSnoopingStatisticsPort'
_Ao='opmen99810bDHCPSnoopingPortModeConfigurationPort'
_An='opmen99810bARPInspectionDynamicIndex'
_Am='opmen99810bARPInspectionStaticIndex'
_Al='opmen99810bARPInspectionConfPortIndex'
_Ak='opmen99810bIPSourceGuardDynamicIndex'
_Aj='opmen99810bIPSourceGuardStaticIndex'
_Ai='opmen99810bIPSourceGuardPortConfigPort'
_Ah='opmen99810bVlanPortsPort'
_Ag='opmen99810bQosQCLStatusList'
_Af='opmen99810bQosQceIndex'
_Ae='opmen99810bQosDSCPClassificationDPL'
_Ad='opmen99810bQosDSCPClassificationQoSClass'
_Ac='opmen99810bQosDSCPTranslationList'
_Ab='opmen99810bQosDSCPList'
_Aa='opmen99810bQosPortDSCPPort'
_AZ='opmen99810bQosTagRemarkingDPLevel'
_AY='opmen99810bQosTagRemarkingQoSClass'
_AX='opmen99810bQosPortEgressTagRemarkingMapPort'
_AW='opmen99810bQosEgressTagRemarkingDefPort'
_AV='opmen99810bQosEgressTagRemarkingPort'
_AU='opmen99810bQosSchedulerPortQueue'
_AT='opmen99810bQosSchedulerPort'
_AS='opmen99810bQosSchedulerModePort'
_AR='opmen99810bQosPortPolicingPort'
_AQ='opmen99810bQoSIngressPortTagDEI'
_AP='opmen99810bQoSIngressPortTagPCP'
_AO='opmen99810bQoSIngressPortTagClassificationPort'
_AN='opmen99810bQosPortClassificationPort'
_AM='opmen99810bLoopProtectionStatusPort'
_AL='opmen99810bLoopProtectionConfPort'
_AK='opmen99810bBroadcastStormProtectionConfPort'
_AJ='opmen99810bACLACEStatusIndex'
_AI='opmen99810bACLACEIndex'
_AH='opmen99810bACLRateLimiterID'
_AG='opmen99810bACLPortsConfPort'
_AF='opmen99810bMirrorPort'
_AE='opmen99810bGVRPStatisticsPort'
_AD='opmen99810bGVRPConfPort'
_AC='opmen99810bGARPStatisticsPort'
_AB='opmen99810bGARPConfPort'
_AA='opmen99810bVoiceVLANOUIIndex'
_A9='opmen99810bVoiceVLANPort'
_A8='opmen99810bPortEEEPort'
_A7='opmen99810bSFPInfoIndex'
_A6='opmen99810bPortQoSStatisticsPort'
_A5='opmen99810bPortTrafficStatisticsPort'
_A4='opmen99810bPortConfPort'
_A3='opmen99810bTrapHostConfIndex'
_A2='opmen99810bSyslogDetailedInfoIndex'
_A1='opmen99810bUserIndex'
_A0='opmen99810bSystemTimeNTPIndex'
_z='fourthWeek'
_y='thirdWeek'
_x='secondWeek'
_w='firstWeek'
_v='saturday'
_u='friday'
_t='thursday'
_s='wednesday'
_r='tuseday'
_q='monday'
_p='sunday'
_o='MacAddress'
_n='OctetString'
_m='tacacsplus'
_l='radius'
_k='local'
_j='ipv6'
_i='do'
_h='doNothing'
_g='yes'
_f='noSupport'
_e='clear'
_d='ipv4'
_c='undo'
_b='edit'
_a='set'
_Z='unset'
_Y='destroy'
_X='notInservice'
_W='create'
_V='opmen99810bInformation'
_U='active'
_T='noData'
_S='DisplayString'
_R='any'
_Q='none'
_P='debug'
_O='info'
_N='notice'
_M='warning'
_L='error'
_K='critical'
_J='alert'
_I='emergency'
_H='not-accessible'
_G='PRIVATETECH-OP-MEN99810B-MIB'
_F='enable'
_E='disable'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_n,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MacAddress,=mibBuilder.importSymbols('BRIDGE-MIB',_o)
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_S,_o,'PhysAddress','TextualConvention')
privatetech=ModuleIdentity((1,3,6,1,4,1,5205))
_Switch_ObjectIdentity=ObjectIdentity
switch=_Switch_ObjectIdentity((1,3,6,1,4,1,5205,2))
_Opmen99810bProductId_ObjectIdentity=ObjectIdentity
opmen99810bProductId=_Opmen99810bProductId_ObjectIdentity((1,3,6,1,4,1,5205,2,94))
_Opmen99810bSystem_ObjectIdentity=ObjectIdentity
opmen99810bSystem=_Opmen99810bSystem_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1))
_Opmen99810bSystemInformation_ObjectIdentity=ObjectIdentity
opmen99810bSystemInformation=_Opmen99810bSystemInformation_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,1))
_Opmen99810bModelName_Type=DisplayString
_Opmen99810bModelName_Object=MibScalar
opmen99810bModelName=_Opmen99810bModelName_Object((1,3,6,1,4,1,5205,2,94,1,1,1),_Opmen99810bModelName_Type())
opmen99810bModelName.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bModelName.setStatus(_A)
_Opmen99810bBIOSVersion_Type=DisplayString
_Opmen99810bBIOSVersion_Object=MibScalar
opmen99810bBIOSVersion=_Opmen99810bBIOSVersion_Object((1,3,6,1,4,1,5205,2,94,1,1,2),_Opmen99810bBIOSVersion_Type())
opmen99810bBIOSVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bBIOSVersion.setStatus(_A)
_Opmen99810bFirmwareVersion_Type=DisplayString
_Opmen99810bFirmwareVersion_Object=MibScalar
opmen99810bFirmwareVersion=_Opmen99810bFirmwareVersion_Object((1,3,6,1,4,1,5205,2,94,1,1,3),_Opmen99810bFirmwareVersion_Type())
opmen99810bFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bFirmwareVersion.setStatus(_A)
_Opmen99810bHardwareMechanicalVersion_Type=DisplayString
_Opmen99810bHardwareMechanicalVersion_Object=MibScalar
opmen99810bHardwareMechanicalVersion=_Opmen99810bHardwareMechanicalVersion_Object((1,3,6,1,4,1,5205,2,94,1,1,4),_Opmen99810bHardwareMechanicalVersion_Type())
opmen99810bHardwareMechanicalVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bHardwareMechanicalVersion.setStatus(_A)
_Opmen99810bSerialNumber_Type=DisplayString
_Opmen99810bSerialNumber_Object=MibScalar
opmen99810bSerialNumber=_Opmen99810bSerialNumber_Object((1,3,6,1,4,1,5205,2,94,1,1,5),_Opmen99810bSerialNumber_Type())
opmen99810bSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSerialNumber.setStatus(_A)
_Opmen99810bHostMACAddress_Type=MacAddress
_Opmen99810bHostMACAddress_Object=MibScalar
opmen99810bHostMACAddress=_Opmen99810bHostMACAddress_Object((1,3,6,1,4,1,5205,2,94,1,1,6),_Opmen99810bHostMACAddress_Type())
opmen99810bHostMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bHostMACAddress.setStatus(_A)
_Opmen99810bConsoleBaudrate_Type=DisplayString
_Opmen99810bConsoleBaudrate_Object=MibScalar
opmen99810bConsoleBaudrate=_Opmen99810bConsoleBaudrate_Object((1,3,6,1,4,1,5205,2,94,1,1,7),_Opmen99810bConsoleBaudrate_Type())
opmen99810bConsoleBaudrate.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bConsoleBaudrate.setStatus(_A)
_Opmen99810bRAMSize_Type=DisplayString
_Opmen99810bRAMSize_Object=MibScalar
opmen99810bRAMSize=_Opmen99810bRAMSize_Object((1,3,6,1,4,1,5205,2,94,1,1,8),_Opmen99810bRAMSize_Type())
opmen99810bRAMSize.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bRAMSize.setStatus(_A)
_Opmen99810bFlashSize_Type=DisplayString
_Opmen99810bFlashSize_Object=MibScalar
opmen99810bFlashSize=_Opmen99810bFlashSize_Object((1,3,6,1,4,1,5205,2,94,1,1,9),_Opmen99810bFlashSize_Type())
opmen99810bFlashSize.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bFlashSize.setStatus(_A)
_Opmen99810bBridgeFBDSize_Type=DisplayString
_Opmen99810bBridgeFBDSize_Object=MibScalar
opmen99810bBridgeFBDSize=_Opmen99810bBridgeFBDSize_Object((1,3,6,1,4,1,5205,2,94,1,1,10),_Opmen99810bBridgeFBDSize_Type())
opmen99810bBridgeFBDSize.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bBridgeFBDSize.setStatus(_A)
_Opmen99810bTransmitQueue_Type=DisplayString
_Opmen99810bTransmitQueue_Object=MibScalar
opmen99810bTransmitQueue=_Opmen99810bTransmitQueue_Object((1,3,6,1,4,1,5205,2,94,1,1,11),_Opmen99810bTransmitQueue_Type())
opmen99810bTransmitQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bTransmitQueue.setStatus(_A)
_Opmen99810bMaximumFrameSize_Type=DisplayString
_Opmen99810bMaximumFrameSize_Object=MibScalar
opmen99810bMaximumFrameSize=_Opmen99810bMaximumFrameSize_Object((1,3,6,1,4,1,5205,2,94,1,1,12),_Opmen99810bMaximumFrameSize_Type())
opmen99810bMaximumFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bMaximumFrameSize.setStatus(_A)
_Opmen99810bCPULoad_Type=DisplayString
_Opmen99810bCPULoad_Object=MibScalar
opmen99810bCPULoad=_Opmen99810bCPULoad_Object((1,3,6,1,4,1,5205,2,94,1,1,13),_Opmen99810bCPULoad_Type())
opmen99810bCPULoad.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bCPULoad.setStatus(_A)
_Opmen99810bPowerSource_Type=DisplayString
_Opmen99810bPowerSource_Object=MibScalar
opmen99810bPowerSource=_Opmen99810bPowerSource_Object((1,3,6,1,4,1,5205,2,94,1,1,14),_Opmen99810bPowerSource_Type())
opmen99810bPowerSource.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPowerSource.setStatus(_A)
_Opmen99810bSystemTime_ObjectIdentity=ObjectIdentity
opmen99810bSystemTime=_Opmen99810bSystemTime_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,2))
_Opmen99810bSystemTimeManual_ObjectIdentity=ObjectIdentity
opmen99810bSystemTimeManual=_Opmen99810bSystemTimeManual_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,2,1))
class _Opmen99810bSystemTimeManualClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('useLocal',0),('useNTP',1)))
_Opmen99810bSystemTimeManualClockSource_Type.__name__=_C
_Opmen99810bSystemTimeManualClockSource_Object=MibScalar
opmen99810bSystemTimeManualClockSource=_Opmen99810bSystemTimeManualClockSource_Object((1,3,6,1,4,1,5205,2,94,1,2,1,1),_Opmen99810bSystemTimeManualClockSource_Type())
opmen99810bSystemTimeManualClockSource.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualClockSource.setStatus(_A)
_Opmen99810bSystemTimeManualLocaltime_Type=DisplayString
_Opmen99810bSystemTimeManualLocaltime_Object=MibScalar
opmen99810bSystemTimeManualLocaltime=_Opmen99810bSystemTimeManualLocaltime_Object((1,3,6,1,4,1,5205,2,94,1,2,1,2),_Opmen99810bSystemTimeManualLocaltime_Type())
opmen99810bSystemTimeManualLocaltime.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualLocaltime.setStatus(_A)
class _Opmen99810bSystemTimeManualTimeZoneOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-720,780))
_Opmen99810bSystemTimeManualTimeZoneOffset_Type.__name__=_C
_Opmen99810bSystemTimeManualTimeZoneOffset_Object=MibScalar
opmen99810bSystemTimeManualTimeZoneOffset=_Opmen99810bSystemTimeManualTimeZoneOffset_Object((1,3,6,1,4,1,5205,2,94,1,2,1,3),_Opmen99810bSystemTimeManualTimeZoneOffset_Type())
opmen99810bSystemTimeManualTimeZoneOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualTimeZoneOffset.setStatus(_A)
class _Opmen99810bSystemTimeManualDaylightSavings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bSystemTimeManualDaylightSavings_Type.__name__=_C
_Opmen99810bSystemTimeManualDaylightSavings_Object=MibScalar
opmen99810bSystemTimeManualDaylightSavings=_Opmen99810bSystemTimeManualDaylightSavings_Object((1,3,6,1,4,1,5205,2,94,1,2,1,4),_Opmen99810bSystemTimeManualDaylightSavings_Type())
opmen99810bSystemTimeManualDaylightSavings.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualDaylightSavings.setStatus(_A)
class _Opmen99810bSystemTimeManualTimeSetOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_Opmen99810bSystemTimeManualTimeSetOffset_Type.__name__=_C
_Opmen99810bSystemTimeManualTimeSetOffset_Object=MibScalar
opmen99810bSystemTimeManualTimeSetOffset=_Opmen99810bSystemTimeManualTimeSetOffset_Object((1,3,6,1,4,1,5205,2,94,1,2,1,5),_Opmen99810bSystemTimeManualTimeSetOffset_Type())
opmen99810bSystemTimeManualTimeSetOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualTimeSetOffset.setStatus(_A)
class _Opmen99810bSystemTimeManualDaylightSavingsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('byDates',0),('recurring',1)))
_Opmen99810bSystemTimeManualDaylightSavingsType_Type.__name__=_C
_Opmen99810bSystemTimeManualDaylightSavingsType_Object=MibScalar
opmen99810bSystemTimeManualDaylightSavingsType=_Opmen99810bSystemTimeManualDaylightSavingsType_Object((1,3,6,1,4,1,5205,2,94,1,2,1,6),_Opmen99810bSystemTimeManualDaylightSavingsType_Type())
opmen99810bSystemTimeManualDaylightSavingsType.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualDaylightSavingsType.setStatus(_A)
_Opmen99810bSystemTimeManualDaylightSavingsBydatesFrom_Type=DisplayString
_Opmen99810bSystemTimeManualDaylightSavingsBydatesFrom_Object=MibScalar
opmen99810bSystemTimeManualDaylightSavingsBydatesFrom=_Opmen99810bSystemTimeManualDaylightSavingsBydatesFrom_Object((1,3,6,1,4,1,5205,2,94,1,2,1,7),_Opmen99810bSystemTimeManualDaylightSavingsBydatesFrom_Type())
opmen99810bSystemTimeManualDaylightSavingsBydatesFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualDaylightSavingsBydatesFrom.setStatus(_A)
_Opmen99810bSystemTimeManualDaylightSavingsBydatesTo_Type=DisplayString
_Opmen99810bSystemTimeManualDaylightSavingsBydatesTo_Object=MibScalar
opmen99810bSystemTimeManualDaylightSavingsBydatesTo=_Opmen99810bSystemTimeManualDaylightSavingsBydatesTo_Object((1,3,6,1,4,1,5205,2,94,1,2,1,8),_Opmen99810bSystemTimeManualDaylightSavingsBydatesTo_Type())
opmen99810bSystemTimeManualDaylightSavingsBydatesTo.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualDaylightSavingsBydatesTo.setStatus(_A)
class _Opmen99810bSystemTimeManualDaylightSavingsRecurringDayFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_p,0),(_q,1),(_r,2),(_s,3),(_t,4),(_u,5),(_v,6)))
_Opmen99810bSystemTimeManualDaylightSavingsRecurringDayFrom_Type.__name__=_C
_Opmen99810bSystemTimeManualDaylightSavingsRecurringDayFrom_Object=MibScalar
opmen99810bSystemTimeManualDaylightSavingsRecurringDayFrom=_Opmen99810bSystemTimeManualDaylightSavingsRecurringDayFrom_Object((1,3,6,1,4,1,5205,2,94,1,2,1,9),_Opmen99810bSystemTimeManualDaylightSavingsRecurringDayFrom_Type())
opmen99810bSystemTimeManualDaylightSavingsRecurringDayFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualDaylightSavingsRecurringDayFrom.setStatus(_A)
class _Opmen99810bSystemTimeManualDaylightSavingsRecurringWeekFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_w,1),(_x,2),(_y,3),(_z,4),('listWeek',5)))
_Opmen99810bSystemTimeManualDaylightSavingsRecurringWeekFrom_Type.__name__=_C
_Opmen99810bSystemTimeManualDaylightSavingsRecurringWeekFrom_Object=MibScalar
opmen99810bSystemTimeManualDaylightSavingsRecurringWeekFrom=_Opmen99810bSystemTimeManualDaylightSavingsRecurringWeekFrom_Object((1,3,6,1,4,1,5205,2,94,1,2,1,10),_Opmen99810bSystemTimeManualDaylightSavingsRecurringWeekFrom_Type())
opmen99810bSystemTimeManualDaylightSavingsRecurringWeekFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualDaylightSavingsRecurringWeekFrom.setStatus(_A)
class _Opmen99810bSystemTimeManualDaylightSavingsRecurringMonthFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('jan',1),('feb',2),('mar',3),('apr',4),('may',5),('jun',6),('jul',7),('aug',8),('sep',9),('oct',10),('nov',11),('dec',12)))
_Opmen99810bSystemTimeManualDaylightSavingsRecurringMonthFrom_Type.__name__=_C
_Opmen99810bSystemTimeManualDaylightSavingsRecurringMonthFrom_Object=MibScalar
opmen99810bSystemTimeManualDaylightSavingsRecurringMonthFrom=_Opmen99810bSystemTimeManualDaylightSavingsRecurringMonthFrom_Object((1,3,6,1,4,1,5205,2,94,1,2,1,11),_Opmen99810bSystemTimeManualDaylightSavingsRecurringMonthFrom_Type())
opmen99810bSystemTimeManualDaylightSavingsRecurringMonthFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualDaylightSavingsRecurringMonthFrom.setStatus(_A)
_Opmen99810bSystemTimeManualDaylightSavingsRecurringTimeFrom_Type=DisplayString
_Opmen99810bSystemTimeManualDaylightSavingsRecurringTimeFrom_Object=MibScalar
opmen99810bSystemTimeManualDaylightSavingsRecurringTimeFrom=_Opmen99810bSystemTimeManualDaylightSavingsRecurringTimeFrom_Object((1,3,6,1,4,1,5205,2,94,1,2,1,12),_Opmen99810bSystemTimeManualDaylightSavingsRecurringTimeFrom_Type())
opmen99810bSystemTimeManualDaylightSavingsRecurringTimeFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualDaylightSavingsRecurringTimeFrom.setStatus(_A)
class _Opmen99810bSystemTimeManualDaylightSavingsRecurringDayTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_p,0),(_q,1),(_r,2),(_s,3),(_t,4),(_u,5),(_v,6)))
_Opmen99810bSystemTimeManualDaylightSavingsRecurringDayTo_Type.__name__=_C
_Opmen99810bSystemTimeManualDaylightSavingsRecurringDayTo_Object=MibScalar
opmen99810bSystemTimeManualDaylightSavingsRecurringDayTo=_Opmen99810bSystemTimeManualDaylightSavingsRecurringDayTo_Object((1,3,6,1,4,1,5205,2,94,1,2,1,13),_Opmen99810bSystemTimeManualDaylightSavingsRecurringDayTo_Type())
opmen99810bSystemTimeManualDaylightSavingsRecurringDayTo.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualDaylightSavingsRecurringDayTo.setStatus(_A)
class _Opmen99810bSystemTimeManualDaylightSavingsRecurringWeekTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_w,1),(_x,2),(_y,3),(_z,4),('listWeek',5)))
_Opmen99810bSystemTimeManualDaylightSavingsRecurringWeekTo_Type.__name__=_C
_Opmen99810bSystemTimeManualDaylightSavingsRecurringWeekTo_Object=MibScalar
opmen99810bSystemTimeManualDaylightSavingsRecurringWeekTo=_Opmen99810bSystemTimeManualDaylightSavingsRecurringWeekTo_Object((1,3,6,1,4,1,5205,2,94,1,2,1,14),_Opmen99810bSystemTimeManualDaylightSavingsRecurringWeekTo_Type())
opmen99810bSystemTimeManualDaylightSavingsRecurringWeekTo.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualDaylightSavingsRecurringWeekTo.setStatus(_A)
class _Opmen99810bSystemTimeManualDaylightSavingsRecurringMonthTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('jan',1),('feb',2),('mar',3),('apr',4),('may',5),('jun',6),('jul',7),('aug',8),('sep',9),('oct',10),('nov',11),('dec',12)))
_Opmen99810bSystemTimeManualDaylightSavingsRecurringMonthTo_Type.__name__=_C
_Opmen99810bSystemTimeManualDaylightSavingsRecurringMonthTo_Object=MibScalar
opmen99810bSystemTimeManualDaylightSavingsRecurringMonthTo=_Opmen99810bSystemTimeManualDaylightSavingsRecurringMonthTo_Object((1,3,6,1,4,1,5205,2,94,1,2,1,15),_Opmen99810bSystemTimeManualDaylightSavingsRecurringMonthTo_Type())
opmen99810bSystemTimeManualDaylightSavingsRecurringMonthTo.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualDaylightSavingsRecurringMonthTo.setStatus(_A)
_Opmen99810bSystemTimeManualDaylightSavingsRecurringTimeTo_Type=DisplayString
_Opmen99810bSystemTimeManualDaylightSavingsRecurringTimeTo_Object=MibScalar
opmen99810bSystemTimeManualDaylightSavingsRecurringTimeTo=_Opmen99810bSystemTimeManualDaylightSavingsRecurringTimeTo_Object((1,3,6,1,4,1,5205,2,94,1,2,1,16),_Opmen99810bSystemTimeManualDaylightSavingsRecurringTimeTo_Type())
opmen99810bSystemTimeManualDaylightSavingsRecurringTimeTo.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeManualDaylightSavingsRecurringTimeTo.setStatus(_A)
_Opmen99810bSystemTimeNTP_ObjectIdentity=ObjectIdentity
opmen99810bSystemTimeNTP=_Opmen99810bSystemTimeNTP_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,2,2))
_Opmen99810bSystemTimeNTPTable_Object=MibTable
opmen99810bSystemTimeNTPTable=_Opmen99810bSystemTimeNTPTable_Object((1,3,6,1,4,1,5205,2,94,1,2,2,1))
if mibBuilder.loadTexts:opmen99810bSystemTimeNTPTable.setStatus(_A)
_Opmen99810bSystemTimeNTPEntry_Object=MibTableRow
opmen99810bSystemTimeNTPEntry=_Opmen99810bSystemTimeNTPEntry_Object((1,3,6,1,4,1,5205,2,94,1,2,2,1,1))
opmen99810bSystemTimeNTPEntry.setIndexNames((0,_G,_A0))
if mibBuilder.loadTexts:opmen99810bSystemTimeNTPEntry.setStatus(_A)
class _Opmen99810bSystemTimeNTPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Opmen99810bSystemTimeNTPIndex_Type.__name__=_C
_Opmen99810bSystemTimeNTPIndex_Object=MibTableColumn
opmen99810bSystemTimeNTPIndex=_Opmen99810bSystemTimeNTPIndex_Object((1,3,6,1,4,1,5205,2,94,1,2,2,1,1,1),_Opmen99810bSystemTimeNTPIndex_Type())
opmen99810bSystemTimeNTPIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bSystemTimeNTPIndex.setStatus(_A)
class _Opmen99810bSystemTimeNTPServerIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_d,0),(_j,1)))
_Opmen99810bSystemTimeNTPServerIPType_Type.__name__=_C
_Opmen99810bSystemTimeNTPServerIPType_Object=MibTableColumn
opmen99810bSystemTimeNTPServerIPType=_Opmen99810bSystemTimeNTPServerIPType_Object((1,3,6,1,4,1,5205,2,94,1,2,2,1,1,2),_Opmen99810bSystemTimeNTPServerIPType_Type())
opmen99810bSystemTimeNTPServerIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeNTPServerIPType.setStatus(_A)
_Opmen99810bSystemTimeNTPServer_Type=DisplayString
_Opmen99810bSystemTimeNTPServer_Object=MibTableColumn
opmen99810bSystemTimeNTPServer=_Opmen99810bSystemTimeNTPServer_Object((1,3,6,1,4,1,5205,2,94,1,2,2,1,1,3),_Opmen99810bSystemTimeNTPServer_Type())
opmen99810bSystemTimeNTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeNTPServer.setStatus(_A)
class _Opmen99810bSystemTimeNTPCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('empty',0),(_U,1),(_b,2),('delete',3)))
_Opmen99810bSystemTimeNTPCurrentMode_Type.__name__=_C
_Opmen99810bSystemTimeNTPCurrentMode_Object=MibTableColumn
opmen99810bSystemTimeNTPCurrentMode=_Opmen99810bSystemTimeNTPCurrentMode_Object((1,3,6,1,4,1,5205,2,94,1,2,2,1,1,4),_Opmen99810bSystemTimeNTPCurrentMode_Type())
opmen99810bSystemTimeNTPCurrentMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemTimeNTPCurrentMode.setStatus(_A)
_Opmen99810bSystemAccount_ObjectIdentity=ObjectIdentity
opmen99810bSystemAccount=_Opmen99810bSystemAccount_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,3))
_Opmen99810bSystemAccountUsers_ObjectIdentity=ObjectIdentity
opmen99810bSystemAccountUsers=_Opmen99810bSystemAccountUsers_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,3,1))
class _Opmen99810bSystemAccountUserCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_W,1)))
_Opmen99810bSystemAccountUserCreate_Type.__name__=_C
_Opmen99810bSystemAccountUserCreate_Object=MibScalar
opmen99810bSystemAccountUserCreate=_Opmen99810bSystemAccountUserCreate_Object((1,3,6,1,4,1,5205,2,94,1,3,1,1),_Opmen99810bSystemAccountUserCreate_Type())
opmen99810bSystemAccountUserCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemAccountUserCreate.setStatus(_A)
_Opmen99810bSystemAccountUsersTable_Object=MibTable
opmen99810bSystemAccountUsersTable=_Opmen99810bSystemAccountUsersTable_Object((1,3,6,1,4,1,5205,2,94,1,3,1,2))
if mibBuilder.loadTexts:opmen99810bSystemAccountUsersTable.setStatus(_A)
_Opmen99810bSystemAccountUsersEntry_Object=MibTableRow
opmen99810bSystemAccountUsersEntry=_Opmen99810bSystemAccountUsersEntry_Object((1,3,6,1,4,1,5205,2,94,1,3,1,2,1))
opmen99810bSystemAccountUsersEntry.setIndexNames((0,_G,_A1))
if mibBuilder.loadTexts:opmen99810bSystemAccountUsersEntry.setStatus(_A)
class _Opmen99810bUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_Opmen99810bUserIndex_Type.__name__=_C
_Opmen99810bUserIndex_Object=MibTableColumn
opmen99810bUserIndex=_Opmen99810bUserIndex_Object((1,3,6,1,4,1,5205,2,94,1,3,1,2,1,1),_Opmen99810bUserIndex_Type())
opmen99810bUserIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bUserIndex.setStatus(_A)
class _Opmen99810bUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Opmen99810bUserName_Type.__name__=_S
_Opmen99810bUserName_Object=MibTableColumn
opmen99810bUserName=_Opmen99810bUserName_Object((1,3,6,1,4,1,5205,2,94,1,3,1,2,1,2),_Opmen99810bUserName_Type())
opmen99810bUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bUserName.setStatus(_A)
class _Opmen99810bPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Opmen99810bPassword_Type.__name__=_S
_Opmen99810bPassword_Object=MibTableColumn
opmen99810bPassword=_Opmen99810bPassword_Object((1,3,6,1,4,1,5205,2,94,1,3,1,2,1,3),_Opmen99810bPassword_Type())
opmen99810bPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPassword.setStatus(_A)
class _Opmen99810bUserPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bUserPrivilegeLevel_Type.__name__=_C
_Opmen99810bUserPrivilegeLevel_Object=MibTableColumn
opmen99810bUserPrivilegeLevel=_Opmen99810bUserPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,1,2,1,4),_Opmen99810bUserPrivilegeLevel_Type())
opmen99810bUserPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bUserPrivilegeLevel.setStatus(_A)
class _Opmen99810bAccountUserRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),(_X,2),(_b,3),(_Y,4),(_c,5)))
_Opmen99810bAccountUserRowStatus_Type.__name__=_C
_Opmen99810bAccountUserRowStatus_Object=MibTableColumn
opmen99810bAccountUserRowStatus=_Opmen99810bAccountUserRowStatus_Object((1,3,6,1,4,1,5205,2,94,1,3,1,2,1,5),_Opmen99810bAccountUserRowStatus_Type())
opmen99810bAccountUserRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bAccountUserRowStatus.setStatus(_A)
_Opmen99810bSystemAccountPrivilegeLevel_ObjectIdentity=ObjectIdentity
opmen99810bSystemAccountPrivilegeLevel=_Opmen99810bSystemAccountPrivilegeLevel_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,3,2))
class _Opmen99810bAccountPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bAccountPrivilegeLevel_Type.__name__=_C
_Opmen99810bAccountPrivilegeLevel_Object=MibScalar
opmen99810bAccountPrivilegeLevel=_Opmen99810bAccountPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,1),_Opmen99810bAccountPrivilegeLevel_Type())
opmen99810bAccountPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bAccountPrivilegeLevel.setStatus(_A)
class _Opmen99810bAggregationPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bAggregationPrivilegeLevel_Type.__name__=_C
_Opmen99810bAggregationPrivilegeLevel_Object=MibScalar
opmen99810bAggregationPrivilegeLevel=_Opmen99810bAggregationPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,2),_Opmen99810bAggregationPrivilegeLevel_Type())
opmen99810bAggregationPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bAggregationPrivilegeLevel.setStatus(_A)
class _Opmen99810bDiagnosticsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bDiagnosticsPrivilegeLevel_Type.__name__=_C
_Opmen99810bDiagnosticsPrivilegeLevel_Object=MibScalar
opmen99810bDiagnosticsPrivilegeLevel=_Opmen99810bDiagnosticsPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,3),_Opmen99810bDiagnosticsPrivilegeLevel_Type())
opmen99810bDiagnosticsPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bDiagnosticsPrivilegeLevel.setStatus(_A)
class _Opmen99810bEEEPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bEEEPrivilegeLevel_Type.__name__=_C
_Opmen99810bEEEPrivilegeLevel_Object=MibScalar
opmen99810bEEEPrivilegeLevel=_Opmen99810bEEEPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,4),_Opmen99810bEEEPrivilegeLevel_Type())
opmen99810bEEEPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bEEEPrivilegeLevel.setStatus(_A)
class _Opmen99810bEasyportPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bEasyportPrivilegeLevel_Type.__name__=_C
_Opmen99810bEasyportPrivilegeLevel_Object=MibScalar
opmen99810bEasyportPrivilegeLevel=_Opmen99810bEasyportPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,9),_Opmen99810bEasyportPrivilegeLevel_Type())
opmen99810bEasyportPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bEasyportPrivilegeLevel.setStatus(_A)
class _Opmen99810bGARPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bGARPPrivilegeLevel_Type.__name__=_C
_Opmen99810bGARPPrivilegeLevel_Object=MibScalar
opmen99810bGARPPrivilegeLevel=_Opmen99810bGARPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,10),_Opmen99810bGARPPrivilegeLevel_Type())
opmen99810bGARPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bGARPPrivilegeLevel.setStatus(_A)
class _Opmen99810bGVRPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bGVRPPrivilegeLevel_Type.__name__=_C
_Opmen99810bGVRPPrivilegeLevel_Object=MibScalar
opmen99810bGVRPPrivilegeLevel=_Opmen99810bGVRPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,11),_Opmen99810bGVRPPrivilegeLevel_Type())
opmen99810bGVRPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bGVRPPrivilegeLevel.setStatus(_A)
class _Opmen99810bIPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bIPPrivilegeLevel_Type.__name__=_C
_Opmen99810bIPPrivilegeLevel_Object=MibScalar
opmen99810bIPPrivilegeLevel=_Opmen99810bIPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,12),_Opmen99810bIPPrivilegeLevel_Type())
opmen99810bIPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPPrivilegeLevel.setStatus(_A)
class _Opmen99810bIPMCSnoopingPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bIPMCSnoopingPrivilegeLevel_Type.__name__=_C
_Opmen99810bIPMCSnoopingPrivilegeLevel_Object=MibScalar
opmen99810bIPMCSnoopingPrivilegeLevel=_Opmen99810bIPMCSnoopingPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,13),_Opmen99810bIPMCSnoopingPrivilegeLevel_Type())
opmen99810bIPMCSnoopingPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPMCSnoopingPrivilegeLevel.setStatus(_A)
class _Opmen99810bLACPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bLACPPrivilegeLevel_Type.__name__=_C
_Opmen99810bLACPPrivilegeLevel_Object=MibScalar
opmen99810bLACPPrivilegeLevel=_Opmen99810bLACPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,14),_Opmen99810bLACPPrivilegeLevel_Type())
opmen99810bLACPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bLACPPrivilegeLevel.setStatus(_A)
class _Opmen99810bLLDPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bLLDPPrivilegeLevel_Type.__name__=_C
_Opmen99810bLLDPPrivilegeLevel_Object=MibScalar
opmen99810bLLDPPrivilegeLevel=_Opmen99810bLLDPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,15),_Opmen99810bLLDPPrivilegeLevel_Type())
opmen99810bLLDPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bLLDPPrivilegeLevel.setStatus(_A)
class _Opmen99810bLLDPMEDPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bLLDPMEDPrivilegeLevel_Type.__name__=_C
_Opmen99810bLLDPMEDPrivilegeLevel_Object=MibScalar
opmen99810bLLDPMEDPrivilegeLevel=_Opmen99810bLLDPMEDPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,16),_Opmen99810bLLDPMEDPrivilegeLevel_Type())
opmen99810bLLDPMEDPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bLLDPMEDPrivilegeLevel.setStatus(_A)
class _Opmen99810bLoopProtectPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bLoopProtectPrivilegeLevel_Type.__name__=_C
_Opmen99810bLoopProtectPrivilegeLevel_Object=MibScalar
opmen99810bLoopProtectPrivilegeLevel=_Opmen99810bLoopProtectPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,17),_Opmen99810bLoopProtectPrivilegeLevel_Type())
opmen99810bLoopProtectPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bLoopProtectPrivilegeLevel.setStatus(_A)
class _Opmen99810bMACTablePrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bMACTablePrivilegeLevel_Type.__name__=_C
_Opmen99810bMACTablePrivilegeLevel_Object=MibScalar
opmen99810bMACTablePrivilegeLevel=_Opmen99810bMACTablePrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,18),_Opmen99810bMACTablePrivilegeLevel_Type())
opmen99810bMACTablePrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bMACTablePrivilegeLevel.setStatus(_A)
class _Opmen99810bMVRPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bMVRPrivilegeLevel_Type.__name__=_C
_Opmen99810bMVRPrivilegeLevel_Object=MibScalar
opmen99810bMVRPrivilegeLevel=_Opmen99810bMVRPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,22),_Opmen99810bMVRPrivilegeLevel_Type())
opmen99810bMVRPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bMVRPrivilegeLevel.setStatus(_A)
class _Opmen99810bMaintenancePrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bMaintenancePrivilegeLevel_Type.__name__=_C
_Opmen99810bMaintenancePrivilegeLevel_Object=MibScalar
opmen99810bMaintenancePrivilegeLevel=_Opmen99810bMaintenancePrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,24),_Opmen99810bMaintenancePrivilegeLevel_Type())
opmen99810bMaintenancePrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bMaintenancePrivilegeLevel.setStatus(_A)
class _Opmen99810bMirroringPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bMirroringPrivilegeLevel_Type.__name__=_C
_Opmen99810bMirroringPrivilegeLevel_Object=MibScalar
opmen99810bMirroringPrivilegeLevel=_Opmen99810bMirroringPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,25),_Opmen99810bMirroringPrivilegeLevel_Type())
opmen99810bMirroringPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bMirroringPrivilegeLevel.setStatus(_A)
class _Opmen99810bPortsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bPortsPrivilegeLevel_Type.__name__=_C
_Opmen99810bPortsPrivilegeLevel_Object=MibScalar
opmen99810bPortsPrivilegeLevel=_Opmen99810bPortsPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,27),_Opmen99810bPortsPrivilegeLevel_Type())
opmen99810bPortsPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortsPrivilegeLevel.setStatus(_A)
class _Opmen99810bPrivateVLANsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bPrivateVLANsPrivilegeLevel_Type.__name__=_C
_Opmen99810bPrivateVLANsPrivilegeLevel_Object=MibScalar
opmen99810bPrivateVLANsPrivilegeLevel=_Opmen99810bPrivateVLANsPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,28),_Opmen99810bPrivateVLANsPrivilegeLevel_Type())
opmen99810bPrivateVLANsPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPrivateVLANsPrivilegeLevel.setStatus(_A)
class _Opmen99810bQoSPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bQoSPrivilegeLevel_Type.__name__=_C
_Opmen99810bQoSPrivilegeLevel_Object=MibScalar
opmen99810bQoSPrivilegeLevel=_Opmen99810bQoSPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,29),_Opmen99810bQoSPrivilegeLevel_Type())
opmen99810bQoSPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQoSPrivilegeLevel.setStatus(_A)
class _Opmen99810bSFlowPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bSFlowPrivilegeLevel_Type.__name__=_C
_Opmen99810bSFlowPrivilegeLevel_Object=MibScalar
opmen99810bSFlowPrivilegeLevel=_Opmen99810bSFlowPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,30),_Opmen99810bSFlowPrivilegeLevel_Type())
opmen99810bSFlowPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSFlowPrivilegeLevel.setStatus(_A)
class _Opmen99810bSMTPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bSMTPPrivilegeLevel_Type.__name__=_C
_Opmen99810bSMTPPrivilegeLevel_Object=MibScalar
opmen99810bSMTPPrivilegeLevel=_Opmen99810bSMTPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,31),_Opmen99810bSMTPPrivilegeLevel_Type())
opmen99810bSMTPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSMTPPrivilegeLevel.setStatus(_A)
class _Opmen99810bSNMPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bSNMPPrivilegeLevel_Type.__name__=_C
_Opmen99810bSNMPPrivilegeLevel_Object=MibScalar
opmen99810bSNMPPrivilegeLevel=_Opmen99810bSNMPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,32),_Opmen99810bSNMPPrivilegeLevel_Type())
opmen99810bSNMPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSNMPPrivilegeLevel.setStatus(_A)
class _Opmen99810bSecurityPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bSecurityPrivilegeLevel_Type.__name__=_C
_Opmen99810bSecurityPrivilegeLevel_Object=MibScalar
opmen99810bSecurityPrivilegeLevel=_Opmen99810bSecurityPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,33),_Opmen99810bSecurityPrivilegeLevel_Type())
opmen99810bSecurityPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSecurityPrivilegeLevel.setStatus(_A)
class _Opmen99810bSingleIPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bSingleIPPrivilegeLevel_Type.__name__=_C
_Opmen99810bSingleIPPrivilegeLevel_Object=MibScalar
opmen99810bSingleIPPrivilegeLevel=_Opmen99810bSingleIPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,34),_Opmen99810bSingleIPPrivilegeLevel_Type())
opmen99810bSingleIPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSingleIPPrivilegeLevel.setStatus(_A)
class _Opmen99810bSpanningTreePrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bSpanningTreePrivilegeLevel_Type.__name__=_C
_Opmen99810bSpanningTreePrivilegeLevel_Object=MibScalar
opmen99810bSpanningTreePrivilegeLevel=_Opmen99810bSpanningTreePrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,35),_Opmen99810bSpanningTreePrivilegeLevel_Type())
opmen99810bSpanningTreePrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSpanningTreePrivilegeLevel.setStatus(_A)
class _Opmen99810bSystemPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bSystemPrivilegeLevel_Type.__name__=_C
_Opmen99810bSystemPrivilegeLevel_Object=MibScalar
opmen99810bSystemPrivilegeLevel=_Opmen99810bSystemPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,36),_Opmen99810bSystemPrivilegeLevel_Type())
opmen99810bSystemPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSystemPrivilegeLevel.setStatus(_A)
class _Opmen99810bTrapEventPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bTrapEventPrivilegeLevel_Type.__name__=_C
_Opmen99810bTrapEventPrivilegeLevel_Object=MibScalar
opmen99810bTrapEventPrivilegeLevel=_Opmen99810bTrapEventPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,37),_Opmen99810bTrapEventPrivilegeLevel_Type())
opmen99810bTrapEventPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventPrivilegeLevel.setStatus(_A)
class _Opmen99810bUPnPPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bUPnPPrivilegeLevel_Type.__name__=_C
_Opmen99810bUPnPPrivilegeLevel_Object=MibScalar
opmen99810bUPnPPrivilegeLevel=_Opmen99810bUPnPPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,38),_Opmen99810bUPnPPrivilegeLevel_Type())
opmen99810bUPnPPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bUPnPPrivilegeLevel.setStatus(_A)
class _Opmen99810bVCLPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bVCLPrivilegeLevel_Type.__name__=_C
_Opmen99810bVCLPrivilegeLevel_Object=MibScalar
opmen99810bVCLPrivilegeLevel=_Opmen99810bVCLPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,39),_Opmen99810bVCLPrivilegeLevel_Type())
opmen99810bVCLPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVCLPrivilegeLevel.setStatus(_A)
class _Opmen99810bVLANsPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bVLANsPrivilegeLevel_Type.__name__=_C
_Opmen99810bVLANsPrivilegeLevel_Object=MibScalar
opmen99810bVLANsPrivilegeLevel=_Opmen99810bVLANsPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,41),_Opmen99810bVLANsPrivilegeLevel_Type())
opmen99810bVLANsPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVLANsPrivilegeLevel.setStatus(_A)
class _Opmen99810bVoiceVLANPrivilegeLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Opmen99810bVoiceVLANPrivilegeLevel_Type.__name__=_C
_Opmen99810bVoiceVLANPrivilegeLevel_Object=MibScalar
opmen99810bVoiceVLANPrivilegeLevel=_Opmen99810bVoiceVLANPrivilegeLevel_Object((1,3,6,1,4,1,5205,2,94,1,3,2,42),_Opmen99810bVoiceVLANPrivilegeLevel_Type())
opmen99810bVoiceVLANPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVoiceVLANPrivilegeLevel.setStatus(_A)
_Opmen99810bIP_ObjectIdentity=ObjectIdentity
opmen99810bIP=_Opmen99810bIP_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,4))
_Opmen99810bIPv4_ObjectIdentity=ObjectIdentity
opmen99810bIPv4=_Opmen99810bIPv4_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,4,1))
_Opmen99810bIPv4Configured_ObjectIdentity=ObjectIdentity
opmen99810bIPv4Configured=_Opmen99810bIPv4Configured_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,4,1,1))
class _Opmen99810bIpv4DHCPClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bIpv4DHCPClient_Type.__name__=_C
_Opmen99810bIpv4DHCPClient_Object=MibScalar
opmen99810bIpv4DHCPClient=_Opmen99810bIpv4DHCPClient_Object((1,3,6,1,4,1,5205,2,94,1,4,1,1,1),_Opmen99810bIpv4DHCPClient_Type())
opmen99810bIpv4DHCPClient.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIpv4DHCPClient.setStatus(_A)
_Opmen99810bIPv4Address_Type=IpAddress
_Opmen99810bIPv4Address_Object=MibScalar
opmen99810bIPv4Address=_Opmen99810bIPv4Address_Object((1,3,6,1,4,1,5205,2,94,1,4,1,1,2),_Opmen99810bIPv4Address_Type())
opmen99810bIPv4Address.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPv4Address.setStatus(_A)
_Opmen99810bIPv4Mask_Type=IpAddress
_Opmen99810bIPv4Mask_Object=MibScalar
opmen99810bIPv4Mask=_Opmen99810bIPv4Mask_Object((1,3,6,1,4,1,5205,2,94,1,4,1,1,3),_Opmen99810bIPv4Mask_Type())
opmen99810bIPv4Mask.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPv4Mask.setStatus(_A)
_Opmen99810bIPv4Gateway_Type=IpAddress
_Opmen99810bIPv4Gateway_Object=MibScalar
opmen99810bIPv4Gateway=_Opmen99810bIPv4Gateway_Object((1,3,6,1,4,1,5205,2,94,1,4,1,1,4),_Opmen99810bIPv4Gateway_Type())
opmen99810bIPv4Gateway.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPv4Gateway.setStatus(_A)
class _Opmen99810bIPv4VLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Opmen99810bIPv4VLANId_Type.__name__=_C
_Opmen99810bIPv4VLANId_Object=MibScalar
opmen99810bIPv4VLANId=_Opmen99810bIPv4VLANId_Object((1,3,6,1,4,1,5205,2,94,1,4,1,1,5),_Opmen99810bIPv4VLANId_Type())
opmen99810bIPv4VLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPv4VLANId.setStatus(_A)
_Opmen99810bIPv4DNSServer_Type=IpAddress
_Opmen99810bIPv4DNSServer_Object=MibScalar
opmen99810bIPv4DNSServer=_Opmen99810bIPv4DNSServer_Object((1,3,6,1,4,1,5205,2,94,1,4,1,1,6),_Opmen99810bIPv4DNSServer_Type())
opmen99810bIPv4DNSServer.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPv4DNSServer.setStatus(_A)
class _Opmen99810bIPv4DNSProxy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bIPv4DNSProxy_Type.__name__=_C
_Opmen99810bIPv4DNSProxy_Object=MibScalar
opmen99810bIPv4DNSProxy=_Opmen99810bIPv4DNSProxy_Object((1,3,6,1,4,1,5205,2,94,1,4,1,1,7),_Opmen99810bIPv4DNSProxy_Type())
opmen99810bIPv4DNSProxy.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPv4DNSProxy.setStatus(_A)
_Opmen99810bIPv4Current_ObjectIdentity=ObjectIdentity
opmen99810bIPv4Current=_Opmen99810bIPv4Current_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,4,1,2))
class _Opmen99810bIpv4CurrentDHCPClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),('renew',1)))
_Opmen99810bIpv4CurrentDHCPClient_Type.__name__=_C
_Opmen99810bIpv4CurrentDHCPClient_Object=MibScalar
opmen99810bIpv4CurrentDHCPClient=_Opmen99810bIpv4CurrentDHCPClient_Object((1,3,6,1,4,1,5205,2,94,1,4,1,2,1),_Opmen99810bIpv4CurrentDHCPClient_Type())
opmen99810bIpv4CurrentDHCPClient.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIpv4CurrentDHCPClient.setStatus(_A)
_Opmen99810bIPv4CurrentAddress_Type=IpAddress
_Opmen99810bIPv4CurrentAddress_Object=MibScalar
opmen99810bIPv4CurrentAddress=_Opmen99810bIPv4CurrentAddress_Object((1,3,6,1,4,1,5205,2,94,1,4,1,2,2),_Opmen99810bIPv4CurrentAddress_Type())
opmen99810bIPv4CurrentAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bIPv4CurrentAddress.setStatus(_A)
_Opmen99810bIPv4CurrentMask_Type=IpAddress
_Opmen99810bIPv4CurrentMask_Object=MibScalar
opmen99810bIPv4CurrentMask=_Opmen99810bIPv4CurrentMask_Object((1,3,6,1,4,1,5205,2,94,1,4,1,2,3),_Opmen99810bIPv4CurrentMask_Type())
opmen99810bIPv4CurrentMask.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bIPv4CurrentMask.setStatus(_A)
_Opmen99810bIPv4CurrentGateway_Type=IpAddress
_Opmen99810bIPv4CurrentGateway_Object=MibScalar
opmen99810bIPv4CurrentGateway=_Opmen99810bIPv4CurrentGateway_Object((1,3,6,1,4,1,5205,2,94,1,4,1,2,4),_Opmen99810bIPv4CurrentGateway_Type())
opmen99810bIPv4CurrentGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bIPv4CurrentGateway.setStatus(_A)
class _Opmen99810bIPv4CurrentVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Opmen99810bIPv4CurrentVLANId_Type.__name__=_C
_Opmen99810bIPv4CurrentVLANId_Object=MibScalar
opmen99810bIPv4CurrentVLANId=_Opmen99810bIPv4CurrentVLANId_Object((1,3,6,1,4,1,5205,2,94,1,4,1,2,5),_Opmen99810bIPv4CurrentVLANId_Type())
opmen99810bIPv4CurrentVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bIPv4CurrentVLANId.setStatus(_A)
_Opmen99810bIPv4CurrentDNSServer_Type=IpAddress
_Opmen99810bIPv4CurrentDNSServer_Object=MibScalar
opmen99810bIPv4CurrentDNSServer=_Opmen99810bIPv4CurrentDNSServer_Object((1,3,6,1,4,1,5205,2,94,1,4,1,2,6),_Opmen99810bIPv4CurrentDNSServer_Type())
opmen99810bIPv4CurrentDNSServer.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bIPv4CurrentDNSServer.setStatus(_A)
_Opmen99810bIPv6_ObjectIdentity=ObjectIdentity
opmen99810bIPv6=_Opmen99810bIPv6_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,4,2))
_Opmen99810bIPv6Configured_ObjectIdentity=ObjectIdentity
opmen99810bIPv6Configured=_Opmen99810bIPv6Configured_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,4,2,1))
class _Opmen99810bIpv6AutoConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bIpv6AutoConfiguration_Type.__name__=_C
_Opmen99810bIpv6AutoConfiguration_Object=MibScalar
opmen99810bIpv6AutoConfiguration=_Opmen99810bIpv6AutoConfiguration_Object((1,3,6,1,4,1,5205,2,94,1,4,2,1,1),_Opmen99810bIpv6AutoConfiguration_Type())
opmen99810bIpv6AutoConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIpv6AutoConfiguration.setStatus(_A)
class _Opmen99810bIpv6Address_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Opmen99810bIpv6Address_Type.__name__=_S
_Opmen99810bIpv6Address_Object=MibScalar
opmen99810bIpv6Address=_Opmen99810bIpv6Address_Object((1,3,6,1,4,1,5205,2,94,1,4,2,1,2),_Opmen99810bIpv6Address_Type())
opmen99810bIpv6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIpv6Address.setStatus(_A)
class _Opmen99810bIpv6Prefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Opmen99810bIpv6Prefix_Type.__name__=_C
_Opmen99810bIpv6Prefix_Object=MibScalar
opmen99810bIpv6Prefix=_Opmen99810bIpv6Prefix_Object((1,3,6,1,4,1,5205,2,94,1,4,2,1,3),_Opmen99810bIpv6Prefix_Type())
opmen99810bIpv6Prefix.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIpv6Prefix.setStatus(_A)
class _Opmen99810bIpv6Gateway_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Opmen99810bIpv6Gateway_Type.__name__=_S
_Opmen99810bIpv6Gateway_Object=MibScalar
opmen99810bIpv6Gateway=_Opmen99810bIpv6Gateway_Object((1,3,6,1,4,1,5205,2,94,1,4,2,1,4),_Opmen99810bIpv6Gateway_Type())
opmen99810bIpv6Gateway.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIpv6Gateway.setStatus(_A)
_Opmen99810bIPv6Current_ObjectIdentity=ObjectIdentity
opmen99810bIPv6Current=_Opmen99810bIPv6Current_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,4,2,2))
class _Opmen99810bIpv6CurrentAutoConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bIpv6CurrentAutoConfiguration_Type.__name__=_C
_Opmen99810bIpv6CurrentAutoConfiguration_Object=MibScalar
opmen99810bIpv6CurrentAutoConfiguration=_Opmen99810bIpv6CurrentAutoConfiguration_Object((1,3,6,1,4,1,5205,2,94,1,4,2,2,1),_Opmen99810bIpv6CurrentAutoConfiguration_Type())
opmen99810bIpv6CurrentAutoConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bIpv6CurrentAutoConfiguration.setStatus(_A)
class _Opmen99810bIpv6CurrentAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Opmen99810bIpv6CurrentAddress_Type.__name__=_S
_Opmen99810bIpv6CurrentAddress_Object=MibScalar
opmen99810bIpv6CurrentAddress=_Opmen99810bIpv6CurrentAddress_Object((1,3,6,1,4,1,5205,2,94,1,4,2,2,2),_Opmen99810bIpv6CurrentAddress_Type())
opmen99810bIpv6CurrentAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bIpv6CurrentAddress.setStatus(_A)
class _Opmen99810bIpv6CurrentLinkLocalAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Opmen99810bIpv6CurrentLinkLocalAddress_Type.__name__=_S
_Opmen99810bIpv6CurrentLinkLocalAddress_Object=MibScalar
opmen99810bIpv6CurrentLinkLocalAddress=_Opmen99810bIpv6CurrentLinkLocalAddress_Object((1,3,6,1,4,1,5205,2,94,1,4,2,2,3),_Opmen99810bIpv6CurrentLinkLocalAddress_Type())
opmen99810bIpv6CurrentLinkLocalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bIpv6CurrentLinkLocalAddress.setStatus(_A)
class _Opmen99810bIpv6CurrentPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Opmen99810bIpv6CurrentPrefix_Type.__name__=_C
_Opmen99810bIpv6CurrentPrefix_Object=MibScalar
opmen99810bIpv6CurrentPrefix=_Opmen99810bIpv6CurrentPrefix_Object((1,3,6,1,4,1,5205,2,94,1,4,2,2,4),_Opmen99810bIpv6CurrentPrefix_Type())
opmen99810bIpv6CurrentPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bIpv6CurrentPrefix.setStatus(_A)
class _Opmen99810bIpv6CurrentGateway_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_Opmen99810bIpv6CurrentGateway_Type.__name__=_S
_Opmen99810bIpv6CurrentGateway_Object=MibScalar
opmen99810bIpv6CurrentGateway=_Opmen99810bIpv6CurrentGateway_Object((1,3,6,1,4,1,5205,2,94,1,4,2,2,5),_Opmen99810bIpv6CurrentGateway_Type())
opmen99810bIpv6CurrentGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bIpv6CurrentGateway.setStatus(_A)
_Opmen99810bSyslog_ObjectIdentity=ObjectIdentity
opmen99810bSyslog=_Opmen99810bSyslog_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,5))
_Opmen99810bSyslogConf_ObjectIdentity=ObjectIdentity
opmen99810bSyslogConf=_Opmen99810bSyslogConf_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,5,1))
class _Opmen99810bServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bServerMode_Type.__name__=_C
_Opmen99810bServerMode_Object=MibScalar
opmen99810bServerMode=_Opmen99810bServerMode_Object((1,3,6,1,4,1,5205,2,94,1,5,1,1),_Opmen99810bServerMode_Type())
opmen99810bServerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bServerMode.setStatus(_A)
_Opmen99810bServerAddress1_Type=IpAddress
_Opmen99810bServerAddress1_Object=MibScalar
opmen99810bServerAddress1=_Opmen99810bServerAddress1_Object((1,3,6,1,4,1,5205,2,94,1,5,1,2),_Opmen99810bServerAddress1_Type())
opmen99810bServerAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bServerAddress1.setStatus(_A)
_Opmen99810bServerAddress2_Type=IpAddress
_Opmen99810bServerAddress2_Object=MibScalar
opmen99810bServerAddress2=_Opmen99810bServerAddress2_Object((1,3,6,1,4,1,5205,2,94,1,5,1,3),_Opmen99810bServerAddress2_Type())
opmen99810bServerAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bServerAddress2.setStatus(_A)
class _Opmen99810bSyslogLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bSyslogLevel_Type.__name__=_C
_Opmen99810bSyslogLevel_Object=MibScalar
opmen99810bSyslogLevel=_Opmen99810bSyslogLevel_Object((1,3,6,1,4,1,5205,2,94,1,5,1,4),_Opmen99810bSyslogLevel_Type())
opmen99810bSyslogLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSyslogLevel.setStatus(_A)
_Opmen99810bSyslogDetailedInfo_ObjectIdentity=ObjectIdentity
opmen99810bSyslogDetailedInfo=_Opmen99810bSyslogDetailedInfo_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,5,2))
class _Opmen99810bSyslogDetailedInfoClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_e,1)))
_Opmen99810bSyslogDetailedInfoClear_Type.__name__=_C
_Opmen99810bSyslogDetailedInfoClear_Object=MibScalar
opmen99810bSyslogDetailedInfoClear=_Opmen99810bSyslogDetailedInfoClear_Object((1,3,6,1,4,1,5205,2,94,1,5,2,1),_Opmen99810bSyslogDetailedInfoClear_Type())
opmen99810bSyslogDetailedInfoClear.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSyslogDetailedInfoClear.setStatus(_A)
_Opmen99810bSyslogDetailedInfoTable_Object=MibTable
opmen99810bSyslogDetailedInfoTable=_Opmen99810bSyslogDetailedInfoTable_Object((1,3,6,1,4,1,5205,2,94,1,5,2,2))
if mibBuilder.loadTexts:opmen99810bSyslogDetailedInfoTable.setStatus(_A)
_Opmen99810bSyslogDetailedInfoEntry_Object=MibTableRow
opmen99810bSyslogDetailedInfoEntry=_Opmen99810bSyslogDetailedInfoEntry_Object((1,3,6,1,4,1,5205,2,94,1,5,2,2,1))
opmen99810bSyslogDetailedInfoEntry.setIndexNames((0,_G,_A2))
if mibBuilder.loadTexts:opmen99810bSyslogDetailedInfoEntry.setStatus(_A)
class _Opmen99810bSyslogDetailedInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Opmen99810bSyslogDetailedInfoIndex_Type.__name__=_C
_Opmen99810bSyslogDetailedInfoIndex_Object=MibTableColumn
opmen99810bSyslogDetailedInfoIndex=_Opmen99810bSyslogDetailedInfoIndex_Object((1,3,6,1,4,1,5205,2,94,1,5,2,2,1,1),_Opmen99810bSyslogDetailedInfoIndex_Type())
opmen99810bSyslogDetailedInfoIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bSyslogDetailedInfoIndex.setStatus(_A)
_Opmen99810bSyslogDetailedInfoLevel_Type=DisplayString
_Opmen99810bSyslogDetailedInfoLevel_Object=MibTableColumn
opmen99810bSyslogDetailedInfoLevel=_Opmen99810bSyslogDetailedInfoLevel_Object((1,3,6,1,4,1,5205,2,94,1,5,2,2,1,2),_Opmen99810bSyslogDetailedInfoLevel_Type())
opmen99810bSyslogDetailedInfoLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSyslogDetailedInfoLevel.setStatus(_A)
class _Opmen99810bSyslogDetailedInfoTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_Opmen99810bSyslogDetailedInfoTime_Type.__name__=_S
_Opmen99810bSyslogDetailedInfoTime_Object=MibTableColumn
opmen99810bSyslogDetailedInfoTime=_Opmen99810bSyslogDetailedInfoTime_Object((1,3,6,1,4,1,5205,2,94,1,5,2,2,1,3),_Opmen99810bSyslogDetailedInfoTime_Type())
opmen99810bSyslogDetailedInfoTime.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSyslogDetailedInfoTime.setStatus(_A)
_Opmen99810bSyslogDetailedInfoMessage_Type=DisplayString
_Opmen99810bSyslogDetailedInfoMessage_Object=MibTableColumn
opmen99810bSyslogDetailedInfoMessage=_Opmen99810bSyslogDetailedInfoMessage_Object((1,3,6,1,4,1,5205,2,94,1,5,2,2,1,4),_Opmen99810bSyslogDetailedInfoMessage_Type())
opmen99810bSyslogDetailedInfoMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSyslogDetailedInfoMessage.setStatus(_A)
_Opmen99810bSnmp_ObjectIdentity=ObjectIdentity
opmen99810bSnmp=_Opmen99810bSnmp_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,6))
_Opmen99810bSnmpConf_ObjectIdentity=ObjectIdentity
opmen99810bSnmpConf=_Opmen99810bSnmpConf_ObjectIdentity((1,3,6,1,4,1,5205,2,94,1,6,1))
_Opmen99810bGetCommunity_Type=DisplayString
_Opmen99810bGetCommunity_Object=MibScalar
opmen99810bGetCommunity=_Opmen99810bGetCommunity_Object((1,3,6,1,4,1,5205,2,94,1,6,1,1),_Opmen99810bGetCommunity_Type())
opmen99810bGetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bGetCommunity.setStatus(_A)
class _Opmen99810bSetCommunityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bSetCommunityMode_Type.__name__=_C
_Opmen99810bSetCommunityMode_Object=MibScalar
opmen99810bSetCommunityMode=_Opmen99810bSetCommunityMode_Object((1,3,6,1,4,1,5205,2,94,1,6,1,2),_Opmen99810bSetCommunityMode_Type())
opmen99810bSetCommunityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSetCommunityMode.setStatus(_A)
_Opmen99810bSetCommunity_Type=DisplayString
_Opmen99810bSetCommunity_Object=MibScalar
opmen99810bSetCommunity=_Opmen99810bSetCommunity_Object((1,3,6,1,4,1,5205,2,94,1,6,1,3),_Opmen99810bSetCommunity_Type())
opmen99810bSetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSetCommunity.setStatus(_A)
_Opmen99810bTrapHostConfTable_Object=MibTable
opmen99810bTrapHostConfTable=_Opmen99810bTrapHostConfTable_Object((1,3,6,1,4,1,5205,2,94,1,6,1,4))
if mibBuilder.loadTexts:opmen99810bTrapHostConfTable.setStatus(_A)
_Opmen99810bTrapHostConfEntry_Object=MibTableRow
opmen99810bTrapHostConfEntry=_Opmen99810bTrapHostConfEntry_Object((1,3,6,1,4,1,5205,2,94,1,6,1,4,1))
opmen99810bTrapHostConfEntry.setIndexNames((0,_G,_A3))
if mibBuilder.loadTexts:opmen99810bTrapHostConfEntry.setStatus(_A)
class _Opmen99810bTrapHostConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Opmen99810bTrapHostConfIndex_Type.__name__=_C
_Opmen99810bTrapHostConfIndex_Object=MibTableColumn
opmen99810bTrapHostConfIndex=_Opmen99810bTrapHostConfIndex_Object((1,3,6,1,4,1,5205,2,94,1,6,1,4,1,1),_Opmen99810bTrapHostConfIndex_Type())
opmen99810bTrapHostConfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bTrapHostConfIndex.setStatus(_A)
class _Opmen99810bTrapHostConfVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('snmpv2c',2),('snmpv3',3)))
_Opmen99810bTrapHostConfVersion_Type.__name__=_C
_Opmen99810bTrapHostConfVersion_Object=MibTableColumn
opmen99810bTrapHostConfVersion=_Opmen99810bTrapHostConfVersion_Object((1,3,6,1,4,1,5205,2,94,1,6,1,4,1,2),_Opmen99810bTrapHostConfVersion_Type())
opmen99810bTrapHostConfVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapHostConfVersion.setStatus(_A)
class _Opmen99810bTrapHostConfIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,6)));namedValues=NamedValues(*((_d,4),(_j,6)))
_Opmen99810bTrapHostConfIPType_Type.__name__=_C
_Opmen99810bTrapHostConfIPType_Object=MibTableColumn
opmen99810bTrapHostConfIPType=_Opmen99810bTrapHostConfIPType_Object((1,3,6,1,4,1,5205,2,94,1,6,1,4,1,3),_Opmen99810bTrapHostConfIPType_Type())
opmen99810bTrapHostConfIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapHostConfIPType.setStatus(_A)
_Opmen99810bTrapHostConfIP_Type=DisplayString
_Opmen99810bTrapHostConfIP_Object=MibTableColumn
opmen99810bTrapHostConfIP=_Opmen99810bTrapHostConfIP_Object((1,3,6,1,4,1,5205,2,94,1,6,1,4,1,4),_Opmen99810bTrapHostConfIP_Type())
opmen99810bTrapHostConfIP.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapHostConfIP.setStatus(_A)
class _Opmen99810bTrapHostConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Opmen99810bTrapHostConfPort_Type.__name__=_C
_Opmen99810bTrapHostConfPort_Object=MibTableColumn
opmen99810bTrapHostConfPort=_Opmen99810bTrapHostConfPort_Object((1,3,6,1,4,1,5205,2,94,1,6,1,4,1,5),_Opmen99810bTrapHostConfPort_Type())
opmen99810bTrapHostConfPort.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapHostConfPort.setStatus(_A)
class _Opmen99810bTrapHostConfCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Opmen99810bTrapHostConfCommunity_Type.__name__=_S
_Opmen99810bTrapHostConfCommunity_Object=MibTableColumn
opmen99810bTrapHostConfCommunity=_Opmen99810bTrapHostConfCommunity_Object((1,3,6,1,4,1,5205,2,94,1,6,1,4,1,6),_Opmen99810bTrapHostConfCommunity_Type())
opmen99810bTrapHostConfCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapHostConfCommunity.setStatus(_A)
class _Opmen99810bTrapHostConfSeverityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapHostConfSeverityLevel_Type.__name__=_C
_Opmen99810bTrapHostConfSeverityLevel_Object=MibTableColumn
opmen99810bTrapHostConfSeverityLevel=_Opmen99810bTrapHostConfSeverityLevel_Object((1,3,6,1,4,1,5205,2,94,1,6,1,4,1,7),_Opmen99810bTrapHostConfSeverityLevel_Type())
opmen99810bTrapHostConfSeverityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapHostConfSeverityLevel.setStatus(_A)
class _Opmen99810bTrapHostConfSecurityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuthNoPriv',1),('authNoPriv',2),('authPriv',3)))
_Opmen99810bTrapHostConfSecurityLevel_Type.__name__=_C
_Opmen99810bTrapHostConfSecurityLevel_Object=MibTableColumn
opmen99810bTrapHostConfSecurityLevel=_Opmen99810bTrapHostConfSecurityLevel_Object((1,3,6,1,4,1,5205,2,94,1,6,1,4,1,8),_Opmen99810bTrapHostConfSecurityLevel_Type())
opmen99810bTrapHostConfSecurityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapHostConfSecurityLevel.setStatus(_A)
class _Opmen99810bTrapHostConfAuthPtc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('md5',1),('sha',2)))
_Opmen99810bTrapHostConfAuthPtc_Type.__name__=_C
_Opmen99810bTrapHostConfAuthPtc_Object=MibTableColumn
opmen99810bTrapHostConfAuthPtc=_Opmen99810bTrapHostConfAuthPtc_Object((1,3,6,1,4,1,5205,2,94,1,6,1,4,1,9),_Opmen99810bTrapHostConfAuthPtc_Type())
opmen99810bTrapHostConfAuthPtc.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapHostConfAuthPtc.setStatus(_A)
_Opmen99810bTrapHostConfAuthPassword_Type=DisplayString
_Opmen99810bTrapHostConfAuthPassword_Object=MibTableColumn
opmen99810bTrapHostConfAuthPassword=_Opmen99810bTrapHostConfAuthPassword_Object((1,3,6,1,4,1,5205,2,94,1,6,1,4,1,10),_Opmen99810bTrapHostConfAuthPassword_Type())
opmen99810bTrapHostConfAuthPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapHostConfAuthPassword.setStatus(_A)
class _Opmen99810bTrapHostConfPrivPtc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('des',1))
_Opmen99810bTrapHostConfPrivPtc_Type.__name__=_C
_Opmen99810bTrapHostConfPrivPtc_Object=MibTableColumn
opmen99810bTrapHostConfPrivPtc=_Opmen99810bTrapHostConfPrivPtc_Object((1,3,6,1,4,1,5205,2,94,1,6,1,4,1,11),_Opmen99810bTrapHostConfPrivPtc_Type())
opmen99810bTrapHostConfPrivPtc.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapHostConfPrivPtc.setStatus(_A)
_Opmen99810bTrapHostConfPrivPassword_Type=DisplayString
_Opmen99810bTrapHostConfPrivPassword_Object=MibTableColumn
opmen99810bTrapHostConfPrivPassword=_Opmen99810bTrapHostConfPrivPassword_Object((1,3,6,1,4,1,5205,2,94,1,6,1,4,1,12),_Opmen99810bTrapHostConfPrivPassword_Type())
opmen99810bTrapHostConfPrivPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapHostConfPrivPassword.setStatus(_A)
class _Opmen99810bTrapHostConfCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('empty',0),(_U,1),(_b,2),('delete',3)))
_Opmen99810bTrapHostConfCurrentMode_Type.__name__=_C
_Opmen99810bTrapHostConfCurrentMode_Object=MibTableColumn
opmen99810bTrapHostConfCurrentMode=_Opmen99810bTrapHostConfCurrentMode_Object((1,3,6,1,4,1,5205,2,94,1,6,1,4,1,13),_Opmen99810bTrapHostConfCurrentMode_Type())
opmen99810bTrapHostConfCurrentMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapHostConfCurrentMode.setStatus(_A)
_Opmen99810bConfiguration_ObjectIdentity=ObjectIdentity
opmen99810bConfiguration=_Opmen99810bConfiguration_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2))
_Opmen99810bPort_ObjectIdentity=ObjectIdentity
opmen99810bPort=_Opmen99810bPort_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,1))
_Opmen99810bPortConfigurationTable_Object=MibTable
opmen99810bPortConfigurationTable=_Opmen99810bPortConfigurationTable_Object((1,3,6,1,4,1,5205,2,94,2,1,1))
if mibBuilder.loadTexts:opmen99810bPortConfigurationTable.setStatus(_A)
_Opmen99810bPortConfigurationEntry_Object=MibTableRow
opmen99810bPortConfigurationEntry=_Opmen99810bPortConfigurationEntry_Object((1,3,6,1,4,1,5205,2,94,2,1,1,1))
opmen99810bPortConfigurationEntry.setIndexNames((0,_G,_A4))
if mibBuilder.loadTexts:opmen99810bPortConfigurationEntry.setStatus(_A)
class _Opmen99810bPortConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bPortConfPort_Type.__name__=_C
_Opmen99810bPortConfPort_Object=MibTableColumn
opmen99810bPortConfPort=_Opmen99810bPortConfPort_Object((1,3,6,1,4,1,5205,2,94,2,1,1,1,1),_Opmen99810bPortConfPort_Type())
opmen99810bPortConfPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bPortConfPort.setStatus(_A)
class _Opmen99810bPortConfPortMedia_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_Opmen99810bPortConfPortMedia_Type.__name__=_S
_Opmen99810bPortConfPortMedia_Object=MibTableColumn
opmen99810bPortConfPortMedia=_Opmen99810bPortConfPortMedia_Object((1,3,6,1,4,1,5205,2,94,2,1,1,1,2),_Opmen99810bPortConfPortMedia_Type())
opmen99810bPortConfPortMedia.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortConfPortMedia.setStatus(_A)
class _Opmen99810bPortConfLink_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,4))
_Opmen99810bPortConfLink_Type.__name__=_S
_Opmen99810bPortConfLink_Object=MibTableColumn
opmen99810bPortConfLink=_Opmen99810bPortConfLink_Object((1,3,6,1,4,1,5205,2,94,2,1,1,1,3),_Opmen99810bPortConfLink_Type())
opmen99810bPortConfLink.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortConfLink.setStatus(_A)
class _Opmen99810bPortConfCurrentSpeed_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,12))
_Opmen99810bPortConfCurrentSpeed_Type.__name__=_S
_Opmen99810bPortConfCurrentSpeed_Object=MibTableColumn
opmen99810bPortConfCurrentSpeed=_Opmen99810bPortConfCurrentSpeed_Object((1,3,6,1,4,1,5205,2,94,2,1,1,1,4),_Opmen99810bPortConfCurrentSpeed_Type())
opmen99810bPortConfCurrentSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortConfCurrentSpeed.setStatus(_A)
class _Opmen99810bPortConfSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_E,0),('auto',1),('speed10Half',2),('speed10Full',3),('speed100Half',4),('speed100Full',5),('speed1Gfull',6),('sfpAutoAMS',7),('speed100FXAMS',8),('speed1000XAMS',9),('speed100FX',10),('speed1000X',11)))
_Opmen99810bPortConfSpeed_Type.__name__=_C
_Opmen99810bPortConfSpeed_Object=MibTableColumn
opmen99810bPortConfSpeed=_Opmen99810bPortConfSpeed_Object((1,3,6,1,4,1,5205,2,94,2,1,1,1,5),_Opmen99810bPortConfSpeed_Type())
opmen99810bPortConfSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortConfSpeed.setStatus(_A)
class _Opmen99810bPortConfCurrentFlowControlRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_F,1),(_f,2)))
_Opmen99810bPortConfCurrentFlowControlRx_Type.__name__=_C
_Opmen99810bPortConfCurrentFlowControlRx_Object=MibTableColumn
opmen99810bPortConfCurrentFlowControlRx=_Opmen99810bPortConfCurrentFlowControlRx_Object((1,3,6,1,4,1,5205,2,94,2,1,1,1,6),_Opmen99810bPortConfCurrentFlowControlRx_Type())
opmen99810bPortConfCurrentFlowControlRx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortConfCurrentFlowControlRx.setStatus(_A)
class _Opmen99810bPortConfCurrentFlowControlTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_F,1),(_f,2)))
_Opmen99810bPortConfCurrentFlowControlTx_Type.__name__=_C
_Opmen99810bPortConfCurrentFlowControlTx_Object=MibTableColumn
opmen99810bPortConfCurrentFlowControlTx=_Opmen99810bPortConfCurrentFlowControlTx_Object((1,3,6,1,4,1,5205,2,94,2,1,1,1,7),_Opmen99810bPortConfCurrentFlowControlTx_Type())
opmen99810bPortConfCurrentFlowControlTx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortConfCurrentFlowControlTx.setStatus(_A)
class _Opmen99810bPortConfFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_F,1),(_f,2)))
_Opmen99810bPortConfFlowControl_Type.__name__=_C
_Opmen99810bPortConfFlowControl_Object=MibTableColumn
opmen99810bPortConfFlowControl=_Opmen99810bPortConfFlowControl_Object((1,3,6,1,4,1,5205,2,94,2,1,1,1,8),_Opmen99810bPortConfFlowControl_Type())
opmen99810bPortConfFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortConfFlowControl.setStatus(_A)
class _Opmen99810bPortConfMaxFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1518,9600))
_Opmen99810bPortConfMaxFrameSize_Type.__name__=_C
_Opmen99810bPortConfMaxFrameSize_Object=MibTableColumn
opmen99810bPortConfMaxFrameSize=_Opmen99810bPortConfMaxFrameSize_Object((1,3,6,1,4,1,5205,2,94,2,1,1,1,9),_Opmen99810bPortConfMaxFrameSize_Type())
opmen99810bPortConfMaxFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortConfMaxFrameSize.setStatus(_A)
class _Opmen99810bPortConfExcessiveCollisionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('discard',0),('restart',1),(_f,2)))
_Opmen99810bPortConfExcessiveCollisionMode_Type.__name__=_C
_Opmen99810bPortConfExcessiveCollisionMode_Object=MibTableColumn
opmen99810bPortConfExcessiveCollisionMode=_Opmen99810bPortConfExcessiveCollisionMode_Object((1,3,6,1,4,1,5205,2,94,2,1,1,1,10),_Opmen99810bPortConfExcessiveCollisionMode_Type())
opmen99810bPortConfExcessiveCollisionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortConfExcessiveCollisionMode.setStatus(_A)
class _Opmen99810bPortConfPowerControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_E,0),('actiphy',1),('dynamic',2),(_F,3),(_f,4)))
_Opmen99810bPortConfPowerControl_Type.__name__=_C
_Opmen99810bPortConfPowerControl_Object=MibTableColumn
opmen99810bPortConfPowerControl=_Opmen99810bPortConfPowerControl_Object((1,3,6,1,4,1,5205,2,94,2,1,1,1,11),_Opmen99810bPortConfPowerControl_Type())
opmen99810bPortConfPowerControl.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortConfPowerControl.setStatus(_A)
_Opmen99810bPortConfDescription_Type=DisplayString
_Opmen99810bPortConfDescription_Object=MibTableColumn
opmen99810bPortConfDescription=_Opmen99810bPortConfDescription_Object((1,3,6,1,4,1,5205,2,94,2,1,1,1,12),_Opmen99810bPortConfDescription_Type())
opmen99810bPortConfDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortConfDescription.setStatus(_A)
_Opmen99810bPortTrafficStatisticsTable_Object=MibTable
opmen99810bPortTrafficStatisticsTable=_Opmen99810bPortTrafficStatisticsTable_Object((1,3,6,1,4,1,5205,2,94,2,1,2))
if mibBuilder.loadTexts:opmen99810bPortTrafficStatisticsTable.setStatus(_A)
_Opmen99810bPortTrafficStatisticsEntry_Object=MibTableRow
opmen99810bPortTrafficStatisticsEntry=_Opmen99810bPortTrafficStatisticsEntry_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1))
opmen99810bPortTrafficStatisticsEntry.setIndexNames((0,_G,_A5))
if mibBuilder.loadTexts:opmen99810bPortTrafficStatisticsEntry.setStatus(_A)
class _Opmen99810bPortTrafficStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bPortTrafficStatisticsPort_Type.__name__=_C
_Opmen99810bPortTrafficStatisticsPort_Object=MibTableColumn
opmen99810bPortTrafficStatisticsPort=_Opmen99810bPortTrafficStatisticsPort_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,1),_Opmen99810bPortTrafficStatisticsPort_Type())
opmen99810bPortTrafficStatisticsPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bPortTrafficStatisticsPort.setStatus(_A)
class _Opmen99810bPortTrafficStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bPortTrafficStatisticsClear_Type.__name__=_C
_Opmen99810bPortTrafficStatisticsClear_Object=MibTableColumn
opmen99810bPortTrafficStatisticsClear=_Opmen99810bPortTrafficStatisticsClear_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,2),_Opmen99810bPortTrafficStatisticsClear_Type())
opmen99810bPortTrafficStatisticsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortTrafficStatisticsClear.setStatus(_A)
_Opmen99810bPortTrafficRxPackets_Type=Counter64
_Opmen99810bPortTrafficRxPackets_Object=MibTableColumn
opmen99810bPortTrafficRxPackets=_Opmen99810bPortTrafficRxPackets_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,3),_Opmen99810bPortTrafficRxPackets_Type())
opmen99810bPortTrafficRxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxPackets.setStatus(_A)
_Opmen99810bPortTrafficRxOctets_Type=Counter64
_Opmen99810bPortTrafficRxOctets_Object=MibTableColumn
opmen99810bPortTrafficRxOctets=_Opmen99810bPortTrafficRxOctets_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,4),_Opmen99810bPortTrafficRxOctets_Type())
opmen99810bPortTrafficRxOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxOctets.setStatus(_A)
_Opmen99810bPortTrafficRxUnicast_Type=Counter64
_Opmen99810bPortTrafficRxUnicast_Object=MibTableColumn
opmen99810bPortTrafficRxUnicast=_Opmen99810bPortTrafficRxUnicast_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,5),_Opmen99810bPortTrafficRxUnicast_Type())
opmen99810bPortTrafficRxUnicast.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxUnicast.setStatus(_A)
_Opmen99810bPortTrafficRxMulticast_Type=Counter64
_Opmen99810bPortTrafficRxMulticast_Object=MibTableColumn
opmen99810bPortTrafficRxMulticast=_Opmen99810bPortTrafficRxMulticast_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,6),_Opmen99810bPortTrafficRxMulticast_Type())
opmen99810bPortTrafficRxMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxMulticast.setStatus(_A)
_Opmen99810bPortTrafficRxBroadcast_Type=Counter64
_Opmen99810bPortTrafficRxBroadcast_Object=MibTableColumn
opmen99810bPortTrafficRxBroadcast=_Opmen99810bPortTrafficRxBroadcast_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,7),_Opmen99810bPortTrafficRxBroadcast_Type())
opmen99810bPortTrafficRxBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxBroadcast.setStatus(_A)
_Opmen99810bPortTrafficRxPause_Type=Counter64
_Opmen99810bPortTrafficRxPause_Object=MibTableColumn
opmen99810bPortTrafficRxPause=_Opmen99810bPortTrafficRxPause_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,8),_Opmen99810bPortTrafficRxPause_Type())
opmen99810bPortTrafficRxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxPause.setStatus(_A)
_Opmen99810bPortTrafficRx64Bytes_Type=Counter64
_Opmen99810bPortTrafficRx64Bytes_Object=MibTableColumn
opmen99810bPortTrafficRx64Bytes=_Opmen99810bPortTrafficRx64Bytes_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,9),_Opmen99810bPortTrafficRx64Bytes_Type())
opmen99810bPortTrafficRx64Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRx64Bytes.setStatus(_A)
_Opmen99810bPortTrafficRx65to127Bytes_Type=Counter64
_Opmen99810bPortTrafficRx65to127Bytes_Object=MibTableColumn
opmen99810bPortTrafficRx65to127Bytes=_Opmen99810bPortTrafficRx65to127Bytes_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,10),_Opmen99810bPortTrafficRx65to127Bytes_Type())
opmen99810bPortTrafficRx65to127Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRx65to127Bytes.setStatus(_A)
_Opmen99810bPortTrafficRx128to255Bytes_Type=Counter64
_Opmen99810bPortTrafficRx128to255Bytes_Object=MibTableColumn
opmen99810bPortTrafficRx128to255Bytes=_Opmen99810bPortTrafficRx128to255Bytes_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,11),_Opmen99810bPortTrafficRx128to255Bytes_Type())
opmen99810bPortTrafficRx128to255Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRx128to255Bytes.setStatus(_A)
_Opmen99810bPortTrafficRx256to511Bytes_Type=Counter64
_Opmen99810bPortTrafficRx256to511Bytes_Object=MibTableColumn
opmen99810bPortTrafficRx256to511Bytes=_Opmen99810bPortTrafficRx256to511Bytes_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,12),_Opmen99810bPortTrafficRx256to511Bytes_Type())
opmen99810bPortTrafficRx256to511Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRx256to511Bytes.setStatus(_A)
_Opmen99810bPortTrafficRx512to1023Bytes_Type=Counter64
_Opmen99810bPortTrafficRx512to1023Bytes_Object=MibTableColumn
opmen99810bPortTrafficRx512to1023Bytes=_Opmen99810bPortTrafficRx512to1023Bytes_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,13),_Opmen99810bPortTrafficRx512to1023Bytes_Type())
opmen99810bPortTrafficRx512to1023Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRx512to1023Bytes.setStatus(_A)
_Opmen99810bPortTrafficRx1024to1526Bytes_Type=Counter64
_Opmen99810bPortTrafficRx1024to1526Bytes_Object=MibTableColumn
opmen99810bPortTrafficRx1024to1526Bytes=_Opmen99810bPortTrafficRx1024to1526Bytes_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,14),_Opmen99810bPortTrafficRx1024to1526Bytes_Type())
opmen99810bPortTrafficRx1024to1526Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRx1024to1526Bytes.setStatus(_A)
_Opmen99810bPortTrafficRxExceecd1527Bytes_Type=Counter64
_Opmen99810bPortTrafficRxExceecd1527Bytes_Object=MibTableColumn
opmen99810bPortTrafficRxExceecd1527Bytes=_Opmen99810bPortTrafficRxExceecd1527Bytes_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,15),_Opmen99810bPortTrafficRxExceecd1527Bytes_Type())
opmen99810bPortTrafficRxExceecd1527Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxExceecd1527Bytes.setStatus(_A)
_Opmen99810bPortTrafficRxQ0_Type=Counter64
_Opmen99810bPortTrafficRxQ0_Object=MibTableColumn
opmen99810bPortTrafficRxQ0=_Opmen99810bPortTrafficRxQ0_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,16),_Opmen99810bPortTrafficRxQ0_Type())
opmen99810bPortTrafficRxQ0.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxQ0.setStatus(_A)
_Opmen99810bPortTrafficRxQ1_Type=Counter64
_Opmen99810bPortTrafficRxQ1_Object=MibTableColumn
opmen99810bPortTrafficRxQ1=_Opmen99810bPortTrafficRxQ1_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,17),_Opmen99810bPortTrafficRxQ1_Type())
opmen99810bPortTrafficRxQ1.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxQ1.setStatus(_A)
_Opmen99810bPortTrafficRxQ2_Type=Counter64
_Opmen99810bPortTrafficRxQ2_Object=MibTableColumn
opmen99810bPortTrafficRxQ2=_Opmen99810bPortTrafficRxQ2_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,18),_Opmen99810bPortTrafficRxQ2_Type())
opmen99810bPortTrafficRxQ2.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxQ2.setStatus(_A)
_Opmen99810bPortTrafficRxQ3_Type=Counter64
_Opmen99810bPortTrafficRxQ3_Object=MibTableColumn
opmen99810bPortTrafficRxQ3=_Opmen99810bPortTrafficRxQ3_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,19),_Opmen99810bPortTrafficRxQ3_Type())
opmen99810bPortTrafficRxQ3.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxQ3.setStatus(_A)
_Opmen99810bPortTrafficRxQ4_Type=Counter64
_Opmen99810bPortTrafficRxQ4_Object=MibTableColumn
opmen99810bPortTrafficRxQ4=_Opmen99810bPortTrafficRxQ4_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,20),_Opmen99810bPortTrafficRxQ4_Type())
opmen99810bPortTrafficRxQ4.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxQ4.setStatus(_A)
_Opmen99810bPortTrafficRxQ5_Type=Counter64
_Opmen99810bPortTrafficRxQ5_Object=MibTableColumn
opmen99810bPortTrafficRxQ5=_Opmen99810bPortTrafficRxQ5_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,21),_Opmen99810bPortTrafficRxQ5_Type())
opmen99810bPortTrafficRxQ5.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxQ5.setStatus(_A)
_Opmen99810bPortTrafficRxQ6_Type=Counter64
_Opmen99810bPortTrafficRxQ6_Object=MibTableColumn
opmen99810bPortTrafficRxQ6=_Opmen99810bPortTrafficRxQ6_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,22),_Opmen99810bPortTrafficRxQ6_Type())
opmen99810bPortTrafficRxQ6.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxQ6.setStatus(_A)
_Opmen99810bPortTrafficRxQ7_Type=Counter64
_Opmen99810bPortTrafficRxQ7_Object=MibTableColumn
opmen99810bPortTrafficRxQ7=_Opmen99810bPortTrafficRxQ7_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,23),_Opmen99810bPortTrafficRxQ7_Type())
opmen99810bPortTrafficRxQ7.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxQ7.setStatus(_A)
_Opmen99810bPortTrafficRxDrops_Type=Counter64
_Opmen99810bPortTrafficRxDrops_Object=MibTableColumn
opmen99810bPortTrafficRxDrops=_Opmen99810bPortTrafficRxDrops_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,24),_Opmen99810bPortTrafficRxDrops_Type())
opmen99810bPortTrafficRxDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxDrops.setStatus(_A)
_Opmen99810bPortTrafficRxCRCorAlignment_Type=Counter64
_Opmen99810bPortTrafficRxCRCorAlignment_Object=MibTableColumn
opmen99810bPortTrafficRxCRCorAlignment=_Opmen99810bPortTrafficRxCRCorAlignment_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,25),_Opmen99810bPortTrafficRxCRCorAlignment_Type())
opmen99810bPortTrafficRxCRCorAlignment.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxCRCorAlignment.setStatus(_A)
_Opmen99810bPortTrafficRxUndersize_Type=Counter64
_Opmen99810bPortTrafficRxUndersize_Object=MibTableColumn
opmen99810bPortTrafficRxUndersize=_Opmen99810bPortTrafficRxUndersize_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,26),_Opmen99810bPortTrafficRxUndersize_Type())
opmen99810bPortTrafficRxUndersize.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxUndersize.setStatus(_A)
_Opmen99810bPortTrafficRxOversize_Type=Counter64
_Opmen99810bPortTrafficRxOversize_Object=MibTableColumn
opmen99810bPortTrafficRxOversize=_Opmen99810bPortTrafficRxOversize_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,27),_Opmen99810bPortTrafficRxOversize_Type())
opmen99810bPortTrafficRxOversize.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxOversize.setStatus(_A)
_Opmen99810bPortTrafficRxFragments_Type=Counter64
_Opmen99810bPortTrafficRxFragments_Object=MibTableColumn
opmen99810bPortTrafficRxFragments=_Opmen99810bPortTrafficRxFragments_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,28),_Opmen99810bPortTrafficRxFragments_Type())
opmen99810bPortTrafficRxFragments.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxFragments.setStatus(_A)
_Opmen99810bPortTrafficRxJabber_Type=Counter64
_Opmen99810bPortTrafficRxJabber_Object=MibTableColumn
opmen99810bPortTrafficRxJabber=_Opmen99810bPortTrafficRxJabber_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,29),_Opmen99810bPortTrafficRxJabber_Type())
opmen99810bPortTrafficRxJabber.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxJabber.setStatus(_A)
_Opmen99810bPortTrafficRxFiltered_Type=Counter64
_Opmen99810bPortTrafficRxFiltered_Object=MibTableColumn
opmen99810bPortTrafficRxFiltered=_Opmen99810bPortTrafficRxFiltered_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,30),_Opmen99810bPortTrafficRxFiltered_Type())
opmen99810bPortTrafficRxFiltered.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficRxFiltered.setStatus(_A)
_Opmen99810bPortTrafficTxPackets_Type=Counter64
_Opmen99810bPortTrafficTxPackets_Object=MibTableColumn
opmen99810bPortTrafficTxPackets=_Opmen99810bPortTrafficTxPackets_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,31),_Opmen99810bPortTrafficTxPackets_Type())
opmen99810bPortTrafficTxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxPackets.setStatus(_A)
_Opmen99810bPortTrafficTxOctets_Type=Counter64
_Opmen99810bPortTrafficTxOctets_Object=MibTableColumn
opmen99810bPortTrafficTxOctets=_Opmen99810bPortTrafficTxOctets_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,32),_Opmen99810bPortTrafficTxOctets_Type())
opmen99810bPortTrafficTxOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxOctets.setStatus(_A)
_Opmen99810bPortTrafficTxUnicast_Type=Counter64
_Opmen99810bPortTrafficTxUnicast_Object=MibTableColumn
opmen99810bPortTrafficTxUnicast=_Opmen99810bPortTrafficTxUnicast_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,33),_Opmen99810bPortTrafficTxUnicast_Type())
opmen99810bPortTrafficTxUnicast.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxUnicast.setStatus(_A)
_Opmen99810bPortTrafficTxMulticast_Type=Counter64
_Opmen99810bPortTrafficTxMulticast_Object=MibTableColumn
opmen99810bPortTrafficTxMulticast=_Opmen99810bPortTrafficTxMulticast_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,34),_Opmen99810bPortTrafficTxMulticast_Type())
opmen99810bPortTrafficTxMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxMulticast.setStatus(_A)
_Opmen99810bPortTrafficTxBroadcast_Type=Counter64
_Opmen99810bPortTrafficTxBroadcast_Object=MibTableColumn
opmen99810bPortTrafficTxBroadcast=_Opmen99810bPortTrafficTxBroadcast_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,35),_Opmen99810bPortTrafficTxBroadcast_Type())
opmen99810bPortTrafficTxBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxBroadcast.setStatus(_A)
_Opmen99810bPortTrafficTxPause_Type=Counter64
_Opmen99810bPortTrafficTxPause_Object=MibTableColumn
opmen99810bPortTrafficTxPause=_Opmen99810bPortTrafficTxPause_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,36),_Opmen99810bPortTrafficTxPause_Type())
opmen99810bPortTrafficTxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxPause.setStatus(_A)
_Opmen99810bPortTrafficTx64Bytes_Type=Counter64
_Opmen99810bPortTrafficTx64Bytes_Object=MibTableColumn
opmen99810bPortTrafficTx64Bytes=_Opmen99810bPortTrafficTx64Bytes_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,37),_Opmen99810bPortTrafficTx64Bytes_Type())
opmen99810bPortTrafficTx64Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTx64Bytes.setStatus(_A)
_Opmen99810bPortTrafficTx65to127Bytes_Type=Counter64
_Opmen99810bPortTrafficTx65to127Bytes_Object=MibTableColumn
opmen99810bPortTrafficTx65to127Bytes=_Opmen99810bPortTrafficTx65to127Bytes_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,38),_Opmen99810bPortTrafficTx65to127Bytes_Type())
opmen99810bPortTrafficTx65to127Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTx65to127Bytes.setStatus(_A)
_Opmen99810bPortTrafficTx128to255Bytes_Type=Counter64
_Opmen99810bPortTrafficTx128to255Bytes_Object=MibTableColumn
opmen99810bPortTrafficTx128to255Bytes=_Opmen99810bPortTrafficTx128to255Bytes_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,39),_Opmen99810bPortTrafficTx128to255Bytes_Type())
opmen99810bPortTrafficTx128to255Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTx128to255Bytes.setStatus(_A)
_Opmen99810bPortTrafficTx256to511Bytes_Type=Counter64
_Opmen99810bPortTrafficTx256to511Bytes_Object=MibTableColumn
opmen99810bPortTrafficTx256to511Bytes=_Opmen99810bPortTrafficTx256to511Bytes_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,40),_Opmen99810bPortTrafficTx256to511Bytes_Type())
opmen99810bPortTrafficTx256to511Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTx256to511Bytes.setStatus(_A)
_Opmen99810bPortTrafficTx512to1023Bytes_Type=Counter64
_Opmen99810bPortTrafficTx512to1023Bytes_Object=MibTableColumn
opmen99810bPortTrafficTx512to1023Bytes=_Opmen99810bPortTrafficTx512to1023Bytes_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,41),_Opmen99810bPortTrafficTx512to1023Bytes_Type())
opmen99810bPortTrafficTx512to1023Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTx512to1023Bytes.setStatus(_A)
_Opmen99810bPortTrafficTx1024to1526Bytes_Type=Counter64
_Opmen99810bPortTrafficTx1024to1526Bytes_Object=MibTableColumn
opmen99810bPortTrafficTx1024to1526Bytes=_Opmen99810bPortTrafficTx1024to1526Bytes_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,42),_Opmen99810bPortTrafficTx1024to1526Bytes_Type())
opmen99810bPortTrafficTx1024to1526Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTx1024to1526Bytes.setStatus(_A)
_Opmen99810bPortTrafficTxExceecd1527Bytes_Type=Counter64
_Opmen99810bPortTrafficTxExceecd1527Bytes_Object=MibTableColumn
opmen99810bPortTrafficTxExceecd1527Bytes=_Opmen99810bPortTrafficTxExceecd1527Bytes_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,43),_Opmen99810bPortTrafficTxExceecd1527Bytes_Type())
opmen99810bPortTrafficTxExceecd1527Bytes.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxExceecd1527Bytes.setStatus(_A)
_Opmen99810bPortTrafficTxQ0_Type=Counter64
_Opmen99810bPortTrafficTxQ0_Object=MibTableColumn
opmen99810bPortTrafficTxQ0=_Opmen99810bPortTrafficTxQ0_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,44),_Opmen99810bPortTrafficTxQ0_Type())
opmen99810bPortTrafficTxQ0.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxQ0.setStatus(_A)
_Opmen99810bPortTrafficTxQ1_Type=Counter64
_Opmen99810bPortTrafficTxQ1_Object=MibTableColumn
opmen99810bPortTrafficTxQ1=_Opmen99810bPortTrafficTxQ1_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,45),_Opmen99810bPortTrafficTxQ1_Type())
opmen99810bPortTrafficTxQ1.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxQ1.setStatus(_A)
_Opmen99810bPortTrafficTxQ2_Type=Counter64
_Opmen99810bPortTrafficTxQ2_Object=MibTableColumn
opmen99810bPortTrafficTxQ2=_Opmen99810bPortTrafficTxQ2_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,46),_Opmen99810bPortTrafficTxQ2_Type())
opmen99810bPortTrafficTxQ2.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxQ2.setStatus(_A)
_Opmen99810bPortTrafficTxQ3_Type=Counter64
_Opmen99810bPortTrafficTxQ3_Object=MibTableColumn
opmen99810bPortTrafficTxQ3=_Opmen99810bPortTrafficTxQ3_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,47),_Opmen99810bPortTrafficTxQ3_Type())
opmen99810bPortTrafficTxQ3.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxQ3.setStatus(_A)
_Opmen99810bPortTrafficTxQ4_Type=Counter64
_Opmen99810bPortTrafficTxQ4_Object=MibTableColumn
opmen99810bPortTrafficTxQ4=_Opmen99810bPortTrafficTxQ4_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,48),_Opmen99810bPortTrafficTxQ4_Type())
opmen99810bPortTrafficTxQ4.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxQ4.setStatus(_A)
_Opmen99810bPortTrafficTxQ5_Type=Counter64
_Opmen99810bPortTrafficTxQ5_Object=MibTableColumn
opmen99810bPortTrafficTxQ5=_Opmen99810bPortTrafficTxQ5_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,49),_Opmen99810bPortTrafficTxQ5_Type())
opmen99810bPortTrafficTxQ5.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxQ5.setStatus(_A)
_Opmen99810bPortTrafficTxQ6_Type=Counter64
_Opmen99810bPortTrafficTxQ6_Object=MibTableColumn
opmen99810bPortTrafficTxQ6=_Opmen99810bPortTrafficTxQ6_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,50),_Opmen99810bPortTrafficTxQ6_Type())
opmen99810bPortTrafficTxQ6.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxQ6.setStatus(_A)
_Opmen99810bPortTrafficTxQ7_Type=Counter64
_Opmen99810bPortTrafficTxQ7_Object=MibTableColumn
opmen99810bPortTrafficTxQ7=_Opmen99810bPortTrafficTxQ7_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,51),_Opmen99810bPortTrafficTxQ7_Type())
opmen99810bPortTrafficTxQ7.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxQ7.setStatus(_A)
_Opmen99810bPortTrafficTxDrops_Type=Counter64
_Opmen99810bPortTrafficTxDrops_Object=MibTableColumn
opmen99810bPortTrafficTxDrops=_Opmen99810bPortTrafficTxDrops_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,52),_Opmen99810bPortTrafficTxDrops_Type())
opmen99810bPortTrafficTxDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxDrops.setStatus(_A)
_Opmen99810bPortTrafficTxLateOrExcColl_Type=Counter64
_Opmen99810bPortTrafficTxLateOrExcColl_Object=MibTableColumn
opmen99810bPortTrafficTxLateOrExcColl=_Opmen99810bPortTrafficTxLateOrExcColl_Object((1,3,6,1,4,1,5205,2,94,2,1,2,1,53),_Opmen99810bPortTrafficTxLateOrExcColl_Type())
opmen99810bPortTrafficTxLateOrExcColl.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortTrafficTxLateOrExcColl.setStatus(_A)
_Opmen99810bPortQoSStatistics_ObjectIdentity=ObjectIdentity
opmen99810bPortQoSStatistics=_Opmen99810bPortQoSStatistics_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,1,3))
class _Opmen99810bPortQoSStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_e,1)))
_Opmen99810bPortQoSStatisticsClear_Type.__name__=_C
_Opmen99810bPortQoSStatisticsClear_Object=MibScalar
opmen99810bPortQoSStatisticsClear=_Opmen99810bPortQoSStatisticsClear_Object((1,3,6,1,4,1,5205,2,94,2,1,3,1),_Opmen99810bPortQoSStatisticsClear_Type())
opmen99810bPortQoSStatisticsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSStatisticsClear.setStatus(_A)
_Opmen99810bPortQoSStatisticsTable_Object=MibTable
opmen99810bPortQoSStatisticsTable=_Opmen99810bPortQoSStatisticsTable_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2))
if mibBuilder.loadTexts:opmen99810bPortQoSStatisticsTable.setStatus(_A)
_Opmen99810bPortQoSStatisticsEntry_Object=MibTableRow
opmen99810bPortQoSStatisticsEntry=_Opmen99810bPortQoSStatisticsEntry_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1))
opmen99810bPortQoSStatisticsEntry.setIndexNames((0,_G,_A6))
if mibBuilder.loadTexts:opmen99810bPortQoSStatisticsEntry.setStatus(_A)
class _Opmen99810bPortQoSStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bPortQoSStatisticsPort_Type.__name__=_C
_Opmen99810bPortQoSStatisticsPort_Object=MibTableColumn
opmen99810bPortQoSStatisticsPort=_Opmen99810bPortQoSStatisticsPort_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,1),_Opmen99810bPortQoSStatisticsPort_Type())
opmen99810bPortQoSStatisticsPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bPortQoSStatisticsPort.setStatus(_A)
_Opmen99810bPortQoSQ0Rx_Type=Counter64
_Opmen99810bPortQoSQ0Rx_Object=MibTableColumn
opmen99810bPortQoSQ0Rx=_Opmen99810bPortQoSQ0Rx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,2),_Opmen99810bPortQoSQ0Rx_Type())
opmen99810bPortQoSQ0Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ0Rx.setStatus(_A)
_Opmen99810bPortQoSQ0Tx_Type=Counter64
_Opmen99810bPortQoSQ0Tx_Object=MibTableColumn
opmen99810bPortQoSQ0Tx=_Opmen99810bPortQoSQ0Tx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,3),_Opmen99810bPortQoSQ0Tx_Type())
opmen99810bPortQoSQ0Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ0Tx.setStatus(_A)
_Opmen99810bPortQoSQ1Rx_Type=Counter64
_Opmen99810bPortQoSQ1Rx_Object=MibTableColumn
opmen99810bPortQoSQ1Rx=_Opmen99810bPortQoSQ1Rx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,4),_Opmen99810bPortQoSQ1Rx_Type())
opmen99810bPortQoSQ1Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ1Rx.setStatus(_A)
_Opmen99810bPortQoSQ1Tx_Type=Counter64
_Opmen99810bPortQoSQ1Tx_Object=MibTableColumn
opmen99810bPortQoSQ1Tx=_Opmen99810bPortQoSQ1Tx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,5),_Opmen99810bPortQoSQ1Tx_Type())
opmen99810bPortQoSQ1Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ1Tx.setStatus(_A)
_Opmen99810bPortQoSQ2Rx_Type=Counter64
_Opmen99810bPortQoSQ2Rx_Object=MibTableColumn
opmen99810bPortQoSQ2Rx=_Opmen99810bPortQoSQ2Rx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,6),_Opmen99810bPortQoSQ2Rx_Type())
opmen99810bPortQoSQ2Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ2Rx.setStatus(_A)
_Opmen99810bPortQoSQ2Tx_Type=Counter64
_Opmen99810bPortQoSQ2Tx_Object=MibTableColumn
opmen99810bPortQoSQ2Tx=_Opmen99810bPortQoSQ2Tx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,7),_Opmen99810bPortQoSQ2Tx_Type())
opmen99810bPortQoSQ2Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ2Tx.setStatus(_A)
_Opmen99810bPortQoSQ3Rx_Type=Counter64
_Opmen99810bPortQoSQ3Rx_Object=MibTableColumn
opmen99810bPortQoSQ3Rx=_Opmen99810bPortQoSQ3Rx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,8),_Opmen99810bPortQoSQ3Rx_Type())
opmen99810bPortQoSQ3Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ3Rx.setStatus(_A)
_Opmen99810bPortQoSQ3Tx_Type=Counter64
_Opmen99810bPortQoSQ3Tx_Object=MibTableColumn
opmen99810bPortQoSQ3Tx=_Opmen99810bPortQoSQ3Tx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,9),_Opmen99810bPortQoSQ3Tx_Type())
opmen99810bPortQoSQ3Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ3Tx.setStatus(_A)
_Opmen99810bPortQoSQ4Rx_Type=Counter64
_Opmen99810bPortQoSQ4Rx_Object=MibTableColumn
opmen99810bPortQoSQ4Rx=_Opmen99810bPortQoSQ4Rx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,10),_Opmen99810bPortQoSQ4Rx_Type())
opmen99810bPortQoSQ4Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ4Rx.setStatus(_A)
_Opmen99810bPortQoSQ4Tx_Type=Counter64
_Opmen99810bPortQoSQ4Tx_Object=MibTableColumn
opmen99810bPortQoSQ4Tx=_Opmen99810bPortQoSQ4Tx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,11),_Opmen99810bPortQoSQ4Tx_Type())
opmen99810bPortQoSQ4Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ4Tx.setStatus(_A)
_Opmen99810bPortQoSQ5Rx_Type=Counter64
_Opmen99810bPortQoSQ5Rx_Object=MibTableColumn
opmen99810bPortQoSQ5Rx=_Opmen99810bPortQoSQ5Rx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,12),_Opmen99810bPortQoSQ5Rx_Type())
opmen99810bPortQoSQ5Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ5Rx.setStatus(_A)
_Opmen99810bPortQoSQ5Tx_Type=Counter64
_Opmen99810bPortQoSQ5Tx_Object=MibTableColumn
opmen99810bPortQoSQ5Tx=_Opmen99810bPortQoSQ5Tx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,13),_Opmen99810bPortQoSQ5Tx_Type())
opmen99810bPortQoSQ5Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ5Tx.setStatus(_A)
_Opmen99810bPortQoSQ6Rx_Type=Counter64
_Opmen99810bPortQoSQ6Rx_Object=MibTableColumn
opmen99810bPortQoSQ6Rx=_Opmen99810bPortQoSQ6Rx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,14),_Opmen99810bPortQoSQ6Rx_Type())
opmen99810bPortQoSQ6Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ6Rx.setStatus(_A)
_Opmen99810bPortQoSQ6Tx_Type=Counter64
_Opmen99810bPortQoSQ6Tx_Object=MibTableColumn
opmen99810bPortQoSQ6Tx=_Opmen99810bPortQoSQ6Tx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,15),_Opmen99810bPortQoSQ6Tx_Type())
opmen99810bPortQoSQ6Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ6Tx.setStatus(_A)
_Opmen99810bPortQoSQ7Rx_Type=Counter64
_Opmen99810bPortQoSQ7Rx_Object=MibTableColumn
opmen99810bPortQoSQ7Rx=_Opmen99810bPortQoSQ7Rx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,16),_Opmen99810bPortQoSQ7Rx_Type())
opmen99810bPortQoSQ7Rx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ7Rx.setStatus(_A)
_Opmen99810bPortQoSQ7Tx_Type=Counter64
_Opmen99810bPortQoSQ7Tx_Object=MibTableColumn
opmen99810bPortQoSQ7Tx=_Opmen99810bPortQoSQ7Tx_Object((1,3,6,1,4,1,5205,2,94,2,1,3,2,1,17),_Opmen99810bPortQoSQ7Tx_Type())
opmen99810bPortQoSQ7Tx.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortQoSQ7Tx.setStatus(_A)
_Opmen99810bSFPInfoTable_Object=MibTable
opmen99810bSFPInfoTable=_Opmen99810bSFPInfoTable_Object((1,3,6,1,4,1,5205,2,94,2,1,4))
if mibBuilder.loadTexts:opmen99810bSFPInfoTable.setStatus(_A)
_Opmen99810bSFPInfoEntry_Object=MibTableRow
opmen99810bSFPInfoEntry=_Opmen99810bSFPInfoEntry_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1))
opmen99810bSFPInfoEntry.setIndexNames((0,_G,_A7))
if mibBuilder.loadTexts:opmen99810bSFPInfoEntry.setStatus(_A)
class _Opmen99810bSFPInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bSFPInfoIndex_Type.__name__=_C
_Opmen99810bSFPInfoIndex_Object=MibTableColumn
opmen99810bSFPInfoIndex=_Opmen99810bSFPInfoIndex_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,1),_Opmen99810bSFPInfoIndex_Type())
opmen99810bSFPInfoIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bSFPInfoIndex.setStatus(_A)
_Opmen99810bSFPInfoPort_Type=DisplayString
_Opmen99810bSFPInfoPort_Object=MibTableColumn
opmen99810bSFPInfoPort=_Opmen99810bSFPInfoPort_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,2),_Opmen99810bSFPInfoPort_Type())
opmen99810bSFPInfoPort.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPInfoPort.setStatus(_A)
_Opmen99810bSFPConnectorType_Type=DisplayString
_Opmen99810bSFPConnectorType_Object=MibTableColumn
opmen99810bSFPConnectorType=_Opmen99810bSFPConnectorType_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,3),_Opmen99810bSFPConnectorType_Type())
opmen99810bSFPConnectorType.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPConnectorType.setStatus(_A)
_Opmen99810bSFPFiberType_Type=DisplayString
_Opmen99810bSFPFiberType_Object=MibTableColumn
opmen99810bSFPFiberType=_Opmen99810bSFPFiberType_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,4),_Opmen99810bSFPFiberType_Type())
opmen99810bSFPFiberType.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPFiberType.setStatus(_A)
_Opmen99810bSFPTxCentralWavelength_Type=DisplayString
_Opmen99810bSFPTxCentralWavelength_Object=MibTableColumn
opmen99810bSFPTxCentralWavelength=_Opmen99810bSFPTxCentralWavelength_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,5),_Opmen99810bSFPTxCentralWavelength_Type())
opmen99810bSFPTxCentralWavelength.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPTxCentralWavelength.setStatus(_A)
_Opmen99810bSFPBaudRate_Type=DisplayString
_Opmen99810bSFPBaudRate_Object=MibTableColumn
opmen99810bSFPBaudRate=_Opmen99810bSFPBaudRate_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,6),_Opmen99810bSFPBaudRate_Type())
opmen99810bSFPBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPBaudRate.setStatus(_A)
_Opmen99810bSFPVendorOUI_Type=DisplayString
_Opmen99810bSFPVendorOUI_Object=MibTableColumn
opmen99810bSFPVendorOUI=_Opmen99810bSFPVendorOUI_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,7),_Opmen99810bSFPVendorOUI_Type())
opmen99810bSFPVendorOUI.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPVendorOUI.setStatus(_A)
_Opmen99810bSFPVendorName_Type=DisplayString
_Opmen99810bSFPVendorName_Object=MibTableColumn
opmen99810bSFPVendorName=_Opmen99810bSFPVendorName_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,8),_Opmen99810bSFPVendorName_Type())
opmen99810bSFPVendorName.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPVendorName.setStatus(_A)
_Opmen99810bSFPVendorPN_Type=DisplayString
_Opmen99810bSFPVendorPN_Object=MibTableColumn
opmen99810bSFPVendorPN=_Opmen99810bSFPVendorPN_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,9),_Opmen99810bSFPVendorPN_Type())
opmen99810bSFPVendorPN.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPVendorPN.setStatus(_A)
_Opmen99810bSFPVendorRev_Type=DisplayString
_Opmen99810bSFPVendorRev_Object=MibTableColumn
opmen99810bSFPVendorRev=_Opmen99810bSFPVendorRev_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,10),_Opmen99810bSFPVendorRev_Type())
opmen99810bSFPVendorRev.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPVendorRev.setStatus(_A)
_Opmen99810bSFPVendorSN_Type=DisplayString
_Opmen99810bSFPVendorSN_Object=MibTableColumn
opmen99810bSFPVendorSN=_Opmen99810bSFPVendorSN_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,11),_Opmen99810bSFPVendorSN_Type())
opmen99810bSFPVendorSN.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPVendorSN.setStatus(_A)
_Opmen99810bSFPDateCode_Type=DisplayString
_Opmen99810bSFPDateCode_Object=MibTableColumn
opmen99810bSFPDateCode=_Opmen99810bSFPDateCode_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,12),_Opmen99810bSFPDateCode_Type())
opmen99810bSFPDateCode.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPDateCode.setStatus(_A)
_Opmen99810bSFPTemperature_Type=DisplayString
_Opmen99810bSFPTemperature_Object=MibTableColumn
opmen99810bSFPTemperature=_Opmen99810bSFPTemperature_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,13),_Opmen99810bSFPTemperature_Type())
opmen99810bSFPTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPTemperature.setStatus(_A)
_Opmen99810bSFPVcc_Type=DisplayString
_Opmen99810bSFPVcc_Object=MibTableColumn
opmen99810bSFPVcc=_Opmen99810bSFPVcc_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,14),_Opmen99810bSFPVcc_Type())
opmen99810bSFPVcc.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPVcc.setStatus(_A)
_Opmen99810bSFPMon1Bias_Type=DisplayString
_Opmen99810bSFPMon1Bias_Object=MibTableColumn
opmen99810bSFPMon1Bias=_Opmen99810bSFPMon1Bias_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,15),_Opmen99810bSFPMon1Bias_Type())
opmen99810bSFPMon1Bias.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPMon1Bias.setStatus(_A)
_Opmen99810bSFPMon2TxPWR_Type=DisplayString
_Opmen99810bSFPMon2TxPWR_Object=MibTableColumn
opmen99810bSFPMon2TxPWR=_Opmen99810bSFPMon2TxPWR_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,16),_Opmen99810bSFPMon2TxPWR_Type())
opmen99810bSFPMon2TxPWR.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPMon2TxPWR.setStatus(_A)
_Opmen99810bSFPMon3RxPWR_Type=DisplayString
_Opmen99810bSFPMon3RxPWR_Object=MibTableColumn
opmen99810bSFPMon3RxPWR=_Opmen99810bSFPMon3RxPWR_Object((1,3,6,1,4,1,5205,2,94,2,1,4,1,17),_Opmen99810bSFPMon3RxPWR_Type())
opmen99810bSFPMon3RxPWR.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSFPMon3RxPWR.setStatus(_A)
_Opmen99810bPortEEETable_Object=MibTable
opmen99810bPortEEETable=_Opmen99810bPortEEETable_Object((1,3,6,1,4,1,5205,2,94,2,1,5))
if mibBuilder.loadTexts:opmen99810bPortEEETable.setStatus(_A)
_Opmen99810bPortEEEEntry_Object=MibTableRow
opmen99810bPortEEEEntry=_Opmen99810bPortEEEEntry_Object((1,3,6,1,4,1,5205,2,94,2,1,5,1))
opmen99810bPortEEEEntry.setIndexNames((0,_G,_A8))
if mibBuilder.loadTexts:opmen99810bPortEEEEntry.setStatus(_A)
class _Opmen99810bPortEEEPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bPortEEEPort_Type.__name__=_C
_Opmen99810bPortEEEPort_Object=MibTableColumn
opmen99810bPortEEEPort=_Opmen99810bPortEEEPort_Object((1,3,6,1,4,1,5205,2,94,2,1,5,1,1),_Opmen99810bPortEEEPort_Type())
opmen99810bPortEEEPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bPortEEEPort.setStatus(_A)
class _Opmen99810bPortEEEMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bPortEEEMode_Type.__name__=_C
_Opmen99810bPortEEEMode_Object=MibTableColumn
opmen99810bPortEEEMode=_Opmen99810bPortEEEMode_Object((1,3,6,1,4,1,5205,2,94,2,1,5,1,2),_Opmen99810bPortEEEMode_Type())
opmen99810bPortEEEMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortEEEMode.setStatus(_A)
class _Opmen99810bPortEEEUrgentQueue1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bPortEEEUrgentQueue1_Type.__name__=_C
_Opmen99810bPortEEEUrgentQueue1_Object=MibTableColumn
opmen99810bPortEEEUrgentQueue1=_Opmen99810bPortEEEUrgentQueue1_Object((1,3,6,1,4,1,5205,2,94,2,1,5,1,3),_Opmen99810bPortEEEUrgentQueue1_Type())
opmen99810bPortEEEUrgentQueue1.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortEEEUrgentQueue1.setStatus(_A)
class _Opmen99810bPortEEEUrgentQueue2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bPortEEEUrgentQueue2_Type.__name__=_C
_Opmen99810bPortEEEUrgentQueue2_Object=MibTableColumn
opmen99810bPortEEEUrgentQueue2=_Opmen99810bPortEEEUrgentQueue2_Object((1,3,6,1,4,1,5205,2,94,2,1,5,1,4),_Opmen99810bPortEEEUrgentQueue2_Type())
opmen99810bPortEEEUrgentQueue2.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortEEEUrgentQueue2.setStatus(_A)
class _Opmen99810bPortEEEUrgentQueue3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bPortEEEUrgentQueue3_Type.__name__=_C
_Opmen99810bPortEEEUrgentQueue3_Object=MibTableColumn
opmen99810bPortEEEUrgentQueue3=_Opmen99810bPortEEEUrgentQueue3_Object((1,3,6,1,4,1,5205,2,94,2,1,5,1,5),_Opmen99810bPortEEEUrgentQueue3_Type())
opmen99810bPortEEEUrgentQueue3.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortEEEUrgentQueue3.setStatus(_A)
class _Opmen99810bPortEEEUrgentQueue4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bPortEEEUrgentQueue4_Type.__name__=_C
_Opmen99810bPortEEEUrgentQueue4_Object=MibTableColumn
opmen99810bPortEEEUrgentQueue4=_Opmen99810bPortEEEUrgentQueue4_Object((1,3,6,1,4,1,5205,2,94,2,1,5,1,6),_Opmen99810bPortEEEUrgentQueue4_Type())
opmen99810bPortEEEUrgentQueue4.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortEEEUrgentQueue4.setStatus(_A)
class _Opmen99810bPortEEEUrgentQueue5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bPortEEEUrgentQueue5_Type.__name__=_C
_Opmen99810bPortEEEUrgentQueue5_Object=MibTableColumn
opmen99810bPortEEEUrgentQueue5=_Opmen99810bPortEEEUrgentQueue5_Object((1,3,6,1,4,1,5205,2,94,2,1,5,1,7),_Opmen99810bPortEEEUrgentQueue5_Type())
opmen99810bPortEEEUrgentQueue5.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortEEEUrgentQueue5.setStatus(_A)
class _Opmen99810bPortEEEUrgentQueue6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bPortEEEUrgentQueue6_Type.__name__=_C
_Opmen99810bPortEEEUrgentQueue6_Object=MibTableColumn
opmen99810bPortEEEUrgentQueue6=_Opmen99810bPortEEEUrgentQueue6_Object((1,3,6,1,4,1,5205,2,94,2,1,5,1,8),_Opmen99810bPortEEEUrgentQueue6_Type())
opmen99810bPortEEEUrgentQueue6.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortEEEUrgentQueue6.setStatus(_A)
class _Opmen99810bPortEEEUrgentQueue7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bPortEEEUrgentQueue7_Type.__name__=_C
_Opmen99810bPortEEEUrgentQueue7_Object=MibTableColumn
opmen99810bPortEEEUrgentQueue7=_Opmen99810bPortEEEUrgentQueue7_Object((1,3,6,1,4,1,5205,2,94,2,1,5,1,9),_Opmen99810bPortEEEUrgentQueue7_Type())
opmen99810bPortEEEUrgentQueue7.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortEEEUrgentQueue7.setStatus(_A)
class _Opmen99810bPortEEEUrgentQueue8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bPortEEEUrgentQueue8_Type.__name__=_C
_Opmen99810bPortEEEUrgentQueue8_Object=MibTableColumn
opmen99810bPortEEEUrgentQueue8=_Opmen99810bPortEEEUrgentQueue8_Object((1,3,6,1,4,1,5205,2,94,2,1,5,1,10),_Opmen99810bPortEEEUrgentQueue8_Type())
opmen99810bPortEEEUrgentQueue8.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortEEEUrgentQueue8.setStatus(_A)
_Opmen99810bVoiceVLAN_ObjectIdentity=ObjectIdentity
opmen99810bVoiceVLAN=_Opmen99810bVoiceVLAN_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,2))
_Opmen99810bVoiceVLANConf_ObjectIdentity=ObjectIdentity
opmen99810bVoiceVLANConf=_Opmen99810bVoiceVLANConf_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,2,1))
class _Opmen99810bVoiceVLANMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bVoiceVLANMode_Type.__name__=_C
_Opmen99810bVoiceVLANMode_Object=MibScalar
opmen99810bVoiceVLANMode=_Opmen99810bVoiceVLANMode_Object((1,3,6,1,4,1,5205,2,94,2,2,1,1),_Opmen99810bVoiceVLANMode_Type())
opmen99810bVoiceVLANMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVoiceVLANMode.setStatus(_A)
class _Opmen99810bVoiceVLANVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Opmen99810bVoiceVLANVLANId_Type.__name__=_C
_Opmen99810bVoiceVLANVLANId_Object=MibScalar
opmen99810bVoiceVLANVLANId=_Opmen99810bVoiceVLANVLANId_Object((1,3,6,1,4,1,5205,2,94,2,2,1,2),_Opmen99810bVoiceVLANVLANId_Type())
opmen99810bVoiceVLANVLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVoiceVLANVLANId.setStatus(_A)
class _Opmen99810bVoiceVLANAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_Opmen99810bVoiceVLANAgingTime_Type.__name__=_C
_Opmen99810bVoiceVLANAgingTime_Object=MibScalar
opmen99810bVoiceVLANAgingTime=_Opmen99810bVoiceVLANAgingTime_Object((1,3,6,1,4,1,5205,2,94,2,2,1,3),_Opmen99810bVoiceVLANAgingTime_Type())
opmen99810bVoiceVLANAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVoiceVLANAgingTime.setStatus(_A)
class _Opmen99810bVoiceVLANTrafficClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Opmen99810bVoiceVLANTrafficClass_Type.__name__=_C
_Opmen99810bVoiceVLANTrafficClass_Object=MibScalar
opmen99810bVoiceVLANTrafficClass=_Opmen99810bVoiceVLANTrafficClass_Object((1,3,6,1,4,1,5205,2,94,2,2,1,4),_Opmen99810bVoiceVLANTrafficClass_Type())
opmen99810bVoiceVLANTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVoiceVLANTrafficClass.setStatus(_A)
_Opmen99810bVoiceVLANPortTable_Object=MibTable
opmen99810bVoiceVLANPortTable=_Opmen99810bVoiceVLANPortTable_Object((1,3,6,1,4,1,5205,2,94,2,2,1,5))
if mibBuilder.loadTexts:opmen99810bVoiceVLANPortTable.setStatus(_A)
_Opmen99810bVoiceVLANPortEntry_Object=MibTableRow
opmen99810bVoiceVLANPortEntry=_Opmen99810bVoiceVLANPortEntry_Object((1,3,6,1,4,1,5205,2,94,2,2,1,5,1))
opmen99810bVoiceVLANPortEntry.setIndexNames((0,_G,_A9))
if mibBuilder.loadTexts:opmen99810bVoiceVLANPortEntry.setStatus(_A)
class _Opmen99810bVoiceVLANPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bVoiceVLANPort_Type.__name__=_C
_Opmen99810bVoiceVLANPort_Object=MibTableColumn
opmen99810bVoiceVLANPort=_Opmen99810bVoiceVLANPort_Object((1,3,6,1,4,1,5205,2,94,2,2,1,5,1,1),_Opmen99810bVoiceVLANPort_Type())
opmen99810bVoiceVLANPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bVoiceVLANPort.setStatus(_A)
class _Opmen99810bVoiceVLANPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('auto',1),('forced',2)))
_Opmen99810bVoiceVLANPortMode_Type.__name__=_C
_Opmen99810bVoiceVLANPortMode_Object=MibTableColumn
opmen99810bVoiceVLANPortMode=_Opmen99810bVoiceVLANPortMode_Object((1,3,6,1,4,1,5205,2,94,2,2,1,5,1,2),_Opmen99810bVoiceVLANPortMode_Type())
opmen99810bVoiceVLANPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVoiceVLANPortMode.setStatus(_A)
class _Opmen99810bVoiceVLANPortSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bVoiceVLANPortSecurity_Type.__name__=_C
_Opmen99810bVoiceVLANPortSecurity_Object=MibTableColumn
opmen99810bVoiceVLANPortSecurity=_Opmen99810bVoiceVLANPortSecurity_Object((1,3,6,1,4,1,5205,2,94,2,2,1,5,1,3),_Opmen99810bVoiceVLANPortSecurity_Type())
opmen99810bVoiceVLANPortSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVoiceVLANPortSecurity.setStatus(_A)
class _Opmen99810bVoiceVLANPortDiscoveryProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('oui',0),('lldp',1),('both',2)))
_Opmen99810bVoiceVLANPortDiscoveryProtocol_Type.__name__=_C
_Opmen99810bVoiceVLANPortDiscoveryProtocol_Object=MibTableColumn
opmen99810bVoiceVLANPortDiscoveryProtocol=_Opmen99810bVoiceVLANPortDiscoveryProtocol_Object((1,3,6,1,4,1,5205,2,94,2,2,1,5,1,4),_Opmen99810bVoiceVLANPortDiscoveryProtocol_Type())
opmen99810bVoiceVLANPortDiscoveryProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVoiceVLANPortDiscoveryProtocol.setStatus(_A)
_Opmen99810bVoiceVLANOUI_ObjectIdentity=ObjectIdentity
opmen99810bVoiceVLANOUI=_Opmen99810bVoiceVLANOUI_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,2,2))
class _Opmen99810bVoiceVLANOUICreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_W,1)))
_Opmen99810bVoiceVLANOUICreate_Type.__name__=_C
_Opmen99810bVoiceVLANOUICreate_Object=MibScalar
opmen99810bVoiceVLANOUICreate=_Opmen99810bVoiceVLANOUICreate_Object((1,3,6,1,4,1,5205,2,94,2,2,2,1),_Opmen99810bVoiceVLANOUICreate_Type())
opmen99810bVoiceVLANOUICreate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVoiceVLANOUICreate.setStatus(_A)
_Opmen99810bVoiceVLANOUITable_Object=MibTable
opmen99810bVoiceVLANOUITable=_Opmen99810bVoiceVLANOUITable_Object((1,3,6,1,4,1,5205,2,94,2,2,2,2))
if mibBuilder.loadTexts:opmen99810bVoiceVLANOUITable.setStatus(_A)
_Opmen99810bVoiceVLANOUIEntry_Object=MibTableRow
opmen99810bVoiceVLANOUIEntry=_Opmen99810bVoiceVLANOUIEntry_Object((1,3,6,1,4,1,5205,2,94,2,2,2,2,1))
opmen99810bVoiceVLANOUIEntry.setIndexNames((0,_G,_AA))
if mibBuilder.loadTexts:opmen99810bVoiceVLANOUIEntry.setStatus(_A)
class _Opmen99810bVoiceVLANOUIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Opmen99810bVoiceVLANOUIIndex_Type.__name__=_C
_Opmen99810bVoiceVLANOUIIndex_Object=MibTableColumn
opmen99810bVoiceVLANOUIIndex=_Opmen99810bVoiceVLANOUIIndex_Object((1,3,6,1,4,1,5205,2,94,2,2,2,2,1,1),_Opmen99810bVoiceVLANOUIIndex_Type())
opmen99810bVoiceVLANOUIIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bVoiceVLANOUIIndex.setStatus(_A)
class _Opmen99810bVoiceVLANTelephonyOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Opmen99810bVoiceVLANTelephonyOUI_Type.__name__=_n
_Opmen99810bVoiceVLANTelephonyOUI_Object=MibTableColumn
opmen99810bVoiceVLANTelephonyOUI=_Opmen99810bVoiceVLANTelephonyOUI_Object((1,3,6,1,4,1,5205,2,94,2,2,2,2,1,2),_Opmen99810bVoiceVLANTelephonyOUI_Type())
opmen99810bVoiceVLANTelephonyOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVoiceVLANTelephonyOUI.setStatus(_A)
class _Opmen99810bVoiceVLANDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Opmen99810bVoiceVLANDescription_Type.__name__=_S
_Opmen99810bVoiceVLANDescription_Object=MibTableColumn
opmen99810bVoiceVLANDescription=_Opmen99810bVoiceVLANDescription_Object((1,3,6,1,4,1,5205,2,94,2,2,2,2,1,3),_Opmen99810bVoiceVLANDescription_Type())
opmen99810bVoiceVLANDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVoiceVLANDescription.setStatus(_A)
class _Opmen99810bVoiceVLANOUIRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_U,1),(_X,2),(_Y,4),(_c,5)))
_Opmen99810bVoiceVLANOUIRowStatus_Type.__name__=_C
_Opmen99810bVoiceVLANOUIRowStatus_Object=MibTableColumn
opmen99810bVoiceVLANOUIRowStatus=_Opmen99810bVoiceVLANOUIRowStatus_Object((1,3,6,1,4,1,5205,2,94,2,2,2,2,1,4),_Opmen99810bVoiceVLANOUIRowStatus_Type())
opmen99810bVoiceVLANOUIRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVoiceVLANOUIRowStatus.setStatus(_A)
_Opmen99810bGARP_ObjectIdentity=ObjectIdentity
opmen99810bGARP=_Opmen99810bGARP_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,3))
_Opmen99810bGARPConfTable_Object=MibTable
opmen99810bGARPConfTable=_Opmen99810bGARPConfTable_Object((1,3,6,1,4,1,5205,2,94,2,3,1))
if mibBuilder.loadTexts:opmen99810bGARPConfTable.setStatus(_A)
_Opmen99810bGARPConfEntry_Object=MibTableRow
opmen99810bGARPConfEntry=_Opmen99810bGARPConfEntry_Object((1,3,6,1,4,1,5205,2,94,2,3,1,1))
opmen99810bGARPConfEntry.setIndexNames((0,_G,_AB))
if mibBuilder.loadTexts:opmen99810bGARPConfEntry.setStatus(_A)
class _Opmen99810bGARPConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bGARPConfPort_Type.__name__=_C
_Opmen99810bGARPConfPort_Object=MibTableColumn
opmen99810bGARPConfPort=_Opmen99810bGARPConfPort_Object((1,3,6,1,4,1,5205,2,94,2,3,1,1,1),_Opmen99810bGARPConfPort_Type())
opmen99810bGARPConfPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bGARPConfPort.setStatus(_A)
class _Opmen99810bGARPJoinTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,1000))
_Opmen99810bGARPJoinTimer_Type.__name__=_C
_Opmen99810bGARPJoinTimer_Object=MibTableColumn
opmen99810bGARPJoinTimer=_Opmen99810bGARPJoinTimer_Object((1,3,6,1,4,1,5205,2,94,2,3,1,1,2),_Opmen99810bGARPJoinTimer_Type())
opmen99810bGARPJoinTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bGARPJoinTimer.setStatus(_A)
class _Opmen99810bGARPLeaveTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,3000))
_Opmen99810bGARPLeaveTimer_Type.__name__=_C
_Opmen99810bGARPLeaveTimer_Object=MibTableColumn
opmen99810bGARPLeaveTimer=_Opmen99810bGARPLeaveTimer_Object((1,3,6,1,4,1,5205,2,94,2,3,1,1,3),_Opmen99810bGARPLeaveTimer_Type())
opmen99810bGARPLeaveTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bGARPLeaveTimer.setStatus(_A)
class _Opmen99810bGARPLeaveAllTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10000,50000))
_Opmen99810bGARPLeaveAllTimer_Type.__name__=_C
_Opmen99810bGARPLeaveAllTimer_Object=MibTableColumn
opmen99810bGARPLeaveAllTimer=_Opmen99810bGARPLeaveAllTimer_Object((1,3,6,1,4,1,5205,2,94,2,3,1,1,4),_Opmen99810bGARPLeaveAllTimer_Type())
opmen99810bGARPLeaveAllTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bGARPLeaveAllTimer.setStatus(_A)
class _Opmen99810bGARPApplicantion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('gvrp',1))
_Opmen99810bGARPApplicantion_Type.__name__=_C
_Opmen99810bGARPApplicantion_Object=MibTableColumn
opmen99810bGARPApplicantion=_Opmen99810bGARPApplicantion_Object((1,3,6,1,4,1,5205,2,94,2,3,1,1,5),_Opmen99810bGARPApplicantion_Type())
opmen99810bGARPApplicantion.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bGARPApplicantion.setStatus(_A)
class _Opmen99810bGARPAttributeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('vlan',1))
_Opmen99810bGARPAttributeType_Type.__name__=_C
_Opmen99810bGARPAttributeType_Object=MibTableColumn
opmen99810bGARPAttributeType=_Opmen99810bGARPAttributeType_Object((1,3,6,1,4,1,5205,2,94,2,3,1,1,6),_Opmen99810bGARPAttributeType_Type())
opmen99810bGARPAttributeType.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bGARPAttributeType.setStatus(_A)
class _Opmen99810bGARPApplicant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('participant',0),('nonParticipant',1)))
_Opmen99810bGARPApplicant_Type.__name__=_C
_Opmen99810bGARPApplicant_Object=MibTableColumn
opmen99810bGARPApplicant=_Opmen99810bGARPApplicant_Object((1,3,6,1,4,1,5205,2,94,2,3,1,1,7),_Opmen99810bGARPApplicant_Type())
opmen99810bGARPApplicant.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bGARPApplicant.setStatus(_A)
_Opmen99810bGARPStatisticsTable_Object=MibTable
opmen99810bGARPStatisticsTable=_Opmen99810bGARPStatisticsTable_Object((1,3,6,1,4,1,5205,2,94,2,3,2))
if mibBuilder.loadTexts:opmen99810bGARPStatisticsTable.setStatus(_A)
_Opmen99810bGARPStatisticsEntry_Object=MibTableRow
opmen99810bGARPStatisticsEntry=_Opmen99810bGARPStatisticsEntry_Object((1,3,6,1,4,1,5205,2,94,2,3,2,1))
opmen99810bGARPStatisticsEntry.setIndexNames((0,_G,_AC))
if mibBuilder.loadTexts:opmen99810bGARPStatisticsEntry.setStatus(_A)
class _Opmen99810bGARPStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bGARPStatisticsPort_Type.__name__=_C
_Opmen99810bGARPStatisticsPort_Object=MibTableColumn
opmen99810bGARPStatisticsPort=_Opmen99810bGARPStatisticsPort_Object((1,3,6,1,4,1,5205,2,94,2,3,2,1,1),_Opmen99810bGARPStatisticsPort_Type())
opmen99810bGARPStatisticsPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bGARPStatisticsPort.setStatus(_A)
_Opmen99810bGARPStatisticsPeerMAC_Type=DisplayString
_Opmen99810bGARPStatisticsPeerMAC_Object=MibTableColumn
opmen99810bGARPStatisticsPeerMAC=_Opmen99810bGARPStatisticsPeerMAC_Object((1,3,6,1,4,1,5205,2,94,2,3,2,1,2),_Opmen99810bGARPStatisticsPeerMAC_Type())
opmen99810bGARPStatisticsPeerMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bGARPStatisticsPeerMAC.setStatus(_A)
_Opmen99810bGARPStatisticsFailedCount_Type=Counter32
_Opmen99810bGARPStatisticsFailedCount_Object=MibTableColumn
opmen99810bGARPStatisticsFailedCount=_Opmen99810bGARPStatisticsFailedCount_Object((1,3,6,1,4,1,5205,2,94,2,3,2,1,3),_Opmen99810bGARPStatisticsFailedCount_Type())
opmen99810bGARPStatisticsFailedCount.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bGARPStatisticsFailedCount.setStatus(_A)
_Opmen99810bGVRP_ObjectIdentity=ObjectIdentity
opmen99810bGVRP=_Opmen99810bGVRP_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,4))
_Opmen99810bGVRPConf_ObjectIdentity=ObjectIdentity
opmen99810bGVRPConf=_Opmen99810bGVRPConf_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,4,1))
class _Opmen99810bGVRPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bGVRPMode_Type.__name__=_C
_Opmen99810bGVRPMode_Object=MibScalar
opmen99810bGVRPMode=_Opmen99810bGVRPMode_Object((1,3,6,1,4,1,5205,2,94,2,4,1,1),_Opmen99810bGVRPMode_Type())
opmen99810bGVRPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bGVRPMode.setStatus(_A)
_Opmen99810bGVRPConfTable_Object=MibTable
opmen99810bGVRPConfTable=_Opmen99810bGVRPConfTable_Object((1,3,6,1,4,1,5205,2,94,2,4,1,2))
if mibBuilder.loadTexts:opmen99810bGVRPConfTable.setStatus(_A)
_Opmen99810bGVRPConfEntry_Object=MibTableRow
opmen99810bGVRPConfEntry=_Opmen99810bGVRPConfEntry_Object((1,3,6,1,4,1,5205,2,94,2,4,1,2,1))
opmen99810bGVRPConfEntry.setIndexNames((0,_G,_AD))
if mibBuilder.loadTexts:opmen99810bGVRPConfEntry.setStatus(_A)
class _Opmen99810bGVRPConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bGVRPConfPort_Type.__name__=_C
_Opmen99810bGVRPConfPort_Object=MibTableColumn
opmen99810bGVRPConfPort=_Opmen99810bGVRPConfPort_Object((1,3,6,1,4,1,5205,2,94,2,4,1,2,1,1),_Opmen99810bGVRPConfPort_Type())
opmen99810bGVRPConfPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bGVRPConfPort.setStatus(_A)
class _Opmen99810bGVRPConfPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bGVRPConfPortMode_Type.__name__=_C
_Opmen99810bGVRPConfPortMode_Object=MibTableColumn
opmen99810bGVRPConfPortMode=_Opmen99810bGVRPConfPortMode_Object((1,3,6,1,4,1,5205,2,94,2,4,1,2,1,2),_Opmen99810bGVRPConfPortMode_Type())
opmen99810bGVRPConfPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bGVRPConfPortMode.setStatus(_A)
class _Opmen99810bGVRPConfPortRRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bGVRPConfPortRRole_Type.__name__=_C
_Opmen99810bGVRPConfPortRRole_Object=MibTableColumn
opmen99810bGVRPConfPortRRole=_Opmen99810bGVRPConfPortRRole_Object((1,3,6,1,4,1,5205,2,94,2,4,1,2,1,3),_Opmen99810bGVRPConfPortRRole_Type())
opmen99810bGVRPConfPortRRole.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bGVRPConfPortRRole.setStatus(_A)
_Opmen99810bGVRPStatisticsTable_Object=MibTable
opmen99810bGVRPStatisticsTable=_Opmen99810bGVRPStatisticsTable_Object((1,3,6,1,4,1,5205,2,94,2,4,2))
if mibBuilder.loadTexts:opmen99810bGVRPStatisticsTable.setStatus(_A)
_Opmen99810bGVRPStatisticsEntry_Object=MibTableRow
opmen99810bGVRPStatisticsEntry=_Opmen99810bGVRPStatisticsEntry_Object((1,3,6,1,4,1,5205,2,94,2,4,2,1))
opmen99810bGVRPStatisticsEntry.setIndexNames((0,_G,_AE))
if mibBuilder.loadTexts:opmen99810bGVRPStatisticsEntry.setStatus(_A)
class _Opmen99810bGVRPStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bGVRPStatisticsPort_Type.__name__=_C
_Opmen99810bGVRPStatisticsPort_Object=MibTableColumn
opmen99810bGVRPStatisticsPort=_Opmen99810bGVRPStatisticsPort_Object((1,3,6,1,4,1,5205,2,94,2,4,2,1,1),_Opmen99810bGVRPStatisticsPort_Type())
opmen99810bGVRPStatisticsPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bGVRPStatisticsPort.setStatus(_A)
_Opmen99810bGVRPStatisticsJoinTxCnt_Type=Counter32
_Opmen99810bGVRPStatisticsJoinTxCnt_Object=MibTableColumn
opmen99810bGVRPStatisticsJoinTxCnt=_Opmen99810bGVRPStatisticsJoinTxCnt_Object((1,3,6,1,4,1,5205,2,94,2,4,2,1,2),_Opmen99810bGVRPStatisticsJoinTxCnt_Type())
opmen99810bGVRPStatisticsJoinTxCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bGVRPStatisticsJoinTxCnt.setStatus(_A)
_Opmen99810bGVRPStatisticsLeaveTxCnt_Type=Counter32
_Opmen99810bGVRPStatisticsLeaveTxCnt_Object=MibTableColumn
opmen99810bGVRPStatisticsLeaveTxCnt=_Opmen99810bGVRPStatisticsLeaveTxCnt_Object((1,3,6,1,4,1,5205,2,94,2,4,2,1,3),_Opmen99810bGVRPStatisticsLeaveTxCnt_Type())
opmen99810bGVRPStatisticsLeaveTxCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bGVRPStatisticsLeaveTxCnt.setStatus(_A)
_Opmen99810bMirroring_ObjectIdentity=ObjectIdentity
opmen99810bMirroring=_Opmen99810bMirroring_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,6))
class _Opmen99810bPortToMirrorOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Opmen99810bPortToMirrorOn_Type.__name__=_C
_Opmen99810bPortToMirrorOn_Object=MibScalar
opmen99810bPortToMirrorOn=_Opmen99810bPortToMirrorOn_Object((1,3,6,1,4,1,5205,2,94,2,6,1),_Opmen99810bPortToMirrorOn_Type())
opmen99810bPortToMirrorOn.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortToMirrorOn.setStatus(_A)
_Opmen99810bMirrorTable_Object=MibTable
opmen99810bMirrorTable=_Opmen99810bMirrorTable_Object((1,3,6,1,4,1,5205,2,94,2,6,2))
if mibBuilder.loadTexts:opmen99810bMirrorTable.setStatus(_A)
_Opmen99810bMirrorEntry_Object=MibTableRow
opmen99810bMirrorEntry=_Opmen99810bMirrorEntry_Object((1,3,6,1,4,1,5205,2,94,2,6,2,1))
opmen99810bMirrorEntry.setIndexNames((0,_G,_AF))
if mibBuilder.loadTexts:opmen99810bMirrorEntry.setStatus(_A)
class _Opmen99810bMirrorPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bMirrorPort_Type.__name__=_C
_Opmen99810bMirrorPort_Object=MibTableColumn
opmen99810bMirrorPort=_Opmen99810bMirrorPort_Object((1,3,6,1,4,1,5205,2,94,2,6,2,1,1),_Opmen99810bMirrorPort_Type())
opmen99810bMirrorPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bMirrorPort.setStatus(_A)
class _Opmen99810bMirrorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),(_F,1),('rxOnly',2),('txOnly',3)))
_Opmen99810bMirrorMode_Type.__name__=_C
_Opmen99810bMirrorMode_Object=MibTableColumn
opmen99810bMirrorMode=_Opmen99810bMirrorMode_Object((1,3,6,1,4,1,5205,2,94,2,6,2,1,2),_Opmen99810bMirrorMode_Type())
opmen99810bMirrorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bMirrorMode.setStatus(_A)
_Opmen99810bTrapEventSeverity_ObjectIdentity=ObjectIdentity
opmen99810bTrapEventSeverity=_Opmen99810bTrapEventSeverity_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,7))
class _Opmen99810bTrapEventSeverityACL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityACL_Type.__name__=_C
_Opmen99810bTrapEventSeverityACL_Object=MibScalar
opmen99810bTrapEventSeverityACL=_Opmen99810bTrapEventSeverityACL_Object((1,3,6,1,4,1,5205,2,94,2,7,1),_Opmen99810bTrapEventSeverityACL_Type())
opmen99810bTrapEventSeverityACL.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityACL.setStatus(_A)
class _Opmen99810bTrapEventSeverityACLLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityACLLog_Type.__name__=_C
_Opmen99810bTrapEventSeverityACLLog_Object=MibScalar
opmen99810bTrapEventSeverityACLLog=_Opmen99810bTrapEventSeverityACLLog_Object((1,3,6,1,4,1,5205,2,94,2,7,2),_Opmen99810bTrapEventSeverityACLLog_Type())
opmen99810bTrapEventSeverityACLLog.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityACLLog.setStatus(_A)
class _Opmen99810bTrapEventSeverityAccessMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityAccessMgmt_Type.__name__=_C
_Opmen99810bTrapEventSeverityAccessMgmt_Object=MibScalar
opmen99810bTrapEventSeverityAccessMgmt=_Opmen99810bTrapEventSeverityAccessMgmt_Object((1,3,6,1,4,1,5205,2,94,2,7,3),_Opmen99810bTrapEventSeverityAccessMgmt_Type())
opmen99810bTrapEventSeverityAccessMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityAccessMgmt.setStatus(_A)
class _Opmen99810bTrapEventSeverityAuthFailed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityAuthFailed_Type.__name__=_C
_Opmen99810bTrapEventSeverityAuthFailed_Object=MibScalar
opmen99810bTrapEventSeverityAuthFailed=_Opmen99810bTrapEventSeverityAuthFailed_Object((1,3,6,1,4,1,5205,2,94,2,7,4),_Opmen99810bTrapEventSeverityAuthFailed_Type())
opmen99810bTrapEventSeverityAuthFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityAuthFailed.setStatus(_A)
class _Opmen99810bTrapEventSeverityColdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityColdStart_Type.__name__=_C
_Opmen99810bTrapEventSeverityColdStart_Object=MibScalar
opmen99810bTrapEventSeverityColdStart=_Opmen99810bTrapEventSeverityColdStart_Object((1,3,6,1,4,1,5205,2,94,2,7,5),_Opmen99810bTrapEventSeverityColdStart_Type())
opmen99810bTrapEventSeverityColdStart.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityColdStart.setStatus(_A)
class _Opmen99810bTrapEventSeverityConfigInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityConfigInfo_Type.__name__=_C
_Opmen99810bTrapEventSeverityConfigInfo_Object=MibScalar
opmen99810bTrapEventSeverityConfigInfo=_Opmen99810bTrapEventSeverityConfigInfo_Object((1,3,6,1,4,1,5205,2,94,2,7,6),_Opmen99810bTrapEventSeverityConfigInfo_Type())
opmen99810bTrapEventSeverityConfigInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityConfigInfo.setStatus(_A)
class _Opmen99810bTrapEventSeverityFirmwareUpgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityFirmwareUpgrade_Type.__name__=_C
_Opmen99810bTrapEventSeverityFirmwareUpgrade_Object=MibScalar
opmen99810bTrapEventSeverityFirmwareUpgrade=_Opmen99810bTrapEventSeverityFirmwareUpgrade_Object((1,3,6,1,4,1,5205,2,94,2,7,7),_Opmen99810bTrapEventSeverityFirmwareUpgrade_Type())
opmen99810bTrapEventSeverityFirmwareUpgrade.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityFirmwareUpgrade.setStatus(_A)
class _Opmen99810bTrapEventSeverityImportExport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityImportExport_Type.__name__=_C
_Opmen99810bTrapEventSeverityImportExport_Object=MibScalar
opmen99810bTrapEventSeverityImportExport=_Opmen99810bTrapEventSeverityImportExport_Object((1,3,6,1,4,1,5205,2,94,2,7,8),_Opmen99810bTrapEventSeverityImportExport_Type())
opmen99810bTrapEventSeverityImportExport.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityImportExport.setStatus(_A)
class _Opmen99810bTrapEventSeverityLACP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityLACP_Type.__name__=_C
_Opmen99810bTrapEventSeverityLACP_Object=MibScalar
opmen99810bTrapEventSeverityLACP=_Opmen99810bTrapEventSeverityLACP_Object((1,3,6,1,4,1,5205,2,94,2,7,9),_Opmen99810bTrapEventSeverityLACP_Type())
opmen99810bTrapEventSeverityLACP.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityLACP.setStatus(_A)
class _Opmen99810bTrapEventSeverityLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityLinkStatus_Type.__name__=_C
_Opmen99810bTrapEventSeverityLinkStatus_Object=MibScalar
opmen99810bTrapEventSeverityLinkStatus=_Opmen99810bTrapEventSeverityLinkStatus_Object((1,3,6,1,4,1,5205,2,94,2,7,10),_Opmen99810bTrapEventSeverityLinkStatus_Type())
opmen99810bTrapEventSeverityLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityLinkStatus.setStatus(_A)
class _Opmen99810bTrapEventSeverityLogin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityLogin_Type.__name__=_C
_Opmen99810bTrapEventSeverityLogin_Object=MibScalar
opmen99810bTrapEventSeverityLogin=_Opmen99810bTrapEventSeverityLogin_Object((1,3,6,1,4,1,5205,2,94,2,7,11),_Opmen99810bTrapEventSeverityLogin_Type())
opmen99810bTrapEventSeverityLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityLogin.setStatus(_A)
class _Opmen99810bTrapEventSeverityLogout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityLogout_Type.__name__=_C
_Opmen99810bTrapEventSeverityLogout_Object=MibScalar
opmen99810bTrapEventSeverityLogout=_Opmen99810bTrapEventSeverityLogout_Object((1,3,6,1,4,1,5205,2,94,2,7,12),_Opmen99810bTrapEventSeverityLogout_Type())
opmen99810bTrapEventSeverityLogout.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityLogout.setStatus(_A)
class _Opmen99810bTrapEventSeverityLoopProtect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityLoopProtect_Type.__name__=_C
_Opmen99810bTrapEventSeverityLoopProtect_Object=MibScalar
opmen99810bTrapEventSeverityLoopProtect=_Opmen99810bTrapEventSeverityLoopProtect_Object((1,3,6,1,4,1,5205,2,94,2,7,13),_Opmen99810bTrapEventSeverityLoopProtect_Type())
opmen99810bTrapEventSeverityLoopProtect.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityLoopProtect.setStatus(_A)
class _Opmen99810bTrapEventSeverityMgmtIPChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityMgmtIPChange_Type.__name__=_C
_Opmen99810bTrapEventSeverityMgmtIPChange_Object=MibScalar
opmen99810bTrapEventSeverityMgmtIPChange=_Opmen99810bTrapEventSeverityMgmtIPChange_Object((1,3,6,1,4,1,5205,2,94,2,7,14),_Opmen99810bTrapEventSeverityMgmtIPChange_Type())
opmen99810bTrapEventSeverityMgmtIPChange.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityMgmtIPChange.setStatus(_A)
class _Opmen99810bTrapEventSeverityModuleChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityModuleChange_Type.__name__=_C
_Opmen99810bTrapEventSeverityModuleChange_Object=MibScalar
opmen99810bTrapEventSeverityModuleChange=_Opmen99810bTrapEventSeverityModuleChange_Object((1,3,6,1,4,1,5205,2,94,2,7,15),_Opmen99810bTrapEventSeverityModuleChange_Type())
opmen99810bTrapEventSeverityModuleChange.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityModuleChange.setStatus(_A)
class _Opmen99810bTrapEventSeverityNAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityNAS_Type.__name__=_C
_Opmen99810bTrapEventSeverityNAS_Object=MibScalar
opmen99810bTrapEventSeverityNAS=_Opmen99810bTrapEventSeverityNAS_Object((1,3,6,1,4,1,5205,2,94,2,7,16),_Opmen99810bTrapEventSeverityNAS_Type())
opmen99810bTrapEventSeverityNAS.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityNAS.setStatus(_A)
class _Opmen99810bTrapEventSeverityPasswordChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityPasswordChange_Type.__name__=_C
_Opmen99810bTrapEventSeverityPasswordChange_Object=MibScalar
opmen99810bTrapEventSeverityPasswordChange=_Opmen99810bTrapEventSeverityPasswordChange_Object((1,3,6,1,4,1,5205,2,94,2,7,17),_Opmen99810bTrapEventSeverityPasswordChange_Type())
opmen99810bTrapEventSeverityPasswordChange.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityPasswordChange.setStatus(_A)
class _Opmen99810bTrapEventSeverityPortSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityPortSecurity_Type.__name__=_C
_Opmen99810bTrapEventSeverityPortSecurity_Object=MibScalar
opmen99810bTrapEventSeverityPortSecurity=_Opmen99810bTrapEventSeverityPortSecurity_Object((1,3,6,1,4,1,5205,2,94,2,7,18),_Opmen99810bTrapEventSeverityPortSecurity_Type())
opmen99810bTrapEventSeverityPortSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityPortSecurity.setStatus(_A)
class _Opmen99810bTrapEventSeverityVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityVLAN_Type.__name__=_C
_Opmen99810bTrapEventSeverityVLAN_Object=MibScalar
opmen99810bTrapEventSeverityVLAN=_Opmen99810bTrapEventSeverityVLAN_Object((1,3,6,1,4,1,5205,2,94,2,7,20),_Opmen99810bTrapEventSeverityVLAN_Type())
opmen99810bTrapEventSeverityVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityVLAN.setStatus(_A)
class _Opmen99810bTrapEventSeverityWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bTrapEventSeverityWarmStart_Type.__name__=_C
_Opmen99810bTrapEventSeverityWarmStart_Object=MibScalar
opmen99810bTrapEventSeverityWarmStart=_Opmen99810bTrapEventSeverityWarmStart_Object((1,3,6,1,4,1,5205,2,94,2,7,21),_Opmen99810bTrapEventSeverityWarmStart_Type())
opmen99810bTrapEventSeverityWarmStart.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTrapEventSeverityWarmStart.setStatus(_A)
_Opmen99810bSMTP_ObjectIdentity=ObjectIdentity
opmen99810bSMTP=_Opmen99810bSMTP_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,8))
_Opmen99810bSMTPMailServer_Type=DisplayString
_Opmen99810bSMTPMailServer_Object=MibScalar
opmen99810bSMTPMailServer=_Opmen99810bSMTPMailServer_Object((1,3,6,1,4,1,5205,2,94,2,8,1),_Opmen99810bSMTPMailServer_Type())
opmen99810bSMTPMailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSMTPMailServer.setStatus(_A)
_Opmen99810bSMTPUserName_Type=DisplayString
_Opmen99810bSMTPUserName_Object=MibScalar
opmen99810bSMTPUserName=_Opmen99810bSMTPUserName_Object((1,3,6,1,4,1,5205,2,94,2,8,2),_Opmen99810bSMTPUserName_Type())
opmen99810bSMTPUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSMTPUserName.setStatus(_A)
_Opmen99810bSMTPPassword_Type=DisplayString
_Opmen99810bSMTPPassword_Object=MibScalar
opmen99810bSMTPPassword=_Opmen99810bSMTPPassword_Object((1,3,6,1,4,1,5205,2,94,2,8,3),_Opmen99810bSMTPPassword_Type())
opmen99810bSMTPPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSMTPPassword.setStatus(_A)
class _Opmen99810bSMTPServeriryLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_Opmen99810bSMTPServeriryLevel_Type.__name__=_C
_Opmen99810bSMTPServeriryLevel_Object=MibScalar
opmen99810bSMTPServeriryLevel=_Opmen99810bSMTPServeriryLevel_Object((1,3,6,1,4,1,5205,2,94,2,8,4),_Opmen99810bSMTPServeriryLevel_Type())
opmen99810bSMTPServeriryLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSMTPServeriryLevel.setStatus(_A)
_Opmen99810bSMTPSender_Type=DisplayString
_Opmen99810bSMTPSender_Object=MibScalar
opmen99810bSMTPSender=_Opmen99810bSMTPSender_Object((1,3,6,1,4,1,5205,2,94,2,8,5),_Opmen99810bSMTPSender_Type())
opmen99810bSMTPSender.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSMTPSender.setStatus(_A)
_Opmen99810bSMTPReturnPath_Type=DisplayString
_Opmen99810bSMTPReturnPath_Object=MibScalar
opmen99810bSMTPReturnPath=_Opmen99810bSMTPReturnPath_Object((1,3,6,1,4,1,5205,2,94,2,8,6),_Opmen99810bSMTPReturnPath_Type())
opmen99810bSMTPReturnPath.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSMTPReturnPath.setStatus(_A)
class _Opmen99810bSMTPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Opmen99810bSMTPPort_Type.__name__=_C
_Opmen99810bSMTPPort_Object=MibScalar
opmen99810bSMTPPort=_Opmen99810bSMTPPort_Object((1,3,6,1,4,1,5205,2,94,2,8,7),_Opmen99810bSMTPPort_Type())
opmen99810bSMTPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSMTPPort.setStatus(_A)
_Opmen99810bSMTPEmailAddress1_Type=DisplayString
_Opmen99810bSMTPEmailAddress1_Object=MibScalar
opmen99810bSMTPEmailAddress1=_Opmen99810bSMTPEmailAddress1_Object((1,3,6,1,4,1,5205,2,94,2,8,8),_Opmen99810bSMTPEmailAddress1_Type())
opmen99810bSMTPEmailAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSMTPEmailAddress1.setStatus(_A)
_Opmen99810bSMTPEmailAddress2_Type=DisplayString
_Opmen99810bSMTPEmailAddress2_Object=MibScalar
opmen99810bSMTPEmailAddress2=_Opmen99810bSMTPEmailAddress2_Object((1,3,6,1,4,1,5205,2,94,2,8,9),_Opmen99810bSMTPEmailAddress2_Type())
opmen99810bSMTPEmailAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSMTPEmailAddress2.setStatus(_A)
_Opmen99810bSMTPEmailAddress3_Type=DisplayString
_Opmen99810bSMTPEmailAddress3_Object=MibScalar
opmen99810bSMTPEmailAddress3=_Opmen99810bSMTPEmailAddress3_Object((1,3,6,1,4,1,5205,2,94,2,8,10),_Opmen99810bSMTPEmailAddress3_Type())
opmen99810bSMTPEmailAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSMTPEmailAddress3.setStatus(_A)
_Opmen99810bSMTPEmailAddress4_Type=DisplayString
_Opmen99810bSMTPEmailAddress4_Object=MibScalar
opmen99810bSMTPEmailAddress4=_Opmen99810bSMTPEmailAddress4_Object((1,3,6,1,4,1,5205,2,94,2,8,11),_Opmen99810bSMTPEmailAddress4_Type())
opmen99810bSMTPEmailAddress4.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSMTPEmailAddress4.setStatus(_A)
_Opmen99810bSMTPEmailAddress5_Type=DisplayString
_Opmen99810bSMTPEmailAddress5_Object=MibScalar
opmen99810bSMTPEmailAddress5=_Opmen99810bSMTPEmailAddress5_Object((1,3,6,1,4,1,5205,2,94,2,8,12),_Opmen99810bSMTPEmailAddress5_Type())
opmen99810bSMTPEmailAddress5.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSMTPEmailAddress5.setStatus(_A)
_Opmen99810bSMTPEmailAddress6_Type=DisplayString
_Opmen99810bSMTPEmailAddress6_Object=MibScalar
opmen99810bSMTPEmailAddress6=_Opmen99810bSMTPEmailAddress6_Object((1,3,6,1,4,1,5205,2,94,2,8,13),_Opmen99810bSMTPEmailAddress6_Type())
opmen99810bSMTPEmailAddress6.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSMTPEmailAddress6.setStatus(_A)
_Opmen99810bACL_ObjectIdentity=ObjectIdentity
opmen99810bACL=_Opmen99810bACL_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,9))
_Opmen99810bACLPortsConfTable_Object=MibTable
opmen99810bACLPortsConfTable=_Opmen99810bACLPortsConfTable_Object((1,3,6,1,4,1,5205,2,94,2,9,1))
if mibBuilder.loadTexts:opmen99810bACLPortsConfTable.setStatus(_A)
_Opmen99810bACLPortsConfEntry_Object=MibTableRow
opmen99810bACLPortsConfEntry=_Opmen99810bACLPortsConfEntry_Object((1,3,6,1,4,1,5205,2,94,2,9,1,1))
opmen99810bACLPortsConfEntry.setIndexNames((0,_G,_AG))
if mibBuilder.loadTexts:opmen99810bACLPortsConfEntry.setStatus(_A)
class _Opmen99810bACLPortsConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bACLPortsConfPort_Type.__name__=_C
_Opmen99810bACLPortsConfPort_Object=MibTableColumn
opmen99810bACLPortsConfPort=_Opmen99810bACLPortsConfPort_Object((1,3,6,1,4,1,5205,2,94,2,9,1,1,1),_Opmen99810bACLPortsConfPort_Type())
opmen99810bACLPortsConfPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bACLPortsConfPort.setStatus(_A)
class _Opmen99810bACLPortsConfPolicyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Opmen99810bACLPortsConfPolicyID_Type.__name__=_C
_Opmen99810bACLPortsConfPolicyID_Object=MibTableColumn
opmen99810bACLPortsConfPolicyID=_Opmen99810bACLPortsConfPolicyID_Object((1,3,6,1,4,1,5205,2,94,2,9,1,1,2),_Opmen99810bACLPortsConfPolicyID_Type())
opmen99810bACLPortsConfPolicyID.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLPortsConfPolicyID.setStatus(_A)
class _Opmen99810bACLPortsConfAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('deny',0),('permit',1)))
_Opmen99810bACLPortsConfAction_Type.__name__=_C
_Opmen99810bACLPortsConfAction_Object=MibTableColumn
opmen99810bACLPortsConfAction=_Opmen99810bACLPortsConfAction_Object((1,3,6,1,4,1,5205,2,94,2,9,1,1,3),_Opmen99810bACLPortsConfAction_Type())
opmen99810bACLPortsConfAction.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLPortsConfAction.setStatus(_A)
class _Opmen99810bACLPortsConfRateLimiterID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_Opmen99810bACLPortsConfRateLimiterID_Type.__name__=_C
_Opmen99810bACLPortsConfRateLimiterID_Object=MibTableColumn
opmen99810bACLPortsConfRateLimiterID=_Opmen99810bACLPortsConfRateLimiterID_Object((1,3,6,1,4,1,5205,2,94,2,9,1,1,4),_Opmen99810bACLPortsConfRateLimiterID_Type())
opmen99810bACLPortsConfRateLimiterID.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLPortsConfRateLimiterID.setStatus(_A)
class _Opmen99810bACLPortsConfPortRedirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_Opmen99810bACLPortsConfPortRedirect_Type.__name__=_C
_Opmen99810bACLPortsConfPortRedirect_Object=MibTableColumn
opmen99810bACLPortsConfPortRedirect=_Opmen99810bACLPortsConfPortRedirect_Object((1,3,6,1,4,1,5205,2,94,2,9,1,1,5),_Opmen99810bACLPortsConfPortRedirect_Type())
opmen99810bACLPortsConfPortRedirect.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLPortsConfPortRedirect.setStatus(_A)
class _Opmen99810bACLPortsConfMirror_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bACLPortsConfMirror_Type.__name__=_C
_Opmen99810bACLPortsConfMirror_Object=MibTableColumn
opmen99810bACLPortsConfMirror=_Opmen99810bACLPortsConfMirror_Object((1,3,6,1,4,1,5205,2,94,2,9,1,1,6),_Opmen99810bACLPortsConfMirror_Type())
opmen99810bACLPortsConfMirror.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLPortsConfMirror.setStatus(_A)
class _Opmen99810bACLPortsConfLogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bACLPortsConfLogging_Type.__name__=_C
_Opmen99810bACLPortsConfLogging_Object=MibTableColumn
opmen99810bACLPortsConfLogging=_Opmen99810bACLPortsConfLogging_Object((1,3,6,1,4,1,5205,2,94,2,9,1,1,7),_Opmen99810bACLPortsConfLogging_Type())
opmen99810bACLPortsConfLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLPortsConfLogging.setStatus(_A)
class _Opmen99810bACLPortsConfShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bACLPortsConfShutdown_Type.__name__=_C
_Opmen99810bACLPortsConfShutdown_Object=MibTableColumn
opmen99810bACLPortsConfShutdown=_Opmen99810bACLPortsConfShutdown_Object((1,3,6,1,4,1,5205,2,94,2,9,1,1,8),_Opmen99810bACLPortsConfShutdown_Type())
opmen99810bACLPortsConfShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLPortsConfShutdown.setStatus(_A)
class _Opmen99810bACLPortsConfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bACLPortsConfState_Type.__name__=_C
_Opmen99810bACLPortsConfState_Object=MibTableColumn
opmen99810bACLPortsConfState=_Opmen99810bACLPortsConfState_Object((1,3,6,1,4,1,5205,2,94,2,9,1,1,9),_Opmen99810bACLPortsConfState_Type())
opmen99810bACLPortsConfState.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLPortsConfState.setStatus(_A)
_Opmen99810bACLPortsConfCounter_Type=Counter32
_Opmen99810bACLPortsConfCounter_Object=MibTableColumn
opmen99810bACLPortsConfCounter=_Opmen99810bACLPortsConfCounter_Object((1,3,6,1,4,1,5205,2,94,2,9,1,1,10),_Opmen99810bACLPortsConfCounter_Type())
opmen99810bACLPortsConfCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bACLPortsConfCounter.setStatus(_A)
_Opmen99810bACLRateLimiterTable_Object=MibTable
opmen99810bACLRateLimiterTable=_Opmen99810bACLRateLimiterTable_Object((1,3,6,1,4,1,5205,2,94,2,9,2))
if mibBuilder.loadTexts:opmen99810bACLRateLimiterTable.setStatus(_A)
_Opmen99810bACLRateLimiterEntry_Object=MibTableRow
opmen99810bACLRateLimiterEntry=_Opmen99810bACLRateLimiterEntry_Object((1,3,6,1,4,1,5205,2,94,2,9,2,1))
opmen99810bACLRateLimiterEntry.setIndexNames((0,_G,_AH))
if mibBuilder.loadTexts:opmen99810bACLRateLimiterEntry.setStatus(_A)
class _Opmen99810bACLRateLimiterID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Opmen99810bACLRateLimiterID_Type.__name__=_C
_Opmen99810bACLRateLimiterID_Object=MibTableColumn
opmen99810bACLRateLimiterID=_Opmen99810bACLRateLimiterID_Object((1,3,6,1,4,1,5205,2,94,2,9,2,1,1),_Opmen99810bACLRateLimiterID_Type())
opmen99810bACLRateLimiterID.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bACLRateLimiterID.setStatus(_A)
class _Opmen99810bACLRateLimiterUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('pps',0),('kbps',1)))
_Opmen99810bACLRateLimiterUnit_Type.__name__=_C
_Opmen99810bACLRateLimiterUnit_Object=MibTableColumn
opmen99810bACLRateLimiterUnit=_Opmen99810bACLRateLimiterUnit_Object((1,3,6,1,4,1,5205,2,94,2,9,2,1,2),_Opmen99810bACLRateLimiterUnit_Type())
opmen99810bACLRateLimiterUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLRateLimiterUnit.setStatus(_A)
class _Opmen99810bACLRateLimiterRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3276700))
_Opmen99810bACLRateLimiterRate_Type.__name__=_C
_Opmen99810bACLRateLimiterRate_Object=MibTableColumn
opmen99810bACLRateLimiterRate=_Opmen99810bACLRateLimiterRate_Object((1,3,6,1,4,1,5205,2,94,2,9,2,1,3),_Opmen99810bACLRateLimiterRate_Type())
opmen99810bACLRateLimiterRate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLRateLimiterRate.setStatus(_A)
_Opmen99810bACLACE_ObjectIdentity=ObjectIdentity
opmen99810bACLACE=_Opmen99810bACLACE_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,9,3))
class _Opmen99810bACLACECreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_W,1)))
_Opmen99810bACLACECreate_Type.__name__=_C
_Opmen99810bACLACECreate_Object=MibScalar
opmen99810bACLACECreate=_Opmen99810bACLACECreate_Object((1,3,6,1,4,1,5205,2,94,2,9,3,1),_Opmen99810bACLACECreate_Type())
opmen99810bACLACECreate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACECreate.setStatus(_A)
_Opmen99810bACLACETable_Object=MibTable
opmen99810bACLACETable=_Opmen99810bACLACETable_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2))
if mibBuilder.loadTexts:opmen99810bACLACETable.setStatus(_A)
_Opmen99810bACLACEEntry_Object=MibTableRow
opmen99810bACLACEEntry=_Opmen99810bACLACEEntry_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1))
opmen99810bACLACEEntry.setIndexNames((0,_G,_AI))
if mibBuilder.loadTexts:opmen99810bACLACEEntry.setStatus(_A)
class _Opmen99810bACLACEIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Opmen99810bACLACEIndex_Type.__name__=_C
_Opmen99810bACLACEIndex_Object=MibTableColumn
opmen99810bACLACEIndex=_Opmen99810bACLACEIndex_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,1),_Opmen99810bACLACEIndex_Type())
opmen99810bACLACEIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bACLACEIndex.setStatus(_A)
class _Opmen99810bACLACEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Opmen99810bACLACEID_Type.__name__=_C
_Opmen99810bACLACEID_Object=MibTableColumn
opmen99810bACLACEID=_Opmen99810bACLACEID_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,2),_Opmen99810bACLACEID_Type())
opmen99810bACLACEID.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEID.setStatus(_A)
class _Opmen99810bACLACENextID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Opmen99810bACLACENextID_Type.__name__=_C
_Opmen99810bACLACENextID_Object=MibTableColumn
opmen99810bACLACENextID=_Opmen99810bACLACENextID_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,3),_Opmen99810bACLACENextID_Type())
opmen99810bACLACENextID.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACENextID.setStatus(_A)
_Opmen99810bACLACEIngressPort_Type=DisplayString
_Opmen99810bACLACEIngressPort_Object=MibTableColumn
opmen99810bACLACEIngressPort=_Opmen99810bACLACEIngressPort_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,4),_Opmen99810bACLACEIngressPort_Type())
opmen99810bACLACEIngressPort.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEIngressPort.setStatus(_A)
class _Opmen99810bACLACEPortPolicyNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Opmen99810bACLACEPortPolicyNumber_Type.__name__=_C
_Opmen99810bACLACEPortPolicyNumber_Object=MibTableColumn
opmen99810bACLACEPortPolicyNumber=_Opmen99810bACLACEPortPolicyNumber_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,5),_Opmen99810bACLACEPortPolicyNumber_Type())
opmen99810bACLACEPortPolicyNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEPortPolicyNumber.setStatus(_A)
class _Opmen99810bACLACEPortPolicyBitmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Opmen99810bACLACEPortPolicyBitmask_Type.__name__=_C
_Opmen99810bACLACEPortPolicyBitmask_Object=MibTableColumn
opmen99810bACLACEPortPolicyBitmask=_Opmen99810bACLACEPortPolicyBitmask_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,6),_Opmen99810bACLACEPortPolicyBitmask_Type())
opmen99810bACLACEPortPolicyBitmask.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEPortPolicyBitmask.setStatus(_A)
class _Opmen99810bACLACEFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_R,0),('arp',1),('etype',2),('icmp',3),(_d,4),('tcp',5),('udp',6)))
_Opmen99810bACLACEFrameType_Type.__name__=_C
_Opmen99810bACLACEFrameType_Object=MibTableColumn
opmen99810bACLACEFrameType=_Opmen99810bACLACEFrameType_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,7),_Opmen99810bACLACEFrameType_Type())
opmen99810bACLACEFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEFrameType.setStatus(_A)
class _Opmen99810bACLACEAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('deny',0),('permit',1)))
_Opmen99810bACLACEAction_Type.__name__=_C
_Opmen99810bACLACEAction_Object=MibTableColumn
opmen99810bACLACEAction=_Opmen99810bACLACEAction_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,8),_Opmen99810bACLACEAction_Type())
opmen99810bACLACEAction.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEAction.setStatus(_A)
_Opmen99810bACLACEDenyPortRedirect_Type=DisplayString
_Opmen99810bACLACEDenyPortRedirect_Object=MibTableColumn
opmen99810bACLACEDenyPortRedirect=_Opmen99810bACLACEDenyPortRedirect_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,9),_Opmen99810bACLACEDenyPortRedirect_Type())
opmen99810bACLACEDenyPortRedirect.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEDenyPortRedirect.setStatus(_A)
class _Opmen99810bACLACELogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bACLACELogging_Type.__name__=_C
_Opmen99810bACLACELogging_Object=MibTableColumn
opmen99810bACLACELogging=_Opmen99810bACLACELogging_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,10),_Opmen99810bACLACELogging_Type())
opmen99810bACLACELogging.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACELogging.setStatus(_A)
class _Opmen99810bACLACEMirror_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bACLACEMirror_Type.__name__=_C
_Opmen99810bACLACEMirror_Object=MibTableColumn
opmen99810bACLACEMirror=_Opmen99810bACLACEMirror_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,11),_Opmen99810bACLACEMirror_Type())
opmen99810bACLACEMirror.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEMirror.setStatus(_A)
class _Opmen99810bACLACERateLimiter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_Opmen99810bACLACERateLimiter_Type.__name__=_C
_Opmen99810bACLACERateLimiter_Object=MibTableColumn
opmen99810bACLACERateLimiter=_Opmen99810bACLACERateLimiter_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,12),_Opmen99810bACLACERateLimiter_Type())
opmen99810bACLACERateLimiter.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACERateLimiter.setStatus(_A)
class _Opmen99810bACLACEShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bACLACEShutdown_Type.__name__=_C
_Opmen99810bACLACEShutdown_Object=MibTableColumn
opmen99810bACLACEShutdown=_Opmen99810bACLACEShutdown_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,13),_Opmen99810bACLACEShutdown_Type())
opmen99810bACLACEShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEShutdown.setStatus(_A)
class _Opmen99810bACLACEVLAN8021QTagged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_F,1),(_R,2)))
_Opmen99810bACLACEVLAN8021QTagged_Type.__name__=_C
_Opmen99810bACLACEVLAN8021QTagged_Object=MibTableColumn
opmen99810bACLACEVLAN8021QTagged=_Opmen99810bACLACEVLAN8021QTagged_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,14),_Opmen99810bACLACEVLAN8021QTagged_Type())
opmen99810bACLACEVLAN8021QTagged.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEVLAN8021QTagged.setStatus(_A)
class _Opmen99810bACLACEVLANTagPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_Opmen99810bACLACEVLANTagPriority_Type.__name__=_C
_Opmen99810bACLACEVLANTagPriority_Object=MibTableColumn
opmen99810bACLACEVLANTagPriority=_Opmen99810bACLACEVLANTagPriority_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,15),_Opmen99810bACLACEVLANTagPriority_Type())
opmen99810bACLACEVLANTagPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEVLANTagPriority.setStatus(_A)
class _Opmen99810bACLACEVLANVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Opmen99810bACLACEVLANVID_Type.__name__=_C
_Opmen99810bACLACEVLANVID_Object=MibTableColumn
opmen99810bACLACEVLANVID=_Opmen99810bACLACEVLANVID_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,16),_Opmen99810bACLACEVLANVID_Type())
opmen99810bACLACEVLANVID.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEVLANVID.setStatus(_A)
class _Opmen99810bACLACEEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Opmen99810bACLACEEtherType_Type.__name__=_C
_Opmen99810bACLACEEtherType_Object=MibTableColumn
opmen99810bACLACEEtherType=_Opmen99810bACLACEEtherType_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,17),_Opmen99810bACLACEEtherType_Type())
opmen99810bACLACEEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEEtherType.setStatus(_A)
_Opmen99810bACLACESMAC_Type=DisplayString
_Opmen99810bACLACESMAC_Object=MibTableColumn
opmen99810bACLACESMAC=_Opmen99810bACLACESMAC_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,18),_Opmen99810bACLACESMAC_Type())
opmen99810bACLACESMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACESMAC.setStatus(_A)
class _Opmen99810bACLACEDMACType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_R,0),('broadcast',1),('unicast',2),('multicast',3),('macAddress',4)))
_Opmen99810bACLACEDMACType_Type.__name__=_C
_Opmen99810bACLACEDMACType_Object=MibTableColumn
opmen99810bACLACEDMACType=_Opmen99810bACLACEDMACType_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,19),_Opmen99810bACLACEDMACType_Type())
opmen99810bACLACEDMACType.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEDMACType.setStatus(_A)
_Opmen99810bACLACEDMAC_Type=DisplayString
_Opmen99810bACLACEDMAC_Object=MibTableColumn
opmen99810bACLACEDMAC=_Opmen99810bACLACEDMAC_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,20),_Opmen99810bACLACEDMAC_Type())
opmen99810bACLACEDMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEDMAC.setStatus(_A)
class _Opmen99810bACLACEArpOpcode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_R,0),('arp',1),('rarp',2),('other',3),(_T,4)))
_Opmen99810bACLACEArpOpcode_Type.__name__=_C
_Opmen99810bACLACEArpOpcode_Object=MibTableColumn
opmen99810bACLACEArpOpcode=_Opmen99810bACLACEArpOpcode_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,21),_Opmen99810bACLACEArpOpcode_Type())
opmen99810bACLACEArpOpcode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEArpOpcode.setStatus(_A)
class _Opmen99810bACLACEArpFlagsRequestReply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('reply',0),('request',1),(_R,2),(_T,3)))
_Opmen99810bACLACEArpFlagsRequestReply_Type.__name__=_C
_Opmen99810bACLACEArpFlagsRequestReply_Object=MibTableColumn
opmen99810bACLACEArpFlagsRequestReply=_Opmen99810bACLACEArpFlagsRequestReply_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,22),_Opmen99810bACLACEArpFlagsRequestReply_Type())
opmen99810bACLACEArpFlagsRequestReply.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEArpFlagsRequestReply.setStatus(_A)
class _Opmen99810bACLACEArpFlagsArpSmac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notEqualSMAC',0),('equalSMAC',1),(_R,2),(_T,3)))
_Opmen99810bACLACEArpFlagsArpSmac_Type.__name__=_C
_Opmen99810bACLACEArpFlagsArpSmac_Object=MibTableColumn
opmen99810bACLACEArpFlagsArpSmac=_Opmen99810bACLACEArpFlagsArpSmac_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,23),_Opmen99810bACLACEArpFlagsArpSmac_Type())
opmen99810bACLACEArpFlagsArpSmac.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEArpFlagsArpSmac.setStatus(_A)
class _Opmen99810bACLACEArpFlagsRarpDmac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notEqualDMAC',0),('equalDMAC',1),(_R,2),(_T,3)))
_Opmen99810bACLACEArpFlagsRarpDmac_Type.__name__=_C
_Opmen99810bACLACEArpFlagsRarpDmac_Object=MibTableColumn
opmen99810bACLACEArpFlagsRarpDmac=_Opmen99810bACLACEArpFlagsRarpDmac_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,24),_Opmen99810bACLACEArpFlagsRarpDmac_Type())
opmen99810bACLACEArpFlagsRarpDmac.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEArpFlagsRarpDmac.setStatus(_A)
class _Opmen99810bACLACEArpFlagsLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Opmen99810bACLACEArpFlagsLength_Type.__name__=_C
_Opmen99810bACLACEArpFlagsLength_Object=MibTableColumn
opmen99810bACLACEArpFlagsLength=_Opmen99810bACLACEArpFlagsLength_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,25),_Opmen99810bACLACEArpFlagsLength_Type())
opmen99810bACLACEArpFlagsLength.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEArpFlagsLength.setStatus(_A)
class _Opmen99810bACLACEArpFlagsIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Opmen99810bACLACEArpFlagsIp_Type.__name__=_C
_Opmen99810bACLACEArpFlagsIp_Object=MibTableColumn
opmen99810bACLACEArpFlagsIp=_Opmen99810bACLACEArpFlagsIp_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,26),_Opmen99810bACLACEArpFlagsIp_Type())
opmen99810bACLACEArpFlagsIp.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEArpFlagsIp.setStatus(_A)
class _Opmen99810bACLACEArpFlagsEthernet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Opmen99810bACLACEArpFlagsEthernet_Type.__name__=_C
_Opmen99810bACLACEArpFlagsEthernet_Object=MibTableColumn
opmen99810bACLACEArpFlagsEthernet=_Opmen99810bACLACEArpFlagsEthernet_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,27),_Opmen99810bACLACEArpFlagsEthernet_Type())
opmen99810bACLACEArpFlagsEthernet.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEArpFlagsEthernet.setStatus(_A)
class _Opmen99810bACLACESIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),('ip',1),(_T,2)))
_Opmen99810bACLACESIPType_Type.__name__=_C
_Opmen99810bACLACESIPType_Object=MibTableColumn
opmen99810bACLACESIPType=_Opmen99810bACLACESIPType_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,28),_Opmen99810bACLACESIPType_Type())
opmen99810bACLACESIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACESIPType.setStatus(_A)
_Opmen99810bACLACESIPIPAddress_Type=IpAddress
_Opmen99810bACLACESIPIPAddress_Object=MibTableColumn
opmen99810bACLACESIPIPAddress=_Opmen99810bACLACESIPIPAddress_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,29),_Opmen99810bACLACESIPIPAddress_Type())
opmen99810bACLACESIPIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACESIPIPAddress.setStatus(_A)
class _Opmen99810bACLACESIPNetworkPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_Opmen99810bACLACESIPNetworkPrefix_Type.__name__=_C
_Opmen99810bACLACESIPNetworkPrefix_Object=MibTableColumn
opmen99810bACLACESIPNetworkPrefix=_Opmen99810bACLACESIPNetworkPrefix_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,30),_Opmen99810bACLACESIPNetworkPrefix_Type())
opmen99810bACLACESIPNetworkPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACESIPNetworkPrefix.setStatus(_A)
class _Opmen99810bACLACEDIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),('ip',1),(_T,2)))
_Opmen99810bACLACEDIPType_Type.__name__=_C
_Opmen99810bACLACEDIPType_Object=MibTableColumn
opmen99810bACLACEDIPType=_Opmen99810bACLACEDIPType_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,32),_Opmen99810bACLACEDIPType_Type())
opmen99810bACLACEDIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEDIPType.setStatus(_A)
_Opmen99810bACLACEDIPIPAddress_Type=IpAddress
_Opmen99810bACLACEDIPIPAddress_Object=MibTableColumn
opmen99810bACLACEDIPIPAddress=_Opmen99810bACLACEDIPIPAddress_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,33),_Opmen99810bACLACEDIPIPAddress_Type())
opmen99810bACLACEDIPIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEDIPIPAddress.setStatus(_A)
class _Opmen99810bACLACEDIPNetworkPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_Opmen99810bACLACEDIPNetworkPrefix_Type.__name__=_C
_Opmen99810bACLACEDIPNetworkPrefix_Object=MibTableColumn
opmen99810bACLACEDIPNetworkPrefix=_Opmen99810bACLACEDIPNetworkPrefix_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,34),_Opmen99810bACLACEDIPNetworkPrefix_Type())
opmen99810bACLACEDIPNetworkPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEDIPNetworkPrefix.setStatus(_A)
class _Opmen99810bACLACEIPProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,257))
_Opmen99810bACLACEIPProtocol_Type.__name__=_C
_Opmen99810bACLACEIPProtocol_Object=MibTableColumn
opmen99810bACLACEIPProtocol=_Opmen99810bACLACEIPProtocol_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,36),_Opmen99810bACLACEIPProtocol_Type())
opmen99810bACLACEIPProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEIPProtocol.setStatus(_A)
class _Opmen99810bACLACEIPFlagsTTL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Opmen99810bACLACEIPFlagsTTL_Type.__name__=_C
_Opmen99810bACLACEIPFlagsTTL_Object=MibTableColumn
opmen99810bACLACEIPFlagsTTL=_Opmen99810bACLACEIPFlagsTTL_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,37),_Opmen99810bACLACEIPFlagsTTL_Type())
opmen99810bACLACEIPFlagsTTL.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEIPFlagsTTL.setStatus(_A)
class _Opmen99810bACLACEIPFlagsOptions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Z,0),(_a,1),(_R,2),(_T,3)))
_Opmen99810bACLACEIPFlagsOptions_Type.__name__=_C
_Opmen99810bACLACEIPFlagsOptions_Object=MibTableColumn
opmen99810bACLACEIPFlagsOptions=_Opmen99810bACLACEIPFlagsOptions_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,38),_Opmen99810bACLACEIPFlagsOptions_Type())
opmen99810bACLACEIPFlagsOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEIPFlagsOptions.setStatus(_A)
class _Opmen99810bACLACEIPFlagsFragment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Opmen99810bACLACEIPFlagsFragment_Type.__name__=_C
_Opmen99810bACLACEIPFlagsFragment_Object=MibTableColumn
opmen99810bACLACEIPFlagsFragment=_Opmen99810bACLACEIPFlagsFragment_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,39),_Opmen99810bACLACEIPFlagsFragment_Type())
opmen99810bACLACEIPFlagsFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEIPFlagsFragment.setStatus(_A)
class _Opmen99810bACLACEICMPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,257))
_Opmen99810bACLACEICMPType_Type.__name__=_C
_Opmen99810bACLACEICMPType_Object=MibTableColumn
opmen99810bACLACEICMPType=_Opmen99810bACLACEICMPType_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,40),_Opmen99810bACLACEICMPType_Type())
opmen99810bACLACEICMPType.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEICMPType.setStatus(_A)
class _Opmen99810bACLACEICMPCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,257))
_Opmen99810bACLACEICMPCode_Type.__name__=_C
_Opmen99810bACLACEICMPCode_Object=MibTableColumn
opmen99810bACLACEICMPCode=_Opmen99810bACLACEICMPCode_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,41),_Opmen99810bACLACEICMPCode_Type())
opmen99810bACLACEICMPCode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEICMPCode.setStatus(_A)
class _Opmen99810bACLACESourcePortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Opmen99810bACLACESourcePortMin_Type.__name__=_C
_Opmen99810bACLACESourcePortMin_Object=MibTableColumn
opmen99810bACLACESourcePortMin=_Opmen99810bACLACESourcePortMin_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,42),_Opmen99810bACLACESourcePortMin_Type())
opmen99810bACLACESourcePortMin.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACESourcePortMin.setStatus(_A)
class _Opmen99810bACLACESourcePortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Opmen99810bACLACESourcePortMax_Type.__name__=_C
_Opmen99810bACLACESourcePortMax_Object=MibTableColumn
opmen99810bACLACESourcePortMax=_Opmen99810bACLACESourcePortMax_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,43),_Opmen99810bACLACESourcePortMax_Type())
opmen99810bACLACESourcePortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACESourcePortMax.setStatus(_A)
class _Opmen99810bACLACEDestPortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Opmen99810bACLACEDestPortMin_Type.__name__=_C
_Opmen99810bACLACEDestPortMin_Object=MibTableColumn
opmen99810bACLACEDestPortMin=_Opmen99810bACLACEDestPortMin_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,44),_Opmen99810bACLACEDestPortMin_Type())
opmen99810bACLACEDestPortMin.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEDestPortMin.setStatus(_A)
class _Opmen99810bACLACEDestPortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Opmen99810bACLACEDestPortMax_Type.__name__=_C
_Opmen99810bACLACEDestPortMax_Object=MibTableColumn
opmen99810bACLACEDestPortMax=_Opmen99810bACLACEDestPortMax_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,45),_Opmen99810bACLACEDestPortMax_Type())
opmen99810bACLACEDestPortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEDestPortMax.setStatus(_A)
class _Opmen99810bACLACETCPFlagsFin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Z,0),(_a,1),(_R,2),(_T,3)))
_Opmen99810bACLACETCPFlagsFin_Type.__name__=_C
_Opmen99810bACLACETCPFlagsFin_Object=MibTableColumn
opmen99810bACLACETCPFlagsFin=_Opmen99810bACLACETCPFlagsFin_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,46),_Opmen99810bACLACETCPFlagsFin_Type())
opmen99810bACLACETCPFlagsFin.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACETCPFlagsFin.setStatus(_A)
class _Opmen99810bACLACETCPFlagsSyn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Z,0),(_a,1),(_R,2),(_T,3)))
_Opmen99810bACLACETCPFlagsSyn_Type.__name__=_C
_Opmen99810bACLACETCPFlagsSyn_Object=MibTableColumn
opmen99810bACLACETCPFlagsSyn=_Opmen99810bACLACETCPFlagsSyn_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,47),_Opmen99810bACLACETCPFlagsSyn_Type())
opmen99810bACLACETCPFlagsSyn.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACETCPFlagsSyn.setStatus(_A)
class _Opmen99810bACLACETCPFlagsRst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Z,0),(_a,1),(_R,2),(_T,3)))
_Opmen99810bACLACETCPFlagsRst_Type.__name__=_C
_Opmen99810bACLACETCPFlagsRst_Object=MibTableColumn
opmen99810bACLACETCPFlagsRst=_Opmen99810bACLACETCPFlagsRst_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,48),_Opmen99810bACLACETCPFlagsRst_Type())
opmen99810bACLACETCPFlagsRst.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACETCPFlagsRst.setStatus(_A)
class _Opmen99810bACLACETCPFlagsPsh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Z,0),(_a,1),(_R,2),(_T,3)))
_Opmen99810bACLACETCPFlagsPsh_Type.__name__=_C
_Opmen99810bACLACETCPFlagsPsh_Object=MibTableColumn
opmen99810bACLACETCPFlagsPsh=_Opmen99810bACLACETCPFlagsPsh_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,49),_Opmen99810bACLACETCPFlagsPsh_Type())
opmen99810bACLACETCPFlagsPsh.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACETCPFlagsPsh.setStatus(_A)
class _Opmen99810bACLACETCPFlagsAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Z,0),(_a,1),(_R,2),(_T,3)))
_Opmen99810bACLACETCPFlagsAck_Type.__name__=_C
_Opmen99810bACLACETCPFlagsAck_Object=MibTableColumn
opmen99810bACLACETCPFlagsAck=_Opmen99810bACLACETCPFlagsAck_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,50),_Opmen99810bACLACETCPFlagsAck_Type())
opmen99810bACLACETCPFlagsAck.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACETCPFlagsAck.setStatus(_A)
class _Opmen99810bACLACETCPFlagsUrg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Z,0),(_a,1),(_R,2),(_T,3)))
_Opmen99810bACLACETCPFlagsUrg_Type.__name__=_C
_Opmen99810bACLACETCPFlagsUrg_Object=MibTableColumn
opmen99810bACLACETCPFlagsUrg=_Opmen99810bACLACETCPFlagsUrg_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,51),_Opmen99810bACLACETCPFlagsUrg_Type())
opmen99810bACLACETCPFlagsUrg.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACETCPFlagsUrg.setStatus(_A)
class _Opmen99810bACLACERowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_U,1),(_X,2),(_Y,4),(_c,5)))
_Opmen99810bACLACERowStatus_Type.__name__=_C
_Opmen99810bACLACERowStatus_Object=MibTableColumn
opmen99810bACLACERowStatus=_Opmen99810bACLACERowStatus_Object((1,3,6,1,4,1,5205,2,94,2,9,3,2,1,66),_Opmen99810bACLACERowStatus_Type())
opmen99810bACLACERowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACERowStatus.setStatus(_A)
class _Opmen99810bACLACEClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noAction',0),(_e,1)))
_Opmen99810bACLACEClear_Type.__name__=_C
_Opmen99810bACLACEClear_Object=MibScalar
opmen99810bACLACEClear=_Opmen99810bACLACEClear_Object((1,3,6,1,4,1,5205,2,94,2,9,3,3),_Opmen99810bACLACEClear_Type())
opmen99810bACLACEClear.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEClear.setStatus(_A)
class _Opmen99810bACLACEMoveACEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Opmen99810bACLACEMoveACEID_Type.__name__=_C
_Opmen99810bACLACEMoveACEID_Object=MibScalar
opmen99810bACLACEMoveACEID=_Opmen99810bACLACEMoveACEID_Object((1,3,6,1,4,1,5205,2,94,2,9,3,4),_Opmen99810bACLACEMoveACEID_Type())
opmen99810bACLACEMoveACEID.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEMoveACEID.setStatus(_A)
class _Opmen99810bACLACEMoveNextACEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Opmen99810bACLACEMoveNextACEID_Type.__name__=_C
_Opmen99810bACLACEMoveNextACEID_Object=MibScalar
opmen99810bACLACEMoveNextACEID=_Opmen99810bACLACEMoveNextACEID_Object((1,3,6,1,4,1,5205,2,94,2,9,3,5),_Opmen99810bACLACEMoveNextACEID_Type())
opmen99810bACLACEMoveNextACEID.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bACLACEMoveNextACEID.setStatus(_A)
_Opmen99810bACLACEStatusTable_Object=MibTable
opmen99810bACLACEStatusTable=_Opmen99810bACLACEStatusTable_Object((1,3,6,1,4,1,5205,2,94,2,9,3,6))
if mibBuilder.loadTexts:opmen99810bACLACEStatusTable.setStatus(_A)
_Opmen99810bACLACEStatusEntry_Object=MibTableRow
opmen99810bACLACEStatusEntry=_Opmen99810bACLACEStatusEntry_Object((1,3,6,1,4,1,5205,2,94,2,9,3,6,1))
opmen99810bACLACEStatusEntry.setIndexNames((0,_G,_AJ))
if mibBuilder.loadTexts:opmen99810bACLACEStatusEntry.setStatus(_A)
class _Opmen99810bACLACEStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Opmen99810bACLACEStatusIndex_Type.__name__=_C
_Opmen99810bACLACEStatusIndex_Object=MibTableColumn
opmen99810bACLACEStatusIndex=_Opmen99810bACLACEStatusIndex_Object((1,3,6,1,4,1,5205,2,94,2,9,3,6,1,1),_Opmen99810bACLACEStatusIndex_Type())
opmen99810bACLACEStatusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bACLACEStatusIndex.setStatus(_A)
_Opmen99810bACLACEStatusUser_Type=DisplayString
_Opmen99810bACLACEStatusUser_Object=MibTableColumn
opmen99810bACLACEStatusUser=_Opmen99810bACLACEStatusUser_Object((1,3,6,1,4,1,5205,2,94,2,9,3,6,1,2),_Opmen99810bACLACEStatusUser_Type())
opmen99810bACLACEStatusUser.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bACLACEStatusUser.setStatus(_A)
class _Opmen99810bACLACEStatusID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Opmen99810bACLACEStatusID_Type.__name__=_C
_Opmen99810bACLACEStatusID_Object=MibTableColumn
opmen99810bACLACEStatusID=_Opmen99810bACLACEStatusID_Object((1,3,6,1,4,1,5205,2,94,2,9,3,6,1,3),_Opmen99810bACLACEStatusID_Type())
opmen99810bACLACEStatusID.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bACLACEStatusID.setStatus(_A)
_Opmen99810bACLACEStatusIngressPort_Type=DisplayString
_Opmen99810bACLACEStatusIngressPort_Object=MibTableColumn
opmen99810bACLACEStatusIngressPort=_Opmen99810bACLACEStatusIngressPort_Object((1,3,6,1,4,1,5205,2,94,2,9,3,6,1,4),_Opmen99810bACLACEStatusIngressPort_Type())
opmen99810bACLACEStatusIngressPort.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bACLACEStatusIngressPort.setStatus(_A)
_Opmen99810bACLACEStatusFrameType_Type=DisplayString
_Opmen99810bACLACEStatusFrameType_Object=MibTableColumn
opmen99810bACLACEStatusFrameType=_Opmen99810bACLACEStatusFrameType_Object((1,3,6,1,4,1,5205,2,94,2,9,3,6,1,5),_Opmen99810bACLACEStatusFrameType_Type())
opmen99810bACLACEStatusFrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bACLACEStatusFrameType.setStatus(_A)
_Opmen99810bACLACEStatusAction_Type=DisplayString
_Opmen99810bACLACEStatusAction_Object=MibTableColumn
opmen99810bACLACEStatusAction=_Opmen99810bACLACEStatusAction_Object((1,3,6,1,4,1,5205,2,94,2,9,3,6,1,6),_Opmen99810bACLACEStatusAction_Type())
opmen99810bACLACEStatusAction.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bACLACEStatusAction.setStatus(_A)
_Opmen99810bACLACEStatusRateLimiter_Type=DisplayString
_Opmen99810bACLACEStatusRateLimiter_Object=MibTableColumn
opmen99810bACLACEStatusRateLimiter=_Opmen99810bACLACEStatusRateLimiter_Object((1,3,6,1,4,1,5205,2,94,2,9,3,6,1,7),_Opmen99810bACLACEStatusRateLimiter_Type())
opmen99810bACLACEStatusRateLimiter.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bACLACEStatusRateLimiter.setStatus(_A)
_Opmen99810bACLACEStatusPortCopy_Type=DisplayString
_Opmen99810bACLACEStatusPortCopy_Object=MibTableColumn
opmen99810bACLACEStatusPortCopy=_Opmen99810bACLACEStatusPortCopy_Object((1,3,6,1,4,1,5205,2,94,2,9,3,6,1,8),_Opmen99810bACLACEStatusPortCopy_Type())
opmen99810bACLACEStatusPortCopy.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bACLACEStatusPortCopy.setStatus(_A)
_Opmen99810bACLACEStatusMirror_Type=DisplayString
_Opmen99810bACLACEStatusMirror_Object=MibTableColumn
opmen99810bACLACEStatusMirror=_Opmen99810bACLACEStatusMirror_Object((1,3,6,1,4,1,5205,2,94,2,9,3,6,1,9),_Opmen99810bACLACEStatusMirror_Type())
opmen99810bACLACEStatusMirror.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bACLACEStatusMirror.setStatus(_A)
_Opmen99810bACLACEStatusCPU_Type=DisplayString
_Opmen99810bACLACEStatusCPU_Object=MibTableColumn
opmen99810bACLACEStatusCPU=_Opmen99810bACLACEStatusCPU_Object((1,3,6,1,4,1,5205,2,94,2,9,3,6,1,10),_Opmen99810bACLACEStatusCPU_Type())
opmen99810bACLACEStatusCPU.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bACLACEStatusCPU.setStatus(_A)
_Opmen99810bACLACEStatusCounter_Type=Counter32
_Opmen99810bACLACEStatusCounter_Object=MibTableColumn
opmen99810bACLACEStatusCounter=_Opmen99810bACLACEStatusCounter_Object((1,3,6,1,4,1,5205,2,94,2,9,3,6,1,11),_Opmen99810bACLACEStatusCounter_Type())
opmen99810bACLACEStatusCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bACLACEStatusCounter.setStatus(_A)
_Opmen99810bACLACEStatusConflict_Type=DisplayString
_Opmen99810bACLACEStatusConflict_Object=MibTableColumn
opmen99810bACLACEStatusConflict=_Opmen99810bACLACEStatusConflict_Object((1,3,6,1,4,1,5205,2,94,2,9,3,6,1,12),_Opmen99810bACLACEStatusConflict_Type())
opmen99810bACLACEStatusConflict.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bACLACEStatusConflict.setStatus(_A)
_Opmen99810bBroadcastStormProtection_ObjectIdentity=ObjectIdentity
opmen99810bBroadcastStormProtection=_Opmen99810bBroadcastStormProtection_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,11))
_Opmen99810bBroadcastStormProtectionConfigurationTable_Object=MibTable
opmen99810bBroadcastStormProtectionConfigurationTable=_Opmen99810bBroadcastStormProtectionConfigurationTable_Object((1,3,6,1,4,1,5205,2,94,2,11,1))
if mibBuilder.loadTexts:opmen99810bBroadcastStormProtectionConfigurationTable.setStatus(_A)
_Opmen99810bBroadcastStormProtectionConfigurationEntry_Object=MibTableRow
opmen99810bBroadcastStormProtectionConfigurationEntry=_Opmen99810bBroadcastStormProtectionConfigurationEntry_Object((1,3,6,1,4,1,5205,2,94,2,11,1,1))
opmen99810bBroadcastStormProtectionConfigurationEntry.setIndexNames((0,_G,_AK))
if mibBuilder.loadTexts:opmen99810bBroadcastStormProtectionConfigurationEntry.setStatus(_A)
class _Opmen99810bBroadcastStormProtectionConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bBroadcastStormProtectionConfPort_Type.__name__=_C
_Opmen99810bBroadcastStormProtectionConfPort_Object=MibTableColumn
opmen99810bBroadcastStormProtectionConfPort=_Opmen99810bBroadcastStormProtectionConfPort_Object((1,3,6,1,4,1,5205,2,94,2,11,1,1,1),_Opmen99810bBroadcastStormProtectionConfPort_Type())
opmen99810bBroadcastStormProtectionConfPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bBroadcastStormProtectionConfPort.setStatus(_A)
class _Opmen99810bBroadcastStormProtectionConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bBroadcastStormProtectionConfMode_Type.__name__=_C
_Opmen99810bBroadcastStormProtectionConfMode_Object=MibTableColumn
opmen99810bBroadcastStormProtectionConfMode=_Opmen99810bBroadcastStormProtectionConfMode_Object((1,3,6,1,4,1,5205,2,94,2,11,1,1,2),_Opmen99810bBroadcastStormProtectionConfMode_Type())
opmen99810bBroadcastStormProtectionConfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bBroadcastStormProtectionConfMode.setStatus(_A)
class _Opmen99810bBroadcastStormProtectionConfAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Opmen99810bBroadcastStormProtectionConfAction_Type.__name__=_C
_Opmen99810bBroadcastStormProtectionConfAction_Object=MibTableColumn
opmen99810bBroadcastStormProtectionConfAction=_Opmen99810bBroadcastStormProtectionConfAction_Object((1,3,6,1,4,1,5205,2,94,2,11,1,1,3),_Opmen99810bBroadcastStormProtectionConfAction_Type())
opmen99810bBroadcastStormProtectionConfAction.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bBroadcastStormProtectionConfAction.setStatus(_A)
class _Opmen99810bBroadcastStormProtectionConfPPS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_Opmen99810bBroadcastStormProtectionConfPPS_Type.__name__=_C
_Opmen99810bBroadcastStormProtectionConfPPS_Object=MibTableColumn
opmen99810bBroadcastStormProtectionConfPPS=_Opmen99810bBroadcastStormProtectionConfPPS_Object((1,3,6,1,4,1,5205,2,94,2,11,1,1,4),_Opmen99810bBroadcastStormProtectionConfPPS_Type())
opmen99810bBroadcastStormProtectionConfPPS.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bBroadcastStormProtectionConfPPS.setStatus(_A)
class _Opmen99810bBroadcastStormProtectionConfTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Opmen99810bBroadcastStormProtectionConfTimer_Type.__name__=_C
_Opmen99810bBroadcastStormProtectionConfTimer_Object=MibTableColumn
opmen99810bBroadcastStormProtectionConfTimer=_Opmen99810bBroadcastStormProtectionConfTimer_Object((1,3,6,1,4,1,5205,2,94,2,11,1,1,5),_Opmen99810bBroadcastStormProtectionConfTimer_Type())
opmen99810bBroadcastStormProtectionConfTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bBroadcastStormProtectionConfTimer.setStatus(_A)
_Opmen99810bBroadcastStormProtectionConfstatus_Type=DisplayString
_Opmen99810bBroadcastStormProtectionConfstatus_Object=MibTableColumn
opmen99810bBroadcastStormProtectionConfstatus=_Opmen99810bBroadcastStormProtectionConfstatus_Object((1,3,6,1,4,1,5205,2,94,2,11,1,1,6),_Opmen99810bBroadcastStormProtectionConfstatus_Type())
opmen99810bBroadcastStormProtectionConfstatus.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bBroadcastStormProtectionConfstatus.setStatus(_A)
_Opmen99810bLoopProtection_ObjectIdentity=ObjectIdentity
opmen99810bLoopProtection=_Opmen99810bLoopProtection_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,12))
_Opmen99810bLoopProtectionConfig_ObjectIdentity=ObjectIdentity
opmen99810bLoopProtectionConfig=_Opmen99810bLoopProtectionConfig_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,12,1))
class _Opmen99810bLoopProtectionGlobalEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bLoopProtectionGlobalEnable_Type.__name__=_C
_Opmen99810bLoopProtectionGlobalEnable_Object=MibScalar
opmen99810bLoopProtectionGlobalEnable=_Opmen99810bLoopProtectionGlobalEnable_Object((1,3,6,1,4,1,5205,2,94,2,12,1,1),_Opmen99810bLoopProtectionGlobalEnable_Type())
opmen99810bLoopProtectionGlobalEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bLoopProtectionGlobalEnable.setStatus(_A)
class _Opmen99810bLoopProtectionTranmisstionTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Opmen99810bLoopProtectionTranmisstionTime_Type.__name__=_C
_Opmen99810bLoopProtectionTranmisstionTime_Object=MibScalar
opmen99810bLoopProtectionTranmisstionTime=_Opmen99810bLoopProtectionTranmisstionTime_Object((1,3,6,1,4,1,5205,2,94,2,12,1,2),_Opmen99810bLoopProtectionTranmisstionTime_Type())
opmen99810bLoopProtectionTranmisstionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bLoopProtectionTranmisstionTime.setStatus(_A)
class _Opmen99810bLoopProtectionShutdownTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_Opmen99810bLoopProtectionShutdownTime_Type.__name__=_C
_Opmen99810bLoopProtectionShutdownTime_Object=MibScalar
opmen99810bLoopProtectionShutdownTime=_Opmen99810bLoopProtectionShutdownTime_Object((1,3,6,1,4,1,5205,2,94,2,12,1,3),_Opmen99810bLoopProtectionShutdownTime_Type())
opmen99810bLoopProtectionShutdownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bLoopProtectionShutdownTime.setStatus(_A)
_Opmen99810bLoopProtectionConfigurationTable_Object=MibTable
opmen99810bLoopProtectionConfigurationTable=_Opmen99810bLoopProtectionConfigurationTable_Object((1,3,6,1,4,1,5205,2,94,2,12,1,4))
if mibBuilder.loadTexts:opmen99810bLoopProtectionConfigurationTable.setStatus(_A)
_Opmen99810bLoopProtectionConfigurationEntry_Object=MibTableRow
opmen99810bLoopProtectionConfigurationEntry=_Opmen99810bLoopProtectionConfigurationEntry_Object((1,3,6,1,4,1,5205,2,94,2,12,1,4,1))
opmen99810bLoopProtectionConfigurationEntry.setIndexNames((0,_G,_AL))
if mibBuilder.loadTexts:opmen99810bLoopProtectionConfigurationEntry.setStatus(_A)
class _Opmen99810bLoopProtectionConfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bLoopProtectionConfPort_Type.__name__=_C
_Opmen99810bLoopProtectionConfPort_Object=MibTableColumn
opmen99810bLoopProtectionConfPort=_Opmen99810bLoopProtectionConfPort_Object((1,3,6,1,4,1,5205,2,94,2,12,1,4,1,1),_Opmen99810bLoopProtectionConfPort_Type())
opmen99810bLoopProtectionConfPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bLoopProtectionConfPort.setStatus(_A)
class _Opmen99810bLoopProtectionConfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bLoopProtectionConfEnable_Type.__name__=_C
_Opmen99810bLoopProtectionConfEnable_Object=MibTableColumn
opmen99810bLoopProtectionConfEnable=_Opmen99810bLoopProtectionConfEnable_Object((1,3,6,1,4,1,5205,2,94,2,12,1,4,1,2),_Opmen99810bLoopProtectionConfEnable_Type())
opmen99810bLoopProtectionConfEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bLoopProtectionConfEnable.setStatus(_A)
class _Opmen99810bLoopProtectionConfAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('shutdown',0),('shutdownLog',1),('log',2)))
_Opmen99810bLoopProtectionConfAction_Type.__name__=_C
_Opmen99810bLoopProtectionConfAction_Object=MibTableColumn
opmen99810bLoopProtectionConfAction=_Opmen99810bLoopProtectionConfAction_Object((1,3,6,1,4,1,5205,2,94,2,12,1,4,1,3),_Opmen99810bLoopProtectionConfAction_Type())
opmen99810bLoopProtectionConfAction.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bLoopProtectionConfAction.setStatus(_A)
class _Opmen99810bLoopProtectionConfTxmode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bLoopProtectionConfTxmode_Type.__name__=_C
_Opmen99810bLoopProtectionConfTxmode_Object=MibTableColumn
opmen99810bLoopProtectionConfTxmode=_Opmen99810bLoopProtectionConfTxmode_Object((1,3,6,1,4,1,5205,2,94,2,12,1,4,1,4),_Opmen99810bLoopProtectionConfTxmode_Type())
opmen99810bLoopProtectionConfTxmode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bLoopProtectionConfTxmode.setStatus(_A)
_Opmen99810bLoopProtectionStatusTable_Object=MibTable
opmen99810bLoopProtectionStatusTable=_Opmen99810bLoopProtectionStatusTable_Object((1,3,6,1,4,1,5205,2,94,2,12,2))
if mibBuilder.loadTexts:opmen99810bLoopProtectionStatusTable.setStatus(_A)
_Opmen99810bLoopProtectionStatusEntry_Object=MibTableRow
opmen99810bLoopProtectionStatusEntry=_Opmen99810bLoopProtectionStatusEntry_Object((1,3,6,1,4,1,5205,2,94,2,12,2,1))
opmen99810bLoopProtectionStatusEntry.setIndexNames((0,_G,_AM))
if mibBuilder.loadTexts:opmen99810bLoopProtectionStatusEntry.setStatus(_A)
class _Opmen99810bLoopProtectionStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bLoopProtectionStatusPort_Type.__name__=_C
_Opmen99810bLoopProtectionStatusPort_Object=MibTableColumn
opmen99810bLoopProtectionStatusPort=_Opmen99810bLoopProtectionStatusPort_Object((1,3,6,1,4,1,5205,2,94,2,12,2,1,1),_Opmen99810bLoopProtectionStatusPort_Type())
opmen99810bLoopProtectionStatusPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bLoopProtectionStatusPort.setStatus(_A)
_Opmen99810bLoopProtectionStatusAction_Type=DisplayString
_Opmen99810bLoopProtectionStatusAction_Object=MibTableColumn
opmen99810bLoopProtectionStatusAction=_Opmen99810bLoopProtectionStatusAction_Object((1,3,6,1,4,1,5205,2,94,2,12,2,1,2),_Opmen99810bLoopProtectionStatusAction_Type())
opmen99810bLoopProtectionStatusAction.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bLoopProtectionStatusAction.setStatus(_A)
_Opmen99810bLoopProtectionStatusTransmit_Type=DisplayString
_Opmen99810bLoopProtectionStatusTransmit_Object=MibTableColumn
opmen99810bLoopProtectionStatusTransmit=_Opmen99810bLoopProtectionStatusTransmit_Object((1,3,6,1,4,1,5205,2,94,2,12,2,1,3),_Opmen99810bLoopProtectionStatusTransmit_Type())
opmen99810bLoopProtectionStatusTransmit.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bLoopProtectionStatusTransmit.setStatus(_A)
class _Opmen99810bLoopProtectionStatusLoops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_Opmen99810bLoopProtectionStatusLoops_Type.__name__=_C
_Opmen99810bLoopProtectionStatusLoops_Object=MibTableColumn
opmen99810bLoopProtectionStatusLoops=_Opmen99810bLoopProtectionStatusLoops_Object((1,3,6,1,4,1,5205,2,94,2,12,2,1,4),_Opmen99810bLoopProtectionStatusLoops_Type())
opmen99810bLoopProtectionStatusLoops.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bLoopProtectionStatusLoops.setStatus(_A)
_Opmen99810bLoopProtectionStatusStatus_Type=DisplayString
_Opmen99810bLoopProtectionStatusStatus_Object=MibTableColumn
opmen99810bLoopProtectionStatusStatus=_Opmen99810bLoopProtectionStatusStatus_Object((1,3,6,1,4,1,5205,2,94,2,12,2,1,5),_Opmen99810bLoopProtectionStatusStatus_Type())
opmen99810bLoopProtectionStatusStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bLoopProtectionStatusStatus.setStatus(_A)
_Opmen99810bLoopProtectionStatusLoop_Type=DisplayString
_Opmen99810bLoopProtectionStatusLoop_Object=MibTableColumn
opmen99810bLoopProtectionStatusLoop=_Opmen99810bLoopProtectionStatusLoop_Object((1,3,6,1,4,1,5205,2,94,2,12,2,1,6),_Opmen99810bLoopProtectionStatusLoop_Type())
opmen99810bLoopProtectionStatusLoop.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bLoopProtectionStatusLoop.setStatus(_A)
_Opmen99810bLoopProtectionStatusTimeLastLoop_Type=DisplayString
_Opmen99810bLoopProtectionStatusTimeLastLoop_Object=MibTableColumn
opmen99810bLoopProtectionStatusTimeLastLoop=_Opmen99810bLoopProtectionStatusTimeLastLoop_Object((1,3,6,1,4,1,5205,2,94,2,12,2,1,7),_Opmen99810bLoopProtectionStatusTimeLastLoop_Type())
opmen99810bLoopProtectionStatusTimeLastLoop.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bLoopProtectionStatusTimeLastLoop.setStatus(_A)
_Opmen99810bQos_ObjectIdentity=ObjectIdentity
opmen99810bQos=_Opmen99810bQos_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,14))
_Opmen99810bQosPortClassification_ObjectIdentity=ObjectIdentity
opmen99810bQosPortClassification=_Opmen99810bQosPortClassification_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,14,1))
_Opmen99810bQosPortClassificationTable_Object=MibTable
opmen99810bQosPortClassificationTable=_Opmen99810bQosPortClassificationTable_Object((1,3,6,1,4,1,5205,2,94,2,14,1,1))
if mibBuilder.loadTexts:opmen99810bQosPortClassificationTable.setStatus(_A)
_Opmen99810bQosPortClassificationEntry_Object=MibTableRow
opmen99810bQosPortClassificationEntry=_Opmen99810bQosPortClassificationEntry_Object((1,3,6,1,4,1,5205,2,94,2,14,1,1,1))
opmen99810bQosPortClassificationEntry.setIndexNames((0,_G,_AN))
if mibBuilder.loadTexts:opmen99810bQosPortClassificationEntry.setStatus(_A)
class _Opmen99810bQosPortClassificationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bQosPortClassificationPort_Type.__name__=_C
_Opmen99810bQosPortClassificationPort_Object=MibTableColumn
opmen99810bQosPortClassificationPort=_Opmen99810bQosPortClassificationPort_Object((1,3,6,1,4,1,5205,2,94,2,14,1,1,1,1),_Opmen99810bQosPortClassificationPort_Type())
opmen99810bQosPortClassificationPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosPortClassificationPort.setStatus(_A)
class _Opmen99810bQosPortClassificationQoSclass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Opmen99810bQosPortClassificationQoSclass_Type.__name__=_C
_Opmen99810bQosPortClassificationQoSclass_Object=MibTableColumn
opmen99810bQosPortClassificationQoSclass=_Opmen99810bQosPortClassificationQoSclass_Object((1,3,6,1,4,1,5205,2,94,2,14,1,1,1,2),_Opmen99810bQosPortClassificationQoSclass_Type())
opmen99810bQosPortClassificationQoSclass.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosPortClassificationQoSclass.setStatus(_A)
class _Opmen99810bQosPortClassificationDPlevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Opmen99810bQosPortClassificationDPlevel_Type.__name__=_C
_Opmen99810bQosPortClassificationDPlevel_Object=MibTableColumn
opmen99810bQosPortClassificationDPlevel=_Opmen99810bQosPortClassificationDPlevel_Object((1,3,6,1,4,1,5205,2,94,2,14,1,1,1,3),_Opmen99810bQosPortClassificationDPlevel_Type())
opmen99810bQosPortClassificationDPlevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosPortClassificationDPlevel.setStatus(_A)
class _Opmen99810bQosPortClassificationPCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Opmen99810bQosPortClassificationPCP_Type.__name__=_C
_Opmen99810bQosPortClassificationPCP_Object=MibTableColumn
opmen99810bQosPortClassificationPCP=_Opmen99810bQosPortClassificationPCP_Object((1,3,6,1,4,1,5205,2,94,2,14,1,1,1,4),_Opmen99810bQosPortClassificationPCP_Type())
opmen99810bQosPortClassificationPCP.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosPortClassificationPCP.setStatus(_A)
class _Opmen99810bQosPortClassificationDEI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bQosPortClassificationDEI_Type.__name__=_C
_Opmen99810bQosPortClassificationDEI_Object=MibTableColumn
opmen99810bQosPortClassificationDEI=_Opmen99810bQosPortClassificationDEI_Object((1,3,6,1,4,1,5205,2,94,2,14,1,1,1,5),_Opmen99810bQosPortClassificationDEI_Type())
opmen99810bQosPortClassificationDEI.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosPortClassificationDEI.setStatus(_A)
class _Opmen99810bQosPortClassificationTagClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bQosPortClassificationTagClass_Type.__name__=_C
_Opmen99810bQosPortClassificationTagClass_Object=MibTableColumn
opmen99810bQosPortClassificationTagClass=_Opmen99810bQosPortClassificationTagClass_Object((1,3,6,1,4,1,5205,2,94,2,14,1,1,1,6),_Opmen99810bQosPortClassificationTagClass_Type())
opmen99810bQosPortClassificationTagClass.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosPortClassificationTagClass.setStatus(_A)
class _Opmen99810bQosPortClassificationDSCPBased_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bQosPortClassificationDSCPBased_Type.__name__=_C
_Opmen99810bQosPortClassificationDSCPBased_Object=MibTableColumn
opmen99810bQosPortClassificationDSCPBased=_Opmen99810bQosPortClassificationDSCPBased_Object((1,3,6,1,4,1,5205,2,94,2,14,1,1,1,7),_Opmen99810bQosPortClassificationDSCPBased_Type())
opmen99810bQosPortClassificationDSCPBased.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosPortClassificationDSCPBased.setStatus(_A)
_Opmen99810bQoSIngressPortTagClassificationTable_Object=MibTable
opmen99810bQoSIngressPortTagClassificationTable=_Opmen99810bQoSIngressPortTagClassificationTable_Object((1,3,6,1,4,1,5205,2,94,2,14,1,2))
if mibBuilder.loadTexts:opmen99810bQoSIngressPortTagClassificationTable.setStatus(_A)
_Opmen99810bQoSIngressPortTagClassificationEntry_Object=MibTableRow
opmen99810bQoSIngressPortTagClassificationEntry=_Opmen99810bQoSIngressPortTagClassificationEntry_Object((1,3,6,1,4,1,5205,2,94,2,14,1,2,1))
opmen99810bQoSIngressPortTagClassificationEntry.setIndexNames((0,_G,_AO),(0,_G,_AP),(0,_G,_AQ))
if mibBuilder.loadTexts:opmen99810bQoSIngressPortTagClassificationEntry.setStatus(_A)
class _Opmen99810bQoSIngressPortTagClassificationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bQoSIngressPortTagClassificationPort_Type.__name__=_C
_Opmen99810bQoSIngressPortTagClassificationPort_Object=MibTableColumn
opmen99810bQoSIngressPortTagClassificationPort=_Opmen99810bQoSIngressPortTagClassificationPort_Object((1,3,6,1,4,1,5205,2,94,2,14,1,2,1,1),_Opmen99810bQoSIngressPortTagClassificationPort_Type())
opmen99810bQoSIngressPortTagClassificationPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQoSIngressPortTagClassificationPort.setStatus(_A)
class _Opmen99810bQoSIngressPortTagPCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('pcp0',1),('pcp1',2),('pcp2',3),('pcp3',4),('pcp4',5),('pcp5',6),('pcp6',7),('pcp7',8)))
_Opmen99810bQoSIngressPortTagPCP_Type.__name__=_C
_Opmen99810bQoSIngressPortTagPCP_Object=MibTableColumn
opmen99810bQoSIngressPortTagPCP=_Opmen99810bQoSIngressPortTagPCP_Object((1,3,6,1,4,1,5205,2,94,2,14,1,2,1,2),_Opmen99810bQoSIngressPortTagPCP_Type())
opmen99810bQoSIngressPortTagPCP.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQoSIngressPortTagPCP.setStatus(_A)
class _Opmen99810bQoSIngressPortTagDEI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dei0',1),('dei1',2)))
_Opmen99810bQoSIngressPortTagDEI_Type.__name__=_C
_Opmen99810bQoSIngressPortTagDEI_Object=MibTableColumn
opmen99810bQoSIngressPortTagDEI=_Opmen99810bQoSIngressPortTagDEI_Object((1,3,6,1,4,1,5205,2,94,2,14,1,2,1,3),_Opmen99810bQoSIngressPortTagDEI_Type())
opmen99810bQoSIngressPortTagDEI.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQoSIngressPortTagDEI.setStatus(_A)
class _Opmen99810bQoSIngressPortTagQosClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Opmen99810bQoSIngressPortTagQosClass_Type.__name__=_C
_Opmen99810bQoSIngressPortTagQosClass_Object=MibTableColumn
opmen99810bQoSIngressPortTagQosClass=_Opmen99810bQoSIngressPortTagQosClass_Object((1,3,6,1,4,1,5205,2,94,2,14,1,2,1,4),_Opmen99810bQoSIngressPortTagQosClass_Type())
opmen99810bQoSIngressPortTagQosClass.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQoSIngressPortTagQosClass.setStatus(_A)
class _Opmen99810bQoSIngressPortTagDPLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Opmen99810bQoSIngressPortTagDPLevel_Type.__name__=_C
_Opmen99810bQoSIngressPortTagDPLevel_Object=MibTableColumn
opmen99810bQoSIngressPortTagDPLevel=_Opmen99810bQoSIngressPortTagDPLevel_Object((1,3,6,1,4,1,5205,2,94,2,14,1,2,1,5),_Opmen99810bQoSIngressPortTagDPLevel_Type())
opmen99810bQoSIngressPortTagDPLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQoSIngressPortTagDPLevel.setStatus(_A)
_Opmen99810bQosPortPolicingTable_Object=MibTable
opmen99810bQosPortPolicingTable=_Opmen99810bQosPortPolicingTable_Object((1,3,6,1,4,1,5205,2,94,2,14,2))
if mibBuilder.loadTexts:opmen99810bQosPortPolicingTable.setStatus(_A)
_Opmen99810bQosPortPolicingEntry_Object=MibTableRow
opmen99810bQosPortPolicingEntry=_Opmen99810bQosPortPolicingEntry_Object((1,3,6,1,4,1,5205,2,94,2,14,2,1))
opmen99810bQosPortPolicingEntry.setIndexNames((0,_G,_AR))
if mibBuilder.loadTexts:opmen99810bQosPortPolicingEntry.setStatus(_A)
class _Opmen99810bQosPortPolicingPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bQosPortPolicingPort_Type.__name__=_C
_Opmen99810bQosPortPolicingPort_Object=MibTableColumn
opmen99810bQosPortPolicingPort=_Opmen99810bQosPortPolicingPort_Object((1,3,6,1,4,1,5205,2,94,2,14,2,1,1),_Opmen99810bQosPortPolicingPort_Type())
opmen99810bQosPortPolicingPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosPortPolicingPort.setStatus(_A)
class _Opmen99810bQosPortPolicingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bQosPortPolicingMode_Type.__name__=_C
_Opmen99810bQosPortPolicingMode_Object=MibTableColumn
opmen99810bQosPortPolicingMode=_Opmen99810bQosPortPolicingMode_Object((1,3,6,1,4,1,5205,2,94,2,14,2,1,2),_Opmen99810bQosPortPolicingMode_Type())
opmen99810bQosPortPolicingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosPortPolicingMode.setStatus(_A)
class _Opmen99810bQosPortPolicingRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000000))
_Opmen99810bQosPortPolicingRate_Type.__name__=_C
_Opmen99810bQosPortPolicingRate_Object=MibTableColumn
opmen99810bQosPortPolicingRate=_Opmen99810bQosPortPolicingRate_Object((1,3,6,1,4,1,5205,2,94,2,14,2,1,3),_Opmen99810bQosPortPolicingRate_Type())
opmen99810bQosPortPolicingRate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosPortPolicingRate.setStatus(_A)
class _Opmen99810bQosPortPolicingUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('kbps',0),('fps',1)))
_Opmen99810bQosPortPolicingUnit_Type.__name__=_C
_Opmen99810bQosPortPolicingUnit_Object=MibTableColumn
opmen99810bQosPortPolicingUnit=_Opmen99810bQosPortPolicingUnit_Object((1,3,6,1,4,1,5205,2,94,2,14,2,1,4),_Opmen99810bQosPortPolicingUnit_Type())
opmen99810bQosPortPolicingUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosPortPolicingUnit.setStatus(_A)
class _Opmen99810bQosPortPolicingFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bQosPortPolicingFlowControl_Type.__name__=_C
_Opmen99810bQosPortPolicingFlowControl_Object=MibTableColumn
opmen99810bQosPortPolicingFlowControl=_Opmen99810bQosPortPolicingFlowControl_Object((1,3,6,1,4,1,5205,2,94,2,14,2,1,5),_Opmen99810bQosPortPolicingFlowControl_Type())
opmen99810bQosPortPolicingFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosPortPolicingFlowControl.setStatus(_A)
_Opmen99810bQosPortScheduler_ObjectIdentity=ObjectIdentity
opmen99810bQosPortScheduler=_Opmen99810bQosPortScheduler_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,14,3))
_Opmen99810bQosPortSchedulerModeTable_Object=MibTable
opmen99810bQosPortSchedulerModeTable=_Opmen99810bQosPortSchedulerModeTable_Object((1,3,6,1,4,1,5205,2,94,2,14,3,1))
if mibBuilder.loadTexts:opmen99810bQosPortSchedulerModeTable.setStatus(_A)
_Opmen99810bQosPortSchedulerModeEntry_Object=MibTableRow
opmen99810bQosPortSchedulerModeEntry=_Opmen99810bQosPortSchedulerModeEntry_Object((1,3,6,1,4,1,5205,2,94,2,14,3,1,1))
opmen99810bQosPortSchedulerModeEntry.setIndexNames((0,_G,_AS))
if mibBuilder.loadTexts:opmen99810bQosPortSchedulerModeEntry.setStatus(_A)
class _Opmen99810bQosSchedulerModePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bQosSchedulerModePort_Type.__name__=_C
_Opmen99810bQosSchedulerModePort_Object=MibTableColumn
opmen99810bQosSchedulerModePort=_Opmen99810bQosSchedulerModePort_Object((1,3,6,1,4,1,5205,2,94,2,14,3,1,1,1),_Opmen99810bQosSchedulerModePort_Type())
opmen99810bQosSchedulerModePort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosSchedulerModePort.setStatus(_A)
class _Opmen99810bQosSchedulerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('strictPriority',0),('weighted',1)))
_Opmen99810bQosSchedulerMode_Type.__name__=_C
_Opmen99810bQosSchedulerMode_Object=MibTableColumn
opmen99810bQosSchedulerMode=_Opmen99810bQosSchedulerMode_Object((1,3,6,1,4,1,5205,2,94,2,14,3,1,1,2),_Opmen99810bQosSchedulerMode_Type())
opmen99810bQosSchedulerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosSchedulerMode.setStatus(_A)
class _Opmen99810bQosSchedulerShaper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bQosSchedulerShaper_Type.__name__=_C
_Opmen99810bQosSchedulerShaper_Object=MibTableColumn
opmen99810bQosSchedulerShaper=_Opmen99810bQosSchedulerShaper_Object((1,3,6,1,4,1,5205,2,94,2,14,3,1,1,3),_Opmen99810bQosSchedulerShaper_Type())
opmen99810bQosSchedulerShaper.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosSchedulerShaper.setStatus(_A)
class _Opmen99810bQosSchedulerShaperRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000000))
_Opmen99810bQosSchedulerShaperRate_Type.__name__=_C
_Opmen99810bQosSchedulerShaperRate_Object=MibTableColumn
opmen99810bQosSchedulerShaperRate=_Opmen99810bQosSchedulerShaperRate_Object((1,3,6,1,4,1,5205,2,94,2,14,3,1,1,4),_Opmen99810bQosSchedulerShaperRate_Type())
opmen99810bQosSchedulerShaperRate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosSchedulerShaperRate.setStatus(_A)
_Opmen99810bQosPortSchedulerTable_Object=MibTable
opmen99810bQosPortSchedulerTable=_Opmen99810bQosPortSchedulerTable_Object((1,3,6,1,4,1,5205,2,94,2,14,3,2))
if mibBuilder.loadTexts:opmen99810bQosPortSchedulerTable.setStatus(_A)
_Opmen99810bQosPortSchedulerEntry_Object=MibTableRow
opmen99810bQosPortSchedulerEntry=_Opmen99810bQosPortSchedulerEntry_Object((1,3,6,1,4,1,5205,2,94,2,14,3,2,1))
opmen99810bQosPortSchedulerEntry.setIndexNames((0,_G,_AT),(0,_G,_AU))
if mibBuilder.loadTexts:opmen99810bQosPortSchedulerEntry.setStatus(_A)
class _Opmen99810bQosSchedulerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bQosSchedulerPort_Type.__name__=_C
_Opmen99810bQosSchedulerPort_Object=MibTableColumn
opmen99810bQosSchedulerPort=_Opmen99810bQosSchedulerPort_Object((1,3,6,1,4,1,5205,2,94,2,14,3,2,1,1),_Opmen99810bQosSchedulerPort_Type())
opmen99810bQosSchedulerPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosSchedulerPort.setStatus(_A)
class _Opmen99810bQosSchedulerPortQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('q0',1),('q1',2),('q2',3),('q3',4),('q4',5),('q5',6),('q6',7),('q7',8)))
_Opmen99810bQosSchedulerPortQueue_Type.__name__=_C
_Opmen99810bQosSchedulerPortQueue_Object=MibTableColumn
opmen99810bQosSchedulerPortQueue=_Opmen99810bQosSchedulerPortQueue_Object((1,3,6,1,4,1,5205,2,94,2,14,3,2,1,2),_Opmen99810bQosSchedulerPortQueue_Type())
opmen99810bQosSchedulerPortQueue.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosSchedulerPortQueue.setStatus(_A)
class _Opmen99810bQosSchedulerPortQueueShaper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bQosSchedulerPortQueueShaper_Type.__name__=_C
_Opmen99810bQosSchedulerPortQueueShaper_Object=MibTableColumn
opmen99810bQosSchedulerPortQueueShaper=_Opmen99810bQosSchedulerPortQueueShaper_Object((1,3,6,1,4,1,5205,2,94,2,14,3,2,1,3),_Opmen99810bQosSchedulerPortQueueShaper_Type())
opmen99810bQosSchedulerPortQueueShaper.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosSchedulerPortQueueShaper.setStatus(_A)
class _Opmen99810bQosSchedulerPortQueueShaperRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000000))
_Opmen99810bQosSchedulerPortQueueShaperRate_Type.__name__=_C
_Opmen99810bQosSchedulerPortQueueShaperRate_Object=MibTableColumn
opmen99810bQosSchedulerPortQueueShaperRate=_Opmen99810bQosSchedulerPortQueueShaperRate_Object((1,3,6,1,4,1,5205,2,94,2,14,3,2,1,4),_Opmen99810bQosSchedulerPortQueueShaperRate_Type())
opmen99810bQosSchedulerPortQueueShaperRate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosSchedulerPortQueueShaperRate.setStatus(_A)
class _Opmen99810bQosSchedulerPortQueueShaperExcess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bQosSchedulerPortQueueShaperExcess_Type.__name__=_C
_Opmen99810bQosSchedulerPortQueueShaperExcess_Object=MibTableColumn
opmen99810bQosSchedulerPortQueueShaperExcess=_Opmen99810bQosSchedulerPortQueueShaperExcess_Object((1,3,6,1,4,1,5205,2,94,2,14,3,2,1,5),_Opmen99810bQosSchedulerPortQueueShaperExcess_Type())
opmen99810bQosSchedulerPortQueueShaperExcess.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosSchedulerPortQueueShaperExcess.setStatus(_A)
class _Opmen99810bQosSchedulerPortQueueSchedulerWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Opmen99810bQosSchedulerPortQueueSchedulerWeight_Type.__name__=_C
_Opmen99810bQosSchedulerPortQueueSchedulerWeight_Object=MibTableColumn
opmen99810bQosSchedulerPortQueueSchedulerWeight=_Opmen99810bQosSchedulerPortQueueSchedulerWeight_Object((1,3,6,1,4,1,5205,2,94,2,14,3,2,1,6),_Opmen99810bQosSchedulerPortQueueSchedulerWeight_Type())
opmen99810bQosSchedulerPortQueueSchedulerWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosSchedulerPortQueueSchedulerWeight.setStatus(_A)
_Opmen99810bQosSchedulerPortQueueSchedulerPercent_Type=DisplayString
_Opmen99810bQosSchedulerPortQueueSchedulerPercent_Object=MibTableColumn
opmen99810bQosSchedulerPortQueueSchedulerPercent=_Opmen99810bQosSchedulerPortQueueSchedulerPercent_Object((1,3,6,1,4,1,5205,2,94,2,14,3,2,1,7),_Opmen99810bQosSchedulerPortQueueSchedulerPercent_Type())
opmen99810bQosSchedulerPortQueueSchedulerPercent.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bQosSchedulerPortQueueSchedulerPercent.setStatus(_A)
_Opmen99810bQosPortEgressTagRemarking_ObjectIdentity=ObjectIdentity
opmen99810bQosPortEgressTagRemarking=_Opmen99810bQosPortEgressTagRemarking_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,14,4))
_Opmen99810bQosPortEgressTagRemarkingTable_Object=MibTable
opmen99810bQosPortEgressTagRemarkingTable=_Opmen99810bQosPortEgressTagRemarkingTable_Object((1,3,6,1,4,1,5205,2,94,2,14,4,1))
if mibBuilder.loadTexts:opmen99810bQosPortEgressTagRemarkingTable.setStatus(_A)
_Opmen99810bQosPortEgressTagRemarkingEntry_Object=MibTableRow
opmen99810bQosPortEgressTagRemarkingEntry=_Opmen99810bQosPortEgressTagRemarkingEntry_Object((1,3,6,1,4,1,5205,2,94,2,14,4,1,1))
opmen99810bQosPortEgressTagRemarkingEntry.setIndexNames((0,_G,_AV))
if mibBuilder.loadTexts:opmen99810bQosPortEgressTagRemarkingEntry.setStatus(_A)
class _Opmen99810bQosEgressTagRemarkingPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bQosEgressTagRemarkingPort_Type.__name__=_C
_Opmen99810bQosEgressTagRemarkingPort_Object=MibTableColumn
opmen99810bQosEgressTagRemarkingPort=_Opmen99810bQosEgressTagRemarkingPort_Object((1,3,6,1,4,1,5205,2,94,2,14,4,1,1,1),_Opmen99810bQosEgressTagRemarkingPort_Type())
opmen99810bQosEgressTagRemarkingPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosEgressTagRemarkingPort.setStatus(_A)
class _Opmen99810bQosEgressTagRemarkingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('classified',0),('default',1),('mapped',2)))
_Opmen99810bQosEgressTagRemarkingMode_Type.__name__=_C
_Opmen99810bQosEgressTagRemarkingMode_Object=MibTableColumn
opmen99810bQosEgressTagRemarkingMode=_Opmen99810bQosEgressTagRemarkingMode_Object((1,3,6,1,4,1,5205,2,94,2,14,4,1,1,2),_Opmen99810bQosEgressTagRemarkingMode_Type())
opmen99810bQosEgressTagRemarkingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosEgressTagRemarkingMode.setStatus(_A)
_Opmen99810bQosPortEgressTagRemarkingDefTable_Object=MibTable
opmen99810bQosPortEgressTagRemarkingDefTable=_Opmen99810bQosPortEgressTagRemarkingDefTable_Object((1,3,6,1,4,1,5205,2,94,2,14,4,2))
if mibBuilder.loadTexts:opmen99810bQosPortEgressTagRemarkingDefTable.setStatus(_A)
_Opmen99810bQosPortEgressTagRemarkingDefEntry_Object=MibTableRow
opmen99810bQosPortEgressTagRemarkingDefEntry=_Opmen99810bQosPortEgressTagRemarkingDefEntry_Object((1,3,6,1,4,1,5205,2,94,2,14,4,2,1))
opmen99810bQosPortEgressTagRemarkingDefEntry.setIndexNames((0,_G,_AW))
if mibBuilder.loadTexts:opmen99810bQosPortEgressTagRemarkingDefEntry.setStatus(_A)
class _Opmen99810bQosEgressTagRemarkingDefPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bQosEgressTagRemarkingDefPort_Type.__name__=_C
_Opmen99810bQosEgressTagRemarkingDefPort_Object=MibTableColumn
opmen99810bQosEgressTagRemarkingDefPort=_Opmen99810bQosEgressTagRemarkingDefPort_Object((1,3,6,1,4,1,5205,2,94,2,14,4,2,1,1),_Opmen99810bQosEgressTagRemarkingDefPort_Type())
opmen99810bQosEgressTagRemarkingDefPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosEgressTagRemarkingDefPort.setStatus(_A)
class _Opmen99810bQosEgressTagRemarkingDefPCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Opmen99810bQosEgressTagRemarkingDefPCP_Type.__name__=_C
_Opmen99810bQosEgressTagRemarkingDefPCP_Object=MibTableColumn
opmen99810bQosEgressTagRemarkingDefPCP=_Opmen99810bQosEgressTagRemarkingDefPCP_Object((1,3,6,1,4,1,5205,2,94,2,14,4,2,1,2),_Opmen99810bQosEgressTagRemarkingDefPCP_Type())
opmen99810bQosEgressTagRemarkingDefPCP.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosEgressTagRemarkingDefPCP.setStatus(_A)
class _Opmen99810bQosEgressTagRemarkingDefDEI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bQosEgressTagRemarkingDefDEI_Type.__name__=_C
_Opmen99810bQosEgressTagRemarkingDefDEI_Object=MibTableColumn
opmen99810bQosEgressTagRemarkingDefDEI=_Opmen99810bQosEgressTagRemarkingDefDEI_Object((1,3,6,1,4,1,5205,2,94,2,14,4,2,1,3),_Opmen99810bQosEgressTagRemarkingDefDEI_Type())
opmen99810bQosEgressTagRemarkingDefDEI.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosEgressTagRemarkingDefDEI.setStatus(_A)
_Opmen99810bQosPortEgressTagRemarkingMapTable_Object=MibTable
opmen99810bQosPortEgressTagRemarkingMapTable=_Opmen99810bQosPortEgressTagRemarkingMapTable_Object((1,3,6,1,4,1,5205,2,94,2,14,4,4))
if mibBuilder.loadTexts:opmen99810bQosPortEgressTagRemarkingMapTable.setStatus(_A)
_Opmen99810bQosPortEgressTagRemarkingMapEntry_Object=MibTableRow
opmen99810bQosPortEgressTagRemarkingMapEntry=_Opmen99810bQosPortEgressTagRemarkingMapEntry_Object((1,3,6,1,4,1,5205,2,94,2,14,4,4,1))
opmen99810bQosPortEgressTagRemarkingMapEntry.setIndexNames((0,_G,_AX),(0,_G,_AY),(0,_G,_AZ))
if mibBuilder.loadTexts:opmen99810bQosPortEgressTagRemarkingMapEntry.setStatus(_A)
class _Opmen99810bQosPortEgressTagRemarkingMapPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bQosPortEgressTagRemarkingMapPort_Type.__name__=_C
_Opmen99810bQosPortEgressTagRemarkingMapPort_Object=MibTableColumn
opmen99810bQosPortEgressTagRemarkingMapPort=_Opmen99810bQosPortEgressTagRemarkingMapPort_Object((1,3,6,1,4,1,5205,2,94,2,14,4,4,1,1),_Opmen99810bQosPortEgressTagRemarkingMapPort_Type())
opmen99810bQosPortEgressTagRemarkingMapPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosPortEgressTagRemarkingMapPort.setStatus(_A)
class _Opmen99810bQosTagRemarkingQoSClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('class0',1),('class1',2),('class2',3),('class3',4),('class4',5),('class5',6),('class6',7),('class7',8)))
_Opmen99810bQosTagRemarkingQoSClass_Type.__name__=_C
_Opmen99810bQosTagRemarkingQoSClass_Object=MibTableColumn
opmen99810bQosTagRemarkingQoSClass=_Opmen99810bQosTagRemarkingQoSClass_Object((1,3,6,1,4,1,5205,2,94,2,14,4,4,1,2),_Opmen99810bQosTagRemarkingQoSClass_Type())
opmen99810bQosTagRemarkingQoSClass.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosTagRemarkingQoSClass.setStatus(_A)
class _Opmen99810bQosTagRemarkingDPLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('level0',1),('level1',2)))
_Opmen99810bQosTagRemarkingDPLevel_Type.__name__=_C
_Opmen99810bQosTagRemarkingDPLevel_Object=MibTableColumn
opmen99810bQosTagRemarkingDPLevel=_Opmen99810bQosTagRemarkingDPLevel_Object((1,3,6,1,4,1,5205,2,94,2,14,4,4,1,3),_Opmen99810bQosTagRemarkingDPLevel_Type())
opmen99810bQosTagRemarkingDPLevel.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosTagRemarkingDPLevel.setStatus(_A)
class _Opmen99810bQosTagRemarkingPCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Opmen99810bQosTagRemarkingPCP_Type.__name__=_C
_Opmen99810bQosTagRemarkingPCP_Object=MibTableColumn
opmen99810bQosTagRemarkingPCP=_Opmen99810bQosTagRemarkingPCP_Object((1,3,6,1,4,1,5205,2,94,2,14,4,4,1,4),_Opmen99810bQosTagRemarkingPCP_Type())
opmen99810bQosTagRemarkingPCP.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosTagRemarkingPCP.setStatus(_A)
class _Opmen99810bQosTagRemarkingDEI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Opmen99810bQosTagRemarkingDEI_Type.__name__=_C
_Opmen99810bQosTagRemarkingDEI_Object=MibTableColumn
opmen99810bQosTagRemarkingDEI=_Opmen99810bQosTagRemarkingDEI_Object((1,3,6,1,4,1,5205,2,94,2,14,4,4,1,5),_Opmen99810bQosTagRemarkingDEI_Type())
opmen99810bQosTagRemarkingDEI.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosTagRemarkingDEI.setStatus(_A)
_Opmen99810bQosPortDSCPTable_Object=MibTable
opmen99810bQosPortDSCPTable=_Opmen99810bQosPortDSCPTable_Object((1,3,6,1,4,1,5205,2,94,2,14,5))
if mibBuilder.loadTexts:opmen99810bQosPortDSCPTable.setStatus(_A)
_Opmen99810bQosPortDSCPEntry_Object=MibTableRow
opmen99810bQosPortDSCPEntry=_Opmen99810bQosPortDSCPEntry_Object((1,3,6,1,4,1,5205,2,94,2,14,5,1))
opmen99810bQosPortDSCPEntry.setIndexNames((0,_G,_Aa))
if mibBuilder.loadTexts:opmen99810bQosPortDSCPEntry.setStatus(_A)
class _Opmen99810bQosPortDSCPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bQosPortDSCPPort_Type.__name__=_C
_Opmen99810bQosPortDSCPPort_Object=MibTableColumn
opmen99810bQosPortDSCPPort=_Opmen99810bQosPortDSCPPort_Object((1,3,6,1,4,1,5205,2,94,2,14,5,1,1),_Opmen99810bQosPortDSCPPort_Type())
opmen99810bQosPortDSCPPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosPortDSCPPort.setStatus(_A)
class _Opmen99810bQosPortDSCPIngressTranslate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bQosPortDSCPIngressTranslate_Type.__name__=_C
_Opmen99810bQosPortDSCPIngressTranslate_Object=MibTableColumn
opmen99810bQosPortDSCPIngressTranslate=_Opmen99810bQosPortDSCPIngressTranslate_Object((1,3,6,1,4,1,5205,2,94,2,14,5,1,2),_Opmen99810bQosPortDSCPIngressTranslate_Type())
opmen99810bQosPortDSCPIngressTranslate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosPortDSCPIngressTranslate.setStatus(_A)
class _Opmen99810bQosPortDSCPIngressClassify_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Opmen99810bQosPortDSCPIngressClassify_Type.__name__=_C
_Opmen99810bQosPortDSCPIngressClassify_Object=MibTableColumn
opmen99810bQosPortDSCPIngressClassify=_Opmen99810bQosPortDSCPIngressClassify_Object((1,3,6,1,4,1,5205,2,94,2,14,5,1,3),_Opmen99810bQosPortDSCPIngressClassify_Type())
opmen99810bQosPortDSCPIngressClassify.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosPortDSCPIngressClassify.setStatus(_A)
class _Opmen99810bQosPortDSCPEgressRewrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Opmen99810bQosPortDSCPEgressRewrite_Type.__name__=_C
_Opmen99810bQosPortDSCPEgressRewrite_Object=MibTableColumn
opmen99810bQosPortDSCPEgressRewrite=_Opmen99810bQosPortDSCPEgressRewrite_Object((1,3,6,1,4,1,5205,2,94,2,14,5,1,4),_Opmen99810bQosPortDSCPEgressRewrite_Type())
opmen99810bQosPortDSCPEgressRewrite.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosPortDSCPEgressRewrite.setStatus(_A)
_Opmen99810bQosDSCPTable_Object=MibTable
opmen99810bQosDSCPTable=_Opmen99810bQosDSCPTable_Object((1,3,6,1,4,1,5205,2,94,2,14,6))
if mibBuilder.loadTexts:opmen99810bQosDSCPTable.setStatus(_A)
_Opmen99810bQosDSCPEntry_Object=MibTableRow
opmen99810bQosDSCPEntry=_Opmen99810bQosDSCPEntry_Object((1,3,6,1,4,1,5205,2,94,2,14,6,1))
opmen99810bQosDSCPEntry.setIndexNames((0,_G,_Ab))
if mibBuilder.loadTexts:opmen99810bQosDSCPEntry.setStatus(_A)
class _Opmen99810bQosDSCPList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Opmen99810bQosDSCPList_Type.__name__=_C
_Opmen99810bQosDSCPList_Object=MibTableColumn
opmen99810bQosDSCPList=_Opmen99810bQosDSCPList_Object((1,3,6,1,4,1,5205,2,94,2,14,6,1,1),_Opmen99810bQosDSCPList_Type())
opmen99810bQosDSCPList.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosDSCPList.setStatus(_A)
_Opmen99810bQosDSCP_Type=DisplayString
_Opmen99810bQosDSCP_Object=MibTableColumn
opmen99810bQosDSCP=_Opmen99810bQosDSCP_Object((1,3,6,1,4,1,5205,2,94,2,14,6,1,2),_Opmen99810bQosDSCP_Type())
opmen99810bQosDSCP.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bQosDSCP.setStatus(_A)
class _Opmen99810bQosDSCPTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bQosDSCPTrust_Type.__name__=_C
_Opmen99810bQosDSCPTrust_Object=MibTableColumn
opmen99810bQosDSCPTrust=_Opmen99810bQosDSCPTrust_Object((1,3,6,1,4,1,5205,2,94,2,14,6,1,3),_Opmen99810bQosDSCPTrust_Type())
opmen99810bQosDSCPTrust.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosDSCPTrust.setStatus(_A)
class _Opmen99810bQosDSCPQosClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Opmen99810bQosDSCPQosClass_Type.__name__=_C
_Opmen99810bQosDSCPQosClass_Object=MibTableColumn
opmen99810bQosDSCPQosClass=_Opmen99810bQosDSCPQosClass_Object((1,3,6,1,4,1,5205,2,94,2,14,6,1,4),_Opmen99810bQosDSCPQosClass_Type())
opmen99810bQosDSCPQosClass.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosDSCPQosClass.setStatus(_A)
class _Opmen99810bQosDSCPDPL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Opmen99810bQosDSCPDPL_Type.__name__=_C
_Opmen99810bQosDSCPDPL_Object=MibTableColumn
opmen99810bQosDSCPDPL=_Opmen99810bQosDSCPDPL_Object((1,3,6,1,4,1,5205,2,94,2,14,6,1,5),_Opmen99810bQosDSCPDPL_Type())
opmen99810bQosDSCPDPL.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosDSCPDPL.setStatus(_A)
_Opmen99810bQosDSCPTranslationTable_Object=MibTable
opmen99810bQosDSCPTranslationTable=_Opmen99810bQosDSCPTranslationTable_Object((1,3,6,1,4,1,5205,2,94,2,14,7))
if mibBuilder.loadTexts:opmen99810bQosDSCPTranslationTable.setStatus(_A)
_Opmen99810bQosDSCPTranslationEntry_Object=MibTableRow
opmen99810bQosDSCPTranslationEntry=_Opmen99810bQosDSCPTranslationEntry_Object((1,3,6,1,4,1,5205,2,94,2,14,7,1))
opmen99810bQosDSCPTranslationEntry.setIndexNames((0,_G,_Ac))
if mibBuilder.loadTexts:opmen99810bQosDSCPTranslationEntry.setStatus(_A)
class _Opmen99810bQosDSCPTranslationList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Opmen99810bQosDSCPTranslationList_Type.__name__=_C
_Opmen99810bQosDSCPTranslationList_Object=MibTableColumn
opmen99810bQosDSCPTranslationList=_Opmen99810bQosDSCPTranslationList_Object((1,3,6,1,4,1,5205,2,94,2,14,7,1,1),_Opmen99810bQosDSCPTranslationList_Type())
opmen99810bQosDSCPTranslationList.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosDSCPTranslationList.setStatus(_A)
_Opmen99810bQosDSCPTranslationDSCPBasedId_Type=DisplayString
_Opmen99810bQosDSCPTranslationDSCPBasedId_Object=MibTableColumn
opmen99810bQosDSCPTranslationDSCPBasedId=_Opmen99810bQosDSCPTranslationDSCPBasedId_Object((1,3,6,1,4,1,5205,2,94,2,14,7,1,2),_Opmen99810bQosDSCPTranslationDSCPBasedId_Type())
opmen99810bQosDSCPTranslationDSCPBasedId.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosDSCPTranslationDSCPBasedId.setStatus(_A)
class _Opmen99810bQosDSCPTranslationIngressTranslate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_Opmen99810bQosDSCPTranslationIngressTranslate_Type.__name__=_C
_Opmen99810bQosDSCPTranslationIngressTranslate_Object=MibTableColumn
opmen99810bQosDSCPTranslationIngressTranslate=_Opmen99810bQosDSCPTranslationIngressTranslate_Object((1,3,6,1,4,1,5205,2,94,2,14,7,1,3),_Opmen99810bQosDSCPTranslationIngressTranslate_Type())
opmen99810bQosDSCPTranslationIngressTranslate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosDSCPTranslationIngressTranslate.setStatus(_A)
class _Opmen99810bQosDSCPTranslationIngressClassify_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bQosDSCPTranslationIngressClassify_Type.__name__=_C
_Opmen99810bQosDSCPTranslationIngressClassify_Object=MibTableColumn
opmen99810bQosDSCPTranslationIngressClassify=_Opmen99810bQosDSCPTranslationIngressClassify_Object((1,3,6,1,4,1,5205,2,94,2,14,7,1,4),_Opmen99810bQosDSCPTranslationIngressClassify_Type())
opmen99810bQosDSCPTranslationIngressClassify.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosDSCPTranslationIngressClassify.setStatus(_A)
class _Opmen99810bQosDSCPTranslationEgressRemapDP0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_Opmen99810bQosDSCPTranslationEgressRemapDP0_Type.__name__=_C
_Opmen99810bQosDSCPTranslationEgressRemapDP0_Object=MibTableColumn
opmen99810bQosDSCPTranslationEgressRemapDP0=_Opmen99810bQosDSCPTranslationEgressRemapDP0_Object((1,3,6,1,4,1,5205,2,94,2,14,7,1,5),_Opmen99810bQosDSCPTranslationEgressRemapDP0_Type())
opmen99810bQosDSCPTranslationEgressRemapDP0.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosDSCPTranslationEgressRemapDP0.setStatus(_A)
class _Opmen99810bQosDSCPTranslationEgressRemapDP1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_Opmen99810bQosDSCPTranslationEgressRemapDP1_Type.__name__=_C
_Opmen99810bQosDSCPTranslationEgressRemapDP1_Object=MibTableColumn
opmen99810bQosDSCPTranslationEgressRemapDP1=_Opmen99810bQosDSCPTranslationEgressRemapDP1_Object((1,3,6,1,4,1,5205,2,94,2,14,7,1,6),_Opmen99810bQosDSCPTranslationEgressRemapDP1_Type())
opmen99810bQosDSCPTranslationEgressRemapDP1.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosDSCPTranslationEgressRemapDP1.setStatus(_A)
_Opmen99810bQosDSCPClassificationTable_Object=MibTable
opmen99810bQosDSCPClassificationTable=_Opmen99810bQosDSCPClassificationTable_Object((1,3,6,1,4,1,5205,2,94,2,14,8))
if mibBuilder.loadTexts:opmen99810bQosDSCPClassificationTable.setStatus(_A)
_Opmen99810bQosDSCPClassificationEntry_Object=MibTableRow
opmen99810bQosDSCPClassificationEntry=_Opmen99810bQosDSCPClassificationEntry_Object((1,3,6,1,4,1,5205,2,94,2,14,8,1))
opmen99810bQosDSCPClassificationEntry.setIndexNames((0,_G,_Ad),(0,_G,_Ae))
if mibBuilder.loadTexts:opmen99810bQosDSCPClassificationEntry.setStatus(_A)
class _Opmen99810bQosDSCPClassificationQoSClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('class0',1),('class1',2),('class2',3),('class3',4),('class4',5),('class5',6),('class6',7),('class7',8)))
_Opmen99810bQosDSCPClassificationQoSClass_Type.__name__=_C
_Opmen99810bQosDSCPClassificationQoSClass_Object=MibTableColumn
opmen99810bQosDSCPClassificationQoSClass=_Opmen99810bQosDSCPClassificationQoSClass_Object((1,3,6,1,4,1,5205,2,94,2,14,8,1,1),_Opmen99810bQosDSCPClassificationQoSClass_Type())
opmen99810bQosDSCPClassificationQoSClass.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosDSCPClassificationQoSClass.setStatus(_A)
class _Opmen99810bQosDSCPClassificationDPL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_Opmen99810bQosDSCPClassificationDPL_Type.__name__=_C
_Opmen99810bQosDSCPClassificationDPL_Object=MibTableColumn
opmen99810bQosDSCPClassificationDPL=_Opmen99810bQosDSCPClassificationDPL_Object((1,3,6,1,4,1,5205,2,94,2,14,8,1,2),_Opmen99810bQosDSCPClassificationDPL_Type())
opmen99810bQosDSCPClassificationDPL.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosDSCPClassificationDPL.setStatus(_A)
class _Opmen99810bQosDSCPClassificationDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_Opmen99810bQosDSCPClassificationDSCP_Type.__name__=_C
_Opmen99810bQosDSCPClassificationDSCP_Object=MibTableColumn
opmen99810bQosDSCPClassificationDSCP=_Opmen99810bQosDSCPClassificationDSCP_Object((1,3,6,1,4,1,5205,2,94,2,14,8,1,3),_Opmen99810bQosDSCPClassificationDSCP_Type())
opmen99810bQosDSCPClassificationDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosDSCPClassificationDSCP.setStatus(_A)
_Opmen99810bQosControlList_ObjectIdentity=ObjectIdentity
opmen99810bQosControlList=_Opmen99810bQosControlList_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,14,9))
class _Opmen99810bQosQceCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_W,1)))
_Opmen99810bQosQceCreate_Type.__name__=_C
_Opmen99810bQosQceCreate_Object=MibScalar
opmen99810bQosQceCreate=_Opmen99810bQosQceCreate_Object((1,3,6,1,4,1,5205,2,94,2,14,9,1),_Opmen99810bQosQceCreate_Type())
opmen99810bQosQceCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosQceCreate.setStatus(_A)
_Opmen99810bQosQceTable_Object=MibTable
opmen99810bQosQceTable=_Opmen99810bQosQceTable_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2))
if mibBuilder.loadTexts:opmen99810bQosQceTable.setStatus(_A)
_Opmen99810bQosQceEntry_Object=MibTableRow
opmen99810bQosQceEntry=_Opmen99810bQosQceEntry_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1))
opmen99810bQosQceEntry.setIndexNames((0,_G,_Af))
if mibBuilder.loadTexts:opmen99810bQosQceEntry.setStatus(_A)
class _Opmen99810bQosQceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Opmen99810bQosQceIndex_Type.__name__=_C
_Opmen99810bQosQceIndex_Object=MibTableColumn
opmen99810bQosQceIndex=_Opmen99810bQosQceIndex_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,1),_Opmen99810bQosQceIndex_Type())
opmen99810bQosQceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosQceIndex.setStatus(_A)
class _Opmen99810bQosQceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Opmen99810bQosQceID_Type.__name__=_C
_Opmen99810bQosQceID_Object=MibTableColumn
opmen99810bQosQceID=_Opmen99810bQosQceID_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,2),_Opmen99810bQosQceID_Type())
opmen99810bQosQceID.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosQceID.setStatus(_A)
class _Opmen99810bQosQceNextID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Opmen99810bQosQceNextID_Type.__name__=_C
_Opmen99810bQosQceNextID_Object=MibTableColumn
opmen99810bQosQceNextID=_Opmen99810bQosQceNextID_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,3),_Opmen99810bQosQceNextID_Type())
opmen99810bQosQceNextID.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosQceNextID.setStatus(_A)
_Opmen99810bQosQcePortMembers_Type=DisplayString
_Opmen99810bQosQcePortMembers_Object=MibTableColumn
opmen99810bQosQcePortMembers=_Opmen99810bQosQcePortMembers_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,4),_Opmen99810bQosQcePortMembers_Type())
opmen99810bQosQcePortMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosQcePortMembers.setStatus(_A)
_Opmen99810bQosQceTag_Type=DisplayString
_Opmen99810bQosQceTag_Object=MibTableColumn
opmen99810bQosQceTag=_Opmen99810bQosQceTag_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,5),_Opmen99810bQosQceTag_Type())
opmen99810bQosQceTag.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosQceTag.setStatus(_A)
_Opmen99810bQosQceVID_Type=DisplayString
_Opmen99810bQosQceVID_Object=MibTableColumn
opmen99810bQosQceVID=_Opmen99810bQosQceVID_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,6),_Opmen99810bQosQceVID_Type())
opmen99810bQosQceVID.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosQceVID.setStatus(_A)
_Opmen99810bQosPCP_Type=DisplayString
_Opmen99810bQosPCP_Object=MibTableColumn
opmen99810bQosPCP=_Opmen99810bQosPCP_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,7),_Opmen99810bQosPCP_Type())
opmen99810bQosPCP.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosPCP.setStatus(_A)
_Opmen99810bQosDEI_Type=DisplayString
_Opmen99810bQosDEI_Object=MibTableColumn
opmen99810bQosDEI=_Opmen99810bQosDEI_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,8),_Opmen99810bQosDEI_Type())
opmen99810bQosDEI.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosDEI.setStatus(_A)
_Opmen99810bQosSMAC_Type=DisplayString
_Opmen99810bQosSMAC_Object=MibTableColumn
opmen99810bQosSMAC=_Opmen99810bQosSMAC_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,9),_Opmen99810bQosSMAC_Type())
opmen99810bQosSMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosSMAC.setStatus(_A)
_Opmen99810bQosDMACType_Type=DisplayString
_Opmen99810bQosDMACType_Object=MibTableColumn
opmen99810bQosDMACType=_Opmen99810bQosDMACType_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,10),_Opmen99810bQosDMACType_Type())
opmen99810bQosDMACType.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosDMACType.setStatus(_A)
class _Opmen99810bQosFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_R,1),('ethernet',2),('llc',3),('snap',4),(_d,5),(_j,6)))
_Opmen99810bQosFrameType_Type.__name__=_C
_Opmen99810bQosFrameType_Object=MibTableColumn
opmen99810bQosFrameType=_Opmen99810bQosFrameType_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,11),_Opmen99810bQosFrameType_Type())
opmen99810bQosFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosFrameType.setStatus(_A)
_Opmen99810bQosMacEtherType_Type=DisplayString
_Opmen99810bQosMacEtherType_Object=MibTableColumn
opmen99810bQosMacEtherType=_Opmen99810bQosMacEtherType_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,12),_Opmen99810bQosMacEtherType_Type())
opmen99810bQosMacEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosMacEtherType.setStatus(_A)
_Opmen99810bQosLLCSSAPAddr_Type=DisplayString
_Opmen99810bQosLLCSSAPAddr_Object=MibTableColumn
opmen99810bQosLLCSSAPAddr=_Opmen99810bQosLLCSSAPAddr_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,13),_Opmen99810bQosLLCSSAPAddr_Type())
opmen99810bQosLLCSSAPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosLLCSSAPAddr.setStatus(_A)
_Opmen99810bQosLLCDSAPAddr_Type=DisplayString
_Opmen99810bQosLLCDSAPAddr_Object=MibTableColumn
opmen99810bQosLLCDSAPAddr=_Opmen99810bQosLLCDSAPAddr_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,14),_Opmen99810bQosLLCDSAPAddr_Type())
opmen99810bQosLLCDSAPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosLLCDSAPAddr.setStatus(_A)
_Opmen99810bQosLLCControl_Type=DisplayString
_Opmen99810bQosLLCControl_Object=MibTableColumn
opmen99810bQosLLCControl=_Opmen99810bQosLLCControl_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,15),_Opmen99810bQosLLCControl_Type())
opmen99810bQosLLCControl.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosLLCControl.setStatus(_A)
_Opmen99810bQosSNAPPID_Type=DisplayString
_Opmen99810bQosSNAPPID_Object=MibTableColumn
opmen99810bQosSNAPPID=_Opmen99810bQosSNAPPID_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,16),_Opmen99810bQosSNAPPID_Type())
opmen99810bQosSNAPPID.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosSNAPPID.setStatus(_A)
_Opmen99810bQosIpv4Protocol_Type=DisplayString
_Opmen99810bQosIpv4Protocol_Object=MibTableColumn
opmen99810bQosIpv4Protocol=_Opmen99810bQosIpv4Protocol_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,17),_Opmen99810bQosIpv4Protocol_Type())
opmen99810bQosIpv4Protocol.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv4Protocol.setStatus(_A)
class _Opmen99810bQosIpv4ProtocolValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Opmen99810bQosIpv4ProtocolValue_Type.__name__=_C
_Opmen99810bQosIpv4ProtocolValue_Object=MibTableColumn
opmen99810bQosIpv4ProtocolValue=_Opmen99810bQosIpv4ProtocolValue_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,18),_Opmen99810bQosIpv4ProtocolValue_Type())
opmen99810bQosIpv4ProtocolValue.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv4ProtocolValue.setStatus(_A)
_Opmen99810bQosIpv4ProtocolUDPSport_Type=DisplayString
_Opmen99810bQosIpv4ProtocolUDPSport_Object=MibTableColumn
opmen99810bQosIpv4ProtocolUDPSport=_Opmen99810bQosIpv4ProtocolUDPSport_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,19),_Opmen99810bQosIpv4ProtocolUDPSport_Type())
opmen99810bQosIpv4ProtocolUDPSport.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv4ProtocolUDPSport.setStatus(_A)
_Opmen99810bQosIpv4ProtocolUDPDport_Type=DisplayString
_Opmen99810bQosIpv4ProtocolUDPDport_Object=MibTableColumn
opmen99810bQosIpv4ProtocolUDPDport=_Opmen99810bQosIpv4ProtocolUDPDport_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,20),_Opmen99810bQosIpv4ProtocolUDPDport_Type())
opmen99810bQosIpv4ProtocolUDPDport.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv4ProtocolUDPDport.setStatus(_A)
_Opmen99810bQosIpv4ProtocolTCPSport_Type=DisplayString
_Opmen99810bQosIpv4ProtocolTCPSport_Object=MibTableColumn
opmen99810bQosIpv4ProtocolTCPSport=_Opmen99810bQosIpv4ProtocolTCPSport_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,21),_Opmen99810bQosIpv4ProtocolTCPSport_Type())
opmen99810bQosIpv4ProtocolTCPSport.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv4ProtocolTCPSport.setStatus(_A)
_Opmen99810bQosIpv4ProtocolTCPDport_Type=DisplayString
_Opmen99810bQosIpv4ProtocolTCPDport_Object=MibTableColumn
opmen99810bQosIpv4ProtocolTCPDport=_Opmen99810bQosIpv4ProtocolTCPDport_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,22),_Opmen99810bQosIpv4ProtocolTCPDport_Type())
opmen99810bQosIpv4ProtocolTCPDport.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv4ProtocolTCPDport.setStatus(_A)
_Opmen99810bQosIpv4SourceIp_Type=DisplayString
_Opmen99810bQosIpv4SourceIp_Object=MibTableColumn
opmen99810bQosIpv4SourceIp=_Opmen99810bQosIpv4SourceIp_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,23),_Opmen99810bQosIpv4SourceIp_Type())
opmen99810bQosIpv4SourceIp.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv4SourceIp.setStatus(_A)
_Opmen99810bQosIpv4SourceMask_Type=DisplayString
_Opmen99810bQosIpv4SourceMask_Object=MibTableColumn
opmen99810bQosIpv4SourceMask=_Opmen99810bQosIpv4SourceMask_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,24),_Opmen99810bQosIpv4SourceMask_Type())
opmen99810bQosIpv4SourceMask.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv4SourceMask.setStatus(_A)
class _Opmen99810bQosIpv4IPFragment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),('no',1),(_g,2)))
_Opmen99810bQosIpv4IPFragment_Type.__name__=_C
_Opmen99810bQosIpv4IPFragment_Object=MibTableColumn
opmen99810bQosIpv4IPFragment=_Opmen99810bQosIpv4IPFragment_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,25),_Opmen99810bQosIpv4IPFragment_Type())
opmen99810bQosIpv4IPFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv4IPFragment.setStatus(_A)
_Opmen99810bQosIpv4DSCP_Type=DisplayString
_Opmen99810bQosIpv4DSCP_Object=MibTableColumn
opmen99810bQosIpv4DSCP=_Opmen99810bQosIpv4DSCP_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,26),_Opmen99810bQosIpv4DSCP_Type())
opmen99810bQosIpv4DSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv4DSCP.setStatus(_A)
_Opmen99810bQosIpv6Protocol_Type=DisplayString
_Opmen99810bQosIpv6Protocol_Object=MibTableColumn
opmen99810bQosIpv6Protocol=_Opmen99810bQosIpv6Protocol_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,27),_Opmen99810bQosIpv6Protocol_Type())
opmen99810bQosIpv6Protocol.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv6Protocol.setStatus(_A)
class _Opmen99810bQosIpv6ProtocolValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Opmen99810bQosIpv6ProtocolValue_Type.__name__=_C
_Opmen99810bQosIpv6ProtocolValue_Object=MibTableColumn
opmen99810bQosIpv6ProtocolValue=_Opmen99810bQosIpv6ProtocolValue_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,28),_Opmen99810bQosIpv6ProtocolValue_Type())
opmen99810bQosIpv6ProtocolValue.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv6ProtocolValue.setStatus(_A)
_Opmen99810bQosIpv6ProtocolUDPSport_Type=DisplayString
_Opmen99810bQosIpv6ProtocolUDPSport_Object=MibTableColumn
opmen99810bQosIpv6ProtocolUDPSport=_Opmen99810bQosIpv6ProtocolUDPSport_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,29),_Opmen99810bQosIpv6ProtocolUDPSport_Type())
opmen99810bQosIpv6ProtocolUDPSport.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv6ProtocolUDPSport.setStatus(_A)
_Opmen99810bQosIpv6ProtocolUDPDport_Type=DisplayString
_Opmen99810bQosIpv6ProtocolUDPDport_Object=MibTableColumn
opmen99810bQosIpv6ProtocolUDPDport=_Opmen99810bQosIpv6ProtocolUDPDport_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,30),_Opmen99810bQosIpv6ProtocolUDPDport_Type())
opmen99810bQosIpv6ProtocolUDPDport.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv6ProtocolUDPDport.setStatus(_A)
_Opmen99810bQosIpv6ProtocolTCPSport_Type=DisplayString
_Opmen99810bQosIpv6ProtocolTCPSport_Object=MibTableColumn
opmen99810bQosIpv6ProtocolTCPSport=_Opmen99810bQosIpv6ProtocolTCPSport_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,31),_Opmen99810bQosIpv6ProtocolTCPSport_Type())
opmen99810bQosIpv6ProtocolTCPSport.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv6ProtocolTCPSport.setStatus(_A)
_Opmen99810bQosIpv6ProtocolTCPDport_Type=DisplayString
_Opmen99810bQosIpv6ProtocolTCPDport_Object=MibTableColumn
opmen99810bQosIpv6ProtocolTCPDport=_Opmen99810bQosIpv6ProtocolTCPDport_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,32),_Opmen99810bQosIpv6ProtocolTCPDport_Type())
opmen99810bQosIpv6ProtocolTCPDport.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv6ProtocolTCPDport.setStatus(_A)
_Opmen99810bQosIpv6SourceIp_Type=DisplayString
_Opmen99810bQosIpv6SourceIp_Object=MibTableColumn
opmen99810bQosIpv6SourceIp=_Opmen99810bQosIpv6SourceIp_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,33),_Opmen99810bQosIpv6SourceIp_Type())
opmen99810bQosIpv6SourceIp.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv6SourceIp.setStatus(_A)
_Opmen99810bQosIpv6SourceMask_Type=DisplayString
_Opmen99810bQosIpv6SourceMask_Object=MibTableColumn
opmen99810bQosIpv6SourceMask=_Opmen99810bQosIpv6SourceMask_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,34),_Opmen99810bQosIpv6SourceMask_Type())
opmen99810bQosIpv6SourceMask.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv6SourceMask.setStatus(_A)
_Opmen99810bQosIpv6DSCP_Type=DisplayString
_Opmen99810bQosIpv6DSCP_Object=MibTableColumn
opmen99810bQosIpv6DSCP=_Opmen99810bQosIpv6DSCP_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,35),_Opmen99810bQosIpv6DSCP_Type())
opmen99810bQosIpv6DSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosIpv6DSCP.setStatus(_A)
class _Opmen99810bQosActionClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_Opmen99810bQosActionClass_Type.__name__=_C
_Opmen99810bQosActionClass_Object=MibTableColumn
opmen99810bQosActionClass=_Opmen99810bQosActionClass_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,36),_Opmen99810bQosActionClass_Type())
opmen99810bQosActionClass.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosActionClass.setStatus(_A)
class _Opmen99810bQosActionDPL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Opmen99810bQosActionDPL_Type.__name__=_C
_Opmen99810bQosActionDPL_Object=MibTableColumn
opmen99810bQosActionDPL=_Opmen99810bQosActionDPL_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,37),_Opmen99810bQosActionDPL_Type())
opmen99810bQosActionDPL.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosActionDPL.setStatus(_A)
class _Opmen99810bQosActionDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_Opmen99810bQosActionDSCP_Type.__name__=_C
_Opmen99810bQosActionDSCP_Object=MibTableColumn
opmen99810bQosActionDSCP=_Opmen99810bQosActionDSCP_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,38),_Opmen99810bQosActionDSCP_Type())
opmen99810bQosActionDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosActionDSCP.setStatus(_A)
class _Opmen99810bQosQceRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*((_U,1),(_X,2),(_Y,4)))
_Opmen99810bQosQceRowStatus_Type.__name__=_C
_Opmen99810bQosQceRowStatus_Object=MibTableColumn
opmen99810bQosQceRowStatus=_Opmen99810bQosQceRowStatus_Object((1,3,6,1,4,1,5205,2,94,2,14,9,2,1,39),_Opmen99810bQosQceRowStatus_Type())
opmen99810bQosQceRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosQceRowStatus.setStatus(_A)
class _Opmen99810bQosQceMoveID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Opmen99810bQosQceMoveID_Type.__name__=_C
_Opmen99810bQosQceMoveID_Object=MibScalar
opmen99810bQosQceMoveID=_Opmen99810bQosQceMoveID_Object((1,3,6,1,4,1,5205,2,94,2,14,9,3),_Opmen99810bQosQceMoveID_Type())
opmen99810bQosQceMoveID.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosQceMoveID.setStatus(_A)
class _Opmen99810bQosQceMoveNextID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_Opmen99810bQosQceMoveNextID_Type.__name__=_C
_Opmen99810bQosQceMoveNextID_Object=MibScalar
opmen99810bQosQceMoveNextID=_Opmen99810bQosQceMoveNextID_Object((1,3,6,1,4,1,5205,2,94,2,14,9,4),_Opmen99810bQosQceMoveNextID_Type())
opmen99810bQosQceMoveNextID.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQosQceMoveNextID.setStatus(_A)
_Opmen99810bQosQCLStatusTable_Object=MibTable
opmen99810bQosQCLStatusTable=_Opmen99810bQosQCLStatusTable_Object((1,3,6,1,4,1,5205,2,94,2,14,10))
if mibBuilder.loadTexts:opmen99810bQosQCLStatusTable.setStatus(_A)
_Opmen99810bQosQCLStatusEntry_Object=MibTableRow
opmen99810bQosQCLStatusEntry=_Opmen99810bQosQCLStatusEntry_Object((1,3,6,1,4,1,5205,2,94,2,14,10,1))
opmen99810bQosQCLStatusEntry.setIndexNames((0,_G,_Ag))
if mibBuilder.loadTexts:opmen99810bQosQCLStatusEntry.setStatus(_A)
class _Opmen99810bQosQCLStatusList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bQosQCLStatusList_Type.__name__=_C
_Opmen99810bQosQCLStatusList_Object=MibTableColumn
opmen99810bQosQCLStatusList=_Opmen99810bQosQCLStatusList_Object((1,3,6,1,4,1,5205,2,94,2,14,10,1,1),_Opmen99810bQosQCLStatusList_Type())
opmen99810bQosQCLStatusList.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bQosQCLStatusList.setStatus(_A)
_Opmen99810bQosQCLStatusUser_Type=DisplayString
_Opmen99810bQosQCLStatusUser_Object=MibTableColumn
opmen99810bQosQCLStatusUser=_Opmen99810bQosQCLStatusUser_Object((1,3,6,1,4,1,5205,2,94,2,14,10,1,2),_Opmen99810bQosQCLStatusUser_Type())
opmen99810bQosQCLStatusUser.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bQosQCLStatusUser.setStatus(_A)
_Opmen99810bQosQCLStatusQCEId_Type=DisplayString
_Opmen99810bQosQCLStatusQCEId_Object=MibTableColumn
opmen99810bQosQCLStatusQCEId=_Opmen99810bQosQCLStatusQCEId_Object((1,3,6,1,4,1,5205,2,94,2,14,10,1,3),_Opmen99810bQosQCLStatusQCEId_Type())
opmen99810bQosQCLStatusQCEId.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bQosQCLStatusQCEId.setStatus(_A)
_Opmen99810bQosQCLStatusFrameType_Type=DisplayString
_Opmen99810bQosQCLStatusFrameType_Object=MibTableColumn
opmen99810bQosQCLStatusFrameType=_Opmen99810bQosQCLStatusFrameType_Object((1,3,6,1,4,1,5205,2,94,2,14,10,1,4),_Opmen99810bQosQCLStatusFrameType_Type())
opmen99810bQosQCLStatusFrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bQosQCLStatusFrameType.setStatus(_A)
_Opmen99810bQosQCLStatusPortlist_Type=DisplayString
_Opmen99810bQosQCLStatusPortlist_Object=MibTableColumn
opmen99810bQosQCLStatusPortlist=_Opmen99810bQosQCLStatusPortlist_Object((1,3,6,1,4,1,5205,2,94,2,14,10,1,5),_Opmen99810bQosQCLStatusPortlist_Type())
opmen99810bQosQCLStatusPortlist.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bQosQCLStatusPortlist.setStatus(_A)
_Opmen99810bQosQCLStatusActionClass_Type=DisplayString
_Opmen99810bQosQCLStatusActionClass_Object=MibTableColumn
opmen99810bQosQCLStatusActionClass=_Opmen99810bQosQCLStatusActionClass_Object((1,3,6,1,4,1,5205,2,94,2,14,10,1,6),_Opmen99810bQosQCLStatusActionClass_Type())
opmen99810bQosQCLStatusActionClass.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bQosQCLStatusActionClass.setStatus(_A)
_Opmen99810bQosQCLStatusActionDPL_Type=DisplayString
_Opmen99810bQosQCLStatusActionDPL_Object=MibTableColumn
opmen99810bQosQCLStatusActionDPL=_Opmen99810bQosQCLStatusActionDPL_Object((1,3,6,1,4,1,5205,2,94,2,14,10,1,7),_Opmen99810bQosQCLStatusActionDPL_Type())
opmen99810bQosQCLStatusActionDPL.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bQosQCLStatusActionDPL.setStatus(_A)
_Opmen99810bQosQCLStatusActionDSCP_Type=DisplayString
_Opmen99810bQosQCLStatusActionDSCP_Object=MibTableColumn
opmen99810bQosQCLStatusActionDSCP=_Opmen99810bQosQCLStatusActionDSCP_Object((1,3,6,1,4,1,5205,2,94,2,14,10,1,8),_Opmen99810bQosQCLStatusActionDSCP_Type())
opmen99810bQosQCLStatusActionDSCP.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bQosQCLStatusActionDSCP.setStatus(_A)
_Opmen99810bQosQCLStatusActionConflict_Type=DisplayString
_Opmen99810bQosQCLStatusActionConflict_Object=MibTableColumn
opmen99810bQosQCLStatusActionConflict=_Opmen99810bQosQCLStatusActionConflict_Object((1,3,6,1,4,1,5205,2,94,2,14,10,1,9),_Opmen99810bQosQCLStatusActionConflict_Type())
opmen99810bQosQCLStatusActionConflict.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bQosQCLStatusActionConflict.setStatus(_A)
_Opmen99810bQosStormControl_ObjectIdentity=ObjectIdentity
opmen99810bQosStormControl=_Opmen99810bQosStormControl_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,14,11))
class _Opmen99810bQoSStormControlUC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bQoSStormControlUC_Type.__name__=_C
_Opmen99810bQoSStormControlUC_Object=MibScalar
opmen99810bQoSStormControlUC=_Opmen99810bQoSStormControlUC_Object((1,3,6,1,4,1,5205,2,94,2,14,11,2),_Opmen99810bQoSStormControlUC_Type())
opmen99810bQoSStormControlUC.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQoSStormControlUC.setStatus(_A)
_Opmen99810bQoSStormControlUCRate_Type=DisplayString
_Opmen99810bQoSStormControlUCRate_Object=MibScalar
opmen99810bQoSStormControlUCRate=_Opmen99810bQoSStormControlUCRate_Object((1,3,6,1,4,1,5205,2,94,2,14,11,3),_Opmen99810bQoSStormControlUCRate_Type())
opmen99810bQoSStormControlUCRate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQoSStormControlUCRate.setStatus(_A)
class _Opmen99810bQoSStormControlMC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bQoSStormControlMC_Type.__name__=_C
_Opmen99810bQoSStormControlMC_Object=MibScalar
opmen99810bQoSStormControlMC=_Opmen99810bQoSStormControlMC_Object((1,3,6,1,4,1,5205,2,94,2,14,11,4),_Opmen99810bQoSStormControlMC_Type())
opmen99810bQoSStormControlMC.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQoSStormControlMC.setStatus(_A)
_Opmen99810bQoSStormControlMCRate_Type=DisplayString
_Opmen99810bQoSStormControlMCRate_Object=MibScalar
opmen99810bQoSStormControlMCRate=_Opmen99810bQoSStormControlMCRate_Object((1,3,6,1,4,1,5205,2,94,2,14,11,5),_Opmen99810bQoSStormControlMCRate_Type())
opmen99810bQoSStormControlMCRate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQoSStormControlMCRate.setStatus(_A)
class _Opmen99810bQoSStormControlBC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bQoSStormControlBC_Type.__name__=_C
_Opmen99810bQoSStormControlBC_Object=MibScalar
opmen99810bQoSStormControlBC=_Opmen99810bQoSStormControlBC_Object((1,3,6,1,4,1,5205,2,94,2,14,11,6),_Opmen99810bQoSStormControlBC_Type())
opmen99810bQoSStormControlBC.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQoSStormControlBC.setStatus(_A)
_Opmen99810bQoSStormControlBCRate_Type=DisplayString
_Opmen99810bQoSStormControlBCRate_Object=MibScalar
opmen99810bQoSStormControlBCRate=_Opmen99810bQoSStormControlBCRate_Object((1,3,6,1,4,1,5205,2,94,2,14,11,7),_Opmen99810bQoSStormControlBCRate_Type())
opmen99810bQoSStormControlBCRate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bQoSStormControlBCRate.setStatus(_A)
_Opmen99810bVlan_ObjectIdentity=ObjectIdentity
opmen99810bVlan=_Opmen99810bVlan_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,15))
_Opmen99810bVlanPorts_ObjectIdentity=ObjectIdentity
opmen99810bVlanPorts=_Opmen99810bVlanPorts_ObjectIdentity((1,3,6,1,4,1,5205,2,94,2,15,1))
class _Opmen99810bVlanPortsTPIDforCustomSport_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_Opmen99810bVlanPortsTPIDforCustomSport_Type.__name__=_n
_Opmen99810bVlanPortsTPIDforCustomSport_Object=MibScalar
opmen99810bVlanPortsTPIDforCustomSport=_Opmen99810bVlanPortsTPIDforCustomSport_Object((1,3,6,1,4,1,5205,2,94,2,15,1,1),_Opmen99810bVlanPortsTPIDforCustomSport_Type())
opmen99810bVlanPortsTPIDforCustomSport.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVlanPortsTPIDforCustomSport.setStatus(_A)
_Opmen99810bVlanPortsTable_Object=MibTable
opmen99810bVlanPortsTable=_Opmen99810bVlanPortsTable_Object((1,3,6,1,4,1,5205,2,94,2,15,1,2))
if mibBuilder.loadTexts:opmen99810bVlanPortsTable.setStatus(_A)
_Opmen99810bVlanPortsEntry_Object=MibTableRow
opmen99810bVlanPortsEntry=_Opmen99810bVlanPortsEntry_Object((1,3,6,1,4,1,5205,2,94,2,15,1,2,1))
opmen99810bVlanPortsEntry.setIndexNames((0,_G,_Ah))
if mibBuilder.loadTexts:opmen99810bVlanPortsEntry.setStatus(_A)
class _Opmen99810bVlanPortsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Opmen99810bVlanPortsPort_Type.__name__=_C
_Opmen99810bVlanPortsPort_Object=MibTableColumn
opmen99810bVlanPortsPort=_Opmen99810bVlanPortsPort_Object((1,3,6,1,4,1,5205,2,94,2,15,1,2,1,1),_Opmen99810bVlanPortsPort_Type())
opmen99810bVlanPortsPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bVlanPortsPort.setStatus(_A)
class _Opmen99810bVlanPortsPVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Opmen99810bVlanPortsPVID_Type.__name__=_C
_Opmen99810bVlanPortsPVID_Object=MibTableColumn
opmen99810bVlanPortsPVID=_Opmen99810bVlanPortsPVID_Object((1,3,6,1,4,1,5205,2,94,2,15,1,2,1,2),_Opmen99810bVlanPortsPVID_Type())
opmen99810bVlanPortsPVID.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVlanPortsPVID.setStatus(_A)
class _Opmen99810bVlanPortsFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('all',0),('tagged',1),('untagged',2)))
_Opmen99810bVlanPortsFrameType_Type.__name__=_C
_Opmen99810bVlanPortsFrameType_Object=MibTableColumn
opmen99810bVlanPortsFrameType=_Opmen99810bVlanPortsFrameType_Object((1,3,6,1,4,1,5205,2,94,2,15,1,2,1,3),_Opmen99810bVlanPortsFrameType_Type())
opmen99810bVlanPortsFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVlanPortsFrameType.setStatus(_A)
class _Opmen99810bVlanPortsIngressFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bVlanPortsIngressFilter_Type.__name__=_C
_Opmen99810bVlanPortsIngressFilter_Object=MibTableColumn
opmen99810bVlanPortsIngressFilter=_Opmen99810bVlanPortsIngressFilter_Object((1,3,6,1,4,1,5205,2,94,2,15,1,2,1,4),_Opmen99810bVlanPortsIngressFilter_Type())
opmen99810bVlanPortsIngressFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVlanPortsIngressFilter.setStatus(_A)
class _Opmen99810bVlanPortsEgressRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('access',0),('hybrid',1),('trunk',2)))
_Opmen99810bVlanPortsEgressRule_Type.__name__=_C
_Opmen99810bVlanPortsEgressRule_Object=MibTableColumn
opmen99810bVlanPortsEgressRule=_Opmen99810bVlanPortsEgressRule_Object((1,3,6,1,4,1,5205,2,94,2,15,1,2,1,5),_Opmen99810bVlanPortsEgressRule_Type())
opmen99810bVlanPortsEgressRule.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVlanPortsEgressRule.setStatus(_A)
class _Opmen99810bVlanPortsPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('cPort',0),('sCustomPort',1),('sPort',2),('unaware',3)))
_Opmen99810bVlanPortsPortType_Type.__name__=_C
_Opmen99810bVlanPortsPortType_Object=MibTableColumn
opmen99810bVlanPortsPortType=_Opmen99810bVlanPortsPortType_Object((1,3,6,1,4,1,5205,2,94,2,15,1,2,1,6),_Opmen99810bVlanPortsPortType_Type())
opmen99810bVlanPortsPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bVlanPortsPortType.setStatus(_A)
_Opmen99810bSecurity_ObjectIdentity=ObjectIdentity
opmen99810bSecurity=_Opmen99810bSecurity_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3))
_Opmen99810bIPSourceGuard_ObjectIdentity=ObjectIdentity
opmen99810bIPSourceGuard=_Opmen99810bIPSourceGuard_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,1))
_Opmen99810bIPSourceGuardConf_ObjectIdentity=ObjectIdentity
opmen99810bIPSourceGuardConf=_Opmen99810bIPSourceGuardConf_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,1,1))
class _Opmen99810bIPSourceGuardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bIPSourceGuardMode_Type.__name__=_C
_Opmen99810bIPSourceGuardMode_Object=MibScalar
opmen99810bIPSourceGuardMode=_Opmen99810bIPSourceGuardMode_Object((1,3,6,1,4,1,5205,2,94,3,1,1,1),_Opmen99810bIPSourceGuardMode_Type())
opmen99810bIPSourceGuardMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardMode.setStatus(_A)
_Opmen99810bIPSourceGuardPortConfigTable_Object=MibTable
opmen99810bIPSourceGuardPortConfigTable=_Opmen99810bIPSourceGuardPortConfigTable_Object((1,3,6,1,4,1,5205,2,94,3,1,1,2))
if mibBuilder.loadTexts:opmen99810bIPSourceGuardPortConfigTable.setStatus(_A)
_Opmen99810bIPSourceGuardPortConfigEntry_Object=MibTableRow
opmen99810bIPSourceGuardPortConfigEntry=_Opmen99810bIPSourceGuardPortConfigEntry_Object((1,3,6,1,4,1,5205,2,94,3,1,1,2,1))
opmen99810bIPSourceGuardPortConfigEntry.setIndexNames((0,_G,_Ai))
if mibBuilder.loadTexts:opmen99810bIPSourceGuardPortConfigEntry.setStatus(_A)
class _Opmen99810bIPSourceGuardPortConfigPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bIPSourceGuardPortConfigPort_Type.__name__=_C
_Opmen99810bIPSourceGuardPortConfigPort_Object=MibTableColumn
opmen99810bIPSourceGuardPortConfigPort=_Opmen99810bIPSourceGuardPortConfigPort_Object((1,3,6,1,4,1,5205,2,94,3,1,1,2,1,1),_Opmen99810bIPSourceGuardPortConfigPort_Type())
opmen99810bIPSourceGuardPortConfigPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardPortConfigPort.setStatus(_A)
class _Opmen99810bIPSourceGuardPortConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bIPSourceGuardPortConfigMode_Type.__name__=_C
_Opmen99810bIPSourceGuardPortConfigMode_Object=MibTableColumn
opmen99810bIPSourceGuardPortConfigMode=_Opmen99810bIPSourceGuardPortConfigMode_Object((1,3,6,1,4,1,5205,2,94,3,1,1,2,1,2),_Opmen99810bIPSourceGuardPortConfigMode_Type())
opmen99810bIPSourceGuardPortConfigMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardPortConfigMode.setStatus(_A)
class _Opmen99810bIPSourceGuardPortMaxDynamicClients_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2),ValueRangeConstraint(99,99))
_Opmen99810bIPSourceGuardPortMaxDynamicClients_Type.__name__=_C
_Opmen99810bIPSourceGuardPortMaxDynamicClients_Object=MibTableColumn
opmen99810bIPSourceGuardPortMaxDynamicClients=_Opmen99810bIPSourceGuardPortMaxDynamicClients_Object((1,3,6,1,4,1,5205,2,94,3,1,1,2,1,3),_Opmen99810bIPSourceGuardPortMaxDynamicClients_Type())
opmen99810bIPSourceGuardPortMaxDynamicClients.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardPortMaxDynamicClients.setStatus(_A)
_Opmen99810bIPSourceGuardStatic_ObjectIdentity=ObjectIdentity
opmen99810bIPSourceGuardStatic=_Opmen99810bIPSourceGuardStatic_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,1,2))
class _Opmen99810bIPSourceGuardStaticCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_W,1)))
_Opmen99810bIPSourceGuardStaticCreate_Type.__name__=_C
_Opmen99810bIPSourceGuardStaticCreate_Object=MibScalar
opmen99810bIPSourceGuardStaticCreate=_Opmen99810bIPSourceGuardStaticCreate_Object((1,3,6,1,4,1,5205,2,94,3,1,2,1),_Opmen99810bIPSourceGuardStaticCreate_Type())
opmen99810bIPSourceGuardStaticCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardStaticCreate.setStatus(_A)
_Opmen99810bIPSourceGuardStaticTable_Object=MibTable
opmen99810bIPSourceGuardStaticTable=_Opmen99810bIPSourceGuardStaticTable_Object((1,3,6,1,4,1,5205,2,94,3,1,2,2))
if mibBuilder.loadTexts:opmen99810bIPSourceGuardStaticTable.setStatus(_A)
_Opmen99810bIPSourceGuardStaticEntry_Object=MibTableRow
opmen99810bIPSourceGuardStaticEntry=_Opmen99810bIPSourceGuardStaticEntry_Object((1,3,6,1,4,1,5205,2,94,3,1,2,2,1))
opmen99810bIPSourceGuardStaticEntry.setIndexNames((0,_G,_Aj))
if mibBuilder.loadTexts:opmen99810bIPSourceGuardStaticEntry.setStatus(_A)
class _Opmen99810bIPSourceGuardStaticIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_Opmen99810bIPSourceGuardStaticIndex_Type.__name__=_C
_Opmen99810bIPSourceGuardStaticIndex_Object=MibTableColumn
opmen99810bIPSourceGuardStaticIndex=_Opmen99810bIPSourceGuardStaticIndex_Object((1,3,6,1,4,1,5205,2,94,3,1,2,2,1,1),_Opmen99810bIPSourceGuardStaticIndex_Type())
opmen99810bIPSourceGuardStaticIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardStaticIndex.setStatus(_A)
class _Opmen99810bIPSourceGuardStaticPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bIPSourceGuardStaticPort_Type.__name__=_C
_Opmen99810bIPSourceGuardStaticPort_Object=MibTableColumn
opmen99810bIPSourceGuardStaticPort=_Opmen99810bIPSourceGuardStaticPort_Object((1,3,6,1,4,1,5205,2,94,3,1,2,2,1,2),_Opmen99810bIPSourceGuardStaticPort_Type())
opmen99810bIPSourceGuardStaticPort.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardStaticPort.setStatus(_A)
class _Opmen99810bIPSourceGuardStaticVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Opmen99810bIPSourceGuardStaticVLANId_Type.__name__=_C
_Opmen99810bIPSourceGuardStaticVLANId_Object=MibTableColumn
opmen99810bIPSourceGuardStaticVLANId=_Opmen99810bIPSourceGuardStaticVLANId_Object((1,3,6,1,4,1,5205,2,94,3,1,2,2,1,3),_Opmen99810bIPSourceGuardStaticVLANId_Type())
opmen99810bIPSourceGuardStaticVLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardStaticVLANId.setStatus(_A)
_Opmen99810bIPSourceGuardStaticIPAddress_Type=IpAddress
_Opmen99810bIPSourceGuardStaticIPAddress_Object=MibTableColumn
opmen99810bIPSourceGuardStaticIPAddress=_Opmen99810bIPSourceGuardStaticIPAddress_Object((1,3,6,1,4,1,5205,2,94,3,1,2,2,1,4),_Opmen99810bIPSourceGuardStaticIPAddress_Type())
opmen99810bIPSourceGuardStaticIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardStaticIPAddress.setStatus(_A)
_Opmen99810bIPSourceGuardStaticMACAddress_Type=MacAddress
_Opmen99810bIPSourceGuardStaticMACAddress_Object=MibTableColumn
opmen99810bIPSourceGuardStaticMACAddress=_Opmen99810bIPSourceGuardStaticMACAddress_Object((1,3,6,1,4,1,5205,2,94,3,1,2,2,1,5),_Opmen99810bIPSourceGuardStaticMACAddress_Type())
opmen99810bIPSourceGuardStaticMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardStaticMACAddress.setStatus(_A)
class _Opmen99810bIPSourceGuardStaticRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),(_X,2),(_b,3),(_Y,4),(_c,5)))
_Opmen99810bIPSourceGuardStaticRowStatus_Type.__name__=_C
_Opmen99810bIPSourceGuardStaticRowStatus_Object=MibTableColumn
opmen99810bIPSourceGuardStaticRowStatus=_Opmen99810bIPSourceGuardStaticRowStatus_Object((1,3,6,1,4,1,5205,2,94,3,1,2,2,1,6),_Opmen99810bIPSourceGuardStaticRowStatus_Type())
opmen99810bIPSourceGuardStaticRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardStaticRowStatus.setStatus(_A)
_Opmen99810bIPSourceGuardDynamicTable_Object=MibTable
opmen99810bIPSourceGuardDynamicTable=_Opmen99810bIPSourceGuardDynamicTable_Object((1,3,6,1,4,1,5205,2,94,3,1,3))
if mibBuilder.loadTexts:opmen99810bIPSourceGuardDynamicTable.setStatus(_A)
_Opmen99810bIPSourceGuardDynamicEntry_Object=MibTableRow
opmen99810bIPSourceGuardDynamicEntry=_Opmen99810bIPSourceGuardDynamicEntry_Object((1,3,6,1,4,1,5205,2,94,3,1,3,1))
opmen99810bIPSourceGuardDynamicEntry.setIndexNames((0,_G,_Ak))
if mibBuilder.loadTexts:opmen99810bIPSourceGuardDynamicEntry.setStatus(_A)
class _Opmen99810bIPSourceGuardDynamicIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bIPSourceGuardDynamicIndex_Type.__name__=_C
_Opmen99810bIPSourceGuardDynamicIndex_Object=MibTableColumn
opmen99810bIPSourceGuardDynamicIndex=_Opmen99810bIPSourceGuardDynamicIndex_Object((1,3,6,1,4,1,5205,2,94,3,1,3,1,1),_Opmen99810bIPSourceGuardDynamicIndex_Type())
opmen99810bIPSourceGuardDynamicIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardDynamicIndex.setStatus(_A)
class _Opmen99810bIPSourceGuardDynamicPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Opmen99810bIPSourceGuardDynamicPort_Type.__name__=_C
_Opmen99810bIPSourceGuardDynamicPort_Object=MibTableColumn
opmen99810bIPSourceGuardDynamicPort=_Opmen99810bIPSourceGuardDynamicPort_Object((1,3,6,1,4,1,5205,2,94,3,1,3,1,2),_Opmen99810bIPSourceGuardDynamicPort_Type())
opmen99810bIPSourceGuardDynamicPort.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardDynamicPort.setStatus(_A)
class _Opmen99810bIPSourceGuardDynamicVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Opmen99810bIPSourceGuardDynamicVLANId_Type.__name__=_C
_Opmen99810bIPSourceGuardDynamicVLANId_Object=MibTableColumn
opmen99810bIPSourceGuardDynamicVLANId=_Opmen99810bIPSourceGuardDynamicVLANId_Object((1,3,6,1,4,1,5205,2,94,3,1,3,1,3),_Opmen99810bIPSourceGuardDynamicVLANId_Type())
opmen99810bIPSourceGuardDynamicVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardDynamicVLANId.setStatus(_A)
_Opmen99810bIPSourceGuardDynamicIPAddress_Type=IpAddress
_Opmen99810bIPSourceGuardDynamicIPAddress_Object=MibTableColumn
opmen99810bIPSourceGuardDynamicIPAddress=_Opmen99810bIPSourceGuardDynamicIPAddress_Object((1,3,6,1,4,1,5205,2,94,3,1,3,1,4),_Opmen99810bIPSourceGuardDynamicIPAddress_Type())
opmen99810bIPSourceGuardDynamicIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardDynamicIPAddress.setStatus(_A)
_Opmen99810bIPSourceGuardDynamicMACAddress_Type=MacAddress
_Opmen99810bIPSourceGuardDynamicMACAddress_Object=MibTableColumn
opmen99810bIPSourceGuardDynamicMACAddress=_Opmen99810bIPSourceGuardDynamicMACAddress_Object((1,3,6,1,4,1,5205,2,94,3,1,3,1,5),_Opmen99810bIPSourceGuardDynamicMACAddress_Type())
opmen99810bIPSourceGuardDynamicMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bIPSourceGuardDynamicMACAddress.setStatus(_A)
_Opmen99810bARPInspection_ObjectIdentity=ObjectIdentity
opmen99810bARPInspection=_Opmen99810bARPInspection_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,2))
_Opmen99810bARPInspectionConf_ObjectIdentity=ObjectIdentity
opmen99810bARPInspectionConf=_Opmen99810bARPInspectionConf_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,2,1))
class _Opmen99810bARPInspectionConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bARPInspectionConfMode_Type.__name__=_C
_Opmen99810bARPInspectionConfMode_Object=MibScalar
opmen99810bARPInspectionConfMode=_Opmen99810bARPInspectionConfMode_Object((1,3,6,1,4,1,5205,2,94,3,2,1,1),_Opmen99810bARPInspectionConfMode_Type())
opmen99810bARPInspectionConfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bARPInspectionConfMode.setStatus(_A)
_Opmen99810bARPInspectionConfTable_Object=MibTable
opmen99810bARPInspectionConfTable=_Opmen99810bARPInspectionConfTable_Object((1,3,6,1,4,1,5205,2,94,3,2,1,2))
if mibBuilder.loadTexts:opmen99810bARPInspectionConfTable.setStatus(_A)
_Opmen99810bARPInspectionConfEntry_Object=MibTableRow
opmen99810bARPInspectionConfEntry=_Opmen99810bARPInspectionConfEntry_Object((1,3,6,1,4,1,5205,2,94,3,2,1,2,1))
opmen99810bARPInspectionConfEntry.setIndexNames((0,_G,_Al))
if mibBuilder.loadTexts:opmen99810bARPInspectionConfEntry.setStatus(_A)
class _Opmen99810bARPInspectionConfPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bARPInspectionConfPortIndex_Type.__name__=_C
_Opmen99810bARPInspectionConfPortIndex_Object=MibTableColumn
opmen99810bARPInspectionConfPortIndex=_Opmen99810bARPInspectionConfPortIndex_Object((1,3,6,1,4,1,5205,2,94,3,2,1,2,1,1),_Opmen99810bARPInspectionConfPortIndex_Type())
opmen99810bARPInspectionConfPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bARPInspectionConfPortIndex.setStatus(_A)
class _Opmen99810bARPInspectionConfPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bARPInspectionConfPortMode_Type.__name__=_C
_Opmen99810bARPInspectionConfPortMode_Object=MibTableColumn
opmen99810bARPInspectionConfPortMode=_Opmen99810bARPInspectionConfPortMode_Object((1,3,6,1,4,1,5205,2,94,3,2,1,2,1,2),_Opmen99810bARPInspectionConfPortMode_Type())
opmen99810bARPInspectionConfPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bARPInspectionConfPortMode.setStatus(_A)
_Opmen99810bARPInspectionStatic_ObjectIdentity=ObjectIdentity
opmen99810bARPInspectionStatic=_Opmen99810bARPInspectionStatic_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,2,2))
class _Opmen99810bARPInspectionStaticCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_W,1)))
_Opmen99810bARPInspectionStaticCreate_Type.__name__=_C
_Opmen99810bARPInspectionStaticCreate_Object=MibScalar
opmen99810bARPInspectionStaticCreate=_Opmen99810bARPInspectionStaticCreate_Object((1,3,6,1,4,1,5205,2,94,3,2,2,1),_Opmen99810bARPInspectionStaticCreate_Type())
opmen99810bARPInspectionStaticCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bARPInspectionStaticCreate.setStatus(_A)
_Opmen99810bARPInspectionStaticTable_Object=MibTable
opmen99810bARPInspectionStaticTable=_Opmen99810bARPInspectionStaticTable_Object((1,3,6,1,4,1,5205,2,94,3,2,2,2))
if mibBuilder.loadTexts:opmen99810bARPInspectionStaticTable.setStatus(_A)
_Opmen99810bARPInspectionStaticEntry_Object=MibTableRow
opmen99810bARPInspectionStaticEntry=_Opmen99810bARPInspectionStaticEntry_Object((1,3,6,1,4,1,5205,2,94,3,2,2,2,1))
opmen99810bARPInspectionStaticEntry.setIndexNames((0,_G,_Am))
if mibBuilder.loadTexts:opmen99810bARPInspectionStaticEntry.setStatus(_A)
class _Opmen99810bARPInspectionStaticIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bARPInspectionStaticIndex_Type.__name__=_C
_Opmen99810bARPInspectionStaticIndex_Object=MibTableColumn
opmen99810bARPInspectionStaticIndex=_Opmen99810bARPInspectionStaticIndex_Object((1,3,6,1,4,1,5205,2,94,3,2,2,2,1,1),_Opmen99810bARPInspectionStaticIndex_Type())
opmen99810bARPInspectionStaticIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bARPInspectionStaticIndex.setStatus(_A)
class _Opmen99810bARPInspectionStaticPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bARPInspectionStaticPort_Type.__name__=_C
_Opmen99810bARPInspectionStaticPort_Object=MibTableColumn
opmen99810bARPInspectionStaticPort=_Opmen99810bARPInspectionStaticPort_Object((1,3,6,1,4,1,5205,2,94,3,2,2,2,1,2),_Opmen99810bARPInspectionStaticPort_Type())
opmen99810bARPInspectionStaticPort.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bARPInspectionStaticPort.setStatus(_A)
class _Opmen99810bARPInspectionStaticVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Opmen99810bARPInspectionStaticVLANId_Type.__name__=_C
_Opmen99810bARPInspectionStaticVLANId_Object=MibTableColumn
opmen99810bARPInspectionStaticVLANId=_Opmen99810bARPInspectionStaticVLANId_Object((1,3,6,1,4,1,5205,2,94,3,2,2,2,1,3),_Opmen99810bARPInspectionStaticVLANId_Type())
opmen99810bARPInspectionStaticVLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bARPInspectionStaticVLANId.setStatus(_A)
_Opmen99810bARPInspectionStaticIPAddress_Type=IpAddress
_Opmen99810bARPInspectionStaticIPAddress_Object=MibTableColumn
opmen99810bARPInspectionStaticIPAddress=_Opmen99810bARPInspectionStaticIPAddress_Object((1,3,6,1,4,1,5205,2,94,3,2,2,2,1,4),_Opmen99810bARPInspectionStaticIPAddress_Type())
opmen99810bARPInspectionStaticIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bARPInspectionStaticIPAddress.setStatus(_A)
_Opmen99810bARPInspectionStaticMACAddress_Type=MacAddress
_Opmen99810bARPInspectionStaticMACAddress_Object=MibTableColumn
opmen99810bARPInspectionStaticMACAddress=_Opmen99810bARPInspectionStaticMACAddress_Object((1,3,6,1,4,1,5205,2,94,3,2,2,2,1,5),_Opmen99810bARPInspectionStaticMACAddress_Type())
opmen99810bARPInspectionStaticMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bARPInspectionStaticMACAddress.setStatus(_A)
class _Opmen99810bARPInspectionStaticRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),(_X,2),(_b,3),(_Y,4),(_c,5)))
_Opmen99810bARPInspectionStaticRowStatus_Type.__name__=_C
_Opmen99810bARPInspectionStaticRowStatus_Object=MibTableColumn
opmen99810bARPInspectionStaticRowStatus=_Opmen99810bARPInspectionStaticRowStatus_Object((1,3,6,1,4,1,5205,2,94,3,2,2,2,1,6),_Opmen99810bARPInspectionStaticRowStatus_Type())
opmen99810bARPInspectionStaticRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bARPInspectionStaticRowStatus.setStatus(_A)
_Opmen99810bARPInspectionDynamicTable_Object=MibTable
opmen99810bARPInspectionDynamicTable=_Opmen99810bARPInspectionDynamicTable_Object((1,3,6,1,4,1,5205,2,94,3,2,3))
if mibBuilder.loadTexts:opmen99810bARPInspectionDynamicTable.setStatus(_A)
_Opmen99810bARPInspectionDynamicEntry_Object=MibTableRow
opmen99810bARPInspectionDynamicEntry=_Opmen99810bARPInspectionDynamicEntry_Object((1,3,6,1,4,1,5205,2,94,3,2,3,1))
opmen99810bARPInspectionDynamicEntry.setIndexNames((0,_G,_An))
if mibBuilder.loadTexts:opmen99810bARPInspectionDynamicEntry.setStatus(_A)
class _Opmen99810bARPInspectionDynamicIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bARPInspectionDynamicIndex_Type.__name__=_C
_Opmen99810bARPInspectionDynamicIndex_Object=MibTableColumn
opmen99810bARPInspectionDynamicIndex=_Opmen99810bARPInspectionDynamicIndex_Object((1,3,6,1,4,1,5205,2,94,3,2,3,1,1),_Opmen99810bARPInspectionDynamicIndex_Type())
opmen99810bARPInspectionDynamicIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bARPInspectionDynamicIndex.setStatus(_A)
class _Opmen99810bARPInspectionDynamicPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bARPInspectionDynamicPort_Type.__name__=_C
_Opmen99810bARPInspectionDynamicPort_Object=MibTableColumn
opmen99810bARPInspectionDynamicPort=_Opmen99810bARPInspectionDynamicPort_Object((1,3,6,1,4,1,5205,2,94,3,2,3,1,2),_Opmen99810bARPInspectionDynamicPort_Type())
opmen99810bARPInspectionDynamicPort.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bARPInspectionDynamicPort.setStatus(_A)
class _Opmen99810bARPInspectionDynamicVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Opmen99810bARPInspectionDynamicVLANId_Type.__name__=_C
_Opmen99810bARPInspectionDynamicVLANId_Object=MibTableColumn
opmen99810bARPInspectionDynamicVLANId=_Opmen99810bARPInspectionDynamicVLANId_Object((1,3,6,1,4,1,5205,2,94,3,2,3,1,3),_Opmen99810bARPInspectionDynamicVLANId_Type())
opmen99810bARPInspectionDynamicVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bARPInspectionDynamicVLANId.setStatus(_A)
_Opmen99810bARPInspectionDynamicIPAddress_Type=IpAddress
_Opmen99810bARPInspectionDynamicIPAddress_Object=MibTableColumn
opmen99810bARPInspectionDynamicIPAddress=_Opmen99810bARPInspectionDynamicIPAddress_Object((1,3,6,1,4,1,5205,2,94,3,2,3,1,4),_Opmen99810bARPInspectionDynamicIPAddress_Type())
opmen99810bARPInspectionDynamicIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bARPInspectionDynamicIPAddress.setStatus(_A)
_Opmen99810bARPInspectionDynamicMACAddress_Type=MacAddress
_Opmen99810bARPInspectionDynamicMACAddress_Object=MibTableColumn
opmen99810bARPInspectionDynamicMACAddress=_Opmen99810bARPInspectionDynamicMACAddress_Object((1,3,6,1,4,1,5205,2,94,3,2,3,1,5),_Opmen99810bARPInspectionDynamicMACAddress_Type())
opmen99810bARPInspectionDynamicMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bARPInspectionDynamicMACAddress.setStatus(_A)
_Opmen99810bDHCPSnooping_ObjectIdentity=ObjectIdentity
opmen99810bDHCPSnooping=_Opmen99810bDHCPSnooping_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,3))
_Opmen99810bDHCPSnoopingConf_ObjectIdentity=ObjectIdentity
opmen99810bDHCPSnoopingConf=_Opmen99810bDHCPSnoopingConf_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,3,1))
class _Opmen99810bDHCPSnoopingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bDHCPSnoopingMode_Type.__name__=_C
_Opmen99810bDHCPSnoopingMode_Object=MibScalar
opmen99810bDHCPSnoopingMode=_Opmen99810bDHCPSnoopingMode_Object((1,3,6,1,4,1,5205,2,94,3,3,1,1),_Opmen99810bDHCPSnoopingMode_Type())
opmen99810bDHCPSnoopingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingMode.setStatus(_A)
_Opmen99810bDHCPSnoopingPortModeConfigurationTable_Object=MibTable
opmen99810bDHCPSnoopingPortModeConfigurationTable=_Opmen99810bDHCPSnoopingPortModeConfigurationTable_Object((1,3,6,1,4,1,5205,2,94,3,3,1,2))
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingPortModeConfigurationTable.setStatus(_A)
_Opmen99810bDHCPSnoopingPortModeConfigurationEntry_Object=MibTableRow
opmen99810bDHCPSnoopingPortModeConfigurationEntry=_Opmen99810bDHCPSnoopingPortModeConfigurationEntry_Object((1,3,6,1,4,1,5205,2,94,3,3,1,2,1))
opmen99810bDHCPSnoopingPortModeConfigurationEntry.setIndexNames((0,_G,_Ao))
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingPortModeConfigurationEntry.setStatus(_A)
class _Opmen99810bDHCPSnoopingPortModeConfigurationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bDHCPSnoopingPortModeConfigurationPort_Type.__name__=_C
_Opmen99810bDHCPSnoopingPortModeConfigurationPort_Object=MibTableColumn
opmen99810bDHCPSnoopingPortModeConfigurationPort=_Opmen99810bDHCPSnoopingPortModeConfigurationPort_Object((1,3,6,1,4,1,5205,2,94,3,3,1,2,1,1),_Opmen99810bDHCPSnoopingPortModeConfigurationPort_Type())
opmen99810bDHCPSnoopingPortModeConfigurationPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingPortModeConfigurationPort.setStatus(_A)
class _Opmen99810bDHCPSnoopingPortModeConfigurationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('trust',0),('untrust',1)))
_Opmen99810bDHCPSnoopingPortModeConfigurationMode_Type.__name__=_C
_Opmen99810bDHCPSnoopingPortModeConfigurationMode_Object=MibTableColumn
opmen99810bDHCPSnoopingPortModeConfigurationMode=_Opmen99810bDHCPSnoopingPortModeConfigurationMode_Object((1,3,6,1,4,1,5205,2,94,3,3,1,2,1,2),_Opmen99810bDHCPSnoopingPortModeConfigurationMode_Type())
opmen99810bDHCPSnoopingPortModeConfigurationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingPortModeConfigurationMode.setStatus(_A)
_Opmen99810bDHCPSnoopingStatisticsTable_Object=MibTable
opmen99810bDHCPSnoopingStatisticsTable=_Opmen99810bDHCPSnoopingStatisticsTable_Object((1,3,6,1,4,1,5205,2,94,3,3,2))
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingStatisticsTable.setStatus(_A)
_Opmen99810bDHCPSnoopingStatisticsEntry_Object=MibTableRow
opmen99810bDHCPSnoopingStatisticsEntry=_Opmen99810bDHCPSnoopingStatisticsEntry_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1))
opmen99810bDHCPSnoopingStatisticsEntry.setIndexNames((0,_G,_Ap))
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingStatisticsEntry.setStatus(_A)
class _Opmen99810bDHCPSnoopingStatisticsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bDHCPSnoopingStatisticsPort_Type.__name__=_C
_Opmen99810bDHCPSnoopingStatisticsPort_Object=MibTableColumn
opmen99810bDHCPSnoopingStatisticsPort=_Opmen99810bDHCPSnoopingStatisticsPort_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,1),_Opmen99810bDHCPSnoopingStatisticsPort_Type())
opmen99810bDHCPSnoopingStatisticsPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingStatisticsPort.setStatus(_A)
class _Opmen99810bDHCPSnoopingStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_e,1)))
_Opmen99810bDHCPSnoopingStatisticsClear_Type.__name__=_C
_Opmen99810bDHCPSnoopingStatisticsClear_Object=MibTableColumn
opmen99810bDHCPSnoopingStatisticsClear=_Opmen99810bDHCPSnoopingStatisticsClear_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,2),_Opmen99810bDHCPSnoopingStatisticsClear_Type())
opmen99810bDHCPSnoopingStatisticsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingStatisticsClear.setStatus(_A)
_Opmen99810bDHCPSnoopingRxDiscover_Type=Counter32
_Opmen99810bDHCPSnoopingRxDiscover_Object=MibTableColumn
opmen99810bDHCPSnoopingRxDiscover=_Opmen99810bDHCPSnoopingRxDiscover_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,3),_Opmen99810bDHCPSnoopingRxDiscover_Type())
opmen99810bDHCPSnoopingRxDiscover.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingRxDiscover.setStatus(_A)
_Opmen99810bDHCPSnoopingRxOffer_Type=Counter32
_Opmen99810bDHCPSnoopingRxOffer_Object=MibTableColumn
opmen99810bDHCPSnoopingRxOffer=_Opmen99810bDHCPSnoopingRxOffer_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,4),_Opmen99810bDHCPSnoopingRxOffer_Type())
opmen99810bDHCPSnoopingRxOffer.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingRxOffer.setStatus(_A)
_Opmen99810bDHCPSnoopingRxRequest_Type=Counter32
_Opmen99810bDHCPSnoopingRxRequest_Object=MibTableColumn
opmen99810bDHCPSnoopingRxRequest=_Opmen99810bDHCPSnoopingRxRequest_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,5),_Opmen99810bDHCPSnoopingRxRequest_Type())
opmen99810bDHCPSnoopingRxRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingRxRequest.setStatus(_A)
_Opmen99810bDHCPSnoopingRxDecline_Type=Counter32
_Opmen99810bDHCPSnoopingRxDecline_Object=MibTableColumn
opmen99810bDHCPSnoopingRxDecline=_Opmen99810bDHCPSnoopingRxDecline_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,6),_Opmen99810bDHCPSnoopingRxDecline_Type())
opmen99810bDHCPSnoopingRxDecline.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingRxDecline.setStatus(_A)
_Opmen99810bDHCPSnoopingRxACK_Type=Counter32
_Opmen99810bDHCPSnoopingRxACK_Object=MibTableColumn
opmen99810bDHCPSnoopingRxACK=_Opmen99810bDHCPSnoopingRxACK_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,7),_Opmen99810bDHCPSnoopingRxACK_Type())
opmen99810bDHCPSnoopingRxACK.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingRxACK.setStatus(_A)
_Opmen99810bDHCPSnoopingRxNAK_Type=Counter32
_Opmen99810bDHCPSnoopingRxNAK_Object=MibTableColumn
opmen99810bDHCPSnoopingRxNAK=_Opmen99810bDHCPSnoopingRxNAK_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,8),_Opmen99810bDHCPSnoopingRxNAK_Type())
opmen99810bDHCPSnoopingRxNAK.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingRxNAK.setStatus(_A)
_Opmen99810bDHCPSnoopingRxRelease_Type=Counter32
_Opmen99810bDHCPSnoopingRxRelease_Object=MibTableColumn
opmen99810bDHCPSnoopingRxRelease=_Opmen99810bDHCPSnoopingRxRelease_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,9),_Opmen99810bDHCPSnoopingRxRelease_Type())
opmen99810bDHCPSnoopingRxRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingRxRelease.setStatus(_A)
_Opmen99810bDHCPSnoopingRxInform_Type=Counter32
_Opmen99810bDHCPSnoopingRxInform_Object=MibTableColumn
opmen99810bDHCPSnoopingRxInform=_Opmen99810bDHCPSnoopingRxInform_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,10),_Opmen99810bDHCPSnoopingRxInform_Type())
opmen99810bDHCPSnoopingRxInform.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingRxInform.setStatus(_A)
_Opmen99810bDHCPSnoopingRxLeaseQuery_Type=Counter32
_Opmen99810bDHCPSnoopingRxLeaseQuery_Object=MibTableColumn
opmen99810bDHCPSnoopingRxLeaseQuery=_Opmen99810bDHCPSnoopingRxLeaseQuery_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,11),_Opmen99810bDHCPSnoopingRxLeaseQuery_Type())
opmen99810bDHCPSnoopingRxLeaseQuery.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingRxLeaseQuery.setStatus(_A)
_Opmen99810bDHCPSnoopingRxLeaseUnassigned_Type=Counter32
_Opmen99810bDHCPSnoopingRxLeaseUnassigned_Object=MibTableColumn
opmen99810bDHCPSnoopingRxLeaseUnassigned=_Opmen99810bDHCPSnoopingRxLeaseUnassigned_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,12),_Opmen99810bDHCPSnoopingRxLeaseUnassigned_Type())
opmen99810bDHCPSnoopingRxLeaseUnassigned.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingRxLeaseUnassigned.setStatus(_A)
_Opmen99810bDHCPSnoopingRxLeaseUnknown_Type=Counter32
_Opmen99810bDHCPSnoopingRxLeaseUnknown_Object=MibTableColumn
opmen99810bDHCPSnoopingRxLeaseUnknown=_Opmen99810bDHCPSnoopingRxLeaseUnknown_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,13),_Opmen99810bDHCPSnoopingRxLeaseUnknown_Type())
opmen99810bDHCPSnoopingRxLeaseUnknown.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingRxLeaseUnknown.setStatus(_A)
_Opmen99810bDHCPSnoopingRxLeaseActive_Type=Counter32
_Opmen99810bDHCPSnoopingRxLeaseActive_Object=MibTableColumn
opmen99810bDHCPSnoopingRxLeaseActive=_Opmen99810bDHCPSnoopingRxLeaseActive_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,14),_Opmen99810bDHCPSnoopingRxLeaseActive_Type())
opmen99810bDHCPSnoopingRxLeaseActive.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingRxLeaseActive.setStatus(_A)
_Opmen99810bDHCPSnoopingTxDiscover_Type=Counter32
_Opmen99810bDHCPSnoopingTxDiscover_Object=MibTableColumn
opmen99810bDHCPSnoopingTxDiscover=_Opmen99810bDHCPSnoopingTxDiscover_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,15),_Opmen99810bDHCPSnoopingTxDiscover_Type())
opmen99810bDHCPSnoopingTxDiscover.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingTxDiscover.setStatus(_A)
_Opmen99810bDHCPSnoopingTxOffer_Type=Counter32
_Opmen99810bDHCPSnoopingTxOffer_Object=MibTableColumn
opmen99810bDHCPSnoopingTxOffer=_Opmen99810bDHCPSnoopingTxOffer_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,16),_Opmen99810bDHCPSnoopingTxOffer_Type())
opmen99810bDHCPSnoopingTxOffer.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingTxOffer.setStatus(_A)
_Opmen99810bDHCPSnoopingTxRequest_Type=Counter32
_Opmen99810bDHCPSnoopingTxRequest_Object=MibTableColumn
opmen99810bDHCPSnoopingTxRequest=_Opmen99810bDHCPSnoopingTxRequest_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,17),_Opmen99810bDHCPSnoopingTxRequest_Type())
opmen99810bDHCPSnoopingTxRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingTxRequest.setStatus(_A)
_Opmen99810bDHCPSnoopingTxDecline_Type=Counter32
_Opmen99810bDHCPSnoopingTxDecline_Object=MibTableColumn
opmen99810bDHCPSnoopingTxDecline=_Opmen99810bDHCPSnoopingTxDecline_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,18),_Opmen99810bDHCPSnoopingTxDecline_Type())
opmen99810bDHCPSnoopingTxDecline.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingTxDecline.setStatus(_A)
_Opmen99810bDHCPSnoopingTxACK_Type=Counter32
_Opmen99810bDHCPSnoopingTxACK_Object=MibTableColumn
opmen99810bDHCPSnoopingTxACK=_Opmen99810bDHCPSnoopingTxACK_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,19),_Opmen99810bDHCPSnoopingTxACK_Type())
opmen99810bDHCPSnoopingTxACK.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingTxACK.setStatus(_A)
_Opmen99810bDHCPSnoopingTxNAK_Type=Counter32
_Opmen99810bDHCPSnoopingTxNAK_Object=MibTableColumn
opmen99810bDHCPSnoopingTxNAK=_Opmen99810bDHCPSnoopingTxNAK_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,20),_Opmen99810bDHCPSnoopingTxNAK_Type())
opmen99810bDHCPSnoopingTxNAK.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingTxNAK.setStatus(_A)
_Opmen99810bDHCPSnoopingTxRelease_Type=Counter32
_Opmen99810bDHCPSnoopingTxRelease_Object=MibTableColumn
opmen99810bDHCPSnoopingTxRelease=_Opmen99810bDHCPSnoopingTxRelease_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,21),_Opmen99810bDHCPSnoopingTxRelease_Type())
opmen99810bDHCPSnoopingTxRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingTxRelease.setStatus(_A)
_Opmen99810bDHCPSnoopingTxInform_Type=Counter32
_Opmen99810bDHCPSnoopingTxInform_Object=MibTableColumn
opmen99810bDHCPSnoopingTxInform=_Opmen99810bDHCPSnoopingTxInform_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,22),_Opmen99810bDHCPSnoopingTxInform_Type())
opmen99810bDHCPSnoopingTxInform.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingTxInform.setStatus(_A)
_Opmen99810bDHCPSnoopingTxLeaseQuery_Type=Counter32
_Opmen99810bDHCPSnoopingTxLeaseQuery_Object=MibTableColumn
opmen99810bDHCPSnoopingTxLeaseQuery=_Opmen99810bDHCPSnoopingTxLeaseQuery_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,23),_Opmen99810bDHCPSnoopingTxLeaseQuery_Type())
opmen99810bDHCPSnoopingTxLeaseQuery.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingTxLeaseQuery.setStatus(_A)
_Opmen99810bDHCPSnoopingTxLeaseUnassigned_Type=Counter32
_Opmen99810bDHCPSnoopingTxLeaseUnassigned_Object=MibTableColumn
opmen99810bDHCPSnoopingTxLeaseUnassigned=_Opmen99810bDHCPSnoopingTxLeaseUnassigned_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,24),_Opmen99810bDHCPSnoopingTxLeaseUnassigned_Type())
opmen99810bDHCPSnoopingTxLeaseUnassigned.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingTxLeaseUnassigned.setStatus(_A)
_Opmen99810bDHCPSnoopingTxLeaseUnknown_Type=Counter32
_Opmen99810bDHCPSnoopingTxLeaseUnknown_Object=MibTableColumn
opmen99810bDHCPSnoopingTxLeaseUnknown=_Opmen99810bDHCPSnoopingTxLeaseUnknown_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,25),_Opmen99810bDHCPSnoopingTxLeaseUnknown_Type())
opmen99810bDHCPSnoopingTxLeaseUnknown.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingTxLeaseUnknown.setStatus(_A)
_Opmen99810bDHCPSnoopingTxLeaseActive_Type=Counter32
_Opmen99810bDHCPSnoopingTxLeaseActive_Object=MibTableColumn
opmen99810bDHCPSnoopingTxLeaseActive=_Opmen99810bDHCPSnoopingTxLeaseActive_Object((1,3,6,1,4,1,5205,2,94,3,3,2,1,26),_Opmen99810bDHCPSnoopingTxLeaseActive_Type())
opmen99810bDHCPSnoopingTxLeaseActive.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bDHCPSnoopingTxLeaseActive.setStatus(_A)
_Opmen99810bDHCPRelay_ObjectIdentity=ObjectIdentity
opmen99810bDHCPRelay=_Opmen99810bDHCPRelay_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,4))
_Opmen99810bDHCPRelayConfiguration_ObjectIdentity=ObjectIdentity
opmen99810bDHCPRelayConfiguration=_Opmen99810bDHCPRelayConfiguration_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,4,1))
class _Opmen99810bDHCPRelayMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bDHCPRelayMode_Type.__name__=_C
_Opmen99810bDHCPRelayMode_Object=MibScalar
opmen99810bDHCPRelayMode=_Opmen99810bDHCPRelayMode_Object((1,3,6,1,4,1,5205,2,94,3,4,1,1),_Opmen99810bDHCPRelayMode_Type())
opmen99810bDHCPRelayMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bDHCPRelayMode.setStatus(_A)
_Opmen99810bDHCPRelayServer_Type=IpAddress
_Opmen99810bDHCPRelayServer_Object=MibScalar
opmen99810bDHCPRelayServer=_Opmen99810bDHCPRelayServer_Object((1,3,6,1,4,1,5205,2,94,3,4,1,2),_Opmen99810bDHCPRelayServer_Type())
opmen99810bDHCPRelayServer.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bDHCPRelayServer.setStatus(_A)
class _Opmen99810bDHCPRelayInformationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bDHCPRelayInformationMode_Type.__name__=_C
_Opmen99810bDHCPRelayInformationMode_Object=MibScalar
opmen99810bDHCPRelayInformationMode=_Opmen99810bDHCPRelayInformationMode_Object((1,3,6,1,4,1,5205,2,94,3,4,1,3),_Opmen99810bDHCPRelayInformationMode_Type())
opmen99810bDHCPRelayInformationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bDHCPRelayInformationMode.setStatus(_A)
class _Opmen99810bDHCPRelayInformationPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('replace',0),('keep',1),('drop',2)))
_Opmen99810bDHCPRelayInformationPolicy_Type.__name__=_C
_Opmen99810bDHCPRelayInformationPolicy_Object=MibScalar
opmen99810bDHCPRelayInformationPolicy=_Opmen99810bDHCPRelayInformationPolicy_Object((1,3,6,1,4,1,5205,2,94,3,4,1,4),_Opmen99810bDHCPRelayInformationPolicy_Type())
opmen99810bDHCPRelayInformationPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bDHCPRelayInformationPolicy.setStatus(_A)
_Opmen99810bDHCPRelayStatistics_ObjectIdentity=ObjectIdentity
opmen99810bDHCPRelayStatistics=_Opmen99810bDHCPRelayStatistics_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,4,2))
_Opmen99810bDHCPRelayServerStatistics_ObjectIdentity=ObjectIdentity
opmen99810bDHCPRelayServerStatistics=_Opmen99810bDHCPRelayServerStatistics_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,4,2,1))
_Opmen99810bServerStatTransmitToServer_Type=Counter32
_Opmen99810bServerStatTransmitToServer_Object=MibScalar
opmen99810bServerStatTransmitToServer=_Opmen99810bServerStatTransmitToServer_Object((1,3,6,1,4,1,5205,2,94,3,4,2,1,1),_Opmen99810bServerStatTransmitToServer_Type())
opmen99810bServerStatTransmitToServer.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bServerStatTransmitToServer.setStatus(_A)
_Opmen99810bServerStatTransmitError_Type=Counter32
_Opmen99810bServerStatTransmitError_Object=MibScalar
opmen99810bServerStatTransmitError=_Opmen99810bServerStatTransmitError_Object((1,3,6,1,4,1,5205,2,94,3,4,2,1,2),_Opmen99810bServerStatTransmitError_Type())
opmen99810bServerStatTransmitError.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bServerStatTransmitError.setStatus(_A)
_Opmen99810bServerStatReceiveFromServer_Type=Counter32
_Opmen99810bServerStatReceiveFromServer_Object=MibScalar
opmen99810bServerStatReceiveFromServer=_Opmen99810bServerStatReceiveFromServer_Object((1,3,6,1,4,1,5205,2,94,3,4,2,1,3),_Opmen99810bServerStatReceiveFromServer_Type())
opmen99810bServerStatReceiveFromServer.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bServerStatReceiveFromServer.setStatus(_A)
_Opmen99810bServerStatReceiveMissingAgentOption_Type=Counter32
_Opmen99810bServerStatReceiveMissingAgentOption_Object=MibScalar
opmen99810bServerStatReceiveMissingAgentOption=_Opmen99810bServerStatReceiveMissingAgentOption_Object((1,3,6,1,4,1,5205,2,94,3,4,2,1,4),_Opmen99810bServerStatReceiveMissingAgentOption_Type())
opmen99810bServerStatReceiveMissingAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bServerStatReceiveMissingAgentOption.setStatus(_A)
_Opmen99810bServerStatReceiveMissingCircuitID_Type=Counter32
_Opmen99810bServerStatReceiveMissingCircuitID_Object=MibScalar
opmen99810bServerStatReceiveMissingCircuitID=_Opmen99810bServerStatReceiveMissingCircuitID_Object((1,3,6,1,4,1,5205,2,94,3,4,2,1,5),_Opmen99810bServerStatReceiveMissingCircuitID_Type())
opmen99810bServerStatReceiveMissingCircuitID.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bServerStatReceiveMissingCircuitID.setStatus(_A)
_Opmen99810bServerStatReceiveMissingRemoteID_Type=Counter32
_Opmen99810bServerStatReceiveMissingRemoteID_Object=MibScalar
opmen99810bServerStatReceiveMissingRemoteID=_Opmen99810bServerStatReceiveMissingRemoteID_Object((1,3,6,1,4,1,5205,2,94,3,4,2,1,6),_Opmen99810bServerStatReceiveMissingRemoteID_Type())
opmen99810bServerStatReceiveMissingRemoteID.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bServerStatReceiveMissingRemoteID.setStatus(_A)
_Opmen99810bServerStatReceiveBadCircuitID_Type=Counter32
_Opmen99810bServerStatReceiveBadCircuitID_Object=MibScalar
opmen99810bServerStatReceiveBadCircuitID=_Opmen99810bServerStatReceiveBadCircuitID_Object((1,3,6,1,4,1,5205,2,94,3,4,2,1,7),_Opmen99810bServerStatReceiveBadCircuitID_Type())
opmen99810bServerStatReceiveBadCircuitID.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bServerStatReceiveBadCircuitID.setStatus(_A)
_Opmen99810bServerStatReceiveBadRemoteID_Type=Counter32
_Opmen99810bServerStatReceiveBadRemoteID_Object=MibScalar
opmen99810bServerStatReceiveBadRemoteID=_Opmen99810bServerStatReceiveBadRemoteID_Object((1,3,6,1,4,1,5205,2,94,3,4,2,1,8),_Opmen99810bServerStatReceiveBadRemoteID_Type())
opmen99810bServerStatReceiveBadRemoteID.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bServerStatReceiveBadRemoteID.setStatus(_A)
_Opmen99810bDHCPRelayClientStatistics_ObjectIdentity=ObjectIdentity
opmen99810bDHCPRelayClientStatistics=_Opmen99810bDHCPRelayClientStatistics_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,4,2,2))
_Opmen99810bClientStatTransmitToClient_Type=Counter32
_Opmen99810bClientStatTransmitToClient_Object=MibScalar
opmen99810bClientStatTransmitToClient=_Opmen99810bClientStatTransmitToClient_Object((1,3,6,1,4,1,5205,2,94,3,4,2,2,1),_Opmen99810bClientStatTransmitToClient_Type())
opmen99810bClientStatTransmitToClient.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bClientStatTransmitToClient.setStatus(_A)
_Opmen99810bClientStatTransmitError_Type=Counter32
_Opmen99810bClientStatTransmitError_Object=MibScalar
opmen99810bClientStatTransmitError=_Opmen99810bClientStatTransmitError_Object((1,3,6,1,4,1,5205,2,94,3,4,2,2,2),_Opmen99810bClientStatTransmitError_Type())
opmen99810bClientStatTransmitError.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bClientStatTransmitError.setStatus(_A)
_Opmen99810bClientStatReceivefromClient_Type=Counter32
_Opmen99810bClientStatReceivefromClient_Object=MibScalar
opmen99810bClientStatReceivefromClient=_Opmen99810bClientStatReceivefromClient_Object((1,3,6,1,4,1,5205,2,94,3,4,2,2,3),_Opmen99810bClientStatReceivefromClient_Type())
opmen99810bClientStatReceivefromClient.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bClientStatReceivefromClient.setStatus(_A)
_Opmen99810bClientStatReceiveAgentOption_Type=Counter32
_Opmen99810bClientStatReceiveAgentOption_Object=MibScalar
opmen99810bClientStatReceiveAgentOption=_Opmen99810bClientStatReceiveAgentOption_Object((1,3,6,1,4,1,5205,2,94,3,4,2,2,4),_Opmen99810bClientStatReceiveAgentOption_Type())
opmen99810bClientStatReceiveAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bClientStatReceiveAgentOption.setStatus(_A)
_Opmen99810bClientStatReplaceAgentOption_Type=Counter32
_Opmen99810bClientStatReplaceAgentOption_Object=MibScalar
opmen99810bClientStatReplaceAgentOption=_Opmen99810bClientStatReplaceAgentOption_Object((1,3,6,1,4,1,5205,2,94,3,4,2,2,5),_Opmen99810bClientStatReplaceAgentOption_Type())
opmen99810bClientStatReplaceAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bClientStatReplaceAgentOption.setStatus(_A)
_Opmen99810bClientStatKeepAgentOption_Type=Counter32
_Opmen99810bClientStatKeepAgentOption_Object=MibScalar
opmen99810bClientStatKeepAgentOption=_Opmen99810bClientStatKeepAgentOption_Object((1,3,6,1,4,1,5205,2,94,3,4,2,2,6),_Opmen99810bClientStatKeepAgentOption_Type())
opmen99810bClientStatKeepAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bClientStatKeepAgentOption.setStatus(_A)
_Opmen99810bClientStatDropAgentOption_Type=Counter32
_Opmen99810bClientStatDropAgentOption_Object=MibScalar
opmen99810bClientStatDropAgentOption=_Opmen99810bClientStatDropAgentOption_Object((1,3,6,1,4,1,5205,2,94,3,4,2,2,7),_Opmen99810bClientStatDropAgentOption_Type())
opmen99810bClientStatDropAgentOption.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bClientStatDropAgentOption.setStatus(_A)
_Opmen99810bPortSecurity_ObjectIdentity=ObjectIdentity
opmen99810bPortSecurity=_Opmen99810bPortSecurity_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,5))
_Opmen99810bPortSecLimitCtrl_ObjectIdentity=ObjectIdentity
opmen99810bPortSecLimitCtrl=_Opmen99810bPortSecLimitCtrl_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,5,1))
_Opmen99810bPortSecLimitCtrlSystemConf_ObjectIdentity=ObjectIdentity
opmen99810bPortSecLimitCtrlSystemConf=_Opmen99810bPortSecLimitCtrlSystemConf_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,5,1,1))
class _Opmen99810bPortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bPortSecurityMode_Type.__name__=_C
_Opmen99810bPortSecurityMode_Object=MibScalar
opmen99810bPortSecurityMode=_Opmen99810bPortSecurityMode_Object((1,3,6,1,4,1,5205,2,94,3,5,1,1,1),_Opmen99810bPortSecurityMode_Type())
opmen99810bPortSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortSecurityMode.setStatus(_A)
class _Opmen99810bPortSecurityAging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bPortSecurityAging_Type.__name__=_C
_Opmen99810bPortSecurityAging_Object=MibScalar
opmen99810bPortSecurityAging=_Opmen99810bPortSecurityAging_Object((1,3,6,1,4,1,5205,2,94,3,5,1,1,2),_Opmen99810bPortSecurityAging_Type())
opmen99810bPortSecurityAging.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortSecurityAging.setStatus(_A)
class _Opmen99810bPortSecurityAgingPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10000000))
_Opmen99810bPortSecurityAgingPeriod_Type.__name__=_C
_Opmen99810bPortSecurityAgingPeriod_Object=MibScalar
opmen99810bPortSecurityAgingPeriod=_Opmen99810bPortSecurityAgingPeriod_Object((1,3,6,1,4,1,5205,2,94,3,5,1,1,3),_Opmen99810bPortSecurityAgingPeriod_Type())
opmen99810bPortSecurityAgingPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortSecurityAgingPeriod.setStatus(_A)
_Opmen99810bPortSecLimitCtrlTable_Object=MibTable
opmen99810bPortSecLimitCtrlTable=_Opmen99810bPortSecLimitCtrlTable_Object((1,3,6,1,4,1,5205,2,94,3,5,1,2))
if mibBuilder.loadTexts:opmen99810bPortSecLimitCtrlTable.setStatus(_A)
_Opmen99810bPortSecLimitCtrlEntry_Object=MibTableRow
opmen99810bPortSecLimitCtrlEntry=_Opmen99810bPortSecLimitCtrlEntry_Object((1,3,6,1,4,1,5205,2,94,3,5,1,2,1))
opmen99810bPortSecLimitCtrlEntry.setIndexNames((0,_G,_Aq))
if mibBuilder.loadTexts:opmen99810bPortSecLimitCtrlEntry.setStatus(_A)
class _Opmen99810bPortSecLimitCtrlPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bPortSecLimitCtrlPort_Type.__name__=_C
_Opmen99810bPortSecLimitCtrlPort_Object=MibTableColumn
opmen99810bPortSecLimitCtrlPort=_Opmen99810bPortSecLimitCtrlPort_Object((1,3,6,1,4,1,5205,2,94,3,5,1,2,1,1),_Opmen99810bPortSecLimitCtrlPort_Type())
opmen99810bPortSecLimitCtrlPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bPortSecLimitCtrlPort.setStatus(_A)
class _Opmen99810bPortSecLimitCtrlPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bPortSecLimitCtrlPortMode_Type.__name__=_C
_Opmen99810bPortSecLimitCtrlPortMode_Object=MibTableColumn
opmen99810bPortSecLimitCtrlPortMode=_Opmen99810bPortSecLimitCtrlPortMode_Object((1,3,6,1,4,1,5205,2,94,3,5,1,2,1,2),_Opmen99810bPortSecLimitCtrlPortMode_Type())
opmen99810bPortSecLimitCtrlPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortSecLimitCtrlPortMode.setStatus(_A)
class _Opmen99810bPortSecLimitCtrlPortLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Opmen99810bPortSecLimitCtrlPortLimit_Type.__name__=_C
_Opmen99810bPortSecLimitCtrlPortLimit_Object=MibTableColumn
opmen99810bPortSecLimitCtrlPortLimit=_Opmen99810bPortSecLimitCtrlPortLimit_Object((1,3,6,1,4,1,5205,2,94,3,5,1,2,1,3),_Opmen99810bPortSecLimitCtrlPortLimit_Type())
opmen99810bPortSecLimitCtrlPortLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortSecLimitCtrlPortLimit.setStatus(_A)
class _Opmen99810bPortSecLimitCtrlPortAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Q,0),('trap',1),('shutdown',2),('trapShutdown',3)))
_Opmen99810bPortSecLimitCtrlPortAction_Type.__name__=_C
_Opmen99810bPortSecLimitCtrlPortAction_Object=MibTableColumn
opmen99810bPortSecLimitCtrlPortAction=_Opmen99810bPortSecLimitCtrlPortAction_Object((1,3,6,1,4,1,5205,2,94,3,5,1,2,1,4),_Opmen99810bPortSecLimitCtrlPortAction_Type())
opmen99810bPortSecLimitCtrlPortAction.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortSecLimitCtrlPortAction.setStatus(_A)
_Opmen99810bPortSecLimitCtrlPortState_Type=DisplayString
_Opmen99810bPortSecLimitCtrlPortState_Object=MibTableColumn
opmen99810bPortSecLimitCtrlPortState=_Opmen99810bPortSecLimitCtrlPortState_Object((1,3,6,1,4,1,5205,2,94,3,5,1,2,1,5),_Opmen99810bPortSecLimitCtrlPortState_Type())
opmen99810bPortSecLimitCtrlPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortSecLimitCtrlPortState.setStatus(_A)
class _Opmen99810bPortSecLimitCtrlPortReOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),('reopen',1)))
_Opmen99810bPortSecLimitCtrlPortReOpen_Type.__name__=_C
_Opmen99810bPortSecLimitCtrlPortReOpen_Object=MibTableColumn
opmen99810bPortSecLimitCtrlPortReOpen=_Opmen99810bPortSecLimitCtrlPortReOpen_Object((1,3,6,1,4,1,5205,2,94,3,5,1,2,1,6),_Opmen99810bPortSecLimitCtrlPortReOpen_Type())
opmen99810bPortSecLimitCtrlPortReOpen.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortSecLimitCtrlPortReOpen.setStatus(_A)
_Opmen99810bPortSecSwitchStatusTable_Object=MibTable
opmen99810bPortSecSwitchStatusTable=_Opmen99810bPortSecSwitchStatusTable_Object((1,3,6,1,4,1,5205,2,94,3,5,2))
if mibBuilder.loadTexts:opmen99810bPortSecSwitchStatusTable.setStatus(_A)
_Opmen99810bPortSecSwitchStatusEntry_Object=MibTableRow
opmen99810bPortSecSwitchStatusEntry=_Opmen99810bPortSecSwitchStatusEntry_Object((1,3,6,1,4,1,5205,2,94,3,5,2,1))
opmen99810bPortSecSwitchStatusEntry.setIndexNames((0,_G,_Ar))
if mibBuilder.loadTexts:opmen99810bPortSecSwitchStatusEntry.setStatus(_A)
class _Opmen99810bPortSecSwitchStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bPortSecSwitchStatusPort_Type.__name__=_C
_Opmen99810bPortSecSwitchStatusPort_Object=MibTableColumn
opmen99810bPortSecSwitchStatusPort=_Opmen99810bPortSecSwitchStatusPort_Object((1,3,6,1,4,1,5205,2,94,3,5,2,1,1),_Opmen99810bPortSecSwitchStatusPort_Type())
opmen99810bPortSecSwitchStatusPort.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bPortSecSwitchStatusPort.setStatus(_A)
_Opmen99810bPortSecSwitchStatusUsers_Type=DisplayString
_Opmen99810bPortSecSwitchStatusUsers_Object=MibTableColumn
opmen99810bPortSecSwitchStatusUsers=_Opmen99810bPortSecSwitchStatusUsers_Object((1,3,6,1,4,1,5205,2,94,3,5,2,1,2),_Opmen99810bPortSecSwitchStatusUsers_Type())
opmen99810bPortSecSwitchStatusUsers.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortSecSwitchStatusUsers.setStatus(_A)
_Opmen99810bPortSecSwitchStatusState_Type=DisplayString
_Opmen99810bPortSecSwitchStatusState_Object=MibTableColumn
opmen99810bPortSecSwitchStatusState=_Opmen99810bPortSecSwitchStatusState_Object((1,3,6,1,4,1,5205,2,94,3,5,2,1,3),_Opmen99810bPortSecSwitchStatusState_Type())
opmen99810bPortSecSwitchStatusState.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortSecSwitchStatusState.setStatus(_A)
class _Opmen99810bPortSecSwitchStatusMACCountCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bPortSecSwitchStatusMACCountCurrent_Type.__name__=_C
_Opmen99810bPortSecSwitchStatusMACCountCurrent_Object=MibTableColumn
opmen99810bPortSecSwitchStatusMACCountCurrent=_Opmen99810bPortSecSwitchStatusMACCountCurrent_Object((1,3,6,1,4,1,5205,2,94,3,5,2,1,4),_Opmen99810bPortSecSwitchStatusMACCountCurrent_Type())
opmen99810bPortSecSwitchStatusMACCountCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortSecSwitchStatusMACCountCurrent.setStatus(_A)
class _Opmen99810bPortSecSwitchStatusMACCountLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bPortSecSwitchStatusMACCountLimit_Type.__name__=_C
_Opmen99810bPortSecSwitchStatusMACCountLimit_Object=MibTableColumn
opmen99810bPortSecSwitchStatusMACCountLimit=_Opmen99810bPortSecSwitchStatusMACCountLimit_Object((1,3,6,1,4,1,5205,2,94,3,5,2,1,5),_Opmen99810bPortSecSwitchStatusMACCountLimit_Type())
opmen99810bPortSecSwitchStatusMACCountLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortSecSwitchStatusMACCountLimit.setStatus(_A)
_Opmen99810bPortSecPortStatus_ObjectIdentity=ObjectIdentity
opmen99810bPortSecPortStatus=_Opmen99810bPortSecPortStatus_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,5,3))
class _Opmen99810bPortSecPortStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bPortSecPortStatusPort_Type.__name__=_C
_Opmen99810bPortSecPortStatusPort_Object=MibScalar
opmen99810bPortSecPortStatusPort=_Opmen99810bPortSecPortStatusPort_Object((1,3,6,1,4,1,5205,2,94,3,5,3,1),_Opmen99810bPortSecPortStatusPort_Type())
opmen99810bPortSecPortStatusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPortSecPortStatusPort.setStatus(_A)
_Opmen99810bPortSecPortStatusTable_Object=MibTable
opmen99810bPortSecPortStatusTable=_Opmen99810bPortSecPortStatusTable_Object((1,3,6,1,4,1,5205,2,94,3,5,3,2))
if mibBuilder.loadTexts:opmen99810bPortSecPortStatusTable.setStatus(_A)
_Opmen99810bPortSecPortStatusEntry_Object=MibTableRow
opmen99810bPortSecPortStatusEntry=_Opmen99810bPortSecPortStatusEntry_Object((1,3,6,1,4,1,5205,2,94,3,5,3,2,1))
opmen99810bPortSecPortStatusEntry.setIndexNames((0,_G,_As))
if mibBuilder.loadTexts:opmen99810bPortSecPortStatusEntry.setStatus(_A)
class _Opmen99810bPortSecPortStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Opmen99810bPortSecPortStatusIndex_Type.__name__=_C
_Opmen99810bPortSecPortStatusIndex_Object=MibTableColumn
opmen99810bPortSecPortStatusIndex=_Opmen99810bPortSecPortStatusIndex_Object((1,3,6,1,4,1,5205,2,94,3,5,3,2,1,1),_Opmen99810bPortSecPortStatusIndex_Type())
opmen99810bPortSecPortStatusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:opmen99810bPortSecPortStatusIndex.setStatus(_A)
_Opmen99810bPortSecPortStatusMACAddress_Type=MacAddress
_Opmen99810bPortSecPortStatusMACAddress_Object=MibTableColumn
opmen99810bPortSecPortStatusMACAddress=_Opmen99810bPortSecPortStatusMACAddress_Object((1,3,6,1,4,1,5205,2,94,3,5,3,2,1,2),_Opmen99810bPortSecPortStatusMACAddress_Type())
opmen99810bPortSecPortStatusMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortSecPortStatusMACAddress.setStatus(_A)
class _Opmen99810bPortSecPortStatusVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Opmen99810bPortSecPortStatusVLANId_Type.__name__=_C
_Opmen99810bPortSecPortStatusVLANId_Object=MibTableColumn
opmen99810bPortSecPortStatusVLANId=_Opmen99810bPortSecPortStatusVLANId_Object((1,3,6,1,4,1,5205,2,94,3,5,3,2,1,3),_Opmen99810bPortSecPortStatusVLANId_Type())
opmen99810bPortSecPortStatusVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortSecPortStatusVLANId.setStatus(_A)
_Opmen99810bPortSecPortStatusState_Type=DisplayString
_Opmen99810bPortSecPortStatusState_Object=MibTableColumn
opmen99810bPortSecPortStatusState=_Opmen99810bPortSecPortStatusState_Object((1,3,6,1,4,1,5205,2,94,3,5,3,2,1,4),_Opmen99810bPortSecPortStatusState_Type())
opmen99810bPortSecPortStatusState.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortSecPortStatusState.setStatus(_A)
_Opmen99810bPortSecPortStatusTimeOfAddition_Type=DisplayString
_Opmen99810bPortSecPortStatusTimeOfAddition_Object=MibTableColumn
opmen99810bPortSecPortStatusTimeOfAddition=_Opmen99810bPortSecPortStatusTimeOfAddition_Object((1,3,6,1,4,1,5205,2,94,3,5,3,2,1,5),_Opmen99810bPortSecPortStatusTimeOfAddition_Type())
opmen99810bPortSecPortStatusTimeOfAddition.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortSecPortStatusTimeOfAddition.setStatus(_A)
_Opmen99810bPortSecPortStatusAgeAndHold_Type=DisplayString
_Opmen99810bPortSecPortStatusAgeAndHold_Object=MibTableColumn
opmen99810bPortSecPortStatusAgeAndHold=_Opmen99810bPortSecPortStatusAgeAndHold_Object((1,3,6,1,4,1,5205,2,94,3,5,3,2,1,6),_Opmen99810bPortSecPortStatusAgeAndHold_Type())
opmen99810bPortSecPortStatusAgeAndHold.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPortSecPortStatusAgeAndHold.setStatus(_A)
_Opmen99810bAccessManagement_ObjectIdentity=ObjectIdentity
opmen99810bAccessManagement=_Opmen99810bAccessManagement_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,6))
_Opmen99810bAccessMgtConf_ObjectIdentity=ObjectIdentity
opmen99810bAccessMgtConf=_Opmen99810bAccessMgtConf_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,6,1))
class _Opmen99810bAccessMgtConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bAccessMgtConfMode_Type.__name__=_C
_Opmen99810bAccessMgtConfMode_Object=MibScalar
opmen99810bAccessMgtConfMode=_Opmen99810bAccessMgtConfMode_Object((1,3,6,1,4,1,5205,2,94,3,6,1,1),_Opmen99810bAccessMgtConfMode_Type())
opmen99810bAccessMgtConfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bAccessMgtConfMode.setStatus(_A)
class _Opmen99810bAccessMgtConfCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_W,1)))
_Opmen99810bAccessMgtConfCreate_Type.__name__=_C
_Opmen99810bAccessMgtConfCreate_Object=MibScalar
opmen99810bAccessMgtConfCreate=_Opmen99810bAccessMgtConfCreate_Object((1,3,6,1,4,1,5205,2,94,3,6,1,2),_Opmen99810bAccessMgtConfCreate_Type())
opmen99810bAccessMgtConfCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bAccessMgtConfCreate.setStatus(_A)
_Opmen99810bAccessMgtConfTable_Object=MibTable
opmen99810bAccessMgtConfTable=_Opmen99810bAccessMgtConfTable_Object((1,3,6,1,4,1,5205,2,94,3,6,1,3))
if mibBuilder.loadTexts:opmen99810bAccessMgtConfTable.setStatus(_A)
_Opmen99810bAccessMgtConfEntry_Object=MibTableRow
opmen99810bAccessMgtConfEntry=_Opmen99810bAccessMgtConfEntry_Object((1,3,6,1,4,1,5205,2,94,3,6,1,3,1))
opmen99810bAccessMgtConfEntry.setIndexNames((0,_G,_At))
if mibBuilder.loadTexts:opmen99810bAccessMgtConfEntry.setStatus(_A)
class _Opmen99810bAccessMgtIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Opmen99810bAccessMgtIndex_Type.__name__=_C
_Opmen99810bAccessMgtIndex_Object=MibTableColumn
opmen99810bAccessMgtIndex=_Opmen99810bAccessMgtIndex_Object((1,3,6,1,4,1,5205,2,94,3,6,1,3,1,1),_Opmen99810bAccessMgtIndex_Type())
opmen99810bAccessMgtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bAccessMgtIndex.setStatus(_A)
class _Opmen99810bAccessMgtAddresstype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_d,0),(_j,1)))
_Opmen99810bAccessMgtAddresstype_Type.__name__=_C
_Opmen99810bAccessMgtAddresstype_Object=MibTableColumn
opmen99810bAccessMgtAddresstype=_Opmen99810bAccessMgtAddresstype_Object((1,3,6,1,4,1,5205,2,94,3,6,1,3,1,2),_Opmen99810bAccessMgtAddresstype_Type())
opmen99810bAccessMgtAddresstype.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bAccessMgtAddresstype.setStatus(_A)
_Opmen99810bAccessMgtStartIpAddress_Type=DisplayString
_Opmen99810bAccessMgtStartIpAddress_Object=MibTableColumn
opmen99810bAccessMgtStartIpAddress=_Opmen99810bAccessMgtStartIpAddress_Object((1,3,6,1,4,1,5205,2,94,3,6,1,3,1,3),_Opmen99810bAccessMgtStartIpAddress_Type())
opmen99810bAccessMgtStartIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bAccessMgtStartIpAddress.setStatus(_A)
_Opmen99810bAccessMgtEndIpAddress_Type=DisplayString
_Opmen99810bAccessMgtEndIpAddress_Object=MibTableColumn
opmen99810bAccessMgtEndIpAddress=_Opmen99810bAccessMgtEndIpAddress_Object((1,3,6,1,4,1,5205,2,94,3,6,1,3,1,4),_Opmen99810bAccessMgtEndIpAddress_Type())
opmen99810bAccessMgtEndIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bAccessMgtEndIpAddress.setStatus(_A)
class _Opmen99810bAccessMgtHttpHttps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bAccessMgtHttpHttps_Type.__name__=_C
_Opmen99810bAccessMgtHttpHttps_Object=MibTableColumn
opmen99810bAccessMgtHttpHttps=_Opmen99810bAccessMgtHttpHttps_Object((1,3,6,1,4,1,5205,2,94,3,6,1,3,1,5),_Opmen99810bAccessMgtHttpHttps_Type())
opmen99810bAccessMgtHttpHttps.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bAccessMgtHttpHttps.setStatus(_A)
class _Opmen99810bAccessMgtSNMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bAccessMgtSNMP_Type.__name__=_C
_Opmen99810bAccessMgtSNMP_Object=MibTableColumn
opmen99810bAccessMgtSNMP=_Opmen99810bAccessMgtSNMP_Object((1,3,6,1,4,1,5205,2,94,3,6,1,3,1,6),_Opmen99810bAccessMgtSNMP_Type())
opmen99810bAccessMgtSNMP.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bAccessMgtSNMP.setStatus(_A)
class _Opmen99810bAccessMgtTelnetSSH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bAccessMgtTelnetSSH_Type.__name__=_C
_Opmen99810bAccessMgtTelnetSSH_Object=MibTableColumn
opmen99810bAccessMgtTelnetSSH=_Opmen99810bAccessMgtTelnetSSH_Object((1,3,6,1,4,1,5205,2,94,3,6,1,3,1,7),_Opmen99810bAccessMgtTelnetSSH_Type())
opmen99810bAccessMgtTelnetSSH.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bAccessMgtTelnetSSH.setStatus(_A)
class _Opmen99810bAccessMgtRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),(_X,2),(_b,3),(_Y,4),(_c,5)))
_Opmen99810bAccessMgtRowStatus_Type.__name__=_C
_Opmen99810bAccessMgtRowStatus_Object=MibTableColumn
opmen99810bAccessMgtRowStatus=_Opmen99810bAccessMgtRowStatus_Object((1,3,6,1,4,1,5205,2,94,3,6,1,3,1,8),_Opmen99810bAccessMgtRowStatus_Type())
opmen99810bAccessMgtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bAccessMgtRowStatus.setStatus(_A)
_Opmen99810bAccessMgtStatistics_ObjectIdentity=ObjectIdentity
opmen99810bAccessMgtStatistics=_Opmen99810bAccessMgtStatistics_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,6,2))
_Opmen99810bHttpReceivedPkts_Type=Counter32
_Opmen99810bHttpReceivedPkts_Object=MibScalar
opmen99810bHttpReceivedPkts=_Opmen99810bHttpReceivedPkts_Object((1,3,6,1,4,1,5205,2,94,3,6,2,1),_Opmen99810bHttpReceivedPkts_Type())
opmen99810bHttpReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bHttpReceivedPkts.setStatus(_A)
_Opmen99810bHttpAllowedPkts_Type=Counter32
_Opmen99810bHttpAllowedPkts_Object=MibScalar
opmen99810bHttpAllowedPkts=_Opmen99810bHttpAllowedPkts_Object((1,3,6,1,4,1,5205,2,94,3,6,2,2),_Opmen99810bHttpAllowedPkts_Type())
opmen99810bHttpAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bHttpAllowedPkts.setStatus(_A)
_Opmen99810bHttpDiscardedPkts_Type=Counter32
_Opmen99810bHttpDiscardedPkts_Object=MibScalar
opmen99810bHttpDiscardedPkts=_Opmen99810bHttpDiscardedPkts_Object((1,3,6,1,4,1,5205,2,94,3,6,2,3),_Opmen99810bHttpDiscardedPkts_Type())
opmen99810bHttpDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bHttpDiscardedPkts.setStatus(_A)
_Opmen99810bHttpsReceivedPkts_Type=Counter32
_Opmen99810bHttpsReceivedPkts_Object=MibScalar
opmen99810bHttpsReceivedPkts=_Opmen99810bHttpsReceivedPkts_Object((1,3,6,1,4,1,5205,2,94,3,6,2,4),_Opmen99810bHttpsReceivedPkts_Type())
opmen99810bHttpsReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bHttpsReceivedPkts.setStatus(_A)
_Opmen99810bHttpsAllowedPkts_Type=Counter32
_Opmen99810bHttpsAllowedPkts_Object=MibScalar
opmen99810bHttpsAllowedPkts=_Opmen99810bHttpsAllowedPkts_Object((1,3,6,1,4,1,5205,2,94,3,6,2,5),_Opmen99810bHttpsAllowedPkts_Type())
opmen99810bHttpsAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bHttpsAllowedPkts.setStatus(_A)
_Opmen99810bHttpsDiscardedPkts_Type=Counter32
_Opmen99810bHttpsDiscardedPkts_Object=MibScalar
opmen99810bHttpsDiscardedPkts=_Opmen99810bHttpsDiscardedPkts_Object((1,3,6,1,4,1,5205,2,94,3,6,2,6),_Opmen99810bHttpsDiscardedPkts_Type())
opmen99810bHttpsDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bHttpsDiscardedPkts.setStatus(_A)
_Opmen99810bSnmpReceivedPkts_Type=Counter32
_Opmen99810bSnmpReceivedPkts_Object=MibScalar
opmen99810bSnmpReceivedPkts=_Opmen99810bSnmpReceivedPkts_Object((1,3,6,1,4,1,5205,2,94,3,6,2,7),_Opmen99810bSnmpReceivedPkts_Type())
opmen99810bSnmpReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSnmpReceivedPkts.setStatus(_A)
_Opmen99810bSnmpAllowedPkts_Type=Counter32
_Opmen99810bSnmpAllowedPkts_Object=MibScalar
opmen99810bSnmpAllowedPkts=_Opmen99810bSnmpAllowedPkts_Object((1,3,6,1,4,1,5205,2,94,3,6,2,8),_Opmen99810bSnmpAllowedPkts_Type())
opmen99810bSnmpAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSnmpAllowedPkts.setStatus(_A)
_Opmen99810bSnmpDiscardedPkts_Type=Counter32
_Opmen99810bSnmpDiscardedPkts_Object=MibScalar
opmen99810bSnmpDiscardedPkts=_Opmen99810bSnmpDiscardedPkts_Object((1,3,6,1,4,1,5205,2,94,3,6,2,9),_Opmen99810bSnmpDiscardedPkts_Type())
opmen99810bSnmpDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSnmpDiscardedPkts.setStatus(_A)
_Opmen99810bTelnetReceivedPkts_Type=Counter32
_Opmen99810bTelnetReceivedPkts_Object=MibScalar
opmen99810bTelnetReceivedPkts=_Opmen99810bTelnetReceivedPkts_Object((1,3,6,1,4,1,5205,2,94,3,6,2,10),_Opmen99810bTelnetReceivedPkts_Type())
opmen99810bTelnetReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bTelnetReceivedPkts.setStatus(_A)
_Opmen99810bTelnetAllowedPkts_Type=Counter32
_Opmen99810bTelnetAllowedPkts_Object=MibScalar
opmen99810bTelnetAllowedPkts=_Opmen99810bTelnetAllowedPkts_Object((1,3,6,1,4,1,5205,2,94,3,6,2,11),_Opmen99810bTelnetAllowedPkts_Type())
opmen99810bTelnetAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bTelnetAllowedPkts.setStatus(_A)
_Opmen99810bTelnetDiscardedPkts_Type=Counter32
_Opmen99810bTelnetDiscardedPkts_Object=MibScalar
opmen99810bTelnetDiscardedPkts=_Opmen99810bTelnetDiscardedPkts_Object((1,3,6,1,4,1,5205,2,94,3,6,2,12),_Opmen99810bTelnetDiscardedPkts_Type())
opmen99810bTelnetDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bTelnetDiscardedPkts.setStatus(_A)
_Opmen99810bSSHReceivedPkts_Type=Counter32
_Opmen99810bSSHReceivedPkts_Object=MibScalar
opmen99810bSSHReceivedPkts=_Opmen99810bSSHReceivedPkts_Object((1,3,6,1,4,1,5205,2,94,3,6,2,13),_Opmen99810bSSHReceivedPkts_Type())
opmen99810bSSHReceivedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSSHReceivedPkts.setStatus(_A)
_Opmen99810bSSHAllowedPkts_Type=Counter32
_Opmen99810bSSHAllowedPkts_Object=MibScalar
opmen99810bSSHAllowedPkts=_Opmen99810bSSHAllowedPkts_Object((1,3,6,1,4,1,5205,2,94,3,6,2,14),_Opmen99810bSSHAllowedPkts_Type())
opmen99810bSSHAllowedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSSHAllowedPkts.setStatus(_A)
_Opmen99810bSSHDiscardedPkts_Type=Counter32
_Opmen99810bSSHDiscardedPkts_Object=MibScalar
opmen99810bSSHDiscardedPkts=_Opmen99810bSSHDiscardedPkts_Object((1,3,6,1,4,1,5205,2,94,3,6,2,15),_Opmen99810bSSHDiscardedPkts_Type())
opmen99810bSSHDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bSSHDiscardedPkts.setStatus(_A)
class _Opmen99810bAccessMgtStatisticsClearAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_e,1)))
_Opmen99810bAccessMgtStatisticsClearAll_Type.__name__=_C
_Opmen99810bAccessMgtStatisticsClearAll_Object=MibScalar
opmen99810bAccessMgtStatisticsClearAll=_Opmen99810bAccessMgtStatisticsClearAll_Object((1,3,6,1,4,1,5205,2,94,3,6,2,16),_Opmen99810bAccessMgtStatisticsClearAll_Type())
opmen99810bAccessMgtStatisticsClearAll.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bAccessMgtStatisticsClearAll.setStatus(_A)
_Opmen99810bSSH_ObjectIdentity=ObjectIdentity
opmen99810bSSH=_Opmen99810bSSH_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,7))
class _Opmen99810bSSHMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bSSHMode_Type.__name__=_C
_Opmen99810bSSHMode_Object=MibScalar
opmen99810bSSHMode=_Opmen99810bSSHMode_Object((1,3,6,1,4,1,5205,2,94,3,7,1),_Opmen99810bSSHMode_Type())
opmen99810bSSHMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSSHMode.setStatus(_A)
_Opmen99810bHTTPS_ObjectIdentity=ObjectIdentity
opmen99810bHTTPS=_Opmen99810bHTTPS_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,8))
class _Opmen99810bHTTPSMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bHTTPSMode_Type.__name__=_C
_Opmen99810bHTTPSMode_Object=MibScalar
opmen99810bHTTPSMode=_Opmen99810bHTTPSMode_Object((1,3,6,1,4,1,5205,2,94,3,8,1),_Opmen99810bHTTPSMode_Type())
opmen99810bHTTPSMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bHTTPSMode.setStatus(_A)
class _Opmen99810bHTTPSAutoRedirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bHTTPSAutoRedirect_Type.__name__=_C
_Opmen99810bHTTPSAutoRedirect_Object=MibScalar
opmen99810bHTTPSAutoRedirect=_Opmen99810bHTTPSAutoRedirect_Object((1,3,6,1,4,1,5205,2,94,3,8,2),_Opmen99810bHTTPSAutoRedirect_Type())
opmen99810bHTTPSAutoRedirect.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bHTTPSAutoRedirect.setStatus(_A)
_Opmen99810bAuthMethod_ObjectIdentity=ObjectIdentity
opmen99810bAuthMethod=_Opmen99810bAuthMethod_ObjectIdentity((1,3,6,1,4,1,5205,2,94,3,9))
class _Opmen99810bConsoleAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Q,0),(_k,1),(_l,2),(_m,3)))
_Opmen99810bConsoleAuthMethod_Type.__name__=_C
_Opmen99810bConsoleAuthMethod_Object=MibScalar
opmen99810bConsoleAuthMethod=_Opmen99810bConsoleAuthMethod_Object((1,3,6,1,4,1,5205,2,94,3,9,1),_Opmen99810bConsoleAuthMethod_Type())
opmen99810bConsoleAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bConsoleAuthMethod.setStatus(_A)
class _Opmen99810bConsoleFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bConsoleFallback_Type.__name__=_C
_Opmen99810bConsoleFallback_Object=MibScalar
opmen99810bConsoleFallback=_Opmen99810bConsoleFallback_Object((1,3,6,1,4,1,5205,2,94,3,9,2),_Opmen99810bConsoleFallback_Type())
opmen99810bConsoleFallback.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bConsoleFallback.setStatus(_A)
class _Opmen99810bTelnetAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Q,0),(_k,1),(_l,2),(_m,3)))
_Opmen99810bTelnetAuthMethod_Type.__name__=_C
_Opmen99810bTelnetAuthMethod_Object=MibScalar
opmen99810bTelnetAuthMethod=_Opmen99810bTelnetAuthMethod_Object((1,3,6,1,4,1,5205,2,94,3,9,3),_Opmen99810bTelnetAuthMethod_Type())
opmen99810bTelnetAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTelnetAuthMethod.setStatus(_A)
class _Opmen99810bTelnetFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bTelnetFallback_Type.__name__=_C
_Opmen99810bTelnetFallback_Object=MibScalar
opmen99810bTelnetFallback=_Opmen99810bTelnetFallback_Object((1,3,6,1,4,1,5205,2,94,3,9,4),_Opmen99810bTelnetFallback_Type())
opmen99810bTelnetFallback.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bTelnetFallback.setStatus(_A)
class _Opmen99810bSshAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Q,0),(_k,1),(_l,2),(_m,3)))
_Opmen99810bSshAuthMethod_Type.__name__=_C
_Opmen99810bSshAuthMethod_Object=MibScalar
opmen99810bSshAuthMethod=_Opmen99810bSshAuthMethod_Object((1,3,6,1,4,1,5205,2,94,3,9,5),_Opmen99810bSshAuthMethod_Type())
opmen99810bSshAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSshAuthMethod.setStatus(_A)
class _Opmen99810bSshFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bSshFallback_Type.__name__=_C
_Opmen99810bSshFallback_Object=MibScalar
opmen99810bSshFallback=_Opmen99810bSshFallback_Object((1,3,6,1,4,1,5205,2,94,3,9,6),_Opmen99810bSshFallback_Type())
opmen99810bSshFallback.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSshFallback.setStatus(_A)
class _Opmen99810bWebAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Q,0),(_k,1),(_l,2),(_m,3)))
_Opmen99810bWebAuthMethod_Type.__name__=_C
_Opmen99810bWebAuthMethod_Object=MibScalar
opmen99810bWebAuthMethod=_Opmen99810bWebAuthMethod_Object((1,3,6,1,4,1,5205,2,94,3,9,7),_Opmen99810bWebAuthMethod_Type())
opmen99810bWebAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bWebAuthMethod.setStatus(_A)
class _Opmen99810bWebFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bWebFallback_Type.__name__=_C
_Opmen99810bWebFallback_Object=MibScalar
opmen99810bWebFallback=_Opmen99810bWebFallback_Object((1,3,6,1,4,1,5205,2,94,3,9,8),_Opmen99810bWebFallback_Type())
opmen99810bWebFallback.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bWebFallback.setStatus(_A)
_Opmen99810bMaintenance_ObjectIdentity=ObjectIdentity
opmen99810bMaintenance=_Opmen99810bMaintenance_ObjectIdentity((1,3,6,1,4,1,5205,2,94,4))
class _Opmen99810bRestartDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Opmen99810bRestartDevice_Type.__name__=_C
_Opmen99810bRestartDevice_Object=MibScalar
opmen99810bRestartDevice=_Opmen99810bRestartDevice_Object((1,3,6,1,4,1,5205,2,94,4,1),_Opmen99810bRestartDevice_Type())
opmen99810bRestartDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bRestartDevice.setStatus(_A)
_Opmen99810bFirmware_ObjectIdentity=ObjectIdentity
opmen99810bFirmware=_Opmen99810bFirmware_ObjectIdentity((1,3,6,1,4,1,5205,2,94,4,2))
_Opmen99810bFirmwareIpAddress_Type=IpAddress
_Opmen99810bFirmwareIpAddress_Object=MibScalar
opmen99810bFirmwareIpAddress=_Opmen99810bFirmwareIpAddress_Object((1,3,6,1,4,1,5205,2,94,4,2,1),_Opmen99810bFirmwareIpAddress_Type())
opmen99810bFirmwareIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bFirmwareIpAddress.setStatus(_A)
_Opmen99810bFirmwareFileName_Type=DisplayString
_Opmen99810bFirmwareFileName_Object=MibScalar
opmen99810bFirmwareFileName=_Opmen99810bFirmwareFileName_Object((1,3,6,1,4,1,5205,2,94,4,2,2),_Opmen99810bFirmwareFileName_Type())
opmen99810bFirmwareFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bFirmwareFileName.setStatus(_A)
class _Opmen99810bDoFirmwareUpgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_h,0),(_i,1)))
_Opmen99810bDoFirmwareUpgrade_Type.__name__=_C
_Opmen99810bDoFirmwareUpgrade_Object=MibScalar
opmen99810bDoFirmwareUpgrade=_Opmen99810bDoFirmwareUpgrade_Object((1,3,6,1,4,1,5205,2,94,4,2,3),_Opmen99810bDoFirmwareUpgrade_Type())
opmen99810bDoFirmwareUpgrade.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bDoFirmwareUpgrade.setStatus(_A)
_Opmen99810bSaveOrRestore_ObjectIdentity=ObjectIdentity
opmen99810bSaveOrRestore=_Opmen99810bSaveOrRestore_ObjectIdentity((1,3,6,1,4,1,5205,2,94,4,3))
class _Opmen99810bFactoryDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_g,1)))
_Opmen99810bFactoryDefaults_Type.__name__=_C
_Opmen99810bFactoryDefaults_Object=MibScalar
opmen99810bFactoryDefaults=_Opmen99810bFactoryDefaults_Object((1,3,6,1,4,1,5205,2,94,4,3,1),_Opmen99810bFactoryDefaults_Type())
opmen99810bFactoryDefaults.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bFactoryDefaults.setStatus(_A)
class _Opmen99810bSaveStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_g,1)))
_Opmen99810bSaveStart_Type.__name__=_C
_Opmen99810bSaveStart_Object=MibScalar
opmen99810bSaveStart=_Opmen99810bSaveStart_Object((1,3,6,1,4,1,5205,2,94,4,3,2),_Opmen99810bSaveStart_Type())
opmen99810bSaveStart.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSaveStart.setStatus(_A)
class _Opmen99810bSaveUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_g,1)))
_Opmen99810bSaveUser_Type.__name__=_C
_Opmen99810bSaveUser_Object=MibScalar
opmen99810bSaveUser=_Opmen99810bSaveUser_Object((1,3,6,1,4,1,5205,2,94,4,3,3),_Opmen99810bSaveUser_Type())
opmen99810bSaveUser.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bSaveUser.setStatus(_A)
class _Opmen99810bRestoreUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_g,1)))
_Opmen99810bRestoreUser_Type.__name__=_C
_Opmen99810bRestoreUser_Object=MibScalar
opmen99810bRestoreUser=_Opmen99810bRestoreUser_Object((1,3,6,1,4,1,5205,2,94,4,3,4),_Opmen99810bRestoreUser_Type())
opmen99810bRestoreUser.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bRestoreUser.setStatus(_A)
_Opmen99810bExportOrImport_ObjectIdentity=ObjectIdentity
opmen99810bExportOrImport=_Opmen99810bExportOrImport_ObjectIdentity((1,3,6,1,4,1,5205,2,94,4,4))
_Opmen99810bExportIpAddress_Type=IpAddress
_Opmen99810bExportIpAddress_Object=MibScalar
opmen99810bExportIpAddress=_Opmen99810bExportIpAddress_Object((1,3,6,1,4,1,5205,2,94,4,4,1),_Opmen99810bExportIpAddress_Type())
opmen99810bExportIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bExportIpAddress.setStatus(_A)
_Opmen99810bExportConfigName_Type=DisplayString
_Opmen99810bExportConfigName_Object=MibScalar
opmen99810bExportConfigName=_Opmen99810bExportConfigName_Object((1,3,6,1,4,1,5205,2,94,4,4,2),_Opmen99810bExportConfigName_Type())
opmen99810bExportConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bExportConfigName.setStatus(_A)
class _Opmen99810bDoExportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_h,0),(_i,1)))
_Opmen99810bDoExportConfig_Type.__name__=_C
_Opmen99810bDoExportConfig_Object=MibScalar
opmen99810bDoExportConfig=_Opmen99810bDoExportConfig_Object((1,3,6,1,4,1,5205,2,94,4,4,3),_Opmen99810bDoExportConfig_Type())
opmen99810bDoExportConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bDoExportConfig.setStatus(_A)
_Opmen99810bImportIpAddress_Type=IpAddress
_Opmen99810bImportIpAddress_Object=MibScalar
opmen99810bImportIpAddress=_Opmen99810bImportIpAddress_Object((1,3,6,1,4,1,5205,2,94,4,4,4),_Opmen99810bImportIpAddress_Type())
opmen99810bImportIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bImportIpAddress.setStatus(_A)
_Opmen99810bImportConfigName_Type=DisplayString
_Opmen99810bImportConfigName_Object=MibScalar
opmen99810bImportConfigName=_Opmen99810bImportConfigName_Object((1,3,6,1,4,1,5205,2,94,4,4,5),_Opmen99810bImportConfigName_Type())
opmen99810bImportConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bImportConfigName.setStatus(_A)
class _Opmen99810bDoImportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_h,0),(_i,1)))
_Opmen99810bDoImportConfig_Type.__name__=_C
_Opmen99810bDoImportConfig_Object=MibScalar
opmen99810bDoImportConfig=_Opmen99810bDoImportConfig_Object((1,3,6,1,4,1,5205,2,94,4,4,6),_Opmen99810bDoImportConfig_Type())
opmen99810bDoImportConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bDoImportConfig.setStatus(_A)
_Opmen99810bDiagnostics_ObjectIdentity=ObjectIdentity
opmen99810bDiagnostics=_Opmen99810bDiagnostics_ObjectIdentity((1,3,6,1,4,1,5205,2,94,4,5))
_Opmen99810bPingIpAddress_Type=IpAddress
_Opmen99810bPingIpAddress_Object=MibScalar
opmen99810bPingIpAddress=_Opmen99810bPingIpAddress_Object((1,3,6,1,4,1,5205,2,94,4,5,1),_Opmen99810bPingIpAddress_Type())
opmen99810bPingIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPingIpAddress.setStatus(_A)
class _Opmen99810bPingSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,1400))
_Opmen99810bPingSize_Type.__name__=_C
_Opmen99810bPingSize_Object=MibScalar
opmen99810bPingSize=_Opmen99810bPingSize_Object((1,3,6,1,4,1,5205,2,94,4,5,2),_Opmen99810bPingSize_Type())
opmen99810bPingSize.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPingSize.setStatus(_A)
class _Opmen99810bDoPingConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_h,0),(_i,1)))
_Opmen99810bDoPingConfig_Type.__name__=_C
_Opmen99810bDoPingConfig_Object=MibScalar
opmen99810bDoPingConfig=_Opmen99810bDoPingConfig_Object((1,3,6,1,4,1,5205,2,94,4,5,3),_Opmen99810bDoPingConfig_Type())
opmen99810bDoPingConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bDoPingConfig.setStatus(_A)
_Opmen99810bPingResult_Type=DisplayString
_Opmen99810bPingResult_Object=MibScalar
opmen99810bPingResult=_Opmen99810bPingResult_Object((1,3,6,1,4,1,5205,2,94,4,5,4),_Opmen99810bPingResult_Type())
opmen99810bPingResult.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPingResult.setStatus(_A)
_Opmen99810bPing6IpAddress_Type=DisplayString
_Opmen99810bPing6IpAddress_Object=MibScalar
opmen99810bPing6IpAddress=_Opmen99810bPing6IpAddress_Object((1,3,6,1,4,1,5205,2,94,4,5,5),_Opmen99810bPing6IpAddress_Type())
opmen99810bPing6IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPing6IpAddress.setStatus(_A)
class _Opmen99810bPing6Size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,1400))
_Opmen99810bPing6Size_Type.__name__=_C
_Opmen99810bPing6Size_Object=MibScalar
opmen99810bPing6Size=_Opmen99810bPing6Size_Object((1,3,6,1,4,1,5205,2,94,4,5,6),_Opmen99810bPing6Size_Type())
opmen99810bPing6Size.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bPing6Size.setStatus(_A)
class _Opmen99810bDoPing6Config_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_h,0),(_i,1)))
_Opmen99810bDoPing6Config_Type.__name__=_C
_Opmen99810bDoPing6Config_Object=MibScalar
opmen99810bDoPing6Config=_Opmen99810bDoPing6Config_Object((1,3,6,1,4,1,5205,2,94,4,5,7),_Opmen99810bDoPing6Config_Type())
opmen99810bDoPing6Config.setMaxAccess(_B)
if mibBuilder.loadTexts:opmen99810bDoPing6Config.setStatus(_A)
_Opmen99810bPing6Result_Type=DisplayString
_Opmen99810bPing6Result_Object=MibScalar
opmen99810bPing6Result=_Opmen99810bPing6Result_Object((1,3,6,1,4,1,5205,2,94,4,5,8),_Opmen99810bPing6Result_Type())
opmen99810bPing6Result.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bPing6Result.setStatus(_A)
_Opmen99810bTrap_ObjectIdentity=ObjectIdentity
opmen99810bTrap=_Opmen99810bTrap_ObjectIdentity((1,3,6,1,4,1,5205,2,94,5))
_Opmen99810bTrapEvent_ObjectIdentity=ObjectIdentity
opmen99810bTrapEvent=_Opmen99810bTrapEvent_ObjectIdentity((1,3,6,1,4,1,5205,2,94,5,1))
_Opmen99810bTrapVariable_ObjectIdentity=ObjectIdentity
opmen99810bTrapVariable=_Opmen99810bTrapVariable_ObjectIdentity((1,3,6,1,4,1,5205,2,94,5,2))
_Opmen99810bInformation_Type=DisplayString
_Opmen99810bInformation_Object=MibScalar
opmen99810bInformation=_Opmen99810bInformation_Object((1,3,6,1,4,1,5205,2,94,5,2,1),_Opmen99810bInformation_Type())
opmen99810bInformation.setMaxAccess(_D)
if mibBuilder.loadTexts:opmen99810bInformation.setStatus(_A)
opmen99810bEmergency=NotificationType((1,3,6,1,4,1,5205,2,94,5,1,1))
opmen99810bEmergency.setObjects((_G,_V))
if mibBuilder.loadTexts:opmen99810bEmergency.setStatus(_A)
opmen99810bAlert=NotificationType((1,3,6,1,4,1,5205,2,94,5,1,2))
opmen99810bAlert.setObjects((_G,_V))
if mibBuilder.loadTexts:opmen99810bAlert.setStatus(_A)
opmen99810bCritical=NotificationType((1,3,6,1,4,1,5205,2,94,5,1,3))
opmen99810bCritical.setObjects((_G,_V))
if mibBuilder.loadTexts:opmen99810bCritical.setStatus(_A)
opmen99810bError=NotificationType((1,3,6,1,4,1,5205,2,94,5,1,4))
opmen99810bError.setObjects((_G,_V))
if mibBuilder.loadTexts:opmen99810bError.setStatus(_A)
opmen99810bWarning=NotificationType((1,3,6,1,4,1,5205,2,94,5,1,5))
opmen99810bWarning.setObjects((_G,_V))
if mibBuilder.loadTexts:opmen99810bWarning.setStatus(_A)
opmen99810bNotice=NotificationType((1,3,6,1,4,1,5205,2,94,5,1,6))
opmen99810bNotice.setObjects((_G,_V))
if mibBuilder.loadTexts:opmen99810bNotice.setStatus(_A)
opmen99810bInformational=NotificationType((1,3,6,1,4,1,5205,2,94,5,1,7))
opmen99810bInformational.setObjects((_G,_V))
if mibBuilder.loadTexts:opmen99810bInformational.setStatus(_A)
opmen99810bDebug=NotificationType((1,3,6,1,4,1,5205,2,94,5,1,8))
opmen99810bDebug.setObjects((_G,_V))
if mibBuilder.loadTexts:opmen99810bDebug.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'privatetech':privatetech,'switch':switch,'opmen99810bProductId':opmen99810bProductId,'opmen99810bSystem':opmen99810bSystem,'opmen99810bSystemInformation':opmen99810bSystemInformation,'opmen99810bModelName':opmen99810bModelName,'opmen99810bBIOSVersion':opmen99810bBIOSVersion,'opmen99810bFirmwareVersion':opmen99810bFirmwareVersion,'opmen99810bHardwareMechanicalVersion':opmen99810bHardwareMechanicalVersion,'opmen99810bSerialNumber':opmen99810bSerialNumber,'opmen99810bHostMACAddress':opmen99810bHostMACAddress,'opmen99810bConsoleBaudrate':opmen99810bConsoleBaudrate,'opmen99810bRAMSize':opmen99810bRAMSize,'opmen99810bFlashSize':opmen99810bFlashSize,'opmen99810bBridgeFBDSize':opmen99810bBridgeFBDSize,'opmen99810bTransmitQueue':opmen99810bTransmitQueue,'opmen99810bMaximumFrameSize':opmen99810bMaximumFrameSize,'opmen99810bCPULoad':opmen99810bCPULoad,'opmen99810bPowerSource':opmen99810bPowerSource,'opmen99810bSystemTime':opmen99810bSystemTime,'opmen99810bSystemTimeManual':opmen99810bSystemTimeManual,'opmen99810bSystemTimeManualClockSource':opmen99810bSystemTimeManualClockSource,'opmen99810bSystemTimeManualLocaltime':opmen99810bSystemTimeManualLocaltime,'opmen99810bSystemTimeManualTimeZoneOffset':opmen99810bSystemTimeManualTimeZoneOffset,'opmen99810bSystemTimeManualDaylightSavings':opmen99810bSystemTimeManualDaylightSavings,'opmen99810bSystemTimeManualTimeSetOffset':opmen99810bSystemTimeManualTimeSetOffset,'opmen99810bSystemTimeManualDaylightSavingsType':opmen99810bSystemTimeManualDaylightSavingsType,'opmen99810bSystemTimeManualDaylightSavingsBydatesFrom':opmen99810bSystemTimeManualDaylightSavingsBydatesFrom,'opmen99810bSystemTimeManualDaylightSavingsBydatesTo':opmen99810bSystemTimeManualDaylightSavingsBydatesTo,'opmen99810bSystemTimeManualDaylightSavingsRecurringDayFrom':opmen99810bSystemTimeManualDaylightSavingsRecurringDayFrom,'opmen99810bSystemTimeManualDaylightSavingsRecurringWeekFrom':opmen99810bSystemTimeManualDaylightSavingsRecurringWeekFrom,'opmen99810bSystemTimeManualDaylightSavingsRecurringMonthFrom':opmen99810bSystemTimeManualDaylightSavingsRecurringMonthFrom,'opmen99810bSystemTimeManualDaylightSavingsRecurringTimeFrom':opmen99810bSystemTimeManualDaylightSavingsRecurringTimeFrom,'opmen99810bSystemTimeManualDaylightSavingsRecurringDayTo':opmen99810bSystemTimeManualDaylightSavingsRecurringDayTo,'opmen99810bSystemTimeManualDaylightSavingsRecurringWeekTo':opmen99810bSystemTimeManualDaylightSavingsRecurringWeekTo,'opmen99810bSystemTimeManualDaylightSavingsRecurringMonthTo':opmen99810bSystemTimeManualDaylightSavingsRecurringMonthTo,'opmen99810bSystemTimeManualDaylightSavingsRecurringTimeTo':opmen99810bSystemTimeManualDaylightSavingsRecurringTimeTo,'opmen99810bSystemTimeNTP':opmen99810bSystemTimeNTP,'opmen99810bSystemTimeNTPTable':opmen99810bSystemTimeNTPTable,'opmen99810bSystemTimeNTPEntry':opmen99810bSystemTimeNTPEntry,_A0:opmen99810bSystemTimeNTPIndex,'opmen99810bSystemTimeNTPServerIPType':opmen99810bSystemTimeNTPServerIPType,'opmen99810bSystemTimeNTPServer':opmen99810bSystemTimeNTPServer,'opmen99810bSystemTimeNTPCurrentMode':opmen99810bSystemTimeNTPCurrentMode,'opmen99810bSystemAccount':opmen99810bSystemAccount,'opmen99810bSystemAccountUsers':opmen99810bSystemAccountUsers,'opmen99810bSystemAccountUserCreate':opmen99810bSystemAccountUserCreate,'opmen99810bSystemAccountUsersTable':opmen99810bSystemAccountUsersTable,'opmen99810bSystemAccountUsersEntry':opmen99810bSystemAccountUsersEntry,_A1:opmen99810bUserIndex,'opmen99810bUserName':opmen99810bUserName,'opmen99810bPassword':opmen99810bPassword,'opmen99810bUserPrivilegeLevel':opmen99810bUserPrivilegeLevel,'opmen99810bAccountUserRowStatus':opmen99810bAccountUserRowStatus,'opmen99810bSystemAccountPrivilegeLevel':opmen99810bSystemAccountPrivilegeLevel,'opmen99810bAccountPrivilegeLevel':opmen99810bAccountPrivilegeLevel,'opmen99810bAggregationPrivilegeLevel':opmen99810bAggregationPrivilegeLevel,'opmen99810bDiagnosticsPrivilegeLevel':opmen99810bDiagnosticsPrivilegeLevel,'opmen99810bEEEPrivilegeLevel':opmen99810bEEEPrivilegeLevel,'opmen99810bEasyportPrivilegeLevel':opmen99810bEasyportPrivilegeLevel,'opmen99810bGARPPrivilegeLevel':opmen99810bGARPPrivilegeLevel,'opmen99810bGVRPPrivilegeLevel':opmen99810bGVRPPrivilegeLevel,'opmen99810bIPPrivilegeLevel':opmen99810bIPPrivilegeLevel,'opmen99810bIPMCSnoopingPrivilegeLevel':opmen99810bIPMCSnoopingPrivilegeLevel,'opmen99810bLACPPrivilegeLevel':opmen99810bLACPPrivilegeLevel,'opmen99810bLLDPPrivilegeLevel':opmen99810bLLDPPrivilegeLevel,'opmen99810bLLDPMEDPrivilegeLevel':opmen99810bLLDPMEDPrivilegeLevel,'opmen99810bLoopProtectPrivilegeLevel':opmen99810bLoopProtectPrivilegeLevel,'opmen99810bMACTablePrivilegeLevel':opmen99810bMACTablePrivilegeLevel,'opmen99810bMVRPrivilegeLevel':opmen99810bMVRPrivilegeLevel,'opmen99810bMaintenancePrivilegeLevel':opmen99810bMaintenancePrivilegeLevel,'opmen99810bMirroringPrivilegeLevel':opmen99810bMirroringPrivilegeLevel,'opmen99810bPortsPrivilegeLevel':opmen99810bPortsPrivilegeLevel,'opmen99810bPrivateVLANsPrivilegeLevel':opmen99810bPrivateVLANsPrivilegeLevel,'opmen99810bQoSPrivilegeLevel':opmen99810bQoSPrivilegeLevel,'opmen99810bSFlowPrivilegeLevel':opmen99810bSFlowPrivilegeLevel,'opmen99810bSMTPPrivilegeLevel':opmen99810bSMTPPrivilegeLevel,'opmen99810bSNMPPrivilegeLevel':opmen99810bSNMPPrivilegeLevel,'opmen99810bSecurityPrivilegeLevel':opmen99810bSecurityPrivilegeLevel,'opmen99810bSingleIPPrivilegeLevel':opmen99810bSingleIPPrivilegeLevel,'opmen99810bSpanningTreePrivilegeLevel':opmen99810bSpanningTreePrivilegeLevel,'opmen99810bSystemPrivilegeLevel':opmen99810bSystemPrivilegeLevel,'opmen99810bTrapEventPrivilegeLevel':opmen99810bTrapEventPrivilegeLevel,'opmen99810bUPnPPrivilegeLevel':opmen99810bUPnPPrivilegeLevel,'opmen99810bVCLPrivilegeLevel':opmen99810bVCLPrivilegeLevel,'opmen99810bVLANsPrivilegeLevel':opmen99810bVLANsPrivilegeLevel,'opmen99810bVoiceVLANPrivilegeLevel':opmen99810bVoiceVLANPrivilegeLevel,'opmen99810bIP':opmen99810bIP,'opmen99810bIPv4':opmen99810bIPv4,'opmen99810bIPv4Configured':opmen99810bIPv4Configured,'opmen99810bIpv4DHCPClient':opmen99810bIpv4DHCPClient,'opmen99810bIPv4Address':opmen99810bIPv4Address,'opmen99810bIPv4Mask':opmen99810bIPv4Mask,'opmen99810bIPv4Gateway':opmen99810bIPv4Gateway,'opmen99810bIPv4VLANId':opmen99810bIPv4VLANId,'opmen99810bIPv4DNSServer':opmen99810bIPv4DNSServer,'opmen99810bIPv4DNSProxy':opmen99810bIPv4DNSProxy,'opmen99810bIPv4Current':opmen99810bIPv4Current,'opmen99810bIpv4CurrentDHCPClient':opmen99810bIpv4CurrentDHCPClient,'opmen99810bIPv4CurrentAddress':opmen99810bIPv4CurrentAddress,'opmen99810bIPv4CurrentMask':opmen99810bIPv4CurrentMask,'opmen99810bIPv4CurrentGateway':opmen99810bIPv4CurrentGateway,'opmen99810bIPv4CurrentVLANId':opmen99810bIPv4CurrentVLANId,'opmen99810bIPv4CurrentDNSServer':opmen99810bIPv4CurrentDNSServer,'opmen99810bIPv6':opmen99810bIPv6,'opmen99810bIPv6Configured':opmen99810bIPv6Configured,'opmen99810bIpv6AutoConfiguration':opmen99810bIpv6AutoConfiguration,'opmen99810bIpv6Address':opmen99810bIpv6Address,'opmen99810bIpv6Prefix':opmen99810bIpv6Prefix,'opmen99810bIpv6Gateway':opmen99810bIpv6Gateway,'opmen99810bIPv6Current':opmen99810bIPv6Current,'opmen99810bIpv6CurrentAutoConfiguration':opmen99810bIpv6CurrentAutoConfiguration,'opmen99810bIpv6CurrentAddress':opmen99810bIpv6CurrentAddress,'opmen99810bIpv6CurrentLinkLocalAddress':opmen99810bIpv6CurrentLinkLocalAddress,'opmen99810bIpv6CurrentPrefix':opmen99810bIpv6CurrentPrefix,'opmen99810bIpv6CurrentGateway':opmen99810bIpv6CurrentGateway,'opmen99810bSyslog':opmen99810bSyslog,'opmen99810bSyslogConf':opmen99810bSyslogConf,'opmen99810bServerMode':opmen99810bServerMode,'opmen99810bServerAddress1':opmen99810bServerAddress1,'opmen99810bServerAddress2':opmen99810bServerAddress2,'opmen99810bSyslogLevel':opmen99810bSyslogLevel,'opmen99810bSyslogDetailedInfo':opmen99810bSyslogDetailedInfo,'opmen99810bSyslogDetailedInfoClear':opmen99810bSyslogDetailedInfoClear,'opmen99810bSyslogDetailedInfoTable':opmen99810bSyslogDetailedInfoTable,'opmen99810bSyslogDetailedInfoEntry':opmen99810bSyslogDetailedInfoEntry,_A2:opmen99810bSyslogDetailedInfoIndex,'opmen99810bSyslogDetailedInfoLevel':opmen99810bSyslogDetailedInfoLevel,'opmen99810bSyslogDetailedInfoTime':opmen99810bSyslogDetailedInfoTime,'opmen99810bSyslogDetailedInfoMessage':opmen99810bSyslogDetailedInfoMessage,'opmen99810bSnmp':opmen99810bSnmp,'opmen99810bSnmpConf':opmen99810bSnmpConf,'opmen99810bGetCommunity':opmen99810bGetCommunity,'opmen99810bSetCommunityMode':opmen99810bSetCommunityMode,'opmen99810bSetCommunity':opmen99810bSetCommunity,'opmen99810bTrapHostConfTable':opmen99810bTrapHostConfTable,'opmen99810bTrapHostConfEntry':opmen99810bTrapHostConfEntry,_A3:opmen99810bTrapHostConfIndex,'opmen99810bTrapHostConfVersion':opmen99810bTrapHostConfVersion,'opmen99810bTrapHostConfIPType':opmen99810bTrapHostConfIPType,'opmen99810bTrapHostConfIP':opmen99810bTrapHostConfIP,'opmen99810bTrapHostConfPort':opmen99810bTrapHostConfPort,'opmen99810bTrapHostConfCommunity':opmen99810bTrapHostConfCommunity,'opmen99810bTrapHostConfSeverityLevel':opmen99810bTrapHostConfSeverityLevel,'opmen99810bTrapHostConfSecurityLevel':opmen99810bTrapHostConfSecurityLevel,'opmen99810bTrapHostConfAuthPtc':opmen99810bTrapHostConfAuthPtc,'opmen99810bTrapHostConfAuthPassword':opmen99810bTrapHostConfAuthPassword,'opmen99810bTrapHostConfPrivPtc':opmen99810bTrapHostConfPrivPtc,'opmen99810bTrapHostConfPrivPassword':opmen99810bTrapHostConfPrivPassword,'opmen99810bTrapHostConfCurrentMode':opmen99810bTrapHostConfCurrentMode,'opmen99810bConfiguration':opmen99810bConfiguration,'opmen99810bPort':opmen99810bPort,'opmen99810bPortConfigurationTable':opmen99810bPortConfigurationTable,'opmen99810bPortConfigurationEntry':opmen99810bPortConfigurationEntry,_A4:opmen99810bPortConfPort,'opmen99810bPortConfPortMedia':opmen99810bPortConfPortMedia,'opmen99810bPortConfLink':opmen99810bPortConfLink,'opmen99810bPortConfCurrentSpeed':opmen99810bPortConfCurrentSpeed,'opmen99810bPortConfSpeed':opmen99810bPortConfSpeed,'opmen99810bPortConfCurrentFlowControlRx':opmen99810bPortConfCurrentFlowControlRx,'opmen99810bPortConfCurrentFlowControlTx':opmen99810bPortConfCurrentFlowControlTx,'opmen99810bPortConfFlowControl':opmen99810bPortConfFlowControl,'opmen99810bPortConfMaxFrameSize':opmen99810bPortConfMaxFrameSize,'opmen99810bPortConfExcessiveCollisionMode':opmen99810bPortConfExcessiveCollisionMode,'opmen99810bPortConfPowerControl':opmen99810bPortConfPowerControl,'opmen99810bPortConfDescription':opmen99810bPortConfDescription,'opmen99810bPortTrafficStatisticsTable':opmen99810bPortTrafficStatisticsTable,'opmen99810bPortTrafficStatisticsEntry':opmen99810bPortTrafficStatisticsEntry,_A5:opmen99810bPortTrafficStatisticsPort,'opmen99810bPortTrafficStatisticsClear':opmen99810bPortTrafficStatisticsClear,'opmen99810bPortTrafficRxPackets':opmen99810bPortTrafficRxPackets,'opmen99810bPortTrafficRxOctets':opmen99810bPortTrafficRxOctets,'opmen99810bPortTrafficRxUnicast':opmen99810bPortTrafficRxUnicast,'opmen99810bPortTrafficRxMulticast':opmen99810bPortTrafficRxMulticast,'opmen99810bPortTrafficRxBroadcast':opmen99810bPortTrafficRxBroadcast,'opmen99810bPortTrafficRxPause':opmen99810bPortTrafficRxPause,'opmen99810bPortTrafficRx64Bytes':opmen99810bPortTrafficRx64Bytes,'opmen99810bPortTrafficRx65to127Bytes':opmen99810bPortTrafficRx65to127Bytes,'opmen99810bPortTrafficRx128to255Bytes':opmen99810bPortTrafficRx128to255Bytes,'opmen99810bPortTrafficRx256to511Bytes':opmen99810bPortTrafficRx256to511Bytes,'opmen99810bPortTrafficRx512to1023Bytes':opmen99810bPortTrafficRx512to1023Bytes,'opmen99810bPortTrafficRx1024to1526Bytes':opmen99810bPortTrafficRx1024to1526Bytes,'opmen99810bPortTrafficRxExceecd1527Bytes':opmen99810bPortTrafficRxExceecd1527Bytes,'opmen99810bPortTrafficRxQ0':opmen99810bPortTrafficRxQ0,'opmen99810bPortTrafficRxQ1':opmen99810bPortTrafficRxQ1,'opmen99810bPortTrafficRxQ2':opmen99810bPortTrafficRxQ2,'opmen99810bPortTrafficRxQ3':opmen99810bPortTrafficRxQ3,'opmen99810bPortTrafficRxQ4':opmen99810bPortTrafficRxQ4,'opmen99810bPortTrafficRxQ5':opmen99810bPortTrafficRxQ5,'opmen99810bPortTrafficRxQ6':opmen99810bPortTrafficRxQ6,'opmen99810bPortTrafficRxQ7':opmen99810bPortTrafficRxQ7,'opmen99810bPortTrafficRxDrops':opmen99810bPortTrafficRxDrops,'opmen99810bPortTrafficRxCRCorAlignment':opmen99810bPortTrafficRxCRCorAlignment,'opmen99810bPortTrafficRxUndersize':opmen99810bPortTrafficRxUndersize,'opmen99810bPortTrafficRxOversize':opmen99810bPortTrafficRxOversize,'opmen99810bPortTrafficRxFragments':opmen99810bPortTrafficRxFragments,'opmen99810bPortTrafficRxJabber':opmen99810bPortTrafficRxJabber,'opmen99810bPortTrafficRxFiltered':opmen99810bPortTrafficRxFiltered,'opmen99810bPortTrafficTxPackets':opmen99810bPortTrafficTxPackets,'opmen99810bPortTrafficTxOctets':opmen99810bPortTrafficTxOctets,'opmen99810bPortTrafficTxUnicast':opmen99810bPortTrafficTxUnicast,'opmen99810bPortTrafficTxMulticast':opmen99810bPortTrafficTxMulticast,'opmen99810bPortTrafficTxBroadcast':opmen99810bPortTrafficTxBroadcast,'opmen99810bPortTrafficTxPause':opmen99810bPortTrafficTxPause,'opmen99810bPortTrafficTx64Bytes':opmen99810bPortTrafficTx64Bytes,'opmen99810bPortTrafficTx65to127Bytes':opmen99810bPortTrafficTx65to127Bytes,'opmen99810bPortTrafficTx128to255Bytes':opmen99810bPortTrafficTx128to255Bytes,'opmen99810bPortTrafficTx256to511Bytes':opmen99810bPortTrafficTx256to511Bytes,'opmen99810bPortTrafficTx512to1023Bytes':opmen99810bPortTrafficTx512to1023Bytes,'opmen99810bPortTrafficTx1024to1526Bytes':opmen99810bPortTrafficTx1024to1526Bytes,'opmen99810bPortTrafficTxExceecd1527Bytes':opmen99810bPortTrafficTxExceecd1527Bytes,'opmen99810bPortTrafficTxQ0':opmen99810bPortTrafficTxQ0,'opmen99810bPortTrafficTxQ1':opmen99810bPortTrafficTxQ1,'opmen99810bPortTrafficTxQ2':opmen99810bPortTrafficTxQ2,'opmen99810bPortTrafficTxQ3':opmen99810bPortTrafficTxQ3,'opmen99810bPortTrafficTxQ4':opmen99810bPortTrafficTxQ4,'opmen99810bPortTrafficTxQ5':opmen99810bPortTrafficTxQ5,'opmen99810bPortTrafficTxQ6':opmen99810bPortTrafficTxQ6,'opmen99810bPortTrafficTxQ7':opmen99810bPortTrafficTxQ7,'opmen99810bPortTrafficTxDrops':opmen99810bPortTrafficTxDrops,'opmen99810bPortTrafficTxLateOrExcColl':opmen99810bPortTrafficTxLateOrExcColl,'opmen99810bPortQoSStatistics':opmen99810bPortQoSStatistics,'opmen99810bPortQoSStatisticsClear':opmen99810bPortQoSStatisticsClear,'opmen99810bPortQoSStatisticsTable':opmen99810bPortQoSStatisticsTable,'opmen99810bPortQoSStatisticsEntry':opmen99810bPortQoSStatisticsEntry,_A6:opmen99810bPortQoSStatisticsPort,'opmen99810bPortQoSQ0Rx':opmen99810bPortQoSQ0Rx,'opmen99810bPortQoSQ0Tx':opmen99810bPortQoSQ0Tx,'opmen99810bPortQoSQ1Rx':opmen99810bPortQoSQ1Rx,'opmen99810bPortQoSQ1Tx':opmen99810bPortQoSQ1Tx,'opmen99810bPortQoSQ2Rx':opmen99810bPortQoSQ2Rx,'opmen99810bPortQoSQ2Tx':opmen99810bPortQoSQ2Tx,'opmen99810bPortQoSQ3Rx':opmen99810bPortQoSQ3Rx,'opmen99810bPortQoSQ3Tx':opmen99810bPortQoSQ3Tx,'opmen99810bPortQoSQ4Rx':opmen99810bPortQoSQ4Rx,'opmen99810bPortQoSQ4Tx':opmen99810bPortQoSQ4Tx,'opmen99810bPortQoSQ5Rx':opmen99810bPortQoSQ5Rx,'opmen99810bPortQoSQ5Tx':opmen99810bPortQoSQ5Tx,'opmen99810bPortQoSQ6Rx':opmen99810bPortQoSQ6Rx,'opmen99810bPortQoSQ6Tx':opmen99810bPortQoSQ6Tx,'opmen99810bPortQoSQ7Rx':opmen99810bPortQoSQ7Rx,'opmen99810bPortQoSQ7Tx':opmen99810bPortQoSQ7Tx,'opmen99810bSFPInfoTable':opmen99810bSFPInfoTable,'opmen99810bSFPInfoEntry':opmen99810bSFPInfoEntry,_A7:opmen99810bSFPInfoIndex,'opmen99810bSFPInfoPort':opmen99810bSFPInfoPort,'opmen99810bSFPConnectorType':opmen99810bSFPConnectorType,'opmen99810bSFPFiberType':opmen99810bSFPFiberType,'opmen99810bSFPTxCentralWavelength':opmen99810bSFPTxCentralWavelength,'opmen99810bSFPBaudRate':opmen99810bSFPBaudRate,'opmen99810bSFPVendorOUI':opmen99810bSFPVendorOUI,'opmen99810bSFPVendorName':opmen99810bSFPVendorName,'opmen99810bSFPVendorPN':opmen99810bSFPVendorPN,'opmen99810bSFPVendorRev':opmen99810bSFPVendorRev,'opmen99810bSFPVendorSN':opmen99810bSFPVendorSN,'opmen99810bSFPDateCode':opmen99810bSFPDateCode,'opmen99810bSFPTemperature':opmen99810bSFPTemperature,'opmen99810bSFPVcc':opmen99810bSFPVcc,'opmen99810bSFPMon1Bias':opmen99810bSFPMon1Bias,'opmen99810bSFPMon2TxPWR':opmen99810bSFPMon2TxPWR,'opmen99810bSFPMon3RxPWR':opmen99810bSFPMon3RxPWR,'opmen99810bPortEEETable':opmen99810bPortEEETable,'opmen99810bPortEEEEntry':opmen99810bPortEEEEntry,_A8:opmen99810bPortEEEPort,'opmen99810bPortEEEMode':opmen99810bPortEEEMode,'opmen99810bPortEEEUrgentQueue1':opmen99810bPortEEEUrgentQueue1,'opmen99810bPortEEEUrgentQueue2':opmen99810bPortEEEUrgentQueue2,'opmen99810bPortEEEUrgentQueue3':opmen99810bPortEEEUrgentQueue3,'opmen99810bPortEEEUrgentQueue4':opmen99810bPortEEEUrgentQueue4,'opmen99810bPortEEEUrgentQueue5':opmen99810bPortEEEUrgentQueue5,'opmen99810bPortEEEUrgentQueue6':opmen99810bPortEEEUrgentQueue6,'opmen99810bPortEEEUrgentQueue7':opmen99810bPortEEEUrgentQueue7,'opmen99810bPortEEEUrgentQueue8':opmen99810bPortEEEUrgentQueue8,'opmen99810bVoiceVLAN':opmen99810bVoiceVLAN,'opmen99810bVoiceVLANConf':opmen99810bVoiceVLANConf,'opmen99810bVoiceVLANMode':opmen99810bVoiceVLANMode,'opmen99810bVoiceVLANVLANId':opmen99810bVoiceVLANVLANId,'opmen99810bVoiceVLANAgingTime':opmen99810bVoiceVLANAgingTime,'opmen99810bVoiceVLANTrafficClass':opmen99810bVoiceVLANTrafficClass,'opmen99810bVoiceVLANPortTable':opmen99810bVoiceVLANPortTable,'opmen99810bVoiceVLANPortEntry':opmen99810bVoiceVLANPortEntry,_A9:opmen99810bVoiceVLANPort,'opmen99810bVoiceVLANPortMode':opmen99810bVoiceVLANPortMode,'opmen99810bVoiceVLANPortSecurity':opmen99810bVoiceVLANPortSecurity,'opmen99810bVoiceVLANPortDiscoveryProtocol':opmen99810bVoiceVLANPortDiscoveryProtocol,'opmen99810bVoiceVLANOUI':opmen99810bVoiceVLANOUI,'opmen99810bVoiceVLANOUICreate':opmen99810bVoiceVLANOUICreate,'opmen99810bVoiceVLANOUITable':opmen99810bVoiceVLANOUITable,'opmen99810bVoiceVLANOUIEntry':opmen99810bVoiceVLANOUIEntry,_AA:opmen99810bVoiceVLANOUIIndex,'opmen99810bVoiceVLANTelephonyOUI':opmen99810bVoiceVLANTelephonyOUI,'opmen99810bVoiceVLANDescription':opmen99810bVoiceVLANDescription,'opmen99810bVoiceVLANOUIRowStatus':opmen99810bVoiceVLANOUIRowStatus,'opmen99810bGARP':opmen99810bGARP,'opmen99810bGARPConfTable':opmen99810bGARPConfTable,'opmen99810bGARPConfEntry':opmen99810bGARPConfEntry,_AB:opmen99810bGARPConfPort,'opmen99810bGARPJoinTimer':opmen99810bGARPJoinTimer,'opmen99810bGARPLeaveTimer':opmen99810bGARPLeaveTimer,'opmen99810bGARPLeaveAllTimer':opmen99810bGARPLeaveAllTimer,'opmen99810bGARPApplicantion':opmen99810bGARPApplicantion,'opmen99810bGARPAttributeType':opmen99810bGARPAttributeType,'opmen99810bGARPApplicant':opmen99810bGARPApplicant,'opmen99810bGARPStatisticsTable':opmen99810bGARPStatisticsTable,'opmen99810bGARPStatisticsEntry':opmen99810bGARPStatisticsEntry,_AC:opmen99810bGARPStatisticsPort,'opmen99810bGARPStatisticsPeerMAC':opmen99810bGARPStatisticsPeerMAC,'opmen99810bGARPStatisticsFailedCount':opmen99810bGARPStatisticsFailedCount,'opmen99810bGVRP':opmen99810bGVRP,'opmen99810bGVRPConf':opmen99810bGVRPConf,'opmen99810bGVRPMode':opmen99810bGVRPMode,'opmen99810bGVRPConfTable':opmen99810bGVRPConfTable,'opmen99810bGVRPConfEntry':opmen99810bGVRPConfEntry,_AD:opmen99810bGVRPConfPort,'opmen99810bGVRPConfPortMode':opmen99810bGVRPConfPortMode,'opmen99810bGVRPConfPortRRole':opmen99810bGVRPConfPortRRole,'opmen99810bGVRPStatisticsTable':opmen99810bGVRPStatisticsTable,'opmen99810bGVRPStatisticsEntry':opmen99810bGVRPStatisticsEntry,_AE:opmen99810bGVRPStatisticsPort,'opmen99810bGVRPStatisticsJoinTxCnt':opmen99810bGVRPStatisticsJoinTxCnt,'opmen99810bGVRPStatisticsLeaveTxCnt':opmen99810bGVRPStatisticsLeaveTxCnt,'opmen99810bMirroring':opmen99810bMirroring,'opmen99810bPortToMirrorOn':opmen99810bPortToMirrorOn,'opmen99810bMirrorTable':opmen99810bMirrorTable,'opmen99810bMirrorEntry':opmen99810bMirrorEntry,_AF:opmen99810bMirrorPort,'opmen99810bMirrorMode':opmen99810bMirrorMode,'opmen99810bTrapEventSeverity':opmen99810bTrapEventSeverity,'opmen99810bTrapEventSeverityACL':opmen99810bTrapEventSeverityACL,'opmen99810bTrapEventSeverityACLLog':opmen99810bTrapEventSeverityACLLog,'opmen99810bTrapEventSeverityAccessMgmt':opmen99810bTrapEventSeverityAccessMgmt,'opmen99810bTrapEventSeverityAuthFailed':opmen99810bTrapEventSeverityAuthFailed,'opmen99810bTrapEventSeverityColdStart':opmen99810bTrapEventSeverityColdStart,'opmen99810bTrapEventSeverityConfigInfo':opmen99810bTrapEventSeverityConfigInfo,'opmen99810bTrapEventSeverityFirmwareUpgrade':opmen99810bTrapEventSeverityFirmwareUpgrade,'opmen99810bTrapEventSeverityImportExport':opmen99810bTrapEventSeverityImportExport,'opmen99810bTrapEventSeverityLACP':opmen99810bTrapEventSeverityLACP,'opmen99810bTrapEventSeverityLinkStatus':opmen99810bTrapEventSeverityLinkStatus,'opmen99810bTrapEventSeverityLogin':opmen99810bTrapEventSeverityLogin,'opmen99810bTrapEventSeverityLogout':opmen99810bTrapEventSeverityLogout,'opmen99810bTrapEventSeverityLoopProtect':opmen99810bTrapEventSeverityLoopProtect,'opmen99810bTrapEventSeverityMgmtIPChange':opmen99810bTrapEventSeverityMgmtIPChange,'opmen99810bTrapEventSeverityModuleChange':opmen99810bTrapEventSeverityModuleChange,'opmen99810bTrapEventSeverityNAS':opmen99810bTrapEventSeverityNAS,'opmen99810bTrapEventSeverityPasswordChange':opmen99810bTrapEventSeverityPasswordChange,'opmen99810bTrapEventSeverityPortSecurity':opmen99810bTrapEventSeverityPortSecurity,'opmen99810bTrapEventSeverityVLAN':opmen99810bTrapEventSeverityVLAN,'opmen99810bTrapEventSeverityWarmStart':opmen99810bTrapEventSeverityWarmStart,'opmen99810bSMTP':opmen99810bSMTP,'opmen99810bSMTPMailServer':opmen99810bSMTPMailServer,'opmen99810bSMTPUserName':opmen99810bSMTPUserName,'opmen99810bSMTPPassword':opmen99810bSMTPPassword,'opmen99810bSMTPServeriryLevel':opmen99810bSMTPServeriryLevel,'opmen99810bSMTPSender':opmen99810bSMTPSender,'opmen99810bSMTPReturnPath':opmen99810bSMTPReturnPath,'opmen99810bSMTPPort':opmen99810bSMTPPort,'opmen99810bSMTPEmailAddress1':opmen99810bSMTPEmailAddress1,'opmen99810bSMTPEmailAddress2':opmen99810bSMTPEmailAddress2,'opmen99810bSMTPEmailAddress3':opmen99810bSMTPEmailAddress3,'opmen99810bSMTPEmailAddress4':opmen99810bSMTPEmailAddress4,'opmen99810bSMTPEmailAddress5':opmen99810bSMTPEmailAddress5,'opmen99810bSMTPEmailAddress6':opmen99810bSMTPEmailAddress6,'opmen99810bACL':opmen99810bACL,'opmen99810bACLPortsConfTable':opmen99810bACLPortsConfTable,'opmen99810bACLPortsConfEntry':opmen99810bACLPortsConfEntry,_AG:opmen99810bACLPortsConfPort,'opmen99810bACLPortsConfPolicyID':opmen99810bACLPortsConfPolicyID,'opmen99810bACLPortsConfAction':opmen99810bACLPortsConfAction,'opmen99810bACLPortsConfRateLimiterID':opmen99810bACLPortsConfRateLimiterID,'opmen99810bACLPortsConfPortRedirect':opmen99810bACLPortsConfPortRedirect,'opmen99810bACLPortsConfMirror':opmen99810bACLPortsConfMirror,'opmen99810bACLPortsConfLogging':opmen99810bACLPortsConfLogging,'opmen99810bACLPortsConfShutdown':opmen99810bACLPortsConfShutdown,'opmen99810bACLPortsConfState':opmen99810bACLPortsConfState,'opmen99810bACLPortsConfCounter':opmen99810bACLPortsConfCounter,'opmen99810bACLRateLimiterTable':opmen99810bACLRateLimiterTable,'opmen99810bACLRateLimiterEntry':opmen99810bACLRateLimiterEntry,_AH:opmen99810bACLRateLimiterID,'opmen99810bACLRateLimiterUnit':opmen99810bACLRateLimiterUnit,'opmen99810bACLRateLimiterRate':opmen99810bACLRateLimiterRate,'opmen99810bACLACE':opmen99810bACLACE,'opmen99810bACLACECreate':opmen99810bACLACECreate,'opmen99810bACLACETable':opmen99810bACLACETable,'opmen99810bACLACEEntry':opmen99810bACLACEEntry,_AI:opmen99810bACLACEIndex,'opmen99810bACLACEID':opmen99810bACLACEID,'opmen99810bACLACENextID':opmen99810bACLACENextID,'opmen99810bACLACEIngressPort':opmen99810bACLACEIngressPort,'opmen99810bACLACEPortPolicyNumber':opmen99810bACLACEPortPolicyNumber,'opmen99810bACLACEPortPolicyBitmask':opmen99810bACLACEPortPolicyBitmask,'opmen99810bACLACEFrameType':opmen99810bACLACEFrameType,'opmen99810bACLACEAction':opmen99810bACLACEAction,'opmen99810bACLACEDenyPortRedirect':opmen99810bACLACEDenyPortRedirect,'opmen99810bACLACELogging':opmen99810bACLACELogging,'opmen99810bACLACEMirror':opmen99810bACLACEMirror,'opmen99810bACLACERateLimiter':opmen99810bACLACERateLimiter,'opmen99810bACLACEShutdown':opmen99810bACLACEShutdown,'opmen99810bACLACEVLAN8021QTagged':opmen99810bACLACEVLAN8021QTagged,'opmen99810bACLACEVLANTagPriority':opmen99810bACLACEVLANTagPriority,'opmen99810bACLACEVLANVID':opmen99810bACLACEVLANVID,'opmen99810bACLACEEtherType':opmen99810bACLACEEtherType,'opmen99810bACLACESMAC':opmen99810bACLACESMAC,'opmen99810bACLACEDMACType':opmen99810bACLACEDMACType,'opmen99810bACLACEDMAC':opmen99810bACLACEDMAC,'opmen99810bACLACEArpOpcode':opmen99810bACLACEArpOpcode,'opmen99810bACLACEArpFlagsRequestReply':opmen99810bACLACEArpFlagsRequestReply,'opmen99810bACLACEArpFlagsArpSmac':opmen99810bACLACEArpFlagsArpSmac,'opmen99810bACLACEArpFlagsRarpDmac':opmen99810bACLACEArpFlagsRarpDmac,'opmen99810bACLACEArpFlagsLength':opmen99810bACLACEArpFlagsLength,'opmen99810bACLACEArpFlagsIp':opmen99810bACLACEArpFlagsIp,'opmen99810bACLACEArpFlagsEthernet':opmen99810bACLACEArpFlagsEthernet,'opmen99810bACLACESIPType':opmen99810bACLACESIPType,'opmen99810bACLACESIPIPAddress':opmen99810bACLACESIPIPAddress,'opmen99810bACLACESIPNetworkPrefix':opmen99810bACLACESIPNetworkPrefix,'opmen99810bACLACEDIPType':opmen99810bACLACEDIPType,'opmen99810bACLACEDIPIPAddress':opmen99810bACLACEDIPIPAddress,'opmen99810bACLACEDIPNetworkPrefix':opmen99810bACLACEDIPNetworkPrefix,'opmen99810bACLACEIPProtocol':opmen99810bACLACEIPProtocol,'opmen99810bACLACEIPFlagsTTL':opmen99810bACLACEIPFlagsTTL,'opmen99810bACLACEIPFlagsOptions':opmen99810bACLACEIPFlagsOptions,'opmen99810bACLACEIPFlagsFragment':opmen99810bACLACEIPFlagsFragment,'opmen99810bACLACEICMPType':opmen99810bACLACEICMPType,'opmen99810bACLACEICMPCode':opmen99810bACLACEICMPCode,'opmen99810bACLACESourcePortMin':opmen99810bACLACESourcePortMin,'opmen99810bACLACESourcePortMax':opmen99810bACLACESourcePortMax,'opmen99810bACLACEDestPortMin':opmen99810bACLACEDestPortMin,'opmen99810bACLACEDestPortMax':opmen99810bACLACEDestPortMax,'opmen99810bACLACETCPFlagsFin':opmen99810bACLACETCPFlagsFin,'opmen99810bACLACETCPFlagsSyn':opmen99810bACLACETCPFlagsSyn,'opmen99810bACLACETCPFlagsRst':opmen99810bACLACETCPFlagsRst,'opmen99810bACLACETCPFlagsPsh':opmen99810bACLACETCPFlagsPsh,'opmen99810bACLACETCPFlagsAck':opmen99810bACLACETCPFlagsAck,'opmen99810bACLACETCPFlagsUrg':opmen99810bACLACETCPFlagsUrg,'opmen99810bACLACERowStatus':opmen99810bACLACERowStatus,'opmen99810bACLACEClear':opmen99810bACLACEClear,'opmen99810bACLACEMoveACEID':opmen99810bACLACEMoveACEID,'opmen99810bACLACEMoveNextACEID':opmen99810bACLACEMoveNextACEID,'opmen99810bACLACEStatusTable':opmen99810bACLACEStatusTable,'opmen99810bACLACEStatusEntry':opmen99810bACLACEStatusEntry,_AJ:opmen99810bACLACEStatusIndex,'opmen99810bACLACEStatusUser':opmen99810bACLACEStatusUser,'opmen99810bACLACEStatusID':opmen99810bACLACEStatusID,'opmen99810bACLACEStatusIngressPort':opmen99810bACLACEStatusIngressPort,'opmen99810bACLACEStatusFrameType':opmen99810bACLACEStatusFrameType,'opmen99810bACLACEStatusAction':opmen99810bACLACEStatusAction,'opmen99810bACLACEStatusRateLimiter':opmen99810bACLACEStatusRateLimiter,'opmen99810bACLACEStatusPortCopy':opmen99810bACLACEStatusPortCopy,'opmen99810bACLACEStatusMirror':opmen99810bACLACEStatusMirror,'opmen99810bACLACEStatusCPU':opmen99810bACLACEStatusCPU,'opmen99810bACLACEStatusCounter':opmen99810bACLACEStatusCounter,'opmen99810bACLACEStatusConflict':opmen99810bACLACEStatusConflict,'opmen99810bBroadcastStormProtection':opmen99810bBroadcastStormProtection,'opmen99810bBroadcastStormProtectionConfigurationTable':opmen99810bBroadcastStormProtectionConfigurationTable,'opmen99810bBroadcastStormProtectionConfigurationEntry':opmen99810bBroadcastStormProtectionConfigurationEntry,_AK:opmen99810bBroadcastStormProtectionConfPort,'opmen99810bBroadcastStormProtectionConfMode':opmen99810bBroadcastStormProtectionConfMode,'opmen99810bBroadcastStormProtectionConfAction':opmen99810bBroadcastStormProtectionConfAction,'opmen99810bBroadcastStormProtectionConfPPS':opmen99810bBroadcastStormProtectionConfPPS,'opmen99810bBroadcastStormProtectionConfTimer':opmen99810bBroadcastStormProtectionConfTimer,'opmen99810bBroadcastStormProtectionConfstatus':opmen99810bBroadcastStormProtectionConfstatus,'opmen99810bLoopProtection':opmen99810bLoopProtection,'opmen99810bLoopProtectionConfig':opmen99810bLoopProtectionConfig,'opmen99810bLoopProtectionGlobalEnable':opmen99810bLoopProtectionGlobalEnable,'opmen99810bLoopProtectionTranmisstionTime':opmen99810bLoopProtectionTranmisstionTime,'opmen99810bLoopProtectionShutdownTime':opmen99810bLoopProtectionShutdownTime,'opmen99810bLoopProtectionConfigurationTable':opmen99810bLoopProtectionConfigurationTable,'opmen99810bLoopProtectionConfigurationEntry':opmen99810bLoopProtectionConfigurationEntry,_AL:opmen99810bLoopProtectionConfPort,'opmen99810bLoopProtectionConfEnable':opmen99810bLoopProtectionConfEnable,'opmen99810bLoopProtectionConfAction':opmen99810bLoopProtectionConfAction,'opmen99810bLoopProtectionConfTxmode':opmen99810bLoopProtectionConfTxmode,'opmen99810bLoopProtectionStatusTable':opmen99810bLoopProtectionStatusTable,'opmen99810bLoopProtectionStatusEntry':opmen99810bLoopProtectionStatusEntry,_AM:opmen99810bLoopProtectionStatusPort,'opmen99810bLoopProtectionStatusAction':opmen99810bLoopProtectionStatusAction,'opmen99810bLoopProtectionStatusTransmit':opmen99810bLoopProtectionStatusTransmit,'opmen99810bLoopProtectionStatusLoops':opmen99810bLoopProtectionStatusLoops,'opmen99810bLoopProtectionStatusStatus':opmen99810bLoopProtectionStatusStatus,'opmen99810bLoopProtectionStatusLoop':opmen99810bLoopProtectionStatusLoop,'opmen99810bLoopProtectionStatusTimeLastLoop':opmen99810bLoopProtectionStatusTimeLastLoop,'opmen99810bQos':opmen99810bQos,'opmen99810bQosPortClassification':opmen99810bQosPortClassification,'opmen99810bQosPortClassificationTable':opmen99810bQosPortClassificationTable,'opmen99810bQosPortClassificationEntry':opmen99810bQosPortClassificationEntry,_AN:opmen99810bQosPortClassificationPort,'opmen99810bQosPortClassificationQoSclass':opmen99810bQosPortClassificationQoSclass,'opmen99810bQosPortClassificationDPlevel':opmen99810bQosPortClassificationDPlevel,'opmen99810bQosPortClassificationPCP':opmen99810bQosPortClassificationPCP,'opmen99810bQosPortClassificationDEI':opmen99810bQosPortClassificationDEI,'opmen99810bQosPortClassificationTagClass':opmen99810bQosPortClassificationTagClass,'opmen99810bQosPortClassificationDSCPBased':opmen99810bQosPortClassificationDSCPBased,'opmen99810bQoSIngressPortTagClassificationTable':opmen99810bQoSIngressPortTagClassificationTable,'opmen99810bQoSIngressPortTagClassificationEntry':opmen99810bQoSIngressPortTagClassificationEntry,_AO:opmen99810bQoSIngressPortTagClassificationPort,_AP:opmen99810bQoSIngressPortTagPCP,_AQ:opmen99810bQoSIngressPortTagDEI,'opmen99810bQoSIngressPortTagQosClass':opmen99810bQoSIngressPortTagQosClass,'opmen99810bQoSIngressPortTagDPLevel':opmen99810bQoSIngressPortTagDPLevel,'opmen99810bQosPortPolicingTable':opmen99810bQosPortPolicingTable,'opmen99810bQosPortPolicingEntry':opmen99810bQosPortPolicingEntry,_AR:opmen99810bQosPortPolicingPort,'opmen99810bQosPortPolicingMode':opmen99810bQosPortPolicingMode,'opmen99810bQosPortPolicingRate':opmen99810bQosPortPolicingRate,'opmen99810bQosPortPolicingUnit':opmen99810bQosPortPolicingUnit,'opmen99810bQosPortPolicingFlowControl':opmen99810bQosPortPolicingFlowControl,'opmen99810bQosPortScheduler':opmen99810bQosPortScheduler,'opmen99810bQosPortSchedulerModeTable':opmen99810bQosPortSchedulerModeTable,'opmen99810bQosPortSchedulerModeEntry':opmen99810bQosPortSchedulerModeEntry,_AS:opmen99810bQosSchedulerModePort,'opmen99810bQosSchedulerMode':opmen99810bQosSchedulerMode,'opmen99810bQosSchedulerShaper':opmen99810bQosSchedulerShaper,'opmen99810bQosSchedulerShaperRate':opmen99810bQosSchedulerShaperRate,'opmen99810bQosPortSchedulerTable':opmen99810bQosPortSchedulerTable,'opmen99810bQosPortSchedulerEntry':opmen99810bQosPortSchedulerEntry,_AT:opmen99810bQosSchedulerPort,_AU:opmen99810bQosSchedulerPortQueue,'opmen99810bQosSchedulerPortQueueShaper':opmen99810bQosSchedulerPortQueueShaper,'opmen99810bQosSchedulerPortQueueShaperRate':opmen99810bQosSchedulerPortQueueShaperRate,'opmen99810bQosSchedulerPortQueueShaperExcess':opmen99810bQosSchedulerPortQueueShaperExcess,'opmen99810bQosSchedulerPortQueueSchedulerWeight':opmen99810bQosSchedulerPortQueueSchedulerWeight,'opmen99810bQosSchedulerPortQueueSchedulerPercent':opmen99810bQosSchedulerPortQueueSchedulerPercent,'opmen99810bQosPortEgressTagRemarking':opmen99810bQosPortEgressTagRemarking,'opmen99810bQosPortEgressTagRemarkingTable':opmen99810bQosPortEgressTagRemarkingTable,'opmen99810bQosPortEgressTagRemarkingEntry':opmen99810bQosPortEgressTagRemarkingEntry,_AV:opmen99810bQosEgressTagRemarkingPort,'opmen99810bQosEgressTagRemarkingMode':opmen99810bQosEgressTagRemarkingMode,'opmen99810bQosPortEgressTagRemarkingDefTable':opmen99810bQosPortEgressTagRemarkingDefTable,'opmen99810bQosPortEgressTagRemarkingDefEntry':opmen99810bQosPortEgressTagRemarkingDefEntry,_AW:opmen99810bQosEgressTagRemarkingDefPort,'opmen99810bQosEgressTagRemarkingDefPCP':opmen99810bQosEgressTagRemarkingDefPCP,'opmen99810bQosEgressTagRemarkingDefDEI':opmen99810bQosEgressTagRemarkingDefDEI,'opmen99810bQosPortEgressTagRemarkingMapTable':opmen99810bQosPortEgressTagRemarkingMapTable,'opmen99810bQosPortEgressTagRemarkingMapEntry':opmen99810bQosPortEgressTagRemarkingMapEntry,_AX:opmen99810bQosPortEgressTagRemarkingMapPort,_AY:opmen99810bQosTagRemarkingQoSClass,_AZ:opmen99810bQosTagRemarkingDPLevel,'opmen99810bQosTagRemarkingPCP':opmen99810bQosTagRemarkingPCP,'opmen99810bQosTagRemarkingDEI':opmen99810bQosTagRemarkingDEI,'opmen99810bQosPortDSCPTable':opmen99810bQosPortDSCPTable,'opmen99810bQosPortDSCPEntry':opmen99810bQosPortDSCPEntry,_Aa:opmen99810bQosPortDSCPPort,'opmen99810bQosPortDSCPIngressTranslate':opmen99810bQosPortDSCPIngressTranslate,'opmen99810bQosPortDSCPIngressClassify':opmen99810bQosPortDSCPIngressClassify,'opmen99810bQosPortDSCPEgressRewrite':opmen99810bQosPortDSCPEgressRewrite,'opmen99810bQosDSCPTable':opmen99810bQosDSCPTable,'opmen99810bQosDSCPEntry':opmen99810bQosDSCPEntry,_Ab:opmen99810bQosDSCPList,'opmen99810bQosDSCP':opmen99810bQosDSCP,'opmen99810bQosDSCPTrust':opmen99810bQosDSCPTrust,'opmen99810bQosDSCPQosClass':opmen99810bQosDSCPQosClass,'opmen99810bQosDSCPDPL':opmen99810bQosDSCPDPL,'opmen99810bQosDSCPTranslationTable':opmen99810bQosDSCPTranslationTable,'opmen99810bQosDSCPTranslationEntry':opmen99810bQosDSCPTranslationEntry,_Ac:opmen99810bQosDSCPTranslationList,'opmen99810bQosDSCPTranslationDSCPBasedId':opmen99810bQosDSCPTranslationDSCPBasedId,'opmen99810bQosDSCPTranslationIngressTranslate':opmen99810bQosDSCPTranslationIngressTranslate,'opmen99810bQosDSCPTranslationIngressClassify':opmen99810bQosDSCPTranslationIngressClassify,'opmen99810bQosDSCPTranslationEgressRemapDP0':opmen99810bQosDSCPTranslationEgressRemapDP0,'opmen99810bQosDSCPTranslationEgressRemapDP1':opmen99810bQosDSCPTranslationEgressRemapDP1,'opmen99810bQosDSCPClassificationTable':opmen99810bQosDSCPClassificationTable,'opmen99810bQosDSCPClassificationEntry':opmen99810bQosDSCPClassificationEntry,_Ad:opmen99810bQosDSCPClassificationQoSClass,_Ae:opmen99810bQosDSCPClassificationDPL,'opmen99810bQosDSCPClassificationDSCP':opmen99810bQosDSCPClassificationDSCP,'opmen99810bQosControlList':opmen99810bQosControlList,'opmen99810bQosQceCreate':opmen99810bQosQceCreate,'opmen99810bQosQceTable':opmen99810bQosQceTable,'opmen99810bQosQceEntry':opmen99810bQosQceEntry,_Af:opmen99810bQosQceIndex,'opmen99810bQosQceID':opmen99810bQosQceID,'opmen99810bQosQceNextID':opmen99810bQosQceNextID,'opmen99810bQosQcePortMembers':opmen99810bQosQcePortMembers,'opmen99810bQosQceTag':opmen99810bQosQceTag,'opmen99810bQosQceVID':opmen99810bQosQceVID,'opmen99810bQosPCP':opmen99810bQosPCP,'opmen99810bQosDEI':opmen99810bQosDEI,'opmen99810bQosSMAC':opmen99810bQosSMAC,'opmen99810bQosDMACType':opmen99810bQosDMACType,'opmen99810bQosFrameType':opmen99810bQosFrameType,'opmen99810bQosMacEtherType':opmen99810bQosMacEtherType,'opmen99810bQosLLCSSAPAddr':opmen99810bQosLLCSSAPAddr,'opmen99810bQosLLCDSAPAddr':opmen99810bQosLLCDSAPAddr,'opmen99810bQosLLCControl':opmen99810bQosLLCControl,'opmen99810bQosSNAPPID':opmen99810bQosSNAPPID,'opmen99810bQosIpv4Protocol':opmen99810bQosIpv4Protocol,'opmen99810bQosIpv4ProtocolValue':opmen99810bQosIpv4ProtocolValue,'opmen99810bQosIpv4ProtocolUDPSport':opmen99810bQosIpv4ProtocolUDPSport,'opmen99810bQosIpv4ProtocolUDPDport':opmen99810bQosIpv4ProtocolUDPDport,'opmen99810bQosIpv4ProtocolTCPSport':opmen99810bQosIpv4ProtocolTCPSport,'opmen99810bQosIpv4ProtocolTCPDport':opmen99810bQosIpv4ProtocolTCPDport,'opmen99810bQosIpv4SourceIp':opmen99810bQosIpv4SourceIp,'opmen99810bQosIpv4SourceMask':opmen99810bQosIpv4SourceMask,'opmen99810bQosIpv4IPFragment':opmen99810bQosIpv4IPFragment,'opmen99810bQosIpv4DSCP':opmen99810bQosIpv4DSCP,'opmen99810bQosIpv6Protocol':opmen99810bQosIpv6Protocol,'opmen99810bQosIpv6ProtocolValue':opmen99810bQosIpv6ProtocolValue,'opmen99810bQosIpv6ProtocolUDPSport':opmen99810bQosIpv6ProtocolUDPSport,'opmen99810bQosIpv6ProtocolUDPDport':opmen99810bQosIpv6ProtocolUDPDport,'opmen99810bQosIpv6ProtocolTCPSport':opmen99810bQosIpv6ProtocolTCPSport,'opmen99810bQosIpv6ProtocolTCPDport':opmen99810bQosIpv6ProtocolTCPDport,'opmen99810bQosIpv6SourceIp':opmen99810bQosIpv6SourceIp,'opmen99810bQosIpv6SourceMask':opmen99810bQosIpv6SourceMask,'opmen99810bQosIpv6DSCP':opmen99810bQosIpv6DSCP,'opmen99810bQosActionClass':opmen99810bQosActionClass,'opmen99810bQosActionDPL':opmen99810bQosActionDPL,'opmen99810bQosActionDSCP':opmen99810bQosActionDSCP,'opmen99810bQosQceRowStatus':opmen99810bQosQceRowStatus,'opmen99810bQosQceMoveID':opmen99810bQosQceMoveID,'opmen99810bQosQceMoveNextID':opmen99810bQosQceMoveNextID,'opmen99810bQosQCLStatusTable':opmen99810bQosQCLStatusTable,'opmen99810bQosQCLStatusEntry':opmen99810bQosQCLStatusEntry,_Ag:opmen99810bQosQCLStatusList,'opmen99810bQosQCLStatusUser':opmen99810bQosQCLStatusUser,'opmen99810bQosQCLStatusQCEId':opmen99810bQosQCLStatusQCEId,'opmen99810bQosQCLStatusFrameType':opmen99810bQosQCLStatusFrameType,'opmen99810bQosQCLStatusPortlist':opmen99810bQosQCLStatusPortlist,'opmen99810bQosQCLStatusActionClass':opmen99810bQosQCLStatusActionClass,'opmen99810bQosQCLStatusActionDPL':opmen99810bQosQCLStatusActionDPL,'opmen99810bQosQCLStatusActionDSCP':opmen99810bQosQCLStatusActionDSCP,'opmen99810bQosQCLStatusActionConflict':opmen99810bQosQCLStatusActionConflict,'opmen99810bQosStormControl':opmen99810bQosStormControl,'opmen99810bQoSStormControlUC':opmen99810bQoSStormControlUC,'opmen99810bQoSStormControlUCRate':opmen99810bQoSStormControlUCRate,'opmen99810bQoSStormControlMC':opmen99810bQoSStormControlMC,'opmen99810bQoSStormControlMCRate':opmen99810bQoSStormControlMCRate,'opmen99810bQoSStormControlBC':opmen99810bQoSStormControlBC,'opmen99810bQoSStormControlBCRate':opmen99810bQoSStormControlBCRate,'opmen99810bVlan':opmen99810bVlan,'opmen99810bVlanPorts':opmen99810bVlanPorts,'opmen99810bVlanPortsTPIDforCustomSport':opmen99810bVlanPortsTPIDforCustomSport,'opmen99810bVlanPortsTable':opmen99810bVlanPortsTable,'opmen99810bVlanPortsEntry':opmen99810bVlanPortsEntry,_Ah:opmen99810bVlanPortsPort,'opmen99810bVlanPortsPVID':opmen99810bVlanPortsPVID,'opmen99810bVlanPortsFrameType':opmen99810bVlanPortsFrameType,'opmen99810bVlanPortsIngressFilter':opmen99810bVlanPortsIngressFilter,'opmen99810bVlanPortsEgressRule':opmen99810bVlanPortsEgressRule,'opmen99810bVlanPortsPortType':opmen99810bVlanPortsPortType,'opmen99810bSecurity':opmen99810bSecurity,'opmen99810bIPSourceGuard':opmen99810bIPSourceGuard,'opmen99810bIPSourceGuardConf':opmen99810bIPSourceGuardConf,'opmen99810bIPSourceGuardMode':opmen99810bIPSourceGuardMode,'opmen99810bIPSourceGuardPortConfigTable':opmen99810bIPSourceGuardPortConfigTable,'opmen99810bIPSourceGuardPortConfigEntry':opmen99810bIPSourceGuardPortConfigEntry,_Ai:opmen99810bIPSourceGuardPortConfigPort,'opmen99810bIPSourceGuardPortConfigMode':opmen99810bIPSourceGuardPortConfigMode,'opmen99810bIPSourceGuardPortMaxDynamicClients':opmen99810bIPSourceGuardPortMaxDynamicClients,'opmen99810bIPSourceGuardStatic':opmen99810bIPSourceGuardStatic,'opmen99810bIPSourceGuardStaticCreate':opmen99810bIPSourceGuardStaticCreate,'opmen99810bIPSourceGuardStaticTable':opmen99810bIPSourceGuardStaticTable,'opmen99810bIPSourceGuardStaticEntry':opmen99810bIPSourceGuardStaticEntry,_Aj:opmen99810bIPSourceGuardStaticIndex,'opmen99810bIPSourceGuardStaticPort':opmen99810bIPSourceGuardStaticPort,'opmen99810bIPSourceGuardStaticVLANId':opmen99810bIPSourceGuardStaticVLANId,'opmen99810bIPSourceGuardStaticIPAddress':opmen99810bIPSourceGuardStaticIPAddress,'opmen99810bIPSourceGuardStaticMACAddress':opmen99810bIPSourceGuardStaticMACAddress,'opmen99810bIPSourceGuardStaticRowStatus':opmen99810bIPSourceGuardStaticRowStatus,'opmen99810bIPSourceGuardDynamicTable':opmen99810bIPSourceGuardDynamicTable,'opmen99810bIPSourceGuardDynamicEntry':opmen99810bIPSourceGuardDynamicEntry,_Ak:opmen99810bIPSourceGuardDynamicIndex,'opmen99810bIPSourceGuardDynamicPort':opmen99810bIPSourceGuardDynamicPort,'opmen99810bIPSourceGuardDynamicVLANId':opmen99810bIPSourceGuardDynamicVLANId,'opmen99810bIPSourceGuardDynamicIPAddress':opmen99810bIPSourceGuardDynamicIPAddress,'opmen99810bIPSourceGuardDynamicMACAddress':opmen99810bIPSourceGuardDynamicMACAddress,'opmen99810bARPInspection':opmen99810bARPInspection,'opmen99810bARPInspectionConf':opmen99810bARPInspectionConf,'opmen99810bARPInspectionConfMode':opmen99810bARPInspectionConfMode,'opmen99810bARPInspectionConfTable':opmen99810bARPInspectionConfTable,'opmen99810bARPInspectionConfEntry':opmen99810bARPInspectionConfEntry,_Al:opmen99810bARPInspectionConfPortIndex,'opmen99810bARPInspectionConfPortMode':opmen99810bARPInspectionConfPortMode,'opmen99810bARPInspectionStatic':opmen99810bARPInspectionStatic,'opmen99810bARPInspectionStaticCreate':opmen99810bARPInspectionStaticCreate,'opmen99810bARPInspectionStaticTable':opmen99810bARPInspectionStaticTable,'opmen99810bARPInspectionStaticEntry':opmen99810bARPInspectionStaticEntry,_Am:opmen99810bARPInspectionStaticIndex,'opmen99810bARPInspectionStaticPort':opmen99810bARPInspectionStaticPort,'opmen99810bARPInspectionStaticVLANId':opmen99810bARPInspectionStaticVLANId,'opmen99810bARPInspectionStaticIPAddress':opmen99810bARPInspectionStaticIPAddress,'opmen99810bARPInspectionStaticMACAddress':opmen99810bARPInspectionStaticMACAddress,'opmen99810bARPInspectionStaticRowStatus':opmen99810bARPInspectionStaticRowStatus,'opmen99810bARPInspectionDynamicTable':opmen99810bARPInspectionDynamicTable,'opmen99810bARPInspectionDynamicEntry':opmen99810bARPInspectionDynamicEntry,_An:opmen99810bARPInspectionDynamicIndex,'opmen99810bARPInspectionDynamicPort':opmen99810bARPInspectionDynamicPort,'opmen99810bARPInspectionDynamicVLANId':opmen99810bARPInspectionDynamicVLANId,'opmen99810bARPInspectionDynamicIPAddress':opmen99810bARPInspectionDynamicIPAddress,'opmen99810bARPInspectionDynamicMACAddress':opmen99810bARPInspectionDynamicMACAddress,'opmen99810bDHCPSnooping':opmen99810bDHCPSnooping,'opmen99810bDHCPSnoopingConf':opmen99810bDHCPSnoopingConf,'opmen99810bDHCPSnoopingMode':opmen99810bDHCPSnoopingMode,'opmen99810bDHCPSnoopingPortModeConfigurationTable':opmen99810bDHCPSnoopingPortModeConfigurationTable,'opmen99810bDHCPSnoopingPortModeConfigurationEntry':opmen99810bDHCPSnoopingPortModeConfigurationEntry,_Ao:opmen99810bDHCPSnoopingPortModeConfigurationPort,'opmen99810bDHCPSnoopingPortModeConfigurationMode':opmen99810bDHCPSnoopingPortModeConfigurationMode,'opmen99810bDHCPSnoopingStatisticsTable':opmen99810bDHCPSnoopingStatisticsTable,'opmen99810bDHCPSnoopingStatisticsEntry':opmen99810bDHCPSnoopingStatisticsEntry,_Ap:opmen99810bDHCPSnoopingStatisticsPort,'opmen99810bDHCPSnoopingStatisticsClear':opmen99810bDHCPSnoopingStatisticsClear,'opmen99810bDHCPSnoopingRxDiscover':opmen99810bDHCPSnoopingRxDiscover,'opmen99810bDHCPSnoopingRxOffer':opmen99810bDHCPSnoopingRxOffer,'opmen99810bDHCPSnoopingRxRequest':opmen99810bDHCPSnoopingRxRequest,'opmen99810bDHCPSnoopingRxDecline':opmen99810bDHCPSnoopingRxDecline,'opmen99810bDHCPSnoopingRxACK':opmen99810bDHCPSnoopingRxACK,'opmen99810bDHCPSnoopingRxNAK':opmen99810bDHCPSnoopingRxNAK,'opmen99810bDHCPSnoopingRxRelease':opmen99810bDHCPSnoopingRxRelease,'opmen99810bDHCPSnoopingRxInform':opmen99810bDHCPSnoopingRxInform,'opmen99810bDHCPSnoopingRxLeaseQuery':opmen99810bDHCPSnoopingRxLeaseQuery,'opmen99810bDHCPSnoopingRxLeaseUnassigned':opmen99810bDHCPSnoopingRxLeaseUnassigned,'opmen99810bDHCPSnoopingRxLeaseUnknown':opmen99810bDHCPSnoopingRxLeaseUnknown,'opmen99810bDHCPSnoopingRxLeaseActive':opmen99810bDHCPSnoopingRxLeaseActive,'opmen99810bDHCPSnoopingTxDiscover':opmen99810bDHCPSnoopingTxDiscover,'opmen99810bDHCPSnoopingTxOffer':opmen99810bDHCPSnoopingTxOffer,'opmen99810bDHCPSnoopingTxRequest':opmen99810bDHCPSnoopingTxRequest,'opmen99810bDHCPSnoopingTxDecline':opmen99810bDHCPSnoopingTxDecline,'opmen99810bDHCPSnoopingTxACK':opmen99810bDHCPSnoopingTxACK,'opmen99810bDHCPSnoopingTxNAK':opmen99810bDHCPSnoopingTxNAK,'opmen99810bDHCPSnoopingTxRelease':opmen99810bDHCPSnoopingTxRelease,'opmen99810bDHCPSnoopingTxInform':opmen99810bDHCPSnoopingTxInform,'opmen99810bDHCPSnoopingTxLeaseQuery':opmen99810bDHCPSnoopingTxLeaseQuery,'opmen99810bDHCPSnoopingTxLeaseUnassigned':opmen99810bDHCPSnoopingTxLeaseUnassigned,'opmen99810bDHCPSnoopingTxLeaseUnknown':opmen99810bDHCPSnoopingTxLeaseUnknown,'opmen99810bDHCPSnoopingTxLeaseActive':opmen99810bDHCPSnoopingTxLeaseActive,'opmen99810bDHCPRelay':opmen99810bDHCPRelay,'opmen99810bDHCPRelayConfiguration':opmen99810bDHCPRelayConfiguration,'opmen99810bDHCPRelayMode':opmen99810bDHCPRelayMode,'opmen99810bDHCPRelayServer':opmen99810bDHCPRelayServer,'opmen99810bDHCPRelayInformationMode':opmen99810bDHCPRelayInformationMode,'opmen99810bDHCPRelayInformationPolicy':opmen99810bDHCPRelayInformationPolicy,'opmen99810bDHCPRelayStatistics':opmen99810bDHCPRelayStatistics,'opmen99810bDHCPRelayServerStatistics':opmen99810bDHCPRelayServerStatistics,'opmen99810bServerStatTransmitToServer':opmen99810bServerStatTransmitToServer,'opmen99810bServerStatTransmitError':opmen99810bServerStatTransmitError,'opmen99810bServerStatReceiveFromServer':opmen99810bServerStatReceiveFromServer,'opmen99810bServerStatReceiveMissingAgentOption':opmen99810bServerStatReceiveMissingAgentOption,'opmen99810bServerStatReceiveMissingCircuitID':opmen99810bServerStatReceiveMissingCircuitID,'opmen99810bServerStatReceiveMissingRemoteID':opmen99810bServerStatReceiveMissingRemoteID,'opmen99810bServerStatReceiveBadCircuitID':opmen99810bServerStatReceiveBadCircuitID,'opmen99810bServerStatReceiveBadRemoteID':opmen99810bServerStatReceiveBadRemoteID,'opmen99810bDHCPRelayClientStatistics':opmen99810bDHCPRelayClientStatistics,'opmen99810bClientStatTransmitToClient':opmen99810bClientStatTransmitToClient,'opmen99810bClientStatTransmitError':opmen99810bClientStatTransmitError,'opmen99810bClientStatReceivefromClient':opmen99810bClientStatReceivefromClient,'opmen99810bClientStatReceiveAgentOption':opmen99810bClientStatReceiveAgentOption,'opmen99810bClientStatReplaceAgentOption':opmen99810bClientStatReplaceAgentOption,'opmen99810bClientStatKeepAgentOption':opmen99810bClientStatKeepAgentOption,'opmen99810bClientStatDropAgentOption':opmen99810bClientStatDropAgentOption,'opmen99810bPortSecurity':opmen99810bPortSecurity,'opmen99810bPortSecLimitCtrl':opmen99810bPortSecLimitCtrl,'opmen99810bPortSecLimitCtrlSystemConf':opmen99810bPortSecLimitCtrlSystemConf,'opmen99810bPortSecurityMode':opmen99810bPortSecurityMode,'opmen99810bPortSecurityAging':opmen99810bPortSecurityAging,'opmen99810bPortSecurityAgingPeriod':opmen99810bPortSecurityAgingPeriod,'opmen99810bPortSecLimitCtrlTable':opmen99810bPortSecLimitCtrlTable,'opmen99810bPortSecLimitCtrlEntry':opmen99810bPortSecLimitCtrlEntry,_Aq:opmen99810bPortSecLimitCtrlPort,'opmen99810bPortSecLimitCtrlPortMode':opmen99810bPortSecLimitCtrlPortMode,'opmen99810bPortSecLimitCtrlPortLimit':opmen99810bPortSecLimitCtrlPortLimit,'opmen99810bPortSecLimitCtrlPortAction':opmen99810bPortSecLimitCtrlPortAction,'opmen99810bPortSecLimitCtrlPortState':opmen99810bPortSecLimitCtrlPortState,'opmen99810bPortSecLimitCtrlPortReOpen':opmen99810bPortSecLimitCtrlPortReOpen,'opmen99810bPortSecSwitchStatusTable':opmen99810bPortSecSwitchStatusTable,'opmen99810bPortSecSwitchStatusEntry':opmen99810bPortSecSwitchStatusEntry,_Ar:opmen99810bPortSecSwitchStatusPort,'opmen99810bPortSecSwitchStatusUsers':opmen99810bPortSecSwitchStatusUsers,'opmen99810bPortSecSwitchStatusState':opmen99810bPortSecSwitchStatusState,'opmen99810bPortSecSwitchStatusMACCountCurrent':opmen99810bPortSecSwitchStatusMACCountCurrent,'opmen99810bPortSecSwitchStatusMACCountLimit':opmen99810bPortSecSwitchStatusMACCountLimit,'opmen99810bPortSecPortStatus':opmen99810bPortSecPortStatus,'opmen99810bPortSecPortStatusPort':opmen99810bPortSecPortStatusPort,'opmen99810bPortSecPortStatusTable':opmen99810bPortSecPortStatusTable,'opmen99810bPortSecPortStatusEntry':opmen99810bPortSecPortStatusEntry,_As:opmen99810bPortSecPortStatusIndex,'opmen99810bPortSecPortStatusMACAddress':opmen99810bPortSecPortStatusMACAddress,'opmen99810bPortSecPortStatusVLANId':opmen99810bPortSecPortStatusVLANId,'opmen99810bPortSecPortStatusState':opmen99810bPortSecPortStatusState,'opmen99810bPortSecPortStatusTimeOfAddition':opmen99810bPortSecPortStatusTimeOfAddition,'opmen99810bPortSecPortStatusAgeAndHold':opmen99810bPortSecPortStatusAgeAndHold,'opmen99810bAccessManagement':opmen99810bAccessManagement,'opmen99810bAccessMgtConf':opmen99810bAccessMgtConf,'opmen99810bAccessMgtConfMode':opmen99810bAccessMgtConfMode,'opmen99810bAccessMgtConfCreate':opmen99810bAccessMgtConfCreate,'opmen99810bAccessMgtConfTable':opmen99810bAccessMgtConfTable,'opmen99810bAccessMgtConfEntry':opmen99810bAccessMgtConfEntry,_At:opmen99810bAccessMgtIndex,'opmen99810bAccessMgtAddresstype':opmen99810bAccessMgtAddresstype,'opmen99810bAccessMgtStartIpAddress':opmen99810bAccessMgtStartIpAddress,'opmen99810bAccessMgtEndIpAddress':opmen99810bAccessMgtEndIpAddress,'opmen99810bAccessMgtHttpHttps':opmen99810bAccessMgtHttpHttps,'opmen99810bAccessMgtSNMP':opmen99810bAccessMgtSNMP,'opmen99810bAccessMgtTelnetSSH':opmen99810bAccessMgtTelnetSSH,'opmen99810bAccessMgtRowStatus':opmen99810bAccessMgtRowStatus,'opmen99810bAccessMgtStatistics':opmen99810bAccessMgtStatistics,'opmen99810bHttpReceivedPkts':opmen99810bHttpReceivedPkts,'opmen99810bHttpAllowedPkts':opmen99810bHttpAllowedPkts,'opmen99810bHttpDiscardedPkts':opmen99810bHttpDiscardedPkts,'opmen99810bHttpsReceivedPkts':opmen99810bHttpsReceivedPkts,'opmen99810bHttpsAllowedPkts':opmen99810bHttpsAllowedPkts,'opmen99810bHttpsDiscardedPkts':opmen99810bHttpsDiscardedPkts,'opmen99810bSnmpReceivedPkts':opmen99810bSnmpReceivedPkts,'opmen99810bSnmpAllowedPkts':opmen99810bSnmpAllowedPkts,'opmen99810bSnmpDiscardedPkts':opmen99810bSnmpDiscardedPkts,'opmen99810bTelnetReceivedPkts':opmen99810bTelnetReceivedPkts,'opmen99810bTelnetAllowedPkts':opmen99810bTelnetAllowedPkts,'opmen99810bTelnetDiscardedPkts':opmen99810bTelnetDiscardedPkts,'opmen99810bSSHReceivedPkts':opmen99810bSSHReceivedPkts,'opmen99810bSSHAllowedPkts':opmen99810bSSHAllowedPkts,'opmen99810bSSHDiscardedPkts':opmen99810bSSHDiscardedPkts,'opmen99810bAccessMgtStatisticsClearAll':opmen99810bAccessMgtStatisticsClearAll,'opmen99810bSSH':opmen99810bSSH,'opmen99810bSSHMode':opmen99810bSSHMode,'opmen99810bHTTPS':opmen99810bHTTPS,'opmen99810bHTTPSMode':opmen99810bHTTPSMode,'opmen99810bHTTPSAutoRedirect':opmen99810bHTTPSAutoRedirect,'opmen99810bAuthMethod':opmen99810bAuthMethod,'opmen99810bConsoleAuthMethod':opmen99810bConsoleAuthMethod,'opmen99810bConsoleFallback':opmen99810bConsoleFallback,'opmen99810bTelnetAuthMethod':opmen99810bTelnetAuthMethod,'opmen99810bTelnetFallback':opmen99810bTelnetFallback,'opmen99810bSshAuthMethod':opmen99810bSshAuthMethod,'opmen99810bSshFallback':opmen99810bSshFallback,'opmen99810bWebAuthMethod':opmen99810bWebAuthMethod,'opmen99810bWebFallback':opmen99810bWebFallback,'opmen99810bMaintenance':opmen99810bMaintenance,'opmen99810bRestartDevice':opmen99810bRestartDevice,'opmen99810bFirmware':opmen99810bFirmware,'opmen99810bFirmwareIpAddress':opmen99810bFirmwareIpAddress,'opmen99810bFirmwareFileName':opmen99810bFirmwareFileName,'opmen99810bDoFirmwareUpgrade':opmen99810bDoFirmwareUpgrade,'opmen99810bSaveOrRestore':opmen99810bSaveOrRestore,'opmen99810bFactoryDefaults':opmen99810bFactoryDefaults,'opmen99810bSaveStart':opmen99810bSaveStart,'opmen99810bSaveUser':opmen99810bSaveUser,'opmen99810bRestoreUser':opmen99810bRestoreUser,'opmen99810bExportOrImport':opmen99810bExportOrImport,'opmen99810bExportIpAddress':opmen99810bExportIpAddress,'opmen99810bExportConfigName':opmen99810bExportConfigName,'opmen99810bDoExportConfig':opmen99810bDoExportConfig,'opmen99810bImportIpAddress':opmen99810bImportIpAddress,'opmen99810bImportConfigName':opmen99810bImportConfigName,'opmen99810bDoImportConfig':opmen99810bDoImportConfig,'opmen99810bDiagnostics':opmen99810bDiagnostics,'opmen99810bPingIpAddress':opmen99810bPingIpAddress,'opmen99810bPingSize':opmen99810bPingSize,'opmen99810bDoPingConfig':opmen99810bDoPingConfig,'opmen99810bPingResult':opmen99810bPingResult,'opmen99810bPing6IpAddress':opmen99810bPing6IpAddress,'opmen99810bPing6Size':opmen99810bPing6Size,'opmen99810bDoPing6Config':opmen99810bDoPing6Config,'opmen99810bPing6Result':opmen99810bPing6Result,'opmen99810bTrap':opmen99810bTrap,'opmen99810bTrapEvent':opmen99810bTrapEvent,'opmen99810bEmergency':opmen99810bEmergency,'opmen99810bAlert':opmen99810bAlert,'opmen99810bCritical':opmen99810bCritical,'opmen99810bError':opmen99810bError,'opmen99810bWarning':opmen99810bWarning,'opmen99810bNotice':opmen99810bNotice,'opmen99810bInformational':opmen99810bInformational,'opmen99810bDebug':opmen99810bDebug,'opmen99810bTrapVariable':opmen99810bTrapVariable,_V:opmen99810bInformation})