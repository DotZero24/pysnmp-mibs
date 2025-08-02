_AO='alaIpMcastMIBMRouteBasicGroup'
_AN='alaIpMcastMIBBasicGroup'
_AM='alaIpMcastRouteDifferentInIfOctets'
_AL='alaIpMcastRouteNextHopOctets'
_AK='alaIpMcastInterfaceOutMcastPkts'
_AJ='alaIpMcastInterfaceInMcastPkts'
_AI='alaIpMcastBoundaryDroppedMcastPkts'
_AH='alaIpMcastBoundaryDroppedMcastOctets'
_AG='alaIpMcastBoundaryStorageType'
_AF='alaIpMcastBoundaryStatus'
_AE='alaIpMcastRouteTtlDropOctets'
_AD='alaIpMcastRouteTtlDropPackets'
_AC='alaIpMcastRouteDifferentInIfPackets'
_AB='alaIpMcastRoutePkts'
_AA='alaIpMcastRouteRtType'
_A9='alaIpMcastRouteRtPrefixLength'
_A8='alaIpMcastRouteRtAddress'
_A7='alaIpMcastRouteRtAddressType'
_A6='alaIpMcastRouteRtProtocol'
_A5='alaIpMcastRouteProtocol'
_A4='alaIpMcastBoundaryHCDroppedMcastPkts'
_A3='alaIpMcastBoundaryHCDroppedMcastOctets'
_A2='alaIpMcastRouteHCOctets'
_A1='alaIpMcastInterfaceHCOutMcastPkts'
_A0='alaIpMcastInterfaceHCInMcastPkts'
_z='alaIpMcastInterfaceHCOutMcastOctets'
_y='alaIpMcastInterfaceHCInMcastOctets'
_x='alaIpMcastRouteNextHopClosestMemberHops'
_w='alaIpMcastInterfaceProtocol'
_v='read-create'
_u='alaIpMcastBoundaryAddressPrefixLength'
_t='alaIpMcastBoundaryAddress'
_s='alaIpMcastBoundaryAddressType'
_r='alaIpMcastBoundaryIfIndex'
_q='alaIpMcastInterfaceIfIndex'
_p='alaIpMcastRouteNextHopAddress'
_o='alaIpMcastRouteNextHopAddressType'
_n='alaIpMcastRouteNextHopIfIndex'
_m='alaIpMcastRouteNextHopSourcePrefixLength'
_l='alaIpMcastRouteNextHopSource'
_k='alaIpMcastRouteNextHopSourceAddressType'
_j='alaIpMcastRouteNextHopGroup'
_i='alaIpMcastRouteNextHopGroupAddressType'
_h='alaIpMcastRouteSourcePrefixLength'
_g='alaIpMcastRouteSource'
_f='alaIpMcastRouteSourceAddressType'
_e='alaIpMcastRouteGroupPrefixLength'
_d='alaIpMcastRouteGroup'
_c='alaIpMcastRouteGroupAddressType'
_b='StorageType'
_a='alaIpMcastRouteOctets'
_Z='alaIpMcastInterfaceOutMcastOctets'
_Y='alaIpMcastInterfaceInMcastOctets'
_X='alaIpMcastInterfaceRateLimit'
_W='alaIpMcastInterfaceTtl'
_V='alaIpMcastRouteNextHopProtocol'
_U='alaIpMcastRouteNextHopExpiryTime'
_T='alaIpMcastRouteNextHopTimeStamp'
_S='alaIpMcastRouteNextHopState'
_R='alaIpMcastRouteExpiryTime'
_Q='alaIpMcastRouteTimeStamp'
_P='alaIpMcastRouteInIfIndex'
_O='alaIpMcastRouteUpstreamNeighbor'
_N='alaIpMcastRouteUpstreamNeighborType'
_M='alaIpMcastRouteEntryCount'
_L='alaIpMcastEnable'
_K='deprecated'
_J='alaIpMcastRouteNextHopPkts'
_I='read-write'
_H='Unsigned32'
_G='Integer32'
_F='InetAddressPrefixLength'
_E='InetAddress'
_D='not-accessible'
_C='read-only'
_B='current'
_A='ALCATEL-IND1-IPMCAST-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Ipmrm,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','routingIND1Ipmrm')
IANAipMRouteProtocol,IANAipRouteProtocol=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipMRouteProtocol','IANAipRouteProtocol')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_E,_F,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_b,'TextualConvention','TimeStamp')
alaIpMcastMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,10,2))
if mibBuilder.loadTexts:alaIpMcastMIB.setRevisions(('2007-07-02 00:00',))
_AlaIpMcastMIBObjects_ObjectIdentity=ObjectIdentity
alaIpMcastMIBObjects=_AlaIpMcastMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1))
_AlaIpMcast_ObjectIdentity=ObjectIdentity
alaIpMcast=_AlaIpMcast_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1))
class _AlaIpMcastEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_AlaIpMcastEnable_Type.__name__=_G
_AlaIpMcastEnable_Object=MibScalar
alaIpMcastEnable=_AlaIpMcastEnable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,1),_AlaIpMcastEnable_Type())
alaIpMcastEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:alaIpMcastEnable.setStatus(_B)
_AlaIpMcastRouteTable_Object=MibTable
alaIpMcastRouteTable=_AlaIpMcastRouteTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2))
if mibBuilder.loadTexts:alaIpMcastRouteTable.setStatus(_B)
_AlaIpMcastRouteEntry_Object=MibTableRow
alaIpMcastRouteEntry=_AlaIpMcastRouteEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1))
alaIpMcastRouteEntry.setIndexNames((0,_A,_c),(0,_A,_d),(0,_A,_e),(0,_A,_f),(0,_A,_g),(0,_A,_h))
if mibBuilder.loadTexts:alaIpMcastRouteEntry.setStatus(_B)
_AlaIpMcastRouteGroupAddressType_Type=InetAddressType
_AlaIpMcastRouteGroupAddressType_Object=MibTableColumn
alaIpMcastRouteGroupAddressType=_AlaIpMcastRouteGroupAddressType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,1),_AlaIpMcastRouteGroupAddressType_Type())
alaIpMcastRouteGroupAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastRouteGroupAddressType.setStatus(_B)
class _AlaIpMcastRouteGroup_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_AlaIpMcastRouteGroup_Type.__name__=_E
_AlaIpMcastRouteGroup_Object=MibTableColumn
alaIpMcastRouteGroup=_AlaIpMcastRouteGroup_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,2),_AlaIpMcastRouteGroup_Type())
alaIpMcastRouteGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastRouteGroup.setStatus(_B)
class _AlaIpMcastRouteGroupPrefixLength_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,128))
_AlaIpMcastRouteGroupPrefixLength_Type.__name__=_F
_AlaIpMcastRouteGroupPrefixLength_Object=MibTableColumn
alaIpMcastRouteGroupPrefixLength=_AlaIpMcastRouteGroupPrefixLength_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,3),_AlaIpMcastRouteGroupPrefixLength_Type())
alaIpMcastRouteGroupPrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastRouteGroupPrefixLength.setStatus(_B)
_AlaIpMcastRouteSourceAddressType_Type=InetAddressType
_AlaIpMcastRouteSourceAddressType_Object=MibTableColumn
alaIpMcastRouteSourceAddressType=_AlaIpMcastRouteSourceAddressType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,4),_AlaIpMcastRouteSourceAddressType_Type())
alaIpMcastRouteSourceAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastRouteSourceAddressType.setStatus(_B)
class _AlaIpMcastRouteSource_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_AlaIpMcastRouteSource_Type.__name__=_E
_AlaIpMcastRouteSource_Object=MibTableColumn
alaIpMcastRouteSource=_AlaIpMcastRouteSource_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,5),_AlaIpMcastRouteSource_Type())
alaIpMcastRouteSource.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastRouteSource.setStatus(_B)
class _AlaIpMcastRouteSourcePrefixLength_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,128))
_AlaIpMcastRouteSourcePrefixLength_Type.__name__=_F
_AlaIpMcastRouteSourcePrefixLength_Object=MibTableColumn
alaIpMcastRouteSourcePrefixLength=_AlaIpMcastRouteSourcePrefixLength_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,6),_AlaIpMcastRouteSourcePrefixLength_Type())
alaIpMcastRouteSourcePrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastRouteSourcePrefixLength.setStatus(_B)
_AlaIpMcastRouteUpstreamNeighborType_Type=InetAddressType
_AlaIpMcastRouteUpstreamNeighborType_Object=MibTableColumn
alaIpMcastRouteUpstreamNeighborType=_AlaIpMcastRouteUpstreamNeighborType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,7),_AlaIpMcastRouteUpstreamNeighborType_Type())
alaIpMcastRouteUpstreamNeighborType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteUpstreamNeighborType.setStatus(_B)
_AlaIpMcastRouteUpstreamNeighbor_Type=InetAddress
_AlaIpMcastRouteUpstreamNeighbor_Object=MibTableColumn
alaIpMcastRouteUpstreamNeighbor=_AlaIpMcastRouteUpstreamNeighbor_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,8),_AlaIpMcastRouteUpstreamNeighbor_Type())
alaIpMcastRouteUpstreamNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteUpstreamNeighbor.setStatus(_B)
_AlaIpMcastRouteInIfIndex_Type=InterfaceIndexOrZero
_AlaIpMcastRouteInIfIndex_Object=MibTableColumn
alaIpMcastRouteInIfIndex=_AlaIpMcastRouteInIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,9),_AlaIpMcastRouteInIfIndex_Type())
alaIpMcastRouteInIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteInIfIndex.setStatus(_B)
_AlaIpMcastRouteTimeStamp_Type=TimeStamp
_AlaIpMcastRouteTimeStamp_Object=MibTableColumn
alaIpMcastRouteTimeStamp=_AlaIpMcastRouteTimeStamp_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,10),_AlaIpMcastRouteTimeStamp_Type())
alaIpMcastRouteTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteTimeStamp.setStatus(_B)
_AlaIpMcastRouteExpiryTime_Type=TimeTicks
_AlaIpMcastRouteExpiryTime_Object=MibTableColumn
alaIpMcastRouteExpiryTime=_AlaIpMcastRouteExpiryTime_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,11),_AlaIpMcastRouteExpiryTime_Type())
alaIpMcastRouteExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteExpiryTime.setStatus(_B)
_AlaIpMcastRoutePkts_Type=Counter32
_AlaIpMcastRoutePkts_Object=MibTableColumn
alaIpMcastRoutePkts=_AlaIpMcastRoutePkts_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,12),_AlaIpMcastRoutePkts_Type())
alaIpMcastRoutePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRoutePkts.setStatus(_B)
_AlaIpMcastRouteDifferentInIfPackets_Type=Counter32
_AlaIpMcastRouteDifferentInIfPackets_Object=MibTableColumn
alaIpMcastRouteDifferentInIfPackets=_AlaIpMcastRouteDifferentInIfPackets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,13),_AlaIpMcastRouteDifferentInIfPackets_Type())
alaIpMcastRouteDifferentInIfPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteDifferentInIfPackets.setStatus(_B)
_AlaIpMcastRouteOctets_Type=Counter32
_AlaIpMcastRouteOctets_Object=MibTableColumn
alaIpMcastRouteOctets=_AlaIpMcastRouteOctets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,14),_AlaIpMcastRouteOctets_Type())
alaIpMcastRouteOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteOctets.setStatus(_B)
_AlaIpMcastRouteProtocol_Type=IANAipMRouteProtocol
_AlaIpMcastRouteProtocol_Object=MibTableColumn
alaIpMcastRouteProtocol=_AlaIpMcastRouteProtocol_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,15),_AlaIpMcastRouteProtocol_Type())
alaIpMcastRouteProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteProtocol.setStatus(_B)
_AlaIpMcastRouteRtProtocol_Type=IANAipRouteProtocol
_AlaIpMcastRouteRtProtocol_Object=MibTableColumn
alaIpMcastRouteRtProtocol=_AlaIpMcastRouteRtProtocol_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,16),_AlaIpMcastRouteRtProtocol_Type())
alaIpMcastRouteRtProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteRtProtocol.setStatus(_B)
_AlaIpMcastRouteRtAddressType_Type=InetAddressType
_AlaIpMcastRouteRtAddressType_Object=MibTableColumn
alaIpMcastRouteRtAddressType=_AlaIpMcastRouteRtAddressType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,17),_AlaIpMcastRouteRtAddressType_Type())
alaIpMcastRouteRtAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteRtAddressType.setStatus(_B)
_AlaIpMcastRouteRtAddress_Type=InetAddress
_AlaIpMcastRouteRtAddress_Object=MibTableColumn
alaIpMcastRouteRtAddress=_AlaIpMcastRouteRtAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,18),_AlaIpMcastRouteRtAddress_Type())
alaIpMcastRouteRtAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteRtAddress.setStatus(_B)
class _AlaIpMcastRouteRtPrefixLength_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,128))
_AlaIpMcastRouteRtPrefixLength_Type.__name__=_F
_AlaIpMcastRouteRtPrefixLength_Object=MibTableColumn
alaIpMcastRouteRtPrefixLength=_AlaIpMcastRouteRtPrefixLength_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,19),_AlaIpMcastRouteRtPrefixLength_Type())
alaIpMcastRouteRtPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteRtPrefixLength.setStatus(_B)
class _AlaIpMcastRouteRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('multicast',2)))
_AlaIpMcastRouteRtType_Type.__name__=_G
_AlaIpMcastRouteRtType_Object=MibTableColumn
alaIpMcastRouteRtType=_AlaIpMcastRouteRtType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,20),_AlaIpMcastRouteRtType_Type())
alaIpMcastRouteRtType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteRtType.setStatus(_B)
_AlaIpMcastRouteHCOctets_Type=Counter64
_AlaIpMcastRouteHCOctets_Object=MibTableColumn
alaIpMcastRouteHCOctets=_AlaIpMcastRouteHCOctets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,21),_AlaIpMcastRouteHCOctets_Type())
alaIpMcastRouteHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteHCOctets.setStatus(_B)
_AlaIpMcastRouteDifferentInIfOctets_Type=Counter32
_AlaIpMcastRouteDifferentInIfOctets_Object=MibTableColumn
alaIpMcastRouteDifferentInIfOctets=_AlaIpMcastRouteDifferentInIfOctets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,22),_AlaIpMcastRouteDifferentInIfOctets_Type())
alaIpMcastRouteDifferentInIfOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteDifferentInIfOctets.setStatus(_B)
_AlaIpMcastRouteTtlDropPackets_Type=Counter32
_AlaIpMcastRouteTtlDropPackets_Object=MibTableColumn
alaIpMcastRouteTtlDropPackets=_AlaIpMcastRouteTtlDropPackets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,23),_AlaIpMcastRouteTtlDropPackets_Type())
alaIpMcastRouteTtlDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteTtlDropPackets.setStatus(_B)
_AlaIpMcastRouteTtlDropOctets_Type=Counter32
_AlaIpMcastRouteTtlDropOctets_Object=MibTableColumn
alaIpMcastRouteTtlDropOctets=_AlaIpMcastRouteTtlDropOctets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,2,1,24),_AlaIpMcastRouteTtlDropOctets_Type())
alaIpMcastRouteTtlDropOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteTtlDropOctets.setStatus(_B)
_AlaIpMcastRouteNextHopTable_Object=MibTable
alaIpMcastRouteNextHopTable=_AlaIpMcastRouteNextHopTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3))
if mibBuilder.loadTexts:alaIpMcastRouteNextHopTable.setStatus(_B)
_AlaIpMcastRouteNextHopEntry_Object=MibTableRow
alaIpMcastRouteNextHopEntry=_AlaIpMcastRouteNextHopEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1))
alaIpMcastRouteNextHopEntry.setIndexNames((0,_A,_i),(0,_A,_j),(0,_A,_k),(0,_A,_l),(0,_A,_m),(0,_A,_n),(0,_A,_o),(0,_A,_p))
if mibBuilder.loadTexts:alaIpMcastRouteNextHopEntry.setStatus(_B)
_AlaIpMcastRouteNextHopGroupAddressType_Type=InetAddressType
_AlaIpMcastRouteNextHopGroupAddressType_Object=MibTableColumn
alaIpMcastRouteNextHopGroupAddressType=_AlaIpMcastRouteNextHopGroupAddressType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1,1),_AlaIpMcastRouteNextHopGroupAddressType_Type())
alaIpMcastRouteNextHopGroupAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastRouteNextHopGroupAddressType.setStatus(_B)
class _AlaIpMcastRouteNextHopGroup_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_AlaIpMcastRouteNextHopGroup_Type.__name__=_E
_AlaIpMcastRouteNextHopGroup_Object=MibTableColumn
alaIpMcastRouteNextHopGroup=_AlaIpMcastRouteNextHopGroup_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1,2),_AlaIpMcastRouteNextHopGroup_Type())
alaIpMcastRouteNextHopGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastRouteNextHopGroup.setStatus(_B)
_AlaIpMcastRouteNextHopSourceAddressType_Type=InetAddressType
_AlaIpMcastRouteNextHopSourceAddressType_Object=MibTableColumn
alaIpMcastRouteNextHopSourceAddressType=_AlaIpMcastRouteNextHopSourceAddressType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1,3),_AlaIpMcastRouteNextHopSourceAddressType_Type())
alaIpMcastRouteNextHopSourceAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastRouteNextHopSourceAddressType.setStatus(_B)
class _AlaIpMcastRouteNextHopSource_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_AlaIpMcastRouteNextHopSource_Type.__name__=_E
_AlaIpMcastRouteNextHopSource_Object=MibTableColumn
alaIpMcastRouteNextHopSource=_AlaIpMcastRouteNextHopSource_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1,4),_AlaIpMcastRouteNextHopSource_Type())
alaIpMcastRouteNextHopSource.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastRouteNextHopSource.setStatus(_B)
class _AlaIpMcastRouteNextHopSourcePrefixLength_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,128))
_AlaIpMcastRouteNextHopSourcePrefixLength_Type.__name__=_F
_AlaIpMcastRouteNextHopSourcePrefixLength_Object=MibTableColumn
alaIpMcastRouteNextHopSourcePrefixLength=_AlaIpMcastRouteNextHopSourcePrefixLength_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1,5),_AlaIpMcastRouteNextHopSourcePrefixLength_Type())
alaIpMcastRouteNextHopSourcePrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastRouteNextHopSourcePrefixLength.setStatus(_B)
_AlaIpMcastRouteNextHopIfIndex_Type=InterfaceIndex
_AlaIpMcastRouteNextHopIfIndex_Object=MibTableColumn
alaIpMcastRouteNextHopIfIndex=_AlaIpMcastRouteNextHopIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1,6),_AlaIpMcastRouteNextHopIfIndex_Type())
alaIpMcastRouteNextHopIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastRouteNextHopIfIndex.setStatus(_B)
_AlaIpMcastRouteNextHopAddressType_Type=InetAddressType
_AlaIpMcastRouteNextHopAddressType_Object=MibTableColumn
alaIpMcastRouteNextHopAddressType=_AlaIpMcastRouteNextHopAddressType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1,7),_AlaIpMcastRouteNextHopAddressType_Type())
alaIpMcastRouteNextHopAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastRouteNextHopAddressType.setStatus(_B)
class _AlaIpMcastRouteNextHopAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_AlaIpMcastRouteNextHopAddress_Type.__name__=_E
_AlaIpMcastRouteNextHopAddress_Object=MibTableColumn
alaIpMcastRouteNextHopAddress=_AlaIpMcastRouteNextHopAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1,8),_AlaIpMcastRouteNextHopAddress_Type())
alaIpMcastRouteNextHopAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastRouteNextHopAddress.setStatus(_B)
class _AlaIpMcastRouteNextHopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pruned',1),('forwarding',2)))
_AlaIpMcastRouteNextHopState_Type.__name__=_G
_AlaIpMcastRouteNextHopState_Object=MibTableColumn
alaIpMcastRouteNextHopState=_AlaIpMcastRouteNextHopState_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1,9),_AlaIpMcastRouteNextHopState_Type())
alaIpMcastRouteNextHopState.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteNextHopState.setStatus(_B)
_AlaIpMcastRouteNextHopTimeStamp_Type=TimeStamp
_AlaIpMcastRouteNextHopTimeStamp_Object=MibTableColumn
alaIpMcastRouteNextHopTimeStamp=_AlaIpMcastRouteNextHopTimeStamp_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1,10),_AlaIpMcastRouteNextHopTimeStamp_Type())
alaIpMcastRouteNextHopTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteNextHopTimeStamp.setStatus(_B)
_AlaIpMcastRouteNextHopExpiryTime_Type=TimeTicks
_AlaIpMcastRouteNextHopExpiryTime_Object=MibTableColumn
alaIpMcastRouteNextHopExpiryTime=_AlaIpMcastRouteNextHopExpiryTime_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1,11),_AlaIpMcastRouteNextHopExpiryTime_Type())
alaIpMcastRouteNextHopExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteNextHopExpiryTime.setStatus(_B)
class _AlaIpMcastRouteNextHopClosestMemberHops_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaIpMcastRouteNextHopClosestMemberHops_Type.__name__=_H
_AlaIpMcastRouteNextHopClosestMemberHops_Object=MibTableColumn
alaIpMcastRouteNextHopClosestMemberHops=_AlaIpMcastRouteNextHopClosestMemberHops_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1,12),_AlaIpMcastRouteNextHopClosestMemberHops_Type())
alaIpMcastRouteNextHopClosestMemberHops.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteNextHopClosestMemberHops.setStatus(_B)
_AlaIpMcastRouteNextHopProtocol_Type=IANAipMRouteProtocol
_AlaIpMcastRouteNextHopProtocol_Object=MibTableColumn
alaIpMcastRouteNextHopProtocol=_AlaIpMcastRouteNextHopProtocol_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1,13),_AlaIpMcastRouteNextHopProtocol_Type())
alaIpMcastRouteNextHopProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteNextHopProtocol.setStatus(_B)
_AlaIpMcastRouteNextHopPkts_Type=Counter32
_AlaIpMcastRouteNextHopPkts_Object=MibTableColumn
alaIpMcastRouteNextHopPkts=_AlaIpMcastRouteNextHopPkts_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1,14),_AlaIpMcastRouteNextHopPkts_Type())
alaIpMcastRouteNextHopPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteNextHopPkts.setStatus(_B)
_AlaIpMcastRouteNextHopOctets_Type=Counter32
_AlaIpMcastRouteNextHopOctets_Object=MibTableColumn
alaIpMcastRouteNextHopOctets=_AlaIpMcastRouteNextHopOctets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,3,1,15),_AlaIpMcastRouteNextHopOctets_Type())
alaIpMcastRouteNextHopOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteNextHopOctets.setStatus(_B)
_AlaIpMcastInterfaceTable_Object=MibTable
alaIpMcastInterfaceTable=_AlaIpMcastInterfaceTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,4))
if mibBuilder.loadTexts:alaIpMcastInterfaceTable.setStatus(_B)
_AlaIpMcastInterfaceEntry_Object=MibTableRow
alaIpMcastInterfaceEntry=_AlaIpMcastInterfaceEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,4,1))
alaIpMcastInterfaceEntry.setIndexNames((0,_A,_q))
if mibBuilder.loadTexts:alaIpMcastInterfaceEntry.setStatus(_B)
_AlaIpMcastInterfaceIfIndex_Type=InterfaceIndex
_AlaIpMcastInterfaceIfIndex_Object=MibTableColumn
alaIpMcastInterfaceIfIndex=_AlaIpMcastInterfaceIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,4,1,1),_AlaIpMcastInterfaceIfIndex_Type())
alaIpMcastInterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastInterfaceIfIndex.setStatus(_B)
class _AlaIpMcastInterfaceTtl_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaIpMcastInterfaceTtl_Type.__name__=_H
_AlaIpMcastInterfaceTtl_Object=MibTableColumn
alaIpMcastInterfaceTtl=_AlaIpMcastInterfaceTtl_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,4,1,2),_AlaIpMcastInterfaceTtl_Type())
alaIpMcastInterfaceTtl.setMaxAccess(_I)
if mibBuilder.loadTexts:alaIpMcastInterfaceTtl.setStatus(_B)
_AlaIpMcastInterfaceProtocol_Type=IANAipMRouteProtocol
_AlaIpMcastInterfaceProtocol_Object=MibTableColumn
alaIpMcastInterfaceProtocol=_AlaIpMcastInterfaceProtocol_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,4,1,3),_AlaIpMcastInterfaceProtocol_Type())
alaIpMcastInterfaceProtocol.setMaxAccess(_I)
if mibBuilder.loadTexts:alaIpMcastInterfaceProtocol.setStatus(_K)
class _AlaIpMcastInterfaceRateLimit_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlaIpMcastInterfaceRateLimit_Type.__name__=_H
_AlaIpMcastInterfaceRateLimit_Object=MibTableColumn
alaIpMcastInterfaceRateLimit=_AlaIpMcastInterfaceRateLimit_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,4,1,4),_AlaIpMcastInterfaceRateLimit_Type())
alaIpMcastInterfaceRateLimit.setMaxAccess(_I)
if mibBuilder.loadTexts:alaIpMcastInterfaceRateLimit.setStatus(_B)
_AlaIpMcastInterfaceInMcastOctets_Type=Counter32
_AlaIpMcastInterfaceInMcastOctets_Object=MibTableColumn
alaIpMcastInterfaceInMcastOctets=_AlaIpMcastInterfaceInMcastOctets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,4,1,5),_AlaIpMcastInterfaceInMcastOctets_Type())
alaIpMcastInterfaceInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastInterfaceInMcastOctets.setStatus(_B)
_AlaIpMcastInterfaceOutMcastOctets_Type=Counter32
_AlaIpMcastInterfaceOutMcastOctets_Object=MibTableColumn
alaIpMcastInterfaceOutMcastOctets=_AlaIpMcastInterfaceOutMcastOctets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,4,1,6),_AlaIpMcastInterfaceOutMcastOctets_Type())
alaIpMcastInterfaceOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastInterfaceOutMcastOctets.setStatus(_B)
_AlaIpMcastInterfaceInMcastPkts_Type=Counter32
_AlaIpMcastInterfaceInMcastPkts_Object=MibTableColumn
alaIpMcastInterfaceInMcastPkts=_AlaIpMcastInterfaceInMcastPkts_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,4,1,7),_AlaIpMcastInterfaceInMcastPkts_Type())
alaIpMcastInterfaceInMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastInterfaceInMcastPkts.setStatus(_B)
_AlaIpMcastInterfaceOutMcastPkts_Type=Counter32
_AlaIpMcastInterfaceOutMcastPkts_Object=MibTableColumn
alaIpMcastInterfaceOutMcastPkts=_AlaIpMcastInterfaceOutMcastPkts_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,4,1,8),_AlaIpMcastInterfaceOutMcastPkts_Type())
alaIpMcastInterfaceOutMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastInterfaceOutMcastPkts.setStatus(_B)
_AlaIpMcastInterfaceHCInMcastOctets_Type=Counter64
_AlaIpMcastInterfaceHCInMcastOctets_Object=MibTableColumn
alaIpMcastInterfaceHCInMcastOctets=_AlaIpMcastInterfaceHCInMcastOctets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,4,1,9),_AlaIpMcastInterfaceHCInMcastOctets_Type())
alaIpMcastInterfaceHCInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastInterfaceHCInMcastOctets.setStatus(_B)
_AlaIpMcastInterfaceHCOutMcastOctets_Type=Counter64
_AlaIpMcastInterfaceHCOutMcastOctets_Object=MibTableColumn
alaIpMcastInterfaceHCOutMcastOctets=_AlaIpMcastInterfaceHCOutMcastOctets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,4,1,10),_AlaIpMcastInterfaceHCOutMcastOctets_Type())
alaIpMcastInterfaceHCOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastInterfaceHCOutMcastOctets.setStatus(_B)
_AlaIpMcastInterfaceHCInMcastPkts_Type=Counter64
_AlaIpMcastInterfaceHCInMcastPkts_Object=MibTableColumn
alaIpMcastInterfaceHCInMcastPkts=_AlaIpMcastInterfaceHCInMcastPkts_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,4,1,11),_AlaIpMcastInterfaceHCInMcastPkts_Type())
alaIpMcastInterfaceHCInMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastInterfaceHCInMcastPkts.setStatus(_B)
_AlaIpMcastInterfaceHCOutMcastPkts_Type=Counter64
_AlaIpMcastInterfaceHCOutMcastPkts_Object=MibTableColumn
alaIpMcastInterfaceHCOutMcastPkts=_AlaIpMcastInterfaceHCOutMcastPkts_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,4,1,12),_AlaIpMcastInterfaceHCOutMcastPkts_Type())
alaIpMcastInterfaceHCOutMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastInterfaceHCOutMcastPkts.setStatus(_B)
_AlaIpMcastBoundaryTable_Object=MibTable
alaIpMcastBoundaryTable=_AlaIpMcastBoundaryTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,5))
if mibBuilder.loadTexts:alaIpMcastBoundaryTable.setStatus(_B)
_AlaIpMcastBoundaryEntry_Object=MibTableRow
alaIpMcastBoundaryEntry=_AlaIpMcastBoundaryEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,5,1))
alaIpMcastBoundaryEntry.setIndexNames((0,_A,_r),(0,_A,_s),(0,_A,_t),(0,_A,_u))
if mibBuilder.loadTexts:alaIpMcastBoundaryEntry.setStatus(_B)
_AlaIpMcastBoundaryIfIndex_Type=InterfaceIndex
_AlaIpMcastBoundaryIfIndex_Object=MibTableColumn
alaIpMcastBoundaryIfIndex=_AlaIpMcastBoundaryIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,5,1,1),_AlaIpMcastBoundaryIfIndex_Type())
alaIpMcastBoundaryIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastBoundaryIfIndex.setStatus(_B)
_AlaIpMcastBoundaryAddressType_Type=InetAddressType
_AlaIpMcastBoundaryAddressType_Object=MibTableColumn
alaIpMcastBoundaryAddressType=_AlaIpMcastBoundaryAddressType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,5,1,2),_AlaIpMcastBoundaryAddressType_Type())
alaIpMcastBoundaryAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastBoundaryAddressType.setStatus(_B)
class _AlaIpMcastBoundaryAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_AlaIpMcastBoundaryAddress_Type.__name__=_E
_AlaIpMcastBoundaryAddress_Object=MibTableColumn
alaIpMcastBoundaryAddress=_AlaIpMcastBoundaryAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,5,1,3),_AlaIpMcastBoundaryAddress_Type())
alaIpMcastBoundaryAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastBoundaryAddress.setStatus(_B)
class _AlaIpMcastBoundaryAddressPrefixLength_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,32))
_AlaIpMcastBoundaryAddressPrefixLength_Type.__name__=_F
_AlaIpMcastBoundaryAddressPrefixLength_Object=MibTableColumn
alaIpMcastBoundaryAddressPrefixLength=_AlaIpMcastBoundaryAddressPrefixLength_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,5,1,4),_AlaIpMcastBoundaryAddressPrefixLength_Type())
alaIpMcastBoundaryAddressPrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIpMcastBoundaryAddressPrefixLength.setStatus(_B)
_AlaIpMcastBoundaryStatus_Type=RowStatus
_AlaIpMcastBoundaryStatus_Object=MibTableColumn
alaIpMcastBoundaryStatus=_AlaIpMcastBoundaryStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,5,1,5),_AlaIpMcastBoundaryStatus_Type())
alaIpMcastBoundaryStatus.setMaxAccess(_v)
if mibBuilder.loadTexts:alaIpMcastBoundaryStatus.setStatus(_B)
class _AlaIpMcastBoundaryStorageType_Type(StorageType):defaultValue=3
_AlaIpMcastBoundaryStorageType_Type.__name__=_b
_AlaIpMcastBoundaryStorageType_Object=MibTableColumn
alaIpMcastBoundaryStorageType=_AlaIpMcastBoundaryStorageType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,5,1,6),_AlaIpMcastBoundaryStorageType_Type())
alaIpMcastBoundaryStorageType.setMaxAccess(_v)
if mibBuilder.loadTexts:alaIpMcastBoundaryStorageType.setStatus(_B)
_AlaIpMcastBoundaryDroppedMcastOctets_Type=Counter32
_AlaIpMcastBoundaryDroppedMcastOctets_Object=MibTableColumn
alaIpMcastBoundaryDroppedMcastOctets=_AlaIpMcastBoundaryDroppedMcastOctets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,5,1,7),_AlaIpMcastBoundaryDroppedMcastOctets_Type())
alaIpMcastBoundaryDroppedMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastBoundaryDroppedMcastOctets.setStatus(_B)
_AlaIpMcastBoundaryDroppedMcastPkts_Type=Counter32
_AlaIpMcastBoundaryDroppedMcastPkts_Object=MibTableColumn
alaIpMcastBoundaryDroppedMcastPkts=_AlaIpMcastBoundaryDroppedMcastPkts_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,5,1,8),_AlaIpMcastBoundaryDroppedMcastPkts_Type())
alaIpMcastBoundaryDroppedMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastBoundaryDroppedMcastPkts.setStatus(_B)
_AlaIpMcastBoundaryHCDroppedMcastOctets_Type=Counter64
_AlaIpMcastBoundaryHCDroppedMcastOctets_Object=MibTableColumn
alaIpMcastBoundaryHCDroppedMcastOctets=_AlaIpMcastBoundaryHCDroppedMcastOctets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,5,1,9),_AlaIpMcastBoundaryHCDroppedMcastOctets_Type())
alaIpMcastBoundaryHCDroppedMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastBoundaryHCDroppedMcastOctets.setStatus(_B)
_AlaIpMcastBoundaryHCDroppedMcastPkts_Type=Counter64
_AlaIpMcastBoundaryHCDroppedMcastPkts_Object=MibTableColumn
alaIpMcastBoundaryHCDroppedMcastPkts=_AlaIpMcastBoundaryHCDroppedMcastPkts_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,5,1,10),_AlaIpMcastBoundaryHCDroppedMcastPkts_Type())
alaIpMcastBoundaryHCDroppedMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastBoundaryHCDroppedMcastPkts.setStatus(_B)
_AlaIpMcastRouteEntryCount_Type=Gauge32
_AlaIpMcastRouteEntryCount_Object=MibScalar
alaIpMcastRouteEntryCount=_AlaIpMcastRouteEntryCount_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,1,1,7),_AlaIpMcastRouteEntryCount_Type())
alaIpMcastRouteEntryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpMcastRouteEntryCount.setStatus(_B)
_AlaIpMcastMIBConformance_ObjectIdentity=ObjectIdentity
alaIpMcastMIBConformance=_AlaIpMcastMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,2))
_AlaIpMcastMIBCompliances_ObjectIdentity=ObjectIdentity
alaIpMcastMIBCompliances=_AlaIpMcastMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,2,1))
_AlaIpMcastMIBGroups_ObjectIdentity=ObjectIdentity
alaIpMcastMIBGroups=_AlaIpMcastMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,2,2))
alaIpMcastMIBMRouteBasicGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,2,2,1))
alaIpMcastMIBMRouteBasicGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_J),(_A,_W),(_A,_w),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:alaIpMcastMIBMRouteBasicGroup.setStatus(_K)
alaIpMcastMIBHopCountGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,2,2,2))
alaIpMcastMIBHopCountGroup.setObjects((_A,_x))
if mibBuilder.loadTexts:alaIpMcastMIBHopCountGroup.setStatus(_B)
alaIpMcastMIBPktsOutGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,2,2,3))
alaIpMcastMIBPktsOutGroup.setObjects((_A,_J))
if mibBuilder.loadTexts:alaIpMcastMIBPktsOutGroup.setStatus(_B)
alaIpMcastMIBHCInterfaceGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,2,2,4))
alaIpMcastMIBHCInterfaceGroup.setObjects(*((_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:alaIpMcastMIBHCInterfaceGroup.setStatus(_B)
alaIpMcastMIBRouteProtoGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,2,2,5))
alaIpMcastMIBRouteProtoGroup.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:alaIpMcastMIBRouteProtoGroup.setStatus(_B)
alaIpMcastMIBBasicGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,2,2,6))
alaIpMcastMIBBasicGroup.setObjects(*((_A,_L),(_A,_M)))
if mibBuilder.loadTexts:alaIpMcastMIBBasicGroup.setStatus(_B)
alaIpMcastMIBRouteGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,2,2,7))
alaIpMcastMIBRouteGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_AB),(_A,_AC),(_A,_a),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_J),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:alaIpMcastMIBRouteGroup.setStatus(_B)
alaIpMcastMIBBoundaryIfGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,2,2,10))
alaIpMcastMIBBoundaryIfGroup.setObjects(*((_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:alaIpMcastMIBBoundaryIfGroup.setStatus(_B)
alaIpMcastMIBIfPktsGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,2,2,12))
alaIpMcastMIBIfPktsGroup.setObjects(*((_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:alaIpMcastMIBIfPktsGroup.setStatus(_B)
alaIpMcastMIBRouteOctetsGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,2,2,13))
alaIpMcastMIBRouteOctetsGroup.setObjects(*((_A,_a),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:alaIpMcastMIBRouteOctetsGroup.setStatus(_B)
alaIpMcastMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,2,1,1))
alaIpMcastMIBCompliance.setObjects((_A,_AN))
if mibBuilder.loadTexts:alaIpMcastMIBCompliance.setStatus(_B)
alaIpMcastMIBMRouteCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,10,10,2,2,1,2))
alaIpMcastMIBMRouteCompliance.setObjects((_A,_AO))
if mibBuilder.loadTexts:alaIpMcastMIBMRouteCompliance.setStatus(_K)
mibBuilder.exportSymbols(_A,**{'alaIpMcastMIB':alaIpMcastMIB,'alaIpMcastMIBObjects':alaIpMcastMIBObjects,'alaIpMcast':alaIpMcast,_L:alaIpMcastEnable,'alaIpMcastRouteTable':alaIpMcastRouteTable,'alaIpMcastRouteEntry':alaIpMcastRouteEntry,_c:alaIpMcastRouteGroupAddressType,_d:alaIpMcastRouteGroup,_e:alaIpMcastRouteGroupPrefixLength,_f:alaIpMcastRouteSourceAddressType,_g:alaIpMcastRouteSource,_h:alaIpMcastRouteSourcePrefixLength,_N:alaIpMcastRouteUpstreamNeighborType,_O:alaIpMcastRouteUpstreamNeighbor,_P:alaIpMcastRouteInIfIndex,_Q:alaIpMcastRouteTimeStamp,_R:alaIpMcastRouteExpiryTime,_AB:alaIpMcastRoutePkts,_AC:alaIpMcastRouteDifferentInIfPackets,_a:alaIpMcastRouteOctets,_A5:alaIpMcastRouteProtocol,_A6:alaIpMcastRouteRtProtocol,_A7:alaIpMcastRouteRtAddressType,_A8:alaIpMcastRouteRtAddress,_A9:alaIpMcastRouteRtPrefixLength,_AA:alaIpMcastRouteRtType,_A2:alaIpMcastRouteHCOctets,_AM:alaIpMcastRouteDifferentInIfOctets,_AD:alaIpMcastRouteTtlDropPackets,_AE:alaIpMcastRouteTtlDropOctets,'alaIpMcastRouteNextHopTable':alaIpMcastRouteNextHopTable,'alaIpMcastRouteNextHopEntry':alaIpMcastRouteNextHopEntry,_i:alaIpMcastRouteNextHopGroupAddressType,_j:alaIpMcastRouteNextHopGroup,_k:alaIpMcastRouteNextHopSourceAddressType,_l:alaIpMcastRouteNextHopSource,_m:alaIpMcastRouteNextHopSourcePrefixLength,_n:alaIpMcastRouteNextHopIfIndex,_o:alaIpMcastRouteNextHopAddressType,_p:alaIpMcastRouteNextHopAddress,_S:alaIpMcastRouteNextHopState,_T:alaIpMcastRouteNextHopTimeStamp,_U:alaIpMcastRouteNextHopExpiryTime,_x:alaIpMcastRouteNextHopClosestMemberHops,_V:alaIpMcastRouteNextHopProtocol,_J:alaIpMcastRouteNextHopPkts,_AL:alaIpMcastRouteNextHopOctets,'alaIpMcastInterfaceTable':alaIpMcastInterfaceTable,'alaIpMcastInterfaceEntry':alaIpMcastInterfaceEntry,_q:alaIpMcastInterfaceIfIndex,_W:alaIpMcastInterfaceTtl,_w:alaIpMcastInterfaceProtocol,_X:alaIpMcastInterfaceRateLimit,_Y:alaIpMcastInterfaceInMcastOctets,_Z:alaIpMcastInterfaceOutMcastOctets,_AJ:alaIpMcastInterfaceInMcastPkts,_AK:alaIpMcastInterfaceOutMcastPkts,_y:alaIpMcastInterfaceHCInMcastOctets,_z:alaIpMcastInterfaceHCOutMcastOctets,_A0:alaIpMcastInterfaceHCInMcastPkts,_A1:alaIpMcastInterfaceHCOutMcastPkts,'alaIpMcastBoundaryTable':alaIpMcastBoundaryTable,'alaIpMcastBoundaryEntry':alaIpMcastBoundaryEntry,_r:alaIpMcastBoundaryIfIndex,_s:alaIpMcastBoundaryAddressType,_t:alaIpMcastBoundaryAddress,_u:alaIpMcastBoundaryAddressPrefixLength,_AF:alaIpMcastBoundaryStatus,_AG:alaIpMcastBoundaryStorageType,_AH:alaIpMcastBoundaryDroppedMcastOctets,_AI:alaIpMcastBoundaryDroppedMcastPkts,_A3:alaIpMcastBoundaryHCDroppedMcastOctets,_A4:alaIpMcastBoundaryHCDroppedMcastPkts,_M:alaIpMcastRouteEntryCount,'alaIpMcastMIBConformance':alaIpMcastMIBConformance,'alaIpMcastMIBCompliances':alaIpMcastMIBCompliances,'alaIpMcastMIBCompliance':alaIpMcastMIBCompliance,'alaIpMcastMIBMRouteCompliance':alaIpMcastMIBMRouteCompliance,'alaIpMcastMIBGroups':alaIpMcastMIBGroups,_AO:alaIpMcastMIBMRouteBasicGroup,'alaIpMcastMIBHopCountGroup':alaIpMcastMIBHopCountGroup,'alaIpMcastMIBPktsOutGroup':alaIpMcastMIBPktsOutGroup,'alaIpMcastMIBHCInterfaceGroup':alaIpMcastMIBHCInterfaceGroup,'alaIpMcastMIBRouteProtoGroup':alaIpMcastMIBRouteProtoGroup,_AN:alaIpMcastMIBBasicGroup,'alaIpMcastMIBRouteGroup':alaIpMcastMIBRouteGroup,'alaIpMcastMIBBoundaryIfGroup':alaIpMcastMIBBoundaryIfGroup,'alaIpMcastMIBIfPktsGroup':alaIpMcastMIBIfPktsGroup,'alaIpMcastMIBRouteOctetsGroup':alaIpMcastMIBRouteOctetsGroup})