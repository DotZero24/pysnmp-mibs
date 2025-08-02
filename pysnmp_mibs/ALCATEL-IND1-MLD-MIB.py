_BD='alaMldPortVlanGroup'
_BC='alaMldPortGroup'
_BB='alaMldTunnelGroup'
_BA='alaMldForwardGroup'
_B9='alaMldSourceGroup'
_B8='alaMldStaticQuerierGroup'
_B7='alaMldQuerierGroup'
_B6='alaMldStaticNeighborGroup'
_B5='alaMldNeighborGroup'
_B4='alaMldStaticMemberGroup'
_B3='alaMldMemberGroup'
_B2='alaMldVlanGroup'
_B1='alaMldGroup'
_B0='alaMldPortVlanMaxGroupExceedAction'
_A_='alaMldPortVlanMaxGroupLimit'
_Az='alaMldPortVlanCurrentGroupCount'
_Ay='alaMldPortMaxGroupExceedAction'
_Ax='alaMldPortMaxGroupLimit'
_Aw='alaMldTunnelNextType'
_Av='alaMldTunnelType'
_Au='alaMldTunnelIfIndex'
_At='alaMldForwardNextType'
_As='alaMldForwardType'
_Ar='alaMldForwardIfIndex'
_Aq='alaMldSourceType'
_Ap='alaMldSourceIfIndex'
_Ao='alaMldStaticQuerierRowStatus'
_An='alaMldQuerierTimeout'
_Am='alaMldQuerierCount'
_Al='alaMldStaticNeighborRowStatus'
_Ak='alaMldNeighborTimeout'
_Aj='alaMldNeighborCount'
_Ai='alaMldStaticMemberRowStatus'
_Ah='alaMldMemberTimeout'
_Ag='alaMldMemberCount'
_Af='alaMldMemberMode'
_Ae='alaMldVlanSpoofAddress'
_Ad='alaMldVlanSpoofAddressType'
_Ac='alaMldVlanMaxGroupExceedAction'
_Ab='alaMldVlanMaxGroupLimit'
_Aa='alaMldVlanQuerierForwarding'
_AZ='alaMldVlanUnsolicitedReportInterval'
_AY='alaMldVlanProxying'
_AX='alaMldVlanSourceTimeout'
_AW='alaMldVlanRouterTimeout'
_AV='alaMldVlanLastMemberQueryInterval'
_AU='alaMldVlanQueryResponseInterval'
_AT='alaMldVlanQueryInterval'
_AS='alaMldVlanRobustness'
_AR='alaMldVlanVersion'
_AQ='alaMldVlanZapping'
_AP='alaMldVlanSpoofing'
_AO='alaMldVlanQuerying'
_AN='alaMldVlanStatus'
_AM='alaMldBufferPacket'
_AL='alaMldFloodUnknown'
_AK='alaMldMaxGroupExceedAction'
_AJ='alaMldMaxGroupLimit'
_AI='alaMldQuerierForwarding'
_AH='alaMldUnsolicitedReportInterval'
_AG='alaMldProxying'
_AF='alaMldSourceTimeout'
_AE='alaMldRouterTimeout'
_AD='alaMldLastMemberQueryInterval'
_AC='alaMldQueryResponseInterval'
_AB='alaMldQueryInterval'
_AA='alaMldRobustness'
_A9='alaMldVersion'
_A8='alaMldZapping'
_A7='alaMldSpoofing'
_A6='alaMldQuerying'
_A5='alaMldStatus'
_A4='alaMldVlanId'
_A3='alaMldTunnelNextDestAddress'
_A2='alaMldTunnelOrigAddress'
_A1='alaMldTunnelDestAddress'
_A0='alaMldTunnelHostAddress'
_z='alaMldTunnelGroupAddress'
_y='alaMldTunnelVlan'
_x='alaMldForwardNextIfIndex'
_w='alaMldForwardNextVlan'
_v='alaMldForwardOrigAddress'
_u='alaMldForwardDestAddress'
_t='alaMldForwardHostAddress'
_s='alaMldForwardGroupAddress'
_r='alaMldForwardVlan'
_q='alaMldSourceOrigAddress'
_p='alaMldSourceDestAddress'
_o='alaMldSourceHostAddress'
_n='alaMldSourceGroupAddress'
_m='alaMldSourceVlan'
_l='alaMldStaticQuerierIfIndex'
_k='alaMldStaticQuerierVlan'
_j='alaMldQuerierHostAddress'
_i='alaMldQuerierIfIndex'
_h='alaMldQuerierVlan'
_g='alaMldStaticNeighborIfIndex'
_f='alaMldStaticNeighborVlan'
_e='alaMldNeighborHostAddress'
_d='alaMldNeighborIfIndex'
_c='alaMldNeighborVlan'
_b='alaMldStaticMemberGroupAddress'
_a='alaMldStaticMemberIfIndex'
_Z='alaMldStaticMemberVlan'
_Y='alaMldMemberSourceAddress'
_X='alaMldMemberGroupAddress'
_W='alaMldMemberIfIndex'
_V='alaMldMemberVlan'
_U='obsolete'
_T='alaMldVlanIndex'
_S='InetAddressType'
_R='alaMldPortIfIndex'
_Q='read-create'
_P='replace'
_O='drop'
_N='milliseconds'
_M='pim'
_L='mcast'
_K='seconds'
_J='Unsigned32'
_I='disable'
_H='enable'
_G='read-only'
_F='none'
_E='Integer32'
_D='not-accessible'
_C='read-write'
_B='ALCATEL-IND1-MLD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Mld,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1Mld')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressIPv6,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv6',_S)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1MldMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1))
if mibBuilder.loadTexts:alcatelIND1MldMIB.setRevisions(('2009-08-06 00:00','2008-08-08 00:00','2007-04-03 00:00'))
_AlcatelIND1MldMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1MldMIBObjects=_AlcatelIND1MldMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,1))
_AlaMld_ObjectIdentity=ObjectIdentity
alaMld=_AlaMld_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1))
class _AlaMldStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_AlaMldStatus_Type.__name__=_E
_AlaMldStatus_Object=MibScalar
alaMldStatus=_AlaMldStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,1),_AlaMldStatus_Type())
alaMldStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldStatus.setStatus(_A)
class _AlaMldQuerying_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_AlaMldQuerying_Type.__name__=_E
_AlaMldQuerying_Object=MibScalar
alaMldQuerying=_AlaMldQuerying_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,2),_AlaMldQuerying_Type())
alaMldQuerying.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldQuerying.setStatus(_A)
class _AlaMldSpoofing_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_AlaMldSpoofing_Type.__name__=_E
_AlaMldSpoofing_Object=MibScalar
alaMldSpoofing=_AlaMldSpoofing_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,3),_AlaMldSpoofing_Type())
alaMldSpoofing.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldSpoofing.setStatus(_A)
class _AlaMldZapping_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_AlaMldZapping_Type.__name__=_E
_AlaMldZapping_Object=MibScalar
alaMldZapping=_AlaMldZapping_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,4),_AlaMldZapping_Type())
alaMldZapping.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldZapping.setStatus(_A)
class _AlaMldVersion_Type(Unsigned32):defaultValue=1
_AlaMldVersion_Type.__name__=_J
_AlaMldVersion_Object=MibScalar
alaMldVersion=_AlaMldVersion_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,5),_AlaMldVersion_Type())
alaMldVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVersion.setStatus(_A)
class _AlaMldRobustness_Type(Unsigned32):defaultValue=2
_AlaMldRobustness_Type.__name__=_J
_AlaMldRobustness_Object=MibScalar
alaMldRobustness=_AlaMldRobustness_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,6),_AlaMldRobustness_Type())
alaMldRobustness.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldRobustness.setStatus(_A)
class _AlaMldQueryInterval_Type(Unsigned32):defaultValue=125
_AlaMldQueryInterval_Type.__name__=_J
_AlaMldQueryInterval_Object=MibScalar
alaMldQueryInterval=_AlaMldQueryInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,7),_AlaMldQueryInterval_Type())
alaMldQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:alaMldQueryInterval.setUnits(_K)
class _AlaMldQueryResponseInterval_Type(Unsigned32):defaultValue=10000
_AlaMldQueryResponseInterval_Type.__name__=_J
_AlaMldQueryResponseInterval_Object=MibScalar
alaMldQueryResponseInterval=_AlaMldQueryResponseInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,8),_AlaMldQueryResponseInterval_Type())
alaMldQueryResponseInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldQueryResponseInterval.setStatus(_A)
if mibBuilder.loadTexts:alaMldQueryResponseInterval.setUnits(_N)
class _AlaMldLastMemberQueryInterval_Type(Unsigned32):defaultValue=1000
_AlaMldLastMemberQueryInterval_Type.__name__=_J
_AlaMldLastMemberQueryInterval_Object=MibScalar
alaMldLastMemberQueryInterval=_AlaMldLastMemberQueryInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,9),_AlaMldLastMemberQueryInterval_Type())
alaMldLastMemberQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldLastMemberQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:alaMldLastMemberQueryInterval.setUnits(_N)
class _AlaMldRouterTimeout_Type(Unsigned32):defaultValue=90
_AlaMldRouterTimeout_Type.__name__=_J
_AlaMldRouterTimeout_Object=MibScalar
alaMldRouterTimeout=_AlaMldRouterTimeout_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,10),_AlaMldRouterTimeout_Type())
alaMldRouterTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldRouterTimeout.setStatus(_A)
if mibBuilder.loadTexts:alaMldRouterTimeout.setUnits(_K)
class _AlaMldSourceTimeout_Type(Unsigned32):defaultValue=30
_AlaMldSourceTimeout_Type.__name__=_J
_AlaMldSourceTimeout_Object=MibScalar
alaMldSourceTimeout=_AlaMldSourceTimeout_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,11),_AlaMldSourceTimeout_Type())
alaMldSourceTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldSourceTimeout.setStatus(_A)
if mibBuilder.loadTexts:alaMldSourceTimeout.setUnits(_K)
class _AlaMldProxying_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_AlaMldProxying_Type.__name__=_E
_AlaMldProxying_Object=MibScalar
alaMldProxying=_AlaMldProxying_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,12),_AlaMldProxying_Type())
alaMldProxying.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldProxying.setStatus(_A)
class _AlaMldUnsolicitedReportInterval_Type(Unsigned32):defaultValue=1
_AlaMldUnsolicitedReportInterval_Type.__name__=_J
_AlaMldUnsolicitedReportInterval_Object=MibScalar
alaMldUnsolicitedReportInterval=_AlaMldUnsolicitedReportInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,13),_AlaMldUnsolicitedReportInterval_Type())
alaMldUnsolicitedReportInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldUnsolicitedReportInterval.setStatus(_A)
if mibBuilder.loadTexts:alaMldUnsolicitedReportInterval.setUnits(_K)
class _AlaMldQuerierForwarding_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_AlaMldQuerierForwarding_Type.__name__=_E
_AlaMldQuerierForwarding_Object=MibScalar
alaMldQuerierForwarding=_AlaMldQuerierForwarding_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,14),_AlaMldQuerierForwarding_Type())
alaMldQuerierForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldQuerierForwarding.setStatus(_A)
class _AlaMldMaxGroupLimit_Type(Unsigned32):defaultValue=0
_AlaMldMaxGroupLimit_Type.__name__=_J
_AlaMldMaxGroupLimit_Object=MibScalar
alaMldMaxGroupLimit=_AlaMldMaxGroupLimit_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,15),_AlaMldMaxGroupLimit_Type())
alaMldMaxGroupLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldMaxGroupLimit.setStatus(_A)
class _AlaMldMaxGroupExceedAction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_O,1),(_P,2)))
_AlaMldMaxGroupExceedAction_Type.__name__=_E
_AlaMldMaxGroupExceedAction_Object=MibScalar
alaMldMaxGroupExceedAction=_AlaMldMaxGroupExceedAction_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,16),_AlaMldMaxGroupExceedAction_Type())
alaMldMaxGroupExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldMaxGroupExceedAction.setStatus(_A)
class _AlaMldFloodUnknown_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_AlaMldFloodUnknown_Type.__name__=_E
_AlaMldFloodUnknown_Object=MibScalar
alaMldFloodUnknown=_AlaMldFloodUnknown_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,17),_AlaMldFloodUnknown_Type())
alaMldFloodUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldFloodUnknown.setStatus(_A)
class _AlaMldBufferPacket_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_AlaMldBufferPacket_Type.__name__=_E
_AlaMldBufferPacket_Object=MibScalar
alaMldBufferPacket=_AlaMldBufferPacket_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,1,18),_AlaMldBufferPacket_Type())
alaMldBufferPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldBufferPacket.setStatus(_A)
_AlaMldVlan_ObjectIdentity=ObjectIdentity
alaMldVlan=_AlaMldVlan_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2))
_AlaMldVlanTable_Object=MibTable
alaMldVlanTable=_AlaMldVlanTable_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1))
if mibBuilder.loadTexts:alaMldVlanTable.setStatus(_A)
_AlaMldVlanEntry_Object=MibTableRow
alaMldVlanEntry=_AlaMldVlanEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1))
alaMldVlanEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:alaMldVlanEntry.setStatus(_A)
_AlaMldVlanIndex_Type=Unsigned32
_AlaMldVlanIndex_Object=MibTableColumn
alaMldVlanIndex=_AlaMldVlanIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,1),_AlaMldVlanIndex_Type())
alaMldVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldVlanIndex.setStatus(_A)
class _AlaMldVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_AlaMldVlanStatus_Type.__name__=_E
_AlaMldVlanStatus_Object=MibTableColumn
alaMldVlanStatus=_AlaMldVlanStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,2),_AlaMldVlanStatus_Type())
alaMldVlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanStatus.setStatus(_A)
class _AlaMldVlanQuerying_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_AlaMldVlanQuerying_Type.__name__=_E
_AlaMldVlanQuerying_Object=MibTableColumn
alaMldVlanQuerying=_AlaMldVlanQuerying_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,3),_AlaMldVlanQuerying_Type())
alaMldVlanQuerying.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanQuerying.setStatus(_A)
class _AlaMldVlanSpoofing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_AlaMldVlanSpoofing_Type.__name__=_E
_AlaMldVlanSpoofing_Object=MibTableColumn
alaMldVlanSpoofing=_AlaMldVlanSpoofing_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,4),_AlaMldVlanSpoofing_Type())
alaMldVlanSpoofing.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanSpoofing.setStatus(_A)
class _AlaMldVlanZapping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_AlaMldVlanZapping_Type.__name__=_E
_AlaMldVlanZapping_Object=MibTableColumn
alaMldVlanZapping=_AlaMldVlanZapping_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,5),_AlaMldVlanZapping_Type())
alaMldVlanZapping.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanZapping.setStatus(_A)
_AlaMldVlanVersion_Type=Unsigned32
_AlaMldVlanVersion_Object=MibTableColumn
alaMldVlanVersion=_AlaMldVlanVersion_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,6),_AlaMldVlanVersion_Type())
alaMldVlanVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanVersion.setStatus(_A)
_AlaMldVlanRobustness_Type=Unsigned32
_AlaMldVlanRobustness_Object=MibTableColumn
alaMldVlanRobustness=_AlaMldVlanRobustness_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,7),_AlaMldVlanRobustness_Type())
alaMldVlanRobustness.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanRobustness.setStatus(_A)
_AlaMldVlanQueryInterval_Type=Unsigned32
_AlaMldVlanQueryInterval_Object=MibTableColumn
alaMldVlanQueryInterval=_AlaMldVlanQueryInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,8),_AlaMldVlanQueryInterval_Type())
alaMldVlanQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:alaMldVlanQueryInterval.setUnits(_K)
_AlaMldVlanQueryResponseInterval_Type=Unsigned32
_AlaMldVlanQueryResponseInterval_Object=MibTableColumn
alaMldVlanQueryResponseInterval=_AlaMldVlanQueryResponseInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,9),_AlaMldVlanQueryResponseInterval_Type())
alaMldVlanQueryResponseInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanQueryResponseInterval.setStatus(_A)
if mibBuilder.loadTexts:alaMldVlanQueryResponseInterval.setUnits(_N)
_AlaMldVlanLastMemberQueryInterval_Type=Unsigned32
_AlaMldVlanLastMemberQueryInterval_Object=MibTableColumn
alaMldVlanLastMemberQueryInterval=_AlaMldVlanLastMemberQueryInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,10),_AlaMldVlanLastMemberQueryInterval_Type())
alaMldVlanLastMemberQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanLastMemberQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:alaMldVlanLastMemberQueryInterval.setUnits(_N)
_AlaMldVlanRouterTimeout_Type=Unsigned32
_AlaMldVlanRouterTimeout_Object=MibTableColumn
alaMldVlanRouterTimeout=_AlaMldVlanRouterTimeout_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,11),_AlaMldVlanRouterTimeout_Type())
alaMldVlanRouterTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanRouterTimeout.setStatus(_A)
if mibBuilder.loadTexts:alaMldVlanRouterTimeout.setUnits(_K)
_AlaMldVlanSourceTimeout_Type=Unsigned32
_AlaMldVlanSourceTimeout_Object=MibTableColumn
alaMldVlanSourceTimeout=_AlaMldVlanSourceTimeout_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,12),_AlaMldVlanSourceTimeout_Type())
alaMldVlanSourceTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanSourceTimeout.setStatus(_A)
if mibBuilder.loadTexts:alaMldVlanSourceTimeout.setUnits(_K)
class _AlaMldVlanProxying_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_AlaMldVlanProxying_Type.__name__=_E
_AlaMldVlanProxying_Object=MibTableColumn
alaMldVlanProxying=_AlaMldVlanProxying_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,13),_AlaMldVlanProxying_Type())
alaMldVlanProxying.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanProxying.setStatus(_A)
_AlaMldVlanUnsolicitedReportInterval_Type=Unsigned32
_AlaMldVlanUnsolicitedReportInterval_Object=MibTableColumn
alaMldVlanUnsolicitedReportInterval=_AlaMldVlanUnsolicitedReportInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,14),_AlaMldVlanUnsolicitedReportInterval_Type())
alaMldVlanUnsolicitedReportInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanUnsolicitedReportInterval.setStatus(_A)
if mibBuilder.loadTexts:alaMldVlanUnsolicitedReportInterval.setUnits(_K)
class _AlaMldVlanQuerierForwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_AlaMldVlanQuerierForwarding_Type.__name__=_E
_AlaMldVlanQuerierForwarding_Object=MibTableColumn
alaMldVlanQuerierForwarding=_AlaMldVlanQuerierForwarding_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,15),_AlaMldVlanQuerierForwarding_Type())
alaMldVlanQuerierForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanQuerierForwarding.setStatus(_A)
class _AlaMldVlanMaxGroupLimit_Type(Unsigned32):defaultValue=0
_AlaMldVlanMaxGroupLimit_Type.__name__=_J
_AlaMldVlanMaxGroupLimit_Object=MibTableColumn
alaMldVlanMaxGroupLimit=_AlaMldVlanMaxGroupLimit_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,16),_AlaMldVlanMaxGroupLimit_Type())
alaMldVlanMaxGroupLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanMaxGroupLimit.setStatus(_A)
class _AlaMldVlanMaxGroupExceedAction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_O,1),(_P,2)))
_AlaMldVlanMaxGroupExceedAction_Type.__name__=_E
_AlaMldVlanMaxGroupExceedAction_Object=MibTableColumn
alaMldVlanMaxGroupExceedAction=_AlaMldVlanMaxGroupExceedAction_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,17),_AlaMldVlanMaxGroupExceedAction_Type())
alaMldVlanMaxGroupExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanMaxGroupExceedAction.setStatus(_A)
class _AlaMldVlanSpoofAddressType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AlaMldVlanSpoofAddressType_Type.__name__=_S
_AlaMldVlanSpoofAddressType_Object=MibTableColumn
alaMldVlanSpoofAddressType=_AlaMldVlanSpoofAddressType_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,18),_AlaMldVlanSpoofAddressType_Type())
alaMldVlanSpoofAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanSpoofAddressType.setStatus(_U)
_AlaMldVlanSpoofAddress_Type=InetAddress
_AlaMldVlanSpoofAddress_Object=MibTableColumn
alaMldVlanSpoofAddress=_AlaMldVlanSpoofAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,2,1,1,19),_AlaMldVlanSpoofAddress_Type())
alaMldVlanSpoofAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldVlanSpoofAddress.setStatus(_U)
_AlaMldMember_ObjectIdentity=ObjectIdentity
alaMldMember=_AlaMldMember_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,3))
_AlaMldMemberTable_Object=MibTable
alaMldMemberTable=_AlaMldMemberTable_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,3,1))
if mibBuilder.loadTexts:alaMldMemberTable.setStatus(_A)
_AlaMldMemberEntry_Object=MibTableRow
alaMldMemberEntry=_AlaMldMemberEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,3,1,1))
alaMldMemberEntry.setIndexNames((0,_B,_V),(0,_B,_W),(0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:alaMldMemberEntry.setStatus(_A)
_AlaMldMemberVlan_Type=Unsigned32
_AlaMldMemberVlan_Object=MibTableColumn
alaMldMemberVlan=_AlaMldMemberVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,3,1,1,1),_AlaMldMemberVlan_Type())
alaMldMemberVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldMemberVlan.setStatus(_A)
_AlaMldMemberIfIndex_Type=InterfaceIndex
_AlaMldMemberIfIndex_Object=MibTableColumn
alaMldMemberIfIndex=_AlaMldMemberIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,3,1,1,2),_AlaMldMemberIfIndex_Type())
alaMldMemberIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldMemberIfIndex.setStatus(_A)
_AlaMldMemberGroupAddress_Type=InetAddressIPv6
_AlaMldMemberGroupAddress_Object=MibTableColumn
alaMldMemberGroupAddress=_AlaMldMemberGroupAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,3,1,1,3),_AlaMldMemberGroupAddress_Type())
alaMldMemberGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldMemberGroupAddress.setStatus(_A)
_AlaMldMemberSourceAddress_Type=InetAddressIPv6
_AlaMldMemberSourceAddress_Object=MibTableColumn
alaMldMemberSourceAddress=_AlaMldMemberSourceAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,3,1,1,4),_AlaMldMemberSourceAddress_Type())
alaMldMemberSourceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldMemberSourceAddress.setStatus(_A)
class _AlaMldMemberMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('include',1),('exclude',2)))
_AlaMldMemberMode_Type.__name__=_E
_AlaMldMemberMode_Object=MibTableColumn
alaMldMemberMode=_AlaMldMemberMode_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,3,1,1,5),_AlaMldMemberMode_Type())
alaMldMemberMode.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldMemberMode.setStatus(_A)
_AlaMldMemberCount_Type=Counter32
_AlaMldMemberCount_Object=MibTableColumn
alaMldMemberCount=_AlaMldMemberCount_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,3,1,1,6),_AlaMldMemberCount_Type())
alaMldMemberCount.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldMemberCount.setStatus(_A)
_AlaMldMemberTimeout_Type=TimeTicks
_AlaMldMemberTimeout_Object=MibTableColumn
alaMldMemberTimeout=_AlaMldMemberTimeout_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,3,1,1,7),_AlaMldMemberTimeout_Type())
alaMldMemberTimeout.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldMemberTimeout.setStatus(_A)
_AlaMldStaticMember_ObjectIdentity=ObjectIdentity
alaMldStaticMember=_AlaMldStaticMember_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,4))
_AlaMldStaticMemberTable_Object=MibTable
alaMldStaticMemberTable=_AlaMldStaticMemberTable_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,4,1))
if mibBuilder.loadTexts:alaMldStaticMemberTable.setStatus(_A)
_AlaMldStaticMemberEntry_Object=MibTableRow
alaMldStaticMemberEntry=_AlaMldStaticMemberEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,4,1,1))
alaMldStaticMemberEntry.setIndexNames((0,_B,_Z),(0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:alaMldStaticMemberEntry.setStatus(_A)
_AlaMldStaticMemberVlan_Type=Unsigned32
_AlaMldStaticMemberVlan_Object=MibTableColumn
alaMldStaticMemberVlan=_AlaMldStaticMemberVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,4,1,1,1),_AlaMldStaticMemberVlan_Type())
alaMldStaticMemberVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldStaticMemberVlan.setStatus(_A)
_AlaMldStaticMemberIfIndex_Type=InterfaceIndex
_AlaMldStaticMemberIfIndex_Object=MibTableColumn
alaMldStaticMemberIfIndex=_AlaMldStaticMemberIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,4,1,1,2),_AlaMldStaticMemberIfIndex_Type())
alaMldStaticMemberIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldStaticMemberIfIndex.setStatus(_A)
_AlaMldStaticMemberGroupAddress_Type=InetAddressIPv6
_AlaMldStaticMemberGroupAddress_Object=MibTableColumn
alaMldStaticMemberGroupAddress=_AlaMldStaticMemberGroupAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,4,1,1,3),_AlaMldStaticMemberGroupAddress_Type())
alaMldStaticMemberGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldStaticMemberGroupAddress.setStatus(_A)
_AlaMldStaticMemberRowStatus_Type=RowStatus
_AlaMldStaticMemberRowStatus_Object=MibTableColumn
alaMldStaticMemberRowStatus=_AlaMldStaticMemberRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,4,1,1,4),_AlaMldStaticMemberRowStatus_Type())
alaMldStaticMemberRowStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:alaMldStaticMemberRowStatus.setStatus(_A)
_AlaMldNeighbor_ObjectIdentity=ObjectIdentity
alaMldNeighbor=_AlaMldNeighbor_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,5))
_AlaMldNeighborTable_Object=MibTable
alaMldNeighborTable=_AlaMldNeighborTable_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,5,1))
if mibBuilder.loadTexts:alaMldNeighborTable.setStatus(_A)
_AlaMldNeighborEntry_Object=MibTableRow
alaMldNeighborEntry=_AlaMldNeighborEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,5,1,1))
alaMldNeighborEntry.setIndexNames((0,_B,_c),(0,_B,_d),(0,_B,_e))
if mibBuilder.loadTexts:alaMldNeighborEntry.setStatus(_A)
_AlaMldNeighborVlan_Type=Unsigned32
_AlaMldNeighborVlan_Object=MibTableColumn
alaMldNeighborVlan=_AlaMldNeighborVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,5,1,1,1),_AlaMldNeighborVlan_Type())
alaMldNeighborVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldNeighborVlan.setStatus(_A)
_AlaMldNeighborIfIndex_Type=InterfaceIndex
_AlaMldNeighborIfIndex_Object=MibTableColumn
alaMldNeighborIfIndex=_AlaMldNeighborIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,5,1,1,2),_AlaMldNeighborIfIndex_Type())
alaMldNeighborIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldNeighborIfIndex.setStatus(_A)
_AlaMldNeighborHostAddress_Type=InetAddressIPv6
_AlaMldNeighborHostAddress_Object=MibTableColumn
alaMldNeighborHostAddress=_AlaMldNeighborHostAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,5,1,1,3),_AlaMldNeighborHostAddress_Type())
alaMldNeighborHostAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldNeighborHostAddress.setStatus(_A)
_AlaMldNeighborCount_Type=Counter32
_AlaMldNeighborCount_Object=MibTableColumn
alaMldNeighborCount=_AlaMldNeighborCount_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,5,1,1,4),_AlaMldNeighborCount_Type())
alaMldNeighborCount.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldNeighborCount.setStatus(_A)
_AlaMldNeighborTimeout_Type=TimeTicks
_AlaMldNeighborTimeout_Object=MibTableColumn
alaMldNeighborTimeout=_AlaMldNeighborTimeout_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,5,1,1,5),_AlaMldNeighborTimeout_Type())
alaMldNeighborTimeout.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldNeighborTimeout.setStatus(_A)
_AlaMldStaticNeighbor_ObjectIdentity=ObjectIdentity
alaMldStaticNeighbor=_AlaMldStaticNeighbor_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,6))
_AlaMldStaticNeighborTable_Object=MibTable
alaMldStaticNeighborTable=_AlaMldStaticNeighborTable_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,6,1))
if mibBuilder.loadTexts:alaMldStaticNeighborTable.setStatus(_A)
_AlaMldStaticNeighborEntry_Object=MibTableRow
alaMldStaticNeighborEntry=_AlaMldStaticNeighborEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,6,1,1))
alaMldStaticNeighborEntry.setIndexNames((0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:alaMldStaticNeighborEntry.setStatus(_A)
_AlaMldStaticNeighborVlan_Type=Unsigned32
_AlaMldStaticNeighborVlan_Object=MibTableColumn
alaMldStaticNeighborVlan=_AlaMldStaticNeighborVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,6,1,1,1),_AlaMldStaticNeighborVlan_Type())
alaMldStaticNeighborVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldStaticNeighborVlan.setStatus(_A)
_AlaMldStaticNeighborIfIndex_Type=InterfaceIndex
_AlaMldStaticNeighborIfIndex_Object=MibTableColumn
alaMldStaticNeighborIfIndex=_AlaMldStaticNeighborIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,6,1,1,2),_AlaMldStaticNeighborIfIndex_Type())
alaMldStaticNeighborIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldStaticNeighborIfIndex.setStatus(_A)
_AlaMldStaticNeighborRowStatus_Type=RowStatus
_AlaMldStaticNeighborRowStatus_Object=MibTableColumn
alaMldStaticNeighborRowStatus=_AlaMldStaticNeighborRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,6,1,1,3),_AlaMldStaticNeighborRowStatus_Type())
alaMldStaticNeighborRowStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:alaMldStaticNeighborRowStatus.setStatus(_A)
_AlaMldQuerier_ObjectIdentity=ObjectIdentity
alaMldQuerier=_AlaMldQuerier_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,7))
_AlaMldQuerierTable_Object=MibTable
alaMldQuerierTable=_AlaMldQuerierTable_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,7,1))
if mibBuilder.loadTexts:alaMldQuerierTable.setStatus(_A)
_AlaMldQuerierEntry_Object=MibTableRow
alaMldQuerierEntry=_AlaMldQuerierEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,7,1,1))
alaMldQuerierEntry.setIndexNames((0,_B,_h),(0,_B,_i),(0,_B,_j))
if mibBuilder.loadTexts:alaMldQuerierEntry.setStatus(_A)
_AlaMldQuerierVlan_Type=Unsigned32
_AlaMldQuerierVlan_Object=MibTableColumn
alaMldQuerierVlan=_AlaMldQuerierVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,7,1,1,1),_AlaMldQuerierVlan_Type())
alaMldQuerierVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldQuerierVlan.setStatus(_A)
_AlaMldQuerierIfIndex_Type=InterfaceIndex
_AlaMldQuerierIfIndex_Object=MibTableColumn
alaMldQuerierIfIndex=_AlaMldQuerierIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,7,1,1,2),_AlaMldQuerierIfIndex_Type())
alaMldQuerierIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldQuerierIfIndex.setStatus(_A)
_AlaMldQuerierHostAddress_Type=InetAddressIPv6
_AlaMldQuerierHostAddress_Object=MibTableColumn
alaMldQuerierHostAddress=_AlaMldQuerierHostAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,7,1,1,3),_AlaMldQuerierHostAddress_Type())
alaMldQuerierHostAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldQuerierHostAddress.setStatus(_A)
_AlaMldQuerierCount_Type=Counter32
_AlaMldQuerierCount_Object=MibTableColumn
alaMldQuerierCount=_AlaMldQuerierCount_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,7,1,1,4),_AlaMldQuerierCount_Type())
alaMldQuerierCount.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldQuerierCount.setStatus(_A)
_AlaMldQuerierTimeout_Type=TimeTicks
_AlaMldQuerierTimeout_Object=MibTableColumn
alaMldQuerierTimeout=_AlaMldQuerierTimeout_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,7,1,1,5),_AlaMldQuerierTimeout_Type())
alaMldQuerierTimeout.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldQuerierTimeout.setStatus(_A)
_AlaMldStaticQuerier_ObjectIdentity=ObjectIdentity
alaMldStaticQuerier=_AlaMldStaticQuerier_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,8))
_AlaMldStaticQuerierTable_Object=MibTable
alaMldStaticQuerierTable=_AlaMldStaticQuerierTable_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,8,1))
if mibBuilder.loadTexts:alaMldStaticQuerierTable.setStatus(_A)
_AlaMldStaticQuerierEntry_Object=MibTableRow
alaMldStaticQuerierEntry=_AlaMldStaticQuerierEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,8,1,1))
alaMldStaticQuerierEntry.setIndexNames((0,_B,_k),(0,_B,_l))
if mibBuilder.loadTexts:alaMldStaticQuerierEntry.setStatus(_A)
_AlaMldStaticQuerierVlan_Type=Unsigned32
_AlaMldStaticQuerierVlan_Object=MibTableColumn
alaMldStaticQuerierVlan=_AlaMldStaticQuerierVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,8,1,1,1),_AlaMldStaticQuerierVlan_Type())
alaMldStaticQuerierVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldStaticQuerierVlan.setStatus(_A)
_AlaMldStaticQuerierIfIndex_Type=InterfaceIndex
_AlaMldStaticQuerierIfIndex_Object=MibTableColumn
alaMldStaticQuerierIfIndex=_AlaMldStaticQuerierIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,8,1,1,2),_AlaMldStaticQuerierIfIndex_Type())
alaMldStaticQuerierIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldStaticQuerierIfIndex.setStatus(_A)
_AlaMldStaticQuerierRowStatus_Type=RowStatus
_AlaMldStaticQuerierRowStatus_Object=MibTableColumn
alaMldStaticQuerierRowStatus=_AlaMldStaticQuerierRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,8,1,1,3),_AlaMldStaticQuerierRowStatus_Type())
alaMldStaticQuerierRowStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:alaMldStaticQuerierRowStatus.setStatus(_A)
_AlaMldSource_ObjectIdentity=ObjectIdentity
alaMldSource=_AlaMldSource_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,9))
_AlaMldSourceTable_Object=MibTable
alaMldSourceTable=_AlaMldSourceTable_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,9,1))
if mibBuilder.loadTexts:alaMldSourceTable.setStatus(_A)
_AlaMldSourceEntry_Object=MibTableRow
alaMldSourceEntry=_AlaMldSourceEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,9,1,1))
alaMldSourceEntry.setIndexNames((0,_B,_m),(0,_B,_n),(0,_B,_o),(0,_B,_p),(0,_B,_q))
if mibBuilder.loadTexts:alaMldSourceEntry.setStatus(_A)
_AlaMldSourceVlan_Type=Unsigned32
_AlaMldSourceVlan_Object=MibTableColumn
alaMldSourceVlan=_AlaMldSourceVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,9,1,1,1),_AlaMldSourceVlan_Type())
alaMldSourceVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldSourceVlan.setStatus(_A)
_AlaMldSourceIfIndex_Type=InterfaceIndex
_AlaMldSourceIfIndex_Object=MibTableColumn
alaMldSourceIfIndex=_AlaMldSourceIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,9,1,1,2),_AlaMldSourceIfIndex_Type())
alaMldSourceIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldSourceIfIndex.setStatus(_A)
_AlaMldSourceGroupAddress_Type=InetAddressIPv6
_AlaMldSourceGroupAddress_Object=MibTableColumn
alaMldSourceGroupAddress=_AlaMldSourceGroupAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,9,1,1,3),_AlaMldSourceGroupAddress_Type())
alaMldSourceGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldSourceGroupAddress.setStatus(_A)
_AlaMldSourceHostAddress_Type=InetAddressIPv6
_AlaMldSourceHostAddress_Object=MibTableColumn
alaMldSourceHostAddress=_AlaMldSourceHostAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,9,1,1,4),_AlaMldSourceHostAddress_Type())
alaMldSourceHostAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldSourceHostAddress.setStatus(_A)
_AlaMldSourceDestAddress_Type=InetAddressIPv6
_AlaMldSourceDestAddress_Object=MibTableColumn
alaMldSourceDestAddress=_AlaMldSourceDestAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,9,1,1,5),_AlaMldSourceDestAddress_Type())
alaMldSourceDestAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldSourceDestAddress.setStatus(_A)
_AlaMldSourceOrigAddress_Type=InetAddressIPv6
_AlaMldSourceOrigAddress_Object=MibTableColumn
alaMldSourceOrigAddress=_AlaMldSourceOrigAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,9,1,1,6),_AlaMldSourceOrigAddress_Type())
alaMldSourceOrigAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldSourceOrigAddress.setStatus(_A)
class _AlaMldSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AlaMldSourceType_Type.__name__=_E
_AlaMldSourceType_Object=MibTableColumn
alaMldSourceType=_AlaMldSourceType_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,9,1,1,7),_AlaMldSourceType_Type())
alaMldSourceType.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldSourceType.setStatus(_A)
_AlaMldForward_ObjectIdentity=ObjectIdentity
alaMldForward=_AlaMldForward_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,10))
_AlaMldForwardTable_Object=MibTable
alaMldForwardTable=_AlaMldForwardTable_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,10,1))
if mibBuilder.loadTexts:alaMldForwardTable.setStatus(_A)
_AlaMldForwardEntry_Object=MibTableRow
alaMldForwardEntry=_AlaMldForwardEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,10,1,1))
alaMldForwardEntry.setIndexNames((0,_B,_r),(0,_B,_s),(0,_B,_t),(0,_B,_u),(0,_B,_v),(0,_B,_w),(0,_B,_x))
if mibBuilder.loadTexts:alaMldForwardEntry.setStatus(_A)
_AlaMldForwardVlan_Type=Unsigned32
_AlaMldForwardVlan_Object=MibTableColumn
alaMldForwardVlan=_AlaMldForwardVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,10,1,1,1),_AlaMldForwardVlan_Type())
alaMldForwardVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldForwardVlan.setStatus(_A)
_AlaMldForwardIfIndex_Type=InterfaceIndex
_AlaMldForwardIfIndex_Object=MibTableColumn
alaMldForwardIfIndex=_AlaMldForwardIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,10,1,1,2),_AlaMldForwardIfIndex_Type())
alaMldForwardIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldForwardIfIndex.setStatus(_A)
_AlaMldForwardGroupAddress_Type=InetAddressIPv6
_AlaMldForwardGroupAddress_Object=MibTableColumn
alaMldForwardGroupAddress=_AlaMldForwardGroupAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,10,1,1,3),_AlaMldForwardGroupAddress_Type())
alaMldForwardGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldForwardGroupAddress.setStatus(_A)
_AlaMldForwardHostAddress_Type=InetAddressIPv6
_AlaMldForwardHostAddress_Object=MibTableColumn
alaMldForwardHostAddress=_AlaMldForwardHostAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,10,1,1,4),_AlaMldForwardHostAddress_Type())
alaMldForwardHostAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldForwardHostAddress.setStatus(_A)
_AlaMldForwardDestAddress_Type=InetAddressIPv6
_AlaMldForwardDestAddress_Object=MibTableColumn
alaMldForwardDestAddress=_AlaMldForwardDestAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,10,1,1,5),_AlaMldForwardDestAddress_Type())
alaMldForwardDestAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldForwardDestAddress.setStatus(_A)
_AlaMldForwardOrigAddress_Type=InetAddressIPv6
_AlaMldForwardOrigAddress_Object=MibTableColumn
alaMldForwardOrigAddress=_AlaMldForwardOrigAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,10,1,1,6),_AlaMldForwardOrigAddress_Type())
alaMldForwardOrigAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldForwardOrigAddress.setStatus(_A)
class _AlaMldForwardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AlaMldForwardType_Type.__name__=_E
_AlaMldForwardType_Object=MibTableColumn
alaMldForwardType=_AlaMldForwardType_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,10,1,1,7),_AlaMldForwardType_Type())
alaMldForwardType.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldForwardType.setStatus(_A)
_AlaMldForwardNextVlan_Type=Unsigned32
_AlaMldForwardNextVlan_Object=MibTableColumn
alaMldForwardNextVlan=_AlaMldForwardNextVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,10,1,1,8),_AlaMldForwardNextVlan_Type())
alaMldForwardNextVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldForwardNextVlan.setStatus(_A)
_AlaMldForwardNextIfIndex_Type=InterfaceIndex
_AlaMldForwardNextIfIndex_Object=MibTableColumn
alaMldForwardNextIfIndex=_AlaMldForwardNextIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,10,1,1,9),_AlaMldForwardNextIfIndex_Type())
alaMldForwardNextIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldForwardNextIfIndex.setStatus(_A)
class _AlaMldForwardNextType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AlaMldForwardNextType_Type.__name__=_E
_AlaMldForwardNextType_Object=MibTableColumn
alaMldForwardNextType=_AlaMldForwardNextType_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,10,1,1,10),_AlaMldForwardNextType_Type())
alaMldForwardNextType.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldForwardNextType.setStatus(_A)
_AlaMldTunnel_ObjectIdentity=ObjectIdentity
alaMldTunnel=_AlaMldTunnel_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,11))
_AlaMldTunnelTable_Object=MibTable
alaMldTunnelTable=_AlaMldTunnelTable_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,11,1))
if mibBuilder.loadTexts:alaMldTunnelTable.setStatus(_A)
_AlaMldTunnelEntry_Object=MibTableRow
alaMldTunnelEntry=_AlaMldTunnelEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,11,1,1))
alaMldTunnelEntry.setIndexNames((0,_B,_y),(0,_B,_z),(0,_B,_A0),(0,_B,_A1),(0,_B,_A2),(0,_B,_A3))
if mibBuilder.loadTexts:alaMldTunnelEntry.setStatus(_A)
_AlaMldTunnelVlan_Type=Unsigned32
_AlaMldTunnelVlan_Object=MibTableColumn
alaMldTunnelVlan=_AlaMldTunnelVlan_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,11,1,1,1),_AlaMldTunnelVlan_Type())
alaMldTunnelVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldTunnelVlan.setStatus(_A)
_AlaMldTunnelIfIndex_Type=InterfaceIndex
_AlaMldTunnelIfIndex_Object=MibTableColumn
alaMldTunnelIfIndex=_AlaMldTunnelIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,11,1,1,2),_AlaMldTunnelIfIndex_Type())
alaMldTunnelIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldTunnelIfIndex.setStatus(_A)
_AlaMldTunnelGroupAddress_Type=InetAddressIPv6
_AlaMldTunnelGroupAddress_Object=MibTableColumn
alaMldTunnelGroupAddress=_AlaMldTunnelGroupAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,11,1,1,3),_AlaMldTunnelGroupAddress_Type())
alaMldTunnelGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldTunnelGroupAddress.setStatus(_A)
_AlaMldTunnelHostAddress_Type=InetAddressIPv6
_AlaMldTunnelHostAddress_Object=MibTableColumn
alaMldTunnelHostAddress=_AlaMldTunnelHostAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,11,1,1,4),_AlaMldTunnelHostAddress_Type())
alaMldTunnelHostAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldTunnelHostAddress.setStatus(_A)
_AlaMldTunnelDestAddress_Type=InetAddressIPv6
_AlaMldTunnelDestAddress_Object=MibTableColumn
alaMldTunnelDestAddress=_AlaMldTunnelDestAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,11,1,1,5),_AlaMldTunnelDestAddress_Type())
alaMldTunnelDestAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldTunnelDestAddress.setStatus(_A)
_AlaMldTunnelOrigAddress_Type=InetAddressIPv6
_AlaMldTunnelOrigAddress_Object=MibTableColumn
alaMldTunnelOrigAddress=_AlaMldTunnelOrigAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,11,1,1,6),_AlaMldTunnelOrigAddress_Type())
alaMldTunnelOrigAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldTunnelOrigAddress.setStatus(_A)
class _AlaMldTunnelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AlaMldTunnelType_Type.__name__=_E
_AlaMldTunnelType_Object=MibTableColumn
alaMldTunnelType=_AlaMldTunnelType_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,11,1,1,7),_AlaMldTunnelType_Type())
alaMldTunnelType.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldTunnelType.setStatus(_A)
_AlaMldTunnelNextDestAddress_Type=InetAddressIPv6
_AlaMldTunnelNextDestAddress_Object=MibTableColumn
alaMldTunnelNextDestAddress=_AlaMldTunnelNextDestAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,11,1,1,8),_AlaMldTunnelNextDestAddress_Type())
alaMldTunnelNextDestAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldTunnelNextDestAddress.setStatus(_A)
class _AlaMldTunnelNextType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AlaMldTunnelNextType_Type.__name__=_E
_AlaMldTunnelNextType_Object=MibTableColumn
alaMldTunnelNextType=_AlaMldTunnelNextType_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,11,1,1,9),_AlaMldTunnelNextType_Type())
alaMldTunnelNextType.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldTunnelNextType.setStatus(_A)
_AlaMldPort_ObjectIdentity=ObjectIdentity
alaMldPort=_AlaMldPort_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,12))
_AlaMldPortTable_Object=MibTable
alaMldPortTable=_AlaMldPortTable_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,12,1))
if mibBuilder.loadTexts:alaMldPortTable.setStatus(_A)
_AlaMldPortEntry_Object=MibTableRow
alaMldPortEntry=_AlaMldPortEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,12,1,1))
alaMldPortEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:alaMldPortEntry.setStatus(_A)
_AlaMldPortIfIndex_Type=InterfaceIndex
_AlaMldPortIfIndex_Object=MibTableColumn
alaMldPortIfIndex=_AlaMldPortIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,12,1,1,1),_AlaMldPortIfIndex_Type())
alaMldPortIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldPortIfIndex.setStatus(_A)
class _AlaMldPortMaxGroupLimit_Type(Unsigned32):defaultValue=0
_AlaMldPortMaxGroupLimit_Type.__name__=_J
_AlaMldPortMaxGroupLimit_Object=MibTableColumn
alaMldPortMaxGroupLimit=_AlaMldPortMaxGroupLimit_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,12,1,1,2),_AlaMldPortMaxGroupLimit_Type())
alaMldPortMaxGroupLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldPortMaxGroupLimit.setStatus(_A)
class _AlaMldPortMaxGroupExceedAction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_O,1),(_P,2)))
_AlaMldPortMaxGroupExceedAction_Type.__name__=_E
_AlaMldPortMaxGroupExceedAction_Object=MibTableColumn
alaMldPortMaxGroupExceedAction=_AlaMldPortMaxGroupExceedAction_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,12,1,1,3),_AlaMldPortMaxGroupExceedAction_Type())
alaMldPortMaxGroupExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMldPortMaxGroupExceedAction.setStatus(_A)
_AlaMldPortVlan_ObjectIdentity=ObjectIdentity
alaMldPortVlan=_AlaMldPortVlan_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,13))
_AlaMldPortVlanTable_Object=MibTable
alaMldPortVlanTable=_AlaMldPortVlanTable_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,13,1))
if mibBuilder.loadTexts:alaMldPortVlanTable.setStatus(_A)
_AlaMldPortVlanEntry_Object=MibTableRow
alaMldPortVlanEntry=_AlaMldPortVlanEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,13,1,1))
alaMldPortVlanEntry.setIndexNames((0,_B,_R),(0,_B,_A4))
if mibBuilder.loadTexts:alaMldPortVlanEntry.setStatus(_A)
_AlaMldVlanId_Type=Unsigned32
_AlaMldVlanId_Object=MibTableColumn
alaMldVlanId=_AlaMldVlanId_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,13,1,1,1),_AlaMldVlanId_Type())
alaMldVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMldVlanId.setStatus(_A)
_AlaMldPortVlanCurrentGroupCount_Type=Unsigned32
_AlaMldPortVlanCurrentGroupCount_Object=MibTableColumn
alaMldPortVlanCurrentGroupCount=_AlaMldPortVlanCurrentGroupCount_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,13,1,1,2),_AlaMldPortVlanCurrentGroupCount_Type())
alaMldPortVlanCurrentGroupCount.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldPortVlanCurrentGroupCount.setStatus(_A)
_AlaMldPortVlanMaxGroupLimit_Type=Unsigned32
_AlaMldPortVlanMaxGroupLimit_Object=MibTableColumn
alaMldPortVlanMaxGroupLimit=_AlaMldPortVlanMaxGroupLimit_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,13,1,1,3),_AlaMldPortVlanMaxGroupLimit_Type())
alaMldPortVlanMaxGroupLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldPortVlanMaxGroupLimit.setStatus(_A)
class _AlaMldPortVlanMaxGroupExceedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_O,1),(_P,2)))
_AlaMldPortVlanMaxGroupExceedAction_Type.__name__=_E
_AlaMldPortVlanMaxGroupExceedAction_Object=MibTableColumn
alaMldPortVlanMaxGroupExceedAction=_AlaMldPortVlanMaxGroupExceedAction_Object((1,3,6,1,4,1,6486,800,1,2,1,35,1,1,13,1,1,4),_AlaMldPortVlanMaxGroupExceedAction_Type())
alaMldPortVlanMaxGroupExceedAction.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMldPortVlanMaxGroupExceedAction.setStatus(_A)
_AlcatelIND1MldMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1MldMIBConformance=_AlcatelIND1MldMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,2))
_AlcatelIND1MldMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1MldMIBCompliances=_AlcatelIND1MldMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,1))
_AlcatelIND1MldMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1MldMIBGroups=_AlcatelIND1MldMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,2))
alaMldGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,2,1))
alaMldGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:alaMldGroup.setStatus(_A)
alaMldVlanGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,2,2))
alaMldVlanGroup.setObjects(*((_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae)))
if mibBuilder.loadTexts:alaMldVlanGroup.setStatus(_A)
alaMldMemberGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,2,3))
alaMldMemberGroup.setObjects(*((_B,_Af),(_B,_Ag),(_B,_Ah)))
if mibBuilder.loadTexts:alaMldMemberGroup.setStatus(_A)
alaMldStaticMemberGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,2,4))
alaMldStaticMemberGroup.setObjects((_B,_Ai))
if mibBuilder.loadTexts:alaMldStaticMemberGroup.setStatus(_A)
alaMldNeighborGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,2,5))
alaMldNeighborGroup.setObjects(*((_B,_Aj),(_B,_Ak)))
if mibBuilder.loadTexts:alaMldNeighborGroup.setStatus(_A)
alaMldStaticNeighborGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,2,6))
alaMldStaticNeighborGroup.setObjects((_B,_Al))
if mibBuilder.loadTexts:alaMldStaticNeighborGroup.setStatus(_A)
alaMldQuerierGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,2,7))
alaMldQuerierGroup.setObjects(*((_B,_Am),(_B,_An)))
if mibBuilder.loadTexts:alaMldQuerierGroup.setStatus(_A)
alaMldStaticQuerierGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,2,8))
alaMldStaticQuerierGroup.setObjects((_B,_Ao))
if mibBuilder.loadTexts:alaMldStaticQuerierGroup.setStatus(_A)
alaMldSourceGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,2,9))
alaMldSourceGroup.setObjects(*((_B,_Ap),(_B,_Aq)))
if mibBuilder.loadTexts:alaMldSourceGroup.setStatus(_A)
alaMldForwardGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,2,10))
alaMldForwardGroup.setObjects(*((_B,_Ar),(_B,_As),(_B,_At)))
if mibBuilder.loadTexts:alaMldForwardGroup.setStatus(_A)
alaMldTunnelGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,2,11))
alaMldTunnelGroup.setObjects(*((_B,_Au),(_B,_Av),(_B,_Aw)))
if mibBuilder.loadTexts:alaMldTunnelGroup.setStatus(_A)
alaMldPortGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,2,12))
alaMldPortGroup.setObjects(*((_B,_Ax),(_B,_Ay)))
if mibBuilder.loadTexts:alaMldPortGroup.setStatus(_A)
alaMldPortVlanGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,2,13))
alaMldPortVlanGroup.setObjects(*((_B,_Az),(_B,_A_),(_B,_B0)))
if mibBuilder.loadTexts:alaMldPortVlanGroup.setStatus(_A)
alaMldCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,35,1,2,1,1))
alaMldCompliance.setObjects(*((_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB),(_B,_BC),(_B,_BD)))
if mibBuilder.loadTexts:alaMldCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1MldMIB':alcatelIND1MldMIB,'alcatelIND1MldMIBObjects':alcatelIND1MldMIBObjects,'alaMld':alaMld,_A5:alaMldStatus,_A6:alaMldQuerying,_A7:alaMldSpoofing,_A8:alaMldZapping,_A9:alaMldVersion,_AA:alaMldRobustness,_AB:alaMldQueryInterval,_AC:alaMldQueryResponseInterval,_AD:alaMldLastMemberQueryInterval,_AE:alaMldRouterTimeout,_AF:alaMldSourceTimeout,_AG:alaMldProxying,_AH:alaMldUnsolicitedReportInterval,_AI:alaMldQuerierForwarding,_AJ:alaMldMaxGroupLimit,_AK:alaMldMaxGroupExceedAction,_AL:alaMldFloodUnknown,_AM:alaMldBufferPacket,'alaMldVlan':alaMldVlan,'alaMldVlanTable':alaMldVlanTable,'alaMldVlanEntry':alaMldVlanEntry,_T:alaMldVlanIndex,_AN:alaMldVlanStatus,_AO:alaMldVlanQuerying,_AP:alaMldVlanSpoofing,_AQ:alaMldVlanZapping,_AR:alaMldVlanVersion,_AS:alaMldVlanRobustness,_AT:alaMldVlanQueryInterval,_AU:alaMldVlanQueryResponseInterval,_AV:alaMldVlanLastMemberQueryInterval,_AW:alaMldVlanRouterTimeout,_AX:alaMldVlanSourceTimeout,_AY:alaMldVlanProxying,_AZ:alaMldVlanUnsolicitedReportInterval,_Aa:alaMldVlanQuerierForwarding,_Ab:alaMldVlanMaxGroupLimit,_Ac:alaMldVlanMaxGroupExceedAction,_Ad:alaMldVlanSpoofAddressType,_Ae:alaMldVlanSpoofAddress,'alaMldMember':alaMldMember,'alaMldMemberTable':alaMldMemberTable,'alaMldMemberEntry':alaMldMemberEntry,_V:alaMldMemberVlan,_W:alaMldMemberIfIndex,_X:alaMldMemberGroupAddress,_Y:alaMldMemberSourceAddress,_Af:alaMldMemberMode,_Ag:alaMldMemberCount,_Ah:alaMldMemberTimeout,'alaMldStaticMember':alaMldStaticMember,'alaMldStaticMemberTable':alaMldStaticMemberTable,'alaMldStaticMemberEntry':alaMldStaticMemberEntry,_Z:alaMldStaticMemberVlan,_a:alaMldStaticMemberIfIndex,_b:alaMldStaticMemberGroupAddress,_Ai:alaMldStaticMemberRowStatus,'alaMldNeighbor':alaMldNeighbor,'alaMldNeighborTable':alaMldNeighborTable,'alaMldNeighborEntry':alaMldNeighborEntry,_c:alaMldNeighborVlan,_d:alaMldNeighborIfIndex,_e:alaMldNeighborHostAddress,_Aj:alaMldNeighborCount,_Ak:alaMldNeighborTimeout,'alaMldStaticNeighbor':alaMldStaticNeighbor,'alaMldStaticNeighborTable':alaMldStaticNeighborTable,'alaMldStaticNeighborEntry':alaMldStaticNeighborEntry,_f:alaMldStaticNeighborVlan,_g:alaMldStaticNeighborIfIndex,_Al:alaMldStaticNeighborRowStatus,'alaMldQuerier':alaMldQuerier,'alaMldQuerierTable':alaMldQuerierTable,'alaMldQuerierEntry':alaMldQuerierEntry,_h:alaMldQuerierVlan,_i:alaMldQuerierIfIndex,_j:alaMldQuerierHostAddress,_Am:alaMldQuerierCount,_An:alaMldQuerierTimeout,'alaMldStaticQuerier':alaMldStaticQuerier,'alaMldStaticQuerierTable':alaMldStaticQuerierTable,'alaMldStaticQuerierEntry':alaMldStaticQuerierEntry,_k:alaMldStaticQuerierVlan,_l:alaMldStaticQuerierIfIndex,_Ao:alaMldStaticQuerierRowStatus,'alaMldSource':alaMldSource,'alaMldSourceTable':alaMldSourceTable,'alaMldSourceEntry':alaMldSourceEntry,_m:alaMldSourceVlan,_Ap:alaMldSourceIfIndex,_n:alaMldSourceGroupAddress,_o:alaMldSourceHostAddress,_p:alaMldSourceDestAddress,_q:alaMldSourceOrigAddress,_Aq:alaMldSourceType,'alaMldForward':alaMldForward,'alaMldForwardTable':alaMldForwardTable,'alaMldForwardEntry':alaMldForwardEntry,_r:alaMldForwardVlan,_Ar:alaMldForwardIfIndex,_s:alaMldForwardGroupAddress,_t:alaMldForwardHostAddress,_u:alaMldForwardDestAddress,_v:alaMldForwardOrigAddress,_As:alaMldForwardType,_w:alaMldForwardNextVlan,_x:alaMldForwardNextIfIndex,_At:alaMldForwardNextType,'alaMldTunnel':alaMldTunnel,'alaMldTunnelTable':alaMldTunnelTable,'alaMldTunnelEntry':alaMldTunnelEntry,_y:alaMldTunnelVlan,_Au:alaMldTunnelIfIndex,_z:alaMldTunnelGroupAddress,_A0:alaMldTunnelHostAddress,_A1:alaMldTunnelDestAddress,_A2:alaMldTunnelOrigAddress,_Av:alaMldTunnelType,_A3:alaMldTunnelNextDestAddress,_Aw:alaMldTunnelNextType,'alaMldPort':alaMldPort,'alaMldPortTable':alaMldPortTable,'alaMldPortEntry':alaMldPortEntry,_R:alaMldPortIfIndex,_Ax:alaMldPortMaxGroupLimit,_Ay:alaMldPortMaxGroupExceedAction,'alaMldPortVlan':alaMldPortVlan,'alaMldPortVlanTable':alaMldPortVlanTable,'alaMldPortVlanEntry':alaMldPortVlanEntry,_A4:alaMldVlanId,_Az:alaMldPortVlanCurrentGroupCount,_A_:alaMldPortVlanMaxGroupLimit,_B0:alaMldPortVlanMaxGroupExceedAction,'alcatelIND1MldMIBConformance':alcatelIND1MldMIBConformance,'alcatelIND1MldMIBCompliances':alcatelIND1MldMIBCompliances,'alaMldCompliance':alaMldCompliance,'alcatelIND1MldMIBGroups':alcatelIND1MldMIBGroups,_B1:alaMldGroup,_B2:alaMldVlanGroup,_B3:alaMldMemberGroup,_B4:alaMldStaticMemberGroup,_B5:alaMldNeighborGroup,_B6:alaMldStaticNeighborGroup,_B7:alaMldQuerierGroup,_B8:alaMldStaticQuerierGroup,_B9:alaMldSourceGroup,_BA:alaMldForwardGroup,_BB:alaMldTunnelGroup,_BC:alaMldPortGroup,_BD:alaMldPortVlanGroup})