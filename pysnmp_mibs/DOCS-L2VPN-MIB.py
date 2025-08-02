_A7='docsL2vpnMultipointGroup'
_A6='docsL2vpnPointToPointGroup'
_A5='docsL2vpnBaseGroup'
_A4='docsL2vpnDot1qTpGroupExtReceivePkts'
_A3='docsL2vpnDot1qTpGroupExtTransmitPkts'
_A2='docsL2vpnDot1qTpFdbExtReceivePkts'
_A1='docsL2vpnDot1qTpFdbExtTransmitPkts'
_A0='docsL2vpnCmNsiTAII'
_z='docsL2vpnCmNsiSAII'
_y='docsL2vpnCmNsiAGI'
_x='docsL2vpnCmNsiEncapValue'
_w='docsL2vpnCmNsiEncapSubtype'
_v='docsL2vpnPktClassVendorSpecific'
_u='docsL2vpnPktClassCMIM'
_t='docsL2vpnPktClassUserPriRangeHigh'
_s='docsL2vpnPktClassUserPriRangeLow'
_r='docsL2vpnPktClassL2vpnId'
_q='docsL2vpnSfStatusVendorSpecific'
_p='docsL2vpnSfStatusIngressUserPriority'
_o='docsL2vpnSfStatusL2vpnId'
_n='docsL2vpnPortStatusGroupSAId'
_m='docsL2vpnVpnCmStatsDownstreamDiscards'
_l='docsL2vpnVpnCmStatsDownstreamBytes'
_k='docsL2vpnVpnCmStatsDownstreamPkts'
_j='docsL2vpnVpnCmStatsUpstreamDiscards'
_i='docsL2vpnVpnCmStatsUpstreamBytes'
_h='docsL2vpnVpnCmStatsUpstreamPkts'
_g='docsL2vpnVpnCmIndividualSAId'
_f='docsL2vpnVpnCmVendorSpecific'
_e='docsL2vpnVpnCmCMIM'
_d='docsL2vpnCmDhcpSnooping'
_c='docsL2vpnCmDutCMIM'
_b='docsL2vpnCmDutFilteringCapability'
_a='docsL2vpnCmCompliantCapability'
_Z='docsL2vpnIndexToIdId'
_Y='docsL2vpnIdToIndexIdx'
_X='not-accessible'
_W='docsL2vpnId'
_V='dot1qVlanIndex'
_U='dot1qTpGroupAddress'
_T='dot1qTpFdbAddress'
_S='dot1qFdbId'
_R='docsQosPktClassId'
_Q='dot1dBasePort'
_P='BRIDGE-MIB'
_O='docsL2vpnVpnCmCpeMacAddress'
_N='docsL2vpnCmVpnCpeMacAddress'
_M='Integer32'
_L='ifIndex'
_K='IF-MIB'
_J='docsQosServiceFlowId'
_I='Unsigned32'
_H='DOCS-QOS-MIB'
_G='Q-BRIDGE-MIB'
_F='docsIfCmtsCmStatusIndex'
_E='DOCS-IF-MIB'
_D='docsL2vpnIdx'
_C='read-only'
_B='DOCS-L2VPN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_P,_Q)
clabProjDocsis,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabProjDocsis')
docsIfCmtsCmStatusIndex,=mibBuilder.importSymbols(_E,_F)
docsQosPktClassId,docsQosServiceFlowId=mibBuilder.importSymbols(_H,_R,_J)
ifIndex,=mibBuilder.importSymbols(_K,_L)
dot1qFdbId,dot1qTpFdbAddress,dot1qTpGroupAddress,dot1qVlanIndex=mibBuilder.importSymbols(_G,_S,_T,_U,_V)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
docsL2vpnMIB=ModuleIdentity((1,3,6,1,4,1,4491,2,1,8))
if mibBuilder.loadTexts:docsL2vpnMIB.setRevisions(('2006-03-28 00:00',))
class DocsL2vpnIdentifier(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
class DocsL2vpnIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class DocsNsiEncapSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('ieee8021q',2),('ieee8021ad',3),('mpls',4),('l2tpv3',5)))
class DocsNsiEncapValue(TextualConvention,OctetString):status=_A
class DocsL2vpnIfList(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('eCm',0),('cmci',1),('docsCableMacLayer',2),('docsCableDownstream',3),('docsCableUpstream',4),('eMta',16),('eStbIp',17),('eStbDsg',18)))
_DocsL2vpnMIBNotifications_ObjectIdentity=ObjectIdentity
docsL2vpnMIBNotifications=_DocsL2vpnMIBNotifications_ObjectIdentity((1,3,6,1,4,1,4491,2,1,8,0))
_DocsL2vpnMIBObjects_ObjectIdentity=ObjectIdentity
docsL2vpnMIBObjects=_DocsL2vpnMIBObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,8,1))
_DocsL2vpnIdToIndexTable_Object=MibTable
docsL2vpnIdToIndexTable=_DocsL2vpnIdToIndexTable_Object((1,3,6,1,4,1,4491,2,1,8,1,1))
if mibBuilder.loadTexts:docsL2vpnIdToIndexTable.setStatus(_A)
_DocsL2vpnIdToIndexEntry_Object=MibTableRow
docsL2vpnIdToIndexEntry=_DocsL2vpnIdToIndexEntry_Object((1,3,6,1,4,1,4491,2,1,8,1,1,1))
docsL2vpnIdToIndexEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:docsL2vpnIdToIndexEntry.setStatus(_A)
_DocsL2vpnId_Type=DocsL2vpnIdentifier
_DocsL2vpnId_Object=MibTableColumn
docsL2vpnId=_DocsL2vpnId_Object((1,3,6,1,4,1,4491,2,1,8,1,1,1,1),_DocsL2vpnId_Type())
docsL2vpnId.setMaxAccess(_X)
if mibBuilder.loadTexts:docsL2vpnId.setStatus(_A)
_DocsL2vpnIdToIndexIdx_Type=DocsL2vpnIndex
_DocsL2vpnIdToIndexIdx_Object=MibTableColumn
docsL2vpnIdToIndexIdx=_DocsL2vpnIdToIndexIdx_Object((1,3,6,1,4,1,4491,2,1,8,1,1,1,2),_DocsL2vpnIdToIndexIdx_Type())
docsL2vpnIdToIndexIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnIdToIndexIdx.setStatus(_A)
_DocsL2vpnIndexToIdTable_Object=MibTable
docsL2vpnIndexToIdTable=_DocsL2vpnIndexToIdTable_Object((1,3,6,1,4,1,4491,2,1,8,1,2))
if mibBuilder.loadTexts:docsL2vpnIndexToIdTable.setStatus(_A)
_DocsL2vpnIndexToIdEntry_Object=MibTableRow
docsL2vpnIndexToIdEntry=_DocsL2vpnIndexToIdEntry_Object((1,3,6,1,4,1,4491,2,1,8,1,2,1))
docsL2vpnIndexToIdEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:docsL2vpnIndexToIdEntry.setStatus(_A)
_DocsL2vpnIdx_Type=DocsL2vpnIndex
_DocsL2vpnIdx_Object=MibTableColumn
docsL2vpnIdx=_DocsL2vpnIdx_Object((1,3,6,1,4,1,4491,2,1,8,1,2,1,1),_DocsL2vpnIdx_Type())
docsL2vpnIdx.setMaxAccess(_X)
if mibBuilder.loadTexts:docsL2vpnIdx.setStatus(_A)
_DocsL2vpnIndexToIdId_Type=DocsL2vpnIdentifier
_DocsL2vpnIndexToIdId_Object=MibTableColumn
docsL2vpnIndexToIdId=_DocsL2vpnIndexToIdId_Object((1,3,6,1,4,1,4491,2,1,8,1,2,1,2),_DocsL2vpnIndexToIdId_Type())
docsL2vpnIndexToIdId.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnIndexToIdId.setStatus(_A)
_DocsL2vpnCmTable_Object=MibTable
docsL2vpnCmTable=_DocsL2vpnCmTable_Object((1,3,6,1,4,1,4491,2,1,8,1,3))
if mibBuilder.loadTexts:docsL2vpnCmTable.setStatus(_A)
_DocsL2vpnCmEntry_Object=MibTableRow
docsL2vpnCmEntry=_DocsL2vpnCmEntry_Object((1,3,6,1,4,1,4491,2,1,8,1,3,1))
docsL2vpnCmEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:docsL2vpnCmEntry.setStatus(_A)
_DocsL2vpnCmCompliantCapability_Type=TruthValue
_DocsL2vpnCmCompliantCapability_Object=MibTableColumn
docsL2vpnCmCompliantCapability=_DocsL2vpnCmCompliantCapability_Object((1,3,6,1,4,1,4491,2,1,8,1,3,1,1),_DocsL2vpnCmCompliantCapability_Type())
docsL2vpnCmCompliantCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnCmCompliantCapability.setStatus(_A)
_DocsL2vpnCmDutFilteringCapability_Type=TruthValue
_DocsL2vpnCmDutFilteringCapability_Object=MibTableColumn
docsL2vpnCmDutFilteringCapability=_DocsL2vpnCmDutFilteringCapability_Object((1,3,6,1,4,1,4491,2,1,8,1,3,1,2),_DocsL2vpnCmDutFilteringCapability_Type())
docsL2vpnCmDutFilteringCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnCmDutFilteringCapability.setStatus(_A)
_DocsL2vpnCmDutCMIM_Type=DocsL2vpnIfList
_DocsL2vpnCmDutCMIM_Object=MibTableColumn
docsL2vpnCmDutCMIM=_DocsL2vpnCmDutCMIM_Object((1,3,6,1,4,1,4491,2,1,8,1,3,1,3),_DocsL2vpnCmDutCMIM_Type())
docsL2vpnCmDutCMIM.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnCmDutCMIM.setStatus(_A)
_DocsL2vpnCmDhcpSnooping_Type=DocsL2vpnIfList
_DocsL2vpnCmDhcpSnooping_Object=MibTableColumn
docsL2vpnCmDhcpSnooping=_DocsL2vpnCmDhcpSnooping_Object((1,3,6,1,4,1,4491,2,1,8,1,3,1,4),_DocsL2vpnCmDhcpSnooping_Type())
docsL2vpnCmDhcpSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnCmDhcpSnooping.setStatus(_A)
_DocsL2vpnVpnCmTable_Object=MibTable
docsL2vpnVpnCmTable=_DocsL2vpnVpnCmTable_Object((1,3,6,1,4,1,4491,2,1,8,1,4))
if mibBuilder.loadTexts:docsL2vpnVpnCmTable.setStatus(_A)
_DocsL2vpnVpnCmEntry_Object=MibTableRow
docsL2vpnVpnCmEntry=_DocsL2vpnVpnCmEntry_Object((1,3,6,1,4,1,4491,2,1,8,1,4,1))
docsL2vpnVpnCmEntry.setIndexNames((0,_B,_D),(0,_E,_F))
if mibBuilder.loadTexts:docsL2vpnVpnCmEntry.setStatus(_A)
_DocsL2vpnVpnCmCMIM_Type=DocsL2vpnIfList
_DocsL2vpnVpnCmCMIM_Object=MibTableColumn
docsL2vpnVpnCmCMIM=_DocsL2vpnVpnCmCMIM_Object((1,3,6,1,4,1,4491,2,1,8,1,4,1,1),_DocsL2vpnVpnCmCMIM_Type())
docsL2vpnVpnCmCMIM.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnVpnCmCMIM.setStatus(_A)
class _DocsL2vpnVpnCmIndividualSAId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
_DocsL2vpnVpnCmIndividualSAId_Type.__name__=_M
_DocsL2vpnVpnCmIndividualSAId_Object=MibTableColumn
docsL2vpnVpnCmIndividualSAId=_DocsL2vpnVpnCmIndividualSAId_Object((1,3,6,1,4,1,4491,2,1,8,1,4,1,2),_DocsL2vpnVpnCmIndividualSAId_Type())
docsL2vpnVpnCmIndividualSAId.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnVpnCmIndividualSAId.setStatus(_A)
_DocsL2vpnVpnCmVendorSpecific_Type=OctetString
_DocsL2vpnVpnCmVendorSpecific_Object=MibTableColumn
docsL2vpnVpnCmVendorSpecific=_DocsL2vpnVpnCmVendorSpecific_Object((1,3,6,1,4,1,4491,2,1,8,1,4,1,3),_DocsL2vpnVpnCmVendorSpecific_Type())
docsL2vpnVpnCmVendorSpecific.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnVpnCmVendorSpecific.setStatus(_A)
_DocsL2vpnVpnCmStatsTable_Object=MibTable
docsL2vpnVpnCmStatsTable=_DocsL2vpnVpnCmStatsTable_Object((1,3,6,1,4,1,4491,2,1,8,1,5))
if mibBuilder.loadTexts:docsL2vpnVpnCmStatsTable.setStatus(_A)
_DocsL2vpnVpnCmStatsEntry_Object=MibTableRow
docsL2vpnVpnCmStatsEntry=_DocsL2vpnVpnCmStatsEntry_Object((1,3,6,1,4,1,4491,2,1,8,1,5,1))
docsL2vpnVpnCmStatsEntry.setIndexNames((0,_B,_D),(0,_E,_F))
if mibBuilder.loadTexts:docsL2vpnVpnCmStatsEntry.setStatus(_A)
_DocsL2vpnVpnCmStatsUpstreamPkts_Type=Counter32
_DocsL2vpnVpnCmStatsUpstreamPkts_Object=MibTableColumn
docsL2vpnVpnCmStatsUpstreamPkts=_DocsL2vpnVpnCmStatsUpstreamPkts_Object((1,3,6,1,4,1,4491,2,1,8,1,5,1,1),_DocsL2vpnVpnCmStatsUpstreamPkts_Type())
docsL2vpnVpnCmStatsUpstreamPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnVpnCmStatsUpstreamPkts.setStatus(_A)
_DocsL2vpnVpnCmStatsUpstreamBytes_Type=Counter32
_DocsL2vpnVpnCmStatsUpstreamBytes_Object=MibTableColumn
docsL2vpnVpnCmStatsUpstreamBytes=_DocsL2vpnVpnCmStatsUpstreamBytes_Object((1,3,6,1,4,1,4491,2,1,8,1,5,1,2),_DocsL2vpnVpnCmStatsUpstreamBytes_Type())
docsL2vpnVpnCmStatsUpstreamBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnVpnCmStatsUpstreamBytes.setStatus(_A)
_DocsL2vpnVpnCmStatsUpstreamDiscards_Type=Counter32
_DocsL2vpnVpnCmStatsUpstreamDiscards_Object=MibTableColumn
docsL2vpnVpnCmStatsUpstreamDiscards=_DocsL2vpnVpnCmStatsUpstreamDiscards_Object((1,3,6,1,4,1,4491,2,1,8,1,5,1,3),_DocsL2vpnVpnCmStatsUpstreamDiscards_Type())
docsL2vpnVpnCmStatsUpstreamDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnVpnCmStatsUpstreamDiscards.setStatus(_A)
_DocsL2vpnVpnCmStatsDownstreamPkts_Type=Counter32
_DocsL2vpnVpnCmStatsDownstreamPkts_Object=MibTableColumn
docsL2vpnVpnCmStatsDownstreamPkts=_DocsL2vpnVpnCmStatsDownstreamPkts_Object((1,3,6,1,4,1,4491,2,1,8,1,5,1,4),_DocsL2vpnVpnCmStatsDownstreamPkts_Type())
docsL2vpnVpnCmStatsDownstreamPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnVpnCmStatsDownstreamPkts.setStatus(_A)
_DocsL2vpnVpnCmStatsDownstreamBytes_Type=Counter32
_DocsL2vpnVpnCmStatsDownstreamBytes_Object=MibTableColumn
docsL2vpnVpnCmStatsDownstreamBytes=_DocsL2vpnVpnCmStatsDownstreamBytes_Object((1,3,6,1,4,1,4491,2,1,8,1,5,1,5),_DocsL2vpnVpnCmStatsDownstreamBytes_Type())
docsL2vpnVpnCmStatsDownstreamBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnVpnCmStatsDownstreamBytes.setStatus(_A)
_DocsL2vpnVpnCmStatsDownstreamDiscards_Type=Counter32
_DocsL2vpnVpnCmStatsDownstreamDiscards_Object=MibTableColumn
docsL2vpnVpnCmStatsDownstreamDiscards=_DocsL2vpnVpnCmStatsDownstreamDiscards_Object((1,3,6,1,4,1,4491,2,1,8,1,5,1,6),_DocsL2vpnVpnCmStatsDownstreamDiscards_Type())
docsL2vpnVpnCmStatsDownstreamDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnVpnCmStatsDownstreamDiscards.setStatus(_A)
_DocsL2vpnPortStatusTable_Object=MibTable
docsL2vpnPortStatusTable=_DocsL2vpnPortStatusTable_Object((1,3,6,1,4,1,4491,2,1,8,1,6))
if mibBuilder.loadTexts:docsL2vpnPortStatusTable.setStatus(_A)
_DocsL2vpnPortStatusEntry_Object=MibTableRow
docsL2vpnPortStatusEntry=_DocsL2vpnPortStatusEntry_Object((1,3,6,1,4,1,4491,2,1,8,1,6,1))
docsL2vpnPortStatusEntry.setIndexNames((0,_P,_Q),(0,_B,_D))
if mibBuilder.loadTexts:docsL2vpnPortStatusEntry.setStatus(_A)
class _DocsL2vpnPortStatusGroupSAId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
_DocsL2vpnPortStatusGroupSAId_Type.__name__=_M
_DocsL2vpnPortStatusGroupSAId_Object=MibTableColumn
docsL2vpnPortStatusGroupSAId=_DocsL2vpnPortStatusGroupSAId_Object((1,3,6,1,4,1,4491,2,1,8,1,6,1,1),_DocsL2vpnPortStatusGroupSAId_Type())
docsL2vpnPortStatusGroupSAId.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnPortStatusGroupSAId.setStatus(_A)
_DocsL2vpnSfStatusTable_Object=MibTable
docsL2vpnSfStatusTable=_DocsL2vpnSfStatusTable_Object((1,3,6,1,4,1,4491,2,1,8,1,7))
if mibBuilder.loadTexts:docsL2vpnSfStatusTable.setStatus(_A)
_DocsL2vpnSfStatusEntry_Object=MibTableRow
docsL2vpnSfStatusEntry=_DocsL2vpnSfStatusEntry_Object((1,3,6,1,4,1,4491,2,1,8,1,7,1))
docsL2vpnSfStatusEntry.setIndexNames((0,_K,_L),(0,_H,_J))
if mibBuilder.loadTexts:docsL2vpnSfStatusEntry.setStatus(_A)
_DocsL2vpnSfStatusL2vpnId_Type=OctetString
_DocsL2vpnSfStatusL2vpnId_Object=MibTableColumn
docsL2vpnSfStatusL2vpnId=_DocsL2vpnSfStatusL2vpnId_Object((1,3,6,1,4,1,4491,2,1,8,1,7,1,1),_DocsL2vpnSfStatusL2vpnId_Type())
docsL2vpnSfStatusL2vpnId.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnSfStatusL2vpnId.setStatus(_A)
class _DocsL2vpnSfStatusIngressUserPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_DocsL2vpnSfStatusIngressUserPriority_Type.__name__=_I
_DocsL2vpnSfStatusIngressUserPriority_Object=MibTableColumn
docsL2vpnSfStatusIngressUserPriority=_DocsL2vpnSfStatusIngressUserPriority_Object((1,3,6,1,4,1,4491,2,1,8,1,7,1,2),_DocsL2vpnSfStatusIngressUserPriority_Type())
docsL2vpnSfStatusIngressUserPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnSfStatusIngressUserPriority.setStatus(_A)
_DocsL2vpnSfStatusVendorSpecific_Type=OctetString
_DocsL2vpnSfStatusVendorSpecific_Object=MibTableColumn
docsL2vpnSfStatusVendorSpecific=_DocsL2vpnSfStatusVendorSpecific_Object((1,3,6,1,4,1,4491,2,1,8,1,7,1,3),_DocsL2vpnSfStatusVendorSpecific_Type())
docsL2vpnSfStatusVendorSpecific.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnSfStatusVendorSpecific.setStatus(_A)
_DocsL2vpnPktClassTable_Object=MibTable
docsL2vpnPktClassTable=_DocsL2vpnPktClassTable_Object((1,3,6,1,4,1,4491,2,1,8,1,8))
if mibBuilder.loadTexts:docsL2vpnPktClassTable.setStatus(_A)
_DocsL2vpnPktClassEntry_Object=MibTableRow
docsL2vpnPktClassEntry=_DocsL2vpnPktClassEntry_Object((1,3,6,1,4,1,4491,2,1,8,1,8,1))
docsL2vpnPktClassEntry.setIndexNames((0,_K,_L),(0,_H,_J),(0,_H,_R))
if mibBuilder.loadTexts:docsL2vpnPktClassEntry.setStatus(_A)
_DocsL2vpnPktClassL2vpnId_Type=DocsL2vpnIdentifier
_DocsL2vpnPktClassL2vpnId_Object=MibTableColumn
docsL2vpnPktClassL2vpnId=_DocsL2vpnPktClassL2vpnId_Object((1,3,6,1,4,1,4491,2,1,8,1,8,1,1),_DocsL2vpnPktClassL2vpnId_Type())
docsL2vpnPktClassL2vpnId.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnPktClassL2vpnId.setStatus(_A)
class _DocsL2vpnPktClassUserPriRangeLow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_DocsL2vpnPktClassUserPriRangeLow_Type.__name__=_I
_DocsL2vpnPktClassUserPriRangeLow_Object=MibTableColumn
docsL2vpnPktClassUserPriRangeLow=_DocsL2vpnPktClassUserPriRangeLow_Object((1,3,6,1,4,1,4491,2,1,8,1,8,1,2),_DocsL2vpnPktClassUserPriRangeLow_Type())
docsL2vpnPktClassUserPriRangeLow.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnPktClassUserPriRangeLow.setStatus(_A)
class _DocsL2vpnPktClassUserPriRangeHigh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_DocsL2vpnPktClassUserPriRangeHigh_Type.__name__=_I
_DocsL2vpnPktClassUserPriRangeHigh_Object=MibTableColumn
docsL2vpnPktClassUserPriRangeHigh=_DocsL2vpnPktClassUserPriRangeHigh_Object((1,3,6,1,4,1,4491,2,1,8,1,8,1,3),_DocsL2vpnPktClassUserPriRangeHigh_Type())
docsL2vpnPktClassUserPriRangeHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnPktClassUserPriRangeHigh.setStatus(_A)
_DocsL2vpnPktClassCMIM_Type=DocsL2vpnIfList
_DocsL2vpnPktClassCMIM_Object=MibTableColumn
docsL2vpnPktClassCMIM=_DocsL2vpnPktClassCMIM_Object((1,3,6,1,4,1,4491,2,1,8,1,8,1,4),_DocsL2vpnPktClassCMIM_Type())
docsL2vpnPktClassCMIM.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnPktClassCMIM.setStatus(_A)
_DocsL2vpnPktClassVendorSpecific_Type=OctetString
_DocsL2vpnPktClassVendorSpecific_Object=MibTableColumn
docsL2vpnPktClassVendorSpecific=_DocsL2vpnPktClassVendorSpecific_Object((1,3,6,1,4,1,4491,2,1,8,1,8,1,5),_DocsL2vpnPktClassVendorSpecific_Type())
docsL2vpnPktClassVendorSpecific.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnPktClassVendorSpecific.setStatus(_A)
_DocsL2vpnCmNsiTable_Object=MibTable
docsL2vpnCmNsiTable=_DocsL2vpnCmNsiTable_Object((1,3,6,1,4,1,4491,2,1,8,1,9))
if mibBuilder.loadTexts:docsL2vpnCmNsiTable.setStatus(_A)
_DocsL2vpnCmNsiEntry_Object=MibTableRow
docsL2vpnCmNsiEntry=_DocsL2vpnCmNsiEntry_Object((1,3,6,1,4,1,4491,2,1,8,1,9,1))
docsL2vpnCmNsiEntry.setIndexNames((0,_B,_D),(0,_E,_F))
if mibBuilder.loadTexts:docsL2vpnCmNsiEntry.setStatus(_A)
_DocsL2vpnCmNsiEncapSubtype_Type=DocsNsiEncapSubtype
_DocsL2vpnCmNsiEncapSubtype_Object=MibTableColumn
docsL2vpnCmNsiEncapSubtype=_DocsL2vpnCmNsiEncapSubtype_Object((1,3,6,1,4,1,4491,2,1,8,1,9,1,1),_DocsL2vpnCmNsiEncapSubtype_Type())
docsL2vpnCmNsiEncapSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnCmNsiEncapSubtype.setStatus(_A)
_DocsL2vpnCmNsiEncapValue_Type=DocsNsiEncapValue
_DocsL2vpnCmNsiEncapValue_Object=MibTableColumn
docsL2vpnCmNsiEncapValue=_DocsL2vpnCmNsiEncapValue_Object((1,3,6,1,4,1,4491,2,1,8,1,9,1,2),_DocsL2vpnCmNsiEncapValue_Type())
docsL2vpnCmNsiEncapValue.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnCmNsiEncapValue.setStatus(_A)
_DocsL2vpnCmNsiAGI_Type=OctetString
_DocsL2vpnCmNsiAGI_Object=MibTableColumn
docsL2vpnCmNsiAGI=_DocsL2vpnCmNsiAGI_Object((1,3,6,1,4,1,4491,2,1,8,1,9,1,3),_DocsL2vpnCmNsiAGI_Type())
docsL2vpnCmNsiAGI.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnCmNsiAGI.setStatus(_A)
_DocsL2vpnCmNsiSAII_Type=OctetString
_DocsL2vpnCmNsiSAII_Object=MibTableColumn
docsL2vpnCmNsiSAII=_DocsL2vpnCmNsiSAII_Object((1,3,6,1,4,1,4491,2,1,8,1,9,1,4),_DocsL2vpnCmNsiSAII_Type())
docsL2vpnCmNsiSAII.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnCmNsiSAII.setStatus(_A)
_DocsL2vpnCmNsiTAII_Type=OctetString
_DocsL2vpnCmNsiTAII_Object=MibTableColumn
docsL2vpnCmNsiTAII=_DocsL2vpnCmNsiTAII_Object((1,3,6,1,4,1,4491,2,1,8,1,9,1,5),_DocsL2vpnCmNsiTAII_Type())
docsL2vpnCmNsiTAII.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnCmNsiTAII.setStatus(_A)
_DocsL2vpnCmVpnCpeTable_Object=MibTable
docsL2vpnCmVpnCpeTable=_DocsL2vpnCmVpnCpeTable_Object((1,3,6,1,4,1,4491,2,1,8,1,10))
if mibBuilder.loadTexts:docsL2vpnCmVpnCpeTable.setStatus(_A)
_DocsL2vpnCmVpnCpeEntry_Object=MibTableRow
docsL2vpnCmVpnCpeEntry=_DocsL2vpnCmVpnCpeEntry_Object((1,3,6,1,4,1,4491,2,1,8,1,10,1))
docsL2vpnCmVpnCpeEntry.setIndexNames((0,_E,_F),(0,_B,_D),(0,_B,_N))
if mibBuilder.loadTexts:docsL2vpnCmVpnCpeEntry.setStatus(_A)
_DocsL2vpnCmVpnCpeMacAddress_Type=MacAddress
_DocsL2vpnCmVpnCpeMacAddress_Object=MibTableColumn
docsL2vpnCmVpnCpeMacAddress=_DocsL2vpnCmVpnCpeMacAddress_Object((1,3,6,1,4,1,4491,2,1,8,1,10,1,1),_DocsL2vpnCmVpnCpeMacAddress_Type())
docsL2vpnCmVpnCpeMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnCmVpnCpeMacAddress.setStatus(_A)
_DocsL2vpnVpnCmCpeTable_Object=MibTable
docsL2vpnVpnCmCpeTable=_DocsL2vpnVpnCmCpeTable_Object((1,3,6,1,4,1,4491,2,1,8,1,11))
if mibBuilder.loadTexts:docsL2vpnVpnCmCpeTable.setStatus(_A)
_DocsL2vpnVpnCmCpeEntry_Object=MibTableRow
docsL2vpnVpnCmCpeEntry=_DocsL2vpnVpnCmCpeEntry_Object((1,3,6,1,4,1,4491,2,1,8,1,11,1))
docsL2vpnVpnCmCpeEntry.setIndexNames((0,_B,_D),(0,_E,_F),(0,_B,_O))
if mibBuilder.loadTexts:docsL2vpnVpnCmCpeEntry.setStatus(_A)
_DocsL2vpnVpnCmCpeMacAddress_Type=MacAddress
_DocsL2vpnVpnCmCpeMacAddress_Object=MibTableColumn
docsL2vpnVpnCmCpeMacAddress=_DocsL2vpnVpnCmCpeMacAddress_Object((1,3,6,1,4,1,4491,2,1,8,1,11,1,1),_DocsL2vpnVpnCmCpeMacAddress_Type())
docsL2vpnVpnCmCpeMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnVpnCmCpeMacAddress.setStatus(_A)
_DocsL2vpnDot1qTpFdbExtTable_Object=MibTable
docsL2vpnDot1qTpFdbExtTable=_DocsL2vpnDot1qTpFdbExtTable_Object((1,3,6,1,4,1,4491,2,1,8,1,12))
if mibBuilder.loadTexts:docsL2vpnDot1qTpFdbExtTable.setStatus(_A)
_DocsL2vpnDot1qTpFdbExtEntry_Object=MibTableRow
docsL2vpnDot1qTpFdbExtEntry=_DocsL2vpnDot1qTpFdbExtEntry_Object((1,3,6,1,4,1,4491,2,1,8,1,12,1))
docsL2vpnDot1qTpFdbExtEntry.setIndexNames((0,_G,_S),(0,_G,_T))
if mibBuilder.loadTexts:docsL2vpnDot1qTpFdbExtEntry.setStatus(_A)
_DocsL2vpnDot1qTpFdbExtTransmitPkts_Type=Counter32
_DocsL2vpnDot1qTpFdbExtTransmitPkts_Object=MibTableColumn
docsL2vpnDot1qTpFdbExtTransmitPkts=_DocsL2vpnDot1qTpFdbExtTransmitPkts_Object((1,3,6,1,4,1,4491,2,1,8,1,12,1,1),_DocsL2vpnDot1qTpFdbExtTransmitPkts_Type())
docsL2vpnDot1qTpFdbExtTransmitPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnDot1qTpFdbExtTransmitPkts.setStatus(_A)
_DocsL2vpnDot1qTpFdbExtReceivePkts_Type=Counter32
_DocsL2vpnDot1qTpFdbExtReceivePkts_Object=MibTableColumn
docsL2vpnDot1qTpFdbExtReceivePkts=_DocsL2vpnDot1qTpFdbExtReceivePkts_Object((1,3,6,1,4,1,4491,2,1,8,1,12,1,2),_DocsL2vpnDot1qTpFdbExtReceivePkts_Type())
docsL2vpnDot1qTpFdbExtReceivePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnDot1qTpFdbExtReceivePkts.setStatus(_A)
_DocsL2vpnDot1qTpGroupExtTable_Object=MibTable
docsL2vpnDot1qTpGroupExtTable=_DocsL2vpnDot1qTpGroupExtTable_Object((1,3,6,1,4,1,4491,2,1,8,1,13))
if mibBuilder.loadTexts:docsL2vpnDot1qTpGroupExtTable.setStatus(_A)
_DocsL2vpnDot1qTpGroupExtEntry_Object=MibTableRow
docsL2vpnDot1qTpGroupExtEntry=_DocsL2vpnDot1qTpGroupExtEntry_Object((1,3,6,1,4,1,4491,2,1,8,1,13,1))
docsL2vpnDot1qTpGroupExtEntry.setIndexNames((0,_G,_V),(0,_G,_U))
if mibBuilder.loadTexts:docsL2vpnDot1qTpGroupExtEntry.setStatus(_A)
_DocsL2vpnDot1qTpGroupExtTransmitPkts_Type=Counter32
_DocsL2vpnDot1qTpGroupExtTransmitPkts_Object=MibTableColumn
docsL2vpnDot1qTpGroupExtTransmitPkts=_DocsL2vpnDot1qTpGroupExtTransmitPkts_Object((1,3,6,1,4,1,4491,2,1,8,1,13,1,1),_DocsL2vpnDot1qTpGroupExtTransmitPkts_Type())
docsL2vpnDot1qTpGroupExtTransmitPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnDot1qTpGroupExtTransmitPkts.setStatus(_A)
_DocsL2vpnDot1qTpGroupExtReceivePkts_Type=Counter32
_DocsL2vpnDot1qTpGroupExtReceivePkts_Object=MibTableColumn
docsL2vpnDot1qTpGroupExtReceivePkts=_DocsL2vpnDot1qTpGroupExtReceivePkts_Object((1,3,6,1,4,1,4491,2,1,8,1,13,1,2),_DocsL2vpnDot1qTpGroupExtReceivePkts_Type())
docsL2vpnDot1qTpGroupExtReceivePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:docsL2vpnDot1qTpGroupExtReceivePkts.setStatus(_A)
_DocsL2vpnConformance_ObjectIdentity=ObjectIdentity
docsL2vpnConformance=_DocsL2vpnConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,1,8,2))
_DocsL2vpnCompliances_ObjectIdentity=ObjectIdentity
docsL2vpnCompliances=_DocsL2vpnCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,1,8,2,1))
_DocsL2vpnGroups_ObjectIdentity=ObjectIdentity
docsL2vpnGroups=_DocsL2vpnGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,1,8,2,2))
docsL2vpnBaseGroup=ObjectGroup((1,3,6,1,4,1,4491,2,1,8,2,2,1))
docsL2vpnBaseGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:docsL2vpnBaseGroup.setStatus(_A)
docsL2vpnPointToPointGroup=ObjectGroup((1,3,6,1,4,1,4491,2,1,8,2,2,2))
docsL2vpnPointToPointGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:docsL2vpnPointToPointGroup.setStatus(_A)
docsL2vpnMultipointGroup=ObjectGroup((1,3,6,1,4,1,4491,2,1,8,2,2,3))
docsL2vpnMultipointGroup.setObjects(*((_B,_N),(_B,_O),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:docsL2vpnMultipointGroup.setStatus(_A)
docsL2vpnCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,1,8,2,1,1))
docsL2vpnCompliance.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:docsL2vpnCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DocsL2vpnIdentifier':DocsL2vpnIdentifier,'DocsL2vpnIndex':DocsL2vpnIndex,'DocsNsiEncapSubtype':DocsNsiEncapSubtype,'DocsNsiEncapValue':DocsNsiEncapValue,'DocsL2vpnIfList':DocsL2vpnIfList,'docsL2vpnMIB':docsL2vpnMIB,'docsL2vpnMIBNotifications':docsL2vpnMIBNotifications,'docsL2vpnMIBObjects':docsL2vpnMIBObjects,'docsL2vpnIdToIndexTable':docsL2vpnIdToIndexTable,'docsL2vpnIdToIndexEntry':docsL2vpnIdToIndexEntry,_W:docsL2vpnId,_Y:docsL2vpnIdToIndexIdx,'docsL2vpnIndexToIdTable':docsL2vpnIndexToIdTable,'docsL2vpnIndexToIdEntry':docsL2vpnIndexToIdEntry,_D:docsL2vpnIdx,_Z:docsL2vpnIndexToIdId,'docsL2vpnCmTable':docsL2vpnCmTable,'docsL2vpnCmEntry':docsL2vpnCmEntry,_a:docsL2vpnCmCompliantCapability,_b:docsL2vpnCmDutFilteringCapability,_c:docsL2vpnCmDutCMIM,_d:docsL2vpnCmDhcpSnooping,'docsL2vpnVpnCmTable':docsL2vpnVpnCmTable,'docsL2vpnVpnCmEntry':docsL2vpnVpnCmEntry,_e:docsL2vpnVpnCmCMIM,_g:docsL2vpnVpnCmIndividualSAId,_f:docsL2vpnVpnCmVendorSpecific,'docsL2vpnVpnCmStatsTable':docsL2vpnVpnCmStatsTable,'docsL2vpnVpnCmStatsEntry':docsL2vpnVpnCmStatsEntry,_h:docsL2vpnVpnCmStatsUpstreamPkts,_i:docsL2vpnVpnCmStatsUpstreamBytes,_j:docsL2vpnVpnCmStatsUpstreamDiscards,_k:docsL2vpnVpnCmStatsDownstreamPkts,_l:docsL2vpnVpnCmStatsDownstreamBytes,_m:docsL2vpnVpnCmStatsDownstreamDiscards,'docsL2vpnPortStatusTable':docsL2vpnPortStatusTable,'docsL2vpnPortStatusEntry':docsL2vpnPortStatusEntry,_n:docsL2vpnPortStatusGroupSAId,'docsL2vpnSfStatusTable':docsL2vpnSfStatusTable,'docsL2vpnSfStatusEntry':docsL2vpnSfStatusEntry,_o:docsL2vpnSfStatusL2vpnId,_p:docsL2vpnSfStatusIngressUserPriority,_q:docsL2vpnSfStatusVendorSpecific,'docsL2vpnPktClassTable':docsL2vpnPktClassTable,'docsL2vpnPktClassEntry':docsL2vpnPktClassEntry,_r:docsL2vpnPktClassL2vpnId,_s:docsL2vpnPktClassUserPriRangeLow,_t:docsL2vpnPktClassUserPriRangeHigh,_u:docsL2vpnPktClassCMIM,_v:docsL2vpnPktClassVendorSpecific,'docsL2vpnCmNsiTable':docsL2vpnCmNsiTable,'docsL2vpnCmNsiEntry':docsL2vpnCmNsiEntry,_w:docsL2vpnCmNsiEncapSubtype,_x:docsL2vpnCmNsiEncapValue,_y:docsL2vpnCmNsiAGI,_z:docsL2vpnCmNsiSAII,_A0:docsL2vpnCmNsiTAII,'docsL2vpnCmVpnCpeTable':docsL2vpnCmVpnCpeTable,'docsL2vpnCmVpnCpeEntry':docsL2vpnCmVpnCpeEntry,_N:docsL2vpnCmVpnCpeMacAddress,'docsL2vpnVpnCmCpeTable':docsL2vpnVpnCmCpeTable,'docsL2vpnVpnCmCpeEntry':docsL2vpnVpnCmCpeEntry,_O:docsL2vpnVpnCmCpeMacAddress,'docsL2vpnDot1qTpFdbExtTable':docsL2vpnDot1qTpFdbExtTable,'docsL2vpnDot1qTpFdbExtEntry':docsL2vpnDot1qTpFdbExtEntry,_A1:docsL2vpnDot1qTpFdbExtTransmitPkts,_A2:docsL2vpnDot1qTpFdbExtReceivePkts,'docsL2vpnDot1qTpGroupExtTable':docsL2vpnDot1qTpGroupExtTable,'docsL2vpnDot1qTpGroupExtEntry':docsL2vpnDot1qTpGroupExtEntry,_A3:docsL2vpnDot1qTpGroupExtTransmitPkts,_A4:docsL2vpnDot1qTpGroupExtReceivePkts,'docsL2vpnConformance':docsL2vpnConformance,'docsL2vpnCompliances':docsL2vpnCompliances,'docsL2vpnCompliance':docsL2vpnCompliance,'docsL2vpnGroups':docsL2vpnGroups,_A5:docsL2vpnBaseGroup,_A6:docsL2vpnPointToPointGroup,_A7:docsL2vpnMultipointGroup})