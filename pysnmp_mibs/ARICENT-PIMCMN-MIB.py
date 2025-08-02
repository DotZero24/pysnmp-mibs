_AU='fsPimCmnNeighborIfIndex'
_AT='fsPimCmnHAEvent'
_AS='accessible-for-notify'
_AR='fsPimCmnIpGenMRouteNextHopAddress'
_AQ='fsPimCmnIpGenMRouteNextHopIfIndex'
_AP='fsPimCmnIpGenMRouteNextHopSourceMasklen'
_AO='fsPimCmnIpGenMRouteNextHopSource'
_AN='fsPimCmnIpGenMRouteNextHopGroupMasklen'
_AM='fsPimCmnIpGenMRouteNextHopGroup'
_AL='fsPimCmnIpGenMRouteNextHopAddrType'
_AK='fsPimCmnIpGenMRouteNextHopCompId'
_AJ='fsPimCmnIpGenMRouteSourceMasklen'
_AI='fsPimCmnIpGenMRouteSource'
_AH='fsPimCmnIpGenMRouteGroupMasklen'
_AG='fsPimCmnIpGenMRouteGroup'
_AF='fsPimCmnIpGenMRouteAddrType'
_AE='fsPimCmnIpGenMRouteCompId'
_AD='fsPimCmnNeighborExtAddress'
_AC='fsPimCmnNeighborExtAddrType'
_AB='fsPimCmnNeighborExtIfIndex'
_AA='fsPimCmnElectedRPGroupMasklen'
_A9='fsPimCmnElectedRPGroupAddress'
_A8='fsPimCmnElectedRPAddrType'
_A7='fsPimCmnElectedRPCompId'
_A6='fsPimCmnDFIfIndex'
_A5='fsPimCmnDFElectedRP'
_A4='fsPimCmnDFIfAddrType'
_A3='fsPimCmnRegChkSumTblRPAddress'
_A2='fsPimCmnRegChkSumTblRPAddrType'
_A1='fsPimCmnRegChkSumTblCompId'
_A0='fsPimCmnComponentId'
_z='fsPimCmnStaticRPSetGroupMasklen'
_y='fsPimCmnStaticRPSetGroupAddress'
_x='fsPimCmnStaticRPAddrType'
_w='fsPimCmnStaticRPSetCompId'
_v='fsPimCmnCandidateRPAddress'
_u='fsPimCmnCandidateRPGroupMasklen'
_t='fsPimCmnCandidateRPGroupAddress'
_s='fsPimCmnCandidateRPAddrType'
_r='fsPimCmnCandidateRPCompId'
_q='assert'
_p='fsPimCmnIpMRouteNextHopAddress'
_o='fsPimCmnIpMRouteNextHopIfIndex'
_n='fsPimCmnIpMRouteNextHopSourceMasklen'
_m='fsPimCmnIpMRouteNextHopSource'
_l='fsPimCmnIpMRouteNextHopGroup'
_k='fsPimCmnIpMRouteNextHopAddrType'
_j='fsPimCmnIpMRouteNextHopCompId'
_i='multicast'
_h='unicast'
_g='originator'
_f='notOriginator'
_e='ackpending'
_d='fsPimCmnIpMRouteSourceMasklen'
_c='fsPimCmnIpMRouteSource'
_b='fsPimCmnIpMRouteGroup'
_a='fsPimCmnIpMRouteAddrType'
_Z='fsPimCmnIpMRouteCompId'
_Y='fsPimCmnNeighborAddrType'
_X='fsPimCmnNeighborCompId'
_W='fsPimCmnInterfaceAddrType'
_V='fsPimCmnInterfaceIfIndex'
_U='fsPimcmnHARtrId'
_T='fsPimCmnNeighborAddress'
_S='milliseconds'
_R='seconds'
_Q='bidir'
_P='sm'
_O='pruned'
_N='read-create'
_M='Unsigned32'
_L='forwarding'
_K='disabled'
_J='enabled'
_I='disable'
_H='enable'
_G='deprecated'
_F='read-write'
_E='not-accessible'
_D='ARICENT-PIMCMN-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAipMRouteProtocol,IANAipRouteProtocol=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipMRouteProtocol','IANAipRouteProtocol')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsPimCmnMIB=ModuleIdentity((1,3,6,1,4,1,2076,111))
if mibBuilder.loadTexts:fsPimCmnMIB.setRevisions(('2012-09-05 00:00',))
class Status(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
class CompList(TextualConvention,OctetString):status=_A
_FsPimCmnMIBObjects_ObjectIdentity=ObjectIdentity
fsPimCmnMIBObjects=_FsPimCmnMIBObjects_ObjectIdentity((1,3,6,1,4,1,2076,111,1))
_FuturePimCmnScalars_ObjectIdentity=ObjectIdentity
futurePimCmnScalars=_FuturePimCmnScalars_ObjectIdentity((1,3,6,1,4,1,2076,111,1,1))
_FsPimCmnVersionString_Type=DisplayString
_FsPimCmnVersionString_Object=MibScalar
fsPimCmnVersionString=_FsPimCmnVersionString_Object((1,3,6,1,4,1,2076,111,1,1,1),_FsPimCmnVersionString_Type())
fsPimCmnVersionString.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnVersionString.setStatus(_A)
class _FsPimCmnSPTGroupThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimCmnSPTGroupThreshold_Type.__name__=_C
_FsPimCmnSPTGroupThreshold_Object=MibScalar
fsPimCmnSPTGroupThreshold=_FsPimCmnSPTGroupThreshold_Object((1,3,6,1,4,1,2076,111,1,1,2),_FsPimCmnSPTGroupThreshold_Type())
fsPimCmnSPTGroupThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnSPTGroupThreshold.setStatus(_A)
class _FsPimCmnSPTSourceThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimCmnSPTSourceThreshold_Type.__name__=_C
_FsPimCmnSPTSourceThreshold_Object=MibScalar
fsPimCmnSPTSourceThreshold=_FsPimCmnSPTSourceThreshold_Object((1,3,6,1,4,1,2076,111,1,1,3),_FsPimCmnSPTSourceThreshold_Type())
fsPimCmnSPTSourceThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnSPTSourceThreshold.setStatus(_A)
class _FsPimCmnSPTSwitchingPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimCmnSPTSwitchingPeriod_Type.__name__=_C
_FsPimCmnSPTSwitchingPeriod_Object=MibScalar
fsPimCmnSPTSwitchingPeriod=_FsPimCmnSPTSwitchingPeriod_Object((1,3,6,1,4,1,2076,111,1,1,4),_FsPimCmnSPTSwitchingPeriod_Type())
fsPimCmnSPTSwitchingPeriod.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnSPTSwitchingPeriod.setStatus(_A)
class _FsPimCmnSPTRpThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimCmnSPTRpThreshold_Type.__name__=_C
_FsPimCmnSPTRpThreshold_Object=MibScalar
fsPimCmnSPTRpThreshold=_FsPimCmnSPTRpThreshold_Object((1,3,6,1,4,1,2076,111,1,1,5),_FsPimCmnSPTRpThreshold_Type())
fsPimCmnSPTRpThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnSPTRpThreshold.setStatus(_A)
class _FsPimCmnSPTRpSwitchingPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimCmnSPTRpSwitchingPeriod_Type.__name__=_C
_FsPimCmnSPTRpSwitchingPeriod_Object=MibScalar
fsPimCmnSPTRpSwitchingPeriod=_FsPimCmnSPTRpSwitchingPeriod_Object((1,3,6,1,4,1,2076,111,1,1,6),_FsPimCmnSPTRpSwitchingPeriod_Type())
fsPimCmnSPTRpSwitchingPeriod.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnSPTRpSwitchingPeriod.setStatus(_A)
class _FsPimCmnRegStopRateLimitingPeriod_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimCmnRegStopRateLimitingPeriod_Type.__name__=_C
_FsPimCmnRegStopRateLimitingPeriod_Object=MibScalar
fsPimCmnRegStopRateLimitingPeriod=_FsPimCmnRegStopRateLimitingPeriod_Object((1,3,6,1,4,1,2076,111,1,1,7),_FsPimCmnRegStopRateLimitingPeriod_Type())
fsPimCmnRegStopRateLimitingPeriod.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnRegStopRateLimitingPeriod.setStatus(_A)
_FsPimCmnMemoryAllocFailCount_Type=Integer32
_FsPimCmnMemoryAllocFailCount_Object=MibScalar
fsPimCmnMemoryAllocFailCount=_FsPimCmnMemoryAllocFailCount_Object((1,3,6,1,4,1,2076,111,1,1,8),_FsPimCmnMemoryAllocFailCount_Type())
fsPimCmnMemoryAllocFailCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnMemoryAllocFailCount.setStatus(_A)
class _FsPimCmnGlobalTrace_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimCmnGlobalTrace_Type.__name__=_C
_FsPimCmnGlobalTrace_Object=MibScalar
fsPimCmnGlobalTrace=_FsPimCmnGlobalTrace_Object((1,3,6,1,4,1,2076,111,1,1,9),_FsPimCmnGlobalTrace_Type())
fsPimCmnGlobalTrace.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnGlobalTrace.setStatus(_A)
class _FsPimCmnGlobalDebug_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimCmnGlobalDebug_Type.__name__=_C
_FsPimCmnGlobalDebug_Object=MibScalar
fsPimCmnGlobalDebug=_FsPimCmnGlobalDebug_Object((1,3,6,1,4,1,2076,111,1,1,10),_FsPimCmnGlobalDebug_Type())
fsPimCmnGlobalDebug.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnGlobalDebug.setStatus(_A)
class _FsPimCmnPmbrStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_FsPimCmnPmbrStatus_Type.__name__=_C
_FsPimCmnPmbrStatus_Object=MibScalar
fsPimCmnPmbrStatus=_FsPimCmnPmbrStatus_Object((1,3,6,1,4,1,2076,111,1,1,11),_FsPimCmnPmbrStatus_Type())
fsPimCmnPmbrStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnPmbrStatus.setStatus(_A)
class _FsPimCmnRouterMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ssmonly',1),('smssm',2)))
_FsPimCmnRouterMode_Type.__name__=_C
_FsPimCmnRouterMode_Object=MibScalar
fsPimCmnRouterMode=_FsPimCmnRouterMode_Object((1,3,6,1,4,1,2076,111,1,1,12),_FsPimCmnRouterMode_Type())
fsPimCmnRouterMode.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnRouterMode.setStatus(_A)
class _FsPimCmnStaticRpEnabled_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_H,1)))
_FsPimCmnStaticRpEnabled_Type.__name__=_C
_FsPimCmnStaticRpEnabled_Object=MibScalar
fsPimCmnStaticRpEnabled=_FsPimCmnStaticRpEnabled_Object((1,3,6,1,4,1,2076,111,1,1,13),_FsPimCmnStaticRpEnabled_Type())
fsPimCmnStaticRpEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnStaticRpEnabled.setStatus(_A)
class _FsPimCmnIpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsPimCmnIpStatus_Type.__name__=_C
_FsPimCmnIpStatus_Object=MibScalar
fsPimCmnIpStatus=_FsPimCmnIpStatus_Object((1,3,6,1,4,1,2076,111,1,1,14),_FsPimCmnIpStatus_Type())
fsPimCmnIpStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnIpStatus.setStatus(_A)
class _FsPimCmnIpv6Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsPimCmnIpv6Status_Type.__name__=_C
_FsPimCmnIpv6Status_Object=MibScalar
fsPimCmnIpv6Status=_FsPimCmnIpv6Status_Object((1,3,6,1,4,1,2076,111,1,1,15),_FsPimCmnIpv6Status_Type())
fsPimCmnIpv6Status.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnIpv6Status.setStatus(_A)
class _FsPimCmnSRProcessingStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_H,1)))
_FsPimCmnSRProcessingStatus_Type.__name__=_C
_FsPimCmnSRProcessingStatus_Object=MibScalar
fsPimCmnSRProcessingStatus=_FsPimCmnSRProcessingStatus_Object((1,3,6,1,4,1,2076,111,1,1,16),_FsPimCmnSRProcessingStatus_Type())
fsPimCmnSRProcessingStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnSRProcessingStatus.setStatus(_A)
class _FsPimCmnRefreshInterval_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(4,100))
_FsPimCmnRefreshInterval_Type.__name__=_C
_FsPimCmnRefreshInterval_Object=MibScalar
fsPimCmnRefreshInterval=_FsPimCmnRefreshInterval_Object((1,3,6,1,4,1,2076,111,1,1,17),_FsPimCmnRefreshInterval_Type())
fsPimCmnRefreshInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnRefreshInterval.setStatus(_A)
if mibBuilder.loadTexts:fsPimCmnRefreshInterval.setUnits(_R)
class _FsPimCmnSourceActiveInterval_Type(Unsigned32):defaultValue=210;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(120,210))
_FsPimCmnSourceActiveInterval_Type.__name__=_M
_FsPimCmnSourceActiveInterval_Object=MibScalar
fsPimCmnSourceActiveInterval=_FsPimCmnSourceActiveInterval_Object((1,3,6,1,4,1,2076,111,1,1,18),_FsPimCmnSourceActiveInterval_Type())
fsPimCmnSourceActiveInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnSourceActiveInterval.setStatus(_A)
if mibBuilder.loadTexts:fsPimCmnSourceActiveInterval.setUnits(_R)
class _FsPimCmnHAAdminStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_J,1)))
_FsPimCmnHAAdminStatus_Type.__name__=_C
_FsPimCmnHAAdminStatus_Object=MibScalar
fsPimCmnHAAdminStatus=_FsPimCmnHAAdminStatus_Object((1,3,6,1,4,1,2076,111,1,1,19),_FsPimCmnHAAdminStatus_Type())
fsPimCmnHAAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnHAAdminStatus.setStatus(_A)
class _FsPimCmnHAState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),('activeStandbyUp',2),('activeStandbyDown',3),('standby',4)))
_FsPimCmnHAState_Type.__name__=_C
_FsPimCmnHAState_Object=MibScalar
fsPimCmnHAState=_FsPimCmnHAState_Object((1,3,6,1,4,1,2076,111,1,1,20),_FsPimCmnHAState_Type())
fsPimCmnHAState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnHAState.setStatus(_A)
class _FsPimCmnHADynamicBulkUpdStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notStarted',1),('inProgress',2),('completed',3),('aborted',4)))
_FsPimCmnHADynamicBulkUpdStatus_Type.__name__=_C
_FsPimCmnHADynamicBulkUpdStatus_Object=MibScalar
fsPimCmnHADynamicBulkUpdStatus=_FsPimCmnHADynamicBulkUpdStatus_Object((1,3,6,1,4,1,2076,111,1,1,21),_FsPimCmnHADynamicBulkUpdStatus_Type())
fsPimCmnHADynamicBulkUpdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnHADynamicBulkUpdStatus.setStatus(_A)
class _FsPimCmnHAForwardingTblEntryCnt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimCmnHAForwardingTblEntryCnt_Type.__name__=_C
_FsPimCmnHAForwardingTblEntryCnt_Object=MibScalar
fsPimCmnHAForwardingTblEntryCnt=_FsPimCmnHAForwardingTblEntryCnt_Object((1,3,6,1,4,1,2076,111,1,1,22),_FsPimCmnHAForwardingTblEntryCnt_Type())
fsPimCmnHAForwardingTblEntryCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnHAForwardingTblEntryCnt.setStatus(_A)
class _FsPimCmnIpRpfVector_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsPimCmnIpRpfVector_Type.__name__=_C
_FsPimCmnIpRpfVector_Object=MibScalar
fsPimCmnIpRpfVector=_FsPimCmnIpRpfVector_Object((1,3,6,1,4,1,2076,111,1,1,23),_FsPimCmnIpRpfVector_Type())
fsPimCmnIpRpfVector.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnIpRpfVector.setStatus(_A)
class _FsPimCmnIpBidirPIMStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsPimCmnIpBidirPIMStatus_Type.__name__=_C
_FsPimCmnIpBidirPIMStatus_Object=MibScalar
fsPimCmnIpBidirPIMStatus=_FsPimCmnIpBidirPIMStatus_Object((1,3,6,1,4,1,2076,111,1,1,24),_FsPimCmnIpBidirPIMStatus_Type())
fsPimCmnIpBidirPIMStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnIpBidirPIMStatus.setStatus(_A)
class _FsPimCmnIpBidirOfferInterval_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20000000))
_FsPimCmnIpBidirOfferInterval_Type.__name__=_C
_FsPimCmnIpBidirOfferInterval_Object=MibScalar
fsPimCmnIpBidirOfferInterval=_FsPimCmnIpBidirOfferInterval_Object((1,3,6,1,4,1,2076,111,1,1,25),_FsPimCmnIpBidirOfferInterval_Type())
fsPimCmnIpBidirOfferInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnIpBidirOfferInterval.setStatus(_A)
if mibBuilder.loadTexts:fsPimCmnIpBidirOfferInterval.setUnits(_S)
class _FsPimCmnIpBidirOfferLimit_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,100))
_FsPimCmnIpBidirOfferLimit_Type.__name__=_C
_FsPimCmnIpBidirOfferLimit_Object=MibScalar
fsPimCmnIpBidirOfferLimit=_FsPimCmnIpBidirOfferLimit_Object((1,3,6,1,4,1,2076,111,1,1,26),_FsPimCmnIpBidirOfferLimit_Type())
fsPimCmnIpBidirOfferLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnIpBidirOfferLimit.setStatus(_A)
_FuturePimCmnTables_ObjectIdentity=ObjectIdentity
futurePimCmnTables=_FuturePimCmnTables_ObjectIdentity((1,3,6,1,4,1,2076,111,1,2))
_FsPimCmnInterfaceTable_Object=MibTable
fsPimCmnInterfaceTable=_FsPimCmnInterfaceTable_Object((1,3,6,1,4,1,2076,111,1,2,1))
if mibBuilder.loadTexts:fsPimCmnInterfaceTable.setStatus(_A)
_FsPimCmnInterfaceEntry_Object=MibTableRow
fsPimCmnInterfaceEntry=_FsPimCmnInterfaceEntry_Object((1,3,6,1,4,1,2076,111,1,2,1,1))
fsPimCmnInterfaceEntry.setIndexNames((0,_D,_V),(0,_D,_W))
if mibBuilder.loadTexts:fsPimCmnInterfaceEntry.setStatus(_A)
class _FsPimCmnInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimCmnInterfaceIfIndex_Type.__name__=_C
_FsPimCmnInterfaceIfIndex_Object=MibTableColumn
fsPimCmnInterfaceIfIndex=_FsPimCmnInterfaceIfIndex_Object((1,3,6,1,4,1,2076,111,1,2,1,1,1),_FsPimCmnInterfaceIfIndex_Type())
fsPimCmnInterfaceIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnInterfaceIfIndex.setStatus(_A)
_FsPimCmnInterfaceAddrType_Type=InetAddressType
_FsPimCmnInterfaceAddrType_Object=MibTableColumn
fsPimCmnInterfaceAddrType=_FsPimCmnInterfaceAddrType_Object((1,3,6,1,4,1,2076,111,1,2,1,1,2),_FsPimCmnInterfaceAddrType_Type())
fsPimCmnInterfaceAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnInterfaceAddrType.setStatus(_A)
class _FsPimCmnInterfaceCompId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnInterfaceCompId_Type.__name__=_C
_FsPimCmnInterfaceCompId_Object=MibTableColumn
fsPimCmnInterfaceCompId=_FsPimCmnInterfaceCompId_Object((1,3,6,1,4,1,2076,111,1,2,1,1,3),_FsPimCmnInterfaceCompId_Type())
fsPimCmnInterfaceCompId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceCompId.setStatus(_A)
class _FsPimCmnInterfaceDRPriority_Type(Unsigned32):defaultValue=1
_FsPimCmnInterfaceDRPriority_Type.__name__=_M
_FsPimCmnInterfaceDRPriority_Object=MibTableColumn
fsPimCmnInterfaceDRPriority=_FsPimCmnInterfaceDRPriority_Object((1,3,6,1,4,1,2076,111,1,2,1,1,4),_FsPimCmnInterfaceDRPriority_Type())
fsPimCmnInterfaceDRPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceDRPriority.setStatus(_A)
class _FsPimCmnInterfaceHelloHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimCmnInterfaceHelloHoldTime_Type.__name__=_C
_FsPimCmnInterfaceHelloHoldTime_Object=MibTableColumn
fsPimCmnInterfaceHelloHoldTime=_FsPimCmnInterfaceHelloHoldTime_Object((1,3,6,1,4,1,2076,111,1,2,1,1,5),_FsPimCmnInterfaceHelloHoldTime_Type())
fsPimCmnInterfaceHelloHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceHelloHoldTime.setStatus(_A)
class _FsPimCmnInterfaceLanPruneDelayPresent_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_H,1)))
_FsPimCmnInterfaceLanPruneDelayPresent_Type.__name__=_C
_FsPimCmnInterfaceLanPruneDelayPresent_Object=MibTableColumn
fsPimCmnInterfaceLanPruneDelayPresent=_FsPimCmnInterfaceLanPruneDelayPresent_Object((1,3,6,1,4,1,2076,111,1,2,1,1,6),_FsPimCmnInterfaceLanPruneDelayPresent_Type())
fsPimCmnInterfaceLanPruneDelayPresent.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceLanPruneDelayPresent.setStatus(_A)
class _FsPimCmnInterfaceLanDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimCmnInterfaceLanDelay_Type.__name__=_C
_FsPimCmnInterfaceLanDelay_Object=MibTableColumn
fsPimCmnInterfaceLanDelay=_FsPimCmnInterfaceLanDelay_Object((1,3,6,1,4,1,2076,111,1,2,1,1,7),_FsPimCmnInterfaceLanDelay_Type())
fsPimCmnInterfaceLanDelay.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceLanDelay.setStatus(_A)
if mibBuilder.loadTexts:fsPimCmnInterfaceLanDelay.setUnits(_S)
class _FsPimCmnInterfaceOverrideInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimCmnInterfaceOverrideInterval_Type.__name__=_C
_FsPimCmnInterfaceOverrideInterval_Object=MibTableColumn
fsPimCmnInterfaceOverrideInterval=_FsPimCmnInterfaceOverrideInterval_Object((1,3,6,1,4,1,2076,111,1,2,1,1,8),_FsPimCmnInterfaceOverrideInterval_Type())
fsPimCmnInterfaceOverrideInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceOverrideInterval.setStatus(_A)
if mibBuilder.loadTexts:fsPimCmnInterfaceOverrideInterval.setUnits(_S)
_FsPimCmnInterfaceGenerationId_Type=Integer32
_FsPimCmnInterfaceGenerationId_Object=MibTableColumn
fsPimCmnInterfaceGenerationId=_FsPimCmnInterfaceGenerationId_Object((1,3,6,1,4,1,2076,111,1,2,1,1,9),_FsPimCmnInterfaceGenerationId_Type())
fsPimCmnInterfaceGenerationId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceGenerationId.setStatus(_A)
_FsPimCmnInterfaceSuppressionInterval_Type=Integer32
_FsPimCmnInterfaceSuppressionInterval_Object=MibTableColumn
fsPimCmnInterfaceSuppressionInterval=_FsPimCmnInterfaceSuppressionInterval_Object((1,3,6,1,4,1,2076,111,1,2,1,1,10),_FsPimCmnInterfaceSuppressionInterval_Type())
fsPimCmnInterfaceSuppressionInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceSuppressionInterval.setStatus(_A)
_FsPimCmnInterfaceAdminStatus_Type=Integer32
_FsPimCmnInterfaceAdminStatus_Object=MibTableColumn
fsPimCmnInterfaceAdminStatus=_FsPimCmnInterfaceAdminStatus_Object((1,3,6,1,4,1,2076,111,1,2,1,1,11),_FsPimCmnInterfaceAdminStatus_Type())
fsPimCmnInterfaceAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceAdminStatus.setStatus(_A)
_FsPimCmnInterfaceBorderBit_Type=Integer32
_FsPimCmnInterfaceBorderBit_Object=MibTableColumn
fsPimCmnInterfaceBorderBit=_FsPimCmnInterfaceBorderBit_Object((1,3,6,1,4,1,2076,111,1,2,1,1,12),_FsPimCmnInterfaceBorderBit_Type())
fsPimCmnInterfaceBorderBit.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceBorderBit.setStatus(_A)
class _FsPimCmnInterfaceGraftRetryInterval_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsPimCmnInterfaceGraftRetryInterval_Type.__name__=_M
_FsPimCmnInterfaceGraftRetryInterval_Object=MibTableColumn
fsPimCmnInterfaceGraftRetryInterval=_FsPimCmnInterfaceGraftRetryInterval_Object((1,3,6,1,4,1,2076,111,1,2,1,1,13),_FsPimCmnInterfaceGraftRetryInterval_Type())
fsPimCmnInterfaceGraftRetryInterval.setMaxAccess(_N)
if mibBuilder.loadTexts:fsPimCmnInterfaceGraftRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:fsPimCmnInterfaceGraftRetryInterval.setUnits(_R)
_FsPimCmnInterfaceSRPriorityEnabled_Type=TruthValue
_FsPimCmnInterfaceSRPriorityEnabled_Object=MibTableColumn
fsPimCmnInterfaceSRPriorityEnabled=_FsPimCmnInterfaceSRPriorityEnabled_Object((1,3,6,1,4,1,2076,111,1,2,1,1,14),_FsPimCmnInterfaceSRPriorityEnabled_Type())
fsPimCmnInterfaceSRPriorityEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceSRPriorityEnabled.setStatus(_A)
class _FsPimCmnInterfaceTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPimCmnInterfaceTtl_Type.__name__=_C
_FsPimCmnInterfaceTtl_Object=MibTableColumn
fsPimCmnInterfaceTtl=_FsPimCmnInterfaceTtl_Object((1,3,6,1,4,1,2076,111,1,2,1,1,15),_FsPimCmnInterfaceTtl_Type())
fsPimCmnInterfaceTtl.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceTtl.setStatus(_A)
_FsPimCmnInterfaceProtocol_Type=IANAipMRouteProtocol
_FsPimCmnInterfaceProtocol_Object=MibTableColumn
fsPimCmnInterfaceProtocol=_FsPimCmnInterfaceProtocol_Object((1,3,6,1,4,1,2076,111,1,2,1,1,16),_FsPimCmnInterfaceProtocol_Type())
fsPimCmnInterfaceProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceProtocol.setStatus(_A)
class _FsPimCmnInterfaceRateLimit_Type(Integer32):defaultValue=0
_FsPimCmnInterfaceRateLimit_Type.__name__=_C
_FsPimCmnInterfaceRateLimit_Object=MibTableColumn
fsPimCmnInterfaceRateLimit=_FsPimCmnInterfaceRateLimit_Object((1,3,6,1,4,1,2076,111,1,2,1,1,17),_FsPimCmnInterfaceRateLimit_Type())
fsPimCmnInterfaceRateLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceRateLimit.setStatus(_A)
_FsPimCmnInterfaceInMcastOctets_Type=Counter32
_FsPimCmnInterfaceInMcastOctets_Object=MibTableColumn
fsPimCmnInterfaceInMcastOctets=_FsPimCmnInterfaceInMcastOctets_Object((1,3,6,1,4,1,2076,111,1,2,1,1,18),_FsPimCmnInterfaceInMcastOctets_Type())
fsPimCmnInterfaceInMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceInMcastOctets.setStatus(_A)
_FsPimCmnInterfaceOutMcastOctets_Type=Counter32
_FsPimCmnInterfaceOutMcastOctets_Object=MibTableColumn
fsPimCmnInterfaceOutMcastOctets=_FsPimCmnInterfaceOutMcastOctets_Object((1,3,6,1,4,1,2076,111,1,2,1,1,19),_FsPimCmnInterfaceOutMcastOctets_Type())
fsPimCmnInterfaceOutMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceOutMcastOctets.setStatus(_A)
_FsPimCmnInterfaceHCInMcastOctets_Type=Counter64
_FsPimCmnInterfaceHCInMcastOctets_Object=MibTableColumn
fsPimCmnInterfaceHCInMcastOctets=_FsPimCmnInterfaceHCInMcastOctets_Object((1,3,6,1,4,1,2076,111,1,2,1,1,20),_FsPimCmnInterfaceHCInMcastOctets_Type())
fsPimCmnInterfaceHCInMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceHCInMcastOctets.setStatus(_A)
_FsPimCmnInterfaceHCOutMcastOctets_Type=Counter64
_FsPimCmnInterfaceHCOutMcastOctets_Object=MibTableColumn
fsPimCmnInterfaceHCOutMcastOctets=_FsPimCmnInterfaceHCOutMcastOctets_Object((1,3,6,1,4,1,2076,111,1,2,1,1,21),_FsPimCmnInterfaceHCOutMcastOctets_Type())
fsPimCmnInterfaceHCOutMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceHCOutMcastOctets.setStatus(_A)
_FsPimCmnInterfaceCompIdList_Type=CompList
_FsPimCmnInterfaceCompIdList_Object=MibTableColumn
fsPimCmnInterfaceCompIdList=_FsPimCmnInterfaceCompIdList_Object((1,3,6,1,4,1,2076,111,1,2,1,1,22),_FsPimCmnInterfaceCompIdList_Type())
fsPimCmnInterfaceCompIdList.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceCompIdList.setStatus(_A)
_FsPimCmnInterfaceDFOfferSentPkts_Type=Counter32
_FsPimCmnInterfaceDFOfferSentPkts_Object=MibTableColumn
fsPimCmnInterfaceDFOfferSentPkts=_FsPimCmnInterfaceDFOfferSentPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,23),_FsPimCmnInterfaceDFOfferSentPkts_Type())
fsPimCmnInterfaceDFOfferSentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceDFOfferSentPkts.setStatus(_A)
_FsPimCmnInterfaceDFOfferRcvdPkts_Type=Counter32
_FsPimCmnInterfaceDFOfferRcvdPkts_Object=MibTableColumn
fsPimCmnInterfaceDFOfferRcvdPkts=_FsPimCmnInterfaceDFOfferRcvdPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,24),_FsPimCmnInterfaceDFOfferRcvdPkts_Type())
fsPimCmnInterfaceDFOfferRcvdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceDFOfferRcvdPkts.setStatus(_A)
_FsPimCmnInterfaceDFWinnerSentPkts_Type=Counter32
_FsPimCmnInterfaceDFWinnerSentPkts_Object=MibTableColumn
fsPimCmnInterfaceDFWinnerSentPkts=_FsPimCmnInterfaceDFWinnerSentPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,25),_FsPimCmnInterfaceDFWinnerSentPkts_Type())
fsPimCmnInterfaceDFWinnerSentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceDFWinnerSentPkts.setStatus(_A)
_FsPimCmnInterfaceDFWinnerRcvdPkts_Type=Counter32
_FsPimCmnInterfaceDFWinnerRcvdPkts_Object=MibTableColumn
fsPimCmnInterfaceDFWinnerRcvdPkts=_FsPimCmnInterfaceDFWinnerRcvdPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,26),_FsPimCmnInterfaceDFWinnerRcvdPkts_Type())
fsPimCmnInterfaceDFWinnerRcvdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceDFWinnerRcvdPkts.setStatus(_A)
_FsPimCmnInterfaceDFBackoffSentPkts_Type=Counter32
_FsPimCmnInterfaceDFBackoffSentPkts_Object=MibTableColumn
fsPimCmnInterfaceDFBackoffSentPkts=_FsPimCmnInterfaceDFBackoffSentPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,27),_FsPimCmnInterfaceDFBackoffSentPkts_Type())
fsPimCmnInterfaceDFBackoffSentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceDFBackoffSentPkts.setStatus(_A)
_FsPimCmnInterfaceDFBackoffRcvdPkts_Type=Counter32
_FsPimCmnInterfaceDFBackoffRcvdPkts_Object=MibTableColumn
fsPimCmnInterfaceDFBackoffRcvdPkts=_FsPimCmnInterfaceDFBackoffRcvdPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,28),_FsPimCmnInterfaceDFBackoffRcvdPkts_Type())
fsPimCmnInterfaceDFBackoffRcvdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceDFBackoffRcvdPkts.setStatus(_A)
_FsPimCmnInterfaceDFPassSentPkts_Type=Counter32
_FsPimCmnInterfaceDFPassSentPkts_Object=MibTableColumn
fsPimCmnInterfaceDFPassSentPkts=_FsPimCmnInterfaceDFPassSentPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,29),_FsPimCmnInterfaceDFPassSentPkts_Type())
fsPimCmnInterfaceDFPassSentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceDFPassSentPkts.setStatus(_A)
_FsPimCmnInterfaceDFPassRcvdPkts_Type=Counter32
_FsPimCmnInterfaceDFPassRcvdPkts_Object=MibTableColumn
fsPimCmnInterfaceDFPassRcvdPkts=_FsPimCmnInterfaceDFPassRcvdPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,30),_FsPimCmnInterfaceDFPassRcvdPkts_Type())
fsPimCmnInterfaceDFPassRcvdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceDFPassRcvdPkts.setStatus(_A)
_FsPimCmnInterfaceCKSumErrorPkts_Type=Counter32
_FsPimCmnInterfaceCKSumErrorPkts_Object=MibTableColumn
fsPimCmnInterfaceCKSumErrorPkts=_FsPimCmnInterfaceCKSumErrorPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,31),_FsPimCmnInterfaceCKSumErrorPkts_Type())
fsPimCmnInterfaceCKSumErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceCKSumErrorPkts.setStatus(_A)
_FsPimCmnInterfaceInvalidTypePkts_Type=Counter32
_FsPimCmnInterfaceInvalidTypePkts_Object=MibTableColumn
fsPimCmnInterfaceInvalidTypePkts=_FsPimCmnInterfaceInvalidTypePkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,32),_FsPimCmnInterfaceInvalidTypePkts_Type())
fsPimCmnInterfaceInvalidTypePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceInvalidTypePkts.setStatus(_A)
_FsPimCmnInterfaceInvalidDFSubTypePkts_Type=Counter32
_FsPimCmnInterfaceInvalidDFSubTypePkts_Object=MibTableColumn
fsPimCmnInterfaceInvalidDFSubTypePkts=_FsPimCmnInterfaceInvalidDFSubTypePkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,33),_FsPimCmnInterfaceInvalidDFSubTypePkts_Type())
fsPimCmnInterfaceInvalidDFSubTypePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceInvalidDFSubTypePkts.setStatus(_A)
_FsPimCmnInterfaceAuthFailPkts_Type=Counter32
_FsPimCmnInterfaceAuthFailPkts_Object=MibTableColumn
fsPimCmnInterfaceAuthFailPkts=_FsPimCmnInterfaceAuthFailPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,34),_FsPimCmnInterfaceAuthFailPkts_Type())
fsPimCmnInterfaceAuthFailPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceAuthFailPkts.setStatus(_A)
_FsPimCmnInterfaceFromNonNbrsPkts_Type=Counter32
_FsPimCmnInterfaceFromNonNbrsPkts_Object=MibTableColumn
fsPimCmnInterfaceFromNonNbrsPkts=_FsPimCmnInterfaceFromNonNbrsPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,35),_FsPimCmnInterfaceFromNonNbrsPkts_Type())
fsPimCmnInterfaceFromNonNbrsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceFromNonNbrsPkts.setStatus(_A)
_FsPimCmnInterfaceJPRcvdOnRPFPkts_Type=Counter32
_FsPimCmnInterfaceJPRcvdOnRPFPkts_Object=MibTableColumn
fsPimCmnInterfaceJPRcvdOnRPFPkts=_FsPimCmnInterfaceJPRcvdOnRPFPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,36),_FsPimCmnInterfaceJPRcvdOnRPFPkts_Type())
fsPimCmnInterfaceJPRcvdOnRPFPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceJPRcvdOnRPFPkts.setStatus(_A)
_FsPimCmnInterfaceJPRcvdNoRPPkts_Type=Counter32
_FsPimCmnInterfaceJPRcvdNoRPPkts_Object=MibTableColumn
fsPimCmnInterfaceJPRcvdNoRPPkts=_FsPimCmnInterfaceJPRcvdNoRPPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,37),_FsPimCmnInterfaceJPRcvdNoRPPkts_Type())
fsPimCmnInterfaceJPRcvdNoRPPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceJPRcvdNoRPPkts.setStatus(_A)
_FsPimCmnInterfaceJPRcvdWrongRPPkts_Type=Counter32
_FsPimCmnInterfaceJPRcvdWrongRPPkts_Object=MibTableColumn
fsPimCmnInterfaceJPRcvdWrongRPPkts=_FsPimCmnInterfaceJPRcvdWrongRPPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,38),_FsPimCmnInterfaceJPRcvdWrongRPPkts_Type())
fsPimCmnInterfaceJPRcvdWrongRPPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceJPRcvdWrongRPPkts.setStatus(_A)
_FsPimCmnInterfaceJoinSSMGrpPkts_Type=Counter32
_FsPimCmnInterfaceJoinSSMGrpPkts_Object=MibTableColumn
fsPimCmnInterfaceJoinSSMGrpPkts=_FsPimCmnInterfaceJoinSSMGrpPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,39),_FsPimCmnInterfaceJoinSSMGrpPkts_Type())
fsPimCmnInterfaceJoinSSMGrpPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceJoinSSMGrpPkts.setStatus(_A)
_FsPimCmnInterfaceJoinBidirGrpPkts_Type=Counter32
_FsPimCmnInterfaceJoinBidirGrpPkts_Object=MibTableColumn
fsPimCmnInterfaceJoinBidirGrpPkts=_FsPimCmnInterfaceJoinBidirGrpPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,40),_FsPimCmnInterfaceJoinBidirGrpPkts_Type())
fsPimCmnInterfaceJoinBidirGrpPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceJoinBidirGrpPkts.setStatus(_A)
_FsPimCmnInterfaceHelloRcvdPkts_Type=Counter32
_FsPimCmnInterfaceHelloRcvdPkts_Object=MibTableColumn
fsPimCmnInterfaceHelloRcvdPkts=_FsPimCmnInterfaceHelloRcvdPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,41),_FsPimCmnInterfaceHelloRcvdPkts_Type())
fsPimCmnInterfaceHelloRcvdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceHelloRcvdPkts.setStatus(_A)
_FsPimCmnInterfaceHelloSentPkts_Type=Counter32
_FsPimCmnInterfaceHelloSentPkts_Object=MibTableColumn
fsPimCmnInterfaceHelloSentPkts=_FsPimCmnInterfaceHelloSentPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,42),_FsPimCmnInterfaceHelloSentPkts_Type())
fsPimCmnInterfaceHelloSentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceHelloSentPkts.setStatus(_A)
_FsPimCmnInterfaceJPRcvdPkts_Type=Counter32
_FsPimCmnInterfaceJPRcvdPkts_Object=MibTableColumn
fsPimCmnInterfaceJPRcvdPkts=_FsPimCmnInterfaceJPRcvdPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,43),_FsPimCmnInterfaceJPRcvdPkts_Type())
fsPimCmnInterfaceJPRcvdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceJPRcvdPkts.setStatus(_A)
_FsPimCmnInterfaceJPSentPkts_Type=Counter32
_FsPimCmnInterfaceJPSentPkts_Object=MibTableColumn
fsPimCmnInterfaceJPSentPkts=_FsPimCmnInterfaceJPSentPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,44),_FsPimCmnInterfaceJPSentPkts_Type())
fsPimCmnInterfaceJPSentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceJPSentPkts.setStatus(_A)
_FsPimCmnInterfaceAssertRcvdPkts_Type=Counter32
_FsPimCmnInterfaceAssertRcvdPkts_Object=MibTableColumn
fsPimCmnInterfaceAssertRcvdPkts=_FsPimCmnInterfaceAssertRcvdPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,45),_FsPimCmnInterfaceAssertRcvdPkts_Type())
fsPimCmnInterfaceAssertRcvdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceAssertRcvdPkts.setStatus(_A)
_FsPimCmnInterfaceAssertSentPkts_Type=Counter32
_FsPimCmnInterfaceAssertSentPkts_Object=MibTableColumn
fsPimCmnInterfaceAssertSentPkts=_FsPimCmnInterfaceAssertSentPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,46),_FsPimCmnInterfaceAssertSentPkts_Type())
fsPimCmnInterfaceAssertSentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceAssertSentPkts.setStatus(_A)
_FsPimCmnInterfaceGraftRcvdPkts_Type=Counter32
_FsPimCmnInterfaceGraftRcvdPkts_Object=MibTableColumn
fsPimCmnInterfaceGraftRcvdPkts=_FsPimCmnInterfaceGraftRcvdPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,47),_FsPimCmnInterfaceGraftRcvdPkts_Type())
fsPimCmnInterfaceGraftRcvdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceGraftRcvdPkts.setStatus(_A)
_FsPimCmnInterfaceGraftSentPkts_Type=Counter32
_FsPimCmnInterfaceGraftSentPkts_Object=MibTableColumn
fsPimCmnInterfaceGraftSentPkts=_FsPimCmnInterfaceGraftSentPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,48),_FsPimCmnInterfaceGraftSentPkts_Type())
fsPimCmnInterfaceGraftSentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceGraftSentPkts.setStatus(_A)
_FsPimCmnInterfaceGraftAckRcvdPkts_Type=Counter32
_FsPimCmnInterfaceGraftAckRcvdPkts_Object=MibTableColumn
fsPimCmnInterfaceGraftAckRcvdPkts=_FsPimCmnInterfaceGraftAckRcvdPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,49),_FsPimCmnInterfaceGraftAckRcvdPkts_Type())
fsPimCmnInterfaceGraftAckRcvdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceGraftAckRcvdPkts.setStatus(_A)
_FsPimCmnInterfaceGraftAckSentPkts_Type=Counter32
_FsPimCmnInterfaceGraftAckSentPkts_Object=MibTableColumn
fsPimCmnInterfaceGraftAckSentPkts=_FsPimCmnInterfaceGraftAckSentPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,50),_FsPimCmnInterfaceGraftAckSentPkts_Type())
fsPimCmnInterfaceGraftAckSentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceGraftAckSentPkts.setStatus(_A)
_FsPimCmnInterfacePackLenErrorPkts_Type=Counter32
_FsPimCmnInterfacePackLenErrorPkts_Object=MibTableColumn
fsPimCmnInterfacePackLenErrorPkts=_FsPimCmnInterfacePackLenErrorPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,51),_FsPimCmnInterfacePackLenErrorPkts_Type())
fsPimCmnInterfacePackLenErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfacePackLenErrorPkts.setStatus(_A)
_FsPimCmnInterfaceBadVersionPkts_Type=Counter32
_FsPimCmnInterfaceBadVersionPkts_Object=MibTableColumn
fsPimCmnInterfaceBadVersionPkts=_FsPimCmnInterfaceBadVersionPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,53),_FsPimCmnInterfaceBadVersionPkts_Type())
fsPimCmnInterfaceBadVersionPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceBadVersionPkts.setStatus(_A)
_FsPimCmnInterfacePktsfromSelf_Type=Counter32
_FsPimCmnInterfacePktsfromSelf_Object=MibTableColumn
fsPimCmnInterfacePktsfromSelf=_FsPimCmnInterfacePktsfromSelf_Object((1,3,6,1,4,1,2076,111,1,2,1,1,54),_FsPimCmnInterfacePktsfromSelf_Type())
fsPimCmnInterfacePktsfromSelf.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfacePktsfromSelf.setStatus(_A)
_FsPimCmnInterfaceExtBorderBit_Type=Integer32
_FsPimCmnInterfaceExtBorderBit_Object=MibTableColumn
fsPimCmnInterfaceExtBorderBit=_FsPimCmnInterfaceExtBorderBit_Object((1,3,6,1,4,1,2076,111,1,2,1,1,55),_FsPimCmnInterfaceExtBorderBit_Type())
fsPimCmnInterfaceExtBorderBit.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceExtBorderBit.setStatus(_A)
_FsPimCmnInterfaceJoinSSMBadPkts_Type=Counter32
_FsPimCmnInterfaceJoinSSMBadPkts_Object=MibTableColumn
fsPimCmnInterfaceJoinSSMBadPkts=_FsPimCmnInterfaceJoinSSMBadPkts_Object((1,3,6,1,4,1,2076,111,1,2,1,1,56),_FsPimCmnInterfaceJoinSSMBadPkts_Type())
fsPimCmnInterfaceJoinSSMBadPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceJoinSSMBadPkts.setStatus(_A)
_FsPimCmnNeighborTable_Object=MibTable
fsPimCmnNeighborTable=_FsPimCmnNeighborTable_Object((1,3,6,1,4,1,2076,111,1,2,2))
if mibBuilder.loadTexts:fsPimCmnNeighborTable.setStatus(_G)
_FsPimCmnNeighborEntry_Object=MibTableRow
fsPimCmnNeighborEntry=_FsPimCmnNeighborEntry_Object((1,3,6,1,4,1,2076,111,1,2,2,1))
fsPimCmnNeighborEntry.setIndexNames((0,_D,_X),(0,_D,_Y),(0,_D,_T))
if mibBuilder.loadTexts:fsPimCmnNeighborEntry.setStatus(_G)
class _FsPimCmnNeighborCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnNeighborCompId_Type.__name__=_C
_FsPimCmnNeighborCompId_Object=MibTableColumn
fsPimCmnNeighborCompId=_FsPimCmnNeighborCompId_Object((1,3,6,1,4,1,2076,111,1,2,2,1,1),_FsPimCmnNeighborCompId_Type())
fsPimCmnNeighborCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnNeighborCompId.setStatus(_G)
_FsPimCmnNeighborAddrType_Type=InetAddressType
_FsPimCmnNeighborAddrType_Object=MibTableColumn
fsPimCmnNeighborAddrType=_FsPimCmnNeighborAddrType_Object((1,3,6,1,4,1,2076,111,1,2,2,1,2),_FsPimCmnNeighborAddrType_Type())
fsPimCmnNeighborAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnNeighborAddrType.setStatus(_G)
_FsPimCmnNeighborAddress_Type=InetAddress
_FsPimCmnNeighborAddress_Object=MibTableColumn
fsPimCmnNeighborAddress=_FsPimCmnNeighborAddress_Object((1,3,6,1,4,1,2076,111,1,2,2,1,3),_FsPimCmnNeighborAddress_Type())
fsPimCmnNeighborAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnNeighborAddress.setStatus(_G)
_FsPimCmnNeighborIfIndex_Type=Integer32
_FsPimCmnNeighborIfIndex_Object=MibTableColumn
fsPimCmnNeighborIfIndex=_FsPimCmnNeighborIfIndex_Object((1,3,6,1,4,1,2076,111,1,2,2,1,4),_FsPimCmnNeighborIfIndex_Type())
fsPimCmnNeighborIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborIfIndex.setStatus(_G)
_FsPimCmnNeighborUpTime_Type=TimeTicks
_FsPimCmnNeighborUpTime_Object=MibTableColumn
fsPimCmnNeighborUpTime=_FsPimCmnNeighborUpTime_Object((1,3,6,1,4,1,2076,111,1,2,2,1,5),_FsPimCmnNeighborUpTime_Type())
fsPimCmnNeighborUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborUpTime.setStatus(_G)
_FsPimCmnNeighborExpiryTime_Type=TimeTicks
_FsPimCmnNeighborExpiryTime_Object=MibTableColumn
fsPimCmnNeighborExpiryTime=_FsPimCmnNeighborExpiryTime_Object((1,3,6,1,4,1,2076,111,1,2,2,1,6),_FsPimCmnNeighborExpiryTime_Type())
fsPimCmnNeighborExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExpiryTime.setStatus(_G)
_FsPimCmnNeighborGenerationId_Type=Integer32
_FsPimCmnNeighborGenerationId_Object=MibTableColumn
fsPimCmnNeighborGenerationId=_FsPimCmnNeighborGenerationId_Object((1,3,6,1,4,1,2076,111,1,2,2,1,7),_FsPimCmnNeighborGenerationId_Type())
fsPimCmnNeighborGenerationId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborGenerationId.setStatus(_G)
_FsPimCmnNeighborLanDelay_Type=Integer32
_FsPimCmnNeighborLanDelay_Object=MibTableColumn
fsPimCmnNeighborLanDelay=_FsPimCmnNeighborLanDelay_Object((1,3,6,1,4,1,2076,111,1,2,2,1,8),_FsPimCmnNeighborLanDelay_Type())
fsPimCmnNeighborLanDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborLanDelay.setStatus(_G)
_FsPimCmnNeighborDRPriority_Type=Unsigned32
_FsPimCmnNeighborDRPriority_Object=MibTableColumn
fsPimCmnNeighborDRPriority=_FsPimCmnNeighborDRPriority_Object((1,3,6,1,4,1,2076,111,1,2,2,1,9),_FsPimCmnNeighborDRPriority_Type())
fsPimCmnNeighborDRPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborDRPriority.setStatus(_G)
_FsPimCmnNeighborOverrideInterval_Type=Integer32
_FsPimCmnNeighborOverrideInterval_Object=MibTableColumn
fsPimCmnNeighborOverrideInterval=_FsPimCmnNeighborOverrideInterval_Object((1,3,6,1,4,1,2076,111,1,2,2,1,10),_FsPimCmnNeighborOverrideInterval_Type())
fsPimCmnNeighborOverrideInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborOverrideInterval.setStatus(_G)
_FsPimCmnNeighborSRCapable_Type=TruthValue
_FsPimCmnNeighborSRCapable_Object=MibTableColumn
fsPimCmnNeighborSRCapable=_FsPimCmnNeighborSRCapable_Object((1,3,6,1,4,1,2076,111,1,2,2,1,11),_FsPimCmnNeighborSRCapable_Type())
fsPimCmnNeighborSRCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborSRCapable.setStatus(_G)
_FsPimCmnNeighborRPFCapable_Type=TruthValue
_FsPimCmnNeighborRPFCapable_Object=MibTableColumn
fsPimCmnNeighborRPFCapable=_FsPimCmnNeighborRPFCapable_Object((1,3,6,1,4,1,2076,111,1,2,2,1,12),_FsPimCmnNeighborRPFCapable_Type())
fsPimCmnNeighborRPFCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborRPFCapable.setStatus(_G)
_FsPimCmnNeighborBidirCapable_Type=TruthValue
_FsPimCmnNeighborBidirCapable_Object=MibTableColumn
fsPimCmnNeighborBidirCapable=_FsPimCmnNeighborBidirCapable_Object((1,3,6,1,4,1,2076,111,1,2,2,1,13),_FsPimCmnNeighborBidirCapable_Type())
fsPimCmnNeighborBidirCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborBidirCapable.setStatus(_G)
_FsPimCmnIpMRouteTable_Object=MibTable
fsPimCmnIpMRouteTable=_FsPimCmnIpMRouteTable_Object((1,3,6,1,4,1,2076,111,1,2,3))
if mibBuilder.loadTexts:fsPimCmnIpMRouteTable.setStatus(_A)
_FsPimCmnIpMRouteEntry_Object=MibTableRow
fsPimCmnIpMRouteEntry=_FsPimCmnIpMRouteEntry_Object((1,3,6,1,4,1,2076,111,1,2,3,1))
fsPimCmnIpMRouteEntry.setIndexNames((0,_D,_Z),(0,_D,_a),(0,_D,_b),(0,_D,_c),(0,_D,_d))
if mibBuilder.loadTexts:fsPimCmnIpMRouteEntry.setStatus(_A)
class _FsPimCmnIpMRouteCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnIpMRouteCompId_Type.__name__=_C
_FsPimCmnIpMRouteCompId_Object=MibTableColumn
fsPimCmnIpMRouteCompId=_FsPimCmnIpMRouteCompId_Object((1,3,6,1,4,1,2076,111,1,2,3,1,1),_FsPimCmnIpMRouteCompId_Type())
fsPimCmnIpMRouteCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteCompId.setStatus(_A)
_FsPimCmnIpMRouteAddrType_Type=InetAddressType
_FsPimCmnIpMRouteAddrType_Object=MibTableColumn
fsPimCmnIpMRouteAddrType=_FsPimCmnIpMRouteAddrType_Object((1,3,6,1,4,1,2076,111,1,2,3,1,2),_FsPimCmnIpMRouteAddrType_Type())
fsPimCmnIpMRouteAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteAddrType.setStatus(_A)
_FsPimCmnIpMRouteGroup_Type=InetAddress
_FsPimCmnIpMRouteGroup_Object=MibTableColumn
fsPimCmnIpMRouteGroup=_FsPimCmnIpMRouteGroup_Object((1,3,6,1,4,1,2076,111,1,2,3,1,3),_FsPimCmnIpMRouteGroup_Type())
fsPimCmnIpMRouteGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteGroup.setStatus(_A)
_FsPimCmnIpMRouteSource_Type=InetAddress
_FsPimCmnIpMRouteSource_Object=MibTableColumn
fsPimCmnIpMRouteSource=_FsPimCmnIpMRouteSource_Object((1,3,6,1,4,1,2076,111,1,2,3,1,4),_FsPimCmnIpMRouteSource_Type())
fsPimCmnIpMRouteSource.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteSource.setStatus(_A)
class _FsPimCmnIpMRouteSourceMasklen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimCmnIpMRouteSourceMasklen_Type.__name__=_C
_FsPimCmnIpMRouteSourceMasklen_Object=MibTableColumn
fsPimCmnIpMRouteSourceMasklen=_FsPimCmnIpMRouteSourceMasklen_Object((1,3,6,1,4,1,2076,111,1,2,3,1,5),_FsPimCmnIpMRouteSourceMasklen_Type())
fsPimCmnIpMRouteSourceMasklen.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteSourceMasklen.setStatus(_A)
_FsPimCmnIpMRouteUpstreamNeighbor_Type=InetAddress
_FsPimCmnIpMRouteUpstreamNeighbor_Object=MibTableColumn
fsPimCmnIpMRouteUpstreamNeighbor=_FsPimCmnIpMRouteUpstreamNeighbor_Object((1,3,6,1,4,1,2076,111,1,2,3,1,6),_FsPimCmnIpMRouteUpstreamNeighbor_Type())
fsPimCmnIpMRouteUpstreamNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteUpstreamNeighbor.setStatus(_A)
_FsPimCmnIpMRouteInIfIndex_Type=Integer32
_FsPimCmnIpMRouteInIfIndex_Object=MibTableColumn
fsPimCmnIpMRouteInIfIndex=_FsPimCmnIpMRouteInIfIndex_Object((1,3,6,1,4,1,2076,111,1,2,3,1,7),_FsPimCmnIpMRouteInIfIndex_Type())
fsPimCmnIpMRouteInIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteInIfIndex.setStatus(_A)
_FsPimCmnIpMRouteUpTime_Type=TimeTicks
_FsPimCmnIpMRouteUpTime_Object=MibTableColumn
fsPimCmnIpMRouteUpTime=_FsPimCmnIpMRouteUpTime_Object((1,3,6,1,4,1,2076,111,1,2,3,1,8),_FsPimCmnIpMRouteUpTime_Type())
fsPimCmnIpMRouteUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteUpTime.setStatus(_A)
_FsPimCmnIpMRoutePkts_Type=Counter32
_FsPimCmnIpMRoutePkts_Object=MibTableColumn
fsPimCmnIpMRoutePkts=_FsPimCmnIpMRoutePkts_Object((1,3,6,1,4,1,2076,111,1,2,3,1,9),_FsPimCmnIpMRoutePkts_Type())
fsPimCmnIpMRoutePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRoutePkts.setStatus(_A)
_FsPimCmnIpMRouteUpstreamAssertTimer_Type=TimeTicks
_FsPimCmnIpMRouteUpstreamAssertTimer_Object=MibTableColumn
fsPimCmnIpMRouteUpstreamAssertTimer=_FsPimCmnIpMRouteUpstreamAssertTimer_Object((1,3,6,1,4,1,2076,111,1,2,3,1,10),_FsPimCmnIpMRouteUpstreamAssertTimer_Type())
fsPimCmnIpMRouteUpstreamAssertTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteUpstreamAssertTimer.setStatus(_A)
_FsPimCmnIpMRouteAssertMetric_Type=Integer32
_FsPimCmnIpMRouteAssertMetric_Object=MibTableColumn
fsPimCmnIpMRouteAssertMetric=_FsPimCmnIpMRouteAssertMetric_Object((1,3,6,1,4,1,2076,111,1,2,3,1,11),_FsPimCmnIpMRouteAssertMetric_Type())
fsPimCmnIpMRouteAssertMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteAssertMetric.setStatus(_A)
_FsPimCmnIpMRouteAssertMetricPref_Type=Integer32
_FsPimCmnIpMRouteAssertMetricPref_Object=MibTableColumn
fsPimCmnIpMRouteAssertMetricPref=_FsPimCmnIpMRouteAssertMetricPref_Object((1,3,6,1,4,1,2076,111,1,2,3,1,12),_FsPimCmnIpMRouteAssertMetricPref_Type())
fsPimCmnIpMRouteAssertMetricPref.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteAssertMetricPref.setStatus(_A)
_FsPimCmnIpMRouteAssertRPTBit_Type=TruthValue
_FsPimCmnIpMRouteAssertRPTBit_Object=MibTableColumn
fsPimCmnIpMRouteAssertRPTBit=_FsPimCmnIpMRouteAssertRPTBit_Object((1,3,6,1,4,1,2076,111,1,2,3,1,13),_FsPimCmnIpMRouteAssertRPTBit_Type())
fsPimCmnIpMRouteAssertRPTBit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteAssertRPTBit.setStatus(_A)
_FsPimCmnIpMRouteTimerFlags_Type=Integer32
_FsPimCmnIpMRouteTimerFlags_Object=MibTableColumn
fsPimCmnIpMRouteTimerFlags=_FsPimCmnIpMRouteTimerFlags_Object((1,3,6,1,4,1,2076,111,1,2,3,1,14),_FsPimCmnIpMRouteTimerFlags_Type())
fsPimCmnIpMRouteTimerFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteTimerFlags.setStatus(_A)
_FsPimCmnIpMRouteFlags_Type=Integer32
_FsPimCmnIpMRouteFlags_Object=MibTableColumn
fsPimCmnIpMRouteFlags=_FsPimCmnIpMRouteFlags_Object((1,3,6,1,4,1,2076,111,1,2,3,1,15),_FsPimCmnIpMRouteFlags_Type())
fsPimCmnIpMRouteFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteFlags.setStatus(_A)
class _FsPimCmnIpMRouteUpstreamPruneState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_e,2),(_O,3)))
_FsPimCmnIpMRouteUpstreamPruneState_Type.__name__=_C
_FsPimCmnIpMRouteUpstreamPruneState_Object=MibTableColumn
fsPimCmnIpMRouteUpstreamPruneState=_FsPimCmnIpMRouteUpstreamPruneState_Object((1,3,6,1,4,1,2076,111,1,2,3,1,16),_FsPimCmnIpMRouteUpstreamPruneState_Type())
fsPimCmnIpMRouteUpstreamPruneState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteUpstreamPruneState.setStatus(_A)
_FsPimCmnIpMRouteUpstreamPruneLimitTimer_Type=TimeTicks
_FsPimCmnIpMRouteUpstreamPruneLimitTimer_Object=MibTableColumn
fsPimCmnIpMRouteUpstreamPruneLimitTimer=_FsPimCmnIpMRouteUpstreamPruneLimitTimer_Object((1,3,6,1,4,1,2076,111,1,2,3,1,17),_FsPimCmnIpMRouteUpstreamPruneLimitTimer_Type())
fsPimCmnIpMRouteUpstreamPruneLimitTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteUpstreamPruneLimitTimer.setStatus(_A)
class _FsPimCmnIpMRouteOriginatorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_FsPimCmnIpMRouteOriginatorState_Type.__name__=_C
_FsPimCmnIpMRouteOriginatorState_Object=MibTableColumn
fsPimCmnIpMRouteOriginatorState=_FsPimCmnIpMRouteOriginatorState_Object((1,3,6,1,4,1,2076,111,1,2,3,1,18),_FsPimCmnIpMRouteOriginatorState_Type())
fsPimCmnIpMRouteOriginatorState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteOriginatorState.setStatus(_A)
_FsPimCmnIpMRouteSourceActiveTimer_Type=TimeTicks
_FsPimCmnIpMRouteSourceActiveTimer_Object=MibTableColumn
fsPimCmnIpMRouteSourceActiveTimer=_FsPimCmnIpMRouteSourceActiveTimer_Object((1,3,6,1,4,1,2076,111,1,2,3,1,19),_FsPimCmnIpMRouteSourceActiveTimer_Type())
fsPimCmnIpMRouteSourceActiveTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteSourceActiveTimer.setStatus(_A)
_FsPimCmnIpMRouteStateRefreshTimer_Type=TimeTicks
_FsPimCmnIpMRouteStateRefreshTimer_Object=MibTableColumn
fsPimCmnIpMRouteStateRefreshTimer=_FsPimCmnIpMRouteStateRefreshTimer_Object((1,3,6,1,4,1,2076,111,1,2,3,1,20),_FsPimCmnIpMRouteStateRefreshTimer_Type())
fsPimCmnIpMRouteStateRefreshTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteStateRefreshTimer.setStatus(_A)
_FsPimCmnIpMRouteExpiryTime_Type=TimeTicks
_FsPimCmnIpMRouteExpiryTime_Object=MibTableColumn
fsPimCmnIpMRouteExpiryTime=_FsPimCmnIpMRouteExpiryTime_Object((1,3,6,1,4,1,2076,111,1,2,3,1,21),_FsPimCmnIpMRouteExpiryTime_Type())
fsPimCmnIpMRouteExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteExpiryTime.setStatus(_A)
_FsPimCmnIpMRouteDifferentInIfPackets_Type=Counter32
_FsPimCmnIpMRouteDifferentInIfPackets_Object=MibTableColumn
fsPimCmnIpMRouteDifferentInIfPackets=_FsPimCmnIpMRouteDifferentInIfPackets_Object((1,3,6,1,4,1,2076,111,1,2,3,1,22),_FsPimCmnIpMRouteDifferentInIfPackets_Type())
fsPimCmnIpMRouteDifferentInIfPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteDifferentInIfPackets.setStatus(_A)
_FsPimCmnIpMRouteOctets_Type=Counter32
_FsPimCmnIpMRouteOctets_Object=MibTableColumn
fsPimCmnIpMRouteOctets=_FsPimCmnIpMRouteOctets_Object((1,3,6,1,4,1,2076,111,1,2,3,1,23),_FsPimCmnIpMRouteOctets_Type())
fsPimCmnIpMRouteOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteOctets.setStatus(_A)
_FsPimCmnIpMRouteProtocol_Type=IANAipMRouteProtocol
_FsPimCmnIpMRouteProtocol_Object=MibTableColumn
fsPimCmnIpMRouteProtocol=_FsPimCmnIpMRouteProtocol_Object((1,3,6,1,4,1,2076,111,1,2,3,1,24),_FsPimCmnIpMRouteProtocol_Type())
fsPimCmnIpMRouteProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteProtocol.setStatus(_A)
_FsPimCmnIpMRouteRtProto_Type=IANAipRouteProtocol
_FsPimCmnIpMRouteRtProto_Object=MibTableColumn
fsPimCmnIpMRouteRtProto=_FsPimCmnIpMRouteRtProto_Object((1,3,6,1,4,1,2076,111,1,2,3,1,25),_FsPimCmnIpMRouteRtProto_Type())
fsPimCmnIpMRouteRtProto.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteRtProto.setStatus(_A)
_FsPimCmnIpMRouteRtAddress_Type=InetAddress
_FsPimCmnIpMRouteRtAddress_Object=MibTableColumn
fsPimCmnIpMRouteRtAddress=_FsPimCmnIpMRouteRtAddress_Object((1,3,6,1,4,1,2076,111,1,2,3,1,26),_FsPimCmnIpMRouteRtAddress_Type())
fsPimCmnIpMRouteRtAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteRtAddress.setStatus(_A)
_FsPimCmnIpMRouteRtMasklen_Type=Integer32
_FsPimCmnIpMRouteRtMasklen_Object=MibTableColumn
fsPimCmnIpMRouteRtMasklen=_FsPimCmnIpMRouteRtMasklen_Object((1,3,6,1,4,1,2076,111,1,2,3,1,27),_FsPimCmnIpMRouteRtMasklen_Type())
fsPimCmnIpMRouteRtMasklen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteRtMasklen.setStatus(_A)
class _FsPimCmnIpMRouteRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_FsPimCmnIpMRouteRtType_Type.__name__=_C
_FsPimCmnIpMRouteRtType_Object=MibTableColumn
fsPimCmnIpMRouteRtType=_FsPimCmnIpMRouteRtType_Object((1,3,6,1,4,1,2076,111,1,2,3,1,28),_FsPimCmnIpMRouteRtType_Type())
fsPimCmnIpMRouteRtType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteRtType.setStatus(_A)
_FsPimCmnIpMRouteHCOctets_Type=Counter64
_FsPimCmnIpMRouteHCOctets_Object=MibTableColumn
fsPimCmnIpMRouteHCOctets=_FsPimCmnIpMRouteHCOctets_Object((1,3,6,1,4,1,2076,111,1,2,3,1,29),_FsPimCmnIpMRouteHCOctets_Type())
fsPimCmnIpMRouteHCOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteHCOctets.setStatus(_A)
_FsPimCmnIpMRouteOIfList_Type=PortList
_FsPimCmnIpMRouteOIfList_Object=MibTableColumn
fsPimCmnIpMRouteOIfList=_FsPimCmnIpMRouteOIfList_Object((1,3,6,1,4,1,2076,111,1,2,3,1,30),_FsPimCmnIpMRouteOIfList_Type())
fsPimCmnIpMRouteOIfList.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteOIfList.setStatus(_A)
_FsPimCmnIpMRouteRPFVectorAddr_Type=InetAddress
_FsPimCmnIpMRouteRPFVectorAddr_Object=MibTableColumn
fsPimCmnIpMRouteRPFVectorAddr=_FsPimCmnIpMRouteRPFVectorAddr_Object((1,3,6,1,4,1,2076,111,1,2,3,1,31),_FsPimCmnIpMRouteRPFVectorAddr_Type())
fsPimCmnIpMRouteRPFVectorAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteRPFVectorAddr.setStatus(_A)
class _FsPimCmnIpMRoutePimMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dm',1),(_P,2),('ssm',3),(_Q,4)))
_FsPimCmnIpMRoutePimMode_Type.__name__=_C
_FsPimCmnIpMRoutePimMode_Object=MibTableColumn
fsPimCmnIpMRoutePimMode=_FsPimCmnIpMRoutePimMode_Object((1,3,6,1,4,1,2076,111,1,2,3,1,32),_FsPimCmnIpMRoutePimMode_Type())
fsPimCmnIpMRoutePimMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRoutePimMode.setStatus(_A)
_FsPimCmnIpMRouteNextHopTable_Object=MibTable
fsPimCmnIpMRouteNextHopTable=_FsPimCmnIpMRouteNextHopTable_Object((1,3,6,1,4,1,2076,111,1,2,4))
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopTable.setStatus(_A)
_FsPimCmnIpMRouteNextHopEntry_Object=MibTableRow
fsPimCmnIpMRouteNextHopEntry=_FsPimCmnIpMRouteNextHopEntry_Object((1,3,6,1,4,1,2076,111,1,2,4,1))
fsPimCmnIpMRouteNextHopEntry.setIndexNames((0,_D,_j),(0,_D,_k),(0,_D,_l),(0,_D,_m),(0,_D,_n),(0,_D,_o),(0,_D,_p))
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopEntry.setStatus(_A)
class _FsPimCmnIpMRouteNextHopCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnIpMRouteNextHopCompId_Type.__name__=_C
_FsPimCmnIpMRouteNextHopCompId_Object=MibTableColumn
fsPimCmnIpMRouteNextHopCompId=_FsPimCmnIpMRouteNextHopCompId_Object((1,3,6,1,4,1,2076,111,1,2,4,1,1),_FsPimCmnIpMRouteNextHopCompId_Type())
fsPimCmnIpMRouteNextHopCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopCompId.setStatus(_A)
_FsPimCmnIpMRouteNextHopAddrType_Type=InetAddressType
_FsPimCmnIpMRouteNextHopAddrType_Object=MibTableColumn
fsPimCmnIpMRouteNextHopAddrType=_FsPimCmnIpMRouteNextHopAddrType_Object((1,3,6,1,4,1,2076,111,1,2,4,1,2),_FsPimCmnIpMRouteNextHopAddrType_Type())
fsPimCmnIpMRouteNextHopAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopAddrType.setStatus(_A)
_FsPimCmnIpMRouteNextHopGroup_Type=InetAddress
_FsPimCmnIpMRouteNextHopGroup_Object=MibTableColumn
fsPimCmnIpMRouteNextHopGroup=_FsPimCmnIpMRouteNextHopGroup_Object((1,3,6,1,4,1,2076,111,1,2,4,1,3),_FsPimCmnIpMRouteNextHopGroup_Type())
fsPimCmnIpMRouteNextHopGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopGroup.setStatus(_A)
_FsPimCmnIpMRouteNextHopSource_Type=InetAddress
_FsPimCmnIpMRouteNextHopSource_Object=MibTableColumn
fsPimCmnIpMRouteNextHopSource=_FsPimCmnIpMRouteNextHopSource_Object((1,3,6,1,4,1,2076,111,1,2,4,1,4),_FsPimCmnIpMRouteNextHopSource_Type())
fsPimCmnIpMRouteNextHopSource.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopSource.setStatus(_A)
class _FsPimCmnIpMRouteNextHopSourceMasklen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimCmnIpMRouteNextHopSourceMasklen_Type.__name__=_C
_FsPimCmnIpMRouteNextHopSourceMasklen_Object=MibTableColumn
fsPimCmnIpMRouteNextHopSourceMasklen=_FsPimCmnIpMRouteNextHopSourceMasklen_Object((1,3,6,1,4,1,2076,111,1,2,4,1,5),_FsPimCmnIpMRouteNextHopSourceMasklen_Type())
fsPimCmnIpMRouteNextHopSourceMasklen.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopSourceMasklen.setStatus(_A)
class _FsPimCmnIpMRouteNextHopIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimCmnIpMRouteNextHopIfIndex_Type.__name__=_C
_FsPimCmnIpMRouteNextHopIfIndex_Object=MibTableColumn
fsPimCmnIpMRouteNextHopIfIndex=_FsPimCmnIpMRouteNextHopIfIndex_Object((1,3,6,1,4,1,2076,111,1,2,4,1,6),_FsPimCmnIpMRouteNextHopIfIndex_Type())
fsPimCmnIpMRouteNextHopIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopIfIndex.setStatus(_A)
_FsPimCmnIpMRouteNextHopAddress_Type=InetAddress
_FsPimCmnIpMRouteNextHopAddress_Object=MibTableColumn
fsPimCmnIpMRouteNextHopAddress=_FsPimCmnIpMRouteNextHopAddress_Object((1,3,6,1,4,1,2076,111,1,2,4,1,7),_FsPimCmnIpMRouteNextHopAddress_Type())
fsPimCmnIpMRouteNextHopAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopAddress.setStatus(_A)
class _FsPimCmnIpMRouteNextHopPruneReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_L,0),('other',1),('prune',2),(_q,3)))
_FsPimCmnIpMRouteNextHopPruneReason_Type.__name__=_C
_FsPimCmnIpMRouteNextHopPruneReason_Object=MibTableColumn
fsPimCmnIpMRouteNextHopPruneReason=_FsPimCmnIpMRouteNextHopPruneReason_Object((1,3,6,1,4,1,2076,111,1,2,4,1,8),_FsPimCmnIpMRouteNextHopPruneReason_Type())
fsPimCmnIpMRouteNextHopPruneReason.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopPruneReason.setStatus(_A)
class _FsPimCmnIpMRouteNextHopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_L,2)))
_FsPimCmnIpMRouteNextHopState_Type.__name__=_C
_FsPimCmnIpMRouteNextHopState_Object=MibTableColumn
fsPimCmnIpMRouteNextHopState=_FsPimCmnIpMRouteNextHopState_Object((1,3,6,1,4,1,2076,111,1,2,4,1,9),_FsPimCmnIpMRouteNextHopState_Type())
fsPimCmnIpMRouteNextHopState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopState.setStatus(_A)
_FsPimCmnIpMRouteNextHopUpTime_Type=TimeTicks
_FsPimCmnIpMRouteNextHopUpTime_Object=MibTableColumn
fsPimCmnIpMRouteNextHopUpTime=_FsPimCmnIpMRouteNextHopUpTime_Object((1,3,6,1,4,1,2076,111,1,2,4,1,10),_FsPimCmnIpMRouteNextHopUpTime_Type())
fsPimCmnIpMRouteNextHopUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopUpTime.setStatus(_A)
_FsPimCmnIpMRouteNextHopExpiryTime_Type=TimeTicks
_FsPimCmnIpMRouteNextHopExpiryTime_Object=MibTableColumn
fsPimCmnIpMRouteNextHopExpiryTime=_FsPimCmnIpMRouteNextHopExpiryTime_Object((1,3,6,1,4,1,2076,111,1,2,4,1,11),_FsPimCmnIpMRouteNextHopExpiryTime_Type())
fsPimCmnIpMRouteNextHopExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopExpiryTime.setStatus(_A)
_FsPimCmnIpMRouteNextHopProtocol_Type=IANAipMRouteProtocol
_FsPimCmnIpMRouteNextHopProtocol_Object=MibTableColumn
fsPimCmnIpMRouteNextHopProtocol=_FsPimCmnIpMRouteNextHopProtocol_Object((1,3,6,1,4,1,2076,111,1,2,4,1,12),_FsPimCmnIpMRouteNextHopProtocol_Type())
fsPimCmnIpMRouteNextHopProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopProtocol.setStatus(_A)
_FsPimCmnIpMRouteNextHopPkts_Type=Counter32
_FsPimCmnIpMRouteNextHopPkts_Object=MibTableColumn
fsPimCmnIpMRouteNextHopPkts=_FsPimCmnIpMRouteNextHopPkts_Object((1,3,6,1,4,1,2076,111,1,2,4,1,13),_FsPimCmnIpMRouteNextHopPkts_Type())
fsPimCmnIpMRouteNextHopPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopPkts.setStatus(_A)
_FsPimCmnCandidateRPTable_Object=MibTable
fsPimCmnCandidateRPTable=_FsPimCmnCandidateRPTable_Object((1,3,6,1,4,1,2076,111,1,2,6))
if mibBuilder.loadTexts:fsPimCmnCandidateRPTable.setStatus(_A)
_FsPimCmnCandidateRPEntry_Object=MibTableRow
fsPimCmnCandidateRPEntry=_FsPimCmnCandidateRPEntry_Object((1,3,6,1,4,1,2076,111,1,2,6,1))
fsPimCmnCandidateRPEntry.setIndexNames((0,_D,_r),(0,_D,_s),(0,_D,_t),(0,_D,_u),(0,_D,_v))
if mibBuilder.loadTexts:fsPimCmnCandidateRPEntry.setStatus(_A)
class _FsPimCmnCandidateRPCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnCandidateRPCompId_Type.__name__=_C
_FsPimCmnCandidateRPCompId_Object=MibTableColumn
fsPimCmnCandidateRPCompId=_FsPimCmnCandidateRPCompId_Object((1,3,6,1,4,1,2076,111,1,2,6,1,1),_FsPimCmnCandidateRPCompId_Type())
fsPimCmnCandidateRPCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnCandidateRPCompId.setStatus(_A)
_FsPimCmnCandidateRPAddrType_Type=InetAddressType
_FsPimCmnCandidateRPAddrType_Object=MibTableColumn
fsPimCmnCandidateRPAddrType=_FsPimCmnCandidateRPAddrType_Object((1,3,6,1,4,1,2076,111,1,2,6,1,2),_FsPimCmnCandidateRPAddrType_Type())
fsPimCmnCandidateRPAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnCandidateRPAddrType.setStatus(_A)
_FsPimCmnCandidateRPGroupAddress_Type=InetAddress
_FsPimCmnCandidateRPGroupAddress_Object=MibTableColumn
fsPimCmnCandidateRPGroupAddress=_FsPimCmnCandidateRPGroupAddress_Object((1,3,6,1,4,1,2076,111,1,2,6,1,3),_FsPimCmnCandidateRPGroupAddress_Type())
fsPimCmnCandidateRPGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnCandidateRPGroupAddress.setStatus(_A)
class _FsPimCmnCandidateRPGroupMasklen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimCmnCandidateRPGroupMasklen_Type.__name__=_C
_FsPimCmnCandidateRPGroupMasklen_Object=MibTableColumn
fsPimCmnCandidateRPGroupMasklen=_FsPimCmnCandidateRPGroupMasklen_Object((1,3,6,1,4,1,2076,111,1,2,6,1,4),_FsPimCmnCandidateRPGroupMasklen_Type())
fsPimCmnCandidateRPGroupMasklen.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnCandidateRPGroupMasklen.setStatus(_A)
_FsPimCmnCandidateRPAddress_Type=InetAddress
_FsPimCmnCandidateRPAddress_Object=MibTableColumn
fsPimCmnCandidateRPAddress=_FsPimCmnCandidateRPAddress_Object((1,3,6,1,4,1,2076,111,1,2,6,1,5),_FsPimCmnCandidateRPAddress_Type())
fsPimCmnCandidateRPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnCandidateRPAddress.setStatus(_A)
class _FsPimCmnCandidateRPPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPimCmnCandidateRPPriority_Type.__name__=_C
_FsPimCmnCandidateRPPriority_Object=MibTableColumn
fsPimCmnCandidateRPPriority=_FsPimCmnCandidateRPPriority_Object((1,3,6,1,4,1,2076,111,1,2,6,1,6),_FsPimCmnCandidateRPPriority_Type())
fsPimCmnCandidateRPPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnCandidateRPPriority.setStatus(_A)
_FsPimCmnCandidateRPRowStatus_Type=RowStatus
_FsPimCmnCandidateRPRowStatus_Object=MibTableColumn
fsPimCmnCandidateRPRowStatus=_FsPimCmnCandidateRPRowStatus_Object((1,3,6,1,4,1,2076,111,1,2,6,1,7),_FsPimCmnCandidateRPRowStatus_Type())
fsPimCmnCandidateRPRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:fsPimCmnCandidateRPRowStatus.setStatus(_A)
class _FsPimCmnCandidateRPPimMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*((_P,2),(_Q,4)))
_FsPimCmnCandidateRPPimMode_Type.__name__=_C
_FsPimCmnCandidateRPPimMode_Object=MibTableColumn
fsPimCmnCandidateRPPimMode=_FsPimCmnCandidateRPPimMode_Object((1,3,6,1,4,1,2076,111,1,2,6,1,8),_FsPimCmnCandidateRPPimMode_Type())
fsPimCmnCandidateRPPimMode.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnCandidateRPPimMode.setStatus(_A)
_FsPimCmnStaticRPSetTable_Object=MibTable
fsPimCmnStaticRPSetTable=_FsPimCmnStaticRPSetTable_Object((1,3,6,1,4,1,2076,111,1,2,7))
if mibBuilder.loadTexts:fsPimCmnStaticRPSetTable.setStatus(_A)
_FsPimCmnStaticRPSetEntry_Object=MibTableRow
fsPimCmnStaticRPSetEntry=_FsPimCmnStaticRPSetEntry_Object((1,3,6,1,4,1,2076,111,1,2,7,1))
fsPimCmnStaticRPSetEntry.setIndexNames((0,_D,_w),(0,_D,_x),(0,_D,_y),(0,_D,_z))
if mibBuilder.loadTexts:fsPimCmnStaticRPSetEntry.setStatus(_A)
class _FsPimCmnStaticRPSetCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnStaticRPSetCompId_Type.__name__=_C
_FsPimCmnStaticRPSetCompId_Object=MibTableColumn
fsPimCmnStaticRPSetCompId=_FsPimCmnStaticRPSetCompId_Object((1,3,6,1,4,1,2076,111,1,2,7,1,1),_FsPimCmnStaticRPSetCompId_Type())
fsPimCmnStaticRPSetCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnStaticRPSetCompId.setStatus(_A)
_FsPimCmnStaticRPAddrType_Type=InetAddressType
_FsPimCmnStaticRPAddrType_Object=MibTableColumn
fsPimCmnStaticRPAddrType=_FsPimCmnStaticRPAddrType_Object((1,3,6,1,4,1,2076,111,1,2,7,1,2),_FsPimCmnStaticRPAddrType_Type())
fsPimCmnStaticRPAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnStaticRPAddrType.setStatus(_A)
_FsPimCmnStaticRPSetGroupAddress_Type=InetAddress
_FsPimCmnStaticRPSetGroupAddress_Object=MibTableColumn
fsPimCmnStaticRPSetGroupAddress=_FsPimCmnStaticRPSetGroupAddress_Object((1,3,6,1,4,1,2076,111,1,2,7,1,3),_FsPimCmnStaticRPSetGroupAddress_Type())
fsPimCmnStaticRPSetGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnStaticRPSetGroupAddress.setStatus(_A)
class _FsPimCmnStaticRPSetGroupMasklen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimCmnStaticRPSetGroupMasklen_Type.__name__=_C
_FsPimCmnStaticRPSetGroupMasklen_Object=MibTableColumn
fsPimCmnStaticRPSetGroupMasklen=_FsPimCmnStaticRPSetGroupMasklen_Object((1,3,6,1,4,1,2076,111,1,2,7,1,4),_FsPimCmnStaticRPSetGroupMasklen_Type())
fsPimCmnStaticRPSetGroupMasklen.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnStaticRPSetGroupMasklen.setStatus(_A)
_FsPimCmnStaticRPAddress_Type=InetAddress
_FsPimCmnStaticRPAddress_Object=MibTableColumn
fsPimCmnStaticRPAddress=_FsPimCmnStaticRPAddress_Object((1,3,6,1,4,1,2076,111,1,2,7,1,5),_FsPimCmnStaticRPAddress_Type())
fsPimCmnStaticRPAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:fsPimCmnStaticRPAddress.setStatus(_A)
_FsPimCmnStaticRPRowStatus_Type=RowStatus
_FsPimCmnStaticRPRowStatus_Object=MibTableColumn
fsPimCmnStaticRPRowStatus=_FsPimCmnStaticRPRowStatus_Object((1,3,6,1,4,1,2076,111,1,2,7,1,6),_FsPimCmnStaticRPRowStatus_Type())
fsPimCmnStaticRPRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:fsPimCmnStaticRPRowStatus.setStatus(_A)
class _FsPimCmnStaticRPEmbdFlag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_H,1)))
_FsPimCmnStaticRPEmbdFlag_Type.__name__=_C
_FsPimCmnStaticRPEmbdFlag_Object=MibTableColumn
fsPimCmnStaticRPEmbdFlag=_FsPimCmnStaticRPEmbdFlag_Object((1,3,6,1,4,1,2076,111,1,2,7,1,7),_FsPimCmnStaticRPEmbdFlag_Type())
fsPimCmnStaticRPEmbdFlag.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnStaticRPEmbdFlag.setStatus(_A)
class _FsPimCmnStaticRPPimMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*((_P,2),(_Q,4)))
_FsPimCmnStaticRPPimMode_Type.__name__=_C
_FsPimCmnStaticRPPimMode_Object=MibTableColumn
fsPimCmnStaticRPPimMode=_FsPimCmnStaticRPPimMode_Object((1,3,6,1,4,1,2076,111,1,2,7,1,8),_FsPimCmnStaticRPPimMode_Type())
fsPimCmnStaticRPPimMode.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnStaticRPPimMode.setStatus(_A)
_FsPimCmnComponentModeTable_Object=MibTable
fsPimCmnComponentModeTable=_FsPimCmnComponentModeTable_Object((1,3,6,1,4,1,2076,111,1,2,8))
if mibBuilder.loadTexts:fsPimCmnComponentModeTable.setStatus(_A)
_FsPimCmnComponentModeEntry_Object=MibTableRow
fsPimCmnComponentModeEntry=_FsPimCmnComponentModeEntry_Object((1,3,6,1,4,1,2076,111,1,2,8,1))
fsPimCmnComponentModeEntry.setIndexNames((0,_D,_A0))
if mibBuilder.loadTexts:fsPimCmnComponentModeEntry.setStatus(_A)
class _FsPimCmnComponentId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnComponentId_Type.__name__=_C
_FsPimCmnComponentId_Object=MibTableColumn
fsPimCmnComponentId=_FsPimCmnComponentId_Object((1,3,6,1,4,1,2076,111,1,2,8,1,1),_FsPimCmnComponentId_Type())
fsPimCmnComponentId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnComponentId.setStatus(_A)
class _FsPimCmnComponentMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dense',1),('sparse',2)))
_FsPimCmnComponentMode_Type.__name__=_C
_FsPimCmnComponentMode_Object=MibTableColumn
fsPimCmnComponentMode=_FsPimCmnComponentMode_Object((1,3,6,1,4,1,2076,111,1,2,8,1,2),_FsPimCmnComponentMode_Type())
fsPimCmnComponentMode.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnComponentMode.setStatus(_A)
class _FsPimCmnCompGraftRetryCount_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPimCmnCompGraftRetryCount_Type.__name__=_C
_FsPimCmnCompGraftRetryCount_Object=MibTableColumn
fsPimCmnCompGraftRetryCount=_FsPimCmnCompGraftRetryCount_Object((1,3,6,1,4,1,2076,111,1,2,8,1,3),_FsPimCmnCompGraftRetryCount_Type())
fsPimCmnCompGraftRetryCount.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnCompGraftRetryCount.setStatus(_A)
_FsPimCmnRegChkSumCfgTable_Object=MibTable
fsPimCmnRegChkSumCfgTable=_FsPimCmnRegChkSumCfgTable_Object((1,3,6,1,4,1,2076,111,1,2,9))
if mibBuilder.loadTexts:fsPimCmnRegChkSumCfgTable.setStatus(_A)
_FsPimCmnRegChkSumCfgEntry_Object=MibTableRow
fsPimCmnRegChkSumCfgEntry=_FsPimCmnRegChkSumCfgEntry_Object((1,3,6,1,4,1,2076,111,1,2,9,1))
fsPimCmnRegChkSumCfgEntry.setIndexNames((0,_D,_A1),(0,_D,_A2),(0,_D,_A3))
if mibBuilder.loadTexts:fsPimCmnRegChkSumCfgEntry.setStatus(_A)
class _FsPimCmnRegChkSumTblCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnRegChkSumTblCompId_Type.__name__=_C
_FsPimCmnRegChkSumTblCompId_Object=MibTableColumn
fsPimCmnRegChkSumTblCompId=_FsPimCmnRegChkSumTblCompId_Object((1,3,6,1,4,1,2076,111,1,2,9,1,1),_FsPimCmnRegChkSumTblCompId_Type())
fsPimCmnRegChkSumTblCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnRegChkSumTblCompId.setStatus(_A)
_FsPimCmnRegChkSumTblRPAddrType_Type=InetAddressType
_FsPimCmnRegChkSumTblRPAddrType_Object=MibTableColumn
fsPimCmnRegChkSumTblRPAddrType=_FsPimCmnRegChkSumTblRPAddrType_Object((1,3,6,1,4,1,2076,111,1,2,9,1,2),_FsPimCmnRegChkSumTblRPAddrType_Type())
fsPimCmnRegChkSumTblRPAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnRegChkSumTblRPAddrType.setStatus(_A)
_FsPimCmnRegChkSumTblRPAddress_Type=InetAddress
_FsPimCmnRegChkSumTblRPAddress_Object=MibTableColumn
fsPimCmnRegChkSumTblRPAddress=_FsPimCmnRegChkSumTblRPAddress_Object((1,3,6,1,4,1,2076,111,1,2,9,1,3),_FsPimCmnRegChkSumTblRPAddress_Type())
fsPimCmnRegChkSumTblRPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnRegChkSumTblRPAddress.setStatus(_A)
class _FsPimCmnRPChkSumStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsPimCmnRPChkSumStatus_Type.__name__=_C
_FsPimCmnRPChkSumStatus_Object=MibTableColumn
fsPimCmnRPChkSumStatus=_FsPimCmnRPChkSumStatus_Object((1,3,6,1,4,1,2076,111,1,2,9,1,4),_FsPimCmnRPChkSumStatus_Type())
fsPimCmnRPChkSumStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnRPChkSumStatus.setStatus(_A)
_FsPimCmnDFTable_Object=MibTable
fsPimCmnDFTable=_FsPimCmnDFTable_Object((1,3,6,1,4,1,2076,111,1,2,10))
if mibBuilder.loadTexts:fsPimCmnDFTable.setStatus(_A)
_FsPimCmnDFEntry_Object=MibTableRow
fsPimCmnDFEntry=_FsPimCmnDFEntry_Object((1,3,6,1,4,1,2076,111,1,2,10,1))
fsPimCmnDFEntry.setIndexNames((0,_D,_A4),(0,_D,_A5),(0,_D,_A6))
if mibBuilder.loadTexts:fsPimCmnDFEntry.setStatus(_A)
_FsPimCmnDFIfAddrType_Type=InetAddressType
_FsPimCmnDFIfAddrType_Object=MibTableColumn
fsPimCmnDFIfAddrType=_FsPimCmnDFIfAddrType_Object((1,3,6,1,4,1,2076,111,1,2,10,1,1),_FsPimCmnDFIfAddrType_Type())
fsPimCmnDFIfAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnDFIfAddrType.setStatus(_A)
_FsPimCmnDFElectedRP_Type=InetAddress
_FsPimCmnDFElectedRP_Object=MibTableColumn
fsPimCmnDFElectedRP=_FsPimCmnDFElectedRP_Object((1,3,6,1,4,1,2076,111,1,2,10,1,2),_FsPimCmnDFElectedRP_Type())
fsPimCmnDFElectedRP.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnDFElectedRP.setStatus(_A)
class _FsPimCmnDFIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimCmnDFIfIndex_Type.__name__=_C
_FsPimCmnDFIfIndex_Object=MibTableColumn
fsPimCmnDFIfIndex=_FsPimCmnDFIfIndex_Object((1,3,6,1,4,1,2076,111,1,2,10,1,3),_FsPimCmnDFIfIndex_Type())
fsPimCmnDFIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnDFIfIndex.setStatus(_A)
class _FsPimCmnDFState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('offer',1),('winner',2),('backoff',3),('lose',4)))
_FsPimCmnDFState_Type.__name__=_C
_FsPimCmnDFState_Object=MibTableColumn
fsPimCmnDFState=_FsPimCmnDFState_Object((1,3,6,1,4,1,2076,111,1,2,10,1,4),_FsPimCmnDFState_Type())
fsPimCmnDFState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnDFState.setStatus(_A)
_FsPimCmnDFWinnerAddr_Type=InetAddress
_FsPimCmnDFWinnerAddr_Object=MibTableColumn
fsPimCmnDFWinnerAddr=_FsPimCmnDFWinnerAddr_Object((1,3,6,1,4,1,2076,111,1,2,10,1,5),_FsPimCmnDFWinnerAddr_Type())
fsPimCmnDFWinnerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnDFWinnerAddr.setStatus(_A)
_FsPimCmnDFWinnerUptime_Type=TimeTicks
_FsPimCmnDFWinnerUptime_Object=MibTableColumn
fsPimCmnDFWinnerUptime=_FsPimCmnDFWinnerUptime_Object((1,3,6,1,4,1,2076,111,1,2,10,1,6),_FsPimCmnDFWinnerUptime_Type())
fsPimCmnDFWinnerUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnDFWinnerUptime.setStatus(_A)
_FsPimCmnDFElectionStateTimer_Type=TimeTicks
_FsPimCmnDFElectionStateTimer_Object=MibTableColumn
fsPimCmnDFElectionStateTimer=_FsPimCmnDFElectionStateTimer_Object((1,3,6,1,4,1,2076,111,1,2,10,1,7),_FsPimCmnDFElectionStateTimer_Type())
fsPimCmnDFElectionStateTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnDFElectionStateTimer.setStatus(_A)
_FsPimCmnDFWinnerMetric_Type=Unsigned32
_FsPimCmnDFWinnerMetric_Object=MibTableColumn
fsPimCmnDFWinnerMetric=_FsPimCmnDFWinnerMetric_Object((1,3,6,1,4,1,2076,111,1,2,10,1,8),_FsPimCmnDFWinnerMetric_Type())
fsPimCmnDFWinnerMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnDFWinnerMetric.setStatus(_A)
_FsPimCmnDFWinnerMetricPref_Type=Unsigned32
_FsPimCmnDFWinnerMetricPref_Object=MibTableColumn
fsPimCmnDFWinnerMetricPref=_FsPimCmnDFWinnerMetricPref_Object((1,3,6,1,4,1,2076,111,1,2,10,1,9),_FsPimCmnDFWinnerMetricPref_Type())
fsPimCmnDFWinnerMetricPref.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnDFWinnerMetricPref.setStatus(_A)
class _FsPimCmnDFMessageCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimCmnDFMessageCount_Type.__name__=_C
_FsPimCmnDFMessageCount_Object=MibTableColumn
fsPimCmnDFMessageCount=_FsPimCmnDFMessageCount_Object((1,3,6,1,4,1,2076,111,1,2,10,1,10),_FsPimCmnDFMessageCount_Type())
fsPimCmnDFMessageCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnDFMessageCount.setStatus(_A)
_FsPimCmnElectedRPTable_Object=MibTable
fsPimCmnElectedRPTable=_FsPimCmnElectedRPTable_Object((1,3,6,1,4,1,2076,111,1,2,11))
if mibBuilder.loadTexts:fsPimCmnElectedRPTable.setStatus(_A)
_FsPimCmnElectedRPEntry_Object=MibTableRow
fsPimCmnElectedRPEntry=_FsPimCmnElectedRPEntry_Object((1,3,6,1,4,1,2076,111,1,2,11,1))
fsPimCmnElectedRPEntry.setIndexNames((0,_D,_A7),(0,_D,_A8),(0,_D,_A9),(0,_D,_AA))
if mibBuilder.loadTexts:fsPimCmnElectedRPEntry.setStatus(_A)
class _FsPimCmnElectedRPCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnElectedRPCompId_Type.__name__=_C
_FsPimCmnElectedRPCompId_Object=MibTableColumn
fsPimCmnElectedRPCompId=_FsPimCmnElectedRPCompId_Object((1,3,6,1,4,1,2076,111,1,2,11,1,1),_FsPimCmnElectedRPCompId_Type())
fsPimCmnElectedRPCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnElectedRPCompId.setStatus(_A)
_FsPimCmnElectedRPAddrType_Type=InetAddressType
_FsPimCmnElectedRPAddrType_Object=MibTableColumn
fsPimCmnElectedRPAddrType=_FsPimCmnElectedRPAddrType_Object((1,3,6,1,4,1,2076,111,1,2,11,1,2),_FsPimCmnElectedRPAddrType_Type())
fsPimCmnElectedRPAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnElectedRPAddrType.setStatus(_A)
_FsPimCmnElectedRPGroupAddress_Type=InetAddress
_FsPimCmnElectedRPGroupAddress_Object=MibTableColumn
fsPimCmnElectedRPGroupAddress=_FsPimCmnElectedRPGroupAddress_Object((1,3,6,1,4,1,2076,111,1,2,11,1,3),_FsPimCmnElectedRPGroupAddress_Type())
fsPimCmnElectedRPGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnElectedRPGroupAddress.setStatus(_A)
class _FsPimCmnElectedRPGroupMasklen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimCmnElectedRPGroupMasklen_Type.__name__=_C
_FsPimCmnElectedRPGroupMasklen_Object=MibTableColumn
fsPimCmnElectedRPGroupMasklen=_FsPimCmnElectedRPGroupMasklen_Object((1,3,6,1,4,1,2076,111,1,2,11,1,4),_FsPimCmnElectedRPGroupMasklen_Type())
fsPimCmnElectedRPGroupMasklen.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnElectedRPGroupMasklen.setStatus(_A)
_FsPimCmnElectedRPAddress_Type=InetAddress
_FsPimCmnElectedRPAddress_Object=MibTableColumn
fsPimCmnElectedRPAddress=_FsPimCmnElectedRPAddress_Object((1,3,6,1,4,1,2076,111,1,2,11,1,5),_FsPimCmnElectedRPAddress_Type())
fsPimCmnElectedRPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnElectedRPAddress.setStatus(_A)
class _FsPimCmnElectedRPPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPimCmnElectedRPPriority_Type.__name__=_C
_FsPimCmnElectedRPPriority_Object=MibTableColumn
fsPimCmnElectedRPPriority=_FsPimCmnElectedRPPriority_Object((1,3,6,1,4,1,2076,111,1,2,11,1,6),_FsPimCmnElectedRPPriority_Type())
fsPimCmnElectedRPPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnElectedRPPriority.setStatus(_A)
class _FsPimCmnElectedRPHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimCmnElectedRPHoldTime_Type.__name__=_C
_FsPimCmnElectedRPHoldTime_Object=MibTableColumn
fsPimCmnElectedRPHoldTime=_FsPimCmnElectedRPHoldTime_Object((1,3,6,1,4,1,2076,111,1,2,11,1,7),_FsPimCmnElectedRPHoldTime_Type())
fsPimCmnElectedRPHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnElectedRPHoldTime.setStatus(_A)
class _FsPimCmnElectedRPUpTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimCmnElectedRPUpTime_Type.__name__=_C
_FsPimCmnElectedRPUpTime_Object=MibTableColumn
fsPimCmnElectedRPUpTime=_FsPimCmnElectedRPUpTime_Object((1,3,6,1,4,1,2076,111,1,2,11,1,8),_FsPimCmnElectedRPUpTime_Type())
fsPimCmnElectedRPUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnElectedRPUpTime.setStatus(_A)
_FsPimCmnNeighborExtTable_Object=MibTable
fsPimCmnNeighborExtTable=_FsPimCmnNeighborExtTable_Object((1,3,6,1,4,1,2076,111,1,2,12))
if mibBuilder.loadTexts:fsPimCmnNeighborExtTable.setStatus(_A)
_FsPimCmnNeighborExtEntry_Object=MibTableRow
fsPimCmnNeighborExtEntry=_FsPimCmnNeighborExtEntry_Object((1,3,6,1,4,1,2076,111,1,2,12,1))
fsPimCmnNeighborExtEntry.setIndexNames((0,_D,_AB),(0,_D,_AC),(0,_D,_AD))
if mibBuilder.loadTexts:fsPimCmnNeighborExtEntry.setStatus(_A)
_FsPimCmnNeighborExtIfIndex_Type=Integer32
_FsPimCmnNeighborExtIfIndex_Object=MibTableColumn
fsPimCmnNeighborExtIfIndex=_FsPimCmnNeighborExtIfIndex_Object((1,3,6,1,4,1,2076,111,1,2,12,1,1),_FsPimCmnNeighborExtIfIndex_Type())
fsPimCmnNeighborExtIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnNeighborExtIfIndex.setStatus(_A)
_FsPimCmnNeighborExtAddrType_Type=InetAddressType
_FsPimCmnNeighborExtAddrType_Object=MibTableColumn
fsPimCmnNeighborExtAddrType=_FsPimCmnNeighborExtAddrType_Object((1,3,6,1,4,1,2076,111,1,2,12,1,2),_FsPimCmnNeighborExtAddrType_Type())
fsPimCmnNeighborExtAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnNeighborExtAddrType.setStatus(_A)
_FsPimCmnNeighborExtAddress_Type=InetAddress
_FsPimCmnNeighborExtAddress_Object=MibTableColumn
fsPimCmnNeighborExtAddress=_FsPimCmnNeighborExtAddress_Object((1,3,6,1,4,1,2076,111,1,2,12,1,3),_FsPimCmnNeighborExtAddress_Type())
fsPimCmnNeighborExtAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnNeighborExtAddress.setStatus(_A)
_FsPimCmnNeighborExtCompIdList_Type=CompList
_FsPimCmnNeighborExtCompIdList_Object=MibTableColumn
fsPimCmnNeighborExtCompIdList=_FsPimCmnNeighborExtCompIdList_Object((1,3,6,1,4,1,2076,111,1,2,12,1,4),_FsPimCmnNeighborExtCompIdList_Type())
fsPimCmnNeighborExtCompIdList.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtCompIdList.setStatus(_A)
_FsPimCmnNeighborExtUpTime_Type=TimeTicks
_FsPimCmnNeighborExtUpTime_Object=MibTableColumn
fsPimCmnNeighborExtUpTime=_FsPimCmnNeighborExtUpTime_Object((1,3,6,1,4,1,2076,111,1,2,12,1,5),_FsPimCmnNeighborExtUpTime_Type())
fsPimCmnNeighborExtUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtUpTime.setStatus(_A)
_FsPimCmnNeighborExtExpiryTime_Type=TimeTicks
_FsPimCmnNeighborExtExpiryTime_Object=MibTableColumn
fsPimCmnNeighborExtExpiryTime=_FsPimCmnNeighborExtExpiryTime_Object((1,3,6,1,4,1,2076,111,1,2,12,1,6),_FsPimCmnNeighborExtExpiryTime_Type())
fsPimCmnNeighborExtExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtExpiryTime.setStatus(_A)
_FsPimCmnNeighborExtGenerationId_Type=Integer32
_FsPimCmnNeighborExtGenerationId_Object=MibTableColumn
fsPimCmnNeighborExtGenerationId=_FsPimCmnNeighborExtGenerationId_Object((1,3,6,1,4,1,2076,111,1,2,12,1,7),_FsPimCmnNeighborExtGenerationId_Type())
fsPimCmnNeighborExtGenerationId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtGenerationId.setStatus(_A)
_FsPimCmnNeighborExtLanDelay_Type=Integer32
_FsPimCmnNeighborExtLanDelay_Object=MibTableColumn
fsPimCmnNeighborExtLanDelay=_FsPimCmnNeighborExtLanDelay_Object((1,3,6,1,4,1,2076,111,1,2,12,1,8),_FsPimCmnNeighborExtLanDelay_Type())
fsPimCmnNeighborExtLanDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtLanDelay.setStatus(_A)
_FsPimCmnNeighborExtDRPriority_Type=Unsigned32
_FsPimCmnNeighborExtDRPriority_Object=MibTableColumn
fsPimCmnNeighborExtDRPriority=_FsPimCmnNeighborExtDRPriority_Object((1,3,6,1,4,1,2076,111,1,2,12,1,9),_FsPimCmnNeighborExtDRPriority_Type())
fsPimCmnNeighborExtDRPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtDRPriority.setStatus(_A)
_FsPimCmnNeighborExtOverrideInterval_Type=Integer32
_FsPimCmnNeighborExtOverrideInterval_Object=MibTableColumn
fsPimCmnNeighborExtOverrideInterval=_FsPimCmnNeighborExtOverrideInterval_Object((1,3,6,1,4,1,2076,111,1,2,12,1,10),_FsPimCmnNeighborExtOverrideInterval_Type())
fsPimCmnNeighborExtOverrideInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtOverrideInterval.setStatus(_A)
_FsPimCmnNeighborExtSRCapable_Type=TruthValue
_FsPimCmnNeighborExtSRCapable_Object=MibTableColumn
fsPimCmnNeighborExtSRCapable=_FsPimCmnNeighborExtSRCapable_Object((1,3,6,1,4,1,2076,111,1,2,12,1,11),_FsPimCmnNeighborExtSRCapable_Type())
fsPimCmnNeighborExtSRCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtSRCapable.setStatus(_A)
_FsPimCmnNeighborExtRPFCapable_Type=TruthValue
_FsPimCmnNeighborExtRPFCapable_Object=MibTableColumn
fsPimCmnNeighborExtRPFCapable=_FsPimCmnNeighborExtRPFCapable_Object((1,3,6,1,4,1,2076,111,1,2,12,1,12),_FsPimCmnNeighborExtRPFCapable_Type())
fsPimCmnNeighborExtRPFCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtRPFCapable.setStatus(_A)
_FsPimCmnNeighborExtBidirCapable_Type=TruthValue
_FsPimCmnNeighborExtBidirCapable_Object=MibTableColumn
fsPimCmnNeighborExtBidirCapable=_FsPimCmnNeighborExtBidirCapable_Object((1,3,6,1,4,1,2076,111,1,2,12,1,13),_FsPimCmnNeighborExtBidirCapable_Type())
fsPimCmnNeighborExtBidirCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtBidirCapable.setStatus(_A)
_FsPimCmnIpGenMRouteTable_Object=MibTable
fsPimCmnIpGenMRouteTable=_FsPimCmnIpGenMRouteTable_Object((1,3,6,1,4,1,2076,111,1,2,13))
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteTable.setStatus(_A)
_FsPimCmnIpGenMRouteEntry_Object=MibTableRow
fsPimCmnIpGenMRouteEntry=_FsPimCmnIpGenMRouteEntry_Object((1,3,6,1,4,1,2076,111,1,2,13,1))
fsPimCmnIpGenMRouteEntry.setIndexNames((0,_D,_AE),(0,_D,_AF),(0,_D,_AG),(0,_D,_AH),(0,_D,_AI),(0,_D,_AJ))
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteEntry.setStatus(_A)
class _FsPimCmnIpGenMRouteCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnIpGenMRouteCompId_Type.__name__=_C
_FsPimCmnIpGenMRouteCompId_Object=MibTableColumn
fsPimCmnIpGenMRouteCompId=_FsPimCmnIpGenMRouteCompId_Object((1,3,6,1,4,1,2076,111,1,2,13,1,1),_FsPimCmnIpGenMRouteCompId_Type())
fsPimCmnIpGenMRouteCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteCompId.setStatus(_A)
_FsPimCmnIpGenMRouteAddrType_Type=InetAddressType
_FsPimCmnIpGenMRouteAddrType_Object=MibTableColumn
fsPimCmnIpGenMRouteAddrType=_FsPimCmnIpGenMRouteAddrType_Object((1,3,6,1,4,1,2076,111,1,2,13,1,2),_FsPimCmnIpGenMRouteAddrType_Type())
fsPimCmnIpGenMRouteAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteAddrType.setStatus(_A)
_FsPimCmnIpGenMRouteGroup_Type=InetAddress
_FsPimCmnIpGenMRouteGroup_Object=MibTableColumn
fsPimCmnIpGenMRouteGroup=_FsPimCmnIpGenMRouteGroup_Object((1,3,6,1,4,1,2076,111,1,2,13,1,3),_FsPimCmnIpGenMRouteGroup_Type())
fsPimCmnIpGenMRouteGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteGroup.setStatus(_A)
class _FsPimCmnIpGenMRouteGroupMasklen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimCmnIpGenMRouteGroupMasklen_Type.__name__=_C
_FsPimCmnIpGenMRouteGroupMasklen_Object=MibTableColumn
fsPimCmnIpGenMRouteGroupMasklen=_FsPimCmnIpGenMRouteGroupMasklen_Object((1,3,6,1,4,1,2076,111,1,2,13,1,4),_FsPimCmnIpGenMRouteGroupMasklen_Type())
fsPimCmnIpGenMRouteGroupMasklen.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteGroupMasklen.setStatus(_A)
_FsPimCmnIpGenMRouteSource_Type=InetAddress
_FsPimCmnIpGenMRouteSource_Object=MibTableColumn
fsPimCmnIpGenMRouteSource=_FsPimCmnIpGenMRouteSource_Object((1,3,6,1,4,1,2076,111,1,2,13,1,5),_FsPimCmnIpGenMRouteSource_Type())
fsPimCmnIpGenMRouteSource.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteSource.setStatus(_A)
class _FsPimCmnIpGenMRouteSourceMasklen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimCmnIpGenMRouteSourceMasklen_Type.__name__=_C
_FsPimCmnIpGenMRouteSourceMasklen_Object=MibTableColumn
fsPimCmnIpGenMRouteSourceMasklen=_FsPimCmnIpGenMRouteSourceMasklen_Object((1,3,6,1,4,1,2076,111,1,2,13,1,6),_FsPimCmnIpGenMRouteSourceMasklen_Type())
fsPimCmnIpGenMRouteSourceMasklen.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteSourceMasklen.setStatus(_A)
_FsPimCmnIpGenMRouteUpstreamNeighbor_Type=InetAddress
_FsPimCmnIpGenMRouteUpstreamNeighbor_Object=MibTableColumn
fsPimCmnIpGenMRouteUpstreamNeighbor=_FsPimCmnIpGenMRouteUpstreamNeighbor_Object((1,3,6,1,4,1,2076,111,1,2,13,1,7),_FsPimCmnIpGenMRouteUpstreamNeighbor_Type())
fsPimCmnIpGenMRouteUpstreamNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteUpstreamNeighbor.setStatus(_A)
_FsPimCmnIpGenMRouteInIfIndex_Type=Integer32
_FsPimCmnIpGenMRouteInIfIndex_Object=MibTableColumn
fsPimCmnIpGenMRouteInIfIndex=_FsPimCmnIpGenMRouteInIfIndex_Object((1,3,6,1,4,1,2076,111,1,2,13,1,8),_FsPimCmnIpGenMRouteInIfIndex_Type())
fsPimCmnIpGenMRouteInIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteInIfIndex.setStatus(_A)
_FsPimCmnIpGenMRouteUpTime_Type=TimeTicks
_FsPimCmnIpGenMRouteUpTime_Object=MibTableColumn
fsPimCmnIpGenMRouteUpTime=_FsPimCmnIpGenMRouteUpTime_Object((1,3,6,1,4,1,2076,111,1,2,13,1,9),_FsPimCmnIpGenMRouteUpTime_Type())
fsPimCmnIpGenMRouteUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteUpTime.setStatus(_A)
_FsPimCmnIpGenMRoutePkts_Type=Counter32
_FsPimCmnIpGenMRoutePkts_Object=MibTableColumn
fsPimCmnIpGenMRoutePkts=_FsPimCmnIpGenMRoutePkts_Object((1,3,6,1,4,1,2076,111,1,2,13,1,10),_FsPimCmnIpGenMRoutePkts_Type())
fsPimCmnIpGenMRoutePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRoutePkts.setStatus(_A)
_FsPimCmnIpGenMRouteUpstreamAssertTimer_Type=TimeTicks
_FsPimCmnIpGenMRouteUpstreamAssertTimer_Object=MibTableColumn
fsPimCmnIpGenMRouteUpstreamAssertTimer=_FsPimCmnIpGenMRouteUpstreamAssertTimer_Object((1,3,6,1,4,1,2076,111,1,2,13,1,11),_FsPimCmnIpGenMRouteUpstreamAssertTimer_Type())
fsPimCmnIpGenMRouteUpstreamAssertTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteUpstreamAssertTimer.setStatus(_A)
_FsPimCmnIpGenMRouteAssertMetric_Type=Integer32
_FsPimCmnIpGenMRouteAssertMetric_Object=MibTableColumn
fsPimCmnIpGenMRouteAssertMetric=_FsPimCmnIpGenMRouteAssertMetric_Object((1,3,6,1,4,1,2076,111,1,2,13,1,12),_FsPimCmnIpGenMRouteAssertMetric_Type())
fsPimCmnIpGenMRouteAssertMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteAssertMetric.setStatus(_A)
_FsPimCmnIpGenMRouteAssertMetricPref_Type=Integer32
_FsPimCmnIpGenMRouteAssertMetricPref_Object=MibTableColumn
fsPimCmnIpGenMRouteAssertMetricPref=_FsPimCmnIpGenMRouteAssertMetricPref_Object((1,3,6,1,4,1,2076,111,1,2,13,1,13),_FsPimCmnIpGenMRouteAssertMetricPref_Type())
fsPimCmnIpGenMRouteAssertMetricPref.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteAssertMetricPref.setStatus(_A)
_FsPimCmnIpGenMRouteAssertRPTBit_Type=TruthValue
_FsPimCmnIpGenMRouteAssertRPTBit_Object=MibTableColumn
fsPimCmnIpGenMRouteAssertRPTBit=_FsPimCmnIpGenMRouteAssertRPTBit_Object((1,3,6,1,4,1,2076,111,1,2,13,1,14),_FsPimCmnIpGenMRouteAssertRPTBit_Type())
fsPimCmnIpGenMRouteAssertRPTBit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteAssertRPTBit.setStatus(_A)
_FsPimCmnIpGenMRouteTimerFlags_Type=Integer32
_FsPimCmnIpGenMRouteTimerFlags_Object=MibTableColumn
fsPimCmnIpGenMRouteTimerFlags=_FsPimCmnIpGenMRouteTimerFlags_Object((1,3,6,1,4,1,2076,111,1,2,13,1,15),_FsPimCmnIpGenMRouteTimerFlags_Type())
fsPimCmnIpGenMRouteTimerFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteTimerFlags.setStatus(_A)
_FsPimCmnIpGenMRouteFlags_Type=Integer32
_FsPimCmnIpGenMRouteFlags_Object=MibTableColumn
fsPimCmnIpGenMRouteFlags=_FsPimCmnIpGenMRouteFlags_Object((1,3,6,1,4,1,2076,111,1,2,13,1,16),_FsPimCmnIpGenMRouteFlags_Type())
fsPimCmnIpGenMRouteFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteFlags.setStatus(_A)
class _FsPimCmnIpGenMRouteUpstreamPruneState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_e,2),(_O,3)))
_FsPimCmnIpGenMRouteUpstreamPruneState_Type.__name__=_C
_FsPimCmnIpGenMRouteUpstreamPruneState_Object=MibTableColumn
fsPimCmnIpGenMRouteUpstreamPruneState=_FsPimCmnIpGenMRouteUpstreamPruneState_Object((1,3,6,1,4,1,2076,111,1,2,13,1,17),_FsPimCmnIpGenMRouteUpstreamPruneState_Type())
fsPimCmnIpGenMRouteUpstreamPruneState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteUpstreamPruneState.setStatus(_A)
_FsPimCmnIpGenMRouteUpstreamPruneLimitTimer_Type=TimeTicks
_FsPimCmnIpGenMRouteUpstreamPruneLimitTimer_Object=MibTableColumn
fsPimCmnIpGenMRouteUpstreamPruneLimitTimer=_FsPimCmnIpGenMRouteUpstreamPruneLimitTimer_Object((1,3,6,1,4,1,2076,111,1,2,13,1,18),_FsPimCmnIpGenMRouteUpstreamPruneLimitTimer_Type())
fsPimCmnIpGenMRouteUpstreamPruneLimitTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteUpstreamPruneLimitTimer.setStatus(_A)
class _FsPimCmnIpGenMRouteOriginatorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_FsPimCmnIpGenMRouteOriginatorState_Type.__name__=_C
_FsPimCmnIpGenMRouteOriginatorState_Object=MibTableColumn
fsPimCmnIpGenMRouteOriginatorState=_FsPimCmnIpGenMRouteOriginatorState_Object((1,3,6,1,4,1,2076,111,1,2,13,1,19),_FsPimCmnIpGenMRouteOriginatorState_Type())
fsPimCmnIpGenMRouteOriginatorState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteOriginatorState.setStatus(_A)
_FsPimCmnIpGenMRouteSourceActiveTimer_Type=TimeTicks
_FsPimCmnIpGenMRouteSourceActiveTimer_Object=MibTableColumn
fsPimCmnIpGenMRouteSourceActiveTimer=_FsPimCmnIpGenMRouteSourceActiveTimer_Object((1,3,6,1,4,1,2076,111,1,2,13,1,20),_FsPimCmnIpGenMRouteSourceActiveTimer_Type())
fsPimCmnIpGenMRouteSourceActiveTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteSourceActiveTimer.setStatus(_A)
_FsPimCmnIpGenMRouteStateRefreshTimer_Type=TimeTicks
_FsPimCmnIpGenMRouteStateRefreshTimer_Object=MibTableColumn
fsPimCmnIpGenMRouteStateRefreshTimer=_FsPimCmnIpGenMRouteStateRefreshTimer_Object((1,3,6,1,4,1,2076,111,1,2,13,1,21),_FsPimCmnIpGenMRouteStateRefreshTimer_Type())
fsPimCmnIpGenMRouteStateRefreshTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteStateRefreshTimer.setStatus(_A)
_FsPimCmnIpGenMRouteExpiryTime_Type=TimeTicks
_FsPimCmnIpGenMRouteExpiryTime_Object=MibTableColumn
fsPimCmnIpGenMRouteExpiryTime=_FsPimCmnIpGenMRouteExpiryTime_Object((1,3,6,1,4,1,2076,111,1,2,13,1,22),_FsPimCmnIpGenMRouteExpiryTime_Type())
fsPimCmnIpGenMRouteExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteExpiryTime.setStatus(_A)
_FsPimCmnIpGenMRouteDifferentInIfPackets_Type=Counter32
_FsPimCmnIpGenMRouteDifferentInIfPackets_Object=MibTableColumn
fsPimCmnIpGenMRouteDifferentInIfPackets=_FsPimCmnIpGenMRouteDifferentInIfPackets_Object((1,3,6,1,4,1,2076,111,1,2,13,1,23),_FsPimCmnIpGenMRouteDifferentInIfPackets_Type())
fsPimCmnIpGenMRouteDifferentInIfPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteDifferentInIfPackets.setStatus(_A)
_FsPimCmnIpGenMRouteOctets_Type=Counter32
_FsPimCmnIpGenMRouteOctets_Object=MibTableColumn
fsPimCmnIpGenMRouteOctets=_FsPimCmnIpGenMRouteOctets_Object((1,3,6,1,4,1,2076,111,1,2,13,1,24),_FsPimCmnIpGenMRouteOctets_Type())
fsPimCmnIpGenMRouteOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteOctets.setStatus(_A)
_FsPimCmnIpGenMRouteProtocol_Type=IANAipMRouteProtocol
_FsPimCmnIpGenMRouteProtocol_Object=MibTableColumn
fsPimCmnIpGenMRouteProtocol=_FsPimCmnIpGenMRouteProtocol_Object((1,3,6,1,4,1,2076,111,1,2,13,1,25),_FsPimCmnIpGenMRouteProtocol_Type())
fsPimCmnIpGenMRouteProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteProtocol.setStatus(_A)
_FsPimCmnIpGenMRouteRtProto_Type=IANAipRouteProtocol
_FsPimCmnIpGenMRouteRtProto_Object=MibTableColumn
fsPimCmnIpGenMRouteRtProto=_FsPimCmnIpGenMRouteRtProto_Object((1,3,6,1,4,1,2076,111,1,2,13,1,26),_FsPimCmnIpGenMRouteRtProto_Type())
fsPimCmnIpGenMRouteRtProto.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteRtProto.setStatus(_A)
_FsPimCmnIpGenMRouteRtAddress_Type=InetAddress
_FsPimCmnIpGenMRouteRtAddress_Object=MibTableColumn
fsPimCmnIpGenMRouteRtAddress=_FsPimCmnIpGenMRouteRtAddress_Object((1,3,6,1,4,1,2076,111,1,2,13,1,27),_FsPimCmnIpGenMRouteRtAddress_Type())
fsPimCmnIpGenMRouteRtAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteRtAddress.setStatus(_A)
_FsPimCmnIpGenMRouteRtMasklen_Type=Integer32
_FsPimCmnIpGenMRouteRtMasklen_Object=MibTableColumn
fsPimCmnIpGenMRouteRtMasklen=_FsPimCmnIpGenMRouteRtMasklen_Object((1,3,6,1,4,1,2076,111,1,2,13,1,28),_FsPimCmnIpGenMRouteRtMasklen_Type())
fsPimCmnIpGenMRouteRtMasklen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteRtMasklen.setStatus(_A)
class _FsPimCmnIpGenMRouteRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_FsPimCmnIpGenMRouteRtType_Type.__name__=_C
_FsPimCmnIpGenMRouteRtType_Object=MibTableColumn
fsPimCmnIpGenMRouteRtType=_FsPimCmnIpGenMRouteRtType_Object((1,3,6,1,4,1,2076,111,1,2,13,1,29),_FsPimCmnIpGenMRouteRtType_Type())
fsPimCmnIpGenMRouteRtType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteRtType.setStatus(_A)
_FsPimCmnIpGenMRouteHCOctets_Type=Counter64
_FsPimCmnIpGenMRouteHCOctets_Object=MibTableColumn
fsPimCmnIpGenMRouteHCOctets=_FsPimCmnIpGenMRouteHCOctets_Object((1,3,6,1,4,1,2076,111,1,2,13,1,30),_FsPimCmnIpGenMRouteHCOctets_Type())
fsPimCmnIpGenMRouteHCOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteHCOctets.setStatus(_A)
_FsPimCmnIpGenMRouteOIfList_Type=PortList
_FsPimCmnIpGenMRouteOIfList_Object=MibTableColumn
fsPimCmnIpGenMRouteOIfList=_FsPimCmnIpGenMRouteOIfList_Object((1,3,6,1,4,1,2076,111,1,2,13,1,31),_FsPimCmnIpGenMRouteOIfList_Type())
fsPimCmnIpGenMRouteOIfList.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteOIfList.setStatus(_A)
_FsPimCmnIpGenMRouteRPFVectorAddr_Type=InetAddress
_FsPimCmnIpGenMRouteRPFVectorAddr_Object=MibTableColumn
fsPimCmnIpGenMRouteRPFVectorAddr=_FsPimCmnIpGenMRouteRPFVectorAddr_Object((1,3,6,1,4,1,2076,111,1,2,13,1,32),_FsPimCmnIpGenMRouteRPFVectorAddr_Type())
fsPimCmnIpGenMRouteRPFVectorAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteRPFVectorAddr.setStatus(_A)
class _FsPimCmnIpGenMRoutePimMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dm',1),(_P,2),('ssm',3),(_Q,4)))
_FsPimCmnIpGenMRoutePimMode_Type.__name__=_C
_FsPimCmnIpGenMRoutePimMode_Object=MibTableColumn
fsPimCmnIpGenMRoutePimMode=_FsPimCmnIpGenMRoutePimMode_Object((1,3,6,1,4,1,2076,111,1,2,13,1,33),_FsPimCmnIpGenMRoutePimMode_Type())
fsPimCmnIpGenMRoutePimMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRoutePimMode.setStatus(_A)
class _FsPimCmnIpGenMRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*(('default',0),('sg',1),('sgrpt',2),('starg',4),('ssrp',8)))
_FsPimCmnIpGenMRouteType_Type.__name__=_C
_FsPimCmnIpGenMRouteType_Object=MibTableColumn
fsPimCmnIpGenMRouteType=_FsPimCmnIpGenMRouteType_Object((1,3,6,1,4,1,2076,111,1,2,13,1,34),_FsPimCmnIpGenMRouteType_Type())
fsPimCmnIpGenMRouteType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteType.setStatus(_A)
_FsPimCmnIpGenMRouteNPStatus_Type=Integer32
_FsPimCmnIpGenMRouteNPStatus_Object=MibTableColumn
fsPimCmnIpGenMRouteNPStatus=_FsPimCmnIpGenMRouteNPStatus_Object((1,3,6,1,4,1,2076,111,1,2,13,1,35),_FsPimCmnIpGenMRouteNPStatus_Type())
fsPimCmnIpGenMRouteNPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNPStatus.setStatus(_A)
_FsPimCmnIpGenMRouteNextHopTable_Object=MibTable
fsPimCmnIpGenMRouteNextHopTable=_FsPimCmnIpGenMRouteNextHopTable_Object((1,3,6,1,4,1,2076,111,1,2,14))
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopTable.setStatus(_A)
_FsPimCmnIpGenMRouteNextHopEntry_Object=MibTableRow
fsPimCmnIpGenMRouteNextHopEntry=_FsPimCmnIpGenMRouteNextHopEntry_Object((1,3,6,1,4,1,2076,111,1,2,14,1))
fsPimCmnIpGenMRouteNextHopEntry.setIndexNames((0,_D,_AK),(0,_D,_AL),(0,_D,_AM),(0,_D,_AN),(0,_D,_AO),(0,_D,_AP),(0,_D,_AQ),(0,_D,_AR))
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopEntry.setStatus(_A)
class _FsPimCmnIpGenMRouteNextHopCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnIpGenMRouteNextHopCompId_Type.__name__=_C
_FsPimCmnIpGenMRouteNextHopCompId_Object=MibTableColumn
fsPimCmnIpGenMRouteNextHopCompId=_FsPimCmnIpGenMRouteNextHopCompId_Object((1,3,6,1,4,1,2076,111,1,2,14,1,1),_FsPimCmnIpGenMRouteNextHopCompId_Type())
fsPimCmnIpGenMRouteNextHopCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopCompId.setStatus(_A)
_FsPimCmnIpGenMRouteNextHopAddrType_Type=InetAddressType
_FsPimCmnIpGenMRouteNextHopAddrType_Object=MibTableColumn
fsPimCmnIpGenMRouteNextHopAddrType=_FsPimCmnIpGenMRouteNextHopAddrType_Object((1,3,6,1,4,1,2076,111,1,2,14,1,2),_FsPimCmnIpGenMRouteNextHopAddrType_Type())
fsPimCmnIpGenMRouteNextHopAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopAddrType.setStatus(_A)
_FsPimCmnIpGenMRouteNextHopGroup_Type=InetAddress
_FsPimCmnIpGenMRouteNextHopGroup_Object=MibTableColumn
fsPimCmnIpGenMRouteNextHopGroup=_FsPimCmnIpGenMRouteNextHopGroup_Object((1,3,6,1,4,1,2076,111,1,2,14,1,3),_FsPimCmnIpGenMRouteNextHopGroup_Type())
fsPimCmnIpGenMRouteNextHopGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopGroup.setStatus(_A)
class _FsPimCmnIpGenMRouteNextHopGroupMasklen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimCmnIpGenMRouteNextHopGroupMasklen_Type.__name__=_C
_FsPimCmnIpGenMRouteNextHopGroupMasklen_Object=MibTableColumn
fsPimCmnIpGenMRouteNextHopGroupMasklen=_FsPimCmnIpGenMRouteNextHopGroupMasklen_Object((1,3,6,1,4,1,2076,111,1,2,14,1,4),_FsPimCmnIpGenMRouteNextHopGroupMasklen_Type())
fsPimCmnIpGenMRouteNextHopGroupMasklen.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopGroupMasklen.setStatus(_A)
_FsPimCmnIpGenMRouteNextHopSource_Type=InetAddress
_FsPimCmnIpGenMRouteNextHopSource_Object=MibTableColumn
fsPimCmnIpGenMRouteNextHopSource=_FsPimCmnIpGenMRouteNextHopSource_Object((1,3,6,1,4,1,2076,111,1,2,14,1,5),_FsPimCmnIpGenMRouteNextHopSource_Type())
fsPimCmnIpGenMRouteNextHopSource.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopSource.setStatus(_A)
class _FsPimCmnIpGenMRouteNextHopSourceMasklen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimCmnIpGenMRouteNextHopSourceMasklen_Type.__name__=_C
_FsPimCmnIpGenMRouteNextHopSourceMasklen_Object=MibTableColumn
fsPimCmnIpGenMRouteNextHopSourceMasklen=_FsPimCmnIpGenMRouteNextHopSourceMasklen_Object((1,3,6,1,4,1,2076,111,1,2,14,1,6),_FsPimCmnIpGenMRouteNextHopSourceMasklen_Type())
fsPimCmnIpGenMRouteNextHopSourceMasklen.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopSourceMasklen.setStatus(_A)
class _FsPimCmnIpGenMRouteNextHopIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimCmnIpGenMRouteNextHopIfIndex_Type.__name__=_C
_FsPimCmnIpGenMRouteNextHopIfIndex_Object=MibTableColumn
fsPimCmnIpGenMRouteNextHopIfIndex=_FsPimCmnIpGenMRouteNextHopIfIndex_Object((1,3,6,1,4,1,2076,111,1,2,14,1,7),_FsPimCmnIpGenMRouteNextHopIfIndex_Type())
fsPimCmnIpGenMRouteNextHopIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopIfIndex.setStatus(_A)
_FsPimCmnIpGenMRouteNextHopAddress_Type=InetAddress
_FsPimCmnIpGenMRouteNextHopAddress_Object=MibTableColumn
fsPimCmnIpGenMRouteNextHopAddress=_FsPimCmnIpGenMRouteNextHopAddress_Object((1,3,6,1,4,1,2076,111,1,2,14,1,8),_FsPimCmnIpGenMRouteNextHopAddress_Type())
fsPimCmnIpGenMRouteNextHopAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopAddress.setStatus(_A)
class _FsPimCmnIpGenMRouteNextHopPruneReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_L,0),('other',1),('prune',2),(_q,3)))
_FsPimCmnIpGenMRouteNextHopPruneReason_Type.__name__=_C
_FsPimCmnIpGenMRouteNextHopPruneReason_Object=MibTableColumn
fsPimCmnIpGenMRouteNextHopPruneReason=_FsPimCmnIpGenMRouteNextHopPruneReason_Object((1,3,6,1,4,1,2076,111,1,2,14,1,9),_FsPimCmnIpGenMRouteNextHopPruneReason_Type())
fsPimCmnIpGenMRouteNextHopPruneReason.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopPruneReason.setStatus(_A)
class _FsPimCmnIpGenMRouteNextHopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_L,2)))
_FsPimCmnIpGenMRouteNextHopState_Type.__name__=_C
_FsPimCmnIpGenMRouteNextHopState_Object=MibTableColumn
fsPimCmnIpGenMRouteNextHopState=_FsPimCmnIpGenMRouteNextHopState_Object((1,3,6,1,4,1,2076,111,1,2,14,1,10),_FsPimCmnIpGenMRouteNextHopState_Type())
fsPimCmnIpGenMRouteNextHopState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopState.setStatus(_A)
_FsPimCmnIpGenMRouteNextHopUpTime_Type=TimeTicks
_FsPimCmnIpGenMRouteNextHopUpTime_Object=MibTableColumn
fsPimCmnIpGenMRouteNextHopUpTime=_FsPimCmnIpGenMRouteNextHopUpTime_Object((1,3,6,1,4,1,2076,111,1,2,14,1,11),_FsPimCmnIpGenMRouteNextHopUpTime_Type())
fsPimCmnIpGenMRouteNextHopUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopUpTime.setStatus(_A)
_FsPimCmnIpGenMRouteNextHopExpiryTime_Type=TimeTicks
_FsPimCmnIpGenMRouteNextHopExpiryTime_Object=MibTableColumn
fsPimCmnIpGenMRouteNextHopExpiryTime=_FsPimCmnIpGenMRouteNextHopExpiryTime_Object((1,3,6,1,4,1,2076,111,1,2,14,1,12),_FsPimCmnIpGenMRouteNextHopExpiryTime_Type())
fsPimCmnIpGenMRouteNextHopExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopExpiryTime.setStatus(_A)
_FsPimCmnIpGenMRouteNextHopProtocol_Type=IANAipMRouteProtocol
_FsPimCmnIpGenMRouteNextHopProtocol_Object=MibTableColumn
fsPimCmnIpGenMRouteNextHopProtocol=_FsPimCmnIpGenMRouteNextHopProtocol_Object((1,3,6,1,4,1,2076,111,1,2,14,1,13),_FsPimCmnIpGenMRouteNextHopProtocol_Type())
fsPimCmnIpGenMRouteNextHopProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopProtocol.setStatus(_A)
_FsPimCmnIpGenMRouteNextHopPkts_Type=Counter32
_FsPimCmnIpGenMRouteNextHopPkts_Object=MibTableColumn
fsPimCmnIpGenMRouteNextHopPkts=_FsPimCmnIpGenMRouteNextHopPkts_Object((1,3,6,1,4,1,2076,111,1,2,14,1,14),_FsPimCmnIpGenMRouteNextHopPkts_Type())
fsPimCmnIpGenMRouteNextHopPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopPkts.setStatus(_A)
_FsPimCmnIpGenMRouteNextHopNPStatus_Type=Integer32
_FsPimCmnIpGenMRouteNextHopNPStatus_Object=MibTableColumn
fsPimCmnIpGenMRouteNextHopNPStatus=_FsPimCmnIpGenMRouteNextHopNPStatus_Object((1,3,6,1,4,1,2076,111,1,2,14,1,15),_FsPimCmnIpGenMRouteNextHopNPStatus_Type())
fsPimCmnIpGenMRouteNextHopNPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpGenMRouteNextHopNPStatus.setStatus(_A)
_FuturePimCmnTrapsControl_ObjectIdentity=ObjectIdentity
futurePimCmnTrapsControl=_FuturePimCmnTrapsControl_ObjectIdentity((1,3,6,1,4,1,2076,111,1,3))
_FsPimcmnHARtrId_Type=IpAddress
_FsPimcmnHARtrId_Object=MibScalar
fsPimcmnHARtrId=_FsPimcmnHARtrId_Object((1,3,6,1,4,1,2076,111,1,3,1),_FsPimcmnHARtrId_Type())
fsPimcmnHARtrId.setMaxAccess(_AS)
if mibBuilder.loadTexts:fsPimcmnHARtrId.setStatus(_A)
class _FsPimCmnHAEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('standbyInstanceUP',1),('standbyInstanceDown',2),('instancesSwitchover',3),('dynamicBulkupdateStart',4),('dynamicBulkupdateComplete',5),('dynamicBulkupdateAborted',6)))
_FsPimCmnHAEvent_Type.__name__=_C
_FsPimCmnHAEvent_Object=MibScalar
fsPimCmnHAEvent=_FsPimCmnHAEvent_Object((1,3,6,1,4,1,2076,111,1,3,3),_FsPimCmnHAEvent_Type())
fsPimCmnHAEvent.setMaxAccess(_AS)
if mibBuilder.loadTexts:fsPimCmnHAEvent.setStatus(_A)
_FuturePimCmnTraps_ObjectIdentity=ObjectIdentity
futurePimCmnTraps=_FuturePimCmnTraps_ObjectIdentity((1,3,6,1,4,1,2076,111,1,4))
_FsPimCmnTraps_ObjectIdentity=ObjectIdentity
fsPimCmnTraps=_FsPimCmnTraps_ObjectIdentity((1,3,6,1,4,1,2076,111,1,4,0))
fsPimCmnHAEventTrap=NotificationType((1,3,6,1,4,1,2076,111,1,4,0,1))
fsPimCmnHAEventTrap.setObjects(*((_D,_U),(_D,_AT)))
if mibBuilder.loadTexts:fsPimCmnHAEventTrap.setStatus(_A)
fsPimCmnBidirEventTrap=NotificationType((1,3,6,1,4,1,2076,111,1,4,0,2))
fsPimCmnBidirEventTrap.setObjects(*((_D,_U),(_D,_T),(_D,_AU)))
if mibBuilder.loadTexts:fsPimCmnBidirEventTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'Status':Status,'CompList':CompList,'fsPimCmnMIB':fsPimCmnMIB,'fsPimCmnMIBObjects':fsPimCmnMIBObjects,'futurePimCmnScalars':futurePimCmnScalars,'fsPimCmnVersionString':fsPimCmnVersionString,'fsPimCmnSPTGroupThreshold':fsPimCmnSPTGroupThreshold,'fsPimCmnSPTSourceThreshold':fsPimCmnSPTSourceThreshold,'fsPimCmnSPTSwitchingPeriod':fsPimCmnSPTSwitchingPeriod,'fsPimCmnSPTRpThreshold':fsPimCmnSPTRpThreshold,'fsPimCmnSPTRpSwitchingPeriod':fsPimCmnSPTRpSwitchingPeriod,'fsPimCmnRegStopRateLimitingPeriod':fsPimCmnRegStopRateLimitingPeriod,'fsPimCmnMemoryAllocFailCount':fsPimCmnMemoryAllocFailCount,'fsPimCmnGlobalTrace':fsPimCmnGlobalTrace,'fsPimCmnGlobalDebug':fsPimCmnGlobalDebug,'fsPimCmnPmbrStatus':fsPimCmnPmbrStatus,'fsPimCmnRouterMode':fsPimCmnRouterMode,'fsPimCmnStaticRpEnabled':fsPimCmnStaticRpEnabled,'fsPimCmnIpStatus':fsPimCmnIpStatus,'fsPimCmnIpv6Status':fsPimCmnIpv6Status,'fsPimCmnSRProcessingStatus':fsPimCmnSRProcessingStatus,'fsPimCmnRefreshInterval':fsPimCmnRefreshInterval,'fsPimCmnSourceActiveInterval':fsPimCmnSourceActiveInterval,'fsPimCmnHAAdminStatus':fsPimCmnHAAdminStatus,'fsPimCmnHAState':fsPimCmnHAState,'fsPimCmnHADynamicBulkUpdStatus':fsPimCmnHADynamicBulkUpdStatus,'fsPimCmnHAForwardingTblEntryCnt':fsPimCmnHAForwardingTblEntryCnt,'fsPimCmnIpRpfVector':fsPimCmnIpRpfVector,'fsPimCmnIpBidirPIMStatus':fsPimCmnIpBidirPIMStatus,'fsPimCmnIpBidirOfferInterval':fsPimCmnIpBidirOfferInterval,'fsPimCmnIpBidirOfferLimit':fsPimCmnIpBidirOfferLimit,'futurePimCmnTables':futurePimCmnTables,'fsPimCmnInterfaceTable':fsPimCmnInterfaceTable,'fsPimCmnInterfaceEntry':fsPimCmnInterfaceEntry,_V:fsPimCmnInterfaceIfIndex,_W:fsPimCmnInterfaceAddrType,'fsPimCmnInterfaceCompId':fsPimCmnInterfaceCompId,'fsPimCmnInterfaceDRPriority':fsPimCmnInterfaceDRPriority,'fsPimCmnInterfaceHelloHoldTime':fsPimCmnInterfaceHelloHoldTime,'fsPimCmnInterfaceLanPruneDelayPresent':fsPimCmnInterfaceLanPruneDelayPresent,'fsPimCmnInterfaceLanDelay':fsPimCmnInterfaceLanDelay,'fsPimCmnInterfaceOverrideInterval':fsPimCmnInterfaceOverrideInterval,'fsPimCmnInterfaceGenerationId':fsPimCmnInterfaceGenerationId,'fsPimCmnInterfaceSuppressionInterval':fsPimCmnInterfaceSuppressionInterval,'fsPimCmnInterfaceAdminStatus':fsPimCmnInterfaceAdminStatus,'fsPimCmnInterfaceBorderBit':fsPimCmnInterfaceBorderBit,'fsPimCmnInterfaceGraftRetryInterval':fsPimCmnInterfaceGraftRetryInterval,'fsPimCmnInterfaceSRPriorityEnabled':fsPimCmnInterfaceSRPriorityEnabled,'fsPimCmnInterfaceTtl':fsPimCmnInterfaceTtl,'fsPimCmnInterfaceProtocol':fsPimCmnInterfaceProtocol,'fsPimCmnInterfaceRateLimit':fsPimCmnInterfaceRateLimit,'fsPimCmnInterfaceInMcastOctets':fsPimCmnInterfaceInMcastOctets,'fsPimCmnInterfaceOutMcastOctets':fsPimCmnInterfaceOutMcastOctets,'fsPimCmnInterfaceHCInMcastOctets':fsPimCmnInterfaceHCInMcastOctets,'fsPimCmnInterfaceHCOutMcastOctets':fsPimCmnInterfaceHCOutMcastOctets,'fsPimCmnInterfaceCompIdList':fsPimCmnInterfaceCompIdList,'fsPimCmnInterfaceDFOfferSentPkts':fsPimCmnInterfaceDFOfferSentPkts,'fsPimCmnInterfaceDFOfferRcvdPkts':fsPimCmnInterfaceDFOfferRcvdPkts,'fsPimCmnInterfaceDFWinnerSentPkts':fsPimCmnInterfaceDFWinnerSentPkts,'fsPimCmnInterfaceDFWinnerRcvdPkts':fsPimCmnInterfaceDFWinnerRcvdPkts,'fsPimCmnInterfaceDFBackoffSentPkts':fsPimCmnInterfaceDFBackoffSentPkts,'fsPimCmnInterfaceDFBackoffRcvdPkts':fsPimCmnInterfaceDFBackoffRcvdPkts,'fsPimCmnInterfaceDFPassSentPkts':fsPimCmnInterfaceDFPassSentPkts,'fsPimCmnInterfaceDFPassRcvdPkts':fsPimCmnInterfaceDFPassRcvdPkts,'fsPimCmnInterfaceCKSumErrorPkts':fsPimCmnInterfaceCKSumErrorPkts,'fsPimCmnInterfaceInvalidTypePkts':fsPimCmnInterfaceInvalidTypePkts,'fsPimCmnInterfaceInvalidDFSubTypePkts':fsPimCmnInterfaceInvalidDFSubTypePkts,'fsPimCmnInterfaceAuthFailPkts':fsPimCmnInterfaceAuthFailPkts,'fsPimCmnInterfaceFromNonNbrsPkts':fsPimCmnInterfaceFromNonNbrsPkts,'fsPimCmnInterfaceJPRcvdOnRPFPkts':fsPimCmnInterfaceJPRcvdOnRPFPkts,'fsPimCmnInterfaceJPRcvdNoRPPkts':fsPimCmnInterfaceJPRcvdNoRPPkts,'fsPimCmnInterfaceJPRcvdWrongRPPkts':fsPimCmnInterfaceJPRcvdWrongRPPkts,'fsPimCmnInterfaceJoinSSMGrpPkts':fsPimCmnInterfaceJoinSSMGrpPkts,'fsPimCmnInterfaceJoinBidirGrpPkts':fsPimCmnInterfaceJoinBidirGrpPkts,'fsPimCmnInterfaceHelloRcvdPkts':fsPimCmnInterfaceHelloRcvdPkts,'fsPimCmnInterfaceHelloSentPkts':fsPimCmnInterfaceHelloSentPkts,'fsPimCmnInterfaceJPRcvdPkts':fsPimCmnInterfaceJPRcvdPkts,'fsPimCmnInterfaceJPSentPkts':fsPimCmnInterfaceJPSentPkts,'fsPimCmnInterfaceAssertRcvdPkts':fsPimCmnInterfaceAssertRcvdPkts,'fsPimCmnInterfaceAssertSentPkts':fsPimCmnInterfaceAssertSentPkts,'fsPimCmnInterfaceGraftRcvdPkts':fsPimCmnInterfaceGraftRcvdPkts,'fsPimCmnInterfaceGraftSentPkts':fsPimCmnInterfaceGraftSentPkts,'fsPimCmnInterfaceGraftAckRcvdPkts':fsPimCmnInterfaceGraftAckRcvdPkts,'fsPimCmnInterfaceGraftAckSentPkts':fsPimCmnInterfaceGraftAckSentPkts,'fsPimCmnInterfacePackLenErrorPkts':fsPimCmnInterfacePackLenErrorPkts,'fsPimCmnInterfaceBadVersionPkts':fsPimCmnInterfaceBadVersionPkts,'fsPimCmnInterfacePktsfromSelf':fsPimCmnInterfacePktsfromSelf,'fsPimCmnInterfaceExtBorderBit':fsPimCmnInterfaceExtBorderBit,'fsPimCmnInterfaceJoinSSMBadPkts':fsPimCmnInterfaceJoinSSMBadPkts,'fsPimCmnNeighborTable':fsPimCmnNeighborTable,'fsPimCmnNeighborEntry':fsPimCmnNeighborEntry,_X:fsPimCmnNeighborCompId,_Y:fsPimCmnNeighborAddrType,_T:fsPimCmnNeighborAddress,_AU:fsPimCmnNeighborIfIndex,'fsPimCmnNeighborUpTime':fsPimCmnNeighborUpTime,'fsPimCmnNeighborExpiryTime':fsPimCmnNeighborExpiryTime,'fsPimCmnNeighborGenerationId':fsPimCmnNeighborGenerationId,'fsPimCmnNeighborLanDelay':fsPimCmnNeighborLanDelay,'fsPimCmnNeighborDRPriority':fsPimCmnNeighborDRPriority,'fsPimCmnNeighborOverrideInterval':fsPimCmnNeighborOverrideInterval,'fsPimCmnNeighborSRCapable':fsPimCmnNeighborSRCapable,'fsPimCmnNeighborRPFCapable':fsPimCmnNeighborRPFCapable,'fsPimCmnNeighborBidirCapable':fsPimCmnNeighborBidirCapable,'fsPimCmnIpMRouteTable':fsPimCmnIpMRouteTable,'fsPimCmnIpMRouteEntry':fsPimCmnIpMRouteEntry,_Z:fsPimCmnIpMRouteCompId,_a:fsPimCmnIpMRouteAddrType,_b:fsPimCmnIpMRouteGroup,_c:fsPimCmnIpMRouteSource,_d:fsPimCmnIpMRouteSourceMasklen,'fsPimCmnIpMRouteUpstreamNeighbor':fsPimCmnIpMRouteUpstreamNeighbor,'fsPimCmnIpMRouteInIfIndex':fsPimCmnIpMRouteInIfIndex,'fsPimCmnIpMRouteUpTime':fsPimCmnIpMRouteUpTime,'fsPimCmnIpMRoutePkts':fsPimCmnIpMRoutePkts,'fsPimCmnIpMRouteUpstreamAssertTimer':fsPimCmnIpMRouteUpstreamAssertTimer,'fsPimCmnIpMRouteAssertMetric':fsPimCmnIpMRouteAssertMetric,'fsPimCmnIpMRouteAssertMetricPref':fsPimCmnIpMRouteAssertMetricPref,'fsPimCmnIpMRouteAssertRPTBit':fsPimCmnIpMRouteAssertRPTBit,'fsPimCmnIpMRouteTimerFlags':fsPimCmnIpMRouteTimerFlags,'fsPimCmnIpMRouteFlags':fsPimCmnIpMRouteFlags,'fsPimCmnIpMRouteUpstreamPruneState':fsPimCmnIpMRouteUpstreamPruneState,'fsPimCmnIpMRouteUpstreamPruneLimitTimer':fsPimCmnIpMRouteUpstreamPruneLimitTimer,'fsPimCmnIpMRouteOriginatorState':fsPimCmnIpMRouteOriginatorState,'fsPimCmnIpMRouteSourceActiveTimer':fsPimCmnIpMRouteSourceActiveTimer,'fsPimCmnIpMRouteStateRefreshTimer':fsPimCmnIpMRouteStateRefreshTimer,'fsPimCmnIpMRouteExpiryTime':fsPimCmnIpMRouteExpiryTime,'fsPimCmnIpMRouteDifferentInIfPackets':fsPimCmnIpMRouteDifferentInIfPackets,'fsPimCmnIpMRouteOctets':fsPimCmnIpMRouteOctets,'fsPimCmnIpMRouteProtocol':fsPimCmnIpMRouteProtocol,'fsPimCmnIpMRouteRtProto':fsPimCmnIpMRouteRtProto,'fsPimCmnIpMRouteRtAddress':fsPimCmnIpMRouteRtAddress,'fsPimCmnIpMRouteRtMasklen':fsPimCmnIpMRouteRtMasklen,'fsPimCmnIpMRouteRtType':fsPimCmnIpMRouteRtType,'fsPimCmnIpMRouteHCOctets':fsPimCmnIpMRouteHCOctets,'fsPimCmnIpMRouteOIfList':fsPimCmnIpMRouteOIfList,'fsPimCmnIpMRouteRPFVectorAddr':fsPimCmnIpMRouteRPFVectorAddr,'fsPimCmnIpMRoutePimMode':fsPimCmnIpMRoutePimMode,'fsPimCmnIpMRouteNextHopTable':fsPimCmnIpMRouteNextHopTable,'fsPimCmnIpMRouteNextHopEntry':fsPimCmnIpMRouteNextHopEntry,_j:fsPimCmnIpMRouteNextHopCompId,_k:fsPimCmnIpMRouteNextHopAddrType,_l:fsPimCmnIpMRouteNextHopGroup,_m:fsPimCmnIpMRouteNextHopSource,_n:fsPimCmnIpMRouteNextHopSourceMasklen,_o:fsPimCmnIpMRouteNextHopIfIndex,_p:fsPimCmnIpMRouteNextHopAddress,'fsPimCmnIpMRouteNextHopPruneReason':fsPimCmnIpMRouteNextHopPruneReason,'fsPimCmnIpMRouteNextHopState':fsPimCmnIpMRouteNextHopState,'fsPimCmnIpMRouteNextHopUpTime':fsPimCmnIpMRouteNextHopUpTime,'fsPimCmnIpMRouteNextHopExpiryTime':fsPimCmnIpMRouteNextHopExpiryTime,'fsPimCmnIpMRouteNextHopProtocol':fsPimCmnIpMRouteNextHopProtocol,'fsPimCmnIpMRouteNextHopPkts':fsPimCmnIpMRouteNextHopPkts,'fsPimCmnCandidateRPTable':fsPimCmnCandidateRPTable,'fsPimCmnCandidateRPEntry':fsPimCmnCandidateRPEntry,_r:fsPimCmnCandidateRPCompId,_s:fsPimCmnCandidateRPAddrType,_t:fsPimCmnCandidateRPGroupAddress,_u:fsPimCmnCandidateRPGroupMasklen,_v:fsPimCmnCandidateRPAddress,'fsPimCmnCandidateRPPriority':fsPimCmnCandidateRPPriority,'fsPimCmnCandidateRPRowStatus':fsPimCmnCandidateRPRowStatus,'fsPimCmnCandidateRPPimMode':fsPimCmnCandidateRPPimMode,'fsPimCmnStaticRPSetTable':fsPimCmnStaticRPSetTable,'fsPimCmnStaticRPSetEntry':fsPimCmnStaticRPSetEntry,_w:fsPimCmnStaticRPSetCompId,_x:fsPimCmnStaticRPAddrType,_y:fsPimCmnStaticRPSetGroupAddress,_z:fsPimCmnStaticRPSetGroupMasklen,'fsPimCmnStaticRPAddress':fsPimCmnStaticRPAddress,'fsPimCmnStaticRPRowStatus':fsPimCmnStaticRPRowStatus,'fsPimCmnStaticRPEmbdFlag':fsPimCmnStaticRPEmbdFlag,'fsPimCmnStaticRPPimMode':fsPimCmnStaticRPPimMode,'fsPimCmnComponentModeTable':fsPimCmnComponentModeTable,'fsPimCmnComponentModeEntry':fsPimCmnComponentModeEntry,_A0:fsPimCmnComponentId,'fsPimCmnComponentMode':fsPimCmnComponentMode,'fsPimCmnCompGraftRetryCount':fsPimCmnCompGraftRetryCount,'fsPimCmnRegChkSumCfgTable':fsPimCmnRegChkSumCfgTable,'fsPimCmnRegChkSumCfgEntry':fsPimCmnRegChkSumCfgEntry,_A1:fsPimCmnRegChkSumTblCompId,_A2:fsPimCmnRegChkSumTblRPAddrType,_A3:fsPimCmnRegChkSumTblRPAddress,'fsPimCmnRPChkSumStatus':fsPimCmnRPChkSumStatus,'fsPimCmnDFTable':fsPimCmnDFTable,'fsPimCmnDFEntry':fsPimCmnDFEntry,_A4:fsPimCmnDFIfAddrType,_A5:fsPimCmnDFElectedRP,_A6:fsPimCmnDFIfIndex,'fsPimCmnDFState':fsPimCmnDFState,'fsPimCmnDFWinnerAddr':fsPimCmnDFWinnerAddr,'fsPimCmnDFWinnerUptime':fsPimCmnDFWinnerUptime,'fsPimCmnDFElectionStateTimer':fsPimCmnDFElectionStateTimer,'fsPimCmnDFWinnerMetric':fsPimCmnDFWinnerMetric,'fsPimCmnDFWinnerMetricPref':fsPimCmnDFWinnerMetricPref,'fsPimCmnDFMessageCount':fsPimCmnDFMessageCount,'fsPimCmnElectedRPTable':fsPimCmnElectedRPTable,'fsPimCmnElectedRPEntry':fsPimCmnElectedRPEntry,_A7:fsPimCmnElectedRPCompId,_A8:fsPimCmnElectedRPAddrType,_A9:fsPimCmnElectedRPGroupAddress,_AA:fsPimCmnElectedRPGroupMasklen,'fsPimCmnElectedRPAddress':fsPimCmnElectedRPAddress,'fsPimCmnElectedRPPriority':fsPimCmnElectedRPPriority,'fsPimCmnElectedRPHoldTime':fsPimCmnElectedRPHoldTime,'fsPimCmnElectedRPUpTime':fsPimCmnElectedRPUpTime,'fsPimCmnNeighborExtTable':fsPimCmnNeighborExtTable,'fsPimCmnNeighborExtEntry':fsPimCmnNeighborExtEntry,_AB:fsPimCmnNeighborExtIfIndex,_AC:fsPimCmnNeighborExtAddrType,_AD:fsPimCmnNeighborExtAddress,'fsPimCmnNeighborExtCompIdList':fsPimCmnNeighborExtCompIdList,'fsPimCmnNeighborExtUpTime':fsPimCmnNeighborExtUpTime,'fsPimCmnNeighborExtExpiryTime':fsPimCmnNeighborExtExpiryTime,'fsPimCmnNeighborExtGenerationId':fsPimCmnNeighborExtGenerationId,'fsPimCmnNeighborExtLanDelay':fsPimCmnNeighborExtLanDelay,'fsPimCmnNeighborExtDRPriority':fsPimCmnNeighborExtDRPriority,'fsPimCmnNeighborExtOverrideInterval':fsPimCmnNeighborExtOverrideInterval,'fsPimCmnNeighborExtSRCapable':fsPimCmnNeighborExtSRCapable,'fsPimCmnNeighborExtRPFCapable':fsPimCmnNeighborExtRPFCapable,'fsPimCmnNeighborExtBidirCapable':fsPimCmnNeighborExtBidirCapable,'fsPimCmnIpGenMRouteTable':fsPimCmnIpGenMRouteTable,'fsPimCmnIpGenMRouteEntry':fsPimCmnIpGenMRouteEntry,_AE:fsPimCmnIpGenMRouteCompId,_AF:fsPimCmnIpGenMRouteAddrType,_AG:fsPimCmnIpGenMRouteGroup,_AH:fsPimCmnIpGenMRouteGroupMasklen,_AI:fsPimCmnIpGenMRouteSource,_AJ:fsPimCmnIpGenMRouteSourceMasklen,'fsPimCmnIpGenMRouteUpstreamNeighbor':fsPimCmnIpGenMRouteUpstreamNeighbor,'fsPimCmnIpGenMRouteInIfIndex':fsPimCmnIpGenMRouteInIfIndex,'fsPimCmnIpGenMRouteUpTime':fsPimCmnIpGenMRouteUpTime,'fsPimCmnIpGenMRoutePkts':fsPimCmnIpGenMRoutePkts,'fsPimCmnIpGenMRouteUpstreamAssertTimer':fsPimCmnIpGenMRouteUpstreamAssertTimer,'fsPimCmnIpGenMRouteAssertMetric':fsPimCmnIpGenMRouteAssertMetric,'fsPimCmnIpGenMRouteAssertMetricPref':fsPimCmnIpGenMRouteAssertMetricPref,'fsPimCmnIpGenMRouteAssertRPTBit':fsPimCmnIpGenMRouteAssertRPTBit,'fsPimCmnIpGenMRouteTimerFlags':fsPimCmnIpGenMRouteTimerFlags,'fsPimCmnIpGenMRouteFlags':fsPimCmnIpGenMRouteFlags,'fsPimCmnIpGenMRouteUpstreamPruneState':fsPimCmnIpGenMRouteUpstreamPruneState,'fsPimCmnIpGenMRouteUpstreamPruneLimitTimer':fsPimCmnIpGenMRouteUpstreamPruneLimitTimer,'fsPimCmnIpGenMRouteOriginatorState':fsPimCmnIpGenMRouteOriginatorState,'fsPimCmnIpGenMRouteSourceActiveTimer':fsPimCmnIpGenMRouteSourceActiveTimer,'fsPimCmnIpGenMRouteStateRefreshTimer':fsPimCmnIpGenMRouteStateRefreshTimer,'fsPimCmnIpGenMRouteExpiryTime':fsPimCmnIpGenMRouteExpiryTime,'fsPimCmnIpGenMRouteDifferentInIfPackets':fsPimCmnIpGenMRouteDifferentInIfPackets,'fsPimCmnIpGenMRouteOctets':fsPimCmnIpGenMRouteOctets,'fsPimCmnIpGenMRouteProtocol':fsPimCmnIpGenMRouteProtocol,'fsPimCmnIpGenMRouteRtProto':fsPimCmnIpGenMRouteRtProto,'fsPimCmnIpGenMRouteRtAddress':fsPimCmnIpGenMRouteRtAddress,'fsPimCmnIpGenMRouteRtMasklen':fsPimCmnIpGenMRouteRtMasklen,'fsPimCmnIpGenMRouteRtType':fsPimCmnIpGenMRouteRtType,'fsPimCmnIpGenMRouteHCOctets':fsPimCmnIpGenMRouteHCOctets,'fsPimCmnIpGenMRouteOIfList':fsPimCmnIpGenMRouteOIfList,'fsPimCmnIpGenMRouteRPFVectorAddr':fsPimCmnIpGenMRouteRPFVectorAddr,'fsPimCmnIpGenMRoutePimMode':fsPimCmnIpGenMRoutePimMode,'fsPimCmnIpGenMRouteType':fsPimCmnIpGenMRouteType,'fsPimCmnIpGenMRouteNPStatus':fsPimCmnIpGenMRouteNPStatus,'fsPimCmnIpGenMRouteNextHopTable':fsPimCmnIpGenMRouteNextHopTable,'fsPimCmnIpGenMRouteNextHopEntry':fsPimCmnIpGenMRouteNextHopEntry,_AK:fsPimCmnIpGenMRouteNextHopCompId,_AL:fsPimCmnIpGenMRouteNextHopAddrType,_AM:fsPimCmnIpGenMRouteNextHopGroup,_AN:fsPimCmnIpGenMRouteNextHopGroupMasklen,_AO:fsPimCmnIpGenMRouteNextHopSource,_AP:fsPimCmnIpGenMRouteNextHopSourceMasklen,_AQ:fsPimCmnIpGenMRouteNextHopIfIndex,_AR:fsPimCmnIpGenMRouteNextHopAddress,'fsPimCmnIpGenMRouteNextHopPruneReason':fsPimCmnIpGenMRouteNextHopPruneReason,'fsPimCmnIpGenMRouteNextHopState':fsPimCmnIpGenMRouteNextHopState,'fsPimCmnIpGenMRouteNextHopUpTime':fsPimCmnIpGenMRouteNextHopUpTime,'fsPimCmnIpGenMRouteNextHopExpiryTime':fsPimCmnIpGenMRouteNextHopExpiryTime,'fsPimCmnIpGenMRouteNextHopProtocol':fsPimCmnIpGenMRouteNextHopProtocol,'fsPimCmnIpGenMRouteNextHopPkts':fsPimCmnIpGenMRouteNextHopPkts,'fsPimCmnIpGenMRouteNextHopNPStatus':fsPimCmnIpGenMRouteNextHopNPStatus,'futurePimCmnTrapsControl':futurePimCmnTrapsControl,_U:fsPimcmnHARtrId,_AT:fsPimCmnHAEvent,'futurePimCmnTraps':futurePimCmnTraps,'fsPimCmnTraps':fsPimCmnTraps,'fsPimCmnHAEventTrap':fsPimCmnHAEventTrap,'fsPimCmnBidirEventTrap':fsPimCmnBidirEventTrap})