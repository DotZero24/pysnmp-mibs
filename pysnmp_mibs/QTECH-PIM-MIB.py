_Au='qtechPimMIBGroup'
_At='qtechPimNeighborLoss'
_As='qtechPimRpCandidateStatus'
_Ar='qtechPimRpCandidateAclName'
_Aq='qtechPimStaticRPStatus'
_Ap='qtechPimStaticRPAclName'
_Ao='qtechPimStaticRPAddressIsOverride'
_An='qtechPimRPNextRPReachableIn'
_Am='qtechPimRPExpiryTime'
_Al='qtechPimRPAddress'
_Ak='qtechPimBsrCandidatePriority'
_Aj='qtechPimBsrCandidateHashMaskLength'
_Ai='qtechPimBsrCandidateIfindex'
_Ah='qtechPimStateRefreshTimeToLive'
_Ag='qtechPimStateRefreshLimitInterval'
_Af='qtechPimStateRefreshInterval'
_Ae='qtechPimSourceLifetime'
_Ad='qtechPimComponentNextCandRPAdv'
_Ac='qtechPimComponentBSRNextBsrMessage'
_Ab='qtechPimComponentBSRHashMaskLength'
_Aa='qtechPimComponentBSRPriority'
_AZ='qtechPimComponentBSRUptime'
_AY='qtechPimComponentCRPHoldTime'
_AX='qtechPimComponentBSRExpiryTime'
_AW='qtechPimComponentBSRAddress'
_AV='qtechPimRPSetUpTime'
_AU='qtechPimRPSetExpiryTime'
_AT='qtechPimRPSetHoldTime'
_AS='qtechPimIpMRouteNextHopJoinPruneTimer'
_AR='qtechPimIpMRouteNextHopAssertMetricPref'
_AQ='qtechPimIpMRouteNextHopAssertMetric'
_AP='qtechPimIpMRouteNextHopAssertTimer'
_AO='qtechPimIpMRouteNextHopAssertWinner'
_AN='qtechPimIpMRouteNextHopPruneReason'
_AM='qtechPimIpMRouteOriginatorSRTTL'
_AL='qtechPimIpMRouteSourceTimer'
_AK='qtechPimIpMRouteRPFNeighbor'
_AJ='qtechPimIpMRouteFlags'
_AI='qtechPimIpMRouteAssertRPTBit'
_AH='qtechPimIpMRouteAssertMetricPref'
_AG='qtechPimIpMRouteAssertMetric'
_AF='qtechPimIpMRouteUpstreamAssertTimer'
_AE='qtechPimNeighborDRPresent'
_AD='qtechPimNeighborSRCapable'
_AC='qtechPimNeighborTBit'
_AB='qtechPimNeighborOverrideInterval'
_AA='qtechPimNeighborLanPruneDelay'
_A9='qtechPimNeighborMode'
_A8='qtechPimNeighborExpiryTime'
_A7='qtechPimNeighborUpTime'
_A6='qtechPimDrSupportAddressBound'
_A5='qtechPimNeighborFilterAcl'
_A4='qtechPimInterfaceEnabled'
_A3='qtechPimInterfaceCountOut'
_A2='qtechPimInterfaceCountIn'
_A1='qtechPimInterfaceBsrBorderEnabled'
_A0='qtechPimInterfaceNbrCounter'
_z='qtechPimInterfaceDRPriority'
_y='qtechPimInterfaceSRCapable'
_x='qtechPimInterfaceLanDelayEnabled'
_w='qtechPimInterfaceSRTTLThreshold'
_v='qtechPimInterfaceMaxGraftRetries'
_u='qtechPimInterfaceGraftRetryInterval'
_t='qtechPimInterfaceJoinPruneHoldtime'
_s='qtechPimInterfaceGenerationID'
_r='qtechPimInterfaceOverrideInterval'
_q='qtechPimInterfacePropagationDelay'
_p='qtechPimInterfaceLanPruneDelay'
_o='qtechPimInterfaceHelloHoldtime'
_n='qtechPimInterfaceTrigHelloInterval'
_m='qtechPimInterfaceCBSRPreference'
_l='qtechPimInterfaceJoinPruneInterval'
_k='qtechPimInterfaceHelloInterval'
_j='qtechPimInterfaceDR'
_i='qtechPimInterfaceMode'
_h='qtechPimInterfaceNetMask'
_g='qtechPimInterfaceAddress'
_f='qtechPimJoinPruneInterval'
_e='qtechPimRpCandidateIfindex'
_d='qtechPimStaticRPAddress'
_c='qtechPimRPGroupAddress'
_b='qtechPimComponentIndex'
_a='qtechPimRPSetAddress'
_Z='qtechPimRPSetGroupMask'
_Y='qtechPimRPSetGroupAddress'
_X='qtechPimRPSetComponent'
_W='qtechPimNeighborAddress'
_V='sparse'
_U='qtechPimInterfaceIfIndex'
_T='ipMRouteSourceMask'
_S='ipMRouteSource'
_R='ipMRouteNextHopSourceMask'
_Q='ipMRouteNextHopSource'
_P='ipMRouteNextHopIfIndex'
_O='ipMRouteNextHopGroup'
_N='ipMRouteNextHopAddress'
_M='ipMRouteGroup'
_L='qtechPimNeighborIfIndex'
_K='EnabledStatus'
_J='DisplayString'
_I='read-create'
_H='IPMROUTE-STD-MIB'
_G='not-accessible'
_F='seconds'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='QTECH-PIM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ipMRouteGroup,ipMRouteNextHopAddress,ipMRouteNextHopGroup,ipMRouteNextHopIfIndex,ipMRouteNextHopSource,ipMRouteNextHopSourceMask,ipMRouteSource,ipMRouteSourceMask=mibBuilder.importSymbols(_H,_M,_N,_O,_P,_Q,_R,_S,_T)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_K)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention','TruthValue')
qtechPimMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,27))
if mibBuilder.loadTexts:qtechPimMIB.setRevisions(('2003-01-20 00:00',))
_QtechPimMIBObjects_ObjectIdentity=ObjectIdentity
qtechPimMIBObjects=_QtechPimMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,27,1))
_QtechPim_ObjectIdentity=ObjectIdentity
qtechPim=_QtechPim_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,27,1,1))
class _QtechPimJoinPruneInterval_Type(Integer32):defaultValue=60
_QtechPimJoinPruneInterval_Type.__name__=_D
_QtechPimJoinPruneInterval_Object=MibScalar
qtechPimJoinPruneInterval=_QtechPimJoinPruneInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,1),_QtechPimJoinPruneInterval_Type())
qtechPimJoinPruneInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimJoinPruneInterval.setStatus(_A)
if mibBuilder.loadTexts:qtechPimJoinPruneInterval.setUnits(_F)
_QtechPimInterfaceTable_Object=MibTable
qtechPimInterfaceTable=_QtechPimInterfaceTable_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2))
if mibBuilder.loadTexts:qtechPimInterfaceTable.setStatus(_A)
_QtechPimInterfaceEntry_Object=MibTableRow
qtechPimInterfaceEntry=_QtechPimInterfaceEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1))
qtechPimInterfaceEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:qtechPimInterfaceEntry.setStatus(_A)
_QtechPimInterfaceIfIndex_Type=InterfaceIndex
_QtechPimInterfaceIfIndex_Object=MibTableColumn
qtechPimInterfaceIfIndex=_QtechPimInterfaceIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,1),_QtechPimInterfaceIfIndex_Type())
qtechPimInterfaceIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechPimInterfaceIfIndex.setStatus(_A)
_QtechPimInterfaceAddress_Type=IpAddress
_QtechPimInterfaceAddress_Object=MibTableColumn
qtechPimInterfaceAddress=_QtechPimInterfaceAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,2),_QtechPimInterfaceAddress_Type())
qtechPimInterfaceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimInterfaceAddress.setStatus(_A)
_QtechPimInterfaceNetMask_Type=IpAddress
_QtechPimInterfaceNetMask_Object=MibTableColumn
qtechPimInterfaceNetMask=_QtechPimInterfaceNetMask_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,3),_QtechPimInterfaceNetMask_Type())
qtechPimInterfaceNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimInterfaceNetMask.setStatus(_A)
class _QtechPimInterfaceMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dense',1),(_V,2),('sparseDense',3)))
_QtechPimInterfaceMode_Type.__name__=_D
_QtechPimInterfaceMode_Object=MibTableColumn
qtechPimInterfaceMode=_QtechPimInterfaceMode_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,4),_QtechPimInterfaceMode_Type())
qtechPimInterfaceMode.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceMode.setStatus(_A)
_QtechPimInterfaceDR_Type=IpAddress
_QtechPimInterfaceDR_Object=MibTableColumn
qtechPimInterfaceDR=_QtechPimInterfaceDR_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,5),_QtechPimInterfaceDR_Type())
qtechPimInterfaceDR.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimInterfaceDR.setStatus(_A)
class _QtechPimInterfaceHelloInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechPimInterfaceHelloInterval_Type.__name__=_D
_QtechPimInterfaceHelloInterval_Object=MibTableColumn
qtechPimInterfaceHelloInterval=_QtechPimInterfaceHelloInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,6),_QtechPimInterfaceHelloInterval_Type())
qtechPimInterfaceHelloInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:qtechPimInterfaceHelloInterval.setUnits(_F)
_QtechPimInterfaceJoinPruneInterval_Type=Integer32
_QtechPimInterfaceJoinPruneInterval_Object=MibTableColumn
qtechPimInterfaceJoinPruneInterval=_QtechPimInterfaceJoinPruneInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,7),_QtechPimInterfaceJoinPruneInterval_Type())
qtechPimInterfaceJoinPruneInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceJoinPruneInterval.setStatus(_A)
if mibBuilder.loadTexts:qtechPimInterfaceJoinPruneInterval.setUnits(_F)
class _QtechPimInterfaceCBSRPreference_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_QtechPimInterfaceCBSRPreference_Type.__name__=_D
_QtechPimInterfaceCBSRPreference_Object=MibTableColumn
qtechPimInterfaceCBSRPreference=_QtechPimInterfaceCBSRPreference_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,8),_QtechPimInterfaceCBSRPreference_Type())
qtechPimInterfaceCBSRPreference.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceCBSRPreference.setStatus(_A)
class _QtechPimInterfaceTrigHelloInterval_Type(Integer32):defaultValue=5
_QtechPimInterfaceTrigHelloInterval_Type.__name__=_D
_QtechPimInterfaceTrigHelloInterval_Object=MibTableColumn
qtechPimInterfaceTrigHelloInterval=_QtechPimInterfaceTrigHelloInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,9),_QtechPimInterfaceTrigHelloInterval_Type())
qtechPimInterfaceTrigHelloInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceTrigHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:qtechPimInterfaceTrigHelloInterval.setUnits(_F)
class _QtechPimInterfaceHelloHoldtime_Type(Integer32):defaultValue=105;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechPimInterfaceHelloHoldtime_Type.__name__=_D
_QtechPimInterfaceHelloHoldtime_Object=MibTableColumn
qtechPimInterfaceHelloHoldtime=_QtechPimInterfaceHelloHoldtime_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,10),_QtechPimInterfaceHelloHoldtime_Type())
qtechPimInterfaceHelloHoldtime.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceHelloHoldtime.setStatus(_A)
if mibBuilder.loadTexts:qtechPimInterfaceHelloHoldtime.setUnits(_F)
class _QtechPimInterfaceLanPruneDelay_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_QtechPimInterfaceLanPruneDelay_Type.__name__=_D
_QtechPimInterfaceLanPruneDelay_Object=MibTableColumn
qtechPimInterfaceLanPruneDelay=_QtechPimInterfaceLanPruneDelay_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,11),_QtechPimInterfaceLanPruneDelay_Type())
qtechPimInterfaceLanPruneDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceLanPruneDelay.setStatus(_A)
class _QtechPimInterfacePropagationDelay_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_QtechPimInterfacePropagationDelay_Type.__name__=_D
_QtechPimInterfacePropagationDelay_Object=MibTableColumn
qtechPimInterfacePropagationDelay=_QtechPimInterfacePropagationDelay_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,12),_QtechPimInterfacePropagationDelay_Type())
qtechPimInterfacePropagationDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfacePropagationDelay.setStatus(_A)
if mibBuilder.loadTexts:qtechPimInterfacePropagationDelay.setUnits('milliseconds')
class _QtechPimInterfaceOverrideInterval_Type(Integer32):defaultValue=2500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechPimInterfaceOverrideInterval_Type.__name__=_D
_QtechPimInterfaceOverrideInterval_Object=MibTableColumn
qtechPimInterfaceOverrideInterval=_QtechPimInterfaceOverrideInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,13),_QtechPimInterfaceOverrideInterval_Type())
qtechPimInterfaceOverrideInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceOverrideInterval.setStatus(_A)
class _QtechPimInterfaceGenerationID_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_QtechPimInterfaceGenerationID_Type.__name__=_D
_QtechPimInterfaceGenerationID_Object=MibTableColumn
qtechPimInterfaceGenerationID=_QtechPimInterfaceGenerationID_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,14),_QtechPimInterfaceGenerationID_Type())
qtechPimInterfaceGenerationID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceGenerationID.setStatus(_A)
class _QtechPimInterfaceJoinPruneHoldtime_Type(Integer32):defaultValue=210;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechPimInterfaceJoinPruneHoldtime_Type.__name__=_D
_QtechPimInterfaceJoinPruneHoldtime_Object=MibTableColumn
qtechPimInterfaceJoinPruneHoldtime=_QtechPimInterfaceJoinPruneHoldtime_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,15),_QtechPimInterfaceJoinPruneHoldtime_Type())
qtechPimInterfaceJoinPruneHoldtime.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceJoinPruneHoldtime.setStatus(_A)
if mibBuilder.loadTexts:qtechPimInterfaceJoinPruneHoldtime.setUnits(_F)
class _QtechPimInterfaceGraftRetryInterval_Type(Integer32):defaultValue=3
_QtechPimInterfaceGraftRetryInterval_Type.__name__=_D
_QtechPimInterfaceGraftRetryInterval_Object=MibTableColumn
qtechPimInterfaceGraftRetryInterval=_QtechPimInterfaceGraftRetryInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,16),_QtechPimInterfaceGraftRetryInterval_Type())
qtechPimInterfaceGraftRetryInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceGraftRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:qtechPimInterfaceGraftRetryInterval.setUnits(_F)
class _QtechPimInterfaceMaxGraftRetries_Type(Integer32):defaultValue=2
_QtechPimInterfaceMaxGraftRetries_Type.__name__=_D
_QtechPimInterfaceMaxGraftRetries_Object=MibTableColumn
qtechPimInterfaceMaxGraftRetries=_QtechPimInterfaceMaxGraftRetries_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,17),_QtechPimInterfaceMaxGraftRetries_Type())
qtechPimInterfaceMaxGraftRetries.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceMaxGraftRetries.setStatus(_A)
class _QtechPimInterfaceSRTTLThreshold_Type(Integer32):defaultValue=0
_QtechPimInterfaceSRTTLThreshold_Type.__name__=_D
_QtechPimInterfaceSRTTLThreshold_Object=MibTableColumn
qtechPimInterfaceSRTTLThreshold=_QtechPimInterfaceSRTTLThreshold_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,18),_QtechPimInterfaceSRTTLThreshold_Type())
qtechPimInterfaceSRTTLThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceSRTTLThreshold.setStatus(_A)
_QtechPimInterfaceLanDelayEnabled_Type=TruthValue
_QtechPimInterfaceLanDelayEnabled_Object=MibTableColumn
qtechPimInterfaceLanDelayEnabled=_QtechPimInterfaceLanDelayEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,19),_QtechPimInterfaceLanDelayEnabled_Type())
qtechPimInterfaceLanDelayEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimInterfaceLanDelayEnabled.setStatus(_A)
_QtechPimInterfaceSRCapable_Type=TruthValue
_QtechPimInterfaceSRCapable_Object=MibTableColumn
qtechPimInterfaceSRCapable=_QtechPimInterfaceSRCapable_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,20),_QtechPimInterfaceSRCapable_Type())
qtechPimInterfaceSRCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimInterfaceSRCapable.setStatus(_A)
class _QtechPimInterfaceDRPriority_Type(Integer32):defaultValue=1
_QtechPimInterfaceDRPriority_Type.__name__=_D
_QtechPimInterfaceDRPriority_Object=MibTableColumn
qtechPimInterfaceDRPriority=_QtechPimInterfaceDRPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,21),_QtechPimInterfaceDRPriority_Type())
qtechPimInterfaceDRPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceDRPriority.setStatus(_A)
_QtechPimInterfaceNbrCounter_Type=Integer32
_QtechPimInterfaceNbrCounter_Object=MibTableColumn
qtechPimInterfaceNbrCounter=_QtechPimInterfaceNbrCounter_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,22),_QtechPimInterfaceNbrCounter_Type())
qtechPimInterfaceNbrCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimInterfaceNbrCounter.setStatus(_A)
class _QtechPimInterfaceBsrBorderEnabled_Type(EnabledStatus):defaultValue=2
_QtechPimInterfaceBsrBorderEnabled_Type.__name__=_K
_QtechPimInterfaceBsrBorderEnabled_Object=MibTableColumn
qtechPimInterfaceBsrBorderEnabled=_QtechPimInterfaceBsrBorderEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,23),_QtechPimInterfaceBsrBorderEnabled_Type())
qtechPimInterfaceBsrBorderEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceBsrBorderEnabled.setStatus(_A)
_QtechPimInterfaceCountIn_Type=Integer32
_QtechPimInterfaceCountIn_Object=MibTableColumn
qtechPimInterfaceCountIn=_QtechPimInterfaceCountIn_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,24),_QtechPimInterfaceCountIn_Type())
qtechPimInterfaceCountIn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimInterfaceCountIn.setStatus(_A)
_QtechPimInterfaceCountOut_Type=Integer32
_QtechPimInterfaceCountOut_Object=MibTableColumn
qtechPimInterfaceCountOut=_QtechPimInterfaceCountOut_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,25),_QtechPimInterfaceCountOut_Type())
qtechPimInterfaceCountOut.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimInterfaceCountOut.setStatus(_A)
class _QtechPimInterfaceEnabled_Type(EnabledStatus):defaultValue=2
_QtechPimInterfaceEnabled_Type.__name__=_K
_QtechPimInterfaceEnabled_Object=MibTableColumn
qtechPimInterfaceEnabled=_QtechPimInterfaceEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,26),_QtechPimInterfaceEnabled_Type())
qtechPimInterfaceEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimInterfaceEnabled.setStatus(_A)
class _QtechPimNeighborFilterAcl_Type(DisplayString):defaultValue=OctetString('')
_QtechPimNeighborFilterAcl_Type.__name__=_J
_QtechPimNeighborFilterAcl_Object=MibTableColumn
qtechPimNeighborFilterAcl=_QtechPimNeighborFilterAcl_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,27),_QtechPimNeighborFilterAcl_Type())
qtechPimNeighborFilterAcl.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimNeighborFilterAcl.setStatus(_A)
class _QtechPimDrSupportAddressBound_Type(DisplayString):defaultValue=OctetString('')
_QtechPimDrSupportAddressBound_Type.__name__=_J
_QtechPimDrSupportAddressBound_Object=MibTableColumn
qtechPimDrSupportAddressBound=_QtechPimDrSupportAddressBound_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,2,1,28),_QtechPimDrSupportAddressBound_Type())
qtechPimDrSupportAddressBound.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimDrSupportAddressBound.setStatus(_A)
_QtechPimNeighborTable_Object=MibTable
qtechPimNeighborTable=_QtechPimNeighborTable_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,3))
if mibBuilder.loadTexts:qtechPimNeighborTable.setStatus(_A)
_QtechPimNeighborEntry_Object=MibTableRow
qtechPimNeighborEntry=_QtechPimNeighborEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,3,1))
qtechPimNeighborEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:qtechPimNeighborEntry.setStatus(_A)
_QtechPimNeighborAddress_Type=IpAddress
_QtechPimNeighborAddress_Object=MibTableColumn
qtechPimNeighborAddress=_QtechPimNeighborAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,3,1,1),_QtechPimNeighborAddress_Type())
qtechPimNeighborAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechPimNeighborAddress.setStatus(_A)
_QtechPimNeighborIfIndex_Type=InterfaceIndex
_QtechPimNeighborIfIndex_Object=MibTableColumn
qtechPimNeighborIfIndex=_QtechPimNeighborIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,3,1,2),_QtechPimNeighborIfIndex_Type())
qtechPimNeighborIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimNeighborIfIndex.setStatus(_A)
_QtechPimNeighborUpTime_Type=TimeTicks
_QtechPimNeighborUpTime_Object=MibTableColumn
qtechPimNeighborUpTime=_QtechPimNeighborUpTime_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,3,1,3),_QtechPimNeighborUpTime_Type())
qtechPimNeighborUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimNeighborUpTime.setStatus(_A)
_QtechPimNeighborExpiryTime_Type=TimeTicks
_QtechPimNeighborExpiryTime_Object=MibTableColumn
qtechPimNeighborExpiryTime=_QtechPimNeighborExpiryTime_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,3,1,4),_QtechPimNeighborExpiryTime_Type())
qtechPimNeighborExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimNeighborExpiryTime.setStatus(_A)
class _QtechPimNeighborMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dense',1),(_V,2)))
_QtechPimNeighborMode_Type.__name__=_D
_QtechPimNeighborMode_Object=MibTableColumn
qtechPimNeighborMode=_QtechPimNeighborMode_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,3,1,5),_QtechPimNeighborMode_Type())
qtechPimNeighborMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimNeighborMode.setStatus('deprecated')
_QtechPimNeighborLanPruneDelay_Type=Integer32
_QtechPimNeighborLanPruneDelay_Object=MibTableColumn
qtechPimNeighborLanPruneDelay=_QtechPimNeighborLanPruneDelay_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,3,1,6),_QtechPimNeighborLanPruneDelay_Type())
qtechPimNeighborLanPruneDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimNeighborLanPruneDelay.setStatus(_A)
_QtechPimNeighborOverrideInterval_Type=Integer32
_QtechPimNeighborOverrideInterval_Object=MibTableColumn
qtechPimNeighborOverrideInterval=_QtechPimNeighborOverrideInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,3,1,7),_QtechPimNeighborOverrideInterval_Type())
qtechPimNeighborOverrideInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimNeighborOverrideInterval.setStatus(_A)
_QtechPimNeighborTBit_Type=Integer32
_QtechPimNeighborTBit_Object=MibTableColumn
qtechPimNeighborTBit=_QtechPimNeighborTBit_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,3,1,8),_QtechPimNeighborTBit_Type())
qtechPimNeighborTBit.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimNeighborTBit.setStatus(_A)
_QtechPimNeighborSRCapable_Type=TruthValue
_QtechPimNeighborSRCapable_Object=MibTableColumn
qtechPimNeighborSRCapable=_QtechPimNeighborSRCapable_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,3,1,9),_QtechPimNeighborSRCapable_Type())
qtechPimNeighborSRCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimNeighborSRCapable.setStatus(_A)
_QtechPimNeighborDRPresent_Type=TruthValue
_QtechPimNeighborDRPresent_Object=MibTableColumn
qtechPimNeighborDRPresent=_QtechPimNeighborDRPresent_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,3,1,10),_QtechPimNeighborDRPresent_Type())
qtechPimNeighborDRPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimNeighborDRPresent.setStatus(_A)
_QtechPimIpMRouteTable_Object=MibTable
qtechPimIpMRouteTable=_QtechPimIpMRouteTable_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,4))
if mibBuilder.loadTexts:qtechPimIpMRouteTable.setStatus(_A)
_QtechPimIpMRouteEntry_Object=MibTableRow
qtechPimIpMRouteEntry=_QtechPimIpMRouteEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,4,1))
qtechPimIpMRouteEntry.setIndexNames((0,_H,_M),(0,_H,_S),(0,_H,_T))
if mibBuilder.loadTexts:qtechPimIpMRouteEntry.setStatus(_A)
_QtechPimIpMRouteUpstreamAssertTimer_Type=TimeTicks
_QtechPimIpMRouteUpstreamAssertTimer_Object=MibTableColumn
qtechPimIpMRouteUpstreamAssertTimer=_QtechPimIpMRouteUpstreamAssertTimer_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,4,1,1),_QtechPimIpMRouteUpstreamAssertTimer_Type())
qtechPimIpMRouteUpstreamAssertTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimIpMRouteUpstreamAssertTimer.setStatus(_A)
_QtechPimIpMRouteAssertMetric_Type=Integer32
_QtechPimIpMRouteAssertMetric_Object=MibTableColumn
qtechPimIpMRouteAssertMetric=_QtechPimIpMRouteAssertMetric_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,4,1,2),_QtechPimIpMRouteAssertMetric_Type())
qtechPimIpMRouteAssertMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimIpMRouteAssertMetric.setStatus(_A)
_QtechPimIpMRouteAssertMetricPref_Type=Integer32
_QtechPimIpMRouteAssertMetricPref_Object=MibTableColumn
qtechPimIpMRouteAssertMetricPref=_QtechPimIpMRouteAssertMetricPref_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,4,1,3),_QtechPimIpMRouteAssertMetricPref_Type())
qtechPimIpMRouteAssertMetricPref.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimIpMRouteAssertMetricPref.setStatus(_A)
_QtechPimIpMRouteAssertRPTBit_Type=TruthValue
_QtechPimIpMRouteAssertRPTBit_Object=MibTableColumn
qtechPimIpMRouteAssertRPTBit=_QtechPimIpMRouteAssertRPTBit_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,4,1,4),_QtechPimIpMRouteAssertRPTBit_Type())
qtechPimIpMRouteAssertRPTBit.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimIpMRouteAssertRPTBit.setStatus(_A)
class _QtechPimIpMRouteFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('rpt',0),('spt',1)))
_QtechPimIpMRouteFlags_Type.__name__=_D
_QtechPimIpMRouteFlags_Object=MibTableColumn
qtechPimIpMRouteFlags=_QtechPimIpMRouteFlags_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,4,1,5),_QtechPimIpMRouteFlags_Type())
qtechPimIpMRouteFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimIpMRouteFlags.setStatus(_A)
_QtechPimIpMRouteRPFNeighbor_Type=IpAddress
_QtechPimIpMRouteRPFNeighbor_Object=MibTableColumn
qtechPimIpMRouteRPFNeighbor=_QtechPimIpMRouteRPFNeighbor_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,4,1,6),_QtechPimIpMRouteRPFNeighbor_Type())
qtechPimIpMRouteRPFNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimIpMRouteRPFNeighbor.setStatus(_A)
_QtechPimIpMRouteSourceTimer_Type=TimeTicks
_QtechPimIpMRouteSourceTimer_Object=MibTableColumn
qtechPimIpMRouteSourceTimer=_QtechPimIpMRouteSourceTimer_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,4,1,7),_QtechPimIpMRouteSourceTimer_Type())
qtechPimIpMRouteSourceTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimIpMRouteSourceTimer.setStatus(_A)
_QtechPimIpMRouteOriginatorSRTTL_Type=Integer32
_QtechPimIpMRouteOriginatorSRTTL_Object=MibTableColumn
qtechPimIpMRouteOriginatorSRTTL=_QtechPimIpMRouteOriginatorSRTTL_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,4,1,8),_QtechPimIpMRouteOriginatorSRTTL_Type())
qtechPimIpMRouteOriginatorSRTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimIpMRouteOriginatorSRTTL.setStatus(_A)
_QtechPimIpMRouteNextHopTable_Object=MibTable
qtechPimIpMRouteNextHopTable=_QtechPimIpMRouteNextHopTable_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,5))
if mibBuilder.loadTexts:qtechPimIpMRouteNextHopTable.setStatus(_A)
_QtechPimIpMRouteNextHopEntry_Object=MibTableRow
qtechPimIpMRouteNextHopEntry=_QtechPimIpMRouteNextHopEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,5,1))
qtechPimIpMRouteNextHopEntry.setIndexNames((0,_H,_O),(0,_H,_Q),(0,_H,_R),(0,_H,_P),(0,_H,_N))
if mibBuilder.loadTexts:qtechPimIpMRouteNextHopEntry.setStatus(_A)
class _QtechPimIpMRouteNextHopPruneReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('prune',2),('assert',3)))
_QtechPimIpMRouteNextHopPruneReason_Type.__name__=_D
_QtechPimIpMRouteNextHopPruneReason_Object=MibTableColumn
qtechPimIpMRouteNextHopPruneReason=_QtechPimIpMRouteNextHopPruneReason_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,5,1,1),_QtechPimIpMRouteNextHopPruneReason_Type())
qtechPimIpMRouteNextHopPruneReason.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimIpMRouteNextHopPruneReason.setStatus(_A)
_QtechPimIpMRouteNextHopAssertWinner_Type=IpAddress
_QtechPimIpMRouteNextHopAssertWinner_Object=MibTableColumn
qtechPimIpMRouteNextHopAssertWinner=_QtechPimIpMRouteNextHopAssertWinner_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,5,1,2),_QtechPimIpMRouteNextHopAssertWinner_Type())
qtechPimIpMRouteNextHopAssertWinner.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimIpMRouteNextHopAssertWinner.setStatus(_A)
_QtechPimIpMRouteNextHopAssertTimer_Type=TimeTicks
_QtechPimIpMRouteNextHopAssertTimer_Object=MibTableColumn
qtechPimIpMRouteNextHopAssertTimer=_QtechPimIpMRouteNextHopAssertTimer_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,5,1,3),_QtechPimIpMRouteNextHopAssertTimer_Type())
qtechPimIpMRouteNextHopAssertTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimIpMRouteNextHopAssertTimer.setStatus(_A)
_QtechPimIpMRouteNextHopAssertMetric_Type=Integer32
_QtechPimIpMRouteNextHopAssertMetric_Object=MibTableColumn
qtechPimIpMRouteNextHopAssertMetric=_QtechPimIpMRouteNextHopAssertMetric_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,5,1,4),_QtechPimIpMRouteNextHopAssertMetric_Type())
qtechPimIpMRouteNextHopAssertMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimIpMRouteNextHopAssertMetric.setStatus(_A)
_QtechPimIpMRouteNextHopAssertMetricPref_Type=Integer32
_QtechPimIpMRouteNextHopAssertMetricPref_Object=MibTableColumn
qtechPimIpMRouteNextHopAssertMetricPref=_QtechPimIpMRouteNextHopAssertMetricPref_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,5,1,5),_QtechPimIpMRouteNextHopAssertMetricPref_Type())
qtechPimIpMRouteNextHopAssertMetricPref.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimIpMRouteNextHopAssertMetricPref.setStatus(_A)
_QtechPimIpMRouteNextHopJoinPruneTimer_Type=TimeTicks
_QtechPimIpMRouteNextHopJoinPruneTimer_Object=MibTableColumn
qtechPimIpMRouteNextHopJoinPruneTimer=_QtechPimIpMRouteNextHopJoinPruneTimer_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,5,1,6),_QtechPimIpMRouteNextHopJoinPruneTimer_Type())
qtechPimIpMRouteNextHopJoinPruneTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimIpMRouteNextHopJoinPruneTimer.setStatus(_A)
_QtechPimRPSetTable_Object=MibTable
qtechPimRPSetTable=_QtechPimRPSetTable_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,6))
if mibBuilder.loadTexts:qtechPimRPSetTable.setStatus(_A)
_QtechPimRPSetEntry_Object=MibTableRow
qtechPimRPSetEntry=_QtechPimRPSetEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,6,1))
qtechPimRPSetEntry.setIndexNames((0,_B,_X),(0,_B,_Y),(0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:qtechPimRPSetEntry.setStatus(_A)
_QtechPimRPSetGroupAddress_Type=IpAddress
_QtechPimRPSetGroupAddress_Object=MibTableColumn
qtechPimRPSetGroupAddress=_QtechPimRPSetGroupAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,6,1,1),_QtechPimRPSetGroupAddress_Type())
qtechPimRPSetGroupAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechPimRPSetGroupAddress.setStatus(_A)
_QtechPimRPSetGroupMask_Type=IpAddress
_QtechPimRPSetGroupMask_Object=MibTableColumn
qtechPimRPSetGroupMask=_QtechPimRPSetGroupMask_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,6,1,2),_QtechPimRPSetGroupMask_Type())
qtechPimRPSetGroupMask.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechPimRPSetGroupMask.setStatus(_A)
_QtechPimRPSetAddress_Type=IpAddress
_QtechPimRPSetAddress_Object=MibTableColumn
qtechPimRPSetAddress=_QtechPimRPSetAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,6,1,3),_QtechPimRPSetAddress_Type())
qtechPimRPSetAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechPimRPSetAddress.setStatus(_A)
class _QtechPimRPSetHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QtechPimRPSetHoldTime_Type.__name__=_D
_QtechPimRPSetHoldTime_Object=MibTableColumn
qtechPimRPSetHoldTime=_QtechPimRPSetHoldTime_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,6,1,4),_QtechPimRPSetHoldTime_Type())
qtechPimRPSetHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimRPSetHoldTime.setStatus(_A)
if mibBuilder.loadTexts:qtechPimRPSetHoldTime.setUnits(_F)
_QtechPimRPSetExpiryTime_Type=TimeTicks
_QtechPimRPSetExpiryTime_Object=MibTableColumn
qtechPimRPSetExpiryTime=_QtechPimRPSetExpiryTime_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,6,1,5),_QtechPimRPSetExpiryTime_Type())
qtechPimRPSetExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimRPSetExpiryTime.setStatus(_A)
class _QtechPimRPSetComponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_QtechPimRPSetComponent_Type.__name__=_D
_QtechPimRPSetComponent_Object=MibTableColumn
qtechPimRPSetComponent=_QtechPimRPSetComponent_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,6,1,6),_QtechPimRPSetComponent_Type())
qtechPimRPSetComponent.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechPimRPSetComponent.setStatus(_A)
_QtechPimRPSetUpTime_Type=TimeTicks
_QtechPimRPSetUpTime_Object=MibTableColumn
qtechPimRPSetUpTime=_QtechPimRPSetUpTime_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,6,1,7),_QtechPimRPSetUpTime_Type())
qtechPimRPSetUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimRPSetUpTime.setStatus(_A)
_QtechPimComponentTable_Object=MibTable
qtechPimComponentTable=_QtechPimComponentTable_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,7))
if mibBuilder.loadTexts:qtechPimComponentTable.setStatus(_A)
_QtechPimComponentEntry_Object=MibTableRow
qtechPimComponentEntry=_QtechPimComponentEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,7,1))
qtechPimComponentEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:qtechPimComponentEntry.setStatus(_A)
class _QtechPimComponentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_QtechPimComponentIndex_Type.__name__=_D
_QtechPimComponentIndex_Object=MibTableColumn
qtechPimComponentIndex=_QtechPimComponentIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,7,1,1),_QtechPimComponentIndex_Type())
qtechPimComponentIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechPimComponentIndex.setStatus(_A)
_QtechPimComponentBSRAddress_Type=IpAddress
_QtechPimComponentBSRAddress_Object=MibTableColumn
qtechPimComponentBSRAddress=_QtechPimComponentBSRAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,7,1,2),_QtechPimComponentBSRAddress_Type())
qtechPimComponentBSRAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimComponentBSRAddress.setStatus(_A)
_QtechPimComponentBSRExpiryTime_Type=TimeTicks
_QtechPimComponentBSRExpiryTime_Object=MibTableColumn
qtechPimComponentBSRExpiryTime=_QtechPimComponentBSRExpiryTime_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,7,1,3),_QtechPimComponentBSRExpiryTime_Type())
qtechPimComponentBSRExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimComponentBSRExpiryTime.setStatus(_A)
class _QtechPimComponentCRPHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QtechPimComponentCRPHoldTime_Type.__name__=_D
_QtechPimComponentCRPHoldTime_Object=MibTableColumn
qtechPimComponentCRPHoldTime=_QtechPimComponentCRPHoldTime_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,7,1,4),_QtechPimComponentCRPHoldTime_Type())
qtechPimComponentCRPHoldTime.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechPimComponentCRPHoldTime.setStatus(_A)
if mibBuilder.loadTexts:qtechPimComponentCRPHoldTime.setUnits(_F)
_QtechPimComponentBSRUptime_Type=TimeTicks
_QtechPimComponentBSRUptime_Object=MibTableColumn
qtechPimComponentBSRUptime=_QtechPimComponentBSRUptime_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,7,1,5),_QtechPimComponentBSRUptime_Type())
qtechPimComponentBSRUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimComponentBSRUptime.setStatus(_A)
_QtechPimComponentBSRPriority_Type=Integer32
_QtechPimComponentBSRPriority_Object=MibTableColumn
qtechPimComponentBSRPriority=_QtechPimComponentBSRPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,7,1,6),_QtechPimComponentBSRPriority_Type())
qtechPimComponentBSRPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimComponentBSRPriority.setStatus(_A)
_QtechPimComponentBSRHashMaskLength_Type=Integer32
_QtechPimComponentBSRHashMaskLength_Object=MibTableColumn
qtechPimComponentBSRHashMaskLength=_QtechPimComponentBSRHashMaskLength_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,7,1,7),_QtechPimComponentBSRHashMaskLength_Type())
qtechPimComponentBSRHashMaskLength.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimComponentBSRHashMaskLength.setStatus(_A)
_QtechPimComponentBSRNextBsrMessage_Type=TimeTicks
_QtechPimComponentBSRNextBsrMessage_Object=MibTableColumn
qtechPimComponentBSRNextBsrMessage=_QtechPimComponentBSRNextBsrMessage_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,7,1,8),_QtechPimComponentBSRNextBsrMessage_Type())
qtechPimComponentBSRNextBsrMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimComponentBSRNextBsrMessage.setStatus(_A)
_QtechPimComponentNextCandRPAdv_Type=TimeTicks
_QtechPimComponentNextCandRPAdv_Object=MibTableColumn
qtechPimComponentNextCandRPAdv=_QtechPimComponentNextCandRPAdv_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,7,1,9),_QtechPimComponentNextCandRPAdv_Type())
qtechPimComponentNextCandRPAdv.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimComponentNextCandRPAdv.setStatus(_A)
class _QtechPimSourceLifetime_Type(Integer32):defaultValue=2100
_QtechPimSourceLifetime_Type.__name__=_D
_QtechPimSourceLifetime_Object=MibScalar
qtechPimSourceLifetime=_QtechPimSourceLifetime_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,8),_QtechPimSourceLifetime_Type())
qtechPimSourceLifetime.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimSourceLifetime.setStatus(_A)
if mibBuilder.loadTexts:qtechPimSourceLifetime.setUnits(_F)
class _QtechPimStateRefreshInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_QtechPimStateRefreshInterval_Type.__name__=_D
_QtechPimStateRefreshInterval_Object=MibScalar
qtechPimStateRefreshInterval=_QtechPimStateRefreshInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,9),_QtechPimStateRefreshInterval_Type())
qtechPimStateRefreshInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimStateRefreshInterval.setStatus(_A)
if mibBuilder.loadTexts:qtechPimStateRefreshInterval.setUnits(_F)
class _QtechPimStateRefreshLimitInterval_Type(Integer32):defaultValue=0
_QtechPimStateRefreshLimitInterval_Type.__name__=_D
_QtechPimStateRefreshLimitInterval_Object=MibScalar
qtechPimStateRefreshLimitInterval=_QtechPimStateRefreshLimitInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,10),_QtechPimStateRefreshLimitInterval_Type())
qtechPimStateRefreshLimitInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimStateRefreshLimitInterval.setStatus(_A)
class _QtechPimStateRefreshTimeToLive_Type(Integer32):defaultValue=16
_QtechPimStateRefreshTimeToLive_Type.__name__=_D
_QtechPimStateRefreshTimeToLive_Object=MibScalar
qtechPimStateRefreshTimeToLive=_QtechPimStateRefreshTimeToLive_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,11),_QtechPimStateRefreshTimeToLive_Type())
qtechPimStateRefreshTimeToLive.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimStateRefreshTimeToLive.setStatus(_A)
_QtechPimBsrCandidateGroup_ObjectIdentity=ObjectIdentity
qtechPimBsrCandidateGroup=_QtechPimBsrCandidateGroup_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,12))
_QtechPimBsrCandidateIfindex_Type=Integer32
_QtechPimBsrCandidateIfindex_Object=MibScalar
qtechPimBsrCandidateIfindex=_QtechPimBsrCandidateIfindex_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,12,1),_QtechPimBsrCandidateIfindex_Type())
qtechPimBsrCandidateIfindex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimBsrCandidateIfindex.setStatus(_A)
class _QtechPimBsrCandidateHashMaskLength_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_QtechPimBsrCandidateHashMaskLength_Type.__name__=_D
_QtechPimBsrCandidateHashMaskLength_Object=MibScalar
qtechPimBsrCandidateHashMaskLength=_QtechPimBsrCandidateHashMaskLength_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,12,2),_QtechPimBsrCandidateHashMaskLength_Type())
qtechPimBsrCandidateHashMaskLength.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimBsrCandidateHashMaskLength.setStatus(_A)
class _QtechPimBsrCandidatePriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QtechPimBsrCandidatePriority_Type.__name__=_D
_QtechPimBsrCandidatePriority_Object=MibScalar
qtechPimBsrCandidatePriority=_QtechPimBsrCandidatePriority_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,12,3),_QtechPimBsrCandidatePriority_Type())
qtechPimBsrCandidatePriority.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechPimBsrCandidatePriority.setStatus(_A)
_QtechPimRPTable_Object=MibTable
qtechPimRPTable=_QtechPimRPTable_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,13))
if mibBuilder.loadTexts:qtechPimRPTable.setStatus(_A)
_QtechPimRPEntry_Object=MibTableRow
qtechPimRPEntry=_QtechPimRPEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,13,1))
qtechPimRPEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:qtechPimRPEntry.setStatus(_A)
_QtechPimRPGroupAddress_Type=IpAddress
_QtechPimRPGroupAddress_Object=MibTableColumn
qtechPimRPGroupAddress=_QtechPimRPGroupAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,13,1,1),_QtechPimRPGroupAddress_Type())
qtechPimRPGroupAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechPimRPGroupAddress.setStatus(_A)
_QtechPimRPAddress_Type=IpAddress
_QtechPimRPAddress_Object=MibTableColumn
qtechPimRPAddress=_QtechPimRPAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,13,1,2),_QtechPimRPAddress_Type())
qtechPimRPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimRPAddress.setStatus(_A)
_QtechPimRPExpiryTime_Type=TimeTicks
_QtechPimRPExpiryTime_Object=MibTableColumn
qtechPimRPExpiryTime=_QtechPimRPExpiryTime_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,13,1,3),_QtechPimRPExpiryTime_Type())
qtechPimRPExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimRPExpiryTime.setStatus(_A)
_QtechPimRPNextRPReachableIn_Type=TimeTicks
_QtechPimRPNextRPReachableIn_Object=MibTableColumn
qtechPimRPNextRPReachableIn=_QtechPimRPNextRPReachableIn_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,13,1,4),_QtechPimRPNextRPReachableIn_Type())
qtechPimRPNextRPReachableIn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPimRPNextRPReachableIn.setStatus(_A)
_QtechPimStaticRPTable_Object=MibTable
qtechPimStaticRPTable=_QtechPimStaticRPTable_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,14))
if mibBuilder.loadTexts:qtechPimStaticRPTable.setStatus(_A)
_QtechPimStaticRPEntry_Object=MibTableRow
qtechPimStaticRPEntry=_QtechPimStaticRPEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,14,1))
qtechPimStaticRPEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:qtechPimStaticRPEntry.setStatus(_A)
_QtechPimStaticRPAddress_Type=IpAddress
_QtechPimStaticRPAddress_Object=MibTableColumn
qtechPimStaticRPAddress=_QtechPimStaticRPAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,14,1,1),_QtechPimStaticRPAddress_Type())
qtechPimStaticRPAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechPimStaticRPAddress.setStatus(_A)
class _QtechPimStaticRPAddressIsOverride_Type(EnabledStatus):defaultValue=2
_QtechPimStaticRPAddressIsOverride_Type.__name__=_K
_QtechPimStaticRPAddressIsOverride_Object=MibTableColumn
qtechPimStaticRPAddressIsOverride=_QtechPimStaticRPAddressIsOverride_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,14,1,2),_QtechPimStaticRPAddressIsOverride_Type())
qtechPimStaticRPAddressIsOverride.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechPimStaticRPAddressIsOverride.setStatus(_A)
class _QtechPimStaticRPAclName_Type(DisplayString):defaultValue=OctetString('')
_QtechPimStaticRPAclName_Type.__name__=_J
_QtechPimStaticRPAclName_Object=MibTableColumn
qtechPimStaticRPAclName=_QtechPimStaticRPAclName_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,14,1,3),_QtechPimStaticRPAclName_Type())
qtechPimStaticRPAclName.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechPimStaticRPAclName.setStatus(_A)
_QtechPimStaticRPStatus_Type=RowStatus
_QtechPimStaticRPStatus_Object=MibTableColumn
qtechPimStaticRPStatus=_QtechPimStaticRPStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,14,1,4),_QtechPimStaticRPStatus_Type())
qtechPimStaticRPStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechPimStaticRPStatus.setStatus(_A)
_QtechPimRpCandidateTable_Object=MibTable
qtechPimRpCandidateTable=_QtechPimRpCandidateTable_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,15))
if mibBuilder.loadTexts:qtechPimRpCandidateTable.setStatus(_A)
_QtechPimRpCandidateEntry_Object=MibTableRow
qtechPimRpCandidateEntry=_QtechPimRpCandidateEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,15,1))
qtechPimRpCandidateEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:qtechPimRpCandidateEntry.setStatus(_A)
_QtechPimRpCandidateIfindex_Type=InterfaceIndex
_QtechPimRpCandidateIfindex_Object=MibTableColumn
qtechPimRpCandidateIfindex=_QtechPimRpCandidateIfindex_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,15,1,1),_QtechPimRpCandidateIfindex_Type())
qtechPimRpCandidateIfindex.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechPimRpCandidateIfindex.setStatus(_A)
class _QtechPimRpCandidateAclName_Type(DisplayString):defaultValue=OctetString('')
_QtechPimRpCandidateAclName_Type.__name__=_J
_QtechPimRpCandidateAclName_Object=MibTableColumn
qtechPimRpCandidateAclName=_QtechPimRpCandidateAclName_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,15,1,2),_QtechPimRpCandidateAclName_Type())
qtechPimRpCandidateAclName.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechPimRpCandidateAclName.setStatus(_A)
_QtechPimRpCandidateStatus_Type=RowStatus
_QtechPimRpCandidateStatus_Object=MibTableColumn
qtechPimRpCandidateStatus=_QtechPimRpCandidateStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,27,1,1,15,1,3),_QtechPimRpCandidateStatus_Type())
qtechPimRpCandidateStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechPimRpCandidateStatus.setStatus(_A)
_QtechPimTraps_ObjectIdentity=ObjectIdentity
qtechPimTraps=_QtechPimTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,27,1,2))
_QtechPimMIBConformance_ObjectIdentity=ObjectIdentity
qtechPimMIBConformance=_QtechPimMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,27,2))
_QtechPimMIBCompliances_ObjectIdentity=ObjectIdentity
qtechPimMIBCompliances=_QtechPimMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,27,2,1))
_QtechPimMIBGroups_ObjectIdentity=ObjectIdentity
qtechPimMIBGroups=_QtechPimMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,27,2,2))
qtechPimMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,27,2,2,1))
qtechPimMIBGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_L),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As)))
if mibBuilder.loadTexts:qtechPimMIBGroup.setStatus(_A)
qtechPimNeighborLoss=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,27,1,2,1))
qtechPimNeighborLoss.setObjects((_B,_L))
if mibBuilder.loadTexts:qtechPimNeighborLoss.setStatus(_A)
qtechPimNotifyGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,27,2,2,2))
qtechPimNotifyGroup.setObjects((_B,_At))
if mibBuilder.loadTexts:qtechPimNotifyGroup.setStatus(_A)
qtechPimMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,27,2,1,1))
qtechPimMIBCompliance.setObjects((_B,_Au))
if mibBuilder.loadTexts:qtechPimMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechPimMIB':qtechPimMIB,'qtechPimMIBObjects':qtechPimMIBObjects,'qtechPim':qtechPim,_f:qtechPimJoinPruneInterval,'qtechPimInterfaceTable':qtechPimInterfaceTable,'qtechPimInterfaceEntry':qtechPimInterfaceEntry,_U:qtechPimInterfaceIfIndex,_g:qtechPimInterfaceAddress,_h:qtechPimInterfaceNetMask,_i:qtechPimInterfaceMode,_j:qtechPimInterfaceDR,_k:qtechPimInterfaceHelloInterval,_l:qtechPimInterfaceJoinPruneInterval,_m:qtechPimInterfaceCBSRPreference,_n:qtechPimInterfaceTrigHelloInterval,_o:qtechPimInterfaceHelloHoldtime,_p:qtechPimInterfaceLanPruneDelay,_q:qtechPimInterfacePropagationDelay,_r:qtechPimInterfaceOverrideInterval,_s:qtechPimInterfaceGenerationID,_t:qtechPimInterfaceJoinPruneHoldtime,_u:qtechPimInterfaceGraftRetryInterval,_v:qtechPimInterfaceMaxGraftRetries,_w:qtechPimInterfaceSRTTLThreshold,_x:qtechPimInterfaceLanDelayEnabled,_y:qtechPimInterfaceSRCapable,_z:qtechPimInterfaceDRPriority,_A0:qtechPimInterfaceNbrCounter,_A1:qtechPimInterfaceBsrBorderEnabled,_A2:qtechPimInterfaceCountIn,_A3:qtechPimInterfaceCountOut,_A4:qtechPimInterfaceEnabled,_A5:qtechPimNeighborFilterAcl,_A6:qtechPimDrSupportAddressBound,'qtechPimNeighborTable':qtechPimNeighborTable,'qtechPimNeighborEntry':qtechPimNeighborEntry,_W:qtechPimNeighborAddress,_L:qtechPimNeighborIfIndex,_A7:qtechPimNeighborUpTime,_A8:qtechPimNeighborExpiryTime,_A9:qtechPimNeighborMode,_AA:qtechPimNeighborLanPruneDelay,_AB:qtechPimNeighborOverrideInterval,_AC:qtechPimNeighborTBit,_AD:qtechPimNeighborSRCapable,_AE:qtechPimNeighborDRPresent,'qtechPimIpMRouteTable':qtechPimIpMRouteTable,'qtechPimIpMRouteEntry':qtechPimIpMRouteEntry,_AF:qtechPimIpMRouteUpstreamAssertTimer,_AG:qtechPimIpMRouteAssertMetric,_AH:qtechPimIpMRouteAssertMetricPref,_AI:qtechPimIpMRouteAssertRPTBit,_AJ:qtechPimIpMRouteFlags,_AK:qtechPimIpMRouteRPFNeighbor,_AL:qtechPimIpMRouteSourceTimer,_AM:qtechPimIpMRouteOriginatorSRTTL,'qtechPimIpMRouteNextHopTable':qtechPimIpMRouteNextHopTable,'qtechPimIpMRouteNextHopEntry':qtechPimIpMRouteNextHopEntry,_AN:qtechPimIpMRouteNextHopPruneReason,_AO:qtechPimIpMRouteNextHopAssertWinner,_AP:qtechPimIpMRouteNextHopAssertTimer,_AQ:qtechPimIpMRouteNextHopAssertMetric,_AR:qtechPimIpMRouteNextHopAssertMetricPref,_AS:qtechPimIpMRouteNextHopJoinPruneTimer,'qtechPimRPSetTable':qtechPimRPSetTable,'qtechPimRPSetEntry':qtechPimRPSetEntry,_Y:qtechPimRPSetGroupAddress,_Z:qtechPimRPSetGroupMask,_a:qtechPimRPSetAddress,_AT:qtechPimRPSetHoldTime,_AU:qtechPimRPSetExpiryTime,_X:qtechPimRPSetComponent,_AV:qtechPimRPSetUpTime,'qtechPimComponentTable':qtechPimComponentTable,'qtechPimComponentEntry':qtechPimComponentEntry,_b:qtechPimComponentIndex,_AW:qtechPimComponentBSRAddress,_AX:qtechPimComponentBSRExpiryTime,_AY:qtechPimComponentCRPHoldTime,_AZ:qtechPimComponentBSRUptime,_Aa:qtechPimComponentBSRPriority,_Ab:qtechPimComponentBSRHashMaskLength,_Ac:qtechPimComponentBSRNextBsrMessage,_Ad:qtechPimComponentNextCandRPAdv,_Ae:qtechPimSourceLifetime,_Af:qtechPimStateRefreshInterval,_Ag:qtechPimStateRefreshLimitInterval,_Ah:qtechPimStateRefreshTimeToLive,'qtechPimBsrCandidateGroup':qtechPimBsrCandidateGroup,_Ai:qtechPimBsrCandidateIfindex,_Aj:qtechPimBsrCandidateHashMaskLength,_Ak:qtechPimBsrCandidatePriority,'qtechPimRPTable':qtechPimRPTable,'qtechPimRPEntry':qtechPimRPEntry,_c:qtechPimRPGroupAddress,_Al:qtechPimRPAddress,_Am:qtechPimRPExpiryTime,_An:qtechPimRPNextRPReachableIn,'qtechPimStaticRPTable':qtechPimStaticRPTable,'qtechPimStaticRPEntry':qtechPimStaticRPEntry,_d:qtechPimStaticRPAddress,_Ao:qtechPimStaticRPAddressIsOverride,_Ap:qtechPimStaticRPAclName,_Aq:qtechPimStaticRPStatus,'qtechPimRpCandidateTable':qtechPimRpCandidateTable,'qtechPimRpCandidateEntry':qtechPimRpCandidateEntry,_e:qtechPimRpCandidateIfindex,_Ar:qtechPimRpCandidateAclName,_As:qtechPimRpCandidateStatus,'qtechPimTraps':qtechPimTraps,_At:qtechPimNeighborLoss,'qtechPimMIBConformance':qtechPimMIBConformance,'qtechPimMIBCompliances':qtechPimMIBCompliances,'qtechPimMIBCompliance':qtechPimMIBCompliance,'qtechPimMIBGroups':qtechPimMIBGroups,_Au:qtechPimMIBGroup,'qtechPimNotifyGroup':qtechPimNotifyGroup})