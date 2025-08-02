_P='hm2AgentDot1qMrpMsrpIntf'
_O='hm2AgentDot1qMsrpReservationDirection'
_N='hm2AgentDot1qMsrpReservationStreamId'
_M='hm2AgentDot1qMsrpStreamIndex'
_L='VlanId'
_K='bits per second'
_J='hm2AgentDot1qFqtssTrafficClass'
_I='Integer32'
_H='TruthValue'
_G='not-accessible'
_F='hm2AgentDot1qMsrpPort'
_E='Unsigned32'
_D='read-write'
_C='HM2-PLATFORM-MSRP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId')
hm2AgentDot1qMrpMxrp,=mibBuilder.importSymbols('HM2-PLATFORM-MRP-MIB','hm2AgentDot1qMrpMxrp')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_H)
hm2PlatformMSRP=ModuleIdentity((1,3,6,1,4,1,248,12,60,2,3))
if mibBuilder.loadTexts:hm2PlatformMSRP.setRevisions(('2013-04-10 00:00',))
class Hm2AgentDot1qPriorityValue(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class Hm2AgentDot1qMsrpStreamRankValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('emergency',0),('nonEmergency',1)))
class Hm2AgentDot1qMsrpStreamIdValue(TextualConvention,OctetString):status=_A;displayHint='1x:1x:1x:1x:1x:1x.1x:1x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class Hm2AgentDot1qMsrpReservationDirectionValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('talkerRegistrations',0),('listenerRegistrations',1)))
class Hm2AgentDot1qMsrpReservationDeclarationTypeValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('talkerAdvertise',0),('talkerFailed',1),('listenerAskingFailed',2),('listenerReady',3),('listenerReadyFailed',4)))
class Hm2AgentDot1qMsrpReservationFailureCodeValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*(('noFailure',0),('insufficientBandwidth',1),('insufficientResources',2),('insufficientTrafficClassBandwidth',3),('streamIDInUse',4),('streamDestinationAddressInUse',5),('streamPreemptedByHigherRank',6),('latencyHasChanged',7),('egressPortNotAVBCapable',8),('useDifferentDestinationAddress',9),('outOfMSRPResources',10),('outOfMMRPResources',11),('cannotStoreDestinationAddress',12),('priorityIsNoAnSRCLass',13),('maxFrameSizeTooLarge',14),('maxFanInPortsLimitReached',15),('firstValueChangedForStreamID',16),('vlanBlockedOnEgress',17),('vlanTaggingDisabledOnEgress',18),('srClassPriorityMismatch',19)))
class Hm2AgentDot1qFqtssTrafficClassValue(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class Hm2AgentDot1qFqtssDeltaBandwidthValue(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
class Hm2AgentDot1qFtqssTxSelectionAlgorithmIDValue(TextualConvention,Unsigned32):status=_A;displayHint='d'
_Hm2AgentDot1qMsrp_ObjectIdentity=ObjectIdentity
hm2AgentDot1qMsrp=_Hm2AgentDot1qMsrp_ObjectIdentity((1,3,6,1,4,1,248,12,60,2,3,1))
_Hm2AgentDot1qPortMsrpTable_Object=MibTable
hm2AgentDot1qPortMsrpTable=_Hm2AgentDot1qPortMsrpTable_Object((1,3,6,1,4,1,248,12,60,2,3,1,1))
if mibBuilder.loadTexts:hm2AgentDot1qPortMsrpTable.setStatus(_A)
_Hm2AgentDot1qPortMsrpEntry_Object=MibTableRow
hm2AgentDot1qPortMsrpEntry=_Hm2AgentDot1qPortMsrpEntry_Object((1,3,6,1,4,1,248,12,60,2,3,1,1,1))
hm2AgentDot1qPortMsrpEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:hm2AgentDot1qPortMsrpEntry.setStatus(_A)
class _Hm2AgentDot1qMsrpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Hm2AgentDot1qMsrpPort_Type.__name__=_I
_Hm2AgentDot1qMsrpPort_Object=MibTableColumn
hm2AgentDot1qMsrpPort=_Hm2AgentDot1qMsrpPort_Object((1,3,6,1,4,1,248,12,60,2,3,1,1,1,1),_Hm2AgentDot1qMsrpPort_Type())
hm2AgentDot1qMsrpPort.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpPort.setStatus(_A)
class _Hm2AgentDot1qPortMsrpEnabledStatus_Type(TruthValue):defaultValue=2
_Hm2AgentDot1qPortMsrpEnabledStatus_Type.__name__=_H
_Hm2AgentDot1qPortMsrpEnabledStatus_Object=MibTableColumn
hm2AgentDot1qPortMsrpEnabledStatus=_Hm2AgentDot1qPortMsrpEnabledStatus_Object((1,3,6,1,4,1,248,12,60,2,3,1,1,1,2),_Hm2AgentDot1qPortMsrpEnabledStatus_Type())
hm2AgentDot1qPortMsrpEnabledStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2AgentDot1qPortMsrpEnabledStatus.setStatus(_A)
_Hm2AgentDot1qPortMsrpFailedRegistrations_Type=Counter64
_Hm2AgentDot1qPortMsrpFailedRegistrations_Object=MibTableColumn
hm2AgentDot1qPortMsrpFailedRegistrations=_Hm2AgentDot1qPortMsrpFailedRegistrations_Object((1,3,6,1,4,1,248,12,60,2,3,1,1,1,3),_Hm2AgentDot1qPortMsrpFailedRegistrations_Type())
hm2AgentDot1qPortMsrpFailedRegistrations.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qPortMsrpFailedRegistrations.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentDot1qPortMsrpFailedRegistrations.setUnits('failed MSRP registrations')
_Hm2AgentDot1qPortMsrpLastPduOrigin_Type=MacAddress
_Hm2AgentDot1qPortMsrpLastPduOrigin_Object=MibTableColumn
hm2AgentDot1qPortMsrpLastPduOrigin=_Hm2AgentDot1qPortMsrpLastPduOrigin_Object((1,3,6,1,4,1,248,12,60,2,3,1,1,1,4),_Hm2AgentDot1qPortMsrpLastPduOrigin_Type())
hm2AgentDot1qPortMsrpLastPduOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qPortMsrpLastPduOrigin.setStatus(_A)
class _Hm2AgentDot1qPortMsrpPvid_Type(VlanId):defaultValue=2
_Hm2AgentDot1qPortMsrpPvid_Type.__name__=_L
_Hm2AgentDot1qPortMsrpPvid_Object=MibTableColumn
hm2AgentDot1qPortMsrpPvid=_Hm2AgentDot1qPortMsrpPvid_Object((1,3,6,1,4,1,248,12,60,2,3,1,1,1,5),_Hm2AgentDot1qPortMsrpPvid_Type())
hm2AgentDot1qPortMsrpPvid.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2AgentDot1qPortMsrpPvid.setStatus(_A)
class _Hm2AgentDot1qBridgeMsrpEnabledStatus_Type(TruthValue):defaultValue=2
_Hm2AgentDot1qBridgeMsrpEnabledStatus_Type.__name__=_H
_Hm2AgentDot1qBridgeMsrpEnabledStatus_Object=MibScalar
hm2AgentDot1qBridgeMsrpEnabledStatus=_Hm2AgentDot1qBridgeMsrpEnabledStatus_Object((1,3,6,1,4,1,248,12,60,2,3,1,2),_Hm2AgentDot1qBridgeMsrpEnabledStatus_Type())
hm2AgentDot1qBridgeMsrpEnabledStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2AgentDot1qBridgeMsrpEnabledStatus.setStatus(_A)
class _Hm2AgentDot1qBridgeMsrpTalkerPruning_Type(TruthValue):defaultValue=2
_Hm2AgentDot1qBridgeMsrpTalkerPruning_Type.__name__=_H
_Hm2AgentDot1qBridgeMsrpTalkerPruning_Object=MibScalar
hm2AgentDot1qBridgeMsrpTalkerPruning=_Hm2AgentDot1qBridgeMsrpTalkerPruning_Object((1,3,6,1,4,1,248,12,60,2,3,1,3),_Hm2AgentDot1qBridgeMsrpTalkerPruning_Type())
hm2AgentDot1qBridgeMsrpTalkerPruning.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2AgentDot1qBridgeMsrpTalkerPruning.setStatus(_A)
class _Hm2AgentDot1qBridgeMsrpMaxFanInPorts_Type(Unsigned32):defaultValue=0
_Hm2AgentDot1qBridgeMsrpMaxFanInPorts_Type.__name__=_E
_Hm2AgentDot1qBridgeMsrpMaxFanInPorts_Object=MibScalar
hm2AgentDot1qBridgeMsrpMaxFanInPorts=_Hm2AgentDot1qBridgeMsrpMaxFanInPorts_Object((1,3,6,1,4,1,248,12,60,2,3,1,4),_Hm2AgentDot1qBridgeMsrpMaxFanInPorts_Type())
hm2AgentDot1qBridgeMsrpMaxFanInPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2AgentDot1qBridgeMsrpMaxFanInPorts.setStatus(_A)
class _Hm2AgentDot1qBridgeMsrpBoundaryPropagate_Type(TruthValue):defaultValue=2
_Hm2AgentDot1qBridgeMsrpBoundaryPropagate_Type.__name__=_H
_Hm2AgentDot1qBridgeMsrpBoundaryPropagate_Object=MibScalar
hm2AgentDot1qBridgeMsrpBoundaryPropagate=_Hm2AgentDot1qBridgeMsrpBoundaryPropagate_Object((1,3,6,1,4,1,248,12,60,2,3,1,6),_Hm2AgentDot1qBridgeMsrpBoundaryPropagate_Type())
hm2AgentDot1qBridgeMsrpBoundaryPropagate.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2AgentDot1qBridgeMsrpBoundaryPropagate.setStatus(_A)
_Hm2AgentDot1qMsrpStreamTable_Object=MibTable
hm2AgentDot1qMsrpStreamTable=_Hm2AgentDot1qMsrpStreamTable_Object((1,3,6,1,4,1,248,12,60,2,3,1,7))
if mibBuilder.loadTexts:hm2AgentDot1qMsrpStreamTable.setStatus(_A)
_Hm2AgentDot1qMsrpStreamEntry_Object=MibTableRow
hm2AgentDot1qMsrpStreamEntry=_Hm2AgentDot1qMsrpStreamEntry_Object((1,3,6,1,4,1,248,12,60,2,3,1,7,1))
hm2AgentDot1qMsrpStreamEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:hm2AgentDot1qMsrpStreamEntry.setStatus(_A)
class _Hm2AgentDot1qMsrpStreamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hm2AgentDot1qMsrpStreamIndex_Type.__name__=_I
_Hm2AgentDot1qMsrpStreamIndex_Object=MibTableColumn
hm2AgentDot1qMsrpStreamIndex=_Hm2AgentDot1qMsrpStreamIndex_Object((1,3,6,1,4,1,248,12,60,2,3,1,7,1,1),_Hm2AgentDot1qMsrpStreamIndex_Type())
hm2AgentDot1qMsrpStreamIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpStreamIndex.setStatus(_A)
_Hm2AgentDot1qMsrpStreamID_Type=Hm2AgentDot1qMsrpStreamIdValue
_Hm2AgentDot1qMsrpStreamID_Object=MibTableColumn
hm2AgentDot1qMsrpStreamID=_Hm2AgentDot1qMsrpStreamID_Object((1,3,6,1,4,1,248,12,60,2,3,1,7,1,2),_Hm2AgentDot1qMsrpStreamID_Type())
hm2AgentDot1qMsrpStreamID.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpStreamID.setStatus(_A)
_Hm2AgentDot1qMsrpStreamDestMacAddr_Type=MacAddress
_Hm2AgentDot1qMsrpStreamDestMacAddr_Object=MibTableColumn
hm2AgentDot1qMsrpStreamDestMacAddr=_Hm2AgentDot1qMsrpStreamDestMacAddr_Object((1,3,6,1,4,1,248,12,60,2,3,1,7,1,3),_Hm2AgentDot1qMsrpStreamDestMacAddr_Type())
hm2AgentDot1qMsrpStreamDestMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpStreamDestMacAddr.setStatus(_A)
_Hm2AgentDot1qMsrpStreamVlanId_Type=Integer32
_Hm2AgentDot1qMsrpStreamVlanId_Object=MibTableColumn
hm2AgentDot1qMsrpStreamVlanId=_Hm2AgentDot1qMsrpStreamVlanId_Object((1,3,6,1,4,1,248,12,60,2,3,1,7,1,4),_Hm2AgentDot1qMsrpStreamVlanId_Type())
hm2AgentDot1qMsrpStreamVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpStreamVlanId.setStatus(_A)
class _Hm2AgentDot1qMsrpStreamTspecMaxFrameSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hm2AgentDot1qMsrpStreamTspecMaxFrameSize_Type.__name__=_E
_Hm2AgentDot1qMsrpStreamTspecMaxFrameSize_Object=MibTableColumn
hm2AgentDot1qMsrpStreamTspecMaxFrameSize=_Hm2AgentDot1qMsrpStreamTspecMaxFrameSize_Object((1,3,6,1,4,1,248,12,60,2,3,1,7,1,5),_Hm2AgentDot1qMsrpStreamTspecMaxFrameSize_Type())
hm2AgentDot1qMsrpStreamTspecMaxFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpStreamTspecMaxFrameSize.setStatus(_A)
class _Hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames_Type.__name__=_E
_Hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames_Object=MibTableColumn
hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames=_Hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames_Object((1,3,6,1,4,1,248,12,60,2,3,1,7,1,6),_Hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames_Type())
hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames.setStatus(_A)
_Hm2AgentDot1qMsrpStreamDataFramePriority_Type=Hm2AgentDot1qPriorityValue
_Hm2AgentDot1qMsrpStreamDataFramePriority_Object=MibTableColumn
hm2AgentDot1qMsrpStreamDataFramePriority=_Hm2AgentDot1qMsrpStreamDataFramePriority_Object((1,3,6,1,4,1,248,12,60,2,3,1,7,1,7),_Hm2AgentDot1qMsrpStreamDataFramePriority_Type())
hm2AgentDot1qMsrpStreamDataFramePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpStreamDataFramePriority.setStatus(_A)
_Hm2AgentDot1qMsrpStreamRank_Type=Hm2AgentDot1qMsrpStreamRankValue
_Hm2AgentDot1qMsrpStreamRank_Object=MibTableColumn
hm2AgentDot1qMsrpStreamRank=_Hm2AgentDot1qMsrpStreamRank_Object((1,3,6,1,4,1,248,12,60,2,3,1,7,1,8),_Hm2AgentDot1qMsrpStreamRank_Type())
hm2AgentDot1qMsrpStreamRank.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpStreamRank.setStatus(_A)
_Hm2AgentDot1qMsrpReservationTable_Object=MibTable
hm2AgentDot1qMsrpReservationTable=_Hm2AgentDot1qMsrpReservationTable_Object((1,3,6,1,4,1,248,12,60,2,3,1,8))
if mibBuilder.loadTexts:hm2AgentDot1qMsrpReservationTable.setStatus(_A)
_Hm2AgentDot1qMsrpReservationEntry_Object=MibTableRow
hm2AgentDot1qMsrpReservationEntry=_Hm2AgentDot1qMsrpReservationEntry_Object((1,3,6,1,4,1,248,12,60,2,3,1,8,1))
hm2AgentDot1qMsrpReservationEntry.setIndexNames((0,_C,_N),(0,_C,_O),(0,_C,_F))
if mibBuilder.loadTexts:hm2AgentDot1qMsrpReservationEntry.setStatus(_A)
_Hm2AgentDot1qMsrpReservationStreamId_Type=Hm2AgentDot1qMsrpStreamIdValue
_Hm2AgentDot1qMsrpReservationStreamId_Object=MibTableColumn
hm2AgentDot1qMsrpReservationStreamId=_Hm2AgentDot1qMsrpReservationStreamId_Object((1,3,6,1,4,1,248,12,60,2,3,1,8,1,1),_Hm2AgentDot1qMsrpReservationStreamId_Type())
hm2AgentDot1qMsrpReservationStreamId.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpReservationStreamId.setStatus(_A)
_Hm2AgentDot1qMsrpReservationDirection_Type=Hm2AgentDot1qMsrpReservationDirectionValue
_Hm2AgentDot1qMsrpReservationDirection_Object=MibTableColumn
hm2AgentDot1qMsrpReservationDirection=_Hm2AgentDot1qMsrpReservationDirection_Object((1,3,6,1,4,1,248,12,60,2,3,1,8,1,2),_Hm2AgentDot1qMsrpReservationDirection_Type())
hm2AgentDot1qMsrpReservationDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpReservationDirection.setStatus(_A)
_Hm2AgentDot1qMsrpReservationDeclarationType_Type=Hm2AgentDot1qMsrpReservationDeclarationTypeValue
_Hm2AgentDot1qMsrpReservationDeclarationType_Object=MibTableColumn
hm2AgentDot1qMsrpReservationDeclarationType=_Hm2AgentDot1qMsrpReservationDeclarationType_Object((1,3,6,1,4,1,248,12,60,2,3,1,8,1,3),_Hm2AgentDot1qMsrpReservationDeclarationType_Type())
hm2AgentDot1qMsrpReservationDeclarationType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpReservationDeclarationType.setStatus(_A)
_Hm2AgentDot1qMsrpReservationAccumulatedLatency_Type=Unsigned32
_Hm2AgentDot1qMsrpReservationAccumulatedLatency_Object=MibTableColumn
hm2AgentDot1qMsrpReservationAccumulatedLatency=_Hm2AgentDot1qMsrpReservationAccumulatedLatency_Object((1,3,6,1,4,1,248,12,60,2,3,1,8,1,4),_Hm2AgentDot1qMsrpReservationAccumulatedLatency_Type())
hm2AgentDot1qMsrpReservationAccumulatedLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpReservationAccumulatedLatency.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpReservationAccumulatedLatency.setUnits('nano-seconds')
_Hm2AgentDot1qMsrpReservationFailureBridgeId_Type=BridgeId
_Hm2AgentDot1qMsrpReservationFailureBridgeId_Object=MibTableColumn
hm2AgentDot1qMsrpReservationFailureBridgeId=_Hm2AgentDot1qMsrpReservationFailureBridgeId_Object((1,3,6,1,4,1,248,12,60,2,3,1,8,1,5),_Hm2AgentDot1qMsrpReservationFailureBridgeId_Type())
hm2AgentDot1qMsrpReservationFailureBridgeId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpReservationFailureBridgeId.setStatus(_A)
_Hm2AgentDot1qMsrpReservationFailureCode_Type=Hm2AgentDot1qMsrpReservationFailureCodeValue
_Hm2AgentDot1qMsrpReservationFailureCode_Object=MibTableColumn
hm2AgentDot1qMsrpReservationFailureCode=_Hm2AgentDot1qMsrpReservationFailureCode_Object((1,3,6,1,4,1,248,12,60,2,3,1,8,1,6),_Hm2AgentDot1qMsrpReservationFailureCode_Type())
hm2AgentDot1qMsrpReservationFailureCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpReservationFailureCode.setStatus(_A)
_Hm2AgentDot1qMsrpReservationDroppedStreamFrames_Type=Counter64
_Hm2AgentDot1qMsrpReservationDroppedStreamFrames_Object=MibTableColumn
hm2AgentDot1qMsrpReservationDroppedStreamFrames=_Hm2AgentDot1qMsrpReservationDroppedStreamFrames_Object((1,3,6,1,4,1,248,12,60,2,3,1,8,1,7),_Hm2AgentDot1qMsrpReservationDroppedStreamFrames_Type())
hm2AgentDot1qMsrpReservationDroppedStreamFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpReservationDroppedStreamFrames.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpReservationDroppedStreamFrames.setUnits('frames')
_Hm2AgentDot1qMsrpReservationStreamAge_Type=Unsigned32
_Hm2AgentDot1qMsrpReservationStreamAge_Object=MibTableColumn
hm2AgentDot1qMsrpReservationStreamAge=_Hm2AgentDot1qMsrpReservationStreamAge_Object((1,3,6,1,4,1,248,12,60,2,3,1,8,1,8),_Hm2AgentDot1qMsrpReservationStreamAge_Type())
hm2AgentDot1qMsrpReservationStreamAge.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpReservationStreamAge.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentDot1qMsrpReservationStreamAge.setUnits('seconds')
_Hm2AgentDot1qMrpMsrpStats_ObjectIdentity=ObjectIdentity
hm2AgentDot1qMrpMsrpStats=_Hm2AgentDot1qMrpMsrpStats_ObjectIdentity((1,3,6,1,4,1,248,12,60,2,3,2))
_Hm2AgentDot1qMrpMsrpPktTx_Type=Counter32
_Hm2AgentDot1qMrpMsrpPktTx_Object=MibScalar
hm2AgentDot1qMrpMsrpPktTx=_Hm2AgentDot1qMrpMsrpPktTx_Object((1,3,6,1,4,1,248,12,60,2,3,2,1),_Hm2AgentDot1qMrpMsrpPktTx_Type())
hm2AgentDot1qMrpMsrpPktTx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMsrpPktTx.setStatus(_A)
_Hm2AgentDot1qMrpMsrpPktRx_Type=Counter32
_Hm2AgentDot1qMrpMsrpPktRx_Object=MibScalar
hm2AgentDot1qMrpMsrpPktRx=_Hm2AgentDot1qMrpMsrpPktRx_Object((1,3,6,1,4,1,248,12,60,2,3,2,2),_Hm2AgentDot1qMrpMsrpPktRx_Type())
hm2AgentDot1qMrpMsrpPktRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMsrpPktRx.setStatus(_A)
_Hm2AgentDot1qMrpMsrpPktRxBadHeader_Type=Counter32
_Hm2AgentDot1qMrpMsrpPktRxBadHeader_Object=MibScalar
hm2AgentDot1qMrpMsrpPktRxBadHeader=_Hm2AgentDot1qMrpMsrpPktRxBadHeader_Object((1,3,6,1,4,1,248,12,60,2,3,2,3),_Hm2AgentDot1qMrpMsrpPktRxBadHeader_Type())
hm2AgentDot1qMrpMsrpPktRxBadHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMsrpPktRxBadHeader.setStatus(_A)
_Hm2AgentDot1qMrpMsrpPktRxBadFormat_Type=Counter32
_Hm2AgentDot1qMrpMsrpPktRxBadFormat_Object=MibScalar
hm2AgentDot1qMrpMsrpPktRxBadFormat=_Hm2AgentDot1qMrpMsrpPktRxBadFormat_Object((1,3,6,1,4,1,248,12,60,2,3,2,4),_Hm2AgentDot1qMrpMsrpPktRxBadFormat_Type())
hm2AgentDot1qMrpMsrpPktRxBadFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMsrpPktRxBadFormat.setStatus(_A)
_Hm2AgentDot1qMrpMsrpPktTxFailure_Type=Counter32
_Hm2AgentDot1qMrpMsrpPktTxFailure_Object=MibScalar
hm2AgentDot1qMrpMsrpPktTxFailure=_Hm2AgentDot1qMrpMsrpPktTxFailure_Object((1,3,6,1,4,1,248,12,60,2,3,2,5),_Hm2AgentDot1qMrpMsrpPktTxFailure_Type())
hm2AgentDot1qMrpMsrpPktTxFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMsrpPktTxFailure.setStatus(_A)
_Hm2AgentDot1qMrpMsrpStatsTable_Object=MibTable
hm2AgentDot1qMrpMsrpStatsTable=_Hm2AgentDot1qMrpMsrpStatsTable_Object((1,3,6,1,4,1,248,12,60,2,3,2,6))
if mibBuilder.loadTexts:hm2AgentDot1qMrpMsrpStatsTable.setStatus(_A)
_Hm2AgentDot1qMrpMsrpStatsEntry_Object=MibTableRow
hm2AgentDot1qMrpMsrpStatsEntry=_Hm2AgentDot1qMrpMsrpStatsEntry_Object((1,3,6,1,4,1,248,12,60,2,3,2,6,1))
hm2AgentDot1qMrpMsrpStatsEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:hm2AgentDot1qMrpMsrpStatsEntry.setStatus(_A)
class _Hm2AgentDot1qMrpMsrpIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Hm2AgentDot1qMrpMsrpIntf_Type.__name__=_I
_Hm2AgentDot1qMrpMsrpIntf_Object=MibTableColumn
hm2AgentDot1qMrpMsrpIntf=_Hm2AgentDot1qMrpMsrpIntf_Object((1,3,6,1,4,1,248,12,60,2,3,2,6,1,1),_Hm2AgentDot1qMrpMsrpIntf_Type())
hm2AgentDot1qMrpMsrpIntf.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMsrpIntf.setStatus(_A)
_Hm2AgentDot1qMrpMsrpPortPktTx_Type=Counter32
_Hm2AgentDot1qMrpMsrpPortPktTx_Object=MibTableColumn
hm2AgentDot1qMrpMsrpPortPktTx=_Hm2AgentDot1qMrpMsrpPortPktTx_Object((1,3,6,1,4,1,248,12,60,2,3,2,6,1,2),_Hm2AgentDot1qMrpMsrpPortPktTx_Type())
hm2AgentDot1qMrpMsrpPortPktTx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMsrpPortPktTx.setStatus(_A)
_Hm2AgentDot1qMrpMsrpPortPktRx_Type=Counter32
_Hm2AgentDot1qMrpMsrpPortPktRx_Object=MibTableColumn
hm2AgentDot1qMrpMsrpPortPktRx=_Hm2AgentDot1qMrpMsrpPortPktRx_Object((1,3,6,1,4,1,248,12,60,2,3,2,6,1,3),_Hm2AgentDot1qMrpMsrpPortPktRx_Type())
hm2AgentDot1qMrpMsrpPortPktRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMsrpPortPktRx.setStatus(_A)
_Hm2AgentDot1qMrpMsrpPortPktRxBadHeader_Type=Counter32
_Hm2AgentDot1qMrpMsrpPortPktRxBadHeader_Object=MibTableColumn
hm2AgentDot1qMrpMsrpPortPktRxBadHeader=_Hm2AgentDot1qMrpMsrpPortPktRxBadHeader_Object((1,3,6,1,4,1,248,12,60,2,3,2,6,1,4),_Hm2AgentDot1qMrpMsrpPortPktRxBadHeader_Type())
hm2AgentDot1qMrpMsrpPortPktRxBadHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMsrpPortPktRxBadHeader.setStatus(_A)
_Hm2AgentDot1qMrpMsrpPortPktRxBadFormat_Type=Counter32
_Hm2AgentDot1qMrpMsrpPortPktRxBadFormat_Object=MibTableColumn
hm2AgentDot1qMrpMsrpPortPktRxBadFormat=_Hm2AgentDot1qMrpMsrpPortPktRxBadFormat_Object((1,3,6,1,4,1,248,12,60,2,3,2,6,1,5),_Hm2AgentDot1qMrpMsrpPortPktRxBadFormat_Type())
hm2AgentDot1qMrpMsrpPortPktRxBadFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMsrpPortPktRxBadFormat.setStatus(_A)
_Hm2AgentDot1qMrpMsrpPortPktTxFailure_Type=Counter32
_Hm2AgentDot1qMrpMsrpPortPktTxFailure_Object=MibTableColumn
hm2AgentDot1qMrpMsrpPortPktTxFailure=_Hm2AgentDot1qMrpMsrpPortPktTxFailure_Object((1,3,6,1,4,1,248,12,60,2,3,2,6,1,6),_Hm2AgentDot1qMrpMsrpPortPktTxFailure_Type())
hm2AgentDot1qMrpMsrpPortPktTxFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMsrpPortPktTxFailure.setStatus(_A)
_Hm2AgentDot1qMrpMsrpPortPktRegFailure_Type=Counter32
_Hm2AgentDot1qMrpMsrpPortPktRegFailure_Object=MibTableColumn
hm2AgentDot1qMrpMsrpPortPktRegFailure=_Hm2AgentDot1qMrpMsrpPortPktRegFailure_Object((1,3,6,1,4,1,248,12,60,2,3,2,6,1,7),_Hm2AgentDot1qMrpMsrpPortPktRegFailure_Type())
hm2AgentDot1qMrpMsrpPortPktRegFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMsrpPortPktRegFailure.setStatus(_A)
_Hm2AgentDot1qMrpMsrpPktMessageFailure_Type=Counter32
_Hm2AgentDot1qMrpMsrpPktMessageFailure_Object=MibScalar
hm2AgentDot1qMrpMsrpPktMessageFailure=_Hm2AgentDot1qMrpMsrpPktMessageFailure_Object((1,3,6,1,4,1,248,12,60,2,3,2,7),_Hm2AgentDot1qMrpMsrpPktMessageFailure_Type())
hm2AgentDot1qMrpMsrpPktMessageFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMsrpPktMessageFailure.setStatus(_A)
_Hm2AgentDot1qFqtss_ObjectIdentity=ObjectIdentity
hm2AgentDot1qFqtss=_Hm2AgentDot1qFqtss_ObjectIdentity((1,3,6,1,4,1,248,12,60,2,3,3))
_Hm2AgentDot1qFqtssNotifications_ObjectIdentity=ObjectIdentity
hm2AgentDot1qFqtssNotifications=_Hm2AgentDot1qFqtssNotifications_ObjectIdentity((1,3,6,1,4,1,248,12,60,2,3,3,0))
_Hm2AgentDot1qFqtssObjects_ObjectIdentity=ObjectIdentity
hm2AgentDot1qFqtssObjects=_Hm2AgentDot1qFqtssObjects_ObjectIdentity((1,3,6,1,4,1,248,12,60,2,3,3,1))
_Hm2AgentDot1qFqtssConformance_ObjectIdentity=ObjectIdentity
hm2AgentDot1qFqtssConformance=_Hm2AgentDot1qFqtssConformance_ObjectIdentity((1,3,6,1,4,1,248,12,60,2,3,3,2))
_Hm2AgentDot1qFqtssBap_ObjectIdentity=ObjectIdentity
hm2AgentDot1qFqtssBap=_Hm2AgentDot1qFqtssBap_ObjectIdentity((1,3,6,1,4,1,248,12,60,2,3,3,3))
_Hm2AgentDot1qFqtssBapTable_Object=MibTable
hm2AgentDot1qFqtssBapTable=_Hm2AgentDot1qFqtssBapTable_Object((1,3,6,1,4,1,248,12,60,2,3,3,3,1))
if mibBuilder.loadTexts:hm2AgentDot1qFqtssBapTable.setStatus(_A)
_Hm2AgentDot1qFqtssBapEntry_Object=MibTableRow
hm2AgentDot1qFqtssBapEntry=_Hm2AgentDot1qFqtssBapEntry_Object((1,3,6,1,4,1,248,12,60,2,3,3,3,1,1))
hm2AgentDot1qFqtssBapEntry.setIndexNames((0,_C,_F),(0,_C,_J))
if mibBuilder.loadTexts:hm2AgentDot1qFqtssBapEntry.setStatus(_A)
_Hm2AgentDot1qFqtssTrafficClass_Type=Hm2AgentDot1qFqtssTrafficClassValue
_Hm2AgentDot1qFqtssTrafficClass_Object=MibTableColumn
hm2AgentDot1qFqtssTrafficClass=_Hm2AgentDot1qFqtssTrafficClass_Object((1,3,6,1,4,1,248,12,60,2,3,3,3,1,1,1),_Hm2AgentDot1qFqtssTrafficClass_Type())
hm2AgentDot1qFqtssTrafficClass.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentDot1qFqtssTrafficClass.setStatus(_A)
_Hm2AgentDot1qFqtssDeltaBandwidth_Type=Hm2AgentDot1qFqtssDeltaBandwidthValue
_Hm2AgentDot1qFqtssDeltaBandwidth_Object=MibTableColumn
hm2AgentDot1qFqtssDeltaBandwidth=_Hm2AgentDot1qFqtssDeltaBandwidth_Object((1,3,6,1,4,1,248,12,60,2,3,3,3,1,1,2),_Hm2AgentDot1qFqtssDeltaBandwidth_Type())
hm2AgentDot1qFqtssDeltaBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2AgentDot1qFqtssDeltaBandwidth.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentDot1qFqtssDeltaBandwidth.setUnits('percent')
_Hm2AgentDot1qFqtssOperIdleSlopeMs_Type=Unsigned32
_Hm2AgentDot1qFqtssOperIdleSlopeMs_Object=MibTableColumn
hm2AgentDot1qFqtssOperIdleSlopeMs=_Hm2AgentDot1qFqtssOperIdleSlopeMs_Object((1,3,6,1,4,1,248,12,60,2,3,3,3,1,1,3),_Hm2AgentDot1qFqtssOperIdleSlopeMs_Type())
hm2AgentDot1qFqtssOperIdleSlopeMs.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qFqtssOperIdleSlopeMs.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentDot1qFqtssOperIdleSlopeMs.setUnits(_K)
_Hm2AgentDot1qFqtssOperIdleSlopeLs_Type=Unsigned32
_Hm2AgentDot1qFqtssOperIdleSlopeLs_Object=MibTableColumn
hm2AgentDot1qFqtssOperIdleSlopeLs=_Hm2AgentDot1qFqtssOperIdleSlopeLs_Object((1,3,6,1,4,1,248,12,60,2,3,3,3,1,1,4),_Hm2AgentDot1qFqtssOperIdleSlopeLs_Type())
hm2AgentDot1qFqtssOperIdleSlopeLs.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qFqtssOperIdleSlopeLs.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentDot1qFqtssOperIdleSlopeLs.setUnits(_K)
class _Hm2AgentDot1qFqtssAdminIdleSlopeMs_Type(Unsigned32):defaultValue=0
_Hm2AgentDot1qFqtssAdminIdleSlopeMs_Type.__name__=_E
_Hm2AgentDot1qFqtssAdminIdleSlopeMs_Object=MibTableColumn
hm2AgentDot1qFqtssAdminIdleSlopeMs=_Hm2AgentDot1qFqtssAdminIdleSlopeMs_Object((1,3,6,1,4,1,248,12,60,2,3,3,3,1,1,5),_Hm2AgentDot1qFqtssAdminIdleSlopeMs_Type())
hm2AgentDot1qFqtssAdminIdleSlopeMs.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2AgentDot1qFqtssAdminIdleSlopeMs.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentDot1qFqtssAdminIdleSlopeMs.setUnits(_K)
class _Hm2AgentDot1qFqtssAdminIdleSlopeLs_Type(Unsigned32):defaultValue=0
_Hm2AgentDot1qFqtssAdminIdleSlopeLs_Type.__name__=_E
_Hm2AgentDot1qFqtssAdminIdleSlopeLs_Object=MibTableColumn
hm2AgentDot1qFqtssAdminIdleSlopeLs=_Hm2AgentDot1qFqtssAdminIdleSlopeLs_Object((1,3,6,1,4,1,248,12,60,2,3,3,3,1,1,6),_Hm2AgentDot1qFqtssAdminIdleSlopeLs_Type())
hm2AgentDot1qFqtssAdminIdleSlopeLs.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2AgentDot1qFqtssAdminIdleSlopeLs.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentDot1qFqtssAdminIdleSlopeLs.setUnits(_K)
_Hm2AgentDot1qFqtssMappings_ObjectIdentity=ObjectIdentity
hm2AgentDot1qFqtssMappings=_Hm2AgentDot1qFqtssMappings_ObjectIdentity((1,3,6,1,4,1,248,12,60,2,3,3,4))
_Hm2AgentDot1qFqtssTxSelectionAlgorithmTable_Object=MibTable
hm2AgentDot1qFqtssTxSelectionAlgorithmTable=_Hm2AgentDot1qFqtssTxSelectionAlgorithmTable_Object((1,3,6,1,4,1,248,12,60,2,3,3,4,1))
if mibBuilder.loadTexts:hm2AgentDot1qFqtssTxSelectionAlgorithmTable.setStatus(_A)
_Hm2AgentDot1qFqtssTxSelectionAlgorithmEntry_Object=MibTableRow
hm2AgentDot1qFqtssTxSelectionAlgorithmEntry=_Hm2AgentDot1qFqtssTxSelectionAlgorithmEntry_Object((1,3,6,1,4,1,248,12,60,2,3,3,4,1,1))
hm2AgentDot1qFqtssTxSelectionAlgorithmEntry.setIndexNames((0,_C,_F),(0,_C,_J))
if mibBuilder.loadTexts:hm2AgentDot1qFqtssTxSelectionAlgorithmEntry.setStatus(_A)
_Hm2AgentDot1qFqtssTxSelectionAlgorithmID_Type=Hm2AgentDot1qFtqssTxSelectionAlgorithmIDValue
_Hm2AgentDot1qFqtssTxSelectionAlgorithmID_Object=MibTableColumn
hm2AgentDot1qFqtssTxSelectionAlgorithmID=_Hm2AgentDot1qFqtssTxSelectionAlgorithmID_Object((1,3,6,1,4,1,248,12,60,2,3,3,4,1,1,1),_Hm2AgentDot1qFqtssTxSelectionAlgorithmID_Type())
hm2AgentDot1qFqtssTxSelectionAlgorithmID.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2AgentDot1qFqtssTxSelectionAlgorithmID.setStatus(_A)
_Hm2AgentDot1qFqtssSrpRegenOverrideTable_Object=MibTable
hm2AgentDot1qFqtssSrpRegenOverrideTable=_Hm2AgentDot1qFqtssSrpRegenOverrideTable_Object((1,3,6,1,4,1,248,12,60,2,3,3,4,2))
if mibBuilder.loadTexts:hm2AgentDot1qFqtssSrpRegenOverrideTable.setStatus(_A)
_Hm2AgentDot1qFqtssSrpRegenOverrideEntry_Object=MibTableRow
hm2AgentDot1qFqtssSrpRegenOverrideEntry=_Hm2AgentDot1qFqtssSrpRegenOverrideEntry_Object((1,3,6,1,4,1,248,12,60,2,3,3,4,2,1))
hm2AgentDot1qFqtssSrpRegenOverrideEntry.setIndexNames((0,_C,_F),(0,_C,_J))
if mibBuilder.loadTexts:hm2AgentDot1qFqtssSrpRegenOverrideEntry.setStatus(_A)
_Hm2AgentDot1qFqtssSrClassPriority_Type=Hm2AgentDot1qPriorityValue
_Hm2AgentDot1qFqtssSrClassPriority_Object=MibTableColumn
hm2AgentDot1qFqtssSrClassPriority=_Hm2AgentDot1qFqtssSrClassPriority_Object((1,3,6,1,4,1,248,12,60,2,3,3,4,2,1,1),_Hm2AgentDot1qFqtssSrClassPriority_Type())
hm2AgentDot1qFqtssSrClassPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2AgentDot1qFqtssSrClassPriority.setStatus(_A)
_Hm2AgentDot1qFqtssPriorityRegenOverride_Type=Hm2AgentDot1qPriorityValue
_Hm2AgentDot1qFqtssPriorityRegenOverride_Object=MibTableColumn
hm2AgentDot1qFqtssPriorityRegenOverride=_Hm2AgentDot1qFqtssPriorityRegenOverride_Object((1,3,6,1,4,1,248,12,60,2,3,3,4,2,1,2),_Hm2AgentDot1qFqtssPriorityRegenOverride_Type())
hm2AgentDot1qFqtssPriorityRegenOverride.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2AgentDot1qFqtssPriorityRegenOverride.setStatus(_A)
_Hm2AgentDot1qFqtssSrpBoundaryPort_Type=TruthValue
_Hm2AgentDot1qFqtssSrpBoundaryPort_Object=MibTableColumn
hm2AgentDot1qFqtssSrpBoundaryPort=_Hm2AgentDot1qFqtssSrpBoundaryPort_Object((1,3,6,1,4,1,248,12,60,2,3,3,4,2,1,3),_Hm2AgentDot1qFqtssSrpBoundaryPort_Type())
hm2AgentDot1qFqtssSrpBoundaryPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qFqtssSrpBoundaryPort.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'Hm2AgentDot1qPriorityValue':Hm2AgentDot1qPriorityValue,'Hm2AgentDot1qMsrpStreamRankValue':Hm2AgentDot1qMsrpStreamRankValue,'Hm2AgentDot1qMsrpStreamIdValue':Hm2AgentDot1qMsrpStreamIdValue,'Hm2AgentDot1qMsrpReservationDirectionValue':Hm2AgentDot1qMsrpReservationDirectionValue,'Hm2AgentDot1qMsrpReservationDeclarationTypeValue':Hm2AgentDot1qMsrpReservationDeclarationTypeValue,'Hm2AgentDot1qMsrpReservationFailureCodeValue':Hm2AgentDot1qMsrpReservationFailureCodeValue,'Hm2AgentDot1qFqtssTrafficClassValue':Hm2AgentDot1qFqtssTrafficClassValue,'Hm2AgentDot1qFqtssDeltaBandwidthValue':Hm2AgentDot1qFqtssDeltaBandwidthValue,'Hm2AgentDot1qFtqssTxSelectionAlgorithmIDValue':Hm2AgentDot1qFtqssTxSelectionAlgorithmIDValue,'hm2PlatformMSRP':hm2PlatformMSRP,'hm2AgentDot1qMsrp':hm2AgentDot1qMsrp,'hm2AgentDot1qPortMsrpTable':hm2AgentDot1qPortMsrpTable,'hm2AgentDot1qPortMsrpEntry':hm2AgentDot1qPortMsrpEntry,_F:hm2AgentDot1qMsrpPort,'hm2AgentDot1qPortMsrpEnabledStatus':hm2AgentDot1qPortMsrpEnabledStatus,'hm2AgentDot1qPortMsrpFailedRegistrations':hm2AgentDot1qPortMsrpFailedRegistrations,'hm2AgentDot1qPortMsrpLastPduOrigin':hm2AgentDot1qPortMsrpLastPduOrigin,'hm2AgentDot1qPortMsrpPvid':hm2AgentDot1qPortMsrpPvid,'hm2AgentDot1qBridgeMsrpEnabledStatus':hm2AgentDot1qBridgeMsrpEnabledStatus,'hm2AgentDot1qBridgeMsrpTalkerPruning':hm2AgentDot1qBridgeMsrpTalkerPruning,'hm2AgentDot1qBridgeMsrpMaxFanInPorts':hm2AgentDot1qBridgeMsrpMaxFanInPorts,'hm2AgentDot1qBridgeMsrpBoundaryPropagate':hm2AgentDot1qBridgeMsrpBoundaryPropagate,'hm2AgentDot1qMsrpStreamTable':hm2AgentDot1qMsrpStreamTable,'hm2AgentDot1qMsrpStreamEntry':hm2AgentDot1qMsrpStreamEntry,_M:hm2AgentDot1qMsrpStreamIndex,'hm2AgentDot1qMsrpStreamID':hm2AgentDot1qMsrpStreamID,'hm2AgentDot1qMsrpStreamDestMacAddr':hm2AgentDot1qMsrpStreamDestMacAddr,'hm2AgentDot1qMsrpStreamVlanId':hm2AgentDot1qMsrpStreamVlanId,'hm2AgentDot1qMsrpStreamTspecMaxFrameSize':hm2AgentDot1qMsrpStreamTspecMaxFrameSize,'hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames':hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames,'hm2AgentDot1qMsrpStreamDataFramePriority':hm2AgentDot1qMsrpStreamDataFramePriority,'hm2AgentDot1qMsrpStreamRank':hm2AgentDot1qMsrpStreamRank,'hm2AgentDot1qMsrpReservationTable':hm2AgentDot1qMsrpReservationTable,'hm2AgentDot1qMsrpReservationEntry':hm2AgentDot1qMsrpReservationEntry,_N:hm2AgentDot1qMsrpReservationStreamId,_O:hm2AgentDot1qMsrpReservationDirection,'hm2AgentDot1qMsrpReservationDeclarationType':hm2AgentDot1qMsrpReservationDeclarationType,'hm2AgentDot1qMsrpReservationAccumulatedLatency':hm2AgentDot1qMsrpReservationAccumulatedLatency,'hm2AgentDot1qMsrpReservationFailureBridgeId':hm2AgentDot1qMsrpReservationFailureBridgeId,'hm2AgentDot1qMsrpReservationFailureCode':hm2AgentDot1qMsrpReservationFailureCode,'hm2AgentDot1qMsrpReservationDroppedStreamFrames':hm2AgentDot1qMsrpReservationDroppedStreamFrames,'hm2AgentDot1qMsrpReservationStreamAge':hm2AgentDot1qMsrpReservationStreamAge,'hm2AgentDot1qMrpMsrpStats':hm2AgentDot1qMrpMsrpStats,'hm2AgentDot1qMrpMsrpPktTx':hm2AgentDot1qMrpMsrpPktTx,'hm2AgentDot1qMrpMsrpPktRx':hm2AgentDot1qMrpMsrpPktRx,'hm2AgentDot1qMrpMsrpPktRxBadHeader':hm2AgentDot1qMrpMsrpPktRxBadHeader,'hm2AgentDot1qMrpMsrpPktRxBadFormat':hm2AgentDot1qMrpMsrpPktRxBadFormat,'hm2AgentDot1qMrpMsrpPktTxFailure':hm2AgentDot1qMrpMsrpPktTxFailure,'hm2AgentDot1qMrpMsrpStatsTable':hm2AgentDot1qMrpMsrpStatsTable,'hm2AgentDot1qMrpMsrpStatsEntry':hm2AgentDot1qMrpMsrpStatsEntry,_P:hm2AgentDot1qMrpMsrpIntf,'hm2AgentDot1qMrpMsrpPortPktTx':hm2AgentDot1qMrpMsrpPortPktTx,'hm2AgentDot1qMrpMsrpPortPktRx':hm2AgentDot1qMrpMsrpPortPktRx,'hm2AgentDot1qMrpMsrpPortPktRxBadHeader':hm2AgentDot1qMrpMsrpPortPktRxBadHeader,'hm2AgentDot1qMrpMsrpPortPktRxBadFormat':hm2AgentDot1qMrpMsrpPortPktRxBadFormat,'hm2AgentDot1qMrpMsrpPortPktTxFailure':hm2AgentDot1qMrpMsrpPortPktTxFailure,'hm2AgentDot1qMrpMsrpPortPktRegFailure':hm2AgentDot1qMrpMsrpPortPktRegFailure,'hm2AgentDot1qMrpMsrpPktMessageFailure':hm2AgentDot1qMrpMsrpPktMessageFailure,'hm2AgentDot1qFqtss':hm2AgentDot1qFqtss,'hm2AgentDot1qFqtssNotifications':hm2AgentDot1qFqtssNotifications,'hm2AgentDot1qFqtssObjects':hm2AgentDot1qFqtssObjects,'hm2AgentDot1qFqtssConformance':hm2AgentDot1qFqtssConformance,'hm2AgentDot1qFqtssBap':hm2AgentDot1qFqtssBap,'hm2AgentDot1qFqtssBapTable':hm2AgentDot1qFqtssBapTable,'hm2AgentDot1qFqtssBapEntry':hm2AgentDot1qFqtssBapEntry,_J:hm2AgentDot1qFqtssTrafficClass,'hm2AgentDot1qFqtssDeltaBandwidth':hm2AgentDot1qFqtssDeltaBandwidth,'hm2AgentDot1qFqtssOperIdleSlopeMs':hm2AgentDot1qFqtssOperIdleSlopeMs,'hm2AgentDot1qFqtssOperIdleSlopeLs':hm2AgentDot1qFqtssOperIdleSlopeLs,'hm2AgentDot1qFqtssAdminIdleSlopeMs':hm2AgentDot1qFqtssAdminIdleSlopeMs,'hm2AgentDot1qFqtssAdminIdleSlopeLs':hm2AgentDot1qFqtssAdminIdleSlopeLs,'hm2AgentDot1qFqtssMappings':hm2AgentDot1qFqtssMappings,'hm2AgentDot1qFqtssTxSelectionAlgorithmTable':hm2AgentDot1qFqtssTxSelectionAlgorithmTable,'hm2AgentDot1qFqtssTxSelectionAlgorithmEntry':hm2AgentDot1qFqtssTxSelectionAlgorithmEntry,'hm2AgentDot1qFqtssTxSelectionAlgorithmID':hm2AgentDot1qFqtssTxSelectionAlgorithmID,'hm2AgentDot1qFqtssSrpRegenOverrideTable':hm2AgentDot1qFqtssSrpRegenOverrideTable,'hm2AgentDot1qFqtssSrpRegenOverrideEntry':hm2AgentDot1qFqtssSrpRegenOverrideEntry,'hm2AgentDot1qFqtssSrClassPriority':hm2AgentDot1qFqtssSrClassPriority,'hm2AgentDot1qFqtssPriorityRegenOverride':hm2AgentDot1qFqtssPriorityRegenOverride,'hm2AgentDot1qFqtssSrpBoundaryPort':hm2AgentDot1qFqtssSrpBoundaryPort})