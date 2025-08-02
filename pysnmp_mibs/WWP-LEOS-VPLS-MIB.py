_AS='wwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum'
_AR='wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx'
_AQ='wwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum'
_AP='wwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx'
_AO='wwpLeosVplsVirtualSwitchEthL2CftProtocolType'
_AN='not-accessible'
_AM='wwpLeosVplsTunnelPairIndx'
_AL='wwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype'
_AK='wwpLeosVplsSwitchEthCtrlProtocolNum'
_AJ='wwpLeosVplsSwitchMplsCtrlProtocolNum'
_AI='wwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc'
_AH='wwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc'
_AG='transparent'
_AF='wwpLeosVplsVirtualCircuitPortId'
_AE='wwpLeosVplsDecapTunnelId'
_AD='staticPbt'
_AC='wwpLeosVplsEncapTunnelId'
_AB='wwpLeosVplsRsvpAttrIndex'
_AA='wwpLeosVplsMplsPathMemberIpIndex'
_A9='wwpLeosVplsMplsPathOptionIndex'
_A8='wwpLeosVplsSwitchReservedVlanId'
_A7='wwpLeosVplsSwitchCtrlProtocolNum'
_A6='wwpLeosVplsVirtualSwitchMemberPortId'
_A5='wwpLeosVplsVirtualCircuitIndex'
_A4='wwpLeosVplsVirtualSwitchEthEvplMemberVlan'
_A3='wwpLeosVplsVirtualSwitchEthEvplMemberPortId'
_A2='wwpLeosVplsVirtualSwitchMplsEvplMemberVlanId'
_A1='wwpLeosVplsVirtualSwitchMplsEvplMemberPortId'
_A0='wwpLeosVplsVirtualSwitchEthMemberPortId'
_z='wwpLeosVplsVirtualSwitchMplsMemberPortId'
_y='wwpLeosVplsMplsPathIndex'
_x='tunnel'
_w='peer'
_v='inheritTunnel'
_u='ethernet'
_t='TruthValue'
_s='OctetString'
_r='wwpLeosVplsVirtualCircuitEthIndex'
_q='wwpLeosVplsVirtualCircuitMplsIndex'
_p='dynamic'
_o='static'
_n='discard'
_m='inheritVc'
_l='wwpLeosVplsVirtualSwitchIndx'
_k='port-inherit'
_j='ciscoUdlp'
_i='ciscoUplinkFast'
_h='l28021x'
_g='provider-inherit'
_f='vlanBridge'
_e='lldp'
_d='oam'
_c='lacpMarker'
_b='lacp'
_a='gvrp'
_Z='ciscoVtp'
_Y='ciscoPvst'
_X='ciscoPagp'
_W='ciscoDtp'
_V='ciscoCdp'
_U='rstp'
_T='none'
_S='inheritPhbg'
_R='inheritIpPrec'
_Q='inheritDot1dPri'
_P='wwpLeosVplsVirtualSwitchEthIndx'
_O='wwpLeosVplsVirtualSwitchMplsIndx'
_N='inheritVs'
_M='leave'
_L='DisplayString'
_K='Unsigned32'
_J='disabled'
_I='enabled'
_H='fixed'
_G='deprecated'
_F='WWP-LEOS-VPLS-MIB'
_E='read-create'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_s,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'MacAddress','PhysAddress','RowStatus','TextualConvention',_t)
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosVplsMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,28))
if mibBuilder.loadTexts:wwpLeosVplsMIB.setRevisions(('2011-06-06 00:00','2010-03-23 17:00','2010-02-10 17:00','2010-01-27 04:25','2009-08-24 04:24','2008-11-14 00:00','2008-09-03 08:39','2008-06-11 00:50','2008-05-15 00:50','2006-09-22 00:50','2006-05-04 17:00','2005-08-15 17:00'))
class VlanId(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24576))
class EtherType(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2048,65535))
_WwpLeosVplsMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosVplsMIBObjects=_WwpLeosVplsMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,28,1))
_WwpLeosVpls_ObjectIdentity=ObjectIdentity
wwpLeosVpls=_WwpLeosVpls_ObjectIdentity((1,3,6,1,4,1,6141,2,60,28,1,1))
_WwpLeosVplsVirtualCircuitTable_Object=MibTable
wwpLeosVplsVirtualCircuitTable=_WwpLeosVplsVirtualCircuitTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,1))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitTable.setStatus(_G)
_WwpLeosVplsVirtualCircuitEntry_Object=MibTableRow
wwpLeosVplsVirtualCircuitEntry=_WwpLeosVplsVirtualCircuitEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,1,1))
wwpLeosVplsVirtualCircuitEntry.setIndexNames((0,_F,_A5))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEntry.setStatus(_G)
class _WwpLeosVplsVirtualCircuitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualCircuitIndex_Type.__name__=_B
_WwpLeosVplsVirtualCircuitIndex_Object=MibTableColumn
wwpLeosVplsVirtualCircuitIndex=_WwpLeosVplsVirtualCircuitIndex_Object((1,3,6,1,4,1,6141,2,60,28,1,1,1,1,1),_WwpLeosVplsVirtualCircuitIndex_Type())
wwpLeosVplsVirtualCircuitIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitIndex.setStatus(_G)
_WwpLeosVplsVirtualCircuitProviderVlanId_Type=VlanId
_WwpLeosVplsVirtualCircuitProviderVlanId_Object=MibTableColumn
wwpLeosVplsVirtualCircuitProviderVlanId=_WwpLeosVplsVirtualCircuitProviderVlanId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,1,1,2),_WwpLeosVplsVirtualCircuitProviderVlanId_Type())
wwpLeosVplsVirtualCircuitProviderVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitProviderVlanId.setStatus(_G)
class _WwpLeosVplsVirtualCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_u,1),('mpls',2)))
_WwpLeosVplsVirtualCircuitType_Type.__name__=_B
_WwpLeosVplsVirtualCircuitType_Object=MibTableColumn
wwpLeosVplsVirtualCircuitType=_WwpLeosVplsVirtualCircuitType_Object((1,3,6,1,4,1,6141,2,60,28,1,1,1,1,3),_WwpLeosVplsVirtualCircuitType_Type())
wwpLeosVplsVirtualCircuitType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitType.setStatus(_G)
class _WwpLeosVplsVirtualCircuitName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosVplsVirtualCircuitName_Type.__name__=_L
_WwpLeosVplsVirtualCircuitName_Object=MibTableColumn
wwpLeosVplsVirtualCircuitName=_WwpLeosVplsVirtualCircuitName_Object((1,3,6,1,4,1,6141,2,60,28,1,1,1,1,4),_WwpLeosVplsVirtualCircuitName_Type())
wwpLeosVplsVirtualCircuitName.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitName.setStatus(_G)
class _WwpLeosVplsVirtualCircuitIngressVcLabel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1048575))
_WwpLeosVplsVirtualCircuitIngressVcLabel_Type.__name__=_B
_WwpLeosVplsVirtualCircuitIngressVcLabel_Object=MibTableColumn
wwpLeosVplsVirtualCircuitIngressVcLabel=_WwpLeosVplsVirtualCircuitIngressVcLabel_Object((1,3,6,1,4,1,6141,2,60,28,1,1,1,1,5),_WwpLeosVplsVirtualCircuitIngressVcLabel_Type())
wwpLeosVplsVirtualCircuitIngressVcLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitIngressVcLabel.setStatus(_G)
class _WwpLeosVplsVirtualCircuitEgressVcLabel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1048575))
_WwpLeosVplsVirtualCircuitEgressVcLabel_Type.__name__=_B
_WwpLeosVplsVirtualCircuitEgressVcLabel_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEgressVcLabel=_WwpLeosVplsVirtualCircuitEgressVcLabel_Object((1,3,6,1,4,1,6141,2,60,28,1,1,1,1,6),_WwpLeosVplsVirtualCircuitEgressVcLabel_Type())
wwpLeosVplsVirtualCircuitEgressVcLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEgressVcLabel.setStatus(_G)
class _WwpLeosVplsVirtualCircuitTunnelIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualCircuitTunnelIndx_Type.__name__=_B
_WwpLeosVplsVirtualCircuitTunnelIndx_Object=MibTableColumn
wwpLeosVplsVirtualCircuitTunnelIndx=_WwpLeosVplsVirtualCircuitTunnelIndx_Object((1,3,6,1,4,1,6141,2,60,28,1,1,1,1,7),_WwpLeosVplsVirtualCircuitTunnelIndx_Type())
wwpLeosVplsVirtualCircuitTunnelIndx.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitTunnelIndx.setStatus(_G)
_WwpLeosVplsVirtualCircuitStatus_Type=RowStatus
_WwpLeosVplsVirtualCircuitStatus_Object=MibTableColumn
wwpLeosVplsVirtualCircuitStatus=_WwpLeosVplsVirtualCircuitStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,1,1,8),_WwpLeosVplsVirtualCircuitStatus_Type())
wwpLeosVplsVirtualCircuitStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitStatus.setStatus(_G)
_WwpLeosVplsVirtualSwitchTable_Object=MibTable
wwpLeosVplsVirtualSwitchTable=_WwpLeosVplsVirtualSwitchTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,5))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchTable.setStatus(_G)
_WwpLeosVplsVirtualSwitchEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchEntry=_WwpLeosVplsVirtualSwitchEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,5,1))
wwpLeosVplsVirtualSwitchEntry.setIndexNames((0,_F,_l))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEntry.setStatus(_G)
class _WwpLeosVplsVirtualSwitchIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualSwitchIndx_Type.__name__=_B
_WwpLeosVplsVirtualSwitchIndx_Object=MibTableColumn
wwpLeosVplsVirtualSwitchIndx=_WwpLeosVplsVirtualSwitchIndx_Object((1,3,6,1,4,1,6141,2,60,28,1,1,5,1,1),_WwpLeosVplsVirtualSwitchIndx_Type())
wwpLeosVplsVirtualSwitchIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchIndx.setStatus(_G)
class _WwpLeosVplsVirtualSwitchName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WwpLeosVplsVirtualSwitchName_Type.__name__=_s
_WwpLeosVplsVirtualSwitchName_Object=MibTableColumn
wwpLeosVplsVirtualSwitchName=_WwpLeosVplsVirtualSwitchName_Object((1,3,6,1,4,1,6141,2,60,28,1,1,5,1,2),_WwpLeosVplsVirtualSwitchName_Type())
wwpLeosVplsVirtualSwitchName.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchName.setStatus(_G)
class _WwpLeosVplsVirtualSwitchPriVc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosVplsVirtualSwitchPriVc_Type.__name__=_B
_WwpLeosVplsVirtualSwitchPriVc_Object=MibTableColumn
wwpLeosVplsVirtualSwitchPriVc=_WwpLeosVplsVirtualSwitchPriVc_Object((1,3,6,1,4,1,6141,2,60,28,1,1,5,1,3),_WwpLeosVplsVirtualSwitchPriVc_Type())
wwpLeosVplsVirtualSwitchPriVc.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchPriVc.setStatus(_G)
class _WwpLeosVplsVirtualSwitchSecVc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosVplsVirtualSwitchSecVc_Type.__name__=_B
_WwpLeosVplsVirtualSwitchSecVc_Object=MibTableColumn
wwpLeosVplsVirtualSwitchSecVc=_WwpLeosVplsVirtualSwitchSecVc_Object((1,3,6,1,4,1,6141,2,60,28,1,1,5,1,4),_WwpLeosVplsVirtualSwitchSecVc_Type())
wwpLeosVplsVirtualSwitchSecVc.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchSecVc.setStatus(_G)
class _WwpLeosVplsVirtualSwitchActiveVc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),('primVc',2),('secVc',3)))
_WwpLeosVplsVirtualSwitchActiveVc_Type.__name__=_B
_WwpLeosVplsVirtualSwitchActiveVc_Object=MibTableColumn
wwpLeosVplsVirtualSwitchActiveVc=_WwpLeosVplsVirtualSwitchActiveVc_Object((1,3,6,1,4,1,6141,2,60,28,1,1,5,1,5),_WwpLeosVplsVirtualSwitchActiveVc_Type())
wwpLeosVplsVirtualSwitchActiveVc.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchActiveVc.setStatus(_G)
class _WwpLeosVplsVirtualSwitchEncapCosPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_Q,2),(_R,3),(_S,4)))
_WwpLeosVplsVirtualSwitchEncapCosPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEncapCosPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEncapCosPolicy=_WwpLeosVplsVirtualSwitchEncapCosPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,5,1,6),_WwpLeosVplsVirtualSwitchEncapCosPolicy_Type())
wwpLeosVplsVirtualSwitchEncapCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEncapCosPolicy.setStatus(_G)
class _WwpLeosVplsVirtualSwitchEncapFixedDot1dPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsVirtualSwitchEncapFixedDot1dPri_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEncapFixedDot1dPri_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEncapFixedDot1dPri=_WwpLeosVplsVirtualSwitchEncapFixedDot1dPri_Object((1,3,6,1,4,1,6141,2,60,28,1,1,5,1,7),_WwpLeosVplsVirtualSwitchEncapFixedDot1dPri_Type())
wwpLeosVplsVirtualSwitchEncapFixedDot1dPri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEncapFixedDot1dPri.setStatus(_G)
class _WwpLeosVplsVirtualSwitchDecapCosPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_m,2),(_v,3),(_M,4)))
_WwpLeosVplsVirtualSwitchDecapCosPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchDecapCosPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchDecapCosPolicy=_WwpLeosVplsVirtualSwitchDecapCosPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,5,1,8),_WwpLeosVplsVirtualSwitchDecapCosPolicy_Type())
wwpLeosVplsVirtualSwitchDecapCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchDecapCosPolicy.setStatus(_G)
class _WwpLeosVplsVirtualSwitchDecapFixedDot1dPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsVirtualSwitchDecapFixedDot1dPri_Type.__name__=_B
_WwpLeosVplsVirtualSwitchDecapFixedDot1dPri_Object=MibTableColumn
wwpLeosVplsVirtualSwitchDecapFixedDot1dPri=_WwpLeosVplsVirtualSwitchDecapFixedDot1dPri_Object((1,3,6,1,4,1,6141,2,60,28,1,1,5,1,9),_WwpLeosVplsVirtualSwitchDecapFixedDot1dPri_Type())
wwpLeosVplsVirtualSwitchDecapFixedDot1dPri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchDecapFixedDot1dPri.setStatus(_G)
class _WwpLeosVplsVirtualSwitchSubscriberVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_WwpLeosVplsVirtualSwitchSubscriberVlan_Type.__name__=_B
_WwpLeosVplsVirtualSwitchSubscriberVlan_Object=MibTableColumn
wwpLeosVplsVirtualSwitchSubscriberVlan=_WwpLeosVplsVirtualSwitchSubscriberVlan_Object((1,3,6,1,4,1,6141,2,60,28,1,1,5,1,10),_WwpLeosVplsVirtualSwitchSubscriberVlan_Type())
wwpLeosVplsVirtualSwitchSubscriberVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchSubscriberVlan.setStatus(_G)
class _WwpLeosVplsVirtualSwitchCtrlProtocolTunnelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosVplsVirtualSwitchCtrlProtocolTunnelState_Type.__name__=_B
_WwpLeosVplsVirtualSwitchCtrlProtocolTunnelState_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState=_WwpLeosVplsVirtualSwitchCtrlProtocolTunnelState_Object((1,3,6,1,4,1,6141,2,60,28,1,1,5,1,11),_WwpLeosVplsVirtualSwitchCtrlProtocolTunnelState_Type())
wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState.setStatus(_G)
class _WwpLeosVplsVirtualSwitchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_u,1),('mpls',2)))
_WwpLeosVplsVirtualSwitchType_Type.__name__=_B
_WwpLeosVplsVirtualSwitchType_Object=MibTableColumn
wwpLeosVplsVirtualSwitchType=_WwpLeosVplsVirtualSwitchType_Object((1,3,6,1,4,1,6141,2,60,28,1,1,5,1,12),_WwpLeosVplsVirtualSwitchType_Type())
wwpLeosVplsVirtualSwitchType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchType.setStatus(_G)
_WwpLeosVplsVirtualSwitchStatus_Type=RowStatus
_WwpLeosVplsVirtualSwitchStatus_Object=MibTableColumn
wwpLeosVplsVirtualSwitchStatus=_WwpLeosVplsVirtualSwitchStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,5,1,13),_WwpLeosVplsVirtualSwitchStatus_Type())
wwpLeosVplsVirtualSwitchStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchStatus.setStatus(_G)
_WwpLeosVplsVirtualSwitchMemberTable_Object=MibTable
wwpLeosVplsVirtualSwitchMemberTable=_WwpLeosVplsVirtualSwitchMemberTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,6))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMemberTable.setStatus(_G)
_WwpLeosVplsVirtualSwitchMemberEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchMemberEntry=_WwpLeosVplsVirtualSwitchMemberEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,6,1))
wwpLeosVplsVirtualSwitchMemberEntry.setIndexNames((0,_F,_l),(0,_F,_A6))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMemberEntry.setStatus(_G)
class _WwpLeosVplsVirtualSwitchMemberPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualSwitchMemberPortId_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMemberPortId_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMemberPortId=_WwpLeosVplsVirtualSwitchMemberPortId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,6,1,1),_WwpLeosVplsVirtualSwitchMemberPortId_Type())
wwpLeosVplsVirtualSwitchMemberPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMemberPortId.setStatus(_G)
_WwpLeosVplsVirtualSwitchMemberStatus_Type=RowStatus
_WwpLeosVplsVirtualSwitchMemberStatus_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMemberStatus=_WwpLeosVplsVirtualSwitchMemberStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,6,1,2),_WwpLeosVplsVirtualSwitchMemberStatus_Type())
wwpLeosVplsVirtualSwitchMemberStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMemberStatus.setStatus(_G)
_WwpLeosVplsSwitchCtrlProtocolTable_Object=MibTable
wwpLeosVplsSwitchCtrlProtocolTable=_WwpLeosVplsSwitchCtrlProtocolTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,7))
if mibBuilder.loadTexts:wwpLeosVplsSwitchCtrlProtocolTable.setStatus(_G)
_WwpLeosVplsSwitchCtrlProtocolEntry_Object=MibTableRow
wwpLeosVplsSwitchCtrlProtocolEntry=_WwpLeosVplsSwitchCtrlProtocolEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,7,1))
wwpLeosVplsSwitchCtrlProtocolEntry.setIndexNames((0,_F,_l),(0,_F,_A7))
if mibBuilder.loadTexts:wwpLeosVplsSwitchCtrlProtocolEntry.setStatus(_G)
class _WwpLeosVplsSwitchCtrlProtocolNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_h,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_i,7),(_j,8),(_Z,9),(_a,10),(_b,11),(_c,12),(_d,13),(_e,14),(_f,15)))
_WwpLeosVplsSwitchCtrlProtocolNum_Type.__name__=_B
_WwpLeosVplsSwitchCtrlProtocolNum_Object=MibTableColumn
wwpLeosVplsSwitchCtrlProtocolNum=_WwpLeosVplsSwitchCtrlProtocolNum_Object((1,3,6,1,4,1,6141,2,60,28,1,1,7,1,1),_WwpLeosVplsSwitchCtrlProtocolNum_Type())
wwpLeosVplsSwitchCtrlProtocolNum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsSwitchCtrlProtocolNum.setStatus(_G)
class _WwpLeosVplsSwitchCtrlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_n,1),(_w,2),(_x,3)))
_WwpLeosVplsSwitchCtrlType_Type.__name__=_B
_WwpLeosVplsSwitchCtrlType_Object=MibTableColumn
wwpLeosVplsSwitchCtrlType=_WwpLeosVplsSwitchCtrlType_Object((1,3,6,1,4,1,6141,2,60,28,1,1,7,1,2),_WwpLeosVplsSwitchCtrlType_Type())
wwpLeosVplsSwitchCtrlType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsSwitchCtrlType.setStatus(_G)
_WwpLeosVplsSwitchReservedVlanTable_Object=MibTable
wwpLeosVplsSwitchReservedVlanTable=_WwpLeosVplsSwitchReservedVlanTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,8))
if mibBuilder.loadTexts:wwpLeosVplsSwitchReservedVlanTable.setStatus(_A)
_WwpLeosVplsSwitchReservedVlanEntry_Object=MibTableRow
wwpLeosVplsSwitchReservedVlanEntry=_WwpLeosVplsSwitchReservedVlanEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,8,1))
wwpLeosVplsSwitchReservedVlanEntry.setIndexNames((0,_F,_A8))
if mibBuilder.loadTexts:wwpLeosVplsSwitchReservedVlanEntry.setStatus(_A)
class _WwpLeosVplsSwitchReservedVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24576))
_WwpLeosVplsSwitchReservedVlanId_Type.__name__=_B
_WwpLeosVplsSwitchReservedVlanId_Object=MibTableColumn
wwpLeosVplsSwitchReservedVlanId=_WwpLeosVplsSwitchReservedVlanId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,8,1,1),_WwpLeosVplsSwitchReservedVlanId_Type())
wwpLeosVplsSwitchReservedVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsSwitchReservedVlanId.setStatus(_A)
_WwpLeosVplsSwitchReservedVlanStatus_Type=RowStatus
_WwpLeosVplsSwitchReservedVlanStatus_Object=MibTableColumn
wwpLeosVplsSwitchReservedVlanStatus=_WwpLeosVplsSwitchReservedVlanStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,8,1,2),_WwpLeosVplsSwitchReservedVlanStatus_Type())
wwpLeosVplsSwitchReservedVlanStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsSwitchReservedVlanStatus.setStatus(_A)
_WwpLeosVplsGlobalAttrs_ObjectIdentity=ObjectIdentity
wwpLeosVplsGlobalAttrs=_WwpLeosVplsGlobalAttrs_ObjectIdentity((1,3,6,1,4,1,6141,2,60,28,1,1,9))
class _WwpLeosVplsTunnelFixedTTL_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,255))
_WwpLeosVplsTunnelFixedTTL_Type.__name__=_B
_WwpLeosVplsTunnelFixedTTL_Object=MibScalar
wwpLeosVplsTunnelFixedTTL=_WwpLeosVplsTunnelFixedTTL_Object((1,3,6,1,4,1,6141,2,60,28,1,1,9,1),_WwpLeosVplsTunnelFixedTTL_Type())
wwpLeosVplsTunnelFixedTTL.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsTunnelFixedTTL.setStatus(_A)
class _WwpLeosVplsResolverTimeout_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,255))
_WwpLeosVplsResolverTimeout_Type.__name__=_B
_WwpLeosVplsResolverTimeout_Object=MibScalar
wwpLeosVplsResolverTimeout=_WwpLeosVplsResolverTimeout_Object((1,3,6,1,4,1,6141,2,60,28,1,1,9,2),_WwpLeosVplsResolverTimeout_Type())
wwpLeosVplsResolverTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsResolverTimeout.setStatus(_A)
class _WwpLeosVplsStaticLabelRangeStart_Type(Unsigned32):defaultValue=1024;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(16,1048575))
_WwpLeosVplsStaticLabelRangeStart_Type.__name__=_K
_WwpLeosVplsStaticLabelRangeStart_Object=MibScalar
wwpLeosVplsStaticLabelRangeStart=_WwpLeosVplsStaticLabelRangeStart_Object((1,3,6,1,4,1,6141,2,60,28,1,1,9,3),_WwpLeosVplsStaticLabelRangeStart_Type())
wwpLeosVplsStaticLabelRangeStart.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsStaticLabelRangeStart.setStatus(_A)
class _WwpLeosVplsStaticLabelRangeEnd_Type(Unsigned32):defaultValue=2047;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(16,1048575))
_WwpLeosVplsStaticLabelRangeEnd_Type.__name__=_K
_WwpLeosVplsStaticLabelRangeEnd_Object=MibScalar
wwpLeosVplsStaticLabelRangeEnd=_WwpLeosVplsStaticLabelRangeEnd_Object((1,3,6,1,4,1,6141,2,60,28,1,1,9,4),_WwpLeosVplsStaticLabelRangeEnd_Type())
wwpLeosVplsStaticLabelRangeEnd.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsStaticLabelRangeEnd.setStatus(_A)
class _WwpLeosVplsDynamicLabelRangeStart_Type(Unsigned32):defaultValue=2048;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(16,1048575))
_WwpLeosVplsDynamicLabelRangeStart_Type.__name__=_K
_WwpLeosVplsDynamicLabelRangeStart_Object=MibScalar
wwpLeosVplsDynamicLabelRangeStart=_WwpLeosVplsDynamicLabelRangeStart_Object((1,3,6,1,4,1,6141,2,60,28,1,1,9,5),_WwpLeosVplsDynamicLabelRangeStart_Type())
wwpLeosVplsDynamicLabelRangeStart.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsDynamicLabelRangeStart.setStatus(_A)
class _WwpLeosVplsDynamicLabelRangeEnd_Type(Unsigned32):defaultValue=1048575;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(16,1048575))
_WwpLeosVplsDynamicLabelRangeEnd_Type.__name__=_K
_WwpLeosVplsDynamicLabelRangeEnd_Object=MibScalar
wwpLeosVplsDynamicLabelRangeEnd=_WwpLeosVplsDynamicLabelRangeEnd_Object((1,3,6,1,4,1,6141,2,60,28,1,1,9,6),_WwpLeosVplsDynamicLabelRangeEnd_Type())
wwpLeosVplsDynamicLabelRangeEnd.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsDynamicLabelRangeEnd.setStatus(_A)
class _WwpLeosVplsVirtualCircuitStatsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),(_T,2)))
_WwpLeosVplsVirtualCircuitStatsClear_Type.__name__=_B
_WwpLeosVplsVirtualCircuitStatsClear_Object=MibScalar
wwpLeosVplsVirtualCircuitStatsClear=_WwpLeosVplsVirtualCircuitStatsClear_Object((1,3,6,1,4,1,6141,2,60,28,1,1,9,7),_WwpLeosVplsVirtualCircuitStatsClear_Type())
wwpLeosVplsVirtualCircuitStatsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitStatsClear.setStatus(_A)
_WwpLeosVplsMplsPathTable_Object=MibTable
wwpLeosVplsMplsPathTable=_WwpLeosVplsMplsPathTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,10))
if mibBuilder.loadTexts:wwpLeosVplsMplsPathTable.setStatus(_A)
_WwpLeosVplsMplsPathEntry_Object=MibTableRow
wwpLeosVplsMplsPathEntry=_WwpLeosVplsMplsPathEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,10,1))
wwpLeosVplsMplsPathEntry.setIndexNames((0,_F,_y))
if mibBuilder.loadTexts:wwpLeosVplsMplsPathEntry.setStatus(_A)
class _WwpLeosVplsMplsPathIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_WwpLeosVplsMplsPathIndex_Type.__name__=_B
_WwpLeosVplsMplsPathIndex_Object=MibTableColumn
wwpLeosVplsMplsPathIndex=_WwpLeosVplsMplsPathIndex_Object((1,3,6,1,4,1,6141,2,60,28,1,1,10,1,1),_WwpLeosVplsMplsPathIndex_Type())
wwpLeosVplsMplsPathIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsMplsPathIndex.setStatus(_A)
class _WwpLeosVplsMplsPathName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosVplsMplsPathName_Type.__name__=_L
_WwpLeosVplsMplsPathName_Object=MibTableColumn
wwpLeosVplsMplsPathName=_WwpLeosVplsMplsPathName_Object((1,3,6,1,4,1,6141,2,60,28,1,1,10,1,2),_WwpLeosVplsMplsPathName_Type())
wwpLeosVplsMplsPathName.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsMplsPathName.setStatus(_A)
_WwpLeosVplsMplsPathRowStatus_Type=RowStatus
_WwpLeosVplsMplsPathRowStatus_Object=MibTableColumn
wwpLeosVplsMplsPathRowStatus=_WwpLeosVplsMplsPathRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,10,1,3),_WwpLeosVplsMplsPathRowStatus_Type())
wwpLeosVplsMplsPathRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsMplsPathRowStatus.setStatus(_A)
_WwpLeosVplsMplsPathMemberTable_Object=MibTable
wwpLeosVplsMplsPathMemberTable=_WwpLeosVplsMplsPathMemberTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,11))
if mibBuilder.loadTexts:wwpLeosVplsMplsPathMemberTable.setStatus(_A)
_WwpLeosVplsMplsPathMemberEntry_Object=MibTableRow
wwpLeosVplsMplsPathMemberEntry=_WwpLeosVplsMplsPathMemberEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,11,1))
wwpLeosVplsMplsPathMemberEntry.setIndexNames((0,_F,_y),(0,_F,_A9),(0,_F,_AA))
if mibBuilder.loadTexts:wwpLeosVplsMplsPathMemberEntry.setStatus(_A)
class _WwpLeosVplsMplsPathOptionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_WwpLeosVplsMplsPathOptionIndex_Type.__name__=_B
_WwpLeosVplsMplsPathOptionIndex_Object=MibTableColumn
wwpLeosVplsMplsPathOptionIndex=_WwpLeosVplsMplsPathOptionIndex_Object((1,3,6,1,4,1,6141,2,60,28,1,1,11,1,1),_WwpLeosVplsMplsPathOptionIndex_Type())
wwpLeosVplsMplsPathOptionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsMplsPathOptionIndex.setStatus(_A)
class _WwpLeosVplsMplsPathMemberIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_WwpLeosVplsMplsPathMemberIpIndex_Type.__name__=_B
_WwpLeosVplsMplsPathMemberIpIndex_Object=MibTableColumn
wwpLeosVplsMplsPathMemberIpIndex=_WwpLeosVplsMplsPathMemberIpIndex_Object((1,3,6,1,4,1,6141,2,60,28,1,1,11,1,2),_WwpLeosVplsMplsPathMemberIpIndex_Type())
wwpLeosVplsMplsPathMemberIpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsMplsPathMemberIpIndex.setStatus(_A)
_WwpLeosVplsMplsPathMemberIp_Type=IpAddress
_WwpLeosVplsMplsPathMemberIp_Object=MibTableColumn
wwpLeosVplsMplsPathMemberIp=_WwpLeosVplsMplsPathMemberIp_Object((1,3,6,1,4,1,6141,2,60,28,1,1,11,1,3),_WwpLeosVplsMplsPathMemberIp_Type())
wwpLeosVplsMplsPathMemberIp.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsMplsPathMemberIp.setStatus(_A)
_WwpLeosVplsMplsPathMemberRowStatus_Type=RowStatus
_WwpLeosVplsMplsPathMemberRowStatus_Object=MibTableColumn
wwpLeosVplsMplsPathMemberRowStatus=_WwpLeosVplsMplsPathMemberRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,11,1,4),_WwpLeosVplsMplsPathMemberRowStatus_Type())
wwpLeosVplsMplsPathMemberRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsMplsPathMemberRowStatus.setStatus(_A)
_WwpLeosVplsRsvpAttrTable_Object=MibTable
wwpLeosVplsRsvpAttrTable=_WwpLeosVplsRsvpAttrTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,12))
if mibBuilder.loadTexts:wwpLeosVplsRsvpAttrTable.setStatus(_A)
_WwpLeosVplsRsvpAttrEntry_Object=MibTableRow
wwpLeosVplsRsvpAttrEntry=_WwpLeosVplsRsvpAttrEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,12,1))
wwpLeosVplsRsvpAttrEntry.setIndexNames((0,_F,_AB))
if mibBuilder.loadTexts:wwpLeosVplsRsvpAttrEntry.setStatus(_A)
class _WwpLeosVplsRsvpAttrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsRsvpAttrIndex_Type.__name__=_B
_WwpLeosVplsRsvpAttrIndex_Object=MibTableColumn
wwpLeosVplsRsvpAttrIndex=_WwpLeosVplsRsvpAttrIndex_Object((1,3,6,1,4,1,6141,2,60,28,1,1,12,1,1),_WwpLeosVplsRsvpAttrIndex_Type())
wwpLeosVplsRsvpAttrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsRsvpAttrIndex.setStatus(_A)
class _WwpLeosVplsRsvpAttrHoldPri_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsRsvpAttrHoldPri_Type.__name__=_B
_WwpLeosVplsRsvpAttrHoldPri_Object=MibTableColumn
wwpLeosVplsRsvpAttrHoldPri=_WwpLeosVplsRsvpAttrHoldPri_Object((1,3,6,1,4,1,6141,2,60,28,1,1,12,1,2),_WwpLeosVplsRsvpAttrHoldPri_Type())
wwpLeosVplsRsvpAttrHoldPri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsRsvpAttrHoldPri.setStatus(_A)
class _WwpLeosVplsRsvpAttrSetupPri_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsRsvpAttrSetupPri_Type.__name__=_B
_WwpLeosVplsRsvpAttrSetupPri_Object=MibTableColumn
wwpLeosVplsRsvpAttrSetupPri=_WwpLeosVplsRsvpAttrSetupPri_Object((1,3,6,1,4,1,6141,2,60,28,1,1,12,1,3),_WwpLeosVplsRsvpAttrSetupPri_Type())
wwpLeosVplsRsvpAttrSetupPri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsRsvpAttrSetupPri.setStatus(_A)
class _WwpLeosVplsRsvpAttrRecordRoute_Type(TruthValue):defaultValue=2
_WwpLeosVplsRsvpAttrRecordRoute_Type.__name__=_t
_WwpLeosVplsRsvpAttrRecordRoute_Object=MibTableColumn
wwpLeosVplsRsvpAttrRecordRoute=_WwpLeosVplsRsvpAttrRecordRoute_Object((1,3,6,1,4,1,6141,2,60,28,1,1,12,1,4),_WwpLeosVplsRsvpAttrRecordRoute_Type())
wwpLeosVplsRsvpAttrRecordRoute.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsRsvpAttrRecordRoute.setStatus(_A)
_WwpLeosVplsEncapTunnelTable_Object=MibTable
wwpLeosVplsEncapTunnelTable=_WwpLeosVplsEncapTunnelTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13))
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelTable.setStatus(_A)
_WwpLeosVplsEncapTunnelEntry_Object=MibTableRow
wwpLeosVplsEncapTunnelEntry=_WwpLeosVplsEncapTunnelEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1))
wwpLeosVplsEncapTunnelEntry.setIndexNames((0,_F,_AC))
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelEntry.setStatus(_A)
class _WwpLeosVplsEncapTunnelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsEncapTunnelId_Type.__name__=_B
_WwpLeosVplsEncapTunnelId_Object=MibTableColumn
wwpLeosVplsEncapTunnelId=_WwpLeosVplsEncapTunnelId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,1),_WwpLeosVplsEncapTunnelId_Type())
wwpLeosVplsEncapTunnelId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelId.setStatus(_A)
class _WwpLeosVplsEncapTunnelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosVplsEncapTunnelName_Type.__name__=_L
_WwpLeosVplsEncapTunnelName_Object=MibTableColumn
wwpLeosVplsEncapTunnelName=_WwpLeosVplsEncapTunnelName_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,2),_WwpLeosVplsEncapTunnelName_Type())
wwpLeosVplsEncapTunnelName.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelName.setStatus(_A)
class _WwpLeosVplsEncapTunnelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_o,1),(_p,2),(_AD,3)))
_WwpLeosVplsEncapTunnelType_Type.__name__=_B
_WwpLeosVplsEncapTunnelType_Object=MibTableColumn
wwpLeosVplsEncapTunnelType=_WwpLeosVplsEncapTunnelType_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,3),_WwpLeosVplsEncapTunnelType_Type())
wwpLeosVplsEncapTunnelType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelType.setStatus(_A)
_WwpLeosVplsEncapTunnelDestAddr_Type=IpAddress
_WwpLeosVplsEncapTunnelDestAddr_Object=MibTableColumn
wwpLeosVplsEncapTunnelDestAddr=_WwpLeosVplsEncapTunnelDestAddr_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,4),_WwpLeosVplsEncapTunnelDestAddr_Type())
wwpLeosVplsEncapTunnelDestAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelDestAddr.setStatus(_A)
_WwpLeosVplsEncapTunnelPathIndex_Type=Integer32
_WwpLeosVplsEncapTunnelPathIndex_Object=MibTableColumn
wwpLeosVplsEncapTunnelPathIndex=_WwpLeosVplsEncapTunnelPathIndex_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,5),_WwpLeosVplsEncapTunnelPathIndex_Type())
wwpLeosVplsEncapTunnelPathIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelPathIndex.setStatus(_A)
class _WwpLeosVplsEncapTunnelEncapCosPolicy_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_m,2),(_N,3),('rcosMapped',4)))
_WwpLeosVplsEncapTunnelEncapCosPolicy_Type.__name__=_B
_WwpLeosVplsEncapTunnelEncapCosPolicy_Object=MibTableColumn
wwpLeosVplsEncapTunnelEncapCosPolicy=_WwpLeosVplsEncapTunnelEncapCosPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,6),_WwpLeosVplsEncapTunnelEncapCosPolicy_Type())
wwpLeosVplsEncapTunnelEncapCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelEncapCosPolicy.setStatus(_A)
class _WwpLeosVplsEncapTunnelEncapFixedExp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsEncapTunnelEncapFixedExp_Type.__name__=_B
_WwpLeosVplsEncapTunnelEncapFixedExp_Object=MibTableColumn
wwpLeosVplsEncapTunnelEncapFixedExp=_WwpLeosVplsEncapTunnelEncapFixedExp_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,7),_WwpLeosVplsEncapTunnelEncapFixedExp_Type())
wwpLeosVplsEncapTunnelEncapFixedExp.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelEncapFixedExp.setStatus(_A)
class _WwpLeosVplsEncapTunnelTTLPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pipe',1),('uniform',2)))
_WwpLeosVplsEncapTunnelTTLPolicy_Type.__name__=_B
_WwpLeosVplsEncapTunnelTTLPolicy_Object=MibTableColumn
wwpLeosVplsEncapTunnelTTLPolicy=_WwpLeosVplsEncapTunnelTTLPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,8),_WwpLeosVplsEncapTunnelTTLPolicy_Type())
wwpLeosVplsEncapTunnelTTLPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelTTLPolicy.setStatus(_A)
class _WwpLeosVplsEncapTunnelEncapLabel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048576))
_WwpLeosVplsEncapTunnelEncapLabel_Type.__name__=_K
_WwpLeosVplsEncapTunnelEncapLabel_Object=MibTableColumn
wwpLeosVplsEncapTunnelEncapLabel=_WwpLeosVplsEncapTunnelEncapLabel_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,9),_WwpLeosVplsEncapTunnelEncapLabel_Type())
wwpLeosVplsEncapTunnelEncapLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelEncapLabel.setStatus(_A)
class _WwpLeosVplsEncapTunnelProtType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('rsvp',2)))
_WwpLeosVplsEncapTunnelProtType_Type.__name__=_B
_WwpLeosVplsEncapTunnelProtType_Object=MibTableColumn
wwpLeosVplsEncapTunnelProtType=_WwpLeosVplsEncapTunnelProtType_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,10),_WwpLeosVplsEncapTunnelProtType_Type())
wwpLeosVplsEncapTunnelProtType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelProtType.setStatus(_A)
_WwpLeosVplsEncapTunnelDestResolvedMac_Type=MacAddress
_WwpLeosVplsEncapTunnelDestResolvedMac_Object=MibTableColumn
wwpLeosVplsEncapTunnelDestResolvedMac=_WwpLeosVplsEncapTunnelDestResolvedMac_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,11),_WwpLeosVplsEncapTunnelDestResolvedMac_Type())
wwpLeosVplsEncapTunnelDestResolvedMac.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelDestResolvedMac.setStatus(_A)
class _WwpLeosVplsEncapTunnelOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosVplsEncapTunnelOperStatus_Type.__name__=_B
_WwpLeosVplsEncapTunnelOperStatus_Object=MibTableColumn
wwpLeosVplsEncapTunnelOperStatus=_WwpLeosVplsEncapTunnelOperStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,12),_WwpLeosVplsEncapTunnelOperStatus_Type())
wwpLeosVplsEncapTunnelOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelOperStatus.setStatus(_A)
class _WwpLeosVplsEncapTunnelAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosVplsEncapTunnelAdminStatus_Type.__name__=_B
_WwpLeosVplsEncapTunnelAdminStatus_Object=MibTableColumn
wwpLeosVplsEncapTunnelAdminStatus=_WwpLeosVplsEncapTunnelAdminStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,13),_WwpLeosVplsEncapTunnelAdminStatus_Type())
wwpLeosVplsEncapTunnelAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelAdminStatus.setStatus(_A)
class _WwpLeosVplsEncapTunnelDestResolvedPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosVplsEncapTunnelDestResolvedPort_Type.__name__=_B
_WwpLeosVplsEncapTunnelDestResolvedPort_Object=MibTableColumn
wwpLeosVplsEncapTunnelDestResolvedPort=_WwpLeosVplsEncapTunnelDestResolvedPort_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,14),_WwpLeosVplsEncapTunnelDestResolvedPort_Type())
wwpLeosVplsEncapTunnelDestResolvedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelDestResolvedPort.setStatus(_A)
class _WwpLeosVplsEncapTunnelDestResolvedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_WwpLeosVplsEncapTunnelDestResolvedVlan_Type.__name__=_B
_WwpLeosVplsEncapTunnelDestResolvedVlan_Object=MibTableColumn
wwpLeosVplsEncapTunnelDestResolvedVlan=_WwpLeosVplsEncapTunnelDestResolvedVlan_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,15),_WwpLeosVplsEncapTunnelDestResolvedVlan_Type())
wwpLeosVplsEncapTunnelDestResolvedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelDestResolvedVlan.setStatus(_A)
_WwpLeosVplsEncapTunnelRowStatus_Type=RowStatus
_WwpLeosVplsEncapTunnelRowStatus_Object=MibTableColumn
wwpLeosVplsEncapTunnelRowStatus=_WwpLeosVplsEncapTunnelRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,16),_WwpLeosVplsEncapTunnelRowStatus_Type())
wwpLeosVplsEncapTunnelRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelRowStatus.setStatus(_A)
class _WwpLeosVplsEncapTunnelFastReroute_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('linkProtect',1),('nodeProtect',2)))
_WwpLeosVplsEncapTunnelFastReroute_Type.__name__=_B
_WwpLeosVplsEncapTunnelFastReroute_Object=MibTableColumn
wwpLeosVplsEncapTunnelFastReroute=_WwpLeosVplsEncapTunnelFastReroute_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,17),_WwpLeosVplsEncapTunnelFastReroute_Type())
wwpLeosVplsEncapTunnelFastReroute.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelFastReroute.setStatus(_A)
class _WwpLeosVplsEncapTunnelLspType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('backup',2)))
_WwpLeosVplsEncapTunnelLspType_Type.__name__=_B
_WwpLeosVplsEncapTunnelLspType_Object=MibTableColumn
wwpLeosVplsEncapTunnelLspType=_WwpLeosVplsEncapTunnelLspType_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,18),_WwpLeosVplsEncapTunnelLspType_Type())
wwpLeosVplsEncapTunnelLspType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelLspType.setStatus(_A)
class _WwpLeosVplsEncapTunnelPartnerTunnelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsEncapTunnelPartnerTunnelId_Type.__name__=_B
_WwpLeosVplsEncapTunnelPartnerTunnelId_Object=MibTableColumn
wwpLeosVplsEncapTunnelPartnerTunnelId=_WwpLeosVplsEncapTunnelPartnerTunnelId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,19),_WwpLeosVplsEncapTunnelPartnerTunnelId_Type())
wwpLeosVplsEncapTunnelPartnerTunnelId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelPartnerTunnelId.setStatus(_A)
_WwpLeosVplsEncapTunnelBVID_Type=VlanId
_WwpLeosVplsEncapTunnelBVID_Object=MibTableColumn
wwpLeosVplsEncapTunnelBVID=_WwpLeosVplsEncapTunnelBVID_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,20),_WwpLeosVplsEncapTunnelBVID_Type())
wwpLeosVplsEncapTunnelBVID.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelBVID.setStatus(_A)
class _WwpLeosVplsEncapTunnelDestBridgeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_WwpLeosVplsEncapTunnelDestBridgeIndex_Type.__name__=_B
_WwpLeosVplsEncapTunnelDestBridgeIndex_Object=MibTableColumn
wwpLeosVplsEncapTunnelDestBridgeIndex=_WwpLeosVplsEncapTunnelDestBridgeIndex_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,21),_WwpLeosVplsEncapTunnelDestBridgeIndex_Type())
wwpLeosVplsEncapTunnelDestBridgeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelDestBridgeIndex.setStatus(_A)
_WwpLeosVplsEncapTunnelEgressPort_Type=Integer32
_WwpLeosVplsEncapTunnelEgressPort_Object=MibTableColumn
wwpLeosVplsEncapTunnelEgressPort=_WwpLeosVplsEncapTunnelEgressPort_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,22),_WwpLeosVplsEncapTunnelEgressPort_Type())
wwpLeosVplsEncapTunnelEgressPort.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelEgressPort.setStatus(_A)
class _WwpLeosVplsEncapTunnelEncapFixedPCP_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsEncapTunnelEncapFixedPCP_Type.__name__=_B
_WwpLeosVplsEncapTunnelEncapFixedPCP_Object=MibTableColumn
wwpLeosVplsEncapTunnelEncapFixedPCP=_WwpLeosVplsEncapTunnelEncapFixedPCP_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,23),_WwpLeosVplsEncapTunnelEncapFixedPCP_Type())
wwpLeosVplsEncapTunnelEncapFixedPCP.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelEncapFixedPCP.setStatus(_A)
class _WwpLeosVplsEncapTunnelActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_WwpLeosVplsEncapTunnelActive_Type.__name__=_B
_WwpLeosVplsEncapTunnelActive_Object=MibTableColumn
wwpLeosVplsEncapTunnelActive=_WwpLeosVplsEncapTunnelActive_Object((1,3,6,1,4,1,6141,2,60,28,1,1,13,1,24),_WwpLeosVplsEncapTunnelActive_Type())
wwpLeosVplsEncapTunnelActive.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsEncapTunnelActive.setStatus(_A)
_WwpLeosVplsDecapTunnelTable_Object=MibTable
wwpLeosVplsDecapTunnelTable=_WwpLeosVplsDecapTunnelTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,14))
if mibBuilder.loadTexts:wwpLeosVplsDecapTunnelTable.setStatus(_A)
_WwpLeosVplsDecapTunnelEntry_Object=MibTableRow
wwpLeosVplsDecapTunnelEntry=_WwpLeosVplsDecapTunnelEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,14,1))
wwpLeosVplsDecapTunnelEntry.setIndexNames((0,_F,_AE))
if mibBuilder.loadTexts:wwpLeosVplsDecapTunnelEntry.setStatus(_A)
class _WwpLeosVplsDecapTunnelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsDecapTunnelId_Type.__name__=_B
_WwpLeosVplsDecapTunnelId_Object=MibTableColumn
wwpLeosVplsDecapTunnelId=_WwpLeosVplsDecapTunnelId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,14,1,1),_WwpLeosVplsDecapTunnelId_Type())
wwpLeosVplsDecapTunnelId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsDecapTunnelId.setStatus(_A)
class _WwpLeosVplsDecapTunnelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosVplsDecapTunnelName_Type.__name__=_L
_WwpLeosVplsDecapTunnelName_Object=MibTableColumn
wwpLeosVplsDecapTunnelName=_WwpLeosVplsDecapTunnelName_Object((1,3,6,1,4,1,6141,2,60,28,1,1,14,1,2),_WwpLeosVplsDecapTunnelName_Type())
wwpLeosVplsDecapTunnelName.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsDecapTunnelName.setStatus(_A)
class _WwpLeosVplsDecapTunnelLabel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048576))
_WwpLeosVplsDecapTunnelLabel_Type.__name__=_K
_WwpLeosVplsDecapTunnelLabel_Object=MibTableColumn
wwpLeosVplsDecapTunnelLabel=_WwpLeosVplsDecapTunnelLabel_Object((1,3,6,1,4,1,6141,2,60,28,1,1,14,1,3),_WwpLeosVplsDecapTunnelLabel_Type())
wwpLeosVplsDecapTunnelLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsDecapTunnelLabel.setStatus(_A)
class _WwpLeosVplsDecapTunnelType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_o,1),(_p,2),(_AD,3)))
_WwpLeosVplsDecapTunnelType_Type.__name__=_B
_WwpLeosVplsDecapTunnelType_Object=MibTableColumn
wwpLeosVplsDecapTunnelType=_WwpLeosVplsDecapTunnelType_Object((1,3,6,1,4,1,6141,2,60,28,1,1,14,1,4),_WwpLeosVplsDecapTunnelType_Type())
wwpLeosVplsDecapTunnelType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsDecapTunnelType.setStatus(_A)
_WwpLeosVplsDecapTunnelRowStatus_Type=RowStatus
_WwpLeosVplsDecapTunnelRowStatus_Object=MibTableColumn
wwpLeosVplsDecapTunnelRowStatus=_WwpLeosVplsDecapTunnelRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,14,1,5),_WwpLeosVplsDecapTunnelRowStatus_Type())
wwpLeosVplsDecapTunnelRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsDecapTunnelRowStatus.setStatus(_A)
_WwpLeosVplsDecapTunnelBVID_Type=Integer32
_WwpLeosVplsDecapTunnelBVID_Object=MibTableColumn
wwpLeosVplsDecapTunnelBVID=_WwpLeosVplsDecapTunnelBVID_Object((1,3,6,1,4,1,6141,2,60,28,1,1,14,1,6),_WwpLeosVplsDecapTunnelBVID_Type())
wwpLeosVplsDecapTunnelBVID.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsDecapTunnelBVID.setStatus(_A)
class _WwpLeosVplsDecapTunnelBridgeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_WwpLeosVplsDecapTunnelBridgeIndex_Type.__name__=_B
_WwpLeosVplsDecapTunnelBridgeIndex_Object=MibTableColumn
wwpLeosVplsDecapTunnelBridgeIndex=_WwpLeosVplsDecapTunnelBridgeIndex_Object((1,3,6,1,4,1,6141,2,60,28,1,1,14,1,7),_WwpLeosVplsDecapTunnelBridgeIndex_Type())
wwpLeosVplsDecapTunnelBridgeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsDecapTunnelBridgeIndex.setStatus(_A)
_WwpLeosVplsDecapTunnelPort_Type=Integer32
_WwpLeosVplsDecapTunnelPort_Object=MibTableColumn
wwpLeosVplsDecapTunnelPort=_WwpLeosVplsDecapTunnelPort_Object((1,3,6,1,4,1,6141,2,60,28,1,1,14,1,8),_WwpLeosVplsDecapTunnelPort_Type())
wwpLeosVplsDecapTunnelPort.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsDecapTunnelPort.setStatus(_A)
_WwpLeosVplsDecapTunnelMac_Type=MacAddress
_WwpLeosVplsDecapTunnelMac_Object=MibTableColumn
wwpLeosVplsDecapTunnelMac=_WwpLeosVplsDecapTunnelMac_Object((1,3,6,1,4,1,6141,2,60,28,1,1,14,1,9),_WwpLeosVplsDecapTunnelMac_Type())
wwpLeosVplsDecapTunnelMac.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsDecapTunnelMac.setStatus(_A)
class _WwpLeosVplsDecapTunnelOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosVplsDecapTunnelOperStatus_Type.__name__=_B
_WwpLeosVplsDecapTunnelOperStatus_Object=MibTableColumn
wwpLeosVplsDecapTunnelOperStatus=_WwpLeosVplsDecapTunnelOperStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,14,1,10),_WwpLeosVplsDecapTunnelOperStatus_Type())
wwpLeosVplsDecapTunnelOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsDecapTunnelOperStatus.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsTable_Object=MibTable
wwpLeosVplsVirtualCircuitMplsTable=_WwpLeosVplsVirtualCircuitMplsTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsTable.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsEntry_Object=MibTableRow
wwpLeosVplsVirtualCircuitMplsEntry=_WwpLeosVplsVirtualCircuitMplsEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1))
wwpLeosVplsVirtualCircuitMplsEntry.setIndexNames((0,_F,_q))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsEntry.setStatus(_A)
class _WwpLeosVplsVirtualCircuitMplsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualCircuitMplsIndex_Type.__name__=_B
_WwpLeosVplsVirtualCircuitMplsIndex_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsIndex=_WwpLeosVplsVirtualCircuitMplsIndex_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1,1),_WwpLeosVplsVirtualCircuitMplsIndex_Type())
wwpLeosVplsVirtualCircuitMplsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsIndex.setStatus(_A)
class _WwpLeosVplsVirtualCircuitMplsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosVplsVirtualCircuitMplsName_Type.__name__=_L
_WwpLeosVplsVirtualCircuitMplsName_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsName=_WwpLeosVplsVirtualCircuitMplsName_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1,2),_WwpLeosVplsVirtualCircuitMplsName_Type())
wwpLeosVplsVirtualCircuitMplsName.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsName.setStatus(_A)
class _WwpLeosVplsVirtualCircuitMplsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_p,1),(_o,2)))
_WwpLeosVplsVirtualCircuitMplsType_Type.__name__=_B
_WwpLeosVplsVirtualCircuitMplsType_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsType=_WwpLeosVplsVirtualCircuitMplsType_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1,3),_WwpLeosVplsVirtualCircuitMplsType_Type())
wwpLeosVplsVirtualCircuitMplsType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsType.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsDestAddr_Type=IpAddress
_WwpLeosVplsVirtualCircuitMplsDestAddr_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsDestAddr=_WwpLeosVplsVirtualCircuitMplsDestAddr_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1,4),_WwpLeosVplsVirtualCircuitMplsDestAddr_Type())
wwpLeosVplsVirtualCircuitMplsDestAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsDestAddr.setStatus(_A)
class _WwpLeosVplsVirtualCircuitMplsTunnelPolicy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('firstAvailable',2)))
_WwpLeosVplsVirtualCircuitMplsTunnelPolicy_Type.__name__=_B
_WwpLeosVplsVirtualCircuitMplsTunnelPolicy_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsTunnelPolicy=_WwpLeosVplsVirtualCircuitMplsTunnelPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1,5),_WwpLeosVplsVirtualCircuitMplsTunnelPolicy_Type())
wwpLeosVplsVirtualCircuitMplsTunnelPolicy.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsTunnelPolicy.setStatus(_A)
class _WwpLeosVplsVirtualCircuitMplsFixedTunnelId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosVplsVirtualCircuitMplsFixedTunnelId_Type.__name__=_B
_WwpLeosVplsVirtualCircuitMplsFixedTunnelId_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsFixedTunnelId=_WwpLeosVplsVirtualCircuitMplsFixedTunnelId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1,6),_WwpLeosVplsVirtualCircuitMplsFixedTunnelId_Type())
wwpLeosVplsVirtualCircuitMplsFixedTunnelId.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsFixedTunnelId.setStatus(_A)
class _WwpLeosVplsVirtualCircuitMplsActiveTunnelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosVplsVirtualCircuitMplsActiveTunnelId_Type.__name__=_B
_WwpLeosVplsVirtualCircuitMplsActiveTunnelId_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsActiveTunnelId=_WwpLeosVplsVirtualCircuitMplsActiveTunnelId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1,7),_WwpLeosVplsVirtualCircuitMplsActiveTunnelId_Type())
wwpLeosVplsVirtualCircuitMplsActiveTunnelId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsActiveTunnelId.setStatus(_A)
class _WwpLeosVplsVirtualCircuitMplsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosVplsVirtualCircuitMplsOperStatus_Type.__name__=_B
_WwpLeosVplsVirtualCircuitMplsOperStatus_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsOperStatus=_WwpLeosVplsVirtualCircuitMplsOperStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1,8),_WwpLeosVplsVirtualCircuitMplsOperStatus_Type())
wwpLeosVplsVirtualCircuitMplsOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsOperStatus.setStatus(_A)
class _WwpLeosVplsVirtualCircuitMplsEncapLabel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048576))
_WwpLeosVplsVirtualCircuitMplsEncapLabel_Type.__name__=_K
_WwpLeosVplsVirtualCircuitMplsEncapLabel_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsEncapLabel=_WwpLeosVplsVirtualCircuitMplsEncapLabel_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1,9),_WwpLeosVplsVirtualCircuitMplsEncapLabel_Type())
wwpLeosVplsVirtualCircuitMplsEncapLabel.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsEncapLabel.setStatus(_A)
class _WwpLeosVplsVirtualCircuitMplsDecapLabel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048576))
_WwpLeosVplsVirtualCircuitMplsDecapLabel_Type.__name__=_K
_WwpLeosVplsVirtualCircuitMplsDecapLabel_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsDecapLabel=_WwpLeosVplsVirtualCircuitMplsDecapLabel_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1,10),_WwpLeosVplsVirtualCircuitMplsDecapLabel_Type())
wwpLeosVplsVirtualCircuitMplsDecapLabel.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsDecapLabel.setStatus(_A)
class _WwpLeosVplsVirtualCircuitMplsGroupId_Type(Unsigned32):defaultValue=0
_WwpLeosVplsVirtualCircuitMplsGroupId_Type.__name__=_K
_WwpLeosVplsVirtualCircuitMplsGroupId_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsGroupId=_WwpLeosVplsVirtualCircuitMplsGroupId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1,11),_WwpLeosVplsVirtualCircuitMplsGroupId_Type())
wwpLeosVplsVirtualCircuitMplsGroupId.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsGroupId.setStatus(_A)
class _WwpLeosVplsVirtualCircuitMplsProtectionType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_WwpLeosVplsVirtualCircuitMplsProtectionType_Type.__name__=_B
_WwpLeosVplsVirtualCircuitMplsProtectionType_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsProtectionType=_WwpLeosVplsVirtualCircuitMplsProtectionType_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1,12),_WwpLeosVplsVirtualCircuitMplsProtectionType_Type())
wwpLeosVplsVirtualCircuitMplsProtectionType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsProtectionType.setStatus(_A)
class _WwpLeosVplsVirtualCircuitMplsStatusTlv_Type(TruthValue):defaultValue=2
_WwpLeosVplsVirtualCircuitMplsStatusTlv_Type.__name__=_t
_WwpLeosVplsVirtualCircuitMplsStatusTlv_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsStatusTlv=_WwpLeosVplsVirtualCircuitMplsStatusTlv_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1,13),_WwpLeosVplsVirtualCircuitMplsStatusTlv_Type())
wwpLeosVplsVirtualCircuitMplsStatusTlv.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsStatusTlv.setStatus(_A)
class _WwpLeosVplsVirtualCircuitMplsMtu_Type(Integer32):defaultValue=9190;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1500,9216))
_WwpLeosVplsVirtualCircuitMplsMtu_Type.__name__=_B
_WwpLeosVplsVirtualCircuitMplsMtu_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsMtu=_WwpLeosVplsVirtualCircuitMplsMtu_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1,14),_WwpLeosVplsVirtualCircuitMplsMtu_Type())
wwpLeosVplsVirtualCircuitMplsMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsMtu.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsStatus_Type=RowStatus
_WwpLeosVplsVirtualCircuitMplsStatus_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsStatus=_WwpLeosVplsVirtualCircuitMplsStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,15,1,15),_WwpLeosVplsVirtualCircuitMplsStatus_Type())
wwpLeosVplsVirtualCircuitMplsStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsStatus.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsStatsTable_Object=MibTable
wwpLeosVplsVirtualCircuitMplsStatsTable=_WwpLeosVplsVirtualCircuitMplsStatsTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,16))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsStatsTable.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsStatsEntry_Object=MibTableRow
wwpLeosVplsVirtualCircuitMplsStatsEntry=_WwpLeosVplsVirtualCircuitMplsStatsEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,16,1))
wwpLeosVplsVirtualCircuitMplsStatsEntry.setIndexNames((0,_F,_q))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsStatsEntry.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsTxBytesHi_Type=Counter32
_WwpLeosVplsVirtualCircuitMplsTxBytesHi_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsTxBytesHi=_WwpLeosVplsVirtualCircuitMplsTxBytesHi_Object((1,3,6,1,4,1,6141,2,60,28,1,1,16,1,1),_WwpLeosVplsVirtualCircuitMplsTxBytesHi_Type())
wwpLeosVplsVirtualCircuitMplsTxBytesHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsTxBytesHi.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsTxBytesLo_Type=Counter32
_WwpLeosVplsVirtualCircuitMplsTxBytesLo_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsTxBytesLo=_WwpLeosVplsVirtualCircuitMplsTxBytesLo_Object((1,3,6,1,4,1,6141,2,60,28,1,1,16,1,2),_WwpLeosVplsVirtualCircuitMplsTxBytesLo_Type())
wwpLeosVplsVirtualCircuitMplsTxBytesLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsTxBytesLo.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsRxBytesHi_Type=Counter32
_WwpLeosVplsVirtualCircuitMplsRxBytesHi_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsRxBytesHi=_WwpLeosVplsVirtualCircuitMplsRxBytesHi_Object((1,3,6,1,4,1,6141,2,60,28,1,1,16,1,3),_WwpLeosVplsVirtualCircuitMplsRxBytesHi_Type())
wwpLeosVplsVirtualCircuitMplsRxBytesHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsRxBytesHi.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsRxBytesLo_Type=Counter32
_WwpLeosVplsVirtualCircuitMplsRxBytesLo_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsRxBytesLo=_WwpLeosVplsVirtualCircuitMplsRxBytesLo_Object((1,3,6,1,4,1,6141,2,60,28,1,1,16,1,4),_WwpLeosVplsVirtualCircuitMplsRxBytesLo_Type())
wwpLeosVplsVirtualCircuitMplsRxBytesLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsRxBytesLo.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthTable_Object=MibTable
wwpLeosVplsVirtualCircuitEthTable=_WwpLeosVplsVirtualCircuitEthTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,17))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthTable.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthEntry_Object=MibTableRow
wwpLeosVplsVirtualCircuitEthEntry=_WwpLeosVplsVirtualCircuitEthEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,17,1))
wwpLeosVplsVirtualCircuitEthEntry.setIndexNames((0,_F,_r))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthEntry.setStatus(_A)
class _WwpLeosVplsVirtualCircuitEthIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualCircuitEthIndex_Type.__name__=_B
_WwpLeosVplsVirtualCircuitEthIndex_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEthIndex=_WwpLeosVplsVirtualCircuitEthIndex_Object((1,3,6,1,4,1,6141,2,60,28,1,1,17,1,1),_WwpLeosVplsVirtualCircuitEthIndex_Type())
wwpLeosVplsVirtualCircuitEthIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthIndex.setStatus(_A)
class _WwpLeosVplsVirtualCircuitEthName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosVplsVirtualCircuitEthName_Type.__name__=_L
_WwpLeosVplsVirtualCircuitEthName_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEthName=_WwpLeosVplsVirtualCircuitEthName_Object((1,3,6,1,4,1,6141,2,60,28,1,1,17,1,2),_WwpLeosVplsVirtualCircuitEthName_Type())
wwpLeosVplsVirtualCircuitEthName.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthName.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthProviderVlanId_Type=VlanId
_WwpLeosVplsVirtualCircuitEthProviderVlanId_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEthProviderVlanId=_WwpLeosVplsVirtualCircuitEthProviderVlanId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,17,1,3),_WwpLeosVplsVirtualCircuitEthProviderVlanId_Type())
wwpLeosVplsVirtualCircuitEthProviderVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthProviderVlanId.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthRowStatus_Type=RowStatus
_WwpLeosVplsVirtualCircuitEthRowStatus_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEthRowStatus=_WwpLeosVplsVirtualCircuitEthRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,17,1,4),_WwpLeosVplsVirtualCircuitEthRowStatus_Type())
wwpLeosVplsVirtualCircuitEthRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthRowStatus.setStatus(_A)
class _WwpLeosVplsVirtualCircuitEthStatsMonitor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WwpLeosVplsVirtualCircuitEthStatsMonitor_Type.__name__=_B
_WwpLeosVplsVirtualCircuitEthStatsMonitor_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEthStatsMonitor=_WwpLeosVplsVirtualCircuitEthStatsMonitor_Object((1,3,6,1,4,1,6141,2,60,28,1,1,17,1,5),_WwpLeosVplsVirtualCircuitEthStatsMonitor_Type())
wwpLeosVplsVirtualCircuitEthStatsMonitor.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthStatsMonitor.setStatus(_A)
_WwpLeosVplsVirtualCircuitEtherTypeTable_Object=MibTable
wwpLeosVplsVirtualCircuitEtherTypeTable=_WwpLeosVplsVirtualCircuitEtherTypeTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,18))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEtherTypeTable.setStatus(_A)
_WwpLeosVplsVirtualCircuitEtherTypeEntry_Object=MibTableRow
wwpLeosVplsVirtualCircuitEtherTypeEntry=_WwpLeosVplsVirtualCircuitEtherTypeEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,18,1))
wwpLeosVplsVirtualCircuitEtherTypeEntry.setIndexNames((0,_F,_AF))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEtherTypeEntry.setStatus(_A)
class _WwpLeosVplsVirtualCircuitPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualCircuitPortId_Type.__name__=_B
_WwpLeosVplsVirtualCircuitPortId_Object=MibTableColumn
wwpLeosVplsVirtualCircuitPortId=_WwpLeosVplsVirtualCircuitPortId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,18,1,1),_WwpLeosVplsVirtualCircuitPortId_Type())
wwpLeosVplsVirtualCircuitPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitPortId.setStatus(_A)
class _WwpLeosVplsVirtualCircuitEtherType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('type8100',1),('type9100',2),('type88A8',3)))
_WwpLeosVplsVirtualCircuitEtherType_Type.__name__=_B
_WwpLeosVplsVirtualCircuitEtherType_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEtherType=_WwpLeosVplsVirtualCircuitEtherType_Object((1,3,6,1,4,1,6141,2,60,28,1,1,18,1,2),_WwpLeosVplsVirtualCircuitEtherType_Type())
wwpLeosVplsVirtualCircuitEtherType.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEtherType.setStatus(_A)
class _WwpLeosVplsVirtualCircuitEtherTypePolicy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('encapOnly',2),('vlanTpid',3)))
_WwpLeosVplsVirtualCircuitEtherTypePolicy_Type.__name__=_B
_WwpLeosVplsVirtualCircuitEtherTypePolicy_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEtherTypePolicy=_WwpLeosVplsVirtualCircuitEtherTypePolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,18,1,3),_WwpLeosVplsVirtualCircuitEtherTypePolicy_Type())
wwpLeosVplsVirtualCircuitEtherTypePolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEtherTypePolicy.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthStatsTable_Object=MibTable
wwpLeosVplsVirtualCircuitEthStatsTable=_WwpLeosVplsVirtualCircuitEthStatsTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,19))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthStatsTable.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthStatsEntry_Object=MibTableRow
wwpLeosVplsVirtualCircuitEthStatsEntry=_WwpLeosVplsVirtualCircuitEthStatsEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,19,1))
wwpLeosVplsVirtualCircuitEthStatsEntry.setIndexNames((0,_F,_r))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthStatsEntry.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthTxBytesHi_Type=Counter32
_WwpLeosVplsVirtualCircuitEthTxBytesHi_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEthTxBytesHi=_WwpLeosVplsVirtualCircuitEthTxBytesHi_Object((1,3,6,1,4,1,6141,2,60,28,1,1,19,1,1),_WwpLeosVplsVirtualCircuitEthTxBytesHi_Type())
wwpLeosVplsVirtualCircuitEthTxBytesHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthTxBytesHi.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthTxBytesLo_Type=Counter32
_WwpLeosVplsVirtualCircuitEthTxBytesLo_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEthTxBytesLo=_WwpLeosVplsVirtualCircuitEthTxBytesLo_Object((1,3,6,1,4,1,6141,2,60,28,1,1,19,1,2),_WwpLeosVplsVirtualCircuitEthTxBytesLo_Type())
wwpLeosVplsVirtualCircuitEthTxBytesLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthTxBytesLo.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthRxBytesHi_Type=Counter32
_WwpLeosVplsVirtualCircuitEthRxBytesHi_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEthRxBytesHi=_WwpLeosVplsVirtualCircuitEthRxBytesHi_Object((1,3,6,1,4,1,6141,2,60,28,1,1,19,1,3),_WwpLeosVplsVirtualCircuitEthRxBytesHi_Type())
wwpLeosVplsVirtualCircuitEthRxBytesHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthRxBytesHi.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthRxBytesLo_Type=Counter32
_WwpLeosVplsVirtualCircuitEthRxBytesLo_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEthRxBytesLo=_WwpLeosVplsVirtualCircuitEthRxBytesLo_Object((1,3,6,1,4,1,6141,2,60,28,1,1,19,1,4),_WwpLeosVplsVirtualCircuitEthRxBytesLo_Type())
wwpLeosVplsVirtualCircuitEthRxBytesLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthRxBytesLo.setStatus(_A)
class _WwpLeosVirtualCircuitEthStatsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),(_T,2)))
_WwpLeosVirtualCircuitEthStatsClear_Type.__name__=_B
_WwpLeosVirtualCircuitEthStatsClear_Object=MibTableColumn
wwpLeosVirtualCircuitEthStatsClear=_WwpLeosVirtualCircuitEthStatsClear_Object((1,3,6,1,4,1,6141,2,60,28,1,1,19,1,5),_WwpLeosVirtualCircuitEthStatsClear_Type())
wwpLeosVirtualCircuitEthStatsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVirtualCircuitEthStatsClear.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsTable_Object=MibTable
wwpLeosVplsVirtualSwitchMplsTable=_WwpLeosVplsVirtualSwitchMplsTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsTable.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchMplsEntry=_WwpLeosVplsVirtualSwitchMplsEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1))
wwpLeosVplsVirtualSwitchMplsEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsEntry.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualSwitchMplsIndx_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsIndx_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsIndx=_WwpLeosVplsVirtualSwitchMplsIndx_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,1),_WwpLeosVplsVirtualSwitchMplsIndx_Type())
wwpLeosVplsVirtualSwitchMplsIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsIndx.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosVplsVirtualSwitchMplsName_Type.__name__=_L
_WwpLeosVplsVirtualSwitchMplsName_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsName=_WwpLeosVplsVirtualSwitchMplsName_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,2),_WwpLeosVplsVirtualSwitchMplsName_Type())
wwpLeosVplsVirtualSwitchMplsName.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsName.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsVpnId_Type=Unsigned32
_WwpLeosVplsVirtualSwitchMplsVpnId_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsVpnId=_WwpLeosVplsVirtualSwitchMplsVpnId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,3),_WwpLeosVplsVirtualSwitchMplsVpnId_Type())
wwpLeosVplsVirtualSwitchMplsVpnId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsVpnId.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsEncapCosPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_Q,2),(_R,3),(_S,4)))
_WwpLeosVplsVirtualSwitchMplsEncapCosPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsEncapCosPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsEncapCosPolicy=_WwpLeosVplsVirtualSwitchMplsEncapCosPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,4),_WwpLeosVplsVirtualSwitchMplsEncapCosPolicy_Type())
wwpLeosVplsVirtualSwitchMplsEncapCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsEncapCosPolicy.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri=_WwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,5),_WwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri_Type())
wwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsDecapCosPolicy_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_m,2),(_v,3),(_M,4)))
_WwpLeosVplsVirtualSwitchMplsDecapCosPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsDecapCosPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsDecapCosPolicy=_WwpLeosVplsVirtualSwitchMplsDecapCosPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,6),_WwpLeosVplsVirtualSwitchMplsDecapCosPolicy_Type())
wwpLeosVplsVirtualSwitchMplsDecapCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsDecapCosPolicy.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri=_WwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,7),_WwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri_Type())
wwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState=_WwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,8),_WwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState_Type())
wwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsDecapTTLPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pipe',1),('uniform',2)))
_WwpLeosVplsVirtualSwitchMplsDecapTTLPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsDecapTTLPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsDecapTTLPolicy=_WwpLeosVplsVirtualSwitchMplsDecapTTLPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,9),_WwpLeosVplsVirtualSwitchMplsDecapTTLPolicy_Type())
wwpLeosVplsVirtualSwitchMplsDecapTTLPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsDecapTTLPolicy.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_o,1),(_p,2)))
_WwpLeosVplsVirtualSwitchMplsType_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsType_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsType=_WwpLeosVplsVirtualSwitchMplsType_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,10),_WwpLeosVplsVirtualSwitchMplsType_Type())
wwpLeosVplsVirtualSwitchMplsType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsType.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsRowStatus_Type=RowStatus
_WwpLeosVplsVirtualSwitchMplsRowStatus_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsRowStatus=_WwpLeosVplsVirtualSwitchMplsRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,11),_WwpLeosVplsVirtualSwitchMplsRowStatus_Type())
wwpLeosVplsVirtualSwitchMplsRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsRowStatus.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsMacLrnState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosVplsVirtualSwitchMplsMacLrnState_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsMacLrnState_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsMacLrnState=_WwpLeosVplsVirtualSwitchMplsMacLrnState_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,12),_WwpLeosVplsVirtualSwitchMplsMacLrnState_Type())
wwpLeosVplsVirtualSwitchMplsMacLrnState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMacLrnState.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsTunnelMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('l2pt',1),(_AG,2)))
_WwpLeosVplsVirtualSwitchMplsTunnelMethod_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsTunnelMethod_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsTunnelMethod=_WwpLeosVplsVirtualSwitchMplsTunnelMethod_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,13),_WwpLeosVplsVirtualSwitchMplsTunnelMethod_Type())
wwpLeosVplsVirtualSwitchMplsTunnelMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsTunnelMethod.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri=_WwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,14),_WwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri_Type())
wwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_g,2)))
_WwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy=_WwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,15),_WwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy_Type())
wwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate=_WwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,16),_WwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate_Type())
wwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsHonorPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('c-vlan',1),('s-vlan',2)))
_WwpLeosVplsVirtualSwitchMplsHonorPriority_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsHonorPriority_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsHonorPriority=_WwpLeosVplsVirtualSwitchMplsHonorPriority_Object((1,3,6,1,4,1,6141,2,60,28,1,1,20,1,17),_WwpLeosVplsVirtualSwitchMplsHonorPriority_Type())
wwpLeosVplsVirtualSwitchMplsHonorPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsHonorPriority.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsMemberTable_Object=MibTable
wwpLeosVplsVirtualSwitchMplsMemberTable=_WwpLeosVplsVirtualSwitchMplsMemberTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,21))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberTable.setStatus(_G)
_WwpLeosVplsVirtualSwitchMplsMemberEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchMplsMemberEntry=_WwpLeosVplsVirtualSwitchMplsMemberEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,21,1))
wwpLeosVplsVirtualSwitchMplsMemberEntry.setIndexNames((0,_F,_O),(0,_F,_z))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberEntry.setStatus(_G)
class _WwpLeosVplsVirtualSwitchMplsMemberPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualSwitchMplsMemberPortId_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsMemberPortId_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberPortId=_WwpLeosVplsVirtualSwitchMplsMemberPortId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,21,1,1),_WwpLeosVplsVirtualSwitchMplsMemberPortId_Type())
wwpLeosVplsVirtualSwitchMplsMemberPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberPortId.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsMemberVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_WwpLeosVplsVirtualSwitchMplsMemberVlanId_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsMemberVlanId_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberVlanId=_WwpLeosVplsVirtualSwitchMplsMemberVlanId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,21,1,2),_WwpLeosVplsVirtualSwitchMplsMemberVlanId_Type())
wwpLeosVplsVirtualSwitchMplsMemberVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberVlanId.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsMemberRowStatus_Type=RowStatus
_WwpLeosVplsVirtualSwitchMplsMemberRowStatus_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberRowStatus=_WwpLeosVplsVirtualSwitchMplsMemberRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,21,1,3),_WwpLeosVplsVirtualSwitchMplsMemberRowStatus_Type())
wwpLeosVplsVirtualSwitchMplsMemberRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberRowStatus.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),(_Q,2),(_R,3),(_S,4),(_N,5),(_k,6)))
_WwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy=_WwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,21,1,4),_WwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy_Type())
wwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri=_WwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri_Object((1,3,6,1,4,1,6141,2,60,28,1,1,21,1,5),_WwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri_Type())
wwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_g,2),(_N,3)))
_WwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy=_WwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,21,1,6),_WwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy_Type())
wwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsMemberStatsTable_Object=MibTable
wwpLeosVplsVirtualSwitchMplsMemberStatsTable=_WwpLeosVplsVirtualSwitchMplsMemberStatsTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,22))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberStatsTable.setStatus(_G)
_WwpLeosVplsVirtualSwitchMplsMemberStatsEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchMplsMemberStatsEntry=_WwpLeosVplsVirtualSwitchMplsMemberStatsEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,22,1))
wwpLeosVplsVirtualSwitchMplsMemberStatsEntry.setIndexNames((0,_F,_O),(0,_F,_z))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberStatsEntry.setStatus(_G)
_WwpLeosVplsVirtualSwitchMplsMemberRxBytesHi_Type=Counter32
_WwpLeosVplsVirtualSwitchMplsMemberRxBytesHi_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberRxBytesHi=_WwpLeosVplsVirtualSwitchMplsMemberRxBytesHi_Object((1,3,6,1,4,1,6141,2,60,28,1,1,22,1,1),_WwpLeosVplsVirtualSwitchMplsMemberRxBytesHi_Type())
wwpLeosVplsVirtualSwitchMplsMemberRxBytesHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberRxBytesHi.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsMemberRxBytesLo_Type=Counter32
_WwpLeosVplsVirtualSwitchMplsMemberRxBytesLo_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberRxBytesLo=_WwpLeosVplsVirtualSwitchMplsMemberRxBytesLo_Object((1,3,6,1,4,1,6141,2,60,28,1,1,22,1,2),_WwpLeosVplsVirtualSwitchMplsMemberRxBytesLo_Type())
wwpLeosVplsVirtualSwitchMplsMemberRxBytesLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberRxBytesLo.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsMemberMeshVcTable_Object=MibTable
wwpLeosVplsVirtualSwitchMplsMemberMeshVcTable=_WwpLeosVplsVirtualSwitchMplsMemberMeshVcTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,23))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberMeshVcTable.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsMemberMeshVcEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchMplsMemberMeshVcEntry=_WwpLeosVplsVirtualSwitchMplsMemberMeshVcEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,23,1))
wwpLeosVplsVirtualSwitchMplsMemberMeshVcEntry.setIndexNames((0,_F,_O),(0,_F,_AH))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberMeshVcEntry.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc=_WwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc_Object((1,3,6,1,4,1,6141,2,60,28,1,1,23,1,1),_WwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc_Type())
wwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus_Type=RowStatus
_WwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus=_WwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,23,1,2),_WwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus_Type())
wwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsMemberAcVcTable_Object=MibTable
wwpLeosVplsVirtualSwitchMplsMemberAcVcTable=_WwpLeosVplsVirtualSwitchMplsMemberAcVcTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,24))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberAcVcTable.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsMemberAcVcEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchMplsMemberAcVcEntry=_WwpLeosVplsVirtualSwitchMplsMemberAcVcEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,24,1))
wwpLeosVplsVirtualSwitchMplsMemberAcVcEntry.setIndexNames((0,_F,_O),(0,_F,_AI))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberAcVcEntry.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc=_WwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc_Object((1,3,6,1,4,1,6141,2,60,28,1,1,24,1,1),_WwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc_Type())
wwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus_Type=RowStatus
_WwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus=_WwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,24,1,2),_WwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus_Type())
wwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus.setStatus(_A)
_WwpLeosVplsSwitchMplsCtrlProtocolTable_Object=MibTable
wwpLeosVplsSwitchMplsCtrlProtocolTable=_WwpLeosVplsSwitchMplsCtrlProtocolTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,25))
if mibBuilder.loadTexts:wwpLeosVplsSwitchMplsCtrlProtocolTable.setStatus(_A)
_WwpLeosVplsSwitchMplsCtrlProtocolEntry_Object=MibTableRow
wwpLeosVplsSwitchMplsCtrlProtocolEntry=_WwpLeosVplsSwitchMplsCtrlProtocolEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,25,1))
wwpLeosVplsSwitchMplsCtrlProtocolEntry.setIndexNames((0,_F,_O),(0,_F,_AJ))
if mibBuilder.loadTexts:wwpLeosVplsSwitchMplsCtrlProtocolEntry.setStatus(_A)
class _WwpLeosVplsSwitchMplsCtrlProtocolNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_h,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_i,7),(_j,8),(_Z,9),(_a,10),(_b,11),(_c,12),(_d,13),(_e,14),(_f,15)))
_WwpLeosVplsSwitchMplsCtrlProtocolNum_Type.__name__=_B
_WwpLeosVplsSwitchMplsCtrlProtocolNum_Object=MibTableColumn
wwpLeosVplsSwitchMplsCtrlProtocolNum=_WwpLeosVplsSwitchMplsCtrlProtocolNum_Object((1,3,6,1,4,1,6141,2,60,28,1,1,25,1,1),_WwpLeosVplsSwitchMplsCtrlProtocolNum_Type())
wwpLeosVplsSwitchMplsCtrlProtocolNum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsSwitchMplsCtrlProtocolNum.setStatus(_A)
class _WwpLeosVplsSwitchMplsCtrlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_n,1),(_w,2),(_x,3)))
_WwpLeosVplsSwitchMplsCtrlType_Type.__name__=_B
_WwpLeosVplsSwitchMplsCtrlType_Object=MibTableColumn
wwpLeosVplsSwitchMplsCtrlType=_WwpLeosVplsSwitchMplsCtrlType_Object((1,3,6,1,4,1,6141,2,60,28,1,1,25,1,2),_WwpLeosVplsSwitchMplsCtrlType_Type())
wwpLeosVplsSwitchMplsCtrlType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsSwitchMplsCtrlType.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthTable_Object=MibTable
wwpLeosVplsVirtualSwitchEthTable=_WwpLeosVplsVirtualSwitchEthTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthTable.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchEthEntry=_WwpLeosVplsVirtualSwitchEthEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1))
wwpLeosVplsVirtualSwitchEthEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEntry.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualSwitchEthIndx_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthIndx_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthIndx=_WwpLeosVplsVirtualSwitchEthIndx_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,1),_WwpLeosVplsVirtualSwitchEthIndx_Type())
wwpLeosVplsVirtualSwitchEthIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthIndx.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosVplsVirtualSwitchEthName_Type.__name__=_L
_WwpLeosVplsVirtualSwitchEthName_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthName=_WwpLeosVplsVirtualSwitchEthName_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,2),_WwpLeosVplsVirtualSwitchEthName_Type())
wwpLeosVplsVirtualSwitchEthName.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthName.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthVc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosVplsVirtualSwitchEthVc_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthVc_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthVc=_WwpLeosVplsVirtualSwitchEthVc_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,3),_WwpLeosVplsVirtualSwitchEthVc_Type())
wwpLeosVplsVirtualSwitchEthVc.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthVc.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthEncapCosPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_Q,2),(_R,3),(_S,4),(_k,5)))
_WwpLeosVplsVirtualSwitchEthEncapCosPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthEncapCosPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthEncapCosPolicy=_WwpLeosVplsVirtualSwitchEthEncapCosPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,4),_WwpLeosVplsVirtualSwitchEthEncapCosPolicy_Type())
wwpLeosVplsVirtualSwitchEthEncapCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEncapCosPolicy.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri=_WwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,5),_WwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri_Type())
wwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthDecapCosPolicy_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_m,2),(_v,3),(_M,4)))
_WwpLeosVplsVirtualSwitchEthDecapCosPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthDecapCosPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthDecapCosPolicy=_WwpLeosVplsVirtualSwitchEthDecapCosPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,6),_WwpLeosVplsVirtualSwitchEthDecapCosPolicy_Type())
wwpLeosVplsVirtualSwitchEthDecapCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthDecapCosPolicy.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri=_WwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,7),_WwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri_Type())
wwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState=_WwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,8),_WwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState_Type())
wwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthRowStatus_Type=RowStatus
_WwpLeosVplsVirtualSwitchEthRowStatus_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthRowStatus=_WwpLeosVplsVirtualSwitchEthRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,9),_WwpLeosVplsVirtualSwitchEthRowStatus_Type())
wwpLeosVplsVirtualSwitchEthRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthRowStatus.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthMacLrnState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosVplsVirtualSwitchEthMacLrnState_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthMacLrnState_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthMacLrnState=_WwpLeosVplsVirtualSwitchEthMacLrnState_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,10),_WwpLeosVplsVirtualSwitchEthMacLrnState_Type())
wwpLeosVplsVirtualSwitchEthMacLrnState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthMacLrnState.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthTunnelMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('l2pt',1),(_AG,2)))
_WwpLeosVplsVirtualSwitchEthTunnelMethod_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthTunnelMethod_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthTunnelMethod=_WwpLeosVplsVirtualSwitchEthTunnelMethod_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,11),_WwpLeosVplsVirtualSwitchEthTunnelMethod_Type())
wwpLeosVplsVirtualSwitchEthTunnelMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthTunnelMethod.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri=_WwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,12),_WwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri_Type())
wwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_g,2)))
_WwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy=_WwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,13),_WwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy_Type())
wwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate=_WwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,14),_WwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate_Type())
wwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthVcType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),(_u,2),('pbt',3)))
_WwpLeosVplsVirtualSwitchEthVcType_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthVcType_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthVcType=_WwpLeosVplsVirtualSwitchEthVcType_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,15),_WwpLeosVplsVirtualSwitchEthVcType_Type())
wwpLeosVplsVirtualSwitchEthVcType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthVcType.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthHonorPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('c-vlan',1),('s-vlan',2)))
_WwpLeosVplsVirtualSwitchEthHonorPriority_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthHonorPriority_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthHonorPriority=_WwpLeosVplsVirtualSwitchEthHonorPriority_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,16),_WwpLeosVplsVirtualSwitchEthHonorPriority_Type())
wwpLeosVplsVirtualSwitchEthHonorPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthHonorPriority.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WwpLeosVplsVirtualSwitchEthDescription_Type.__name__=_s
_WwpLeosVplsVirtualSwitchEthDescription_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthDescription=_WwpLeosVplsVirtualSwitchEthDescription_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,17),_WwpLeosVplsVirtualSwitchEthDescription_Type())
wwpLeosVplsVirtualSwitchEthDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthDescription.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthReservedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpLeosVplsVirtualSwitchEthReservedVlan_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthReservedVlan_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthReservedVlan=_WwpLeosVplsVirtualSwitchEthReservedVlan_Object((1,3,6,1,4,1,6141,2,60,28,1,1,26,1,18),_WwpLeosVplsVirtualSwitchEthReservedVlan_Type())
wwpLeosVplsVirtualSwitchEthReservedVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthReservedVlan.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthMemberTable_Object=MibTable
wwpLeosVplsVirtualSwitchEthMemberTable=_WwpLeosVplsVirtualSwitchEthMemberTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,27))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthMemberTable.setStatus(_G)
_WwpLeosVplsVirtualSwitchEthMemberEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchEthMemberEntry=_WwpLeosVplsVirtualSwitchEthMemberEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,27,1))
wwpLeosVplsVirtualSwitchEthMemberEntry.setIndexNames((0,_F,_P),(0,_F,_A0))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthMemberEntry.setStatus(_G)
class _WwpLeosVplsVirtualSwitchEthMemberPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualSwitchEthMemberPortId_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthMemberPortId_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberPortId=_WwpLeosVplsVirtualSwitchEthMemberPortId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,27,1,1),_WwpLeosVplsVirtualSwitchEthMemberPortId_Type())
wwpLeosVplsVirtualSwitchEthMemberPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthMemberPortId.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthMemberVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_WwpLeosVplsVirtualSwitchEthMemberVlan_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthMemberVlan_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberVlan=_WwpLeosVplsVirtualSwitchEthMemberVlan_Object((1,3,6,1,4,1,6141,2,60,28,1,1,27,1,2),_WwpLeosVplsVirtualSwitchEthMemberVlan_Type())
wwpLeosVplsVirtualSwitchEthMemberVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthMemberVlan.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthMemberRowStatus_Type=RowStatus
_WwpLeosVplsVirtualSwitchEthMemberRowStatus_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberRowStatus=_WwpLeosVplsVirtualSwitchEthMemberRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,27,1,3),_WwpLeosVplsVirtualSwitchEthMemberRowStatus_Type())
wwpLeosVplsVirtualSwitchEthMemberRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthMemberRowStatus.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),(_Q,2),(_R,3),(_S,4),(_N,5),(_k,6)))
_WwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy=_WwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,27,1,4),_WwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy_Type())
wwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri=_WwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri_Object((1,3,6,1,4,1,6141,2,60,28,1,1,27,1,5),_WwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri_Type())
wwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_g,2),(_N,3)))
_WwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy=_WwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,27,1,6),_WwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy_Type())
wwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthMemberStatsTable_Object=MibTable
wwpLeosVplsVirtualSwitchEthMemberStatsTable=_WwpLeosVplsVirtualSwitchEthMemberStatsTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,28))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthMemberStatsTable.setStatus(_G)
_WwpLeosVplsVirtualSwitchEthMemberStatsEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchEthMemberStatsEntry=_WwpLeosVplsVirtualSwitchEthMemberStatsEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,28,1))
wwpLeosVplsVirtualSwitchEthMemberStatsEntry.setIndexNames((0,_F,_P),(0,_F,_A0))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthMemberStatsEntry.setStatus(_G)
_WwpLeosVplsVirtualSwitchEthMemberRxBytesHi_Type=Counter32
_WwpLeosVplsVirtualSwitchEthMemberRxBytesHi_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberRxBytesHi=_WwpLeosVplsVirtualSwitchEthMemberRxBytesHi_Object((1,3,6,1,4,1,6141,2,60,28,1,1,28,1,1),_WwpLeosVplsVirtualSwitchEthMemberRxBytesHi_Type())
wwpLeosVplsVirtualSwitchEthMemberRxBytesHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthMemberRxBytesHi.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthMemberRxBytesLo_Type=Counter32
_WwpLeosVplsVirtualSwitchEthMemberRxBytesLo_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberRxBytesLo=_WwpLeosVplsVirtualSwitchEthMemberRxBytesLo_Object((1,3,6,1,4,1,6141,2,60,28,1,1,28,1,2),_WwpLeosVplsVirtualSwitchEthMemberRxBytesLo_Type())
wwpLeosVplsVirtualSwitchEthMemberRxBytesLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthMemberRxBytesLo.setStatus(_A)
_WwpLeosVplsSwitchEthCtrlProtocolTable_Object=MibTable
wwpLeosVplsSwitchEthCtrlProtocolTable=_WwpLeosVplsSwitchEthCtrlProtocolTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,29))
if mibBuilder.loadTexts:wwpLeosVplsSwitchEthCtrlProtocolTable.setStatus(_A)
_WwpLeosVplsSwitchEthCtrlProtocolEntry_Object=MibTableRow
wwpLeosVplsSwitchEthCtrlProtocolEntry=_WwpLeosVplsSwitchEthCtrlProtocolEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,29,1))
wwpLeosVplsSwitchEthCtrlProtocolEntry.setIndexNames((0,_F,_P),(0,_F,_AK))
if mibBuilder.loadTexts:wwpLeosVplsSwitchEthCtrlProtocolEntry.setStatus(_A)
class _WwpLeosVplsSwitchEthCtrlProtocolNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_h,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_i,7),(_j,8),(_Z,9),(_a,10),(_b,11),(_c,12),(_d,13),(_e,14),(_f,15)))
_WwpLeosVplsSwitchEthCtrlProtocolNum_Type.__name__=_B
_WwpLeosVplsSwitchEthCtrlProtocolNum_Object=MibTableColumn
wwpLeosVplsSwitchEthCtrlProtocolNum=_WwpLeosVplsSwitchEthCtrlProtocolNum_Object((1,3,6,1,4,1,6141,2,60,28,1,1,29,1,1),_WwpLeosVplsSwitchEthCtrlProtocolNum_Type())
wwpLeosVplsSwitchEthCtrlProtocolNum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsSwitchEthCtrlProtocolNum.setStatus(_A)
class _WwpLeosVplsSwitchEthCtrlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_n,1),(_w,2),(_x,3)))
_WwpLeosVplsSwitchEthCtrlType_Type.__name__=_B
_WwpLeosVplsSwitchEthCtrlType_Object=MibTableColumn
wwpLeosVplsSwitchEthCtrlType=_WwpLeosVplsSwitchEthCtrlType_Object((1,3,6,1,4,1,6141,2,60,28,1,1,29,1,2),_WwpLeosVplsSwitchEthCtrlType_Type())
wwpLeosVplsSwitchEthCtrlType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsSwitchEthCtrlType.setStatus(_A)
_WwpLeosVplsVirtualSwitchEtypeTranslationTable_Object=MibTable
wwpLeosVplsVirtualSwitchEtypeTranslationTable=_WwpLeosVplsVirtualSwitchEtypeTranslationTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,30))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEtypeTranslationTable.setStatus(_A)
_WwpLeosVplsVirtualSwitchEtypeTranslationEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchEtypeTranslationEntry=_WwpLeosVplsVirtualSwitchEtypeTranslationEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,30,1))
wwpLeosVplsVirtualSwitchEtypeTranslationEntry.setIndexNames((0,_F,_AL))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEtypeTranslationEntry.setStatus(_A)
_WwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype_Type=EtherType
_WwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype=_WwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype_Object((1,3,6,1,4,1,6141,2,60,28,1,1,30,1,1),_WwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype_Type())
wwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype.setStatus(_A)
_WwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype_Type=EtherType
_WwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype=_WwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype_Object((1,3,6,1,4,1,6141,2,60,28,1,1,30,1,2),_WwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype_Type())
wwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype.setStatus(_A)
_WwpLeosVplsVirtualSwitchEtypeTranslationRowStatus_Type=RowStatus
_WwpLeosVplsVirtualSwitchEtypeTranslationRowStatus_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEtypeTranslationRowStatus=_WwpLeosVplsVirtualSwitchEtypeTranslationRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,30,1,3),_WwpLeosVplsVirtualSwitchEtypeTranslationRowStatus_Type())
wwpLeosVplsVirtualSwitchEtypeTranslationRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEtypeTranslationRowStatus.setStatus(_A)
_WwpLeosVplsTunnelPairTable_Object=MibTable
wwpLeosVplsTunnelPairTable=_WwpLeosVplsTunnelPairTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,31))
if mibBuilder.loadTexts:wwpLeosVplsTunnelPairTable.setStatus(_A)
_WwpLeosVplsTunnelPairEntry_Object=MibTableRow
wwpLeosVplsTunnelPairEntry=_WwpLeosVplsTunnelPairEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,31,1))
wwpLeosVplsTunnelPairEntry.setIndexNames((0,_F,_AM))
if mibBuilder.loadTexts:wwpLeosVplsTunnelPairEntry.setStatus(_A)
class _WwpLeosVplsTunnelPairIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsTunnelPairIndx_Type.__name__=_B
_WwpLeosVplsTunnelPairIndx_Object=MibTableColumn
wwpLeosVplsTunnelPairIndx=_WwpLeosVplsTunnelPairIndx_Object((1,3,6,1,4,1,6141,2,60,28,1,1,31,1,1),_WwpLeosVplsTunnelPairIndx_Type())
wwpLeosVplsTunnelPairIndx.setMaxAccess(_AN)
if mibBuilder.loadTexts:wwpLeosVplsTunnelPairIndx.setStatus(_A)
class _WwpLeosVplsTunnelPairName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosVplsTunnelPairName_Type.__name__=_L
_WwpLeosVplsTunnelPairName_Object=MibTableColumn
wwpLeosVplsTunnelPairName=_WwpLeosVplsTunnelPairName_Object((1,3,6,1,4,1,6141,2,60,28,1,1,31,1,2),_WwpLeosVplsTunnelPairName_Type())
wwpLeosVplsTunnelPairName.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsTunnelPairName.setStatus(_A)
_WwpLeosVplsTunnelPairEncapTunnelIndx_Type=Integer32
_WwpLeosVplsTunnelPairEncapTunnelIndx_Object=MibTableColumn
wwpLeosVplsTunnelPairEncapTunnelIndx=_WwpLeosVplsTunnelPairEncapTunnelIndx_Object((1,3,6,1,4,1,6141,2,60,28,1,1,31,1,3),_WwpLeosVplsTunnelPairEncapTunnelIndx_Type())
wwpLeosVplsTunnelPairEncapTunnelIndx.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsTunnelPairEncapTunnelIndx.setStatus(_A)
_WwpLeosVplsTunnelPairDecapTunnelIndx_Type=Integer32
_WwpLeosVplsTunnelPairDecapTunnelIndx_Object=MibTableColumn
wwpLeosVplsTunnelPairDecapTunnelIndx=_WwpLeosVplsTunnelPairDecapTunnelIndx_Object((1,3,6,1,4,1,6141,2,60,28,1,1,31,1,4),_WwpLeosVplsTunnelPairDecapTunnelIndx_Type())
wwpLeosVplsTunnelPairDecapTunnelIndx.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsTunnelPairDecapTunnelIndx.setStatus(_A)
_WwpLeosVplsTunnelPairRowStatus_Type=RowStatus
_WwpLeosVplsTunnelPairRowStatus_Object=MibTableColumn
wwpLeosVplsTunnelPairRowStatus=_WwpLeosVplsTunnelPairRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,31,1,5),_WwpLeosVplsTunnelPairRowStatus_Type())
wwpLeosVplsTunnelPairRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsTunnelPairRowStatus.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsEvplMemberTable_Object=MibTable
wwpLeosVplsVirtualSwitchMplsEvplMemberTable=_WwpLeosVplsVirtualSwitchMplsEvplMemberTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,32))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsEvplMemberTable.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsEvplMemberEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchMplsEvplMemberEntry=_WwpLeosVplsVirtualSwitchMplsEvplMemberEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,32,1))
wwpLeosVplsVirtualSwitchMplsEvplMemberEntry.setIndexNames((0,_F,_O),(0,_F,_A1),(0,_F,_A2))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsEvplMemberEntry.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsEvplMemberPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualSwitchMplsEvplMemberPortId_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsEvplMemberPortId_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberPortId=_WwpLeosVplsVirtualSwitchMplsEvplMemberPortId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,32,1,1),_WwpLeosVplsVirtualSwitchMplsEvplMemberPortId_Type())
wwpLeosVplsVirtualSwitchMplsEvplMemberPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsEvplMemberPortId.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsEvplMemberVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_WwpLeosVplsVirtualSwitchMplsEvplMemberVlanId_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsEvplMemberVlanId_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberVlanId=_WwpLeosVplsVirtualSwitchMplsEvplMemberVlanId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,32,1,2),_WwpLeosVplsVirtualSwitchMplsEvplMemberVlanId_Type())
wwpLeosVplsVirtualSwitchMplsEvplMemberVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsEvplMemberVlanId.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus_Type=RowStatus
_WwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus=_WwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,32,1,3),_WwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus_Type())
wwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),(_Q,2),(_R,3),(_S,4),(_N,5),(_k,6)))
_WwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy=_WwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,32,1,4),_WwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy_Type())
wwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri=_WwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri_Object((1,3,6,1,4,1,6141,2,60,28,1,1,32,1,5),_WwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri_Type())
wwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri.setStatus(_A)
class _WwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_g,2),(_N,3)))
_WwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy=_WwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,32,1,6),_WwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy_Type())
wwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsEvplMemberStatsTable_Object=MibTable
wwpLeosVplsVirtualSwitchMplsEvplMemberStatsTable=_WwpLeosVplsVirtualSwitchMplsEvplMemberStatsTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,33))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsEvplMemberStatsTable.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsEvplMemberStatsEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchMplsEvplMemberStatsEntry=_WwpLeosVplsVirtualSwitchMplsEvplMemberStatsEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,33,1))
wwpLeosVplsVirtualSwitchMplsEvplMemberStatsEntry.setIndexNames((0,_F,_O),(0,_F,_A1),(0,_F,_A2))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsEvplMemberStatsEntry.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi_Type=Counter32
_WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi=_WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi_Object((1,3,6,1,4,1,6141,2,60,28,1,1,33,1,1),_WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi_Type())
wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi.setStatus(_A)
_WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo_Type=Counter32
_WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo_Object=MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo=_WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo_Object((1,3,6,1,4,1,6141,2,60,28,1,1,33,1,2),_WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo_Type())
wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthEvplMemberTable_Object=MibTable
wwpLeosVplsVirtualSwitchEthEvplMemberTable=_WwpLeosVplsVirtualSwitchEthEvplMemberTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,34))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEvplMemberTable.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthEvplMemberEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchEthEvplMemberEntry=_WwpLeosVplsVirtualSwitchEthEvplMemberEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,34,1))
wwpLeosVplsVirtualSwitchEthEvplMemberEntry.setIndexNames((0,_F,_P),(0,_F,_A3),(0,_F,_A4))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEvplMemberEntry.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthEvplMemberPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualSwitchEthEvplMemberPortId_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthEvplMemberPortId_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberPortId=_WwpLeosVplsVirtualSwitchEthEvplMemberPortId_Object((1,3,6,1,4,1,6141,2,60,28,1,1,34,1,1),_WwpLeosVplsVirtualSwitchEthEvplMemberPortId_Type())
wwpLeosVplsVirtualSwitchEthEvplMemberPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEvplMemberPortId.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthEvplMemberVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_WwpLeosVplsVirtualSwitchEthEvplMemberVlan_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthEvplMemberVlan_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberVlan=_WwpLeosVplsVirtualSwitchEthEvplMemberVlan_Object((1,3,6,1,4,1,6141,2,60,28,1,1,34,1,2),_WwpLeosVplsVirtualSwitchEthEvplMemberVlan_Type())
wwpLeosVplsVirtualSwitchEthEvplMemberVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEvplMemberVlan.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthEvplMemberRowStatus_Type=RowStatus
_WwpLeosVplsVirtualSwitchEthEvplMemberRowStatus_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberRowStatus=_WwpLeosVplsVirtualSwitchEthEvplMemberRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,34,1,3),_WwpLeosVplsVirtualSwitchEthEvplMemberRowStatus_Type())
wwpLeosVplsVirtualSwitchEthEvplMemberRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEvplMemberRowStatus.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),(_Q,2),(_R,3),(_S,4),(_N,5),(_k,6)))
_WwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy=_WwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,34,1,4),_WwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy_Type())
wwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri=_WwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri_Object((1,3,6,1,4,1,6141,2,60,28,1,1,34,1,5),_WwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri_Type())
wwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_g,2),(_N,3)))
_WwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy=_WwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy_Object((1,3,6,1,4,1,6141,2,60,28,1,1,34,1,6),_WwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy_Type())
wwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag=_WwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag_Object((1,3,6,1,4,1,6141,2,60,28,1,1,34,1,7),_WwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag_Type())
wwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,99)));namedValues=NamedValues(*(('tpid8100',1),('tpid9100',2),('tpid88A8',3),(_T,99)))
_WwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid=_WwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid_Object((1,3,6,1,4,1,6141,2,60,28,1,1,34,1,8),_WwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid_Type())
wwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthEvplMemberStatsTable_Object=MibTable
wwpLeosVplsVirtualSwitchEthEvplMemberStatsTable=_WwpLeosVplsVirtualSwitchEthEvplMemberStatsTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,35))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEvplMemberStatsTable.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthEvplMemberStatsEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchEthEvplMemberStatsEntry=_WwpLeosVplsVirtualSwitchEthEvplMemberStatsEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,35,1))
wwpLeosVplsVirtualSwitchEthEvplMemberStatsEntry.setIndexNames((0,_F,_P),(0,_F,_A3),(0,_F,_A4))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEvplMemberStatsEntry.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi_Type=Counter32
_WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi=_WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi_Object((1,3,6,1,4,1,6141,2,60,28,1,1,35,1,1),_WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi_Type())
wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo_Type=Counter32
_WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo=_WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo_Object((1,3,6,1,4,1,6141,2,60,28,1,1,35,1,2),_WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo_Type())
wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthTotalStatsTable_Object=MibTable
wwpLeosVplsVirtualCircuitEthTotalStatsTable=_WwpLeosVplsVirtualCircuitEthTotalStatsTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,36))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthTotalStatsTable.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthTotalStatsEntry_Object=MibTableRow
wwpLeosVplsVirtualCircuitEthTotalStatsEntry=_WwpLeosVplsVirtualCircuitEthTotalStatsEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,36,1))
wwpLeosVplsVirtualCircuitEthTotalStatsEntry.setIndexNames((0,_F,_r))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthTotalStatsEntry.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthTotalTxBytesHi_Type=Counter32
_WwpLeosVplsVirtualCircuitEthTotalTxBytesHi_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEthTotalTxBytesHi=_WwpLeosVplsVirtualCircuitEthTotalTxBytesHi_Object((1,3,6,1,4,1,6141,2,60,28,1,1,36,1,1),_WwpLeosVplsVirtualCircuitEthTotalTxBytesHi_Type())
wwpLeosVplsVirtualCircuitEthTotalTxBytesHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthTotalTxBytesHi.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthTotalTxBytesLo_Type=Counter32
_WwpLeosVplsVirtualCircuitEthTotalTxBytesLo_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEthTotalTxBytesLo=_WwpLeosVplsVirtualCircuitEthTotalTxBytesLo_Object((1,3,6,1,4,1,6141,2,60,28,1,1,36,1,2),_WwpLeosVplsVirtualCircuitEthTotalTxBytesLo_Type())
wwpLeosVplsVirtualCircuitEthTotalTxBytesLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthTotalTxBytesLo.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthTotalRxBytesHi_Type=Counter32
_WwpLeosVplsVirtualCircuitEthTotalRxBytesHi_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEthTotalRxBytesHi=_WwpLeosVplsVirtualCircuitEthTotalRxBytesHi_Object((1,3,6,1,4,1,6141,2,60,28,1,1,36,1,3),_WwpLeosVplsVirtualCircuitEthTotalRxBytesHi_Type())
wwpLeosVplsVirtualCircuitEthTotalRxBytesHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthTotalRxBytesHi.setStatus(_A)
_WwpLeosVplsVirtualCircuitEthTotalRxBytesLo_Type=Counter32
_WwpLeosVplsVirtualCircuitEthTotalRxBytesLo_Object=MibTableColumn
wwpLeosVplsVirtualCircuitEthTotalRxBytesLo=_WwpLeosVplsVirtualCircuitEthTotalRxBytesLo_Object((1,3,6,1,4,1,6141,2,60,28,1,1,36,1,4),_WwpLeosVplsVirtualCircuitEthTotalRxBytesLo_Type())
wwpLeosVplsVirtualCircuitEthTotalRxBytesLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitEthTotalRxBytesLo.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsTotalStatsTable_Object=MibTable
wwpLeosVplsVirtualCircuitMplsTotalStatsTable=_WwpLeosVplsVirtualCircuitMplsTotalStatsTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,37))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsTotalStatsTable.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsTotalStatsEntry_Object=MibTableRow
wwpLeosVplsVirtualCircuitMplsTotalStatsEntry=_WwpLeosVplsVirtualCircuitMplsTotalStatsEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,37,1))
wwpLeosVplsVirtualCircuitMplsTotalStatsEntry.setIndexNames((0,_F,_q))
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsTotalStatsEntry.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsTotalTxBytesHi_Type=Counter32
_WwpLeosVplsVirtualCircuitMplsTotalTxBytesHi_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsTotalTxBytesHi=_WwpLeosVplsVirtualCircuitMplsTotalTxBytesHi_Object((1,3,6,1,4,1,6141,2,60,28,1,1,37,1,1),_WwpLeosVplsVirtualCircuitMplsTotalTxBytesHi_Type())
wwpLeosVplsVirtualCircuitMplsTotalTxBytesHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsTotalTxBytesHi.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsTotalTxBytesLo_Type=Counter32
_WwpLeosVplsVirtualCircuitMplsTotalTxBytesLo_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsTotalTxBytesLo=_WwpLeosVplsVirtualCircuitMplsTotalTxBytesLo_Object((1,3,6,1,4,1,6141,2,60,28,1,1,37,1,2),_WwpLeosVplsVirtualCircuitMplsTotalTxBytesLo_Type())
wwpLeosVplsVirtualCircuitMplsTotalTxBytesLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsTotalTxBytesLo.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsTotalRxBytesHi_Type=Counter32
_WwpLeosVplsVirtualCircuitMplsTotalRxBytesHi_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsTotalRxBytesHi=_WwpLeosVplsVirtualCircuitMplsTotalRxBytesHi_Object((1,3,6,1,4,1,6141,2,60,28,1,1,37,1,3),_WwpLeosVplsVirtualCircuitMplsTotalRxBytesHi_Type())
wwpLeosVplsVirtualCircuitMplsTotalRxBytesHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsTotalRxBytesHi.setStatus(_A)
_WwpLeosVplsVirtualCircuitMplsTotalRxBytesLo_Type=Counter32
_WwpLeosVplsVirtualCircuitMplsTotalRxBytesLo_Object=MibTableColumn
wwpLeosVplsVirtualCircuitMplsTotalRxBytesLo=_WwpLeosVplsVirtualCircuitMplsTotalRxBytesLo_Object((1,3,6,1,4,1,6141,2,60,28,1,1,37,1,4),_WwpLeosVplsVirtualCircuitMplsTotalRxBytesLo_Type())
wwpLeosVplsVirtualCircuitMplsTotalRxBytesLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualCircuitMplsTotalRxBytesLo.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthL2CftProtocolTable_Object=MibTable
wwpLeosVplsVirtualSwitchEthL2CftProtocolTable=_WwpLeosVplsVirtualSwitchEthL2CftProtocolTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,49))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthL2CftProtocolTable.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthL2CftProtocolEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchEthL2CftProtocolEntry=_WwpLeosVplsVirtualSwitchEthL2CftProtocolEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,49,1))
wwpLeosVplsVirtualSwitchEthL2CftProtocolEntry.setIndexNames((0,_F,_P),(0,_F,_AO))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthL2CftProtocolEntry.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthL2CftProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,32,33,34,99)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),('ciscoUdld',4),(_Z,5),(_Y,6),('ciscoStpUplinkFast',7),(_f,8),(_U,9),(_b,10),(_c,11),(_d,12),(_e,13),('i8021x',14),('gmrp',15),(_a,16),('brigeBlock',32),('allBridgesBlock',33),('garpBlock',34),('unknown',99)))
_WwpLeosVplsVirtualSwitchEthL2CftProtocolType_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthL2CftProtocolType_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthL2CftProtocolType=_WwpLeosVplsVirtualSwitchEthL2CftProtocolType_Object((1,3,6,1,4,1,6141,2,60,28,1,1,49,1,1),_WwpLeosVplsVirtualSwitchEthL2CftProtocolType_Type())
wwpLeosVplsVirtualSwitchEthL2CftProtocolType.setMaxAccess(_AN)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthL2CftProtocolType.setStatus(_A)
class _WwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forward',1),(_n,2)))
_WwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition_Type.__name__=_B
_WwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition=_WwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition_Object((1,3,6,1,4,1,6141,2,60,28,1,1,49,1,2),_WwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition_Type())
wwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition.setStatus(_A)
_WwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus_Type=RowStatus
_WwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus_Object=MibTableColumn
wwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus=_WwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus_Object((1,3,6,1,4,1,6141,2,60,28,1,1,49,1,64),_WwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus_Type())
wwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtoStatsTable_Object=MibTable
wwpLeosVplsVirtualSwitchCFTProtoStatsTable=_WwpLeosVplsVirtualSwitchCFTProtoStatsTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,50))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtoStatsTable.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtoStatsEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchCFTProtoStatsEntry=_WwpLeosVplsVirtualSwitchCFTProtoStatsEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,50,1))
wwpLeosVplsVirtualSwitchCFTProtoStatsEntry.setIndexNames((0,_F,_AP),(0,_F,_AQ))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtoStatsEntry.setStatus(_A)
class _WwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx_Type.__name__=_B
_WwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx=_WwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx_Object((1,3,6,1,4,1,6141,2,60,28,1,1,50,1,1),_WwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx_Type())
wwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtol2RxPkts_Type=Counter32
_WwpLeosVplsVirtualSwitchCFTProtol2RxPkts_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2RxPkts=_WwpLeosVplsVirtualSwitchCFTProtol2RxPkts_Object((1,3,6,1,4,1,6141,2,60,28,1,1,50,1,2),_WwpLeosVplsVirtualSwitchCFTProtol2RxPkts_Type())
wwpLeosVplsVirtualSwitchCFTProtol2RxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtol2RxPkts.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts_Type=Counter32
_WwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts=_WwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts_Object((1,3,6,1,4,1,6141,2,60,28,1,1,50,1,3),_WwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts_Type())
wwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtol2PeerPkts_Type=Counter32
_WwpLeosVplsVirtualSwitchCFTProtol2PeerPkts_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2PeerPkts=_WwpLeosVplsVirtualSwitchCFTProtol2PeerPkts_Object((1,3,6,1,4,1,6141,2,60,28,1,1,50,1,4),_WwpLeosVplsVirtualSwitchCFTProtol2PeerPkts_Type())
wwpLeosVplsVirtualSwitchCFTProtol2PeerPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtol2PeerPkts.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts_Type=Counter32
_WwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts=_WwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts_Object((1,3,6,1,4,1,6141,2,60,28,1,1,50,1,5),_WwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts_Type())
wwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts_Type=Counter32
_WwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts=_WwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts_Object((1,3,6,1,4,1,6141,2,60,28,1,1,50,1,6),_WwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts_Type())
wwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures_Type=Counter32
_WwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures=_WwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures_Object((1,3,6,1,4,1,6141,2,60,28,1,1,50,1,7),_WwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures_Type())
wwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts_Type=Counter32
_WwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts=_WwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts_Object((1,3,6,1,4,1,6141,2,60,28,1,1,50,1,8),_WwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts_Type())
wwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts.setStatus(_A)
class _WwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_h,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_i,7),(_j,8),(_Z,9),(_a,10),(_b,11),(_c,12),(_e,13),(_d,14),(_f,15)))
_WwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum_Type.__name__=_B
_WwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum=_WwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum_Object((1,3,6,1,4,1,6141,2,60,28,1,1,50,1,9),_WwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum_Type())
wwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtoTotalStatsTable_Object=MibTable
wwpLeosVplsVirtualSwitchCFTProtoTotalStatsTable=_WwpLeosVplsVirtualSwitchCFTProtoTotalStatsTable_Object((1,3,6,1,4,1,6141,2,60,28,1,1,51))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtoTotalStatsTable.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntry_Object=MibTableRow
wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntry=_WwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntry_Object((1,3,6,1,4,1,6141,2,60,28,1,1,51,1))
wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntry.setIndexNames((0,_F,_AR),(0,_F,_AS))
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntry.setStatus(_A)
class _WwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx_Type.__name__=_B
_WwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx=_WwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx_Object((1,3,6,1,4,1,6141,2,60,28,1,1,51,1,1),_WwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx_Type())
wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts_Type=Counter32
_WwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts=_WwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts_Object((1,3,6,1,4,1,6141,2,60,28,1,1,51,1,2),_WwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts_Type())
wwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts_Type=Counter32
_WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts=_WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts_Object((1,3,6,1,4,1,6141,2,60,28,1,1,51,1,3),_WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts_Type())
wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts_Type=Counter32
_WwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts=_WwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts_Object((1,3,6,1,4,1,6141,2,60,28,1,1,51,1,4),_WwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts_Type())
wwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts_Type=Counter32
_WwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts=_WwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts_Object((1,3,6,1,4,1,6141,2,60,28,1,1,51,1,5),_WwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts_Type())
wwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts_Type=Counter32
_WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts=_WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts_Object((1,3,6,1,4,1,6141,2,60,28,1,1,51,1,6),_WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts_Type())
wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures_Type=Counter32
_WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures=_WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures_Object((1,3,6,1,4,1,6141,2,60,28,1,1,51,1,7),_WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures_Type())
wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures.setStatus(_A)
_WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts_Type=Counter32
_WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts=_WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts_Object((1,3,6,1,4,1,6141,2,60,28,1,1,51,1,8),_WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts_Type())
wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts.setStatus(_A)
class _WwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_h,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_i,7),(_j,8),(_Z,9),(_a,10),(_b,11),(_c,12),(_e,13),(_d,14),(_f,15)))
_WwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum_Type.__name__=_B
_WwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum_Object=MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum=_WwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum_Object((1,3,6,1,4,1,6141,2,60,28,1,1,51,1,9),_WwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum_Type())
wwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum.setStatus(_A)
_WwpLeosVplsMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosVplsMIBNotificationPrefix=_WwpLeosVplsMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,28,2))
_WwpLeosVplsMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosVplsMIBNotifications=_WwpLeosVplsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,28,2,0))
_WwpLeosVplsMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosVplsMIBConformance=_WwpLeosVplsMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,28,3))
_WwpLeosVplsMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosVplsMIBCompliances=_WwpLeosVplsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,28,3,1))
_WwpLeosVplsMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosVplsMIBGroups=_WwpLeosVplsMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,28,3,2))
mibBuilder.exportSymbols(_F,**{'VlanId':VlanId,'EtherType':EtherType,'wwpLeosVplsMIB':wwpLeosVplsMIB,'wwpLeosVplsMIBObjects':wwpLeosVplsMIBObjects,'wwpLeosVpls':wwpLeosVpls,'wwpLeosVplsVirtualCircuitTable':wwpLeosVplsVirtualCircuitTable,'wwpLeosVplsVirtualCircuitEntry':wwpLeosVplsVirtualCircuitEntry,_A5:wwpLeosVplsVirtualCircuitIndex,'wwpLeosVplsVirtualCircuitProviderVlanId':wwpLeosVplsVirtualCircuitProviderVlanId,'wwpLeosVplsVirtualCircuitType':wwpLeosVplsVirtualCircuitType,'wwpLeosVplsVirtualCircuitName':wwpLeosVplsVirtualCircuitName,'wwpLeosVplsVirtualCircuitIngressVcLabel':wwpLeosVplsVirtualCircuitIngressVcLabel,'wwpLeosVplsVirtualCircuitEgressVcLabel':wwpLeosVplsVirtualCircuitEgressVcLabel,'wwpLeosVplsVirtualCircuitTunnelIndx':wwpLeosVplsVirtualCircuitTunnelIndx,'wwpLeosVplsVirtualCircuitStatus':wwpLeosVplsVirtualCircuitStatus,'wwpLeosVplsVirtualSwitchTable':wwpLeosVplsVirtualSwitchTable,'wwpLeosVplsVirtualSwitchEntry':wwpLeosVplsVirtualSwitchEntry,_l:wwpLeosVplsVirtualSwitchIndx,'wwpLeosVplsVirtualSwitchName':wwpLeosVplsVirtualSwitchName,'wwpLeosVplsVirtualSwitchPriVc':wwpLeosVplsVirtualSwitchPriVc,'wwpLeosVplsVirtualSwitchSecVc':wwpLeosVplsVirtualSwitchSecVc,'wwpLeosVplsVirtualSwitchActiveVc':wwpLeosVplsVirtualSwitchActiveVc,'wwpLeosVplsVirtualSwitchEncapCosPolicy':wwpLeosVplsVirtualSwitchEncapCosPolicy,'wwpLeosVplsVirtualSwitchEncapFixedDot1dPri':wwpLeosVplsVirtualSwitchEncapFixedDot1dPri,'wwpLeosVplsVirtualSwitchDecapCosPolicy':wwpLeosVplsVirtualSwitchDecapCosPolicy,'wwpLeosVplsVirtualSwitchDecapFixedDot1dPri':wwpLeosVplsVirtualSwitchDecapFixedDot1dPri,'wwpLeosVplsVirtualSwitchSubscriberVlan':wwpLeosVplsVirtualSwitchSubscriberVlan,'wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState':wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState,'wwpLeosVplsVirtualSwitchType':wwpLeosVplsVirtualSwitchType,'wwpLeosVplsVirtualSwitchStatus':wwpLeosVplsVirtualSwitchStatus,'wwpLeosVplsVirtualSwitchMemberTable':wwpLeosVplsVirtualSwitchMemberTable,'wwpLeosVplsVirtualSwitchMemberEntry':wwpLeosVplsVirtualSwitchMemberEntry,_A6:wwpLeosVplsVirtualSwitchMemberPortId,'wwpLeosVplsVirtualSwitchMemberStatus':wwpLeosVplsVirtualSwitchMemberStatus,'wwpLeosVplsSwitchCtrlProtocolTable':wwpLeosVplsSwitchCtrlProtocolTable,'wwpLeosVplsSwitchCtrlProtocolEntry':wwpLeosVplsSwitchCtrlProtocolEntry,_A7:wwpLeosVplsSwitchCtrlProtocolNum,'wwpLeosVplsSwitchCtrlType':wwpLeosVplsSwitchCtrlType,'wwpLeosVplsSwitchReservedVlanTable':wwpLeosVplsSwitchReservedVlanTable,'wwpLeosVplsSwitchReservedVlanEntry':wwpLeosVplsSwitchReservedVlanEntry,_A8:wwpLeosVplsSwitchReservedVlanId,'wwpLeosVplsSwitchReservedVlanStatus':wwpLeosVplsSwitchReservedVlanStatus,'wwpLeosVplsGlobalAttrs':wwpLeosVplsGlobalAttrs,'wwpLeosVplsTunnelFixedTTL':wwpLeosVplsTunnelFixedTTL,'wwpLeosVplsResolverTimeout':wwpLeosVplsResolverTimeout,'wwpLeosVplsStaticLabelRangeStart':wwpLeosVplsStaticLabelRangeStart,'wwpLeosVplsStaticLabelRangeEnd':wwpLeosVplsStaticLabelRangeEnd,'wwpLeosVplsDynamicLabelRangeStart':wwpLeosVplsDynamicLabelRangeStart,'wwpLeosVplsDynamicLabelRangeEnd':wwpLeosVplsDynamicLabelRangeEnd,'wwpLeosVplsVirtualCircuitStatsClear':wwpLeosVplsVirtualCircuitStatsClear,'wwpLeosVplsMplsPathTable':wwpLeosVplsMplsPathTable,'wwpLeosVplsMplsPathEntry':wwpLeosVplsMplsPathEntry,_y:wwpLeosVplsMplsPathIndex,'wwpLeosVplsMplsPathName':wwpLeosVplsMplsPathName,'wwpLeosVplsMplsPathRowStatus':wwpLeosVplsMplsPathRowStatus,'wwpLeosVplsMplsPathMemberTable':wwpLeosVplsMplsPathMemberTable,'wwpLeosVplsMplsPathMemberEntry':wwpLeosVplsMplsPathMemberEntry,_A9:wwpLeosVplsMplsPathOptionIndex,_AA:wwpLeosVplsMplsPathMemberIpIndex,'wwpLeosVplsMplsPathMemberIp':wwpLeosVplsMplsPathMemberIp,'wwpLeosVplsMplsPathMemberRowStatus':wwpLeosVplsMplsPathMemberRowStatus,'wwpLeosVplsRsvpAttrTable':wwpLeosVplsRsvpAttrTable,'wwpLeosVplsRsvpAttrEntry':wwpLeosVplsRsvpAttrEntry,_AB:wwpLeosVplsRsvpAttrIndex,'wwpLeosVplsRsvpAttrHoldPri':wwpLeosVplsRsvpAttrHoldPri,'wwpLeosVplsRsvpAttrSetupPri':wwpLeosVplsRsvpAttrSetupPri,'wwpLeosVplsRsvpAttrRecordRoute':wwpLeosVplsRsvpAttrRecordRoute,'wwpLeosVplsEncapTunnelTable':wwpLeosVplsEncapTunnelTable,'wwpLeosVplsEncapTunnelEntry':wwpLeosVplsEncapTunnelEntry,_AC:wwpLeosVplsEncapTunnelId,'wwpLeosVplsEncapTunnelName':wwpLeosVplsEncapTunnelName,'wwpLeosVplsEncapTunnelType':wwpLeosVplsEncapTunnelType,'wwpLeosVplsEncapTunnelDestAddr':wwpLeosVplsEncapTunnelDestAddr,'wwpLeosVplsEncapTunnelPathIndex':wwpLeosVplsEncapTunnelPathIndex,'wwpLeosVplsEncapTunnelEncapCosPolicy':wwpLeosVplsEncapTunnelEncapCosPolicy,'wwpLeosVplsEncapTunnelEncapFixedExp':wwpLeosVplsEncapTunnelEncapFixedExp,'wwpLeosVplsEncapTunnelTTLPolicy':wwpLeosVplsEncapTunnelTTLPolicy,'wwpLeosVplsEncapTunnelEncapLabel':wwpLeosVplsEncapTunnelEncapLabel,'wwpLeosVplsEncapTunnelProtType':wwpLeosVplsEncapTunnelProtType,'wwpLeosVplsEncapTunnelDestResolvedMac':wwpLeosVplsEncapTunnelDestResolvedMac,'wwpLeosVplsEncapTunnelOperStatus':wwpLeosVplsEncapTunnelOperStatus,'wwpLeosVplsEncapTunnelAdminStatus':wwpLeosVplsEncapTunnelAdminStatus,'wwpLeosVplsEncapTunnelDestResolvedPort':wwpLeosVplsEncapTunnelDestResolvedPort,'wwpLeosVplsEncapTunnelDestResolvedVlan':wwpLeosVplsEncapTunnelDestResolvedVlan,'wwpLeosVplsEncapTunnelRowStatus':wwpLeosVplsEncapTunnelRowStatus,'wwpLeosVplsEncapTunnelFastReroute':wwpLeosVplsEncapTunnelFastReroute,'wwpLeosVplsEncapTunnelLspType':wwpLeosVplsEncapTunnelLspType,'wwpLeosVplsEncapTunnelPartnerTunnelId':wwpLeosVplsEncapTunnelPartnerTunnelId,'wwpLeosVplsEncapTunnelBVID':wwpLeosVplsEncapTunnelBVID,'wwpLeosVplsEncapTunnelDestBridgeIndex':wwpLeosVplsEncapTunnelDestBridgeIndex,'wwpLeosVplsEncapTunnelEgressPort':wwpLeosVplsEncapTunnelEgressPort,'wwpLeosVplsEncapTunnelEncapFixedPCP':wwpLeosVplsEncapTunnelEncapFixedPCP,'wwpLeosVplsEncapTunnelActive':wwpLeosVplsEncapTunnelActive,'wwpLeosVplsDecapTunnelTable':wwpLeosVplsDecapTunnelTable,'wwpLeosVplsDecapTunnelEntry':wwpLeosVplsDecapTunnelEntry,_AE:wwpLeosVplsDecapTunnelId,'wwpLeosVplsDecapTunnelName':wwpLeosVplsDecapTunnelName,'wwpLeosVplsDecapTunnelLabel':wwpLeosVplsDecapTunnelLabel,'wwpLeosVplsDecapTunnelType':wwpLeosVplsDecapTunnelType,'wwpLeosVplsDecapTunnelRowStatus':wwpLeosVplsDecapTunnelRowStatus,'wwpLeosVplsDecapTunnelBVID':wwpLeosVplsDecapTunnelBVID,'wwpLeosVplsDecapTunnelBridgeIndex':wwpLeosVplsDecapTunnelBridgeIndex,'wwpLeosVplsDecapTunnelPort':wwpLeosVplsDecapTunnelPort,'wwpLeosVplsDecapTunnelMac':wwpLeosVplsDecapTunnelMac,'wwpLeosVplsDecapTunnelOperStatus':wwpLeosVplsDecapTunnelOperStatus,'wwpLeosVplsVirtualCircuitMplsTable':wwpLeosVplsVirtualCircuitMplsTable,'wwpLeosVplsVirtualCircuitMplsEntry':wwpLeosVplsVirtualCircuitMplsEntry,_q:wwpLeosVplsVirtualCircuitMplsIndex,'wwpLeosVplsVirtualCircuitMplsName':wwpLeosVplsVirtualCircuitMplsName,'wwpLeosVplsVirtualCircuitMplsType':wwpLeosVplsVirtualCircuitMplsType,'wwpLeosVplsVirtualCircuitMplsDestAddr':wwpLeosVplsVirtualCircuitMplsDestAddr,'wwpLeosVplsVirtualCircuitMplsTunnelPolicy':wwpLeosVplsVirtualCircuitMplsTunnelPolicy,'wwpLeosVplsVirtualCircuitMplsFixedTunnelId':wwpLeosVplsVirtualCircuitMplsFixedTunnelId,'wwpLeosVplsVirtualCircuitMplsActiveTunnelId':wwpLeosVplsVirtualCircuitMplsActiveTunnelId,'wwpLeosVplsVirtualCircuitMplsOperStatus':wwpLeosVplsVirtualCircuitMplsOperStatus,'wwpLeosVplsVirtualCircuitMplsEncapLabel':wwpLeosVplsVirtualCircuitMplsEncapLabel,'wwpLeosVplsVirtualCircuitMplsDecapLabel':wwpLeosVplsVirtualCircuitMplsDecapLabel,'wwpLeosVplsVirtualCircuitMplsGroupId':wwpLeosVplsVirtualCircuitMplsGroupId,'wwpLeosVplsVirtualCircuitMplsProtectionType':wwpLeosVplsVirtualCircuitMplsProtectionType,'wwpLeosVplsVirtualCircuitMplsStatusTlv':wwpLeosVplsVirtualCircuitMplsStatusTlv,'wwpLeosVplsVirtualCircuitMplsMtu':wwpLeosVplsVirtualCircuitMplsMtu,'wwpLeosVplsVirtualCircuitMplsStatus':wwpLeosVplsVirtualCircuitMplsStatus,'wwpLeosVplsVirtualCircuitMplsStatsTable':wwpLeosVplsVirtualCircuitMplsStatsTable,'wwpLeosVplsVirtualCircuitMplsStatsEntry':wwpLeosVplsVirtualCircuitMplsStatsEntry,'wwpLeosVplsVirtualCircuitMplsTxBytesHi':wwpLeosVplsVirtualCircuitMplsTxBytesHi,'wwpLeosVplsVirtualCircuitMplsTxBytesLo':wwpLeosVplsVirtualCircuitMplsTxBytesLo,'wwpLeosVplsVirtualCircuitMplsRxBytesHi':wwpLeosVplsVirtualCircuitMplsRxBytesHi,'wwpLeosVplsVirtualCircuitMplsRxBytesLo':wwpLeosVplsVirtualCircuitMplsRxBytesLo,'wwpLeosVplsVirtualCircuitEthTable':wwpLeosVplsVirtualCircuitEthTable,'wwpLeosVplsVirtualCircuitEthEntry':wwpLeosVplsVirtualCircuitEthEntry,_r:wwpLeosVplsVirtualCircuitEthIndex,'wwpLeosVplsVirtualCircuitEthName':wwpLeosVplsVirtualCircuitEthName,'wwpLeosVplsVirtualCircuitEthProviderVlanId':wwpLeosVplsVirtualCircuitEthProviderVlanId,'wwpLeosVplsVirtualCircuitEthRowStatus':wwpLeosVplsVirtualCircuitEthRowStatus,'wwpLeosVplsVirtualCircuitEthStatsMonitor':wwpLeosVplsVirtualCircuitEthStatsMonitor,'wwpLeosVplsVirtualCircuitEtherTypeTable':wwpLeosVplsVirtualCircuitEtherTypeTable,'wwpLeosVplsVirtualCircuitEtherTypeEntry':wwpLeosVplsVirtualCircuitEtherTypeEntry,_AF:wwpLeosVplsVirtualCircuitPortId,'wwpLeosVplsVirtualCircuitEtherType':wwpLeosVplsVirtualCircuitEtherType,'wwpLeosVplsVirtualCircuitEtherTypePolicy':wwpLeosVplsVirtualCircuitEtherTypePolicy,'wwpLeosVplsVirtualCircuitEthStatsTable':wwpLeosVplsVirtualCircuitEthStatsTable,'wwpLeosVplsVirtualCircuitEthStatsEntry':wwpLeosVplsVirtualCircuitEthStatsEntry,'wwpLeosVplsVirtualCircuitEthTxBytesHi':wwpLeosVplsVirtualCircuitEthTxBytesHi,'wwpLeosVplsVirtualCircuitEthTxBytesLo':wwpLeosVplsVirtualCircuitEthTxBytesLo,'wwpLeosVplsVirtualCircuitEthRxBytesHi':wwpLeosVplsVirtualCircuitEthRxBytesHi,'wwpLeosVplsVirtualCircuitEthRxBytesLo':wwpLeosVplsVirtualCircuitEthRxBytesLo,'wwpLeosVirtualCircuitEthStatsClear':wwpLeosVirtualCircuitEthStatsClear,'wwpLeosVplsVirtualSwitchMplsTable':wwpLeosVplsVirtualSwitchMplsTable,'wwpLeosVplsVirtualSwitchMplsEntry':wwpLeosVplsVirtualSwitchMplsEntry,_O:wwpLeosVplsVirtualSwitchMplsIndx,'wwpLeosVplsVirtualSwitchMplsName':wwpLeosVplsVirtualSwitchMplsName,'wwpLeosVplsVirtualSwitchMplsVpnId':wwpLeosVplsVirtualSwitchMplsVpnId,'wwpLeosVplsVirtualSwitchMplsEncapCosPolicy':wwpLeosVplsVirtualSwitchMplsEncapCosPolicy,'wwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri':wwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri,'wwpLeosVplsVirtualSwitchMplsDecapCosPolicy':wwpLeosVplsVirtualSwitchMplsDecapCosPolicy,'wwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri':wwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri,'wwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState':wwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState,'wwpLeosVplsVirtualSwitchMplsDecapTTLPolicy':wwpLeosVplsVirtualSwitchMplsDecapTTLPolicy,'wwpLeosVplsVirtualSwitchMplsType':wwpLeosVplsVirtualSwitchMplsType,'wwpLeosVplsVirtualSwitchMplsRowStatus':wwpLeosVplsVirtualSwitchMplsRowStatus,'wwpLeosVplsVirtualSwitchMplsMacLrnState':wwpLeosVplsVirtualSwitchMplsMacLrnState,'wwpLeosVplsVirtualSwitchMplsTunnelMethod':wwpLeosVplsVirtualSwitchMplsTunnelMethod,'wwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri':wwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri,'wwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy':wwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy,'wwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate':wwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate,'wwpLeosVplsVirtualSwitchMplsHonorPriority':wwpLeosVplsVirtualSwitchMplsHonorPriority,'wwpLeosVplsVirtualSwitchMplsMemberTable':wwpLeosVplsVirtualSwitchMplsMemberTable,'wwpLeosVplsVirtualSwitchMplsMemberEntry':wwpLeosVplsVirtualSwitchMplsMemberEntry,_z:wwpLeosVplsVirtualSwitchMplsMemberPortId,'wwpLeosVplsVirtualSwitchMplsMemberVlanId':wwpLeosVplsVirtualSwitchMplsMemberVlanId,'wwpLeosVplsVirtualSwitchMplsMemberRowStatus':wwpLeosVplsVirtualSwitchMplsMemberRowStatus,'wwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy':wwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy,'wwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri':wwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri,'wwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy':wwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy,'wwpLeosVplsVirtualSwitchMplsMemberStatsTable':wwpLeosVplsVirtualSwitchMplsMemberStatsTable,'wwpLeosVplsVirtualSwitchMplsMemberStatsEntry':wwpLeosVplsVirtualSwitchMplsMemberStatsEntry,'wwpLeosVplsVirtualSwitchMplsMemberRxBytesHi':wwpLeosVplsVirtualSwitchMplsMemberRxBytesHi,'wwpLeosVplsVirtualSwitchMplsMemberRxBytesLo':wwpLeosVplsVirtualSwitchMplsMemberRxBytesLo,'wwpLeosVplsVirtualSwitchMplsMemberMeshVcTable':wwpLeosVplsVirtualSwitchMplsMemberMeshVcTable,'wwpLeosVplsVirtualSwitchMplsMemberMeshVcEntry':wwpLeosVplsVirtualSwitchMplsMemberMeshVcEntry,_AH:wwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc,'wwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus':wwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus,'wwpLeosVplsVirtualSwitchMplsMemberAcVcTable':wwpLeosVplsVirtualSwitchMplsMemberAcVcTable,'wwpLeosVplsVirtualSwitchMplsMemberAcVcEntry':wwpLeosVplsVirtualSwitchMplsMemberAcVcEntry,_AI:wwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc,'wwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus':wwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus,'wwpLeosVplsSwitchMplsCtrlProtocolTable':wwpLeosVplsSwitchMplsCtrlProtocolTable,'wwpLeosVplsSwitchMplsCtrlProtocolEntry':wwpLeosVplsSwitchMplsCtrlProtocolEntry,_AJ:wwpLeosVplsSwitchMplsCtrlProtocolNum,'wwpLeosVplsSwitchMplsCtrlType':wwpLeosVplsSwitchMplsCtrlType,'wwpLeosVplsVirtualSwitchEthTable':wwpLeosVplsVirtualSwitchEthTable,'wwpLeosVplsVirtualSwitchEthEntry':wwpLeosVplsVirtualSwitchEthEntry,_P:wwpLeosVplsVirtualSwitchEthIndx,'wwpLeosVplsVirtualSwitchEthName':wwpLeosVplsVirtualSwitchEthName,'wwpLeosVplsVirtualSwitchEthVc':wwpLeosVplsVirtualSwitchEthVc,'wwpLeosVplsVirtualSwitchEthEncapCosPolicy':wwpLeosVplsVirtualSwitchEthEncapCosPolicy,'wwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri':wwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri,'wwpLeosVplsVirtualSwitchEthDecapCosPolicy':wwpLeosVplsVirtualSwitchEthDecapCosPolicy,'wwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri':wwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri,'wwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState':wwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState,'wwpLeosVplsVirtualSwitchEthRowStatus':wwpLeosVplsVirtualSwitchEthRowStatus,'wwpLeosVplsVirtualSwitchEthMacLrnState':wwpLeosVplsVirtualSwitchEthMacLrnState,'wwpLeosVplsVirtualSwitchEthTunnelMethod':wwpLeosVplsVirtualSwitchEthTunnelMethod,'wwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri':wwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri,'wwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy':wwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy,'wwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate':wwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate,'wwpLeosVplsVirtualSwitchEthVcType':wwpLeosVplsVirtualSwitchEthVcType,'wwpLeosVplsVirtualSwitchEthHonorPriority':wwpLeosVplsVirtualSwitchEthHonorPriority,'wwpLeosVplsVirtualSwitchEthDescription':wwpLeosVplsVirtualSwitchEthDescription,'wwpLeosVplsVirtualSwitchEthReservedVlan':wwpLeosVplsVirtualSwitchEthReservedVlan,'wwpLeosVplsVirtualSwitchEthMemberTable':wwpLeosVplsVirtualSwitchEthMemberTable,'wwpLeosVplsVirtualSwitchEthMemberEntry':wwpLeosVplsVirtualSwitchEthMemberEntry,_A0:wwpLeosVplsVirtualSwitchEthMemberPortId,'wwpLeosVplsVirtualSwitchEthMemberVlan':wwpLeosVplsVirtualSwitchEthMemberVlan,'wwpLeosVplsVirtualSwitchEthMemberRowStatus':wwpLeosVplsVirtualSwitchEthMemberRowStatus,'wwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy':wwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy,'wwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri':wwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri,'wwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy':wwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy,'wwpLeosVplsVirtualSwitchEthMemberStatsTable':wwpLeosVplsVirtualSwitchEthMemberStatsTable,'wwpLeosVplsVirtualSwitchEthMemberStatsEntry':wwpLeosVplsVirtualSwitchEthMemberStatsEntry,'wwpLeosVplsVirtualSwitchEthMemberRxBytesHi':wwpLeosVplsVirtualSwitchEthMemberRxBytesHi,'wwpLeosVplsVirtualSwitchEthMemberRxBytesLo':wwpLeosVplsVirtualSwitchEthMemberRxBytesLo,'wwpLeosVplsSwitchEthCtrlProtocolTable':wwpLeosVplsSwitchEthCtrlProtocolTable,'wwpLeosVplsSwitchEthCtrlProtocolEntry':wwpLeosVplsSwitchEthCtrlProtocolEntry,_AK:wwpLeosVplsSwitchEthCtrlProtocolNum,'wwpLeosVplsSwitchEthCtrlType':wwpLeosVplsSwitchEthCtrlType,'wwpLeosVplsVirtualSwitchEtypeTranslationTable':wwpLeosVplsVirtualSwitchEtypeTranslationTable,'wwpLeosVplsVirtualSwitchEtypeTranslationEntry':wwpLeosVplsVirtualSwitchEtypeTranslationEntry,_AL:wwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype,'wwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype':wwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype,'wwpLeosVplsVirtualSwitchEtypeTranslationRowStatus':wwpLeosVplsVirtualSwitchEtypeTranslationRowStatus,'wwpLeosVplsTunnelPairTable':wwpLeosVplsTunnelPairTable,'wwpLeosVplsTunnelPairEntry':wwpLeosVplsTunnelPairEntry,_AM:wwpLeosVplsTunnelPairIndx,'wwpLeosVplsTunnelPairName':wwpLeosVplsTunnelPairName,'wwpLeosVplsTunnelPairEncapTunnelIndx':wwpLeosVplsTunnelPairEncapTunnelIndx,'wwpLeosVplsTunnelPairDecapTunnelIndx':wwpLeosVplsTunnelPairDecapTunnelIndx,'wwpLeosVplsTunnelPairRowStatus':wwpLeosVplsTunnelPairRowStatus,'wwpLeosVplsVirtualSwitchMplsEvplMemberTable':wwpLeosVplsVirtualSwitchMplsEvplMemberTable,'wwpLeosVplsVirtualSwitchMplsEvplMemberEntry':wwpLeosVplsVirtualSwitchMplsEvplMemberEntry,_A1:wwpLeosVplsVirtualSwitchMplsEvplMemberPortId,_A2:wwpLeosVplsVirtualSwitchMplsEvplMemberVlanId,'wwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus':wwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus,'wwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy':wwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy,'wwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri':wwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri,'wwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy':wwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy,'wwpLeosVplsVirtualSwitchMplsEvplMemberStatsTable':wwpLeosVplsVirtualSwitchMplsEvplMemberStatsTable,'wwpLeosVplsVirtualSwitchMplsEvplMemberStatsEntry':wwpLeosVplsVirtualSwitchMplsEvplMemberStatsEntry,'wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi':wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi,'wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo':wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo,'wwpLeosVplsVirtualSwitchEthEvplMemberTable':wwpLeosVplsVirtualSwitchEthEvplMemberTable,'wwpLeosVplsVirtualSwitchEthEvplMemberEntry':wwpLeosVplsVirtualSwitchEthEvplMemberEntry,_A3:wwpLeosVplsVirtualSwitchEthEvplMemberPortId,_A4:wwpLeosVplsVirtualSwitchEthEvplMemberVlan,'wwpLeosVplsVirtualSwitchEthEvplMemberRowStatus':wwpLeosVplsVirtualSwitchEthEvplMemberRowStatus,'wwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy':wwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy,'wwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri':wwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri,'wwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy':wwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy,'wwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag':wwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag,'wwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid':wwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid,'wwpLeosVplsVirtualSwitchEthEvplMemberStatsTable':wwpLeosVplsVirtualSwitchEthEvplMemberStatsTable,'wwpLeosVplsVirtualSwitchEthEvplMemberStatsEntry':wwpLeosVplsVirtualSwitchEthEvplMemberStatsEntry,'wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi':wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi,'wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo':wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo,'wwpLeosVplsVirtualCircuitEthTotalStatsTable':wwpLeosVplsVirtualCircuitEthTotalStatsTable,'wwpLeosVplsVirtualCircuitEthTotalStatsEntry':wwpLeosVplsVirtualCircuitEthTotalStatsEntry,'wwpLeosVplsVirtualCircuitEthTotalTxBytesHi':wwpLeosVplsVirtualCircuitEthTotalTxBytesHi,'wwpLeosVplsVirtualCircuitEthTotalTxBytesLo':wwpLeosVplsVirtualCircuitEthTotalTxBytesLo,'wwpLeosVplsVirtualCircuitEthTotalRxBytesHi':wwpLeosVplsVirtualCircuitEthTotalRxBytesHi,'wwpLeosVplsVirtualCircuitEthTotalRxBytesLo':wwpLeosVplsVirtualCircuitEthTotalRxBytesLo,'wwpLeosVplsVirtualCircuitMplsTotalStatsTable':wwpLeosVplsVirtualCircuitMplsTotalStatsTable,'wwpLeosVplsVirtualCircuitMplsTotalStatsEntry':wwpLeosVplsVirtualCircuitMplsTotalStatsEntry,'wwpLeosVplsVirtualCircuitMplsTotalTxBytesHi':wwpLeosVplsVirtualCircuitMplsTotalTxBytesHi,'wwpLeosVplsVirtualCircuitMplsTotalTxBytesLo':wwpLeosVplsVirtualCircuitMplsTotalTxBytesLo,'wwpLeosVplsVirtualCircuitMplsTotalRxBytesHi':wwpLeosVplsVirtualCircuitMplsTotalRxBytesHi,'wwpLeosVplsVirtualCircuitMplsTotalRxBytesLo':wwpLeosVplsVirtualCircuitMplsTotalRxBytesLo,'wwpLeosVplsVirtualSwitchEthL2CftProtocolTable':wwpLeosVplsVirtualSwitchEthL2CftProtocolTable,'wwpLeosVplsVirtualSwitchEthL2CftProtocolEntry':wwpLeosVplsVirtualSwitchEthL2CftProtocolEntry,_AO:wwpLeosVplsVirtualSwitchEthL2CftProtocolType,'wwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition':wwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition,'wwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus':wwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus,'wwpLeosVplsVirtualSwitchCFTProtoStatsTable':wwpLeosVplsVirtualSwitchCFTProtoStatsTable,'wwpLeosVplsVirtualSwitchCFTProtoStatsEntry':wwpLeosVplsVirtualSwitchCFTProtoStatsEntry,_AP:wwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx,'wwpLeosVplsVirtualSwitchCFTProtol2RxPkts':wwpLeosVplsVirtualSwitchCFTProtol2RxPkts,'wwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts':wwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts,'wwpLeosVplsVirtualSwitchCFTProtol2PeerPkts':wwpLeosVplsVirtualSwitchCFTProtol2PeerPkts,'wwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts':wwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts,'wwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts':wwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts,'wwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures':wwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures,'wwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts':wwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts,_AQ:wwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum,'wwpLeosVplsVirtualSwitchCFTProtoTotalStatsTable':wwpLeosVplsVirtualSwitchCFTProtoTotalStatsTable,'wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntry':wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntry,_AR:wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx,'wwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts':wwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts,'wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts':wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts,'wwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts':wwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts,'wwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts':wwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts,'wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts':wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts,'wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures':wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures,'wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts':wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts,_AS:wwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum,'wwpLeosVplsMIBNotificationPrefix':wwpLeosVplsMIBNotificationPrefix,'wwpLeosVplsMIBNotifications':wwpLeosVplsMIBNotifications,'wwpLeosVplsMIBConformance':wwpLeosVplsMIBConformance,'wwpLeosVplsMIBCompliances':wwpLeosVplsMIBCompliances,'wwpLeosVplsMIBGroups':wwpLeosVplsMIBGroups})