_N='channelInterArrvJitter'
_M='channelPktsLost'
_L='voiceDspResetCount'
_K='channelId'
_J='milliseconds'
_I='zhoneSlotIndex'
_H='zhoneShelfIndex'
_G='ZHONE-COM-VOICE-DSP-MIB'
_F='Unsigned32'
_E='read-write'
_D='Integer32'
_C='Zhone'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zhoneModules,zhoneShelfIndex,zhoneSlotIndex,zhoneVoice=mibBuilder.importSymbols(_C,'zhoneModules',_H,_I,'zhoneVoice')
ZhoneShelfValue,ZhoneSlotValue=mibBuilder.importSymbols('Zhone-TC','ZhoneShelfValue','ZhoneSlotValue')
comVoiceDsp=ModuleIdentity((1,3,6,1,4,1,5504,6,12))
if mibBuilder.loadTexts:comVoiceDsp.setRevisions(('2003-03-28 10:42','2003-02-13 19:35','2001-10-02 18:34','2000-11-28 13:56','2000-09-20 18:42'))
_ZhoneVoiceDsp_ObjectIdentity=ObjectIdentity
zhoneVoiceDsp=_ZhoneVoiceDsp_ObjectIdentity((1,3,6,1,4,1,5504,4,3,3))
if mibBuilder.loadTexts:zhoneVoiceDsp.setStatus(_A)
_VoiceDspDefaultConfiguration_ObjectIdentity=ObjectIdentity
voiceDspDefaultConfiguration=_VoiceDspDefaultConfiguration_ObjectIdentity((1,3,6,1,4,1,5504,4,3,3,1))
if mibBuilder.loadTexts:voiceDspDefaultConfiguration.setStatus(_A)
class _RedundancyOverSubscriptionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('low',2),('medium',3),('high',4)))
_RedundancyOverSubscriptionType_Type.__name__=_D
_RedundancyOverSubscriptionType_Object=MibScalar
redundancyOverSubscriptionType=_RedundancyOverSubscriptionType_Object((1,3,6,1,4,1,5504,4,3,3,1,1),_RedundancyOverSubscriptionType_Type())
redundancyOverSubscriptionType.setMaxAccess(_E)
if mibBuilder.loadTexts:redundancyOverSubscriptionType.setStatus(_A)
class _JitterBufferType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_JitterBufferType_Type.__name__=_D
_JitterBufferType_Object=MibScalar
jitterBufferType=_JitterBufferType_Object((1,3,6,1,4,1,5504,4,3,3,1,2),_JitterBufferType_Type())
jitterBufferType.setMaxAccess(_E)
if mibBuilder.loadTexts:jitterBufferType.setStatus(_A)
class _JitterBufferSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_JitterBufferSize_Type.__name__=_F
_JitterBufferSize_Object=MibScalar
jitterBufferSize=_JitterBufferSize_Object((1,3,6,1,4,1,5504,4,3,3,1,3),_JitterBufferSize_Type())
jitterBufferSize.setMaxAccess(_E)
if mibBuilder.loadTexts:jitterBufferSize.setStatus(_A)
if mibBuilder.loadTexts:jitterBufferSize.setUnits(_J)
class _InterArrvJitThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_InterArrvJitThreshold_Type.__name__=_F
_InterArrvJitThreshold_Object=MibScalar
interArrvJitThreshold=_InterArrvJitThreshold_Object((1,3,6,1,4,1,5504,4,3,3,1,4),_InterArrvJitThreshold_Type())
interArrvJitThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:interArrvJitThreshold.setStatus(_A)
if mibBuilder.loadTexts:interArrvJitThreshold.setUnits(_J)
class _PktsLostThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_PktsLostThreshold_Type.__name__=_F
_PktsLostThreshold_Object=MibScalar
pktsLostThreshold=_PktsLostThreshold_Object((1,3,6,1,4,1,5504,4,3,3,1,5),_PktsLostThreshold_Type())
pktsLostThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:pktsLostThreshold.setStatus(_A)
class _EchoCancellationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('off',1),('g165EchoTL16',2),('g165EchoTL32',3),('g165EchoTL48',4),('g168EchoTL32',5),('g168EchoTL48',6),('g168EchoTL64',7),('g168EchoTL80',8),('g168EchoTL96',9),('g168EchoTL112',10),('g168EchoTL128',11)))
_EchoCancellationType_Type.__name__=_D
_EchoCancellationType_Object=MibScalar
echoCancellationType=_EchoCancellationType_Object((1,3,6,1,4,1,5504,4,3,3,1,6),_EchoCancellationType_Type())
echoCancellationType.setMaxAccess(_E)
if mibBuilder.loadTexts:echoCancellationType.setStatus(_A)
class _SilenceSuppressionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('silSupOff',1),('silSupOnSidOff',2),('silSupOnSidOn',3),('silSupOnSidConst',4)))
_SilenceSuppressionType_Type.__name__=_D
_SilenceSuppressionType_Object=MibScalar
silenceSuppressionType=_SilenceSuppressionType_Object((1,3,6,1,4,1,5504,4,3,3,1,7),_SilenceSuppressionType_Type())
silenceSuppressionType.setMaxAccess(_E)
if mibBuilder.loadTexts:silenceSuppressionType.setStatus(_A)
class _EchoReturnLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('erl0dB',1),('erl3dB',2),('erl6dB',3)))
_EchoReturnLoss_Type.__name__=_D
_EchoReturnLoss_Object=MibScalar
echoReturnLoss=_EchoReturnLoss_Object((1,3,6,1,4,1,5504,4,3,3,1,8),_EchoReturnLoss_Type())
echoReturnLoss.setMaxAccess(_E)
if mibBuilder.loadTexts:echoReturnLoss.setStatus(_A)
_VoiceDspStatusTable_Object=MibTable
voiceDspStatusTable=_VoiceDspStatusTable_Object((1,3,6,1,4,1,5504,4,3,3,2))
if mibBuilder.loadTexts:voiceDspStatusTable.setStatus(_A)
_VoiceDspStatusEntry_Object=MibTableRow
voiceDspStatusEntry=_VoiceDspStatusEntry_Object((1,3,6,1,4,1,5504,4,3,3,2,1))
voiceDspStatusEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:voiceDspStatusEntry.setStatus(_A)
class _VoiceDspMaxChannelOnBoard_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1008))
_VoiceDspMaxChannelOnBoard_Type.__name__=_F
_VoiceDspMaxChannelOnBoard_Object=MibTableColumn
voiceDspMaxChannelOnBoard=_VoiceDspMaxChannelOnBoard_Object((1,3,6,1,4,1,5504,4,3,3,2,1,1),_VoiceDspMaxChannelOnBoard_Type())
voiceDspMaxChannelOnBoard.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceDspMaxChannelOnBoard.setStatus(_A)
class _VoiceDspActiveChannelCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1008))
_VoiceDspActiveChannelCount_Type.__name__=_F
_VoiceDspActiveChannelCount_Object=MibTableColumn
voiceDspActiveChannelCount=_VoiceDspActiveChannelCount_Object((1,3,6,1,4,1,5504,4,3,3,2,1,2),_VoiceDspActiveChannelCount_Type())
voiceDspActiveChannelCount.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceDspActiveChannelCount.setStatus(_A)
class _VoiceDspHiWaterChannelCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1008))
_VoiceDspHiWaterChannelCount_Type.__name__=_F
_VoiceDspHiWaterChannelCount_Object=MibTableColumn
voiceDspHiWaterChannelCount=_VoiceDspHiWaterChannelCount_Object((1,3,6,1,4,1,5504,4,3,3,2,1,3),_VoiceDspHiWaterChannelCount_Type())
voiceDspHiWaterChannelCount.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceDspHiWaterChannelCount.setStatus(_A)
_VoiceDspResetCount_Type=Counter32
_VoiceDspResetCount_Object=MibTableColumn
voiceDspResetCount=_VoiceDspResetCount_Object((1,3,6,1,4,1,5504,4,3,3,2,1,4),_VoiceDspResetCount_Type())
voiceDspResetCount.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceDspResetCount.setStatus(_A)
_ChannelStatusTable_Object=MibTable
channelStatusTable=_ChannelStatusTable_Object((1,3,6,1,4,1,5504,4,3,3,3))
if mibBuilder.loadTexts:channelStatusTable.setStatus(_A)
_ChannelStatusEntry_Object=MibTableRow
channelStatusEntry=_ChannelStatusEntry_Object((1,3,6,1,4,1,5504,4,3,3,3,1))
channelStatusEntry.setIndexNames((0,_C,_H),(0,_C,_I),(0,_G,_K))
if mibBuilder.loadTexts:channelStatusEntry.setStatus(_A)
class _ChannelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_ChannelId_Type.__name__=_D
_ChannelId_Object=MibTableColumn
channelId=_ChannelId_Object((1,3,6,1,4,1,5504,4,3,3,3,1,1),_ChannelId_Type())
channelId.setMaxAccess(_B)
if mibBuilder.loadTexts:channelId.setStatus(_A)
_ChannelVoiceSessionIdHigh_Type=Unsigned32
_ChannelVoiceSessionIdHigh_Object=MibTableColumn
channelVoiceSessionIdHigh=_ChannelVoiceSessionIdHigh_Object((1,3,6,1,4,1,5504,4,3,3,3,1,2),_ChannelVoiceSessionIdHigh_Type())
channelVoiceSessionIdHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:channelVoiceSessionIdHigh.setStatus(_A)
_ChannelVoiceSessionIdLow_Type=Unsigned32
_ChannelVoiceSessionIdLow_Object=MibTableColumn
channelVoiceSessionIdLow=_ChannelVoiceSessionIdLow_Object((1,3,6,1,4,1,5504,4,3,3,3,1,3),_ChannelVoiceSessionIdLow_Type())
channelVoiceSessionIdLow.setMaxAccess(_B)
if mibBuilder.loadTexts:channelVoiceSessionIdLow.setStatus(_A)
_ChannelCcrpShelf_Type=ZhoneShelfValue
_ChannelCcrpShelf_Object=MibTableColumn
channelCcrpShelf=_ChannelCcrpShelf_Object((1,3,6,1,4,1,5504,4,3,3,3,1,4),_ChannelCcrpShelf_Type())
channelCcrpShelf.setMaxAccess(_B)
if mibBuilder.loadTexts:channelCcrpShelf.setStatus(_A)
_ChannelCcrpSlot_Type=ZhoneSlotValue
_ChannelCcrpSlot_Object=MibTableColumn
channelCcrpSlot=_ChannelCcrpSlot_Object((1,3,6,1,4,1,5504,4,3,3,3,1,5),_ChannelCcrpSlot_Type())
channelCcrpSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:channelCcrpSlot.setStatus(_A)
_ChannelTrunkCtrpShelf_Type=ZhoneShelfValue
_ChannelTrunkCtrpShelf_Object=MibTableColumn
channelTrunkCtrpShelf=_ChannelTrunkCtrpShelf_Object((1,3,6,1,4,1,5504,4,3,3,3,1,6),_ChannelTrunkCtrpShelf_Type())
channelTrunkCtrpShelf.setMaxAccess(_B)
if mibBuilder.loadTexts:channelTrunkCtrpShelf.setStatus(_A)
_ChannelTrunkCtrpSlot_Type=ZhoneSlotValue
_ChannelTrunkCtrpSlot_Object=MibTableColumn
channelTrunkCtrpSlot=_ChannelTrunkCtrpSlot_Object((1,3,6,1,4,1,5504,4,3,3,3,1,7),_ChannelTrunkCtrpSlot_Type())
channelTrunkCtrpSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:channelTrunkCtrpSlot.setStatus(_A)
_ChannelPktCtrpShelf_Type=ZhoneShelfValue
_ChannelPktCtrpShelf_Object=MibTableColumn
channelPktCtrpShelf=_ChannelPktCtrpShelf_Object((1,3,6,1,4,1,5504,4,3,3,3,1,8),_ChannelPktCtrpShelf_Type())
channelPktCtrpShelf.setMaxAccess(_B)
if mibBuilder.loadTexts:channelPktCtrpShelf.setStatus(_A)
_ChannelPktCtrpSlot_Type=ZhoneSlotValue
_ChannelPktCtrpSlot_Object=MibTableColumn
channelPktCtrpSlot=_ChannelPktCtrpSlot_Object((1,3,6,1,4,1,5504,4,3,3,3,1,9),_ChannelPktCtrpSlot_Type())
channelPktCtrpSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:channelPktCtrpSlot.setStatus(_A)
class _ChannelActiveCodec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('g711Ulaw',1),('g711Alaw',2),('g726',3),('g729A',4),('g729B',5),('g729E',6),('g723R1KBPS5Dot3',7),('g723R1KBPS6Dot3',8),('g723R1AKBPS5Dot3',9),('g723R1AKBPS6Dot3',10)))
_ChannelActiveCodec_Type.__name__=_D
_ChannelActiveCodec_Object=MibTableColumn
channelActiveCodec=_ChannelActiveCodec_Object((1,3,6,1,4,1,5504,4,3,3,3,1,10),_ChannelActiveCodec_Type())
channelActiveCodec.setMaxAccess(_B)
if mibBuilder.loadTexts:channelActiveCodec.setStatus(_A)
_ChannelTimeAlive_Type=TimeTicks
_ChannelTimeAlive_Object=MibTableColumn
channelTimeAlive=_ChannelTimeAlive_Object((1,3,6,1,4,1,5504,4,3,3,3,1,11),_ChannelTimeAlive_Type())
channelTimeAlive.setMaxAccess(_B)
if mibBuilder.loadTexts:channelTimeAlive.setStatus(_A)
_ChannelPktsSent_Type=Counter32
_ChannelPktsSent_Object=MibTableColumn
channelPktsSent=_ChannelPktsSent_Object((1,3,6,1,4,1,5504,4,3,3,3,1,12),_ChannelPktsSent_Type())
channelPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:channelPktsSent.setStatus(_A)
_ChannelBytesSent_Type=Counter32
_ChannelBytesSent_Object=MibTableColumn
channelBytesSent=_ChannelBytesSent_Object((1,3,6,1,4,1,5504,4,3,3,3,1,13),_ChannelBytesSent_Type())
channelBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:channelBytesSent.setStatus(_A)
_ChannelPktsReceived_Type=Counter32
_ChannelPktsReceived_Object=MibTableColumn
channelPktsReceived=_ChannelPktsReceived_Object((1,3,6,1,4,1,5504,4,3,3,3,1,14),_ChannelPktsReceived_Type())
channelPktsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:channelPktsReceived.setStatus(_A)
_ChannelBytesReceived_Type=Counter32
_ChannelBytesReceived_Object=MibTableColumn
channelBytesReceived=_ChannelBytesReceived_Object((1,3,6,1,4,1,5504,4,3,3,3,1,15),_ChannelBytesReceived_Type())
channelBytesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:channelBytesReceived.setStatus(_A)
_ChannelPktsLost_Type=Counter32
_ChannelPktsLost_Object=MibTableColumn
channelPktsLost=_ChannelPktsLost_Object((1,3,6,1,4,1,5504,4,3,3,3,1,16),_ChannelPktsLost_Type())
channelPktsLost.setMaxAccess(_B)
if mibBuilder.loadTexts:channelPktsLost.setStatus(_A)
_ChannelInterArrvJitter_Type=Unsigned32
_ChannelInterArrvJitter_Object=MibTableColumn
channelInterArrvJitter=_ChannelInterArrvJitter_Object((1,3,6,1,4,1,5504,4,3,3,3,1,17),_ChannelInterArrvJitter_Type())
channelInterArrvJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInterArrvJitter.setStatus(_A)
if mibBuilder.loadTexts:channelInterArrvJitter.setUnits(_J)
_ChannelJitterBufferSize_Type=Unsigned32
_ChannelJitterBufferSize_Object=MibTableColumn
channelJitterBufferSize=_ChannelJitterBufferSize_Object((1,3,6,1,4,1,5504,4,3,3,3,1,18),_ChannelJitterBufferSize_Type())
channelJitterBufferSize.setMaxAccess(_B)
if mibBuilder.loadTexts:channelJitterBufferSize.setStatus(_A)
if mibBuilder.loadTexts:channelJitterBufferSize.setUnits(_J)
_VoiceDspTraps_ObjectIdentity=ObjectIdentity
voiceDspTraps=_VoiceDspTraps_ObjectIdentity((1,3,6,1,4,1,5504,4,3,3,4))
if mibBuilder.loadTexts:voiceDspTraps.setStatus(_A)
_VoiceDspTrapsPrefix_ObjectIdentity=ObjectIdentity
voiceDspTrapsPrefix=_VoiceDspTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,5504,4,3,3,4,0))
if mibBuilder.loadTexts:voiceDspTrapsPrefix.setStatus(_A)
voiceDspReset=NotificationType((1,3,6,1,4,1,5504,4,3,3,4,0,1))
voiceDspReset.setObjects(*((_C,_H),(_C,_I),(_G,_L)))
if mibBuilder.loadTexts:voiceDspReset.setStatus(_A)
voiceDspChannelPktsLoss=NotificationType((1,3,6,1,4,1,5504,4,3,3,4,0,2))
voiceDspChannelPktsLoss.setObjects(*((_C,_H),(_C,_I),(_G,_K),(_G,_M)))
if mibBuilder.loadTexts:voiceDspChannelPktsLoss.setStatus(_A)
voiceDspChannelInterArrvJitterTrigger=NotificationType((1,3,6,1,4,1,5504,4,3,3,4,0,3))
voiceDspChannelInterArrvJitterTrigger.setObjects(*((_C,_H),(_C,_I),(_G,_K),(_G,_N)))
if mibBuilder.loadTexts:voiceDspChannelInterArrvJitterTrigger.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'zhoneVoiceDsp':zhoneVoiceDsp,'voiceDspDefaultConfiguration':voiceDspDefaultConfiguration,'redundancyOverSubscriptionType':redundancyOverSubscriptionType,'jitterBufferType':jitterBufferType,'jitterBufferSize':jitterBufferSize,'interArrvJitThreshold':interArrvJitThreshold,'pktsLostThreshold':pktsLostThreshold,'echoCancellationType':echoCancellationType,'silenceSuppressionType':silenceSuppressionType,'echoReturnLoss':echoReturnLoss,'voiceDspStatusTable':voiceDspStatusTable,'voiceDspStatusEntry':voiceDspStatusEntry,'voiceDspMaxChannelOnBoard':voiceDspMaxChannelOnBoard,'voiceDspActiveChannelCount':voiceDspActiveChannelCount,'voiceDspHiWaterChannelCount':voiceDspHiWaterChannelCount,_L:voiceDspResetCount,'channelStatusTable':channelStatusTable,'channelStatusEntry':channelStatusEntry,_K:channelId,'channelVoiceSessionIdHigh':channelVoiceSessionIdHigh,'channelVoiceSessionIdLow':channelVoiceSessionIdLow,'channelCcrpShelf':channelCcrpShelf,'channelCcrpSlot':channelCcrpSlot,'channelTrunkCtrpShelf':channelTrunkCtrpShelf,'channelTrunkCtrpSlot':channelTrunkCtrpSlot,'channelPktCtrpShelf':channelPktCtrpShelf,'channelPktCtrpSlot':channelPktCtrpSlot,'channelActiveCodec':channelActiveCodec,'channelTimeAlive':channelTimeAlive,'channelPktsSent':channelPktsSent,'channelBytesSent':channelBytesSent,'channelPktsReceived':channelPktsReceived,'channelBytesReceived':channelBytesReceived,_M:channelPktsLost,_N:channelInterArrvJitter,'channelJitterBufferSize':channelJitterBufferSize,'voiceDspTraps':voiceDspTraps,'voiceDspTrapsPrefix':voiceDspTrapsPrefix,'voiceDspReset':voiceDspReset,'voiceDspChannelPktsLoss':voiceDspChannelPktsLoss,'voiceDspChannelInterArrvJitterTrigger':voiceDspChannelInterArrvJitterTrigger,'comVoiceDsp':comVoiceDsp})