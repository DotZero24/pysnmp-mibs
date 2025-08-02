_AE='fsipv6Protocol'
_AD='fsipv6RouteNextHop'
_AC='fsipv6RouteProtocol'
_AB='fsipv6RoutePfxLength'
_AA='fsipv6RouteDest'
_A9='fsipv6RARoutePrefixLen'
_A8='fsipv6RARoutePrefix'
_A7='fsipv6RARouteIfIndex'
_A6='fsipv6SENDDrpPktType'
_A5='fsipv6SENDRcvPktType'
_A4='fsipv6SENDSentPktType'
_A3='fsipv6ScopeZoneName'
_A2='overridden'
_A1='fsipv6ScopeZoneIndexIfIndex'
_A0='fsipv6AddrSelPolicyIfIndex'
_z='fsipv6AddrSelPolicyPrefixLen'
_y='fsipv6AddrSelPolicyPrefix'
_x='fsipv6NdProxyAddr'
_w='create'
_v='fsipv6PingIndex'
_u='fsipv6NdWanCacheIPv6Addr'
_t='fsipv6NdWanCacheIfIndex'
_s='static'
_r='fsipv6NdLanCacheIPv6Addr'
_q='fsipv6NdLanCacheIfIndex'
_p='fsipv6PmtuDest'
_o='variable'
_n='fsipv6AddrProfileIndex'
_m='fsipv6AddrPrefixLen'
_l='fsipv6AddrAddress'
_k='fsipv6AddrIndex'
_j='fsipv6PrefixAddrLen'
_i='fsipv6PrefixAddress'
_h='fsipv6PrefixIndex'
_g='fsipv6IfStatsIndex'
_f='medium'
_e='inprogress'
_d='disable'
_c='enable'
_b='cpa'
_a='cps'
_Z='automatic'
_Y='reachable'
_X='unicast'
_W='other'
_V='off'
_U='on'
_T='valid'
_S='anycast'
_R='local'
_Q='down'
_P='TruthValue'
_O='invalid'
_N='read-create'
_M='fsipv6IfIndex'
_L='Invalid'
_K='disabled'
_J='enabled'
_I='DisplayString'
_H='Unsigned32'
_G='OctetString'
_F='not-accessible'
_E='ARICENT-IPV6-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetScopeType,InetZoneIndex=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetScopeType','InetZoneIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention',_P)
futureipv6=ModuleIdentity((1,3,6,1,4,1,2076,28))
if mibBuilder.loadTexts:futureipv6.setRevisions(('2012-09-05 00:00','1999-12-17 13:30'))
class InterfaceList(TextualConvention,OctetString):status=_A
class Ipv6Address(TextualConvention,OctetString):status=_A;displayHint='2x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Fsipv6_ObjectIdentity=ObjectIdentity
fsipv6=_Fsipv6_ObjectIdentity((1,3,6,1,4,1,2076,28,1))
_Fsipv6Scalars_ObjectIdentity=ObjectIdentity
fsipv6Scalars=_Fsipv6Scalars_ObjectIdentity((1,3,6,1,4,1,2076,28,1,1))
class _Fsipv6NdCacheMaxRetries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Fsipv6NdCacheMaxRetries_Type.__name__=_D
_Fsipv6NdCacheMaxRetries_Object=MibScalar
fsipv6NdCacheMaxRetries=_Fsipv6NdCacheMaxRetries_Object((1,3,6,1,4,1,2076,28,1,1,1),_Fsipv6NdCacheMaxRetries_Type())
fsipv6NdCacheMaxRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6NdCacheMaxRetries.setStatus(_A)
class _Fsipv6PmtuConfigStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_Fsipv6PmtuConfigStatus_Type.__name__=_D
_Fsipv6PmtuConfigStatus_Object=MibScalar
fsipv6PmtuConfigStatus=_Fsipv6PmtuConfigStatus_Object((1,3,6,1,4,1,2076,28,1,1,2),_Fsipv6PmtuConfigStatus_Type())
fsipv6PmtuConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PmtuConfigStatus.setStatus(_A)
class _Fsipv6PmtuTimeOutInterval_Type(Unsigned32):defaultValue=60
_Fsipv6PmtuTimeOutInterval_Type.__name__=_H
_Fsipv6PmtuTimeOutInterval_Object=MibScalar
fsipv6PmtuTimeOutInterval=_Fsipv6PmtuTimeOutInterval_Object((1,3,6,1,4,1,2076,28,1,1,3),_Fsipv6PmtuTimeOutInterval_Type())
fsipv6PmtuTimeOutInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PmtuTimeOutInterval.setStatus(_A)
class _Fsipv6JumboEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_Fsipv6JumboEnable_Type.__name__=_D
_Fsipv6JumboEnable_Object=MibScalar
fsipv6JumboEnable=_Fsipv6JumboEnable_Object((1,3,6,1,4,1,2076,28,1,1,4),_Fsipv6JumboEnable_Type())
fsipv6JumboEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6JumboEnable.setStatus(_A)
_Fsipv6NumOfSendJumbo_Type=Integer32
_Fsipv6NumOfSendJumbo_Object=MibScalar
fsipv6NumOfSendJumbo=_Fsipv6NumOfSendJumbo_Object((1,3,6,1,4,1,2076,28,1,1,5),_Fsipv6NumOfSendJumbo_Type())
fsipv6NumOfSendJumbo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6NumOfSendJumbo.setStatus(_A)
_Fsipv6NumOfRecvJumbo_Type=Integer32
_Fsipv6NumOfRecvJumbo_Object=MibScalar
fsipv6NumOfRecvJumbo=_Fsipv6NumOfRecvJumbo_Object((1,3,6,1,4,1,2076,28,1,1,6),_Fsipv6NumOfRecvJumbo_Type())
fsipv6NumOfRecvJumbo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6NumOfRecvJumbo.setStatus(_A)
_Fsipv6ErrJumbo_Type=Integer32
_Fsipv6ErrJumbo_Object=MibScalar
fsipv6ErrJumbo=_Fsipv6ErrJumbo_Object((1,3,6,1,4,1,2076,28,1,1,7),_Fsipv6ErrJumbo_Type())
fsipv6ErrJumbo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6ErrJumbo.setStatus(_A)
_Fsipv6GlobalDebug_Type=Unsigned32
_Fsipv6GlobalDebug_Object=MibScalar
fsipv6GlobalDebug=_Fsipv6GlobalDebug_Object((1,3,6,1,4,1,2076,28,1,1,8),_Fsipv6GlobalDebug_Type())
fsipv6GlobalDebug.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6GlobalDebug.setStatus(_A)
_Fsipv6MaxRouteEntries_Type=Unsigned32
_Fsipv6MaxRouteEntries_Object=MibScalar
fsipv6MaxRouteEntries=_Fsipv6MaxRouteEntries_Object((1,3,6,1,4,1,2076,28,1,1,9),_Fsipv6MaxRouteEntries_Type())
fsipv6MaxRouteEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6MaxRouteEntries.setStatus(_A)
_Fsipv6MaxLogicalIfaces_Type=Unsigned32
_Fsipv6MaxLogicalIfaces_Object=MibScalar
fsipv6MaxLogicalIfaces=_Fsipv6MaxLogicalIfaces_Object((1,3,6,1,4,1,2076,28,1,1,10),_Fsipv6MaxLogicalIfaces_Type())
fsipv6MaxLogicalIfaces.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6MaxLogicalIfaces.setStatus(_A)
_Fsipv6MaxTunnelIfaces_Type=Unsigned32
_Fsipv6MaxTunnelIfaces_Object=MibScalar
fsipv6MaxTunnelIfaces=_Fsipv6MaxTunnelIfaces_Object((1,3,6,1,4,1,2076,28,1,1,11),_Fsipv6MaxTunnelIfaces_Type())
fsipv6MaxTunnelIfaces.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6MaxTunnelIfaces.setStatus(_A)
_Fsipv6MaxAddresses_Type=Unsigned32
_Fsipv6MaxAddresses_Object=MibScalar
fsipv6MaxAddresses=_Fsipv6MaxAddresses_Object((1,3,6,1,4,1,2076,28,1,1,12),_Fsipv6MaxAddresses_Type())
fsipv6MaxAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6MaxAddresses.setStatus(_A)
_Fsipv6MaxFragReasmEntries_Type=Unsigned32
_Fsipv6MaxFragReasmEntries_Object=MibScalar
fsipv6MaxFragReasmEntries=_Fsipv6MaxFragReasmEntries_Object((1,3,6,1,4,1,2076,28,1,1,13),_Fsipv6MaxFragReasmEntries_Type())
fsipv6MaxFragReasmEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6MaxFragReasmEntries.setStatus(_A)
_Fsipv6Nd6MaxCacheEntries_Type=Unsigned32
_Fsipv6Nd6MaxCacheEntries_Object=MibScalar
fsipv6Nd6MaxCacheEntries=_Fsipv6Nd6MaxCacheEntries_Object((1,3,6,1,4,1,2076,28,1,1,14),_Fsipv6Nd6MaxCacheEntries_Type())
fsipv6Nd6MaxCacheEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6Nd6MaxCacheEntries.setStatus(_A)
_Fsipv6PmtuMaxDest_Type=Unsigned32
_Fsipv6PmtuMaxDest_Object=MibScalar
fsipv6PmtuMaxDest=_Fsipv6PmtuMaxDest_Object((1,3,6,1,4,1,2076,28,1,1,15),_Fsipv6PmtuMaxDest_Type())
fsipv6PmtuMaxDest.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PmtuMaxDest.setStatus(_A)
class _Fsipv6RFC5095Compatibility_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Fsipv6RFC5095Compatibility_Type.__name__=_D
_Fsipv6RFC5095Compatibility_Object=MibScalar
fsipv6RFC5095Compatibility=_Fsipv6RFC5095Compatibility_Object((1,3,6,1,4,1,2076,28,1,1,16),_Fsipv6RFC5095Compatibility_Type())
fsipv6RFC5095Compatibility.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6RFC5095Compatibility.setStatus(_A)
class _Fsipv6RFC5942Compatibility_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Fsipv6RFC5942Compatibility_Type.__name__=_D
_Fsipv6RFC5942Compatibility_Object=MibScalar
fsipv6RFC5942Compatibility=_Fsipv6RFC5942Compatibility_Object((1,3,6,1,4,1,2076,28,1,1,17),_Fsipv6RFC5942Compatibility_Type())
fsipv6RFC5942Compatibility.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6RFC5942Compatibility.setStatus(_A)
class _Fsipv6SENDSecLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fsipv6SENDSecLevel_Type.__name__=_D
_Fsipv6SENDSecLevel_Object=MibScalar
fsipv6SENDSecLevel=_Fsipv6SENDSecLevel_Object((1,3,6,1,4,1,2076,28,1,1,18),_Fsipv6SENDSecLevel_Type())
fsipv6SENDSecLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6SENDSecLevel.setStatus(_A)
class _Fsipv6SENDNbrSecLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Fsipv6SENDNbrSecLevel_Type.__name__=_D
_Fsipv6SENDNbrSecLevel_Object=MibScalar
fsipv6SENDNbrSecLevel=_Fsipv6SENDNbrSecLevel_Object((1,3,6,1,4,1,2076,28,1,1,19),_Fsipv6SENDNbrSecLevel_Type())
fsipv6SENDNbrSecLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6SENDNbrSecLevel.setStatus(_A)
class _Fsipv6SENDAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('cga',0),('ta',1),('cgaandta',2),('cgaorta',3)))
_Fsipv6SENDAuthType_Type.__name__=_D
_Fsipv6SENDAuthType_Object=MibScalar
fsipv6SENDAuthType=_Fsipv6SENDAuthType_Object((1,3,6,1,4,1,2076,28,1,1,20),_Fsipv6SENDAuthType_Type())
fsipv6SENDAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6SENDAuthType.setStatus(_A)
class _Fsipv6SENDMinBits_Type(Integer32):defaultValue=1024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(512,1024)));namedValues=NamedValues(*(('key512',512),('key1024',1024)))
_Fsipv6SENDMinBits_Type.__name__=_D
_Fsipv6SENDMinBits_Object=MibScalar
fsipv6SENDMinBits=_Fsipv6SENDMinBits_Object((1,3,6,1,4,1,2076,28,1,1,21),_Fsipv6SENDMinBits_Type())
fsipv6SENDMinBits.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6SENDMinBits.setStatus(_A)
class _Fsipv6SENDSecDAD_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Fsipv6SENDSecDAD_Type.__name__=_D
_Fsipv6SENDSecDAD_Object=MibScalar
fsipv6SENDSecDAD=_Fsipv6SENDSecDAD_Object((1,3,6,1,4,1,2076,28,1,1,22),_Fsipv6SENDSecDAD_Type())
fsipv6SENDSecDAD.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6SENDSecDAD.setStatus(_A)
class _Fsipv6SENDPrefixChk_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Fsipv6SENDPrefixChk_Type.__name__=_D
_Fsipv6SENDPrefixChk_Object=MibScalar
fsipv6SENDPrefixChk=_Fsipv6SENDPrefixChk_Object((1,3,6,1,4,1,2076,28,1,1,23),_Fsipv6SENDPrefixChk_Type())
fsipv6SENDPrefixChk.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6SENDPrefixChk.setStatus(_A)
class _Fsipv6ECMPPRTTimer_Type(Integer32):defaultValue=60
_Fsipv6ECMPPRTTimer_Type.__name__=_D
_Fsipv6ECMPPRTTimer_Object=MibScalar
fsipv6ECMPPRTTimer=_Fsipv6ECMPPRTTimer_Object((1,3,6,1,4,1,2076,28,1,1,24),_Fsipv6ECMPPRTTimer_Type())
fsipv6ECMPPRTTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6ECMPPRTTimer.setStatus(_A)
class _Fsipv6NdCacheTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,86400))
_Fsipv6NdCacheTimeout_Type.__name__=_D
_Fsipv6NdCacheTimeout_Object=MibScalar
fsipv6NdCacheTimeout=_Fsipv6NdCacheTimeout_Object((1,3,6,1,4,1,2076,28,1,1,25),_Fsipv6NdCacheTimeout_Type())
fsipv6NdCacheTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6NdCacheTimeout.setStatus(_A)
_Fsipv6Tables_ObjectIdentity=ObjectIdentity
fsipv6Tables=_Fsipv6Tables_ObjectIdentity((1,3,6,1,4,1,2076,28,1,2))
_Fsipv6IfTable_Object=MibTable
fsipv6IfTable=_Fsipv6IfTable_Object((1,3,6,1,4,1,2076,28,1,2,1))
if mibBuilder.loadTexts:fsipv6IfTable.setStatus(_A)
_Fsipv6IfEntry_Object=MibTableRow
fsipv6IfEntry=_Fsipv6IfEntry_Object((1,3,6,1,4,1,2076,28,1,2,1,1))
fsipv6IfEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:fsipv6IfEntry.setStatus(_A)
_Fsipv6IfIndex_Type=InterfaceIndex
_Fsipv6IfIndex_Object=MibTableColumn
fsipv6IfIndex=_Fsipv6IfIndex_Object((1,3,6,1,4,1,2076,28,1,2,1,1,1),_Fsipv6IfIndex_Type())
fsipv6IfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6IfIndex.setStatus(_A)
class _Fsipv6IfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,23,24,32,131,136)));namedValues=NamedValues(*(('ethernetcsmacd',6),('ppp',23),('softwareLoopback',24),('framerelay',32),('tunnel',131),('l3ipvlan',136)))
_Fsipv6IfType_Type.__name__=_D
_Fsipv6IfType_Object=MibTableColumn
fsipv6IfType=_Fsipv6IfType_Object((1,3,6,1,4,1,2076,28,1,2,1,1,2),_Fsipv6IfType_Type())
fsipv6IfType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfType.setStatus(_A)
class _Fsipv6IfPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Fsipv6IfPortNum_Type.__name__=_D
_Fsipv6IfPortNum_Object=MibTableColumn
fsipv6IfPortNum=_Fsipv6IfPortNum_Object((1,3,6,1,4,1,2076,28,1,2,1,1,3),_Fsipv6IfPortNum_Type())
fsipv6IfPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfPortNum.setStatus(_A)
_Fsipv6IfCircuitNum_Type=Integer32
_Fsipv6IfCircuitNum_Object=MibTableColumn
fsipv6IfCircuitNum=_Fsipv6IfCircuitNum_Object((1,3,6,1,4,1,2076,28,1,2,1,1,4),_Fsipv6IfCircuitNum_Type())
fsipv6IfCircuitNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfCircuitNum.setStatus(_A)
class _Fsipv6IfToken_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_Fsipv6IfToken_Type.__name__=_G
_Fsipv6IfToken_Object=MibTableColumn
fsipv6IfToken=_Fsipv6IfToken_Object((1,3,6,1,4,1,2076,28,1,2,1,1,5),_Fsipv6IfToken_Type())
fsipv6IfToken.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfToken.setStatus(_A)
class _Fsipv6IfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_Q,2)))
_Fsipv6IfAdminStatus_Type.__name__=_D
_Fsipv6IfAdminStatus_Object=MibTableColumn
fsipv6IfAdminStatus=_Fsipv6IfAdminStatus_Object((1,3,6,1,4,1,2076,28,1,2,1,1,6),_Fsipv6IfAdminStatus_Type())
fsipv6IfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfAdminStatus.setStatus(_A)
class _Fsipv6IfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_Q,2),('stale',3)))
_Fsipv6IfOperStatus_Type.__name__=_D
_Fsipv6IfOperStatus_Object=MibTableColumn
fsipv6IfOperStatus=_Fsipv6IfOperStatus_Object((1,3,6,1,4,1,2076,28,1,2,1,1,7),_Fsipv6IfOperStatus_Type())
fsipv6IfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfOperStatus.setStatus(_A)
class _Fsipv6IfRouterAdvStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Fsipv6IfRouterAdvStatus_Type.__name__=_D
_Fsipv6IfRouterAdvStatus_Object=MibTableColumn
fsipv6IfRouterAdvStatus=_Fsipv6IfRouterAdvStatus_Object((1,3,6,1,4,1,2076,28,1,2,1,1,8),_Fsipv6IfRouterAdvStatus_Type())
fsipv6IfRouterAdvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfRouterAdvStatus.setStatus(_A)
class _Fsipv6IfRouterAdvFlags_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('mbit',1),('obit',2),('nombit',3),('noobit',4),('mobits',5),('none',6)))
_Fsipv6IfRouterAdvFlags_Type.__name__=_D
_Fsipv6IfRouterAdvFlags_Object=MibTableColumn
fsipv6IfRouterAdvFlags=_Fsipv6IfRouterAdvFlags_Object((1,3,6,1,4,1,2076,28,1,2,1,1,9),_Fsipv6IfRouterAdvFlags_Type())
fsipv6IfRouterAdvFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfRouterAdvFlags.setStatus(_A)
class _Fsipv6IfHopLimit_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Fsipv6IfHopLimit_Type.__name__=_D
_Fsipv6IfHopLimit_Object=MibTableColumn
fsipv6IfHopLimit=_Fsipv6IfHopLimit_Object((1,3,6,1,4,1,2076,28,1,2,1,1,10),_Fsipv6IfHopLimit_Type())
fsipv6IfHopLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfHopLimit.setStatus(_A)
class _Fsipv6IfDefRouterTime_Type(Integer32):defaultValue=0
_Fsipv6IfDefRouterTime_Type.__name__=_D
_Fsipv6IfDefRouterTime_Object=MibTableColumn
fsipv6IfDefRouterTime=_Fsipv6IfDefRouterTime_Object((1,3,6,1,4,1,2076,28,1,2,1,1,11),_Fsipv6IfDefRouterTime_Type())
fsipv6IfDefRouterTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfDefRouterTime.setStatus(_A)
class _Fsipv6IfReachableTime_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_Fsipv6IfReachableTime_Type.__name__=_D
_Fsipv6IfReachableTime_Object=MibTableColumn
fsipv6IfReachableTime=_Fsipv6IfReachableTime_Object((1,3,6,1,4,1,2076,28,1,2,1,1,12),_Fsipv6IfReachableTime_Type())
fsipv6IfReachableTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfReachableTime.setStatus(_A)
class _Fsipv6IfRetransmitTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_Fsipv6IfRetransmitTime_Type.__name__=_D
_Fsipv6IfRetransmitTime_Object=MibTableColumn
fsipv6IfRetransmitTime=_Fsipv6IfRetransmitTime_Object((1,3,6,1,4,1,2076,28,1,2,1,1,13),_Fsipv6IfRetransmitTime_Type())
fsipv6IfRetransmitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfRetransmitTime.setStatus(_A)
class _Fsipv6IfDelayProbeTime_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Fsipv6IfDelayProbeTime_Type.__name__=_D
_Fsipv6IfDelayProbeTime_Object=MibTableColumn
fsipv6IfDelayProbeTime=_Fsipv6IfDelayProbeTime_Object((1,3,6,1,4,1,2076,28,1,2,1,1,14),_Fsipv6IfDelayProbeTime_Type())
fsipv6IfDelayProbeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfDelayProbeTime.setStatus(_A)
class _Fsipv6IfPrefixAdvStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Fsipv6IfPrefixAdvStatus_Type.__name__=_D
_Fsipv6IfPrefixAdvStatus_Object=MibTableColumn
fsipv6IfPrefixAdvStatus=_Fsipv6IfPrefixAdvStatus_Object((1,3,6,1,4,1,2076,28,1,2,1,1,15),_Fsipv6IfPrefixAdvStatus_Type())
fsipv6IfPrefixAdvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfPrefixAdvStatus.setStatus(_A)
class _Fsipv6IfMinRouterAdvTime_Type(Integer32):defaultValue=198
_Fsipv6IfMinRouterAdvTime_Type.__name__=_D
_Fsipv6IfMinRouterAdvTime_Object=MibTableColumn
fsipv6IfMinRouterAdvTime=_Fsipv6IfMinRouterAdvTime_Object((1,3,6,1,4,1,2076,28,1,2,1,1,16),_Fsipv6IfMinRouterAdvTime_Type())
fsipv6IfMinRouterAdvTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfMinRouterAdvTime.setStatus(_A)
class _Fsipv6IfMaxRouterAdvTime_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_Fsipv6IfMaxRouterAdvTime_Type.__name__=_D
_Fsipv6IfMaxRouterAdvTime_Object=MibTableColumn
fsipv6IfMaxRouterAdvTime=_Fsipv6IfMaxRouterAdvTime_Object((1,3,6,1,4,1,2076,28,1,2,1,1,17),_Fsipv6IfMaxRouterAdvTime_Type())
fsipv6IfMaxRouterAdvTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfMaxRouterAdvTime.setStatus(_A)
class _Fsipv6IfDADRetries_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Fsipv6IfDADRetries_Type.__name__=_D
_Fsipv6IfDADRetries_Object=MibTableColumn
fsipv6IfDADRetries=_Fsipv6IfDADRetries_Object((1,3,6,1,4,1,2076,28,1,2,1,1,18),_Fsipv6IfDADRetries_Type())
fsipv6IfDADRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfDADRetries.setStatus(_A)
class _Fsipv6IfForwarding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Fsipv6IfForwarding_Type.__name__=_D
_Fsipv6IfForwarding_Object=MibTableColumn
fsipv6IfForwarding=_Fsipv6IfForwarding_Object((1,3,6,1,4,1,2076,28,1,2,1,1,19),_Fsipv6IfForwarding_Type())
fsipv6IfForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfForwarding.setStatus(_A)
class _Fsipv6IfRoutingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Fsipv6IfRoutingStatus_Type.__name__=_D
_Fsipv6IfRoutingStatus_Object=MibTableColumn
fsipv6IfRoutingStatus=_Fsipv6IfRoutingStatus_Object((1,3,6,1,4,1,2076,28,1,2,1,1,20),_Fsipv6IfRoutingStatus_Type())
fsipv6IfRoutingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfRoutingStatus.setStatus(_A)
class _Fsipv6IfIcmpErrInterval_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Fsipv6IfIcmpErrInterval_Type.__name__=_D
_Fsipv6IfIcmpErrInterval_Object=MibTableColumn
fsipv6IfIcmpErrInterval=_Fsipv6IfIcmpErrInterval_Object((1,3,6,1,4,1,2076,28,1,2,1,1,21),_Fsipv6IfIcmpErrInterval_Type())
fsipv6IfIcmpErrInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfIcmpErrInterval.setStatus(_A)
if mibBuilder.loadTexts:fsipv6IfIcmpErrInterval.setUnits('milliseconds')
class _Fsipv6IfIcmpTokenBucketSize_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Fsipv6IfIcmpTokenBucketSize_Type.__name__=_D
_Fsipv6IfIcmpTokenBucketSize_Object=MibTableColumn
fsipv6IfIcmpTokenBucketSize=_Fsipv6IfIcmpTokenBucketSize_Object((1,3,6,1,4,1,2076,28,1,2,1,1,22),_Fsipv6IfIcmpTokenBucketSize_Type())
fsipv6IfIcmpTokenBucketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfIcmpTokenBucketSize.setStatus(_A)
class _Fsipv6IfDestUnreachableMsg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Fsipv6IfDestUnreachableMsg_Type.__name__=_D
_Fsipv6IfDestUnreachableMsg_Object=MibTableColumn
fsipv6IfDestUnreachableMsg=_Fsipv6IfDestUnreachableMsg_Object((1,3,6,1,4,1,2076,28,1,2,1,1,23),_Fsipv6IfDestUnreachableMsg_Type())
fsipv6IfDestUnreachableMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfDestUnreachableMsg.setStatus(_A)
_Fsipv6IfUnnumAssocIPIf_Type=InterfaceIndex
_Fsipv6IfUnnumAssocIPIf_Object=MibTableColumn
fsipv6IfUnnumAssocIPIf=_Fsipv6IfUnnumAssocIPIf_Object((1,3,6,1,4,1,2076,28,1,2,1,1,24),_Fsipv6IfUnnumAssocIPIf_Type())
fsipv6IfUnnumAssocIPIf.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfUnnumAssocIPIf.setStatus(_A)
class _Fsipv6IfRedirectMsg_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Fsipv6IfRedirectMsg_Type.__name__=_D
_Fsipv6IfRedirectMsg_Object=MibTableColumn
fsipv6IfRedirectMsg=_Fsipv6IfRedirectMsg_Object((1,3,6,1,4,1,2076,28,1,2,1,1,25),_Fsipv6IfRedirectMsg_Type())
fsipv6IfRedirectMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfRedirectMsg.setStatus(_A)
class _Fsipv6IfAdvSrcLLAdr_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Fsipv6IfAdvSrcLLAdr_Type.__name__=_D
_Fsipv6IfAdvSrcLLAdr_Object=MibTableColumn
fsipv6IfAdvSrcLLAdr=_Fsipv6IfAdvSrcLLAdr_Object((1,3,6,1,4,1,2076,28,1,2,1,1,26),_Fsipv6IfAdvSrcLLAdr_Type())
fsipv6IfAdvSrcLLAdr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfAdvSrcLLAdr.setStatus(_A)
class _Fsipv6IfAdvIntOpt_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Fsipv6IfAdvIntOpt_Type.__name__=_D
_Fsipv6IfAdvIntOpt_Object=MibTableColumn
fsipv6IfAdvIntOpt=_Fsipv6IfAdvIntOpt_Object((1,3,6,1,4,1,2076,28,1,2,1,1,27),_Fsipv6IfAdvIntOpt_Type())
fsipv6IfAdvIntOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfAdvIntOpt.setStatus(_A)
class _Fsipv6IfNDProxyAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Fsipv6IfNDProxyAdminStatus_Type.__name__=_D
_Fsipv6IfNDProxyAdminStatus_Object=MibTableColumn
fsipv6IfNDProxyAdminStatus=_Fsipv6IfNDProxyAdminStatus_Object((1,3,6,1,4,1,2076,28,1,2,1,1,28),_Fsipv6IfNDProxyAdminStatus_Type())
fsipv6IfNDProxyAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfNDProxyAdminStatus.setStatus(_A)
class _Fsipv6IfNDProxyMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('global',1),(_R,2)))
_Fsipv6IfNDProxyMode_Type.__name__=_D
_Fsipv6IfNDProxyMode_Object=MibTableColumn
fsipv6IfNDProxyMode=_Fsipv6IfNDProxyMode_Object((1,3,6,1,4,1,2076,28,1,2,1,1,29),_Fsipv6IfNDProxyMode_Type())
fsipv6IfNDProxyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfNDProxyMode.setStatus(_A)
class _Fsipv6IfNDProxyOperStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_e,2),(_K,3)))
_Fsipv6IfNDProxyOperStatus_Type.__name__=_D
_Fsipv6IfNDProxyOperStatus_Object=MibTableColumn
fsipv6IfNDProxyOperStatus=_Fsipv6IfNDProxyOperStatus_Object((1,3,6,1,4,1,2076,28,1,2,1,1,30),_Fsipv6IfNDProxyOperStatus_Type())
fsipv6IfNDProxyOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfNDProxyOperStatus.setStatus(_A)
class _Fsipv6IfNDProxyUpStream_Type(TruthValue):defaultValue=2
_Fsipv6IfNDProxyUpStream_Type.__name__=_P
_Fsipv6IfNDProxyUpStream_Object=MibTableColumn
fsipv6IfNDProxyUpStream=_Fsipv6IfNDProxyUpStream_Object((1,3,6,1,4,1,2076,28,1,2,1,1,31),_Fsipv6IfNDProxyUpStream_Type())
fsipv6IfNDProxyUpStream.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfNDProxyUpStream.setStatus(_A)
class _Fsipv6IfSENDSecStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('secured',1),('unsecured',2),('mixed',3)))
_Fsipv6IfSENDSecStatus_Type.__name__=_D
_Fsipv6IfSENDSecStatus_Object=MibTableColumn
fsipv6IfSENDSecStatus=_Fsipv6IfSENDSecStatus_Object((1,3,6,1,4,1,2076,28,1,2,1,1,32),_Fsipv6IfSENDSecStatus_Type())
fsipv6IfSENDSecStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfSENDSecStatus.setStatus(_A)
class _Fsipv6IfSENDDeltaTimestamp_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Fsipv6IfSENDDeltaTimestamp_Type.__name__=_H
_Fsipv6IfSENDDeltaTimestamp_Object=MibTableColumn
fsipv6IfSENDDeltaTimestamp=_Fsipv6IfSENDDeltaTimestamp_Object((1,3,6,1,4,1,2076,28,1,2,1,1,33),_Fsipv6IfSENDDeltaTimestamp_Type())
fsipv6IfSENDDeltaTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfSENDDeltaTimestamp.setStatus(_A)
class _Fsipv6IfSENDFuzzTimestamp_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Fsipv6IfSENDFuzzTimestamp_Type.__name__=_H
_Fsipv6IfSENDFuzzTimestamp_Object=MibTableColumn
fsipv6IfSENDFuzzTimestamp=_Fsipv6IfSENDFuzzTimestamp_Object((1,3,6,1,4,1,2076,28,1,2,1,1,34),_Fsipv6IfSENDFuzzTimestamp_Type())
fsipv6IfSENDFuzzTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfSENDFuzzTimestamp.setStatus(_A)
class _Fsipv6IfSENDDriftTimestamp_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_Fsipv6IfSENDDriftTimestamp_Type.__name__=_H
_Fsipv6IfSENDDriftTimestamp_Object=MibTableColumn
fsipv6IfSENDDriftTimestamp=_Fsipv6IfSENDDriftTimestamp_Object((1,3,6,1,4,1,2076,28,1,2,1,1,35),_Fsipv6IfSENDDriftTimestamp_Type())
fsipv6IfSENDDriftTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfSENDDriftTimestamp.setStatus(_A)
class _Fsipv6IfDefRoutePreference_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('low',0),(_f,1),('high',2)))
_Fsipv6IfDefRoutePreference_Type.__name__=_D
_Fsipv6IfDefRoutePreference_Object=MibTableColumn
fsipv6IfDefRoutePreference=_Fsipv6IfDefRoutePreference_Object((1,3,6,1,4,1,2076,28,1,2,1,1,36),_Fsipv6IfDefRoutePreference_Type())
fsipv6IfDefRoutePreference.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfDefRoutePreference.setStatus(_A)
_Fsipv6IfStatsTable_Object=MibTable
fsipv6IfStatsTable=_Fsipv6IfStatsTable_Object((1,3,6,1,4,1,2076,28,1,2,2))
if mibBuilder.loadTexts:fsipv6IfStatsTable.setStatus(_A)
_Fsipv6IfStatsEntry_Object=MibTableRow
fsipv6IfStatsEntry=_Fsipv6IfStatsEntry_Object((1,3,6,1,4,1,2076,28,1,2,2,1))
fsipv6IfStatsEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:fsipv6IfStatsEntry.setStatus(_A)
_Fsipv6IfStatsIndex_Type=InterfaceIndex
_Fsipv6IfStatsIndex_Object=MibTableColumn
fsipv6IfStatsIndex=_Fsipv6IfStatsIndex_Object((1,3,6,1,4,1,2076,28,1,2,2,1,1),_Fsipv6IfStatsIndex_Type())
fsipv6IfStatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6IfStatsIndex.setStatus(_A)
_Fsipv6IfStatsInReceives_Type=Counter32
_Fsipv6IfStatsInReceives_Object=MibTableColumn
fsipv6IfStatsInReceives=_Fsipv6IfStatsInReceives_Object((1,3,6,1,4,1,2076,28,1,2,2,1,2),_Fsipv6IfStatsInReceives_Type())
fsipv6IfStatsInReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsInReceives.setStatus(_A)
_Fsipv6IfStatsInHdrErrors_Type=Counter32
_Fsipv6IfStatsInHdrErrors_Object=MibTableColumn
fsipv6IfStatsInHdrErrors=_Fsipv6IfStatsInHdrErrors_Object((1,3,6,1,4,1,2076,28,1,2,2,1,3),_Fsipv6IfStatsInHdrErrors_Type())
fsipv6IfStatsInHdrErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsInHdrErrors.setStatus(_A)
_Fsipv6IfStatsTooBigErrors_Type=Counter32
_Fsipv6IfStatsTooBigErrors_Object=MibTableColumn
fsipv6IfStatsTooBigErrors=_Fsipv6IfStatsTooBigErrors_Object((1,3,6,1,4,1,2076,28,1,2,2,1,4),_Fsipv6IfStatsTooBigErrors_Type())
fsipv6IfStatsTooBigErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsTooBigErrors.setStatus(_A)
_Fsipv6IfStatsInAddrErrors_Type=Counter32
_Fsipv6IfStatsInAddrErrors_Object=MibTableColumn
fsipv6IfStatsInAddrErrors=_Fsipv6IfStatsInAddrErrors_Object((1,3,6,1,4,1,2076,28,1,2,2,1,5),_Fsipv6IfStatsInAddrErrors_Type())
fsipv6IfStatsInAddrErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsInAddrErrors.setStatus(_A)
_Fsipv6IfStatsForwDatagrams_Type=Counter32
_Fsipv6IfStatsForwDatagrams_Object=MibTableColumn
fsipv6IfStatsForwDatagrams=_Fsipv6IfStatsForwDatagrams_Object((1,3,6,1,4,1,2076,28,1,2,2,1,6),_Fsipv6IfStatsForwDatagrams_Type())
fsipv6IfStatsForwDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsForwDatagrams.setStatus(_A)
_Fsipv6IfStatsInUnknownProtos_Type=Counter32
_Fsipv6IfStatsInUnknownProtos_Object=MibTableColumn
fsipv6IfStatsInUnknownProtos=_Fsipv6IfStatsInUnknownProtos_Object((1,3,6,1,4,1,2076,28,1,2,2,1,7),_Fsipv6IfStatsInUnknownProtos_Type())
fsipv6IfStatsInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsInUnknownProtos.setStatus(_A)
_Fsipv6IfStatsInDiscards_Type=Counter32
_Fsipv6IfStatsInDiscards_Object=MibTableColumn
fsipv6IfStatsInDiscards=_Fsipv6IfStatsInDiscards_Object((1,3,6,1,4,1,2076,28,1,2,2,1,8),_Fsipv6IfStatsInDiscards_Type())
fsipv6IfStatsInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsInDiscards.setStatus(_A)
_Fsipv6IfStatsInDelivers_Type=Counter32
_Fsipv6IfStatsInDelivers_Object=MibTableColumn
fsipv6IfStatsInDelivers=_Fsipv6IfStatsInDelivers_Object((1,3,6,1,4,1,2076,28,1,2,2,1,9),_Fsipv6IfStatsInDelivers_Type())
fsipv6IfStatsInDelivers.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsInDelivers.setStatus(_A)
_Fsipv6IfStatsOutRequests_Type=Counter32
_Fsipv6IfStatsOutRequests_Object=MibTableColumn
fsipv6IfStatsOutRequests=_Fsipv6IfStatsOutRequests_Object((1,3,6,1,4,1,2076,28,1,2,2,1,10),_Fsipv6IfStatsOutRequests_Type())
fsipv6IfStatsOutRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsOutRequests.setStatus(_A)
_Fsipv6IfStatsOutDiscards_Type=Counter32
_Fsipv6IfStatsOutDiscards_Object=MibTableColumn
fsipv6IfStatsOutDiscards=_Fsipv6IfStatsOutDiscards_Object((1,3,6,1,4,1,2076,28,1,2,2,1,11),_Fsipv6IfStatsOutDiscards_Type())
fsipv6IfStatsOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsOutDiscards.setStatus(_A)
_Fsipv6IfStatsOutNoRoutes_Type=Counter32
_Fsipv6IfStatsOutNoRoutes_Object=MibTableColumn
fsipv6IfStatsOutNoRoutes=_Fsipv6IfStatsOutNoRoutes_Object((1,3,6,1,4,1,2076,28,1,2,2,1,12),_Fsipv6IfStatsOutNoRoutes_Type())
fsipv6IfStatsOutNoRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsOutNoRoutes.setStatus(_A)
_Fsipv6IfStatsReasmReqds_Type=Counter32
_Fsipv6IfStatsReasmReqds_Object=MibTableColumn
fsipv6IfStatsReasmReqds=_Fsipv6IfStatsReasmReqds_Object((1,3,6,1,4,1,2076,28,1,2,2,1,13),_Fsipv6IfStatsReasmReqds_Type())
fsipv6IfStatsReasmReqds.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsReasmReqds.setStatus(_A)
_Fsipv6IfStatsReasmOKs_Type=Counter32
_Fsipv6IfStatsReasmOKs_Object=MibTableColumn
fsipv6IfStatsReasmOKs=_Fsipv6IfStatsReasmOKs_Object((1,3,6,1,4,1,2076,28,1,2,2,1,14),_Fsipv6IfStatsReasmOKs_Type())
fsipv6IfStatsReasmOKs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsReasmOKs.setStatus(_A)
_Fsipv6IfStatsReasmFails_Type=Counter32
_Fsipv6IfStatsReasmFails_Object=MibTableColumn
fsipv6IfStatsReasmFails=_Fsipv6IfStatsReasmFails_Object((1,3,6,1,4,1,2076,28,1,2,2,1,15),_Fsipv6IfStatsReasmFails_Type())
fsipv6IfStatsReasmFails.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsReasmFails.setStatus(_A)
_Fsipv6IfStatsFragOKs_Type=Counter32
_Fsipv6IfStatsFragOKs_Object=MibTableColumn
fsipv6IfStatsFragOKs=_Fsipv6IfStatsFragOKs_Object((1,3,6,1,4,1,2076,28,1,2,2,1,16),_Fsipv6IfStatsFragOKs_Type())
fsipv6IfStatsFragOKs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsFragOKs.setStatus(_A)
_Fsipv6IfStatsFragFails_Type=Counter32
_Fsipv6IfStatsFragFails_Object=MibTableColumn
fsipv6IfStatsFragFails=_Fsipv6IfStatsFragFails_Object((1,3,6,1,4,1,2076,28,1,2,2,1,17),_Fsipv6IfStatsFragFails_Type())
fsipv6IfStatsFragFails.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsFragFails.setStatus(_A)
_Fsipv6IfStatsFragCreates_Type=Counter32
_Fsipv6IfStatsFragCreates_Object=MibTableColumn
fsipv6IfStatsFragCreates=_Fsipv6IfStatsFragCreates_Object((1,3,6,1,4,1,2076,28,1,2,2,1,18),_Fsipv6IfStatsFragCreates_Type())
fsipv6IfStatsFragCreates.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsFragCreates.setStatus(_A)
_Fsipv6IfStatsInMcastPkts_Type=Counter32
_Fsipv6IfStatsInMcastPkts_Object=MibTableColumn
fsipv6IfStatsInMcastPkts=_Fsipv6IfStatsInMcastPkts_Object((1,3,6,1,4,1,2076,28,1,2,2,1,19),_Fsipv6IfStatsInMcastPkts_Type())
fsipv6IfStatsInMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsInMcastPkts.setStatus(_A)
_Fsipv6IfStatsOutMcastPkts_Type=Counter32
_Fsipv6IfStatsOutMcastPkts_Object=MibTableColumn
fsipv6IfStatsOutMcastPkts=_Fsipv6IfStatsOutMcastPkts_Object((1,3,6,1,4,1,2076,28,1,2,2,1,20),_Fsipv6IfStatsOutMcastPkts_Type())
fsipv6IfStatsOutMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsOutMcastPkts.setStatus(_A)
_Fsipv6IfStatsInTruncatedPkts_Type=Counter32
_Fsipv6IfStatsInTruncatedPkts_Object=MibTableColumn
fsipv6IfStatsInTruncatedPkts=_Fsipv6IfStatsInTruncatedPkts_Object((1,3,6,1,4,1,2076,28,1,2,2,1,21),_Fsipv6IfStatsInTruncatedPkts_Type())
fsipv6IfStatsInTruncatedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsInTruncatedPkts.setStatus(_A)
_Fsipv6IfStatsInRouterSols_Type=Counter32
_Fsipv6IfStatsInRouterSols_Object=MibTableColumn
fsipv6IfStatsInRouterSols=_Fsipv6IfStatsInRouterSols_Object((1,3,6,1,4,1,2076,28,1,2,2,1,22),_Fsipv6IfStatsInRouterSols_Type())
fsipv6IfStatsInRouterSols.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsInRouterSols.setStatus(_A)
_Fsipv6IfStatsInRouterAdvs_Type=Counter32
_Fsipv6IfStatsInRouterAdvs_Object=MibTableColumn
fsipv6IfStatsInRouterAdvs=_Fsipv6IfStatsInRouterAdvs_Object((1,3,6,1,4,1,2076,28,1,2,2,1,23),_Fsipv6IfStatsInRouterAdvs_Type())
fsipv6IfStatsInRouterAdvs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsInRouterAdvs.setStatus(_A)
_Fsipv6IfStatsInNeighSols_Type=Counter32
_Fsipv6IfStatsInNeighSols_Object=MibTableColumn
fsipv6IfStatsInNeighSols=_Fsipv6IfStatsInNeighSols_Object((1,3,6,1,4,1,2076,28,1,2,2,1,24),_Fsipv6IfStatsInNeighSols_Type())
fsipv6IfStatsInNeighSols.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsInNeighSols.setStatus(_A)
_Fsipv6IfStatsInNeighAdvs_Type=Counter32
_Fsipv6IfStatsInNeighAdvs_Object=MibTableColumn
fsipv6IfStatsInNeighAdvs=_Fsipv6IfStatsInNeighAdvs_Object((1,3,6,1,4,1,2076,28,1,2,2,1,25),_Fsipv6IfStatsInNeighAdvs_Type())
fsipv6IfStatsInNeighAdvs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsInNeighAdvs.setStatus(_A)
_Fsipv6IfStatsInRedirects_Type=Counter32
_Fsipv6IfStatsInRedirects_Object=MibTableColumn
fsipv6IfStatsInRedirects=_Fsipv6IfStatsInRedirects_Object((1,3,6,1,4,1,2076,28,1,2,2,1,26),_Fsipv6IfStatsInRedirects_Type())
fsipv6IfStatsInRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsInRedirects.setStatus(_A)
_Fsipv6IfStatsOutRouterSols_Type=Counter32
_Fsipv6IfStatsOutRouterSols_Object=MibTableColumn
fsipv6IfStatsOutRouterSols=_Fsipv6IfStatsOutRouterSols_Object((1,3,6,1,4,1,2076,28,1,2,2,1,27),_Fsipv6IfStatsOutRouterSols_Type())
fsipv6IfStatsOutRouterSols.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsOutRouterSols.setStatus(_A)
_Fsipv6IfStatsOutRouterAdvs_Type=Counter32
_Fsipv6IfStatsOutRouterAdvs_Object=MibTableColumn
fsipv6IfStatsOutRouterAdvs=_Fsipv6IfStatsOutRouterAdvs_Object((1,3,6,1,4,1,2076,28,1,2,2,1,28),_Fsipv6IfStatsOutRouterAdvs_Type())
fsipv6IfStatsOutRouterAdvs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsOutRouterAdvs.setStatus(_A)
_Fsipv6IfStatsOutNeighSols_Type=Counter32
_Fsipv6IfStatsOutNeighSols_Object=MibTableColumn
fsipv6IfStatsOutNeighSols=_Fsipv6IfStatsOutNeighSols_Object((1,3,6,1,4,1,2076,28,1,2,2,1,29),_Fsipv6IfStatsOutNeighSols_Type())
fsipv6IfStatsOutNeighSols.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsOutNeighSols.setStatus(_A)
_Fsipv6IfStatsOutNeighAdvs_Type=Counter32
_Fsipv6IfStatsOutNeighAdvs_Object=MibTableColumn
fsipv6IfStatsOutNeighAdvs=_Fsipv6IfStatsOutNeighAdvs_Object((1,3,6,1,4,1,2076,28,1,2,2,1,30),_Fsipv6IfStatsOutNeighAdvs_Type())
fsipv6IfStatsOutNeighAdvs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsOutNeighAdvs.setStatus(_A)
_Fsipv6IfStatsOutRedirects_Type=Counter32
_Fsipv6IfStatsOutRedirects_Object=MibTableColumn
fsipv6IfStatsOutRedirects=_Fsipv6IfStatsOutRedirects_Object((1,3,6,1,4,1,2076,28,1,2,2,1,31),_Fsipv6IfStatsOutRedirects_Type())
fsipv6IfStatsOutRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsOutRedirects.setStatus(_A)
_Fsipv6IfStatsLastRouterAdvTime_Type=TimeTicks
_Fsipv6IfStatsLastRouterAdvTime_Object=MibTableColumn
fsipv6IfStatsLastRouterAdvTime=_Fsipv6IfStatsLastRouterAdvTime_Object((1,3,6,1,4,1,2076,28,1,2,2,1,32),_Fsipv6IfStatsLastRouterAdvTime_Type())
fsipv6IfStatsLastRouterAdvTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsLastRouterAdvTime.setStatus(_A)
_Fsipv6IfStatsNextRouterAdvTime_Type=TimeTicks
_Fsipv6IfStatsNextRouterAdvTime_Object=MibTableColumn
fsipv6IfStatsNextRouterAdvTime=_Fsipv6IfStatsNextRouterAdvTime_Object((1,3,6,1,4,1,2076,28,1,2,2,1,33),_Fsipv6IfStatsNextRouterAdvTime_Type())
fsipv6IfStatsNextRouterAdvTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsNextRouterAdvTime.setStatus(_A)
_Fsipv6IfStatsIcmp6ErrRateLmtd_Type=Counter32
_Fsipv6IfStatsIcmp6ErrRateLmtd_Object=MibTableColumn
fsipv6IfStatsIcmp6ErrRateLmtd=_Fsipv6IfStatsIcmp6ErrRateLmtd_Object((1,3,6,1,4,1,2076,28,1,2,2,1,34),_Fsipv6IfStatsIcmp6ErrRateLmtd_Type())
fsipv6IfStatsIcmp6ErrRateLmtd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsIcmp6ErrRateLmtd.setStatus(_A)
_Fsipv6IfStatsSENDDroppedPkts_Type=Counter32
_Fsipv6IfStatsSENDDroppedPkts_Object=MibTableColumn
fsipv6IfStatsSENDDroppedPkts=_Fsipv6IfStatsSENDDroppedPkts_Object((1,3,6,1,4,1,2076,28,1,2,2,1,35),_Fsipv6IfStatsSENDDroppedPkts_Type())
fsipv6IfStatsSENDDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsSENDDroppedPkts.setStatus(_A)
_Fsipv6IfStatsSENDInvalidPkts_Type=Counter32
_Fsipv6IfStatsSENDInvalidPkts_Object=MibTableColumn
fsipv6IfStatsSENDInvalidPkts=_Fsipv6IfStatsSENDInvalidPkts_Object((1,3,6,1,4,1,2076,28,1,2,2,1,36),_Fsipv6IfStatsSENDInvalidPkts_Type())
fsipv6IfStatsSENDInvalidPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfStatsSENDInvalidPkts.setStatus(_A)
_Fsipv6PrefixTable_Object=MibTable
fsipv6PrefixTable=_Fsipv6PrefixTable_Object((1,3,6,1,4,1,2076,28,1,2,3))
if mibBuilder.loadTexts:fsipv6PrefixTable.setStatus(_A)
_Fsipv6PrefixEntry_Object=MibTableRow
fsipv6PrefixEntry=_Fsipv6PrefixEntry_Object((1,3,6,1,4,1,2076,28,1,2,3,1))
fsipv6PrefixEntry.setIndexNames((0,_E,_h),(0,_E,_i),(0,_E,_j))
if mibBuilder.loadTexts:fsipv6PrefixEntry.setStatus(_A)
_Fsipv6PrefixIndex_Type=InterfaceIndex
_Fsipv6PrefixIndex_Object=MibTableColumn
fsipv6PrefixIndex=_Fsipv6PrefixIndex_Object((1,3,6,1,4,1,2076,28,1,2,3,1,1),_Fsipv6PrefixIndex_Type())
fsipv6PrefixIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6PrefixIndex.setStatus(_A)
class _Fsipv6PrefixAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Fsipv6PrefixAddress_Type.__name__=_G
_Fsipv6PrefixAddress_Object=MibTableColumn
fsipv6PrefixAddress=_Fsipv6PrefixAddress_Object((1,3,6,1,4,1,2076,28,1,2,3,1,2),_Fsipv6PrefixAddress_Type())
fsipv6PrefixAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6PrefixAddress.setStatus(_A)
class _Fsipv6PrefixAddrLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Fsipv6PrefixAddrLen_Type.__name__=_D
_Fsipv6PrefixAddrLen_Object=MibTableColumn
fsipv6PrefixAddrLen=_Fsipv6PrefixAddrLen_Object((1,3,6,1,4,1,2076,28,1,2,3,1,3),_Fsipv6PrefixAddrLen_Type())
fsipv6PrefixAddrLen.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6PrefixAddrLen.setStatus(_A)
class _Fsipv6PrefixProfileIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Fsipv6PrefixProfileIndex_Type.__name__=_D
_Fsipv6PrefixProfileIndex_Object=MibTableColumn
fsipv6PrefixProfileIndex=_Fsipv6PrefixProfileIndex_Object((1,3,6,1,4,1,2076,28,1,2,3,1,4),_Fsipv6PrefixProfileIndex_Type())
fsipv6PrefixProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PrefixProfileIndex.setStatus(_A)
_Fsipv6PrefixAdminStatus_Type=RowStatus
_Fsipv6PrefixAdminStatus_Object=MibTableColumn
fsipv6PrefixAdminStatus=_Fsipv6PrefixAdminStatus_Object((1,3,6,1,4,1,2076,28,1,2,3,1,5),_Fsipv6PrefixAdminStatus_Type())
fsipv6PrefixAdminStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:fsipv6PrefixAdminStatus.setStatus(_A)
class _Fsipv6SupportEmbeddedRp_Type(TruthValue):defaultValue=2
_Fsipv6SupportEmbeddedRp_Type.__name__=_P
_Fsipv6SupportEmbeddedRp_Object=MibTableColumn
fsipv6SupportEmbeddedRp=_Fsipv6SupportEmbeddedRp_Object((1,3,6,1,4,1,2076,28,1,2,3,1,6),_Fsipv6SupportEmbeddedRp_Type())
fsipv6SupportEmbeddedRp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6SupportEmbeddedRp.setStatus(_A)
_Fsipv6AddrTable_Object=MibTable
fsipv6AddrTable=_Fsipv6AddrTable_Object((1,3,6,1,4,1,2076,28,1,2,4))
if mibBuilder.loadTexts:fsipv6AddrTable.setStatus(_A)
_Fsipv6AddrEntry_Object=MibTableRow
fsipv6AddrEntry=_Fsipv6AddrEntry_Object((1,3,6,1,4,1,2076,28,1,2,4,1))
fsipv6AddrEntry.setIndexNames((0,_E,_k),(0,_E,_l),(0,_E,_m))
if mibBuilder.loadTexts:fsipv6AddrEntry.setStatus(_A)
_Fsipv6AddrIndex_Type=InterfaceIndex
_Fsipv6AddrIndex_Object=MibTableColumn
fsipv6AddrIndex=_Fsipv6AddrIndex_Object((1,3,6,1,4,1,2076,28,1,2,4,1,1),_Fsipv6AddrIndex_Type())
fsipv6AddrIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6AddrIndex.setStatus(_A)
class _Fsipv6AddrAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Fsipv6AddrAddress_Type.__name__=_G
_Fsipv6AddrAddress_Object=MibTableColumn
fsipv6AddrAddress=_Fsipv6AddrAddress_Object((1,3,6,1,4,1,2076,28,1,2,4,1,2),_Fsipv6AddrAddress_Type())
fsipv6AddrAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6AddrAddress.setStatus(_A)
class _Fsipv6AddrPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Fsipv6AddrPrefixLen_Type.__name__=_D
_Fsipv6AddrPrefixLen_Object=MibTableColumn
fsipv6AddrPrefixLen=_Fsipv6AddrPrefixLen_Object((1,3,6,1,4,1,2076,28,1,2,4,1,3),_Fsipv6AddrPrefixLen_Type())
fsipv6AddrPrefixLen.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6AddrPrefixLen.setStatus(_A)
_Fsipv6AddrAdminStatus_Type=RowStatus
_Fsipv6AddrAdminStatus_Object=MibTableColumn
fsipv6AddrAdminStatus=_Fsipv6AddrAdminStatus_Object((1,3,6,1,4,1,2076,28,1,2,4,1,4),_Fsipv6AddrAdminStatus_Type())
fsipv6AddrAdminStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:fsipv6AddrAdminStatus.setStatus(_A)
class _Fsipv6AddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_S,2),('linklocal',3)))
_Fsipv6AddrType_Type.__name__=_D
_Fsipv6AddrType_Object=MibTableColumn
fsipv6AddrType=_Fsipv6AddrType_Object((1,3,6,1,4,1,2076,28,1,2,4,1,5),_Fsipv6AddrType_Type())
fsipv6AddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrType.setStatus(_A)
class _Fsipv6AddrProfIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Fsipv6AddrProfIndex_Type.__name__=_D
_Fsipv6AddrProfIndex_Object=MibTableColumn
fsipv6AddrProfIndex=_Fsipv6AddrProfIndex_Object((1,3,6,1,4,1,2076,28,1,2,4,1,6),_Fsipv6AddrProfIndex_Type())
fsipv6AddrProfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrProfIndex.setStatus(_A)
class _Fsipv6AddrOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tentative',1),('complete',2),(_Q,3),('failed',4)))
_Fsipv6AddrOperStatus_Type.__name__=_D
_Fsipv6AddrOperStatus_Object=MibTableColumn
fsipv6AddrOperStatus=_Fsipv6AddrOperStatus_Object((1,3,6,1,4,1,2076,28,1,2,4,1,7),_Fsipv6AddrOperStatus_Type())
fsipv6AddrOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6AddrOperStatus.setStatus(_A)
_Fsipv6AddrScope_Type=InetScopeType
_Fsipv6AddrScope_Object=MibTableColumn
fsipv6AddrScope=_Fsipv6AddrScope_Object((1,3,6,1,4,1,2076,28,1,2,4,1,8),_Fsipv6AddrScope_Type())
fsipv6AddrScope.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6AddrScope.setStatus(_A)
class _Fsipv6AddrSENDCgaStatus_Type(TruthValue):defaultValue=2
_Fsipv6AddrSENDCgaStatus_Type.__name__=_P
_Fsipv6AddrSENDCgaStatus_Object=MibTableColumn
fsipv6AddrSENDCgaStatus=_Fsipv6AddrSENDCgaStatus_Object((1,3,6,1,4,1,2076,28,1,2,4,1,9),_Fsipv6AddrSENDCgaStatus_Type())
fsipv6AddrSENDCgaStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrSENDCgaStatus.setStatus(_A)
_Fsipv6AddrSENDCgaModifier_Type=OctetString
_Fsipv6AddrSENDCgaModifier_Object=MibTableColumn
fsipv6AddrSENDCgaModifier=_Fsipv6AddrSENDCgaModifier_Object((1,3,6,1,4,1,2076,28,1,2,4,1,10),_Fsipv6AddrSENDCgaModifier_Type())
fsipv6AddrSENDCgaModifier.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrSENDCgaModifier.setStatus(_A)
_Fsipv6AddrSENDCollisionCount_Type=Integer32
_Fsipv6AddrSENDCollisionCount_Object=MibTableColumn
fsipv6AddrSENDCollisionCount=_Fsipv6AddrSENDCollisionCount_Object((1,3,6,1,4,1,2076,28,1,2,4,1,11),_Fsipv6AddrSENDCollisionCount_Type())
fsipv6AddrSENDCollisionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrSENDCollisionCount.setStatus(_A)
_Fsipv6AddrProfileTable_Object=MibTable
fsipv6AddrProfileTable=_Fsipv6AddrProfileTable_Object((1,3,6,1,4,1,2076,28,1,2,5))
if mibBuilder.loadTexts:fsipv6AddrProfileTable.setStatus(_A)
_Fsipv6AddrProfileEntry_Object=MibTableRow
fsipv6AddrProfileEntry=_Fsipv6AddrProfileEntry_Object((1,3,6,1,4,1,2076,28,1,2,5,1))
fsipv6AddrProfileEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:fsipv6AddrProfileEntry.setStatus(_A)
class _Fsipv6AddrProfileIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Fsipv6AddrProfileIndex_Type.__name__=_H
_Fsipv6AddrProfileIndex_Object=MibTableColumn
fsipv6AddrProfileIndex=_Fsipv6AddrProfileIndex_Object((1,3,6,1,4,1,2076,28,1,2,5,1,1),_Fsipv6AddrProfileIndex_Type())
fsipv6AddrProfileIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6AddrProfileIndex.setStatus(_A)
class _Fsipv6AddrProfileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_O,2)))
_Fsipv6AddrProfileStatus_Type.__name__=_D
_Fsipv6AddrProfileStatus_Object=MibTableColumn
fsipv6AddrProfileStatus=_Fsipv6AddrProfileStatus_Object((1,3,6,1,4,1,2076,28,1,2,5,1,2),_Fsipv6AddrProfileStatus_Type())
fsipv6AddrProfileStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrProfileStatus.setStatus(_A)
class _Fsipv6AddrProfilePrefixAdvStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_Fsipv6AddrProfilePrefixAdvStatus_Type.__name__=_D
_Fsipv6AddrProfilePrefixAdvStatus_Object=MibTableColumn
fsipv6AddrProfilePrefixAdvStatus=_Fsipv6AddrProfilePrefixAdvStatus_Object((1,3,6,1,4,1,2076,28,1,2,5,1,3),_Fsipv6AddrProfilePrefixAdvStatus_Type())
fsipv6AddrProfilePrefixAdvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrProfilePrefixAdvStatus.setStatus(_A)
class _Fsipv6AddrProfileOnLinkAdvStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_Fsipv6AddrProfileOnLinkAdvStatus_Type.__name__=_D
_Fsipv6AddrProfileOnLinkAdvStatus_Object=MibTableColumn
fsipv6AddrProfileOnLinkAdvStatus=_Fsipv6AddrProfileOnLinkAdvStatus_Object((1,3,6,1,4,1,2076,28,1,2,5,1,4),_Fsipv6AddrProfileOnLinkAdvStatus_Type())
fsipv6AddrProfileOnLinkAdvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrProfileOnLinkAdvStatus.setStatus(_A)
class _Fsipv6AddrProfileAutoConfAdvStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_Fsipv6AddrProfileAutoConfAdvStatus_Type.__name__=_D
_Fsipv6AddrProfileAutoConfAdvStatus_Object=MibTableColumn
fsipv6AddrProfileAutoConfAdvStatus=_Fsipv6AddrProfileAutoConfAdvStatus_Object((1,3,6,1,4,1,2076,28,1,2,5,1,5),_Fsipv6AddrProfileAutoConfAdvStatus_Type())
fsipv6AddrProfileAutoConfAdvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrProfileAutoConfAdvStatus.setStatus(_A)
class _Fsipv6AddrProfilePreferredTime_Type(Unsigned32):defaultValue=604800;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Fsipv6AddrProfilePreferredTime_Type.__name__=_H
_Fsipv6AddrProfilePreferredTime_Object=MibTableColumn
fsipv6AddrProfilePreferredTime=_Fsipv6AddrProfilePreferredTime_Object((1,3,6,1,4,1,2076,28,1,2,5,1,6),_Fsipv6AddrProfilePreferredTime_Type())
fsipv6AddrProfilePreferredTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrProfilePreferredTime.setStatus(_A)
class _Fsipv6AddrProfileValidTime_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Fsipv6AddrProfileValidTime_Type.__name__=_H
_Fsipv6AddrProfileValidTime_Object=MibTableColumn
fsipv6AddrProfileValidTime=_Fsipv6AddrProfileValidTime_Object((1,3,6,1,4,1,2076,28,1,2,5,1,7),_Fsipv6AddrProfileValidTime_Type())
fsipv6AddrProfileValidTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrProfileValidTime.setStatus(_A)
class _Fsipv6AddrProfileValidLifeTimeFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixed',1),(_o,2)))
_Fsipv6AddrProfileValidLifeTimeFlag_Type.__name__=_D
_Fsipv6AddrProfileValidLifeTimeFlag_Object=MibTableColumn
fsipv6AddrProfileValidLifeTimeFlag=_Fsipv6AddrProfileValidLifeTimeFlag_Object((1,3,6,1,4,1,2076,28,1,2,5,1,8),_Fsipv6AddrProfileValidLifeTimeFlag_Type())
fsipv6AddrProfileValidLifeTimeFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrProfileValidLifeTimeFlag.setStatus(_A)
class _Fsipv6AddrProfilePreferredLifeTimeFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixed',1),(_o,2)))
_Fsipv6AddrProfilePreferredLifeTimeFlag_Type.__name__=_D
_Fsipv6AddrProfilePreferredLifeTimeFlag_Object=MibTableColumn
fsipv6AddrProfilePreferredLifeTimeFlag=_Fsipv6AddrProfilePreferredLifeTimeFlag_Object((1,3,6,1,4,1,2076,28,1,2,5,1,9),_Fsipv6AddrProfilePreferredLifeTimeFlag_Type())
fsipv6AddrProfilePreferredLifeTimeFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrProfilePreferredLifeTimeFlag.setStatus(_A)
_Fsipv6PmtuTable_Object=MibTable
fsipv6PmtuTable=_Fsipv6PmtuTable_Object((1,3,6,1,4,1,2076,28,1,2,6))
if mibBuilder.loadTexts:fsipv6PmtuTable.setStatus(_A)
_Fsipv6PmtuEntry_Object=MibTableRow
fsipv6PmtuEntry=_Fsipv6PmtuEntry_Object((1,3,6,1,4,1,2076,28,1,2,6,1))
fsipv6PmtuEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:fsipv6PmtuEntry.setStatus(_A)
class _Fsipv6PmtuDest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Fsipv6PmtuDest_Type.__name__=_G
_Fsipv6PmtuDest_Object=MibTableColumn
fsipv6PmtuDest=_Fsipv6PmtuDest_Object((1,3,6,1,4,1,2076,28,1,2,6,1,1),_Fsipv6PmtuDest_Type())
fsipv6PmtuDest.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6PmtuDest.setStatus(_A)
class _Fsipv6Pmtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1280,65535))
_Fsipv6Pmtu_Type.__name__=_D
_Fsipv6Pmtu_Object=MibTableColumn
fsipv6Pmtu=_Fsipv6Pmtu_Object((1,3,6,1,4,1,2076,28,1,2,6,1,2),_Fsipv6Pmtu_Type())
fsipv6Pmtu.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6Pmtu.setStatus(_A)
_Fsipv6PmtuTimeStamp_Type=Integer32
_Fsipv6PmtuTimeStamp_Object=MibTableColumn
fsipv6PmtuTimeStamp=_Fsipv6PmtuTimeStamp_Object((1,3,6,1,4,1,2076,28,1,2,6,1,3),_Fsipv6PmtuTimeStamp_Type())
fsipv6PmtuTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6PmtuTimeStamp.setStatus(_A)
class _Fsipv6PmtuAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_O,2)))
_Fsipv6PmtuAdminStatus_Type.__name__=_D
_Fsipv6PmtuAdminStatus_Object=MibTableColumn
fsipv6PmtuAdminStatus=_Fsipv6PmtuAdminStatus_Object((1,3,6,1,4,1,2076,28,1,2,6,1,4),_Fsipv6PmtuAdminStatus_Type())
fsipv6PmtuAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PmtuAdminStatus.setStatus(_A)
_Fsipv6NdLanCacheTable_Object=MibTable
fsipv6NdLanCacheTable=_Fsipv6NdLanCacheTable_Object((1,3,6,1,4,1,2076,28,1,2,7))
if mibBuilder.loadTexts:fsipv6NdLanCacheTable.setStatus(_A)
_Fsipv6NdLanCacheEntry_Object=MibTableRow
fsipv6NdLanCacheEntry=_Fsipv6NdLanCacheEntry_Object((1,3,6,1,4,1,2076,28,1,2,7,1))
fsipv6NdLanCacheEntry.setIndexNames((0,_E,_q),(0,_E,_r))
if mibBuilder.loadTexts:fsipv6NdLanCacheEntry.setStatus(_A)
_Fsipv6NdLanCacheIfIndex_Type=InterfaceIndex
_Fsipv6NdLanCacheIfIndex_Object=MibTableColumn
fsipv6NdLanCacheIfIndex=_Fsipv6NdLanCacheIfIndex_Object((1,3,6,1,4,1,2076,28,1,2,7,1,1),_Fsipv6NdLanCacheIfIndex_Type())
fsipv6NdLanCacheIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6NdLanCacheIfIndex.setStatus(_A)
class _Fsipv6NdLanCacheIPv6Addr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Fsipv6NdLanCacheIPv6Addr_Type.__name__=_G
_Fsipv6NdLanCacheIPv6Addr_Object=MibTableColumn
fsipv6NdLanCacheIPv6Addr=_Fsipv6NdLanCacheIPv6Addr_Object((1,3,6,1,4,1,2076,28,1,2,7,1,2),_Fsipv6NdLanCacheIPv6Addr_Type())
fsipv6NdLanCacheIPv6Addr.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6NdLanCacheIPv6Addr.setStatus(_A)
class _Fsipv6NdLanCacheStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_O,2)))
_Fsipv6NdLanCacheStatus_Type.__name__=_D
_Fsipv6NdLanCacheStatus_Object=MibTableColumn
fsipv6NdLanCacheStatus=_Fsipv6NdLanCacheStatus_Object((1,3,6,1,4,1,2076,28,1,2,7,1,3),_Fsipv6NdLanCacheStatus_Type())
fsipv6NdLanCacheStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6NdLanCacheStatus.setStatus(_A)
class _Fsipv6NdLanCachePhysAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_Fsipv6NdLanCachePhysAddr_Type.__name__=_G
_Fsipv6NdLanCachePhysAddr_Object=MibTableColumn
fsipv6NdLanCachePhysAddr=_Fsipv6NdLanCachePhysAddr_Object((1,3,6,1,4,1,2076,28,1,2,7,1,4),_Fsipv6NdLanCachePhysAddr_Type())
fsipv6NdLanCachePhysAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6NdLanCachePhysAddr.setStatus(_A)
class _Fsipv6NdLanCacheState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_s,1),(_Y,2),('incomplete',3),('stale',4),('delay',5),('probe',6)))
_Fsipv6NdLanCacheState_Type.__name__=_D
_Fsipv6NdLanCacheState_Object=MibTableColumn
fsipv6NdLanCacheState=_Fsipv6NdLanCacheState_Object((1,3,6,1,4,1,2076,28,1,2,7,1,5),_Fsipv6NdLanCacheState_Type())
fsipv6NdLanCacheState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6NdLanCacheState.setStatus(_A)
_Fsipv6NdLanCacheUseTime_Type=TimeTicks
_Fsipv6NdLanCacheUseTime_Object=MibTableColumn
fsipv6NdLanCacheUseTime=_Fsipv6NdLanCacheUseTime_Object((1,3,6,1,4,1,2076,28,1,2,7,1,6),_Fsipv6NdLanCacheUseTime_Type())
fsipv6NdLanCacheUseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6NdLanCacheUseTime.setStatus(_A)
_Fsipv6NdLanCacheIsSecure_Type=TruthValue
_Fsipv6NdLanCacheIsSecure_Object=MibTableColumn
fsipv6NdLanCacheIsSecure=_Fsipv6NdLanCacheIsSecure_Object((1,3,6,1,4,1,2076,28,1,2,7,1,7),_Fsipv6NdLanCacheIsSecure_Type())
fsipv6NdLanCacheIsSecure.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6NdLanCacheIsSecure.setStatus(_A)
_Fsipv6NdWanCacheTable_Object=MibTable
fsipv6NdWanCacheTable=_Fsipv6NdWanCacheTable_Object((1,3,6,1,4,1,2076,28,1,2,8))
if mibBuilder.loadTexts:fsipv6NdWanCacheTable.setStatus(_A)
_Fsipv6NdWanCacheEntry_Object=MibTableRow
fsipv6NdWanCacheEntry=_Fsipv6NdWanCacheEntry_Object((1,3,6,1,4,1,2076,28,1,2,8,1))
fsipv6NdWanCacheEntry.setIndexNames((0,_E,_t),(0,_E,_u))
if mibBuilder.loadTexts:fsipv6NdWanCacheEntry.setStatus(_A)
_Fsipv6NdWanCacheIfIndex_Type=InterfaceIndex
_Fsipv6NdWanCacheIfIndex_Object=MibTableColumn
fsipv6NdWanCacheIfIndex=_Fsipv6NdWanCacheIfIndex_Object((1,3,6,1,4,1,2076,28,1,2,8,1,1),_Fsipv6NdWanCacheIfIndex_Type())
fsipv6NdWanCacheIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6NdWanCacheIfIndex.setStatus(_A)
class _Fsipv6NdWanCacheIPv6Addr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Fsipv6NdWanCacheIPv6Addr_Type.__name__=_G
_Fsipv6NdWanCacheIPv6Addr_Object=MibTableColumn
fsipv6NdWanCacheIPv6Addr=_Fsipv6NdWanCacheIPv6Addr_Object((1,3,6,1,4,1,2076,28,1,2,8,1,2),_Fsipv6NdWanCacheIPv6Addr_Type())
fsipv6NdWanCacheIPv6Addr.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6NdWanCacheIPv6Addr.setStatus(_A)
class _Fsipv6NdWanCacheStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_O,2)))
_Fsipv6NdWanCacheStatus_Type.__name__=_D
_Fsipv6NdWanCacheStatus_Object=MibTableColumn
fsipv6NdWanCacheStatus=_Fsipv6NdWanCacheStatus_Object((1,3,6,1,4,1,2076,28,1,2,8,1,3),_Fsipv6NdWanCacheStatus_Type())
fsipv6NdWanCacheStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6NdWanCacheStatus.setStatus(_A)
class _Fsipv6NdWanCacheState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_s,1),(_Y,2)))
_Fsipv6NdWanCacheState_Type.__name__=_D
_Fsipv6NdWanCacheState_Object=MibTableColumn
fsipv6NdWanCacheState=_Fsipv6NdWanCacheState_Object((1,3,6,1,4,1,2076,28,1,2,8,1,4),_Fsipv6NdWanCacheState_Type())
fsipv6NdWanCacheState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6NdWanCacheState.setStatus(_A)
_Fsipv6NdWanCacheUseTime_Type=TimeTicks
_Fsipv6NdWanCacheUseTime_Object=MibTableColumn
fsipv6NdWanCacheUseTime=_Fsipv6NdWanCacheUseTime_Object((1,3,6,1,4,1,2076,28,1,2,8,1,5),_Fsipv6NdWanCacheUseTime_Type())
fsipv6NdWanCacheUseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6NdWanCacheUseTime.setStatus(_A)
_Fsipv6PingTable_Object=MibTable
fsipv6PingTable=_Fsipv6PingTable_Object((1,3,6,1,4,1,2076,28,1,2,12))
if mibBuilder.loadTexts:fsipv6PingTable.setStatus(_A)
_Fsipv6PingEntry_Object=MibTableRow
fsipv6PingEntry=_Fsipv6PingEntry_Object((1,3,6,1,4,1,2076,28,1,2,12,1))
fsipv6PingEntry.setIndexNames((0,_E,_v))
if mibBuilder.loadTexts:fsipv6PingEntry.setStatus(_A)
class _Fsipv6PingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_Fsipv6PingIndex_Type.__name__=_D
_Fsipv6PingIndex_Object=MibTableColumn
fsipv6PingIndex=_Fsipv6PingIndex_Object((1,3,6,1,4,1,2076,28,1,2,12,1,1),_Fsipv6PingIndex_Type())
fsipv6PingIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6PingIndex.setStatus(_A)
class _Fsipv6PingDest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Fsipv6PingDest_Type.__name__=_G
_Fsipv6PingDest_Object=MibTableColumn
fsipv6PingDest=_Fsipv6PingDest_Object((1,3,6,1,4,1,2076,28,1,2,12,1,2),_Fsipv6PingDest_Type())
fsipv6PingDest.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PingDest.setStatus(_A)
_Fsipv6PingIfIndex_Type=InterfaceIndex
_Fsipv6PingIfIndex_Object=MibTableColumn
fsipv6PingIfIndex=_Fsipv6PingIfIndex_Object((1,3,6,1,4,1,2076,28,1,2,12,1,3),_Fsipv6PingIfIndex_Type())
fsipv6PingIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PingIfIndex.setStatus(_A)
class _Fsipv6PingAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),(_Q,2),(_O,3),(_w,4)))
_Fsipv6PingAdminStatus_Type.__name__=_D
_Fsipv6PingAdminStatus_Object=MibTableColumn
fsipv6PingAdminStatus=_Fsipv6PingAdminStatus_Object((1,3,6,1,4,1,2076,28,1,2,12,1,4),_Fsipv6PingAdminStatus_Type())
fsipv6PingAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PingAdminStatus.setStatus(_A)
class _Fsipv6PingInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_Fsipv6PingInterval_Type.__name__=_D
_Fsipv6PingInterval_Object=MibTableColumn
fsipv6PingInterval=_Fsipv6PingInterval_Object((1,3,6,1,4,1,2076,28,1,2,12,1,5),_Fsipv6PingInterval_Type())
fsipv6PingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PingInterval.setStatus(_A)
class _Fsipv6PingRcvTimeout_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fsipv6PingRcvTimeout_Type.__name__=_D
_Fsipv6PingRcvTimeout_Object=MibTableColumn
fsipv6PingRcvTimeout=_Fsipv6PingRcvTimeout_Object((1,3,6,1,4,1,2076,28,1,2,12,1,6),_Fsipv6PingRcvTimeout_Type())
fsipv6PingRcvTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PingRcvTimeout.setStatus(_A)
class _Fsipv6PingTries_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_Fsipv6PingTries_Type.__name__=_D
_Fsipv6PingTries_Object=MibTableColumn
fsipv6PingTries=_Fsipv6PingTries_Object((1,3,6,1,4,1,2076,28,1,2,12,1,7),_Fsipv6PingTries_Type())
fsipv6PingTries.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PingTries.setStatus(_A)
class _Fsipv6PingSize_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,2080))
_Fsipv6PingSize_Type.__name__=_D
_Fsipv6PingSize_Object=MibTableColumn
fsipv6PingSize=_Fsipv6PingSize_Object((1,3,6,1,4,1,2076,28,1,2,12,1,8),_Fsipv6PingSize_Type())
fsipv6PingSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PingSize.setStatus(_A)
_Fsipv6PingSentCount_Type=Integer32
_Fsipv6PingSentCount_Object=MibTableColumn
fsipv6PingSentCount=_Fsipv6PingSentCount_Object((1,3,6,1,4,1,2076,28,1,2,12,1,9),_Fsipv6PingSentCount_Type())
fsipv6PingSentCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6PingSentCount.setStatus(_A)
_Fsipv6PingAverageTime_Type=Integer32
_Fsipv6PingAverageTime_Object=MibTableColumn
fsipv6PingAverageTime=_Fsipv6PingAverageTime_Object((1,3,6,1,4,1,2076,28,1,2,12,1,10),_Fsipv6PingAverageTime_Type())
fsipv6PingAverageTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6PingAverageTime.setStatus(_A)
_Fsipv6PingMaxTime_Type=Integer32
_Fsipv6PingMaxTime_Object=MibTableColumn
fsipv6PingMaxTime=_Fsipv6PingMaxTime_Object((1,3,6,1,4,1,2076,28,1,2,12,1,11),_Fsipv6PingMaxTime_Type())
fsipv6PingMaxTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6PingMaxTime.setStatus(_A)
_Fsipv6PingMinTime_Type=Integer32
_Fsipv6PingMinTime_Object=MibTableColumn
fsipv6PingMinTime=_Fsipv6PingMinTime_Object((1,3,6,1,4,1,2076,28,1,2,12,1,12),_Fsipv6PingMinTime_Type())
fsipv6PingMinTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6PingMinTime.setStatus(_A)
class _Fsipv6PingOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),('notinprogress',2)))
_Fsipv6PingOperStatus_Type.__name__=_D
_Fsipv6PingOperStatus_Object=MibTableColumn
fsipv6PingOperStatus=_Fsipv6PingOperStatus_Object((1,3,6,1,4,1,2076,28,1,2,12,1,13),_Fsipv6PingOperStatus_Type())
fsipv6PingOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6PingOperStatus.setStatus(_A)
_Fsipv6PingSuccesses_Type=Counter32
_Fsipv6PingSuccesses_Object=MibTableColumn
fsipv6PingSuccesses=_Fsipv6PingSuccesses_Object((1,3,6,1,4,1,2076,28,1,2,12,1,14),_Fsipv6PingSuccesses_Type())
fsipv6PingSuccesses.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6PingSuccesses.setStatus(_A)
_Fsipv6PingPercentageLoss_Type=Integer32
_Fsipv6PingPercentageLoss_Object=MibTableColumn
fsipv6PingPercentageLoss=_Fsipv6PingPercentageLoss_Object((1,3,6,1,4,1,2076,28,1,2,12,1,15),_Fsipv6PingPercentageLoss_Type())
fsipv6PingPercentageLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6PingPercentageLoss.setStatus(_A)
class _Fsipv6PingData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_Fsipv6PingData_Type.__name__=_G
_Fsipv6PingData_Object=MibTableColumn
fsipv6PingData=_Fsipv6PingData_Object((1,3,6,1,4,1,2076,28,1,2,12,1,16),_Fsipv6PingData_Type())
fsipv6PingData.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PingData.setStatus(_A)
class _Fsipv6PingSrcAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Fsipv6PingSrcAddr_Type.__name__=_G
_Fsipv6PingSrcAddr_Object=MibTableColumn
fsipv6PingSrcAddr=_Fsipv6PingSrcAddr_Object((1,3,6,1,4,1,2076,28,1,2,12,1,17),_Fsipv6PingSrcAddr_Type())
fsipv6PingSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PingSrcAddr.setStatus(_A)
_Fsipv6PingZoneId_Type=DisplayString
_Fsipv6PingZoneId_Object=MibTableColumn
fsipv6PingZoneId=_Fsipv6PingZoneId_Object((1,3,6,1,4,1,2076,28,1,2,12,1,18),_Fsipv6PingZoneId_Type())
fsipv6PingZoneId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PingZoneId.setStatus(_A)
class _Fsipv6PingDestAddrType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_W,0),(_S,2)))
_Fsipv6PingDestAddrType_Type.__name__=_D
_Fsipv6PingDestAddrType_Object=MibTableColumn
fsipv6PingDestAddrType=_Fsipv6PingDestAddrType_Object((1,3,6,1,4,1,2076,28,1,2,12,1,19),_Fsipv6PingDestAddrType_Type())
fsipv6PingDestAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PingDestAddrType.setStatus(_A)
class _Fsipv6PingHostName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Fsipv6PingHostName_Type.__name__=_G
_Fsipv6PingHostName_Object=MibTableColumn
fsipv6PingHostName=_Fsipv6PingHostName_Object((1,3,6,1,4,1,2076,28,1,2,12,1,20),_Fsipv6PingHostName_Type())
fsipv6PingHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6PingHostName.setStatus(_A)
_Fsipv6NDProxyListTable_Object=MibTable
fsipv6NDProxyListTable=_Fsipv6NDProxyListTable_Object((1,3,6,1,4,1,2076,28,1,2,13))
if mibBuilder.loadTexts:fsipv6NDProxyListTable.setStatus(_A)
_Fsipv6NDProxyListEntry_Object=MibTableRow
fsipv6NDProxyListEntry=_Fsipv6NDProxyListEntry_Object((1,3,6,1,4,1,2076,28,1,2,13,1))
fsipv6NDProxyListEntry.setIndexNames((0,_E,_x))
if mibBuilder.loadTexts:fsipv6NDProxyListEntry.setStatus(_A)
class _Fsipv6NdProxyAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Fsipv6NdProxyAddr_Type.__name__=_G
_Fsipv6NdProxyAddr_Object=MibTableColumn
fsipv6NdProxyAddr=_Fsipv6NdProxyAddr_Object((1,3,6,1,4,1,2076,28,1,2,13,1,1),_Fsipv6NdProxyAddr_Type())
fsipv6NdProxyAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6NdProxyAddr.setStatus(_A)
class _Fsipv6NdProxyAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_w,1),(_O,2)))
_Fsipv6NdProxyAdminStatus_Type.__name__=_D
_Fsipv6NdProxyAdminStatus_Object=MibTableColumn
fsipv6NdProxyAdminStatus=_Fsipv6NdProxyAdminStatus_Object((1,3,6,1,4,1,2076,28,1,2,13,1,2),_Fsipv6NdProxyAdminStatus_Type())
fsipv6NdProxyAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6NdProxyAdminStatus.setStatus(_A)
_Fsipv6AddrSelPolicyTable_Object=MibTable
fsipv6AddrSelPolicyTable=_Fsipv6AddrSelPolicyTable_Object((1,3,6,1,4,1,2076,28,1,2,14))
if mibBuilder.loadTexts:fsipv6AddrSelPolicyTable.setStatus(_A)
_Fsipv6AddrSelPolicyEntry_Object=MibTableRow
fsipv6AddrSelPolicyEntry=_Fsipv6AddrSelPolicyEntry_Object((1,3,6,1,4,1,2076,28,1,2,14,1))
fsipv6AddrSelPolicyEntry.setIndexNames((0,_E,_y),(0,_E,_z),(0,_E,_A0))
if mibBuilder.loadTexts:fsipv6AddrSelPolicyEntry.setStatus(_A)
class _Fsipv6AddrSelPolicyPrefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Fsipv6AddrSelPolicyPrefix_Type.__name__=_G
_Fsipv6AddrSelPolicyPrefix_Object=MibTableColumn
fsipv6AddrSelPolicyPrefix=_Fsipv6AddrSelPolicyPrefix_Object((1,3,6,1,4,1,2076,28,1,2,14,1,1),_Fsipv6AddrSelPolicyPrefix_Type())
fsipv6AddrSelPolicyPrefix.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6AddrSelPolicyPrefix.setStatus(_A)
class _Fsipv6AddrSelPolicyPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Fsipv6AddrSelPolicyPrefixLen_Type.__name__=_D
_Fsipv6AddrSelPolicyPrefixLen_Object=MibTableColumn
fsipv6AddrSelPolicyPrefixLen=_Fsipv6AddrSelPolicyPrefixLen_Object((1,3,6,1,4,1,2076,28,1,2,14,1,2),_Fsipv6AddrSelPolicyPrefixLen_Type())
fsipv6AddrSelPolicyPrefixLen.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6AddrSelPolicyPrefixLen.setStatus(_A)
_Fsipv6AddrSelPolicyIfIndex_Type=InterfaceIndex
_Fsipv6AddrSelPolicyIfIndex_Object=MibTableColumn
fsipv6AddrSelPolicyIfIndex=_Fsipv6AddrSelPolicyIfIndex_Object((1,3,6,1,4,1,2076,28,1,2,14,1,3),_Fsipv6AddrSelPolicyIfIndex_Type())
fsipv6AddrSelPolicyIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6AddrSelPolicyIfIndex.setStatus(_A)
class _Fsipv6AddrSelPolicyScope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Fsipv6AddrSelPolicyScope_Type.__name__=_D
_Fsipv6AddrSelPolicyScope_Object=MibTableColumn
fsipv6AddrSelPolicyScope=_Fsipv6AddrSelPolicyScope_Object((1,3,6,1,4,1,2076,28,1,2,14,1,4),_Fsipv6AddrSelPolicyScope_Type())
fsipv6AddrSelPolicyScope.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6AddrSelPolicyScope.setStatus(_A)
class _Fsipv6AddrSelPolicyPrecedence_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Fsipv6AddrSelPolicyPrecedence_Type.__name__=_D
_Fsipv6AddrSelPolicyPrecedence_Object=MibTableColumn
fsipv6AddrSelPolicyPrecedence=_Fsipv6AddrSelPolicyPrecedence_Object((1,3,6,1,4,1,2076,28,1,2,14,1,5),_Fsipv6AddrSelPolicyPrecedence_Type())
fsipv6AddrSelPolicyPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrSelPolicyPrecedence.setStatus(_A)
class _Fsipv6AddrSelPolicyLabel_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Fsipv6AddrSelPolicyLabel_Type.__name__=_D
_Fsipv6AddrSelPolicyLabel_Object=MibTableColumn
fsipv6AddrSelPolicyLabel=_Fsipv6AddrSelPolicyLabel_Object((1,3,6,1,4,1,2076,28,1,2,14,1,6),_Fsipv6AddrSelPolicyLabel_Type())
fsipv6AddrSelPolicyLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrSelPolicyLabel.setStatus(_A)
class _Fsipv6AddrSelPolicyAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_S,2),('multicast',3)))
_Fsipv6AddrSelPolicyAddrType_Type.__name__=_D
_Fsipv6AddrSelPolicyAddrType_Object=MibTableColumn
fsipv6AddrSelPolicyAddrType=_Fsipv6AddrSelPolicyAddrType_Object((1,3,6,1,4,1,2076,28,1,2,14,1,7),_Fsipv6AddrSelPolicyAddrType_Type())
fsipv6AddrSelPolicyAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6AddrSelPolicyAddrType.setStatus(_A)
class _Fsipv6AddrSelPolicyIsPublicAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Fsipv6AddrSelPolicyIsPublicAddr_Type.__name__=_D
_Fsipv6AddrSelPolicyIsPublicAddr_Object=MibTableColumn
fsipv6AddrSelPolicyIsPublicAddr=_Fsipv6AddrSelPolicyIsPublicAddr_Object((1,3,6,1,4,1,2076,28,1,2,14,1,8),_Fsipv6AddrSelPolicyIsPublicAddr_Type())
fsipv6AddrSelPolicyIsPublicAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6AddrSelPolicyIsPublicAddr.setStatus(_A)
class _Fsipv6AddrSelPolicyIsSelfAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Fsipv6AddrSelPolicyIsSelfAddr_Type.__name__=_D
_Fsipv6AddrSelPolicyIsSelfAddr_Object=MibTableColumn
fsipv6AddrSelPolicyIsSelfAddr=_Fsipv6AddrSelPolicyIsSelfAddr_Object((1,3,6,1,4,1,2076,28,1,2,14,1,9),_Fsipv6AddrSelPolicyIsSelfAddr_Type())
fsipv6AddrSelPolicyIsSelfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6AddrSelPolicyIsSelfAddr.setStatus(_A)
class _Fsipv6AddrSelPolicyReachabilityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),('unreachable',2)))
_Fsipv6AddrSelPolicyReachabilityStatus_Type.__name__=_D
_Fsipv6AddrSelPolicyReachabilityStatus_Object=MibTableColumn
fsipv6AddrSelPolicyReachabilityStatus=_Fsipv6AddrSelPolicyReachabilityStatus_Object((1,3,6,1,4,1,2076,28,1,2,14,1,10),_Fsipv6AddrSelPolicyReachabilityStatus_Type())
fsipv6AddrSelPolicyReachabilityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6AddrSelPolicyReachabilityStatus.setStatus(_A)
class _Fsipv6AddrSelPolicyConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),('management',2)))
_Fsipv6AddrSelPolicyConfigStatus_Type.__name__=_D
_Fsipv6AddrSelPolicyConfigStatus_Object=MibTableColumn
fsipv6AddrSelPolicyConfigStatus=_Fsipv6AddrSelPolicyConfigStatus_Object((1,3,6,1,4,1,2076,28,1,2,14,1,11),_Fsipv6AddrSelPolicyConfigStatus_Type())
fsipv6AddrSelPolicyConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6AddrSelPolicyConfigStatus.setStatus(_A)
_Fsipv6AddrSelPolicyRowStatus_Type=RowStatus
_Fsipv6AddrSelPolicyRowStatus_Object=MibTableColumn
fsipv6AddrSelPolicyRowStatus=_Fsipv6AddrSelPolicyRowStatus_Object((1,3,6,1,4,1,2076,28,1,2,14,1,12),_Fsipv6AddrSelPolicyRowStatus_Type())
fsipv6AddrSelPolicyRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:fsipv6AddrSelPolicyRowStatus.setStatus(_A)
_Fsipv6IfScopeZoneMapTable_Object=MibTable
fsipv6IfScopeZoneMapTable=_Fsipv6IfScopeZoneMapTable_Object((1,3,6,1,4,1,2076,28,1,2,15))
if mibBuilder.loadTexts:fsipv6IfScopeZoneMapTable.setStatus(_A)
_Fsipv6IfScopeZoneMapEntry_Object=MibTableRow
fsipv6IfScopeZoneMapEntry=_Fsipv6IfScopeZoneMapEntry_Object((1,3,6,1,4,1,2076,28,1,2,15,1))
fsipv6IfScopeZoneMapEntry.setIndexNames((0,_E,_A1))
if mibBuilder.loadTexts:fsipv6IfScopeZoneMapEntry.setStatus(_A)
_Fsipv6ScopeZoneIndexIfIndex_Type=InterfaceIndex
_Fsipv6ScopeZoneIndexIfIndex_Object=MibTableColumn
fsipv6ScopeZoneIndexIfIndex=_Fsipv6ScopeZoneIndexIfIndex_Object((1,3,6,1,4,1,2076,28,1,2,15,1,1),_Fsipv6ScopeZoneIndexIfIndex_Type())
fsipv6ScopeZoneIndexIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndexIfIndex.setStatus(_A)
class _Fsipv6ScopeZoneIndexInterfaceLocal_Type(DisplayString):defaultValue=OctetString(_L)
_Fsipv6ScopeZoneIndexInterfaceLocal_Type.__name__=_I
_Fsipv6ScopeZoneIndexInterfaceLocal_Object=MibTableColumn
fsipv6ScopeZoneIndexInterfaceLocal=_Fsipv6ScopeZoneIndexInterfaceLocal_Object((1,3,6,1,4,1,2076,28,1,2,15,1,2),_Fsipv6ScopeZoneIndexInterfaceLocal_Type())
fsipv6ScopeZoneIndexInterfaceLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndexInterfaceLocal.setStatus(_A)
class _Fsipv6ScopeZoneIndexLinkLocal_Type(DisplayString):defaultValue=OctetString(_L)
_Fsipv6ScopeZoneIndexLinkLocal_Type.__name__=_I
_Fsipv6ScopeZoneIndexLinkLocal_Object=MibTableColumn
fsipv6ScopeZoneIndexLinkLocal=_Fsipv6ScopeZoneIndexLinkLocal_Object((1,3,6,1,4,1,2076,28,1,2,15,1,3),_Fsipv6ScopeZoneIndexLinkLocal_Type())
fsipv6ScopeZoneIndexLinkLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndexLinkLocal.setStatus(_A)
class _Fsipv6ScopeZoneIndex3_Type(DisplayString):defaultValue=OctetString(_L)
_Fsipv6ScopeZoneIndex3_Type.__name__=_I
_Fsipv6ScopeZoneIndex3_Object=MibTableColumn
fsipv6ScopeZoneIndex3=_Fsipv6ScopeZoneIndex3_Object((1,3,6,1,4,1,2076,28,1,2,15,1,4),_Fsipv6ScopeZoneIndex3_Type())
fsipv6ScopeZoneIndex3.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndex3.setStatus(_A)
class _Fsipv6ScopeZoneIndexAdminLocal_Type(DisplayString):defaultValue=OctetString(_L)
_Fsipv6ScopeZoneIndexAdminLocal_Type.__name__=_I
_Fsipv6ScopeZoneIndexAdminLocal_Object=MibTableColumn
fsipv6ScopeZoneIndexAdminLocal=_Fsipv6ScopeZoneIndexAdminLocal_Object((1,3,6,1,4,1,2076,28,1,2,15,1,5),_Fsipv6ScopeZoneIndexAdminLocal_Type())
fsipv6ScopeZoneIndexAdminLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndexAdminLocal.setStatus(_A)
class _Fsipv6ScopeZoneIndexSiteLocal_Type(DisplayString):defaultValue=OctetString(_L)
_Fsipv6ScopeZoneIndexSiteLocal_Type.__name__=_I
_Fsipv6ScopeZoneIndexSiteLocal_Object=MibTableColumn
fsipv6ScopeZoneIndexSiteLocal=_Fsipv6ScopeZoneIndexSiteLocal_Object((1,3,6,1,4,1,2076,28,1,2,15,1,6),_Fsipv6ScopeZoneIndexSiteLocal_Type())
fsipv6ScopeZoneIndexSiteLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndexSiteLocal.setStatus(_A)
class _Fsipv6ScopeZoneIndex6_Type(DisplayString):defaultValue=OctetString(_L)
_Fsipv6ScopeZoneIndex6_Type.__name__=_I
_Fsipv6ScopeZoneIndex6_Object=MibTableColumn
fsipv6ScopeZoneIndex6=_Fsipv6ScopeZoneIndex6_Object((1,3,6,1,4,1,2076,28,1,2,15,1,7),_Fsipv6ScopeZoneIndex6_Type())
fsipv6ScopeZoneIndex6.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndex6.setStatus(_A)
class _Fsipv6ScopeZoneIndex7_Type(DisplayString):defaultValue=OctetString(_L)
_Fsipv6ScopeZoneIndex7_Type.__name__=_I
_Fsipv6ScopeZoneIndex7_Object=MibTableColumn
fsipv6ScopeZoneIndex7=_Fsipv6ScopeZoneIndex7_Object((1,3,6,1,4,1,2076,28,1,2,15,1,8),_Fsipv6ScopeZoneIndex7_Type())
fsipv6ScopeZoneIndex7.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndex7.setStatus(_A)
class _Fsipv6ScopeZoneIndexOrganizationLocal_Type(DisplayString):defaultValue=OctetString(_L)
_Fsipv6ScopeZoneIndexOrganizationLocal_Type.__name__=_I
_Fsipv6ScopeZoneIndexOrganizationLocal_Object=MibTableColumn
fsipv6ScopeZoneIndexOrganizationLocal=_Fsipv6ScopeZoneIndexOrganizationLocal_Object((1,3,6,1,4,1,2076,28,1,2,15,1,9),_Fsipv6ScopeZoneIndexOrganizationLocal_Type())
fsipv6ScopeZoneIndexOrganizationLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndexOrganizationLocal.setStatus(_A)
class _Fsipv6ScopeZoneIndex9_Type(DisplayString):defaultValue=OctetString(_L)
_Fsipv6ScopeZoneIndex9_Type.__name__=_I
_Fsipv6ScopeZoneIndex9_Object=MibTableColumn
fsipv6ScopeZoneIndex9=_Fsipv6ScopeZoneIndex9_Object((1,3,6,1,4,1,2076,28,1,2,15,1,10),_Fsipv6ScopeZoneIndex9_Type())
fsipv6ScopeZoneIndex9.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndex9.setStatus(_A)
class _Fsipv6ScopeZoneIndexA_Type(DisplayString):defaultValue=OctetString(_L)
_Fsipv6ScopeZoneIndexA_Type.__name__=_I
_Fsipv6ScopeZoneIndexA_Object=MibTableColumn
fsipv6ScopeZoneIndexA=_Fsipv6ScopeZoneIndexA_Object((1,3,6,1,4,1,2076,28,1,2,15,1,11),_Fsipv6ScopeZoneIndexA_Type())
fsipv6ScopeZoneIndexA.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndexA.setStatus(_A)
class _Fsipv6ScopeZoneIndexB_Type(DisplayString):defaultValue=OctetString(_L)
_Fsipv6ScopeZoneIndexB_Type.__name__=_I
_Fsipv6ScopeZoneIndexB_Object=MibTableColumn
fsipv6ScopeZoneIndexB=_Fsipv6ScopeZoneIndexB_Object((1,3,6,1,4,1,2076,28,1,2,15,1,12),_Fsipv6ScopeZoneIndexB_Type())
fsipv6ScopeZoneIndexB.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndexB.setStatus(_A)
class _Fsipv6ScopeZoneIndexC_Type(DisplayString):defaultValue=OctetString(_L)
_Fsipv6ScopeZoneIndexC_Type.__name__=_I
_Fsipv6ScopeZoneIndexC_Object=MibTableColumn
fsipv6ScopeZoneIndexC=_Fsipv6ScopeZoneIndexC_Object((1,3,6,1,4,1,2076,28,1,2,15,1,13),_Fsipv6ScopeZoneIndexC_Type())
fsipv6ScopeZoneIndexC.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndexC.setStatus(_A)
class _Fsipv6ScopeZoneIndexD_Type(DisplayString):defaultValue=OctetString(_L)
_Fsipv6ScopeZoneIndexD_Type.__name__=_I
_Fsipv6ScopeZoneIndexD_Object=MibTableColumn
fsipv6ScopeZoneIndexD=_Fsipv6ScopeZoneIndexD_Object((1,3,6,1,4,1,2076,28,1,2,15,1,14),_Fsipv6ScopeZoneIndexD_Type())
fsipv6ScopeZoneIndexD.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndexD.setStatus(_A)
class _Fsipv6ScopeZoneIndexE_Type(DisplayString):defaultValue=OctetString(_L)
_Fsipv6ScopeZoneIndexE_Type.__name__=_I
_Fsipv6ScopeZoneIndexE_Object=MibTableColumn
fsipv6ScopeZoneIndexE=_Fsipv6ScopeZoneIndexE_Object((1,3,6,1,4,1,2076,28,1,2,15,1,15),_Fsipv6ScopeZoneIndexE_Type())
fsipv6ScopeZoneIndexE.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndexE.setStatus(_A)
class _Fsipv6IfScopeZoneCreationStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notcreated',0),(_Z,1),('mgmt',2),(_A2,3)))
_Fsipv6IfScopeZoneCreationStatus_Type.__name__=_D
_Fsipv6IfScopeZoneCreationStatus_Object=MibTableColumn
fsipv6IfScopeZoneCreationStatus=_Fsipv6IfScopeZoneCreationStatus_Object((1,3,6,1,4,1,2076,28,1,2,15,1,16),_Fsipv6IfScopeZoneCreationStatus_Type())
fsipv6IfScopeZoneCreationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IfScopeZoneCreationStatus.setStatus(_A)
_Fsipv6IfScopeZoneRowStatus_Type=RowStatus
_Fsipv6IfScopeZoneRowStatus_Object=MibTableColumn
fsipv6IfScopeZoneRowStatus=_Fsipv6IfScopeZoneRowStatus_Object((1,3,6,1,4,1,2076,28,1,2,15,1,17),_Fsipv6IfScopeZoneRowStatus_Type())
fsipv6IfScopeZoneRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:fsipv6IfScopeZoneRowStatus.setStatus(_A)
_Fsipv6ScopeZoneTable_Object=MibTable
fsipv6ScopeZoneTable=_Fsipv6ScopeZoneTable_Object((1,3,6,1,4,1,2076,28,1,2,16))
if mibBuilder.loadTexts:fsipv6ScopeZoneTable.setStatus(_A)
_Fsipv6ScopeZoneEntry_Object=MibTableRow
fsipv6ScopeZoneEntry=_Fsipv6ScopeZoneEntry_Object((1,3,6,1,4,1,2076,28,1,2,16,1))
fsipv6ScopeZoneEntry.setIndexNames((0,_E,_A3))
if mibBuilder.loadTexts:fsipv6ScopeZoneEntry.setStatus(_A)
_Fsipv6ScopeZoneName_Type=DisplayString
_Fsipv6ScopeZoneName_Object=MibTableColumn
fsipv6ScopeZoneName=_Fsipv6ScopeZoneName_Object((1,3,6,1,4,1,2076,28,1,2,16,1,1),_Fsipv6ScopeZoneName_Type())
fsipv6ScopeZoneName.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6ScopeZoneName.setStatus(_A)
_Fsipv6ScopeZoneIndex_Type=InetZoneIndex
_Fsipv6ScopeZoneIndex_Object=MibTableColumn
fsipv6ScopeZoneIndex=_Fsipv6ScopeZoneIndex_Object((1,3,6,1,4,1,2076,28,1,2,16,1,2),_Fsipv6ScopeZoneIndex_Type())
fsipv6ScopeZoneIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6ScopeZoneIndex.setStatus(_A)
class _Fsipv6ScopeZoneCreationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),('mgmt',2),(_A2,3)))
_Fsipv6ScopeZoneCreationStatus_Type.__name__=_D
_Fsipv6ScopeZoneCreationStatus_Object=MibTableColumn
fsipv6ScopeZoneCreationStatus=_Fsipv6ScopeZoneCreationStatus_Object((1,3,6,1,4,1,2076,28,1,2,16,1,3),_Fsipv6ScopeZoneCreationStatus_Type())
fsipv6ScopeZoneCreationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6ScopeZoneCreationStatus.setStatus(_A)
_Fsipv6ScopeZoneInterfaceList_Type=InterfaceList
_Fsipv6ScopeZoneInterfaceList_Object=MibTableColumn
fsipv6ScopeZoneInterfaceList=_Fsipv6ScopeZoneInterfaceList_Object((1,3,6,1,4,1,2076,28,1,2,16,1,4),_Fsipv6ScopeZoneInterfaceList_Type())
fsipv6ScopeZoneInterfaceList.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6ScopeZoneInterfaceList.setStatus(_A)
class _Fsipv6IsDefaultScopeZone_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_Fsipv6IsDefaultScopeZone_Type.__name__=_D
_Fsipv6IsDefaultScopeZone_Object=MibTableColumn
fsipv6IsDefaultScopeZone=_Fsipv6IsDefaultScopeZone_Object((1,3,6,1,4,1,2076,28,1,2,16,1,5),_Fsipv6IsDefaultScopeZone_Type())
fsipv6IsDefaultScopeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IsDefaultScopeZone.setStatus(_A)
_Fsipv6SENDSentPktStatsTable_Object=MibTable
fsipv6SENDSentPktStatsTable=_Fsipv6SENDSentPktStatsTable_Object((1,3,6,1,4,1,2076,28,1,2,17))
if mibBuilder.loadTexts:fsipv6SENDSentPktStatsTable.setStatus(_A)
_Fsipv6SENDSentPktStatsEntry_Object=MibTableRow
fsipv6SENDSentPktStatsEntry=_Fsipv6SENDSentPktStatsEntry_Object((1,3,6,1,4,1,2076,28,1,2,17,1))
fsipv6SENDSentPktStatsEntry.setIndexNames((0,_E,_M),(0,_E,_A4))
if mibBuilder.loadTexts:fsipv6SENDSentPktStatsEntry.setStatus(_A)
class _Fsipv6SENDSentPktType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ns',1),('na',2),('rs',3),('ra',4),('rd',5),(_a,6),(_b,7)))
_Fsipv6SENDSentPktType_Type.__name__=_D
_Fsipv6SENDSentPktType_Object=MibTableColumn
fsipv6SENDSentPktType=_Fsipv6SENDSentPktType_Object((1,3,6,1,4,1,2076,28,1,2,17,1,1),_Fsipv6SENDSentPktType_Type())
fsipv6SENDSentPktType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6SENDSentPktType.setStatus(_A)
_Fsipv6SENDSentCgaOptPkts_Type=Counter32
_Fsipv6SENDSentCgaOptPkts_Object=MibTableColumn
fsipv6SENDSentCgaOptPkts=_Fsipv6SENDSentCgaOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,17,1,2),_Fsipv6SENDSentCgaOptPkts_Type())
fsipv6SENDSentCgaOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDSentCgaOptPkts.setStatus(_A)
_Fsipv6SENDSentCertOptPkts_Type=Counter32
_Fsipv6SENDSentCertOptPkts_Object=MibTableColumn
fsipv6SENDSentCertOptPkts=_Fsipv6SENDSentCertOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,17,1,3),_Fsipv6SENDSentCertOptPkts_Type())
fsipv6SENDSentCertOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDSentCertOptPkts.setStatus(_A)
_Fsipv6SENDSentMtuOptPkts_Type=Counter32
_Fsipv6SENDSentMtuOptPkts_Object=MibTableColumn
fsipv6SENDSentMtuOptPkts=_Fsipv6SENDSentMtuOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,17,1,4),_Fsipv6SENDSentMtuOptPkts_Type())
fsipv6SENDSentMtuOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDSentMtuOptPkts.setStatus(_A)
_Fsipv6SENDSentNonceOptPkts_Type=Counter32
_Fsipv6SENDSentNonceOptPkts_Object=MibTableColumn
fsipv6SENDSentNonceOptPkts=_Fsipv6SENDSentNonceOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,17,1,5),_Fsipv6SENDSentNonceOptPkts_Type())
fsipv6SENDSentNonceOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDSentNonceOptPkts.setStatus(_A)
_Fsipv6SENDSentPrefixOptPkts_Type=Counter32
_Fsipv6SENDSentPrefixOptPkts_Object=MibTableColumn
fsipv6SENDSentPrefixOptPkts=_Fsipv6SENDSentPrefixOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,17,1,6),_Fsipv6SENDSentPrefixOptPkts_Type())
fsipv6SENDSentPrefixOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDSentPrefixOptPkts.setStatus(_A)
_Fsipv6SENDSentRedirHdrPkts_Type=Counter32
_Fsipv6SENDSentRedirHdrPkts_Object=MibTableColumn
fsipv6SENDSentRedirHdrPkts=_Fsipv6SENDSentRedirHdrPkts_Object((1,3,6,1,4,1,2076,28,1,2,17,1,7),_Fsipv6SENDSentRedirHdrPkts_Type())
fsipv6SENDSentRedirHdrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDSentRedirHdrPkts.setStatus(_A)
_Fsipv6SENDSentRsaOptPkts_Type=Counter32
_Fsipv6SENDSentRsaOptPkts_Object=MibTableColumn
fsipv6SENDSentRsaOptPkts=_Fsipv6SENDSentRsaOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,17,1,8),_Fsipv6SENDSentRsaOptPkts_Type())
fsipv6SENDSentRsaOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDSentRsaOptPkts.setStatus(_A)
_Fsipv6SENDSentSrcLinkAddrPkts_Type=Counter32
_Fsipv6SENDSentSrcLinkAddrPkts_Object=MibTableColumn
fsipv6SENDSentSrcLinkAddrPkts=_Fsipv6SENDSentSrcLinkAddrPkts_Object((1,3,6,1,4,1,2076,28,1,2,17,1,9),_Fsipv6SENDSentSrcLinkAddrPkts_Type())
fsipv6SENDSentSrcLinkAddrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDSentSrcLinkAddrPkts.setStatus(_A)
_Fsipv6SENDSentTgtLinkAddrPkts_Type=Counter32
_Fsipv6SENDSentTgtLinkAddrPkts_Object=MibTableColumn
fsipv6SENDSentTgtLinkAddrPkts=_Fsipv6SENDSentTgtLinkAddrPkts_Object((1,3,6,1,4,1,2076,28,1,2,17,1,10),_Fsipv6SENDSentTgtLinkAddrPkts_Type())
fsipv6SENDSentTgtLinkAddrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDSentTgtLinkAddrPkts.setStatus(_A)
_Fsipv6SENDSentTaOptPkts_Type=Counter32
_Fsipv6SENDSentTaOptPkts_Object=MibTableColumn
fsipv6SENDSentTaOptPkts=_Fsipv6SENDSentTaOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,17,1,11),_Fsipv6SENDSentTaOptPkts_Type())
fsipv6SENDSentTaOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDSentTaOptPkts.setStatus(_A)
_Fsipv6SENDSentTimeStampOptPkts_Type=Counter32
_Fsipv6SENDSentTimeStampOptPkts_Object=MibTableColumn
fsipv6SENDSentTimeStampOptPkts=_Fsipv6SENDSentTimeStampOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,17,1,12),_Fsipv6SENDSentTimeStampOptPkts_Type())
fsipv6SENDSentTimeStampOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDSentTimeStampOptPkts.setStatus(_A)
_Fsipv6SENDRcvPktStatsTable_Object=MibTable
fsipv6SENDRcvPktStatsTable=_Fsipv6SENDRcvPktStatsTable_Object((1,3,6,1,4,1,2076,28,1,2,18))
if mibBuilder.loadTexts:fsipv6SENDRcvPktStatsTable.setStatus(_A)
_Fsipv6SENDRcvPktStatsEntry_Object=MibTableRow
fsipv6SENDRcvPktStatsEntry=_Fsipv6SENDRcvPktStatsEntry_Object((1,3,6,1,4,1,2076,28,1,2,18,1))
fsipv6SENDRcvPktStatsEntry.setIndexNames((0,_E,_M),(0,_E,_A5))
if mibBuilder.loadTexts:fsipv6SENDRcvPktStatsEntry.setStatus(_A)
class _Fsipv6SENDRcvPktType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ns',1),('na',2),('rs',3),('ra',4),('rd',5),(_a,6),(_b,7)))
_Fsipv6SENDRcvPktType_Type.__name__=_D
_Fsipv6SENDRcvPktType_Object=MibTableColumn
fsipv6SENDRcvPktType=_Fsipv6SENDRcvPktType_Object((1,3,6,1,4,1,2076,28,1,2,18,1,1),_Fsipv6SENDRcvPktType_Type())
fsipv6SENDRcvPktType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6SENDRcvPktType.setStatus(_A)
_Fsipv6SENDRcvCgaOptPkts_Type=Counter32
_Fsipv6SENDRcvCgaOptPkts_Object=MibTableColumn
fsipv6SENDRcvCgaOptPkts=_Fsipv6SENDRcvCgaOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,18,1,2),_Fsipv6SENDRcvCgaOptPkts_Type())
fsipv6SENDRcvCgaOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDRcvCgaOptPkts.setStatus(_A)
_Fsipv6SENDRcvCertOptPkts_Type=Counter32
_Fsipv6SENDRcvCertOptPkts_Object=MibTableColumn
fsipv6SENDRcvCertOptPkts=_Fsipv6SENDRcvCertOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,18,1,3),_Fsipv6SENDRcvCertOptPkts_Type())
fsipv6SENDRcvCertOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDRcvCertOptPkts.setStatus(_A)
_Fsipv6SENDRcvMtuOptPkts_Type=Counter32
_Fsipv6SENDRcvMtuOptPkts_Object=MibTableColumn
fsipv6SENDRcvMtuOptPkts=_Fsipv6SENDRcvMtuOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,18,1,4),_Fsipv6SENDRcvMtuOptPkts_Type())
fsipv6SENDRcvMtuOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDRcvMtuOptPkts.setStatus(_A)
_Fsipv6SENDRcvNonceOptPkts_Type=Counter32
_Fsipv6SENDRcvNonceOptPkts_Object=MibTableColumn
fsipv6SENDRcvNonceOptPkts=_Fsipv6SENDRcvNonceOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,18,1,5),_Fsipv6SENDRcvNonceOptPkts_Type())
fsipv6SENDRcvNonceOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDRcvNonceOptPkts.setStatus(_A)
_Fsipv6SENDRcvPrefixOptPkts_Type=Counter32
_Fsipv6SENDRcvPrefixOptPkts_Object=MibTableColumn
fsipv6SENDRcvPrefixOptPkts=_Fsipv6SENDRcvPrefixOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,18,1,6),_Fsipv6SENDRcvPrefixOptPkts_Type())
fsipv6SENDRcvPrefixOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDRcvPrefixOptPkts.setStatus(_A)
_Fsipv6SENDRcvRedirHdrPkts_Type=Counter32
_Fsipv6SENDRcvRedirHdrPkts_Object=MibTableColumn
fsipv6SENDRcvRedirHdrPkts=_Fsipv6SENDRcvRedirHdrPkts_Object((1,3,6,1,4,1,2076,28,1,2,18,1,7),_Fsipv6SENDRcvRedirHdrPkts_Type())
fsipv6SENDRcvRedirHdrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDRcvRedirHdrPkts.setStatus(_A)
_Fsipv6SENDRcvRsaOptPkts_Type=Counter32
_Fsipv6SENDRcvRsaOptPkts_Object=MibTableColumn
fsipv6SENDRcvRsaOptPkts=_Fsipv6SENDRcvRsaOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,18,1,8),_Fsipv6SENDRcvRsaOptPkts_Type())
fsipv6SENDRcvRsaOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDRcvRsaOptPkts.setStatus(_A)
_Fsipv6SENDRcvSrcLinkAddrPkts_Type=Counter32
_Fsipv6SENDRcvSrcLinkAddrPkts_Object=MibTableColumn
fsipv6SENDRcvSrcLinkAddrPkts=_Fsipv6SENDRcvSrcLinkAddrPkts_Object((1,3,6,1,4,1,2076,28,1,2,18,1,9),_Fsipv6SENDRcvSrcLinkAddrPkts_Type())
fsipv6SENDRcvSrcLinkAddrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDRcvSrcLinkAddrPkts.setStatus(_A)
_Fsipv6SENDRcvTgtLinkAddrPkts_Type=Counter32
_Fsipv6SENDRcvTgtLinkAddrPkts_Object=MibTableColumn
fsipv6SENDRcvTgtLinkAddrPkts=_Fsipv6SENDRcvTgtLinkAddrPkts_Object((1,3,6,1,4,1,2076,28,1,2,18,1,10),_Fsipv6SENDRcvTgtLinkAddrPkts_Type())
fsipv6SENDRcvTgtLinkAddrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDRcvTgtLinkAddrPkts.setStatus(_A)
_Fsipv6SENDRcvTaOptPkts_Type=Counter32
_Fsipv6SENDRcvTaOptPkts_Object=MibTableColumn
fsipv6SENDRcvTaOptPkts=_Fsipv6SENDRcvTaOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,18,1,11),_Fsipv6SENDRcvTaOptPkts_Type())
fsipv6SENDRcvTaOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDRcvTaOptPkts.setStatus(_A)
_Fsipv6SENDRcvTimeStampOptPkts_Type=Counter32
_Fsipv6SENDRcvTimeStampOptPkts_Object=MibTableColumn
fsipv6SENDRcvTimeStampOptPkts=_Fsipv6SENDRcvTimeStampOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,18,1,12),_Fsipv6SENDRcvTimeStampOptPkts_Type())
fsipv6SENDRcvTimeStampOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDRcvTimeStampOptPkts.setStatus(_A)
_Fsipv6SENDDrpPktStatsTable_Object=MibTable
fsipv6SENDDrpPktStatsTable=_Fsipv6SENDDrpPktStatsTable_Object((1,3,6,1,4,1,2076,28,1,2,19))
if mibBuilder.loadTexts:fsipv6SENDDrpPktStatsTable.setStatus(_A)
_Fsipv6SENDDrpPktStatsEntry_Object=MibTableRow
fsipv6SENDDrpPktStatsEntry=_Fsipv6SENDDrpPktStatsEntry_Object((1,3,6,1,4,1,2076,28,1,2,19,1))
fsipv6SENDDrpPktStatsEntry.setIndexNames((0,_E,_M),(0,_E,_A6))
if mibBuilder.loadTexts:fsipv6SENDDrpPktStatsEntry.setStatus(_A)
class _Fsipv6SENDDrpPktType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ns',1),('na',2),('rs',3),('ra',4),('rd',5),(_a,6),(_b,7)))
_Fsipv6SENDDrpPktType_Type.__name__=_D
_Fsipv6SENDDrpPktType_Object=MibTableColumn
fsipv6SENDDrpPktType=_Fsipv6SENDDrpPktType_Object((1,3,6,1,4,1,2076,28,1,2,19,1,1),_Fsipv6SENDDrpPktType_Type())
fsipv6SENDDrpPktType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6SENDDrpPktType.setStatus(_A)
_Fsipv6SENDDrpCgaOptPkts_Type=Counter32
_Fsipv6SENDDrpCgaOptPkts_Object=MibTableColumn
fsipv6SENDDrpCgaOptPkts=_Fsipv6SENDDrpCgaOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,19,1,2),_Fsipv6SENDDrpCgaOptPkts_Type())
fsipv6SENDDrpCgaOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDDrpCgaOptPkts.setStatus(_A)
_Fsipv6SENDDrpCertOptPkts_Type=Counter32
_Fsipv6SENDDrpCertOptPkts_Object=MibTableColumn
fsipv6SENDDrpCertOptPkts=_Fsipv6SENDDrpCertOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,19,1,3),_Fsipv6SENDDrpCertOptPkts_Type())
fsipv6SENDDrpCertOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDDrpCertOptPkts.setStatus(_A)
_Fsipv6SENDDrpMtuOptPkts_Type=Counter32
_Fsipv6SENDDrpMtuOptPkts_Object=MibTableColumn
fsipv6SENDDrpMtuOptPkts=_Fsipv6SENDDrpMtuOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,19,1,4),_Fsipv6SENDDrpMtuOptPkts_Type())
fsipv6SENDDrpMtuOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDDrpMtuOptPkts.setStatus(_A)
_Fsipv6SENDDrpNonceOptPkts_Type=Counter32
_Fsipv6SENDDrpNonceOptPkts_Object=MibTableColumn
fsipv6SENDDrpNonceOptPkts=_Fsipv6SENDDrpNonceOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,19,1,5),_Fsipv6SENDDrpNonceOptPkts_Type())
fsipv6SENDDrpNonceOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDDrpNonceOptPkts.setStatus(_A)
_Fsipv6SENDDrpPrefixOptPkts_Type=Counter32
_Fsipv6SENDDrpPrefixOptPkts_Object=MibTableColumn
fsipv6SENDDrpPrefixOptPkts=_Fsipv6SENDDrpPrefixOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,19,1,6),_Fsipv6SENDDrpPrefixOptPkts_Type())
fsipv6SENDDrpPrefixOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDDrpPrefixOptPkts.setStatus(_A)
_Fsipv6SENDDrpRedirHdrPkts_Type=Counter32
_Fsipv6SENDDrpRedirHdrPkts_Object=MibTableColumn
fsipv6SENDDrpRedirHdrPkts=_Fsipv6SENDDrpRedirHdrPkts_Object((1,3,6,1,4,1,2076,28,1,2,19,1,7),_Fsipv6SENDDrpRedirHdrPkts_Type())
fsipv6SENDDrpRedirHdrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDDrpRedirHdrPkts.setStatus(_A)
_Fsipv6SENDDrpRsaOptPkts_Type=Counter32
_Fsipv6SENDDrpRsaOptPkts_Object=MibTableColumn
fsipv6SENDDrpRsaOptPkts=_Fsipv6SENDDrpRsaOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,19,1,8),_Fsipv6SENDDrpRsaOptPkts_Type())
fsipv6SENDDrpRsaOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDDrpRsaOptPkts.setStatus(_A)
_Fsipv6SENDDrpSrcLinkAddrPkts_Type=Counter32
_Fsipv6SENDDrpSrcLinkAddrPkts_Object=MibTableColumn
fsipv6SENDDrpSrcLinkAddrPkts=_Fsipv6SENDDrpSrcLinkAddrPkts_Object((1,3,6,1,4,1,2076,28,1,2,19,1,9),_Fsipv6SENDDrpSrcLinkAddrPkts_Type())
fsipv6SENDDrpSrcLinkAddrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDDrpSrcLinkAddrPkts.setStatus(_A)
_Fsipv6SENDDrpTgtLinkAddrPkts_Type=Counter32
_Fsipv6SENDDrpTgtLinkAddrPkts_Object=MibTableColumn
fsipv6SENDDrpTgtLinkAddrPkts=_Fsipv6SENDDrpTgtLinkAddrPkts_Object((1,3,6,1,4,1,2076,28,1,2,19,1,10),_Fsipv6SENDDrpTgtLinkAddrPkts_Type())
fsipv6SENDDrpTgtLinkAddrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDDrpTgtLinkAddrPkts.setStatus(_A)
_Fsipv6SENDDrpTaOptPkts_Type=Counter32
_Fsipv6SENDDrpTaOptPkts_Object=MibTableColumn
fsipv6SENDDrpTaOptPkts=_Fsipv6SENDDrpTaOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,19,1,11),_Fsipv6SENDDrpTaOptPkts_Type())
fsipv6SENDDrpTaOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDDrpTaOptPkts.setStatus(_A)
_Fsipv6SENDDrpTimeStampOptPkts_Type=Counter32
_Fsipv6SENDDrpTimeStampOptPkts_Object=MibTableColumn
fsipv6SENDDrpTimeStampOptPkts=_Fsipv6SENDDrpTimeStampOptPkts_Object((1,3,6,1,4,1,2076,28,1,2,19,1,12),_Fsipv6SENDDrpTimeStampOptPkts_Type())
fsipv6SENDDrpTimeStampOptPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6SENDDrpTimeStampOptPkts.setStatus(_A)
_Fsipv6RARouteInfoTable_Object=MibTable
fsipv6RARouteInfoTable=_Fsipv6RARouteInfoTable_Object((1,3,6,1,4,1,2076,28,1,2,20))
if mibBuilder.loadTexts:fsipv6RARouteInfoTable.setStatus(_A)
_Fsipv6RARouteInfoEntry_Object=MibTableRow
fsipv6RARouteInfoEntry=_Fsipv6RARouteInfoEntry_Object((1,3,6,1,4,1,2076,28,1,2,20,1))
fsipv6RARouteInfoEntry.setIndexNames((0,_E,_A7),(0,_E,_A8),(0,_E,_A9))
if mibBuilder.loadTexts:fsipv6RARouteInfoEntry.setStatus(_A)
_Fsipv6RARouteIfIndex_Type=InterfaceIndex
_Fsipv6RARouteIfIndex_Object=MibTableColumn
fsipv6RARouteIfIndex=_Fsipv6RARouteIfIndex_Object((1,3,6,1,4,1,2076,28,1,2,20,1,1),_Fsipv6RARouteIfIndex_Type())
fsipv6RARouteIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6RARouteIfIndex.setStatus(_A)
class _Fsipv6RARoutePrefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Fsipv6RARoutePrefix_Type.__name__=_G
_Fsipv6RARoutePrefix_Object=MibTableColumn
fsipv6RARoutePrefix=_Fsipv6RARoutePrefix_Object((1,3,6,1,4,1,2076,28,1,2,20,1,2),_Fsipv6RARoutePrefix_Type())
fsipv6RARoutePrefix.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6RARoutePrefix.setStatus(_A)
class _Fsipv6RARoutePrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Fsipv6RARoutePrefixLen_Type.__name__=_D
_Fsipv6RARoutePrefixLen_Object=MibTableColumn
fsipv6RARoutePrefixLen=_Fsipv6RARoutePrefixLen_Object((1,3,6,1,4,1,2076,28,1,2,20,1,3),_Fsipv6RARoutePrefixLen_Type())
fsipv6RARoutePrefixLen.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6RARoutePrefixLen.setStatus(_A)
class _Fsipv6RARoutePreference_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('low',0),(_f,1),('high',2)))
_Fsipv6RARoutePreference_Type.__name__=_D
_Fsipv6RARoutePreference_Object=MibTableColumn
fsipv6RARoutePreference=_Fsipv6RARoutePreference_Object((1,3,6,1,4,1,2076,28,1,2,20,1,4),_Fsipv6RARoutePreference_Type())
fsipv6RARoutePreference.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6RARoutePreference.setStatus(_A)
class _Fsipv6RARouteLifetime_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Fsipv6RARouteLifetime_Type.__name__=_H
_Fsipv6RARouteLifetime_Object=MibTableColumn
fsipv6RARouteLifetime=_Fsipv6RARouteLifetime_Object((1,3,6,1,4,1,2076,28,1,2,20,1,5),_Fsipv6RARouteLifetime_Type())
fsipv6RARouteLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6RARouteLifetime.setStatus(_A)
_Fsipv6RARouteRowStatus_Type=RowStatus
_Fsipv6RARouteRowStatus_Object=MibTableColumn
fsipv6RARouteRowStatus=_Fsipv6RARouteRowStatus_Object((1,3,6,1,4,1,2076,28,1,2,20,1,6),_Fsipv6RARouteRowStatus_Type())
fsipv6RARouteRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:fsipv6RARouteRowStatus.setStatus(_A)
_Fsipv6Test_ObjectIdentity=ObjectIdentity
fsipv6Test=_Fsipv6Test_ObjectIdentity((1,3,6,1,4,1,2076,28,1,3))
_FsIpv6TestRedEntryTime_Type=Integer32
_FsIpv6TestRedEntryTime_Object=MibScalar
fsIpv6TestRedEntryTime=_FsIpv6TestRedEntryTime_Object((1,3,6,1,4,1,2076,28,1,3,1),_FsIpv6TestRedEntryTime_Type())
fsIpv6TestRedEntryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6TestRedEntryTime.setStatus(_A)
_FsIpv6TestRedExitTime_Type=Integer32
_FsIpv6TestRedExitTime_Object=MibScalar
fsIpv6TestRedExitTime=_FsIpv6TestRedExitTime_Object((1,3,6,1,4,1,2076,28,1,3,2),_FsIpv6TestRedExitTime_Type())
fsIpv6TestRedExitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6TestRedExitTime.setStatus(_A)
_Fsipv6RaRDNSSTable_ObjectIdentity=ObjectIdentity
fsipv6RaRDNSSTable=_Fsipv6RaRDNSSTable_ObjectIdentity((1,3,6,1,4,1,2076,28,1,4))
_Fsipv6IfRaRDNSSTable_Object=MibTable
fsipv6IfRaRDNSSTable=_Fsipv6IfRaRDNSSTable_Object((1,3,6,1,4,1,2076,28,1,4,1))
if mibBuilder.loadTexts:fsipv6IfRaRDNSSTable.setStatus(_A)
_Fsipv6IfRaRDNSSEntry_Object=MibTableRow
fsipv6IfRaRDNSSEntry=_Fsipv6IfRaRDNSSEntry_Object((1,3,6,1,4,1,2076,28,1,4,1,1))
fsipv6IfRaRDNSSEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:fsipv6IfRaRDNSSEntry.setStatus(_A)
_Fsipv6IfRaRDNSSIndex_Type=InterfaceIndex
_Fsipv6IfRaRDNSSIndex_Object=MibTableColumn
fsipv6IfRaRDNSSIndex=_Fsipv6IfRaRDNSSIndex_Object((1,3,6,1,4,1,2076,28,1,4,1,1,1),_Fsipv6IfRaRDNSSIndex_Type())
fsipv6IfRaRDNSSIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6IfRaRDNSSIndex.setStatus(_A)
class _Fsipv6IfRadvRDNSSOpen_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_Fsipv6IfRadvRDNSSOpen_Type.__name__=_D
_Fsipv6IfRadvRDNSSOpen_Object=MibTableColumn
fsipv6IfRadvRDNSSOpen=_Fsipv6IfRadvRDNSSOpen_Object((1,3,6,1,4,1,2076,28,1,4,1,1,2),_Fsipv6IfRadvRDNSSOpen_Type())
fsipv6IfRadvRDNSSOpen.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfRadvRDNSSOpen.setStatus(_A)
class _Fsipv6IfRaRDNSSPreference_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Fsipv6IfRaRDNSSPreference_Type.__name__=_D
_Fsipv6IfRaRDNSSPreference_Object=MibTableColumn
fsipv6IfRaRDNSSPreference=_Fsipv6IfRaRDNSSPreference_Object((1,3,6,1,4,1,2076,28,1,4,1,1,3),_Fsipv6IfRaRDNSSPreference_Type())
fsipv6IfRaRDNSSPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfRaRDNSSPreference.setStatus(_A)
class _Fsipv6IfRaRDNSSLifetime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Fsipv6IfRaRDNSSLifetime_Type.__name__=_H
_Fsipv6IfRaRDNSSLifetime_Object=MibTableColumn
fsipv6IfRaRDNSSLifetime=_Fsipv6IfRaRDNSSLifetime_Object((1,3,6,1,4,1,2076,28,1,4,1,1,4),_Fsipv6IfRaRDNSSLifetime_Type())
fsipv6IfRaRDNSSLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfRaRDNSSLifetime.setStatus(_A)
_Fsipv6IfRaRDNSSAddrOne_Type=Ipv6Address
_Fsipv6IfRaRDNSSAddrOne_Object=MibTableColumn
fsipv6IfRaRDNSSAddrOne=_Fsipv6IfRaRDNSSAddrOne_Object((1,3,6,1,4,1,2076,28,1,4,1,1,5),_Fsipv6IfRaRDNSSAddrOne_Type())
fsipv6IfRaRDNSSAddrOne.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfRaRDNSSAddrOne.setStatus(_A)
_Fsipv6IfRaRDNSSAddrTwo_Type=Ipv6Address
_Fsipv6IfRaRDNSSAddrTwo_Object=MibTableColumn
fsipv6IfRaRDNSSAddrTwo=_Fsipv6IfRaRDNSSAddrTwo_Object((1,3,6,1,4,1,2076,28,1,4,1,1,6),_Fsipv6IfRaRDNSSAddrTwo_Type())
fsipv6IfRaRDNSSAddrTwo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfRaRDNSSAddrTwo.setStatus(_A)
_Fsipv6IfRaRDNSSAddrThree_Type=Ipv6Address
_Fsipv6IfRaRDNSSAddrThree_Object=MibTableColumn
fsipv6IfRaRDNSSAddrThree=_Fsipv6IfRaRDNSSAddrThree_Object((1,3,6,1,4,1,2076,28,1,4,1,1,7),_Fsipv6IfRaRDNSSAddrThree_Type())
fsipv6IfRaRDNSSAddrThree.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfRaRDNSSAddrThree.setStatus(_A)
_Fsipv6IfRaRDNSSRowStatus_Type=RowStatus
_Fsipv6IfRaRDNSSRowStatus_Object=MibTableColumn
fsipv6IfRaRDNSSRowStatus=_Fsipv6IfRaRDNSSRowStatus_Object((1,3,6,1,4,1,2076,28,1,4,1,1,8),_Fsipv6IfRaRDNSSRowStatus_Type())
fsipv6IfRaRDNSSRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfRaRDNSSRowStatus.setStatus(_A)
class _Fsipv6IfDomainNameOne_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_Fsipv6IfDomainNameOne_Type.__name__=_G
_Fsipv6IfDomainNameOne_Object=MibTableColumn
fsipv6IfDomainNameOne=_Fsipv6IfDomainNameOne_Object((1,3,6,1,4,1,2076,28,1,4,1,1,9),_Fsipv6IfDomainNameOne_Type())
fsipv6IfDomainNameOne.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfDomainNameOne.setStatus(_A)
class _Fsipv6IfDomainNameTwo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_Fsipv6IfDomainNameTwo_Type.__name__=_G
_Fsipv6IfDomainNameTwo_Object=MibTableColumn
fsipv6IfDomainNameTwo=_Fsipv6IfDomainNameTwo_Object((1,3,6,1,4,1,2076,28,1,4,1,1,10),_Fsipv6IfDomainNameTwo_Type())
fsipv6IfDomainNameTwo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfDomainNameTwo.setStatus(_A)
class _Fsipv6IfDomainNameThree_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_Fsipv6IfDomainNameThree_Type.__name__=_G
_Fsipv6IfDomainNameThree_Object=MibTableColumn
fsipv6IfDomainNameThree=_Fsipv6IfDomainNameThree_Object((1,3,6,1,4,1,2076,28,1,4,1,1,11),_Fsipv6IfDomainNameThree_Type())
fsipv6IfDomainNameThree.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfDomainNameThree.setStatus(_A)
class _Fsipv6IfDnsLifeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_Fsipv6IfDnsLifeTime_Type.__name__=_D
_Fsipv6IfDnsLifeTime_Object=MibTableColumn
fsipv6IfDnsLifeTime=_Fsipv6IfDnsLifeTime_Object((1,3,6,1,4,1,2076,28,1,4,1,1,12),_Fsipv6IfDnsLifeTime_Type())
fsipv6IfDnsLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfDnsLifeTime.setStatus(_A)
class _Fsipv6IfRaRDNSSAddrOneLife_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Fsipv6IfRaRDNSSAddrOneLife_Type.__name__=_H
_Fsipv6IfRaRDNSSAddrOneLife_Object=MibTableColumn
fsipv6IfRaRDNSSAddrOneLife=_Fsipv6IfRaRDNSSAddrOneLife_Object((1,3,6,1,4,1,2076,28,1,4,1,1,13),_Fsipv6IfRaRDNSSAddrOneLife_Type())
fsipv6IfRaRDNSSAddrOneLife.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfRaRDNSSAddrOneLife.setStatus(_A)
class _Fsipv6IfRaRDNSSAddrTwoLife_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Fsipv6IfRaRDNSSAddrTwoLife_Type.__name__=_H
_Fsipv6IfRaRDNSSAddrTwoLife_Object=MibTableColumn
fsipv6IfRaRDNSSAddrTwoLife=_Fsipv6IfRaRDNSSAddrTwoLife_Object((1,3,6,1,4,1,2076,28,1,4,1,1,14),_Fsipv6IfRaRDNSSAddrTwoLife_Type())
fsipv6IfRaRDNSSAddrTwoLife.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfRaRDNSSAddrTwoLife.setStatus(_A)
class _Fsipv6IfRaRDNSSAddrThreeLife_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Fsipv6IfRaRDNSSAddrThreeLife_Type.__name__=_H
_Fsipv6IfRaRDNSSAddrThreeLife_Object=MibTableColumn
fsipv6IfRaRDNSSAddrThreeLife=_Fsipv6IfRaRDNSSAddrThreeLife_Object((1,3,6,1,4,1,2076,28,1,4,1,1,15),_Fsipv6IfRaRDNSSAddrThreeLife_Type())
fsipv6IfRaRDNSSAddrThreeLife.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfRaRDNSSAddrThreeLife.setStatus(_A)
class _Fsipv6IfDomainNameOneLife_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Fsipv6IfDomainNameOneLife_Type.__name__=_H
_Fsipv6IfDomainNameOneLife_Object=MibTableColumn
fsipv6IfDomainNameOneLife=_Fsipv6IfDomainNameOneLife_Object((1,3,6,1,4,1,2076,28,1,4,1,1,16),_Fsipv6IfDomainNameOneLife_Type())
fsipv6IfDomainNameOneLife.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfDomainNameOneLife.setStatus(_A)
class _Fsipv6IfDomainNameTwoLife_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Fsipv6IfDomainNameTwoLife_Type.__name__=_H
_Fsipv6IfDomainNameTwoLife_Object=MibTableColumn
fsipv6IfDomainNameTwoLife=_Fsipv6IfDomainNameTwoLife_Object((1,3,6,1,4,1,2076,28,1,4,1,1,17),_Fsipv6IfDomainNameTwoLife_Type())
fsipv6IfDomainNameTwoLife.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfDomainNameTwoLife.setStatus(_A)
class _Fsipv6IfDomainNameThreeLife_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Fsipv6IfDomainNameThreeLife_Type.__name__=_H
_Fsipv6IfDomainNameThreeLife_Object=MibTableColumn
fsipv6IfDomainNameThreeLife=_Fsipv6IfDomainNameThreeLife_Object((1,3,6,1,4,1,2076,28,1,4,1,1,18),_Fsipv6IfDomainNameThreeLife_Type())
fsipv6IfDomainNameThreeLife.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6IfDomainNameThreeLife.setStatus(_A)
_Fsipv6Icmp_ObjectIdentity=ObjectIdentity
fsipv6Icmp=_Fsipv6Icmp_ObjectIdentity((1,3,6,1,4,1,2076,28,2))
_Fsipv6IcmpInMsgs_Type=Counter32
_Fsipv6IcmpInMsgs_Object=MibScalar
fsipv6IcmpInMsgs=_Fsipv6IcmpInMsgs_Object((1,3,6,1,4,1,2076,28,2,1),_Fsipv6IcmpInMsgs_Type())
fsipv6IcmpInMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInMsgs.setStatus(_A)
_Fsipv6IcmpInErrors_Type=Counter32
_Fsipv6IcmpInErrors_Object=MibScalar
fsipv6IcmpInErrors=_Fsipv6IcmpInErrors_Object((1,3,6,1,4,1,2076,28,2,2),_Fsipv6IcmpInErrors_Type())
fsipv6IcmpInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInErrors.setStatus(_A)
_Fsipv6IcmpInDestUnreachs_Type=Counter32
_Fsipv6IcmpInDestUnreachs_Object=MibScalar
fsipv6IcmpInDestUnreachs=_Fsipv6IcmpInDestUnreachs_Object((1,3,6,1,4,1,2076,28,2,3),_Fsipv6IcmpInDestUnreachs_Type())
fsipv6IcmpInDestUnreachs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInDestUnreachs.setStatus(_A)
_Fsipv6IcmpInTimeExcds_Type=Counter32
_Fsipv6IcmpInTimeExcds_Object=MibScalar
fsipv6IcmpInTimeExcds=_Fsipv6IcmpInTimeExcds_Object((1,3,6,1,4,1,2076,28,2,4),_Fsipv6IcmpInTimeExcds_Type())
fsipv6IcmpInTimeExcds.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInTimeExcds.setStatus(_A)
_Fsipv6IcmpInParmProbs_Type=Counter32
_Fsipv6IcmpInParmProbs_Object=MibScalar
fsipv6IcmpInParmProbs=_Fsipv6IcmpInParmProbs_Object((1,3,6,1,4,1,2076,28,2,5),_Fsipv6IcmpInParmProbs_Type())
fsipv6IcmpInParmProbs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInParmProbs.setStatus(_A)
_Fsipv6IcmpInPktTooBigs_Type=Counter32
_Fsipv6IcmpInPktTooBigs_Object=MibScalar
fsipv6IcmpInPktTooBigs=_Fsipv6IcmpInPktTooBigs_Object((1,3,6,1,4,1,2076,28,2,6),_Fsipv6IcmpInPktTooBigs_Type())
fsipv6IcmpInPktTooBigs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInPktTooBigs.setStatus(_A)
_Fsipv6IcmpInEchos_Type=Counter32
_Fsipv6IcmpInEchos_Object=MibScalar
fsipv6IcmpInEchos=_Fsipv6IcmpInEchos_Object((1,3,6,1,4,1,2076,28,2,7),_Fsipv6IcmpInEchos_Type())
fsipv6IcmpInEchos.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInEchos.setStatus(_A)
_Fsipv6IcmpInEchoReps_Type=Counter32
_Fsipv6IcmpInEchoReps_Object=MibScalar
fsipv6IcmpInEchoReps=_Fsipv6IcmpInEchoReps_Object((1,3,6,1,4,1,2076,28,2,8),_Fsipv6IcmpInEchoReps_Type())
fsipv6IcmpInEchoReps.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInEchoReps.setStatus(_A)
_Fsipv6IcmpInRouterSolicits_Type=Counter32
_Fsipv6IcmpInRouterSolicits_Object=MibScalar
fsipv6IcmpInRouterSolicits=_Fsipv6IcmpInRouterSolicits_Object((1,3,6,1,4,1,2076,28,2,9),_Fsipv6IcmpInRouterSolicits_Type())
fsipv6IcmpInRouterSolicits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInRouterSolicits.setStatus(_A)
_Fsipv6IcmpInRouterAdvertisements_Type=Counter32
_Fsipv6IcmpInRouterAdvertisements_Object=MibScalar
fsipv6IcmpInRouterAdvertisements=_Fsipv6IcmpInRouterAdvertisements_Object((1,3,6,1,4,1,2076,28,2,10),_Fsipv6IcmpInRouterAdvertisements_Type())
fsipv6IcmpInRouterAdvertisements.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInRouterAdvertisements.setStatus(_A)
_Fsipv6IcmpInNeighborSolicits_Type=Counter32
_Fsipv6IcmpInNeighborSolicits_Object=MibScalar
fsipv6IcmpInNeighborSolicits=_Fsipv6IcmpInNeighborSolicits_Object((1,3,6,1,4,1,2076,28,2,11),_Fsipv6IcmpInNeighborSolicits_Type())
fsipv6IcmpInNeighborSolicits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInNeighborSolicits.setStatus(_A)
_Fsipv6IcmpInNeighborAdvertisements_Type=Counter32
_Fsipv6IcmpInNeighborAdvertisements_Object=MibScalar
fsipv6IcmpInNeighborAdvertisements=_Fsipv6IcmpInNeighborAdvertisements_Object((1,3,6,1,4,1,2076,28,2,12),_Fsipv6IcmpInNeighborAdvertisements_Type())
fsipv6IcmpInNeighborAdvertisements.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInNeighborAdvertisements.setStatus(_A)
_Fsipv6IcmpInRedirects_Type=Counter32
_Fsipv6IcmpInRedirects_Object=MibScalar
fsipv6IcmpInRedirects=_Fsipv6IcmpInRedirects_Object((1,3,6,1,4,1,2076,28,2,13),_Fsipv6IcmpInRedirects_Type())
fsipv6IcmpInRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInRedirects.setStatus(_A)
_Fsipv6IcmpInAdminProhib_Type=Counter32
_Fsipv6IcmpInAdminProhib_Object=MibScalar
fsipv6IcmpInAdminProhib=_Fsipv6IcmpInAdminProhib_Object((1,3,6,1,4,1,2076,28,2,14),_Fsipv6IcmpInAdminProhib_Type())
fsipv6IcmpInAdminProhib.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInAdminProhib.setStatus(_A)
_Fsipv6IcmpOutMsgs_Type=Counter32
_Fsipv6IcmpOutMsgs_Object=MibScalar
fsipv6IcmpOutMsgs=_Fsipv6IcmpOutMsgs_Object((1,3,6,1,4,1,2076,28,2,15),_Fsipv6IcmpOutMsgs_Type())
fsipv6IcmpOutMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutMsgs.setStatus(_A)
_Fsipv6IcmpOutErrors_Type=Counter32
_Fsipv6IcmpOutErrors_Object=MibScalar
fsipv6IcmpOutErrors=_Fsipv6IcmpOutErrors_Object((1,3,6,1,4,1,2076,28,2,16),_Fsipv6IcmpOutErrors_Type())
fsipv6IcmpOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutErrors.setStatus(_A)
_Fsipv6IcmpOutDestUnreachs_Type=Counter32
_Fsipv6IcmpOutDestUnreachs_Object=MibScalar
fsipv6IcmpOutDestUnreachs=_Fsipv6IcmpOutDestUnreachs_Object((1,3,6,1,4,1,2076,28,2,17),_Fsipv6IcmpOutDestUnreachs_Type())
fsipv6IcmpOutDestUnreachs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutDestUnreachs.setStatus(_A)
_Fsipv6IcmpOutTimeExcds_Type=Counter32
_Fsipv6IcmpOutTimeExcds_Object=MibScalar
fsipv6IcmpOutTimeExcds=_Fsipv6IcmpOutTimeExcds_Object((1,3,6,1,4,1,2076,28,2,18),_Fsipv6IcmpOutTimeExcds_Type())
fsipv6IcmpOutTimeExcds.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutTimeExcds.setStatus(_A)
_Fsipv6IcmpOutParmProbs_Type=Counter32
_Fsipv6IcmpOutParmProbs_Object=MibScalar
fsipv6IcmpOutParmProbs=_Fsipv6IcmpOutParmProbs_Object((1,3,6,1,4,1,2076,28,2,19),_Fsipv6IcmpOutParmProbs_Type())
fsipv6IcmpOutParmProbs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutParmProbs.setStatus(_A)
_Fsipv6IcmpOutPktTooBigs_Type=Counter32
_Fsipv6IcmpOutPktTooBigs_Object=MibScalar
fsipv6IcmpOutPktTooBigs=_Fsipv6IcmpOutPktTooBigs_Object((1,3,6,1,4,1,2076,28,2,20),_Fsipv6IcmpOutPktTooBigs_Type())
fsipv6IcmpOutPktTooBigs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutPktTooBigs.setStatus(_A)
_Fsipv6IcmpOutEchos_Type=Counter32
_Fsipv6IcmpOutEchos_Object=MibScalar
fsipv6IcmpOutEchos=_Fsipv6IcmpOutEchos_Object((1,3,6,1,4,1,2076,28,2,21),_Fsipv6IcmpOutEchos_Type())
fsipv6IcmpOutEchos.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutEchos.setStatus(_A)
_Fsipv6IcmpOutEchoReps_Type=Counter32
_Fsipv6IcmpOutEchoReps_Object=MibScalar
fsipv6IcmpOutEchoReps=_Fsipv6IcmpOutEchoReps_Object((1,3,6,1,4,1,2076,28,2,22),_Fsipv6IcmpOutEchoReps_Type())
fsipv6IcmpOutEchoReps.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutEchoReps.setStatus(_A)
_Fsipv6IcmpOutRouterSolicits_Type=Counter32
_Fsipv6IcmpOutRouterSolicits_Object=MibScalar
fsipv6IcmpOutRouterSolicits=_Fsipv6IcmpOutRouterSolicits_Object((1,3,6,1,4,1,2076,28,2,23),_Fsipv6IcmpOutRouterSolicits_Type())
fsipv6IcmpOutRouterSolicits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutRouterSolicits.setStatus(_A)
_Fsipv6IcmpOutRouterAdvertisements_Type=Counter32
_Fsipv6IcmpOutRouterAdvertisements_Object=MibScalar
fsipv6IcmpOutRouterAdvertisements=_Fsipv6IcmpOutRouterAdvertisements_Object((1,3,6,1,4,1,2076,28,2,24),_Fsipv6IcmpOutRouterAdvertisements_Type())
fsipv6IcmpOutRouterAdvertisements.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutRouterAdvertisements.setStatus(_A)
_Fsipv6IcmpOutNeighborSolicits_Type=Counter32
_Fsipv6IcmpOutNeighborSolicits_Object=MibScalar
fsipv6IcmpOutNeighborSolicits=_Fsipv6IcmpOutNeighborSolicits_Object((1,3,6,1,4,1,2076,28,2,25),_Fsipv6IcmpOutNeighborSolicits_Type())
fsipv6IcmpOutNeighborSolicits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutNeighborSolicits.setStatus(_A)
_Fsipv6IcmpOutNeighborAdvertisements_Type=Counter32
_Fsipv6IcmpOutNeighborAdvertisements_Object=MibScalar
fsipv6IcmpOutNeighborAdvertisements=_Fsipv6IcmpOutNeighborAdvertisements_Object((1,3,6,1,4,1,2076,28,2,26),_Fsipv6IcmpOutNeighborAdvertisements_Type())
fsipv6IcmpOutNeighborAdvertisements.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutNeighborAdvertisements.setStatus(_A)
_Fsipv6IcmpOutRedirects_Type=Counter32
_Fsipv6IcmpOutRedirects_Object=MibScalar
fsipv6IcmpOutRedirects=_Fsipv6IcmpOutRedirects_Object((1,3,6,1,4,1,2076,28,2,27),_Fsipv6IcmpOutRedirects_Type())
fsipv6IcmpOutRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutRedirects.setStatus(_A)
_Fsipv6IcmpOutAdminProhib_Type=Counter32
_Fsipv6IcmpOutAdminProhib_Object=MibScalar
fsipv6IcmpOutAdminProhib=_Fsipv6IcmpOutAdminProhib_Object((1,3,6,1,4,1,2076,28,2,28),_Fsipv6IcmpOutAdminProhib_Type())
fsipv6IcmpOutAdminProhib.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutAdminProhib.setStatus(_A)
_Fsipv6IcmpInBadCode_Type=Counter32
_Fsipv6IcmpInBadCode_Object=MibScalar
fsipv6IcmpInBadCode=_Fsipv6IcmpInBadCode_Object((1,3,6,1,4,1,2076,28,2,29),_Fsipv6IcmpInBadCode_Type())
fsipv6IcmpInBadCode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInBadCode.setStatus(_A)
_Fsipv6IcmpInNARouterFlagSet_Type=Counter32
_Fsipv6IcmpInNARouterFlagSet_Object=MibScalar
fsipv6IcmpInNARouterFlagSet=_Fsipv6IcmpInNARouterFlagSet_Object((1,3,6,1,4,1,2076,28,2,30),_Fsipv6IcmpInNARouterFlagSet_Type())
fsipv6IcmpInNARouterFlagSet.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInNARouterFlagSet.setStatus(_A)
_Fsipv6IcmpInNASolicitedFlagSet_Type=Counter32
_Fsipv6IcmpInNASolicitedFlagSet_Object=MibScalar
fsipv6IcmpInNASolicitedFlagSet=_Fsipv6IcmpInNASolicitedFlagSet_Object((1,3,6,1,4,1,2076,28,2,31),_Fsipv6IcmpInNASolicitedFlagSet_Type())
fsipv6IcmpInNASolicitedFlagSet.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInNASolicitedFlagSet.setStatus(_A)
_Fsipv6IcmpInNAOverrideFlagSet_Type=Counter32
_Fsipv6IcmpInNAOverrideFlagSet_Object=MibScalar
fsipv6IcmpInNAOverrideFlagSet=_Fsipv6IcmpInNAOverrideFlagSet_Object((1,3,6,1,4,1,2076,28,2,32),_Fsipv6IcmpInNAOverrideFlagSet_Type())
fsipv6IcmpInNAOverrideFlagSet.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpInNAOverrideFlagSet.setStatus(_A)
_Fsipv6IcmpOutNARouterFlagSet_Type=Counter32
_Fsipv6IcmpOutNARouterFlagSet_Object=MibScalar
fsipv6IcmpOutNARouterFlagSet=_Fsipv6IcmpOutNARouterFlagSet_Object((1,3,6,1,4,1,2076,28,2,33),_Fsipv6IcmpOutNARouterFlagSet_Type())
fsipv6IcmpOutNARouterFlagSet.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutNARouterFlagSet.setStatus(_A)
_Fsipv6IcmpOutNASolicitedFlagSet_Type=Counter32
_Fsipv6IcmpOutNASolicitedFlagSet_Object=MibScalar
fsipv6IcmpOutNASolicitedFlagSet=_Fsipv6IcmpOutNASolicitedFlagSet_Object((1,3,6,1,4,1,2076,28,2,34),_Fsipv6IcmpOutNASolicitedFlagSet_Type())
fsipv6IcmpOutNASolicitedFlagSet.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutNASolicitedFlagSet.setStatus(_A)
_Fsipv6IcmpOutNAOverrideFlagSet_Type=Counter32
_Fsipv6IcmpOutNAOverrideFlagSet_Object=MibScalar
fsipv6IcmpOutNAOverrideFlagSet=_Fsipv6IcmpOutNAOverrideFlagSet_Object((1,3,6,1,4,1,2076,28,2,35),_Fsipv6IcmpOutNAOverrideFlagSet_Type())
fsipv6IcmpOutNAOverrideFlagSet.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6IcmpOutNAOverrideFlagSet.setStatus(_A)
_Fsipv6Udp_ObjectIdentity=ObjectIdentity
fsipv6Udp=_Fsipv6Udp_ObjectIdentity((1,3,6,1,4,1,2076,28,3))
_Fsipv6UdpScalars_ObjectIdentity=ObjectIdentity
fsipv6UdpScalars=_Fsipv6UdpScalars_ObjectIdentity((1,3,6,1,4,1,2076,28,3,1))
_Fsipv6UdpInDatagrams_Type=Counter32
_Fsipv6UdpInDatagrams_Object=MibScalar
fsipv6UdpInDatagrams=_Fsipv6UdpInDatagrams_Object((1,3,6,1,4,1,2076,28,3,1,1),_Fsipv6UdpInDatagrams_Type())
fsipv6UdpInDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6UdpInDatagrams.setStatus(_A)
_Fsipv6UdpNoPorts_Type=Counter32
_Fsipv6UdpNoPorts_Object=MibScalar
fsipv6UdpNoPorts=_Fsipv6UdpNoPorts_Object((1,3,6,1,4,1,2076,28,3,1,2),_Fsipv6UdpNoPorts_Type())
fsipv6UdpNoPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6UdpNoPorts.setStatus(_A)
_Fsipv6UdpInErrors_Type=Counter32
_Fsipv6UdpInErrors_Object=MibScalar
fsipv6UdpInErrors=_Fsipv6UdpInErrors_Object((1,3,6,1,4,1,2076,28,3,1,3),_Fsipv6UdpInErrors_Type())
fsipv6UdpInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6UdpInErrors.setStatus(_A)
_Fsipv6UdpOutDatagrams_Type=Counter32
_Fsipv6UdpOutDatagrams_Object=MibScalar
fsipv6UdpOutDatagrams=_Fsipv6UdpOutDatagrams_Object((1,3,6,1,4,1,2076,28,3,1,4),_Fsipv6UdpOutDatagrams_Type())
fsipv6UdpOutDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6UdpOutDatagrams.setStatus(_A)
_Fsipv6Tunnel_ObjectIdentity=ObjectIdentity
fsipv6Tunnel=_Fsipv6Tunnel_ObjectIdentity((1,3,6,1,4,1,2076,28,5))
_Fsipv6Route_ObjectIdentity=ObjectIdentity
fsipv6Route=_Fsipv6Route_ObjectIdentity((1,3,6,1,4,1,2076,28,6))
_Fsipv6RouteTable_Object=MibTable
fsipv6RouteTable=_Fsipv6RouteTable_Object((1,3,6,1,4,1,2076,28,6,1))
if mibBuilder.loadTexts:fsipv6RouteTable.setStatus(_A)
_Fsipv6RouteEntry_Object=MibTableRow
fsipv6RouteEntry=_Fsipv6RouteEntry_Object((1,3,6,1,4,1,2076,28,6,1,1))
fsipv6RouteEntry.setIndexNames((0,_E,_AA),(0,_E,_AB),(0,_E,_AC),(0,_E,_AD))
if mibBuilder.loadTexts:fsipv6RouteEntry.setStatus(_A)
class _Fsipv6RouteDest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Fsipv6RouteDest_Type.__name__=_G
_Fsipv6RouteDest_Object=MibTableColumn
fsipv6RouteDest=_Fsipv6RouteDest_Object((1,3,6,1,4,1,2076,28,6,1,1,1),_Fsipv6RouteDest_Type())
fsipv6RouteDest.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6RouteDest.setStatus(_A)
class _Fsipv6RoutePfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Fsipv6RoutePfxLength_Type.__name__=_D
_Fsipv6RoutePfxLength_Object=MibTableColumn
fsipv6RoutePfxLength=_Fsipv6RoutePfxLength_Object((1,3,6,1,4,1,2076,28,6,1,1,2),_Fsipv6RoutePfxLength_Type())
fsipv6RoutePfxLength.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6RoutePfxLength.setStatus(_A)
class _Fsipv6RouteProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_W,1),(_R,2),('netmgmt',3),('ndisc',4),('rip',5),('ospf',6),('bgp',7),('idrp',8),('igrp',9)))
_Fsipv6RouteProtocol_Type.__name__=_D
_Fsipv6RouteProtocol_Object=MibTableColumn
fsipv6RouteProtocol=_Fsipv6RouteProtocol_Object((1,3,6,1,4,1,2076,28,6,1,1,3),_Fsipv6RouteProtocol_Type())
fsipv6RouteProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6RouteProtocol.setStatus(_A)
class _Fsipv6RouteNextHop_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Fsipv6RouteNextHop_Type.__name__=_G
_Fsipv6RouteNextHop_Object=MibTableColumn
fsipv6RouteNextHop=_Fsipv6RouteNextHop_Object((1,3,6,1,4,1,2076,28,6,1,1,4),_Fsipv6RouteNextHop_Type())
fsipv6RouteNextHop.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6RouteNextHop.setStatus(_A)
_Fsipv6RouteIfIndex_Type=InterfaceIndex
_Fsipv6RouteIfIndex_Object=MibTableColumn
fsipv6RouteIfIndex=_Fsipv6RouteIfIndex_Object((1,3,6,1,4,1,2076,28,6,1,1,5),_Fsipv6RouteIfIndex_Type())
fsipv6RouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6RouteIfIndex.setStatus(_A)
class _Fsipv6RouteMetric_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Fsipv6RouteMetric_Type.__name__=_H
_Fsipv6RouteMetric_Object=MibTableColumn
fsipv6RouteMetric=_Fsipv6RouteMetric_Object((1,3,6,1,4,1,2076,28,6,1,1,6),_Fsipv6RouteMetric_Type())
fsipv6RouteMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6RouteMetric.setStatus(_A)
class _Fsipv6RouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),('discard',2),(_R,3),('remote',4)))
_Fsipv6RouteType_Type.__name__=_D
_Fsipv6RouteType_Object=MibTableColumn
fsipv6RouteType=_Fsipv6RouteType_Object((1,3,6,1,4,1,2076,28,6,1,1,7),_Fsipv6RouteType_Type())
fsipv6RouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6RouteType.setStatus(_A)
class _Fsipv6RouteTag_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Fsipv6RouteTag_Type.__name__=_H
_Fsipv6RouteTag_Object=MibTableColumn
fsipv6RouteTag=_Fsipv6RouteTag_Object((1,3,6,1,4,1,2076,28,6,1,1,8),_Fsipv6RouteTag_Type())
fsipv6RouteTag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6RouteTag.setStatus(_A)
_Fsipv6RouteAge_Type=Integer32
_Fsipv6RouteAge_Object=MibTableColumn
fsipv6RouteAge=_Fsipv6RouteAge_Object((1,3,6,1,4,1,2076,28,6,1,1,9),_Fsipv6RouteAge_Type())
fsipv6RouteAge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6RouteAge.setStatus(_A)
_Fsipv6RouteAdminStatus_Type=RowStatus
_Fsipv6RouteAdminStatus_Object=MibTableColumn
fsipv6RouteAdminStatus=_Fsipv6RouteAdminStatus_Object((1,3,6,1,4,1,2076,28,6,1,1,10),_Fsipv6RouteAdminStatus_Type())
fsipv6RouteAdminStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:fsipv6RouteAdminStatus.setStatus(_A)
class _Fsipv6RouteAddrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_S,2)))
_Fsipv6RouteAddrType_Type.__name__=_D
_Fsipv6RouteAddrType_Object=MibTableColumn
fsipv6RouteAddrType=_Fsipv6RouteAddrType_Object((1,3,6,1,4,1,2076,28,6,1,1,11),_Fsipv6RouteAddrType_Type())
fsipv6RouteAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6RouteAddrType.setStatus(_A)
class _Fsipv6RouteHwStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('present',1),('not-present',2)))
_Fsipv6RouteHwStatus_Type.__name__=_D
_Fsipv6RouteHwStatus_Object=MibTableColumn
fsipv6RouteHwStatus=_Fsipv6RouteHwStatus_Object((1,3,6,1,4,1,2076,28,6,1,1,12),_Fsipv6RouteHwStatus_Type())
fsipv6RouteHwStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsipv6RouteHwStatus.setStatus(_A)
class _Fsipv6RoutePreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Fsipv6RoutePreference_Type.__name__=_D
_Fsipv6RoutePreference_Object=MibTableColumn
fsipv6RoutePreference=_Fsipv6RoutePreference_Object((1,3,6,1,4,1,2076,28,6,1,1,13),_Fsipv6RoutePreference_Type())
fsipv6RoutePreference.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6RoutePreference.setStatus(_A)
_Fsipv6PrefTable_Object=MibTable
fsipv6PrefTable=_Fsipv6PrefTable_Object((1,3,6,1,4,1,2076,28,6,2))
if mibBuilder.loadTexts:fsipv6PrefTable.setStatus(_A)
_Fsipv6PrefEntry_Object=MibTableRow
fsipv6PrefEntry=_Fsipv6PrefEntry_Object((1,3,6,1,4,1,2076,28,6,2,1))
fsipv6PrefEntry.setIndexNames((0,_E,_AE))
if mibBuilder.loadTexts:fsipv6PrefEntry.setStatus(_A)
class _Fsipv6Protocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_W,1),(_R,2),('netmgmt',3),('ndisc',4),('rip',5),('ospf',6),('bgp',7),('idrp',8),('igrp',9)))
_Fsipv6Protocol_Type.__name__=_D
_Fsipv6Protocol_Object=MibTableColumn
fsipv6Protocol=_Fsipv6Protocol_Object((1,3,6,1,4,1,2076,28,6,2,1,1),_Fsipv6Protocol_Type())
fsipv6Protocol.setMaxAccess(_F)
if mibBuilder.loadTexts:fsipv6Protocol.setStatus(_A)
class _Fsipv6Preference_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Fsipv6Preference_Type.__name__=_H
_Fsipv6Preference_Object=MibTableColumn
fsipv6Preference=_Fsipv6Preference_Object((1,3,6,1,4,1,2076,28,6,2,1,2),_Fsipv6Preference_Type())
fsipv6Preference.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipv6Preference.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'InterfaceList':InterfaceList,'Ipv6Address':Ipv6Address,'futureipv6':futureipv6,'fsipv6':fsipv6,'fsipv6Scalars':fsipv6Scalars,'fsipv6NdCacheMaxRetries':fsipv6NdCacheMaxRetries,'fsipv6PmtuConfigStatus':fsipv6PmtuConfigStatus,'fsipv6PmtuTimeOutInterval':fsipv6PmtuTimeOutInterval,'fsipv6JumboEnable':fsipv6JumboEnable,'fsipv6NumOfSendJumbo':fsipv6NumOfSendJumbo,'fsipv6NumOfRecvJumbo':fsipv6NumOfRecvJumbo,'fsipv6ErrJumbo':fsipv6ErrJumbo,'fsipv6GlobalDebug':fsipv6GlobalDebug,'fsipv6MaxRouteEntries':fsipv6MaxRouteEntries,'fsipv6MaxLogicalIfaces':fsipv6MaxLogicalIfaces,'fsipv6MaxTunnelIfaces':fsipv6MaxTunnelIfaces,'fsipv6MaxAddresses':fsipv6MaxAddresses,'fsipv6MaxFragReasmEntries':fsipv6MaxFragReasmEntries,'fsipv6Nd6MaxCacheEntries':fsipv6Nd6MaxCacheEntries,'fsipv6PmtuMaxDest':fsipv6PmtuMaxDest,'fsipv6RFC5095Compatibility':fsipv6RFC5095Compatibility,'fsipv6RFC5942Compatibility':fsipv6RFC5942Compatibility,'fsipv6SENDSecLevel':fsipv6SENDSecLevel,'fsipv6SENDNbrSecLevel':fsipv6SENDNbrSecLevel,'fsipv6SENDAuthType':fsipv6SENDAuthType,'fsipv6SENDMinBits':fsipv6SENDMinBits,'fsipv6SENDSecDAD':fsipv6SENDSecDAD,'fsipv6SENDPrefixChk':fsipv6SENDPrefixChk,'fsipv6ECMPPRTTimer':fsipv6ECMPPRTTimer,'fsipv6NdCacheTimeout':fsipv6NdCacheTimeout,'fsipv6Tables':fsipv6Tables,'fsipv6IfTable':fsipv6IfTable,'fsipv6IfEntry':fsipv6IfEntry,_M:fsipv6IfIndex,'fsipv6IfType':fsipv6IfType,'fsipv6IfPortNum':fsipv6IfPortNum,'fsipv6IfCircuitNum':fsipv6IfCircuitNum,'fsipv6IfToken':fsipv6IfToken,'fsipv6IfAdminStatus':fsipv6IfAdminStatus,'fsipv6IfOperStatus':fsipv6IfOperStatus,'fsipv6IfRouterAdvStatus':fsipv6IfRouterAdvStatus,'fsipv6IfRouterAdvFlags':fsipv6IfRouterAdvFlags,'fsipv6IfHopLimit':fsipv6IfHopLimit,'fsipv6IfDefRouterTime':fsipv6IfDefRouterTime,'fsipv6IfReachableTime':fsipv6IfReachableTime,'fsipv6IfRetransmitTime':fsipv6IfRetransmitTime,'fsipv6IfDelayProbeTime':fsipv6IfDelayProbeTime,'fsipv6IfPrefixAdvStatus':fsipv6IfPrefixAdvStatus,'fsipv6IfMinRouterAdvTime':fsipv6IfMinRouterAdvTime,'fsipv6IfMaxRouterAdvTime':fsipv6IfMaxRouterAdvTime,'fsipv6IfDADRetries':fsipv6IfDADRetries,'fsipv6IfForwarding':fsipv6IfForwarding,'fsipv6IfRoutingStatus':fsipv6IfRoutingStatus,'fsipv6IfIcmpErrInterval':fsipv6IfIcmpErrInterval,'fsipv6IfIcmpTokenBucketSize':fsipv6IfIcmpTokenBucketSize,'fsipv6IfDestUnreachableMsg':fsipv6IfDestUnreachableMsg,'fsipv6IfUnnumAssocIPIf':fsipv6IfUnnumAssocIPIf,'fsipv6IfRedirectMsg':fsipv6IfRedirectMsg,'fsipv6IfAdvSrcLLAdr':fsipv6IfAdvSrcLLAdr,'fsipv6IfAdvIntOpt':fsipv6IfAdvIntOpt,'fsipv6IfNDProxyAdminStatus':fsipv6IfNDProxyAdminStatus,'fsipv6IfNDProxyMode':fsipv6IfNDProxyMode,'fsipv6IfNDProxyOperStatus':fsipv6IfNDProxyOperStatus,'fsipv6IfNDProxyUpStream':fsipv6IfNDProxyUpStream,'fsipv6IfSENDSecStatus':fsipv6IfSENDSecStatus,'fsipv6IfSENDDeltaTimestamp':fsipv6IfSENDDeltaTimestamp,'fsipv6IfSENDFuzzTimestamp':fsipv6IfSENDFuzzTimestamp,'fsipv6IfSENDDriftTimestamp':fsipv6IfSENDDriftTimestamp,'fsipv6IfDefRoutePreference':fsipv6IfDefRoutePreference,'fsipv6IfStatsTable':fsipv6IfStatsTable,'fsipv6IfStatsEntry':fsipv6IfStatsEntry,_g:fsipv6IfStatsIndex,'fsipv6IfStatsInReceives':fsipv6IfStatsInReceives,'fsipv6IfStatsInHdrErrors':fsipv6IfStatsInHdrErrors,'fsipv6IfStatsTooBigErrors':fsipv6IfStatsTooBigErrors,'fsipv6IfStatsInAddrErrors':fsipv6IfStatsInAddrErrors,'fsipv6IfStatsForwDatagrams':fsipv6IfStatsForwDatagrams,'fsipv6IfStatsInUnknownProtos':fsipv6IfStatsInUnknownProtos,'fsipv6IfStatsInDiscards':fsipv6IfStatsInDiscards,'fsipv6IfStatsInDelivers':fsipv6IfStatsInDelivers,'fsipv6IfStatsOutRequests':fsipv6IfStatsOutRequests,'fsipv6IfStatsOutDiscards':fsipv6IfStatsOutDiscards,'fsipv6IfStatsOutNoRoutes':fsipv6IfStatsOutNoRoutes,'fsipv6IfStatsReasmReqds':fsipv6IfStatsReasmReqds,'fsipv6IfStatsReasmOKs':fsipv6IfStatsReasmOKs,'fsipv6IfStatsReasmFails':fsipv6IfStatsReasmFails,'fsipv6IfStatsFragOKs':fsipv6IfStatsFragOKs,'fsipv6IfStatsFragFails':fsipv6IfStatsFragFails,'fsipv6IfStatsFragCreates':fsipv6IfStatsFragCreates,'fsipv6IfStatsInMcastPkts':fsipv6IfStatsInMcastPkts,'fsipv6IfStatsOutMcastPkts':fsipv6IfStatsOutMcastPkts,'fsipv6IfStatsInTruncatedPkts':fsipv6IfStatsInTruncatedPkts,'fsipv6IfStatsInRouterSols':fsipv6IfStatsInRouterSols,'fsipv6IfStatsInRouterAdvs':fsipv6IfStatsInRouterAdvs,'fsipv6IfStatsInNeighSols':fsipv6IfStatsInNeighSols,'fsipv6IfStatsInNeighAdvs':fsipv6IfStatsInNeighAdvs,'fsipv6IfStatsInRedirects':fsipv6IfStatsInRedirects,'fsipv6IfStatsOutRouterSols':fsipv6IfStatsOutRouterSols,'fsipv6IfStatsOutRouterAdvs':fsipv6IfStatsOutRouterAdvs,'fsipv6IfStatsOutNeighSols':fsipv6IfStatsOutNeighSols,'fsipv6IfStatsOutNeighAdvs':fsipv6IfStatsOutNeighAdvs,'fsipv6IfStatsOutRedirects':fsipv6IfStatsOutRedirects,'fsipv6IfStatsLastRouterAdvTime':fsipv6IfStatsLastRouterAdvTime,'fsipv6IfStatsNextRouterAdvTime':fsipv6IfStatsNextRouterAdvTime,'fsipv6IfStatsIcmp6ErrRateLmtd':fsipv6IfStatsIcmp6ErrRateLmtd,'fsipv6IfStatsSENDDroppedPkts':fsipv6IfStatsSENDDroppedPkts,'fsipv6IfStatsSENDInvalidPkts':fsipv6IfStatsSENDInvalidPkts,'fsipv6PrefixTable':fsipv6PrefixTable,'fsipv6PrefixEntry':fsipv6PrefixEntry,_h:fsipv6PrefixIndex,_i:fsipv6PrefixAddress,_j:fsipv6PrefixAddrLen,'fsipv6PrefixProfileIndex':fsipv6PrefixProfileIndex,'fsipv6PrefixAdminStatus':fsipv6PrefixAdminStatus,'fsipv6SupportEmbeddedRp':fsipv6SupportEmbeddedRp,'fsipv6AddrTable':fsipv6AddrTable,'fsipv6AddrEntry':fsipv6AddrEntry,_k:fsipv6AddrIndex,_l:fsipv6AddrAddress,_m:fsipv6AddrPrefixLen,'fsipv6AddrAdminStatus':fsipv6AddrAdminStatus,'fsipv6AddrType':fsipv6AddrType,'fsipv6AddrProfIndex':fsipv6AddrProfIndex,'fsipv6AddrOperStatus':fsipv6AddrOperStatus,'fsipv6AddrScope':fsipv6AddrScope,'fsipv6AddrSENDCgaStatus':fsipv6AddrSENDCgaStatus,'fsipv6AddrSENDCgaModifier':fsipv6AddrSENDCgaModifier,'fsipv6AddrSENDCollisionCount':fsipv6AddrSENDCollisionCount,'fsipv6AddrProfileTable':fsipv6AddrProfileTable,'fsipv6AddrProfileEntry':fsipv6AddrProfileEntry,_n:fsipv6AddrProfileIndex,'fsipv6AddrProfileStatus':fsipv6AddrProfileStatus,'fsipv6AddrProfilePrefixAdvStatus':fsipv6AddrProfilePrefixAdvStatus,'fsipv6AddrProfileOnLinkAdvStatus':fsipv6AddrProfileOnLinkAdvStatus,'fsipv6AddrProfileAutoConfAdvStatus':fsipv6AddrProfileAutoConfAdvStatus,'fsipv6AddrProfilePreferredTime':fsipv6AddrProfilePreferredTime,'fsipv6AddrProfileValidTime':fsipv6AddrProfileValidTime,'fsipv6AddrProfileValidLifeTimeFlag':fsipv6AddrProfileValidLifeTimeFlag,'fsipv6AddrProfilePreferredLifeTimeFlag':fsipv6AddrProfilePreferredLifeTimeFlag,'fsipv6PmtuTable':fsipv6PmtuTable,'fsipv6PmtuEntry':fsipv6PmtuEntry,_p:fsipv6PmtuDest,'fsipv6Pmtu':fsipv6Pmtu,'fsipv6PmtuTimeStamp':fsipv6PmtuTimeStamp,'fsipv6PmtuAdminStatus':fsipv6PmtuAdminStatus,'fsipv6NdLanCacheTable':fsipv6NdLanCacheTable,'fsipv6NdLanCacheEntry':fsipv6NdLanCacheEntry,_q:fsipv6NdLanCacheIfIndex,_r:fsipv6NdLanCacheIPv6Addr,'fsipv6NdLanCacheStatus':fsipv6NdLanCacheStatus,'fsipv6NdLanCachePhysAddr':fsipv6NdLanCachePhysAddr,'fsipv6NdLanCacheState':fsipv6NdLanCacheState,'fsipv6NdLanCacheUseTime':fsipv6NdLanCacheUseTime,'fsipv6NdLanCacheIsSecure':fsipv6NdLanCacheIsSecure,'fsipv6NdWanCacheTable':fsipv6NdWanCacheTable,'fsipv6NdWanCacheEntry':fsipv6NdWanCacheEntry,_t:fsipv6NdWanCacheIfIndex,_u:fsipv6NdWanCacheIPv6Addr,'fsipv6NdWanCacheStatus':fsipv6NdWanCacheStatus,'fsipv6NdWanCacheState':fsipv6NdWanCacheState,'fsipv6NdWanCacheUseTime':fsipv6NdWanCacheUseTime,'fsipv6PingTable':fsipv6PingTable,'fsipv6PingEntry':fsipv6PingEntry,_v:fsipv6PingIndex,'fsipv6PingDest':fsipv6PingDest,'fsipv6PingIfIndex':fsipv6PingIfIndex,'fsipv6PingAdminStatus':fsipv6PingAdminStatus,'fsipv6PingInterval':fsipv6PingInterval,'fsipv6PingRcvTimeout':fsipv6PingRcvTimeout,'fsipv6PingTries':fsipv6PingTries,'fsipv6PingSize':fsipv6PingSize,'fsipv6PingSentCount':fsipv6PingSentCount,'fsipv6PingAverageTime':fsipv6PingAverageTime,'fsipv6PingMaxTime':fsipv6PingMaxTime,'fsipv6PingMinTime':fsipv6PingMinTime,'fsipv6PingOperStatus':fsipv6PingOperStatus,'fsipv6PingSuccesses':fsipv6PingSuccesses,'fsipv6PingPercentageLoss':fsipv6PingPercentageLoss,'fsipv6PingData':fsipv6PingData,'fsipv6PingSrcAddr':fsipv6PingSrcAddr,'fsipv6PingZoneId':fsipv6PingZoneId,'fsipv6PingDestAddrType':fsipv6PingDestAddrType,'fsipv6PingHostName':fsipv6PingHostName,'fsipv6NDProxyListTable':fsipv6NDProxyListTable,'fsipv6NDProxyListEntry':fsipv6NDProxyListEntry,_x:fsipv6NdProxyAddr,'fsipv6NdProxyAdminStatus':fsipv6NdProxyAdminStatus,'fsipv6AddrSelPolicyTable':fsipv6AddrSelPolicyTable,'fsipv6AddrSelPolicyEntry':fsipv6AddrSelPolicyEntry,_y:fsipv6AddrSelPolicyPrefix,_z:fsipv6AddrSelPolicyPrefixLen,_A0:fsipv6AddrSelPolicyIfIndex,'fsipv6AddrSelPolicyScope':fsipv6AddrSelPolicyScope,'fsipv6AddrSelPolicyPrecedence':fsipv6AddrSelPolicyPrecedence,'fsipv6AddrSelPolicyLabel':fsipv6AddrSelPolicyLabel,'fsipv6AddrSelPolicyAddrType':fsipv6AddrSelPolicyAddrType,'fsipv6AddrSelPolicyIsPublicAddr':fsipv6AddrSelPolicyIsPublicAddr,'fsipv6AddrSelPolicyIsSelfAddr':fsipv6AddrSelPolicyIsSelfAddr,'fsipv6AddrSelPolicyReachabilityStatus':fsipv6AddrSelPolicyReachabilityStatus,'fsipv6AddrSelPolicyConfigStatus':fsipv6AddrSelPolicyConfigStatus,'fsipv6AddrSelPolicyRowStatus':fsipv6AddrSelPolicyRowStatus,'fsipv6IfScopeZoneMapTable':fsipv6IfScopeZoneMapTable,'fsipv6IfScopeZoneMapEntry':fsipv6IfScopeZoneMapEntry,_A1:fsipv6ScopeZoneIndexIfIndex,'fsipv6ScopeZoneIndexInterfaceLocal':fsipv6ScopeZoneIndexInterfaceLocal,'fsipv6ScopeZoneIndexLinkLocal':fsipv6ScopeZoneIndexLinkLocal,'fsipv6ScopeZoneIndex3':fsipv6ScopeZoneIndex3,'fsipv6ScopeZoneIndexAdminLocal':fsipv6ScopeZoneIndexAdminLocal,'fsipv6ScopeZoneIndexSiteLocal':fsipv6ScopeZoneIndexSiteLocal,'fsipv6ScopeZoneIndex6':fsipv6ScopeZoneIndex6,'fsipv6ScopeZoneIndex7':fsipv6ScopeZoneIndex7,'fsipv6ScopeZoneIndexOrganizationLocal':fsipv6ScopeZoneIndexOrganizationLocal,'fsipv6ScopeZoneIndex9':fsipv6ScopeZoneIndex9,'fsipv6ScopeZoneIndexA':fsipv6ScopeZoneIndexA,'fsipv6ScopeZoneIndexB':fsipv6ScopeZoneIndexB,'fsipv6ScopeZoneIndexC':fsipv6ScopeZoneIndexC,'fsipv6ScopeZoneIndexD':fsipv6ScopeZoneIndexD,'fsipv6ScopeZoneIndexE':fsipv6ScopeZoneIndexE,'fsipv6IfScopeZoneCreationStatus':fsipv6IfScopeZoneCreationStatus,'fsipv6IfScopeZoneRowStatus':fsipv6IfScopeZoneRowStatus,'fsipv6ScopeZoneTable':fsipv6ScopeZoneTable,'fsipv6ScopeZoneEntry':fsipv6ScopeZoneEntry,_A3:fsipv6ScopeZoneName,'fsipv6ScopeZoneIndex':fsipv6ScopeZoneIndex,'fsipv6ScopeZoneCreationStatus':fsipv6ScopeZoneCreationStatus,'fsipv6ScopeZoneInterfaceList':fsipv6ScopeZoneInterfaceList,'fsipv6IsDefaultScopeZone':fsipv6IsDefaultScopeZone,'fsipv6SENDSentPktStatsTable':fsipv6SENDSentPktStatsTable,'fsipv6SENDSentPktStatsEntry':fsipv6SENDSentPktStatsEntry,_A4:fsipv6SENDSentPktType,'fsipv6SENDSentCgaOptPkts':fsipv6SENDSentCgaOptPkts,'fsipv6SENDSentCertOptPkts':fsipv6SENDSentCertOptPkts,'fsipv6SENDSentMtuOptPkts':fsipv6SENDSentMtuOptPkts,'fsipv6SENDSentNonceOptPkts':fsipv6SENDSentNonceOptPkts,'fsipv6SENDSentPrefixOptPkts':fsipv6SENDSentPrefixOptPkts,'fsipv6SENDSentRedirHdrPkts':fsipv6SENDSentRedirHdrPkts,'fsipv6SENDSentRsaOptPkts':fsipv6SENDSentRsaOptPkts,'fsipv6SENDSentSrcLinkAddrPkts':fsipv6SENDSentSrcLinkAddrPkts,'fsipv6SENDSentTgtLinkAddrPkts':fsipv6SENDSentTgtLinkAddrPkts,'fsipv6SENDSentTaOptPkts':fsipv6SENDSentTaOptPkts,'fsipv6SENDSentTimeStampOptPkts':fsipv6SENDSentTimeStampOptPkts,'fsipv6SENDRcvPktStatsTable':fsipv6SENDRcvPktStatsTable,'fsipv6SENDRcvPktStatsEntry':fsipv6SENDRcvPktStatsEntry,_A5:fsipv6SENDRcvPktType,'fsipv6SENDRcvCgaOptPkts':fsipv6SENDRcvCgaOptPkts,'fsipv6SENDRcvCertOptPkts':fsipv6SENDRcvCertOptPkts,'fsipv6SENDRcvMtuOptPkts':fsipv6SENDRcvMtuOptPkts,'fsipv6SENDRcvNonceOptPkts':fsipv6SENDRcvNonceOptPkts,'fsipv6SENDRcvPrefixOptPkts':fsipv6SENDRcvPrefixOptPkts,'fsipv6SENDRcvRedirHdrPkts':fsipv6SENDRcvRedirHdrPkts,'fsipv6SENDRcvRsaOptPkts':fsipv6SENDRcvRsaOptPkts,'fsipv6SENDRcvSrcLinkAddrPkts':fsipv6SENDRcvSrcLinkAddrPkts,'fsipv6SENDRcvTgtLinkAddrPkts':fsipv6SENDRcvTgtLinkAddrPkts,'fsipv6SENDRcvTaOptPkts':fsipv6SENDRcvTaOptPkts,'fsipv6SENDRcvTimeStampOptPkts':fsipv6SENDRcvTimeStampOptPkts,'fsipv6SENDDrpPktStatsTable':fsipv6SENDDrpPktStatsTable,'fsipv6SENDDrpPktStatsEntry':fsipv6SENDDrpPktStatsEntry,_A6:fsipv6SENDDrpPktType,'fsipv6SENDDrpCgaOptPkts':fsipv6SENDDrpCgaOptPkts,'fsipv6SENDDrpCertOptPkts':fsipv6SENDDrpCertOptPkts,'fsipv6SENDDrpMtuOptPkts':fsipv6SENDDrpMtuOptPkts,'fsipv6SENDDrpNonceOptPkts':fsipv6SENDDrpNonceOptPkts,'fsipv6SENDDrpPrefixOptPkts':fsipv6SENDDrpPrefixOptPkts,'fsipv6SENDDrpRedirHdrPkts':fsipv6SENDDrpRedirHdrPkts,'fsipv6SENDDrpRsaOptPkts':fsipv6SENDDrpRsaOptPkts,'fsipv6SENDDrpSrcLinkAddrPkts':fsipv6SENDDrpSrcLinkAddrPkts,'fsipv6SENDDrpTgtLinkAddrPkts':fsipv6SENDDrpTgtLinkAddrPkts,'fsipv6SENDDrpTaOptPkts':fsipv6SENDDrpTaOptPkts,'fsipv6SENDDrpTimeStampOptPkts':fsipv6SENDDrpTimeStampOptPkts,'fsipv6RARouteInfoTable':fsipv6RARouteInfoTable,'fsipv6RARouteInfoEntry':fsipv6RARouteInfoEntry,_A7:fsipv6RARouteIfIndex,_A8:fsipv6RARoutePrefix,_A9:fsipv6RARoutePrefixLen,'fsipv6RARoutePreference':fsipv6RARoutePreference,'fsipv6RARouteLifetime':fsipv6RARouteLifetime,'fsipv6RARouteRowStatus':fsipv6RARouteRowStatus,'fsipv6Test':fsipv6Test,'fsIpv6TestRedEntryTime':fsIpv6TestRedEntryTime,'fsIpv6TestRedExitTime':fsIpv6TestRedExitTime,'fsipv6RaRDNSSTable':fsipv6RaRDNSSTable,'fsipv6IfRaRDNSSTable':fsipv6IfRaRDNSSTable,'fsipv6IfRaRDNSSEntry':fsipv6IfRaRDNSSEntry,'fsipv6IfRaRDNSSIndex':fsipv6IfRaRDNSSIndex,'fsipv6IfRadvRDNSSOpen':fsipv6IfRadvRDNSSOpen,'fsipv6IfRaRDNSSPreference':fsipv6IfRaRDNSSPreference,'fsipv6IfRaRDNSSLifetime':fsipv6IfRaRDNSSLifetime,'fsipv6IfRaRDNSSAddrOne':fsipv6IfRaRDNSSAddrOne,'fsipv6IfRaRDNSSAddrTwo':fsipv6IfRaRDNSSAddrTwo,'fsipv6IfRaRDNSSAddrThree':fsipv6IfRaRDNSSAddrThree,'fsipv6IfRaRDNSSRowStatus':fsipv6IfRaRDNSSRowStatus,'fsipv6IfDomainNameOne':fsipv6IfDomainNameOne,'fsipv6IfDomainNameTwo':fsipv6IfDomainNameTwo,'fsipv6IfDomainNameThree':fsipv6IfDomainNameThree,'fsipv6IfDnsLifeTime':fsipv6IfDnsLifeTime,'fsipv6IfRaRDNSSAddrOneLife':fsipv6IfRaRDNSSAddrOneLife,'fsipv6IfRaRDNSSAddrTwoLife':fsipv6IfRaRDNSSAddrTwoLife,'fsipv6IfRaRDNSSAddrThreeLife':fsipv6IfRaRDNSSAddrThreeLife,'fsipv6IfDomainNameOneLife':fsipv6IfDomainNameOneLife,'fsipv6IfDomainNameTwoLife':fsipv6IfDomainNameTwoLife,'fsipv6IfDomainNameThreeLife':fsipv6IfDomainNameThreeLife,'fsipv6Icmp':fsipv6Icmp,'fsipv6IcmpInMsgs':fsipv6IcmpInMsgs,'fsipv6IcmpInErrors':fsipv6IcmpInErrors,'fsipv6IcmpInDestUnreachs':fsipv6IcmpInDestUnreachs,'fsipv6IcmpInTimeExcds':fsipv6IcmpInTimeExcds,'fsipv6IcmpInParmProbs':fsipv6IcmpInParmProbs,'fsipv6IcmpInPktTooBigs':fsipv6IcmpInPktTooBigs,'fsipv6IcmpInEchos':fsipv6IcmpInEchos,'fsipv6IcmpInEchoReps':fsipv6IcmpInEchoReps,'fsipv6IcmpInRouterSolicits':fsipv6IcmpInRouterSolicits,'fsipv6IcmpInRouterAdvertisements':fsipv6IcmpInRouterAdvertisements,'fsipv6IcmpInNeighborSolicits':fsipv6IcmpInNeighborSolicits,'fsipv6IcmpInNeighborAdvertisements':fsipv6IcmpInNeighborAdvertisements,'fsipv6IcmpInRedirects':fsipv6IcmpInRedirects,'fsipv6IcmpInAdminProhib':fsipv6IcmpInAdminProhib,'fsipv6IcmpOutMsgs':fsipv6IcmpOutMsgs,'fsipv6IcmpOutErrors':fsipv6IcmpOutErrors,'fsipv6IcmpOutDestUnreachs':fsipv6IcmpOutDestUnreachs,'fsipv6IcmpOutTimeExcds':fsipv6IcmpOutTimeExcds,'fsipv6IcmpOutParmProbs':fsipv6IcmpOutParmProbs,'fsipv6IcmpOutPktTooBigs':fsipv6IcmpOutPktTooBigs,'fsipv6IcmpOutEchos':fsipv6IcmpOutEchos,'fsipv6IcmpOutEchoReps':fsipv6IcmpOutEchoReps,'fsipv6IcmpOutRouterSolicits':fsipv6IcmpOutRouterSolicits,'fsipv6IcmpOutRouterAdvertisements':fsipv6IcmpOutRouterAdvertisements,'fsipv6IcmpOutNeighborSolicits':fsipv6IcmpOutNeighborSolicits,'fsipv6IcmpOutNeighborAdvertisements':fsipv6IcmpOutNeighborAdvertisements,'fsipv6IcmpOutRedirects':fsipv6IcmpOutRedirects,'fsipv6IcmpOutAdminProhib':fsipv6IcmpOutAdminProhib,'fsipv6IcmpInBadCode':fsipv6IcmpInBadCode,'fsipv6IcmpInNARouterFlagSet':fsipv6IcmpInNARouterFlagSet,'fsipv6IcmpInNASolicitedFlagSet':fsipv6IcmpInNASolicitedFlagSet,'fsipv6IcmpInNAOverrideFlagSet':fsipv6IcmpInNAOverrideFlagSet,'fsipv6IcmpOutNARouterFlagSet':fsipv6IcmpOutNARouterFlagSet,'fsipv6IcmpOutNASolicitedFlagSet':fsipv6IcmpOutNASolicitedFlagSet,'fsipv6IcmpOutNAOverrideFlagSet':fsipv6IcmpOutNAOverrideFlagSet,'fsipv6Udp':fsipv6Udp,'fsipv6UdpScalars':fsipv6UdpScalars,'fsipv6UdpInDatagrams':fsipv6UdpInDatagrams,'fsipv6UdpNoPorts':fsipv6UdpNoPorts,'fsipv6UdpInErrors':fsipv6UdpInErrors,'fsipv6UdpOutDatagrams':fsipv6UdpOutDatagrams,'fsipv6Tunnel':fsipv6Tunnel,'fsipv6Route':fsipv6Route,'fsipv6RouteTable':fsipv6RouteTable,'fsipv6RouteEntry':fsipv6RouteEntry,_AA:fsipv6RouteDest,_AB:fsipv6RoutePfxLength,_AC:fsipv6RouteProtocol,_AD:fsipv6RouteNextHop,'fsipv6RouteIfIndex':fsipv6RouteIfIndex,'fsipv6RouteMetric':fsipv6RouteMetric,'fsipv6RouteType':fsipv6RouteType,'fsipv6RouteTag':fsipv6RouteTag,'fsipv6RouteAge':fsipv6RouteAge,'fsipv6RouteAdminStatus':fsipv6RouteAdminStatus,'fsipv6RouteAddrType':fsipv6RouteAddrType,'fsipv6RouteHwStatus':fsipv6RouteHwStatus,'fsipv6RoutePreference':fsipv6RoutePreference,'fsipv6PrefTable':fsipv6PrefTable,'fsipv6PrefEntry':fsipv6PrefEntry,_AE:fsipv6Protocol,'fsipv6Preference':fsipv6Preference})