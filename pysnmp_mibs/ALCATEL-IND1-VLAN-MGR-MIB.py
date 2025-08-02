_A2='vlanMgrVlanSetGroup'
_A1='vlanMgrVpaGroup'
_A0='vlanMgrVlanGroup'
_z='vlanSetMultiRtrMacStatus'
_y='vlanSetIpxRouterCount'
_x='vlanSetIpRouterCount'
_w='vlanSetVlanRouterCount'
_v='vlanSetVlanCount'
_u='vpaStatus'
_t='vpaState'
_s='vpaType'
_r='vlanSvlanMacTunnelStatus'
_q='vlanIpxStatus'
_p='vlanIpxDelayTicks'
_o='vlanIpxRipSapMode'
_n='vlanIpxEncap'
_m='vlanIpxNet'
_l='vlanIpStatus'
_k='vlanIpForward'
_j='vlanIpEncap'
_i='vlanIpMask'
_h='vlanIpAddress'
_g='vlanVoiceStatus'
_f='vlanAuthentStatus'
_e='vlanStpStatus'
_d='vlanflatStpStatus'
_c='vlan1x1StpStatus'
_b='vlanStatus'
_a='vlanOperStatus'
_Z='vlanAdmStatus'
_Y='vlanDescription'
_X='vlanHAPortType'
_W='vlanHAPortIfIndex'
_V='vlanHAPortVlanId'
_U='egress'
_T='ingress'
_S='delete'
_R='ethernet2'
_Q='DisplayString'
_P='Unsigned32'
_O='vpaIfIndex'
_N='vpaVlanNumber'
_M='inactive'
_L='vlanNumber'
_K='notApplicable'
_J='disable'
_I='enable'
_H='disabled'
_G='enabled'
_F='read-write'
_E='read-only'
_D='read-create'
_C='Integer32'
_B='ALCATEL-IND1-VLAN-MGR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1VlanMgt,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1VlanMgt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_P,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_Q,'PhysAddress','RowStatus','TextualConvention')
alcatelIND1VLANMgrMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,3,1))
if mibBuilder.loadTexts:alcatelIND1VLANMgrMIB.setRevisions(('2007-04-03 00:00',))
class IpxNetworkAddress(TextualConvention,Unsigned32):status=_A;displayHint='x'
_AlcatelIND1VLANMgrMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1VLANMgrMIBObjects=_AlcatelIND1VLANMgrMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,3,1,1))
if mibBuilder.loadTexts:alcatelIND1VLANMgrMIBObjects.setStatus(_A)
_VlanMgrVlan_ObjectIdentity=ObjectIdentity
vlanMgrVlan=_VlanMgrVlan_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1))
_VlanTable_Object=MibTable
vlanTable=_VlanTable_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1))
if mibBuilder.loadTexts:vlanTable.setStatus(_A)
_VlanEntry_Object=MibTableRow
vlanEntry=_VlanEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1))
vlanEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:vlanEntry.setStatus(_A)
class _VlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanNumber_Type.__name__=_C
_VlanNumber_Object=MibTableColumn
vlanNumber=_VlanNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,1),_VlanNumber_Type())
vlanNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanNumber.setStatus(_A)
class _VlanDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VlanDescription_Type.__name__=_Q
_VlanDescription_Object=MibTableColumn
vlanDescription=_VlanDescription_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,2),_VlanDescription_Type())
vlanDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanDescription.setStatus(_A)
class _VlanAdmStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_VlanAdmStatus_Type.__name__=_C
_VlanAdmStatus_Object=MibTableColumn
vlanAdmStatus=_VlanAdmStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,3),_VlanAdmStatus_Type())
vlanAdmStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanAdmStatus.setStatus(_A)
class _VlanOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),(_M,2)))
_VlanOperStatus_Type.__name__=_C
_VlanOperStatus_Object=MibTableColumn
vlanOperStatus=_VlanOperStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,4),_VlanOperStatus_Type())
vlanOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanOperStatus.setStatus(_A)
_VlanStatus_Type=RowStatus
_VlanStatus_Object=MibTableColumn
vlanStatus=_VlanStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,5),_VlanStatus_Type())
vlanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanStatus.setStatus(_A)
class _VlanStpStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_VlanStpStatus_Type.__name__=_C
_VlanStpStatus_Object=MibTableColumn
vlanStpStatus=_VlanStpStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,6),_VlanStpStatus_Type())
vlanStpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanStpStatus.setStatus(_A)
class _VlanAuthentStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_VlanAuthentStatus_Type.__name__=_C
_VlanAuthentStatus_Object=MibTableColumn
vlanAuthentStatus=_VlanAuthentStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,7),_VlanAuthentStatus_Type())
vlanAuthentStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanAuthentStatus.setStatus(_A)
class _VlanVoiceStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_VlanVoiceStatus_Type.__name__=_C
_VlanVoiceStatus_Object=MibTableColumn
vlanVoiceStatus=_VlanVoiceStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,8),_VlanVoiceStatus_Type())
vlanVoiceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVoiceStatus.setStatus(_A)
_VlanIpAddress_Type=IpAddress
_VlanIpAddress_Object=MibTableColumn
vlanIpAddress=_VlanIpAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,9),_VlanIpAddress_Type())
vlanIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanIpAddress.setStatus(_A)
_VlanIpMask_Type=IpAddress
_VlanIpMask_Object=MibTableColumn
vlanIpMask=_VlanIpMask_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,10),_VlanIpMask_Type())
vlanIpMask.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanIpMask.setStatus(_A)
class _VlanIpEncap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('snap',2),(_K,3)))
_VlanIpEncap_Type.__name__=_C
_VlanIpEncap_Object=MibTableColumn
vlanIpEncap=_VlanIpEncap_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,11),_VlanIpEncap_Type())
vlanIpEncap.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanIpEncap.setStatus(_A)
class _VlanIpForward_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_VlanIpForward_Type.__name__=_C
_VlanIpForward_Object=MibTableColumn
vlanIpForward=_VlanIpForward_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,12),_VlanIpForward_Type())
vlanIpForward.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanIpForward.setStatus(_A)
class _VlanIpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('add',1),(_S,2)))
_VlanIpStatus_Type.__name__=_C
_VlanIpStatus_Object=MibTableColumn
vlanIpStatus=_VlanIpStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,13),_VlanIpStatus_Type())
vlanIpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanIpStatus.setStatus(_A)
_VlanIpxNet_Type=IpxNetworkAddress
_VlanIpxNet_Object=MibTableColumn
vlanIpxNet=_VlanIpxNet_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,14),_VlanIpxNet_Type())
vlanIpxNet.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanIpxNet.setStatus(_A)
class _VlanIpxEncap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),('novellraw',2),('llc',3),('snap',4),(_K,5)))
_VlanIpxEncap_Type.__name__=_C
_VlanIpxEncap_Object=MibTableColumn
vlanIpxEncap=_VlanIpxEncap_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,15),_VlanIpxEncap_Type())
vlanIpxEncap.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanIpxEncap.setStatus(_A)
class _VlanIpxRipSapMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('riponly',1),('ripsap',2),('triggered',3),(_M,4),(_K,5)))
_VlanIpxRipSapMode_Type.__name__=_C
_VlanIpxRipSapMode_Object=MibTableColumn
vlanIpxRipSapMode=_VlanIpxRipSapMode_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,16),_VlanIpxRipSapMode_Type())
vlanIpxRipSapMode.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanIpxRipSapMode.setStatus(_A)
class _VlanIpxDelayTicks_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VlanIpxDelayTicks_Type.__name__=_C
_VlanIpxDelayTicks_Object=MibTableColumn
vlanIpxDelayTicks=_VlanIpxDelayTicks_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,17),_VlanIpxDelayTicks_Type())
vlanIpxDelayTicks.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanIpxDelayTicks.setStatus(_A)
class _VlanIpxStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('add',1),(_S,2)))
_VlanIpxStatus_Type.__name__=_C
_VlanIpxStatus_Object=MibTableColumn
vlanIpxStatus=_VlanIpxStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,18),_VlanIpxStatus_Type())
vlanIpxStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanIpxStatus.setStatus(_A)
class _VlanTagMobilePortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_VlanTagMobilePortStatus_Type.__name__=_C
_VlanTagMobilePortStatus_Object=MibTableColumn
vlanTagMobilePortStatus=_VlanTagMobilePortStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,19),_VlanTagMobilePortStatus_Type())
vlanTagMobilePortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanTagMobilePortStatus.setStatus(_A)
class _VlanPortMacStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_VlanPortMacStatus_Type.__name__=_C
_VlanPortMacStatus_Object=MibTableColumn
vlanPortMacStatus=_VlanPortMacStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,20),_VlanPortMacStatus_Type())
vlanPortMacStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanPortMacStatus.setStatus(_A)
class _VlanLocalProxyArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_VlanLocalProxyArp_Type.__name__=_C
_VlanLocalProxyArp_Object=MibTableColumn
vlanLocalProxyArp=_VlanLocalProxyArp_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,21),_VlanLocalProxyArp_Type())
vlanLocalProxyArp.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanLocalProxyArp.setStatus(_A)
class _VlanMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1280,9198))
_VlanMtu_Type.__name__=_C
_VlanMtu_Object=MibTableColumn
vlanMtu=_VlanMtu_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,22),_VlanMtu_Type())
vlanMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanMtu.setStatus(_A)
class _Vlan1x1StpStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Vlan1x1StpStatus_Type.__name__=_C
_Vlan1x1StpStatus_Object=MibTableColumn
vlan1x1StpStatus=_Vlan1x1StpStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,23),_Vlan1x1StpStatus_Type())
vlan1x1StpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlan1x1StpStatus.setStatus(_A)
class _VlanflatStpStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_VlanflatStpStatus_Type.__name__=_C
_VlanflatStpStatus_Object=MibTableColumn
vlanflatStpStatus=_VlanflatStpStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,24),_VlanflatStpStatus_Type())
vlanflatStpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanflatStpStatus.setStatus(_A)
class _VlanHABandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_VlanHABandwidth_Type.__name__=_C
_VlanHABandwidth_Object=MibTableColumn
vlanHABandwidth=_VlanHABandwidth_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,25),_VlanHABandwidth_Type())
vlanHABandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanHABandwidth.setStatus(_A)
class _VlanSvlanTrafficType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,6,7,8)));namedValues=NamedValues(*((_K,0),('customer',1),('provider',2),('multicastEnterprise',3),('multicastVlanStacking',4),('eServiceCustomer',6),('eServiceManagement',7),('eServiceMulticastVlanStacking',8)))
_VlanSvlanTrafficType_Type.__name__=_C
_VlanSvlanTrafficType_Object=MibTableColumn
vlanSvlanTrafficType=_VlanSvlanTrafficType_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,26),_VlanSvlanTrafficType_Type())
vlanSvlanTrafficType.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanSvlanTrafficType.setStatus(_A)
class _VlanSvlanPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_VlanSvlanPriority_Type.__name__=_C
_VlanSvlanPriority_Object=MibTableColumn
vlanSvlanPriority=_VlanSvlanPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,27),_VlanSvlanPriority_Type())
vlanSvlanPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanSvlanPriority.setStatus(_A)
class _VlanMacLearningControlStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_VlanMacLearningControlStatus_Type.__name__=_C
_VlanMacLearningControlStatus_Object=MibTableColumn
vlanMacLearningControlStatus=_VlanMacLearningControlStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,28),_VlanMacLearningControlStatus_Type())
vlanMacLearningControlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanMacLearningControlStatus.setStatus(_A)
class _VlanSvlanMacTunnelStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_VlanSvlanMacTunnelStatus_Type.__name__=_C
_VlanSvlanMacTunnelStatus_Object=MibTableColumn
vlanSvlanMacTunnelStatus=_VlanSvlanMacTunnelStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,1,1,1,29),_VlanSvlanMacTunnelStatus_Type())
vlanSvlanMacTunnelStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanSvlanMacTunnelStatus.setStatus(_A)
_VlanMgrVpa_ObjectIdentity=ObjectIdentity
vlanMgrVpa=_VlanMgrVpa_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,2))
_VpaTable_Object=MibTable
vpaTable=_VpaTable_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,2,1))
if mibBuilder.loadTexts:vpaTable.setStatus(_A)
_VpaEntry_Object=MibTableRow
vpaEntry=_VpaEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,2,1,1))
vpaEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:vpaEntry.setStatus(_A)
class _VpaVlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VpaVlanNumber_Type.__name__=_C
_VpaVlanNumber_Object=MibTableColumn
vpaVlanNumber=_VpaVlanNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,2,1,1,1),_VpaVlanNumber_Type())
vpaVlanNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:vpaVlanNumber.setStatus(_A)
class _VpaIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,4294967295))
_VpaIfIndex_Type.__name__=_P
_VpaIfIndex_Object=MibTableColumn
vpaIfIndex=_VpaIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,2,1,1,2),_VpaIfIndex_Type())
vpaIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:vpaIfIndex.setStatus(_A)
class _VpaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6,7)));namedValues=NamedValues(*(('cfgDefault',1),('qTagged',2),('mobile',3),('mirrored',4),('svlan',6),('dynamic',7)))
_VpaType_Type.__name__=_C
_VpaType_Object=MibTableColumn
vpaType=_VpaType_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,2,1,1,3),_VpaType_Type())
vpaType.setMaxAccess(_E)
if mibBuilder.loadTexts:vpaType.setStatus(_A)
class _VpaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),('blocking',2),('forwarding',3),('filtering',4)))
_VpaState_Type.__name__=_C
_VpaState_Object=MibTableColumn
vpaState=_VpaState_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,2,1,1,4),_VpaState_Type())
vpaState.setMaxAccess(_E)
if mibBuilder.loadTexts:vpaState.setStatus(_A)
_VpaStatus_Type=RowStatus
_VpaStatus_Object=MibTableColumn
vpaStatus=_VpaStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,2,1,1,5),_VpaStatus_Type())
vpaStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vpaStatus.setStatus(_A)
class _VpaPortMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),(_U,2),('inapplicable',3)))
_VpaPortMacType_Type.__name__=_C
_VpaPortMacType_Object=MibTableColumn
vpaPortMacType=_VpaPortMacType_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,2,1,1,6),_VpaPortMacType_Type())
vpaPortMacType.setMaxAccess(_D)
if mibBuilder.loadTexts:vpaPortMacType.setStatus(_A)
_VlanMgrVlanSet_ObjectIdentity=ObjectIdentity
vlanMgrVlanSet=_VlanMgrVlanSet_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,3))
class _VlanSetVlanCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanSetVlanCount_Type.__name__=_C
_VlanSetVlanCount_Object=MibScalar
vlanSetVlanCount=_VlanSetVlanCount_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,3,1),_VlanSetVlanCount_Type())
vlanSetVlanCount.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanSetVlanCount.setStatus(_A)
class _VlanSetVlanRouterCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_VlanSetVlanRouterCount_Type.__name__=_C
_VlanSetVlanRouterCount_Object=MibScalar
vlanSetVlanRouterCount=_VlanSetVlanRouterCount_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,3,2),_VlanSetVlanRouterCount_Type())
vlanSetVlanRouterCount.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanSetVlanRouterCount.setStatus(_A)
class _VlanSetIpRouterCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_VlanSetIpRouterCount_Type.__name__=_C
_VlanSetIpRouterCount_Object=MibScalar
vlanSetIpRouterCount=_VlanSetIpRouterCount_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,3,3),_VlanSetIpRouterCount_Type())
vlanSetIpRouterCount.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanSetIpRouterCount.setStatus(_A)
class _VlanSetIpxRouterCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_VlanSetIpxRouterCount_Type.__name__=_C
_VlanSetIpxRouterCount_Object=MibScalar
vlanSetIpxRouterCount=_VlanSetIpxRouterCount_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,3,4),_VlanSetIpxRouterCount_Type())
vlanSetIpxRouterCount.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanSetIpxRouterCount.setStatus(_A)
class _VlanSetMultiRtrMacStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_VlanSetMultiRtrMacStatus_Type.__name__=_C
_VlanSetMultiRtrMacStatus_Object=MibScalar
vlanSetMultiRtrMacStatus=_VlanSetMultiRtrMacStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,3,5),_VlanSetMultiRtrMacStatus_Type())
vlanSetMultiRtrMacStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanSetMultiRtrMacStatus.setStatus(_A)
_VlanMgrHAPort_ObjectIdentity=ObjectIdentity
vlanMgrHAPort=_VlanMgrHAPort_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,4))
_VlanHAPortTable_Object=MibTable
vlanHAPortTable=_VlanHAPortTable_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,4,1))
if mibBuilder.loadTexts:vlanHAPortTable.setStatus(_A)
_VlanHAPortEntry_Object=MibTableRow
vlanHAPortEntry=_VlanHAPortEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,4,1,1))
vlanHAPortEntry.setIndexNames((0,_B,_V),(0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:vlanHAPortEntry.setStatus(_A)
class _VlanHAPortVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanHAPortVlanId_Type.__name__=_C
_VlanHAPortVlanId_Object=MibTableColumn
vlanHAPortVlanId=_VlanHAPortVlanId_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,4,1,1,1),_VlanHAPortVlanId_Type())
vlanHAPortVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanHAPortVlanId.setStatus(_A)
_VlanHAPortIfIndex_Type=Unsigned32
_VlanHAPortIfIndex_Object=MibTableColumn
vlanHAPortIfIndex=_VlanHAPortIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,4,1,1,2),_VlanHAPortIfIndex_Type())
vlanHAPortIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanHAPortIfIndex.setStatus(_A)
class _VlanHAPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_VlanHAPortType_Type.__name__=_C
_VlanHAPortType_Object=MibTableColumn
vlanHAPortType=_VlanHAPortType_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,4,1,1,3),_VlanHAPortType_Type())
vlanHAPortType.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanHAPortType.setStatus(_A)
_VlanHAPortRowStatus_Type=RowStatus
_VlanHAPortRowStatus_Object=MibTableColumn
vlanHAPortRowStatus=_VlanHAPortRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,3,1,1,4,1,1,4),_VlanHAPortRowStatus_Type())
vlanHAPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanHAPortRowStatus.setStatus(_A)
_AlcatelIND1VLANMgrMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1VLANMgrMIBConformance=_AlcatelIND1VLANMgrMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,3,1,2))
if mibBuilder.loadTexts:alcatelIND1VLANMgrMIBConformance.setStatus(_A)
_AlcatelIND1VLANMgrMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1VLANMgrMIBGroups=_AlcatelIND1VLANMgrMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,3,1,2,1))
if mibBuilder.loadTexts:alcatelIND1VLANMgrMIBGroups.setStatus(_A)
_AlcatelIND1VLANMgrMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1VLANMgrMIBCompliances=_AlcatelIND1VLANMgrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,3,1,2,2))
if mibBuilder.loadTexts:alcatelIND1VLANMgrMIBCompliances.setStatus(_A)
vlanMgrVlanGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,3,1,2,1,1))
vlanMgrVlanGroup.setObjects(*((_B,_L),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:vlanMgrVlanGroup.setStatus(_A)
vlanMgrVpaGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,3,1,2,1,2))
vlanMgrVpaGroup.setObjects(*((_B,_N),(_B,_O),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:vlanMgrVpaGroup.setStatus(_A)
vlanMgrVlanSetGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,3,1,2,1,3))
vlanMgrVlanSetGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:vlanMgrVlanSetGroup.setStatus(_A)
alcatelIND1VLANMgrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,3,1,2,2,1))
alcatelIND1VLANMgrMIBCompliance.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:alcatelIND1VLANMgrMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IpxNetworkAddress':IpxNetworkAddress,'alcatelIND1VLANMgrMIB':alcatelIND1VLANMgrMIB,'alcatelIND1VLANMgrMIBObjects':alcatelIND1VLANMgrMIBObjects,'vlanMgrVlan':vlanMgrVlan,'vlanTable':vlanTable,'vlanEntry':vlanEntry,_L:vlanNumber,_Y:vlanDescription,_Z:vlanAdmStatus,_a:vlanOperStatus,_b:vlanStatus,_e:vlanStpStatus,_f:vlanAuthentStatus,_g:vlanVoiceStatus,_h:vlanIpAddress,_i:vlanIpMask,_j:vlanIpEncap,_k:vlanIpForward,_l:vlanIpStatus,_m:vlanIpxNet,_n:vlanIpxEncap,_o:vlanIpxRipSapMode,_p:vlanIpxDelayTicks,_q:vlanIpxStatus,'vlanTagMobilePortStatus':vlanTagMobilePortStatus,'vlanPortMacStatus':vlanPortMacStatus,'vlanLocalProxyArp':vlanLocalProxyArp,'vlanMtu':vlanMtu,_c:vlan1x1StpStatus,_d:vlanflatStpStatus,'vlanHABandwidth':vlanHABandwidth,'vlanSvlanTrafficType':vlanSvlanTrafficType,'vlanSvlanPriority':vlanSvlanPriority,'vlanMacLearningControlStatus':vlanMacLearningControlStatus,_r:vlanSvlanMacTunnelStatus,'vlanMgrVpa':vlanMgrVpa,'vpaTable':vpaTable,'vpaEntry':vpaEntry,_N:vpaVlanNumber,_O:vpaIfIndex,_s:vpaType,_t:vpaState,_u:vpaStatus,'vpaPortMacType':vpaPortMacType,'vlanMgrVlanSet':vlanMgrVlanSet,_v:vlanSetVlanCount,_w:vlanSetVlanRouterCount,_x:vlanSetIpRouterCount,_y:vlanSetIpxRouterCount,_z:vlanSetMultiRtrMacStatus,'vlanMgrHAPort':vlanMgrHAPort,'vlanHAPortTable':vlanHAPortTable,'vlanHAPortEntry':vlanHAPortEntry,_V:vlanHAPortVlanId,_W:vlanHAPortIfIndex,_X:vlanHAPortType,'vlanHAPortRowStatus':vlanHAPortRowStatus,'alcatelIND1VLANMgrMIBConformance':alcatelIND1VLANMgrMIBConformance,'alcatelIND1VLANMgrMIBGroups':alcatelIND1VLANMgrMIBGroups,_A0:vlanMgrVlanGroup,_A1:vlanMgrVpaGroup,_A2:vlanMgrVlanSetGroup,'alcatelIND1VLANMgrMIBCompliances':alcatelIND1VLANMgrMIBCompliances,'alcatelIND1VLANMgrMIBCompliance':alcatelIND1VLANMgrMIBCompliance})