_AC='hmPIMDenseV2MIBGroup'
_AB='hmPIMV2CandidateRPMIBGroup'
_AA='hmPIMV2MIBGroup'
_A9='hmPIMV1MIBGroup'
_A8='hmPIMNeighborLoss'
_A7='hmPIMIpMRouteAssertRPTBit'
_A6='hmPIMIpMRouteAssertMetricPref'
_A5='hmPIMIpMRouteAssertMetric'
_A4='hmPIMIpMRouteNextHopPruneReason'
_A3='hmPIMRPRowStatus'
_A2='hmPIMRPLastChange'
_A1='hmPIMRPStateTimer'
_A0='hmPIMRPState'
_z='hmPIMNeighborMode'
_y='hmPIMCandidateRPRowStatus'
_x='hmPIMCandidateRPAddress'
_w='hmPIMIpMRouteUpstreamAssertTimer'
_v='hmPIMIpMRouteFlags'
_u='hmPIMComponentStatus'
_t='hmPIMComponentCRPHoldTime'
_s='hmPIMComponentBSRExpiryTime'
_r='hmPIMComponentBSRAddress'
_q='hmPIMRPSetExpiryTime'
_p='hmPIMRPSetHoldTime'
_o='hmPIMInterfaceCBSRPreference'
_n='hmPIMComponentIndex'
_m='hmPIMCandidateRPGroupMask'
_l='hmPIMCandidateRPGroupAddress'
_k='hmPIMRPSetAddress'
_j='hmPIMRPSetGroupMask'
_i='hmPIMRPSetGroupAddress'
_h='hmPIMRPSetComponent'
_g='hmPIMRPAddress'
_f='hmPIMRPGroupAddress'
_e='hmPIMNeighborAddress'
_d='sparse'
_c='hmPIMInterfaceIfIndex'
_b='ipMRouteSourceMask'
_a='ipMRouteSource'
_Z='ipMRouteNextHopSourceMask'
_Y='ipMRouteNextHopSource'
_X='ipMRouteNextHopIfIndex'
_W='ipMRouteNextHopGroup'
_V='ipMRouteNextHopAddress'
_U='ipMRouteGroup'
_T='hmPIMInterfaceJoinPruneInterval'
_S='hmPIMJoinPruneInterval'
_R='hmPIMInterfaceMode'
_Q='hmPIMInterfaceStatus'
_P='hmPIMInterfaceHelloInterval'
_O='hmPIMInterfaceDR'
_N='hmPIMInterfaceNetMask'
_M='hmPIMInterfaceAddress'
_L='hmPIMNeighborExpiryTime'
_K='hmPIMNeighborUpTime'
_J='hmPIMNeighborIfIndex'
_I='seconds'
_H='IPMROUTE-STD-MIB'
_G='read-create'
_F='deprecated'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='current'
_A='HIRSCHMANN-PIM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmPlatform4Multicast,=mibBuilder.importSymbols('HIRSCHMANN-MULTICAST-MIB','hmPlatform4Multicast')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ipMRouteGroup,ipMRouteNextHopAddress,ipMRouteNextHopGroup,ipMRouteNextHopIfIndex,ipMRouteNextHopSource,ipMRouteNextHopSourceMask,ipMRouteSource,ipMRouteSourceMask=mibBuilder.importSymbols(_H,_U,_V,_W,_X,_Y,_Z,_a,_b)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hmPIMMIB=ModuleIdentity((1,3,6,1,4,1,248,15,4,99))
if mibBuilder.loadTexts:hmPIMMIB.setRevisions(('2006-02-06 12:00',))
_HmPIMMIBObjects_ObjectIdentity=ObjectIdentity
hmPIMMIBObjects=_HmPIMMIBObjects_ObjectIdentity((1,3,6,1,4,1,248,15,4,99,1))
_HmPIMTraps_ObjectIdentity=ObjectIdentity
hmPIMTraps=_HmPIMTraps_ObjectIdentity((1,3,6,1,4,1,248,15,4,99,1,0))
_HmPIM_ObjectIdentity=ObjectIdentity
hmPIM=_HmPIM_ObjectIdentity((1,3,6,1,4,1,248,15,4,99,1,1))
_HmPIMJoinPruneInterval_Type=Integer32
_HmPIMJoinPruneInterval_Object=MibScalar
hmPIMJoinPruneInterval=_HmPIMJoinPruneInterval_Object((1,3,6,1,4,1,248,15,4,99,1,1,1),_HmPIMJoinPruneInterval_Type())
hmPIMJoinPruneInterval.setMaxAccess('read-write')
if mibBuilder.loadTexts:hmPIMJoinPruneInterval.setStatus(_B)
if mibBuilder.loadTexts:hmPIMJoinPruneInterval.setUnits(_I)
_HmPIMInterfaceTable_Object=MibTable
hmPIMInterfaceTable=_HmPIMInterfaceTable_Object((1,3,6,1,4,1,248,15,4,99,1,1,2))
if mibBuilder.loadTexts:hmPIMInterfaceTable.setStatus(_B)
_HmPIMInterfaceEntry_Object=MibTableRow
hmPIMInterfaceEntry=_HmPIMInterfaceEntry_Object((1,3,6,1,4,1,248,15,4,99,1,1,2,1))
hmPIMInterfaceEntry.setIndexNames((0,_A,_c))
if mibBuilder.loadTexts:hmPIMInterfaceEntry.setStatus(_B)
_HmPIMInterfaceIfIndex_Type=InterfaceIndex
_HmPIMInterfaceIfIndex_Object=MibTableColumn
hmPIMInterfaceIfIndex=_HmPIMInterfaceIfIndex_Object((1,3,6,1,4,1,248,15,4,99,1,1,2,1,1),_HmPIMInterfaceIfIndex_Type())
hmPIMInterfaceIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPIMInterfaceIfIndex.setStatus(_B)
_HmPIMInterfaceAddress_Type=IpAddress
_HmPIMInterfaceAddress_Object=MibTableColumn
hmPIMInterfaceAddress=_HmPIMInterfaceAddress_Object((1,3,6,1,4,1,248,15,4,99,1,1,2,1,2),_HmPIMInterfaceAddress_Type())
hmPIMInterfaceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMInterfaceAddress.setStatus(_B)
_HmPIMInterfaceNetMask_Type=IpAddress
_HmPIMInterfaceNetMask_Object=MibTableColumn
hmPIMInterfaceNetMask=_HmPIMInterfaceNetMask_Object((1,3,6,1,4,1,248,15,4,99,1,1,2,1,3),_HmPIMInterfaceNetMask_Type())
hmPIMInterfaceNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMInterfaceNetMask.setStatus(_B)
class _HmPIMInterfaceMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dense',1),(_d,2),('sparseDense',3)))
_HmPIMInterfaceMode_Type.__name__=_D
_HmPIMInterfaceMode_Object=MibTableColumn
hmPIMInterfaceMode=_HmPIMInterfaceMode_Object((1,3,6,1,4,1,248,15,4,99,1,1,2,1,4),_HmPIMInterfaceMode_Type())
hmPIMInterfaceMode.setMaxAccess(_G)
if mibBuilder.loadTexts:hmPIMInterfaceMode.setStatus(_B)
_HmPIMInterfaceDR_Type=IpAddress
_HmPIMInterfaceDR_Object=MibTableColumn
hmPIMInterfaceDR=_HmPIMInterfaceDR_Object((1,3,6,1,4,1,248,15,4,99,1,1,2,1,5),_HmPIMInterfaceDR_Type())
hmPIMInterfaceDR.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMInterfaceDR.setStatus(_B)
class _HmPIMInterfaceHelloInterval_Type(Integer32):defaultValue=30
_HmPIMInterfaceHelloInterval_Type.__name__=_D
_HmPIMInterfaceHelloInterval_Object=MibTableColumn
hmPIMInterfaceHelloInterval=_HmPIMInterfaceHelloInterval_Object((1,3,6,1,4,1,248,15,4,99,1,1,2,1,6),_HmPIMInterfaceHelloInterval_Type())
hmPIMInterfaceHelloInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:hmPIMInterfaceHelloInterval.setStatus(_B)
if mibBuilder.loadTexts:hmPIMInterfaceHelloInterval.setUnits(_I)
_HmPIMInterfaceStatus_Type=RowStatus
_HmPIMInterfaceStatus_Object=MibTableColumn
hmPIMInterfaceStatus=_HmPIMInterfaceStatus_Object((1,3,6,1,4,1,248,15,4,99,1,1,2,1,7),_HmPIMInterfaceStatus_Type())
hmPIMInterfaceStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hmPIMInterfaceStatus.setStatus(_B)
_HmPIMInterfaceJoinPruneInterval_Type=Integer32
_HmPIMInterfaceJoinPruneInterval_Object=MibTableColumn
hmPIMInterfaceJoinPruneInterval=_HmPIMInterfaceJoinPruneInterval_Object((1,3,6,1,4,1,248,15,4,99,1,1,2,1,8),_HmPIMInterfaceJoinPruneInterval_Type())
hmPIMInterfaceJoinPruneInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:hmPIMInterfaceJoinPruneInterval.setStatus(_B)
if mibBuilder.loadTexts:hmPIMInterfaceJoinPruneInterval.setUnits(_I)
class _HmPIMInterfaceCBSRPreference_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_HmPIMInterfaceCBSRPreference_Type.__name__=_D
_HmPIMInterfaceCBSRPreference_Object=MibTableColumn
hmPIMInterfaceCBSRPreference=_HmPIMInterfaceCBSRPreference_Object((1,3,6,1,4,1,248,15,4,99,1,1,2,1,9),_HmPIMInterfaceCBSRPreference_Type())
hmPIMInterfaceCBSRPreference.setMaxAccess(_G)
if mibBuilder.loadTexts:hmPIMInterfaceCBSRPreference.setStatus(_B)
_HmPIMNeighborTable_Object=MibTable
hmPIMNeighborTable=_HmPIMNeighborTable_Object((1,3,6,1,4,1,248,15,4,99,1,1,3))
if mibBuilder.loadTexts:hmPIMNeighborTable.setStatus(_B)
_HmPIMNeighborEntry_Object=MibTableRow
hmPIMNeighborEntry=_HmPIMNeighborEntry_Object((1,3,6,1,4,1,248,15,4,99,1,1,3,1))
hmPIMNeighborEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:hmPIMNeighborEntry.setStatus(_B)
_HmPIMNeighborAddress_Type=IpAddress
_HmPIMNeighborAddress_Object=MibTableColumn
hmPIMNeighborAddress=_HmPIMNeighborAddress_Object((1,3,6,1,4,1,248,15,4,99,1,1,3,1,1),_HmPIMNeighborAddress_Type())
hmPIMNeighborAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPIMNeighborAddress.setStatus(_B)
_HmPIMNeighborIfIndex_Type=InterfaceIndex
_HmPIMNeighborIfIndex_Object=MibTableColumn
hmPIMNeighborIfIndex=_HmPIMNeighborIfIndex_Object((1,3,6,1,4,1,248,15,4,99,1,1,3,1,2),_HmPIMNeighborIfIndex_Type())
hmPIMNeighborIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMNeighborIfIndex.setStatus(_B)
_HmPIMNeighborUpTime_Type=TimeTicks
_HmPIMNeighborUpTime_Object=MibTableColumn
hmPIMNeighborUpTime=_HmPIMNeighborUpTime_Object((1,3,6,1,4,1,248,15,4,99,1,1,3,1,3),_HmPIMNeighborUpTime_Type())
hmPIMNeighborUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMNeighborUpTime.setStatus(_B)
_HmPIMNeighborExpiryTime_Type=TimeTicks
_HmPIMNeighborExpiryTime_Object=MibTableColumn
hmPIMNeighborExpiryTime=_HmPIMNeighborExpiryTime_Object((1,3,6,1,4,1,248,15,4,99,1,1,3,1,4),_HmPIMNeighborExpiryTime_Type())
hmPIMNeighborExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMNeighborExpiryTime.setStatus(_B)
class _HmPIMNeighborMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dense',1),(_d,2)))
_HmPIMNeighborMode_Type.__name__=_D
_HmPIMNeighborMode_Object=MibTableColumn
hmPIMNeighborMode=_HmPIMNeighborMode_Object((1,3,6,1,4,1,248,15,4,99,1,1,3,1,5),_HmPIMNeighborMode_Type())
hmPIMNeighborMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMNeighborMode.setStatus(_F)
_HmPIMIpMRouteTable_Object=MibTable
hmPIMIpMRouteTable=_HmPIMIpMRouteTable_Object((1,3,6,1,4,1,248,15,4,99,1,1,4))
if mibBuilder.loadTexts:hmPIMIpMRouteTable.setStatus(_B)
_HmPIMIpMRouteEntry_Object=MibTableRow
hmPIMIpMRouteEntry=_HmPIMIpMRouteEntry_Object((1,3,6,1,4,1,248,15,4,99,1,1,4,1))
hmPIMIpMRouteEntry.setIndexNames((0,_H,_U),(0,_H,_a),(0,_H,_b))
if mibBuilder.loadTexts:hmPIMIpMRouteEntry.setStatus(_B)
_HmPIMIpMRouteUpstreamAssertTimer_Type=TimeTicks
_HmPIMIpMRouteUpstreamAssertTimer_Object=MibTableColumn
hmPIMIpMRouteUpstreamAssertTimer=_HmPIMIpMRouteUpstreamAssertTimer_Object((1,3,6,1,4,1,248,15,4,99,1,1,4,1,1),_HmPIMIpMRouteUpstreamAssertTimer_Type())
hmPIMIpMRouteUpstreamAssertTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMIpMRouteUpstreamAssertTimer.setStatus(_B)
_HmPIMIpMRouteAssertMetric_Type=Integer32
_HmPIMIpMRouteAssertMetric_Object=MibTableColumn
hmPIMIpMRouteAssertMetric=_HmPIMIpMRouteAssertMetric_Object((1,3,6,1,4,1,248,15,4,99,1,1,4,1,2),_HmPIMIpMRouteAssertMetric_Type())
hmPIMIpMRouteAssertMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMIpMRouteAssertMetric.setStatus(_B)
_HmPIMIpMRouteAssertMetricPref_Type=Integer32
_HmPIMIpMRouteAssertMetricPref_Object=MibTableColumn
hmPIMIpMRouteAssertMetricPref=_HmPIMIpMRouteAssertMetricPref_Object((1,3,6,1,4,1,248,15,4,99,1,1,4,1,3),_HmPIMIpMRouteAssertMetricPref_Type())
hmPIMIpMRouteAssertMetricPref.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMIpMRouteAssertMetricPref.setStatus(_B)
_HmPIMIpMRouteAssertRPTBit_Type=TruthValue
_HmPIMIpMRouteAssertRPTBit_Object=MibTableColumn
hmPIMIpMRouteAssertRPTBit=_HmPIMIpMRouteAssertRPTBit_Object((1,3,6,1,4,1,248,15,4,99,1,1,4,1,4),_HmPIMIpMRouteAssertRPTBit_Type())
hmPIMIpMRouteAssertRPTBit.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMIpMRouteAssertRPTBit.setStatus(_B)
class _HmPIMIpMRouteFlags_Type(Bits):namedValues=NamedValues(*(('rpt',0),('spt',1)))
_HmPIMIpMRouteFlags_Type.__name__='Bits'
_HmPIMIpMRouteFlags_Object=MibTableColumn
hmPIMIpMRouteFlags=_HmPIMIpMRouteFlags_Object((1,3,6,1,4,1,248,15,4,99,1,1,4,1,5),_HmPIMIpMRouteFlags_Type())
hmPIMIpMRouteFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMIpMRouteFlags.setStatus(_B)
_HmPIMRPTable_Object=MibTable
hmPIMRPTable=_HmPIMRPTable_Object((1,3,6,1,4,1,248,15,4,99,1,1,5))
if mibBuilder.loadTexts:hmPIMRPTable.setStatus(_F)
_HmPIMRPEntry_Object=MibTableRow
hmPIMRPEntry=_HmPIMRPEntry_Object((1,3,6,1,4,1,248,15,4,99,1,1,5,1))
hmPIMRPEntry.setIndexNames((0,_A,_f),(0,_A,_g))
if mibBuilder.loadTexts:hmPIMRPEntry.setStatus(_F)
_HmPIMRPGroupAddress_Type=IpAddress
_HmPIMRPGroupAddress_Object=MibTableColumn
hmPIMRPGroupAddress=_HmPIMRPGroupAddress_Object((1,3,6,1,4,1,248,15,4,99,1,1,5,1,1),_HmPIMRPGroupAddress_Type())
hmPIMRPGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPIMRPGroupAddress.setStatus(_F)
_HmPIMRPAddress_Type=IpAddress
_HmPIMRPAddress_Object=MibTableColumn
hmPIMRPAddress=_HmPIMRPAddress_Object((1,3,6,1,4,1,248,15,4,99,1,1,5,1,2),_HmPIMRPAddress_Type())
hmPIMRPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPIMRPAddress.setStatus(_F)
class _HmPIMRPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HmPIMRPState_Type.__name__=_D
_HmPIMRPState_Object=MibTableColumn
hmPIMRPState=_HmPIMRPState_Object((1,3,6,1,4,1,248,15,4,99,1,1,5,1,3),_HmPIMRPState_Type())
hmPIMRPState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMRPState.setStatus(_F)
_HmPIMRPStateTimer_Type=TimeTicks
_HmPIMRPStateTimer_Object=MibTableColumn
hmPIMRPStateTimer=_HmPIMRPStateTimer_Object((1,3,6,1,4,1,248,15,4,99,1,1,5,1,4),_HmPIMRPStateTimer_Type())
hmPIMRPStateTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMRPStateTimer.setStatus(_F)
_HmPIMRPLastChange_Type=TimeTicks
_HmPIMRPLastChange_Object=MibTableColumn
hmPIMRPLastChange=_HmPIMRPLastChange_Object((1,3,6,1,4,1,248,15,4,99,1,1,5,1,5),_HmPIMRPLastChange_Type())
hmPIMRPLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMRPLastChange.setStatus(_F)
_HmPIMRPRowStatus_Type=RowStatus
_HmPIMRPRowStatus_Object=MibTableColumn
hmPIMRPRowStatus=_HmPIMRPRowStatus_Object((1,3,6,1,4,1,248,15,4,99,1,1,5,1,6),_HmPIMRPRowStatus_Type())
hmPIMRPRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hmPIMRPRowStatus.setStatus(_F)
_HmPIMRPSetTable_Object=MibTable
hmPIMRPSetTable=_HmPIMRPSetTable_Object((1,3,6,1,4,1,248,15,4,99,1,1,6))
if mibBuilder.loadTexts:hmPIMRPSetTable.setStatus(_B)
_HmPIMRPSetEntry_Object=MibTableRow
hmPIMRPSetEntry=_HmPIMRPSetEntry_Object((1,3,6,1,4,1,248,15,4,99,1,1,6,1))
hmPIMRPSetEntry.setIndexNames((0,_A,_h),(0,_A,_i),(0,_A,_j),(0,_A,_k))
if mibBuilder.loadTexts:hmPIMRPSetEntry.setStatus(_B)
_HmPIMRPSetGroupAddress_Type=IpAddress
_HmPIMRPSetGroupAddress_Object=MibTableColumn
hmPIMRPSetGroupAddress=_HmPIMRPSetGroupAddress_Object((1,3,6,1,4,1,248,15,4,99,1,1,6,1,1),_HmPIMRPSetGroupAddress_Type())
hmPIMRPSetGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPIMRPSetGroupAddress.setStatus(_B)
_HmPIMRPSetGroupMask_Type=IpAddress
_HmPIMRPSetGroupMask_Object=MibTableColumn
hmPIMRPSetGroupMask=_HmPIMRPSetGroupMask_Object((1,3,6,1,4,1,248,15,4,99,1,1,6,1,2),_HmPIMRPSetGroupMask_Type())
hmPIMRPSetGroupMask.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPIMRPSetGroupMask.setStatus(_B)
_HmPIMRPSetAddress_Type=IpAddress
_HmPIMRPSetAddress_Object=MibTableColumn
hmPIMRPSetAddress=_HmPIMRPSetAddress_Object((1,3,6,1,4,1,248,15,4,99,1,1,6,1,3),_HmPIMRPSetAddress_Type())
hmPIMRPSetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPIMRPSetAddress.setStatus(_B)
class _HmPIMRPSetHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmPIMRPSetHoldTime_Type.__name__=_D
_HmPIMRPSetHoldTime_Object=MibTableColumn
hmPIMRPSetHoldTime=_HmPIMRPSetHoldTime_Object((1,3,6,1,4,1,248,15,4,99,1,1,6,1,4),_HmPIMRPSetHoldTime_Type())
hmPIMRPSetHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMRPSetHoldTime.setStatus(_B)
if mibBuilder.loadTexts:hmPIMRPSetHoldTime.setUnits(_I)
_HmPIMRPSetExpiryTime_Type=TimeTicks
_HmPIMRPSetExpiryTime_Object=MibTableColumn
hmPIMRPSetExpiryTime=_HmPIMRPSetExpiryTime_Object((1,3,6,1,4,1,248,15,4,99,1,1,6,1,5),_HmPIMRPSetExpiryTime_Type())
hmPIMRPSetExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMRPSetExpiryTime.setStatus(_B)
class _HmPIMRPSetComponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HmPIMRPSetComponent_Type.__name__=_D
_HmPIMRPSetComponent_Object=MibTableColumn
hmPIMRPSetComponent=_HmPIMRPSetComponent_Object((1,3,6,1,4,1,248,15,4,99,1,1,6,1,6),_HmPIMRPSetComponent_Type())
hmPIMRPSetComponent.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPIMRPSetComponent.setStatus(_B)
_HmPIMIpMRouteNextHopTable_Object=MibTable
hmPIMIpMRouteNextHopTable=_HmPIMIpMRouteNextHopTable_Object((1,3,6,1,4,1,248,15,4,99,1,1,7))
if mibBuilder.loadTexts:hmPIMIpMRouteNextHopTable.setStatus(_B)
_HmPIMIpMRouteNextHopEntry_Object=MibTableRow
hmPIMIpMRouteNextHopEntry=_HmPIMIpMRouteNextHopEntry_Object((1,3,6,1,4,1,248,15,4,99,1,1,7,1))
hmPIMIpMRouteNextHopEntry.setIndexNames((0,_H,_W),(0,_H,_Y),(0,_H,_Z),(0,_H,_X),(0,_H,_V))
if mibBuilder.loadTexts:hmPIMIpMRouteNextHopEntry.setStatus(_B)
class _HmPIMIpMRouteNextHopPruneReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('prune',2),('assert',3)))
_HmPIMIpMRouteNextHopPruneReason_Type.__name__=_D
_HmPIMIpMRouteNextHopPruneReason_Object=MibTableColumn
hmPIMIpMRouteNextHopPruneReason=_HmPIMIpMRouteNextHopPruneReason_Object((1,3,6,1,4,1,248,15,4,99,1,1,7,1,2),_HmPIMIpMRouteNextHopPruneReason_Type())
hmPIMIpMRouteNextHopPruneReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMIpMRouteNextHopPruneReason.setStatus(_B)
_HmPIMCandidateRPTable_Object=MibTable
hmPIMCandidateRPTable=_HmPIMCandidateRPTable_Object((1,3,6,1,4,1,248,15,4,99,1,1,11))
if mibBuilder.loadTexts:hmPIMCandidateRPTable.setStatus(_B)
_HmPIMCandidateRPEntry_Object=MibTableRow
hmPIMCandidateRPEntry=_HmPIMCandidateRPEntry_Object((1,3,6,1,4,1,248,15,4,99,1,1,11,1))
hmPIMCandidateRPEntry.setIndexNames((0,_A,_l),(0,_A,_m))
if mibBuilder.loadTexts:hmPIMCandidateRPEntry.setStatus(_B)
_HmPIMCandidateRPGroupAddress_Type=IpAddress
_HmPIMCandidateRPGroupAddress_Object=MibTableColumn
hmPIMCandidateRPGroupAddress=_HmPIMCandidateRPGroupAddress_Object((1,3,6,1,4,1,248,15,4,99,1,1,11,1,1),_HmPIMCandidateRPGroupAddress_Type())
hmPIMCandidateRPGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPIMCandidateRPGroupAddress.setStatus(_B)
_HmPIMCandidateRPGroupMask_Type=IpAddress
_HmPIMCandidateRPGroupMask_Object=MibTableColumn
hmPIMCandidateRPGroupMask=_HmPIMCandidateRPGroupMask_Object((1,3,6,1,4,1,248,15,4,99,1,1,11,1,2),_HmPIMCandidateRPGroupMask_Type())
hmPIMCandidateRPGroupMask.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPIMCandidateRPGroupMask.setStatus(_B)
_HmPIMCandidateRPAddress_Type=IpAddress
_HmPIMCandidateRPAddress_Object=MibTableColumn
hmPIMCandidateRPAddress=_HmPIMCandidateRPAddress_Object((1,3,6,1,4,1,248,15,4,99,1,1,11,1,3),_HmPIMCandidateRPAddress_Type())
hmPIMCandidateRPAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hmPIMCandidateRPAddress.setStatus(_B)
_HmPIMCandidateRPRowStatus_Type=RowStatus
_HmPIMCandidateRPRowStatus_Object=MibTableColumn
hmPIMCandidateRPRowStatus=_HmPIMCandidateRPRowStatus_Object((1,3,6,1,4,1,248,15,4,99,1,1,11,1,4),_HmPIMCandidateRPRowStatus_Type())
hmPIMCandidateRPRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hmPIMCandidateRPRowStatus.setStatus(_B)
_HmPIMComponentTable_Object=MibTable
hmPIMComponentTable=_HmPIMComponentTable_Object((1,3,6,1,4,1,248,15,4,99,1,1,12))
if mibBuilder.loadTexts:hmPIMComponentTable.setStatus(_B)
_HmPIMComponentEntry_Object=MibTableRow
hmPIMComponentEntry=_HmPIMComponentEntry_Object((1,3,6,1,4,1,248,15,4,99,1,1,12,1))
hmPIMComponentEntry.setIndexNames((0,_A,_n))
if mibBuilder.loadTexts:hmPIMComponentEntry.setStatus(_B)
class _HmPIMComponentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HmPIMComponentIndex_Type.__name__=_D
_HmPIMComponentIndex_Object=MibTableColumn
hmPIMComponentIndex=_HmPIMComponentIndex_Object((1,3,6,1,4,1,248,15,4,99,1,1,12,1,1),_HmPIMComponentIndex_Type())
hmPIMComponentIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPIMComponentIndex.setStatus(_B)
_HmPIMComponentBSRAddress_Type=IpAddress
_HmPIMComponentBSRAddress_Object=MibTableColumn
hmPIMComponentBSRAddress=_HmPIMComponentBSRAddress_Object((1,3,6,1,4,1,248,15,4,99,1,1,12,1,2),_HmPIMComponentBSRAddress_Type())
hmPIMComponentBSRAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMComponentBSRAddress.setStatus(_B)
_HmPIMComponentBSRExpiryTime_Type=TimeTicks
_HmPIMComponentBSRExpiryTime_Object=MibTableColumn
hmPIMComponentBSRExpiryTime=_HmPIMComponentBSRExpiryTime_Object((1,3,6,1,4,1,248,15,4,99,1,1,12,1,3),_HmPIMComponentBSRExpiryTime_Type())
hmPIMComponentBSRExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmPIMComponentBSRExpiryTime.setStatus(_B)
class _HmPIMComponentCRPHoldTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmPIMComponentCRPHoldTime_Type.__name__=_D
_HmPIMComponentCRPHoldTime_Object=MibTableColumn
hmPIMComponentCRPHoldTime=_HmPIMComponentCRPHoldTime_Object((1,3,6,1,4,1,248,15,4,99,1,1,12,1,4),_HmPIMComponentCRPHoldTime_Type())
hmPIMComponentCRPHoldTime.setMaxAccess(_G)
if mibBuilder.loadTexts:hmPIMComponentCRPHoldTime.setStatus(_B)
if mibBuilder.loadTexts:hmPIMComponentCRPHoldTime.setUnits(_I)
_HmPIMComponentStatus_Type=RowStatus
_HmPIMComponentStatus_Object=MibTableColumn
hmPIMComponentStatus=_HmPIMComponentStatus_Object((1,3,6,1,4,1,248,15,4,99,1,1,12,1,5),_HmPIMComponentStatus_Type())
hmPIMComponentStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hmPIMComponentStatus.setStatus(_B)
_HmPIMMIBConformance_ObjectIdentity=ObjectIdentity
hmPIMMIBConformance=_HmPIMMIBConformance_ObjectIdentity((1,3,6,1,4,1,248,15,4,99,2))
_HmPIMMIBCompliances_ObjectIdentity=ObjectIdentity
hmPIMMIBCompliances=_HmPIMMIBCompliances_ObjectIdentity((1,3,6,1,4,1,248,15,4,99,2,1))
_HmPIMMIBGroups_ObjectIdentity=ObjectIdentity
hmPIMMIBGroups=_HmPIMMIBGroups_ObjectIdentity((1,3,6,1,4,1,248,15,4,99,2,2))
hmPIMV2MIBGroup=ObjectGroup((1,3,6,1,4,1,248,15,4,99,2,2,2))
hmPIMV2MIBGroup.setObjects(*((_A,_S),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_T),(_A,_o),(_A,_R),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:hmPIMV2MIBGroup.setStatus(_B)
hmPIMV2CandidateRPMIBGroup=ObjectGroup((1,3,6,1,4,1,248,15,4,99,2,2,3))
hmPIMV2CandidateRPMIBGroup.setObjects(*((_A,_x),(_A,_y)))
if mibBuilder.loadTexts:hmPIMV2CandidateRPMIBGroup.setStatus(_B)
hmPIMV1MIBGroup=ObjectGroup((1,3,6,1,4,1,248,15,4,99,2,2,4))
hmPIMV1MIBGroup.setObjects(*((_A,_S),(_A,_J),(_A,_K),(_A,_L),(_A,_z),(_A,_M),(_A,_N),(_A,_T),(_A,_Q),(_A,_R),(_A,_O),(_A,_P),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:hmPIMV1MIBGroup.setStatus(_F)
hmPIMDenseV2MIBGroup=ObjectGroup((1,3,6,1,4,1,248,15,4,99,2,2,5))
hmPIMDenseV2MIBGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:hmPIMDenseV2MIBGroup.setStatus(_B)
hmPIMNextHopGroup=ObjectGroup((1,3,6,1,4,1,248,15,4,99,2,2,6))
hmPIMNextHopGroup.setObjects((_A,_A4))
if mibBuilder.loadTexts:hmPIMNextHopGroup.setStatus(_B)
hmPIMAssertGroup=ObjectGroup((1,3,6,1,4,1,248,15,4,99,2,2,7))
hmPIMAssertGroup.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:hmPIMAssertGroup.setStatus(_B)
hmPIMNeighborLoss=NotificationType((1,3,6,1,4,1,248,15,4,99,1,0,1))
hmPIMNeighborLoss.setObjects((_A,_J))
if mibBuilder.loadTexts:hmPIMNeighborLoss.setStatus(_B)
hmPIMNotificationGroup=NotificationGroup((1,3,6,1,4,1,248,15,4,99,2,2,1))
hmPIMNotificationGroup.setObjects((_A,_A8))
if mibBuilder.loadTexts:hmPIMNotificationGroup.setStatus(_B)
hmPIMV1MIBCompliance=ModuleCompliance((1,3,6,1,4,1,248,15,4,99,2,1,1))
hmPIMV1MIBCompliance.setObjects((_A,_A9))
if mibBuilder.loadTexts:hmPIMV1MIBCompliance.setStatus(_F)
hmPIMSparseV2MIBCompliance=ModuleCompliance((1,3,6,1,4,1,248,15,4,99,2,1,2))
hmPIMSparseV2MIBCompliance.setObjects(*((_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:hmPIMSparseV2MIBCompliance.setStatus(_B)
hmPIMDenseV2MIBCompliance=ModuleCompliance((1,3,6,1,4,1,248,15,4,99,2,1,3))
hmPIMDenseV2MIBCompliance.setObjects((_A,_AC))
if mibBuilder.loadTexts:hmPIMDenseV2MIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hmPIMMIB':hmPIMMIB,'hmPIMMIBObjects':hmPIMMIBObjects,'hmPIMTraps':hmPIMTraps,_A8:hmPIMNeighborLoss,'hmPIM':hmPIM,_S:hmPIMJoinPruneInterval,'hmPIMInterfaceTable':hmPIMInterfaceTable,'hmPIMInterfaceEntry':hmPIMInterfaceEntry,_c:hmPIMInterfaceIfIndex,_M:hmPIMInterfaceAddress,_N:hmPIMInterfaceNetMask,_R:hmPIMInterfaceMode,_O:hmPIMInterfaceDR,_P:hmPIMInterfaceHelloInterval,_Q:hmPIMInterfaceStatus,_T:hmPIMInterfaceJoinPruneInterval,_o:hmPIMInterfaceCBSRPreference,'hmPIMNeighborTable':hmPIMNeighborTable,'hmPIMNeighborEntry':hmPIMNeighborEntry,_e:hmPIMNeighborAddress,_J:hmPIMNeighborIfIndex,_K:hmPIMNeighborUpTime,_L:hmPIMNeighborExpiryTime,_z:hmPIMNeighborMode,'hmPIMIpMRouteTable':hmPIMIpMRouteTable,'hmPIMIpMRouteEntry':hmPIMIpMRouteEntry,_w:hmPIMIpMRouteUpstreamAssertTimer,_A5:hmPIMIpMRouteAssertMetric,_A6:hmPIMIpMRouteAssertMetricPref,_A7:hmPIMIpMRouteAssertRPTBit,_v:hmPIMIpMRouteFlags,'hmPIMRPTable':hmPIMRPTable,'hmPIMRPEntry':hmPIMRPEntry,_f:hmPIMRPGroupAddress,_g:hmPIMRPAddress,_A0:hmPIMRPState,_A1:hmPIMRPStateTimer,_A2:hmPIMRPLastChange,_A3:hmPIMRPRowStatus,'hmPIMRPSetTable':hmPIMRPSetTable,'hmPIMRPSetEntry':hmPIMRPSetEntry,_i:hmPIMRPSetGroupAddress,_j:hmPIMRPSetGroupMask,_k:hmPIMRPSetAddress,_p:hmPIMRPSetHoldTime,_q:hmPIMRPSetExpiryTime,_h:hmPIMRPSetComponent,'hmPIMIpMRouteNextHopTable':hmPIMIpMRouteNextHopTable,'hmPIMIpMRouteNextHopEntry':hmPIMIpMRouteNextHopEntry,_A4:hmPIMIpMRouteNextHopPruneReason,'hmPIMCandidateRPTable':hmPIMCandidateRPTable,'hmPIMCandidateRPEntry':hmPIMCandidateRPEntry,_l:hmPIMCandidateRPGroupAddress,_m:hmPIMCandidateRPGroupMask,_x:hmPIMCandidateRPAddress,_y:hmPIMCandidateRPRowStatus,'hmPIMComponentTable':hmPIMComponentTable,'hmPIMComponentEntry':hmPIMComponentEntry,_n:hmPIMComponentIndex,_r:hmPIMComponentBSRAddress,_s:hmPIMComponentBSRExpiryTime,_t:hmPIMComponentCRPHoldTime,_u:hmPIMComponentStatus,'hmPIMMIBConformance':hmPIMMIBConformance,'hmPIMMIBCompliances':hmPIMMIBCompliances,'hmPIMV1MIBCompliance':hmPIMV1MIBCompliance,'hmPIMSparseV2MIBCompliance':hmPIMSparseV2MIBCompliance,'hmPIMDenseV2MIBCompliance':hmPIMDenseV2MIBCompliance,'hmPIMMIBGroups':hmPIMMIBGroups,'hmPIMNotificationGroup':hmPIMNotificationGroup,_AA:hmPIMV2MIBGroup,_AB:hmPIMV2CandidateRPMIBGroup,_A9:hmPIMV1MIBGroup,_AC:hmPIMDenseV2MIBGroup,'hmPIMNextHopGroup':hmPIMNextHopGroup,'hmPIMAssertGroup':hmPIMAssertGroup})