_B3='swL2IpMacBindingViolationMac'
_B2='swL2IpMacBindingViolationIP'
_B1='swL2PortSecurityViolationMac'
_B0='swL2PortInfoType'
_A_='swL2macNotifyInfo'
_Az='swL2DhcpLocalRelayVLANID'
_Ay='swL2TrafficSegPort'
_Ax='swL2DhcpRelayCtrlServer'
_Aw='swL2DhcpRelayCtrlInterfaceName'
_Av='swL2IGMPRouterPortVlanid'
_Au='swL2IGMPMulticastVlanid'
_At='swL2IGMPGroupIpAddr'
_As='swL2IGMPVid'
_Ar='swL2IGMPInfoVid'
_Aq='swL2IGMPCtrlVid'
_Ap='swL2TrunkIndex'
_Ao='swL2IpMacBindingPermitIPPoolEndIP'
_An='swL2IpMacBindingPermitIPPoolStartIP'
_Am='swL2IpMacBindingDHCPSnoopIpIndex'
_Al='swL2IpMacBindingBlockedMac'
_Ak='swL2IpMacBindingBlockedVID'
_Aj='swL2IpMacBindingIpIndex'
_Ai='enable-loose'
_Ah='enable-strict'
_Ag='swL2QOS8021pDefaultPriorityIndex'
_Af='swL2QOS8021pUserPriorityIndex'
_Ae='swL2QOSSchedulingClassIndex'
_Ad='swL2QOSBandwidthPortIndex'
_Ac='swL2LimitedMulticastID'
_Ab='swL2MulticastRangeName'
_Aa='swL2PortControlMediumType'
_AZ='swL2PortControlPortIndex'
_AY='swL2PortInformationMediumType'
_AX='swL2PortInformationPortIndex'
_AW='filter-unregistered-groups'
_AV='forward-unregistered-groups'
_AU='forward-all-groups'
_AT='nway-disabled-1Gigabps-Full'
_AS='nway-disabled-1Gigabps-Half'
_AR='nway-disabled-100Mbps-Full'
_AQ='nway-disabled-100Mbps-Half'
_AP='nway-disabled-10Mbps-Full'
_AO='nway-disabled-10Mbps-Half'
_AN='nway-enabled'
_AM='swL2PortCtrlPortIndex'
_AL='moduleType-BaseModule-24PORT'
_AK='moduleType-2P-100TX'
_AJ='moduleType-2P-100FL'
_AI='moduleType-1P-100FL'
_AH='moduleType-2P-100FX-NEW'
_AG='moduleType-1P-100FX'
_AF='moduleType-2P-100FX'
_AE='moduleType-2P-STACK'
_AD='moduleType-1P-GBIC-1P-STACK'
_AC='moduleType-1P-GBIC-1P-TX'
_AB='moduleType-2P-GBIC'
_AA='moduleType-1P-GBIC'
_A9='moduleType-2P-MTRJ-LX'
_A8='moduleType-1P-MTRJ-LX'
_A7='moduleType-2P-MTRJ-SX'
_A6='moduleType-1P-MTRJ-SX'
_A5='moduleType-2P-TX'
_A4='moduleType-1P-TX'
_A3='moduleType-2P-SC-LX'
_A2='moduleType-1P-SC-LX'
_A1='moduleType-2P-SC-SX'
_A0='moduleType-1P-SC-SX'
_z='moduleType-MGBIC'
_y='moduleType-1000T'
_x='moduleType-1394'
_w='moduleType-COMBO'
_v='full-1Gigabps'
_u='half-1Gigabps'
_t='full-100Mbps'
_s='half-100Mbps'
_r='full-10Mbps'
_q='half-10Mbps'
_p='link-fail'
_o='link-pass'
_n='portType-1000Base-1394'
_m='portType-1000Base-TX-GBIC'
_l='portType-1000Base-LX-GBIC'
_k='portType-1000Base-SX-GBIC'
_j='portType-1000Base-LX'
_i='portType-1000Base-SX'
_h='portType-1000Base-TX'
_g='portType-100Base-FL'
_f='portType-100Base-FX'
_e='portType-100Base-TX'
_d='swL2VlanIndex'
_c='OctetString'
_b='swL2VlanLoopDetectVID'
_a='swL2PortSecurityPortIndex'
_Z='swL2IpMacBindingPortIndex'
_Y='swL2LimitedMulticastPort'
_X='swL2PortInfoPortIndex'
_W='active'
_V='SnmpAdminString'
_U='swDevInfoPowerStatus'
_T='accessible-for-notify'
_S='auto'
_R='normal'
_Q='DisplayString'
_P='swDevInfoPowerID'
_O='swDevInfoPowerUnitIndex'
_N='swL2LoopDetectPortIndex'
_M='enable'
_L='none'
_K='disable'
_J='read-create'
_I='obsolete'
_H='enabled'
_G='disabled'
_F='other'
_E='DES3526-L2MGMT-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_c,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_V)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_Q,'MacAddress','PhysAddress','RowStatus','TextualConvention')
des3526,=mibBuilder.importSymbols('SW3500PRIMGMT-MIB','des3526')
swL2MgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,11,64,1,2))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
class VlanIndex(Unsigned32):0
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2DevMgmt_ObjectIdentity=ObjectIdentity
swL2DevMgmt=_SwL2DevMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,1))
_SwL2DevInfo_ObjectIdentity=ObjectIdentity
swL2DevInfo=_SwL2DevInfo_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,1,1))
_SwDevInfoSystemUpTime_Type=TimeTicks
_SwDevInfoSystemUpTime_Object=MibScalar
swDevInfoSystemUpTime=_SwDevInfoSystemUpTime_Object((1,3,6,1,4,1,171,11,64,1,2,1,1,1),_SwDevInfoSystemUpTime_Type())
swDevInfoSystemUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swDevInfoSystemUpTime.setStatus(_A)
class _SwDevInfoTotalNumOfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwDevInfoTotalNumOfPort_Type.__name__=_B
_SwDevInfoTotalNumOfPort_Object=MibScalar
swDevInfoTotalNumOfPort=_SwDevInfoTotalNumOfPort_Object((1,3,6,1,4,1,171,11,64,1,2,1,1,2),_SwDevInfoTotalNumOfPort_Type())
swDevInfoTotalNumOfPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swDevInfoTotalNumOfPort.setStatus(_A)
class _SwDevInfoNumOfPortInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwDevInfoNumOfPortInUse_Type.__name__=_B
_SwDevInfoNumOfPortInUse_Object=MibScalar
swDevInfoNumOfPortInUse=_SwDevInfoNumOfPortInUse_Object((1,3,6,1,4,1,171,11,64,1,2,1,1,3),_SwDevInfoNumOfPortInUse_Type())
swDevInfoNumOfPortInUse.setMaxAccess(_D)
if mibBuilder.loadTexts:swDevInfoNumOfPortInUse.setStatus(_A)
class _SwDevInfoConsoleInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('in-use',2),('not-in-use',3)))
_SwDevInfoConsoleInUse_Type.__name__=_B
_SwDevInfoConsoleInUse_Object=MibScalar
swDevInfoConsoleInUse=_SwDevInfoConsoleInUse_Object((1,3,6,1,4,1,171,11,64,1,2,1,1,4),_SwDevInfoConsoleInUse_Type())
swDevInfoConsoleInUse.setMaxAccess(_D)
if mibBuilder.loadTexts:swDevInfoConsoleInUse.setStatus(_A)
_SwDevInfoModuleType_Type=OctetString
_SwDevInfoModuleType_Object=MibScalar
swDevInfoModuleType=_SwDevInfoModuleType_Object((1,3,6,1,4,1,171,11,64,1,2,1,1,5),_SwDevInfoModuleType_Type())
swDevInfoModuleType.setMaxAccess(_D)
if mibBuilder.loadTexts:swDevInfoModuleType.setStatus(_A)
_SwDevInfoPowerTable_Object=MibTable
swDevInfoPowerTable=_SwDevInfoPowerTable_Object((1,3,6,1,4,1,171,11,64,1,2,1,1,8))
if mibBuilder.loadTexts:swDevInfoPowerTable.setStatus(_A)
_SwDevInfoPowerEntry_Object=MibTableRow
swDevInfoPowerEntry=_SwDevInfoPowerEntry_Object((1,3,6,1,4,1,171,11,64,1,2,1,1,8,1))
swDevInfoPowerEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:swDevInfoPowerEntry.setStatus(_A)
class _SwDevInfoPowerUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwDevInfoPowerUnitIndex_Type.__name__=_B
_SwDevInfoPowerUnitIndex_Object=MibTableColumn
swDevInfoPowerUnitIndex=_SwDevInfoPowerUnitIndex_Object((1,3,6,1,4,1,171,11,64,1,2,1,1,8,1,1),_SwDevInfoPowerUnitIndex_Type())
swDevInfoPowerUnitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swDevInfoPowerUnitIndex.setStatus(_A)
class _SwDevInfoPowerID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwDevInfoPowerID_Type.__name__=_B
_SwDevInfoPowerID_Object=MibTableColumn
swDevInfoPowerID=_SwDevInfoPowerID_Object((1,3,6,1,4,1,171,11,64,1,2,1,1,8,1,2),_SwDevInfoPowerID_Type())
swDevInfoPowerID.setMaxAccess(_D)
if mibBuilder.loadTexts:swDevInfoPowerID.setStatus(_A)
class _SwDevInfoPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_F,0),('lowVoltage',1),('overCurrent',2),('working',3),('fail',4),('connect',5),('disconnect',6)))
_SwDevInfoPowerStatus_Type.__name__=_B
_SwDevInfoPowerStatus_Object=MibTableColumn
swDevInfoPowerStatus=_SwDevInfoPowerStatus_Object((1,3,6,1,4,1,171,11,64,1,2,1,1,8,1,3),_SwDevInfoPowerStatus_Type())
swDevInfoPowerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swDevInfoPowerStatus.setStatus(_A)
_SwL2DevCtrl_ObjectIdentity=ObjectIdentity
swL2DevCtrl=_SwL2DevCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,1,2))
class _SwL2DevCtrlStpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlStpState_Type.__name__=_B
_SwL2DevCtrlStpState_Object=MibScalar
swL2DevCtrlStpState=_SwL2DevCtrlStpState_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,1),_SwL2DevCtrlStpState_Type())
swL2DevCtrlStpState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlStpState.setStatus(_A)
class _SwL2DevCtrlIGMPSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlIGMPSnooping_Type.__name__=_B
_SwL2DevCtrlIGMPSnooping_Object=MibScalar
swL2DevCtrlIGMPSnooping=_SwL2DevCtrlIGMPSnooping_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,2),_SwL2DevCtrlIGMPSnooping_Type())
swL2DevCtrlIGMPSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlIGMPSnooping.setStatus(_A)
class _SwL2DevCtrlRmonState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlRmonState_Type.__name__=_B
_SwL2DevCtrlRmonState_Object=MibScalar
swL2DevCtrlRmonState=_SwL2DevCtrlRmonState_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,3),_SwL2DevCtrlRmonState_Type())
swL2DevCtrlRmonState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlRmonState.setStatus(_A)
class _SwL2DevCtrlCleanAllStatisticCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_W,2)))
_SwL2DevCtrlCleanAllStatisticCounter_Type.__name__=_B
_SwL2DevCtrlCleanAllStatisticCounter_Object=MibScalar
swL2DevCtrlCleanAllStatisticCounter=_SwL2DevCtrlCleanAllStatisticCounter_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,8),_SwL2DevCtrlCleanAllStatisticCounter_Type())
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlCleanAllStatisticCounter.setStatus(_A)
_SwL2DevCtrlVlanIdOfFDBTbl_Type=VlanId
_SwL2DevCtrlVlanIdOfFDBTbl_Object=MibScalar
swL2DevCtrlVlanIdOfFDBTbl=_SwL2DevCtrlVlanIdOfFDBTbl_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,9),_SwL2DevCtrlVlanIdOfFDBTbl_Type())
swL2DevCtrlVlanIdOfFDBTbl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlVlanIdOfFDBTbl.setStatus(_A)
class _SwL2MACNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2MACNotifyState_Type.__name__=_B
_SwL2MACNotifyState_Object=MibScalar
swL2MACNotifyState=_SwL2MACNotifyState_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,10),_SwL2MACNotifyState_Type())
swL2MACNotifyState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MACNotifyState.setStatus(_A)
class _SwL2MACNotifyHistorySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_SwL2MACNotifyHistorySize_Type.__name__=_B
_SwL2MACNotifyHistorySize_Object=MibScalar
swL2MACNotifyHistorySize=_SwL2MACNotifyHistorySize_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,11),_SwL2MACNotifyHistorySize_Type())
swL2MACNotifyHistorySize.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MACNotifyHistorySize.setStatus(_A)
class _SwL2MACNotifyInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SwL2MACNotifyInterval_Type.__name__=_B
_SwL2MACNotifyInterval_Object=MibScalar
swL2MACNotifyInterval=_SwL2MACNotifyInterval_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,12),_SwL2MACNotifyInterval_Type())
swL2MACNotifyInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MACNotifyInterval.setStatus(_A)
class _SwL2DevCtrlAsymVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlAsymVlanState_Type.__name__=_B
_SwL2DevCtrlAsymVlanState_Object=MibScalar
swL2DevCtrlAsymVlanState=_SwL2DevCtrlAsymVlanState_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,13),_SwL2DevCtrlAsymVlanState_Type())
swL2DevCtrlAsymVlanState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlAsymVlanState.setStatus(_A)
_SwL2DevCtrlManagementVlanId_Type=VlanId
_SwL2DevCtrlManagementVlanId_Object=MibScalar
swL2DevCtrlManagementVlanId=_SwL2DevCtrlManagementVlanId_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,14),_SwL2DevCtrlManagementVlanId_Type())
swL2DevCtrlManagementVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlManagementVlanId.setStatus(_A)
_SwL2DevCtrlTelnet_ObjectIdentity=ObjectIdentity
swL2DevCtrlTelnet=_SwL2DevCtrlTelnet_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,1,2,15))
class _SwL2DevCtrlTelnetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlTelnetState_Type.__name__=_B
_SwL2DevCtrlTelnetState_Object=MibScalar
swL2DevCtrlTelnetState=_SwL2DevCtrlTelnetState_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,15,1),_SwL2DevCtrlTelnetState_Type())
swL2DevCtrlTelnetState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlTelnetState.setStatus(_A)
class _SwL2DevCtrlTelnetTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2DevCtrlTelnetTcpPort_Type.__name__=_B
_SwL2DevCtrlTelnetTcpPort_Object=MibScalar
swL2DevCtrlTelnetTcpPort=_SwL2DevCtrlTelnetTcpPort_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,15,2),_SwL2DevCtrlTelnetTcpPort_Type())
swL2DevCtrlTelnetTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlTelnetTcpPort.setStatus(_A)
class _SwL2DevCtrlLLDPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlLLDPState_Type.__name__=_B
_SwL2DevCtrlLLDPState_Object=MibScalar
swL2DevCtrlLLDPState=_SwL2DevCtrlLLDPState_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,16),_SwL2DevCtrlLLDPState_Type())
swL2DevCtrlLLDPState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlLLDPState.setStatus(_A)
_SwL2DevCtrlWeb_ObjectIdentity=ObjectIdentity
swL2DevCtrlWeb=_SwL2DevCtrlWeb_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,1,2,17))
class _SwL2DevCtrlWebState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevCtrlWebState_Type.__name__=_B
_SwL2DevCtrlWebState_Object=MibScalar
swL2DevCtrlWebState=_SwL2DevCtrlWebState_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,17,1),_SwL2DevCtrlWebState_Type())
swL2DevCtrlWebState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlWebState.setStatus(_A)
class _SwL2DevCtrlWebTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2DevCtrlWebTcpPort_Type.__name__=_B
_SwL2DevCtrlWebTcpPort_Object=MibScalar
swL2DevCtrlWebTcpPort=_SwL2DevCtrlWebTcpPort_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,17,2),_SwL2DevCtrlWebTcpPort_Type())
swL2DevCtrlWebTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlWebTcpPort.setStatus(_A)
class _SwL2DevCtrlLLDPForwardMessageState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlLLDPForwardMessageState_Type.__name__=_B
_SwL2DevCtrlLLDPForwardMessageState_Object=MibScalar
swL2DevCtrlLLDPForwardMessageState=_SwL2DevCtrlLLDPForwardMessageState_Object((1,3,6,1,4,1,171,11,64,1,2,1,2,18),_SwL2DevCtrlLLDPForwardMessageState_Type())
swL2DevCtrlLLDPForwardMessageState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlLLDPForwardMessageState.setStatus(_A)
_SwL2DevAlarm_ObjectIdentity=ObjectIdentity
swL2DevAlarm=_SwL2DevAlarm_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,1,3))
class _SwL2DevAlarmNewRoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevAlarmNewRoot_Type.__name__=_B
_SwL2DevAlarmNewRoot_Object=MibScalar
swL2DevAlarmNewRoot=_SwL2DevAlarmNewRoot_Object((1,3,6,1,4,1,171,11,64,1,2,1,3,1),_SwL2DevAlarmNewRoot_Type())
swL2DevAlarmNewRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevAlarmNewRoot.setStatus(_A)
class _SwL2DevAlarmTopologyChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevAlarmTopologyChange_Type.__name__=_B
_SwL2DevAlarmTopologyChange_Object=MibScalar
swL2DevAlarmTopologyChange=_SwL2DevAlarmTopologyChange_Object((1,3,6,1,4,1,171,11,64,1,2,1,3,2),_SwL2DevAlarmTopologyChange_Type())
swL2DevAlarmTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevAlarmTopologyChange.setStatus(_A)
class _SwL2DevAlarmLinkChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DevAlarmLinkChange_Type.__name__=_B
_SwL2DevAlarmLinkChange_Object=MibScalar
swL2DevAlarmLinkChange=_SwL2DevAlarmLinkChange_Object((1,3,6,1,4,1,171,11,64,1,2,1,3,3),_SwL2DevAlarmLinkChange_Type())
swL2DevAlarmLinkChange.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevAlarmLinkChange.setStatus(_A)
_SwL2VlanMgmt_ObjectIdentity=ObjectIdentity
swL2VlanMgmt=_SwL2VlanMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,3))
_SwL2VlanAdvertisementTable_Object=MibTable
swL2VlanAdvertisementTable=_SwL2VlanAdvertisementTable_Object((1,3,6,1,4,1,171,11,64,1,2,3,1))
if mibBuilder.loadTexts:swL2VlanAdvertisementTable.setStatus(_A)
_SwL2VlanAdvertisementEntry_Object=MibTableRow
swL2VlanAdvertisementEntry=_SwL2VlanAdvertisementEntry_Object((1,3,6,1,4,1,171,11,64,1,2,3,1,1))
swL2VlanAdvertisementEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:swL2VlanAdvertisementEntry.setStatus(_A)
class _SwL2VlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2VlanIndex_Type.__name__=_B
_SwL2VlanIndex_Object=MibTableColumn
swL2VlanIndex=_SwL2VlanIndex_Object((1,3,6,1,4,1,171,11,64,1,2,3,1,1,1),_SwL2VlanIndex_Type())
swL2VlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanIndex.setStatus(_A)
class _SwL2VlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2VlanName_Type.__name__=_Q
_SwL2VlanName_Object=MibTableColumn
swL2VlanName=_SwL2VlanName_Object((1,3,6,1,4,1,171,11,64,1,2,3,1,1,2),_SwL2VlanName_Type())
swL2VlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanName.setStatus(_A)
class _SwL2VlanAdvertiseState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2VlanAdvertiseState_Type.__name__=_B
_SwL2VlanAdvertiseState_Object=MibTableColumn
swL2VlanAdvertiseState=_SwL2VlanAdvertiseState_Object((1,3,6,1,4,1,171,11,64,1,2,3,1,1,3),_SwL2VlanAdvertiseState_Type())
swL2VlanAdvertiseState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanAdvertiseState.setStatus(_A)
_SwL2PortMgmt_ObjectIdentity=ObjectIdentity
swL2PortMgmt=_SwL2PortMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,4))
_SwL2PortInfoTable_Object=MibTable
swL2PortInfoTable=_SwL2PortInfoTable_Object((1,3,6,1,4,1,171,11,64,1,2,4,1))
if mibBuilder.loadTexts:swL2PortInfoTable.setStatus(_I)
_SwL2PortInfoEntry_Object=MibTableRow
swL2PortInfoEntry=_SwL2PortInfoEntry_Object((1,3,6,1,4,1,171,11,64,1,2,4,1,1))
swL2PortInfoEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:swL2PortInfoEntry.setStatus(_I)
class _SwL2PortInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortInfoPortIndex_Type.__name__=_B
_SwL2PortInfoPortIndex_Object=MibTableColumn
swL2PortInfoPortIndex=_SwL2PortInfoPortIndex_Object((1,3,6,1,4,1,171,11,64,1,2,4,1,1,1),_SwL2PortInfoPortIndex_Type())
swL2PortInfoPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoPortIndex.setStatus(_I)
class _SwL2PortInfoUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortInfoUnitIndex_Type.__name__=_B
_SwL2PortInfoUnitIndex_Object=MibTableColumn
swL2PortInfoUnitIndex=_SwL2PortInfoUnitIndex_Object((1,3,6,1,4,1,171,11,64,1,2,4,1,1,2),_SwL2PortInfoUnitIndex_Type())
swL2PortInfoUnitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoUnitIndex.setStatus(_I)
class _SwL2PortInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3),(_h,4),(_i,5),(_j,6),(_k,7),(_l,8),(_m,9),(_n,10),(_L,11)))
_SwL2PortInfoType_Type.__name__=_B
_SwL2PortInfoType_Object=MibTableColumn
swL2PortInfoType=_SwL2PortInfoType_Object((1,3,6,1,4,1,171,11,64,1,2,4,1,1,3),_SwL2PortInfoType_Type())
swL2PortInfoType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoType.setStatus(_I)
class _SwL2PortInfoLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_o,2),(_p,3)))
_SwL2PortInfoLinkStatus_Type.__name__=_B
_SwL2PortInfoLinkStatus_Object=MibTableColumn
swL2PortInfoLinkStatus=_SwL2PortInfoLinkStatus_Object((1,3,6,1,4,1,171,11,64,1,2,4,1,1,4),_SwL2PortInfoLinkStatus_Type())
swL2PortInfoLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoLinkStatus.setStatus(_I)
class _SwL2PortInfoNwayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_F,1),(_S,2),(_q,3),(_r,4),(_s,5),(_t,6),(_u,7),(_v,8)))
_SwL2PortInfoNwayStatus_Type.__name__=_B
_SwL2PortInfoNwayStatus_Object=MibTableColumn
swL2PortInfoNwayStatus=_SwL2PortInfoNwayStatus_Object((1,3,6,1,4,1,171,11,64,1,2,4,1,1,5),_SwL2PortInfoNwayStatus_Type())
swL2PortInfoNwayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoNwayStatus.setStatus(_I)
class _SwL2PortInfoModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*((_L,0),(_w,1),(_x,2),(_y,3),(_z,4),(_A0,5),(_A1,6),(_A2,7),(_A3,8),(_A4,9),(_A5,10),(_A6,11),(_A7,12),(_A8,13),(_A9,14),(_AA,15),(_AB,16),(_AC,17),(_AD,18),(_AE,19),(_AF,20),(_AG,21),(_AH,22),(_AI,23),(_AJ,24),(_AK,25),(_AL,26)))
_SwL2PortInfoModuleType_Type.__name__=_B
_SwL2PortInfoModuleType_Object=MibTableColumn
swL2PortInfoModuleType=_SwL2PortInfoModuleType_Object((1,3,6,1,4,1,171,11,64,1,2,4,1,1,6),_SwL2PortInfoModuleType_Type())
swL2PortInfoModuleType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoModuleType.setStatus(_I)
class _SwL2PortInfoErrorDisabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_L,0),('storm',1),('lbd',2),('unknow',3)))
_SwL2PortInfoErrorDisabled_Type.__name__=_B
_SwL2PortInfoErrorDisabled_Object=MibTableColumn
swL2PortInfoErrorDisabled=_SwL2PortInfoErrorDisabled_Object((1,3,6,1,4,1,171,11,64,1,2,4,1,1,7),_SwL2PortInfoErrorDisabled_Type())
swL2PortInfoErrorDisabled.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoErrorDisabled.setStatus(_I)
_SwL2PortCtrlTable_Object=MibTable
swL2PortCtrlTable=_SwL2PortCtrlTable_Object((1,3,6,1,4,1,171,11,64,1,2,4,2))
if mibBuilder.loadTexts:swL2PortCtrlTable.setStatus(_I)
_SwL2PortCtrlEntry_Object=MibTableRow
swL2PortCtrlEntry=_SwL2PortCtrlEntry_Object((1,3,6,1,4,1,171,11,64,1,2,4,2,1))
swL2PortCtrlEntry.setIndexNames((0,_E,_AM))
if mibBuilder.loadTexts:swL2PortCtrlEntry.setStatus(_I)
class _SwL2PortCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortCtrlPortIndex_Type.__name__=_B
_SwL2PortCtrlPortIndex_Object=MibTableColumn
swL2PortCtrlPortIndex=_SwL2PortCtrlPortIndex_Object((1,3,6,1,4,1,171,11,64,1,2,4,2,1,1),_SwL2PortCtrlPortIndex_Type())
swL2PortCtrlPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlPortIndex.setStatus(_I)
class _SwL2PortCtrlUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortCtrlUnitIndex_Type.__name__=_B
_SwL2PortCtrlUnitIndex_Object=MibTableColumn
swL2PortCtrlUnitIndex=_SwL2PortCtrlUnitIndex_Object((1,3,6,1,4,1,171,11,64,1,2,4,2,1,2),_SwL2PortCtrlUnitIndex_Type())
swL2PortCtrlUnitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlUnitIndex.setStatus(_I)
class _SwL2PortCtrlAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortCtrlAdminState_Type.__name__=_B
_SwL2PortCtrlAdminState_Object=MibTableColumn
swL2PortCtrlAdminState=_SwL2PortCtrlAdminState_Object((1,3,6,1,4,1,171,11,64,1,2,4,2,1,3),_SwL2PortCtrlAdminState_Type())
swL2PortCtrlAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlAdminState.setStatus(_I)
class _SwL2PortCtrlNwayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_F,1),(_AN,2),(_AO,3),(_AP,4),(_AQ,5),(_AR,6),(_AS,7),(_AT,8)))
_SwL2PortCtrlNwayState_Type.__name__=_B
_SwL2PortCtrlNwayState_Object=MibTableColumn
swL2PortCtrlNwayState=_SwL2PortCtrlNwayState_Object((1,3,6,1,4,1,171,11,64,1,2,4,2,1,4),_SwL2PortCtrlNwayState_Type())
swL2PortCtrlNwayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlNwayState.setStatus(_I)
class _SwL2PortCtrlFlowCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortCtrlFlowCtrlState_Type.__name__=_B
_SwL2PortCtrlFlowCtrlState_Object=MibTableColumn
swL2PortCtrlFlowCtrlState=_SwL2PortCtrlFlowCtrlState_Object((1,3,6,1,4,1,171,11,64,1,2,4,2,1,5),_SwL2PortCtrlFlowCtrlState_Type())
swL2PortCtrlFlowCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlFlowCtrlState.setStatus(_I)
class _SwL2PortCtrlLockState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortCtrlLockState_Type.__name__=_B
_SwL2PortCtrlLockState_Object=MibTableColumn
swL2PortCtrlLockState=_SwL2PortCtrlLockState_Object((1,3,6,1,4,1,171,11,64,1,2,4,2,1,6),_SwL2PortCtrlLockState_Type())
swL2PortCtrlLockState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlLockState.setStatus(_I)
class _SwL2PortCtrlMACNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortCtrlMACNotifyState_Type.__name__=_B
_SwL2PortCtrlMACNotifyState_Object=MibTableColumn
swL2PortCtrlMACNotifyState=_SwL2PortCtrlMACNotifyState_Object((1,3,6,1,4,1,171,11,64,1,2,4,2,1,7),_SwL2PortCtrlMACNotifyState_Type())
swL2PortCtrlMACNotifyState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlMACNotifyState.setStatus(_I)
class _SwL2PortCtrlMulticastfilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_AU,1),(_AV,2),(_AW,3)))
_SwL2PortCtrlMulticastfilter_Type.__name__=_B
_SwL2PortCtrlMulticastfilter_Object=MibTableColumn
swL2PortCtrlMulticastfilter=_SwL2PortCtrlMulticastfilter_Object((1,3,6,1,4,1,171,11,64,1,2,4,2,1,8),_SwL2PortCtrlMulticastfilter_Type())
swL2PortCtrlMulticastfilter.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlMulticastfilter.setStatus(_I)
class _SwL2PortCtrlMdixState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),(_R,2),('cross',3)))
_SwL2PortCtrlMdixState_Type.__name__=_B
_SwL2PortCtrlMdixState_Object=MibTableColumn
swL2PortCtrlMdixState=_SwL2PortCtrlMdixState_Object((1,3,6,1,4,1,171,11,64,1,2,4,2,1,11),_SwL2PortCtrlMdixState_Type())
swL2PortCtrlMdixState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlMdixState.setStatus(_I)
_SwL2PortInformationTable_Object=MibTable
swL2PortInformationTable=_SwL2PortInformationTable_Object((1,3,6,1,4,1,171,11,64,1,2,4,4))
if mibBuilder.loadTexts:swL2PortInformationTable.setStatus(_A)
_SwL2PortInformationEntry_Object=MibTableRow
swL2PortInformationEntry=_SwL2PortInformationEntry_Object((1,3,6,1,4,1,171,11,64,1,2,4,4,1))
swL2PortInformationEntry.setIndexNames((0,_E,_AX),(0,_E,_AY))
if mibBuilder.loadTexts:swL2PortInformationEntry.setStatus(_A)
class _SwL2PortInformationPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortInformationPortIndex_Type.__name__=_B
_SwL2PortInformationPortIndex_Object=MibTableColumn
swL2PortInformationPortIndex=_SwL2PortInformationPortIndex_Object((1,3,6,1,4,1,171,11,64,1,2,4,4,1,1),_SwL2PortInformationPortIndex_Type())
swL2PortInformationPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInformationPortIndex.setStatus(_A)
class _SwL2PortInformationMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('copper',1),('fiber',2)))
_SwL2PortInformationMediumType_Type.__name__=_B
_SwL2PortInformationMediumType_Object=MibTableColumn
swL2PortInformationMediumType=_SwL2PortInformationMediumType_Object((1,3,6,1,4,1,171,11,64,1,2,4,4,1,2),_SwL2PortInformationMediumType_Type())
swL2PortInformationMediumType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInformationMediumType.setStatus(_A)
class _SwL2PortInformationUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortInformationUnitID_Type.__name__=_B
_SwL2PortInformationUnitID_Object=MibTableColumn
swL2PortInformationUnitID=_SwL2PortInformationUnitID_Object((1,3,6,1,4,1,171,11,64,1,2,4,4,1,3),_SwL2PortInformationUnitID_Type())
swL2PortInformationUnitID.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInformationUnitID.setStatus(_A)
class _SwL2PortInformationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3),(_h,4),(_i,5),(_j,6),(_k,7),(_l,8),(_m,9),(_n,10),('portType-1000Base-TX-GBIC-COMBO',11),('portType-1000Base-none-GBIC',12),('portType-1000Base-SX-MGBIC',13),('portType-1000Base-LX-MGBIC',14),('portType-1000Base-TX-MGBIC',15),('portType-1000Base-none-MGBIC',16),('portType-SIO',17),('portType-10G',18),('portType-10G-xenpak-1310nm',19),('portType-10G-xenpak-850nm',20),('portType-10G-xenpak-empty',21),('portType-10G-xfp-1310nm',22),('portType-10G-xfp-850nm',23),('portType-10G-xfp-empty',24),('portType-none',25)))
_SwL2PortInformationType_Type.__name__=_B
_SwL2PortInformationType_Object=MibTableColumn
swL2PortInformationType=_SwL2PortInformationType_Object((1,3,6,1,4,1,171,11,64,1,2,4,4,1,4),_SwL2PortInformationType_Type())
swL2PortInformationType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInformationType.setStatus(_A)
class _SwL2PortInformationLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_o,2),(_p,3)))
_SwL2PortInformationLinkStatus_Type.__name__=_B
_SwL2PortInformationLinkStatus_Object=MibTableColumn
swL2PortInformationLinkStatus=_SwL2PortInformationLinkStatus_Object((1,3,6,1,4,1,171,11,64,1,2,4,4,1,5),_SwL2PortInformationLinkStatus_Type())
swL2PortInformationLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInformationLinkStatus.setStatus(_A)
class _SwL2PortInformationNwayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_F,0),('empty',1),('link-down',2),(_q,3),(_r,4),(_s,5),(_t,6),(_u,7),(_v,8),('full-10Gigabps',9)))
_SwL2PortInformationNwayStatus_Type.__name__=_B
_SwL2PortInformationNwayStatus_Object=MibTableColumn
swL2PortInformationNwayStatus=_SwL2PortInformationNwayStatus_Object((1,3,6,1,4,1,171,11,64,1,2,4,4,1,6),_SwL2PortInformationNwayStatus_Type())
swL2PortInformationNwayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInformationNwayStatus.setStatus(_A)
class _SwL2PortInformationModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*((_L,0),(_w,1),(_x,2),(_y,3),(_z,4),(_A0,5),(_A1,6),(_A2,7),(_A3,8),(_A4,9),(_A5,10),(_A6,11),(_A7,12),(_A8,13),(_A9,14),(_AA,15),(_AB,16),(_AC,17),(_AD,18),(_AE,19),(_AF,20),(_AG,21),(_AH,22),(_AI,23),(_AJ,24),(_AK,25),(_AL,26)))
_SwL2PortInformationModuleType_Type.__name__=_B
_SwL2PortInformationModuleType_Object=MibTableColumn
swL2PortInformationModuleType=_SwL2PortInformationModuleType_Object((1,3,6,1,4,1,171,11,64,1,2,4,4,1,7),_SwL2PortInformationModuleType_Type())
swL2PortInformationModuleType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInformationModuleType.setStatus(_A)
class _SwL2PortInformationErrorDisabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_L,0),('storm',1),('lbd',2),('unknow',3)))
_SwL2PortInformationErrorDisabled_Type.__name__=_B
_SwL2PortInformationErrorDisabled_Object=MibTableColumn
swL2PortInformationErrorDisabled=_SwL2PortInformationErrorDisabled_Object((1,3,6,1,4,1,171,11,64,1,2,4,4,1,8),_SwL2PortInformationErrorDisabled_Type())
swL2PortInformationErrorDisabled.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInformationErrorDisabled.setStatus(_A)
_SwL2PortControlTable_Object=MibTable
swL2PortControlTable=_SwL2PortControlTable_Object((1,3,6,1,4,1,171,11,64,1,2,4,5))
if mibBuilder.loadTexts:swL2PortControlTable.setStatus(_A)
_SwL2PortControlEntry_Object=MibTableRow
swL2PortControlEntry=_SwL2PortControlEntry_Object((1,3,6,1,4,1,171,11,64,1,2,4,5,1))
swL2PortControlEntry.setIndexNames((0,_E,_AZ),(0,_E,_Aa))
if mibBuilder.loadTexts:swL2PortControlEntry.setStatus(_A)
class _SwL2PortControlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortControlPortIndex_Type.__name__=_B
_SwL2PortControlPortIndex_Object=MibTableColumn
swL2PortControlPortIndex=_SwL2PortControlPortIndex_Object((1,3,6,1,4,1,171,11,64,1,2,4,5,1,1),_SwL2PortControlPortIndex_Type())
swL2PortControlPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortControlPortIndex.setStatus(_A)
class _SwL2PortControlMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('copper',1),('fiber',2)))
_SwL2PortControlMediumType_Type.__name__=_B
_SwL2PortControlMediumType_Object=MibTableColumn
swL2PortControlMediumType=_SwL2PortControlMediumType_Object((1,3,6,1,4,1,171,11,64,1,2,4,5,1,2),_SwL2PortControlMediumType_Type())
swL2PortControlMediumType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortControlMediumType.setStatus(_A)
class _SwL2PortControlUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortControlUnitIndex_Type.__name__=_B
_SwL2PortControlUnitIndex_Object=MibTableColumn
swL2PortControlUnitIndex=_SwL2PortControlUnitIndex_Object((1,3,6,1,4,1,171,11,64,1,2,4,5,1,3),_SwL2PortControlUnitIndex_Type())
swL2PortControlUnitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortControlUnitIndex.setStatus(_A)
class _SwL2PortControlAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortControlAdminState_Type.__name__=_B
_SwL2PortControlAdminState_Object=MibTableColumn
swL2PortControlAdminState=_SwL2PortControlAdminState_Object((1,3,6,1,4,1,171,11,64,1,2,4,5,1,4),_SwL2PortControlAdminState_Type())
swL2PortControlAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortControlAdminState.setStatus(_A)
class _SwL2PortControlNwayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_F,1),(_AN,2),(_AO,3),(_AP,4),(_AQ,5),(_AR,6),(_AS,7),(_AT,8),('nway-disabled-1Gigabps-Full-master',9),('nway-disabled-1Gigabps-Full-slave',10)))
_SwL2PortControlNwayState_Type.__name__=_B
_SwL2PortControlNwayState_Object=MibTableColumn
swL2PortControlNwayState=_SwL2PortControlNwayState_Object((1,3,6,1,4,1,171,11,64,1,2,4,5,1,5),_SwL2PortControlNwayState_Type())
swL2PortControlNwayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortControlNwayState.setStatus(_A)
class _SwL2PortControlFlowCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortControlFlowCtrlState_Type.__name__=_B
_SwL2PortControlFlowCtrlState_Object=MibTableColumn
swL2PortControlFlowCtrlState=_SwL2PortControlFlowCtrlState_Object((1,3,6,1,4,1,171,11,64,1,2,4,5,1,6),_SwL2PortControlFlowCtrlState_Type())
swL2PortControlFlowCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortControlFlowCtrlState.setStatus(_A)
class _SwL2PortControlLockState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortControlLockState_Type.__name__=_B
_SwL2PortControlLockState_Object=MibTableColumn
swL2PortControlLockState=_SwL2PortControlLockState_Object((1,3,6,1,4,1,171,11,64,1,2,4,5,1,7),_SwL2PortControlLockState_Type())
swL2PortControlLockState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortControlLockState.setStatus(_I)
class _SwL2PortControlMACNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2PortControlMACNotifyState_Type.__name__=_B
_SwL2PortControlMACNotifyState_Object=MibTableColumn
swL2PortControlMACNotifyState=_SwL2PortControlMACNotifyState_Object((1,3,6,1,4,1,171,11,64,1,2,4,5,1,8),_SwL2PortControlMACNotifyState_Type())
swL2PortControlMACNotifyState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortControlMACNotifyState.setStatus(_A)
class _SwL2PortControlMulticastfilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_AU,1),(_AV,2),(_AW,3)))
_SwL2PortControlMulticastfilter_Type.__name__=_B
_SwL2PortControlMulticastfilter_Object=MibTableColumn
swL2PortControlMulticastfilter=_SwL2PortControlMulticastfilter_Object((1,3,6,1,4,1,171,11,64,1,2,4,5,1,9),_SwL2PortControlMulticastfilter_Type())
swL2PortControlMulticastfilter.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortControlMulticastfilter.setStatus(_A)
class _SwL2PortControlMdixState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),(_R,2),('cross',3)))
_SwL2PortControlMdixState_Type.__name__=_B
_SwL2PortControlMdixState_Object=MibTableColumn
swL2PortControlMdixState=_SwL2PortControlMdixState_Object((1,3,6,1,4,1,171,11,64,1,2,4,5,1,11),_SwL2PortControlMdixState_Type())
swL2PortControlMdixState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortControlMdixState.setStatus(_A)
_SwL2LimitedMulticastMgmt_ObjectIdentity=ObjectIdentity
swL2LimitedMulticastMgmt=_SwL2LimitedMulticastMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,5))
_SwL2MulticastRangeTable_Object=MibTable
swL2MulticastRangeTable=_SwL2MulticastRangeTable_Object((1,3,6,1,4,1,171,11,64,1,2,5,1))
if mibBuilder.loadTexts:swL2MulticastRangeTable.setStatus(_A)
_SwL2MulticastRangeEntry_Object=MibTableRow
swL2MulticastRangeEntry=_SwL2MulticastRangeEntry_Object((1,3,6,1,4,1,171,11,64,1,2,5,1,1))
swL2MulticastRangeEntry.setIndexNames((0,_E,_Ab))
if mibBuilder.loadTexts:swL2MulticastRangeEntry.setStatus(_A)
_SwL2MulticastRangeName_Type=DisplayString
_SwL2MulticastRangeName_Object=MibTableColumn
swL2MulticastRangeName=_SwL2MulticastRangeName_Object((1,3,6,1,4,1,171,11,64,1,2,5,1,1,1),_SwL2MulticastRangeName_Type())
swL2MulticastRangeName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MulticastRangeName.setStatus(_A)
_SwL2MulticastRangeFromIp_Type=IpAddress
_SwL2MulticastRangeFromIp_Object=MibTableColumn
swL2MulticastRangeFromIp=_SwL2MulticastRangeFromIp_Object((1,3,6,1,4,1,171,11,64,1,2,5,1,1,2),_SwL2MulticastRangeFromIp_Type())
swL2MulticastRangeFromIp.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2MulticastRangeFromIp.setStatus(_A)
_SwL2MulticastRangeToIp_Type=IpAddress
_SwL2MulticastRangeToIp_Object=MibTableColumn
swL2MulticastRangeToIp=_SwL2MulticastRangeToIp_Object((1,3,6,1,4,1,171,11,64,1,2,5,1,1,3),_SwL2MulticastRangeToIp_Type())
swL2MulticastRangeToIp.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2MulticastRangeToIp.setStatus(_A)
_SwL2MulticastRangeRowStatus_Type=RowStatus
_SwL2MulticastRangeRowStatus_Object=MibTableColumn
swL2MulticastRangeRowStatus=_SwL2MulticastRangeRowStatus_Object((1,3,6,1,4,1,171,11,64,1,2,5,1,1,4),_SwL2MulticastRangeRowStatus_Type())
swL2MulticastRangeRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2MulticastRangeRowStatus.setStatus(_A)
_SwL2LimitedMulticastPortInfo_ObjectIdentity=ObjectIdentity
swL2LimitedMulticastPortInfo=_SwL2LimitedMulticastPortInfo_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,5,2))
_SwL2LimitedMulticastStatusTable_Object=MibTable
swL2LimitedMulticastStatusTable=_SwL2LimitedMulticastStatusTable_Object((1,3,6,1,4,1,171,11,64,1,2,5,2,1))
if mibBuilder.loadTexts:swL2LimitedMulticastStatusTable.setStatus(_A)
_SwL2LimitedMulticastStatusEntry_Object=MibTableRow
swL2LimitedMulticastStatusEntry=_SwL2LimitedMulticastStatusEntry_Object((1,3,6,1,4,1,171,11,64,1,2,5,2,1,1))
swL2LimitedMulticastStatusEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:swL2LimitedMulticastStatusEntry.setStatus(_A)
class _SwL2LimitedMulticastPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2LimitedMulticastPort_Type.__name__=_B
_SwL2LimitedMulticastPort_Object=MibTableColumn
swL2LimitedMulticastPort=_SwL2LimitedMulticastPort_Object((1,3,6,1,4,1,171,11,64,1,2,5,2,1,1,1),_SwL2LimitedMulticastPort_Type())
swL2LimitedMulticastPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LimitedMulticastPort.setStatus(_A)
class _SwL2LimitedMulticastAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('permit',2),('deny',3)))
_SwL2LimitedMulticastAccess_Type.__name__=_B
_SwL2LimitedMulticastAccess_Object=MibTableColumn
swL2LimitedMulticastAccess=_SwL2LimitedMulticastAccess_Object((1,3,6,1,4,1,171,11,64,1,2,5,2,1,1,2),_SwL2LimitedMulticastAccess_Type())
swL2LimitedMulticastAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LimitedMulticastAccess.setStatus(_A)
class _SwL2LimitedMulticastState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2LimitedMulticastState_Type.__name__=_B
_SwL2LimitedMulticastState_Object=MibTableColumn
swL2LimitedMulticastState=_SwL2LimitedMulticastState_Object((1,3,6,1,4,1,171,11,64,1,2,5,2,1,1,3),_SwL2LimitedMulticastState_Type())
swL2LimitedMulticastState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LimitedMulticastState.setStatus(_A)
_SwL2LimitedMulticastRangeTable_Object=MibTable
swL2LimitedMulticastRangeTable=_SwL2LimitedMulticastRangeTable_Object((1,3,6,1,4,1,171,11,64,1,2,5,2,2))
if mibBuilder.loadTexts:swL2LimitedMulticastRangeTable.setStatus(_A)
_SwL2LimitedMulticastRangeEntry_Object=MibTableRow
swL2LimitedMulticastRangeEntry=_SwL2LimitedMulticastRangeEntry_Object((1,3,6,1,4,1,171,11,64,1,2,5,2,2,1))
swL2LimitedMulticastRangeEntry.setIndexNames((0,_E,_Y),(0,_E,_Ac))
if mibBuilder.loadTexts:swL2LimitedMulticastRangeEntry.setStatus(_A)
class _SwL2LimitedMulticastID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2LimitedMulticastID_Type.__name__=_B
_SwL2LimitedMulticastID_Object=MibTableColumn
swL2LimitedMulticastID=_SwL2LimitedMulticastID_Object((1,3,6,1,4,1,171,11,64,1,2,5,2,2,1,1),_SwL2LimitedMulticastID_Type())
swL2LimitedMulticastID.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LimitedMulticastID.setStatus(_A)
_SwL2LimitedMulticastRangeName_Type=DisplayString
_SwL2LimitedMulticastRangeName_Object=MibTableColumn
swL2LimitedMulticastRangeName=_SwL2LimitedMulticastRangeName_Object((1,3,6,1,4,1,171,11,64,1,2,5,2,2,1,2),_SwL2LimitedMulticastRangeName_Type())
swL2LimitedMulticastRangeName.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2LimitedMulticastRangeName.setStatus(_A)
_SwL2LimitedMulticastFromIp_Type=IpAddress
_SwL2LimitedMulticastFromIp_Object=MibTableColumn
swL2LimitedMulticastFromIp=_SwL2LimitedMulticastFromIp_Object((1,3,6,1,4,1,171,11,64,1,2,5,2,2,1,3),_SwL2LimitedMulticastFromIp_Type())
swL2LimitedMulticastFromIp.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LimitedMulticastFromIp.setStatus(_A)
_SwL2LimitedMulticastToIp_Type=IpAddress
_SwL2LimitedMulticastToIp_Object=MibTableColumn
swL2LimitedMulticastToIp=_SwL2LimitedMulticastToIp_Object((1,3,6,1,4,1,171,11,64,1,2,5,2,2,1,4),_SwL2LimitedMulticastToIp_Type())
swL2LimitedMulticastToIp.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LimitedMulticastToIp.setStatus(_A)
_SwL2LimitedMulticastRowStatus_Type=RowStatus
_SwL2LimitedMulticastRowStatus_Object=MibTableColumn
swL2LimitedMulticastRowStatus=_SwL2LimitedMulticastRowStatus_Object((1,3,6,1,4,1,171,11,64,1,2,5,2,2,1,5),_SwL2LimitedMulticastRowStatus_Type())
swL2LimitedMulticastRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2LimitedMulticastRowStatus.setStatus(_A)
_SwL2QOSMgmt_ObjectIdentity=ObjectIdentity
swL2QOSMgmt=_SwL2QOSMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,6))
_SwL2QOSBandwidthControlTable_Object=MibTable
swL2QOSBandwidthControlTable=_SwL2QOSBandwidthControlTable_Object((1,3,6,1,4,1,171,11,64,1,2,6,1))
if mibBuilder.loadTexts:swL2QOSBandwidthControlTable.setStatus(_A)
_SwL2QOSBandwidthControlEntry_Object=MibTableRow
swL2QOSBandwidthControlEntry=_SwL2QOSBandwidthControlEntry_Object((1,3,6,1,4,1,171,11,64,1,2,6,1,1))
swL2QOSBandwidthControlEntry.setIndexNames((0,_E,_Ad))
if mibBuilder.loadTexts:swL2QOSBandwidthControlEntry.setStatus(_A)
class _SwL2QOSBandwidthPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,650))
_SwL2QOSBandwidthPortIndex_Type.__name__=_B
_SwL2QOSBandwidthPortIndex_Object=MibTableColumn
swL2QOSBandwidthPortIndex=_SwL2QOSBandwidthPortIndex_Object((1,3,6,1,4,1,171,11,64,1,2,6,1,1,1),_SwL2QOSBandwidthPortIndex_Type())
swL2QOSBandwidthPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthPortIndex.setStatus(_A)
class _SwL2QOSBandwidthRxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_SwL2QOSBandwidthRxRate_Type.__name__=_B
_SwL2QOSBandwidthRxRate_Object=MibTableColumn
swL2QOSBandwidthRxRate=_SwL2QOSBandwidthRxRate_Object((1,3,6,1,4,1,171,11,64,1,2,6,1,1,2),_SwL2QOSBandwidthRxRate_Type())
swL2QOSBandwidthRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSBandwidthRxRate.setStatus(_A)
class _SwL2QOSBandwidthTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_SwL2QOSBandwidthTxRate_Type.__name__=_B
_SwL2QOSBandwidthTxRate_Object=MibTableColumn
swL2QOSBandwidthTxRate=_SwL2QOSBandwidthTxRate_Object((1,3,6,1,4,1,171,11,64,1,2,6,1,1,3),_SwL2QOSBandwidthTxRate_Type())
swL2QOSBandwidthTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSBandwidthTxRate.setStatus(_A)
_SwL2QOSBandwidthRadiusRxRate_Type=Integer32
_SwL2QOSBandwidthRadiusRxRate_Object=MibTableColumn
swL2QOSBandwidthRadiusRxRate=_SwL2QOSBandwidthRadiusRxRate_Object((1,3,6,1,4,1,171,11,64,1,2,6,1,1,4),_SwL2QOSBandwidthRadiusRxRate_Type())
swL2QOSBandwidthRadiusRxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthRadiusRxRate.setStatus(_A)
_SwL2QOSBandwidthRadiusTxRate_Type=Integer32
_SwL2QOSBandwidthRadiusTxRate_Object=MibTableColumn
swL2QOSBandwidthRadiusTxRate=_SwL2QOSBandwidthRadiusTxRate_Object((1,3,6,1,4,1,171,11,64,1,2,6,1,1,5),_SwL2QOSBandwidthRadiusTxRate_Type())
swL2QOSBandwidthRadiusTxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthRadiusTxRate.setStatus(_A)
_SwL2QOSSchedulingTable_Object=MibTable
swL2QOSSchedulingTable=_SwL2QOSSchedulingTable_Object((1,3,6,1,4,1,171,11,64,1,2,6,2))
if mibBuilder.loadTexts:swL2QOSSchedulingTable.setStatus(_A)
_SwL2QOSSchedulingEntry_Object=MibTableRow
swL2QOSSchedulingEntry=_SwL2QOSSchedulingEntry_Object((1,3,6,1,4,1,171,11,64,1,2,6,2,1))
swL2QOSSchedulingEntry.setIndexNames((0,_E,_Ae))
if mibBuilder.loadTexts:swL2QOSSchedulingEntry.setStatus(_A)
class _SwL2QOSSchedulingClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwL2QOSSchedulingClassIndex_Type.__name__=_B
_SwL2QOSSchedulingClassIndex_Object=MibTableColumn
swL2QOSSchedulingClassIndex=_SwL2QOSSchedulingClassIndex_Object((1,3,6,1,4,1,171,11,64,1,2,6,2,1,1),_SwL2QOSSchedulingClassIndex_Type())
swL2QOSSchedulingClassIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSSchedulingClassIndex.setStatus(_A)
class _SwL2QOSSchedulingMaxPkts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL2QOSSchedulingMaxPkts_Type.__name__=_B
_SwL2QOSSchedulingMaxPkts_Object=MibTableColumn
swL2QOSSchedulingMaxPkts=_SwL2QOSSchedulingMaxPkts_Object((1,3,6,1,4,1,171,11,64,1,2,6,2,1,2),_SwL2QOSSchedulingMaxPkts_Type())
swL2QOSSchedulingMaxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSSchedulingMaxPkts.setStatus(_A)
class _SwL2QOSSchedulingMaxLatency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL2QOSSchedulingMaxLatency_Type.__name__=_B
_SwL2QOSSchedulingMaxLatency_Object=MibTableColumn
swL2QOSSchedulingMaxLatency=_SwL2QOSSchedulingMaxLatency_Object((1,3,6,1,4,1,171,11,64,1,2,6,2,1,3),_SwL2QOSSchedulingMaxLatency_Type())
swL2QOSSchedulingMaxLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSSchedulingMaxLatency.setStatus(_A)
_SwL2QOS8021pUserPriorityTable_Object=MibTable
swL2QOS8021pUserPriorityTable=_SwL2QOS8021pUserPriorityTable_Object((1,3,6,1,4,1,171,11,64,1,2,6,3))
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityTable.setStatus(_A)
_SwL2QOS8021pUserPriorityEntry_Object=MibTableRow
swL2QOS8021pUserPriorityEntry=_SwL2QOS8021pUserPriorityEntry_Object((1,3,6,1,4,1,171,11,64,1,2,6,3,1))
swL2QOS8021pUserPriorityEntry.setIndexNames((0,_E,_Af))
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityEntry.setStatus(_A)
class _SwL2QOS8021pUserPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOS8021pUserPriorityIndex_Type.__name__=_B
_SwL2QOS8021pUserPriorityIndex_Object=MibTableColumn
swL2QOS8021pUserPriorityIndex=_SwL2QOS8021pUserPriorityIndex_Object((1,3,6,1,4,1,171,11,64,1,2,6,3,1,1),_SwL2QOS8021pUserPriorityIndex_Type())
swL2QOS8021pUserPriorityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityIndex.setStatus(_A)
class _SwL2QOS8021pUserPriorityClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwL2QOS8021pUserPriorityClass_Type.__name__=_B
_SwL2QOS8021pUserPriorityClass_Object=MibTableColumn
swL2QOS8021pUserPriorityClass=_SwL2QOS8021pUserPriorityClass_Object((1,3,6,1,4,1,171,11,64,1,2,6,3,1,2),_SwL2QOS8021pUserPriorityClass_Type())
swL2QOS8021pUserPriorityClass.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityClass.setStatus(_A)
_SwL2QOS8021pDefaultPriorityTable_Object=MibTable
swL2QOS8021pDefaultPriorityTable=_SwL2QOS8021pDefaultPriorityTable_Object((1,3,6,1,4,1,171,11,64,1,2,6,4))
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityTable.setStatus(_A)
_SwL2QOS8021pDefaultPriorityEntry_Object=MibTableRow
swL2QOS8021pDefaultPriorityEntry=_SwL2QOS8021pDefaultPriorityEntry_Object((1,3,6,1,4,1,171,11,64,1,2,6,4,1))
swL2QOS8021pDefaultPriorityEntry.setIndexNames((0,_E,_Ag))
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityEntry.setStatus(_A)
class _SwL2QOS8021pDefaultPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,650))
_SwL2QOS8021pDefaultPriorityIndex_Type.__name__=_B
_SwL2QOS8021pDefaultPriorityIndex_Object=MibTableColumn
swL2QOS8021pDefaultPriorityIndex=_SwL2QOS8021pDefaultPriorityIndex_Object((1,3,6,1,4,1,171,11,64,1,2,6,4,1,1),_SwL2QOS8021pDefaultPriorityIndex_Type())
swL2QOS8021pDefaultPriorityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityIndex.setStatus(_A)
class _SwL2QOS8021pDefaultPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOS8021pDefaultPriority_Type.__name__=_B
_SwL2QOS8021pDefaultPriority_Object=MibTableColumn
swL2QOS8021pDefaultPriority=_SwL2QOS8021pDefaultPriority_Object((1,3,6,1,4,1,171,11,64,1,2,6,4,1,2),_SwL2QOS8021pDefaultPriority_Type())
swL2QOS8021pDefaultPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriority.setStatus(_A)
_SwL2QOS8021pRadiusPriority_Type=Integer32
_SwL2QOS8021pRadiusPriority_Object=MibTableColumn
swL2QOS8021pRadiusPriority=_SwL2QOS8021pRadiusPriority_Object((1,3,6,1,4,1,171,11,64,1,2,6,4,1,3),_SwL2QOS8021pRadiusPriority_Type())
swL2QOS8021pRadiusPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pRadiusPriority.setStatus(_A)
_SwL2IpMacBindingMgmt_ObjectIdentity=ObjectIdentity
swL2IpMacBindingMgmt=_SwL2IpMacBindingMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,7))
_SwL2IpMacBindingPortTable_Object=MibTable
swL2IpMacBindingPortTable=_SwL2IpMacBindingPortTable_Object((1,3,6,1,4,1,171,11,64,1,2,7,1))
if mibBuilder.loadTexts:swL2IpMacBindingPortTable.setStatus(_A)
_SwL2IpMacBindingPortEntry_Object=MibTableRow
swL2IpMacBindingPortEntry=_SwL2IpMacBindingPortEntry_Object((1,3,6,1,4,1,171,11,64,1,2,7,1,1))
swL2IpMacBindingPortEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:swL2IpMacBindingPortEntry.setStatus(_A)
class _SwL2IpMacBindingPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IpMacBindingPortIndex_Type.__name__=_B
_SwL2IpMacBindingPortIndex_Object=MibTableColumn
swL2IpMacBindingPortIndex=_SwL2IpMacBindingPortIndex_Object((1,3,6,1,4,1,171,11,64,1,2,7,1,1,1),_SwL2IpMacBindingPortIndex_Type())
swL2IpMacBindingPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpMacBindingPortIndex.setStatus(_A)
class _SwL2IpMacBindingPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_Ah,2),(_K,3),(_Ai,4)))
_SwL2IpMacBindingPortState_Type.__name__=_B
_SwL2IpMacBindingPortState_Object=MibTableColumn
swL2IpMacBindingPortState=_SwL2IpMacBindingPortState_Object((1,3,6,1,4,1,171,11,64,1,2,7,1,1,2),_SwL2IpMacBindingPortState_Type())
swL2IpMacBindingPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IpMacBindingPortState.setStatus(_A)
class _SwL2IpMacBindingPortAllowZeroIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_M,2),(_K,3)))
_SwL2IpMacBindingPortAllowZeroIp_Type.__name__=_B
_SwL2IpMacBindingPortAllowZeroIp_Object=MibTableColumn
swL2IpMacBindingPortAllowZeroIp=_SwL2IpMacBindingPortAllowZeroIp_Object((1,3,6,1,4,1,171,11,64,1,2,7,1,1,3),_SwL2IpMacBindingPortAllowZeroIp_Type())
swL2IpMacBindingPortAllowZeroIp.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IpMacBindingPortAllowZeroIp.setStatus(_A)
class _SwL2IpMacBindingPortForwardDhcpPkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2IpMacBindingPortForwardDhcpPkt_Type.__name__=_B
_SwL2IpMacBindingPortForwardDhcpPkt_Object=MibTableColumn
swL2IpMacBindingPortForwardDhcpPkt=_SwL2IpMacBindingPortForwardDhcpPkt_Object((1,3,6,1,4,1,171,11,64,1,2,7,1,1,4),_SwL2IpMacBindingPortForwardDhcpPkt_Type())
swL2IpMacBindingPortForwardDhcpPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IpMacBindingPortForwardDhcpPkt.setStatus(_A)
class _SwL2IpMacBindingPortDHCPSnoopMaxEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_SwL2IpMacBindingPortDHCPSnoopMaxEntry_Type.__name__=_B
_SwL2IpMacBindingPortDHCPSnoopMaxEntry_Object=MibTableColumn
swL2IpMacBindingPortDHCPSnoopMaxEntry=_SwL2IpMacBindingPortDHCPSnoopMaxEntry_Object((1,3,6,1,4,1,171,11,64,1,2,7,1,1,5),_SwL2IpMacBindingPortDHCPSnoopMaxEntry_Type())
swL2IpMacBindingPortDHCPSnoopMaxEntry.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IpMacBindingPortDHCPSnoopMaxEntry.setStatus(_A)
class _SwL2IpMacBindingPortDHCPSnoopEntryClearAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('start',2)))
_SwL2IpMacBindingPortDHCPSnoopEntryClearAction_Type.__name__=_B
_SwL2IpMacBindingPortDHCPSnoopEntryClearAction_Object=MibTableColumn
swL2IpMacBindingPortDHCPSnoopEntryClearAction=_SwL2IpMacBindingPortDHCPSnoopEntryClearAction_Object((1,3,6,1,4,1,171,11,64,1,2,7,1,1,6),_SwL2IpMacBindingPortDHCPSnoopEntryClearAction_Type())
swL2IpMacBindingPortDHCPSnoopEntryClearAction.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IpMacBindingPortDHCPSnoopEntryClearAction.setStatus(_A)
_SwL2IpMacBindingTable_Object=MibTable
swL2IpMacBindingTable=_SwL2IpMacBindingTable_Object((1,3,6,1,4,1,171,11,64,1,2,7,2))
if mibBuilder.loadTexts:swL2IpMacBindingTable.setStatus(_A)
_SwL2IpMacBindingEntry_Object=MibTableRow
swL2IpMacBindingEntry=_SwL2IpMacBindingEntry_Object((1,3,6,1,4,1,171,11,64,1,2,7,2,1))
swL2IpMacBindingEntry.setIndexNames((0,_E,_Aj))
if mibBuilder.loadTexts:swL2IpMacBindingEntry.setStatus(_A)
_SwL2IpMacBindingIpIndex_Type=IpAddress
_SwL2IpMacBindingIpIndex_Object=MibTableColumn
swL2IpMacBindingIpIndex=_SwL2IpMacBindingIpIndex_Object((1,3,6,1,4,1,171,11,64,1,2,7,2,1,1),_SwL2IpMacBindingIpIndex_Type())
swL2IpMacBindingIpIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpMacBindingIpIndex.setStatus(_A)
_SwL2IpMacBindingMac_Type=MacAddress
_SwL2IpMacBindingMac_Object=MibTableColumn
swL2IpMacBindingMac=_SwL2IpMacBindingMac_Object((1,3,6,1,4,1,171,11,64,1,2,7,2,1,2),_SwL2IpMacBindingMac_Type())
swL2IpMacBindingMac.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IpMacBindingMac.setStatus(_A)
_SwL2IpMacBindingStatus_Type=RowStatus
_SwL2IpMacBindingStatus_Object=MibTableColumn
swL2IpMacBindingStatus=_SwL2IpMacBindingStatus_Object((1,3,6,1,4,1,171,11,64,1,2,7,2,1,3),_SwL2IpMacBindingStatus_Type())
swL2IpMacBindingStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IpMacBindingStatus.setStatus(_A)
_SwL2IpMacBindingPorts_Type=PortList
_SwL2IpMacBindingPorts_Object=MibTableColumn
swL2IpMacBindingPorts=_SwL2IpMacBindingPorts_Object((1,3,6,1,4,1,171,11,64,1,2,7,2,1,4),_SwL2IpMacBindingPorts_Type())
swL2IpMacBindingPorts.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IpMacBindingPorts.setStatus(_A)
class _SwL2IpMacBindingAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inactive',0),(_W,1)))
_SwL2IpMacBindingAction_Type.__name__=_B
_SwL2IpMacBindingAction_Object=MibTableColumn
swL2IpMacBindingAction=_SwL2IpMacBindingAction_Object((1,3,6,1,4,1,171,11,64,1,2,7,2,1,5),_SwL2IpMacBindingAction_Type())
swL2IpMacBindingAction.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpMacBindingAction.setStatus(_A)
class _SwL2IpMacBindingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('arp',0),('acl',1),(_S,2)))
_SwL2IpMacBindingMode_Type.__name__=_B
_SwL2IpMacBindingMode_Object=MibTableColumn
swL2IpMacBindingMode=_SwL2IpMacBindingMode_Object((1,3,6,1,4,1,171,11,64,1,2,7,2,1,6),_SwL2IpMacBindingMode_Type())
swL2IpMacBindingMode.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IpMacBindingMode.setStatus(_A)
_SwL2IpMacBindingBlockedTable_Object=MibTable
swL2IpMacBindingBlockedTable=_SwL2IpMacBindingBlockedTable_Object((1,3,6,1,4,1,171,11,64,1,2,7,3))
if mibBuilder.loadTexts:swL2IpMacBindingBlockedTable.setStatus(_A)
_SwL2IpMacBindingBlockedEntry_Object=MibTableRow
swL2IpMacBindingBlockedEntry=_SwL2IpMacBindingBlockedEntry_Object((1,3,6,1,4,1,171,11,64,1,2,7,3,1))
swL2IpMacBindingBlockedEntry.setIndexNames((0,_E,_Ak),(0,_E,_Al))
if mibBuilder.loadTexts:swL2IpMacBindingBlockedEntry.setStatus(_A)
_SwL2IpMacBindingBlockedVID_Type=VlanIndex
_SwL2IpMacBindingBlockedVID_Object=MibTableColumn
swL2IpMacBindingBlockedVID=_SwL2IpMacBindingBlockedVID_Object((1,3,6,1,4,1,171,11,64,1,2,7,3,1,1),_SwL2IpMacBindingBlockedVID_Type())
swL2IpMacBindingBlockedVID.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpMacBindingBlockedVID.setStatus(_A)
_SwL2IpMacBindingBlockedMac_Type=MacAddress
_SwL2IpMacBindingBlockedMac_Object=MibTableColumn
swL2IpMacBindingBlockedMac=_SwL2IpMacBindingBlockedMac_Object((1,3,6,1,4,1,171,11,64,1,2,7,3,1,2),_SwL2IpMacBindingBlockedMac_Type())
swL2IpMacBindingBlockedMac.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpMacBindingBlockedMac.setStatus(_A)
_SwL2IpMacBindingBlockedVlanName_Type=DisplayString
_SwL2IpMacBindingBlockedVlanName_Object=MibTableColumn
swL2IpMacBindingBlockedVlanName=_SwL2IpMacBindingBlockedVlanName_Object((1,3,6,1,4,1,171,11,64,1,2,7,3,1,3),_SwL2IpMacBindingBlockedVlanName_Type())
swL2IpMacBindingBlockedVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpMacBindingBlockedVlanName.setStatus(_A)
class _SwL2IpMacBindingBlockedPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IpMacBindingBlockedPort_Type.__name__=_B
_SwL2IpMacBindingBlockedPort_Object=MibTableColumn
swL2IpMacBindingBlockedPort=_SwL2IpMacBindingBlockedPort_Object((1,3,6,1,4,1,171,11,64,1,2,7,3,1,4),_SwL2IpMacBindingBlockedPort_Type())
swL2IpMacBindingBlockedPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpMacBindingBlockedPort.setStatus(_A)
class _SwL2IpMacBindingBlockedType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('blockByAddrBind',2),('delete',3)))
_SwL2IpMacBindingBlockedType_Type.__name__=_B
_SwL2IpMacBindingBlockedType_Object=MibTableColumn
swL2IpMacBindingBlockedType=_SwL2IpMacBindingBlockedType_Object((1,3,6,1,4,1,171,11,64,1,2,7,3,1,5),_SwL2IpMacBindingBlockedType_Type())
swL2IpMacBindingBlockedType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IpMacBindingBlockedType.setStatus(_A)
class _SwL2IpMacBindingAllPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_Ah,2),(_K,3),(_Ai,4)))
_SwL2IpMacBindingAllPortState_Type.__name__=_B
_SwL2IpMacBindingAllPortState_Object=MibScalar
swL2IpMacBindingAllPortState=_SwL2IpMacBindingAllPortState_Object((1,3,6,1,4,1,171,11,64,1,2,7,4),_SwL2IpMacBindingAllPortState_Type())
swL2IpMacBindingAllPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IpMacBindingAllPortState.setStatus(_A)
class _SwL2IpMacBindingTrapLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_M,2),(_K,3)))
_SwL2IpMacBindingTrapLogState_Type.__name__=_B
_SwL2IpMacBindingTrapLogState_Object=MibScalar
swL2IpMacBindingTrapLogState=_SwL2IpMacBindingTrapLogState_Object((1,3,6,1,4,1,171,11,64,1,2,7,5),_SwL2IpMacBindingTrapLogState_Type())
swL2IpMacBindingTrapLogState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IpMacBindingTrapLogState.setStatus(_A)
class _SwL2IpMacBindingACLMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_M,2),(_K,3)))
_SwL2IpMacBindingACLMode_Type.__name__=_B
_SwL2IpMacBindingACLMode_Object=MibScalar
swL2IpMacBindingACLMode=_SwL2IpMacBindingACLMode_Object((1,3,6,1,4,1,171,11,64,1,2,7,6),_SwL2IpMacBindingACLMode_Type())
swL2IpMacBindingACLMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IpMacBindingACLMode.setStatus(_A)
class _SwL2IpMacBindingDHCPSnoopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2IpMacBindingDHCPSnoopState_Type.__name__=_B
_SwL2IpMacBindingDHCPSnoopState_Object=MibScalar
swL2IpMacBindingDHCPSnoopState=_SwL2IpMacBindingDHCPSnoopState_Object((1,3,6,1,4,1,171,11,64,1,2,7,7),_SwL2IpMacBindingDHCPSnoopState_Type())
swL2IpMacBindingDHCPSnoopState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IpMacBindingDHCPSnoopState.setStatus(_A)
class _SwL2IpMacBindingDHCPSnoopEntryClearAllState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('start',2)))
_SwL2IpMacBindingDHCPSnoopEntryClearAllState_Type.__name__=_B
_SwL2IpMacBindingDHCPSnoopEntryClearAllState_Object=MibScalar
swL2IpMacBindingDHCPSnoopEntryClearAllState=_SwL2IpMacBindingDHCPSnoopEntryClearAllState_Object((1,3,6,1,4,1,171,11,64,1,2,7,8),_SwL2IpMacBindingDHCPSnoopEntryClearAllState_Type())
swL2IpMacBindingDHCPSnoopEntryClearAllState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IpMacBindingDHCPSnoopEntryClearAllState.setStatus(_A)
_SwL2IpMacBindingDHCPSnoopTable_Object=MibTable
swL2IpMacBindingDHCPSnoopTable=_SwL2IpMacBindingDHCPSnoopTable_Object((1,3,6,1,4,1,171,11,64,1,2,7,9))
if mibBuilder.loadTexts:swL2IpMacBindingDHCPSnoopTable.setStatus(_A)
_SwL2IpMacBindingDHCPSnoopEntry_Object=MibTableRow
swL2IpMacBindingDHCPSnoopEntry=_SwL2IpMacBindingDHCPSnoopEntry_Object((1,3,6,1,4,1,171,11,64,1,2,7,9,1))
swL2IpMacBindingDHCPSnoopEntry.setIndexNames((0,_E,_Am))
if mibBuilder.loadTexts:swL2IpMacBindingDHCPSnoopEntry.setStatus(_A)
_SwL2IpMacBindingDHCPSnoopIpIndex_Type=IpAddress
_SwL2IpMacBindingDHCPSnoopIpIndex_Object=MibTableColumn
swL2IpMacBindingDHCPSnoopIpIndex=_SwL2IpMacBindingDHCPSnoopIpIndex_Object((1,3,6,1,4,1,171,11,64,1,2,7,9,1,1),_SwL2IpMacBindingDHCPSnoopIpIndex_Type())
swL2IpMacBindingDHCPSnoopIpIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpMacBindingDHCPSnoopIpIndex.setStatus(_A)
_SwL2IpMacBindingDHCPSnoopMac_Type=MacAddress
_SwL2IpMacBindingDHCPSnoopMac_Object=MibTableColumn
swL2IpMacBindingDHCPSnoopMac=_SwL2IpMacBindingDHCPSnoopMac_Object((1,3,6,1,4,1,171,11,64,1,2,7,9,1,2),_SwL2IpMacBindingDHCPSnoopMac_Type())
swL2IpMacBindingDHCPSnoopMac.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpMacBindingDHCPSnoopMac.setStatus(_A)
_SwL2IpMacBindingDHCPSnoopLeaseTime_Type=Integer32
_SwL2IpMacBindingDHCPSnoopLeaseTime_Object=MibTableColumn
swL2IpMacBindingDHCPSnoopLeaseTime=_SwL2IpMacBindingDHCPSnoopLeaseTime_Object((1,3,6,1,4,1,171,11,64,1,2,7,9,1,3),_SwL2IpMacBindingDHCPSnoopLeaseTime_Type())
swL2IpMacBindingDHCPSnoopLeaseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpMacBindingDHCPSnoopLeaseTime.setStatus(_A)
_SwL2IpMacBindingDHCPSnoopPort_Type=Integer32
_SwL2IpMacBindingDHCPSnoopPort_Object=MibTableColumn
swL2IpMacBindingDHCPSnoopPort=_SwL2IpMacBindingDHCPSnoopPort_Object((1,3,6,1,4,1,171,11,64,1,2,7,9,1,4),_SwL2IpMacBindingDHCPSnoopPort_Type())
swL2IpMacBindingDHCPSnoopPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpMacBindingDHCPSnoopPort.setStatus(_A)
class _SwL2IpMacBindingDHCPSnoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),(_W,2)))
_SwL2IpMacBindingDHCPSnoopStatus_Type.__name__=_B
_SwL2IpMacBindingDHCPSnoopStatus_Object=MibTableColumn
swL2IpMacBindingDHCPSnoopStatus=_SwL2IpMacBindingDHCPSnoopStatus_Object((1,3,6,1,4,1,171,11,64,1,2,7,9,1,5),_SwL2IpMacBindingDHCPSnoopStatus_Type())
swL2IpMacBindingDHCPSnoopStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpMacBindingDHCPSnoopStatus.setStatus(_A)
_SwL2IpMacBindingPermitIPPoolTable_Object=MibTable
swL2IpMacBindingPermitIPPoolTable=_SwL2IpMacBindingPermitIPPoolTable_Object((1,3,6,1,4,1,171,11,64,1,2,7,10))
if mibBuilder.loadTexts:swL2IpMacBindingPermitIPPoolTable.setStatus(_A)
_SwL2IpMacBindingPermitIPPoolEntry_Object=MibTableRow
swL2IpMacBindingPermitIPPoolEntry=_SwL2IpMacBindingPermitIPPoolEntry_Object((1,3,6,1,4,1,171,11,64,1,2,7,10,1))
swL2IpMacBindingPermitIPPoolEntry.setIndexNames((0,_E,_An),(0,_E,_Ao))
if mibBuilder.loadTexts:swL2IpMacBindingPermitIPPoolEntry.setStatus(_A)
_SwL2IpMacBindingPermitIPPoolStartIP_Type=IpAddress
_SwL2IpMacBindingPermitIPPoolStartIP_Object=MibTableColumn
swL2IpMacBindingPermitIPPoolStartIP=_SwL2IpMacBindingPermitIPPoolStartIP_Object((1,3,6,1,4,1,171,11,64,1,2,7,10,1,1),_SwL2IpMacBindingPermitIPPoolStartIP_Type())
swL2IpMacBindingPermitIPPoolStartIP.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpMacBindingPermitIPPoolStartIP.setStatus(_A)
_SwL2IpMacBindingPermitIPPoolEndIP_Type=IpAddress
_SwL2IpMacBindingPermitIPPoolEndIP_Object=MibTableColumn
swL2IpMacBindingPermitIPPoolEndIP=_SwL2IpMacBindingPermitIPPoolEndIP_Object((1,3,6,1,4,1,171,11,64,1,2,7,10,1,2),_SwL2IpMacBindingPermitIPPoolEndIP_Type())
swL2IpMacBindingPermitIPPoolEndIP.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpMacBindingPermitIPPoolEndIP.setStatus(_A)
_SwL2IpMacBindingPermitIPPoolPorts_Type=PortList
_SwL2IpMacBindingPermitIPPoolPorts_Object=MibTableColumn
swL2IpMacBindingPermitIPPoolPorts=_SwL2IpMacBindingPermitIPPoolPorts_Object((1,3,6,1,4,1,171,11,64,1,2,7,10,1,3),_SwL2IpMacBindingPermitIPPoolPorts_Type())
swL2IpMacBindingPermitIPPoolPorts.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IpMacBindingPermitIPPoolPorts.setStatus(_A)
_SwL2IpMacBindingPermitIPPoolStatus_Type=RowStatus
_SwL2IpMacBindingPermitIPPoolStatus_Object=MibTableColumn
swL2IpMacBindingPermitIPPoolStatus=_SwL2IpMacBindingPermitIPPoolStatus_Object((1,3,6,1,4,1,171,11,64,1,2,7,10,1,4),_SwL2IpMacBindingPermitIPPoolStatus_Type())
swL2IpMacBindingPermitIPPoolStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IpMacBindingPermitIPPoolStatus.setStatus(_A)
_SwL2TrunkMgmt_ObjectIdentity=ObjectIdentity
swL2TrunkMgmt=_SwL2TrunkMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,8))
class _SwL2TrunkMaxSupportedEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkMaxSupportedEntries_Type.__name__=_B
_SwL2TrunkMaxSupportedEntries_Object=MibScalar
swL2TrunkMaxSupportedEntries=_SwL2TrunkMaxSupportedEntries_Object((1,3,6,1,4,1,171,11,64,1,2,8,1),_SwL2TrunkMaxSupportedEntries_Type())
swL2TrunkMaxSupportedEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkMaxSupportedEntries.setStatus(_A)
class _SwL2TrunkCurrentNumEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkCurrentNumEntries_Type.__name__=_B
_SwL2TrunkCurrentNumEntries_Object=MibScalar
swL2TrunkCurrentNumEntries=_SwL2TrunkCurrentNumEntries_Object((1,3,6,1,4,1,171,11,64,1,2,8,2),_SwL2TrunkCurrentNumEntries_Type())
swL2TrunkCurrentNumEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkCurrentNumEntries.setStatus(_A)
_SwL2TrunkCtrlTable_Object=MibTable
swL2TrunkCtrlTable=_SwL2TrunkCtrlTable_Object((1,3,6,1,4,1,171,11,64,1,2,8,3))
if mibBuilder.loadTexts:swL2TrunkCtrlTable.setStatus(_A)
_SwL2TrunkCtrlEntry_Object=MibTableRow
swL2TrunkCtrlEntry=_SwL2TrunkCtrlEntry_Object((1,3,6,1,4,1,171,11,64,1,2,8,3,1))
swL2TrunkCtrlEntry.setIndexNames((0,_E,_Ap))
if mibBuilder.loadTexts:swL2TrunkCtrlEntry.setStatus(_A)
class _SwL2TrunkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkIndex_Type.__name__=_B
_SwL2TrunkIndex_Object=MibTableColumn
swL2TrunkIndex=_SwL2TrunkIndex_Object((1,3,6,1,4,1,171,11,64,1,2,8,3,1,1),_SwL2TrunkIndex_Type())
swL2TrunkIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkIndex.setStatus(_A)
class _SwL2TrunkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwL2TrunkName_Type.__name__=_Q
_SwL2TrunkName_Object=MibTableColumn
swL2TrunkName=_SwL2TrunkName_Object((1,3,6,1,4,1,171,11,64,1,2,8,3,1,2),_SwL2TrunkName_Type())
swL2TrunkName.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2TrunkName.setStatus(_A)
class _SwL2TrunkMasterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2TrunkMasterPort_Type.__name__=_B
_SwL2TrunkMasterPort_Object=MibTableColumn
swL2TrunkMasterPort=_SwL2TrunkMasterPort_Object((1,3,6,1,4,1,171,11,64,1,2,8,3,1,3),_SwL2TrunkMasterPort_Type())
swL2TrunkMasterPort.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2TrunkMasterPort.setStatus(_A)
_SwL2TrunkMember_Type=PortList
_SwL2TrunkMember_Object=MibTableColumn
swL2TrunkMember=_SwL2TrunkMember_Object((1,3,6,1,4,1,171,11,64,1,2,8,3,1,4),_SwL2TrunkMember_Type())
swL2TrunkMember.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2TrunkMember.setStatus(_A)
class _SwL2TrunkFloodingPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2TrunkFloodingPort_Type.__name__=_B
_SwL2TrunkFloodingPort_Object=MibTableColumn
swL2TrunkFloodingPort=_SwL2TrunkFloodingPort_Object((1,3,6,1,4,1,171,11,64,1,2,8,3,1,5),_SwL2TrunkFloodingPort_Type())
swL2TrunkFloodingPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkFloodingPort.setStatus(_A)
class _SwL2TrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('static',2),('lacp',3)))
_SwL2TrunkType_Type.__name__=_B
_SwL2TrunkType_Object=MibTableColumn
swL2TrunkType=_SwL2TrunkType_Object((1,3,6,1,4,1,171,11,64,1,2,8,3,1,6),_SwL2TrunkType_Type())
swL2TrunkType.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2TrunkType.setStatus(_A)
_SwL2TrunkState_Type=RowStatus
_SwL2TrunkState_Object=MibTableColumn
swL2TrunkState=_SwL2TrunkState_Object((1,3,6,1,4,1,171,11,64,1,2,8,3,1,7),_SwL2TrunkState_Type())
swL2TrunkState.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2TrunkState.setStatus(_A)
class _SwL2TrunkAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),('mac-source',2),('mac-destination',3),('mac-source-dest',4),('ip-source',5),('ip-destination',6),('ip-source-dest',7)))
_SwL2TrunkAlgorithm_Type.__name__=_B
_SwL2TrunkAlgorithm_Object=MibScalar
swL2TrunkAlgorithm=_SwL2TrunkAlgorithm_Object((1,3,6,1,4,1,171,11,64,1,2,8,4),_SwL2TrunkAlgorithm_Type())
swL2TrunkAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkAlgorithm.setStatus(_A)
_SwL2MirrorMgmt_ObjectIdentity=ObjectIdentity
swL2MirrorMgmt=_SwL2MirrorMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,9))
class _SwL2MirrorLogicTargetPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2MirrorLogicTargetPort_Type.__name__=_B
_SwL2MirrorLogicTargetPort_Object=MibScalar
swL2MirrorLogicTargetPort=_SwL2MirrorLogicTargetPort_Object((1,3,6,1,4,1,171,11,64,1,2,9,1),_SwL2MirrorLogicTargetPort_Type())
swL2MirrorLogicTargetPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MirrorLogicTargetPort.setStatus(_A)
_SwL2MirrorPortSourceIngress_Type=PortList
_SwL2MirrorPortSourceIngress_Object=MibScalar
swL2MirrorPortSourceIngress=_SwL2MirrorPortSourceIngress_Object((1,3,6,1,4,1,171,11,64,1,2,9,2),_SwL2MirrorPortSourceIngress_Type())
swL2MirrorPortSourceIngress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MirrorPortSourceIngress.setStatus(_A)
_SwL2MirrorPortSourceEgress_Type=PortList
_SwL2MirrorPortSourceEgress_Object=MibScalar
swL2MirrorPortSourceEgress=_SwL2MirrorPortSourceEgress_Object((1,3,6,1,4,1,171,11,64,1,2,9,3),_SwL2MirrorPortSourceEgress_Type())
swL2MirrorPortSourceEgress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MirrorPortSourceEgress.setStatus(_A)
class _SwL2MirrorPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2MirrorPortState_Type.__name__=_B
_SwL2MirrorPortState_Object=MibScalar
swL2MirrorPortState=_SwL2MirrorPortState_Object((1,3,6,1,4,1,171,11,64,1,2,9,4),_SwL2MirrorPortState_Type())
swL2MirrorPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MirrorPortState.setStatus(_A)
_SwL2IGMPMgmt_ObjectIdentity=ObjectIdentity
swL2IGMPMgmt=_SwL2IGMPMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,10))
class _SwL2IGMPMaxSupportedVlans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPMaxSupportedVlans_Type.__name__=_B
_SwL2IGMPMaxSupportedVlans_Object=MibScalar
swL2IGMPMaxSupportedVlans=_SwL2IGMPMaxSupportedVlans_Object((1,3,6,1,4,1,171,11,64,1,2,10,1),_SwL2IGMPMaxSupportedVlans_Type())
swL2IGMPMaxSupportedVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMaxSupportedVlans.setStatus(_A)
_SwL2IGMPCtrlTable_Object=MibTable
swL2IGMPCtrlTable=_SwL2IGMPCtrlTable_Object((1,3,6,1,4,1,171,11,64,1,2,10,3))
if mibBuilder.loadTexts:swL2IGMPCtrlTable.setStatus(_A)
_SwL2IGMPCtrlEntry_Object=MibTableRow
swL2IGMPCtrlEntry=_SwL2IGMPCtrlEntry_Object((1,3,6,1,4,1,171,11,64,1,2,10,3,1))
swL2IGMPCtrlEntry.setIndexNames((0,_E,_Aq))
if mibBuilder.loadTexts:swL2IGMPCtrlEntry.setStatus(_A)
class _SwL2IGMPCtrlVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPCtrlVid_Type.__name__=_B
_SwL2IGMPCtrlVid_Object=MibTableColumn
swL2IGMPCtrlVid=_SwL2IGMPCtrlVid_Object((1,3,6,1,4,1,171,11,64,1,2,10,3,1,1),_SwL2IGMPCtrlVid_Type())
swL2IGMPCtrlVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPCtrlVid.setStatus(_A)
class _SwL2IGMPQueryInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2IGMPQueryInterval_Type.__name__=_B
_SwL2IGMPQueryInterval_Object=MibTableColumn
swL2IGMPQueryInterval=_SwL2IGMPQueryInterval_Object((1,3,6,1,4,1,171,11,64,1,2,10,3,1,2),_SwL2IGMPQueryInterval_Type())
swL2IGMPQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPQueryInterval.setStatus(_A)
class _SwL2IGMPMaxResponseTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_SwL2IGMPMaxResponseTime_Type.__name__=_B
_SwL2IGMPMaxResponseTime_Object=MibTableColumn
swL2IGMPMaxResponseTime=_SwL2IGMPMaxResponseTime_Object((1,3,6,1,4,1,171,11,64,1,2,10,3,1,3),_SwL2IGMPMaxResponseTime_Type())
swL2IGMPMaxResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMaxResponseTime.setStatus(_A)
class _SwL2IGMPRobustness_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2IGMPRobustness_Type.__name__=_B
_SwL2IGMPRobustness_Object=MibTableColumn
swL2IGMPRobustness=_SwL2IGMPRobustness_Object((1,3,6,1,4,1,171,11,64,1,2,10,3,1,4),_SwL2IGMPRobustness_Type())
swL2IGMPRobustness.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRobustness.setStatus(_A)
class _SwL2IGMPLastMemberQueryInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2IGMPLastMemberQueryInterval_Type.__name__=_B
_SwL2IGMPLastMemberQueryInterval_Object=MibTableColumn
swL2IGMPLastMemberQueryInterval=_SwL2IGMPLastMemberQueryInterval_Object((1,3,6,1,4,1,171,11,64,1,2,10,3,1,5),_SwL2IGMPLastMemberQueryInterval_Type())
swL2IGMPLastMemberQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPLastMemberQueryInterval.setStatus(_A)
class _SwL2IGMPHostTimeout_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPHostTimeout_Type.__name__=_B
_SwL2IGMPHostTimeout_Object=MibTableColumn
swL2IGMPHostTimeout=_SwL2IGMPHostTimeout_Object((1,3,6,1,4,1,171,11,64,1,2,10,3,1,6),_SwL2IGMPHostTimeout_Type())
swL2IGMPHostTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPHostTimeout.setStatus(_A)
class _SwL2IGMPRouteTimeout_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPRouteTimeout_Type.__name__=_B
_SwL2IGMPRouteTimeout_Object=MibTableColumn
swL2IGMPRouteTimeout=_SwL2IGMPRouteTimeout_Object((1,3,6,1,4,1,171,11,64,1,2,10,3,1,7),_SwL2IGMPRouteTimeout_Type())
swL2IGMPRouteTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouteTimeout.setStatus(_A)
class _SwL2IGMPLeaveTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16711450))
_SwL2IGMPLeaveTimer_Type.__name__=_B
_SwL2IGMPLeaveTimer_Object=MibTableColumn
swL2IGMPLeaveTimer=_SwL2IGMPLeaveTimer_Object((1,3,6,1,4,1,171,11,64,1,2,10,3,1,8),_SwL2IGMPLeaveTimer_Type())
swL2IGMPLeaveTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPLeaveTimer.setStatus(_A)
class _SwL2IGMPQueryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2IGMPQueryState_Type.__name__=_B
_SwL2IGMPQueryState_Object=MibTableColumn
swL2IGMPQueryState=_SwL2IGMPQueryState_Object((1,3,6,1,4,1,171,11,64,1,2,10,3,1,9),_SwL2IGMPQueryState_Type())
swL2IGMPQueryState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPQueryState.setStatus(_A)
class _SwL2IGMPCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('querier',2),('non-querier',3)))
_SwL2IGMPCurrentState_Type.__name__=_B
_SwL2IGMPCurrentState_Object=MibTableColumn
swL2IGMPCurrentState=_SwL2IGMPCurrentState_Object((1,3,6,1,4,1,171,11,64,1,2,10,3,1,10),_SwL2IGMPCurrentState_Type())
swL2IGMPCurrentState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPCurrentState.setStatus(_A)
class _SwL2IGMPCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_K,2),(_M,3)))
_SwL2IGMPCtrlState_Type.__name__=_B
_SwL2IGMPCtrlState_Object=MibTableColumn
swL2IGMPCtrlState=_SwL2IGMPCtrlState_Object((1,3,6,1,4,1,171,11,64,1,2,10,3,1,11),_SwL2IGMPCtrlState_Type())
swL2IGMPCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPCtrlState.setStatus(_A)
_SwL2IGMPQueryInfoTable_Object=MibTable
swL2IGMPQueryInfoTable=_SwL2IGMPQueryInfoTable_Object((1,3,6,1,4,1,171,11,64,1,2,10,4))
if mibBuilder.loadTexts:swL2IGMPQueryInfoTable.setStatus(_A)
_SwL2IGMPQueryInfoEntry_Object=MibTableRow
swL2IGMPQueryInfoEntry=_SwL2IGMPQueryInfoEntry_Object((1,3,6,1,4,1,171,11,64,1,2,10,4,1))
swL2IGMPQueryInfoEntry.setIndexNames((0,_E,_Ar))
if mibBuilder.loadTexts:swL2IGMPQueryInfoEntry.setStatus(_A)
class _SwL2IGMPInfoVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoVid_Type.__name__=_B
_SwL2IGMPInfoVid_Object=MibTableColumn
swL2IGMPInfoVid=_SwL2IGMPInfoVid_Object((1,3,6,1,4,1,171,11,64,1,2,10,4,1,1),_SwL2IGMPInfoVid_Type())
swL2IGMPInfoVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPInfoVid.setStatus(_A)
class _SwL2IGMPInfoQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoQueryCount_Type.__name__=_B
_SwL2IGMPInfoQueryCount_Object=MibTableColumn
swL2IGMPInfoQueryCount=_SwL2IGMPInfoQueryCount_Object((1,3,6,1,4,1,171,11,64,1,2,10,4,1,2),_SwL2IGMPInfoQueryCount_Type())
swL2IGMPInfoQueryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPInfoQueryCount.setStatus(_A)
class _SwL2IGMPInfoTxQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoTxQueryCount_Type.__name__=_B
_SwL2IGMPInfoTxQueryCount_Object=MibTableColumn
swL2IGMPInfoTxQueryCount=_SwL2IGMPInfoTxQueryCount_Object((1,3,6,1,4,1,171,11,64,1,2,10,4,1,3),_SwL2IGMPInfoTxQueryCount_Type())
swL2IGMPInfoTxQueryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPInfoTxQueryCount.setStatus(_A)
_SwL2IGMPInfoTable_Object=MibTable
swL2IGMPInfoTable=_SwL2IGMPInfoTable_Object((1,3,6,1,4,1,171,11,64,1,2,10,5))
if mibBuilder.loadTexts:swL2IGMPInfoTable.setStatus(_A)
_SwL2IGMPInfoEntry_Object=MibTableRow
swL2IGMPInfoEntry=_SwL2IGMPInfoEntry_Object((1,3,6,1,4,1,171,11,64,1,2,10,5,1))
swL2IGMPInfoEntry.setIndexNames((0,_E,_As),(0,_E,_At))
if mibBuilder.loadTexts:swL2IGMPInfoEntry.setStatus(_A)
class _SwL2IGMPVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPVid_Type.__name__=_B
_SwL2IGMPVid_Object=MibTableColumn
swL2IGMPVid=_SwL2IGMPVid_Object((1,3,6,1,4,1,171,11,64,1,2,10,5,1,1),_SwL2IGMPVid_Type())
swL2IGMPVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPVid.setStatus(_A)
_SwL2IGMPGroupIpAddr_Type=IpAddress
_SwL2IGMPGroupIpAddr_Object=MibTableColumn
swL2IGMPGroupIpAddr=_SwL2IGMPGroupIpAddr_Object((1,3,6,1,4,1,171,11,64,1,2,10,5,1,2),_SwL2IGMPGroupIpAddr_Type())
swL2IGMPGroupIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPGroupIpAddr.setStatus(_A)
_SwL2IGMPMacAddr_Type=MacAddress
_SwL2IGMPMacAddr_Object=MibTableColumn
swL2IGMPMacAddr=_SwL2IGMPMacAddr_Object((1,3,6,1,4,1,171,11,64,1,2,10,5,1,3),_SwL2IGMPMacAddr_Type())
swL2IGMPMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMacAddr.setStatus(_A)
_SwL2IGMPPortMap_Type=PortList
_SwL2IGMPPortMap_Object=MibTableColumn
swL2IGMPPortMap=_SwL2IGMPPortMap_Object((1,3,6,1,4,1,171,11,64,1,2,10,5,1,4),_SwL2IGMPPortMap_Type())
swL2IGMPPortMap.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPPortMap.setStatus(_A)
class _SwL2IGMPIpGroupReportCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPIpGroupReportCount_Type.__name__=_B
_SwL2IGMPIpGroupReportCount_Object=MibTableColumn
swL2IGMPIpGroupReportCount=_SwL2IGMPIpGroupReportCount_Object((1,3,6,1,4,1,171,11,64,1,2,10,5,1,5),_SwL2IGMPIpGroupReportCount_Type())
swL2IGMPIpGroupReportCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPIpGroupReportCount.setStatus(_A)
_SwL2IGMPMulticastVlanTable_Object=MibTable
swL2IGMPMulticastVlanTable=_SwL2IGMPMulticastVlanTable_Object((1,3,6,1,4,1,171,11,64,1,2,10,6))
if mibBuilder.loadTexts:swL2IGMPMulticastVlanTable.setStatus(_A)
_SwL2IGMPMulticastVlanEntry_Object=MibTableRow
swL2IGMPMulticastVlanEntry=_SwL2IGMPMulticastVlanEntry_Object((1,3,6,1,4,1,171,11,64,1,2,10,6,1))
swL2IGMPMulticastVlanEntry.setIndexNames((0,_E,_Au))
if mibBuilder.loadTexts:swL2IGMPMulticastVlanEntry.setStatus(_A)
class _SwL2IGMPMulticastVlanid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_SwL2IGMPMulticastVlanid_Type.__name__=_B
_SwL2IGMPMulticastVlanid_Object=MibTableColumn
swL2IGMPMulticastVlanid=_SwL2IGMPMulticastVlanid_Object((1,3,6,1,4,1,171,11,64,1,2,10,6,1,1),_SwL2IGMPMulticastVlanid_Type())
swL2IGMPMulticastVlanid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanid.setStatus(_A)
class _SwL2IGMPMulticastVlanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2IGMPMulticastVlanName_Type.__name__=_V
_SwL2IGMPMulticastVlanName_Object=MibTableColumn
swL2IGMPMulticastVlanName=_SwL2IGMPMulticastVlanName_Object((1,3,6,1,4,1,171,11,64,1,2,10,6,1,2),_SwL2IGMPMulticastVlanName_Type())
swL2IGMPMulticastVlanName.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanName.setStatus(_A)
_SwL2IGMPMulticastVlanSourcePort_Type=PortList
_SwL2IGMPMulticastVlanSourcePort_Object=MibTableColumn
swL2IGMPMulticastVlanSourcePort=_SwL2IGMPMulticastVlanSourcePort_Object((1,3,6,1,4,1,171,11,64,1,2,10,6,1,3),_SwL2IGMPMulticastVlanSourcePort_Type())
swL2IGMPMulticastVlanSourcePort.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanSourcePort.setStatus(_A)
_SwL2IGMPMulticastVlanMemberPort_Type=PortList
_SwL2IGMPMulticastVlanMemberPort_Object=MibTableColumn
swL2IGMPMulticastVlanMemberPort=_SwL2IGMPMulticastVlanMemberPort_Object((1,3,6,1,4,1,171,11,64,1,2,10,6,1,4),_SwL2IGMPMulticastVlanMemberPort_Type())
swL2IGMPMulticastVlanMemberPort.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanMemberPort.setStatus(_A)
_SwL2IGMPMulticastVlanRowStatus_Type=RowStatus
_SwL2IGMPMulticastVlanRowStatus_Object=MibTableColumn
swL2IGMPMulticastVlanRowStatus=_SwL2IGMPMulticastVlanRowStatus_Object((1,3,6,1,4,1,171,11,64,1,2,10,6,1,5),_SwL2IGMPMulticastVlanRowStatus_Type())
swL2IGMPMulticastVlanRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanRowStatus.setStatus(_A)
_SwL2IGMPMulticastVlanReplaceSourceIP_Type=IpAddress
_SwL2IGMPMulticastVlanReplaceSourceIP_Object=MibTableColumn
swL2IGMPMulticastVlanReplaceSourceIP=_SwL2IGMPMulticastVlanReplaceSourceIP_Object((1,3,6,1,4,1,171,11,64,1,2,10,6,1,6),_SwL2IGMPMulticastVlanReplaceSourceIP_Type())
swL2IGMPMulticastVlanReplaceSourceIP.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanReplaceSourceIP.setStatus(_A)
_SwL2IGMPRouterPortTable_Object=MibTable
swL2IGMPRouterPortTable=_SwL2IGMPRouterPortTable_Object((1,3,6,1,4,1,171,11,64,1,2,10,7))
if mibBuilder.loadTexts:swL2IGMPRouterPortTable.setStatus(_A)
_SwL2IGMPRouterPortEntry_Object=MibTableRow
swL2IGMPRouterPortEntry=_SwL2IGMPRouterPortEntry_Object((1,3,6,1,4,1,171,11,64,1,2,10,7,1))
swL2IGMPRouterPortEntry.setIndexNames((0,_E,_Av))
if mibBuilder.loadTexts:swL2IGMPRouterPortEntry.setStatus(_A)
class _SwL2IGMPRouterPortVlanid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2IGMPRouterPortVlanid_Type.__name__=_B
_SwL2IGMPRouterPortVlanid_Object=MibTableColumn
swL2IGMPRouterPortVlanid=_SwL2IGMPRouterPortVlanid_Object((1,3,6,1,4,1,171,11,64,1,2,10,7,1,1),_SwL2IGMPRouterPortVlanid_Type())
swL2IGMPRouterPortVlanid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterPortVlanid.setStatus(_A)
class _SwL2IGMPRouterPortVlanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2IGMPRouterPortVlanName_Type.__name__=_V
_SwL2IGMPRouterPortVlanName_Object=MibTableColumn
swL2IGMPRouterPortVlanName=_SwL2IGMPRouterPortVlanName_Object((1,3,6,1,4,1,171,11,64,1,2,10,7,1,2),_SwL2IGMPRouterPortVlanName_Type())
swL2IGMPRouterPortVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterPortVlanName.setStatus(_A)
_SwL2IGMPRouterPortStaticPortList_Type=PortList
_SwL2IGMPRouterPortStaticPortList_Object=MibTableColumn
swL2IGMPRouterPortStaticPortList=_SwL2IGMPRouterPortStaticPortList_Object((1,3,6,1,4,1,171,11,64,1,2,10,7,1,3),_SwL2IGMPRouterPortStaticPortList_Type())
swL2IGMPRouterPortStaticPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouterPortStaticPortList.setStatus(_A)
_SwL2IGMPRouterPortDynamicPortList_Type=PortList
_SwL2IGMPRouterPortDynamicPortList_Object=MibTableColumn
swL2IGMPRouterPortDynamicPortList=_SwL2IGMPRouterPortDynamicPortList_Object((1,3,6,1,4,1,171,11,64,1,2,10,7,1,4),_SwL2IGMPRouterPortDynamicPortList_Type())
swL2IGMPRouterPortDynamicPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterPortDynamicPortList.setStatus(_A)
_SwL2IGMPRouterPortForbiddenPortList_Type=PortList
_SwL2IGMPRouterPortForbiddenPortList_Object=MibTableColumn
swL2IGMPRouterPortForbiddenPortList=_SwL2IGMPRouterPortForbiddenPortList_Object((1,3,6,1,4,1,171,11,64,1,2,10,7,1,5),_SwL2IGMPRouterPortForbiddenPortList_Type())
swL2IGMPRouterPortForbiddenPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouterPortForbiddenPortList.setStatus(_A)
_SwL2DhcpRelayMgmt_ObjectIdentity=ObjectIdentity
swL2DhcpRelayMgmt=_SwL2DhcpRelayMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,11))
class _SwL2DhcpRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DhcpRelayState_Type.__name__=_B
_SwL2DhcpRelayState_Object=MibScalar
swL2DhcpRelayState=_SwL2DhcpRelayState_Object((1,3,6,1,4,1,171,11,64,1,2,11,1),_SwL2DhcpRelayState_Type())
swL2DhcpRelayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayState.setStatus(_I)
class _SwL2DhcpRelayHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_SwL2DhcpRelayHopCount_Type.__name__=_B
_SwL2DhcpRelayHopCount_Object=MibScalar
swL2DhcpRelayHopCount=_SwL2DhcpRelayHopCount_Object((1,3,6,1,4,1,171,11,64,1,2,11,2),_SwL2DhcpRelayHopCount_Type())
swL2DhcpRelayHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayHopCount.setStatus(_I)
class _SwL2DhcpRelayTimeThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2DhcpRelayTimeThreshold_Type.__name__=_B
_SwL2DhcpRelayTimeThreshold_Object=MibScalar
swL2DhcpRelayTimeThreshold=_SwL2DhcpRelayTimeThreshold_Object((1,3,6,1,4,1,171,11,64,1,2,11,3),_SwL2DhcpRelayTimeThreshold_Type())
swL2DhcpRelayTimeThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayTimeThreshold.setStatus(_I)
class _SwL2DhcpRelayOption82State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DhcpRelayOption82State_Type.__name__=_B
_SwL2DhcpRelayOption82State_Object=MibScalar
swL2DhcpRelayOption82State=_SwL2DhcpRelayOption82State_Object((1,3,6,1,4,1,171,11,64,1,2,11,4),_SwL2DhcpRelayOption82State_Type())
swL2DhcpRelayOption82State.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayOption82State.setStatus(_I)
class _SwL2DhcpRelayOption82Check_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DhcpRelayOption82Check_Type.__name__=_B
_SwL2DhcpRelayOption82Check_Object=MibScalar
swL2DhcpRelayOption82Check=_SwL2DhcpRelayOption82Check_Object((1,3,6,1,4,1,171,11,64,1,2,11,5),_SwL2DhcpRelayOption82Check_Type())
swL2DhcpRelayOption82Check.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayOption82Check.setStatus(_I)
class _SwL2DhcpRelayOption82Policy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('replace',1),('drop',2),('keep',3)))
_SwL2DhcpRelayOption82Policy_Type.__name__=_B
_SwL2DhcpRelayOption82Policy_Object=MibScalar
swL2DhcpRelayOption82Policy=_SwL2DhcpRelayOption82Policy_Object((1,3,6,1,4,1,171,11,64,1,2,11,6),_SwL2DhcpRelayOption82Policy_Type())
swL2DhcpRelayOption82Policy.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayOption82Policy.setStatus(_I)
_SwL2DhcpRelayCtrlTable_Object=MibTable
swL2DhcpRelayCtrlTable=_SwL2DhcpRelayCtrlTable_Object((1,3,6,1,4,1,171,11,64,1,2,11,7))
if mibBuilder.loadTexts:swL2DhcpRelayCtrlTable.setStatus(_I)
_SwL2DhcpRelayCtrlEntry_Object=MibTableRow
swL2DhcpRelayCtrlEntry=_SwL2DhcpRelayCtrlEntry_Object((1,3,6,1,4,1,171,11,64,1,2,11,7,1))
swL2DhcpRelayCtrlEntry.setIndexNames((0,_E,_Aw),(0,_E,_Ax))
if mibBuilder.loadTexts:swL2DhcpRelayCtrlEntry.setStatus(_I)
class _SwL2DhcpRelayCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL2DhcpRelayCtrlInterfaceName_Type.__name__=_Q
_SwL2DhcpRelayCtrlInterfaceName_Object=MibTableColumn
swL2DhcpRelayCtrlInterfaceName=_SwL2DhcpRelayCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,64,1,2,11,7,1,1),_SwL2DhcpRelayCtrlInterfaceName_Type())
swL2DhcpRelayCtrlInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpRelayCtrlInterfaceName.setStatus(_I)
_SwL2DhcpRelayCtrlServer_Type=IpAddress
_SwL2DhcpRelayCtrlServer_Object=MibTableColumn
swL2DhcpRelayCtrlServer=_SwL2DhcpRelayCtrlServer_Object((1,3,6,1,4,1,171,11,64,1,2,11,7,1,2),_SwL2DhcpRelayCtrlServer_Type())
swL2DhcpRelayCtrlServer.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpRelayCtrlServer.setStatus(_I)
class _SwL2DhcpRelayCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('invalid',2),('valid',3)))
_SwL2DhcpRelayCtrlState_Type.__name__=_B
_SwL2DhcpRelayCtrlState_Object=MibTableColumn
swL2DhcpRelayCtrlState=_SwL2DhcpRelayCtrlState_Object((1,3,6,1,4,1,171,11,64,1,2,11,7,1,3),_SwL2DhcpRelayCtrlState_Type())
swL2DhcpRelayCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayCtrlState.setStatus(_I)
_SwL2LoopDetectMgmt_ObjectIdentity=ObjectIdentity
swL2LoopDetectMgmt=_SwL2LoopDetectMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,12))
_SwL2LoopDetectCtrl_ObjectIdentity=ObjectIdentity
swL2LoopDetectCtrl=_SwL2LoopDetectCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,12,1))
class _SwL2LoopDetectAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2LoopDetectAdminState_Type.__name__=_B
_SwL2LoopDetectAdminState_Object=MibScalar
swL2LoopDetectAdminState=_SwL2LoopDetectAdminState_Object((1,3,6,1,4,1,171,11,64,1,2,12,1,1),_SwL2LoopDetectAdminState_Type())
swL2LoopDetectAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectAdminState.setStatus(_A)
class _SwL2LoopDetectInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_SwL2LoopDetectInterval_Type.__name__=_B
_SwL2LoopDetectInterval_Object=MibScalar
swL2LoopDetectInterval=_SwL2LoopDetectInterval_Object((1,3,6,1,4,1,171,11,64,1,2,12,1,2),_SwL2LoopDetectInterval_Type())
swL2LoopDetectInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectInterval.setStatus(_A)
class _SwL2LoopDetectRecoverTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_SwL2LoopDetectRecoverTime_Type.__name__=_B
_SwL2LoopDetectRecoverTime_Object=MibScalar
swL2LoopDetectRecoverTime=_SwL2LoopDetectRecoverTime_Object((1,3,6,1,4,1,171,11,64,1,2,12,1,3),_SwL2LoopDetectRecoverTime_Type())
swL2LoopDetectRecoverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectRecoverTime.setStatus(_A)
class _SwL2LoopDetectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan-based',1),('port-based',2)))
_SwL2LoopDetectMode_Type.__name__=_B
_SwL2LoopDetectMode_Object=MibScalar
swL2LoopDetectMode=_SwL2LoopDetectMode_Object((1,3,6,1,4,1,171,11,64,1,2,12,1,4),_SwL2LoopDetectMode_Type())
swL2LoopDetectMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectMode.setStatus(_A)
_SwL2LoopDetectPortMgmt_ObjectIdentity=ObjectIdentity
swL2LoopDetectPortMgmt=_SwL2LoopDetectPortMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,12,2))
_SwL2LoopDetectPortTable_Object=MibTable
swL2LoopDetectPortTable=_SwL2LoopDetectPortTable_Object((1,3,6,1,4,1,171,11,64,1,2,12,2,1))
if mibBuilder.loadTexts:swL2LoopDetectPortTable.setStatus(_A)
_SwL2LoopDetectPortEntry_Object=MibTableRow
swL2LoopDetectPortEntry=_SwL2LoopDetectPortEntry_Object((1,3,6,1,4,1,171,11,64,1,2,12,2,1,1))
swL2LoopDetectPortEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:swL2LoopDetectPortEntry.setStatus(_A)
class _SwL2LoopDetectPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2LoopDetectPortIndex_Type.__name__=_B
_SwL2LoopDetectPortIndex_Object=MibTableColumn
swL2LoopDetectPortIndex=_SwL2LoopDetectPortIndex_Object((1,3,6,1,4,1,171,11,64,1,2,12,2,1,1,1),_SwL2LoopDetectPortIndex_Type())
swL2LoopDetectPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectPortIndex.setStatus(_A)
class _SwL2LoopDetectPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2LoopDetectPortState_Type.__name__=_B
_SwL2LoopDetectPortState_Object=MibTableColumn
swL2LoopDetectPortState=_SwL2LoopDetectPortState_Object((1,3,6,1,4,1,171,11,64,1,2,12,2,1,1,2),_SwL2LoopDetectPortState_Type())
swL2LoopDetectPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectPortState.setStatus(_A)
_SwL2LoopDetectPortLoopVLAN_Type=DisplayString
_SwL2LoopDetectPortLoopVLAN_Object=MibTableColumn
swL2LoopDetectPortLoopVLAN=_SwL2LoopDetectPortLoopVLAN_Object((1,3,6,1,4,1,171,11,64,1,2,12,2,1,1,3),_SwL2LoopDetectPortLoopVLAN_Type())
swL2LoopDetectPortLoopVLAN.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectPortLoopVLAN.setStatus(_A)
class _SwL2LoopDetectPortLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('loop',2),('error',3)))
_SwL2LoopDetectPortLoopStatus_Type.__name__=_B
_SwL2LoopDetectPortLoopStatus_Object=MibTableColumn
swL2LoopDetectPortLoopStatus=_SwL2LoopDetectPortLoopStatus_Object((1,3,6,1,4,1,171,11,64,1,2,12,2,1,1,4),_SwL2LoopDetectPortLoopStatus_Type())
swL2LoopDetectPortLoopStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectPortLoopStatus.setStatus(_A)
_SwL2TrafficSegMgmt_ObjectIdentity=ObjectIdentity
swL2TrafficSegMgmt=_SwL2TrafficSegMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,13))
_SwL2TrafficSegTable_Object=MibTable
swL2TrafficSegTable=_SwL2TrafficSegTable_Object((1,3,6,1,4,1,171,11,64,1,2,13,1))
if mibBuilder.loadTexts:swL2TrafficSegTable.setStatus(_A)
_SwL2TrafficSegEntry_Object=MibTableRow
swL2TrafficSegEntry=_SwL2TrafficSegEntry_Object((1,3,6,1,4,1,171,11,64,1,2,13,1,1))
swL2TrafficSegEntry.setIndexNames((0,_E,_Ay))
if mibBuilder.loadTexts:swL2TrafficSegEntry.setStatus(_A)
class _SwL2TrafficSegPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrafficSegPort_Type.__name__=_B
_SwL2TrafficSegPort_Object=MibTableColumn
swL2TrafficSegPort=_SwL2TrafficSegPort_Object((1,3,6,1,4,1,171,11,64,1,2,13,1,1,1),_SwL2TrafficSegPort_Type())
swL2TrafficSegPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrafficSegPort.setStatus(_A)
_SwL2TrafficSegForwardPorts_Type=PortList
_SwL2TrafficSegForwardPorts_Object=MibTableColumn
swL2TrafficSegForwardPorts=_SwL2TrafficSegForwardPorts_Object((1,3,6,1,4,1,171,11,64,1,2,13,1,1,2),_SwL2TrafficSegForwardPorts_Type())
swL2TrafficSegForwardPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrafficSegForwardPorts.setStatus(_A)
_SwL2PortSecurityMgmt_ObjectIdentity=ObjectIdentity
swL2PortSecurityMgmt=_SwL2PortSecurityMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,14))
_SwL2PortSecurityControlTable_Object=MibTable
swL2PortSecurityControlTable=_SwL2PortSecurityControlTable_Object((1,3,6,1,4,1,171,11,64,1,2,14,1))
if mibBuilder.loadTexts:swL2PortSecurityControlTable.setStatus(_A)
_SwL2PortSecurityControlEntry_Object=MibTableRow
swL2PortSecurityControlEntry=_SwL2PortSecurityControlEntry_Object((1,3,6,1,4,1,171,11,64,1,2,14,1,1))
swL2PortSecurityControlEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:swL2PortSecurityControlEntry.setStatus(_A)
class _SwL2PortSecurityPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2PortSecurityPortIndex_Type.__name__=_B
_SwL2PortSecurityPortIndex_Object=MibTableColumn
swL2PortSecurityPortIndex=_SwL2PortSecurityPortIndex_Object((1,3,6,1,4,1,171,11,64,1,2,14,1,1,1),_SwL2PortSecurityPortIndex_Type())
swL2PortSecurityPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityPortIndex.setStatus(_A)
class _SwL2PortSecurityMaxLernAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortSecurityMaxLernAddr_Type.__name__=_B
_SwL2PortSecurityMaxLernAddr_Object=MibTableColumn
swL2PortSecurityMaxLernAddr=_SwL2PortSecurityMaxLernAddr_Object((1,3,6,1,4,1,171,11,64,1,2,14,1,1,2),_SwL2PortSecurityMaxLernAddr_Type())
swL2PortSecurityMaxLernAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityMaxLernAddr.setStatus(_A)
class _SwL2PortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('permanent',2),('deleteOnTimeout',3),('deleteOnReset',4)))
_SwL2PortSecurityMode_Type.__name__=_B
_SwL2PortSecurityMode_Object=MibTableColumn
swL2PortSecurityMode=_SwL2PortSecurityMode_Object((1,3,6,1,4,1,171,11,64,1,2,14,1,1,3),_SwL2PortSecurityMode_Type())
swL2PortSecurityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityMode.setStatus(_A)
class _SwL2PortSecurityAdmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_M,2),(_K,3)))
_SwL2PortSecurityAdmState_Type.__name__=_B
_SwL2PortSecurityAdmState_Object=MibTableColumn
swL2PortSecurityAdmState=_SwL2PortSecurityAdmState_Object((1,3,6,1,4,1,171,11,64,1,2,14,1,1,4),_SwL2PortSecurityAdmState_Type())
swL2PortSecurityAdmState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityAdmState.setStatus(_A)
class _SwL2PortSecurityTrapLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_M,2),(_K,3)))
_SwL2PortSecurityTrapLogState_Type.__name__=_B
_SwL2PortSecurityTrapLogState_Object=MibScalar
swL2PortSecurityTrapLogState=_SwL2PortSecurityTrapLogState_Object((1,3,6,1,4,1,171,11,64,1,2,14,2),_SwL2PortSecurityTrapLogState_Type())
swL2PortSecurityTrapLogState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityTrapLogState.setStatus(_A)
_SwL2MgmtMIBTraps_ObjectIdentity=ObjectIdentity
swL2MgmtMIBTraps=_SwL2MgmtMIBTraps_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,15))
_SwL2MgmtMIBTrapPrefix_ObjectIdentity=ObjectIdentity
swL2MgmtMIBTrapPrefix=_SwL2MgmtMIBTrapPrefix_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,15,0))
_Swl2NotificationBidings_ObjectIdentity=ObjectIdentity
swl2NotificationBidings=_Swl2NotificationBidings_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,15,1))
class _SwL2macNotifyInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_SwL2macNotifyInfo_Type.__name__=_c
_SwL2macNotifyInfo_Object=MibScalar
swL2macNotifyInfo=_SwL2macNotifyInfo_Object((1,3,6,1,4,1,171,11,64,1,2,15,1,1),_SwL2macNotifyInfo_Type())
swL2macNotifyInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2macNotifyInfo.setStatus(_A)
_Swl2NotifyPortSecurity_ObjectIdentity=ObjectIdentity
swl2NotifyPortSecurity=_Swl2NotifyPortSecurity_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,15,2))
_SwL2PortSecurityViolationMac_Type=MacAddress
_SwL2PortSecurityViolationMac_Object=MibScalar
swL2PortSecurityViolationMac=_SwL2PortSecurityViolationMac_Object((1,3,6,1,4,1,171,11,64,1,2,15,2,1),_SwL2PortSecurityViolationMac_Type())
swL2PortSecurityViolationMac.setMaxAccess(_T)
if mibBuilder.loadTexts:swL2PortSecurityViolationMac.setStatus(_A)
_Swl2NotifyIpMacBinding_ObjectIdentity=ObjectIdentity
swl2NotifyIpMacBinding=_Swl2NotifyIpMacBinding_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,15,3))
_SwL2IpMacBindingViolationIP_Type=MacAddress
_SwL2IpMacBindingViolationIP_Object=MibScalar
swL2IpMacBindingViolationIP=_SwL2IpMacBindingViolationIP_Object((1,3,6,1,4,1,171,11,64,1,2,15,3,1),_SwL2IpMacBindingViolationIP_Type())
swL2IpMacBindingViolationIP.setMaxAccess(_T)
if mibBuilder.loadTexts:swL2IpMacBindingViolationIP.setStatus(_A)
_SwL2IpMacBindingViolationMac_Type=MacAddress
_SwL2IpMacBindingViolationMac_Object=MibScalar
swL2IpMacBindingViolationMac=_SwL2IpMacBindingViolationMac_Object((1,3,6,1,4,1,171,11,64,1,2,15,3,2),_SwL2IpMacBindingViolationMac_Type())
swL2IpMacBindingViolationMac.setMaxAccess(_T)
if mibBuilder.loadTexts:swL2IpMacBindingViolationMac.setStatus(_A)
_Swl2NotifyLoopDetect_ObjectIdentity=ObjectIdentity
swl2NotifyLoopDetect=_Swl2NotifyLoopDetect_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,15,4))
_SwL2VlanLoopDetectVID_Type=Integer32
_SwL2VlanLoopDetectVID_Object=MibScalar
swL2VlanLoopDetectVID=_SwL2VlanLoopDetectVID_Object((1,3,6,1,4,1,171,11,64,1,2,15,4,1),_SwL2VlanLoopDetectVID_Type())
swL2VlanLoopDetectVID.setMaxAccess(_T)
if mibBuilder.loadTexts:swL2VlanLoopDetectVID.setStatus(_A)
_SwL2DhcpLocalRelayMgmt_ObjectIdentity=ObjectIdentity
swL2DhcpLocalRelayMgmt=_SwL2DhcpLocalRelayMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,64,1,2,24))
class _SwL2DhcpLocalRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DhcpLocalRelayState_Type.__name__=_B
_SwL2DhcpLocalRelayState_Object=MibScalar
swL2DhcpLocalRelayState=_SwL2DhcpLocalRelayState_Object((1,3,6,1,4,1,171,11,64,1,2,24,1),_SwL2DhcpLocalRelayState_Type())
swL2DhcpLocalRelayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpLocalRelayState.setStatus(_A)
_SwL2DhcpLocalRelayVLANTable_Object=MibTable
swL2DhcpLocalRelayVLANTable=_SwL2DhcpLocalRelayVLANTable_Object((1,3,6,1,4,1,171,11,64,1,2,24,2))
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANTable.setStatus(_A)
_SwL2DhcpLocalRelayVLANEntry_Object=MibTableRow
swL2DhcpLocalRelayVLANEntry=_SwL2DhcpLocalRelayVLANEntry_Object((1,3,6,1,4,1,171,11,64,1,2,24,2,1))
swL2DhcpLocalRelayVLANEntry.setIndexNames((0,_E,_Az))
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANEntry.setStatus(_A)
class _SwL2DhcpLocalRelayVLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2DhcpLocalRelayVLANID_Type.__name__=_B
_SwL2DhcpLocalRelayVLANID_Object=MibTableColumn
swL2DhcpLocalRelayVLANID=_SwL2DhcpLocalRelayVLANID_Object((1,3,6,1,4,1,171,11,64,1,2,24,2,1,1),_SwL2DhcpLocalRelayVLANID_Type())
swL2DhcpLocalRelayVLANID.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANID.setStatus(_A)
class _SwL2DhcpLocalRelayVLANState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SwL2DhcpLocalRelayVLANState_Type.__name__=_B
_SwL2DhcpLocalRelayVLANState_Object=MibTableColumn
swL2DhcpLocalRelayVLANState=_SwL2DhcpLocalRelayVLANState_Object((1,3,6,1,4,1,171,11,64,1,2,24,2,1,2),_SwL2DhcpLocalRelayVLANState_Type())
swL2DhcpLocalRelayVLANState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANState.setStatus(_A)
swL2macNotification=NotificationType((1,3,6,1,4,1,171,11,64,1,2,15,0,3))
swL2macNotification.setObjects((_E,_A_))
if mibBuilder.loadTexts:swL2macNotification.setStatus(_A)
swL2porttypechgNotification=NotificationType((1,3,6,1,4,1,171,11,64,1,2,15,0,4))
swL2porttypechgNotification.setObjects(*((_E,_X),(_E,_B0)))
if mibBuilder.loadTexts:swL2porttypechgNotification.setStatus(_A)
swPowerStatusChg=NotificationType((1,3,6,1,4,1,171,11,64,1,2,15,0,5))
swPowerStatusChg.setObjects(*((_E,_O),(_E,_P),(_E,_U)))
if mibBuilder.loadTexts:swPowerStatusChg.setStatus(_A)
swPowerFailure=NotificationType((1,3,6,1,4,1,171,11,64,1,2,15,0,6))
swPowerFailure.setObjects(*((_E,_O),(_E,_P),(_E,_U)))
if mibBuilder.loadTexts:swPowerFailure.setStatus(_A)
swPowerRecover=NotificationType((1,3,6,1,4,1,171,11,64,1,2,15,0,7))
swPowerRecover.setObjects(*((_E,_O),(_E,_P),(_E,_U)))
if mibBuilder.loadTexts:swPowerRecover.setStatus(_A)
swL2PortSecurityViolationTrap=NotificationType((1,3,6,1,4,1,171,11,64,1,2,15,2,2))
swL2PortSecurityViolationTrap.setObjects(*((_E,_a),(_E,_B1)))
if mibBuilder.loadTexts:swL2PortSecurityViolationTrap.setStatus(_A)
swL2IpMacBindingViolationTrap=NotificationType((1,3,6,1,4,1,171,11,64,1,2,15,3,3))
swL2IpMacBindingViolationTrap.setObjects(*((_E,_Z),(_E,_B2),(_E,_B3)))
if mibBuilder.loadTexts:swL2IpMacBindingViolationTrap.setStatus(_A)
swL2PortLoopOccurred=NotificationType((1,3,6,1,4,1,171,11,64,1,2,15,4,2))
swL2PortLoopOccurred.setObjects((_E,_N))
if mibBuilder.loadTexts:swL2PortLoopOccurred.setStatus(_A)
swL2PortLoopRestart=NotificationType((1,3,6,1,4,1,171,11,64,1,2,15,4,3))
swL2PortLoopRestart.setObjects((_E,_N))
if mibBuilder.loadTexts:swL2PortLoopRestart.setStatus(_A)
swL2VlanLoopOccurred=NotificationType((1,3,6,1,4,1,171,11,64,1,2,15,4,4))
swL2VlanLoopOccurred.setObjects(*((_E,_N),(_E,_b)))
if mibBuilder.loadTexts:swL2VlanLoopOccurred.setStatus(_A)
swL2VlanLoopRestart=NotificationType((1,3,6,1,4,1,171,11,64,1,2,15,4,5))
swL2VlanLoopRestart.setObjects(*((_E,_N),(_E,_b)))
if mibBuilder.loadTexts:swL2VlanLoopRestart.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'PortList':PortList,'VlanIndex':VlanIndex,'VlanId':VlanId,'swL2MgmtMIB':swL2MgmtMIB,'swL2DevMgmt':swL2DevMgmt,'swL2DevInfo':swL2DevInfo,'swDevInfoSystemUpTime':swDevInfoSystemUpTime,'swDevInfoTotalNumOfPort':swDevInfoTotalNumOfPort,'swDevInfoNumOfPortInUse':swDevInfoNumOfPortInUse,'swDevInfoConsoleInUse':swDevInfoConsoleInUse,'swDevInfoModuleType':swDevInfoModuleType,'swDevInfoPowerTable':swDevInfoPowerTable,'swDevInfoPowerEntry':swDevInfoPowerEntry,_O:swDevInfoPowerUnitIndex,_P:swDevInfoPowerID,_U:swDevInfoPowerStatus,'swL2DevCtrl':swL2DevCtrl,'swL2DevCtrlStpState':swL2DevCtrlStpState,'swL2DevCtrlIGMPSnooping':swL2DevCtrlIGMPSnooping,'swL2DevCtrlRmonState':swL2DevCtrlRmonState,'swL2DevCtrlCleanAllStatisticCounter':swL2DevCtrlCleanAllStatisticCounter,'swL2DevCtrlVlanIdOfFDBTbl':swL2DevCtrlVlanIdOfFDBTbl,'swL2MACNotifyState':swL2MACNotifyState,'swL2MACNotifyHistorySize':swL2MACNotifyHistorySize,'swL2MACNotifyInterval':swL2MACNotifyInterval,'swL2DevCtrlAsymVlanState':swL2DevCtrlAsymVlanState,'swL2DevCtrlManagementVlanId':swL2DevCtrlManagementVlanId,'swL2DevCtrlTelnet':swL2DevCtrlTelnet,'swL2DevCtrlTelnetState':swL2DevCtrlTelnetState,'swL2DevCtrlTelnetTcpPort':swL2DevCtrlTelnetTcpPort,'swL2DevCtrlLLDPState':swL2DevCtrlLLDPState,'swL2DevCtrlWeb':swL2DevCtrlWeb,'swL2DevCtrlWebState':swL2DevCtrlWebState,'swL2DevCtrlWebTcpPort':swL2DevCtrlWebTcpPort,'swL2DevCtrlLLDPForwardMessageState':swL2DevCtrlLLDPForwardMessageState,'swL2DevAlarm':swL2DevAlarm,'swL2DevAlarmNewRoot':swL2DevAlarmNewRoot,'swL2DevAlarmTopologyChange':swL2DevAlarmTopologyChange,'swL2DevAlarmLinkChange':swL2DevAlarmLinkChange,'swL2VlanMgmt':swL2VlanMgmt,'swL2VlanAdvertisementTable':swL2VlanAdvertisementTable,'swL2VlanAdvertisementEntry':swL2VlanAdvertisementEntry,_d:swL2VlanIndex,'swL2VlanName':swL2VlanName,'swL2VlanAdvertiseState':swL2VlanAdvertiseState,'swL2PortMgmt':swL2PortMgmt,'swL2PortInfoTable':swL2PortInfoTable,'swL2PortInfoEntry':swL2PortInfoEntry,_X:swL2PortInfoPortIndex,'swL2PortInfoUnitIndex':swL2PortInfoUnitIndex,_B0:swL2PortInfoType,'swL2PortInfoLinkStatus':swL2PortInfoLinkStatus,'swL2PortInfoNwayStatus':swL2PortInfoNwayStatus,'swL2PortInfoModuleType':swL2PortInfoModuleType,'swL2PortInfoErrorDisabled':swL2PortInfoErrorDisabled,'swL2PortCtrlTable':swL2PortCtrlTable,'swL2PortCtrlEntry':swL2PortCtrlEntry,_AM:swL2PortCtrlPortIndex,'swL2PortCtrlUnitIndex':swL2PortCtrlUnitIndex,'swL2PortCtrlAdminState':swL2PortCtrlAdminState,'swL2PortCtrlNwayState':swL2PortCtrlNwayState,'swL2PortCtrlFlowCtrlState':swL2PortCtrlFlowCtrlState,'swL2PortCtrlLockState':swL2PortCtrlLockState,'swL2PortCtrlMACNotifyState':swL2PortCtrlMACNotifyState,'swL2PortCtrlMulticastfilter':swL2PortCtrlMulticastfilter,'swL2PortCtrlMdixState':swL2PortCtrlMdixState,'swL2PortInformationTable':swL2PortInformationTable,'swL2PortInformationEntry':swL2PortInformationEntry,_AX:swL2PortInformationPortIndex,_AY:swL2PortInformationMediumType,'swL2PortInformationUnitID':swL2PortInformationUnitID,'swL2PortInformationType':swL2PortInformationType,'swL2PortInformationLinkStatus':swL2PortInformationLinkStatus,'swL2PortInformationNwayStatus':swL2PortInformationNwayStatus,'swL2PortInformationModuleType':swL2PortInformationModuleType,'swL2PortInformationErrorDisabled':swL2PortInformationErrorDisabled,'swL2PortControlTable':swL2PortControlTable,'swL2PortControlEntry':swL2PortControlEntry,_AZ:swL2PortControlPortIndex,_Aa:swL2PortControlMediumType,'swL2PortControlUnitIndex':swL2PortControlUnitIndex,'swL2PortControlAdminState':swL2PortControlAdminState,'swL2PortControlNwayState':swL2PortControlNwayState,'swL2PortControlFlowCtrlState':swL2PortControlFlowCtrlState,'swL2PortControlLockState':swL2PortControlLockState,'swL2PortControlMACNotifyState':swL2PortControlMACNotifyState,'swL2PortControlMulticastfilter':swL2PortControlMulticastfilter,'swL2PortControlMdixState':swL2PortControlMdixState,'swL2LimitedMulticastMgmt':swL2LimitedMulticastMgmt,'swL2MulticastRangeTable':swL2MulticastRangeTable,'swL2MulticastRangeEntry':swL2MulticastRangeEntry,_Ab:swL2MulticastRangeName,'swL2MulticastRangeFromIp':swL2MulticastRangeFromIp,'swL2MulticastRangeToIp':swL2MulticastRangeToIp,'swL2MulticastRangeRowStatus':swL2MulticastRangeRowStatus,'swL2LimitedMulticastPortInfo':swL2LimitedMulticastPortInfo,'swL2LimitedMulticastStatusTable':swL2LimitedMulticastStatusTable,'swL2LimitedMulticastStatusEntry':swL2LimitedMulticastStatusEntry,_Y:swL2LimitedMulticastPort,'swL2LimitedMulticastAccess':swL2LimitedMulticastAccess,'swL2LimitedMulticastState':swL2LimitedMulticastState,'swL2LimitedMulticastRangeTable':swL2LimitedMulticastRangeTable,'swL2LimitedMulticastRangeEntry':swL2LimitedMulticastRangeEntry,_Ac:swL2LimitedMulticastID,'swL2LimitedMulticastRangeName':swL2LimitedMulticastRangeName,'swL2LimitedMulticastFromIp':swL2LimitedMulticastFromIp,'swL2LimitedMulticastToIp':swL2LimitedMulticastToIp,'swL2LimitedMulticastRowStatus':swL2LimitedMulticastRowStatus,'swL2QOSMgmt':swL2QOSMgmt,'swL2QOSBandwidthControlTable':swL2QOSBandwidthControlTable,'swL2QOSBandwidthControlEntry':swL2QOSBandwidthControlEntry,_Ad:swL2QOSBandwidthPortIndex,'swL2QOSBandwidthRxRate':swL2QOSBandwidthRxRate,'swL2QOSBandwidthTxRate':swL2QOSBandwidthTxRate,'swL2QOSBandwidthRadiusRxRate':swL2QOSBandwidthRadiusRxRate,'swL2QOSBandwidthRadiusTxRate':swL2QOSBandwidthRadiusTxRate,'swL2QOSSchedulingTable':swL2QOSSchedulingTable,'swL2QOSSchedulingEntry':swL2QOSSchedulingEntry,_Ae:swL2QOSSchedulingClassIndex,'swL2QOSSchedulingMaxPkts':swL2QOSSchedulingMaxPkts,'swL2QOSSchedulingMaxLatency':swL2QOSSchedulingMaxLatency,'swL2QOS8021pUserPriorityTable':swL2QOS8021pUserPriorityTable,'swL2QOS8021pUserPriorityEntry':swL2QOS8021pUserPriorityEntry,_Af:swL2QOS8021pUserPriorityIndex,'swL2QOS8021pUserPriorityClass':swL2QOS8021pUserPriorityClass,'swL2QOS8021pDefaultPriorityTable':swL2QOS8021pDefaultPriorityTable,'swL2QOS8021pDefaultPriorityEntry':swL2QOS8021pDefaultPriorityEntry,_Ag:swL2QOS8021pDefaultPriorityIndex,'swL2QOS8021pDefaultPriority':swL2QOS8021pDefaultPriority,'swL2QOS8021pRadiusPriority':swL2QOS8021pRadiusPriority,'swL2IpMacBindingMgmt':swL2IpMacBindingMgmt,'swL2IpMacBindingPortTable':swL2IpMacBindingPortTable,'swL2IpMacBindingPortEntry':swL2IpMacBindingPortEntry,_Z:swL2IpMacBindingPortIndex,'swL2IpMacBindingPortState':swL2IpMacBindingPortState,'swL2IpMacBindingPortAllowZeroIp':swL2IpMacBindingPortAllowZeroIp,'swL2IpMacBindingPortForwardDhcpPkt':swL2IpMacBindingPortForwardDhcpPkt,'swL2IpMacBindingPortDHCPSnoopMaxEntry':swL2IpMacBindingPortDHCPSnoopMaxEntry,'swL2IpMacBindingPortDHCPSnoopEntryClearAction':swL2IpMacBindingPortDHCPSnoopEntryClearAction,'swL2IpMacBindingTable':swL2IpMacBindingTable,'swL2IpMacBindingEntry':swL2IpMacBindingEntry,_Aj:swL2IpMacBindingIpIndex,'swL2IpMacBindingMac':swL2IpMacBindingMac,'swL2IpMacBindingStatus':swL2IpMacBindingStatus,'swL2IpMacBindingPorts':swL2IpMacBindingPorts,'swL2IpMacBindingAction':swL2IpMacBindingAction,'swL2IpMacBindingMode':swL2IpMacBindingMode,'swL2IpMacBindingBlockedTable':swL2IpMacBindingBlockedTable,'swL2IpMacBindingBlockedEntry':swL2IpMacBindingBlockedEntry,_Ak:swL2IpMacBindingBlockedVID,_Al:swL2IpMacBindingBlockedMac,'swL2IpMacBindingBlockedVlanName':swL2IpMacBindingBlockedVlanName,'swL2IpMacBindingBlockedPort':swL2IpMacBindingBlockedPort,'swL2IpMacBindingBlockedType':swL2IpMacBindingBlockedType,'swL2IpMacBindingAllPortState':swL2IpMacBindingAllPortState,'swL2IpMacBindingTrapLogState':swL2IpMacBindingTrapLogState,'swL2IpMacBindingACLMode':swL2IpMacBindingACLMode,'swL2IpMacBindingDHCPSnoopState':swL2IpMacBindingDHCPSnoopState,'swL2IpMacBindingDHCPSnoopEntryClearAllState':swL2IpMacBindingDHCPSnoopEntryClearAllState,'swL2IpMacBindingDHCPSnoopTable':swL2IpMacBindingDHCPSnoopTable,'swL2IpMacBindingDHCPSnoopEntry':swL2IpMacBindingDHCPSnoopEntry,_Am:swL2IpMacBindingDHCPSnoopIpIndex,'swL2IpMacBindingDHCPSnoopMac':swL2IpMacBindingDHCPSnoopMac,'swL2IpMacBindingDHCPSnoopLeaseTime':swL2IpMacBindingDHCPSnoopLeaseTime,'swL2IpMacBindingDHCPSnoopPort':swL2IpMacBindingDHCPSnoopPort,'swL2IpMacBindingDHCPSnoopStatus':swL2IpMacBindingDHCPSnoopStatus,'swL2IpMacBindingPermitIPPoolTable':swL2IpMacBindingPermitIPPoolTable,'swL2IpMacBindingPermitIPPoolEntry':swL2IpMacBindingPermitIPPoolEntry,_An:swL2IpMacBindingPermitIPPoolStartIP,_Ao:swL2IpMacBindingPermitIPPoolEndIP,'swL2IpMacBindingPermitIPPoolPorts':swL2IpMacBindingPermitIPPoolPorts,'swL2IpMacBindingPermitIPPoolStatus':swL2IpMacBindingPermitIPPoolStatus,'swL2TrunkMgmt':swL2TrunkMgmt,'swL2TrunkMaxSupportedEntries':swL2TrunkMaxSupportedEntries,'swL2TrunkCurrentNumEntries':swL2TrunkCurrentNumEntries,'swL2TrunkCtrlTable':swL2TrunkCtrlTable,'swL2TrunkCtrlEntry':swL2TrunkCtrlEntry,_Ap:swL2TrunkIndex,'swL2TrunkName':swL2TrunkName,'swL2TrunkMasterPort':swL2TrunkMasterPort,'swL2TrunkMember':swL2TrunkMember,'swL2TrunkFloodingPort':swL2TrunkFloodingPort,'swL2TrunkType':swL2TrunkType,'swL2TrunkState':swL2TrunkState,'swL2TrunkAlgorithm':swL2TrunkAlgorithm,'swL2MirrorMgmt':swL2MirrorMgmt,'swL2MirrorLogicTargetPort':swL2MirrorLogicTargetPort,'swL2MirrorPortSourceIngress':swL2MirrorPortSourceIngress,'swL2MirrorPortSourceEgress':swL2MirrorPortSourceEgress,'swL2MirrorPortState':swL2MirrorPortState,'swL2IGMPMgmt':swL2IGMPMgmt,'swL2IGMPMaxSupportedVlans':swL2IGMPMaxSupportedVlans,'swL2IGMPCtrlTable':swL2IGMPCtrlTable,'swL2IGMPCtrlEntry':swL2IGMPCtrlEntry,_Aq:swL2IGMPCtrlVid,'swL2IGMPQueryInterval':swL2IGMPQueryInterval,'swL2IGMPMaxResponseTime':swL2IGMPMaxResponseTime,'swL2IGMPRobustness':swL2IGMPRobustness,'swL2IGMPLastMemberQueryInterval':swL2IGMPLastMemberQueryInterval,'swL2IGMPHostTimeout':swL2IGMPHostTimeout,'swL2IGMPRouteTimeout':swL2IGMPRouteTimeout,'swL2IGMPLeaveTimer':swL2IGMPLeaveTimer,'swL2IGMPQueryState':swL2IGMPQueryState,'swL2IGMPCurrentState':swL2IGMPCurrentState,'swL2IGMPCtrlState':swL2IGMPCtrlState,'swL2IGMPQueryInfoTable':swL2IGMPQueryInfoTable,'swL2IGMPQueryInfoEntry':swL2IGMPQueryInfoEntry,_Ar:swL2IGMPInfoVid,'swL2IGMPInfoQueryCount':swL2IGMPInfoQueryCount,'swL2IGMPInfoTxQueryCount':swL2IGMPInfoTxQueryCount,'swL2IGMPInfoTable':swL2IGMPInfoTable,'swL2IGMPInfoEntry':swL2IGMPInfoEntry,_As:swL2IGMPVid,_At:swL2IGMPGroupIpAddr,'swL2IGMPMacAddr':swL2IGMPMacAddr,'swL2IGMPPortMap':swL2IGMPPortMap,'swL2IGMPIpGroupReportCount':swL2IGMPIpGroupReportCount,'swL2IGMPMulticastVlanTable':swL2IGMPMulticastVlanTable,'swL2IGMPMulticastVlanEntry':swL2IGMPMulticastVlanEntry,_Au:swL2IGMPMulticastVlanid,'swL2IGMPMulticastVlanName':swL2IGMPMulticastVlanName,'swL2IGMPMulticastVlanSourcePort':swL2IGMPMulticastVlanSourcePort,'swL2IGMPMulticastVlanMemberPort':swL2IGMPMulticastVlanMemberPort,'swL2IGMPMulticastVlanRowStatus':swL2IGMPMulticastVlanRowStatus,'swL2IGMPMulticastVlanReplaceSourceIP':swL2IGMPMulticastVlanReplaceSourceIP,'swL2IGMPRouterPortTable':swL2IGMPRouterPortTable,'swL2IGMPRouterPortEntry':swL2IGMPRouterPortEntry,_Av:swL2IGMPRouterPortVlanid,'swL2IGMPRouterPortVlanName':swL2IGMPRouterPortVlanName,'swL2IGMPRouterPortStaticPortList':swL2IGMPRouterPortStaticPortList,'swL2IGMPRouterPortDynamicPortList':swL2IGMPRouterPortDynamicPortList,'swL2IGMPRouterPortForbiddenPortList':swL2IGMPRouterPortForbiddenPortList,'swL2DhcpRelayMgmt':swL2DhcpRelayMgmt,'swL2DhcpRelayState':swL2DhcpRelayState,'swL2DhcpRelayHopCount':swL2DhcpRelayHopCount,'swL2DhcpRelayTimeThreshold':swL2DhcpRelayTimeThreshold,'swL2DhcpRelayOption82State':swL2DhcpRelayOption82State,'swL2DhcpRelayOption82Check':swL2DhcpRelayOption82Check,'swL2DhcpRelayOption82Policy':swL2DhcpRelayOption82Policy,'swL2DhcpRelayCtrlTable':swL2DhcpRelayCtrlTable,'swL2DhcpRelayCtrlEntry':swL2DhcpRelayCtrlEntry,_Aw:swL2DhcpRelayCtrlInterfaceName,_Ax:swL2DhcpRelayCtrlServer,'swL2DhcpRelayCtrlState':swL2DhcpRelayCtrlState,'swL2LoopDetectMgmt':swL2LoopDetectMgmt,'swL2LoopDetectCtrl':swL2LoopDetectCtrl,'swL2LoopDetectAdminState':swL2LoopDetectAdminState,'swL2LoopDetectInterval':swL2LoopDetectInterval,'swL2LoopDetectRecoverTime':swL2LoopDetectRecoverTime,'swL2LoopDetectMode':swL2LoopDetectMode,'swL2LoopDetectPortMgmt':swL2LoopDetectPortMgmt,'swL2LoopDetectPortTable':swL2LoopDetectPortTable,'swL2LoopDetectPortEntry':swL2LoopDetectPortEntry,_N:swL2LoopDetectPortIndex,'swL2LoopDetectPortState':swL2LoopDetectPortState,'swL2LoopDetectPortLoopVLAN':swL2LoopDetectPortLoopVLAN,'swL2LoopDetectPortLoopStatus':swL2LoopDetectPortLoopStatus,'swL2TrafficSegMgmt':swL2TrafficSegMgmt,'swL2TrafficSegTable':swL2TrafficSegTable,'swL2TrafficSegEntry':swL2TrafficSegEntry,_Ay:swL2TrafficSegPort,'swL2TrafficSegForwardPorts':swL2TrafficSegForwardPorts,'swL2PortSecurityMgmt':swL2PortSecurityMgmt,'swL2PortSecurityControlTable':swL2PortSecurityControlTable,'swL2PortSecurityControlEntry':swL2PortSecurityControlEntry,_a:swL2PortSecurityPortIndex,'swL2PortSecurityMaxLernAddr':swL2PortSecurityMaxLernAddr,'swL2PortSecurityMode':swL2PortSecurityMode,'swL2PortSecurityAdmState':swL2PortSecurityAdmState,'swL2PortSecurityTrapLogState':swL2PortSecurityTrapLogState,'swL2MgmtMIBTraps':swL2MgmtMIBTraps,'swL2MgmtMIBTrapPrefix':swL2MgmtMIBTrapPrefix,'swL2macNotification':swL2macNotification,'swL2porttypechgNotification':swL2porttypechgNotification,'swPowerStatusChg':swPowerStatusChg,'swPowerFailure':swPowerFailure,'swPowerRecover':swPowerRecover,'swl2NotificationBidings':swl2NotificationBidings,_A_:swL2macNotifyInfo,'swl2NotifyPortSecurity':swl2NotifyPortSecurity,_B1:swL2PortSecurityViolationMac,'swL2PortSecurityViolationTrap':swL2PortSecurityViolationTrap,'swl2NotifyIpMacBinding':swl2NotifyIpMacBinding,_B2:swL2IpMacBindingViolationIP,_B3:swL2IpMacBindingViolationMac,'swL2IpMacBindingViolationTrap':swL2IpMacBindingViolationTrap,'swl2NotifyLoopDetect':swl2NotifyLoopDetect,_b:swL2VlanLoopDetectVID,'swL2PortLoopOccurred':swL2PortLoopOccurred,'swL2PortLoopRestart':swL2PortLoopRestart,'swL2VlanLoopOccurred':swL2VlanLoopOccurred,'swL2VlanLoopRestart':swL2VlanLoopRestart,'swL2DhcpLocalRelayMgmt':swL2DhcpLocalRelayMgmt,'swL2DhcpLocalRelayState':swL2DhcpLocalRelayState,'swL2DhcpLocalRelayVLANTable':swL2DhcpLocalRelayVLANTable,'swL2DhcpLocalRelayVLANEntry':swL2DhcpLocalRelayVLANEntry,_Az:swL2DhcpLocalRelayVLANID,'swL2DhcpLocalRelayVLANState':swL2DhcpLocalRelayVLANState})