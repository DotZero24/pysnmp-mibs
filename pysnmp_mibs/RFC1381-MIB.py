_P='lapbXidIndex'
_O='lapbFlowIfIndex'
_N='lapbOperIndex'
_M='sendDISC'
_L='sendSABM'
_K='modulo128'
_J='modulo8'
_I='lapbAdmnIndex'
_H='other'
_G='RFC1381-MIB'
_F='PositiveInteger'
_E='OctetString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class PositiveInteger(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class IfIndexType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Lapb_ObjectIdentity=ObjectIdentity
lapb=_Lapb_ObjectIdentity((1,3,6,1,2,1,10,16))
_LapbAdmnTable_Object=MibTable
lapbAdmnTable=_LapbAdmnTable_Object((1,3,6,1,2,1,10,16,1))
if mibBuilder.loadTexts:lapbAdmnTable.setStatus(_A)
_LapbAdmnEntry_Object=MibTableRow
lapbAdmnEntry=_LapbAdmnEntry_Object((1,3,6,1,2,1,10,16,1,1))
lapbAdmnEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:lapbAdmnEntry.setStatus(_A)
_LapbAdmnIndex_Type=IfIndexType
_LapbAdmnIndex_Object=MibTableColumn
lapbAdmnIndex=_LapbAdmnIndex_Object((1,3,6,1,2,1,10,16,1,1,1),_LapbAdmnIndex_Type())
lapbAdmnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbAdmnIndex.setStatus(_A)
class _LapbAdmnStationType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dte',1),('dce',2),('dxe',3)))
_LapbAdmnStationType_Type.__name__=_D
_LapbAdmnStationType_Object=MibTableColumn
lapbAdmnStationType=_LapbAdmnStationType_Object((1,3,6,1,2,1,10,16,1,1,2),_LapbAdmnStationType_Type())
lapbAdmnStationType.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbAdmnStationType.setStatus(_A)
class _LapbAdmnControlField_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_LapbAdmnControlField_Type.__name__=_D
_LapbAdmnControlField_Object=MibTableColumn
lapbAdmnControlField=_LapbAdmnControlField_Object((1,3,6,1,2,1,10,16,1,1,3),_LapbAdmnControlField_Type())
lapbAdmnControlField.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbAdmnControlField.setStatus(_A)
class _LapbAdmnTransmitN1FrameSize_Type(PositiveInteger):defaultValue=36000
_LapbAdmnTransmitN1FrameSize_Type.__name__=_F
_LapbAdmnTransmitN1FrameSize_Object=MibTableColumn
lapbAdmnTransmitN1FrameSize=_LapbAdmnTransmitN1FrameSize_Object((1,3,6,1,2,1,10,16,1,1,4),_LapbAdmnTransmitN1FrameSize_Type())
lapbAdmnTransmitN1FrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbAdmnTransmitN1FrameSize.setStatus(_A)
class _LapbAdmnReceiveN1FrameSize_Type(PositiveInteger):defaultValue=36000
_LapbAdmnReceiveN1FrameSize_Type.__name__=_F
_LapbAdmnReceiveN1FrameSize_Object=MibTableColumn
lapbAdmnReceiveN1FrameSize=_LapbAdmnReceiveN1FrameSize_Object((1,3,6,1,2,1,10,16,1,1,5),_LapbAdmnReceiveN1FrameSize_Type())
lapbAdmnReceiveN1FrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbAdmnReceiveN1FrameSize.setStatus(_A)
class _LapbAdmnTransmitKWindowSize_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_LapbAdmnTransmitKWindowSize_Type.__name__=_D
_LapbAdmnTransmitKWindowSize_Object=MibTableColumn
lapbAdmnTransmitKWindowSize=_LapbAdmnTransmitKWindowSize_Object((1,3,6,1,2,1,10,16,1,1,6),_LapbAdmnTransmitKWindowSize_Type())
lapbAdmnTransmitKWindowSize.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbAdmnTransmitKWindowSize.setStatus(_A)
class _LapbAdmnReceiveKWindowSize_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_LapbAdmnReceiveKWindowSize_Type.__name__=_D
_LapbAdmnReceiveKWindowSize_Object=MibTableColumn
lapbAdmnReceiveKWindowSize=_LapbAdmnReceiveKWindowSize_Object((1,3,6,1,2,1,10,16,1,1,7),_LapbAdmnReceiveKWindowSize_Type())
lapbAdmnReceiveKWindowSize.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbAdmnReceiveKWindowSize.setStatus(_A)
class _LapbAdmnN2RxmitCount_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LapbAdmnN2RxmitCount_Type.__name__=_D
_LapbAdmnN2RxmitCount_Object=MibTableColumn
lapbAdmnN2RxmitCount=_LapbAdmnN2RxmitCount_Object((1,3,6,1,2,1,10,16,1,1,8),_LapbAdmnN2RxmitCount_Type())
lapbAdmnN2RxmitCount.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbAdmnN2RxmitCount.setStatus(_A)
class _LapbAdmnT1AckTimer_Type(PositiveInteger):defaultValue=3000
_LapbAdmnT1AckTimer_Type.__name__=_F
_LapbAdmnT1AckTimer_Object=MibTableColumn
lapbAdmnT1AckTimer=_LapbAdmnT1AckTimer_Object((1,3,6,1,2,1,10,16,1,1,9),_LapbAdmnT1AckTimer_Type())
lapbAdmnT1AckTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbAdmnT1AckTimer.setStatus(_A)
class _LapbAdmnT2AckDelayTimer_Type(PositiveInteger):defaultValue=0
_LapbAdmnT2AckDelayTimer_Type.__name__=_F
_LapbAdmnT2AckDelayTimer_Object=MibTableColumn
lapbAdmnT2AckDelayTimer=_LapbAdmnT2AckDelayTimer_Object((1,3,6,1,2,1,10,16,1,1,10),_LapbAdmnT2AckDelayTimer_Type())
lapbAdmnT2AckDelayTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbAdmnT2AckDelayTimer.setStatus(_A)
class _LapbAdmnT3DisconnectTimer_Type(PositiveInteger):defaultValue=60000
_LapbAdmnT3DisconnectTimer_Type.__name__=_F
_LapbAdmnT3DisconnectTimer_Object=MibTableColumn
lapbAdmnT3DisconnectTimer=_LapbAdmnT3DisconnectTimer_Object((1,3,6,1,2,1,10,16,1,1,11),_LapbAdmnT3DisconnectTimer_Type())
lapbAdmnT3DisconnectTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbAdmnT3DisconnectTimer.setStatus(_A)
class _LapbAdmnT4IdleTimer_Type(PositiveInteger):defaultValue=2147483647
_LapbAdmnT4IdleTimer_Type.__name__=_F
_LapbAdmnT4IdleTimer_Object=MibTableColumn
lapbAdmnT4IdleTimer=_LapbAdmnT4IdleTimer_Object((1,3,6,1,2,1,10,16,1,1,12),_LapbAdmnT4IdleTimer_Type())
lapbAdmnT4IdleTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbAdmnT4IdleTimer.setStatus(_A)
class _LapbAdmnActionInitiate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_M,2),('sendDM',3),('none',4),(_H,5)))
_LapbAdmnActionInitiate_Type.__name__=_D
_LapbAdmnActionInitiate_Object=MibTableColumn
lapbAdmnActionInitiate=_LapbAdmnActionInitiate_Object((1,3,6,1,2,1,10,16,1,1,13),_LapbAdmnActionInitiate_Type())
lapbAdmnActionInitiate.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbAdmnActionInitiate.setStatus(_A)
class _LapbAdmnActionRecvDM_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_H,3)))
_LapbAdmnActionRecvDM_Type.__name__=_D
_LapbAdmnActionRecvDM_Object=MibTableColumn
lapbAdmnActionRecvDM=_LapbAdmnActionRecvDM_Object((1,3,6,1,2,1,10,16,1,1,14),_LapbAdmnActionRecvDM_Type())
lapbAdmnActionRecvDM.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbAdmnActionRecvDM.setStatus(_A)
_LapbOperTable_Object=MibTable
lapbOperTable=_LapbOperTable_Object((1,3,6,1,2,1,10,16,2))
if mibBuilder.loadTexts:lapbOperTable.setStatus(_A)
_LapbOperEntry_Object=MibTableRow
lapbOperEntry=_LapbOperEntry_Object((1,3,6,1,2,1,10,16,2,1))
lapbOperEntry.setIndexNames((0,_G,_N))
if mibBuilder.loadTexts:lapbOperEntry.setStatus(_A)
_LapbOperIndex_Type=IfIndexType
_LapbOperIndex_Object=MibTableColumn
lapbOperIndex=_LapbOperIndex_Object((1,3,6,1,2,1,10,16,2,1,1),_LapbOperIndex_Type())
lapbOperIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbOperIndex.setStatus(_A)
class _LapbOperStationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dte',1),('dce',2),('dxe',3)))
_LapbOperStationType_Type.__name__=_D
_LapbOperStationType_Object=MibTableColumn
lapbOperStationType=_LapbOperStationType_Object((1,3,6,1,2,1,10,16,2,1,2),_LapbOperStationType_Type())
lapbOperStationType.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbOperStationType.setStatus(_A)
class _LapbOperControlField_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_LapbOperControlField_Type.__name__=_D
_LapbOperControlField_Object=MibTableColumn
lapbOperControlField=_LapbOperControlField_Object((1,3,6,1,2,1,10,16,2,1,3),_LapbOperControlField_Type())
lapbOperControlField.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbOperControlField.setStatus(_A)
_LapbOperTransmitN1FrameSize_Type=PositiveInteger
_LapbOperTransmitN1FrameSize_Object=MibTableColumn
lapbOperTransmitN1FrameSize=_LapbOperTransmitN1FrameSize_Object((1,3,6,1,2,1,10,16,2,1,4),_LapbOperTransmitN1FrameSize_Type())
lapbOperTransmitN1FrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbOperTransmitN1FrameSize.setStatus(_A)
_LapbOperReceiveN1FrameSize_Type=PositiveInteger
_LapbOperReceiveN1FrameSize_Object=MibTableColumn
lapbOperReceiveN1FrameSize=_LapbOperReceiveN1FrameSize_Object((1,3,6,1,2,1,10,16,2,1,5),_LapbOperReceiveN1FrameSize_Type())
lapbOperReceiveN1FrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbOperReceiveN1FrameSize.setStatus(_A)
class _LapbOperTransmitKWindowSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_LapbOperTransmitKWindowSize_Type.__name__=_D
_LapbOperTransmitKWindowSize_Object=MibTableColumn
lapbOperTransmitKWindowSize=_LapbOperTransmitKWindowSize_Object((1,3,6,1,2,1,10,16,2,1,6),_LapbOperTransmitKWindowSize_Type())
lapbOperTransmitKWindowSize.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbOperTransmitKWindowSize.setStatus(_A)
class _LapbOperReceiveKWindowSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_LapbOperReceiveKWindowSize_Type.__name__=_D
_LapbOperReceiveKWindowSize_Object=MibTableColumn
lapbOperReceiveKWindowSize=_LapbOperReceiveKWindowSize_Object((1,3,6,1,2,1,10,16,2,1,7),_LapbOperReceiveKWindowSize_Type())
lapbOperReceiveKWindowSize.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbOperReceiveKWindowSize.setStatus(_A)
class _LapbOperN2RxmitCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LapbOperN2RxmitCount_Type.__name__=_D
_LapbOperN2RxmitCount_Object=MibTableColumn
lapbOperN2RxmitCount=_LapbOperN2RxmitCount_Object((1,3,6,1,2,1,10,16,2,1,8),_LapbOperN2RxmitCount_Type())
lapbOperN2RxmitCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbOperN2RxmitCount.setStatus(_A)
_LapbOperT1AckTimer_Type=PositiveInteger
_LapbOperT1AckTimer_Object=MibTableColumn
lapbOperT1AckTimer=_LapbOperT1AckTimer_Object((1,3,6,1,2,1,10,16,2,1,9),_LapbOperT1AckTimer_Type())
lapbOperT1AckTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbOperT1AckTimer.setStatus(_A)
_LapbOperT2AckDelayTimer_Type=PositiveInteger
_LapbOperT2AckDelayTimer_Object=MibTableColumn
lapbOperT2AckDelayTimer=_LapbOperT2AckDelayTimer_Object((1,3,6,1,2,1,10,16,2,1,10),_LapbOperT2AckDelayTimer_Type())
lapbOperT2AckDelayTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbOperT2AckDelayTimer.setStatus(_A)
_LapbOperT3DisconnectTimer_Type=PositiveInteger
_LapbOperT3DisconnectTimer_Object=MibTableColumn
lapbOperT3DisconnectTimer=_LapbOperT3DisconnectTimer_Object((1,3,6,1,2,1,10,16,2,1,11),_LapbOperT3DisconnectTimer_Type())
lapbOperT3DisconnectTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbOperT3DisconnectTimer.setStatus(_A)
_LapbOperT4IdleTimer_Type=PositiveInteger
_LapbOperT4IdleTimer_Object=MibTableColumn
lapbOperT4IdleTimer=_LapbOperT4IdleTimer_Object((1,3,6,1,2,1,10,16,2,1,12),_LapbOperT4IdleTimer_Type())
lapbOperT4IdleTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbOperT4IdleTimer.setStatus(_A)
_LapbOperPortId_Type=ObjectIdentifier
_LapbOperPortId_Object=MibTableColumn
lapbOperPortId=_LapbOperPortId_Object((1,3,6,1,2,1,10,16,2,1,13),_LapbOperPortId_Type())
lapbOperPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbOperPortId.setStatus(_A)
_LapbOperProtocolVersionId_Type=ObjectIdentifier
_LapbOperProtocolVersionId_Object=MibTableColumn
lapbOperProtocolVersionId=_LapbOperProtocolVersionId_Object((1,3,6,1,2,1,10,16,2,1,14),_LapbOperProtocolVersionId_Type())
lapbOperProtocolVersionId.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbOperProtocolVersionId.setStatus(_A)
_LapbFlowTable_Object=MibTable
lapbFlowTable=_LapbFlowTable_Object((1,3,6,1,2,1,10,16,3))
if mibBuilder.loadTexts:lapbFlowTable.setStatus(_A)
_LapbFlowEntry_Object=MibTableRow
lapbFlowEntry=_LapbFlowEntry_Object((1,3,6,1,2,1,10,16,3,1))
lapbFlowEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:lapbFlowEntry.setStatus(_A)
_LapbFlowIfIndex_Type=IfIndexType
_LapbFlowIfIndex_Object=MibTableColumn
lapbFlowIfIndex=_LapbFlowIfIndex_Object((1,3,6,1,2,1,10,16,3,1,1),_LapbFlowIfIndex_Type())
lapbFlowIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbFlowIfIndex.setStatus(_A)
_LapbFlowStateChanges_Type=Counter32
_LapbFlowStateChanges_Object=MibTableColumn
lapbFlowStateChanges=_LapbFlowStateChanges_Object((1,3,6,1,2,1,10,16,3,1,2),_LapbFlowStateChanges_Type())
lapbFlowStateChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbFlowStateChanges.setStatus(_A)
class _LapbFlowChangeReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('notStarted',1),('abmEntered',2),('abmeEntered',3),('abmReset',4),('abmeReset',5),('dmReceived',6),('dmSent',7),('discReceived',8),('discSent',9),('frmrReceived',10),('frmrSent',11),('n2Timeout',12),(_H,13)))
_LapbFlowChangeReason_Type.__name__=_D
_LapbFlowChangeReason_Object=MibTableColumn
lapbFlowChangeReason=_LapbFlowChangeReason_Object((1,3,6,1,2,1,10,16,3,1,3),_LapbFlowChangeReason_Type())
lapbFlowChangeReason.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbFlowChangeReason.setStatus(_A)
class _LapbFlowCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('disconnected',1),('linkSetup',2),('frameReject',3),('disconnectRequest',4),('informationTransfer',5),('rejFrameSent',6),('waitingAcknowledgement',7),('stationBusy',8),('remoteStationBusy',9),('bothStationsBusy',10),('waitingAckStationBusy',11),('waitingAckRemoteBusy',12),('waitingAckBothBusy',13),('rejFrameSentRemoteBusy',14),('xidFrameSent',15),('error',16),(_H,17)))
_LapbFlowCurrentMode_Type.__name__=_D
_LapbFlowCurrentMode_Object=MibTableColumn
lapbFlowCurrentMode=_LapbFlowCurrentMode_Object((1,3,6,1,2,1,10,16,3,1,4),_LapbFlowCurrentMode_Type())
lapbFlowCurrentMode.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbFlowCurrentMode.setStatus(_A)
_LapbFlowBusyDefers_Type=Counter32
_LapbFlowBusyDefers_Object=MibTableColumn
lapbFlowBusyDefers=_LapbFlowBusyDefers_Object((1,3,6,1,2,1,10,16,3,1,5),_LapbFlowBusyDefers_Type())
lapbFlowBusyDefers.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbFlowBusyDefers.setStatus(_A)
_LapbFlowRejOutPkts_Type=Counter32
_LapbFlowRejOutPkts_Object=MibTableColumn
lapbFlowRejOutPkts=_LapbFlowRejOutPkts_Object((1,3,6,1,2,1,10,16,3,1,6),_LapbFlowRejOutPkts_Type())
lapbFlowRejOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbFlowRejOutPkts.setStatus(_A)
_LapbFlowRejInPkts_Type=Counter32
_LapbFlowRejInPkts_Object=MibTableColumn
lapbFlowRejInPkts=_LapbFlowRejInPkts_Object((1,3,6,1,2,1,10,16,3,1,7),_LapbFlowRejInPkts_Type())
lapbFlowRejInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbFlowRejInPkts.setStatus(_A)
_LapbFlowT1Timeouts_Type=Counter32
_LapbFlowT1Timeouts_Object=MibTableColumn
lapbFlowT1Timeouts=_LapbFlowT1Timeouts_Object((1,3,6,1,2,1,10,16,3,1,8),_LapbFlowT1Timeouts_Type())
lapbFlowT1Timeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbFlowT1Timeouts.setStatus(_A)
class _LapbFlowFrmrSent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_LapbFlowFrmrSent_Type.__name__=_E
_LapbFlowFrmrSent_Object=MibTableColumn
lapbFlowFrmrSent=_LapbFlowFrmrSent_Object((1,3,6,1,2,1,10,16,3,1,9),_LapbFlowFrmrSent_Type())
lapbFlowFrmrSent.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbFlowFrmrSent.setStatus(_A)
class _LapbFlowFrmrReceived_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_LapbFlowFrmrReceived_Type.__name__=_E
_LapbFlowFrmrReceived_Object=MibTableColumn
lapbFlowFrmrReceived=_LapbFlowFrmrReceived_Object((1,3,6,1,2,1,10,16,3,1,10),_LapbFlowFrmrReceived_Type())
lapbFlowFrmrReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbFlowFrmrReceived.setStatus(_A)
class _LapbFlowXidReceived_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8206))
_LapbFlowXidReceived_Type.__name__=_E
_LapbFlowXidReceived_Object=MibTableColumn
lapbFlowXidReceived=_LapbFlowXidReceived_Object((1,3,6,1,2,1,10,16,3,1,11),_LapbFlowXidReceived_Type())
lapbFlowXidReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbFlowXidReceived.setStatus(_A)
_LapbXidTable_Object=MibTable
lapbXidTable=_LapbXidTable_Object((1,3,6,1,2,1,10,16,4))
if mibBuilder.loadTexts:lapbXidTable.setStatus(_A)
_LapbXidEntry_Object=MibTableRow
lapbXidEntry=_LapbXidEntry_Object((1,3,6,1,2,1,10,16,4,1))
lapbXidEntry.setIndexNames((0,_G,_P))
if mibBuilder.loadTexts:lapbXidEntry.setStatus(_A)
_LapbXidIndex_Type=IfIndexType
_LapbXidIndex_Object=MibTableColumn
lapbXidIndex=_LapbXidIndex_Object((1,3,6,1,2,1,10,16,4,1,1),_LapbXidIndex_Type())
lapbXidIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lapbXidIndex.setStatus(_A)
class _LapbXidAdRIdentifier_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LapbXidAdRIdentifier_Type.__name__=_E
_LapbXidAdRIdentifier_Object=MibTableColumn
lapbXidAdRIdentifier=_LapbXidAdRIdentifier_Object((1,3,6,1,2,1,10,16,4,1,2),_LapbXidAdRIdentifier_Type())
lapbXidAdRIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbXidAdRIdentifier.setStatus(_A)
class _LapbXidAdRAddress_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LapbXidAdRAddress_Type.__name__=_E
_LapbXidAdRAddress_Object=MibTableColumn
lapbXidAdRAddress=_LapbXidAdRAddress_Object((1,3,6,1,2,1,10,16,4,1,3),_LapbXidAdRAddress_Type())
lapbXidAdRAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbXidAdRAddress.setStatus(_A)
class _LapbXidParameterUniqueIdentifier_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LapbXidParameterUniqueIdentifier_Type.__name__=_E
_LapbXidParameterUniqueIdentifier_Object=MibTableColumn
lapbXidParameterUniqueIdentifier=_LapbXidParameterUniqueIdentifier_Object((1,3,6,1,2,1,10,16,4,1,4),_LapbXidParameterUniqueIdentifier_Type())
lapbXidParameterUniqueIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbXidParameterUniqueIdentifier.setStatus(_A)
class _LapbXidGroupAddress_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LapbXidGroupAddress_Type.__name__=_E
_LapbXidGroupAddress_Object=MibTableColumn
lapbXidGroupAddress=_LapbXidGroupAddress_Object((1,3,6,1,2,1,10,16,4,1,5),_LapbXidGroupAddress_Type())
lapbXidGroupAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbXidGroupAddress.setStatus(_A)
class _LapbXidPortNumber_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LapbXidPortNumber_Type.__name__=_E
_LapbXidPortNumber_Object=MibTableColumn
lapbXidPortNumber=_LapbXidPortNumber_Object((1,3,6,1,2,1,10,16,4,1,6),_LapbXidPortNumber_Type())
lapbXidPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbXidPortNumber.setStatus(_A)
class _LapbXidUserDataSubfield_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8206))
_LapbXidUserDataSubfield_Type.__name__=_E
_LapbXidUserDataSubfield_Object=MibTableColumn
lapbXidUserDataSubfield=_LapbXidUserDataSubfield_Object((1,3,6,1,2,1,10,16,4,1,7),_LapbXidUserDataSubfield_Type())
lapbXidUserDataSubfield.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbXidUserDataSubfield.setStatus(_A)
_LapbProtocolVersion_ObjectIdentity=ObjectIdentity
lapbProtocolVersion=_LapbProtocolVersion_ObjectIdentity((1,3,6,1,2,1,10,16,5))
_LapbProtocolIso7776v1986_ObjectIdentity=ObjectIdentity
lapbProtocolIso7776v1986=_LapbProtocolIso7776v1986_ObjectIdentity((1,3,6,1,2,1,10,16,5,1))
_LapbProtocolCcittV1980_ObjectIdentity=ObjectIdentity
lapbProtocolCcittV1980=_LapbProtocolCcittV1980_ObjectIdentity((1,3,6,1,2,1,10,16,5,2))
_LapbProtocolCcittV1984_ObjectIdentity=ObjectIdentity
lapbProtocolCcittV1984=_LapbProtocolCcittV1984_ObjectIdentity((1,3,6,1,2,1,10,16,5,3))
mibBuilder.exportSymbols(_G,**{_F:PositiveInteger,'IfIndexType':IfIndexType,'lapb':lapb,'lapbAdmnTable':lapbAdmnTable,'lapbAdmnEntry':lapbAdmnEntry,_I:lapbAdmnIndex,'lapbAdmnStationType':lapbAdmnStationType,'lapbAdmnControlField':lapbAdmnControlField,'lapbAdmnTransmitN1FrameSize':lapbAdmnTransmitN1FrameSize,'lapbAdmnReceiveN1FrameSize':lapbAdmnReceiveN1FrameSize,'lapbAdmnTransmitKWindowSize':lapbAdmnTransmitKWindowSize,'lapbAdmnReceiveKWindowSize':lapbAdmnReceiveKWindowSize,'lapbAdmnN2RxmitCount':lapbAdmnN2RxmitCount,'lapbAdmnT1AckTimer':lapbAdmnT1AckTimer,'lapbAdmnT2AckDelayTimer':lapbAdmnT2AckDelayTimer,'lapbAdmnT3DisconnectTimer':lapbAdmnT3DisconnectTimer,'lapbAdmnT4IdleTimer':lapbAdmnT4IdleTimer,'lapbAdmnActionInitiate':lapbAdmnActionInitiate,'lapbAdmnActionRecvDM':lapbAdmnActionRecvDM,'lapbOperTable':lapbOperTable,'lapbOperEntry':lapbOperEntry,_N:lapbOperIndex,'lapbOperStationType':lapbOperStationType,'lapbOperControlField':lapbOperControlField,'lapbOperTransmitN1FrameSize':lapbOperTransmitN1FrameSize,'lapbOperReceiveN1FrameSize':lapbOperReceiveN1FrameSize,'lapbOperTransmitKWindowSize':lapbOperTransmitKWindowSize,'lapbOperReceiveKWindowSize':lapbOperReceiveKWindowSize,'lapbOperN2RxmitCount':lapbOperN2RxmitCount,'lapbOperT1AckTimer':lapbOperT1AckTimer,'lapbOperT2AckDelayTimer':lapbOperT2AckDelayTimer,'lapbOperT3DisconnectTimer':lapbOperT3DisconnectTimer,'lapbOperT4IdleTimer':lapbOperT4IdleTimer,'lapbOperPortId':lapbOperPortId,'lapbOperProtocolVersionId':lapbOperProtocolVersionId,'lapbFlowTable':lapbFlowTable,'lapbFlowEntry':lapbFlowEntry,_O:lapbFlowIfIndex,'lapbFlowStateChanges':lapbFlowStateChanges,'lapbFlowChangeReason':lapbFlowChangeReason,'lapbFlowCurrentMode':lapbFlowCurrentMode,'lapbFlowBusyDefers':lapbFlowBusyDefers,'lapbFlowRejOutPkts':lapbFlowRejOutPkts,'lapbFlowRejInPkts':lapbFlowRejInPkts,'lapbFlowT1Timeouts':lapbFlowT1Timeouts,'lapbFlowFrmrSent':lapbFlowFrmrSent,'lapbFlowFrmrReceived':lapbFlowFrmrReceived,'lapbFlowXidReceived':lapbFlowXidReceived,'lapbXidTable':lapbXidTable,'lapbXidEntry':lapbXidEntry,_P:lapbXidIndex,'lapbXidAdRIdentifier':lapbXidAdRIdentifier,'lapbXidAdRAddress':lapbXidAdRAddress,'lapbXidParameterUniqueIdentifier':lapbXidParameterUniqueIdentifier,'lapbXidGroupAddress':lapbXidGroupAddress,'lapbXidPortNumber':lapbXidPortNumber,'lapbXidUserDataSubfield':lapbXidUserDataSubfield,'lapbProtocolVersion':lapbProtocolVersion,'lapbProtocolIso7776v1986':lapbProtocolIso7776v1986,'lapbProtocolCcittV1980':lapbProtocolCcittV1980,'lapbProtocolCcittV1984':lapbProtocolCcittV1984})