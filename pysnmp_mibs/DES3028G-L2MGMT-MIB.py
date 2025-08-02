_AL='swL2FloodMacDetectedMacAddress'
_AK='swL2FloodMacDetectedMacVid'
_AJ='swL2macNotifyInfo'
_AI='swL2PortSecurityViolationMac'
_AH='swL2FloodMACFDBMacAddress'
_AG='swL2FloodMACFDBVID'
_AF='swL2FloodMACFDBIndex'
_AE='swL2DhcpLocalRelayVLANID'
_AD='swL2VlanIndex'
_AC='swL2McastFilterPortInfoPortIndex'
_AB='swL2McastFilterPortMaxGroupPortIndex'
_AA='swL2McastFilterPortGroupPortIndex'
_A9='swL2McastFilterProfileIndex'
_A8='swL2DhcpRelayCtrlServer'
_A7='swL2DhcpRelayCtrlInterfaceName'
_A6='swL2CosDscpPRIIndex'
_A5='swL2CosTosPRIIndex'
_A4='swL2CosMacBasePRIIndex'
_A3='swL2CosPortPRIIndex'
_A2='swL2CosPriorityPort'
_A1='swL2TrafficSegPort'
_A0='swIGMPSnoopingGroupSourceAddr'
_z='swIGMPSnoopingGroupGroupAddr'
_y='swIGMPSnoopingGroupVid'
_x='swL2IGMPv3SourceIPAddr'
_w='swL2IGMPMulticastVlanGroupToIp'
_v='swL2IGMPMulticastVlanGroupFromIp'
_u='swL2IGMPMulticastVlanGroupVid'
_t='swL2IGMPMulticastVlanid'
_s='swL2IGMPAccessAuthPort'
_r='swL2IGMPRouterPortVlanid'
_q='swL2IGMPInfoVid'
_p='swL2IGMPCtrlVid'
_o='swL2TrunkVLANPort'
_n='swL2TrunkLACPPortIndex'
_m='swPortTrunkIndex'
_l='swL2QOS8021pDefaultPriorityIndex'
_k='swL2QOS8021pUserPriorityIndex'
_j='weightfair'
_i='strict'
_h='swL2QOSSchedulingClassIndex'
_g='swL2QOSBandwidthPortIndex'
_f='swL2PortErrPortIndex'
_e='swL2PortCtrlPortMediumType'
_d='swL2PortCtrlPortIndex'
_c='copper'
_b='swL2PortInfoMediumType'
_a='swL2PortInfoPortIndex'
_Z='SnmpAdminString'
_Y='swL2FloodMACAutoFDBIPAddress'
_X='swL2PortSecurityPortIndex'
_W='start'
_V='swL2IGMPGroupIpAddr'
_U='swL2IGMPVid'
_T='active'
_S='normal'
_R='OctetString'
_Q='not-accessible'
_P='delete'
_O='swL2LoopDetectPortIndex'
_N='enable'
_M='none'
_L='disable'
_K='DisplayString'
_J='obsolete'
_I='read-create'
_H='enabled'
_G='disabled'
_F='other'
_E='DES3028G-L2MGMT-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_Z)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention','TruthValue')
des3028g,=mibBuilder.importSymbols('SWPRIMGMT-DES30XXP-MIB','des3028g')
swL2MgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,11,63,11,2))
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SwL2DevMgmt_ObjectIdentity=ObjectIdentity
swL2DevMgmt=_SwL2DevMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,1))
_SwL2DevInfo_ObjectIdentity=ObjectIdentity
swL2DevInfo=_SwL2DevInfo_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,1,1))
class _SwL2DevInfoFrontPanelLedStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwL2DevInfoFrontPanelLedStatus_Type.__name__=_R
_SwL2DevInfoFrontPanelLedStatus_Object=MibScalar
swL2DevInfoFrontPanelLedStatus=_SwL2DevInfoFrontPanelLedStatus_Object((1,3,6,1,4,1,171,11,63,11,2,1,1,5),_SwL2DevInfoFrontPanelLedStatus_Type())
swL2DevInfoFrontPanelLedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevInfoFrontPanelLedStatus.setStatus(_A)
_SwL2DevCtrl_ObjectIdentity=ObjectIdentity
swL2DevCtrl=_SwL2DevCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,1,2))
class _SwL2DevCtrlSystemReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('reboot',2),('save-config-and-reboot',3),('reboot-and-load-factory-default-config',4)))
_SwL2DevCtrlSystemReboot_Type.__name__=_B
_SwL2DevCtrlSystemReboot_Object=MibScalar
swL2DevCtrlSystemReboot=_SwL2DevCtrlSystemReboot_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,1),_SwL2DevCtrlSystemReboot_Type())
swL2DevCtrlSystemReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlSystemReboot.setStatus(_A)
_SwL2DevCtrlSystemIP_Type=IpAddress
_SwL2DevCtrlSystemIP_Object=MibScalar
swL2DevCtrlSystemIP=_SwL2DevCtrlSystemIP_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,2),_SwL2DevCtrlSystemIP_Type())
swL2DevCtrlSystemIP.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlSystemIP.setStatus(_A)
_SwL2DevCtrlSubnetMask_Type=IpAddress
_SwL2DevCtrlSubnetMask_Object=MibScalar
swL2DevCtrlSubnetMask=_SwL2DevCtrlSubnetMask_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,3),_SwL2DevCtrlSubnetMask_Type())
swL2DevCtrlSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlSubnetMask.setStatus(_A)
_SwL2DevCtrlDefaultGateway_Type=IpAddress
_SwL2DevCtrlDefaultGateway_Object=MibScalar
swL2DevCtrlDefaultGateway=_SwL2DevCtrlDefaultGateway_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,4),_SwL2DevCtrlDefaultGateway_Type())
swL2DevCtrlDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlDefaultGateway.setStatus(_A)
_SwL2DevCtrlManagementVlanId_Type=VlanId
_SwL2DevCtrlManagementVlanId_Object=MibScalar
swL2DevCtrlManagementVlanId=_SwL2DevCtrlManagementVlanId_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,5),_SwL2DevCtrlManagementVlanId_Type())
swL2DevCtrlManagementVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlManagementVlanId.setStatus(_A)
class _SwL2DevCtrlIGMPSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlIGMPSnooping_Type.__name__=_B
_SwL2DevCtrlIGMPSnooping_Object=MibScalar
swL2DevCtrlIGMPSnooping=_SwL2DevCtrlIGMPSnooping_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,7),_SwL2DevCtrlIGMPSnooping_Type())
swL2DevCtrlIGMPSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlIGMPSnooping.setStatus(_A)
class _SwL2DevCtrlCleanAllStatisticCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_SwL2DevCtrlCleanAllStatisticCounter_Type.__name__=_B
_SwL2DevCtrlCleanAllStatisticCounter_Object=MibScalar
swL2DevCtrlCleanAllStatisticCounter=_SwL2DevCtrlCleanAllStatisticCounter_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,12),_SwL2DevCtrlCleanAllStatisticCounter_Type())
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlCleanAllStatisticCounter.setStatus(_A)
class _SwL2DevCtrlSnmpEnableAuthenTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlSnmpEnableAuthenTraps_Type.__name__=_B
_SwL2DevCtrlSnmpEnableAuthenTraps_Object=MibScalar
swL2DevCtrlSnmpEnableAuthenTraps=_SwL2DevCtrlSnmpEnableAuthenTraps_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,13),_SwL2DevCtrlSnmpEnableAuthenTraps_Type())
swL2DevCtrlSnmpEnableAuthenTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlSnmpEnableAuthenTraps.setStatus(_A)
class _SwL2DevCtrlRmonState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlRmonState_Type.__name__=_B
_SwL2DevCtrlRmonState_Object=MibScalar
swL2DevCtrlRmonState=_SwL2DevCtrlRmonState_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,16),_SwL2DevCtrlRmonState_Type())
swL2DevCtrlRmonState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlRmonState.setStatus(_A)
class _SwL2DevCtrlIpAutoConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlIpAutoConfig_Type.__name__=_B
_SwL2DevCtrlIpAutoConfig_Object=MibScalar
swL2DevCtrlIpAutoConfig=_SwL2DevCtrlIpAutoConfig_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,17),_SwL2DevCtrlIpAutoConfig_Type())
swL2DevCtrlIpAutoConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlIpAutoConfig.setStatus(_A)
class _SwL2MACNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2MACNotifyState_Type.__name__=_B
_SwL2MACNotifyState_Object=MibScalar
swL2MACNotifyState=_SwL2MACNotifyState_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,19),_SwL2MACNotifyState_Type())
swL2MACNotifyState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MACNotifyState.setStatus(_A)
class _SwL2MACNotifyHistorySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_SwL2MACNotifyHistorySize_Type.__name__=_B
_SwL2MACNotifyHistorySize_Object=MibScalar
swL2MACNotifyHistorySize=_SwL2MACNotifyHistorySize_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,20),_SwL2MACNotifyHistorySize_Type())
swL2MACNotifyHistorySize.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MACNotifyHistorySize.setStatus(_A)
class _SwL2MACNotifyInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SwL2MACNotifyInterval_Type.__name__=_B
_SwL2MACNotifyInterval_Object=MibScalar
swL2MACNotifyInterval=_SwL2MACNotifyInterval_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,21),_SwL2MACNotifyInterval_Type())
swL2MACNotifyInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MACNotifyInterval.setStatus(_A)
class _SwL2DevCtrlLLDPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlLLDPState_Type.__name__=_B
_SwL2DevCtrlLLDPState_Object=MibScalar
swL2DevCtrlLLDPState=_SwL2DevCtrlLLDPState_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,22),_SwL2DevCtrlLLDPState_Type())
swL2DevCtrlLLDPState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlLLDPState.setStatus(_A)
class _SwL2DevCtrlLLDPForwardMessageState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlLLDPForwardMessageState_Type.__name__=_B
_SwL2DevCtrlLLDPForwardMessageState_Object=MibScalar
swL2DevCtrlLLDPForwardMessageState=_SwL2DevCtrlLLDPForwardMessageState_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,23),_SwL2DevCtrlLLDPForwardMessageState_Type())
swL2DevCtrlLLDPForwardMessageState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlLLDPForwardMessageState.setStatus(_A)
class _SwL2DevCtrlAsymVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlAsymVlanState_Type.__name__=_B
_SwL2DevCtrlAsymVlanState_Object=MibScalar
swL2DevCtrlAsymVlanState=_SwL2DevCtrlAsymVlanState_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,24),_SwL2DevCtrlAsymVlanState_Type())
swL2DevCtrlAsymVlanState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlAsymVlanState.setStatus(_A)
class _SwL2IGMPSnoopingMulticastVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2IGMPSnoopingMulticastVlanState_Type.__name__=_B
_SwL2IGMPSnoopingMulticastVlanState_Object=MibScalar
swL2IGMPSnoopingMulticastVlanState=_SwL2IGMPSnoopingMulticastVlanState_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,25),_SwL2IGMPSnoopingMulticastVlanState_Type())
swL2IGMPSnoopingMulticastVlanState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPSnoopingMulticastVlanState.setStatus(_A)
class _SwL2DevCtrlVLANTrunkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlVLANTrunkState_Type.__name__=_B
_SwL2DevCtrlVLANTrunkState_Object=MibScalar
swL2DevCtrlVLANTrunkState=_SwL2DevCtrlVLANTrunkState_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,26),_SwL2DevCtrlVLANTrunkState_Type())
swL2DevCtrlVLANTrunkState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlVLANTrunkState.setStatus(_A)
_SwL2DevCtrlWeb_ObjectIdentity=ObjectIdentity
swL2DevCtrlWeb=_SwL2DevCtrlWeb_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,1,2,27))
class _SwL2DevCtrlWebState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlWebState_Type.__name__=_B
_SwL2DevCtrlWebState_Object=MibScalar
swL2DevCtrlWebState=_SwL2DevCtrlWebState_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,27,1),_SwL2DevCtrlWebState_Type())
swL2DevCtrlWebState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlWebState.setStatus(_A)
_SwL2DevCtrlTelnet_ObjectIdentity=ObjectIdentity
swL2DevCtrlTelnet=_SwL2DevCtrlTelnet_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,1,2,28))
class _SwL2DevCtrlTelnetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlTelnetState_Type.__name__=_B
_SwL2DevCtrlTelnetState_Object=MibScalar
swL2DevCtrlTelnetState=_SwL2DevCtrlTelnetState_Object((1,3,6,1,4,1,171,11,63,11,2,1,2,28,1),_SwL2DevCtrlTelnetState_Type())
swL2DevCtrlTelnetState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlTelnetState.setStatus(_A)
_SwL2DevAlarm_ObjectIdentity=ObjectIdentity
swL2DevAlarm=_SwL2DevAlarm_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,1,3))
class _SwL2DevAlarmNewRoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevAlarmNewRoot_Type.__name__=_B
_SwL2DevAlarmNewRoot_Object=MibScalar
swL2DevAlarmNewRoot=_SwL2DevAlarmNewRoot_Object((1,3,6,1,4,1,171,11,63,11,2,1,3,1),_SwL2DevAlarmNewRoot_Type())
swL2DevAlarmNewRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevAlarmNewRoot.setStatus(_A)
class _SwL2DevAlarmTopologyChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevAlarmTopologyChange_Type.__name__=_B
_SwL2DevAlarmTopologyChange_Object=MibScalar
swL2DevAlarmTopologyChange=_SwL2DevAlarmTopologyChange_Object((1,3,6,1,4,1,171,11,63,11,2,1,3,2),_SwL2DevAlarmTopologyChange_Type())
swL2DevAlarmTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevAlarmTopologyChange.setStatus(_A)
class _SwL2DevAlarmLinkChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevAlarmLinkChange_Type.__name__=_B
_SwL2DevAlarmLinkChange_Object=MibScalar
swL2DevAlarmLinkChange=_SwL2DevAlarmLinkChange_Object((1,3,6,1,4,1,171,11,63,11,2,1,3,3),_SwL2DevAlarmLinkChange_Type())
swL2DevAlarmLinkChange.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevAlarmLinkChange.setStatus(_A)
_SwL2PortMgmt_ObjectIdentity=ObjectIdentity
swL2PortMgmt=_SwL2PortMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,2))
_SwL2PortInfoTable_Object=MibTable
swL2PortInfoTable=_SwL2PortInfoTable_Object((1,3,6,1,4,1,171,11,63,11,2,2,1))
if mibBuilder.loadTexts:swL2PortInfoTable.setStatus(_A)
_SwL2PortInfoEntry_Object=MibTableRow
swL2PortInfoEntry=_SwL2PortInfoEntry_Object((1,3,6,1,4,1,171,11,63,11,2,2,1,1))
swL2PortInfoEntry.setIndexNames((0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:swL2PortInfoEntry.setStatus(_A)
class _SwL2PortInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2PortInfoPortIndex_Type.__name__=_B
_SwL2PortInfoPortIndex_Object=MibTableColumn
swL2PortInfoPortIndex=_SwL2PortInfoPortIndex_Object((1,3,6,1,4,1,171,11,63,11,2,2,1,1,1),_SwL2PortInfoPortIndex_Type())
swL2PortInfoPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoPortIndex.setStatus(_A)
class _SwL2PortInfoMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,101)));namedValues=NamedValues(*((_c,100),('fiber',101)))
_SwL2PortInfoMediumType_Type.__name__=_B
_SwL2PortInfoMediumType_Object=MibTableColumn
swL2PortInfoMediumType=_SwL2PortInfoMediumType_Object((1,3,6,1,4,1,171,11,63,11,2,2,1,1,2),_SwL2PortInfoMediumType_Type())
swL2PortInfoMediumType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoMediumType.setStatus(_A)
class _SwL2PortInfoLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('link-pass',2),('link-fail',3)))
_SwL2PortInfoLinkStatus_Type.__name__=_B
_SwL2PortInfoLinkStatus_Object=MibTableColumn
swL2PortInfoLinkStatus=_SwL2PortInfoLinkStatus_Object((1,3,6,1,4,1,171,11,63,11,2,2,1,1,4),_SwL2PortInfoLinkStatus_Type())
swL2PortInfoLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoLinkStatus.setStatus(_A)
class _SwL2PortInfoNwayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('auto',1),('half-10Mbps',2),('full-10Mbps',3),('half-100Mbps',4),('full-100Mbps',5),('half-1Gigabps',6),('full-1Gigabps',7)))
_SwL2PortInfoNwayStatus_Type.__name__=_B
_SwL2PortInfoNwayStatus_Object=MibTableColumn
swL2PortInfoNwayStatus=_SwL2PortInfoNwayStatus_Object((1,3,6,1,4,1,171,11,63,11,2,2,1,1,5),_SwL2PortInfoNwayStatus_Type())
swL2PortInfoNwayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoNwayStatus.setStatus(_A)
_SwL2PortCtrlTable_Object=MibTable
swL2PortCtrlTable=_SwL2PortCtrlTable_Object((1,3,6,1,4,1,171,11,63,11,2,2,2))
if mibBuilder.loadTexts:swL2PortCtrlTable.setStatus(_A)
_SwL2PortCtrlEntry_Object=MibTableRow
swL2PortCtrlEntry=_SwL2PortCtrlEntry_Object((1,3,6,1,4,1,171,11,63,11,2,2,2,1))
swL2PortCtrlEntry.setIndexNames((0,_E,_d),(0,_E,_e))
if mibBuilder.loadTexts:swL2PortCtrlEntry.setStatus(_A)
class _SwL2PortCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2PortCtrlPortIndex_Type.__name__=_B
_SwL2PortCtrlPortIndex_Object=MibTableColumn
swL2PortCtrlPortIndex=_SwL2PortCtrlPortIndex_Object((1,3,6,1,4,1,171,11,63,11,2,2,2,1,1),_SwL2PortCtrlPortIndex_Type())
swL2PortCtrlPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlPortIndex.setStatus(_A)
class _SwL2PortCtrlPortMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,101)));namedValues=NamedValues(*((_c,100),('fiber',101)))
_SwL2PortCtrlPortMediumType_Type.__name__=_B
_SwL2PortCtrlPortMediumType_Object=MibTableColumn
swL2PortCtrlPortMediumType=_SwL2PortCtrlPortMediumType_Object((1,3,6,1,4,1,171,11,63,11,2,2,2,1,2),_SwL2PortCtrlPortMediumType_Type())
swL2PortCtrlPortMediumType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlPortMediumType.setStatus(_A)
class _SwL2PortCtrlAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortCtrlAdminState_Type.__name__=_B
_SwL2PortCtrlAdminState_Object=MibTableColumn
swL2PortCtrlAdminState=_SwL2PortCtrlAdminState_Object((1,3,6,1,4,1,171,11,63,11,2,2,2,1,3),_SwL2PortCtrlAdminState_Type())
swL2PortCtrlAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlAdminState.setStatus(_A)
class _SwL2PortCtrlNwayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,8,9)));namedValues=NamedValues(*(('nway-auto',1),('nway-disabled-10Mbps-Half',2),('nway-disabled-10Mbps-Full',3),('nway-disabled-100Mbps-Half',4),('nway-disabled-100Mbps-Full',5),('nway-disabled-1Gigabps-Full',7),('nway-disabled-1Gigabps-Full-Master',8),('nway-disabled-1Gigabps-Full-Slave',9)))
_SwL2PortCtrlNwayState_Type.__name__=_B
_SwL2PortCtrlNwayState_Object=MibTableColumn
swL2PortCtrlNwayState=_SwL2PortCtrlNwayState_Object((1,3,6,1,4,1,171,11,63,11,2,2,2,1,4),_SwL2PortCtrlNwayState_Type())
swL2PortCtrlNwayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlNwayState.setStatus(_A)
class _SwL2PortCtrlFlowCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortCtrlFlowCtrlState_Type.__name__=_B
_SwL2PortCtrlFlowCtrlState_Object=MibTableColumn
swL2PortCtrlFlowCtrlState=_SwL2PortCtrlFlowCtrlState_Object((1,3,6,1,4,1,171,11,63,11,2,2,2,1,5),_SwL2PortCtrlFlowCtrlState_Type())
swL2PortCtrlFlowCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlFlowCtrlState.setStatus(_A)
class _SwL2PortCtrlDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2PortCtrlDescription_Type.__name__=_K
_SwL2PortCtrlDescription_Object=MibTableColumn
swL2PortCtrlDescription=_SwL2PortCtrlDescription_Object((1,3,6,1,4,1,171,11,63,11,2,2,2,1,6),_SwL2PortCtrlDescription_Type())
swL2PortCtrlDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlDescription.setStatus(_A)
class _SwL2PortCtrlAddressLearning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortCtrlAddressLearning_Type.__name__=_B
_SwL2PortCtrlAddressLearning_Object=MibTableColumn
swL2PortCtrlAddressLearning=_SwL2PortCtrlAddressLearning_Object((1,3,6,1,4,1,171,11,63,11,2,2,2,1,7),_SwL2PortCtrlAddressLearning_Type())
swL2PortCtrlAddressLearning.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlAddressLearning.setStatus(_A)
class _SwL2PortCtrlMACNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortCtrlMACNotifyState_Type.__name__=_B
_SwL2PortCtrlMACNotifyState_Object=MibTableColumn
swL2PortCtrlMACNotifyState=_SwL2PortCtrlMACNotifyState_Object((1,3,6,1,4,1,171,11,63,11,2,2,2,1,8),_SwL2PortCtrlMACNotifyState_Type())
swL2PortCtrlMACNotifyState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlMACNotifyState.setStatus(_A)
class _SwL2PortCtrlMulticastfilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('forward-unregistered-groups',2),('filter-unregistered-groups',3)))
_SwL2PortCtrlMulticastfilter_Type.__name__=_B
_SwL2PortCtrlMulticastfilter_Object=MibTableColumn
swL2PortCtrlMulticastfilter=_SwL2PortCtrlMulticastfilter_Object((1,3,6,1,4,1,171,11,63,11,2,2,2,1,9),_SwL2PortCtrlMulticastfilter_Type())
swL2PortCtrlMulticastfilter.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlMulticastfilter.setStatus(_A)
class _SwL2PortCtrlMDIXState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('auto',1),(_S,2),('cross',3),(_F,4)))
_SwL2PortCtrlMDIXState_Type.__name__=_B
_SwL2PortCtrlMDIXState_Object=MibTableColumn
swL2PortCtrlMDIXState=_SwL2PortCtrlMDIXState_Object((1,3,6,1,4,1,171,11,63,11,2,2,2,1,10),_SwL2PortCtrlMDIXState_Type())
swL2PortCtrlMDIXState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlMDIXState.setStatus(_A)
_SwL2PortErrTable_Object=MibTable
swL2PortErrTable=_SwL2PortErrTable_Object((1,3,6,1,4,1,171,11,63,11,2,2,3))
if mibBuilder.loadTexts:swL2PortErrTable.setStatus(_A)
_SwL2PortErrEntry_Object=MibTableRow
swL2PortErrEntry=_SwL2PortErrEntry_Object((1,3,6,1,4,1,171,11,63,11,2,2,3,1))
swL2PortErrEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:swL2PortErrEntry.setStatus(_A)
class _SwL2PortErrPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2PortErrPortIndex_Type.__name__=_B
_SwL2PortErrPortIndex_Object=MibTableColumn
swL2PortErrPortIndex=_SwL2PortErrPortIndex_Object((1,3,6,1,4,1,171,11,63,11,2,2,3,1,1),_SwL2PortErrPortIndex_Type())
swL2PortErrPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortIndex.setStatus(_A)
class _SwL2PortErrPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwL2PortErrPortState_Type.__name__=_B
_SwL2PortErrPortState_Object=MibTableColumn
swL2PortErrPortState=_SwL2PortErrPortState_Object((1,3,6,1,4,1,171,11,63,11,2,2,3,1,2),_SwL2PortErrPortState_Type())
swL2PortErrPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortState.setStatus(_A)
class _SwL2PortErrPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('err-disabled',2)))
_SwL2PortErrPortStatus_Type.__name__=_B
_SwL2PortErrPortStatus_Object=MibTableColumn
swL2PortErrPortStatus=_SwL2PortErrPortStatus_Object((1,3,6,1,4,1,171,11,63,11,2,2,3,1,3),_SwL2PortErrPortStatus_Type())
swL2PortErrPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortStatus.setStatus(_A)
class _SwL2PortErrPortReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('stp-lbd',1),('storm-control',2),('ddm',3),('duld',4)))
_SwL2PortErrPortReason_Type.__name__=_B
_SwL2PortErrPortReason_Object=MibTableColumn
swL2PortErrPortReason=_SwL2PortErrPortReason_Object((1,3,6,1,4,1,171,11,63,11,2,2,3,1,4),_SwL2PortErrPortReason_Type())
swL2PortErrPortReason.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortReason.setStatus(_A)
class _SwL2PortErrDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2PortErrDescription_Type.__name__=_K
_SwL2PortErrDescription_Object=MibTableColumn
swL2PortErrDescription=_SwL2PortErrDescription_Object((1,3,6,1,4,1,171,11,63,11,2,2,3,1,5),_SwL2PortErrDescription_Type())
swL2PortErrDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrDescription.setStatus(_A)
_SwL2QOSMgmt_ObjectIdentity=ObjectIdentity
swL2QOSMgmt=_SwL2QOSMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,3))
_SwL2QOSBandwidthControlTable_Object=MibTable
swL2QOSBandwidthControlTable=_SwL2QOSBandwidthControlTable_Object((1,3,6,1,4,1,171,11,63,11,2,3,1))
if mibBuilder.loadTexts:swL2QOSBandwidthControlTable.setStatus(_A)
_SwL2QOSBandwidthControlEntry_Object=MibTableRow
swL2QOSBandwidthControlEntry=_SwL2QOSBandwidthControlEntry_Object((1,3,6,1,4,1,171,11,63,11,2,3,1,1))
swL2QOSBandwidthControlEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:swL2QOSBandwidthControlEntry.setStatus(_A)
class _SwL2QOSBandwidthPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,650))
_SwL2QOSBandwidthPortIndex_Type.__name__=_B
_SwL2QOSBandwidthPortIndex_Object=MibTableColumn
swL2QOSBandwidthPortIndex=_SwL2QOSBandwidthPortIndex_Object((1,3,6,1,4,1,171,11,63,11,2,3,1,1,1),_SwL2QOSBandwidthPortIndex_Type())
swL2QOSBandwidthPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthPortIndex.setStatus(_A)
class _SwL2QOSBandwidthRxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1024000))
_SwL2QOSBandwidthRxRate_Type.__name__=_B
_SwL2QOSBandwidthRxRate_Object=MibTableColumn
swL2QOSBandwidthRxRate=_SwL2QOSBandwidthRxRate_Object((1,3,6,1,4,1,171,11,63,11,2,3,1,1,2),_SwL2QOSBandwidthRxRate_Type())
swL2QOSBandwidthRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSBandwidthRxRate.setStatus(_A)
class _SwL2QOSBandwidthTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1024000))
_SwL2QOSBandwidthTxRate_Type.__name__=_B
_SwL2QOSBandwidthTxRate_Object=MibTableColumn
swL2QOSBandwidthTxRate=_SwL2QOSBandwidthTxRate_Object((1,3,6,1,4,1,171,11,63,11,2,3,1,1,3),_SwL2QOSBandwidthTxRate_Type())
swL2QOSBandwidthTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSBandwidthTxRate.setStatus(_A)
_SwL2QOSBandwidthRadiusRxRate_Type=Integer32
_SwL2QOSBandwidthRadiusRxRate_Object=MibTableColumn
swL2QOSBandwidthRadiusRxRate=_SwL2QOSBandwidthRadiusRxRate_Object((1,3,6,1,4,1,171,11,63,11,2,3,1,1,4),_SwL2QOSBandwidthRadiusRxRate_Type())
swL2QOSBandwidthRadiusRxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthRadiusRxRate.setStatus(_A)
_SwL2QOSBandwidthRadiusTxRate_Type=Integer32
_SwL2QOSBandwidthRadiusTxRate_Object=MibTableColumn
swL2QOSBandwidthRadiusTxRate=_SwL2QOSBandwidthRadiusTxRate_Object((1,3,6,1,4,1,171,11,63,11,2,3,1,1,5),_SwL2QOSBandwidthRadiusTxRate_Type())
swL2QOSBandwidthRadiusTxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthRadiusTxRate.setStatus(_A)
_SwL2QOSSchedulingTable_Object=MibTable
swL2QOSSchedulingTable=_SwL2QOSSchedulingTable_Object((1,3,6,1,4,1,171,11,63,11,2,3,2))
if mibBuilder.loadTexts:swL2QOSSchedulingTable.setStatus(_A)
_SwL2QOSSchedulingEntry_Object=MibTableRow
swL2QOSSchedulingEntry=_SwL2QOSSchedulingEntry_Object((1,3,6,1,4,1,171,11,63,11,2,3,2,1))
swL2QOSSchedulingEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:swL2QOSSchedulingEntry.setStatus(_A)
class _SwL2QOSSchedulingClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwL2QOSSchedulingClassIndex_Type.__name__=_B
_SwL2QOSSchedulingClassIndex_Object=MibTableColumn
swL2QOSSchedulingClassIndex=_SwL2QOSSchedulingClassIndex_Object((1,3,6,1,4,1,171,11,63,11,2,3,2,1,1),_SwL2QOSSchedulingClassIndex_Type())
swL2QOSSchedulingClassIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSSchedulingClassIndex.setStatus(_A)
class _SwL2QOSSchedulingMaxWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,55))
_SwL2QOSSchedulingMaxWeight_Type.__name__=_B
_SwL2QOSSchedulingMaxWeight_Object=MibTableColumn
swL2QOSSchedulingMaxWeight=_SwL2QOSSchedulingMaxWeight_Object((1,3,6,1,4,1,171,11,63,11,2,3,2,1,4),_SwL2QOSSchedulingMaxWeight_Type())
swL2QOSSchedulingMaxWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSSchedulingMaxWeight.setStatus(_A)
class _SwL2QOSSchedulingMechanism_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),('roundrobin',2),(_j,3)))
_SwL2QOSSchedulingMechanism_Type.__name__=_B
_SwL2QOSSchedulingMechanism_Object=MibTableColumn
swL2QOSSchedulingMechanism=_SwL2QOSSchedulingMechanism_Object((1,3,6,1,4,1,171,11,63,11,2,3,2,1,5),_SwL2QOSSchedulingMechanism_Type())
swL2QOSSchedulingMechanism.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSSchedulingMechanism.setStatus(_A)
_SwL2QOS8021pUserPriorityTable_Object=MibTable
swL2QOS8021pUserPriorityTable=_SwL2QOS8021pUserPriorityTable_Object((1,3,6,1,4,1,171,11,63,11,2,3,3))
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityTable.setStatus(_A)
_SwL2QOS8021pUserPriorityEntry_Object=MibTableRow
swL2QOS8021pUserPriorityEntry=_SwL2QOS8021pUserPriorityEntry_Object((1,3,6,1,4,1,171,11,63,11,2,3,3,1))
swL2QOS8021pUserPriorityEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityEntry.setStatus(_A)
class _SwL2QOS8021pUserPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOS8021pUserPriorityIndex_Type.__name__=_B
_SwL2QOS8021pUserPriorityIndex_Object=MibTableColumn
swL2QOS8021pUserPriorityIndex=_SwL2QOS8021pUserPriorityIndex_Object((1,3,6,1,4,1,171,11,63,11,2,3,3,1,1),_SwL2QOS8021pUserPriorityIndex_Type())
swL2QOS8021pUserPriorityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityIndex.setStatus(_A)
class _SwL2QOS8021pUserPriorityClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwL2QOS8021pUserPriorityClass_Type.__name__=_B
_SwL2QOS8021pUserPriorityClass_Object=MibTableColumn
swL2QOS8021pUserPriorityClass=_SwL2QOS8021pUserPriorityClass_Object((1,3,6,1,4,1,171,11,63,11,2,3,3,1,2),_SwL2QOS8021pUserPriorityClass_Type())
swL2QOS8021pUserPriorityClass.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityClass.setStatus(_A)
_SwL2QOS8021pDefaultPriorityTable_Object=MibTable
swL2QOS8021pDefaultPriorityTable=_SwL2QOS8021pDefaultPriorityTable_Object((1,3,6,1,4,1,171,11,63,11,2,3,4))
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityTable.setStatus(_A)
_SwL2QOS8021pDefaultPriorityEntry_Object=MibTableRow
swL2QOS8021pDefaultPriorityEntry=_SwL2QOS8021pDefaultPriorityEntry_Object((1,3,6,1,4,1,171,11,63,11,2,3,4,1))
swL2QOS8021pDefaultPriorityEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityEntry.setStatus(_A)
class _SwL2QOS8021pDefaultPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,650))
_SwL2QOS8021pDefaultPriorityIndex_Type.__name__=_B
_SwL2QOS8021pDefaultPriorityIndex_Object=MibTableColumn
swL2QOS8021pDefaultPriorityIndex=_SwL2QOS8021pDefaultPriorityIndex_Object((1,3,6,1,4,1,171,11,63,11,2,3,4,1,1),_SwL2QOS8021pDefaultPriorityIndex_Type())
swL2QOS8021pDefaultPriorityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityIndex.setStatus(_A)
class _SwL2QOS8021pDefaultPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOS8021pDefaultPriority_Type.__name__=_B
_SwL2QOS8021pDefaultPriority_Object=MibTableColumn
swL2QOS8021pDefaultPriority=_SwL2QOS8021pDefaultPriority_Object((1,3,6,1,4,1,171,11,63,11,2,3,4,1,2),_SwL2QOS8021pDefaultPriority_Type())
swL2QOS8021pDefaultPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriority.setStatus(_A)
_SwL2QOS8021pRadiusPriority_Type=Integer32
_SwL2QOS8021pRadiusPriority_Object=MibTableColumn
swL2QOS8021pRadiusPriority=_SwL2QOS8021pRadiusPriority_Object((1,3,6,1,4,1,171,11,63,11,2,3,4,1,3),_SwL2QOS8021pRadiusPriority_Type())
swL2QOS8021pRadiusPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pRadiusPriority.setStatus(_A)
class _SwL2QOSSchedulingMechanismCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),(_j,2),(_M,3)))
_SwL2QOSSchedulingMechanismCtrl_Type.__name__=_B
_SwL2QOSSchedulingMechanismCtrl_Object=MibScalar
swL2QOSSchedulingMechanismCtrl=_SwL2QOSSchedulingMechanismCtrl_Object((1,3,6,1,4,1,171,11,63,11,2,3,5),_SwL2QOSSchedulingMechanismCtrl_Type())
swL2QOSSchedulingMechanismCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSSchedulingMechanismCtrl.setStatus(_A)
_SwL2TrunkMgmt_ObjectIdentity=ObjectIdentity
swL2TrunkMgmt=_SwL2TrunkMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,4))
_SwPortTrunkMaxEntries_Type=Integer32
_SwPortTrunkMaxEntries_Object=MibScalar
swPortTrunkMaxEntries=_SwPortTrunkMaxEntries_Object((1,3,6,1,4,1,171,11,63,11,2,4,1),_SwPortTrunkMaxEntries_Type())
swPortTrunkMaxEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:swPortTrunkMaxEntries.setStatus(_A)
_SwPortTrunkMaxPortMembers_Type=Integer32
_SwPortTrunkMaxPortMembers_Object=MibScalar
swPortTrunkMaxPortMembers=_SwPortTrunkMaxPortMembers_Object((1,3,6,1,4,1,171,11,63,11,2,4,2),_SwPortTrunkMaxPortMembers_Type())
swPortTrunkMaxPortMembers.setMaxAccess(_D)
if mibBuilder.loadTexts:swPortTrunkMaxPortMembers.setStatus(_A)
_SwPortTrunkTable_Object=MibTable
swPortTrunkTable=_SwPortTrunkTable_Object((1,3,6,1,4,1,171,11,63,11,2,4,3))
if mibBuilder.loadTexts:swPortTrunkTable.setStatus(_A)
_SwPortTrunkEntry_Object=MibTableRow
swPortTrunkEntry=_SwPortTrunkEntry_Object((1,3,6,1,4,1,171,11,63,11,2,4,3,1))
swPortTrunkEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:swPortTrunkEntry.setStatus(_A)
class _SwPortTrunkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_SwPortTrunkIndex_Type.__name__=_B
_SwPortTrunkIndex_Object=MibTableColumn
swPortTrunkIndex=_SwPortTrunkIndex_Object((1,3,6,1,4,1,171,11,63,11,2,4,3,1,1),_SwPortTrunkIndex_Type())
swPortTrunkIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swPortTrunkIndex.setStatus(_A)
_SwPortTrunkMasterPort_Type=Integer32
_SwPortTrunkMasterPort_Object=MibTableColumn
swPortTrunkMasterPort=_SwPortTrunkMasterPort_Object((1,3,6,1,4,1,171,11,63,11,2,4,3,1,2),_SwPortTrunkMasterPort_Type())
swPortTrunkMasterPort.setMaxAccess(_I)
if mibBuilder.loadTexts:swPortTrunkMasterPort.setStatus(_A)
_SwPortTrunkPortList_Type=PortList
_SwPortTrunkPortList_Object=MibTableColumn
swPortTrunkPortList=_SwPortTrunkPortList_Object((1,3,6,1,4,1,171,11,63,11,2,4,3,1,3),_SwPortTrunkPortList_Type())
swPortTrunkPortList.setMaxAccess(_I)
if mibBuilder.loadTexts:swPortTrunkPortList.setStatus(_A)
class _SwPortTrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('lacp',2)))
_SwPortTrunkType_Type.__name__=_B
_SwPortTrunkType_Object=MibTableColumn
swPortTrunkType=_SwPortTrunkType_Object((1,3,6,1,4,1,171,11,63,11,2,4,3,1,4),_SwPortTrunkType_Type())
swPortTrunkType.setMaxAccess(_I)
if mibBuilder.loadTexts:swPortTrunkType.setStatus(_A)
_SwPortTrunkActivePort_Type=PortList
_SwPortTrunkActivePort_Object=MibTableColumn
swPortTrunkActivePort=_SwPortTrunkActivePort_Object((1,3,6,1,4,1,171,11,63,11,2,4,3,1,5),_SwPortTrunkActivePort_Type())
swPortTrunkActivePort.setMaxAccess(_D)
if mibBuilder.loadTexts:swPortTrunkActivePort.setStatus(_A)
_SwPortTrunkState_Type=RowStatus
_SwPortTrunkState_Object=MibTableColumn
swPortTrunkState=_SwPortTrunkState_Object((1,3,6,1,4,1,171,11,63,11,2,4,3,1,6),_SwPortTrunkState_Type())
swPortTrunkState.setMaxAccess(_I)
if mibBuilder.loadTexts:swPortTrunkState.setStatus(_A)
_SwPortTrunkFloodingPort_Type=Integer32
_SwPortTrunkFloodingPort_Object=MibTableColumn
swPortTrunkFloodingPort=_SwPortTrunkFloodingPort_Object((1,3,6,1,4,1,171,11,63,11,2,4,3,1,7),_SwPortTrunkFloodingPort_Type())
swPortTrunkFloodingPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swPortTrunkFloodingPort.setStatus(_A)
class _SwL2TrunkAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('mac-source',2),('mac-destination',3),('mac-source-dest',4)))
_SwL2TrunkAlgorithm_Type.__name__=_B
_SwL2TrunkAlgorithm_Object=MibScalar
swL2TrunkAlgorithm=_SwL2TrunkAlgorithm_Object((1,3,6,1,4,1,171,11,63,11,2,4,4),_SwL2TrunkAlgorithm_Type())
swL2TrunkAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkAlgorithm.setStatus(_A)
_SwL2TrunkLACPPortTable_Object=MibTable
swL2TrunkLACPPortTable=_SwL2TrunkLACPPortTable_Object((1,3,6,1,4,1,171,11,63,11,2,4,5))
if mibBuilder.loadTexts:swL2TrunkLACPPortTable.setStatus(_A)
_SwL2TrunkLACPPortEntry_Object=MibTableRow
swL2TrunkLACPPortEntry=_SwL2TrunkLACPPortEntry_Object((1,3,6,1,4,1,171,11,63,11,2,4,5,1))
swL2TrunkLACPPortEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:swL2TrunkLACPPortEntry.setStatus(_A)
class _SwL2TrunkLACPPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkLACPPortIndex_Type.__name__=_B
_SwL2TrunkLACPPortIndex_Object=MibTableColumn
swL2TrunkLACPPortIndex=_SwL2TrunkLACPPortIndex_Object((1,3,6,1,4,1,171,11,63,11,2,4,5,1,1),_SwL2TrunkLACPPortIndex_Type())
swL2TrunkLACPPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkLACPPortIndex.setStatus(_A)
class _SwL2TrunkLACPPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('passive',2)))
_SwL2TrunkLACPPortState_Type.__name__=_B
_SwL2TrunkLACPPortState_Object=MibTableColumn
swL2TrunkLACPPortState=_SwL2TrunkLACPPortState_Object((1,3,6,1,4,1,171,11,63,11,2,4,5,1,2),_SwL2TrunkLACPPortState_Type())
swL2TrunkLACPPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkLACPPortState.setStatus(_A)
_SwL2TrunkVLANTable_Object=MibTable
swL2TrunkVLANTable=_SwL2TrunkVLANTable_Object((1,3,6,1,4,1,171,11,63,11,2,4,6))
if mibBuilder.loadTexts:swL2TrunkVLANTable.setStatus(_A)
_SwL2TrunkVLANEntry_Object=MibTableRow
swL2TrunkVLANEntry=_SwL2TrunkVLANEntry_Object((1,3,6,1,4,1,171,11,63,11,2,4,6,1))
swL2TrunkVLANEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:swL2TrunkVLANEntry.setStatus(_A)
class _SwL2TrunkVLANPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkVLANPort_Type.__name__=_B
_SwL2TrunkVLANPort_Object=MibTableColumn
swL2TrunkVLANPort=_SwL2TrunkVLANPort_Object((1,3,6,1,4,1,171,11,63,11,2,4,6,1,1),_SwL2TrunkVLANPort_Type())
swL2TrunkVLANPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkVLANPort.setStatus(_A)
class _SwL2TrunkVLANState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2TrunkVLANState_Type.__name__=_B
_SwL2TrunkVLANState_Object=MibTableColumn
swL2TrunkVLANState=_SwL2TrunkVLANState_Object((1,3,6,1,4,1,171,11,63,11,2,4,6,1,2),_SwL2TrunkVLANState_Type())
swL2TrunkVLANState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkVLANState.setStatus(_A)
_SwPortMirrorPackage_ObjectIdentity=ObjectIdentity
swPortMirrorPackage=_SwPortMirrorPackage_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,6))
_SwPortMirrorRxPortList_Type=PortList
_SwPortMirrorRxPortList_Object=MibScalar
swPortMirrorRxPortList=_SwPortMirrorRxPortList_Object((1,3,6,1,4,1,171,11,63,11,2,6,2),_SwPortMirrorRxPortList_Type())
swPortMirrorRxPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortMirrorRxPortList.setStatus(_A)
_SwPortMirrorTxPortList_Type=PortList
_SwPortMirrorTxPortList_Object=MibScalar
swPortMirrorTxPortList=_SwPortMirrorTxPortList_Object((1,3,6,1,4,1,171,11,63,11,2,6,3),_SwPortMirrorTxPortList_Type())
swPortMirrorTxPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortMirrorTxPortList.setStatus(_A)
_SwPortMirrorTargetPort_Type=Integer32
_SwPortMirrorTargetPort_Object=MibScalar
swPortMirrorTargetPort=_SwPortMirrorTargetPort_Object((1,3,6,1,4,1,171,11,63,11,2,6,4),_SwPortMirrorTargetPort_Type())
swPortMirrorTargetPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortMirrorTargetPort.setStatus(_A)
class _SwPortMirrorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwPortMirrorState_Type.__name__=_B
_SwPortMirrorState_Object=MibScalar
swPortMirrorState=_SwPortMirrorState_Object((1,3,6,1,4,1,171,11,63,11,2,6,5),_SwPortMirrorState_Type())
swPortMirrorState.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortMirrorState.setStatus(_A)
_SwIGMPPackage_ObjectIdentity=ObjectIdentity
swIGMPPackage=_SwIGMPPackage_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,7))
class _SwL2IGMPMaxSupportedVlans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPMaxSupportedVlans_Type.__name__=_B
_SwL2IGMPMaxSupportedVlans_Object=MibScalar
swL2IGMPMaxSupportedVlans=_SwL2IGMPMaxSupportedVlans_Object((1,3,6,1,4,1,171,11,63,11,2,7,1),_SwL2IGMPMaxSupportedVlans_Type())
swL2IGMPMaxSupportedVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMaxSupportedVlans.setStatus(_A)
class _SwL2IGMPMaxIpGroupNumPerVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPMaxIpGroupNumPerVlan_Type.__name__=_B
_SwL2IGMPMaxIpGroupNumPerVlan_Object=MibScalar
swL2IGMPMaxIpGroupNumPerVlan=_SwL2IGMPMaxIpGroupNumPerVlan_Object((1,3,6,1,4,1,171,11,63,11,2,7,2),_SwL2IGMPMaxIpGroupNumPerVlan_Type())
swL2IGMPMaxIpGroupNumPerVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMaxIpGroupNumPerVlan.setStatus(_A)
_SwL2IGMPCtrlTable_Object=MibTable
swL2IGMPCtrlTable=_SwL2IGMPCtrlTable_Object((1,3,6,1,4,1,171,11,63,11,2,7,3))
if mibBuilder.loadTexts:swL2IGMPCtrlTable.setStatus(_A)
_SwL2IGMPCtrlEntry_Object=MibTableRow
swL2IGMPCtrlEntry=_SwL2IGMPCtrlEntry_Object((1,3,6,1,4,1,171,11,63,11,2,7,3,1))
swL2IGMPCtrlEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:swL2IGMPCtrlEntry.setStatus(_A)
class _SwL2IGMPCtrlVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPCtrlVid_Type.__name__=_B
_SwL2IGMPCtrlVid_Object=MibTableColumn
swL2IGMPCtrlVid=_SwL2IGMPCtrlVid_Object((1,3,6,1,4,1,171,11,63,11,2,7,3,1,1),_SwL2IGMPCtrlVid_Type())
swL2IGMPCtrlVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPCtrlVid.setStatus(_A)
class _SwL2IGMPQueryInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2IGMPQueryInterval_Type.__name__=_B
_SwL2IGMPQueryInterval_Object=MibTableColumn
swL2IGMPQueryInterval=_SwL2IGMPQueryInterval_Object((1,3,6,1,4,1,171,11,63,11,2,7,3,1,2),_SwL2IGMPQueryInterval_Type())
swL2IGMPQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPQueryInterval.setStatus(_A)
class _SwL2IGMPMaxResponseTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_SwL2IGMPMaxResponseTime_Type.__name__=_B
_SwL2IGMPMaxResponseTime_Object=MibTableColumn
swL2IGMPMaxResponseTime=_SwL2IGMPMaxResponseTime_Object((1,3,6,1,4,1,171,11,63,11,2,7,3,1,3),_SwL2IGMPMaxResponseTime_Type())
swL2IGMPMaxResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMaxResponseTime.setStatus(_A)
class _SwL2IGMPRobustness_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2IGMPRobustness_Type.__name__=_B
_SwL2IGMPRobustness_Object=MibTableColumn
swL2IGMPRobustness=_SwL2IGMPRobustness_Object((1,3,6,1,4,1,171,11,63,11,2,7,3,1,4),_SwL2IGMPRobustness_Type())
swL2IGMPRobustness.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRobustness.setStatus(_A)
class _SwL2IGMPLastMemberQueryInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_SwL2IGMPLastMemberQueryInterval_Type.__name__=_B
_SwL2IGMPLastMemberQueryInterval_Object=MibTableColumn
swL2IGMPLastMemberQueryInterval=_SwL2IGMPLastMemberQueryInterval_Object((1,3,6,1,4,1,171,11,63,11,2,7,3,1,5),_SwL2IGMPLastMemberQueryInterval_Type())
swL2IGMPLastMemberQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPLastMemberQueryInterval.setStatus(_A)
class _SwL2IGMPHostTimeout_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPHostTimeout_Type.__name__=_B
_SwL2IGMPHostTimeout_Object=MibTableColumn
swL2IGMPHostTimeout=_SwL2IGMPHostTimeout_Object((1,3,6,1,4,1,171,11,63,11,2,7,3,1,6),_SwL2IGMPHostTimeout_Type())
swL2IGMPHostTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPHostTimeout.setStatus(_A)
class _SwL2IGMPRouteTimeout_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPRouteTimeout_Type.__name__=_B
_SwL2IGMPRouteTimeout_Object=MibTableColumn
swL2IGMPRouteTimeout=_SwL2IGMPRouteTimeout_Object((1,3,6,1,4,1,171,11,63,11,2,7,3,1,7),_SwL2IGMPRouteTimeout_Type())
swL2IGMPRouteTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouteTimeout.setStatus(_A)
class _SwL2IGMPLeaveTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPLeaveTimer_Type.__name__=_B
_SwL2IGMPLeaveTimer_Object=MibTableColumn
swL2IGMPLeaveTimer=_SwL2IGMPLeaveTimer_Object((1,3,6,1,4,1,171,11,63,11,2,7,3,1,8),_SwL2IGMPLeaveTimer_Type())
swL2IGMPLeaveTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPLeaveTimer.setStatus(_A)
class _SwL2IGMPQueryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2IGMPQueryState_Type.__name__=_B
_SwL2IGMPQueryState_Object=MibTableColumn
swL2IGMPQueryState=_SwL2IGMPQueryState_Object((1,3,6,1,4,1,171,11,63,11,2,7,3,1,9),_SwL2IGMPQueryState_Type())
swL2IGMPQueryState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPQueryState.setStatus(_A)
class _SwL2IGMPCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('querier',2),('non-querier',3)))
_SwL2IGMPCurrentState_Type.__name__=_B
_SwL2IGMPCurrentState_Object=MibTableColumn
swL2IGMPCurrentState=_SwL2IGMPCurrentState_Object((1,3,6,1,4,1,171,11,63,11,2,7,3,1,10),_SwL2IGMPCurrentState_Type())
swL2IGMPCurrentState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPCurrentState.setStatus(_A)
class _SwL2IGMPCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_L,2),(_N,3)))
_SwL2IGMPCtrlState_Type.__name__=_B
_SwL2IGMPCtrlState_Object=MibTableColumn
swL2IGMPCtrlState=_SwL2IGMPCtrlState_Object((1,3,6,1,4,1,171,11,63,11,2,7,3,1,11),_SwL2IGMPCtrlState_Type())
swL2IGMPCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPCtrlState.setStatus(_A)
class _SwL2IGMPFastLeave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_L,2),(_N,3)))
_SwL2IGMPFastLeave_Type.__name__=_B
_SwL2IGMPFastLeave_Object=MibTableColumn
swL2IGMPFastLeave=_SwL2IGMPFastLeave_Object((1,3,6,1,4,1,171,11,63,11,2,7,3,1,12),_SwL2IGMPFastLeave_Type())
swL2IGMPFastLeave.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPFastLeave.setStatus(_A)
class _SwL2IGMPDynIPMultVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2IGMPDynIPMultVlanState_Type.__name__=_B
_SwL2IGMPDynIPMultVlanState_Object=MibTableColumn
swL2IGMPDynIPMultVlanState=_SwL2IGMPDynIPMultVlanState_Object((1,3,6,1,4,1,171,11,63,11,2,7,3,1,13),_SwL2IGMPDynIPMultVlanState_Type())
swL2IGMPDynIPMultVlanState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPDynIPMultVlanState.setStatus(_A)
class _SwL2IGMPDynIPMultVlanAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2IGMPDynIPMultVlanAge_Type.__name__=_B
_SwL2IGMPDynIPMultVlanAge_Object=MibTableColumn
swL2IGMPDynIPMultVlanAge=_SwL2IGMPDynIPMultVlanAge_Object((1,3,6,1,4,1,171,11,63,11,2,7,3,1,14),_SwL2IGMPDynIPMultVlanAge_Type())
swL2IGMPDynIPMultVlanAge.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPDynIPMultVlanAge.setStatus(_A)
_SwL2IGMPQueryInfoTable_Object=MibTable
swL2IGMPQueryInfoTable=_SwL2IGMPQueryInfoTable_Object((1,3,6,1,4,1,171,11,63,11,2,7,4))
if mibBuilder.loadTexts:swL2IGMPQueryInfoTable.setStatus(_A)
_SwL2IGMPQueryInfoEntry_Object=MibTableRow
swL2IGMPQueryInfoEntry=_SwL2IGMPQueryInfoEntry_Object((1,3,6,1,4,1,171,11,63,11,2,7,4,1))
swL2IGMPQueryInfoEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:swL2IGMPQueryInfoEntry.setStatus(_A)
class _SwL2IGMPInfoVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoVid_Type.__name__=_B
_SwL2IGMPInfoVid_Object=MibTableColumn
swL2IGMPInfoVid=_SwL2IGMPInfoVid_Object((1,3,6,1,4,1,171,11,63,11,2,7,4,1,1),_SwL2IGMPInfoVid_Type())
swL2IGMPInfoVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPInfoVid.setStatus(_A)
class _SwL2IGMPInfoQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoQueryCount_Type.__name__=_B
_SwL2IGMPInfoQueryCount_Object=MibTableColumn
swL2IGMPInfoQueryCount=_SwL2IGMPInfoQueryCount_Object((1,3,6,1,4,1,171,11,63,11,2,7,4,1,2),_SwL2IGMPInfoQueryCount_Type())
swL2IGMPInfoQueryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPInfoQueryCount.setStatus(_A)
class _SwL2IGMPInfoTxQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoTxQueryCount_Type.__name__=_B
_SwL2IGMPInfoTxQueryCount_Object=MibTableColumn
swL2IGMPInfoTxQueryCount=_SwL2IGMPInfoTxQueryCount_Object((1,3,6,1,4,1,171,11,63,11,2,7,4,1,3),_SwL2IGMPInfoTxQueryCount_Type())
swL2IGMPInfoTxQueryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPInfoTxQueryCount.setStatus(_A)
_SwL2IGMPInfoTable_Object=MibTable
swL2IGMPInfoTable=_SwL2IGMPInfoTable_Object((1,3,6,1,4,1,171,11,63,11,2,7,5))
if mibBuilder.loadTexts:swL2IGMPInfoTable.setStatus(_A)
_SwL2IGMPInfoEntry_Object=MibTableRow
swL2IGMPInfoEntry=_SwL2IGMPInfoEntry_Object((1,3,6,1,4,1,171,11,63,11,2,7,5,1))
swL2IGMPInfoEntry.setIndexNames((0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:swL2IGMPInfoEntry.setStatus(_A)
class _SwL2IGMPVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPVid_Type.__name__=_B
_SwL2IGMPVid_Object=MibTableColumn
swL2IGMPVid=_SwL2IGMPVid_Object((1,3,6,1,4,1,171,11,63,11,2,7,5,1,1),_SwL2IGMPVid_Type())
swL2IGMPVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPVid.setStatus(_A)
_SwL2IGMPGroupIpAddr_Type=IpAddress
_SwL2IGMPGroupIpAddr_Object=MibTableColumn
swL2IGMPGroupIpAddr=_SwL2IGMPGroupIpAddr_Object((1,3,6,1,4,1,171,11,63,11,2,7,5,1,2),_SwL2IGMPGroupIpAddr_Type())
swL2IGMPGroupIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPGroupIpAddr.setStatus(_A)
_SwL2IGMPMacAddr_Type=MacAddress
_SwL2IGMPMacAddr_Object=MibTableColumn
swL2IGMPMacAddr=_SwL2IGMPMacAddr_Object((1,3,6,1,4,1,171,11,63,11,2,7,5,1,3),_SwL2IGMPMacAddr_Type())
swL2IGMPMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMacAddr.setStatus(_A)
_SwL2IGMPPortMap_Type=PortList
_SwL2IGMPPortMap_Object=MibTableColumn
swL2IGMPPortMap=_SwL2IGMPPortMap_Object((1,3,6,1,4,1,171,11,63,11,2,7,5,1,4),_SwL2IGMPPortMap_Type())
swL2IGMPPortMap.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPPortMap.setStatus(_A)
class _SwL2IGMPIpGroupReportCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPIpGroupReportCount_Type.__name__=_B
_SwL2IGMPIpGroupReportCount_Object=MibTableColumn
swL2IGMPIpGroupReportCount=_SwL2IGMPIpGroupReportCount_Object((1,3,6,1,4,1,171,11,63,11,2,7,5,1,5),_SwL2IGMPIpGroupReportCount_Type())
swL2IGMPIpGroupReportCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPIpGroupReportCount.setStatus(_A)
_SwL2IGMPRouterPortTable_Object=MibTable
swL2IGMPRouterPortTable=_SwL2IGMPRouterPortTable_Object((1,3,6,1,4,1,171,11,63,11,2,7,6))
if mibBuilder.loadTexts:swL2IGMPRouterPortTable.setStatus(_A)
_SwL2IGMPRouterPortEntry_Object=MibTableRow
swL2IGMPRouterPortEntry=_SwL2IGMPRouterPortEntry_Object((1,3,6,1,4,1,171,11,63,11,2,7,6,1))
swL2IGMPRouterPortEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:swL2IGMPRouterPortEntry.setStatus(_A)
class _SwL2IGMPRouterPortVlanid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2IGMPRouterPortVlanid_Type.__name__=_B
_SwL2IGMPRouterPortVlanid_Object=MibTableColumn
swL2IGMPRouterPortVlanid=_SwL2IGMPRouterPortVlanid_Object((1,3,6,1,4,1,171,11,63,11,2,7,6,1,1),_SwL2IGMPRouterPortVlanid_Type())
swL2IGMPRouterPortVlanid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterPortVlanid.setStatus(_A)
class _SwL2IGMPRouterPortVlanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2IGMPRouterPortVlanName_Type.__name__=_Z
_SwL2IGMPRouterPortVlanName_Object=MibTableColumn
swL2IGMPRouterPortVlanName=_SwL2IGMPRouterPortVlanName_Object((1,3,6,1,4,1,171,11,63,11,2,7,6,1,2),_SwL2IGMPRouterPortVlanName_Type())
swL2IGMPRouterPortVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterPortVlanName.setStatus(_A)
_SwL2IGMPRouterPortStaticPortList_Type=PortList
_SwL2IGMPRouterPortStaticPortList_Object=MibTableColumn
swL2IGMPRouterPortStaticPortList=_SwL2IGMPRouterPortStaticPortList_Object((1,3,6,1,4,1,171,11,63,11,2,7,6,1,3),_SwL2IGMPRouterPortStaticPortList_Type())
swL2IGMPRouterPortStaticPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouterPortStaticPortList.setStatus(_A)
_SwL2IGMPRouterPortDynamicPortList_Type=PortList
_SwL2IGMPRouterPortDynamicPortList_Object=MibTableColumn
swL2IGMPRouterPortDynamicPortList=_SwL2IGMPRouterPortDynamicPortList_Object((1,3,6,1,4,1,171,11,63,11,2,7,6,1,4),_SwL2IGMPRouterPortDynamicPortList_Type())
swL2IGMPRouterPortDynamicPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterPortDynamicPortList.setStatus(_A)
_SwL2IGMPRouterPortForbiddenPortList_Type=PortList
_SwL2IGMPRouterPortForbiddenPortList_Object=MibTableColumn
swL2IGMPRouterPortForbiddenPortList=_SwL2IGMPRouterPortForbiddenPortList_Object((1,3,6,1,4,1,171,11,63,11,2,7,6,1,5),_SwL2IGMPRouterPortForbiddenPortList_Type())
swL2IGMPRouterPortForbiddenPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouterPortForbiddenPortList.setStatus(_A)
_SwL2IGMPAccessAuthTable_Object=MibTable
swL2IGMPAccessAuthTable=_SwL2IGMPAccessAuthTable_Object((1,3,6,1,4,1,171,11,63,11,2,7,7))
if mibBuilder.loadTexts:swL2IGMPAccessAuthTable.setStatus(_A)
_SwL2IGMPAccessAuthEntry_Object=MibTableRow
swL2IGMPAccessAuthEntry=_SwL2IGMPAccessAuthEntry_Object((1,3,6,1,4,1,171,11,63,11,2,7,7,1))
swL2IGMPAccessAuthEntry.setIndexNames((0,_E,_s))
if mibBuilder.loadTexts:swL2IGMPAccessAuthEntry.setStatus(_A)
_SwL2IGMPAccessAuthPort_Type=Integer32
_SwL2IGMPAccessAuthPort_Object=MibTableColumn
swL2IGMPAccessAuthPort=_SwL2IGMPAccessAuthPort_Object((1,3,6,1,4,1,171,11,63,11,2,7,7,1,1),_SwL2IGMPAccessAuthPort_Type())
swL2IGMPAccessAuthPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPAccessAuthPort.setStatus(_A)
class _SwL2IGMPAccessAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwL2IGMPAccessAuthState_Type.__name__=_B
_SwL2IGMPAccessAuthState_Object=MibTableColumn
swL2IGMPAccessAuthState=_SwL2IGMPAccessAuthState_Object((1,3,6,1,4,1,171,11,63,11,2,7,7,1,2),_SwL2IGMPAccessAuthState_Type())
swL2IGMPAccessAuthState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPAccessAuthState.setStatus(_A)
_SwL2IGMPMulticastVlanTable_Object=MibTable
swL2IGMPMulticastVlanTable=_SwL2IGMPMulticastVlanTable_Object((1,3,6,1,4,1,171,11,63,11,2,7,8))
if mibBuilder.loadTexts:swL2IGMPMulticastVlanTable.setStatus(_A)
_SwL2IGMPMulticastVlanEntry_Object=MibTableRow
swL2IGMPMulticastVlanEntry=_SwL2IGMPMulticastVlanEntry_Object((1,3,6,1,4,1,171,11,63,11,2,7,8,1))
swL2IGMPMulticastVlanEntry.setIndexNames((0,_E,_t))
if mibBuilder.loadTexts:swL2IGMPMulticastVlanEntry.setStatus(_A)
class _SwL2IGMPMulticastVlanid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_SwL2IGMPMulticastVlanid_Type.__name__=_B
_SwL2IGMPMulticastVlanid_Object=MibTableColumn
swL2IGMPMulticastVlanid=_SwL2IGMPMulticastVlanid_Object((1,3,6,1,4,1,171,11,63,11,2,7,8,1,1),_SwL2IGMPMulticastVlanid_Type())
swL2IGMPMulticastVlanid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanid.setStatus(_A)
class _SwL2IGMPMulticastVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2IGMPMulticastVlanName_Type.__name__=_K
_SwL2IGMPMulticastVlanName_Object=MibTableColumn
swL2IGMPMulticastVlanName=_SwL2IGMPMulticastVlanName_Object((1,3,6,1,4,1,171,11,63,11,2,7,8,1,2),_SwL2IGMPMulticastVlanName_Type())
swL2IGMPMulticastVlanName.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanName.setStatus(_A)
_SwL2IGMPMulticastVlanSourcePort_Type=PortList
_SwL2IGMPMulticastVlanSourcePort_Object=MibTableColumn
swL2IGMPMulticastVlanSourcePort=_SwL2IGMPMulticastVlanSourcePort_Object((1,3,6,1,4,1,171,11,63,11,2,7,8,1,3),_SwL2IGMPMulticastVlanSourcePort_Type())
swL2IGMPMulticastVlanSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanSourcePort.setStatus(_A)
_SwL2IGMPMulticastVlanMemberPort_Type=PortList
_SwL2IGMPMulticastVlanMemberPort_Object=MibTableColumn
swL2IGMPMulticastVlanMemberPort=_SwL2IGMPMulticastVlanMemberPort_Object((1,3,6,1,4,1,171,11,63,11,2,7,8,1,4),_SwL2IGMPMulticastVlanMemberPort_Type())
swL2IGMPMulticastVlanMemberPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanMemberPort.setStatus(_A)
_SwL2IGMPMulticastVlanTagMemberPort_Type=PortList
_SwL2IGMPMulticastVlanTagMemberPort_Object=MibTableColumn
swL2IGMPMulticastVlanTagMemberPort=_SwL2IGMPMulticastVlanTagMemberPort_Object((1,3,6,1,4,1,171,11,63,11,2,7,8,1,5),_SwL2IGMPMulticastVlanTagMemberPort_Type())
swL2IGMPMulticastVlanTagMemberPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanTagMemberPort.setStatus(_A)
class _SwL2IGMPMulticastVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2IGMPMulticastVlanState_Type.__name__=_B
_SwL2IGMPMulticastVlanState_Object=MibTableColumn
swL2IGMPMulticastVlanState=_SwL2IGMPMulticastVlanState_Object((1,3,6,1,4,1,171,11,63,11,2,7,8,1,6),_SwL2IGMPMulticastVlanState_Type())
swL2IGMPMulticastVlanState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanState.setStatus(_A)
_SwL2IGMPMulticastVlanReplaceSourceIp_Type=IpAddress
_SwL2IGMPMulticastVlanReplaceSourceIp_Object=MibTableColumn
swL2IGMPMulticastVlanReplaceSourceIp=_SwL2IGMPMulticastVlanReplaceSourceIp_Object((1,3,6,1,4,1,171,11,63,11,2,7,8,1,7),_SwL2IGMPMulticastVlanReplaceSourceIp_Type())
swL2IGMPMulticastVlanReplaceSourceIp.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanReplaceSourceIp.setStatus(_A)
_SwL2IGMPMulticastVlanRowStatus_Type=RowStatus
_SwL2IGMPMulticastVlanRowStatus_Object=MibTableColumn
swL2IGMPMulticastVlanRowStatus=_SwL2IGMPMulticastVlanRowStatus_Object((1,3,6,1,4,1,171,11,63,11,2,7,8,1,8),_SwL2IGMPMulticastVlanRowStatus_Type())
swL2IGMPMulticastVlanRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanRowStatus.setStatus(_A)
class _SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_W,2)))
_SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Type.__name__=_B
_SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Object=MibTableColumn
swL2IGMPMulticastVlanRemoveAllMcastAddrListAction=_SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Object((1,3,6,1,4,1,171,11,63,11,2,7,8,1,9),_SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Type())
swL2IGMPMulticastVlanRemoveAllMcastAddrListAction.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanRemoveAllMcastAddrListAction.setStatus(_A)
_SwL2IGMPMulticastVlanUntagSourcePort_Type=PortList
_SwL2IGMPMulticastVlanUntagSourcePort_Object=MibTableColumn
swL2IGMPMulticastVlanUntagSourcePort=_SwL2IGMPMulticastVlanUntagSourcePort_Object((1,3,6,1,4,1,171,11,63,11,2,7,8,1,10),_SwL2IGMPMulticastVlanUntagSourcePort_Type())
swL2IGMPMulticastVlanUntagSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanUntagSourcePort.setStatus(_A)
class _SwL2IGMPMulticastVlanRemapPriority_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_SwL2IGMPMulticastVlanRemapPriority_Type.__name__=_B
_SwL2IGMPMulticastVlanRemapPriority_Object=MibTableColumn
swL2IGMPMulticastVlanRemapPriority=_SwL2IGMPMulticastVlanRemapPriority_Object((1,3,6,1,4,1,171,11,63,11,2,7,8,1,11),_SwL2IGMPMulticastVlanRemapPriority_Type())
swL2IGMPMulticastVlanRemapPriority.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanRemapPriority.setStatus(_A)
class _SwL2IGMPMulticastVlanReplacePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_SwL2IGMPMulticastVlanReplacePriority_Type.__name__=_B
_SwL2IGMPMulticastVlanReplacePriority_Object=MibTableColumn
swL2IGMPMulticastVlanReplacePriority=_SwL2IGMPMulticastVlanReplacePriority_Object((1,3,6,1,4,1,171,11,63,11,2,7,8,1,12),_SwL2IGMPMulticastVlanReplacePriority_Type())
swL2IGMPMulticastVlanReplacePriority.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanReplacePriority.setStatus(_A)
_SwL2IGMPMulticastVlanGroupTable_Object=MibTable
swL2IGMPMulticastVlanGroupTable=_SwL2IGMPMulticastVlanGroupTable_Object((1,3,6,1,4,1,171,11,63,11,2,7,9))
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupTable.setStatus(_A)
_SwL2IGMPMulticastVlanGroupEntry_Object=MibTableRow
swL2IGMPMulticastVlanGroupEntry=_SwL2IGMPMulticastVlanGroupEntry_Object((1,3,6,1,4,1,171,11,63,11,2,7,9,1))
swL2IGMPMulticastVlanGroupEntry.setIndexNames((0,_E,_u),(0,_E,_v),(0,_E,_w))
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupEntry.setStatus(_A)
class _SwL2IGMPMulticastVlanGroupVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2IGMPMulticastVlanGroupVid_Type.__name__=_B
_SwL2IGMPMulticastVlanGroupVid_Object=MibTableColumn
swL2IGMPMulticastVlanGroupVid=_SwL2IGMPMulticastVlanGroupVid_Object((1,3,6,1,4,1,171,11,63,11,2,7,9,1,1),_SwL2IGMPMulticastVlanGroupVid_Type())
swL2IGMPMulticastVlanGroupVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupVid.setStatus(_A)
_SwL2IGMPMulticastVlanGroupFromIp_Type=IpAddress
_SwL2IGMPMulticastVlanGroupFromIp_Object=MibTableColumn
swL2IGMPMulticastVlanGroupFromIp=_SwL2IGMPMulticastVlanGroupFromIp_Object((1,3,6,1,4,1,171,11,63,11,2,7,9,1,2),_SwL2IGMPMulticastVlanGroupFromIp_Type())
swL2IGMPMulticastVlanGroupFromIp.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupFromIp.setStatus(_A)
_SwL2IGMPMulticastVlanGroupToIp_Type=IpAddress
_SwL2IGMPMulticastVlanGroupToIp_Object=MibTableColumn
swL2IGMPMulticastVlanGroupToIp=_SwL2IGMPMulticastVlanGroupToIp_Object((1,3,6,1,4,1,171,11,63,11,2,7,9,1,3),_SwL2IGMPMulticastVlanGroupToIp_Type())
swL2IGMPMulticastVlanGroupToIp.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupToIp.setStatus(_A)
_SwL2IGMPMulticastVlanGroupStatus_Type=RowStatus
_SwL2IGMPMulticastVlanGroupStatus_Object=MibTableColumn
swL2IGMPMulticastVlanGroupStatus=_SwL2IGMPMulticastVlanGroupStatus_Object((1,3,6,1,4,1,171,11,63,11,2,7,9,1,4),_SwL2IGMPMulticastVlanGroupStatus_Type())
swL2IGMPMulticastVlanGroupStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupStatus.setStatus(_A)
_SwL2IGMPv3Table_Object=MibTable
swL2IGMPv3Table=_SwL2IGMPv3Table_Object((1,3,6,1,4,1,171,11,63,11,2,7,10))
if mibBuilder.loadTexts:swL2IGMPv3Table.setStatus(_A)
_SwL2IGMPv3Entry_Object=MibTableRow
swL2IGMPv3Entry=_SwL2IGMPv3Entry_Object((1,3,6,1,4,1,171,11,63,11,2,7,10,1))
swL2IGMPv3Entry.setIndexNames((0,_E,_U),(0,_E,_V),(0,_E,_x))
if mibBuilder.loadTexts:swL2IGMPv3Entry.setStatus(_A)
_SwL2IGMPv3SourceIPAddr_Type=IpAddress
_SwL2IGMPv3SourceIPAddr_Object=MibTableColumn
swL2IGMPv3SourceIPAddr=_SwL2IGMPv3SourceIPAddr_Object((1,3,6,1,4,1,171,11,63,11,2,7,10,1,1),_SwL2IGMPv3SourceIPAddr_Type())
swL2IGMPv3SourceIPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPv3SourceIPAddr.setStatus(_A)
class _SwL2IGMPv3Forwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2IGMPv3Forwarding_Type.__name__=_B
_SwL2IGMPv3Forwarding_Object=MibTableColumn
swL2IGMPv3Forwarding=_SwL2IGMPv3Forwarding_Object((1,3,6,1,4,1,171,11,63,11,2,7,10,1,2),_SwL2IGMPv3Forwarding_Type())
swL2IGMPv3Forwarding.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPv3Forwarding.setStatus(_A)
_SwL2IGMPv3ExpireTimer_Type=Integer32
_SwL2IGMPv3ExpireTimer_Object=MibTableColumn
swL2IGMPv3ExpireTimer=_SwL2IGMPv3ExpireTimer_Object((1,3,6,1,4,1,171,11,63,11,2,7,10,1,3),_SwL2IGMPv3ExpireTimer_Type())
swL2IGMPv3ExpireTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPv3ExpireTimer.setStatus(_A)
_SwIGMPSnoopingGroupTable_Object=MibTable
swIGMPSnoopingGroupTable=_SwIGMPSnoopingGroupTable_Object((1,3,6,1,4,1,171,11,63,11,2,7,11))
if mibBuilder.loadTexts:swIGMPSnoopingGroupTable.setStatus(_A)
_SwIGMPSnoopingGroupEntry_Object=MibTableRow
swIGMPSnoopingGroupEntry=_SwIGMPSnoopingGroupEntry_Object((1,3,6,1,4,1,171,11,63,11,2,7,11,1))
swIGMPSnoopingGroupEntry.setIndexNames((0,_E,_y),(0,_E,_z),(0,_E,_A0))
if mibBuilder.loadTexts:swIGMPSnoopingGroupEntry.setStatus(_A)
class _SwIGMPSnoopingGroupVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwIGMPSnoopingGroupVid_Type.__name__=_B
_SwIGMPSnoopingGroupVid_Object=MibTableColumn
swIGMPSnoopingGroupVid=_SwIGMPSnoopingGroupVid_Object((1,3,6,1,4,1,171,11,63,11,2,7,11,1,1),_SwIGMPSnoopingGroupVid_Type())
swIGMPSnoopingGroupVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupVid.setStatus(_A)
_SwIGMPSnoopingGroupGroupAddr_Type=IpAddress
_SwIGMPSnoopingGroupGroupAddr_Object=MibTableColumn
swIGMPSnoopingGroupGroupAddr=_SwIGMPSnoopingGroupGroupAddr_Object((1,3,6,1,4,1,171,11,63,11,2,7,11,1,2),_SwIGMPSnoopingGroupGroupAddr_Type())
swIGMPSnoopingGroupGroupAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupGroupAddr.setStatus(_A)
_SwIGMPSnoopingGroupSourceAddr_Type=IpAddress
_SwIGMPSnoopingGroupSourceAddr_Object=MibTableColumn
swIGMPSnoopingGroupSourceAddr=_SwIGMPSnoopingGroupSourceAddr_Object((1,3,6,1,4,1,171,11,63,11,2,7,11,1,3),_SwIGMPSnoopingGroupSourceAddr_Type())
swIGMPSnoopingGroupSourceAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupSourceAddr.setStatus(_A)
_SwIGMPSnoopingGroupIncludePortMap_Type=PortList
_SwIGMPSnoopingGroupIncludePortMap_Object=MibTableColumn
swIGMPSnoopingGroupIncludePortMap=_SwIGMPSnoopingGroupIncludePortMap_Object((1,3,6,1,4,1,171,11,63,11,2,7,11,1,4),_SwIGMPSnoopingGroupIncludePortMap_Type())
swIGMPSnoopingGroupIncludePortMap.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupIncludePortMap.setStatus(_A)
_SwIGMPSnoopingGroupExcludePortMap_Type=PortList
_SwIGMPSnoopingGroupExcludePortMap_Object=MibTableColumn
swIGMPSnoopingGroupExcludePortMap=_SwIGMPSnoopingGroupExcludePortMap_Object((1,3,6,1,4,1,171,11,63,11,2,7,11,1,5),_SwIGMPSnoopingGroupExcludePortMap_Type())
swIGMPSnoopingGroupExcludePortMap.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupExcludePortMap.setStatus(_A)
_SwIGMPSnoopingGroupReportCount_Type=Integer32
_SwIGMPSnoopingGroupReportCount_Object=MibTableColumn
swIGMPSnoopingGroupReportCount=_SwIGMPSnoopingGroupReportCount_Object((1,3,6,1,4,1,171,11,63,11,2,7,11,1,6),_SwIGMPSnoopingGroupReportCount_Type())
swIGMPSnoopingGroupReportCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupReportCount.setStatus(_A)
_SwIGMPSnoopingGroupUpTime_Type=TimeTicks
_SwIGMPSnoopingGroupUpTime_Object=MibTableColumn
swIGMPSnoopingGroupUpTime=_SwIGMPSnoopingGroupUpTime_Object((1,3,6,1,4,1,171,11,63,11,2,7,11,1,7),_SwIGMPSnoopingGroupUpTime_Type())
swIGMPSnoopingGroupUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupUpTime.setStatus(_A)
_SwIGMPSnoopingGroupExpiryTime_Type=TimeTicks
_SwIGMPSnoopingGroupExpiryTime_Object=MibTableColumn
swIGMPSnoopingGroupExpiryTime=_SwIGMPSnoopingGroupExpiryTime_Object((1,3,6,1,4,1,171,11,63,11,2,7,11,1,8),_SwIGMPSnoopingGroupExpiryTime_Type())
swIGMPSnoopingGroupExpiryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupExpiryTime.setStatus(_A)
_SwIGMPSnoopingGroupRouterPorts_Type=PortList
_SwIGMPSnoopingGroupRouterPorts_Object=MibTableColumn
swIGMPSnoopingGroupRouterPorts=_SwIGMPSnoopingGroupRouterPorts_Object((1,3,6,1,4,1,171,11,63,11,2,7,11,1,9),_SwIGMPSnoopingGroupRouterPorts_Type())
swIGMPSnoopingGroupRouterPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPSnoopingGroupRouterPorts.setStatus(_A)
_SwL2IGMPDynIpMultMgmt_ObjectIdentity=ObjectIdentity
swL2IGMPDynIpMultMgmt=_SwL2IGMPDynIpMultMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,7,12))
_SwL2IGMPDynIPMultMaxEntry_Type=Integer32
_SwL2IGMPDynIPMultMaxEntry_Object=MibScalar
swL2IGMPDynIPMultMaxEntry=_SwL2IGMPDynIPMultMaxEntry_Object((1,3,6,1,4,1,171,11,63,11,2,7,12,1),_SwL2IGMPDynIPMultMaxEntry_Type())
swL2IGMPDynIPMultMaxEntry.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPDynIPMultMaxEntry.setStatus(_A)
_SwL2IGMPSnoopingClearDynIpMult_ObjectIdentity=ObjectIdentity
swL2IGMPSnoopingClearDynIpMult=_SwL2IGMPSnoopingClearDynIpMult_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,7,12,2))
_SwL2IGMPSnoopingClearDynIpMultVID_Type=VlanId
_SwL2IGMPSnoopingClearDynIpMultVID_Object=MibScalar
swL2IGMPSnoopingClearDynIpMultVID=_SwL2IGMPSnoopingClearDynIpMultVID_Object((1,3,6,1,4,1,171,11,63,11,2,7,12,2,1),_SwL2IGMPSnoopingClearDynIpMultVID_Type())
swL2IGMPSnoopingClearDynIpMultVID.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPSnoopingClearDynIpMultVID.setStatus(_A)
_SwL2IGMPSnoopingClearDynIpMultIP_Type=IpAddress
_SwL2IGMPSnoopingClearDynIpMultIP_Object=MibScalar
swL2IGMPSnoopingClearDynIpMultIP=_SwL2IGMPSnoopingClearDynIpMultIP_Object((1,3,6,1,4,1,171,11,63,11,2,7,12,2,2),_SwL2IGMPSnoopingClearDynIpMultIP_Type())
swL2IGMPSnoopingClearDynIpMultIP.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPSnoopingClearDynIpMultIP.setStatus(_A)
class _SwL2IGMPSnoopingClearDynIpMultAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('all',1),('vlan',2),('group',3),(_F,4)))
_SwL2IGMPSnoopingClearDynIpMultAction_Type.__name__=_B
_SwL2IGMPSnoopingClearDynIpMultAction_Object=MibScalar
swL2IGMPSnoopingClearDynIpMultAction=_SwL2IGMPSnoopingClearDynIpMultAction_Object((1,3,6,1,4,1,171,11,63,11,2,7,12,2,3),_SwL2IGMPSnoopingClearDynIpMultAction_Type())
swL2IGMPSnoopingClearDynIpMultAction.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPSnoopingClearDynIpMultAction.setStatus(_A)
_SwL2TrafficSegMgmt_ObjectIdentity=ObjectIdentity
swL2TrafficSegMgmt=_SwL2TrafficSegMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,12))
_SwL2TrafficSegTable_Object=MibTable
swL2TrafficSegTable=_SwL2TrafficSegTable_Object((1,3,6,1,4,1,171,11,63,11,2,12,1))
if mibBuilder.loadTexts:swL2TrafficSegTable.setStatus(_A)
_SwL2TrafficSegEntry_Object=MibTableRow
swL2TrafficSegEntry=_SwL2TrafficSegEntry_Object((1,3,6,1,4,1,171,11,63,11,2,12,1,1))
swL2TrafficSegEntry.setIndexNames((0,_E,_A1))
if mibBuilder.loadTexts:swL2TrafficSegEntry.setStatus(_A)
class _SwL2TrafficSegPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrafficSegPort_Type.__name__=_B
_SwL2TrafficSegPort_Object=MibTableColumn
swL2TrafficSegPort=_SwL2TrafficSegPort_Object((1,3,6,1,4,1,171,11,63,11,2,12,1,1,1),_SwL2TrafficSegPort_Type())
swL2TrafficSegPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrafficSegPort.setStatus(_A)
_SwL2TrafficSegForwardPorts_Type=PortList
_SwL2TrafficSegForwardPorts_Object=MibTableColumn
swL2TrafficSegForwardPorts=_SwL2TrafficSegForwardPorts_Object((1,3,6,1,4,1,171,11,63,11,2,12,1,1,2),_SwL2TrafficSegForwardPorts_Type())
swL2TrafficSegForwardPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrafficSegForwardPorts.setStatus(_A)
_SwL2PortSecurityMgmt_ObjectIdentity=ObjectIdentity
swL2PortSecurityMgmt=_SwL2PortSecurityMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,15))
_SwL2PortSecurityControlTable_Object=MibTable
swL2PortSecurityControlTable=_SwL2PortSecurityControlTable_Object((1,3,6,1,4,1,171,11,63,11,2,15,1))
if mibBuilder.loadTexts:swL2PortSecurityControlTable.setStatus(_A)
_SwL2PortSecurityControlEntry_Object=MibTableRow
swL2PortSecurityControlEntry=_SwL2PortSecurityControlEntry_Object((1,3,6,1,4,1,171,11,63,11,2,15,1,1))
swL2PortSecurityControlEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:swL2PortSecurityControlEntry.setStatus(_A)
class _SwL2PortSecurityPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2PortSecurityPortIndex_Type.__name__=_B
_SwL2PortSecurityPortIndex_Object=MibTableColumn
swL2PortSecurityPortIndex=_SwL2PortSecurityPortIndex_Object((1,3,6,1,4,1,171,11,63,11,2,15,1,1,1),_SwL2PortSecurityPortIndex_Type())
swL2PortSecurityPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityPortIndex.setStatus(_A)
class _SwL2PortSecurityMaxLernAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_SwL2PortSecurityMaxLernAddr_Type.__name__=_B
_SwL2PortSecurityMaxLernAddr_Object=MibTableColumn
swL2PortSecurityMaxLernAddr=_SwL2PortSecurityMaxLernAddr_Object((1,3,6,1,4,1,171,11,63,11,2,15,1,1,2),_SwL2PortSecurityMaxLernAddr_Type())
swL2PortSecurityMaxLernAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityMaxLernAddr.setStatus(_A)
class _SwL2PortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('permanent',2),('deleteOnTimeout',3),('deleteOnReset',4)))
_SwL2PortSecurityMode_Type.__name__=_B
_SwL2PortSecurityMode_Object=MibTableColumn
swL2PortSecurityMode=_SwL2PortSecurityMode_Object((1,3,6,1,4,1,171,11,63,11,2,15,1,1,3),_SwL2PortSecurityMode_Type())
swL2PortSecurityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityMode.setStatus(_A)
class _SwL2PortSecurityAdmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_L,3)))
_SwL2PortSecurityAdmState_Type.__name__=_B
_SwL2PortSecurityAdmState_Object=MibTableColumn
swL2PortSecurityAdmState=_SwL2PortSecurityAdmState_Object((1,3,6,1,4,1,171,11,63,11,2,15,1,1,4),_SwL2PortSecurityAdmState_Type())
swL2PortSecurityAdmState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityAdmState.setStatus(_A)
class _SwL2PortSecurityTrapLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_L,3)))
_SwL2PortSecurityTrapLogState_Type.__name__=_B
_SwL2PortSecurityTrapLogState_Object=MibScalar
swL2PortSecurityTrapLogState=_SwL2PortSecurityTrapLogState_Object((1,3,6,1,4,1,171,11,63,11,2,15,2),_SwL2PortSecurityTrapLogState_Type())
swL2PortSecurityTrapLogState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityTrapLogState.setStatus(_A)
_SwL2PortSecurityDelCtrl_ObjectIdentity=ObjectIdentity
swL2PortSecurityDelCtrl=_SwL2PortSecurityDelCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,15,3))
class _SwL2PortSecurityDelVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2PortSecurityDelVlanName_Type.__name__=_K
_SwL2PortSecurityDelVlanName_Object=MibScalar
swL2PortSecurityDelVlanName=_SwL2PortSecurityDelVlanName_Object((1,3,6,1,4,1,171,11,63,11,2,15,3,1),_SwL2PortSecurityDelVlanName_Type())
swL2PortSecurityDelVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityDelVlanName.setStatus(_A)
class _SwL2PortSecurityDelPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,768))
_SwL2PortSecurityDelPort_Type.__name__=_B
_SwL2PortSecurityDelPort_Object=MibScalar
swL2PortSecurityDelPort=_SwL2PortSecurityDelPort_Object((1,3,6,1,4,1,171,11,63,11,2,15,3,2),_SwL2PortSecurityDelPort_Type())
swL2PortSecurityDelPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityDelPort.setStatus(_A)
_SwL2PortSecurityDelMacAddress_Type=MacAddress
_SwL2PortSecurityDelMacAddress_Object=MibScalar
swL2PortSecurityDelMacAddress=_SwL2PortSecurityDelMacAddress_Object((1,3,6,1,4,1,171,11,63,11,2,15,3,3),_SwL2PortSecurityDelMacAddress_Type())
swL2PortSecurityDelMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityDelMacAddress.setStatus(_A)
class _SwL2PortSecurityDelActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_W,2)))
_SwL2PortSecurityDelActivity_Type.__name__=_B
_SwL2PortSecurityDelActivity_Object=MibScalar
swL2PortSecurityDelActivity=_SwL2PortSecurityDelActivity_Object((1,3,6,1,4,1,171,11,63,11,2,15,3,4),_SwL2PortSecurityDelActivity_Type())
swL2PortSecurityDelActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityDelActivity.setStatus(_A)
_SwL2CosMgmt_ObjectIdentity=ObjectIdentity
swL2CosMgmt=_SwL2CosMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,17))
_SwL2CosPriorityCtrl_ObjectIdentity=ObjectIdentity
swL2CosPriorityCtrl=_SwL2CosPriorityCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,17,3))
_SwL2CosPriorityTable_Object=MibTable
swL2CosPriorityTable=_SwL2CosPriorityTable_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,1))
if mibBuilder.loadTexts:swL2CosPriorityTable.setStatus(_A)
_SwL2CosPriorityEntry_Object=MibTableRow
swL2CosPriorityEntry=_SwL2CosPriorityEntry_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,1,1))
swL2CosPriorityEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:swL2CosPriorityEntry.setStatus(_A)
class _SwL2CosPriorityPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2CosPriorityPort_Type.__name__=_B
_SwL2CosPriorityPort_Object=MibTableColumn
swL2CosPriorityPort=_SwL2CosPriorityPort_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,1,1,1),_SwL2CosPriorityPort_Type())
swL2CosPriorityPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2CosPriorityPort.setStatus(_A)
class _SwL2CosPriorityPortPRI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_L,2),(_N,3)))
_SwL2CosPriorityPortPRI_Type.__name__=_B
_SwL2CosPriorityPortPRI_Object=MibTableColumn
swL2CosPriorityPortPRI=_SwL2CosPriorityPortPRI_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,1,1,2),_SwL2CosPriorityPortPRI_Type())
swL2CosPriorityPortPRI.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosPriorityPortPRI.setStatus(_A)
class _SwL2CosPriorityEtherPRI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('ether8021p',2),('macBase',3)))
_SwL2CosPriorityEtherPRI_Type.__name__=_B
_SwL2CosPriorityEtherPRI_Object=MibTableColumn
swL2CosPriorityEtherPRI=_SwL2CosPriorityEtherPRI_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,1,1,3),_SwL2CosPriorityEtherPRI_Type())
swL2CosPriorityEtherPRI.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosPriorityEtherPRI.setStatus(_A)
class _SwL2CosPriorityIpPRI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('tos',2),('dscp',3)))
_SwL2CosPriorityIpPRI_Type.__name__=_B
_SwL2CosPriorityIpPRI_Object=MibTableColumn
swL2CosPriorityIpPRI=_SwL2CosPriorityIpPRI_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,1,1,4),_SwL2CosPriorityIpPRI_Type())
swL2CosPriorityIpPRI.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosPriorityIpPRI.setStatus(_A)
class _SwL2CosPriorityNone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_SwL2CosPriorityNone_Type.__name__=_B
_SwL2CosPriorityNone_Object=MibTableColumn
swL2CosPriorityNone=_SwL2CosPriorityNone_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,1,1,5),_SwL2CosPriorityNone_Type())
swL2CosPriorityNone.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosPriorityNone.setStatus(_A)
_SwL2CosPortPRITable_Object=MibTable
swL2CosPortPRITable=_SwL2CosPortPRITable_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,2))
if mibBuilder.loadTexts:swL2CosPortPRITable.setStatus(_A)
_SwL2CosPortPRIEntry_Object=MibTableRow
swL2CosPortPRIEntry=_SwL2CosPortPRIEntry_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,2,1))
swL2CosPortPRIEntry.setIndexNames((0,_E,_A3))
if mibBuilder.loadTexts:swL2CosPortPRIEntry.setStatus(_A)
class _SwL2CosPortPRIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2CosPortPRIIndex_Type.__name__=_B
_SwL2CosPortPRIIndex_Object=MibTableColumn
swL2CosPortPRIIndex=_SwL2CosPortPRIIndex_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,2,1,1),_SwL2CosPortPRIIndex_Type())
swL2CosPortPRIIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2CosPortPRIIndex.setStatus(_A)
class _SwL2CosPortPRIClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwL2CosPortPRIClass_Type.__name__=_B
_SwL2CosPortPRIClass_Object=MibTableColumn
swL2CosPortPRIClass=_SwL2CosPortPRIClass_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,2,1,2),_SwL2CosPortPRIClass_Type())
swL2CosPortPRIClass.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosPortPRIClass.setStatus(_A)
_SwL2CosMacBasePRITable_Object=MibTable
swL2CosMacBasePRITable=_SwL2CosMacBasePRITable_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,3))
if mibBuilder.loadTexts:swL2CosMacBasePRITable.setStatus(_A)
_SwL2CosMacBasePRIEntry_Object=MibTableRow
swL2CosMacBasePRIEntry=_SwL2CosMacBasePRIEntry_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,3,1))
swL2CosMacBasePRIEntry.setIndexNames((0,_E,_A4))
if mibBuilder.loadTexts:swL2CosMacBasePRIEntry.setStatus(_A)
_SwL2CosMacBasePRIIndex_Type=MacAddress
_SwL2CosMacBasePRIIndex_Object=MibTableColumn
swL2CosMacBasePRIIndex=_SwL2CosMacBasePRIIndex_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,3,1,1),_SwL2CosMacBasePRIIndex_Type())
swL2CosMacBasePRIIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2CosMacBasePRIIndex.setStatus(_A)
class _SwL2CosMacBasePRIClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwL2CosMacBasePRIClass_Type.__name__=_B
_SwL2CosMacBasePRIClass_Object=MibTableColumn
swL2CosMacBasePRIClass=_SwL2CosMacBasePRIClass_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,3,1,2),_SwL2CosMacBasePRIClass_Type())
swL2CosMacBasePRIClass.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosMacBasePRIClass.setStatus(_A)
_SwL2CosTosPRITable_Object=MibTable
swL2CosTosPRITable=_SwL2CosTosPRITable_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,4))
if mibBuilder.loadTexts:swL2CosTosPRITable.setStatus(_A)
_SwL2CosTosPRIEntry_Object=MibTableRow
swL2CosTosPRIEntry=_SwL2CosTosPRIEntry_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,4,1))
swL2CosTosPRIEntry.setIndexNames((0,_E,_A5))
if mibBuilder.loadTexts:swL2CosTosPRIEntry.setStatus(_A)
class _SwL2CosTosPRIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2CosTosPRIIndex_Type.__name__=_B
_SwL2CosTosPRIIndex_Object=MibTableColumn
swL2CosTosPRIIndex=_SwL2CosTosPRIIndex_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,4,1,1),_SwL2CosTosPRIIndex_Type())
swL2CosTosPRIIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2CosTosPRIIndex.setStatus(_A)
class _SwL2CosTosPRIClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwL2CosTosPRIClass_Type.__name__=_B
_SwL2CosTosPRIClass_Object=MibTableColumn
swL2CosTosPRIClass=_SwL2CosTosPRIClass_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,4,1,2),_SwL2CosTosPRIClass_Type())
swL2CosTosPRIClass.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosTosPRIClass.setStatus(_A)
_SwL2CosDscpPRITable_Object=MibTable
swL2CosDscpPRITable=_SwL2CosDscpPRITable_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,5))
if mibBuilder.loadTexts:swL2CosDscpPRITable.setStatus(_A)
_SwL2CosDscpPRIEntry_Object=MibTableRow
swL2CosDscpPRIEntry=_SwL2CosDscpPRIEntry_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,5,1))
swL2CosDscpPRIEntry.setIndexNames((0,_E,_A6))
if mibBuilder.loadTexts:swL2CosDscpPRIEntry.setStatus(_A)
class _SwL2CosDscpPRIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SwL2CosDscpPRIIndex_Type.__name__=_B
_SwL2CosDscpPRIIndex_Object=MibTableColumn
swL2CosDscpPRIIndex=_SwL2CosDscpPRIIndex_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,5,1,1),_SwL2CosDscpPRIIndex_Type())
swL2CosDscpPRIIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2CosDscpPRIIndex.setStatus(_A)
class _SwL2CosDscpPRIClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwL2CosDscpPRIClass_Type.__name__=_B
_SwL2CosDscpPRIClass_Object=MibTableColumn
swL2CosDscpPRIClass=_SwL2CosDscpPRIClass_Object((1,3,6,1,4,1,171,11,63,11,2,17,3,5,1,2),_SwL2CosDscpPRIClass_Type())
swL2CosDscpPRIClass.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosDscpPRIClass.setStatus(_A)
_SwL2DhcpRelayMgmt_ObjectIdentity=ObjectIdentity
swL2DhcpRelayMgmt=_SwL2DhcpRelayMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,18))
class _SwL2DhcpRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DhcpRelayState_Type.__name__=_B
_SwL2DhcpRelayState_Object=MibScalar
swL2DhcpRelayState=_SwL2DhcpRelayState_Object((1,3,6,1,4,1,171,11,63,11,2,18,1),_SwL2DhcpRelayState_Type())
swL2DhcpRelayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayState.setStatus(_J)
class _SwL2DhcpRelayHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_SwL2DhcpRelayHopCount_Type.__name__=_B
_SwL2DhcpRelayHopCount_Object=MibScalar
swL2DhcpRelayHopCount=_SwL2DhcpRelayHopCount_Object((1,3,6,1,4,1,171,11,63,11,2,18,2),_SwL2DhcpRelayHopCount_Type())
swL2DhcpRelayHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayHopCount.setStatus(_J)
class _SwL2DhcpRelayTimeThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2DhcpRelayTimeThreshold_Type.__name__=_B
_SwL2DhcpRelayTimeThreshold_Object=MibScalar
swL2DhcpRelayTimeThreshold=_SwL2DhcpRelayTimeThreshold_Object((1,3,6,1,4,1,171,11,63,11,2,18,3),_SwL2DhcpRelayTimeThreshold_Type())
swL2DhcpRelayTimeThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayTimeThreshold.setStatus(_J)
class _SwL2DhcpRelayOption82State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DhcpRelayOption82State_Type.__name__=_B
_SwL2DhcpRelayOption82State_Object=MibScalar
swL2DhcpRelayOption82State=_SwL2DhcpRelayOption82State_Object((1,3,6,1,4,1,171,11,63,11,2,18,4),_SwL2DhcpRelayOption82State_Type())
swL2DhcpRelayOption82State.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayOption82State.setStatus(_J)
class _SwL2DhcpRelayOption82Check_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DhcpRelayOption82Check_Type.__name__=_B
_SwL2DhcpRelayOption82Check_Object=MibScalar
swL2DhcpRelayOption82Check=_SwL2DhcpRelayOption82Check_Object((1,3,6,1,4,1,171,11,63,11,2,18,5),_SwL2DhcpRelayOption82Check_Type())
swL2DhcpRelayOption82Check.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayOption82Check.setStatus(_J)
class _SwL2DhcpRelayOption82Policy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('replace',1),('drop',2),('keep',3)))
_SwL2DhcpRelayOption82Policy_Type.__name__=_B
_SwL2DhcpRelayOption82Policy_Object=MibScalar
swL2DhcpRelayOption82Policy=_SwL2DhcpRelayOption82Policy_Object((1,3,6,1,4,1,171,11,63,11,2,18,6),_SwL2DhcpRelayOption82Policy_Type())
swL2DhcpRelayOption82Policy.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayOption82Policy.setStatus(_J)
_SwL2DhcpRelayCtrlTable_Object=MibTable
swL2DhcpRelayCtrlTable=_SwL2DhcpRelayCtrlTable_Object((1,3,6,1,4,1,171,11,63,11,2,18,7))
if mibBuilder.loadTexts:swL2DhcpRelayCtrlTable.setStatus(_J)
_SwL2DhcpRelayCtrlEntry_Object=MibTableRow
swL2DhcpRelayCtrlEntry=_SwL2DhcpRelayCtrlEntry_Object((1,3,6,1,4,1,171,11,63,11,2,18,7,1))
swL2DhcpRelayCtrlEntry.setIndexNames((0,_E,_A7),(0,_E,_A8))
if mibBuilder.loadTexts:swL2DhcpRelayCtrlEntry.setStatus(_J)
class _SwL2DhcpRelayCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL2DhcpRelayCtrlInterfaceName_Type.__name__=_K
_SwL2DhcpRelayCtrlInterfaceName_Object=MibTableColumn
swL2DhcpRelayCtrlInterfaceName=_SwL2DhcpRelayCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,63,11,2,18,7,1,1),_SwL2DhcpRelayCtrlInterfaceName_Type())
swL2DhcpRelayCtrlInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpRelayCtrlInterfaceName.setStatus(_J)
_SwL2DhcpRelayCtrlServer_Type=IpAddress
_SwL2DhcpRelayCtrlServer_Object=MibTableColumn
swL2DhcpRelayCtrlServer=_SwL2DhcpRelayCtrlServer_Object((1,3,6,1,4,1,171,11,63,11,2,18,7,1,2),_SwL2DhcpRelayCtrlServer_Type())
swL2DhcpRelayCtrlServer.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpRelayCtrlServer.setStatus(_A)
class _SwL2DhcpRelayCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('invalid',2),('valid',3)))
_SwL2DhcpRelayCtrlState_Type.__name__=_B
_SwL2DhcpRelayCtrlState_Object=MibTableColumn
swL2DhcpRelayCtrlState=_SwL2DhcpRelayCtrlState_Object((1,3,6,1,4,1,171,11,63,11,2,18,7,1,3),_SwL2DhcpRelayCtrlState_Type())
swL2DhcpRelayCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayCtrlState.setStatus(_J)
_SwL2MgmtMIBTraps_ObjectIdentity=ObjectIdentity
swL2MgmtMIBTraps=_SwL2MgmtMIBTraps_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,20))
_SwL2MgmtMIBTrapPrefix_ObjectIdentity=ObjectIdentity
swL2MgmtMIBTrapPrefix=_SwL2MgmtMIBTrapPrefix_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,20,0))
_Swl2PortSecurityBindings_ObjectIdentity=ObjectIdentity
swl2PortSecurityBindings=_Swl2PortSecurityBindings_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,20,1))
_SwL2PortSecurityViolationMac_Type=MacAddress
_SwL2PortSecurityViolationMac_Object=MibScalar
swL2PortSecurityViolationMac=_SwL2PortSecurityViolationMac_Object((1,3,6,1,4,1,171,11,63,11,2,20,1,1),_SwL2PortSecurityViolationMac_Type())
swL2PortSecurityViolationMac.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:swL2PortSecurityViolationMac.setStatus(_A)
_Swl2NotificationBindings_ObjectIdentity=ObjectIdentity
swl2NotificationBindings=_Swl2NotificationBindings_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,20,2))
class _SwL2macNotifyInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_SwL2macNotifyInfo_Type.__name__=_R
_SwL2macNotifyInfo_Object=MibScalar
swL2macNotifyInfo=_SwL2macNotifyInfo_Object((1,3,6,1,4,1,171,11,63,11,2,20,2,1),_SwL2macNotifyInfo_Type())
swL2macNotifyInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2macNotifyInfo.setStatus(_A)
class _SwL2FloodMacDetectedMacVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2FloodMacDetectedMacVid_Type.__name__=_B
_SwL2FloodMacDetectedMacVid_Object=MibScalar
swL2FloodMacDetectedMacVid=_SwL2FloodMacDetectedMacVid_Object((1,3,6,1,4,1,171,11,63,11,2,20,2,2),_SwL2FloodMacDetectedMacVid_Type())
swL2FloodMacDetectedMacVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2FloodMacDetectedMacVid.setStatus(_A)
_SwL2FloodMacDetectedMacAddress_Type=MacAddress
_SwL2FloodMacDetectedMacAddress_Object=MibScalar
swL2FloodMacDetectedMacAddress=_SwL2FloodMacDetectedMacAddress_Object((1,3,6,1,4,1,171,11,63,11,2,20,2,3),_SwL2FloodMacDetectedMacAddress_Type())
swL2FloodMacDetectedMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2FloodMacDetectedMacAddress.setStatus(_A)
_SwL2LoopDetectMgmt_ObjectIdentity=ObjectIdentity
swL2LoopDetectMgmt=_SwL2LoopDetectMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,21))
_SwL2LoopDetectCtrl_ObjectIdentity=ObjectIdentity
swL2LoopDetectCtrl=_SwL2LoopDetectCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,21,1))
class _SwL2LoopDetectAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2LoopDetectAdminState_Type.__name__=_B
_SwL2LoopDetectAdminState_Object=MibScalar
swL2LoopDetectAdminState=_SwL2LoopDetectAdminState_Object((1,3,6,1,4,1,171,11,63,11,2,21,1,1),_SwL2LoopDetectAdminState_Type())
swL2LoopDetectAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectAdminState.setStatus(_A)
class _SwL2LoopDetectInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_SwL2LoopDetectInterval_Type.__name__=_B
_SwL2LoopDetectInterval_Object=MibScalar
swL2LoopDetectInterval=_SwL2LoopDetectInterval_Object((1,3,6,1,4,1,171,11,63,11,2,21,1,2),_SwL2LoopDetectInterval_Type())
swL2LoopDetectInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectInterval.setStatus(_A)
class _SwL2LoopDetectRecoverTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_SwL2LoopDetectRecoverTime_Type.__name__=_B
_SwL2LoopDetectRecoverTime_Object=MibScalar
swL2LoopDetectRecoverTime=_SwL2LoopDetectRecoverTime_Object((1,3,6,1,4,1,171,11,63,11,2,21,1,3),_SwL2LoopDetectRecoverTime_Type())
swL2LoopDetectRecoverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectRecoverTime.setStatus(_A)
class _SwL2LoopDetectTrapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),('loop_detected',2),('loop_cleared',3),('both',4)))
_SwL2LoopDetectTrapMode_Type.__name__=_B
_SwL2LoopDetectTrapMode_Object=MibScalar
swL2LoopDetectTrapMode=_SwL2LoopDetectTrapMode_Object((1,3,6,1,4,1,171,11,63,11,2,21,1,5),_SwL2LoopDetectTrapMode_Type())
swL2LoopDetectTrapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectTrapMode.setStatus(_A)
_SwL2LoopDetectPortMgmt_ObjectIdentity=ObjectIdentity
swL2LoopDetectPortMgmt=_SwL2LoopDetectPortMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,21,2))
_SwL2LoopDetectPortTable_Object=MibTable
swL2LoopDetectPortTable=_SwL2LoopDetectPortTable_Object((1,3,6,1,4,1,171,11,63,11,2,21,2,1))
if mibBuilder.loadTexts:swL2LoopDetectPortTable.setStatus(_A)
_SwL2LoopDetectPortEntry_Object=MibTableRow
swL2LoopDetectPortEntry=_SwL2LoopDetectPortEntry_Object((1,3,6,1,4,1,171,11,63,11,2,21,2,1,1))
swL2LoopDetectPortEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:swL2LoopDetectPortEntry.setStatus(_A)
class _SwL2LoopDetectPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2LoopDetectPortIndex_Type.__name__=_B
_SwL2LoopDetectPortIndex_Object=MibTableColumn
swL2LoopDetectPortIndex=_SwL2LoopDetectPortIndex_Object((1,3,6,1,4,1,171,11,63,11,2,21,2,1,1,1),_SwL2LoopDetectPortIndex_Type())
swL2LoopDetectPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectPortIndex.setStatus(_A)
class _SwL2LoopDetectPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2LoopDetectPortState_Type.__name__=_B
_SwL2LoopDetectPortState_Object=MibTableColumn
swL2LoopDetectPortState=_SwL2LoopDetectPortState_Object((1,3,6,1,4,1,171,11,63,11,2,21,2,1,1,2),_SwL2LoopDetectPortState_Type())
swL2LoopDetectPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectPortState.setStatus(_A)
class _SwL2LoopDetectPortLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('loop',2),('error',3)))
_SwL2LoopDetectPortLoopStatus_Type.__name__=_B
_SwL2LoopDetectPortLoopStatus_Object=MibTableColumn
swL2LoopDetectPortLoopStatus=_SwL2LoopDetectPortLoopStatus_Object((1,3,6,1,4,1,171,11,63,11,2,21,2,1,1,4),_SwL2LoopDetectPortLoopStatus_Type())
swL2LoopDetectPortLoopStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectPortLoopStatus.setStatus(_A)
_SwL2MultiFilter_ObjectIdentity=ObjectIdentity
swL2MultiFilter=_SwL2MultiFilter_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,22))
_SwL2McastFilterTable_Object=MibTable
swL2McastFilterTable=_SwL2McastFilterTable_Object((1,3,6,1,4,1,171,11,63,11,2,22,2))
if mibBuilder.loadTexts:swL2McastFilterTable.setStatus(_A)
_SwL2McastFilterEntry_Object=MibTableRow
swL2McastFilterEntry=_SwL2McastFilterEntry_Object((1,3,6,1,4,1,171,11,63,11,2,22,2,1))
swL2McastFilterEntry.setIndexNames((0,_E,_A9))
if mibBuilder.loadTexts:swL2McastFilterEntry.setStatus(_A)
class _SwL2McastFilterProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_SwL2McastFilterProfileIndex_Type.__name__=_B
_SwL2McastFilterProfileIndex_Object=MibTableColumn
swL2McastFilterProfileIndex=_SwL2McastFilterProfileIndex_Object((1,3,6,1,4,1,171,11,63,11,2,22,2,1,1),_SwL2McastFilterProfileIndex_Type())
swL2McastFilterProfileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2McastFilterProfileIndex.setStatus(_A)
class _SwL2McastFilterProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwL2McastFilterProfileName_Type.__name__=_K
_SwL2McastFilterProfileName_Object=MibTableColumn
swL2McastFilterProfileName=_SwL2McastFilterProfileName_Object((1,3,6,1,4,1,171,11,63,11,2,22,2,1,2),_SwL2McastFilterProfileName_Type())
swL2McastFilterProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2McastFilterProfileName.setStatus(_A)
class _SwL2McastFilterAddOrDelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('add',2),(_P,3)))
_SwL2McastFilterAddOrDelState_Type.__name__=_B
_SwL2McastFilterAddOrDelState_Object=MibTableColumn
swL2McastFilterAddOrDelState=_SwL2McastFilterAddOrDelState_Object((1,3,6,1,4,1,171,11,63,11,2,22,2,1,3),_SwL2McastFilterAddOrDelState_Type())
swL2McastFilterAddOrDelState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2McastFilterAddOrDelState.setStatus(_A)
_SwL2McastFilterGroupList_Type=DisplayString
_SwL2McastFilterGroupList_Object=MibTableColumn
swL2McastFilterGroupList=_SwL2McastFilterGroupList_Object((1,3,6,1,4,1,171,11,63,11,2,22,2,1,4),_SwL2McastFilterGroupList_Type())
swL2McastFilterGroupList.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2McastFilterGroupList.setStatus(_A)
_SwL2McastFilterStatus_Type=RowStatus
_SwL2McastFilterStatus_Object=MibTableColumn
swL2McastFilterStatus=_SwL2McastFilterStatus_Object((1,3,6,1,4,1,171,11,63,11,2,22,2,1,5),_SwL2McastFilterStatus_Type())
swL2McastFilterStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2McastFilterStatus.setStatus(_A)
_SwL2McastFilterPortTable_Object=MibTable
swL2McastFilterPortTable=_SwL2McastFilterPortTable_Object((1,3,6,1,4,1,171,11,63,11,2,22,3))
if mibBuilder.loadTexts:swL2McastFilterPortTable.setStatus(_A)
_SwL2McastFilterPortEntry_Object=MibTableRow
swL2McastFilterPortEntry=_SwL2McastFilterPortEntry_Object((1,3,6,1,4,1,171,11,63,11,2,22,3,1))
swL2McastFilterPortEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:swL2McastFilterPortEntry.setStatus(_A)
_SwL2McastFilterPortGroupPortIndex_Type=Integer32
_SwL2McastFilterPortGroupPortIndex_Object=MibTableColumn
swL2McastFilterPortGroupPortIndex=_SwL2McastFilterPortGroupPortIndex_Object((1,3,6,1,4,1,171,11,63,11,2,22,3,1,1),_SwL2McastFilterPortGroupPortIndex_Type())
swL2McastFilterPortGroupPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2McastFilterPortGroupPortIndex.setStatus(_A)
class _SwL2McastFilterPortProfileAddOrDelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('add',2),(_P,3)))
_SwL2McastFilterPortProfileAddOrDelState_Type.__name__=_B
_SwL2McastFilterPortProfileAddOrDelState_Object=MibTableColumn
swL2McastFilterPortProfileAddOrDelState=_SwL2McastFilterPortProfileAddOrDelState_Object((1,3,6,1,4,1,171,11,63,11,2,22,3,1,2),_SwL2McastFilterPortProfileAddOrDelState_Type())
swL2McastFilterPortProfileAddOrDelState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2McastFilterPortProfileAddOrDelState.setStatus(_A)
class _SwL2McastFilterPortProfileID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_SwL2McastFilterPortProfileID_Type.__name__=_B
_SwL2McastFilterPortProfileID_Object=MibTableColumn
swL2McastFilterPortProfileID=_SwL2McastFilterPortProfileID_Object((1,3,6,1,4,1,171,11,63,11,2,22,3,1,3),_SwL2McastFilterPortProfileID_Type())
swL2McastFilterPortProfileID.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2McastFilterPortProfileID.setStatus(_A)
_SwL2McastFilterPortMaxGroupTable_Object=MibTable
swL2McastFilterPortMaxGroupTable=_SwL2McastFilterPortMaxGroupTable_Object((1,3,6,1,4,1,171,11,63,11,2,22,4))
if mibBuilder.loadTexts:swL2McastFilterPortMaxGroupTable.setStatus(_A)
_SwL2McastFilterPortMaxGroupEntry_Object=MibTableRow
swL2McastFilterPortMaxGroupEntry=_SwL2McastFilterPortMaxGroupEntry_Object((1,3,6,1,4,1,171,11,63,11,2,22,4,1))
swL2McastFilterPortMaxGroupEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:swL2McastFilterPortMaxGroupEntry.setStatus(_A)
_SwL2McastFilterPortMaxGroupPortIndex_Type=Integer32
_SwL2McastFilterPortMaxGroupPortIndex_Object=MibTableColumn
swL2McastFilterPortMaxGroupPortIndex=_SwL2McastFilterPortMaxGroupPortIndex_Object((1,3,6,1,4,1,171,11,63,11,2,22,4,1,1),_SwL2McastFilterPortMaxGroupPortIndex_Type())
swL2McastFilterPortMaxGroupPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2McastFilterPortMaxGroupPortIndex.setStatus(_A)
class _SwL2McastFilterPortMaxGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_SwL2McastFilterPortMaxGroup_Type.__name__=_B
_SwL2McastFilterPortMaxGroup_Object=MibTableColumn
swL2McastFilterPortMaxGroup=_SwL2McastFilterPortMaxGroup_Object((1,3,6,1,4,1,171,11,63,11,2,22,4,1,2),_SwL2McastFilterPortMaxGroup_Type())
swL2McastFilterPortMaxGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2McastFilterPortMaxGroup.setStatus(_A)
_SwL2McastFilterPortInfoTable_Object=MibTable
swL2McastFilterPortInfoTable=_SwL2McastFilterPortInfoTable_Object((1,3,6,1,4,1,171,11,63,11,2,22,5))
if mibBuilder.loadTexts:swL2McastFilterPortInfoTable.setStatus(_A)
_SwL2McastFilterPortInfoEntry_Object=MibTableRow
swL2McastFilterPortInfoEntry=_SwL2McastFilterPortInfoEntry_Object((1,3,6,1,4,1,171,11,63,11,2,22,5,1))
swL2McastFilterPortInfoEntry.setIndexNames((0,_E,_AC))
if mibBuilder.loadTexts:swL2McastFilterPortInfoEntry.setStatus(_A)
_SwL2McastFilterPortInfoPortIndex_Type=Integer32
_SwL2McastFilterPortInfoPortIndex_Object=MibTableColumn
swL2McastFilterPortInfoPortIndex=_SwL2McastFilterPortInfoPortIndex_Object((1,3,6,1,4,1,171,11,63,11,2,22,5,1,1),_SwL2McastFilterPortInfoPortIndex_Type())
swL2McastFilterPortInfoPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2McastFilterPortInfoPortIndex.setStatus(_A)
_SwL2McastFilterPortInfoProfileName_Type=DisplayString
_SwL2McastFilterPortInfoProfileName_Object=MibTableColumn
swL2McastFilterPortInfoProfileName=_SwL2McastFilterPortInfoProfileName_Object((1,3,6,1,4,1,171,11,63,11,2,22,5,1,2),_SwL2McastFilterPortInfoProfileName_Type())
swL2McastFilterPortInfoProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2McastFilterPortInfoProfileName.setStatus(_A)
_SwL2VlanMgmt_ObjectIdentity=ObjectIdentity
swL2VlanMgmt=_SwL2VlanMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,23))
_SwL2VlanAdvertisementTable_Object=MibTable
swL2VlanAdvertisementTable=_SwL2VlanAdvertisementTable_Object((1,3,6,1,4,1,171,11,63,11,2,23,1))
if mibBuilder.loadTexts:swL2VlanAdvertisementTable.setStatus(_A)
_SwL2VlanAdvertisementEntry_Object=MibTableRow
swL2VlanAdvertisementEntry=_SwL2VlanAdvertisementEntry_Object((1,3,6,1,4,1,171,11,63,11,2,23,1,1))
swL2VlanAdvertisementEntry.setIndexNames((0,_E,_AD))
if mibBuilder.loadTexts:swL2VlanAdvertisementEntry.setStatus(_A)
class _SwL2VlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2VlanIndex_Type.__name__=_B
_SwL2VlanIndex_Object=MibTableColumn
swL2VlanIndex=_SwL2VlanIndex_Object((1,3,6,1,4,1,171,11,63,11,2,23,1,1,1),_SwL2VlanIndex_Type())
swL2VlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanIndex.setStatus(_A)
class _SwL2VlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2VlanName_Type.__name__=_K
_SwL2VlanName_Object=MibTableColumn
swL2VlanName=_SwL2VlanName_Object((1,3,6,1,4,1,171,11,63,11,2,23,1,1,2),_SwL2VlanName_Type())
swL2VlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanName.setStatus(_A)
class _SwL2VlanAdvertiseState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2VlanAdvertiseState_Type.__name__=_B
_SwL2VlanAdvertiseState_Object=MibTableColumn
swL2VlanAdvertiseState=_SwL2VlanAdvertiseState_Object((1,3,6,1,4,1,171,11,63,11,2,23,1,1,3),_SwL2VlanAdvertiseState_Type())
swL2VlanAdvertiseState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanAdvertiseState.setStatus(_A)
_SwL2VlanMultiplyMgmt_ObjectIdentity=ObjectIdentity
swL2VlanMultiplyMgmt=_SwL2VlanMultiplyMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,23,2))
class _SwL2VlanMultiplyVlanList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwL2VlanMultiplyVlanList_Type.__name__=_K
_SwL2VlanMultiplyVlanList_Object=MibScalar
swL2VlanMultiplyVlanList=_SwL2VlanMultiplyVlanList_Object((1,3,6,1,4,1,171,11,63,11,2,23,2,1),_SwL2VlanMultiplyVlanList_Type())
swL2VlanMultiplyVlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanMultiplyVlanList.setStatus(_A)
class _SwL2VlanMultiplyAdvertisement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_H,2),(_G,3)))
_SwL2VlanMultiplyAdvertisement_Type.__name__=_B
_SwL2VlanMultiplyAdvertisement_Object=MibScalar
swL2VlanMultiplyAdvertisement=_SwL2VlanMultiplyAdvertisement_Object((1,3,6,1,4,1,171,11,63,11,2,23,2,2),_SwL2VlanMultiplyAdvertisement_Type())
swL2VlanMultiplyAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanMultiplyAdvertisement.setStatus(_A)
_SwL2VlanMultiplyPortList_Type=PortList
_SwL2VlanMultiplyPortList_Object=MibScalar
swL2VlanMultiplyPortList=_SwL2VlanMultiplyPortList_Object((1,3,6,1,4,1,171,11,63,11,2,23,2,3),_SwL2VlanMultiplyPortList_Type())
swL2VlanMultiplyPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanMultiplyPortList.setStatus(_A)
class _SwL2VlanMultiplyPortListAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('add-tagged',2),('add-untagged',3),('add-forbidden',4),(_P,5)))
_SwL2VlanMultiplyPortListAction_Type.__name__=_B
_SwL2VlanMultiplyPortListAction_Object=MibScalar
swL2VlanMultiplyPortListAction=_SwL2VlanMultiplyPortListAction_Object((1,3,6,1,4,1,171,11,63,11,2,23,2,4),_SwL2VlanMultiplyPortListAction_Type())
swL2VlanMultiplyPortListAction.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanMultiplyPortListAction.setStatus(_A)
class _SwL2VlanMultiplyAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('create',2),('configure',3),(_P,4)))
_SwL2VlanMultiplyAction_Type.__name__=_B
_SwL2VlanMultiplyAction_Object=MibScalar
swL2VlanMultiplyAction=_SwL2VlanMultiplyAction_Object((1,3,6,1,4,1,171,11,63,11,2,23,2,5),_SwL2VlanMultiplyAction_Type())
swL2VlanMultiplyAction.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanMultiplyAction.setStatus(_A)
_SwL2DhcpLocalRelayMgmt_ObjectIdentity=ObjectIdentity
swL2DhcpLocalRelayMgmt=_SwL2DhcpLocalRelayMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,24))
class _SwL2DhcpLocalRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DhcpLocalRelayState_Type.__name__=_B
_SwL2DhcpLocalRelayState_Object=MibScalar
swL2DhcpLocalRelayState=_SwL2DhcpLocalRelayState_Object((1,3,6,1,4,1,171,11,63,11,2,24,1),_SwL2DhcpLocalRelayState_Type())
swL2DhcpLocalRelayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpLocalRelayState.setStatus(_A)
_SwL2DhcpLocalRelayVLANTable_Object=MibTable
swL2DhcpLocalRelayVLANTable=_SwL2DhcpLocalRelayVLANTable_Object((1,3,6,1,4,1,171,11,63,11,2,24,2))
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANTable.setStatus(_A)
_SwL2DhcpLocalRelayVLANEntry_Object=MibTableRow
swL2DhcpLocalRelayVLANEntry=_SwL2DhcpLocalRelayVLANEntry_Object((1,3,6,1,4,1,171,11,63,11,2,24,2,1))
swL2DhcpLocalRelayVLANEntry.setIndexNames((0,_E,_AE))
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANEntry.setStatus(_A)
class _SwL2DhcpLocalRelayVLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2DhcpLocalRelayVLANID_Type.__name__=_B
_SwL2DhcpLocalRelayVLANID_Object=MibTableColumn
swL2DhcpLocalRelayVLANID=_SwL2DhcpLocalRelayVLANID_Object((1,3,6,1,4,1,171,11,63,11,2,24,2,1,1),_SwL2DhcpLocalRelayVLANID_Type())
swL2DhcpLocalRelayVLANID.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANID.setStatus(_A)
class _SwL2DhcpLocalRelayVLANState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DhcpLocalRelayVLANState_Type.__name__=_B
_SwL2DhcpLocalRelayVLANState_Object=MibTableColumn
swL2DhcpLocalRelayVLANState=_SwL2DhcpLocalRelayVLANState_Object((1,3,6,1,4,1,171,11,63,11,2,24,2,1,2),_SwL2DhcpLocalRelayVLANState_Type())
swL2DhcpLocalRelayVLANState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANState.setStatus(_A)
_SwL2FloodMAC_ObjectIdentity=ObjectIdentity
swL2FloodMAC=_SwL2FloodMAC_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,25))
_SwL2FloodMACMgmt_ObjectIdentity=ObjectIdentity
swL2FloodMACMgmt=_SwL2FloodMACMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,25,1))
_SwL2FloodMACGlobalSettings_ObjectIdentity=ObjectIdentity
swL2FloodMACGlobalSettings=_SwL2FloodMACGlobalSettings_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,25,1,1))
class _SwL2FloodMACState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2FloodMACState_Type.__name__=_B
_SwL2FloodMACState_Object=MibScalar
swL2FloodMACState=_SwL2FloodMACState_Object((1,3,6,1,4,1,171,11,63,11,2,25,1,1,1),_SwL2FloodMACState_Type())
swL2FloodMACState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2FloodMACState.setStatus(_A)
class _SwL2FloodMACLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2FloodMACLogState_Type.__name__=_B
_SwL2FloodMACLogState_Object=MibScalar
swL2FloodMACLogState=_SwL2FloodMACLogState_Object((1,3,6,1,4,1,171,11,63,11,2,25,1,1,2),_SwL2FloodMACLogState_Type())
swL2FloodMACLogState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2FloodMACLogState.setStatus(_A)
class _SwL2FloodMACTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2FloodMACTrapState_Type.__name__=_B
_SwL2FloodMACTrapState_Object=MibScalar
swL2FloodMACTrapState=_SwL2FloodMACTrapState_Object((1,3,6,1,4,1,171,11,63,11,2,25,1,1,3),_SwL2FloodMACTrapState_Type())
swL2FloodMACTrapState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2FloodMACTrapState.setStatus(_A)
class _SwL2FloodMACClearFDB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no-action',1),(_W,2)))
_SwL2FloodMACClearFDB_Type.__name__=_B
_SwL2FloodMACClearFDB_Object=MibScalar
swL2FloodMACClearFDB=_SwL2FloodMACClearFDB_Object((1,3,6,1,4,1,171,11,63,11,2,25,1,1,4),_SwL2FloodMACClearFDB_Type())
swL2FloodMACClearFDB.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2FloodMACClearFDB.setStatus(_A)
_SwL2FloodMACAutoFDBCtrlTable_Object=MibTable
swL2FloodMACAutoFDBCtrlTable=_SwL2FloodMACAutoFDBCtrlTable_Object((1,3,6,1,4,1,171,11,63,11,2,25,1,2))
if mibBuilder.loadTexts:swL2FloodMACAutoFDBCtrlTable.setStatus(_A)
_SwL2FloodMACAutoFDBCtrlEntry_Object=MibTableRow
swL2FloodMACAutoFDBCtrlEntry=_SwL2FloodMACAutoFDBCtrlEntry_Object((1,3,6,1,4,1,171,11,63,11,2,25,1,2,1))
swL2FloodMACAutoFDBCtrlEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:swL2FloodMACAutoFDBCtrlEntry.setStatus(_A)
_SwL2FloodMACAutoFDBIPAddress_Type=IpAddress
_SwL2FloodMACAutoFDBIPAddress_Object=MibTableColumn
swL2FloodMACAutoFDBIPAddress=_SwL2FloodMACAutoFDBIPAddress_Object((1,3,6,1,4,1,171,11,63,11,2,25,1,2,1,1),_SwL2FloodMACAutoFDBIPAddress_Type())
swL2FloodMACAutoFDBIPAddress.setMaxAccess(_Q)
if mibBuilder.loadTexts:swL2FloodMACAutoFDBIPAddress.setStatus(_A)
_SwL2FloodMACAutoFDBRowStatus_Type=RowStatus
_SwL2FloodMACAutoFDBRowStatus_Object=MibTableColumn
swL2FloodMACAutoFDBRowStatus=_SwL2FloodMACAutoFDBRowStatus_Object((1,3,6,1,4,1,171,11,63,11,2,25,1,2,1,2),_SwL2FloodMACAutoFDBRowStatus_Type())
swL2FloodMACAutoFDBRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2FloodMACAutoFDBRowStatus.setStatus(_A)
_SwL2FloodMACInfo_ObjectIdentity=ObjectIdentity
swL2FloodMACInfo=_SwL2FloodMACInfo_ObjectIdentity((1,3,6,1,4,1,171,11,63,11,2,25,2))
_SwL2FloodMACFDBTable_Object=MibTable
swL2FloodMACFDBTable=_SwL2FloodMACFDBTable_Object((1,3,6,1,4,1,171,11,63,11,2,25,2,1))
if mibBuilder.loadTexts:swL2FloodMACFDBTable.setStatus(_A)
_SwL2FloodMACFDBEntry_Object=MibTableRow
swL2FloodMACFDBEntry=_SwL2FloodMACFDBEntry_Object((1,3,6,1,4,1,171,11,63,11,2,25,2,1,1))
swL2FloodMACFDBEntry.setIndexNames((0,_E,_AF),(0,_E,_AG),(0,_E,_AH))
if mibBuilder.loadTexts:swL2FloodMACFDBEntry.setStatus(_A)
_SwL2FloodMACFDBIndex_Type=Integer32
_SwL2FloodMACFDBIndex_Object=MibTableColumn
swL2FloodMACFDBIndex=_SwL2FloodMACFDBIndex_Object((1,3,6,1,4,1,171,11,63,11,2,25,2,1,1,1),_SwL2FloodMACFDBIndex_Type())
swL2FloodMACFDBIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:swL2FloodMACFDBIndex.setStatus(_A)
class _SwL2FloodMACFDBVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2FloodMACFDBVID_Type.__name__=_B
_SwL2FloodMACFDBVID_Object=MibTableColumn
swL2FloodMACFDBVID=_SwL2FloodMACFDBVID_Object((1,3,6,1,4,1,171,11,63,11,2,25,2,1,1,2),_SwL2FloodMACFDBVID_Type())
swL2FloodMACFDBVID.setMaxAccess(_Q)
if mibBuilder.loadTexts:swL2FloodMACFDBVID.setStatus(_A)
_SwL2FloodMACFDBMacAddress_Type=MacAddress
_SwL2FloodMACFDBMacAddress_Object=MibTableColumn
swL2FloodMACFDBMacAddress=_SwL2FloodMACFDBMacAddress_Object((1,3,6,1,4,1,171,11,63,11,2,25,2,1,1,3),_SwL2FloodMACFDBMacAddress_Type())
swL2FloodMACFDBMacAddress.setMaxAccess(_Q)
if mibBuilder.loadTexts:swL2FloodMACFDBMacAddress.setStatus(_A)
class _SwL2FloodMACFDBStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('inactive',2)))
_SwL2FloodMACFDBStatus_Type.__name__=_B
_SwL2FloodMACFDBStatus_Object=MibTableColumn
swL2FloodMACFDBStatus=_SwL2FloodMACFDBStatus_Object((1,3,6,1,4,1,171,11,63,11,2,25,2,1,1,4),_SwL2FloodMACFDBStatus_Type())
swL2FloodMACFDBStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2FloodMACFDBStatus.setStatus(_A)
_SwL2FloodMACFDBTimestamp_Type=Integer32
_SwL2FloodMACFDBTimestamp_Object=MibTableColumn
swL2FloodMACFDBTimestamp=_SwL2FloodMACFDBTimestamp_Object((1,3,6,1,4,1,171,11,63,11,2,25,2,1,1,5),_SwL2FloodMACFDBTimestamp_Type())
swL2FloodMACFDBTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2FloodMACFDBTimestamp.setStatus(_A)
_SwL2FloodMACAutoFDBTable_Object=MibTable
swL2FloodMACAutoFDBTable=_SwL2FloodMACAutoFDBTable_Object((1,3,6,1,4,1,171,11,63,11,2,25,2,2))
if mibBuilder.loadTexts:swL2FloodMACAutoFDBTable.setStatus(_A)
_SwL2FloodMACAutoFDBEntry_Object=MibTableRow
swL2FloodMACAutoFDBEntry=_SwL2FloodMACAutoFDBEntry_Object((1,3,6,1,4,1,171,11,63,11,2,25,2,2,1))
swL2FloodMACAutoFDBEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:swL2FloodMACAutoFDBEntry.setStatus(_A)
class _SwL2FloodMACAutoFDBVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2FloodMACAutoFDBVID_Type.__name__=_B
_SwL2FloodMACAutoFDBVID_Object=MibTableColumn
swL2FloodMACAutoFDBVID=_SwL2FloodMACAutoFDBVID_Object((1,3,6,1,4,1,171,11,63,11,2,25,2,2,1,1),_SwL2FloodMACAutoFDBVID_Type())
swL2FloodMACAutoFDBVID.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2FloodMACAutoFDBVID.setStatus(_A)
_SwL2FloodMACAutoFDBMacAddress_Type=MacAddress
_SwL2FloodMACAutoFDBMacAddress_Object=MibTableColumn
swL2FloodMACAutoFDBMacAddress=_SwL2FloodMACAutoFDBMacAddress_Object((1,3,6,1,4,1,171,11,63,11,2,25,2,2,1,2),_SwL2FloodMACAutoFDBMacAddress_Type())
swL2FloodMACAutoFDBMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2FloodMACAutoFDBMacAddress.setStatus(_A)
_SwL2FloodMACAutoFDBPort_Type=Integer32
_SwL2FloodMACAutoFDBPort_Object=MibTableColumn
swL2FloodMACAutoFDBPort=_SwL2FloodMACAutoFDBPort_Object((1,3,6,1,4,1,171,11,63,11,2,25,2,2,1,3),_SwL2FloodMACAutoFDBPort_Type())
swL2FloodMACAutoFDBPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2FloodMACAutoFDBPort.setStatus(_A)
_SwL2FloodMACAutoFDBTimestamp_Type=Integer32
_SwL2FloodMACAutoFDBTimestamp_Object=MibTableColumn
swL2FloodMACAutoFDBTimestamp=_SwL2FloodMACAutoFDBTimestamp_Object((1,3,6,1,4,1,171,11,63,11,2,25,2,2,1,4),_SwL2FloodMACAutoFDBTimestamp_Type())
swL2FloodMACAutoFDBTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2FloodMACAutoFDBTimestamp.setStatus(_A)
swL2PortSecurityViolationTrap=NotificationType((1,3,6,1,4,1,171,11,63,11,2,20,0,1))
swL2PortSecurityViolationTrap.setObjects(*((_E,_X),(_E,_AI)))
if mibBuilder.loadTexts:swL2PortSecurityViolationTrap.setStatus(_A)
swL2macNotification=NotificationType((1,3,6,1,4,1,171,11,63,11,2,20,0,2))
swL2macNotification.setObjects((_E,_AJ))
if mibBuilder.loadTexts:swL2macNotification.setStatus(_A)
swL2FloodMacDetectedTrap=NotificationType((1,3,6,1,4,1,171,11,63,11,2,20,0,3))
swL2FloodMacDetectedTrap.setObjects(*((_E,_AK),(_E,_AL)))
if mibBuilder.loadTexts:swL2FloodMacDetectedTrap.setStatus(_A)
swL2PortLoopOccurred=NotificationType((1,3,6,1,4,1,171,11,63,11,2,20,0,4))
swL2PortLoopOccurred.setObjects((_E,_O))
if mibBuilder.loadTexts:swL2PortLoopOccurred.setStatus(_A)
swL2PortLoopRestart=NotificationType((1,3,6,1,4,1,171,11,63,11,2,20,0,5))
swL2PortLoopRestart.setObjects((_E,_O))
if mibBuilder.loadTexts:swL2PortLoopRestart.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'VlanId':VlanId,'PortList':PortList,'MacAddress':MacAddress,'swL2MgmtMIB':swL2MgmtMIB,'swL2DevMgmt':swL2DevMgmt,'swL2DevInfo':swL2DevInfo,'swL2DevInfoFrontPanelLedStatus':swL2DevInfoFrontPanelLedStatus,'swL2DevCtrl':swL2DevCtrl,'swL2DevCtrlSystemReboot':swL2DevCtrlSystemReboot,'swL2DevCtrlSystemIP':swL2DevCtrlSystemIP,'swL2DevCtrlSubnetMask':swL2DevCtrlSubnetMask,'swL2DevCtrlDefaultGateway':swL2DevCtrlDefaultGateway,'swL2DevCtrlManagementVlanId':swL2DevCtrlManagementVlanId,'swL2DevCtrlIGMPSnooping':swL2DevCtrlIGMPSnooping,'swL2DevCtrlCleanAllStatisticCounter':swL2DevCtrlCleanAllStatisticCounter,'swL2DevCtrlSnmpEnableAuthenTraps':swL2DevCtrlSnmpEnableAuthenTraps,'swL2DevCtrlRmonState':swL2DevCtrlRmonState,'swL2DevCtrlIpAutoConfig':swL2DevCtrlIpAutoConfig,'swL2MACNotifyState':swL2MACNotifyState,'swL2MACNotifyHistorySize':swL2MACNotifyHistorySize,'swL2MACNotifyInterval':swL2MACNotifyInterval,'swL2DevCtrlLLDPState':swL2DevCtrlLLDPState,'swL2DevCtrlLLDPForwardMessageState':swL2DevCtrlLLDPForwardMessageState,'swL2DevCtrlAsymVlanState':swL2DevCtrlAsymVlanState,'swL2IGMPSnoopingMulticastVlanState':swL2IGMPSnoopingMulticastVlanState,'swL2DevCtrlVLANTrunkState':swL2DevCtrlVLANTrunkState,'swL2DevCtrlWeb':swL2DevCtrlWeb,'swL2DevCtrlWebState':swL2DevCtrlWebState,'swL2DevCtrlTelnet':swL2DevCtrlTelnet,'swL2DevCtrlTelnetState':swL2DevCtrlTelnetState,'swL2DevAlarm':swL2DevAlarm,'swL2DevAlarmNewRoot':swL2DevAlarmNewRoot,'swL2DevAlarmTopologyChange':swL2DevAlarmTopologyChange,'swL2DevAlarmLinkChange':swL2DevAlarmLinkChange,'swL2PortMgmt':swL2PortMgmt,'swL2PortInfoTable':swL2PortInfoTable,'swL2PortInfoEntry':swL2PortInfoEntry,_a:swL2PortInfoPortIndex,_b:swL2PortInfoMediumType,'swL2PortInfoLinkStatus':swL2PortInfoLinkStatus,'swL2PortInfoNwayStatus':swL2PortInfoNwayStatus,'swL2PortCtrlTable':swL2PortCtrlTable,'swL2PortCtrlEntry':swL2PortCtrlEntry,_d:swL2PortCtrlPortIndex,_e:swL2PortCtrlPortMediumType,'swL2PortCtrlAdminState':swL2PortCtrlAdminState,'swL2PortCtrlNwayState':swL2PortCtrlNwayState,'swL2PortCtrlFlowCtrlState':swL2PortCtrlFlowCtrlState,'swL2PortCtrlDescription':swL2PortCtrlDescription,'swL2PortCtrlAddressLearning':swL2PortCtrlAddressLearning,'swL2PortCtrlMACNotifyState':swL2PortCtrlMACNotifyState,'swL2PortCtrlMulticastfilter':swL2PortCtrlMulticastfilter,'swL2PortCtrlMDIXState':swL2PortCtrlMDIXState,'swL2PortErrTable':swL2PortErrTable,'swL2PortErrEntry':swL2PortErrEntry,_f:swL2PortErrPortIndex,'swL2PortErrPortState':swL2PortErrPortState,'swL2PortErrPortStatus':swL2PortErrPortStatus,'swL2PortErrPortReason':swL2PortErrPortReason,'swL2PortErrDescription':swL2PortErrDescription,'swL2QOSMgmt':swL2QOSMgmt,'swL2QOSBandwidthControlTable':swL2QOSBandwidthControlTable,'swL2QOSBandwidthControlEntry':swL2QOSBandwidthControlEntry,_g:swL2QOSBandwidthPortIndex,'swL2QOSBandwidthRxRate':swL2QOSBandwidthRxRate,'swL2QOSBandwidthTxRate':swL2QOSBandwidthTxRate,'swL2QOSBandwidthRadiusRxRate':swL2QOSBandwidthRadiusRxRate,'swL2QOSBandwidthRadiusTxRate':swL2QOSBandwidthRadiusTxRate,'swL2QOSSchedulingTable':swL2QOSSchedulingTable,'swL2QOSSchedulingEntry':swL2QOSSchedulingEntry,_h:swL2QOSSchedulingClassIndex,'swL2QOSSchedulingMaxWeight':swL2QOSSchedulingMaxWeight,'swL2QOSSchedulingMechanism':swL2QOSSchedulingMechanism,'swL2QOS8021pUserPriorityTable':swL2QOS8021pUserPriorityTable,'swL2QOS8021pUserPriorityEntry':swL2QOS8021pUserPriorityEntry,_k:swL2QOS8021pUserPriorityIndex,'swL2QOS8021pUserPriorityClass':swL2QOS8021pUserPriorityClass,'swL2QOS8021pDefaultPriorityTable':swL2QOS8021pDefaultPriorityTable,'swL2QOS8021pDefaultPriorityEntry':swL2QOS8021pDefaultPriorityEntry,_l:swL2QOS8021pDefaultPriorityIndex,'swL2QOS8021pDefaultPriority':swL2QOS8021pDefaultPriority,'swL2QOS8021pRadiusPriority':swL2QOS8021pRadiusPriority,'swL2QOSSchedulingMechanismCtrl':swL2QOSSchedulingMechanismCtrl,'swL2TrunkMgmt':swL2TrunkMgmt,'swPortTrunkMaxEntries':swPortTrunkMaxEntries,'swPortTrunkMaxPortMembers':swPortTrunkMaxPortMembers,'swPortTrunkTable':swPortTrunkTable,'swPortTrunkEntry':swPortTrunkEntry,_m:swPortTrunkIndex,'swPortTrunkMasterPort':swPortTrunkMasterPort,'swPortTrunkPortList':swPortTrunkPortList,'swPortTrunkType':swPortTrunkType,'swPortTrunkActivePort':swPortTrunkActivePort,'swPortTrunkState':swPortTrunkState,'swPortTrunkFloodingPort':swPortTrunkFloodingPort,'swL2TrunkAlgorithm':swL2TrunkAlgorithm,'swL2TrunkLACPPortTable':swL2TrunkLACPPortTable,'swL2TrunkLACPPortEntry':swL2TrunkLACPPortEntry,_n:swL2TrunkLACPPortIndex,'swL2TrunkLACPPortState':swL2TrunkLACPPortState,'swL2TrunkVLANTable':swL2TrunkVLANTable,'swL2TrunkVLANEntry':swL2TrunkVLANEntry,_o:swL2TrunkVLANPort,'swL2TrunkVLANState':swL2TrunkVLANState,'swPortMirrorPackage':swPortMirrorPackage,'swPortMirrorRxPortList':swPortMirrorRxPortList,'swPortMirrorTxPortList':swPortMirrorTxPortList,'swPortMirrorTargetPort':swPortMirrorTargetPort,'swPortMirrorState':swPortMirrorState,'swIGMPPackage':swIGMPPackage,'swL2IGMPMaxSupportedVlans':swL2IGMPMaxSupportedVlans,'swL2IGMPMaxIpGroupNumPerVlan':swL2IGMPMaxIpGroupNumPerVlan,'swL2IGMPCtrlTable':swL2IGMPCtrlTable,'swL2IGMPCtrlEntry':swL2IGMPCtrlEntry,_p:swL2IGMPCtrlVid,'swL2IGMPQueryInterval':swL2IGMPQueryInterval,'swL2IGMPMaxResponseTime':swL2IGMPMaxResponseTime,'swL2IGMPRobustness':swL2IGMPRobustness,'swL2IGMPLastMemberQueryInterval':swL2IGMPLastMemberQueryInterval,'swL2IGMPHostTimeout':swL2IGMPHostTimeout,'swL2IGMPRouteTimeout':swL2IGMPRouteTimeout,'swL2IGMPLeaveTimer':swL2IGMPLeaveTimer,'swL2IGMPQueryState':swL2IGMPQueryState,'swL2IGMPCurrentState':swL2IGMPCurrentState,'swL2IGMPCtrlState':swL2IGMPCtrlState,'swL2IGMPFastLeave':swL2IGMPFastLeave,'swL2IGMPDynIPMultVlanState':swL2IGMPDynIPMultVlanState,'swL2IGMPDynIPMultVlanAge':swL2IGMPDynIPMultVlanAge,'swL2IGMPQueryInfoTable':swL2IGMPQueryInfoTable,'swL2IGMPQueryInfoEntry':swL2IGMPQueryInfoEntry,_q:swL2IGMPInfoVid,'swL2IGMPInfoQueryCount':swL2IGMPInfoQueryCount,'swL2IGMPInfoTxQueryCount':swL2IGMPInfoTxQueryCount,'swL2IGMPInfoTable':swL2IGMPInfoTable,'swL2IGMPInfoEntry':swL2IGMPInfoEntry,_U:swL2IGMPVid,_V:swL2IGMPGroupIpAddr,'swL2IGMPMacAddr':swL2IGMPMacAddr,'swL2IGMPPortMap':swL2IGMPPortMap,'swL2IGMPIpGroupReportCount':swL2IGMPIpGroupReportCount,'swL2IGMPRouterPortTable':swL2IGMPRouterPortTable,'swL2IGMPRouterPortEntry':swL2IGMPRouterPortEntry,_r:swL2IGMPRouterPortVlanid,'swL2IGMPRouterPortVlanName':swL2IGMPRouterPortVlanName,'swL2IGMPRouterPortStaticPortList':swL2IGMPRouterPortStaticPortList,'swL2IGMPRouterPortDynamicPortList':swL2IGMPRouterPortDynamicPortList,'swL2IGMPRouterPortForbiddenPortList':swL2IGMPRouterPortForbiddenPortList,'swL2IGMPAccessAuthTable':swL2IGMPAccessAuthTable,'swL2IGMPAccessAuthEntry':swL2IGMPAccessAuthEntry,_s:swL2IGMPAccessAuthPort,'swL2IGMPAccessAuthState':swL2IGMPAccessAuthState,'swL2IGMPMulticastVlanTable':swL2IGMPMulticastVlanTable,'swL2IGMPMulticastVlanEntry':swL2IGMPMulticastVlanEntry,_t:swL2IGMPMulticastVlanid,'swL2IGMPMulticastVlanName':swL2IGMPMulticastVlanName,'swL2IGMPMulticastVlanSourcePort':swL2IGMPMulticastVlanSourcePort,'swL2IGMPMulticastVlanMemberPort':swL2IGMPMulticastVlanMemberPort,'swL2IGMPMulticastVlanTagMemberPort':swL2IGMPMulticastVlanTagMemberPort,'swL2IGMPMulticastVlanState':swL2IGMPMulticastVlanState,'swL2IGMPMulticastVlanReplaceSourceIp':swL2IGMPMulticastVlanReplaceSourceIp,'swL2IGMPMulticastVlanRowStatus':swL2IGMPMulticastVlanRowStatus,'swL2IGMPMulticastVlanRemoveAllMcastAddrListAction':swL2IGMPMulticastVlanRemoveAllMcastAddrListAction,'swL2IGMPMulticastVlanUntagSourcePort':swL2IGMPMulticastVlanUntagSourcePort,'swL2IGMPMulticastVlanRemapPriority':swL2IGMPMulticastVlanRemapPriority,'swL2IGMPMulticastVlanReplacePriority':swL2IGMPMulticastVlanReplacePriority,'swL2IGMPMulticastVlanGroupTable':swL2IGMPMulticastVlanGroupTable,'swL2IGMPMulticastVlanGroupEntry':swL2IGMPMulticastVlanGroupEntry,_u:swL2IGMPMulticastVlanGroupVid,_v:swL2IGMPMulticastVlanGroupFromIp,_w:swL2IGMPMulticastVlanGroupToIp,'swL2IGMPMulticastVlanGroupStatus':swL2IGMPMulticastVlanGroupStatus,'swL2IGMPv3Table':swL2IGMPv3Table,'swL2IGMPv3Entry':swL2IGMPv3Entry,_x:swL2IGMPv3SourceIPAddr,'swL2IGMPv3Forwarding':swL2IGMPv3Forwarding,'swL2IGMPv3ExpireTimer':swL2IGMPv3ExpireTimer,'swIGMPSnoopingGroupTable':swIGMPSnoopingGroupTable,'swIGMPSnoopingGroupEntry':swIGMPSnoopingGroupEntry,_y:swIGMPSnoopingGroupVid,_z:swIGMPSnoopingGroupGroupAddr,_A0:swIGMPSnoopingGroupSourceAddr,'swIGMPSnoopingGroupIncludePortMap':swIGMPSnoopingGroupIncludePortMap,'swIGMPSnoopingGroupExcludePortMap':swIGMPSnoopingGroupExcludePortMap,'swIGMPSnoopingGroupReportCount':swIGMPSnoopingGroupReportCount,'swIGMPSnoopingGroupUpTime':swIGMPSnoopingGroupUpTime,'swIGMPSnoopingGroupExpiryTime':swIGMPSnoopingGroupExpiryTime,'swIGMPSnoopingGroupRouterPorts':swIGMPSnoopingGroupRouterPorts,'swL2IGMPDynIpMultMgmt':swL2IGMPDynIpMultMgmt,'swL2IGMPDynIPMultMaxEntry':swL2IGMPDynIPMultMaxEntry,'swL2IGMPSnoopingClearDynIpMult':swL2IGMPSnoopingClearDynIpMult,'swL2IGMPSnoopingClearDynIpMultVID':swL2IGMPSnoopingClearDynIpMultVID,'swL2IGMPSnoopingClearDynIpMultIP':swL2IGMPSnoopingClearDynIpMultIP,'swL2IGMPSnoopingClearDynIpMultAction':swL2IGMPSnoopingClearDynIpMultAction,'swL2TrafficSegMgmt':swL2TrafficSegMgmt,'swL2TrafficSegTable':swL2TrafficSegTable,'swL2TrafficSegEntry':swL2TrafficSegEntry,_A1:swL2TrafficSegPort,'swL2TrafficSegForwardPorts':swL2TrafficSegForwardPorts,'swL2PortSecurityMgmt':swL2PortSecurityMgmt,'swL2PortSecurityControlTable':swL2PortSecurityControlTable,'swL2PortSecurityControlEntry':swL2PortSecurityControlEntry,_X:swL2PortSecurityPortIndex,'swL2PortSecurityMaxLernAddr':swL2PortSecurityMaxLernAddr,'swL2PortSecurityMode':swL2PortSecurityMode,'swL2PortSecurityAdmState':swL2PortSecurityAdmState,'swL2PortSecurityTrapLogState':swL2PortSecurityTrapLogState,'swL2PortSecurityDelCtrl':swL2PortSecurityDelCtrl,'swL2PortSecurityDelVlanName':swL2PortSecurityDelVlanName,'swL2PortSecurityDelPort':swL2PortSecurityDelPort,'swL2PortSecurityDelMacAddress':swL2PortSecurityDelMacAddress,'swL2PortSecurityDelActivity':swL2PortSecurityDelActivity,'swL2CosMgmt':swL2CosMgmt,'swL2CosPriorityCtrl':swL2CosPriorityCtrl,'swL2CosPriorityTable':swL2CosPriorityTable,'swL2CosPriorityEntry':swL2CosPriorityEntry,_A2:swL2CosPriorityPort,'swL2CosPriorityPortPRI':swL2CosPriorityPortPRI,'swL2CosPriorityEtherPRI':swL2CosPriorityEtherPRI,'swL2CosPriorityIpPRI':swL2CosPriorityIpPRI,'swL2CosPriorityNone':swL2CosPriorityNone,'swL2CosPortPRITable':swL2CosPortPRITable,'swL2CosPortPRIEntry':swL2CosPortPRIEntry,_A3:swL2CosPortPRIIndex,'swL2CosPortPRIClass':swL2CosPortPRIClass,'swL2CosMacBasePRITable':swL2CosMacBasePRITable,'swL2CosMacBasePRIEntry':swL2CosMacBasePRIEntry,_A4:swL2CosMacBasePRIIndex,'swL2CosMacBasePRIClass':swL2CosMacBasePRIClass,'swL2CosTosPRITable':swL2CosTosPRITable,'swL2CosTosPRIEntry':swL2CosTosPRIEntry,_A5:swL2CosTosPRIIndex,'swL2CosTosPRIClass':swL2CosTosPRIClass,'swL2CosDscpPRITable':swL2CosDscpPRITable,'swL2CosDscpPRIEntry':swL2CosDscpPRIEntry,_A6:swL2CosDscpPRIIndex,'swL2CosDscpPRIClass':swL2CosDscpPRIClass,'swL2DhcpRelayMgmt':swL2DhcpRelayMgmt,'swL2DhcpRelayState':swL2DhcpRelayState,'swL2DhcpRelayHopCount':swL2DhcpRelayHopCount,'swL2DhcpRelayTimeThreshold':swL2DhcpRelayTimeThreshold,'swL2DhcpRelayOption82State':swL2DhcpRelayOption82State,'swL2DhcpRelayOption82Check':swL2DhcpRelayOption82Check,'swL2DhcpRelayOption82Policy':swL2DhcpRelayOption82Policy,'swL2DhcpRelayCtrlTable':swL2DhcpRelayCtrlTable,'swL2DhcpRelayCtrlEntry':swL2DhcpRelayCtrlEntry,_A7:swL2DhcpRelayCtrlInterfaceName,_A8:swL2DhcpRelayCtrlServer,'swL2DhcpRelayCtrlState':swL2DhcpRelayCtrlState,'swL2MgmtMIBTraps':swL2MgmtMIBTraps,'swL2MgmtMIBTrapPrefix':swL2MgmtMIBTrapPrefix,'swL2PortSecurityViolationTrap':swL2PortSecurityViolationTrap,'swL2macNotification':swL2macNotification,'swL2FloodMacDetectedTrap':swL2FloodMacDetectedTrap,'swL2PortLoopOccurred':swL2PortLoopOccurred,'swL2PortLoopRestart':swL2PortLoopRestart,'swl2PortSecurityBindings':swl2PortSecurityBindings,_AI:swL2PortSecurityViolationMac,'swl2NotificationBindings':swl2NotificationBindings,_AJ:swL2macNotifyInfo,_AK:swL2FloodMacDetectedMacVid,_AL:swL2FloodMacDetectedMacAddress,'swL2LoopDetectMgmt':swL2LoopDetectMgmt,'swL2LoopDetectCtrl':swL2LoopDetectCtrl,'swL2LoopDetectAdminState':swL2LoopDetectAdminState,'swL2LoopDetectInterval':swL2LoopDetectInterval,'swL2LoopDetectRecoverTime':swL2LoopDetectRecoverTime,'swL2LoopDetectTrapMode':swL2LoopDetectTrapMode,'swL2LoopDetectPortMgmt':swL2LoopDetectPortMgmt,'swL2LoopDetectPortTable':swL2LoopDetectPortTable,'swL2LoopDetectPortEntry':swL2LoopDetectPortEntry,_O:swL2LoopDetectPortIndex,'swL2LoopDetectPortState':swL2LoopDetectPortState,'swL2LoopDetectPortLoopStatus':swL2LoopDetectPortLoopStatus,'swL2MultiFilter':swL2MultiFilter,'swL2McastFilterTable':swL2McastFilterTable,'swL2McastFilterEntry':swL2McastFilterEntry,_A9:swL2McastFilterProfileIndex,'swL2McastFilterProfileName':swL2McastFilterProfileName,'swL2McastFilterAddOrDelState':swL2McastFilterAddOrDelState,'swL2McastFilterGroupList':swL2McastFilterGroupList,'swL2McastFilterStatus':swL2McastFilterStatus,'swL2McastFilterPortTable':swL2McastFilterPortTable,'swL2McastFilterPortEntry':swL2McastFilterPortEntry,_AA:swL2McastFilterPortGroupPortIndex,'swL2McastFilterPortProfileAddOrDelState':swL2McastFilterPortProfileAddOrDelState,'swL2McastFilterPortProfileID':swL2McastFilterPortProfileID,'swL2McastFilterPortMaxGroupTable':swL2McastFilterPortMaxGroupTable,'swL2McastFilterPortMaxGroupEntry':swL2McastFilterPortMaxGroupEntry,_AB:swL2McastFilterPortMaxGroupPortIndex,'swL2McastFilterPortMaxGroup':swL2McastFilterPortMaxGroup,'swL2McastFilterPortInfoTable':swL2McastFilterPortInfoTable,'swL2McastFilterPortInfoEntry':swL2McastFilterPortInfoEntry,_AC:swL2McastFilterPortInfoPortIndex,'swL2McastFilterPortInfoProfileName':swL2McastFilterPortInfoProfileName,'swL2VlanMgmt':swL2VlanMgmt,'swL2VlanAdvertisementTable':swL2VlanAdvertisementTable,'swL2VlanAdvertisementEntry':swL2VlanAdvertisementEntry,_AD:swL2VlanIndex,'swL2VlanName':swL2VlanName,'swL2VlanAdvertiseState':swL2VlanAdvertiseState,'swL2VlanMultiplyMgmt':swL2VlanMultiplyMgmt,'swL2VlanMultiplyVlanList':swL2VlanMultiplyVlanList,'swL2VlanMultiplyAdvertisement':swL2VlanMultiplyAdvertisement,'swL2VlanMultiplyPortList':swL2VlanMultiplyPortList,'swL2VlanMultiplyPortListAction':swL2VlanMultiplyPortListAction,'swL2VlanMultiplyAction':swL2VlanMultiplyAction,'swL2DhcpLocalRelayMgmt':swL2DhcpLocalRelayMgmt,'swL2DhcpLocalRelayState':swL2DhcpLocalRelayState,'swL2DhcpLocalRelayVLANTable':swL2DhcpLocalRelayVLANTable,'swL2DhcpLocalRelayVLANEntry':swL2DhcpLocalRelayVLANEntry,_AE:swL2DhcpLocalRelayVLANID,'swL2DhcpLocalRelayVLANState':swL2DhcpLocalRelayVLANState,'swL2FloodMAC':swL2FloodMAC,'swL2FloodMACMgmt':swL2FloodMACMgmt,'swL2FloodMACGlobalSettings':swL2FloodMACGlobalSettings,'swL2FloodMACState':swL2FloodMACState,'swL2FloodMACLogState':swL2FloodMACLogState,'swL2FloodMACTrapState':swL2FloodMACTrapState,'swL2FloodMACClearFDB':swL2FloodMACClearFDB,'swL2FloodMACAutoFDBCtrlTable':swL2FloodMACAutoFDBCtrlTable,'swL2FloodMACAutoFDBCtrlEntry':swL2FloodMACAutoFDBCtrlEntry,_Y:swL2FloodMACAutoFDBIPAddress,'swL2FloodMACAutoFDBRowStatus':swL2FloodMACAutoFDBRowStatus,'swL2FloodMACInfo':swL2FloodMACInfo,'swL2FloodMACFDBTable':swL2FloodMACFDBTable,'swL2FloodMACFDBEntry':swL2FloodMACFDBEntry,_AF:swL2FloodMACFDBIndex,_AG:swL2FloodMACFDBVID,_AH:swL2FloodMACFDBMacAddress,'swL2FloodMACFDBStatus':swL2FloodMACFDBStatus,'swL2FloodMACFDBTimestamp':swL2FloodMACFDBTimestamp,'swL2FloodMACAutoFDBTable':swL2FloodMACAutoFDBTable,'swL2FloodMACAutoFDBEntry':swL2FloodMACAutoFDBEntry,'swL2FloodMACAutoFDBVID':swL2FloodMACAutoFDBVID,'swL2FloodMACAutoFDBMacAddress':swL2FloodMACAutoFDBMacAddress,'swL2FloodMACAutoFDBPort':swL2FloodMACAutoFDBPort,'swL2FloodMACAutoFDBTimestamp':swL2FloodMACAutoFDBTimestamp})