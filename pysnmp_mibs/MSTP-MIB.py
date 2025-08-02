_O='dot1sStpInstDesignatedRoot'
_N='dot1sStpVlanIndex'
_M='DisplayString'
_L='Unsigned32'
_K='OctetString'
_J='not-accessible'
_I='dot1sStpInstId'
_H='dot1sStpPort'
_G='TruthValue'
_F='Timeout'
_E='MSTP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,Timeout,dot1dBridge=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId',_F,'dot1dBridge')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','RowStatus','TextualConvention',_G)
mstpMib=ModuleIdentity((1,3,6,1,2,1,17,8))
if mibBuilder.loadTexts:mstpMib.setRevisions(('1904-12-05 00:00',))
_MstpMIBObjects_ObjectIdentity=ObjectIdentity
mstpMIBObjects=_MstpMIBObjects_ObjectIdentity((1,3,6,1,2,1,17,8,1))
_Dot1sStp_ObjectIdentity=ObjectIdentity
dot1sStp=_Dot1sStp_ObjectIdentity((1,3,6,1,2,1,17,8,1,1))
class _Dot1sStpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dot1sStpName_Type.__name__=_M
_Dot1sStpName_Object=MibScalar
dot1sStpName=_Dot1sStpName_Object((1,3,6,1,2,1,17,8,1,1,1),_Dot1sStpName_Type())
dot1sStpName.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpName.setStatus(_A)
class _Dot1sStpRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1sStpRevision_Type.__name__=_C
_Dot1sStpRevision_Object=MibScalar
dot1sStpRevision=_Dot1sStpRevision_Object((1,3,6,1,2,1,17,8,1,1,2),_Dot1sStpRevision_Type())
dot1sStpRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpRevision.setStatus(_A)
class _Dot1sStpEnable_Type(TruthValue):defaultValue=2
_Dot1sStpEnable_Type.__name__=_G
_Dot1sStpEnable_Object=MibScalar
dot1sStpEnable=_Dot1sStpEnable_Object((1,3,6,1,2,1,17,8,1,1,3),_Dot1sStpEnable_Type())
dot1sStpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpEnable.setStatus(_A)
class _Dot1sStpBridgeMaxAge_Type(Timeout):defaultValue=20;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_Dot1sStpBridgeMaxAge_Type.__name__=_F
_Dot1sStpBridgeMaxAge_Object=MibScalar
dot1sStpBridgeMaxAge=_Dot1sStpBridgeMaxAge_Object((1,3,6,1,2,1,17,8,1,1,4),_Dot1sStpBridgeMaxAge_Type())
dot1sStpBridgeMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpBridgeMaxAge.setStatus(_A)
class _Dot1sStpBridgeHelloTime_Type(Timeout):defaultValue=2;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Dot1sStpBridgeHelloTime_Type.__name__=_F
_Dot1sStpBridgeHelloTime_Object=MibScalar
dot1sStpBridgeHelloTime=_Dot1sStpBridgeHelloTime_Object((1,3,6,1,2,1,17,8,1,1,5),_Dot1sStpBridgeHelloTime_Type())
dot1sStpBridgeHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpBridgeHelloTime.setStatus(_A)
class _Dot1sStpBridgeForwardDelay_Type(Timeout):defaultValue=15;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_Dot1sStpBridgeForwardDelay_Type.__name__=_F
_Dot1sStpBridgeForwardDelay_Object=MibScalar
dot1sStpBridgeForwardDelay=_Dot1sStpBridgeForwardDelay_Object((1,3,6,1,2,1,17,8,1,1,6),_Dot1sStpBridgeForwardDelay_Type())
dot1sStpBridgeForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpBridgeForwardDelay.setStatus(_A)
class _Dot1sStpBridgeMaxHops_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Dot1sStpBridgeMaxHops_Type.__name__=_L
_Dot1sStpBridgeMaxHops_Object=MibScalar
dot1sStpBridgeMaxHops=_Dot1sStpBridgeMaxHops_Object((1,3,6,1,2,1,17,8,1,1,7),_Dot1sStpBridgeMaxHops_Type())
dot1sStpBridgeMaxHops.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpBridgeMaxHops.setStatus(_A)
class _Dot1sStpTxHoldCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Dot1sStpTxHoldCount_Type.__name__=_C
_Dot1sStpTxHoldCount_Object=MibScalar
dot1sStpTxHoldCount=_Dot1sStpTxHoldCount_Object((1,3,6,1,2,1,17,8,1,1,8),_Dot1sStpTxHoldCount_Type())
dot1sStpTxHoldCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpTxHoldCount.setStatus(_A)
class _Dot1sStpProtocolSpecification_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('decLb100',2),('ieee8021d',3),('ieee8021w',4),('ieee8021s',5)))
_Dot1sStpProtocolSpecification_Type.__name__=_C
_Dot1sStpProtocolSpecification_Object=MibScalar
dot1sStpProtocolSpecification=_Dot1sStpProtocolSpecification_Object((1,3,6,1,2,1,17,8,1,1,9),_Dot1sStpProtocolSpecification_Type())
dot1sStpProtocolSpecification.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpProtocolSpecification.setStatus(_A)
_Dot1sStpInstTable_Object=MibTable
dot1sStpInstTable=_Dot1sStpInstTable_Object((1,3,6,1,2,1,17,8,1,1,10))
if mibBuilder.loadTexts:dot1sStpInstTable.setStatus(_A)
_Dot1sStpInstEntry_Object=MibTableRow
dot1sStpInstEntry=_Dot1sStpInstEntry_Object((1,3,6,1,2,1,17,8,1,1,10,1))
dot1sStpInstEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:dot1sStpInstEntry.setStatus(_A)
class _Dot1sStpInstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Dot1sStpInstId_Type.__name__=_C
_Dot1sStpInstId_Object=MibTableColumn
dot1sStpInstId=_Dot1sStpInstId_Object((1,3,6,1,2,1,17,8,1,1,10,1,1),_Dot1sStpInstId_Type())
dot1sStpInstId.setMaxAccess(_J)
if mibBuilder.loadTexts:dot1sStpInstId.setStatus(_A)
class _Dot1sStpPriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_Dot1sStpPriority_Type.__name__=_C
_Dot1sStpPriority_Object=MibTableColumn
dot1sStpPriority=_Dot1sStpPriority_Object((1,3,6,1,2,1,17,8,1,1,10,1,2),_Dot1sStpPriority_Type())
dot1sStpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpPriority.setStatus(_A)
_Dot1sStpInstTimeSinceTopologyChange_Type=TimeTicks
_Dot1sStpInstTimeSinceTopologyChange_Object=MibTableColumn
dot1sStpInstTimeSinceTopologyChange=_Dot1sStpInstTimeSinceTopologyChange_Object((1,3,6,1,2,1,17,8,1,1,10,1,3),_Dot1sStpInstTimeSinceTopologyChange_Type())
dot1sStpInstTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpInstTimeSinceTopologyChange.setStatus(_A)
_Dot1sStpInstTopChanges_Type=Counter32
_Dot1sStpInstTopChanges_Object=MibTableColumn
dot1sStpInstTopChanges=_Dot1sStpInstTopChanges_Object((1,3,6,1,2,1,17,8,1,1,10,1,4),_Dot1sStpInstTopChanges_Type())
dot1sStpInstTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpInstTopChanges.setStatus(_A)
_Dot1sStpInstDesignatedRoot_Type=BridgeId
_Dot1sStpInstDesignatedRoot_Object=MibTableColumn
dot1sStpInstDesignatedRoot=_Dot1sStpInstDesignatedRoot_Object((1,3,6,1,2,1,17,8,1,1,10,1,5),_Dot1sStpInstDesignatedRoot_Type())
dot1sStpInstDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpInstDesignatedRoot.setStatus(_A)
_Dot1sStpInstRootCost_Type=Integer32
_Dot1sStpInstRootCost_Object=MibTableColumn
dot1sStpInstRootCost=_Dot1sStpInstRootCost_Object((1,3,6,1,2,1,17,8,1,1,10,1,6),_Dot1sStpInstRootCost_Type())
dot1sStpInstRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpInstRootCost.setStatus(_A)
_Dot1sStpInstRootPort_Type=Integer32
_Dot1sStpInstRootPort_Object=MibTableColumn
dot1sStpInstRootPort=_Dot1sStpInstRootPort_Object((1,3,6,1,2,1,17,8,1,1,10,1,7),_Dot1sStpInstRootPort_Type())
dot1sStpInstRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpInstRootPort.setStatus(_A)
_Dot1sStpInstMaxAge_Type=Timeout
_Dot1sStpInstMaxAge_Object=MibTableColumn
dot1sStpInstMaxAge=_Dot1sStpInstMaxAge_Object((1,3,6,1,2,1,17,8,1,1,10,1,8),_Dot1sStpInstMaxAge_Type())
dot1sStpInstMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpInstMaxAge.setStatus(_A)
_Dot1sStpInstHelloTime_Type=Timeout
_Dot1sStpInstHelloTime_Object=MibTableColumn
dot1sStpInstHelloTime=_Dot1sStpInstHelloTime_Object((1,3,6,1,2,1,17,8,1,1,10,1,9),_Dot1sStpInstHelloTime_Type())
dot1sStpInstHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpInstHelloTime.setStatus(_A)
_Dot1sStpInstForwardDelay_Type=Timeout
_Dot1sStpInstForwardDelay_Object=MibTableColumn
dot1sStpInstForwardDelay=_Dot1sStpInstForwardDelay_Object((1,3,6,1,2,1,17,8,1,1,10,1,10),_Dot1sStpInstForwardDelay_Type())
dot1sStpInstForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpInstForwardDelay.setStatus(_A)
class _Dot1sStpInstAdminEnable_Type(TruthValue):defaultValue=2
_Dot1sStpInstAdminEnable_Type.__name__=_G
_Dot1sStpInstAdminEnable_Object=MibTableColumn
dot1sStpInstAdminEnable=_Dot1sStpInstAdminEnable_Object((1,3,6,1,2,1,17,8,1,1,10,1,11),_Dot1sStpInstAdminEnable_Type())
dot1sStpInstAdminEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpInstAdminEnable.setStatus(_A)
class _Dot1sStpInstOperEnable_Type(TruthValue):defaultValue=2
_Dot1sStpInstOperEnable_Type.__name__=_G
_Dot1sStpInstOperEnable_Object=MibTableColumn
dot1sStpInstOperEnable=_Dot1sStpInstOperEnable_Object((1,3,6,1,2,1,17,8,1,1,10,1,12),_Dot1sStpInstOperEnable_Type())
dot1sStpInstOperEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpInstOperEnable.setStatus(_A)
_Dot1sStpPortTable_Object=MibTable
dot1sStpPortTable=_Dot1sStpPortTable_Object((1,3,6,1,2,1,17,8,1,1,11))
if mibBuilder.loadTexts:dot1sStpPortTable.setStatus(_A)
_Dot1sStpPortEntry_Object=MibTableRow
dot1sStpPortEntry=_Dot1sStpPortEntry_Object((1,3,6,1,2,1,17,8,1,1,11,1))
dot1sStpPortEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:dot1sStpPortEntry.setStatus(_A)
class _Dot1sStpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1sStpPort_Type.__name__=_C
_Dot1sStpPort_Object=MibTableColumn
dot1sStpPort=_Dot1sStpPort_Object((1,3,6,1,2,1,17,8,1,1,11,1,1),_Dot1sStpPort_Type())
dot1sStpPort.setMaxAccess(_J)
if mibBuilder.loadTexts:dot1sStpPort.setStatus(_A)
_Dot1sStpPortAdminEdgePort_Type=TruthValue
_Dot1sStpPortAdminEdgePort_Object=MibTableColumn
dot1sStpPortAdminEdgePort=_Dot1sStpPortAdminEdgePort_Object((1,3,6,1,2,1,17,8,1,1,11,1,2),_Dot1sStpPortAdminEdgePort_Type())
dot1sStpPortAdminEdgePort.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpPortAdminEdgePort.setStatus(_A)
class _Dot1sStpPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forceTrue',1),('forceFalse',2),('auto',3)))
_Dot1sStpPortAdminPointToPoint_Type.__name__=_C
_Dot1sStpPortAdminPointToPoint_Object=MibTableColumn
dot1sStpPortAdminPointToPoint=_Dot1sStpPortAdminPointToPoint_Object((1,3,6,1,2,1,17,8,1,1,11,1,3),_Dot1sStpPortAdminPointToPoint_Type())
dot1sStpPortAdminPointToPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpPortAdminPointToPoint.setStatus(_A)
_Dot1sStpPortOperEdgePort_Type=TruthValue
_Dot1sStpPortOperEdgePort_Object=MibTableColumn
dot1sStpPortOperEdgePort=_Dot1sStpPortOperEdgePort_Object((1,3,6,1,2,1,17,8,1,1,11,1,4),_Dot1sStpPortOperEdgePort_Type())
dot1sStpPortOperEdgePort.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpPortOperEdgePort.setStatus(_A)
_Dot1sStpPortOperPointToPoint_Type=TruthValue
_Dot1sStpPortOperPointToPoint_Object=MibTableColumn
dot1sStpPortOperPointToPoint=_Dot1sStpPortOperPointToPoint_Object((1,3,6,1,2,1,17,8,1,1,11,1,5),_Dot1sStpPortOperPointToPoint_Type())
dot1sStpPortOperPointToPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpPortOperPointToPoint.setStatus(_A)
class _Dot1sStpPortExterPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_Dot1sStpPortExterPathCost_Type.__name__=_C
_Dot1sStpPortExterPathCost_Object=MibTableColumn
dot1sStpPortExterPathCost=_Dot1sStpPortExterPathCost_Object((1,3,6,1,2,1,17,8,1,1,11,1,6),_Dot1sStpPortExterPathCost_Type())
dot1sStpPortExterPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpPortExterPathCost.setStatus(_A)
class _Dot1sStpVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*(('stpCompatible',0),('rstp-mstp',2)))
_Dot1sStpVersion_Type.__name__=_C
_Dot1sStpVersion_Object=MibTableColumn
dot1sStpVersion=_Dot1sStpVersion_Object((1,3,6,1,2,1,17,8,1,1,11,1,7),_Dot1sStpVersion_Type())
dot1sStpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpVersion.setStatus(_A)
_Dot1sStpPortSnoopingEnable_Type=TruthValue
_Dot1sStpPortSnoopingEnable_Object=MibTableColumn
dot1sStpPortSnoopingEnable=_Dot1sStpPortSnoopingEnable_Object((1,3,6,1,2,1,17,8,1,1,11,1,8),_Dot1sStpPortSnoopingEnable_Type())
dot1sStpPortSnoopingEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpPortSnoopingEnable.setStatus(_A)
_Dot1sStpInstPortTable_Object=MibTable
dot1sStpInstPortTable=_Dot1sStpInstPortTable_Object((1,3,6,1,2,1,17,8,1,1,12))
if mibBuilder.loadTexts:dot1sStpInstPortTable.setStatus(_A)
_Dot1sStpInstPortEntry_Object=MibTableRow
dot1sStpInstPortEntry=_Dot1sStpInstPortEntry_Object((1,3,6,1,2,1,17,8,1,1,12,1))
dot1sStpInstPortEntry.setIndexNames((0,_E,_I),(0,_E,_H))
if mibBuilder.loadTexts:dot1sStpInstPortEntry.setStatus(_A)
class _Dot1sStpInstPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_Dot1sStpInstPortPriority_Type.__name__=_C
_Dot1sStpInstPortPriority_Object=MibTableColumn
dot1sStpInstPortPriority=_Dot1sStpInstPortPriority_Object((1,3,6,1,2,1,17,8,1,1,12,1,1),_Dot1sStpInstPortPriority_Type())
dot1sStpInstPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpInstPortPriority.setStatus(_A)
class _Dot1sStpInstPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disabled',1),('discarding',2),('learning',3),('forwarding',4)))
_Dot1sStpInstPortState_Type.__name__=_C
_Dot1sStpInstPortState_Object=MibTableColumn
dot1sStpInstPortState=_Dot1sStpInstPortState_Object((1,3,6,1,2,1,17,8,1,1,12,1,2),_Dot1sStpInstPortState_Type())
dot1sStpInstPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpInstPortState.setStatus(_A)
class _Dot1sStpInstPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_Dot1sStpInstPortPathCost_Type.__name__=_C
_Dot1sStpInstPortPathCost_Object=MibTableColumn
dot1sStpInstPortPathCost=_Dot1sStpInstPortPathCost_Object((1,3,6,1,2,1,17,8,1,1,12,1,3),_Dot1sStpInstPortPathCost_Type())
dot1sStpInstPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpInstPortPathCost.setStatus(_A)
_Dot1sStpInstPortDesignatedRoot_Type=BridgeId
_Dot1sStpInstPortDesignatedRoot_Object=MibTableColumn
dot1sStpInstPortDesignatedRoot=_Dot1sStpInstPortDesignatedRoot_Object((1,3,6,1,2,1,17,8,1,1,12,1,4),_Dot1sStpInstPortDesignatedRoot_Type())
dot1sStpInstPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpInstPortDesignatedRoot.setStatus(_A)
_Dot1sStpInstPortDesignatedCost_Type=Integer32
_Dot1sStpInstPortDesignatedCost_Object=MibTableColumn
dot1sStpInstPortDesignatedCost=_Dot1sStpInstPortDesignatedCost_Object((1,3,6,1,2,1,17,8,1,1,12,1,5),_Dot1sStpInstPortDesignatedCost_Type())
dot1sStpInstPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpInstPortDesignatedCost.setStatus(_A)
_Dot1sStpInstPortDesignatedBridge_Type=BridgeId
_Dot1sStpInstPortDesignatedBridge_Object=MibTableColumn
dot1sStpInstPortDesignatedBridge=_Dot1sStpInstPortDesignatedBridge_Object((1,3,6,1,2,1,17,8,1,1,12,1,6),_Dot1sStpInstPortDesignatedBridge_Type())
dot1sStpInstPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpInstPortDesignatedBridge.setStatus(_A)
class _Dot1sStpInstPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_Dot1sStpInstPortDesignatedPort_Type.__name__=_K
_Dot1sStpInstPortDesignatedPort_Object=MibTableColumn
dot1sStpInstPortDesignatedPort=_Dot1sStpInstPortDesignatedPort_Object((1,3,6,1,2,1,17,8,1,1,12,1,7),_Dot1sStpInstPortDesignatedPort_Type())
dot1sStpInstPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpInstPortDesignatedPort.setStatus(_A)
_Dot1sStpInstPortForwardTransitions_Type=Counter32
_Dot1sStpInstPortForwardTransitions_Object=MibTableColumn
dot1sStpInstPortForwardTransitions=_Dot1sStpInstPortForwardTransitions_Object((1,3,6,1,2,1,17,8,1,1,12,1,8),_Dot1sStpInstPortForwardTransitions_Type())
dot1sStpInstPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpInstPortForwardTransitions.setStatus(_A)
class _Dot1sStpInstPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('master',0),('alternate-backup',1),('root',2),('designated',3)))
_Dot1sStpInstPortRole_Type.__name__=_C
_Dot1sStpInstPortRole_Object=MibTableColumn
dot1sStpInstPortRole=_Dot1sStpInstPortRole_Object((1,3,6,1,2,1,17,8,1,1,12,1,9),_Dot1sStpInstPortRole_Type())
dot1sStpInstPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1sStpInstPortRole.setStatus(_A)
_Dot1sStpVlanTable_Object=MibTable
dot1sStpVlanTable=_Dot1sStpVlanTable_Object((1,3,6,1,2,1,17,8,1,1,13))
if mibBuilder.loadTexts:dot1sStpVlanTable.setStatus(_A)
_Dot1sStpVlanEntry_Object=MibTableRow
dot1sStpVlanEntry=_Dot1sStpVlanEntry_Object((1,3,6,1,2,1,17,8,1,1,13,1))
dot1sStpVlanEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:dot1sStpVlanEntry.setStatus(_A)
class _Dot1sStpVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Dot1sStpVlanIndex_Type.__name__=_C
_Dot1sStpVlanIndex_Object=MibTableColumn
dot1sStpVlanIndex=_Dot1sStpVlanIndex_Object((1,3,6,1,2,1,17,8,1,1,13,1,1),_Dot1sStpVlanIndex_Type())
dot1sStpVlanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:dot1sStpVlanIndex.setStatus(_A)
class _Dot1sStpVlanInstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Dot1sStpVlanInstId_Type.__name__=_C
_Dot1sStpVlanInstId_Object=MibTableColumn
dot1sStpVlanInstId=_Dot1sStpVlanInstId_Object((1,3,6,1,2,1,17,8,1,1,13,1,2),_Dot1sStpVlanInstId_Type())
dot1sStpVlanInstId.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1sStpVlanInstId.setStatus(_A)
_Dot1sStpTrapTable_ObjectIdentity=ObjectIdentity
dot1sStpTrapTable=_Dot1sStpTrapTable_ObjectIdentity((1,3,6,1,2,1,17,8,1,1,14))
_Dot1sStpTrapEntry_ObjectIdentity=ObjectIdentity
dot1sStpTrapEntry=_Dot1sStpTrapEntry_ObjectIdentity((1,3,6,1,2,1,17,8,1,1,14,1))
dot1sStpInstNewRoot=NotificationType((1,3,6,1,2,1,17,8,1,1,14,1,1))
dot1sStpInstNewRoot.setObjects((_E,_O))
if mibBuilder.loadTexts:dot1sStpInstNewRoot.setStatus(_A)
dot1sStpInstPortForwarding=NotificationType((1,3,6,1,2,1,17,8,1,1,14,1,2))
dot1sStpInstPortForwarding.setObjects((_E,_H))
if mibBuilder.loadTexts:dot1sStpInstPortForwarding.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'mstpMib':mstpMib,'mstpMIBObjects':mstpMIBObjects,'dot1sStp':dot1sStp,'dot1sStpName':dot1sStpName,'dot1sStpRevision':dot1sStpRevision,'dot1sStpEnable':dot1sStpEnable,'dot1sStpBridgeMaxAge':dot1sStpBridgeMaxAge,'dot1sStpBridgeHelloTime':dot1sStpBridgeHelloTime,'dot1sStpBridgeForwardDelay':dot1sStpBridgeForwardDelay,'dot1sStpBridgeMaxHops':dot1sStpBridgeMaxHops,'dot1sStpTxHoldCount':dot1sStpTxHoldCount,'dot1sStpProtocolSpecification':dot1sStpProtocolSpecification,'dot1sStpInstTable':dot1sStpInstTable,'dot1sStpInstEntry':dot1sStpInstEntry,_I:dot1sStpInstId,'dot1sStpPriority':dot1sStpPriority,'dot1sStpInstTimeSinceTopologyChange':dot1sStpInstTimeSinceTopologyChange,'dot1sStpInstTopChanges':dot1sStpInstTopChanges,_O:dot1sStpInstDesignatedRoot,'dot1sStpInstRootCost':dot1sStpInstRootCost,'dot1sStpInstRootPort':dot1sStpInstRootPort,'dot1sStpInstMaxAge':dot1sStpInstMaxAge,'dot1sStpInstHelloTime':dot1sStpInstHelloTime,'dot1sStpInstForwardDelay':dot1sStpInstForwardDelay,'dot1sStpInstAdminEnable':dot1sStpInstAdminEnable,'dot1sStpInstOperEnable':dot1sStpInstOperEnable,'dot1sStpPortTable':dot1sStpPortTable,'dot1sStpPortEntry':dot1sStpPortEntry,_H:dot1sStpPort,'dot1sStpPortAdminEdgePort':dot1sStpPortAdminEdgePort,'dot1sStpPortAdminPointToPoint':dot1sStpPortAdminPointToPoint,'dot1sStpPortOperEdgePort':dot1sStpPortOperEdgePort,'dot1sStpPortOperPointToPoint':dot1sStpPortOperPointToPoint,'dot1sStpPortExterPathCost':dot1sStpPortExterPathCost,'dot1sStpVersion':dot1sStpVersion,'dot1sStpPortSnoopingEnable':dot1sStpPortSnoopingEnable,'dot1sStpInstPortTable':dot1sStpInstPortTable,'dot1sStpInstPortEntry':dot1sStpInstPortEntry,'dot1sStpInstPortPriority':dot1sStpInstPortPriority,'dot1sStpInstPortState':dot1sStpInstPortState,'dot1sStpInstPortPathCost':dot1sStpInstPortPathCost,'dot1sStpInstPortDesignatedRoot':dot1sStpInstPortDesignatedRoot,'dot1sStpInstPortDesignatedCost':dot1sStpInstPortDesignatedCost,'dot1sStpInstPortDesignatedBridge':dot1sStpInstPortDesignatedBridge,'dot1sStpInstPortDesignatedPort':dot1sStpInstPortDesignatedPort,'dot1sStpInstPortForwardTransitions':dot1sStpInstPortForwardTransitions,'dot1sStpInstPortRole':dot1sStpInstPortRole,'dot1sStpVlanTable':dot1sStpVlanTable,'dot1sStpVlanEntry':dot1sStpVlanEntry,_N:dot1sStpVlanIndex,'dot1sStpVlanInstId':dot1sStpVlanInstId,'dot1sStpTrapTable':dot1sStpTrapTable,'dot1sStpTrapEntry':dot1sStpTrapEntry,'dot1sStpInstNewRoot':dot1sStpInstNewRoot,'dot1sStpInstPortForwarding':dot1sStpInstPortForwarding})