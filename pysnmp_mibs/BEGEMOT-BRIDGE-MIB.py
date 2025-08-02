_T='begemotBridgeTpEntry'
_S='begemotBridgeStpExtPortEntry'
_R='begemotBridgeStpEntry'
_Q='BridgeIfNameOrEmpty'
_P='begemotBridgeTpFdbAddress'
_O='read-create'
_N='unknown'
_M='frames'
_L='seconds'
_K='enabled'
_J='disabled'
_I='begemotBridgeBasePortIfIndex'
_H='Timeout'
_G='centi-seconds'
_F='begemotBridgeBaseName'
_E='BEGEMOT-BRIDGE-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
begemot,=mibBuilder.importSymbols('BEGEMOT-MIB','begemot')
BridgeId,Timeout=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId',_H)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
begemotBridge=ModuleIdentity((1,3,6,1,4,1,12325,1,205))
if mibBuilder.loadTexts:begemotBridge.setRevisions(('2007-08-06 00:00','2006-11-21 00:00','2006-07-27 00:00'))
class BridgeIfName(TextualConvention,OctetString):status=_A;displayHint='16a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
class BridgeIfNameOrEmpty(TextualConvention,OctetString):status=_A;displayHint='16a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
class BridgePortId(TextualConvention,OctetString):status=_A;displayHint='1x.1x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_BegemotBridgeNotifications_ObjectIdentity=ObjectIdentity
begemotBridgeNotifications=_BegemotBridgeNotifications_ObjectIdentity((1,3,6,1,4,1,12325,1,205,0))
_BegemotBridgeBase_ObjectIdentity=ObjectIdentity
begemotBridgeBase=_BegemotBridgeBase_ObjectIdentity((1,3,6,1,4,1,12325,1,205,1))
_BegemotBridgeBaseTable_Object=MibTable
begemotBridgeBaseTable=_BegemotBridgeBaseTable_Object((1,3,6,1,4,1,12325,1,205,1,1))
if mibBuilder.loadTexts:begemotBridgeBaseTable.setStatus(_A)
_BegemotBridgeBaseEntry_Object=MibTableRow
begemotBridgeBaseEntry=_BegemotBridgeBaseEntry_Object((1,3,6,1,4,1,12325,1,205,1,1,1))
begemotBridgeBaseEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:begemotBridgeBaseEntry.setStatus(_A)
_BegemotBridgeBaseName_Type=BridgeIfName
_BegemotBridgeBaseName_Object=MibTableColumn
begemotBridgeBaseName=_BegemotBridgeBaseName_Object((1,3,6,1,4,1,12325,1,205,1,1,1,1),_BegemotBridgeBaseName_Type())
begemotBridgeBaseName.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeBaseName.setStatus(_A)
_BegemotBridgeBaseAddress_Type=MacAddress
_BegemotBridgeBaseAddress_Object=MibTableColumn
begemotBridgeBaseAddress=_BegemotBridgeBaseAddress_Object((1,3,6,1,4,1,12325,1,205,1,1,1,2),_BegemotBridgeBaseAddress_Type())
begemotBridgeBaseAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeBaseAddress.setStatus(_A)
_BegemotBridgeBaseNumPorts_Type=Integer32
_BegemotBridgeBaseNumPorts_Object=MibTableColumn
begemotBridgeBaseNumPorts=_BegemotBridgeBaseNumPorts_Object((1,3,6,1,4,1,12325,1,205,1,1,1,3),_BegemotBridgeBaseNumPorts_Type())
begemotBridgeBaseNumPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeBaseNumPorts.setStatus(_A)
class _BegemotBridgeBaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('transparent-only',2),('sourceroute-only',3),('srt',4)))
_BegemotBridgeBaseType_Type.__name__=_D
_BegemotBridgeBaseType_Object=MibTableColumn
begemotBridgeBaseType=_BegemotBridgeBaseType_Object((1,3,6,1,4,1,12325,1,205,1,1,1,4),_BegemotBridgeBaseType_Type())
begemotBridgeBaseType.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeBaseType.setStatus(_A)
_BegemotBridgeBaseStatus_Type=RowStatus
_BegemotBridgeBaseStatus_Object=MibTableColumn
begemotBridgeBaseStatus=_BegemotBridgeBaseStatus_Object((1,3,6,1,4,1,12325,1,205,1,1,1,5),_BegemotBridgeBaseStatus_Type())
begemotBridgeBaseStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:begemotBridgeBaseStatus.setStatus(_A)
_BegemotBridgeBasePortTable_Object=MibTable
begemotBridgeBasePortTable=_BegemotBridgeBasePortTable_Object((1,3,6,1,4,1,12325,1,205,1,2))
if mibBuilder.loadTexts:begemotBridgeBasePortTable.setStatus(_A)
_BegemotBridgeBasePortEntry_Object=MibTableRow
begemotBridgeBasePortEntry=_BegemotBridgeBasePortEntry_Object((1,3,6,1,4,1,12325,1,205,1,2,1))
begemotBridgeBasePortEntry.setIndexNames((0,_E,_F),(0,_E,_I))
if mibBuilder.loadTexts:begemotBridgeBasePortEntry.setStatus(_A)
class _BegemotBridgeBasePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BegemotBridgeBasePort_Type.__name__=_D
_BegemotBridgeBasePort_Object=MibTableColumn
begemotBridgeBasePort=_BegemotBridgeBasePort_Object((1,3,6,1,4,1,12325,1,205,1,2,1,1),_BegemotBridgeBasePort_Type())
begemotBridgeBasePort.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeBasePort.setStatus(_A)
_BegemotBridgeBasePortIfIndex_Type=InterfaceIndex
_BegemotBridgeBasePortIfIndex_Object=MibTableColumn
begemotBridgeBasePortIfIndex=_BegemotBridgeBasePortIfIndex_Object((1,3,6,1,4,1,12325,1,205,1,2,1,2),_BegemotBridgeBasePortIfIndex_Type())
begemotBridgeBasePortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeBasePortIfIndex.setStatus(_A)
class _BegemotBridgeBaseSpanEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_BegemotBridgeBaseSpanEnabled_Type.__name__=_D
_BegemotBridgeBaseSpanEnabled_Object=MibTableColumn
begemotBridgeBaseSpanEnabled=_BegemotBridgeBaseSpanEnabled_Object((1,3,6,1,4,1,12325,1,205,1,2,1,3),_BegemotBridgeBaseSpanEnabled_Type())
begemotBridgeBaseSpanEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeBaseSpanEnabled.setStatus(_A)
_BegemotBridgeBasePortDelayExceededDiscards_Type=Counter32
_BegemotBridgeBasePortDelayExceededDiscards_Object=MibTableColumn
begemotBridgeBasePortDelayExceededDiscards=_BegemotBridgeBasePortDelayExceededDiscards_Object((1,3,6,1,4,1,12325,1,205,1,2,1,4),_BegemotBridgeBasePortDelayExceededDiscards_Type())
begemotBridgeBasePortDelayExceededDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeBasePortDelayExceededDiscards.setStatus(_A)
_BegemotBridgeBasePortMtuExceededDiscards_Type=Counter32
_BegemotBridgeBasePortMtuExceededDiscards_Object=MibTableColumn
begemotBridgeBasePortMtuExceededDiscards=_BegemotBridgeBasePortMtuExceededDiscards_Object((1,3,6,1,4,1,12325,1,205,1,2,1,5),_BegemotBridgeBasePortMtuExceededDiscards_Type())
begemotBridgeBasePortMtuExceededDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeBasePortMtuExceededDiscards.setStatus(_A)
_BegemotBridgeBasePortStatus_Type=RowStatus
_BegemotBridgeBasePortStatus_Object=MibTableColumn
begemotBridgeBasePortStatus=_BegemotBridgeBasePortStatus_Object((1,3,6,1,4,1,12325,1,205,1,2,1,6),_BegemotBridgeBasePortStatus_Type())
begemotBridgeBasePortStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:begemotBridgeBasePortStatus.setStatus(_A)
_BegemotBridgeBasePortPrivate_Type=TruthValue
_BegemotBridgeBasePortPrivate_Object=MibTableColumn
begemotBridgeBasePortPrivate=_BegemotBridgeBasePortPrivate_Object((1,3,6,1,4,1,12325,1,205,1,2,1,7),_BegemotBridgeBasePortPrivate_Type())
begemotBridgeBasePortPrivate.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeBasePortPrivate.setStatus(_A)
_BegemotBridgeStp_ObjectIdentity=ObjectIdentity
begemotBridgeStp=_BegemotBridgeStp_ObjectIdentity((1,3,6,1,4,1,12325,1,205,2))
_BegemotBridgeStpTable_Object=MibTable
begemotBridgeStpTable=_BegemotBridgeStpTable_Object((1,3,6,1,4,1,12325,1,205,2,1))
if mibBuilder.loadTexts:begemotBridgeStpTable.setStatus(_A)
_BegemotBridgeStpEntry_Object=MibTableRow
begemotBridgeStpEntry=_BegemotBridgeStpEntry_Object((1,3,6,1,4,1,12325,1,205,2,1,1))
if mibBuilder.loadTexts:begemotBridgeStpEntry.setStatus(_A)
class _BegemotBridgeStpProtocolSpecification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('decLb100',2),('ieee8021d',3)))
_BegemotBridgeStpProtocolSpecification_Type.__name__=_D
_BegemotBridgeStpProtocolSpecification_Object=MibTableColumn
begemotBridgeStpProtocolSpecification=_BegemotBridgeStpProtocolSpecification_Object((1,3,6,1,4,1,12325,1,205,2,1,1,1),_BegemotBridgeStpProtocolSpecification_Type())
begemotBridgeStpProtocolSpecification.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpProtocolSpecification.setStatus(_A)
class _BegemotBridgeStpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BegemotBridgeStpPriority_Type.__name__=_D
_BegemotBridgeStpPriority_Object=MibTableColumn
begemotBridgeStpPriority=_BegemotBridgeStpPriority_Object((1,3,6,1,4,1,12325,1,205,2,1,1,2),_BegemotBridgeStpPriority_Type())
begemotBridgeStpPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeStpPriority.setStatus(_A)
_BegemotBridgeStpTimeSinceTopologyChange_Type=TimeTicks
_BegemotBridgeStpTimeSinceTopologyChange_Object=MibTableColumn
begemotBridgeStpTimeSinceTopologyChange=_BegemotBridgeStpTimeSinceTopologyChange_Object((1,3,6,1,4,1,12325,1,205,2,1,1,3),_BegemotBridgeStpTimeSinceTopologyChange_Type())
begemotBridgeStpTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpTimeSinceTopologyChange.setStatus(_A)
if mibBuilder.loadTexts:begemotBridgeStpTimeSinceTopologyChange.setUnits(_G)
_BegemotBridgeStpTopChanges_Type=Counter32
_BegemotBridgeStpTopChanges_Object=MibTableColumn
begemotBridgeStpTopChanges=_BegemotBridgeStpTopChanges_Object((1,3,6,1,4,1,12325,1,205,2,1,1,4),_BegemotBridgeStpTopChanges_Type())
begemotBridgeStpTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpTopChanges.setStatus(_A)
_BegemotBridgeStpDesignatedRoot_Type=BridgeId
_BegemotBridgeStpDesignatedRoot_Object=MibTableColumn
begemotBridgeStpDesignatedRoot=_BegemotBridgeStpDesignatedRoot_Object((1,3,6,1,4,1,12325,1,205,2,1,1,5),_BegemotBridgeStpDesignatedRoot_Type())
begemotBridgeStpDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpDesignatedRoot.setStatus(_A)
_BegemotBridgeStpRootCost_Type=Integer32
_BegemotBridgeStpRootCost_Object=MibTableColumn
begemotBridgeStpRootCost=_BegemotBridgeStpRootCost_Object((1,3,6,1,4,1,12325,1,205,2,1,1,6),_BegemotBridgeStpRootCost_Type())
begemotBridgeStpRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpRootCost.setStatus(_A)
_BegemotBridgeStpRootPort_Type=Integer32
_BegemotBridgeStpRootPort_Object=MibTableColumn
begemotBridgeStpRootPort=_BegemotBridgeStpRootPort_Object((1,3,6,1,4,1,12325,1,205,2,1,1,7),_BegemotBridgeStpRootPort_Type())
begemotBridgeStpRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpRootPort.setStatus(_A)
_BegemotBridgeStpMaxAge_Type=Timeout
_BegemotBridgeStpMaxAge_Object=MibTableColumn
begemotBridgeStpMaxAge=_BegemotBridgeStpMaxAge_Object((1,3,6,1,4,1,12325,1,205,2,1,1,8),_BegemotBridgeStpMaxAge_Type())
begemotBridgeStpMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpMaxAge.setStatus(_A)
if mibBuilder.loadTexts:begemotBridgeStpMaxAge.setUnits(_G)
_BegemotBridgeStpHelloTime_Type=Timeout
_BegemotBridgeStpHelloTime_Object=MibTableColumn
begemotBridgeStpHelloTime=_BegemotBridgeStpHelloTime_Object((1,3,6,1,4,1,12325,1,205,2,1,1,9),_BegemotBridgeStpHelloTime_Type())
begemotBridgeStpHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpHelloTime.setStatus(_A)
if mibBuilder.loadTexts:begemotBridgeStpHelloTime.setUnits(_G)
_BegemotBridgeStpHoldTime_Type=Integer32
_BegemotBridgeStpHoldTime_Object=MibTableColumn
begemotBridgeStpHoldTime=_BegemotBridgeStpHoldTime_Object((1,3,6,1,4,1,12325,1,205,2,1,1,10),_BegemotBridgeStpHoldTime_Type())
begemotBridgeStpHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpHoldTime.setStatus(_A)
if mibBuilder.loadTexts:begemotBridgeStpHoldTime.setUnits(_G)
_BegemotBridgeStpForwardDelay_Type=Timeout
_BegemotBridgeStpForwardDelay_Object=MibTableColumn
begemotBridgeStpForwardDelay=_BegemotBridgeStpForwardDelay_Object((1,3,6,1,4,1,12325,1,205,2,1,1,11),_BegemotBridgeStpForwardDelay_Type())
begemotBridgeStpForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:begemotBridgeStpForwardDelay.setUnits(_G)
class _BegemotBridgeStpBridgeMaxAge_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_BegemotBridgeStpBridgeMaxAge_Type.__name__=_H
_BegemotBridgeStpBridgeMaxAge_Object=MibTableColumn
begemotBridgeStpBridgeMaxAge=_BegemotBridgeStpBridgeMaxAge_Object((1,3,6,1,4,1,12325,1,205,2,1,1,12),_BegemotBridgeStpBridgeMaxAge_Type())
begemotBridgeStpBridgeMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeStpBridgeMaxAge.setStatus(_A)
if mibBuilder.loadTexts:begemotBridgeStpBridgeMaxAge.setUnits(_G)
class _BegemotBridgeStpBridgeHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_BegemotBridgeStpBridgeHelloTime_Type.__name__=_H
_BegemotBridgeStpBridgeHelloTime_Object=MibTableColumn
begemotBridgeStpBridgeHelloTime=_BegemotBridgeStpBridgeHelloTime_Object((1,3,6,1,4,1,12325,1,205,2,1,1,13),_BegemotBridgeStpBridgeHelloTime_Type())
begemotBridgeStpBridgeHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeStpBridgeHelloTime.setStatus(_A)
if mibBuilder.loadTexts:begemotBridgeStpBridgeHelloTime.setUnits(_G)
class _BegemotBridgeStpBridgeForwardDelay_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_BegemotBridgeStpBridgeForwardDelay_Type.__name__=_H
_BegemotBridgeStpBridgeForwardDelay_Object=MibTableColumn
begemotBridgeStpBridgeForwardDelay=_BegemotBridgeStpBridgeForwardDelay_Object((1,3,6,1,4,1,12325,1,205,2,1,1,14),_BegemotBridgeStpBridgeForwardDelay_Type())
begemotBridgeStpBridgeForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeStpBridgeForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:begemotBridgeStpBridgeForwardDelay.setUnits(_G)
class _BegemotBridgeStpVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*(('stpCompatible',0),('rstp',2)))
_BegemotBridgeStpVersion_Type.__name__=_D
_BegemotBridgeStpVersion_Object=MibTableColumn
begemotBridgeStpVersion=_BegemotBridgeStpVersion_Object((1,3,6,1,4,1,12325,1,205,2,1,1,15),_BegemotBridgeStpVersion_Type())
begemotBridgeStpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeStpVersion.setStatus(_A)
class _BegemotBridgeStpTxHoldCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_BegemotBridgeStpTxHoldCount_Type.__name__=_D
_BegemotBridgeStpTxHoldCount_Object=MibTableColumn
begemotBridgeStpTxHoldCount=_BegemotBridgeStpTxHoldCount_Object((1,3,6,1,4,1,12325,1,205,2,1,1,16),_BegemotBridgeStpTxHoldCount_Type())
begemotBridgeStpTxHoldCount.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeStpTxHoldCount.setStatus(_A)
_BegemotBridgeStpPortTable_Object=MibTable
begemotBridgeStpPortTable=_BegemotBridgeStpPortTable_Object((1,3,6,1,4,1,12325,1,205,2,2))
if mibBuilder.loadTexts:begemotBridgeStpPortTable.setStatus(_A)
_BegemotBridgeStpPortEntry_Object=MibTableRow
begemotBridgeStpPortEntry=_BegemotBridgeStpPortEntry_Object((1,3,6,1,4,1,12325,1,205,2,2,1))
begemotBridgeStpPortEntry.setIndexNames((0,_E,_F),(0,_E,_I))
if mibBuilder.loadTexts:begemotBridgeStpPortEntry.setStatus(_A)
class _BegemotBridgeStpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BegemotBridgeStpPort_Type.__name__=_D
_BegemotBridgeStpPort_Object=MibTableColumn
begemotBridgeStpPort=_BegemotBridgeStpPort_Object((1,3,6,1,4,1,12325,1,205,2,2,1,1),_BegemotBridgeStpPort_Type())
begemotBridgeStpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpPort.setStatus(_A)
class _BegemotBridgeStpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BegemotBridgeStpPortPriority_Type.__name__=_D
_BegemotBridgeStpPortPriority_Object=MibTableColumn
begemotBridgeStpPortPriority=_BegemotBridgeStpPortPriority_Object((1,3,6,1,4,1,12325,1,205,2,2,1,2),_BegemotBridgeStpPortPriority_Type())
begemotBridgeStpPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeStpPortPriority.setStatus(_A)
class _BegemotBridgeStpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),('blocking',2),('listening',3),('learning',4),('forwarding',5),('broken',6)))
_BegemotBridgeStpPortState_Type.__name__=_D
_BegemotBridgeStpPortState_Object=MibTableColumn
begemotBridgeStpPortState=_BegemotBridgeStpPortState_Object((1,3,6,1,4,1,12325,1,205,2,2,1,3),_BegemotBridgeStpPortState_Type())
begemotBridgeStpPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpPortState.setStatus(_A)
class _BegemotBridgeStpPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_BegemotBridgeStpPortEnable_Type.__name__=_D
_BegemotBridgeStpPortEnable_Object=MibTableColumn
begemotBridgeStpPortEnable=_BegemotBridgeStpPortEnable_Object((1,3,6,1,4,1,12325,1,205,2,2,1,4),_BegemotBridgeStpPortEnable_Type())
begemotBridgeStpPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeStpPortEnable.setStatus(_A)
class _BegemotBridgeStpPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BegemotBridgeStpPortPathCost_Type.__name__=_D
_BegemotBridgeStpPortPathCost_Object=MibTableColumn
begemotBridgeStpPortPathCost=_BegemotBridgeStpPortPathCost_Object((1,3,6,1,4,1,12325,1,205,2,2,1,5),_BegemotBridgeStpPortPathCost_Type())
begemotBridgeStpPortPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeStpPortPathCost.setStatus(_A)
_BegemotBridgeStpPortDesignatedRoot_Type=BridgeId
_BegemotBridgeStpPortDesignatedRoot_Object=MibTableColumn
begemotBridgeStpPortDesignatedRoot=_BegemotBridgeStpPortDesignatedRoot_Object((1,3,6,1,4,1,12325,1,205,2,2,1,6),_BegemotBridgeStpPortDesignatedRoot_Type())
begemotBridgeStpPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpPortDesignatedRoot.setStatus(_A)
_BegemotBridgeStpPortDesignatedCost_Type=Integer32
_BegemotBridgeStpPortDesignatedCost_Object=MibTableColumn
begemotBridgeStpPortDesignatedCost=_BegemotBridgeStpPortDesignatedCost_Object((1,3,6,1,4,1,12325,1,205,2,2,1,7),_BegemotBridgeStpPortDesignatedCost_Type())
begemotBridgeStpPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpPortDesignatedCost.setStatus(_A)
_BegemotBridgeStpPortDesignatedBridge_Type=BridgeId
_BegemotBridgeStpPortDesignatedBridge_Object=MibTableColumn
begemotBridgeStpPortDesignatedBridge=_BegemotBridgeStpPortDesignatedBridge_Object((1,3,6,1,4,1,12325,1,205,2,2,1,8),_BegemotBridgeStpPortDesignatedBridge_Type())
begemotBridgeStpPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpPortDesignatedBridge.setStatus(_A)
_BegemotBridgeStpPortDesignatedPort_Type=BridgePortId
_BegemotBridgeStpPortDesignatedPort_Object=MibTableColumn
begemotBridgeStpPortDesignatedPort=_BegemotBridgeStpPortDesignatedPort_Object((1,3,6,1,4,1,12325,1,205,2,2,1,9),_BegemotBridgeStpPortDesignatedPort_Type())
begemotBridgeStpPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpPortDesignatedPort.setStatus(_A)
_BegemotBridgeStpPortForwardTransitions_Type=Counter32
_BegemotBridgeStpPortForwardTransitions_Object=MibTableColumn
begemotBridgeStpPortForwardTransitions=_BegemotBridgeStpPortForwardTransitions_Object((1,3,6,1,4,1,12325,1,205,2,2,1,10),_BegemotBridgeStpPortForwardTransitions_Type())
begemotBridgeStpPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpPortForwardTransitions.setStatus(_A)
_BegemotBridgeStpExtPortTable_Object=MibTable
begemotBridgeStpExtPortTable=_BegemotBridgeStpExtPortTable_Object((1,3,6,1,4,1,12325,1,205,2,3))
if mibBuilder.loadTexts:begemotBridgeStpExtPortTable.setStatus(_A)
_BegemotBridgeStpExtPortEntry_Object=MibTableRow
begemotBridgeStpExtPortEntry=_BegemotBridgeStpExtPortEntry_Object((1,3,6,1,4,1,12325,1,205,2,3,1))
if mibBuilder.loadTexts:begemotBridgeStpExtPortEntry.setStatus(_A)
_BegemotBridgeStpPortProtocolMigration_Type=TruthValue
_BegemotBridgeStpPortProtocolMigration_Object=MibTableColumn
begemotBridgeStpPortProtocolMigration=_BegemotBridgeStpPortProtocolMigration_Object((1,3,6,1,4,1,12325,1,205,2,3,1,1),_BegemotBridgeStpPortProtocolMigration_Type())
begemotBridgeStpPortProtocolMigration.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeStpPortProtocolMigration.setStatus(_A)
_BegemotBridgeStpPortAdminEdgePort_Type=TruthValue
_BegemotBridgeStpPortAdminEdgePort_Object=MibTableColumn
begemotBridgeStpPortAdminEdgePort=_BegemotBridgeStpPortAdminEdgePort_Object((1,3,6,1,4,1,12325,1,205,2,3,1,2),_BegemotBridgeStpPortAdminEdgePort_Type())
begemotBridgeStpPortAdminEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeStpPortAdminEdgePort.setStatus(_A)
_BegemotBridgeStpPortOperEdgePort_Type=TruthValue
_BegemotBridgeStpPortOperEdgePort_Object=MibTableColumn
begemotBridgeStpPortOperEdgePort=_BegemotBridgeStpPortOperEdgePort_Object((1,3,6,1,4,1,12325,1,205,2,3,1,3),_BegemotBridgeStpPortOperEdgePort_Type())
begemotBridgeStpPortOperEdgePort.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpPortOperEdgePort.setStatus(_A)
class _BegemotBridgeStpPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_BegemotBridgeStpPortAdminPointToPoint_Type.__name__=_D
_BegemotBridgeStpPortAdminPointToPoint_Object=MibTableColumn
begemotBridgeStpPortAdminPointToPoint=_BegemotBridgeStpPortAdminPointToPoint_Object((1,3,6,1,4,1,12325,1,205,2,3,1,4),_BegemotBridgeStpPortAdminPointToPoint_Type())
begemotBridgeStpPortAdminPointToPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeStpPortAdminPointToPoint.setStatus(_A)
_BegemotBridgeStpPortOperPointToPoint_Type=TruthValue
_BegemotBridgeStpPortOperPointToPoint_Object=MibTableColumn
begemotBridgeStpPortOperPointToPoint=_BegemotBridgeStpPortOperPointToPoint_Object((1,3,6,1,4,1,12325,1,205,2,3,1,5),_BegemotBridgeStpPortOperPointToPoint_Type())
begemotBridgeStpPortOperPointToPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeStpPortOperPointToPoint.setStatus(_A)
class _BegemotBridgeStpPortAdminPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_BegemotBridgeStpPortAdminPathCost_Type.__name__=_D
_BegemotBridgeStpPortAdminPathCost_Object=MibTableColumn
begemotBridgeStpPortAdminPathCost=_BegemotBridgeStpPortAdminPathCost_Object((1,3,6,1,4,1,12325,1,205,2,3,1,6),_BegemotBridgeStpPortAdminPathCost_Type())
begemotBridgeStpPortAdminPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeStpPortAdminPathCost.setStatus(_A)
_BegemotBridgeTp_ObjectIdentity=ObjectIdentity
begemotBridgeTp=_BegemotBridgeTp_ObjectIdentity((1,3,6,1,4,1,12325,1,205,3))
_BegemotBridgeTpTable_Object=MibTable
begemotBridgeTpTable=_BegemotBridgeTpTable_Object((1,3,6,1,4,1,12325,1,205,3,1))
if mibBuilder.loadTexts:begemotBridgeTpTable.setStatus(_A)
_BegemotBridgeTpEntry_Object=MibTableRow
begemotBridgeTpEntry=_BegemotBridgeTpEntry_Object((1,3,6,1,4,1,12325,1,205,3,1,1))
if mibBuilder.loadTexts:begemotBridgeTpEntry.setStatus(_A)
_BegemotBridgeTpLearnedEntryDiscards_Type=Counter32
_BegemotBridgeTpLearnedEntryDiscards_Object=MibTableColumn
begemotBridgeTpLearnedEntryDiscards=_BegemotBridgeTpLearnedEntryDiscards_Object((1,3,6,1,4,1,12325,1,205,3,1,1,1),_BegemotBridgeTpLearnedEntryDiscards_Type())
begemotBridgeTpLearnedEntryDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeTpLearnedEntryDiscards.setStatus(_A)
class _BegemotBridgeTpAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_BegemotBridgeTpAgingTime_Type.__name__=_D
_BegemotBridgeTpAgingTime_Object=MibTableColumn
begemotBridgeTpAgingTime=_BegemotBridgeTpAgingTime_Object((1,3,6,1,4,1,12325,1,205,3,1,1,2),_BegemotBridgeTpAgingTime_Type())
begemotBridgeTpAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeTpAgingTime.setStatus(_A)
if mibBuilder.loadTexts:begemotBridgeTpAgingTime.setUnits(_L)
class _BegemotBridgeTpMaxAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_BegemotBridgeTpMaxAddresses_Type.__name__=_D
_BegemotBridgeTpMaxAddresses_Object=MibTableColumn
begemotBridgeTpMaxAddresses=_BegemotBridgeTpMaxAddresses_Object((1,3,6,1,4,1,12325,1,205,3,1,1,3),_BegemotBridgeTpMaxAddresses_Type())
begemotBridgeTpMaxAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeTpMaxAddresses.setStatus(_A)
_BegemotBridgeTpFdbTable_Object=MibTable
begemotBridgeTpFdbTable=_BegemotBridgeTpFdbTable_Object((1,3,6,1,4,1,12325,1,205,3,2))
if mibBuilder.loadTexts:begemotBridgeTpFdbTable.setStatus(_A)
_BegemotBridgeTpFdbEntry_Object=MibTableRow
begemotBridgeTpFdbEntry=_BegemotBridgeTpFdbEntry_Object((1,3,6,1,4,1,12325,1,205,3,2,1))
begemotBridgeTpFdbEntry.setIndexNames((0,_E,_F),(0,_E,_P))
if mibBuilder.loadTexts:begemotBridgeTpFdbEntry.setStatus(_A)
_BegemotBridgeTpFdbAddress_Type=MacAddress
_BegemotBridgeTpFdbAddress_Object=MibTableColumn
begemotBridgeTpFdbAddress=_BegemotBridgeTpFdbAddress_Object((1,3,6,1,4,1,12325,1,205,3,2,1,1),_BegemotBridgeTpFdbAddress_Type())
begemotBridgeTpFdbAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeTpFdbAddress.setStatus(_A)
_BegemotBridgeTpFdbPort_Type=Integer32
_BegemotBridgeTpFdbPort_Object=MibTableColumn
begemotBridgeTpFdbPort=_BegemotBridgeTpFdbPort_Object((1,3,6,1,4,1,12325,1,205,3,2,1,2),_BegemotBridgeTpFdbPort_Type())
begemotBridgeTpFdbPort.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeTpFdbPort.setStatus(_A)
class _BegemotBridgeTpFdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('invalid',2),('learned',3),('self',4),('mgmt',5)))
_BegemotBridgeTpFdbStatus_Type.__name__=_D
_BegemotBridgeTpFdbStatus_Object=MibTableColumn
begemotBridgeTpFdbStatus=_BegemotBridgeTpFdbStatus_Object((1,3,6,1,4,1,12325,1,205,3,2,1,3),_BegemotBridgeTpFdbStatus_Type())
begemotBridgeTpFdbStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeTpFdbStatus.setStatus(_A)
_BegemotBridgeTpPortTable_Object=MibTable
begemotBridgeTpPortTable=_BegemotBridgeTpPortTable_Object((1,3,6,1,4,1,12325,1,205,3,3))
if mibBuilder.loadTexts:begemotBridgeTpPortTable.setStatus(_A)
_BegemotBridgeTpPortEntry_Object=MibTableRow
begemotBridgeTpPortEntry=_BegemotBridgeTpPortEntry_Object((1,3,6,1,4,1,12325,1,205,3,3,1))
begemotBridgeTpPortEntry.setIndexNames((0,_E,_F),(0,_E,_I))
if mibBuilder.loadTexts:begemotBridgeTpPortEntry.setStatus(_A)
class _BegemotBridgeTpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BegemotBridgeTpPort_Type.__name__=_D
_BegemotBridgeTpPort_Object=MibTableColumn
begemotBridgeTpPort=_BegemotBridgeTpPort_Object((1,3,6,1,4,1,12325,1,205,3,3,1,1),_BegemotBridgeTpPort_Type())
begemotBridgeTpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeTpPort.setStatus(_A)
_BegemotBridgeTpPortMaxInfo_Type=Integer32
_BegemotBridgeTpPortMaxInfo_Object=MibTableColumn
begemotBridgeTpPortMaxInfo=_BegemotBridgeTpPortMaxInfo_Object((1,3,6,1,4,1,12325,1,205,3,3,1,2),_BegemotBridgeTpPortMaxInfo_Type())
begemotBridgeTpPortMaxInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeTpPortMaxInfo.setStatus(_A)
if mibBuilder.loadTexts:begemotBridgeTpPortMaxInfo.setUnits('bytes')
_BegemotBridgeTpPortInFrames_Type=Counter32
_BegemotBridgeTpPortInFrames_Object=MibTableColumn
begemotBridgeTpPortInFrames=_BegemotBridgeTpPortInFrames_Object((1,3,6,1,4,1,12325,1,205,3,3,1,3),_BegemotBridgeTpPortInFrames_Type())
begemotBridgeTpPortInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeTpPortInFrames.setStatus(_A)
if mibBuilder.loadTexts:begemotBridgeTpPortInFrames.setUnits(_M)
_BegemotBridgeTpPortOutFrames_Type=Counter32
_BegemotBridgeTpPortOutFrames_Object=MibTableColumn
begemotBridgeTpPortOutFrames=_BegemotBridgeTpPortOutFrames_Object((1,3,6,1,4,1,12325,1,205,3,3,1,4),_BegemotBridgeTpPortOutFrames_Type())
begemotBridgeTpPortOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeTpPortOutFrames.setStatus(_A)
if mibBuilder.loadTexts:begemotBridgeTpPortOutFrames.setUnits(_M)
_BegemotBridgeTpPortInDiscards_Type=Counter32
_BegemotBridgeTpPortInDiscards_Object=MibTableColumn
begemotBridgeTpPortInDiscards=_BegemotBridgeTpPortInDiscards_Object((1,3,6,1,4,1,12325,1,205,3,3,1,5),_BegemotBridgeTpPortInDiscards_Type())
begemotBridgeTpPortInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotBridgeTpPortInDiscards.setStatus(_A)
if mibBuilder.loadTexts:begemotBridgeTpPortInDiscards.setUnits(_M)
_BegemotBridgePf_ObjectIdentity=ObjectIdentity
begemotBridgePf=_BegemotBridgePf_ObjectIdentity((1,3,6,1,4,1,12325,1,205,4))
_BegemotBridgePfilStatus_Type=TruthValue
_BegemotBridgePfilStatus_Object=MibScalar
begemotBridgePfilStatus=_BegemotBridgePfilStatus_Object((1,3,6,1,4,1,12325,1,205,4,1),_BegemotBridgePfilStatus_Type())
begemotBridgePfilStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgePfilStatus.setStatus(_A)
_BegemotBridgePfilMembers_Type=TruthValue
_BegemotBridgePfilMembers_Object=MibScalar
begemotBridgePfilMembers=_BegemotBridgePfilMembers_Object((1,3,6,1,4,1,12325,1,205,4,2),_BegemotBridgePfilMembers_Type())
begemotBridgePfilMembers.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgePfilMembers.setStatus(_A)
_BegemotBridgePfilIpOnly_Type=TruthValue
_BegemotBridgePfilIpOnly_Object=MibScalar
begemotBridgePfilIpOnly=_BegemotBridgePfilIpOnly_Object((1,3,6,1,4,1,12325,1,205,4,3),_BegemotBridgePfilIpOnly_Type())
begemotBridgePfilIpOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgePfilIpOnly.setStatus(_A)
class _BegemotBridgeLayer2PfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_BegemotBridgeLayer2PfStatus_Type.__name__=_D
_BegemotBridgeLayer2PfStatus_Object=MibScalar
begemotBridgeLayer2PfStatus=_BegemotBridgeLayer2PfStatus_Object((1,3,6,1,4,1,12325,1,205,4,4),_BegemotBridgeLayer2PfStatus_Type())
begemotBridgeLayer2PfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeLayer2PfStatus.setStatus(_A)
_BegemotBridgeConfigObjects_ObjectIdentity=ObjectIdentity
begemotBridgeConfigObjects=_BegemotBridgeConfigObjects_ObjectIdentity((1,3,6,1,4,1,12325,1,205,5))
class _BegemotBridgeDefaultBridgeIf_Type(BridgeIfNameOrEmpty):defaultValue=OctetString('bridge0')
_BegemotBridgeDefaultBridgeIf_Type.__name__=_Q
_BegemotBridgeDefaultBridgeIf_Object=MibScalar
begemotBridgeDefaultBridgeIf=_BegemotBridgeDefaultBridgeIf_Object((1,3,6,1,4,1,12325,1,205,5,1),_BegemotBridgeDefaultBridgeIf_Type())
begemotBridgeDefaultBridgeIf.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeDefaultBridgeIf.setStatus(_A)
class _BegemotBridgeDataUpdate_Type(Timeout):defaultValue=10;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_BegemotBridgeDataUpdate_Type.__name__=_H
_BegemotBridgeDataUpdate_Object=MibScalar
begemotBridgeDataUpdate=_BegemotBridgeDataUpdate_Object((1,3,6,1,4,1,12325,1,205,5,2),_BegemotBridgeDataUpdate_Type())
begemotBridgeDataUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeDataUpdate.setStatus(_A)
if mibBuilder.loadTexts:begemotBridgeDataUpdate.setUnits(_L)
class _BegemotBridgeDataPoll_Type(Timeout):defaultValue=300;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_BegemotBridgeDataPoll_Type.__name__=_H
_BegemotBridgeDataPoll_Object=MibScalar
begemotBridgeDataPoll=_BegemotBridgeDataPoll_Object((1,3,6,1,4,1,12325,1,205,5,3),_BegemotBridgeDataPoll_Type())
begemotBridgeDataPoll.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotBridgeDataPoll.setStatus(_A)
if mibBuilder.loadTexts:begemotBridgeDataPoll.setUnits(_L)
begemotBridgeBaseEntry.registerAugmentions((_E,_R))
begemotBridgeStpEntry.setIndexNames(*begemotBridgeBaseEntry.getIndexNames())
begemotBridgeStpPortEntry.registerAugmentions((_E,_S))
begemotBridgeStpExtPortEntry.setIndexNames(*begemotBridgeStpPortEntry.getIndexNames())
begemotBridgeBaseEntry.registerAugmentions((_E,_T))
begemotBridgeTpEntry.setIndexNames(*begemotBridgeBaseEntry.getIndexNames())
begemotBridgeNewRoot=NotificationType((1,3,6,1,4,1,12325,1,205,0,1))
begemotBridgeNewRoot.setObjects((_E,_F))
if mibBuilder.loadTexts:begemotBridgeNewRoot.setStatus(_A)
begemotBridgeTopologyChange=NotificationType((1,3,6,1,4,1,12325,1,205,0,2))
begemotBridgeTopologyChange.setObjects((_E,_F))
if mibBuilder.loadTexts:begemotBridgeTopologyChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'BridgeIfName':BridgeIfName,_Q:BridgeIfNameOrEmpty,'BridgePortId':BridgePortId,'begemotBridge':begemotBridge,'begemotBridgeNotifications':begemotBridgeNotifications,'begemotBridgeNewRoot':begemotBridgeNewRoot,'begemotBridgeTopologyChange':begemotBridgeTopologyChange,'begemotBridgeBase':begemotBridgeBase,'begemotBridgeBaseTable':begemotBridgeBaseTable,'begemotBridgeBaseEntry':begemotBridgeBaseEntry,_F:begemotBridgeBaseName,'begemotBridgeBaseAddress':begemotBridgeBaseAddress,'begemotBridgeBaseNumPorts':begemotBridgeBaseNumPorts,'begemotBridgeBaseType':begemotBridgeBaseType,'begemotBridgeBaseStatus':begemotBridgeBaseStatus,'begemotBridgeBasePortTable':begemotBridgeBasePortTable,'begemotBridgeBasePortEntry':begemotBridgeBasePortEntry,'begemotBridgeBasePort':begemotBridgeBasePort,_I:begemotBridgeBasePortIfIndex,'begemotBridgeBaseSpanEnabled':begemotBridgeBaseSpanEnabled,'begemotBridgeBasePortDelayExceededDiscards':begemotBridgeBasePortDelayExceededDiscards,'begemotBridgeBasePortMtuExceededDiscards':begemotBridgeBasePortMtuExceededDiscards,'begemotBridgeBasePortStatus':begemotBridgeBasePortStatus,'begemotBridgeBasePortPrivate':begemotBridgeBasePortPrivate,'begemotBridgeStp':begemotBridgeStp,'begemotBridgeStpTable':begemotBridgeStpTable,_R:begemotBridgeStpEntry,'begemotBridgeStpProtocolSpecification':begemotBridgeStpProtocolSpecification,'begemotBridgeStpPriority':begemotBridgeStpPriority,'begemotBridgeStpTimeSinceTopologyChange':begemotBridgeStpTimeSinceTopologyChange,'begemotBridgeStpTopChanges':begemotBridgeStpTopChanges,'begemotBridgeStpDesignatedRoot':begemotBridgeStpDesignatedRoot,'begemotBridgeStpRootCost':begemotBridgeStpRootCost,'begemotBridgeStpRootPort':begemotBridgeStpRootPort,'begemotBridgeStpMaxAge':begemotBridgeStpMaxAge,'begemotBridgeStpHelloTime':begemotBridgeStpHelloTime,'begemotBridgeStpHoldTime':begemotBridgeStpHoldTime,'begemotBridgeStpForwardDelay':begemotBridgeStpForwardDelay,'begemotBridgeStpBridgeMaxAge':begemotBridgeStpBridgeMaxAge,'begemotBridgeStpBridgeHelloTime':begemotBridgeStpBridgeHelloTime,'begemotBridgeStpBridgeForwardDelay':begemotBridgeStpBridgeForwardDelay,'begemotBridgeStpVersion':begemotBridgeStpVersion,'begemotBridgeStpTxHoldCount':begemotBridgeStpTxHoldCount,'begemotBridgeStpPortTable':begemotBridgeStpPortTable,'begemotBridgeStpPortEntry':begemotBridgeStpPortEntry,'begemotBridgeStpPort':begemotBridgeStpPort,'begemotBridgeStpPortPriority':begemotBridgeStpPortPriority,'begemotBridgeStpPortState':begemotBridgeStpPortState,'begemotBridgeStpPortEnable':begemotBridgeStpPortEnable,'begemotBridgeStpPortPathCost':begemotBridgeStpPortPathCost,'begemotBridgeStpPortDesignatedRoot':begemotBridgeStpPortDesignatedRoot,'begemotBridgeStpPortDesignatedCost':begemotBridgeStpPortDesignatedCost,'begemotBridgeStpPortDesignatedBridge':begemotBridgeStpPortDesignatedBridge,'begemotBridgeStpPortDesignatedPort':begemotBridgeStpPortDesignatedPort,'begemotBridgeStpPortForwardTransitions':begemotBridgeStpPortForwardTransitions,'begemotBridgeStpExtPortTable':begemotBridgeStpExtPortTable,_S:begemotBridgeStpExtPortEntry,'begemotBridgeStpPortProtocolMigration':begemotBridgeStpPortProtocolMigration,'begemotBridgeStpPortAdminEdgePort':begemotBridgeStpPortAdminEdgePort,'begemotBridgeStpPortOperEdgePort':begemotBridgeStpPortOperEdgePort,'begemotBridgeStpPortAdminPointToPoint':begemotBridgeStpPortAdminPointToPoint,'begemotBridgeStpPortOperPointToPoint':begemotBridgeStpPortOperPointToPoint,'begemotBridgeStpPortAdminPathCost':begemotBridgeStpPortAdminPathCost,'begemotBridgeTp':begemotBridgeTp,'begemotBridgeTpTable':begemotBridgeTpTable,_T:begemotBridgeTpEntry,'begemotBridgeTpLearnedEntryDiscards':begemotBridgeTpLearnedEntryDiscards,'begemotBridgeTpAgingTime':begemotBridgeTpAgingTime,'begemotBridgeTpMaxAddresses':begemotBridgeTpMaxAddresses,'begemotBridgeTpFdbTable':begemotBridgeTpFdbTable,'begemotBridgeTpFdbEntry':begemotBridgeTpFdbEntry,_P:begemotBridgeTpFdbAddress,'begemotBridgeTpFdbPort':begemotBridgeTpFdbPort,'begemotBridgeTpFdbStatus':begemotBridgeTpFdbStatus,'begemotBridgeTpPortTable':begemotBridgeTpPortTable,'begemotBridgeTpPortEntry':begemotBridgeTpPortEntry,'begemotBridgeTpPort':begemotBridgeTpPort,'begemotBridgeTpPortMaxInfo':begemotBridgeTpPortMaxInfo,'begemotBridgeTpPortInFrames':begemotBridgeTpPortInFrames,'begemotBridgeTpPortOutFrames':begemotBridgeTpPortOutFrames,'begemotBridgeTpPortInDiscards':begemotBridgeTpPortInDiscards,'begemotBridgePf':begemotBridgePf,'begemotBridgePfilStatus':begemotBridgePfilStatus,'begemotBridgePfilMembers':begemotBridgePfilMembers,'begemotBridgePfilIpOnly':begemotBridgePfilIpOnly,'begemotBridgeLayer2PfStatus':begemotBridgeLayer2PfStatus,'begemotBridgeConfigObjects':begemotBridgeConfigObjects,'begemotBridgeDefaultBridgeIf':begemotBridgeDefaultBridgeIf,'begemotBridgeDataUpdate':begemotBridgeDataUpdate,'begemotBridgeDataPoll':begemotBridgeDataPoll})