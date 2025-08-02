_h='extremeEsrpDmnTrackedActivePortWeight'
_g='extremeEsrpDmnActivePortWeight'
_f='extremeEsrpDmnTrackedPings'
_e='extremeEsrpDmnTrackedIpRoutes'
_d='extremeEsrpDmnTrackedActivePorts'
_c='extremeEsrpDmnInternalActivePorts'
_b='extremeEsrpDmnActivePorts'
_a='extremeEsrpDmnMasterMacAddress'
_Z='extremeEsrpDmnNetAddress'
_Y='extremeEsrpDmnState'
_X='extremeEsrpAwareSelFwdListDmnGroup'
_W='extremeEsrpAwareSelFwdListDmnName'
_V='extremeEsrpVlanDescr'
_U='premaster'
_T='extremeEsrpPortIfIndex'
_S='extremeEsrpTrackIpRouteNetMask'
_R='extremeEsrpTrackIpRouteIpAddress'
_Q='extremeEsrpTrackVlanIfIndex'
_P='extremeEsrpNeighborMacAddress'
_O='extremeEsrpDmnGroup'
_N='accessible-for-notify'
_M='slave'
_L='neutral'
_K='master'
_J='extremeEsrpGroup'
_I='DisplayString'
_H='extremeEsrpVlanIfIndex'
_G='extremeEsrpDmnName'
_F='not-accessible'
_E='read-create'
_D='EXTREME-ESRP-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ExtremeGenAddr,PortList,extremeAgent=mibBuilder.importSymbols('EXTREME-BASE-MIB','ExtremeGenAddr','PortList','extremeAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
extremeEsrp=ModuleIdentity((1,3,6,1,4,1,1916,1,12))
_ExtremeEsrpTable_Object=MibTable
extremeEsrpTable=_ExtremeEsrpTable_Object((1,3,6,1,4,1,1916,1,12,2))
if mibBuilder.loadTexts:extremeEsrpTable.setStatus(_A)
_ExtremeEsrpEntry_Object=MibTableRow
extremeEsrpEntry=_ExtremeEsrpEntry_Object((1,3,6,1,4,1,1916,1,12,2,1))
extremeEsrpEntry.setIndexNames((0,_D,_H),(0,_D,_J))
if mibBuilder.loadTexts:extremeEsrpEntry.setStatus(_A)
class _ExtremeEsrpVlanIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeEsrpVlanIfIndex_Type.__name__=_C
_ExtremeEsrpVlanIfIndex_Object=MibTableColumn
extremeEsrpVlanIfIndex=_ExtremeEsrpVlanIfIndex_Object((1,3,6,1,4,1,1916,1,12,2,1,1),_ExtremeEsrpVlanIfIndex_Type())
extremeEsrpVlanIfIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:extremeEsrpVlanIfIndex.setStatus(_A)
class _ExtremeEsrpGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeEsrpGroup_Type.__name__=_C
_ExtremeEsrpGroup_Object=MibTableColumn
extremeEsrpGroup=_ExtremeEsrpGroup_Object((1,3,6,1,4,1,1916,1,12,2,1,2),_ExtremeEsrpGroup_Type())
extremeEsrpGroup.setMaxAccess(_N)
if mibBuilder.loadTexts:extremeEsrpGroup.setStatus(_A)
_ExtremeEsrpRowStatus_Type=RowStatus
_ExtremeEsrpRowStatus_Object=MibTableColumn
extremeEsrpRowStatus=_ExtremeEsrpRowStatus_Object((1,3,6,1,4,1,1916,1,12,2,1,3),_ExtremeEsrpRowStatus_Type())
extremeEsrpRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpRowStatus.setStatus(_A)
_ExtremeEsrpNetAddress_Type=ExtremeGenAddr
_ExtremeEsrpNetAddress_Object=MibTableColumn
extremeEsrpNetAddress=_ExtremeEsrpNetAddress_Object((1,3,6,1,4,1,1916,1,12,2,1,4),_ExtremeEsrpNetAddress_Type())
extremeEsrpNetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNetAddress.setStatus(_A)
class _ExtremeEsrpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_K,2),(_M,3)))
_ExtremeEsrpState_Type.__name__=_C
_ExtremeEsrpState_Object=MibTableColumn
extremeEsrpState=_ExtremeEsrpState_Object((1,3,6,1,4,1,1916,1,12,2,1,5),_ExtremeEsrpState_Type())
extremeEsrpState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpState.setStatus(_A)
class _ExtremeEsrpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ExtremeEsrpPriority_Type.__name__=_C
_ExtremeEsrpPriority_Object=MibTableColumn
extremeEsrpPriority=_ExtremeEsrpPriority_Object((1,3,6,1,4,1,1916,1,12,2,1,6),_ExtremeEsrpPriority_Type())
extremeEsrpPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpPriority.setStatus(_A)
class _ExtremeEsrpElectionAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('portsTrackPriorityMac',1),('trackPortsPriorityMac',2),('priorityPortsTrackMac',3),('priorityTrackPortsMac',4),('priorityMacOnly',5)))
_ExtremeEsrpElectionAlgorithm_Type.__name__=_C
_ExtremeEsrpElectionAlgorithm_Object=MibTableColumn
extremeEsrpElectionAlgorithm=_ExtremeEsrpElectionAlgorithm_Object((1,3,6,1,4,1,1916,1,12,2,1,7),_ExtremeEsrpElectionAlgorithm_Type())
extremeEsrpElectionAlgorithm.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpElectionAlgorithm.setStatus(_A)
class _ExtremeEsrpHelloTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ExtremeEsrpHelloTimer_Type.__name__=_C
_ExtremeEsrpHelloTimer_Object=MibTableColumn
extremeEsrpHelloTimer=_ExtremeEsrpHelloTimer_Object((1,3,6,1,4,1,1916,1,12,2,1,8),_ExtremeEsrpHelloTimer_Type())
extremeEsrpHelloTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpHelloTimer.setStatus(_A)
class _ExtremeEsrpActivePorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpActivePorts_Type.__name__=_C
_ExtremeEsrpActivePorts_Object=MibTableColumn
extremeEsrpActivePorts=_ExtremeEsrpActivePorts_Object((1,3,6,1,4,1,1916,1,12,2,1,9),_ExtremeEsrpActivePorts_Type())
extremeEsrpActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpActivePorts.setStatus(_A)
_ExtremeEsrpTrackedActivePorts_Type=Integer32
_ExtremeEsrpTrackedActivePorts_Object=MibTableColumn
extremeEsrpTrackedActivePorts=_ExtremeEsrpTrackedActivePorts_Object((1,3,6,1,4,1,1916,1,12,2,1,10),_ExtremeEsrpTrackedActivePorts_Type())
extremeEsrpTrackedActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpTrackedActivePorts.setStatus(_A)
_ExtremeEsrpTrackedIpRoutes_Type=Integer32
_ExtremeEsrpTrackedIpRoutes_Object=MibTableColumn
extremeEsrpTrackedIpRoutes=_ExtremeEsrpTrackedIpRoutes_Object((1,3,6,1,4,1,1916,1,12,2,1,11),_ExtremeEsrpTrackedIpRoutes_Type())
extremeEsrpTrackedIpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpTrackedIpRoutes.setStatus(_A)
_ExtremeEsrpTrackedPings_Type=Integer32
_ExtremeEsrpTrackedPings_Object=MibTableColumn
extremeEsrpTrackedPings=_ExtremeEsrpTrackedPings_Object((1,3,6,1,4,1,1916,1,12,2,1,12),_ExtremeEsrpTrackedPings_Type())
extremeEsrpTrackedPings.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpTrackedPings.setStatus(_A)
_ExtremeEsrpNumTransitionsToMaster_Type=Integer32
_ExtremeEsrpNumTransitionsToMaster_Object=MibTableColumn
extremeEsrpNumTransitionsToMaster=_ExtremeEsrpNumTransitionsToMaster_Object((1,3,6,1,4,1,1916,1,12,2,1,13),_ExtremeEsrpNumTransitionsToMaster_Type())
extremeEsrpNumTransitionsToMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNumTransitionsToMaster.setStatus(_A)
_ExtremeEsrpNumTransitionsToSlave_Type=Integer32
_ExtremeEsrpNumTransitionsToSlave_Object=MibTableColumn
extremeEsrpNumTransitionsToSlave=_ExtremeEsrpNumTransitionsToSlave_Object((1,3,6,1,4,1,1916,1,12,2,1,14),_ExtremeEsrpNumTransitionsToSlave_Type())
extremeEsrpNumTransitionsToSlave.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNumTransitionsToSlave.setStatus(_A)
class _ExtremeEsrpInternalActivePorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpInternalActivePorts_Type.__name__=_C
_ExtremeEsrpInternalActivePorts_Object=MibTableColumn
extremeEsrpInternalActivePorts=_ExtremeEsrpInternalActivePorts_Object((1,3,6,1,4,1,1916,1,12,2,1,15),_ExtremeEsrpInternalActivePorts_Type())
extremeEsrpInternalActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpInternalActivePorts.setStatus(_A)
_ExtremeEsrpNeighborTable_Object=MibTable
extremeEsrpNeighborTable=_ExtremeEsrpNeighborTable_Object((1,3,6,1,4,1,1916,1,12,3))
if mibBuilder.loadTexts:extremeEsrpNeighborTable.setStatus(_A)
_ExtremeEsrpNeighborEntry_Object=MibTableRow
extremeEsrpNeighborEntry=_ExtremeEsrpNeighborEntry_Object((1,3,6,1,4,1,1916,1,12,3,1))
extremeEsrpNeighborEntry.setIndexNames((0,_D,_H),(0,_D,_J),(0,_D,_P))
if mibBuilder.loadTexts:extremeEsrpNeighborEntry.setStatus(_A)
_ExtremeEsrpNeighborMacAddress_Type=MacAddress
_ExtremeEsrpNeighborMacAddress_Object=MibTableColumn
extremeEsrpNeighborMacAddress=_ExtremeEsrpNeighborMacAddress_Object((1,3,6,1,4,1,1916,1,12,3,1,1),_ExtremeEsrpNeighborMacAddress_Type())
extremeEsrpNeighborMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeEsrpNeighborMacAddress.setStatus(_A)
class _ExtremeEsrpNeighborGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeEsrpNeighborGroup_Type.__name__=_C
_ExtremeEsrpNeighborGroup_Object=MibTableColumn
extremeEsrpNeighborGroup=_ExtremeEsrpNeighborGroup_Object((1,3,6,1,4,1,1916,1,12,3,1,2),_ExtremeEsrpNeighborGroup_Type())
extremeEsrpNeighborGroup.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeEsrpNeighborGroup.setStatus(_A)
_ExtremeEsrpNeighborNetAddress_Type=ExtremeGenAddr
_ExtremeEsrpNeighborNetAddress_Object=MibTableColumn
extremeEsrpNeighborNetAddress=_ExtremeEsrpNeighborNetAddress_Object((1,3,6,1,4,1,1916,1,12,3,1,3),_ExtremeEsrpNeighborNetAddress_Type())
extremeEsrpNeighborNetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNeighborNetAddress.setStatus(_A)
class _ExtremeEsrpNeighborState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_K,2),(_M,3)))
_ExtremeEsrpNeighborState_Type.__name__=_C
_ExtremeEsrpNeighborState_Object=MibTableColumn
extremeEsrpNeighborState=_ExtremeEsrpNeighborState_Object((1,3,6,1,4,1,1916,1,12,3,1,4),_ExtremeEsrpNeighborState_Type())
extremeEsrpNeighborState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNeighborState.setStatus(_A)
_ExtremeEsrpNeighborPriority_Type=Integer32
_ExtremeEsrpNeighborPriority_Object=MibTableColumn
extremeEsrpNeighborPriority=_ExtremeEsrpNeighborPriority_Object((1,3,6,1,4,1,1916,1,12,3,1,5),_ExtremeEsrpNeighborPriority_Type())
extremeEsrpNeighborPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNeighborPriority.setStatus(_A)
class _ExtremeEsrpNeighborElectionAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('portAndPriority',1),('priority',2),('priorityThenPort',3)))
_ExtremeEsrpNeighborElectionAlgorithm_Type.__name__=_C
_ExtremeEsrpNeighborElectionAlgorithm_Object=MibTableColumn
extremeEsrpNeighborElectionAlgorithm=_ExtremeEsrpNeighborElectionAlgorithm_Object((1,3,6,1,4,1,1916,1,12,3,1,6),_ExtremeEsrpNeighborElectionAlgorithm_Type())
extremeEsrpNeighborElectionAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNeighborElectionAlgorithm.setStatus(_A)
_ExtremeEsrpNeighborHelloTimer_Type=Integer32
_ExtremeEsrpNeighborHelloTimer_Object=MibTableColumn
extremeEsrpNeighborHelloTimer=_ExtremeEsrpNeighborHelloTimer_Object((1,3,6,1,4,1,1916,1,12,3,1,7),_ExtremeEsrpNeighborHelloTimer_Type())
extremeEsrpNeighborHelloTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNeighborHelloTimer.setStatus(_A)
_ExtremeEsrpNeighborActivePorts_Type=Integer32
_ExtremeEsrpNeighborActivePorts_Object=MibTableColumn
extremeEsrpNeighborActivePorts=_ExtremeEsrpNeighborActivePorts_Object((1,3,6,1,4,1,1916,1,12,3,1,8),_ExtremeEsrpNeighborActivePorts_Type())
extremeEsrpNeighborActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNeighborActivePorts.setStatus(_A)
_ExtremeEsrpNeighborTrackedActivePorts_Type=Integer32
_ExtremeEsrpNeighborTrackedActivePorts_Object=MibTableColumn
extremeEsrpNeighborTrackedActivePorts=_ExtremeEsrpNeighborTrackedActivePorts_Object((1,3,6,1,4,1,1916,1,12,3,1,9),_ExtremeEsrpNeighborTrackedActivePorts_Type())
extremeEsrpNeighborTrackedActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNeighborTrackedActivePorts.setStatus(_A)
_ExtremeEsrpNeighborTrackedIpRoutes_Type=Integer32
_ExtremeEsrpNeighborTrackedIpRoutes_Object=MibTableColumn
extremeEsrpNeighborTrackedIpRoutes=_ExtremeEsrpNeighborTrackedIpRoutes_Object((1,3,6,1,4,1,1916,1,12,3,1,10),_ExtremeEsrpNeighborTrackedIpRoutes_Type())
extremeEsrpNeighborTrackedIpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNeighborTrackedIpRoutes.setStatus(_A)
_ExtremeEsrpNeighborInternalActivePorts_Type=Integer32
_ExtremeEsrpNeighborInternalActivePorts_Object=MibTableColumn
extremeEsrpNeighborInternalActivePorts=_ExtremeEsrpNeighborInternalActivePorts_Object((1,3,6,1,4,1,1916,1,12,3,1,11),_ExtremeEsrpNeighborInternalActivePorts_Type())
extremeEsrpNeighborInternalActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNeighborInternalActivePorts.setStatus(_A)
_ExtremeEsrpTrackVlanTable_Object=MibTable
extremeEsrpTrackVlanTable=_ExtremeEsrpTrackVlanTable_Object((1,3,6,1,4,1,1916,1,12,4))
if mibBuilder.loadTexts:extremeEsrpTrackVlanTable.setStatus(_A)
_ExtremeEsrpTrackVlanEntry_Object=MibTableRow
extremeEsrpTrackVlanEntry=_ExtremeEsrpTrackVlanEntry_Object((1,3,6,1,4,1,1916,1,12,4,1))
extremeEsrpTrackVlanEntry.setIndexNames((0,_D,_H),(0,_D,_J),(0,_D,_Q))
if mibBuilder.loadTexts:extremeEsrpTrackVlanEntry.setStatus(_A)
class _ExtremeEsrpTrackVlanIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeEsrpTrackVlanIfIndex_Type.__name__=_C
_ExtremeEsrpTrackVlanIfIndex_Object=MibTableColumn
extremeEsrpTrackVlanIfIndex=_ExtremeEsrpTrackVlanIfIndex_Object((1,3,6,1,4,1,1916,1,12,4,1,1),_ExtremeEsrpTrackVlanIfIndex_Type())
extremeEsrpTrackVlanIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeEsrpTrackVlanIfIndex.setStatus(_A)
_ExtremeEsrpTrackVlanRowStatus_Type=RowStatus
_ExtremeEsrpTrackVlanRowStatus_Object=MibTableColumn
extremeEsrpTrackVlanRowStatus=_ExtremeEsrpTrackVlanRowStatus_Object((1,3,6,1,4,1,1916,1,12,4,1,2),_ExtremeEsrpTrackVlanRowStatus_Type())
extremeEsrpTrackVlanRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpTrackVlanRowStatus.setStatus(_A)
_ExtremeEsrpTrackIpRouteTable_Object=MibTable
extremeEsrpTrackIpRouteTable=_ExtremeEsrpTrackIpRouteTable_Object((1,3,6,1,4,1,1916,1,12,5))
if mibBuilder.loadTexts:extremeEsrpTrackIpRouteTable.setStatus(_A)
_ExtremeEsrpTrackIpRouteEntry_Object=MibTableRow
extremeEsrpTrackIpRouteEntry=_ExtremeEsrpTrackIpRouteEntry_Object((1,3,6,1,4,1,1916,1,12,5,1))
extremeEsrpTrackIpRouteEntry.setIndexNames((0,_D,_H),(0,_D,_J),(0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:extremeEsrpTrackIpRouteEntry.setStatus(_A)
_ExtremeEsrpTrackIpRouteIpAddress_Type=IpAddress
_ExtremeEsrpTrackIpRouteIpAddress_Object=MibTableColumn
extremeEsrpTrackIpRouteIpAddress=_ExtremeEsrpTrackIpRouteIpAddress_Object((1,3,6,1,4,1,1916,1,12,5,1,1),_ExtremeEsrpTrackIpRouteIpAddress_Type())
extremeEsrpTrackIpRouteIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeEsrpTrackIpRouteIpAddress.setStatus(_A)
_ExtremeEsrpTrackIpRouteNetMask_Type=IpAddress
_ExtremeEsrpTrackIpRouteNetMask_Object=MibTableColumn
extremeEsrpTrackIpRouteNetMask=_ExtremeEsrpTrackIpRouteNetMask_Object((1,3,6,1,4,1,1916,1,12,5,1,2),_ExtremeEsrpTrackIpRouteNetMask_Type())
extremeEsrpTrackIpRouteNetMask.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeEsrpTrackIpRouteNetMask.setStatus(_A)
_ExtremeEsrpTrackIpRouteRowStatus_Type=RowStatus
_ExtremeEsrpTrackIpRouteRowStatus_Object=MibTableColumn
extremeEsrpTrackIpRouteRowStatus=_ExtremeEsrpTrackIpRouteRowStatus_Object((1,3,6,1,4,1,1916,1,12,5,1,3),_ExtremeEsrpTrackIpRouteRowStatus_Type())
extremeEsrpTrackIpRouteRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpTrackIpRouteRowStatus.setStatus(_A)
_ExtremeEsrpPortTable_Object=MibTable
extremeEsrpPortTable=_ExtremeEsrpPortTable_Object((1,3,6,1,4,1,1916,1,12,6))
if mibBuilder.loadTexts:extremeEsrpPortTable.setStatus(_A)
_ExtremeEsrpPortEntry_Object=MibTableRow
extremeEsrpPortEntry=_ExtremeEsrpPortEntry_Object((1,3,6,1,4,1,1916,1,12,6,1))
extremeEsrpPortEntry.setIndexNames((0,_D,_H),(0,_D,_T))
if mibBuilder.loadTexts:extremeEsrpPortEntry.setStatus(_A)
_ExtremeEsrpPortIfIndex_Type=Integer32
_ExtremeEsrpPortIfIndex_Object=MibTableColumn
extremeEsrpPortIfIndex=_ExtremeEsrpPortIfIndex_Object((1,3,6,1,4,1,1916,1,12,6,1,1),_ExtremeEsrpPortIfIndex_Type())
extremeEsrpPortIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeEsrpPortIfIndex.setStatus(_A)
_ExtremeEsrpPortState_Type=TruthValue
_ExtremeEsrpPortState_Object=MibTableColumn
extremeEsrpPortState=_ExtremeEsrpPortState_Object((1,3,6,1,4,1,1916,1,12,6,1,2),_ExtremeEsrpPortState_Type())
extremeEsrpPortState.setMaxAccess('read-write')
if mibBuilder.loadTexts:extremeEsrpPortState.setStatus(_A)
_ExtremeEsrpNotifications_ObjectIdentity=ObjectIdentity
extremeEsrpNotifications=_ExtremeEsrpNotifications_ObjectIdentity((1,3,6,1,4,1,1916,1,12,7))
_ExtremeEsrpNotificationsPrefix_ObjectIdentity=ObjectIdentity
extremeEsrpNotificationsPrefix=_ExtremeEsrpNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,12,7,0))
_ExtremeEsrpObjects_ObjectIdentity=ObjectIdentity
extremeEsrpObjects=_ExtremeEsrpObjects_ObjectIdentity((1,3,6,1,4,1,1916,1,12,8))
_ExtremeEsrpDomainTable_Object=MibTable
extremeEsrpDomainTable=_ExtremeEsrpDomainTable_Object((1,3,6,1,4,1,1916,1,12,8,1))
if mibBuilder.loadTexts:extremeEsrpDomainTable.setStatus(_A)
_ExtremeEsrpDomainEntry_Object=MibTableRow
extremeEsrpDomainEntry=_ExtremeEsrpDomainEntry_Object((1,3,6,1,4,1,1916,1,12,8,1,1))
extremeEsrpDomainEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:extremeEsrpDomainEntry.setStatus(_A)
class _ExtremeEsrpDmnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ExtremeEsrpDmnName_Type.__name__=_I
_ExtremeEsrpDmnName_Object=MibTableColumn
extremeEsrpDmnName=_ExtremeEsrpDmnName_Object((1,3,6,1,4,1,1916,1,12,8,1,1,1),_ExtremeEsrpDmnName_Type())
extremeEsrpDmnName.setMaxAccess(_N)
if mibBuilder.loadTexts:extremeEsrpDmnName.setStatus(_A)
class _ExtremeEsrpDmnGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_ExtremeEsrpDmnGroup_Type.__name__=_C
_ExtremeEsrpDmnGroup_Object=MibTableColumn
extremeEsrpDmnGroup=_ExtremeEsrpDmnGroup_Object((1,3,6,1,4,1,1916,1,12,8,1,1,2),_ExtremeEsrpDmnGroup_Type())
extremeEsrpDmnGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnGroup.setStatus(_A)
class _ExtremeEsrpDmnVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('v1',1),('v2',2)))
_ExtremeEsrpDmnVersion_Type.__name__=_C
_ExtremeEsrpDmnVersion_Object=MibTableColumn
extremeEsrpDmnVersion=_ExtremeEsrpDmnVersion_Object((1,3,6,1,4,1,1916,1,12,8,1,1,3),_ExtremeEsrpDmnVersion_Type())
extremeEsrpDmnVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnVersion.setStatus(_A)
class _ExtremeEsrpDmnAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ExtremeEsrpDmnAdminStatus_Type.__name__=_C
_ExtremeEsrpDmnAdminStatus_Object=MibTableColumn
extremeEsrpDmnAdminStatus=_ExtremeEsrpDmnAdminStatus_Object((1,3,6,1,4,1,1916,1,12,8,1,1,4),_ExtremeEsrpDmnAdminStatus_Type())
extremeEsrpDmnAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnAdminStatus.setStatus(_A)
_ExtremeEsrpDmnVlan_Type=DisplayString
_ExtremeEsrpDmnVlan_Object=MibTableColumn
extremeEsrpDmnVlan=_ExtremeEsrpDmnVlan_Object((1,3,6,1,4,1,1916,1,12,8,1,1,5),_ExtremeEsrpDmnVlan_Type())
extremeEsrpDmnVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnVlan.setStatus(_A)
class _ExtremeEsrpDmnVlanTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4093))
_ExtremeEsrpDmnVlanTag_Type.__name__=_C
_ExtremeEsrpDmnVlanTag_Object=MibTableColumn
extremeEsrpDmnVlanTag=_ExtremeEsrpDmnVlanTag_Object((1,3,6,1,4,1,1916,1,12,8,1,1,6),_ExtremeEsrpDmnVlanTag_Type())
extremeEsrpDmnVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnVlanTag.setStatus(_A)
class _ExtremeEsrpDmnId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeEsrpDmnId_Type.__name__=_C
_ExtremeEsrpDmnId_Object=MibTableColumn
extremeEsrpDmnId=_ExtremeEsrpDmnId_Object((1,3,6,1,4,1,1916,1,12,8,1,1,7),_ExtremeEsrpDmnId_Type())
extremeEsrpDmnId.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnId.setStatus(_A)
class _ExtremeEsrpDmnState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_L,0),(_K,1),(_M,2),(_U,3),('aware',4)))
_ExtremeEsrpDmnState_Type.__name__=_C
_ExtremeEsrpDmnState_Object=MibTableColumn
extremeEsrpDmnState=_ExtremeEsrpDmnState_Object((1,3,6,1,4,1,1916,1,12,8,1,1,8),_ExtremeEsrpDmnState_Type())
extremeEsrpDmnState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnState.setStatus(_A)
_ExtremeEsrpDmnNetAddress_Type=IpAddress
_ExtremeEsrpDmnNetAddress_Object=MibTableColumn
extremeEsrpDmnNetAddress=_ExtremeEsrpDmnNetAddress_Object((1,3,6,1,4,1,1916,1,12,8,1,1,9),_ExtremeEsrpDmnNetAddress_Type())
extremeEsrpDmnNetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnNetAddress.setStatus(_A)
_ExtremeEsrpDmnMasterMacAddress_Type=MacAddress
_ExtremeEsrpDmnMasterMacAddress_Object=MibTableColumn
extremeEsrpDmnMasterMacAddress=_ExtremeEsrpDmnMasterMacAddress_Object((1,3,6,1,4,1,1916,1,12,8,1,1,10),_ExtremeEsrpDmnMasterMacAddress_Type())
extremeEsrpDmnMasterMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnMasterMacAddress.setStatus(_A)
class _ExtremeEsrpDmnPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ExtremeEsrpDmnPriority_Type.__name__=_C
_ExtremeEsrpDmnPriority_Object=MibTableColumn
extremeEsrpDmnPriority=_ExtremeEsrpDmnPriority_Object((1,3,6,1,4,1,1916,1,12,8,1,1,11),_ExtremeEsrpDmnPriority_Type())
extremeEsrpDmnPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnPriority.setStatus(_A)
class _ExtremeEsrpDmnOperPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ExtremeEsrpDmnOperPriority_Type.__name__=_C
_ExtremeEsrpDmnOperPriority_Object=MibTableColumn
extremeEsrpDmnOperPriority=_ExtremeEsrpDmnOperPriority_Object((1,3,6,1,4,1,1916,1,12,8,1,1,12),_ExtremeEsrpDmnOperPriority_Type())
extremeEsrpDmnOperPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnOperPriority.setStatus(_A)
class _ExtremeEsrpDmnHelloTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ExtremeEsrpDmnHelloTimer_Type.__name__=_C
_ExtremeEsrpDmnHelloTimer_Object=MibTableColumn
extremeEsrpDmnHelloTimer=_ExtremeEsrpDmnHelloTimer_Object((1,3,6,1,4,1,1916,1,12,8,1,1,13),_ExtremeEsrpDmnHelloTimer_Type())
extremeEsrpDmnHelloTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnHelloTimer.setStatus(_A)
class _ExtremeEsrpDmnNeutralTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ExtremeEsrpDmnNeutralTimer_Type.__name__=_C
_ExtremeEsrpDmnNeutralTimer_Object=MibTableColumn
extremeEsrpDmnNeutralTimer=_ExtremeEsrpDmnNeutralTimer_Object((1,3,6,1,4,1,1916,1,12,8,1,1,14),_ExtremeEsrpDmnNeutralTimer_Type())
extremeEsrpDmnNeutralTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnNeutralTimer.setStatus(_A)
class _ExtremeEsrpDmnPreMasterTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ExtremeEsrpDmnPreMasterTimer_Type.__name__=_C
_ExtremeEsrpDmnPreMasterTimer_Object=MibTableColumn
extremeEsrpDmnPreMasterTimer=_ExtremeEsrpDmnPreMasterTimer_Object((1,3,6,1,4,1,1916,1,12,8,1,1,15),_ExtremeEsrpDmnPreMasterTimer_Type())
extremeEsrpDmnPreMasterTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnPreMasterTimer.setStatus(_A)
class _ExtremeEsrpDmnNbrTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ExtremeEsrpDmnNbrTimer_Type.__name__=_C
_ExtremeEsrpDmnNbrTimer_Object=MibTableColumn
extremeEsrpDmnNbrTimer=_ExtremeEsrpDmnNbrTimer_Object((1,3,6,1,4,1,1916,1,12,8,1,1,16),_ExtremeEsrpDmnNbrTimer_Type())
extremeEsrpDmnNbrTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnNbrTimer.setStatus(_A)
class _ExtremeEsrpDmnRestartTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ExtremeEsrpDmnRestartTimer_Type.__name__=_C
_ExtremeEsrpDmnRestartTimer_Object=MibTableColumn
extremeEsrpDmnRestartTimer=_ExtremeEsrpDmnRestartTimer_Object((1,3,6,1,4,1,1916,1,12,8,1,1,17),_ExtremeEsrpDmnRestartTimer_Type())
extremeEsrpDmnRestartTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnRestartTimer.setStatus(_A)
class _ExtremeEsrpDmnActivePorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnActivePorts_Type.__name__=_C
_ExtremeEsrpDmnActivePorts_Object=MibTableColumn
extremeEsrpDmnActivePorts=_ExtremeEsrpDmnActivePorts_Object((1,3,6,1,4,1,1916,1,12,8,1,1,18),_ExtremeEsrpDmnActivePorts_Type())
extremeEsrpDmnActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnActivePorts.setStatus(_A)
class _ExtremeEsrpDmnActivePortWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnActivePortWeight_Type.__name__=_C
_ExtremeEsrpDmnActivePortWeight_Object=MibTableColumn
extremeEsrpDmnActivePortWeight=_ExtremeEsrpDmnActivePortWeight_Object((1,3,6,1,4,1,1916,1,12,8,1,1,19),_ExtremeEsrpDmnActivePortWeight_Type())
extremeEsrpDmnActivePortWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnActivePortWeight.setStatus(_A)
class _ExtremeEsrpDmnInternalActivePorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnInternalActivePorts_Type.__name__=_C
_ExtremeEsrpDmnInternalActivePorts_Object=MibTableColumn
extremeEsrpDmnInternalActivePorts=_ExtremeEsrpDmnInternalActivePorts_Object((1,3,6,1,4,1,1916,1,12,8,1,1,20),_ExtremeEsrpDmnInternalActivePorts_Type())
extremeEsrpDmnInternalActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnInternalActivePorts.setStatus(_A)
class _ExtremeEsrpDmnTrackedActivePorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnTrackedActivePorts_Type.__name__=_C
_ExtremeEsrpDmnTrackedActivePorts_Object=MibTableColumn
extremeEsrpDmnTrackedActivePorts=_ExtremeEsrpDmnTrackedActivePorts_Object((1,3,6,1,4,1,1916,1,12,8,1,1,21),_ExtremeEsrpDmnTrackedActivePorts_Type())
extremeEsrpDmnTrackedActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnTrackedActivePorts.setStatus(_A)
class _ExtremeEsrpDmnTrackedActivePortWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnTrackedActivePortWeight_Type.__name__=_C
_ExtremeEsrpDmnTrackedActivePortWeight_Object=MibTableColumn
extremeEsrpDmnTrackedActivePortWeight=_ExtremeEsrpDmnTrackedActivePortWeight_Object((1,3,6,1,4,1,1916,1,12,8,1,1,22),_ExtremeEsrpDmnTrackedActivePortWeight_Type())
extremeEsrpDmnTrackedActivePortWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnTrackedActivePortWeight.setStatus(_A)
class _ExtremeEsrpDmnTrackedIpRoutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnTrackedIpRoutes_Type.__name__=_C
_ExtremeEsrpDmnTrackedIpRoutes_Object=MibTableColumn
extremeEsrpDmnTrackedIpRoutes=_ExtremeEsrpDmnTrackedIpRoutes_Object((1,3,6,1,4,1,1916,1,12,8,1,1,23),_ExtremeEsrpDmnTrackedIpRoutes_Type())
extremeEsrpDmnTrackedIpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnTrackedIpRoutes.setStatus(_A)
class _ExtremeEsrpDmnTrackedPings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnTrackedPings_Type.__name__=_C
_ExtremeEsrpDmnTrackedPings_Object=MibTableColumn
extremeEsrpDmnTrackedPings=_ExtremeEsrpDmnTrackedPings_Object((1,3,6,1,4,1,1916,1,12,8,1,1,24),_ExtremeEsrpDmnTrackedPings_Type())
extremeEsrpDmnTrackedPings.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnTrackedPings.setStatus(_A)
class _ExtremeEsrpDmnTrackedVlans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnTrackedVlans_Type.__name__=_C
_ExtremeEsrpDmnTrackedVlans_Object=MibTableColumn
extremeEsrpDmnTrackedVlans=_ExtremeEsrpDmnTrackedVlans_Object((1,3,6,1,4,1,1916,1,12,8,1,1,25),_ExtremeEsrpDmnTrackedVlans_Type())
extremeEsrpDmnTrackedVlans.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnTrackedVlans.setStatus(_A)
class _ExtremeEsrpDmnElectPreferenceForPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnElectPreferenceForPorts_Type.__name__=_C
_ExtremeEsrpDmnElectPreferenceForPorts_Object=MibTableColumn
extremeEsrpDmnElectPreferenceForPorts=_ExtremeEsrpDmnElectPreferenceForPorts_Object((1,3,6,1,4,1,1916,1,12,8,1,1,26),_ExtremeEsrpDmnElectPreferenceForPorts_Type())
extremeEsrpDmnElectPreferenceForPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnElectPreferenceForPorts.setStatus(_A)
class _ExtremeEsrpDmnElectPreferenceForPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnElectPreferenceForPriority_Type.__name__=_C
_ExtremeEsrpDmnElectPreferenceForPriority_Object=MibTableColumn
extremeEsrpDmnElectPreferenceForPriority=_ExtremeEsrpDmnElectPreferenceForPriority_Object((1,3,6,1,4,1,1916,1,12,8,1,1,27),_ExtremeEsrpDmnElectPreferenceForPriority_Type())
extremeEsrpDmnElectPreferenceForPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnElectPreferenceForPriority.setStatus(_A)
class _ExtremeEsrpDmnElectPreferenceForMac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnElectPreferenceForMac_Type.__name__=_C
_ExtremeEsrpDmnElectPreferenceForMac_Object=MibTableColumn
extremeEsrpDmnElectPreferenceForMac=_ExtremeEsrpDmnElectPreferenceForMac_Object((1,3,6,1,4,1,1916,1,12,8,1,1,28),_ExtremeEsrpDmnElectPreferenceForMac_Type())
extremeEsrpDmnElectPreferenceForMac.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnElectPreferenceForMac.setStatus(_A)
class _ExtremeEsrpDmnElectPreferenceForTrack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnElectPreferenceForTrack_Type.__name__=_C
_ExtremeEsrpDmnElectPreferenceForTrack_Object=MibTableColumn
extremeEsrpDmnElectPreferenceForTrack=_ExtremeEsrpDmnElectPreferenceForTrack_Object((1,3,6,1,4,1,1916,1,12,8,1,1,29),_ExtremeEsrpDmnElectPreferenceForTrack_Type())
extremeEsrpDmnElectPreferenceForTrack.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnElectPreferenceForTrack.setStatus(_A)
class _ExtremeEsrpDmnElectPreferenceForSticky_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnElectPreferenceForSticky_Type.__name__=_C
_ExtremeEsrpDmnElectPreferenceForSticky_Object=MibTableColumn
extremeEsrpDmnElectPreferenceForSticky=_ExtremeEsrpDmnElectPreferenceForSticky_Object((1,3,6,1,4,1,1916,1,12,8,1,1,30),_ExtremeEsrpDmnElectPreferenceForSticky_Type())
extremeEsrpDmnElectPreferenceForSticky.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnElectPreferenceForSticky.setStatus(_A)
class _ExtremeEsrpDmnElectPreferenceForWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnElectPreferenceForWeight_Type.__name__=_C
_ExtremeEsrpDmnElectPreferenceForWeight_Object=MibTableColumn
extremeEsrpDmnElectPreferenceForWeight=_ExtremeEsrpDmnElectPreferenceForWeight_Object((1,3,6,1,4,1,1916,1,12,8,1,1,31),_ExtremeEsrpDmnElectPreferenceForWeight_Type())
extremeEsrpDmnElectPreferenceForWeight.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnElectPreferenceForWeight.setStatus(_A)
_ExtremeEsrpDmnRowStatus_Type=RowStatus
_ExtremeEsrpDmnRowStatus_Object=MibTableColumn
extremeEsrpDmnRowStatus=_ExtremeEsrpDmnRowStatus_Object((1,3,6,1,4,1,1916,1,12,8,1,1,32),_ExtremeEsrpDmnRowStatus_Type())
extremeEsrpDmnRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDmnRowStatus.setStatus(_A)
_ExtremeEsrpDomainMemberTable_Object=MibTable
extremeEsrpDomainMemberTable=_ExtremeEsrpDomainMemberTable_Object((1,3,6,1,4,1,1916,1,12,8,2))
if mibBuilder.loadTexts:extremeEsrpDomainMemberTable.setStatus(_A)
_ExtremeEsrpDomainMemberEntry_Object=MibTableRow
extremeEsrpDomainMemberEntry=_ExtremeEsrpDomainMemberEntry_Object((1,3,6,1,4,1,1916,1,12,8,2,1))
extremeEsrpDomainMemberEntry.setIndexNames((0,_D,_G),(0,_D,_V))
if mibBuilder.loadTexts:extremeEsrpDomainMemberEntry.setStatus(_A)
class _ExtremeEsrpVlanDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ExtremeEsrpVlanDescr_Type.__name__=_I
_ExtremeEsrpVlanDescr_Object=MibTableColumn
extremeEsrpVlanDescr=_ExtremeEsrpVlanDescr_Object((1,3,6,1,4,1,1916,1,12,8,2,1,1),_ExtremeEsrpVlanDescr_Type())
extremeEsrpVlanDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeEsrpVlanDescr.setStatus(_A)
class _ExtremeEsrpVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('protected',2)))
_ExtremeEsrpVlanType_Type.__name__=_C
_ExtremeEsrpVlanType_Object=MibTableColumn
extremeEsrpVlanType=_ExtremeEsrpVlanType_Object((1,3,6,1,4,1,1916,1,12,8,2,1,2),_ExtremeEsrpVlanType_Type())
extremeEsrpVlanType.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpVlanType.setStatus(_A)
_ExtremeEsrpDomainVlanIfIndex_Type=Integer32
_ExtremeEsrpDomainVlanIfIndex_Object=MibTableColumn
extremeEsrpDomainVlanIfIndex=_ExtremeEsrpDomainVlanIfIndex_Object((1,3,6,1,4,1,1916,1,12,8,2,1,3),_ExtremeEsrpDomainVlanIfIndex_Type())
extremeEsrpDomainVlanIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpDomainVlanIfIndex.setStatus(_A)
_ExtremeEsrpVlanRowStatus_Type=RowStatus
_ExtremeEsrpVlanRowStatus_Object=MibTableColumn
extremeEsrpVlanRowStatus=_ExtremeEsrpVlanRowStatus_Object((1,3,6,1,4,1,1916,1,12,8,2,1,4),_ExtremeEsrpVlanRowStatus_Type())
extremeEsrpVlanRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeEsrpVlanRowStatus.setStatus(_A)
_ExtremeEsrpDomainNeighborTable_Object=MibTable
extremeEsrpDomainNeighborTable=_ExtremeEsrpDomainNeighborTable_Object((1,3,6,1,4,1,1916,1,12,8,3))
if mibBuilder.loadTexts:extremeEsrpDomainNeighborTable.setStatus(_A)
_ExtremeEsrpDomainNeighborEntry_Object=MibTableRow
extremeEsrpDomainNeighborEntry=_ExtremeEsrpDomainNeighborEntry_Object((1,3,6,1,4,1,1916,1,12,8,3,1))
extremeEsrpDomainNeighborEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:extremeEsrpDomainNeighborEntry.setStatus(_A)
_ExtremeEsrpDmnNeighborMacAddress_Type=MacAddress
_ExtremeEsrpDmnNeighborMacAddress_Object=MibTableColumn
extremeEsrpDmnNeighborMacAddress=_ExtremeEsrpDmnNeighborMacAddress_Object((1,3,6,1,4,1,1916,1,12,8,3,1,1),_ExtremeEsrpDmnNeighborMacAddress_Type())
extremeEsrpDmnNeighborMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnNeighborMacAddress.setStatus(_A)
class _ExtremeEsrpDmnNeighborGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_ExtremeEsrpDmnNeighborGroup_Type.__name__=_C
_ExtremeEsrpDmnNeighborGroup_Object=MibTableColumn
extremeEsrpDmnNeighborGroup=_ExtremeEsrpDmnNeighborGroup_Object((1,3,6,1,4,1,1916,1,12,8,3,1,2),_ExtremeEsrpDmnNeighborGroup_Type())
extremeEsrpDmnNeighborGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnNeighborGroup.setStatus(_A)
_ExtremeEsrpDmnNeighborNetAddress_Type=IpAddress
_ExtremeEsrpDmnNeighborNetAddress_Object=MibTableColumn
extremeEsrpDmnNeighborNetAddress=_ExtremeEsrpDmnNeighborNetAddress_Object((1,3,6,1,4,1,1916,1,12,8,3,1,3),_ExtremeEsrpDmnNeighborNetAddress_Type())
extremeEsrpDmnNeighborNetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnNeighborNetAddress.setStatus(_A)
class _ExtremeEsrpDmnNeighborState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_L,0),(_K,1),(_M,2),(_U,3),('aware',4)))
_ExtremeEsrpDmnNeighborState_Type.__name__=_C
_ExtremeEsrpDmnNeighborState_Object=MibTableColumn
extremeEsrpDmnNeighborState=_ExtremeEsrpDmnNeighborState_Object((1,3,6,1,4,1,1916,1,12,8,3,1,4),_ExtremeEsrpDmnNeighborState_Type())
extremeEsrpDmnNeighborState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnNeighborState.setStatus(_A)
class _ExtremeEsrpDmnNeighborPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ExtremeEsrpDmnNeighborPriority_Type.__name__=_C
_ExtremeEsrpDmnNeighborPriority_Object=MibTableColumn
extremeEsrpDmnNeighborPriority=_ExtremeEsrpDmnNeighborPriority_Object((1,3,6,1,4,1,1916,1,12,8,3,1,5),_ExtremeEsrpDmnNeighborPriority_Type())
extremeEsrpDmnNeighborPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnNeighborPriority.setStatus(_A)
class _ExtremeEsrpDmnNeighborHelloTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ExtremeEsrpDmnNeighborHelloTimer_Type.__name__=_C
_ExtremeEsrpDmnNeighborHelloTimer_Object=MibTableColumn
extremeEsrpDmnNeighborHelloTimer=_ExtremeEsrpDmnNeighborHelloTimer_Object((1,3,6,1,4,1,1916,1,12,8,3,1,6),_ExtremeEsrpDmnNeighborHelloTimer_Type())
extremeEsrpDmnNeighborHelloTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnNeighborHelloTimer.setStatus(_A)
class _ExtremeEsrpDmnNeighborActivePorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnNeighborActivePorts_Type.__name__=_C
_ExtremeEsrpDmnNeighborActivePorts_Object=MibTableColumn
extremeEsrpDmnNeighborActivePorts=_ExtremeEsrpDmnNeighborActivePorts_Object((1,3,6,1,4,1,1916,1,12,8,3,1,7),_ExtremeEsrpDmnNeighborActivePorts_Type())
extremeEsrpDmnNeighborActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnNeighborActivePorts.setStatus(_A)
class _ExtremeEsrpDmnNeighborInternalActivePorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnNeighborInternalActivePorts_Type.__name__=_C
_ExtremeEsrpDmnNeighborInternalActivePorts_Object=MibTableColumn
extremeEsrpDmnNeighborInternalActivePorts=_ExtremeEsrpDmnNeighborInternalActivePorts_Object((1,3,6,1,4,1,1916,1,12,8,3,1,8),_ExtremeEsrpDmnNeighborInternalActivePorts_Type())
extremeEsrpDmnNeighborInternalActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnNeighborInternalActivePorts.setStatus(_A)
class _ExtremeEsrpDmnNeighborTrackedActivePorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnNeighborTrackedActivePorts_Type.__name__=_C
_ExtremeEsrpDmnNeighborTrackedActivePorts_Object=MibTableColumn
extremeEsrpDmnNeighborTrackedActivePorts=_ExtremeEsrpDmnNeighborTrackedActivePorts_Object((1,3,6,1,4,1,1916,1,12,8,3,1,9),_ExtremeEsrpDmnNeighborTrackedActivePorts_Type())
extremeEsrpDmnNeighborTrackedActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnNeighborTrackedActivePorts.setStatus(_A)
class _ExtremeEsrpDmnNeighborTrackedIpCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnNeighborTrackedIpCount_Type.__name__=_C
_ExtremeEsrpDmnNeighborTrackedIpCount_Object=MibTableColumn
extremeEsrpDmnNeighborTrackedIpCount=_ExtremeEsrpDmnNeighborTrackedIpCount_Object((1,3,6,1,4,1,1916,1,12,8,3,1,10),_ExtremeEsrpDmnNeighborTrackedIpCount_Type())
extremeEsrpDmnNeighborTrackedIpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnNeighborTrackedIpCount.setStatus(_A)
class _ExtremeEsrpDmnNeighborActivePortWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnNeighborActivePortWeight_Type.__name__=_C
_ExtremeEsrpDmnNeighborActivePortWeight_Object=MibTableColumn
extremeEsrpDmnNeighborActivePortWeight=_ExtremeEsrpDmnNeighborActivePortWeight_Object((1,3,6,1,4,1,1916,1,12,8,3,1,11),_ExtremeEsrpDmnNeighborActivePortWeight_Type())
extremeEsrpDmnNeighborActivePortWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnNeighborActivePortWeight.setStatus(_A)
class _ExtremeEsrpDmnNeighborTrackedActivePortWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpDmnNeighborTrackedActivePortWeight_Type.__name__=_C
_ExtremeEsrpDmnNeighborTrackedActivePortWeight_Object=MibTableColumn
extremeEsrpDmnNeighborTrackedActivePortWeight=_ExtremeEsrpDmnNeighborTrackedActivePortWeight_Object((1,3,6,1,4,1,1916,1,12,8,3,1,12),_ExtremeEsrpDmnNeighborTrackedActivePortWeight_Type())
extremeEsrpDmnNeighborTrackedActivePortWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDmnNeighborTrackedActivePortWeight.setStatus(_A)
_ExtremeEsrpDomainAwareTable_Object=MibTable
extremeEsrpDomainAwareTable=_ExtremeEsrpDomainAwareTable_Object((1,3,6,1,4,1,1916,1,12,8,4))
if mibBuilder.loadTexts:extremeEsrpDomainAwareTable.setStatus(_A)
_ExtremeEsrpDomainAwareEntry_Object=MibTableRow
extremeEsrpDomainAwareEntry=_ExtremeEsrpDomainAwareEntry_Object((1,3,6,1,4,1,1916,1,12,8,4,1))
extremeEsrpDomainAwareEntry.setIndexNames((0,_D,_G),(0,_D,_O))
if mibBuilder.loadTexts:extremeEsrpDomainAwareEntry.setStatus(_A)
_ExtremeEsrpMasterMacAddress_Type=MacAddress
_ExtremeEsrpMasterMacAddress_Object=MibTableColumn
extremeEsrpMasterMacAddress=_ExtremeEsrpMasterMacAddress_Object((1,3,6,1,4,1,1916,1,12,8,4,1,1),_ExtremeEsrpMasterMacAddress_Type())
extremeEsrpMasterMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpMasterMacAddress.setStatus(_A)
class _ExtremeEsrpMasterLastChanged_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ExtremeEsrpMasterLastChanged_Type.__name__=_I
_ExtremeEsrpMasterLastChanged_Object=MibTableColumn
extremeEsrpMasterLastChanged=_ExtremeEsrpMasterLastChanged_Object((1,3,6,1,4,1,1916,1,12,8,4,1,2),_ExtremeEsrpMasterLastChanged_Type())
extremeEsrpMasterLastChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpMasterLastChanged.setStatus(_A)
_ExtremeEsrpNumFdbFlushes_Type=Counter32
_ExtremeEsrpNumFdbFlushes_Object=MibTableColumn
extremeEsrpNumFdbFlushes=_ExtremeEsrpNumFdbFlushes_Object((1,3,6,1,4,1,1916,1,12,8,4,1,3),_ExtremeEsrpNumFdbFlushes_Type())
extremeEsrpNumFdbFlushes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNumFdbFlushes.setStatus(_A)
_ExtremeEsrpHelloPktsReceived_Type=Counter32
_ExtremeEsrpHelloPktsReceived_Object=MibTableColumn
extremeEsrpHelloPktsReceived=_ExtremeEsrpHelloPktsReceived_Object((1,3,6,1,4,1,1916,1,12,8,4,1,4),_ExtremeEsrpHelloPktsReceived_Type())
extremeEsrpHelloPktsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpHelloPktsReceived.setStatus(_A)
_ExtremeEsrpHelloPktsForwarded_Type=Counter32
_ExtremeEsrpHelloPktsForwarded_Object=MibTableColumn
extremeEsrpHelloPktsForwarded=_ExtremeEsrpHelloPktsForwarded_Object((1,3,6,1,4,1,1916,1,12,8,4,1,5),_ExtremeEsrpHelloPktsForwarded_Type())
extremeEsrpHelloPktsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpHelloPktsForwarded.setStatus(_A)
_ExtremeEsrpDomainStatsTable_Object=MibTable
extremeEsrpDomainStatsTable=_ExtremeEsrpDomainStatsTable_Object((1,3,6,1,4,1,1916,1,12,8,5))
if mibBuilder.loadTexts:extremeEsrpDomainStatsTable.setStatus(_A)
_ExtremeEsrpDomainStatsEntry_Object=MibTableRow
extremeEsrpDomainStatsEntry=_ExtremeEsrpDomainStatsEntry_Object((1,3,6,1,4,1,1916,1,12,8,5,1))
extremeEsrpDomainStatsEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:extremeEsrpDomainStatsEntry.setStatus(_A)
class _ExtremeEsrpLastStateChanged_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ExtremeEsrpLastStateChanged_Type.__name__=_I
_ExtremeEsrpLastStateChanged_Object=MibTableColumn
extremeEsrpLastStateChanged=_ExtremeEsrpLastStateChanged_Object((1,3,6,1,4,1,1916,1,12,8,5,1,1),_ExtremeEsrpLastStateChanged_Type())
extremeEsrpLastStateChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpLastStateChanged.setStatus(_A)
_ExtremeEsrpDomainNumTransitionsToMaster_Type=Counter32
_ExtremeEsrpDomainNumTransitionsToMaster_Object=MibTableColumn
extremeEsrpDomainNumTransitionsToMaster=_ExtremeEsrpDomainNumTransitionsToMaster_Object((1,3,6,1,4,1,1916,1,12,8,5,1,2),_ExtremeEsrpDomainNumTransitionsToMaster_Type())
extremeEsrpDomainNumTransitionsToMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDomainNumTransitionsToMaster.setStatus(_A)
_ExtremeEsrpNumTransitionsToPreMaster_Type=Counter32
_ExtremeEsrpNumTransitionsToPreMaster_Object=MibTableColumn
extremeEsrpNumTransitionsToPreMaster=_ExtremeEsrpNumTransitionsToPreMaster_Object((1,3,6,1,4,1,1916,1,12,8,5,1,3),_ExtremeEsrpNumTransitionsToPreMaster_Type())
extremeEsrpNumTransitionsToPreMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNumTransitionsToPreMaster.setStatus(_A)
_ExtremeEsrpDomainNumTransitionsToSlave_Type=Counter32
_ExtremeEsrpDomainNumTransitionsToSlave_Object=MibTableColumn
extremeEsrpDomainNumTransitionsToSlave=_ExtremeEsrpDomainNumTransitionsToSlave_Object((1,3,6,1,4,1,1916,1,12,8,5,1,4),_ExtremeEsrpDomainNumTransitionsToSlave_Type())
extremeEsrpDomainNumTransitionsToSlave.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpDomainNumTransitionsToSlave.setStatus(_A)
_ExtremeEsrpNumTransitionsToNeutral_Type=Counter32
_ExtremeEsrpNumTransitionsToNeutral_Object=MibTableColumn
extremeEsrpNumTransitionsToNeutral=_ExtremeEsrpNumTransitionsToNeutral_Object((1,3,6,1,4,1,1916,1,12,8,5,1,5),_ExtremeEsrpNumTransitionsToNeutral_Type())
extremeEsrpNumTransitionsToNeutral.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNumTransitionsToNeutral.setStatus(_A)
_ExtremeEsrpNumTransitionsToAware_Type=Counter32
_ExtremeEsrpNumTransitionsToAware_Object=MibTableColumn
extremeEsrpNumTransitionsToAware=_ExtremeEsrpNumTransitionsToAware_Object((1,3,6,1,4,1,1916,1,12,8,5,1,6),_ExtremeEsrpNumTransitionsToAware_Type())
extremeEsrpNumTransitionsToAware.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpNumTransitionsToAware.setStatus(_A)
_ExtremeEsrpHelloPktsReceived1_Type=Counter32
_ExtremeEsrpHelloPktsReceived1_Object=MibTableColumn
extremeEsrpHelloPktsReceived1=_ExtremeEsrpHelloPktsReceived1_Object((1,3,6,1,4,1,1916,1,12,8,5,1,7),_ExtremeEsrpHelloPktsReceived1_Type())
extremeEsrpHelloPktsReceived1.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpHelloPktsReceived1.setStatus(_A)
_ExtremeEsrpHelloPktsTransmitted_Type=Counter32
_ExtremeEsrpHelloPktsTransmitted_Object=MibTableColumn
extremeEsrpHelloPktsTransmitted=_ExtremeEsrpHelloPktsTransmitted_Object((1,3,6,1,4,1,1916,1,12,8,5,1,8),_ExtremeEsrpHelloPktsTransmitted_Type())
extremeEsrpHelloPktsTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpHelloPktsTransmitted.setStatus(_A)
_ExtremeEsrpAwareSelectForwardPortsTable_Object=MibTable
extremeEsrpAwareSelectForwardPortsTable=_ExtremeEsrpAwareSelectForwardPortsTable_Object((1,3,6,1,4,1,1916,1,12,8,6))
if mibBuilder.loadTexts:extremeEsrpAwareSelectForwardPortsTable.setStatus(_A)
_ExtremeEsrpAwareSelectForwardPortsEntry_Object=MibTableRow
extremeEsrpAwareSelectForwardPortsEntry=_ExtremeEsrpAwareSelectForwardPortsEntry_Object((1,3,6,1,4,1,1916,1,12,8,6,1))
extremeEsrpAwareSelectForwardPortsEntry.setIndexNames((0,_D,_W),(0,_D,_X))
if mibBuilder.loadTexts:extremeEsrpAwareSelectForwardPortsEntry.setStatus(_A)
_ExtremeEsrpAwareSelFwdListDmnName_Type=DisplayString
_ExtremeEsrpAwareSelFwdListDmnName_Object=MibTableColumn
extremeEsrpAwareSelFwdListDmnName=_ExtremeEsrpAwareSelFwdListDmnName_Object((1,3,6,1,4,1,1916,1,12,8,6,1,1),_ExtremeEsrpAwareSelFwdListDmnName_Type())
extremeEsrpAwareSelFwdListDmnName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpAwareSelFwdListDmnName.setStatus(_A)
class _ExtremeEsrpAwareSelFwdListDmnGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_ExtremeEsrpAwareSelFwdListDmnGroup_Type.__name__=_C
_ExtremeEsrpAwareSelFwdListDmnGroup_Object=MibTableColumn
extremeEsrpAwareSelFwdListDmnGroup=_ExtremeEsrpAwareSelFwdListDmnGroup_Object((1,3,6,1,4,1,1916,1,12,8,6,1,2),_ExtremeEsrpAwareSelFwdListDmnGroup_Type())
extremeEsrpAwareSelFwdListDmnGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpAwareSelFwdListDmnGroup.setStatus(_A)
class _ExtremeEsrpAwareSelFwdListPortCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEsrpAwareSelFwdListPortCount_Type.__name__=_C
_ExtremeEsrpAwareSelFwdListPortCount_Object=MibTableColumn
extremeEsrpAwareSelFwdListPortCount=_ExtremeEsrpAwareSelFwdListPortCount_Object((1,3,6,1,4,1,1916,1,12,8,6,1,3),_ExtremeEsrpAwareSelFwdListPortCount_Type())
extremeEsrpAwareSelFwdListPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpAwareSelFwdListPortCount.setStatus(_A)
_ExtremeEsrpAwareSelFwdListPortList_Type=PortList
_ExtremeEsrpAwareSelFwdListPortList_Object=MibTableColumn
extremeEsrpAwareSelFwdListPortList=_ExtremeEsrpAwareSelFwdListPortList_Object((1,3,6,1,4,1,1916,1,12,8,6,1,4),_ExtremeEsrpAwareSelFwdListPortList_Type())
extremeEsrpAwareSelFwdListPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEsrpAwareSelFwdListPortList.setStatus(_A)
extremeEsrpDomainStateChange=NotificationType((1,3,6,1,4,1,1916,1,12,7,0,1))
extremeEsrpDomainStateChange.setObjects(*((_D,_G),(_D,_O),(_D,_Y),(_D,_Z),(_D,_a),(_D,_b),(_D,_c),(_D,_d),(_D,_e),(_D,_f),(_D,_g),(_D,_h)))
if mibBuilder.loadTexts:extremeEsrpDomainStateChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'extremeEsrp':extremeEsrp,'extremeEsrpTable':extremeEsrpTable,'extremeEsrpEntry':extremeEsrpEntry,_H:extremeEsrpVlanIfIndex,_J:extremeEsrpGroup,'extremeEsrpRowStatus':extremeEsrpRowStatus,'extremeEsrpNetAddress':extremeEsrpNetAddress,'extremeEsrpState':extremeEsrpState,'extremeEsrpPriority':extremeEsrpPriority,'extremeEsrpElectionAlgorithm':extremeEsrpElectionAlgorithm,'extremeEsrpHelloTimer':extremeEsrpHelloTimer,'extremeEsrpActivePorts':extremeEsrpActivePorts,'extremeEsrpTrackedActivePorts':extremeEsrpTrackedActivePorts,'extremeEsrpTrackedIpRoutes':extremeEsrpTrackedIpRoutes,'extremeEsrpTrackedPings':extremeEsrpTrackedPings,'extremeEsrpNumTransitionsToMaster':extremeEsrpNumTransitionsToMaster,'extremeEsrpNumTransitionsToSlave':extremeEsrpNumTransitionsToSlave,'extremeEsrpInternalActivePorts':extremeEsrpInternalActivePorts,'extremeEsrpNeighborTable':extremeEsrpNeighborTable,'extremeEsrpNeighborEntry':extremeEsrpNeighborEntry,_P:extremeEsrpNeighborMacAddress,'extremeEsrpNeighborGroup':extremeEsrpNeighborGroup,'extremeEsrpNeighborNetAddress':extremeEsrpNeighborNetAddress,'extremeEsrpNeighborState':extremeEsrpNeighborState,'extremeEsrpNeighborPriority':extremeEsrpNeighborPriority,'extremeEsrpNeighborElectionAlgorithm':extremeEsrpNeighborElectionAlgorithm,'extremeEsrpNeighborHelloTimer':extremeEsrpNeighborHelloTimer,'extremeEsrpNeighborActivePorts':extremeEsrpNeighborActivePorts,'extremeEsrpNeighborTrackedActivePorts':extremeEsrpNeighborTrackedActivePorts,'extremeEsrpNeighborTrackedIpRoutes':extremeEsrpNeighborTrackedIpRoutes,'extremeEsrpNeighborInternalActivePorts':extremeEsrpNeighborInternalActivePorts,'extremeEsrpTrackVlanTable':extremeEsrpTrackVlanTable,'extremeEsrpTrackVlanEntry':extremeEsrpTrackVlanEntry,_Q:extremeEsrpTrackVlanIfIndex,'extremeEsrpTrackVlanRowStatus':extremeEsrpTrackVlanRowStatus,'extremeEsrpTrackIpRouteTable':extremeEsrpTrackIpRouteTable,'extremeEsrpTrackIpRouteEntry':extremeEsrpTrackIpRouteEntry,_R:extremeEsrpTrackIpRouteIpAddress,_S:extremeEsrpTrackIpRouteNetMask,'extremeEsrpTrackIpRouteRowStatus':extremeEsrpTrackIpRouteRowStatus,'extremeEsrpPortTable':extremeEsrpPortTable,'extremeEsrpPortEntry':extremeEsrpPortEntry,_T:extremeEsrpPortIfIndex,'extremeEsrpPortState':extremeEsrpPortState,'extremeEsrpNotifications':extremeEsrpNotifications,'extremeEsrpNotificationsPrefix':extremeEsrpNotificationsPrefix,'extremeEsrpDomainStateChange':extremeEsrpDomainStateChange,'extremeEsrpObjects':extremeEsrpObjects,'extremeEsrpDomainTable':extremeEsrpDomainTable,'extremeEsrpDomainEntry':extremeEsrpDomainEntry,_G:extremeEsrpDmnName,_O:extremeEsrpDmnGroup,'extremeEsrpDmnVersion':extremeEsrpDmnVersion,'extremeEsrpDmnAdminStatus':extremeEsrpDmnAdminStatus,'extremeEsrpDmnVlan':extremeEsrpDmnVlan,'extremeEsrpDmnVlanTag':extremeEsrpDmnVlanTag,'extremeEsrpDmnId':extremeEsrpDmnId,_Y:extremeEsrpDmnState,_Z:extremeEsrpDmnNetAddress,_a:extremeEsrpDmnMasterMacAddress,'extremeEsrpDmnPriority':extremeEsrpDmnPriority,'extremeEsrpDmnOperPriority':extremeEsrpDmnOperPriority,'extremeEsrpDmnHelloTimer':extremeEsrpDmnHelloTimer,'extremeEsrpDmnNeutralTimer':extremeEsrpDmnNeutralTimer,'extremeEsrpDmnPreMasterTimer':extremeEsrpDmnPreMasterTimer,'extremeEsrpDmnNbrTimer':extremeEsrpDmnNbrTimer,'extremeEsrpDmnRestartTimer':extremeEsrpDmnRestartTimer,_b:extremeEsrpDmnActivePorts,_g:extremeEsrpDmnActivePortWeight,_c:extremeEsrpDmnInternalActivePorts,_d:extremeEsrpDmnTrackedActivePorts,_h:extremeEsrpDmnTrackedActivePortWeight,_e:extremeEsrpDmnTrackedIpRoutes,_f:extremeEsrpDmnTrackedPings,'extremeEsrpDmnTrackedVlans':extremeEsrpDmnTrackedVlans,'extremeEsrpDmnElectPreferenceForPorts':extremeEsrpDmnElectPreferenceForPorts,'extremeEsrpDmnElectPreferenceForPriority':extremeEsrpDmnElectPreferenceForPriority,'extremeEsrpDmnElectPreferenceForMac':extremeEsrpDmnElectPreferenceForMac,'extremeEsrpDmnElectPreferenceForTrack':extremeEsrpDmnElectPreferenceForTrack,'extremeEsrpDmnElectPreferenceForSticky':extremeEsrpDmnElectPreferenceForSticky,'extremeEsrpDmnElectPreferenceForWeight':extremeEsrpDmnElectPreferenceForWeight,'extremeEsrpDmnRowStatus':extremeEsrpDmnRowStatus,'extremeEsrpDomainMemberTable':extremeEsrpDomainMemberTable,'extremeEsrpDomainMemberEntry':extremeEsrpDomainMemberEntry,_V:extremeEsrpVlanDescr,'extremeEsrpVlanType':extremeEsrpVlanType,'extremeEsrpDomainVlanIfIndex':extremeEsrpDomainVlanIfIndex,'extremeEsrpVlanRowStatus':extremeEsrpVlanRowStatus,'extremeEsrpDomainNeighborTable':extremeEsrpDomainNeighborTable,'extremeEsrpDomainNeighborEntry':extremeEsrpDomainNeighborEntry,'extremeEsrpDmnNeighborMacAddress':extremeEsrpDmnNeighborMacAddress,'extremeEsrpDmnNeighborGroup':extremeEsrpDmnNeighborGroup,'extremeEsrpDmnNeighborNetAddress':extremeEsrpDmnNeighborNetAddress,'extremeEsrpDmnNeighborState':extremeEsrpDmnNeighborState,'extremeEsrpDmnNeighborPriority':extremeEsrpDmnNeighborPriority,'extremeEsrpDmnNeighborHelloTimer':extremeEsrpDmnNeighborHelloTimer,'extremeEsrpDmnNeighborActivePorts':extremeEsrpDmnNeighborActivePorts,'extremeEsrpDmnNeighborInternalActivePorts':extremeEsrpDmnNeighborInternalActivePorts,'extremeEsrpDmnNeighborTrackedActivePorts':extremeEsrpDmnNeighborTrackedActivePorts,'extremeEsrpDmnNeighborTrackedIpCount':extremeEsrpDmnNeighborTrackedIpCount,'extremeEsrpDmnNeighborActivePortWeight':extremeEsrpDmnNeighborActivePortWeight,'extremeEsrpDmnNeighborTrackedActivePortWeight':extremeEsrpDmnNeighborTrackedActivePortWeight,'extremeEsrpDomainAwareTable':extremeEsrpDomainAwareTable,'extremeEsrpDomainAwareEntry':extremeEsrpDomainAwareEntry,'extremeEsrpMasterMacAddress':extremeEsrpMasterMacAddress,'extremeEsrpMasterLastChanged':extremeEsrpMasterLastChanged,'extremeEsrpNumFdbFlushes':extremeEsrpNumFdbFlushes,'extremeEsrpHelloPktsReceived':extremeEsrpHelloPktsReceived,'extremeEsrpHelloPktsForwarded':extremeEsrpHelloPktsForwarded,'extremeEsrpDomainStatsTable':extremeEsrpDomainStatsTable,'extremeEsrpDomainStatsEntry':extremeEsrpDomainStatsEntry,'extremeEsrpLastStateChanged':extremeEsrpLastStateChanged,'extremeEsrpDomainNumTransitionsToMaster':extremeEsrpDomainNumTransitionsToMaster,'extremeEsrpNumTransitionsToPreMaster':extremeEsrpNumTransitionsToPreMaster,'extremeEsrpDomainNumTransitionsToSlave':extremeEsrpDomainNumTransitionsToSlave,'extremeEsrpNumTransitionsToNeutral':extremeEsrpNumTransitionsToNeutral,'extremeEsrpNumTransitionsToAware':extremeEsrpNumTransitionsToAware,'extremeEsrpHelloPktsReceived1':extremeEsrpHelloPktsReceived1,'extremeEsrpHelloPktsTransmitted':extremeEsrpHelloPktsTransmitted,'extremeEsrpAwareSelectForwardPortsTable':extremeEsrpAwareSelectForwardPortsTable,'extremeEsrpAwareSelectForwardPortsEntry':extremeEsrpAwareSelectForwardPortsEntry,_W:extremeEsrpAwareSelFwdListDmnName,_X:extremeEsrpAwareSelFwdListDmnGroup,'extremeEsrpAwareSelFwdListPortCount':extremeEsrpAwareSelFwdListPortCount,'extremeEsrpAwareSelFwdListPortList':extremeEsrpAwareSelFwdListPortList})