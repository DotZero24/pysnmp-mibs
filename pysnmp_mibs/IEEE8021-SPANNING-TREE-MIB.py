_y='ieee8021SpanningTreeRstpPortGroup'
_x='ieee8021SpanningTreeRstpGroup'
_w='ieee8021SpanningTreeTopologyChange'
_v='ieee8021SpanningTreeNewRoot'
_u='ieee8021SpanningTreeRstpPortIsolatePort'
_t='ieee8021SpanningTreeRstpPortAutoIsolatePort'
_s='ieee8021SpanningTreeRstpPortAutoEdgePort'
_r='ieee8021SpanningTreeRstpPortAdminPathCost'
_q='ieee8021SpanningTreeRstpPortOperEdgePort'
_p='ieee8021SpanningTreeRstpPortAdminEdgePort'
_o='ieee8021SpanningTreeRstpPortProtocolMigration'
_n='ieee8021SpanningTreePortForwardTransitions'
_m='ieee8021SpanningTreePortDesignatedPort'
_l='ieee8021SpanningTreePortDesignatedBridge'
_k='ieee8021SpanningTreePortDesignatedCost'
_j='ieee8021SpanningTreePortDesignatedRoot'
_i='ieee8021SpanningTreePortPathCost'
_h='ieee8021SpanningTreePortEnabled'
_g='ieee8021SpanningTreePortState'
_f='ieee8021SpanningTreePortPriority'
_e='ieee8021SpanningTreeRstpTxHoldCount'
_d='ieee8021SpanningTreeVersion'
_c='ieee8021SpanningTreeBridgeForwardDelay'
_b='ieee8021SpanningTreeBridgeHelloTime'
_a='ieee8021SpanningTreeBridgeMaxAge'
_Z='ieee8021SpanningTreeForwardDelay'
_Y='ieee8021SpanningTreeHoldTime'
_X='ieee8021SpanningTreeHelloTime'
_W='ieee8021SpanningTreeMaxAge'
_V='ieee8021SpanningTreeRootPort'
_U='ieee8021SpanningTreeRootCost'
_T='ieee8021SpanningTreeDesignatedRoot'
_S='ieee8021SpanningTreeTopChanges'
_R='ieee8021SpanningTreeTimeSinceTopologyChange'
_Q='ieee8021SpanningTreePriority'
_P='ieee8021SpanningTreeProtocolSpecification'
_O='ieee8021SpanningTreePortExtensionEntry'
_N='ieee8021SpanningTreePort'
_M='ieee8021SpanningTreePortComponentId'
_L='ieee8021SpanningTreeComponentId'
_K='OctetString'
_J='ieee8021SpanningTreePortGroup'
_I='ieee8021SpanningTreeGroup'
_H='not-accessible'
_G='Timeout'
_F='centi-seconds'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='IEEE8021-SPANNING-TREE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,Timeout=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId',_G)
IEEE8021BridgePortNumber,IEEE8021PbbComponentIdentifier,ieee802dot1mibs=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021BridgePortNumber','IEEE8021PbbComponentIdentifier','ieee802dot1mibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ieee8021SpanningTreeMib=ModuleIdentity((1,3,111,2,802,1,1,3))
if mibBuilder.loadTexts:ieee8021SpanningTreeMib.setRevisions(('2018-06-28 00:00','2014-12-15 00:00','2011-03-24 00:00','2008-10-15 00:00'))
_Ieee8021SpanningTreeNotifications_ObjectIdentity=ObjectIdentity
ieee8021SpanningTreeNotifications=_Ieee8021SpanningTreeNotifications_ObjectIdentity((1,3,111,2,802,1,1,3,0))
_Ieee8021SpanningTreeObjects_ObjectIdentity=ObjectIdentity
ieee8021SpanningTreeObjects=_Ieee8021SpanningTreeObjects_ObjectIdentity((1,3,111,2,802,1,1,3,1))
_Ieee8021SpanningTreeTable_Object=MibTable
ieee8021SpanningTreeTable=_Ieee8021SpanningTreeTable_Object((1,3,111,2,802,1,1,3,1,1))
if mibBuilder.loadTexts:ieee8021SpanningTreeTable.setStatus(_A)
_Ieee8021SpanningTreeEntry_Object=MibTableRow
ieee8021SpanningTreeEntry=_Ieee8021SpanningTreeEntry_Object((1,3,111,2,802,1,1,3,1,1,1))
ieee8021SpanningTreeEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:ieee8021SpanningTreeEntry.setStatus(_A)
_Ieee8021SpanningTreeComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021SpanningTreeComponentId_Object=MibTableColumn
ieee8021SpanningTreeComponentId=_Ieee8021SpanningTreeComponentId_Object((1,3,111,2,802,1,1,3,1,1,1,1),_Ieee8021SpanningTreeComponentId_Type())
ieee8021SpanningTreeComponentId.setMaxAccess(_H)
if mibBuilder.loadTexts:ieee8021SpanningTreeComponentId.setStatus(_A)
class _Ieee8021SpanningTreeProtocolSpecification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('decLb100',2),('ieee8021d',3),('ieee8021q',4)))
_Ieee8021SpanningTreeProtocolSpecification_Type.__name__=_E
_Ieee8021SpanningTreeProtocolSpecification_Object=MibTableColumn
ieee8021SpanningTreeProtocolSpecification=_Ieee8021SpanningTreeProtocolSpecification_Object((1,3,111,2,802,1,1,3,1,1,1,2),_Ieee8021SpanningTreeProtocolSpecification_Type())
ieee8021SpanningTreeProtocolSpecification.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreeProtocolSpecification.setStatus(_A)
class _Ieee8021SpanningTreePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ieee8021SpanningTreePriority_Type.__name__=_E
_Ieee8021SpanningTreePriority_Object=MibTableColumn
ieee8021SpanningTreePriority=_Ieee8021SpanningTreePriority_Object((1,3,111,2,802,1,1,3,1,1,1,3),_Ieee8021SpanningTreePriority_Type())
ieee8021SpanningTreePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SpanningTreePriority.setStatus(_A)
_Ieee8021SpanningTreeTimeSinceTopologyChange_Type=TimeTicks
_Ieee8021SpanningTreeTimeSinceTopologyChange_Object=MibTableColumn
ieee8021SpanningTreeTimeSinceTopologyChange=_Ieee8021SpanningTreeTimeSinceTopologyChange_Object((1,3,111,2,802,1,1,3,1,1,1,4),_Ieee8021SpanningTreeTimeSinceTopologyChange_Type())
ieee8021SpanningTreeTimeSinceTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreeTimeSinceTopologyChange.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SpanningTreeTimeSinceTopologyChange.setUnits(_F)
_Ieee8021SpanningTreeTopChanges_Type=Counter64
_Ieee8021SpanningTreeTopChanges_Object=MibTableColumn
ieee8021SpanningTreeTopChanges=_Ieee8021SpanningTreeTopChanges_Object((1,3,111,2,802,1,1,3,1,1,1,5),_Ieee8021SpanningTreeTopChanges_Type())
ieee8021SpanningTreeTopChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreeTopChanges.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SpanningTreeTopChanges.setUnits('topology changes')
_Ieee8021SpanningTreeDesignatedRoot_Type=BridgeId
_Ieee8021SpanningTreeDesignatedRoot_Object=MibTableColumn
ieee8021SpanningTreeDesignatedRoot=_Ieee8021SpanningTreeDesignatedRoot_Object((1,3,111,2,802,1,1,3,1,1,1,6),_Ieee8021SpanningTreeDesignatedRoot_Type())
ieee8021SpanningTreeDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreeDesignatedRoot.setStatus(_A)
_Ieee8021SpanningTreeRootCost_Type=Integer32
_Ieee8021SpanningTreeRootCost_Object=MibTableColumn
ieee8021SpanningTreeRootCost=_Ieee8021SpanningTreeRootCost_Object((1,3,111,2,802,1,1,3,1,1,1,7),_Ieee8021SpanningTreeRootCost_Type())
ieee8021SpanningTreeRootCost.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreeRootCost.setStatus(_A)
_Ieee8021SpanningTreeRootPort_Type=IEEE8021BridgePortNumber
_Ieee8021SpanningTreeRootPort_Object=MibTableColumn
ieee8021SpanningTreeRootPort=_Ieee8021SpanningTreeRootPort_Object((1,3,111,2,802,1,1,3,1,1,1,8),_Ieee8021SpanningTreeRootPort_Type())
ieee8021SpanningTreeRootPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreeRootPort.setStatus(_A)
_Ieee8021SpanningTreeMaxAge_Type=Timeout
_Ieee8021SpanningTreeMaxAge_Object=MibTableColumn
ieee8021SpanningTreeMaxAge=_Ieee8021SpanningTreeMaxAge_Object((1,3,111,2,802,1,1,3,1,1,1,9),_Ieee8021SpanningTreeMaxAge_Type())
ieee8021SpanningTreeMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreeMaxAge.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SpanningTreeMaxAge.setUnits(_F)
_Ieee8021SpanningTreeHelloTime_Type=Timeout
_Ieee8021SpanningTreeHelloTime_Object=MibTableColumn
ieee8021SpanningTreeHelloTime=_Ieee8021SpanningTreeHelloTime_Object((1,3,111,2,802,1,1,3,1,1,1,10),_Ieee8021SpanningTreeHelloTime_Type())
ieee8021SpanningTreeHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreeHelloTime.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SpanningTreeHelloTime.setUnits(_F)
_Ieee8021SpanningTreeHoldTime_Type=Integer32
_Ieee8021SpanningTreeHoldTime_Object=MibTableColumn
ieee8021SpanningTreeHoldTime=_Ieee8021SpanningTreeHoldTime_Object((1,3,111,2,802,1,1,3,1,1,1,11),_Ieee8021SpanningTreeHoldTime_Type())
ieee8021SpanningTreeHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreeHoldTime.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SpanningTreeHoldTime.setUnits(_F)
_Ieee8021SpanningTreeForwardDelay_Type=Timeout
_Ieee8021SpanningTreeForwardDelay_Object=MibTableColumn
ieee8021SpanningTreeForwardDelay=_Ieee8021SpanningTreeForwardDelay_Object((1,3,111,2,802,1,1,3,1,1,1,12),_Ieee8021SpanningTreeForwardDelay_Type())
ieee8021SpanningTreeForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreeForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SpanningTreeForwardDelay.setUnits(_F)
class _Ieee8021SpanningTreeBridgeMaxAge_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_Ieee8021SpanningTreeBridgeMaxAge_Type.__name__=_G
_Ieee8021SpanningTreeBridgeMaxAge_Object=MibTableColumn
ieee8021SpanningTreeBridgeMaxAge=_Ieee8021SpanningTreeBridgeMaxAge_Object((1,3,111,2,802,1,1,3,1,1,1,13),_Ieee8021SpanningTreeBridgeMaxAge_Type())
ieee8021SpanningTreeBridgeMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SpanningTreeBridgeMaxAge.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SpanningTreeBridgeMaxAge.setUnits(_F)
class _Ieee8021SpanningTreeBridgeHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_Ieee8021SpanningTreeBridgeHelloTime_Type.__name__=_G
_Ieee8021SpanningTreeBridgeHelloTime_Object=MibTableColumn
ieee8021SpanningTreeBridgeHelloTime=_Ieee8021SpanningTreeBridgeHelloTime_Object((1,3,111,2,802,1,1,3,1,1,1,14),_Ieee8021SpanningTreeBridgeHelloTime_Type())
ieee8021SpanningTreeBridgeHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SpanningTreeBridgeHelloTime.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SpanningTreeBridgeHelloTime.setUnits(_F)
class _Ieee8021SpanningTreeBridgeForwardDelay_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_Ieee8021SpanningTreeBridgeForwardDelay_Type.__name__=_G
_Ieee8021SpanningTreeBridgeForwardDelay_Object=MibTableColumn
ieee8021SpanningTreeBridgeForwardDelay=_Ieee8021SpanningTreeBridgeForwardDelay_Object((1,3,111,2,802,1,1,3,1,1,1,15),_Ieee8021SpanningTreeBridgeForwardDelay_Type())
ieee8021SpanningTreeBridgeForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SpanningTreeBridgeForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SpanningTreeBridgeForwardDelay.setUnits(_F)
class _Ieee8021SpanningTreeVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*(('stp',0),('rstp',2),('mstp',3)))
_Ieee8021SpanningTreeVersion_Type.__name__=_E
_Ieee8021SpanningTreeVersion_Object=MibTableColumn
ieee8021SpanningTreeVersion=_Ieee8021SpanningTreeVersion_Object((1,3,111,2,802,1,1,3,1,1,1,16),_Ieee8021SpanningTreeVersion_Type())
ieee8021SpanningTreeVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SpanningTreeVersion.setStatus(_A)
class _Ieee8021SpanningTreeRstpTxHoldCount_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Ieee8021SpanningTreeRstpTxHoldCount_Type.__name__=_E
_Ieee8021SpanningTreeRstpTxHoldCount_Object=MibTableColumn
ieee8021SpanningTreeRstpTxHoldCount=_Ieee8021SpanningTreeRstpTxHoldCount_Object((1,3,111,2,802,1,1,3,1,1,1,17),_Ieee8021SpanningTreeRstpTxHoldCount_Type())
ieee8021SpanningTreeRstpTxHoldCount.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SpanningTreeRstpTxHoldCount.setStatus(_A)
_Ieee8021SpanningTreePortTable_Object=MibTable
ieee8021SpanningTreePortTable=_Ieee8021SpanningTreePortTable_Object((1,3,111,2,802,1,1,3,1,2))
if mibBuilder.loadTexts:ieee8021SpanningTreePortTable.setStatus(_A)
_Ieee8021SpanningTreePortEntry_Object=MibTableRow
ieee8021SpanningTreePortEntry=_Ieee8021SpanningTreePortEntry_Object((1,3,111,2,802,1,1,3,1,2,1))
ieee8021SpanningTreePortEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:ieee8021SpanningTreePortEntry.setStatus(_A)
_Ieee8021SpanningTreePortComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021SpanningTreePortComponentId_Object=MibTableColumn
ieee8021SpanningTreePortComponentId=_Ieee8021SpanningTreePortComponentId_Object((1,3,111,2,802,1,1,3,1,2,1,1),_Ieee8021SpanningTreePortComponentId_Type())
ieee8021SpanningTreePortComponentId.setMaxAccess(_H)
if mibBuilder.loadTexts:ieee8021SpanningTreePortComponentId.setStatus(_A)
_Ieee8021SpanningTreePort_Type=IEEE8021BridgePortNumber
_Ieee8021SpanningTreePort_Object=MibTableColumn
ieee8021SpanningTreePort=_Ieee8021SpanningTreePort_Object((1,3,111,2,802,1,1,3,1,2,1,2),_Ieee8021SpanningTreePort_Type())
ieee8021SpanningTreePort.setMaxAccess(_H)
if mibBuilder.loadTexts:ieee8021SpanningTreePort.setStatus(_A)
class _Ieee8021SpanningTreePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Ieee8021SpanningTreePortPriority_Type.__name__=_E
_Ieee8021SpanningTreePortPriority_Object=MibTableColumn
ieee8021SpanningTreePortPriority=_Ieee8021SpanningTreePortPriority_Object((1,3,111,2,802,1,1,3,1,2,1,3),_Ieee8021SpanningTreePortPriority_Type())
ieee8021SpanningTreePortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SpanningTreePortPriority.setStatus(_A)
class _Ieee8021SpanningTreePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('disabled',1),('blocking',2),('listening',3),('learning',4),('forwarding',5),('broken',6)))
_Ieee8021SpanningTreePortState_Type.__name__=_E
_Ieee8021SpanningTreePortState_Object=MibTableColumn
ieee8021SpanningTreePortState=_Ieee8021SpanningTreePortState_Object((1,3,111,2,802,1,1,3,1,2,1,4),_Ieee8021SpanningTreePortState_Type())
ieee8021SpanningTreePortState.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreePortState.setStatus(_A)
_Ieee8021SpanningTreePortEnabled_Type=TruthValue
_Ieee8021SpanningTreePortEnabled_Object=MibTableColumn
ieee8021SpanningTreePortEnabled=_Ieee8021SpanningTreePortEnabled_Object((1,3,111,2,802,1,1,3,1,2,1,5),_Ieee8021SpanningTreePortEnabled_Type())
ieee8021SpanningTreePortEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SpanningTreePortEnabled.setStatus(_A)
class _Ieee8021SpanningTreePortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_Ieee8021SpanningTreePortPathCost_Type.__name__=_E
_Ieee8021SpanningTreePortPathCost_Object=MibTableColumn
ieee8021SpanningTreePortPathCost=_Ieee8021SpanningTreePortPathCost_Object((1,3,111,2,802,1,1,3,1,2,1,6),_Ieee8021SpanningTreePortPathCost_Type())
ieee8021SpanningTreePortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SpanningTreePortPathCost.setStatus(_A)
_Ieee8021SpanningTreePortDesignatedRoot_Type=BridgeId
_Ieee8021SpanningTreePortDesignatedRoot_Object=MibTableColumn
ieee8021SpanningTreePortDesignatedRoot=_Ieee8021SpanningTreePortDesignatedRoot_Object((1,3,111,2,802,1,1,3,1,2,1,7),_Ieee8021SpanningTreePortDesignatedRoot_Type())
ieee8021SpanningTreePortDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreePortDesignatedRoot.setStatus(_A)
_Ieee8021SpanningTreePortDesignatedCost_Type=Integer32
_Ieee8021SpanningTreePortDesignatedCost_Object=MibTableColumn
ieee8021SpanningTreePortDesignatedCost=_Ieee8021SpanningTreePortDesignatedCost_Object((1,3,111,2,802,1,1,3,1,2,1,8),_Ieee8021SpanningTreePortDesignatedCost_Type())
ieee8021SpanningTreePortDesignatedCost.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreePortDesignatedCost.setStatus(_A)
_Ieee8021SpanningTreePortDesignatedBridge_Type=BridgeId
_Ieee8021SpanningTreePortDesignatedBridge_Object=MibTableColumn
ieee8021SpanningTreePortDesignatedBridge=_Ieee8021SpanningTreePortDesignatedBridge_Object((1,3,111,2,802,1,1,3,1,2,1,9),_Ieee8021SpanningTreePortDesignatedBridge_Type())
ieee8021SpanningTreePortDesignatedBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreePortDesignatedBridge.setStatus(_A)
class _Ieee8021SpanningTreePortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_Ieee8021SpanningTreePortDesignatedPort_Type.__name__=_K
_Ieee8021SpanningTreePortDesignatedPort_Object=MibTableColumn
ieee8021SpanningTreePortDesignatedPort=_Ieee8021SpanningTreePortDesignatedPort_Object((1,3,111,2,802,1,1,3,1,2,1,10),_Ieee8021SpanningTreePortDesignatedPort_Type())
ieee8021SpanningTreePortDesignatedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreePortDesignatedPort.setStatus(_A)
_Ieee8021SpanningTreePortForwardTransitions_Type=Counter64
_Ieee8021SpanningTreePortForwardTransitions_Object=MibTableColumn
ieee8021SpanningTreePortForwardTransitions=_Ieee8021SpanningTreePortForwardTransitions_Object((1,3,111,2,802,1,1,3,1,2,1,11),_Ieee8021SpanningTreePortForwardTransitions_Type())
ieee8021SpanningTreePortForwardTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreePortForwardTransitions.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SpanningTreePortForwardTransitions.setUnits('forwarding transitions')
_Ieee8021SpanningTreeRstpPortProtocolMigration_Type=TruthValue
_Ieee8021SpanningTreeRstpPortProtocolMigration_Object=MibTableColumn
ieee8021SpanningTreeRstpPortProtocolMigration=_Ieee8021SpanningTreeRstpPortProtocolMigration_Object((1,3,111,2,802,1,1,3,1,2,1,12),_Ieee8021SpanningTreeRstpPortProtocolMigration_Type())
ieee8021SpanningTreeRstpPortProtocolMigration.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SpanningTreeRstpPortProtocolMigration.setStatus(_A)
_Ieee8021SpanningTreeRstpPortAdminEdgePort_Type=TruthValue
_Ieee8021SpanningTreeRstpPortAdminEdgePort_Object=MibTableColumn
ieee8021SpanningTreeRstpPortAdminEdgePort=_Ieee8021SpanningTreeRstpPortAdminEdgePort_Object((1,3,111,2,802,1,1,3,1,2,1,13),_Ieee8021SpanningTreeRstpPortAdminEdgePort_Type())
ieee8021SpanningTreeRstpPortAdminEdgePort.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SpanningTreeRstpPortAdminEdgePort.setStatus(_A)
_Ieee8021SpanningTreeRstpPortOperEdgePort_Type=TruthValue
_Ieee8021SpanningTreeRstpPortOperEdgePort_Object=MibTableColumn
ieee8021SpanningTreeRstpPortOperEdgePort=_Ieee8021SpanningTreeRstpPortOperEdgePort_Object((1,3,111,2,802,1,1,3,1,2,1,14),_Ieee8021SpanningTreeRstpPortOperEdgePort_Type())
ieee8021SpanningTreeRstpPortOperEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreeRstpPortOperEdgePort.setStatus(_A)
class _Ieee8021SpanningTreeRstpPortAdminPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_Ieee8021SpanningTreeRstpPortAdminPathCost_Type.__name__=_E
_Ieee8021SpanningTreeRstpPortAdminPathCost_Object=MibTableColumn
ieee8021SpanningTreeRstpPortAdminPathCost=_Ieee8021SpanningTreeRstpPortAdminPathCost_Object((1,3,111,2,802,1,1,3,1,2,1,15),_Ieee8021SpanningTreeRstpPortAdminPathCost_Type())
ieee8021SpanningTreeRstpPortAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SpanningTreeRstpPortAdminPathCost.setStatus(_A)
_Ieee8021SpanningTreePortExtensionTable_Object=MibTable
ieee8021SpanningTreePortExtensionTable=_Ieee8021SpanningTreePortExtensionTable_Object((1,3,111,2,802,1,1,3,1,3))
if mibBuilder.loadTexts:ieee8021SpanningTreePortExtensionTable.setStatus(_A)
_Ieee8021SpanningTreePortExtensionEntry_Object=MibTableRow
ieee8021SpanningTreePortExtensionEntry=_Ieee8021SpanningTreePortExtensionEntry_Object((1,3,111,2,802,1,1,3,1,3,1))
if mibBuilder.loadTexts:ieee8021SpanningTreePortExtensionEntry.setStatus(_A)
_Ieee8021SpanningTreeRstpPortAutoEdgePort_Type=TruthValue
_Ieee8021SpanningTreeRstpPortAutoEdgePort_Object=MibTableColumn
ieee8021SpanningTreeRstpPortAutoEdgePort=_Ieee8021SpanningTreeRstpPortAutoEdgePort_Object((1,3,111,2,802,1,1,3,1,3,1,1),_Ieee8021SpanningTreeRstpPortAutoEdgePort_Type())
ieee8021SpanningTreeRstpPortAutoEdgePort.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SpanningTreeRstpPortAutoEdgePort.setStatus(_A)
_Ieee8021SpanningTreeRstpPortAutoIsolatePort_Type=TruthValue
_Ieee8021SpanningTreeRstpPortAutoIsolatePort_Object=MibTableColumn
ieee8021SpanningTreeRstpPortAutoIsolatePort=_Ieee8021SpanningTreeRstpPortAutoIsolatePort_Object((1,3,111,2,802,1,1,3,1,3,1,2),_Ieee8021SpanningTreeRstpPortAutoIsolatePort_Type())
ieee8021SpanningTreeRstpPortAutoIsolatePort.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreeRstpPortAutoIsolatePort.setStatus(_A)
_Ieee8021SpanningTreeRstpPortIsolatePort_Type=TruthValue
_Ieee8021SpanningTreeRstpPortIsolatePort_Object=MibTableColumn
ieee8021SpanningTreeRstpPortIsolatePort=_Ieee8021SpanningTreeRstpPortIsolatePort_Object((1,3,111,2,802,1,1,3,1,3,1,3),_Ieee8021SpanningTreeRstpPortIsolatePort_Type())
ieee8021SpanningTreeRstpPortIsolatePort.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SpanningTreeRstpPortIsolatePort.setStatus(_A)
_Ieee8021SpanningTreeConformance_ObjectIdentity=ObjectIdentity
ieee8021SpanningTreeConformance=_Ieee8021SpanningTreeConformance_ObjectIdentity((1,3,111,2,802,1,1,3,2))
_Ieee8021SpanningTreeCompliances_ObjectIdentity=ObjectIdentity
ieee8021SpanningTreeCompliances=_Ieee8021SpanningTreeCompliances_ObjectIdentity((1,3,111,2,802,1,1,3,2,1))
_Ieee8021SpanningTreeGroups_ObjectIdentity=ObjectIdentity
ieee8021SpanningTreeGroups=_Ieee8021SpanningTreeGroups_ObjectIdentity((1,3,111,2,802,1,1,3,2,2))
ieee8021SpanningTreePortEntry.registerAugmentions((_B,_O))
ieee8021SpanningTreePortExtensionEntry.setIndexNames(*ieee8021SpanningTreePortEntry.getIndexNames())
ieee8021SpanningTreeGroup=ObjectGroup((1,3,111,2,802,1,1,3,2,2,1))
ieee8021SpanningTreeGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ieee8021SpanningTreeGroup.setStatus(_A)
ieee8021SpanningTreeRstpGroup=ObjectGroup((1,3,111,2,802,1,1,3,2,2,2))
ieee8021SpanningTreeRstpGroup.setObjects((_B,_e))
if mibBuilder.loadTexts:ieee8021SpanningTreeRstpGroup.setStatus(_A)
ieee8021SpanningTreePortGroup=ObjectGroup((1,3,111,2,802,1,1,3,2,2,3))
ieee8021SpanningTreePortGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:ieee8021SpanningTreePortGroup.setStatus(_A)
ieee8021SpanningTreeRstpPortGroup=ObjectGroup((1,3,111,2,802,1,1,3,2,2,4))
ieee8021SpanningTreeRstpPortGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:ieee8021SpanningTreeRstpPortGroup.setStatus(_A)
ieee8021SpanningTreeRstpFragileGroup=ObjectGroup((1,3,111,2,802,1,1,3,2,2,6))
ieee8021SpanningTreeRstpFragileGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ieee8021SpanningTreeRstpFragileGroup.setStatus(_A)
ieee8021SpanningTreeNewRoot=NotificationType((1,3,111,2,802,1,1,3,0,1))
if mibBuilder.loadTexts:ieee8021SpanningTreeNewRoot.setStatus(_A)
ieee8021SpanningTreeTopologyChange=NotificationType((1,3,111,2,802,1,1,3,0,2))
if mibBuilder.loadTexts:ieee8021SpanningTreeTopologyChange.setStatus(_A)
ieee8021SpanningTreeNotificationGroup=NotificationGroup((1,3,111,2,802,1,1,3,2,2,5))
ieee8021SpanningTreeNotificationGroup.setObjects(*((_B,_v),(_B,_w)))
if mibBuilder.loadTexts:ieee8021SpanningTreeNotificationGroup.setStatus(_A)
ieee8021SpanningTreeCompliance=ModuleCompliance((1,3,111,2,802,1,1,3,2,1,1))
ieee8021SpanningTreeCompliance.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:ieee8021SpanningTreeCompliance.setStatus(_A)
ieee8021SpanningTreeRstpCompliance=ModuleCompliance((1,3,111,2,802,1,1,3,2,1,2))
ieee8021SpanningTreeRstpCompliance.setObjects(*((_B,_I),(_B,_x),(_B,_J),(_B,_y)))
if mibBuilder.loadTexts:ieee8021SpanningTreeRstpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ieee8021SpanningTreeMib':ieee8021SpanningTreeMib,'ieee8021SpanningTreeNotifications':ieee8021SpanningTreeNotifications,_v:ieee8021SpanningTreeNewRoot,_w:ieee8021SpanningTreeTopologyChange,'ieee8021SpanningTreeObjects':ieee8021SpanningTreeObjects,'ieee8021SpanningTreeTable':ieee8021SpanningTreeTable,'ieee8021SpanningTreeEntry':ieee8021SpanningTreeEntry,_L:ieee8021SpanningTreeComponentId,_P:ieee8021SpanningTreeProtocolSpecification,_Q:ieee8021SpanningTreePriority,_R:ieee8021SpanningTreeTimeSinceTopologyChange,_S:ieee8021SpanningTreeTopChanges,_T:ieee8021SpanningTreeDesignatedRoot,_U:ieee8021SpanningTreeRootCost,_V:ieee8021SpanningTreeRootPort,_W:ieee8021SpanningTreeMaxAge,_X:ieee8021SpanningTreeHelloTime,_Y:ieee8021SpanningTreeHoldTime,_Z:ieee8021SpanningTreeForwardDelay,_a:ieee8021SpanningTreeBridgeMaxAge,_b:ieee8021SpanningTreeBridgeHelloTime,_c:ieee8021SpanningTreeBridgeForwardDelay,_d:ieee8021SpanningTreeVersion,_e:ieee8021SpanningTreeRstpTxHoldCount,'ieee8021SpanningTreePortTable':ieee8021SpanningTreePortTable,'ieee8021SpanningTreePortEntry':ieee8021SpanningTreePortEntry,_M:ieee8021SpanningTreePortComponentId,_N:ieee8021SpanningTreePort,_f:ieee8021SpanningTreePortPriority,_g:ieee8021SpanningTreePortState,_h:ieee8021SpanningTreePortEnabled,_i:ieee8021SpanningTreePortPathCost,_j:ieee8021SpanningTreePortDesignatedRoot,_k:ieee8021SpanningTreePortDesignatedCost,_l:ieee8021SpanningTreePortDesignatedBridge,_m:ieee8021SpanningTreePortDesignatedPort,_n:ieee8021SpanningTreePortForwardTransitions,_o:ieee8021SpanningTreeRstpPortProtocolMigration,_p:ieee8021SpanningTreeRstpPortAdminEdgePort,_q:ieee8021SpanningTreeRstpPortOperEdgePort,_r:ieee8021SpanningTreeRstpPortAdminPathCost,'ieee8021SpanningTreePortExtensionTable':ieee8021SpanningTreePortExtensionTable,_O:ieee8021SpanningTreePortExtensionEntry,_s:ieee8021SpanningTreeRstpPortAutoEdgePort,_t:ieee8021SpanningTreeRstpPortAutoIsolatePort,_u:ieee8021SpanningTreeRstpPortIsolatePort,'ieee8021SpanningTreeConformance':ieee8021SpanningTreeConformance,'ieee8021SpanningTreeCompliances':ieee8021SpanningTreeCompliances,'ieee8021SpanningTreeCompliance':ieee8021SpanningTreeCompliance,'ieee8021SpanningTreeRstpCompliance':ieee8021SpanningTreeRstpCompliance,'ieee8021SpanningTreeGroups':ieee8021SpanningTreeGroups,_I:ieee8021SpanningTreeGroup,_x:ieee8021SpanningTreeRstpGroup,_J:ieee8021SpanningTreePortGroup,_y:ieee8021SpanningTreeRstpPortGroup,'ieee8021SpanningTreeNotificationGroup':ieee8021SpanningTreeNotificationGroup,'ieee8021SpanningTreeRstpFragileGroup':ieee8021SpanningTreeRstpFragileGroup})