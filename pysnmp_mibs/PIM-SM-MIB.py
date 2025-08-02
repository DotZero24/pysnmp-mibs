_b='swPimRPSetAddress'
_a='swPimRPSetGroupMask'
_Z='swPimRPSetGroupAddress'
_Y='swPimRPSetComponent'
_X='swPimIpMRouteSourceMask'
_W='swPimIpMRouteSource'
_V='swPimIpMRouteGroup'
_U='swPimStaticRPAddress'
_T='swPimStaticRPGroupMask'
_S='swPimStaticRPGroupAddress'
_R='swL3SwPimRegChksumIncDataRpAddr'
_Q='swPimNeighborAddress'
_P='swPimCandidateRPGroupMask'
_O='swPimCandidateRPGroupAddress'
_N='swPimCbsrInterface'
_M='seconds'
_L='swPimInfoInterface'
_K='DisplayString'
_J='Unsigned32'
_I='read-create'
_H='enabled'
_G='disabled'
_F='not-accessible'
_E='PIM-SM-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
swPimSmMIB=ModuleIdentity((1,3,6,1,4,1,171,12,52))
_SwPimSmCtrl_ObjectIdentity=ObjectIdentity
swPimSmCtrl=_SwPimSmCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,52,1))
class _SwPimSmGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('other',0),(_G,1),(_H,2)))
_SwPimSmGlobalState_Type.__name__=_B
_SwPimSmGlobalState_Object=MibScalar
swPimSmGlobalState=_SwPimSmGlobalState_Object((1,3,6,1,4,1,171,12,52,1,1),_SwPimSmGlobalState_Type())
swPimSmGlobalState.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimSmGlobalState.setStatus(_A)
_SwPimSmInfo_ObjectIdentity=ObjectIdentity
swPimSmInfo=_SwPimSmInfo_ObjectIdentity((1,3,6,1,4,1,171,12,52,2))
class _SwPimRegisterProbeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_SwPimRegisterProbeTime_Type.__name__=_B
_SwPimRegisterProbeTime_Object=MibScalar
swPimRegisterProbeTime=_SwPimRegisterProbeTime_Object((1,3,6,1,4,1,171,12,52,2,1),_SwPimRegisterProbeTime_Type())
swPimRegisterProbeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimRegisterProbeTime.setStatus(_A)
class _SwPimRegisterSuppressionTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,255))
_SwPimRegisterSuppressionTime_Type.__name__=_B
_SwPimRegisterSuppressionTime_Object=MibScalar
swPimRegisterSuppressionTime=_SwPimRegisterSuppressionTime_Object((1,3,6,1,4,1,171,12,52,2,2),_SwPimRegisterSuppressionTime_Type())
swPimRegisterSuppressionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimRegisterSuppressionTime.setStatus(_A)
_SwPimInfoTable_Object=MibTable
swPimInfoTable=_SwPimInfoTable_Object((1,3,6,1,4,1,171,12,52,2,3))
if mibBuilder.loadTexts:swPimInfoTable.setStatus(_A)
_SwPimInfoEntry_Object=MibTableRow
swPimInfoEntry=_SwPimInfoEntry_Object((1,3,6,1,4,1,171,12,52,2,3,1))
swPimInfoEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:swPimInfoEntry.setStatus(_A)
_SwPimInfoInterface_Type=InterfaceIndex
_SwPimInfoInterface_Object=MibTableColumn
swPimInfoInterface=_SwPimInfoInterface_Object((1,3,6,1,4,1,171,12,52,2,3,1,1),_SwPimInfoInterface_Type())
swPimInfoInterface.setMaxAccess(_F)
if mibBuilder.loadTexts:swPimInfoInterface.setStatus(_A)
_SwPimInfoAddress_Type=IpAddress
_SwPimInfoAddress_Object=MibTableColumn
swPimInfoAddress=_SwPimInfoAddress_Object((1,3,6,1,4,1,171,12,52,2,3,1,2),_SwPimInfoAddress_Type())
swPimInfoAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimInfoAddress.setStatus(_A)
_SwPimInfoNetMask_Type=IpAddress
_SwPimInfoNetMask_Object=MibTableColumn
swPimInfoNetMask=_SwPimInfoNetMask_Object((1,3,6,1,4,1,171,12,52,2,3,1,3),_SwPimInfoNetMask_Type())
swPimInfoNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimInfoNetMask.setStatus(_A)
_SwPimInfoDesignatedRouter_Type=IpAddress
_SwPimInfoDesignatedRouter_Object=MibTableColumn
swPimInfoDesignatedRouter=_SwPimInfoDesignatedRouter_Object((1,3,6,1,4,1,171,12,52,2,3,1,4),_SwPimInfoDesignatedRouter_Type())
swPimInfoDesignatedRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimInfoDesignatedRouter.setStatus(_A)
class _SwPimInfoHelloInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18724))
_SwPimInfoHelloInterval_Type.__name__=_B
_SwPimInfoHelloInterval_Object=MibTableColumn
swPimInfoHelloInterval=_SwPimInfoHelloInterval_Object((1,3,6,1,4,1,171,12,52,2,3,1,5),_SwPimInfoHelloInterval_Type())
swPimInfoHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimInfoHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:swPimInfoHelloInterval.setUnits(_M)
class _SwPimInfoJoinPruneInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18724))
_SwPimInfoJoinPruneInterval_Type.__name__=_B
_SwPimInfoJoinPruneInterval_Object=MibTableColumn
swPimInfoJoinPruneInterval=_SwPimInfoJoinPruneInterval_Object((1,3,6,1,4,1,171,12,52,2,3,1,6),_SwPimInfoJoinPruneInterval_Type())
swPimInfoJoinPruneInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimInfoJoinPruneInterval.setStatus(_A)
if mibBuilder.loadTexts:swPimInfoJoinPruneInterval.setUnits(_M)
class _SwPimInfoDRPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_SwPimInfoDRPriority_Type.__name__=_J
_SwPimInfoDRPriority_Object=MibTableColumn
swPimInfoDRPriority=_SwPimInfoDRPriority_Object((1,3,6,1,4,1,171,12,52,2,3,1,7),_SwPimInfoDRPriority_Type())
swPimInfoDRPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimInfoDRPriority.setStatus(_A)
class _SwPimInfoMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dense',1),('sparse',2),('sparseDense',3)))
_SwPimInfoMode_Type.__name__=_B
_SwPimInfoMode_Object=MibTableColumn
swPimInfoMode=_SwPimInfoMode_Object((1,3,6,1,4,1,171,12,52,2,3,1,8),_SwPimInfoMode_Type())
swPimInfoMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimInfoMode.setStatus(_A)
class _SwPimInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwPimInfoState_Type.__name__=_B
_SwPimInfoState_Object=MibTableColumn
swPimInfoState=_SwPimInfoState_Object((1,3,6,1,4,1,171,12,52,2,3,1,9),_SwPimInfoState_Type())
swPimInfoState.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimInfoState.setStatus(_A)
class _SwPimInfoPassiveMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwPimInfoPassiveMode_Type.__name__=_B
_SwPimInfoPassiveMode_Object=MibTableColumn
swPimInfoPassiveMode=_SwPimInfoPassiveMode_Object((1,3,6,1,4,1,171,12,52,2,3,1,10),_SwPimInfoPassiveMode_Type())
swPimInfoPassiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimInfoPassiveMode.setStatus(_A)
_SwPimSmMgmt_ObjectIdentity=ObjectIdentity
swPimSmMgmt=_SwPimSmMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,52,3))
_SwPimCbsrInfoMgmt_ObjectIdentity=ObjectIdentity
swPimCbsrInfoMgmt=_SwPimCbsrInfoMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,52,3,1))
class _SwpimCbsrBootStrapPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwpimCbsrBootStrapPeriod_Type.__name__=_B
_SwpimCbsrBootStrapPeriod_Object=MibScalar
swpimCbsrBootStrapPeriod=_SwpimCbsrBootStrapPeriod_Object((1,3,6,1,4,1,171,12,52,3,1,1),_SwpimCbsrBootStrapPeriod_Type())
swpimCbsrBootStrapPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:swpimCbsrBootStrapPeriod.setStatus(_A)
class _SwPimCbsrHashMaskLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_SwPimCbsrHashMaskLen_Type.__name__=_B
_SwPimCbsrHashMaskLen_Object=MibScalar
swPimCbsrHashMaskLen=_SwPimCbsrHashMaskLen_Object((1,3,6,1,4,1,171,12,52,3,1,2),_SwPimCbsrHashMaskLen_Type())
swPimCbsrHashMaskLen.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimCbsrHashMaskLen.setStatus(_A)
_SwPimCbsrTable_Object=MibTable
swPimCbsrTable=_SwPimCbsrTable_Object((1,3,6,1,4,1,171,12,52,3,1,3))
if mibBuilder.loadTexts:swPimCbsrTable.setStatus(_A)
_SwPimCbsrEntry_Object=MibTableRow
swPimCbsrEntry=_SwPimCbsrEntry_Object((1,3,6,1,4,1,171,12,52,3,1,3,1))
swPimCbsrEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:swPimCbsrEntry.setStatus(_A)
_SwPimCbsrInterface_Type=InterfaceIndex
_SwPimCbsrInterface_Object=MibTableColumn
swPimCbsrInterface=_SwPimCbsrInterface_Object((1,3,6,1,4,1,171,12,52,3,1,3,1,1),_SwPimCbsrInterface_Type())
swPimCbsrInterface.setMaxAccess(_F)
if mibBuilder.loadTexts:swPimCbsrInterface.setStatus(_A)
_SwPimCbsrIpAddress_Type=IpAddress
_SwPimCbsrIpAddress_Object=MibTableColumn
swPimCbsrIpAddress=_SwPimCbsrIpAddress_Object((1,3,6,1,4,1,171,12,52,3,1,3,1,2),_SwPimCbsrIpAddress_Type())
swPimCbsrIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimCbsrIpAddress.setStatus(_A)
_SwPimCbsrSubnetMask_Type=IpAddress
_SwPimCbsrSubnetMask_Object=MibTableColumn
swPimCbsrSubnetMask=_SwPimCbsrSubnetMask_Object((1,3,6,1,4,1,171,12,52,3,1,3,1,3),_SwPimCbsrSubnetMask_Type())
swPimCbsrSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimCbsrSubnetMask.setStatus(_A)
class _SwPimCbsrPriority_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_SwPimCbsrPriority_Type.__name__=_B
_SwPimCbsrPriority_Object=MibTableColumn
swPimCbsrPriority=_SwPimCbsrPriority_Object((1,3,6,1,4,1,171,12,52,3,1,3,1,4),_SwPimCbsrPriority_Type())
swPimCbsrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimCbsrPriority.setStatus(_A)
_SwPimCandidateRPMgmt_ObjectIdentity=ObjectIdentity
swPimCandidateRPMgmt=_SwPimCandidateRPMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,52,3,2))
class _SwPimCandidateRPHoldtime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwPimCandidateRPHoldtime_Type.__name__=_B
_SwPimCandidateRPHoldtime_Object=MibScalar
swPimCandidateRPHoldtime=_SwPimCandidateRPHoldtime_Object((1,3,6,1,4,1,171,12,52,3,2,1),_SwPimCandidateRPHoldtime_Type())
swPimCandidateRPHoldtime.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimCandidateRPHoldtime.setStatus(_A)
class _SwPimCandidateRPPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwPimCandidateRPPriority_Type.__name__=_B
_SwPimCandidateRPPriority_Object=MibScalar
swPimCandidateRPPriority=_SwPimCandidateRPPriority_Object((1,3,6,1,4,1,171,12,52,3,2,2),_SwPimCandidateRPPriority_Type())
swPimCandidateRPPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimCandidateRPPriority.setStatus(_A)
class _SwPimCandidateRPWildcardPrefixCnt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_SwPimCandidateRPWildcardPrefixCnt_Type.__name__=_B
_SwPimCandidateRPWildcardPrefixCnt_Object=MibScalar
swPimCandidateRPWildcardPrefixCnt=_SwPimCandidateRPWildcardPrefixCnt_Object((1,3,6,1,4,1,171,12,52,3,2,3),_SwPimCandidateRPWildcardPrefixCnt_Type())
swPimCandidateRPWildcardPrefixCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimCandidateRPWildcardPrefixCnt.setStatus(_A)
_SwPimCandidateRPTable_Object=MibTable
swPimCandidateRPTable=_SwPimCandidateRPTable_Object((1,3,6,1,4,1,171,12,52,3,2,4))
if mibBuilder.loadTexts:swPimCandidateRPTable.setStatus(_A)
_SwPimCandidateRPEntry_Object=MibTableRow
swPimCandidateRPEntry=_SwPimCandidateRPEntry_Object((1,3,6,1,4,1,171,12,52,3,2,4,1))
swPimCandidateRPEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:swPimCandidateRPEntry.setStatus(_A)
_SwPimCandidateRPGroupAddress_Type=IpAddress
_SwPimCandidateRPGroupAddress_Object=MibTableColumn
swPimCandidateRPGroupAddress=_SwPimCandidateRPGroupAddress_Object((1,3,6,1,4,1,171,12,52,3,2,4,1,1),_SwPimCandidateRPGroupAddress_Type())
swPimCandidateRPGroupAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:swPimCandidateRPGroupAddress.setStatus(_A)
_SwPimCandidateRPGroupMask_Type=IpAddress
_SwPimCandidateRPGroupMask_Object=MibTableColumn
swPimCandidateRPGroupMask=_SwPimCandidateRPGroupMask_Object((1,3,6,1,4,1,171,12,52,3,2,4,1,2),_SwPimCandidateRPGroupMask_Type())
swPimCandidateRPGroupMask.setMaxAccess(_F)
if mibBuilder.loadTexts:swPimCandidateRPGroupMask.setStatus(_A)
class _SwPimCandidateRPInterface_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwPimCandidateRPInterface_Type.__name__=_K
_SwPimCandidateRPInterface_Object=MibTableColumn
swPimCandidateRPInterface=_SwPimCandidateRPInterface_Object((1,3,6,1,4,1,171,12,52,3,2,4,1,3),_SwPimCandidateRPInterface_Type())
swPimCandidateRPInterface.setMaxAccess(_I)
if mibBuilder.loadTexts:swPimCandidateRPInterface.setStatus(_A)
_SwPimCandidateRPRowStatus_Type=RowStatus
_SwPimCandidateRPRowStatus_Object=MibTableColumn
swPimCandidateRPRowStatus=_SwPimCandidateRPRowStatus_Object((1,3,6,1,4,1,171,12,52,3,2,4,1,4),_SwPimCandidateRPRowStatus_Type())
swPimCandidateRPRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swPimCandidateRPRowStatus.setStatus(_A)
_SwPimNeighborTable_Object=MibTable
swPimNeighborTable=_SwPimNeighborTable_Object((1,3,6,1,4,1,171,12,52,3,3))
if mibBuilder.loadTexts:swPimNeighborTable.setStatus(_A)
_SwPimNeighborEntry_Object=MibTableRow
swPimNeighborEntry=_SwPimNeighborEntry_Object((1,3,6,1,4,1,171,12,52,3,3,1))
swPimNeighborEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:swPimNeighborEntry.setStatus(_A)
_SwPimNeighborAddress_Type=IpAddress
_SwPimNeighborAddress_Object=MibTableColumn
swPimNeighborAddress=_SwPimNeighborAddress_Object((1,3,6,1,4,1,171,12,52,3,3,1,1),_SwPimNeighborAddress_Type())
swPimNeighborAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:swPimNeighborAddress.setStatus(_A)
_SwPimNeighborIfIndex_Type=InterfaceIndex
_SwPimNeighborIfIndex_Object=MibTableColumn
swPimNeighborIfIndex=_SwPimNeighborIfIndex_Object((1,3,6,1,4,1,171,12,52,3,3,1,2),_SwPimNeighborIfIndex_Type())
swPimNeighborIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimNeighborIfIndex.setStatus(_A)
_SwPimNeighborExpiryTime_Type=TimeTicks
_SwPimNeighborExpiryTime_Object=MibTableColumn
swPimNeighborExpiryTime=_SwPimNeighborExpiryTime_Object((1,3,6,1,4,1,171,12,52,3,3,1,3),_SwPimNeighborExpiryTime_Type())
swPimNeighborExpiryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimNeighborExpiryTime.setStatus(_A)
_SwPimSptMgmt_ObjectIdentity=ObjectIdentity
swPimSptMgmt=_SwPimSptMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,52,3,4))
class _SwPimLastHopSptThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_SwPimLastHopSptThreshold_Type.__name__=_B
_SwPimLastHopSptThreshold_Object=MibScalar
swPimLastHopSptThreshold=_SwPimLastHopSptThreshold_Object((1,3,6,1,4,1,171,12,52,3,4,1),_SwPimLastHopSptThreshold_Type())
swPimLastHopSptThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimLastHopSptThreshold.setStatus(_A)
class _SwPimRPSptThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_SwPimRPSptThreshold_Type.__name__=_B
_SwPimRPSptThreshold_Object=MibScalar
swPimRPSptThreshold=_SwPimRPSptThreshold_Object((1,3,6,1,4,1,171,12,52,3,4,2),_SwPimRPSptThreshold_Type())
swPimRPSptThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimRPSptThreshold.setStatus(_A)
class _SwPimLastHopSptSwitchover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('never',1),('immediately',2)))
_SwPimLastHopSptSwitchover_Type.__name__=_B
_SwPimLastHopSptSwitchover_Object=MibScalar
swPimLastHopSptSwitchover=_SwPimLastHopSptSwitchover_Object((1,3,6,1,4,1,171,12,52,3,4,3),_SwPimLastHopSptSwitchover_Type())
swPimLastHopSptSwitchover.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimLastHopSptSwitchover.setStatus(_A)
_SwPimRegChksumIncDataTable_Object=MibTable
swPimRegChksumIncDataTable=_SwPimRegChksumIncDataTable_Object((1,3,6,1,4,1,171,12,52,3,5))
if mibBuilder.loadTexts:swPimRegChksumIncDataTable.setStatus(_A)
_SwPimRegChksumIncDataEntry_Object=MibTableRow
swPimRegChksumIncDataEntry=_SwPimRegChksumIncDataEntry_Object((1,3,6,1,4,1,171,12,52,3,5,1))
swPimRegChksumIncDataEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:swPimRegChksumIncDataEntry.setStatus(_A)
_SwL3SwPimRegChksumIncDataRpAddr_Type=IpAddress
_SwL3SwPimRegChksumIncDataRpAddr_Object=MibTableColumn
swL3SwPimRegChksumIncDataRpAddr=_SwL3SwPimRegChksumIncDataRpAddr_Object((1,3,6,1,4,1,171,12,52,3,5,1,1),_SwL3SwPimRegChksumIncDataRpAddr_Type())
swL3SwPimRegChksumIncDataRpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:swL3SwPimRegChksumIncDataRpAddr.setStatus(_A)
_SwL3SwPimRegChksumIncDataState_Type=RowStatus
_SwL3SwPimRegChksumIncDataState_Object=MibTableColumn
swL3SwPimRegChksumIncDataState=_SwL3SwPimRegChksumIncDataState_Object((1,3,6,1,4,1,171,12,52,3,5,1,2),_SwL3SwPimRegChksumIncDataState_Type())
swL3SwPimRegChksumIncDataState.setMaxAccess(_I)
if mibBuilder.loadTexts:swL3SwPimRegChksumIncDataState.setStatus(_A)
_SwPimStaticRPTable_Object=MibTable
swPimStaticRPTable=_SwPimStaticRPTable_Object((1,3,6,1,4,1,171,12,52,3,6))
if mibBuilder.loadTexts:swPimStaticRPTable.setStatus(_A)
_SwPimStaticRPEntry_Object=MibTableRow
swPimStaticRPEntry=_SwPimStaticRPEntry_Object((1,3,6,1,4,1,171,12,52,3,6,1))
swPimStaticRPEntry.setIndexNames((0,_E,_S),(0,_E,_T),(0,_E,_U))
if mibBuilder.loadTexts:swPimStaticRPEntry.setStatus(_A)
_SwPimStaticRPGroupAddress_Type=IpAddress
_SwPimStaticRPGroupAddress_Object=MibTableColumn
swPimStaticRPGroupAddress=_SwPimStaticRPGroupAddress_Object((1,3,6,1,4,1,171,12,52,3,6,1,1),_SwPimStaticRPGroupAddress_Type())
swPimStaticRPGroupAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:swPimStaticRPGroupAddress.setStatus(_A)
_SwPimStaticRPGroupMask_Type=IpAddress
_SwPimStaticRPGroupMask_Object=MibTableColumn
swPimStaticRPGroupMask=_SwPimStaticRPGroupMask_Object((1,3,6,1,4,1,171,12,52,3,6,1,2),_SwPimStaticRPGroupMask_Type())
swPimStaticRPGroupMask.setMaxAccess(_F)
if mibBuilder.loadTexts:swPimStaticRPGroupMask.setStatus(_A)
_SwPimStaticRPAddress_Type=IpAddress
_SwPimStaticRPAddress_Object=MibTableColumn
swPimStaticRPAddress=_SwPimStaticRPAddress_Object((1,3,6,1,4,1,171,12,52,3,6,1,3),_SwPimStaticRPAddress_Type())
swPimStaticRPAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:swPimStaticRPAddress.setStatus(_A)
_SwPimStaticRPRowStatus_Type=RowStatus
_SwPimStaticRPRowStatus_Object=MibTableColumn
swPimStaticRPRowStatus=_SwPimStaticRPRowStatus_Object((1,3,6,1,4,1,171,12,52,3,6,1,4),_SwPimStaticRPRowStatus_Type())
swPimStaticRPRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swPimStaticRPRowStatus.setStatus(_A)
_SwPimIpMRouteTable_Object=MibTable
swPimIpMRouteTable=_SwPimIpMRouteTable_Object((1,3,6,1,4,1,171,12,52,3,7))
if mibBuilder.loadTexts:swPimIpMRouteTable.setStatus(_A)
_SwPimIpMRouteEntry_Object=MibTableRow
swPimIpMRouteEntry=_SwPimIpMRouteEntry_Object((1,3,6,1,4,1,171,12,52,3,7,1))
swPimIpMRouteEntry.setIndexNames((0,_E,_V),(0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:swPimIpMRouteEntry.setStatus(_A)
_SwPimIpMRouteGroup_Type=IpAddress
_SwPimIpMRouteGroup_Object=MibTableColumn
swPimIpMRouteGroup=_SwPimIpMRouteGroup_Object((1,3,6,1,4,1,171,12,52,3,7,1,1),_SwPimIpMRouteGroup_Type())
swPimIpMRouteGroup.setMaxAccess(_F)
if mibBuilder.loadTexts:swPimIpMRouteGroup.setStatus(_A)
_SwPimIpMRouteSource_Type=IpAddress
_SwPimIpMRouteSource_Object=MibTableColumn
swPimIpMRouteSource=_SwPimIpMRouteSource_Object((1,3,6,1,4,1,171,12,52,3,7,1,2),_SwPimIpMRouteSource_Type())
swPimIpMRouteSource.setMaxAccess(_F)
if mibBuilder.loadTexts:swPimIpMRouteSource.setStatus(_A)
_SwPimIpMRouteSourceMask_Type=IpAddress
_SwPimIpMRouteSourceMask_Object=MibTableColumn
swPimIpMRouteSourceMask=_SwPimIpMRouteSourceMask_Object((1,3,6,1,4,1,171,12,52,3,7,1,3),_SwPimIpMRouteSourceMask_Type())
swPimIpMRouteSourceMask.setMaxAccess(_F)
if mibBuilder.loadTexts:swPimIpMRouteSourceMask.setStatus(_A)
_SwPimIpMRouteUpstreamAssertTimer_Type=TimeTicks
_SwPimIpMRouteUpstreamAssertTimer_Object=MibTableColumn
swPimIpMRouteUpstreamAssertTimer=_SwPimIpMRouteUpstreamAssertTimer_Object((1,3,6,1,4,1,171,12,52,3,7,1,4),_SwPimIpMRouteUpstreamAssertTimer_Type())
swPimIpMRouteUpstreamAssertTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimIpMRouteUpstreamAssertTimer.setStatus(_A)
_SwPimIpMRouteAssertMetric_Type=Integer32
_SwPimIpMRouteAssertMetric_Object=MibTableColumn
swPimIpMRouteAssertMetric=_SwPimIpMRouteAssertMetric_Object((1,3,6,1,4,1,171,12,52,3,7,1,5),_SwPimIpMRouteAssertMetric_Type())
swPimIpMRouteAssertMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimIpMRouteAssertMetric.setStatus(_A)
_SwPimIpMRouteAssertMetricPref_Type=Integer32
_SwPimIpMRouteAssertMetricPref_Object=MibTableColumn
swPimIpMRouteAssertMetricPref=_SwPimIpMRouteAssertMetricPref_Object((1,3,6,1,4,1,171,12,52,3,7,1,6),_SwPimIpMRouteAssertMetricPref_Type())
swPimIpMRouteAssertMetricPref.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimIpMRouteAssertMetricPref.setStatus(_A)
_SwPimIpMRouteAssertRPTBit_Type=TruthValue
_SwPimIpMRouteAssertRPTBit_Object=MibTableColumn
swPimIpMRouteAssertRPTBit=_SwPimIpMRouteAssertRPTBit_Object((1,3,6,1,4,1,171,12,52,3,7,1,7),_SwPimIpMRouteAssertRPTBit_Type())
swPimIpMRouteAssertRPTBit.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimIpMRouteAssertRPTBit.setStatus(_A)
class _SwPimIpMRouteFlags_Type(Bits):namedValues=NamedValues(*(('rpt',0),('spt',1)))
_SwPimIpMRouteFlags_Type.__name__='Bits'
_SwPimIpMRouteFlags_Object=MibTableColumn
swPimIpMRouteFlags=_SwPimIpMRouteFlags_Object((1,3,6,1,4,1,171,12,52,3,7,1,8),_SwPimIpMRouteFlags_Type())
swPimIpMRouteFlags.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimIpMRouteFlags.setStatus(_A)
_SwPimIpMRouteType_Type=DisplayString
_SwPimIpMRouteType_Object=MibTableColumn
swPimIpMRouteType=_SwPimIpMRouteType_Object((1,3,6,1,4,1,171,12,52,3,7,1,9),_SwPimIpMRouteType_Type())
swPimIpMRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimIpMRouteType.setStatus(_A)
_SwPimRPSetMgmt_ObjectIdentity=ObjectIdentity
swPimRPSetMgmt=_SwPimRPSetMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,52,3,8))
_SwPimRPSetBootstrapRouter_Type=IpAddress
_SwPimRPSetBootstrapRouter_Object=MibScalar
swPimRPSetBootstrapRouter=_SwPimRPSetBootstrapRouter_Object((1,3,6,1,4,1,171,12,52,3,8,1),_SwPimRPSetBootstrapRouter_Type())
swPimRPSetBootstrapRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimRPSetBootstrapRouter.setStatus(_A)
_SwPimRPSetTable_Object=MibTable
swPimRPSetTable=_SwPimRPSetTable_Object((1,3,6,1,4,1,171,12,52,3,8,2))
if mibBuilder.loadTexts:swPimRPSetTable.setStatus(_A)
_SwPimRPSetEntry_Object=MibTableRow
swPimRPSetEntry=_SwPimRPSetEntry_Object((1,3,6,1,4,1,171,12,52,3,8,2,1))
swPimRPSetEntry.setIndexNames((0,_E,_Y),(0,_E,_Z),(0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:swPimRPSetEntry.setStatus(_A)
class _SwPimRPSetComponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwPimRPSetComponent_Type.__name__=_B
_SwPimRPSetComponent_Object=MibTableColumn
swPimRPSetComponent=_SwPimRPSetComponent_Object((1,3,6,1,4,1,171,12,52,3,8,2,1,1),_SwPimRPSetComponent_Type())
swPimRPSetComponent.setMaxAccess(_F)
if mibBuilder.loadTexts:swPimRPSetComponent.setStatus(_A)
_SwPimRPSetGroupAddress_Type=IpAddress
_SwPimRPSetGroupAddress_Object=MibTableColumn
swPimRPSetGroupAddress=_SwPimRPSetGroupAddress_Object((1,3,6,1,4,1,171,12,52,3,8,2,1,2),_SwPimRPSetGroupAddress_Type())
swPimRPSetGroupAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:swPimRPSetGroupAddress.setStatus(_A)
_SwPimRPSetGroupMask_Type=IpAddress
_SwPimRPSetGroupMask_Object=MibTableColumn
swPimRPSetGroupMask=_SwPimRPSetGroupMask_Object((1,3,6,1,4,1,171,12,52,3,8,2,1,3),_SwPimRPSetGroupMask_Type())
swPimRPSetGroupMask.setMaxAccess(_F)
if mibBuilder.loadTexts:swPimRPSetGroupMask.setStatus(_A)
_SwPimRPSetAddress_Type=IpAddress
_SwPimRPSetAddress_Object=MibTableColumn
swPimRPSetAddress=_SwPimRPSetAddress_Object((1,3,6,1,4,1,171,12,52,3,8,2,1,4),_SwPimRPSetAddress_Type())
swPimRPSetAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:swPimRPSetAddress.setStatus(_A)
class _SwPimRPSetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('static',2),('dynamic',3)))
_SwPimRPSetType_Type.__name__=_B
_SwPimRPSetType_Object=MibTableColumn
swPimRPSetType=_SwPimRPSetType_Object((1,3,6,1,4,1,171,12,52,3,8,2,1,5),_SwPimRPSetType_Type())
swPimRPSetType.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimRPSetType.setStatus(_A)
_SwPimRPSetHoldTime_Type=Integer32
_SwPimRPSetHoldTime_Object=MibTableColumn
swPimRPSetHoldTime=_SwPimRPSetHoldTime_Object((1,3,6,1,4,1,171,12,52,3,8,2,1,6),_SwPimRPSetHoldTime_Type())
swPimRPSetHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimRPSetHoldTime.setStatus(_A)
_SwPimRPSetUpTime_Type=TimeTicks
_SwPimRPSetUpTime_Object=MibTableColumn
swPimRPSetUpTime=_SwPimRPSetUpTime_Object((1,3,6,1,4,1,171,12,52,3,8,2,1,7),_SwPimRPSetUpTime_Type())
swPimRPSetUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimRPSetUpTime.setStatus(_A)
_SwPimRPSetExpiryTime_Type=TimeTicks
_SwPimRPSetExpiryTime_Object=MibTableColumn
swPimRPSetExpiryTime=_SwPimRPSetExpiryTime_Object((1,3,6,1,4,1,171,12,52,3,8,2,1,8),_SwPimRPSetExpiryTime_Type())
swPimRPSetExpiryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swPimRPSetExpiryTime.setStatus(_A)
_SwPimSSmMgmt_ObjectIdentity=ObjectIdentity
swPimSSmMgmt=_SwPimSSmMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,52,4))
class _SwPimSSmGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwPimSSmGlobalState_Type.__name__=_B
_SwPimSSmGlobalState_Object=MibScalar
swPimSSmGlobalState=_SwPimSSmGlobalState_Object((1,3,6,1,4,1,171,12,52,4,1),_SwPimSSmGlobalState_Type())
swPimSSmGlobalState.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimSSmGlobalState.setStatus(_A)
_SwPimSSmGroupAddress_Type=IpAddress
_SwPimSSmGroupAddress_Object=MibScalar
swPimSSmGroupAddress=_SwPimSSmGroupAddress_Object((1,3,6,1,4,1,171,12,52,4,2),_SwPimSSmGroupAddress_Type())
swPimSSmGroupAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimSSmGroupAddress.setStatus(_A)
_SwPimSSmGroupMask_Type=IpAddress
_SwPimSSmGroupMask_Object=MibScalar
swPimSSmGroupMask=_SwPimSSmGroupMask_Object((1,3,6,1,4,1,171,12,52,4,3),_SwPimSSmGroupMask_Type())
swPimSSmGroupMask.setMaxAccess(_C)
if mibBuilder.loadTexts:swPimSSmGroupMask.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'swPimSmMIB':swPimSmMIB,'swPimSmCtrl':swPimSmCtrl,'swPimSmGlobalState':swPimSmGlobalState,'swPimSmInfo':swPimSmInfo,'swPimRegisterProbeTime':swPimRegisterProbeTime,'swPimRegisterSuppressionTime':swPimRegisterSuppressionTime,'swPimInfoTable':swPimInfoTable,'swPimInfoEntry':swPimInfoEntry,_L:swPimInfoInterface,'swPimInfoAddress':swPimInfoAddress,'swPimInfoNetMask':swPimInfoNetMask,'swPimInfoDesignatedRouter':swPimInfoDesignatedRouter,'swPimInfoHelloInterval':swPimInfoHelloInterval,'swPimInfoJoinPruneInterval':swPimInfoJoinPruneInterval,'swPimInfoDRPriority':swPimInfoDRPriority,'swPimInfoMode':swPimInfoMode,'swPimInfoState':swPimInfoState,'swPimInfoPassiveMode':swPimInfoPassiveMode,'swPimSmMgmt':swPimSmMgmt,'swPimCbsrInfoMgmt':swPimCbsrInfoMgmt,'swpimCbsrBootStrapPeriod':swpimCbsrBootStrapPeriod,'swPimCbsrHashMaskLen':swPimCbsrHashMaskLen,'swPimCbsrTable':swPimCbsrTable,'swPimCbsrEntry':swPimCbsrEntry,_N:swPimCbsrInterface,'swPimCbsrIpAddress':swPimCbsrIpAddress,'swPimCbsrSubnetMask':swPimCbsrSubnetMask,'swPimCbsrPriority':swPimCbsrPriority,'swPimCandidateRPMgmt':swPimCandidateRPMgmt,'swPimCandidateRPHoldtime':swPimCandidateRPHoldtime,'swPimCandidateRPPriority':swPimCandidateRPPriority,'swPimCandidateRPWildcardPrefixCnt':swPimCandidateRPWildcardPrefixCnt,'swPimCandidateRPTable':swPimCandidateRPTable,'swPimCandidateRPEntry':swPimCandidateRPEntry,_O:swPimCandidateRPGroupAddress,_P:swPimCandidateRPGroupMask,'swPimCandidateRPInterface':swPimCandidateRPInterface,'swPimCandidateRPRowStatus':swPimCandidateRPRowStatus,'swPimNeighborTable':swPimNeighborTable,'swPimNeighborEntry':swPimNeighborEntry,_Q:swPimNeighborAddress,'swPimNeighborIfIndex':swPimNeighborIfIndex,'swPimNeighborExpiryTime':swPimNeighborExpiryTime,'swPimSptMgmt':swPimSptMgmt,'swPimLastHopSptThreshold':swPimLastHopSptThreshold,'swPimRPSptThreshold':swPimRPSptThreshold,'swPimLastHopSptSwitchover':swPimLastHopSptSwitchover,'swPimRegChksumIncDataTable':swPimRegChksumIncDataTable,'swPimRegChksumIncDataEntry':swPimRegChksumIncDataEntry,_R:swL3SwPimRegChksumIncDataRpAddr,'swL3SwPimRegChksumIncDataState':swL3SwPimRegChksumIncDataState,'swPimStaticRPTable':swPimStaticRPTable,'swPimStaticRPEntry':swPimStaticRPEntry,_S:swPimStaticRPGroupAddress,_T:swPimStaticRPGroupMask,_U:swPimStaticRPAddress,'swPimStaticRPRowStatus':swPimStaticRPRowStatus,'swPimIpMRouteTable':swPimIpMRouteTable,'swPimIpMRouteEntry':swPimIpMRouteEntry,_V:swPimIpMRouteGroup,_W:swPimIpMRouteSource,_X:swPimIpMRouteSourceMask,'swPimIpMRouteUpstreamAssertTimer':swPimIpMRouteUpstreamAssertTimer,'swPimIpMRouteAssertMetric':swPimIpMRouteAssertMetric,'swPimIpMRouteAssertMetricPref':swPimIpMRouteAssertMetricPref,'swPimIpMRouteAssertRPTBit':swPimIpMRouteAssertRPTBit,'swPimIpMRouteFlags':swPimIpMRouteFlags,'swPimIpMRouteType':swPimIpMRouteType,'swPimRPSetMgmt':swPimRPSetMgmt,'swPimRPSetBootstrapRouter':swPimRPSetBootstrapRouter,'swPimRPSetTable':swPimRPSetTable,'swPimRPSetEntry':swPimRPSetEntry,_Y:swPimRPSetComponent,_Z:swPimRPSetGroupAddress,_a:swPimRPSetGroupMask,_b:swPimRPSetAddress,'swPimRPSetType':swPimRPSetType,'swPimRPSetHoldTime':swPimRPSetHoldTime,'swPimRPSetUpTime':swPimRPSetUpTime,'swPimRPSetExpiryTime':swPimRPSetExpiryTime,'swPimSSmMgmt':swPimSSmMgmt,'swPimSSmGlobalState':swPimSSmGlobalState,'swPimSSmGroupAddress':swPimSSmGroupAddress,'swPimSSmGroupMask':swPimSSmGroupMask})