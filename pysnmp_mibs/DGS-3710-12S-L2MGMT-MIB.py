_k='swL2DyingGaspMac'
_j='swL2macNotifyInfo'
_i='swL2DhcpLocalRelayVLANID'
_h='swL2MulticastFilterVid'
_g='swL2TrafficSegPort'
_f='swL2TrunkLACPPortIndex'
_e='swL2TrunkIndex'
_d='swL2PortDropCounterPortIndex'
_c='swL2PortErrPortIndex'
_b='swL2PortCounterCtrlPortIndex'
_a='swL2PortCtrlMediumType'
_Z='swL2PortCtrlPortIndex'
_Y='ctp-lbd'
_X='err-disabled'
_W='copper'
_V='swL2PortInfoMediumType'
_U='swL2PortInfoPortIndex'
_T='swL2VlanPortInfoVid'
_S='swL2VlanPortInfoPortIndex'
_R='swL2VlanIndex'
_Q='not-accessible'
_P='swL2DevCtrlCFMPortIndex'
_O='active'
_N='swL2VlanLoopDetectVID'
_M='normal'
_L='OctetString'
_K='read-create'
_J='none'
_I='swL2LoopDetectPortIndex'
_H='other'
_G='DGS-3710-12S-L2MGMT-MIB'
_F='enabled'
_E='disabled'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AgentNotifyLevel,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','AgentNotifyLevel')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
dgs3710s,=mibBuilder.importSymbols('SW3700PRIMGMT-MIB','dgs3710s')
swL2MgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,11,102,1,4,2))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
class Ipv6Address(TextualConvention,OctetString):status=_A;displayHint='2x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwL2DevMgmt_ObjectIdentity=ObjectIdentity
swL2DevMgmt=_SwL2DevMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,1))
_SwL2DevInfo_ObjectIdentity=ObjectIdentity
swL2DevInfo=_SwL2DevInfo_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,1,1))
class _SwDevInfoTotalNumOfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwDevInfoTotalNumOfPort_Type.__name__=_B
_SwDevInfoTotalNumOfPort_Object=MibScalar
swDevInfoTotalNumOfPort=_SwDevInfoTotalNumOfPort_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,1,1),_SwDevInfoTotalNumOfPort_Type())
swDevInfoTotalNumOfPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swDevInfoTotalNumOfPort.setStatus(_A)
class _SwDevInfoNumOfPortInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwDevInfoNumOfPortInUse_Type.__name__=_B
_SwDevInfoNumOfPortInUse_Object=MibScalar
swDevInfoNumOfPortInUse=_SwDevInfoNumOfPortInUse_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,1,2),_SwDevInfoNumOfPortInUse_Type())
swDevInfoNumOfPortInUse.setMaxAccess(_D)
if mibBuilder.loadTexts:swDevInfoNumOfPortInUse.setStatus(_A)
class _SwDevInfoFrontPanelLedStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwDevInfoFrontPanelLedStatus_Type.__name__=_L
_SwDevInfoFrontPanelLedStatus_Object=MibScalar
swDevInfoFrontPanelLedStatus=_SwDevInfoFrontPanelLedStatus_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,1,4),_SwDevInfoFrontPanelLedStatus_Type())
swDevInfoFrontPanelLedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swDevInfoFrontPanelLedStatus.setStatus(_A)
_SwL2DevCtrl_ObjectIdentity=ObjectIdentity
swL2DevCtrl=_SwL2DevCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,1,2))
class _SwL2DevCtrlStpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_E,2),(_F,3)))
_SwL2DevCtrlStpState_Type.__name__=_B
_SwL2DevCtrlStpState_Object=MibScalar
swL2DevCtrlStpState=_SwL2DevCtrlStpState_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,1),_SwL2DevCtrlStpState_Type())
swL2DevCtrlStpState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlStpState.setStatus(_A)
class _SwL2DevCtrlIGMPSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_E,2),(_F,3)))
_SwL2DevCtrlIGMPSnooping_Type.__name__=_B
_SwL2DevCtrlIGMPSnooping_Object=MibScalar
swL2DevCtrlIGMPSnooping=_SwL2DevCtrlIGMPSnooping_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,2),_SwL2DevCtrlIGMPSnooping_Type())
swL2DevCtrlIGMPSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlIGMPSnooping.setStatus(_A)
class _SwL2DevCtrlSnmpTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_SwL2DevCtrlSnmpTrapState_Type.__name__=_B
_SwL2DevCtrlSnmpTrapState_Object=MibScalar
swL2DevCtrlSnmpTrapState=_SwL2DevCtrlSnmpTrapState_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,5),_SwL2DevCtrlSnmpTrapState_Type())
swL2DevCtrlSnmpTrapState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlSnmpTrapState.setStatus(_A)
class _SwL2DevCtrlCleanAllStatisticCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_O,2)))
_SwL2DevCtrlCleanAllStatisticCounter_Type.__name__=_B
_SwL2DevCtrlCleanAllStatisticCounter_Object=MibScalar
swL2DevCtrlCleanAllStatisticCounter=_SwL2DevCtrlCleanAllStatisticCounter_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,6),_SwL2DevCtrlCleanAllStatisticCounter_Type())
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlCleanAllStatisticCounter.setStatus(_A)
_SwL2DevCtrlVlanIdOfFDBTbl_Type=VlanId
_SwL2DevCtrlVlanIdOfFDBTbl_Object=MibScalar
swL2DevCtrlVlanIdOfFDBTbl=_SwL2DevCtrlVlanIdOfFDBTbl_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,7),_SwL2DevCtrlVlanIdOfFDBTbl_Type())
swL2DevCtrlVlanIdOfFDBTbl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlVlanIdOfFDBTbl.setStatus(_A)
class _SwL2MACNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_E,2),(_F,3)))
_SwL2MACNotifyState_Type.__name__=_B
_SwL2MACNotifyState_Object=MibScalar
swL2MACNotifyState=_SwL2MACNotifyState_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,8),_SwL2MACNotifyState_Type())
swL2MACNotifyState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MACNotifyState.setStatus(_A)
class _SwL2MACNotifyHistorySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_SwL2MACNotifyHistorySize_Type.__name__=_B
_SwL2MACNotifyHistorySize_Object=MibScalar
swL2MACNotifyHistorySize=_SwL2MACNotifyHistorySize_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,9),_SwL2MACNotifyHistorySize_Type())
swL2MACNotifyHistorySize.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MACNotifyHistorySize.setStatus(_A)
class _SwL2MACNotifyInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SwL2MACNotifyInterval_Type.__name__=_B
_SwL2MACNotifyInterval_Object=MibScalar
swL2MACNotifyInterval=_SwL2MACNotifyInterval_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,10),_SwL2MACNotifyInterval_Type())
swL2MACNotifyInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MACNotifyInterval.setStatus(_A)
_SwL2DevCtrlTelnet_ObjectIdentity=ObjectIdentity
swL2DevCtrlTelnet=_SwL2DevCtrlTelnet_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,1,2,14))
class _SwL2DevCtrlTelnetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_E,2),(_F,3)))
_SwL2DevCtrlTelnetState_Type.__name__=_B
_SwL2DevCtrlTelnetState_Object=MibScalar
swL2DevCtrlTelnetState=_SwL2DevCtrlTelnetState_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,14,1),_SwL2DevCtrlTelnetState_Type())
swL2DevCtrlTelnetState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlTelnetState.setStatus(_A)
class _SwL2DevCtrlTelnetTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2DevCtrlTelnetTcpPort_Type.__name__=_B
_SwL2DevCtrlTelnetTcpPort_Object=MibScalar
swL2DevCtrlTelnetTcpPort=_SwL2DevCtrlTelnetTcpPort_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,14,2),_SwL2DevCtrlTelnetTcpPort_Type())
swL2DevCtrlTelnetTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlTelnetTcpPort.setStatus(_A)
_SwL2DevCtrlManagementVlanId_Type=VlanId
_SwL2DevCtrlManagementVlanId_Object=MibScalar
swL2DevCtrlManagementVlanId=_SwL2DevCtrlManagementVlanId_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,16),_SwL2DevCtrlManagementVlanId_Type())
swL2DevCtrlManagementVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlManagementVlanId.setStatus(_A)
_SwL2DevCtrlWeb_ObjectIdentity=ObjectIdentity
swL2DevCtrlWeb=_SwL2DevCtrlWeb_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,1,2,17))
class _SwL2DevCtrlWebState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_SwL2DevCtrlWebState_Type.__name__=_B
_SwL2DevCtrlWebState_Object=MibScalar
swL2DevCtrlWebState=_SwL2DevCtrlWebState_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,17,1),_SwL2DevCtrlWebState_Type())
swL2DevCtrlWebState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlWebState.setStatus(_A)
class _SwL2DevCtrlWebTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2DevCtrlWebTcpPort_Type.__name__=_B
_SwL2DevCtrlWebTcpPort_Object=MibScalar
swL2DevCtrlWebTcpPort=_SwL2DevCtrlWebTcpPort_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,17,2),_SwL2DevCtrlWebTcpPort_Type())
swL2DevCtrlWebTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlWebTcpPort.setStatus(_A)
class _SwL2DevCtrlLLDPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_SwL2DevCtrlLLDPState_Type.__name__=_B
_SwL2DevCtrlLLDPState_Object=MibScalar
swL2DevCtrlLLDPState=_SwL2DevCtrlLLDPState_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,18),_SwL2DevCtrlLLDPState_Type())
swL2DevCtrlLLDPState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlLLDPState.setStatus(_A)
class _SwL2DevCtrlLLDPForwardMessageState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_SwL2DevCtrlLLDPForwardMessageState_Type.__name__=_B
_SwL2DevCtrlLLDPForwardMessageState_Object=MibScalar
swL2DevCtrlLLDPForwardMessageState=_SwL2DevCtrlLLDPForwardMessageState_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,19),_SwL2DevCtrlLLDPForwardMessageState_Type())
swL2DevCtrlLLDPForwardMessageState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlLLDPForwardMessageState.setStatus(_A)
class _SwL2DevCtrlIpAutoconfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_SwL2DevCtrlIpAutoconfig_Type.__name__=_B
_SwL2DevCtrlIpAutoconfig_Object=MibScalar
swL2DevCtrlIpAutoconfig=_SwL2DevCtrlIpAutoconfig_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,20),_SwL2DevCtrlIpAutoconfig_Type())
swL2DevCtrlIpAutoconfig.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlIpAutoconfig.setStatus(_A)
_SwL2DevCtrlCFM_ObjectIdentity=ObjectIdentity
swL2DevCtrlCFM=_SwL2DevCtrlCFM_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,1,2,21))
class _SwL2DevCtrlCFMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_SwL2DevCtrlCFMState_Type.__name__=_B
_SwL2DevCtrlCFMState_Object=MibScalar
swL2DevCtrlCFMState=_SwL2DevCtrlCFMState_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,21,1),_SwL2DevCtrlCFMState_Type())
swL2DevCtrlCFMState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlCFMState.setStatus(_A)
_SwL2DevCtrlCFMPortTable_Object=MibTable
swL2DevCtrlCFMPortTable=_SwL2DevCtrlCFMPortTable_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,21,2))
if mibBuilder.loadTexts:swL2DevCtrlCFMPortTable.setStatus(_A)
_SwL2DevCtrlCFMPortEntry_Object=MibTableRow
swL2DevCtrlCFMPortEntry=_SwL2DevCtrlCFMPortEntry_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,21,2,1))
swL2DevCtrlCFMPortEntry.setIndexNames((0,_G,_P))
if mibBuilder.loadTexts:swL2DevCtrlCFMPortEntry.setStatus(_A)
_SwL2DevCtrlCFMPortIndex_Type=Integer32
_SwL2DevCtrlCFMPortIndex_Object=MibTableColumn
swL2DevCtrlCFMPortIndex=_SwL2DevCtrlCFMPortIndex_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,21,2,1,1),_SwL2DevCtrlCFMPortIndex_Type())
swL2DevCtrlCFMPortIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:swL2DevCtrlCFMPortIndex.setStatus(_A)
class _SwL2DevCtrlCFMPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_SwL2DevCtrlCFMPortState_Type.__name__=_B
_SwL2DevCtrlCFMPortState_Object=MibTableColumn
swL2DevCtrlCFMPortState=_SwL2DevCtrlCFMPortState_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,2,21,2,1,2),_SwL2DevCtrlCFMPortState_Type())
swL2DevCtrlCFMPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlCFMPortState.setStatus(_A)
_SwL2DevAlarm_ObjectIdentity=ObjectIdentity
swL2DevAlarm=_SwL2DevAlarm_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,1,3))
class _SwL2DevAlarmNewRoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_E,2),(_F,3)))
_SwL2DevAlarmNewRoot_Type.__name__=_B
_SwL2DevAlarmNewRoot_Object=MibScalar
swL2DevAlarmNewRoot=_SwL2DevAlarmNewRoot_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,3,1),_SwL2DevAlarmNewRoot_Type())
swL2DevAlarmNewRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevAlarmNewRoot.setStatus(_A)
class _SwL2DevAlarmTopologyChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_E,2),(_F,3)))
_SwL2DevAlarmTopologyChange_Type.__name__=_B
_SwL2DevAlarmTopologyChange_Object=MibScalar
swL2DevAlarmTopologyChange=_SwL2DevAlarmTopologyChange_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,3,2),_SwL2DevAlarmTopologyChange_Type())
swL2DevAlarmTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevAlarmTopologyChange.setStatus(_A)
class _SwL2DevAlarmLinkChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_E,2),(_F,3)))
_SwL2DevAlarmLinkChange_Type.__name__=_B
_SwL2DevAlarmLinkChange_Object=MibScalar
swL2DevAlarmLinkChange=_SwL2DevAlarmLinkChange_Object((1,3,6,1,4,1,171,11,102,1,4,2,1,3,3),_SwL2DevAlarmLinkChange_Type())
swL2DevAlarmLinkChange.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevAlarmLinkChange.setStatus(_A)
_SwL2VLANMgmt_ObjectIdentity=ObjectIdentity
swL2VLANMgmt=_SwL2VLANMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,2))
_SwL2VlanStaticTable_Object=MibTable
swL2VlanStaticTable=_SwL2VlanStaticTable_Object((1,3,6,1,4,1,171,11,102,1,4,2,2,1))
if mibBuilder.loadTexts:swL2VlanStaticTable.setStatus(_A)
_SwL2VlanStaticEntry_Object=MibTableRow
swL2VlanStaticEntry=_SwL2VlanStaticEntry_Object((1,3,6,1,4,1,171,11,102,1,4,2,2,1,1))
swL2VlanStaticEntry.setIndexNames((0,_G,_R))
if mibBuilder.loadTexts:swL2VlanStaticEntry.setStatus(_A)
_SwL2VlanIndex_Type=VlanId
_SwL2VlanIndex_Object=MibTableColumn
swL2VlanIndex=_SwL2VlanIndex_Object((1,3,6,1,4,1,171,11,102,1,4,2,2,1,1,1),_SwL2VlanIndex_Type())
swL2VlanIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:swL2VlanIndex.setStatus(_A)
class _SwL2VLANAdvertisement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_SwL2VLANAdvertisement_Type.__name__=_B
_SwL2VLANAdvertisement_Object=MibTableColumn
swL2VLANAdvertisement=_SwL2VLANAdvertisement_Object((1,3,6,1,4,1,171,11,102,1,4,2,2,1,1,2),_SwL2VLANAdvertisement_Type())
swL2VLANAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VLANAdvertisement.setStatus(_A)
class _SwL2PVIDAutoAssignmentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_SwL2PVIDAutoAssignmentState_Type.__name__=_B
_SwL2PVIDAutoAssignmentState_Object=MibScalar
swL2PVIDAutoAssignmentState=_SwL2PVIDAutoAssignmentState_Object((1,3,6,1,4,1,171,11,102,1,4,2,2,2),_SwL2PVIDAutoAssignmentState_Type())
swL2PVIDAutoAssignmentState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PVIDAutoAssignmentState.setStatus(_A)
_SwL2VlanPortInfoTable_Object=MibTable
swL2VlanPortInfoTable=_SwL2VlanPortInfoTable_Object((1,3,6,1,4,1,171,11,102,1,4,2,2,3))
if mibBuilder.loadTexts:swL2VlanPortInfoTable.setStatus(_A)
_SwL2VlanPortInfoEntry_Object=MibTableRow
swL2VlanPortInfoEntry=_SwL2VlanPortInfoEntry_Object((1,3,6,1,4,1,171,11,102,1,4,2,2,3,1))
swL2VlanPortInfoEntry.setIndexNames((0,_G,_S),(0,_G,_T))
if mibBuilder.loadTexts:swL2VlanPortInfoEntry.setStatus(_A)
class _SwL2VlanPortInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2VlanPortInfoPortIndex_Type.__name__=_B
_SwL2VlanPortInfoPortIndex_Object=MibTableColumn
swL2VlanPortInfoPortIndex=_SwL2VlanPortInfoPortIndex_Object((1,3,6,1,4,1,171,11,102,1,4,2,2,3,1,1),_SwL2VlanPortInfoPortIndex_Type())
swL2VlanPortInfoPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanPortInfoPortIndex.setStatus(_A)
class _SwL2VlanPortInfoVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2VlanPortInfoVid_Type.__name__=_B
_SwL2VlanPortInfoVid_Object=MibTableColumn
swL2VlanPortInfoVid=_SwL2VlanPortInfoVid_Object((1,3,6,1,4,1,171,11,102,1,4,2,2,3,1,2),_SwL2VlanPortInfoVid_Type())
swL2VlanPortInfoVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanPortInfoVid.setStatus(_A)
class _SwL2VlanPortInfoPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),('untagged',2),('tagged',3),('dynamic',4),('forbidden',5)))
_SwL2VlanPortInfoPortRole_Type.__name__=_B
_SwL2VlanPortInfoPortRole_Object=MibTableColumn
swL2VlanPortInfoPortRole=_SwL2VlanPortInfoPortRole_Object((1,3,6,1,4,1,171,11,102,1,4,2,2,3,1,3),_SwL2VlanPortInfoPortRole_Type())
swL2VlanPortInfoPortRole.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanPortInfoPortRole.setStatus(_A)
class _SwL2NniGvrpBpduAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot1d',1),('dot1ad',2)))
_SwL2NniGvrpBpduAddress_Type.__name__=_B
_SwL2NniGvrpBpduAddress_Object=MibScalar
swL2NniGvrpBpduAddress=_SwL2NniGvrpBpduAddress_Object((1,3,6,1,4,1,171,11,102,1,4,2,2,7),_SwL2NniGvrpBpduAddress_Type())
swL2NniGvrpBpduAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2NniGvrpBpduAddress.setStatus(_A)
_SwL2PortMgmt_ObjectIdentity=ObjectIdentity
swL2PortMgmt=_SwL2PortMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,3))
_SwL2PortInfoTable_Object=MibTable
swL2PortInfoTable=_SwL2PortInfoTable_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,1))
if mibBuilder.loadTexts:swL2PortInfoTable.setStatus(_A)
_SwL2PortInfoEntry_Object=MibTableRow
swL2PortInfoEntry=_SwL2PortInfoEntry_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,1,1))
swL2PortInfoEntry.setIndexNames((0,_G,_U),(0,_G,_V))
if mibBuilder.loadTexts:swL2PortInfoEntry.setStatus(_A)
class _SwL2PortInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortInfoPortIndex_Type.__name__=_B
_SwL2PortInfoPortIndex_Object=MibTableColumn
swL2PortInfoPortIndex=_SwL2PortInfoPortIndex_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,1,1,1),_SwL2PortInfoPortIndex_Type())
swL2PortInfoPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoPortIndex.setStatus(_A)
class _SwL2PortInfoMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),('fiber',2)))
_SwL2PortInfoMediumType_Type.__name__=_B
_SwL2PortInfoMediumType_Object=MibTableColumn
swL2PortInfoMediumType=_SwL2PortInfoMediumType_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,1,1,2),_SwL2PortInfoMediumType_Type())
swL2PortInfoMediumType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoMediumType.setStatus(_A)
class _SwL2PortInfoUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortInfoUnitID_Type.__name__=_B
_SwL2PortInfoUnitID_Object=MibTableColumn
swL2PortInfoUnitID=_SwL2PortInfoUnitID_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,1,1,3),_SwL2PortInfoUnitID_Type())
swL2PortInfoUnitID.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoUnitID.setStatus(_A)
class _SwL2PortInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('portType-none',0),('portType-100Base-T',2),('portType-100Base-X',3),('portType-1000Base-T',4),('portType-1000Base-X',5),('portType-10GBase-R',6),('portType-10GBase-CX4',7),('portType-SIO',8),('portType-module-empty',9),('portType-user-last',10)))
_SwL2PortInfoType_Type.__name__=_B
_SwL2PortInfoType_Object=MibTableColumn
swL2PortInfoType=_SwL2PortInfoType_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,1,1,4),_SwL2PortInfoType_Type())
swL2PortInfoType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoType.setStatus(_A)
class _SwL2PortInfoLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('link-pass',2),('link-fail',3)))
_SwL2PortInfoLinkStatus_Type.__name__=_B
_SwL2PortInfoLinkStatus_Object=MibTableColumn
swL2PortInfoLinkStatus=_SwL2PortInfoLinkStatus_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,1,1,5),_SwL2PortInfoLinkStatus_Type())
swL2PortInfoLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoLinkStatus.setStatus(_A)
class _SwL2PortInfoNwayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('link-down',0),('full-10Mbps-8023x',1),('full-10Mbps-none',2),('half-10Mbps-backp',3),('half-10Mbps-none',4),('full-100Mbps-8023x',5),('full-100Mbps-none',6),('half-100Mbps-backp',7),('half-100Mbps-none',8),('full-1Gigabps-8023x',9),('full-1Gigabps-none',10),('half-1Gigabps-backp',11),('half-1Gigabps-none',12),('full-10Gigabps-8023x',13),('full-10Gigabps-none',14),('half-10Gigabps-8023x',15),('half-10Gigabps-none',16),('empty',17),(_X,18)))
_SwL2PortInfoNwayStatus_Type.__name__=_B
_SwL2PortInfoNwayStatus_Object=MibTableColumn
swL2PortInfoNwayStatus=_SwL2PortInfoNwayStatus_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,1,1,6),_SwL2PortInfoNwayStatus_Type())
swL2PortInfoNwayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoNwayStatus.setStatus(_A)
class _SwL2PortInfoErrorDisabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,4,5)));namedValues=NamedValues(*((_J,0),('storm',1),('unknow',3),(_Y,4),('ddm',5)))
_SwL2PortInfoErrorDisabled_Type.__name__=_B
_SwL2PortInfoErrorDisabled_Object=MibTableColumn
swL2PortInfoErrorDisabled=_SwL2PortInfoErrorDisabled_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,1,1,8),_SwL2PortInfoErrorDisabled_Type())
swL2PortInfoErrorDisabled.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoErrorDisabled.setStatus(_A)
_SwL2PortCtrlTable_Object=MibTable
swL2PortCtrlTable=_SwL2PortCtrlTable_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,2))
if mibBuilder.loadTexts:swL2PortCtrlTable.setStatus(_A)
_SwL2PortCtrlEntry_Object=MibTableRow
swL2PortCtrlEntry=_SwL2PortCtrlEntry_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,2,1))
swL2PortCtrlEntry.setIndexNames((0,_G,_Z),(0,_G,_a))
if mibBuilder.loadTexts:swL2PortCtrlEntry.setStatus(_A)
class _SwL2PortCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortCtrlPortIndex_Type.__name__=_B
_SwL2PortCtrlPortIndex_Object=MibTableColumn
swL2PortCtrlPortIndex=_SwL2PortCtrlPortIndex_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,2,1,1),_SwL2PortCtrlPortIndex_Type())
swL2PortCtrlPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlPortIndex.setStatus(_A)
class _SwL2PortCtrlMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),('fiber',2)))
_SwL2PortCtrlMediumType_Type.__name__=_B
_SwL2PortCtrlMediumType_Object=MibTableColumn
swL2PortCtrlMediumType=_SwL2PortCtrlMediumType_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,2,1,2),_SwL2PortCtrlMediumType_Type())
swL2PortCtrlMediumType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlMediumType.setStatus(_A)
class _SwL2PortCtrlUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortCtrlUnitIndex_Type.__name__=_B
_SwL2PortCtrlUnitIndex_Object=MibTableColumn
swL2PortCtrlUnitIndex=_SwL2PortCtrlUnitIndex_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,2,1,3),_SwL2PortCtrlUnitIndex_Type())
swL2PortCtrlUnitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlUnitIndex.setStatus(_A)
class _SwL2PortCtrlAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_E,2),(_F,3)))
_SwL2PortCtrlAdminState_Type.__name__=_B
_SwL2PortCtrlAdminState_Object=MibTableColumn
swL2PortCtrlAdminState=_SwL2PortCtrlAdminState_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,2,1,4),_SwL2PortCtrlAdminState_Type())
swL2PortCtrlAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlAdminState.setStatus(_A)
class _SwL2PortCtrlNwayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_H,1),('nway-enabled',2),('nway-disabled-10Mbps-Half',3),('nway-disabled-10Mbps-Full',4),('nway-disabled-100Mbps-Half',5),('nway-disabled-100Mbps-Full',6),('nway-disabled-1Gigabps-Half',7),('nway-disabled-1Gigabps-Full',8),('nway-disabled-1Gigabps-Full-master',9),('nway-disabled-1Gigabps-Full-slave',10)))
_SwL2PortCtrlNwayState_Type.__name__=_B
_SwL2PortCtrlNwayState_Object=MibTableColumn
swL2PortCtrlNwayState=_SwL2PortCtrlNwayState_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,2,1,5),_SwL2PortCtrlNwayState_Type())
swL2PortCtrlNwayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlNwayState.setStatus(_A)
class _SwL2PortCtrlFlowCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_E,2),(_F,3)))
_SwL2PortCtrlFlowCtrlState_Type.__name__=_B
_SwL2PortCtrlFlowCtrlState_Object=MibTableColumn
swL2PortCtrlFlowCtrlState=_SwL2PortCtrlFlowCtrlState_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,2,1,6),_SwL2PortCtrlFlowCtrlState_Type())
swL2PortCtrlFlowCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlFlowCtrlState.setStatus(_A)
class _SwL2PortCtrlLearningState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_E,2),(_F,3)))
_SwL2PortCtrlLearningState_Type.__name__=_B
_SwL2PortCtrlLearningState_Object=MibTableColumn
swL2PortCtrlLearningState=_SwL2PortCtrlLearningState_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,2,1,7),_SwL2PortCtrlLearningState_Type())
swL2PortCtrlLearningState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlLearningState.setStatus(_A)
class _SwL2PortCtrlMACNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_E,2),(_F,3)))
_SwL2PortCtrlMACNotifyState_Type.__name__=_B
_SwL2PortCtrlMACNotifyState_Object=MibTableColumn
swL2PortCtrlMACNotifyState=_SwL2PortCtrlMACNotifyState_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,2,1,8),_SwL2PortCtrlMACNotifyState_Type())
swL2PortCtrlMACNotifyState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlMACNotifyState.setStatus(_A)
class _SwL2PortCtrlMDIXState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),(_M,2),('cross',3)))
_SwL2PortCtrlMDIXState_Type.__name__=_B
_SwL2PortCtrlMDIXState_Object=MibTableColumn
swL2PortCtrlMDIXState=_SwL2PortCtrlMDIXState_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,2,1,10),_SwL2PortCtrlMDIXState_Type())
swL2PortCtrlMDIXState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlMDIXState.setStatus(_A)
class _SwL2PortCtrlJumboFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_E,2),(_F,3)))
_SwL2PortCtrlJumboFrame_Type.__name__=_B
_SwL2PortCtrlJumboFrame_Object=MibScalar
swL2PortCtrlJumboFrame=_SwL2PortCtrlJumboFrame_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,3),_SwL2PortCtrlJumboFrame_Type())
swL2PortCtrlJumboFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlJumboFrame.setStatus(_A)
_SwL2PortCtrlJumboFrameMaxSize_Type=Integer32
_SwL2PortCtrlJumboFrameMaxSize_Object=MibScalar
swL2PortCtrlJumboFrameMaxSize=_SwL2PortCtrlJumboFrameMaxSize_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,4),_SwL2PortCtrlJumboFrameMaxSize_Type())
swL2PortCtrlJumboFrameMaxSize.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlJumboFrameMaxSize.setStatus(_A)
_SwL2PortCounterCtrlTable_Object=MibTable
swL2PortCounterCtrlTable=_SwL2PortCounterCtrlTable_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,6))
if mibBuilder.loadTexts:swL2PortCounterCtrlTable.setStatus(_A)
_SwL2PortCounterCtrlEntry_Object=MibTableRow
swL2PortCounterCtrlEntry=_SwL2PortCounterCtrlEntry_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,6,1))
swL2PortCounterCtrlEntry.setIndexNames((0,_G,_b))
if mibBuilder.loadTexts:swL2PortCounterCtrlEntry.setStatus(_A)
class _SwL2PortCounterCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortCounterCtrlPortIndex_Type.__name__=_B
_SwL2PortCounterCtrlPortIndex_Object=MibTableColumn
swL2PortCounterCtrlPortIndex=_SwL2PortCounterCtrlPortIndex_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,6,1,1),_SwL2PortCounterCtrlPortIndex_Type())
swL2PortCounterCtrlPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCounterCtrlPortIndex.setStatus(_A)
class _SwL2PortCounterClearCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('start',2)))
_SwL2PortCounterClearCtrl_Type.__name__=_B
_SwL2PortCounterClearCtrl_Object=MibTableColumn
swL2PortCounterClearCtrl=_SwL2PortCounterClearCtrl_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,6,1,2),_SwL2PortCounterClearCtrl_Type())
swL2PortCounterClearCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCounterClearCtrl.setStatus(_A)
_SwL2PortErrTable_Object=MibTable
swL2PortErrTable=_SwL2PortErrTable_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,7))
if mibBuilder.loadTexts:swL2PortErrTable.setStatus(_A)
_SwL2PortErrEntry_Object=MibTableRow
swL2PortErrEntry=_SwL2PortErrEntry_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,7,1))
swL2PortErrEntry.setIndexNames((0,_G,_c))
if mibBuilder.loadTexts:swL2PortErrEntry.setStatus(_A)
class _SwL2PortErrPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortErrPortIndex_Type.__name__=_B
_SwL2PortErrPortIndex_Object=MibTableColumn
swL2PortErrPortIndex=_SwL2PortErrPortIndex_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,7,1,1),_SwL2PortErrPortIndex_Type())
swL2PortErrPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortIndex.setStatus(_A)
class _SwL2PortErrPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_SwL2PortErrPortState_Type.__name__=_B
_SwL2PortErrPortState_Object=MibTableColumn
swL2PortErrPortState=_SwL2PortErrPortState_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,7,1,2),_SwL2PortErrPortState_Type())
swL2PortErrPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortState.setStatus(_A)
class _SwL2PortErrPortConnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_X,2)))
_SwL2PortErrPortConnStatus_Type.__name__=_B
_SwL2PortErrPortConnStatus_Object=MibTableColumn
swL2PortErrPortConnStatus=_SwL2PortErrPortConnStatus_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,7,1,3),_SwL2PortErrPortConnStatus_Type())
swL2PortErrPortConnStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortConnStatus.setStatus(_A)
class _SwL2PortErrPortReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('storm-control',2),(_Y,3),('ddm',4)))
_SwL2PortErrPortReason_Type.__name__=_B
_SwL2PortErrPortReason_Object=MibTableColumn
swL2PortErrPortReason=_SwL2PortErrPortReason_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,7,1,4),_SwL2PortErrPortReason_Type())
swL2PortErrPortReason.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortReason.setStatus(_A)
_SwL2PortDropCounterTable_Object=MibTable
swL2PortDropCounterTable=_SwL2PortDropCounterTable_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,9))
if mibBuilder.loadTexts:swL2PortDropCounterTable.setStatus(_A)
_SwL2PortDropCounterEntry_Object=MibTableRow
swL2PortDropCounterEntry=_SwL2PortDropCounterEntry_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,9,1))
swL2PortDropCounterEntry.setIndexNames((0,_G,_d))
if mibBuilder.loadTexts:swL2PortDropCounterEntry.setStatus(_A)
class _SwL2PortDropCounterPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortDropCounterPortIndex_Type.__name__=_B
_SwL2PortDropCounterPortIndex_Object=MibTableColumn
swL2PortDropCounterPortIndex=_SwL2PortDropCounterPortIndex_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,9,1,1),_SwL2PortDropCounterPortIndex_Type())
swL2PortDropCounterPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortDropCounterPortIndex.setStatus(_A)
_SwL2PortIngressBandwidthControlDrops_Type=Counter32
_SwL2PortIngressBandwidthControlDrops_Object=MibTableColumn
swL2PortIngressBandwidthControlDrops=_SwL2PortIngressBandwidthControlDrops_Object((1,3,6,1,4,1,171,11,102,1,4,2,3,9,1,6),_SwL2PortIngressBandwidthControlDrops_Type())
swL2PortIngressBandwidthControlDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortIngressBandwidthControlDrops.setStatus(_A)
_SwL2DhcpRelayMgmt_ObjectIdentity=ObjectIdentity
swL2DhcpRelayMgmt=_SwL2DhcpRelayMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,8))
_SwL2TrunkMgmt_ObjectIdentity=ObjectIdentity
swL2TrunkMgmt=_SwL2TrunkMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,9))
class _SwL2TrunkMaxSupportedEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkMaxSupportedEntries_Type.__name__=_B
_SwL2TrunkMaxSupportedEntries_Object=MibScalar
swL2TrunkMaxSupportedEntries=_SwL2TrunkMaxSupportedEntries_Object((1,3,6,1,4,1,171,11,102,1,4,2,9,1),_SwL2TrunkMaxSupportedEntries_Type())
swL2TrunkMaxSupportedEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkMaxSupportedEntries.setStatus(_A)
class _SwL2TrunkCurrentNumEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkCurrentNumEntries_Type.__name__=_B
_SwL2TrunkCurrentNumEntries_Object=MibScalar
swL2TrunkCurrentNumEntries=_SwL2TrunkCurrentNumEntries_Object((1,3,6,1,4,1,171,11,102,1,4,2,9,2),_SwL2TrunkCurrentNumEntries_Type())
swL2TrunkCurrentNumEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkCurrentNumEntries.setStatus(_A)
_SwL2TrunkCtrlTable_Object=MibTable
swL2TrunkCtrlTable=_SwL2TrunkCtrlTable_Object((1,3,6,1,4,1,171,11,102,1,4,2,9,3))
if mibBuilder.loadTexts:swL2TrunkCtrlTable.setStatus(_A)
_SwL2TrunkCtrlEntry_Object=MibTableRow
swL2TrunkCtrlEntry=_SwL2TrunkCtrlEntry_Object((1,3,6,1,4,1,171,11,102,1,4,2,9,3,1))
swL2TrunkCtrlEntry.setIndexNames((0,_G,_e))
if mibBuilder.loadTexts:swL2TrunkCtrlEntry.setStatus(_A)
class _SwL2TrunkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkIndex_Type.__name__=_B
_SwL2TrunkIndex_Object=MibTableColumn
swL2TrunkIndex=_SwL2TrunkIndex_Object((1,3,6,1,4,1,171,11,102,1,4,2,9,3,1,1),_SwL2TrunkIndex_Type())
swL2TrunkIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkIndex.setStatus(_A)
class _SwL2TrunkMasterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2TrunkMasterPort_Type.__name__=_B
_SwL2TrunkMasterPort_Object=MibTableColumn
swL2TrunkMasterPort=_SwL2TrunkMasterPort_Object((1,3,6,1,4,1,171,11,102,1,4,2,9,3,1,3),_SwL2TrunkMasterPort_Type())
swL2TrunkMasterPort.setMaxAccess(_K)
if mibBuilder.loadTexts:swL2TrunkMasterPort.setStatus(_A)
_SwL2TrunkMember_Type=PortList
_SwL2TrunkMember_Object=MibTableColumn
swL2TrunkMember=_SwL2TrunkMember_Object((1,3,6,1,4,1,171,11,102,1,4,2,9,3,1,4),_SwL2TrunkMember_Type())
swL2TrunkMember.setMaxAccess(_K)
if mibBuilder.loadTexts:swL2TrunkMember.setStatus(_A)
class _SwL2TrunkFloodingPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2TrunkFloodingPort_Type.__name__=_B
_SwL2TrunkFloodingPort_Object=MibTableColumn
swL2TrunkFloodingPort=_SwL2TrunkFloodingPort_Object((1,3,6,1,4,1,171,11,102,1,4,2,9,3,1,5),_SwL2TrunkFloodingPort_Type())
swL2TrunkFloodingPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkFloodingPort.setStatus(_A)
class _SwL2TrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('static',2),('lacp',3)))
_SwL2TrunkType_Type.__name__=_B
_SwL2TrunkType_Object=MibTableColumn
swL2TrunkType=_SwL2TrunkType_Object((1,3,6,1,4,1,171,11,102,1,4,2,9,3,1,6),_SwL2TrunkType_Type())
swL2TrunkType.setMaxAccess(_K)
if mibBuilder.loadTexts:swL2TrunkType.setStatus(_A)
_SwL2TrunkState_Type=RowStatus
_SwL2TrunkState_Object=MibTableColumn
swL2TrunkState=_SwL2TrunkState_Object((1,3,6,1,4,1,171,11,102,1,4,2,9,3,1,7),_SwL2TrunkState_Type())
swL2TrunkState.setMaxAccess(_K)
if mibBuilder.loadTexts:swL2TrunkState.setStatus(_A)
class _SwL2TrunkAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_H,1),('mac-source',2),('mac-destination',3),('mac-source-dest',4),('ip-source',5),('ip-destination',6),('ip-source-dest',7)))
_SwL2TrunkAlgorithm_Type.__name__=_B
_SwL2TrunkAlgorithm_Object=MibScalar
swL2TrunkAlgorithm=_SwL2TrunkAlgorithm_Object((1,3,6,1,4,1,171,11,102,1,4,2,9,4),_SwL2TrunkAlgorithm_Type())
swL2TrunkAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkAlgorithm.setStatus(_A)
_SwL2TrunkLACPPortTable_Object=MibTable
swL2TrunkLACPPortTable=_SwL2TrunkLACPPortTable_Object((1,3,6,1,4,1,171,11,102,1,4,2,9,5))
if mibBuilder.loadTexts:swL2TrunkLACPPortTable.setStatus(_A)
_SwL2TrunkLACPPortEntry_Object=MibTableRow
swL2TrunkLACPPortEntry=_SwL2TrunkLACPPortEntry_Object((1,3,6,1,4,1,171,11,102,1,4,2,9,5,1))
swL2TrunkLACPPortEntry.setIndexNames((0,_G,_f))
if mibBuilder.loadTexts:swL2TrunkLACPPortEntry.setStatus(_A)
class _SwL2TrunkLACPPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkLACPPortIndex_Type.__name__=_B
_SwL2TrunkLACPPortIndex_Object=MibTableColumn
swL2TrunkLACPPortIndex=_SwL2TrunkLACPPortIndex_Object((1,3,6,1,4,1,171,11,102,1,4,2,9,5,1,1),_SwL2TrunkLACPPortIndex_Type())
swL2TrunkLACPPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkLACPPortIndex.setStatus(_A)
class _SwL2TrunkLACPPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),('passive',2)))
_SwL2TrunkLACPPortState_Type.__name__=_B
_SwL2TrunkLACPPortState_Object=MibTableColumn
swL2TrunkLACPPortState=_SwL2TrunkLACPPortState_Object((1,3,6,1,4,1,171,11,102,1,4,2,9,5,1,2),_SwL2TrunkLACPPortState_Type())
swL2TrunkLACPPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkLACPPortState.setStatus(_A)
_SwL2MirrorMgmt_ObjectIdentity=ObjectIdentity
swL2MirrorMgmt=_SwL2MirrorMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,10))
class _SwL2MirrorLogicTargetPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2MirrorLogicTargetPort_Type.__name__=_B
_SwL2MirrorLogicTargetPort_Object=MibScalar
swL2MirrorLogicTargetPort=_SwL2MirrorLogicTargetPort_Object((1,3,6,1,4,1,171,11,102,1,4,2,10,1),_SwL2MirrorLogicTargetPort_Type())
swL2MirrorLogicTargetPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MirrorLogicTargetPort.setStatus(_A)
_SwL2MirrorPortSourceIngress_Type=PortList
_SwL2MirrorPortSourceIngress_Object=MibScalar
swL2MirrorPortSourceIngress=_SwL2MirrorPortSourceIngress_Object((1,3,6,1,4,1,171,11,102,1,4,2,10,2),_SwL2MirrorPortSourceIngress_Type())
swL2MirrorPortSourceIngress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MirrorPortSourceIngress.setStatus(_A)
_SwL2MirrorPortSourceEgress_Type=PortList
_SwL2MirrorPortSourceEgress_Object=MibScalar
swL2MirrorPortSourceEgress=_SwL2MirrorPortSourceEgress_Object((1,3,6,1,4,1,171,11,102,1,4,2,10,3),_SwL2MirrorPortSourceEgress_Type())
swL2MirrorPortSourceEgress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MirrorPortSourceEgress.setStatus(_A)
class _SwL2MirrorPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_E,2),(_F,3)))
_SwL2MirrorPortState_Type.__name__=_B
_SwL2MirrorPortState_Object=MibScalar
swL2MirrorPortState=_SwL2MirrorPortState_Object((1,3,6,1,4,1,171,11,102,1,4,2,10,4),_SwL2MirrorPortState_Type())
swL2MirrorPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MirrorPortState.setStatus(_A)
_SwL2TrafficSegMgmt_ObjectIdentity=ObjectIdentity
swL2TrafficSegMgmt=_SwL2TrafficSegMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,14))
_SwL2TrafficSegTable_Object=MibTable
swL2TrafficSegTable=_SwL2TrafficSegTable_Object((1,3,6,1,4,1,171,11,102,1,4,2,14,1))
if mibBuilder.loadTexts:swL2TrafficSegTable.setStatus(_A)
_SwL2TrafficSegEntry_Object=MibTableRow
swL2TrafficSegEntry=_SwL2TrafficSegEntry_Object((1,3,6,1,4,1,171,11,102,1,4,2,14,1,1))
swL2TrafficSegEntry.setIndexNames((0,_G,_g))
if mibBuilder.loadTexts:swL2TrafficSegEntry.setStatus(_A)
class _SwL2TrafficSegPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrafficSegPort_Type.__name__=_B
_SwL2TrafficSegPort_Object=MibTableColumn
swL2TrafficSegPort=_SwL2TrafficSegPort_Object((1,3,6,1,4,1,171,11,102,1,4,2,14,1,1,1),_SwL2TrafficSegPort_Type())
swL2TrafficSegPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrafficSegPort.setStatus(_A)
_SwL2TrafficSegForwardPorts_Type=PortList
_SwL2TrafficSegForwardPorts_Object=MibTableColumn
swL2TrafficSegForwardPorts=_SwL2TrafficSegForwardPorts_Object((1,3,6,1,4,1,171,11,102,1,4,2,14,1,1,2),_SwL2TrafficSegForwardPorts_Type())
swL2TrafficSegForwardPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrafficSegForwardPorts.setStatus(_A)
_SwL2MulticastFilterMode_ObjectIdentity=ObjectIdentity
swL2MulticastFilterMode=_SwL2MulticastFilterMode_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,17))
_SwL2MulticastFilterModeVlanTable_Object=MibTable
swL2MulticastFilterModeVlanTable=_SwL2MulticastFilterModeVlanTable_Object((1,3,6,1,4,1,171,11,102,1,4,2,17,1))
if mibBuilder.loadTexts:swL2MulticastFilterModeVlanTable.setStatus(_A)
_SwL2MulticastFilterModeVlanEntry_Object=MibTableRow
swL2MulticastFilterModeVlanEntry=_SwL2MulticastFilterModeVlanEntry_Object((1,3,6,1,4,1,171,11,102,1,4,2,17,1,1))
swL2MulticastFilterModeVlanEntry.setIndexNames((0,_G,_h))
if mibBuilder.loadTexts:swL2MulticastFilterModeVlanEntry.setStatus(_A)
class _SwL2MulticastFilterVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2MulticastFilterVid_Type.__name__=_B
_SwL2MulticastFilterVid_Object=MibTableColumn
swL2MulticastFilterVid=_SwL2MulticastFilterVid_Object((1,3,6,1,4,1,171,11,102,1,4,2,17,1,1,1),_SwL2MulticastFilterVid_Type())
swL2MulticastFilterVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MulticastFilterVid.setStatus(_A)
class _SwL2MulticastFilterVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forward-all-groups',1),('forward-unregistered-groups',2),('filter-unregistered-groups',3)))
_SwL2MulticastFilterVlanMode_Type.__name__=_B
_SwL2MulticastFilterVlanMode_Object=MibTableColumn
swL2MulticastFilterVlanMode=_SwL2MulticastFilterVlanMode_Object((1,3,6,1,4,1,171,11,102,1,4,2,17,1,1,2),_SwL2MulticastFilterVlanMode_Type())
swL2MulticastFilterVlanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MulticastFilterVlanMode.setStatus(_A)
_SwL2LoopDetectMgmt_ObjectIdentity=ObjectIdentity
swL2LoopDetectMgmt=_SwL2LoopDetectMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,18))
_SwL2LoopDetectCtrl_ObjectIdentity=ObjectIdentity
swL2LoopDetectCtrl=_SwL2LoopDetectCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,18,1))
class _SwL2LoopDetectAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_SwL2LoopDetectAdminState_Type.__name__=_B
_SwL2LoopDetectAdminState_Object=MibScalar
swL2LoopDetectAdminState=_SwL2LoopDetectAdminState_Object((1,3,6,1,4,1,171,11,102,1,4,2,18,1,1),_SwL2LoopDetectAdminState_Type())
swL2LoopDetectAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectAdminState.setStatus(_A)
class _SwL2LoopDetectInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_SwL2LoopDetectInterval_Type.__name__=_B
_SwL2LoopDetectInterval_Object=MibScalar
swL2LoopDetectInterval=_SwL2LoopDetectInterval_Object((1,3,6,1,4,1,171,11,102,1,4,2,18,1,2),_SwL2LoopDetectInterval_Type())
swL2LoopDetectInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectInterval.setStatus(_A)
class _SwL2LoopDetectRecoverTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_SwL2LoopDetectRecoverTime_Type.__name__=_B
_SwL2LoopDetectRecoverTime_Object=MibScalar
swL2LoopDetectRecoverTime=_SwL2LoopDetectRecoverTime_Object((1,3,6,1,4,1,171,11,102,1,4,2,18,1,3),_SwL2LoopDetectRecoverTime_Type())
swL2LoopDetectRecoverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectRecoverTime.setStatus(_A)
class _SwL2LoopDetectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan-based',1),('port-based',2)))
_SwL2LoopDetectMode_Type.__name__=_B
_SwL2LoopDetectMode_Object=MibScalar
swL2LoopDetectMode=_SwL2LoopDetectMode_Object((1,3,6,1,4,1,171,11,102,1,4,2,18,1,4),_SwL2LoopDetectMode_Type())
swL2LoopDetectMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectMode.setStatus(_A)
class _SwL2LoopDetectTrapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('loop-detected',2),('loop-cleared',3),('both',4)))
_SwL2LoopDetectTrapMode_Type.__name__=_B
_SwL2LoopDetectTrapMode_Object=MibScalar
swL2LoopDetectTrapMode=_SwL2LoopDetectTrapMode_Object((1,3,6,1,4,1,171,11,102,1,4,2,18,1,5),_SwL2LoopDetectTrapMode_Type())
swL2LoopDetectTrapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectTrapMode.setStatus(_A)
_SwL2LoopDetectPortMgmt_ObjectIdentity=ObjectIdentity
swL2LoopDetectPortMgmt=_SwL2LoopDetectPortMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,18,2))
_SwL2LoopDetectPortTable_Object=MibTable
swL2LoopDetectPortTable=_SwL2LoopDetectPortTable_Object((1,3,6,1,4,1,171,11,102,1,4,2,18,2,1))
if mibBuilder.loadTexts:swL2LoopDetectPortTable.setStatus(_A)
_SwL2LoopDetectPortEntry_Object=MibTableRow
swL2LoopDetectPortEntry=_SwL2LoopDetectPortEntry_Object((1,3,6,1,4,1,171,11,102,1,4,2,18,2,1,1))
swL2LoopDetectPortEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:swL2LoopDetectPortEntry.setStatus(_A)
class _SwL2LoopDetectPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2LoopDetectPortIndex_Type.__name__=_B
_SwL2LoopDetectPortIndex_Object=MibTableColumn
swL2LoopDetectPortIndex=_SwL2LoopDetectPortIndex_Object((1,3,6,1,4,1,171,11,102,1,4,2,18,2,1,1,1),_SwL2LoopDetectPortIndex_Type())
swL2LoopDetectPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectPortIndex.setStatus(_A)
class _SwL2LoopDetectPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_SwL2LoopDetectPortState_Type.__name__=_B
_SwL2LoopDetectPortState_Object=MibTableColumn
swL2LoopDetectPortState=_SwL2LoopDetectPortState_Object((1,3,6,1,4,1,171,11,102,1,4,2,18,2,1,1,2),_SwL2LoopDetectPortState_Type())
swL2LoopDetectPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectPortState.setStatus(_A)
_SwL2LoopDetectPortLoopVLAN_Type=DisplayString
_SwL2LoopDetectPortLoopVLAN_Object=MibTableColumn
swL2LoopDetectPortLoopVLAN=_SwL2LoopDetectPortLoopVLAN_Object((1,3,6,1,4,1,171,11,102,1,4,2,18,2,1,1,3),_SwL2LoopDetectPortLoopVLAN_Type())
swL2LoopDetectPortLoopVLAN.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectPortLoopVLAN.setStatus(_A)
class _SwL2LoopDetectPortLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),('loop',2),('error',3),(_J,4)))
_SwL2LoopDetectPortLoopStatus_Type.__name__=_B
_SwL2LoopDetectPortLoopStatus_Object=MibTableColumn
swL2LoopDetectPortLoopStatus=_SwL2LoopDetectPortLoopStatus_Object((1,3,6,1,4,1,171,11,102,1,4,2,18,2,1,1,4),_SwL2LoopDetectPortLoopStatus_Type())
swL2LoopDetectPortLoopStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectPortLoopStatus.setStatus(_A)
_SwL2DhcpLocalRelayMgmt_ObjectIdentity=ObjectIdentity
swL2DhcpLocalRelayMgmt=_SwL2DhcpLocalRelayMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,24))
class _SwL2DhcpLocalRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_E,2),(_F,3)))
_SwL2DhcpLocalRelayState_Type.__name__=_B
_SwL2DhcpLocalRelayState_Object=MibScalar
swL2DhcpLocalRelayState=_SwL2DhcpLocalRelayState_Object((1,3,6,1,4,1,171,11,102,1,4,2,24,1),_SwL2DhcpLocalRelayState_Type())
swL2DhcpLocalRelayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpLocalRelayState.setStatus(_A)
_SwL2DhcpLocalRelayVLANTable_Object=MibTable
swL2DhcpLocalRelayVLANTable=_SwL2DhcpLocalRelayVLANTable_Object((1,3,6,1,4,1,171,11,102,1,4,2,24,2))
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANTable.setStatus(_A)
_SwL2DhcpLocalRelayVLANEntry_Object=MibTableRow
swL2DhcpLocalRelayVLANEntry=_SwL2DhcpLocalRelayVLANEntry_Object((1,3,6,1,4,1,171,11,102,1,4,2,24,2,1))
swL2DhcpLocalRelayVLANEntry.setIndexNames((0,_G,_i))
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANEntry.setStatus(_A)
class _SwL2DhcpLocalRelayVLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2DhcpLocalRelayVLANID_Type.__name__=_B
_SwL2DhcpLocalRelayVLANID_Object=MibTableColumn
swL2DhcpLocalRelayVLANID=_SwL2DhcpLocalRelayVLANID_Object((1,3,6,1,4,1,171,11,102,1,4,2,24,2,1,1),_SwL2DhcpLocalRelayVLANID_Type())
swL2DhcpLocalRelayVLANID.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANID.setStatus(_A)
class _SwL2DhcpLocalRelayVLANState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_E,2),(_F,3)))
_SwL2DhcpLocalRelayVLANState_Type.__name__=_B
_SwL2DhcpLocalRelayVLANState_Object=MibTableColumn
swL2DhcpLocalRelayVLANState=_SwL2DhcpLocalRelayVLANState_Object((1,3,6,1,4,1,171,11,102,1,4,2,24,2,1,2),_SwL2DhcpLocalRelayVLANState_Type())
swL2DhcpLocalRelayVLANState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANState.setStatus(_A)
_SwL2MgmtMIBTraps_ObjectIdentity=ObjectIdentity
swL2MgmtMIBTraps=_SwL2MgmtMIBTraps_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,100))
_SwL2Notify_ObjectIdentity=ObjectIdentity
swL2Notify=_SwL2Notify_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,100,1))
_SwL2NotifyMgmt_ObjectIdentity=ObjectIdentity
swL2NotifyMgmt=_SwL2NotifyMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,100,1,1))
_SwL2NotifyPrefix_ObjectIdentity=ObjectIdentity
swL2NotifyPrefix=_SwL2NotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,100,1,2))
_SwL2NotifFirmware_ObjectIdentity=ObjectIdentity
swL2NotifFirmware=_SwL2NotifFirmware_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,100,1,2,0))
_Swl2NotificationBidings_ObjectIdentity=ObjectIdentity
swl2NotificationBidings=_Swl2NotificationBidings_ObjectIdentity((1,3,6,1,4,1,171,11,102,1,4,2,100,1,2,1))
class _SwL2macNotifyInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_SwL2macNotifyInfo_Type.__name__=_L
_SwL2macNotifyInfo_Object=MibScalar
swL2macNotifyInfo=_SwL2macNotifyInfo_Object((1,3,6,1,4,1,171,11,102,1,4,2,100,1,2,1,1),_SwL2macNotifyInfo_Type())
swL2macNotifyInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2macNotifyInfo.setStatus(_A)
_SwL2VlanLoopDetectVID_Type=Integer32
_SwL2VlanLoopDetectVID_Object=MibScalar
swL2VlanLoopDetectVID=_SwL2VlanLoopDetectVID_Object((1,3,6,1,4,1,171,11,102,1,4,2,100,1,2,1,3),_SwL2VlanLoopDetectVID_Type())
swL2VlanLoopDetectVID.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:swL2VlanLoopDetectVID.setStatus(_A)
_SwL2DyingGaspMac_Type=MacAddress
_SwL2DyingGaspMac_Object=MibScalar
swL2DyingGaspMac=_SwL2DyingGaspMac_Object((1,3,6,1,4,1,171,11,102,1,4,2,100,1,2,1,4),_SwL2DyingGaspMac_Type())
swL2DyingGaspMac.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DyingGaspMac.setStatus(_A)
swL2macNotification=NotificationType((1,3,6,1,4,1,171,11,102,1,4,2,100,1,2,0,1))
swL2macNotification.setObjects((_G,_j))
if mibBuilder.loadTexts:swL2macNotification.setStatus(_A)
swL2PortLoopOccurred=NotificationType((1,3,6,1,4,1,171,11,102,1,4,2,100,1,2,0,3))
swL2PortLoopOccurred.setObjects((_G,_I))
if mibBuilder.loadTexts:swL2PortLoopOccurred.setStatus(_A)
swL2PortLoopRestart=NotificationType((1,3,6,1,4,1,171,11,102,1,4,2,100,1,2,0,4))
swL2PortLoopRestart.setObjects((_G,_I))
if mibBuilder.loadTexts:swL2PortLoopRestart.setStatus(_A)
swL2VlanLoopOccurred=NotificationType((1,3,6,1,4,1,171,11,102,1,4,2,100,1,2,0,5))
swL2VlanLoopOccurred.setObjects(*((_G,_I),(_G,_N)))
if mibBuilder.loadTexts:swL2VlanLoopOccurred.setStatus(_A)
swL2VlanLoopRestart=NotificationType((1,3,6,1,4,1,171,11,102,1,4,2,100,1,2,0,6))
swL2VlanLoopRestart.setObjects(*((_G,_I),(_G,_N)))
if mibBuilder.loadTexts:swL2VlanLoopRestart.setStatus(_A)
swL2DyingGaspPowerLost=NotificationType((1,3,6,1,4,1,171,11,102,1,4,2,100,1,2,0,7))
swL2DyingGaspPowerLost.setObjects((_G,_k))
if mibBuilder.loadTexts:swL2DyingGaspPowerLost.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'MacAddress':MacAddress,'VlanId':VlanId,'PortList':PortList,'Ipv6Address':Ipv6Address,'swL2MgmtMIB':swL2MgmtMIB,'swL2DevMgmt':swL2DevMgmt,'swL2DevInfo':swL2DevInfo,'swDevInfoTotalNumOfPort':swDevInfoTotalNumOfPort,'swDevInfoNumOfPortInUse':swDevInfoNumOfPortInUse,'swDevInfoFrontPanelLedStatus':swDevInfoFrontPanelLedStatus,'swL2DevCtrl':swL2DevCtrl,'swL2DevCtrlStpState':swL2DevCtrlStpState,'swL2DevCtrlIGMPSnooping':swL2DevCtrlIGMPSnooping,'swL2DevCtrlSnmpTrapState':swL2DevCtrlSnmpTrapState,'swL2DevCtrlCleanAllStatisticCounter':swL2DevCtrlCleanAllStatisticCounter,'swL2DevCtrlVlanIdOfFDBTbl':swL2DevCtrlVlanIdOfFDBTbl,'swL2MACNotifyState':swL2MACNotifyState,'swL2MACNotifyHistorySize':swL2MACNotifyHistorySize,'swL2MACNotifyInterval':swL2MACNotifyInterval,'swL2DevCtrlTelnet':swL2DevCtrlTelnet,'swL2DevCtrlTelnetState':swL2DevCtrlTelnetState,'swL2DevCtrlTelnetTcpPort':swL2DevCtrlTelnetTcpPort,'swL2DevCtrlManagementVlanId':swL2DevCtrlManagementVlanId,'swL2DevCtrlWeb':swL2DevCtrlWeb,'swL2DevCtrlWebState':swL2DevCtrlWebState,'swL2DevCtrlWebTcpPort':swL2DevCtrlWebTcpPort,'swL2DevCtrlLLDPState':swL2DevCtrlLLDPState,'swL2DevCtrlLLDPForwardMessageState':swL2DevCtrlLLDPForwardMessageState,'swL2DevCtrlIpAutoconfig':swL2DevCtrlIpAutoconfig,'swL2DevCtrlCFM':swL2DevCtrlCFM,'swL2DevCtrlCFMState':swL2DevCtrlCFMState,'swL2DevCtrlCFMPortTable':swL2DevCtrlCFMPortTable,'swL2DevCtrlCFMPortEntry':swL2DevCtrlCFMPortEntry,_P:swL2DevCtrlCFMPortIndex,'swL2DevCtrlCFMPortState':swL2DevCtrlCFMPortState,'swL2DevAlarm':swL2DevAlarm,'swL2DevAlarmNewRoot':swL2DevAlarmNewRoot,'swL2DevAlarmTopologyChange':swL2DevAlarmTopologyChange,'swL2DevAlarmLinkChange':swL2DevAlarmLinkChange,'swL2VLANMgmt':swL2VLANMgmt,'swL2VlanStaticTable':swL2VlanStaticTable,'swL2VlanStaticEntry':swL2VlanStaticEntry,_R:swL2VlanIndex,'swL2VLANAdvertisement':swL2VLANAdvertisement,'swL2PVIDAutoAssignmentState':swL2PVIDAutoAssignmentState,'swL2VlanPortInfoTable':swL2VlanPortInfoTable,'swL2VlanPortInfoEntry':swL2VlanPortInfoEntry,_S:swL2VlanPortInfoPortIndex,_T:swL2VlanPortInfoVid,'swL2VlanPortInfoPortRole':swL2VlanPortInfoPortRole,'swL2NniGvrpBpduAddress':swL2NniGvrpBpduAddress,'swL2PortMgmt':swL2PortMgmt,'swL2PortInfoTable':swL2PortInfoTable,'swL2PortInfoEntry':swL2PortInfoEntry,_U:swL2PortInfoPortIndex,_V:swL2PortInfoMediumType,'swL2PortInfoUnitID':swL2PortInfoUnitID,'swL2PortInfoType':swL2PortInfoType,'swL2PortInfoLinkStatus':swL2PortInfoLinkStatus,'swL2PortInfoNwayStatus':swL2PortInfoNwayStatus,'swL2PortInfoErrorDisabled':swL2PortInfoErrorDisabled,'swL2PortCtrlTable':swL2PortCtrlTable,'swL2PortCtrlEntry':swL2PortCtrlEntry,_Z:swL2PortCtrlPortIndex,_a:swL2PortCtrlMediumType,'swL2PortCtrlUnitIndex':swL2PortCtrlUnitIndex,'swL2PortCtrlAdminState':swL2PortCtrlAdminState,'swL2PortCtrlNwayState':swL2PortCtrlNwayState,'swL2PortCtrlFlowCtrlState':swL2PortCtrlFlowCtrlState,'swL2PortCtrlLearningState':swL2PortCtrlLearningState,'swL2PortCtrlMACNotifyState':swL2PortCtrlMACNotifyState,'swL2PortCtrlMDIXState':swL2PortCtrlMDIXState,'swL2PortCtrlJumboFrame':swL2PortCtrlJumboFrame,'swL2PortCtrlJumboFrameMaxSize':swL2PortCtrlJumboFrameMaxSize,'swL2PortCounterCtrlTable':swL2PortCounterCtrlTable,'swL2PortCounterCtrlEntry':swL2PortCounterCtrlEntry,_b:swL2PortCounterCtrlPortIndex,'swL2PortCounterClearCtrl':swL2PortCounterClearCtrl,'swL2PortErrTable':swL2PortErrTable,'swL2PortErrEntry':swL2PortErrEntry,_c:swL2PortErrPortIndex,'swL2PortErrPortState':swL2PortErrPortState,'swL2PortErrPortConnStatus':swL2PortErrPortConnStatus,'swL2PortErrPortReason':swL2PortErrPortReason,'swL2PortDropCounterTable':swL2PortDropCounterTable,'swL2PortDropCounterEntry':swL2PortDropCounterEntry,_d:swL2PortDropCounterPortIndex,'swL2PortIngressBandwidthControlDrops':swL2PortIngressBandwidthControlDrops,'swL2DhcpRelayMgmt':swL2DhcpRelayMgmt,'swL2TrunkMgmt':swL2TrunkMgmt,'swL2TrunkMaxSupportedEntries':swL2TrunkMaxSupportedEntries,'swL2TrunkCurrentNumEntries':swL2TrunkCurrentNumEntries,'swL2TrunkCtrlTable':swL2TrunkCtrlTable,'swL2TrunkCtrlEntry':swL2TrunkCtrlEntry,_e:swL2TrunkIndex,'swL2TrunkMasterPort':swL2TrunkMasterPort,'swL2TrunkMember':swL2TrunkMember,'swL2TrunkFloodingPort':swL2TrunkFloodingPort,'swL2TrunkType':swL2TrunkType,'swL2TrunkState':swL2TrunkState,'swL2TrunkAlgorithm':swL2TrunkAlgorithm,'swL2TrunkLACPPortTable':swL2TrunkLACPPortTable,'swL2TrunkLACPPortEntry':swL2TrunkLACPPortEntry,_f:swL2TrunkLACPPortIndex,'swL2TrunkLACPPortState':swL2TrunkLACPPortState,'swL2MirrorMgmt':swL2MirrorMgmt,'swL2MirrorLogicTargetPort':swL2MirrorLogicTargetPort,'swL2MirrorPortSourceIngress':swL2MirrorPortSourceIngress,'swL2MirrorPortSourceEgress':swL2MirrorPortSourceEgress,'swL2MirrorPortState':swL2MirrorPortState,'swL2TrafficSegMgmt':swL2TrafficSegMgmt,'swL2TrafficSegTable':swL2TrafficSegTable,'swL2TrafficSegEntry':swL2TrafficSegEntry,_g:swL2TrafficSegPort,'swL2TrafficSegForwardPorts':swL2TrafficSegForwardPorts,'swL2MulticastFilterMode':swL2MulticastFilterMode,'swL2MulticastFilterModeVlanTable':swL2MulticastFilterModeVlanTable,'swL2MulticastFilterModeVlanEntry':swL2MulticastFilterModeVlanEntry,_h:swL2MulticastFilterVid,'swL2MulticastFilterVlanMode':swL2MulticastFilterVlanMode,'swL2LoopDetectMgmt':swL2LoopDetectMgmt,'swL2LoopDetectCtrl':swL2LoopDetectCtrl,'swL2LoopDetectAdminState':swL2LoopDetectAdminState,'swL2LoopDetectInterval':swL2LoopDetectInterval,'swL2LoopDetectRecoverTime':swL2LoopDetectRecoverTime,'swL2LoopDetectMode':swL2LoopDetectMode,'swL2LoopDetectTrapMode':swL2LoopDetectTrapMode,'swL2LoopDetectPortMgmt':swL2LoopDetectPortMgmt,'swL2LoopDetectPortTable':swL2LoopDetectPortTable,'swL2LoopDetectPortEntry':swL2LoopDetectPortEntry,_I:swL2LoopDetectPortIndex,'swL2LoopDetectPortState':swL2LoopDetectPortState,'swL2LoopDetectPortLoopVLAN':swL2LoopDetectPortLoopVLAN,'swL2LoopDetectPortLoopStatus':swL2LoopDetectPortLoopStatus,'swL2DhcpLocalRelayMgmt':swL2DhcpLocalRelayMgmt,'swL2DhcpLocalRelayState':swL2DhcpLocalRelayState,'swL2DhcpLocalRelayVLANTable':swL2DhcpLocalRelayVLANTable,'swL2DhcpLocalRelayVLANEntry':swL2DhcpLocalRelayVLANEntry,_i:swL2DhcpLocalRelayVLANID,'swL2DhcpLocalRelayVLANState':swL2DhcpLocalRelayVLANState,'swL2MgmtMIBTraps':swL2MgmtMIBTraps,'swL2Notify':swL2Notify,'swL2NotifyMgmt':swL2NotifyMgmt,'swL2NotifyPrefix':swL2NotifyPrefix,'swL2NotifFirmware':swL2NotifFirmware,'swL2macNotification':swL2macNotification,'swL2PortLoopOccurred':swL2PortLoopOccurred,'swL2PortLoopRestart':swL2PortLoopRestart,'swL2VlanLoopOccurred':swL2VlanLoopOccurred,'swL2VlanLoopRestart':swL2VlanLoopRestart,'swL2DyingGaspPowerLost':swL2DyingGaspPowerLost,'swl2NotificationBidings':swl2NotificationBidings,_j:swL2macNotifyInfo,_N:swL2VlanLoopDetectVID,_k:swL2DyingGaspMac})