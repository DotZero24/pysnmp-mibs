_R='mwWncIpv6VarsTableIndex'
_Q='mwWncMobilityVarsTableIndex'
_P='mwUdpBcastDownstreamBridgedTableIndex'
_O='mwUdpBcastUpstreamBridgedTableIndex'
_N='mwDhcpServerTableIndex'
_M='mwVirtualInterfaceProfileTableIndex'
_L='mwWncNetworkConfigTableIndex'
_K='mwDnsServerTableIndex'
_J='mwUdpBcastDownstreamTableIndex'
_I='mwUdpBcastUpstreamTableIndex'
_H='Integer32'
_G='not-accessible'
_F='MERU-CONFIG-CONTROLLER-MIB'
_E='DisplayString'
_D='read-only'
_C='read-write'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwConfiguration,=mibBuilder.importSymbols('MERU-SMI','mwConfiguration')
MwlAlarmState,MwlAvailabilityStatus,MwlBonding,MwlControllerHwType,MwlEnableDisableOption,MwlOnOffSwitch,MwlOperationalState,MwlRegionSettings,MwlVpnClientProtocol,MwlVpnConnectivityStatus=mibBuilder.importSymbols('MERU-TC','MwlAlarmState','MwlAvailabilityStatus','MwlBonding','MwlControllerHwType','MwlEnableDisableOption','MwlOnOffSwitch','MwlOperationalState','MwlRegionSettings','MwlVpnClientProtocol','MwlVpnConnectivityStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwConfigController=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,1))
_MwWncVars_ObjectIdentity=ObjectIdentity
mwWncVars=_MwWncVars_ObjectIdentity((1,3,6,1,4,1,15983,1,1,4,1,1))
_MwWncVarsDescr_Type=DisplayString
_MwWncVarsDescr_Object=MibScalar
mwWncVarsDescr=_MwWncVarsDescr_Object((1,3,6,1,4,1,15983,1,1,4,1,1,1),_MwWncVarsDescr_Type())
mwWncVarsDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:mwWncVarsDescr.setStatus(_A)
class _MwWncVarsLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_MwWncVarsLocation_Type.__name__=_E
_MwWncVarsLocation_Object=MibScalar
mwWncVarsLocation=_MwWncVarsLocation_Object((1,3,6,1,4,1,15983,1,1,4,1,1,2),_MwWncVarsLocation_Type())
mwWncVarsLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:mwWncVarsLocation.setStatus(_A)
class _MwWncVarsContact_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_MwWncVarsContact_Type.__name__=_E
_MwWncVarsContact_Object=MibScalar
mwWncVarsContact=_MwWncVarsContact_Object((1,3,6,1,4,1,15983,1,1,4,1,1,3),_MwWncVarsContact_Type())
mwWncVarsContact.setMaxAccess(_C)
if mibBuilder.loadTexts:mwWncVarsContact.setStatus(_A)
_MwWncVarsAutoApUpgrade_Type=MwlOnOffSwitch
_MwWncVarsAutoApUpgrade_Object=MibScalar
mwWncVarsAutoApUpgrade=_MwWncVarsAutoApUpgrade_Object((1,3,6,1,4,1,15983,1,1,4,1,1,4),_MwWncVarsAutoApUpgrade_Type())
mwWncVarsAutoApUpgrade.setMaxAccess(_C)
if mibBuilder.loadTexts:mwWncVarsAutoApUpgrade.setStatus(_A)
_MwWncVarsDhcpServer_Type=IpAddress
_MwWncVarsDhcpServer_Object=MibScalar
mwWncVarsDhcpServer=_MwWncVarsDhcpServer_Object((1,3,6,1,4,1,15983,1,1,4,1,1,5),_MwWncVarsDhcpServer_Type())
mwWncVarsDhcpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:mwWncVarsDhcpServer.setStatus(_A)
class _MwWncVarsStatPollingPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MwWncVarsStatPollingPeriod_Type.__name__=_H
_MwWncVarsStatPollingPeriod_Object=MibScalar
mwWncVarsStatPollingPeriod=_MwWncVarsStatPollingPeriod_Object((1,3,6,1,4,1,15983,1,1,4,1,1,6),_MwWncVarsStatPollingPeriod_Type())
mwWncVarsStatPollingPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:mwWncVarsStatPollingPeriod.setStatus(_A)
class _MwWncVarsAuditPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MwWncVarsAuditPeriod_Type.__name__=_H
_MwWncVarsAuditPeriod_Object=MibScalar
mwWncVarsAuditPeriod=_MwWncVarsAuditPeriod_Object((1,3,6,1,4,1,15983,1,1,4,1,1,7),_MwWncVarsAuditPeriod_Type())
mwWncVarsAuditPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:mwWncVarsAuditPeriod.setStatus(_A)
class _MwWncVarsApInitScript_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MwWncVarsApInitScript_Type.__name__=_E
_MwWncVarsApInitScript_Object=MibScalar
mwWncVarsApInitScript=_MwWncVarsApInitScript_Object((1,3,6,1,4,1,15983,1,1,4,1,1,8),_MwWncVarsApInitScript_Type())
mwWncVarsApInitScript.setMaxAccess(_C)
if mibBuilder.loadTexts:mwWncVarsApInitScript.setStatus(_A)
_MwWncVarsDhcpRelayPassThroughFlag_Type=MwlOnOffSwitch
_MwWncVarsDhcpRelayPassThroughFlag_Object=MibScalar
mwWncVarsDhcpRelayPassThroughFlag=_MwWncVarsDhcpRelayPassThroughFlag_Object((1,3,6,1,4,1,15983,1,1,4,1,1,9),_MwWncVarsDhcpRelayPassThroughFlag_Type())
mwWncVarsDhcpRelayPassThroughFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:mwWncVarsDhcpRelayPassThroughFlag.setStatus(_A)
_MwWncVarsManagementFromWirelessClients_Type=MwlOnOffSwitch
_MwWncVarsManagementFromWirelessClients_Object=MibScalar
mwWncVarsManagementFromWirelessClients=_MwWncVarsManagementFromWirelessClients_Object((1,3,6,1,4,1,15983,1,1,4,1,1,10),_MwWncVarsManagementFromWirelessClients_Type())
mwWncVarsManagementFromWirelessClients.setMaxAccess(_C)
if mibBuilder.loadTexts:mwWncVarsManagementFromWirelessClients.setStatus(_A)
class _MwWncVarsControllerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_MwWncVarsControllerIndex_Type.__name__=_H
_MwWncVarsControllerIndex_Object=MibScalar
mwWncVarsControllerIndex=_MwWncVarsControllerIndex_Object((1,3,6,1,4,1,15983,1,1,4,1,1,11),_MwWncVarsControllerIndex_Type())
mwWncVarsControllerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mwWncVarsControllerIndex.setStatus(_A)
_MwWncVarsFastPath_Type=MwlOnOffSwitch
_MwWncVarsFastPath_Object=MibScalar
mwWncVarsFastPath=_MwWncVarsFastPath_Object((1,3,6,1,4,1,15983,1,1,4,1,1,14),_MwWncVarsFastPath_Type())
mwWncVarsFastPath.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsFastPath.setStatus(_A)
_MwWncVarsBonding_Type=MwlBonding
_MwWncVarsBonding_Object=MibScalar
mwWncVarsBonding=_MwWncVarsBonding_Object((1,3,6,1,4,1,15983,1,1,4,1,1,15),_MwWncVarsBonding_Type())
mwWncVarsBonding.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsBonding.setStatus(_A)
_MwWncVarsNodeId_Type=Integer32
_MwWncVarsNodeId_Object=MibScalar
mwWncVarsNodeId=_MwWncVarsNodeId_Object((1,3,6,1,4,1,15983,1,1,4,1,1,18),_MwWncVarsNodeId_Type())
mwWncVarsNodeId.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsNodeId.setStatus(_A)
_MwWncVarsHostName_Type=DisplayString
_MwWncVarsHostName_Object=MibScalar
mwWncVarsHostName=_MwWncVarsHostName_Object((1,3,6,1,4,1,15983,1,1,4,1,1,19),_MwWncVarsHostName_Type())
mwWncVarsHostName.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsHostName.setStatus(_A)
_MwWncVarsUpTime_Type=TimeTicks
_MwWncVarsUpTime_Object=MibScalar
mwWncVarsUpTime=_MwWncVarsUpTime_Object((1,3,6,1,4,1,15983,1,1,4,1,1,20),_MwWncVarsUpTime_Type())
mwWncVarsUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsUpTime.setStatus(_A)
_MwWncVarsOperationalState_Type=MwlOperationalState
_MwWncVarsOperationalState_Object=MibScalar
mwWncVarsOperationalState=_MwWncVarsOperationalState_Object((1,3,6,1,4,1,15983,1,1,4,1,1,21),_MwWncVarsOperationalState_Type())
mwWncVarsOperationalState.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsOperationalState.setStatus(_A)
_MwWncVarsAvailabilityStatus_Type=MwlAvailabilityStatus
_MwWncVarsAvailabilityStatus_Object=MibScalar
mwWncVarsAvailabilityStatus=_MwWncVarsAvailabilityStatus_Object((1,3,6,1,4,1,15983,1,1,4,1,1,22),_MwWncVarsAvailabilityStatus_Type())
mwWncVarsAvailabilityStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsAvailabilityStatus.setStatus(_A)
_MwWncVarsAlarmState_Type=MwlAlarmState
_MwWncVarsAlarmState_Object=MibScalar
mwWncVarsAlarmState=_MwWncVarsAlarmState_Object((1,3,6,1,4,1,15983,1,1,4,1,1,23),_MwWncVarsAlarmState_Type())
mwWncVarsAlarmState.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsAlarmState.setStatus(_A)
_MwWncVarsVirtualIpAddress_Type=IpAddress
_MwWncVarsVirtualIpAddress_Object=MibScalar
mwWncVarsVirtualIpAddress=_MwWncVarsVirtualIpAddress_Object((1,3,6,1,4,1,15983,1,1,4,1,1,24),_MwWncVarsVirtualIpAddress_Type())
mwWncVarsVirtualIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsVirtualIpAddress.setStatus(_A)
_MwWncVarsVirtualNetMask_Type=IpAddress
_MwWncVarsVirtualNetMask_Object=MibScalar
mwWncVarsVirtualNetMask=_MwWncVarsVirtualNetMask_Object((1,3,6,1,4,1,15983,1,1,4,1,1,25),_MwWncVarsVirtualNetMask_Type())
mwWncVarsVirtualNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsVirtualNetMask.setStatus(_A)
_MwWncVarsDefaultGatewayAddr_Type=IpAddress
_MwWncVarsDefaultGatewayAddr_Object=MibScalar
mwWncVarsDefaultGatewayAddr=_MwWncVarsDefaultGatewayAddr_Object((1,3,6,1,4,1,15983,1,1,4,1,1,26),_MwWncVarsDefaultGatewayAddr_Type())
mwWncVarsDefaultGatewayAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsDefaultGatewayAddr.setStatus(_A)
_MwWncVarsSoftwareVersion_Type=DisplayString
_MwWncVarsSoftwareVersion_Object=MibScalar
mwWncVarsSoftwareVersion=_MwWncVarsSoftwareVersion_Object((1,3,6,1,4,1,15983,1,1,4,1,1,27),_MwWncVarsSoftwareVersion_Type())
mwWncVarsSoftwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsSoftwareVersion.setStatus(_A)
_MwWncVarsSerialNumber_Type=DisplayString
_MwWncVarsSerialNumber_Object=MibScalar
mwWncVarsSerialNumber=_MwWncVarsSerialNumber_Object((1,3,6,1,4,1,15983,1,1,4,1,1,28),_MwWncVarsSerialNumber_Type())
mwWncVarsSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsSerialNumber.setStatus(_A)
_MwWncVarsSystemId_Type=DisplayString
_MwWncVarsSystemId_Object=MibScalar
mwWncVarsSystemId=_MwWncVarsSystemId_Object((1,3,6,1,4,1,15983,1,1,4,1,1,29),_MwWncVarsSystemId_Type())
mwWncVarsSystemId.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsSystemId.setStatus(_A)
_MwWncVarsHardwareType_Type=MwlControllerHwType
_MwWncVarsHardwareType_Object=MibScalar
mwWncVarsHardwareType=_MwWncVarsHardwareType_Object((1,3,6,1,4,1,15983,1,1,4,1,1,30),_MwWncVarsHardwareType_Type())
mwWncVarsHardwareType.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsHardwareType.setStatus(_A)
_MwWncVarsCountry_Type=DisplayString
_MwWncVarsCountry_Object=MibScalar
mwWncVarsCountry=_MwWncVarsCountry_Object((1,3,6,1,4,1,15983,1,1,4,1,1,31),_MwWncVarsCountry_Type())
mwWncVarsCountry.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsCountry.setStatus(_A)
_MwWncVarsManSerialNumber_Type=DisplayString
_MwWncVarsManSerialNumber_Object=MibScalar
mwWncVarsManSerialNumber=_MwWncVarsManSerialNumber_Object((1,3,6,1,4,1,15983,1,1,4,1,1,32),_MwWncVarsManSerialNumber_Type())
mwWncVarsManSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsManSerialNumber.setStatus(_A)
class _MwWncVarsStationAgingOutPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MwWncVarsStationAgingOutPeriod_Type.__name__=_H
_MwWncVarsStationAgingOutPeriod_Object=MibScalar
mwWncVarsStationAgingOutPeriod=_MwWncVarsStationAgingOutPeriod_Object((1,3,6,1,4,1,15983,1,1,4,1,1,33),_MwWncVarsStationAgingOutPeriod_Type())
mwWncVarsStationAgingOutPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:mwWncVarsStationAgingOutPeriod.setStatus(_A)
_MwWncVarsRoamingDomainState_Type=MwlEnableDisableOption
_MwWncVarsRoamingDomainState_Object=MibScalar
mwWncVarsRoamingDomainState=_MwWncVarsRoamingDomainState_Object((1,3,6,1,4,1,15983,1,1,4,1,1,34),_MwWncVarsRoamingDomainState_Type())
mwWncVarsRoamingDomainState.setMaxAccess(_C)
if mibBuilder.loadTexts:mwWncVarsRoamingDomainState.setStatus(_A)
_MwWncVarsL3RoutingMode_Type=MwlOnOffSwitch
_MwWncVarsL3RoutingMode_Object=MibScalar
mwWncVarsL3RoutingMode=_MwWncVarsL3RoutingMode_Object((1,3,6,1,4,1,15983,1,1,4,1,1,37),_MwWncVarsL3RoutingMode_Type())
mwWncVarsL3RoutingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsL3RoutingMode.setStatus(_A)
_MwWncVarsRegion_Type=MwlRegionSettings
_MwWncVarsRegion_Object=MibScalar
mwWncVarsRegion=_MwWncVarsRegion_Object((1,3,6,1,4,1,15983,1,1,4,1,1,38),_MwWncVarsRegion_Type())
mwWncVarsRegion.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWncVarsRegion.setStatus(_A)
_MwWncVarsRoamingTimeOutPeriod_Type=Unsigned32
_MwWncVarsRoamingTimeOutPeriod_Object=MibScalar
mwWncVarsRoamingTimeOutPeriod=_MwWncVarsRoamingTimeOutPeriod_Object((1,3,6,1,4,1,15983,1,1,4,1,1,41),_MwWncVarsRoamingTimeOutPeriod_Type())
mwWncVarsRoamingTimeOutPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:mwWncVarsRoamingTimeOutPeriod.setStatus(_A)
_MwSystemFileVars_ObjectIdentity=ObjectIdentity
mwSystemFileVars=_MwSystemFileVars_ObjectIdentity((1,3,6,1,4,1,15983,1,1,4,1,3))
class _MwSystemFileVarspHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MwSystemFileVarspHostName_Type.__name__=_E
_MwSystemFileVarspHostName_Object=MibScalar
mwSystemFileVarspHostName=_MwSystemFileVarspHostName_Object((1,3,6,1,4,1,15983,1,1,4,1,3,1),_MwSystemFileVarspHostName_Type())
mwSystemFileVarspHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:mwSystemFileVarspHostName.setStatus(_A)
class _MwSystemFileVarspDnsDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MwSystemFileVarspDnsDomainName_Type.__name__=_E
_MwSystemFileVarspDnsDomainName_Object=MibScalar
mwSystemFileVarspDnsDomainName=_MwSystemFileVarspDnsDomainName_Object((1,3,6,1,4,1,15983,1,1,4,1,3,2),_MwSystemFileVarspDnsDomainName_Type())
mwSystemFileVarspDnsDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:mwSystemFileVarspDnsDomainName.setStatus(_A)
_MwUdpBcastUpstreamTable_Object=MibTable
mwUdpBcastUpstreamTable=_MwUdpBcastUpstreamTable_Object((1,3,6,1,4,1,15983,1,1,4,1,4))
if mibBuilder.loadTexts:mwUdpBcastUpstreamTable.setStatus(_A)
_MwUdpBcastUpstreamEntry_Object=MibTableRow
mwUdpBcastUpstreamEntry=_MwUdpBcastUpstreamEntry_Object((1,3,6,1,4,1,15983,1,1,4,1,4,1))
mwUdpBcastUpstreamEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:mwUdpBcastUpstreamEntry.setStatus(_A)
_MwUdpBcastUpstreamTableIndex_Type=Integer32
_MwUdpBcastUpstreamTableIndex_Object=MibTableColumn
mwUdpBcastUpstreamTableIndex=_MwUdpBcastUpstreamTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,1,4,1,1),_MwUdpBcastUpstreamTableIndex_Type())
mwUdpBcastUpstreamTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwUdpBcastUpstreamTableIndex.setStatus(_A)
_MwUdpBcastUpstreamPort_Type=Unsigned32
_MwUdpBcastUpstreamPort_Object=MibTableColumn
mwUdpBcastUpstreamPort=_MwUdpBcastUpstreamPort_Object((1,3,6,1,4,1,15983,1,1,4,1,4,1,2),_MwUdpBcastUpstreamPort_Type())
mwUdpBcastUpstreamPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mwUdpBcastUpstreamPort.setStatus(_A)
_MwUdpBcastUpstreamRowStatus_Type=RowStatus
_MwUdpBcastUpstreamRowStatus_Object=MibTableColumn
mwUdpBcastUpstreamRowStatus=_MwUdpBcastUpstreamRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,1,4,1,3),_MwUdpBcastUpstreamRowStatus_Type())
mwUdpBcastUpstreamRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwUdpBcastUpstreamRowStatus.setStatus(_A)
_MwUdpBcastDownstreamTable_Object=MibTable
mwUdpBcastDownstreamTable=_MwUdpBcastDownstreamTable_Object((1,3,6,1,4,1,15983,1,1,4,1,5))
if mibBuilder.loadTexts:mwUdpBcastDownstreamTable.setStatus(_A)
_MwUdpBcastDownstreamEntry_Object=MibTableRow
mwUdpBcastDownstreamEntry=_MwUdpBcastDownstreamEntry_Object((1,3,6,1,4,1,15983,1,1,4,1,5,1))
mwUdpBcastDownstreamEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:mwUdpBcastDownstreamEntry.setStatus(_A)
_MwUdpBcastDownstreamTableIndex_Type=Integer32
_MwUdpBcastDownstreamTableIndex_Object=MibTableColumn
mwUdpBcastDownstreamTableIndex=_MwUdpBcastDownstreamTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,1,5,1,1),_MwUdpBcastDownstreamTableIndex_Type())
mwUdpBcastDownstreamTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwUdpBcastDownstreamTableIndex.setStatus(_A)
_MwUdpBcastDownstreamPort_Type=Unsigned32
_MwUdpBcastDownstreamPort_Object=MibTableColumn
mwUdpBcastDownstreamPort=_MwUdpBcastDownstreamPort_Object((1,3,6,1,4,1,15983,1,1,4,1,5,1,2),_MwUdpBcastDownstreamPort_Type())
mwUdpBcastDownstreamPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mwUdpBcastDownstreamPort.setStatus(_A)
_MwUdpBcastDownstreamRowStatus_Type=RowStatus
_MwUdpBcastDownstreamRowStatus_Object=MibTableColumn
mwUdpBcastDownstreamRowStatus=_MwUdpBcastDownstreamRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,1,5,1,3),_MwUdpBcastDownstreamRowStatus_Type())
mwUdpBcastDownstreamRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwUdpBcastDownstreamRowStatus.setStatus(_A)
_MwDnsServerTable_Object=MibTable
mwDnsServerTable=_MwDnsServerTable_Object((1,3,6,1,4,1,15983,1,1,4,1,6))
if mibBuilder.loadTexts:mwDnsServerTable.setStatus(_A)
_MwDnsServerEntry_Object=MibTableRow
mwDnsServerEntry=_MwDnsServerEntry_Object((1,3,6,1,4,1,15983,1,1,4,1,6,1))
mwDnsServerEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:mwDnsServerEntry.setStatus(_A)
_MwDnsServerTableIndex_Type=Integer32
_MwDnsServerTableIndex_Object=MibTableColumn
mwDnsServerTableIndex=_MwDnsServerTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,1,6,1,1),_MwDnsServerTableIndex_Type())
mwDnsServerTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwDnsServerTableIndex.setStatus(_A)
_MwDnsServer_Type=IpAddress
_MwDnsServer_Object=MibTableColumn
mwDnsServer=_MwDnsServer_Object((1,3,6,1,4,1,15983,1,1,4,1,6,1,2),_MwDnsServer_Type())
mwDnsServer.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDnsServer.setStatus(_A)
_MwDnsServerRowStatus_Type=RowStatus
_MwDnsServerRowStatus_Object=MibTableColumn
mwDnsServerRowStatus=_MwDnsServerRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,1,6,1,3),_MwDnsServerRowStatus_Type())
mwDnsServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDnsServerRowStatus.setStatus(_A)
_MwWncNetworkConfigTable_Object=MibTable
mwWncNetworkConfigTable=_MwWncNetworkConfigTable_Object((1,3,6,1,4,1,15983,1,1,4,1,7))
if mibBuilder.loadTexts:mwWncNetworkConfigTable.setStatus(_A)
_MwWncNetworkConfigEntry_Object=MibTableRow
mwWncNetworkConfigEntry=_MwWncNetworkConfigEntry_Object((1,3,6,1,4,1,15983,1,1,4,1,7,1))
mwWncNetworkConfigEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:mwWncNetworkConfigEntry.setStatus(_A)
_MwWncNetworkConfigTableIndex_Type=Integer32
_MwWncNetworkConfigTableIndex_Object=MibTableColumn
mwWncNetworkConfigTableIndex=_MwWncNetworkConfigTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,1,7,1,1),_MwWncNetworkConfigTableIndex_Type())
mwWncNetworkConfigTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwWncNetworkConfigTableIndex.setStatus(_A)
_MwWncNetworkConfigFastPath_Type=MwlOnOffSwitch
_MwWncNetworkConfigFastPath_Object=MibTableColumn
mwWncNetworkConfigFastPath=_MwWncNetworkConfigFastPath_Object((1,3,6,1,4,1,15983,1,1,4,1,7,1,2),_MwWncNetworkConfigFastPath_Type())
mwWncNetworkConfigFastPath.setMaxAccess(_B)
if mibBuilder.loadTexts:mwWncNetworkConfigFastPath.setStatus(_A)
_MwWncNetworkConfigBonding_Type=MwlBonding
_MwWncNetworkConfigBonding_Object=MibTableColumn
mwWncNetworkConfigBonding=_MwWncNetworkConfigBonding_Object((1,3,6,1,4,1,15983,1,1,4,1,7,1,3),_MwWncNetworkConfigBonding_Type())
mwWncNetworkConfigBonding.setMaxAccess(_B)
if mibBuilder.loadTexts:mwWncNetworkConfigBonding.setStatus(_A)
_MwWncNetworkConfigTenGigModule_Type=MwlEnableDisableOption
_MwWncNetworkConfigTenGigModule_Object=MibTableColumn
mwWncNetworkConfigTenGigModule=_MwWncNetworkConfigTenGigModule_Object((1,3,6,1,4,1,15983,1,1,4,1,7,1,4),_MwWncNetworkConfigTenGigModule_Type())
mwWncNetworkConfigTenGigModule.setMaxAccess(_B)
if mibBuilder.loadTexts:mwWncNetworkConfigTenGigModule.setStatus(_A)
_MwWncNetworkConfigRebridHandOffLogic_Type=MwlOnOffSwitch
_MwWncNetworkConfigRebridHandOffLogic_Object=MibTableColumn
mwWncNetworkConfigRebridHandOffLogic=_MwWncNetworkConfigRebridHandOffLogic_Object((1,3,6,1,4,1,15983,1,1,4,1,7,1,5),_MwWncNetworkConfigRebridHandOffLogic_Type())
mwWncNetworkConfigRebridHandOffLogic.setMaxAccess(_B)
if mibBuilder.loadTexts:mwWncNetworkConfigRebridHandOffLogic.setStatus(_A)
_MwWncNetworkConfigOneGigSFP_Type=MwlEnableDisableOption
_MwWncNetworkConfigOneGigSFP_Object=MibTableColumn
mwWncNetworkConfigOneGigSFP=_MwWncNetworkConfigOneGigSFP_Object((1,3,6,1,4,1,15983,1,1,4,1,7,1,6),_MwWncNetworkConfigOneGigSFP_Type())
mwWncNetworkConfigOneGigSFP.setMaxAccess(_B)
if mibBuilder.loadTexts:mwWncNetworkConfigOneGigSFP.setStatus(_A)
_MwWncNetworkConfigRowStatus_Type=RowStatus
_MwWncNetworkConfigRowStatus_Object=MibTableColumn
mwWncNetworkConfigRowStatus=_MwWncNetworkConfigRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,1,7,1,7),_MwWncNetworkConfigRowStatus_Type())
mwWncNetworkConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwWncNetworkConfigRowStatus.setStatus(_A)
_MwVirtualInterfaceProfileTable_Object=MibTable
mwVirtualInterfaceProfileTable=_MwVirtualInterfaceProfileTable_Object((1,3,6,1,4,1,15983,1,1,4,1,8))
if mibBuilder.loadTexts:mwVirtualInterfaceProfileTable.setStatus(_A)
_MwVirtualInterfaceProfileEntry_Object=MibTableRow
mwVirtualInterfaceProfileEntry=_MwVirtualInterfaceProfileEntry_Object((1,3,6,1,4,1,15983,1,1,4,1,8,1))
mwVirtualInterfaceProfileEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:mwVirtualInterfaceProfileEntry.setStatus(_A)
_MwVirtualInterfaceProfileTableIndex_Type=Integer32
_MwVirtualInterfaceProfileTableIndex_Object=MibTableColumn
mwVirtualInterfaceProfileTableIndex=_MwVirtualInterfaceProfileTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,1,8,1,1),_MwVirtualInterfaceProfileTableIndex_Type())
mwVirtualInterfaceProfileTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwVirtualInterfaceProfileTableIndex.setStatus(_A)
class _MwVirtualInterfaceProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MwVirtualInterfaceProfileName_Type.__name__=_E
_MwVirtualInterfaceProfileName_Object=MibTableColumn
mwVirtualInterfaceProfileName=_MwVirtualInterfaceProfileName_Object((1,3,6,1,4,1,15983,1,1,4,1,8,1,2),_MwVirtualInterfaceProfileName_Type())
mwVirtualInterfaceProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVirtualInterfaceProfileName.setStatus(_A)
class _MwVirtualInterfaceProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_MwVirtualInterfaceProfileId_Type.__name__=_H
_MwVirtualInterfaceProfileId_Object=MibTableColumn
mwVirtualInterfaceProfileId=_MwVirtualInterfaceProfileId_Object((1,3,6,1,4,1,15983,1,1,4,1,8,1,3),_MwVirtualInterfaceProfileId_Type())
mwVirtualInterfaceProfileId.setMaxAccess(_D)
if mibBuilder.loadTexts:mwVirtualInterfaceProfileId.setStatus(_A)
_MwVirtualInterfaceProfileState_Type=MwlEnableDisableOption
_MwVirtualInterfaceProfileState_Object=MibTableColumn
mwVirtualInterfaceProfileState=_MwVirtualInterfaceProfileState_Object((1,3,6,1,4,1,15983,1,1,4,1,8,1,4),_MwVirtualInterfaceProfileState_Type())
mwVirtualInterfaceProfileState.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVirtualInterfaceProfileState.setStatus(_A)
_MwVirtualInterfaceProfileSubnetIp_Type=IpAddress
_MwVirtualInterfaceProfileSubnetIp_Object=MibTableColumn
mwVirtualInterfaceProfileSubnetIp=_MwVirtualInterfaceProfileSubnetIp_Object((1,3,6,1,4,1,15983,1,1,4,1,8,1,5),_MwVirtualInterfaceProfileSubnetIp_Type())
mwVirtualInterfaceProfileSubnetIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVirtualInterfaceProfileSubnetIp.setStatus(_A)
_MwVirtualInterfaceProfileSubnetMask_Type=IpAddress
_MwVirtualInterfaceProfileSubnetMask_Object=MibTableColumn
mwVirtualInterfaceProfileSubnetMask=_MwVirtualInterfaceProfileSubnetMask_Object((1,3,6,1,4,1,15983,1,1,4,1,8,1,6),_MwVirtualInterfaceProfileSubnetMask_Type())
mwVirtualInterfaceProfileSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVirtualInterfaceProfileSubnetMask.setStatus(_A)
_MwVirtualInterfaceProfileGatewayIp_Type=IpAddress
_MwVirtualInterfaceProfileGatewayIp_Object=MibTableColumn
mwVirtualInterfaceProfileGatewayIp=_MwVirtualInterfaceProfileGatewayIp_Object((1,3,6,1,4,1,15983,1,1,4,1,8,1,7),_MwVirtualInterfaceProfileGatewayIp_Type())
mwVirtualInterfaceProfileGatewayIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVirtualInterfaceProfileGatewayIp.setStatus(_A)
_MwVirtualInterfaceProfileRowStatus_Type=RowStatus
_MwVirtualInterfaceProfileRowStatus_Object=MibTableColumn
mwVirtualInterfaceProfileRowStatus=_MwVirtualInterfaceProfileRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,1,8,1,8),_MwVirtualInterfaceProfileRowStatus_Type())
mwVirtualInterfaceProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVirtualInterfaceProfileRowStatus.setStatus(_A)
_MwDhcpServerTable_Object=MibTable
mwDhcpServerTable=_MwDhcpServerTable_Object((1,3,6,1,4,1,15983,1,1,4,1,9))
if mibBuilder.loadTexts:mwDhcpServerTable.setStatus(_A)
_MwDhcpServerEntry_Object=MibTableRow
mwDhcpServerEntry=_MwDhcpServerEntry_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1))
mwDhcpServerEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:mwDhcpServerEntry.setStatus(_A)
_MwDhcpServerTableIndex_Type=Integer32
_MwDhcpServerTableIndex_Object=MibTableColumn
mwDhcpServerTableIndex=_MwDhcpServerTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1,1),_MwDhcpServerTableIndex_Type())
mwDhcpServerTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwDhcpServerTableIndex.setStatus(_A)
class _MwDhcpServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MwDhcpServerName_Type.__name__=_E
_MwDhcpServerName_Object=MibTableColumn
mwDhcpServerName=_MwDhcpServerName_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1,2),_MwDhcpServerName_Type())
mwDhcpServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDhcpServerName.setStatus(_A)
class _MwDhcpServerVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MwDhcpServerVlanName_Type.__name__=_E
_MwDhcpServerVlanName_Object=MibTableColumn
mwDhcpServerVlanName=_MwDhcpServerVlanName_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1,3),_MwDhcpServerVlanName_Type())
mwDhcpServerVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDhcpServerVlanName.setStatus(_A)
class _MwDhcpServerVirtualInterfaceProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MwDhcpServerVirtualInterfaceProfileName_Type.__name__=_E
_MwDhcpServerVirtualInterfaceProfileName_Object=MibTableColumn
mwDhcpServerVirtualInterfaceProfileName=_MwDhcpServerVirtualInterfaceProfileName_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1,4),_MwDhcpServerVirtualInterfaceProfileName_Type())
mwDhcpServerVirtualInterfaceProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDhcpServerVirtualInterfaceProfileName.setStatus(_A)
_MwDhcpServerState_Type=MwlEnableDisableOption
_MwDhcpServerState_Object=MibTableColumn
mwDhcpServerState=_MwDhcpServerState_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1,5),_MwDhcpServerState_Type())
mwDhcpServerState.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDhcpServerState.setStatus(_A)
class _MwDhcpServerLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,65535))
_MwDhcpServerLeaseTime_Type.__name__=_H
_MwDhcpServerLeaseTime_Object=MibTableColumn
mwDhcpServerLeaseTime=_MwDhcpServerLeaseTime_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1,6),_MwDhcpServerLeaseTime_Type())
mwDhcpServerLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDhcpServerLeaseTime.setStatus(_A)
_MwDhcpServerIpPoolStart_Type=IpAddress
_MwDhcpServerIpPoolStart_Object=MibTableColumn
mwDhcpServerIpPoolStart=_MwDhcpServerIpPoolStart_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1,7),_MwDhcpServerIpPoolStart_Type())
mwDhcpServerIpPoolStart.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDhcpServerIpPoolStart.setStatus(_A)
_MwDhcpServerIpPoolEnd_Type=IpAddress
_MwDhcpServerIpPoolEnd_Object=MibTableColumn
mwDhcpServerIpPoolEnd=_MwDhcpServerIpPoolEnd_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1,8),_MwDhcpServerIpPoolEnd_Type())
mwDhcpServerIpPoolEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDhcpServerIpPoolEnd.setStatus(_A)
_MwDhcpServerDomainName_Type=DisplayString
_MwDhcpServerDomainName_Object=MibTableColumn
mwDhcpServerDomainName=_MwDhcpServerDomainName_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1,9),_MwDhcpServerDomainName_Type())
mwDhcpServerDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDhcpServerDomainName.setStatus(_A)
_MwDhcpServerDnsServer1_Type=IpAddress
_MwDhcpServerDnsServer1_Object=MibTableColumn
mwDhcpServerDnsServer1=_MwDhcpServerDnsServer1_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1,10),_MwDhcpServerDnsServer1_Type())
mwDhcpServerDnsServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDhcpServerDnsServer1.setStatus(_A)
_MwDhcpServerDnsServer2_Type=IpAddress
_MwDhcpServerDnsServer2_Object=MibTableColumn
mwDhcpServerDnsServer2=_MwDhcpServerDnsServer2_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1,11),_MwDhcpServerDnsServer2_Type())
mwDhcpServerDnsServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDhcpServerDnsServer2.setStatus(_A)
_MwDhcpServerNetbiosServer1_Type=IpAddress
_MwDhcpServerNetbiosServer1_Object=MibTableColumn
mwDhcpServerNetbiosServer1=_MwDhcpServerNetbiosServer1_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1,12),_MwDhcpServerNetbiosServer1_Type())
mwDhcpServerNetbiosServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDhcpServerNetbiosServer1.setStatus(_A)
_MwDhcpServerNetbiosServer2_Type=IpAddress
_MwDhcpServerNetbiosServer2_Object=MibTableColumn
mwDhcpServerNetbiosServer2=_MwDhcpServerNetbiosServer2_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1,13),_MwDhcpServerNetbiosServer2_Type())
mwDhcpServerNetbiosServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDhcpServerNetbiosServer2.setStatus(_A)
class _MwDhcpServerOption43_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MwDhcpServerOption43_Type.__name__=_E
_MwDhcpServerOption43_Object=MibTableColumn
mwDhcpServerOption43=_MwDhcpServerOption43_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1,14),_MwDhcpServerOption43_Type())
mwDhcpServerOption43.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDhcpServerOption43.setStatus(_A)
_MwDhcpServerRowStatus_Type=RowStatus
_MwDhcpServerRowStatus_Object=MibTableColumn
mwDhcpServerRowStatus=_MwDhcpServerRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,1,9,1,16),_MwDhcpServerRowStatus_Type())
mwDhcpServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwDhcpServerRowStatus.setStatus(_A)
_MwVpnServer_ObjectIdentity=ObjectIdentity
mwVpnServer=_MwVpnServer_ObjectIdentity((1,3,6,1,4,1,15983,1,1,4,1,10))
_MwVpnServerState_Type=MwlEnableDisableOption
_MwVpnServerState_Object=MibScalar
mwVpnServerState=_MwVpnServerState_Object((1,3,6,1,4,1,15983,1,1,4,1,10,2),_MwVpnServerState_Type())
mwVpnServerState.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVpnServerState.setStatus(_A)
_MwVpnServerIp_Type=IpAddress
_MwVpnServerIp_Object=MibScalar
mwVpnServerIp=_MwVpnServerIp_Object((1,3,6,1,4,1,15983,1,1,4,1,10,3),_MwVpnServerIp_Type())
mwVpnServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVpnServerIp.setStatus(_A)
class _MwVpnServerHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_MwVpnServerHostName_Type.__name__=_E
_MwVpnServerHostName_Object=MibScalar
mwVpnServerHostName=_MwVpnServerHostName_Object((1,3,6,1,4,1,15983,1,1,4,1,10,4),_MwVpnServerHostName_Type())
mwVpnServerHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVpnServerHostName.setStatus(_A)
_MwVpnServerPort_Type=Unsigned32
_MwVpnServerPort_Object=MibScalar
mwVpnServerPort=_MwVpnServerPort_Object((1,3,6,1,4,1,15983,1,1,4,1,10,5),_MwVpnServerPort_Type())
mwVpnServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVpnServerPort.setStatus(_A)
_MwVpnServerIpPool_Type=IpAddress
_MwVpnServerIpPool_Object=MibScalar
mwVpnServerIpPool=_MwVpnServerIpPool_Object((1,3,6,1,4,1,15983,1,1,4,1,10,6),_MwVpnServerIpPool_Type())
mwVpnServerIpPool.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVpnServerIpPool.setStatus(_A)
_MwVpnServerSubnetMask_Type=IpAddress
_MwVpnServerSubnetMask_Object=MibScalar
mwVpnServerSubnetMask=_MwVpnServerSubnetMask_Object((1,3,6,1,4,1,15983,1,1,4,1,10,7),_MwVpnServerSubnetMask_Type())
mwVpnServerSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVpnServerSubnetMask.setStatus(_A)
_MwVpnClient_ObjectIdentity=ObjectIdentity
mwVpnClient=_MwVpnClient_ObjectIdentity((1,3,6,1,4,1,15983,1,1,4,1,11))
_MwVpnClientState_Type=MwlEnableDisableOption
_MwVpnClientState_Object=MibScalar
mwVpnClientState=_MwVpnClientState_Object((1,3,6,1,4,1,15983,1,1,4,1,11,2),_MwVpnClientState_Type())
mwVpnClientState.setMaxAccess(_C)
if mibBuilder.loadTexts:mwVpnClientState.setStatus(_A)
_MwVpnClientVpnServerIp_Type=IpAddress
_MwVpnClientVpnServerIp_Object=MibScalar
mwVpnClientVpnServerIp=_MwVpnClientVpnServerIp_Object((1,3,6,1,4,1,15983,1,1,4,1,11,3),_MwVpnClientVpnServerIp_Type())
mwVpnClientVpnServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:mwVpnClientVpnServerIp.setStatus(_A)
_MwVpnClientVpnServerPort_Type=Unsigned32
_MwVpnClientVpnServerPort_Object=MibScalar
mwVpnClientVpnServerPort=_MwVpnClientVpnServerPort_Object((1,3,6,1,4,1,15983,1,1,4,1,11,4),_MwVpnClientVpnServerPort_Type())
mwVpnClientVpnServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:mwVpnClientVpnServerPort.setStatus(_A)
_MwVpnClientStatus_Type=MwlVpnConnectivityStatus
_MwVpnClientStatus_Object=MibScalar
mwVpnClientStatus=_MwVpnClientStatus_Object((1,3,6,1,4,1,15983,1,1,4,1,11,5),_MwVpnClientStatus_Type())
mwVpnClientStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mwVpnClientStatus.setStatus(_A)
_MwVpnClientProtocol_Type=MwlVpnClientProtocol
_MwVpnClientProtocol_Object=MibScalar
mwVpnClientProtocol=_MwVpnClientProtocol_Object((1,3,6,1,4,1,15983,1,1,4,1,11,6),_MwVpnClientProtocol_Type())
mwVpnClientProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:mwVpnClientProtocol.setStatus(_A)
_MwUdpBcastUpstreamBridgedTable_Object=MibTable
mwUdpBcastUpstreamBridgedTable=_MwUdpBcastUpstreamBridgedTable_Object((1,3,6,1,4,1,15983,1,1,4,1,12))
if mibBuilder.loadTexts:mwUdpBcastUpstreamBridgedTable.setStatus(_A)
_MwUdpBcastUpstreamBridgedEntry_Object=MibTableRow
mwUdpBcastUpstreamBridgedEntry=_MwUdpBcastUpstreamBridgedEntry_Object((1,3,6,1,4,1,15983,1,1,4,1,12,1))
mwUdpBcastUpstreamBridgedEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:mwUdpBcastUpstreamBridgedEntry.setStatus(_A)
_MwUdpBcastUpstreamBridgedTableIndex_Type=Integer32
_MwUdpBcastUpstreamBridgedTableIndex_Object=MibTableColumn
mwUdpBcastUpstreamBridgedTableIndex=_MwUdpBcastUpstreamBridgedTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,1,12,1,1),_MwUdpBcastUpstreamBridgedTableIndex_Type())
mwUdpBcastUpstreamBridgedTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwUdpBcastUpstreamBridgedTableIndex.setStatus(_A)
_MwUdpBcastUpstreamBridgedPort_Type=Unsigned32
_MwUdpBcastUpstreamBridgedPort_Object=MibTableColumn
mwUdpBcastUpstreamBridgedPort=_MwUdpBcastUpstreamBridgedPort_Object((1,3,6,1,4,1,15983,1,1,4,1,12,1,2),_MwUdpBcastUpstreamBridgedPort_Type())
mwUdpBcastUpstreamBridgedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mwUdpBcastUpstreamBridgedPort.setStatus(_A)
_MwUdpBcastUpstreamBridgedRowStatus_Type=RowStatus
_MwUdpBcastUpstreamBridgedRowStatus_Object=MibTableColumn
mwUdpBcastUpstreamBridgedRowStatus=_MwUdpBcastUpstreamBridgedRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,1,12,1,3),_MwUdpBcastUpstreamBridgedRowStatus_Type())
mwUdpBcastUpstreamBridgedRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwUdpBcastUpstreamBridgedRowStatus.setStatus(_A)
_MwUdpBcastDownstreamBridgedTable_Object=MibTable
mwUdpBcastDownstreamBridgedTable=_MwUdpBcastDownstreamBridgedTable_Object((1,3,6,1,4,1,15983,1,1,4,1,13))
if mibBuilder.loadTexts:mwUdpBcastDownstreamBridgedTable.setStatus(_A)
_MwUdpBcastDownstreamBridgedEntry_Object=MibTableRow
mwUdpBcastDownstreamBridgedEntry=_MwUdpBcastDownstreamBridgedEntry_Object((1,3,6,1,4,1,15983,1,1,4,1,13,1))
mwUdpBcastDownstreamBridgedEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:mwUdpBcastDownstreamBridgedEntry.setStatus(_A)
_MwUdpBcastDownstreamBridgedTableIndex_Type=Integer32
_MwUdpBcastDownstreamBridgedTableIndex_Object=MibTableColumn
mwUdpBcastDownstreamBridgedTableIndex=_MwUdpBcastDownstreamBridgedTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,1,13,1,1),_MwUdpBcastDownstreamBridgedTableIndex_Type())
mwUdpBcastDownstreamBridgedTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwUdpBcastDownstreamBridgedTableIndex.setStatus(_A)
_MwUdpBcastDownstreamBridgedPort_Type=Unsigned32
_MwUdpBcastDownstreamBridgedPort_Object=MibTableColumn
mwUdpBcastDownstreamBridgedPort=_MwUdpBcastDownstreamBridgedPort_Object((1,3,6,1,4,1,15983,1,1,4,1,13,1,2),_MwUdpBcastDownstreamBridgedPort_Type())
mwUdpBcastDownstreamBridgedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mwUdpBcastDownstreamBridgedPort.setStatus(_A)
_MwUdpBcastDownstreamBridgedRowStatus_Type=RowStatus
_MwUdpBcastDownstreamBridgedRowStatus_Object=MibTableColumn
mwUdpBcastDownstreamBridgedRowStatus=_MwUdpBcastDownstreamBridgedRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,1,13,1,3),_MwUdpBcastDownstreamBridgedRowStatus_Type())
mwUdpBcastDownstreamBridgedRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwUdpBcastDownstreamBridgedRowStatus.setStatus(_A)
_MwWncMobilityVarsTable_Object=MibTable
mwWncMobilityVarsTable=_MwWncMobilityVarsTable_Object((1,3,6,1,4,1,15983,1,1,4,1,14))
if mibBuilder.loadTexts:mwWncMobilityVarsTable.setStatus(_A)
_MwWncMobilityVarsEntry_Object=MibTableRow
mwWncMobilityVarsEntry=_MwWncMobilityVarsEntry_Object((1,3,6,1,4,1,15983,1,1,4,1,14,1))
mwWncMobilityVarsEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:mwWncMobilityVarsEntry.setStatus(_A)
_MwWncMobilityVarsTableIndex_Type=Integer32
_MwWncMobilityVarsTableIndex_Object=MibTableColumn
mwWncMobilityVarsTableIndex=_MwWncMobilityVarsTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,1,14,1,1),_MwWncMobilityVarsTableIndex_Type())
mwWncMobilityVarsTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwWncMobilityVarsTableIndex.setStatus(_A)
_MwWncMobilityVarsTopoUpdate_Type=MwlOnOffSwitch
_MwWncMobilityVarsTopoUpdate_Object=MibTableColumn
mwWncMobilityVarsTopoUpdate=_MwWncMobilityVarsTopoUpdate_Object((1,3,6,1,4,1,15983,1,1,4,1,14,1,3),_MwWncMobilityVarsTopoUpdate_Type())
mwWncMobilityVarsTopoUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:mwWncMobilityVarsTopoUpdate.setStatus(_A)
_MwWncMobilityVarsAssocStationMaxIdlePeriod_Type=Unsigned32
_MwWncMobilityVarsAssocStationMaxIdlePeriod_Object=MibTableColumn
mwWncMobilityVarsAssocStationMaxIdlePeriod=_MwWncMobilityVarsAssocStationMaxIdlePeriod_Object((1,3,6,1,4,1,15983,1,1,4,1,14,1,4),_MwWncMobilityVarsAssocStationMaxIdlePeriod_Type())
mwWncMobilityVarsAssocStationMaxIdlePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:mwWncMobilityVarsAssocStationMaxIdlePeriod.setStatus(_A)
class _MwWncMobilityVarsAdequateRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-75,-25))
_MwWncMobilityVarsAdequateRssi_Type.__name__=_H
_MwWncMobilityVarsAdequateRssi_Object=MibTableColumn
mwWncMobilityVarsAdequateRssi=_MwWncMobilityVarsAdequateRssi_Object((1,3,6,1,4,1,15983,1,1,4,1,14,1,6),_MwWncMobilityVarsAdequateRssi_Type())
mwWncMobilityVarsAdequateRssi.setMaxAccess(_B)
if mibBuilder.loadTexts:mwWncMobilityVarsAdequateRssi.setStatus(_A)
_MwWncMobilityVarsRowStatus_Type=RowStatus
_MwWncMobilityVarsRowStatus_Object=MibTableColumn
mwWncMobilityVarsRowStatus=_MwWncMobilityVarsRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,1,14,1,7),_MwWncMobilityVarsRowStatus_Type())
mwWncMobilityVarsRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwWncMobilityVarsRowStatus.setStatus(_A)
_MwWncIpv6VarsTable_Object=MibTable
mwWncIpv6VarsTable=_MwWncIpv6VarsTable_Object((1,3,6,1,4,1,15983,1,1,4,1,15))
if mibBuilder.loadTexts:mwWncIpv6VarsTable.setStatus(_A)
_MwWncIpv6VarsEntry_Object=MibTableRow
mwWncIpv6VarsEntry=_MwWncIpv6VarsEntry_Object((1,3,6,1,4,1,15983,1,1,4,1,15,1))
mwWncIpv6VarsEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:mwWncIpv6VarsEntry.setStatus(_A)
_MwWncIpv6VarsTableIndex_Type=Integer32
_MwWncIpv6VarsTableIndex_Object=MibTableColumn
mwWncIpv6VarsTableIndex=_MwWncIpv6VarsTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,1,15,1,1),_MwWncIpv6VarsTableIndex_Type())
mwWncIpv6VarsTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwWncIpv6VarsTableIndex.setStatus(_A)
_MwWncIpv6VarsNeighborDiscOptimization_Type=MwlOnOffSwitch
_MwWncIpv6VarsNeighborDiscOptimization_Object=MibTableColumn
mwWncIpv6VarsNeighborDiscOptimization=_MwWncIpv6VarsNeighborDiscOptimization_Object((1,3,6,1,4,1,15983,1,1,4,1,15,1,2),_MwWncIpv6VarsNeighborDiscOptimization_Type())
mwWncIpv6VarsNeighborDiscOptimization.setMaxAccess(_C)
if mibBuilder.loadTexts:mwWncIpv6VarsNeighborDiscOptimization.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'mwConfigController':mwConfigController,'mwWncVars':mwWncVars,'mwWncVarsDescr':mwWncVarsDescr,'mwWncVarsLocation':mwWncVarsLocation,'mwWncVarsContact':mwWncVarsContact,'mwWncVarsAutoApUpgrade':mwWncVarsAutoApUpgrade,'mwWncVarsDhcpServer':mwWncVarsDhcpServer,'mwWncVarsStatPollingPeriod':mwWncVarsStatPollingPeriod,'mwWncVarsAuditPeriod':mwWncVarsAuditPeriod,'mwWncVarsApInitScript':mwWncVarsApInitScript,'mwWncVarsDhcpRelayPassThroughFlag':mwWncVarsDhcpRelayPassThroughFlag,'mwWncVarsManagementFromWirelessClients':mwWncVarsManagementFromWirelessClients,'mwWncVarsControllerIndex':mwWncVarsControllerIndex,'mwWncVarsFastPath':mwWncVarsFastPath,'mwWncVarsBonding':mwWncVarsBonding,'mwWncVarsNodeId':mwWncVarsNodeId,'mwWncVarsHostName':mwWncVarsHostName,'mwWncVarsUpTime':mwWncVarsUpTime,'mwWncVarsOperationalState':mwWncVarsOperationalState,'mwWncVarsAvailabilityStatus':mwWncVarsAvailabilityStatus,'mwWncVarsAlarmState':mwWncVarsAlarmState,'mwWncVarsVirtualIpAddress':mwWncVarsVirtualIpAddress,'mwWncVarsVirtualNetMask':mwWncVarsVirtualNetMask,'mwWncVarsDefaultGatewayAddr':mwWncVarsDefaultGatewayAddr,'mwWncVarsSoftwareVersion':mwWncVarsSoftwareVersion,'mwWncVarsSerialNumber':mwWncVarsSerialNumber,'mwWncVarsSystemId':mwWncVarsSystemId,'mwWncVarsHardwareType':mwWncVarsHardwareType,'mwWncVarsCountry':mwWncVarsCountry,'mwWncVarsManSerialNumber':mwWncVarsManSerialNumber,'mwWncVarsStationAgingOutPeriod':mwWncVarsStationAgingOutPeriod,'mwWncVarsRoamingDomainState':mwWncVarsRoamingDomainState,'mwWncVarsL3RoutingMode':mwWncVarsL3RoutingMode,'mwWncVarsRegion':mwWncVarsRegion,'mwWncVarsRoamingTimeOutPeriod':mwWncVarsRoamingTimeOutPeriod,'mwSystemFileVars':mwSystemFileVars,'mwSystemFileVarspHostName':mwSystemFileVarspHostName,'mwSystemFileVarspDnsDomainName':mwSystemFileVarspDnsDomainName,'mwUdpBcastUpstreamTable':mwUdpBcastUpstreamTable,'mwUdpBcastUpstreamEntry':mwUdpBcastUpstreamEntry,_I:mwUdpBcastUpstreamTableIndex,'mwUdpBcastUpstreamPort':mwUdpBcastUpstreamPort,'mwUdpBcastUpstreamRowStatus':mwUdpBcastUpstreamRowStatus,'mwUdpBcastDownstreamTable':mwUdpBcastDownstreamTable,'mwUdpBcastDownstreamEntry':mwUdpBcastDownstreamEntry,_J:mwUdpBcastDownstreamTableIndex,'mwUdpBcastDownstreamPort':mwUdpBcastDownstreamPort,'mwUdpBcastDownstreamRowStatus':mwUdpBcastDownstreamRowStatus,'mwDnsServerTable':mwDnsServerTable,'mwDnsServerEntry':mwDnsServerEntry,_K:mwDnsServerTableIndex,'mwDnsServer':mwDnsServer,'mwDnsServerRowStatus':mwDnsServerRowStatus,'mwWncNetworkConfigTable':mwWncNetworkConfigTable,'mwWncNetworkConfigEntry':mwWncNetworkConfigEntry,_L:mwWncNetworkConfigTableIndex,'mwWncNetworkConfigFastPath':mwWncNetworkConfigFastPath,'mwWncNetworkConfigBonding':mwWncNetworkConfigBonding,'mwWncNetworkConfigTenGigModule':mwWncNetworkConfigTenGigModule,'mwWncNetworkConfigRebridHandOffLogic':mwWncNetworkConfigRebridHandOffLogic,'mwWncNetworkConfigOneGigSFP':mwWncNetworkConfigOneGigSFP,'mwWncNetworkConfigRowStatus':mwWncNetworkConfigRowStatus,'mwVirtualInterfaceProfileTable':mwVirtualInterfaceProfileTable,'mwVirtualInterfaceProfileEntry':mwVirtualInterfaceProfileEntry,_M:mwVirtualInterfaceProfileTableIndex,'mwVirtualInterfaceProfileName':mwVirtualInterfaceProfileName,'mwVirtualInterfaceProfileId':mwVirtualInterfaceProfileId,'mwVirtualInterfaceProfileState':mwVirtualInterfaceProfileState,'mwVirtualInterfaceProfileSubnetIp':mwVirtualInterfaceProfileSubnetIp,'mwVirtualInterfaceProfileSubnetMask':mwVirtualInterfaceProfileSubnetMask,'mwVirtualInterfaceProfileGatewayIp':mwVirtualInterfaceProfileGatewayIp,'mwVirtualInterfaceProfileRowStatus':mwVirtualInterfaceProfileRowStatus,'mwDhcpServerTable':mwDhcpServerTable,'mwDhcpServerEntry':mwDhcpServerEntry,_N:mwDhcpServerTableIndex,'mwDhcpServerName':mwDhcpServerName,'mwDhcpServerVlanName':mwDhcpServerVlanName,'mwDhcpServerVirtualInterfaceProfileName':mwDhcpServerVirtualInterfaceProfileName,'mwDhcpServerState':mwDhcpServerState,'mwDhcpServerLeaseTime':mwDhcpServerLeaseTime,'mwDhcpServerIpPoolStart':mwDhcpServerIpPoolStart,'mwDhcpServerIpPoolEnd':mwDhcpServerIpPoolEnd,'mwDhcpServerDomainName':mwDhcpServerDomainName,'mwDhcpServerDnsServer1':mwDhcpServerDnsServer1,'mwDhcpServerDnsServer2':mwDhcpServerDnsServer2,'mwDhcpServerNetbiosServer1':mwDhcpServerNetbiosServer1,'mwDhcpServerNetbiosServer2':mwDhcpServerNetbiosServer2,'mwDhcpServerOption43':mwDhcpServerOption43,'mwDhcpServerRowStatus':mwDhcpServerRowStatus,'mwVpnServer':mwVpnServer,'mwVpnServerState':mwVpnServerState,'mwVpnServerIp':mwVpnServerIp,'mwVpnServerHostName':mwVpnServerHostName,'mwVpnServerPort':mwVpnServerPort,'mwVpnServerIpPool':mwVpnServerIpPool,'mwVpnServerSubnetMask':mwVpnServerSubnetMask,'mwVpnClient':mwVpnClient,'mwVpnClientState':mwVpnClientState,'mwVpnClientVpnServerIp':mwVpnClientVpnServerIp,'mwVpnClientVpnServerPort':mwVpnClientVpnServerPort,'mwVpnClientStatus':mwVpnClientStatus,'mwVpnClientProtocol':mwVpnClientProtocol,'mwUdpBcastUpstreamBridgedTable':mwUdpBcastUpstreamBridgedTable,'mwUdpBcastUpstreamBridgedEntry':mwUdpBcastUpstreamBridgedEntry,_O:mwUdpBcastUpstreamBridgedTableIndex,'mwUdpBcastUpstreamBridgedPort':mwUdpBcastUpstreamBridgedPort,'mwUdpBcastUpstreamBridgedRowStatus':mwUdpBcastUpstreamBridgedRowStatus,'mwUdpBcastDownstreamBridgedTable':mwUdpBcastDownstreamBridgedTable,'mwUdpBcastDownstreamBridgedEntry':mwUdpBcastDownstreamBridgedEntry,_P:mwUdpBcastDownstreamBridgedTableIndex,'mwUdpBcastDownstreamBridgedPort':mwUdpBcastDownstreamBridgedPort,'mwUdpBcastDownstreamBridgedRowStatus':mwUdpBcastDownstreamBridgedRowStatus,'mwWncMobilityVarsTable':mwWncMobilityVarsTable,'mwWncMobilityVarsEntry':mwWncMobilityVarsEntry,_Q:mwWncMobilityVarsTableIndex,'mwWncMobilityVarsTopoUpdate':mwWncMobilityVarsTopoUpdate,'mwWncMobilityVarsAssocStationMaxIdlePeriod':mwWncMobilityVarsAssocStationMaxIdlePeriod,'mwWncMobilityVarsAdequateRssi':mwWncMobilityVarsAdequateRssi,'mwWncMobilityVarsRowStatus':mwWncMobilityVarsRowStatus,'mwWncIpv6VarsTable':mwWncIpv6VarsTable,'mwWncIpv6VarsEntry':mwWncIpv6VarsEntry,_R:mwWncIpv6VarsTableIndex,'mwWncIpv6VarsNeighborDiscOptimization':mwWncIpv6VarsNeighborDiscOptimization})