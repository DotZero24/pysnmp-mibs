_AC='swL2PortSecurityViolationMac'
_AB='swL2macNotifyInfo'
_AA='accessible-for-notify'
_A9='swL2DhcpLocalRelayVLANID'
_A8='swL2MulticastFilterVid'
_A7='swL2TrafficSegPort'
_A6='swL2IGMPAccessAuthPort'
_A5='swIGMPSnoopingGroupSourceAddr'
_A4='swIGMPSnoopingGroupGroupAddr'
_A3='swIGMPSnoopingGroupVid'
_A2='swL2IGMPRouterPortVlanid'
_A1='swL2IGMPInfoVid'
_A0='swL2TrunkVLANPort'
_z='swL2TrunkLACPPortIndex'
_y='swL2TrunkIndex'
_x='swL2DhcpRelayCtrlServer'
_w='swL2DhcpRelayCtrlInterfaceName'
_v='swL2QOS8021pDefaultPriorityIndex'
_u='swL2QOS8021pUserPriorityIndex'
_t='weightfair'
_s='roundrobin'
_r='strict'
_q='swL2QOSSchedulingClassIndex'
_p='swL2QOSBandwidthPortIndex'
_o='swL2MulticastFilterPortMaxGroupPortIndex'
_n='swL2LimitedMulticastFilterPortIndex'
_m='swL2MulticastFilterToIp'
_l='swL2MulticastFilterFromIp'
_k='swL2MulticastFilterProfileIdIndex'
_j='swL2MulticastFilterProfileIndex'
_i='swL2PortErrPortIndex'
_h='swL2PortCounterCtrlPortIndex'
_g='swL2PortCtrlMediumType'
_f='swL2PortCtrlPortIndex'
_e='power-saving'
_d='err-disabled'
_c='copper'
_b='swL2PortInfoMediumType'
_a='swL2PortInfoPortIndex'
_Z='swL2VlanPortInfoVid'
_Y='swL2VlanPortInfoPortIndex'
_X='swL2VlanIndex'
_W='not-accessible'
_V='swL2DevCtrlCFMPortIndex'
_U='active'
_T='normal'
_S='swL2VlanLoopDetectVID'
_R='swL2IGMPCtrlVid'
_Q='swL2PortSecurityPortIndex'
_P='start'
_O='OctetString'
_N='disable'
_M='enable'
_L='none'
_K='DisplayString'
_J='swL2LoopDetectPortIndex'
_I='read-create'
_H='enabled'
_G='disabled'
_F='other'
_E='DGS3200-L2MGMT-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AgentNotifyLevel,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','AgentNotifyLevel')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention','TruthValue')
dgs3200,=mibBuilder.importSymbols('SW3200PRIMGMT-MIB','dgs3200')
swL2MgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,11,101,1,2))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwL2DevMgmt_ObjectIdentity=ObjectIdentity
swL2DevMgmt=_SwL2DevMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,1))
_SwL2DevInfo_ObjectIdentity=ObjectIdentity
swL2DevInfo=_SwL2DevInfo_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,1,1))
class _SwDevInfoTotalNumOfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwDevInfoTotalNumOfPort_Type.__name__=_B
_SwDevInfoTotalNumOfPort_Object=MibScalar
swDevInfoTotalNumOfPort=_SwDevInfoTotalNumOfPort_Object((1,3,6,1,4,1,171,11,101,1,2,1,1,1),_SwDevInfoTotalNumOfPort_Type())
swDevInfoTotalNumOfPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swDevInfoTotalNumOfPort.setStatus(_A)
class _SwDevInfoNumOfPortInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwDevInfoNumOfPortInUse_Type.__name__=_B
_SwDevInfoNumOfPortInUse_Object=MibScalar
swDevInfoNumOfPortInUse=_SwDevInfoNumOfPortInUse_Object((1,3,6,1,4,1,171,11,101,1,2,1,1,2),_SwDevInfoNumOfPortInUse_Type())
swDevInfoNumOfPortInUse.setMaxAccess(_D)
if mibBuilder.loadTexts:swDevInfoNumOfPortInUse.setStatus(_A)
class _SwDevInfoFrontPanelLedStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwDevInfoFrontPanelLedStatus_Type.__name__=_O
_SwDevInfoFrontPanelLedStatus_Object=MibScalar
swDevInfoFrontPanelLedStatus=_SwDevInfoFrontPanelLedStatus_Object((1,3,6,1,4,1,171,11,101,1,2,1,1,4),_SwDevInfoFrontPanelLedStatus_Type())
swDevInfoFrontPanelLedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swDevInfoFrontPanelLedStatus.setStatus(_A)
_SwL2DevCtrl_ObjectIdentity=ObjectIdentity
swL2DevCtrl=_SwL2DevCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,1,2))
class _SwL2DevCtrlStpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlStpState_Type.__name__=_B
_SwL2DevCtrlStpState_Object=MibScalar
swL2DevCtrlStpState=_SwL2DevCtrlStpState_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,1),_SwL2DevCtrlStpState_Type())
swL2DevCtrlStpState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlStpState.setStatus(_A)
class _SwL2DevCtrlIGMPSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlIGMPSnooping_Type.__name__=_B
_SwL2DevCtrlIGMPSnooping_Object=MibScalar
swL2DevCtrlIGMPSnooping=_SwL2DevCtrlIGMPSnooping_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,2),_SwL2DevCtrlIGMPSnooping_Type())
swL2DevCtrlIGMPSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlIGMPSnooping.setStatus(_A)
class _SwL2DevCtrlRmonState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlRmonState_Type.__name__=_B
_SwL2DevCtrlRmonState_Object=MibScalar
swL2DevCtrlRmonState=_SwL2DevCtrlRmonState_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,4),_SwL2DevCtrlRmonState_Type())
swL2DevCtrlRmonState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlRmonState.setStatus(_A)
class _SwL2DevCtrlSnmpTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlSnmpTrapState_Type.__name__=_B
_SwL2DevCtrlSnmpTrapState_Object=MibScalar
swL2DevCtrlSnmpTrapState=_SwL2DevCtrlSnmpTrapState_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,5),_SwL2DevCtrlSnmpTrapState_Type())
swL2DevCtrlSnmpTrapState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlSnmpTrapState.setStatus(_A)
class _SwL2DevCtrlCleanAllStatisticCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_SwL2DevCtrlCleanAllStatisticCounter_Type.__name__=_B
_SwL2DevCtrlCleanAllStatisticCounter_Object=MibScalar
swL2DevCtrlCleanAllStatisticCounter=_SwL2DevCtrlCleanAllStatisticCounter_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,6),_SwL2DevCtrlCleanAllStatisticCounter_Type())
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlCleanAllStatisticCounter.setStatus(_A)
_SwL2DevCtrlVlanIdOfFDBTbl_Type=VlanId
_SwL2DevCtrlVlanIdOfFDBTbl_Object=MibScalar
swL2DevCtrlVlanIdOfFDBTbl=_SwL2DevCtrlVlanIdOfFDBTbl_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,7),_SwL2DevCtrlVlanIdOfFDBTbl_Type())
swL2DevCtrlVlanIdOfFDBTbl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlVlanIdOfFDBTbl.setStatus(_A)
class _SwL2MACNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2MACNotifyState_Type.__name__=_B
_SwL2MACNotifyState_Object=MibScalar
swL2MACNotifyState=_SwL2MACNotifyState_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,8),_SwL2MACNotifyState_Type())
swL2MACNotifyState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MACNotifyState.setStatus(_A)
class _SwL2MACNotifyHistorySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_SwL2MACNotifyHistorySize_Type.__name__=_B
_SwL2MACNotifyHistorySize_Object=MibScalar
swL2MACNotifyHistorySize=_SwL2MACNotifyHistorySize_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,9),_SwL2MACNotifyHistorySize_Type())
swL2MACNotifyHistorySize.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MACNotifyHistorySize.setStatus(_A)
class _SwL2MACNotifyInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SwL2MACNotifyInterval_Type.__name__=_B
_SwL2MACNotifyInterval_Object=MibScalar
swL2MACNotifyInterval=_SwL2MACNotifyInterval_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,10),_SwL2MACNotifyInterval_Type())
swL2MACNotifyInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MACNotifyInterval.setStatus(_A)
_SwL2DevCtrlTelnet_ObjectIdentity=ObjectIdentity
swL2DevCtrlTelnet=_SwL2DevCtrlTelnet_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,1,2,14))
class _SwL2DevCtrlTelnetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlTelnetState_Type.__name__=_B
_SwL2DevCtrlTelnetState_Object=MibScalar
swL2DevCtrlTelnetState=_SwL2DevCtrlTelnetState_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,14,1),_SwL2DevCtrlTelnetState_Type())
swL2DevCtrlTelnetState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlTelnetState.setStatus(_A)
class _SwL2DevCtrlTelnetTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2DevCtrlTelnetTcpPort_Type.__name__=_B
_SwL2DevCtrlTelnetTcpPort_Object=MibScalar
swL2DevCtrlTelnetTcpPort=_SwL2DevCtrlTelnetTcpPort_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,14,2),_SwL2DevCtrlTelnetTcpPort_Type())
swL2DevCtrlTelnetTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlTelnetTcpPort.setStatus(_A)
_SwL2DevCtrlManagementVlanId_Type=VlanId
_SwL2DevCtrlManagementVlanId_Object=MibScalar
swL2DevCtrlManagementVlanId=_SwL2DevCtrlManagementVlanId_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,16),_SwL2DevCtrlManagementVlanId_Type())
swL2DevCtrlManagementVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlManagementVlanId.setStatus(_A)
_SwL2DevCtrlWeb_ObjectIdentity=ObjectIdentity
swL2DevCtrlWeb=_SwL2DevCtrlWeb_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,1,2,17))
class _SwL2DevCtrlWebState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlWebState_Type.__name__=_B
_SwL2DevCtrlWebState_Object=MibScalar
swL2DevCtrlWebState=_SwL2DevCtrlWebState_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,17,1),_SwL2DevCtrlWebState_Type())
swL2DevCtrlWebState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlWebState.setStatus(_A)
class _SwL2DevCtrlWebTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2DevCtrlWebTcpPort_Type.__name__=_B
_SwL2DevCtrlWebTcpPort_Object=MibScalar
swL2DevCtrlWebTcpPort=_SwL2DevCtrlWebTcpPort_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,17,2),_SwL2DevCtrlWebTcpPort_Type())
swL2DevCtrlWebTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlWebTcpPort.setStatus(_A)
class _SwL2DevCtrlLLDPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlLLDPState_Type.__name__=_B
_SwL2DevCtrlLLDPState_Object=MibScalar
swL2DevCtrlLLDPState=_SwL2DevCtrlLLDPState_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,18),_SwL2DevCtrlLLDPState_Type())
swL2DevCtrlLLDPState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlLLDPState.setStatus(_A)
class _SwL2DevCtrlLLDPForwardMessageState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlLLDPForwardMessageState_Type.__name__=_B
_SwL2DevCtrlLLDPForwardMessageState_Object=MibScalar
swL2DevCtrlLLDPForwardMessageState=_SwL2DevCtrlLLDPForwardMessageState_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,19),_SwL2DevCtrlLLDPForwardMessageState_Type())
swL2DevCtrlLLDPForwardMessageState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlLLDPForwardMessageState.setStatus(_A)
class _SwL2DevCtrlIpAutoconfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlIpAutoconfig_Type.__name__=_B
_SwL2DevCtrlIpAutoconfig_Object=MibScalar
swL2DevCtrlIpAutoconfig=_SwL2DevCtrlIpAutoconfig_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,20),_SwL2DevCtrlIpAutoconfig_Type())
swL2DevCtrlIpAutoconfig.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlIpAutoconfig.setStatus(_A)
_SwL2DevCtrlCFM_ObjectIdentity=ObjectIdentity
swL2DevCtrlCFM=_SwL2DevCtrlCFM_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,1,2,21))
class _SwL2DevCtrlCFMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlCFMState_Type.__name__=_B
_SwL2DevCtrlCFMState_Object=MibScalar
swL2DevCtrlCFMState=_SwL2DevCtrlCFMState_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,21,1),_SwL2DevCtrlCFMState_Type())
swL2DevCtrlCFMState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlCFMState.setStatus(_A)
_SwL2DevCtrlCFMPortTable_Object=MibTable
swL2DevCtrlCFMPortTable=_SwL2DevCtrlCFMPortTable_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,21,2))
if mibBuilder.loadTexts:swL2DevCtrlCFMPortTable.setStatus(_A)
_SwL2DevCtrlCFMPortEntry_Object=MibTableRow
swL2DevCtrlCFMPortEntry=_SwL2DevCtrlCFMPortEntry_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,21,2,1))
swL2DevCtrlCFMPortEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:swL2DevCtrlCFMPortEntry.setStatus(_A)
_SwL2DevCtrlCFMPortIndex_Type=Integer32
_SwL2DevCtrlCFMPortIndex_Object=MibTableColumn
swL2DevCtrlCFMPortIndex=_SwL2DevCtrlCFMPortIndex_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,21,2,1,1),_SwL2DevCtrlCFMPortIndex_Type())
swL2DevCtrlCFMPortIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:swL2DevCtrlCFMPortIndex.setStatus(_A)
class _SwL2DevCtrlCFMPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlCFMPortState_Type.__name__=_B
_SwL2DevCtrlCFMPortState_Object=MibTableColumn
swL2DevCtrlCFMPortState=_SwL2DevCtrlCFMPortState_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,21,2,1,2),_SwL2DevCtrlCFMPortState_Type())
swL2DevCtrlCFMPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlCFMPortState.setStatus(_A)
class _SwL2DevCtrlVLANTrunkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlVLANTrunkState_Type.__name__=_B
_SwL2DevCtrlVLANTrunkState_Object=MibScalar
swL2DevCtrlVLANTrunkState=_SwL2DevCtrlVLANTrunkState_Object((1,3,6,1,4,1,171,11,101,1,2,1,2,22),_SwL2DevCtrlVLANTrunkState_Type())
swL2DevCtrlVLANTrunkState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlVLANTrunkState.setStatus(_A)
_SwL2DevAlarm_ObjectIdentity=ObjectIdentity
swL2DevAlarm=_SwL2DevAlarm_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,1,3))
class _SwL2DevAlarmNewRoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevAlarmNewRoot_Type.__name__=_B
_SwL2DevAlarmNewRoot_Object=MibScalar
swL2DevAlarmNewRoot=_SwL2DevAlarmNewRoot_Object((1,3,6,1,4,1,171,11,101,1,2,1,3,1),_SwL2DevAlarmNewRoot_Type())
swL2DevAlarmNewRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevAlarmNewRoot.setStatus(_A)
class _SwL2DevAlarmTopologyChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevAlarmTopologyChange_Type.__name__=_B
_SwL2DevAlarmTopologyChange_Object=MibScalar
swL2DevAlarmTopologyChange=_SwL2DevAlarmTopologyChange_Object((1,3,6,1,4,1,171,11,101,1,2,1,3,2),_SwL2DevAlarmTopologyChange_Type())
swL2DevAlarmTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevAlarmTopologyChange.setStatus(_A)
class _SwL2DevAlarmLinkChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevAlarmLinkChange_Type.__name__=_B
_SwL2DevAlarmLinkChange_Object=MibScalar
swL2DevAlarmLinkChange=_SwL2DevAlarmLinkChange_Object((1,3,6,1,4,1,171,11,101,1,2,1,3,3),_SwL2DevAlarmLinkChange_Type())
swL2DevAlarmLinkChange.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevAlarmLinkChange.setStatus(_A)
_SwL2VLANMgmt_ObjectIdentity=ObjectIdentity
swL2VLANMgmt=_SwL2VLANMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,2))
_SwL2VlanStaticTable_Object=MibTable
swL2VlanStaticTable=_SwL2VlanStaticTable_Object((1,3,6,1,4,1,171,11,101,1,2,2,1))
if mibBuilder.loadTexts:swL2VlanStaticTable.setStatus(_A)
_SwL2VlanStaticEntry_Object=MibTableRow
swL2VlanStaticEntry=_SwL2VlanStaticEntry_Object((1,3,6,1,4,1,171,11,101,1,2,2,1,1))
swL2VlanStaticEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:swL2VlanStaticEntry.setStatus(_A)
_SwL2VlanIndex_Type=VlanId
_SwL2VlanIndex_Object=MibTableColumn
swL2VlanIndex=_SwL2VlanIndex_Object((1,3,6,1,4,1,171,11,101,1,2,2,1,1,1),_SwL2VlanIndex_Type())
swL2VlanIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:swL2VlanIndex.setStatus(_A)
class _SwL2VLANAdvertisement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2VLANAdvertisement_Type.__name__=_B
_SwL2VLANAdvertisement_Object=MibTableColumn
swL2VLANAdvertisement=_SwL2VLANAdvertisement_Object((1,3,6,1,4,1,171,11,101,1,2,2,1,1,2),_SwL2VLANAdvertisement_Type())
swL2VLANAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VLANAdvertisement.setStatus(_A)
class _SwL2PVIDAutoAssignmentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2PVIDAutoAssignmentState_Type.__name__=_B
_SwL2PVIDAutoAssignmentState_Object=MibScalar
swL2PVIDAutoAssignmentState=_SwL2PVIDAutoAssignmentState_Object((1,3,6,1,4,1,171,11,101,1,2,2,2),_SwL2PVIDAutoAssignmentState_Type())
swL2PVIDAutoAssignmentState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PVIDAutoAssignmentState.setStatus(_A)
_SwL2VlanPortInfoTable_Object=MibTable
swL2VlanPortInfoTable=_SwL2VlanPortInfoTable_Object((1,3,6,1,4,1,171,11,101,1,2,2,3))
if mibBuilder.loadTexts:swL2VlanPortInfoTable.setStatus(_A)
_SwL2VlanPortInfoEntry_Object=MibTableRow
swL2VlanPortInfoEntry=_SwL2VlanPortInfoEntry_Object((1,3,6,1,4,1,171,11,101,1,2,2,3,1))
swL2VlanPortInfoEntry.setIndexNames((0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:swL2VlanPortInfoEntry.setStatus(_A)
class _SwL2VlanPortInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2VlanPortInfoPortIndex_Type.__name__=_B
_SwL2VlanPortInfoPortIndex_Object=MibTableColumn
swL2VlanPortInfoPortIndex=_SwL2VlanPortInfoPortIndex_Object((1,3,6,1,4,1,171,11,101,1,2,2,3,1,1),_SwL2VlanPortInfoPortIndex_Type())
swL2VlanPortInfoPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanPortInfoPortIndex.setStatus(_A)
class _SwL2VlanPortInfoVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2VlanPortInfoVid_Type.__name__=_B
_SwL2VlanPortInfoVid_Object=MibTableColumn
swL2VlanPortInfoVid=_SwL2VlanPortInfoVid_Object((1,3,6,1,4,1,171,11,101,1,2,2,3,1,2),_SwL2VlanPortInfoVid_Type())
swL2VlanPortInfoVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanPortInfoVid.setStatus(_A)
class _SwL2VlanPortInfoPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),('untagged',2),('tagged',3),('dynamic',4),('forbidden',5)))
_SwL2VlanPortInfoPortRole_Type.__name__=_B
_SwL2VlanPortInfoPortRole_Object=MibTableColumn
swL2VlanPortInfoPortRole=_SwL2VlanPortInfoPortRole_Object((1,3,6,1,4,1,171,11,101,1,2,2,3,1,3),_SwL2VlanPortInfoPortRole_Type())
swL2VlanPortInfoPortRole.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanPortInfoPortRole.setStatus(_A)
_SwL2PortMgmt_ObjectIdentity=ObjectIdentity
swL2PortMgmt=_SwL2PortMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,3))
_SwL2PortInfoTable_Object=MibTable
swL2PortInfoTable=_SwL2PortInfoTable_Object((1,3,6,1,4,1,171,11,101,1,2,3,1))
if mibBuilder.loadTexts:swL2PortInfoTable.setStatus(_A)
_SwL2PortInfoEntry_Object=MibTableRow
swL2PortInfoEntry=_SwL2PortInfoEntry_Object((1,3,6,1,4,1,171,11,101,1,2,3,1,1))
swL2PortInfoEntry.setIndexNames((0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:swL2PortInfoEntry.setStatus(_A)
class _SwL2PortInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortInfoPortIndex_Type.__name__=_B
_SwL2PortInfoPortIndex_Object=MibTableColumn
swL2PortInfoPortIndex=_SwL2PortInfoPortIndex_Object((1,3,6,1,4,1,171,11,101,1,2,3,1,1,1),_SwL2PortInfoPortIndex_Type())
swL2PortInfoPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoPortIndex.setStatus(_A)
class _SwL2PortInfoMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),('fiber',2)))
_SwL2PortInfoMediumType_Type.__name__=_B
_SwL2PortInfoMediumType_Object=MibTableColumn
swL2PortInfoMediumType=_SwL2PortInfoMediumType_Object((1,3,6,1,4,1,171,11,101,1,2,3,1,1,2),_SwL2PortInfoMediumType_Type())
swL2PortInfoMediumType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoMediumType.setStatus(_A)
class _SwL2PortInfoUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortInfoUnitID_Type.__name__=_B
_SwL2PortInfoUnitID_Object=MibTableColumn
swL2PortInfoUnitID=_SwL2PortInfoUnitID_Object((1,3,6,1,4,1,171,11,101,1,2,3,1,1,3),_SwL2PortInfoUnitID_Type())
swL2PortInfoUnitID.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoUnitID.setStatus(_A)
class _SwL2PortInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('portType-none',0),('portType-100Base-T',2),('portType-100Base-X',3),('portType-1000Base-T',4),('portType-1000Base-X',5),('portType-10GBase-R',6),('portType-10GBase-CX4',7),('portType-SIO',8),('portType-module-empty',9),('portType-user-last',10)))
_SwL2PortInfoType_Type.__name__=_B
_SwL2PortInfoType_Object=MibTableColumn
swL2PortInfoType=_SwL2PortInfoType_Object((1,3,6,1,4,1,171,11,101,1,2,3,1,1,4),_SwL2PortInfoType_Type())
swL2PortInfoType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoType.setStatus(_A)
class _SwL2PortInfoLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('link-pass',2),('link-fail',3)))
_SwL2PortInfoLinkStatus_Type.__name__=_B
_SwL2PortInfoLinkStatus_Object=MibTableColumn
swL2PortInfoLinkStatus=_SwL2PortInfoLinkStatus_Object((1,3,6,1,4,1,171,11,101,1,2,3,1,1,5),_SwL2PortInfoLinkStatus_Type())
swL2PortInfoLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoLinkStatus.setStatus(_A)
class _SwL2PortInfoNwayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('link-down',0),('full-10Mbps-8023x',1),('full-10Mbps-none',2),('half-10Mbps-backp',3),('half-10Mbps-none',4),('full-100Mbps-8023x',5),('full-100Mbps-none',6),('half-100Mbps-backp',7),('half-100Mbps-none',8),('full-1Gigabps-8023x',9),('full-1Gigabps-none',10),('half-1Gigabps-backp',11),('half-1Gigabps-none',12),('full-10Gigabps-8023x',13),('full-10Gigabps-none',14),('half-10Gigabps-8023x',15),('half-10Gigabps-none',16),('empty',17),(_d,18)))
_SwL2PortInfoNwayStatus_Type.__name__=_B
_SwL2PortInfoNwayStatus_Object=MibTableColumn
swL2PortInfoNwayStatus=_SwL2PortInfoNwayStatus_Object((1,3,6,1,4,1,171,11,101,1,2,3,1,1,6),_SwL2PortInfoNwayStatus_Type())
swL2PortInfoNwayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoNwayStatus.setStatus(_A)
class _SwL2PortInfoErrorDisabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,7)));namedValues=NamedValues(*((_L,0),('storm',1),('lbd',2),('unknow',3),(_e,7)))
_SwL2PortInfoErrorDisabled_Type.__name__=_B
_SwL2PortInfoErrorDisabled_Object=MibTableColumn
swL2PortInfoErrorDisabled=_SwL2PortInfoErrorDisabled_Object((1,3,6,1,4,1,171,11,101,1,2,3,1,1,8),_SwL2PortInfoErrorDisabled_Type())
swL2PortInfoErrorDisabled.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoErrorDisabled.setStatus(_A)
_SwL2PortCtrlTable_Object=MibTable
swL2PortCtrlTable=_SwL2PortCtrlTable_Object((1,3,6,1,4,1,171,11,101,1,2,3,2))
if mibBuilder.loadTexts:swL2PortCtrlTable.setStatus(_A)
_SwL2PortCtrlEntry_Object=MibTableRow
swL2PortCtrlEntry=_SwL2PortCtrlEntry_Object((1,3,6,1,4,1,171,11,101,1,2,3,2,1))
swL2PortCtrlEntry.setIndexNames((0,_E,_f),(0,_E,_g))
if mibBuilder.loadTexts:swL2PortCtrlEntry.setStatus(_A)
class _SwL2PortCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortCtrlPortIndex_Type.__name__=_B
_SwL2PortCtrlPortIndex_Object=MibTableColumn
swL2PortCtrlPortIndex=_SwL2PortCtrlPortIndex_Object((1,3,6,1,4,1,171,11,101,1,2,3,2,1,1),_SwL2PortCtrlPortIndex_Type())
swL2PortCtrlPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlPortIndex.setStatus(_A)
class _SwL2PortCtrlMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),('fiber',2)))
_SwL2PortCtrlMediumType_Type.__name__=_B
_SwL2PortCtrlMediumType_Object=MibTableColumn
swL2PortCtrlMediumType=_SwL2PortCtrlMediumType_Object((1,3,6,1,4,1,171,11,101,1,2,3,2,1,2),_SwL2PortCtrlMediumType_Type())
swL2PortCtrlMediumType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlMediumType.setStatus(_A)
class _SwL2PortCtrlUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortCtrlUnitIndex_Type.__name__=_B
_SwL2PortCtrlUnitIndex_Object=MibTableColumn
swL2PortCtrlUnitIndex=_SwL2PortCtrlUnitIndex_Object((1,3,6,1,4,1,171,11,101,1,2,3,2,1,3),_SwL2PortCtrlUnitIndex_Type())
swL2PortCtrlUnitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlUnitIndex.setStatus(_A)
class _SwL2PortCtrlAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortCtrlAdminState_Type.__name__=_B
_SwL2PortCtrlAdminState_Object=MibTableColumn
swL2PortCtrlAdminState=_SwL2PortCtrlAdminState_Object((1,3,6,1,4,1,171,11,101,1,2,3,2,1,4),_SwL2PortCtrlAdminState_Type())
swL2PortCtrlAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlAdminState.setStatus(_A)
class _SwL2PortCtrlNwayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,9,10)));namedValues=NamedValues(*((_F,1),('nway-enabled',2),('nway-disabled-10Mbps-Half',3),('nway-disabled-10Mbps-Full',4),('nway-disabled-100Mbps-Half',5),('nway-disabled-100Mbps-Full',6),('nway-disabled-1Gigabps-Full-master',9),('nway-disabled-1Gigabps-Full-slave',10)))
_SwL2PortCtrlNwayState_Type.__name__=_B
_SwL2PortCtrlNwayState_Object=MibTableColumn
swL2PortCtrlNwayState=_SwL2PortCtrlNwayState_Object((1,3,6,1,4,1,171,11,101,1,2,3,2,1,5),_SwL2PortCtrlNwayState_Type())
swL2PortCtrlNwayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlNwayState.setStatus(_A)
class _SwL2PortCtrlFlowCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortCtrlFlowCtrlState_Type.__name__=_B
_SwL2PortCtrlFlowCtrlState_Object=MibTableColumn
swL2PortCtrlFlowCtrlState=_SwL2PortCtrlFlowCtrlState_Object((1,3,6,1,4,1,171,11,101,1,2,3,2,1,6),_SwL2PortCtrlFlowCtrlState_Type())
swL2PortCtrlFlowCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlFlowCtrlState.setStatus(_A)
class _SwL2PortCtrlLearningState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortCtrlLearningState_Type.__name__=_B
_SwL2PortCtrlLearningState_Object=MibTableColumn
swL2PortCtrlLearningState=_SwL2PortCtrlLearningState_Object((1,3,6,1,4,1,171,11,101,1,2,3,2,1,7),_SwL2PortCtrlLearningState_Type())
swL2PortCtrlLearningState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlLearningState.setStatus(_A)
class _SwL2PortCtrlMACNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortCtrlMACNotifyState_Type.__name__=_B
_SwL2PortCtrlMACNotifyState_Object=MibTableColumn
swL2PortCtrlMACNotifyState=_SwL2PortCtrlMACNotifyState_Object((1,3,6,1,4,1,171,11,101,1,2,3,2,1,8),_SwL2PortCtrlMACNotifyState_Type())
swL2PortCtrlMACNotifyState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlMACNotifyState.setStatus(_A)
class _SwL2PortCtrlJumboFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortCtrlJumboFrame_Type.__name__=_B
_SwL2PortCtrlJumboFrame_Object=MibScalar
swL2PortCtrlJumboFrame=_SwL2PortCtrlJumboFrame_Object((1,3,6,1,4,1,171,11,101,1,2,3,3),_SwL2PortCtrlJumboFrame_Type())
swL2PortCtrlJumboFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlJumboFrame.setStatus(_A)
_SwL2PortCtrlJumboFrameMaxSize_Type=Integer32
_SwL2PortCtrlJumboFrameMaxSize_Object=MibScalar
swL2PortCtrlJumboFrameMaxSize=_SwL2PortCtrlJumboFrameMaxSize_Object((1,3,6,1,4,1,171,11,101,1,2,3,4),_SwL2PortCtrlJumboFrameMaxSize_Type())
swL2PortCtrlJumboFrameMaxSize.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlJumboFrameMaxSize.setStatus(_A)
_SwL2PortCounterCtrlTable_Object=MibTable
swL2PortCounterCtrlTable=_SwL2PortCounterCtrlTable_Object((1,3,6,1,4,1,171,11,101,1,2,3,6))
if mibBuilder.loadTexts:swL2PortCounterCtrlTable.setStatus(_A)
_SwL2PortCounterCtrlEntry_Object=MibTableRow
swL2PortCounterCtrlEntry=_SwL2PortCounterCtrlEntry_Object((1,3,6,1,4,1,171,11,101,1,2,3,6,1))
swL2PortCounterCtrlEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:swL2PortCounterCtrlEntry.setStatus(_A)
class _SwL2PortCounterCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortCounterCtrlPortIndex_Type.__name__=_B
_SwL2PortCounterCtrlPortIndex_Object=MibTableColumn
swL2PortCounterCtrlPortIndex=_SwL2PortCounterCtrlPortIndex_Object((1,3,6,1,4,1,171,11,101,1,2,3,6,1,1),_SwL2PortCounterCtrlPortIndex_Type())
swL2PortCounterCtrlPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCounterCtrlPortIndex.setStatus(_A)
class _SwL2PortCounterClearCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_P,2)))
_SwL2PortCounterClearCtrl_Type.__name__=_B
_SwL2PortCounterClearCtrl_Object=MibTableColumn
swL2PortCounterClearCtrl=_SwL2PortCounterClearCtrl_Object((1,3,6,1,4,1,171,11,101,1,2,3,6,1,2),_SwL2PortCounterClearCtrl_Type())
swL2PortCounterClearCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCounterClearCtrl.setStatus(_A)
_SwL2PortErrTable_Object=MibTable
swL2PortErrTable=_SwL2PortErrTable_Object((1,3,6,1,4,1,171,11,101,1,2,3,7))
if mibBuilder.loadTexts:swL2PortErrTable.setStatus(_A)
_SwL2PortErrEntry_Object=MibTableRow
swL2PortErrEntry=_SwL2PortErrEntry_Object((1,3,6,1,4,1,171,11,101,1,2,3,7,1))
swL2PortErrEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:swL2PortErrEntry.setStatus(_A)
class _SwL2PortErrPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortErrPortIndex_Type.__name__=_B
_SwL2PortErrPortIndex_Object=MibTableColumn
swL2PortErrPortIndex=_SwL2PortErrPortIndex_Object((1,3,6,1,4,1,171,11,101,1,2,3,7,1,1),_SwL2PortErrPortIndex_Type())
swL2PortErrPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortIndex.setStatus(_A)
class _SwL2PortErrPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2PortErrPortState_Type.__name__=_B
_SwL2PortErrPortState_Object=MibTableColumn
swL2PortErrPortState=_SwL2PortErrPortState_Object((1,3,6,1,4,1,171,11,101,1,2,3,7,1,2),_SwL2PortErrPortState_Type())
swL2PortErrPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortState.setStatus(_A)
class _SwL2PortErrPortConnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_d,2)))
_SwL2PortErrPortConnStatus_Type.__name__=_B
_SwL2PortErrPortConnStatus_Object=MibTableColumn
swL2PortErrPortConnStatus=_SwL2PortErrPortConnStatus_Object((1,3,6,1,4,1,171,11,101,1,2,3,7,1,3),_SwL2PortErrPortConnStatus_Type())
swL2PortErrPortConnStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortConnStatus.setStatus(_A)
class _SwL2PortErrPortReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,7)));namedValues=NamedValues(*(('stp-lbd',1),('storm-control',2),('ctp-lbd',3),(_e,7)))
_SwL2PortErrPortReason_Type.__name__=_B
_SwL2PortErrPortReason_Object=MibTableColumn
swL2PortErrPortReason=_SwL2PortErrPortReason_Object((1,3,6,1,4,1,171,11,101,1,2,3,7,1,4),_SwL2PortErrPortReason_Type())
swL2PortErrPortReason.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortReason.setStatus(_A)
_SwL2LimitedMulticastMgmt_ObjectIdentity=ObjectIdentity
swL2LimitedMulticastMgmt=_SwL2LimitedMulticastMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,5))
_SwL2MulticastFilterProfileTable_Object=MibTable
swL2MulticastFilterProfileTable=_SwL2MulticastFilterProfileTable_Object((1,3,6,1,4,1,171,11,101,1,2,5,1))
if mibBuilder.loadTexts:swL2MulticastFilterProfileTable.setStatus(_A)
_SwL2MulticastFilterProfileEntry_Object=MibTableRow
swL2MulticastFilterProfileEntry=_SwL2MulticastFilterProfileEntry_Object((1,3,6,1,4,1,171,11,101,1,2,5,1,1))
swL2MulticastFilterProfileEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:swL2MulticastFilterProfileEntry.setStatus(_A)
class _SwL2MulticastFilterProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_SwL2MulticastFilterProfileIndex_Type.__name__=_B
_SwL2MulticastFilterProfileIndex_Object=MibTableColumn
swL2MulticastFilterProfileIndex=_SwL2MulticastFilterProfileIndex_Object((1,3,6,1,4,1,171,11,101,1,2,5,1,1,1),_SwL2MulticastFilterProfileIndex_Type())
swL2MulticastFilterProfileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MulticastFilterProfileIndex.setStatus(_A)
class _SwL2MulticastFilterProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwL2MulticastFilterProfileName_Type.__name__=_K
_SwL2MulticastFilterProfileName_Object=MibTableColumn
swL2MulticastFilterProfileName=_SwL2MulticastFilterProfileName_Object((1,3,6,1,4,1,171,11,101,1,2,5,1,1,2),_SwL2MulticastFilterProfileName_Type())
swL2MulticastFilterProfileName.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2MulticastFilterProfileName.setStatus(_A)
_SwL2MulticastFilterStatus_Type=RowStatus
_SwL2MulticastFilterStatus_Object=MibTableColumn
swL2MulticastFilterStatus=_SwL2MulticastFilterStatus_Object((1,3,6,1,4,1,171,11,101,1,2,5,1,1,3),_SwL2MulticastFilterStatus_Type())
swL2MulticastFilterStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2MulticastFilterStatus.setStatus(_A)
_SwL2MulticastFilterProfileAddressTable_Object=MibTable
swL2MulticastFilterProfileAddressTable=_SwL2MulticastFilterProfileAddressTable_Object((1,3,6,1,4,1,171,11,101,1,2,5,2))
if mibBuilder.loadTexts:swL2MulticastFilterProfileAddressTable.setStatus(_A)
_SwL2MulticastFilterProfileAddressEntry_Object=MibTableRow
swL2MulticastFilterProfileAddressEntry=_SwL2MulticastFilterProfileAddressEntry_Object((1,3,6,1,4,1,171,11,101,1,2,5,2,1))
swL2MulticastFilterProfileAddressEntry.setIndexNames((0,_E,_k),(0,_E,_l),(0,_E,_m))
if mibBuilder.loadTexts:swL2MulticastFilterProfileAddressEntry.setStatus(_A)
class _SwL2MulticastFilterProfileIdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_SwL2MulticastFilterProfileIdIndex_Type.__name__=_B
_SwL2MulticastFilterProfileIdIndex_Object=MibTableColumn
swL2MulticastFilterProfileIdIndex=_SwL2MulticastFilterProfileIdIndex_Object((1,3,6,1,4,1,171,11,101,1,2,5,2,1,1),_SwL2MulticastFilterProfileIdIndex_Type())
swL2MulticastFilterProfileIdIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MulticastFilterProfileIdIndex.setStatus(_A)
_SwL2MulticastFilterFromIp_Type=IpAddress
_SwL2MulticastFilterFromIp_Object=MibTableColumn
swL2MulticastFilterFromIp=_SwL2MulticastFilterFromIp_Object((1,3,6,1,4,1,171,11,101,1,2,5,2,1,2),_SwL2MulticastFilterFromIp_Type())
swL2MulticastFilterFromIp.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MulticastFilterFromIp.setStatus(_A)
_SwL2MulticastFilterToIp_Type=IpAddress
_SwL2MulticastFilterToIp_Object=MibTableColumn
swL2MulticastFilterToIp=_SwL2MulticastFilterToIp_Object((1,3,6,1,4,1,171,11,101,1,2,5,2,1,3),_SwL2MulticastFilterToIp_Type())
swL2MulticastFilterToIp.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MulticastFilterToIp.setStatus(_A)
_SwL2MulticastFilterAddressState_Type=RowStatus
_SwL2MulticastFilterAddressState_Object=MibTableColumn
swL2MulticastFilterAddressState=_SwL2MulticastFilterAddressState_Object((1,3,6,1,4,1,171,11,101,1,2,5,2,1,4),_SwL2MulticastFilterAddressState_Type())
swL2MulticastFilterAddressState.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2MulticastFilterAddressState.setStatus(_A)
_SwL2LimitedMulticastFilterPortTable_Object=MibTable
swL2LimitedMulticastFilterPortTable=_SwL2LimitedMulticastFilterPortTable_Object((1,3,6,1,4,1,171,11,101,1,2,5,3))
if mibBuilder.loadTexts:swL2LimitedMulticastFilterPortTable.setStatus(_A)
_SwL2LimitedMulticastFilterPortEntry_Object=MibTableRow
swL2LimitedMulticastFilterPortEntry=_SwL2LimitedMulticastFilterPortEntry_Object((1,3,6,1,4,1,171,11,101,1,2,5,3,1))
swL2LimitedMulticastFilterPortEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:swL2LimitedMulticastFilterPortEntry.setStatus(_A)
_SwL2LimitedMulticastFilterPortIndex_Type=Integer32
_SwL2LimitedMulticastFilterPortIndex_Object=MibTableColumn
swL2LimitedMulticastFilterPortIndex=_SwL2LimitedMulticastFilterPortIndex_Object((1,3,6,1,4,1,171,11,101,1,2,5,3,1,1),_SwL2LimitedMulticastFilterPortIndex_Type())
swL2LimitedMulticastFilterPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LimitedMulticastFilterPortIndex.setStatus(_A)
class _SwL2LimitedMulticastFilterPortAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_SwL2LimitedMulticastFilterPortAccess_Type.__name__=_B
_SwL2LimitedMulticastFilterPortAccess_Object=MibTableColumn
swL2LimitedMulticastFilterPortAccess=_SwL2LimitedMulticastFilterPortAccess_Object((1,3,6,1,4,1,171,11,101,1,2,5,3,1,2),_SwL2LimitedMulticastFilterPortAccess_Type())
swL2LimitedMulticastFilterPortAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LimitedMulticastFilterPortAccess.setStatus(_A)
_SwL2LimitedMulticastFilterPortProfileID_Type=DisplayString
_SwL2LimitedMulticastFilterPortProfileID_Object=MibTableColumn
swL2LimitedMulticastFilterPortProfileID=_SwL2LimitedMulticastFilterPortProfileID_Object((1,3,6,1,4,1,171,11,101,1,2,5,3,1,3),_SwL2LimitedMulticastFilterPortProfileID_Type())
swL2LimitedMulticastFilterPortProfileID.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LimitedMulticastFilterPortProfileID.setStatus(_A)
class _SwL2LimitedMulticastFilterPortProfileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('add',2),('delete',3)))
_SwL2LimitedMulticastFilterPortProfileStatus_Type.__name__=_B
_SwL2LimitedMulticastFilterPortProfileStatus_Object=MibTableColumn
swL2LimitedMulticastFilterPortProfileStatus=_SwL2LimitedMulticastFilterPortProfileStatus_Object((1,3,6,1,4,1,171,11,101,1,2,5,3,1,4),_SwL2LimitedMulticastFilterPortProfileStatus_Type())
swL2LimitedMulticastFilterPortProfileStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2LimitedMulticastFilterPortProfileStatus.setStatus(_A)
_SwL2MulticastFilterPortMaxGroupTable_Object=MibTable
swL2MulticastFilterPortMaxGroupTable=_SwL2MulticastFilterPortMaxGroupTable_Object((1,3,6,1,4,1,171,11,101,1,2,5,4))
if mibBuilder.loadTexts:swL2MulticastFilterPortMaxGroupTable.setStatus(_A)
_SwL2MulticastFilterPortMaxGroupEntry_Object=MibTableRow
swL2MulticastFilterPortMaxGroupEntry=_SwL2MulticastFilterPortMaxGroupEntry_Object((1,3,6,1,4,1,171,11,101,1,2,5,4,1))
swL2MulticastFilterPortMaxGroupEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:swL2MulticastFilterPortMaxGroupEntry.setStatus(_A)
_SwL2MulticastFilterPortMaxGroupPortIndex_Type=Integer32
_SwL2MulticastFilterPortMaxGroupPortIndex_Object=MibTableColumn
swL2MulticastFilterPortMaxGroupPortIndex=_SwL2MulticastFilterPortMaxGroupPortIndex_Object((1,3,6,1,4,1,171,11,101,1,2,5,4,1,1),_SwL2MulticastFilterPortMaxGroupPortIndex_Type())
swL2MulticastFilterPortMaxGroupPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MulticastFilterPortMaxGroupPortIndex.setStatus(_A)
class _SwL2MulticastFilterPortMaxGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_SwL2MulticastFilterPortMaxGroup_Type.__name__=_B
_SwL2MulticastFilterPortMaxGroup_Object=MibTableColumn
swL2MulticastFilterPortMaxGroup=_SwL2MulticastFilterPortMaxGroup_Object((1,3,6,1,4,1,171,11,101,1,2,5,4,1,2),_SwL2MulticastFilterPortMaxGroup_Type())
swL2MulticastFilterPortMaxGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MulticastFilterPortMaxGroup.setStatus(_A)
_SwL2QOSMgmt_ObjectIdentity=ObjectIdentity
swL2QOSMgmt=_SwL2QOSMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,6))
_SwL2QOSBandwidthControlTable_Object=MibTable
swL2QOSBandwidthControlTable=_SwL2QOSBandwidthControlTable_Object((1,3,6,1,4,1,171,11,101,1,2,6,1))
if mibBuilder.loadTexts:swL2QOSBandwidthControlTable.setStatus(_A)
_SwL2QOSBandwidthControlEntry_Object=MibTableRow
swL2QOSBandwidthControlEntry=_SwL2QOSBandwidthControlEntry_Object((1,3,6,1,4,1,171,11,101,1,2,6,1,1))
swL2QOSBandwidthControlEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:swL2QOSBandwidthControlEntry.setStatus(_A)
class _SwL2QOSBandwidthPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,768))
_SwL2QOSBandwidthPortIndex_Type.__name__=_B
_SwL2QOSBandwidthPortIndex_Object=MibTableColumn
swL2QOSBandwidthPortIndex=_SwL2QOSBandwidthPortIndex_Object((1,3,6,1,4,1,171,11,101,1,2,6,1,1,1),_SwL2QOSBandwidthPortIndex_Type())
swL2QOSBandwidthPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthPortIndex.setStatus(_A)
class _SwL2QOSBandwidthRxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1024001))
_SwL2QOSBandwidthRxRate_Type.__name__=_B
_SwL2QOSBandwidthRxRate_Object=MibTableColumn
swL2QOSBandwidthRxRate=_SwL2QOSBandwidthRxRate_Object((1,3,6,1,4,1,171,11,101,1,2,6,1,1,2),_SwL2QOSBandwidthRxRate_Type())
swL2QOSBandwidthRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSBandwidthRxRate.setStatus(_A)
class _SwL2QOSBandwidthTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1024001))
_SwL2QOSBandwidthTxRate_Type.__name__=_B
_SwL2QOSBandwidthTxRate_Object=MibTableColumn
swL2QOSBandwidthTxRate=_SwL2QOSBandwidthTxRate_Object((1,3,6,1,4,1,171,11,101,1,2,6,1,1,3),_SwL2QOSBandwidthTxRate_Type())
swL2QOSBandwidthTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSBandwidthTxRate.setStatus(_A)
_SwL2QOSBandwidthRadiusRxRate_Type=Integer32
_SwL2QOSBandwidthRadiusRxRate_Object=MibTableColumn
swL2QOSBandwidthRadiusRxRate=_SwL2QOSBandwidthRadiusRxRate_Object((1,3,6,1,4,1,171,11,101,1,2,6,1,1,4),_SwL2QOSBandwidthRadiusRxRate_Type())
swL2QOSBandwidthRadiusRxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthRadiusRxRate.setStatus(_A)
_SwL2QOSBandwidthRadiusTxRate_Type=Integer32
_SwL2QOSBandwidthRadiusTxRate_Object=MibTableColumn
swL2QOSBandwidthRadiusTxRate=_SwL2QOSBandwidthRadiusTxRate_Object((1,3,6,1,4,1,171,11,101,1,2,6,1,1,5),_SwL2QOSBandwidthRadiusTxRate_Type())
swL2QOSBandwidthRadiusTxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthRadiusTxRate.setStatus(_A)
_SwL2QOSSchedulingTable_Object=MibTable
swL2QOSSchedulingTable=_SwL2QOSSchedulingTable_Object((1,3,6,1,4,1,171,11,101,1,2,6,2))
if mibBuilder.loadTexts:swL2QOSSchedulingTable.setStatus(_A)
_SwL2QOSSchedulingEntry_Object=MibTableRow
swL2QOSSchedulingEntry=_SwL2QOSSchedulingEntry_Object((1,3,6,1,4,1,171,11,101,1,2,6,2,1))
swL2QOSSchedulingEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:swL2QOSSchedulingEntry.setStatus(_A)
class _SwL2QOSSchedulingClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOSSchedulingClassIndex_Type.__name__=_B
_SwL2QOSSchedulingClassIndex_Object=MibTableColumn
swL2QOSSchedulingClassIndex=_SwL2QOSSchedulingClassIndex_Object((1,3,6,1,4,1,171,11,101,1,2,6,2,1,1),_SwL2QOSSchedulingClassIndex_Type())
swL2QOSSchedulingClassIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSSchedulingClassIndex.setStatus(_A)
class _SwL2QOSSchedulingMaxPkts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL2QOSSchedulingMaxPkts_Type.__name__=_B
_SwL2QOSSchedulingMaxPkts_Object=MibTableColumn
swL2QOSSchedulingMaxPkts=_SwL2QOSSchedulingMaxPkts_Object((1,3,6,1,4,1,171,11,101,1,2,6,2,1,2),_SwL2QOSSchedulingMaxPkts_Type())
swL2QOSSchedulingMaxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSSchedulingMaxPkts.setStatus(_A)
class _SwL2QOSSchedulingMechanism_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_r,1),(_s,2),(_t,3)))
_SwL2QOSSchedulingMechanism_Type.__name__=_B
_SwL2QOSSchedulingMechanism_Object=MibTableColumn
swL2QOSSchedulingMechanism=_SwL2QOSSchedulingMechanism_Object((1,3,6,1,4,1,171,11,101,1,2,6,2,1,3),_SwL2QOSSchedulingMechanism_Type())
swL2QOSSchedulingMechanism.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSSchedulingMechanism.setStatus(_A)
_SwL2QOS8021pUserPriorityTable_Object=MibTable
swL2QOS8021pUserPriorityTable=_SwL2QOS8021pUserPriorityTable_Object((1,3,6,1,4,1,171,11,101,1,2,6,3))
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityTable.setStatus(_A)
_SwL2QOS8021pUserPriorityEntry_Object=MibTableRow
swL2QOS8021pUserPriorityEntry=_SwL2QOS8021pUserPriorityEntry_Object((1,3,6,1,4,1,171,11,101,1,2,6,3,1))
swL2QOS8021pUserPriorityEntry.setIndexNames((0,_E,_u))
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityEntry.setStatus(_A)
class _SwL2QOS8021pUserPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOS8021pUserPriorityIndex_Type.__name__=_B
_SwL2QOS8021pUserPriorityIndex_Object=MibTableColumn
swL2QOS8021pUserPriorityIndex=_SwL2QOS8021pUserPriorityIndex_Object((1,3,6,1,4,1,171,11,101,1,2,6,3,1,1),_SwL2QOS8021pUserPriorityIndex_Type())
swL2QOS8021pUserPriorityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityIndex.setStatus(_A)
class _SwL2QOS8021pUserPriorityClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOS8021pUserPriorityClass_Type.__name__=_B
_SwL2QOS8021pUserPriorityClass_Object=MibTableColumn
swL2QOS8021pUserPriorityClass=_SwL2QOS8021pUserPriorityClass_Object((1,3,6,1,4,1,171,11,101,1,2,6,3,1,2),_SwL2QOS8021pUserPriorityClass_Type())
swL2QOS8021pUserPriorityClass.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityClass.setStatus(_A)
_SwL2QOS8021pDefaultPriorityTable_Object=MibTable
swL2QOS8021pDefaultPriorityTable=_SwL2QOS8021pDefaultPriorityTable_Object((1,3,6,1,4,1,171,11,101,1,2,6,4))
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityTable.setStatus(_A)
_SwL2QOS8021pDefaultPriorityEntry_Object=MibTableRow
swL2QOS8021pDefaultPriorityEntry=_SwL2QOS8021pDefaultPriorityEntry_Object((1,3,6,1,4,1,171,11,101,1,2,6,4,1))
swL2QOS8021pDefaultPriorityEntry.setIndexNames((0,_E,_v))
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityEntry.setStatus(_A)
class _SwL2QOS8021pDefaultPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,768))
_SwL2QOS8021pDefaultPriorityIndex_Type.__name__=_B
_SwL2QOS8021pDefaultPriorityIndex_Object=MibTableColumn
swL2QOS8021pDefaultPriorityIndex=_SwL2QOS8021pDefaultPriorityIndex_Object((1,3,6,1,4,1,171,11,101,1,2,6,4,1,1),_SwL2QOS8021pDefaultPriorityIndex_Type())
swL2QOS8021pDefaultPriorityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityIndex.setStatus(_A)
class _SwL2QOS8021pDefaultPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOS8021pDefaultPriority_Type.__name__=_B
_SwL2QOS8021pDefaultPriority_Object=MibTableColumn
swL2QOS8021pDefaultPriority=_SwL2QOS8021pDefaultPriority_Object((1,3,6,1,4,1,171,11,101,1,2,6,4,1,2),_SwL2QOS8021pDefaultPriority_Type())
swL2QOS8021pDefaultPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriority.setStatus(_A)
_SwL2QOS8021pRadiusPriority_Type=Integer32
_SwL2QOS8021pRadiusPriority_Object=MibTableColumn
swL2QOS8021pRadiusPriority=_SwL2QOS8021pRadiusPriority_Object((1,3,6,1,4,1,171,11,101,1,2,6,4,1,3),_SwL2QOS8021pRadiusPriority_Type())
swL2QOS8021pRadiusPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pRadiusPriority.setStatus(_A)
class _SwL2QOSSchedulingMechanismCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_r,1),(_s,2),(_t,3)))
_SwL2QOSSchedulingMechanismCtrl_Type.__name__=_B
_SwL2QOSSchedulingMechanismCtrl_Object=MibScalar
swL2QOSSchedulingMechanismCtrl=_SwL2QOSSchedulingMechanismCtrl_Object((1,3,6,1,4,1,171,11,101,1,2,6,5),_SwL2QOSSchedulingMechanismCtrl_Type())
swL2QOSSchedulingMechanismCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSSchedulingMechanismCtrl.setStatus(_A)
_SwL2PortSecurityMgmt_ObjectIdentity=ObjectIdentity
swL2PortSecurityMgmt=_SwL2PortSecurityMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,7))
_SwL2PortSecurityControlTable_Object=MibTable
swL2PortSecurityControlTable=_SwL2PortSecurityControlTable_Object((1,3,6,1,4,1,171,11,101,1,2,7,1))
if mibBuilder.loadTexts:swL2PortSecurityControlTable.setStatus(_A)
_SwL2PortSecurityControlEntry_Object=MibTableRow
swL2PortSecurityControlEntry=_SwL2PortSecurityControlEntry_Object((1,3,6,1,4,1,171,11,101,1,2,7,1,1))
swL2PortSecurityControlEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:swL2PortSecurityControlEntry.setStatus(_A)
class _SwL2PortSecurityPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,768))
_SwL2PortSecurityPortIndex_Type.__name__=_B
_SwL2PortSecurityPortIndex_Object=MibTableColumn
swL2PortSecurityPortIndex=_SwL2PortSecurityPortIndex_Object((1,3,6,1,4,1,171,11,101,1,2,7,1,1,1),_SwL2PortSecurityPortIndex_Type())
swL2PortSecurityPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityPortIndex.setStatus(_A)
class _SwL2PortSecurityMaxLernAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_SwL2PortSecurityMaxLernAddr_Type.__name__=_B
_SwL2PortSecurityMaxLernAddr_Object=MibTableColumn
swL2PortSecurityMaxLernAddr=_SwL2PortSecurityMaxLernAddr_Object((1,3,6,1,4,1,171,11,101,1,2,7,1,1,2),_SwL2PortSecurityMaxLernAddr_Type())
swL2PortSecurityMaxLernAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityMaxLernAddr.setStatus(_A)
class _SwL2PortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('permanent',2),('deleteOnTimeout',3),('deleteOnReset',4)))
_SwL2PortSecurityMode_Type.__name__=_B
_SwL2PortSecurityMode_Object=MibTableColumn
swL2PortSecurityMode=_SwL2PortSecurityMode_Object((1,3,6,1,4,1,171,11,101,1,2,7,1,1,3),_SwL2PortSecurityMode_Type())
swL2PortSecurityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityMode.setStatus(_A)
class _SwL2PortSecurityAdmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_M,2),(_N,3)))
_SwL2PortSecurityAdmState_Type.__name__=_B
_SwL2PortSecurityAdmState_Object=MibTableColumn
swL2PortSecurityAdmState=_SwL2PortSecurityAdmState_Object((1,3,6,1,4,1,171,11,101,1,2,7,1,1,4),_SwL2PortSecurityAdmState_Type())
swL2PortSecurityAdmState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityAdmState.setStatus(_A)
class _SwL2PortSecurityEntryClearCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_P,2)))
_SwL2PortSecurityEntryClearCtrl_Type.__name__=_B
_SwL2PortSecurityEntryClearCtrl_Object=MibTableColumn
swL2PortSecurityEntryClearCtrl=_SwL2PortSecurityEntryClearCtrl_Object((1,3,6,1,4,1,171,11,101,1,2,7,1,1,5),_SwL2PortSecurityEntryClearCtrl_Type())
swL2PortSecurityEntryClearCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityEntryClearCtrl.setStatus(_A)
_SwL2PortSecurityDelCtrl_ObjectIdentity=ObjectIdentity
swL2PortSecurityDelCtrl=_SwL2PortSecurityDelCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,7,2))
class _SwL2PortSecurityDelVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2PortSecurityDelVlanName_Type.__name__=_K
_SwL2PortSecurityDelVlanName_Object=MibScalar
swL2PortSecurityDelVlanName=_SwL2PortSecurityDelVlanName_Object((1,3,6,1,4,1,171,11,101,1,2,7,2,1),_SwL2PortSecurityDelVlanName_Type())
swL2PortSecurityDelVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityDelVlanName.setStatus(_A)
class _SwL2PortSecurityDelPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,768))
_SwL2PortSecurityDelPort_Type.__name__=_B
_SwL2PortSecurityDelPort_Object=MibScalar
swL2PortSecurityDelPort=_SwL2PortSecurityDelPort_Object((1,3,6,1,4,1,171,11,101,1,2,7,2,2),_SwL2PortSecurityDelPort_Type())
swL2PortSecurityDelPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityDelPort.setStatus(_A)
_SwL2PortSecurityDelMacAddress_Type=MacAddress
_SwL2PortSecurityDelMacAddress_Object=MibScalar
swL2PortSecurityDelMacAddress=_SwL2PortSecurityDelMacAddress_Object((1,3,6,1,4,1,171,11,101,1,2,7,2,3),_SwL2PortSecurityDelMacAddress_Type())
swL2PortSecurityDelMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityDelMacAddress.setStatus(_A)
class _SwL2PortSecurityDelActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_P,2)))
_SwL2PortSecurityDelActivity_Type.__name__=_B
_SwL2PortSecurityDelActivity_Object=MibScalar
swL2PortSecurityDelActivity=_SwL2PortSecurityDelActivity_Object((1,3,6,1,4,1,171,11,101,1,2,7,2,4),_SwL2PortSecurityDelActivity_Type())
swL2PortSecurityDelActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityDelActivity.setStatus(_A)
class _SwL2PortSecurityTrapLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_M,2),(_N,3)))
_SwL2PortSecurityTrapLogState_Type.__name__=_B
_SwL2PortSecurityTrapLogState_Object=MibScalar
swL2PortSecurityTrapLogState=_SwL2PortSecurityTrapLogState_Object((1,3,6,1,4,1,171,11,101,1,2,7,3),_SwL2PortSecurityTrapLogState_Type())
swL2PortSecurityTrapLogState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityTrapLogState.setStatus(_A)
_SwL2DhcpRelayMgmt_ObjectIdentity=ObjectIdentity
swL2DhcpRelayMgmt=_SwL2DhcpRelayMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,8))
class _SwL2DhcpRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DhcpRelayState_Type.__name__=_B
_SwL2DhcpRelayState_Object=MibScalar
swL2DhcpRelayState=_SwL2DhcpRelayState_Object((1,3,6,1,4,1,171,11,101,1,2,8,1),_SwL2DhcpRelayState_Type())
swL2DhcpRelayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayState.setStatus(_A)
class _SwL2DhcpRelayHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_SwL2DhcpRelayHopCount_Type.__name__=_B
_SwL2DhcpRelayHopCount_Object=MibScalar
swL2DhcpRelayHopCount=_SwL2DhcpRelayHopCount_Object((1,3,6,1,4,1,171,11,101,1,2,8,2),_SwL2DhcpRelayHopCount_Type())
swL2DhcpRelayHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayHopCount.setStatus(_A)
class _SwL2DhcpRelayTimeThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2DhcpRelayTimeThreshold_Type.__name__=_B
_SwL2DhcpRelayTimeThreshold_Object=MibScalar
swL2DhcpRelayTimeThreshold=_SwL2DhcpRelayTimeThreshold_Object((1,3,6,1,4,1,171,11,101,1,2,8,3),_SwL2DhcpRelayTimeThreshold_Type())
swL2DhcpRelayTimeThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayTimeThreshold.setStatus(_A)
class _SwL2DhcpRelayOption82State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DhcpRelayOption82State_Type.__name__=_B
_SwL2DhcpRelayOption82State_Object=MibScalar
swL2DhcpRelayOption82State=_SwL2DhcpRelayOption82State_Object((1,3,6,1,4,1,171,11,101,1,2,8,4),_SwL2DhcpRelayOption82State_Type())
swL2DhcpRelayOption82State.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayOption82State.setStatus(_A)
class _SwL2DhcpRelayOption82Check_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DhcpRelayOption82Check_Type.__name__=_B
_SwL2DhcpRelayOption82Check_Object=MibScalar
swL2DhcpRelayOption82Check=_SwL2DhcpRelayOption82Check_Object((1,3,6,1,4,1,171,11,101,1,2,8,5),_SwL2DhcpRelayOption82Check_Type())
swL2DhcpRelayOption82Check.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayOption82Check.setStatus(_A)
class _SwL2DhcpRelayOption82Policy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('replace',1),('drop',2),('keep',3)))
_SwL2DhcpRelayOption82Policy_Type.__name__=_B
_SwL2DhcpRelayOption82Policy_Object=MibScalar
swL2DhcpRelayOption82Policy=_SwL2DhcpRelayOption82Policy_Object((1,3,6,1,4,1,171,11,101,1,2,8,6),_SwL2DhcpRelayOption82Policy_Type())
swL2DhcpRelayOption82Policy.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayOption82Policy.setStatus(_A)
_SwL2DhcpRelayCtrlTable_Object=MibTable
swL2DhcpRelayCtrlTable=_SwL2DhcpRelayCtrlTable_Object((1,3,6,1,4,1,171,11,101,1,2,8,7))
if mibBuilder.loadTexts:swL2DhcpRelayCtrlTable.setStatus(_A)
_SwL2DhcpRelayCtrlEntry_Object=MibTableRow
swL2DhcpRelayCtrlEntry=_SwL2DhcpRelayCtrlEntry_Object((1,3,6,1,4,1,171,11,101,1,2,8,7,1))
swL2DhcpRelayCtrlEntry.setIndexNames((0,_E,_w),(0,_E,_x))
if mibBuilder.loadTexts:swL2DhcpRelayCtrlEntry.setStatus(_A)
class _SwL2DhcpRelayCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL2DhcpRelayCtrlInterfaceName_Type.__name__=_K
_SwL2DhcpRelayCtrlInterfaceName_Object=MibTableColumn
swL2DhcpRelayCtrlInterfaceName=_SwL2DhcpRelayCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,101,1,2,8,7,1,1),_SwL2DhcpRelayCtrlInterfaceName_Type())
swL2DhcpRelayCtrlInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpRelayCtrlInterfaceName.setStatus(_A)
_SwL2DhcpRelayCtrlServer_Type=IpAddress
_SwL2DhcpRelayCtrlServer_Object=MibTableColumn
swL2DhcpRelayCtrlServer=_SwL2DhcpRelayCtrlServer_Object((1,3,6,1,4,1,171,11,101,1,2,8,7,1,2),_SwL2DhcpRelayCtrlServer_Type())
swL2DhcpRelayCtrlServer.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpRelayCtrlServer.setStatus(_A)
class _SwL2DhcpRelayCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('invalid',2),('valid',3)))
_SwL2DhcpRelayCtrlState_Type.__name__=_B
_SwL2DhcpRelayCtrlState_Object=MibTableColumn
swL2DhcpRelayCtrlState=_SwL2DhcpRelayCtrlState_Object((1,3,6,1,4,1,171,11,101,1,2,8,7,1,3),_SwL2DhcpRelayCtrlState_Type())
swL2DhcpRelayCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayCtrlState.setStatus(_A)
_SwL2TrunkMgmt_ObjectIdentity=ObjectIdentity
swL2TrunkMgmt=_SwL2TrunkMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,9))
class _SwL2TrunkMaxSupportedEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_SwL2TrunkMaxSupportedEntries_Type.__name__=_B
_SwL2TrunkMaxSupportedEntries_Object=MibScalar
swL2TrunkMaxSupportedEntries=_SwL2TrunkMaxSupportedEntries_Object((1,3,6,1,4,1,171,11,101,1,2,9,1),_SwL2TrunkMaxSupportedEntries_Type())
swL2TrunkMaxSupportedEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkMaxSupportedEntries.setStatus(_A)
class _SwL2TrunkCurrentNumEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkCurrentNumEntries_Type.__name__=_B
_SwL2TrunkCurrentNumEntries_Object=MibScalar
swL2TrunkCurrentNumEntries=_SwL2TrunkCurrentNumEntries_Object((1,3,6,1,4,1,171,11,101,1,2,9,2),_SwL2TrunkCurrentNumEntries_Type())
swL2TrunkCurrentNumEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkCurrentNumEntries.setStatus(_A)
_SwL2TrunkCtrlTable_Object=MibTable
swL2TrunkCtrlTable=_SwL2TrunkCtrlTable_Object((1,3,6,1,4,1,171,11,101,1,2,9,3))
if mibBuilder.loadTexts:swL2TrunkCtrlTable.setStatus(_A)
_SwL2TrunkCtrlEntry_Object=MibTableRow
swL2TrunkCtrlEntry=_SwL2TrunkCtrlEntry_Object((1,3,6,1,4,1,171,11,101,1,2,9,3,1))
swL2TrunkCtrlEntry.setIndexNames((0,_E,_y))
if mibBuilder.loadTexts:swL2TrunkCtrlEntry.setStatus(_A)
class _SwL2TrunkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_SwL2TrunkIndex_Type.__name__=_B
_SwL2TrunkIndex_Object=MibTableColumn
swL2TrunkIndex=_SwL2TrunkIndex_Object((1,3,6,1,4,1,171,11,101,1,2,9,3,1,1),_SwL2TrunkIndex_Type())
swL2TrunkIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkIndex.setStatus(_A)
class _SwL2TrunkMasterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2TrunkMasterPort_Type.__name__=_B
_SwL2TrunkMasterPort_Object=MibTableColumn
swL2TrunkMasterPort=_SwL2TrunkMasterPort_Object((1,3,6,1,4,1,171,11,101,1,2,9,3,1,3),_SwL2TrunkMasterPort_Type())
swL2TrunkMasterPort.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2TrunkMasterPort.setStatus(_A)
_SwL2TrunkMember_Type=PortList
_SwL2TrunkMember_Object=MibTableColumn
swL2TrunkMember=_SwL2TrunkMember_Object((1,3,6,1,4,1,171,11,101,1,2,9,3,1,4),_SwL2TrunkMember_Type())
swL2TrunkMember.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2TrunkMember.setStatus(_A)
class _SwL2TrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('static',2),('lacp',3)))
_SwL2TrunkType_Type.__name__=_B
_SwL2TrunkType_Object=MibTableColumn
swL2TrunkType=_SwL2TrunkType_Object((1,3,6,1,4,1,171,11,101,1,2,9,3,1,6),_SwL2TrunkType_Type())
swL2TrunkType.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2TrunkType.setStatus(_A)
_SwL2TrunkState_Type=RowStatus
_SwL2TrunkState_Object=MibTableColumn
swL2TrunkState=_SwL2TrunkState_Object((1,3,6,1,4,1,171,11,101,1,2,9,3,1,7),_SwL2TrunkState_Type())
swL2TrunkState.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2TrunkState.setStatus(_A)
_SwL2TrunkActivePort_Type=PortList
_SwL2TrunkActivePort_Object=MibTableColumn
swL2TrunkActivePort=_SwL2TrunkActivePort_Object((1,3,6,1,4,1,171,11,101,1,2,9,3,1,8),_SwL2TrunkActivePort_Type())
swL2TrunkActivePort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkActivePort.setStatus(_A)
class _SwL2TrunkAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,7)));namedValues=NamedValues(*((_F,1),('mac-source-dest',4),('ip-source-dest',7)))
_SwL2TrunkAlgorithm_Type.__name__=_B
_SwL2TrunkAlgorithm_Object=MibScalar
swL2TrunkAlgorithm=_SwL2TrunkAlgorithm_Object((1,3,6,1,4,1,171,11,101,1,2,9,4),_SwL2TrunkAlgorithm_Type())
swL2TrunkAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkAlgorithm.setStatus(_A)
_SwL2TrunkLACPPortTable_Object=MibTable
swL2TrunkLACPPortTable=_SwL2TrunkLACPPortTable_Object((1,3,6,1,4,1,171,11,101,1,2,9,5))
if mibBuilder.loadTexts:swL2TrunkLACPPortTable.setStatus(_A)
_SwL2TrunkLACPPortEntry_Object=MibTableRow
swL2TrunkLACPPortEntry=_SwL2TrunkLACPPortEntry_Object((1,3,6,1,4,1,171,11,101,1,2,9,5,1))
swL2TrunkLACPPortEntry.setIndexNames((0,_E,_z))
if mibBuilder.loadTexts:swL2TrunkLACPPortEntry.setStatus(_A)
class _SwL2TrunkLACPPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkLACPPortIndex_Type.__name__=_B
_SwL2TrunkLACPPortIndex_Object=MibTableColumn
swL2TrunkLACPPortIndex=_SwL2TrunkLACPPortIndex_Object((1,3,6,1,4,1,171,11,101,1,2,9,5,1,1),_SwL2TrunkLACPPortIndex_Type())
swL2TrunkLACPPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkLACPPortIndex.setStatus(_A)
class _SwL2TrunkLACPPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),('passive',2)))
_SwL2TrunkLACPPortState_Type.__name__=_B
_SwL2TrunkLACPPortState_Object=MibTableColumn
swL2TrunkLACPPortState=_SwL2TrunkLACPPortState_Object((1,3,6,1,4,1,171,11,101,1,2,9,5,1,2),_SwL2TrunkLACPPortState_Type())
swL2TrunkLACPPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkLACPPortState.setStatus(_A)
_SwL2TrunkVLANTable_Object=MibTable
swL2TrunkVLANTable=_SwL2TrunkVLANTable_Object((1,3,6,1,4,1,171,11,101,1,2,9,6))
if mibBuilder.loadTexts:swL2TrunkVLANTable.setStatus(_A)
_SwL2TrunkVLANEntry_Object=MibTableRow
swL2TrunkVLANEntry=_SwL2TrunkVLANEntry_Object((1,3,6,1,4,1,171,11,101,1,2,9,6,1))
swL2TrunkVLANEntry.setIndexNames((0,_E,_A0))
if mibBuilder.loadTexts:swL2TrunkVLANEntry.setStatus(_A)
class _SwL2TrunkVLANPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkVLANPort_Type.__name__=_B
_SwL2TrunkVLANPort_Object=MibTableColumn
swL2TrunkVLANPort=_SwL2TrunkVLANPort_Object((1,3,6,1,4,1,171,11,101,1,2,9,6,1,1),_SwL2TrunkVLANPort_Type())
swL2TrunkVLANPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkVLANPort.setStatus(_A)
class _SwL2TrunkVLANState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2TrunkVLANState_Type.__name__=_B
_SwL2TrunkVLANState_Object=MibTableColumn
swL2TrunkVLANState=_SwL2TrunkVLANState_Object((1,3,6,1,4,1,171,11,101,1,2,9,6,1,2),_SwL2TrunkVLANState_Type())
swL2TrunkVLANState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkVLANState.setStatus(_A)
_SwL2MirrorMgmt_ObjectIdentity=ObjectIdentity
swL2MirrorMgmt=_SwL2MirrorMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,10))
class _SwL2MirrorLogicTargetPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2MirrorLogicTargetPort_Type.__name__=_B
_SwL2MirrorLogicTargetPort_Object=MibScalar
swL2MirrorLogicTargetPort=_SwL2MirrorLogicTargetPort_Object((1,3,6,1,4,1,171,11,101,1,2,10,1),_SwL2MirrorLogicTargetPort_Type())
swL2MirrorLogicTargetPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MirrorLogicTargetPort.setStatus(_A)
_SwL2MirrorPortSourceIngress_Type=PortList
_SwL2MirrorPortSourceIngress_Object=MibScalar
swL2MirrorPortSourceIngress=_SwL2MirrorPortSourceIngress_Object((1,3,6,1,4,1,171,11,101,1,2,10,2),_SwL2MirrorPortSourceIngress_Type())
swL2MirrorPortSourceIngress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MirrorPortSourceIngress.setStatus(_A)
_SwL2MirrorPortSourceEgress_Type=PortList
_SwL2MirrorPortSourceEgress_Object=MibScalar
swL2MirrorPortSourceEgress=_SwL2MirrorPortSourceEgress_Object((1,3,6,1,4,1,171,11,101,1,2,10,3),_SwL2MirrorPortSourceEgress_Type())
swL2MirrorPortSourceEgress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MirrorPortSourceEgress.setStatus(_A)
class _SwL2MirrorPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2MirrorPortState_Type.__name__=_B
_SwL2MirrorPortState_Object=MibScalar
swL2MirrorPortState=_SwL2MirrorPortState_Object((1,3,6,1,4,1,171,11,101,1,2,10,4),_SwL2MirrorPortState_Type())
swL2MirrorPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MirrorPortState.setStatus(_A)
_SwL2IGMPMgmt_ObjectIdentity=ObjectIdentity
swL2IGMPMgmt=_SwL2IGMPMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,11))
class _SwL2IGMPMaxSupportedVlans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPMaxSupportedVlans_Type.__name__=_B
_SwL2IGMPMaxSupportedVlans_Object=MibScalar
swL2IGMPMaxSupportedVlans=_SwL2IGMPMaxSupportedVlans_Object((1,3,6,1,4,1,171,11,101,1,2,11,1),_SwL2IGMPMaxSupportedVlans_Type())
swL2IGMPMaxSupportedVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMaxSupportedVlans.setStatus(_A)
class _SwL2IGMPMaxIpGroupNumPerVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPMaxIpGroupNumPerVlan_Type.__name__=_B
_SwL2IGMPMaxIpGroupNumPerVlan_Object=MibScalar
swL2IGMPMaxIpGroupNumPerVlan=_SwL2IGMPMaxIpGroupNumPerVlan_Object((1,3,6,1,4,1,171,11,101,1,2,11,2),_SwL2IGMPMaxIpGroupNumPerVlan_Type())
swL2IGMPMaxIpGroupNumPerVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMaxIpGroupNumPerVlan.setStatus(_A)
_SwL2IGMPCtrlTable_Object=MibTable
swL2IGMPCtrlTable=_SwL2IGMPCtrlTable_Object((1,3,6,1,4,1,171,11,101,1,2,11,3))
if mibBuilder.loadTexts:swL2IGMPCtrlTable.setStatus(_A)
_SwL2IGMPCtrlEntry_Object=MibTableRow
swL2IGMPCtrlEntry=_SwL2IGMPCtrlEntry_Object((1,3,6,1,4,1,171,11,101,1,2,11,3,1))
swL2IGMPCtrlEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:swL2IGMPCtrlEntry.setStatus(_A)
class _SwL2IGMPCtrlVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPCtrlVid_Type.__name__=_B
_SwL2IGMPCtrlVid_Object=MibTableColumn
swL2IGMPCtrlVid=_SwL2IGMPCtrlVid_Object((1,3,6,1,4,1,171,11,101,1,2,11,3,1,1),_SwL2IGMPCtrlVid_Type())
swL2IGMPCtrlVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPCtrlVid.setStatus(_A)
class _SwL2IGMPQueryInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2IGMPQueryInterval_Type.__name__=_B
_SwL2IGMPQueryInterval_Object=MibTableColumn
swL2IGMPQueryInterval=_SwL2IGMPQueryInterval_Object((1,3,6,1,4,1,171,11,101,1,2,11,3,1,2),_SwL2IGMPQueryInterval_Type())
swL2IGMPQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPQueryInterval.setStatus(_A)
class _SwL2IGMPMaxResponseTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_SwL2IGMPMaxResponseTime_Type.__name__=_B
_SwL2IGMPMaxResponseTime_Object=MibTableColumn
swL2IGMPMaxResponseTime=_SwL2IGMPMaxResponseTime_Object((1,3,6,1,4,1,171,11,101,1,2,11,3,1,3),_SwL2IGMPMaxResponseTime_Type())
swL2IGMPMaxResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMaxResponseTime.setStatus(_A)
class _SwL2IGMPRobustness_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2IGMPRobustness_Type.__name__=_B
_SwL2IGMPRobustness_Object=MibTableColumn
swL2IGMPRobustness=_SwL2IGMPRobustness_Object((1,3,6,1,4,1,171,11,101,1,2,11,3,1,4),_SwL2IGMPRobustness_Type())
swL2IGMPRobustness.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRobustness.setStatus(_A)
class _SwL2IGMPLastMemberQueryInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_SwL2IGMPLastMemberQueryInterval_Type.__name__=_B
_SwL2IGMPLastMemberQueryInterval_Object=MibTableColumn
swL2IGMPLastMemberQueryInterval=_SwL2IGMPLastMemberQueryInterval_Object((1,3,6,1,4,1,171,11,101,1,2,11,3,1,5),_SwL2IGMPLastMemberQueryInterval_Type())
swL2IGMPLastMemberQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPLastMemberQueryInterval.setStatus(_A)
class _SwL2IGMPHostTimeout_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPHostTimeout_Type.__name__=_B
_SwL2IGMPHostTimeout_Object=MibTableColumn
swL2IGMPHostTimeout=_SwL2IGMPHostTimeout_Object((1,3,6,1,4,1,171,11,101,1,2,11,3,1,6),_SwL2IGMPHostTimeout_Type())
swL2IGMPHostTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPHostTimeout.setStatus(_A)
class _SwL2IGMPRouteTimeout_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPRouteTimeout_Type.__name__=_B
_SwL2IGMPRouteTimeout_Object=MibTableColumn
swL2IGMPRouteTimeout=_SwL2IGMPRouteTimeout_Object((1,3,6,1,4,1,171,11,101,1,2,11,3,1,7),_SwL2IGMPRouteTimeout_Type())
swL2IGMPRouteTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouteTimeout.setStatus(_A)
class _SwL2IGMPLeaveTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPLeaveTimer_Type.__name__=_B
_SwL2IGMPLeaveTimer_Object=MibTableColumn
swL2IGMPLeaveTimer=_SwL2IGMPLeaveTimer_Object((1,3,6,1,4,1,171,11,101,1,2,11,3,1,8),_SwL2IGMPLeaveTimer_Type())
swL2IGMPLeaveTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPLeaveTimer.setStatus(_A)
class _SwL2IGMPQueryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2IGMPQueryState_Type.__name__=_B
_SwL2IGMPQueryState_Object=MibTableColumn
swL2IGMPQueryState=_SwL2IGMPQueryState_Object((1,3,6,1,4,1,171,11,101,1,2,11,3,1,9),_SwL2IGMPQueryState_Type())
swL2IGMPQueryState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPQueryState.setStatus(_A)
class _SwL2IGMPCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('querier',2),('non-querier',3)))
_SwL2IGMPCurrentState_Type.__name__=_B
_SwL2IGMPCurrentState_Object=MibTableColumn
swL2IGMPCurrentState=_SwL2IGMPCurrentState_Object((1,3,6,1,4,1,171,11,101,1,2,11,3,1,10),_SwL2IGMPCurrentState_Type())
swL2IGMPCurrentState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPCurrentState.setStatus(_A)
class _SwL2IGMPCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_M,3)))
_SwL2IGMPCtrlState_Type.__name__=_B
_SwL2IGMPCtrlState_Object=MibTableColumn
swL2IGMPCtrlState=_SwL2IGMPCtrlState_Object((1,3,6,1,4,1,171,11,101,1,2,11,3,1,11),_SwL2IGMPCtrlState_Type())
swL2IGMPCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPCtrlState.setStatus(_A)
class _SwL2IGMPFastLeaveState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_M,3)))
_SwL2IGMPFastLeaveState_Type.__name__=_B
_SwL2IGMPFastLeaveState_Object=MibTableColumn
swL2IGMPFastLeaveState=_SwL2IGMPFastLeaveState_Object((1,3,6,1,4,1,171,11,101,1,2,11,3,1,12),_SwL2IGMPFastLeaveState_Type())
swL2IGMPFastLeaveState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPFastLeaveState.setStatus(_A)
class _SwL2IGMPQueryVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_SwL2IGMPQueryVersion_Type.__name__=_B
_SwL2IGMPQueryVersion_Object=MibTableColumn
swL2IGMPQueryVersion=_SwL2IGMPQueryVersion_Object((1,3,6,1,4,1,171,11,101,1,2,11,3,1,13),_SwL2IGMPQueryVersion_Type())
swL2IGMPQueryVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPQueryVersion.setStatus(_A)
_SwL2IGMPQueryInfoTable_Object=MibTable
swL2IGMPQueryInfoTable=_SwL2IGMPQueryInfoTable_Object((1,3,6,1,4,1,171,11,101,1,2,11,4))
if mibBuilder.loadTexts:swL2IGMPQueryInfoTable.setStatus(_A)
_SwL2IGMPQueryInfoEntry_Object=MibTableRow
swL2IGMPQueryInfoEntry=_SwL2IGMPQueryInfoEntry_Object((1,3,6,1,4,1,171,11,101,1,2,11,4,1))
swL2IGMPQueryInfoEntry.setIndexNames((0,_E,_A1))
if mibBuilder.loadTexts:swL2IGMPQueryInfoEntry.setStatus(_A)
class _SwL2IGMPInfoVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoVid_Type.__name__=_B
_SwL2IGMPInfoVid_Object=MibTableColumn
swL2IGMPInfoVid=_SwL2IGMPInfoVid_Object((1,3,6,1,4,1,171,11,101,1,2,11,4,1,1),_SwL2IGMPInfoVid_Type())
swL2IGMPInfoVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPInfoVid.setStatus(_A)
class _SwL2IGMPInfoQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoQueryCount_Type.__name__=_B
_SwL2IGMPInfoQueryCount_Object=MibTableColumn
swL2IGMPInfoQueryCount=_SwL2IGMPInfoQueryCount_Object((1,3,6,1,4,1,171,11,101,1,2,11,4,1,2),_SwL2IGMPInfoQueryCount_Type())
swL2IGMPInfoQueryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPInfoQueryCount.setStatus(_A)
class _SwL2IGMPInfoTxQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoTxQueryCount_Type.__name__=_B
_SwL2IGMPInfoTxQueryCount_Object=MibTableColumn
swL2IGMPInfoTxQueryCount=_SwL2IGMPInfoTxQueryCount_Object((1,3,6,1,4,1,171,11,101,1,2,11,4,1,3),_SwL2IGMPInfoTxQueryCount_Type())
swL2IGMPInfoTxQueryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPInfoTxQueryCount.setStatus(_A)
_SwL2IGMPRouterPortTable_Object=MibTable
swL2IGMPRouterPortTable=_SwL2IGMPRouterPortTable_Object((1,3,6,1,4,1,171,11,101,1,2,11,6))
if mibBuilder.loadTexts:swL2IGMPRouterPortTable.setStatus(_A)
_SwL2IGMPRouterPortEntry_Object=MibTableRow
swL2IGMPRouterPortEntry=_SwL2IGMPRouterPortEntry_Object((1,3,6,1,4,1,171,11,101,1,2,11,6,1))
swL2IGMPRouterPortEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:swL2IGMPRouterPortEntry.setStatus(_A)
class _SwL2IGMPRouterPortVlanid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2IGMPRouterPortVlanid_Type.__name__=_B
_SwL2IGMPRouterPortVlanid_Object=MibTableColumn
swL2IGMPRouterPortVlanid=_SwL2IGMPRouterPortVlanid_Object((1,3,6,1,4,1,171,11,101,1,2,11,6,1,1),_SwL2IGMPRouterPortVlanid_Type())
swL2IGMPRouterPortVlanid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterPortVlanid.setStatus(_A)
class _SwL2IGMPRouterPortVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2IGMPRouterPortVlanName_Type.__name__=_K
_SwL2IGMPRouterPortVlanName_Object=MibTableColumn
swL2IGMPRouterPortVlanName=_SwL2IGMPRouterPortVlanName_Object((1,3,6,1,4,1,171,11,101,1,2,11,6,1,2),_SwL2IGMPRouterPortVlanName_Type())
swL2IGMPRouterPortVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterPortVlanName.setStatus(_A)
_SwL2IGMPRouterPortStaticPortList_Type=PortList
_SwL2IGMPRouterPortStaticPortList_Object=MibTableColumn
swL2IGMPRouterPortStaticPortList=_SwL2IGMPRouterPortStaticPortList_Object((1,3,6,1,4,1,171,11,101,1,2,11,6,1,3),_SwL2IGMPRouterPortStaticPortList_Type())
swL2IGMPRouterPortStaticPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouterPortStaticPortList.setStatus(_A)
_SwL2IGMPRouterPortDynamicPortList_Type=PortList
_SwL2IGMPRouterPortDynamicPortList_Object=MibTableColumn
swL2IGMPRouterPortDynamicPortList=_SwL2IGMPRouterPortDynamicPortList_Object((1,3,6,1,4,1,171,11,101,1,2,11,6,1,4),_SwL2IGMPRouterPortDynamicPortList_Type())
swL2IGMPRouterPortDynamicPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterPortDynamicPortList.setStatus(_A)
_SwL2IGMPRouterPortForbiddenPortList_Type=PortList
_SwL2IGMPRouterPortForbiddenPortList_Object=MibTableColumn
swL2IGMPRouterPortForbiddenPortList=_SwL2IGMPRouterPortForbiddenPortList_Object((1,3,6,1,4,1,171,11,101,1,2,11,6,1,5),_SwL2IGMPRouterPortForbiddenPortList_Type())
swL2IGMPRouterPortForbiddenPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouterPortForbiddenPortList.setStatus(_A)
_SwIGMPSnoopingGroupTable_Object=MibTable
swIGMPSnoopingGroupTable=_SwIGMPSnoopingGroupTable_Object((1,3,6,1,4,1,171,11,101,1,2,11,11))
if mibBuilder.loadTexts:swIGMPSnoopingGroupTable.setStatus(_A)
_SwIGMPSnoopingGroupEntry_Object=MibTableRow
swIGMPSnoopingGroupEntry=_SwIGMPSnoopingGroupEntry_Object((1,3,6,1,4,1,171,11,101,1,2,11,11,1))
swIGMPSnoopingGroupEntry.setIndexNames((0,_E,_A3),(0,_E,_A4),(0,_E,_A5))
if mibBuilder.loadTexts:swIGMPSnoopingGroupEntry.setStatus(_A)
class _SwIGMPSnoopingGroupVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwIGMPSnoopingGroupVid_Type.__name__=_B
_SwIGMPSnoopingGroupVid_Object=MibTableColumn
swIGMPSnoopingGroupVid=_SwIGMPSnoopingGroupVid_Object((1,3,6,1,4,1,171,11,101,1,2,11,11,1,1),_SwIGMPSnoopingGroupVid_Type())
swIGMPSnoopingGroupVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupVid.setStatus(_A)
_SwIGMPSnoopingGroupGroupAddr_Type=IpAddress
_SwIGMPSnoopingGroupGroupAddr_Object=MibTableColumn
swIGMPSnoopingGroupGroupAddr=_SwIGMPSnoopingGroupGroupAddr_Object((1,3,6,1,4,1,171,11,101,1,2,11,11,1,2),_SwIGMPSnoopingGroupGroupAddr_Type())
swIGMPSnoopingGroupGroupAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupGroupAddr.setStatus(_A)
_SwIGMPSnoopingGroupSourceAddr_Type=IpAddress
_SwIGMPSnoopingGroupSourceAddr_Object=MibTableColumn
swIGMPSnoopingGroupSourceAddr=_SwIGMPSnoopingGroupSourceAddr_Object((1,3,6,1,4,1,171,11,101,1,2,11,11,1,3),_SwIGMPSnoopingGroupSourceAddr_Type())
swIGMPSnoopingGroupSourceAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupSourceAddr.setStatus(_A)
_SwIGMPSnoopingGroupIncludePortMap_Type=PortList
_SwIGMPSnoopingGroupIncludePortMap_Object=MibTableColumn
swIGMPSnoopingGroupIncludePortMap=_SwIGMPSnoopingGroupIncludePortMap_Object((1,3,6,1,4,1,171,11,101,1,2,11,11,1,4),_SwIGMPSnoopingGroupIncludePortMap_Type())
swIGMPSnoopingGroupIncludePortMap.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupIncludePortMap.setStatus(_A)
_SwIGMPSnoopingGroupExcludePortMap_Type=PortList
_SwIGMPSnoopingGroupExcludePortMap_Object=MibTableColumn
swIGMPSnoopingGroupExcludePortMap=_SwIGMPSnoopingGroupExcludePortMap_Object((1,3,6,1,4,1,171,11,101,1,2,11,11,1,5),_SwIGMPSnoopingGroupExcludePortMap_Type())
swIGMPSnoopingGroupExcludePortMap.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupExcludePortMap.setStatus(_A)
_SwIGMPSnoopingGroupReportCount_Type=Integer32
_SwIGMPSnoopingGroupReportCount_Object=MibTableColumn
swIGMPSnoopingGroupReportCount=_SwIGMPSnoopingGroupReportCount_Object((1,3,6,1,4,1,171,11,101,1,2,11,11,1,6),_SwIGMPSnoopingGroupReportCount_Type())
swIGMPSnoopingGroupReportCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupReportCount.setStatus(_A)
_SwIGMPSnoopingGroupUpTime_Type=TimeTicks
_SwIGMPSnoopingGroupUpTime_Object=MibTableColumn
swIGMPSnoopingGroupUpTime=_SwIGMPSnoopingGroupUpTime_Object((1,3,6,1,4,1,171,11,101,1,2,11,11,1,7),_SwIGMPSnoopingGroupUpTime_Type())
swIGMPSnoopingGroupUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupUpTime.setStatus(_A)
_SwIGMPSnoopingGroupExpiryTime_Type=TimeTicks
_SwIGMPSnoopingGroupExpiryTime_Object=MibTableColumn
swIGMPSnoopingGroupExpiryTime=_SwIGMPSnoopingGroupExpiryTime_Object((1,3,6,1,4,1,171,11,101,1,2,11,11,1,8),_SwIGMPSnoopingGroupExpiryTime_Type())
swIGMPSnoopingGroupExpiryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupExpiryTime.setStatus(_A)
_SwIGMPSnoopingGroupRouterPorts_Type=PortList
_SwIGMPSnoopingGroupRouterPorts_Object=MibTableColumn
swIGMPSnoopingGroupRouterPorts=_SwIGMPSnoopingGroupRouterPorts_Object((1,3,6,1,4,1,171,11,101,1,2,11,11,1,9),_SwIGMPSnoopingGroupRouterPorts_Type())
swIGMPSnoopingGroupRouterPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupRouterPorts.setStatus(_A)
_SwL2IGMPDynIpMultMgmt_ObjectIdentity=ObjectIdentity
swL2IGMPDynIpMultMgmt=_SwL2IGMPDynIpMultMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,11,12))
_SwL2IGMPDynIPMultMaxEntry_Type=Integer32
_SwL2IGMPDynIPMultMaxEntry_Object=MibScalar
swL2IGMPDynIPMultMaxEntry=_SwL2IGMPDynIPMultMaxEntry_Object((1,3,6,1,4,1,171,11,101,1,2,11,12,1),_SwL2IGMPDynIPMultMaxEntry_Type())
swL2IGMPDynIPMultMaxEntry.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPDynIPMultMaxEntry.setStatus(_A)
_SwL2IGMPDynIPMultCtrlTable_Object=MibTable
swL2IGMPDynIPMultCtrlTable=_SwL2IGMPDynIPMultCtrlTable_Object((1,3,6,1,4,1,171,11,101,1,2,11,12,3))
if mibBuilder.loadTexts:swL2IGMPDynIPMultCtrlTable.setStatus(_A)
_SwL2IGMPDynIPMultCtrlEntry_Object=MibTableRow
swL2IGMPDynIPMultCtrlEntry=_SwL2IGMPDynIPMultCtrlEntry_Object((1,3,6,1,4,1,171,11,101,1,2,11,12,3,1))
swL2IGMPDynIPMultCtrlEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:swL2IGMPDynIPMultCtrlEntry.setStatus(_A)
class _SwL2IGMPDynIPMultVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2IGMPDynIPMultVlanState_Type.__name__=_B
_SwL2IGMPDynIPMultVlanState_Object=MibTableColumn
swL2IGMPDynIPMultVlanState=_SwL2IGMPDynIPMultVlanState_Object((1,3,6,1,4,1,171,11,101,1,2,11,12,3,1,1),_SwL2IGMPDynIPMultVlanState_Type())
swL2IGMPDynIPMultVlanState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPDynIPMultVlanState.setStatus(_A)
class _SwL2IGMPDynIPMultVlanAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2IGMPDynIPMultVlanAge_Type.__name__=_B
_SwL2IGMPDynIPMultVlanAge_Object=MibTableColumn
swL2IGMPDynIPMultVlanAge=_SwL2IGMPDynIPMultVlanAge_Object((1,3,6,1,4,1,171,11,101,1,2,11,12,3,1,2),_SwL2IGMPDynIPMultVlanAge_Type())
swL2IGMPDynIPMultVlanAge.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPDynIPMultVlanAge.setStatus(_A)
_SwL2IGMPAccessAuthTable_Object=MibTable
swL2IGMPAccessAuthTable=_SwL2IGMPAccessAuthTable_Object((1,3,6,1,4,1,171,11,101,1,2,11,20))
if mibBuilder.loadTexts:swL2IGMPAccessAuthTable.setStatus(_A)
_SwL2IGMPAccessAuthEntry_Object=MibTableRow
swL2IGMPAccessAuthEntry=_SwL2IGMPAccessAuthEntry_Object((1,3,6,1,4,1,171,11,101,1,2,11,20,1))
swL2IGMPAccessAuthEntry.setIndexNames((0,_E,_A6))
if mibBuilder.loadTexts:swL2IGMPAccessAuthEntry.setStatus(_A)
class _SwL2IGMPAccessAuthPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPAccessAuthPort_Type.__name__=_B
_SwL2IGMPAccessAuthPort_Object=MibTableColumn
swL2IGMPAccessAuthPort=_SwL2IGMPAccessAuthPort_Object((1,3,6,1,4,1,171,11,101,1,2,11,20,1,1),_SwL2IGMPAccessAuthPort_Type())
swL2IGMPAccessAuthPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPAccessAuthPort.setStatus(_A)
class _SwL2IGMPAccessAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_M,3)))
_SwL2IGMPAccessAuthState_Type.__name__=_B
_SwL2IGMPAccessAuthState_Object=MibTableColumn
swL2IGMPAccessAuthState=_SwL2IGMPAccessAuthState_Object((1,3,6,1,4,1,171,11,101,1,2,11,20,1,2),_SwL2IGMPAccessAuthState_Type())
swL2IGMPAccessAuthState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPAccessAuthState.setStatus(_A)
_SwL2TrafficSegMgmt_ObjectIdentity=ObjectIdentity
swL2TrafficSegMgmt=_SwL2TrafficSegMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,14))
_SwL2TrafficSegTable_Object=MibTable
swL2TrafficSegTable=_SwL2TrafficSegTable_Object((1,3,6,1,4,1,171,11,101,1,2,14,1))
if mibBuilder.loadTexts:swL2TrafficSegTable.setStatus(_A)
_SwL2TrafficSegEntry_Object=MibTableRow
swL2TrafficSegEntry=_SwL2TrafficSegEntry_Object((1,3,6,1,4,1,171,11,101,1,2,14,1,1))
swL2TrafficSegEntry.setIndexNames((0,_E,_A7))
if mibBuilder.loadTexts:swL2TrafficSegEntry.setStatus(_A)
class _SwL2TrafficSegPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrafficSegPort_Type.__name__=_B
_SwL2TrafficSegPort_Object=MibTableColumn
swL2TrafficSegPort=_SwL2TrafficSegPort_Object((1,3,6,1,4,1,171,11,101,1,2,14,1,1,1),_SwL2TrafficSegPort_Type())
swL2TrafficSegPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrafficSegPort.setStatus(_A)
_SwL2TrafficSegForwardPorts_Type=PortList
_SwL2TrafficSegForwardPorts_Object=MibTableColumn
swL2TrafficSegForwardPorts=_SwL2TrafficSegForwardPorts_Object((1,3,6,1,4,1,171,11,101,1,2,14,1,1,2),_SwL2TrafficSegForwardPorts_Type())
swL2TrafficSegForwardPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrafficSegForwardPorts.setStatus(_A)
_SwL2MulticastFilterMode_ObjectIdentity=ObjectIdentity
swL2MulticastFilterMode=_SwL2MulticastFilterMode_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,17))
_SwL2MulticastFilterModeVlanTable_Object=MibTable
swL2MulticastFilterModeVlanTable=_SwL2MulticastFilterModeVlanTable_Object((1,3,6,1,4,1,171,11,101,1,2,17,1))
if mibBuilder.loadTexts:swL2MulticastFilterModeVlanTable.setStatus(_A)
_SwL2MulticastFilterModeVlanEntry_Object=MibTableRow
swL2MulticastFilterModeVlanEntry=_SwL2MulticastFilterModeVlanEntry_Object((1,3,6,1,4,1,171,11,101,1,2,17,1,1))
swL2MulticastFilterModeVlanEntry.setIndexNames((0,_E,_A8))
if mibBuilder.loadTexts:swL2MulticastFilterModeVlanEntry.setStatus(_A)
class _SwL2MulticastFilterVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2MulticastFilterVid_Type.__name__=_B
_SwL2MulticastFilterVid_Object=MibTableColumn
swL2MulticastFilterVid=_SwL2MulticastFilterVid_Object((1,3,6,1,4,1,171,11,101,1,2,17,1,1,1),_SwL2MulticastFilterVid_Type())
swL2MulticastFilterVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MulticastFilterVid.setStatus(_A)
class _SwL2MulticastFilterVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('forward-unregistered-groups',2),('filter-unregistered-groups',3)))
_SwL2MulticastFilterVlanMode_Type.__name__=_B
_SwL2MulticastFilterVlanMode_Object=MibTableColumn
swL2MulticastFilterVlanMode=_SwL2MulticastFilterVlanMode_Object((1,3,6,1,4,1,171,11,101,1,2,17,1,1,2),_SwL2MulticastFilterVlanMode_Type())
swL2MulticastFilterVlanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MulticastFilterVlanMode.setStatus(_A)
_SwL2LoopDetectMgmt_ObjectIdentity=ObjectIdentity
swL2LoopDetectMgmt=_SwL2LoopDetectMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,18))
_SwL2LoopDetectCtrl_ObjectIdentity=ObjectIdentity
swL2LoopDetectCtrl=_SwL2LoopDetectCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,18,1))
class _SwL2LoopDetectAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2LoopDetectAdminState_Type.__name__=_B
_SwL2LoopDetectAdminState_Object=MibScalar
swL2LoopDetectAdminState=_SwL2LoopDetectAdminState_Object((1,3,6,1,4,1,171,11,101,1,2,18,1,1),_SwL2LoopDetectAdminState_Type())
swL2LoopDetectAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectAdminState.setStatus(_A)
class _SwL2LoopDetectInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_SwL2LoopDetectInterval_Type.__name__=_B
_SwL2LoopDetectInterval_Object=MibScalar
swL2LoopDetectInterval=_SwL2LoopDetectInterval_Object((1,3,6,1,4,1,171,11,101,1,2,18,1,2),_SwL2LoopDetectInterval_Type())
swL2LoopDetectInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectInterval.setStatus(_A)
class _SwL2LoopDetectRecoverTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_SwL2LoopDetectRecoverTime_Type.__name__=_B
_SwL2LoopDetectRecoverTime_Object=MibScalar
swL2LoopDetectRecoverTime=_SwL2LoopDetectRecoverTime_Object((1,3,6,1,4,1,171,11,101,1,2,18,1,3),_SwL2LoopDetectRecoverTime_Type())
swL2LoopDetectRecoverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectRecoverTime.setStatus(_A)
class _SwL2LoopDetectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan-based',1),('port-based',2)))
_SwL2LoopDetectMode_Type.__name__=_B
_SwL2LoopDetectMode_Object=MibScalar
swL2LoopDetectMode=_SwL2LoopDetectMode_Object((1,3,6,1,4,1,171,11,101,1,2,18,1,4),_SwL2LoopDetectMode_Type())
swL2LoopDetectMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectMode.setStatus(_A)
class _SwL2LoopDetectTrapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('loop-detected',2),('loop-cleared',3),('both',4)))
_SwL2LoopDetectTrapMode_Type.__name__=_B
_SwL2LoopDetectTrapMode_Object=MibScalar
swL2LoopDetectTrapMode=_SwL2LoopDetectTrapMode_Object((1,3,6,1,4,1,171,11,101,1,2,18,1,5),_SwL2LoopDetectTrapMode_Type())
swL2LoopDetectTrapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectTrapMode.setStatus(_A)
_SwL2LoopDetectPortMgmt_ObjectIdentity=ObjectIdentity
swL2LoopDetectPortMgmt=_SwL2LoopDetectPortMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,18,2))
_SwL2LoopDetectPortTable_Object=MibTable
swL2LoopDetectPortTable=_SwL2LoopDetectPortTable_Object((1,3,6,1,4,1,171,11,101,1,2,18,2,1))
if mibBuilder.loadTexts:swL2LoopDetectPortTable.setStatus(_A)
_SwL2LoopDetectPortEntry_Object=MibTableRow
swL2LoopDetectPortEntry=_SwL2LoopDetectPortEntry_Object((1,3,6,1,4,1,171,11,101,1,2,18,2,1,1))
swL2LoopDetectPortEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:swL2LoopDetectPortEntry.setStatus(_A)
class _SwL2LoopDetectPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2LoopDetectPortIndex_Type.__name__=_B
_SwL2LoopDetectPortIndex_Object=MibTableColumn
swL2LoopDetectPortIndex=_SwL2LoopDetectPortIndex_Object((1,3,6,1,4,1,171,11,101,1,2,18,2,1,1,1),_SwL2LoopDetectPortIndex_Type())
swL2LoopDetectPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectPortIndex.setStatus(_A)
class _SwL2LoopDetectPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2LoopDetectPortState_Type.__name__=_B
_SwL2LoopDetectPortState_Object=MibTableColumn
swL2LoopDetectPortState=_SwL2LoopDetectPortState_Object((1,3,6,1,4,1,171,11,101,1,2,18,2,1,1,2),_SwL2LoopDetectPortState_Type())
swL2LoopDetectPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectPortState.setStatus(_A)
_SwL2LoopDetectPortLoopVLAN_Type=DisplayString
_SwL2LoopDetectPortLoopVLAN_Object=MibTableColumn
swL2LoopDetectPortLoopVLAN=_SwL2LoopDetectPortLoopVLAN_Object((1,3,6,1,4,1,171,11,101,1,2,18,2,1,1,3),_SwL2LoopDetectPortLoopVLAN_Type())
swL2LoopDetectPortLoopVLAN.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectPortLoopVLAN.setStatus(_A)
class _SwL2LoopDetectPortLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_T,1),('loop',2),('error',3),(_L,4)))
_SwL2LoopDetectPortLoopStatus_Type.__name__=_B
_SwL2LoopDetectPortLoopStatus_Object=MibTableColumn
swL2LoopDetectPortLoopStatus=_SwL2LoopDetectPortLoopStatus_Object((1,3,6,1,4,1,171,11,101,1,2,18,2,1,1,4),_SwL2LoopDetectPortLoopStatus_Type())
swL2LoopDetectPortLoopStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectPortLoopStatus.setStatus(_A)
_SwL2DhcpLocalRelayMgmt_ObjectIdentity=ObjectIdentity
swL2DhcpLocalRelayMgmt=_SwL2DhcpLocalRelayMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,24))
class _SwL2DhcpLocalRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DhcpLocalRelayState_Type.__name__=_B
_SwL2DhcpLocalRelayState_Object=MibScalar
swL2DhcpLocalRelayState=_SwL2DhcpLocalRelayState_Object((1,3,6,1,4,1,171,11,101,1,2,24,1),_SwL2DhcpLocalRelayState_Type())
swL2DhcpLocalRelayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpLocalRelayState.setStatus(_A)
_SwL2DhcpLocalRelayVLANTable_Object=MibTable
swL2DhcpLocalRelayVLANTable=_SwL2DhcpLocalRelayVLANTable_Object((1,3,6,1,4,1,171,11,101,1,2,24,2))
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANTable.setStatus(_A)
_SwL2DhcpLocalRelayVLANEntry_Object=MibTableRow
swL2DhcpLocalRelayVLANEntry=_SwL2DhcpLocalRelayVLANEntry_Object((1,3,6,1,4,1,171,11,101,1,2,24,2,1))
swL2DhcpLocalRelayVLANEntry.setIndexNames((0,_E,_A9))
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANEntry.setStatus(_A)
class _SwL2DhcpLocalRelayVLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2DhcpLocalRelayVLANID_Type.__name__=_B
_SwL2DhcpLocalRelayVLANID_Object=MibTableColumn
swL2DhcpLocalRelayVLANID=_SwL2DhcpLocalRelayVLANID_Object((1,3,6,1,4,1,171,11,101,1,2,24,2,1,1),_SwL2DhcpLocalRelayVLANID_Type())
swL2DhcpLocalRelayVLANID.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANID.setStatus(_A)
class _SwL2DhcpLocalRelayVLANState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DhcpLocalRelayVLANState_Type.__name__=_B
_SwL2DhcpLocalRelayVLANState_Object=MibTableColumn
swL2DhcpLocalRelayVLANState=_SwL2DhcpLocalRelayVLANState_Object((1,3,6,1,4,1,171,11,101,1,2,24,2,1,2),_SwL2DhcpLocalRelayVLANState_Type())
swL2DhcpLocalRelayVLANState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANState.setStatus(_A)
_SwL2MgmtMIBTraps_ObjectIdentity=ObjectIdentity
swL2MgmtMIBTraps=_SwL2MgmtMIBTraps_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,100))
_SwL2Notify_ObjectIdentity=ObjectIdentity
swL2Notify=_SwL2Notify_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,100,1))
_SwL2NotifyMgmt_ObjectIdentity=ObjectIdentity
swL2NotifyMgmt=_SwL2NotifyMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,100,1,1))
_SwL2NotifyPrefix_ObjectIdentity=ObjectIdentity
swL2NotifyPrefix=_SwL2NotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,100,1,2))
_SwL2NotifFirmware_ObjectIdentity=ObjectIdentity
swL2NotifFirmware=_SwL2NotifFirmware_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,100,1,2,0))
_Swl2NotificationBidings_ObjectIdentity=ObjectIdentity
swl2NotificationBidings=_Swl2NotificationBidings_ObjectIdentity((1,3,6,1,4,1,171,11,101,1,2,100,1,2,1))
class _SwL2macNotifyInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_SwL2macNotifyInfo_Type.__name__=_O
_SwL2macNotifyInfo_Object=MibScalar
swL2macNotifyInfo=_SwL2macNotifyInfo_Object((1,3,6,1,4,1,171,11,101,1,2,100,1,2,1,1),_SwL2macNotifyInfo_Type())
swL2macNotifyInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2macNotifyInfo.setStatus(_A)
_SwL2PortSecurityViolationMac_Type=MacAddress
_SwL2PortSecurityViolationMac_Object=MibScalar
swL2PortSecurityViolationMac=_SwL2PortSecurityViolationMac_Object((1,3,6,1,4,1,171,11,101,1,2,100,1,2,1,2),_SwL2PortSecurityViolationMac_Type())
swL2PortSecurityViolationMac.setMaxAccess(_AA)
if mibBuilder.loadTexts:swL2PortSecurityViolationMac.setStatus(_A)
_SwL2VlanLoopDetectVID_Type=Integer32
_SwL2VlanLoopDetectVID_Object=MibScalar
swL2VlanLoopDetectVID=_SwL2VlanLoopDetectVID_Object((1,3,6,1,4,1,171,11,101,1,2,100,1,2,1,3),_SwL2VlanLoopDetectVID_Type())
swL2VlanLoopDetectVID.setMaxAccess(_AA)
if mibBuilder.loadTexts:swL2VlanLoopDetectVID.setStatus(_A)
swL2macNotification=NotificationType((1,3,6,1,4,1,171,11,101,1,2,100,1,2,0,1))
swL2macNotification.setObjects((_E,_AB))
if mibBuilder.loadTexts:swL2macNotification.setStatus(_A)
swL2PortSecurityViolationTrap=NotificationType((1,3,6,1,4,1,171,11,101,1,2,100,1,2,0,2))
swL2PortSecurityViolationTrap.setObjects(*((_E,_Q),(_E,_AC)))
if mibBuilder.loadTexts:swL2PortSecurityViolationTrap.setStatus(_A)
swL2PortLoopOccurred=NotificationType((1,3,6,1,4,1,171,11,101,1,2,100,1,2,0,3))
swL2PortLoopOccurred.setObjects((_E,_J))
if mibBuilder.loadTexts:swL2PortLoopOccurred.setStatus(_A)
swL2PortLoopRestart=NotificationType((1,3,6,1,4,1,171,11,101,1,2,100,1,2,0,4))
swL2PortLoopRestart.setObjects((_E,_J))
if mibBuilder.loadTexts:swL2PortLoopRestart.setStatus(_A)
swL2VlanLoopOccurred=NotificationType((1,3,6,1,4,1,171,11,101,1,2,100,1,2,0,5))
swL2VlanLoopOccurred.setObjects(*((_E,_J),(_E,_S)))
if mibBuilder.loadTexts:swL2VlanLoopOccurred.setStatus(_A)
swL2VlanLoopRestart=NotificationType((1,3,6,1,4,1,171,11,101,1,2,100,1,2,0,6))
swL2VlanLoopRestart.setObjects(*((_E,_J),(_E,_S)))
if mibBuilder.loadTexts:swL2VlanLoopRestart.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'MacAddress':MacAddress,'VlanId':VlanId,'PortList':PortList,'swL2MgmtMIB':swL2MgmtMIB,'swL2DevMgmt':swL2DevMgmt,'swL2DevInfo':swL2DevInfo,'swDevInfoTotalNumOfPort':swDevInfoTotalNumOfPort,'swDevInfoNumOfPortInUse':swDevInfoNumOfPortInUse,'swDevInfoFrontPanelLedStatus':swDevInfoFrontPanelLedStatus,'swL2DevCtrl':swL2DevCtrl,'swL2DevCtrlStpState':swL2DevCtrlStpState,'swL2DevCtrlIGMPSnooping':swL2DevCtrlIGMPSnooping,'swL2DevCtrlRmonState':swL2DevCtrlRmonState,'swL2DevCtrlSnmpTrapState':swL2DevCtrlSnmpTrapState,'swL2DevCtrlCleanAllStatisticCounter':swL2DevCtrlCleanAllStatisticCounter,'swL2DevCtrlVlanIdOfFDBTbl':swL2DevCtrlVlanIdOfFDBTbl,'swL2MACNotifyState':swL2MACNotifyState,'swL2MACNotifyHistorySize':swL2MACNotifyHistorySize,'swL2MACNotifyInterval':swL2MACNotifyInterval,'swL2DevCtrlTelnet':swL2DevCtrlTelnet,'swL2DevCtrlTelnetState':swL2DevCtrlTelnetState,'swL2DevCtrlTelnetTcpPort':swL2DevCtrlTelnetTcpPort,'swL2DevCtrlManagementVlanId':swL2DevCtrlManagementVlanId,'swL2DevCtrlWeb':swL2DevCtrlWeb,'swL2DevCtrlWebState':swL2DevCtrlWebState,'swL2DevCtrlWebTcpPort':swL2DevCtrlWebTcpPort,'swL2DevCtrlLLDPState':swL2DevCtrlLLDPState,'swL2DevCtrlLLDPForwardMessageState':swL2DevCtrlLLDPForwardMessageState,'swL2DevCtrlIpAutoconfig':swL2DevCtrlIpAutoconfig,'swL2DevCtrlCFM':swL2DevCtrlCFM,'swL2DevCtrlCFMState':swL2DevCtrlCFMState,'swL2DevCtrlCFMPortTable':swL2DevCtrlCFMPortTable,'swL2DevCtrlCFMPortEntry':swL2DevCtrlCFMPortEntry,_V:swL2DevCtrlCFMPortIndex,'swL2DevCtrlCFMPortState':swL2DevCtrlCFMPortState,'swL2DevCtrlVLANTrunkState':swL2DevCtrlVLANTrunkState,'swL2DevAlarm':swL2DevAlarm,'swL2DevAlarmNewRoot':swL2DevAlarmNewRoot,'swL2DevAlarmTopologyChange':swL2DevAlarmTopologyChange,'swL2DevAlarmLinkChange':swL2DevAlarmLinkChange,'swL2VLANMgmt':swL2VLANMgmt,'swL2VlanStaticTable':swL2VlanStaticTable,'swL2VlanStaticEntry':swL2VlanStaticEntry,_X:swL2VlanIndex,'swL2VLANAdvertisement':swL2VLANAdvertisement,'swL2PVIDAutoAssignmentState':swL2PVIDAutoAssignmentState,'swL2VlanPortInfoTable':swL2VlanPortInfoTable,'swL2VlanPortInfoEntry':swL2VlanPortInfoEntry,_Y:swL2VlanPortInfoPortIndex,_Z:swL2VlanPortInfoVid,'swL2VlanPortInfoPortRole':swL2VlanPortInfoPortRole,'swL2PortMgmt':swL2PortMgmt,'swL2PortInfoTable':swL2PortInfoTable,'swL2PortInfoEntry':swL2PortInfoEntry,_a:swL2PortInfoPortIndex,_b:swL2PortInfoMediumType,'swL2PortInfoUnitID':swL2PortInfoUnitID,'swL2PortInfoType':swL2PortInfoType,'swL2PortInfoLinkStatus':swL2PortInfoLinkStatus,'swL2PortInfoNwayStatus':swL2PortInfoNwayStatus,'swL2PortInfoErrorDisabled':swL2PortInfoErrorDisabled,'swL2PortCtrlTable':swL2PortCtrlTable,'swL2PortCtrlEntry':swL2PortCtrlEntry,_f:swL2PortCtrlPortIndex,_g:swL2PortCtrlMediumType,'swL2PortCtrlUnitIndex':swL2PortCtrlUnitIndex,'swL2PortCtrlAdminState':swL2PortCtrlAdminState,'swL2PortCtrlNwayState':swL2PortCtrlNwayState,'swL2PortCtrlFlowCtrlState':swL2PortCtrlFlowCtrlState,'swL2PortCtrlLearningState':swL2PortCtrlLearningState,'swL2PortCtrlMACNotifyState':swL2PortCtrlMACNotifyState,'swL2PortCtrlJumboFrame':swL2PortCtrlJumboFrame,'swL2PortCtrlJumboFrameMaxSize':swL2PortCtrlJumboFrameMaxSize,'swL2PortCounterCtrlTable':swL2PortCounterCtrlTable,'swL2PortCounterCtrlEntry':swL2PortCounterCtrlEntry,_h:swL2PortCounterCtrlPortIndex,'swL2PortCounterClearCtrl':swL2PortCounterClearCtrl,'swL2PortErrTable':swL2PortErrTable,'swL2PortErrEntry':swL2PortErrEntry,_i:swL2PortErrPortIndex,'swL2PortErrPortState':swL2PortErrPortState,'swL2PortErrPortConnStatus':swL2PortErrPortConnStatus,'swL2PortErrPortReason':swL2PortErrPortReason,'swL2LimitedMulticastMgmt':swL2LimitedMulticastMgmt,'swL2MulticastFilterProfileTable':swL2MulticastFilterProfileTable,'swL2MulticastFilterProfileEntry':swL2MulticastFilterProfileEntry,_j:swL2MulticastFilterProfileIndex,'swL2MulticastFilterProfileName':swL2MulticastFilterProfileName,'swL2MulticastFilterStatus':swL2MulticastFilterStatus,'swL2MulticastFilterProfileAddressTable':swL2MulticastFilterProfileAddressTable,'swL2MulticastFilterProfileAddressEntry':swL2MulticastFilterProfileAddressEntry,_k:swL2MulticastFilterProfileIdIndex,_l:swL2MulticastFilterFromIp,_m:swL2MulticastFilterToIp,'swL2MulticastFilterAddressState':swL2MulticastFilterAddressState,'swL2LimitedMulticastFilterPortTable':swL2LimitedMulticastFilterPortTable,'swL2LimitedMulticastFilterPortEntry':swL2LimitedMulticastFilterPortEntry,_n:swL2LimitedMulticastFilterPortIndex,'swL2LimitedMulticastFilterPortAccess':swL2LimitedMulticastFilterPortAccess,'swL2LimitedMulticastFilterPortProfileID':swL2LimitedMulticastFilterPortProfileID,'swL2LimitedMulticastFilterPortProfileStatus':swL2LimitedMulticastFilterPortProfileStatus,'swL2MulticastFilterPortMaxGroupTable':swL2MulticastFilterPortMaxGroupTable,'swL2MulticastFilterPortMaxGroupEntry':swL2MulticastFilterPortMaxGroupEntry,_o:swL2MulticastFilterPortMaxGroupPortIndex,'swL2MulticastFilterPortMaxGroup':swL2MulticastFilterPortMaxGroup,'swL2QOSMgmt':swL2QOSMgmt,'swL2QOSBandwidthControlTable':swL2QOSBandwidthControlTable,'swL2QOSBandwidthControlEntry':swL2QOSBandwidthControlEntry,_p:swL2QOSBandwidthPortIndex,'swL2QOSBandwidthRxRate':swL2QOSBandwidthRxRate,'swL2QOSBandwidthTxRate':swL2QOSBandwidthTxRate,'swL2QOSBandwidthRadiusRxRate':swL2QOSBandwidthRadiusRxRate,'swL2QOSBandwidthRadiusTxRate':swL2QOSBandwidthRadiusTxRate,'swL2QOSSchedulingTable':swL2QOSSchedulingTable,'swL2QOSSchedulingEntry':swL2QOSSchedulingEntry,_q:swL2QOSSchedulingClassIndex,'swL2QOSSchedulingMaxPkts':swL2QOSSchedulingMaxPkts,'swL2QOSSchedulingMechanism':swL2QOSSchedulingMechanism,'swL2QOS8021pUserPriorityTable':swL2QOS8021pUserPriorityTable,'swL2QOS8021pUserPriorityEntry':swL2QOS8021pUserPriorityEntry,_u:swL2QOS8021pUserPriorityIndex,'swL2QOS8021pUserPriorityClass':swL2QOS8021pUserPriorityClass,'swL2QOS8021pDefaultPriorityTable':swL2QOS8021pDefaultPriorityTable,'swL2QOS8021pDefaultPriorityEntry':swL2QOS8021pDefaultPriorityEntry,_v:swL2QOS8021pDefaultPriorityIndex,'swL2QOS8021pDefaultPriority':swL2QOS8021pDefaultPriority,'swL2QOS8021pRadiusPriority':swL2QOS8021pRadiusPriority,'swL2QOSSchedulingMechanismCtrl':swL2QOSSchedulingMechanismCtrl,'swL2PortSecurityMgmt':swL2PortSecurityMgmt,'swL2PortSecurityControlTable':swL2PortSecurityControlTable,'swL2PortSecurityControlEntry':swL2PortSecurityControlEntry,_Q:swL2PortSecurityPortIndex,'swL2PortSecurityMaxLernAddr':swL2PortSecurityMaxLernAddr,'swL2PortSecurityMode':swL2PortSecurityMode,'swL2PortSecurityAdmState':swL2PortSecurityAdmState,'swL2PortSecurityEntryClearCtrl':swL2PortSecurityEntryClearCtrl,'swL2PortSecurityDelCtrl':swL2PortSecurityDelCtrl,'swL2PortSecurityDelVlanName':swL2PortSecurityDelVlanName,'swL2PortSecurityDelPort':swL2PortSecurityDelPort,'swL2PortSecurityDelMacAddress':swL2PortSecurityDelMacAddress,'swL2PortSecurityDelActivity':swL2PortSecurityDelActivity,'swL2PortSecurityTrapLogState':swL2PortSecurityTrapLogState,'swL2DhcpRelayMgmt':swL2DhcpRelayMgmt,'swL2DhcpRelayState':swL2DhcpRelayState,'swL2DhcpRelayHopCount':swL2DhcpRelayHopCount,'swL2DhcpRelayTimeThreshold':swL2DhcpRelayTimeThreshold,'swL2DhcpRelayOption82State':swL2DhcpRelayOption82State,'swL2DhcpRelayOption82Check':swL2DhcpRelayOption82Check,'swL2DhcpRelayOption82Policy':swL2DhcpRelayOption82Policy,'swL2DhcpRelayCtrlTable':swL2DhcpRelayCtrlTable,'swL2DhcpRelayCtrlEntry':swL2DhcpRelayCtrlEntry,_w:swL2DhcpRelayCtrlInterfaceName,_x:swL2DhcpRelayCtrlServer,'swL2DhcpRelayCtrlState':swL2DhcpRelayCtrlState,'swL2TrunkMgmt':swL2TrunkMgmt,'swL2TrunkMaxSupportedEntries':swL2TrunkMaxSupportedEntries,'swL2TrunkCurrentNumEntries':swL2TrunkCurrentNumEntries,'swL2TrunkCtrlTable':swL2TrunkCtrlTable,'swL2TrunkCtrlEntry':swL2TrunkCtrlEntry,_y:swL2TrunkIndex,'swL2TrunkMasterPort':swL2TrunkMasterPort,'swL2TrunkMember':swL2TrunkMember,'swL2TrunkType':swL2TrunkType,'swL2TrunkState':swL2TrunkState,'swL2TrunkActivePort':swL2TrunkActivePort,'swL2TrunkAlgorithm':swL2TrunkAlgorithm,'swL2TrunkLACPPortTable':swL2TrunkLACPPortTable,'swL2TrunkLACPPortEntry':swL2TrunkLACPPortEntry,_z:swL2TrunkLACPPortIndex,'swL2TrunkLACPPortState':swL2TrunkLACPPortState,'swL2TrunkVLANTable':swL2TrunkVLANTable,'swL2TrunkVLANEntry':swL2TrunkVLANEntry,_A0:swL2TrunkVLANPort,'swL2TrunkVLANState':swL2TrunkVLANState,'swL2MirrorMgmt':swL2MirrorMgmt,'swL2MirrorLogicTargetPort':swL2MirrorLogicTargetPort,'swL2MirrorPortSourceIngress':swL2MirrorPortSourceIngress,'swL2MirrorPortSourceEgress':swL2MirrorPortSourceEgress,'swL2MirrorPortState':swL2MirrorPortState,'swL2IGMPMgmt':swL2IGMPMgmt,'swL2IGMPMaxSupportedVlans':swL2IGMPMaxSupportedVlans,'swL2IGMPMaxIpGroupNumPerVlan':swL2IGMPMaxIpGroupNumPerVlan,'swL2IGMPCtrlTable':swL2IGMPCtrlTable,'swL2IGMPCtrlEntry':swL2IGMPCtrlEntry,_R:swL2IGMPCtrlVid,'swL2IGMPQueryInterval':swL2IGMPQueryInterval,'swL2IGMPMaxResponseTime':swL2IGMPMaxResponseTime,'swL2IGMPRobustness':swL2IGMPRobustness,'swL2IGMPLastMemberQueryInterval':swL2IGMPLastMemberQueryInterval,'swL2IGMPHostTimeout':swL2IGMPHostTimeout,'swL2IGMPRouteTimeout':swL2IGMPRouteTimeout,'swL2IGMPLeaveTimer':swL2IGMPLeaveTimer,'swL2IGMPQueryState':swL2IGMPQueryState,'swL2IGMPCurrentState':swL2IGMPCurrentState,'swL2IGMPCtrlState':swL2IGMPCtrlState,'swL2IGMPFastLeaveState':swL2IGMPFastLeaveState,'swL2IGMPQueryVersion':swL2IGMPQueryVersion,'swL2IGMPQueryInfoTable':swL2IGMPQueryInfoTable,'swL2IGMPQueryInfoEntry':swL2IGMPQueryInfoEntry,_A1:swL2IGMPInfoVid,'swL2IGMPInfoQueryCount':swL2IGMPInfoQueryCount,'swL2IGMPInfoTxQueryCount':swL2IGMPInfoTxQueryCount,'swL2IGMPRouterPortTable':swL2IGMPRouterPortTable,'swL2IGMPRouterPortEntry':swL2IGMPRouterPortEntry,_A2:swL2IGMPRouterPortVlanid,'swL2IGMPRouterPortVlanName':swL2IGMPRouterPortVlanName,'swL2IGMPRouterPortStaticPortList':swL2IGMPRouterPortStaticPortList,'swL2IGMPRouterPortDynamicPortList':swL2IGMPRouterPortDynamicPortList,'swL2IGMPRouterPortForbiddenPortList':swL2IGMPRouterPortForbiddenPortList,'swIGMPSnoopingGroupTable':swIGMPSnoopingGroupTable,'swIGMPSnoopingGroupEntry':swIGMPSnoopingGroupEntry,_A3:swIGMPSnoopingGroupVid,_A4:swIGMPSnoopingGroupGroupAddr,_A5:swIGMPSnoopingGroupSourceAddr,'swIGMPSnoopingGroupIncludePortMap':swIGMPSnoopingGroupIncludePortMap,'swIGMPSnoopingGroupExcludePortMap':swIGMPSnoopingGroupExcludePortMap,'swIGMPSnoopingGroupReportCount':swIGMPSnoopingGroupReportCount,'swIGMPSnoopingGroupUpTime':swIGMPSnoopingGroupUpTime,'swIGMPSnoopingGroupExpiryTime':swIGMPSnoopingGroupExpiryTime,'swIGMPSnoopingGroupRouterPorts':swIGMPSnoopingGroupRouterPorts,'swL2IGMPDynIpMultMgmt':swL2IGMPDynIpMultMgmt,'swL2IGMPDynIPMultMaxEntry':swL2IGMPDynIPMultMaxEntry,'swL2IGMPDynIPMultCtrlTable':swL2IGMPDynIPMultCtrlTable,'swL2IGMPDynIPMultCtrlEntry':swL2IGMPDynIPMultCtrlEntry,'swL2IGMPDynIPMultVlanState':swL2IGMPDynIPMultVlanState,'swL2IGMPDynIPMultVlanAge':swL2IGMPDynIPMultVlanAge,'swL2IGMPAccessAuthTable':swL2IGMPAccessAuthTable,'swL2IGMPAccessAuthEntry':swL2IGMPAccessAuthEntry,_A6:swL2IGMPAccessAuthPort,'swL2IGMPAccessAuthState':swL2IGMPAccessAuthState,'swL2TrafficSegMgmt':swL2TrafficSegMgmt,'swL2TrafficSegTable':swL2TrafficSegTable,'swL2TrafficSegEntry':swL2TrafficSegEntry,_A7:swL2TrafficSegPort,'swL2TrafficSegForwardPorts':swL2TrafficSegForwardPorts,'swL2MulticastFilterMode':swL2MulticastFilterMode,'swL2MulticastFilterModeVlanTable':swL2MulticastFilterModeVlanTable,'swL2MulticastFilterModeVlanEntry':swL2MulticastFilterModeVlanEntry,_A8:swL2MulticastFilterVid,'swL2MulticastFilterVlanMode':swL2MulticastFilterVlanMode,'swL2LoopDetectMgmt':swL2LoopDetectMgmt,'swL2LoopDetectCtrl':swL2LoopDetectCtrl,'swL2LoopDetectAdminState':swL2LoopDetectAdminState,'swL2LoopDetectInterval':swL2LoopDetectInterval,'swL2LoopDetectRecoverTime':swL2LoopDetectRecoverTime,'swL2LoopDetectMode':swL2LoopDetectMode,'swL2LoopDetectTrapMode':swL2LoopDetectTrapMode,'swL2LoopDetectPortMgmt':swL2LoopDetectPortMgmt,'swL2LoopDetectPortTable':swL2LoopDetectPortTable,'swL2LoopDetectPortEntry':swL2LoopDetectPortEntry,_J:swL2LoopDetectPortIndex,'swL2LoopDetectPortState':swL2LoopDetectPortState,'swL2LoopDetectPortLoopVLAN':swL2LoopDetectPortLoopVLAN,'swL2LoopDetectPortLoopStatus':swL2LoopDetectPortLoopStatus,'swL2DhcpLocalRelayMgmt':swL2DhcpLocalRelayMgmt,'swL2DhcpLocalRelayState':swL2DhcpLocalRelayState,'swL2DhcpLocalRelayVLANTable':swL2DhcpLocalRelayVLANTable,'swL2DhcpLocalRelayVLANEntry':swL2DhcpLocalRelayVLANEntry,_A9:swL2DhcpLocalRelayVLANID,'swL2DhcpLocalRelayVLANState':swL2DhcpLocalRelayVLANState,'swL2MgmtMIBTraps':swL2MgmtMIBTraps,'swL2Notify':swL2Notify,'swL2NotifyMgmt':swL2NotifyMgmt,'swL2NotifyPrefix':swL2NotifyPrefix,'swL2NotifFirmware':swL2NotifFirmware,'swL2macNotification':swL2macNotification,'swL2PortSecurityViolationTrap':swL2PortSecurityViolationTrap,'swL2PortLoopOccurred':swL2PortLoopOccurred,'swL2PortLoopRestart':swL2PortLoopRestart,'swL2VlanLoopOccurred':swL2VlanLoopOccurred,'swL2VlanLoopRestart':swL2VlanLoopRestart,'swl2NotificationBidings':swl2NotificationBidings,_AB:swL2macNotifyInfo,_AC:swL2PortSecurityViolationMac,_S:swL2VlanLoopDetectVID})