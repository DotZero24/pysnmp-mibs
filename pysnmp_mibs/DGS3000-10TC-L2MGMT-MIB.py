_Aq='swL2PortSecurityViolationMac'
_Ap='swL2macNotifyInfo'
_Ao='accessible-for-notify'
_An='swL2MulticastFilterPortIndex'
_Am='filter-unregistered-groups'
_Al='forward-unregistered-groups'
_Ak='forward-all-groups'
_Aj='swL2MulticastFilterVid'
_Ai='swL2StpPort'
_Ah='swL2TrafficSegPort'
_Ag='swL2TrafficCtrlGroupIndex'
_Af='swL2IGMPSnoopingStaticGroupIPaddress'
_Ae='swL2IGMPSnoopingStaticGroupVID'
_Ad='swL2IGMPRouterIPAddress'
_Ac='swL2IGMPRouterIPAddressVid'
_Ab='swL2IGMPPortCounterInfoIndex'
_Aa='swL2IGMPVlanCounterInfoVid'
_AZ='swL2IGMPAccessAuthPort'
_AY='swIGMPSnoopingGroupSourceAddr'
_AX='swIGMPSnoopingGroupGroupAddr'
_AW='swIGMPSnoopingGroupVid'
_AV='swL2IGMPv3SourceIPAddr'
_AU='swL2IGMPMulticastVlanGroupToIp'
_AT='swL2IGMPMulticastVlanGroupFromIp'
_AS='swL2IGMPMulticastVlanGroupVid'
_AR='swL2IGMPMulticastVlanid'
_AQ='swL2IGMPRouterPortVlanid'
_AP='swL2IGMPInfoVid'
_AO='swL2MirrorGroupID'
_AN='swL2TrunkVLANPort'
_AM='swL2TrunkLACPPortIndex'
_AL='swL2TrunkIndex'
_AK='swL2DhcpRelayCtrlServer'
_AJ='swL2DhcpRelayCtrlInterfaceName'
_AI='swL2PortSecurityPortIndex'
_AH='swL2QOS8021pDefaultPriorityIndex'
_AG='swL2QOS8021pUserPriorityIndex'
_AF='weightfair'
_AE='roundrobin'
_AD='swL2QOSSchedulingClassIndex'
_AC='swL2QOSBandwidthPortIndex'
_AB='swL2MulticastFilterVIDMaxGroupVIDIndex'
_AA='swL2LimitedMulticastFilterVIDIndex'
_A9='swL2MulticastFilterPortMaxGroupPortIndex'
_A8='swL2LimitedMulticastFilterPortIndex'
_A7='swL2MulticastFilterToIp'
_A6='swL2MulticastFilterFromIp'
_A5='swL2MulticastFilterProfileIdIndex'
_A4='swL2MulticastFilterProfileIndex'
_A3='swL2DiffServTOSCtrlPortIndex'
_A2='swL2DiffServDSCPCtrlPortIndex'
_A1='swL2DiffServTypeCtrlPortIndex'
_A0='swL2PortJumboFrameCtrlPortIndex'
_z='swL2PortDropCounterPortIndex'
_y='swL2PortAutoNegInfoPortIndex'
_x='err-disabled'
_w='swL2PortErrPortIndex'
_v='swL2PortCounterCtrlPortIndex'
_u='swL2PortCableDiagnosisPairIndex'
_t='swL2PortCableDiagnosisPortIndex'
_s='swL2PortCtrlMediumType'
_r='swL2PortCtrlPortIndex'
_q='power-saving'
_p='ctp-lbd'
_o='stp-lbd'
_n='link-down'
_m='copper'
_l='swL2PortInfoMediumType'
_k='swL2PortInfoPortIndex'
_j='swL2VlanPrecedencePortIndex'
_i='swL2SubnetVLANIPMask'
_h='swL2SubnetVLANIPAddress'
_g='swL2VlanPortInfoVid'
_f='swL2VlanPortInfoPortIndex'
_e='swL2VlanIndex'
_d='swL2DevCtrlCFMPortIndex'
_c='active'
_b='swDevModuleInfoUnitID'
_a='Unsigned32'
_Z='swPortSecPortIndex'
_Y='PORT-SECURITY-MIB'
_X='swL2VlanLoopDetectVID'
_W='swL2IGMPGroupIpAddr'
_V='swL2IGMPVid'
_U='swL2IGMPCtrlVid'
_T='unknown'
_S='normal'
_R='OctetString'
_Q='disable'
_P='enable'
_O='not-accessible'
_N='start'
_M='none'
_L='swL2LoopDetectPortIndex'
_K='DisplayString'
_J='obsolete'
_I='read-create'
_H='other'
_G='enabled'
_F='disabled'
_E='DGS3000-10TC-L2MGMT-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AgentNotifyLevel,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','AgentNotifyLevel')
swPortSecPortIndex,=mibBuilder.importSymbols(_Y,_Z)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_a,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention','TruthValue')
dgs3000_10_tc,=mibBuilder.importSymbols('SWPRIMGMT-DGS3000-MIB','dgs3000-10-tc')
swL2MgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,11,133,1,1,2))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
class IANAifMauAutoNegCapBits(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('bOther',0),('b10baseT',1),('b10baseTFD',2),('b100baseT4',3),('b100baseTX',4),('b100baseTXFD',5),('b100baseT2',6),('b100baseT2FD',7),('bFdxPause',8),('bFdxAPause',9),('bFdxSPause',10),('bFdxBPause',11),('b1000baseX',12),('b1000baseXFD',13),('b1000baseT',14),('b1000baseTFD',15)))
_SwL2DevMgmt_ObjectIdentity=ObjectIdentity
swL2DevMgmt=_SwL2DevMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,1))
_SwL2DevInfo_ObjectIdentity=ObjectIdentity
swL2DevInfo=_SwL2DevInfo_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,1,1))
class _SwDevInfoTotalNumOfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwDevInfoTotalNumOfPort_Type.__name__=_B
_SwDevInfoTotalNumOfPort_Object=MibScalar
swDevInfoTotalNumOfPort=_SwDevInfoTotalNumOfPort_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,1,1),_SwDevInfoTotalNumOfPort_Type())
swDevInfoTotalNumOfPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevInfoTotalNumOfPort.setStatus(_A)
class _SwDevInfoNumOfPortInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwDevInfoNumOfPortInUse_Type.__name__=_B
_SwDevInfoNumOfPortInUse_Object=MibScalar
swDevInfoNumOfPortInUse=_SwDevInfoNumOfPortInUse_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,1,2),_SwDevInfoNumOfPortInUse_Type())
swDevInfoNumOfPortInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevInfoNumOfPortInUse.setStatus(_A)
_SwDevModuleInfoTable_Object=MibTable
swDevModuleInfoTable=_SwDevModuleInfoTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,1,3))
if mibBuilder.loadTexts:swDevModuleInfoTable.setStatus(_A)
_SwDevModuleInfoEntry_Object=MibTableRow
swDevModuleInfoEntry=_SwDevModuleInfoEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,1,3,1))
swDevModuleInfoEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:swDevModuleInfoEntry.setStatus(_A)
class _SwDevModuleInfoUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_SwDevModuleInfoUnitID_Type.__name__=_B
_SwDevModuleInfoUnitID_Object=MibTableColumn
swDevModuleInfoUnitID=_SwDevModuleInfoUnitID_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,1,3,1,1),_SwDevModuleInfoUnitID_Type())
swDevModuleInfoUnitID.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevModuleInfoUnitID.setStatus(_A)
class _SwDevModuleInfoModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwDevModuleInfoModuleName_Type.__name__=_K
_SwDevModuleInfoModuleName_Object=MibTableColumn
swDevModuleInfoModuleName=_SwDevModuleInfoModuleName_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,1,3,1,3),_SwDevModuleInfoModuleName_Type())
swDevModuleInfoModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevModuleInfoModuleName.setStatus(_A)
class _SwDevModuleInfoReversion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_SwDevModuleInfoReversion_Type.__name__=_K
_SwDevModuleInfoReversion_Object=MibTableColumn
swDevModuleInfoReversion=_SwDevModuleInfoReversion_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,1,3,1,4),_SwDevModuleInfoReversion_Type())
swDevModuleInfoReversion.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevModuleInfoReversion.setStatus(_A)
class _SwDevModuleInfoSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_SwDevModuleInfoSerial_Type.__name__=_K
_SwDevModuleInfoSerial_Object=MibTableColumn
swDevModuleInfoSerial=_SwDevModuleInfoSerial_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,1,3,1,5),_SwDevModuleInfoSerial_Type())
swDevModuleInfoSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevModuleInfoSerial.setStatus(_A)
class _SwDevModuleInfoDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwDevModuleInfoDescription_Type.__name__=_K
_SwDevModuleInfoDescription_Object=MibTableColumn
swDevModuleInfoDescription=_SwDevModuleInfoDescription_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,1,3,1,6),_SwDevModuleInfoDescription_Type())
swDevModuleInfoDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevModuleInfoDescription.setStatus(_A)
class _SwDevInfoFrontPanelLedStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwDevInfoFrontPanelLedStatus_Type.__name__=_R
_SwDevInfoFrontPanelLedStatus_Object=MibScalar
swDevInfoFrontPanelLedStatus=_SwDevInfoFrontPanelLedStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,1,4),_SwDevInfoFrontPanelLedStatus_Type())
swDevInfoFrontPanelLedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevInfoFrontPanelLedStatus.setStatus(_A)
_SwL2DevCtrl_ObjectIdentity=ObjectIdentity
swL2DevCtrl=_SwL2DevCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,1,2))
class _SwL2DevCtrlStpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DevCtrlStpState_Type.__name__=_B
_SwL2DevCtrlStpState_Object=MibScalar
swL2DevCtrlStpState=_SwL2DevCtrlStpState_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,1),_SwL2DevCtrlStpState_Type())
swL2DevCtrlStpState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlStpState.setStatus(_A)
class _SwL2DevCtrlIGMPSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DevCtrlIGMPSnooping_Type.__name__=_B
_SwL2DevCtrlIGMPSnooping_Object=MibScalar
swL2DevCtrlIGMPSnooping=_SwL2DevCtrlIGMPSnooping_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,2),_SwL2DevCtrlIGMPSnooping_Type())
swL2DevCtrlIGMPSnooping.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlIGMPSnooping.setStatus(_A)
class _SwL2DevCtrlIGMPSnoopingMcstRTOnly_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlIGMPSnoopingMcstRTOnly_Type.__name__=_B
_SwL2DevCtrlIGMPSnoopingMcstRTOnly_Object=MibScalar
swL2DevCtrlIGMPSnoopingMcstRTOnly=_SwL2DevCtrlIGMPSnoopingMcstRTOnly_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,3),_SwL2DevCtrlIGMPSnoopingMcstRTOnly_Type())
swL2DevCtrlIGMPSnoopingMcstRTOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlIGMPSnoopingMcstRTOnly.setStatus(_A)
class _SwL2DevCtrlRmonState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DevCtrlRmonState_Type.__name__=_B
_SwL2DevCtrlRmonState_Object=MibScalar
swL2DevCtrlRmonState=_SwL2DevCtrlRmonState_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,4),_SwL2DevCtrlRmonState_Type())
swL2DevCtrlRmonState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlRmonState.setStatus(_A)
class _SwL2DevCtrlSnmpTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlSnmpTrapState_Type.__name__=_B
_SwL2DevCtrlSnmpTrapState_Object=MibScalar
swL2DevCtrlSnmpTrapState=_SwL2DevCtrlSnmpTrapState_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,5),_SwL2DevCtrlSnmpTrapState_Type())
swL2DevCtrlSnmpTrapState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlSnmpTrapState.setStatus(_A)
class _SwL2DevCtrlCleanAllStatisticCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_c,2)))
_SwL2DevCtrlCleanAllStatisticCounter_Type.__name__=_B
_SwL2DevCtrlCleanAllStatisticCounter_Object=MibScalar
swL2DevCtrlCleanAllStatisticCounter=_SwL2DevCtrlCleanAllStatisticCounter_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,6),_SwL2DevCtrlCleanAllStatisticCounter_Type())
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlCleanAllStatisticCounter.setStatus(_A)
_SwL2DevCtrlVlanIdOfFDBTbl_Type=VlanId
_SwL2DevCtrlVlanIdOfFDBTbl_Object=MibScalar
swL2DevCtrlVlanIdOfFDBTbl=_SwL2DevCtrlVlanIdOfFDBTbl_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,7),_SwL2DevCtrlVlanIdOfFDBTbl_Type())
swL2DevCtrlVlanIdOfFDBTbl.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlVlanIdOfFDBTbl.setStatus(_A)
class _SwL2MACNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2MACNotifyState_Type.__name__=_B
_SwL2MACNotifyState_Object=MibScalar
swL2MACNotifyState=_SwL2MACNotifyState_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,8),_SwL2MACNotifyState_Type())
swL2MACNotifyState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MACNotifyState.setStatus(_A)
class _SwL2MACNotifyHistorySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_SwL2MACNotifyHistorySize_Type.__name__=_B
_SwL2MACNotifyHistorySize_Object=MibScalar
swL2MACNotifyHistorySize=_SwL2MACNotifyHistorySize_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,9),_SwL2MACNotifyHistorySize_Type())
swL2MACNotifyHistorySize.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MACNotifyHistorySize.setStatus(_A)
class _SwL2MACNotifyInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SwL2MACNotifyInterval_Type.__name__=_B
_SwL2MACNotifyInterval_Object=MibScalar
swL2MACNotifyInterval=_SwL2MACNotifyInterval_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,10),_SwL2MACNotifyInterval_Type())
swL2MACNotifyInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MACNotifyInterval.setStatus(_A)
class _SwL2DevCtrlAsymVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DevCtrlAsymVlanState_Type.__name__=_B
_SwL2DevCtrlAsymVlanState_Object=MibScalar
swL2DevCtrlAsymVlanState=_SwL2DevCtrlAsymVlanState_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,13),_SwL2DevCtrlAsymVlanState_Type())
swL2DevCtrlAsymVlanState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlAsymVlanState.setStatus(_A)
_SwL2DevCtrlTelnet_ObjectIdentity=ObjectIdentity
swL2DevCtrlTelnet=_SwL2DevCtrlTelnet_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,1,2,14))
class _SwL2DevCtrlTelnetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DevCtrlTelnetState_Type.__name__=_B
_SwL2DevCtrlTelnetState_Object=MibScalar
swL2DevCtrlTelnetState=_SwL2DevCtrlTelnetState_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,14,1),_SwL2DevCtrlTelnetState_Type())
swL2DevCtrlTelnetState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlTelnetState.setStatus(_A)
class _SwL2DevCtrlTelnetTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2DevCtrlTelnetTcpPort_Type.__name__=_B
_SwL2DevCtrlTelnetTcpPort_Object=MibScalar
swL2DevCtrlTelnetTcpPort=_SwL2DevCtrlTelnetTcpPort_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,14,2),_SwL2DevCtrlTelnetTcpPort_Type())
swL2DevCtrlTelnetTcpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlTelnetTcpPort.setStatus(_A)
_SwL2DevCtrlManagementVlanId_Type=VlanId
_SwL2DevCtrlManagementVlanId_Object=MibScalar
swL2DevCtrlManagementVlanId=_SwL2DevCtrlManagementVlanId_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,16),_SwL2DevCtrlManagementVlanId_Type())
swL2DevCtrlManagementVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlManagementVlanId.setStatus(_A)
_SwL2DevCtrlWeb_ObjectIdentity=ObjectIdentity
swL2DevCtrlWeb=_SwL2DevCtrlWeb_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,1,2,17))
class _SwL2DevCtrlWebState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlWebState_Type.__name__=_B
_SwL2DevCtrlWebState_Object=MibScalar
swL2DevCtrlWebState=_SwL2DevCtrlWebState_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,17,1),_SwL2DevCtrlWebState_Type())
swL2DevCtrlWebState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlWebState.setStatus(_A)
class _SwL2DevCtrlWebTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2DevCtrlWebTcpPort_Type.__name__=_B
_SwL2DevCtrlWebTcpPort_Object=MibScalar
swL2DevCtrlWebTcpPort=_SwL2DevCtrlWebTcpPort_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,17,2),_SwL2DevCtrlWebTcpPort_Type())
swL2DevCtrlWebTcpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlWebTcpPort.setStatus(_A)
class _SwL2DevCtrlLLDPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlLLDPState_Type.__name__=_B
_SwL2DevCtrlLLDPState_Object=MibScalar
swL2DevCtrlLLDPState=_SwL2DevCtrlLLDPState_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,18),_SwL2DevCtrlLLDPState_Type())
swL2DevCtrlLLDPState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlLLDPState.setStatus(_A)
class _SwL2DevCtrlLLDPForwardMessageState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlLLDPForwardMessageState_Type.__name__=_B
_SwL2DevCtrlLLDPForwardMessageState_Object=MibScalar
swL2DevCtrlLLDPForwardMessageState=_SwL2DevCtrlLLDPForwardMessageState_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,19),_SwL2DevCtrlLLDPForwardMessageState_Type())
swL2DevCtrlLLDPForwardMessageState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlLLDPForwardMessageState.setStatus(_A)
class _SwL2DevCtrlIpAutoconfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlIpAutoconfig_Type.__name__=_B
_SwL2DevCtrlIpAutoconfig_Object=MibScalar
swL2DevCtrlIpAutoconfig=_SwL2DevCtrlIpAutoconfig_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,20),_SwL2DevCtrlIpAutoconfig_Type())
swL2DevCtrlIpAutoconfig.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlIpAutoconfig.setStatus(_A)
_SwL2DevCtrlCFM_ObjectIdentity=ObjectIdentity
swL2DevCtrlCFM=_SwL2DevCtrlCFM_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,1,2,21))
class _SwL2DevCtrlCFMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlCFMState_Type.__name__=_B
_SwL2DevCtrlCFMState_Object=MibScalar
swL2DevCtrlCFMState=_SwL2DevCtrlCFMState_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,21,1),_SwL2DevCtrlCFMState_Type())
swL2DevCtrlCFMState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlCFMState.setStatus(_A)
_SwL2DevCtrlCFMPortTable_Object=MibTable
swL2DevCtrlCFMPortTable=_SwL2DevCtrlCFMPortTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,21,2))
if mibBuilder.loadTexts:swL2DevCtrlCFMPortTable.setStatus(_A)
_SwL2DevCtrlCFMPortEntry_Object=MibTableRow
swL2DevCtrlCFMPortEntry=_SwL2DevCtrlCFMPortEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,21,2,1))
swL2DevCtrlCFMPortEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:swL2DevCtrlCFMPortEntry.setStatus(_A)
_SwL2DevCtrlCFMPortIndex_Type=Integer32
_SwL2DevCtrlCFMPortIndex_Object=MibTableColumn
swL2DevCtrlCFMPortIndex=_SwL2DevCtrlCFMPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,21,2,1,1),_SwL2DevCtrlCFMPortIndex_Type())
swL2DevCtrlCFMPortIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:swL2DevCtrlCFMPortIndex.setStatus(_A)
class _SwL2DevCtrlCFMPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlCFMPortState_Type.__name__=_B
_SwL2DevCtrlCFMPortState_Object=MibTableColumn
swL2DevCtrlCFMPortState=_SwL2DevCtrlCFMPortState_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,21,2,1,2),_SwL2DevCtrlCFMPortState_Type())
swL2DevCtrlCFMPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlCFMPortState.setStatus(_A)
class _SwL2DevCtrlVLANTrunkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlVLANTrunkState_Type.__name__=_B
_SwL2DevCtrlVLANTrunkState_Object=MibScalar
swL2DevCtrlVLANTrunkState=_SwL2DevCtrlVLANTrunkState_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,2,22),_SwL2DevCtrlVLANTrunkState_Type())
swL2DevCtrlVLANTrunkState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlVLANTrunkState.setStatus(_A)
_SwL2DevAlarm_ObjectIdentity=ObjectIdentity
swL2DevAlarm=_SwL2DevAlarm_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,1,3))
class _SwL2DevAlarmNewRoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DevAlarmNewRoot_Type.__name__=_B
_SwL2DevAlarmNewRoot_Object=MibScalar
swL2DevAlarmNewRoot=_SwL2DevAlarmNewRoot_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,3,1),_SwL2DevAlarmNewRoot_Type())
swL2DevAlarmNewRoot.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevAlarmNewRoot.setStatus(_A)
class _SwL2DevAlarmTopologyChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DevAlarmTopologyChange_Type.__name__=_B
_SwL2DevAlarmTopologyChange_Object=MibScalar
swL2DevAlarmTopologyChange=_SwL2DevAlarmTopologyChange_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,3,2),_SwL2DevAlarmTopologyChange_Type())
swL2DevAlarmTopologyChange.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevAlarmTopologyChange.setStatus(_A)
class _SwL2DevAlarmLinkChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DevAlarmLinkChange_Type.__name__=_B
_SwL2DevAlarmLinkChange_Object=MibScalar
swL2DevAlarmLinkChange=_SwL2DevAlarmLinkChange_Object((1,3,6,1,4,1,171,11,133,1,1,2,1,3,3),_SwL2DevAlarmLinkChange_Type())
swL2DevAlarmLinkChange.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevAlarmLinkChange.setStatus(_A)
_SwL2VLANMgmt_ObjectIdentity=ObjectIdentity
swL2VLANMgmt=_SwL2VLANMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,2))
_SwL2VlanStaticTable_Object=MibTable
swL2VlanStaticTable=_SwL2VlanStaticTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,1))
if mibBuilder.loadTexts:swL2VlanStaticTable.setStatus(_A)
_SwL2VlanStaticEntry_Object=MibTableRow
swL2VlanStaticEntry=_SwL2VlanStaticEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,1,1))
swL2VlanStaticEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:swL2VlanStaticEntry.setStatus(_A)
_SwL2VlanIndex_Type=VlanId
_SwL2VlanIndex_Object=MibTableColumn
swL2VlanIndex=_SwL2VlanIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,1,1,1),_SwL2VlanIndex_Type())
swL2VlanIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:swL2VlanIndex.setStatus(_A)
class _SwL2VLANAdvertisement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2VLANAdvertisement_Type.__name__=_B
_SwL2VLANAdvertisement_Object=MibTableColumn
swL2VLANAdvertisement=_SwL2VLANAdvertisement_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,1,1,2),_SwL2VLANAdvertisement_Type())
swL2VLANAdvertisement.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VLANAdvertisement.setStatus(_A)
class _SwL2PVIDAutoAssignmentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2PVIDAutoAssignmentState_Type.__name__=_B
_SwL2PVIDAutoAssignmentState_Object=MibScalar
swL2PVIDAutoAssignmentState=_SwL2PVIDAutoAssignmentState_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,2),_SwL2PVIDAutoAssignmentState_Type())
swL2PVIDAutoAssignmentState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PVIDAutoAssignmentState.setStatus(_A)
_SwL2VlanPortInfoTable_Object=MibTable
swL2VlanPortInfoTable=_SwL2VlanPortInfoTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,3))
if mibBuilder.loadTexts:swL2VlanPortInfoTable.setStatus(_A)
_SwL2VlanPortInfoEntry_Object=MibTableRow
swL2VlanPortInfoEntry=_SwL2VlanPortInfoEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,3,1))
swL2VlanPortInfoEntry.setIndexNames((0,_E,_f),(0,_E,_g))
if mibBuilder.loadTexts:swL2VlanPortInfoEntry.setStatus(_A)
class _SwL2VlanPortInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2VlanPortInfoPortIndex_Type.__name__=_B
_SwL2VlanPortInfoPortIndex_Object=MibTableColumn
swL2VlanPortInfoPortIndex=_SwL2VlanPortInfoPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,3,1,1),_SwL2VlanPortInfoPortIndex_Type())
swL2VlanPortInfoPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanPortInfoPortIndex.setStatus(_A)
_SwL2VlanPortInfoVid_Type=VlanId
_SwL2VlanPortInfoVid_Object=MibTableColumn
swL2VlanPortInfoVid=_SwL2VlanPortInfoVid_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,3,1,2),_SwL2VlanPortInfoVid_Type())
swL2VlanPortInfoVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanPortInfoVid.setStatus(_A)
class _SwL2VlanPortInfoPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('untagged',2),('tagged',3),('dynamic',4),('forbidden',5)))
_SwL2VlanPortInfoPortRole_Type.__name__=_B
_SwL2VlanPortInfoPortRole_Object=MibTableColumn
swL2VlanPortInfoPortRole=_SwL2VlanPortInfoPortRole_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,3,1,3),_SwL2VlanPortInfoPortRole_Type())
swL2VlanPortInfoPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanPortInfoPortRole.setStatus(_A)
_SwL2SubnetVLANTable_Object=MibTable
swL2SubnetVLANTable=_SwL2SubnetVLANTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,4))
if mibBuilder.loadTexts:swL2SubnetVLANTable.setStatus(_A)
_SwL2SubnetVLANEntry_Object=MibTableRow
swL2SubnetVLANEntry=_SwL2SubnetVLANEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,4,1))
swL2SubnetVLANEntry.setIndexNames((0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:swL2SubnetVLANEntry.setStatus(_A)
_SwL2SubnetVLANIPAddress_Type=IpAddress
_SwL2SubnetVLANIPAddress_Object=MibTableColumn
swL2SubnetVLANIPAddress=_SwL2SubnetVLANIPAddress_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,4,1,1),_SwL2SubnetVLANIPAddress_Type())
swL2SubnetVLANIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2SubnetVLANIPAddress.setStatus(_A)
_SwL2SubnetVLANIPMask_Type=IpAddress
_SwL2SubnetVLANIPMask_Object=MibTableColumn
swL2SubnetVLANIPMask=_SwL2SubnetVLANIPMask_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,4,1,2),_SwL2SubnetVLANIPMask_Type())
swL2SubnetVLANIPMask.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2SubnetVLANIPMask.setStatus(_A)
_SwL2SubnetVLANID_Type=VlanId
_SwL2SubnetVLANID_Object=MibTableColumn
swL2SubnetVLANID=_SwL2SubnetVLANID_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,4,1,3),_SwL2SubnetVLANID_Type())
swL2SubnetVLANID.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2SubnetVLANID.setStatus(_A)
class _SwL2SubnetVLANPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2SubnetVLANPriority_Type.__name__=_B
_SwL2SubnetVLANPriority_Object=MibTableColumn
swL2SubnetVLANPriority=_SwL2SubnetVLANPriority_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,4,1,4),_SwL2SubnetVLANPriority_Type())
swL2SubnetVLANPriority.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2SubnetVLANPriority.setStatus(_A)
_SwL2SubnetVLANRowStatus_Type=RowStatus
_SwL2SubnetVLANRowStatus_Object=MibTableColumn
swL2SubnetVLANRowStatus=_SwL2SubnetVLANRowStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,4,1,5),_SwL2SubnetVLANRowStatus_Type())
swL2SubnetVLANRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2SubnetVLANRowStatus.setStatus(_A)
_SwL2VlanPrecedenceTable_Object=MibTable
swL2VlanPrecedenceTable=_SwL2VlanPrecedenceTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,5))
if mibBuilder.loadTexts:swL2VlanPrecedenceTable.setStatus(_A)
_SwL2VlanPrecedenceEntry_Object=MibTableRow
swL2VlanPrecedenceEntry=_SwL2VlanPrecedenceEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,5,1))
swL2VlanPrecedenceEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:swL2VlanPrecedenceEntry.setStatus(_A)
class _SwL2VlanPrecedencePortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2VlanPrecedencePortIndex_Type.__name__=_B
_SwL2VlanPrecedencePortIndex_Object=MibTableColumn
swL2VlanPrecedencePortIndex=_SwL2VlanPrecedencePortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,5,1,1),_SwL2VlanPrecedencePortIndex_Type())
swL2VlanPrecedencePortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanPrecedencePortIndex.setStatus(_A)
class _SwL2VlanPrecedenceClassification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mac-based',1),('subnet-based',2)))
_SwL2VlanPrecedenceClassification_Type.__name__=_B
_SwL2VlanPrecedenceClassification_Object=MibTableColumn
swL2VlanPrecedenceClassification=_SwL2VlanPrecedenceClassification_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,5,1,2),_SwL2VlanPrecedenceClassification_Type())
swL2VlanPrecedenceClassification.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanPrecedenceClassification.setStatus(_A)
class _SwL2NniGvrpBpduAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot1d',1),('dot1ad',2)))
_SwL2NniGvrpBpduAddress_Type.__name__=_B
_SwL2NniGvrpBpduAddress_Object=MibScalar
swL2NniGvrpBpduAddress=_SwL2NniGvrpBpduAddress_Object((1,3,6,1,4,1,171,11,133,1,1,2,2,6),_SwL2NniGvrpBpduAddress_Type())
swL2NniGvrpBpduAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2NniGvrpBpduAddress.setStatus(_A)
_SwL2PortMgmt_ObjectIdentity=ObjectIdentity
swL2PortMgmt=_SwL2PortMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,3))
_SwL2PortInfoTable_Object=MibTable
swL2PortInfoTable=_SwL2PortInfoTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,1))
if mibBuilder.loadTexts:swL2PortInfoTable.setStatus(_A)
_SwL2PortInfoEntry_Object=MibTableRow
swL2PortInfoEntry=_SwL2PortInfoEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,1,1))
swL2PortInfoEntry.setIndexNames((0,_E,_k),(0,_E,_l))
if mibBuilder.loadTexts:swL2PortInfoEntry.setStatus(_A)
class _SwL2PortInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortInfoPortIndex_Type.__name__=_B
_SwL2PortInfoPortIndex_Object=MibTableColumn
swL2PortInfoPortIndex=_SwL2PortInfoPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,1,1,1),_SwL2PortInfoPortIndex_Type())
swL2PortInfoPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortInfoPortIndex.setStatus(_A)
class _SwL2PortInfoMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_m,1),('fiber',2)))
_SwL2PortInfoMediumType_Type.__name__=_B
_SwL2PortInfoMediumType_Object=MibTableColumn
swL2PortInfoMediumType=_SwL2PortInfoMediumType_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,1,1,2),_SwL2PortInfoMediumType_Type())
swL2PortInfoMediumType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortInfoMediumType.setStatus(_A)
class _SwL2PortInfoUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortInfoUnitID_Type.__name__=_B
_SwL2PortInfoUnitID_Object=MibTableColumn
swL2PortInfoUnitID=_SwL2PortInfoUnitID_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,1,1,3),_SwL2PortInfoUnitID_Type())
swL2PortInfoUnitID.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortInfoUnitID.setStatus(_A)
class _SwL2PortInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*(('portType-100Base-TX',1),('portType-100Base-FX',2),('portType-100Base-FL',3),('portType-1000Base-TX',4),('portType-1000Base-SX',5),('portType-1000Base-LX',6),('portType-1000Base-SX-GBIC',7),('portType-1000Base-LX-GBIC',8),('portType-1000Base-TX-GBIC',9),('portType-1000Base-1394',10),('portType-1000Base-TX-GBIC-COMBO',11),('portType-1000Base-none-GBIC',12),('portType-1000Base-SX-MGBIC',13),('portType-1000Base-LX-MGBIC',14),('portType-1000Base-TX-MGBIC',15),('portType-1000Base-none-MGBIC',16),('portType-SIO',17),('portType-10G',18),('portType-10G-xenpak-1310nm',19),('portType-10G-xenpak-850nm',20),('portType-10G-xenpak-empty',21),('portType-10G-xfp-1310nm',22),('portType-10G-xfp-850nm',23),('portType-10G-xfp-empty',24),('portType-none',25)))
_SwL2PortInfoType_Type.__name__=_B
_SwL2PortInfoType_Object=MibTableColumn
swL2PortInfoType=_SwL2PortInfoType_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,1,1,4),_SwL2PortInfoType_Type())
swL2PortInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortInfoType.setStatus(_A)
class _SwL2PortInfoLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('link-pass',2),('link-fail',3)))
_SwL2PortInfoLinkStatus_Type.__name__=_B
_SwL2PortInfoLinkStatus_Object=MibTableColumn
swL2PortInfoLinkStatus=_SwL2PortInfoLinkStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,1,1,5),_SwL2PortInfoLinkStatus_Type())
swL2PortInfoLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortInfoLinkStatus.setStatus(_A)
class _SwL2PortInfoNwayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_H,0),('empty',1),(_n,2),('half-10Mbps',3),('full-10Mbps',4),('half-100Mbps',5),('full-100Mbps',6),('half-1Gigabps',7),('full-1Gigabps',8),('full-10Gigabps',9)))
_SwL2PortInfoNwayStatus_Type.__name__=_B
_SwL2PortInfoNwayStatus_Object=MibTableColumn
swL2PortInfoNwayStatus=_SwL2PortInfoNwayStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,1,1,6),_SwL2PortInfoNwayStatus_Type())
swL2PortInfoNwayStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortInfoNwayStatus.setStatus(_A)
class _SwL2PortInfoModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*((_M,0),('moduleType-COMBO',1),('moduleType-1394',2),('moduleType-1000T',3),('moduleType-MGBIC',4),('moduleType-1P-SC-SX',5),('moduleType-2P-SC-SX',6),('moduleType-1P-SC-LX',7),('moduleType-2P-SC-LX',8),('moduleType-1P-TX',9),('moduleType-2P-TX',10),('moduleType-1P-MTRJ-SX',11),('moduleType-2P-MTRJ-SX',12),('moduleType-1P-MTRJ-LX',13),('moduleType-2P-MTRJ-LX',14),('moduleType-1P-GBIC',15),('moduleType-2P-GBIC',16),('moduleType-1P-GBIC-1P-TX',17),('moduleType-1P-GBIC-1P-STACK',18),('moduleType-2P-STACK',19),('moduleType-2P-100FX',20),('moduleType-1P-100FX',21),('moduleType-2P-100FX-NEW',22),('moduleType-1P-100FL',23),('moduleType-2P-100FL',24),('moduleType-2P-100TX',25),('moduleType-BaseModule-24PORT',26)))
_SwL2PortInfoModuleType_Type.__name__=_B
_SwL2PortInfoModuleType_Object=MibTableColumn
swL2PortInfoModuleType=_SwL2PortInfoModuleType_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,1,1,7),_SwL2PortInfoModuleType_Type())
swL2PortInfoModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortInfoModuleType.setStatus(_A)
class _SwL2PortInfoErrorDisabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_M,0),('storm',1),(_o,2),('unknow',3),(_p,4),('ddm',5),('bpdu-protection',6),(_q,7),('duld',8)))
_SwL2PortInfoErrorDisabled_Type.__name__=_B
_SwL2PortInfoErrorDisabled_Object=MibTableColumn
swL2PortInfoErrorDisabled=_SwL2PortInfoErrorDisabled_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,1,1,8),_SwL2PortInfoErrorDisabled_Type())
swL2PortInfoErrorDisabled.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortInfoErrorDisabled.setStatus(_A)
_SwL2PortCtrlTable_Object=MibTable
swL2PortCtrlTable=_SwL2PortCtrlTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,2))
if mibBuilder.loadTexts:swL2PortCtrlTable.setStatus(_A)
_SwL2PortCtrlEntry_Object=MibTableRow
swL2PortCtrlEntry=_SwL2PortCtrlEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,2,1))
swL2PortCtrlEntry.setIndexNames((0,_E,_r),(0,_E,_s))
if mibBuilder.loadTexts:swL2PortCtrlEntry.setStatus(_A)
class _SwL2PortCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortCtrlPortIndex_Type.__name__=_B
_SwL2PortCtrlPortIndex_Object=MibTableColumn
swL2PortCtrlPortIndex=_SwL2PortCtrlPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,2,1,1),_SwL2PortCtrlPortIndex_Type())
swL2PortCtrlPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlPortIndex.setStatus(_A)
class _SwL2PortCtrlMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_m,1),('fiber',2)))
_SwL2PortCtrlMediumType_Type.__name__=_B
_SwL2PortCtrlMediumType_Object=MibTableColumn
swL2PortCtrlMediumType=_SwL2PortCtrlMediumType_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,2,1,2),_SwL2PortCtrlMediumType_Type())
swL2PortCtrlMediumType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlMediumType.setStatus(_A)
class _SwL2PortCtrlUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortCtrlUnitIndex_Type.__name__=_B
_SwL2PortCtrlUnitIndex_Object=MibTableColumn
swL2PortCtrlUnitIndex=_SwL2PortCtrlUnitIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,2,1,3),_SwL2PortCtrlUnitIndex_Type())
swL2PortCtrlUnitIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlUnitIndex.setStatus(_A)
class _SwL2PortCtrlAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2PortCtrlAdminState_Type.__name__=_B
_SwL2PortCtrlAdminState_Object=MibTableColumn
swL2PortCtrlAdminState=_SwL2PortCtrlAdminState_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,2,1,4),_SwL2PortCtrlAdminState_Type())
swL2PortCtrlAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlAdminState.setStatus(_A)
class _SwL2PortCtrlNwayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_H,1),('nway-enabled',2),('nway-disabled-10Mbps-Half',3),('nway-disabled-10Mbps-Full',4),('nway-disabled-100Mbps-Half',5),('nway-disabled-100Mbps-Full',6),('nway-disabled-1Gigabps-Half',7),('nway-disabled-1Gigabps-Full',8),('nway-disabled-1Gigabps-Full-master',9),('nway-disabled-1Gigabps-Full-slave',10)))
_SwL2PortCtrlNwayState_Type.__name__=_B
_SwL2PortCtrlNwayState_Object=MibTableColumn
swL2PortCtrlNwayState=_SwL2PortCtrlNwayState_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,2,1,5),_SwL2PortCtrlNwayState_Type())
swL2PortCtrlNwayState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlNwayState.setStatus(_A)
class _SwL2PortCtrlFlowCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2PortCtrlFlowCtrlState_Type.__name__=_B
_SwL2PortCtrlFlowCtrlState_Object=MibTableColumn
swL2PortCtrlFlowCtrlState=_SwL2PortCtrlFlowCtrlState_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,2,1,6),_SwL2PortCtrlFlowCtrlState_Type())
swL2PortCtrlFlowCtrlState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlFlowCtrlState.setStatus(_A)
class _SwL2PortCtrlLearningState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2PortCtrlLearningState_Type.__name__=_B
_SwL2PortCtrlLearningState_Object=MibTableColumn
swL2PortCtrlLearningState=_SwL2PortCtrlLearningState_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,2,1,7),_SwL2PortCtrlLearningState_Type())
swL2PortCtrlLearningState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlLearningState.setStatus(_A)
class _SwL2PortCtrlMACNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2PortCtrlMACNotifyState_Type.__name__=_B
_SwL2PortCtrlMACNotifyState_Object=MibTableColumn
swL2PortCtrlMACNotifyState=_SwL2PortCtrlMACNotifyState_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,2,1,8),_SwL2PortCtrlMACNotifyState_Type())
swL2PortCtrlMACNotifyState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlMACNotifyState.setStatus(_A)
class _SwL2PortCtrlMDIXState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),(_S,2),('cross',3)))
_SwL2PortCtrlMDIXState_Type.__name__=_B
_SwL2PortCtrlMDIXState_Object=MibTableColumn
swL2PortCtrlMDIXState=_SwL2PortCtrlMDIXState_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,2,1,10),_SwL2PortCtrlMDIXState_Type())
swL2PortCtrlMDIXState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlMDIXState.setStatus(_A)
class _SwL2PortCtrlAutoNegRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('restart',1),('norestart',2)))
_SwL2PortCtrlAutoNegRestart_Type.__name__=_B
_SwL2PortCtrlAutoNegRestart_Object=MibTableColumn
swL2PortCtrlAutoNegRestart=_SwL2PortCtrlAutoNegRestart_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,2,1,11),_SwL2PortCtrlAutoNegRestart_Type())
swL2PortCtrlAutoNegRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlAutoNegRestart.setStatus(_A)
_SwL2PortCtrlAutoNegCapAdvertisedBits_Type=IANAifMauAutoNegCapBits
_SwL2PortCtrlAutoNegCapAdvertisedBits_Object=MibTableColumn
swL2PortCtrlAutoNegCapAdvertisedBits=_SwL2PortCtrlAutoNegCapAdvertisedBits_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,2,1,12),_SwL2PortCtrlAutoNegCapAdvertisedBits_Type())
swL2PortCtrlAutoNegCapAdvertisedBits.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlAutoNegCapAdvertisedBits.setStatus(_A)
class _SwL2PortCtrlJumboFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2PortCtrlJumboFrame_Type.__name__=_B
_SwL2PortCtrlJumboFrame_Object=MibScalar
swL2PortCtrlJumboFrame=_SwL2PortCtrlJumboFrame_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,3),_SwL2PortCtrlJumboFrame_Type())
swL2PortCtrlJumboFrame.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlJumboFrame.setStatus(_A)
_SwL2PortCtrlJumboFrameMaxSize_Type=Integer32
_SwL2PortCtrlJumboFrameMaxSize_Object=MibScalar
swL2PortCtrlJumboFrameMaxSize=_SwL2PortCtrlJumboFrameMaxSize_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,4),_SwL2PortCtrlJumboFrameMaxSize_Type())
swL2PortCtrlJumboFrameMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlJumboFrameMaxSize.setStatus(_A)
_SwL2PortCableDiagnosisTable_Object=MibTable
swL2PortCableDiagnosisTable=_SwL2PortCableDiagnosisTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,5))
if mibBuilder.loadTexts:swL2PortCableDiagnosisTable.setStatus(_A)
_SwL2PortCableDiagnosisEntry_Object=MibTableRow
swL2PortCableDiagnosisEntry=_SwL2PortCableDiagnosisEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,5,1))
swL2PortCableDiagnosisEntry.setIndexNames((0,_E,_t),(0,_E,_u))
if mibBuilder.loadTexts:swL2PortCableDiagnosisEntry.setStatus(_A)
class _SwL2PortCableDiagnosisPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortCableDiagnosisPortIndex_Type.__name__=_B
_SwL2PortCableDiagnosisPortIndex_Object=MibTableColumn
swL2PortCableDiagnosisPortIndex=_SwL2PortCableDiagnosisPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,5,1,1),_SwL2PortCableDiagnosisPortIndex_Type())
swL2PortCableDiagnosisPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCableDiagnosisPortIndex.setStatus(_A)
class _SwL2PortCableDiagnosisPairIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_SwL2PortCableDiagnosisPairIndex_Type.__name__=_B
_SwL2PortCableDiagnosisPairIndex_Object=MibTableColumn
swL2PortCableDiagnosisPairIndex=_SwL2PortCableDiagnosisPairIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,5,1,2),_SwL2PortCableDiagnosisPairIndex_Type())
swL2PortCableDiagnosisPairIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCableDiagnosisPairIndex.setStatus(_A)
class _SwL2PortCableDiagnosisCableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('ok',0),('open',1),('short',2),('open-short',3),('not-support',4),(_T,5)))
_SwL2PortCableDiagnosisCableStatus_Type.__name__=_B
_SwL2PortCableDiagnosisCableStatus_Object=MibTableColumn
swL2PortCableDiagnosisCableStatus=_SwL2PortCableDiagnosisCableStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,5,1,3),_SwL2PortCableDiagnosisCableStatus_Type())
swL2PortCableDiagnosisCableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCableDiagnosisCableStatus.setStatus(_A)
class _SwL2PortCableDiagnosisPairStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('ok',0),('open',1),('short',2),('fail',3),('not-supported',4),(_T,5)))
_SwL2PortCableDiagnosisPairStatus_Type.__name__=_B
_SwL2PortCableDiagnosisPairStatus_Object=MibTableColumn
swL2PortCableDiagnosisPairStatus=_SwL2PortCableDiagnosisPairStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,5,1,4),_SwL2PortCableDiagnosisPairStatus_Type())
swL2PortCableDiagnosisPairStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCableDiagnosisPairStatus.setStatus(_A)
_SwL2PortCableDiagnosisPairLength_Type=Integer32
_SwL2PortCableDiagnosisPairLength_Object=MibTableColumn
swL2PortCableDiagnosisPairLength=_SwL2PortCableDiagnosisPairLength_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,5,1,5),_SwL2PortCableDiagnosisPairLength_Type())
swL2PortCableDiagnosisPairLength.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCableDiagnosisPairLength.setStatus(_A)
_SwL2PortCableDiagnosisPairLengthInaccuracy_Type=Integer32
_SwL2PortCableDiagnosisPairLengthInaccuracy_Object=MibTableColumn
swL2PortCableDiagnosisPairLengthInaccuracy=_SwL2PortCableDiagnosisPairLengthInaccuracy_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,5,1,6),_SwL2PortCableDiagnosisPairLengthInaccuracy_Type())
swL2PortCableDiagnosisPairLengthInaccuracy.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCableDiagnosisPairLengthInaccuracy.setStatus(_A)
_SwL2PortCounterCtrlTable_Object=MibTable
swL2PortCounterCtrlTable=_SwL2PortCounterCtrlTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,6))
if mibBuilder.loadTexts:swL2PortCounterCtrlTable.setStatus(_A)
_SwL2PortCounterCtrlEntry_Object=MibTableRow
swL2PortCounterCtrlEntry=_SwL2PortCounterCtrlEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,6,1))
swL2PortCounterCtrlEntry.setIndexNames((0,_E,_v))
if mibBuilder.loadTexts:swL2PortCounterCtrlEntry.setStatus(_A)
class _SwL2PortCounterCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortCounterCtrlPortIndex_Type.__name__=_B
_SwL2PortCounterCtrlPortIndex_Object=MibTableColumn
swL2PortCounterCtrlPortIndex=_SwL2PortCounterCtrlPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,6,1,1),_SwL2PortCounterCtrlPortIndex_Type())
swL2PortCounterCtrlPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCounterCtrlPortIndex.setStatus(_A)
class _SwL2PortCounterClearCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_N,2)))
_SwL2PortCounterClearCtrl_Type.__name__=_B
_SwL2PortCounterClearCtrl_Object=MibTableColumn
swL2PortCounterClearCtrl=_SwL2PortCounterClearCtrl_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,6,1,2),_SwL2PortCounterClearCtrl_Type())
swL2PortCounterClearCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCounterClearCtrl.setStatus(_A)
_SwL2PortErrTable_Object=MibTable
swL2PortErrTable=_SwL2PortErrTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,7))
if mibBuilder.loadTexts:swL2PortErrTable.setStatus(_A)
_SwL2PortErrEntry_Object=MibTableRow
swL2PortErrEntry=_SwL2PortErrEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,7,1))
swL2PortErrEntry.setIndexNames((0,_E,_w))
if mibBuilder.loadTexts:swL2PortErrEntry.setStatus(_A)
class _SwL2PortErrPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortErrPortIndex_Type.__name__=_B
_SwL2PortErrPortIndex_Object=MibTableColumn
swL2PortErrPortIndex=_SwL2PortErrPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,7,1,1),_SwL2PortErrPortIndex_Type())
swL2PortErrPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortErrPortIndex.setStatus(_A)
class _SwL2PortErrPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2PortErrPortState_Type.__name__=_B
_SwL2PortErrPortState_Object=MibTableColumn
swL2PortErrPortState=_SwL2PortErrPortState_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,7,1,2),_SwL2PortErrPortState_Type())
swL2PortErrPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortErrPortState.setStatus(_A)
class _SwL2PortErrPortConnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_x,2)))
_SwL2PortErrPortConnStatus_Type.__name__=_B
_SwL2PortErrPortConnStatus_Object=MibTableColumn
swL2PortErrPortConnStatus=_SwL2PortErrPortConnStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,7,1,3),_SwL2PortErrPortConnStatus_Type())
swL2PortErrPortConnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortErrPortConnStatus.setStatus(_A)
class _SwL2PortErrPortReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_T,0),(_o,1),('storm-control',2),(_p,3),('ddm',4),('bpdu_protection',5),(_q,6),('duld',7)))
_SwL2PortErrPortReason_Type.__name__=_B
_SwL2PortErrPortReason_Object=MibTableColumn
swL2PortErrPortReason=_SwL2PortErrPortReason_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,7,1,4),_SwL2PortErrPortReason_Type())
swL2PortErrPortReason.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortErrPortReason.setStatus(_A)
_SwL2PortAutoNegInfoTable_Object=MibTable
swL2PortAutoNegInfoTable=_SwL2PortAutoNegInfoTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,8))
if mibBuilder.loadTexts:swL2PortAutoNegInfoTable.setStatus(_A)
_SwL2PortAutoNegInfoEntry_Object=MibTableRow
swL2PortAutoNegInfoEntry=_SwL2PortAutoNegInfoEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,8,1))
swL2PortAutoNegInfoEntry.setIndexNames((0,_E,_y))
if mibBuilder.loadTexts:swL2PortAutoNegInfoEntry.setStatus(_A)
class _SwL2PortAutoNegInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortAutoNegInfoPortIndex_Type.__name__=_B
_SwL2PortAutoNegInfoPortIndex_Object=MibTableColumn
swL2PortAutoNegInfoPortIndex=_SwL2PortAutoNegInfoPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,8,1,1),_SwL2PortAutoNegInfoPortIndex_Type())
swL2PortAutoNegInfoPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortAutoNegInfoPortIndex.setStatus(_A)
class _SwL2PortAutoNegInfoAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2PortAutoNegInfoAdminStatus_Type.__name__=_B
_SwL2PortAutoNegInfoAdminStatus_Object=MibTableColumn
swL2PortAutoNegInfoAdminStatus=_SwL2PortAutoNegInfoAdminStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,8,1,2),_SwL2PortAutoNegInfoAdminStatus_Type())
swL2PortAutoNegInfoAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortAutoNegInfoAdminStatus.setStatus(_A)
_SwL2PortAutoNegInfoCapabilityBits_Type=IANAifMauAutoNegCapBits
_SwL2PortAutoNegInfoCapabilityBits_Object=MibTableColumn
swL2PortAutoNegInfoCapabilityBits=_SwL2PortAutoNegInfoCapabilityBits_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,8,1,3),_SwL2PortAutoNegInfoCapabilityBits_Type())
swL2PortAutoNegInfoCapabilityBits.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortAutoNegInfoCapabilityBits.setStatus(_A)
_SwL2PortAutoNegInfoCapAdvertisedBits_Type=IANAifMauAutoNegCapBits
_SwL2PortAutoNegInfoCapAdvertisedBits_Object=MibTableColumn
swL2PortAutoNegInfoCapAdvertisedBits=_SwL2PortAutoNegInfoCapAdvertisedBits_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,8,1,4),_SwL2PortAutoNegInfoCapAdvertisedBits_Type())
swL2PortAutoNegInfoCapAdvertisedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortAutoNegInfoCapAdvertisedBits.setStatus(_A)
_SwL2PortAutoNegInfoCapReceivedBits_Type=IANAifMauAutoNegCapBits
_SwL2PortAutoNegInfoCapReceivedBits_Object=MibTableColumn
swL2PortAutoNegInfoCapReceivedBits=_SwL2PortAutoNegInfoCapReceivedBits_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,8,1,5),_SwL2PortAutoNegInfoCapReceivedBits_Type())
swL2PortAutoNegInfoCapReceivedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortAutoNegInfoCapReceivedBits.setStatus(_A)
_SwL2PortDropCounterTable_Object=MibTable
swL2PortDropCounterTable=_SwL2PortDropCounterTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,9))
if mibBuilder.loadTexts:swL2PortDropCounterTable.setStatus(_A)
_SwL2PortDropCounterEntry_Object=MibTableRow
swL2PortDropCounterEntry=_SwL2PortDropCounterEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,9,1))
swL2PortDropCounterEntry.setIndexNames((0,_E,_z))
if mibBuilder.loadTexts:swL2PortDropCounterEntry.setStatus(_A)
class _SwL2PortDropCounterPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortDropCounterPortIndex_Type.__name__=_B
_SwL2PortDropCounterPortIndex_Object=MibTableColumn
swL2PortDropCounterPortIndex=_SwL2PortDropCounterPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,9,1,1),_SwL2PortDropCounterPortIndex_Type())
swL2PortDropCounterPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortDropCounterPortIndex.setStatus(_A)
_SwL2PortBufferFullDrops_Type=Counter32
_SwL2PortBufferFullDrops_Object=MibTableColumn
swL2PortBufferFullDrops=_SwL2PortBufferFullDrops_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,9,1,2),_SwL2PortBufferFullDrops_Type())
swL2PortBufferFullDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortBufferFullDrops.setStatus(_A)
_SwL2PortACLDrops_Type=Counter32
_SwL2PortACLDrops_Object=MibTableColumn
swL2PortACLDrops=_SwL2PortACLDrops_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,9,1,3),_SwL2PortACLDrops_Type())
swL2PortACLDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortACLDrops.setStatus(_A)
_SwL2PortMulticastDrops_Type=Counter32
_SwL2PortMulticastDrops_Object=MibTableColumn
swL2PortMulticastDrops=_SwL2PortMulticastDrops_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,9,1,4),_SwL2PortMulticastDrops_Type())
swL2PortMulticastDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortMulticastDrops.setStatus(_A)
_SwL2PortVLANIngressDrops_Type=Counter32
_SwL2PortVLANIngressDrops_Object=MibTableColumn
swL2PortVLANIngressDrops=_SwL2PortVLANIngressDrops_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,9,1,5),_SwL2PortVLANIngressDrops_Type())
swL2PortVLANIngressDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortVLANIngressDrops.setStatus(_A)
_SwL2PortJumboFrameCtrlTable_Object=MibTable
swL2PortJumboFrameCtrlTable=_SwL2PortJumboFrameCtrlTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,10))
if mibBuilder.loadTexts:swL2PortJumboFrameCtrlTable.setStatus(_A)
_SwL2PortJumboFrameCtrlEntry_Object=MibTableRow
swL2PortJumboFrameCtrlEntry=_SwL2PortJumboFrameCtrlEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,10,1))
swL2PortJumboFrameCtrlEntry.setIndexNames((0,_E,_A0))
if mibBuilder.loadTexts:swL2PortJumboFrameCtrlEntry.setStatus(_A)
_SwL2PortJumboFrameCtrlPortIndex_Type=Integer32
_SwL2PortJumboFrameCtrlPortIndex_Object=MibTableColumn
swL2PortJumboFrameCtrlPortIndex=_SwL2PortJumboFrameCtrlPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,10,1,1),_SwL2PortJumboFrameCtrlPortIndex_Type())
swL2PortJumboFrameCtrlPortIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:swL2PortJumboFrameCtrlPortIndex.setStatus(_A)
class _SwL2PortJumboFrameCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2PortJumboFrameCtrlState_Type.__name__=_B
_SwL2PortJumboFrameCtrlState_Object=MibTableColumn
swL2PortJumboFrameCtrlState=_SwL2PortJumboFrameCtrlState_Object((1,3,6,1,4,1,171,11,133,1,1,2,3,10,1,2),_SwL2PortJumboFrameCtrlState_Type())
swL2PortJumboFrameCtrlState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortJumboFrameCtrlState.setStatus(_A)
_SwL2DiffServMgmt_ObjectIdentity=ObjectIdentity
swL2DiffServMgmt=_SwL2DiffServMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,4))
_SwL2DiffServTypeCtrlTable_Object=MibTable
swL2DiffServTypeCtrlTable=_SwL2DiffServTypeCtrlTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,4,1))
if mibBuilder.loadTexts:swL2DiffServTypeCtrlTable.setStatus(_A)
_SwL2DiffServTypeCtrlEntry_Object=MibTableRow
swL2DiffServTypeCtrlEntry=_SwL2DiffServTypeCtrlEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,4,1,1))
swL2DiffServTypeCtrlEntry.setIndexNames((0,_E,_A1))
if mibBuilder.loadTexts:swL2DiffServTypeCtrlEntry.setStatus(_A)
class _SwL2DiffServTypeCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2DiffServTypeCtrlPortIndex_Type.__name__=_B
_SwL2DiffServTypeCtrlPortIndex_Object=MibTableColumn
swL2DiffServTypeCtrlPortIndex=_SwL2DiffServTypeCtrlPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,4,1,1,1),_SwL2DiffServTypeCtrlPortIndex_Type())
swL2DiffServTypeCtrlPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DiffServTypeCtrlPortIndex.setStatus(_A)
class _SwL2DiffServTypeCtrlDiffServType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('dscp',2),('tos',3)))
_SwL2DiffServTypeCtrlDiffServType_Type.__name__=_B
_SwL2DiffServTypeCtrlDiffServType_Object=MibTableColumn
swL2DiffServTypeCtrlDiffServType=_SwL2DiffServTypeCtrlDiffServType_Object((1,3,6,1,4,1,171,11,133,1,1,2,4,1,1,2),_SwL2DiffServTypeCtrlDiffServType_Type())
swL2DiffServTypeCtrlDiffServType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DiffServTypeCtrlDiffServType.setStatus(_A)
_SwL2DiffServDSCPCtrlTable_Object=MibTable
swL2DiffServDSCPCtrlTable=_SwL2DiffServDSCPCtrlTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,4,2))
if mibBuilder.loadTexts:swL2DiffServDSCPCtrlTable.setStatus(_A)
_SwL2DiffServDSCPCtrlEntry_Object=MibTableRow
swL2DiffServDSCPCtrlEntry=_SwL2DiffServDSCPCtrlEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,4,2,1))
swL2DiffServDSCPCtrlEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:swL2DiffServDSCPCtrlEntry.setStatus(_A)
class _SwL2DiffServDSCPCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2DiffServDSCPCtrlPortIndex_Type.__name__=_B
_SwL2DiffServDSCPCtrlPortIndex_Object=MibTableColumn
swL2DiffServDSCPCtrlPortIndex=_SwL2DiffServDSCPCtrlPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,4,2,1,1),_SwL2DiffServDSCPCtrlPortIndex_Type())
swL2DiffServDSCPCtrlPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DiffServDSCPCtrlPortIndex.setStatus(_A)
class _SwL2DiffServDSCPCtrlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dscp-Force-Overwrite',1),('dscp-Change-If-Zero',2)))
_SwL2DiffServDSCPCtrlMode_Type.__name__=_B
_SwL2DiffServDSCPCtrlMode_Object=MibTableColumn
swL2DiffServDSCPCtrlMode=_SwL2DiffServDSCPCtrlMode_Object((1,3,6,1,4,1,171,11,133,1,1,2,4,2,1,2),_SwL2DiffServDSCPCtrlMode_Type())
swL2DiffServDSCPCtrlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DiffServDSCPCtrlMode.setStatus(_A)
class _SwL2DiffServDSCPCtrlValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SwL2DiffServDSCPCtrlValue_Type.__name__=_B
_SwL2DiffServDSCPCtrlValue_Object=MibTableColumn
swL2DiffServDSCPCtrlValue=_SwL2DiffServDSCPCtrlValue_Object((1,3,6,1,4,1,171,11,133,1,1,2,4,2,1,3),_SwL2DiffServDSCPCtrlValue_Type())
swL2DiffServDSCPCtrlValue.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DiffServDSCPCtrlValue.setStatus(_A)
_SwL2DiffServTOSCtrlTable_Object=MibTable
swL2DiffServTOSCtrlTable=_SwL2DiffServTOSCtrlTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,4,3))
if mibBuilder.loadTexts:swL2DiffServTOSCtrlTable.setStatus(_A)
_SwL2DiffServTOSCtrlEntry_Object=MibTableRow
swL2DiffServTOSCtrlEntry=_SwL2DiffServTOSCtrlEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,4,3,1))
swL2DiffServTOSCtrlEntry.setIndexNames((0,_E,_A3))
if mibBuilder.loadTexts:swL2DiffServTOSCtrlEntry.setStatus(_A)
class _SwL2DiffServTOSCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2DiffServTOSCtrlPortIndex_Type.__name__=_B
_SwL2DiffServTOSCtrlPortIndex_Object=MibTableColumn
swL2DiffServTOSCtrlPortIndex=_SwL2DiffServTOSCtrlPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,4,3,1,1),_SwL2DiffServTOSCtrlPortIndex_Type())
swL2DiffServTOSCtrlPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DiffServTOSCtrlPortIndex.setStatus(_A)
class _SwL2DiffServTOSCtrlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tos-Force-Overwrite',1),('tos-TOS-Overwrite-802dot1p',2),('tos-802dot1p-Overwrite-TOS',3)))
_SwL2DiffServTOSCtrlMode_Type.__name__=_B
_SwL2DiffServTOSCtrlMode_Object=MibTableColumn
swL2DiffServTOSCtrlMode=_SwL2DiffServTOSCtrlMode_Object((1,3,6,1,4,1,171,11,133,1,1,2,4,3,1,2),_SwL2DiffServTOSCtrlMode_Type())
swL2DiffServTOSCtrlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DiffServTOSCtrlMode.setStatus(_A)
class _SwL2DiffServTOSCtrlValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2DiffServTOSCtrlValue_Type.__name__=_B
_SwL2DiffServTOSCtrlValue_Object=MibTableColumn
swL2DiffServTOSCtrlValue=_SwL2DiffServTOSCtrlValue_Object((1,3,6,1,4,1,171,11,133,1,1,2,4,3,1,3),_SwL2DiffServTOSCtrlValue_Type())
swL2DiffServTOSCtrlValue.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DiffServTOSCtrlValue.setStatus(_A)
_SwL2LimitedMulticastMgmt_ObjectIdentity=ObjectIdentity
swL2LimitedMulticastMgmt=_SwL2LimitedMulticastMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,5))
_SwL2MulticastFilterProfileTable_Object=MibTable
swL2MulticastFilterProfileTable=_SwL2MulticastFilterProfileTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,1))
if mibBuilder.loadTexts:swL2MulticastFilterProfileTable.setStatus(_A)
_SwL2MulticastFilterProfileEntry_Object=MibTableRow
swL2MulticastFilterProfileEntry=_SwL2MulticastFilterProfileEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,1,1))
swL2MulticastFilterProfileEntry.setIndexNames((0,_E,_A4))
if mibBuilder.loadTexts:swL2MulticastFilterProfileEntry.setStatus(_A)
class _SwL2MulticastFilterProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_SwL2MulticastFilterProfileIndex_Type.__name__=_B
_SwL2MulticastFilterProfileIndex_Object=MibTableColumn
swL2MulticastFilterProfileIndex=_SwL2MulticastFilterProfileIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,1,1,1),_SwL2MulticastFilterProfileIndex_Type())
swL2MulticastFilterProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MulticastFilterProfileIndex.setStatus(_A)
class _SwL2MulticastFilterProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwL2MulticastFilterProfileName_Type.__name__=_K
_SwL2MulticastFilterProfileName_Object=MibTableColumn
swL2MulticastFilterProfileName=_SwL2MulticastFilterProfileName_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,1,1,2),_SwL2MulticastFilterProfileName_Type())
swL2MulticastFilterProfileName.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2MulticastFilterProfileName.setStatus(_A)
_SwL2MulticastFilterStatus_Type=RowStatus
_SwL2MulticastFilterStatus_Object=MibTableColumn
swL2MulticastFilterStatus=_SwL2MulticastFilterStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,1,1,3),_SwL2MulticastFilterStatus_Type())
swL2MulticastFilterStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2MulticastFilterStatus.setStatus(_A)
_SwL2MulticastFilterProfileAddressTable_Object=MibTable
swL2MulticastFilterProfileAddressTable=_SwL2MulticastFilterProfileAddressTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,2))
if mibBuilder.loadTexts:swL2MulticastFilterProfileAddressTable.setStatus(_A)
_SwL2MulticastFilterProfileAddressEntry_Object=MibTableRow
swL2MulticastFilterProfileAddressEntry=_SwL2MulticastFilterProfileAddressEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,2,1))
swL2MulticastFilterProfileAddressEntry.setIndexNames((0,_E,_A5),(0,_E,_A6),(0,_E,_A7))
if mibBuilder.loadTexts:swL2MulticastFilterProfileAddressEntry.setStatus(_A)
class _SwL2MulticastFilterProfileIdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_SwL2MulticastFilterProfileIdIndex_Type.__name__=_B
_SwL2MulticastFilterProfileIdIndex_Object=MibTableColumn
swL2MulticastFilterProfileIdIndex=_SwL2MulticastFilterProfileIdIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,2,1,1),_SwL2MulticastFilterProfileIdIndex_Type())
swL2MulticastFilterProfileIdIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MulticastFilterProfileIdIndex.setStatus(_A)
_SwL2MulticastFilterFromIp_Type=IpAddress
_SwL2MulticastFilterFromIp_Object=MibTableColumn
swL2MulticastFilterFromIp=_SwL2MulticastFilterFromIp_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,2,1,2),_SwL2MulticastFilterFromIp_Type())
swL2MulticastFilterFromIp.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MulticastFilterFromIp.setStatus(_A)
_SwL2MulticastFilterToIp_Type=IpAddress
_SwL2MulticastFilterToIp_Object=MibTableColumn
swL2MulticastFilterToIp=_SwL2MulticastFilterToIp_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,2,1,3),_SwL2MulticastFilterToIp_Type())
swL2MulticastFilterToIp.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MulticastFilterToIp.setStatus(_A)
_SwL2MulticastFilterAddressState_Type=RowStatus
_SwL2MulticastFilterAddressState_Object=MibTableColumn
swL2MulticastFilterAddressState=_SwL2MulticastFilterAddressState_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,2,1,4),_SwL2MulticastFilterAddressState_Type())
swL2MulticastFilterAddressState.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2MulticastFilterAddressState.setStatus(_A)
_SwL2LimitedMulticastFilterPortTable_Object=MibTable
swL2LimitedMulticastFilterPortTable=_SwL2LimitedMulticastFilterPortTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,3))
if mibBuilder.loadTexts:swL2LimitedMulticastFilterPortTable.setStatus(_A)
_SwL2LimitedMulticastFilterPortEntry_Object=MibTableRow
swL2LimitedMulticastFilterPortEntry=_SwL2LimitedMulticastFilterPortEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,3,1))
swL2LimitedMulticastFilterPortEntry.setIndexNames((0,_E,_A8))
if mibBuilder.loadTexts:swL2LimitedMulticastFilterPortEntry.setStatus(_A)
_SwL2LimitedMulticastFilterPortIndex_Type=Integer32
_SwL2LimitedMulticastFilterPortIndex_Object=MibTableColumn
swL2LimitedMulticastFilterPortIndex=_SwL2LimitedMulticastFilterPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,3,1,1),_SwL2LimitedMulticastFilterPortIndex_Type())
swL2LimitedMulticastFilterPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LimitedMulticastFilterPortIndex.setStatus(_A)
class _SwL2LimitedMulticastFilterPortAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_SwL2LimitedMulticastFilterPortAccess_Type.__name__=_B
_SwL2LimitedMulticastFilterPortAccess_Object=MibTableColumn
swL2LimitedMulticastFilterPortAccess=_SwL2LimitedMulticastFilterPortAccess_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,3,1,2),_SwL2LimitedMulticastFilterPortAccess_Type())
swL2LimitedMulticastFilterPortAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LimitedMulticastFilterPortAccess.setStatus(_A)
_SwL2LimitedMulticastFilterPortProfileID_Type=DisplayString
_SwL2LimitedMulticastFilterPortProfileID_Object=MibTableColumn
swL2LimitedMulticastFilterPortProfileID=_SwL2LimitedMulticastFilterPortProfileID_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,3,1,3),_SwL2LimitedMulticastFilterPortProfileID_Type())
swL2LimitedMulticastFilterPortProfileID.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LimitedMulticastFilterPortProfileID.setStatus(_A)
class _SwL2LimitedMulticastFilterPortProfileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('add',2),('delete',3)))
_SwL2LimitedMulticastFilterPortProfileStatus_Type.__name__=_B
_SwL2LimitedMulticastFilterPortProfileStatus_Object=MibTableColumn
swL2LimitedMulticastFilterPortProfileStatus=_SwL2LimitedMulticastFilterPortProfileStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,3,1,4),_SwL2LimitedMulticastFilterPortProfileStatus_Type())
swL2LimitedMulticastFilterPortProfileStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2LimitedMulticastFilterPortProfileStatus.setStatus(_A)
_SwL2MulticastFilterPortMaxGroupTable_Object=MibTable
swL2MulticastFilterPortMaxGroupTable=_SwL2MulticastFilterPortMaxGroupTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,4))
if mibBuilder.loadTexts:swL2MulticastFilterPortMaxGroupTable.setStatus(_A)
_SwL2MulticastFilterPortMaxGroupEntry_Object=MibTableRow
swL2MulticastFilterPortMaxGroupEntry=_SwL2MulticastFilterPortMaxGroupEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,4,1))
swL2MulticastFilterPortMaxGroupEntry.setIndexNames((0,_E,_A9))
if mibBuilder.loadTexts:swL2MulticastFilterPortMaxGroupEntry.setStatus(_A)
_SwL2MulticastFilterPortMaxGroupPortIndex_Type=Integer32
_SwL2MulticastFilterPortMaxGroupPortIndex_Object=MibTableColumn
swL2MulticastFilterPortMaxGroupPortIndex=_SwL2MulticastFilterPortMaxGroupPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,4,1,1),_SwL2MulticastFilterPortMaxGroupPortIndex_Type())
swL2MulticastFilterPortMaxGroupPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MulticastFilterPortMaxGroupPortIndex.setStatus(_A)
class _SwL2MulticastFilterPortMaxGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_SwL2MulticastFilterPortMaxGroup_Type.__name__=_B
_SwL2MulticastFilterPortMaxGroup_Object=MibTableColumn
swL2MulticastFilterPortMaxGroup=_SwL2MulticastFilterPortMaxGroup_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,4,1,2),_SwL2MulticastFilterPortMaxGroup_Type())
swL2MulticastFilterPortMaxGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MulticastFilterPortMaxGroup.setStatus(_A)
_SwL2LimitedMulticastFilterVIDTable_Object=MibTable
swL2LimitedMulticastFilterVIDTable=_SwL2LimitedMulticastFilterVIDTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,5))
if mibBuilder.loadTexts:swL2LimitedMulticastFilterVIDTable.setStatus(_A)
_SwL2LimitedMulticastFilterVIDEntry_Object=MibTableRow
swL2LimitedMulticastFilterVIDEntry=_SwL2LimitedMulticastFilterVIDEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,5,1))
swL2LimitedMulticastFilterVIDEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:swL2LimitedMulticastFilterVIDEntry.setStatus(_A)
_SwL2LimitedMulticastFilterVIDIndex_Type=Integer32
_SwL2LimitedMulticastFilterVIDIndex_Object=MibTableColumn
swL2LimitedMulticastFilterVIDIndex=_SwL2LimitedMulticastFilterVIDIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,5,1,1),_SwL2LimitedMulticastFilterVIDIndex_Type())
swL2LimitedMulticastFilterVIDIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LimitedMulticastFilterVIDIndex.setStatus(_A)
class _SwL2LimitedMulticastFilterVIDAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_SwL2LimitedMulticastFilterVIDAccess_Type.__name__=_B
_SwL2LimitedMulticastFilterVIDAccess_Object=MibTableColumn
swL2LimitedMulticastFilterVIDAccess=_SwL2LimitedMulticastFilterVIDAccess_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,5,1,2),_SwL2LimitedMulticastFilterVIDAccess_Type())
swL2LimitedMulticastFilterVIDAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LimitedMulticastFilterVIDAccess.setStatus(_A)
_SwL2LimitedMulticastFilterVIDProfileID_Type=DisplayString
_SwL2LimitedMulticastFilterVIDProfileID_Object=MibTableColumn
swL2LimitedMulticastFilterVIDProfileID=_SwL2LimitedMulticastFilterVIDProfileID_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,5,1,3),_SwL2LimitedMulticastFilterVIDProfileID_Type())
swL2LimitedMulticastFilterVIDProfileID.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LimitedMulticastFilterVIDProfileID.setStatus(_A)
class _SwL2LimitedMulticastFilterVIDProfileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('add',2),('delete',3)))
_SwL2LimitedMulticastFilterVIDProfileStatus_Type.__name__=_B
_SwL2LimitedMulticastFilterVIDProfileStatus_Object=MibTableColumn
swL2LimitedMulticastFilterVIDProfileStatus=_SwL2LimitedMulticastFilterVIDProfileStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,5,1,4),_SwL2LimitedMulticastFilterVIDProfileStatus_Type())
swL2LimitedMulticastFilterVIDProfileStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2LimitedMulticastFilterVIDProfileStatus.setStatus(_A)
_SwL2MulticastFilterVIDMaxGroupTable_Object=MibTable
swL2MulticastFilterVIDMaxGroupTable=_SwL2MulticastFilterVIDMaxGroupTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,6))
if mibBuilder.loadTexts:swL2MulticastFilterVIDMaxGroupTable.setStatus(_A)
_SwL2MulticastFilterVIDMaxGroupEntry_Object=MibTableRow
swL2MulticastFilterVIDMaxGroupEntry=_SwL2MulticastFilterVIDMaxGroupEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,6,1))
swL2MulticastFilterVIDMaxGroupEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:swL2MulticastFilterVIDMaxGroupEntry.setStatus(_A)
_SwL2MulticastFilterVIDMaxGroupVIDIndex_Type=Integer32
_SwL2MulticastFilterVIDMaxGroupVIDIndex_Object=MibTableColumn
swL2MulticastFilterVIDMaxGroupVIDIndex=_SwL2MulticastFilterVIDMaxGroupVIDIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,6,1,1),_SwL2MulticastFilterVIDMaxGroupVIDIndex_Type())
swL2MulticastFilterVIDMaxGroupVIDIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MulticastFilterVIDMaxGroupVIDIndex.setStatus(_A)
class _SwL2MulticastFilterVIDMaxGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_SwL2MulticastFilterVIDMaxGroup_Type.__name__=_B
_SwL2MulticastFilterVIDMaxGroup_Object=MibTableColumn
swL2MulticastFilterVIDMaxGroup=_SwL2MulticastFilterVIDMaxGroup_Object((1,3,6,1,4,1,171,11,133,1,1,2,5,6,1,2),_SwL2MulticastFilterVIDMaxGroup_Type())
swL2MulticastFilterVIDMaxGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MulticastFilterVIDMaxGroup.setStatus(_A)
_SwL2QOSMgmt_ObjectIdentity=ObjectIdentity
swL2QOSMgmt=_SwL2QOSMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,6))
_SwL2QOSBandwidthControlTable_Object=MibTable
swL2QOSBandwidthControlTable=_SwL2QOSBandwidthControlTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,1))
if mibBuilder.loadTexts:swL2QOSBandwidthControlTable.setStatus(_A)
_SwL2QOSBandwidthControlEntry_Object=MibTableRow
swL2QOSBandwidthControlEntry=_SwL2QOSBandwidthControlEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,1,1))
swL2QOSBandwidthControlEntry.setIndexNames((0,_E,_AC))
if mibBuilder.loadTexts:swL2QOSBandwidthControlEntry.setStatus(_A)
class _SwL2QOSBandwidthPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,768))
_SwL2QOSBandwidthPortIndex_Type.__name__=_B
_SwL2QOSBandwidthPortIndex_Object=MibTableColumn
swL2QOSBandwidthPortIndex=_SwL2QOSBandwidthPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,1,1,1),_SwL2QOSBandwidthPortIndex_Type())
swL2QOSBandwidthPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSBandwidthPortIndex.setStatus(_A)
class _SwL2QOSBandwidthRxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_SwL2QOSBandwidthRxRate_Type.__name__=_B
_SwL2QOSBandwidthRxRate_Object=MibTableColumn
swL2QOSBandwidthRxRate=_SwL2QOSBandwidthRxRate_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,1,1,2),_SwL2QOSBandwidthRxRate_Type())
swL2QOSBandwidthRxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthRxRate.setStatus(_A)
class _SwL2QOSBandwidthTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_SwL2QOSBandwidthTxRate_Type.__name__=_B
_SwL2QOSBandwidthTxRate_Object=MibTableColumn
swL2QOSBandwidthTxRate=_SwL2QOSBandwidthTxRate_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,1,1,3),_SwL2QOSBandwidthTxRate_Type())
swL2QOSBandwidthTxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthTxRate.setStatus(_A)
_SwL2QOSBandwidthRadiusRxRate_Type=Integer32
_SwL2QOSBandwidthRadiusRxRate_Object=MibTableColumn
swL2QOSBandwidthRadiusRxRate=_SwL2QOSBandwidthRadiusRxRate_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,1,1,4),_SwL2QOSBandwidthRadiusRxRate_Type())
swL2QOSBandwidthRadiusRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSBandwidthRadiusRxRate.setStatus(_A)
_SwL2QOSBandwidthRadiusTxRate_Type=Integer32
_SwL2QOSBandwidthRadiusTxRate_Object=MibTableColumn
swL2QOSBandwidthRadiusTxRate=_SwL2QOSBandwidthRadiusTxRate_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,1,1,5),_SwL2QOSBandwidthRadiusTxRate_Type())
swL2QOSBandwidthRadiusTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSBandwidthRadiusTxRate.setStatus(_A)
_SwL2QOSSchedulingTable_Object=MibTable
swL2QOSSchedulingTable=_SwL2QOSSchedulingTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,2))
if mibBuilder.loadTexts:swL2QOSSchedulingTable.setStatus(_A)
_SwL2QOSSchedulingEntry_Object=MibTableRow
swL2QOSSchedulingEntry=_SwL2QOSSchedulingEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,2,1))
swL2QOSSchedulingEntry.setIndexNames((0,_E,_AD))
if mibBuilder.loadTexts:swL2QOSSchedulingEntry.setStatus(_A)
class _SwL2QOSSchedulingClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOSSchedulingClassIndex_Type.__name__=_B
_SwL2QOSSchedulingClassIndex_Object=MibTableColumn
swL2QOSSchedulingClassIndex=_SwL2QOSSchedulingClassIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,2,1,1),_SwL2QOSSchedulingClassIndex_Type())
swL2QOSSchedulingClassIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSSchedulingClassIndex.setStatus(_A)
class _SwL2QOSSchedulingMaxPkts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_SwL2QOSSchedulingMaxPkts_Type.__name__=_B
_SwL2QOSSchedulingMaxPkts_Object=MibTableColumn
swL2QOSSchedulingMaxPkts=_SwL2QOSSchedulingMaxPkts_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,2,1,2),_SwL2QOSSchedulingMaxPkts_Type())
swL2QOSSchedulingMaxPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSSchedulingMaxPkts.setStatus(_A)
class _SwL2QOSSchedulingMechanism_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('strict',1),(_AE,2),(_AF,3)))
_SwL2QOSSchedulingMechanism_Type.__name__=_B
_SwL2QOSSchedulingMechanism_Object=MibTableColumn
swL2QOSSchedulingMechanism=_SwL2QOSSchedulingMechanism_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,2,1,3),_SwL2QOSSchedulingMechanism_Type())
swL2QOSSchedulingMechanism.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSSchedulingMechanism.setStatus(_A)
class _SwL2QOSSchedulingMaxLatency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL2QOSSchedulingMaxLatency_Type.__name__=_B
_SwL2QOSSchedulingMaxLatency_Object=MibTableColumn
swL2QOSSchedulingMaxLatency=_SwL2QOSSchedulingMaxLatency_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,2,1,4),_SwL2QOSSchedulingMaxLatency_Type())
swL2QOSSchedulingMaxLatency.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSSchedulingMaxLatency.setStatus(_A)
_SwL2QOS8021pUserPriorityTable_Object=MibTable
swL2QOS8021pUserPriorityTable=_SwL2QOS8021pUserPriorityTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,3))
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityTable.setStatus(_A)
_SwL2QOS8021pUserPriorityEntry_Object=MibTableRow
swL2QOS8021pUserPriorityEntry=_SwL2QOS8021pUserPriorityEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,3,1))
swL2QOS8021pUserPriorityEntry.setIndexNames((0,_E,_AG))
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityEntry.setStatus(_A)
class _SwL2QOS8021pUserPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOS8021pUserPriorityIndex_Type.__name__=_B
_SwL2QOS8021pUserPriorityIndex_Object=MibTableColumn
swL2QOS8021pUserPriorityIndex=_SwL2QOS8021pUserPriorityIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,3,1,1),_SwL2QOS8021pUserPriorityIndex_Type())
swL2QOS8021pUserPriorityIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityIndex.setStatus(_A)
class _SwL2QOS8021pUserPriorityClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_SwL2QOS8021pUserPriorityClass_Type.__name__=_B
_SwL2QOS8021pUserPriorityClass_Object=MibTableColumn
swL2QOS8021pUserPriorityClass=_SwL2QOS8021pUserPriorityClass_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,3,1,2),_SwL2QOS8021pUserPriorityClass_Type())
swL2QOS8021pUserPriorityClass.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityClass.setStatus(_A)
_SwL2QOS8021pDefaultPriorityTable_Object=MibTable
swL2QOS8021pDefaultPriorityTable=_SwL2QOS8021pDefaultPriorityTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,4))
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityTable.setStatus(_A)
_SwL2QOS8021pDefaultPriorityEntry_Object=MibTableRow
swL2QOS8021pDefaultPriorityEntry=_SwL2QOS8021pDefaultPriorityEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,4,1))
swL2QOS8021pDefaultPriorityEntry.setIndexNames((0,_E,_AH))
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityEntry.setStatus(_A)
class _SwL2QOS8021pDefaultPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,768))
_SwL2QOS8021pDefaultPriorityIndex_Type.__name__=_B
_SwL2QOS8021pDefaultPriorityIndex_Object=MibTableColumn
swL2QOS8021pDefaultPriorityIndex=_SwL2QOS8021pDefaultPriorityIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,4,1,1),_SwL2QOS8021pDefaultPriorityIndex_Type())
swL2QOS8021pDefaultPriorityIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityIndex.setStatus(_A)
class _SwL2QOS8021pDefaultPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOS8021pDefaultPriority_Type.__name__=_B
_SwL2QOS8021pDefaultPriority_Object=MibTableColumn
swL2QOS8021pDefaultPriority=_SwL2QOS8021pDefaultPriority_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,4,1,2),_SwL2QOS8021pDefaultPriority_Type())
swL2QOS8021pDefaultPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriority.setStatus(_A)
_SwL2QOS8021pRadiusPriority_Type=Integer32
_SwL2QOS8021pRadiusPriority_Object=MibTableColumn
swL2QOS8021pRadiusPriority=_SwL2QOS8021pRadiusPriority_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,4,1,3),_SwL2QOS8021pRadiusPriority_Type())
swL2QOS8021pRadiusPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOS8021pRadiusPriority.setStatus(_A)
class _SwL2QOSSchedulingMechanismCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('strict',1),(_AE,2),(_AF,3)))
_SwL2QOSSchedulingMechanismCtrl_Type.__name__=_B
_SwL2QOSSchedulingMechanismCtrl_Object=MibScalar
swL2QOSSchedulingMechanismCtrl=_SwL2QOSSchedulingMechanismCtrl_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,5),_SwL2QOSSchedulingMechanismCtrl_Type())
swL2QOSSchedulingMechanismCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSSchedulingMechanismCtrl.setStatus(_A)
class _SwL2QOSHolPreventionCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2QOSHolPreventionCtrl_Type.__name__=_B
_SwL2QOSHolPreventionCtrl_Object=MibScalar
swL2QOSHolPreventionCtrl=_SwL2QOSHolPreventionCtrl_Object((1,3,6,1,4,1,171,11,133,1,1,2,6,6),_SwL2QOSHolPreventionCtrl_Type())
swL2QOSHolPreventionCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSHolPreventionCtrl.setStatus(_A)
_SwL2PortSecurityMgmt_ObjectIdentity=ObjectIdentity
swL2PortSecurityMgmt=_SwL2PortSecurityMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,7))
_SwL2PortSecurityControlTable_Object=MibTable
swL2PortSecurityControlTable=_SwL2PortSecurityControlTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,7,1))
if mibBuilder.loadTexts:swL2PortSecurityControlTable.setStatus(_A)
_SwL2PortSecurityControlEntry_Object=MibTableRow
swL2PortSecurityControlEntry=_SwL2PortSecurityControlEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,7,1,1))
swL2PortSecurityControlEntry.setIndexNames((0,_E,_AI))
if mibBuilder.loadTexts:swL2PortSecurityControlEntry.setStatus(_A)
class _SwL2PortSecurityPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,768))
_SwL2PortSecurityPortIndex_Type.__name__=_B
_SwL2PortSecurityPortIndex_Object=MibTableColumn
swL2PortSecurityPortIndex=_SwL2PortSecurityPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,7,1,1,1),_SwL2PortSecurityPortIndex_Type())
swL2PortSecurityPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityPortIndex.setStatus(_A)
class _SwL2PortSecurityMaxLernAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortSecurityMaxLernAddr_Type.__name__=_B
_SwL2PortSecurityMaxLernAddr_Object=MibTableColumn
swL2PortSecurityMaxLernAddr=_SwL2PortSecurityMaxLernAddr_Object((1,3,6,1,4,1,171,11,133,1,1,2,7,1,1,2),_SwL2PortSecurityMaxLernAddr_Type())
swL2PortSecurityMaxLernAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityMaxLernAddr.setStatus(_A)
class _SwL2PortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('permanent',2),('deleteOnTimeout',3),('deleteOnReset',4)))
_SwL2PortSecurityMode_Type.__name__=_B
_SwL2PortSecurityMode_Object=MibTableColumn
swL2PortSecurityMode=_SwL2PortSecurityMode_Object((1,3,6,1,4,1,171,11,133,1,1,2,7,1,1,3),_SwL2PortSecurityMode_Type())
swL2PortSecurityMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityMode.setStatus(_A)
class _SwL2PortSecurityAdmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_P,2),(_Q,3)))
_SwL2PortSecurityAdmState_Type.__name__=_B
_SwL2PortSecurityAdmState_Object=MibTableColumn
swL2PortSecurityAdmState=_SwL2PortSecurityAdmState_Object((1,3,6,1,4,1,171,11,133,1,1,2,7,1,1,4),_SwL2PortSecurityAdmState_Type())
swL2PortSecurityAdmState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityAdmState.setStatus(_A)
class _SwL2PortSecurityEntryClearCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_N,2)))
_SwL2PortSecurityEntryClearCtrl_Type.__name__=_B
_SwL2PortSecurityEntryClearCtrl_Object=MibTableColumn
swL2PortSecurityEntryClearCtrl=_SwL2PortSecurityEntryClearCtrl_Object((1,3,6,1,4,1,171,11,133,1,1,2,7,1,1,5),_SwL2PortSecurityEntryClearCtrl_Type())
swL2PortSecurityEntryClearCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityEntryClearCtrl.setStatus(_A)
_SwL2PortSecurityDelCtrl_ObjectIdentity=ObjectIdentity
swL2PortSecurityDelCtrl=_SwL2PortSecurityDelCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,7,2))
class _SwL2PortSecurityDelVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2PortSecurityDelVlanName_Type.__name__=_K
_SwL2PortSecurityDelVlanName_Object=MibScalar
swL2PortSecurityDelVlanName=_SwL2PortSecurityDelVlanName_Object((1,3,6,1,4,1,171,11,133,1,1,2,7,2,1),_SwL2PortSecurityDelVlanName_Type())
swL2PortSecurityDelVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityDelVlanName.setStatus(_A)
class _SwL2PortSecurityDelPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,768))
_SwL2PortSecurityDelPort_Type.__name__=_B
_SwL2PortSecurityDelPort_Object=MibScalar
swL2PortSecurityDelPort=_SwL2PortSecurityDelPort_Object((1,3,6,1,4,1,171,11,133,1,1,2,7,2,2),_SwL2PortSecurityDelPort_Type())
swL2PortSecurityDelPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityDelPort.setStatus(_A)
_SwL2PortSecurityDelMacAddress_Type=MacAddress
_SwL2PortSecurityDelMacAddress_Object=MibScalar
swL2PortSecurityDelMacAddress=_SwL2PortSecurityDelMacAddress_Object((1,3,6,1,4,1,171,11,133,1,1,2,7,2,3),_SwL2PortSecurityDelMacAddress_Type())
swL2PortSecurityDelMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityDelMacAddress.setStatus(_A)
class _SwL2PortSecurityDelActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SwL2PortSecurityDelActivity_Type.__name__=_B
_SwL2PortSecurityDelActivity_Object=MibScalar
swL2PortSecurityDelActivity=_SwL2PortSecurityDelActivity_Object((1,3,6,1,4,1,171,11,133,1,1,2,7,2,4),_SwL2PortSecurityDelActivity_Type())
swL2PortSecurityDelActivity.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityDelActivity.setStatus(_A)
class _SwL2PortSecurityTrapLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_P,2),(_Q,3)))
_SwL2PortSecurityTrapLogState_Type.__name__=_B
_SwL2PortSecurityTrapLogState_Object=MibScalar
swL2PortSecurityTrapLogState=_SwL2PortSecurityTrapLogState_Object((1,3,6,1,4,1,171,11,133,1,1,2,7,3),_SwL2PortSecurityTrapLogState_Type())
swL2PortSecurityTrapLogState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityTrapLogState.setStatus(_A)
_SwL2DhcpRelayMgmt_ObjectIdentity=ObjectIdentity
swL2DhcpRelayMgmt=_SwL2DhcpRelayMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,8))
class _SwL2DhcpRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DhcpRelayState_Type.__name__=_B
_SwL2DhcpRelayState_Object=MibScalar
swL2DhcpRelayState=_SwL2DhcpRelayState_Object((1,3,6,1,4,1,171,11,133,1,1,2,8,1),_SwL2DhcpRelayState_Type())
swL2DhcpRelayState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpRelayState.setStatus(_A)
class _SwL2DhcpRelayHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_SwL2DhcpRelayHopCount_Type.__name__=_B
_SwL2DhcpRelayHopCount_Object=MibScalar
swL2DhcpRelayHopCount=_SwL2DhcpRelayHopCount_Object((1,3,6,1,4,1,171,11,133,1,1,2,8,2),_SwL2DhcpRelayHopCount_Type())
swL2DhcpRelayHopCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpRelayHopCount.setStatus(_A)
class _SwL2DhcpRelayTimeThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2DhcpRelayTimeThreshold_Type.__name__=_B
_SwL2DhcpRelayTimeThreshold_Object=MibScalar
swL2DhcpRelayTimeThreshold=_SwL2DhcpRelayTimeThreshold_Object((1,3,6,1,4,1,171,11,133,1,1,2,8,3),_SwL2DhcpRelayTimeThreshold_Type())
swL2DhcpRelayTimeThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpRelayTimeThreshold.setStatus(_A)
class _SwL2DhcpRelayOption82State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DhcpRelayOption82State_Type.__name__=_B
_SwL2DhcpRelayOption82State_Object=MibScalar
swL2DhcpRelayOption82State=_SwL2DhcpRelayOption82State_Object((1,3,6,1,4,1,171,11,133,1,1,2,8,4),_SwL2DhcpRelayOption82State_Type())
swL2DhcpRelayOption82State.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpRelayOption82State.setStatus(_A)
class _SwL2DhcpRelayOption82Check_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DhcpRelayOption82Check_Type.__name__=_B
_SwL2DhcpRelayOption82Check_Object=MibScalar
swL2DhcpRelayOption82Check=_SwL2DhcpRelayOption82Check_Object((1,3,6,1,4,1,171,11,133,1,1,2,8,5),_SwL2DhcpRelayOption82Check_Type())
swL2DhcpRelayOption82Check.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpRelayOption82Check.setStatus(_A)
class _SwL2DhcpRelayOption82Policy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('replace',1),('drop',2),('keep',3)))
_SwL2DhcpRelayOption82Policy_Type.__name__=_B
_SwL2DhcpRelayOption82Policy_Object=MibScalar
swL2DhcpRelayOption82Policy=_SwL2DhcpRelayOption82Policy_Object((1,3,6,1,4,1,171,11,133,1,1,2,8,6),_SwL2DhcpRelayOption82Policy_Type())
swL2DhcpRelayOption82Policy.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpRelayOption82Policy.setStatus(_A)
_SwL2DhcpRelayCtrlTable_Object=MibTable
swL2DhcpRelayCtrlTable=_SwL2DhcpRelayCtrlTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,8,7))
if mibBuilder.loadTexts:swL2DhcpRelayCtrlTable.setStatus(_A)
_SwL2DhcpRelayCtrlEntry_Object=MibTableRow
swL2DhcpRelayCtrlEntry=_SwL2DhcpRelayCtrlEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,8,7,1))
swL2DhcpRelayCtrlEntry.setIndexNames((0,_E,_AJ),(0,_E,_AK))
if mibBuilder.loadTexts:swL2DhcpRelayCtrlEntry.setStatus(_A)
class _SwL2DhcpRelayCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL2DhcpRelayCtrlInterfaceName_Type.__name__=_K
_SwL2DhcpRelayCtrlInterfaceName_Object=MibTableColumn
swL2DhcpRelayCtrlInterfaceName=_SwL2DhcpRelayCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,133,1,1,2,8,7,1,1),_SwL2DhcpRelayCtrlInterfaceName_Type())
swL2DhcpRelayCtrlInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayCtrlInterfaceName.setStatus(_A)
_SwL2DhcpRelayCtrlServer_Type=IpAddress
_SwL2DhcpRelayCtrlServer_Object=MibTableColumn
swL2DhcpRelayCtrlServer=_SwL2DhcpRelayCtrlServer_Object((1,3,6,1,4,1,171,11,133,1,1,2,8,7,1,2),_SwL2DhcpRelayCtrlServer_Type())
swL2DhcpRelayCtrlServer.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpRelayCtrlServer.setStatus(_A)
class _SwL2DhcpRelayCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('invalid',2),('valid',3)))
_SwL2DhcpRelayCtrlState_Type.__name__=_B
_SwL2DhcpRelayCtrlState_Object=MibTableColumn
swL2DhcpRelayCtrlState=_SwL2DhcpRelayCtrlState_Object((1,3,6,1,4,1,171,11,133,1,1,2,8,7,1,3),_SwL2DhcpRelayCtrlState_Type())
swL2DhcpRelayCtrlState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpRelayCtrlState.setStatus(_A)
_SwL2TrunkMgmt_ObjectIdentity=ObjectIdentity
swL2TrunkMgmt=_SwL2TrunkMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,9))
class _SwL2TrunkMaxSupportedEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkMaxSupportedEntries_Type.__name__=_B
_SwL2TrunkMaxSupportedEntries_Object=MibScalar
swL2TrunkMaxSupportedEntries=_SwL2TrunkMaxSupportedEntries_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,1),_SwL2TrunkMaxSupportedEntries_Type())
swL2TrunkMaxSupportedEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkMaxSupportedEntries.setStatus(_A)
class _SwL2TrunkCurrentNumEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkCurrentNumEntries_Type.__name__=_B
_SwL2TrunkCurrentNumEntries_Object=MibScalar
swL2TrunkCurrentNumEntries=_SwL2TrunkCurrentNumEntries_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,2),_SwL2TrunkCurrentNumEntries_Type())
swL2TrunkCurrentNumEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkCurrentNumEntries.setStatus(_A)
_SwL2TrunkCtrlTable_Object=MibTable
swL2TrunkCtrlTable=_SwL2TrunkCtrlTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,3))
if mibBuilder.loadTexts:swL2TrunkCtrlTable.setStatus(_A)
_SwL2TrunkCtrlEntry_Object=MibTableRow
swL2TrunkCtrlEntry=_SwL2TrunkCtrlEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,3,1))
swL2TrunkCtrlEntry.setIndexNames((0,_E,_AL))
if mibBuilder.loadTexts:swL2TrunkCtrlEntry.setStatus(_A)
class _SwL2TrunkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkIndex_Type.__name__=_B
_SwL2TrunkIndex_Object=MibTableColumn
swL2TrunkIndex=_SwL2TrunkIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,3,1,1),_SwL2TrunkIndex_Type())
swL2TrunkIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkIndex.setStatus(_A)
class _SwL2TrunkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwL2TrunkName_Type.__name__=_K
_SwL2TrunkName_Object=MibTableColumn
swL2TrunkName=_SwL2TrunkName_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,3,1,2),_SwL2TrunkName_Type())
swL2TrunkName.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2TrunkName.setStatus(_A)
class _SwL2TrunkMasterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2TrunkMasterPort_Type.__name__=_B
_SwL2TrunkMasterPort_Object=MibTableColumn
swL2TrunkMasterPort=_SwL2TrunkMasterPort_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,3,1,3),_SwL2TrunkMasterPort_Type())
swL2TrunkMasterPort.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2TrunkMasterPort.setStatus(_A)
_SwL2TrunkMember_Type=PortList
_SwL2TrunkMember_Object=MibTableColumn
swL2TrunkMember=_SwL2TrunkMember_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,3,1,4),_SwL2TrunkMember_Type())
swL2TrunkMember.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2TrunkMember.setStatus(_A)
class _SwL2TrunkFloodingPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2TrunkFloodingPort_Type.__name__=_B
_SwL2TrunkFloodingPort_Object=MibTableColumn
swL2TrunkFloodingPort=_SwL2TrunkFloodingPort_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,3,1,5),_SwL2TrunkFloodingPort_Type())
swL2TrunkFloodingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkFloodingPort.setStatus(_A)
class _SwL2TrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('static',2),('lacp',3)))
_SwL2TrunkType_Type.__name__=_B
_SwL2TrunkType_Object=MibTableColumn
swL2TrunkType=_SwL2TrunkType_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,3,1,6),_SwL2TrunkType_Type())
swL2TrunkType.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2TrunkType.setStatus(_A)
_SwL2TrunkState_Type=RowStatus
_SwL2TrunkState_Object=MibTableColumn
swL2TrunkState=_SwL2TrunkState_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,3,1,7),_SwL2TrunkState_Type())
swL2TrunkState.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2TrunkState.setStatus(_A)
class _SwL2TrunkAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_H,1),('mac-source',2),('mac-destination',3),('mac-source-dest',4),('ip-source',5),('ip-destination',6),('ip-source-dest',7),('l4-source-port',8),('l4-destination-port',9),('l4-source-dest-port',10)))
_SwL2TrunkAlgorithm_Type.__name__=_B
_SwL2TrunkAlgorithm_Object=MibScalar
swL2TrunkAlgorithm=_SwL2TrunkAlgorithm_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,4),_SwL2TrunkAlgorithm_Type())
swL2TrunkAlgorithm.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkAlgorithm.setStatus(_A)
_SwL2TrunkLACPPortTable_Object=MibTable
swL2TrunkLACPPortTable=_SwL2TrunkLACPPortTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,5))
if mibBuilder.loadTexts:swL2TrunkLACPPortTable.setStatus(_A)
_SwL2TrunkLACPPortEntry_Object=MibTableRow
swL2TrunkLACPPortEntry=_SwL2TrunkLACPPortEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,5,1))
swL2TrunkLACPPortEntry.setIndexNames((0,_E,_AM))
if mibBuilder.loadTexts:swL2TrunkLACPPortEntry.setStatus(_A)
class _SwL2TrunkLACPPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkLACPPortIndex_Type.__name__=_B
_SwL2TrunkLACPPortIndex_Object=MibTableColumn
swL2TrunkLACPPortIndex=_SwL2TrunkLACPPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,5,1,1),_SwL2TrunkLACPPortIndex_Type())
swL2TrunkLACPPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkLACPPortIndex.setStatus(_A)
class _SwL2TrunkLACPPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),('passive',2)))
_SwL2TrunkLACPPortState_Type.__name__=_B
_SwL2TrunkLACPPortState_Object=MibTableColumn
swL2TrunkLACPPortState=_SwL2TrunkLACPPortState_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,5,1,2),_SwL2TrunkLACPPortState_Type())
swL2TrunkLACPPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkLACPPortState.setStatus(_A)
_SwL2TrunkVLANTable_Object=MibTable
swL2TrunkVLANTable=_SwL2TrunkVLANTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,6))
if mibBuilder.loadTexts:swL2TrunkVLANTable.setStatus(_A)
_SwL2TrunkVLANEntry_Object=MibTableRow
swL2TrunkVLANEntry=_SwL2TrunkVLANEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,6,1))
swL2TrunkVLANEntry.setIndexNames((0,_E,_AN))
if mibBuilder.loadTexts:swL2TrunkVLANEntry.setStatus(_A)
class _SwL2TrunkVLANPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkVLANPort_Type.__name__=_B
_SwL2TrunkVLANPort_Object=MibTableColumn
swL2TrunkVLANPort=_SwL2TrunkVLANPort_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,6,1,1),_SwL2TrunkVLANPort_Type())
swL2TrunkVLANPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkVLANPort.setStatus(_A)
class _SwL2TrunkVLANState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2TrunkVLANState_Type.__name__=_B
_SwL2TrunkVLANState_Object=MibTableColumn
swL2TrunkVLANState=_SwL2TrunkVLANState_Object((1,3,6,1,4,1,171,11,133,1,1,2,9,6,1,2),_SwL2TrunkVLANState_Type())
swL2TrunkVLANState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkVLANState.setStatus(_A)
_SwL2MirrorMgmt_ObjectIdentity=ObjectIdentity
swL2MirrorMgmt=_SwL2MirrorMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,10))
class _SwL2MirrorLogicTargetPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2MirrorLogicTargetPort_Type.__name__=_B
_SwL2MirrorLogicTargetPort_Object=MibScalar
swL2MirrorLogicTargetPort=_SwL2MirrorLogicTargetPort_Object((1,3,6,1,4,1,171,11,133,1,1,2,10,1),_SwL2MirrorLogicTargetPort_Type())
swL2MirrorLogicTargetPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MirrorLogicTargetPort.setStatus(_A)
_SwL2MirrorPortSourceIngress_Type=PortList
_SwL2MirrorPortSourceIngress_Object=MibScalar
swL2MirrorPortSourceIngress=_SwL2MirrorPortSourceIngress_Object((1,3,6,1,4,1,171,11,133,1,1,2,10,2),_SwL2MirrorPortSourceIngress_Type())
swL2MirrorPortSourceIngress.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MirrorPortSourceIngress.setStatus(_A)
_SwL2MirrorPortSourceEgress_Type=PortList
_SwL2MirrorPortSourceEgress_Object=MibScalar
swL2MirrorPortSourceEgress=_SwL2MirrorPortSourceEgress_Object((1,3,6,1,4,1,171,11,133,1,1,2,10,3),_SwL2MirrorPortSourceEgress_Type())
swL2MirrorPortSourceEgress.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MirrorPortSourceEgress.setStatus(_A)
class _SwL2MirrorPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2MirrorPortState_Type.__name__=_B
_SwL2MirrorPortState_Object=MibScalar
swL2MirrorPortState=_SwL2MirrorPortState_Object((1,3,6,1,4,1,171,11,133,1,1,2,10,4),_SwL2MirrorPortState_Type())
swL2MirrorPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MirrorPortState.setStatus(_A)
_SwL2MirrorGroupTable_Object=MibTable
swL2MirrorGroupTable=_SwL2MirrorGroupTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,10,5))
if mibBuilder.loadTexts:swL2MirrorGroupTable.setStatus(_A)
_SwL2MirrorGroupEntry_Object=MibTableRow
swL2MirrorGroupEntry=_SwL2MirrorGroupEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,10,5,1))
swL2MirrorGroupEntry.setIndexNames((0,_E,_AO))
if mibBuilder.loadTexts:swL2MirrorGroupEntry.setStatus(_A)
_SwL2MirrorGroupID_Type=Integer32
_SwL2MirrorGroupID_Object=MibTableColumn
swL2MirrorGroupID=_SwL2MirrorGroupID_Object((1,3,6,1,4,1,171,11,133,1,1,2,10,5,1,1),_SwL2MirrorGroupID_Type())
swL2MirrorGroupID.setMaxAccess(_O)
if mibBuilder.loadTexts:swL2MirrorGroupID.setStatus(_A)
_SwL2MirrorGroupRowStatus_Type=RowStatus
_SwL2MirrorGroupRowStatus_Object=MibTableColumn
swL2MirrorGroupRowStatus=_SwL2MirrorGroupRowStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,10,5,1,2),_SwL2MirrorGroupRowStatus_Type())
swL2MirrorGroupRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2MirrorGroupRowStatus.setStatus(_A)
class _SwL2MirrorGroupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2MirrorGroupState_Type.__name__=_B
_SwL2MirrorGroupState_Object=MibTableColumn
swL2MirrorGroupState=_SwL2MirrorGroupState_Object((1,3,6,1,4,1,171,11,133,1,1,2,10,5,1,3),_SwL2MirrorGroupState_Type())
swL2MirrorGroupState.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2MirrorGroupState.setStatus(_A)
class _SwL2MirrorGroupTargetPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2MirrorGroupTargetPort_Type.__name__=_B
_SwL2MirrorGroupTargetPort_Object=MibTableColumn
swL2MirrorGroupTargetPort=_SwL2MirrorGroupTargetPort_Object((1,3,6,1,4,1,171,11,133,1,1,2,10,5,1,4),_SwL2MirrorGroupTargetPort_Type())
swL2MirrorGroupTargetPort.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2MirrorGroupTargetPort.setStatus(_A)
_SwL2MirrorGroupSourceIngress_Type=PortList
_SwL2MirrorGroupSourceIngress_Object=MibTableColumn
swL2MirrorGroupSourceIngress=_SwL2MirrorGroupSourceIngress_Object((1,3,6,1,4,1,171,11,133,1,1,2,10,5,1,5),_SwL2MirrorGroupSourceIngress_Type())
swL2MirrorGroupSourceIngress.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2MirrorGroupSourceIngress.setStatus(_A)
_SwL2MirrorGroupSourceEngress_Type=PortList
_SwL2MirrorGroupSourceEngress_Object=MibTableColumn
swL2MirrorGroupSourceEngress=_SwL2MirrorGroupSourceEngress_Object((1,3,6,1,4,1,171,11,133,1,1,2,10,5,1,6),_SwL2MirrorGroupSourceEngress_Type())
swL2MirrorGroupSourceEngress.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2MirrorGroupSourceEngress.setStatus(_A)
_SwL2IGMPMgmt_ObjectIdentity=ObjectIdentity
swL2IGMPMgmt=_SwL2IGMPMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,11))
class _SwL2IGMPMaxSupportedVlans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPMaxSupportedVlans_Type.__name__=_B
_SwL2IGMPMaxSupportedVlans_Object=MibScalar
swL2IGMPMaxSupportedVlans=_SwL2IGMPMaxSupportedVlans_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,1),_SwL2IGMPMaxSupportedVlans_Type())
swL2IGMPMaxSupportedVlans.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMaxSupportedVlans.setStatus(_A)
class _SwL2IGMPMaxIpGroupNumPerVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPMaxIpGroupNumPerVlan_Type.__name__=_B
_SwL2IGMPMaxIpGroupNumPerVlan_Object=MibScalar
swL2IGMPMaxIpGroupNumPerVlan=_SwL2IGMPMaxIpGroupNumPerVlan_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,2),_SwL2IGMPMaxIpGroupNumPerVlan_Type())
swL2IGMPMaxIpGroupNumPerVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMaxIpGroupNumPerVlan.setStatus(_A)
class _SwL2IGMPSnoopingMulticastVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2IGMPSnoopingMulticastVlanState_Type.__name__=_B
_SwL2IGMPSnoopingMulticastVlanState_Object=MibScalar
swL2IGMPSnoopingMulticastVlanState=_SwL2IGMPSnoopingMulticastVlanState_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,3),_SwL2IGMPSnoopingMulticastVlanState_Type())
swL2IGMPSnoopingMulticastVlanState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPSnoopingMulticastVlanState.setStatus(_A)
_SwL2IGMPCtrlTable_Object=MibTable
swL2IGMPCtrlTable=_SwL2IGMPCtrlTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4))
if mibBuilder.loadTexts:swL2IGMPCtrlTable.setStatus(_A)
_SwL2IGMPCtrlEntry_Object=MibTableRow
swL2IGMPCtrlEntry=_SwL2IGMPCtrlEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1))
swL2IGMPCtrlEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:swL2IGMPCtrlEntry.setStatus(_A)
class _SwL2IGMPCtrlVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2IGMPCtrlVid_Type.__name__=_B
_SwL2IGMPCtrlVid_Object=MibTableColumn
swL2IGMPCtrlVid=_SwL2IGMPCtrlVid_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1,1),_SwL2IGMPCtrlVid_Type())
swL2IGMPCtrlVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPCtrlVid.setStatus(_A)
class _SwL2IGMPQueryInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2IGMPQueryInterval_Type.__name__=_B
_SwL2IGMPQueryInterval_Object=MibTableColumn
swL2IGMPQueryInterval=_SwL2IGMPQueryInterval_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1,2),_SwL2IGMPQueryInterval_Type())
swL2IGMPQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPQueryInterval.setStatus(_A)
class _SwL2IGMPMaxResponseTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_SwL2IGMPMaxResponseTime_Type.__name__=_B
_SwL2IGMPMaxResponseTime_Object=MibTableColumn
swL2IGMPMaxResponseTime=_SwL2IGMPMaxResponseTime_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1,3),_SwL2IGMPMaxResponseTime_Type())
swL2IGMPMaxResponseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMaxResponseTime.setStatus(_A)
class _SwL2IGMPRobustness_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2IGMPRobustness_Type.__name__=_B
_SwL2IGMPRobustness_Object=MibTableColumn
swL2IGMPRobustness=_SwL2IGMPRobustness_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1,4),_SwL2IGMPRobustness_Type())
swL2IGMPRobustness.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRobustness.setStatus(_A)
class _SwL2IGMPLastMemberQueryInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_SwL2IGMPLastMemberQueryInterval_Type.__name__=_B
_SwL2IGMPLastMemberQueryInterval_Object=MibTableColumn
swL2IGMPLastMemberQueryInterval=_SwL2IGMPLastMemberQueryInterval_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1,5),_SwL2IGMPLastMemberQueryInterval_Type())
swL2IGMPLastMemberQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPLastMemberQueryInterval.setStatus(_A)
class _SwL2IGMPHostTimeout_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPHostTimeout_Type.__name__=_B
_SwL2IGMPHostTimeout_Object=MibTableColumn
swL2IGMPHostTimeout=_SwL2IGMPHostTimeout_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1,6),_SwL2IGMPHostTimeout_Type())
swL2IGMPHostTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPHostTimeout.setStatus(_J)
class _SwL2IGMPRouteTimeout_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPRouteTimeout_Type.__name__=_B
_SwL2IGMPRouteTimeout_Object=MibTableColumn
swL2IGMPRouteTimeout=_SwL2IGMPRouteTimeout_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1,7),_SwL2IGMPRouteTimeout_Type())
swL2IGMPRouteTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouteTimeout.setStatus(_J)
class _SwL2IGMPLeaveTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPLeaveTimer_Type.__name__=_B
_SwL2IGMPLeaveTimer_Object=MibTableColumn
swL2IGMPLeaveTimer=_SwL2IGMPLeaveTimer_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1,8),_SwL2IGMPLeaveTimer_Type())
swL2IGMPLeaveTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPLeaveTimer.setStatus(_J)
class _SwL2IGMPQueryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2IGMPQueryState_Type.__name__=_B
_SwL2IGMPQueryState_Object=MibTableColumn
swL2IGMPQueryState=_SwL2IGMPQueryState_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1,9),_SwL2IGMPQueryState_Type())
swL2IGMPQueryState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPQueryState.setStatus(_A)
class _SwL2IGMPCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('querier',2),('non-querier',3)))
_SwL2IGMPCurrentState_Type.__name__=_B
_SwL2IGMPCurrentState_Object=MibTableColumn
swL2IGMPCurrentState=_SwL2IGMPCurrentState_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1,10),_SwL2IGMPCurrentState_Type())
swL2IGMPCurrentState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPCurrentState.setStatus(_A)
class _SwL2IGMPCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_Q,2),(_P,3)))
_SwL2IGMPCtrlState_Type.__name__=_B
_SwL2IGMPCtrlState_Object=MibTableColumn
swL2IGMPCtrlState=_SwL2IGMPCtrlState_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1,11),_SwL2IGMPCtrlState_Type())
swL2IGMPCtrlState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPCtrlState.setStatus(_A)
class _SwL2IGMPFastLeaveState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_Q,2),(_P,3)))
_SwL2IGMPFastLeaveState_Type.__name__=_B
_SwL2IGMPFastLeaveState_Object=MibTableColumn
swL2IGMPFastLeaveState=_SwL2IGMPFastLeaveState_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1,12),_SwL2IGMPFastLeaveState_Type())
swL2IGMPFastLeaveState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPFastLeaveState.setStatus(_A)
class _SwL2IGMPQueryVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_SwL2IGMPQueryVersion_Type.__name__=_B
_SwL2IGMPQueryVersion_Object=MibTableColumn
swL2IGMPQueryVersion=_SwL2IGMPQueryVersion_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1,13),_SwL2IGMPQueryVersion_Type())
swL2IGMPQueryVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPQueryVersion.setStatus(_A)
class _SwL2IGMPRateLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_SwL2IGMPRateLimit_Type.__name__=_B
_SwL2IGMPRateLimit_Object=MibTableColumn
swL2IGMPRateLimit=_SwL2IGMPRateLimit_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1,14),_SwL2IGMPRateLimit_Type())
swL2IGMPRateLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRateLimit.setStatus(_A)
class _SwL2IGMPReportSuppression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2IGMPReportSuppression_Type.__name__=_B
_SwL2IGMPReportSuppression_Object=MibTableColumn
swL2IGMPReportSuppression=_SwL2IGMPReportSuppression_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,4,1,15),_SwL2IGMPReportSuppression_Type())
swL2IGMPReportSuppression.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPReportSuppression.setStatus(_A)
_SwL2IGMPQueryInfoTable_Object=MibTable
swL2IGMPQueryInfoTable=_SwL2IGMPQueryInfoTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,5))
if mibBuilder.loadTexts:swL2IGMPQueryInfoTable.setStatus(_A)
_SwL2IGMPQueryInfoEntry_Object=MibTableRow
swL2IGMPQueryInfoEntry=_SwL2IGMPQueryInfoEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,5,1))
swL2IGMPQueryInfoEntry.setIndexNames((0,_E,_AP))
if mibBuilder.loadTexts:swL2IGMPQueryInfoEntry.setStatus(_A)
class _SwL2IGMPInfoVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2IGMPInfoVid_Type.__name__=_B
_SwL2IGMPInfoVid_Object=MibTableColumn
swL2IGMPInfoVid=_SwL2IGMPInfoVid_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,5,1,1),_SwL2IGMPInfoVid_Type())
swL2IGMPInfoVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPInfoVid.setStatus(_A)
class _SwL2IGMPInfoQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoQueryCount_Type.__name__=_B
_SwL2IGMPInfoQueryCount_Object=MibTableColumn
swL2IGMPInfoQueryCount=_SwL2IGMPInfoQueryCount_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,5,1,2),_SwL2IGMPInfoQueryCount_Type())
swL2IGMPInfoQueryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPInfoQueryCount.setStatus(_J)
class _SwL2IGMPInfoTxQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoTxQueryCount_Type.__name__=_B
_SwL2IGMPInfoTxQueryCount_Object=MibTableColumn
swL2IGMPInfoTxQueryCount=_SwL2IGMPInfoTxQueryCount_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,5,1,3),_SwL2IGMPInfoTxQueryCount_Type())
swL2IGMPInfoTxQueryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPInfoTxQueryCount.setStatus(_J)
_SwL2IGMPQueryIPAddress_Type=IpAddress
_SwL2IGMPQueryIPAddress_Object=MibTableColumn
swL2IGMPQueryIPAddress=_SwL2IGMPQueryIPAddress_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,5,1,4),_SwL2IGMPQueryIPAddress_Type())
swL2IGMPQueryIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPQueryIPAddress.setStatus(_A)
class _SwL2IGMPQueryExpiryTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPQueryExpiryTime_Type.__name__=_B
_SwL2IGMPQueryExpiryTime_Object=MibTableColumn
swL2IGMPQueryExpiryTime=_SwL2IGMPQueryExpiryTime_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,5,1,5),_SwL2IGMPQueryExpiryTime_Type())
swL2IGMPQueryExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPQueryExpiryTime.setStatus(_A)
_SwL2IGMPInfoTable_Object=MibTable
swL2IGMPInfoTable=_SwL2IGMPInfoTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,6))
if mibBuilder.loadTexts:swL2IGMPInfoTable.setStatus(_J)
_SwL2IGMPInfoEntry_Object=MibTableRow
swL2IGMPInfoEntry=_SwL2IGMPInfoEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,6,1))
swL2IGMPInfoEntry.setIndexNames((0,_E,_V),(0,_E,_W))
if mibBuilder.loadTexts:swL2IGMPInfoEntry.setStatus(_J)
class _SwL2IGMPVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2IGMPVid_Type.__name__=_B
_SwL2IGMPVid_Object=MibTableColumn
swL2IGMPVid=_SwL2IGMPVid_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,6,1,1),_SwL2IGMPVid_Type())
swL2IGMPVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVid.setStatus(_J)
_SwL2IGMPGroupIpAddr_Type=IpAddress
_SwL2IGMPGroupIpAddr_Object=MibTableColumn
swL2IGMPGroupIpAddr=_SwL2IGMPGroupIpAddr_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,6,1,2),_SwL2IGMPGroupIpAddr_Type())
swL2IGMPGroupIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPGroupIpAddr.setStatus(_J)
_SwL2IGMPMacAddr_Type=MacAddress
_SwL2IGMPMacAddr_Object=MibTableColumn
swL2IGMPMacAddr=_SwL2IGMPMacAddr_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,6,1,3),_SwL2IGMPMacAddr_Type())
swL2IGMPMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMacAddr.setStatus(_J)
_SwL2IGMPPortMap_Type=PortList
_SwL2IGMPPortMap_Object=MibTableColumn
swL2IGMPPortMap=_SwL2IGMPPortMap_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,6,1,4),_SwL2IGMPPortMap_Type())
swL2IGMPPortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortMap.setStatus(_J)
class _SwL2IGMPIpGroupReportCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPIpGroupReportCount_Type.__name__=_B
_SwL2IGMPIpGroupReportCount_Object=MibTableColumn
swL2IGMPIpGroupReportCount=_SwL2IGMPIpGroupReportCount_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,6,1,5),_SwL2IGMPIpGroupReportCount_Type())
swL2IGMPIpGroupReportCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPIpGroupReportCount.setStatus(_J)
_SwL2IGMPVersion_Type=Integer32
_SwL2IGMPVersion_Object=MibTableColumn
swL2IGMPVersion=_SwL2IGMPVersion_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,6,1,6),_SwL2IGMPVersion_Type())
swL2IGMPVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVersion.setStatus(_J)
class _SwL2IGMPGroupMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('include',1),('exclude',2)))
_SwL2IGMPGroupMode_Type.__name__=_B
_SwL2IGMPGroupMode_Object=MibTableColumn
swL2IGMPGroupMode=_SwL2IGMPGroupMode_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,6,1,7),_SwL2IGMPGroupMode_Type())
swL2IGMPGroupMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPGroupMode.setStatus(_J)
_SwL2IGMPRouterPortTable_Object=MibTable
swL2IGMPRouterPortTable=_SwL2IGMPRouterPortTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,7))
if mibBuilder.loadTexts:swL2IGMPRouterPortTable.setStatus(_A)
_SwL2IGMPRouterPortEntry_Object=MibTableRow
swL2IGMPRouterPortEntry=_SwL2IGMPRouterPortEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,7,1))
swL2IGMPRouterPortEntry.setIndexNames((0,_E,_AQ))
if mibBuilder.loadTexts:swL2IGMPRouterPortEntry.setStatus(_A)
class _SwL2IGMPRouterPortVlanid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2IGMPRouterPortVlanid_Type.__name__=_B
_SwL2IGMPRouterPortVlanid_Object=MibTableColumn
swL2IGMPRouterPortVlanid=_SwL2IGMPRouterPortVlanid_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,7,1,1),_SwL2IGMPRouterPortVlanid_Type())
swL2IGMPRouterPortVlanid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouterPortVlanid.setStatus(_A)
class _SwL2IGMPRouterPortVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2IGMPRouterPortVlanName_Type.__name__=_K
_SwL2IGMPRouterPortVlanName_Object=MibTableColumn
swL2IGMPRouterPortVlanName=_SwL2IGMPRouterPortVlanName_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,7,1,2),_SwL2IGMPRouterPortVlanName_Type())
swL2IGMPRouterPortVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouterPortVlanName.setStatus(_A)
_SwL2IGMPRouterPortStaticPortList_Type=PortList
_SwL2IGMPRouterPortStaticPortList_Object=MibTableColumn
swL2IGMPRouterPortStaticPortList=_SwL2IGMPRouterPortStaticPortList_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,7,1,3),_SwL2IGMPRouterPortStaticPortList_Type())
swL2IGMPRouterPortStaticPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterPortStaticPortList.setStatus(_A)
_SwL2IGMPRouterPortDynamicPortList_Type=PortList
_SwL2IGMPRouterPortDynamicPortList_Object=MibTableColumn
swL2IGMPRouterPortDynamicPortList=_SwL2IGMPRouterPortDynamicPortList_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,7,1,4),_SwL2IGMPRouterPortDynamicPortList_Type())
swL2IGMPRouterPortDynamicPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouterPortDynamicPortList.setStatus(_A)
_SwL2IGMPRouterPortForbiddenPortList_Type=PortList
_SwL2IGMPRouterPortForbiddenPortList_Object=MibTableColumn
swL2IGMPRouterPortForbiddenPortList=_SwL2IGMPRouterPortForbiddenPortList_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,7,1,5),_SwL2IGMPRouterPortForbiddenPortList_Type())
swL2IGMPRouterPortForbiddenPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterPortForbiddenPortList.setStatus(_A)
_SwL2IGMPMulticastVlanTable_Object=MibTable
swL2IGMPMulticastVlanTable=_SwL2IGMPMulticastVlanTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,8))
if mibBuilder.loadTexts:swL2IGMPMulticastVlanTable.setStatus(_A)
_SwL2IGMPMulticastVlanEntry_Object=MibTableRow
swL2IGMPMulticastVlanEntry=_SwL2IGMPMulticastVlanEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,8,1))
swL2IGMPMulticastVlanEntry.setIndexNames((0,_E,_AR))
if mibBuilder.loadTexts:swL2IGMPMulticastVlanEntry.setStatus(_A)
class _SwL2IGMPMulticastVlanid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_SwL2IGMPMulticastVlanid_Type.__name__=_B
_SwL2IGMPMulticastVlanid_Object=MibTableColumn
swL2IGMPMulticastVlanid=_SwL2IGMPMulticastVlanid_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,8,1,1),_SwL2IGMPMulticastVlanid_Type())
swL2IGMPMulticastVlanid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanid.setStatus(_A)
class _SwL2IGMPMulticastVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2IGMPMulticastVlanName_Type.__name__=_K
_SwL2IGMPMulticastVlanName_Object=MibTableColumn
swL2IGMPMulticastVlanName=_SwL2IGMPMulticastVlanName_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,8,1,2),_SwL2IGMPMulticastVlanName_Type())
swL2IGMPMulticastVlanName.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanName.setStatus(_A)
_SwL2IGMPMulticastVlanSourcePort_Type=PortList
_SwL2IGMPMulticastVlanSourcePort_Object=MibTableColumn
swL2IGMPMulticastVlanSourcePort=_SwL2IGMPMulticastVlanSourcePort_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,8,1,3),_SwL2IGMPMulticastVlanSourcePort_Type())
swL2IGMPMulticastVlanSourcePort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanSourcePort.setStatus(_A)
_SwL2IGMPMulticastVlanMemberPort_Type=PortList
_SwL2IGMPMulticastVlanMemberPort_Object=MibTableColumn
swL2IGMPMulticastVlanMemberPort=_SwL2IGMPMulticastVlanMemberPort_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,8,1,4),_SwL2IGMPMulticastVlanMemberPort_Type())
swL2IGMPMulticastVlanMemberPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanMemberPort.setStatus(_A)
_SwL2IGMPMulticastVlanTagMemberPort_Type=PortList
_SwL2IGMPMulticastVlanTagMemberPort_Object=MibTableColumn
swL2IGMPMulticastVlanTagMemberPort=_SwL2IGMPMulticastVlanTagMemberPort_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,8,1,5),_SwL2IGMPMulticastVlanTagMemberPort_Type())
swL2IGMPMulticastVlanTagMemberPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanTagMemberPort.setStatus(_A)
class _SwL2IGMPMulticastVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2IGMPMulticastVlanState_Type.__name__=_B
_SwL2IGMPMulticastVlanState_Object=MibTableColumn
swL2IGMPMulticastVlanState=_SwL2IGMPMulticastVlanState_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,8,1,6),_SwL2IGMPMulticastVlanState_Type())
swL2IGMPMulticastVlanState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanState.setStatus(_A)
_SwL2IGMPMulticastVlanReplaceSourceIp_Type=IpAddress
_SwL2IGMPMulticastVlanReplaceSourceIp_Object=MibTableColumn
swL2IGMPMulticastVlanReplaceSourceIp=_SwL2IGMPMulticastVlanReplaceSourceIp_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,8,1,7),_SwL2IGMPMulticastVlanReplaceSourceIp_Type())
swL2IGMPMulticastVlanReplaceSourceIp.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanReplaceSourceIp.setStatus(_A)
_SwL2IGMPMulticastVlanRowStatus_Type=RowStatus
_SwL2IGMPMulticastVlanRowStatus_Object=MibTableColumn
swL2IGMPMulticastVlanRowStatus=_SwL2IGMPMulticastVlanRowStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,8,1,8),_SwL2IGMPMulticastVlanRowStatus_Type())
swL2IGMPMulticastVlanRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanRowStatus.setStatus(_A)
class _SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_N,2)))
_SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Type.__name__=_B
_SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Object=MibTableColumn
swL2IGMPMulticastVlanRemoveAllMcastAddrListAction=_SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,8,1,9),_SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Type())
swL2IGMPMulticastVlanRemoveAllMcastAddrListAction.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanRemoveAllMcastAddrListAction.setStatus(_A)
_SwL2IGMPMulticastVlanUntagSourcePort_Type=PortList
_SwL2IGMPMulticastVlanUntagSourcePort_Object=MibTableColumn
swL2IGMPMulticastVlanUntagSourcePort=_SwL2IGMPMulticastVlanUntagSourcePort_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,8,1,10),_SwL2IGMPMulticastVlanUntagSourcePort_Type())
swL2IGMPMulticastVlanUntagSourcePort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanUntagSourcePort.setStatus(_A)
class _SwL2IGMPMulticastVlanRemapPriority_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_SwL2IGMPMulticastVlanRemapPriority_Type.__name__=_B
_SwL2IGMPMulticastVlanRemapPriority_Object=MibTableColumn
swL2IGMPMulticastVlanRemapPriority=_SwL2IGMPMulticastVlanRemapPriority_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,8,1,11),_SwL2IGMPMulticastVlanRemapPriority_Type())
swL2IGMPMulticastVlanRemapPriority.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanRemapPriority.setStatus(_A)
class _SwL2IGMPMulticastVlanReplacePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_SwL2IGMPMulticastVlanReplacePriority_Type.__name__=_B
_SwL2IGMPMulticastVlanReplacePriority_Object=MibTableColumn
swL2IGMPMulticastVlanReplacePriority=_SwL2IGMPMulticastVlanReplacePriority_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,8,1,12),_SwL2IGMPMulticastVlanReplacePriority_Type())
swL2IGMPMulticastVlanReplacePriority.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanReplacePriority.setStatus(_A)
_SwL2IGMPMulticastVlanGroupTable_Object=MibTable
swL2IGMPMulticastVlanGroupTable=_SwL2IGMPMulticastVlanGroupTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,9))
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupTable.setStatus(_A)
_SwL2IGMPMulticastVlanGroupEntry_Object=MibTableRow
swL2IGMPMulticastVlanGroupEntry=_SwL2IGMPMulticastVlanGroupEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,9,1))
swL2IGMPMulticastVlanGroupEntry.setIndexNames((0,_E,_AS),(0,_E,_AT),(0,_E,_AU))
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupEntry.setStatus(_A)
class _SwL2IGMPMulticastVlanGroupVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2IGMPMulticastVlanGroupVid_Type.__name__=_B
_SwL2IGMPMulticastVlanGroupVid_Object=MibTableColumn
swL2IGMPMulticastVlanGroupVid=_SwL2IGMPMulticastVlanGroupVid_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,9,1,1),_SwL2IGMPMulticastVlanGroupVid_Type())
swL2IGMPMulticastVlanGroupVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupVid.setStatus(_A)
_SwL2IGMPMulticastVlanGroupFromIp_Type=IpAddress
_SwL2IGMPMulticastVlanGroupFromIp_Object=MibTableColumn
swL2IGMPMulticastVlanGroupFromIp=_SwL2IGMPMulticastVlanGroupFromIp_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,9,1,2),_SwL2IGMPMulticastVlanGroupFromIp_Type())
swL2IGMPMulticastVlanGroupFromIp.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupFromIp.setStatus(_A)
_SwL2IGMPMulticastVlanGroupToIp_Type=IpAddress
_SwL2IGMPMulticastVlanGroupToIp_Object=MibTableColumn
swL2IGMPMulticastVlanGroupToIp=_SwL2IGMPMulticastVlanGroupToIp_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,9,1,3),_SwL2IGMPMulticastVlanGroupToIp_Type())
swL2IGMPMulticastVlanGroupToIp.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupToIp.setStatus(_A)
_SwL2IGMPMulticastVlanGroupStatus_Type=RowStatus
_SwL2IGMPMulticastVlanGroupStatus_Object=MibTableColumn
swL2IGMPMulticastVlanGroupStatus=_SwL2IGMPMulticastVlanGroupStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,9,1,4),_SwL2IGMPMulticastVlanGroupStatus_Type())
swL2IGMPMulticastVlanGroupStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupStatus.setStatus(_A)
_SwL2IGMPv3Table_Object=MibTable
swL2IGMPv3Table=_SwL2IGMPv3Table_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,10))
if mibBuilder.loadTexts:swL2IGMPv3Table.setStatus(_A)
_SwL2IGMPv3Entry_Object=MibTableRow
swL2IGMPv3Entry=_SwL2IGMPv3Entry_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,10,1))
swL2IGMPv3Entry.setIndexNames((0,_E,_V),(0,_E,_W),(0,_E,_AV))
if mibBuilder.loadTexts:swL2IGMPv3Entry.setStatus(_A)
_SwL2IGMPv3SourceIPAddr_Type=IpAddress
_SwL2IGMPv3SourceIPAddr_Object=MibTableColumn
swL2IGMPv3SourceIPAddr=_SwL2IGMPv3SourceIPAddr_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,10,1,1),_SwL2IGMPv3SourceIPAddr_Type())
swL2IGMPv3SourceIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPv3SourceIPAddr.setStatus(_A)
class _SwL2IGMPv3Forwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2IGMPv3Forwarding_Type.__name__=_B
_SwL2IGMPv3Forwarding_Object=MibTableColumn
swL2IGMPv3Forwarding=_SwL2IGMPv3Forwarding_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,10,1,2),_SwL2IGMPv3Forwarding_Type())
swL2IGMPv3Forwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPv3Forwarding.setStatus(_A)
_SwL2IGMPv3ExpireTimer_Type=Integer32
_SwL2IGMPv3ExpireTimer_Object=MibTableColumn
swL2IGMPv3ExpireTimer=_SwL2IGMPv3ExpireTimer_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,10,1,3),_SwL2IGMPv3ExpireTimer_Type())
swL2IGMPv3ExpireTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPv3ExpireTimer.setStatus(_A)
_SwIGMPSnoopingGroupTable_Object=MibTable
swIGMPSnoopingGroupTable=_SwIGMPSnoopingGroupTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,11))
if mibBuilder.loadTexts:swIGMPSnoopingGroupTable.setStatus(_A)
_SwIGMPSnoopingGroupEntry_Object=MibTableRow
swIGMPSnoopingGroupEntry=_SwIGMPSnoopingGroupEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,11,1))
swIGMPSnoopingGroupEntry.setIndexNames((0,_E,_AW),(0,_E,_AX),(0,_E,_AY))
if mibBuilder.loadTexts:swIGMPSnoopingGroupEntry.setStatus(_A)
class _SwIGMPSnoopingGroupVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwIGMPSnoopingGroupVid_Type.__name__=_B
_SwIGMPSnoopingGroupVid_Object=MibTableColumn
swIGMPSnoopingGroupVid=_SwIGMPSnoopingGroupVid_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,11,1,1),_SwIGMPSnoopingGroupVid_Type())
swIGMPSnoopingGroupVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPSnoopingGroupVid.setStatus(_A)
_SwIGMPSnoopingGroupGroupAddr_Type=IpAddress
_SwIGMPSnoopingGroupGroupAddr_Object=MibTableColumn
swIGMPSnoopingGroupGroupAddr=_SwIGMPSnoopingGroupGroupAddr_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,11,1,2),_SwIGMPSnoopingGroupGroupAddr_Type())
swIGMPSnoopingGroupGroupAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPSnoopingGroupGroupAddr.setStatus(_A)
_SwIGMPSnoopingGroupSourceAddr_Type=IpAddress
_SwIGMPSnoopingGroupSourceAddr_Object=MibTableColumn
swIGMPSnoopingGroupSourceAddr=_SwIGMPSnoopingGroupSourceAddr_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,11,1,3),_SwIGMPSnoopingGroupSourceAddr_Type())
swIGMPSnoopingGroupSourceAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPSnoopingGroupSourceAddr.setStatus(_A)
_SwIGMPSnoopingGroupIncludePortMap_Type=PortList
_SwIGMPSnoopingGroupIncludePortMap_Object=MibTableColumn
swIGMPSnoopingGroupIncludePortMap=_SwIGMPSnoopingGroupIncludePortMap_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,11,1,4),_SwIGMPSnoopingGroupIncludePortMap_Type())
swIGMPSnoopingGroupIncludePortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPSnoopingGroupIncludePortMap.setStatus(_A)
_SwIGMPSnoopingGroupExcludePortMap_Type=PortList
_SwIGMPSnoopingGroupExcludePortMap_Object=MibTableColumn
swIGMPSnoopingGroupExcludePortMap=_SwIGMPSnoopingGroupExcludePortMap_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,11,1,5),_SwIGMPSnoopingGroupExcludePortMap_Type())
swIGMPSnoopingGroupExcludePortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPSnoopingGroupExcludePortMap.setStatus(_A)
_SwIGMPSnoopingGroupReportCount_Type=Integer32
_SwIGMPSnoopingGroupReportCount_Object=MibTableColumn
swIGMPSnoopingGroupReportCount=_SwIGMPSnoopingGroupReportCount_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,11,1,6),_SwIGMPSnoopingGroupReportCount_Type())
swIGMPSnoopingGroupReportCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPSnoopingGroupReportCount.setStatus(_A)
_SwIGMPSnoopingGroupUpTime_Type=TimeTicks
_SwIGMPSnoopingGroupUpTime_Object=MibTableColumn
swIGMPSnoopingGroupUpTime=_SwIGMPSnoopingGroupUpTime_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,11,1,7),_SwIGMPSnoopingGroupUpTime_Type())
swIGMPSnoopingGroupUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPSnoopingGroupUpTime.setStatus(_A)
_SwIGMPSnoopingGroupExpiryTime_Type=TimeTicks
_SwIGMPSnoopingGroupExpiryTime_Object=MibTableColumn
swIGMPSnoopingGroupExpiryTime=_SwIGMPSnoopingGroupExpiryTime_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,11,1,8),_SwIGMPSnoopingGroupExpiryTime_Type())
swIGMPSnoopingGroupExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPSnoopingGroupExpiryTime.setStatus(_A)
_SwIGMPSnoopingGroupRouterPorts_Type=PortList
_SwIGMPSnoopingGroupRouterPorts_Object=MibTableColumn
swIGMPSnoopingGroupRouterPorts=_SwIGMPSnoopingGroupRouterPorts_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,11,1,9),_SwIGMPSnoopingGroupRouterPorts_Type())
swIGMPSnoopingGroupRouterPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPSnoopingGroupRouterPorts.setStatus(_A)
_SwIGMPSnoopingGroupStaticMemberPorts_Type=PortList
_SwIGMPSnoopingGroupStaticMemberPorts_Object=MibTableColumn
swIGMPSnoopingGroupStaticMemberPorts=_SwIGMPSnoopingGroupStaticMemberPorts_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,11,1,10),_SwIGMPSnoopingGroupStaticMemberPorts_Type())
swIGMPSnoopingGroupStaticMemberPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPSnoopingGroupStaticMemberPorts.setStatus(_A)
_SwL2IGMPDynIpMultMgmt_ObjectIdentity=ObjectIdentity
swL2IGMPDynIpMultMgmt=_SwL2IGMPDynIpMultMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,11,12))
_SwL2IGMPDynIPMultMaxEntry_Type=Integer32
_SwL2IGMPDynIPMultMaxEntry_Object=MibScalar
swL2IGMPDynIPMultMaxEntry=_SwL2IGMPDynIPMultMaxEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,12,1),_SwL2IGMPDynIPMultMaxEntry_Type())
swL2IGMPDynIPMultMaxEntry.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPDynIPMultMaxEntry.setStatus(_A)
_SwL2IGMPSnoopingClearDynIpMult_ObjectIdentity=ObjectIdentity
swL2IGMPSnoopingClearDynIpMult=_SwL2IGMPSnoopingClearDynIpMult_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,11,12,2))
_SwL2IGMPSnoopingClearDynIpMultVID_Type=VlanId
_SwL2IGMPSnoopingClearDynIpMultVID_Object=MibScalar
swL2IGMPSnoopingClearDynIpMultVID=_SwL2IGMPSnoopingClearDynIpMultVID_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,12,2,1),_SwL2IGMPSnoopingClearDynIpMultVID_Type())
swL2IGMPSnoopingClearDynIpMultVID.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPSnoopingClearDynIpMultVID.setStatus(_A)
_SwL2IGMPSnoopingClearDynIpMultIP_Type=IpAddress
_SwL2IGMPSnoopingClearDynIpMultIP_Object=MibScalar
swL2IGMPSnoopingClearDynIpMultIP=_SwL2IGMPSnoopingClearDynIpMultIP_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,12,2,2),_SwL2IGMPSnoopingClearDynIpMultIP_Type())
swL2IGMPSnoopingClearDynIpMultIP.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPSnoopingClearDynIpMultIP.setStatus(_A)
class _SwL2IGMPSnoopingClearDynIpMultAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('all',1),('vlan',2),('group',3),(_H,4)))
_SwL2IGMPSnoopingClearDynIpMultAction_Type.__name__=_B
_SwL2IGMPSnoopingClearDynIpMultAction_Object=MibScalar
swL2IGMPSnoopingClearDynIpMultAction=_SwL2IGMPSnoopingClearDynIpMultAction_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,12,2,3),_SwL2IGMPSnoopingClearDynIpMultAction_Type())
swL2IGMPSnoopingClearDynIpMultAction.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPSnoopingClearDynIpMultAction.setStatus(_A)
_SwL2IGMPDynIPMultCtrlTable_Object=MibTable
swL2IGMPDynIPMultCtrlTable=_SwL2IGMPDynIPMultCtrlTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,12,3))
if mibBuilder.loadTexts:swL2IGMPDynIPMultCtrlTable.setStatus(_A)
_SwL2IGMPDynIPMultCtrlEntry_Object=MibTableRow
swL2IGMPDynIPMultCtrlEntry=_SwL2IGMPDynIPMultCtrlEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,12,3,1))
swL2IGMPDynIPMultCtrlEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:swL2IGMPDynIPMultCtrlEntry.setStatus(_A)
class _SwL2IGMPDynIPMultVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2IGMPDynIPMultVlanState_Type.__name__=_B
_SwL2IGMPDynIPMultVlanState_Object=MibTableColumn
swL2IGMPDynIPMultVlanState=_SwL2IGMPDynIPMultVlanState_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,12,3,1,1),_SwL2IGMPDynIPMultVlanState_Type())
swL2IGMPDynIPMultVlanState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPDynIPMultVlanState.setStatus(_A)
class _SwL2IGMPDynIPMultVlanAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2IGMPDynIPMultVlanAge_Type.__name__=_B
_SwL2IGMPDynIPMultVlanAge_Object=MibTableColumn
swL2IGMPDynIPMultVlanAge=_SwL2IGMPDynIPMultVlanAge_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,12,3,1,2),_SwL2IGMPDynIPMultVlanAge_Type())
swL2IGMPDynIPMultVlanAge.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPDynIPMultVlanAge.setStatus(_A)
class _SwL2IGMPDynIPMultGroupExpiryTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPDynIPMultGroupExpiryTime_Type.__name__=_B
_SwL2IGMPDynIPMultGroupExpiryTime_Object=MibTableColumn
swL2IGMPDynIPMultGroupExpiryTime=_SwL2IGMPDynIPMultGroupExpiryTime_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,12,3,1,3),_SwL2IGMPDynIPMultGroupExpiryTime_Type())
swL2IGMPDynIPMultGroupExpiryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPDynIPMultGroupExpiryTime.setStatus(_A)
_SwL2IGMPAccessAuthTable_Object=MibTable
swL2IGMPAccessAuthTable=_SwL2IGMPAccessAuthTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,13))
if mibBuilder.loadTexts:swL2IGMPAccessAuthTable.setStatus(_A)
_SwL2IGMPAccessAuthEntry_Object=MibTableRow
swL2IGMPAccessAuthEntry=_SwL2IGMPAccessAuthEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,13,1))
swL2IGMPAccessAuthEntry.setIndexNames((0,_E,_AZ))
if mibBuilder.loadTexts:swL2IGMPAccessAuthEntry.setStatus(_A)
_SwL2IGMPAccessAuthPort_Type=Integer32
_SwL2IGMPAccessAuthPort_Object=MibTableColumn
swL2IGMPAccessAuthPort=_SwL2IGMPAccessAuthPort_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,13,1,1),_SwL2IGMPAccessAuthPort_Type())
swL2IGMPAccessAuthPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPAccessAuthPort.setStatus(_A)
class _SwL2IGMPAccessAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2IGMPAccessAuthState_Type.__name__=_B
_SwL2IGMPAccessAuthState_Object=MibTableColumn
swL2IGMPAccessAuthState=_SwL2IGMPAccessAuthState_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,13,1,2),_SwL2IGMPAccessAuthState_Type())
swL2IGMPAccessAuthState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPAccessAuthState.setStatus(_A)
_SwL2IGMPCountrInfoMgmt_ObjectIdentity=ObjectIdentity
swL2IGMPCountrInfoMgmt=_SwL2IGMPCountrInfoMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,11,14))
class _SwL2IGMPSnoopingClearStatisticsCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_N,2)))
_SwL2IGMPSnoopingClearStatisticsCounter_Type.__name__=_B
_SwL2IGMPSnoopingClearStatisticsCounter_Object=MibScalar
swL2IGMPSnoopingClearStatisticsCounter=_SwL2IGMPSnoopingClearStatisticsCounter_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,1),_SwL2IGMPSnoopingClearStatisticsCounter_Type())
swL2IGMPSnoopingClearStatisticsCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPSnoopingClearStatisticsCounter.setStatus(_A)
_SwL2IGMPVlanCounterInfoTable_Object=MibTable
swL2IGMPVlanCounterInfoTable=_SwL2IGMPVlanCounterInfoTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2))
if mibBuilder.loadTexts:swL2IGMPVlanCounterInfoTable.setStatus(_A)
_SwL2IGMPVlanCounterInfoEntry_Object=MibTableRow
swL2IGMPVlanCounterInfoEntry=_SwL2IGMPVlanCounterInfoEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1))
swL2IGMPVlanCounterInfoEntry.setIndexNames((0,_E,_Aa))
if mibBuilder.loadTexts:swL2IGMPVlanCounterInfoEntry.setStatus(_A)
class _SwL2IGMPVlanCounterInfoVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2IGMPVlanCounterInfoVid_Type.__name__=_B
_SwL2IGMPVlanCounterInfoVid_Object=MibTableColumn
swL2IGMPVlanCounterInfoVid=_SwL2IGMPVlanCounterInfoVid_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,1),_SwL2IGMPVlanCounterInfoVid_Type())
swL2IGMPVlanCounterInfoVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanCounterInfoVid.setStatus(_A)
class _SwL2IGMPVlanCounterGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPVlanCounterGroupNumber_Type.__name__=_B
_SwL2IGMPVlanCounterGroupNumber_Object=MibTableColumn
swL2IGMPVlanCounterGroupNumber=_SwL2IGMPVlanCounterGroupNumber_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,2),_SwL2IGMPVlanCounterGroupNumber_Type())
swL2IGMPVlanCounterGroupNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanCounterGroupNumber.setStatus(_A)
_SwL2IGMPVlanQueryCountV1_Type=Counter32
_SwL2IGMPVlanQueryCountV1_Object=MibTableColumn
swL2IGMPVlanQueryCountV1=_SwL2IGMPVlanQueryCountV1_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,3),_SwL2IGMPVlanQueryCountV1_Type())
swL2IGMPVlanQueryCountV1.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanQueryCountV1.setStatus(_A)
_SwL2IGMPVlanQueryCountV2_Type=Counter32
_SwL2IGMPVlanQueryCountV2_Object=MibTableColumn
swL2IGMPVlanQueryCountV2=_SwL2IGMPVlanQueryCountV2_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,4),_SwL2IGMPVlanQueryCountV2_Type())
swL2IGMPVlanQueryCountV2.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanQueryCountV2.setStatus(_A)
_SwL2IGMPVlanQueryCountV3_Type=Counter32
_SwL2IGMPVlanQueryCountV3_Object=MibTableColumn
swL2IGMPVlanQueryCountV3=_SwL2IGMPVlanQueryCountV3_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,5),_SwL2IGMPVlanQueryCountV3_Type())
swL2IGMPVlanQueryCountV3.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanQueryCountV3.setStatus(_A)
_SwL2IGMPVlanDropQueryCount_Type=Counter32
_SwL2IGMPVlanDropQueryCount_Object=MibTableColumn
swL2IGMPVlanDropQueryCount=_SwL2IGMPVlanDropQueryCount_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,6),_SwL2IGMPVlanDropQueryCount_Type())
swL2IGMPVlanDropQueryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanDropQueryCount.setStatus(_A)
_SwL2IGMPVlanReportCountV1_Type=Counter32
_SwL2IGMPVlanReportCountV1_Object=MibTableColumn
swL2IGMPVlanReportCountV1=_SwL2IGMPVlanReportCountV1_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,7),_SwL2IGMPVlanReportCountV1_Type())
swL2IGMPVlanReportCountV1.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanReportCountV1.setStatus(_A)
_SwL2IGMPVlanReportCountV2_Type=Counter32
_SwL2IGMPVlanReportCountV2_Object=MibTableColumn
swL2IGMPVlanReportCountV2=_SwL2IGMPVlanReportCountV2_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,8),_SwL2IGMPVlanReportCountV2_Type())
swL2IGMPVlanReportCountV2.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanReportCountV2.setStatus(_A)
_SwL2IGMPVlanReportCountV3_Type=Counter32
_SwL2IGMPVlanReportCountV3_Object=MibTableColumn
swL2IGMPVlanReportCountV3=_SwL2IGMPVlanReportCountV3_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,9),_SwL2IGMPVlanReportCountV3_Type())
swL2IGMPVlanReportCountV3.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanReportCountV3.setStatus(_A)
_SwL2IGMPVlanLeaveCountV2_Type=Counter32
_SwL2IGMPVlanLeaveCountV2_Object=MibTableColumn
swL2IGMPVlanLeaveCountV2=_SwL2IGMPVlanLeaveCountV2_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,10),_SwL2IGMPVlanLeaveCountV2_Type())
swL2IGMPVlanLeaveCountV2.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanLeaveCountV2.setStatus(_A)
_SwL2IGMPVlanDropedReportAndLeaveCount_Type=Counter32
_SwL2IGMPVlanDropedReportAndLeaveCount_Object=MibTableColumn
swL2IGMPVlanDropedReportAndLeaveCount=_SwL2IGMPVlanDropedReportAndLeaveCount_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,11),_SwL2IGMPVlanDropedReportAndLeaveCount_Type())
swL2IGMPVlanDropedReportAndLeaveCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanDropedReportAndLeaveCount.setStatus(_A)
_SwL2IGMPVlanDroppedByMaxGroupLimitation_Type=Counter32
_SwL2IGMPVlanDroppedByMaxGroupLimitation_Object=MibTableColumn
swL2IGMPVlanDroppedByMaxGroupLimitation=_SwL2IGMPVlanDroppedByMaxGroupLimitation_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,12),_SwL2IGMPVlanDroppedByMaxGroupLimitation_Type())
swL2IGMPVlanDroppedByMaxGroupLimitation.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanDroppedByMaxGroupLimitation.setStatus(_A)
_SwL2IGMPVlanDroppedByGroupFilter_Type=Counter32
_SwL2IGMPVlanDroppedByGroupFilter_Object=MibTableColumn
swL2IGMPVlanDroppedByGroupFilter=_SwL2IGMPVlanDroppedByGroupFilter_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,13),_SwL2IGMPVlanDroppedByGroupFilter_Type())
swL2IGMPVlanDroppedByGroupFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanDroppedByGroupFilter.setStatus(_A)
_SwL2IGMPVlanTxQueryCountV1_Type=Counter32
_SwL2IGMPVlanTxQueryCountV1_Object=MibTableColumn
swL2IGMPVlanTxQueryCountV1=_SwL2IGMPVlanTxQueryCountV1_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,14),_SwL2IGMPVlanTxQueryCountV1_Type())
swL2IGMPVlanTxQueryCountV1.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanTxQueryCountV1.setStatus(_A)
_SwL2IGMPVlanTxQueryCountV2_Type=Counter32
_SwL2IGMPVlanTxQueryCountV2_Object=MibTableColumn
swL2IGMPVlanTxQueryCountV2=_SwL2IGMPVlanTxQueryCountV2_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,15),_SwL2IGMPVlanTxQueryCountV2_Type())
swL2IGMPVlanTxQueryCountV2.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanTxQueryCountV2.setStatus(_A)
_SwL2IGMPVlanTxQueryCountV3_Type=Counter32
_SwL2IGMPVlanTxQueryCountV3_Object=MibTableColumn
swL2IGMPVlanTxQueryCountV3=_SwL2IGMPVlanTxQueryCountV3_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,16),_SwL2IGMPVlanTxQueryCountV3_Type())
swL2IGMPVlanTxQueryCountV3.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanTxQueryCountV3.setStatus(_A)
_SwL2IGMPVlanTxReportCountV1_Type=Counter32
_SwL2IGMPVlanTxReportCountV1_Object=MibTableColumn
swL2IGMPVlanTxReportCountV1=_SwL2IGMPVlanTxReportCountV1_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,17),_SwL2IGMPVlanTxReportCountV1_Type())
swL2IGMPVlanTxReportCountV1.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanTxReportCountV1.setStatus(_A)
_SwL2IGMPVlanTxReportCountV2_Type=Counter32
_SwL2IGMPVlanTxReportCountV2_Object=MibTableColumn
swL2IGMPVlanTxReportCountV2=_SwL2IGMPVlanTxReportCountV2_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,18),_SwL2IGMPVlanTxReportCountV2_Type())
swL2IGMPVlanTxReportCountV2.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanTxReportCountV2.setStatus(_A)
_SwL2IGMPVlanTxReportCountV3_Type=Counter32
_SwL2IGMPVlanTxReportCountV3_Object=MibTableColumn
swL2IGMPVlanTxReportCountV3=_SwL2IGMPVlanTxReportCountV3_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,19),_SwL2IGMPVlanTxReportCountV3_Type())
swL2IGMPVlanTxReportCountV3.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanTxReportCountV3.setStatus(_A)
_SwL2IGMPVlanTxLeaveCountV2_Type=Counter32
_SwL2IGMPVlanTxLeaveCountV2_Object=MibTableColumn
swL2IGMPVlanTxLeaveCountV2=_SwL2IGMPVlanTxLeaveCountV2_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,2,1,20),_SwL2IGMPVlanTxLeaveCountV2_Type())
swL2IGMPVlanTxLeaveCountV2.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVlanTxLeaveCountV2.setStatus(_A)
_SwL2IGMPPortCounterInfoTable_Object=MibTable
swL2IGMPPortCounterInfoTable=_SwL2IGMPPortCounterInfoTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3))
if mibBuilder.loadTexts:swL2IGMPPortCounterInfoTable.setStatus(_A)
_SwL2IGMPPortCounterInfoEntry_Object=MibTableRow
swL2IGMPPortCounterInfoEntry=_SwL2IGMPPortCounterInfoEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1))
swL2IGMPPortCounterInfoEntry.setIndexNames((0,_E,_Ab))
if mibBuilder.loadTexts:swL2IGMPPortCounterInfoEntry.setStatus(_A)
class _SwL2IGMPPortCounterInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPPortCounterInfoIndex_Type.__name__=_B
_SwL2IGMPPortCounterInfoIndex_Object=MibTableColumn
swL2IGMPPortCounterInfoIndex=_SwL2IGMPPortCounterInfoIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,1),_SwL2IGMPPortCounterInfoIndex_Type())
swL2IGMPPortCounterInfoIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortCounterInfoIndex.setStatus(_A)
class _SwL2IGMPPortCounterGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPPortCounterGroupNumber_Type.__name__=_B
_SwL2IGMPPortCounterGroupNumber_Object=MibTableColumn
swL2IGMPPortCounterGroupNumber=_SwL2IGMPPortCounterGroupNumber_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,2),_SwL2IGMPPortCounterGroupNumber_Type())
swL2IGMPPortCounterGroupNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortCounterGroupNumber.setStatus(_A)
_SwL2IGMPPortQueryCountV1_Type=Counter32
_SwL2IGMPPortQueryCountV1_Object=MibTableColumn
swL2IGMPPortQueryCountV1=_SwL2IGMPPortQueryCountV1_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,3),_SwL2IGMPPortQueryCountV1_Type())
swL2IGMPPortQueryCountV1.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortQueryCountV1.setStatus(_A)
_SwL2IGMPPortQueryCountV2_Type=Counter32
_SwL2IGMPPortQueryCountV2_Object=MibTableColumn
swL2IGMPPortQueryCountV2=_SwL2IGMPPortQueryCountV2_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,4),_SwL2IGMPPortQueryCountV2_Type())
swL2IGMPPortQueryCountV2.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortQueryCountV2.setStatus(_A)
_SwL2IGMPPortQueryCountV3_Type=Counter32
_SwL2IGMPPortQueryCountV3_Object=MibTableColumn
swL2IGMPPortQueryCountV3=_SwL2IGMPPortQueryCountV3_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,5),_SwL2IGMPPortQueryCountV3_Type())
swL2IGMPPortQueryCountV3.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortQueryCountV3.setStatus(_A)
_SwL2IGMPPortDropQueryCount_Type=Counter32
_SwL2IGMPPortDropQueryCount_Object=MibTableColumn
swL2IGMPPortDropQueryCount=_SwL2IGMPPortDropQueryCount_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,6),_SwL2IGMPPortDropQueryCount_Type())
swL2IGMPPortDropQueryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortDropQueryCount.setStatus(_A)
_SwL2IGMPPortReportCountV1_Type=Counter32
_SwL2IGMPPortReportCountV1_Object=MibTableColumn
swL2IGMPPortReportCountV1=_SwL2IGMPPortReportCountV1_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,7),_SwL2IGMPPortReportCountV1_Type())
swL2IGMPPortReportCountV1.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortReportCountV1.setStatus(_A)
_SwL2IGMPPortReportCountV2_Type=Counter32
_SwL2IGMPPortReportCountV2_Object=MibTableColumn
swL2IGMPPortReportCountV2=_SwL2IGMPPortReportCountV2_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,8),_SwL2IGMPPortReportCountV2_Type())
swL2IGMPPortReportCountV2.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortReportCountV2.setStatus(_A)
_SwL2IGMPPortReportCountV3_Type=Counter32
_SwL2IGMPPortReportCountV3_Object=MibTableColumn
swL2IGMPPortReportCountV3=_SwL2IGMPPortReportCountV3_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,9),_SwL2IGMPPortReportCountV3_Type())
swL2IGMPPortReportCountV3.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortReportCountV3.setStatus(_A)
_SwL2IGMPPortLeaveCountV2_Type=Counter32
_SwL2IGMPPortLeaveCountV2_Object=MibTableColumn
swL2IGMPPortLeaveCountV2=_SwL2IGMPPortLeaveCountV2_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,10),_SwL2IGMPPortLeaveCountV2_Type())
swL2IGMPPortLeaveCountV2.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortLeaveCountV2.setStatus(_A)
_SwL2IGMPPortDropedReportAndLeaveCount_Type=Counter32
_SwL2IGMPPortDropedReportAndLeaveCount_Object=MibTableColumn
swL2IGMPPortDropedReportAndLeaveCount=_SwL2IGMPPortDropedReportAndLeaveCount_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,11),_SwL2IGMPPortDropedReportAndLeaveCount_Type())
swL2IGMPPortDropedReportAndLeaveCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortDropedReportAndLeaveCount.setStatus(_A)
_SwL2IGMPPortDroppedByMaxGroupLimitation_Type=Counter32
_SwL2IGMPPortDroppedByMaxGroupLimitation_Object=MibTableColumn
swL2IGMPPortDroppedByMaxGroupLimitation=_SwL2IGMPPortDroppedByMaxGroupLimitation_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,12),_SwL2IGMPPortDroppedByMaxGroupLimitation_Type())
swL2IGMPPortDroppedByMaxGroupLimitation.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortDroppedByMaxGroupLimitation.setStatus(_A)
_SwL2IGMPPortDroppedByGroupFilter_Type=Counter32
_SwL2IGMPPortDroppedByGroupFilter_Object=MibTableColumn
swL2IGMPPortDroppedByGroupFilter=_SwL2IGMPPortDroppedByGroupFilter_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,13),_SwL2IGMPPortDroppedByGroupFilter_Type())
swL2IGMPPortDroppedByGroupFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortDroppedByGroupFilter.setStatus(_A)
_SwL2IGMPPortTxQueryCountV1_Type=Counter32
_SwL2IGMPPortTxQueryCountV1_Object=MibTableColumn
swL2IGMPPortTxQueryCountV1=_SwL2IGMPPortTxQueryCountV1_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,14),_SwL2IGMPPortTxQueryCountV1_Type())
swL2IGMPPortTxQueryCountV1.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortTxQueryCountV1.setStatus(_A)
_SwL2IGMPPortTxQueryCountV2_Type=Counter32
_SwL2IGMPPortTxQueryCountV2_Object=MibTableColumn
swL2IGMPPortTxQueryCountV2=_SwL2IGMPPortTxQueryCountV2_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,15),_SwL2IGMPPortTxQueryCountV2_Type())
swL2IGMPPortTxQueryCountV2.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortTxQueryCountV2.setStatus(_A)
_SwL2IGMPPortTxQueryCountV3_Type=Counter32
_SwL2IGMPPortTxQueryCountV3_Object=MibTableColumn
swL2IGMPPortTxQueryCountV3=_SwL2IGMPPortTxQueryCountV3_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,16),_SwL2IGMPPortTxQueryCountV3_Type())
swL2IGMPPortTxQueryCountV3.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortTxQueryCountV3.setStatus(_A)
_SwL2IGMPPortTxReportCountV1_Type=Counter32
_SwL2IGMPPortTxReportCountV1_Object=MibTableColumn
swL2IGMPPortTxReportCountV1=_SwL2IGMPPortTxReportCountV1_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,17),_SwL2IGMPPortTxReportCountV1_Type())
swL2IGMPPortTxReportCountV1.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortTxReportCountV1.setStatus(_A)
_SwL2IGMPPortTxReportCountV2_Type=Counter32
_SwL2IGMPPortTxReportCountV2_Object=MibTableColumn
swL2IGMPPortTxReportCountV2=_SwL2IGMPPortTxReportCountV2_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,18),_SwL2IGMPPortTxReportCountV2_Type())
swL2IGMPPortTxReportCountV2.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortTxReportCountV2.setStatus(_A)
_SwL2IGMPPortTxReportCountV3_Type=Counter32
_SwL2IGMPPortTxReportCountV3_Object=MibTableColumn
swL2IGMPPortTxReportCountV3=_SwL2IGMPPortTxReportCountV3_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,19),_SwL2IGMPPortTxReportCountV3_Type())
swL2IGMPPortTxReportCountV3.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortTxReportCountV3.setStatus(_A)
_SwL2IGMPPortTxLeaveCountV2_Type=Counter32
_SwL2IGMPPortTxLeaveCountV2_Object=MibTableColumn
swL2IGMPPortTxLeaveCountV2=_SwL2IGMPPortTxLeaveCountV2_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,14,3,1,20),_SwL2IGMPPortTxLeaveCountV2_Type())
swL2IGMPPortTxLeaveCountV2.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortTxLeaveCountV2.setStatus(_A)
_SwL2IGMPRouterIPAddressTable_Object=MibTable
swL2IGMPRouterIPAddressTable=_SwL2IGMPRouterIPAddressTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,15))
if mibBuilder.loadTexts:swL2IGMPRouterIPAddressTable.setStatus(_A)
_SwL2IGMPRouterIPAddressEntry_Object=MibTableRow
swL2IGMPRouterIPAddressEntry=_SwL2IGMPRouterIPAddressEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,15,1))
swL2IGMPRouterIPAddressEntry.setIndexNames((0,_E,_Ac),(0,_E,_Ad))
if mibBuilder.loadTexts:swL2IGMPRouterIPAddressEntry.setStatus(_A)
class _SwL2IGMPRouterIPAddressVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2IGMPRouterIPAddressVid_Type.__name__=_B
_SwL2IGMPRouterIPAddressVid_Object=MibTableColumn
swL2IGMPRouterIPAddressVid=_SwL2IGMPRouterIPAddressVid_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,15,1,1),_SwL2IGMPRouterIPAddressVid_Type())
swL2IGMPRouterIPAddressVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouterIPAddressVid.setStatus(_A)
_SwL2IGMPRouterIPAddress_Type=IpAddress
_SwL2IGMPRouterIPAddress_Object=MibTableColumn
swL2IGMPRouterIPAddress=_SwL2IGMPRouterIPAddress_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,15,1,2),_SwL2IGMPRouterIPAddress_Type())
swL2IGMPRouterIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouterIPAddress.setStatus(_A)
_SwL2IGMPSnoopingStaticGroupTable_Object=MibTable
swL2IGMPSnoopingStaticGroupTable=_SwL2IGMPSnoopingStaticGroupTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,16))
if mibBuilder.loadTexts:swL2IGMPSnoopingStaticGroupTable.setStatus(_A)
_SwL2IGMPSnoopingStaticGroupEntry_Object=MibTableRow
swL2IGMPSnoopingStaticGroupEntry=_SwL2IGMPSnoopingStaticGroupEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,16,1))
swL2IGMPSnoopingStaticGroupEntry.setIndexNames((0,_E,_Ae),(0,_E,_Af))
if mibBuilder.loadTexts:swL2IGMPSnoopingStaticGroupEntry.setStatus(_A)
class _SwL2IGMPSnoopingStaticGroupVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2IGMPSnoopingStaticGroupVID_Type.__name__=_B
_SwL2IGMPSnoopingStaticGroupVID_Object=MibTableColumn
swL2IGMPSnoopingStaticGroupVID=_SwL2IGMPSnoopingStaticGroupVID_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,16,1,1),_SwL2IGMPSnoopingStaticGroupVID_Type())
swL2IGMPSnoopingStaticGroupVID.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPSnoopingStaticGroupVID.setStatus(_A)
_SwL2IGMPSnoopingStaticGroupIPaddress_Type=IpAddress
_SwL2IGMPSnoopingStaticGroupIPaddress_Object=MibTableColumn
swL2IGMPSnoopingStaticGroupIPaddress=_SwL2IGMPSnoopingStaticGroupIPaddress_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,16,1,2),_SwL2IGMPSnoopingStaticGroupIPaddress_Type())
swL2IGMPSnoopingStaticGroupIPaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPSnoopingStaticGroupIPaddress.setStatus(_A)
_SwL2IGMPSnoopingStaticGroupMemberPortList_Type=PortList
_SwL2IGMPSnoopingStaticGroupMemberPortList_Object=MibTableColumn
swL2IGMPSnoopingStaticGroupMemberPortList=_SwL2IGMPSnoopingStaticGroupMemberPortList_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,16,1,3),_SwL2IGMPSnoopingStaticGroupMemberPortList_Type())
swL2IGMPSnoopingStaticGroupMemberPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPSnoopingStaticGroupMemberPortList.setStatus(_A)
_SwL2IGMPSnoopingStaticGroupRowStatus_Type=RowStatus
_SwL2IGMPSnoopingStaticGroupRowStatus_Object=MibTableColumn
swL2IGMPSnoopingStaticGroupRowStatus=_SwL2IGMPSnoopingStaticGroupRowStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,11,16,1,4),_SwL2IGMPSnoopingStaticGroupRowStatus_Type())
swL2IGMPSnoopingStaticGroupRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swL2IGMPSnoopingStaticGroupRowStatus.setStatus(_A)
_SwL2TrafficMgmt_ObjectIdentity=ObjectIdentity
swL2TrafficMgmt=_SwL2TrafficMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,13))
_SwL2TrafficCtrlTable_Object=MibTable
swL2TrafficCtrlTable=_SwL2TrafficCtrlTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,13,1))
if mibBuilder.loadTexts:swL2TrafficCtrlTable.setStatus(_A)
_SwL2TrafficCtrlEntry_Object=MibTableRow
swL2TrafficCtrlEntry=_SwL2TrafficCtrlEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,13,1,1))
swL2TrafficCtrlEntry.setIndexNames((0,_E,_Ag))
if mibBuilder.loadTexts:swL2TrafficCtrlEntry.setStatus(_A)
class _SwL2TrafficCtrlGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrafficCtrlGroupIndex_Type.__name__=_B
_SwL2TrafficCtrlGroupIndex_Object=MibTableColumn
swL2TrafficCtrlGroupIndex=_SwL2TrafficCtrlGroupIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,13,1,1,1),_SwL2TrafficCtrlGroupIndex_Type())
swL2TrafficCtrlGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrafficCtrlGroupIndex.setStatus(_A)
class _SwL2TrafficCtrlUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrafficCtrlUnitIndex_Type.__name__=_B
_SwL2TrafficCtrlUnitIndex_Object=MibTableColumn
swL2TrafficCtrlUnitIndex=_SwL2TrafficCtrlUnitIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,13,1,1,2),_SwL2TrafficCtrlUnitIndex_Type())
swL2TrafficCtrlUnitIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrafficCtrlUnitIndex.setStatus(_A)
class _SwL2TrafficCtrlBMStromthreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL2TrafficCtrlBMStromthreshold_Type.__name__=_B
_SwL2TrafficCtrlBMStromthreshold_Object=MibTableColumn
swL2TrafficCtrlBMStromthreshold=_SwL2TrafficCtrlBMStromthreshold_Object((1,3,6,1,4,1,171,11,133,1,1,2,13,1,1,3),_SwL2TrafficCtrlBMStromthreshold_Type())
swL2TrafficCtrlBMStromthreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrafficCtrlBMStromthreshold.setStatus(_A)
class _SwL2TrafficCtrlBcastStromCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2TrafficCtrlBcastStromCtrl_Type.__name__=_B
_SwL2TrafficCtrlBcastStromCtrl_Object=MibTableColumn
swL2TrafficCtrlBcastStromCtrl=_SwL2TrafficCtrlBcastStromCtrl_Object((1,3,6,1,4,1,171,11,133,1,1,2,13,1,1,4),_SwL2TrafficCtrlBcastStromCtrl_Type())
swL2TrafficCtrlBcastStromCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrafficCtrlBcastStromCtrl.setStatus(_A)
class _SwL2TrafficCtrlMcastStromCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2TrafficCtrlMcastStromCtrl_Type.__name__=_B
_SwL2TrafficCtrlMcastStromCtrl_Object=MibTableColumn
swL2TrafficCtrlMcastStromCtrl=_SwL2TrafficCtrlMcastStromCtrl_Object((1,3,6,1,4,1,171,11,133,1,1,2,13,1,1,5),_SwL2TrafficCtrlMcastStromCtrl_Type())
swL2TrafficCtrlMcastStromCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrafficCtrlMcastStromCtrl.setStatus(_A)
class _SwL2TrafficCtrlDlfStromCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2TrafficCtrlDlfStromCtrl_Type.__name__=_B
_SwL2TrafficCtrlDlfStromCtrl_Object=MibTableColumn
swL2TrafficCtrlDlfStromCtrl=_SwL2TrafficCtrlDlfStromCtrl_Object((1,3,6,1,4,1,171,11,133,1,1,2,13,1,1,6),_SwL2TrafficCtrlDlfStromCtrl_Type())
swL2TrafficCtrlDlfStromCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrafficCtrlDlfStromCtrl.setStatus(_A)
_SwL2TrafficSegMgmt_ObjectIdentity=ObjectIdentity
swL2TrafficSegMgmt=_SwL2TrafficSegMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,14))
_SwL2TrafficSegTable_Object=MibTable
swL2TrafficSegTable=_SwL2TrafficSegTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,14,1))
if mibBuilder.loadTexts:swL2TrafficSegTable.setStatus(_A)
_SwL2TrafficSegEntry_Object=MibTableRow
swL2TrafficSegEntry=_SwL2TrafficSegEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,14,1,1))
swL2TrafficSegEntry.setIndexNames((0,_E,_Ah))
if mibBuilder.loadTexts:swL2TrafficSegEntry.setStatus(_A)
class _SwL2TrafficSegPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrafficSegPort_Type.__name__=_B
_SwL2TrafficSegPort_Object=MibTableColumn
swL2TrafficSegPort=_SwL2TrafficSegPort_Object((1,3,6,1,4,1,171,11,133,1,1,2,14,1,1,1),_SwL2TrafficSegPort_Type())
swL2TrafficSegPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrafficSegPort.setStatus(_A)
_SwL2TrafficSegForwardPorts_Type=PortList
_SwL2TrafficSegForwardPorts_Object=MibTableColumn
swL2TrafficSegForwardPorts=_SwL2TrafficSegForwardPorts_Object((1,3,6,1,4,1,171,11,133,1,1,2,14,1,1,2),_SwL2TrafficSegForwardPorts_Type())
swL2TrafficSegForwardPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrafficSegForwardPorts.setStatus(_A)
_SwL2StpMgmt_ObjectIdentity=ObjectIdentity
swL2StpMgmt=_SwL2StpMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,15))
class _SwL2StpForwardBPDU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2StpForwardBPDU_Type.__name__=_B
_SwL2StpForwardBPDU_Object=MibScalar
swL2StpForwardBPDU=_SwL2StpForwardBPDU_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,1),_SwL2StpForwardBPDU_Type())
swL2StpForwardBPDU.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpForwardBPDU.setStatus(_A)
class _SwL2StpLbd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2StpLbd_Type.__name__=_B
_SwL2StpLbd_Object=MibScalar
swL2StpLbd=_SwL2StpLbd_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,2),_SwL2StpLbd_Type())
swL2StpLbd.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpLbd.setStatus(_A)
class _SwL2StpLbdRecoverTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_SwL2StpLbdRecoverTime_Type.__name__=_B
_SwL2StpLbdRecoverTime_Object=MibScalar
swL2StpLbdRecoverTime=_SwL2StpLbdRecoverTime_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,3),_SwL2StpLbdRecoverTime_Type())
swL2StpLbdRecoverTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpLbdRecoverTime.setStatus(_A)
_SwL2StpPortTable_Object=MibTable
swL2StpPortTable=_SwL2StpPortTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4))
if mibBuilder.loadTexts:swL2StpPortTable.setStatus(_A)
_SwL2StpPortEntry_Object=MibTableRow
swL2StpPortEntry=_SwL2StpPortEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4,1))
swL2StpPortEntry.setIndexNames((0,_E,_Ai))
if mibBuilder.loadTexts:swL2StpPortEntry.setStatus(_A)
class _SwL2StpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2StpPort_Type.__name__=_B
_SwL2StpPort_Object=MibTableColumn
swL2StpPort=_SwL2StpPort_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4,1,1),_SwL2StpPort_Type())
swL2StpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2StpPort.setStatus(_A)
class _SwL2StpPortLbd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2StpPortLbd_Type.__name__=_B
_SwL2StpPortLbd_Object=MibTableColumn
swL2StpPortLbd=_SwL2StpPortLbd_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4,1,2),_SwL2StpPortLbd_Type())
swL2StpPortLbd.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpPortLbd.setStatus(_A)
class _SwL2StpPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_H,1),(_F,2),('discarding',3),('learning',4),('forwarding',5),('broken',6),('no-stp-enabled',7),(_x,8)))
_SwL2StpPortStatus_Type.__name__=_B
_SwL2StpPortStatus_Object=MibTableColumn
swL2StpPortStatus=_SwL2StpPortStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4,1,3),_SwL2StpPortStatus_Type())
swL2StpPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2StpPortStatus.setStatus(_A)
class _SwL2StpPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),('alternate',2),('backup',3),('root',4),('designated',5),('nonStp',6),('loopback',7)))
_SwL2StpPortRole_Type.__name__=_B
_SwL2StpPortRole_Object=MibTableColumn
swL2StpPortRole=_SwL2StpPortRole_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4,1,4),_SwL2StpPortRole_Type())
swL2StpPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2StpPortRole.setStatus(_A)
class _SwL2StpPortFBPDU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2StpPortFBPDU_Type.__name__=_B
_SwL2StpPortFBPDU_Object=MibTableColumn
swL2StpPortFBPDU=_SwL2StpPortFBPDU_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4,1,5),_SwL2StpPortFBPDU_Type())
swL2StpPortFBPDU.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpPortFBPDU.setStatus(_A)
class _SwL2StpPortLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_n,1),('half-10Mbps-none',2),('half-10Mbps-backp',3),('full-10Mbps-none',4),('full-10Mbps-8023x',5),('half-100Mbps-none',6),('half-100Mbps-backp',7),('full-100Mbps-none',8),('full-100Mbps-8023x',9),('half-1000Mbps-none',10),('full-1000Mbps-backp',11),('full-1000Mbps-none',12),('full-1000Mbps-8023x',13)))
_SwL2StpPortLinkState_Type.__name__=_B
_SwL2StpPortLinkState_Object=MibTableColumn
swL2StpPortLinkState=_SwL2StpPortLinkState_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4,1,6),_SwL2StpPortLinkState_Type())
swL2StpPortLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2StpPortLinkState.setStatus(_A)
_SwL2StpPortProtocolMigration_Type=TruthValue
_SwL2StpPortProtocolMigration_Object=MibTableColumn
swL2StpPortProtocolMigration=_SwL2StpPortProtocolMigration_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4,1,7),_SwL2StpPortProtocolMigration_Type())
swL2StpPortProtocolMigration.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpPortProtocolMigration.setStatus(_A)
_SwL2StpPortAdminEdgePort_Type=TruthValue
_SwL2StpPortAdminEdgePort_Object=MibTableColumn
swL2StpPortAdminEdgePort=_SwL2StpPortAdminEdgePort_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4,1,8),_SwL2StpPortAdminEdgePort_Type())
swL2StpPortAdminEdgePort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpPortAdminEdgePort.setStatus(_A)
_SwL2StpPortOperEdgePort_Type=TruthValue
_SwL2StpPortOperEdgePort_Object=MibTableColumn
swL2StpPortOperEdgePort=_SwL2StpPortOperEdgePort_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4,1,9),_SwL2StpPortOperEdgePort_Type())
swL2StpPortOperEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2StpPortOperEdgePort.setStatus(_A)
class _SwL2StpPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_SwL2StpPortAdminPointToPoint_Type.__name__=_B
_SwL2StpPortAdminPointToPoint_Object=MibTableColumn
swL2StpPortAdminPointToPoint=_SwL2StpPortAdminPointToPoint_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4,1,10),_SwL2StpPortAdminPointToPoint_Type())
swL2StpPortAdminPointToPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpPortAdminPointToPoint.setStatus(_A)
_SwL2StpPortOperPointToPoint_Type=TruthValue
_SwL2StpPortOperPointToPoint_Object=MibTableColumn
swL2StpPortOperPointToPoint=_SwL2StpPortOperPointToPoint_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4,1,11),_SwL2StpPortOperPointToPoint_Type())
swL2StpPortOperPointToPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2StpPortOperPointToPoint.setStatus(_A)
class _SwL2StpPortAdminPathCost_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_SwL2StpPortAdminPathCost_Type.__name__=_a
_SwL2StpPortAdminPathCost_Object=MibTableColumn
swL2StpPortAdminPathCost=_SwL2StpPortAdminPathCost_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4,1,12),_SwL2StpPortAdminPathCost_Type())
swL2StpPortAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpPortAdminPathCost.setStatus(_A)
class _SwL2StpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_SwL2StpPortPriority_Type.__name__=_B
_SwL2StpPortPriority_Object=MibTableColumn
swL2StpPortPriority=_SwL2StpPortPriority_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4,1,13),_SwL2StpPortPriority_Type())
swL2StpPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpPortPriority.setStatus(_A)
class _SwL2STPPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2STPPortState_Type.__name__=_B
_SwL2STPPortState_Object=MibTableColumn
swL2STPPortState=_SwL2STPPortState_Object((1,3,6,1,4,1,171,11,133,1,1,2,15,4,1,14),_SwL2STPPortState_Type())
swL2STPPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2STPPortState.setStatus(_A)
_SwL2MulticastFilterMode_ObjectIdentity=ObjectIdentity
swL2MulticastFilterMode=_SwL2MulticastFilterMode_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,17))
_SwL2MulticastFilterModeVlanTable_Object=MibTable
swL2MulticastFilterModeVlanTable=_SwL2MulticastFilterModeVlanTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,17,1))
if mibBuilder.loadTexts:swL2MulticastFilterModeVlanTable.setStatus(_A)
_SwL2MulticastFilterModeVlanEntry_Object=MibTableRow
swL2MulticastFilterModeVlanEntry=_SwL2MulticastFilterModeVlanEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,17,1,1))
swL2MulticastFilterModeVlanEntry.setIndexNames((0,_E,_Aj))
if mibBuilder.loadTexts:swL2MulticastFilterModeVlanEntry.setStatus(_A)
class _SwL2MulticastFilterVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2MulticastFilterVid_Type.__name__=_B
_SwL2MulticastFilterVid_Object=MibTableColumn
swL2MulticastFilterVid=_SwL2MulticastFilterVid_Object((1,3,6,1,4,1,171,11,133,1,1,2,17,1,1,1),_SwL2MulticastFilterVid_Type())
swL2MulticastFilterVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MulticastFilterVid.setStatus(_A)
class _SwL2MulticastFilterVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Ak,1),(_Al,2),(_Am,3)))
_SwL2MulticastFilterVlanMode_Type.__name__=_B
_SwL2MulticastFilterVlanMode_Object=MibTableColumn
swL2MulticastFilterVlanMode=_SwL2MulticastFilterVlanMode_Object((1,3,6,1,4,1,171,11,133,1,1,2,17,1,1,2),_SwL2MulticastFilterVlanMode_Type())
swL2MulticastFilterVlanMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MulticastFilterVlanMode.setStatus(_A)
_SwL2MulticastFilterModePortTable_Object=MibTable
swL2MulticastFilterModePortTable=_SwL2MulticastFilterModePortTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,17,2))
if mibBuilder.loadTexts:swL2MulticastFilterModePortTable.setStatus(_A)
_SwL2MulticastFilterModePortEntry_Object=MibTableRow
swL2MulticastFilterModePortEntry=_SwL2MulticastFilterModePortEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,17,2,1))
swL2MulticastFilterModePortEntry.setIndexNames((0,_E,_An))
if mibBuilder.loadTexts:swL2MulticastFilterModePortEntry.setStatus(_A)
class _SwL2MulticastFilterPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2MulticastFilterPortIndex_Type.__name__=_B
_SwL2MulticastFilterPortIndex_Object=MibTableColumn
swL2MulticastFilterPortIndex=_SwL2MulticastFilterPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,17,2,1,1),_SwL2MulticastFilterPortIndex_Type())
swL2MulticastFilterPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MulticastFilterPortIndex.setStatus(_A)
class _SwL2MulticastFilterPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Ak,1),(_Al,2),(_Am,3)))
_SwL2MulticastFilterPortMode_Type.__name__=_B
_SwL2MulticastFilterPortMode_Object=MibTableColumn
swL2MulticastFilterPortMode=_SwL2MulticastFilterPortMode_Object((1,3,6,1,4,1,171,11,133,1,1,2,17,2,1,2),_SwL2MulticastFilterPortMode_Type())
swL2MulticastFilterPortMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MulticastFilterPortMode.setStatus(_A)
_SwL2LoopDetectMgmt_ObjectIdentity=ObjectIdentity
swL2LoopDetectMgmt=_SwL2LoopDetectMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,18))
_SwL2LoopDetectCtrl_ObjectIdentity=ObjectIdentity
swL2LoopDetectCtrl=_SwL2LoopDetectCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,18,1))
class _SwL2LoopDetectAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2LoopDetectAdminState_Type.__name__=_B
_SwL2LoopDetectAdminState_Object=MibScalar
swL2LoopDetectAdminState=_SwL2LoopDetectAdminState_Object((1,3,6,1,4,1,171,11,133,1,1,2,18,1,1),_SwL2LoopDetectAdminState_Type())
swL2LoopDetectAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectAdminState.setStatus(_A)
class _SwL2LoopDetectInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_SwL2LoopDetectInterval_Type.__name__=_B
_SwL2LoopDetectInterval_Object=MibScalar
swL2LoopDetectInterval=_SwL2LoopDetectInterval_Object((1,3,6,1,4,1,171,11,133,1,1,2,18,1,2),_SwL2LoopDetectInterval_Type())
swL2LoopDetectInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectInterval.setStatus(_A)
class _SwL2LoopDetectRecoverTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_SwL2LoopDetectRecoverTime_Type.__name__=_B
_SwL2LoopDetectRecoverTime_Object=MibScalar
swL2LoopDetectRecoverTime=_SwL2LoopDetectRecoverTime_Object((1,3,6,1,4,1,171,11,133,1,1,2,18,1,3),_SwL2LoopDetectRecoverTime_Type())
swL2LoopDetectRecoverTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectRecoverTime.setStatus(_A)
class _SwL2LoopDetectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan-based',1),('port-based',2)))
_SwL2LoopDetectMode_Type.__name__=_B
_SwL2LoopDetectMode_Object=MibScalar
swL2LoopDetectMode=_SwL2LoopDetectMode_Object((1,3,6,1,4,1,171,11,133,1,1,2,18,1,4),_SwL2LoopDetectMode_Type())
swL2LoopDetectMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectMode.setStatus(_A)
class _SwL2LoopDetectTrapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),('loop_detected',2),('loop_cleared',3),('both',4)))
_SwL2LoopDetectTrapMode_Type.__name__=_B
_SwL2LoopDetectTrapMode_Object=MibScalar
swL2LoopDetectTrapMode=_SwL2LoopDetectTrapMode_Object((1,3,6,1,4,1,171,11,133,1,1,2,18,1,5),_SwL2LoopDetectTrapMode_Type())
swL2LoopDetectTrapMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectTrapMode.setStatus(_A)
_SwL2LoopDetectPortMgmt_ObjectIdentity=ObjectIdentity
swL2LoopDetectPortMgmt=_SwL2LoopDetectPortMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,18,2))
_SwL2LoopDetectPortTable_Object=MibTable
swL2LoopDetectPortTable=_SwL2LoopDetectPortTable_Object((1,3,6,1,4,1,171,11,133,1,1,2,18,2,1))
if mibBuilder.loadTexts:swL2LoopDetectPortTable.setStatus(_A)
_SwL2LoopDetectPortEntry_Object=MibTableRow
swL2LoopDetectPortEntry=_SwL2LoopDetectPortEntry_Object((1,3,6,1,4,1,171,11,133,1,1,2,18,2,1,1))
swL2LoopDetectPortEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:swL2LoopDetectPortEntry.setStatus(_A)
class _SwL2LoopDetectPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2LoopDetectPortIndex_Type.__name__=_B
_SwL2LoopDetectPortIndex_Object=MibTableColumn
swL2LoopDetectPortIndex=_SwL2LoopDetectPortIndex_Object((1,3,6,1,4,1,171,11,133,1,1,2,18,2,1,1,1),_SwL2LoopDetectPortIndex_Type())
swL2LoopDetectPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectPortIndex.setStatus(_A)
class _SwL2LoopDetectPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2LoopDetectPortState_Type.__name__=_B
_SwL2LoopDetectPortState_Object=MibTableColumn
swL2LoopDetectPortState=_SwL2LoopDetectPortState_Object((1,3,6,1,4,1,171,11,133,1,1,2,18,2,1,1,2),_SwL2LoopDetectPortState_Type())
swL2LoopDetectPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectPortState.setStatus(_A)
_SwL2LoopDetectPortLoopVLAN_Type=DisplayString
_SwL2LoopDetectPortLoopVLAN_Object=MibTableColumn
swL2LoopDetectPortLoopVLAN=_SwL2LoopDetectPortLoopVLAN_Object((1,3,6,1,4,1,171,11,133,1,1,2,18,2,1,1,3),_SwL2LoopDetectPortLoopVLAN_Type())
swL2LoopDetectPortLoopVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectPortLoopVLAN.setStatus(_A)
class _SwL2LoopDetectPortLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('loop',2),('error',3),(_M,4)))
_SwL2LoopDetectPortLoopStatus_Type.__name__=_B
_SwL2LoopDetectPortLoopStatus_Object=MibTableColumn
swL2LoopDetectPortLoopStatus=_SwL2LoopDetectPortLoopStatus_Object((1,3,6,1,4,1,171,11,133,1,1,2,18,2,1,1,4),_SwL2LoopDetectPortLoopStatus_Type())
swL2LoopDetectPortLoopStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectPortLoopStatus.setStatus(_A)
_SwL2MgmtMIBTraps_ObjectIdentity=ObjectIdentity
swL2MgmtMIBTraps=_SwL2MgmtMIBTraps_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,100))
_SwL2Notify_ObjectIdentity=ObjectIdentity
swL2Notify=_SwL2Notify_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,100,1))
_SwL2NotifyMgmt_ObjectIdentity=ObjectIdentity
swL2NotifyMgmt=_SwL2NotifyMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,100,1,1))
_SwL2macNotificationSeverity_Type=AgentNotifyLevel
_SwL2macNotificationSeverity_Object=MibScalar
swL2macNotificationSeverity=_SwL2macNotificationSeverity_Object((1,3,6,1,4,1,171,11,133,1,1,2,100,1,1,1),_SwL2macNotificationSeverity_Type())
swL2macNotificationSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2macNotificationSeverity.setStatus(_A)
_SwL2PortSecurityViolationSeverity_Type=AgentNotifyLevel
_SwL2PortSecurityViolationSeverity_Object=MibScalar
swL2PortSecurityViolationSeverity=_SwL2PortSecurityViolationSeverity_Object((1,3,6,1,4,1,171,11,133,1,1,2,100,1,1,2),_SwL2PortSecurityViolationSeverity_Type())
swL2PortSecurityViolationSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityViolationSeverity.setStatus(_A)
_SwL2NotifyPrefix_ObjectIdentity=ObjectIdentity
swL2NotifyPrefix=_SwL2NotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,100,1,2))
_SwL2NotifFirmware_ObjectIdentity=ObjectIdentity
swL2NotifFirmware=_SwL2NotifFirmware_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,100,1,2,0))
_Swl2NotificationBidings_ObjectIdentity=ObjectIdentity
swl2NotificationBidings=_Swl2NotificationBidings_ObjectIdentity((1,3,6,1,4,1,171,11,133,1,1,2,100,1,2,1))
class _SwL2macNotifyInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_SwL2macNotifyInfo_Type.__name__=_R
_SwL2macNotifyInfo_Object=MibScalar
swL2macNotifyInfo=_SwL2macNotifyInfo_Object((1,3,6,1,4,1,171,11,133,1,1,2,100,1,2,1,1),_SwL2macNotifyInfo_Type())
swL2macNotifyInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2macNotifyInfo.setStatus(_A)
_SwL2PortSecurityViolationMac_Type=MacAddress
_SwL2PortSecurityViolationMac_Object=MibScalar
swL2PortSecurityViolationMac=_SwL2PortSecurityViolationMac_Object((1,3,6,1,4,1,171,11,133,1,1,2,100,1,2,1,2),_SwL2PortSecurityViolationMac_Type())
swL2PortSecurityViolationMac.setMaxAccess(_Ao)
if mibBuilder.loadTexts:swL2PortSecurityViolationMac.setStatus(_A)
_SwL2VlanLoopDetectVID_Type=Integer32
_SwL2VlanLoopDetectVID_Object=MibScalar
swL2VlanLoopDetectVID=_SwL2VlanLoopDetectVID_Object((1,3,6,1,4,1,171,11,133,1,1,2,100,1,2,1,3),_SwL2VlanLoopDetectVID_Type())
swL2VlanLoopDetectVID.setMaxAccess(_Ao)
if mibBuilder.loadTexts:swL2VlanLoopDetectVID.setStatus(_A)
swL2macNotification=NotificationType((1,3,6,1,4,1,171,11,133,1,1,2,100,1,2,0,1))
swL2macNotification.setObjects((_E,_Ap))
if mibBuilder.loadTexts:swL2macNotification.setStatus(_A)
swL2PortSecurityViolationTrap=NotificationType((1,3,6,1,4,1,171,11,133,1,1,2,100,1,2,0,2))
swL2PortSecurityViolationTrap.setObjects(*((_Y,_Z),(_E,_Aq)))
if mibBuilder.loadTexts:swL2PortSecurityViolationTrap.setStatus(_A)
swL2PortLoopOccurred=NotificationType((1,3,6,1,4,1,171,11,133,1,1,2,100,1,2,0,3))
swL2PortLoopOccurred.setObjects((_E,_L))
if mibBuilder.loadTexts:swL2PortLoopOccurred.setStatus(_A)
swL2PortLoopRestart=NotificationType((1,3,6,1,4,1,171,11,133,1,1,2,100,1,2,0,4))
swL2PortLoopRestart.setObjects((_E,_L))
if mibBuilder.loadTexts:swL2PortLoopRestart.setStatus(_A)
swL2VlanLoopOccurred=NotificationType((1,3,6,1,4,1,171,11,133,1,1,2,100,1,2,0,5))
swL2VlanLoopOccurred.setObjects(*((_E,_L),(_E,_X)))
if mibBuilder.loadTexts:swL2VlanLoopOccurred.setStatus(_A)
swL2VlanLoopRestart=NotificationType((1,3,6,1,4,1,171,11,133,1,1,2,100,1,2,0,6))
swL2VlanLoopRestart.setObjects(*((_E,_L),(_E,_X)))
if mibBuilder.loadTexts:swL2VlanLoopRestart.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'MacAddress':MacAddress,'VlanId':VlanId,'PortList':PortList,'IANAifMauAutoNegCapBits':IANAifMauAutoNegCapBits,'swL2MgmtMIB':swL2MgmtMIB,'swL2DevMgmt':swL2DevMgmt,'swL2DevInfo':swL2DevInfo,'swDevInfoTotalNumOfPort':swDevInfoTotalNumOfPort,'swDevInfoNumOfPortInUse':swDevInfoNumOfPortInUse,'swDevModuleInfoTable':swDevModuleInfoTable,'swDevModuleInfoEntry':swDevModuleInfoEntry,_b:swDevModuleInfoUnitID,'swDevModuleInfoModuleName':swDevModuleInfoModuleName,'swDevModuleInfoReversion':swDevModuleInfoReversion,'swDevModuleInfoSerial':swDevModuleInfoSerial,'swDevModuleInfoDescription':swDevModuleInfoDescription,'swDevInfoFrontPanelLedStatus':swDevInfoFrontPanelLedStatus,'swL2DevCtrl':swL2DevCtrl,'swL2DevCtrlStpState':swL2DevCtrlStpState,'swL2DevCtrlIGMPSnooping':swL2DevCtrlIGMPSnooping,'swL2DevCtrlIGMPSnoopingMcstRTOnly':swL2DevCtrlIGMPSnoopingMcstRTOnly,'swL2DevCtrlRmonState':swL2DevCtrlRmonState,'swL2DevCtrlSnmpTrapState':swL2DevCtrlSnmpTrapState,'swL2DevCtrlCleanAllStatisticCounter':swL2DevCtrlCleanAllStatisticCounter,'swL2DevCtrlVlanIdOfFDBTbl':swL2DevCtrlVlanIdOfFDBTbl,'swL2MACNotifyState':swL2MACNotifyState,'swL2MACNotifyHistorySize':swL2MACNotifyHistorySize,'swL2MACNotifyInterval':swL2MACNotifyInterval,'swL2DevCtrlAsymVlanState':swL2DevCtrlAsymVlanState,'swL2DevCtrlTelnet':swL2DevCtrlTelnet,'swL2DevCtrlTelnetState':swL2DevCtrlTelnetState,'swL2DevCtrlTelnetTcpPort':swL2DevCtrlTelnetTcpPort,'swL2DevCtrlManagementVlanId':swL2DevCtrlManagementVlanId,'swL2DevCtrlWeb':swL2DevCtrlWeb,'swL2DevCtrlWebState':swL2DevCtrlWebState,'swL2DevCtrlWebTcpPort':swL2DevCtrlWebTcpPort,'swL2DevCtrlLLDPState':swL2DevCtrlLLDPState,'swL2DevCtrlLLDPForwardMessageState':swL2DevCtrlLLDPForwardMessageState,'swL2DevCtrlIpAutoconfig':swL2DevCtrlIpAutoconfig,'swL2DevCtrlCFM':swL2DevCtrlCFM,'swL2DevCtrlCFMState':swL2DevCtrlCFMState,'swL2DevCtrlCFMPortTable':swL2DevCtrlCFMPortTable,'swL2DevCtrlCFMPortEntry':swL2DevCtrlCFMPortEntry,_d:swL2DevCtrlCFMPortIndex,'swL2DevCtrlCFMPortState':swL2DevCtrlCFMPortState,'swL2DevCtrlVLANTrunkState':swL2DevCtrlVLANTrunkState,'swL2DevAlarm':swL2DevAlarm,'swL2DevAlarmNewRoot':swL2DevAlarmNewRoot,'swL2DevAlarmTopologyChange':swL2DevAlarmTopologyChange,'swL2DevAlarmLinkChange':swL2DevAlarmLinkChange,'swL2VLANMgmt':swL2VLANMgmt,'swL2VlanStaticTable':swL2VlanStaticTable,'swL2VlanStaticEntry':swL2VlanStaticEntry,_e:swL2VlanIndex,'swL2VLANAdvertisement':swL2VLANAdvertisement,'swL2PVIDAutoAssignmentState':swL2PVIDAutoAssignmentState,'swL2VlanPortInfoTable':swL2VlanPortInfoTable,'swL2VlanPortInfoEntry':swL2VlanPortInfoEntry,_f:swL2VlanPortInfoPortIndex,_g:swL2VlanPortInfoVid,'swL2VlanPortInfoPortRole':swL2VlanPortInfoPortRole,'swL2SubnetVLANTable':swL2SubnetVLANTable,'swL2SubnetVLANEntry':swL2SubnetVLANEntry,_h:swL2SubnetVLANIPAddress,_i:swL2SubnetVLANIPMask,'swL2SubnetVLANID':swL2SubnetVLANID,'swL2SubnetVLANPriority':swL2SubnetVLANPriority,'swL2SubnetVLANRowStatus':swL2SubnetVLANRowStatus,'swL2VlanPrecedenceTable':swL2VlanPrecedenceTable,'swL2VlanPrecedenceEntry':swL2VlanPrecedenceEntry,_j:swL2VlanPrecedencePortIndex,'swL2VlanPrecedenceClassification':swL2VlanPrecedenceClassification,'swL2NniGvrpBpduAddress':swL2NniGvrpBpduAddress,'swL2PortMgmt':swL2PortMgmt,'swL2PortInfoTable':swL2PortInfoTable,'swL2PortInfoEntry':swL2PortInfoEntry,_k:swL2PortInfoPortIndex,_l:swL2PortInfoMediumType,'swL2PortInfoUnitID':swL2PortInfoUnitID,'swL2PortInfoType':swL2PortInfoType,'swL2PortInfoLinkStatus':swL2PortInfoLinkStatus,'swL2PortInfoNwayStatus':swL2PortInfoNwayStatus,'swL2PortInfoModuleType':swL2PortInfoModuleType,'swL2PortInfoErrorDisabled':swL2PortInfoErrorDisabled,'swL2PortCtrlTable':swL2PortCtrlTable,'swL2PortCtrlEntry':swL2PortCtrlEntry,_r:swL2PortCtrlPortIndex,_s:swL2PortCtrlMediumType,'swL2PortCtrlUnitIndex':swL2PortCtrlUnitIndex,'swL2PortCtrlAdminState':swL2PortCtrlAdminState,'swL2PortCtrlNwayState':swL2PortCtrlNwayState,'swL2PortCtrlFlowCtrlState':swL2PortCtrlFlowCtrlState,'swL2PortCtrlLearningState':swL2PortCtrlLearningState,'swL2PortCtrlMACNotifyState':swL2PortCtrlMACNotifyState,'swL2PortCtrlMDIXState':swL2PortCtrlMDIXState,'swL2PortCtrlAutoNegRestart':swL2PortCtrlAutoNegRestart,'swL2PortCtrlAutoNegCapAdvertisedBits':swL2PortCtrlAutoNegCapAdvertisedBits,'swL2PortCtrlJumboFrame':swL2PortCtrlJumboFrame,'swL2PortCtrlJumboFrameMaxSize':swL2PortCtrlJumboFrameMaxSize,'swL2PortCableDiagnosisTable':swL2PortCableDiagnosisTable,'swL2PortCableDiagnosisEntry':swL2PortCableDiagnosisEntry,_t:swL2PortCableDiagnosisPortIndex,_u:swL2PortCableDiagnosisPairIndex,'swL2PortCableDiagnosisCableStatus':swL2PortCableDiagnosisCableStatus,'swL2PortCableDiagnosisPairStatus':swL2PortCableDiagnosisPairStatus,'swL2PortCableDiagnosisPairLength':swL2PortCableDiagnosisPairLength,'swL2PortCableDiagnosisPairLengthInaccuracy':swL2PortCableDiagnosisPairLengthInaccuracy,'swL2PortCounterCtrlTable':swL2PortCounterCtrlTable,'swL2PortCounterCtrlEntry':swL2PortCounterCtrlEntry,_v:swL2PortCounterCtrlPortIndex,'swL2PortCounterClearCtrl':swL2PortCounterClearCtrl,'swL2PortErrTable':swL2PortErrTable,'swL2PortErrEntry':swL2PortErrEntry,_w:swL2PortErrPortIndex,'swL2PortErrPortState':swL2PortErrPortState,'swL2PortErrPortConnStatus':swL2PortErrPortConnStatus,'swL2PortErrPortReason':swL2PortErrPortReason,'swL2PortAutoNegInfoTable':swL2PortAutoNegInfoTable,'swL2PortAutoNegInfoEntry':swL2PortAutoNegInfoEntry,_y:swL2PortAutoNegInfoPortIndex,'swL2PortAutoNegInfoAdminStatus':swL2PortAutoNegInfoAdminStatus,'swL2PortAutoNegInfoCapabilityBits':swL2PortAutoNegInfoCapabilityBits,'swL2PortAutoNegInfoCapAdvertisedBits':swL2PortAutoNegInfoCapAdvertisedBits,'swL2PortAutoNegInfoCapReceivedBits':swL2PortAutoNegInfoCapReceivedBits,'swL2PortDropCounterTable':swL2PortDropCounterTable,'swL2PortDropCounterEntry':swL2PortDropCounterEntry,_z:swL2PortDropCounterPortIndex,'swL2PortBufferFullDrops':swL2PortBufferFullDrops,'swL2PortACLDrops':swL2PortACLDrops,'swL2PortMulticastDrops':swL2PortMulticastDrops,'swL2PortVLANIngressDrops':swL2PortVLANIngressDrops,'swL2PortJumboFrameCtrlTable':swL2PortJumboFrameCtrlTable,'swL2PortJumboFrameCtrlEntry':swL2PortJumboFrameCtrlEntry,_A0:swL2PortJumboFrameCtrlPortIndex,'swL2PortJumboFrameCtrlState':swL2PortJumboFrameCtrlState,'swL2DiffServMgmt':swL2DiffServMgmt,'swL2DiffServTypeCtrlTable':swL2DiffServTypeCtrlTable,'swL2DiffServTypeCtrlEntry':swL2DiffServTypeCtrlEntry,_A1:swL2DiffServTypeCtrlPortIndex,'swL2DiffServTypeCtrlDiffServType':swL2DiffServTypeCtrlDiffServType,'swL2DiffServDSCPCtrlTable':swL2DiffServDSCPCtrlTable,'swL2DiffServDSCPCtrlEntry':swL2DiffServDSCPCtrlEntry,_A2:swL2DiffServDSCPCtrlPortIndex,'swL2DiffServDSCPCtrlMode':swL2DiffServDSCPCtrlMode,'swL2DiffServDSCPCtrlValue':swL2DiffServDSCPCtrlValue,'swL2DiffServTOSCtrlTable':swL2DiffServTOSCtrlTable,'swL2DiffServTOSCtrlEntry':swL2DiffServTOSCtrlEntry,_A3:swL2DiffServTOSCtrlPortIndex,'swL2DiffServTOSCtrlMode':swL2DiffServTOSCtrlMode,'swL2DiffServTOSCtrlValue':swL2DiffServTOSCtrlValue,'swL2LimitedMulticastMgmt':swL2LimitedMulticastMgmt,'swL2MulticastFilterProfileTable':swL2MulticastFilterProfileTable,'swL2MulticastFilterProfileEntry':swL2MulticastFilterProfileEntry,_A4:swL2MulticastFilterProfileIndex,'swL2MulticastFilterProfileName':swL2MulticastFilterProfileName,'swL2MulticastFilterStatus':swL2MulticastFilterStatus,'swL2MulticastFilterProfileAddressTable':swL2MulticastFilterProfileAddressTable,'swL2MulticastFilterProfileAddressEntry':swL2MulticastFilterProfileAddressEntry,_A5:swL2MulticastFilterProfileIdIndex,_A6:swL2MulticastFilterFromIp,_A7:swL2MulticastFilterToIp,'swL2MulticastFilterAddressState':swL2MulticastFilterAddressState,'swL2LimitedMulticastFilterPortTable':swL2LimitedMulticastFilterPortTable,'swL2LimitedMulticastFilterPortEntry':swL2LimitedMulticastFilterPortEntry,_A8:swL2LimitedMulticastFilterPortIndex,'swL2LimitedMulticastFilterPortAccess':swL2LimitedMulticastFilterPortAccess,'swL2LimitedMulticastFilterPortProfileID':swL2LimitedMulticastFilterPortProfileID,'swL2LimitedMulticastFilterPortProfileStatus':swL2LimitedMulticastFilterPortProfileStatus,'swL2MulticastFilterPortMaxGroupTable':swL2MulticastFilterPortMaxGroupTable,'swL2MulticastFilterPortMaxGroupEntry':swL2MulticastFilterPortMaxGroupEntry,_A9:swL2MulticastFilterPortMaxGroupPortIndex,'swL2MulticastFilterPortMaxGroup':swL2MulticastFilterPortMaxGroup,'swL2LimitedMulticastFilterVIDTable':swL2LimitedMulticastFilterVIDTable,'swL2LimitedMulticastFilterVIDEntry':swL2LimitedMulticastFilterVIDEntry,_AA:swL2LimitedMulticastFilterVIDIndex,'swL2LimitedMulticastFilterVIDAccess':swL2LimitedMulticastFilterVIDAccess,'swL2LimitedMulticastFilterVIDProfileID':swL2LimitedMulticastFilterVIDProfileID,'swL2LimitedMulticastFilterVIDProfileStatus':swL2LimitedMulticastFilterVIDProfileStatus,'swL2MulticastFilterVIDMaxGroupTable':swL2MulticastFilterVIDMaxGroupTable,'swL2MulticastFilterVIDMaxGroupEntry':swL2MulticastFilterVIDMaxGroupEntry,_AB:swL2MulticastFilterVIDMaxGroupVIDIndex,'swL2MulticastFilterVIDMaxGroup':swL2MulticastFilterVIDMaxGroup,'swL2QOSMgmt':swL2QOSMgmt,'swL2QOSBandwidthControlTable':swL2QOSBandwidthControlTable,'swL2QOSBandwidthControlEntry':swL2QOSBandwidthControlEntry,_AC:swL2QOSBandwidthPortIndex,'swL2QOSBandwidthRxRate':swL2QOSBandwidthRxRate,'swL2QOSBandwidthTxRate':swL2QOSBandwidthTxRate,'swL2QOSBandwidthRadiusRxRate':swL2QOSBandwidthRadiusRxRate,'swL2QOSBandwidthRadiusTxRate':swL2QOSBandwidthRadiusTxRate,'swL2QOSSchedulingTable':swL2QOSSchedulingTable,'swL2QOSSchedulingEntry':swL2QOSSchedulingEntry,_AD:swL2QOSSchedulingClassIndex,'swL2QOSSchedulingMaxPkts':swL2QOSSchedulingMaxPkts,'swL2QOSSchedulingMechanism':swL2QOSSchedulingMechanism,'swL2QOSSchedulingMaxLatency':swL2QOSSchedulingMaxLatency,'swL2QOS8021pUserPriorityTable':swL2QOS8021pUserPriorityTable,'swL2QOS8021pUserPriorityEntry':swL2QOS8021pUserPriorityEntry,_AG:swL2QOS8021pUserPriorityIndex,'swL2QOS8021pUserPriorityClass':swL2QOS8021pUserPriorityClass,'swL2QOS8021pDefaultPriorityTable':swL2QOS8021pDefaultPriorityTable,'swL2QOS8021pDefaultPriorityEntry':swL2QOS8021pDefaultPriorityEntry,_AH:swL2QOS8021pDefaultPriorityIndex,'swL2QOS8021pDefaultPriority':swL2QOS8021pDefaultPriority,'swL2QOS8021pRadiusPriority':swL2QOS8021pRadiusPriority,'swL2QOSSchedulingMechanismCtrl':swL2QOSSchedulingMechanismCtrl,'swL2QOSHolPreventionCtrl':swL2QOSHolPreventionCtrl,'swL2PortSecurityMgmt':swL2PortSecurityMgmt,'swL2PortSecurityControlTable':swL2PortSecurityControlTable,'swL2PortSecurityControlEntry':swL2PortSecurityControlEntry,_AI:swL2PortSecurityPortIndex,'swL2PortSecurityMaxLernAddr':swL2PortSecurityMaxLernAddr,'swL2PortSecurityMode':swL2PortSecurityMode,'swL2PortSecurityAdmState':swL2PortSecurityAdmState,'swL2PortSecurityEntryClearCtrl':swL2PortSecurityEntryClearCtrl,'swL2PortSecurityDelCtrl':swL2PortSecurityDelCtrl,'swL2PortSecurityDelVlanName':swL2PortSecurityDelVlanName,'swL2PortSecurityDelPort':swL2PortSecurityDelPort,'swL2PortSecurityDelMacAddress':swL2PortSecurityDelMacAddress,'swL2PortSecurityDelActivity':swL2PortSecurityDelActivity,'swL2PortSecurityTrapLogState':swL2PortSecurityTrapLogState,'swL2DhcpRelayMgmt':swL2DhcpRelayMgmt,'swL2DhcpRelayState':swL2DhcpRelayState,'swL2DhcpRelayHopCount':swL2DhcpRelayHopCount,'swL2DhcpRelayTimeThreshold':swL2DhcpRelayTimeThreshold,'swL2DhcpRelayOption82State':swL2DhcpRelayOption82State,'swL2DhcpRelayOption82Check':swL2DhcpRelayOption82Check,'swL2DhcpRelayOption82Policy':swL2DhcpRelayOption82Policy,'swL2DhcpRelayCtrlTable':swL2DhcpRelayCtrlTable,'swL2DhcpRelayCtrlEntry':swL2DhcpRelayCtrlEntry,_AJ:swL2DhcpRelayCtrlInterfaceName,_AK:swL2DhcpRelayCtrlServer,'swL2DhcpRelayCtrlState':swL2DhcpRelayCtrlState,'swL2TrunkMgmt':swL2TrunkMgmt,'swL2TrunkMaxSupportedEntries':swL2TrunkMaxSupportedEntries,'swL2TrunkCurrentNumEntries':swL2TrunkCurrentNumEntries,'swL2TrunkCtrlTable':swL2TrunkCtrlTable,'swL2TrunkCtrlEntry':swL2TrunkCtrlEntry,_AL:swL2TrunkIndex,'swL2TrunkName':swL2TrunkName,'swL2TrunkMasterPort':swL2TrunkMasterPort,'swL2TrunkMember':swL2TrunkMember,'swL2TrunkFloodingPort':swL2TrunkFloodingPort,'swL2TrunkType':swL2TrunkType,'swL2TrunkState':swL2TrunkState,'swL2TrunkAlgorithm':swL2TrunkAlgorithm,'swL2TrunkLACPPortTable':swL2TrunkLACPPortTable,'swL2TrunkLACPPortEntry':swL2TrunkLACPPortEntry,_AM:swL2TrunkLACPPortIndex,'swL2TrunkLACPPortState':swL2TrunkLACPPortState,'swL2TrunkVLANTable':swL2TrunkVLANTable,'swL2TrunkVLANEntry':swL2TrunkVLANEntry,_AN:swL2TrunkVLANPort,'swL2TrunkVLANState':swL2TrunkVLANState,'swL2MirrorMgmt':swL2MirrorMgmt,'swL2MirrorLogicTargetPort':swL2MirrorLogicTargetPort,'swL2MirrorPortSourceIngress':swL2MirrorPortSourceIngress,'swL2MirrorPortSourceEgress':swL2MirrorPortSourceEgress,'swL2MirrorPortState':swL2MirrorPortState,'swL2MirrorGroupTable':swL2MirrorGroupTable,'swL2MirrorGroupEntry':swL2MirrorGroupEntry,_AO:swL2MirrorGroupID,'swL2MirrorGroupRowStatus':swL2MirrorGroupRowStatus,'swL2MirrorGroupState':swL2MirrorGroupState,'swL2MirrorGroupTargetPort':swL2MirrorGroupTargetPort,'swL2MirrorGroupSourceIngress':swL2MirrorGroupSourceIngress,'swL2MirrorGroupSourceEngress':swL2MirrorGroupSourceEngress,'swL2IGMPMgmt':swL2IGMPMgmt,'swL2IGMPMaxSupportedVlans':swL2IGMPMaxSupportedVlans,'swL2IGMPMaxIpGroupNumPerVlan':swL2IGMPMaxIpGroupNumPerVlan,'swL2IGMPSnoopingMulticastVlanState':swL2IGMPSnoopingMulticastVlanState,'swL2IGMPCtrlTable':swL2IGMPCtrlTable,'swL2IGMPCtrlEntry':swL2IGMPCtrlEntry,_U:swL2IGMPCtrlVid,'swL2IGMPQueryInterval':swL2IGMPQueryInterval,'swL2IGMPMaxResponseTime':swL2IGMPMaxResponseTime,'swL2IGMPRobustness':swL2IGMPRobustness,'swL2IGMPLastMemberQueryInterval':swL2IGMPLastMemberQueryInterval,'swL2IGMPHostTimeout':swL2IGMPHostTimeout,'swL2IGMPRouteTimeout':swL2IGMPRouteTimeout,'swL2IGMPLeaveTimer':swL2IGMPLeaveTimer,'swL2IGMPQueryState':swL2IGMPQueryState,'swL2IGMPCurrentState':swL2IGMPCurrentState,'swL2IGMPCtrlState':swL2IGMPCtrlState,'swL2IGMPFastLeaveState':swL2IGMPFastLeaveState,'swL2IGMPQueryVersion':swL2IGMPQueryVersion,'swL2IGMPRateLimit':swL2IGMPRateLimit,'swL2IGMPReportSuppression':swL2IGMPReportSuppression,'swL2IGMPQueryInfoTable':swL2IGMPQueryInfoTable,'swL2IGMPQueryInfoEntry':swL2IGMPQueryInfoEntry,_AP:swL2IGMPInfoVid,'swL2IGMPInfoQueryCount':swL2IGMPInfoQueryCount,'swL2IGMPInfoTxQueryCount':swL2IGMPInfoTxQueryCount,'swL2IGMPQueryIPAddress':swL2IGMPQueryIPAddress,'swL2IGMPQueryExpiryTime':swL2IGMPQueryExpiryTime,'swL2IGMPInfoTable':swL2IGMPInfoTable,'swL2IGMPInfoEntry':swL2IGMPInfoEntry,_V:swL2IGMPVid,_W:swL2IGMPGroupIpAddr,'swL2IGMPMacAddr':swL2IGMPMacAddr,'swL2IGMPPortMap':swL2IGMPPortMap,'swL2IGMPIpGroupReportCount':swL2IGMPIpGroupReportCount,'swL2IGMPVersion':swL2IGMPVersion,'swL2IGMPGroupMode':swL2IGMPGroupMode,'swL2IGMPRouterPortTable':swL2IGMPRouterPortTable,'swL2IGMPRouterPortEntry':swL2IGMPRouterPortEntry,_AQ:swL2IGMPRouterPortVlanid,'swL2IGMPRouterPortVlanName':swL2IGMPRouterPortVlanName,'swL2IGMPRouterPortStaticPortList':swL2IGMPRouterPortStaticPortList,'swL2IGMPRouterPortDynamicPortList':swL2IGMPRouterPortDynamicPortList,'swL2IGMPRouterPortForbiddenPortList':swL2IGMPRouterPortForbiddenPortList,'swL2IGMPMulticastVlanTable':swL2IGMPMulticastVlanTable,'swL2IGMPMulticastVlanEntry':swL2IGMPMulticastVlanEntry,_AR:swL2IGMPMulticastVlanid,'swL2IGMPMulticastVlanName':swL2IGMPMulticastVlanName,'swL2IGMPMulticastVlanSourcePort':swL2IGMPMulticastVlanSourcePort,'swL2IGMPMulticastVlanMemberPort':swL2IGMPMulticastVlanMemberPort,'swL2IGMPMulticastVlanTagMemberPort':swL2IGMPMulticastVlanTagMemberPort,'swL2IGMPMulticastVlanState':swL2IGMPMulticastVlanState,'swL2IGMPMulticastVlanReplaceSourceIp':swL2IGMPMulticastVlanReplaceSourceIp,'swL2IGMPMulticastVlanRowStatus':swL2IGMPMulticastVlanRowStatus,'swL2IGMPMulticastVlanRemoveAllMcastAddrListAction':swL2IGMPMulticastVlanRemoveAllMcastAddrListAction,'swL2IGMPMulticastVlanUntagSourcePort':swL2IGMPMulticastVlanUntagSourcePort,'swL2IGMPMulticastVlanRemapPriority':swL2IGMPMulticastVlanRemapPriority,'swL2IGMPMulticastVlanReplacePriority':swL2IGMPMulticastVlanReplacePriority,'swL2IGMPMulticastVlanGroupTable':swL2IGMPMulticastVlanGroupTable,'swL2IGMPMulticastVlanGroupEntry':swL2IGMPMulticastVlanGroupEntry,_AS:swL2IGMPMulticastVlanGroupVid,_AT:swL2IGMPMulticastVlanGroupFromIp,_AU:swL2IGMPMulticastVlanGroupToIp,'swL2IGMPMulticastVlanGroupStatus':swL2IGMPMulticastVlanGroupStatus,'swL2IGMPv3Table':swL2IGMPv3Table,'swL2IGMPv3Entry':swL2IGMPv3Entry,_AV:swL2IGMPv3SourceIPAddr,'swL2IGMPv3Forwarding':swL2IGMPv3Forwarding,'swL2IGMPv3ExpireTimer':swL2IGMPv3ExpireTimer,'swIGMPSnoopingGroupTable':swIGMPSnoopingGroupTable,'swIGMPSnoopingGroupEntry':swIGMPSnoopingGroupEntry,_AW:swIGMPSnoopingGroupVid,_AX:swIGMPSnoopingGroupGroupAddr,_AY:swIGMPSnoopingGroupSourceAddr,'swIGMPSnoopingGroupIncludePortMap':swIGMPSnoopingGroupIncludePortMap,'swIGMPSnoopingGroupExcludePortMap':swIGMPSnoopingGroupExcludePortMap,'swIGMPSnoopingGroupReportCount':swIGMPSnoopingGroupReportCount,'swIGMPSnoopingGroupUpTime':swIGMPSnoopingGroupUpTime,'swIGMPSnoopingGroupExpiryTime':swIGMPSnoopingGroupExpiryTime,'swIGMPSnoopingGroupRouterPorts':swIGMPSnoopingGroupRouterPorts,'swIGMPSnoopingGroupStaticMemberPorts':swIGMPSnoopingGroupStaticMemberPorts,'swL2IGMPDynIpMultMgmt':swL2IGMPDynIpMultMgmt,'swL2IGMPDynIPMultMaxEntry':swL2IGMPDynIPMultMaxEntry,'swL2IGMPSnoopingClearDynIpMult':swL2IGMPSnoopingClearDynIpMult,'swL2IGMPSnoopingClearDynIpMultVID':swL2IGMPSnoopingClearDynIpMultVID,'swL2IGMPSnoopingClearDynIpMultIP':swL2IGMPSnoopingClearDynIpMultIP,'swL2IGMPSnoopingClearDynIpMultAction':swL2IGMPSnoopingClearDynIpMultAction,'swL2IGMPDynIPMultCtrlTable':swL2IGMPDynIPMultCtrlTable,'swL2IGMPDynIPMultCtrlEntry':swL2IGMPDynIPMultCtrlEntry,'swL2IGMPDynIPMultVlanState':swL2IGMPDynIPMultVlanState,'swL2IGMPDynIPMultVlanAge':swL2IGMPDynIPMultVlanAge,'swL2IGMPDynIPMultGroupExpiryTime':swL2IGMPDynIPMultGroupExpiryTime,'swL2IGMPAccessAuthTable':swL2IGMPAccessAuthTable,'swL2IGMPAccessAuthEntry':swL2IGMPAccessAuthEntry,_AZ:swL2IGMPAccessAuthPort,'swL2IGMPAccessAuthState':swL2IGMPAccessAuthState,'swL2IGMPCountrInfoMgmt':swL2IGMPCountrInfoMgmt,'swL2IGMPSnoopingClearStatisticsCounter':swL2IGMPSnoopingClearStatisticsCounter,'swL2IGMPVlanCounterInfoTable':swL2IGMPVlanCounterInfoTable,'swL2IGMPVlanCounterInfoEntry':swL2IGMPVlanCounterInfoEntry,_Aa:swL2IGMPVlanCounterInfoVid,'swL2IGMPVlanCounterGroupNumber':swL2IGMPVlanCounterGroupNumber,'swL2IGMPVlanQueryCountV1':swL2IGMPVlanQueryCountV1,'swL2IGMPVlanQueryCountV2':swL2IGMPVlanQueryCountV2,'swL2IGMPVlanQueryCountV3':swL2IGMPVlanQueryCountV3,'swL2IGMPVlanDropQueryCount':swL2IGMPVlanDropQueryCount,'swL2IGMPVlanReportCountV1':swL2IGMPVlanReportCountV1,'swL2IGMPVlanReportCountV2':swL2IGMPVlanReportCountV2,'swL2IGMPVlanReportCountV3':swL2IGMPVlanReportCountV3,'swL2IGMPVlanLeaveCountV2':swL2IGMPVlanLeaveCountV2,'swL2IGMPVlanDropedReportAndLeaveCount':swL2IGMPVlanDropedReportAndLeaveCount,'swL2IGMPVlanDroppedByMaxGroupLimitation':swL2IGMPVlanDroppedByMaxGroupLimitation,'swL2IGMPVlanDroppedByGroupFilter':swL2IGMPVlanDroppedByGroupFilter,'swL2IGMPVlanTxQueryCountV1':swL2IGMPVlanTxQueryCountV1,'swL2IGMPVlanTxQueryCountV2':swL2IGMPVlanTxQueryCountV2,'swL2IGMPVlanTxQueryCountV3':swL2IGMPVlanTxQueryCountV3,'swL2IGMPVlanTxReportCountV1':swL2IGMPVlanTxReportCountV1,'swL2IGMPVlanTxReportCountV2':swL2IGMPVlanTxReportCountV2,'swL2IGMPVlanTxReportCountV3':swL2IGMPVlanTxReportCountV3,'swL2IGMPVlanTxLeaveCountV2':swL2IGMPVlanTxLeaveCountV2,'swL2IGMPPortCounterInfoTable':swL2IGMPPortCounterInfoTable,'swL2IGMPPortCounterInfoEntry':swL2IGMPPortCounterInfoEntry,_Ab:swL2IGMPPortCounterInfoIndex,'swL2IGMPPortCounterGroupNumber':swL2IGMPPortCounterGroupNumber,'swL2IGMPPortQueryCountV1':swL2IGMPPortQueryCountV1,'swL2IGMPPortQueryCountV2':swL2IGMPPortQueryCountV2,'swL2IGMPPortQueryCountV3':swL2IGMPPortQueryCountV3,'swL2IGMPPortDropQueryCount':swL2IGMPPortDropQueryCount,'swL2IGMPPortReportCountV1':swL2IGMPPortReportCountV1,'swL2IGMPPortReportCountV2':swL2IGMPPortReportCountV2,'swL2IGMPPortReportCountV3':swL2IGMPPortReportCountV3,'swL2IGMPPortLeaveCountV2':swL2IGMPPortLeaveCountV2,'swL2IGMPPortDropedReportAndLeaveCount':swL2IGMPPortDropedReportAndLeaveCount,'swL2IGMPPortDroppedByMaxGroupLimitation':swL2IGMPPortDroppedByMaxGroupLimitation,'swL2IGMPPortDroppedByGroupFilter':swL2IGMPPortDroppedByGroupFilter,'swL2IGMPPortTxQueryCountV1':swL2IGMPPortTxQueryCountV1,'swL2IGMPPortTxQueryCountV2':swL2IGMPPortTxQueryCountV2,'swL2IGMPPortTxQueryCountV3':swL2IGMPPortTxQueryCountV3,'swL2IGMPPortTxReportCountV1':swL2IGMPPortTxReportCountV1,'swL2IGMPPortTxReportCountV2':swL2IGMPPortTxReportCountV2,'swL2IGMPPortTxReportCountV3':swL2IGMPPortTxReportCountV3,'swL2IGMPPortTxLeaveCountV2':swL2IGMPPortTxLeaveCountV2,'swL2IGMPRouterIPAddressTable':swL2IGMPRouterIPAddressTable,'swL2IGMPRouterIPAddressEntry':swL2IGMPRouterIPAddressEntry,_Ac:swL2IGMPRouterIPAddressVid,_Ad:swL2IGMPRouterIPAddress,'swL2IGMPSnoopingStaticGroupTable':swL2IGMPSnoopingStaticGroupTable,'swL2IGMPSnoopingStaticGroupEntry':swL2IGMPSnoopingStaticGroupEntry,_Ae:swL2IGMPSnoopingStaticGroupVID,_Af:swL2IGMPSnoopingStaticGroupIPaddress,'swL2IGMPSnoopingStaticGroupMemberPortList':swL2IGMPSnoopingStaticGroupMemberPortList,'swL2IGMPSnoopingStaticGroupRowStatus':swL2IGMPSnoopingStaticGroupRowStatus,'swL2TrafficMgmt':swL2TrafficMgmt,'swL2TrafficCtrlTable':swL2TrafficCtrlTable,'swL2TrafficCtrlEntry':swL2TrafficCtrlEntry,_Ag:swL2TrafficCtrlGroupIndex,'swL2TrafficCtrlUnitIndex':swL2TrafficCtrlUnitIndex,'swL2TrafficCtrlBMStromthreshold':swL2TrafficCtrlBMStromthreshold,'swL2TrafficCtrlBcastStromCtrl':swL2TrafficCtrlBcastStromCtrl,'swL2TrafficCtrlMcastStromCtrl':swL2TrafficCtrlMcastStromCtrl,'swL2TrafficCtrlDlfStromCtrl':swL2TrafficCtrlDlfStromCtrl,'swL2TrafficSegMgmt':swL2TrafficSegMgmt,'swL2TrafficSegTable':swL2TrafficSegTable,'swL2TrafficSegEntry':swL2TrafficSegEntry,_Ah:swL2TrafficSegPort,'swL2TrafficSegForwardPorts':swL2TrafficSegForwardPorts,'swL2StpMgmt':swL2StpMgmt,'swL2StpForwardBPDU':swL2StpForwardBPDU,'swL2StpLbd':swL2StpLbd,'swL2StpLbdRecoverTime':swL2StpLbdRecoverTime,'swL2StpPortTable':swL2StpPortTable,'swL2StpPortEntry':swL2StpPortEntry,_Ai:swL2StpPort,'swL2StpPortLbd':swL2StpPortLbd,'swL2StpPortStatus':swL2StpPortStatus,'swL2StpPortRole':swL2StpPortRole,'swL2StpPortFBPDU':swL2StpPortFBPDU,'swL2StpPortLinkState':swL2StpPortLinkState,'swL2StpPortProtocolMigration':swL2StpPortProtocolMigration,'swL2StpPortAdminEdgePort':swL2StpPortAdminEdgePort,'swL2StpPortOperEdgePort':swL2StpPortOperEdgePort,'swL2StpPortAdminPointToPoint':swL2StpPortAdminPointToPoint,'swL2StpPortOperPointToPoint':swL2StpPortOperPointToPoint,'swL2StpPortAdminPathCost':swL2StpPortAdminPathCost,'swL2StpPortPriority':swL2StpPortPriority,'swL2STPPortState':swL2STPPortState,'swL2MulticastFilterMode':swL2MulticastFilterMode,'swL2MulticastFilterModeVlanTable':swL2MulticastFilterModeVlanTable,'swL2MulticastFilterModeVlanEntry':swL2MulticastFilterModeVlanEntry,_Aj:swL2MulticastFilterVid,'swL2MulticastFilterVlanMode':swL2MulticastFilterVlanMode,'swL2MulticastFilterModePortTable':swL2MulticastFilterModePortTable,'swL2MulticastFilterModePortEntry':swL2MulticastFilterModePortEntry,_An:swL2MulticastFilterPortIndex,'swL2MulticastFilterPortMode':swL2MulticastFilterPortMode,'swL2LoopDetectMgmt':swL2LoopDetectMgmt,'swL2LoopDetectCtrl':swL2LoopDetectCtrl,'swL2LoopDetectAdminState':swL2LoopDetectAdminState,'swL2LoopDetectInterval':swL2LoopDetectInterval,'swL2LoopDetectRecoverTime':swL2LoopDetectRecoverTime,'swL2LoopDetectMode':swL2LoopDetectMode,'swL2LoopDetectTrapMode':swL2LoopDetectTrapMode,'swL2LoopDetectPortMgmt':swL2LoopDetectPortMgmt,'swL2LoopDetectPortTable':swL2LoopDetectPortTable,'swL2LoopDetectPortEntry':swL2LoopDetectPortEntry,_L:swL2LoopDetectPortIndex,'swL2LoopDetectPortState':swL2LoopDetectPortState,'swL2LoopDetectPortLoopVLAN':swL2LoopDetectPortLoopVLAN,'swL2LoopDetectPortLoopStatus':swL2LoopDetectPortLoopStatus,'swL2MgmtMIBTraps':swL2MgmtMIBTraps,'swL2Notify':swL2Notify,'swL2NotifyMgmt':swL2NotifyMgmt,'swL2macNotificationSeverity':swL2macNotificationSeverity,'swL2PortSecurityViolationSeverity':swL2PortSecurityViolationSeverity,'swL2NotifyPrefix':swL2NotifyPrefix,'swL2NotifFirmware':swL2NotifFirmware,'swL2macNotification':swL2macNotification,'swL2PortSecurityViolationTrap':swL2PortSecurityViolationTrap,'swL2PortLoopOccurred':swL2PortLoopOccurred,'swL2PortLoopRestart':swL2PortLoopRestart,'swL2VlanLoopOccurred':swL2VlanLoopOccurred,'swL2VlanLoopRestart':swL2VlanLoopRestart,'swl2NotificationBidings':swl2NotificationBidings,_Ap:swL2macNotifyInfo,_Aq:swL2PortSecurityViolationMac,_X:swL2VlanLoopDetectVID})