_A3='ipMRouteMIBBoundaryGroup'
_A2='ipMRouteMIBRouteGroup'
_A1='ipMRouteMIBBasicGroup'
_A0='ipMRouteRtType'
_z='ipMRouteRtMask'
_y='ipMRouteRtAddress'
_x='ipMRouteRtProto'
_w='ipMRouteBoundaryStatus'
_v='ipMRouteNextHopClosestMemberHops'
_u='ipMRouteProtocol'
_t='ipMRouteInterfaceOutMcastOctets'
_s='ipMRouteInterfaceInMcastOctets'
_r='ipMRouteInterfaceRateLimit'
_q='ipMRouteInterfaceProtocol'
_p='ipMRouteInterfaceTtl'
_o='ipMRouteNextHopProtocol'
_n='ipMRouteNextHopExpiryTime'
_m='ipMRouteNextHopUpTime'
_l='ipMRouteNextHopState'
_k='ipMRouteOctets'
_j='ipMRouteDifferentInIfPackets'
_i='ipMRoutePkts'
_h='ipMRouteExpiryTime'
_g='ipMRouteUpTime'
_f='ipMRouteInIfIndex'
_e='ipMRouteUpstreamNeighbor'
_d='ipMRouteEnable'
_c='ipMRouteBoundaryAddressMask'
_b='ipMRouteBoundaryAddress'
_a='ipMRouteBoundaryIfIndex'
_Z='ipMRouteInterfaceIfIndex'
_Y='ipMRouteNextHopAddress'
_X='ipMRouteNextHopIfIndex'
_W='ipMRouteNextHopSourceMask'
_V='ipMRouteNextHopSource'
_U='ipMRouteNextHopGroup'
_T='ipMRouteSourceMask'
_S='ipMRouteSource'
_R='ipMRouteGroup'
_Q='ipMRouteNextHopPkts'
_P='igmpOnly'
_O='pimDenseMode'
_N='pimSparseMode'
_M='cbt'
_L='pimSparseDense'
_K='mospf'
_J='read-write'
_I='dvmrp'
_H='netmgmt'
_G='local'
_F='other'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='IPMROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ipMRouteMIB=ModuleIdentity((1,3,6,1,3,60))
if mibBuilder.loadTexts:ipMRouteMIB.setRevisions(('1994-11-04 11:59','1997-01-06 00:00','1997-05-20 00:00','1997-12-18 00:00','1999-02-08 00:00'))
_IpMRouteMIBObjects_ObjectIdentity=ObjectIdentity
ipMRouteMIBObjects=_IpMRouteMIBObjects_ObjectIdentity((1,3,6,1,3,60,1))
_IpMRoute_ObjectIdentity=ObjectIdentity
ipMRoute=_IpMRoute_ObjectIdentity((1,3,6,1,3,60,1,1))
class _IpMRouteEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_IpMRouteEnable_Type.__name__=_D
_IpMRouteEnable_Object=MibScalar
ipMRouteEnable=_IpMRouteEnable_Object((1,3,6,1,3,60,1,1,1),_IpMRouteEnable_Type())
ipMRouteEnable.setMaxAccess(_J)
if mibBuilder.loadTexts:ipMRouteEnable.setStatus(_A)
_IpMRouteTable_Object=MibTable
ipMRouteTable=_IpMRouteTable_Object((1,3,6,1,3,60,1,1,2))
if mibBuilder.loadTexts:ipMRouteTable.setStatus(_A)
_IpMRouteEntry_Object=MibTableRow
ipMRouteEntry=_IpMRouteEntry_Object((1,3,6,1,3,60,1,1,2,1))
ipMRouteEntry.setIndexNames((0,_B,_R),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:ipMRouteEntry.setStatus(_A)
_IpMRouteGroup_Type=IpAddress
_IpMRouteGroup_Object=MibTableColumn
ipMRouteGroup=_IpMRouteGroup_Object((1,3,6,1,3,60,1,1,2,1,1),_IpMRouteGroup_Type())
ipMRouteGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteGroup.setStatus(_A)
_IpMRouteSource_Type=IpAddress
_IpMRouteSource_Object=MibTableColumn
ipMRouteSource=_IpMRouteSource_Object((1,3,6,1,3,60,1,1,2,1,2),_IpMRouteSource_Type())
ipMRouteSource.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteSource.setStatus(_A)
_IpMRouteSourceMask_Type=IpAddress
_IpMRouteSourceMask_Object=MibTableColumn
ipMRouteSourceMask=_IpMRouteSourceMask_Object((1,3,6,1,3,60,1,1,2,1,3),_IpMRouteSourceMask_Type())
ipMRouteSourceMask.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteSourceMask.setStatus(_A)
_IpMRouteUpstreamNeighbor_Type=IpAddress
_IpMRouteUpstreamNeighbor_Object=MibTableColumn
ipMRouteUpstreamNeighbor=_IpMRouteUpstreamNeighbor_Object((1,3,6,1,3,60,1,1,2,1,4),_IpMRouteUpstreamNeighbor_Type())
ipMRouteUpstreamNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteUpstreamNeighbor.setStatus(_A)
_IpMRouteInIfIndex_Type=Integer32
_IpMRouteInIfIndex_Object=MibTableColumn
ipMRouteInIfIndex=_IpMRouteInIfIndex_Object((1,3,6,1,3,60,1,1,2,1,5),_IpMRouteInIfIndex_Type())
ipMRouteInIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInIfIndex.setStatus(_A)
_IpMRouteUpTime_Type=TimeTicks
_IpMRouteUpTime_Object=MibTableColumn
ipMRouteUpTime=_IpMRouteUpTime_Object((1,3,6,1,3,60,1,1,2,1,6),_IpMRouteUpTime_Type())
ipMRouteUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteUpTime.setStatus(_A)
_IpMRouteExpiryTime_Type=TimeTicks
_IpMRouteExpiryTime_Object=MibTableColumn
ipMRouteExpiryTime=_IpMRouteExpiryTime_Object((1,3,6,1,3,60,1,1,2,1,7),_IpMRouteExpiryTime_Type())
ipMRouteExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteExpiryTime.setStatus(_A)
_IpMRoutePkts_Type=Counter32
_IpMRoutePkts_Object=MibTableColumn
ipMRoutePkts=_IpMRoutePkts_Object((1,3,6,1,3,60,1,1,2,1,8),_IpMRoutePkts_Type())
ipMRoutePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoutePkts.setStatus(_A)
_IpMRouteDifferentInIfPackets_Type=Counter32
_IpMRouteDifferentInIfPackets_Object=MibTableColumn
ipMRouteDifferentInIfPackets=_IpMRouteDifferentInIfPackets_Object((1,3,6,1,3,60,1,1,2,1,9),_IpMRouteDifferentInIfPackets_Type())
ipMRouteDifferentInIfPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteDifferentInIfPackets.setStatus(_A)
_IpMRouteOctets_Type=Counter32
_IpMRouteOctets_Object=MibTableColumn
ipMRouteOctets=_IpMRouteOctets_Object((1,3,6,1,3,60,1,1,2,1,10),_IpMRouteOctets_Type())
ipMRouteOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteOctets.setStatus(_A)
class _IpMRouteProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10)))
_IpMRouteProtocol_Type.__name__=_D
_IpMRouteProtocol_Object=MibTableColumn
ipMRouteProtocol=_IpMRouteProtocol_Object((1,3,6,1,3,60,1,1,2,1,11),_IpMRouteProtocol_Type())
ipMRouteProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteProtocol.setStatus(_A)
class _IpMRouteRtProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('isIs',9),('esIs',10),('ciscoIgrp',11),('bbnSpfIgp',12),('ospf',13),('bgp',14),('idpr',15),('ciscoEigrp',16),(_I,17)))
_IpMRouteRtProto_Type.__name__=_D
_IpMRouteRtProto_Object=MibTableColumn
ipMRouteRtProto=_IpMRouteRtProto_Object((1,3,6,1,3,60,1,1,2,1,12),_IpMRouteRtProto_Type())
ipMRouteRtProto.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteRtProto.setStatus(_A)
_IpMRouteRtAddress_Type=IpAddress
_IpMRouteRtAddress_Object=MibTableColumn
ipMRouteRtAddress=_IpMRouteRtAddress_Object((1,3,6,1,3,60,1,1,2,1,13),_IpMRouteRtAddress_Type())
ipMRouteRtAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteRtAddress.setStatus(_A)
_IpMRouteRtMask_Type=IpAddress
_IpMRouteRtMask_Object=MibTableColumn
ipMRouteRtMask=_IpMRouteRtMask_Object((1,3,6,1,3,60,1,1,2,1,14),_IpMRouteRtMask_Type())
ipMRouteRtMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteRtMask.setStatus(_A)
class _IpMRouteRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('multicast',2)))
_IpMRouteRtType_Type.__name__=_D
_IpMRouteRtType_Object=MibTableColumn
ipMRouteRtType=_IpMRouteRtType_Object((1,3,6,1,3,60,1,1,2,1,15),_IpMRouteRtType_Type())
ipMRouteRtType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteRtType.setStatus(_A)
_IpMRouteNextHopTable_Object=MibTable
ipMRouteNextHopTable=_IpMRouteNextHopTable_Object((1,3,6,1,3,60,1,1,3))
if mibBuilder.loadTexts:ipMRouteNextHopTable.setStatus(_A)
_IpMRouteNextHopEntry_Object=MibTableRow
ipMRouteNextHopEntry=_IpMRouteNextHopEntry_Object((1,3,6,1,3,60,1,1,3,1))
ipMRouteNextHopEntry.setIndexNames((0,_B,_U),(0,_B,_V),(0,_B,_W),(0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:ipMRouteNextHopEntry.setStatus(_A)
_IpMRouteNextHopGroup_Type=IpAddress
_IpMRouteNextHopGroup_Object=MibTableColumn
ipMRouteNextHopGroup=_IpMRouteNextHopGroup_Object((1,3,6,1,3,60,1,1,3,1,1),_IpMRouteNextHopGroup_Type())
ipMRouteNextHopGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteNextHopGroup.setStatus(_A)
_IpMRouteNextHopSource_Type=IpAddress
_IpMRouteNextHopSource_Object=MibTableColumn
ipMRouteNextHopSource=_IpMRouteNextHopSource_Object((1,3,6,1,3,60,1,1,3,1,2),_IpMRouteNextHopSource_Type())
ipMRouteNextHopSource.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteNextHopSource.setStatus(_A)
_IpMRouteNextHopSourceMask_Type=IpAddress
_IpMRouteNextHopSourceMask_Object=MibTableColumn
ipMRouteNextHopSourceMask=_IpMRouteNextHopSourceMask_Object((1,3,6,1,3,60,1,1,3,1,3),_IpMRouteNextHopSourceMask_Type())
ipMRouteNextHopSourceMask.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteNextHopSourceMask.setStatus(_A)
class _IpMRouteNextHopIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IpMRouteNextHopIfIndex_Type.__name__=_D
_IpMRouteNextHopIfIndex_Object=MibTableColumn
ipMRouteNextHopIfIndex=_IpMRouteNextHopIfIndex_Object((1,3,6,1,3,60,1,1,3,1,4),_IpMRouteNextHopIfIndex_Type())
ipMRouteNextHopIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteNextHopIfIndex.setStatus(_A)
_IpMRouteNextHopAddress_Type=IpAddress
_IpMRouteNextHopAddress_Object=MibTableColumn
ipMRouteNextHopAddress=_IpMRouteNextHopAddress_Object((1,3,6,1,3,60,1,1,3,1,5),_IpMRouteNextHopAddress_Type())
ipMRouteNextHopAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteNextHopAddress.setStatus(_A)
class _IpMRouteNextHopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pruned',1),('forwarding',2)))
_IpMRouteNextHopState_Type.__name__=_D
_IpMRouteNextHopState_Object=MibTableColumn
ipMRouteNextHopState=_IpMRouteNextHopState_Object((1,3,6,1,3,60,1,1,3,1,6),_IpMRouteNextHopState_Type())
ipMRouteNextHopState.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteNextHopState.setStatus(_A)
_IpMRouteNextHopUpTime_Type=TimeTicks
_IpMRouteNextHopUpTime_Object=MibTableColumn
ipMRouteNextHopUpTime=_IpMRouteNextHopUpTime_Object((1,3,6,1,3,60,1,1,3,1,7),_IpMRouteNextHopUpTime_Type())
ipMRouteNextHopUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteNextHopUpTime.setStatus(_A)
_IpMRouteNextHopExpiryTime_Type=TimeTicks
_IpMRouteNextHopExpiryTime_Object=MibTableColumn
ipMRouteNextHopExpiryTime=_IpMRouteNextHopExpiryTime_Object((1,3,6,1,3,60,1,1,3,1,8),_IpMRouteNextHopExpiryTime_Type())
ipMRouteNextHopExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteNextHopExpiryTime.setStatus(_A)
_IpMRouteNextHopClosestMemberHops_Type=Integer32
_IpMRouteNextHopClosestMemberHops_Object=MibTableColumn
ipMRouteNextHopClosestMemberHops=_IpMRouteNextHopClosestMemberHops_Object((1,3,6,1,3,60,1,1,3,1,9),_IpMRouteNextHopClosestMemberHops_Type())
ipMRouteNextHopClosestMemberHops.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteNextHopClosestMemberHops.setStatus(_A)
class _IpMRouteNextHopProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10)))
_IpMRouteNextHopProtocol_Type.__name__=_D
_IpMRouteNextHopProtocol_Object=MibTableColumn
ipMRouteNextHopProtocol=_IpMRouteNextHopProtocol_Object((1,3,6,1,3,60,1,1,3,1,10),_IpMRouteNextHopProtocol_Type())
ipMRouteNextHopProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteNextHopProtocol.setStatus(_A)
_IpMRouteNextHopPkts_Type=Counter32
_IpMRouteNextHopPkts_Object=MibTableColumn
ipMRouteNextHopPkts=_IpMRouteNextHopPkts_Object((1,3,6,1,3,60,1,1,3,1,11),_IpMRouteNextHopPkts_Type())
ipMRouteNextHopPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteNextHopPkts.setStatus(_A)
_IpMRouteInterfaceTable_Object=MibTable
ipMRouteInterfaceTable=_IpMRouteInterfaceTable_Object((1,3,6,1,3,60,1,1,4))
if mibBuilder.loadTexts:ipMRouteInterfaceTable.setStatus(_A)
_IpMRouteInterfaceEntry_Object=MibTableRow
ipMRouteInterfaceEntry=_IpMRouteInterfaceEntry_Object((1,3,6,1,3,60,1,1,4,1))
ipMRouteInterfaceEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:ipMRouteInterfaceEntry.setStatus(_A)
class _IpMRouteInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IpMRouteInterfaceIfIndex_Type.__name__=_D
_IpMRouteInterfaceIfIndex_Object=MibTableColumn
ipMRouteInterfaceIfIndex=_IpMRouteInterfaceIfIndex_Object((1,3,6,1,3,60,1,1,4,1,1),_IpMRouteInterfaceIfIndex_Type())
ipMRouteInterfaceIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteInterfaceIfIndex.setStatus(_A)
_IpMRouteInterfaceTtl_Type=Integer32
_IpMRouteInterfaceTtl_Object=MibTableColumn
ipMRouteInterfaceTtl=_IpMRouteInterfaceTtl_Object((1,3,6,1,3,60,1,1,4,1,2),_IpMRouteInterfaceTtl_Type())
ipMRouteInterfaceTtl.setMaxAccess(_J)
if mibBuilder.loadTexts:ipMRouteInterfaceTtl.setStatus(_A)
class _IpMRouteInterfaceProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10)))
_IpMRouteInterfaceProtocol_Type.__name__=_D
_IpMRouteInterfaceProtocol_Object=MibTableColumn
ipMRouteInterfaceProtocol=_IpMRouteInterfaceProtocol_Object((1,3,6,1,3,60,1,1,4,1,3),_IpMRouteInterfaceProtocol_Type())
ipMRouteInterfaceProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceProtocol.setStatus(_A)
class _IpMRouteInterfaceRateLimit_Type(Integer32):defaultValue=0
_IpMRouteInterfaceRateLimit_Type.__name__=_D
_IpMRouteInterfaceRateLimit_Object=MibTableColumn
ipMRouteInterfaceRateLimit=_IpMRouteInterfaceRateLimit_Object((1,3,6,1,3,60,1,1,4,1,4),_IpMRouteInterfaceRateLimit_Type())
ipMRouteInterfaceRateLimit.setMaxAccess(_J)
if mibBuilder.loadTexts:ipMRouteInterfaceRateLimit.setStatus(_A)
_IpMRouteInterfaceInMcastOctets_Type=Counter32
_IpMRouteInterfaceInMcastOctets_Object=MibTableColumn
ipMRouteInterfaceInMcastOctets=_IpMRouteInterfaceInMcastOctets_Object((1,3,6,1,3,60,1,1,4,1,5),_IpMRouteInterfaceInMcastOctets_Type())
ipMRouteInterfaceInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceInMcastOctets.setStatus(_A)
_IpMRouteInterfaceOutMcastOctets_Type=Counter32
_IpMRouteInterfaceOutMcastOctets_Object=MibTableColumn
ipMRouteInterfaceOutMcastOctets=_IpMRouteInterfaceOutMcastOctets_Object((1,3,6,1,3,60,1,1,4,1,6),_IpMRouteInterfaceOutMcastOctets_Type())
ipMRouteInterfaceOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceOutMcastOctets.setStatus(_A)
_IpMRouteBoundaryTable_Object=MibTable
ipMRouteBoundaryTable=_IpMRouteBoundaryTable_Object((1,3,6,1,3,60,1,1,5))
if mibBuilder.loadTexts:ipMRouteBoundaryTable.setStatus(_A)
_IpMRouteBoundaryEntry_Object=MibTableRow
ipMRouteBoundaryEntry=_IpMRouteBoundaryEntry_Object((1,3,6,1,3,60,1,1,5,1))
ipMRouteBoundaryEntry.setIndexNames((0,_B,_a),(0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:ipMRouteBoundaryEntry.setStatus(_A)
class _IpMRouteBoundaryIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IpMRouteBoundaryIfIndex_Type.__name__=_D
_IpMRouteBoundaryIfIndex_Object=MibTableColumn
ipMRouteBoundaryIfIndex=_IpMRouteBoundaryIfIndex_Object((1,3,6,1,3,60,1,1,5,1,1),_IpMRouteBoundaryIfIndex_Type())
ipMRouteBoundaryIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteBoundaryIfIndex.setStatus(_A)
_IpMRouteBoundaryAddress_Type=IpAddress
_IpMRouteBoundaryAddress_Object=MibTableColumn
ipMRouteBoundaryAddress=_IpMRouteBoundaryAddress_Object((1,3,6,1,3,60,1,1,5,1,2),_IpMRouteBoundaryAddress_Type())
ipMRouteBoundaryAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteBoundaryAddress.setStatus(_A)
_IpMRouteBoundaryAddressMask_Type=IpAddress
_IpMRouteBoundaryAddressMask_Object=MibTableColumn
ipMRouteBoundaryAddressMask=_IpMRouteBoundaryAddressMask_Object((1,3,6,1,3,60,1,1,5,1,3),_IpMRouteBoundaryAddressMask_Type())
ipMRouteBoundaryAddressMask.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteBoundaryAddressMask.setStatus(_A)
_IpMRouteBoundaryStatus_Type=RowStatus
_IpMRouteBoundaryStatus_Object=MibTableColumn
ipMRouteBoundaryStatus=_IpMRouteBoundaryStatus_Object((1,3,6,1,3,60,1,1,5,1,4),_IpMRouteBoundaryStatus_Type())
ipMRouteBoundaryStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:ipMRouteBoundaryStatus.setStatus(_A)
_IpMRouteMIBConformance_ObjectIdentity=ObjectIdentity
ipMRouteMIBConformance=_IpMRouteMIBConformance_ObjectIdentity((1,3,6,1,3,60,2))
_IpMRouteMIBCompliances_ObjectIdentity=ObjectIdentity
ipMRouteMIBCompliances=_IpMRouteMIBCompliances_ObjectIdentity((1,3,6,1,3,60,2,1))
_IpMRouteMIBGroups_ObjectIdentity=ObjectIdentity
ipMRouteMIBGroups=_IpMRouteMIBGroups_ObjectIdentity((1,3,6,1,3,60,2,2))
ipMRouteMIBBasicGroup=ObjectGroup((1,3,6,1,3,60,2,2,1))
ipMRouteMIBBasicGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_Q),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ipMRouteMIBBasicGroup.setStatus(_A)
ipMRouteMIBHopCountGroup=ObjectGroup((1,3,6,1,3,60,2,2,2))
ipMRouteMIBHopCountGroup.setObjects((_B,_v))
if mibBuilder.loadTexts:ipMRouteMIBHopCountGroup.setStatus(_A)
ipMRouteMIBBoundaryGroup=ObjectGroup((1,3,6,1,3,60,2,2,3))
ipMRouteMIBBoundaryGroup.setObjects((_B,_w))
if mibBuilder.loadTexts:ipMRouteMIBBoundaryGroup.setStatus(_A)
ipMRouteMIBPktsOutGroup=ObjectGroup((1,3,6,1,3,60,2,2,4))
ipMRouteMIBPktsOutGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:ipMRouteMIBPktsOutGroup.setStatus(_A)
ipMRouteMIBRouteGroup=ObjectGroup((1,3,6,1,3,60,2,2,6))
ipMRouteMIBRouteGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:ipMRouteMIBRouteGroup.setStatus(_A)
ipMRouteMIBCompliance=ModuleCompliance((1,3,6,1,3,60,2,1,1))
ipMRouteMIBCompliance.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:ipMRouteMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ipMRouteMIB':ipMRouteMIB,'ipMRouteMIBObjects':ipMRouteMIBObjects,'ipMRoute':ipMRoute,_d:ipMRouteEnable,'ipMRouteTable':ipMRouteTable,'ipMRouteEntry':ipMRouteEntry,_R:ipMRouteGroup,_S:ipMRouteSource,_T:ipMRouteSourceMask,_e:ipMRouteUpstreamNeighbor,_f:ipMRouteInIfIndex,_g:ipMRouteUpTime,_h:ipMRouteExpiryTime,_i:ipMRoutePkts,_j:ipMRouteDifferentInIfPackets,_k:ipMRouteOctets,_u:ipMRouteProtocol,_x:ipMRouteRtProto,_y:ipMRouteRtAddress,_z:ipMRouteRtMask,_A0:ipMRouteRtType,'ipMRouteNextHopTable':ipMRouteNextHopTable,'ipMRouteNextHopEntry':ipMRouteNextHopEntry,_U:ipMRouteNextHopGroup,_V:ipMRouteNextHopSource,_W:ipMRouteNextHopSourceMask,_X:ipMRouteNextHopIfIndex,_Y:ipMRouteNextHopAddress,_l:ipMRouteNextHopState,_m:ipMRouteNextHopUpTime,_n:ipMRouteNextHopExpiryTime,_v:ipMRouteNextHopClosestMemberHops,_o:ipMRouteNextHopProtocol,_Q:ipMRouteNextHopPkts,'ipMRouteInterfaceTable':ipMRouteInterfaceTable,'ipMRouteInterfaceEntry':ipMRouteInterfaceEntry,_Z:ipMRouteInterfaceIfIndex,_p:ipMRouteInterfaceTtl,_q:ipMRouteInterfaceProtocol,_r:ipMRouteInterfaceRateLimit,_s:ipMRouteInterfaceInMcastOctets,_t:ipMRouteInterfaceOutMcastOctets,'ipMRouteBoundaryTable':ipMRouteBoundaryTable,'ipMRouteBoundaryEntry':ipMRouteBoundaryEntry,_a:ipMRouteBoundaryIfIndex,_b:ipMRouteBoundaryAddress,_c:ipMRouteBoundaryAddressMask,_w:ipMRouteBoundaryStatus,'ipMRouteMIBConformance':ipMRouteMIBConformance,'ipMRouteMIBCompliances':ipMRouteMIBCompliances,'ipMRouteMIBCompliance':ipMRouteMIBCompliance,'ipMRouteMIBGroups':ipMRouteMIBGroups,_A1:ipMRouteMIBBasicGroup,'ipMRouteMIBHopCountGroup':ipMRouteMIBHopCountGroup,_A3:ipMRouteMIBBoundaryGroup,'ipMRouteMIBPktsOutGroup':ipMRouteMIBPktsOutGroup,_A2:ipMRouteMIBRouteGroup})