_AC='pimDenseV2MIBGroup'
_AB='pimV2CandidateRPMIBGroup'
_AA='pimV2MIBGroup'
_A9='pimV1MIBGroup'
_A8='pimNeighborLoss'
_A7='pimIpMRouteAssertRPTBit'
_A6='pimIpMRouteAssertMetricPref'
_A5='pimIpMRouteAssertMetric'
_A4='pimIpMRouteNextHopPruneReason'
_A3='pimRPRowStatus'
_A2='pimRPLastChange'
_A1='pimRPStateTimer'
_A0='pimRPState'
_z='pimNeighborMode'
_y='pimCandidateRPRowStatus'
_x='pimCandidateRPAddress'
_w='pimIpMRouteUpstreamAssertTimer'
_v='pimIpMRouteFlags'
_u='pimComponentStatus'
_t='pimComponentCRPHoldTime'
_s='pimComponentBSRExpiryTime'
_r='pimComponentBSRAddress'
_q='pimRPSetExpiryTime'
_p='pimRPSetHoldTime'
_o='pimInterfaceCBSRPreference'
_n='pimComponentIndex'
_m='pimCandidateRPGroupMask'
_l='pimCandidateRPGroupAddress'
_k='pimRPSetAddress'
_j='pimRPSetGroupMask'
_i='pimRPSetGroupAddress'
_h='pimRPSetComponent'
_g='pimRPAddress'
_f='pimRPGroupAddress'
_e='pimNeighborAddress'
_d='sparse'
_c='pimInterfaceIfIndex'
_b='ipMRouteSourceMask'
_a='ipMRouteSource'
_Z='ipMRouteNextHopSourceMask'
_Y='ipMRouteNextHopSource'
_X='ipMRouteNextHopIfIndex'
_W='ipMRouteNextHopGroup'
_V='ipMRouteNextHopAddress'
_U='ipMRouteGroup'
_T='pimInterfaceJoinPruneInterval'
_S='pimJoinPruneInterval'
_R='pimInterfaceMode'
_Q='pimInterfaceStatus'
_P='pimInterfaceHelloInterval'
_O='pimInterfaceDR'
_N='pimInterfaceNetMask'
_M='pimInterfaceAddress'
_L='pimNeighborExpiryTime'
_K='pimNeighborUpTime'
_J='pimNeighborIfIndex'
_I='seconds'
_H='IPMROUTE-STD-MIB'
_G='read-create'
_F='deprecated'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='current'
_A='PIM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ipMRouteGroup,ipMRouteNextHopAddress,ipMRouteNextHopGroup,ipMRouteNextHopIfIndex,ipMRouteNextHopSource,ipMRouteNextHopSourceMask,ipMRouteSource,ipMRouteSourceMask=mibBuilder.importSymbols(_H,_U,_V,_W,_X,_Y,_Z,_a,_b)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
pimMIB=ModuleIdentity((1,3,6,1,3,61))
if mibBuilder.loadTexts:pimMIB.setRevisions(('2000-09-28 00:00',))
_PimMIBObjects_ObjectIdentity=ObjectIdentity
pimMIBObjects=_PimMIBObjects_ObjectIdentity((1,3,6,1,3,61,1))
_PimTraps_ObjectIdentity=ObjectIdentity
pimTraps=_PimTraps_ObjectIdentity((1,3,6,1,3,61,1,0))
_Pim_ObjectIdentity=ObjectIdentity
pim=_Pim_ObjectIdentity((1,3,6,1,3,61,1,1))
_PimJoinPruneInterval_Type=Integer32
_PimJoinPruneInterval_Object=MibScalar
pimJoinPruneInterval=_PimJoinPruneInterval_Object((1,3,6,1,3,61,1,1,1),_PimJoinPruneInterval_Type())
pimJoinPruneInterval.setMaxAccess('read-write')
if mibBuilder.loadTexts:pimJoinPruneInterval.setStatus(_B)
if mibBuilder.loadTexts:pimJoinPruneInterval.setUnits(_I)
_PimInterfaceTable_Object=MibTable
pimInterfaceTable=_PimInterfaceTable_Object((1,3,6,1,3,61,1,1,2))
if mibBuilder.loadTexts:pimInterfaceTable.setStatus(_B)
_PimInterfaceEntry_Object=MibTableRow
pimInterfaceEntry=_PimInterfaceEntry_Object((1,3,6,1,3,61,1,1,2,1))
pimInterfaceEntry.setIndexNames((0,_A,_c))
if mibBuilder.loadTexts:pimInterfaceEntry.setStatus(_B)
_PimInterfaceIfIndex_Type=InterfaceIndex
_PimInterfaceIfIndex_Object=MibTableColumn
pimInterfaceIfIndex=_PimInterfaceIfIndex_Object((1,3,6,1,3,61,1,1,2,1,1),_PimInterfaceIfIndex_Type())
pimInterfaceIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pimInterfaceIfIndex.setStatus(_B)
_PimInterfaceAddress_Type=IpAddress
_PimInterfaceAddress_Object=MibTableColumn
pimInterfaceAddress=_PimInterfaceAddress_Object((1,3,6,1,3,61,1,1,2,1,2),_PimInterfaceAddress_Type())
pimInterfaceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pimInterfaceAddress.setStatus(_B)
_PimInterfaceNetMask_Type=IpAddress
_PimInterfaceNetMask_Object=MibTableColumn
pimInterfaceNetMask=_PimInterfaceNetMask_Object((1,3,6,1,3,61,1,1,2,1,3),_PimInterfaceNetMask_Type())
pimInterfaceNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:pimInterfaceNetMask.setStatus(_B)
class _PimInterfaceMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dense',1),(_d,2),('sparseDense',3)))
_PimInterfaceMode_Type.__name__=_D
_PimInterfaceMode_Object=MibTableColumn
pimInterfaceMode=_PimInterfaceMode_Object((1,3,6,1,3,61,1,1,2,1,4),_PimInterfaceMode_Type())
pimInterfaceMode.setMaxAccess(_G)
if mibBuilder.loadTexts:pimInterfaceMode.setStatus(_B)
_PimInterfaceDR_Type=IpAddress
_PimInterfaceDR_Object=MibTableColumn
pimInterfaceDR=_PimInterfaceDR_Object((1,3,6,1,3,61,1,1,2,1,5),_PimInterfaceDR_Type())
pimInterfaceDR.setMaxAccess(_C)
if mibBuilder.loadTexts:pimInterfaceDR.setStatus(_B)
class _PimInterfaceHelloInterval_Type(Integer32):defaultValue=30
_PimInterfaceHelloInterval_Type.__name__=_D
_PimInterfaceHelloInterval_Object=MibTableColumn
pimInterfaceHelloInterval=_PimInterfaceHelloInterval_Object((1,3,6,1,3,61,1,1,2,1,6),_PimInterfaceHelloInterval_Type())
pimInterfaceHelloInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:pimInterfaceHelloInterval.setStatus(_B)
if mibBuilder.loadTexts:pimInterfaceHelloInterval.setUnits(_I)
_PimInterfaceStatus_Type=RowStatus
_PimInterfaceStatus_Object=MibTableColumn
pimInterfaceStatus=_PimInterfaceStatus_Object((1,3,6,1,3,61,1,1,2,1,7),_PimInterfaceStatus_Type())
pimInterfaceStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:pimInterfaceStatus.setStatus(_B)
_PimInterfaceJoinPruneInterval_Type=Integer32
_PimInterfaceJoinPruneInterval_Object=MibTableColumn
pimInterfaceJoinPruneInterval=_PimInterfaceJoinPruneInterval_Object((1,3,6,1,3,61,1,1,2,1,8),_PimInterfaceJoinPruneInterval_Type())
pimInterfaceJoinPruneInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:pimInterfaceJoinPruneInterval.setStatus(_B)
if mibBuilder.loadTexts:pimInterfaceJoinPruneInterval.setUnits(_I)
class _PimInterfaceCBSRPreference_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_PimInterfaceCBSRPreference_Type.__name__=_D
_PimInterfaceCBSRPreference_Object=MibTableColumn
pimInterfaceCBSRPreference=_PimInterfaceCBSRPreference_Object((1,3,6,1,3,61,1,1,2,1,9),_PimInterfaceCBSRPreference_Type())
pimInterfaceCBSRPreference.setMaxAccess(_G)
if mibBuilder.loadTexts:pimInterfaceCBSRPreference.setStatus(_B)
_PimNeighborTable_Object=MibTable
pimNeighborTable=_PimNeighborTable_Object((1,3,6,1,3,61,1,1,3))
if mibBuilder.loadTexts:pimNeighborTable.setStatus(_B)
_PimNeighborEntry_Object=MibTableRow
pimNeighborEntry=_PimNeighborEntry_Object((1,3,6,1,3,61,1,1,3,1))
pimNeighborEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:pimNeighborEntry.setStatus(_B)
_PimNeighborAddress_Type=IpAddress
_PimNeighborAddress_Object=MibTableColumn
pimNeighborAddress=_PimNeighborAddress_Object((1,3,6,1,3,61,1,1,3,1,1),_PimNeighborAddress_Type())
pimNeighborAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:pimNeighborAddress.setStatus(_B)
_PimNeighborIfIndex_Type=InterfaceIndex
_PimNeighborIfIndex_Object=MibTableColumn
pimNeighborIfIndex=_PimNeighborIfIndex_Object((1,3,6,1,3,61,1,1,3,1,2),_PimNeighborIfIndex_Type())
pimNeighborIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pimNeighborIfIndex.setStatus(_B)
_PimNeighborUpTime_Type=TimeTicks
_PimNeighborUpTime_Object=MibTableColumn
pimNeighborUpTime=_PimNeighborUpTime_Object((1,3,6,1,3,61,1,1,3,1,3),_PimNeighborUpTime_Type())
pimNeighborUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pimNeighborUpTime.setStatus(_B)
_PimNeighborExpiryTime_Type=TimeTicks
_PimNeighborExpiryTime_Object=MibTableColumn
pimNeighborExpiryTime=_PimNeighborExpiryTime_Object((1,3,6,1,3,61,1,1,3,1,4),_PimNeighborExpiryTime_Type())
pimNeighborExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pimNeighborExpiryTime.setStatus(_B)
class _PimNeighborMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dense',1),(_d,2)))
_PimNeighborMode_Type.__name__=_D
_PimNeighborMode_Object=MibTableColumn
pimNeighborMode=_PimNeighborMode_Object((1,3,6,1,3,61,1,1,3,1,5),_PimNeighborMode_Type())
pimNeighborMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pimNeighborMode.setStatus(_F)
_PimIpMRouteTable_Object=MibTable
pimIpMRouteTable=_PimIpMRouteTable_Object((1,3,6,1,3,61,1,1,4))
if mibBuilder.loadTexts:pimIpMRouteTable.setStatus(_B)
_PimIpMRouteEntry_Object=MibTableRow
pimIpMRouteEntry=_PimIpMRouteEntry_Object((1,3,6,1,3,61,1,1,4,1))
pimIpMRouteEntry.setIndexNames((0,_H,_U),(0,_H,_a),(0,_H,_b))
if mibBuilder.loadTexts:pimIpMRouteEntry.setStatus(_B)
_PimIpMRouteUpstreamAssertTimer_Type=TimeTicks
_PimIpMRouteUpstreamAssertTimer_Object=MibTableColumn
pimIpMRouteUpstreamAssertTimer=_PimIpMRouteUpstreamAssertTimer_Object((1,3,6,1,3,61,1,1,4,1,1),_PimIpMRouteUpstreamAssertTimer_Type())
pimIpMRouteUpstreamAssertTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:pimIpMRouteUpstreamAssertTimer.setStatus(_B)
_PimIpMRouteAssertMetric_Type=Integer32
_PimIpMRouteAssertMetric_Object=MibTableColumn
pimIpMRouteAssertMetric=_PimIpMRouteAssertMetric_Object((1,3,6,1,3,61,1,1,4,1,2),_PimIpMRouteAssertMetric_Type())
pimIpMRouteAssertMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:pimIpMRouteAssertMetric.setStatus(_B)
_PimIpMRouteAssertMetricPref_Type=Integer32
_PimIpMRouteAssertMetricPref_Object=MibTableColumn
pimIpMRouteAssertMetricPref=_PimIpMRouteAssertMetricPref_Object((1,3,6,1,3,61,1,1,4,1,3),_PimIpMRouteAssertMetricPref_Type())
pimIpMRouteAssertMetricPref.setMaxAccess(_C)
if mibBuilder.loadTexts:pimIpMRouteAssertMetricPref.setStatus(_B)
_PimIpMRouteAssertRPTBit_Type=TruthValue
_PimIpMRouteAssertRPTBit_Object=MibTableColumn
pimIpMRouteAssertRPTBit=_PimIpMRouteAssertRPTBit_Object((1,3,6,1,3,61,1,1,4,1,4),_PimIpMRouteAssertRPTBit_Type())
pimIpMRouteAssertRPTBit.setMaxAccess(_C)
if mibBuilder.loadTexts:pimIpMRouteAssertRPTBit.setStatus(_B)
class _PimIpMRouteFlags_Type(Bits):namedValues=NamedValues(*(('rpt',0),('spt',1)))
_PimIpMRouteFlags_Type.__name__='Bits'
_PimIpMRouteFlags_Object=MibTableColumn
pimIpMRouteFlags=_PimIpMRouteFlags_Object((1,3,6,1,3,61,1,1,4,1,5),_PimIpMRouteFlags_Type())
pimIpMRouteFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:pimIpMRouteFlags.setStatus(_B)
_PimRPTable_Object=MibTable
pimRPTable=_PimRPTable_Object((1,3,6,1,3,61,1,1,5))
if mibBuilder.loadTexts:pimRPTable.setStatus(_F)
_PimRPEntry_Object=MibTableRow
pimRPEntry=_PimRPEntry_Object((1,3,6,1,3,61,1,1,5,1))
pimRPEntry.setIndexNames((0,_A,_f),(0,_A,_g))
if mibBuilder.loadTexts:pimRPEntry.setStatus(_F)
_PimRPGroupAddress_Type=IpAddress
_PimRPGroupAddress_Object=MibTableColumn
pimRPGroupAddress=_PimRPGroupAddress_Object((1,3,6,1,3,61,1,1,5,1,1),_PimRPGroupAddress_Type())
pimRPGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:pimRPGroupAddress.setStatus(_F)
_PimRPAddress_Type=IpAddress
_PimRPAddress_Object=MibTableColumn
pimRPAddress=_PimRPAddress_Object((1,3,6,1,3,61,1,1,5,1,2),_PimRPAddress_Type())
pimRPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:pimRPAddress.setStatus(_F)
class _PimRPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_PimRPState_Type.__name__=_D
_PimRPState_Object=MibTableColumn
pimRPState=_PimRPState_Object((1,3,6,1,3,61,1,1,5,1,3),_PimRPState_Type())
pimRPState.setMaxAccess(_C)
if mibBuilder.loadTexts:pimRPState.setStatus(_F)
_PimRPStateTimer_Type=TimeTicks
_PimRPStateTimer_Object=MibTableColumn
pimRPStateTimer=_PimRPStateTimer_Object((1,3,6,1,3,61,1,1,5,1,4),_PimRPStateTimer_Type())
pimRPStateTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:pimRPStateTimer.setStatus(_F)
_PimRPLastChange_Type=TimeTicks
_PimRPLastChange_Object=MibTableColumn
pimRPLastChange=_PimRPLastChange_Object((1,3,6,1,3,61,1,1,5,1,5),_PimRPLastChange_Type())
pimRPLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:pimRPLastChange.setStatus(_F)
_PimRPRowStatus_Type=RowStatus
_PimRPRowStatus_Object=MibTableColumn
pimRPRowStatus=_PimRPRowStatus_Object((1,3,6,1,3,61,1,1,5,1,6),_PimRPRowStatus_Type())
pimRPRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:pimRPRowStatus.setStatus(_F)
_PimRPSetTable_Object=MibTable
pimRPSetTable=_PimRPSetTable_Object((1,3,6,1,3,61,1,1,6))
if mibBuilder.loadTexts:pimRPSetTable.setStatus(_B)
_PimRPSetEntry_Object=MibTableRow
pimRPSetEntry=_PimRPSetEntry_Object((1,3,6,1,3,61,1,1,6,1))
pimRPSetEntry.setIndexNames((0,_A,_h),(0,_A,_i),(0,_A,_j),(0,_A,_k))
if mibBuilder.loadTexts:pimRPSetEntry.setStatus(_B)
_PimRPSetGroupAddress_Type=IpAddress
_PimRPSetGroupAddress_Object=MibTableColumn
pimRPSetGroupAddress=_PimRPSetGroupAddress_Object((1,3,6,1,3,61,1,1,6,1,1),_PimRPSetGroupAddress_Type())
pimRPSetGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:pimRPSetGroupAddress.setStatus(_B)
_PimRPSetGroupMask_Type=IpAddress
_PimRPSetGroupMask_Object=MibTableColumn
pimRPSetGroupMask=_PimRPSetGroupMask_Object((1,3,6,1,3,61,1,1,6,1,2),_PimRPSetGroupMask_Type())
pimRPSetGroupMask.setMaxAccess(_E)
if mibBuilder.loadTexts:pimRPSetGroupMask.setStatus(_B)
_PimRPSetAddress_Type=IpAddress
_PimRPSetAddress_Object=MibTableColumn
pimRPSetAddress=_PimRPSetAddress_Object((1,3,6,1,3,61,1,1,6,1,3),_PimRPSetAddress_Type())
pimRPSetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:pimRPSetAddress.setStatus(_B)
class _PimRPSetHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PimRPSetHoldTime_Type.__name__=_D
_PimRPSetHoldTime_Object=MibTableColumn
pimRPSetHoldTime=_PimRPSetHoldTime_Object((1,3,6,1,3,61,1,1,6,1,4),_PimRPSetHoldTime_Type())
pimRPSetHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pimRPSetHoldTime.setStatus(_B)
if mibBuilder.loadTexts:pimRPSetHoldTime.setUnits(_I)
_PimRPSetExpiryTime_Type=TimeTicks
_PimRPSetExpiryTime_Object=MibTableColumn
pimRPSetExpiryTime=_PimRPSetExpiryTime_Object((1,3,6,1,3,61,1,1,6,1,5),_PimRPSetExpiryTime_Type())
pimRPSetExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pimRPSetExpiryTime.setStatus(_B)
class _PimRPSetComponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PimRPSetComponent_Type.__name__=_D
_PimRPSetComponent_Object=MibTableColumn
pimRPSetComponent=_PimRPSetComponent_Object((1,3,6,1,3,61,1,1,6,1,6),_PimRPSetComponent_Type())
pimRPSetComponent.setMaxAccess(_E)
if mibBuilder.loadTexts:pimRPSetComponent.setStatus(_B)
_PimIpMRouteNextHopTable_Object=MibTable
pimIpMRouteNextHopTable=_PimIpMRouteNextHopTable_Object((1,3,6,1,3,61,1,1,7))
if mibBuilder.loadTexts:pimIpMRouteNextHopTable.setStatus(_B)
_PimIpMRouteNextHopEntry_Object=MibTableRow
pimIpMRouteNextHopEntry=_PimIpMRouteNextHopEntry_Object((1,3,6,1,3,61,1,1,7,1))
pimIpMRouteNextHopEntry.setIndexNames((0,_H,_W),(0,_H,_Y),(0,_H,_Z),(0,_H,_X),(0,_H,_V))
if mibBuilder.loadTexts:pimIpMRouteNextHopEntry.setStatus(_B)
class _PimIpMRouteNextHopPruneReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('prune',2),('assert',3)))
_PimIpMRouteNextHopPruneReason_Type.__name__=_D
_PimIpMRouteNextHopPruneReason_Object=MibTableColumn
pimIpMRouteNextHopPruneReason=_PimIpMRouteNextHopPruneReason_Object((1,3,6,1,3,61,1,1,7,1,2),_PimIpMRouteNextHopPruneReason_Type())
pimIpMRouteNextHopPruneReason.setMaxAccess(_C)
if mibBuilder.loadTexts:pimIpMRouteNextHopPruneReason.setStatus(_B)
_PimCandidateRPTable_Object=MibTable
pimCandidateRPTable=_PimCandidateRPTable_Object((1,3,6,1,3,61,1,1,11))
if mibBuilder.loadTexts:pimCandidateRPTable.setStatus(_B)
_PimCandidateRPEntry_Object=MibTableRow
pimCandidateRPEntry=_PimCandidateRPEntry_Object((1,3,6,1,3,61,1,1,11,1))
pimCandidateRPEntry.setIndexNames((0,_A,_l),(0,_A,_m))
if mibBuilder.loadTexts:pimCandidateRPEntry.setStatus(_B)
_PimCandidateRPGroupAddress_Type=IpAddress
_PimCandidateRPGroupAddress_Object=MibTableColumn
pimCandidateRPGroupAddress=_PimCandidateRPGroupAddress_Object((1,3,6,1,3,61,1,1,11,1,1),_PimCandidateRPGroupAddress_Type())
pimCandidateRPGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:pimCandidateRPGroupAddress.setStatus(_B)
_PimCandidateRPGroupMask_Type=IpAddress
_PimCandidateRPGroupMask_Object=MibTableColumn
pimCandidateRPGroupMask=_PimCandidateRPGroupMask_Object((1,3,6,1,3,61,1,1,11,1,2),_PimCandidateRPGroupMask_Type())
pimCandidateRPGroupMask.setMaxAccess(_E)
if mibBuilder.loadTexts:pimCandidateRPGroupMask.setStatus(_B)
_PimCandidateRPAddress_Type=IpAddress
_PimCandidateRPAddress_Object=MibTableColumn
pimCandidateRPAddress=_PimCandidateRPAddress_Object((1,3,6,1,3,61,1,1,11,1,3),_PimCandidateRPAddress_Type())
pimCandidateRPAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:pimCandidateRPAddress.setStatus(_B)
_PimCandidateRPRowStatus_Type=RowStatus
_PimCandidateRPRowStatus_Object=MibTableColumn
pimCandidateRPRowStatus=_PimCandidateRPRowStatus_Object((1,3,6,1,3,61,1,1,11,1,4),_PimCandidateRPRowStatus_Type())
pimCandidateRPRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:pimCandidateRPRowStatus.setStatus(_B)
_PimComponentTable_Object=MibTable
pimComponentTable=_PimComponentTable_Object((1,3,6,1,3,61,1,1,12))
if mibBuilder.loadTexts:pimComponentTable.setStatus(_B)
_PimComponentEntry_Object=MibTableRow
pimComponentEntry=_PimComponentEntry_Object((1,3,6,1,3,61,1,1,12,1))
pimComponentEntry.setIndexNames((0,_A,_n))
if mibBuilder.loadTexts:pimComponentEntry.setStatus(_B)
class _PimComponentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PimComponentIndex_Type.__name__=_D
_PimComponentIndex_Object=MibTableColumn
pimComponentIndex=_PimComponentIndex_Object((1,3,6,1,3,61,1,1,12,1,1),_PimComponentIndex_Type())
pimComponentIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pimComponentIndex.setStatus(_B)
_PimComponentBSRAddress_Type=IpAddress
_PimComponentBSRAddress_Object=MibTableColumn
pimComponentBSRAddress=_PimComponentBSRAddress_Object((1,3,6,1,3,61,1,1,12,1,2),_PimComponentBSRAddress_Type())
pimComponentBSRAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pimComponentBSRAddress.setStatus(_B)
_PimComponentBSRExpiryTime_Type=TimeTicks
_PimComponentBSRExpiryTime_Object=MibTableColumn
pimComponentBSRExpiryTime=_PimComponentBSRExpiryTime_Object((1,3,6,1,3,61,1,1,12,1,3),_PimComponentBSRExpiryTime_Type())
pimComponentBSRExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pimComponentBSRExpiryTime.setStatus(_B)
class _PimComponentCRPHoldTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PimComponentCRPHoldTime_Type.__name__=_D
_PimComponentCRPHoldTime_Object=MibTableColumn
pimComponentCRPHoldTime=_PimComponentCRPHoldTime_Object((1,3,6,1,3,61,1,1,12,1,4),_PimComponentCRPHoldTime_Type())
pimComponentCRPHoldTime.setMaxAccess(_G)
if mibBuilder.loadTexts:pimComponentCRPHoldTime.setStatus(_B)
if mibBuilder.loadTexts:pimComponentCRPHoldTime.setUnits(_I)
_PimComponentStatus_Type=RowStatus
_PimComponentStatus_Object=MibTableColumn
pimComponentStatus=_PimComponentStatus_Object((1,3,6,1,3,61,1,1,12,1,5),_PimComponentStatus_Type())
pimComponentStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:pimComponentStatus.setStatus(_B)
_PimMIBConformance_ObjectIdentity=ObjectIdentity
pimMIBConformance=_PimMIBConformance_ObjectIdentity((1,3,6,1,3,61,2))
_PimMIBCompliances_ObjectIdentity=ObjectIdentity
pimMIBCompliances=_PimMIBCompliances_ObjectIdentity((1,3,6,1,3,61,2,1))
_PimMIBGroups_ObjectIdentity=ObjectIdentity
pimMIBGroups=_PimMIBGroups_ObjectIdentity((1,3,6,1,3,61,2,2))
pimV2MIBGroup=ObjectGroup((1,3,6,1,3,61,2,2,2))
pimV2MIBGroup.setObjects(*((_A,_S),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_T),(_A,_o),(_A,_R),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:pimV2MIBGroup.setStatus(_B)
pimV2CandidateRPMIBGroup=ObjectGroup((1,3,6,1,3,61,2,2,3))
pimV2CandidateRPMIBGroup.setObjects(*((_A,_x),(_A,_y)))
if mibBuilder.loadTexts:pimV2CandidateRPMIBGroup.setStatus(_B)
pimV1MIBGroup=ObjectGroup((1,3,6,1,3,61,2,2,4))
pimV1MIBGroup.setObjects(*((_A,_S),(_A,_J),(_A,_K),(_A,_L),(_A,_z),(_A,_M),(_A,_N),(_A,_T),(_A,_Q),(_A,_R),(_A,_O),(_A,_P),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:pimV1MIBGroup.setStatus(_F)
pimDenseV2MIBGroup=ObjectGroup((1,3,6,1,3,61,2,2,5))
pimDenseV2MIBGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:pimDenseV2MIBGroup.setStatus(_B)
pimNextHopGroup=ObjectGroup((1,3,6,1,3,61,2,2,6))
pimNextHopGroup.setObjects((_A,_A4))
if mibBuilder.loadTexts:pimNextHopGroup.setStatus(_B)
pimAssertGroup=ObjectGroup((1,3,6,1,3,61,2,2,7))
pimAssertGroup.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:pimAssertGroup.setStatus(_B)
pimNeighborLoss=NotificationType((1,3,6,1,3,61,1,0,1))
pimNeighborLoss.setObjects((_A,_J))
if mibBuilder.loadTexts:pimNeighborLoss.setStatus(_B)
pimNotificationGroup=NotificationGroup((1,3,6,1,3,61,2,2,1))
pimNotificationGroup.setObjects((_A,_A8))
if mibBuilder.loadTexts:pimNotificationGroup.setStatus(_B)
pimV1MIBCompliance=ModuleCompliance((1,3,6,1,3,61,2,1,1))
pimV1MIBCompliance.setObjects((_A,_A9))
if mibBuilder.loadTexts:pimV1MIBCompliance.setStatus(_F)
pimSparseV2MIBCompliance=ModuleCompliance((1,3,6,1,3,61,2,1,2))
pimSparseV2MIBCompliance.setObjects(*((_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:pimSparseV2MIBCompliance.setStatus(_B)
pimDenseV2MIBCompliance=ModuleCompliance((1,3,6,1,3,61,2,1,3))
pimDenseV2MIBCompliance.setObjects((_A,_AC))
if mibBuilder.loadTexts:pimDenseV2MIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'pimMIB':pimMIB,'pimMIBObjects':pimMIBObjects,'pimTraps':pimTraps,_A8:pimNeighborLoss,'pim':pim,_S:pimJoinPruneInterval,'pimInterfaceTable':pimInterfaceTable,'pimInterfaceEntry':pimInterfaceEntry,_c:pimInterfaceIfIndex,_M:pimInterfaceAddress,_N:pimInterfaceNetMask,_R:pimInterfaceMode,_O:pimInterfaceDR,_P:pimInterfaceHelloInterval,_Q:pimInterfaceStatus,_T:pimInterfaceJoinPruneInterval,_o:pimInterfaceCBSRPreference,'pimNeighborTable':pimNeighborTable,'pimNeighborEntry':pimNeighborEntry,_e:pimNeighborAddress,_J:pimNeighborIfIndex,_K:pimNeighborUpTime,_L:pimNeighborExpiryTime,_z:pimNeighborMode,'pimIpMRouteTable':pimIpMRouteTable,'pimIpMRouteEntry':pimIpMRouteEntry,_w:pimIpMRouteUpstreamAssertTimer,_A5:pimIpMRouteAssertMetric,_A6:pimIpMRouteAssertMetricPref,_A7:pimIpMRouteAssertRPTBit,_v:pimIpMRouteFlags,'pimRPTable':pimRPTable,'pimRPEntry':pimRPEntry,_f:pimRPGroupAddress,_g:pimRPAddress,_A0:pimRPState,_A1:pimRPStateTimer,_A2:pimRPLastChange,_A3:pimRPRowStatus,'pimRPSetTable':pimRPSetTable,'pimRPSetEntry':pimRPSetEntry,_i:pimRPSetGroupAddress,_j:pimRPSetGroupMask,_k:pimRPSetAddress,_p:pimRPSetHoldTime,_q:pimRPSetExpiryTime,_h:pimRPSetComponent,'pimIpMRouteNextHopTable':pimIpMRouteNextHopTable,'pimIpMRouteNextHopEntry':pimIpMRouteNextHopEntry,_A4:pimIpMRouteNextHopPruneReason,'pimCandidateRPTable':pimCandidateRPTable,'pimCandidateRPEntry':pimCandidateRPEntry,_l:pimCandidateRPGroupAddress,_m:pimCandidateRPGroupMask,_x:pimCandidateRPAddress,_y:pimCandidateRPRowStatus,'pimComponentTable':pimComponentTable,'pimComponentEntry':pimComponentEntry,_n:pimComponentIndex,_r:pimComponentBSRAddress,_s:pimComponentBSRExpiryTime,_t:pimComponentCRPHoldTime,_u:pimComponentStatus,'pimMIBConformance':pimMIBConformance,'pimMIBCompliances':pimMIBCompliances,'pimV1MIBCompliance':pimV1MIBCompliance,'pimSparseV2MIBCompliance':pimSparseV2MIBCompliance,'pimDenseV2MIBCompliance':pimDenseV2MIBCompliance,'pimMIBGroups':pimMIBGroups,'pimNotificationGroup':pimNotificationGroup,_AA:pimV2MIBGroup,_AB:pimV2CandidateRPMIBGroup,_A9:pimV1MIBGroup,_AC:pimDenseV2MIBGroup,'pimNextHopGroup':pimNextHopGroup,'pimAssertGroup':pimAssertGroup})