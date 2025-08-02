_p='fsMIIpv6IfEntry'
_o='fsMIIpv6Protocol'
_n='fsMIIpv6ScopeZoneName'
_m='fsMIIpv6ScopeZoneContextId'
_l='overridden'
_k='fsMIIpv6ScopeZoneIndexIfIndex'
_j='fsMIIpv6AddrSelPolicyIfIndex'
_i='fsMIIpv6AddrSelPolicyPrefixLen'
_h='fsMIIpv6AddrSelPolicyPrefix'
_g='fsMIIpv6PingIndex'
_f='create'
_e='fsMIIpv6NDProxyAddr'
_d='fsMIIpv6PmtuDest'
_c='variable'
_b='fsMIIpv6AddrProfileIndex'
_a='unicast'
_Z='fsMIIpv6AddrPrefixLen'
_Y='fsMIIpv6AddrAddress'
_X='disable'
_W='enable'
_V='fsMIStdIpv6InterfaceIfIndex'
_U='fsMIStdIpIfStatsIfIndex'
_T='automatic'
_S='off'
_R='anycast'
_Q='read-create'
_P='down'
_O='invalid'
_N='disabled'
_M='enabled'
_L='fsMIStdIpContextId'
_K='Unsigned32'
_J='SUPERMICRO-MISTD-IPVX-MIB'
_I='OctetString'
_H='not-accessible'
_G='Invalid'
_F='SUPERMICRO-MIIPV6-MIB'
_E='DisplayString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetScopeType,InetZoneIndex=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetScopeType','InetZoneIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
fsMIStdIpContextId,fsMIStdIpIfStatsIfIndex,fsMIStdIpv6InterfaceEntry,fsMIStdIpv6InterfaceIfIndex=mibBuilder.importSymbols(_J,_L,_U,'fsMIStdIpv6InterfaceEntry',_V)
fsMIipv6MIB=ModuleIdentity((1,3,6,1,4,1,10876,101,2,35))
if mibBuilder.loadTexts:fsMIipv6MIB.setRevisions(('2012-09-05 00:00',))
class InterfaceList(TextualConvention,OctetString):status=_A
_FsMIipv6_ObjectIdentity=ObjectIdentity
fsMIipv6=_FsMIipv6_ObjectIdentity((1,3,6,1,4,1,10876,101,2,35,1))
_FsMIIpv6ContextTable_Object=MibTable
fsMIIpv6ContextTable=_FsMIIpv6ContextTable_Object((1,3,6,1,4,1,10876,101,2,35,1,1))
if mibBuilder.loadTexts:fsMIIpv6ContextTable.setStatus(_A)
_FsMIIpv6ContextEntry_Object=MibTableRow
fsMIIpv6ContextEntry=_FsMIIpv6ContextEntry_Object((1,3,6,1,4,1,10876,101,2,35,1,1,1))
fsMIIpv6ContextEntry.setIndexNames((0,_J,_L))
if mibBuilder.loadTexts:fsMIIpv6ContextEntry.setStatus(_A)
class _FsMIIpv6NdCacheMaxRetries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsMIIpv6NdCacheMaxRetries_Type.__name__=_D
_FsMIIpv6NdCacheMaxRetries_Object=MibTableColumn
fsMIIpv6NdCacheMaxRetries=_FsMIIpv6NdCacheMaxRetries_Object((1,3,6,1,4,1,10876,101,2,35,1,1,1,1),_FsMIIpv6NdCacheMaxRetries_Type())
fsMIIpv6NdCacheMaxRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6NdCacheMaxRetries.setStatus(_A)
class _FsMIIpv6PmtuConfigStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_FsMIIpv6PmtuConfigStatus_Type.__name__=_D
_FsMIIpv6PmtuConfigStatus_Object=MibTableColumn
fsMIIpv6PmtuConfigStatus=_FsMIIpv6PmtuConfigStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,1,1,2),_FsMIIpv6PmtuConfigStatus_Type())
fsMIIpv6PmtuConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6PmtuConfigStatus.setStatus(_A)
class _FsMIIpv6PmtuTimeOutInterval_Type(Unsigned32):defaultValue=60
_FsMIIpv6PmtuTimeOutInterval_Type.__name__=_K
_FsMIIpv6PmtuTimeOutInterval_Object=MibTableColumn
fsMIIpv6PmtuTimeOutInterval=_FsMIIpv6PmtuTimeOutInterval_Object((1,3,6,1,4,1,10876,101,2,35,1,1,1,3),_FsMIIpv6PmtuTimeOutInterval_Type())
fsMIIpv6PmtuTimeOutInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6PmtuTimeOutInterval.setStatus(_A)
class _FsMIIpv6JumboEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_FsMIIpv6JumboEnable_Type.__name__=_D
_FsMIIpv6JumboEnable_Object=MibTableColumn
fsMIIpv6JumboEnable=_FsMIIpv6JumboEnable_Object((1,3,6,1,4,1,10876,101,2,35,1,1,1,4),_FsMIIpv6JumboEnable_Type())
fsMIIpv6JumboEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6JumboEnable.setStatus(_A)
_FsMIIpv6NumOfSendJumbo_Type=Integer32
_FsMIIpv6NumOfSendJumbo_Object=MibTableColumn
fsMIIpv6NumOfSendJumbo=_FsMIIpv6NumOfSendJumbo_Object((1,3,6,1,4,1,10876,101,2,35,1,1,1,5),_FsMIIpv6NumOfSendJumbo_Type())
fsMIIpv6NumOfSendJumbo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6NumOfSendJumbo.setStatus(_A)
_FsMIIpv6NumOfRecvJumbo_Type=Integer32
_FsMIIpv6NumOfRecvJumbo_Object=MibTableColumn
fsMIIpv6NumOfRecvJumbo=_FsMIIpv6NumOfRecvJumbo_Object((1,3,6,1,4,1,10876,101,2,35,1,1,1,6),_FsMIIpv6NumOfRecvJumbo_Type())
fsMIIpv6NumOfRecvJumbo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6NumOfRecvJumbo.setStatus(_A)
_FsMIIpv6ErrJumbo_Type=Integer32
_FsMIIpv6ErrJumbo_Object=MibTableColumn
fsMIIpv6ErrJumbo=_FsMIIpv6ErrJumbo_Object((1,3,6,1,4,1,10876,101,2,35,1,1,1,7),_FsMIIpv6ErrJumbo_Type())
fsMIIpv6ErrJumbo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6ErrJumbo.setStatus(_A)
_FsMIIpv6ContextDebug_Type=Unsigned32
_FsMIIpv6ContextDebug_Object=MibTableColumn
fsMIIpv6ContextDebug=_FsMIIpv6ContextDebug_Object((1,3,6,1,4,1,10876,101,2,35,1,1,1,8),_FsMIIpv6ContextDebug_Type())
fsMIIpv6ContextDebug.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6ContextDebug.setStatus(_A)
class _FsMIIpv6RFC5095Compatibility_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_FsMIIpv6RFC5095Compatibility_Type.__name__=_D
_FsMIIpv6RFC5095Compatibility_Object=MibTableColumn
fsMIIpv6RFC5095Compatibility=_FsMIIpv6RFC5095Compatibility_Object((1,3,6,1,4,1,10876,101,2,35,1,1,1,9),_FsMIIpv6RFC5095Compatibility_Type())
fsMIIpv6RFC5095Compatibility.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6RFC5095Compatibility.setStatus(_A)
_FsMIIpv6IfTable_Object=MibTable
fsMIIpv6IfTable=_FsMIIpv6IfTable_Object((1,3,6,1,4,1,10876,101,2,35,1,2))
if mibBuilder.loadTexts:fsMIIpv6IfTable.setStatus(_A)
_FsMIIpv6IfEntry_Object=MibTableRow
fsMIIpv6IfEntry=_FsMIIpv6IfEntry_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1))
if mibBuilder.loadTexts:fsMIIpv6IfEntry.setStatus(_A)
class _FsMIIpv6IfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,23,32,131,136)));namedValues=NamedValues(*(('ethernetcsmacd',6),('ppp',23),('framerelay',32),('tunnel',131),('l3ipvlan',136)))
_FsMIIpv6IfType_Type.__name__=_D
_FsMIIpv6IfType_Object=MibTableColumn
fsMIIpv6IfType=_FsMIIpv6IfType_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,1),_FsMIIpv6IfType_Type())
fsMIIpv6IfType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfType.setStatus(_A)
class _FsMIIpv6IfPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsMIIpv6IfPortNum_Type.__name__=_D
_FsMIIpv6IfPortNum_Object=MibTableColumn
fsMIIpv6IfPortNum=_FsMIIpv6IfPortNum_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,2),_FsMIIpv6IfPortNum_Type())
fsMIIpv6IfPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfPortNum.setStatus(_A)
_FsMIIpv6IfCircuitNum_Type=Integer32
_FsMIIpv6IfCircuitNum_Object=MibTableColumn
fsMIIpv6IfCircuitNum=_FsMIIpv6IfCircuitNum_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,3),_FsMIIpv6IfCircuitNum_Type())
fsMIIpv6IfCircuitNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfCircuitNum.setStatus(_A)
class _FsMIIpv6IfToken_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_FsMIIpv6IfToken_Type.__name__=_I
_FsMIIpv6IfToken_Object=MibTableColumn
fsMIIpv6IfToken=_FsMIIpv6IfToken_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,4),_FsMIIpv6IfToken_Type())
fsMIIpv6IfToken.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfToken.setStatus(_A)
class _FsMIIpv6IfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_P,2),('stale',3)))
_FsMIIpv6IfOperStatus_Type.__name__=_D
_FsMIIpv6IfOperStatus_Object=MibTableColumn
fsMIIpv6IfOperStatus=_FsMIIpv6IfOperStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,5),_FsMIIpv6IfOperStatus_Type())
fsMIIpv6IfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfOperStatus.setStatus(_A)
class _FsMIIpv6IfRouterAdvStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_FsMIIpv6IfRouterAdvStatus_Type.__name__=_D
_FsMIIpv6IfRouterAdvStatus_Object=MibTableColumn
fsMIIpv6IfRouterAdvStatus=_FsMIIpv6IfRouterAdvStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,6),_FsMIIpv6IfRouterAdvStatus_Type())
fsMIIpv6IfRouterAdvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfRouterAdvStatus.setStatus(_A)
class _FsMIIpv6IfRouterAdvFlags_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('mbit',1),('obit',2),('nombit',3),('noobit',4),('mobits',5),('none',6)))
_FsMIIpv6IfRouterAdvFlags_Type.__name__=_D
_FsMIIpv6IfRouterAdvFlags_Object=MibTableColumn
fsMIIpv6IfRouterAdvFlags=_FsMIIpv6IfRouterAdvFlags_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,7),_FsMIIpv6IfRouterAdvFlags_Type())
fsMIIpv6IfRouterAdvFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfRouterAdvFlags.setStatus(_A)
class _FsMIIpv6IfHopLimit_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsMIIpv6IfHopLimit_Type.__name__=_D
_FsMIIpv6IfHopLimit_Object=MibTableColumn
fsMIIpv6IfHopLimit=_FsMIIpv6IfHopLimit_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,8),_FsMIIpv6IfHopLimit_Type())
fsMIIpv6IfHopLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfHopLimit.setStatus(_A)
class _FsMIIpv6IfDefRouterTime_Type(Integer32):defaultValue=0
_FsMIIpv6IfDefRouterTime_Type.__name__=_D
_FsMIIpv6IfDefRouterTime_Object=MibTableColumn
fsMIIpv6IfDefRouterTime=_FsMIIpv6IfDefRouterTime_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,9),_FsMIIpv6IfDefRouterTime_Type())
fsMIIpv6IfDefRouterTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfDefRouterTime.setStatus(_A)
class _FsMIIpv6IfReachableTime_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FsMIIpv6IfReachableTime_Type.__name__=_D
_FsMIIpv6IfReachableTime_Object=MibTableColumn
fsMIIpv6IfReachableTime=_FsMIIpv6IfReachableTime_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,10),_FsMIIpv6IfReachableTime_Type())
fsMIIpv6IfReachableTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfReachableTime.setStatus(_A)
class _FsMIIpv6IfRetransmitTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_FsMIIpv6IfRetransmitTime_Type.__name__=_D
_FsMIIpv6IfRetransmitTime_Object=MibTableColumn
fsMIIpv6IfRetransmitTime=_FsMIIpv6IfRetransmitTime_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,11),_FsMIIpv6IfRetransmitTime_Type())
fsMIIpv6IfRetransmitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfRetransmitTime.setStatus(_A)
class _FsMIIpv6IfDelayProbeTime_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FsMIIpv6IfDelayProbeTime_Type.__name__=_D
_FsMIIpv6IfDelayProbeTime_Object=MibTableColumn
fsMIIpv6IfDelayProbeTime=_FsMIIpv6IfDelayProbeTime_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,12),_FsMIIpv6IfDelayProbeTime_Type())
fsMIIpv6IfDelayProbeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfDelayProbeTime.setStatus(_A)
class _FsMIIpv6IfPrefixAdvStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_FsMIIpv6IfPrefixAdvStatus_Type.__name__=_D
_FsMIIpv6IfPrefixAdvStatus_Object=MibTableColumn
fsMIIpv6IfPrefixAdvStatus=_FsMIIpv6IfPrefixAdvStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,13),_FsMIIpv6IfPrefixAdvStatus_Type())
fsMIIpv6IfPrefixAdvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfPrefixAdvStatus.setStatus(_A)
class _FsMIIpv6IfMinRouterAdvTime_Type(Integer32):defaultValue=198
_FsMIIpv6IfMinRouterAdvTime_Type.__name__=_D
_FsMIIpv6IfMinRouterAdvTime_Object=MibTableColumn
fsMIIpv6IfMinRouterAdvTime=_FsMIIpv6IfMinRouterAdvTime_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,14),_FsMIIpv6IfMinRouterAdvTime_Type())
fsMIIpv6IfMinRouterAdvTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfMinRouterAdvTime.setStatus(_A)
class _FsMIIpv6IfMaxRouterAdvTime_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_FsMIIpv6IfMaxRouterAdvTime_Type.__name__=_D
_FsMIIpv6IfMaxRouterAdvTime_Object=MibTableColumn
fsMIIpv6IfMaxRouterAdvTime=_FsMIIpv6IfMaxRouterAdvTime_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,15),_FsMIIpv6IfMaxRouterAdvTime_Type())
fsMIIpv6IfMaxRouterAdvTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfMaxRouterAdvTime.setStatus(_A)
class _FsMIIpv6IfDADRetries_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FsMIIpv6IfDADRetries_Type.__name__=_D
_FsMIIpv6IfDADRetries_Object=MibTableColumn
fsMIIpv6IfDADRetries=_FsMIIpv6IfDADRetries_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,16),_FsMIIpv6IfDADRetries_Type())
fsMIIpv6IfDADRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfDADRetries.setStatus(_A)
class _FsMIIpv6IfForwarding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_FsMIIpv6IfForwarding_Type.__name__=_D
_FsMIIpv6IfForwarding_Object=MibTableColumn
fsMIIpv6IfForwarding=_FsMIIpv6IfForwarding_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,17),_FsMIIpv6IfForwarding_Type())
fsMIIpv6IfForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfForwarding.setStatus(_A)
class _FsMIIpv6IfRoutingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_FsMIIpv6IfRoutingStatus_Type.__name__=_D
_FsMIIpv6IfRoutingStatus_Object=MibTableColumn
fsMIIpv6IfRoutingStatus=_FsMIIpv6IfRoutingStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,18),_FsMIIpv6IfRoutingStatus_Type())
fsMIIpv6IfRoutingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfRoutingStatus.setStatus(_A)
class _FsMIIpv6IfIcmpErrInterval_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMIIpv6IfIcmpErrInterval_Type.__name__=_D
_FsMIIpv6IfIcmpErrInterval_Object=MibTableColumn
fsMIIpv6IfIcmpErrInterval=_FsMIIpv6IfIcmpErrInterval_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,19),_FsMIIpv6IfIcmpErrInterval_Type())
fsMIIpv6IfIcmpErrInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfIcmpErrInterval.setStatus(_A)
class _FsMIIpv6IfIcmpTokenBucketSize_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_FsMIIpv6IfIcmpTokenBucketSize_Type.__name__=_D
_FsMIIpv6IfIcmpTokenBucketSize_Object=MibTableColumn
fsMIIpv6IfIcmpTokenBucketSize=_FsMIIpv6IfIcmpTokenBucketSize_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,20),_FsMIIpv6IfIcmpTokenBucketSize_Type())
fsMIIpv6IfIcmpTokenBucketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfIcmpTokenBucketSize.setStatus(_A)
class _FsMIIpv6IfDestUnreachableMsg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_FsMIIpv6IfDestUnreachableMsg_Type.__name__=_D
_FsMIIpv6IfDestUnreachableMsg_Object=MibTableColumn
fsMIIpv6IfDestUnreachableMsg=_FsMIIpv6IfDestUnreachableMsg_Object((1,3,6,1,4,1,10876,101,2,35,1,2,1,21),_FsMIIpv6IfDestUnreachableMsg_Type())
fsMIIpv6IfDestUnreachableMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IfDestUnreachableMsg.setStatus(_A)
_FsMIIpv6IfStatsTable_Object=MibTable
fsMIIpv6IfStatsTable=_FsMIIpv6IfStatsTable_Object((1,3,6,1,4,1,10876,101,2,35,1,3))
if mibBuilder.loadTexts:fsMIIpv6IfStatsTable.setStatus(_A)
_FsMIIpv6IfStatsEntry_Object=MibTableRow
fsMIIpv6IfStatsEntry=_FsMIIpv6IfStatsEntry_Object((1,3,6,1,4,1,10876,101,2,35,1,3,1))
fsMIIpv6IfStatsEntry.setIndexNames((0,_J,_U))
if mibBuilder.loadTexts:fsMIIpv6IfStatsEntry.setStatus(_A)
_FsMIIpv6IfStatsTooBigErrors_Type=Counter32
_FsMIIpv6IfStatsTooBigErrors_Object=MibTableColumn
fsMIIpv6IfStatsTooBigErrors=_FsMIIpv6IfStatsTooBigErrors_Object((1,3,6,1,4,1,10876,101,2,35,1,3,1,1),_FsMIIpv6IfStatsTooBigErrors_Type())
fsMIIpv6IfStatsTooBigErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfStatsTooBigErrors.setStatus(_A)
_FsMIIpv6IfStatsInRouterSols_Type=Counter32
_FsMIIpv6IfStatsInRouterSols_Object=MibTableColumn
fsMIIpv6IfStatsInRouterSols=_FsMIIpv6IfStatsInRouterSols_Object((1,3,6,1,4,1,10876,101,2,35,1,3,1,2),_FsMIIpv6IfStatsInRouterSols_Type())
fsMIIpv6IfStatsInRouterSols.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfStatsInRouterSols.setStatus(_A)
_FsMIIpv6IfStatsInRouterAdvs_Type=Counter32
_FsMIIpv6IfStatsInRouterAdvs_Object=MibTableColumn
fsMIIpv6IfStatsInRouterAdvs=_FsMIIpv6IfStatsInRouterAdvs_Object((1,3,6,1,4,1,10876,101,2,35,1,3,1,3),_FsMIIpv6IfStatsInRouterAdvs_Type())
fsMIIpv6IfStatsInRouterAdvs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfStatsInRouterAdvs.setStatus(_A)
_FsMIIpv6IfStatsInNeighSols_Type=Counter32
_FsMIIpv6IfStatsInNeighSols_Object=MibTableColumn
fsMIIpv6IfStatsInNeighSols=_FsMIIpv6IfStatsInNeighSols_Object((1,3,6,1,4,1,10876,101,2,35,1,3,1,4),_FsMIIpv6IfStatsInNeighSols_Type())
fsMIIpv6IfStatsInNeighSols.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfStatsInNeighSols.setStatus(_A)
_FsMIIpv6IfStatsInNeighAdvs_Type=Counter32
_FsMIIpv6IfStatsInNeighAdvs_Object=MibTableColumn
fsMIIpv6IfStatsInNeighAdvs=_FsMIIpv6IfStatsInNeighAdvs_Object((1,3,6,1,4,1,10876,101,2,35,1,3,1,5),_FsMIIpv6IfStatsInNeighAdvs_Type())
fsMIIpv6IfStatsInNeighAdvs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfStatsInNeighAdvs.setStatus(_A)
_FsMIIpv6IfStatsInRedirects_Type=Counter32
_FsMIIpv6IfStatsInRedirects_Object=MibTableColumn
fsMIIpv6IfStatsInRedirects=_FsMIIpv6IfStatsInRedirects_Object((1,3,6,1,4,1,10876,101,2,35,1,3,1,6),_FsMIIpv6IfStatsInRedirects_Type())
fsMIIpv6IfStatsInRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfStatsInRedirects.setStatus(_A)
_FsMIIpv6IfStatsOutRouterSols_Type=Counter32
_FsMIIpv6IfStatsOutRouterSols_Object=MibTableColumn
fsMIIpv6IfStatsOutRouterSols=_FsMIIpv6IfStatsOutRouterSols_Object((1,3,6,1,4,1,10876,101,2,35,1,3,1,7),_FsMIIpv6IfStatsOutRouterSols_Type())
fsMIIpv6IfStatsOutRouterSols.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfStatsOutRouterSols.setStatus(_A)
_FsMIIpv6IfStatsOutRouterAdvs_Type=Counter32
_FsMIIpv6IfStatsOutRouterAdvs_Object=MibTableColumn
fsMIIpv6IfStatsOutRouterAdvs=_FsMIIpv6IfStatsOutRouterAdvs_Object((1,3,6,1,4,1,10876,101,2,35,1,3,1,8),_FsMIIpv6IfStatsOutRouterAdvs_Type())
fsMIIpv6IfStatsOutRouterAdvs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfStatsOutRouterAdvs.setStatus(_A)
_FsMIIpv6IfStatsOutNeighSols_Type=Counter32
_FsMIIpv6IfStatsOutNeighSols_Object=MibTableColumn
fsMIIpv6IfStatsOutNeighSols=_FsMIIpv6IfStatsOutNeighSols_Object((1,3,6,1,4,1,10876,101,2,35,1,3,1,9),_FsMIIpv6IfStatsOutNeighSols_Type())
fsMIIpv6IfStatsOutNeighSols.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfStatsOutNeighSols.setStatus(_A)
_FsMIIpv6IfStatsOutNeighAdvs_Type=Counter32
_FsMIIpv6IfStatsOutNeighAdvs_Object=MibTableColumn
fsMIIpv6IfStatsOutNeighAdvs=_FsMIIpv6IfStatsOutNeighAdvs_Object((1,3,6,1,4,1,10876,101,2,35,1,3,1,10),_FsMIIpv6IfStatsOutNeighAdvs_Type())
fsMIIpv6IfStatsOutNeighAdvs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfStatsOutNeighAdvs.setStatus(_A)
_FsMIIpv6IfStatsOutRedirects_Type=Counter32
_FsMIIpv6IfStatsOutRedirects_Object=MibTableColumn
fsMIIpv6IfStatsOutRedirects=_FsMIIpv6IfStatsOutRedirects_Object((1,3,6,1,4,1,10876,101,2,35,1,3,1,11),_FsMIIpv6IfStatsOutRedirects_Type())
fsMIIpv6IfStatsOutRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfStatsOutRedirects.setStatus(_A)
_FsMIIpv6IfStatsLastRouterAdvTime_Type=TimeTicks
_FsMIIpv6IfStatsLastRouterAdvTime_Object=MibTableColumn
fsMIIpv6IfStatsLastRouterAdvTime=_FsMIIpv6IfStatsLastRouterAdvTime_Object((1,3,6,1,4,1,10876,101,2,35,1,3,1,12),_FsMIIpv6IfStatsLastRouterAdvTime_Type())
fsMIIpv6IfStatsLastRouterAdvTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfStatsLastRouterAdvTime.setStatus(_A)
_FsMIIpv6IfStatsNextRouterAdvTime_Type=TimeTicks
_FsMIIpv6IfStatsNextRouterAdvTime_Object=MibTableColumn
fsMIIpv6IfStatsNextRouterAdvTime=_FsMIIpv6IfStatsNextRouterAdvTime_Object((1,3,6,1,4,1,10876,101,2,35,1,3,1,13),_FsMIIpv6IfStatsNextRouterAdvTime_Type())
fsMIIpv6IfStatsNextRouterAdvTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfStatsNextRouterAdvTime.setStatus(_A)
_FsMIIpv6IfStatsIcmp6ErrRateLmtd_Type=Counter32
_FsMIIpv6IfStatsIcmp6ErrRateLmtd_Object=MibTableColumn
fsMIIpv6IfStatsIcmp6ErrRateLmtd=_FsMIIpv6IfStatsIcmp6ErrRateLmtd_Object((1,3,6,1,4,1,10876,101,2,35,1,3,1,14),_FsMIIpv6IfStatsIcmp6ErrRateLmtd_Type())
fsMIIpv6IfStatsIcmp6ErrRateLmtd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfStatsIcmp6ErrRateLmtd.setStatus(_A)
_FsMIIpv6AddrTable_Object=MibTable
fsMIIpv6AddrTable=_FsMIIpv6AddrTable_Object((1,3,6,1,4,1,10876,101,2,35,1,4))
if mibBuilder.loadTexts:fsMIIpv6AddrTable.setStatus(_A)
_FsMIIpv6AddrEntry_Object=MibTableRow
fsMIIpv6AddrEntry=_FsMIIpv6AddrEntry_Object((1,3,6,1,4,1,10876,101,2,35,1,4,1))
fsMIIpv6AddrEntry.setIndexNames((0,_J,_V),(0,_F,_Y),(0,_F,_Z))
if mibBuilder.loadTexts:fsMIIpv6AddrEntry.setStatus(_A)
class _FsMIIpv6AddrAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIIpv6AddrAddress_Type.__name__=_I
_FsMIIpv6AddrAddress_Object=MibTableColumn
fsMIIpv6AddrAddress=_FsMIIpv6AddrAddress_Object((1,3,6,1,4,1,10876,101,2,35,1,4,1,1),_FsMIIpv6AddrAddress_Type())
fsMIIpv6AddrAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpv6AddrAddress.setStatus(_A)
class _FsMIIpv6AddrPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsMIIpv6AddrPrefixLen_Type.__name__=_D
_FsMIIpv6AddrPrefixLen_Object=MibTableColumn
fsMIIpv6AddrPrefixLen=_FsMIIpv6AddrPrefixLen_Object((1,3,6,1,4,1,10876,101,2,35,1,4,1,2),_FsMIIpv6AddrPrefixLen_Type())
fsMIIpv6AddrPrefixLen.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpv6AddrPrefixLen.setStatus(_A)
_FsMIIpv6AddrAdminStatus_Type=RowStatus
_FsMIIpv6AddrAdminStatus_Object=MibTableColumn
fsMIIpv6AddrAdminStatus=_FsMIIpv6AddrAdminStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,4,1,3),_FsMIIpv6AddrAdminStatus_Type())
fsMIIpv6AddrAdminStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsMIIpv6AddrAdminStatus.setStatus(_A)
class _FsMIIpv6AddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),(_R,2),('linklocal',3)))
_FsMIIpv6AddrType_Type.__name__=_D
_FsMIIpv6AddrType_Object=MibTableColumn
fsMIIpv6AddrType=_FsMIIpv6AddrType_Object((1,3,6,1,4,1,10876,101,2,35,1,4,1,4),_FsMIIpv6AddrType_Type())
fsMIIpv6AddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6AddrType.setStatus(_A)
class _FsMIIpv6AddrProfIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_FsMIIpv6AddrProfIndex_Type.__name__=_D
_FsMIIpv6AddrProfIndex_Object=MibTableColumn
fsMIIpv6AddrProfIndex=_FsMIIpv6AddrProfIndex_Object((1,3,6,1,4,1,10876,101,2,35,1,4,1,5),_FsMIIpv6AddrProfIndex_Type())
fsMIIpv6AddrProfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6AddrProfIndex.setStatus(_A)
class _FsMIIpv6AddrOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tentative',1),('complete',2),(_P,3),('failed',4)))
_FsMIIpv6AddrOperStatus_Type.__name__=_D
_FsMIIpv6AddrOperStatus_Object=MibTableColumn
fsMIIpv6AddrOperStatus=_FsMIIpv6AddrOperStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,4,1,6),_FsMIIpv6AddrOperStatus_Type())
fsMIIpv6AddrOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6AddrOperStatus.setStatus(_A)
class _FsMIIpv6AddrContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIIpv6AddrContextId_Type.__name__=_D
_FsMIIpv6AddrContextId_Object=MibTableColumn
fsMIIpv6AddrContextId=_FsMIIpv6AddrContextId_Object((1,3,6,1,4,1,10876,101,2,35,1,4,1,7),_FsMIIpv6AddrContextId_Type())
fsMIIpv6AddrContextId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6AddrContextId.setStatus(_A)
_FsMIIpv6AddrScope_Type=InetScopeType
_FsMIIpv6AddrScope_Object=MibTableColumn
fsMIIpv6AddrScope=_FsMIIpv6AddrScope_Object((1,3,6,1,4,1,10876,101,2,35,1,4,1,8),_FsMIIpv6AddrScope_Type())
fsMIIpv6AddrScope.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6AddrScope.setStatus(_A)
_FsMIIpv6AddrProfileTable_Object=MibTable
fsMIIpv6AddrProfileTable=_FsMIIpv6AddrProfileTable_Object((1,3,6,1,4,1,10876,101,2,35,1,5))
if mibBuilder.loadTexts:fsMIIpv6AddrProfileTable.setStatus(_A)
_FsMIIpv6AddrProfileEntry_Object=MibTableRow
fsMIIpv6AddrProfileEntry=_FsMIIpv6AddrProfileEntry_Object((1,3,6,1,4,1,10876,101,2,35,1,5,1))
fsMIIpv6AddrProfileEntry.setIndexNames((0,_F,_b))
if mibBuilder.loadTexts:fsMIIpv6AddrProfileEntry.setStatus(_A)
class _FsMIIpv6AddrProfileIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_FsMIIpv6AddrProfileIndex_Type.__name__=_K
_FsMIIpv6AddrProfileIndex_Object=MibTableColumn
fsMIIpv6AddrProfileIndex=_FsMIIpv6AddrProfileIndex_Object((1,3,6,1,4,1,10876,101,2,35,1,5,1,1),_FsMIIpv6AddrProfileIndex_Type())
fsMIIpv6AddrProfileIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpv6AddrProfileIndex.setStatus(_A)
class _FsMIIpv6AddrProfileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_O,2)))
_FsMIIpv6AddrProfileStatus_Type.__name__=_D
_FsMIIpv6AddrProfileStatus_Object=MibTableColumn
fsMIIpv6AddrProfileStatus=_FsMIIpv6AddrProfileStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,5,1,2),_FsMIIpv6AddrProfileStatus_Type())
fsMIIpv6AddrProfileStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6AddrProfileStatus.setStatus(_A)
class _FsMIIpv6AddrProfilePrefixAdvStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_S,2)))
_FsMIIpv6AddrProfilePrefixAdvStatus_Type.__name__=_D
_FsMIIpv6AddrProfilePrefixAdvStatus_Object=MibTableColumn
fsMIIpv6AddrProfilePrefixAdvStatus=_FsMIIpv6AddrProfilePrefixAdvStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,5,1,3),_FsMIIpv6AddrProfilePrefixAdvStatus_Type())
fsMIIpv6AddrProfilePrefixAdvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6AddrProfilePrefixAdvStatus.setStatus(_A)
class _FsMIIpv6AddrProfileOnLinkAdvStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_S,2)))
_FsMIIpv6AddrProfileOnLinkAdvStatus_Type.__name__=_D
_FsMIIpv6AddrProfileOnLinkAdvStatus_Object=MibTableColumn
fsMIIpv6AddrProfileOnLinkAdvStatus=_FsMIIpv6AddrProfileOnLinkAdvStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,5,1,4),_FsMIIpv6AddrProfileOnLinkAdvStatus_Type())
fsMIIpv6AddrProfileOnLinkAdvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6AddrProfileOnLinkAdvStatus.setStatus(_A)
class _FsMIIpv6AddrProfileAutoConfAdvStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_S,2)))
_FsMIIpv6AddrProfileAutoConfAdvStatus_Type.__name__=_D
_FsMIIpv6AddrProfileAutoConfAdvStatus_Object=MibTableColumn
fsMIIpv6AddrProfileAutoConfAdvStatus=_FsMIIpv6AddrProfileAutoConfAdvStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,5,1,5),_FsMIIpv6AddrProfileAutoConfAdvStatus_Type())
fsMIIpv6AddrProfileAutoConfAdvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6AddrProfileAutoConfAdvStatus.setStatus(_A)
class _FsMIIpv6AddrProfilePreferredTime_Type(Unsigned32):defaultValue=604800;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsMIIpv6AddrProfilePreferredTime_Type.__name__=_K
_FsMIIpv6AddrProfilePreferredTime_Object=MibTableColumn
fsMIIpv6AddrProfilePreferredTime=_FsMIIpv6AddrProfilePreferredTime_Object((1,3,6,1,4,1,10876,101,2,35,1,5,1,6),_FsMIIpv6AddrProfilePreferredTime_Type())
fsMIIpv6AddrProfilePreferredTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6AddrProfilePreferredTime.setStatus(_A)
class _FsMIIpv6AddrProfileValidTime_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsMIIpv6AddrProfileValidTime_Type.__name__=_K
_FsMIIpv6AddrProfileValidTime_Object=MibTableColumn
fsMIIpv6AddrProfileValidTime=_FsMIIpv6AddrProfileValidTime_Object((1,3,6,1,4,1,10876,101,2,35,1,5,1,7),_FsMIIpv6AddrProfileValidTime_Type())
fsMIIpv6AddrProfileValidTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6AddrProfileValidTime.setStatus(_A)
class _FsMIIpv6AddrProfileValidLifeTimeFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixed',1),(_c,2)))
_FsMIIpv6AddrProfileValidLifeTimeFlag_Type.__name__=_D
_FsMIIpv6AddrProfileValidLifeTimeFlag_Object=MibTableColumn
fsMIIpv6AddrProfileValidLifeTimeFlag=_FsMIIpv6AddrProfileValidLifeTimeFlag_Object((1,3,6,1,4,1,10876,101,2,35,1,5,1,8),_FsMIIpv6AddrProfileValidLifeTimeFlag_Type())
fsMIIpv6AddrProfileValidLifeTimeFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6AddrProfileValidLifeTimeFlag.setStatus(_A)
class _FsMIIpv6AddrProfilePreferredLifeTimeFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixed',1),(_c,2)))
_FsMIIpv6AddrProfilePreferredLifeTimeFlag_Type.__name__=_D
_FsMIIpv6AddrProfilePreferredLifeTimeFlag_Object=MibTableColumn
fsMIIpv6AddrProfilePreferredLifeTimeFlag=_FsMIIpv6AddrProfilePreferredLifeTimeFlag_Object((1,3,6,1,4,1,10876,101,2,35,1,5,1,9),_FsMIIpv6AddrProfilePreferredLifeTimeFlag_Type())
fsMIIpv6AddrProfilePreferredLifeTimeFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6AddrProfilePreferredLifeTimeFlag.setStatus(_A)
_FsMIIpv6IcmpStatsTable_Object=MibTable
fsMIIpv6IcmpStatsTable=_FsMIIpv6IcmpStatsTable_Object((1,3,6,1,4,1,10876,101,2,35,1,6))
if mibBuilder.loadTexts:fsMIIpv6IcmpStatsTable.setStatus(_A)
_FsMIIpv6IcmpStatsEntry_Object=MibTableRow
fsMIIpv6IcmpStatsEntry=_FsMIIpv6IcmpStatsEntry_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1))
fsMIIpv6IcmpStatsEntry.setIndexNames((0,_J,_L))
if mibBuilder.loadTexts:fsMIIpv6IcmpStatsEntry.setStatus(_A)
_FsMIIpv6IcmpInMsgs_Type=Counter32
_FsMIIpv6IcmpInMsgs_Object=MibTableColumn
fsMIIpv6IcmpInMsgs=_FsMIIpv6IcmpInMsgs_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,1),_FsMIIpv6IcmpInMsgs_Type())
fsMIIpv6IcmpInMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInMsgs.setStatus(_A)
_FsMIIpv6IcmpInErrors_Type=Counter32
_FsMIIpv6IcmpInErrors_Object=MibTableColumn
fsMIIpv6IcmpInErrors=_FsMIIpv6IcmpInErrors_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,2),_FsMIIpv6IcmpInErrors_Type())
fsMIIpv6IcmpInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInErrors.setStatus(_A)
_FsMIIpv6IcmpInDestUnreachs_Type=Counter32
_FsMIIpv6IcmpInDestUnreachs_Object=MibTableColumn
fsMIIpv6IcmpInDestUnreachs=_FsMIIpv6IcmpInDestUnreachs_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,3),_FsMIIpv6IcmpInDestUnreachs_Type())
fsMIIpv6IcmpInDestUnreachs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInDestUnreachs.setStatus(_A)
_FsMIIpv6IcmpInTimeExcds_Type=Counter32
_FsMIIpv6IcmpInTimeExcds_Object=MibTableColumn
fsMIIpv6IcmpInTimeExcds=_FsMIIpv6IcmpInTimeExcds_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,4),_FsMIIpv6IcmpInTimeExcds_Type())
fsMIIpv6IcmpInTimeExcds.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInTimeExcds.setStatus(_A)
_FsMIIpv6IcmpInParmProbs_Type=Counter32
_FsMIIpv6IcmpInParmProbs_Object=MibTableColumn
fsMIIpv6IcmpInParmProbs=_FsMIIpv6IcmpInParmProbs_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,5),_FsMIIpv6IcmpInParmProbs_Type())
fsMIIpv6IcmpInParmProbs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInParmProbs.setStatus(_A)
_FsMIIpv6IcmpInPktTooBigs_Type=Counter32
_FsMIIpv6IcmpInPktTooBigs_Object=MibTableColumn
fsMIIpv6IcmpInPktTooBigs=_FsMIIpv6IcmpInPktTooBigs_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,6),_FsMIIpv6IcmpInPktTooBigs_Type())
fsMIIpv6IcmpInPktTooBigs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInPktTooBigs.setStatus(_A)
_FsMIIpv6IcmpInEchos_Type=Counter32
_FsMIIpv6IcmpInEchos_Object=MibTableColumn
fsMIIpv6IcmpInEchos=_FsMIIpv6IcmpInEchos_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,7),_FsMIIpv6IcmpInEchos_Type())
fsMIIpv6IcmpInEchos.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInEchos.setStatus(_A)
_FsMIIpv6IcmpInEchoReps_Type=Counter32
_FsMIIpv6IcmpInEchoReps_Object=MibTableColumn
fsMIIpv6IcmpInEchoReps=_FsMIIpv6IcmpInEchoReps_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,8),_FsMIIpv6IcmpInEchoReps_Type())
fsMIIpv6IcmpInEchoReps.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInEchoReps.setStatus(_A)
_FsMIIpv6IcmpInRouterSolicits_Type=Counter32
_FsMIIpv6IcmpInRouterSolicits_Object=MibTableColumn
fsMIIpv6IcmpInRouterSolicits=_FsMIIpv6IcmpInRouterSolicits_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,9),_FsMIIpv6IcmpInRouterSolicits_Type())
fsMIIpv6IcmpInRouterSolicits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInRouterSolicits.setStatus(_A)
_FsMIIpv6IcmpInRouterAdvertisements_Type=Counter32
_FsMIIpv6IcmpInRouterAdvertisements_Object=MibTableColumn
fsMIIpv6IcmpInRouterAdvertisements=_FsMIIpv6IcmpInRouterAdvertisements_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,10),_FsMIIpv6IcmpInRouterAdvertisements_Type())
fsMIIpv6IcmpInRouterAdvertisements.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInRouterAdvertisements.setStatus(_A)
_FsMIIpv6IcmpInNeighborSolicits_Type=Counter32
_FsMIIpv6IcmpInNeighborSolicits_Object=MibTableColumn
fsMIIpv6IcmpInNeighborSolicits=_FsMIIpv6IcmpInNeighborSolicits_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,11),_FsMIIpv6IcmpInNeighborSolicits_Type())
fsMIIpv6IcmpInNeighborSolicits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInNeighborSolicits.setStatus(_A)
_FsMIIpv6IcmpInNeighborAdvertisements_Type=Counter32
_FsMIIpv6IcmpInNeighborAdvertisements_Object=MibTableColumn
fsMIIpv6IcmpInNeighborAdvertisements=_FsMIIpv6IcmpInNeighborAdvertisements_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,12),_FsMIIpv6IcmpInNeighborAdvertisements_Type())
fsMIIpv6IcmpInNeighborAdvertisements.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInNeighborAdvertisements.setStatus(_A)
_FsMIIpv6IcmpInRedirects_Type=Counter32
_FsMIIpv6IcmpInRedirects_Object=MibTableColumn
fsMIIpv6IcmpInRedirects=_FsMIIpv6IcmpInRedirects_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,13),_FsMIIpv6IcmpInRedirects_Type())
fsMIIpv6IcmpInRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInRedirects.setStatus(_A)
_FsMIIpv6IcmpInAdminProhib_Type=Counter32
_FsMIIpv6IcmpInAdminProhib_Object=MibTableColumn
fsMIIpv6IcmpInAdminProhib=_FsMIIpv6IcmpInAdminProhib_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,14),_FsMIIpv6IcmpInAdminProhib_Type())
fsMIIpv6IcmpInAdminProhib.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInAdminProhib.setStatus(_A)
_FsMIIpv6IcmpOutMsgs_Type=Counter32
_FsMIIpv6IcmpOutMsgs_Object=MibTableColumn
fsMIIpv6IcmpOutMsgs=_FsMIIpv6IcmpOutMsgs_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,15),_FsMIIpv6IcmpOutMsgs_Type())
fsMIIpv6IcmpOutMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutMsgs.setStatus(_A)
_FsMIIpv6IcmpOutErrors_Type=Counter32
_FsMIIpv6IcmpOutErrors_Object=MibTableColumn
fsMIIpv6IcmpOutErrors=_FsMIIpv6IcmpOutErrors_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,16),_FsMIIpv6IcmpOutErrors_Type())
fsMIIpv6IcmpOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutErrors.setStatus(_A)
_FsMIIpv6IcmpOutDestUnreachs_Type=Counter32
_FsMIIpv6IcmpOutDestUnreachs_Object=MibTableColumn
fsMIIpv6IcmpOutDestUnreachs=_FsMIIpv6IcmpOutDestUnreachs_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,17),_FsMIIpv6IcmpOutDestUnreachs_Type())
fsMIIpv6IcmpOutDestUnreachs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutDestUnreachs.setStatus(_A)
_FsMIIpv6IcmpOutTimeExcds_Type=Counter32
_FsMIIpv6IcmpOutTimeExcds_Object=MibTableColumn
fsMIIpv6IcmpOutTimeExcds=_FsMIIpv6IcmpOutTimeExcds_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,18),_FsMIIpv6IcmpOutTimeExcds_Type())
fsMIIpv6IcmpOutTimeExcds.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutTimeExcds.setStatus(_A)
_FsMIIpv6IcmpOutParmProbs_Type=Counter32
_FsMIIpv6IcmpOutParmProbs_Object=MibTableColumn
fsMIIpv6IcmpOutParmProbs=_FsMIIpv6IcmpOutParmProbs_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,19),_FsMIIpv6IcmpOutParmProbs_Type())
fsMIIpv6IcmpOutParmProbs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutParmProbs.setStatus(_A)
_FsMIIpv6IcmpOutPktTooBigs_Type=Counter32
_FsMIIpv6IcmpOutPktTooBigs_Object=MibTableColumn
fsMIIpv6IcmpOutPktTooBigs=_FsMIIpv6IcmpOutPktTooBigs_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,20),_FsMIIpv6IcmpOutPktTooBigs_Type())
fsMIIpv6IcmpOutPktTooBigs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutPktTooBigs.setStatus(_A)
_FsMIIpv6IcmpOutEchos_Type=Counter32
_FsMIIpv6IcmpOutEchos_Object=MibTableColumn
fsMIIpv6IcmpOutEchos=_FsMIIpv6IcmpOutEchos_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,21),_FsMIIpv6IcmpOutEchos_Type())
fsMIIpv6IcmpOutEchos.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutEchos.setStatus(_A)
_FsMIIpv6IcmpOutEchoReps_Type=Counter32
_FsMIIpv6IcmpOutEchoReps_Object=MibTableColumn
fsMIIpv6IcmpOutEchoReps=_FsMIIpv6IcmpOutEchoReps_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,22),_FsMIIpv6IcmpOutEchoReps_Type())
fsMIIpv6IcmpOutEchoReps.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutEchoReps.setStatus(_A)
_FsMIIpv6IcmpOutRouterSolicits_Type=Counter32
_FsMIIpv6IcmpOutRouterSolicits_Object=MibTableColumn
fsMIIpv6IcmpOutRouterSolicits=_FsMIIpv6IcmpOutRouterSolicits_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,23),_FsMIIpv6IcmpOutRouterSolicits_Type())
fsMIIpv6IcmpOutRouterSolicits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutRouterSolicits.setStatus(_A)
_FsMIIpv6IcmpOutRouterAdvertisements_Type=Counter32
_FsMIIpv6IcmpOutRouterAdvertisements_Object=MibTableColumn
fsMIIpv6IcmpOutRouterAdvertisements=_FsMIIpv6IcmpOutRouterAdvertisements_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,24),_FsMIIpv6IcmpOutRouterAdvertisements_Type())
fsMIIpv6IcmpOutRouterAdvertisements.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutRouterAdvertisements.setStatus(_A)
_FsMIIpv6IcmpOutNeighborSolicits_Type=Counter32
_FsMIIpv6IcmpOutNeighborSolicits_Object=MibTableColumn
fsMIIpv6IcmpOutNeighborSolicits=_FsMIIpv6IcmpOutNeighborSolicits_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,25),_FsMIIpv6IcmpOutNeighborSolicits_Type())
fsMIIpv6IcmpOutNeighborSolicits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutNeighborSolicits.setStatus(_A)
_FsMIIpv6IcmpOutNeighborAdvertisements_Type=Counter32
_FsMIIpv6IcmpOutNeighborAdvertisements_Object=MibTableColumn
fsMIIpv6IcmpOutNeighborAdvertisements=_FsMIIpv6IcmpOutNeighborAdvertisements_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,26),_FsMIIpv6IcmpOutNeighborAdvertisements_Type())
fsMIIpv6IcmpOutNeighborAdvertisements.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutNeighborAdvertisements.setStatus(_A)
_FsMIIpv6IcmpOutRedirects_Type=Counter32
_FsMIIpv6IcmpOutRedirects_Object=MibTableColumn
fsMIIpv6IcmpOutRedirects=_FsMIIpv6IcmpOutRedirects_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,27),_FsMIIpv6IcmpOutRedirects_Type())
fsMIIpv6IcmpOutRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutRedirects.setStatus(_A)
_FsMIIpv6IcmpOutAdminProhib_Type=Counter32
_FsMIIpv6IcmpOutAdminProhib_Object=MibTableColumn
fsMIIpv6IcmpOutAdminProhib=_FsMIIpv6IcmpOutAdminProhib_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,28),_FsMIIpv6IcmpOutAdminProhib_Type())
fsMIIpv6IcmpOutAdminProhib.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutAdminProhib.setStatus(_A)
_FsMIIpv6IcmpInBadCode_Type=Counter32
_FsMIIpv6IcmpInBadCode_Object=MibTableColumn
fsMIIpv6IcmpInBadCode=_FsMIIpv6IcmpInBadCode_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,29),_FsMIIpv6IcmpInBadCode_Type())
fsMIIpv6IcmpInBadCode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInBadCode.setStatus(_A)
_FsMIIpv6IcmpInNARouterFlagSet_Type=Counter32
_FsMIIpv6IcmpInNARouterFlagSet_Object=MibTableColumn
fsMIIpv6IcmpInNARouterFlagSet=_FsMIIpv6IcmpInNARouterFlagSet_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,30),_FsMIIpv6IcmpInNARouterFlagSet_Type())
fsMIIpv6IcmpInNARouterFlagSet.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInNARouterFlagSet.setStatus(_A)
_FsMIIpv6IcmpInNASolicitedFlagSet_Type=Counter32
_FsMIIpv6IcmpInNASolicitedFlagSet_Object=MibTableColumn
fsMIIpv6IcmpInNASolicitedFlagSet=_FsMIIpv6IcmpInNASolicitedFlagSet_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,31),_FsMIIpv6IcmpInNASolicitedFlagSet_Type())
fsMIIpv6IcmpInNASolicitedFlagSet.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInNASolicitedFlagSet.setStatus(_A)
_FsMIIpv6IcmpInNAOverrideFlagSet_Type=Counter32
_FsMIIpv6IcmpInNAOverrideFlagSet_Object=MibTableColumn
fsMIIpv6IcmpInNAOverrideFlagSet=_FsMIIpv6IcmpInNAOverrideFlagSet_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,32),_FsMIIpv6IcmpInNAOverrideFlagSet_Type())
fsMIIpv6IcmpInNAOverrideFlagSet.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpInNAOverrideFlagSet.setStatus(_A)
_FsMIIpv6IcmpOutNARouterFlagSet_Type=Counter32
_FsMIIpv6IcmpOutNARouterFlagSet_Object=MibTableColumn
fsMIIpv6IcmpOutNARouterFlagSet=_FsMIIpv6IcmpOutNARouterFlagSet_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,33),_FsMIIpv6IcmpOutNARouterFlagSet_Type())
fsMIIpv6IcmpOutNARouterFlagSet.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutNARouterFlagSet.setStatus(_A)
_FsMIIpv6IcmpOutNASolicitedFlagSet_Type=Counter32
_FsMIIpv6IcmpOutNASolicitedFlagSet_Object=MibTableColumn
fsMIIpv6IcmpOutNASolicitedFlagSet=_FsMIIpv6IcmpOutNASolicitedFlagSet_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,34),_FsMIIpv6IcmpOutNASolicitedFlagSet_Type())
fsMIIpv6IcmpOutNASolicitedFlagSet.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutNASolicitedFlagSet.setStatus(_A)
_FsMIIpv6IcmpOutNAOverrideFlagSet_Type=Counter32
_FsMIIpv6IcmpOutNAOverrideFlagSet_Object=MibTableColumn
fsMIIpv6IcmpOutNAOverrideFlagSet=_FsMIIpv6IcmpOutNAOverrideFlagSet_Object((1,3,6,1,4,1,10876,101,2,35,1,6,1,35),_FsMIIpv6IcmpOutNAOverrideFlagSet_Type())
fsMIIpv6IcmpOutNAOverrideFlagSet.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IcmpOutNAOverrideFlagSet.setStatus(_A)
_FsMIIpv6PmtuTable_Object=MibTable
fsMIIpv6PmtuTable=_FsMIIpv6PmtuTable_Object((1,3,6,1,4,1,10876,101,2,35,1,7))
if mibBuilder.loadTexts:fsMIIpv6PmtuTable.setStatus(_A)
_FsMIIpv6PmtuEntry_Object=MibTableRow
fsMIIpv6PmtuEntry=_FsMIIpv6PmtuEntry_Object((1,3,6,1,4,1,10876,101,2,35,1,7,1))
fsMIIpv6PmtuEntry.setIndexNames((0,_J,_L),(0,_F,_d))
if mibBuilder.loadTexts:fsMIIpv6PmtuEntry.setStatus(_A)
class _FsMIIpv6PmtuDest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIIpv6PmtuDest_Type.__name__=_I
_FsMIIpv6PmtuDest_Object=MibTableColumn
fsMIIpv6PmtuDest=_FsMIIpv6PmtuDest_Object((1,3,6,1,4,1,10876,101,2,35,1,7,1,1),_FsMIIpv6PmtuDest_Type())
fsMIIpv6PmtuDest.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpv6PmtuDest.setStatus(_A)
_FsMIIpv6Pmtu_Type=Integer32
_FsMIIpv6Pmtu_Object=MibTableColumn
fsMIIpv6Pmtu=_FsMIIpv6Pmtu_Object((1,3,6,1,4,1,10876,101,2,35,1,7,1,2),_FsMIIpv6Pmtu_Type())
fsMIIpv6Pmtu.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6Pmtu.setStatus(_A)
_FsMIIpv6PmtuTimeStamp_Type=Integer32
_FsMIIpv6PmtuTimeStamp_Object=MibTableColumn
fsMIIpv6PmtuTimeStamp=_FsMIIpv6PmtuTimeStamp_Object((1,3,6,1,4,1,10876,101,2,35,1,7,1,3),_FsMIIpv6PmtuTimeStamp_Type())
fsMIIpv6PmtuTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6PmtuTimeStamp.setStatus(_A)
class _FsMIIpv6PmtuAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_O,2)))
_FsMIIpv6PmtuAdminStatus_Type.__name__=_D
_FsMIIpv6PmtuAdminStatus_Object=MibTableColumn
fsMIIpv6PmtuAdminStatus=_FsMIIpv6PmtuAdminStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,7,1,4),_FsMIIpv6PmtuAdminStatus_Type())
fsMIIpv6PmtuAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6PmtuAdminStatus.setStatus(_A)
_FsMIIpv6NDProxyListTable_Object=MibTable
fsMIIpv6NDProxyListTable=_FsMIIpv6NDProxyListTable_Object((1,3,6,1,4,1,10876,101,2,35,1,9))
if mibBuilder.loadTexts:fsMIIpv6NDProxyListTable.setStatus(_A)
_FsMIIpv6NDProxyListEntry_Object=MibTableRow
fsMIIpv6NDProxyListEntry=_FsMIIpv6NDProxyListEntry_Object((1,3,6,1,4,1,10876,101,2,35,1,9,1))
fsMIIpv6NDProxyListEntry.setIndexNames((0,_J,_L),(0,_F,_e))
if mibBuilder.loadTexts:fsMIIpv6NDProxyListEntry.setStatus(_A)
class _FsMIIpv6NDProxyAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIIpv6NDProxyAddr_Type.__name__=_I
_FsMIIpv6NDProxyAddr_Object=MibTableColumn
fsMIIpv6NDProxyAddr=_FsMIIpv6NDProxyAddr_Object((1,3,6,1,4,1,10876,101,2,35,1,9,1,1),_FsMIIpv6NDProxyAddr_Type())
fsMIIpv6NDProxyAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpv6NDProxyAddr.setStatus(_A)
class _FsMIIpv6NDProxyAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_O,2)))
_FsMIIpv6NDProxyAdminStatus_Type.__name__=_D
_FsMIIpv6NDProxyAdminStatus_Object=MibTableColumn
fsMIIpv6NDProxyAdminStatus=_FsMIIpv6NDProxyAdminStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,9,1,2),_FsMIIpv6NDProxyAdminStatus_Type())
fsMIIpv6NDProxyAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6NDProxyAdminStatus.setStatus(_A)
_FsMIIpv6PingTable_Object=MibTable
fsMIIpv6PingTable=_FsMIIpv6PingTable_Object((1,3,6,1,4,1,10876,101,2,35,1,10))
if mibBuilder.loadTexts:fsMIIpv6PingTable.setStatus(_A)
_FsMIIpv6PingEntry_Object=MibTableRow
fsMIIpv6PingEntry=_FsMIIpv6PingEntry_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1))
fsMIIpv6PingEntry.setIndexNames((0,_F,_g))
if mibBuilder.loadTexts:fsMIIpv6PingEntry.setStatus(_A)
class _FsMIIpv6PingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_FsMIIpv6PingIndex_Type.__name__=_D
_FsMIIpv6PingIndex_Object=MibTableColumn
fsMIIpv6PingIndex=_FsMIIpv6PingIndex_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,1),_FsMIIpv6PingIndex_Type())
fsMIIpv6PingIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpv6PingIndex.setStatus(_A)
class _FsMIIpv6PingDest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIIpv6PingDest_Type.__name__=_I
_FsMIIpv6PingDest_Object=MibTableColumn
fsMIIpv6PingDest=_FsMIIpv6PingDest_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,2),_FsMIIpv6PingDest_Type())
fsMIIpv6PingDest.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6PingDest.setStatus(_A)
_FsMIIpv6PingIfIndex_Type=InterfaceIndex
_FsMIIpv6PingIfIndex_Object=MibTableColumn
fsMIIpv6PingIfIndex=_FsMIIpv6PingIfIndex_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,3),_FsMIIpv6PingIfIndex_Type())
fsMIIpv6PingIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6PingIfIndex.setStatus(_A)
class _FsMIIpv6PingContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIIpv6PingContextId_Type.__name__=_D
_FsMIIpv6PingContextId_Object=MibTableColumn
fsMIIpv6PingContextId=_FsMIIpv6PingContextId_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,4),_FsMIIpv6PingContextId_Type())
fsMIIpv6PingContextId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6PingContextId.setStatus(_A)
class _FsMIIpv6PingAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),(_P,2),(_O,3),(_f,4)))
_FsMIIpv6PingAdminStatus_Type.__name__=_D
_FsMIIpv6PingAdminStatus_Object=MibTableColumn
fsMIIpv6PingAdminStatus=_FsMIIpv6PingAdminStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,5),_FsMIIpv6PingAdminStatus_Type())
fsMIIpv6PingAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6PingAdminStatus.setStatus(_A)
class _FsMIIpv6PingInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_FsMIIpv6PingInterval_Type.__name__=_D
_FsMIIpv6PingInterval_Object=MibTableColumn
fsMIIpv6PingInterval=_FsMIIpv6PingInterval_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,6),_FsMIIpv6PingInterval_Type())
fsMIIpv6PingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6PingInterval.setStatus(_A)
class _FsMIIpv6PingRcvTimeout_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsMIIpv6PingRcvTimeout_Type.__name__=_D
_FsMIIpv6PingRcvTimeout_Object=MibTableColumn
fsMIIpv6PingRcvTimeout=_FsMIIpv6PingRcvTimeout_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,7),_FsMIIpv6PingRcvTimeout_Type())
fsMIIpv6PingRcvTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6PingRcvTimeout.setStatus(_A)
class _FsMIIpv6PingTries_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_FsMIIpv6PingTries_Type.__name__=_D
_FsMIIpv6PingTries_Object=MibTableColumn
fsMIIpv6PingTries=_FsMIIpv6PingTries_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,8),_FsMIIpv6PingTries_Type())
fsMIIpv6PingTries.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6PingTries.setStatus(_A)
class _FsMIIpv6PingSize_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,2080))
_FsMIIpv6PingSize_Type.__name__=_D
_FsMIIpv6PingSize_Object=MibTableColumn
fsMIIpv6PingSize=_FsMIIpv6PingSize_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,9),_FsMIIpv6PingSize_Type())
fsMIIpv6PingSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6PingSize.setStatus(_A)
_FsMIIpv6PingSentCount_Type=Integer32
_FsMIIpv6PingSentCount_Object=MibTableColumn
fsMIIpv6PingSentCount=_FsMIIpv6PingSentCount_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,10),_FsMIIpv6PingSentCount_Type())
fsMIIpv6PingSentCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6PingSentCount.setStatus(_A)
_FsMIIpv6PingAverageTime_Type=Integer32
_FsMIIpv6PingAverageTime_Object=MibTableColumn
fsMIIpv6PingAverageTime=_FsMIIpv6PingAverageTime_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,11),_FsMIIpv6PingAverageTime_Type())
fsMIIpv6PingAverageTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6PingAverageTime.setStatus(_A)
_FsMIIpv6PingMaxTime_Type=Integer32
_FsMIIpv6PingMaxTime_Object=MibTableColumn
fsMIIpv6PingMaxTime=_FsMIIpv6PingMaxTime_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,12),_FsMIIpv6PingMaxTime_Type())
fsMIIpv6PingMaxTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6PingMaxTime.setStatus(_A)
_FsMIIpv6PingMinTime_Type=Integer32
_FsMIIpv6PingMinTime_Object=MibTableColumn
fsMIIpv6PingMinTime=_FsMIIpv6PingMinTime_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,13),_FsMIIpv6PingMinTime_Type())
fsMIIpv6PingMinTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6PingMinTime.setStatus(_A)
class _FsMIIpv6PingOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inprogress',1),('notinprogress',2)))
_FsMIIpv6PingOperStatus_Type.__name__=_D
_FsMIIpv6PingOperStatus_Object=MibTableColumn
fsMIIpv6PingOperStatus=_FsMIIpv6PingOperStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,14),_FsMIIpv6PingOperStatus_Type())
fsMIIpv6PingOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6PingOperStatus.setStatus(_A)
_FsMIIpv6PingSuccesses_Type=Counter32
_FsMIIpv6PingSuccesses_Object=MibTableColumn
fsMIIpv6PingSuccesses=_FsMIIpv6PingSuccesses_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,15),_FsMIIpv6PingSuccesses_Type())
fsMIIpv6PingSuccesses.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6PingSuccesses.setStatus(_A)
_FsMIIpv6PingPercentageLoss_Type=Integer32
_FsMIIpv6PingPercentageLoss_Object=MibTableColumn
fsMIIpv6PingPercentageLoss=_FsMIIpv6PingPercentageLoss_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,16),_FsMIIpv6PingPercentageLoss_Type())
fsMIIpv6PingPercentageLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6PingPercentageLoss.setStatus(_A)
class _FsMIIpv6PingData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_FsMIIpv6PingData_Type.__name__=_I
_FsMIIpv6PingData_Object=MibTableColumn
fsMIIpv6PingData=_FsMIIpv6PingData_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,17),_FsMIIpv6PingData_Type())
fsMIIpv6PingData.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6PingData.setStatus(_A)
class _FsMIIpv6PingSrcAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIIpv6PingSrcAddr_Type.__name__=_I
_FsMIIpv6PingSrcAddr_Object=MibTableColumn
fsMIIpv6PingSrcAddr=_FsMIIpv6PingSrcAddr_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,18),_FsMIIpv6PingSrcAddr_Type())
fsMIIpv6PingSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6PingSrcAddr.setStatus(_A)
_FsMIIpv6PingZoneId_Type=DisplayString
_FsMIIpv6PingZoneId_Object=MibTableColumn
fsMIIpv6PingZoneId=_FsMIIpv6PingZoneId_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,19),_FsMIIpv6PingZoneId_Type())
fsMIIpv6PingZoneId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6PingZoneId.setStatus(_A)
class _FsMIIpv6PingDestAddrType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*(('other',0),(_R,2)))
_FsMIIpv6PingDestAddrType_Type.__name__=_D
_FsMIIpv6PingDestAddrType_Object=MibTableColumn
fsMIIpv6PingDestAddrType=_FsMIIpv6PingDestAddrType_Object((1,3,6,1,4,1,10876,101,2,35,1,10,1,20),_FsMIIpv6PingDestAddrType_Type())
fsMIIpv6PingDestAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6PingDestAddrType.setStatus(_A)
_FsMIIpv6GlobalDebug_Type=Unsigned32
_FsMIIpv6GlobalDebug_Object=MibScalar
fsMIIpv6GlobalDebug=_FsMIIpv6GlobalDebug_Object((1,3,6,1,4,1,10876,101,2,35,1,11),_FsMIIpv6GlobalDebug_Type())
fsMIIpv6GlobalDebug.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6GlobalDebug.setStatus(_A)
_FsMIIpv6AddrSelPolicyTable_Object=MibTable
fsMIIpv6AddrSelPolicyTable=_FsMIIpv6AddrSelPolicyTable_Object((1,3,6,1,4,1,10876,101,2,35,1,12))
if mibBuilder.loadTexts:fsMIIpv6AddrSelPolicyTable.setStatus(_A)
_FsMIIpv6AddrSelPolicyEntry_Object=MibTableRow
fsMIIpv6AddrSelPolicyEntry=_FsMIIpv6AddrSelPolicyEntry_Object((1,3,6,1,4,1,10876,101,2,35,1,12,1))
fsMIIpv6AddrSelPolicyEntry.setIndexNames((0,_F,_h),(0,_F,_i),(0,_F,_j))
if mibBuilder.loadTexts:fsMIIpv6AddrSelPolicyEntry.setStatus(_A)
class _FsMIIpv6AddrSelPolicyPrefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIIpv6AddrSelPolicyPrefix_Type.__name__=_I
_FsMIIpv6AddrSelPolicyPrefix_Object=MibTableColumn
fsMIIpv6AddrSelPolicyPrefix=_FsMIIpv6AddrSelPolicyPrefix_Object((1,3,6,1,4,1,10876,101,2,35,1,12,1,1),_FsMIIpv6AddrSelPolicyPrefix_Type())
fsMIIpv6AddrSelPolicyPrefix.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpv6AddrSelPolicyPrefix.setStatus(_A)
class _FsMIIpv6AddrSelPolicyPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_FsMIIpv6AddrSelPolicyPrefixLen_Type.__name__=_D
_FsMIIpv6AddrSelPolicyPrefixLen_Object=MibTableColumn
fsMIIpv6AddrSelPolicyPrefixLen=_FsMIIpv6AddrSelPolicyPrefixLen_Object((1,3,6,1,4,1,10876,101,2,35,1,12,1,2),_FsMIIpv6AddrSelPolicyPrefixLen_Type())
fsMIIpv6AddrSelPolicyPrefixLen.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpv6AddrSelPolicyPrefixLen.setStatus(_A)
_FsMIIpv6AddrSelPolicyIfIndex_Type=InterfaceIndex
_FsMIIpv6AddrSelPolicyIfIndex_Object=MibTableColumn
fsMIIpv6AddrSelPolicyIfIndex=_FsMIIpv6AddrSelPolicyIfIndex_Object((1,3,6,1,4,1,10876,101,2,35,1,12,1,3),_FsMIIpv6AddrSelPolicyIfIndex_Type())
fsMIIpv6AddrSelPolicyIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpv6AddrSelPolicyIfIndex.setStatus(_A)
class _FsMIIpv6AddrSelPolicyScope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsMIIpv6AddrSelPolicyScope_Type.__name__=_D
_FsMIIpv6AddrSelPolicyScope_Object=MibTableColumn
fsMIIpv6AddrSelPolicyScope=_FsMIIpv6AddrSelPolicyScope_Object((1,3,6,1,4,1,10876,101,2,35,1,12,1,4),_FsMIIpv6AddrSelPolicyScope_Type())
fsMIIpv6AddrSelPolicyScope.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6AddrSelPolicyScope.setStatus(_A)
class _FsMIIpv6AddrSelPolicyPrecedence_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_FsMIIpv6AddrSelPolicyPrecedence_Type.__name__=_D
_FsMIIpv6AddrSelPolicyPrecedence_Object=MibTableColumn
fsMIIpv6AddrSelPolicyPrecedence=_FsMIIpv6AddrSelPolicyPrecedence_Object((1,3,6,1,4,1,10876,101,2,35,1,12,1,5),_FsMIIpv6AddrSelPolicyPrecedence_Type())
fsMIIpv6AddrSelPolicyPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6AddrSelPolicyPrecedence.setStatus(_A)
class _FsMIIpv6AddrSelPolicyLabel_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIIpv6AddrSelPolicyLabel_Type.__name__=_D
_FsMIIpv6AddrSelPolicyLabel_Object=MibTableColumn
fsMIIpv6AddrSelPolicyLabel=_FsMIIpv6AddrSelPolicyLabel_Object((1,3,6,1,4,1,10876,101,2,35,1,12,1,6),_FsMIIpv6AddrSelPolicyLabel_Type())
fsMIIpv6AddrSelPolicyLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6AddrSelPolicyLabel.setStatus(_A)
class _FsMIIpv6AddrSelPolicyAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),(_R,2),('multicast',3)))
_FsMIIpv6AddrSelPolicyAddrType_Type.__name__=_D
_FsMIIpv6AddrSelPolicyAddrType_Object=MibTableColumn
fsMIIpv6AddrSelPolicyAddrType=_FsMIIpv6AddrSelPolicyAddrType_Object((1,3,6,1,4,1,10876,101,2,35,1,12,1,7),_FsMIIpv6AddrSelPolicyAddrType_Type())
fsMIIpv6AddrSelPolicyAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6AddrSelPolicyAddrType.setStatus(_A)
class _FsMIIpv6AddrSelPolicyIsPublicAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_FsMIIpv6AddrSelPolicyIsPublicAddr_Type.__name__=_D
_FsMIIpv6AddrSelPolicyIsPublicAddr_Object=MibTableColumn
fsMIIpv6AddrSelPolicyIsPublicAddr=_FsMIIpv6AddrSelPolicyIsPublicAddr_Object((1,3,6,1,4,1,10876,101,2,35,1,12,1,8),_FsMIIpv6AddrSelPolicyIsPublicAddr_Type())
fsMIIpv6AddrSelPolicyIsPublicAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6AddrSelPolicyIsPublicAddr.setStatus(_A)
class _FsMIIpv6AddrSelPolicyIsSelfAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_FsMIIpv6AddrSelPolicyIsSelfAddr_Type.__name__=_D
_FsMIIpv6AddrSelPolicyIsSelfAddr_Object=MibTableColumn
fsMIIpv6AddrSelPolicyIsSelfAddr=_FsMIIpv6AddrSelPolicyIsSelfAddr_Object((1,3,6,1,4,1,10876,101,2,35,1,12,1,9),_FsMIIpv6AddrSelPolicyIsSelfAddr_Type())
fsMIIpv6AddrSelPolicyIsSelfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6AddrSelPolicyIsSelfAddr.setStatus(_A)
class _FsMIIpv6AddrSelPolicyReachabilityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reachable',1),('unreachable',2)))
_FsMIIpv6AddrSelPolicyReachabilityStatus_Type.__name__=_D
_FsMIIpv6AddrSelPolicyReachabilityStatus_Object=MibTableColumn
fsMIIpv6AddrSelPolicyReachabilityStatus=_FsMIIpv6AddrSelPolicyReachabilityStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,12,1,10),_FsMIIpv6AddrSelPolicyReachabilityStatus_Type())
fsMIIpv6AddrSelPolicyReachabilityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6AddrSelPolicyReachabilityStatus.setStatus(_A)
class _FsMIIpv6AddrSelPolicyConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('management',2)))
_FsMIIpv6AddrSelPolicyConfigStatus_Type.__name__=_D
_FsMIIpv6AddrSelPolicyConfigStatus_Object=MibTableColumn
fsMIIpv6AddrSelPolicyConfigStatus=_FsMIIpv6AddrSelPolicyConfigStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,12,1,11),_FsMIIpv6AddrSelPolicyConfigStatus_Type())
fsMIIpv6AddrSelPolicyConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6AddrSelPolicyConfigStatus.setStatus(_A)
_FsMIIpv6AddrSelPolicyRowStatus_Type=RowStatus
_FsMIIpv6AddrSelPolicyRowStatus_Object=MibTableColumn
fsMIIpv6AddrSelPolicyRowStatus=_FsMIIpv6AddrSelPolicyRowStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,12,1,12),_FsMIIpv6AddrSelPolicyRowStatus_Type())
fsMIIpv6AddrSelPolicyRowStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsMIIpv6AddrSelPolicyRowStatus.setStatus(_A)
_FsMIIpv6IfScopeZoneMapTable_Object=MibTable
fsMIIpv6IfScopeZoneMapTable=_FsMIIpv6IfScopeZoneMapTable_Object((1,3,6,1,4,1,10876,101,2,35,1,13))
if mibBuilder.loadTexts:fsMIIpv6IfScopeZoneMapTable.setStatus(_A)
_FsMIIpv6IfScopeZoneMapEntry_Object=MibTableRow
fsMIIpv6IfScopeZoneMapEntry=_FsMIIpv6IfScopeZoneMapEntry_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1))
fsMIIpv6IfScopeZoneMapEntry.setIndexNames((0,_F,_k))
if mibBuilder.loadTexts:fsMIIpv6IfScopeZoneMapEntry.setStatus(_A)
_FsMIIpv6ScopeZoneIndexIfIndex_Type=InterfaceIndex
_FsMIIpv6ScopeZoneIndexIfIndex_Object=MibTableColumn
fsMIIpv6ScopeZoneIndexIfIndex=_FsMIIpv6ScopeZoneIndexIfIndex_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,1),_FsMIIpv6ScopeZoneIndexIfIndex_Type())
fsMIIpv6ScopeZoneIndexIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndexIfIndex.setStatus(_A)
class _FsMIIpv6ScopeZoneIndexInterfaceLocal_Type(DisplayString):defaultValue=OctetString(_G)
_FsMIIpv6ScopeZoneIndexInterfaceLocal_Type.__name__=_E
_FsMIIpv6ScopeZoneIndexInterfaceLocal_Object=MibTableColumn
fsMIIpv6ScopeZoneIndexInterfaceLocal=_FsMIIpv6ScopeZoneIndexInterfaceLocal_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,2),_FsMIIpv6ScopeZoneIndexInterfaceLocal_Type())
fsMIIpv6ScopeZoneIndexInterfaceLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndexInterfaceLocal.setStatus(_A)
class _FsMIIpv6ScopeZoneIndexLinkLocal_Type(DisplayString):defaultValue=OctetString(_G)
_FsMIIpv6ScopeZoneIndexLinkLocal_Type.__name__=_E
_FsMIIpv6ScopeZoneIndexLinkLocal_Object=MibTableColumn
fsMIIpv6ScopeZoneIndexLinkLocal=_FsMIIpv6ScopeZoneIndexLinkLocal_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,3),_FsMIIpv6ScopeZoneIndexLinkLocal_Type())
fsMIIpv6ScopeZoneIndexLinkLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndexLinkLocal.setStatus(_A)
class _FsMIIpv6ScopeZoneIndex3_Type(DisplayString):defaultValue=OctetString(_G)
_FsMIIpv6ScopeZoneIndex3_Type.__name__=_E
_FsMIIpv6ScopeZoneIndex3_Object=MibTableColumn
fsMIIpv6ScopeZoneIndex3=_FsMIIpv6ScopeZoneIndex3_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,4),_FsMIIpv6ScopeZoneIndex3_Type())
fsMIIpv6ScopeZoneIndex3.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndex3.setStatus(_A)
class _FsMIIpv6ScopeZoneIndexAdminLocal_Type(DisplayString):defaultValue=OctetString(_G)
_FsMIIpv6ScopeZoneIndexAdminLocal_Type.__name__=_E
_FsMIIpv6ScopeZoneIndexAdminLocal_Object=MibTableColumn
fsMIIpv6ScopeZoneIndexAdminLocal=_FsMIIpv6ScopeZoneIndexAdminLocal_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,5),_FsMIIpv6ScopeZoneIndexAdminLocal_Type())
fsMIIpv6ScopeZoneIndexAdminLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndexAdminLocal.setStatus(_A)
class _FsMIIpv6ScopeZoneIndexSiteLocal_Type(DisplayString):defaultValue=OctetString(_G)
_FsMIIpv6ScopeZoneIndexSiteLocal_Type.__name__=_E
_FsMIIpv6ScopeZoneIndexSiteLocal_Object=MibTableColumn
fsMIIpv6ScopeZoneIndexSiteLocal=_FsMIIpv6ScopeZoneIndexSiteLocal_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,6),_FsMIIpv6ScopeZoneIndexSiteLocal_Type())
fsMIIpv6ScopeZoneIndexSiteLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndexSiteLocal.setStatus(_A)
class _FsMIIpv6ScopeZoneIndex6_Type(DisplayString):defaultValue=OctetString(_G)
_FsMIIpv6ScopeZoneIndex6_Type.__name__=_E
_FsMIIpv6ScopeZoneIndex6_Object=MibTableColumn
fsMIIpv6ScopeZoneIndex6=_FsMIIpv6ScopeZoneIndex6_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,7),_FsMIIpv6ScopeZoneIndex6_Type())
fsMIIpv6ScopeZoneIndex6.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndex6.setStatus(_A)
class _FsMIIpv6ScopeZoneIndex7_Type(DisplayString):defaultValue=OctetString(_G)
_FsMIIpv6ScopeZoneIndex7_Type.__name__=_E
_FsMIIpv6ScopeZoneIndex7_Object=MibTableColumn
fsMIIpv6ScopeZoneIndex7=_FsMIIpv6ScopeZoneIndex7_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,8),_FsMIIpv6ScopeZoneIndex7_Type())
fsMIIpv6ScopeZoneIndex7.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndex7.setStatus(_A)
class _FsMIIpv6ScopeZoneIndexOrganizationLocal_Type(DisplayString):defaultValue=OctetString(_G)
_FsMIIpv6ScopeZoneIndexOrganizationLocal_Type.__name__=_E
_FsMIIpv6ScopeZoneIndexOrganizationLocal_Object=MibTableColumn
fsMIIpv6ScopeZoneIndexOrganizationLocal=_FsMIIpv6ScopeZoneIndexOrganizationLocal_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,9),_FsMIIpv6ScopeZoneIndexOrganizationLocal_Type())
fsMIIpv6ScopeZoneIndexOrganizationLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndexOrganizationLocal.setStatus(_A)
class _FsMIIpv6ScopeZoneIndex9_Type(DisplayString):defaultValue=OctetString(_G)
_FsMIIpv6ScopeZoneIndex9_Type.__name__=_E
_FsMIIpv6ScopeZoneIndex9_Object=MibTableColumn
fsMIIpv6ScopeZoneIndex9=_FsMIIpv6ScopeZoneIndex9_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,10),_FsMIIpv6ScopeZoneIndex9_Type())
fsMIIpv6ScopeZoneIndex9.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndex9.setStatus(_A)
class _FsMIIpv6ScopeZoneIndexA_Type(DisplayString):defaultValue=OctetString(_G)
_FsMIIpv6ScopeZoneIndexA_Type.__name__=_E
_FsMIIpv6ScopeZoneIndexA_Object=MibTableColumn
fsMIIpv6ScopeZoneIndexA=_FsMIIpv6ScopeZoneIndexA_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,11),_FsMIIpv6ScopeZoneIndexA_Type())
fsMIIpv6ScopeZoneIndexA.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndexA.setStatus(_A)
class _FsMIIpv6ScopeZoneIndexB_Type(DisplayString):defaultValue=OctetString(_G)
_FsMIIpv6ScopeZoneIndexB_Type.__name__=_E
_FsMIIpv6ScopeZoneIndexB_Object=MibTableColumn
fsMIIpv6ScopeZoneIndexB=_FsMIIpv6ScopeZoneIndexB_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,12),_FsMIIpv6ScopeZoneIndexB_Type())
fsMIIpv6ScopeZoneIndexB.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndexB.setStatus(_A)
class _FsMIIpv6ScopeZoneIndexC_Type(DisplayString):defaultValue=OctetString(_G)
_FsMIIpv6ScopeZoneIndexC_Type.__name__=_E
_FsMIIpv6ScopeZoneIndexC_Object=MibTableColumn
fsMIIpv6ScopeZoneIndexC=_FsMIIpv6ScopeZoneIndexC_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,13),_FsMIIpv6ScopeZoneIndexC_Type())
fsMIIpv6ScopeZoneIndexC.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndexC.setStatus(_A)
class _FsMIIpv6ScopeZoneIndexD_Type(DisplayString):defaultValue=OctetString(_G)
_FsMIIpv6ScopeZoneIndexD_Type.__name__=_E
_FsMIIpv6ScopeZoneIndexD_Object=MibTableColumn
fsMIIpv6ScopeZoneIndexD=_FsMIIpv6ScopeZoneIndexD_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,14),_FsMIIpv6ScopeZoneIndexD_Type())
fsMIIpv6ScopeZoneIndexD.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndexD.setStatus(_A)
class _FsMIIpv6ScopeZoneIndexE_Type(DisplayString):defaultValue=OctetString(_G)
_FsMIIpv6ScopeZoneIndexE_Type.__name__=_E
_FsMIIpv6ScopeZoneIndexE_Object=MibTableColumn
fsMIIpv6ScopeZoneIndexE=_FsMIIpv6ScopeZoneIndexE_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,15),_FsMIIpv6ScopeZoneIndexE_Type())
fsMIIpv6ScopeZoneIndexE.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndexE.setStatus(_A)
class _FsMIIpv6IfScopeZoneCreationStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notcreated',0),(_T,1),('mgmt',2),(_l,3)))
_FsMIIpv6IfScopeZoneCreationStatus_Type.__name__=_D
_FsMIIpv6IfScopeZoneCreationStatus_Object=MibTableColumn
fsMIIpv6IfScopeZoneCreationStatus=_FsMIIpv6IfScopeZoneCreationStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,16),_FsMIIpv6IfScopeZoneCreationStatus_Type())
fsMIIpv6IfScopeZoneCreationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6IfScopeZoneCreationStatus.setStatus(_A)
_FsMIIpv6IfScopeZoneRowStatus_Type=RowStatus
_FsMIIpv6IfScopeZoneRowStatus_Object=MibTableColumn
fsMIIpv6IfScopeZoneRowStatus=_FsMIIpv6IfScopeZoneRowStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,13,1,17),_FsMIIpv6IfScopeZoneRowStatus_Type())
fsMIIpv6IfScopeZoneRowStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsMIIpv6IfScopeZoneRowStatus.setStatus(_A)
_FsMIIpv6ScopeZoneTable_Object=MibTable
fsMIIpv6ScopeZoneTable=_FsMIIpv6ScopeZoneTable_Object((1,3,6,1,4,1,10876,101,2,35,1,14))
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneTable.setStatus(_A)
_FsMIIpv6ScopeZoneEntry_Object=MibTableRow
fsMIIpv6ScopeZoneEntry=_FsMIIpv6ScopeZoneEntry_Object((1,3,6,1,4,1,10876,101,2,35,1,14,1))
fsMIIpv6ScopeZoneEntry.setIndexNames((0,_F,_m),(0,_F,_n))
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneEntry.setStatus(_A)
class _FsMIIpv6ScopeZoneContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIIpv6ScopeZoneContextId_Type.__name__=_D
_FsMIIpv6ScopeZoneContextId_Object=MibTableColumn
fsMIIpv6ScopeZoneContextId=_FsMIIpv6ScopeZoneContextId_Object((1,3,6,1,4,1,10876,101,2,35,1,14,1,1),_FsMIIpv6ScopeZoneContextId_Type())
fsMIIpv6ScopeZoneContextId.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneContextId.setStatus(_A)
_FsMIIpv6ScopeZoneName_Type=DisplayString
_FsMIIpv6ScopeZoneName_Object=MibTableColumn
fsMIIpv6ScopeZoneName=_FsMIIpv6ScopeZoneName_Object((1,3,6,1,4,1,10876,101,2,35,1,14,1,2),_FsMIIpv6ScopeZoneName_Type())
fsMIIpv6ScopeZoneName.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneName.setStatus(_A)
_FsMIIpv6ScopeZoneIndex_Type=InetZoneIndex
_FsMIIpv6ScopeZoneIndex_Object=MibTableColumn
fsMIIpv6ScopeZoneIndex=_FsMIIpv6ScopeZoneIndex_Object((1,3,6,1,4,1,10876,101,2,35,1,14,1,3),_FsMIIpv6ScopeZoneIndex_Type())
fsMIIpv6ScopeZoneIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneIndex.setStatus(_A)
class _FsMIIpv6ScopeZoneCreationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),('mgmt',2),(_l,3)))
_FsMIIpv6ScopeZoneCreationStatus_Type.__name__=_D
_FsMIIpv6ScopeZoneCreationStatus_Object=MibTableColumn
fsMIIpv6ScopeZoneCreationStatus=_FsMIIpv6ScopeZoneCreationStatus_Object((1,3,6,1,4,1,10876,101,2,35,1,14,1,4),_FsMIIpv6ScopeZoneCreationStatus_Type())
fsMIIpv6ScopeZoneCreationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneCreationStatus.setStatus(_A)
_FsMIIpv6ScopeZoneInterfaceList_Type=InterfaceList
_FsMIIpv6ScopeZoneInterfaceList_Object=MibTableColumn
fsMIIpv6ScopeZoneInterfaceList=_FsMIIpv6ScopeZoneInterfaceList_Object((1,3,6,1,4,1,10876,101,2,35,1,14,1,5),_FsMIIpv6ScopeZoneInterfaceList_Type())
fsMIIpv6ScopeZoneInterfaceList.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6ScopeZoneInterfaceList.setStatus(_A)
class _FsMIIpv6IsDefaultScopeZone_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_FsMIIpv6IsDefaultScopeZone_Type.__name__=_D
_FsMIIpv6IsDefaultScopeZone_Object=MibTableColumn
fsMIIpv6IsDefaultScopeZone=_FsMIIpv6IsDefaultScopeZone_Object((1,3,6,1,4,1,10876,101,2,35,1,14,1,6),_FsMIIpv6IsDefaultScopeZone_Type())
fsMIIpv6IsDefaultScopeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6IsDefaultScopeZone.setStatus(_A)
_FsMIipv6Route_ObjectIdentity=ObjectIdentity
fsMIipv6Route=_FsMIipv6Route_ObjectIdentity((1,3,6,1,4,1,10876,101,2,35,2))
_FsMIIpv6PrefTable_Object=MibTable
fsMIIpv6PrefTable=_FsMIIpv6PrefTable_Object((1,3,6,1,4,1,10876,101,2,35,2,1))
if mibBuilder.loadTexts:fsMIIpv6PrefTable.setStatus(_A)
_FsMIIpv6PrefEntry_Object=MibTableRow
fsMIIpv6PrefEntry=_FsMIIpv6PrefEntry_Object((1,3,6,1,4,1,10876,101,2,35,2,1,1))
fsMIIpv6PrefEntry.setIndexNames((0,_J,_L),(0,_F,_o))
if mibBuilder.loadTexts:fsMIIpv6PrefEntry.setStatus(_A)
class _FsMIIpv6Protocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('other',1),('local',2),('netmgmt',3),('ndisc',4),('rip',5),('ospf',6),('bgp',7),('idrp',8),('igrp',9)))
_FsMIIpv6Protocol_Type.__name__=_D
_FsMIIpv6Protocol_Object=MibTableColumn
fsMIIpv6Protocol=_FsMIIpv6Protocol_Object((1,3,6,1,4,1,10876,101,2,35,2,1,1,1),_FsMIIpv6Protocol_Type())
fsMIIpv6Protocol.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpv6Protocol.setStatus(_A)
class _FsMIIpv6Preference_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIIpv6Preference_Type.__name__=_K
_FsMIIpv6Preference_Object=MibTableColumn
fsMIIpv6Preference=_FsMIIpv6Preference_Object((1,3,6,1,4,1,10876,101,2,35,2,1,1,2),_FsMIIpv6Preference_Type())
fsMIIpv6Preference.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpv6Preference.setStatus(_A)
_FsMIIpv6Test_ObjectIdentity=ObjectIdentity
fsMIIpv6Test=_FsMIIpv6Test_ObjectIdentity((1,3,6,1,4,1,10876,101,2,35,3))
_FsMIIpv6TestRedEntryTime_Type=Integer32
_FsMIIpv6TestRedEntryTime_Object=MibScalar
fsMIIpv6TestRedEntryTime=_FsMIIpv6TestRedEntryTime_Object((1,3,6,1,4,1,10876,101,2,35,3,1),_FsMIIpv6TestRedEntryTime_Type())
fsMIIpv6TestRedEntryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6TestRedEntryTime.setStatus(_A)
_FsMIIpv6TestRedExitTime_Type=Integer32
_FsMIIpv6TestRedExitTime_Object=MibScalar
fsMIIpv6TestRedExitTime=_FsMIIpv6TestRedExitTime_Object((1,3,6,1,4,1,10876,101,2,35,3,2),_FsMIIpv6TestRedExitTime_Type())
fsMIIpv6TestRedExitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpv6TestRedExitTime.setStatus(_A)
fsMIStdIpv6InterfaceEntry.registerAugmentions((_F,_p))
fsMIIpv6IfEntry.setIndexNames(*fsMIStdIpv6InterfaceEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'InterfaceList':InterfaceList,'fsMIipv6MIB':fsMIipv6MIB,'fsMIipv6':fsMIipv6,'fsMIIpv6ContextTable':fsMIIpv6ContextTable,'fsMIIpv6ContextEntry':fsMIIpv6ContextEntry,'fsMIIpv6NdCacheMaxRetries':fsMIIpv6NdCacheMaxRetries,'fsMIIpv6PmtuConfigStatus':fsMIIpv6PmtuConfigStatus,'fsMIIpv6PmtuTimeOutInterval':fsMIIpv6PmtuTimeOutInterval,'fsMIIpv6JumboEnable':fsMIIpv6JumboEnable,'fsMIIpv6NumOfSendJumbo':fsMIIpv6NumOfSendJumbo,'fsMIIpv6NumOfRecvJumbo':fsMIIpv6NumOfRecvJumbo,'fsMIIpv6ErrJumbo':fsMIIpv6ErrJumbo,'fsMIIpv6ContextDebug':fsMIIpv6ContextDebug,'fsMIIpv6RFC5095Compatibility':fsMIIpv6RFC5095Compatibility,'fsMIIpv6IfTable':fsMIIpv6IfTable,_p:fsMIIpv6IfEntry,'fsMIIpv6IfType':fsMIIpv6IfType,'fsMIIpv6IfPortNum':fsMIIpv6IfPortNum,'fsMIIpv6IfCircuitNum':fsMIIpv6IfCircuitNum,'fsMIIpv6IfToken':fsMIIpv6IfToken,'fsMIIpv6IfOperStatus':fsMIIpv6IfOperStatus,'fsMIIpv6IfRouterAdvStatus':fsMIIpv6IfRouterAdvStatus,'fsMIIpv6IfRouterAdvFlags':fsMIIpv6IfRouterAdvFlags,'fsMIIpv6IfHopLimit':fsMIIpv6IfHopLimit,'fsMIIpv6IfDefRouterTime':fsMIIpv6IfDefRouterTime,'fsMIIpv6IfReachableTime':fsMIIpv6IfReachableTime,'fsMIIpv6IfRetransmitTime':fsMIIpv6IfRetransmitTime,'fsMIIpv6IfDelayProbeTime':fsMIIpv6IfDelayProbeTime,'fsMIIpv6IfPrefixAdvStatus':fsMIIpv6IfPrefixAdvStatus,'fsMIIpv6IfMinRouterAdvTime':fsMIIpv6IfMinRouterAdvTime,'fsMIIpv6IfMaxRouterAdvTime':fsMIIpv6IfMaxRouterAdvTime,'fsMIIpv6IfDADRetries':fsMIIpv6IfDADRetries,'fsMIIpv6IfForwarding':fsMIIpv6IfForwarding,'fsMIIpv6IfRoutingStatus':fsMIIpv6IfRoutingStatus,'fsMIIpv6IfIcmpErrInterval':fsMIIpv6IfIcmpErrInterval,'fsMIIpv6IfIcmpTokenBucketSize':fsMIIpv6IfIcmpTokenBucketSize,'fsMIIpv6IfDestUnreachableMsg':fsMIIpv6IfDestUnreachableMsg,'fsMIIpv6IfStatsTable':fsMIIpv6IfStatsTable,'fsMIIpv6IfStatsEntry':fsMIIpv6IfStatsEntry,'fsMIIpv6IfStatsTooBigErrors':fsMIIpv6IfStatsTooBigErrors,'fsMIIpv6IfStatsInRouterSols':fsMIIpv6IfStatsInRouterSols,'fsMIIpv6IfStatsInRouterAdvs':fsMIIpv6IfStatsInRouterAdvs,'fsMIIpv6IfStatsInNeighSols':fsMIIpv6IfStatsInNeighSols,'fsMIIpv6IfStatsInNeighAdvs':fsMIIpv6IfStatsInNeighAdvs,'fsMIIpv6IfStatsInRedirects':fsMIIpv6IfStatsInRedirects,'fsMIIpv6IfStatsOutRouterSols':fsMIIpv6IfStatsOutRouterSols,'fsMIIpv6IfStatsOutRouterAdvs':fsMIIpv6IfStatsOutRouterAdvs,'fsMIIpv6IfStatsOutNeighSols':fsMIIpv6IfStatsOutNeighSols,'fsMIIpv6IfStatsOutNeighAdvs':fsMIIpv6IfStatsOutNeighAdvs,'fsMIIpv6IfStatsOutRedirects':fsMIIpv6IfStatsOutRedirects,'fsMIIpv6IfStatsLastRouterAdvTime':fsMIIpv6IfStatsLastRouterAdvTime,'fsMIIpv6IfStatsNextRouterAdvTime':fsMIIpv6IfStatsNextRouterAdvTime,'fsMIIpv6IfStatsIcmp6ErrRateLmtd':fsMIIpv6IfStatsIcmp6ErrRateLmtd,'fsMIIpv6AddrTable':fsMIIpv6AddrTable,'fsMIIpv6AddrEntry':fsMIIpv6AddrEntry,_Y:fsMIIpv6AddrAddress,_Z:fsMIIpv6AddrPrefixLen,'fsMIIpv6AddrAdminStatus':fsMIIpv6AddrAdminStatus,'fsMIIpv6AddrType':fsMIIpv6AddrType,'fsMIIpv6AddrProfIndex':fsMIIpv6AddrProfIndex,'fsMIIpv6AddrOperStatus':fsMIIpv6AddrOperStatus,'fsMIIpv6AddrContextId':fsMIIpv6AddrContextId,'fsMIIpv6AddrScope':fsMIIpv6AddrScope,'fsMIIpv6AddrProfileTable':fsMIIpv6AddrProfileTable,'fsMIIpv6AddrProfileEntry':fsMIIpv6AddrProfileEntry,_b:fsMIIpv6AddrProfileIndex,'fsMIIpv6AddrProfileStatus':fsMIIpv6AddrProfileStatus,'fsMIIpv6AddrProfilePrefixAdvStatus':fsMIIpv6AddrProfilePrefixAdvStatus,'fsMIIpv6AddrProfileOnLinkAdvStatus':fsMIIpv6AddrProfileOnLinkAdvStatus,'fsMIIpv6AddrProfileAutoConfAdvStatus':fsMIIpv6AddrProfileAutoConfAdvStatus,'fsMIIpv6AddrProfilePreferredTime':fsMIIpv6AddrProfilePreferredTime,'fsMIIpv6AddrProfileValidTime':fsMIIpv6AddrProfileValidTime,'fsMIIpv6AddrProfileValidLifeTimeFlag':fsMIIpv6AddrProfileValidLifeTimeFlag,'fsMIIpv6AddrProfilePreferredLifeTimeFlag':fsMIIpv6AddrProfilePreferredLifeTimeFlag,'fsMIIpv6IcmpStatsTable':fsMIIpv6IcmpStatsTable,'fsMIIpv6IcmpStatsEntry':fsMIIpv6IcmpStatsEntry,'fsMIIpv6IcmpInMsgs':fsMIIpv6IcmpInMsgs,'fsMIIpv6IcmpInErrors':fsMIIpv6IcmpInErrors,'fsMIIpv6IcmpInDestUnreachs':fsMIIpv6IcmpInDestUnreachs,'fsMIIpv6IcmpInTimeExcds':fsMIIpv6IcmpInTimeExcds,'fsMIIpv6IcmpInParmProbs':fsMIIpv6IcmpInParmProbs,'fsMIIpv6IcmpInPktTooBigs':fsMIIpv6IcmpInPktTooBigs,'fsMIIpv6IcmpInEchos':fsMIIpv6IcmpInEchos,'fsMIIpv6IcmpInEchoReps':fsMIIpv6IcmpInEchoReps,'fsMIIpv6IcmpInRouterSolicits':fsMIIpv6IcmpInRouterSolicits,'fsMIIpv6IcmpInRouterAdvertisements':fsMIIpv6IcmpInRouterAdvertisements,'fsMIIpv6IcmpInNeighborSolicits':fsMIIpv6IcmpInNeighborSolicits,'fsMIIpv6IcmpInNeighborAdvertisements':fsMIIpv6IcmpInNeighborAdvertisements,'fsMIIpv6IcmpInRedirects':fsMIIpv6IcmpInRedirects,'fsMIIpv6IcmpInAdminProhib':fsMIIpv6IcmpInAdminProhib,'fsMIIpv6IcmpOutMsgs':fsMIIpv6IcmpOutMsgs,'fsMIIpv6IcmpOutErrors':fsMIIpv6IcmpOutErrors,'fsMIIpv6IcmpOutDestUnreachs':fsMIIpv6IcmpOutDestUnreachs,'fsMIIpv6IcmpOutTimeExcds':fsMIIpv6IcmpOutTimeExcds,'fsMIIpv6IcmpOutParmProbs':fsMIIpv6IcmpOutParmProbs,'fsMIIpv6IcmpOutPktTooBigs':fsMIIpv6IcmpOutPktTooBigs,'fsMIIpv6IcmpOutEchos':fsMIIpv6IcmpOutEchos,'fsMIIpv6IcmpOutEchoReps':fsMIIpv6IcmpOutEchoReps,'fsMIIpv6IcmpOutRouterSolicits':fsMIIpv6IcmpOutRouterSolicits,'fsMIIpv6IcmpOutRouterAdvertisements':fsMIIpv6IcmpOutRouterAdvertisements,'fsMIIpv6IcmpOutNeighborSolicits':fsMIIpv6IcmpOutNeighborSolicits,'fsMIIpv6IcmpOutNeighborAdvertisements':fsMIIpv6IcmpOutNeighborAdvertisements,'fsMIIpv6IcmpOutRedirects':fsMIIpv6IcmpOutRedirects,'fsMIIpv6IcmpOutAdminProhib':fsMIIpv6IcmpOutAdminProhib,'fsMIIpv6IcmpInBadCode':fsMIIpv6IcmpInBadCode,'fsMIIpv6IcmpInNARouterFlagSet':fsMIIpv6IcmpInNARouterFlagSet,'fsMIIpv6IcmpInNASolicitedFlagSet':fsMIIpv6IcmpInNASolicitedFlagSet,'fsMIIpv6IcmpInNAOverrideFlagSet':fsMIIpv6IcmpInNAOverrideFlagSet,'fsMIIpv6IcmpOutNARouterFlagSet':fsMIIpv6IcmpOutNARouterFlagSet,'fsMIIpv6IcmpOutNASolicitedFlagSet':fsMIIpv6IcmpOutNASolicitedFlagSet,'fsMIIpv6IcmpOutNAOverrideFlagSet':fsMIIpv6IcmpOutNAOverrideFlagSet,'fsMIIpv6PmtuTable':fsMIIpv6PmtuTable,'fsMIIpv6PmtuEntry':fsMIIpv6PmtuEntry,_d:fsMIIpv6PmtuDest,'fsMIIpv6Pmtu':fsMIIpv6Pmtu,'fsMIIpv6PmtuTimeStamp':fsMIIpv6PmtuTimeStamp,'fsMIIpv6PmtuAdminStatus':fsMIIpv6PmtuAdminStatus,'fsMIIpv6NDProxyListTable':fsMIIpv6NDProxyListTable,'fsMIIpv6NDProxyListEntry':fsMIIpv6NDProxyListEntry,_e:fsMIIpv6NDProxyAddr,'fsMIIpv6NDProxyAdminStatus':fsMIIpv6NDProxyAdminStatus,'fsMIIpv6PingTable':fsMIIpv6PingTable,'fsMIIpv6PingEntry':fsMIIpv6PingEntry,_g:fsMIIpv6PingIndex,'fsMIIpv6PingDest':fsMIIpv6PingDest,'fsMIIpv6PingIfIndex':fsMIIpv6PingIfIndex,'fsMIIpv6PingContextId':fsMIIpv6PingContextId,'fsMIIpv6PingAdminStatus':fsMIIpv6PingAdminStatus,'fsMIIpv6PingInterval':fsMIIpv6PingInterval,'fsMIIpv6PingRcvTimeout':fsMIIpv6PingRcvTimeout,'fsMIIpv6PingTries':fsMIIpv6PingTries,'fsMIIpv6PingSize':fsMIIpv6PingSize,'fsMIIpv6PingSentCount':fsMIIpv6PingSentCount,'fsMIIpv6PingAverageTime':fsMIIpv6PingAverageTime,'fsMIIpv6PingMaxTime':fsMIIpv6PingMaxTime,'fsMIIpv6PingMinTime':fsMIIpv6PingMinTime,'fsMIIpv6PingOperStatus':fsMIIpv6PingOperStatus,'fsMIIpv6PingSuccesses':fsMIIpv6PingSuccesses,'fsMIIpv6PingPercentageLoss':fsMIIpv6PingPercentageLoss,'fsMIIpv6PingData':fsMIIpv6PingData,'fsMIIpv6PingSrcAddr':fsMIIpv6PingSrcAddr,'fsMIIpv6PingZoneId':fsMIIpv6PingZoneId,'fsMIIpv6PingDestAddrType':fsMIIpv6PingDestAddrType,'fsMIIpv6GlobalDebug':fsMIIpv6GlobalDebug,'fsMIIpv6AddrSelPolicyTable':fsMIIpv6AddrSelPolicyTable,'fsMIIpv6AddrSelPolicyEntry':fsMIIpv6AddrSelPolicyEntry,_h:fsMIIpv6AddrSelPolicyPrefix,_i:fsMIIpv6AddrSelPolicyPrefixLen,_j:fsMIIpv6AddrSelPolicyIfIndex,'fsMIIpv6AddrSelPolicyScope':fsMIIpv6AddrSelPolicyScope,'fsMIIpv6AddrSelPolicyPrecedence':fsMIIpv6AddrSelPolicyPrecedence,'fsMIIpv6AddrSelPolicyLabel':fsMIIpv6AddrSelPolicyLabel,'fsMIIpv6AddrSelPolicyAddrType':fsMIIpv6AddrSelPolicyAddrType,'fsMIIpv6AddrSelPolicyIsPublicAddr':fsMIIpv6AddrSelPolicyIsPublicAddr,'fsMIIpv6AddrSelPolicyIsSelfAddr':fsMIIpv6AddrSelPolicyIsSelfAddr,'fsMIIpv6AddrSelPolicyReachabilityStatus':fsMIIpv6AddrSelPolicyReachabilityStatus,'fsMIIpv6AddrSelPolicyConfigStatus':fsMIIpv6AddrSelPolicyConfigStatus,'fsMIIpv6AddrSelPolicyRowStatus':fsMIIpv6AddrSelPolicyRowStatus,'fsMIIpv6IfScopeZoneMapTable':fsMIIpv6IfScopeZoneMapTable,'fsMIIpv6IfScopeZoneMapEntry':fsMIIpv6IfScopeZoneMapEntry,_k:fsMIIpv6ScopeZoneIndexIfIndex,'fsMIIpv6ScopeZoneIndexInterfaceLocal':fsMIIpv6ScopeZoneIndexInterfaceLocal,'fsMIIpv6ScopeZoneIndexLinkLocal':fsMIIpv6ScopeZoneIndexLinkLocal,'fsMIIpv6ScopeZoneIndex3':fsMIIpv6ScopeZoneIndex3,'fsMIIpv6ScopeZoneIndexAdminLocal':fsMIIpv6ScopeZoneIndexAdminLocal,'fsMIIpv6ScopeZoneIndexSiteLocal':fsMIIpv6ScopeZoneIndexSiteLocal,'fsMIIpv6ScopeZoneIndex6':fsMIIpv6ScopeZoneIndex6,'fsMIIpv6ScopeZoneIndex7':fsMIIpv6ScopeZoneIndex7,'fsMIIpv6ScopeZoneIndexOrganizationLocal':fsMIIpv6ScopeZoneIndexOrganizationLocal,'fsMIIpv6ScopeZoneIndex9':fsMIIpv6ScopeZoneIndex9,'fsMIIpv6ScopeZoneIndexA':fsMIIpv6ScopeZoneIndexA,'fsMIIpv6ScopeZoneIndexB':fsMIIpv6ScopeZoneIndexB,'fsMIIpv6ScopeZoneIndexC':fsMIIpv6ScopeZoneIndexC,'fsMIIpv6ScopeZoneIndexD':fsMIIpv6ScopeZoneIndexD,'fsMIIpv6ScopeZoneIndexE':fsMIIpv6ScopeZoneIndexE,'fsMIIpv6IfScopeZoneCreationStatus':fsMIIpv6IfScopeZoneCreationStatus,'fsMIIpv6IfScopeZoneRowStatus':fsMIIpv6IfScopeZoneRowStatus,'fsMIIpv6ScopeZoneTable':fsMIIpv6ScopeZoneTable,'fsMIIpv6ScopeZoneEntry':fsMIIpv6ScopeZoneEntry,_m:fsMIIpv6ScopeZoneContextId,_n:fsMIIpv6ScopeZoneName,'fsMIIpv6ScopeZoneIndex':fsMIIpv6ScopeZoneIndex,'fsMIIpv6ScopeZoneCreationStatus':fsMIIpv6ScopeZoneCreationStatus,'fsMIIpv6ScopeZoneInterfaceList':fsMIIpv6ScopeZoneInterfaceList,'fsMIIpv6IsDefaultScopeZone':fsMIIpv6IsDefaultScopeZone,'fsMIipv6Route':fsMIipv6Route,'fsMIIpv6PrefTable':fsMIIpv6PrefTable,'fsMIIpv6PrefEntry':fsMIIpv6PrefEntry,_o:fsMIIpv6Protocol,'fsMIIpv6Preference':fsMIIpv6Preference,'fsMIIpv6Test':fsMIIpv6Test,'fsMIIpv6TestRedEntryTime':fsMIIpv6TestRedEntryTime,'fsMIIpv6TestRedExitTime':fsMIIpv6TestRedExitTime})