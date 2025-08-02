_k='mpConferenceGroup'
_j='mpConfigGroup'
_i='mpConferenceGlobalVideoMixTerminalIdentifier'
_h='mpConferenceGlobalAudioMixTerminalIdentifier'
_g='mpConferenceParticipantsFullPictureCounter'
_f='mpConferenceParticipantsVideoResolution'
_e='mpConferenceParticipantsVideoFrameRate'
_d='mpConferenceParticipantsSilencePacketsGenerated'
_c='mpConferenceParticipantsReceivedSilencePackets'
_b='mpConferenceParticipantsLateAudioPacketsDropped'
_a='mpConferenceParticipantsTotalPacketsReceived'
_Z='mpConferenceParticipantsTotalPacketsTransmitted'
_Y='mpConferenceParticipantsMaxAudioDecoderPayloadSize'
_X='mpConferenceParticipantsMaxAudioEncoderPayloadSize'
_W='mpConferenceParticipantsOutputAudioGain'
_V='mpConferenceParticipantsInputAudioGain'
_U='mpConferenceParticipantsVoiceActivity'
_T='mpConferenceParticipantsLoudnessMeasurement'
_S='mpConferenceParticipantsReceiveVideoState'
_R='mpConferenceParticipantsTransmitVideoState'
_Q='mpConferenceParticipantsReceiveAudioState'
_P='mpConferenceParticipantsTransmitAudioState'
_O='mpConferenceParticipantsEndpointId'
_N='mpConferenceLipSyncEnable'
_M='mpConferenceAudioNoiseThreshold'
_L='mpConfigMaxVideoMixCount'
_K='mpConfigMaxAudioMixCount'
_J='mpConferenceGlobalVideoMixTableIndex'
_I='mpConferenceGlobalAudioMixTableIndex'
_H='normal'
_G='mpConferenceParticipantsTableIndex'
_F='off'
_E='mpConferenceConferenceId'
_D='Integer32'
_C='read-only'
_B='MP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MmEndpointID,MmGatekeeperID,MmGlobalIdentifier,MmTAddressTag=mibBuilder.importSymbols('MULTI-MEDIA-MIB-TC','MmEndpointID','MmGatekeeperID','MmGlobalIdentifier','MmTAddressTag')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TAddress','TextualConvention','TruthValue')
h323MP=ModuleIdentity((1,3,6,1,4,1,3011,2,2))
_Media_ObjectIdentity=ObjectIdentity
media=_Media_ObjectIdentity((1,3,6,1,4,1,3011,2))
_MpConfig_ObjectIdentity=ObjectIdentity
mpConfig=_MpConfig_ObjectIdentity((1,3,6,1,4,1,3011,2,2,1))
_MpConfigMaxAudioMixCount_Type=Integer32
_MpConfigMaxAudioMixCount_Object=MibScalar
mpConfigMaxAudioMixCount=_MpConfigMaxAudioMixCount_Object((1,3,6,1,4,1,3011,2,2,1,1),_MpConfigMaxAudioMixCount_Type())
mpConfigMaxAudioMixCount.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConfigMaxAudioMixCount.setStatus(_A)
_MpConfigMaxVideoMixCount_Type=Integer32
_MpConfigMaxVideoMixCount_Object=MibScalar
mpConfigMaxVideoMixCount=_MpConfigMaxVideoMixCount_Object((1,3,6,1,4,1,3011,2,2,1,2),_MpConfigMaxVideoMixCount_Type())
mpConfigMaxVideoMixCount.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConfigMaxVideoMixCount.setStatus(_A)
_MpConference_ObjectIdentity=ObjectIdentity
mpConference=_MpConference_ObjectIdentity((1,3,6,1,4,1,3011,2,2,2))
_MpConferenceTable_Object=MibTable
mpConferenceTable=_MpConferenceTable_Object((1,3,6,1,4,1,3011,2,2,2,1))
if mibBuilder.loadTexts:mpConferenceTable.setStatus(_A)
_MpConferenceTableEntry_Object=MibTableRow
mpConferenceTableEntry=_MpConferenceTableEntry_Object((1,3,6,1,4,1,3011,2,2,2,1,1))
mpConferenceTableEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:mpConferenceTableEntry.setStatus(_A)
_MpConferenceConferenceId_Type=MmGlobalIdentifier
_MpConferenceConferenceId_Object=MibTableColumn
mpConferenceConferenceId=_MpConferenceConferenceId_Object((1,3,6,1,4,1,3011,2,2,2,1,1,1),_MpConferenceConferenceId_Type())
mpConferenceConferenceId.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceConferenceId.setStatus(_A)
_MpConferenceAudioNoiseThreshold_Type=Integer32
_MpConferenceAudioNoiseThreshold_Object=MibTableColumn
mpConferenceAudioNoiseThreshold=_MpConferenceAudioNoiseThreshold_Object((1,3,6,1,4,1,3011,2,2,2,1,1,2),_MpConferenceAudioNoiseThreshold_Type())
mpConferenceAudioNoiseThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceAudioNoiseThreshold.setStatus(_A)
_MpConferenceLipSyncEnable_Type=TruthValue
_MpConferenceLipSyncEnable_Object=MibTableColumn
mpConferenceLipSyncEnable=_MpConferenceLipSyncEnable_Object((1,3,6,1,4,1,3011,2,2,2,1,1,3),_MpConferenceLipSyncEnable_Type())
mpConferenceLipSyncEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceLipSyncEnable.setStatus(_A)
_MpConferenceParticipantsTable_Object=MibTable
mpConferenceParticipantsTable=_MpConferenceParticipantsTable_Object((1,3,6,1,4,1,3011,2,2,2,2))
if mibBuilder.loadTexts:mpConferenceParticipantsTable.setStatus(_A)
_MpConferenceParticipantsTableEntry_Object=MibTableRow
mpConferenceParticipantsTableEntry=_MpConferenceParticipantsTableEntry_Object((1,3,6,1,4,1,3011,2,2,2,2,1))
mpConferenceParticipantsTableEntry.setIndexNames((0,_B,_E),(0,_B,_G))
if mibBuilder.loadTexts:mpConferenceParticipantsTableEntry.setStatus(_A)
_MpConferenceParticipantsTableIndex_Type=Integer32
_MpConferenceParticipantsTableIndex_Object=MibTableColumn
mpConferenceParticipantsTableIndex=_MpConferenceParticipantsTableIndex_Object((1,3,6,1,4,1,3011,2,2,2,2,1,1),_MpConferenceParticipantsTableIndex_Type())
mpConferenceParticipantsTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsTableIndex.setStatus(_A)
_MpConferenceParticipantsEndpointId_Type=MmEndpointID
_MpConferenceParticipantsEndpointId_Object=MibTableColumn
mpConferenceParticipantsEndpointId=_MpConferenceParticipantsEndpointId_Object((1,3,6,1,4,1,3011,2,2,2,2,1,2),_MpConferenceParticipantsEndpointId_Type())
mpConferenceParticipantsEndpointId.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsEndpointId.setStatus(_A)
class _MpConferenceParticipantsTransmitAudioState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('mute',2),('toneGeneration',3),(_F,4)))
_MpConferenceParticipantsTransmitAudioState_Type.__name__=_D
_MpConferenceParticipantsTransmitAudioState_Object=MibTableColumn
mpConferenceParticipantsTransmitAudioState=_MpConferenceParticipantsTransmitAudioState_Object((1,3,6,1,4,1,3011,2,2,2,2,1,3),_MpConferenceParticipantsTransmitAudioState_Type())
mpConferenceParticipantsTransmitAudioState.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsTransmitAudioState.setStatus(_A)
class _MpConferenceParticipantsReceiveAudioState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('loopBack',2),('block',3),(_F,4)))
_MpConferenceParticipantsReceiveAudioState_Type.__name__=_D
_MpConferenceParticipantsReceiveAudioState_Object=MibTableColumn
mpConferenceParticipantsReceiveAudioState=_MpConferenceParticipantsReceiveAudioState_Object((1,3,6,1,4,1,3011,2,2,2,2,1,4),_MpConferenceParticipantsReceiveAudioState_Type())
mpConferenceParticipantsReceiveAudioState.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsReceiveAudioState.setStatus(_A)
class _MpConferenceParticipantsTransmitVideoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_F,2)))
_MpConferenceParticipantsTransmitVideoState_Type.__name__=_D
_MpConferenceParticipantsTransmitVideoState_Object=MibTableColumn
mpConferenceParticipantsTransmitVideoState=_MpConferenceParticipantsTransmitVideoState_Object((1,3,6,1,4,1,3011,2,2,2,2,1,5),_MpConferenceParticipantsTransmitVideoState_Type())
mpConferenceParticipantsTransmitVideoState.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsTransmitVideoState.setStatus(_A)
class _MpConferenceParticipantsReceiveVideoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('block',2),(_F,3)))
_MpConferenceParticipantsReceiveVideoState_Type.__name__=_D
_MpConferenceParticipantsReceiveVideoState_Object=MibTableColumn
mpConferenceParticipantsReceiveVideoState=_MpConferenceParticipantsReceiveVideoState_Object((1,3,6,1,4,1,3011,2,2,2,2,1,6),_MpConferenceParticipantsReceiveVideoState_Type())
mpConferenceParticipantsReceiveVideoState.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsReceiveVideoState.setStatus(_A)
_MpConferenceParticipantsLoudnessMeasurement_Type=Integer32
_MpConferenceParticipantsLoudnessMeasurement_Object=MibTableColumn
mpConferenceParticipantsLoudnessMeasurement=_MpConferenceParticipantsLoudnessMeasurement_Object((1,3,6,1,4,1,3011,2,2,2,2,1,7),_MpConferenceParticipantsLoudnessMeasurement_Type())
mpConferenceParticipantsLoudnessMeasurement.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsLoudnessMeasurement.setStatus(_A)
_MpConferenceParticipantsVoiceActivity_Type=TruthValue
_MpConferenceParticipantsVoiceActivity_Object=MibTableColumn
mpConferenceParticipantsVoiceActivity=_MpConferenceParticipantsVoiceActivity_Object((1,3,6,1,4,1,3011,2,2,2,2,1,8),_MpConferenceParticipantsVoiceActivity_Type())
mpConferenceParticipantsVoiceActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsVoiceActivity.setStatus(_A)
_MpConferenceParticipantsInputAudioGain_Type=Integer32
_MpConferenceParticipantsInputAudioGain_Object=MibTableColumn
mpConferenceParticipantsInputAudioGain=_MpConferenceParticipantsInputAudioGain_Object((1,3,6,1,4,1,3011,2,2,2,2,1,9),_MpConferenceParticipantsInputAudioGain_Type())
mpConferenceParticipantsInputAudioGain.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsInputAudioGain.setStatus(_A)
_MpConferenceParticipantsOutputAudioGain_Type=Integer32
_MpConferenceParticipantsOutputAudioGain_Object=MibTableColumn
mpConferenceParticipantsOutputAudioGain=_MpConferenceParticipantsOutputAudioGain_Object((1,3,6,1,4,1,3011,2,2,2,2,1,10),_MpConferenceParticipantsOutputAudioGain_Type())
mpConferenceParticipantsOutputAudioGain.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsOutputAudioGain.setStatus(_A)
_MpConferenceParticipantsMaxAudioEncoderPayloadSize_Type=Integer32
_MpConferenceParticipantsMaxAudioEncoderPayloadSize_Object=MibTableColumn
mpConferenceParticipantsMaxAudioEncoderPayloadSize=_MpConferenceParticipantsMaxAudioEncoderPayloadSize_Object((1,3,6,1,4,1,3011,2,2,2,2,1,11),_MpConferenceParticipantsMaxAudioEncoderPayloadSize_Type())
mpConferenceParticipantsMaxAudioEncoderPayloadSize.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsMaxAudioEncoderPayloadSize.setStatus(_A)
_MpConferenceParticipantsMaxAudioDecoderPayloadSize_Type=Integer32
_MpConferenceParticipantsMaxAudioDecoderPayloadSize_Object=MibTableColumn
mpConferenceParticipantsMaxAudioDecoderPayloadSize=_MpConferenceParticipantsMaxAudioDecoderPayloadSize_Object((1,3,6,1,4,1,3011,2,2,2,2,1,12),_MpConferenceParticipantsMaxAudioDecoderPayloadSize_Type())
mpConferenceParticipantsMaxAudioDecoderPayloadSize.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsMaxAudioDecoderPayloadSize.setStatus(_A)
_MpConferenceParticipantsTotalPacketsTransmitted_Type=Counter32
_MpConferenceParticipantsTotalPacketsTransmitted_Object=MibTableColumn
mpConferenceParticipantsTotalPacketsTransmitted=_MpConferenceParticipantsTotalPacketsTransmitted_Object((1,3,6,1,4,1,3011,2,2,2,2,1,13),_MpConferenceParticipantsTotalPacketsTransmitted_Type())
mpConferenceParticipantsTotalPacketsTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsTotalPacketsTransmitted.setStatus(_A)
_MpConferenceParticipantsTotalPacketsReceived_Type=Counter32
_MpConferenceParticipantsTotalPacketsReceived_Object=MibTableColumn
mpConferenceParticipantsTotalPacketsReceived=_MpConferenceParticipantsTotalPacketsReceived_Object((1,3,6,1,4,1,3011,2,2,2,2,1,14),_MpConferenceParticipantsTotalPacketsReceived_Type())
mpConferenceParticipantsTotalPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsTotalPacketsReceived.setStatus(_A)
_MpConferenceParticipantsInvalidPacketErrors_Type=Counter32
_MpConferenceParticipantsInvalidPacketErrors_Object=MibTableColumn
mpConferenceParticipantsInvalidPacketErrors=_MpConferenceParticipantsInvalidPacketErrors_Object((1,3,6,1,4,1,3011,2,2,2,2,1,15),_MpConferenceParticipantsInvalidPacketErrors_Type())
mpConferenceParticipantsInvalidPacketErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsInvalidPacketErrors.setStatus(_A)
_MpConferenceParticipantsLateAudioPacketsDropped_Type=Counter32
_MpConferenceParticipantsLateAudioPacketsDropped_Object=MibTableColumn
mpConferenceParticipantsLateAudioPacketsDropped=_MpConferenceParticipantsLateAudioPacketsDropped_Object((1,3,6,1,4,1,3011,2,2,2,2,1,16),_MpConferenceParticipantsLateAudioPacketsDropped_Type())
mpConferenceParticipantsLateAudioPacketsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsLateAudioPacketsDropped.setStatus(_A)
_MpConferenceParticipantsReceivedSilencePackets_Type=Counter32
_MpConferenceParticipantsReceivedSilencePackets_Object=MibTableColumn
mpConferenceParticipantsReceivedSilencePackets=_MpConferenceParticipantsReceivedSilencePackets_Object((1,3,6,1,4,1,3011,2,2,2,2,1,17),_MpConferenceParticipantsReceivedSilencePackets_Type())
mpConferenceParticipantsReceivedSilencePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsReceivedSilencePackets.setStatus(_A)
_MpConferenceParticipantsSilencePacketsGenerated_Type=Counter32
_MpConferenceParticipantsSilencePacketsGenerated_Object=MibTableColumn
mpConferenceParticipantsSilencePacketsGenerated=_MpConferenceParticipantsSilencePacketsGenerated_Object((1,3,6,1,4,1,3011,2,2,2,2,1,18),_MpConferenceParticipantsSilencePacketsGenerated_Type())
mpConferenceParticipantsSilencePacketsGenerated.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsSilencePacketsGenerated.setStatus(_A)
_MpConferenceParticipantsVideoFrameRate_Type=Integer32
_MpConferenceParticipantsVideoFrameRate_Object=MibTableColumn
mpConferenceParticipantsVideoFrameRate=_MpConferenceParticipantsVideoFrameRate_Object((1,3,6,1,4,1,3011,2,2,2,2,1,19),_MpConferenceParticipantsVideoFrameRate_Type())
mpConferenceParticipantsVideoFrameRate.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsVideoFrameRate.setStatus(_A)
class _MpConferenceParticipantsVideoResolution_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('h263SubQCIF',1),('h263QCIF',2),('h263CIF',3),('h2634CIF',4),('h26316CIF',5),('h263Reserved',6),('h261QCIF',7),('h261CIF',8)))
_MpConferenceParticipantsVideoResolution_Type.__name__=_D
_MpConferenceParticipantsVideoResolution_Object=MibTableColumn
mpConferenceParticipantsVideoResolution=_MpConferenceParticipantsVideoResolution_Object((1,3,6,1,4,1,3011,2,2,2,2,1,20),_MpConferenceParticipantsVideoResolution_Type())
mpConferenceParticipantsVideoResolution.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsVideoResolution.setStatus(_A)
_MpConferenceParticipantsFullPictureCounter_Type=Integer32
_MpConferenceParticipantsFullPictureCounter_Object=MibTableColumn
mpConferenceParticipantsFullPictureCounter=_MpConferenceParticipantsFullPictureCounter_Object((1,3,6,1,4,1,3011,2,2,2,2,1,21),_MpConferenceParticipantsFullPictureCounter_Type())
mpConferenceParticipantsFullPictureCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceParticipantsFullPictureCounter.setStatus(_A)
_MpConferenceGlobalAudioMixTable_Object=MibTable
mpConferenceGlobalAudioMixTable=_MpConferenceGlobalAudioMixTable_Object((1,3,6,1,4,1,3011,2,2,2,3))
if mibBuilder.loadTexts:mpConferenceGlobalAudioMixTable.setStatus(_A)
_MpConferenceGlobalAudioMixTableEntry_Object=MibTableRow
mpConferenceGlobalAudioMixTableEntry=_MpConferenceGlobalAudioMixTableEntry_Object((1,3,6,1,4,1,3011,2,2,2,3,1))
mpConferenceGlobalAudioMixTableEntry.setIndexNames((0,_B,_E),(0,_B,_I))
if mibBuilder.loadTexts:mpConferenceGlobalAudioMixTableEntry.setStatus(_A)
_MpConferenceGlobalAudioMixTableIndex_Type=Integer32
_MpConferenceGlobalAudioMixTableIndex_Object=MibTableColumn
mpConferenceGlobalAudioMixTableIndex=_MpConferenceGlobalAudioMixTableIndex_Object((1,3,6,1,4,1,3011,2,2,2,3,1,1),_MpConferenceGlobalAudioMixTableIndex_Type())
mpConferenceGlobalAudioMixTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceGlobalAudioMixTableIndex.setStatus(_A)
_MpConferenceGlobalAudioMixTerminalIdentifier_Type=MmEndpointID
_MpConferenceGlobalAudioMixTerminalIdentifier_Object=MibTableColumn
mpConferenceGlobalAudioMixTerminalIdentifier=_MpConferenceGlobalAudioMixTerminalIdentifier_Object((1,3,6,1,4,1,3011,2,2,2,3,1,2),_MpConferenceGlobalAudioMixTerminalIdentifier_Type())
mpConferenceGlobalAudioMixTerminalIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceGlobalAudioMixTerminalIdentifier.setStatus(_A)
_MpConferenceGlobalVideoMixTable_Object=MibTable
mpConferenceGlobalVideoMixTable=_MpConferenceGlobalVideoMixTable_Object((1,3,6,1,4,1,3011,2,2,2,4))
if mibBuilder.loadTexts:mpConferenceGlobalVideoMixTable.setStatus(_A)
_MpConferenceGlobalVideoMixTableEntry_Object=MibTableRow
mpConferenceGlobalVideoMixTableEntry=_MpConferenceGlobalVideoMixTableEntry_Object((1,3,6,1,4,1,3011,2,2,2,4,1))
mpConferenceGlobalVideoMixTableEntry.setIndexNames((0,_B,_E),(0,_B,_J))
if mibBuilder.loadTexts:mpConferenceGlobalVideoMixTableEntry.setStatus(_A)
_MpConferenceGlobalVideoMixTableIndex_Type=Integer32
_MpConferenceGlobalVideoMixTableIndex_Object=MibTableColumn
mpConferenceGlobalVideoMixTableIndex=_MpConferenceGlobalVideoMixTableIndex_Object((1,3,6,1,4,1,3011,2,2,2,4,1,1),_MpConferenceGlobalVideoMixTableIndex_Type())
mpConferenceGlobalVideoMixTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceGlobalVideoMixTableIndex.setStatus(_A)
_MpConferenceGlobalVideoMixTerminalIdentifier_Type=MmEndpointID
_MpConferenceGlobalVideoMixTerminalIdentifier_Object=MibTableColumn
mpConferenceGlobalVideoMixTerminalIdentifier=_MpConferenceGlobalVideoMixTerminalIdentifier_Object((1,3,6,1,4,1,3011,2,2,2,4,1,2),_MpConferenceGlobalVideoMixTerminalIdentifier_Type())
mpConferenceGlobalVideoMixTerminalIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:mpConferenceGlobalVideoMixTerminalIdentifier.setStatus(_A)
_MpMIBConformance_ObjectIdentity=ObjectIdentity
mpMIBConformance=_MpMIBConformance_ObjectIdentity((1,3,6,1,4,1,3011,2,2,3))
_MpMIBGroups_ObjectIdentity=ObjectIdentity
mpMIBGroups=_MpMIBGroups_ObjectIdentity((1,3,6,1,4,1,3011,2,2,3,1))
mpConfigGroup=ObjectGroup((1,3,6,1,4,1,3011,2,2,3,1,1))
mpConfigGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:mpConfigGroup.setStatus(_A)
mpConferenceGroup=ObjectGroup((1,3,6,1,4,1,3011,2,2,3,1,2))
mpConferenceGroup.setObjects(*((_B,_E),(_B,_M),(_B,_N),(_B,_G),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_I),(_B,_h),(_B,_J),(_B,_i)))
if mibBuilder.loadTexts:mpConferenceGroup.setStatus(_A)
mpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3011,2,2,3,2))
mpMIBCompliance.setObjects(*((_B,_j),(_B,_k)))
if mibBuilder.loadTexts:mpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'media':media,'h323MP':h323MP,'mpConfig':mpConfig,_K:mpConfigMaxAudioMixCount,_L:mpConfigMaxVideoMixCount,'mpConference':mpConference,'mpConferenceTable':mpConferenceTable,'mpConferenceTableEntry':mpConferenceTableEntry,_E:mpConferenceConferenceId,_M:mpConferenceAudioNoiseThreshold,_N:mpConferenceLipSyncEnable,'mpConferenceParticipantsTable':mpConferenceParticipantsTable,'mpConferenceParticipantsTableEntry':mpConferenceParticipantsTableEntry,_G:mpConferenceParticipantsTableIndex,_O:mpConferenceParticipantsEndpointId,_P:mpConferenceParticipantsTransmitAudioState,_Q:mpConferenceParticipantsReceiveAudioState,_R:mpConferenceParticipantsTransmitVideoState,_S:mpConferenceParticipantsReceiveVideoState,_T:mpConferenceParticipantsLoudnessMeasurement,_U:mpConferenceParticipantsVoiceActivity,_V:mpConferenceParticipantsInputAudioGain,_W:mpConferenceParticipantsOutputAudioGain,_X:mpConferenceParticipantsMaxAudioEncoderPayloadSize,_Y:mpConferenceParticipantsMaxAudioDecoderPayloadSize,_Z:mpConferenceParticipantsTotalPacketsTransmitted,_a:mpConferenceParticipantsTotalPacketsReceived,'mpConferenceParticipantsInvalidPacketErrors':mpConferenceParticipantsInvalidPacketErrors,_b:mpConferenceParticipantsLateAudioPacketsDropped,_c:mpConferenceParticipantsReceivedSilencePackets,_d:mpConferenceParticipantsSilencePacketsGenerated,_e:mpConferenceParticipantsVideoFrameRate,_f:mpConferenceParticipantsVideoResolution,_g:mpConferenceParticipantsFullPictureCounter,'mpConferenceGlobalAudioMixTable':mpConferenceGlobalAudioMixTable,'mpConferenceGlobalAudioMixTableEntry':mpConferenceGlobalAudioMixTableEntry,_I:mpConferenceGlobalAudioMixTableIndex,_h:mpConferenceGlobalAudioMixTerminalIdentifier,'mpConferenceGlobalVideoMixTable':mpConferenceGlobalVideoMixTable,'mpConferenceGlobalVideoMixTableEntry':mpConferenceGlobalVideoMixTableEntry,_J:mpConferenceGlobalVideoMixTableIndex,_i:mpConferenceGlobalVideoMixTerminalIdentifier,'mpMIBConformance':mpMIBConformance,'mpMIBGroups':mpMIBGroups,_j:mpConfigGroup,_k:mpConferenceGroup,'mpMIBCompliance':mpMIBCompliance})