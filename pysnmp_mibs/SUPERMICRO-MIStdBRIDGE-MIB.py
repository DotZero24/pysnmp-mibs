_U='invalid'
_T='fsDot1dTpFdbAddress'
_S='disabled'
_R='fsDot1dStpPort'
_Q='fsDot1dStpContextId'
_P='fsDot1dBasePort'
_O='unknown'
_N='OctetString'
_M='fsDot1dStaticReceivePort'
_L='fsDot1dStaticAddress'
_K='frames'
_J='fsDot1dTpPort'
_I='Timeout'
_H='fsDot1dBaseContextId'
_G='centi-seconds'
_F='not-accessible'
_E='read-write'
_D='SUPERMICRO-MIStdBRIDGE-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsDot1dBridge=ModuleIdentity((1,3,6,1,4,1,10876,101,1,116))
if mibBuilder.loadTexts:fsDot1dBridge.setRevisions(('2012-09-05 00:00',))
class MacAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class BridgeId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class Timeout(TextualConvention,Integer32):status=_A;displayHint='d'
_FsDot1dNotifications_ObjectIdentity=ObjectIdentity
fsDot1dNotifications=_FsDot1dNotifications_ObjectIdentity((1,3,6,1,4,1,10876,101,1,116,0))
_FsDot1dBase_ObjectIdentity=ObjectIdentity
fsDot1dBase=_FsDot1dBase_ObjectIdentity((1,3,6,1,4,1,10876,101,1,116,1))
_FsDot1dBaseTable_Object=MibTable
fsDot1dBaseTable=_FsDot1dBaseTable_Object((1,3,6,1,4,1,10876,101,1,116,1,1))
if mibBuilder.loadTexts:fsDot1dBaseTable.setStatus(_A)
_FsDot1dBaseEntry_Object=MibTableRow
fsDot1dBaseEntry=_FsDot1dBaseEntry_Object((1,3,6,1,4,1,10876,101,1,116,1,1,1))
fsDot1dBaseEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:fsDot1dBaseEntry.setStatus(_A)
class _FsDot1dBaseContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsDot1dBaseContextId_Type.__name__=_C
_FsDot1dBaseContextId_Object=MibTableColumn
fsDot1dBaseContextId=_FsDot1dBaseContextId_Object((1,3,6,1,4,1,10876,101,1,116,1,1,1,1),_FsDot1dBaseContextId_Type())
fsDot1dBaseContextId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1dBaseContextId.setStatus(_A)
_FsDot1dBaseBridgeAddress_Type=MacAddress
_FsDot1dBaseBridgeAddress_Object=MibTableColumn
fsDot1dBaseBridgeAddress=_FsDot1dBaseBridgeAddress_Object((1,3,6,1,4,1,10876,101,1,116,1,1,1,2),_FsDot1dBaseBridgeAddress_Type())
fsDot1dBaseBridgeAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dBaseBridgeAddress.setStatus(_A)
_FsDot1dBaseNumPorts_Type=Integer32
_FsDot1dBaseNumPorts_Object=MibTableColumn
fsDot1dBaseNumPorts=_FsDot1dBaseNumPorts_Object((1,3,6,1,4,1,10876,101,1,116,1,1,1,3),_FsDot1dBaseNumPorts_Type())
fsDot1dBaseNumPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dBaseNumPorts.setStatus(_A)
if mibBuilder.loadTexts:fsDot1dBaseNumPorts.setUnits('ports')
class _FsDot1dBaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),('transparentonly',2),('sourcerouteonly',3),('srt',4)))
_FsDot1dBaseType_Type.__name__=_C
_FsDot1dBaseType_Object=MibTableColumn
fsDot1dBaseType=_FsDot1dBaseType_Object((1,3,6,1,4,1,10876,101,1,116,1,1,1,4),_FsDot1dBaseType_Type())
fsDot1dBaseType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dBaseType.setStatus(_A)
_FsDot1dBasePortTable_Object=MibTable
fsDot1dBasePortTable=_FsDot1dBasePortTable_Object((1,3,6,1,4,1,10876,101,1,116,1,2))
if mibBuilder.loadTexts:fsDot1dBasePortTable.setStatus(_A)
_FsDot1dBasePortEntry_Object=MibTableRow
fsDot1dBasePortEntry=_FsDot1dBasePortEntry_Object((1,3,6,1,4,1,10876,101,1,116,1,2,1))
fsDot1dBasePortEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:fsDot1dBasePortEntry.setStatus(_A)
class _FsDot1dBasePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsDot1dBasePort_Type.__name__=_C
_FsDot1dBasePort_Object=MibTableColumn
fsDot1dBasePort=_FsDot1dBasePort_Object((1,3,6,1,4,1,10876,101,1,116,1,2,1,1),_FsDot1dBasePort_Type())
fsDot1dBasePort.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1dBasePort.setStatus(_A)
_FsDot1dBasePortIfIndex_Type=InterfaceIndex
_FsDot1dBasePortIfIndex_Object=MibTableColumn
fsDot1dBasePortIfIndex=_FsDot1dBasePortIfIndex_Object((1,3,6,1,4,1,10876,101,1,116,1,2,1,2),_FsDot1dBasePortIfIndex_Type())
fsDot1dBasePortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dBasePortIfIndex.setStatus(_A)
_FsDot1dBasePortCircuit_Type=ObjectIdentifier
_FsDot1dBasePortCircuit_Object=MibTableColumn
fsDot1dBasePortCircuit=_FsDot1dBasePortCircuit_Object((1,3,6,1,4,1,10876,101,1,116,1,2,1,3),_FsDot1dBasePortCircuit_Type())
fsDot1dBasePortCircuit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dBasePortCircuit.setStatus(_A)
_FsDot1dBasePortDelayExceededDiscards_Type=Counter32
_FsDot1dBasePortDelayExceededDiscards_Object=MibTableColumn
fsDot1dBasePortDelayExceededDiscards=_FsDot1dBasePortDelayExceededDiscards_Object((1,3,6,1,4,1,10876,101,1,116,1,2,1,4),_FsDot1dBasePortDelayExceededDiscards_Type())
fsDot1dBasePortDelayExceededDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dBasePortDelayExceededDiscards.setStatus(_A)
_FsDot1dBasePortMtuExceededDiscards_Type=Counter32
_FsDot1dBasePortMtuExceededDiscards_Object=MibTableColumn
fsDot1dBasePortMtuExceededDiscards=_FsDot1dBasePortMtuExceededDiscards_Object((1,3,6,1,4,1,10876,101,1,116,1,2,1,5),_FsDot1dBasePortMtuExceededDiscards_Type())
fsDot1dBasePortMtuExceededDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dBasePortMtuExceededDiscards.setStatus(_A)
_FsDot1dStp_ObjectIdentity=ObjectIdentity
fsDot1dStp=_FsDot1dStp_ObjectIdentity((1,3,6,1,4,1,10876,101,1,116,2))
_FsDot1dStpTable_Object=MibTable
fsDot1dStpTable=_FsDot1dStpTable_Object((1,3,6,1,4,1,10876,101,1,116,2,1))
if mibBuilder.loadTexts:fsDot1dStpTable.setStatus(_A)
_FsDot1dStpEntry_Object=MibTableRow
fsDot1dStpEntry=_FsDot1dStpEntry_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1))
fsDot1dStpEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:fsDot1dStpEntry.setStatus(_A)
class _FsDot1dStpContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsDot1dStpContextId_Type.__name__=_C
_FsDot1dStpContextId_Object=MibTableColumn
fsDot1dStpContextId=_FsDot1dStpContextId_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1,1),_FsDot1dStpContextId_Type())
fsDot1dStpContextId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1dStpContextId.setStatus(_A)
class _FsDot1dStpProtocolSpecification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('decLb100',2),('ieee8021d',3)))
_FsDot1dStpProtocolSpecification_Type.__name__=_C
_FsDot1dStpProtocolSpecification_Object=MibTableColumn
fsDot1dStpProtocolSpecification=_FsDot1dStpProtocolSpecification_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1,2),_FsDot1dStpProtocolSpecification_Type())
fsDot1dStpProtocolSpecification.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpProtocolSpecification.setStatus(_A)
class _FsDot1dStpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsDot1dStpPriority_Type.__name__=_C
_FsDot1dStpPriority_Object=MibTableColumn
fsDot1dStpPriority=_FsDot1dStpPriority_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1,3),_FsDot1dStpPriority_Type())
fsDot1dStpPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot1dStpPriority.setStatus(_A)
_FsDot1dStpTimeSinceTopologyChange_Type=TimeTicks
_FsDot1dStpTimeSinceTopologyChange_Object=MibTableColumn
fsDot1dStpTimeSinceTopologyChange=_FsDot1dStpTimeSinceTopologyChange_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1,4),_FsDot1dStpTimeSinceTopologyChange_Type())
fsDot1dStpTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpTimeSinceTopologyChange.setStatus(_A)
if mibBuilder.loadTexts:fsDot1dStpTimeSinceTopologyChange.setUnits(_G)
_FsDot1dStpTopChanges_Type=Counter32
_FsDot1dStpTopChanges_Object=MibTableColumn
fsDot1dStpTopChanges=_FsDot1dStpTopChanges_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1,5),_FsDot1dStpTopChanges_Type())
fsDot1dStpTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpTopChanges.setStatus(_A)
_FsDot1dStpDesignatedRoot_Type=BridgeId
_FsDot1dStpDesignatedRoot_Object=MibTableColumn
fsDot1dStpDesignatedRoot=_FsDot1dStpDesignatedRoot_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1,6),_FsDot1dStpDesignatedRoot_Type())
fsDot1dStpDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpDesignatedRoot.setStatus(_A)
_FsDot1dStpRootCost_Type=Integer32
_FsDot1dStpRootCost_Object=MibTableColumn
fsDot1dStpRootCost=_FsDot1dStpRootCost_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1,7),_FsDot1dStpRootCost_Type())
fsDot1dStpRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpRootCost.setStatus(_A)
_FsDot1dStpRootPort_Type=Integer32
_FsDot1dStpRootPort_Object=MibTableColumn
fsDot1dStpRootPort=_FsDot1dStpRootPort_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1,8),_FsDot1dStpRootPort_Type())
fsDot1dStpRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpRootPort.setStatus(_A)
_FsDot1dStpMaxAge_Type=Timeout
_FsDot1dStpMaxAge_Object=MibTableColumn
fsDot1dStpMaxAge=_FsDot1dStpMaxAge_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1,9),_FsDot1dStpMaxAge_Type())
fsDot1dStpMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpMaxAge.setStatus(_A)
if mibBuilder.loadTexts:fsDot1dStpMaxAge.setUnits(_G)
_FsDot1dStpHelloTime_Type=Timeout
_FsDot1dStpHelloTime_Object=MibTableColumn
fsDot1dStpHelloTime=_FsDot1dStpHelloTime_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1,10),_FsDot1dStpHelloTime_Type())
fsDot1dStpHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpHelloTime.setStatus(_A)
if mibBuilder.loadTexts:fsDot1dStpHelloTime.setUnits(_G)
_FsDot1dStpHoldTime_Type=Integer32
_FsDot1dStpHoldTime_Object=MibTableColumn
fsDot1dStpHoldTime=_FsDot1dStpHoldTime_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1,11),_FsDot1dStpHoldTime_Type())
fsDot1dStpHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpHoldTime.setStatus(_A)
if mibBuilder.loadTexts:fsDot1dStpHoldTime.setUnits(_G)
_FsDot1dStpForwardDelay_Type=Timeout
_FsDot1dStpForwardDelay_Object=MibTableColumn
fsDot1dStpForwardDelay=_FsDot1dStpForwardDelay_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1,12),_FsDot1dStpForwardDelay_Type())
fsDot1dStpForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:fsDot1dStpForwardDelay.setUnits(_G)
class _FsDot1dStpBridgeMaxAge_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_FsDot1dStpBridgeMaxAge_Type.__name__=_I
_FsDot1dStpBridgeMaxAge_Object=MibTableColumn
fsDot1dStpBridgeMaxAge=_FsDot1dStpBridgeMaxAge_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1,13),_FsDot1dStpBridgeMaxAge_Type())
fsDot1dStpBridgeMaxAge.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot1dStpBridgeMaxAge.setStatus(_A)
if mibBuilder.loadTexts:fsDot1dStpBridgeMaxAge.setUnits(_G)
class _FsDot1dStpBridgeHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,100),ValueRangeConstraint(200,200))
_FsDot1dStpBridgeHelloTime_Type.__name__=_I
_FsDot1dStpBridgeHelloTime_Object=MibTableColumn
fsDot1dStpBridgeHelloTime=_FsDot1dStpBridgeHelloTime_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1,14),_FsDot1dStpBridgeHelloTime_Type())
fsDot1dStpBridgeHelloTime.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot1dStpBridgeHelloTime.setStatus(_A)
if mibBuilder.loadTexts:fsDot1dStpBridgeHelloTime.setUnits(_G)
class _FsDot1dStpBridgeForwardDelay_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_FsDot1dStpBridgeForwardDelay_Type.__name__=_I
_FsDot1dStpBridgeForwardDelay_Object=MibTableColumn
fsDot1dStpBridgeForwardDelay=_FsDot1dStpBridgeForwardDelay_Object((1,3,6,1,4,1,10876,101,1,116,2,1,1,15),_FsDot1dStpBridgeForwardDelay_Type())
fsDot1dStpBridgeForwardDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot1dStpBridgeForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:fsDot1dStpBridgeForwardDelay.setUnits(_G)
_FsDot1dStpPortTable_Object=MibTable
fsDot1dStpPortTable=_FsDot1dStpPortTable_Object((1,3,6,1,4,1,10876,101,1,116,2,2))
if mibBuilder.loadTexts:fsDot1dStpPortTable.setStatus(_A)
_FsDot1dStpPortEntry_Object=MibTableRow
fsDot1dStpPortEntry=_FsDot1dStpPortEntry_Object((1,3,6,1,4,1,10876,101,1,116,2,2,1))
fsDot1dStpPortEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:fsDot1dStpPortEntry.setStatus(_A)
class _FsDot1dStpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsDot1dStpPort_Type.__name__=_C
_FsDot1dStpPort_Object=MibTableColumn
fsDot1dStpPort=_FsDot1dStpPort_Object((1,3,6,1,4,1,10876,101,1,116,2,2,1,1),_FsDot1dStpPort_Type())
fsDot1dStpPort.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1dStpPort.setStatus(_A)
class _FsDot1dStpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsDot1dStpPortPriority_Type.__name__=_C
_FsDot1dStpPortPriority_Object=MibTableColumn
fsDot1dStpPortPriority=_FsDot1dStpPortPriority_Object((1,3,6,1,4,1,10876,101,1,116,2,2,1,2),_FsDot1dStpPortPriority_Type())
fsDot1dStpPortPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot1dStpPortPriority.setStatus(_A)
class _FsDot1dStpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_S,1),('blocking',2),('listening',3),('learning',4),('forwarding',5),('broken',6)))
_FsDot1dStpPortState_Type.__name__=_C
_FsDot1dStpPortState_Object=MibTableColumn
fsDot1dStpPortState=_FsDot1dStpPortState_Object((1,3,6,1,4,1,10876,101,1,116,2,2,1,3),_FsDot1dStpPortState_Type())
fsDot1dStpPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpPortState.setStatus(_A)
class _FsDot1dStpPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_S,2)))
_FsDot1dStpPortEnable_Type.__name__=_C
_FsDot1dStpPortEnable_Object=MibTableColumn
fsDot1dStpPortEnable=_FsDot1dStpPortEnable_Object((1,3,6,1,4,1,10876,101,1,116,2,2,1,4),_FsDot1dStpPortEnable_Type())
fsDot1dStpPortEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot1dStpPortEnable.setStatus(_A)
class _FsDot1dStpPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsDot1dStpPortPathCost_Type.__name__=_C
_FsDot1dStpPortPathCost_Object=MibTableColumn
fsDot1dStpPortPathCost=_FsDot1dStpPortPathCost_Object((1,3,6,1,4,1,10876,101,1,116,2,2,1,5),_FsDot1dStpPortPathCost_Type())
fsDot1dStpPortPathCost.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot1dStpPortPathCost.setStatus(_A)
_FsDot1dStpPortDesignatedRoot_Type=BridgeId
_FsDot1dStpPortDesignatedRoot_Object=MibTableColumn
fsDot1dStpPortDesignatedRoot=_FsDot1dStpPortDesignatedRoot_Object((1,3,6,1,4,1,10876,101,1,116,2,2,1,6),_FsDot1dStpPortDesignatedRoot_Type())
fsDot1dStpPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpPortDesignatedRoot.setStatus(_A)
_FsDot1dStpPortDesignatedCost_Type=Integer32
_FsDot1dStpPortDesignatedCost_Object=MibTableColumn
fsDot1dStpPortDesignatedCost=_FsDot1dStpPortDesignatedCost_Object((1,3,6,1,4,1,10876,101,1,116,2,2,1,7),_FsDot1dStpPortDesignatedCost_Type())
fsDot1dStpPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpPortDesignatedCost.setStatus(_A)
_FsDot1dStpPortDesignatedBridge_Type=BridgeId
_FsDot1dStpPortDesignatedBridge_Object=MibTableColumn
fsDot1dStpPortDesignatedBridge=_FsDot1dStpPortDesignatedBridge_Object((1,3,6,1,4,1,10876,101,1,116,2,2,1,8),_FsDot1dStpPortDesignatedBridge_Type())
fsDot1dStpPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpPortDesignatedBridge.setStatus(_A)
class _FsDot1dStpPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_FsDot1dStpPortDesignatedPort_Type.__name__=_N
_FsDot1dStpPortDesignatedPort_Object=MibTableColumn
fsDot1dStpPortDesignatedPort=_FsDot1dStpPortDesignatedPort_Object((1,3,6,1,4,1,10876,101,1,116,2,2,1,9),_FsDot1dStpPortDesignatedPort_Type())
fsDot1dStpPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpPortDesignatedPort.setStatus(_A)
_FsDot1dStpPortForwardTransitions_Type=Counter32
_FsDot1dStpPortForwardTransitions_Object=MibTableColumn
fsDot1dStpPortForwardTransitions=_FsDot1dStpPortForwardTransitions_Object((1,3,6,1,4,1,10876,101,1,116,2,2,1,10),_FsDot1dStpPortForwardTransitions_Type())
fsDot1dStpPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dStpPortForwardTransitions.setStatus(_A)
class _FsDot1dStpPortPathCost32_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_FsDot1dStpPortPathCost32_Type.__name__=_C
_FsDot1dStpPortPathCost32_Object=MibTableColumn
fsDot1dStpPortPathCost32=_FsDot1dStpPortPathCost32_Object((1,3,6,1,4,1,10876,101,1,116,2,2,1,11),_FsDot1dStpPortPathCost32_Type())
fsDot1dStpPortPathCost32.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot1dStpPortPathCost32.setStatus(_A)
_FsDot1dSr_ObjectIdentity=ObjectIdentity
fsDot1dSr=_FsDot1dSr_ObjectIdentity((1,3,6,1,4,1,10876,101,1,116,3))
_FsDot1dTp_ObjectIdentity=ObjectIdentity
fsDot1dTp=_FsDot1dTp_ObjectIdentity((1,3,6,1,4,1,10876,101,1,116,4))
_FsDot1dTpTable_Object=MibTable
fsDot1dTpTable=_FsDot1dTpTable_Object((1,3,6,1,4,1,10876,101,1,116,4,1))
if mibBuilder.loadTexts:fsDot1dTpTable.setStatus(_A)
_FsDot1dTpEntry_Object=MibTableRow
fsDot1dTpEntry=_FsDot1dTpEntry_Object((1,3,6,1,4,1,10876,101,1,116,4,1,1))
fsDot1dTpEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:fsDot1dTpEntry.setStatus(_A)
_FsDot1dTpLearnedEntryDiscards_Type=Counter32
_FsDot1dTpLearnedEntryDiscards_Object=MibTableColumn
fsDot1dTpLearnedEntryDiscards=_FsDot1dTpLearnedEntryDiscards_Object((1,3,6,1,4,1,10876,101,1,116,4,1,1,1),_FsDot1dTpLearnedEntryDiscards_Type())
fsDot1dTpLearnedEntryDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dTpLearnedEntryDiscards.setStatus(_A)
class _FsDot1dTpAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_FsDot1dTpAgingTime_Type.__name__=_C
_FsDot1dTpAgingTime_Object=MibTableColumn
fsDot1dTpAgingTime=_FsDot1dTpAgingTime_Object((1,3,6,1,4,1,10876,101,1,116,4,1,1,2),_FsDot1dTpAgingTime_Type())
fsDot1dTpAgingTime.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot1dTpAgingTime.setStatus(_A)
if mibBuilder.loadTexts:fsDot1dTpAgingTime.setUnits('seconds')
_FsDot1dTpFdbTable_Object=MibTable
fsDot1dTpFdbTable=_FsDot1dTpFdbTable_Object((1,3,6,1,4,1,10876,101,1,116,4,2))
if mibBuilder.loadTexts:fsDot1dTpFdbTable.setStatus(_A)
_FsDot1dTpFdbEntry_Object=MibTableRow
fsDot1dTpFdbEntry=_FsDot1dTpFdbEntry_Object((1,3,6,1,4,1,10876,101,1,116,4,2,1))
fsDot1dTpFdbEntry.setIndexNames((0,_D,_H),(0,_D,_T))
if mibBuilder.loadTexts:fsDot1dTpFdbEntry.setStatus(_A)
_FsDot1dTpFdbAddress_Type=MacAddress
_FsDot1dTpFdbAddress_Object=MibTableColumn
fsDot1dTpFdbAddress=_FsDot1dTpFdbAddress_Object((1,3,6,1,4,1,10876,101,1,116,4,2,1,1),_FsDot1dTpFdbAddress_Type())
fsDot1dTpFdbAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1dTpFdbAddress.setStatus(_A)
_FsDot1dTpFdbPort_Type=Integer32
_FsDot1dTpFdbPort_Object=MibTableColumn
fsDot1dTpFdbPort=_FsDot1dTpFdbPort_Object((1,3,6,1,4,1,10876,101,1,116,4,2,1,2),_FsDot1dTpFdbPort_Type())
fsDot1dTpFdbPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dTpFdbPort.setStatus(_A)
class _FsDot1dTpFdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),(_U,2),('learned',3),('self',4),('mgmt',5)))
_FsDot1dTpFdbStatus_Type.__name__=_C
_FsDot1dTpFdbStatus_Object=MibTableColumn
fsDot1dTpFdbStatus=_FsDot1dTpFdbStatus_Object((1,3,6,1,4,1,10876,101,1,116,4,2,1,3),_FsDot1dTpFdbStatus_Type())
fsDot1dTpFdbStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dTpFdbStatus.setStatus(_A)
_FsDot1dTpPortTable_Object=MibTable
fsDot1dTpPortTable=_FsDot1dTpPortTable_Object((1,3,6,1,4,1,10876,101,1,116,4,3))
if mibBuilder.loadTexts:fsDot1dTpPortTable.setStatus(_A)
_FsDot1dTpPortEntry_Object=MibTableRow
fsDot1dTpPortEntry=_FsDot1dTpPortEntry_Object((1,3,6,1,4,1,10876,101,1,116,4,3,1))
fsDot1dTpPortEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:fsDot1dTpPortEntry.setStatus(_A)
class _FsDot1dTpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsDot1dTpPort_Type.__name__=_C
_FsDot1dTpPort_Object=MibTableColumn
fsDot1dTpPort=_FsDot1dTpPort_Object((1,3,6,1,4,1,10876,101,1,116,4,3,1,1),_FsDot1dTpPort_Type())
fsDot1dTpPort.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1dTpPort.setStatus(_A)
_FsDot1dTpPortMaxInfo_Type=Integer32
_FsDot1dTpPortMaxInfo_Object=MibTableColumn
fsDot1dTpPortMaxInfo=_FsDot1dTpPortMaxInfo_Object((1,3,6,1,4,1,10876,101,1,116,4,3,1,2),_FsDot1dTpPortMaxInfo_Type())
fsDot1dTpPortMaxInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dTpPortMaxInfo.setStatus(_A)
if mibBuilder.loadTexts:fsDot1dTpPortMaxInfo.setUnits('bytes')
_FsDot1dTpPortInFrames_Type=Counter32
_FsDot1dTpPortInFrames_Object=MibTableColumn
fsDot1dTpPortInFrames=_FsDot1dTpPortInFrames_Object((1,3,6,1,4,1,10876,101,1,116,4,3,1,3),_FsDot1dTpPortInFrames_Type())
fsDot1dTpPortInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dTpPortInFrames.setStatus(_A)
if mibBuilder.loadTexts:fsDot1dTpPortInFrames.setUnits(_K)
_FsDot1dTpPortOutFrames_Type=Counter32
_FsDot1dTpPortOutFrames_Object=MibTableColumn
fsDot1dTpPortOutFrames=_FsDot1dTpPortOutFrames_Object((1,3,6,1,4,1,10876,101,1,116,4,3,1,4),_FsDot1dTpPortOutFrames_Type())
fsDot1dTpPortOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dTpPortOutFrames.setStatus(_A)
if mibBuilder.loadTexts:fsDot1dTpPortOutFrames.setUnits(_K)
_FsDot1dTpPortInDiscards_Type=Counter32
_FsDot1dTpPortInDiscards_Object=MibTableColumn
fsDot1dTpPortInDiscards=_FsDot1dTpPortInDiscards_Object((1,3,6,1,4,1,10876,101,1,116,4,3,1,5),_FsDot1dTpPortInDiscards_Type())
fsDot1dTpPortInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDot1dTpPortInDiscards.setStatus(_A)
if mibBuilder.loadTexts:fsDot1dTpPortInDiscards.setUnits(_K)
_FsDot1dStatic_ObjectIdentity=ObjectIdentity
fsDot1dStatic=_FsDot1dStatic_ObjectIdentity((1,3,6,1,4,1,10876,101,1,116,5))
_FsDot1dStaticTable_Object=MibTable
fsDot1dStaticTable=_FsDot1dStaticTable_Object((1,3,6,1,4,1,10876,101,1,116,5,1))
if mibBuilder.loadTexts:fsDot1dStaticTable.setStatus(_A)
_FsDot1dStaticEntry_Object=MibTableRow
fsDot1dStaticEntry=_FsDot1dStaticEntry_Object((1,3,6,1,4,1,10876,101,1,116,5,1,1))
fsDot1dStaticEntry.setIndexNames((0,_D,_H),(0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:fsDot1dStaticEntry.setStatus(_A)
_FsDot1dStaticAddress_Type=MacAddress
_FsDot1dStaticAddress_Object=MibTableColumn
fsDot1dStaticAddress=_FsDot1dStaticAddress_Object((1,3,6,1,4,1,10876,101,1,116,5,1,1,1),_FsDot1dStaticAddress_Type())
fsDot1dStaticAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1dStaticAddress.setStatus(_A)
class _FsDot1dStaticReceivePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsDot1dStaticReceivePort_Type.__name__=_C
_FsDot1dStaticReceivePort_Object=MibTableColumn
fsDot1dStaticReceivePort=_FsDot1dStaticReceivePort_Object((1,3,6,1,4,1,10876,101,1,116,5,1,1,2),_FsDot1dStaticReceivePort_Type())
fsDot1dStaticReceivePort.setMaxAccess(_F)
if mibBuilder.loadTexts:fsDot1dStaticReceivePort.setStatus(_A)
_FsDot1dStaticRowStatus_Type=RowStatus
_FsDot1dStaticRowStatus_Object=MibTableColumn
fsDot1dStaticRowStatus=_FsDot1dStaticRowStatus_Object((1,3,6,1,4,1,10876,101,1,116,5,1,1,3),_FsDot1dStaticRowStatus_Type())
fsDot1dStaticRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsDot1dStaticRowStatus.setStatus(_A)
class _FsDot1dStaticStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),(_U,2),('permanent',3),('deleteOnReset',4),('deleteOnTimeout',5)))
_FsDot1dStaticStatus_Type.__name__=_C
_FsDot1dStaticStatus_Object=MibTableColumn
fsDot1dStaticStatus=_FsDot1dStaticStatus_Object((1,3,6,1,4,1,10876,101,1,116,5,1,1,4),_FsDot1dStaticStatus_Type())
fsDot1dStaticStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot1dStaticStatus.setStatus(_A)
_FsDot1dStaticAllowedToGoTable_Object=MibTable
fsDot1dStaticAllowedToGoTable=_FsDot1dStaticAllowedToGoTable_Object((1,3,6,1,4,1,10876,101,1,116,5,2))
if mibBuilder.loadTexts:fsDot1dStaticAllowedToGoTable.setStatus(_A)
_FsDot1dStaticAllowedToGoEntry_Object=MibTableRow
fsDot1dStaticAllowedToGoEntry=_FsDot1dStaticAllowedToGoEntry_Object((1,3,6,1,4,1,10876,101,1,116,5,2,1))
fsDot1dStaticAllowedToGoEntry.setIndexNames((0,_D,_H),(0,_D,_L),(0,_D,_M),(0,_D,_J))
if mibBuilder.loadTexts:fsDot1dStaticAllowedToGoEntry.setStatus(_A)
_FsDot1dStaticAllowedIsMember_Type=TruthValue
_FsDot1dStaticAllowedIsMember_Object=MibTableColumn
fsDot1dStaticAllowedIsMember=_FsDot1dStaticAllowedIsMember_Object((1,3,6,1,4,1,10876,101,1,116,5,2,1,1),_FsDot1dStaticAllowedIsMember_Type())
fsDot1dStaticAllowedIsMember.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot1dStaticAllowedIsMember.setStatus(_A)
newRoot=NotificationType((1,3,6,1,4,1,10876,101,1,116,0,1))
if mibBuilder.loadTexts:newRoot.setStatus(_A)
topologyChange=NotificationType((1,3,6,1,4,1,10876,101,1,116,0,2))
if mibBuilder.loadTexts:topologyChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'MacAddress':MacAddress,'BridgeId':BridgeId,_I:Timeout,'fsDot1dBridge':fsDot1dBridge,'fsDot1dNotifications':fsDot1dNotifications,'newRoot':newRoot,'topologyChange':topologyChange,'fsDot1dBase':fsDot1dBase,'fsDot1dBaseTable':fsDot1dBaseTable,'fsDot1dBaseEntry':fsDot1dBaseEntry,_H:fsDot1dBaseContextId,'fsDot1dBaseBridgeAddress':fsDot1dBaseBridgeAddress,'fsDot1dBaseNumPorts':fsDot1dBaseNumPorts,'fsDot1dBaseType':fsDot1dBaseType,'fsDot1dBasePortTable':fsDot1dBasePortTable,'fsDot1dBasePortEntry':fsDot1dBasePortEntry,_P:fsDot1dBasePort,'fsDot1dBasePortIfIndex':fsDot1dBasePortIfIndex,'fsDot1dBasePortCircuit':fsDot1dBasePortCircuit,'fsDot1dBasePortDelayExceededDiscards':fsDot1dBasePortDelayExceededDiscards,'fsDot1dBasePortMtuExceededDiscards':fsDot1dBasePortMtuExceededDiscards,'fsDot1dStp':fsDot1dStp,'fsDot1dStpTable':fsDot1dStpTable,'fsDot1dStpEntry':fsDot1dStpEntry,_Q:fsDot1dStpContextId,'fsDot1dStpProtocolSpecification':fsDot1dStpProtocolSpecification,'fsDot1dStpPriority':fsDot1dStpPriority,'fsDot1dStpTimeSinceTopologyChange':fsDot1dStpTimeSinceTopologyChange,'fsDot1dStpTopChanges':fsDot1dStpTopChanges,'fsDot1dStpDesignatedRoot':fsDot1dStpDesignatedRoot,'fsDot1dStpRootCost':fsDot1dStpRootCost,'fsDot1dStpRootPort':fsDot1dStpRootPort,'fsDot1dStpMaxAge':fsDot1dStpMaxAge,'fsDot1dStpHelloTime':fsDot1dStpHelloTime,'fsDot1dStpHoldTime':fsDot1dStpHoldTime,'fsDot1dStpForwardDelay':fsDot1dStpForwardDelay,'fsDot1dStpBridgeMaxAge':fsDot1dStpBridgeMaxAge,'fsDot1dStpBridgeHelloTime':fsDot1dStpBridgeHelloTime,'fsDot1dStpBridgeForwardDelay':fsDot1dStpBridgeForwardDelay,'fsDot1dStpPortTable':fsDot1dStpPortTable,'fsDot1dStpPortEntry':fsDot1dStpPortEntry,_R:fsDot1dStpPort,'fsDot1dStpPortPriority':fsDot1dStpPortPriority,'fsDot1dStpPortState':fsDot1dStpPortState,'fsDot1dStpPortEnable':fsDot1dStpPortEnable,'fsDot1dStpPortPathCost':fsDot1dStpPortPathCost,'fsDot1dStpPortDesignatedRoot':fsDot1dStpPortDesignatedRoot,'fsDot1dStpPortDesignatedCost':fsDot1dStpPortDesignatedCost,'fsDot1dStpPortDesignatedBridge':fsDot1dStpPortDesignatedBridge,'fsDot1dStpPortDesignatedPort':fsDot1dStpPortDesignatedPort,'fsDot1dStpPortForwardTransitions':fsDot1dStpPortForwardTransitions,'fsDot1dStpPortPathCost32':fsDot1dStpPortPathCost32,'fsDot1dSr':fsDot1dSr,'fsDot1dTp':fsDot1dTp,'fsDot1dTpTable':fsDot1dTpTable,'fsDot1dTpEntry':fsDot1dTpEntry,'fsDot1dTpLearnedEntryDiscards':fsDot1dTpLearnedEntryDiscards,'fsDot1dTpAgingTime':fsDot1dTpAgingTime,'fsDot1dTpFdbTable':fsDot1dTpFdbTable,'fsDot1dTpFdbEntry':fsDot1dTpFdbEntry,_T:fsDot1dTpFdbAddress,'fsDot1dTpFdbPort':fsDot1dTpFdbPort,'fsDot1dTpFdbStatus':fsDot1dTpFdbStatus,'fsDot1dTpPortTable':fsDot1dTpPortTable,'fsDot1dTpPortEntry':fsDot1dTpPortEntry,_J:fsDot1dTpPort,'fsDot1dTpPortMaxInfo':fsDot1dTpPortMaxInfo,'fsDot1dTpPortInFrames':fsDot1dTpPortInFrames,'fsDot1dTpPortOutFrames':fsDot1dTpPortOutFrames,'fsDot1dTpPortInDiscards':fsDot1dTpPortInDiscards,'fsDot1dStatic':fsDot1dStatic,'fsDot1dStaticTable':fsDot1dStaticTable,'fsDot1dStaticEntry':fsDot1dStaticEntry,_L:fsDot1dStaticAddress,_M:fsDot1dStaticReceivePort,'fsDot1dStaticRowStatus':fsDot1dStaticRowStatus,'fsDot1dStaticStatus':fsDot1dStaticStatus,'fsDot1dStaticAllowedToGoTable':fsDot1dStaticAllowedToGoTable,'fsDot1dStaticAllowedToGoEntry':fsDot1dStaticAllowedToGoEntry,'fsDot1dStaticAllowedIsMember':fsDot1dStaticAllowedIsMember})