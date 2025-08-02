_A9='ieee8021SrpReservationsPreloadGroup'
_A8='ieee8021SrpStreamsPreloadGroup'
_A7='ieee8021SrpMonitoringSRclassesGroup'
_A6='ieee8021SrpConfigurationPruningGroup'
_A5='ieee8021SrpReservationsGroup'
_A4='ieee8021SrpStreamsGroup'
_A3='ieee8021SrpLatencyGroup'
_A2='ieee8021SrpConfigurationGroup'
_A1='ieee8021SrpReservationPreloadAccumulatedLatency'
_A0='ieee8021SrpStreamPreloadRank'
_z='ieee8021SrpStreamPreloadDataFramePriority'
_y='ieee8021SrpStreamPreloadTspecMaxIntervalFrames'
_x='ieee8021SrpStreamPreloadTspecMaxFrameSize'
_w='ieee8021SrpStreamPreloadVlanId'
_v='ieee8021SrpStreamPreloadDestinationAddress'
_u='ieee8021SrpReservationStreamAge'
_t='ieee8021SrpReservationDroppedStreamFrames'
_s='ieee8021SrpReservationFailureCode'
_r='ieee8021SrpReservationFailureSystemId'
_q='ieee8021SrpReservationAccumulatedLatency'
_p='ieee8021SrpReservationDeclarationType'
_o='ieee8021SrpStreamRank'
_n='ieee8021SrpStreamDataFramePriority'
_m='ieee8021SrpStreamTspecMaxIntervalFrames'
_l='ieee8021SrpStreamTspecMaxFrameSize'
_k='ieee8021SrpStreamVlanId'
_j='ieee8021SrpStreamDestinationAddress'
_i='ieee8021SrpPortTcLatency'
_h='ieee8021SrpBridgePortSrPvid'
_g='ieee8021SrpBridgePortMsrpLastPduOrigin'
_f='ieee8021SrpBridgePortMsrpFailedRegistrations'
_e='ieee8021SrpBridgePortMsrpEnabledStatus'
_d='ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize'
_c='ieee8021SrpBridgeBaseMsrpMaxFanInPorts'
_b='ieee8021SrpBridgeBaseMsrpTalkerPruning'
_a='ieee8021SrpBridgeBaseMsrpEnabledStatus'
_Z='ieee8021SrpBridgePortEntry'
_Y='ieee8021SrpBridgeBaseEntry'
_X='ieee8021SrpReservationDirection'
_W='ieee8021SrpReservationStreamId'
_V='ieee8021SrpStreamId'
_U='ieee8021SrpTrafficClass'
_T='IEEE8021VlanIndex'
_S='OctetString'
_R='ieee8021SrpBridgePortMsrpTalkerPrunningPerPort'
_Q='ieee8021SrpBridgeBaseMsrpMaxSRClasses'
_P='ieee8021SrpBridgeBaseMsrpTalkerVlanPruning'
_O='ieee8021SrpReservationPreloadDirection'
_N='ieee8021SrpReservationsPreloadStreamId'
_M='ieee8021SrpStreamPreloadId'
_L='nano-seconds'
_K='ieee8021BridgeBasePort'
_J='ieee8021BridgeBaseComponentId'
_I='not-accessible'
_H='TruthValue'
_G='Unsigned32'
_F='IEEE8021-BRIDGE-MIB'
_E='read-write'
_D='read-create'
_C='read-only'
_B='IEEE8021-SRP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ieee8021BridgeBaseComponentId,ieee8021BridgeBaseEntry,ieee8021BridgeBasePort,ieee8021BridgeBasePortEntry=mibBuilder.importSymbols(_F,_J,'ieee8021BridgeBaseEntry',_K,'ieee8021BridgeBasePortEntry')
IEEE8021FqtssTrafficClassValue,=mibBuilder.importSymbols('IEEE8021-FQTSS-MIB','IEEE8021FqtssTrafficClassValue')
IEEE8021PriorityCodePoint,IEEE8021VlanIndex,ieee802dot1mibs=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021PriorityCodePoint',_T,'ieee802dot1mibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_H)
ieee8021SrpMib=ModuleIdentity((1,3,111,2,802,1,1,19))
if mibBuilder.loadTexts:ieee8021SrpMib.setRevisions(('2018-10-04 00:00','2018-06-28 00:00','2015-12-02 00:00','2014-12-15 00:00','2011-02-27 00:00','2010-04-19 00:00'))
class IEEE8021SrpStreamRankValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('emergency',0),('nonEmergency',1)))
class IEEE8021SrpStreamIdValue(TextualConvention,OctetString):status=_A;displayHint='1x:1x:1x:1x:1x:1x.1x:1x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class IEEE8021SrpReservationDirectionValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('talkerRegistrations',0),('listenerRegistrations',1)))
class IEEE8021SrpReservationDeclarationTypeValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('talkerAdvertise',0),('talkerFailed',1),('listenerAskingFailed',2),('listenerReady',3),('listenerReadyFailed',4)))
class IEEE8021SrpReservationFailureCodeValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*(('noFailure',0),('insufficientBandwidth',1),('insufficientResources',2),('insufficientTrafficClassBandwidth',3),('streamIDInUse',4),('streamDestinationAddressInUse',5),('streamPreemptedByHigherRank',6),('latencyHasChanged',7),('egressPortNotAVBCapable',8),('useDifferentDestinationAddress',9),('outOfMSRPResources',10),('outOfMMRPResources',11),('cannotStoreDestinationAddress',12),('priorityIsNoAnSRCLass',13),('maxFrameSizeTooLarge',14),('maxFanInPortsLimitReached',15),('firstValueChangedForStreamID',16),('vlanBlockedOnEgress',17),('vlanTaggingDisabledOnEgress',18),('srClassPriorityMismatch',19)))
_Ieee8021SrpNotifications_ObjectIdentity=ObjectIdentity
ieee8021SrpNotifications=_Ieee8021SrpNotifications_ObjectIdentity((1,3,111,2,802,1,1,19,0))
_Ieee8021SrpObjects_ObjectIdentity=ObjectIdentity
ieee8021SrpObjects=_Ieee8021SrpObjects_ObjectIdentity((1,3,111,2,802,1,1,19,1))
_Ieee8021SrpConfiguration_ObjectIdentity=ObjectIdentity
ieee8021SrpConfiguration=_Ieee8021SrpConfiguration_ObjectIdentity((1,3,111,2,802,1,1,19,1,1))
_Ieee8021SrpBridgeBaseTable_Object=MibTable
ieee8021SrpBridgeBaseTable=_Ieee8021SrpBridgeBaseTable_Object((1,3,111,2,802,1,1,19,1,1,1))
if mibBuilder.loadTexts:ieee8021SrpBridgeBaseTable.setStatus(_A)
_Ieee8021SrpBridgeBaseEntry_Object=MibTableRow
ieee8021SrpBridgeBaseEntry=_Ieee8021SrpBridgeBaseEntry_Object((1,3,111,2,802,1,1,19,1,1,1,1))
if mibBuilder.loadTexts:ieee8021SrpBridgeBaseEntry.setStatus(_A)
class _Ieee8021SrpBridgeBaseMsrpEnabledStatus_Type(TruthValue):defaultValue=1
_Ieee8021SrpBridgeBaseMsrpEnabledStatus_Type.__name__=_H
_Ieee8021SrpBridgeBaseMsrpEnabledStatus_Object=MibTableColumn
ieee8021SrpBridgeBaseMsrpEnabledStatus=_Ieee8021SrpBridgeBaseMsrpEnabledStatus_Object((1,3,111,2,802,1,1,19,1,1,1,1,1),_Ieee8021SrpBridgeBaseMsrpEnabledStatus_Type())
ieee8021SrpBridgeBaseMsrpEnabledStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SrpBridgeBaseMsrpEnabledStatus.setStatus(_A)
class _Ieee8021SrpBridgeBaseMsrpTalkerPruning_Type(TruthValue):defaultValue=2
_Ieee8021SrpBridgeBaseMsrpTalkerPruning_Type.__name__=_H
_Ieee8021SrpBridgeBaseMsrpTalkerPruning_Object=MibTableColumn
ieee8021SrpBridgeBaseMsrpTalkerPruning=_Ieee8021SrpBridgeBaseMsrpTalkerPruning_Object((1,3,111,2,802,1,1,19,1,1,1,1,2),_Ieee8021SrpBridgeBaseMsrpTalkerPruning_Type())
ieee8021SrpBridgeBaseMsrpTalkerPruning.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SrpBridgeBaseMsrpTalkerPruning.setStatus(_A)
class _Ieee8021SrpBridgeBaseMsrpMaxFanInPorts_Type(Unsigned32):defaultValue=0
_Ieee8021SrpBridgeBaseMsrpMaxFanInPorts_Type.__name__=_G
_Ieee8021SrpBridgeBaseMsrpMaxFanInPorts_Object=MibTableColumn
ieee8021SrpBridgeBaseMsrpMaxFanInPorts=_Ieee8021SrpBridgeBaseMsrpMaxFanInPorts_Object((1,3,111,2,802,1,1,19,1,1,1,1,3),_Ieee8021SrpBridgeBaseMsrpMaxFanInPorts_Type())
ieee8021SrpBridgeBaseMsrpMaxFanInPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SrpBridgeBaseMsrpMaxFanInPorts.setStatus(_A)
class _Ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize_Type(Unsigned32):defaultValue=2000
_Ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize_Type.__name__=_G
_Ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize_Object=MibTableColumn
ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize=_Ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize_Object((1,3,111,2,802,1,1,19,1,1,1,1,4),_Ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize_Type())
ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize.setStatus(_A)
class _Ieee8021SrpBridgeBaseMsrpTalkerVlanPruning_Type(TruthValue):defaultValue=2
_Ieee8021SrpBridgeBaseMsrpTalkerVlanPruning_Type.__name__=_H
_Ieee8021SrpBridgeBaseMsrpTalkerVlanPruning_Object=MibTableColumn
ieee8021SrpBridgeBaseMsrpTalkerVlanPruning=_Ieee8021SrpBridgeBaseMsrpTalkerVlanPruning_Object((1,3,111,2,802,1,1,19,1,1,1,1,5),_Ieee8021SrpBridgeBaseMsrpTalkerVlanPruning_Type())
ieee8021SrpBridgeBaseMsrpTalkerVlanPruning.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SrpBridgeBaseMsrpTalkerVlanPruning.setStatus(_A)
_Ieee8021SrpBridgeBaseMsrpMaxSRClasses_Type=Unsigned32
_Ieee8021SrpBridgeBaseMsrpMaxSRClasses_Object=MibTableColumn
ieee8021SrpBridgeBaseMsrpMaxSRClasses=_Ieee8021SrpBridgeBaseMsrpMaxSRClasses_Object((1,3,111,2,802,1,1,19,1,1,1,1,6),_Ieee8021SrpBridgeBaseMsrpMaxSRClasses_Type())
ieee8021SrpBridgeBaseMsrpMaxSRClasses.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpBridgeBaseMsrpMaxSRClasses.setStatus(_A)
_Ieee8021SrpBridgePortTable_Object=MibTable
ieee8021SrpBridgePortTable=_Ieee8021SrpBridgePortTable_Object((1,3,111,2,802,1,1,19,1,1,2))
if mibBuilder.loadTexts:ieee8021SrpBridgePortTable.setStatus(_A)
_Ieee8021SrpBridgePortEntry_Object=MibTableRow
ieee8021SrpBridgePortEntry=_Ieee8021SrpBridgePortEntry_Object((1,3,111,2,802,1,1,19,1,1,2,1))
if mibBuilder.loadTexts:ieee8021SrpBridgePortEntry.setStatus(_A)
class _Ieee8021SrpBridgePortMsrpEnabledStatus_Type(TruthValue):defaultValue=1
_Ieee8021SrpBridgePortMsrpEnabledStatus_Type.__name__=_H
_Ieee8021SrpBridgePortMsrpEnabledStatus_Object=MibTableColumn
ieee8021SrpBridgePortMsrpEnabledStatus=_Ieee8021SrpBridgePortMsrpEnabledStatus_Object((1,3,111,2,802,1,1,19,1,1,2,1,1),_Ieee8021SrpBridgePortMsrpEnabledStatus_Type())
ieee8021SrpBridgePortMsrpEnabledStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SrpBridgePortMsrpEnabledStatus.setStatus(_A)
_Ieee8021SrpBridgePortMsrpFailedRegistrations_Type=Counter64
_Ieee8021SrpBridgePortMsrpFailedRegistrations_Object=MibTableColumn
ieee8021SrpBridgePortMsrpFailedRegistrations=_Ieee8021SrpBridgePortMsrpFailedRegistrations_Object((1,3,111,2,802,1,1,19,1,1,2,1,2),_Ieee8021SrpBridgePortMsrpFailedRegistrations_Type())
ieee8021SrpBridgePortMsrpFailedRegistrations.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpBridgePortMsrpFailedRegistrations.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SrpBridgePortMsrpFailedRegistrations.setUnits('failed MSRP registrations')
_Ieee8021SrpBridgePortMsrpLastPduOrigin_Type=MacAddress
_Ieee8021SrpBridgePortMsrpLastPduOrigin_Object=MibTableColumn
ieee8021SrpBridgePortMsrpLastPduOrigin=_Ieee8021SrpBridgePortMsrpLastPduOrigin_Object((1,3,111,2,802,1,1,19,1,1,2,1,3),_Ieee8021SrpBridgePortMsrpLastPduOrigin_Type())
ieee8021SrpBridgePortMsrpLastPduOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpBridgePortMsrpLastPduOrigin.setStatus(_A)
class _Ieee8021SrpBridgePortSrPvid_Type(IEEE8021VlanIndex):defaultValue=2
_Ieee8021SrpBridgePortSrPvid_Type.__name__=_T
_Ieee8021SrpBridgePortSrPvid_Object=MibTableColumn
ieee8021SrpBridgePortSrPvid=_Ieee8021SrpBridgePortSrPvid_Object((1,3,111,2,802,1,1,19,1,1,2,1,4),_Ieee8021SrpBridgePortSrPvid_Type())
ieee8021SrpBridgePortSrPvid.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SrpBridgePortSrPvid.setStatus(_A)
class _Ieee8021SrpBridgePortMsrpTalkerPrunningPerPort_Type(TruthValue):defaultValue=2
_Ieee8021SrpBridgePortMsrpTalkerPrunningPerPort_Type.__name__=_H
_Ieee8021SrpBridgePortMsrpTalkerPrunningPerPort_Object=MibTableColumn
ieee8021SrpBridgePortMsrpTalkerPrunningPerPort=_Ieee8021SrpBridgePortMsrpTalkerPrunningPerPort_Object((1,3,111,2,802,1,1,19,1,1,2,1,5),_Ieee8021SrpBridgePortMsrpTalkerPrunningPerPort_Type())
ieee8021SrpBridgePortMsrpTalkerPrunningPerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021SrpBridgePortMsrpTalkerPrunningPerPort.setStatus(_A)
_Ieee8021SrpLatency_ObjectIdentity=ObjectIdentity
ieee8021SrpLatency=_Ieee8021SrpLatency_ObjectIdentity((1,3,111,2,802,1,1,19,1,2))
_Ieee8021SrpLatencyTable_Object=MibTable
ieee8021SrpLatencyTable=_Ieee8021SrpLatencyTable_Object((1,3,111,2,802,1,1,19,1,2,1))
if mibBuilder.loadTexts:ieee8021SrpLatencyTable.setStatus(_A)
_Ieee8021SrpLatencyEntry_Object=MibTableRow
ieee8021SrpLatencyEntry=_Ieee8021SrpLatencyEntry_Object((1,3,111,2,802,1,1,19,1,2,1,1))
ieee8021SrpLatencyEntry.setIndexNames((0,_F,_J),(0,_F,_K),(0,_B,_U))
if mibBuilder.loadTexts:ieee8021SrpLatencyEntry.setStatus(_A)
_Ieee8021SrpTrafficClass_Type=IEEE8021FqtssTrafficClassValue
_Ieee8021SrpTrafficClass_Object=MibTableColumn
ieee8021SrpTrafficClass=_Ieee8021SrpTrafficClass_Object((1,3,111,2,802,1,1,19,1,2,1,1,1),_Ieee8021SrpTrafficClass_Type())
ieee8021SrpTrafficClass.setMaxAccess(_I)
if mibBuilder.loadTexts:ieee8021SrpTrafficClass.setStatus(_A)
_Ieee8021SrpPortTcLatency_Type=Unsigned32
_Ieee8021SrpPortTcLatency_Object=MibTableColumn
ieee8021SrpPortTcLatency=_Ieee8021SrpPortTcLatency_Object((1,3,111,2,802,1,1,19,1,2,1,1,2),_Ieee8021SrpPortTcLatency_Type())
ieee8021SrpPortTcLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpPortTcLatency.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SrpPortTcLatency.setUnits(_L)
_Ieee8021SrpStreams_ObjectIdentity=ObjectIdentity
ieee8021SrpStreams=_Ieee8021SrpStreams_ObjectIdentity((1,3,111,2,802,1,1,19,1,3))
_Ieee8021SrpStreamTable_Object=MibTable
ieee8021SrpStreamTable=_Ieee8021SrpStreamTable_Object((1,3,111,2,802,1,1,19,1,3,1))
if mibBuilder.loadTexts:ieee8021SrpStreamTable.setStatus(_A)
_Ieee8021SrpStreamEntry_Object=MibTableRow
ieee8021SrpStreamEntry=_Ieee8021SrpStreamEntry_Object((1,3,111,2,802,1,1,19,1,3,1,1))
ieee8021SrpStreamEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:ieee8021SrpStreamEntry.setStatus(_A)
_Ieee8021SrpStreamId_Type=IEEE8021SrpStreamIdValue
_Ieee8021SrpStreamId_Object=MibTableColumn
ieee8021SrpStreamId=_Ieee8021SrpStreamId_Object((1,3,111,2,802,1,1,19,1,3,1,1,1),_Ieee8021SrpStreamId_Type())
ieee8021SrpStreamId.setMaxAccess(_I)
if mibBuilder.loadTexts:ieee8021SrpStreamId.setStatus(_A)
_Ieee8021SrpStreamDestinationAddress_Type=MacAddress
_Ieee8021SrpStreamDestinationAddress_Object=MibTableColumn
ieee8021SrpStreamDestinationAddress=_Ieee8021SrpStreamDestinationAddress_Object((1,3,111,2,802,1,1,19,1,3,1,1,2),_Ieee8021SrpStreamDestinationAddress_Type())
ieee8021SrpStreamDestinationAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpStreamDestinationAddress.setStatus(_A)
_Ieee8021SrpStreamVlanId_Type=IEEE8021VlanIndex
_Ieee8021SrpStreamVlanId_Object=MibTableColumn
ieee8021SrpStreamVlanId=_Ieee8021SrpStreamVlanId_Object((1,3,111,2,802,1,1,19,1,3,1,1,3),_Ieee8021SrpStreamVlanId_Type())
ieee8021SrpStreamVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpStreamVlanId.setStatus(_A)
class _Ieee8021SrpStreamTspecMaxFrameSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ieee8021SrpStreamTspecMaxFrameSize_Type.__name__=_G
_Ieee8021SrpStreamTspecMaxFrameSize_Object=MibTableColumn
ieee8021SrpStreamTspecMaxFrameSize=_Ieee8021SrpStreamTspecMaxFrameSize_Object((1,3,111,2,802,1,1,19,1,3,1,1,4),_Ieee8021SrpStreamTspecMaxFrameSize_Type())
ieee8021SrpStreamTspecMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpStreamTspecMaxFrameSize.setStatus(_A)
class _Ieee8021SrpStreamTspecMaxIntervalFrames_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ieee8021SrpStreamTspecMaxIntervalFrames_Type.__name__=_G
_Ieee8021SrpStreamTspecMaxIntervalFrames_Object=MibTableColumn
ieee8021SrpStreamTspecMaxIntervalFrames=_Ieee8021SrpStreamTspecMaxIntervalFrames_Object((1,3,111,2,802,1,1,19,1,3,1,1,5),_Ieee8021SrpStreamTspecMaxIntervalFrames_Type())
ieee8021SrpStreamTspecMaxIntervalFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpStreamTspecMaxIntervalFrames.setStatus(_A)
_Ieee8021SrpStreamDataFramePriority_Type=IEEE8021PriorityCodePoint
_Ieee8021SrpStreamDataFramePriority_Object=MibTableColumn
ieee8021SrpStreamDataFramePriority=_Ieee8021SrpStreamDataFramePriority_Object((1,3,111,2,802,1,1,19,1,3,1,1,6),_Ieee8021SrpStreamDataFramePriority_Type())
ieee8021SrpStreamDataFramePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpStreamDataFramePriority.setStatus(_A)
_Ieee8021SrpStreamRank_Type=IEEE8021SrpStreamRankValue
_Ieee8021SrpStreamRank_Object=MibTableColumn
ieee8021SrpStreamRank=_Ieee8021SrpStreamRank_Object((1,3,111,2,802,1,1,19,1,3,1,1,7),_Ieee8021SrpStreamRank_Type())
ieee8021SrpStreamRank.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpStreamRank.setStatus(_A)
_Ieee8021SrpStreamPreloadTable_Object=MibTable
ieee8021SrpStreamPreloadTable=_Ieee8021SrpStreamPreloadTable_Object((1,3,111,2,802,1,1,19,1,3,2))
if mibBuilder.loadTexts:ieee8021SrpStreamPreloadTable.setStatus(_A)
_Ieee8021SrpStreamPreloadEntry_Object=MibTableRow
ieee8021SrpStreamPreloadEntry=_Ieee8021SrpStreamPreloadEntry_Object((1,3,111,2,802,1,1,19,1,3,2,1))
ieee8021SrpStreamPreloadEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:ieee8021SrpStreamPreloadEntry.setStatus(_A)
_Ieee8021SrpStreamPreloadId_Type=IEEE8021SrpStreamIdValue
_Ieee8021SrpStreamPreloadId_Object=MibTableColumn
ieee8021SrpStreamPreloadId=_Ieee8021SrpStreamPreloadId_Object((1,3,111,2,802,1,1,19,1,3,2,1,1),_Ieee8021SrpStreamPreloadId_Type())
ieee8021SrpStreamPreloadId.setMaxAccess(_I)
if mibBuilder.loadTexts:ieee8021SrpStreamPreloadId.setStatus(_A)
_Ieee8021SrpStreamPreloadDestinationAddress_Type=MacAddress
_Ieee8021SrpStreamPreloadDestinationAddress_Object=MibTableColumn
ieee8021SrpStreamPreloadDestinationAddress=_Ieee8021SrpStreamPreloadDestinationAddress_Object((1,3,111,2,802,1,1,19,1,3,2,1,2),_Ieee8021SrpStreamPreloadDestinationAddress_Type())
ieee8021SrpStreamPreloadDestinationAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021SrpStreamPreloadDestinationAddress.setStatus(_A)
_Ieee8021SrpStreamPreloadVlanId_Type=IEEE8021VlanIndex
_Ieee8021SrpStreamPreloadVlanId_Object=MibTableColumn
ieee8021SrpStreamPreloadVlanId=_Ieee8021SrpStreamPreloadVlanId_Object((1,3,111,2,802,1,1,19,1,3,2,1,3),_Ieee8021SrpStreamPreloadVlanId_Type())
ieee8021SrpStreamPreloadVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021SrpStreamPreloadVlanId.setStatus(_A)
class _Ieee8021SrpStreamPreloadTspecMaxFrameSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ieee8021SrpStreamPreloadTspecMaxFrameSize_Type.__name__=_G
_Ieee8021SrpStreamPreloadTspecMaxFrameSize_Object=MibTableColumn
ieee8021SrpStreamPreloadTspecMaxFrameSize=_Ieee8021SrpStreamPreloadTspecMaxFrameSize_Object((1,3,111,2,802,1,1,19,1,3,2,1,4),_Ieee8021SrpStreamPreloadTspecMaxFrameSize_Type())
ieee8021SrpStreamPreloadTspecMaxFrameSize.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021SrpStreamPreloadTspecMaxFrameSize.setStatus(_A)
class _Ieee8021SrpStreamPreloadTspecMaxIntervalFrames_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ieee8021SrpStreamPreloadTspecMaxIntervalFrames_Type.__name__=_G
_Ieee8021SrpStreamPreloadTspecMaxIntervalFrames_Object=MibTableColumn
ieee8021SrpStreamPreloadTspecMaxIntervalFrames=_Ieee8021SrpStreamPreloadTspecMaxIntervalFrames_Object((1,3,111,2,802,1,1,19,1,3,2,1,5),_Ieee8021SrpStreamPreloadTspecMaxIntervalFrames_Type())
ieee8021SrpStreamPreloadTspecMaxIntervalFrames.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021SrpStreamPreloadTspecMaxIntervalFrames.setStatus(_A)
_Ieee8021SrpStreamPreloadDataFramePriority_Type=IEEE8021PriorityCodePoint
_Ieee8021SrpStreamPreloadDataFramePriority_Object=MibTableColumn
ieee8021SrpStreamPreloadDataFramePriority=_Ieee8021SrpStreamPreloadDataFramePriority_Object((1,3,111,2,802,1,1,19,1,3,2,1,6),_Ieee8021SrpStreamPreloadDataFramePriority_Type())
ieee8021SrpStreamPreloadDataFramePriority.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021SrpStreamPreloadDataFramePriority.setStatus(_A)
_Ieee8021SrpStreamPreloadRank_Type=IEEE8021SrpStreamRankValue
_Ieee8021SrpStreamPreloadRank_Object=MibTableColumn
ieee8021SrpStreamPreloadRank=_Ieee8021SrpStreamPreloadRank_Object((1,3,111,2,802,1,1,19,1,3,2,1,7),_Ieee8021SrpStreamPreloadRank_Type())
ieee8021SrpStreamPreloadRank.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021SrpStreamPreloadRank.setStatus(_A)
_Ieee8021SrpReservations_ObjectIdentity=ObjectIdentity
ieee8021SrpReservations=_Ieee8021SrpReservations_ObjectIdentity((1,3,111,2,802,1,1,19,1,4))
_Ieee8021SrpReservationsTable_Object=MibTable
ieee8021SrpReservationsTable=_Ieee8021SrpReservationsTable_Object((1,3,111,2,802,1,1,19,1,4,1))
if mibBuilder.loadTexts:ieee8021SrpReservationsTable.setStatus(_A)
_Ieee8021SrpReservationsEntry_Object=MibTableRow
ieee8021SrpReservationsEntry=_Ieee8021SrpReservationsEntry_Object((1,3,111,2,802,1,1,19,1,4,1,1))
ieee8021SrpReservationsEntry.setIndexNames((0,_B,_W),(0,_B,_X),(0,_F,_J),(0,_F,_K))
if mibBuilder.loadTexts:ieee8021SrpReservationsEntry.setStatus(_A)
_Ieee8021SrpReservationStreamId_Type=IEEE8021SrpStreamIdValue
_Ieee8021SrpReservationStreamId_Object=MibTableColumn
ieee8021SrpReservationStreamId=_Ieee8021SrpReservationStreamId_Object((1,3,111,2,802,1,1,19,1,4,1,1,1),_Ieee8021SrpReservationStreamId_Type())
ieee8021SrpReservationStreamId.setMaxAccess(_I)
if mibBuilder.loadTexts:ieee8021SrpReservationStreamId.setStatus(_A)
_Ieee8021SrpReservationDirection_Type=IEEE8021SrpReservationDirectionValue
_Ieee8021SrpReservationDirection_Object=MibTableColumn
ieee8021SrpReservationDirection=_Ieee8021SrpReservationDirection_Object((1,3,111,2,802,1,1,19,1,4,1,1,2),_Ieee8021SrpReservationDirection_Type())
ieee8021SrpReservationDirection.setMaxAccess(_I)
if mibBuilder.loadTexts:ieee8021SrpReservationDirection.setStatus(_A)
_Ieee8021SrpReservationDeclarationType_Type=IEEE8021SrpReservationDeclarationTypeValue
_Ieee8021SrpReservationDeclarationType_Object=MibTableColumn
ieee8021SrpReservationDeclarationType=_Ieee8021SrpReservationDeclarationType_Object((1,3,111,2,802,1,1,19,1,4,1,1,3),_Ieee8021SrpReservationDeclarationType_Type())
ieee8021SrpReservationDeclarationType.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpReservationDeclarationType.setStatus(_A)
_Ieee8021SrpReservationAccumulatedLatency_Type=Unsigned32
_Ieee8021SrpReservationAccumulatedLatency_Object=MibTableColumn
ieee8021SrpReservationAccumulatedLatency=_Ieee8021SrpReservationAccumulatedLatency_Object((1,3,111,2,802,1,1,19,1,4,1,1,4),_Ieee8021SrpReservationAccumulatedLatency_Type())
ieee8021SrpReservationAccumulatedLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpReservationAccumulatedLatency.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SrpReservationAccumulatedLatency.setUnits(_L)
class _Ieee8021SrpReservationFailureSystemId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_Ieee8021SrpReservationFailureSystemId_Type.__name__=_S
_Ieee8021SrpReservationFailureSystemId_Object=MibTableColumn
ieee8021SrpReservationFailureSystemId=_Ieee8021SrpReservationFailureSystemId_Object((1,3,111,2,802,1,1,19,1,4,1,1,5),_Ieee8021SrpReservationFailureSystemId_Type())
ieee8021SrpReservationFailureSystemId.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpReservationFailureSystemId.setStatus(_A)
_Ieee8021SrpReservationFailureCode_Type=IEEE8021SrpReservationFailureCodeValue
_Ieee8021SrpReservationFailureCode_Object=MibTableColumn
ieee8021SrpReservationFailureCode=_Ieee8021SrpReservationFailureCode_Object((1,3,111,2,802,1,1,19,1,4,1,1,6),_Ieee8021SrpReservationFailureCode_Type())
ieee8021SrpReservationFailureCode.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpReservationFailureCode.setStatus(_A)
_Ieee8021SrpReservationDroppedStreamFrames_Type=Counter64
_Ieee8021SrpReservationDroppedStreamFrames_Object=MibTableColumn
ieee8021SrpReservationDroppedStreamFrames=_Ieee8021SrpReservationDroppedStreamFrames_Object((1,3,111,2,802,1,1,19,1,4,1,1,7),_Ieee8021SrpReservationDroppedStreamFrames_Type())
ieee8021SrpReservationDroppedStreamFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpReservationDroppedStreamFrames.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SrpReservationDroppedStreamFrames.setUnits('frames')
_Ieee8021SrpReservationStreamAge_Type=Unsigned32
_Ieee8021SrpReservationStreamAge_Object=MibTableColumn
ieee8021SrpReservationStreamAge=_Ieee8021SrpReservationStreamAge_Object((1,3,111,2,802,1,1,19,1,4,1,1,8),_Ieee8021SrpReservationStreamAge_Type())
ieee8021SrpReservationStreamAge.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021SrpReservationStreamAge.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SrpReservationStreamAge.setUnits('seconds')
_Ieee8021SrpReservationsPreloadTable_Object=MibTable
ieee8021SrpReservationsPreloadTable=_Ieee8021SrpReservationsPreloadTable_Object((1,3,111,2,802,1,1,19,1,4,2))
if mibBuilder.loadTexts:ieee8021SrpReservationsPreloadTable.setStatus(_A)
_Ieee8021SrpReservationsPreloadEntry_Object=MibTableRow
ieee8021SrpReservationsPreloadEntry=_Ieee8021SrpReservationsPreloadEntry_Object((1,3,111,2,802,1,1,19,1,4,2,1))
ieee8021SrpReservationsPreloadEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_F,_J),(0,_F,_K))
if mibBuilder.loadTexts:ieee8021SrpReservationsPreloadEntry.setStatus(_A)
_Ieee8021SrpReservationsPreloadStreamId_Type=IEEE8021SrpStreamIdValue
_Ieee8021SrpReservationsPreloadStreamId_Object=MibTableColumn
ieee8021SrpReservationsPreloadStreamId=_Ieee8021SrpReservationsPreloadStreamId_Object((1,3,111,2,802,1,1,19,1,4,2,1,1),_Ieee8021SrpReservationsPreloadStreamId_Type())
ieee8021SrpReservationsPreloadStreamId.setMaxAccess(_I)
if mibBuilder.loadTexts:ieee8021SrpReservationsPreloadStreamId.setStatus(_A)
_Ieee8021SrpReservationPreloadDirection_Type=IEEE8021SrpReservationDirectionValue
_Ieee8021SrpReservationPreloadDirection_Object=MibTableColumn
ieee8021SrpReservationPreloadDirection=_Ieee8021SrpReservationPreloadDirection_Object((1,3,111,2,802,1,1,19,1,4,2,1,2),_Ieee8021SrpReservationPreloadDirection_Type())
ieee8021SrpReservationPreloadDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021SrpReservationPreloadDirection.setStatus(_A)
_Ieee8021SrpReservationPreloadAccumulatedLatency_Type=Unsigned32
_Ieee8021SrpReservationPreloadAccumulatedLatency_Object=MibTableColumn
ieee8021SrpReservationPreloadAccumulatedLatency=_Ieee8021SrpReservationPreloadAccumulatedLatency_Object((1,3,111,2,802,1,1,19,1,4,2,1,3),_Ieee8021SrpReservationPreloadAccumulatedLatency_Type())
ieee8021SrpReservationPreloadAccumulatedLatency.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021SrpReservationPreloadAccumulatedLatency.setStatus(_A)
if mibBuilder.loadTexts:ieee8021SrpReservationPreloadAccumulatedLatency.setUnits(_L)
_Ieee8021SrpConformance_ObjectIdentity=ObjectIdentity
ieee8021SrpConformance=_Ieee8021SrpConformance_ObjectIdentity((1,3,111,2,802,1,1,19,2))
_Ieee8021SrpCompliances_ObjectIdentity=ObjectIdentity
ieee8021SrpCompliances=_Ieee8021SrpCompliances_ObjectIdentity((1,3,111,2,802,1,1,19,2,1))
_Ieee8021SrpGroups_ObjectIdentity=ObjectIdentity
ieee8021SrpGroups=_Ieee8021SrpGroups_ObjectIdentity((1,3,111,2,802,1,1,19,2,2))
ieee8021BridgeBaseEntry.registerAugmentions((_B,_Y))
ieee8021SrpBridgeBaseEntry.setIndexNames(*ieee8021BridgeBaseEntry.getIndexNames())
ieee8021BridgeBasePortEntry.registerAugmentions((_B,_Z))
ieee8021SrpBridgePortEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())
ieee8021SrpConfigurationGroup=ObjectGroup((1,3,111,2,802,1,1,19,2,2,1))
ieee8021SrpConfigurationGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_P),(_B,_Q),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_R)))
if mibBuilder.loadTexts:ieee8021SrpConfigurationGroup.setStatus(_A)
ieee8021SrpLatencyGroup=ObjectGroup((1,3,111,2,802,1,1,19,2,2,2))
ieee8021SrpLatencyGroup.setObjects((_B,_i))
if mibBuilder.loadTexts:ieee8021SrpLatencyGroup.setStatus(_A)
ieee8021SrpStreamsGroup=ObjectGroup((1,3,111,2,802,1,1,19,2,2,3))
ieee8021SrpStreamsGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ieee8021SrpStreamsGroup.setStatus(_A)
ieee8021SrpReservationsGroup=ObjectGroup((1,3,111,2,802,1,1,19,2,2,4))
ieee8021SrpReservationsGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ieee8021SrpReservationsGroup.setStatus(_A)
ieee8021SrpConfigurationPruningGroup=ObjectGroup((1,3,111,2,802,1,1,19,2,2,5))
ieee8021SrpConfigurationPruningGroup.setObjects(*((_B,_P),(_B,_R)))
if mibBuilder.loadTexts:ieee8021SrpConfigurationPruningGroup.setStatus(_A)
ieee8021SrpMonitoringSRclassesGroup=ObjectGroup((1,3,111,2,802,1,1,19,2,2,6))
ieee8021SrpMonitoringSRclassesGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:ieee8021SrpMonitoringSRclassesGroup.setStatus(_A)
ieee8021SrpStreamsPreloadGroup=ObjectGroup((1,3,111,2,802,1,1,19,2,2,7))
ieee8021SrpStreamsPreloadGroup.setObjects(*((_B,_M),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:ieee8021SrpStreamsPreloadGroup.setStatus(_A)
ieee8021SrpReservationsPreloadGroup=ObjectGroup((1,3,111,2,802,1,1,19,2,2,8))
ieee8021SrpReservationsPreloadGroup.setObjects(*((_B,_N),(_B,_O),(_B,_A1)))
if mibBuilder.loadTexts:ieee8021SrpReservationsPreloadGroup.setStatus(_A)
ieee8021SrpCompliance=ModuleCompliance((1,3,111,2,802,1,1,19,2,1,1))
ieee8021SrpCompliance.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:ieee8021SrpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IEEE8021SrpStreamRankValue':IEEE8021SrpStreamRankValue,'IEEE8021SrpStreamIdValue':IEEE8021SrpStreamIdValue,'IEEE8021SrpReservationDirectionValue':IEEE8021SrpReservationDirectionValue,'IEEE8021SrpReservationDeclarationTypeValue':IEEE8021SrpReservationDeclarationTypeValue,'IEEE8021SrpReservationFailureCodeValue':IEEE8021SrpReservationFailureCodeValue,'ieee8021SrpMib':ieee8021SrpMib,'ieee8021SrpNotifications':ieee8021SrpNotifications,'ieee8021SrpObjects':ieee8021SrpObjects,'ieee8021SrpConfiguration':ieee8021SrpConfiguration,'ieee8021SrpBridgeBaseTable':ieee8021SrpBridgeBaseTable,_Y:ieee8021SrpBridgeBaseEntry,_a:ieee8021SrpBridgeBaseMsrpEnabledStatus,_b:ieee8021SrpBridgeBaseMsrpTalkerPruning,_c:ieee8021SrpBridgeBaseMsrpMaxFanInPorts,_d:ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize,_P:ieee8021SrpBridgeBaseMsrpTalkerVlanPruning,_Q:ieee8021SrpBridgeBaseMsrpMaxSRClasses,'ieee8021SrpBridgePortTable':ieee8021SrpBridgePortTable,_Z:ieee8021SrpBridgePortEntry,_e:ieee8021SrpBridgePortMsrpEnabledStatus,_f:ieee8021SrpBridgePortMsrpFailedRegistrations,_g:ieee8021SrpBridgePortMsrpLastPduOrigin,_h:ieee8021SrpBridgePortSrPvid,_R:ieee8021SrpBridgePortMsrpTalkerPrunningPerPort,'ieee8021SrpLatency':ieee8021SrpLatency,'ieee8021SrpLatencyTable':ieee8021SrpLatencyTable,'ieee8021SrpLatencyEntry':ieee8021SrpLatencyEntry,_U:ieee8021SrpTrafficClass,_i:ieee8021SrpPortTcLatency,'ieee8021SrpStreams':ieee8021SrpStreams,'ieee8021SrpStreamTable':ieee8021SrpStreamTable,'ieee8021SrpStreamEntry':ieee8021SrpStreamEntry,_V:ieee8021SrpStreamId,_j:ieee8021SrpStreamDestinationAddress,_k:ieee8021SrpStreamVlanId,_l:ieee8021SrpStreamTspecMaxFrameSize,_m:ieee8021SrpStreamTspecMaxIntervalFrames,_n:ieee8021SrpStreamDataFramePriority,_o:ieee8021SrpStreamRank,'ieee8021SrpStreamPreloadTable':ieee8021SrpStreamPreloadTable,'ieee8021SrpStreamPreloadEntry':ieee8021SrpStreamPreloadEntry,_M:ieee8021SrpStreamPreloadId,_v:ieee8021SrpStreamPreloadDestinationAddress,_w:ieee8021SrpStreamPreloadVlanId,_x:ieee8021SrpStreamPreloadTspecMaxFrameSize,_y:ieee8021SrpStreamPreloadTspecMaxIntervalFrames,_z:ieee8021SrpStreamPreloadDataFramePriority,_A0:ieee8021SrpStreamPreloadRank,'ieee8021SrpReservations':ieee8021SrpReservations,'ieee8021SrpReservationsTable':ieee8021SrpReservationsTable,'ieee8021SrpReservationsEntry':ieee8021SrpReservationsEntry,_W:ieee8021SrpReservationStreamId,_X:ieee8021SrpReservationDirection,_p:ieee8021SrpReservationDeclarationType,_q:ieee8021SrpReservationAccumulatedLatency,_r:ieee8021SrpReservationFailureSystemId,_s:ieee8021SrpReservationFailureCode,_t:ieee8021SrpReservationDroppedStreamFrames,_u:ieee8021SrpReservationStreamAge,'ieee8021SrpReservationsPreloadTable':ieee8021SrpReservationsPreloadTable,'ieee8021SrpReservationsPreloadEntry':ieee8021SrpReservationsPreloadEntry,_N:ieee8021SrpReservationsPreloadStreamId,_O:ieee8021SrpReservationPreloadDirection,_A1:ieee8021SrpReservationPreloadAccumulatedLatency,'ieee8021SrpConformance':ieee8021SrpConformance,'ieee8021SrpCompliances':ieee8021SrpCompliances,'ieee8021SrpCompliance':ieee8021SrpCompliance,'ieee8021SrpGroups':ieee8021SrpGroups,_A2:ieee8021SrpConfigurationGroup,_A3:ieee8021SrpLatencyGroup,_A4:ieee8021SrpStreamsGroup,_A5:ieee8021SrpReservationsGroup,_A6:ieee8021SrpConfigurationPruningGroup,_A7:ieee8021SrpMonitoringSRclassesGroup,_A8:ieee8021SrpStreamsPreloadGroup,_A9:ieee8021SrpReservationsPreloadGroup})