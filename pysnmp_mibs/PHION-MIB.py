_AD='notificationGroup'
_AC='eventGroup'
_AB='trafficshapeGroup'
_AA='vpnusersGroup'
_A9='fwstatsGroup'
_A8='ospfGroup'
_A7='raidGroup'
_A6='hotfixGroup'
_A5='releaseGroup'
_A4='serverGroup'
_A3='eventTrap'
_A2='ripNeighborState'
_A1='ospfNeighborStatus'
_A0='ospfNeighborInterface'
_z='ospfNeighborAddress'
_y='bgpNeighborState'
_x='vpnState'
_w='noDelayDrop'
_v='noDelayPakets'
_u='noDelayTotal'
_t='class3Drop'
_s='class3Pakets'
_r='class3Total'
_q='class2Drop'
_p='class2Pakets'
_o='class2Total'
_n='class1Drop'
_m='class1Pakets'
_l='class1Total'
_k='sessions'
_j='dataThroughput'
_i='packetThroughput'
_h='raidEventText'
_g='raidEventTime'
_f='raidEventSev'
_e='hwSensorValue'
_d='hwSensorType'
_c='hotfixInstallTime'
_b='phionRelease'
_a='serverServiceState'
_Z='boxServiceState'
_Y='Integer32'
_X='eventSeverity'
_W='eventRepresentation'
_V='eventClassification'
_U='eventLayerDescription'
_T='eventAlarmTime'
_S='eventType'
_R='eventIDDescription'
_Q='eventID'
_P='connectorName'
_O='firewallSessions'
_N='ripNeighborAddress'
_M='ospfNeighborId'
_L='bgpNeighborAddress'
_K='vpnName'
_J='raidEventIndex'
_I='hwSensorName'
_H='hotfixName'
_G='serverServiceName'
_F='boxServiceName'
_E='unknown'
_D='DisplayString'
_C='read-only'
_B='PHION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_Y,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_D,'PhysAddress','TextualConvention')
phion=ModuleIdentity((1,3,6,1,4,1,10704))
if mibBuilder.loadTexts:phion.setRevisions(('2014-01-08 00:00','2014-01-07 00:00','2013-12-03 00:00'))
class ServiceState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,4)));namedValues=NamedValues(*((_E,-1),('stopped',0),('started',1),('blocked',2),('removed',4)))
class SensorType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3)));namedValues=NamedValues(*((_E,-1),('voltage',0),('fan',1),('temperature',2),('psu-status',3)))
class RaidEventSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_E,0),('error',1),('warning',2),('information',3),('debug',4)))
class VpnStates(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*(('down',-1),('down-disabled',0),('active',1)))
_Firewall_ObjectIdentity=ObjectIdentity
firewall=_Firewall_ObjectIdentity((1,3,6,1,4,1,10704,1))
_BoxServices_Object=MibTable
boxServices=_BoxServices_Object((1,3,6,1,4,1,10704,1,0))
if mibBuilder.loadTexts:boxServices.setStatus(_A)
_BoxServicesEntry_Object=MibTableRow
boxServicesEntry=_BoxServicesEntry_Object((1,3,6,1,4,1,10704,1,0,1))
boxServicesEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:boxServicesEntry.setStatus(_A)
class _BoxServiceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_BoxServiceName_Type.__name__=_D
_BoxServiceName_Object=MibTableColumn
boxServiceName=_BoxServiceName_Object((1,3,6,1,4,1,10704,1,0,1,1),_BoxServiceName_Type())
boxServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServiceName.setStatus(_A)
_BoxServiceState_Type=ServiceState
_BoxServiceState_Object=MibTableColumn
boxServiceState=_BoxServiceState_Object((1,3,6,1,4,1,10704,1,0,1,2),_BoxServiceState_Type())
boxServiceState.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServiceState.setStatus(_A)
_ServerServices_Object=MibTable
serverServices=_ServerServices_Object((1,3,6,1,4,1,10704,1,1))
if mibBuilder.loadTexts:serverServices.setStatus(_A)
_ServerServicesEntry_Object=MibTableRow
serverServicesEntry=_ServerServicesEntry_Object((1,3,6,1,4,1,10704,1,1,1))
serverServicesEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:serverServicesEntry.setStatus(_A)
class _ServerServiceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ServerServiceName_Type.__name__=_D
_ServerServiceName_Object=MibTableColumn
serverServiceName=_ServerServiceName_Object((1,3,6,1,4,1,10704,1,1,1,1),_ServerServiceName_Type())
serverServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:serverServiceName.setStatus(_A)
_ServerServiceState_Type=ServiceState
_ServerServiceState_Object=MibTableColumn
serverServiceState=_ServerServiceState_Object((1,3,6,1,4,1,10704,1,1,1,2),_ServerServiceState_Type())
serverServiceState.setMaxAccess(_C)
if mibBuilder.loadTexts:serverServiceState.setStatus(_A)
_PhionRelease_Type=DisplayString
_PhionRelease_Object=MibScalar
phionRelease=_PhionRelease_Object((1,3,6,1,4,1,10704,1,2),_PhionRelease_Type())
phionRelease.setMaxAccess(_C)
if mibBuilder.loadTexts:phionRelease.setStatus(_A)
_PhionHotfixes_Object=MibTable
phionHotfixes=_PhionHotfixes_Object((1,3,6,1,4,1,10704,1,3))
if mibBuilder.loadTexts:phionHotfixes.setStatus(_A)
_PhionHotfixesEntry_Object=MibTableRow
phionHotfixesEntry=_PhionHotfixesEntry_Object((1,3,6,1,4,1,10704,1,3,1))
phionHotfixesEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:phionHotfixesEntry.setStatus(_A)
class _HotfixName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HotfixName_Type.__name__=_D
_HotfixName_Object=MibTableColumn
hotfixName=_HotfixName_Object((1,3,6,1,4,1,10704,1,3,1,1),_HotfixName_Type())
hotfixName.setMaxAccess(_C)
if mibBuilder.loadTexts:hotfixName.setStatus(_A)
_HotfixInstallTime_Type=DateAndTime
_HotfixInstallTime_Object=MibTableColumn
hotfixInstallTime=_HotfixInstallTime_Object((1,3,6,1,4,1,10704,1,3,1,2),_HotfixInstallTime_Type())
hotfixInstallTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hotfixInstallTime.setStatus(_A)
_HwSensors_Object=MibTable
hwSensors=_HwSensors_Object((1,3,6,1,4,1,10704,1,4))
if mibBuilder.loadTexts:hwSensors.setStatus(_A)
_HwSensorsEntry_Object=MibTableRow
hwSensorsEntry=_HwSensorsEntry_Object((1,3,6,1,4,1,10704,1,4,1))
hwSensorsEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwSensorsEntry.setStatus(_A)
class _HwSensorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HwSensorName_Type.__name__=_D
_HwSensorName_Object=MibTableColumn
hwSensorName=_HwSensorName_Object((1,3,6,1,4,1,10704,1,4,1,1),_HwSensorName_Type())
hwSensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSensorName.setStatus(_A)
_HwSensorType_Type=SensorType
_HwSensorType_Object=MibTableColumn
hwSensorType=_HwSensorType_Object((1,3,6,1,4,1,10704,1,4,1,2),_HwSensorType_Type())
hwSensorType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSensorType.setStatus(_A)
_HwSensorValue_Type=Integer32
_HwSensorValue_Object=MibTableColumn
hwSensorValue=_HwSensorValue_Object((1,3,6,1,4,1,10704,1,4,1,3),_HwSensorValue_Type())
hwSensorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSensorValue.setStatus(_A)
_RaidEvents_Object=MibTable
raidEvents=_RaidEvents_Object((1,3,6,1,4,1,10704,1,5))
if mibBuilder.loadTexts:raidEvents.setStatus(_A)
_RaidEventsEntry_Object=MibTableRow
raidEventsEntry=_RaidEventsEntry_Object((1,3,6,1,4,1,10704,1,5,1))
raidEventsEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:raidEventsEntry.setStatus(_A)
class _RaidEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RaidEventIndex_Type.__name__=_Y
_RaidEventIndex_Object=MibTableColumn
raidEventIndex=_RaidEventIndex_Object((1,3,6,1,4,1,10704,1,5,1,1),_RaidEventIndex_Type())
raidEventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:raidEventIndex.setStatus(_A)
_RaidEventSev_Type=RaidEventSeverity
_RaidEventSev_Object=MibTableColumn
raidEventSev=_RaidEventSev_Object((1,3,6,1,4,1,10704,1,5,1,2),_RaidEventSev_Type())
raidEventSev.setMaxAccess(_C)
if mibBuilder.loadTexts:raidEventSev.setStatus(_A)
_RaidEventTime_Type=DateAndTime
_RaidEventTime_Object=MibTableColumn
raidEventTime=_RaidEventTime_Object((1,3,6,1,4,1,10704,1,5,1,3),_RaidEventTime_Type())
raidEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:raidEventTime.setStatus(_A)
_RaidEventText_Type=DisplayString
_RaidEventText_Object=MibTableColumn
raidEventText=_RaidEventText_Object((1,3,6,1,4,1,10704,1,5,1,4),_RaidEventText_Type())
raidEventText.setMaxAccess(_C)
if mibBuilder.loadTexts:raidEventText.setStatus(_A)
_VpnTunnels_Object=MibTable
vpnTunnels=_VpnTunnels_Object((1,3,6,1,4,1,10704,1,6))
if mibBuilder.loadTexts:vpnTunnels.setStatus(_A)
_VpnTunnelsEntry_Object=MibTableRow
vpnTunnelsEntry=_VpnTunnelsEntry_Object((1,3,6,1,4,1,10704,1,6,1))
vpnTunnelsEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:vpnTunnelsEntry.setStatus(_A)
class _VpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_VpnName_Type.__name__=_D
_VpnName_Object=MibTableColumn
vpnName=_VpnName_Object((1,3,6,1,4,1,10704,1,6,1,1),_VpnName_Type())
vpnName.setMaxAccess(_C)
if mibBuilder.loadTexts:vpnName.setStatus(_A)
_VpnState_Type=VpnStates
_VpnState_Object=MibTableColumn
vpnState=_VpnState_Object((1,3,6,1,4,1,10704,1,6,1,2),_VpnState_Type())
vpnState.setMaxAccess(_C)
if mibBuilder.loadTexts:vpnState.setStatus(_A)
_BgpNeighbors_Object=MibTable
bgpNeighbors=_BgpNeighbors_Object((1,3,6,1,4,1,10704,1,7))
if mibBuilder.loadTexts:bgpNeighbors.setStatus(_A)
_BgpNeighborsEntry_Object=MibTableRow
bgpNeighborsEntry=_BgpNeighborsEntry_Object((1,3,6,1,4,1,10704,1,7,1))
bgpNeighborsEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:bgpNeighborsEntry.setStatus(_A)
class _BgpNeighborAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_BgpNeighborAddress_Type.__name__=_D
_BgpNeighborAddress_Object=MibTableColumn
bgpNeighborAddress=_BgpNeighborAddress_Object((1,3,6,1,4,1,10704,1,7,1,1),_BgpNeighborAddress_Type())
bgpNeighborAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpNeighborAddress.setStatus(_A)
_BgpNeighborState_Type=Integer32
_BgpNeighborState_Object=MibTableColumn
bgpNeighborState=_BgpNeighborState_Object((1,3,6,1,4,1,10704,1,7,1,2),_BgpNeighborState_Type())
bgpNeighborState.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpNeighborState.setStatus(_A)
_OspfNeighbors_Object=MibTable
ospfNeighbors=_OspfNeighbors_Object((1,3,6,1,4,1,10704,1,8))
if mibBuilder.loadTexts:ospfNeighbors.setStatus(_A)
_OspfNeighborsEntry_Object=MibTableRow
ospfNeighborsEntry=_OspfNeighborsEntry_Object((1,3,6,1,4,1,10704,1,8,1))
ospfNeighborsEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:ospfNeighborsEntry.setStatus(_A)
class _OspfNeighborId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_OspfNeighborId_Type.__name__=_D
_OspfNeighborId_Object=MibTableColumn
ospfNeighborId=_OspfNeighborId_Object((1,3,6,1,4,1,10704,1,8,1,1),_OspfNeighborId_Type())
ospfNeighborId.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfNeighborId.setStatus(_A)
class _OspfNeighborAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_OspfNeighborAddress_Type.__name__=_D
_OspfNeighborAddress_Object=MibTableColumn
ospfNeighborAddress=_OspfNeighborAddress_Object((1,3,6,1,4,1,10704,1,8,1,2),_OspfNeighborAddress_Type())
ospfNeighborAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfNeighborAddress.setStatus(_A)
class _OspfNeighborInterface_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_OspfNeighborInterface_Type.__name__=_D
_OspfNeighborInterface_Object=MibTableColumn
ospfNeighborInterface=_OspfNeighborInterface_Object((1,3,6,1,4,1,10704,1,8,1,3),_OspfNeighborInterface_Type())
ospfNeighborInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfNeighborInterface.setStatus(_A)
class _OspfNeighborStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_OspfNeighborStatus_Type.__name__=_D
_OspfNeighborStatus_Object=MibTableColumn
ospfNeighborStatus=_OspfNeighborStatus_Object((1,3,6,1,4,1,10704,1,8,1,4),_OspfNeighborStatus_Type())
ospfNeighborStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfNeighborStatus.setStatus(_A)
_RipNeighbors_Object=MibTable
ripNeighbors=_RipNeighbors_Object((1,3,6,1,4,1,10704,1,9))
if mibBuilder.loadTexts:ripNeighbors.setStatus(_A)
_RipNeighborsEntry_Object=MibTableRow
ripNeighborsEntry=_RipNeighborsEntry_Object((1,3,6,1,4,1,10704,1,9,1))
ripNeighborsEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:ripNeighborsEntry.setStatus(_A)
class _RipNeighborAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_RipNeighborAddress_Type.__name__=_D
_RipNeighborAddress_Object=MibTableColumn
ripNeighborAddress=_RipNeighborAddress_Object((1,3,6,1,4,1,10704,1,9,1,1),_RipNeighborAddress_Type())
ripNeighborAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ripNeighborAddress.setStatus(_A)
class _RipNeighborState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_RipNeighborState_Type.__name__=_D
_RipNeighborState_Object=MibTableColumn
ripNeighborState=_RipNeighborState_Object((1,3,6,1,4,1,10704,1,9,1,2),_RipNeighborState_Type())
ripNeighborState.setMaxAccess(_C)
if mibBuilder.loadTexts:ripNeighborState.setStatus(_A)
_FwStats_Object=MibTable
fwStats=_FwStats_Object((1,3,6,1,4,1,10704,1,10))
if mibBuilder.loadTexts:fwStats.setStatus(_A)
_FwStatsEntry_Object=MibTableRow
fwStatsEntry=_FwStatsEntry_Object((1,3,6,1,4,1,10704,1,10,1))
fwStatsEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:fwStatsEntry.setStatus(_A)
_FirewallSessions_Type=Integer32
_FirewallSessions_Object=MibTableColumn
firewallSessions=_FirewallSessions_Object((1,3,6,1,4,1,10704,1,10,1,1),_FirewallSessions_Type())
firewallSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:firewallSessions.setStatus(_A)
_PacketThroughput_Type=Integer32
_PacketThroughput_Object=MibTableColumn
packetThroughput=_PacketThroughput_Object((1,3,6,1,4,1,10704,1,10,1,2),_PacketThroughput_Type())
packetThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:packetThroughput.setStatus(_A)
_DataThroughput_Type=Integer32
_DataThroughput_Object=MibTableColumn
dataThroughput=_DataThroughput_Object((1,3,6,1,4,1,10704,1,10,1,3),_DataThroughput_Type())
dataThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:dataThroughput.setStatus(_A)
_VpnUsers_Type=Integer32
_VpnUsers_Object=MibScalar
vpnUsers=_VpnUsers_Object((1,3,6,1,4,1,10704,1,11),_VpnUsers_Type())
vpnUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:vpnUsers.setStatus(_A)
_TrafficShape_Object=MibTable
trafficShape=_TrafficShape_Object((1,3,6,1,4,1,10704,1,12))
if mibBuilder.loadTexts:trafficShape.setStatus(_A)
_TrafficShapeEntry_Object=MibTableRow
trafficShapeEntry=_TrafficShapeEntry_Object((1,3,6,1,4,1,10704,1,12,1))
trafficShapeEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:trafficShapeEntry.setStatus(_A)
class _ConnectorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ConnectorName_Type.__name__=_D
_ConnectorName_Object=MibTableColumn
connectorName=_ConnectorName_Object((1,3,6,1,4,1,10704,1,12,1,1),_ConnectorName_Type())
connectorName.setMaxAccess(_C)
if mibBuilder.loadTexts:connectorName.setStatus(_A)
_Rate_Type=Counter64
_Rate_Object=MibTableColumn
rate=_Rate_Object((1,3,6,1,4,1,10704,1,12,1,2),_Rate_Type())
rate.setMaxAccess(_C)
if mibBuilder.loadTexts:rate.setStatus(_A)
_Sessions_Type=Counter64
_Sessions_Object=MibTableColumn
sessions=_Sessions_Object((1,3,6,1,4,1,10704,1,12,1,3),_Sessions_Type())
sessions.setMaxAccess(_C)
if mibBuilder.loadTexts:sessions.setStatus(_A)
_Class1Total_Type=Counter64
_Class1Total_Object=MibTableColumn
class1Total=_Class1Total_Object((1,3,6,1,4,1,10704,1,12,1,4),_Class1Total_Type())
class1Total.setMaxAccess(_C)
if mibBuilder.loadTexts:class1Total.setStatus(_A)
_Class1Pakets_Type=Counter64
_Class1Pakets_Object=MibTableColumn
class1Pakets=_Class1Pakets_Object((1,3,6,1,4,1,10704,1,12,1,5),_Class1Pakets_Type())
class1Pakets.setMaxAccess(_C)
if mibBuilder.loadTexts:class1Pakets.setStatus(_A)
_Class1Drop_Type=Counter64
_Class1Drop_Object=MibTableColumn
class1Drop=_Class1Drop_Object((1,3,6,1,4,1,10704,1,12,1,6),_Class1Drop_Type())
class1Drop.setMaxAccess(_C)
if mibBuilder.loadTexts:class1Drop.setStatus(_A)
_Class2Total_Type=Counter64
_Class2Total_Object=MibTableColumn
class2Total=_Class2Total_Object((1,3,6,1,4,1,10704,1,12,1,7),_Class2Total_Type())
class2Total.setMaxAccess(_C)
if mibBuilder.loadTexts:class2Total.setStatus(_A)
_Class2Pakets_Type=Counter64
_Class2Pakets_Object=MibTableColumn
class2Pakets=_Class2Pakets_Object((1,3,6,1,4,1,10704,1,12,1,8),_Class2Pakets_Type())
class2Pakets.setMaxAccess(_C)
if mibBuilder.loadTexts:class2Pakets.setStatus(_A)
_Class2Drop_Type=Counter64
_Class2Drop_Object=MibTableColumn
class2Drop=_Class2Drop_Object((1,3,6,1,4,1,10704,1,12,1,9),_Class2Drop_Type())
class2Drop.setMaxAccess(_C)
if mibBuilder.loadTexts:class2Drop.setStatus(_A)
_Class3Total_Type=Counter64
_Class3Total_Object=MibTableColumn
class3Total=_Class3Total_Object((1,3,6,1,4,1,10704,1,12,1,10),_Class3Total_Type())
class3Total.setMaxAccess(_C)
if mibBuilder.loadTexts:class3Total.setStatus(_A)
_Class3Pakets_Type=Counter64
_Class3Pakets_Object=MibTableColumn
class3Pakets=_Class3Pakets_Object((1,3,6,1,4,1,10704,1,12,1,11),_Class3Pakets_Type())
class3Pakets.setMaxAccess(_C)
if mibBuilder.loadTexts:class3Pakets.setStatus(_A)
_Class3Drop_Type=Counter64
_Class3Drop_Object=MibTableColumn
class3Drop=_Class3Drop_Object((1,3,6,1,4,1,10704,1,12,1,12),_Class3Drop_Type())
class3Drop.setMaxAccess(_C)
if mibBuilder.loadTexts:class3Drop.setStatus(_A)
_NoDelayTotal_Type=Counter64
_NoDelayTotal_Object=MibTableColumn
noDelayTotal=_NoDelayTotal_Object((1,3,6,1,4,1,10704,1,12,1,13),_NoDelayTotal_Type())
noDelayTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:noDelayTotal.setStatus(_A)
_NoDelayPakets_Type=Counter64
_NoDelayPakets_Object=MibTableColumn
noDelayPakets=_NoDelayPakets_Object((1,3,6,1,4,1,10704,1,12,1,14),_NoDelayPakets_Type())
noDelayPakets.setMaxAccess(_C)
if mibBuilder.loadTexts:noDelayPakets.setStatus(_A)
_NoDelayDrop_Type=Counter64
_NoDelayDrop_Object=MibTableColumn
noDelayDrop=_NoDelayDrop_Object((1,3,6,1,4,1,10704,1,12,1,15),_NoDelayDrop_Type())
noDelayDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:noDelayDrop.setStatus(_A)
_Event_ObjectIdentity=ObjectIdentity
event=_Event_ObjectIdentity((1,3,6,1,4,1,10704,10))
class _EventID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_EventID_Type.__name__=_D
_EventID_Object=MibScalar
eventID=_EventID_Object((1,3,6,1,4,1,10704,10,1),_EventID_Type())
eventID.setMaxAccess(_C)
if mibBuilder.loadTexts:eventID.setStatus(_A)
_EventIDDescription_Type=DisplayString
_EventIDDescription_Object=MibScalar
eventIDDescription=_EventIDDescription_Object((1,3,6,1,4,1,10704,10,2),_EventIDDescription_Type())
eventIDDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:eventIDDescription.setStatus(_A)
class _EventType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_EventType_Type.__name__=_D
_EventType_Object=MibScalar
eventType=_EventType_Object((1,3,6,1,4,1,10704,10,3),_EventType_Type())
eventType.setMaxAccess(_C)
if mibBuilder.loadTexts:eventType.setStatus(_A)
class _EventAlarmTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_EventAlarmTime_Type.__name__=_D
_EventAlarmTime_Object=MibScalar
eventAlarmTime=_EventAlarmTime_Object((1,3,6,1,4,1,10704,10,4),_EventAlarmTime_Type())
eventAlarmTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eventAlarmTime.setStatus(_A)
_EventLayerDescription_Type=DisplayString
_EventLayerDescription_Object=MibScalar
eventLayerDescription=_EventLayerDescription_Object((1,3,6,1,4,1,10704,10,5),_EventLayerDescription_Type())
eventLayerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:eventLayerDescription.setStatus(_A)
_EventClassification_Type=DisplayString
_EventClassification_Object=MibScalar
eventClassification=_EventClassification_Object((1,3,6,1,4,1,10704,10,6),_EventClassification_Type())
eventClassification.setMaxAccess(_C)
if mibBuilder.loadTexts:eventClassification.setStatus(_A)
_EventRepresentation_Type=DisplayString
_EventRepresentation_Object=MibScalar
eventRepresentation=_EventRepresentation_Object((1,3,6,1,4,1,10704,10,7),_EventRepresentation_Type())
eventRepresentation.setMaxAccess(_C)
if mibBuilder.loadTexts:eventRepresentation.setStatus(_A)
_EventSeverity_Type=DisplayString
_EventSeverity_Object=MibScalar
eventSeverity=_EventSeverity_Object((1,3,6,1,4,1,10704,10,8),_EventSeverity_Type())
eventSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:eventSeverity.setStatus(_A)
_FwCompliances_ObjectIdentity=ObjectIdentity
fwCompliances=_FwCompliances_ObjectIdentity((1,3,6,1,4,1,10704,20))
_FwGroups_ObjectIdentity=ObjectIdentity
fwGroups=_FwGroups_ObjectIdentity((1,3,6,1,4,1,10704,21))
_ServiceGroups_ObjectIdentity=ObjectIdentity
serviceGroups=_ServiceGroups_ObjectIdentity((1,3,6,1,4,1,10704,21,1))
_FirmwareGroups_ObjectIdentity=ObjectIdentity
firmwareGroups=_FirmwareGroups_ObjectIdentity((1,3,6,1,4,1,10704,21,2))
_HwGroups_ObjectIdentity=ObjectIdentity
hwGroups=_HwGroups_ObjectIdentity((1,3,6,1,4,1,10704,21,3))
_NetGroups_ObjectIdentity=ObjectIdentity
netGroups=_NetGroups_ObjectIdentity((1,3,6,1,4,1,10704,21,4))
_EventGroups_ObjectIdentity=ObjectIdentity
eventGroups=_EventGroups_ObjectIdentity((1,3,6,1,4,1,10704,21,5))
boxGroup=ObjectGroup((1,3,6,1,4,1,10704,21,1,1))
boxGroup.setObjects(*((_B,_F),(_B,_Z)))
if mibBuilder.loadTexts:boxGroup.setStatus(_A)
serverGroup=ObjectGroup((1,3,6,1,4,1,10704,21,1,2))
serverGroup.setObjects(*((_B,_G),(_B,_a)))
if mibBuilder.loadTexts:serverGroup.setStatus(_A)
releaseGroup=ObjectGroup((1,3,6,1,4,1,10704,21,2,1))
releaseGroup.setObjects((_B,_b))
if mibBuilder.loadTexts:releaseGroup.setStatus(_A)
hotfixGroup=ObjectGroup((1,3,6,1,4,1,10704,21,2,2))
hotfixGroup.setObjects(*((_B,_H),(_B,_c)))
if mibBuilder.loadTexts:hotfixGroup.setStatus(_A)
hwGroup=ObjectGroup((1,3,6,1,4,1,10704,21,3,1))
hwGroup.setObjects(*((_B,_I),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:hwGroup.setStatus(_A)
raidGroup=ObjectGroup((1,3,6,1,4,1,10704,21,3,2))
raidGroup.setObjects(*((_B,_J),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:raidGroup.setStatus(_A)
fwstatsGroup=ObjectGroup((1,3,6,1,4,1,10704,21,3,3))
fwstatsGroup.setObjects(*((_B,_O),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:fwstatsGroup.setStatus(_A)
trafficshapeGroup=ObjectGroup((1,3,6,1,4,1,10704,21,3,4))
trafficshapeGroup.setObjects(*((_B,_P),(_B,'rate'),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:trafficshapeGroup.setStatus(_A)
vpnGroup=ObjectGroup((1,3,6,1,4,1,10704,21,4,1))
vpnGroup.setObjects(*((_B,_K),(_B,_x)))
if mibBuilder.loadTexts:vpnGroup.setStatus(_A)
bgpGroup=ObjectGroup((1,3,6,1,4,1,10704,21,4,2))
bgpGroup.setObjects(*((_B,_L),(_B,_y)))
if mibBuilder.loadTexts:bgpGroup.setStatus(_A)
ospfGroup=ObjectGroup((1,3,6,1,4,1,10704,21,4,3))
ospfGroup.setObjects(*((_B,_M),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:ospfGroup.setStatus(_A)
ripGroup=ObjectGroup((1,3,6,1,4,1,10704,21,4,4))
ripGroup.setObjects(*((_B,_N),(_B,_A2)))
if mibBuilder.loadTexts:ripGroup.setStatus(_A)
vpnusersGroup=ObjectGroup((1,3,6,1,4,1,10704,21,4,5))
vpnusersGroup.setObjects((_B,'vpnUsers'))
if mibBuilder.loadTexts:vpnusersGroup.setStatus(_A)
eventGroup=ObjectGroup((1,3,6,1,4,1,10704,21,5,1))
eventGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:eventGroup.setStatus(_A)
eventTrap=NotificationType((1,3,6,1,4,1,10704,11))
eventTrap.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:eventTrap.setStatus(_A)
notificationGroup=NotificationGroup((1,3,6,1,4,1,10704,21,5,2))
notificationGroup.setObjects((_B,_A3))
if mibBuilder.loadTexts:notificationGroup.setStatus(_A)
fwCompliance=ModuleCompliance((1,3,6,1,4,1,10704,20,1))
fwCompliance.setObjects(*((_B,'boxGroup'),(_B,_A4),(_B,_A5),(_B,_A6),(_B,'hwGroup'),(_B,_A7),(_B,'vpnGroup'),(_B,'bgpGroup'),(_B,_A8),(_B,'ripGroup'),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:fwCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ServiceState':ServiceState,'SensorType':SensorType,'RaidEventSeverity':RaidEventSeverity,'VpnStates':VpnStates,'phion':phion,'firewall':firewall,'boxServices':boxServices,'boxServicesEntry':boxServicesEntry,_F:boxServiceName,_Z:boxServiceState,'serverServices':serverServices,'serverServicesEntry':serverServicesEntry,_G:serverServiceName,_a:serverServiceState,_b:phionRelease,'phionHotfixes':phionHotfixes,'phionHotfixesEntry':phionHotfixesEntry,_H:hotfixName,_c:hotfixInstallTime,'hwSensors':hwSensors,'hwSensorsEntry':hwSensorsEntry,_I:hwSensorName,_d:hwSensorType,_e:hwSensorValue,'raidEvents':raidEvents,'raidEventsEntry':raidEventsEntry,_J:raidEventIndex,_f:raidEventSev,_g:raidEventTime,_h:raidEventText,'vpnTunnels':vpnTunnels,'vpnTunnelsEntry':vpnTunnelsEntry,_K:vpnName,_x:vpnState,'bgpNeighbors':bgpNeighbors,'bgpNeighborsEntry':bgpNeighborsEntry,_L:bgpNeighborAddress,_y:bgpNeighborState,'ospfNeighbors':ospfNeighbors,'ospfNeighborsEntry':ospfNeighborsEntry,_M:ospfNeighborId,_z:ospfNeighborAddress,_A0:ospfNeighborInterface,_A1:ospfNeighborStatus,'ripNeighbors':ripNeighbors,'ripNeighborsEntry':ripNeighborsEntry,_N:ripNeighborAddress,_A2:ripNeighborState,'fwStats':fwStats,'fwStatsEntry':fwStatsEntry,_O:firewallSessions,_i:packetThroughput,_j:dataThroughput,'vpnUsers':vpnUsers,'trafficShape':trafficShape,'trafficShapeEntry':trafficShapeEntry,_P:connectorName,'rate':rate,_k:sessions,_l:class1Total,_m:class1Pakets,_n:class1Drop,_o:class2Total,_p:class2Pakets,_q:class2Drop,_r:class3Total,_s:class3Pakets,_t:class3Drop,_u:noDelayTotal,_v:noDelayPakets,_w:noDelayDrop,'event':event,_Q:eventID,_R:eventIDDescription,_S:eventType,_T:eventAlarmTime,_U:eventLayerDescription,_V:eventClassification,_W:eventRepresentation,_X:eventSeverity,_A3:eventTrap,'fwCompliances':fwCompliances,'fwCompliance':fwCompliance,'fwGroups':fwGroups,'serviceGroups':serviceGroups,'boxGroup':boxGroup,_A4:serverGroup,'firmwareGroups':firmwareGroups,_A5:releaseGroup,_A6:hotfixGroup,'hwGroups':hwGroups,'hwGroup':hwGroup,_A7:raidGroup,_A9:fwstatsGroup,_AB:trafficshapeGroup,'netGroups':netGroups,'vpnGroup':vpnGroup,'bgpGroup':bgpGroup,_A8:ospfGroup,'ripGroup':ripGroup,_AA:vpnusersGroup,'eventGroups':eventGroups,_AC:eventGroup,_AD:notificationGroup})