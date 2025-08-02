_X='atbrStaticReceivePort'
_W='atbrStaticAddress'
_V='atbrStaticLanId'
_U='atbrTpPort'
_T='atbrTpPortLanId'
_S='atbrTpFdbAddress'
_R='atbrTpFdbLanId'
_Q='atbrTpLanId'
_P='disabled'
_O='atbrStpPort'
_N='atbrStpPortLanId'
_M='atbrStpLanId'
_L='atbrBasePort'
_K='atbrBasePortLanId'
_J='unknown'
_I='atbrBaseLanId'
_H='NotificationType'
_G='OctetString'
_F='Timeout'
_E='read-write'
_D='Integer32'
_C='ATI-BRIDGE-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_H,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_H,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class BridgeId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class Timeout(Integer32):0
_AlliedTelesyn_ObjectIdentity=ObjectIdentity
alliedTelesyn=_AlliedTelesyn_ObjectIdentity((1,3,6,1,4,1,207))
_MibObject_ObjectIdentity=ObjectIdentity
mibObject=_MibObject_ObjectIdentity((1,3,6,1,4,1,207,8))
_SwitchMib_ObjectIdentity=ObjectIdentity
switchMib=_SwitchMib_ObjectIdentity((1,3,6,1,4,1,207,8,5))
_AtiBridgeMib_ObjectIdentity=ObjectIdentity
atiBridgeMib=_AtiBridgeMib_ObjectIdentity((1,3,6,1,4,1,207,8,5,10))
_AtbrBase_ObjectIdentity=ObjectIdentity
atbrBase=_AtbrBase_ObjectIdentity((1,3,6,1,4,1,207,8,5,10,1))
_AtbrBaseTable_Object=MibTable
atbrBaseTable=_AtbrBaseTable_Object((1,3,6,1,4,1,207,8,5,10,1,1))
if mibBuilder.loadTexts:atbrBaseTable.setStatus(_A)
_AtbrBaseEntry_Object=MibTableRow
atbrBaseEntry=_AtbrBaseEntry_Object((1,3,6,1,4,1,207,8,5,10,1,1,1))
atbrBaseEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:atbrBaseEntry.setStatus(_A)
_AtbrBaseLanId_Type=Integer32
_AtbrBaseLanId_Object=MibTableColumn
atbrBaseLanId=_AtbrBaseLanId_Object((1,3,6,1,4,1,207,8,5,10,1,1,1,1),_AtbrBaseLanId_Type())
atbrBaseLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrBaseLanId.setStatus(_A)
_AtbrBaseBridgeAddress_Type=MacAddress
_AtbrBaseBridgeAddress_Object=MibTableColumn
atbrBaseBridgeAddress=_AtbrBaseBridgeAddress_Object((1,3,6,1,4,1,207,8,5,10,1,1,1,2),_AtbrBaseBridgeAddress_Type())
atbrBaseBridgeAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrBaseBridgeAddress.setStatus(_A)
_AtbrBaseNumPorts_Type=Integer32
_AtbrBaseNumPorts_Object=MibTableColumn
atbrBaseNumPorts=_AtbrBaseNumPorts_Object((1,3,6,1,4,1,207,8,5,10,1,1,1,3),_AtbrBaseNumPorts_Type())
atbrBaseNumPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrBaseNumPorts.setStatus(_A)
class _AtbrBaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('transparent-only',2),('sourceroute-only',3),('srt',4)))
_AtbrBaseType_Type.__name__=_D
_AtbrBaseType_Object=MibTableColumn
atbrBaseType=_AtbrBaseType_Object((1,3,6,1,4,1,207,8,5,10,1,1,1,4),_AtbrBaseType_Type())
atbrBaseType.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrBaseType.setStatus(_A)
_AtbrBasePortTable_Object=MibTable
atbrBasePortTable=_AtbrBasePortTable_Object((1,3,6,1,4,1,207,8,5,10,1,4))
if mibBuilder.loadTexts:atbrBasePortTable.setStatus(_A)
_AtbrBasePortEntry_Object=MibTableRow
atbrBasePortEntry=_AtbrBasePortEntry_Object((1,3,6,1,4,1,207,8,5,10,1,4,1))
atbrBasePortEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:atbrBasePortEntry.setStatus(_A)
_AtbrBasePortLanId_Type=Integer32
_AtbrBasePortLanId_Object=MibTableColumn
atbrBasePortLanId=_AtbrBasePortLanId_Object((1,3,6,1,4,1,207,8,5,10,1,4,1,1),_AtbrBasePortLanId_Type())
atbrBasePortLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrBasePortLanId.setStatus(_A)
class _AtbrBasePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtbrBasePort_Type.__name__=_D
_AtbrBasePort_Object=MibTableColumn
atbrBasePort=_AtbrBasePort_Object((1,3,6,1,4,1,207,8,5,10,1,4,1,2),_AtbrBasePort_Type())
atbrBasePort.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrBasePort.setStatus(_A)
_AtbrBasePortIfIndex_Type=Integer32
_AtbrBasePortIfIndex_Object=MibTableColumn
atbrBasePortIfIndex=_AtbrBasePortIfIndex_Object((1,3,6,1,4,1,207,8,5,10,1,4,1,3),_AtbrBasePortIfIndex_Type())
atbrBasePortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrBasePortIfIndex.setStatus(_A)
_AtbrBasePortCircuit_Type=ObjectIdentifier
_AtbrBasePortCircuit_Object=MibTableColumn
atbrBasePortCircuit=_AtbrBasePortCircuit_Object((1,3,6,1,4,1,207,8,5,10,1,4,1,4),_AtbrBasePortCircuit_Type())
atbrBasePortCircuit.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrBasePortCircuit.setStatus(_A)
_AtbrBasePortDelayExceededDiscards_Type=Counter32
_AtbrBasePortDelayExceededDiscards_Object=MibTableColumn
atbrBasePortDelayExceededDiscards=_AtbrBasePortDelayExceededDiscards_Object((1,3,6,1,4,1,207,8,5,10,1,4,1,5),_AtbrBasePortDelayExceededDiscards_Type())
atbrBasePortDelayExceededDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrBasePortDelayExceededDiscards.setStatus(_A)
_AtbrBasePortMtuExceededDiscards_Type=Counter32
_AtbrBasePortMtuExceededDiscards_Object=MibTableColumn
atbrBasePortMtuExceededDiscards=_AtbrBasePortMtuExceededDiscards_Object((1,3,6,1,4,1,207,8,5,10,1,4,1,6),_AtbrBasePortMtuExceededDiscards_Type())
atbrBasePortMtuExceededDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrBasePortMtuExceededDiscards.setStatus(_A)
_AtbrStp_ObjectIdentity=ObjectIdentity
atbrStp=_AtbrStp_ObjectIdentity((1,3,6,1,4,1,207,8,5,10,2))
_AtbrStpTable_Object=MibTable
atbrStpTable=_AtbrStpTable_Object((1,3,6,1,4,1,207,8,5,10,2,1))
if mibBuilder.loadTexts:atbrStpTable.setStatus(_A)
_AtbrStpEntry_Object=MibTableRow
atbrStpEntry=_AtbrStpEntry_Object((1,3,6,1,4,1,207,8,5,10,2,1,1))
atbrStpEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:atbrStpEntry.setStatus(_A)
_AtbrStpLanId_Type=Integer32
_AtbrStpLanId_Object=MibTableColumn
atbrStpLanId=_AtbrStpLanId_Object((1,3,6,1,4,1,207,8,5,10,2,1,1,1),_AtbrStpLanId_Type())
atbrStpLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpLanId.setStatus(_A)
class _AtbrStpProtocolSpecification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('decLb100',2),('ieee8021d',3)))
_AtbrStpProtocolSpecification_Type.__name__=_D
_AtbrStpProtocolSpecification_Object=MibTableColumn
atbrStpProtocolSpecification=_AtbrStpProtocolSpecification_Object((1,3,6,1,4,1,207,8,5,10,2,1,1,2),_AtbrStpProtocolSpecification_Type())
atbrStpProtocolSpecification.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpProtocolSpecification.setStatus(_A)
class _AtbrStpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtbrStpPriority_Type.__name__=_D
_AtbrStpPriority_Object=MibTableColumn
atbrStpPriority=_AtbrStpPriority_Object((1,3,6,1,4,1,207,8,5,10,2,1,1,3),_AtbrStpPriority_Type())
atbrStpPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:atbrStpPriority.setStatus(_A)
_AtbrStpTimeSinceTopologyChange_Type=TimeTicks
_AtbrStpTimeSinceTopologyChange_Object=MibTableColumn
atbrStpTimeSinceTopologyChange=_AtbrStpTimeSinceTopologyChange_Object((1,3,6,1,4,1,207,8,5,10,2,1,1,4),_AtbrStpTimeSinceTopologyChange_Type())
atbrStpTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpTimeSinceTopologyChange.setStatus(_A)
_AtbrStpTopChanges_Type=Counter32
_AtbrStpTopChanges_Object=MibTableColumn
atbrStpTopChanges=_AtbrStpTopChanges_Object((1,3,6,1,4,1,207,8,5,10,2,1,1,5),_AtbrStpTopChanges_Type())
atbrStpTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpTopChanges.setStatus(_A)
_AtbrStpDesignatedRoot_Type=BridgeId
_AtbrStpDesignatedRoot_Object=MibTableColumn
atbrStpDesignatedRoot=_AtbrStpDesignatedRoot_Object((1,3,6,1,4,1,207,8,5,10,2,1,1,6),_AtbrStpDesignatedRoot_Type())
atbrStpDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpDesignatedRoot.setStatus(_A)
_AtbrStpRootCost_Type=Integer32
_AtbrStpRootCost_Object=MibTableColumn
atbrStpRootCost=_AtbrStpRootCost_Object((1,3,6,1,4,1,207,8,5,10,2,1,1,7),_AtbrStpRootCost_Type())
atbrStpRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpRootCost.setStatus(_A)
_AtbrStpRootPort_Type=Integer32
_AtbrStpRootPort_Object=MibTableColumn
atbrStpRootPort=_AtbrStpRootPort_Object((1,3,6,1,4,1,207,8,5,10,2,1,1,8),_AtbrStpRootPort_Type())
atbrStpRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpRootPort.setStatus(_A)
_AtbrStpMaxAge_Type=Timeout
_AtbrStpMaxAge_Object=MibTableColumn
atbrStpMaxAge=_AtbrStpMaxAge_Object((1,3,6,1,4,1,207,8,5,10,2,1,1,9),_AtbrStpMaxAge_Type())
atbrStpMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpMaxAge.setStatus(_A)
_AtbrStpHelloTime_Type=Timeout
_AtbrStpHelloTime_Object=MibTableColumn
atbrStpHelloTime=_AtbrStpHelloTime_Object((1,3,6,1,4,1,207,8,5,10,2,1,1,10),_AtbrStpHelloTime_Type())
atbrStpHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpHelloTime.setStatus(_A)
_AtbrStpHoldTime_Type=Integer32
_AtbrStpHoldTime_Object=MibTableColumn
atbrStpHoldTime=_AtbrStpHoldTime_Object((1,3,6,1,4,1,207,8,5,10,2,1,1,11),_AtbrStpHoldTime_Type())
atbrStpHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpHoldTime.setStatus(_A)
_AtbrStpForwardDelay_Type=Timeout
_AtbrStpForwardDelay_Object=MibTableColumn
atbrStpForwardDelay=_AtbrStpForwardDelay_Object((1,3,6,1,4,1,207,8,5,10,2,1,1,12),_AtbrStpForwardDelay_Type())
atbrStpForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpForwardDelay.setStatus(_A)
class _AtbrStpBridgeMaxAge_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_AtbrStpBridgeMaxAge_Type.__name__=_F
_AtbrStpBridgeMaxAge_Object=MibTableColumn
atbrStpBridgeMaxAge=_AtbrStpBridgeMaxAge_Object((1,3,6,1,4,1,207,8,5,10,2,1,1,13),_AtbrStpBridgeMaxAge_Type())
atbrStpBridgeMaxAge.setMaxAccess(_E)
if mibBuilder.loadTexts:atbrStpBridgeMaxAge.setStatus(_A)
class _AtbrStpBridgeHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_AtbrStpBridgeHelloTime_Type.__name__=_F
_AtbrStpBridgeHelloTime_Object=MibTableColumn
atbrStpBridgeHelloTime=_AtbrStpBridgeHelloTime_Object((1,3,6,1,4,1,207,8,5,10,2,1,1,14),_AtbrStpBridgeHelloTime_Type())
atbrStpBridgeHelloTime.setMaxAccess(_E)
if mibBuilder.loadTexts:atbrStpBridgeHelloTime.setStatus(_A)
class _AtbrStpBridgeForwardDelay_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_AtbrStpBridgeForwardDelay_Type.__name__=_F
_AtbrStpBridgeForwardDelay_Object=MibTableColumn
atbrStpBridgeForwardDelay=_AtbrStpBridgeForwardDelay_Object((1,3,6,1,4,1,207,8,5,10,2,1,1,15),_AtbrStpBridgeForwardDelay_Type())
atbrStpBridgeForwardDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:atbrStpBridgeForwardDelay.setStatus(_A)
_AtbrStpPortTable_Object=MibTable
atbrStpPortTable=_AtbrStpPortTable_Object((1,3,6,1,4,1,207,8,5,10,2,15))
if mibBuilder.loadTexts:atbrStpPortTable.setStatus(_A)
_AtbrStpPortEntry_Object=MibTableRow
atbrStpPortEntry=_AtbrStpPortEntry_Object((1,3,6,1,4,1,207,8,5,10,2,15,1))
atbrStpPortEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:atbrStpPortEntry.setStatus(_A)
_AtbrStpPortLanId_Type=Integer32
_AtbrStpPortLanId_Object=MibTableColumn
atbrStpPortLanId=_AtbrStpPortLanId_Object((1,3,6,1,4,1,207,8,5,10,2,15,1,1),_AtbrStpPortLanId_Type())
atbrStpPortLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpPortLanId.setStatus(_A)
class _AtbrStpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtbrStpPort_Type.__name__=_D
_AtbrStpPort_Object=MibTableColumn
atbrStpPort=_AtbrStpPort_Object((1,3,6,1,4,1,207,8,5,10,2,15,1,2),_AtbrStpPort_Type())
atbrStpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpPort.setStatus(_A)
class _AtbrStpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtbrStpPortPriority_Type.__name__=_D
_AtbrStpPortPriority_Object=MibTableColumn
atbrStpPortPriority=_AtbrStpPortPriority_Object((1,3,6,1,4,1,207,8,5,10,2,15,1,3),_AtbrStpPortPriority_Type())
atbrStpPortPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:atbrStpPortPriority.setStatus(_A)
class _AtbrStpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_P,1),('blocking',2),('listening',3),('learning',4),('forwarding',5),('broken',6)))
_AtbrStpPortState_Type.__name__=_D
_AtbrStpPortState_Object=MibTableColumn
atbrStpPortState=_AtbrStpPortState_Object((1,3,6,1,4,1,207,8,5,10,2,15,1,4),_AtbrStpPortState_Type())
atbrStpPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpPortState.setStatus(_A)
class _AtbrStpPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_P,2)))
_AtbrStpPortEnable_Type.__name__=_D
_AtbrStpPortEnable_Object=MibTableColumn
atbrStpPortEnable=_AtbrStpPortEnable_Object((1,3,6,1,4,1,207,8,5,10,2,15,1,5),_AtbrStpPortEnable_Type())
atbrStpPortEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:atbrStpPortEnable.setStatus(_A)
class _AtbrStpPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtbrStpPortPathCost_Type.__name__=_D
_AtbrStpPortPathCost_Object=MibTableColumn
atbrStpPortPathCost=_AtbrStpPortPathCost_Object((1,3,6,1,4,1,207,8,5,10,2,15,1,6),_AtbrStpPortPathCost_Type())
atbrStpPortPathCost.setMaxAccess(_E)
if mibBuilder.loadTexts:atbrStpPortPathCost.setStatus(_A)
_AtbrStpPortDesignatedRoot_Type=BridgeId
_AtbrStpPortDesignatedRoot_Object=MibTableColumn
atbrStpPortDesignatedRoot=_AtbrStpPortDesignatedRoot_Object((1,3,6,1,4,1,207,8,5,10,2,15,1,7),_AtbrStpPortDesignatedRoot_Type())
atbrStpPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpPortDesignatedRoot.setStatus(_A)
_AtbrStpPortDesignatedCost_Type=Integer32
_AtbrStpPortDesignatedCost_Object=MibTableColumn
atbrStpPortDesignatedCost=_AtbrStpPortDesignatedCost_Object((1,3,6,1,4,1,207,8,5,10,2,15,1,8),_AtbrStpPortDesignatedCost_Type())
atbrStpPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpPortDesignatedCost.setStatus(_A)
_AtbrStpPortDesignatedBridge_Type=BridgeId
_AtbrStpPortDesignatedBridge_Object=MibTableColumn
atbrStpPortDesignatedBridge=_AtbrStpPortDesignatedBridge_Object((1,3,6,1,4,1,207,8,5,10,2,15,1,9),_AtbrStpPortDesignatedBridge_Type())
atbrStpPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpPortDesignatedBridge.setStatus(_A)
class _AtbrStpPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AtbrStpPortDesignatedPort_Type.__name__=_G
_AtbrStpPortDesignatedPort_Object=MibTableColumn
atbrStpPortDesignatedPort=_AtbrStpPortDesignatedPort_Object((1,3,6,1,4,1,207,8,5,10,2,15,1,10),_AtbrStpPortDesignatedPort_Type())
atbrStpPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpPortDesignatedPort.setStatus(_A)
_AtbrStpPortForwardTransitions_Type=Counter32
_AtbrStpPortForwardTransitions_Object=MibTableColumn
atbrStpPortForwardTransitions=_AtbrStpPortForwardTransitions_Object((1,3,6,1,4,1,207,8,5,10,2,15,1,11),_AtbrStpPortForwardTransitions_Type())
atbrStpPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStpPortForwardTransitions.setStatus(_A)
_AtbrSr_ObjectIdentity=ObjectIdentity
atbrSr=_AtbrSr_ObjectIdentity((1,3,6,1,4,1,207,8,5,10,3))
_AtbrTp_ObjectIdentity=ObjectIdentity
atbrTp=_AtbrTp_ObjectIdentity((1,3,6,1,4,1,207,8,5,10,4))
_AtbrTpTable_Object=MibTable
atbrTpTable=_AtbrTpTable_Object((1,3,6,1,4,1,207,8,5,10,4,1))
if mibBuilder.loadTexts:atbrTpTable.setStatus(_A)
_AtbrTpEntry_Object=MibTableRow
atbrTpEntry=_AtbrTpEntry_Object((1,3,6,1,4,1,207,8,5,10,4,1,1))
atbrTpEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:atbrTpEntry.setStatus(_A)
_AtbrTpLanId_Type=Integer32
_AtbrTpLanId_Object=MibTableColumn
atbrTpLanId=_AtbrTpLanId_Object((1,3,6,1,4,1,207,8,5,10,4,1,1,1),_AtbrTpLanId_Type())
atbrTpLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrTpLanId.setStatus(_A)
_AtbrTpLearnedEntryDiscards_Type=Counter32
_AtbrTpLearnedEntryDiscards_Object=MibTableColumn
atbrTpLearnedEntryDiscards=_AtbrTpLearnedEntryDiscards_Object((1,3,6,1,4,1,207,8,5,10,4,1,1,2),_AtbrTpLearnedEntryDiscards_Type())
atbrTpLearnedEntryDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrTpLearnedEntryDiscards.setStatus(_A)
class _AtbrTpAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_AtbrTpAgingTime_Type.__name__=_D
_AtbrTpAgingTime_Object=MibTableColumn
atbrTpAgingTime=_AtbrTpAgingTime_Object((1,3,6,1,4,1,207,8,5,10,4,1,1,3),_AtbrTpAgingTime_Type())
atbrTpAgingTime.setMaxAccess(_E)
if mibBuilder.loadTexts:atbrTpAgingTime.setStatus(_A)
_AtbrTpFdbTable_Object=MibTable
atbrTpFdbTable=_AtbrTpFdbTable_Object((1,3,6,1,4,1,207,8,5,10,4,3))
if mibBuilder.loadTexts:atbrTpFdbTable.setStatus(_A)
_AtbrTpFdbEntry_Object=MibTableRow
atbrTpFdbEntry=_AtbrTpFdbEntry_Object((1,3,6,1,4,1,207,8,5,10,4,3,1))
atbrTpFdbEntry.setIndexNames((0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:atbrTpFdbEntry.setStatus(_A)
_AtbrTpFdbLanId_Type=Integer32
_AtbrTpFdbLanId_Object=MibTableColumn
atbrTpFdbLanId=_AtbrTpFdbLanId_Object((1,3,6,1,4,1,207,8,5,10,4,3,1,1),_AtbrTpFdbLanId_Type())
atbrTpFdbLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrTpFdbLanId.setStatus(_A)
_AtbrTpFdbAddress_Type=MacAddress
_AtbrTpFdbAddress_Object=MibTableColumn
atbrTpFdbAddress=_AtbrTpFdbAddress_Object((1,3,6,1,4,1,207,8,5,10,4,3,1,2),_AtbrTpFdbAddress_Type())
atbrTpFdbAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrTpFdbAddress.setStatus(_A)
_AtbrTpFdbPort_Type=Integer32
_AtbrTpFdbPort_Object=MibTableColumn
atbrTpFdbPort=_AtbrTpFdbPort_Object((1,3,6,1,4,1,207,8,5,10,4,3,1,3),_AtbrTpFdbPort_Type())
atbrTpFdbPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrTpFdbPort.setStatus(_A)
class _AtbrTpFdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('inactive',1),('le-arp-pending',2),('vcc-setup-pending',3),('vlan-resolve-pending',4),('join-pending',5),('active',6),('other',7)))
_AtbrTpFdbStatus_Type.__name__=_D
_AtbrTpFdbStatus_Object=MibTableColumn
atbrTpFdbStatus=_AtbrTpFdbStatus_Object((1,3,6,1,4,1,207,8,5,10,4,3,1,4),_AtbrTpFdbStatus_Type())
atbrTpFdbStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrTpFdbStatus.setStatus(_A)
_AtbrTpPortTable_Object=MibTable
atbrTpPortTable=_AtbrTpPortTable_Object((1,3,6,1,4,1,207,8,5,10,4,4))
if mibBuilder.loadTexts:atbrTpPortTable.setStatus(_A)
_AtbrTpPortEntry_Object=MibTableRow
atbrTpPortEntry=_AtbrTpPortEntry_Object((1,3,6,1,4,1,207,8,5,10,4,4,1))
atbrTpPortEntry.setIndexNames((0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:atbrTpPortEntry.setStatus(_A)
_AtbrTpPortLanId_Type=Integer32
_AtbrTpPortLanId_Object=MibTableColumn
atbrTpPortLanId=_AtbrTpPortLanId_Object((1,3,6,1,4,1,207,8,5,10,4,4,1,1),_AtbrTpPortLanId_Type())
atbrTpPortLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrTpPortLanId.setStatus(_A)
class _AtbrTpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtbrTpPort_Type.__name__=_D
_AtbrTpPort_Object=MibTableColumn
atbrTpPort=_AtbrTpPort_Object((1,3,6,1,4,1,207,8,5,10,4,4,1,2),_AtbrTpPort_Type())
atbrTpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrTpPort.setStatus(_A)
_AtbrTpPortMaxInfo_Type=Integer32
_AtbrTpPortMaxInfo_Object=MibTableColumn
atbrTpPortMaxInfo=_AtbrTpPortMaxInfo_Object((1,3,6,1,4,1,207,8,5,10,4,4,1,3),_AtbrTpPortMaxInfo_Type())
atbrTpPortMaxInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrTpPortMaxInfo.setStatus(_A)
_AtbrTpPortInFrames_Type=Counter32
_AtbrTpPortInFrames_Object=MibTableColumn
atbrTpPortInFrames=_AtbrTpPortInFrames_Object((1,3,6,1,4,1,207,8,5,10,4,4,1,4),_AtbrTpPortInFrames_Type())
atbrTpPortInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrTpPortInFrames.setStatus(_A)
_AtbrTpPortOutFrames_Type=Counter32
_AtbrTpPortOutFrames_Object=MibTableColumn
atbrTpPortOutFrames=_AtbrTpPortOutFrames_Object((1,3,6,1,4,1,207,8,5,10,4,4,1,5),_AtbrTpPortOutFrames_Type())
atbrTpPortOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrTpPortOutFrames.setStatus(_A)
_AtbrTpPortInDiscards_Type=Counter32
_AtbrTpPortInDiscards_Object=MibTableColumn
atbrTpPortInDiscards=_AtbrTpPortInDiscards_Object((1,3,6,1,4,1,207,8,5,10,4,4,1,6),_AtbrTpPortInDiscards_Type())
atbrTpPortInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrTpPortInDiscards.setStatus(_A)
_AtbrStatic_ObjectIdentity=ObjectIdentity
atbrStatic=_AtbrStatic_ObjectIdentity((1,3,6,1,4,1,207,8,5,10,5))
_AtbrStaticTable_Object=MibTable
atbrStaticTable=_AtbrStaticTable_Object((1,3,6,1,4,1,207,8,5,10,5,1))
if mibBuilder.loadTexts:atbrStaticTable.setStatus(_A)
_AtbrStaticEntry_Object=MibTableRow
atbrStaticEntry=_AtbrStaticEntry_Object((1,3,6,1,4,1,207,8,5,10,5,1,1))
atbrStaticEntry.setIndexNames((0,_C,_V),(0,_C,_W),(0,_C,_X))
if mibBuilder.loadTexts:atbrStaticEntry.setStatus(_A)
_AtbrStaticLanId_Type=Integer32
_AtbrStaticLanId_Object=MibTableColumn
atbrStaticLanId=_AtbrStaticLanId_Object((1,3,6,1,4,1,207,8,5,10,5,1,1,1),_AtbrStaticLanId_Type())
atbrStaticLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atbrStaticLanId.setStatus(_A)
_AtbrStaticAddress_Type=MacAddress
_AtbrStaticAddress_Object=MibTableColumn
atbrStaticAddress=_AtbrStaticAddress_Object((1,3,6,1,4,1,207,8,5,10,5,1,1,2),_AtbrStaticAddress_Type())
atbrStaticAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:atbrStaticAddress.setStatus(_A)
_AtbrStaticReceivePort_Type=Integer32
_AtbrStaticReceivePort_Object=MibTableColumn
atbrStaticReceivePort=_AtbrStaticReceivePort_Object((1,3,6,1,4,1,207,8,5,10,5,1,1,3),_AtbrStaticReceivePort_Type())
atbrStaticReceivePort.setMaxAccess(_E)
if mibBuilder.loadTexts:atbrStaticReceivePort.setStatus(_A)
_AtbrStaticAllowedToGoTo_Type=OctetString
_AtbrStaticAllowedToGoTo_Object=MibTableColumn
atbrStaticAllowedToGoTo=_AtbrStaticAllowedToGoTo_Object((1,3,6,1,4,1,207,8,5,10,5,1,1,4),_AtbrStaticAllowedToGoTo_Type())
atbrStaticAllowedToGoTo.setMaxAccess(_E)
if mibBuilder.loadTexts:atbrStaticAllowedToGoTo.setStatus(_A)
class _AtbrStaticStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('invalid',2),('permanent',3),('deleteOnReset',4),('deleteOnTimeout',5)))
_AtbrStaticStatus_Type.__name__=_D
_AtbrStaticStatus_Object=MibTableColumn
atbrStaticStatus=_AtbrStaticStatus_Object((1,3,6,1,4,1,207,8,5,10,5,1,1,5),_AtbrStaticStatus_Type())
atbrStaticStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:atbrStaticStatus.setStatus(_A)
newRoot=NotificationType((1,3,6,1,4,1,207,0,101))
if mibBuilder.loadTexts:newRoot.setStatus('')
topologyChange=NotificationType((1,3,6,1,4,1,207,0,102))
if mibBuilder.loadTexts:topologyChange.setStatus('')
mibBuilder.exportSymbols(_C,**{'MacAddress':MacAddress,'BridgeId':BridgeId,_F:Timeout,'alliedTelesyn':alliedTelesyn,'newRoot':newRoot,'topologyChange':topologyChange,'mibObject':mibObject,'switchMib':switchMib,'atiBridgeMib':atiBridgeMib,'atbrBase':atbrBase,'atbrBaseTable':atbrBaseTable,'atbrBaseEntry':atbrBaseEntry,_I:atbrBaseLanId,'atbrBaseBridgeAddress':atbrBaseBridgeAddress,'atbrBaseNumPorts':atbrBaseNumPorts,'atbrBaseType':atbrBaseType,'atbrBasePortTable':atbrBasePortTable,'atbrBasePortEntry':atbrBasePortEntry,_K:atbrBasePortLanId,_L:atbrBasePort,'atbrBasePortIfIndex':atbrBasePortIfIndex,'atbrBasePortCircuit':atbrBasePortCircuit,'atbrBasePortDelayExceededDiscards':atbrBasePortDelayExceededDiscards,'atbrBasePortMtuExceededDiscards':atbrBasePortMtuExceededDiscards,'atbrStp':atbrStp,'atbrStpTable':atbrStpTable,'atbrStpEntry':atbrStpEntry,_M:atbrStpLanId,'atbrStpProtocolSpecification':atbrStpProtocolSpecification,'atbrStpPriority':atbrStpPriority,'atbrStpTimeSinceTopologyChange':atbrStpTimeSinceTopologyChange,'atbrStpTopChanges':atbrStpTopChanges,'atbrStpDesignatedRoot':atbrStpDesignatedRoot,'atbrStpRootCost':atbrStpRootCost,'atbrStpRootPort':atbrStpRootPort,'atbrStpMaxAge':atbrStpMaxAge,'atbrStpHelloTime':atbrStpHelloTime,'atbrStpHoldTime':atbrStpHoldTime,'atbrStpForwardDelay':atbrStpForwardDelay,'atbrStpBridgeMaxAge':atbrStpBridgeMaxAge,'atbrStpBridgeHelloTime':atbrStpBridgeHelloTime,'atbrStpBridgeForwardDelay':atbrStpBridgeForwardDelay,'atbrStpPortTable':atbrStpPortTable,'atbrStpPortEntry':atbrStpPortEntry,_N:atbrStpPortLanId,_O:atbrStpPort,'atbrStpPortPriority':atbrStpPortPriority,'atbrStpPortState':atbrStpPortState,'atbrStpPortEnable':atbrStpPortEnable,'atbrStpPortPathCost':atbrStpPortPathCost,'atbrStpPortDesignatedRoot':atbrStpPortDesignatedRoot,'atbrStpPortDesignatedCost':atbrStpPortDesignatedCost,'atbrStpPortDesignatedBridge':atbrStpPortDesignatedBridge,'atbrStpPortDesignatedPort':atbrStpPortDesignatedPort,'atbrStpPortForwardTransitions':atbrStpPortForwardTransitions,'atbrSr':atbrSr,'atbrTp':atbrTp,'atbrTpTable':atbrTpTable,'atbrTpEntry':atbrTpEntry,_Q:atbrTpLanId,'atbrTpLearnedEntryDiscards':atbrTpLearnedEntryDiscards,'atbrTpAgingTime':atbrTpAgingTime,'atbrTpFdbTable':atbrTpFdbTable,'atbrTpFdbEntry':atbrTpFdbEntry,_R:atbrTpFdbLanId,_S:atbrTpFdbAddress,'atbrTpFdbPort':atbrTpFdbPort,'atbrTpFdbStatus':atbrTpFdbStatus,'atbrTpPortTable':atbrTpPortTable,'atbrTpPortEntry':atbrTpPortEntry,_T:atbrTpPortLanId,_U:atbrTpPort,'atbrTpPortMaxInfo':atbrTpPortMaxInfo,'atbrTpPortInFrames':atbrTpPortInFrames,'atbrTpPortOutFrames':atbrTpPortOutFrames,'atbrTpPortInDiscards':atbrTpPortInDiscards,'atbrStatic':atbrStatic,'atbrStaticTable':atbrStaticTable,'atbrStaticEntry':atbrStaticEntry,_V:atbrStaticLanId,_W:atbrStaticAddress,_X:atbrStaticReceivePort,'atbrStaticAllowedToGoTo':atbrStaticAllowedToGoTo,'atbrStaticStatus':atbrStaticStatus})