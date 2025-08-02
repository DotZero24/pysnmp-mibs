_T='ruckusZDEventReason'
_S='ruckusZDEventIpAddr'
_R='ruckusZDEventClientMacAddr'
_Q='ruckusZDEventSSID'
_P='accessible-for-notify'
_O='ruckusZDEventAPMacAddr'
_N='ruckusZDEventContent'
_M='ruckusZDEventTitle'
_L='ruckusZDEventStatus'
_K='ruckusZDEventTime'
_J='ruckusZDEventType'
_I='ruckusZDEventSeverity'
_H='ruckusZDEventNEID'
_G='ruckusZDEventSerial'
_F='read-write'
_E='enable'
_D='disable'
_C='Integer32'
_B='current'
_A='RUCKUS-ZD-EVENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ruckusEvents,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusEvents')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ruckusZDEventMIB=ModuleIdentity((1,3,6,1,4,1,25053,2,2))
_RuckusZDEventTraps_ObjectIdentity=ObjectIdentity
ruckusZDEventTraps=_RuckusZDEventTraps_ObjectIdentity((1,3,6,1,4,1,25053,2,2,1))
_RuckusZDEventObjects_ObjectIdentity=ObjectIdentity
ruckusZDEventObjects=_RuckusZDEventObjects_ObjectIdentity((1,3,6,1,4,1,25053,2,2,2))
_RuckusZDEventSerial_Type=OctetString
_RuckusZDEventSerial_Object=MibScalar
ruckusZDEventSerial=_RuckusZDEventSerial_Object((1,3,6,1,4,1,25053,2,2,2,1),_RuckusZDEventSerial_Type())
ruckusZDEventSerial.setMaxAccess(_P)
if mibBuilder.loadTexts:ruckusZDEventSerial.setStatus(_B)
_RuckusZDEventNEID_Type=OctetString
_RuckusZDEventNEID_Object=MibScalar
ruckusZDEventNEID=_RuckusZDEventNEID_Object((1,3,6,1,4,1,25053,2,2,2,2),_RuckusZDEventNEID_Type())
ruckusZDEventNEID.setMaxAccess(_P)
if mibBuilder.loadTexts:ruckusZDEventNEID.setStatus(_B)
_RuckusZDEventSeverity_Type=OctetString
_RuckusZDEventSeverity_Object=MibScalar
ruckusZDEventSeverity=_RuckusZDEventSeverity_Object((1,3,6,1,4,1,25053,2,2,2,3),_RuckusZDEventSeverity_Type())
ruckusZDEventSeverity.setMaxAccess(_P)
if mibBuilder.loadTexts:ruckusZDEventSeverity.setStatus(_B)
_RuckusZDEventType_Type=OctetString
_RuckusZDEventType_Object=MibScalar
ruckusZDEventType=_RuckusZDEventType_Object((1,3,6,1,4,1,25053,2,2,2,4),_RuckusZDEventType_Type())
ruckusZDEventType.setMaxAccess(_P)
if mibBuilder.loadTexts:ruckusZDEventType.setStatus(_B)
_RuckusZDEventTime_Type=OctetString
_RuckusZDEventTime_Object=MibScalar
ruckusZDEventTime=_RuckusZDEventTime_Object((1,3,6,1,4,1,25053,2,2,2,5),_RuckusZDEventTime_Type())
ruckusZDEventTime.setMaxAccess(_P)
if mibBuilder.loadTexts:ruckusZDEventTime.setStatus(_B)
class _RuckusZDEventStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('raise',1),('clear',2)))
_RuckusZDEventStatus_Type.__name__=_C
_RuckusZDEventStatus_Object=MibScalar
ruckusZDEventStatus=_RuckusZDEventStatus_Object((1,3,6,1,4,1,25053,2,2,2,6),_RuckusZDEventStatus_Type())
ruckusZDEventStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:ruckusZDEventStatus.setStatus(_B)
_RuckusZDEventTitle_Type=OctetString
_RuckusZDEventTitle_Object=MibScalar
ruckusZDEventTitle=_RuckusZDEventTitle_Object((1,3,6,1,4,1,25053,2,2,2,7),_RuckusZDEventTitle_Type())
ruckusZDEventTitle.setMaxAccess(_P)
if mibBuilder.loadTexts:ruckusZDEventTitle.setStatus(_B)
_RuckusZDEventContent_Type=OctetString
_RuckusZDEventContent_Object=MibScalar
ruckusZDEventContent=_RuckusZDEventContent_Object((1,3,6,1,4,1,25053,2,2,2,8),_RuckusZDEventContent_Type())
ruckusZDEventContent.setMaxAccess(_P)
if mibBuilder.loadTexts:ruckusZDEventContent.setStatus(_B)
_RuckusZDEventClientMacAddr_Type=OctetString
_RuckusZDEventClientMacAddr_Object=MibScalar
ruckusZDEventClientMacAddr=_RuckusZDEventClientMacAddr_Object((1,3,6,1,4,1,25053,2,2,2,15),_RuckusZDEventClientMacAddr_Type())
ruckusZDEventClientMacAddr.setMaxAccess(_P)
if mibBuilder.loadTexts:ruckusZDEventClientMacAddr.setStatus(_B)
_RuckusZDEventAPMacAddr_Type=OctetString
_RuckusZDEventAPMacAddr_Object=MibScalar
ruckusZDEventAPMacAddr=_RuckusZDEventAPMacAddr_Object((1,3,6,1,4,1,25053,2,2,2,18),_RuckusZDEventAPMacAddr_Type())
ruckusZDEventAPMacAddr.setMaxAccess(_P)
if mibBuilder.loadTexts:ruckusZDEventAPMacAddr.setStatus(_B)
_RuckusZDEventRogueMacAddr_Type=OctetString
_RuckusZDEventRogueMacAddr_Object=MibScalar
ruckusZDEventRogueMacAddr=_RuckusZDEventRogueMacAddr_Object((1,3,6,1,4,1,25053,2,2,2,20),_RuckusZDEventRogueMacAddr_Type())
ruckusZDEventRogueMacAddr.setMaxAccess(_P)
if mibBuilder.loadTexts:ruckusZDEventRogueMacAddr.setStatus(_B)
_RuckusZDEventSSID_Type=OctetString
_RuckusZDEventSSID_Object=MibScalar
ruckusZDEventSSID=_RuckusZDEventSSID_Object((1,3,6,1,4,1,25053,2,2,2,23),_RuckusZDEventSSID_Type())
ruckusZDEventSSID.setMaxAccess(_P)
if mibBuilder.loadTexts:ruckusZDEventSSID.setStatus(_B)
_RuckusZDEventChannel_Type=Unsigned32
_RuckusZDEventChannel_Object=MibScalar
ruckusZDEventChannel=_RuckusZDEventChannel_Object((1,3,6,1,4,1,25053,2,2,2,25),_RuckusZDEventChannel_Type())
ruckusZDEventChannel.setMaxAccess(_P)
if mibBuilder.loadTexts:ruckusZDEventChannel.setStatus(_B)
_RuckusZDEventReason_Type=OctetString
_RuckusZDEventReason_Object=MibScalar
ruckusZDEventReason=_RuckusZDEventReason_Object((1,3,6,1,4,1,25053,2,2,2,28),_RuckusZDEventReason_Type())
ruckusZDEventReason.setMaxAccess(_P)
if mibBuilder.loadTexts:ruckusZDEventReason.setStatus(_B)
_RuckusZDEventIpAddr_Type=OctetString
_RuckusZDEventIpAddr_Object=MibScalar
ruckusZDEventIpAddr=_RuckusZDEventIpAddr_Object((1,3,6,1,4,1,25053,2,2,2,30),_RuckusZDEventIpAddr_Type())
ruckusZDEventIpAddr.setMaxAccess(_P)
if mibBuilder.loadTexts:ruckusZDEventIpAddr.setStatus(_B)
_RuckusZDEventTrapSwitchCmd_ObjectIdentity=ObjectIdentity
ruckusZDEventTrapSwitchCmd=_RuckusZDEventTrapSwitchCmd_ObjectIdentity((1,3,6,1,4,1,25053,2,2,3))
class _RuckusZDEventAPJoinTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPJoinTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPJoinTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPJoinTrapSwitchCmd=_RuckusZDEventAPJoinTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,1),_RuckusZDEventAPJoinTrapSwitchCmd_Type())
ruckusZDEventAPJoinTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPJoinTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventSSIDSpoofTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventSSIDSpoofTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventSSIDSpoofTrapSwitchCmd_Object=MibScalar
ruckusZDEventSSIDSpoofTrapSwitchCmd=_RuckusZDEventSSIDSpoofTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,2),_RuckusZDEventSSIDSpoofTrapSwitchCmd_Type())
ruckusZDEventSSIDSpoofTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventSSIDSpoofTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventMACSpoofTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventMACSpoofTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventMACSpoofTrapSwitchCmd_Object=MibScalar
ruckusZDEventMACSpoofTrapSwitchCmd=_RuckusZDEventMACSpoofTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,3),_RuckusZDEventMACSpoofTrapSwitchCmd_Type())
ruckusZDEventMACSpoofTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventMACSpoofTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventRogueAPTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventRogueAPTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventRogueAPTrapSwitchCmd_Object=MibScalar
ruckusZDEventRogueAPTrapSwitchCmd=_RuckusZDEventRogueAPTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,4),_RuckusZDEventRogueAPTrapSwitchCmd_Type())
ruckusZDEventRogueAPTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventRogueAPTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPLostTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPLostTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPLostTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPLostTrapSwitchCmd=_RuckusZDEventAPLostTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,5),_RuckusZDEventAPLostTrapSwitchCmd_Type())
ruckusZDEventAPLostTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPLostTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPLostHeartbeatTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPLostHeartbeatTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPLostHeartbeatTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPLostHeartbeatTrapSwitchCmd=_RuckusZDEventAPLostHeartbeatTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,6),_RuckusZDEventAPLostHeartbeatTrapSwitchCmd_Type())
ruckusZDEventAPLostHeartbeatTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPLostHeartbeatTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventClientAuthFailBlockTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventClientAuthFailBlockTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventClientAuthFailBlockTrapSwitchCmd_Object=MibScalar
ruckusZDEventClientAuthFailBlockTrapSwitchCmd=_RuckusZDEventClientAuthFailBlockTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,7),_RuckusZDEventClientAuthFailBlockTrapSwitchCmd_Type())
ruckusZDEventClientAuthFailBlockTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventClientAuthFailBlockTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPResetSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPResetSwitchCmd_Type.__name__=_C
_RuckusZDEventAPResetSwitchCmd_Object=MibScalar
ruckusZDEventAPResetSwitchCmd=_RuckusZDEventAPResetSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,8),_RuckusZDEventAPResetSwitchCmd_Type())
ruckusZDEventAPResetSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPResetSwitchCmd.setStatus(_B)
class _RuckusZDEventIPChangeSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventIPChangeSwitchCmd_Type.__name__=_C
_RuckusZDEventIPChangeSwitchCmd_Object=MibScalar
ruckusZDEventIPChangeSwitchCmd=_RuckusZDEventIPChangeSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,9),_RuckusZDEventIPChangeSwitchCmd_Type())
ruckusZDEventIPChangeSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventIPChangeSwitchCmd.setStatus(_B)
class _RuckusZDEventSystemColdStartTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventSystemColdStartTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventSystemColdStartTrapSwitchCmd_Object=MibScalar
ruckusZDEventSystemColdStartTrapSwitchCmd=_RuckusZDEventSystemColdStartTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,10),_RuckusZDEventSystemColdStartTrapSwitchCmd_Type())
ruckusZDEventSystemColdStartTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventSystemColdStartTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPChannelChangeTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPChannelChangeTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPChannelChangeTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPChannelChangeTrapSwitchCmd=_RuckusZDEventAPChannelChangeTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,11),_RuckusZDEventAPChannelChangeTrapSwitchCmd_Type())
ruckusZDEventAPChannelChangeTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPChannelChangeTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventRadiusAuthUnavailableTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventRadiusAuthUnavailableTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventRadiusAuthUnavailableTrapSwitchCmd_Object=MibScalar
ruckusZDEventRadiusAuthUnavailableTrapSwitchCmd=_RuckusZDEventRadiusAuthUnavailableTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,12),_RuckusZDEventRadiusAuthUnavailableTrapSwitchCmd_Type())
ruckusZDEventRadiusAuthUnavailableTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventRadiusAuthUnavailableTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventRadiusAcctUnavailableTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventRadiusAcctUnavailableTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventRadiusAcctUnavailableTrapSwitchCmd_Object=MibScalar
ruckusZDEventRadiusAcctUnavailableTrapSwitchCmd=_RuckusZDEventRadiusAcctUnavailableTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,13),_RuckusZDEventRadiusAcctUnavailableTrapSwitchCmd_Type())
ruckusZDEventRadiusAcctUnavailableTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventRadiusAcctUnavailableTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventClientJoinFailAPBusyTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventClientJoinFailAPBusyTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventClientJoinFailAPBusyTrapSwitchCmd_Object=MibScalar
ruckusZDEventClientJoinFailAPBusyTrapSwitchCmd=_RuckusZDEventClientJoinFailAPBusyTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,14),_RuckusZDEventClientJoinFailAPBusyTrapSwitchCmd_Type())
ruckusZDEventClientJoinFailAPBusyTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventClientJoinFailAPBusyTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventInterferenceADHocTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventInterferenceADHocTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventInterferenceADHocTrapSwitchCmd_Object=MibScalar
ruckusZDEventInterferenceADHocTrapSwitchCmd=_RuckusZDEventInterferenceADHocTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,15),_RuckusZDEventInterferenceADHocTrapSwitchCmd_Type())
ruckusZDEventInterferenceADHocTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventInterferenceADHocTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventImageUpgradeFailTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventImageUpgradeFailTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventImageUpgradeFailTrapSwitchCmd_Object=MibScalar
ruckusZDEventImageUpgradeFailTrapSwitchCmd=_RuckusZDEventImageUpgradeFailTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,16),_RuckusZDEventImageUpgradeFailTrapSwitchCmd_Type())
ruckusZDEventImageUpgradeFailTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventImageUpgradeFailTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventHeartbeatTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventHeartbeatTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventHeartbeatTrapSwitchCmd_Object=MibScalar
ruckusZDEventHeartbeatTrapSwitchCmd=_RuckusZDEventHeartbeatTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,22),_RuckusZDEventHeartbeatTrapSwitchCmd_Type())
ruckusZDEventHeartbeatTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventHeartbeatTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAttackedTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAttackedTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAttackedTrapSwitchCmd_Object=MibScalar
ruckusZDEventAttackedTrapSwitchCmd=_RuckusZDEventAttackedTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,24),_RuckusZDEventAttackedTrapSwitchCmd_Type())
ruckusZDEventAttackedTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAttackedTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventSystemWarmStartTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventSystemWarmStartTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventSystemWarmStartTrapSwitchCmd_Object=MibScalar
ruckusZDEventSystemWarmStartTrapSwitchCmd=_RuckusZDEventSystemWarmStartTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,25),_RuckusZDEventSystemWarmStartTrapSwitchCmd_Type())
ruckusZDEventSystemWarmStartTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventSystemWarmStartTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventInterfereAPTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventInterfereAPTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventInterfereAPTrapSwitchCmd_Object=MibScalar
ruckusZDEventInterfereAPTrapSwitchCmd=_RuckusZDEventInterfereAPTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,26),_RuckusZDEventInterfereAPTrapSwitchCmd_Type())
ruckusZDEventInterfereAPTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventInterfereAPTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPSystemColdStartTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPSystemColdStartTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPSystemColdStartTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPSystemColdStartTrapSwitchCmd=_RuckusZDEventAPSystemColdStartTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,31),_RuckusZDEventAPSystemColdStartTrapSwitchCmd_Type())
ruckusZDEventAPSystemColdStartTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPSystemColdStartTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPSystemWarmStartTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPSystemWarmStartTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPSystemWarmStartTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPSystemWarmStartTrapSwitchCmd=_RuckusZDEventAPSystemWarmStartTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,32),_RuckusZDEventAPSystemWarmStartTrapSwitchCmd_Type())
ruckusZDEventAPSystemWarmStartTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPSystemWarmStartTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPSSIDChangedTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPSSIDChangedTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPSSIDChangedTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPSSIDChangedTrapSwitchCmd=_RuckusZDEventAPSSIDChangedTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,33),_RuckusZDEventAPSSIDChangedTrapSwitchCmd_Type())
ruckusZDEventAPSSIDChangedTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPSSIDChangedTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPClientExceedValveTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPClientExceedValveTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPClientExceedValveTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPClientExceedValveTrapSwitchCmd=_RuckusZDEventAPClientExceedValveTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,34),_RuckusZDEventAPClientExceedValveTrapSwitchCmd_Type())
ruckusZDEventAPClientExceedValveTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPClientExceedValveTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPAvailableStatusTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPAvailableStatusTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPAvailableStatusTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPAvailableStatusTrapSwitchCmd=_RuckusZDEventAPAvailableStatusTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,35),_RuckusZDEventAPAvailableStatusTrapSwitchCmd_Type())
ruckusZDEventAPAvailableStatusTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPAvailableStatusTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd=_RuckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,36),_RuckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd_Type())
ruckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd_Object=MibScalar
ruckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd=_RuckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,37),_RuckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd_Type())
ruckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventSystemMemUtilExceedValveTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventSystemMemUtilExceedValveTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventSystemMemUtilExceedValveTrapSwitchCmd_Object=MibScalar
ruckusZDEventSystemMemUtilExceedValveTrapSwitchCmd=_RuckusZDEventSystemMemUtilExceedValveTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,38),_RuckusZDEventSystemMemUtilExceedValveTrapSwitchCmd_Type())
ruckusZDEventSystemMemUtilExceedValveTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventSystemMemUtilExceedValveTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd_Object=MibScalar
ruckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd=_RuckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,39),_RuckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd_Type())
ruckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd_Object=MibScalar
ruckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd=_RuckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,40),_RuckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd_Type())
ruckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPSyncTimeFailTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPSyncTimeFailTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPSyncTimeFailTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPSyncTimeFailTrapSwitchCmd=_RuckusZDEventAPSyncTimeFailTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,41),_RuckusZDEventAPSyncTimeFailTrapSwitchCmd_Type())
ruckusZDEventAPSyncTimeFailTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPSyncTimeFailTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd_Object=MibScalar
ruckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd=_RuckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,42),_RuckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd_Type())
ruckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventSystemMemUtilClrwarnTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventSystemMemUtilClrwarnTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventSystemMemUtilClrwarnTrapSwitchCmd_Object=MibScalar
ruckusZDEventSystemMemUtilClrwarnTrapSwitchCmd=_RuckusZDEventSystemMemUtilClrwarnTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,43),_RuckusZDEventSystemMemUtilClrwarnTrapSwitchCmd_Type())
ruckusZDEventSystemMemUtilClrwarnTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventSystemMemUtilClrwarnTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventClientJoinTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventClientJoinTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventClientJoinTrapSwitchCmd_Object=MibScalar
ruckusZDEventClientJoinTrapSwitchCmd=_RuckusZDEventClientJoinTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,60),_RuckusZDEventClientJoinTrapSwitchCmd_Type())
ruckusZDEventClientJoinTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventClientJoinTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventClientJoinFailedTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventClientJoinFailedTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventClientJoinFailedTrapSwitchCmd_Object=MibScalar
ruckusZDEventClientJoinFailedTrapSwitchCmd=_RuckusZDEventClientJoinFailedTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,61),_RuckusZDEventClientJoinFailedTrapSwitchCmd_Type())
ruckusZDEventClientJoinFailedTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventClientJoinFailedTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventClientJoinFailedAPBusyTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventClientJoinFailedAPBusyTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventClientJoinFailedAPBusyTrapSwitchCmd_Object=MibScalar
ruckusZDEventClientJoinFailedAPBusyTrapSwitchCmd=_RuckusZDEventClientJoinFailedAPBusyTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,62),_RuckusZDEventClientJoinFailedAPBusyTrapSwitchCmd_Type())
ruckusZDEventClientJoinFailedAPBusyTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventClientJoinFailedAPBusyTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventClientDisconnectTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventClientDisconnectTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventClientDisconnectTrapSwitchCmd_Object=MibScalar
ruckusZDEventClientDisconnectTrapSwitchCmd=_RuckusZDEventClientDisconnectTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,63),_RuckusZDEventClientDisconnectTrapSwitchCmd_Type())
ruckusZDEventClientDisconnectTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventClientDisconnectTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventClientRoamOutTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventClientRoamOutTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventClientRoamOutTrapSwitchCmd_Object=MibScalar
ruckusZDEventClientRoamOutTrapSwitchCmd=_RuckusZDEventClientRoamOutTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,64),_RuckusZDEventClientRoamOutTrapSwitchCmd_Type())
ruckusZDEventClientRoamOutTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventClientRoamOutTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventClientRoamInTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventClientRoamInTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventClientRoamInTrapSwitchCmd_Object=MibScalar
ruckusZDEventClientRoamInTrapSwitchCmd=_RuckusZDEventClientRoamInTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,65),_RuckusZDEventClientRoamInTrapSwitchCmd_Type())
ruckusZDEventClientRoamInTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventClientRoamInTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventClientAuthFailedTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventClientAuthFailedTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventClientAuthFailedTrapSwitchCmd_Object=MibScalar
ruckusZDEventClientAuthFailedTrapSwitchCmd=_RuckusZDEventClientAuthFailedTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,66),_RuckusZDEventClientAuthFailedTrapSwitchCmd_Type())
ruckusZDEventClientAuthFailedTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventClientAuthFailedTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventClientAuthorizationFailedTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventClientAuthorizationFailedTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventClientAuthorizationFailedTrapSwitchCmd_Object=MibScalar
ruckusZDEventClientAuthorizationFailedTrapSwitchCmd=_RuckusZDEventClientAuthorizationFailedTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,67),_RuckusZDEventClientAuthorizationFailedTrapSwitchCmd_Type())
ruckusZDEventClientAuthorizationFailedTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventClientAuthorizationFailedTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPCPUvalveTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPCPUvalveTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPCPUvalveTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPCPUvalveTrapSwitchCmd=_RuckusZDEventAPCPUvalveTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,83),_RuckusZDEventAPCPUvalveTrapSwitchCmd_Type())
ruckusZDEventAPCPUvalveTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPCPUvalveTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPMEMvalveTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPMEMvalveTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPMEMvalveTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPMEMvalveTrapSwitchCmd=_RuckusZDEventAPMEMvalveTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,84),_RuckusZDEventAPMEMvalveTrapSwitchCmd_Type())
ruckusZDEventAPMEMvalveTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPMEMvalveTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPCPUvalveClrwarnTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPCPUvalveClrwarnTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPCPUvalveClrwarnTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPCPUvalveClrwarnTrapSwitchCmd=_RuckusZDEventAPCPUvalveClrwarnTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,85),_RuckusZDEventAPCPUvalveClrwarnTrapSwitchCmd_Type())
ruckusZDEventAPCPUvalveClrwarnTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPCPUvalveClrwarnTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPMEMvalveClrwarnTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPMEMvalveClrwarnTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPMEMvalveClrwarnTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPMEMvalveClrwarnTrapSwitchCmd=_RuckusZDEventAPMEMvalveClrwarnTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,86),_RuckusZDEventAPMEMvalveClrwarnTrapSwitchCmd_Type())
ruckusZDEventAPMEMvalveClrwarnTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPMEMvalveClrwarnTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd_Object=MibScalar
ruckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd=_RuckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,87),_RuckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd_Type())
ruckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventDhcpPoolFullTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventDhcpPoolFullTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventDhcpPoolFullTrapSwitchCmd_Object=MibScalar
ruckusZDEventDhcpPoolFullTrapSwitchCmd=_RuckusZDEventDhcpPoolFullTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,88),_RuckusZDEventDhcpPoolFullTrapSwitchCmd_Type())
ruckusZDEventDhcpPoolFullTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventDhcpPoolFullTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventDhcpPoolAbunTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventDhcpPoolAbunTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventDhcpPoolAbunTrapSwitchCmd_Object=MibScalar
ruckusZDEventDhcpPoolAbunTrapSwitchCmd=_RuckusZDEventDhcpPoolAbunTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,89),_RuckusZDEventDhcpPoolAbunTrapSwitchCmd_Type())
ruckusZDEventDhcpPoolAbunTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventDhcpPoolAbunTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd_Object=MibScalar
ruckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd=_RuckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,100),_RuckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd_Type())
ruckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd_Object=MibScalar
ruckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd=_RuckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,101),_RuckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd_Type())
ruckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd_Object=MibScalar
ruckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd=_RuckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,102),_RuckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd_Type())
ruckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd_Object=MibScalar
ruckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd=_RuckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,103),_RuckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd_Type())
ruckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd_Object=MibScalar
ruckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd=_RuckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,104),_RuckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd_Type())
ruckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventLBSAdminEnabledTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventLBSAdminEnabledTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventLBSAdminEnabledTrapSwitchCmd_Object=MibScalar
ruckusZDEventLBSAdminEnabledTrapSwitchCmd=_RuckusZDEventLBSAdminEnabledTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,120),_RuckusZDEventLBSAdminEnabledTrapSwitchCmd_Type())
ruckusZDEventLBSAdminEnabledTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventLBSAdminEnabledTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventLBSAdminDisabledTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventLBSAdminDisabledTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventLBSAdminDisabledTrapSwitchCmd_Object=MibScalar
ruckusZDEventLBSAdminDisabledTrapSwitchCmd=_RuckusZDEventLBSAdminDisabledTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,121),_RuckusZDEventLBSAdminDisabledTrapSwitchCmd_Type())
ruckusZDEventLBSAdminDisabledTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventLBSAdminDisabledTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventLBSZDLSConnectionUpTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventLBSZDLSConnectionUpTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventLBSZDLSConnectionUpTrapSwitchCmd_Object=MibScalar
ruckusZDEventLBSZDLSConnectionUpTrapSwitchCmd=_RuckusZDEventLBSZDLSConnectionUpTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,122),_RuckusZDEventLBSZDLSConnectionUpTrapSwitchCmd_Type())
ruckusZDEventLBSZDLSConnectionUpTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventLBSZDLSConnectionUpTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventLBSZDLSConnectionDownTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventLBSZDLSConnectionDownTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventLBSZDLSConnectionDownTrapSwitchCmd_Object=MibScalar
ruckusZDEventLBSZDLSConnectionDownTrapSwitchCmd=_RuckusZDEventLBSZDLSConnectionDownTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,123),_RuckusZDEventLBSZDLSConnectionDownTrapSwitchCmd_Type())
ruckusZDEventLBSZDLSConnectionDownTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventLBSZDLSConnectionDownTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd_Object=MibScalar
ruckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd=_RuckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,124),_RuckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd_Type())
ruckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RuckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd_Object=MibScalar
ruckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd=_RuckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,125),_RuckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd_Type())
ruckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd.setStatus(_B)
class _RuckusZDEventALLEventTrapSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_D,0),(_E,1),('hybrid',3)))
_RuckusZDEventALLEventTrapSwitchCmd_Type.__name__=_C
_RuckusZDEventALLEventTrapSwitchCmd_Object=MibScalar
ruckusZDEventALLEventTrapSwitchCmd=_RuckusZDEventALLEventTrapSwitchCmd_Object((1,3,6,1,4,1,25053,2,2,3,200),_RuckusZDEventALLEventTrapSwitchCmd_Type())
ruckusZDEventALLEventTrapSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusZDEventALLEventTrapSwitchCmd.setStatus(_B)
ruckusZDEventAPJoinTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,1))
ruckusZDEventAPJoinTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_O)))
if mibBuilder.loadTexts:ruckusZDEventAPJoinTrap.setStatus(_B)
ruckusZDEventSSIDSpoofTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,2))
ruckusZDEventSSIDSpoofTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_Q)))
if mibBuilder.loadTexts:ruckusZDEventSSIDSpoofTrap.setStatus(_B)
ruckusZDEventMACSpoofTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,3))
ruckusZDEventMACSpoofTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_Q)))
if mibBuilder.loadTexts:ruckusZDEventMACSpoofTrap.setStatus(_B)
ruckusZDEventRogueAPTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,4))
ruckusZDEventRogueAPTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_Q)))
if mibBuilder.loadTexts:ruckusZDEventRogueAPTrap.setStatus(_B)
ruckusZDEventAPLostTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,5))
ruckusZDEventAPLostTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_O)))
if mibBuilder.loadTexts:ruckusZDEventAPLostTrap.setStatus(_B)
ruckusZDEventAPLostHeartbeatTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,6))
ruckusZDEventAPLostHeartbeatTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_O)))
if mibBuilder.loadTexts:ruckusZDEventAPLostHeartbeatTrap.setStatus(_B)
ruckusZDEventClientAuthFailBlockTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,7))
ruckusZDEventClientAuthFailBlockTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_R),(_A,_O),(_A,_Q)))
if mibBuilder.loadTexts:ruckusZDEventClientAuthFailBlockTrap.setStatus(_B)
ruckusZDEventAPResetTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,8))
ruckusZDEventAPResetTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ruckusZDEventAPResetTrap.setStatus(_B)
ruckusZDEventIPChangeTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,9))
ruckusZDEventIPChangeTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventIPChangeTrap.setStatus(_B)
ruckusZDEventSystemColdStartTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,10))
ruckusZDEventSystemColdStartTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventSystemColdStartTrap.setStatus(_B)
ruckusZDEventAPChannelChangeTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,11))
ruckusZDEventAPChannelChangeTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ruckusZDEventAPChannelChangeTrap.setStatus(_B)
ruckusZDEventRadiusAuthUnavailableTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,12))
ruckusZDEventRadiusAuthUnavailableTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventRadiusAuthUnavailableTrap.setStatus(_B)
ruckusZDEventRadiusAcctUnavailableTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,13))
ruckusZDEventRadiusAcctUnavailableTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventRadiusAcctUnavailableTrap.setStatus(_B)
ruckusZDEventClientJoinFailAPBusyTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,14))
ruckusZDEventClientJoinFailAPBusyTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventClientJoinFailAPBusyTrap.setStatus(_B)
ruckusZDEventInterferenceADHoc=NotificationType((1,3,6,1,4,1,25053,2,2,1,15))
ruckusZDEventInterferenceADHoc.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventInterferenceADHoc.setStatus(_B)
ruckusZDEventImageUpgradeFailTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,16))
ruckusZDEventImageUpgradeFailTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventImageUpgradeFailTrap.setStatus(_B)
ruckusZDEventHeartbeatTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,22))
ruckusZDEventHeartbeatTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventHeartbeatTrap.setStatus(_B)
ruckusZDEventAttackedTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,24))
ruckusZDEventAttackedTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventAttackedTrap.setStatus(_B)
ruckusZDEventSystemWarmStartTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,25))
ruckusZDEventSystemWarmStartTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventSystemWarmStartTrap.setStatus(_B)
ruckusZDEventInterfereAPTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,26))
ruckusZDEventInterfereAPTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventInterfereAPTrap.setStatus(_B)
ruckusZDEventAPSystemColdStartTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,31))
ruckusZDEventAPSystemColdStartTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventAPSystemColdStartTrap.setStatus(_B)
ruckusZDEventAPSystemWarmStartTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,32))
ruckusZDEventAPSystemWarmStartTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventAPSystemWarmStartTrap.setStatus(_B)
ruckusZDEventAPSSIDChangedTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,33))
ruckusZDEventAPSSIDChangedTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventAPSSIDChangedTrap.setStatus(_B)
ruckusZDEventAPClientExceedValve=NotificationType((1,3,6,1,4,1,25053,2,2,1,34))
ruckusZDEventAPClientExceedValve.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ruckusZDEventAPClientExceedValve.setStatus(_B)
ruckusZDEventAPAvailableStatusTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,35))
ruckusZDEventAPAvailableStatusTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventAPAvailableStatusTrap.setStatus(_B)
ruckusZDEventAPWirelessInterfaceFaultTrap=NotificationType((1,3,6,1,4,1,25053,2,2,1,36))
ruckusZDEventAPWirelessInterfaceFaultTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventAPWirelessInterfaceFaultTrap.setStatus(_B)
ruckusZDEventSystemCpuUtilExceedValve=NotificationType((1,3,6,1,4,1,25053,2,2,1,37))
ruckusZDEventSystemCpuUtilExceedValve.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventSystemCpuUtilExceedValve.setStatus(_B)
ruckusZDEventSystemMemUtilExceedValve=NotificationType((1,3,6,1,4,1,25053,2,2,1,38))
ruckusZDEventSystemMemUtilExceedValve.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventSystemMemUtilExceedValve.setStatus(_B)
ruckusZDEventSystemBandwidthUtilExceedValve=NotificationType((1,3,6,1,4,1,25053,2,2,1,39))
ruckusZDEventSystemBandwidthUtilExceedValve.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventSystemBandwidthUtilExceedValve.setStatus(_B)
ruckusZDEventSystemDropPacketRateExceedValve=NotificationType((1,3,6,1,4,1,25053,2,2,1,40))
ruckusZDEventSystemDropPacketRateExceedValve.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventSystemDropPacketRateExceedValve.setStatus(_B)
ruckusZDEventAPSyncTimeFail=NotificationType((1,3,6,1,4,1,25053,2,2,1,41))
ruckusZDEventAPSyncTimeFail.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventAPSyncTimeFail.setStatus(_B)
ruckusZDEventSystemCpuUtilClrWarn=NotificationType((1,3,6,1,4,1,25053,2,2,1,42))
ruckusZDEventSystemCpuUtilClrWarn.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventSystemCpuUtilClrWarn.setStatus(_B)
ruckusZDEventSystemMemUtilClrwarn=NotificationType((1,3,6,1,4,1,25053,2,2,1,43))
ruckusZDEventSystemMemUtilClrwarn.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventSystemMemUtilClrwarn.setStatus(_B)
ruckusZDEventClientJoin=NotificationType((1,3,6,1,4,1,25053,2,2,1,60))
ruckusZDEventClientJoin.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_R),(_A,_O),(_A,_Q)))
if mibBuilder.loadTexts:ruckusZDEventClientJoin.setStatus(_B)
ruckusZDEventClientJoinFailed=NotificationType((1,3,6,1,4,1,25053,2,2,1,61))
ruckusZDEventClientJoinFailed.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_R),(_A,_O),(_A,_Q),(_A,_T)))
if mibBuilder.loadTexts:ruckusZDEventClientJoinFailed.setStatus(_B)
ruckusZDEventClientJoinFailedAPBusy=NotificationType((1,3,6,1,4,1,25053,2,2,1,62))
ruckusZDEventClientJoinFailedAPBusy.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_R),(_A,_O),(_A,_Q)))
if mibBuilder.loadTexts:ruckusZDEventClientJoinFailedAPBusy.setStatus(_B)
ruckusZDEventClientDisconnect=NotificationType((1,3,6,1,4,1,25053,2,2,1,63))
ruckusZDEventClientDisconnect.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_R),(_A,_O),(_A,_Q)))
if mibBuilder.loadTexts:ruckusZDEventClientDisconnect.setStatus(_B)
ruckusZDEventClientRoamOut=NotificationType((1,3,6,1,4,1,25053,2,2,1,64))
ruckusZDEventClientRoamOut.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_R),(_A,_O),(_A,_Q)))
if mibBuilder.loadTexts:ruckusZDEventClientRoamOut.setStatus(_B)
ruckusZDEventClientRoamIn=NotificationType((1,3,6,1,4,1,25053,2,2,1,65))
ruckusZDEventClientRoamIn.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_R),(_A,_O),(_A,_Q)))
if mibBuilder.loadTexts:ruckusZDEventClientRoamIn.setStatus(_B)
ruckusZDEventClientAuthFailed=NotificationType((1,3,6,1,4,1,25053,2,2,1,66))
ruckusZDEventClientAuthFailed.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_R),(_A,_O),(_A,_Q),(_A,_T)))
if mibBuilder.loadTexts:ruckusZDEventClientAuthFailed.setStatus(_B)
ruckusZDEventClientAuthorizationFailed=NotificationType((1,3,6,1,4,1,25053,2,2,1,67))
ruckusZDEventClientAuthorizationFailed.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_R),(_A,_O),(_A,_Q)))
if mibBuilder.loadTexts:ruckusZDEventClientAuthorizationFailed.setStatus(_B)
ruckusZDEventAPCPUvalve=NotificationType((1,3,6,1,4,1,25053,2,2,1,83))
ruckusZDEventAPCPUvalve.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ruckusZDEventAPCPUvalve.setStatus(_B)
ruckusZDEventAPMEMvalve=NotificationType((1,3,6,1,4,1,25053,2,2,1,84))
ruckusZDEventAPMEMvalve.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ruckusZDEventAPMEMvalve.setStatus(_B)
ruckusZDEventAPCPUvalveClrwarn=NotificationType((1,3,6,1,4,1,25053,2,2,1,85))
ruckusZDEventAPCPUvalveClrwarn.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ruckusZDEventAPCPUvalveClrwarn.setStatus(_B)
ruckusZDEventAPMEMvalveClrwarn=NotificationType((1,3,6,1,4,1,25053,2,2,1,86))
ruckusZDEventAPMEMvalveClrwarn.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ruckusZDEventAPMEMvalveClrwarn.setStatus(_B)
ruckusZDEventAPNumStaExceedValveClrwarn=NotificationType((1,3,6,1,4,1,25053,2,2,1,87))
ruckusZDEventAPNumStaExceedValveClrwarn.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ruckusZDEventAPNumStaExceedValveClrwarn.setStatus(_B)
ruckusZDEventDhcpPoolFull=NotificationType((1,3,6,1,4,1,25053,2,2,1,88))
ruckusZDEventDhcpPoolFull.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventDhcpPoolFull.setStatus(_B)
ruckusZDEventDhcpPoolAbun=NotificationType((1,3,6,1,4,1,25053,2,2,1,89))
ruckusZDEventDhcpPoolAbun.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventDhcpPoolAbun.setStatus(_B)
ruckusZDEventSmartRedundancyChangetoActive=NotificationType((1,3,6,1,4,1,25053,2,2,1,100))
ruckusZDEventSmartRedundancyChangetoActive.setObjects((_A,_S))
if mibBuilder.loadTexts:ruckusZDEventSmartRedundancyChangetoActive.setStatus(_B)
ruckusZDEventSmartRedundancyActiveConnected=NotificationType((1,3,6,1,4,1,25053,2,2,1,101))
ruckusZDEventSmartRedundancyActiveConnected.setObjects((_A,_S))
if mibBuilder.loadTexts:ruckusZDEventSmartRedundancyActiveConnected.setStatus(_B)
ruckusZDEventSmartRedundancyActiveDisconnected=NotificationType((1,3,6,1,4,1,25053,2,2,1,102))
ruckusZDEventSmartRedundancyActiveDisconnected.setObjects((_A,_S))
if mibBuilder.loadTexts:ruckusZDEventSmartRedundancyActiveDisconnected.setStatus(_B)
ruckusZDEventSmartRedundancyStandbyConnected=NotificationType((1,3,6,1,4,1,25053,2,2,1,103))
ruckusZDEventSmartRedundancyStandbyConnected.setObjects((_A,_S))
if mibBuilder.loadTexts:ruckusZDEventSmartRedundancyStandbyConnected.setStatus(_B)
ruckusZDEventSmartRedundancyStandbyDisconnected=NotificationType((1,3,6,1,4,1,25053,2,2,1,104))
ruckusZDEventSmartRedundancyStandbyDisconnected.setObjects((_A,_S))
if mibBuilder.loadTexts:ruckusZDEventSmartRedundancyStandbyDisconnected.setStatus(_B)
ruckusZDEventLBSAdminEnabled=NotificationType((1,3,6,1,4,1,25053,2,2,1,120))
ruckusZDEventLBSAdminEnabled.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventLBSAdminEnabled.setStatus(_B)
ruckusZDEventLBSAdminDisabled=NotificationType((1,3,6,1,4,1,25053,2,2,1,121))
ruckusZDEventLBSAdminDisabled.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventLBSAdminDisabled.setStatus(_B)
ruckusZDEventLBSZDLSConnectionUp=NotificationType((1,3,6,1,4,1,25053,2,2,1,122))
ruckusZDEventLBSZDLSConnectionUp.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventLBSZDLSConnectionUp.setStatus(_B)
ruckusZDEventLBSZDLSConnectionDown=NotificationType((1,3,6,1,4,1,25053,2,2,1,123))
ruckusZDEventLBSZDLSConnectionDown.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventLBSZDLSConnectionDown.setStatus(_B)
ruckusZDEventLBSReceiveCMDFootfall=NotificationType((1,3,6,1,4,1,25053,2,2,1,124))
ruckusZDEventLBSReceiveCMDFootfall.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventLBSReceiveCMDFootfall.setStatus(_B)
ruckusZDEventLBSReceiveCMDCalibration=NotificationType((1,3,6,1,4,1,25053,2,2,1,125))
ruckusZDEventLBSReceiveCMDCalibration.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ruckusZDEventLBSReceiveCMDCalibration.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ruckusZDEventMIB':ruckusZDEventMIB,'ruckusZDEventTraps':ruckusZDEventTraps,'ruckusZDEventAPJoinTrap':ruckusZDEventAPJoinTrap,'ruckusZDEventSSIDSpoofTrap':ruckusZDEventSSIDSpoofTrap,'ruckusZDEventMACSpoofTrap':ruckusZDEventMACSpoofTrap,'ruckusZDEventRogueAPTrap':ruckusZDEventRogueAPTrap,'ruckusZDEventAPLostTrap':ruckusZDEventAPLostTrap,'ruckusZDEventAPLostHeartbeatTrap':ruckusZDEventAPLostHeartbeatTrap,'ruckusZDEventClientAuthFailBlockTrap':ruckusZDEventClientAuthFailBlockTrap,'ruckusZDEventAPResetTrap':ruckusZDEventAPResetTrap,'ruckusZDEventIPChangeTrap':ruckusZDEventIPChangeTrap,'ruckusZDEventSystemColdStartTrap':ruckusZDEventSystemColdStartTrap,'ruckusZDEventAPChannelChangeTrap':ruckusZDEventAPChannelChangeTrap,'ruckusZDEventRadiusAuthUnavailableTrap':ruckusZDEventRadiusAuthUnavailableTrap,'ruckusZDEventRadiusAcctUnavailableTrap':ruckusZDEventRadiusAcctUnavailableTrap,'ruckusZDEventClientJoinFailAPBusyTrap':ruckusZDEventClientJoinFailAPBusyTrap,'ruckusZDEventInterferenceADHoc':ruckusZDEventInterferenceADHoc,'ruckusZDEventImageUpgradeFailTrap':ruckusZDEventImageUpgradeFailTrap,'ruckusZDEventHeartbeatTrap':ruckusZDEventHeartbeatTrap,'ruckusZDEventAttackedTrap':ruckusZDEventAttackedTrap,'ruckusZDEventSystemWarmStartTrap':ruckusZDEventSystemWarmStartTrap,'ruckusZDEventInterfereAPTrap':ruckusZDEventInterfereAPTrap,'ruckusZDEventAPSystemColdStartTrap':ruckusZDEventAPSystemColdStartTrap,'ruckusZDEventAPSystemWarmStartTrap':ruckusZDEventAPSystemWarmStartTrap,'ruckusZDEventAPSSIDChangedTrap':ruckusZDEventAPSSIDChangedTrap,'ruckusZDEventAPClientExceedValve':ruckusZDEventAPClientExceedValve,'ruckusZDEventAPAvailableStatusTrap':ruckusZDEventAPAvailableStatusTrap,'ruckusZDEventAPWirelessInterfaceFaultTrap':ruckusZDEventAPWirelessInterfaceFaultTrap,'ruckusZDEventSystemCpuUtilExceedValve':ruckusZDEventSystemCpuUtilExceedValve,'ruckusZDEventSystemMemUtilExceedValve':ruckusZDEventSystemMemUtilExceedValve,'ruckusZDEventSystemBandwidthUtilExceedValve':ruckusZDEventSystemBandwidthUtilExceedValve,'ruckusZDEventSystemDropPacketRateExceedValve':ruckusZDEventSystemDropPacketRateExceedValve,'ruckusZDEventAPSyncTimeFail':ruckusZDEventAPSyncTimeFail,'ruckusZDEventSystemCpuUtilClrWarn':ruckusZDEventSystemCpuUtilClrWarn,'ruckusZDEventSystemMemUtilClrwarn':ruckusZDEventSystemMemUtilClrwarn,'ruckusZDEventClientJoin':ruckusZDEventClientJoin,'ruckusZDEventClientJoinFailed':ruckusZDEventClientJoinFailed,'ruckusZDEventClientJoinFailedAPBusy':ruckusZDEventClientJoinFailedAPBusy,'ruckusZDEventClientDisconnect':ruckusZDEventClientDisconnect,'ruckusZDEventClientRoamOut':ruckusZDEventClientRoamOut,'ruckusZDEventClientRoamIn':ruckusZDEventClientRoamIn,'ruckusZDEventClientAuthFailed':ruckusZDEventClientAuthFailed,'ruckusZDEventClientAuthorizationFailed':ruckusZDEventClientAuthorizationFailed,'ruckusZDEventAPCPUvalve':ruckusZDEventAPCPUvalve,'ruckusZDEventAPMEMvalve':ruckusZDEventAPMEMvalve,'ruckusZDEventAPCPUvalveClrwarn':ruckusZDEventAPCPUvalveClrwarn,'ruckusZDEventAPMEMvalveClrwarn':ruckusZDEventAPMEMvalveClrwarn,'ruckusZDEventAPNumStaExceedValveClrwarn':ruckusZDEventAPNumStaExceedValveClrwarn,'ruckusZDEventDhcpPoolFull':ruckusZDEventDhcpPoolFull,'ruckusZDEventDhcpPoolAbun':ruckusZDEventDhcpPoolAbun,'ruckusZDEventSmartRedundancyChangetoActive':ruckusZDEventSmartRedundancyChangetoActive,'ruckusZDEventSmartRedundancyActiveConnected':ruckusZDEventSmartRedundancyActiveConnected,'ruckusZDEventSmartRedundancyActiveDisconnected':ruckusZDEventSmartRedundancyActiveDisconnected,'ruckusZDEventSmartRedundancyStandbyConnected':ruckusZDEventSmartRedundancyStandbyConnected,'ruckusZDEventSmartRedundancyStandbyDisconnected':ruckusZDEventSmartRedundancyStandbyDisconnected,'ruckusZDEventLBSAdminEnabled':ruckusZDEventLBSAdminEnabled,'ruckusZDEventLBSAdminDisabled':ruckusZDEventLBSAdminDisabled,'ruckusZDEventLBSZDLSConnectionUp':ruckusZDEventLBSZDLSConnectionUp,'ruckusZDEventLBSZDLSConnectionDown':ruckusZDEventLBSZDLSConnectionDown,'ruckusZDEventLBSReceiveCMDFootfall':ruckusZDEventLBSReceiveCMDFootfall,'ruckusZDEventLBSReceiveCMDCalibration':ruckusZDEventLBSReceiveCMDCalibration,'ruckusZDEventObjects':ruckusZDEventObjects,_G:ruckusZDEventSerial,_H:ruckusZDEventNEID,_I:ruckusZDEventSeverity,_J:ruckusZDEventType,_K:ruckusZDEventTime,_L:ruckusZDEventStatus,_M:ruckusZDEventTitle,_N:ruckusZDEventContent,_R:ruckusZDEventClientMacAddr,_O:ruckusZDEventAPMacAddr,'ruckusZDEventRogueMacAddr':ruckusZDEventRogueMacAddr,_Q:ruckusZDEventSSID,'ruckusZDEventChannel':ruckusZDEventChannel,_T:ruckusZDEventReason,_S:ruckusZDEventIpAddr,'ruckusZDEventTrapSwitchCmd':ruckusZDEventTrapSwitchCmd,'ruckusZDEventAPJoinTrapSwitchCmd':ruckusZDEventAPJoinTrapSwitchCmd,'ruckusZDEventSSIDSpoofTrapSwitchCmd':ruckusZDEventSSIDSpoofTrapSwitchCmd,'ruckusZDEventMACSpoofTrapSwitchCmd':ruckusZDEventMACSpoofTrapSwitchCmd,'ruckusZDEventRogueAPTrapSwitchCmd':ruckusZDEventRogueAPTrapSwitchCmd,'ruckusZDEventAPLostTrapSwitchCmd':ruckusZDEventAPLostTrapSwitchCmd,'ruckusZDEventAPLostHeartbeatTrapSwitchCmd':ruckusZDEventAPLostHeartbeatTrapSwitchCmd,'ruckusZDEventClientAuthFailBlockTrapSwitchCmd':ruckusZDEventClientAuthFailBlockTrapSwitchCmd,'ruckusZDEventAPResetSwitchCmd':ruckusZDEventAPResetSwitchCmd,'ruckusZDEventIPChangeSwitchCmd':ruckusZDEventIPChangeSwitchCmd,'ruckusZDEventSystemColdStartTrapSwitchCmd':ruckusZDEventSystemColdStartTrapSwitchCmd,'ruckusZDEventAPChannelChangeTrapSwitchCmd':ruckusZDEventAPChannelChangeTrapSwitchCmd,'ruckusZDEventRadiusAuthUnavailableTrapSwitchCmd':ruckusZDEventRadiusAuthUnavailableTrapSwitchCmd,'ruckusZDEventRadiusAcctUnavailableTrapSwitchCmd':ruckusZDEventRadiusAcctUnavailableTrapSwitchCmd,'ruckusZDEventClientJoinFailAPBusyTrapSwitchCmd':ruckusZDEventClientJoinFailAPBusyTrapSwitchCmd,'ruckusZDEventInterferenceADHocTrapSwitchCmd':ruckusZDEventInterferenceADHocTrapSwitchCmd,'ruckusZDEventImageUpgradeFailTrapSwitchCmd':ruckusZDEventImageUpgradeFailTrapSwitchCmd,'ruckusZDEventHeartbeatTrapSwitchCmd':ruckusZDEventHeartbeatTrapSwitchCmd,'ruckusZDEventAttackedTrapSwitchCmd':ruckusZDEventAttackedTrapSwitchCmd,'ruckusZDEventSystemWarmStartTrapSwitchCmd':ruckusZDEventSystemWarmStartTrapSwitchCmd,'ruckusZDEventInterfereAPTrapSwitchCmd':ruckusZDEventInterfereAPTrapSwitchCmd,'ruckusZDEventAPSystemColdStartTrapSwitchCmd':ruckusZDEventAPSystemColdStartTrapSwitchCmd,'ruckusZDEventAPSystemWarmStartTrapSwitchCmd':ruckusZDEventAPSystemWarmStartTrapSwitchCmd,'ruckusZDEventAPSSIDChangedTrapSwitchCmd':ruckusZDEventAPSSIDChangedTrapSwitchCmd,'ruckusZDEventAPClientExceedValveTrapSwitchCmd':ruckusZDEventAPClientExceedValveTrapSwitchCmd,'ruckusZDEventAPAvailableStatusTrapSwitchCmd':ruckusZDEventAPAvailableStatusTrapSwitchCmd,'ruckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd':ruckusZDEventAPWirelessInterfaceFaultTrapSwitchCmd,'ruckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd':ruckusZDEventSystemCpuUtilExceedValveTrapSwitchCmd,'ruckusZDEventSystemMemUtilExceedValveTrapSwitchCmd':ruckusZDEventSystemMemUtilExceedValveTrapSwitchCmd,'ruckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd':ruckusZDEventSystemBandwidthUtilExceedValveTrapSwitchCmd,'ruckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd':ruckusZDEventSystemDropPacketRateExceedValveTrapSwitchCmd,'ruckusZDEventAPSyncTimeFailTrapSwitchCmd':ruckusZDEventAPSyncTimeFailTrapSwitchCmd,'ruckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd':ruckusZDEventSystemCpuUtilClrWarnTrapSwitchCmd,'ruckusZDEventSystemMemUtilClrwarnTrapSwitchCmd':ruckusZDEventSystemMemUtilClrwarnTrapSwitchCmd,'ruckusZDEventClientJoinTrapSwitchCmd':ruckusZDEventClientJoinTrapSwitchCmd,'ruckusZDEventClientJoinFailedTrapSwitchCmd':ruckusZDEventClientJoinFailedTrapSwitchCmd,'ruckusZDEventClientJoinFailedAPBusyTrapSwitchCmd':ruckusZDEventClientJoinFailedAPBusyTrapSwitchCmd,'ruckusZDEventClientDisconnectTrapSwitchCmd':ruckusZDEventClientDisconnectTrapSwitchCmd,'ruckusZDEventClientRoamOutTrapSwitchCmd':ruckusZDEventClientRoamOutTrapSwitchCmd,'ruckusZDEventClientRoamInTrapSwitchCmd':ruckusZDEventClientRoamInTrapSwitchCmd,'ruckusZDEventClientAuthFailedTrapSwitchCmd':ruckusZDEventClientAuthFailedTrapSwitchCmd,'ruckusZDEventClientAuthorizationFailedTrapSwitchCmd':ruckusZDEventClientAuthorizationFailedTrapSwitchCmd,'ruckusZDEventAPCPUvalveTrapSwitchCmd':ruckusZDEventAPCPUvalveTrapSwitchCmd,'ruckusZDEventAPMEMvalveTrapSwitchCmd':ruckusZDEventAPMEMvalveTrapSwitchCmd,'ruckusZDEventAPCPUvalveClrwarnTrapSwitchCmd':ruckusZDEventAPCPUvalveClrwarnTrapSwitchCmd,'ruckusZDEventAPMEMvalveClrwarnTrapSwitchCmd':ruckusZDEventAPMEMvalveClrwarnTrapSwitchCmd,'ruckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd':ruckusZDEventAPNumStaExceedValveClrwarnTrapSwitchCmd,'ruckusZDEventDhcpPoolFullTrapSwitchCmd':ruckusZDEventDhcpPoolFullTrapSwitchCmd,'ruckusZDEventDhcpPoolAbunTrapSwitchCmd':ruckusZDEventDhcpPoolAbunTrapSwitchCmd,'ruckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd':ruckusZDEventSmartRedundancyChangetoActiveTrapSwitchCmd,'ruckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd':ruckusZDEventSmartRedundancyActiveConnectedTrapSwitchCmd,'ruckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd':ruckusZDEventSmartRedundancyActiveDisconnectedTrapSwitchCmd,'ruckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd':ruckusZDEventSmartRedundancyStandbyConnectedTrapSwitchCmd,'ruckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd':ruckusZDEventSmartRedundancyStandbyDisconnectedTrapSwitchCmd,'ruckusZDEventLBSAdminEnabledTrapSwitchCmd':ruckusZDEventLBSAdminEnabledTrapSwitchCmd,'ruckusZDEventLBSAdminDisabledTrapSwitchCmd':ruckusZDEventLBSAdminDisabledTrapSwitchCmd,'ruckusZDEventLBSZDLSConnectionUpTrapSwitchCmd':ruckusZDEventLBSZDLSConnectionUpTrapSwitchCmd,'ruckusZDEventLBSZDLSConnectionDownTrapSwitchCmd':ruckusZDEventLBSZDLSConnectionDownTrapSwitchCmd,'ruckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd':ruckusZDEventLBSReceiveCMDFootfallTrapSwitchCmd,'ruckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd':ruckusZDEventLBSReceiveCMDCalibrationTrapSwitchCmd,'ruckusZDEventALLEventTrapSwitchCmd':ruckusZDEventALLEventTrapSwitchCmd})