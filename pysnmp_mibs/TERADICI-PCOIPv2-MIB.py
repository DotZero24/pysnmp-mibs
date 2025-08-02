_L='pcoipUSBDevicesIndex'
_K='pcoipImagingDevicesIndex'
_J='pcoipGenDevicesSessionNumber'
_I='pcoipUSBStatsSessionNumber'
_H='pcoipImagingStatsSessionNumber'
_G='pcoipAudioStatsSessionNumber'
_F='pcoipNetStatsSessionNumber'
_E='pcoipGenStatsSessionNumber'
_D='TERADICI-PCOIPv2-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
teraMibModule=ModuleIdentity((1,3,6,1,4,1,25071))
if mibBuilder.loadTexts:teraMibModule.setRevisions(('2012-01-28 10:00',))
_TeraProducts_ObjectIdentity=ObjectIdentity
teraProducts=_TeraProducts_ObjectIdentity((1,3,6,1,4,1,25071,1))
_TeraPcoipV2_ObjectIdentity=ObjectIdentity
teraPcoipV2=_TeraPcoipV2_ObjectIdentity((1,3,6,1,4,1,25071,1,2))
_TeraPcoipGenStats_ObjectIdentity=ObjectIdentity
teraPcoipGenStats=_TeraPcoipGenStats_ObjectIdentity((1,3,6,1,4,1,25071,1,2,1))
_PcoipGenStatsTable_Object=MibTable
pcoipGenStatsTable=_PcoipGenStatsTable_Object((1,3,6,1,4,1,25071,1,2,1,1))
if mibBuilder.loadTexts:pcoipGenStatsTable.setStatus(_A)
_PcoipGenStatsEntry_Object=MibTableRow
pcoipGenStatsEntry=_PcoipGenStatsEntry_Object((1,3,6,1,4,1,25071,1,2,1,1,1))
pcoipGenStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pcoipGenStatsEntry.setStatus(_A)
class _PcoipGenStatsSessionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_PcoipGenStatsSessionNumber_Type.__name__=_C
_PcoipGenStatsSessionNumber_Object=MibTableColumn
pcoipGenStatsSessionNumber=_PcoipGenStatsSessionNumber_Object((1,3,6,1,4,1,25071,1,2,1,1,1,1),_PcoipGenStatsSessionNumber_Type())
pcoipGenStatsSessionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenStatsSessionNumber.setStatus(_A)
_PcoipGenStatsPacketsSent_Type=Counter64
_PcoipGenStatsPacketsSent_Object=MibTableColumn
pcoipGenStatsPacketsSent=_PcoipGenStatsPacketsSent_Object((1,3,6,1,4,1,25071,1,2,1,1,1,2),_PcoipGenStatsPacketsSent_Type())
pcoipGenStatsPacketsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenStatsPacketsSent.setStatus(_A)
_PcoipGenStatsBytesSent_Type=Counter64
_PcoipGenStatsBytesSent_Object=MibTableColumn
pcoipGenStatsBytesSent=_PcoipGenStatsBytesSent_Object((1,3,6,1,4,1,25071,1,2,1,1,1,3),_PcoipGenStatsBytesSent_Type())
pcoipGenStatsBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenStatsBytesSent.setStatus(_A)
_PcoipGenStatsPacketsReceived_Type=Counter64
_PcoipGenStatsPacketsReceived_Object=MibTableColumn
pcoipGenStatsPacketsReceived=_PcoipGenStatsPacketsReceived_Object((1,3,6,1,4,1,25071,1,2,1,1,1,4),_PcoipGenStatsPacketsReceived_Type())
pcoipGenStatsPacketsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenStatsPacketsReceived.setStatus(_A)
_PcoipGenStatsBytesReceived_Type=Counter64
_PcoipGenStatsBytesReceived_Object=MibTableColumn
pcoipGenStatsBytesReceived=_PcoipGenStatsBytesReceived_Object((1,3,6,1,4,1,25071,1,2,1,1,1,5),_PcoipGenStatsBytesReceived_Type())
pcoipGenStatsBytesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenStatsBytesReceived.setStatus(_A)
_PcoipGenStatsTxPacketsLost_Type=Counter64
_PcoipGenStatsTxPacketsLost_Object=MibTableColumn
pcoipGenStatsTxPacketsLost=_PcoipGenStatsTxPacketsLost_Object((1,3,6,1,4,1,25071,1,2,1,1,1,6),_PcoipGenStatsTxPacketsLost_Type())
pcoipGenStatsTxPacketsLost.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenStatsTxPacketsLost.setStatus(_A)
_PcoipGenStatsSessionDuration_Type=Counter64
_PcoipGenStatsSessionDuration_Object=MibTableColumn
pcoipGenStatsSessionDuration=_PcoipGenStatsSessionDuration_Object((1,3,6,1,4,1,25071,1,2,1,1,1,7),_PcoipGenStatsSessionDuration_Type())
pcoipGenStatsSessionDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenStatsSessionDuration.setStatus(_A)
_TeraPcoipNetStats_ObjectIdentity=ObjectIdentity
teraPcoipNetStats=_TeraPcoipNetStats_ObjectIdentity((1,3,6,1,4,1,25071,1,2,2))
_PcoipNetStatsTable_Object=MibTable
pcoipNetStatsTable=_PcoipNetStatsTable_Object((1,3,6,1,4,1,25071,1,2,2,1))
if mibBuilder.loadTexts:pcoipNetStatsTable.setStatus(_A)
_PcoipNetStatsEntry_Object=MibTableRow
pcoipNetStatsEntry=_PcoipNetStatsEntry_Object((1,3,6,1,4,1,25071,1,2,2,1,1))
pcoipNetStatsEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:pcoipNetStatsEntry.setStatus(_A)
class _PcoipNetStatsSessionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_PcoipNetStatsSessionNumber_Type.__name__=_C
_PcoipNetStatsSessionNumber_Object=MibTableColumn
pcoipNetStatsSessionNumber=_PcoipNetStatsSessionNumber_Object((1,3,6,1,4,1,25071,1,2,2,1,1,1),_PcoipNetStatsSessionNumber_Type())
pcoipNetStatsSessionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipNetStatsSessionNumber.setStatus(_A)
_PcoipNetStatsRoundTripLatencyMs_Type=Counter64
_PcoipNetStatsRoundTripLatencyMs_Object=MibTableColumn
pcoipNetStatsRoundTripLatencyMs=_PcoipNetStatsRoundTripLatencyMs_Object((1,3,6,1,4,1,25071,1,2,2,1,1,2),_PcoipNetStatsRoundTripLatencyMs_Type())
pcoipNetStatsRoundTripLatencyMs.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipNetStatsRoundTripLatencyMs.setStatus(_A)
_PcoipNetStatsRXBWkbitPersec_Type=Counter64
_PcoipNetStatsRXBWkbitPersec_Object=MibTableColumn
pcoipNetStatsRXBWkbitPersec=_PcoipNetStatsRXBWkbitPersec_Object((1,3,6,1,4,1,25071,1,2,2,1,1,3),_PcoipNetStatsRXBWkbitPersec_Type())
pcoipNetStatsRXBWkbitPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipNetStatsRXBWkbitPersec.setStatus(_A)
class _PcoipNetStatsRXBWPeakkbitPersec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_PcoipNetStatsRXBWPeakkbitPersec_Type.__name__=_C
_PcoipNetStatsRXBWPeakkbitPersec_Object=MibTableColumn
pcoipNetStatsRXBWPeakkbitPersec=_PcoipNetStatsRXBWPeakkbitPersec_Object((1,3,6,1,4,1,25071,1,2,2,1,1,4),_PcoipNetStatsRXBWPeakkbitPersec_Type())
pcoipNetStatsRXBWPeakkbitPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipNetStatsRXBWPeakkbitPersec.setStatus(_A)
class _PcoipNetStatsRXPacketLossPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PcoipNetStatsRXPacketLossPercent_Type.__name__=_C
_PcoipNetStatsRXPacketLossPercent_Object=MibTableColumn
pcoipNetStatsRXPacketLossPercent=_PcoipNetStatsRXPacketLossPercent_Object((1,3,6,1,4,1,25071,1,2,2,1,1,5),_PcoipNetStatsRXPacketLossPercent_Type())
pcoipNetStatsRXPacketLossPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipNetStatsRXPacketLossPercent.setStatus(_A)
_PcoipNetStatsTXBWkbitPersec_Type=Counter64
_PcoipNetStatsTXBWkbitPersec_Object=MibTableColumn
pcoipNetStatsTXBWkbitPersec=_PcoipNetStatsTXBWkbitPersec_Object((1,3,6,1,4,1,25071,1,2,2,1,1,6),_PcoipNetStatsTXBWkbitPersec_Type())
pcoipNetStatsTXBWkbitPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipNetStatsTXBWkbitPersec.setStatus(_A)
class _PcoipNetStatsTXBWActiveLimitkbitPersec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_PcoipNetStatsTXBWActiveLimitkbitPersec_Type.__name__=_C
_PcoipNetStatsTXBWActiveLimitkbitPersec_Object=MibTableColumn
pcoipNetStatsTXBWActiveLimitkbitPersec=_PcoipNetStatsTXBWActiveLimitkbitPersec_Object((1,3,6,1,4,1,25071,1,2,2,1,1,7),_PcoipNetStatsTXBWActiveLimitkbitPersec_Type())
pcoipNetStatsTXBWActiveLimitkbitPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipNetStatsTXBWActiveLimitkbitPersec.setStatus(_A)
class _PcoipNetStatsTXBWLimitkbitPersec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_PcoipNetStatsTXBWLimitkbitPersec_Type.__name__=_C
_PcoipNetStatsTXBWLimitkbitPersec_Object=MibTableColumn
pcoipNetStatsTXBWLimitkbitPersec=_PcoipNetStatsTXBWLimitkbitPersec_Object((1,3,6,1,4,1,25071,1,2,2,1,1,8),_PcoipNetStatsTXBWLimitkbitPersec_Type())
pcoipNetStatsTXBWLimitkbitPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipNetStatsTXBWLimitkbitPersec.setStatus(_A)
class _PcoipNetStatsTXPacketLossPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PcoipNetStatsTXPacketLossPercent_Type.__name__=_C
_PcoipNetStatsTXPacketLossPercent_Object=MibTableColumn
pcoipNetStatsTXPacketLossPercent=_PcoipNetStatsTXPacketLossPercent_Object((1,3,6,1,4,1,25071,1,2,2,1,1,9),_PcoipNetStatsTXPacketLossPercent_Type())
pcoipNetStatsTXPacketLossPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipNetStatsTXPacketLossPercent.setStatus(_A)
_TeraPcoipAudioStats_ObjectIdentity=ObjectIdentity
teraPcoipAudioStats=_TeraPcoipAudioStats_ObjectIdentity((1,3,6,1,4,1,25071,1,2,3))
_PcoipAudioStatsTable_Object=MibTable
pcoipAudioStatsTable=_PcoipAudioStatsTable_Object((1,3,6,1,4,1,25071,1,2,3,1))
if mibBuilder.loadTexts:pcoipAudioStatsTable.setStatus(_A)
_PcoipAudioStatsEntry_Object=MibTableRow
pcoipAudioStatsEntry=_PcoipAudioStatsEntry_Object((1,3,6,1,4,1,25071,1,2,3,1,1))
pcoipAudioStatsEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:pcoipAudioStatsEntry.setStatus(_A)
class _PcoipAudioStatsSessionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_PcoipAudioStatsSessionNumber_Type.__name__=_C
_PcoipAudioStatsSessionNumber_Object=MibTableColumn
pcoipAudioStatsSessionNumber=_PcoipAudioStatsSessionNumber_Object((1,3,6,1,4,1,25071,1,2,3,1,1,1),_PcoipAudioStatsSessionNumber_Type())
pcoipAudioStatsSessionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipAudioStatsSessionNumber.setStatus(_A)
_PcoipAudioStatsBytesReceived_Type=Counter64
_PcoipAudioStatsBytesReceived_Object=MibTableColumn
pcoipAudioStatsBytesReceived=_PcoipAudioStatsBytesReceived_Object((1,3,6,1,4,1,25071,1,2,3,1,1,2),_PcoipAudioStatsBytesReceived_Type())
pcoipAudioStatsBytesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipAudioStatsBytesReceived.setStatus(_A)
_PcoipAudioStatsBytesSent_Type=Counter64
_PcoipAudioStatsBytesSent_Object=MibTableColumn
pcoipAudioStatsBytesSent=_PcoipAudioStatsBytesSent_Object((1,3,6,1,4,1,25071,1,2,3,1,1,3),_PcoipAudioStatsBytesSent_Type())
pcoipAudioStatsBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipAudioStatsBytesSent.setStatus(_A)
_PcoipAudioStatsRXBWkbitPersec_Type=Counter64
_PcoipAudioStatsRXBWkbitPersec_Object=MibTableColumn
pcoipAudioStatsRXBWkbitPersec=_PcoipAudioStatsRXBWkbitPersec_Object((1,3,6,1,4,1,25071,1,2,3,1,1,4),_PcoipAudioStatsRXBWkbitPersec_Type())
pcoipAudioStatsRXBWkbitPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipAudioStatsRXBWkbitPersec.setStatus(_A)
_PcoipAudioStatsTXBWkbitPersec_Type=Counter64
_PcoipAudioStatsTXBWkbitPersec_Object=MibTableColumn
pcoipAudioStatsTXBWkbitPersec=_PcoipAudioStatsTXBWkbitPersec_Object((1,3,6,1,4,1,25071,1,2,3,1,1,5),_PcoipAudioStatsTXBWkbitPersec_Type())
pcoipAudioStatsTXBWkbitPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipAudioStatsTXBWkbitPersec.setStatus(_A)
class _PcoipAudioStatsTXBWLimitkbitPersec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_PcoipAudioStatsTXBWLimitkbitPersec_Type.__name__=_C
_PcoipAudioStatsTXBWLimitkbitPersec_Object=MibTableColumn
pcoipAudioStatsTXBWLimitkbitPersec=_PcoipAudioStatsTXBWLimitkbitPersec_Object((1,3,6,1,4,1,25071,1,2,3,1,1,6),_PcoipAudioStatsTXBWLimitkbitPersec_Type())
pcoipAudioStatsTXBWLimitkbitPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipAudioStatsTXBWLimitkbitPersec.setStatus(_A)
_TeraPcoipImagingStats_ObjectIdentity=ObjectIdentity
teraPcoipImagingStats=_TeraPcoipImagingStats_ObjectIdentity((1,3,6,1,4,1,25071,1,2,4))
_PcoipImagingStatsTable_Object=MibTable
pcoipImagingStatsTable=_PcoipImagingStatsTable_Object((1,3,6,1,4,1,25071,1,2,4,1))
if mibBuilder.loadTexts:pcoipImagingStatsTable.setStatus(_A)
_PcoipImagingStatsEntry_Object=MibTableRow
pcoipImagingStatsEntry=_PcoipImagingStatsEntry_Object((1,3,6,1,4,1,25071,1,2,4,1,1))
pcoipImagingStatsEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:pcoipImagingStatsEntry.setStatus(_A)
class _PcoipImagingStatsSessionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_PcoipImagingStatsSessionNumber_Type.__name__=_C
_PcoipImagingStatsSessionNumber_Object=MibTableColumn
pcoipImagingStatsSessionNumber=_PcoipImagingStatsSessionNumber_Object((1,3,6,1,4,1,25071,1,2,4,1,1,1),_PcoipImagingStatsSessionNumber_Type())
pcoipImagingStatsSessionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingStatsSessionNumber.setStatus(_A)
_PcoipImagingStatsBytesReceived_Type=Counter64
_PcoipImagingStatsBytesReceived_Object=MibTableColumn
pcoipImagingStatsBytesReceived=_PcoipImagingStatsBytesReceived_Object((1,3,6,1,4,1,25071,1,2,4,1,1,2),_PcoipImagingStatsBytesReceived_Type())
pcoipImagingStatsBytesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingStatsBytesReceived.setStatus(_A)
_PcoipImagingStatsBytesSent_Type=Counter64
_PcoipImagingStatsBytesSent_Object=MibTableColumn
pcoipImagingStatsBytesSent=_PcoipImagingStatsBytesSent_Object((1,3,6,1,4,1,25071,1,2,4,1,1,3),_PcoipImagingStatsBytesSent_Type())
pcoipImagingStatsBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingStatsBytesSent.setStatus(_A)
_PcoipImagingStatsRXBWkbitPersec_Type=Counter64
_PcoipImagingStatsRXBWkbitPersec_Object=MibTableColumn
pcoipImagingStatsRXBWkbitPersec=_PcoipImagingStatsRXBWkbitPersec_Object((1,3,6,1,4,1,25071,1,2,4,1,1,4),_PcoipImagingStatsRXBWkbitPersec_Type())
pcoipImagingStatsRXBWkbitPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingStatsRXBWkbitPersec.setStatus(_A)
_PcoipImagingStatsTXBWkbitPersec_Type=Counter64
_PcoipImagingStatsTXBWkbitPersec_Object=MibTableColumn
pcoipImagingStatsTXBWkbitPersec=_PcoipImagingStatsTXBWkbitPersec_Object((1,3,6,1,4,1,25071,1,2,4,1,1,5),_PcoipImagingStatsTXBWkbitPersec_Type())
pcoipImagingStatsTXBWkbitPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingStatsTXBWkbitPersec.setStatus(_A)
class _PcoipImagingStatsEncodedFramesPersec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2400))
_PcoipImagingStatsEncodedFramesPersec_Type.__name__=_C
_PcoipImagingStatsEncodedFramesPersec_Object=MibTableColumn
pcoipImagingStatsEncodedFramesPersec=_PcoipImagingStatsEncodedFramesPersec_Object((1,3,6,1,4,1,25071,1,2,4,1,1,6),_PcoipImagingStatsEncodedFramesPersec_Type())
pcoipImagingStatsEncodedFramesPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingStatsEncodedFramesPersec.setStatus(_A)
class _PcoipImagingStatsActiveMinimumQuality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PcoipImagingStatsActiveMinimumQuality_Type.__name__=_C
_PcoipImagingStatsActiveMinimumQuality_Object=MibTableColumn
pcoipImagingStatsActiveMinimumQuality=_PcoipImagingStatsActiveMinimumQuality_Object((1,3,6,1,4,1,25071,1,2,4,1,1,7),_PcoipImagingStatsActiveMinimumQuality_Type())
pcoipImagingStatsActiveMinimumQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingStatsActiveMinimumQuality.setStatus(_A)
class _PcoipImagingStatsDecoderCapabilitykbitPersec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_PcoipImagingStatsDecoderCapabilitykbitPersec_Type.__name__=_C
_PcoipImagingStatsDecoderCapabilitykbitPersec_Object=MibTableColumn
pcoipImagingStatsDecoderCapabilitykbitPersec=_PcoipImagingStatsDecoderCapabilitykbitPersec_Object((1,3,6,1,4,1,25071,1,2,4,1,1,8),_PcoipImagingStatsDecoderCapabilitykbitPersec_Type())
pcoipImagingStatsDecoderCapabilitykbitPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingStatsDecoderCapabilitykbitPersec.setStatus(_A)
class _PcoipImagingStatsPipelineProcRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_PcoipImagingStatsPipelineProcRate_Type.__name__=_C
_PcoipImagingStatsPipelineProcRate_Object=MibTableColumn
pcoipImagingStatsPipelineProcRate=_PcoipImagingStatsPipelineProcRate_Object((1,3,6,1,4,1,25071,1,2,4,1,1,9),_PcoipImagingStatsPipelineProcRate_Type())
pcoipImagingStatsPipelineProcRate.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingStatsPipelineProcRate.setStatus(_A)
_TeraPcoipUSBStats_ObjectIdentity=ObjectIdentity
teraPcoipUSBStats=_TeraPcoipUSBStats_ObjectIdentity((1,3,6,1,4,1,25071,1,2,5))
_PcoipUSBStatsTable_Object=MibTable
pcoipUSBStatsTable=_PcoipUSBStatsTable_Object((1,3,6,1,4,1,25071,1,2,5,1))
if mibBuilder.loadTexts:pcoipUSBStatsTable.setStatus(_A)
_PcoipUSBStatsEntry_Object=MibTableRow
pcoipUSBStatsEntry=_PcoipUSBStatsEntry_Object((1,3,6,1,4,1,25071,1,2,5,1,1))
pcoipUSBStatsEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:pcoipUSBStatsEntry.setStatus(_A)
class _PcoipUSBStatsSessionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_PcoipUSBStatsSessionNumber_Type.__name__=_C
_PcoipUSBStatsSessionNumber_Object=MibTableColumn
pcoipUSBStatsSessionNumber=_PcoipUSBStatsSessionNumber_Object((1,3,6,1,4,1,25071,1,2,5,1,1,1),_PcoipUSBStatsSessionNumber_Type())
pcoipUSBStatsSessionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBStatsSessionNumber.setStatus(_A)
_PcoipUSBStatsBytesReceived_Type=Counter64
_PcoipUSBStatsBytesReceived_Object=MibTableColumn
pcoipUSBStatsBytesReceived=_PcoipUSBStatsBytesReceived_Object((1,3,6,1,4,1,25071,1,2,5,1,1,2),_PcoipUSBStatsBytesReceived_Type())
pcoipUSBStatsBytesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBStatsBytesReceived.setStatus(_A)
_PcoipUSBStatsBytesSent_Type=Counter64
_PcoipUSBStatsBytesSent_Object=MibTableColumn
pcoipUSBStatsBytesSent=_PcoipUSBStatsBytesSent_Object((1,3,6,1,4,1,25071,1,2,5,1,1,3),_PcoipUSBStatsBytesSent_Type())
pcoipUSBStatsBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBStatsBytesSent.setStatus(_A)
_PcoipUSBStatsRXBWkbitPersec_Type=Counter64
_PcoipUSBStatsRXBWkbitPersec_Object=MibTableColumn
pcoipUSBStatsRXBWkbitPersec=_PcoipUSBStatsRXBWkbitPersec_Object((1,3,6,1,4,1,25071,1,2,5,1,1,4),_PcoipUSBStatsRXBWkbitPersec_Type())
pcoipUSBStatsRXBWkbitPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBStatsRXBWkbitPersec.setStatus(_A)
_PcoipUSBStatsTXBWkbitPersec_Type=Counter64
_PcoipUSBStatsTXBWkbitPersec_Object=MibTableColumn
pcoipUSBStatsTXBWkbitPersec=_PcoipUSBStatsTXBWkbitPersec_Object((1,3,6,1,4,1,25071,1,2,5,1,1,5),_PcoipUSBStatsTXBWkbitPersec_Type())
pcoipUSBStatsTXBWkbitPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBStatsTXBWkbitPersec.setStatus(_A)
_TeraPcoipGenDevices_ObjectIdentity=ObjectIdentity
teraPcoipGenDevices=_TeraPcoipGenDevices_ObjectIdentity((1,3,6,1,4,1,25071,1,2,6))
_PcoipGenDevicesTable_Object=MibTable
pcoipGenDevicesTable=_PcoipGenDevicesTable_Object((1,3,6,1,4,1,25071,1,2,6,1))
if mibBuilder.loadTexts:pcoipGenDevicesTable.setStatus(_A)
_PcoipGenDevicesEntry_Object=MibTableRow
pcoipGenDevicesEntry=_PcoipGenDevicesEntry_Object((1,3,6,1,4,1,25071,1,2,6,1,1))
pcoipGenDevicesEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:pcoipGenDevicesEntry.setStatus(_A)
class _PcoipGenDevicesSessionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_PcoipGenDevicesSessionNumber_Type.__name__=_C
_PcoipGenDevicesSessionNumber_Object=MibTableColumn
pcoipGenDevicesSessionNumber=_PcoipGenDevicesSessionNumber_Object((1,3,6,1,4,1,25071,1,2,6,1,1,1),_PcoipGenDevicesSessionNumber_Type())
pcoipGenDevicesSessionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenDevicesSessionNumber.setStatus(_A)
_PcoipGenDevicesName_Type=OctetString
_PcoipGenDevicesName_Object=MibTableColumn
pcoipGenDevicesName=_PcoipGenDevicesName_Object((1,3,6,1,4,1,25071,1,2,6,1,1,2),_PcoipGenDevicesName_Type())
pcoipGenDevicesName.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenDevicesName.setStatus(_A)
_PcoipGenDevicesDescription_Type=OctetString
_PcoipGenDevicesDescription_Object=MibTableColumn
pcoipGenDevicesDescription=_PcoipGenDevicesDescription_Object((1,3,6,1,4,1,25071,1,2,6,1,1,3),_PcoipGenDevicesDescription_Type())
pcoipGenDevicesDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenDevicesDescription.setStatus(_A)
_PcoipGenDevicesGenericTag_Type=OctetString
_PcoipGenDevicesGenericTag_Object=MibTableColumn
pcoipGenDevicesGenericTag=_PcoipGenDevicesGenericTag_Object((1,3,6,1,4,1,25071,1,2,6,1,1,4),_PcoipGenDevicesGenericTag_Type())
pcoipGenDevicesGenericTag.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenDevicesGenericTag.setStatus(_A)
_PcoipGenDevicesPartNumber_Type=OctetString
_PcoipGenDevicesPartNumber_Object=MibTableColumn
pcoipGenDevicesPartNumber=_PcoipGenDevicesPartNumber_Object((1,3,6,1,4,1,25071,1,2,6,1,1,5),_PcoipGenDevicesPartNumber_Type())
pcoipGenDevicesPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenDevicesPartNumber.setStatus(_A)
_PcoipGenDevicesFwPartNumber_Type=OctetString
_PcoipGenDevicesFwPartNumber_Object=MibScalar
pcoipGenDevicesFwPartNumber=_PcoipGenDevicesFwPartNumber_Object((1,3,6,1,4,1,25071,1,2,6,1,1,6),_PcoipGenDevicesFwPartNumber_Type())
pcoipGenDevicesFwPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenDevicesFwPartNumber.setStatus(_A)
_PcoipGenDevicesSerialNumber_Type=OctetString
_PcoipGenDevicesSerialNumber_Object=MibTableColumn
pcoipGenDevicesSerialNumber=_PcoipGenDevicesSerialNumber_Object((1,3,6,1,4,1,25071,1,2,6,1,1,7),_PcoipGenDevicesSerialNumber_Type())
pcoipGenDevicesSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenDevicesSerialNumber.setStatus(_A)
_PcoipGenDevicesHardwareVersion_Type=OctetString
_PcoipGenDevicesHardwareVersion_Object=MibTableColumn
pcoipGenDevicesHardwareVersion=_PcoipGenDevicesHardwareVersion_Object((1,3,6,1,4,1,25071,1,2,6,1,1,8),_PcoipGenDevicesHardwareVersion_Type())
pcoipGenDevicesHardwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenDevicesHardwareVersion.setStatus(_A)
_PcoipGenDevicesFirmwareVersion_Type=OctetString
_PcoipGenDevicesFirmwareVersion_Object=MibTableColumn
pcoipGenDevicesFirmwareVersion=_PcoipGenDevicesFirmwareVersion_Object((1,3,6,1,4,1,25071,1,2,6,1,1,9),_PcoipGenDevicesFirmwareVersion_Type())
pcoipGenDevicesFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenDevicesFirmwareVersion.setStatus(_A)
_PcoipGenDevicesUniqueID_Type=OctetString
_PcoipGenDevicesUniqueID_Object=MibTableColumn
pcoipGenDevicesUniqueID=_PcoipGenDevicesUniqueID_Object((1,3,6,1,4,1,25071,1,2,6,1,1,10),_PcoipGenDevicesUniqueID_Type())
pcoipGenDevicesUniqueID.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenDevicesUniqueID.setStatus(_A)
_PcoipGenDevicesMAC_Type=OctetString
_PcoipGenDevicesMAC_Object=MibTableColumn
pcoipGenDevicesMAC=_PcoipGenDevicesMAC_Object((1,3,6,1,4,1,25071,1,2,6,1,1,11),_PcoipGenDevicesMAC_Type())
pcoipGenDevicesMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenDevicesMAC.setStatus(_A)
_PcoipGenDevicesUptime_Type=Counter64
_PcoipGenDevicesUptime_Object=MibTableColumn
pcoipGenDevicesUptime=_PcoipGenDevicesUptime_Object((1,3,6,1,4,1,25071,1,2,6,1,1,12),_PcoipGenDevicesUptime_Type())
pcoipGenDevicesUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipGenDevicesUptime.setStatus(_A)
_TeraPcoipImagingDevices_ObjectIdentity=ObjectIdentity
teraPcoipImagingDevices=_TeraPcoipImagingDevices_ObjectIdentity((1,3,6,1,4,1,25071,1,2,7))
_PcoipImagingDevicesTable_Object=MibTable
pcoipImagingDevicesTable=_PcoipImagingDevicesTable_Object((1,3,6,1,4,1,25071,1,2,7,1))
if mibBuilder.loadTexts:pcoipImagingDevicesTable.setStatus(_A)
_PcoipImagingDevicesEntry_Object=MibTableRow
pcoipImagingDevicesEntry=_PcoipImagingDevicesEntry_Object((1,3,6,1,4,1,25071,1,2,7,1,1))
pcoipImagingDevicesEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:pcoipImagingDevicesEntry.setStatus(_A)
class _PcoipImagingDevicesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_PcoipImagingDevicesIndex_Type.__name__=_C
_PcoipImagingDevicesIndex_Object=MibTableColumn
pcoipImagingDevicesIndex=_PcoipImagingDevicesIndex_Object((1,3,6,1,4,1,25071,1,2,7,1,1,1),_PcoipImagingDevicesIndex_Type())
pcoipImagingDevicesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingDevicesIndex.setStatus(_A)
class _PcoipImagingDevicesSessionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_PcoipImagingDevicesSessionNumber_Type.__name__=_C
_PcoipImagingDevicesSessionNumber_Object=MibTableColumn
pcoipImagingDevicesSessionNumber=_PcoipImagingDevicesSessionNumber_Object((1,3,6,1,4,1,25071,1,2,7,1,1,2),_PcoipImagingDevicesSessionNumber_Type())
pcoipImagingDevicesSessionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingDevicesSessionNumber.setStatus(_A)
class _PcoipImagingDevicesDisplayWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_PcoipImagingDevicesDisplayWidth_Type.__name__=_C
_PcoipImagingDevicesDisplayWidth_Object=MibTableColumn
pcoipImagingDevicesDisplayWidth=_PcoipImagingDevicesDisplayWidth_Object((1,3,6,1,4,1,25071,1,2,7,1,1,3),_PcoipImagingDevicesDisplayWidth_Type())
pcoipImagingDevicesDisplayWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingDevicesDisplayWidth.setStatus(_A)
class _PcoipImagingDevicesDisplayHeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_PcoipImagingDevicesDisplayHeight_Type.__name__=_C
_PcoipImagingDevicesDisplayHeight_Object=MibTableColumn
pcoipImagingDevicesDisplayHeight=_PcoipImagingDevicesDisplayHeight_Object((1,3,6,1,4,1,25071,1,2,7,1,1,4),_PcoipImagingDevicesDisplayHeight_Type())
pcoipImagingDevicesDisplayHeight.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingDevicesDisplayHeight.setStatus(_A)
class _PcoipImagingDevicesDisplayRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_PcoipImagingDevicesDisplayRefreshRate_Type.__name__=_C
_PcoipImagingDevicesDisplayRefreshRate_Object=MibTableColumn
pcoipImagingDevicesDisplayRefreshRate=_PcoipImagingDevicesDisplayRefreshRate_Object((1,3,6,1,4,1,25071,1,2,7,1,1,5),_PcoipImagingDevicesDisplayRefreshRate_Type())
pcoipImagingDevicesDisplayRefreshRate.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingDevicesDisplayRefreshRate.setStatus(_A)
class _PcoipImagingDevicesDisplayChangeRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_PcoipImagingDevicesDisplayChangeRate_Type.__name__=_C
_PcoipImagingDevicesDisplayChangeRate_Object=MibTableColumn
pcoipImagingDevicesDisplayChangeRate=_PcoipImagingDevicesDisplayChangeRate_Object((1,3,6,1,4,1,25071,1,2,7,1,1,6),_PcoipImagingDevicesDisplayChangeRate_Type())
pcoipImagingDevicesDisplayChangeRate.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingDevicesDisplayChangeRate.setStatus(_A)
class _PcoipImagingDevicesDisplayProcessRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_PcoipImagingDevicesDisplayProcessRate_Type.__name__=_C
_PcoipImagingDevicesDisplayProcessRate_Object=MibTableColumn
pcoipImagingDevicesDisplayProcessRate=_PcoipImagingDevicesDisplayProcessRate_Object((1,3,6,1,4,1,25071,1,2,7,1,1,7),_PcoipImagingDevicesDisplayProcessRate_Type())
pcoipImagingDevicesDisplayProcessRate.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingDevicesDisplayProcessRate.setStatus(_A)
_PcoipImagingDevicesLimitReason_Type=OctetString
_PcoipImagingDevicesLimitReason_Object=MibTableColumn
pcoipImagingDevicesLimitReason=_PcoipImagingDevicesLimitReason_Object((1,3,6,1,4,1,25071,1,2,7,1,1,8),_PcoipImagingDevicesLimitReason_Type())
pcoipImagingDevicesLimitReason.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingDevicesLimitReason.setStatus(_A)
_PcoipImagingDevicesModel_Type=OctetString
_PcoipImagingDevicesModel_Object=MibTableColumn
pcoipImagingDevicesModel=_PcoipImagingDevicesModel_Object((1,3,6,1,4,1,25071,1,2,7,1,1,9),_PcoipImagingDevicesModel_Type())
pcoipImagingDevicesModel.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingDevicesModel.setStatus(_A)
_PcoipImagingDevicesStatus_Type=OctetString
_PcoipImagingDevicesStatus_Object=MibTableColumn
pcoipImagingDevicesStatus=_PcoipImagingDevicesStatus_Object((1,3,6,1,4,1,25071,1,2,7,1,1,10),_PcoipImagingDevicesStatus_Type())
pcoipImagingDevicesStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingDevicesStatus.setStatus(_A)
_PcoipImagingDevicesMode_Type=OctetString
_PcoipImagingDevicesMode_Object=MibTableColumn
pcoipImagingDevicesMode=_PcoipImagingDevicesMode_Object((1,3,6,1,4,1,25071,1,2,7,1,1,11),_PcoipImagingDevicesMode_Type())
pcoipImagingDevicesMode.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingDevicesMode.setStatus(_A)
_PcoipImagingDevicesSerial_Type=OctetString
_PcoipImagingDevicesSerial_Object=MibTableColumn
pcoipImagingDevicesSerial=_PcoipImagingDevicesSerial_Object((1,3,6,1,4,1,25071,1,2,7,1,1,12),_PcoipImagingDevicesSerial_Type())
pcoipImagingDevicesSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingDevicesSerial.setStatus(_A)
_PcoipImagingDevicesVID_Type=OctetString
_PcoipImagingDevicesVID_Object=MibTableColumn
pcoipImagingDevicesVID=_PcoipImagingDevicesVID_Object((1,3,6,1,4,1,25071,1,2,7,1,1,13),_PcoipImagingDevicesVID_Type())
pcoipImagingDevicesVID.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingDevicesVID.setStatus(_A)
_PcoipImagingDevicesPID_Type=OctetString
_PcoipImagingDevicesPID_Object=MibTableColumn
pcoipImagingDevicesPID=_PcoipImagingDevicesPID_Object((1,3,6,1,4,1,25071,1,2,7,1,1,14),_PcoipImagingDevicesPID_Type())
pcoipImagingDevicesPID.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingDevicesPID.setStatus(_A)
_PcoipImagingDevicesDate_Type=OctetString
_PcoipImagingDevicesDate_Object=MibTableColumn
pcoipImagingDevicesDate=_PcoipImagingDevicesDate_Object((1,3,6,1,4,1,25071,1,2,7,1,1,15),_PcoipImagingDevicesDate_Type())
pcoipImagingDevicesDate.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipImagingDevicesDate.setStatus(_A)
_TeraPcoipUSBDevices_ObjectIdentity=ObjectIdentity
teraPcoipUSBDevices=_TeraPcoipUSBDevices_ObjectIdentity((1,3,6,1,4,1,25071,1,2,8))
_PcoipUSBDevicesTable_Object=MibTable
pcoipUSBDevicesTable=_PcoipUSBDevicesTable_Object((1,3,6,1,4,1,25071,1,2,8,1))
if mibBuilder.loadTexts:pcoipUSBDevicesTable.setStatus(_A)
_PcoipUSBDevicesEntry_Object=MibTableRow
pcoipUSBDevicesEntry=_PcoipUSBDevicesEntry_Object((1,3,6,1,4,1,25071,1,2,8,1,1))
pcoipUSBDevicesEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:pcoipUSBDevicesEntry.setStatus(_A)
class _PcoipUSBDevicesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_PcoipUSBDevicesIndex_Type.__name__=_C
_PcoipUSBDevicesIndex_Object=MibTableColumn
pcoipUSBDevicesIndex=_PcoipUSBDevicesIndex_Object((1,3,6,1,4,1,25071,1,2,8,1,1,1),_PcoipUSBDevicesIndex_Type())
pcoipUSBDevicesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBDevicesIndex.setStatus(_A)
class _PcoipUSBDevicesSessionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_PcoipUSBDevicesSessionNumber_Type.__name__=_C
_PcoipUSBDevicesSessionNumber_Object=MibTableColumn
pcoipUSBDevicesSessionNumber=_PcoipUSBDevicesSessionNumber_Object((1,3,6,1,4,1,25071,1,2,8,1,1,2),_PcoipUSBDevicesSessionNumber_Type())
pcoipUSBDevicesSessionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBDevicesSessionNumber.setStatus(_A)
_PcoipUSBDevicesPort_Type=OctetString
_PcoipUSBDevicesPort_Object=MibTableColumn
pcoipUSBDevicesPort=_PcoipUSBDevicesPort_Object((1,3,6,1,4,1,25071,1,2,8,1,1,3),_PcoipUSBDevicesPort_Type())
pcoipUSBDevicesPort.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBDevicesPort.setStatus(_A)
_PcoipUSBDevicesModel_Type=OctetString
_PcoipUSBDevicesModel_Object=MibTableColumn
pcoipUSBDevicesModel=_PcoipUSBDevicesModel_Object((1,3,6,1,4,1,25071,1,2,8,1,1,4),_PcoipUSBDevicesModel_Type())
pcoipUSBDevicesModel.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBDevicesModel.setStatus(_A)
_PcoipUSBDevicesStatus_Type=OctetString
_PcoipUSBDevicesStatus_Object=MibTableColumn
pcoipUSBDevicesStatus=_PcoipUSBDevicesStatus_Object((1,3,6,1,4,1,25071,1,2,8,1,1,5),_PcoipUSBDevicesStatus_Type())
pcoipUSBDevicesStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBDevicesStatus.setStatus(_A)
_PcoipUSBDevicesDeviceClass_Type=OctetString
_PcoipUSBDevicesDeviceClass_Object=MibTableColumn
pcoipUSBDevicesDeviceClass=_PcoipUSBDevicesDeviceClass_Object((1,3,6,1,4,1,25071,1,2,8,1,1,6),_PcoipUSBDevicesDeviceClass_Type())
pcoipUSBDevicesDeviceClass.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBDevicesDeviceClass.setStatus(_A)
_PcoipUSBDevicesSubClass_Type=OctetString
_PcoipUSBDevicesSubClass_Object=MibTableColumn
pcoipUSBDevicesSubClass=_PcoipUSBDevicesSubClass_Object((1,3,6,1,4,1,25071,1,2,8,1,1,7),_PcoipUSBDevicesSubClass_Type())
pcoipUSBDevicesSubClass.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBDevicesSubClass.setStatus(_A)
_PcoipUSBDevicesProtocol_Type=OctetString
_PcoipUSBDevicesProtocol_Object=MibTableColumn
pcoipUSBDevicesProtocol=_PcoipUSBDevicesProtocol_Object((1,3,6,1,4,1,25071,1,2,8,1,1,8),_PcoipUSBDevicesProtocol_Type())
pcoipUSBDevicesProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBDevicesProtocol.setStatus(_A)
_PcoipUSBDevicesSerial_Type=OctetString
_PcoipUSBDevicesSerial_Object=MibTableColumn
pcoipUSBDevicesSerial=_PcoipUSBDevicesSerial_Object((1,3,6,1,4,1,25071,1,2,8,1,1,9),_PcoipUSBDevicesSerial_Type())
pcoipUSBDevicesSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBDevicesSerial.setStatus(_A)
_PcoipUSBDevicesVID_Type=OctetString
_PcoipUSBDevicesVID_Object=MibTableColumn
pcoipUSBDevicesVID=_PcoipUSBDevicesVID_Object((1,3,6,1,4,1,25071,1,2,8,1,1,10),_PcoipUSBDevicesVID_Type())
pcoipUSBDevicesVID.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBDevicesVID.setStatus(_A)
_PcoipUSBDevicesPID_Type=OctetString
_PcoipUSBDevicesPID_Object=MibTableColumn
pcoipUSBDevicesPID=_PcoipUSBDevicesPID_Object((1,3,6,1,4,1,25071,1,2,8,1,1,11),_PcoipUSBDevicesPID_Type())
pcoipUSBDevicesPID.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipUSBDevicesPID.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'teraMibModule':teraMibModule,'teraProducts':teraProducts,'teraPcoipV2':teraPcoipV2,'teraPcoipGenStats':teraPcoipGenStats,'pcoipGenStatsTable':pcoipGenStatsTable,'pcoipGenStatsEntry':pcoipGenStatsEntry,_E:pcoipGenStatsSessionNumber,'pcoipGenStatsPacketsSent':pcoipGenStatsPacketsSent,'pcoipGenStatsBytesSent':pcoipGenStatsBytesSent,'pcoipGenStatsPacketsReceived':pcoipGenStatsPacketsReceived,'pcoipGenStatsBytesReceived':pcoipGenStatsBytesReceived,'pcoipGenStatsTxPacketsLost':pcoipGenStatsTxPacketsLost,'pcoipGenStatsSessionDuration':pcoipGenStatsSessionDuration,'teraPcoipNetStats':teraPcoipNetStats,'pcoipNetStatsTable':pcoipNetStatsTable,'pcoipNetStatsEntry':pcoipNetStatsEntry,_F:pcoipNetStatsSessionNumber,'pcoipNetStatsRoundTripLatencyMs':pcoipNetStatsRoundTripLatencyMs,'pcoipNetStatsRXBWkbitPersec':pcoipNetStatsRXBWkbitPersec,'pcoipNetStatsRXBWPeakkbitPersec':pcoipNetStatsRXBWPeakkbitPersec,'pcoipNetStatsRXPacketLossPercent':pcoipNetStatsRXPacketLossPercent,'pcoipNetStatsTXBWkbitPersec':pcoipNetStatsTXBWkbitPersec,'pcoipNetStatsTXBWActiveLimitkbitPersec':pcoipNetStatsTXBWActiveLimitkbitPersec,'pcoipNetStatsTXBWLimitkbitPersec':pcoipNetStatsTXBWLimitkbitPersec,'pcoipNetStatsTXPacketLossPercent':pcoipNetStatsTXPacketLossPercent,'teraPcoipAudioStats':teraPcoipAudioStats,'pcoipAudioStatsTable':pcoipAudioStatsTable,'pcoipAudioStatsEntry':pcoipAudioStatsEntry,_G:pcoipAudioStatsSessionNumber,'pcoipAudioStatsBytesReceived':pcoipAudioStatsBytesReceived,'pcoipAudioStatsBytesSent':pcoipAudioStatsBytesSent,'pcoipAudioStatsRXBWkbitPersec':pcoipAudioStatsRXBWkbitPersec,'pcoipAudioStatsTXBWkbitPersec':pcoipAudioStatsTXBWkbitPersec,'pcoipAudioStatsTXBWLimitkbitPersec':pcoipAudioStatsTXBWLimitkbitPersec,'teraPcoipImagingStats':teraPcoipImagingStats,'pcoipImagingStatsTable':pcoipImagingStatsTable,'pcoipImagingStatsEntry':pcoipImagingStatsEntry,_H:pcoipImagingStatsSessionNumber,'pcoipImagingStatsBytesReceived':pcoipImagingStatsBytesReceived,'pcoipImagingStatsBytesSent':pcoipImagingStatsBytesSent,'pcoipImagingStatsRXBWkbitPersec':pcoipImagingStatsRXBWkbitPersec,'pcoipImagingStatsTXBWkbitPersec':pcoipImagingStatsTXBWkbitPersec,'pcoipImagingStatsEncodedFramesPersec':pcoipImagingStatsEncodedFramesPersec,'pcoipImagingStatsActiveMinimumQuality':pcoipImagingStatsActiveMinimumQuality,'pcoipImagingStatsDecoderCapabilitykbitPersec':pcoipImagingStatsDecoderCapabilitykbitPersec,'pcoipImagingStatsPipelineProcRate':pcoipImagingStatsPipelineProcRate,'teraPcoipUSBStats':teraPcoipUSBStats,'pcoipUSBStatsTable':pcoipUSBStatsTable,'pcoipUSBStatsEntry':pcoipUSBStatsEntry,_I:pcoipUSBStatsSessionNumber,'pcoipUSBStatsBytesReceived':pcoipUSBStatsBytesReceived,'pcoipUSBStatsBytesSent':pcoipUSBStatsBytesSent,'pcoipUSBStatsRXBWkbitPersec':pcoipUSBStatsRXBWkbitPersec,'pcoipUSBStatsTXBWkbitPersec':pcoipUSBStatsTXBWkbitPersec,'teraPcoipGenDevices':teraPcoipGenDevices,'pcoipGenDevicesTable':pcoipGenDevicesTable,'pcoipGenDevicesEntry':pcoipGenDevicesEntry,_J:pcoipGenDevicesSessionNumber,'pcoipGenDevicesName':pcoipGenDevicesName,'pcoipGenDevicesDescription':pcoipGenDevicesDescription,'pcoipGenDevicesGenericTag':pcoipGenDevicesGenericTag,'pcoipGenDevicesPartNumber':pcoipGenDevicesPartNumber,'pcoipGenDevicesFwPartNumber':pcoipGenDevicesFwPartNumber,'pcoipGenDevicesSerialNumber':pcoipGenDevicesSerialNumber,'pcoipGenDevicesHardwareVersion':pcoipGenDevicesHardwareVersion,'pcoipGenDevicesFirmwareVersion':pcoipGenDevicesFirmwareVersion,'pcoipGenDevicesUniqueID':pcoipGenDevicesUniqueID,'pcoipGenDevicesMAC':pcoipGenDevicesMAC,'pcoipGenDevicesUptime':pcoipGenDevicesUptime,'teraPcoipImagingDevices':teraPcoipImagingDevices,'pcoipImagingDevicesTable':pcoipImagingDevicesTable,'pcoipImagingDevicesEntry':pcoipImagingDevicesEntry,_K:pcoipImagingDevicesIndex,'pcoipImagingDevicesSessionNumber':pcoipImagingDevicesSessionNumber,'pcoipImagingDevicesDisplayWidth':pcoipImagingDevicesDisplayWidth,'pcoipImagingDevicesDisplayHeight':pcoipImagingDevicesDisplayHeight,'pcoipImagingDevicesDisplayRefreshRate':pcoipImagingDevicesDisplayRefreshRate,'pcoipImagingDevicesDisplayChangeRate':pcoipImagingDevicesDisplayChangeRate,'pcoipImagingDevicesDisplayProcessRate':pcoipImagingDevicesDisplayProcessRate,'pcoipImagingDevicesLimitReason':pcoipImagingDevicesLimitReason,'pcoipImagingDevicesModel':pcoipImagingDevicesModel,'pcoipImagingDevicesStatus':pcoipImagingDevicesStatus,'pcoipImagingDevicesMode':pcoipImagingDevicesMode,'pcoipImagingDevicesSerial':pcoipImagingDevicesSerial,'pcoipImagingDevicesVID':pcoipImagingDevicesVID,'pcoipImagingDevicesPID':pcoipImagingDevicesPID,'pcoipImagingDevicesDate':pcoipImagingDevicesDate,'teraPcoipUSBDevices':teraPcoipUSBDevices,'pcoipUSBDevicesTable':pcoipUSBDevicesTable,'pcoipUSBDevicesEntry':pcoipUSBDevicesEntry,_L:pcoipUSBDevicesIndex,'pcoipUSBDevicesSessionNumber':pcoipUSBDevicesSessionNumber,'pcoipUSBDevicesPort':pcoipUSBDevicesPort,'pcoipUSBDevicesModel':pcoipUSBDevicesModel,'pcoipUSBDevicesStatus':pcoipUSBDevicesStatus,'pcoipUSBDevicesDeviceClass':pcoipUSBDevicesDeviceClass,'pcoipUSBDevicesSubClass':pcoipUSBDevicesSubClass,'pcoipUSBDevicesProtocol':pcoipUSBDevicesProtocol,'pcoipUSBDevicesSerial':pcoipUSBDevicesSerial,'pcoipUSBDevicesVID':pcoipUSBDevicesVID,'pcoipUSBDevicesPID':pcoipUSBDevicesPID})