_A8='fsPimCmnNeighborIfIndex'
_A7='fsPimCmnHAEvent'
_A6='accessible-for-notify'
_A5='fsPimCmnNeighborExtAddress'
_A4='fsPimCmnNeighborExtAddrType'
_A3='fsPimCmnNeighborExtIfIndex'
_A2='fsPimCmnElectedRPGroupMasklen'
_A1='fsPimCmnElectedRPGroupAddress'
_A0='fsPimCmnElectedRPAddrType'
_z='fsPimCmnElectedRPCompId'
_y='fsPimCmnDFIfIndex'
_x='fsPimCmnDFElectedRP'
_w='fsPimCmnDFIfAddrType'
_v='fsPimCmnRegChkSumTblRPAddress'
_u='fsPimCmnRegChkSumTblRPAddrType'
_t='fsPimCmnRegChkSumTblCompId'
_s='fsPimCmnComponentId'
_r='fsPimCmnStaticRPSetGroupMasklen'
_q='fsPimCmnStaticRPSetGroupAddress'
_p='fsPimCmnStaticRPAddrType'
_o='fsPimCmnStaticRPSetCompId'
_n='fsPimCmnCandidateRPAddress'
_m='fsPimCmnCandidateRPGroupMasklen'
_l='fsPimCmnCandidateRPGroupAddress'
_k='fsPimCmnCandidateRPAddrType'
_j='fsPimCmnCandidateRPCompId'
_i='fsPimCmnIpMRouteNextHopAddress'
_h='fsPimCmnIpMRouteNextHopIfIndex'
_g='fsPimCmnIpMRouteNextHopSourceMasklen'
_f='fsPimCmnIpMRouteNextHopSource'
_e='fsPimCmnIpMRouteNextHopGroup'
_d='fsPimCmnIpMRouteNextHopAddrType'
_c='fsPimCmnIpMRouteNextHopCompId'
_b='pruned'
_a='fsPimCmnIpMRouteSourceMasklen'
_Z='fsPimCmnIpMRouteSource'
_Y='fsPimCmnIpMRouteGroup'
_X='fsPimCmnIpMRouteAddrType'
_W='fsPimCmnIpMRouteCompId'
_V='fsPimCmnNeighborAddrType'
_U='fsPimCmnNeighborCompId'
_T='fsPimCmnInterfaceAddrType'
_S='fsPimCmnInterfaceIfIndex'
_R='fsPimcmnHARtrId'
_Q='bidir'
_P='forwarding'
_O='fsPimCmnNeighborAddress'
_N='seconds'
_M='read-create'
_L='Unsigned32'
_K='disabled'
_J='enabled'
_I='disable'
_H='enable'
_G='deprecated'
_F='read-write'
_E='not-accessible'
_D='SUPERMICRO-PIMCMN-MIB'
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
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsPimCmnMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,111))
if mibBuilder.loadTexts:fsPimCmnMIB.setRevisions(('2012-09-05 00:00',))
class Status(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
class CompList(TextualConvention,OctetString):status=_A
_FsPimCmnMIBObjects_ObjectIdentity=ObjectIdentity
fsPimCmnMIBObjects=_FsPimCmnMIBObjects_ObjectIdentity((1,3,6,1,4,1,10876,101,1,111,1))
_FuturePimCmnScalars_ObjectIdentity=ObjectIdentity
futurePimCmnScalars=_FuturePimCmnScalars_ObjectIdentity((1,3,6,1,4,1,10876,101,1,111,1,1))
_FsPimCmnVersionString_Type=DisplayString
_FsPimCmnVersionString_Object=MibScalar
fsPimCmnVersionString=_FsPimCmnVersionString_Object((1,3,6,1,4,1,10876,101,1,111,1,1,1),_FsPimCmnVersionString_Type())
fsPimCmnVersionString.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnVersionString.setStatus(_A)
class _FsPimCmnSPTGroupThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimCmnSPTGroupThreshold_Type.__name__=_C
_FsPimCmnSPTGroupThreshold_Object=MibScalar
fsPimCmnSPTGroupThreshold=_FsPimCmnSPTGroupThreshold_Object((1,3,6,1,4,1,10876,101,1,111,1,1,2),_FsPimCmnSPTGroupThreshold_Type())
fsPimCmnSPTGroupThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnSPTGroupThreshold.setStatus(_A)
class _FsPimCmnSPTSourceThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimCmnSPTSourceThreshold_Type.__name__=_C
_FsPimCmnSPTSourceThreshold_Object=MibScalar
fsPimCmnSPTSourceThreshold=_FsPimCmnSPTSourceThreshold_Object((1,3,6,1,4,1,10876,101,1,111,1,1,3),_FsPimCmnSPTSourceThreshold_Type())
fsPimCmnSPTSourceThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnSPTSourceThreshold.setStatus(_A)
class _FsPimCmnSPTSwitchingPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimCmnSPTSwitchingPeriod_Type.__name__=_C
_FsPimCmnSPTSwitchingPeriod_Object=MibScalar
fsPimCmnSPTSwitchingPeriod=_FsPimCmnSPTSwitchingPeriod_Object((1,3,6,1,4,1,10876,101,1,111,1,1,4),_FsPimCmnSPTSwitchingPeriod_Type())
fsPimCmnSPTSwitchingPeriod.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnSPTSwitchingPeriod.setStatus(_A)
class _FsPimCmnSPTRpThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimCmnSPTRpThreshold_Type.__name__=_C
_FsPimCmnSPTRpThreshold_Object=MibScalar
fsPimCmnSPTRpThreshold=_FsPimCmnSPTRpThreshold_Object((1,3,6,1,4,1,10876,101,1,111,1,1,5),_FsPimCmnSPTRpThreshold_Type())
fsPimCmnSPTRpThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnSPTRpThreshold.setStatus(_A)
class _FsPimCmnSPTRpSwitchingPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimCmnSPTRpSwitchingPeriod_Type.__name__=_C
_FsPimCmnSPTRpSwitchingPeriod_Object=MibScalar
fsPimCmnSPTRpSwitchingPeriod=_FsPimCmnSPTRpSwitchingPeriod_Object((1,3,6,1,4,1,10876,101,1,111,1,1,6),_FsPimCmnSPTRpSwitchingPeriod_Type())
fsPimCmnSPTRpSwitchingPeriod.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnSPTRpSwitchingPeriod.setStatus(_A)
class _FsPimCmnRegStopRateLimitingPeriod_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimCmnRegStopRateLimitingPeriod_Type.__name__=_C
_FsPimCmnRegStopRateLimitingPeriod_Object=MibScalar
fsPimCmnRegStopRateLimitingPeriod=_FsPimCmnRegStopRateLimitingPeriod_Object((1,3,6,1,4,1,10876,101,1,111,1,1,7),_FsPimCmnRegStopRateLimitingPeriod_Type())
fsPimCmnRegStopRateLimitingPeriod.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnRegStopRateLimitingPeriod.setStatus(_A)
_FsPimCmnMemoryAllocFailCount_Type=Integer32
_FsPimCmnMemoryAllocFailCount_Object=MibScalar
fsPimCmnMemoryAllocFailCount=_FsPimCmnMemoryAllocFailCount_Object((1,3,6,1,4,1,10876,101,1,111,1,1,8),_FsPimCmnMemoryAllocFailCount_Type())
fsPimCmnMemoryAllocFailCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnMemoryAllocFailCount.setStatus(_A)
class _FsPimCmnGlobalTrace_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimCmnGlobalTrace_Type.__name__=_C
_FsPimCmnGlobalTrace_Object=MibScalar
fsPimCmnGlobalTrace=_FsPimCmnGlobalTrace_Object((1,3,6,1,4,1,10876,101,1,111,1,1,9),_FsPimCmnGlobalTrace_Type())
fsPimCmnGlobalTrace.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnGlobalTrace.setStatus(_A)
class _FsPimCmnGlobalDebug_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimCmnGlobalDebug_Type.__name__=_C
_FsPimCmnGlobalDebug_Object=MibScalar
fsPimCmnGlobalDebug=_FsPimCmnGlobalDebug_Object((1,3,6,1,4,1,10876,101,1,111,1,1,10),_FsPimCmnGlobalDebug_Type())
fsPimCmnGlobalDebug.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnGlobalDebug.setStatus(_A)
class _FsPimCmnPmbrStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_FsPimCmnPmbrStatus_Type.__name__=_C
_FsPimCmnPmbrStatus_Object=MibScalar
fsPimCmnPmbrStatus=_FsPimCmnPmbrStatus_Object((1,3,6,1,4,1,10876,101,1,111,1,1,11),_FsPimCmnPmbrStatus_Type())
fsPimCmnPmbrStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnPmbrStatus.setStatus(_A)
class _FsPimCmnRouterMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ssmonly',1),('smssm',2)))
_FsPimCmnRouterMode_Type.__name__=_C
_FsPimCmnRouterMode_Object=MibScalar
fsPimCmnRouterMode=_FsPimCmnRouterMode_Object((1,3,6,1,4,1,10876,101,1,111,1,1,12),_FsPimCmnRouterMode_Type())
fsPimCmnRouterMode.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnRouterMode.setStatus(_A)
class _FsPimCmnStaticRpEnabled_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_H,1)))
_FsPimCmnStaticRpEnabled_Type.__name__=_C
_FsPimCmnStaticRpEnabled_Object=MibScalar
fsPimCmnStaticRpEnabled=_FsPimCmnStaticRpEnabled_Object((1,3,6,1,4,1,10876,101,1,111,1,1,13),_FsPimCmnStaticRpEnabled_Type())
fsPimCmnStaticRpEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnStaticRpEnabled.setStatus(_A)
class _FsPimCmnIpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsPimCmnIpStatus_Type.__name__=_C
_FsPimCmnIpStatus_Object=MibScalar
fsPimCmnIpStatus=_FsPimCmnIpStatus_Object((1,3,6,1,4,1,10876,101,1,111,1,1,14),_FsPimCmnIpStatus_Type())
fsPimCmnIpStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnIpStatus.setStatus(_A)
class _FsPimCmnIpv6Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsPimCmnIpv6Status_Type.__name__=_C
_FsPimCmnIpv6Status_Object=MibScalar
fsPimCmnIpv6Status=_FsPimCmnIpv6Status_Object((1,3,6,1,4,1,10876,101,1,111,1,1,15),_FsPimCmnIpv6Status_Type())
fsPimCmnIpv6Status.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnIpv6Status.setStatus(_A)
class _FsPimCmnSRProcessingStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_H,1)))
_FsPimCmnSRProcessingStatus_Type.__name__=_C
_FsPimCmnSRProcessingStatus_Object=MibScalar
fsPimCmnSRProcessingStatus=_FsPimCmnSRProcessingStatus_Object((1,3,6,1,4,1,10876,101,1,111,1,1,16),_FsPimCmnSRProcessingStatus_Type())
fsPimCmnSRProcessingStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnSRProcessingStatus.setStatus(_A)
class _FsPimCmnRefreshInterval_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(4,100))
_FsPimCmnRefreshInterval_Type.__name__=_C
_FsPimCmnRefreshInterval_Object=MibScalar
fsPimCmnRefreshInterval=_FsPimCmnRefreshInterval_Object((1,3,6,1,4,1,10876,101,1,111,1,1,17),_FsPimCmnRefreshInterval_Type())
fsPimCmnRefreshInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnRefreshInterval.setStatus(_A)
if mibBuilder.loadTexts:fsPimCmnRefreshInterval.setUnits(_N)
class _FsPimCmnSourceActiveInterval_Type(Unsigned32):defaultValue=210;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(120,210))
_FsPimCmnSourceActiveInterval_Type.__name__=_L
_FsPimCmnSourceActiveInterval_Object=MibScalar
fsPimCmnSourceActiveInterval=_FsPimCmnSourceActiveInterval_Object((1,3,6,1,4,1,10876,101,1,111,1,1,18),_FsPimCmnSourceActiveInterval_Type())
fsPimCmnSourceActiveInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnSourceActiveInterval.setStatus(_A)
if mibBuilder.loadTexts:fsPimCmnSourceActiveInterval.setUnits(_N)
class _FsPimCmnHAAdminStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_J,1)))
_FsPimCmnHAAdminStatus_Type.__name__=_C
_FsPimCmnHAAdminStatus_Object=MibScalar
fsPimCmnHAAdminStatus=_FsPimCmnHAAdminStatus_Object((1,3,6,1,4,1,10876,101,1,111,1,1,19),_FsPimCmnHAAdminStatus_Type())
fsPimCmnHAAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnHAAdminStatus.setStatus(_A)
class _FsPimCmnHAState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),('activeStandbyUp',2),('activeStandbyDown',3),('standby',4)))
_FsPimCmnHAState_Type.__name__=_C
_FsPimCmnHAState_Object=MibScalar
fsPimCmnHAState=_FsPimCmnHAState_Object((1,3,6,1,4,1,10876,101,1,111,1,1,20),_FsPimCmnHAState_Type())
fsPimCmnHAState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnHAState.setStatus(_A)
class _FsPimCmnHADynamicBulkUpdStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notStarted',1),('inProgress',2),('completed',3),('aborted',4)))
_FsPimCmnHADynamicBulkUpdStatus_Type.__name__=_C
_FsPimCmnHADynamicBulkUpdStatus_Object=MibScalar
fsPimCmnHADynamicBulkUpdStatus=_FsPimCmnHADynamicBulkUpdStatus_Object((1,3,6,1,4,1,10876,101,1,111,1,1,21),_FsPimCmnHADynamicBulkUpdStatus_Type())
fsPimCmnHADynamicBulkUpdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnHADynamicBulkUpdStatus.setStatus(_A)
class _FsPimCmnHAForwardingTblEntryCnt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimCmnHAForwardingTblEntryCnt_Type.__name__=_C
_FsPimCmnHAForwardingTblEntryCnt_Object=MibScalar
fsPimCmnHAForwardingTblEntryCnt=_FsPimCmnHAForwardingTblEntryCnt_Object((1,3,6,1,4,1,10876,101,1,111,1,1,22),_FsPimCmnHAForwardingTblEntryCnt_Type())
fsPimCmnHAForwardingTblEntryCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnHAForwardingTblEntryCnt.setStatus(_A)
class _FsPimCmnIpRpfVector_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsPimCmnIpRpfVector_Type.__name__=_C
_FsPimCmnIpRpfVector_Object=MibScalar
fsPimCmnIpRpfVector=_FsPimCmnIpRpfVector_Object((1,3,6,1,4,1,10876,101,1,111,1,1,23),_FsPimCmnIpRpfVector_Type())
fsPimCmnIpRpfVector.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnIpRpfVector.setStatus(_A)
class _FsPimCmnIpBidirPIMStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsPimCmnIpBidirPIMStatus_Type.__name__=_C
_FsPimCmnIpBidirPIMStatus_Object=MibScalar
fsPimCmnIpBidirPIMStatus=_FsPimCmnIpBidirPIMStatus_Object((1,3,6,1,4,1,10876,101,1,111,1,1,24),_FsPimCmnIpBidirPIMStatus_Type())
fsPimCmnIpBidirPIMStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnIpBidirPIMStatus.setStatus(_A)
class _FsPimCmnIpBidirOfferInterval_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20000000))
_FsPimCmnIpBidirOfferInterval_Type.__name__=_C
_FsPimCmnIpBidirOfferInterval_Object=MibScalar
fsPimCmnIpBidirOfferInterval=_FsPimCmnIpBidirOfferInterval_Object((1,3,6,1,4,1,10876,101,1,111,1,1,25),_FsPimCmnIpBidirOfferInterval_Type())
fsPimCmnIpBidirOfferInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnIpBidirOfferInterval.setStatus(_A)
if mibBuilder.loadTexts:fsPimCmnIpBidirOfferInterval.setUnits('milliseconds')
class _FsPimCmnIpBidirOfferLimit_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,100))
_FsPimCmnIpBidirOfferLimit_Type.__name__=_C
_FsPimCmnIpBidirOfferLimit_Object=MibScalar
fsPimCmnIpBidirOfferLimit=_FsPimCmnIpBidirOfferLimit_Object((1,3,6,1,4,1,10876,101,1,111,1,1,26),_FsPimCmnIpBidirOfferLimit_Type())
fsPimCmnIpBidirOfferLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnIpBidirOfferLimit.setStatus(_A)
_FuturePimCmnTables_ObjectIdentity=ObjectIdentity
futurePimCmnTables=_FuturePimCmnTables_ObjectIdentity((1,3,6,1,4,1,10876,101,1,111,1,2))
_FsPimCmnInterfaceTable_Object=MibTable
fsPimCmnInterfaceTable=_FsPimCmnInterfaceTable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1))
if mibBuilder.loadTexts:fsPimCmnInterfaceTable.setStatus(_A)
_FsPimCmnInterfaceEntry_Object=MibTableRow
fsPimCmnInterfaceEntry=_FsPimCmnInterfaceEntry_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1))
fsPimCmnInterfaceEntry.setIndexNames((0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:fsPimCmnInterfaceEntry.setStatus(_A)
class _FsPimCmnInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimCmnInterfaceIfIndex_Type.__name__=_C
_FsPimCmnInterfaceIfIndex_Object=MibTableColumn
fsPimCmnInterfaceIfIndex=_FsPimCmnInterfaceIfIndex_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,1),_FsPimCmnInterfaceIfIndex_Type())
fsPimCmnInterfaceIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnInterfaceIfIndex.setStatus(_A)
_FsPimCmnInterfaceAddrType_Type=InetAddressType
_FsPimCmnInterfaceAddrType_Object=MibTableColumn
fsPimCmnInterfaceAddrType=_FsPimCmnInterfaceAddrType_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,2),_FsPimCmnInterfaceAddrType_Type())
fsPimCmnInterfaceAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnInterfaceAddrType.setStatus(_A)
class _FsPimCmnInterfaceCompId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnInterfaceCompId_Type.__name__=_C
_FsPimCmnInterfaceCompId_Object=MibTableColumn
fsPimCmnInterfaceCompId=_FsPimCmnInterfaceCompId_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,3),_FsPimCmnInterfaceCompId_Type())
fsPimCmnInterfaceCompId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceCompId.setStatus(_A)
class _FsPimCmnInterfaceDRPriority_Type(Unsigned32):defaultValue=1
_FsPimCmnInterfaceDRPriority_Type.__name__=_L
_FsPimCmnInterfaceDRPriority_Object=MibTableColumn
fsPimCmnInterfaceDRPriority=_FsPimCmnInterfaceDRPriority_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,4),_FsPimCmnInterfaceDRPriority_Type())
fsPimCmnInterfaceDRPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceDRPriority.setStatus(_A)
class _FsPimCmnInterfaceHelloHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimCmnInterfaceHelloHoldTime_Type.__name__=_C
_FsPimCmnInterfaceHelloHoldTime_Object=MibTableColumn
fsPimCmnInterfaceHelloHoldTime=_FsPimCmnInterfaceHelloHoldTime_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,5),_FsPimCmnInterfaceHelloHoldTime_Type())
fsPimCmnInterfaceHelloHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceHelloHoldTime.setStatus(_A)
class _FsPimCmnInterfaceLanPruneDelayPresent_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_H,1)))
_FsPimCmnInterfaceLanPruneDelayPresent_Type.__name__=_C
_FsPimCmnInterfaceLanPruneDelayPresent_Object=MibTableColumn
fsPimCmnInterfaceLanPruneDelayPresent=_FsPimCmnInterfaceLanPruneDelayPresent_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,6),_FsPimCmnInterfaceLanPruneDelayPresent_Type())
fsPimCmnInterfaceLanPruneDelayPresent.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceLanPruneDelayPresent.setStatus(_A)
class _FsPimCmnInterfaceLanDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimCmnInterfaceLanDelay_Type.__name__=_C
_FsPimCmnInterfaceLanDelay_Object=MibTableColumn
fsPimCmnInterfaceLanDelay=_FsPimCmnInterfaceLanDelay_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,7),_FsPimCmnInterfaceLanDelay_Type())
fsPimCmnInterfaceLanDelay.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceLanDelay.setStatus(_A)
class _FsPimCmnInterfaceOverrideInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimCmnInterfaceOverrideInterval_Type.__name__=_C
_FsPimCmnInterfaceOverrideInterval_Object=MibTableColumn
fsPimCmnInterfaceOverrideInterval=_FsPimCmnInterfaceOverrideInterval_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,8),_FsPimCmnInterfaceOverrideInterval_Type())
fsPimCmnInterfaceOverrideInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceOverrideInterval.setStatus(_A)
_FsPimCmnInterfaceGenerationId_Type=Integer32
_FsPimCmnInterfaceGenerationId_Object=MibTableColumn
fsPimCmnInterfaceGenerationId=_FsPimCmnInterfaceGenerationId_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,9),_FsPimCmnInterfaceGenerationId_Type())
fsPimCmnInterfaceGenerationId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceGenerationId.setStatus(_A)
_FsPimCmnInterfaceSuppressionInterval_Type=Integer32
_FsPimCmnInterfaceSuppressionInterval_Object=MibTableColumn
fsPimCmnInterfaceSuppressionInterval=_FsPimCmnInterfaceSuppressionInterval_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,10),_FsPimCmnInterfaceSuppressionInterval_Type())
fsPimCmnInterfaceSuppressionInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceSuppressionInterval.setStatus(_A)
_FsPimCmnInterfaceAdminStatus_Type=Integer32
_FsPimCmnInterfaceAdminStatus_Object=MibTableColumn
fsPimCmnInterfaceAdminStatus=_FsPimCmnInterfaceAdminStatus_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,11),_FsPimCmnInterfaceAdminStatus_Type())
fsPimCmnInterfaceAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceAdminStatus.setStatus(_A)
_FsPimCmnInterfaceBorderBit_Type=Integer32
_FsPimCmnInterfaceBorderBit_Object=MibTableColumn
fsPimCmnInterfaceBorderBit=_FsPimCmnInterfaceBorderBit_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,12),_FsPimCmnInterfaceBorderBit_Type())
fsPimCmnInterfaceBorderBit.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceBorderBit.setStatus(_A)
class _FsPimCmnInterfaceGraftRetryInterval_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsPimCmnInterfaceGraftRetryInterval_Type.__name__=_L
_FsPimCmnInterfaceGraftRetryInterval_Object=MibTableColumn
fsPimCmnInterfaceGraftRetryInterval=_FsPimCmnInterfaceGraftRetryInterval_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,13),_FsPimCmnInterfaceGraftRetryInterval_Type())
fsPimCmnInterfaceGraftRetryInterval.setMaxAccess(_M)
if mibBuilder.loadTexts:fsPimCmnInterfaceGraftRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:fsPimCmnInterfaceGraftRetryInterval.setUnits(_N)
_FsPimCmnInterfaceSRPriorityEnabled_Type=TruthValue
_FsPimCmnInterfaceSRPriorityEnabled_Object=MibTableColumn
fsPimCmnInterfaceSRPriorityEnabled=_FsPimCmnInterfaceSRPriorityEnabled_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,14),_FsPimCmnInterfaceSRPriorityEnabled_Type())
fsPimCmnInterfaceSRPriorityEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceSRPriorityEnabled.setStatus(_A)
class _FsPimCmnInterfaceTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPimCmnInterfaceTtl_Type.__name__=_C
_FsPimCmnInterfaceTtl_Object=MibTableColumn
fsPimCmnInterfaceTtl=_FsPimCmnInterfaceTtl_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,15),_FsPimCmnInterfaceTtl_Type())
fsPimCmnInterfaceTtl.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceTtl.setStatus(_A)
_FsPimCmnInterfaceProtocol_Type=IANAipMRouteProtocol
_FsPimCmnInterfaceProtocol_Object=MibTableColumn
fsPimCmnInterfaceProtocol=_FsPimCmnInterfaceProtocol_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,16),_FsPimCmnInterfaceProtocol_Type())
fsPimCmnInterfaceProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceProtocol.setStatus(_A)
class _FsPimCmnInterfaceRateLimit_Type(Integer32):defaultValue=0
_FsPimCmnInterfaceRateLimit_Type.__name__=_C
_FsPimCmnInterfaceRateLimit_Object=MibTableColumn
fsPimCmnInterfaceRateLimit=_FsPimCmnInterfaceRateLimit_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,17),_FsPimCmnInterfaceRateLimit_Type())
fsPimCmnInterfaceRateLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceRateLimit.setStatus(_A)
_FsPimCmnInterfaceInMcastOctets_Type=Counter32
_FsPimCmnInterfaceInMcastOctets_Object=MibTableColumn
fsPimCmnInterfaceInMcastOctets=_FsPimCmnInterfaceInMcastOctets_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,18),_FsPimCmnInterfaceInMcastOctets_Type())
fsPimCmnInterfaceInMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceInMcastOctets.setStatus(_A)
_FsPimCmnInterfaceOutMcastOctets_Type=Counter32
_FsPimCmnInterfaceOutMcastOctets_Object=MibTableColumn
fsPimCmnInterfaceOutMcastOctets=_FsPimCmnInterfaceOutMcastOctets_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,19),_FsPimCmnInterfaceOutMcastOctets_Type())
fsPimCmnInterfaceOutMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceOutMcastOctets.setStatus(_A)
_FsPimCmnInterfaceHCInMcastOctets_Type=Counter64
_FsPimCmnInterfaceHCInMcastOctets_Object=MibTableColumn
fsPimCmnInterfaceHCInMcastOctets=_FsPimCmnInterfaceHCInMcastOctets_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,20),_FsPimCmnInterfaceHCInMcastOctets_Type())
fsPimCmnInterfaceHCInMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceHCInMcastOctets.setStatus(_A)
_FsPimCmnInterfaceHCOutMcastOctets_Type=Counter64
_FsPimCmnInterfaceHCOutMcastOctets_Object=MibTableColumn
fsPimCmnInterfaceHCOutMcastOctets=_FsPimCmnInterfaceHCOutMcastOctets_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,21),_FsPimCmnInterfaceHCOutMcastOctets_Type())
fsPimCmnInterfaceHCOutMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnInterfaceHCOutMcastOctets.setStatus(_A)
_FsPimCmnInterfaceCompIdList_Type=CompList
_FsPimCmnInterfaceCompIdList_Object=MibTableColumn
fsPimCmnInterfaceCompIdList=_FsPimCmnInterfaceCompIdList_Object((1,3,6,1,4,1,10876,101,1,111,1,2,1,1,22),_FsPimCmnInterfaceCompIdList_Type())
fsPimCmnInterfaceCompIdList.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnInterfaceCompIdList.setStatus(_A)
_FsPimCmnNeighborTable_Object=MibTable
fsPimCmnNeighborTable=_FsPimCmnNeighborTable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,2))
if mibBuilder.loadTexts:fsPimCmnNeighborTable.setStatus(_G)
_FsPimCmnNeighborEntry_Object=MibTableRow
fsPimCmnNeighborEntry=_FsPimCmnNeighborEntry_Object((1,3,6,1,4,1,10876,101,1,111,1,2,2,1))
fsPimCmnNeighborEntry.setIndexNames((0,_D,_U),(0,_D,_V),(0,_D,_O))
if mibBuilder.loadTexts:fsPimCmnNeighborEntry.setStatus(_G)
class _FsPimCmnNeighborCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnNeighborCompId_Type.__name__=_C
_FsPimCmnNeighborCompId_Object=MibTableColumn
fsPimCmnNeighborCompId=_FsPimCmnNeighborCompId_Object((1,3,6,1,4,1,10876,101,1,111,1,2,2,1,1),_FsPimCmnNeighborCompId_Type())
fsPimCmnNeighborCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnNeighborCompId.setStatus(_G)
_FsPimCmnNeighborAddrType_Type=InetAddressType
_FsPimCmnNeighborAddrType_Object=MibTableColumn
fsPimCmnNeighborAddrType=_FsPimCmnNeighborAddrType_Object((1,3,6,1,4,1,10876,101,1,111,1,2,2,1,2),_FsPimCmnNeighborAddrType_Type())
fsPimCmnNeighborAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnNeighborAddrType.setStatus(_G)
_FsPimCmnNeighborAddress_Type=InetAddress
_FsPimCmnNeighborAddress_Object=MibTableColumn
fsPimCmnNeighborAddress=_FsPimCmnNeighborAddress_Object((1,3,6,1,4,1,10876,101,1,111,1,2,2,1,3),_FsPimCmnNeighborAddress_Type())
fsPimCmnNeighborAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnNeighborAddress.setStatus(_G)
_FsPimCmnNeighborIfIndex_Type=Integer32
_FsPimCmnNeighborIfIndex_Object=MibTableColumn
fsPimCmnNeighborIfIndex=_FsPimCmnNeighborIfIndex_Object((1,3,6,1,4,1,10876,101,1,111,1,2,2,1,4),_FsPimCmnNeighborIfIndex_Type())
fsPimCmnNeighborIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborIfIndex.setStatus(_G)
_FsPimCmnNeighborUpTime_Type=TimeTicks
_FsPimCmnNeighborUpTime_Object=MibTableColumn
fsPimCmnNeighborUpTime=_FsPimCmnNeighborUpTime_Object((1,3,6,1,4,1,10876,101,1,111,1,2,2,1,5),_FsPimCmnNeighborUpTime_Type())
fsPimCmnNeighborUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborUpTime.setStatus(_G)
_FsPimCmnNeighborExpiryTime_Type=TimeTicks
_FsPimCmnNeighborExpiryTime_Object=MibTableColumn
fsPimCmnNeighborExpiryTime=_FsPimCmnNeighborExpiryTime_Object((1,3,6,1,4,1,10876,101,1,111,1,2,2,1,6),_FsPimCmnNeighborExpiryTime_Type())
fsPimCmnNeighborExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExpiryTime.setStatus(_G)
_FsPimCmnNeighborGenerationId_Type=Integer32
_FsPimCmnNeighborGenerationId_Object=MibTableColumn
fsPimCmnNeighborGenerationId=_FsPimCmnNeighborGenerationId_Object((1,3,6,1,4,1,10876,101,1,111,1,2,2,1,7),_FsPimCmnNeighborGenerationId_Type())
fsPimCmnNeighborGenerationId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborGenerationId.setStatus(_G)
_FsPimCmnNeighborLanDelay_Type=Integer32
_FsPimCmnNeighborLanDelay_Object=MibTableColumn
fsPimCmnNeighborLanDelay=_FsPimCmnNeighborLanDelay_Object((1,3,6,1,4,1,10876,101,1,111,1,2,2,1,8),_FsPimCmnNeighborLanDelay_Type())
fsPimCmnNeighborLanDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborLanDelay.setStatus(_G)
_FsPimCmnNeighborDRPriority_Type=Unsigned32
_FsPimCmnNeighborDRPriority_Object=MibTableColumn
fsPimCmnNeighborDRPriority=_FsPimCmnNeighborDRPriority_Object((1,3,6,1,4,1,10876,101,1,111,1,2,2,1,9),_FsPimCmnNeighborDRPriority_Type())
fsPimCmnNeighborDRPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborDRPriority.setStatus(_G)
_FsPimCmnNeighborOverrideInterval_Type=Integer32
_FsPimCmnNeighborOverrideInterval_Object=MibTableColumn
fsPimCmnNeighborOverrideInterval=_FsPimCmnNeighborOverrideInterval_Object((1,3,6,1,4,1,10876,101,1,111,1,2,2,1,10),_FsPimCmnNeighborOverrideInterval_Type())
fsPimCmnNeighborOverrideInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborOverrideInterval.setStatus(_G)
_FsPimCmnNeighborSRCapable_Type=TruthValue
_FsPimCmnNeighborSRCapable_Object=MibTableColumn
fsPimCmnNeighborSRCapable=_FsPimCmnNeighborSRCapable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,2,1,11),_FsPimCmnNeighborSRCapable_Type())
fsPimCmnNeighborSRCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborSRCapable.setStatus(_G)
_FsPimCmnNeighborRPFCapable_Type=TruthValue
_FsPimCmnNeighborRPFCapable_Object=MibTableColumn
fsPimCmnNeighborRPFCapable=_FsPimCmnNeighborRPFCapable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,2,1,12),_FsPimCmnNeighborRPFCapable_Type())
fsPimCmnNeighborRPFCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborRPFCapable.setStatus(_G)
_FsPimCmnNeighborBidirCapable_Type=TruthValue
_FsPimCmnNeighborBidirCapable_Object=MibTableColumn
fsPimCmnNeighborBidirCapable=_FsPimCmnNeighborBidirCapable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,2,1,13),_FsPimCmnNeighborBidirCapable_Type())
fsPimCmnNeighborBidirCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborBidirCapable.setStatus(_G)
_FsPimCmnIpMRouteTable_Object=MibTable
fsPimCmnIpMRouteTable=_FsPimCmnIpMRouteTable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3))
if mibBuilder.loadTexts:fsPimCmnIpMRouteTable.setStatus(_A)
_FsPimCmnIpMRouteEntry_Object=MibTableRow
fsPimCmnIpMRouteEntry=_FsPimCmnIpMRouteEntry_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1))
fsPimCmnIpMRouteEntry.setIndexNames((0,_D,_W),(0,_D,_X),(0,_D,_Y),(0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:fsPimCmnIpMRouteEntry.setStatus(_A)
class _FsPimCmnIpMRouteCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnIpMRouteCompId_Type.__name__=_C
_FsPimCmnIpMRouteCompId_Object=MibTableColumn
fsPimCmnIpMRouteCompId=_FsPimCmnIpMRouteCompId_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,1),_FsPimCmnIpMRouteCompId_Type())
fsPimCmnIpMRouteCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteCompId.setStatus(_A)
_FsPimCmnIpMRouteAddrType_Type=InetAddressType
_FsPimCmnIpMRouteAddrType_Object=MibTableColumn
fsPimCmnIpMRouteAddrType=_FsPimCmnIpMRouteAddrType_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,2),_FsPimCmnIpMRouteAddrType_Type())
fsPimCmnIpMRouteAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteAddrType.setStatus(_A)
_FsPimCmnIpMRouteGroup_Type=InetAddress
_FsPimCmnIpMRouteGroup_Object=MibTableColumn
fsPimCmnIpMRouteGroup=_FsPimCmnIpMRouteGroup_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,3),_FsPimCmnIpMRouteGroup_Type())
fsPimCmnIpMRouteGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteGroup.setStatus(_A)
_FsPimCmnIpMRouteSource_Type=InetAddress
_FsPimCmnIpMRouteSource_Object=MibTableColumn
fsPimCmnIpMRouteSource=_FsPimCmnIpMRouteSource_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,4),_FsPimCmnIpMRouteSource_Type())
fsPimCmnIpMRouteSource.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteSource.setStatus(_A)
class _FsPimCmnIpMRouteSourceMasklen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimCmnIpMRouteSourceMasklen_Type.__name__=_C
_FsPimCmnIpMRouteSourceMasklen_Object=MibTableColumn
fsPimCmnIpMRouteSourceMasklen=_FsPimCmnIpMRouteSourceMasklen_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,5),_FsPimCmnIpMRouteSourceMasklen_Type())
fsPimCmnIpMRouteSourceMasklen.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteSourceMasklen.setStatus(_A)
_FsPimCmnIpMRouteUpstreamNeighbor_Type=InetAddress
_FsPimCmnIpMRouteUpstreamNeighbor_Object=MibTableColumn
fsPimCmnIpMRouteUpstreamNeighbor=_FsPimCmnIpMRouteUpstreamNeighbor_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,6),_FsPimCmnIpMRouteUpstreamNeighbor_Type())
fsPimCmnIpMRouteUpstreamNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteUpstreamNeighbor.setStatus(_A)
_FsPimCmnIpMRouteInIfIndex_Type=Integer32
_FsPimCmnIpMRouteInIfIndex_Object=MibTableColumn
fsPimCmnIpMRouteInIfIndex=_FsPimCmnIpMRouteInIfIndex_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,7),_FsPimCmnIpMRouteInIfIndex_Type())
fsPimCmnIpMRouteInIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteInIfIndex.setStatus(_A)
_FsPimCmnIpMRouteUpTime_Type=TimeTicks
_FsPimCmnIpMRouteUpTime_Object=MibTableColumn
fsPimCmnIpMRouteUpTime=_FsPimCmnIpMRouteUpTime_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,8),_FsPimCmnIpMRouteUpTime_Type())
fsPimCmnIpMRouteUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteUpTime.setStatus(_A)
_FsPimCmnIpMRoutePkts_Type=Counter32
_FsPimCmnIpMRoutePkts_Object=MibTableColumn
fsPimCmnIpMRoutePkts=_FsPimCmnIpMRoutePkts_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,9),_FsPimCmnIpMRoutePkts_Type())
fsPimCmnIpMRoutePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRoutePkts.setStatus(_A)
_FsPimCmnIpMRouteUpstreamAssertTimer_Type=TimeTicks
_FsPimCmnIpMRouteUpstreamAssertTimer_Object=MibTableColumn
fsPimCmnIpMRouteUpstreamAssertTimer=_FsPimCmnIpMRouteUpstreamAssertTimer_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,10),_FsPimCmnIpMRouteUpstreamAssertTimer_Type())
fsPimCmnIpMRouteUpstreamAssertTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteUpstreamAssertTimer.setStatus(_A)
_FsPimCmnIpMRouteAssertMetric_Type=Integer32
_FsPimCmnIpMRouteAssertMetric_Object=MibTableColumn
fsPimCmnIpMRouteAssertMetric=_FsPimCmnIpMRouteAssertMetric_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,11),_FsPimCmnIpMRouteAssertMetric_Type())
fsPimCmnIpMRouteAssertMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteAssertMetric.setStatus(_A)
_FsPimCmnIpMRouteAssertMetricPref_Type=Integer32
_FsPimCmnIpMRouteAssertMetricPref_Object=MibTableColumn
fsPimCmnIpMRouteAssertMetricPref=_FsPimCmnIpMRouteAssertMetricPref_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,12),_FsPimCmnIpMRouteAssertMetricPref_Type())
fsPimCmnIpMRouteAssertMetricPref.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteAssertMetricPref.setStatus(_A)
_FsPimCmnIpMRouteAssertRPTBit_Type=TruthValue
_FsPimCmnIpMRouteAssertRPTBit_Object=MibTableColumn
fsPimCmnIpMRouteAssertRPTBit=_FsPimCmnIpMRouteAssertRPTBit_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,13),_FsPimCmnIpMRouteAssertRPTBit_Type())
fsPimCmnIpMRouteAssertRPTBit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteAssertRPTBit.setStatus(_A)
_FsPimCmnIpMRouteTimerFlags_Type=Integer32
_FsPimCmnIpMRouteTimerFlags_Object=MibTableColumn
fsPimCmnIpMRouteTimerFlags=_FsPimCmnIpMRouteTimerFlags_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,14),_FsPimCmnIpMRouteTimerFlags_Type())
fsPimCmnIpMRouteTimerFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteTimerFlags.setStatus(_A)
_FsPimCmnIpMRouteFlags_Type=Integer32
_FsPimCmnIpMRouteFlags_Object=MibTableColumn
fsPimCmnIpMRouteFlags=_FsPimCmnIpMRouteFlags_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,15),_FsPimCmnIpMRouteFlags_Type())
fsPimCmnIpMRouteFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteFlags.setStatus(_A)
class _FsPimCmnIpMRouteUpstreamPruneState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('ackpending',2),(_b,3)))
_FsPimCmnIpMRouteUpstreamPruneState_Type.__name__=_C
_FsPimCmnIpMRouteUpstreamPruneState_Object=MibTableColumn
fsPimCmnIpMRouteUpstreamPruneState=_FsPimCmnIpMRouteUpstreamPruneState_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,16),_FsPimCmnIpMRouteUpstreamPruneState_Type())
fsPimCmnIpMRouteUpstreamPruneState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteUpstreamPruneState.setStatus(_A)
_FsPimCmnIpMRouteUpstreamPruneLimitTimer_Type=TimeTicks
_FsPimCmnIpMRouteUpstreamPruneLimitTimer_Object=MibTableColumn
fsPimCmnIpMRouteUpstreamPruneLimitTimer=_FsPimCmnIpMRouteUpstreamPruneLimitTimer_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,17),_FsPimCmnIpMRouteUpstreamPruneLimitTimer_Type())
fsPimCmnIpMRouteUpstreamPruneLimitTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteUpstreamPruneLimitTimer.setStatus(_A)
class _FsPimCmnIpMRouteOriginatorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notOriginator',1),('originator',2)))
_FsPimCmnIpMRouteOriginatorState_Type.__name__=_C
_FsPimCmnIpMRouteOriginatorState_Object=MibTableColumn
fsPimCmnIpMRouteOriginatorState=_FsPimCmnIpMRouteOriginatorState_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,18),_FsPimCmnIpMRouteOriginatorState_Type())
fsPimCmnIpMRouteOriginatorState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteOriginatorState.setStatus(_A)
_FsPimCmnIpMRouteSourceActiveTimer_Type=TimeTicks
_FsPimCmnIpMRouteSourceActiveTimer_Object=MibTableColumn
fsPimCmnIpMRouteSourceActiveTimer=_FsPimCmnIpMRouteSourceActiveTimer_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,19),_FsPimCmnIpMRouteSourceActiveTimer_Type())
fsPimCmnIpMRouteSourceActiveTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteSourceActiveTimer.setStatus(_A)
_FsPimCmnIpMRouteStateRefreshTimer_Type=TimeTicks
_FsPimCmnIpMRouteStateRefreshTimer_Object=MibTableColumn
fsPimCmnIpMRouteStateRefreshTimer=_FsPimCmnIpMRouteStateRefreshTimer_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,20),_FsPimCmnIpMRouteStateRefreshTimer_Type())
fsPimCmnIpMRouteStateRefreshTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteStateRefreshTimer.setStatus(_A)
_FsPimCmnIpMRouteExpiryTime_Type=TimeTicks
_FsPimCmnIpMRouteExpiryTime_Object=MibTableColumn
fsPimCmnIpMRouteExpiryTime=_FsPimCmnIpMRouteExpiryTime_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,21),_FsPimCmnIpMRouteExpiryTime_Type())
fsPimCmnIpMRouteExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteExpiryTime.setStatus(_A)
_FsPimCmnIpMRouteDifferentInIfPackets_Type=Counter32
_FsPimCmnIpMRouteDifferentInIfPackets_Object=MibTableColumn
fsPimCmnIpMRouteDifferentInIfPackets=_FsPimCmnIpMRouteDifferentInIfPackets_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,22),_FsPimCmnIpMRouteDifferentInIfPackets_Type())
fsPimCmnIpMRouteDifferentInIfPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteDifferentInIfPackets.setStatus(_A)
_FsPimCmnIpMRouteOctets_Type=Counter32
_FsPimCmnIpMRouteOctets_Object=MibTableColumn
fsPimCmnIpMRouteOctets=_FsPimCmnIpMRouteOctets_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,23),_FsPimCmnIpMRouteOctets_Type())
fsPimCmnIpMRouteOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteOctets.setStatus(_A)
_FsPimCmnIpMRouteProtocol_Type=IANAipMRouteProtocol
_FsPimCmnIpMRouteProtocol_Object=MibTableColumn
fsPimCmnIpMRouteProtocol=_FsPimCmnIpMRouteProtocol_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,24),_FsPimCmnIpMRouteProtocol_Type())
fsPimCmnIpMRouteProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteProtocol.setStatus(_A)
_FsPimCmnIpMRouteRtProto_Type=IANAipRouteProtocol
_FsPimCmnIpMRouteRtProto_Object=MibTableColumn
fsPimCmnIpMRouteRtProto=_FsPimCmnIpMRouteRtProto_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,25),_FsPimCmnIpMRouteRtProto_Type())
fsPimCmnIpMRouteRtProto.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteRtProto.setStatus(_A)
_FsPimCmnIpMRouteRtAddress_Type=InetAddress
_FsPimCmnIpMRouteRtAddress_Object=MibTableColumn
fsPimCmnIpMRouteRtAddress=_FsPimCmnIpMRouteRtAddress_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,26),_FsPimCmnIpMRouteRtAddress_Type())
fsPimCmnIpMRouteRtAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteRtAddress.setStatus(_A)
_FsPimCmnIpMRouteRtMasklen_Type=Integer32
_FsPimCmnIpMRouteRtMasklen_Object=MibTableColumn
fsPimCmnIpMRouteRtMasklen=_FsPimCmnIpMRouteRtMasklen_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,27),_FsPimCmnIpMRouteRtMasklen_Type())
fsPimCmnIpMRouteRtMasklen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteRtMasklen.setStatus(_A)
class _FsPimCmnIpMRouteRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('multicast',2)))
_FsPimCmnIpMRouteRtType_Type.__name__=_C
_FsPimCmnIpMRouteRtType_Object=MibTableColumn
fsPimCmnIpMRouteRtType=_FsPimCmnIpMRouteRtType_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,28),_FsPimCmnIpMRouteRtType_Type())
fsPimCmnIpMRouteRtType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteRtType.setStatus(_A)
_FsPimCmnIpMRouteHCOctets_Type=Counter64
_FsPimCmnIpMRouteHCOctets_Object=MibTableColumn
fsPimCmnIpMRouteHCOctets=_FsPimCmnIpMRouteHCOctets_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,29),_FsPimCmnIpMRouteHCOctets_Type())
fsPimCmnIpMRouteHCOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteHCOctets.setStatus(_A)
_FsPimCmnIpMRouteOIfList_Type=PortList
_FsPimCmnIpMRouteOIfList_Object=MibTableColumn
fsPimCmnIpMRouteOIfList=_FsPimCmnIpMRouteOIfList_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,30),_FsPimCmnIpMRouteOIfList_Type())
fsPimCmnIpMRouteOIfList.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteOIfList.setStatus(_A)
_FsPimCmnIpMRouteRPFVectorAddr_Type=InetAddress
_FsPimCmnIpMRouteRPFVectorAddr_Object=MibTableColumn
fsPimCmnIpMRouteRPFVectorAddr=_FsPimCmnIpMRouteRPFVectorAddr_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,31),_FsPimCmnIpMRouteRPFVectorAddr_Type())
fsPimCmnIpMRouteRPFVectorAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteRPFVectorAddr.setStatus(_A)
class _FsPimCmnIpMRoutePimMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dm',1),('sm',2),('ssm',3),(_Q,4)))
_FsPimCmnIpMRoutePimMode_Type.__name__=_C
_FsPimCmnIpMRoutePimMode_Object=MibTableColumn
fsPimCmnIpMRoutePimMode=_FsPimCmnIpMRoutePimMode_Object((1,3,6,1,4,1,10876,101,1,111,1,2,3,1,32),_FsPimCmnIpMRoutePimMode_Type())
fsPimCmnIpMRoutePimMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRoutePimMode.setStatus(_A)
_FsPimCmnIpMRouteNextHopTable_Object=MibTable
fsPimCmnIpMRouteNextHopTable=_FsPimCmnIpMRouteNextHopTable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,4))
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopTable.setStatus(_A)
_FsPimCmnIpMRouteNextHopEntry_Object=MibTableRow
fsPimCmnIpMRouteNextHopEntry=_FsPimCmnIpMRouteNextHopEntry_Object((1,3,6,1,4,1,10876,101,1,111,1,2,4,1))
fsPimCmnIpMRouteNextHopEntry.setIndexNames((0,_D,_c),(0,_D,_d),(0,_D,_e),(0,_D,_f),(0,_D,_g),(0,_D,_h),(0,_D,_i))
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopEntry.setStatus(_A)
class _FsPimCmnIpMRouteNextHopCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnIpMRouteNextHopCompId_Type.__name__=_C
_FsPimCmnIpMRouteNextHopCompId_Object=MibTableColumn
fsPimCmnIpMRouteNextHopCompId=_FsPimCmnIpMRouteNextHopCompId_Object((1,3,6,1,4,1,10876,101,1,111,1,2,4,1,1),_FsPimCmnIpMRouteNextHopCompId_Type())
fsPimCmnIpMRouteNextHopCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopCompId.setStatus(_A)
_FsPimCmnIpMRouteNextHopAddrType_Type=InetAddressType
_FsPimCmnIpMRouteNextHopAddrType_Object=MibTableColumn
fsPimCmnIpMRouteNextHopAddrType=_FsPimCmnIpMRouteNextHopAddrType_Object((1,3,6,1,4,1,10876,101,1,111,1,2,4,1,2),_FsPimCmnIpMRouteNextHopAddrType_Type())
fsPimCmnIpMRouteNextHopAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopAddrType.setStatus(_A)
_FsPimCmnIpMRouteNextHopGroup_Type=InetAddress
_FsPimCmnIpMRouteNextHopGroup_Object=MibTableColumn
fsPimCmnIpMRouteNextHopGroup=_FsPimCmnIpMRouteNextHopGroup_Object((1,3,6,1,4,1,10876,101,1,111,1,2,4,1,3),_FsPimCmnIpMRouteNextHopGroup_Type())
fsPimCmnIpMRouteNextHopGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopGroup.setStatus(_A)
_FsPimCmnIpMRouteNextHopSource_Type=InetAddress
_FsPimCmnIpMRouteNextHopSource_Object=MibTableColumn
fsPimCmnIpMRouteNextHopSource=_FsPimCmnIpMRouteNextHopSource_Object((1,3,6,1,4,1,10876,101,1,111,1,2,4,1,4),_FsPimCmnIpMRouteNextHopSource_Type())
fsPimCmnIpMRouteNextHopSource.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopSource.setStatus(_A)
class _FsPimCmnIpMRouteNextHopSourceMasklen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimCmnIpMRouteNextHopSourceMasklen_Type.__name__=_C
_FsPimCmnIpMRouteNextHopSourceMasklen_Object=MibTableColumn
fsPimCmnIpMRouteNextHopSourceMasklen=_FsPimCmnIpMRouteNextHopSourceMasklen_Object((1,3,6,1,4,1,10876,101,1,111,1,2,4,1,5),_FsPimCmnIpMRouteNextHopSourceMasklen_Type())
fsPimCmnIpMRouteNextHopSourceMasklen.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopSourceMasklen.setStatus(_A)
class _FsPimCmnIpMRouteNextHopIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimCmnIpMRouteNextHopIfIndex_Type.__name__=_C
_FsPimCmnIpMRouteNextHopIfIndex_Object=MibTableColumn
fsPimCmnIpMRouteNextHopIfIndex=_FsPimCmnIpMRouteNextHopIfIndex_Object((1,3,6,1,4,1,10876,101,1,111,1,2,4,1,6),_FsPimCmnIpMRouteNextHopIfIndex_Type())
fsPimCmnIpMRouteNextHopIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopIfIndex.setStatus(_A)
_FsPimCmnIpMRouteNextHopAddress_Type=InetAddress
_FsPimCmnIpMRouteNextHopAddress_Object=MibTableColumn
fsPimCmnIpMRouteNextHopAddress=_FsPimCmnIpMRouteNextHopAddress_Object((1,3,6,1,4,1,10876,101,1,111,1,2,4,1,7),_FsPimCmnIpMRouteNextHopAddress_Type())
fsPimCmnIpMRouteNextHopAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopAddress.setStatus(_A)
class _FsPimCmnIpMRouteNextHopPruneReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_P,0),('other',1),('prune',2),('assert',3)))
_FsPimCmnIpMRouteNextHopPruneReason_Type.__name__=_C
_FsPimCmnIpMRouteNextHopPruneReason_Object=MibTableColumn
fsPimCmnIpMRouteNextHopPruneReason=_FsPimCmnIpMRouteNextHopPruneReason_Object((1,3,6,1,4,1,10876,101,1,111,1,2,4,1,8),_FsPimCmnIpMRouteNextHopPruneReason_Type())
fsPimCmnIpMRouteNextHopPruneReason.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopPruneReason.setStatus(_A)
class _FsPimCmnIpMRouteNextHopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_P,2)))
_FsPimCmnIpMRouteNextHopState_Type.__name__=_C
_FsPimCmnIpMRouteNextHopState_Object=MibTableColumn
fsPimCmnIpMRouteNextHopState=_FsPimCmnIpMRouteNextHopState_Object((1,3,6,1,4,1,10876,101,1,111,1,2,4,1,9),_FsPimCmnIpMRouteNextHopState_Type())
fsPimCmnIpMRouteNextHopState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopState.setStatus(_A)
_FsPimCmnIpMRouteNextHopUpTime_Type=TimeTicks
_FsPimCmnIpMRouteNextHopUpTime_Object=MibTableColumn
fsPimCmnIpMRouteNextHopUpTime=_FsPimCmnIpMRouteNextHopUpTime_Object((1,3,6,1,4,1,10876,101,1,111,1,2,4,1,10),_FsPimCmnIpMRouteNextHopUpTime_Type())
fsPimCmnIpMRouteNextHopUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopUpTime.setStatus(_A)
_FsPimCmnIpMRouteNextHopExpiryTime_Type=TimeTicks
_FsPimCmnIpMRouteNextHopExpiryTime_Object=MibTableColumn
fsPimCmnIpMRouteNextHopExpiryTime=_FsPimCmnIpMRouteNextHopExpiryTime_Object((1,3,6,1,4,1,10876,101,1,111,1,2,4,1,11),_FsPimCmnIpMRouteNextHopExpiryTime_Type())
fsPimCmnIpMRouteNextHopExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopExpiryTime.setStatus(_A)
_FsPimCmnIpMRouteNextHopProtocol_Type=IANAipMRouteProtocol
_FsPimCmnIpMRouteNextHopProtocol_Object=MibTableColumn
fsPimCmnIpMRouteNextHopProtocol=_FsPimCmnIpMRouteNextHopProtocol_Object((1,3,6,1,4,1,10876,101,1,111,1,2,4,1,12),_FsPimCmnIpMRouteNextHopProtocol_Type())
fsPimCmnIpMRouteNextHopProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopProtocol.setStatus(_A)
_FsPimCmnIpMRouteNextHopPkts_Type=Counter32
_FsPimCmnIpMRouteNextHopPkts_Object=MibTableColumn
fsPimCmnIpMRouteNextHopPkts=_FsPimCmnIpMRouteNextHopPkts_Object((1,3,6,1,4,1,10876,101,1,111,1,2,4,1,13),_FsPimCmnIpMRouteNextHopPkts_Type())
fsPimCmnIpMRouteNextHopPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnIpMRouteNextHopPkts.setStatus(_A)
_FsPimCmnCandidateRPTable_Object=MibTable
fsPimCmnCandidateRPTable=_FsPimCmnCandidateRPTable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,6))
if mibBuilder.loadTexts:fsPimCmnCandidateRPTable.setStatus(_A)
_FsPimCmnCandidateRPEntry_Object=MibTableRow
fsPimCmnCandidateRPEntry=_FsPimCmnCandidateRPEntry_Object((1,3,6,1,4,1,10876,101,1,111,1,2,6,1))
fsPimCmnCandidateRPEntry.setIndexNames((0,_D,_j),(0,_D,_k),(0,_D,_l),(0,_D,_m),(0,_D,_n))
if mibBuilder.loadTexts:fsPimCmnCandidateRPEntry.setStatus(_A)
class _FsPimCmnCandidateRPCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnCandidateRPCompId_Type.__name__=_C
_FsPimCmnCandidateRPCompId_Object=MibTableColumn
fsPimCmnCandidateRPCompId=_FsPimCmnCandidateRPCompId_Object((1,3,6,1,4,1,10876,101,1,111,1,2,6,1,1),_FsPimCmnCandidateRPCompId_Type())
fsPimCmnCandidateRPCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnCandidateRPCompId.setStatus(_A)
_FsPimCmnCandidateRPAddrType_Type=InetAddressType
_FsPimCmnCandidateRPAddrType_Object=MibTableColumn
fsPimCmnCandidateRPAddrType=_FsPimCmnCandidateRPAddrType_Object((1,3,6,1,4,1,10876,101,1,111,1,2,6,1,2),_FsPimCmnCandidateRPAddrType_Type())
fsPimCmnCandidateRPAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnCandidateRPAddrType.setStatus(_A)
_FsPimCmnCandidateRPGroupAddress_Type=InetAddress
_FsPimCmnCandidateRPGroupAddress_Object=MibTableColumn
fsPimCmnCandidateRPGroupAddress=_FsPimCmnCandidateRPGroupAddress_Object((1,3,6,1,4,1,10876,101,1,111,1,2,6,1,3),_FsPimCmnCandidateRPGroupAddress_Type())
fsPimCmnCandidateRPGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnCandidateRPGroupAddress.setStatus(_A)
class _FsPimCmnCandidateRPGroupMasklen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimCmnCandidateRPGroupMasklen_Type.__name__=_C
_FsPimCmnCandidateRPGroupMasklen_Object=MibTableColumn
fsPimCmnCandidateRPGroupMasklen=_FsPimCmnCandidateRPGroupMasklen_Object((1,3,6,1,4,1,10876,101,1,111,1,2,6,1,4),_FsPimCmnCandidateRPGroupMasklen_Type())
fsPimCmnCandidateRPGroupMasklen.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnCandidateRPGroupMasklen.setStatus(_A)
_FsPimCmnCandidateRPAddress_Type=InetAddress
_FsPimCmnCandidateRPAddress_Object=MibTableColumn
fsPimCmnCandidateRPAddress=_FsPimCmnCandidateRPAddress_Object((1,3,6,1,4,1,10876,101,1,111,1,2,6,1,5),_FsPimCmnCandidateRPAddress_Type())
fsPimCmnCandidateRPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnCandidateRPAddress.setStatus(_A)
class _FsPimCmnCandidateRPPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPimCmnCandidateRPPriority_Type.__name__=_C
_FsPimCmnCandidateRPPriority_Object=MibTableColumn
fsPimCmnCandidateRPPriority=_FsPimCmnCandidateRPPriority_Object((1,3,6,1,4,1,10876,101,1,111,1,2,6,1,6),_FsPimCmnCandidateRPPriority_Type())
fsPimCmnCandidateRPPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnCandidateRPPriority.setStatus(_A)
_FsPimCmnCandidateRPRowStatus_Type=RowStatus
_FsPimCmnCandidateRPRowStatus_Object=MibTableColumn
fsPimCmnCandidateRPRowStatus=_FsPimCmnCandidateRPRowStatus_Object((1,3,6,1,4,1,10876,101,1,111,1,2,6,1,7),_FsPimCmnCandidateRPRowStatus_Type())
fsPimCmnCandidateRPRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:fsPimCmnCandidateRPRowStatus.setStatus(_A)
class _FsPimCmnCandidateRPPimMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*(('sm',2),(_Q,4)))
_FsPimCmnCandidateRPPimMode_Type.__name__=_C
_FsPimCmnCandidateRPPimMode_Object=MibTableColumn
fsPimCmnCandidateRPPimMode=_FsPimCmnCandidateRPPimMode_Object((1,3,6,1,4,1,10876,101,1,111,1,2,6,1,8),_FsPimCmnCandidateRPPimMode_Type())
fsPimCmnCandidateRPPimMode.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnCandidateRPPimMode.setStatus(_A)
_FsPimCmnStaticRPSetTable_Object=MibTable
fsPimCmnStaticRPSetTable=_FsPimCmnStaticRPSetTable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,7))
if mibBuilder.loadTexts:fsPimCmnStaticRPSetTable.setStatus(_A)
_FsPimCmnStaticRPSetEntry_Object=MibTableRow
fsPimCmnStaticRPSetEntry=_FsPimCmnStaticRPSetEntry_Object((1,3,6,1,4,1,10876,101,1,111,1,2,7,1))
fsPimCmnStaticRPSetEntry.setIndexNames((0,_D,_o),(0,_D,_p),(0,_D,_q),(0,_D,_r))
if mibBuilder.loadTexts:fsPimCmnStaticRPSetEntry.setStatus(_A)
class _FsPimCmnStaticRPSetCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnStaticRPSetCompId_Type.__name__=_C
_FsPimCmnStaticRPSetCompId_Object=MibTableColumn
fsPimCmnStaticRPSetCompId=_FsPimCmnStaticRPSetCompId_Object((1,3,6,1,4,1,10876,101,1,111,1,2,7,1,1),_FsPimCmnStaticRPSetCompId_Type())
fsPimCmnStaticRPSetCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnStaticRPSetCompId.setStatus(_A)
_FsPimCmnStaticRPAddrType_Type=InetAddressType
_FsPimCmnStaticRPAddrType_Object=MibTableColumn
fsPimCmnStaticRPAddrType=_FsPimCmnStaticRPAddrType_Object((1,3,6,1,4,1,10876,101,1,111,1,2,7,1,2),_FsPimCmnStaticRPAddrType_Type())
fsPimCmnStaticRPAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnStaticRPAddrType.setStatus(_A)
_FsPimCmnStaticRPSetGroupAddress_Type=InetAddress
_FsPimCmnStaticRPSetGroupAddress_Object=MibTableColumn
fsPimCmnStaticRPSetGroupAddress=_FsPimCmnStaticRPSetGroupAddress_Object((1,3,6,1,4,1,10876,101,1,111,1,2,7,1,3),_FsPimCmnStaticRPSetGroupAddress_Type())
fsPimCmnStaticRPSetGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnStaticRPSetGroupAddress.setStatus(_A)
class _FsPimCmnStaticRPSetGroupMasklen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimCmnStaticRPSetGroupMasklen_Type.__name__=_C
_FsPimCmnStaticRPSetGroupMasklen_Object=MibTableColumn
fsPimCmnStaticRPSetGroupMasklen=_FsPimCmnStaticRPSetGroupMasklen_Object((1,3,6,1,4,1,10876,101,1,111,1,2,7,1,4),_FsPimCmnStaticRPSetGroupMasklen_Type())
fsPimCmnStaticRPSetGroupMasklen.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnStaticRPSetGroupMasklen.setStatus(_A)
_FsPimCmnStaticRPAddress_Type=InetAddress
_FsPimCmnStaticRPAddress_Object=MibTableColumn
fsPimCmnStaticRPAddress=_FsPimCmnStaticRPAddress_Object((1,3,6,1,4,1,10876,101,1,111,1,2,7,1,5),_FsPimCmnStaticRPAddress_Type())
fsPimCmnStaticRPAddress.setMaxAccess(_M)
if mibBuilder.loadTexts:fsPimCmnStaticRPAddress.setStatus(_A)
_FsPimCmnStaticRPRowStatus_Type=RowStatus
_FsPimCmnStaticRPRowStatus_Object=MibTableColumn
fsPimCmnStaticRPRowStatus=_FsPimCmnStaticRPRowStatus_Object((1,3,6,1,4,1,10876,101,1,111,1,2,7,1,6),_FsPimCmnStaticRPRowStatus_Type())
fsPimCmnStaticRPRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:fsPimCmnStaticRPRowStatus.setStatus(_A)
class _FsPimCmnStaticRPEmbdFlag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_H,1)))
_FsPimCmnStaticRPEmbdFlag_Type.__name__=_C
_FsPimCmnStaticRPEmbdFlag_Object=MibTableColumn
fsPimCmnStaticRPEmbdFlag=_FsPimCmnStaticRPEmbdFlag_Object((1,3,6,1,4,1,10876,101,1,111,1,2,7,1,7),_FsPimCmnStaticRPEmbdFlag_Type())
fsPimCmnStaticRPEmbdFlag.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnStaticRPEmbdFlag.setStatus(_A)
class _FsPimCmnStaticRPPimMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*(('sm',2),(_Q,4)))
_FsPimCmnStaticRPPimMode_Type.__name__=_C
_FsPimCmnStaticRPPimMode_Object=MibTableColumn
fsPimCmnStaticRPPimMode=_FsPimCmnStaticRPPimMode_Object((1,3,6,1,4,1,10876,101,1,111,1,2,7,1,8),_FsPimCmnStaticRPPimMode_Type())
fsPimCmnStaticRPPimMode.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnStaticRPPimMode.setStatus(_A)
_FsPimCmnComponentModeTable_Object=MibTable
fsPimCmnComponentModeTable=_FsPimCmnComponentModeTable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,8))
if mibBuilder.loadTexts:fsPimCmnComponentModeTable.setStatus(_A)
_FsPimCmnComponentModeEntry_Object=MibTableRow
fsPimCmnComponentModeEntry=_FsPimCmnComponentModeEntry_Object((1,3,6,1,4,1,10876,101,1,111,1,2,8,1))
fsPimCmnComponentModeEntry.setIndexNames((0,_D,_s))
if mibBuilder.loadTexts:fsPimCmnComponentModeEntry.setStatus(_A)
class _FsPimCmnComponentId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnComponentId_Type.__name__=_C
_FsPimCmnComponentId_Object=MibTableColumn
fsPimCmnComponentId=_FsPimCmnComponentId_Object((1,3,6,1,4,1,10876,101,1,111,1,2,8,1,1),_FsPimCmnComponentId_Type())
fsPimCmnComponentId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnComponentId.setStatus(_A)
class _FsPimCmnComponentMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dense',1),('sparse',2)))
_FsPimCmnComponentMode_Type.__name__=_C
_FsPimCmnComponentMode_Object=MibTableColumn
fsPimCmnComponentMode=_FsPimCmnComponentMode_Object((1,3,6,1,4,1,10876,101,1,111,1,2,8,1,2),_FsPimCmnComponentMode_Type())
fsPimCmnComponentMode.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnComponentMode.setStatus(_A)
class _FsPimCmnCompGraftRetryCount_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPimCmnCompGraftRetryCount_Type.__name__=_C
_FsPimCmnCompGraftRetryCount_Object=MibTableColumn
fsPimCmnCompGraftRetryCount=_FsPimCmnCompGraftRetryCount_Object((1,3,6,1,4,1,10876,101,1,111,1,2,8,1,3),_FsPimCmnCompGraftRetryCount_Type())
fsPimCmnCompGraftRetryCount.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnCompGraftRetryCount.setStatus(_A)
_FsPimCmnRegChkSumCfgTable_Object=MibTable
fsPimCmnRegChkSumCfgTable=_FsPimCmnRegChkSumCfgTable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,9))
if mibBuilder.loadTexts:fsPimCmnRegChkSumCfgTable.setStatus(_A)
_FsPimCmnRegChkSumCfgEntry_Object=MibTableRow
fsPimCmnRegChkSumCfgEntry=_FsPimCmnRegChkSumCfgEntry_Object((1,3,6,1,4,1,10876,101,1,111,1,2,9,1))
fsPimCmnRegChkSumCfgEntry.setIndexNames((0,_D,_t),(0,_D,_u),(0,_D,_v))
if mibBuilder.loadTexts:fsPimCmnRegChkSumCfgEntry.setStatus(_A)
class _FsPimCmnRegChkSumTblCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnRegChkSumTblCompId_Type.__name__=_C
_FsPimCmnRegChkSumTblCompId_Object=MibTableColumn
fsPimCmnRegChkSumTblCompId=_FsPimCmnRegChkSumTblCompId_Object((1,3,6,1,4,1,10876,101,1,111,1,2,9,1,1),_FsPimCmnRegChkSumTblCompId_Type())
fsPimCmnRegChkSumTblCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnRegChkSumTblCompId.setStatus(_A)
_FsPimCmnRegChkSumTblRPAddrType_Type=InetAddressType
_FsPimCmnRegChkSumTblRPAddrType_Object=MibTableColumn
fsPimCmnRegChkSumTblRPAddrType=_FsPimCmnRegChkSumTblRPAddrType_Object((1,3,6,1,4,1,10876,101,1,111,1,2,9,1,2),_FsPimCmnRegChkSumTblRPAddrType_Type())
fsPimCmnRegChkSumTblRPAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnRegChkSumTblRPAddrType.setStatus(_A)
_FsPimCmnRegChkSumTblRPAddress_Type=InetAddress
_FsPimCmnRegChkSumTblRPAddress_Object=MibTableColumn
fsPimCmnRegChkSumTblRPAddress=_FsPimCmnRegChkSumTblRPAddress_Object((1,3,6,1,4,1,10876,101,1,111,1,2,9,1,3),_FsPimCmnRegChkSumTblRPAddress_Type())
fsPimCmnRegChkSumTblRPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnRegChkSumTblRPAddress.setStatus(_A)
class _FsPimCmnRPChkSumStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsPimCmnRPChkSumStatus_Type.__name__=_C
_FsPimCmnRPChkSumStatus_Object=MibTableColumn
fsPimCmnRPChkSumStatus=_FsPimCmnRPChkSumStatus_Object((1,3,6,1,4,1,10876,101,1,111,1,2,9,1,4),_FsPimCmnRPChkSumStatus_Type())
fsPimCmnRPChkSumStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCmnRPChkSumStatus.setStatus(_A)
_FsPimCmnDFTable_Object=MibTable
fsPimCmnDFTable=_FsPimCmnDFTable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,10))
if mibBuilder.loadTexts:fsPimCmnDFTable.setStatus(_A)
_FsPimCmnDFEntry_Object=MibTableRow
fsPimCmnDFEntry=_FsPimCmnDFEntry_Object((1,3,6,1,4,1,10876,101,1,111,1,2,10,1))
fsPimCmnDFEntry.setIndexNames((0,_D,_w),(0,_D,_x),(0,_D,_y))
if mibBuilder.loadTexts:fsPimCmnDFEntry.setStatus(_A)
_FsPimCmnDFIfAddrType_Type=InetAddressType
_FsPimCmnDFIfAddrType_Object=MibTableColumn
fsPimCmnDFIfAddrType=_FsPimCmnDFIfAddrType_Object((1,3,6,1,4,1,10876,101,1,111,1,2,10,1,1),_FsPimCmnDFIfAddrType_Type())
fsPimCmnDFIfAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnDFIfAddrType.setStatus(_A)
_FsPimCmnDFElectedRP_Type=InetAddress
_FsPimCmnDFElectedRP_Object=MibTableColumn
fsPimCmnDFElectedRP=_FsPimCmnDFElectedRP_Object((1,3,6,1,4,1,10876,101,1,111,1,2,10,1,2),_FsPimCmnDFElectedRP_Type())
fsPimCmnDFElectedRP.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnDFElectedRP.setStatus(_A)
class _FsPimCmnDFIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimCmnDFIfIndex_Type.__name__=_C
_FsPimCmnDFIfIndex_Object=MibTableColumn
fsPimCmnDFIfIndex=_FsPimCmnDFIfIndex_Object((1,3,6,1,4,1,10876,101,1,111,1,2,10,1,3),_FsPimCmnDFIfIndex_Type())
fsPimCmnDFIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnDFIfIndex.setStatus(_A)
class _FsPimCmnDFState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('offer',1),('winner',2),('backoff',3),('lose',4)))
_FsPimCmnDFState_Type.__name__=_C
_FsPimCmnDFState_Object=MibTableColumn
fsPimCmnDFState=_FsPimCmnDFState_Object((1,3,6,1,4,1,10876,101,1,111,1,2,10,1,4),_FsPimCmnDFState_Type())
fsPimCmnDFState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnDFState.setStatus(_A)
_FsPimCmnDFWinnerAddr_Type=InetAddress
_FsPimCmnDFWinnerAddr_Object=MibTableColumn
fsPimCmnDFWinnerAddr=_FsPimCmnDFWinnerAddr_Object((1,3,6,1,4,1,10876,101,1,111,1,2,10,1,5),_FsPimCmnDFWinnerAddr_Type())
fsPimCmnDFWinnerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnDFWinnerAddr.setStatus(_A)
_FsPimCmnDFWinnerUptime_Type=TimeTicks
_FsPimCmnDFWinnerUptime_Object=MibTableColumn
fsPimCmnDFWinnerUptime=_FsPimCmnDFWinnerUptime_Object((1,3,6,1,4,1,10876,101,1,111,1,2,10,1,6),_FsPimCmnDFWinnerUptime_Type())
fsPimCmnDFWinnerUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnDFWinnerUptime.setStatus(_A)
_FsPimCmnDFElectionStateTimer_Type=TimeTicks
_FsPimCmnDFElectionStateTimer_Object=MibTableColumn
fsPimCmnDFElectionStateTimer=_FsPimCmnDFElectionStateTimer_Object((1,3,6,1,4,1,10876,101,1,111,1,2,10,1,7),_FsPimCmnDFElectionStateTimer_Type())
fsPimCmnDFElectionStateTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnDFElectionStateTimer.setStatus(_A)
_FsPimCmnDFWinnerMetric_Type=Unsigned32
_FsPimCmnDFWinnerMetric_Object=MibTableColumn
fsPimCmnDFWinnerMetric=_FsPimCmnDFWinnerMetric_Object((1,3,6,1,4,1,10876,101,1,111,1,2,10,1,8),_FsPimCmnDFWinnerMetric_Type())
fsPimCmnDFWinnerMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnDFWinnerMetric.setStatus(_A)
_FsPimCmnDFWinnerMetricPref_Type=Unsigned32
_FsPimCmnDFWinnerMetricPref_Object=MibTableColumn
fsPimCmnDFWinnerMetricPref=_FsPimCmnDFWinnerMetricPref_Object((1,3,6,1,4,1,10876,101,1,111,1,2,10,1,9),_FsPimCmnDFWinnerMetricPref_Type())
fsPimCmnDFWinnerMetricPref.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnDFWinnerMetricPref.setStatus(_A)
class _FsPimCmnDFMessageCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimCmnDFMessageCount_Type.__name__=_C
_FsPimCmnDFMessageCount_Object=MibTableColumn
fsPimCmnDFMessageCount=_FsPimCmnDFMessageCount_Object((1,3,6,1,4,1,10876,101,1,111,1,2,10,1,10),_FsPimCmnDFMessageCount_Type())
fsPimCmnDFMessageCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnDFMessageCount.setStatus(_A)
_FsPimCmnElectedRPTable_Object=MibTable
fsPimCmnElectedRPTable=_FsPimCmnElectedRPTable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,11))
if mibBuilder.loadTexts:fsPimCmnElectedRPTable.setStatus(_A)
_FsPimCmnElectedRPEntry_Object=MibTableRow
fsPimCmnElectedRPEntry=_FsPimCmnElectedRPEntry_Object((1,3,6,1,4,1,10876,101,1,111,1,2,11,1))
fsPimCmnElectedRPEntry.setIndexNames((0,_D,_z),(0,_D,_A0),(0,_D,_A1),(0,_D,_A2))
if mibBuilder.loadTexts:fsPimCmnElectedRPEntry.setStatus(_A)
class _FsPimCmnElectedRPCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCmnElectedRPCompId_Type.__name__=_C
_FsPimCmnElectedRPCompId_Object=MibTableColumn
fsPimCmnElectedRPCompId=_FsPimCmnElectedRPCompId_Object((1,3,6,1,4,1,10876,101,1,111,1,2,11,1,1),_FsPimCmnElectedRPCompId_Type())
fsPimCmnElectedRPCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnElectedRPCompId.setStatus(_A)
_FsPimCmnElectedRPAddrType_Type=InetAddressType
_FsPimCmnElectedRPAddrType_Object=MibTableColumn
fsPimCmnElectedRPAddrType=_FsPimCmnElectedRPAddrType_Object((1,3,6,1,4,1,10876,101,1,111,1,2,11,1,2),_FsPimCmnElectedRPAddrType_Type())
fsPimCmnElectedRPAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnElectedRPAddrType.setStatus(_A)
_FsPimCmnElectedRPGroupAddress_Type=InetAddress
_FsPimCmnElectedRPGroupAddress_Object=MibTableColumn
fsPimCmnElectedRPGroupAddress=_FsPimCmnElectedRPGroupAddress_Object((1,3,6,1,4,1,10876,101,1,111,1,2,11,1,3),_FsPimCmnElectedRPGroupAddress_Type())
fsPimCmnElectedRPGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnElectedRPGroupAddress.setStatus(_A)
class _FsPimCmnElectedRPGroupMasklen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimCmnElectedRPGroupMasklen_Type.__name__=_C
_FsPimCmnElectedRPGroupMasklen_Object=MibTableColumn
fsPimCmnElectedRPGroupMasklen=_FsPimCmnElectedRPGroupMasklen_Object((1,3,6,1,4,1,10876,101,1,111,1,2,11,1,4),_FsPimCmnElectedRPGroupMasklen_Type())
fsPimCmnElectedRPGroupMasklen.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnElectedRPGroupMasklen.setStatus(_A)
_FsPimCmnElectedRPAddress_Type=InetAddress
_FsPimCmnElectedRPAddress_Object=MibTableColumn
fsPimCmnElectedRPAddress=_FsPimCmnElectedRPAddress_Object((1,3,6,1,4,1,10876,101,1,111,1,2,11,1,5),_FsPimCmnElectedRPAddress_Type())
fsPimCmnElectedRPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnElectedRPAddress.setStatus(_A)
class _FsPimCmnElectedRPPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPimCmnElectedRPPriority_Type.__name__=_C
_FsPimCmnElectedRPPriority_Object=MibTableColumn
fsPimCmnElectedRPPriority=_FsPimCmnElectedRPPriority_Object((1,3,6,1,4,1,10876,101,1,111,1,2,11,1,6),_FsPimCmnElectedRPPriority_Type())
fsPimCmnElectedRPPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnElectedRPPriority.setStatus(_A)
class _FsPimCmnElectedRPHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimCmnElectedRPHoldTime_Type.__name__=_C
_FsPimCmnElectedRPHoldTime_Object=MibTableColumn
fsPimCmnElectedRPHoldTime=_FsPimCmnElectedRPHoldTime_Object((1,3,6,1,4,1,10876,101,1,111,1,2,11,1,7),_FsPimCmnElectedRPHoldTime_Type())
fsPimCmnElectedRPHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnElectedRPHoldTime.setStatus(_A)
_FsPimCmnNeighborExtTable_Object=MibTable
fsPimCmnNeighborExtTable=_FsPimCmnNeighborExtTable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,12))
if mibBuilder.loadTexts:fsPimCmnNeighborExtTable.setStatus(_A)
_FsPimCmnNeighborExtEntry_Object=MibTableRow
fsPimCmnNeighborExtEntry=_FsPimCmnNeighborExtEntry_Object((1,3,6,1,4,1,10876,101,1,111,1,2,12,1))
fsPimCmnNeighborExtEntry.setIndexNames((0,_D,_A3),(0,_D,_A4),(0,_D,_A5))
if mibBuilder.loadTexts:fsPimCmnNeighborExtEntry.setStatus(_A)
_FsPimCmnNeighborExtIfIndex_Type=Integer32
_FsPimCmnNeighborExtIfIndex_Object=MibTableColumn
fsPimCmnNeighborExtIfIndex=_FsPimCmnNeighborExtIfIndex_Object((1,3,6,1,4,1,10876,101,1,111,1,2,12,1,1),_FsPimCmnNeighborExtIfIndex_Type())
fsPimCmnNeighborExtIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnNeighborExtIfIndex.setStatus(_A)
_FsPimCmnNeighborExtAddrType_Type=InetAddressType
_FsPimCmnNeighborExtAddrType_Object=MibTableColumn
fsPimCmnNeighborExtAddrType=_FsPimCmnNeighborExtAddrType_Object((1,3,6,1,4,1,10876,101,1,111,1,2,12,1,2),_FsPimCmnNeighborExtAddrType_Type())
fsPimCmnNeighborExtAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnNeighborExtAddrType.setStatus(_A)
_FsPimCmnNeighborExtAddress_Type=InetAddress
_FsPimCmnNeighborExtAddress_Object=MibTableColumn
fsPimCmnNeighborExtAddress=_FsPimCmnNeighborExtAddress_Object((1,3,6,1,4,1,10876,101,1,111,1,2,12,1,3),_FsPimCmnNeighborExtAddress_Type())
fsPimCmnNeighborExtAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCmnNeighborExtAddress.setStatus(_A)
_FsPimCmnNeighborExtCompIdList_Type=CompList
_FsPimCmnNeighborExtCompIdList_Object=MibTableColumn
fsPimCmnNeighborExtCompIdList=_FsPimCmnNeighborExtCompIdList_Object((1,3,6,1,4,1,10876,101,1,111,1,2,12,1,4),_FsPimCmnNeighborExtCompIdList_Type())
fsPimCmnNeighborExtCompIdList.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtCompIdList.setStatus(_A)
_FsPimCmnNeighborExtUpTime_Type=TimeTicks
_FsPimCmnNeighborExtUpTime_Object=MibTableColumn
fsPimCmnNeighborExtUpTime=_FsPimCmnNeighborExtUpTime_Object((1,3,6,1,4,1,10876,101,1,111,1,2,12,1,5),_FsPimCmnNeighborExtUpTime_Type())
fsPimCmnNeighborExtUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtUpTime.setStatus(_A)
_FsPimCmnNeighborExtExpiryTime_Type=TimeTicks
_FsPimCmnNeighborExtExpiryTime_Object=MibTableColumn
fsPimCmnNeighborExtExpiryTime=_FsPimCmnNeighborExtExpiryTime_Object((1,3,6,1,4,1,10876,101,1,111,1,2,12,1,6),_FsPimCmnNeighborExtExpiryTime_Type())
fsPimCmnNeighborExtExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtExpiryTime.setStatus(_A)
_FsPimCmnNeighborExtGenerationId_Type=Integer32
_FsPimCmnNeighborExtGenerationId_Object=MibTableColumn
fsPimCmnNeighborExtGenerationId=_FsPimCmnNeighborExtGenerationId_Object((1,3,6,1,4,1,10876,101,1,111,1,2,12,1,7),_FsPimCmnNeighborExtGenerationId_Type())
fsPimCmnNeighborExtGenerationId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtGenerationId.setStatus(_A)
_FsPimCmnNeighborExtLanDelay_Type=Integer32
_FsPimCmnNeighborExtLanDelay_Object=MibTableColumn
fsPimCmnNeighborExtLanDelay=_FsPimCmnNeighborExtLanDelay_Object((1,3,6,1,4,1,10876,101,1,111,1,2,12,1,8),_FsPimCmnNeighborExtLanDelay_Type())
fsPimCmnNeighborExtLanDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtLanDelay.setStatus(_A)
_FsPimCmnNeighborExtDRPriority_Type=Unsigned32
_FsPimCmnNeighborExtDRPriority_Object=MibTableColumn
fsPimCmnNeighborExtDRPriority=_FsPimCmnNeighborExtDRPriority_Object((1,3,6,1,4,1,10876,101,1,111,1,2,12,1,9),_FsPimCmnNeighborExtDRPriority_Type())
fsPimCmnNeighborExtDRPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtDRPriority.setStatus(_A)
_FsPimCmnNeighborExtOverrideInterval_Type=Integer32
_FsPimCmnNeighborExtOverrideInterval_Object=MibTableColumn
fsPimCmnNeighborExtOverrideInterval=_FsPimCmnNeighborExtOverrideInterval_Object((1,3,6,1,4,1,10876,101,1,111,1,2,12,1,10),_FsPimCmnNeighborExtOverrideInterval_Type())
fsPimCmnNeighborExtOverrideInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtOverrideInterval.setStatus(_A)
_FsPimCmnNeighborExtSRCapable_Type=TruthValue
_FsPimCmnNeighborExtSRCapable_Object=MibTableColumn
fsPimCmnNeighborExtSRCapable=_FsPimCmnNeighborExtSRCapable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,12,1,11),_FsPimCmnNeighborExtSRCapable_Type())
fsPimCmnNeighborExtSRCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtSRCapable.setStatus(_A)
_FsPimCmnNeighborExtRPFCapable_Type=TruthValue
_FsPimCmnNeighborExtRPFCapable_Object=MibTableColumn
fsPimCmnNeighborExtRPFCapable=_FsPimCmnNeighborExtRPFCapable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,12,1,12),_FsPimCmnNeighborExtRPFCapable_Type())
fsPimCmnNeighborExtRPFCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtRPFCapable.setStatus(_A)
_FsPimCmnNeighborExtBidirCapable_Type=TruthValue
_FsPimCmnNeighborExtBidirCapable_Object=MibTableColumn
fsPimCmnNeighborExtBidirCapable=_FsPimCmnNeighborExtBidirCapable_Object((1,3,6,1,4,1,10876,101,1,111,1,2,12,1,13),_FsPimCmnNeighborExtBidirCapable_Type())
fsPimCmnNeighborExtBidirCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPimCmnNeighborExtBidirCapable.setStatus(_A)
_FuturePimCmnTrapsControl_ObjectIdentity=ObjectIdentity
futurePimCmnTrapsControl=_FuturePimCmnTrapsControl_ObjectIdentity((1,3,6,1,4,1,10876,101,1,111,1,3))
_FsPimcmnHARtrId_Type=IpAddress
_FsPimcmnHARtrId_Object=MibScalar
fsPimcmnHARtrId=_FsPimcmnHARtrId_Object((1,3,6,1,4,1,10876,101,1,111,1,3,1),_FsPimcmnHARtrId_Type())
fsPimcmnHARtrId.setMaxAccess(_A6)
if mibBuilder.loadTexts:fsPimcmnHARtrId.setStatus(_A)
class _FsPimCmnHAEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('standbyInstanceUP',1),('standbyInstanceDown',2),('instancesSwitchover',3),('dynamicBulkupdateStart',4),('dynamicBulkupdateComplete',5),('dynamicBulkupdateAborted',6)))
_FsPimCmnHAEvent_Type.__name__=_C
_FsPimCmnHAEvent_Object=MibScalar
fsPimCmnHAEvent=_FsPimCmnHAEvent_Object((1,3,6,1,4,1,10876,101,1,111,1,3,3),_FsPimCmnHAEvent_Type())
fsPimCmnHAEvent.setMaxAccess(_A6)
if mibBuilder.loadTexts:fsPimCmnHAEvent.setStatus(_A)
_FuturePimCmnTraps_ObjectIdentity=ObjectIdentity
futurePimCmnTraps=_FuturePimCmnTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,111,1,4))
_FsPimCmnTraps_ObjectIdentity=ObjectIdentity
fsPimCmnTraps=_FsPimCmnTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,111,1,4,0))
fsPimCmnHAEventTrap=NotificationType((1,3,6,1,4,1,10876,101,1,111,1,4,0,1))
fsPimCmnHAEventTrap.setObjects(*((_D,_R),(_D,_A7)))
if mibBuilder.loadTexts:fsPimCmnHAEventTrap.setStatus(_A)
fsPimCmnBidirEventTrap=NotificationType((1,3,6,1,4,1,10876,101,1,111,1,4,0,2))
fsPimCmnBidirEventTrap.setObjects(*((_D,_R),(_D,_O),(_D,_A8)))
if mibBuilder.loadTexts:fsPimCmnBidirEventTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'Status':Status,'CompList':CompList,'fsPimCmnMIB':fsPimCmnMIB,'fsPimCmnMIBObjects':fsPimCmnMIBObjects,'futurePimCmnScalars':futurePimCmnScalars,'fsPimCmnVersionString':fsPimCmnVersionString,'fsPimCmnSPTGroupThreshold':fsPimCmnSPTGroupThreshold,'fsPimCmnSPTSourceThreshold':fsPimCmnSPTSourceThreshold,'fsPimCmnSPTSwitchingPeriod':fsPimCmnSPTSwitchingPeriod,'fsPimCmnSPTRpThreshold':fsPimCmnSPTRpThreshold,'fsPimCmnSPTRpSwitchingPeriod':fsPimCmnSPTRpSwitchingPeriod,'fsPimCmnRegStopRateLimitingPeriod':fsPimCmnRegStopRateLimitingPeriod,'fsPimCmnMemoryAllocFailCount':fsPimCmnMemoryAllocFailCount,'fsPimCmnGlobalTrace':fsPimCmnGlobalTrace,'fsPimCmnGlobalDebug':fsPimCmnGlobalDebug,'fsPimCmnPmbrStatus':fsPimCmnPmbrStatus,'fsPimCmnRouterMode':fsPimCmnRouterMode,'fsPimCmnStaticRpEnabled':fsPimCmnStaticRpEnabled,'fsPimCmnIpStatus':fsPimCmnIpStatus,'fsPimCmnIpv6Status':fsPimCmnIpv6Status,'fsPimCmnSRProcessingStatus':fsPimCmnSRProcessingStatus,'fsPimCmnRefreshInterval':fsPimCmnRefreshInterval,'fsPimCmnSourceActiveInterval':fsPimCmnSourceActiveInterval,'fsPimCmnHAAdminStatus':fsPimCmnHAAdminStatus,'fsPimCmnHAState':fsPimCmnHAState,'fsPimCmnHADynamicBulkUpdStatus':fsPimCmnHADynamicBulkUpdStatus,'fsPimCmnHAForwardingTblEntryCnt':fsPimCmnHAForwardingTblEntryCnt,'fsPimCmnIpRpfVector':fsPimCmnIpRpfVector,'fsPimCmnIpBidirPIMStatus':fsPimCmnIpBidirPIMStatus,'fsPimCmnIpBidirOfferInterval':fsPimCmnIpBidirOfferInterval,'fsPimCmnIpBidirOfferLimit':fsPimCmnIpBidirOfferLimit,'futurePimCmnTables':futurePimCmnTables,'fsPimCmnInterfaceTable':fsPimCmnInterfaceTable,'fsPimCmnInterfaceEntry':fsPimCmnInterfaceEntry,_S:fsPimCmnInterfaceIfIndex,_T:fsPimCmnInterfaceAddrType,'fsPimCmnInterfaceCompId':fsPimCmnInterfaceCompId,'fsPimCmnInterfaceDRPriority':fsPimCmnInterfaceDRPriority,'fsPimCmnInterfaceHelloHoldTime':fsPimCmnInterfaceHelloHoldTime,'fsPimCmnInterfaceLanPruneDelayPresent':fsPimCmnInterfaceLanPruneDelayPresent,'fsPimCmnInterfaceLanDelay':fsPimCmnInterfaceLanDelay,'fsPimCmnInterfaceOverrideInterval':fsPimCmnInterfaceOverrideInterval,'fsPimCmnInterfaceGenerationId':fsPimCmnInterfaceGenerationId,'fsPimCmnInterfaceSuppressionInterval':fsPimCmnInterfaceSuppressionInterval,'fsPimCmnInterfaceAdminStatus':fsPimCmnInterfaceAdminStatus,'fsPimCmnInterfaceBorderBit':fsPimCmnInterfaceBorderBit,'fsPimCmnInterfaceGraftRetryInterval':fsPimCmnInterfaceGraftRetryInterval,'fsPimCmnInterfaceSRPriorityEnabled':fsPimCmnInterfaceSRPriorityEnabled,'fsPimCmnInterfaceTtl':fsPimCmnInterfaceTtl,'fsPimCmnInterfaceProtocol':fsPimCmnInterfaceProtocol,'fsPimCmnInterfaceRateLimit':fsPimCmnInterfaceRateLimit,'fsPimCmnInterfaceInMcastOctets':fsPimCmnInterfaceInMcastOctets,'fsPimCmnInterfaceOutMcastOctets':fsPimCmnInterfaceOutMcastOctets,'fsPimCmnInterfaceHCInMcastOctets':fsPimCmnInterfaceHCInMcastOctets,'fsPimCmnInterfaceHCOutMcastOctets':fsPimCmnInterfaceHCOutMcastOctets,'fsPimCmnInterfaceCompIdList':fsPimCmnInterfaceCompIdList,'fsPimCmnNeighborTable':fsPimCmnNeighborTable,'fsPimCmnNeighborEntry':fsPimCmnNeighborEntry,_U:fsPimCmnNeighborCompId,_V:fsPimCmnNeighborAddrType,_O:fsPimCmnNeighborAddress,_A8:fsPimCmnNeighborIfIndex,'fsPimCmnNeighborUpTime':fsPimCmnNeighborUpTime,'fsPimCmnNeighborExpiryTime':fsPimCmnNeighborExpiryTime,'fsPimCmnNeighborGenerationId':fsPimCmnNeighborGenerationId,'fsPimCmnNeighborLanDelay':fsPimCmnNeighborLanDelay,'fsPimCmnNeighborDRPriority':fsPimCmnNeighborDRPriority,'fsPimCmnNeighborOverrideInterval':fsPimCmnNeighborOverrideInterval,'fsPimCmnNeighborSRCapable':fsPimCmnNeighborSRCapable,'fsPimCmnNeighborRPFCapable':fsPimCmnNeighborRPFCapable,'fsPimCmnNeighborBidirCapable':fsPimCmnNeighborBidirCapable,'fsPimCmnIpMRouteTable':fsPimCmnIpMRouteTable,'fsPimCmnIpMRouteEntry':fsPimCmnIpMRouteEntry,_W:fsPimCmnIpMRouteCompId,_X:fsPimCmnIpMRouteAddrType,_Y:fsPimCmnIpMRouteGroup,_Z:fsPimCmnIpMRouteSource,_a:fsPimCmnIpMRouteSourceMasklen,'fsPimCmnIpMRouteUpstreamNeighbor':fsPimCmnIpMRouteUpstreamNeighbor,'fsPimCmnIpMRouteInIfIndex':fsPimCmnIpMRouteInIfIndex,'fsPimCmnIpMRouteUpTime':fsPimCmnIpMRouteUpTime,'fsPimCmnIpMRoutePkts':fsPimCmnIpMRoutePkts,'fsPimCmnIpMRouteUpstreamAssertTimer':fsPimCmnIpMRouteUpstreamAssertTimer,'fsPimCmnIpMRouteAssertMetric':fsPimCmnIpMRouteAssertMetric,'fsPimCmnIpMRouteAssertMetricPref':fsPimCmnIpMRouteAssertMetricPref,'fsPimCmnIpMRouteAssertRPTBit':fsPimCmnIpMRouteAssertRPTBit,'fsPimCmnIpMRouteTimerFlags':fsPimCmnIpMRouteTimerFlags,'fsPimCmnIpMRouteFlags':fsPimCmnIpMRouteFlags,'fsPimCmnIpMRouteUpstreamPruneState':fsPimCmnIpMRouteUpstreamPruneState,'fsPimCmnIpMRouteUpstreamPruneLimitTimer':fsPimCmnIpMRouteUpstreamPruneLimitTimer,'fsPimCmnIpMRouteOriginatorState':fsPimCmnIpMRouteOriginatorState,'fsPimCmnIpMRouteSourceActiveTimer':fsPimCmnIpMRouteSourceActiveTimer,'fsPimCmnIpMRouteStateRefreshTimer':fsPimCmnIpMRouteStateRefreshTimer,'fsPimCmnIpMRouteExpiryTime':fsPimCmnIpMRouteExpiryTime,'fsPimCmnIpMRouteDifferentInIfPackets':fsPimCmnIpMRouteDifferentInIfPackets,'fsPimCmnIpMRouteOctets':fsPimCmnIpMRouteOctets,'fsPimCmnIpMRouteProtocol':fsPimCmnIpMRouteProtocol,'fsPimCmnIpMRouteRtProto':fsPimCmnIpMRouteRtProto,'fsPimCmnIpMRouteRtAddress':fsPimCmnIpMRouteRtAddress,'fsPimCmnIpMRouteRtMasklen':fsPimCmnIpMRouteRtMasklen,'fsPimCmnIpMRouteRtType':fsPimCmnIpMRouteRtType,'fsPimCmnIpMRouteHCOctets':fsPimCmnIpMRouteHCOctets,'fsPimCmnIpMRouteOIfList':fsPimCmnIpMRouteOIfList,'fsPimCmnIpMRouteRPFVectorAddr':fsPimCmnIpMRouteRPFVectorAddr,'fsPimCmnIpMRoutePimMode':fsPimCmnIpMRoutePimMode,'fsPimCmnIpMRouteNextHopTable':fsPimCmnIpMRouteNextHopTable,'fsPimCmnIpMRouteNextHopEntry':fsPimCmnIpMRouteNextHopEntry,_c:fsPimCmnIpMRouteNextHopCompId,_d:fsPimCmnIpMRouteNextHopAddrType,_e:fsPimCmnIpMRouteNextHopGroup,_f:fsPimCmnIpMRouteNextHopSource,_g:fsPimCmnIpMRouteNextHopSourceMasklen,_h:fsPimCmnIpMRouteNextHopIfIndex,_i:fsPimCmnIpMRouteNextHopAddress,'fsPimCmnIpMRouteNextHopPruneReason':fsPimCmnIpMRouteNextHopPruneReason,'fsPimCmnIpMRouteNextHopState':fsPimCmnIpMRouteNextHopState,'fsPimCmnIpMRouteNextHopUpTime':fsPimCmnIpMRouteNextHopUpTime,'fsPimCmnIpMRouteNextHopExpiryTime':fsPimCmnIpMRouteNextHopExpiryTime,'fsPimCmnIpMRouteNextHopProtocol':fsPimCmnIpMRouteNextHopProtocol,'fsPimCmnIpMRouteNextHopPkts':fsPimCmnIpMRouteNextHopPkts,'fsPimCmnCandidateRPTable':fsPimCmnCandidateRPTable,'fsPimCmnCandidateRPEntry':fsPimCmnCandidateRPEntry,_j:fsPimCmnCandidateRPCompId,_k:fsPimCmnCandidateRPAddrType,_l:fsPimCmnCandidateRPGroupAddress,_m:fsPimCmnCandidateRPGroupMasklen,_n:fsPimCmnCandidateRPAddress,'fsPimCmnCandidateRPPriority':fsPimCmnCandidateRPPriority,'fsPimCmnCandidateRPRowStatus':fsPimCmnCandidateRPRowStatus,'fsPimCmnCandidateRPPimMode':fsPimCmnCandidateRPPimMode,'fsPimCmnStaticRPSetTable':fsPimCmnStaticRPSetTable,'fsPimCmnStaticRPSetEntry':fsPimCmnStaticRPSetEntry,_o:fsPimCmnStaticRPSetCompId,_p:fsPimCmnStaticRPAddrType,_q:fsPimCmnStaticRPSetGroupAddress,_r:fsPimCmnStaticRPSetGroupMasklen,'fsPimCmnStaticRPAddress':fsPimCmnStaticRPAddress,'fsPimCmnStaticRPRowStatus':fsPimCmnStaticRPRowStatus,'fsPimCmnStaticRPEmbdFlag':fsPimCmnStaticRPEmbdFlag,'fsPimCmnStaticRPPimMode':fsPimCmnStaticRPPimMode,'fsPimCmnComponentModeTable':fsPimCmnComponentModeTable,'fsPimCmnComponentModeEntry':fsPimCmnComponentModeEntry,_s:fsPimCmnComponentId,'fsPimCmnComponentMode':fsPimCmnComponentMode,'fsPimCmnCompGraftRetryCount':fsPimCmnCompGraftRetryCount,'fsPimCmnRegChkSumCfgTable':fsPimCmnRegChkSumCfgTable,'fsPimCmnRegChkSumCfgEntry':fsPimCmnRegChkSumCfgEntry,_t:fsPimCmnRegChkSumTblCompId,_u:fsPimCmnRegChkSumTblRPAddrType,_v:fsPimCmnRegChkSumTblRPAddress,'fsPimCmnRPChkSumStatus':fsPimCmnRPChkSumStatus,'fsPimCmnDFTable':fsPimCmnDFTable,'fsPimCmnDFEntry':fsPimCmnDFEntry,_w:fsPimCmnDFIfAddrType,_x:fsPimCmnDFElectedRP,_y:fsPimCmnDFIfIndex,'fsPimCmnDFState':fsPimCmnDFState,'fsPimCmnDFWinnerAddr':fsPimCmnDFWinnerAddr,'fsPimCmnDFWinnerUptime':fsPimCmnDFWinnerUptime,'fsPimCmnDFElectionStateTimer':fsPimCmnDFElectionStateTimer,'fsPimCmnDFWinnerMetric':fsPimCmnDFWinnerMetric,'fsPimCmnDFWinnerMetricPref':fsPimCmnDFWinnerMetricPref,'fsPimCmnDFMessageCount':fsPimCmnDFMessageCount,'fsPimCmnElectedRPTable':fsPimCmnElectedRPTable,'fsPimCmnElectedRPEntry':fsPimCmnElectedRPEntry,_z:fsPimCmnElectedRPCompId,_A0:fsPimCmnElectedRPAddrType,_A1:fsPimCmnElectedRPGroupAddress,_A2:fsPimCmnElectedRPGroupMasklen,'fsPimCmnElectedRPAddress':fsPimCmnElectedRPAddress,'fsPimCmnElectedRPPriority':fsPimCmnElectedRPPriority,'fsPimCmnElectedRPHoldTime':fsPimCmnElectedRPHoldTime,'fsPimCmnNeighborExtTable':fsPimCmnNeighborExtTable,'fsPimCmnNeighborExtEntry':fsPimCmnNeighborExtEntry,_A3:fsPimCmnNeighborExtIfIndex,_A4:fsPimCmnNeighborExtAddrType,_A5:fsPimCmnNeighborExtAddress,'fsPimCmnNeighborExtCompIdList':fsPimCmnNeighborExtCompIdList,'fsPimCmnNeighborExtUpTime':fsPimCmnNeighborExtUpTime,'fsPimCmnNeighborExtExpiryTime':fsPimCmnNeighborExtExpiryTime,'fsPimCmnNeighborExtGenerationId':fsPimCmnNeighborExtGenerationId,'fsPimCmnNeighborExtLanDelay':fsPimCmnNeighborExtLanDelay,'fsPimCmnNeighborExtDRPriority':fsPimCmnNeighborExtDRPriority,'fsPimCmnNeighborExtOverrideInterval':fsPimCmnNeighborExtOverrideInterval,'fsPimCmnNeighborExtSRCapable':fsPimCmnNeighborExtSRCapable,'fsPimCmnNeighborExtRPFCapable':fsPimCmnNeighborExtRPFCapable,'fsPimCmnNeighborExtBidirCapable':fsPimCmnNeighborExtBidirCapable,'futurePimCmnTrapsControl':futurePimCmnTrapsControl,_R:fsPimcmnHARtrId,_A7:fsPimCmnHAEvent,'futurePimCmnTraps':futurePimCmnTraps,'fsPimCmnTraps':fsPimCmnTraps,'fsPimCmnHAEventTrap':fsPimCmnHAEventTrap,'fsPimCmnBidirEventTrap':fsPimCmnBidirEventTrap})