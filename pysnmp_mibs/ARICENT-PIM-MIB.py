_j='fsPimRegChkSumTblRPAddress'
_i='fsPimRegChkSumTblCompId'
_h='fsPimComponentId'
_g='fsPimStaticRPSetGroupMask'
_f='fsPimStaticRPSetGroupAddress'
_e='fsPimStaticRPSetCompId'
_d='fsPimCandidateRPAddress'
_c='fsPimCandidateRPGroupMask'
_b='fsPimCandidateRPGroupAddress'
_a='fsPimCandidateRPCompId'
_Z='forwarding'
_Y='fsPimIpMRouteNextHopAddress'
_X='fsPimIpMRouteNextHopIfIndex'
_W='fsPimIpMRouteNextHopSourceMask'
_V='fsPimIpMRouteNextHopSource'
_U='fsPimIpMRouteNextHopGroup'
_T='fsPimIpMRouteNextHopCompId'
_S='fsPimIpMRouteSourceMask'
_R='fsPimIpMRouteSource'
_Q='fsPimIpMRouteGroup'
_P='fsPimIpMRouteCompId'
_O='fsPimNeighborCompId'
_N='fsPimNeighborAddress'
_M='fsPimInterfaceIfIndex'
_L='disabled'
_K='Unsigned32'
_J='read-create'
_I='enabled'
_H='enable'
_G='disable'
_F='not-accessible'
_E='read-write'
_D='ARICENT-PIM-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsPimMIB=ModuleIdentity((1,3,6,1,4,1,2076,20))
if mibBuilder.loadTexts:fsPimMIB.setRevisions(('2012-09-05 00:00',))
class Status(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_FsPimMIBObjects_ObjectIdentity=ObjectIdentity
fsPimMIBObjects=_FsPimMIBObjects_ObjectIdentity((1,3,6,1,4,1,2076,20,1))
_FuturePimScalars_ObjectIdentity=ObjectIdentity
futurePimScalars=_FuturePimScalars_ObjectIdentity((1,3,6,1,4,1,2076,20,1,1))
_FsPimVersionString_Type=DisplayString
_FsPimVersionString_Object=MibScalar
fsPimVersionString=_FsPimVersionString_Object((1,3,6,1,4,1,2076,20,1,1,1),_FsPimVersionString_Type())
fsPimVersionString.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimVersionString.setStatus(_A)
class _FsPimSPTGroupThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimSPTGroupThreshold_Type.__name__=_B
_FsPimSPTGroupThreshold_Object=MibScalar
fsPimSPTGroupThreshold=_FsPimSPTGroupThreshold_Object((1,3,6,1,4,1,2076,20,1,1,2),_FsPimSPTGroupThreshold_Type())
fsPimSPTGroupThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimSPTGroupThreshold.setStatus(_A)
class _FsPimSPTSourceThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimSPTSourceThreshold_Type.__name__=_B
_FsPimSPTSourceThreshold_Object=MibScalar
fsPimSPTSourceThreshold=_FsPimSPTSourceThreshold_Object((1,3,6,1,4,1,2076,20,1,1,3),_FsPimSPTSourceThreshold_Type())
fsPimSPTSourceThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimSPTSourceThreshold.setStatus(_A)
class _FsPimSPTSwitchingPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimSPTSwitchingPeriod_Type.__name__=_B
_FsPimSPTSwitchingPeriod_Object=MibScalar
fsPimSPTSwitchingPeriod=_FsPimSPTSwitchingPeriod_Object((1,3,6,1,4,1,2076,20,1,1,4),_FsPimSPTSwitchingPeriod_Type())
fsPimSPTSwitchingPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimSPTSwitchingPeriod.setStatus(_A)
class _FsPimSPTRpThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimSPTRpThreshold_Type.__name__=_B
_FsPimSPTRpThreshold_Object=MibScalar
fsPimSPTRpThreshold=_FsPimSPTRpThreshold_Object((1,3,6,1,4,1,2076,20,1,1,5),_FsPimSPTRpThreshold_Type())
fsPimSPTRpThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimSPTRpThreshold.setStatus(_A)
class _FsPimSPTRpSwitchingPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimSPTRpSwitchingPeriod_Type.__name__=_B
_FsPimSPTRpSwitchingPeriod_Object=MibScalar
fsPimSPTRpSwitchingPeriod=_FsPimSPTRpSwitchingPeriod_Object((1,3,6,1,4,1,2076,20,1,1,6),_FsPimSPTRpSwitchingPeriod_Type())
fsPimSPTRpSwitchingPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimSPTRpSwitchingPeriod.setStatus(_A)
class _FsPimRegStopRateLimitingPeriod_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPimRegStopRateLimitingPeriod_Type.__name__=_B
_FsPimRegStopRateLimitingPeriod_Object=MibScalar
fsPimRegStopRateLimitingPeriod=_FsPimRegStopRateLimitingPeriod_Object((1,3,6,1,4,1,2076,20,1,1,7),_FsPimRegStopRateLimitingPeriod_Type())
fsPimRegStopRateLimitingPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimRegStopRateLimitingPeriod.setStatus(_A)
_FsPimMemoryAllocFailCount_Type=Integer32
_FsPimMemoryAllocFailCount_Object=MibScalar
fsPimMemoryAllocFailCount=_FsPimMemoryAllocFailCount_Object((1,3,6,1,4,1,2076,20,1,1,8),_FsPimMemoryAllocFailCount_Type())
fsPimMemoryAllocFailCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimMemoryAllocFailCount.setStatus(_A)
class _FsPimGlobalTrace_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimGlobalTrace_Type.__name__=_B
_FsPimGlobalTrace_Object=MibScalar
fsPimGlobalTrace=_FsPimGlobalTrace_Object((1,3,6,1,4,1,2076,20,1,1,9),_FsPimGlobalTrace_Type())
fsPimGlobalTrace.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimGlobalTrace.setStatus(_A)
class _FsPimGlobalDebug_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimGlobalDebug_Type.__name__=_B
_FsPimGlobalDebug_Object=MibScalar
fsPimGlobalDebug=_FsPimGlobalDebug_Object((1,3,6,1,4,1,2076,20,1,1,10),_FsPimGlobalDebug_Type())
fsPimGlobalDebug.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimGlobalDebug.setStatus(_A)
class _FsPimPmbrStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsPimPmbrStatus_Type.__name__=_B
_FsPimPmbrStatus_Object=MibScalar
fsPimPmbrStatus=_FsPimPmbrStatus_Object((1,3,6,1,4,1,2076,20,1,1,11),_FsPimPmbrStatus_Type())
fsPimPmbrStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimPmbrStatus.setStatus(_A)
class _FsPimRouterMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ssmonly',1),('smssm',2)))
_FsPimRouterMode_Type.__name__=_B
_FsPimRouterMode_Object=MibScalar
fsPimRouterMode=_FsPimRouterMode_Object((1,3,6,1,4,1,2076,20,1,1,12),_FsPimRouterMode_Type())
fsPimRouterMode.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimRouterMode.setStatus(_A)
class _FsPimStaticRpEnabled_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_I,1)))
_FsPimStaticRpEnabled_Type.__name__=_B
_FsPimStaticRpEnabled_Object=MibScalar
fsPimStaticRpEnabled=_FsPimStaticRpEnabled_Object((1,3,6,1,4,1,2076,20,1,1,13),_FsPimStaticRpEnabled_Type())
fsPimStaticRpEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimStaticRpEnabled.setStatus(_A)
class _FsPimStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_L,2)))
_FsPimStatus_Type.__name__=_B
_FsPimStatus_Object=MibScalar
fsPimStatus=_FsPimStatus_Object((1,3,6,1,4,1,2076,20,1,1,14),_FsPimStatus_Type())
fsPimStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimStatus.setStatus(_A)
_FuturePimTables_ObjectIdentity=ObjectIdentity
futurePimTables=_FuturePimTables_ObjectIdentity((1,3,6,1,4,1,2076,20,1,2))
_FsPimInterfaceTable_Object=MibTable
fsPimInterfaceTable=_FsPimInterfaceTable_Object((1,3,6,1,4,1,2076,20,1,2,1))
if mibBuilder.loadTexts:fsPimInterfaceTable.setStatus(_A)
_FsPimInterfaceEntry_Object=MibTableRow
fsPimInterfaceEntry=_FsPimInterfaceEntry_Object((1,3,6,1,4,1,2076,20,1,2,1,1))
fsPimInterfaceEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:fsPimInterfaceEntry.setStatus(_A)
class _FsPimInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimInterfaceIfIndex_Type.__name__=_B
_FsPimInterfaceIfIndex_Object=MibTableColumn
fsPimInterfaceIfIndex=_FsPimInterfaceIfIndex_Object((1,3,6,1,4,1,2076,20,1,2,1,1,1),_FsPimInterfaceIfIndex_Type())
fsPimInterfaceIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimInterfaceIfIndex.setStatus(_A)
class _FsPimInterfaceCompId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimInterfaceCompId_Type.__name__=_B
_FsPimInterfaceCompId_Object=MibTableColumn
fsPimInterfaceCompId=_FsPimInterfaceCompId_Object((1,3,6,1,4,1,2076,20,1,2,1,1,2),_FsPimInterfaceCompId_Type())
fsPimInterfaceCompId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimInterfaceCompId.setStatus(_A)
class _FsPimInterfaceDRPriority_Type(Unsigned32):defaultValue=1
_FsPimInterfaceDRPriority_Type.__name__=_K
_FsPimInterfaceDRPriority_Object=MibTableColumn
fsPimInterfaceDRPriority=_FsPimInterfaceDRPriority_Object((1,3,6,1,4,1,2076,20,1,2,1,1,3),_FsPimInterfaceDRPriority_Type())
fsPimInterfaceDRPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimInterfaceDRPriority.setStatus(_A)
class _FsPimInterfaceHelloHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimInterfaceHelloHoldTime_Type.__name__=_B
_FsPimInterfaceHelloHoldTime_Object=MibTableColumn
fsPimInterfaceHelloHoldTime=_FsPimInterfaceHelloHoldTime_Object((1,3,6,1,4,1,2076,20,1,2,1,1,4),_FsPimInterfaceHelloHoldTime_Type())
fsPimInterfaceHelloHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimInterfaceHelloHoldTime.setStatus(_A)
class _FsPimInterfaceLanPruneDelayPresent_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_FsPimInterfaceLanPruneDelayPresent_Type.__name__=_B
_FsPimInterfaceLanPruneDelayPresent_Object=MibTableColumn
fsPimInterfaceLanPruneDelayPresent=_FsPimInterfaceLanPruneDelayPresent_Object((1,3,6,1,4,1,2076,20,1,2,1,1,5),_FsPimInterfaceLanPruneDelayPresent_Type())
fsPimInterfaceLanPruneDelayPresent.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimInterfaceLanPruneDelayPresent.setStatus(_A)
class _FsPimInterfaceLanDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimInterfaceLanDelay_Type.__name__=_B
_FsPimInterfaceLanDelay_Object=MibTableColumn
fsPimInterfaceLanDelay=_FsPimInterfaceLanDelay_Object((1,3,6,1,4,1,2076,20,1,2,1,1,6),_FsPimInterfaceLanDelay_Type())
fsPimInterfaceLanDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimInterfaceLanDelay.setStatus(_A)
class _FsPimInterfaceOverrideInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPimInterfaceOverrideInterval_Type.__name__=_B
_FsPimInterfaceOverrideInterval_Object=MibTableColumn
fsPimInterfaceOverrideInterval=_FsPimInterfaceOverrideInterval_Object((1,3,6,1,4,1,2076,20,1,2,1,1,7),_FsPimInterfaceOverrideInterval_Type())
fsPimInterfaceOverrideInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimInterfaceOverrideInterval.setStatus(_A)
_FsPimInterfaceGenerationId_Type=Integer32
_FsPimInterfaceGenerationId_Object=MibTableColumn
fsPimInterfaceGenerationId=_FsPimInterfaceGenerationId_Object((1,3,6,1,4,1,2076,20,1,2,1,1,8),_FsPimInterfaceGenerationId_Type())
fsPimInterfaceGenerationId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimInterfaceGenerationId.setStatus(_A)
_FsPimInterfaceSuppressionInterval_Type=Integer32
_FsPimInterfaceSuppressionInterval_Object=MibTableColumn
fsPimInterfaceSuppressionInterval=_FsPimInterfaceSuppressionInterval_Object((1,3,6,1,4,1,2076,20,1,2,1,1,9),_FsPimInterfaceSuppressionInterval_Type())
fsPimInterfaceSuppressionInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimInterfaceSuppressionInterval.setStatus(_A)
_FsPimInterfaceAdminStatus_Type=Integer32
_FsPimInterfaceAdminStatus_Object=MibTableColumn
fsPimInterfaceAdminStatus=_FsPimInterfaceAdminStatus_Object((1,3,6,1,4,1,2076,20,1,2,1,1,10),_FsPimInterfaceAdminStatus_Type())
fsPimInterfaceAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimInterfaceAdminStatus.setStatus(_A)
_FsPimInterfaceBorderBit_Type=Integer32
_FsPimInterfaceBorderBit_Object=MibTableColumn
fsPimInterfaceBorderBit=_FsPimInterfaceBorderBit_Object((1,3,6,1,4,1,2076,20,1,2,1,1,11),_FsPimInterfaceBorderBit_Type())
fsPimInterfaceBorderBit.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimInterfaceBorderBit.setStatus(_A)
_FsPimNeighborTable_Object=MibTable
fsPimNeighborTable=_FsPimNeighborTable_Object((1,3,6,1,4,1,2076,20,1,2,2))
if mibBuilder.loadTexts:fsPimNeighborTable.setStatus(_A)
_FsPimNeighborEntry_Object=MibTableRow
fsPimNeighborEntry=_FsPimNeighborEntry_Object((1,3,6,1,4,1,2076,20,1,2,2,1))
fsPimNeighborEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:fsPimNeighborEntry.setStatus(_A)
_FsPimNeighborAddress_Type=IpAddress
_FsPimNeighborAddress_Object=MibTableColumn
fsPimNeighborAddress=_FsPimNeighborAddress_Object((1,3,6,1,4,1,2076,20,1,2,2,1,1),_FsPimNeighborAddress_Type())
fsPimNeighborAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimNeighborAddress.setStatus(_A)
class _FsPimNeighborCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimNeighborCompId_Type.__name__=_B
_FsPimNeighborCompId_Object=MibTableColumn
fsPimNeighborCompId=_FsPimNeighborCompId_Object((1,3,6,1,4,1,2076,20,1,2,2,1,2),_FsPimNeighborCompId_Type())
fsPimNeighborCompId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimNeighborCompId.setStatus(_A)
_FsPimNeighborIfIndex_Type=Integer32
_FsPimNeighborIfIndex_Object=MibTableColumn
fsPimNeighborIfIndex=_FsPimNeighborIfIndex_Object((1,3,6,1,4,1,2076,20,1,2,2,1,3),_FsPimNeighborIfIndex_Type())
fsPimNeighborIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimNeighborIfIndex.setStatus(_A)
_FsPimNeighborUpTime_Type=TimeTicks
_FsPimNeighborUpTime_Object=MibTableColumn
fsPimNeighborUpTime=_FsPimNeighborUpTime_Object((1,3,6,1,4,1,2076,20,1,2,2,1,4),_FsPimNeighborUpTime_Type())
fsPimNeighborUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimNeighborUpTime.setStatus(_A)
_FsPimNeighborExpiryTime_Type=TimeTicks
_FsPimNeighborExpiryTime_Object=MibTableColumn
fsPimNeighborExpiryTime=_FsPimNeighborExpiryTime_Object((1,3,6,1,4,1,2076,20,1,2,2,1,5),_FsPimNeighborExpiryTime_Type())
fsPimNeighborExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimNeighborExpiryTime.setStatus(_A)
_FsPimNeighborGenerationId_Type=Integer32
_FsPimNeighborGenerationId_Object=MibTableColumn
fsPimNeighborGenerationId=_FsPimNeighborGenerationId_Object((1,3,6,1,4,1,2076,20,1,2,2,1,6),_FsPimNeighborGenerationId_Type())
fsPimNeighborGenerationId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimNeighborGenerationId.setStatus(_A)
_FsPimNeighborLanDelay_Type=Integer32
_FsPimNeighborLanDelay_Object=MibTableColumn
fsPimNeighborLanDelay=_FsPimNeighborLanDelay_Object((1,3,6,1,4,1,2076,20,1,2,2,1,7),_FsPimNeighborLanDelay_Type())
fsPimNeighborLanDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimNeighborLanDelay.setStatus(_A)
_FsPimNeighborDRPriority_Type=Unsigned32
_FsPimNeighborDRPriority_Object=MibTableColumn
fsPimNeighborDRPriority=_FsPimNeighborDRPriority_Object((1,3,6,1,4,1,2076,20,1,2,2,1,8),_FsPimNeighborDRPriority_Type())
fsPimNeighborDRPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimNeighborDRPriority.setStatus(_A)
_FsPimNeighborOverrideInterval_Type=Integer32
_FsPimNeighborOverrideInterval_Object=MibTableColumn
fsPimNeighborOverrideInterval=_FsPimNeighborOverrideInterval_Object((1,3,6,1,4,1,2076,20,1,2,2,1,9),_FsPimNeighborOverrideInterval_Type())
fsPimNeighborOverrideInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimNeighborOverrideInterval.setStatus(_A)
_FsPimIpMRouteTable_Object=MibTable
fsPimIpMRouteTable=_FsPimIpMRouteTable_Object((1,3,6,1,4,1,2076,20,1,2,3))
if mibBuilder.loadTexts:fsPimIpMRouteTable.setStatus(_A)
_FsPimIpMRouteEntry_Object=MibTableRow
fsPimIpMRouteEntry=_FsPimIpMRouteEntry_Object((1,3,6,1,4,1,2076,20,1,2,3,1))
fsPimIpMRouteEntry.setIndexNames((0,_D,_P),(0,_D,_Q),(0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:fsPimIpMRouteEntry.setStatus(_A)
class _FsPimIpMRouteCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimIpMRouteCompId_Type.__name__=_B
_FsPimIpMRouteCompId_Object=MibTableColumn
fsPimIpMRouteCompId=_FsPimIpMRouteCompId_Object((1,3,6,1,4,1,2076,20,1,2,3,1,1),_FsPimIpMRouteCompId_Type())
fsPimIpMRouteCompId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimIpMRouteCompId.setStatus(_A)
_FsPimIpMRouteGroup_Type=IpAddress
_FsPimIpMRouteGroup_Object=MibTableColumn
fsPimIpMRouteGroup=_FsPimIpMRouteGroup_Object((1,3,6,1,4,1,2076,20,1,2,3,1,2),_FsPimIpMRouteGroup_Type())
fsPimIpMRouteGroup.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimIpMRouteGroup.setStatus(_A)
_FsPimIpMRouteSource_Type=IpAddress
_FsPimIpMRouteSource_Object=MibTableColumn
fsPimIpMRouteSource=_FsPimIpMRouteSource_Object((1,3,6,1,4,1,2076,20,1,2,3,1,3),_FsPimIpMRouteSource_Type())
fsPimIpMRouteSource.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimIpMRouteSource.setStatus(_A)
_FsPimIpMRouteSourceMask_Type=IpAddress
_FsPimIpMRouteSourceMask_Object=MibTableColumn
fsPimIpMRouteSourceMask=_FsPimIpMRouteSourceMask_Object((1,3,6,1,4,1,2076,20,1,2,3,1,4),_FsPimIpMRouteSourceMask_Type())
fsPimIpMRouteSourceMask.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimIpMRouteSourceMask.setStatus(_A)
_FsPimIpMRouteUpstreamNeighbor_Type=IpAddress
_FsPimIpMRouteUpstreamNeighbor_Object=MibTableColumn
fsPimIpMRouteUpstreamNeighbor=_FsPimIpMRouteUpstreamNeighbor_Object((1,3,6,1,4,1,2076,20,1,2,3,1,5),_FsPimIpMRouteUpstreamNeighbor_Type())
fsPimIpMRouteUpstreamNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimIpMRouteUpstreamNeighbor.setStatus(_A)
_FsPimIpMRouteInIfIndex_Type=Integer32
_FsPimIpMRouteInIfIndex_Object=MibTableColumn
fsPimIpMRouteInIfIndex=_FsPimIpMRouteInIfIndex_Object((1,3,6,1,4,1,2076,20,1,2,3,1,6),_FsPimIpMRouteInIfIndex_Type())
fsPimIpMRouteInIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimIpMRouteInIfIndex.setStatus(_A)
_FsPimIpMRouteUpTime_Type=TimeTicks
_FsPimIpMRouteUpTime_Object=MibTableColumn
fsPimIpMRouteUpTime=_FsPimIpMRouteUpTime_Object((1,3,6,1,4,1,2076,20,1,2,3,1,7),_FsPimIpMRouteUpTime_Type())
fsPimIpMRouteUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimIpMRouteUpTime.setStatus(_A)
_FsPimIpMRoutePkts_Type=Counter32
_FsPimIpMRoutePkts_Object=MibTableColumn
fsPimIpMRoutePkts=_FsPimIpMRoutePkts_Object((1,3,6,1,4,1,2076,20,1,2,3,1,8),_FsPimIpMRoutePkts_Type())
fsPimIpMRoutePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimIpMRoutePkts.setStatus(_A)
_FsPimIpMRouteUpstreamAssertTimer_Type=TimeTicks
_FsPimIpMRouteUpstreamAssertTimer_Object=MibTableColumn
fsPimIpMRouteUpstreamAssertTimer=_FsPimIpMRouteUpstreamAssertTimer_Object((1,3,6,1,4,1,2076,20,1,2,3,1,9),_FsPimIpMRouteUpstreamAssertTimer_Type())
fsPimIpMRouteUpstreamAssertTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimIpMRouteUpstreamAssertTimer.setStatus(_A)
_FsPimIpMRouteAssertMetric_Type=Integer32
_FsPimIpMRouteAssertMetric_Object=MibTableColumn
fsPimIpMRouteAssertMetric=_FsPimIpMRouteAssertMetric_Object((1,3,6,1,4,1,2076,20,1,2,3,1,10),_FsPimIpMRouteAssertMetric_Type())
fsPimIpMRouteAssertMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimIpMRouteAssertMetric.setStatus(_A)
_FsPimIpMRouteAssertMetricPref_Type=Integer32
_FsPimIpMRouteAssertMetricPref_Object=MibTableColumn
fsPimIpMRouteAssertMetricPref=_FsPimIpMRouteAssertMetricPref_Object((1,3,6,1,4,1,2076,20,1,2,3,1,11),_FsPimIpMRouteAssertMetricPref_Type())
fsPimIpMRouteAssertMetricPref.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimIpMRouteAssertMetricPref.setStatus(_A)
_FsPimIpMRouteAssertRPTBit_Type=TruthValue
_FsPimIpMRouteAssertRPTBit_Object=MibTableColumn
fsPimIpMRouteAssertRPTBit=_FsPimIpMRouteAssertRPTBit_Object((1,3,6,1,4,1,2076,20,1,2,3,1,12),_FsPimIpMRouteAssertRPTBit_Type())
fsPimIpMRouteAssertRPTBit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimIpMRouteAssertRPTBit.setStatus(_A)
_FsPimIpMRouteTimerFlags_Type=Integer32
_FsPimIpMRouteTimerFlags_Object=MibTableColumn
fsPimIpMRouteTimerFlags=_FsPimIpMRouteTimerFlags_Object((1,3,6,1,4,1,2076,20,1,2,3,1,13),_FsPimIpMRouteTimerFlags_Type())
fsPimIpMRouteTimerFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimIpMRouteTimerFlags.setStatus(_A)
_FsPimIpMRouteFlags_Type=Integer32
_FsPimIpMRouteFlags_Object=MibTableColumn
fsPimIpMRouteFlags=_FsPimIpMRouteFlags_Object((1,3,6,1,4,1,2076,20,1,2,3,1,14),_FsPimIpMRouteFlags_Type())
fsPimIpMRouteFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimIpMRouteFlags.setStatus(_A)
_FsPimIpMRouteNextHopTable_Object=MibTable
fsPimIpMRouteNextHopTable=_FsPimIpMRouteNextHopTable_Object((1,3,6,1,4,1,2076,20,1,2,4))
if mibBuilder.loadTexts:fsPimIpMRouteNextHopTable.setStatus(_A)
_FsPimIpMRouteNextHopEntry_Object=MibTableRow
fsPimIpMRouteNextHopEntry=_FsPimIpMRouteNextHopEntry_Object((1,3,6,1,4,1,2076,20,1,2,4,1))
fsPimIpMRouteNextHopEntry.setIndexNames((0,_D,_T),(0,_D,_U),(0,_D,_V),(0,_D,_W),(0,_D,_X),(0,_D,_Y))
if mibBuilder.loadTexts:fsPimIpMRouteNextHopEntry.setStatus(_A)
class _FsPimIpMRouteNextHopCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimIpMRouteNextHopCompId_Type.__name__=_B
_FsPimIpMRouteNextHopCompId_Object=MibTableColumn
fsPimIpMRouteNextHopCompId=_FsPimIpMRouteNextHopCompId_Object((1,3,6,1,4,1,2076,20,1,2,4,1,1),_FsPimIpMRouteNextHopCompId_Type())
fsPimIpMRouteNextHopCompId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimIpMRouteNextHopCompId.setStatus(_A)
_FsPimIpMRouteNextHopGroup_Type=IpAddress
_FsPimIpMRouteNextHopGroup_Object=MibTableColumn
fsPimIpMRouteNextHopGroup=_FsPimIpMRouteNextHopGroup_Object((1,3,6,1,4,1,2076,20,1,2,4,1,2),_FsPimIpMRouteNextHopGroup_Type())
fsPimIpMRouteNextHopGroup.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimIpMRouteNextHopGroup.setStatus(_A)
_FsPimIpMRouteNextHopSource_Type=IpAddress
_FsPimIpMRouteNextHopSource_Object=MibTableColumn
fsPimIpMRouteNextHopSource=_FsPimIpMRouteNextHopSource_Object((1,3,6,1,4,1,2076,20,1,2,4,1,3),_FsPimIpMRouteNextHopSource_Type())
fsPimIpMRouteNextHopSource.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimIpMRouteNextHopSource.setStatus(_A)
_FsPimIpMRouteNextHopSourceMask_Type=IpAddress
_FsPimIpMRouteNextHopSourceMask_Object=MibTableColumn
fsPimIpMRouteNextHopSourceMask=_FsPimIpMRouteNextHopSourceMask_Object((1,3,6,1,4,1,2076,20,1,2,4,1,4),_FsPimIpMRouteNextHopSourceMask_Type())
fsPimIpMRouteNextHopSourceMask.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimIpMRouteNextHopSourceMask.setStatus(_A)
class _FsPimIpMRouteNextHopIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimIpMRouteNextHopIfIndex_Type.__name__=_B
_FsPimIpMRouteNextHopIfIndex_Object=MibTableColumn
fsPimIpMRouteNextHopIfIndex=_FsPimIpMRouteNextHopIfIndex_Object((1,3,6,1,4,1,2076,20,1,2,4,1,5),_FsPimIpMRouteNextHopIfIndex_Type())
fsPimIpMRouteNextHopIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimIpMRouteNextHopIfIndex.setStatus(_A)
_FsPimIpMRouteNextHopAddress_Type=IpAddress
_FsPimIpMRouteNextHopAddress_Object=MibTableColumn
fsPimIpMRouteNextHopAddress=_FsPimIpMRouteNextHopAddress_Object((1,3,6,1,4,1,2076,20,1,2,4,1,6),_FsPimIpMRouteNextHopAddress_Type())
fsPimIpMRouteNextHopAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimIpMRouteNextHopAddress.setStatus(_A)
class _FsPimIpMRouteNextHopPruneReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Z,0),('other',1),('prune',2),('assert',3)))
_FsPimIpMRouteNextHopPruneReason_Type.__name__=_B
_FsPimIpMRouteNextHopPruneReason_Object=MibTableColumn
fsPimIpMRouteNextHopPruneReason=_FsPimIpMRouteNextHopPruneReason_Object((1,3,6,1,4,1,2076,20,1,2,4,1,7),_FsPimIpMRouteNextHopPruneReason_Type())
fsPimIpMRouteNextHopPruneReason.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimIpMRouteNextHopPruneReason.setStatus(_A)
class _FsPimIpMRouteNextHopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pruned',1),(_Z,2)))
_FsPimIpMRouteNextHopState_Type.__name__=_B
_FsPimIpMRouteNextHopState_Object=MibTableColumn
fsPimIpMRouteNextHopState=_FsPimIpMRouteNextHopState_Object((1,3,6,1,4,1,2076,20,1,2,4,1,8),_FsPimIpMRouteNextHopState_Type())
fsPimIpMRouteNextHopState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimIpMRouteNextHopState.setStatus(_A)
_FsPimCandidateRPTable_Object=MibTable
fsPimCandidateRPTable=_FsPimCandidateRPTable_Object((1,3,6,1,4,1,2076,20,1,2,6))
if mibBuilder.loadTexts:fsPimCandidateRPTable.setStatus(_A)
_FsPimCandidateRPEntry_Object=MibTableRow
fsPimCandidateRPEntry=_FsPimCandidateRPEntry_Object((1,3,6,1,4,1,2076,20,1,2,6,1))
fsPimCandidateRPEntry.setIndexNames((0,_D,_a),(0,_D,_b),(0,_D,_c),(0,_D,_d))
if mibBuilder.loadTexts:fsPimCandidateRPEntry.setStatus(_A)
class _FsPimCandidateRPCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimCandidateRPCompId_Type.__name__=_B
_FsPimCandidateRPCompId_Object=MibTableColumn
fsPimCandidateRPCompId=_FsPimCandidateRPCompId_Object((1,3,6,1,4,1,2076,20,1,2,6,1,1),_FsPimCandidateRPCompId_Type())
fsPimCandidateRPCompId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCandidateRPCompId.setStatus(_A)
_FsPimCandidateRPGroupAddress_Type=IpAddress
_FsPimCandidateRPGroupAddress_Object=MibTableColumn
fsPimCandidateRPGroupAddress=_FsPimCandidateRPGroupAddress_Object((1,3,6,1,4,1,2076,20,1,2,6,1,2),_FsPimCandidateRPGroupAddress_Type())
fsPimCandidateRPGroupAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCandidateRPGroupAddress.setStatus(_A)
_FsPimCandidateRPGroupMask_Type=IpAddress
_FsPimCandidateRPGroupMask_Object=MibTableColumn
fsPimCandidateRPGroupMask=_FsPimCandidateRPGroupMask_Object((1,3,6,1,4,1,2076,20,1,2,6,1,3),_FsPimCandidateRPGroupMask_Type())
fsPimCandidateRPGroupMask.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCandidateRPGroupMask.setStatus(_A)
_FsPimCandidateRPAddress_Type=IpAddress
_FsPimCandidateRPAddress_Object=MibTableColumn
fsPimCandidateRPAddress=_FsPimCandidateRPAddress_Object((1,3,6,1,4,1,2076,20,1,2,6,1,4),_FsPimCandidateRPAddress_Type())
fsPimCandidateRPAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimCandidateRPAddress.setStatus(_A)
class _FsPimCandidateRPPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPimCandidateRPPriority_Type.__name__=_B
_FsPimCandidateRPPriority_Object=MibTableColumn
fsPimCandidateRPPriority=_FsPimCandidateRPPriority_Object((1,3,6,1,4,1,2076,20,1,2,6,1,5),_FsPimCandidateRPPriority_Type())
fsPimCandidateRPPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCandidateRPPriority.setStatus(_A)
_FsPimCandidateRPRowStatus_Type=RowStatus
_FsPimCandidateRPRowStatus_Object=MibTableColumn
fsPimCandidateRPRowStatus=_FsPimCandidateRPRowStatus_Object((1,3,6,1,4,1,2076,20,1,2,6,1,6),_FsPimCandidateRPRowStatus_Type())
fsPimCandidateRPRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:fsPimCandidateRPRowStatus.setStatus(_A)
_FsPimStaticRPSetTable_Object=MibTable
fsPimStaticRPSetTable=_FsPimStaticRPSetTable_Object((1,3,6,1,4,1,2076,20,1,2,7))
if mibBuilder.loadTexts:fsPimStaticRPSetTable.setStatus(_A)
_FsPimStaticRPSetEntry_Object=MibTableRow
fsPimStaticRPSetEntry=_FsPimStaticRPSetEntry_Object((1,3,6,1,4,1,2076,20,1,2,7,1))
fsPimStaticRPSetEntry.setIndexNames((0,_D,_e),(0,_D,_f),(0,_D,_g))
if mibBuilder.loadTexts:fsPimStaticRPSetEntry.setStatus(_A)
class _FsPimStaticRPSetCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimStaticRPSetCompId_Type.__name__=_B
_FsPimStaticRPSetCompId_Object=MibTableColumn
fsPimStaticRPSetCompId=_FsPimStaticRPSetCompId_Object((1,3,6,1,4,1,2076,20,1,2,7,1,1),_FsPimStaticRPSetCompId_Type())
fsPimStaticRPSetCompId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimStaticRPSetCompId.setStatus(_A)
_FsPimStaticRPSetGroupAddress_Type=IpAddress
_FsPimStaticRPSetGroupAddress_Object=MibTableColumn
fsPimStaticRPSetGroupAddress=_FsPimStaticRPSetGroupAddress_Object((1,3,6,1,4,1,2076,20,1,2,7,1,2),_FsPimStaticRPSetGroupAddress_Type())
fsPimStaticRPSetGroupAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimStaticRPSetGroupAddress.setStatus(_A)
_FsPimStaticRPSetGroupMask_Type=IpAddress
_FsPimStaticRPSetGroupMask_Object=MibTableColumn
fsPimStaticRPSetGroupMask=_FsPimStaticRPSetGroupMask_Object((1,3,6,1,4,1,2076,20,1,2,7,1,3),_FsPimStaticRPSetGroupMask_Type())
fsPimStaticRPSetGroupMask.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimStaticRPSetGroupMask.setStatus(_A)
_FsPimStaticRPAddress_Type=IpAddress
_FsPimStaticRPAddress_Object=MibTableColumn
fsPimStaticRPAddress=_FsPimStaticRPAddress_Object((1,3,6,1,4,1,2076,20,1,2,7,1,4),_FsPimStaticRPAddress_Type())
fsPimStaticRPAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:fsPimStaticRPAddress.setStatus(_A)
_FsPimStaticRPRowStatus_Type=RowStatus
_FsPimStaticRPRowStatus_Object=MibTableColumn
fsPimStaticRPRowStatus=_FsPimStaticRPRowStatus_Object((1,3,6,1,4,1,2076,20,1,2,7,1,5),_FsPimStaticRPRowStatus_Type())
fsPimStaticRPRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:fsPimStaticRPRowStatus.setStatus(_A)
_FsPimComponentModeTable_Object=MibTable
fsPimComponentModeTable=_FsPimComponentModeTable_Object((1,3,6,1,4,1,2076,20,1,2,8))
if mibBuilder.loadTexts:fsPimComponentModeTable.setStatus(_A)
_FsPimComponentModeEntry_Object=MibTableRow
fsPimComponentModeEntry=_FsPimComponentModeEntry_Object((1,3,6,1,4,1,2076,20,1,2,8,1))
fsPimComponentModeEntry.setIndexNames((0,_D,_h))
if mibBuilder.loadTexts:fsPimComponentModeEntry.setStatus(_A)
class _FsPimComponentId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimComponentId_Type.__name__=_B
_FsPimComponentId_Object=MibTableColumn
fsPimComponentId=_FsPimComponentId_Object((1,3,6,1,4,1,2076,20,1,2,8,1,1),_FsPimComponentId_Type())
fsPimComponentId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimComponentId.setStatus(_A)
class _FsPimComponentMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dense',1),('sparse',2)))
_FsPimComponentMode_Type.__name__=_B
_FsPimComponentMode_Object=MibTableColumn
fsPimComponentMode=_FsPimComponentMode_Object((1,3,6,1,4,1,2076,20,1,2,8,1,2),_FsPimComponentMode_Type())
fsPimComponentMode.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimComponentMode.setStatus(_A)
class _FsPimCompGraftRetryCount_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPimCompGraftRetryCount_Type.__name__=_B
_FsPimCompGraftRetryCount_Object=MibTableColumn
fsPimCompGraftRetryCount=_FsPimCompGraftRetryCount_Object((1,3,6,1,4,1,2076,20,1,2,8,1,3),_FsPimCompGraftRetryCount_Type())
fsPimCompGraftRetryCount.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimCompGraftRetryCount.setStatus(_A)
_FsPimRegChkSumCfgTable_Object=MibTable
fsPimRegChkSumCfgTable=_FsPimRegChkSumCfgTable_Object((1,3,6,1,4,1,2076,20,1,2,9))
if mibBuilder.loadTexts:fsPimRegChkSumCfgTable.setStatus(_A)
_FsPimRegChkSumCfgEntry_Object=MibTableRow
fsPimRegChkSumCfgEntry=_FsPimRegChkSumCfgEntry_Object((1,3,6,1,4,1,2076,20,1,2,9,1))
fsPimRegChkSumCfgEntry.setIndexNames((0,_D,_i),(0,_D,_j))
if mibBuilder.loadTexts:fsPimRegChkSumCfgEntry.setStatus(_A)
class _FsPimRegChkSumTblCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimRegChkSumTblCompId_Type.__name__=_B
_FsPimRegChkSumTblCompId_Object=MibTableColumn
fsPimRegChkSumTblCompId=_FsPimRegChkSumTblCompId_Object((1,3,6,1,4,1,2076,20,1,2,9,1,1),_FsPimRegChkSumTblCompId_Type())
fsPimRegChkSumTblCompId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimRegChkSumTblCompId.setStatus(_A)
_FsPimRegChkSumTblRPAddress_Type=IpAddress
_FsPimRegChkSumTblRPAddress_Object=MibTableColumn
fsPimRegChkSumTblRPAddress=_FsPimRegChkSumTblRPAddress_Object((1,3,6,1,4,1,2076,20,1,2,9,1,2),_FsPimRegChkSumTblRPAddress_Type())
fsPimRegChkSumTblRPAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimRegChkSumTblRPAddress.setStatus(_A)
class _FsPimRPChkSumStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_L,2)))
_FsPimRPChkSumStatus_Type.__name__=_B
_FsPimRPChkSumStatus_Object=MibTableColumn
fsPimRPChkSumStatus=_FsPimRPChkSumStatus_Object((1,3,6,1,4,1,2076,20,1,2,9,1,3),_FsPimRPChkSumStatus_Type())
fsPimRPChkSumStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPimRPChkSumStatus.setStatus(_A)
_FuturePimTraps_ObjectIdentity=ObjectIdentity
futurePimTraps=_FuturePimTraps_ObjectIdentity((1,3,6,1,4,1,2076,20,1,3))
mibBuilder.exportSymbols(_D,**{'Status':Status,'fsPimMIB':fsPimMIB,'fsPimMIBObjects':fsPimMIBObjects,'futurePimScalars':futurePimScalars,'fsPimVersionString':fsPimVersionString,'fsPimSPTGroupThreshold':fsPimSPTGroupThreshold,'fsPimSPTSourceThreshold':fsPimSPTSourceThreshold,'fsPimSPTSwitchingPeriod':fsPimSPTSwitchingPeriod,'fsPimSPTRpThreshold':fsPimSPTRpThreshold,'fsPimSPTRpSwitchingPeriod':fsPimSPTRpSwitchingPeriod,'fsPimRegStopRateLimitingPeriod':fsPimRegStopRateLimitingPeriod,'fsPimMemoryAllocFailCount':fsPimMemoryAllocFailCount,'fsPimGlobalTrace':fsPimGlobalTrace,'fsPimGlobalDebug':fsPimGlobalDebug,'fsPimPmbrStatus':fsPimPmbrStatus,'fsPimRouterMode':fsPimRouterMode,'fsPimStaticRpEnabled':fsPimStaticRpEnabled,'fsPimStatus':fsPimStatus,'futurePimTables':futurePimTables,'fsPimInterfaceTable':fsPimInterfaceTable,'fsPimInterfaceEntry':fsPimInterfaceEntry,_M:fsPimInterfaceIfIndex,'fsPimInterfaceCompId':fsPimInterfaceCompId,'fsPimInterfaceDRPriority':fsPimInterfaceDRPriority,'fsPimInterfaceHelloHoldTime':fsPimInterfaceHelloHoldTime,'fsPimInterfaceLanPruneDelayPresent':fsPimInterfaceLanPruneDelayPresent,'fsPimInterfaceLanDelay':fsPimInterfaceLanDelay,'fsPimInterfaceOverrideInterval':fsPimInterfaceOverrideInterval,'fsPimInterfaceGenerationId':fsPimInterfaceGenerationId,'fsPimInterfaceSuppressionInterval':fsPimInterfaceSuppressionInterval,'fsPimInterfaceAdminStatus':fsPimInterfaceAdminStatus,'fsPimInterfaceBorderBit':fsPimInterfaceBorderBit,'fsPimNeighborTable':fsPimNeighborTable,'fsPimNeighborEntry':fsPimNeighborEntry,_N:fsPimNeighborAddress,_O:fsPimNeighborCompId,'fsPimNeighborIfIndex':fsPimNeighborIfIndex,'fsPimNeighborUpTime':fsPimNeighborUpTime,'fsPimNeighborExpiryTime':fsPimNeighborExpiryTime,'fsPimNeighborGenerationId':fsPimNeighborGenerationId,'fsPimNeighborLanDelay':fsPimNeighborLanDelay,'fsPimNeighborDRPriority':fsPimNeighborDRPriority,'fsPimNeighborOverrideInterval':fsPimNeighborOverrideInterval,'fsPimIpMRouteTable':fsPimIpMRouteTable,'fsPimIpMRouteEntry':fsPimIpMRouteEntry,_P:fsPimIpMRouteCompId,_Q:fsPimIpMRouteGroup,_R:fsPimIpMRouteSource,_S:fsPimIpMRouteSourceMask,'fsPimIpMRouteUpstreamNeighbor':fsPimIpMRouteUpstreamNeighbor,'fsPimIpMRouteInIfIndex':fsPimIpMRouteInIfIndex,'fsPimIpMRouteUpTime':fsPimIpMRouteUpTime,'fsPimIpMRoutePkts':fsPimIpMRoutePkts,'fsPimIpMRouteUpstreamAssertTimer':fsPimIpMRouteUpstreamAssertTimer,'fsPimIpMRouteAssertMetric':fsPimIpMRouteAssertMetric,'fsPimIpMRouteAssertMetricPref':fsPimIpMRouteAssertMetricPref,'fsPimIpMRouteAssertRPTBit':fsPimIpMRouteAssertRPTBit,'fsPimIpMRouteTimerFlags':fsPimIpMRouteTimerFlags,'fsPimIpMRouteFlags':fsPimIpMRouteFlags,'fsPimIpMRouteNextHopTable':fsPimIpMRouteNextHopTable,'fsPimIpMRouteNextHopEntry':fsPimIpMRouteNextHopEntry,_T:fsPimIpMRouteNextHopCompId,_U:fsPimIpMRouteNextHopGroup,_V:fsPimIpMRouteNextHopSource,_W:fsPimIpMRouteNextHopSourceMask,_X:fsPimIpMRouteNextHopIfIndex,_Y:fsPimIpMRouteNextHopAddress,'fsPimIpMRouteNextHopPruneReason':fsPimIpMRouteNextHopPruneReason,'fsPimIpMRouteNextHopState':fsPimIpMRouteNextHopState,'fsPimCandidateRPTable':fsPimCandidateRPTable,'fsPimCandidateRPEntry':fsPimCandidateRPEntry,_a:fsPimCandidateRPCompId,_b:fsPimCandidateRPGroupAddress,_c:fsPimCandidateRPGroupMask,_d:fsPimCandidateRPAddress,'fsPimCandidateRPPriority':fsPimCandidateRPPriority,'fsPimCandidateRPRowStatus':fsPimCandidateRPRowStatus,'fsPimStaticRPSetTable':fsPimStaticRPSetTable,'fsPimStaticRPSetEntry':fsPimStaticRPSetEntry,_e:fsPimStaticRPSetCompId,_f:fsPimStaticRPSetGroupAddress,_g:fsPimStaticRPSetGroupMask,'fsPimStaticRPAddress':fsPimStaticRPAddress,'fsPimStaticRPRowStatus':fsPimStaticRPRowStatus,'fsPimComponentModeTable':fsPimComponentModeTable,'fsPimComponentModeEntry':fsPimComponentModeEntry,_h:fsPimComponentId,'fsPimComponentMode':fsPimComponentMode,'fsPimCompGraftRetryCount':fsPimCompGraftRetryCount,'fsPimRegChkSumCfgTable':fsPimRegChkSumCfgTable,'fsPimRegChkSumCfgEntry':fsPimRegChkSumCfgEntry,_i:fsPimRegChkSumTblCompId,_j:fsPimRegChkSumTblRPAddress,'fsPimRPChkSumStatus':fsPimRPChkSumStatus,'futurePimTraps':futurePimTraps})