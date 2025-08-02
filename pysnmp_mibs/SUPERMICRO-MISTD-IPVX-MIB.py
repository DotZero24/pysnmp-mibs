_z='fsMIStdInetCidrRouteNextHop'
_y='fsMIStdInetCidrRouteNextHopType'
_x='fsMIStdInetCidrRoutePolicy'
_w='fsMIStdInetCidrRoutePfxLen'
_v='fsMIStdInetCidrRouteDest'
_u='fsMIStdInetCidrRouteDestType'
_t='fsMIStdIcmpMsgStatsType'
_s='fsMIStdIcmpMsgStatsIPVersion'
_r='fsMIStdIcmpStatsIPVersion'
_q='fsMIStdIpv6RouterAdvertIfIndex'
_p='fsMIStdIpDefaultRouterIfIndex'
_o='fsMIStdIpDefaultRouterAddress'
_n='fsMIStdIpDefaultRouterAddressType'
_m='fsMIStdIpv6ScopeZoneIndexIfIndex'
_l='reachable'
_k='invalid'
_j='fsMIStdIpNetToPhysicalNetAddress'
_i='fsMIStdIpNetToPhysicalNetAddressType'
_h='fsMIStdIpNetToPhysicalIfIndex'
_g='anycast'
_f='unicast'
_e='fsMIStdIpAddressAddr'
_d='fsMIStdIpAddressAddrType'
_c='fsMIStdIpAddressPrefixLength'
_b='fsMIStdIpAddressPrefixPrefix'
_a='fsMIStdIpAddressPrefixType'
_Z='fsMIStdIpAddressPrefixIfIndex'
_Y='fsMIStdIpIfStatsIfIndex'
_X='fsMIStdIpIfStatsIPVersion'
_W='milli-seconds'
_V='fsMIStdIpSystemStatsIPVersion'
_U='fsMIStdIpv6InterfaceIfIndex'
_T='fsMIStdIpv4InterfaceIfIndex'
_S='unknown'
_R='StorageType'
_Q='PhysAddress'
_P='InetAutonomousSystemNumber'
_O='notForwarding'
_N='forwarding'
_M='TruthValue'
_L='milliseconds'
_K='seconds'
_J='fsMIStdIpContextId'
_I='InetAddress'
_H='read-write'
_G='Unsigned32'
_F='Integer32'
_E='read-create'
_D='not-accessible'
_C='SUPERMICRO-MISTD-IPVX-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAipRouteProtocol,=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipRouteProtocol')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressPrefixLength,InetAddressType,InetAutonomousSystemNumber,InetZoneIndex=mibBuilder.importSymbols('INET-ADDRESS-MIB',_I,'InetAddressPrefixLength','InetAddressType',_P,'InetZoneIndex')
IpAddressOriginTC,IpAddressPrefixOriginTC,IpAddressStatusTC,Ipv6AddressIfIdentifierTC=mibBuilder.importSymbols('IP-MIB','IpAddressOriginTC','IpAddressPrefixOriginTC','IpAddressStatusTC','Ipv6AddressIfIdentifierTC')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'enterprises','iso')
DisplayString,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_Q,'RowPointer','RowStatus',_R,'TextualConvention','TimeStamp',_M)
fsMIStdIp=ModuleIdentity((1,3,6,1,4,1,10876,101,2,37))
if mibBuilder.loadTexts:fsMIStdIp.setRevisions(('2012-09-05 00:00',))
class FsInetVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),('ipv4',1),('ipv6',2)))
_FsMIStdIpv4InterfaceTableLastChange_Type=TimeStamp
_FsMIStdIpv4InterfaceTableLastChange_Object=MibScalar
fsMIStdIpv4InterfaceTableLastChange=_FsMIStdIpv4InterfaceTableLastChange_Object((1,3,6,1,4,1,10876,101,2,37,1),_FsMIStdIpv4InterfaceTableLastChange_Type())
fsMIStdIpv4InterfaceTableLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv4InterfaceTableLastChange.setStatus(_A)
_FsMIStdIpv6InterfaceTableLastChange_Type=TimeStamp
_FsMIStdIpv6InterfaceTableLastChange_Object=MibScalar
fsMIStdIpv6InterfaceTableLastChange=_FsMIStdIpv6InterfaceTableLastChange_Object((1,3,6,1,4,1,10876,101,2,37,2),_FsMIStdIpv6InterfaceTableLastChange_Type())
fsMIStdIpv6InterfaceTableLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6InterfaceTableLastChange.setStatus(_A)
_FsMIStdIpIfStatsTableLastChange_Type=TimeStamp
_FsMIStdIpIfStatsTableLastChange_Object=MibScalar
fsMIStdIpIfStatsTableLastChange=_FsMIStdIpIfStatsTableLastChange_Object((1,3,6,1,4,1,10876,101,2,37,3),_FsMIStdIpIfStatsTableLastChange_Type())
fsMIStdIpIfStatsTableLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsTableLastChange.setStatus(_A)
_FsMIStdIpGlobalTable_Object=MibTable
fsMIStdIpGlobalTable=_FsMIStdIpGlobalTable_Object((1,3,6,1,4,1,10876,101,2,37,4))
if mibBuilder.loadTexts:fsMIStdIpGlobalTable.setStatus(_A)
_FsMIStdIpGlobalEntry_Object=MibTableRow
fsMIStdIpGlobalEntry=_FsMIStdIpGlobalEntry_Object((1,3,6,1,4,1,10876,101,2,37,4,1))
fsMIStdIpGlobalEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:fsMIStdIpGlobalEntry.setStatus(_A)
class _FsMIStdIpContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_FsMIStdIpContextId_Type.__name__=_F
_FsMIStdIpContextId_Object=MibTableColumn
fsMIStdIpContextId=_FsMIStdIpContextId_Object((1,3,6,1,4,1,10876,101,2,37,4,1,1),_FsMIStdIpContextId_Type())
fsMIStdIpContextId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpContextId.setStatus(_A)
class _FsMIStdIpForwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_FsMIStdIpForwarding_Type.__name__=_F
_FsMIStdIpForwarding_Object=MibTableColumn
fsMIStdIpForwarding=_FsMIStdIpForwarding_Object((1,3,6,1,4,1,10876,101,2,37,4,1,2),_FsMIStdIpForwarding_Type())
fsMIStdIpForwarding.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdIpForwarding.setStatus(_A)
class _FsMIStdIpDefaultTTL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsMIStdIpDefaultTTL_Type.__name__=_F
_FsMIStdIpDefaultTTL_Object=MibTableColumn
fsMIStdIpDefaultTTL=_FsMIStdIpDefaultTTL_Object((1,3,6,1,4,1,10876,101,2,37,4,1,3),_FsMIStdIpDefaultTTL_Type())
fsMIStdIpDefaultTTL.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdIpDefaultTTL.setStatus(_A)
_FsMIStdIpReasmTimeout_Type=Integer32
_FsMIStdIpReasmTimeout_Object=MibTableColumn
fsMIStdIpReasmTimeout=_FsMIStdIpReasmTimeout_Object((1,3,6,1,4,1,10876,101,2,37,4,1,4),_FsMIStdIpReasmTimeout_Type())
fsMIStdIpReasmTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpReasmTimeout.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdIpReasmTimeout.setUnits(_K)
class _FsMIStdIpv6IpForwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_FsMIStdIpv6IpForwarding_Type.__name__=_F
_FsMIStdIpv6IpForwarding_Object=MibTableColumn
fsMIStdIpv6IpForwarding=_FsMIStdIpv6IpForwarding_Object((1,3,6,1,4,1,10876,101,2,37,4,1,5),_FsMIStdIpv6IpForwarding_Type())
fsMIStdIpv6IpForwarding.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdIpv6IpForwarding.setStatus(_A)
class _FsMIStdIpv6IpDefaultHopLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIStdIpv6IpDefaultHopLimit_Type.__name__=_F
_FsMIStdIpv6IpDefaultHopLimit_Object=MibTableColumn
fsMIStdIpv6IpDefaultHopLimit=_FsMIStdIpv6IpDefaultHopLimit_Object((1,3,6,1,4,1,10876,101,2,37,4,1,6),_FsMIStdIpv6IpDefaultHopLimit_Type())
fsMIStdIpv6IpDefaultHopLimit.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdIpv6IpDefaultHopLimit.setStatus(_A)
_FsMIStdInetCidrRouteNumber_Type=Gauge32
_FsMIStdInetCidrRouteNumber_Object=MibTableColumn
fsMIStdInetCidrRouteNumber=_FsMIStdInetCidrRouteNumber_Object((1,3,6,1,4,1,10876,101,2,37,4,1,7),_FsMIStdInetCidrRouteNumber_Type())
fsMIStdInetCidrRouteNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteNumber.setStatus(_A)
_FsMIStdInetCidrRouteDiscards_Type=Counter32
_FsMIStdInetCidrRouteDiscards_Object=MibTableColumn
fsMIStdInetCidrRouteDiscards=_FsMIStdInetCidrRouteDiscards_Object((1,3,6,1,4,1,10876,101,2,37,4,1,8),_FsMIStdInetCidrRouteDiscards_Type())
fsMIStdInetCidrRouteDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteDiscards.setStatus(_A)
_FsMIStdIpv4InterfaceTable_Object=MibTable
fsMIStdIpv4InterfaceTable=_FsMIStdIpv4InterfaceTable_Object((1,3,6,1,4,1,10876,101,2,37,5))
if mibBuilder.loadTexts:fsMIStdIpv4InterfaceTable.setStatus(_A)
_FsMIStdIpv4InterfaceEntry_Object=MibTableRow
fsMIStdIpv4InterfaceEntry=_FsMIStdIpv4InterfaceEntry_Object((1,3,6,1,4,1,10876,101,2,37,5,1))
fsMIStdIpv4InterfaceEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:fsMIStdIpv4InterfaceEntry.setStatus(_A)
_FsMIStdIpv4InterfaceIfIndex_Type=InterfaceIndex
_FsMIStdIpv4InterfaceIfIndex_Object=MibTableColumn
fsMIStdIpv4InterfaceIfIndex=_FsMIStdIpv4InterfaceIfIndex_Object((1,3,6,1,4,1,10876,101,2,37,5,1,1),_FsMIStdIpv4InterfaceIfIndex_Type())
fsMIStdIpv4InterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpv4InterfaceIfIndex.setStatus(_A)
class _FsMIStdIpv4InterfaceReasmMaxSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIStdIpv4InterfaceReasmMaxSize_Type.__name__=_F
_FsMIStdIpv4InterfaceReasmMaxSize_Object=MibTableColumn
fsMIStdIpv4InterfaceReasmMaxSize=_FsMIStdIpv4InterfaceReasmMaxSize_Object((1,3,6,1,4,1,10876,101,2,37,5,1,2),_FsMIStdIpv4InterfaceReasmMaxSize_Type())
fsMIStdIpv4InterfaceReasmMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv4InterfaceReasmMaxSize.setStatus(_A)
class _FsMIStdIpv4InterfaceEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_FsMIStdIpv4InterfaceEnableStatus_Type.__name__=_F
_FsMIStdIpv4InterfaceEnableStatus_Object=MibTableColumn
fsMIStdIpv4InterfaceEnableStatus=_FsMIStdIpv4InterfaceEnableStatus_Object((1,3,6,1,4,1,10876,101,2,37,5,1,3),_FsMIStdIpv4InterfaceEnableStatus_Type())
fsMIStdIpv4InterfaceEnableStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdIpv4InterfaceEnableStatus.setStatus(_A)
class _FsMIStdIpv4InterfaceRetransmitTime_Type(Unsigned32):defaultValue=1000
_FsMIStdIpv4InterfaceRetransmitTime_Type.__name__=_G
_FsMIStdIpv4InterfaceRetransmitTime_Object=MibTableColumn
fsMIStdIpv4InterfaceRetransmitTime=_FsMIStdIpv4InterfaceRetransmitTime_Object((1,3,6,1,4,1,10876,101,2,37,5,1,4),_FsMIStdIpv4InterfaceRetransmitTime_Type())
fsMIStdIpv4InterfaceRetransmitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv4InterfaceRetransmitTime.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdIpv4InterfaceRetransmitTime.setUnits(_L)
_FsMIStdIpv4IfContextId_Type=Integer32
_FsMIStdIpv4IfContextId_Object=MibTableColumn
fsMIStdIpv4IfContextId=_FsMIStdIpv4IfContextId_Object((1,3,6,1,4,1,10876,101,2,37,5,1,5),_FsMIStdIpv4IfContextId_Type())
fsMIStdIpv4IfContextId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv4IfContextId.setStatus(_A)
_FsMIStdIpv6InterfaceTable_Object=MibTable
fsMIStdIpv6InterfaceTable=_FsMIStdIpv6InterfaceTable_Object((1,3,6,1,4,1,10876,101,2,37,6))
if mibBuilder.loadTexts:fsMIStdIpv6InterfaceTable.setStatus(_A)
_FsMIStdIpv6InterfaceEntry_Object=MibTableRow
fsMIStdIpv6InterfaceEntry=_FsMIStdIpv6InterfaceEntry_Object((1,3,6,1,4,1,10876,101,2,37,6,1))
fsMIStdIpv6InterfaceEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:fsMIStdIpv6InterfaceEntry.setStatus(_A)
_FsMIStdIpv6InterfaceIfIndex_Type=InterfaceIndex
_FsMIStdIpv6InterfaceIfIndex_Object=MibTableColumn
fsMIStdIpv6InterfaceIfIndex=_FsMIStdIpv6InterfaceIfIndex_Object((1,3,6,1,4,1,10876,101,2,37,6,1,1),_FsMIStdIpv6InterfaceIfIndex_Type())
fsMIStdIpv6InterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpv6InterfaceIfIndex.setStatus(_A)
class _FsMIStdIpv6InterfaceReasmMaxSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1500,65535))
_FsMIStdIpv6InterfaceReasmMaxSize_Type.__name__=_G
_FsMIStdIpv6InterfaceReasmMaxSize_Object=MibTableColumn
fsMIStdIpv6InterfaceReasmMaxSize=_FsMIStdIpv6InterfaceReasmMaxSize_Object((1,3,6,1,4,1,10876,101,2,37,6,1,2),_FsMIStdIpv6InterfaceReasmMaxSize_Type())
fsMIStdIpv6InterfaceReasmMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6InterfaceReasmMaxSize.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdIpv6InterfaceReasmMaxSize.setUnits('octets')
_FsMIStdIpv6InterfaceIdentifier_Type=Ipv6AddressIfIdentifierTC
_FsMIStdIpv6InterfaceIdentifier_Object=MibTableColumn
fsMIStdIpv6InterfaceIdentifier=_FsMIStdIpv6InterfaceIdentifier_Object((1,3,6,1,4,1,10876,101,2,37,6,1,3),_FsMIStdIpv6InterfaceIdentifier_Type())
fsMIStdIpv6InterfaceIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6InterfaceIdentifier.setStatus(_A)
class _FsMIStdIpv6InterfaceEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_FsMIStdIpv6InterfaceEnableStatus_Type.__name__=_F
_FsMIStdIpv6InterfaceEnableStatus_Object=MibTableColumn
fsMIStdIpv6InterfaceEnableStatus=_FsMIStdIpv6InterfaceEnableStatus_Object((1,3,6,1,4,1,10876,101,2,37,6,1,4),_FsMIStdIpv6InterfaceEnableStatus_Type())
fsMIStdIpv6InterfaceEnableStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdIpv6InterfaceEnableStatus.setStatus(_A)
_FsMIStdIpv6InterfaceReachableTime_Type=Unsigned32
_FsMIStdIpv6InterfaceReachableTime_Object=MibTableColumn
fsMIStdIpv6InterfaceReachableTime=_FsMIStdIpv6InterfaceReachableTime_Object((1,3,6,1,4,1,10876,101,2,37,6,1,5),_FsMIStdIpv6InterfaceReachableTime_Type())
fsMIStdIpv6InterfaceReachableTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6InterfaceReachableTime.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdIpv6InterfaceReachableTime.setUnits(_L)
_FsMIStdIpv6InterfaceRetransmitTime_Type=Unsigned32
_FsMIStdIpv6InterfaceRetransmitTime_Object=MibTableColumn
fsMIStdIpv6InterfaceRetransmitTime=_FsMIStdIpv6InterfaceRetransmitTime_Object((1,3,6,1,4,1,10876,101,2,37,6,1,6),_FsMIStdIpv6InterfaceRetransmitTime_Type())
fsMIStdIpv6InterfaceRetransmitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6InterfaceRetransmitTime.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdIpv6InterfaceRetransmitTime.setUnits(_L)
class _FsMIStdIpv6InterfaceForwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_FsMIStdIpv6InterfaceForwarding_Type.__name__=_F
_FsMIStdIpv6InterfaceForwarding_Object=MibTableColumn
fsMIStdIpv6InterfaceForwarding=_FsMIStdIpv6InterfaceForwarding_Object((1,3,6,1,4,1,10876,101,2,37,6,1,7),_FsMIStdIpv6InterfaceForwarding_Type())
fsMIStdIpv6InterfaceForwarding.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdIpv6InterfaceForwarding.setStatus(_A)
_FsMIStdIpv6IfContextId_Type=Integer32
_FsMIStdIpv6IfContextId_Object=MibTableColumn
fsMIStdIpv6IfContextId=_FsMIStdIpv6IfContextId_Object((1,3,6,1,4,1,10876,101,2,37,6,1,8),_FsMIStdIpv6IfContextId_Type())
fsMIStdIpv6IfContextId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6IfContextId.setStatus(_A)
_FsMIStdIpSystemStatsTable_Object=MibTable
fsMIStdIpSystemStatsTable=_FsMIStdIpSystemStatsTable_Object((1,3,6,1,4,1,10876,101,2,37,7))
if mibBuilder.loadTexts:fsMIStdIpSystemStatsTable.setStatus(_A)
_FsMIStdIpSystemStatsEntry_Object=MibTableRow
fsMIStdIpSystemStatsEntry=_FsMIStdIpSystemStatsEntry_Object((1,3,6,1,4,1,10876,101,2,37,7,1))
fsMIStdIpSystemStatsEntry.setIndexNames((0,_C,_J),(0,_C,_V))
if mibBuilder.loadTexts:fsMIStdIpSystemStatsEntry.setStatus(_A)
_FsMIStdIpSystemStatsIPVersion_Type=FsInetVersion
_FsMIStdIpSystemStatsIPVersion_Object=MibTableColumn
fsMIStdIpSystemStatsIPVersion=_FsMIStdIpSystemStatsIPVersion_Object((1,3,6,1,4,1,10876,101,2,37,7,1,1),_FsMIStdIpSystemStatsIPVersion_Type())
fsMIStdIpSystemStatsIPVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsIPVersion.setStatus(_A)
_FsMIStdIpSystemStatsInReceives_Type=Counter32
_FsMIStdIpSystemStatsInReceives_Object=MibTableColumn
fsMIStdIpSystemStatsInReceives=_FsMIStdIpSystemStatsInReceives_Object((1,3,6,1,4,1,10876,101,2,37,7,1,2),_FsMIStdIpSystemStatsInReceives_Type())
fsMIStdIpSystemStatsInReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsInReceives.setStatus(_A)
_FsMIStdIpSystemStatsHCInReceives_Type=Counter64
_FsMIStdIpSystemStatsHCInReceives_Object=MibTableColumn
fsMIStdIpSystemStatsHCInReceives=_FsMIStdIpSystemStatsHCInReceives_Object((1,3,6,1,4,1,10876,101,2,37,7,1,3),_FsMIStdIpSystemStatsHCInReceives_Type())
fsMIStdIpSystemStatsHCInReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsHCInReceives.setStatus(_A)
_FsMIStdIpSystemStatsInOctets_Type=Counter32
_FsMIStdIpSystemStatsInOctets_Object=MibTableColumn
fsMIStdIpSystemStatsInOctets=_FsMIStdIpSystemStatsInOctets_Object((1,3,6,1,4,1,10876,101,2,37,7,1,4),_FsMIStdIpSystemStatsInOctets_Type())
fsMIStdIpSystemStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsInOctets.setStatus(_A)
_FsMIStdIpSystemStatsHCInOctets_Type=Counter64
_FsMIStdIpSystemStatsHCInOctets_Object=MibTableColumn
fsMIStdIpSystemStatsHCInOctets=_FsMIStdIpSystemStatsHCInOctets_Object((1,3,6,1,4,1,10876,101,2,37,7,1,5),_FsMIStdIpSystemStatsHCInOctets_Type())
fsMIStdIpSystemStatsHCInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsHCInOctets.setStatus(_A)
_FsMIStdIpSystemStatsInHdrErrors_Type=Counter32
_FsMIStdIpSystemStatsInHdrErrors_Object=MibTableColumn
fsMIStdIpSystemStatsInHdrErrors=_FsMIStdIpSystemStatsInHdrErrors_Object((1,3,6,1,4,1,10876,101,2,37,7,1,6),_FsMIStdIpSystemStatsInHdrErrors_Type())
fsMIStdIpSystemStatsInHdrErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsInHdrErrors.setStatus(_A)
_FsMIStdIpSystemStatsInNoRoutes_Type=Counter32
_FsMIStdIpSystemStatsInNoRoutes_Object=MibTableColumn
fsMIStdIpSystemStatsInNoRoutes=_FsMIStdIpSystemStatsInNoRoutes_Object((1,3,6,1,4,1,10876,101,2,37,7,1,7),_FsMIStdIpSystemStatsInNoRoutes_Type())
fsMIStdIpSystemStatsInNoRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsInNoRoutes.setStatus(_A)
_FsMIStdIpSystemStatsInAddrErrors_Type=Counter32
_FsMIStdIpSystemStatsInAddrErrors_Object=MibTableColumn
fsMIStdIpSystemStatsInAddrErrors=_FsMIStdIpSystemStatsInAddrErrors_Object((1,3,6,1,4,1,10876,101,2,37,7,1,8),_FsMIStdIpSystemStatsInAddrErrors_Type())
fsMIStdIpSystemStatsInAddrErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsInAddrErrors.setStatus(_A)
_FsMIStdIpSystemStatsInUnknownProtos_Type=Counter32
_FsMIStdIpSystemStatsInUnknownProtos_Object=MibTableColumn
fsMIStdIpSystemStatsInUnknownProtos=_FsMIStdIpSystemStatsInUnknownProtos_Object((1,3,6,1,4,1,10876,101,2,37,7,1,9),_FsMIStdIpSystemStatsInUnknownProtos_Type())
fsMIStdIpSystemStatsInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsInUnknownProtos.setStatus(_A)
_FsMIStdIpSystemStatsInTruncatedPkts_Type=Counter32
_FsMIStdIpSystemStatsInTruncatedPkts_Object=MibTableColumn
fsMIStdIpSystemStatsInTruncatedPkts=_FsMIStdIpSystemStatsInTruncatedPkts_Object((1,3,6,1,4,1,10876,101,2,37,7,1,10),_FsMIStdIpSystemStatsInTruncatedPkts_Type())
fsMIStdIpSystemStatsInTruncatedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsInTruncatedPkts.setStatus(_A)
_FsMIStdIpSystemStatsInForwDatagrams_Type=Counter32
_FsMIStdIpSystemStatsInForwDatagrams_Object=MibTableColumn
fsMIStdIpSystemStatsInForwDatagrams=_FsMIStdIpSystemStatsInForwDatagrams_Object((1,3,6,1,4,1,10876,101,2,37,7,1,11),_FsMIStdIpSystemStatsInForwDatagrams_Type())
fsMIStdIpSystemStatsInForwDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsInForwDatagrams.setStatus(_A)
_FsMIStdIpSystemStatsHCInForwDatagrams_Type=Counter64
_FsMIStdIpSystemStatsHCInForwDatagrams_Object=MibTableColumn
fsMIStdIpSystemStatsHCInForwDatagrams=_FsMIStdIpSystemStatsHCInForwDatagrams_Object((1,3,6,1,4,1,10876,101,2,37,7,1,12),_FsMIStdIpSystemStatsHCInForwDatagrams_Type())
fsMIStdIpSystemStatsHCInForwDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsHCInForwDatagrams.setStatus(_A)
_FsMIStdIpSystemStatsReasmReqds_Type=Counter32
_FsMIStdIpSystemStatsReasmReqds_Object=MibTableColumn
fsMIStdIpSystemStatsReasmReqds=_FsMIStdIpSystemStatsReasmReqds_Object((1,3,6,1,4,1,10876,101,2,37,7,1,13),_FsMIStdIpSystemStatsReasmReqds_Type())
fsMIStdIpSystemStatsReasmReqds.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsReasmReqds.setStatus(_A)
_FsMIStdIpSystemStatsReasmOKs_Type=Counter32
_FsMIStdIpSystemStatsReasmOKs_Object=MibTableColumn
fsMIStdIpSystemStatsReasmOKs=_FsMIStdIpSystemStatsReasmOKs_Object((1,3,6,1,4,1,10876,101,2,37,7,1,14),_FsMIStdIpSystemStatsReasmOKs_Type())
fsMIStdIpSystemStatsReasmOKs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsReasmOKs.setStatus(_A)
_FsMIStdIpSystemStatsReasmFails_Type=Counter32
_FsMIStdIpSystemStatsReasmFails_Object=MibTableColumn
fsMIStdIpSystemStatsReasmFails=_FsMIStdIpSystemStatsReasmFails_Object((1,3,6,1,4,1,10876,101,2,37,7,1,15),_FsMIStdIpSystemStatsReasmFails_Type())
fsMIStdIpSystemStatsReasmFails.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsReasmFails.setStatus(_A)
_FsMIStdIpSystemStatsInDiscards_Type=Counter32
_FsMIStdIpSystemStatsInDiscards_Object=MibTableColumn
fsMIStdIpSystemStatsInDiscards=_FsMIStdIpSystemStatsInDiscards_Object((1,3,6,1,4,1,10876,101,2,37,7,1,16),_FsMIStdIpSystemStatsInDiscards_Type())
fsMIStdIpSystemStatsInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsInDiscards.setStatus(_A)
_FsMIStdIpSystemStatsInDelivers_Type=Counter32
_FsMIStdIpSystemStatsInDelivers_Object=MibTableColumn
fsMIStdIpSystemStatsInDelivers=_FsMIStdIpSystemStatsInDelivers_Object((1,3,6,1,4,1,10876,101,2,37,7,1,17),_FsMIStdIpSystemStatsInDelivers_Type())
fsMIStdIpSystemStatsInDelivers.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsInDelivers.setStatus(_A)
_FsMIStdIpSystemStatsHCInDelivers_Type=Counter64
_FsMIStdIpSystemStatsHCInDelivers_Object=MibTableColumn
fsMIStdIpSystemStatsHCInDelivers=_FsMIStdIpSystemStatsHCInDelivers_Object((1,3,6,1,4,1,10876,101,2,37,7,1,18),_FsMIStdIpSystemStatsHCInDelivers_Type())
fsMIStdIpSystemStatsHCInDelivers.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsHCInDelivers.setStatus(_A)
_FsMIStdIpSystemStatsOutRequests_Type=Counter32
_FsMIStdIpSystemStatsOutRequests_Object=MibTableColumn
fsMIStdIpSystemStatsOutRequests=_FsMIStdIpSystemStatsOutRequests_Object((1,3,6,1,4,1,10876,101,2,37,7,1,19),_FsMIStdIpSystemStatsOutRequests_Type())
fsMIStdIpSystemStatsOutRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsOutRequests.setStatus(_A)
_FsMIStdIpSystemStatsHCOutRequests_Type=Counter64
_FsMIStdIpSystemStatsHCOutRequests_Object=MibTableColumn
fsMIStdIpSystemStatsHCOutRequests=_FsMIStdIpSystemStatsHCOutRequests_Object((1,3,6,1,4,1,10876,101,2,37,7,1,20),_FsMIStdIpSystemStatsHCOutRequests_Type())
fsMIStdIpSystemStatsHCOutRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsHCOutRequests.setStatus(_A)
_FsMIStdIpSystemStatsOutNoRoutes_Type=Counter32
_FsMIStdIpSystemStatsOutNoRoutes_Object=MibTableColumn
fsMIStdIpSystemStatsOutNoRoutes=_FsMIStdIpSystemStatsOutNoRoutes_Object((1,3,6,1,4,1,10876,101,2,37,7,1,21),_FsMIStdIpSystemStatsOutNoRoutes_Type())
fsMIStdIpSystemStatsOutNoRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsOutNoRoutes.setStatus(_A)
_FsMIStdIpSystemStatsOutForwDatagrams_Type=Counter32
_FsMIStdIpSystemStatsOutForwDatagrams_Object=MibTableColumn
fsMIStdIpSystemStatsOutForwDatagrams=_FsMIStdIpSystemStatsOutForwDatagrams_Object((1,3,6,1,4,1,10876,101,2,37,7,1,22),_FsMIStdIpSystemStatsOutForwDatagrams_Type())
fsMIStdIpSystemStatsOutForwDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsOutForwDatagrams.setStatus(_A)
_FsMIStdIpSystemStatsHCOutForwDatagrams_Type=Counter64
_FsMIStdIpSystemStatsHCOutForwDatagrams_Object=MibTableColumn
fsMIStdIpSystemStatsHCOutForwDatagrams=_FsMIStdIpSystemStatsHCOutForwDatagrams_Object((1,3,6,1,4,1,10876,101,2,37,7,1,23),_FsMIStdIpSystemStatsHCOutForwDatagrams_Type())
fsMIStdIpSystemStatsHCOutForwDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsHCOutForwDatagrams.setStatus(_A)
_FsMIStdIpSystemStatsOutDiscards_Type=Counter32
_FsMIStdIpSystemStatsOutDiscards_Object=MibTableColumn
fsMIStdIpSystemStatsOutDiscards=_FsMIStdIpSystemStatsOutDiscards_Object((1,3,6,1,4,1,10876,101,2,37,7,1,24),_FsMIStdIpSystemStatsOutDiscards_Type())
fsMIStdIpSystemStatsOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsOutDiscards.setStatus(_A)
_FsMIStdIpSystemStatsOutFragReqds_Type=Counter32
_FsMIStdIpSystemStatsOutFragReqds_Object=MibTableColumn
fsMIStdIpSystemStatsOutFragReqds=_FsMIStdIpSystemStatsOutFragReqds_Object((1,3,6,1,4,1,10876,101,2,37,7,1,25),_FsMIStdIpSystemStatsOutFragReqds_Type())
fsMIStdIpSystemStatsOutFragReqds.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsOutFragReqds.setStatus(_A)
_FsMIStdIpSystemStatsOutFragOKs_Type=Counter32
_FsMIStdIpSystemStatsOutFragOKs_Object=MibTableColumn
fsMIStdIpSystemStatsOutFragOKs=_FsMIStdIpSystemStatsOutFragOKs_Object((1,3,6,1,4,1,10876,101,2,37,7,1,26),_FsMIStdIpSystemStatsOutFragOKs_Type())
fsMIStdIpSystemStatsOutFragOKs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsOutFragOKs.setStatus(_A)
_FsMIStdIpSystemStatsOutFragFails_Type=Counter32
_FsMIStdIpSystemStatsOutFragFails_Object=MibTableColumn
fsMIStdIpSystemStatsOutFragFails=_FsMIStdIpSystemStatsOutFragFails_Object((1,3,6,1,4,1,10876,101,2,37,7,1,27),_FsMIStdIpSystemStatsOutFragFails_Type())
fsMIStdIpSystemStatsOutFragFails.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsOutFragFails.setStatus(_A)
_FsMIStdIpSystemStatsOutFragCreates_Type=Counter32
_FsMIStdIpSystemStatsOutFragCreates_Object=MibTableColumn
fsMIStdIpSystemStatsOutFragCreates=_FsMIStdIpSystemStatsOutFragCreates_Object((1,3,6,1,4,1,10876,101,2,37,7,1,28),_FsMIStdIpSystemStatsOutFragCreates_Type())
fsMIStdIpSystemStatsOutFragCreates.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsOutFragCreates.setStatus(_A)
_FsMIStdIpSystemStatsOutTransmits_Type=Counter32
_FsMIStdIpSystemStatsOutTransmits_Object=MibTableColumn
fsMIStdIpSystemStatsOutTransmits=_FsMIStdIpSystemStatsOutTransmits_Object((1,3,6,1,4,1,10876,101,2,37,7,1,29),_FsMIStdIpSystemStatsOutTransmits_Type())
fsMIStdIpSystemStatsOutTransmits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsOutTransmits.setStatus(_A)
_FsMIStdIpSystemStatsHCOutTransmits_Type=Counter64
_FsMIStdIpSystemStatsHCOutTransmits_Object=MibTableColumn
fsMIStdIpSystemStatsHCOutTransmits=_FsMIStdIpSystemStatsHCOutTransmits_Object((1,3,6,1,4,1,10876,101,2,37,7,1,30),_FsMIStdIpSystemStatsHCOutTransmits_Type())
fsMIStdIpSystemStatsHCOutTransmits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsHCOutTransmits.setStatus(_A)
_FsMIStdIpSystemStatsOutOctets_Type=Counter32
_FsMIStdIpSystemStatsOutOctets_Object=MibTableColumn
fsMIStdIpSystemStatsOutOctets=_FsMIStdIpSystemStatsOutOctets_Object((1,3,6,1,4,1,10876,101,2,37,7,1,31),_FsMIStdIpSystemStatsOutOctets_Type())
fsMIStdIpSystemStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsOutOctets.setStatus(_A)
_FsMIStdIpSystemStatsHCOutOctets_Type=Counter64
_FsMIStdIpSystemStatsHCOutOctets_Object=MibTableColumn
fsMIStdIpSystemStatsHCOutOctets=_FsMIStdIpSystemStatsHCOutOctets_Object((1,3,6,1,4,1,10876,101,2,37,7,1,32),_FsMIStdIpSystemStatsHCOutOctets_Type())
fsMIStdIpSystemStatsHCOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsHCOutOctets.setStatus(_A)
_FsMIStdIpSystemStatsInMcastPkts_Type=Counter32
_FsMIStdIpSystemStatsInMcastPkts_Object=MibTableColumn
fsMIStdIpSystemStatsInMcastPkts=_FsMIStdIpSystemStatsInMcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,7,1,33),_FsMIStdIpSystemStatsInMcastPkts_Type())
fsMIStdIpSystemStatsInMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsInMcastPkts.setStatus(_A)
_FsMIStdIpSystemStatsHCInMcastPkts_Type=Counter64
_FsMIStdIpSystemStatsHCInMcastPkts_Object=MibTableColumn
fsMIStdIpSystemStatsHCInMcastPkts=_FsMIStdIpSystemStatsHCInMcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,7,1,34),_FsMIStdIpSystemStatsHCInMcastPkts_Type())
fsMIStdIpSystemStatsHCInMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsHCInMcastPkts.setStatus(_A)
_FsMIStdIpSystemStatsInMcastOctets_Type=Counter32
_FsMIStdIpSystemStatsInMcastOctets_Object=MibTableColumn
fsMIStdIpSystemStatsInMcastOctets=_FsMIStdIpSystemStatsInMcastOctets_Object((1,3,6,1,4,1,10876,101,2,37,7,1,35),_FsMIStdIpSystemStatsInMcastOctets_Type())
fsMIStdIpSystemStatsInMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsInMcastOctets.setStatus(_A)
_FsMIStdIpSystemStatsHCInMcastOctets_Type=Counter64
_FsMIStdIpSystemStatsHCInMcastOctets_Object=MibTableColumn
fsMIStdIpSystemStatsHCInMcastOctets=_FsMIStdIpSystemStatsHCInMcastOctets_Object((1,3,6,1,4,1,10876,101,2,37,7,1,36),_FsMIStdIpSystemStatsHCInMcastOctets_Type())
fsMIStdIpSystemStatsHCInMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsHCInMcastOctets.setStatus(_A)
_FsMIStdIpSystemStatsOutMcastPkts_Type=Counter32
_FsMIStdIpSystemStatsOutMcastPkts_Object=MibTableColumn
fsMIStdIpSystemStatsOutMcastPkts=_FsMIStdIpSystemStatsOutMcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,7,1,37),_FsMIStdIpSystemStatsOutMcastPkts_Type())
fsMIStdIpSystemStatsOutMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsOutMcastPkts.setStatus(_A)
_FsMIStdIpSystemStatsHCOutMcastPkts_Type=Counter64
_FsMIStdIpSystemStatsHCOutMcastPkts_Object=MibTableColumn
fsMIStdIpSystemStatsHCOutMcastPkts=_FsMIStdIpSystemStatsHCOutMcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,7,1,38),_FsMIStdIpSystemStatsHCOutMcastPkts_Type())
fsMIStdIpSystemStatsHCOutMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsHCOutMcastPkts.setStatus(_A)
_FsMIStdIpSystemStatsOutMcastOctets_Type=Counter32
_FsMIStdIpSystemStatsOutMcastOctets_Object=MibTableColumn
fsMIStdIpSystemStatsOutMcastOctets=_FsMIStdIpSystemStatsOutMcastOctets_Object((1,3,6,1,4,1,10876,101,2,37,7,1,39),_FsMIStdIpSystemStatsOutMcastOctets_Type())
fsMIStdIpSystemStatsOutMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsOutMcastOctets.setStatus(_A)
_FsMIStdIpSystemStatsHCOutMcastOctets_Type=Counter64
_FsMIStdIpSystemStatsHCOutMcastOctets_Object=MibTableColumn
fsMIStdIpSystemStatsHCOutMcastOctets=_FsMIStdIpSystemStatsHCOutMcastOctets_Object((1,3,6,1,4,1,10876,101,2,37,7,1,40),_FsMIStdIpSystemStatsHCOutMcastOctets_Type())
fsMIStdIpSystemStatsHCOutMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsHCOutMcastOctets.setStatus(_A)
_FsMIStdIpSystemStatsInBcastPkts_Type=Counter32
_FsMIStdIpSystemStatsInBcastPkts_Object=MibTableColumn
fsMIStdIpSystemStatsInBcastPkts=_FsMIStdIpSystemStatsInBcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,7,1,41),_FsMIStdIpSystemStatsInBcastPkts_Type())
fsMIStdIpSystemStatsInBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsInBcastPkts.setStatus(_A)
_FsMIStdIpSystemStatsHCInBcastPkts_Type=Counter64
_FsMIStdIpSystemStatsHCInBcastPkts_Object=MibTableColumn
fsMIStdIpSystemStatsHCInBcastPkts=_FsMIStdIpSystemStatsHCInBcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,7,1,42),_FsMIStdIpSystemStatsHCInBcastPkts_Type())
fsMIStdIpSystemStatsHCInBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsHCInBcastPkts.setStatus(_A)
_FsMIStdIpSystemStatsOutBcastPkts_Type=Counter32
_FsMIStdIpSystemStatsOutBcastPkts_Object=MibTableColumn
fsMIStdIpSystemStatsOutBcastPkts=_FsMIStdIpSystemStatsOutBcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,7,1,43),_FsMIStdIpSystemStatsOutBcastPkts_Type())
fsMIStdIpSystemStatsOutBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsOutBcastPkts.setStatus(_A)
_FsMIStdIpSystemStatsHCOutBcastPkts_Type=Counter64
_FsMIStdIpSystemStatsHCOutBcastPkts_Object=MibTableColumn
fsMIStdIpSystemStatsHCOutBcastPkts=_FsMIStdIpSystemStatsHCOutBcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,7,1,44),_FsMIStdIpSystemStatsHCOutBcastPkts_Type())
fsMIStdIpSystemStatsHCOutBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsHCOutBcastPkts.setStatus(_A)
_FsMIStdIpSystemStatsDiscontinuityTime_Type=TimeStamp
_FsMIStdIpSystemStatsDiscontinuityTime_Object=MibTableColumn
fsMIStdIpSystemStatsDiscontinuityTime=_FsMIStdIpSystemStatsDiscontinuityTime_Object((1,3,6,1,4,1,10876,101,2,37,7,1,45),_FsMIStdIpSystemStatsDiscontinuityTime_Type())
fsMIStdIpSystemStatsDiscontinuityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsDiscontinuityTime.setStatus(_A)
_FsMIStdIpSystemStatsRefreshRate_Type=Unsigned32
_FsMIStdIpSystemStatsRefreshRate_Object=MibTableColumn
fsMIStdIpSystemStatsRefreshRate=_FsMIStdIpSystemStatsRefreshRate_Object((1,3,6,1,4,1,10876,101,2,37,7,1,46),_FsMIStdIpSystemStatsRefreshRate_Type())
fsMIStdIpSystemStatsRefreshRate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsRefreshRate.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdIpSystemStatsRefreshRate.setUnits(_W)
_FsMIStdIpIfStatsTable_Object=MibTable
fsMIStdIpIfStatsTable=_FsMIStdIpIfStatsTable_Object((1,3,6,1,4,1,10876,101,2,37,8))
if mibBuilder.loadTexts:fsMIStdIpIfStatsTable.setStatus(_A)
_FsMIStdIpIfStatsEntry_Object=MibTableRow
fsMIStdIpIfStatsEntry=_FsMIStdIpIfStatsEntry_Object((1,3,6,1,4,1,10876,101,2,37,8,1))
fsMIStdIpIfStatsEntry.setIndexNames((0,_C,_X),(0,_C,_Y))
if mibBuilder.loadTexts:fsMIStdIpIfStatsEntry.setStatus(_A)
_FsMIStdIpIfStatsIPVersion_Type=FsInetVersion
_FsMIStdIpIfStatsIPVersion_Object=MibTableColumn
fsMIStdIpIfStatsIPVersion=_FsMIStdIpIfStatsIPVersion_Object((1,3,6,1,4,1,10876,101,2,37,8,1,1),_FsMIStdIpIfStatsIPVersion_Type())
fsMIStdIpIfStatsIPVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpIfStatsIPVersion.setStatus(_A)
_FsMIStdIpIfStatsIfIndex_Type=InterfaceIndex
_FsMIStdIpIfStatsIfIndex_Object=MibTableColumn
fsMIStdIpIfStatsIfIndex=_FsMIStdIpIfStatsIfIndex_Object((1,3,6,1,4,1,10876,101,2,37,8,1,2),_FsMIStdIpIfStatsIfIndex_Type())
fsMIStdIpIfStatsIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpIfStatsIfIndex.setStatus(_A)
_FsMIStdIpIfStatsInReceives_Type=Counter32
_FsMIStdIpIfStatsInReceives_Object=MibTableColumn
fsMIStdIpIfStatsInReceives=_FsMIStdIpIfStatsInReceives_Object((1,3,6,1,4,1,10876,101,2,37,8,1,3),_FsMIStdIpIfStatsInReceives_Type())
fsMIStdIpIfStatsInReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsInReceives.setStatus(_A)
_FsMIStdIpIfStatsHCInReceives_Type=Counter64
_FsMIStdIpIfStatsHCInReceives_Object=MibTableColumn
fsMIStdIpIfStatsHCInReceives=_FsMIStdIpIfStatsHCInReceives_Object((1,3,6,1,4,1,10876,101,2,37,8,1,4),_FsMIStdIpIfStatsHCInReceives_Type())
fsMIStdIpIfStatsHCInReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsHCInReceives.setStatus(_A)
_FsMIStdIpIfStatsInOctets_Type=Counter32
_FsMIStdIpIfStatsInOctets_Object=MibTableColumn
fsMIStdIpIfStatsInOctets=_FsMIStdIpIfStatsInOctets_Object((1,3,6,1,4,1,10876,101,2,37,8,1,5),_FsMIStdIpIfStatsInOctets_Type())
fsMIStdIpIfStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsInOctets.setStatus(_A)
_FsMIStdIpIfStatsHCInOctets_Type=Counter64
_FsMIStdIpIfStatsHCInOctets_Object=MibTableColumn
fsMIStdIpIfStatsHCInOctets=_FsMIStdIpIfStatsHCInOctets_Object((1,3,6,1,4,1,10876,101,2,37,8,1,6),_FsMIStdIpIfStatsHCInOctets_Type())
fsMIStdIpIfStatsHCInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsHCInOctets.setStatus(_A)
_FsMIStdIpIfStatsInHdrErrors_Type=Counter32
_FsMIStdIpIfStatsInHdrErrors_Object=MibTableColumn
fsMIStdIpIfStatsInHdrErrors=_FsMIStdIpIfStatsInHdrErrors_Object((1,3,6,1,4,1,10876,101,2,37,8,1,7),_FsMIStdIpIfStatsInHdrErrors_Type())
fsMIStdIpIfStatsInHdrErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsInHdrErrors.setStatus(_A)
_FsMIStdIpIfStatsInNoRoutes_Type=Counter32
_FsMIStdIpIfStatsInNoRoutes_Object=MibTableColumn
fsMIStdIpIfStatsInNoRoutes=_FsMIStdIpIfStatsInNoRoutes_Object((1,3,6,1,4,1,10876,101,2,37,8,1,8),_FsMIStdIpIfStatsInNoRoutes_Type())
fsMIStdIpIfStatsInNoRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsInNoRoutes.setStatus(_A)
_FsMIStdIpIfStatsInAddrErrors_Type=Counter32
_FsMIStdIpIfStatsInAddrErrors_Object=MibTableColumn
fsMIStdIpIfStatsInAddrErrors=_FsMIStdIpIfStatsInAddrErrors_Object((1,3,6,1,4,1,10876,101,2,37,8,1,9),_FsMIStdIpIfStatsInAddrErrors_Type())
fsMIStdIpIfStatsInAddrErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsInAddrErrors.setStatus(_A)
_FsMIStdIpIfStatsInUnknownProtos_Type=Counter32
_FsMIStdIpIfStatsInUnknownProtos_Object=MibTableColumn
fsMIStdIpIfStatsInUnknownProtos=_FsMIStdIpIfStatsInUnknownProtos_Object((1,3,6,1,4,1,10876,101,2,37,8,1,10),_FsMIStdIpIfStatsInUnknownProtos_Type())
fsMIStdIpIfStatsInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsInUnknownProtos.setStatus(_A)
_FsMIStdIpIfStatsInTruncatedPkts_Type=Counter32
_FsMIStdIpIfStatsInTruncatedPkts_Object=MibTableColumn
fsMIStdIpIfStatsInTruncatedPkts=_FsMIStdIpIfStatsInTruncatedPkts_Object((1,3,6,1,4,1,10876,101,2,37,8,1,11),_FsMIStdIpIfStatsInTruncatedPkts_Type())
fsMIStdIpIfStatsInTruncatedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsInTruncatedPkts.setStatus(_A)
_FsMIStdIpIfStatsInForwDatagrams_Type=Counter32
_FsMIStdIpIfStatsInForwDatagrams_Object=MibTableColumn
fsMIStdIpIfStatsInForwDatagrams=_FsMIStdIpIfStatsInForwDatagrams_Object((1,3,6,1,4,1,10876,101,2,37,8,1,12),_FsMIStdIpIfStatsInForwDatagrams_Type())
fsMIStdIpIfStatsInForwDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsInForwDatagrams.setStatus(_A)
_FsMIStdIpIfStatsHCInForwDatagrams_Type=Counter64
_FsMIStdIpIfStatsHCInForwDatagrams_Object=MibTableColumn
fsMIStdIpIfStatsHCInForwDatagrams=_FsMIStdIpIfStatsHCInForwDatagrams_Object((1,3,6,1,4,1,10876,101,2,37,8,1,13),_FsMIStdIpIfStatsHCInForwDatagrams_Type())
fsMIStdIpIfStatsHCInForwDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsHCInForwDatagrams.setStatus(_A)
_FsMIStdIpIfStatsReasmReqds_Type=Counter32
_FsMIStdIpIfStatsReasmReqds_Object=MibTableColumn
fsMIStdIpIfStatsReasmReqds=_FsMIStdIpIfStatsReasmReqds_Object((1,3,6,1,4,1,10876,101,2,37,8,1,14),_FsMIStdIpIfStatsReasmReqds_Type())
fsMIStdIpIfStatsReasmReqds.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsReasmReqds.setStatus(_A)
_FsMIStdIpIfStatsReasmOKs_Type=Counter32
_FsMIStdIpIfStatsReasmOKs_Object=MibTableColumn
fsMIStdIpIfStatsReasmOKs=_FsMIStdIpIfStatsReasmOKs_Object((1,3,6,1,4,1,10876,101,2,37,8,1,15),_FsMIStdIpIfStatsReasmOKs_Type())
fsMIStdIpIfStatsReasmOKs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsReasmOKs.setStatus(_A)
_FsMIStdIpIfStatsReasmFails_Type=Counter32
_FsMIStdIpIfStatsReasmFails_Object=MibTableColumn
fsMIStdIpIfStatsReasmFails=_FsMIStdIpIfStatsReasmFails_Object((1,3,6,1,4,1,10876,101,2,37,8,1,16),_FsMIStdIpIfStatsReasmFails_Type())
fsMIStdIpIfStatsReasmFails.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsReasmFails.setStatus(_A)
_FsMIStdIpIfStatsInDiscards_Type=Counter32
_FsMIStdIpIfStatsInDiscards_Object=MibTableColumn
fsMIStdIpIfStatsInDiscards=_FsMIStdIpIfStatsInDiscards_Object((1,3,6,1,4,1,10876,101,2,37,8,1,17),_FsMIStdIpIfStatsInDiscards_Type())
fsMIStdIpIfStatsInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsInDiscards.setStatus(_A)
_FsMIStdIpIfStatsInDelivers_Type=Counter32
_FsMIStdIpIfStatsInDelivers_Object=MibTableColumn
fsMIStdIpIfStatsInDelivers=_FsMIStdIpIfStatsInDelivers_Object((1,3,6,1,4,1,10876,101,2,37,8,1,18),_FsMIStdIpIfStatsInDelivers_Type())
fsMIStdIpIfStatsInDelivers.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsInDelivers.setStatus(_A)
_FsMIStdIpIfStatsHCInDelivers_Type=Counter64
_FsMIStdIpIfStatsHCInDelivers_Object=MibTableColumn
fsMIStdIpIfStatsHCInDelivers=_FsMIStdIpIfStatsHCInDelivers_Object((1,3,6,1,4,1,10876,101,2,37,8,1,19),_FsMIStdIpIfStatsHCInDelivers_Type())
fsMIStdIpIfStatsHCInDelivers.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsHCInDelivers.setStatus(_A)
_FsMIStdIpIfStatsOutRequests_Type=Counter32
_FsMIStdIpIfStatsOutRequests_Object=MibTableColumn
fsMIStdIpIfStatsOutRequests=_FsMIStdIpIfStatsOutRequests_Object((1,3,6,1,4,1,10876,101,2,37,8,1,20),_FsMIStdIpIfStatsOutRequests_Type())
fsMIStdIpIfStatsOutRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsOutRequests.setStatus(_A)
_FsMIStdIpIfStatsHCOutRequests_Type=Counter64
_FsMIStdIpIfStatsHCOutRequests_Object=MibTableColumn
fsMIStdIpIfStatsHCOutRequests=_FsMIStdIpIfStatsHCOutRequests_Object((1,3,6,1,4,1,10876,101,2,37,8,1,21),_FsMIStdIpIfStatsHCOutRequests_Type())
fsMIStdIpIfStatsHCOutRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsHCOutRequests.setStatus(_A)
_FsMIStdIpIfStatsOutForwDatagrams_Type=Counter32
_FsMIStdIpIfStatsOutForwDatagrams_Object=MibTableColumn
fsMIStdIpIfStatsOutForwDatagrams=_FsMIStdIpIfStatsOutForwDatagrams_Object((1,3,6,1,4,1,10876,101,2,37,8,1,22),_FsMIStdIpIfStatsOutForwDatagrams_Type())
fsMIStdIpIfStatsOutForwDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsOutForwDatagrams.setStatus(_A)
_FsMIStdIpIfStatsHCOutForwDatagrams_Type=Counter64
_FsMIStdIpIfStatsHCOutForwDatagrams_Object=MibTableColumn
fsMIStdIpIfStatsHCOutForwDatagrams=_FsMIStdIpIfStatsHCOutForwDatagrams_Object((1,3,6,1,4,1,10876,101,2,37,8,1,23),_FsMIStdIpIfStatsHCOutForwDatagrams_Type())
fsMIStdIpIfStatsHCOutForwDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsHCOutForwDatagrams.setStatus(_A)
_FsMIStdIpIfStatsOutDiscards_Type=Counter32
_FsMIStdIpIfStatsOutDiscards_Object=MibTableColumn
fsMIStdIpIfStatsOutDiscards=_FsMIStdIpIfStatsOutDiscards_Object((1,3,6,1,4,1,10876,101,2,37,8,1,24),_FsMIStdIpIfStatsOutDiscards_Type())
fsMIStdIpIfStatsOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsOutDiscards.setStatus(_A)
_FsMIStdIpIfStatsOutFragReqds_Type=Counter32
_FsMIStdIpIfStatsOutFragReqds_Object=MibTableColumn
fsMIStdIpIfStatsOutFragReqds=_FsMIStdIpIfStatsOutFragReqds_Object((1,3,6,1,4,1,10876,101,2,37,8,1,25),_FsMIStdIpIfStatsOutFragReqds_Type())
fsMIStdIpIfStatsOutFragReqds.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsOutFragReqds.setStatus(_A)
_FsMIStdIpIfStatsOutFragOKs_Type=Counter32
_FsMIStdIpIfStatsOutFragOKs_Object=MibTableColumn
fsMIStdIpIfStatsOutFragOKs=_FsMIStdIpIfStatsOutFragOKs_Object((1,3,6,1,4,1,10876,101,2,37,8,1,26),_FsMIStdIpIfStatsOutFragOKs_Type())
fsMIStdIpIfStatsOutFragOKs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsOutFragOKs.setStatus(_A)
_FsMIStdIpIfStatsOutFragFails_Type=Counter32
_FsMIStdIpIfStatsOutFragFails_Object=MibTableColumn
fsMIStdIpIfStatsOutFragFails=_FsMIStdIpIfStatsOutFragFails_Object((1,3,6,1,4,1,10876,101,2,37,8,1,27),_FsMIStdIpIfStatsOutFragFails_Type())
fsMIStdIpIfStatsOutFragFails.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsOutFragFails.setStatus(_A)
_FsMIStdIpIfStatsOutFragCreates_Type=Counter32
_FsMIStdIpIfStatsOutFragCreates_Object=MibTableColumn
fsMIStdIpIfStatsOutFragCreates=_FsMIStdIpIfStatsOutFragCreates_Object((1,3,6,1,4,1,10876,101,2,37,8,1,28),_FsMIStdIpIfStatsOutFragCreates_Type())
fsMIStdIpIfStatsOutFragCreates.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsOutFragCreates.setStatus(_A)
_FsMIStdIpIfStatsOutTransmits_Type=Counter32
_FsMIStdIpIfStatsOutTransmits_Object=MibTableColumn
fsMIStdIpIfStatsOutTransmits=_FsMIStdIpIfStatsOutTransmits_Object((1,3,6,1,4,1,10876,101,2,37,8,1,29),_FsMIStdIpIfStatsOutTransmits_Type())
fsMIStdIpIfStatsOutTransmits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsOutTransmits.setStatus(_A)
_FsMIStdIpIfStatsHCOutTransmits_Type=Counter64
_FsMIStdIpIfStatsHCOutTransmits_Object=MibTableColumn
fsMIStdIpIfStatsHCOutTransmits=_FsMIStdIpIfStatsHCOutTransmits_Object((1,3,6,1,4,1,10876,101,2,37,8,1,30),_FsMIStdIpIfStatsHCOutTransmits_Type())
fsMIStdIpIfStatsHCOutTransmits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsHCOutTransmits.setStatus(_A)
_FsMIStdIpIfStatsOutOctets_Type=Counter32
_FsMIStdIpIfStatsOutOctets_Object=MibTableColumn
fsMIStdIpIfStatsOutOctets=_FsMIStdIpIfStatsOutOctets_Object((1,3,6,1,4,1,10876,101,2,37,8,1,31),_FsMIStdIpIfStatsOutOctets_Type())
fsMIStdIpIfStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsOutOctets.setStatus(_A)
_FsMIStdIpIfStatsHCOutOctets_Type=Counter64
_FsMIStdIpIfStatsHCOutOctets_Object=MibTableColumn
fsMIStdIpIfStatsHCOutOctets=_FsMIStdIpIfStatsHCOutOctets_Object((1,3,6,1,4,1,10876,101,2,37,8,1,32),_FsMIStdIpIfStatsHCOutOctets_Type())
fsMIStdIpIfStatsHCOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsHCOutOctets.setStatus(_A)
_FsMIStdIpIfStatsInMcastPkts_Type=Counter32
_FsMIStdIpIfStatsInMcastPkts_Object=MibTableColumn
fsMIStdIpIfStatsInMcastPkts=_FsMIStdIpIfStatsInMcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,8,1,33),_FsMIStdIpIfStatsInMcastPkts_Type())
fsMIStdIpIfStatsInMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsInMcastPkts.setStatus(_A)
_FsMIStdIpIfStatsHCInMcastPkts_Type=Counter64
_FsMIStdIpIfStatsHCInMcastPkts_Object=MibTableColumn
fsMIStdIpIfStatsHCInMcastPkts=_FsMIStdIpIfStatsHCInMcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,8,1,34),_FsMIStdIpIfStatsHCInMcastPkts_Type())
fsMIStdIpIfStatsHCInMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsHCInMcastPkts.setStatus(_A)
_FsMIStdIpIfStatsInMcastOctets_Type=Counter32
_FsMIStdIpIfStatsInMcastOctets_Object=MibTableColumn
fsMIStdIpIfStatsInMcastOctets=_FsMIStdIpIfStatsInMcastOctets_Object((1,3,6,1,4,1,10876,101,2,37,8,1,35),_FsMIStdIpIfStatsInMcastOctets_Type())
fsMIStdIpIfStatsInMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsInMcastOctets.setStatus(_A)
_FsMIStdIpIfStatsHCInMcastOctets_Type=Counter64
_FsMIStdIpIfStatsHCInMcastOctets_Object=MibTableColumn
fsMIStdIpIfStatsHCInMcastOctets=_FsMIStdIpIfStatsHCInMcastOctets_Object((1,3,6,1,4,1,10876,101,2,37,8,1,36),_FsMIStdIpIfStatsHCInMcastOctets_Type())
fsMIStdIpIfStatsHCInMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsHCInMcastOctets.setStatus(_A)
_FsMIStdIpIfStatsOutMcastPkts_Type=Counter32
_FsMIStdIpIfStatsOutMcastPkts_Object=MibTableColumn
fsMIStdIpIfStatsOutMcastPkts=_FsMIStdIpIfStatsOutMcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,8,1,37),_FsMIStdIpIfStatsOutMcastPkts_Type())
fsMIStdIpIfStatsOutMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsOutMcastPkts.setStatus(_A)
_FsMIStdIpIfStatsHCOutMcastPkts_Type=Counter64
_FsMIStdIpIfStatsHCOutMcastPkts_Object=MibTableColumn
fsMIStdIpIfStatsHCOutMcastPkts=_FsMIStdIpIfStatsHCOutMcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,8,1,38),_FsMIStdIpIfStatsHCOutMcastPkts_Type())
fsMIStdIpIfStatsHCOutMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsHCOutMcastPkts.setStatus(_A)
_FsMIStdIpIfStatsOutMcastOctets_Type=Counter32
_FsMIStdIpIfStatsOutMcastOctets_Object=MibTableColumn
fsMIStdIpIfStatsOutMcastOctets=_FsMIStdIpIfStatsOutMcastOctets_Object((1,3,6,1,4,1,10876,101,2,37,8,1,39),_FsMIStdIpIfStatsOutMcastOctets_Type())
fsMIStdIpIfStatsOutMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsOutMcastOctets.setStatus(_A)
_FsMIStdIpIfStatsHCOutMcastOctets_Type=Counter64
_FsMIStdIpIfStatsHCOutMcastOctets_Object=MibTableColumn
fsMIStdIpIfStatsHCOutMcastOctets=_FsMIStdIpIfStatsHCOutMcastOctets_Object((1,3,6,1,4,1,10876,101,2,37,8,1,40),_FsMIStdIpIfStatsHCOutMcastOctets_Type())
fsMIStdIpIfStatsHCOutMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsHCOutMcastOctets.setStatus(_A)
_FsMIStdIpIfStatsInBcastPkts_Type=Counter32
_FsMIStdIpIfStatsInBcastPkts_Object=MibTableColumn
fsMIStdIpIfStatsInBcastPkts=_FsMIStdIpIfStatsInBcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,8,1,41),_FsMIStdIpIfStatsInBcastPkts_Type())
fsMIStdIpIfStatsInBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsInBcastPkts.setStatus(_A)
_FsMIStdIpIfStatsHCInBcastPkts_Type=Counter64
_FsMIStdIpIfStatsHCInBcastPkts_Object=MibTableColumn
fsMIStdIpIfStatsHCInBcastPkts=_FsMIStdIpIfStatsHCInBcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,8,1,42),_FsMIStdIpIfStatsHCInBcastPkts_Type())
fsMIStdIpIfStatsHCInBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsHCInBcastPkts.setStatus(_A)
_FsMIStdIpIfStatsOutBcastPkts_Type=Counter32
_FsMIStdIpIfStatsOutBcastPkts_Object=MibTableColumn
fsMIStdIpIfStatsOutBcastPkts=_FsMIStdIpIfStatsOutBcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,8,1,43),_FsMIStdIpIfStatsOutBcastPkts_Type())
fsMIStdIpIfStatsOutBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsOutBcastPkts.setStatus(_A)
_FsMIStdIpIfStatsHCOutBcastPkts_Type=Counter64
_FsMIStdIpIfStatsHCOutBcastPkts_Object=MibTableColumn
fsMIStdIpIfStatsHCOutBcastPkts=_FsMIStdIpIfStatsHCOutBcastPkts_Object((1,3,6,1,4,1,10876,101,2,37,8,1,44),_FsMIStdIpIfStatsHCOutBcastPkts_Type())
fsMIStdIpIfStatsHCOutBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsHCOutBcastPkts.setStatus(_A)
_FsMIStdIpIfStatsDiscontinuityTime_Type=TimeStamp
_FsMIStdIpIfStatsDiscontinuityTime_Object=MibTableColumn
fsMIStdIpIfStatsDiscontinuityTime=_FsMIStdIpIfStatsDiscontinuityTime_Object((1,3,6,1,4,1,10876,101,2,37,8,1,45),_FsMIStdIpIfStatsDiscontinuityTime_Type())
fsMIStdIpIfStatsDiscontinuityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsDiscontinuityTime.setStatus(_A)
_FsMIStdIpIfStatsRefreshRate_Type=Unsigned32
_FsMIStdIpIfStatsRefreshRate_Object=MibTableColumn
fsMIStdIpIfStatsRefreshRate=_FsMIStdIpIfStatsRefreshRate_Object((1,3,6,1,4,1,10876,101,2,37,8,1,47),_FsMIStdIpIfStatsRefreshRate_Type())
fsMIStdIpIfStatsRefreshRate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsRefreshRate.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdIpIfStatsRefreshRate.setUnits(_W)
_FsMIStdIpIfStatsContextId_Type=Integer32
_FsMIStdIpIfStatsContextId_Object=MibTableColumn
fsMIStdIpIfStatsContextId=_FsMIStdIpIfStatsContextId_Object((1,3,6,1,4,1,10876,101,2,37,8,1,48),_FsMIStdIpIfStatsContextId_Type())
fsMIStdIpIfStatsContextId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpIfStatsContextId.setStatus(_A)
_FsMIStdIpAddressPrefixTable_Object=MibTable
fsMIStdIpAddressPrefixTable=_FsMIStdIpAddressPrefixTable_Object((1,3,6,1,4,1,10876,101,2,37,9))
if mibBuilder.loadTexts:fsMIStdIpAddressPrefixTable.setStatus(_A)
_FsMIStdIpAddressPrefixEntry_Object=MibTableRow
fsMIStdIpAddressPrefixEntry=_FsMIStdIpAddressPrefixEntry_Object((1,3,6,1,4,1,10876,101,2,37,9,1))
fsMIStdIpAddressPrefixEntry.setIndexNames((0,_C,_Z),(0,_C,_a),(0,_C,_b),(0,_C,_c))
if mibBuilder.loadTexts:fsMIStdIpAddressPrefixEntry.setStatus(_A)
_FsMIStdIpAddressPrefixIfIndex_Type=InterfaceIndex
_FsMIStdIpAddressPrefixIfIndex_Object=MibTableColumn
fsMIStdIpAddressPrefixIfIndex=_FsMIStdIpAddressPrefixIfIndex_Object((1,3,6,1,4,1,10876,101,2,37,9,1,1),_FsMIStdIpAddressPrefixIfIndex_Type())
fsMIStdIpAddressPrefixIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpAddressPrefixIfIndex.setStatus(_A)
_FsMIStdIpAddressPrefixType_Type=InetAddressType
_FsMIStdIpAddressPrefixType_Object=MibTableColumn
fsMIStdIpAddressPrefixType=_FsMIStdIpAddressPrefixType_Object((1,3,6,1,4,1,10876,101,2,37,9,1,2),_FsMIStdIpAddressPrefixType_Type())
fsMIStdIpAddressPrefixType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpAddressPrefixType.setStatus(_A)
class _FsMIStdIpAddressPrefixPrefix_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIStdIpAddressPrefixPrefix_Type.__name__=_I
_FsMIStdIpAddressPrefixPrefix_Object=MibTableColumn
fsMIStdIpAddressPrefixPrefix=_FsMIStdIpAddressPrefixPrefix_Object((1,3,6,1,4,1,10876,101,2,37,9,1,3),_FsMIStdIpAddressPrefixPrefix_Type())
fsMIStdIpAddressPrefixPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpAddressPrefixPrefix.setStatus(_A)
_FsMIStdIpAddressPrefixLength_Type=InetAddressPrefixLength
_FsMIStdIpAddressPrefixLength_Object=MibTableColumn
fsMIStdIpAddressPrefixLength=_FsMIStdIpAddressPrefixLength_Object((1,3,6,1,4,1,10876,101,2,37,9,1,4),_FsMIStdIpAddressPrefixLength_Type())
fsMIStdIpAddressPrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpAddressPrefixLength.setStatus(_A)
_FsMIStdIpAddressPrefixOrigin_Type=IpAddressPrefixOriginTC
_FsMIStdIpAddressPrefixOrigin_Object=MibTableColumn
fsMIStdIpAddressPrefixOrigin=_FsMIStdIpAddressPrefixOrigin_Object((1,3,6,1,4,1,10876,101,2,37,9,1,5),_FsMIStdIpAddressPrefixOrigin_Type())
fsMIStdIpAddressPrefixOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpAddressPrefixOrigin.setStatus(_A)
_FsMIStdIpAddressPrefixOnLinkFlag_Type=TruthValue
_FsMIStdIpAddressPrefixOnLinkFlag_Object=MibTableColumn
fsMIStdIpAddressPrefixOnLinkFlag=_FsMIStdIpAddressPrefixOnLinkFlag_Object((1,3,6,1,4,1,10876,101,2,37,9,1,6),_FsMIStdIpAddressPrefixOnLinkFlag_Type())
fsMIStdIpAddressPrefixOnLinkFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpAddressPrefixOnLinkFlag.setStatus(_A)
_FsMIStdIpAddressPrefixAutonomousFlag_Type=TruthValue
_FsMIStdIpAddressPrefixAutonomousFlag_Object=MibTableColumn
fsMIStdIpAddressPrefixAutonomousFlag=_FsMIStdIpAddressPrefixAutonomousFlag_Object((1,3,6,1,4,1,10876,101,2,37,9,1,7),_FsMIStdIpAddressPrefixAutonomousFlag_Type())
fsMIStdIpAddressPrefixAutonomousFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpAddressPrefixAutonomousFlag.setStatus(_A)
_FsMIStdIpAddressPrefixAdvPreferredLifetime_Type=Unsigned32
_FsMIStdIpAddressPrefixAdvPreferredLifetime_Object=MibTableColumn
fsMIStdIpAddressPrefixAdvPreferredLifetime=_FsMIStdIpAddressPrefixAdvPreferredLifetime_Object((1,3,6,1,4,1,10876,101,2,37,9,1,8),_FsMIStdIpAddressPrefixAdvPreferredLifetime_Type())
fsMIStdIpAddressPrefixAdvPreferredLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpAddressPrefixAdvPreferredLifetime.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdIpAddressPrefixAdvPreferredLifetime.setUnits(_K)
_FsMIStdIpAddressPrefixAdvValidLifetime_Type=Unsigned32
_FsMIStdIpAddressPrefixAdvValidLifetime_Object=MibTableColumn
fsMIStdIpAddressPrefixAdvValidLifetime=_FsMIStdIpAddressPrefixAdvValidLifetime_Object((1,3,6,1,4,1,10876,101,2,37,9,1,9),_FsMIStdIpAddressPrefixAdvValidLifetime_Type())
fsMIStdIpAddressPrefixAdvValidLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpAddressPrefixAdvValidLifetime.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdIpAddressPrefixAdvValidLifetime.setUnits(_K)
_FsMIStdIpAddressContextId_Type=Integer32
_FsMIStdIpAddressContextId_Object=MibTableColumn
fsMIStdIpAddressContextId=_FsMIStdIpAddressContextId_Object((1,3,6,1,4,1,10876,101,2,37,9,1,10),_FsMIStdIpAddressContextId_Type())
fsMIStdIpAddressContextId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpAddressContextId.setStatus(_A)
_FsMIStdIpAddressTable_Object=MibTable
fsMIStdIpAddressTable=_FsMIStdIpAddressTable_Object((1,3,6,1,4,1,10876,101,2,37,10))
if mibBuilder.loadTexts:fsMIStdIpAddressTable.setStatus(_A)
_FsMIStdIpAddressEntry_Object=MibTableRow
fsMIStdIpAddressEntry=_FsMIStdIpAddressEntry_Object((1,3,6,1,4,1,10876,101,2,37,10,1))
fsMIStdIpAddressEntry.setIndexNames((0,_C,_J),(0,_C,_d),(0,_C,_e))
if mibBuilder.loadTexts:fsMIStdIpAddressEntry.setStatus(_A)
_FsMIStdIpAddressAddrType_Type=InetAddressType
_FsMIStdIpAddressAddrType_Object=MibTableColumn
fsMIStdIpAddressAddrType=_FsMIStdIpAddressAddrType_Object((1,3,6,1,4,1,10876,101,2,37,10,1,2),_FsMIStdIpAddressAddrType_Type())
fsMIStdIpAddressAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpAddressAddrType.setStatus(_A)
class _FsMIStdIpAddressAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIStdIpAddressAddr_Type.__name__=_I
_FsMIStdIpAddressAddr_Object=MibTableColumn
fsMIStdIpAddressAddr=_FsMIStdIpAddressAddr_Object((1,3,6,1,4,1,10876,101,2,37,10,1,3),_FsMIStdIpAddressAddr_Type())
fsMIStdIpAddressAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpAddressAddr.setStatus(_A)
_FsMIStdIpAddressIfIndex_Type=InterfaceIndex
_FsMIStdIpAddressIfIndex_Object=MibTableColumn
fsMIStdIpAddressIfIndex=_FsMIStdIpAddressIfIndex_Object((1,3,6,1,4,1,10876,101,2,37,10,1,4),_FsMIStdIpAddressIfIndex_Type())
fsMIStdIpAddressIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpAddressIfIndex.setStatus(_A)
class _FsMIStdIpAddressType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),(_g,2),('broadcast',3)))
_FsMIStdIpAddressType_Type.__name__=_F
_FsMIStdIpAddressType_Object=MibTableColumn
fsMIStdIpAddressType=_FsMIStdIpAddressType_Object((1,3,6,1,4,1,10876,101,2,37,10,1,5),_FsMIStdIpAddressType_Type())
fsMIStdIpAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpAddressType.setStatus(_A)
_FsMIStdIpAddressPrefix_Type=RowPointer
_FsMIStdIpAddressPrefix_Object=MibTableColumn
fsMIStdIpAddressPrefix=_FsMIStdIpAddressPrefix_Object((1,3,6,1,4,1,10876,101,2,37,10,1,6),_FsMIStdIpAddressPrefix_Type())
fsMIStdIpAddressPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpAddressPrefix.setStatus(_A)
_FsMIStdIpAddressOrigin_Type=IpAddressOriginTC
_FsMIStdIpAddressOrigin_Object=MibTableColumn
fsMIStdIpAddressOrigin=_FsMIStdIpAddressOrigin_Object((1,3,6,1,4,1,10876,101,2,37,10,1,7),_FsMIStdIpAddressOrigin_Type())
fsMIStdIpAddressOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpAddressOrigin.setStatus(_A)
_FsMIStdIpAddressStatus_Type=IpAddressStatusTC
_FsMIStdIpAddressStatus_Object=MibTableColumn
fsMIStdIpAddressStatus=_FsMIStdIpAddressStatus_Object((1,3,6,1,4,1,10876,101,2,37,10,1,8),_FsMIStdIpAddressStatus_Type())
fsMIStdIpAddressStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpAddressStatus.setStatus(_A)
_FsMIStdIpAddressCreated_Type=TimeStamp
_FsMIStdIpAddressCreated_Object=MibTableColumn
fsMIStdIpAddressCreated=_FsMIStdIpAddressCreated_Object((1,3,6,1,4,1,10876,101,2,37,10,1,9),_FsMIStdIpAddressCreated_Type())
fsMIStdIpAddressCreated.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpAddressCreated.setStatus(_A)
_FsMIStdIpAddressLastChanged_Type=TimeStamp
_FsMIStdIpAddressLastChanged_Object=MibTableColumn
fsMIStdIpAddressLastChanged=_FsMIStdIpAddressLastChanged_Object((1,3,6,1,4,1,10876,101,2,37,10,1,10),_FsMIStdIpAddressLastChanged_Type())
fsMIStdIpAddressLastChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpAddressLastChanged.setStatus(_A)
_FsMIStdIpAddressRowStatus_Type=RowStatus
_FsMIStdIpAddressRowStatus_Object=MibTableColumn
fsMIStdIpAddressRowStatus=_FsMIStdIpAddressRowStatus_Object((1,3,6,1,4,1,10876,101,2,37,10,1,11),_FsMIStdIpAddressRowStatus_Type())
fsMIStdIpAddressRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpAddressRowStatus.setStatus(_A)
class _FsMIStdIpAddressStorageType_Type(StorageType):defaultValue=2
_FsMIStdIpAddressStorageType_Type.__name__=_R
_FsMIStdIpAddressStorageType_Object=MibTableColumn
fsMIStdIpAddressStorageType=_FsMIStdIpAddressStorageType_Object((1,3,6,1,4,1,10876,101,2,37,10,1,12),_FsMIStdIpAddressStorageType_Type())
fsMIStdIpAddressStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpAddressStorageType.setStatus(_A)
_FsMIStdIpNetToPhysicalTable_Object=MibTable
fsMIStdIpNetToPhysicalTable=_FsMIStdIpNetToPhysicalTable_Object((1,3,6,1,4,1,10876,101,2,37,11))
if mibBuilder.loadTexts:fsMIStdIpNetToPhysicalTable.setStatus(_A)
_FsMIStdIpNetToPhysicalEntry_Object=MibTableRow
fsMIStdIpNetToPhysicalEntry=_FsMIStdIpNetToPhysicalEntry_Object((1,3,6,1,4,1,10876,101,2,37,11,1))
fsMIStdIpNetToPhysicalEntry.setIndexNames((0,_C,_h),(0,_C,_i),(0,_C,_j))
if mibBuilder.loadTexts:fsMIStdIpNetToPhysicalEntry.setStatus(_A)
_FsMIStdIpNetToPhysicalIfIndex_Type=InterfaceIndex
_FsMIStdIpNetToPhysicalIfIndex_Object=MibTableColumn
fsMIStdIpNetToPhysicalIfIndex=_FsMIStdIpNetToPhysicalIfIndex_Object((1,3,6,1,4,1,10876,101,2,37,11,1,1),_FsMIStdIpNetToPhysicalIfIndex_Type())
fsMIStdIpNetToPhysicalIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpNetToPhysicalIfIndex.setStatus(_A)
_FsMIStdIpNetToPhysicalNetAddressType_Type=InetAddressType
_FsMIStdIpNetToPhysicalNetAddressType_Object=MibTableColumn
fsMIStdIpNetToPhysicalNetAddressType=_FsMIStdIpNetToPhysicalNetAddressType_Object((1,3,6,1,4,1,10876,101,2,37,11,1,2),_FsMIStdIpNetToPhysicalNetAddressType_Type())
fsMIStdIpNetToPhysicalNetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpNetToPhysicalNetAddressType.setStatus(_A)
class _FsMIStdIpNetToPhysicalNetAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIStdIpNetToPhysicalNetAddress_Type.__name__=_I
_FsMIStdIpNetToPhysicalNetAddress_Object=MibTableColumn
fsMIStdIpNetToPhysicalNetAddress=_FsMIStdIpNetToPhysicalNetAddress_Object((1,3,6,1,4,1,10876,101,2,37,11,1,3),_FsMIStdIpNetToPhysicalNetAddress_Type())
fsMIStdIpNetToPhysicalNetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpNetToPhysicalNetAddress.setStatus(_A)
class _FsMIStdIpNetToPhysicalPhysAddress_Type(PhysAddress):subtypeSpec=PhysAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_FsMIStdIpNetToPhysicalPhysAddress_Type.__name__=_Q
_FsMIStdIpNetToPhysicalPhysAddress_Object=MibTableColumn
fsMIStdIpNetToPhysicalPhysAddress=_FsMIStdIpNetToPhysicalPhysAddress_Object((1,3,6,1,4,1,10876,101,2,37,11,1,4),_FsMIStdIpNetToPhysicalPhysAddress_Type())
fsMIStdIpNetToPhysicalPhysAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpNetToPhysicalPhysAddress.setStatus(_A)
_FsMIStdIpNetToPhysicalLastUpdated_Type=TimeStamp
_FsMIStdIpNetToPhysicalLastUpdated_Object=MibTableColumn
fsMIStdIpNetToPhysicalLastUpdated=_FsMIStdIpNetToPhysicalLastUpdated_Object((1,3,6,1,4,1,10876,101,2,37,11,1,5),_FsMIStdIpNetToPhysicalLastUpdated_Type())
fsMIStdIpNetToPhysicalLastUpdated.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpNetToPhysicalLastUpdated.setStatus(_A)
class _FsMIStdIpNetToPhysicalType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),(_k,2),('dynamic',3),('static',4),('local',5)))
_FsMIStdIpNetToPhysicalType_Type.__name__=_F
_FsMIStdIpNetToPhysicalType_Object=MibTableColumn
fsMIStdIpNetToPhysicalType=_FsMIStdIpNetToPhysicalType_Object((1,3,6,1,4,1,10876,101,2,37,11,1,6),_FsMIStdIpNetToPhysicalType_Type())
fsMIStdIpNetToPhysicalType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpNetToPhysicalType.setStatus(_A)
class _FsMIStdIpNetToPhysicalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_l,1),('stale',2),('delay',3),('probe',4),(_k,5),(_S,6),('incomplete',7)))
_FsMIStdIpNetToPhysicalState_Type.__name__=_F
_FsMIStdIpNetToPhysicalState_Object=MibTableColumn
fsMIStdIpNetToPhysicalState=_FsMIStdIpNetToPhysicalState_Object((1,3,6,1,4,1,10876,101,2,37,11,1,7),_FsMIStdIpNetToPhysicalState_Type())
fsMIStdIpNetToPhysicalState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpNetToPhysicalState.setStatus(_A)
_FsMIStdIpNetToPhysicalRowStatus_Type=RowStatus
_FsMIStdIpNetToPhysicalRowStatus_Object=MibTableColumn
fsMIStdIpNetToPhysicalRowStatus=_FsMIStdIpNetToPhysicalRowStatus_Object((1,3,6,1,4,1,10876,101,2,37,11,1,8),_FsMIStdIpNetToPhysicalRowStatus_Type())
fsMIStdIpNetToPhysicalRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpNetToPhysicalRowStatus.setStatus(_A)
_FsMIStdIpNetToPhysicalContextId_Type=Integer32
_FsMIStdIpNetToPhysicalContextId_Object=MibTableColumn
fsMIStdIpNetToPhysicalContextId=_FsMIStdIpNetToPhysicalContextId_Object((1,3,6,1,4,1,10876,101,2,37,11,1,9),_FsMIStdIpNetToPhysicalContextId_Type())
fsMIStdIpNetToPhysicalContextId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpNetToPhysicalContextId.setStatus(_A)
_FsMIStdIpv6ScopeZoneIndexTable_Object=MibTable
fsMIStdIpv6ScopeZoneIndexTable=_FsMIStdIpv6ScopeZoneIndexTable_Object((1,3,6,1,4,1,10876,101,2,37,12))
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneIndexTable.setStatus(_A)
_FsMIStdIpv6ScopeZoneIndexEntry_Object=MibTableRow
fsMIStdIpv6ScopeZoneIndexEntry=_FsMIStdIpv6ScopeZoneIndexEntry_Object((1,3,6,1,4,1,10876,101,2,37,12,1))
fsMIStdIpv6ScopeZoneIndexEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneIndexEntry.setStatus(_A)
_FsMIStdIpv6ScopeZoneIndexIfIndex_Type=InterfaceIndex
_FsMIStdIpv6ScopeZoneIndexIfIndex_Object=MibTableColumn
fsMIStdIpv6ScopeZoneIndexIfIndex=_FsMIStdIpv6ScopeZoneIndexIfIndex_Object((1,3,6,1,4,1,10876,101,2,37,12,1,1),_FsMIStdIpv6ScopeZoneIndexIfIndex_Type())
fsMIStdIpv6ScopeZoneIndexIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneIndexIfIndex.setStatus(_A)
_FsMIStdIpv6ScopeZoneIndexLinkLocal_Type=InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexLinkLocal_Object=MibTableColumn
fsMIStdIpv6ScopeZoneIndexLinkLocal=_FsMIStdIpv6ScopeZoneIndexLinkLocal_Object((1,3,6,1,4,1,10876,101,2,37,12,1,2),_FsMIStdIpv6ScopeZoneIndexLinkLocal_Type())
fsMIStdIpv6ScopeZoneIndexLinkLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneIndexLinkLocal.setStatus(_A)
_FsMIStdIpv6ScopeZoneIndex3_Type=InetZoneIndex
_FsMIStdIpv6ScopeZoneIndex3_Object=MibTableColumn
fsMIStdIpv6ScopeZoneIndex3=_FsMIStdIpv6ScopeZoneIndex3_Object((1,3,6,1,4,1,10876,101,2,37,12,1,3),_FsMIStdIpv6ScopeZoneIndex3_Type())
fsMIStdIpv6ScopeZoneIndex3.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneIndex3.setStatus(_A)
_FsMIStdIpv6ScopeZoneIndexAdminLocal_Type=InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexAdminLocal_Object=MibTableColumn
fsMIStdIpv6ScopeZoneIndexAdminLocal=_FsMIStdIpv6ScopeZoneIndexAdminLocal_Object((1,3,6,1,4,1,10876,101,2,37,12,1,4),_FsMIStdIpv6ScopeZoneIndexAdminLocal_Type())
fsMIStdIpv6ScopeZoneIndexAdminLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneIndexAdminLocal.setStatus(_A)
_FsMIStdIpv6ScopeZoneIndexSiteLocal_Type=InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexSiteLocal_Object=MibTableColumn
fsMIStdIpv6ScopeZoneIndexSiteLocal=_FsMIStdIpv6ScopeZoneIndexSiteLocal_Object((1,3,6,1,4,1,10876,101,2,37,12,1,5),_FsMIStdIpv6ScopeZoneIndexSiteLocal_Type())
fsMIStdIpv6ScopeZoneIndexSiteLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneIndexSiteLocal.setStatus(_A)
_FsMIStdIpv6ScopeZoneIndex6_Type=InetZoneIndex
_FsMIStdIpv6ScopeZoneIndex6_Object=MibTableColumn
fsMIStdIpv6ScopeZoneIndex6=_FsMIStdIpv6ScopeZoneIndex6_Object((1,3,6,1,4,1,10876,101,2,37,12,1,6),_FsMIStdIpv6ScopeZoneIndex6_Type())
fsMIStdIpv6ScopeZoneIndex6.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneIndex6.setStatus(_A)
_FsMIStdIpv6ScopeZoneIndex7_Type=InetZoneIndex
_FsMIStdIpv6ScopeZoneIndex7_Object=MibTableColumn
fsMIStdIpv6ScopeZoneIndex7=_FsMIStdIpv6ScopeZoneIndex7_Object((1,3,6,1,4,1,10876,101,2,37,12,1,7),_FsMIStdIpv6ScopeZoneIndex7_Type())
fsMIStdIpv6ScopeZoneIndex7.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneIndex7.setStatus(_A)
_FsMIStdIpv6ScopeZoneIndexOrganizationLocal_Type=InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexOrganizationLocal_Object=MibTableColumn
fsMIStdIpv6ScopeZoneIndexOrganizationLocal=_FsMIStdIpv6ScopeZoneIndexOrganizationLocal_Object((1,3,6,1,4,1,10876,101,2,37,12,1,8),_FsMIStdIpv6ScopeZoneIndexOrganizationLocal_Type())
fsMIStdIpv6ScopeZoneIndexOrganizationLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneIndexOrganizationLocal.setStatus(_A)
_FsMIStdIpv6ScopeZoneIndex9_Type=InetZoneIndex
_FsMIStdIpv6ScopeZoneIndex9_Object=MibTableColumn
fsMIStdIpv6ScopeZoneIndex9=_FsMIStdIpv6ScopeZoneIndex9_Object((1,3,6,1,4,1,10876,101,2,37,12,1,9),_FsMIStdIpv6ScopeZoneIndex9_Type())
fsMIStdIpv6ScopeZoneIndex9.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneIndex9.setStatus(_A)
_FsMIStdIpv6ScopeZoneIndexA_Type=InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexA_Object=MibTableColumn
fsMIStdIpv6ScopeZoneIndexA=_FsMIStdIpv6ScopeZoneIndexA_Object((1,3,6,1,4,1,10876,101,2,37,12,1,10),_FsMIStdIpv6ScopeZoneIndexA_Type())
fsMIStdIpv6ScopeZoneIndexA.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneIndexA.setStatus(_A)
_FsMIStdIpv6ScopeZoneIndexB_Type=InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexB_Object=MibTableColumn
fsMIStdIpv6ScopeZoneIndexB=_FsMIStdIpv6ScopeZoneIndexB_Object((1,3,6,1,4,1,10876,101,2,37,12,1,11),_FsMIStdIpv6ScopeZoneIndexB_Type())
fsMIStdIpv6ScopeZoneIndexB.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneIndexB.setStatus(_A)
_FsMIStdIpv6ScopeZoneIndexC_Type=InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexC_Object=MibTableColumn
fsMIStdIpv6ScopeZoneIndexC=_FsMIStdIpv6ScopeZoneIndexC_Object((1,3,6,1,4,1,10876,101,2,37,12,1,12),_FsMIStdIpv6ScopeZoneIndexC_Type())
fsMIStdIpv6ScopeZoneIndexC.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneIndexC.setStatus(_A)
_FsMIStdIpv6ScopeZoneIndexD_Type=InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexD_Object=MibTableColumn
fsMIStdIpv6ScopeZoneIndexD=_FsMIStdIpv6ScopeZoneIndexD_Object((1,3,6,1,4,1,10876,101,2,37,12,1,13),_FsMIStdIpv6ScopeZoneIndexD_Type())
fsMIStdIpv6ScopeZoneIndexD.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneIndexD.setStatus(_A)
_FsMIStdIpv6ScopeZoneContextId_Type=Integer32
_FsMIStdIpv6ScopeZoneContextId_Object=MibTableColumn
fsMIStdIpv6ScopeZoneContextId=_FsMIStdIpv6ScopeZoneContextId_Object((1,3,6,1,4,1,10876,101,2,37,12,1,14),_FsMIStdIpv6ScopeZoneContextId_Type())
fsMIStdIpv6ScopeZoneContextId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6ScopeZoneContextId.setStatus(_A)
_FsMIStdIpDefaultRouterTable_Object=MibTable
fsMIStdIpDefaultRouterTable=_FsMIStdIpDefaultRouterTable_Object((1,3,6,1,4,1,10876,101,2,37,13))
if mibBuilder.loadTexts:fsMIStdIpDefaultRouterTable.setStatus(_A)
_FsMIStdIpDefaultRouterEntry_Object=MibTableRow
fsMIStdIpDefaultRouterEntry=_FsMIStdIpDefaultRouterEntry_Object((1,3,6,1,4,1,10876,101,2,37,13,1))
fsMIStdIpDefaultRouterEntry.setIndexNames((0,_C,_n),(0,_C,_o),(0,_C,_p))
if mibBuilder.loadTexts:fsMIStdIpDefaultRouterEntry.setStatus(_A)
_FsMIStdIpDefaultRouterAddressType_Type=InetAddressType
_FsMIStdIpDefaultRouterAddressType_Object=MibTableColumn
fsMIStdIpDefaultRouterAddressType=_FsMIStdIpDefaultRouterAddressType_Object((1,3,6,1,4,1,10876,101,2,37,13,1,1),_FsMIStdIpDefaultRouterAddressType_Type())
fsMIStdIpDefaultRouterAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpDefaultRouterAddressType.setStatus(_A)
class _FsMIStdIpDefaultRouterAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIStdIpDefaultRouterAddress_Type.__name__=_I
_FsMIStdIpDefaultRouterAddress_Object=MibTableColumn
fsMIStdIpDefaultRouterAddress=_FsMIStdIpDefaultRouterAddress_Object((1,3,6,1,4,1,10876,101,2,37,13,1,2),_FsMIStdIpDefaultRouterAddress_Type())
fsMIStdIpDefaultRouterAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpDefaultRouterAddress.setStatus(_A)
_FsMIStdIpDefaultRouterIfIndex_Type=InterfaceIndex
_FsMIStdIpDefaultRouterIfIndex_Object=MibTableColumn
fsMIStdIpDefaultRouterIfIndex=_FsMIStdIpDefaultRouterIfIndex_Object((1,3,6,1,4,1,10876,101,2,37,13,1,3),_FsMIStdIpDefaultRouterIfIndex_Type())
fsMIStdIpDefaultRouterIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpDefaultRouterIfIndex.setStatus(_A)
class _FsMIStdIpDefaultRouterLifetime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIStdIpDefaultRouterLifetime_Type.__name__=_G
_FsMIStdIpDefaultRouterLifetime_Object=MibTableColumn
fsMIStdIpDefaultRouterLifetime=_FsMIStdIpDefaultRouterLifetime_Object((1,3,6,1,4,1,10876,101,2,37,13,1,4),_FsMIStdIpDefaultRouterLifetime_Type())
fsMIStdIpDefaultRouterLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpDefaultRouterLifetime.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdIpDefaultRouterLifetime.setUnits(_K)
class _FsMIStdIpDefaultRouterPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-2,-1,0,1)));namedValues=NamedValues(*(('reserved',-2),('low',-1),('medium',0),('high',1)))
_FsMIStdIpDefaultRouterPreference_Type.__name__=_F
_FsMIStdIpDefaultRouterPreference_Object=MibTableColumn
fsMIStdIpDefaultRouterPreference=_FsMIStdIpDefaultRouterPreference_Object((1,3,6,1,4,1,10876,101,2,37,13,1,5),_FsMIStdIpDefaultRouterPreference_Type())
fsMIStdIpDefaultRouterPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpDefaultRouterPreference.setStatus(_A)
_FsMIStdIpv6RouterAdvertTable_Object=MibTable
fsMIStdIpv6RouterAdvertTable=_FsMIStdIpv6RouterAdvertTable_Object((1,3,6,1,4,1,10876,101,2,37,14))
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertTable.setStatus(_A)
_FsMIStdIpv6RouterAdvertEntry_Object=MibTableRow
fsMIStdIpv6RouterAdvertEntry=_FsMIStdIpv6RouterAdvertEntry_Object((1,3,6,1,4,1,10876,101,2,37,14,1))
fsMIStdIpv6RouterAdvertEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertEntry.setStatus(_A)
_FsMIStdIpv6RouterAdvertIfIndex_Type=InterfaceIndex
_FsMIStdIpv6RouterAdvertIfIndex_Object=MibTableColumn
fsMIStdIpv6RouterAdvertIfIndex=_FsMIStdIpv6RouterAdvertIfIndex_Object((1,3,6,1,4,1,10876,101,2,37,14,1,1),_FsMIStdIpv6RouterAdvertIfIndex_Type())
fsMIStdIpv6RouterAdvertIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertIfIndex.setStatus(_A)
class _FsMIStdIpv6RouterAdvertSendAdverts_Type(TruthValue):defaultValue=2
_FsMIStdIpv6RouterAdvertSendAdverts_Type.__name__=_M
_FsMIStdIpv6RouterAdvertSendAdverts_Object=MibTableColumn
fsMIStdIpv6RouterAdvertSendAdverts=_FsMIStdIpv6RouterAdvertSendAdverts_Object((1,3,6,1,4,1,10876,101,2,37,14,1,2),_FsMIStdIpv6RouterAdvertSendAdverts_Type())
fsMIStdIpv6RouterAdvertSendAdverts.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertSendAdverts.setStatus(_A)
class _FsMIStdIpv6RouterAdvertMaxInterval_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_FsMIStdIpv6RouterAdvertMaxInterval_Type.__name__=_G
_FsMIStdIpv6RouterAdvertMaxInterval_Object=MibTableColumn
fsMIStdIpv6RouterAdvertMaxInterval=_FsMIStdIpv6RouterAdvertMaxInterval_Object((1,3,6,1,4,1,10876,101,2,37,14,1,3),_FsMIStdIpv6RouterAdvertMaxInterval_Type())
fsMIStdIpv6RouterAdvertMaxInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertMaxInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertMaxInterval.setUnits(_K)
class _FsMIStdIpv6RouterAdvertMinInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1350))
_FsMIStdIpv6RouterAdvertMinInterval_Type.__name__=_G
_FsMIStdIpv6RouterAdvertMinInterval_Object=MibTableColumn
fsMIStdIpv6RouterAdvertMinInterval=_FsMIStdIpv6RouterAdvertMinInterval_Object((1,3,6,1,4,1,10876,101,2,37,14,1,4),_FsMIStdIpv6RouterAdvertMinInterval_Type())
fsMIStdIpv6RouterAdvertMinInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertMinInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertMinInterval.setUnits(_K)
class _FsMIStdIpv6RouterAdvertManagedFlag_Type(TruthValue):defaultValue=2
_FsMIStdIpv6RouterAdvertManagedFlag_Type.__name__=_M
_FsMIStdIpv6RouterAdvertManagedFlag_Object=MibTableColumn
fsMIStdIpv6RouterAdvertManagedFlag=_FsMIStdIpv6RouterAdvertManagedFlag_Object((1,3,6,1,4,1,10876,101,2,37,14,1,5),_FsMIStdIpv6RouterAdvertManagedFlag_Type())
fsMIStdIpv6RouterAdvertManagedFlag.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertManagedFlag.setStatus(_A)
class _FsMIStdIpv6RouterAdvertOtherConfigFlag_Type(TruthValue):defaultValue=2
_FsMIStdIpv6RouterAdvertOtherConfigFlag_Type.__name__=_M
_FsMIStdIpv6RouterAdvertOtherConfigFlag_Object=MibTableColumn
fsMIStdIpv6RouterAdvertOtherConfigFlag=_FsMIStdIpv6RouterAdvertOtherConfigFlag_Object((1,3,6,1,4,1,10876,101,2,37,14,1,6),_FsMIStdIpv6RouterAdvertOtherConfigFlag_Type())
fsMIStdIpv6RouterAdvertOtherConfigFlag.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertOtherConfigFlag.setStatus(_A)
class _FsMIStdIpv6RouterAdvertLinkMTU_Type(Unsigned32):defaultValue=0
_FsMIStdIpv6RouterAdvertLinkMTU_Type.__name__=_G
_FsMIStdIpv6RouterAdvertLinkMTU_Object=MibTableColumn
fsMIStdIpv6RouterAdvertLinkMTU=_FsMIStdIpv6RouterAdvertLinkMTU_Object((1,3,6,1,4,1,10876,101,2,37,14,1,7),_FsMIStdIpv6RouterAdvertLinkMTU_Type())
fsMIStdIpv6RouterAdvertLinkMTU.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertLinkMTU.setStatus(_A)
class _FsMIStdIpv6RouterAdvertReachableTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_FsMIStdIpv6RouterAdvertReachableTime_Type.__name__=_G
_FsMIStdIpv6RouterAdvertReachableTime_Object=MibTableColumn
fsMIStdIpv6RouterAdvertReachableTime=_FsMIStdIpv6RouterAdvertReachableTime_Object((1,3,6,1,4,1,10876,101,2,37,14,1,8),_FsMIStdIpv6RouterAdvertReachableTime_Type())
fsMIStdIpv6RouterAdvertReachableTime.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertReachableTime.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertReachableTime.setUnits(_L)
class _FsMIStdIpv6RouterAdvertRetransmitTime_Type(Unsigned32):defaultValue=0
_FsMIStdIpv6RouterAdvertRetransmitTime_Type.__name__=_G
_FsMIStdIpv6RouterAdvertRetransmitTime_Object=MibTableColumn
fsMIStdIpv6RouterAdvertRetransmitTime=_FsMIStdIpv6RouterAdvertRetransmitTime_Object((1,3,6,1,4,1,10876,101,2,37,14,1,9),_FsMIStdIpv6RouterAdvertRetransmitTime_Type())
fsMIStdIpv6RouterAdvertRetransmitTime.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertRetransmitTime.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertRetransmitTime.setUnits(_L)
class _FsMIStdIpv6RouterAdvertCurHopLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIStdIpv6RouterAdvertCurHopLimit_Type.__name__=_G
_FsMIStdIpv6RouterAdvertCurHopLimit_Object=MibTableColumn
fsMIStdIpv6RouterAdvertCurHopLimit=_FsMIStdIpv6RouterAdvertCurHopLimit_Object((1,3,6,1,4,1,10876,101,2,37,14,1,10),_FsMIStdIpv6RouterAdvertCurHopLimit_Type())
fsMIStdIpv6RouterAdvertCurHopLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertCurHopLimit.setStatus(_A)
class _FsMIStdIpv6RouterAdvertDefaultLifetime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4,9000))
_FsMIStdIpv6RouterAdvertDefaultLifetime_Type.__name__=_G
_FsMIStdIpv6RouterAdvertDefaultLifetime_Object=MibTableColumn
fsMIStdIpv6RouterAdvertDefaultLifetime=_FsMIStdIpv6RouterAdvertDefaultLifetime_Object((1,3,6,1,4,1,10876,101,2,37,14,1,11),_FsMIStdIpv6RouterAdvertDefaultLifetime_Type())
fsMIStdIpv6RouterAdvertDefaultLifetime.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertDefaultLifetime.setStatus(_A)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertDefaultLifetime.setUnits(_K)
_FsMIStdIpv6RouterAdvertRowStatus_Type=RowStatus
_FsMIStdIpv6RouterAdvertRowStatus_Object=MibTableColumn
fsMIStdIpv6RouterAdvertRowStatus=_FsMIStdIpv6RouterAdvertRowStatus_Object((1,3,6,1,4,1,10876,101,2,37,14,1,12),_FsMIStdIpv6RouterAdvertRowStatus_Type())
fsMIStdIpv6RouterAdvertRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertRowStatus.setStatus(_A)
_FsMIStdIpv6RouterAdvertContextId_Type=Integer32
_FsMIStdIpv6RouterAdvertContextId_Object=MibTableColumn
fsMIStdIpv6RouterAdvertContextId=_FsMIStdIpv6RouterAdvertContextId_Object((1,3,6,1,4,1,10876,101,2,37,14,1,13),_FsMIStdIpv6RouterAdvertContextId_Type())
fsMIStdIpv6RouterAdvertContextId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIpv6RouterAdvertContextId.setStatus(_A)
_FsMIStdIcmpStatsTable_Object=MibTable
fsMIStdIcmpStatsTable=_FsMIStdIcmpStatsTable_Object((1,3,6,1,4,1,10876,101,2,37,15))
if mibBuilder.loadTexts:fsMIStdIcmpStatsTable.setStatus(_A)
_FsMIStdIcmpStatsEntry_Object=MibTableRow
fsMIStdIcmpStatsEntry=_FsMIStdIcmpStatsEntry_Object((1,3,6,1,4,1,10876,101,2,37,15,1))
fsMIStdIcmpStatsEntry.setIndexNames((0,_C,_J),(0,_C,_r))
if mibBuilder.loadTexts:fsMIStdIcmpStatsEntry.setStatus(_A)
_FsMIStdIcmpStatsIPVersion_Type=FsInetVersion
_FsMIStdIcmpStatsIPVersion_Object=MibTableColumn
fsMIStdIcmpStatsIPVersion=_FsMIStdIcmpStatsIPVersion_Object((1,3,6,1,4,1,10876,101,2,37,15,1,1),_FsMIStdIcmpStatsIPVersion_Type())
fsMIStdIcmpStatsIPVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIcmpStatsIPVersion.setStatus(_A)
_FsMIStdIcmpStatsInMsgs_Type=Counter32
_FsMIStdIcmpStatsInMsgs_Object=MibTableColumn
fsMIStdIcmpStatsInMsgs=_FsMIStdIcmpStatsInMsgs_Object((1,3,6,1,4,1,10876,101,2,37,15,1,2),_FsMIStdIcmpStatsInMsgs_Type())
fsMIStdIcmpStatsInMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIcmpStatsInMsgs.setStatus(_A)
_FsMIStdIcmpStatsInErrors_Type=Counter32
_FsMIStdIcmpStatsInErrors_Object=MibTableColumn
fsMIStdIcmpStatsInErrors=_FsMIStdIcmpStatsInErrors_Object((1,3,6,1,4,1,10876,101,2,37,15,1,3),_FsMIStdIcmpStatsInErrors_Type())
fsMIStdIcmpStatsInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIcmpStatsInErrors.setStatus(_A)
_FsMIStdIcmpStatsOutMsgs_Type=Counter32
_FsMIStdIcmpStatsOutMsgs_Object=MibTableColumn
fsMIStdIcmpStatsOutMsgs=_FsMIStdIcmpStatsOutMsgs_Object((1,3,6,1,4,1,10876,101,2,37,15,1,4),_FsMIStdIcmpStatsOutMsgs_Type())
fsMIStdIcmpStatsOutMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIcmpStatsOutMsgs.setStatus(_A)
_FsMIStdIcmpStatsOutErrors_Type=Counter32
_FsMIStdIcmpStatsOutErrors_Object=MibTableColumn
fsMIStdIcmpStatsOutErrors=_FsMIStdIcmpStatsOutErrors_Object((1,3,6,1,4,1,10876,101,2,37,15,1,5),_FsMIStdIcmpStatsOutErrors_Type())
fsMIStdIcmpStatsOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIcmpStatsOutErrors.setStatus(_A)
_FsMIStdIcmpMsgStatsTable_Object=MibTable
fsMIStdIcmpMsgStatsTable=_FsMIStdIcmpMsgStatsTable_Object((1,3,6,1,4,1,10876,101,2,37,16))
if mibBuilder.loadTexts:fsMIStdIcmpMsgStatsTable.setStatus(_A)
_FsMIStdIcmpMsgStatsEntry_Object=MibTableRow
fsMIStdIcmpMsgStatsEntry=_FsMIStdIcmpMsgStatsEntry_Object((1,3,6,1,4,1,10876,101,2,37,16,1))
fsMIStdIcmpMsgStatsEntry.setIndexNames((0,_C,_J),(0,_C,_s),(0,_C,_t))
if mibBuilder.loadTexts:fsMIStdIcmpMsgStatsEntry.setStatus(_A)
_FsMIStdIcmpMsgStatsIPVersion_Type=FsInetVersion
_FsMIStdIcmpMsgStatsIPVersion_Object=MibTableColumn
fsMIStdIcmpMsgStatsIPVersion=_FsMIStdIcmpMsgStatsIPVersion_Object((1,3,6,1,4,1,10876,101,2,37,16,1,1),_FsMIStdIcmpMsgStatsIPVersion_Type())
fsMIStdIcmpMsgStatsIPVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIcmpMsgStatsIPVersion.setStatus(_A)
class _FsMIStdIcmpMsgStatsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIStdIcmpMsgStatsType_Type.__name__=_F
_FsMIStdIcmpMsgStatsType_Object=MibTableColumn
fsMIStdIcmpMsgStatsType=_FsMIStdIcmpMsgStatsType_Object((1,3,6,1,4,1,10876,101,2,37,16,1,2),_FsMIStdIcmpMsgStatsType_Type())
fsMIStdIcmpMsgStatsType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdIcmpMsgStatsType.setStatus(_A)
_FsMIStdIcmpMsgStatsInPkts_Type=Counter32
_FsMIStdIcmpMsgStatsInPkts_Object=MibTableColumn
fsMIStdIcmpMsgStatsInPkts=_FsMIStdIcmpMsgStatsInPkts_Object((1,3,6,1,4,1,10876,101,2,37,16,1,3),_FsMIStdIcmpMsgStatsInPkts_Type())
fsMIStdIcmpMsgStatsInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIcmpMsgStatsInPkts.setStatus(_A)
_FsMIStdIcmpMsgStatsOutPkts_Type=Counter32
_FsMIStdIcmpMsgStatsOutPkts_Object=MibTableColumn
fsMIStdIcmpMsgStatsOutPkts=_FsMIStdIcmpMsgStatsOutPkts_Object((1,3,6,1,4,1,10876,101,2,37,16,1,4),_FsMIStdIcmpMsgStatsOutPkts_Type())
fsMIStdIcmpMsgStatsOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdIcmpMsgStatsOutPkts.setStatus(_A)
_FsMIStdInetCidrRouteTable_Object=MibTable
fsMIStdInetCidrRouteTable=_FsMIStdInetCidrRouteTable_Object((1,3,6,1,4,1,10876,101,2,37,17))
if mibBuilder.loadTexts:fsMIStdInetCidrRouteTable.setStatus(_A)
_FsMIStdInetCidrRouteEntry_Object=MibTableRow
fsMIStdInetCidrRouteEntry=_FsMIStdInetCidrRouteEntry_Object((1,3,6,1,4,1,10876,101,2,37,17,1))
fsMIStdInetCidrRouteEntry.setIndexNames((0,_C,_J),(0,_C,_u),(0,_C,_v),(0,_C,_w),(0,_C,_x),(0,_C,_y),(0,_C,_z))
if mibBuilder.loadTexts:fsMIStdInetCidrRouteEntry.setStatus(_A)
_FsMIStdInetCidrRouteDestType_Type=InetAddressType
_FsMIStdInetCidrRouteDestType_Object=MibTableColumn
fsMIStdInetCidrRouteDestType=_FsMIStdInetCidrRouteDestType_Object((1,3,6,1,4,1,10876,101,2,37,17,1,1),_FsMIStdInetCidrRouteDestType_Type())
fsMIStdInetCidrRouteDestType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteDestType.setStatus(_A)
class _FsMIStdInetCidrRouteDest_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIStdInetCidrRouteDest_Type.__name__=_I
_FsMIStdInetCidrRouteDest_Object=MibTableColumn
fsMIStdInetCidrRouteDest=_FsMIStdInetCidrRouteDest_Object((1,3,6,1,4,1,10876,101,2,37,17,1,2),_FsMIStdInetCidrRouteDest_Type())
fsMIStdInetCidrRouteDest.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteDest.setStatus(_A)
_FsMIStdInetCidrRoutePfxLen_Type=InetAddressPrefixLength
_FsMIStdInetCidrRoutePfxLen_Object=MibTableColumn
fsMIStdInetCidrRoutePfxLen=_FsMIStdInetCidrRoutePfxLen_Object((1,3,6,1,4,1,10876,101,2,37,17,1,3),_FsMIStdInetCidrRoutePfxLen_Type())
fsMIStdInetCidrRoutePfxLen.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdInetCidrRoutePfxLen.setStatus(_A)
_FsMIStdInetCidrRoutePolicy_Type=ObjectIdentifier
_FsMIStdInetCidrRoutePolicy_Object=MibTableColumn
fsMIStdInetCidrRoutePolicy=_FsMIStdInetCidrRoutePolicy_Object((1,3,6,1,4,1,10876,101,2,37,17,1,4),_FsMIStdInetCidrRoutePolicy_Type())
fsMIStdInetCidrRoutePolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdInetCidrRoutePolicy.setStatus(_A)
_FsMIStdInetCidrRouteNextHopType_Type=InetAddressType
_FsMIStdInetCidrRouteNextHopType_Object=MibTableColumn
fsMIStdInetCidrRouteNextHopType=_FsMIStdInetCidrRouteNextHopType_Object((1,3,6,1,4,1,10876,101,2,37,17,1,5),_FsMIStdInetCidrRouteNextHopType_Type())
fsMIStdInetCidrRouteNextHopType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteNextHopType.setStatus(_A)
class _FsMIStdInetCidrRouteNextHop_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIStdInetCidrRouteNextHop_Type.__name__=_I
_FsMIStdInetCidrRouteNextHop_Object=MibTableColumn
fsMIStdInetCidrRouteNextHop=_FsMIStdInetCidrRouteNextHop_Object((1,3,6,1,4,1,10876,101,2,37,17,1,6),_FsMIStdInetCidrRouteNextHop_Type())
fsMIStdInetCidrRouteNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteNextHop.setStatus(_A)
_FsMIStdInetCidrRouteIfIndex_Type=InterfaceIndexOrZero
_FsMIStdInetCidrRouteIfIndex_Object=MibTableColumn
fsMIStdInetCidrRouteIfIndex=_FsMIStdInetCidrRouteIfIndex_Object((1,3,6,1,4,1,10876,101,2,37,17,1,7),_FsMIStdInetCidrRouteIfIndex_Type())
fsMIStdInetCidrRouteIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteIfIndex.setStatus(_A)
class _FsMIStdInetCidrRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('reject',2),('local',3),('remote',4),('blackhole',5)))
_FsMIStdInetCidrRouteType_Type.__name__=_F
_FsMIStdInetCidrRouteType_Object=MibTableColumn
fsMIStdInetCidrRouteType=_FsMIStdInetCidrRouteType_Object((1,3,6,1,4,1,10876,101,2,37,17,1,8),_FsMIStdInetCidrRouteType_Type())
fsMIStdInetCidrRouteType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteType.setStatus(_A)
_FsMIStdInetCidrRouteProto_Type=IANAipRouteProtocol
_FsMIStdInetCidrRouteProto_Object=MibTableColumn
fsMIStdInetCidrRouteProto=_FsMIStdInetCidrRouteProto_Object((1,3,6,1,4,1,10876,101,2,37,17,1,9),_FsMIStdInetCidrRouteProto_Type())
fsMIStdInetCidrRouteProto.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteProto.setStatus(_A)
_FsMIStdInetCidrRouteAge_Type=Gauge32
_FsMIStdInetCidrRouteAge_Object=MibTableColumn
fsMIStdInetCidrRouteAge=_FsMIStdInetCidrRouteAge_Object((1,3,6,1,4,1,10876,101,2,37,17,1,10),_FsMIStdInetCidrRouteAge_Type())
fsMIStdInetCidrRouteAge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteAge.setStatus(_A)
class _FsMIStdInetCidrRouteNextHopAS_Type(InetAutonomousSystemNumber):defaultValue=0
_FsMIStdInetCidrRouteNextHopAS_Type.__name__=_P
_FsMIStdInetCidrRouteNextHopAS_Object=MibTableColumn
fsMIStdInetCidrRouteNextHopAS=_FsMIStdInetCidrRouteNextHopAS_Object((1,3,6,1,4,1,10876,101,2,37,17,1,11),_FsMIStdInetCidrRouteNextHopAS_Type())
fsMIStdInetCidrRouteNextHopAS.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteNextHopAS.setStatus(_A)
class _FsMIStdInetCidrRouteMetric1_Type(Integer32):defaultValue=-1
_FsMIStdInetCidrRouteMetric1_Type.__name__=_F
_FsMIStdInetCidrRouteMetric1_Object=MibTableColumn
fsMIStdInetCidrRouteMetric1=_FsMIStdInetCidrRouteMetric1_Object((1,3,6,1,4,1,10876,101,2,37,17,1,12),_FsMIStdInetCidrRouteMetric1_Type())
fsMIStdInetCidrRouteMetric1.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteMetric1.setStatus(_A)
class _FsMIStdInetCidrRouteMetric2_Type(Integer32):defaultValue=-1
_FsMIStdInetCidrRouteMetric2_Type.__name__=_F
_FsMIStdInetCidrRouteMetric2_Object=MibTableColumn
fsMIStdInetCidrRouteMetric2=_FsMIStdInetCidrRouteMetric2_Object((1,3,6,1,4,1,10876,101,2,37,17,1,13),_FsMIStdInetCidrRouteMetric2_Type())
fsMIStdInetCidrRouteMetric2.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteMetric2.setStatus(_A)
class _FsMIStdInetCidrRouteMetric3_Type(Integer32):defaultValue=-1
_FsMIStdInetCidrRouteMetric3_Type.__name__=_F
_FsMIStdInetCidrRouteMetric3_Object=MibTableColumn
fsMIStdInetCidrRouteMetric3=_FsMIStdInetCidrRouteMetric3_Object((1,3,6,1,4,1,10876,101,2,37,17,1,14),_FsMIStdInetCidrRouteMetric3_Type())
fsMIStdInetCidrRouteMetric3.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteMetric3.setStatus(_A)
class _FsMIStdInetCidrRouteMetric4_Type(Integer32):defaultValue=-1
_FsMIStdInetCidrRouteMetric4_Type.__name__=_F
_FsMIStdInetCidrRouteMetric4_Object=MibTableColumn
fsMIStdInetCidrRouteMetric4=_FsMIStdInetCidrRouteMetric4_Object((1,3,6,1,4,1,10876,101,2,37,17,1,15),_FsMIStdInetCidrRouteMetric4_Type())
fsMIStdInetCidrRouteMetric4.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteMetric4.setStatus(_A)
class _FsMIStdInetCidrRouteMetric5_Type(Integer32):defaultValue=-1
_FsMIStdInetCidrRouteMetric5_Type.__name__=_F
_FsMIStdInetCidrRouteMetric5_Object=MibTableColumn
fsMIStdInetCidrRouteMetric5=_FsMIStdInetCidrRouteMetric5_Object((1,3,6,1,4,1,10876,101,2,37,17,1,16),_FsMIStdInetCidrRouteMetric5_Type())
fsMIStdInetCidrRouteMetric5.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteMetric5.setStatus(_A)
_FsMIStdInetCidrRouteStatus_Type=RowStatus
_FsMIStdInetCidrRouteStatus_Object=MibTableColumn
fsMIStdInetCidrRouteStatus=_FsMIStdInetCidrRouteStatus_Object((1,3,6,1,4,1,10876,101,2,37,17,1,17),_FsMIStdInetCidrRouteStatus_Type())
fsMIStdInetCidrRouteStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteStatus.setStatus(_A)
class _FsMIStdInetCidrRouteAddrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_FsMIStdInetCidrRouteAddrType_Type.__name__=_F
_FsMIStdInetCidrRouteAddrType_Object=MibTableColumn
fsMIStdInetCidrRouteAddrType=_FsMIStdInetCidrRouteAddrType_Object((1,3,6,1,4,1,10876,101,2,37,17,1,18),_FsMIStdInetCidrRouteAddrType_Type())
fsMIStdInetCidrRouteAddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteAddrType.setStatus(_A)
class _FsMIStdInetCidrRouteHWStatus_Type(Bits):namedValues=NamedValues(*(('bestRoute',40),('hardwareStatus',80),(_l,100)))
_FsMIStdInetCidrRouteHWStatus_Type.__name__='Bits'
_FsMIStdInetCidrRouteHWStatus_Object=MibTableColumn
fsMIStdInetCidrRouteHWStatus=_FsMIStdInetCidrRouteHWStatus_Object((1,3,6,1,4,1,10876,101,2,37,17,1,19),_FsMIStdInetCidrRouteHWStatus_Type())
fsMIStdInetCidrRouteHWStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdInetCidrRouteHWStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'FsInetVersion':FsInetVersion,'fsMIStdIp':fsMIStdIp,'fsMIStdIpv4InterfaceTableLastChange':fsMIStdIpv4InterfaceTableLastChange,'fsMIStdIpv6InterfaceTableLastChange':fsMIStdIpv6InterfaceTableLastChange,'fsMIStdIpIfStatsTableLastChange':fsMIStdIpIfStatsTableLastChange,'fsMIStdIpGlobalTable':fsMIStdIpGlobalTable,'fsMIStdIpGlobalEntry':fsMIStdIpGlobalEntry,_J:fsMIStdIpContextId,'fsMIStdIpForwarding':fsMIStdIpForwarding,'fsMIStdIpDefaultTTL':fsMIStdIpDefaultTTL,'fsMIStdIpReasmTimeout':fsMIStdIpReasmTimeout,'fsMIStdIpv6IpForwarding':fsMIStdIpv6IpForwarding,'fsMIStdIpv6IpDefaultHopLimit':fsMIStdIpv6IpDefaultHopLimit,'fsMIStdInetCidrRouteNumber':fsMIStdInetCidrRouteNumber,'fsMIStdInetCidrRouteDiscards':fsMIStdInetCidrRouteDiscards,'fsMIStdIpv4InterfaceTable':fsMIStdIpv4InterfaceTable,'fsMIStdIpv4InterfaceEntry':fsMIStdIpv4InterfaceEntry,_T:fsMIStdIpv4InterfaceIfIndex,'fsMIStdIpv4InterfaceReasmMaxSize':fsMIStdIpv4InterfaceReasmMaxSize,'fsMIStdIpv4InterfaceEnableStatus':fsMIStdIpv4InterfaceEnableStatus,'fsMIStdIpv4InterfaceRetransmitTime':fsMIStdIpv4InterfaceRetransmitTime,'fsMIStdIpv4IfContextId':fsMIStdIpv4IfContextId,'fsMIStdIpv6InterfaceTable':fsMIStdIpv6InterfaceTable,'fsMIStdIpv6InterfaceEntry':fsMIStdIpv6InterfaceEntry,_U:fsMIStdIpv6InterfaceIfIndex,'fsMIStdIpv6InterfaceReasmMaxSize':fsMIStdIpv6InterfaceReasmMaxSize,'fsMIStdIpv6InterfaceIdentifier':fsMIStdIpv6InterfaceIdentifier,'fsMIStdIpv6InterfaceEnableStatus':fsMIStdIpv6InterfaceEnableStatus,'fsMIStdIpv6InterfaceReachableTime':fsMIStdIpv6InterfaceReachableTime,'fsMIStdIpv6InterfaceRetransmitTime':fsMIStdIpv6InterfaceRetransmitTime,'fsMIStdIpv6InterfaceForwarding':fsMIStdIpv6InterfaceForwarding,'fsMIStdIpv6IfContextId':fsMIStdIpv6IfContextId,'fsMIStdIpSystemStatsTable':fsMIStdIpSystemStatsTable,'fsMIStdIpSystemStatsEntry':fsMIStdIpSystemStatsEntry,_V:fsMIStdIpSystemStatsIPVersion,'fsMIStdIpSystemStatsInReceives':fsMIStdIpSystemStatsInReceives,'fsMIStdIpSystemStatsHCInReceives':fsMIStdIpSystemStatsHCInReceives,'fsMIStdIpSystemStatsInOctets':fsMIStdIpSystemStatsInOctets,'fsMIStdIpSystemStatsHCInOctets':fsMIStdIpSystemStatsHCInOctets,'fsMIStdIpSystemStatsInHdrErrors':fsMIStdIpSystemStatsInHdrErrors,'fsMIStdIpSystemStatsInNoRoutes':fsMIStdIpSystemStatsInNoRoutes,'fsMIStdIpSystemStatsInAddrErrors':fsMIStdIpSystemStatsInAddrErrors,'fsMIStdIpSystemStatsInUnknownProtos':fsMIStdIpSystemStatsInUnknownProtos,'fsMIStdIpSystemStatsInTruncatedPkts':fsMIStdIpSystemStatsInTruncatedPkts,'fsMIStdIpSystemStatsInForwDatagrams':fsMIStdIpSystemStatsInForwDatagrams,'fsMIStdIpSystemStatsHCInForwDatagrams':fsMIStdIpSystemStatsHCInForwDatagrams,'fsMIStdIpSystemStatsReasmReqds':fsMIStdIpSystemStatsReasmReqds,'fsMIStdIpSystemStatsReasmOKs':fsMIStdIpSystemStatsReasmOKs,'fsMIStdIpSystemStatsReasmFails':fsMIStdIpSystemStatsReasmFails,'fsMIStdIpSystemStatsInDiscards':fsMIStdIpSystemStatsInDiscards,'fsMIStdIpSystemStatsInDelivers':fsMIStdIpSystemStatsInDelivers,'fsMIStdIpSystemStatsHCInDelivers':fsMIStdIpSystemStatsHCInDelivers,'fsMIStdIpSystemStatsOutRequests':fsMIStdIpSystemStatsOutRequests,'fsMIStdIpSystemStatsHCOutRequests':fsMIStdIpSystemStatsHCOutRequests,'fsMIStdIpSystemStatsOutNoRoutes':fsMIStdIpSystemStatsOutNoRoutes,'fsMIStdIpSystemStatsOutForwDatagrams':fsMIStdIpSystemStatsOutForwDatagrams,'fsMIStdIpSystemStatsHCOutForwDatagrams':fsMIStdIpSystemStatsHCOutForwDatagrams,'fsMIStdIpSystemStatsOutDiscards':fsMIStdIpSystemStatsOutDiscards,'fsMIStdIpSystemStatsOutFragReqds':fsMIStdIpSystemStatsOutFragReqds,'fsMIStdIpSystemStatsOutFragOKs':fsMIStdIpSystemStatsOutFragOKs,'fsMIStdIpSystemStatsOutFragFails':fsMIStdIpSystemStatsOutFragFails,'fsMIStdIpSystemStatsOutFragCreates':fsMIStdIpSystemStatsOutFragCreates,'fsMIStdIpSystemStatsOutTransmits':fsMIStdIpSystemStatsOutTransmits,'fsMIStdIpSystemStatsHCOutTransmits':fsMIStdIpSystemStatsHCOutTransmits,'fsMIStdIpSystemStatsOutOctets':fsMIStdIpSystemStatsOutOctets,'fsMIStdIpSystemStatsHCOutOctets':fsMIStdIpSystemStatsHCOutOctets,'fsMIStdIpSystemStatsInMcastPkts':fsMIStdIpSystemStatsInMcastPkts,'fsMIStdIpSystemStatsHCInMcastPkts':fsMIStdIpSystemStatsHCInMcastPkts,'fsMIStdIpSystemStatsInMcastOctets':fsMIStdIpSystemStatsInMcastOctets,'fsMIStdIpSystemStatsHCInMcastOctets':fsMIStdIpSystemStatsHCInMcastOctets,'fsMIStdIpSystemStatsOutMcastPkts':fsMIStdIpSystemStatsOutMcastPkts,'fsMIStdIpSystemStatsHCOutMcastPkts':fsMIStdIpSystemStatsHCOutMcastPkts,'fsMIStdIpSystemStatsOutMcastOctets':fsMIStdIpSystemStatsOutMcastOctets,'fsMIStdIpSystemStatsHCOutMcastOctets':fsMIStdIpSystemStatsHCOutMcastOctets,'fsMIStdIpSystemStatsInBcastPkts':fsMIStdIpSystemStatsInBcastPkts,'fsMIStdIpSystemStatsHCInBcastPkts':fsMIStdIpSystemStatsHCInBcastPkts,'fsMIStdIpSystemStatsOutBcastPkts':fsMIStdIpSystemStatsOutBcastPkts,'fsMIStdIpSystemStatsHCOutBcastPkts':fsMIStdIpSystemStatsHCOutBcastPkts,'fsMIStdIpSystemStatsDiscontinuityTime':fsMIStdIpSystemStatsDiscontinuityTime,'fsMIStdIpSystemStatsRefreshRate':fsMIStdIpSystemStatsRefreshRate,'fsMIStdIpIfStatsTable':fsMIStdIpIfStatsTable,'fsMIStdIpIfStatsEntry':fsMIStdIpIfStatsEntry,_X:fsMIStdIpIfStatsIPVersion,_Y:fsMIStdIpIfStatsIfIndex,'fsMIStdIpIfStatsInReceives':fsMIStdIpIfStatsInReceives,'fsMIStdIpIfStatsHCInReceives':fsMIStdIpIfStatsHCInReceives,'fsMIStdIpIfStatsInOctets':fsMIStdIpIfStatsInOctets,'fsMIStdIpIfStatsHCInOctets':fsMIStdIpIfStatsHCInOctets,'fsMIStdIpIfStatsInHdrErrors':fsMIStdIpIfStatsInHdrErrors,'fsMIStdIpIfStatsInNoRoutes':fsMIStdIpIfStatsInNoRoutes,'fsMIStdIpIfStatsInAddrErrors':fsMIStdIpIfStatsInAddrErrors,'fsMIStdIpIfStatsInUnknownProtos':fsMIStdIpIfStatsInUnknownProtos,'fsMIStdIpIfStatsInTruncatedPkts':fsMIStdIpIfStatsInTruncatedPkts,'fsMIStdIpIfStatsInForwDatagrams':fsMIStdIpIfStatsInForwDatagrams,'fsMIStdIpIfStatsHCInForwDatagrams':fsMIStdIpIfStatsHCInForwDatagrams,'fsMIStdIpIfStatsReasmReqds':fsMIStdIpIfStatsReasmReqds,'fsMIStdIpIfStatsReasmOKs':fsMIStdIpIfStatsReasmOKs,'fsMIStdIpIfStatsReasmFails':fsMIStdIpIfStatsReasmFails,'fsMIStdIpIfStatsInDiscards':fsMIStdIpIfStatsInDiscards,'fsMIStdIpIfStatsInDelivers':fsMIStdIpIfStatsInDelivers,'fsMIStdIpIfStatsHCInDelivers':fsMIStdIpIfStatsHCInDelivers,'fsMIStdIpIfStatsOutRequests':fsMIStdIpIfStatsOutRequests,'fsMIStdIpIfStatsHCOutRequests':fsMIStdIpIfStatsHCOutRequests,'fsMIStdIpIfStatsOutForwDatagrams':fsMIStdIpIfStatsOutForwDatagrams,'fsMIStdIpIfStatsHCOutForwDatagrams':fsMIStdIpIfStatsHCOutForwDatagrams,'fsMIStdIpIfStatsOutDiscards':fsMIStdIpIfStatsOutDiscards,'fsMIStdIpIfStatsOutFragReqds':fsMIStdIpIfStatsOutFragReqds,'fsMIStdIpIfStatsOutFragOKs':fsMIStdIpIfStatsOutFragOKs,'fsMIStdIpIfStatsOutFragFails':fsMIStdIpIfStatsOutFragFails,'fsMIStdIpIfStatsOutFragCreates':fsMIStdIpIfStatsOutFragCreates,'fsMIStdIpIfStatsOutTransmits':fsMIStdIpIfStatsOutTransmits,'fsMIStdIpIfStatsHCOutTransmits':fsMIStdIpIfStatsHCOutTransmits,'fsMIStdIpIfStatsOutOctets':fsMIStdIpIfStatsOutOctets,'fsMIStdIpIfStatsHCOutOctets':fsMIStdIpIfStatsHCOutOctets,'fsMIStdIpIfStatsInMcastPkts':fsMIStdIpIfStatsInMcastPkts,'fsMIStdIpIfStatsHCInMcastPkts':fsMIStdIpIfStatsHCInMcastPkts,'fsMIStdIpIfStatsInMcastOctets':fsMIStdIpIfStatsInMcastOctets,'fsMIStdIpIfStatsHCInMcastOctets':fsMIStdIpIfStatsHCInMcastOctets,'fsMIStdIpIfStatsOutMcastPkts':fsMIStdIpIfStatsOutMcastPkts,'fsMIStdIpIfStatsHCOutMcastPkts':fsMIStdIpIfStatsHCOutMcastPkts,'fsMIStdIpIfStatsOutMcastOctets':fsMIStdIpIfStatsOutMcastOctets,'fsMIStdIpIfStatsHCOutMcastOctets':fsMIStdIpIfStatsHCOutMcastOctets,'fsMIStdIpIfStatsInBcastPkts':fsMIStdIpIfStatsInBcastPkts,'fsMIStdIpIfStatsHCInBcastPkts':fsMIStdIpIfStatsHCInBcastPkts,'fsMIStdIpIfStatsOutBcastPkts':fsMIStdIpIfStatsOutBcastPkts,'fsMIStdIpIfStatsHCOutBcastPkts':fsMIStdIpIfStatsHCOutBcastPkts,'fsMIStdIpIfStatsDiscontinuityTime':fsMIStdIpIfStatsDiscontinuityTime,'fsMIStdIpIfStatsRefreshRate':fsMIStdIpIfStatsRefreshRate,'fsMIStdIpIfStatsContextId':fsMIStdIpIfStatsContextId,'fsMIStdIpAddressPrefixTable':fsMIStdIpAddressPrefixTable,'fsMIStdIpAddressPrefixEntry':fsMIStdIpAddressPrefixEntry,_Z:fsMIStdIpAddressPrefixIfIndex,_a:fsMIStdIpAddressPrefixType,_b:fsMIStdIpAddressPrefixPrefix,_c:fsMIStdIpAddressPrefixLength,'fsMIStdIpAddressPrefixOrigin':fsMIStdIpAddressPrefixOrigin,'fsMIStdIpAddressPrefixOnLinkFlag':fsMIStdIpAddressPrefixOnLinkFlag,'fsMIStdIpAddressPrefixAutonomousFlag':fsMIStdIpAddressPrefixAutonomousFlag,'fsMIStdIpAddressPrefixAdvPreferredLifetime':fsMIStdIpAddressPrefixAdvPreferredLifetime,'fsMIStdIpAddressPrefixAdvValidLifetime':fsMIStdIpAddressPrefixAdvValidLifetime,'fsMIStdIpAddressContextId':fsMIStdIpAddressContextId,'fsMIStdIpAddressTable':fsMIStdIpAddressTable,'fsMIStdIpAddressEntry':fsMIStdIpAddressEntry,_d:fsMIStdIpAddressAddrType,_e:fsMIStdIpAddressAddr,'fsMIStdIpAddressIfIndex':fsMIStdIpAddressIfIndex,'fsMIStdIpAddressType':fsMIStdIpAddressType,'fsMIStdIpAddressPrefix':fsMIStdIpAddressPrefix,'fsMIStdIpAddressOrigin':fsMIStdIpAddressOrigin,'fsMIStdIpAddressStatus':fsMIStdIpAddressStatus,'fsMIStdIpAddressCreated':fsMIStdIpAddressCreated,'fsMIStdIpAddressLastChanged':fsMIStdIpAddressLastChanged,'fsMIStdIpAddressRowStatus':fsMIStdIpAddressRowStatus,'fsMIStdIpAddressStorageType':fsMIStdIpAddressStorageType,'fsMIStdIpNetToPhysicalTable':fsMIStdIpNetToPhysicalTable,'fsMIStdIpNetToPhysicalEntry':fsMIStdIpNetToPhysicalEntry,_h:fsMIStdIpNetToPhysicalIfIndex,_i:fsMIStdIpNetToPhysicalNetAddressType,_j:fsMIStdIpNetToPhysicalNetAddress,'fsMIStdIpNetToPhysicalPhysAddress':fsMIStdIpNetToPhysicalPhysAddress,'fsMIStdIpNetToPhysicalLastUpdated':fsMIStdIpNetToPhysicalLastUpdated,'fsMIStdIpNetToPhysicalType':fsMIStdIpNetToPhysicalType,'fsMIStdIpNetToPhysicalState':fsMIStdIpNetToPhysicalState,'fsMIStdIpNetToPhysicalRowStatus':fsMIStdIpNetToPhysicalRowStatus,'fsMIStdIpNetToPhysicalContextId':fsMIStdIpNetToPhysicalContextId,'fsMIStdIpv6ScopeZoneIndexTable':fsMIStdIpv6ScopeZoneIndexTable,'fsMIStdIpv6ScopeZoneIndexEntry':fsMIStdIpv6ScopeZoneIndexEntry,_m:fsMIStdIpv6ScopeZoneIndexIfIndex,'fsMIStdIpv6ScopeZoneIndexLinkLocal':fsMIStdIpv6ScopeZoneIndexLinkLocal,'fsMIStdIpv6ScopeZoneIndex3':fsMIStdIpv6ScopeZoneIndex3,'fsMIStdIpv6ScopeZoneIndexAdminLocal':fsMIStdIpv6ScopeZoneIndexAdminLocal,'fsMIStdIpv6ScopeZoneIndexSiteLocal':fsMIStdIpv6ScopeZoneIndexSiteLocal,'fsMIStdIpv6ScopeZoneIndex6':fsMIStdIpv6ScopeZoneIndex6,'fsMIStdIpv6ScopeZoneIndex7':fsMIStdIpv6ScopeZoneIndex7,'fsMIStdIpv6ScopeZoneIndexOrganizationLocal':fsMIStdIpv6ScopeZoneIndexOrganizationLocal,'fsMIStdIpv6ScopeZoneIndex9':fsMIStdIpv6ScopeZoneIndex9,'fsMIStdIpv6ScopeZoneIndexA':fsMIStdIpv6ScopeZoneIndexA,'fsMIStdIpv6ScopeZoneIndexB':fsMIStdIpv6ScopeZoneIndexB,'fsMIStdIpv6ScopeZoneIndexC':fsMIStdIpv6ScopeZoneIndexC,'fsMIStdIpv6ScopeZoneIndexD':fsMIStdIpv6ScopeZoneIndexD,'fsMIStdIpv6ScopeZoneContextId':fsMIStdIpv6ScopeZoneContextId,'fsMIStdIpDefaultRouterTable':fsMIStdIpDefaultRouterTable,'fsMIStdIpDefaultRouterEntry':fsMIStdIpDefaultRouterEntry,_n:fsMIStdIpDefaultRouterAddressType,_o:fsMIStdIpDefaultRouterAddress,_p:fsMIStdIpDefaultRouterIfIndex,'fsMIStdIpDefaultRouterLifetime':fsMIStdIpDefaultRouterLifetime,'fsMIStdIpDefaultRouterPreference':fsMIStdIpDefaultRouterPreference,'fsMIStdIpv6RouterAdvertTable':fsMIStdIpv6RouterAdvertTable,'fsMIStdIpv6RouterAdvertEntry':fsMIStdIpv6RouterAdvertEntry,_q:fsMIStdIpv6RouterAdvertIfIndex,'fsMIStdIpv6RouterAdvertSendAdverts':fsMIStdIpv6RouterAdvertSendAdverts,'fsMIStdIpv6RouterAdvertMaxInterval':fsMIStdIpv6RouterAdvertMaxInterval,'fsMIStdIpv6RouterAdvertMinInterval':fsMIStdIpv6RouterAdvertMinInterval,'fsMIStdIpv6RouterAdvertManagedFlag':fsMIStdIpv6RouterAdvertManagedFlag,'fsMIStdIpv6RouterAdvertOtherConfigFlag':fsMIStdIpv6RouterAdvertOtherConfigFlag,'fsMIStdIpv6RouterAdvertLinkMTU':fsMIStdIpv6RouterAdvertLinkMTU,'fsMIStdIpv6RouterAdvertReachableTime':fsMIStdIpv6RouterAdvertReachableTime,'fsMIStdIpv6RouterAdvertRetransmitTime':fsMIStdIpv6RouterAdvertRetransmitTime,'fsMIStdIpv6RouterAdvertCurHopLimit':fsMIStdIpv6RouterAdvertCurHopLimit,'fsMIStdIpv6RouterAdvertDefaultLifetime':fsMIStdIpv6RouterAdvertDefaultLifetime,'fsMIStdIpv6RouterAdvertRowStatus':fsMIStdIpv6RouterAdvertRowStatus,'fsMIStdIpv6RouterAdvertContextId':fsMIStdIpv6RouterAdvertContextId,'fsMIStdIcmpStatsTable':fsMIStdIcmpStatsTable,'fsMIStdIcmpStatsEntry':fsMIStdIcmpStatsEntry,_r:fsMIStdIcmpStatsIPVersion,'fsMIStdIcmpStatsInMsgs':fsMIStdIcmpStatsInMsgs,'fsMIStdIcmpStatsInErrors':fsMIStdIcmpStatsInErrors,'fsMIStdIcmpStatsOutMsgs':fsMIStdIcmpStatsOutMsgs,'fsMIStdIcmpStatsOutErrors':fsMIStdIcmpStatsOutErrors,'fsMIStdIcmpMsgStatsTable':fsMIStdIcmpMsgStatsTable,'fsMIStdIcmpMsgStatsEntry':fsMIStdIcmpMsgStatsEntry,_s:fsMIStdIcmpMsgStatsIPVersion,_t:fsMIStdIcmpMsgStatsType,'fsMIStdIcmpMsgStatsInPkts':fsMIStdIcmpMsgStatsInPkts,'fsMIStdIcmpMsgStatsOutPkts':fsMIStdIcmpMsgStatsOutPkts,'fsMIStdInetCidrRouteTable':fsMIStdInetCidrRouteTable,'fsMIStdInetCidrRouteEntry':fsMIStdInetCidrRouteEntry,_u:fsMIStdInetCidrRouteDestType,_v:fsMIStdInetCidrRouteDest,_w:fsMIStdInetCidrRoutePfxLen,_x:fsMIStdInetCidrRoutePolicy,_y:fsMIStdInetCidrRouteNextHopType,_z:fsMIStdInetCidrRouteNextHop,'fsMIStdInetCidrRouteIfIndex':fsMIStdInetCidrRouteIfIndex,'fsMIStdInetCidrRouteType':fsMIStdInetCidrRouteType,'fsMIStdInetCidrRouteProto':fsMIStdInetCidrRouteProto,'fsMIStdInetCidrRouteAge':fsMIStdInetCidrRouteAge,'fsMIStdInetCidrRouteNextHopAS':fsMIStdInetCidrRouteNextHopAS,'fsMIStdInetCidrRouteMetric1':fsMIStdInetCidrRouteMetric1,'fsMIStdInetCidrRouteMetric2':fsMIStdInetCidrRouteMetric2,'fsMIStdInetCidrRouteMetric3':fsMIStdInetCidrRouteMetric3,'fsMIStdInetCidrRouteMetric4':fsMIStdInetCidrRouteMetric4,'fsMIStdInetCidrRouteMetric5':fsMIStdInetCidrRouteMetric5,'fsMIStdInetCidrRouteStatus':fsMIStdInetCidrRouteStatus,'fsMIStdInetCidrRouteAddrType':fsMIStdInetCidrRouteAddrType,'fsMIStdInetCidrRouteHWStatus':fsMIStdInetCidrRouteHWStatus})