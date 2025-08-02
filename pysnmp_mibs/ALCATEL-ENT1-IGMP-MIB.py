_BL='alaIgmpPortVlanGroup'
_BK='alaIgmpPortGroup'
_BJ='alaIgmpTunnelGroup'
_BI='alaIgmpForwardGroup'
_BH='alaIgmpSourceGroup'
_BG='alaIgmpStaticQuerierGroup'
_BF='alaIgmpQuerierGroup'
_BE='alaIgmpStaticNeighborGroup'
_BD='alaIgmpNeighborGroup'
_BC='alaIgmpStaticMemberGroup'
_BB='alaIgmpMemberGroup'
_BA='alaIgmpVlanGroup'
_B9='alaIgmpGroup'
_B8='alaIgmpPortVlanMaxGroupExceedAction'
_B7='alaIgmpPortVlanMaxGroupLimit'
_B6='alaIgmpPortVlanCurrentGroupCount'
_B5='alaIgmpPortMaxGroupExceedAction'
_B4='alaIgmpPortMaxGroupLimit'
_B3='alaIgmpTunnelNextType'
_B2='alaIgmpTunnelType'
_B1='alaIgmpTunnelIfIndex'
_B0='alaIgmpForwardNextType'
_A_='alaIgmpForwardType'
_Az='alaIgmpForwardIfIndex'
_Ay='alaIgmpSourceType'
_Ax='alaIgmpSourceIfIndex'
_Aw='alaIgmpStaticQuerierRowStatus'
_Av='alaIgmpQuerierTimeout'
_Au='alaIgmpQuerierCount'
_At='alaIgmpStaticNeighborRowStatus'
_As='alaIgmpNeighborTimeout'
_Ar='alaIgmpNeighborCount'
_Aq='alaIgmpStaticMemberRowStatus'
_Ap='alaIgmpMemberTimeout'
_Ao='alaIgmpMemberCount'
_An='alaIgmpMemberMode'
_Am='alaIgmpVlanZeroBasedQuery'
_Al='alaIgmpVlanMaxGroupExceedAction'
_Ak='alaIgmpVlanMaxGroupLimit'
_Aj='alaIgmpVlanQuerierForwarding'
_Ai='alaIgmpVlanUnsolicitedReportInterval'
_Ah='alaIgmpVlanProxying'
_Ag='alaIgmpVlanSourceTimeout'
_Af='alaIgmpVlanRouterTimeout'
_Ae='alaIgmpVlanLastMemberQueryInterval'
_Ad='alaIgmpVlanQueryResponseInterval'
_Ac='alaIgmpVlanQueryInterval'
_Ab='alaIgmpVlanRobustness'
_Aa='alaIgmpVlanVersion'
_AZ='alaIgmpVlanZapping'
_AY='alaIgmpVlanSpoofing'
_AX='alaIgmpVlanQuerying'
_AW='alaIgmpVlanStatus'
_AV='alaIgmpInitialPacketBufferMinDelay'
_AU='alaIgmpInitialPacketBufferTimeout'
_AT='alaIgmpInitialPacketBufferMaxFlow'
_AS='alaIgmpInitialPacketBufferMaxPacket'
_AR='alaIgmpInitialPacketBuffer'
_AQ='alaIgmpZeroBasedQuery'
_AP='alaIgmpHelperAddress'
_AO='alaIgmpHelperAddressType'
_AN='alaIgmpFloodUnknown'
_AM='alaIgmpMaxGroupExceedAction'
_AL='alaIgmpMaxGroupLimit'
_AK='alaIgmpQuerierForwarding'
_AJ='alaIgmpUnsolicitedReportInterval'
_AI='alaIgmpProxying'
_AH='alaIgmpSourceTimeout'
_AG='alaIgmpRouterTimeout'
_AF='alaIgmpLastMemberQueryInterval'
_AE='alaIgmpQueryResponseInterval'
_AD='alaIgmpQueryInterval'
_AC='alaIgmpRobustness'
_AB='alaIgmpVersion'
_AA='alaIgmpZapping'
_A9='alaIgmpSpoofing'
_A8='alaIgmpQuerying'
_A7='alaIgmpStatus'
_A6='alaIgmpVlanId'
_A5='alaIgmpTunnelNextDestAddress'
_A4='alaIgmpTunnelOrigAddress'
_A3='alaIgmpTunnelDestAddress'
_A2='alaIgmpTunnelHostAddress'
_A1='alaIgmpTunnelGroupAddress'
_A0='alaIgmpTunnelVlan'
_z='alaIgmpForwardNextIfIndex'
_y='alaIgmpForwardNextVlan'
_x='alaIgmpForwardOrigAddress'
_w='alaIgmpForwardDestAddress'
_v='alaIgmpForwardHostAddress'
_u='alaIgmpForwardGroupAddress'
_t='alaIgmpForwardVlan'
_s='alaIgmpSourceOrigAddress'
_r='alaIgmpSourceDestAddress'
_q='alaIgmpSourceHostAddress'
_p='alaIgmpSourceGroupAddress'
_o='alaIgmpSourceVlan'
_n='alaIgmpStaticQuerierIfIndex'
_m='alaIgmpStaticQuerierVlan'
_l='alaIgmpQuerierHostAddress'
_k='alaIgmpQuerierIfIndex'
_j='alaIgmpQuerierVlan'
_i='alaIgmpStaticNeighborIfIndex'
_h='alaIgmpStaticNeighborVlan'
_g='alaIgmpNeighborHostAddress'
_f='alaIgmpNeighborIfIndex'
_e='alaIgmpNeighborVlan'
_d='alaIgmpStaticMemberGroupAddress'
_c='alaIgmpStaticMemberIfIndex'
_b='alaIgmpStaticMemberVlan'
_a='alaIgmpMemberSourceAddress'
_Z='alaIgmpMemberGroupAddress'
_Y='alaIgmpMemberIfIndex'
_X='alaIgmpMemberVlan'
_W='alaIgmpVlanIndex'
_V='InetAddressType'
_U='InetAddress'
_T='alaIgmpPortIfIndex'
_S='read-create'
_R='replace'
_Q='drop'
_P='tenths of seconds'
_O='ipip'
_N='pim'
_M='mcast'
_L='seconds'
_K='current'
_J='disable'
_I='enable'
_H='Unsigned32'
_G='read-only'
_F='none'
_E='Integer32'
_D='not-accessible'
_C='read-write'
_B='ALCATEL-ENT1-IGMP-MIB'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Igmp,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1Igmp')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressIPv4,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_U,'InetAddressIPv4','InetAddressPrefixLength',_V)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1IgmpMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1))
if mibBuilder.loadTexts:alcatelIND1IgmpMIB.setRevisions(('2016-02-18 00:00','2015-09-17 00:00','2013-11-26 00:00','2011-02-23 00:00','2009-03-31 00:00','2008-09-10 00:00','2008-08-08 00:00','2007-04-03 00:00'))
_AlcatelIND1IgmpMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1IgmpMIBObjects=_AlcatelIND1IgmpMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,1))
_AlaIgmp_ObjectIdentity=ObjectIdentity
alaIgmp=_AlaIgmp_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1))
class _AlaIgmpStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpStatus_Type.__name__=_E
_AlaIgmpStatus_Object=MibScalar
alaIgmpStatus=_AlaIgmpStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,1),_AlaIgmpStatus_Type())
alaIgmpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpStatus.setStatus(_A)
class _AlaIgmpQuerying_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpQuerying_Type.__name__=_E
_AlaIgmpQuerying_Object=MibScalar
alaIgmpQuerying=_AlaIgmpQuerying_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,2),_AlaIgmpQuerying_Type())
alaIgmpQuerying.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpQuerying.setStatus(_A)
class _AlaIgmpSpoofing_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpSpoofing_Type.__name__=_E
_AlaIgmpSpoofing_Object=MibScalar
alaIgmpSpoofing=_AlaIgmpSpoofing_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,3),_AlaIgmpSpoofing_Type())
alaIgmpSpoofing.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpSpoofing.setStatus(_A)
class _AlaIgmpZapping_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpZapping_Type.__name__=_E
_AlaIgmpZapping_Object=MibScalar
alaIgmpZapping=_AlaIgmpZapping_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,4),_AlaIgmpZapping_Type())
alaIgmpZapping.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpZapping.setStatus(_A)
class _AlaIgmpVersion_Type(Unsigned32):defaultValue=2
_AlaIgmpVersion_Type.__name__=_H
_AlaIgmpVersion_Object=MibScalar
alaIgmpVersion=_AlaIgmpVersion_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,5),_AlaIgmpVersion_Type())
alaIgmpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVersion.setStatus(_A)
class _AlaIgmpRobustness_Type(Unsigned32):defaultValue=2
_AlaIgmpRobustness_Type.__name__=_H
_AlaIgmpRobustness_Object=MibScalar
alaIgmpRobustness=_AlaIgmpRobustness_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,6),_AlaIgmpRobustness_Type())
alaIgmpRobustness.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpRobustness.setStatus(_A)
class _AlaIgmpQueryInterval_Type(Unsigned32):defaultValue=125
_AlaIgmpQueryInterval_Type.__name__=_H
_AlaIgmpQueryInterval_Object=MibScalar
alaIgmpQueryInterval=_AlaIgmpQueryInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,7),_AlaIgmpQueryInterval_Type())
alaIgmpQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:alaIgmpQueryInterval.setUnits(_L)
class _AlaIgmpQueryResponseInterval_Type(Unsigned32):defaultValue=100
_AlaIgmpQueryResponseInterval_Type.__name__=_H
_AlaIgmpQueryResponseInterval_Object=MibScalar
alaIgmpQueryResponseInterval=_AlaIgmpQueryResponseInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,8),_AlaIgmpQueryResponseInterval_Type())
alaIgmpQueryResponseInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpQueryResponseInterval.setStatus(_A)
if mibBuilder.loadTexts:alaIgmpQueryResponseInterval.setUnits(_P)
class _AlaIgmpLastMemberQueryInterval_Type(Unsigned32):defaultValue=10
_AlaIgmpLastMemberQueryInterval_Type.__name__=_H
_AlaIgmpLastMemberQueryInterval_Object=MibScalar
alaIgmpLastMemberQueryInterval=_AlaIgmpLastMemberQueryInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,9),_AlaIgmpLastMemberQueryInterval_Type())
alaIgmpLastMemberQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpLastMemberQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:alaIgmpLastMemberQueryInterval.setUnits(_P)
class _AlaIgmpRouterTimeout_Type(Unsigned32):defaultValue=90
_AlaIgmpRouterTimeout_Type.__name__=_H
_AlaIgmpRouterTimeout_Object=MibScalar
alaIgmpRouterTimeout=_AlaIgmpRouterTimeout_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,10),_AlaIgmpRouterTimeout_Type())
alaIgmpRouterTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpRouterTimeout.setStatus(_A)
if mibBuilder.loadTexts:alaIgmpRouterTimeout.setUnits(_L)
class _AlaIgmpSourceTimeout_Type(Unsigned32):defaultValue=30
_AlaIgmpSourceTimeout_Type.__name__=_H
_AlaIgmpSourceTimeout_Object=MibScalar
alaIgmpSourceTimeout=_AlaIgmpSourceTimeout_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,11),_AlaIgmpSourceTimeout_Type())
alaIgmpSourceTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpSourceTimeout.setStatus(_A)
if mibBuilder.loadTexts:alaIgmpSourceTimeout.setUnits(_L)
class _AlaIgmpProxying_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpProxying_Type.__name__=_E
_AlaIgmpProxying_Object=MibScalar
alaIgmpProxying=_AlaIgmpProxying_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,12),_AlaIgmpProxying_Type())
alaIgmpProxying.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpProxying.setStatus(_A)
class _AlaIgmpUnsolicitedReportInterval_Type(Unsigned32):defaultValue=1
_AlaIgmpUnsolicitedReportInterval_Type.__name__=_H
_AlaIgmpUnsolicitedReportInterval_Object=MibScalar
alaIgmpUnsolicitedReportInterval=_AlaIgmpUnsolicitedReportInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,13),_AlaIgmpUnsolicitedReportInterval_Type())
alaIgmpUnsolicitedReportInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpUnsolicitedReportInterval.setStatus(_A)
if mibBuilder.loadTexts:alaIgmpUnsolicitedReportInterval.setUnits(_L)
class _AlaIgmpQuerierForwarding_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpQuerierForwarding_Type.__name__=_E
_AlaIgmpQuerierForwarding_Object=MibScalar
alaIgmpQuerierForwarding=_AlaIgmpQuerierForwarding_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,14),_AlaIgmpQuerierForwarding_Type())
alaIgmpQuerierForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpQuerierForwarding.setStatus(_A)
class _AlaIgmpMaxGroupLimit_Type(Unsigned32):defaultValue=0
_AlaIgmpMaxGroupLimit_Type.__name__=_H
_AlaIgmpMaxGroupLimit_Object=MibScalar
alaIgmpMaxGroupLimit=_AlaIgmpMaxGroupLimit_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,15),_AlaIgmpMaxGroupLimit_Type())
alaIgmpMaxGroupLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpMaxGroupLimit.setStatus(_A)
class _AlaIgmpMaxGroupExceedAction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_Q,1),(_R,2)))
_AlaIgmpMaxGroupExceedAction_Type.__name__=_E
_AlaIgmpMaxGroupExceedAction_Object=MibScalar
alaIgmpMaxGroupExceedAction=_AlaIgmpMaxGroupExceedAction_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,16),_AlaIgmpMaxGroupExceedAction_Type())
alaIgmpMaxGroupExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpMaxGroupExceedAction.setStatus(_A)
class _AlaIgmpFloodUnknown_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpFloodUnknown_Type.__name__=_E
_AlaIgmpFloodUnknown_Object=MibScalar
alaIgmpFloodUnknown=_AlaIgmpFloodUnknown_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,17),_AlaIgmpFloodUnknown_Type())
alaIgmpFloodUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpFloodUnknown.setStatus(_A)
class _AlaIgmpHelperAddressType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AlaIgmpHelperAddressType_Type.__name__=_V
_AlaIgmpHelperAddressType_Object=MibScalar
alaIgmpHelperAddressType=_AlaIgmpHelperAddressType_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,18),_AlaIgmpHelperAddressType_Type())
alaIgmpHelperAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpHelperAddressType.setStatus(_A)
class _AlaIgmpHelperAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_AlaIgmpHelperAddress_Type.__name__=_U
_AlaIgmpHelperAddress_Object=MibScalar
alaIgmpHelperAddress=_AlaIgmpHelperAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,19),_AlaIgmpHelperAddress_Type())
alaIgmpHelperAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpHelperAddress.setStatus(_A)
class _AlaIgmpZeroBasedQuery_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpZeroBasedQuery_Type.__name__=_E
_AlaIgmpZeroBasedQuery_Object=MibScalar
alaIgmpZeroBasedQuery=_AlaIgmpZeroBasedQuery_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,20),_AlaIgmpZeroBasedQuery_Type())
alaIgmpZeroBasedQuery.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpZeroBasedQuery.setStatus(_A)
class _AlaIgmpInitialPacketBuffer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpInitialPacketBuffer_Type.__name__=_E
_AlaIgmpInitialPacketBuffer_Object=MibScalar
alaIgmpInitialPacketBuffer=_AlaIgmpInitialPacketBuffer_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,21),_AlaIgmpInitialPacketBuffer_Type())
alaIgmpInitialPacketBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpInitialPacketBuffer.setStatus(_A)
class _AlaIgmpInitialPacketBufferMaxPacket_Type(Unsigned32):defaultValue=4
_AlaIgmpInitialPacketBufferMaxPacket_Type.__name__=_H
_AlaIgmpInitialPacketBufferMaxPacket_Object=MibScalar
alaIgmpInitialPacketBufferMaxPacket=_AlaIgmpInitialPacketBufferMaxPacket_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,22),_AlaIgmpInitialPacketBufferMaxPacket_Type())
alaIgmpInitialPacketBufferMaxPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpInitialPacketBufferMaxPacket.setStatus(_A)
class _AlaIgmpInitialPacketBufferMaxFlow_Type(Unsigned32):defaultValue=32
_AlaIgmpInitialPacketBufferMaxFlow_Type.__name__=_H
_AlaIgmpInitialPacketBufferMaxFlow_Object=MibScalar
alaIgmpInitialPacketBufferMaxFlow=_AlaIgmpInitialPacketBufferMaxFlow_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,23),_AlaIgmpInitialPacketBufferMaxFlow_Type())
alaIgmpInitialPacketBufferMaxFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpInitialPacketBufferMaxFlow.setStatus(_A)
class _AlaIgmpInitialPacketBufferTimeout_Type(Unsigned32):defaultValue=10
_AlaIgmpInitialPacketBufferTimeout_Type.__name__=_H
_AlaIgmpInitialPacketBufferTimeout_Object=MibScalar
alaIgmpInitialPacketBufferTimeout=_AlaIgmpInitialPacketBufferTimeout_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,24),_AlaIgmpInitialPacketBufferTimeout_Type())
alaIgmpInitialPacketBufferTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpInitialPacketBufferTimeout.setStatus(_A)
if mibBuilder.loadTexts:alaIgmpInitialPacketBufferTimeout.setUnits(_L)
class _AlaIgmpInitialPacketBufferMinDelay_Type(Unsigned32):defaultValue=0
_AlaIgmpInitialPacketBufferMinDelay_Type.__name__=_H
_AlaIgmpInitialPacketBufferMinDelay_Object=MibScalar
alaIgmpInitialPacketBufferMinDelay=_AlaIgmpInitialPacketBufferMinDelay_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,1,25),_AlaIgmpInitialPacketBufferMinDelay_Type())
alaIgmpInitialPacketBufferMinDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpInitialPacketBufferMinDelay.setStatus(_A)
if mibBuilder.loadTexts:alaIgmpInitialPacketBufferMinDelay.setUnits('milliseconds')
_AlaIgmpVlan_ObjectIdentity=ObjectIdentity
alaIgmpVlan=_AlaIgmpVlan_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2))
_AlaIgmpVlanTable_Object=MibTable
alaIgmpVlanTable=_AlaIgmpVlanTable_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1))
if mibBuilder.loadTexts:alaIgmpVlanTable.setStatus(_A)
_AlaIgmpVlanEntry_Object=MibTableRow
alaIgmpVlanEntry=_AlaIgmpVlanEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1))
alaIgmpVlanEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:alaIgmpVlanEntry.setStatus(_A)
_AlaIgmpVlanIndex_Type=Unsigned32
_AlaIgmpVlanIndex_Object=MibTableColumn
alaIgmpVlanIndex=_AlaIgmpVlanIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,1),_AlaIgmpVlanIndex_Type())
alaIgmpVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpVlanIndex.setStatus(_A)
class _AlaIgmpVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpVlanStatus_Type.__name__=_E
_AlaIgmpVlanStatus_Object=MibTableColumn
alaIgmpVlanStatus=_AlaIgmpVlanStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,2),_AlaIgmpVlanStatus_Type())
alaIgmpVlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanStatus.setStatus(_A)
class _AlaIgmpVlanQuerying_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpVlanQuerying_Type.__name__=_E
_AlaIgmpVlanQuerying_Object=MibTableColumn
alaIgmpVlanQuerying=_AlaIgmpVlanQuerying_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,3),_AlaIgmpVlanQuerying_Type())
alaIgmpVlanQuerying.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanQuerying.setStatus(_A)
class _AlaIgmpVlanSpoofing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpVlanSpoofing_Type.__name__=_E
_AlaIgmpVlanSpoofing_Object=MibTableColumn
alaIgmpVlanSpoofing=_AlaIgmpVlanSpoofing_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,4),_AlaIgmpVlanSpoofing_Type())
alaIgmpVlanSpoofing.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanSpoofing.setStatus(_A)
class _AlaIgmpVlanZapping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpVlanZapping_Type.__name__=_E
_AlaIgmpVlanZapping_Object=MibTableColumn
alaIgmpVlanZapping=_AlaIgmpVlanZapping_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,5),_AlaIgmpVlanZapping_Type())
alaIgmpVlanZapping.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanZapping.setStatus(_A)
_AlaIgmpVlanVersion_Type=Unsigned32
_AlaIgmpVlanVersion_Object=MibTableColumn
alaIgmpVlanVersion=_AlaIgmpVlanVersion_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,6),_AlaIgmpVlanVersion_Type())
alaIgmpVlanVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanVersion.setStatus(_A)
_AlaIgmpVlanRobustness_Type=Unsigned32
_AlaIgmpVlanRobustness_Object=MibTableColumn
alaIgmpVlanRobustness=_AlaIgmpVlanRobustness_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,7),_AlaIgmpVlanRobustness_Type())
alaIgmpVlanRobustness.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanRobustness.setStatus(_A)
_AlaIgmpVlanQueryInterval_Type=Unsigned32
_AlaIgmpVlanQueryInterval_Object=MibTableColumn
alaIgmpVlanQueryInterval=_AlaIgmpVlanQueryInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,8),_AlaIgmpVlanQueryInterval_Type())
alaIgmpVlanQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:alaIgmpVlanQueryInterval.setUnits(_L)
_AlaIgmpVlanQueryResponseInterval_Type=Unsigned32
_AlaIgmpVlanQueryResponseInterval_Object=MibTableColumn
alaIgmpVlanQueryResponseInterval=_AlaIgmpVlanQueryResponseInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,9),_AlaIgmpVlanQueryResponseInterval_Type())
alaIgmpVlanQueryResponseInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanQueryResponseInterval.setStatus(_A)
if mibBuilder.loadTexts:alaIgmpVlanQueryResponseInterval.setUnits(_P)
_AlaIgmpVlanLastMemberQueryInterval_Type=Unsigned32
_AlaIgmpVlanLastMemberQueryInterval_Object=MibTableColumn
alaIgmpVlanLastMemberQueryInterval=_AlaIgmpVlanLastMemberQueryInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,10),_AlaIgmpVlanLastMemberQueryInterval_Type())
alaIgmpVlanLastMemberQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanLastMemberQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:alaIgmpVlanLastMemberQueryInterval.setUnits(_P)
_AlaIgmpVlanRouterTimeout_Type=Unsigned32
_AlaIgmpVlanRouterTimeout_Object=MibTableColumn
alaIgmpVlanRouterTimeout=_AlaIgmpVlanRouterTimeout_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,11),_AlaIgmpVlanRouterTimeout_Type())
alaIgmpVlanRouterTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanRouterTimeout.setStatus(_A)
if mibBuilder.loadTexts:alaIgmpVlanRouterTimeout.setUnits(_L)
_AlaIgmpVlanSourceTimeout_Type=Unsigned32
_AlaIgmpVlanSourceTimeout_Object=MibTableColumn
alaIgmpVlanSourceTimeout=_AlaIgmpVlanSourceTimeout_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,12),_AlaIgmpVlanSourceTimeout_Type())
alaIgmpVlanSourceTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanSourceTimeout.setStatus(_A)
if mibBuilder.loadTexts:alaIgmpVlanSourceTimeout.setUnits(_L)
class _AlaIgmpVlanProxying_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpVlanProxying_Type.__name__=_E
_AlaIgmpVlanProxying_Object=MibTableColumn
alaIgmpVlanProxying=_AlaIgmpVlanProxying_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,13),_AlaIgmpVlanProxying_Type())
alaIgmpVlanProxying.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanProxying.setStatus(_A)
_AlaIgmpVlanUnsolicitedReportInterval_Type=Unsigned32
_AlaIgmpVlanUnsolicitedReportInterval_Object=MibTableColumn
alaIgmpVlanUnsolicitedReportInterval=_AlaIgmpVlanUnsolicitedReportInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,14),_AlaIgmpVlanUnsolicitedReportInterval_Type())
alaIgmpVlanUnsolicitedReportInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanUnsolicitedReportInterval.setStatus(_A)
if mibBuilder.loadTexts:alaIgmpVlanUnsolicitedReportInterval.setUnits(_L)
class _AlaIgmpVlanQuerierForwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpVlanQuerierForwarding_Type.__name__=_E
_AlaIgmpVlanQuerierForwarding_Object=MibTableColumn
alaIgmpVlanQuerierForwarding=_AlaIgmpVlanQuerierForwarding_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,15),_AlaIgmpVlanQuerierForwarding_Type())
alaIgmpVlanQuerierForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanQuerierForwarding.setStatus(_A)
class _AlaIgmpVlanMaxGroupLimit_Type(Unsigned32):defaultValue=0
_AlaIgmpVlanMaxGroupLimit_Type.__name__=_H
_AlaIgmpVlanMaxGroupLimit_Object=MibTableColumn
alaIgmpVlanMaxGroupLimit=_AlaIgmpVlanMaxGroupLimit_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,16),_AlaIgmpVlanMaxGroupLimit_Type())
alaIgmpVlanMaxGroupLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanMaxGroupLimit.setStatus(_A)
class _AlaIgmpVlanMaxGroupExceedAction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_Q,1),(_R,2)))
_AlaIgmpVlanMaxGroupExceedAction_Type.__name__=_E
_AlaIgmpVlanMaxGroupExceedAction_Object=MibTableColumn
alaIgmpVlanMaxGroupExceedAction=_AlaIgmpVlanMaxGroupExceedAction_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,17),_AlaIgmpVlanMaxGroupExceedAction_Type())
alaIgmpVlanMaxGroupExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanMaxGroupExceedAction.setStatus(_A)
class _AlaIgmpVlanZeroBasedQuery_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),(_J,2)))
_AlaIgmpVlanZeroBasedQuery_Type.__name__=_E
_AlaIgmpVlanZeroBasedQuery_Object=MibTableColumn
alaIgmpVlanZeroBasedQuery=_AlaIgmpVlanZeroBasedQuery_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,2,1,1,18),_AlaIgmpVlanZeroBasedQuery_Type())
alaIgmpVlanZeroBasedQuery.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpVlanZeroBasedQuery.setStatus(_A)
_AlaIgmpMember_ObjectIdentity=ObjectIdentity
alaIgmpMember=_AlaIgmpMember_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,3))
_AlaIgmpMemberTable_Object=MibTable
alaIgmpMemberTable=_AlaIgmpMemberTable_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,3,1))
if mibBuilder.loadTexts:alaIgmpMemberTable.setStatus(_A)
_AlaIgmpMemberEntry_Object=MibTableRow
alaIgmpMemberEntry=_AlaIgmpMemberEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,3,1,1))
alaIgmpMemberEntry.setIndexNames((0,_B,_X),(0,_B,_Y),(0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:alaIgmpMemberEntry.setStatus(_A)
_AlaIgmpMemberVlan_Type=Unsigned32
_AlaIgmpMemberVlan_Object=MibTableColumn
alaIgmpMemberVlan=_AlaIgmpMemberVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,3,1,1,1),_AlaIgmpMemberVlan_Type())
alaIgmpMemberVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpMemberVlan.setStatus(_A)
_AlaIgmpMemberIfIndex_Type=InterfaceIndex
_AlaIgmpMemberIfIndex_Object=MibTableColumn
alaIgmpMemberIfIndex=_AlaIgmpMemberIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,3,1,1,2),_AlaIgmpMemberIfIndex_Type())
alaIgmpMemberIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpMemberIfIndex.setStatus(_A)
_AlaIgmpMemberGroupAddress_Type=InetAddressIPv4
_AlaIgmpMemberGroupAddress_Object=MibTableColumn
alaIgmpMemberGroupAddress=_AlaIgmpMemberGroupAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,3,1,1,3),_AlaIgmpMemberGroupAddress_Type())
alaIgmpMemberGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpMemberGroupAddress.setStatus(_A)
_AlaIgmpMemberSourceAddress_Type=InetAddressIPv4
_AlaIgmpMemberSourceAddress_Object=MibTableColumn
alaIgmpMemberSourceAddress=_AlaIgmpMemberSourceAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,3,1,1,4),_AlaIgmpMemberSourceAddress_Type())
alaIgmpMemberSourceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpMemberSourceAddress.setStatus(_A)
class _AlaIgmpMemberMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('include',1),('exclude',2)))
_AlaIgmpMemberMode_Type.__name__=_E
_AlaIgmpMemberMode_Object=MibTableColumn
alaIgmpMemberMode=_AlaIgmpMemberMode_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,3,1,1,5),_AlaIgmpMemberMode_Type())
alaIgmpMemberMode.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpMemberMode.setStatus(_A)
_AlaIgmpMemberCount_Type=Counter32
_AlaIgmpMemberCount_Object=MibTableColumn
alaIgmpMemberCount=_AlaIgmpMemberCount_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,3,1,1,6),_AlaIgmpMemberCount_Type())
alaIgmpMemberCount.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpMemberCount.setStatus(_A)
_AlaIgmpMemberTimeout_Type=TimeTicks
_AlaIgmpMemberTimeout_Object=MibTableColumn
alaIgmpMemberTimeout=_AlaIgmpMemberTimeout_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,3,1,1,7),_AlaIgmpMemberTimeout_Type())
alaIgmpMemberTimeout.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpMemberTimeout.setStatus(_A)
_AlaIgmpStaticMember_ObjectIdentity=ObjectIdentity
alaIgmpStaticMember=_AlaIgmpStaticMember_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,4))
_AlaIgmpStaticMemberTable_Object=MibTable
alaIgmpStaticMemberTable=_AlaIgmpStaticMemberTable_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,4,1))
if mibBuilder.loadTexts:alaIgmpStaticMemberTable.setStatus(_A)
_AlaIgmpStaticMemberEntry_Object=MibTableRow
alaIgmpStaticMemberEntry=_AlaIgmpStaticMemberEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,4,1,1))
alaIgmpStaticMemberEntry.setIndexNames((0,_B,_b),(0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:alaIgmpStaticMemberEntry.setStatus(_A)
_AlaIgmpStaticMemberVlan_Type=Unsigned32
_AlaIgmpStaticMemberVlan_Object=MibTableColumn
alaIgmpStaticMemberVlan=_AlaIgmpStaticMemberVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,4,1,1,1),_AlaIgmpStaticMemberVlan_Type())
alaIgmpStaticMemberVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpStaticMemberVlan.setStatus(_A)
_AlaIgmpStaticMemberIfIndex_Type=InterfaceIndex
_AlaIgmpStaticMemberIfIndex_Object=MibTableColumn
alaIgmpStaticMemberIfIndex=_AlaIgmpStaticMemberIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,4,1,1,2),_AlaIgmpStaticMemberIfIndex_Type())
alaIgmpStaticMemberIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpStaticMemberIfIndex.setStatus(_A)
_AlaIgmpStaticMemberGroupAddress_Type=InetAddressIPv4
_AlaIgmpStaticMemberGroupAddress_Object=MibTableColumn
alaIgmpStaticMemberGroupAddress=_AlaIgmpStaticMemberGroupAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,4,1,1,3),_AlaIgmpStaticMemberGroupAddress_Type())
alaIgmpStaticMemberGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpStaticMemberGroupAddress.setStatus(_A)
_AlaIgmpStaticMemberRowStatus_Type=RowStatus
_AlaIgmpStaticMemberRowStatus_Object=MibTableColumn
alaIgmpStaticMemberRowStatus=_AlaIgmpStaticMemberRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,4,1,1,4),_AlaIgmpStaticMemberRowStatus_Type())
alaIgmpStaticMemberRowStatus.setMaxAccess(_S)
if mibBuilder.loadTexts:alaIgmpStaticMemberRowStatus.setStatus(_A)
_AlaIgmpNeighbor_ObjectIdentity=ObjectIdentity
alaIgmpNeighbor=_AlaIgmpNeighbor_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,5))
_AlaIgmpNeighborTable_Object=MibTable
alaIgmpNeighborTable=_AlaIgmpNeighborTable_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,5,1))
if mibBuilder.loadTexts:alaIgmpNeighborTable.setStatus(_A)
_AlaIgmpNeighborEntry_Object=MibTableRow
alaIgmpNeighborEntry=_AlaIgmpNeighborEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,5,1,1))
alaIgmpNeighborEntry.setIndexNames((0,_B,_e),(0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:alaIgmpNeighborEntry.setStatus(_A)
_AlaIgmpNeighborVlan_Type=Unsigned32
_AlaIgmpNeighborVlan_Object=MibTableColumn
alaIgmpNeighborVlan=_AlaIgmpNeighborVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,5,1,1,1),_AlaIgmpNeighborVlan_Type())
alaIgmpNeighborVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpNeighborVlan.setStatus(_A)
_AlaIgmpNeighborIfIndex_Type=InterfaceIndex
_AlaIgmpNeighborIfIndex_Object=MibTableColumn
alaIgmpNeighborIfIndex=_AlaIgmpNeighborIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,5,1,1,2),_AlaIgmpNeighborIfIndex_Type())
alaIgmpNeighborIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpNeighborIfIndex.setStatus(_A)
_AlaIgmpNeighborHostAddress_Type=InetAddressIPv4
_AlaIgmpNeighborHostAddress_Object=MibTableColumn
alaIgmpNeighborHostAddress=_AlaIgmpNeighborHostAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,5,1,1,3),_AlaIgmpNeighborHostAddress_Type())
alaIgmpNeighborHostAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpNeighborHostAddress.setStatus(_A)
_AlaIgmpNeighborCount_Type=Counter32
_AlaIgmpNeighborCount_Object=MibTableColumn
alaIgmpNeighborCount=_AlaIgmpNeighborCount_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,5,1,1,4),_AlaIgmpNeighborCount_Type())
alaIgmpNeighborCount.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpNeighborCount.setStatus(_A)
_AlaIgmpNeighborTimeout_Type=TimeTicks
_AlaIgmpNeighborTimeout_Object=MibTableColumn
alaIgmpNeighborTimeout=_AlaIgmpNeighborTimeout_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,5,1,1,5),_AlaIgmpNeighborTimeout_Type())
alaIgmpNeighborTimeout.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpNeighborTimeout.setStatus(_A)
_AlaIgmpStaticNeighbor_ObjectIdentity=ObjectIdentity
alaIgmpStaticNeighbor=_AlaIgmpStaticNeighbor_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,6))
_AlaIgmpStaticNeighborTable_Object=MibTable
alaIgmpStaticNeighborTable=_AlaIgmpStaticNeighborTable_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,6,1))
if mibBuilder.loadTexts:alaIgmpStaticNeighborTable.setStatus(_A)
_AlaIgmpStaticNeighborEntry_Object=MibTableRow
alaIgmpStaticNeighborEntry=_AlaIgmpStaticNeighborEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,6,1,1))
alaIgmpStaticNeighborEntry.setIndexNames((0,_B,_h),(0,_B,_i))
if mibBuilder.loadTexts:alaIgmpStaticNeighborEntry.setStatus(_A)
_AlaIgmpStaticNeighborVlan_Type=Unsigned32
_AlaIgmpStaticNeighborVlan_Object=MibTableColumn
alaIgmpStaticNeighborVlan=_AlaIgmpStaticNeighborVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,6,1,1,1),_AlaIgmpStaticNeighborVlan_Type())
alaIgmpStaticNeighborVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpStaticNeighborVlan.setStatus(_A)
_AlaIgmpStaticNeighborIfIndex_Type=InterfaceIndex
_AlaIgmpStaticNeighborIfIndex_Object=MibTableColumn
alaIgmpStaticNeighborIfIndex=_AlaIgmpStaticNeighborIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,6,1,1,2),_AlaIgmpStaticNeighborIfIndex_Type())
alaIgmpStaticNeighborIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpStaticNeighborIfIndex.setStatus(_A)
_AlaIgmpStaticNeighborRowStatus_Type=RowStatus
_AlaIgmpStaticNeighborRowStatus_Object=MibTableColumn
alaIgmpStaticNeighborRowStatus=_AlaIgmpStaticNeighborRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,6,1,1,3),_AlaIgmpStaticNeighborRowStatus_Type())
alaIgmpStaticNeighborRowStatus.setMaxAccess(_S)
if mibBuilder.loadTexts:alaIgmpStaticNeighborRowStatus.setStatus(_A)
_AlaIgmpQuerier_ObjectIdentity=ObjectIdentity
alaIgmpQuerier=_AlaIgmpQuerier_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,7))
_AlaIgmpQuerierTable_Object=MibTable
alaIgmpQuerierTable=_AlaIgmpQuerierTable_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,7,1))
if mibBuilder.loadTexts:alaIgmpQuerierTable.setStatus(_A)
_AlaIgmpQuerierEntry_Object=MibTableRow
alaIgmpQuerierEntry=_AlaIgmpQuerierEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,7,1,1))
alaIgmpQuerierEntry.setIndexNames((0,_B,_j),(0,_B,_k),(0,_B,_l))
if mibBuilder.loadTexts:alaIgmpQuerierEntry.setStatus(_A)
_AlaIgmpQuerierVlan_Type=Unsigned32
_AlaIgmpQuerierVlan_Object=MibTableColumn
alaIgmpQuerierVlan=_AlaIgmpQuerierVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,7,1,1,1),_AlaIgmpQuerierVlan_Type())
alaIgmpQuerierVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpQuerierVlan.setStatus(_A)
_AlaIgmpQuerierIfIndex_Type=InterfaceIndex
_AlaIgmpQuerierIfIndex_Object=MibTableColumn
alaIgmpQuerierIfIndex=_AlaIgmpQuerierIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,7,1,1,2),_AlaIgmpQuerierIfIndex_Type())
alaIgmpQuerierIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpQuerierIfIndex.setStatus(_A)
_AlaIgmpQuerierHostAddress_Type=InetAddressIPv4
_AlaIgmpQuerierHostAddress_Object=MibTableColumn
alaIgmpQuerierHostAddress=_AlaIgmpQuerierHostAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,7,1,1,3),_AlaIgmpQuerierHostAddress_Type())
alaIgmpQuerierHostAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpQuerierHostAddress.setStatus(_A)
_AlaIgmpQuerierCount_Type=Counter32
_AlaIgmpQuerierCount_Object=MibTableColumn
alaIgmpQuerierCount=_AlaIgmpQuerierCount_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,7,1,1,4),_AlaIgmpQuerierCount_Type())
alaIgmpQuerierCount.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpQuerierCount.setStatus(_A)
_AlaIgmpQuerierTimeout_Type=TimeTicks
_AlaIgmpQuerierTimeout_Object=MibTableColumn
alaIgmpQuerierTimeout=_AlaIgmpQuerierTimeout_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,7,1,1,5),_AlaIgmpQuerierTimeout_Type())
alaIgmpQuerierTimeout.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpQuerierTimeout.setStatus(_A)
_AlaIgmpStaticQuerier_ObjectIdentity=ObjectIdentity
alaIgmpStaticQuerier=_AlaIgmpStaticQuerier_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,8))
_AlaIgmpStaticQuerierTable_Object=MibTable
alaIgmpStaticQuerierTable=_AlaIgmpStaticQuerierTable_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,8,1))
if mibBuilder.loadTexts:alaIgmpStaticQuerierTable.setStatus(_A)
_AlaIgmpStaticQuerierEntry_Object=MibTableRow
alaIgmpStaticQuerierEntry=_AlaIgmpStaticQuerierEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,8,1,1))
alaIgmpStaticQuerierEntry.setIndexNames((0,_B,_m),(0,_B,_n))
if mibBuilder.loadTexts:alaIgmpStaticQuerierEntry.setStatus(_A)
_AlaIgmpStaticQuerierVlan_Type=Unsigned32
_AlaIgmpStaticQuerierVlan_Object=MibTableColumn
alaIgmpStaticQuerierVlan=_AlaIgmpStaticQuerierVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,8,1,1,1),_AlaIgmpStaticQuerierVlan_Type())
alaIgmpStaticQuerierVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpStaticQuerierVlan.setStatus(_A)
_AlaIgmpStaticQuerierIfIndex_Type=InterfaceIndex
_AlaIgmpStaticQuerierIfIndex_Object=MibTableColumn
alaIgmpStaticQuerierIfIndex=_AlaIgmpStaticQuerierIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,8,1,1,2),_AlaIgmpStaticQuerierIfIndex_Type())
alaIgmpStaticQuerierIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpStaticQuerierIfIndex.setStatus(_A)
_AlaIgmpStaticQuerierRowStatus_Type=RowStatus
_AlaIgmpStaticQuerierRowStatus_Object=MibTableColumn
alaIgmpStaticQuerierRowStatus=_AlaIgmpStaticQuerierRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,8,1,1,3),_AlaIgmpStaticQuerierRowStatus_Type())
alaIgmpStaticQuerierRowStatus.setMaxAccess(_S)
if mibBuilder.loadTexts:alaIgmpStaticQuerierRowStatus.setStatus(_A)
_AlaIgmpSource_ObjectIdentity=ObjectIdentity
alaIgmpSource=_AlaIgmpSource_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,9))
_AlaIgmpSourceTable_Object=MibTable
alaIgmpSourceTable=_AlaIgmpSourceTable_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,9,1))
if mibBuilder.loadTexts:alaIgmpSourceTable.setStatus(_A)
_AlaIgmpSourceEntry_Object=MibTableRow
alaIgmpSourceEntry=_AlaIgmpSourceEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,9,1,1))
alaIgmpSourceEntry.setIndexNames((0,_B,_o),(0,_B,_p),(0,_B,_q),(0,_B,_r),(0,_B,_s))
if mibBuilder.loadTexts:alaIgmpSourceEntry.setStatus(_A)
_AlaIgmpSourceVlan_Type=Unsigned32
_AlaIgmpSourceVlan_Object=MibTableColumn
alaIgmpSourceVlan=_AlaIgmpSourceVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,9,1,1,1),_AlaIgmpSourceVlan_Type())
alaIgmpSourceVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpSourceVlan.setStatus(_A)
_AlaIgmpSourceIfIndex_Type=InterfaceIndexOrZero
_AlaIgmpSourceIfIndex_Object=MibTableColumn
alaIgmpSourceIfIndex=_AlaIgmpSourceIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,9,1,1,2),_AlaIgmpSourceIfIndex_Type())
alaIgmpSourceIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpSourceIfIndex.setStatus(_A)
_AlaIgmpSourceGroupAddress_Type=InetAddressIPv4
_AlaIgmpSourceGroupAddress_Object=MibTableColumn
alaIgmpSourceGroupAddress=_AlaIgmpSourceGroupAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,9,1,1,3),_AlaIgmpSourceGroupAddress_Type())
alaIgmpSourceGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpSourceGroupAddress.setStatus(_A)
_AlaIgmpSourceHostAddress_Type=InetAddressIPv4
_AlaIgmpSourceHostAddress_Object=MibTableColumn
alaIgmpSourceHostAddress=_AlaIgmpSourceHostAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,9,1,1,4),_AlaIgmpSourceHostAddress_Type())
alaIgmpSourceHostAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpSourceHostAddress.setStatus(_A)
_AlaIgmpSourceDestAddress_Type=InetAddressIPv4
_AlaIgmpSourceDestAddress_Object=MibTableColumn
alaIgmpSourceDestAddress=_AlaIgmpSourceDestAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,9,1,1,5),_AlaIgmpSourceDestAddress_Type())
alaIgmpSourceDestAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpSourceDestAddress.setStatus(_A)
_AlaIgmpSourceOrigAddress_Type=InetAddressIPv4
_AlaIgmpSourceOrigAddress_Object=MibTableColumn
alaIgmpSourceOrigAddress=_AlaIgmpSourceOrigAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,9,1,1,6),_AlaIgmpSourceOrigAddress_Type())
alaIgmpSourceOrigAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpSourceOrigAddress.setStatus(_A)
class _AlaIgmpSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AlaIgmpSourceType_Type.__name__=_E
_AlaIgmpSourceType_Object=MibTableColumn
alaIgmpSourceType=_AlaIgmpSourceType_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,9,1,1,7),_AlaIgmpSourceType_Type())
alaIgmpSourceType.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpSourceType.setStatus(_A)
_AlaIgmpForward_ObjectIdentity=ObjectIdentity
alaIgmpForward=_AlaIgmpForward_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,10))
_AlaIgmpForwardTable_Object=MibTable
alaIgmpForwardTable=_AlaIgmpForwardTable_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,10,1))
if mibBuilder.loadTexts:alaIgmpForwardTable.setStatus(_A)
_AlaIgmpForwardEntry_Object=MibTableRow
alaIgmpForwardEntry=_AlaIgmpForwardEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,10,1,1))
alaIgmpForwardEntry.setIndexNames((0,_B,_t),(0,_B,_u),(0,_B,_v),(0,_B,_w),(0,_B,_x),(0,_B,_y),(0,_B,_z))
if mibBuilder.loadTexts:alaIgmpForwardEntry.setStatus(_A)
_AlaIgmpForwardVlan_Type=Unsigned32
_AlaIgmpForwardVlan_Object=MibTableColumn
alaIgmpForwardVlan=_AlaIgmpForwardVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,10,1,1,1),_AlaIgmpForwardVlan_Type())
alaIgmpForwardVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpForwardVlan.setStatus(_A)
_AlaIgmpForwardIfIndex_Type=InterfaceIndexOrZero
_AlaIgmpForwardIfIndex_Object=MibTableColumn
alaIgmpForwardIfIndex=_AlaIgmpForwardIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,10,1,1,2),_AlaIgmpForwardIfIndex_Type())
alaIgmpForwardIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpForwardIfIndex.setStatus(_A)
_AlaIgmpForwardGroupAddress_Type=InetAddressIPv4
_AlaIgmpForwardGroupAddress_Object=MibTableColumn
alaIgmpForwardGroupAddress=_AlaIgmpForwardGroupAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,10,1,1,3),_AlaIgmpForwardGroupAddress_Type())
alaIgmpForwardGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpForwardGroupAddress.setStatus(_A)
_AlaIgmpForwardHostAddress_Type=InetAddressIPv4
_AlaIgmpForwardHostAddress_Object=MibTableColumn
alaIgmpForwardHostAddress=_AlaIgmpForwardHostAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,10,1,1,4),_AlaIgmpForwardHostAddress_Type())
alaIgmpForwardHostAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpForwardHostAddress.setStatus(_A)
_AlaIgmpForwardDestAddress_Type=InetAddressIPv4
_AlaIgmpForwardDestAddress_Object=MibTableColumn
alaIgmpForwardDestAddress=_AlaIgmpForwardDestAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,10,1,1,5),_AlaIgmpForwardDestAddress_Type())
alaIgmpForwardDestAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpForwardDestAddress.setStatus(_A)
_AlaIgmpForwardOrigAddress_Type=InetAddressIPv4
_AlaIgmpForwardOrigAddress_Object=MibTableColumn
alaIgmpForwardOrigAddress=_AlaIgmpForwardOrigAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,10,1,1,6),_AlaIgmpForwardOrigAddress_Type())
alaIgmpForwardOrigAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpForwardOrigAddress.setStatus(_A)
class _AlaIgmpForwardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AlaIgmpForwardType_Type.__name__=_E
_AlaIgmpForwardType_Object=MibTableColumn
alaIgmpForwardType=_AlaIgmpForwardType_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,10,1,1,7),_AlaIgmpForwardType_Type())
alaIgmpForwardType.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpForwardType.setStatus(_A)
_AlaIgmpForwardNextVlan_Type=Unsigned32
_AlaIgmpForwardNextVlan_Object=MibTableColumn
alaIgmpForwardNextVlan=_AlaIgmpForwardNextVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,10,1,1,8),_AlaIgmpForwardNextVlan_Type())
alaIgmpForwardNextVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpForwardNextVlan.setStatus(_A)
_AlaIgmpForwardNextIfIndex_Type=InterfaceIndex
_AlaIgmpForwardNextIfIndex_Object=MibTableColumn
alaIgmpForwardNextIfIndex=_AlaIgmpForwardNextIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,10,1,1,9),_AlaIgmpForwardNextIfIndex_Type())
alaIgmpForwardNextIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpForwardNextIfIndex.setStatus(_A)
class _AlaIgmpForwardNextType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AlaIgmpForwardNextType_Type.__name__=_E
_AlaIgmpForwardNextType_Object=MibTableColumn
alaIgmpForwardNextType=_AlaIgmpForwardNextType_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,10,1,1,10),_AlaIgmpForwardNextType_Type())
alaIgmpForwardNextType.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpForwardNextType.setStatus(_A)
_AlaIgmpTunnel_ObjectIdentity=ObjectIdentity
alaIgmpTunnel=_AlaIgmpTunnel_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,11))
_AlaIgmpTunnelTable_Object=MibTable
alaIgmpTunnelTable=_AlaIgmpTunnelTable_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,11,1))
if mibBuilder.loadTexts:alaIgmpTunnelTable.setStatus(_A)
_AlaIgmpTunnelEntry_Object=MibTableRow
alaIgmpTunnelEntry=_AlaIgmpTunnelEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,11,1,1))
alaIgmpTunnelEntry.setIndexNames((0,_B,_A0),(0,_B,_A1),(0,_B,_A2),(0,_B,_A3),(0,_B,_A4),(0,_B,_A5))
if mibBuilder.loadTexts:alaIgmpTunnelEntry.setStatus(_A)
_AlaIgmpTunnelVlan_Type=Unsigned32
_AlaIgmpTunnelVlan_Object=MibTableColumn
alaIgmpTunnelVlan=_AlaIgmpTunnelVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,11,1,1,1),_AlaIgmpTunnelVlan_Type())
alaIgmpTunnelVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpTunnelVlan.setStatus(_A)
_AlaIgmpTunnelIfIndex_Type=InterfaceIndexOrZero
_AlaIgmpTunnelIfIndex_Object=MibTableColumn
alaIgmpTunnelIfIndex=_AlaIgmpTunnelIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,11,1,1,2),_AlaIgmpTunnelIfIndex_Type())
alaIgmpTunnelIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpTunnelIfIndex.setStatus(_A)
_AlaIgmpTunnelGroupAddress_Type=InetAddressIPv4
_AlaIgmpTunnelGroupAddress_Object=MibTableColumn
alaIgmpTunnelGroupAddress=_AlaIgmpTunnelGroupAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,11,1,1,3),_AlaIgmpTunnelGroupAddress_Type())
alaIgmpTunnelGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpTunnelGroupAddress.setStatus(_A)
_AlaIgmpTunnelHostAddress_Type=InetAddressIPv4
_AlaIgmpTunnelHostAddress_Object=MibTableColumn
alaIgmpTunnelHostAddress=_AlaIgmpTunnelHostAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,11,1,1,4),_AlaIgmpTunnelHostAddress_Type())
alaIgmpTunnelHostAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpTunnelHostAddress.setStatus(_A)
_AlaIgmpTunnelDestAddress_Type=InetAddressIPv4
_AlaIgmpTunnelDestAddress_Object=MibTableColumn
alaIgmpTunnelDestAddress=_AlaIgmpTunnelDestAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,11,1,1,5),_AlaIgmpTunnelDestAddress_Type())
alaIgmpTunnelDestAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpTunnelDestAddress.setStatus(_A)
_AlaIgmpTunnelOrigAddress_Type=InetAddressIPv4
_AlaIgmpTunnelOrigAddress_Object=MibTableColumn
alaIgmpTunnelOrigAddress=_AlaIgmpTunnelOrigAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,11,1,1,6),_AlaIgmpTunnelOrigAddress_Type())
alaIgmpTunnelOrigAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpTunnelOrigAddress.setStatus(_A)
class _AlaIgmpTunnelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AlaIgmpTunnelType_Type.__name__=_E
_AlaIgmpTunnelType_Object=MibTableColumn
alaIgmpTunnelType=_AlaIgmpTunnelType_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,11,1,1,7),_AlaIgmpTunnelType_Type())
alaIgmpTunnelType.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpTunnelType.setStatus(_A)
_AlaIgmpTunnelNextDestAddress_Type=InetAddressIPv4
_AlaIgmpTunnelNextDestAddress_Object=MibTableColumn
alaIgmpTunnelNextDestAddress=_AlaIgmpTunnelNextDestAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,11,1,1,8),_AlaIgmpTunnelNextDestAddress_Type())
alaIgmpTunnelNextDestAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpTunnelNextDestAddress.setStatus(_A)
class _AlaIgmpTunnelNextType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_AlaIgmpTunnelNextType_Type.__name__=_E
_AlaIgmpTunnelNextType_Object=MibTableColumn
alaIgmpTunnelNextType=_AlaIgmpTunnelNextType_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,11,1,1,9),_AlaIgmpTunnelNextType_Type())
alaIgmpTunnelNextType.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpTunnelNextType.setStatus(_A)
_AlaIgmpPort_ObjectIdentity=ObjectIdentity
alaIgmpPort=_AlaIgmpPort_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,12))
_AlaIgmpPortTable_Object=MibTable
alaIgmpPortTable=_AlaIgmpPortTable_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,12,1))
if mibBuilder.loadTexts:alaIgmpPortTable.setStatus(_A)
_AlaIgmpPortEntry_Object=MibTableRow
alaIgmpPortEntry=_AlaIgmpPortEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,12,1,1))
alaIgmpPortEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:alaIgmpPortEntry.setStatus(_A)
_AlaIgmpPortIfIndex_Type=InterfaceIndex
_AlaIgmpPortIfIndex_Object=MibTableColumn
alaIgmpPortIfIndex=_AlaIgmpPortIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,12,1,1,1),_AlaIgmpPortIfIndex_Type())
alaIgmpPortIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpPortIfIndex.setStatus(_A)
class _AlaIgmpPortMaxGroupLimit_Type(Unsigned32):defaultValue=0
_AlaIgmpPortMaxGroupLimit_Type.__name__=_H
_AlaIgmpPortMaxGroupLimit_Object=MibTableColumn
alaIgmpPortMaxGroupLimit=_AlaIgmpPortMaxGroupLimit_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,12,1,1,2),_AlaIgmpPortMaxGroupLimit_Type())
alaIgmpPortMaxGroupLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpPortMaxGroupLimit.setStatus(_A)
class _AlaIgmpPortMaxGroupExceedAction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_Q,1),(_R,2)))
_AlaIgmpPortMaxGroupExceedAction_Type.__name__=_E
_AlaIgmpPortMaxGroupExceedAction_Object=MibTableColumn
alaIgmpPortMaxGroupExceedAction=_AlaIgmpPortMaxGroupExceedAction_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,12,1,1,3),_AlaIgmpPortMaxGroupExceedAction_Type())
alaIgmpPortMaxGroupExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIgmpPortMaxGroupExceedAction.setStatus(_A)
_AlaIgmpPortVlan_ObjectIdentity=ObjectIdentity
alaIgmpPortVlan=_AlaIgmpPortVlan_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,13))
_AlaIgmpPortVlanTable_Object=MibTable
alaIgmpPortVlanTable=_AlaIgmpPortVlanTable_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,13,1))
if mibBuilder.loadTexts:alaIgmpPortVlanTable.setStatus(_A)
_AlaIgmpPortVlanEntry_Object=MibTableRow
alaIgmpPortVlanEntry=_AlaIgmpPortVlanEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,13,1,1))
alaIgmpPortVlanEntry.setIndexNames((0,_B,_T),(0,_B,_A6))
if mibBuilder.loadTexts:alaIgmpPortVlanEntry.setStatus(_A)
_AlaIgmpVlanId_Type=Unsigned32
_AlaIgmpVlanId_Object=MibTableColumn
alaIgmpVlanId=_AlaIgmpVlanId_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,13,1,1,1),_AlaIgmpVlanId_Type())
alaIgmpVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIgmpVlanId.setStatus(_A)
_AlaIgmpPortVlanCurrentGroupCount_Type=Unsigned32
_AlaIgmpPortVlanCurrentGroupCount_Object=MibTableColumn
alaIgmpPortVlanCurrentGroupCount=_AlaIgmpPortVlanCurrentGroupCount_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,13,1,1,2),_AlaIgmpPortVlanCurrentGroupCount_Type())
alaIgmpPortVlanCurrentGroupCount.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpPortVlanCurrentGroupCount.setStatus(_A)
_AlaIgmpPortVlanMaxGroupLimit_Type=Unsigned32
_AlaIgmpPortVlanMaxGroupLimit_Object=MibTableColumn
alaIgmpPortVlanMaxGroupLimit=_AlaIgmpPortVlanMaxGroupLimit_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,13,1,1,3),_AlaIgmpPortVlanMaxGroupLimit_Type())
alaIgmpPortVlanMaxGroupLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpPortVlanMaxGroupLimit.setStatus(_A)
class _AlaIgmpPortVlanMaxGroupExceedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_Q,1),(_R,2)))
_AlaIgmpPortVlanMaxGroupExceedAction_Type.__name__=_E
_AlaIgmpPortVlanMaxGroupExceedAction_Object=MibTableColumn
alaIgmpPortVlanMaxGroupExceedAction=_AlaIgmpPortVlanMaxGroupExceedAction_Object((1,3,6,1,4,1,6486,801,1,2,1,34,1,1,13,1,1,4),_AlaIgmpPortVlanMaxGroupExceedAction_Type())
alaIgmpPortVlanMaxGroupExceedAction.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIgmpPortVlanMaxGroupExceedAction.setStatus(_A)
_AlcatelIND1IgmpMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1IgmpMIBConformance=_AlcatelIND1IgmpMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,2))
_AlcatelIND1IgmpMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1IgmpMIBCompliances=_AlcatelIND1IgmpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,1))
_AlcatelIND1IgmpMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1IgmpMIBGroups=_AlcatelIND1IgmpMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,2))
alaIgmpGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,2,1))
alaIgmpGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:alaIgmpGroup.setStatus(_K)
alaIgmpVlanGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,2,2))
alaIgmpVlanGroup.setObjects(*((_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am)))
if mibBuilder.loadTexts:alaIgmpVlanGroup.setStatus(_K)
alaIgmpMemberGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,2,3))
alaIgmpMemberGroup.setObjects(*((_B,_An),(_B,_Ao),(_B,_Ap)))
if mibBuilder.loadTexts:alaIgmpMemberGroup.setStatus(_K)
alaIgmpStaticMemberGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,2,4))
alaIgmpStaticMemberGroup.setObjects((_B,_Aq))
if mibBuilder.loadTexts:alaIgmpStaticMemberGroup.setStatus(_K)
alaIgmpNeighborGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,2,5))
alaIgmpNeighborGroup.setObjects(*((_B,_Ar),(_B,_As)))
if mibBuilder.loadTexts:alaIgmpNeighborGroup.setStatus(_K)
alaIgmpStaticNeighborGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,2,6))
alaIgmpStaticNeighborGroup.setObjects((_B,_At))
if mibBuilder.loadTexts:alaIgmpStaticNeighborGroup.setStatus(_K)
alaIgmpQuerierGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,2,7))
alaIgmpQuerierGroup.setObjects(*((_B,_Au),(_B,_Av)))
if mibBuilder.loadTexts:alaIgmpQuerierGroup.setStatus(_K)
alaIgmpStaticQuerierGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,2,8))
alaIgmpStaticQuerierGroup.setObjects((_B,_Aw))
if mibBuilder.loadTexts:alaIgmpStaticQuerierGroup.setStatus(_K)
alaIgmpSourceGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,2,9))
alaIgmpSourceGroup.setObjects(*((_B,_Ax),(_B,_Ay)))
if mibBuilder.loadTexts:alaIgmpSourceGroup.setStatus(_K)
alaIgmpForwardGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,2,10))
alaIgmpForwardGroup.setObjects(*((_B,_Az),(_B,_A_),(_B,_B0)))
if mibBuilder.loadTexts:alaIgmpForwardGroup.setStatus(_K)
alaIgmpTunnelGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,2,11))
alaIgmpTunnelGroup.setObjects(*((_B,_B1),(_B,_B2),(_B,_B3)))
if mibBuilder.loadTexts:alaIgmpTunnelGroup.setStatus(_K)
alaIgmpPortGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,2,12))
alaIgmpPortGroup.setObjects(*((_B,_B4),(_B,_B5)))
if mibBuilder.loadTexts:alaIgmpPortGroup.setStatus(_K)
alaIgmpPortVlanGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,2,13))
alaIgmpPortVlanGroup.setObjects(*((_B,_B6),(_B,_B7),(_B,_B8)))
if mibBuilder.loadTexts:alaIgmpPortVlanGroup.setStatus(_K)
alaIgmpCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,34,1,2,1,1))
alaIgmpCompliance.setObjects(*((_B,_B9),(_B,_BA),(_B,_BB),(_B,_BC),(_B,_BD),(_B,_BE),(_B,_BF),(_B,_BG),(_B,_BH),(_B,_BI),(_B,_BJ),(_B,_BK),(_B,_BL)))
if mibBuilder.loadTexts:alaIgmpCompliance.setStatus(_K)
mibBuilder.exportSymbols(_B,**{'alcatelIND1IgmpMIB':alcatelIND1IgmpMIB,'alcatelIND1IgmpMIBObjects':alcatelIND1IgmpMIBObjects,'alaIgmp':alaIgmp,_A7:alaIgmpStatus,_A8:alaIgmpQuerying,_A9:alaIgmpSpoofing,_AA:alaIgmpZapping,_AB:alaIgmpVersion,_AC:alaIgmpRobustness,_AD:alaIgmpQueryInterval,_AE:alaIgmpQueryResponseInterval,_AF:alaIgmpLastMemberQueryInterval,_AG:alaIgmpRouterTimeout,_AH:alaIgmpSourceTimeout,_AI:alaIgmpProxying,_AJ:alaIgmpUnsolicitedReportInterval,_AK:alaIgmpQuerierForwarding,_AL:alaIgmpMaxGroupLimit,_AM:alaIgmpMaxGroupExceedAction,_AN:alaIgmpFloodUnknown,_AO:alaIgmpHelperAddressType,_AP:alaIgmpHelperAddress,_AQ:alaIgmpZeroBasedQuery,_AR:alaIgmpInitialPacketBuffer,_AS:alaIgmpInitialPacketBufferMaxPacket,_AT:alaIgmpInitialPacketBufferMaxFlow,_AU:alaIgmpInitialPacketBufferTimeout,_AV:alaIgmpInitialPacketBufferMinDelay,'alaIgmpVlan':alaIgmpVlan,'alaIgmpVlanTable':alaIgmpVlanTable,'alaIgmpVlanEntry':alaIgmpVlanEntry,_W:alaIgmpVlanIndex,_AW:alaIgmpVlanStatus,_AX:alaIgmpVlanQuerying,_AY:alaIgmpVlanSpoofing,_AZ:alaIgmpVlanZapping,_Aa:alaIgmpVlanVersion,_Ab:alaIgmpVlanRobustness,_Ac:alaIgmpVlanQueryInterval,_Ad:alaIgmpVlanQueryResponseInterval,_Ae:alaIgmpVlanLastMemberQueryInterval,_Af:alaIgmpVlanRouterTimeout,_Ag:alaIgmpVlanSourceTimeout,_Ah:alaIgmpVlanProxying,_Ai:alaIgmpVlanUnsolicitedReportInterval,_Aj:alaIgmpVlanQuerierForwarding,_Ak:alaIgmpVlanMaxGroupLimit,_Al:alaIgmpVlanMaxGroupExceedAction,_Am:alaIgmpVlanZeroBasedQuery,'alaIgmpMember':alaIgmpMember,'alaIgmpMemberTable':alaIgmpMemberTable,'alaIgmpMemberEntry':alaIgmpMemberEntry,_X:alaIgmpMemberVlan,_Y:alaIgmpMemberIfIndex,_Z:alaIgmpMemberGroupAddress,_a:alaIgmpMemberSourceAddress,_An:alaIgmpMemberMode,_Ao:alaIgmpMemberCount,_Ap:alaIgmpMemberTimeout,'alaIgmpStaticMember':alaIgmpStaticMember,'alaIgmpStaticMemberTable':alaIgmpStaticMemberTable,'alaIgmpStaticMemberEntry':alaIgmpStaticMemberEntry,_b:alaIgmpStaticMemberVlan,_c:alaIgmpStaticMemberIfIndex,_d:alaIgmpStaticMemberGroupAddress,_Aq:alaIgmpStaticMemberRowStatus,'alaIgmpNeighbor':alaIgmpNeighbor,'alaIgmpNeighborTable':alaIgmpNeighborTable,'alaIgmpNeighborEntry':alaIgmpNeighborEntry,_e:alaIgmpNeighborVlan,_f:alaIgmpNeighborIfIndex,_g:alaIgmpNeighborHostAddress,_Ar:alaIgmpNeighborCount,_As:alaIgmpNeighborTimeout,'alaIgmpStaticNeighbor':alaIgmpStaticNeighbor,'alaIgmpStaticNeighborTable':alaIgmpStaticNeighborTable,'alaIgmpStaticNeighborEntry':alaIgmpStaticNeighborEntry,_h:alaIgmpStaticNeighborVlan,_i:alaIgmpStaticNeighborIfIndex,_At:alaIgmpStaticNeighborRowStatus,'alaIgmpQuerier':alaIgmpQuerier,'alaIgmpQuerierTable':alaIgmpQuerierTable,'alaIgmpQuerierEntry':alaIgmpQuerierEntry,_j:alaIgmpQuerierVlan,_k:alaIgmpQuerierIfIndex,_l:alaIgmpQuerierHostAddress,_Au:alaIgmpQuerierCount,_Av:alaIgmpQuerierTimeout,'alaIgmpStaticQuerier':alaIgmpStaticQuerier,'alaIgmpStaticQuerierTable':alaIgmpStaticQuerierTable,'alaIgmpStaticQuerierEntry':alaIgmpStaticQuerierEntry,_m:alaIgmpStaticQuerierVlan,_n:alaIgmpStaticQuerierIfIndex,_Aw:alaIgmpStaticQuerierRowStatus,'alaIgmpSource':alaIgmpSource,'alaIgmpSourceTable':alaIgmpSourceTable,'alaIgmpSourceEntry':alaIgmpSourceEntry,_o:alaIgmpSourceVlan,_Ax:alaIgmpSourceIfIndex,_p:alaIgmpSourceGroupAddress,_q:alaIgmpSourceHostAddress,_r:alaIgmpSourceDestAddress,_s:alaIgmpSourceOrigAddress,_Ay:alaIgmpSourceType,'alaIgmpForward':alaIgmpForward,'alaIgmpForwardTable':alaIgmpForwardTable,'alaIgmpForwardEntry':alaIgmpForwardEntry,_t:alaIgmpForwardVlan,_Az:alaIgmpForwardIfIndex,_u:alaIgmpForwardGroupAddress,_v:alaIgmpForwardHostAddress,_w:alaIgmpForwardDestAddress,_x:alaIgmpForwardOrigAddress,_A_:alaIgmpForwardType,_y:alaIgmpForwardNextVlan,_z:alaIgmpForwardNextIfIndex,_B0:alaIgmpForwardNextType,'alaIgmpTunnel':alaIgmpTunnel,'alaIgmpTunnelTable':alaIgmpTunnelTable,'alaIgmpTunnelEntry':alaIgmpTunnelEntry,_A0:alaIgmpTunnelVlan,_B1:alaIgmpTunnelIfIndex,_A1:alaIgmpTunnelGroupAddress,_A2:alaIgmpTunnelHostAddress,_A3:alaIgmpTunnelDestAddress,_A4:alaIgmpTunnelOrigAddress,_B2:alaIgmpTunnelType,_A5:alaIgmpTunnelNextDestAddress,_B3:alaIgmpTunnelNextType,'alaIgmpPort':alaIgmpPort,'alaIgmpPortTable':alaIgmpPortTable,'alaIgmpPortEntry':alaIgmpPortEntry,_T:alaIgmpPortIfIndex,_B4:alaIgmpPortMaxGroupLimit,_B5:alaIgmpPortMaxGroupExceedAction,'alaIgmpPortVlan':alaIgmpPortVlan,'alaIgmpPortVlanTable':alaIgmpPortVlanTable,'alaIgmpPortVlanEntry':alaIgmpPortVlanEntry,_A6:alaIgmpVlanId,_B6:alaIgmpPortVlanCurrentGroupCount,_B7:alaIgmpPortVlanMaxGroupLimit,_B8:alaIgmpPortVlanMaxGroupExceedAction,'alcatelIND1IgmpMIBConformance':alcatelIND1IgmpMIBConformance,'alcatelIND1IgmpMIBCompliances':alcatelIND1IgmpMIBCompliances,'alaIgmpCompliance':alaIgmpCompliance,'alcatelIND1IgmpMIBGroups':alcatelIND1IgmpMIBGroups,_B9:alaIgmpGroup,_BA:alaIgmpVlanGroup,_BB:alaIgmpMemberGroup,_BC:alaIgmpStaticMemberGroup,_BD:alaIgmpNeighborGroup,_BE:alaIgmpStaticNeighborGroup,_BF:alaIgmpQuerierGroup,_BG:alaIgmpStaticQuerierGroup,_BH:alaIgmpSourceGroup,_BI:alaIgmpForwardGroup,_BJ:alaIgmpTunnelGroup,_BK:alaIgmpPortGroup,_BL:alaIgmpPortVlanGroup})