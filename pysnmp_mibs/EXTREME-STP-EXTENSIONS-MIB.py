_L='extremeStpPortPortIfIndex'
_K='extremeVlanIfIndex'
_J='EXTREME-VLAN-MIB'
_I='extremeStpDomainPortInstance'
_H='DisplayString'
_G='OctetString'
_F='Timeout'
_E='extremeStpDomainStpdInstance'
_D='Integer32'
_C='EXTREME-STP-EXTENSIONS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,extremeAgent=mibBuilder.importSymbols('EXTREME-BASE-MIB','PortList','extremeAgent')
extremeSlotNumber,=mibBuilder.importSymbols('EXTREME-SYSTEM-MIB','extremeSlotNumber')
extremeVlanIfIndex,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention','TruthValue')
extremeStp=ModuleIdentity((1,3,6,1,4,1,1916,1,17))
class BridgeId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class Timeout(Integer32):0
_ExtremeStpDomainTable_Object=MibTable
extremeStpDomainTable=_ExtremeStpDomainTable_Object((1,3,6,1,4,1,1916,1,17,1))
if mibBuilder.loadTexts:extremeStpDomainTable.setStatus(_A)
_ExtremeStpDomainEntry_Object=MibTableRow
extremeStpDomainEntry=_ExtremeStpDomainEntry_Object((1,3,6,1,4,1,1916,1,17,1,1))
extremeStpDomainEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:extremeStpDomainEntry.setStatus(_A)
_ExtremeStpDomainStpdInstance_Type=Integer32
_ExtremeStpDomainStpdInstance_Object=MibTableColumn
extremeStpDomainStpdInstance=_ExtremeStpDomainStpdInstance_Object((1,3,6,1,4,1,1916,1,17,1,1,1),_ExtremeStpDomainStpdInstance_Type())
extremeStpDomainStpdInstance.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:extremeStpDomainStpdInstance.setStatus(_A)
class _ExtremeStpDomainStpdName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_ExtremeStpDomainStpdName_Type.__name__=_H
_ExtremeStpDomainStpdName_Object=MibTableColumn
extremeStpDomainStpdName=_ExtremeStpDomainStpdName_Object((1,3,6,1,4,1,1916,1,17,1,1,2),_ExtremeStpDomainStpdName_Type())
extremeStpDomainStpdName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainStpdName.setStatus(_A)
_ExtremeStpDomainStpEnabled_Type=TruthValue
_ExtremeStpDomainStpEnabled_Object=MibTableColumn
extremeStpDomainStpEnabled=_ExtremeStpDomainStpEnabled_Object((1,3,6,1,4,1,1916,1,17,1,1,3),_ExtremeStpDomainStpEnabled_Type())
extremeStpDomainStpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainStpEnabled.setStatus(_A)
_ExtremeStpDomainRstpEnabled_Type=TruthValue
_ExtremeStpDomainRstpEnabled_Object=MibTableColumn
extremeStpDomainRstpEnabled=_ExtremeStpDomainRstpEnabled_Object((1,3,6,1,4,1,1916,1,17,1,1,4),_ExtremeStpDomainRstpEnabled_Type())
extremeStpDomainRstpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainRstpEnabled.setStatus(_A)
class _ExtremeStpDomainStpdTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_ExtremeStpDomainStpdTag_Type.__name__=_D
_ExtremeStpDomainStpdTag_Object=MibTableColumn
extremeStpDomainStpdTag=_ExtremeStpDomainStpdTag_Object((1,3,6,1,4,1,1916,1,17,1,1,5),_ExtremeStpDomainStpdTag_Type())
extremeStpDomainStpdTag.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainStpdTag.setStatus(_A)
_ExtremeStpDomainNumPorts_Type=Integer32
_ExtremeStpDomainNumPorts_Object=MibTableColumn
extremeStpDomainNumPorts=_ExtremeStpDomainNumPorts_Object((1,3,6,1,4,1,1916,1,17,1,1,6),_ExtremeStpDomainNumPorts_Type())
extremeStpDomainNumPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainNumPorts.setStatus(_A)
_ExtremeStpDomainBridgeId_Type=BridgeId
_ExtremeStpDomainBridgeId_Object=MibTableColumn
extremeStpDomainBridgeId=_ExtremeStpDomainBridgeId_Object((1,3,6,1,4,1,1916,1,17,1,1,7),_ExtremeStpDomainBridgeId_Type())
extremeStpDomainBridgeId.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainBridgeId.setStatus(_A)
class _ExtremeStpDomainBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeStpDomainBridgePriority_Type.__name__=_D
_ExtremeStpDomainBridgePriority_Object=MibTableColumn
extremeStpDomainBridgePriority=_ExtremeStpDomainBridgePriority_Object((1,3,6,1,4,1,1916,1,17,1,1,8),_ExtremeStpDomainBridgePriority_Type())
extremeStpDomainBridgePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainBridgePriority.setStatus(_A)
_ExtremeStpDomainDesignatedRoot_Type=BridgeId
_ExtremeStpDomainDesignatedRoot_Object=MibTableColumn
extremeStpDomainDesignatedRoot=_ExtremeStpDomainDesignatedRoot_Object((1,3,6,1,4,1,1916,1,17,1,1,9),_ExtremeStpDomainDesignatedRoot_Type())
extremeStpDomainDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainDesignatedRoot.setStatus(_A)
_ExtremeStpDomainRootPortIfIndex_Type=Integer32
_ExtremeStpDomainRootPortIfIndex_Object=MibTableColumn
extremeStpDomainRootPortIfIndex=_ExtremeStpDomainRootPortIfIndex_Object((1,3,6,1,4,1,1916,1,17,1,1,10),_ExtremeStpDomainRootPortIfIndex_Type())
extremeStpDomainRootPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainRootPortIfIndex.setStatus(_A)
_ExtremeStpDomainRootCost_Type=Integer32
_ExtremeStpDomainRootCost_Object=MibTableColumn
extremeStpDomainRootCost=_ExtremeStpDomainRootCost_Object((1,3,6,1,4,1,1916,1,17,1,1,11),_ExtremeStpDomainRootCost_Type())
extremeStpDomainRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainRootCost.setStatus(_A)
_ExtremeStpDomainRRFailoverEnabled_Type=TruthValue
_ExtremeStpDomainRRFailoverEnabled_Object=MibTableColumn
extremeStpDomainRRFailoverEnabled=_ExtremeStpDomainRRFailoverEnabled_Object((1,3,6,1,4,1,1916,1,17,1,1,12),_ExtremeStpDomainRRFailoverEnabled_Type())
extremeStpDomainRRFailoverEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainRRFailoverEnabled.setStatus(_A)
_ExtremeStpDomainMaxAge_Type=Timeout
_ExtremeStpDomainMaxAge_Object=MibTableColumn
extremeStpDomainMaxAge=_ExtremeStpDomainMaxAge_Object((1,3,6,1,4,1,1916,1,17,1,1,13),_ExtremeStpDomainMaxAge_Type())
extremeStpDomainMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainMaxAge.setStatus(_A)
_ExtremeStpDomainHelloTime_Type=Timeout
_ExtremeStpDomainHelloTime_Object=MibTableColumn
extremeStpDomainHelloTime=_ExtremeStpDomainHelloTime_Object((1,3,6,1,4,1,1916,1,17,1,1,14),_ExtremeStpDomainHelloTime_Type())
extremeStpDomainHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainHelloTime.setStatus(_A)
_ExtremeStpDomainForwardDelay_Type=Timeout
_ExtremeStpDomainForwardDelay_Object=MibTableColumn
extremeStpDomainForwardDelay=_ExtremeStpDomainForwardDelay_Object((1,3,6,1,4,1,1916,1,17,1,1,15),_ExtremeStpDomainForwardDelay_Type())
extremeStpDomainForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainForwardDelay.setStatus(_A)
class _ExtremeStpDomainBridgeMaxAge_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_ExtremeStpDomainBridgeMaxAge_Type.__name__=_F
_ExtremeStpDomainBridgeMaxAge_Object=MibTableColumn
extremeStpDomainBridgeMaxAge=_ExtremeStpDomainBridgeMaxAge_Object((1,3,6,1,4,1,1916,1,17,1,1,16),_ExtremeStpDomainBridgeMaxAge_Type())
extremeStpDomainBridgeMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainBridgeMaxAge.setStatus(_A)
class _ExtremeStpDomainBridgeHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_ExtremeStpDomainBridgeHelloTime_Type.__name__=_F
_ExtremeStpDomainBridgeHelloTime_Object=MibTableColumn
extremeStpDomainBridgeHelloTime=_ExtremeStpDomainBridgeHelloTime_Object((1,3,6,1,4,1,1916,1,17,1,1,17),_ExtremeStpDomainBridgeHelloTime_Type())
extremeStpDomainBridgeHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainBridgeHelloTime.setStatus(_A)
class _ExtremeStpDomainBridgeForwardDelay_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_ExtremeStpDomainBridgeForwardDelay_Type.__name__=_F
_ExtremeStpDomainBridgeForwardDelay_Object=MibTableColumn
extremeStpDomainBridgeForwardDelay=_ExtremeStpDomainBridgeForwardDelay_Object((1,3,6,1,4,1,1916,1,17,1,1,18),_ExtremeStpDomainBridgeForwardDelay_Type())
extremeStpDomainBridgeForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainBridgeForwardDelay.setStatus(_A)
_ExtremeStpDomainHoldTime_Type=Timeout
_ExtremeStpDomainHoldTime_Object=MibTableColumn
extremeStpDomainHoldTime=_ExtremeStpDomainHoldTime_Object((1,3,6,1,4,1,1916,1,17,1,1,19),_ExtremeStpDomainHoldTime_Type())
extremeStpDomainHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainHoldTime.setStatus(_A)
_ExtremeStpDomainTopChanges_Type=Counter32
_ExtremeStpDomainTopChanges_Object=MibTableColumn
extremeStpDomainTopChanges=_ExtremeStpDomainTopChanges_Object((1,3,6,1,4,1,1916,1,17,1,1,20),_ExtremeStpDomainTopChanges_Type())
extremeStpDomainTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainTopChanges.setStatus(_A)
_ExtremeStpDomainTimeSinceTopologyChange_Type=TimeTicks
_ExtremeStpDomainTimeSinceTopologyChange_Object=MibTableColumn
extremeStpDomainTimeSinceTopologyChange=_ExtremeStpDomainTimeSinceTopologyChange_Object((1,3,6,1,4,1,1916,1,17,1,1,21),_ExtremeStpDomainTimeSinceTopologyChange_Type())
extremeStpDomainTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainTimeSinceTopologyChange.setStatus(_A)
_ExtremeStpDomainRowStatus_Type=RowStatus
_ExtremeStpDomainRowStatus_Object=MibTableColumn
extremeStpDomainRowStatus=_ExtremeStpDomainRowStatus_Object((1,3,6,1,4,1,1916,1,17,1,1,22),_ExtremeStpDomainRowStatus_Type())
extremeStpDomainRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainRowStatus.setStatus(_A)
_ExtremeStpDomainPortInstance_Type=Integer32
_ExtremeStpDomainPortInstance_Object=MibTableColumn
extremeStpDomainPortInstance=_ExtremeStpDomainPortInstance_Object((1,3,6,1,4,1,1916,1,17,1,1,23),_ExtremeStpDomainPortInstance_Type())
extremeStpDomainPortInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainPortInstance.setStatus(_A)
class _ExtremeStpDomainStpdDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,180))
_ExtremeStpDomainStpdDescription_Type.__name__=_H
_ExtremeStpDomainStpdDescription_Object=MibTableColumn
extremeStpDomainStpdDescription=_ExtremeStpDomainStpdDescription_Object((1,3,6,1,4,1,1916,1,17,1,1,24),_ExtremeStpDomainStpdDescription_Type())
extremeStpDomainStpdDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpDomainStpdDescription.setStatus(_A)
_ExtremeStpPortTable_Object=MibTable
extremeStpPortTable=_ExtremeStpPortTable_Object((1,3,6,1,4,1,1916,1,17,2))
if mibBuilder.loadTexts:extremeStpPortTable.setStatus(_A)
_ExtremeStpPortEntry_Object=MibTableRow
extremeStpPortEntry=_ExtremeStpPortEntry_Object((1,3,6,1,4,1,1916,1,17,2,1))
extremeStpPortEntry.setIndexNames((0,_C,_E),(0,_C,_L))
if mibBuilder.loadTexts:extremeStpPortEntry.setStatus(_A)
_ExtremeStpPortPortIfIndex_Type=Integer32
_ExtremeStpPortPortIfIndex_Object=MibTableColumn
extremeStpPortPortIfIndex=_ExtremeStpPortPortIfIndex_Object((1,3,6,1,4,1,1916,1,17,2,1,1),_ExtremeStpPortPortIfIndex_Type())
extremeStpPortPortIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:extremeStpPortPortIfIndex.setStatus(_A)
_ExtremeStpPortStpEnabled_Type=TruthValue
_ExtremeStpPortStpEnabled_Object=MibTableColumn
extremeStpPortStpEnabled=_ExtremeStpPortStpEnabled_Object((1,3,6,1,4,1,1916,1,17,2,1,2),_ExtremeStpPortStpEnabled_Type())
extremeStpPortStpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpPortStpEnabled.setStatus(_A)
class _ExtremeStpPortPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dot1d',1),('emistp',2),('pvstp',3),('dot1w',4)))
_ExtremeStpPortPortMode_Type.__name__=_D
_ExtremeStpPortPortMode_Object=MibTableColumn
extremeStpPortPortMode=_ExtremeStpPortPortMode_Object((1,3,6,1,4,1,1916,1,17,2,1,3),_ExtremeStpPortPortMode_Type())
extremeStpPortPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpPortPortMode.setStatus(_A)
class _ExtremeStpPortPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('disabled',1),('blocking',2),('listening',3),('learning',4),('forwarding',5)))
_ExtremeStpPortPortState_Type.__name__=_D
_ExtremeStpPortPortState_Object=MibTableColumn
extremeStpPortPortState=_ExtremeStpPortPortState_Object((1,3,6,1,4,1,1916,1,17,2,1,4),_ExtremeStpPortPortState_Type())
extremeStpPortPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpPortPortState.setStatus(_A)
class _ExtremeStpPortPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_ExtremeStpPortPortPriority_Type.__name__=_D
_ExtremeStpPortPortPriority_Object=MibTableColumn
extremeStpPortPortPriority=_ExtremeStpPortPortPriority_Object((1,3,6,1,4,1,1916,1,17,2,1,5),_ExtremeStpPortPortPriority_Type())
extremeStpPortPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpPortPortPriority.setStatus(_A)
class _ExtremeStpPortPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ExtremeStpPortPortId_Type.__name__=_G
_ExtremeStpPortPortId_Object=MibTableColumn
extremeStpPortPortId=_ExtremeStpPortPortId_Object((1,3,6,1,4,1,1916,1,17,2,1,6),_ExtremeStpPortPortId_Type())
extremeStpPortPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpPortPortId.setStatus(_A)
class _ExtremeStpPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeStpPortPathCost_Type.__name__=_D
_ExtremeStpPortPathCost_Object=MibTableColumn
extremeStpPortPathCost=_ExtremeStpPortPathCost_Object((1,3,6,1,4,1,1916,1,17,2,1,7),_ExtremeStpPortPathCost_Type())
extremeStpPortPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpPortPathCost.setStatus(_A)
_ExtremeStpPortDesignatedCost_Type=Integer32
_ExtremeStpPortDesignatedCost_Object=MibTableColumn
extremeStpPortDesignatedCost=_ExtremeStpPortDesignatedCost_Object((1,3,6,1,4,1,1916,1,17,2,1,8),_ExtremeStpPortDesignatedCost_Type())
extremeStpPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpPortDesignatedCost.setStatus(_A)
_ExtremeStpPortDesignatedRoot_Type=BridgeId
_ExtremeStpPortDesignatedRoot_Object=MibTableColumn
extremeStpPortDesignatedRoot=_ExtremeStpPortDesignatedRoot_Object((1,3,6,1,4,1,1916,1,17,2,1,9),_ExtremeStpPortDesignatedRoot_Type())
extremeStpPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpPortDesignatedRoot.setStatus(_A)
_ExtremeStpPortDesignatedBridge_Type=BridgeId
_ExtremeStpPortDesignatedBridge_Object=MibTableColumn
extremeStpPortDesignatedBridge=_ExtremeStpPortDesignatedBridge_Object((1,3,6,1,4,1,1916,1,17,2,1,10),_ExtremeStpPortDesignatedBridge_Type())
extremeStpPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpPortDesignatedBridge.setStatus(_A)
class _ExtremeStpPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ExtremeStpPortDesignatedPort_Type.__name__=_G
_ExtremeStpPortDesignatedPort_Object=MibTableColumn
extremeStpPortDesignatedPort=_ExtremeStpPortDesignatedPort_Object((1,3,6,1,4,1,1916,1,17,2,1,11),_ExtremeStpPortDesignatedPort_Type())
extremeStpPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpPortDesignatedPort.setStatus(_A)
_ExtremeStpPortRowStatus_Type=RowStatus
_ExtremeStpPortRowStatus_Object=MibTableColumn
extremeStpPortRowStatus=_ExtremeStpPortRowStatus_Object((1,3,6,1,4,1,1916,1,17,2,1,12),_ExtremeStpPortRowStatus_Type())
extremeStpPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpPortRowStatus.setStatus(_A)
_ExtremeStpVlanPortTable_Object=MibTable
extremeStpVlanPortTable=_ExtremeStpVlanPortTable_Object((1,3,6,1,4,1,1916,1,17,3))
if mibBuilder.loadTexts:extremeStpVlanPortTable.setStatus(_A)
_ExtremeStpVlanPortEntry_Object=MibTableRow
extremeStpVlanPortEntry=_ExtremeStpVlanPortEntry_Object((1,3,6,1,4,1,1916,1,17,3,1))
extremeStpVlanPortEntry.setIndexNames((0,_J,_K),(0,_C,_E))
if mibBuilder.loadTexts:extremeStpVlanPortEntry.setStatus(_A)
_ExtremeStpVlanPortPortMask_Type=PortList
_ExtremeStpVlanPortPortMask_Object=MibTableColumn
extremeStpVlanPortPortMask=_ExtremeStpVlanPortPortMask_Object((1,3,6,1,4,1,1916,1,17,3,1,1),_ExtremeStpVlanPortPortMask_Type())
extremeStpVlanPortPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpVlanPortPortMask.setStatus(_A)
_ExtremeStpVlanPortRowStatus_Type=RowStatus
_ExtremeStpVlanPortRowStatus_Object=MibTableColumn
extremeStpVlanPortRowStatus=_ExtremeStpVlanPortRowStatus_Object((1,3,6,1,4,1,1916,1,17,3,1,2),_ExtremeStpVlanPortRowStatus_Type())
extremeStpVlanPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStpVlanPortRowStatus.setStatus(_A)
_ExtremeStpNotifications_ObjectIdentity=ObjectIdentity
extremeStpNotifications=_ExtremeStpNotifications_ObjectIdentity((1,3,6,1,4,1,1916,1,17,4))
_ExtremeStpNotificationsPrefix_ObjectIdentity=ObjectIdentity
extremeStpNotificationsPrefix=_ExtremeStpNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,17,4,0))
extremeStpEdgePortLoopDetected=NotificationType((1,3,6,1,4,1,1916,1,17,4,0,1))
extremeStpEdgePortLoopDetected.setObjects(*((_C,_E),(_C,_I)))
if mibBuilder.loadTexts:extremeStpEdgePortLoopDetected.setStatus(_A)
extremeStpPortLoopProtectEventDetected=NotificationType((1,3,6,1,4,1,1916,1,17,4,0,2))
extremeStpPortLoopProtectEventDetected.setObjects((_C,_I))
if mibBuilder.loadTexts:extremeStpPortLoopProtectEventDetected.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'BridgeId':BridgeId,_F:Timeout,'extremeStp':extremeStp,'extremeStpDomainTable':extremeStpDomainTable,'extremeStpDomainEntry':extremeStpDomainEntry,_E:extremeStpDomainStpdInstance,'extremeStpDomainStpdName':extremeStpDomainStpdName,'extremeStpDomainStpEnabled':extremeStpDomainStpEnabled,'extremeStpDomainRstpEnabled':extremeStpDomainRstpEnabled,'extremeStpDomainStpdTag':extremeStpDomainStpdTag,'extremeStpDomainNumPorts':extremeStpDomainNumPorts,'extremeStpDomainBridgeId':extremeStpDomainBridgeId,'extremeStpDomainBridgePriority':extremeStpDomainBridgePriority,'extremeStpDomainDesignatedRoot':extremeStpDomainDesignatedRoot,'extremeStpDomainRootPortIfIndex':extremeStpDomainRootPortIfIndex,'extremeStpDomainRootCost':extremeStpDomainRootCost,'extremeStpDomainRRFailoverEnabled':extremeStpDomainRRFailoverEnabled,'extremeStpDomainMaxAge':extremeStpDomainMaxAge,'extremeStpDomainHelloTime':extremeStpDomainHelloTime,'extremeStpDomainForwardDelay':extremeStpDomainForwardDelay,'extremeStpDomainBridgeMaxAge':extremeStpDomainBridgeMaxAge,'extremeStpDomainBridgeHelloTime':extremeStpDomainBridgeHelloTime,'extremeStpDomainBridgeForwardDelay':extremeStpDomainBridgeForwardDelay,'extremeStpDomainHoldTime':extremeStpDomainHoldTime,'extremeStpDomainTopChanges':extremeStpDomainTopChanges,'extremeStpDomainTimeSinceTopologyChange':extremeStpDomainTimeSinceTopologyChange,'extremeStpDomainRowStatus':extremeStpDomainRowStatus,_I:extremeStpDomainPortInstance,'extremeStpDomainStpdDescription':extremeStpDomainStpdDescription,'extremeStpPortTable':extremeStpPortTable,'extremeStpPortEntry':extremeStpPortEntry,_L:extremeStpPortPortIfIndex,'extremeStpPortStpEnabled':extremeStpPortStpEnabled,'extremeStpPortPortMode':extremeStpPortPortMode,'extremeStpPortPortState':extremeStpPortPortState,'extremeStpPortPortPriority':extremeStpPortPortPriority,'extremeStpPortPortId':extremeStpPortPortId,'extremeStpPortPathCost':extremeStpPortPathCost,'extremeStpPortDesignatedCost':extremeStpPortDesignatedCost,'extremeStpPortDesignatedRoot':extremeStpPortDesignatedRoot,'extremeStpPortDesignatedBridge':extremeStpPortDesignatedBridge,'extremeStpPortDesignatedPort':extremeStpPortDesignatedPort,'extremeStpPortRowStatus':extremeStpPortRowStatus,'extremeStpVlanPortTable':extremeStpVlanPortTable,'extremeStpVlanPortEntry':extremeStpVlanPortEntry,'extremeStpVlanPortPortMask':extremeStpVlanPortPortMask,'extremeStpVlanPortRowStatus':extremeStpVlanPortRowStatus,'extremeStpNotifications':extremeStpNotifications,'extremeStpNotificationsPrefix':extremeStpNotificationsPrefix,'extremeStpEdgePortLoopDetected':extremeStpEdgePortLoopDetected,'extremeStpPortLoopProtectEventDetected':extremeStpPortLoopProtectEventDetected})