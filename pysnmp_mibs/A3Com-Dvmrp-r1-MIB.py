_e='a3ComDvmrpNbrRouterIpAddr'
_d='a3ComDvmrpNbrRouterPort'
_c='a3ComDvmrpForwardGroup'
_b='a3ComDvmrpForwardSource'
_a='a3ComDvmrpRouteSource'
_Z='a3ComDvmrpDestGroupIpMask'
_Y='a3ComDvmrpDestGroupIpAddr'
_X='a3ComDvmrpAggreRangeIpMask'
_W='a3ComDvmrpAggreRangeIpAddr'
_V='a3ComDvmrpAggreExceptIpMask'
_U='a3ComDvmrpAggreExceptIpAddr'
_T='a3ComDvmrpTunnelId'
_S='a3ComDvmrpNeighborAddr'
_R='a3ComDvmrpNeighborType'
_Q='a3ComDvmrpNeighborPort'
_P='reject'
_O='a3ComDvmrpMospfIpMask'
_N='a3ComDvmrpMospfIpAddr'
_M='a3ComDvmrpBoundaryAddrIpAddr'
_L='a3ComDvmrpBoundaryAddrPort'
_K='a3ComDvmrpPortIndex'
_J='other'
_I='disabled'
_H='enabled'
_G='no'
_F='yes'
_E='A3Com-Dvmrp-r1-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class RowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('active',1),('notInService',2),('notReady',3),('createAndGo',4),('createAndWait',5),('destroy',6)))
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_BrouterMIB_ObjectIdentity=ObjectIdentity
brouterMIB=_BrouterMIB_ObjectIdentity((1,3,6,1,4,1,43,2))
_A3ComDVMRP_ObjectIdentity=ObjectIdentity
a3ComDVMRP=_A3ComDVMRP_ObjectIdentity((1,3,6,1,4,1,43,2,28))
_A3ComDvmrpSConfig_ObjectIdentity=ObjectIdentity
a3ComDvmrpSConfig=_A3ComDvmrpSConfig_ObjectIdentity((1,3,6,1,4,1,43,2,28,1))
class _A3ComDvmrpCacheTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,86400))
_A3ComDvmrpCacheTime_Type.__name__=_D
_A3ComDvmrpCacheTime_Object=MibScalar
a3ComDvmrpCacheTime=_A3ComDvmrpCacheTime_Object((1,3,6,1,4,1,43,2,28,1,1),_A3ComDvmrpCacheTime_Type())
a3ComDvmrpCacheTime.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpCacheTime.setStatus(_A)
class _A3ComDvmrpPrune_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_A3ComDvmrpPrune_Type.__name__=_D
_A3ComDvmrpPrune_Object=MibScalar
a3ComDvmrpPrune=_A3ComDvmrpPrune_Object((1,3,6,1,4,1,43,2,28,1,2),_A3ComDvmrpPrune_Type())
a3ComDvmrpPrune.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpPrune.setStatus(_A)
class _A3ComDvmrpUpdateTime_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,5400))
_A3ComDvmrpUpdateTime_Type.__name__=_D
_A3ComDvmrpUpdateTime_Object=MibScalar
a3ComDvmrpUpdateTime=_A3ComDvmrpUpdateTime_Object((1,3,6,1,4,1,43,2,28,1,3),_A3ComDvmrpUpdateTime_Type())
a3ComDvmrpUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpUpdateTime.setStatus(_A)
class _A3ComDvmrpMospfPolicy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mospf',1),('noMospf',2)))
_A3ComDvmrpMospfPolicy_Type.__name__=_D
_A3ComDvmrpMospfPolicy_Object=MibScalar
a3ComDvmrpMospfPolicy=_A3ComDvmrpMospfPolicy_Object((1,3,6,1,4,1,43,2,28,1,4),_A3ComDvmrpMospfPolicy_Type())
a3ComDvmrpMospfPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpMospfPolicy.setStatus(_A)
class _A3ComDvmrpDestGroupPolicy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('destGroup',1),('noDestGroup',2)))
_A3ComDvmrpDestGroupPolicy_Type.__name__=_D
_A3ComDvmrpDestGroupPolicy_Object=MibScalar
a3ComDvmrpDestGroupPolicy=_A3ComDvmrpDestGroupPolicy_Object((1,3,6,1,4,1,43,2,28,1,5),_A3ComDvmrpDestGroupPolicy_Type())
a3ComDvmrpDestGroupPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpDestGroupPolicy.setStatus(_A)
_A3ComDvmrpCConfig_ObjectIdentity=ObjectIdentity
a3ComDvmrpCConfig=_A3ComDvmrpCConfig_ObjectIdentity((1,3,6,1,4,1,43,2,28,2))
_A3ComDvmrpPortTable_Object=MibTable
a3ComDvmrpPortTable=_A3ComDvmrpPortTable_Object((1,3,6,1,4,1,43,2,28,2,1))
if mibBuilder.loadTexts:a3ComDvmrpPortTable.setStatus(_A)
_A3ComDvmrpPortEntry_Object=MibTableRow
a3ComDvmrpPortEntry=_A3ComDvmrpPortEntry_Object((1,3,6,1,4,1,43,2,28,2,1,1))
a3ComDvmrpPortEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:a3ComDvmrpPortEntry.setStatus(_A)
_A3ComDvmrpPortIndex_Type=Integer32
_A3ComDvmrpPortIndex_Object=MibTableColumn
a3ComDvmrpPortIndex=_A3ComDvmrpPortIndex_Object((1,3,6,1,4,1,43,2,28,2,1,1,1),_A3ComDvmrpPortIndex_Type())
a3ComDvmrpPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpPortIndex.setStatus(_A)
class _A3ComDvmrpPortControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_A3ComDvmrpPortControl_Type.__name__=_D
_A3ComDvmrpPortControl_Object=MibTableColumn
a3ComDvmrpPortControl=_A3ComDvmrpPortControl_Object((1,3,6,1,4,1,43,2,28,2,1,1,2),_A3ComDvmrpPortControl_Type())
a3ComDvmrpPortControl.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpPortControl.setStatus(_A)
class _A3ComDvmrpPortMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_A3ComDvmrpPortMetric_Type.__name__=_D
_A3ComDvmrpPortMetric_Object=MibTableColumn
a3ComDvmrpPortMetric=_A3ComDvmrpPortMetric_Object((1,3,6,1,4,1,43,2,28,2,1,1,3),_A3ComDvmrpPortMetric_Type())
a3ComDvmrpPortMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpPortMetric.setStatus(_A)
class _A3ComDvmrpPortRateLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_A3ComDvmrpPortRateLimit_Type.__name__=_D
_A3ComDvmrpPortRateLimit_Object=MibTableColumn
a3ComDvmrpPortRateLimit=_A3ComDvmrpPortRateLimit_Object((1,3,6,1,4,1,43,2,28,2,1,1,4),_A3ComDvmrpPortRateLimit_Type())
a3ComDvmrpPortRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpPortRateLimit.setStatus(_A)
class _A3ComDvmrpPortAggregateCtrl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_A3ComDvmrpPortAggregateCtrl_Type.__name__=_D
_A3ComDvmrpPortAggregateCtrl_Object=MibTableColumn
a3ComDvmrpPortAggregateCtrl=_A3ComDvmrpPortAggregateCtrl_Object((1,3,6,1,4,1,43,2,28,2,1,1,5),_A3ComDvmrpPortAggregateCtrl_Type())
a3ComDvmrpPortAggregateCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpPortAggregateCtrl.setStatus(_A)
_A3ComDvmrpBoundaryAddrTable_Object=MibTable
a3ComDvmrpBoundaryAddrTable=_A3ComDvmrpBoundaryAddrTable_Object((1,3,6,1,4,1,43,2,28,2,2))
if mibBuilder.loadTexts:a3ComDvmrpBoundaryAddrTable.setStatus(_A)
_A3ComDvmrpBoundaryAddrEntry_Object=MibTableRow
a3ComDvmrpBoundaryAddrEntry=_A3ComDvmrpBoundaryAddrEntry_Object((1,3,6,1,4,1,43,2,28,2,2,1))
a3ComDvmrpBoundaryAddrEntry.setIndexNames((0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:a3ComDvmrpBoundaryAddrEntry.setStatus(_A)
_A3ComDvmrpBoundaryAddrPort_Type=Integer32
_A3ComDvmrpBoundaryAddrPort_Object=MibTableColumn
a3ComDvmrpBoundaryAddrPort=_A3ComDvmrpBoundaryAddrPort_Object((1,3,6,1,4,1,43,2,28,2,2,1,1),_A3ComDvmrpBoundaryAddrPort_Type())
a3ComDvmrpBoundaryAddrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpBoundaryAddrPort.setStatus(_A)
_A3ComDvmrpBoundaryAddrIpAddr_Type=IpAddress
_A3ComDvmrpBoundaryAddrIpAddr_Object=MibTableColumn
a3ComDvmrpBoundaryAddrIpAddr=_A3ComDvmrpBoundaryAddrIpAddr_Object((1,3,6,1,4,1,43,2,28,2,2,1,2),_A3ComDvmrpBoundaryAddrIpAddr_Type())
a3ComDvmrpBoundaryAddrIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpBoundaryAddrIpAddr.setStatus(_A)
_A3ComDvmrpBoundaryAddrMask_Type=IpAddress
_A3ComDvmrpBoundaryAddrMask_Object=MibTableColumn
a3ComDvmrpBoundaryAddrMask=_A3ComDvmrpBoundaryAddrMask_Object((1,3,6,1,4,1,43,2,28,2,2,1,3),_A3ComDvmrpBoundaryAddrMask_Type())
a3ComDvmrpBoundaryAddrMask.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpBoundaryAddrMask.setStatus(_A)
_A3ComDvmrpBoundaryAddrStatus_Type=RowStatus
_A3ComDvmrpBoundaryAddrStatus_Object=MibTableColumn
a3ComDvmrpBoundaryAddrStatus=_A3ComDvmrpBoundaryAddrStatus_Object((1,3,6,1,4,1,43,2,28,2,2,1,4),_A3ComDvmrpBoundaryAddrStatus_Type())
a3ComDvmrpBoundaryAddrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpBoundaryAddrStatus.setStatus(_A)
_A3ComDvmrpMospfTable_Object=MibTable
a3ComDvmrpMospfTable=_A3ComDvmrpMospfTable_Object((1,3,6,1,4,1,43,2,28,2,3))
if mibBuilder.loadTexts:a3ComDvmrpMospfTable.setStatus(_A)
_A3ComDvmrpMospfEntry_Object=MibTableRow
a3ComDvmrpMospfEntry=_A3ComDvmrpMospfEntry_Object((1,3,6,1,4,1,43,2,28,2,3,1))
a3ComDvmrpMospfEntry.setIndexNames((0,_E,_N),(0,_E,_O))
if mibBuilder.loadTexts:a3ComDvmrpMospfEntry.setStatus(_A)
_A3ComDvmrpMospfIpAddr_Type=IpAddress
_A3ComDvmrpMospfIpAddr_Object=MibTableColumn
a3ComDvmrpMospfIpAddr=_A3ComDvmrpMospfIpAddr_Object((1,3,6,1,4,1,43,2,28,2,3,1,1),_A3ComDvmrpMospfIpAddr_Type())
a3ComDvmrpMospfIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpMospfIpAddr.setStatus(_A)
_A3ComDvmrpMospfIpMask_Type=Integer32
_A3ComDvmrpMospfIpMask_Object=MibTableColumn
a3ComDvmrpMospfIpMask=_A3ComDvmrpMospfIpMask_Object((1,3,6,1,4,1,43,2,28,2,3,1,2),_A3ComDvmrpMospfIpMask_Type())
a3ComDvmrpMospfIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpMospfIpMask.setStatus(_A)
class _A3ComDvmrpMospfMetric_Type(Integer32):defaultValue=1
_A3ComDvmrpMospfMetric_Type.__name__=_D
_A3ComDvmrpMospfMetric_Object=MibTableColumn
a3ComDvmrpMospfMetric=_A3ComDvmrpMospfMetric_Object((1,3,6,1,4,1,43,2,28,2,3,1,3),_A3ComDvmrpMospfMetric_Type())
a3ComDvmrpMospfMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpMospfMetric.setStatus(_A)
class _A3ComDvmrpMospfAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('aggregate',1),('individual',2),(_P,3)))
_A3ComDvmrpMospfAction_Type.__name__=_D
_A3ComDvmrpMospfAction_Object=MibTableColumn
a3ComDvmrpMospfAction=_A3ComDvmrpMospfAction_Object((1,3,6,1,4,1,43,2,28,2,3,1,4),_A3ComDvmrpMospfAction_Type())
a3ComDvmrpMospfAction.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpMospfAction.setStatus(_A)
_A3ComDvmrpMospfStatus_Type=RowStatus
_A3ComDvmrpMospfStatus_Object=MibTableColumn
a3ComDvmrpMospfStatus=_A3ComDvmrpMospfStatus_Object((1,3,6,1,4,1,43,2,28,2,3,1,5),_A3ComDvmrpMospfStatus_Type())
a3ComDvmrpMospfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpMospfStatus.setStatus(_A)
_A3ComDvmrpNeighborTable_Object=MibTable
a3ComDvmrpNeighborTable=_A3ComDvmrpNeighborTable_Object((1,3,6,1,4,1,43,2,28,2,4))
if mibBuilder.loadTexts:a3ComDvmrpNeighborTable.setStatus(_A)
_A3ComDvmrpNeighborEntry_Object=MibTableRow
a3ComDvmrpNeighborEntry=_A3ComDvmrpNeighborEntry_Object((1,3,6,1,4,1,43,2,28,2,4,1))
a3ComDvmrpNeighborEntry.setIndexNames((0,_E,_Q),(0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:a3ComDvmrpNeighborEntry.setStatus(_A)
_A3ComDvmrpNeighborPort_Type=Integer32
_A3ComDvmrpNeighborPort_Object=MibTableColumn
a3ComDvmrpNeighborPort=_A3ComDvmrpNeighborPort_Object((1,3,6,1,4,1,43,2,28,2,4,1,1),_A3ComDvmrpNeighborPort_Type())
a3ComDvmrpNeighborPort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpNeighborPort.setStatus(_A)
class _A3ComDvmrpNeighborType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*(('x25',2),('frame-relay',4)))
_A3ComDvmrpNeighborType_Type.__name__=_D
_A3ComDvmrpNeighborType_Object=MibTableColumn
a3ComDvmrpNeighborType=_A3ComDvmrpNeighborType_Object((1,3,6,1,4,1,43,2,28,2,4,1,2),_A3ComDvmrpNeighborType_Type())
a3ComDvmrpNeighborType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpNeighborType.setStatus(_A)
_A3ComDvmrpNeighborAddr_Type=PhysAddress
_A3ComDvmrpNeighborAddr_Object=MibTableColumn
a3ComDvmrpNeighborAddr=_A3ComDvmrpNeighborAddr_Object((1,3,6,1,4,1,43,2,28,2,4,1,3),_A3ComDvmrpNeighborAddr_Type())
a3ComDvmrpNeighborAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpNeighborAddr.setStatus(_A)
_A3ComDvmrpNeighborStatus_Type=RowStatus
_A3ComDvmrpNeighborStatus_Object=MibTableColumn
a3ComDvmrpNeighborStatus=_A3ComDvmrpNeighborStatus_Object((1,3,6,1,4,1,43,2,28,2,4,1,4),_A3ComDvmrpNeighborStatus_Type())
a3ComDvmrpNeighborStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpNeighborStatus.setStatus(_A)
_A3ComDvmrpTunnelTable_Object=MibTable
a3ComDvmrpTunnelTable=_A3ComDvmrpTunnelTable_Object((1,3,6,1,4,1,43,2,28,2,5))
if mibBuilder.loadTexts:a3ComDvmrpTunnelTable.setStatus(_A)
_A3ComDvmrpTunnelEntry_Object=MibTableRow
a3ComDvmrpTunnelEntry=_A3ComDvmrpTunnelEntry_Object((1,3,6,1,4,1,43,2,28,2,5,1))
a3ComDvmrpTunnelEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:a3ComDvmrpTunnelEntry.setStatus(_A)
_A3ComDvmrpTunnelId_Type=Integer32
_A3ComDvmrpTunnelId_Object=MibTableColumn
a3ComDvmrpTunnelId=_A3ComDvmrpTunnelId_Object((1,3,6,1,4,1,43,2,28,2,5,1,1),_A3ComDvmrpTunnelId_Type())
a3ComDvmrpTunnelId.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpTunnelId.setStatus(_A)
_A3ComDvmrpTunnelLocalIp_Type=IpAddress
_A3ComDvmrpTunnelLocalIp_Object=MibTableColumn
a3ComDvmrpTunnelLocalIp=_A3ComDvmrpTunnelLocalIp_Object((1,3,6,1,4,1,43,2,28,2,5,1,2),_A3ComDvmrpTunnelLocalIp_Type())
a3ComDvmrpTunnelLocalIp.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpTunnelLocalIp.setStatus(_A)
_A3ComDvmrpTunnelRemoteIp_Type=IpAddress
_A3ComDvmrpTunnelRemoteIp_Object=MibTableColumn
a3ComDvmrpTunnelRemoteIp=_A3ComDvmrpTunnelRemoteIp_Object((1,3,6,1,4,1,43,2,28,2,5,1,3),_A3ComDvmrpTunnelRemoteIp_Type())
a3ComDvmrpTunnelRemoteIp.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpTunnelRemoteIp.setStatus(_A)
class _A3ComDvmrpTunnelTtl_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A3ComDvmrpTunnelTtl_Type.__name__=_D
_A3ComDvmrpTunnelTtl_Object=MibTableColumn
a3ComDvmrpTunnelTtl=_A3ComDvmrpTunnelTtl_Object((1,3,6,1,4,1,43,2,28,2,5,1,4),_A3ComDvmrpTunnelTtl_Type())
a3ComDvmrpTunnelTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpTunnelTtl.setStatus(_A)
_A3ComDvmrpTunnelStatus_Type=RowStatus
_A3ComDvmrpTunnelStatus_Object=MibTableColumn
a3ComDvmrpTunnelStatus=_A3ComDvmrpTunnelStatus_Object((1,3,6,1,4,1,43,2,28,2,5,1,5),_A3ComDvmrpTunnelStatus_Type())
a3ComDvmrpTunnelStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpTunnelStatus.setStatus(_A)
_A3ComDvmrpAggreExceptTable_Object=MibTable
a3ComDvmrpAggreExceptTable=_A3ComDvmrpAggreExceptTable_Object((1,3,6,1,4,1,43,2,28,2,6))
if mibBuilder.loadTexts:a3ComDvmrpAggreExceptTable.setStatus(_A)
_A3ComDvmrpAggreExceptEntry_Object=MibTableRow
a3ComDvmrpAggreExceptEntry=_A3ComDvmrpAggreExceptEntry_Object((1,3,6,1,4,1,43,2,28,2,6,1))
a3ComDvmrpAggreExceptEntry.setIndexNames((0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:a3ComDvmrpAggreExceptEntry.setStatus(_A)
_A3ComDvmrpAggreExceptIpAddr_Type=IpAddress
_A3ComDvmrpAggreExceptIpAddr_Object=MibTableColumn
a3ComDvmrpAggreExceptIpAddr=_A3ComDvmrpAggreExceptIpAddr_Object((1,3,6,1,4,1,43,2,28,2,6,1,1),_A3ComDvmrpAggreExceptIpAddr_Type())
a3ComDvmrpAggreExceptIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpAggreExceptIpAddr.setStatus(_A)
class _A3ComDvmrpAggreExceptIpMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_A3ComDvmrpAggreExceptIpMask_Type.__name__=_D
_A3ComDvmrpAggreExceptIpMask_Object=MibTableColumn
a3ComDvmrpAggreExceptIpMask=_A3ComDvmrpAggreExceptIpMask_Object((1,3,6,1,4,1,43,2,28,2,6,1,2),_A3ComDvmrpAggreExceptIpMask_Type())
a3ComDvmrpAggreExceptIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpAggreExceptIpMask.setStatus(_A)
_A3ComDvmrpAggreExceptStatus_Type=RowStatus
_A3ComDvmrpAggreExceptStatus_Object=MibTableColumn
a3ComDvmrpAggreExceptStatus=_A3ComDvmrpAggreExceptStatus_Object((1,3,6,1,4,1,43,2,28,2,6,1,3),_A3ComDvmrpAggreExceptStatus_Type())
a3ComDvmrpAggreExceptStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpAggreExceptStatus.setStatus(_A)
_A3ComDvmrpAggreRangeTable_Object=MibTable
a3ComDvmrpAggreRangeTable=_A3ComDvmrpAggreRangeTable_Object((1,3,6,1,4,1,43,2,28,2,7))
if mibBuilder.loadTexts:a3ComDvmrpAggreRangeTable.setStatus(_A)
_A3ComDvmrpAggreRangeEntry_Object=MibTableRow
a3ComDvmrpAggreRangeEntry=_A3ComDvmrpAggreRangeEntry_Object((1,3,6,1,4,1,43,2,28,2,7,1))
a3ComDvmrpAggreRangeEntry.setIndexNames((0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:a3ComDvmrpAggreRangeEntry.setStatus(_A)
_A3ComDvmrpAggreRangeIpAddr_Type=IpAddress
_A3ComDvmrpAggreRangeIpAddr_Object=MibTableColumn
a3ComDvmrpAggreRangeIpAddr=_A3ComDvmrpAggreRangeIpAddr_Object((1,3,6,1,4,1,43,2,28,2,7,1,1),_A3ComDvmrpAggreRangeIpAddr_Type())
a3ComDvmrpAggreRangeIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpAggreRangeIpAddr.setStatus(_A)
class _A3ComDvmrpAggreRangeIpMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_A3ComDvmrpAggreRangeIpMask_Type.__name__=_D
_A3ComDvmrpAggreRangeIpMask_Object=MibTableColumn
a3ComDvmrpAggreRangeIpMask=_A3ComDvmrpAggreRangeIpMask_Object((1,3,6,1,4,1,43,2,28,2,7,1,2),_A3ComDvmrpAggreRangeIpMask_Type())
a3ComDvmrpAggreRangeIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpAggreRangeIpMask.setStatus(_A)
class _A3ComDvmrpAggreRangeMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_A3ComDvmrpAggreRangeMetric_Type.__name__=_D
_A3ComDvmrpAggreRangeMetric_Object=MibTableColumn
a3ComDvmrpAggreRangeMetric=_A3ComDvmrpAggreRangeMetric_Object((1,3,6,1,4,1,43,2,28,2,7,1,3),_A3ComDvmrpAggreRangeMetric_Type())
a3ComDvmrpAggreRangeMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpAggreRangeMetric.setStatus(_A)
_A3ComDvmrpAggreRangeStatus_Type=RowStatus
_A3ComDvmrpAggreRangeStatus_Object=MibTableColumn
a3ComDvmrpAggreRangeStatus=_A3ComDvmrpAggreRangeStatus_Object((1,3,6,1,4,1,43,2,28,2,7,1,4),_A3ComDvmrpAggreRangeStatus_Type())
a3ComDvmrpAggreRangeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpAggreRangeStatus.setStatus(_A)
_A3ComDvmrpDestGroupTable_Object=MibTable
a3ComDvmrpDestGroupTable=_A3ComDvmrpDestGroupTable_Object((1,3,6,1,4,1,43,2,28,2,8))
if mibBuilder.loadTexts:a3ComDvmrpDestGroupTable.setStatus(_A)
_A3ComDvmrpDestGroupEntry_Object=MibTableRow
a3ComDvmrpDestGroupEntry=_A3ComDvmrpDestGroupEntry_Object((1,3,6,1,4,1,43,2,28,2,8,1))
a3ComDvmrpDestGroupEntry.setIndexNames((0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:a3ComDvmrpDestGroupEntry.setStatus(_A)
_A3ComDvmrpDestGroupIpAddr_Type=IpAddress
_A3ComDvmrpDestGroupIpAddr_Object=MibTableColumn
a3ComDvmrpDestGroupIpAddr=_A3ComDvmrpDestGroupIpAddr_Object((1,3,6,1,4,1,43,2,28,2,8,1,1),_A3ComDvmrpDestGroupIpAddr_Type())
a3ComDvmrpDestGroupIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpDestGroupIpAddr.setStatus(_A)
_A3ComDvmrpDestGroupIpMask_Type=Integer32
_A3ComDvmrpDestGroupIpMask_Object=MibTableColumn
a3ComDvmrpDestGroupIpMask=_A3ComDvmrpDestGroupIpMask_Object((1,3,6,1,4,1,43,2,28,2,8,1,2),_A3ComDvmrpDestGroupIpMask_Type())
a3ComDvmrpDestGroupIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpDestGroupIpMask.setStatus(_A)
class _A3ComDvmrpDestGroupAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('accept',1),(_P,2)))
_A3ComDvmrpDestGroupAction_Type.__name__=_D
_A3ComDvmrpDestGroupAction_Object=MibTableColumn
a3ComDvmrpDestGroupAction=_A3ComDvmrpDestGroupAction_Object((1,3,6,1,4,1,43,2,28,2,8,1,3),_A3ComDvmrpDestGroupAction_Type())
a3ComDvmrpDestGroupAction.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpDestGroupAction.setStatus(_A)
_A3ComDvmrpDestGroupStatus_Type=RowStatus
_A3ComDvmrpDestGroupStatus_Object=MibTableColumn
a3ComDvmrpDestGroupStatus=_A3ComDvmrpDestGroupStatus_Object((1,3,6,1,4,1,43,2,28,2,8,1,4),_A3ComDvmrpDestGroupStatus_Type())
a3ComDvmrpDestGroupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDvmrpDestGroupStatus.setStatus(_A)
_A3ComDvmrpData_ObjectIdentity=ObjectIdentity
a3ComDvmrpData=_A3ComDvmrpData_ObjectIdentity((1,3,6,1,4,1,43,2,28,3))
_A3ComDvmrpRouteTable_Object=MibTable
a3ComDvmrpRouteTable=_A3ComDvmrpRouteTable_Object((1,3,6,1,4,1,43,2,28,3,1))
if mibBuilder.loadTexts:a3ComDvmrpRouteTable.setStatus(_A)
_A3ComDvmrpRouteEntry_Object=MibTableRow
a3ComDvmrpRouteEntry=_A3ComDvmrpRouteEntry_Object((1,3,6,1,4,1,43,2,28,3,1,1))
a3ComDvmrpRouteEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:a3ComDvmrpRouteEntry.setStatus(_A)
_A3ComDvmrpRouteSource_Type=IpAddress
_A3ComDvmrpRouteSource_Object=MibTableColumn
a3ComDvmrpRouteSource=_A3ComDvmrpRouteSource_Object((1,3,6,1,4,1,43,2,28,3,1,1,1),_A3ComDvmrpRouteSource_Type())
a3ComDvmrpRouteSource.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpRouteSource.setStatus(_A)
_A3ComDvmrpRouteMask_Type=IpAddress
_A3ComDvmrpRouteMask_Object=MibTableColumn
a3ComDvmrpRouteMask=_A3ComDvmrpRouteMask_Object((1,3,6,1,4,1,43,2,28,3,1,1,2),_A3ComDvmrpRouteMask_Type())
a3ComDvmrpRouteMask.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpRouteMask.setStatus(_A)
_A3ComDvmrpRoutePreHop_Type=IpAddress
_A3ComDvmrpRoutePreHop_Object=MibTableColumn
a3ComDvmrpRoutePreHop=_A3ComDvmrpRoutePreHop_Object((1,3,6,1,4,1,43,2,28,3,1,1,3),_A3ComDvmrpRoutePreHop_Type())
a3ComDvmrpRoutePreHop.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpRoutePreHop.setStatus(_A)
_A3ComDvmrpRouteMetric_Type=Integer32
_A3ComDvmrpRouteMetric_Object=MibTableColumn
a3ComDvmrpRouteMetric=_A3ComDvmrpRouteMetric_Object((1,3,6,1,4,1,43,2,28,3,1,1,4),_A3ComDvmrpRouteMetric_Type())
a3ComDvmrpRouteMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpRouteMetric.setStatus(_A)
_A3ComDvmrpRoutePort_Type=Integer32
_A3ComDvmrpRoutePort_Object=MibTableColumn
a3ComDvmrpRoutePort=_A3ComDvmrpRoutePort_Object((1,3,6,1,4,1,43,2,28,3,1,1,5),_A3ComDvmrpRoutePort_Type())
a3ComDvmrpRoutePort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpRoutePort.setStatus(_A)
class _A3ComDvmrpRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('direct',2),('remote',3)))
_A3ComDvmrpRouteType_Type.__name__=_D
_A3ComDvmrpRouteType_Object=MibTableColumn
a3ComDvmrpRouteType=_A3ComDvmrpRouteType_Object((1,3,6,1,4,1,43,2,28,3,1,1,6),_A3ComDvmrpRouteType_Type())
a3ComDvmrpRouteType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpRouteType.setStatus(_A)
class _A3ComDvmrpRouteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),('up',2),('down',3),('hold-down',4),('garbage-collection',5)))
_A3ComDvmrpRouteStatus_Type.__name__=_D
_A3ComDvmrpRouteStatus_Object=MibTableColumn
a3ComDvmrpRouteStatus=_A3ComDvmrpRouteStatus_Object((1,3,6,1,4,1,43,2,28,3,1,1,7),_A3ComDvmrpRouteStatus_Type())
a3ComDvmrpRouteStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpRouteStatus.setStatus(_A)
class _A3ComDvmrpRouteProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),('static',2),('dvmrp',3),('mospf',4),('cbt',5),('pim',6)))
_A3ComDvmrpRouteProtocol_Type.__name__=_D
_A3ComDvmrpRouteProtocol_Object=MibTableColumn
a3ComDvmrpRouteProtocol=_A3ComDvmrpRouteProtocol_Object((1,3,6,1,4,1,43,2,28,3,1,1,8),_A3ComDvmrpRouteProtocol_Type())
a3ComDvmrpRouteProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpRouteProtocol.setStatus(_A)
_A3ComDvmrpRouteTtl_Type=Integer32
_A3ComDvmrpRouteTtl_Object=MibTableColumn
a3ComDvmrpRouteTtl=_A3ComDvmrpRouteTtl_Object((1,3,6,1,4,1,43,2,28,3,1,1,9),_A3ComDvmrpRouteTtl_Type())
a3ComDvmrpRouteTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpRouteTtl.setStatus(_A)
_A3ComDvmrpRouteChild_Type=OctetString
_A3ComDvmrpRouteChild_Object=MibTableColumn
a3ComDvmrpRouteChild=_A3ComDvmrpRouteChild_Object((1,3,6,1,4,1,43,2,28,3,1,1,10),_A3ComDvmrpRouteChild_Type())
a3ComDvmrpRouteChild.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpRouteChild.setStatus(_A)
_A3ComDvmrpRouteChildTunnel_Type=OctetString
_A3ComDvmrpRouteChildTunnel_Object=MibTableColumn
a3ComDvmrpRouteChildTunnel=_A3ComDvmrpRouteChildTunnel_Object((1,3,6,1,4,1,43,2,28,3,1,1,11),_A3ComDvmrpRouteChildTunnel_Type())
a3ComDvmrpRouteChildTunnel.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpRouteChildTunnel.setStatus(_A)
_A3ComDvmrpRouteLeaf_Type=OctetString
_A3ComDvmrpRouteLeaf_Object=MibTableColumn
a3ComDvmrpRouteLeaf=_A3ComDvmrpRouteLeaf_Object((1,3,6,1,4,1,43,2,28,3,1,1,12),_A3ComDvmrpRouteLeaf_Type())
a3ComDvmrpRouteLeaf.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpRouteLeaf.setStatus(_A)
_A3ComDvmrpRouteLeafTunnel_Type=OctetString
_A3ComDvmrpRouteLeafTunnel_Object=MibTableColumn
a3ComDvmrpRouteLeafTunnel=_A3ComDvmrpRouteLeafTunnel_Object((1,3,6,1,4,1,43,2,28,3,1,1,13),_A3ComDvmrpRouteLeafTunnel_Type())
a3ComDvmrpRouteLeafTunnel.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpRouteLeafTunnel.setStatus(_A)
_A3ComDvmrpForwardTable_Object=MibTable
a3ComDvmrpForwardTable=_A3ComDvmrpForwardTable_Object((1,3,6,1,4,1,43,2,28,3,2))
if mibBuilder.loadTexts:a3ComDvmrpForwardTable.setStatus(_A)
_A3ComDvmrpForwardEntry_Object=MibTableRow
a3ComDvmrpForwardEntry=_A3ComDvmrpForwardEntry_Object((1,3,6,1,4,1,43,2,28,3,2,1))
a3ComDvmrpForwardEntry.setIndexNames((0,_E,_b),(0,_E,_c))
if mibBuilder.loadTexts:a3ComDvmrpForwardEntry.setStatus(_A)
_A3ComDvmrpForwardSource_Type=IpAddress
_A3ComDvmrpForwardSource_Object=MibTableColumn
a3ComDvmrpForwardSource=_A3ComDvmrpForwardSource_Object((1,3,6,1,4,1,43,2,28,3,2,1,1),_A3ComDvmrpForwardSource_Type())
a3ComDvmrpForwardSource.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpForwardSource.setStatus(_A)
_A3ComDvmrpForwardGroup_Type=IpAddress
_A3ComDvmrpForwardGroup_Object=MibTableColumn
a3ComDvmrpForwardGroup=_A3ComDvmrpForwardGroup_Object((1,3,6,1,4,1,43,2,28,3,2,1,2),_A3ComDvmrpForwardGroup_Type())
a3ComDvmrpForwardGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpForwardGroup.setStatus(_A)
_A3ComDvmrpForwardTtl_Type=Integer32
_A3ComDvmrpForwardTtl_Object=MibTableColumn
a3ComDvmrpForwardTtl=_A3ComDvmrpForwardTtl_Object((1,3,6,1,4,1,43,2,28,3,2,1,3),_A3ComDvmrpForwardTtl_Type())
a3ComDvmrpForwardTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpForwardTtl.setStatus(_A)
_A3ComDvmrpForwardInPort_Type=Integer32
_A3ComDvmrpForwardInPort_Object=MibTableColumn
a3ComDvmrpForwardInPort=_A3ComDvmrpForwardInPort_Object((1,3,6,1,4,1,43,2,28,3,2,1,4),_A3ComDvmrpForwardInPort_Type())
a3ComDvmrpForwardInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpForwardInPort.setStatus(_A)
_A3ComDvmrpForwardOutPorts_Type=OctetString
_A3ComDvmrpForwardOutPorts_Object=MibTableColumn
a3ComDvmrpForwardOutPorts=_A3ComDvmrpForwardOutPorts_Object((1,3,6,1,4,1,43,2,28,3,2,1,5),_A3ComDvmrpForwardOutPorts_Type())
a3ComDvmrpForwardOutPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpForwardOutPorts.setStatus(_A)
_A3ComDvmrpForwardOutPortsTunnel_Type=OctetString
_A3ComDvmrpForwardOutPortsTunnel_Object=MibTableColumn
a3ComDvmrpForwardOutPortsTunnel=_A3ComDvmrpForwardOutPortsTunnel_Object((1,3,6,1,4,1,43,2,28,3,2,1,6),_A3ComDvmrpForwardOutPortsTunnel_Type())
a3ComDvmrpForwardOutPortsTunnel.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpForwardOutPortsTunnel.setStatus(_A)
class _A3ComDvmrpForwardScoped_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_A3ComDvmrpForwardScoped_Type.__name__=_D
_A3ComDvmrpForwardScoped_Object=MibTableColumn
a3ComDvmrpForwardScoped=_A3ComDvmrpForwardScoped_Object((1,3,6,1,4,1,43,2,28,3,2,1,7),_A3ComDvmrpForwardScoped_Type())
a3ComDvmrpForwardScoped.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpForwardScoped.setStatus(_A)
class _A3ComDvmrpForwardPruneSent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_A3ComDvmrpForwardPruneSent_Type.__name__=_D
_A3ComDvmrpForwardPruneSent_Object=MibTableColumn
a3ComDvmrpForwardPruneSent=_A3ComDvmrpForwardPruneSent_Object((1,3,6,1,4,1,43,2,28,3,2,1,8),_A3ComDvmrpForwardPruneSent_Type())
a3ComDvmrpForwardPruneSent.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpForwardPruneSent.setStatus(_A)
_A3ComDvmrpNbrRouterTable_Object=MibTable
a3ComDvmrpNbrRouterTable=_A3ComDvmrpNbrRouterTable_Object((1,3,6,1,4,1,43,2,28,3,3))
if mibBuilder.loadTexts:a3ComDvmrpNbrRouterTable.setStatus(_A)
_A3ComDvmrpNbrRouterEntry_Object=MibTableRow
a3ComDvmrpNbrRouterEntry=_A3ComDvmrpNbrRouterEntry_Object((1,3,6,1,4,1,43,2,28,3,3,1))
a3ComDvmrpNbrRouterEntry.setIndexNames((0,_E,_d),(0,_E,_e))
if mibBuilder.loadTexts:a3ComDvmrpNbrRouterEntry.setStatus(_A)
_A3ComDvmrpNbrRouterPort_Type=Integer32
_A3ComDvmrpNbrRouterPort_Object=MibTableColumn
a3ComDvmrpNbrRouterPort=_A3ComDvmrpNbrRouterPort_Object((1,3,6,1,4,1,43,2,28,3,3,1,1),_A3ComDvmrpNbrRouterPort_Type())
a3ComDvmrpNbrRouterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpNbrRouterPort.setStatus(_A)
_A3ComDvmrpNbrRouterIpAddr_Type=IpAddress
_A3ComDvmrpNbrRouterIpAddr_Object=MibTableColumn
a3ComDvmrpNbrRouterIpAddr=_A3ComDvmrpNbrRouterIpAddr_Object((1,3,6,1,4,1,43,2,28,3,3,1,2),_A3ComDvmrpNbrRouterIpAddr_Type())
a3ComDvmrpNbrRouterIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpNbrRouterIpAddr.setStatus(_A)
_A3ComDvmrpNbrRouterGenId_Type=Integer32
_A3ComDvmrpNbrRouterGenId_Object=MibTableColumn
a3ComDvmrpNbrRouterGenId=_A3ComDvmrpNbrRouterGenId_Object((1,3,6,1,4,1,43,2,28,3,3,1,3),_A3ComDvmrpNbrRouterGenId_Type())
a3ComDvmrpNbrRouterGenId.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpNbrRouterGenId.setStatus(_A)
_A3ComDvmrpNbrRouterVerProtocol_Type=Integer32
_A3ComDvmrpNbrRouterVerProtocol_Object=MibTableColumn
a3ComDvmrpNbrRouterVerProtocol=_A3ComDvmrpNbrRouterVerProtocol_Object((1,3,6,1,4,1,43,2,28,3,3,1,4),_A3ComDvmrpNbrRouterVerProtocol_Type())
a3ComDvmrpNbrRouterVerProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpNbrRouterVerProtocol.setStatus(_A)
_A3ComDvmrpNbrRouterVerMrouted_Type=Integer32
_A3ComDvmrpNbrRouterVerMrouted_Object=MibTableColumn
a3ComDvmrpNbrRouterVerMrouted=_A3ComDvmrpNbrRouterVerMrouted_Object((1,3,6,1,4,1,43,2,28,3,3,1,5),_A3ComDvmrpNbrRouterVerMrouted_Type())
a3ComDvmrpNbrRouterVerMrouted.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpNbrRouterVerMrouted.setStatus(_A)
_A3ComDvmrpNbrRouterTtl_Type=Integer32
_A3ComDvmrpNbrRouterTtl_Object=MibTableColumn
a3ComDvmrpNbrRouterTtl=_A3ComDvmrpNbrRouterTtl_Object((1,3,6,1,4,1,43,2,28,3,3,1,6),_A3ComDvmrpNbrRouterTtl_Type())
a3ComDvmrpNbrRouterTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpNbrRouterTtl.setStatus(_A)
class _A3ComDvmrpNbrRouterLeafStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_A3ComDvmrpNbrRouterLeafStatus_Type.__name__=_D
_A3ComDvmrpNbrRouterLeafStatus_Object=MibTableColumn
a3ComDvmrpNbrRouterLeafStatus=_A3ComDvmrpNbrRouterLeafStatus_Object((1,3,6,1,4,1,43,2,28,3,3,1,7),_A3ComDvmrpNbrRouterLeafStatus_Type())
a3ComDvmrpNbrRouterLeafStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpNbrRouterLeafStatus.setStatus(_A)
class _A3ComDvmrpNbrRouterPruneStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_A3ComDvmrpNbrRouterPruneStatus_Type.__name__=_D
_A3ComDvmrpNbrRouterPruneStatus_Object=MibTableColumn
a3ComDvmrpNbrRouterPruneStatus=_A3ComDvmrpNbrRouterPruneStatus_Object((1,3,6,1,4,1,43,2,28,3,3,1,8),_A3ComDvmrpNbrRouterPruneStatus_Type())
a3ComDvmrpNbrRouterPruneStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpNbrRouterPruneStatus.setStatus(_A)
class _A3ComDvmrpNbrRouterGenIdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_A3ComDvmrpNbrRouterGenIdStatus_Type.__name__=_D
_A3ComDvmrpNbrRouterGenIdStatus_Object=MibTableColumn
a3ComDvmrpNbrRouterGenIdStatus=_A3ComDvmrpNbrRouterGenIdStatus_Object((1,3,6,1,4,1,43,2,28,3,3,1,9),_A3ComDvmrpNbrRouterGenIdStatus_Type())
a3ComDvmrpNbrRouterGenIdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpNbrRouterGenIdStatus.setStatus(_A)
class _A3ComDvmrpNbrRouterMtraceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_A3ComDvmrpNbrRouterMtraceStatus_Type.__name__=_D
_A3ComDvmrpNbrRouterMtraceStatus_Object=MibTableColumn
a3ComDvmrpNbrRouterMtraceStatus=_A3ComDvmrpNbrRouterMtraceStatus_Object((1,3,6,1,4,1,43,2,28,3,3,1,10),_A3ComDvmrpNbrRouterMtraceStatus_Type())
a3ComDvmrpNbrRouterMtraceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComDvmrpNbrRouterMtraceStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'RowStatus':RowStatus,'a3Com':a3Com,'brouterMIB':brouterMIB,'a3ComDVMRP':a3ComDVMRP,'a3ComDvmrpSConfig':a3ComDvmrpSConfig,'a3ComDvmrpCacheTime':a3ComDvmrpCacheTime,'a3ComDvmrpPrune':a3ComDvmrpPrune,'a3ComDvmrpUpdateTime':a3ComDvmrpUpdateTime,'a3ComDvmrpMospfPolicy':a3ComDvmrpMospfPolicy,'a3ComDvmrpDestGroupPolicy':a3ComDvmrpDestGroupPolicy,'a3ComDvmrpCConfig':a3ComDvmrpCConfig,'a3ComDvmrpPortTable':a3ComDvmrpPortTable,'a3ComDvmrpPortEntry':a3ComDvmrpPortEntry,_K:a3ComDvmrpPortIndex,'a3ComDvmrpPortControl':a3ComDvmrpPortControl,'a3ComDvmrpPortMetric':a3ComDvmrpPortMetric,'a3ComDvmrpPortRateLimit':a3ComDvmrpPortRateLimit,'a3ComDvmrpPortAggregateCtrl':a3ComDvmrpPortAggregateCtrl,'a3ComDvmrpBoundaryAddrTable':a3ComDvmrpBoundaryAddrTable,'a3ComDvmrpBoundaryAddrEntry':a3ComDvmrpBoundaryAddrEntry,_L:a3ComDvmrpBoundaryAddrPort,_M:a3ComDvmrpBoundaryAddrIpAddr,'a3ComDvmrpBoundaryAddrMask':a3ComDvmrpBoundaryAddrMask,'a3ComDvmrpBoundaryAddrStatus':a3ComDvmrpBoundaryAddrStatus,'a3ComDvmrpMospfTable':a3ComDvmrpMospfTable,'a3ComDvmrpMospfEntry':a3ComDvmrpMospfEntry,_N:a3ComDvmrpMospfIpAddr,_O:a3ComDvmrpMospfIpMask,'a3ComDvmrpMospfMetric':a3ComDvmrpMospfMetric,'a3ComDvmrpMospfAction':a3ComDvmrpMospfAction,'a3ComDvmrpMospfStatus':a3ComDvmrpMospfStatus,'a3ComDvmrpNeighborTable':a3ComDvmrpNeighborTable,'a3ComDvmrpNeighborEntry':a3ComDvmrpNeighborEntry,_Q:a3ComDvmrpNeighborPort,_R:a3ComDvmrpNeighborType,_S:a3ComDvmrpNeighborAddr,'a3ComDvmrpNeighborStatus':a3ComDvmrpNeighborStatus,'a3ComDvmrpTunnelTable':a3ComDvmrpTunnelTable,'a3ComDvmrpTunnelEntry':a3ComDvmrpTunnelEntry,_T:a3ComDvmrpTunnelId,'a3ComDvmrpTunnelLocalIp':a3ComDvmrpTunnelLocalIp,'a3ComDvmrpTunnelRemoteIp':a3ComDvmrpTunnelRemoteIp,'a3ComDvmrpTunnelTtl':a3ComDvmrpTunnelTtl,'a3ComDvmrpTunnelStatus':a3ComDvmrpTunnelStatus,'a3ComDvmrpAggreExceptTable':a3ComDvmrpAggreExceptTable,'a3ComDvmrpAggreExceptEntry':a3ComDvmrpAggreExceptEntry,_U:a3ComDvmrpAggreExceptIpAddr,_V:a3ComDvmrpAggreExceptIpMask,'a3ComDvmrpAggreExceptStatus':a3ComDvmrpAggreExceptStatus,'a3ComDvmrpAggreRangeTable':a3ComDvmrpAggreRangeTable,'a3ComDvmrpAggreRangeEntry':a3ComDvmrpAggreRangeEntry,_W:a3ComDvmrpAggreRangeIpAddr,_X:a3ComDvmrpAggreRangeIpMask,'a3ComDvmrpAggreRangeMetric':a3ComDvmrpAggreRangeMetric,'a3ComDvmrpAggreRangeStatus':a3ComDvmrpAggreRangeStatus,'a3ComDvmrpDestGroupTable':a3ComDvmrpDestGroupTable,'a3ComDvmrpDestGroupEntry':a3ComDvmrpDestGroupEntry,_Y:a3ComDvmrpDestGroupIpAddr,_Z:a3ComDvmrpDestGroupIpMask,'a3ComDvmrpDestGroupAction':a3ComDvmrpDestGroupAction,'a3ComDvmrpDestGroupStatus':a3ComDvmrpDestGroupStatus,'a3ComDvmrpData':a3ComDvmrpData,'a3ComDvmrpRouteTable':a3ComDvmrpRouteTable,'a3ComDvmrpRouteEntry':a3ComDvmrpRouteEntry,_a:a3ComDvmrpRouteSource,'a3ComDvmrpRouteMask':a3ComDvmrpRouteMask,'a3ComDvmrpRoutePreHop':a3ComDvmrpRoutePreHop,'a3ComDvmrpRouteMetric':a3ComDvmrpRouteMetric,'a3ComDvmrpRoutePort':a3ComDvmrpRoutePort,'a3ComDvmrpRouteType':a3ComDvmrpRouteType,'a3ComDvmrpRouteStatus':a3ComDvmrpRouteStatus,'a3ComDvmrpRouteProtocol':a3ComDvmrpRouteProtocol,'a3ComDvmrpRouteTtl':a3ComDvmrpRouteTtl,'a3ComDvmrpRouteChild':a3ComDvmrpRouteChild,'a3ComDvmrpRouteChildTunnel':a3ComDvmrpRouteChildTunnel,'a3ComDvmrpRouteLeaf':a3ComDvmrpRouteLeaf,'a3ComDvmrpRouteLeafTunnel':a3ComDvmrpRouteLeafTunnel,'a3ComDvmrpForwardTable':a3ComDvmrpForwardTable,'a3ComDvmrpForwardEntry':a3ComDvmrpForwardEntry,_b:a3ComDvmrpForwardSource,_c:a3ComDvmrpForwardGroup,'a3ComDvmrpForwardTtl':a3ComDvmrpForwardTtl,'a3ComDvmrpForwardInPort':a3ComDvmrpForwardInPort,'a3ComDvmrpForwardOutPorts':a3ComDvmrpForwardOutPorts,'a3ComDvmrpForwardOutPortsTunnel':a3ComDvmrpForwardOutPortsTunnel,'a3ComDvmrpForwardScoped':a3ComDvmrpForwardScoped,'a3ComDvmrpForwardPruneSent':a3ComDvmrpForwardPruneSent,'a3ComDvmrpNbrRouterTable':a3ComDvmrpNbrRouterTable,'a3ComDvmrpNbrRouterEntry':a3ComDvmrpNbrRouterEntry,_d:a3ComDvmrpNbrRouterPort,_e:a3ComDvmrpNbrRouterIpAddr,'a3ComDvmrpNbrRouterGenId':a3ComDvmrpNbrRouterGenId,'a3ComDvmrpNbrRouterVerProtocol':a3ComDvmrpNbrRouterVerProtocol,'a3ComDvmrpNbrRouterVerMrouted':a3ComDvmrpNbrRouterVerMrouted,'a3ComDvmrpNbrRouterTtl':a3ComDvmrpNbrRouterTtl,'a3ComDvmrpNbrRouterLeafStatus':a3ComDvmrpNbrRouterLeafStatus,'a3ComDvmrpNbrRouterPruneStatus':a3ComDvmrpNbrRouterPruneStatus,'a3ComDvmrpNbrRouterGenIdStatus':a3ComDvmrpNbrRouterGenIdStatus,'a3ComDvmrpNbrRouterMtraceStatus':a3ComDvmrpNbrRouterMtraceStatus})