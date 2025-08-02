_T='slSonetFsSts'
_S='activate'
_R='ms2250'
_Q='ms2000'
_P='ms1750'
_O='disable'
_N='enable'
_M='enabled'
_L='disabled'
_K='slSonetFsIfIndex'
_J='none'
_I='resetCounters'
_H='SL-SONET-MIB'
_G='DisplayString'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_E,'InterfaceIndex',_F)
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
sitelight,=mibBuilder.importSymbols('SL-NE-MIB','sitelight')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention','TruthValue')
slSonetMib=ModuleIdentity((1,3,6,1,4,1,4515,1,6))
class SignalLabel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,18,19,20,21,22,27)));namedValues=NamedValues(*(('sigUnequipped',0),('sigEquipped',1),('sigPathFloatVt',2),('sigPathLoackedVt',3),('sigPathAsynchDs3',4),('sigPathSyntran',5),('sigPathAsyncDs4na',18),('sigPathAtm',19),('sigPathDqdb',20),('sigPathFddi',21),('sigPathHdlc',22),('sigPathGfp',27)))
_SlSonetConfig_ObjectIdentity=ObjectIdentity
slSonetConfig=_SlSonetConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,6,1))
_SlSonetConfigTable_Object=MibTable
slSonetConfigTable=_SlSonetConfigTable_Object((1,3,6,1,4,1,4515,1,6,1,1))
if mibBuilder.loadTexts:slSonetConfigTable.setStatus(_A)
_SlSonetConfigEntry_Object=MibTableRow
slSonetConfigEntry=_SlSonetConfigEntry_Object((1,3,6,1,4,1,4515,1,6,1,1,1))
slSonetConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:slSonetConfigEntry.setStatus(_A)
class _SlSonetConfigFrameScramble_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SlSonetConfigFrameScramble_Type.__name__=_C
_SlSonetConfigFrameScramble_Object=MibTableColumn
slSonetConfigFrameScramble=_SlSonetConfigFrameScramble_Object((1,3,6,1,4,1,4515,1,6,1,1,1,1),_SlSonetConfigFrameScramble_Type())
slSonetConfigFrameScramble.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetConfigFrameScramble.setStatus(_A)
class _SlSonetConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('sonetSts3',1),('sonetSts3c',2),('sonetSts12',3),('sonetSts12c',4),('sonetSts48c',5),('sonetSts3cx4',6),('sonetSts48',7),('sonetSts3cx16',8),('sonetSts3x16',9),('sonetSts12cx4',10),('sonetSts12x4',11),('sonetSts192c',12),('sonetStsOther',13)))
_SlSonetConfigType_Type.__name__=_C
_SlSonetConfigType_Object=MibTableColumn
slSonetConfigType=_SlSonetConfigType_Object((1,3,6,1,4,1,4515,1,6,1,1,1,2),_SlSonetConfigType_Type())
slSonetConfigType.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetConfigType.setStatus(_A)
class _SlSonetConfigDccSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sonetLineDcc',1),('sonetSectionDcc',2),('sonetInband',3)))
_SlSonetConfigDccSelection_Type.__name__=_C
_SlSonetConfigDccSelection_Object=MibTableColumn
slSonetConfigDccSelection=_SlSonetConfigDccSelection_Object((1,3,6,1,4,1,4515,1,6,1,1,1,3),_SlSonetConfigDccSelection_Type())
slSonetConfigDccSelection.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetConfigDccSelection.setStatus(_A)
class _SlSonetResetAllCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_SlSonetResetAllCounters_Type.__name__=_C
_SlSonetResetAllCounters_Object=MibTableColumn
slSonetResetAllCounters=_SlSonetResetAllCounters_Object((1,3,6,1,4,1,4515,1,6,1,1,1,4),_SlSonetResetAllCounters_Type())
slSonetResetAllCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetResetAllCounters.setStatus(_A)
class _SlSonetPortThresholdTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_L,2)))
_SlSonetPortThresholdTrapEnable_Type.__name__=_C
_SlSonetPortThresholdTrapEnable_Object=MibTableColumn
slSonetPortThresholdTrapEnable=_SlSonetPortThresholdTrapEnable_Object((1,3,6,1,4,1,4515,1,6,1,1,1,5),_SlSonetPortThresholdTrapEnable_Type())
slSonetPortThresholdTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetPortThresholdTrapEnable.setStatus(_A)
class _SlSonetConfigSdThreshold_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,9))
_SlSonetConfigSdThreshold_Type.__name__=_C
_SlSonetConfigSdThreshold_Object=MibTableColumn
slSonetConfigSdThreshold=_SlSonetConfigSdThreshold_Object((1,3,6,1,4,1,4515,1,6,1,1,1,6),_SlSonetConfigSdThreshold_Type())
slSonetConfigSdThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetConfigSdThreshold.setStatus(_A)
class _SlSonetConfigSfThreshold_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,5))
_SlSonetConfigSfThreshold_Type.__name__=_C
_SlSonetConfigSfThreshold_Object=MibTableColumn
slSonetConfigSfThreshold=_SlSonetConfigSfThreshold_Object((1,3,6,1,4,1,4515,1,6,1,1,1,7),_SlSonetConfigSfThreshold_Type())
slSonetConfigSfThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetConfigSfThreshold.setStatus(_A)
class _SlSonetCompression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('uncompress',0),('posCompress32',1),('posCompress16',2)))
_SlSonetCompression_Type.__name__=_C
_SlSonetCompression_Object=MibTableColumn
slSonetCompression=_SlSonetCompression_Object((1,3,6,1,4,1,4515,1,6,1,1,1,9),_SlSonetCompression_Type())
slSonetCompression.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetCompression.setStatus(_A)
class _SlSonetOverheadTunneling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),('lineDcc',1),('k1k2',2),('full',3)))
_SlSonetOverheadTunneling_Type.__name__=_C
_SlSonetOverheadTunneling_Object=MibTableColumn
slSonetOverheadTunneling=_SlSonetOverheadTunneling_Object((1,3,6,1,4,1,4515,1,6,1,1,1,10),_SlSonetOverheadTunneling_Type())
slSonetOverheadTunneling.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetOverheadTunneling.setStatus(_A)
_SlSonetLopBitmask_Type=Counter64
_SlSonetLopBitmask_Object=MibTableColumn
slSonetLopBitmask=_SlSonetLopBitmask_Object((1,3,6,1,4,1,4515,1,6,1,1,1,11),_SlSonetLopBitmask_Type())
slSonetLopBitmask.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetLopBitmask.setStatus(_A)
_SlSonetTdmTrunk_Type=TruthValue
_SlSonetTdmTrunk_Object=MibTableColumn
slSonetTdmTrunk=_SlSonetTdmTrunk_Object((1,3,6,1,4,1,4515,1,6,1,1,1,12),_SlSonetTdmTrunk_Type())
slSonetTdmTrunk.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetTdmTrunk.setStatus(_A)
_SlSonetFsApply_Type=Integer32
_SlSonetFsApply_Object=MibTableColumn
slSonetFsApply=_SlSonetFsApply_Object((1,3,6,1,4,1,4515,1,6,1,1,1,13),_SlSonetFsApply_Type())
slSonetFsApply.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetFsApply.setStatus(_A)
class _SlSonetTxLte_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5)));namedValues=NamedValues(*(('ssb00',1),('ssb10',2),('auto',5)))
_SlSonetTxLte_Type.__name__=_C
_SlSonetTxLte_Object=MibTableColumn
slSonetTxLte=_SlSonetTxLte_Object((1,3,6,1,4,1,4515,1,6,1,1,1,14),_SlSonetTxLte_Type())
slSonetTxLte.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetTxLte.setStatus(_A)
class _SlSonetReceivedLte_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ssb00',1),('ssb10',2),('ssb01',3),('ssb11',4),('ssbinv',5)))
_SlSonetReceivedLte_Type.__name__=_C
_SlSonetReceivedLte_Object=MibTableColumn
slSonetReceivedLte=_SlSonetReceivedLte_Object((1,3,6,1,4,1,4515,1,6,1,1,1,15),_SlSonetReceivedLte_Type())
slSonetReceivedLte.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetReceivedLte.setStatus(_A)
class _SlSonetResetPmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_SlSonetResetPmThreshold_Type.__name__=_C
_SlSonetResetPmThreshold_Object=MibTableColumn
slSonetResetPmThreshold=_SlSonetResetPmThreshold_Object((1,3,6,1,4,1,4515,1,6,1,1,1,16),_SlSonetResetPmThreshold_Type())
slSonetResetPmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetResetPmThreshold.setStatus(_A)
class _SlSonetResetAlsParams_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_SlSonetResetAlsParams_Type.__name__=_C
_SlSonetResetAlsParams_Object=MibTableColumn
slSonetResetAlsParams=_SlSonetResetAlsParams_Object((1,3,6,1,4,1,4515,1,6,1,1,1,17),_SlSonetResetAlsParams_Type())
slSonetResetAlsParams.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetResetAlsParams.setStatus(_A)
class _SlSonetTransceiverType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('shortWave',2),('longWave',3)))
_SlSonetTransceiverType_Type.__name__=_C
_SlSonetTransceiverType_Object=MibTableColumn
slSonetTransceiverType=_SlSonetTransceiverType_Object((1,3,6,1,4,1,4515,1,6,1,1,1,18),_SlSonetTransceiverType_Type())
slSonetTransceiverType.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetTransceiverType.setStatus(_A)
class _SlSonetTransceiverMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('sm',2),('mm',3)))
_SlSonetTransceiverMedia_Type.__name__=_C
_SlSonetTransceiverMedia_Object=MibTableColumn
slSonetTransceiverMedia=_SlSonetTransceiverMedia_Object((1,3,6,1,4,1,4515,1,6,1,1,1,19),_SlSonetTransceiverMedia_Type())
slSonetTransceiverMedia.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetTransceiverMedia.setStatus(_A)
_SlSonetOh_ObjectIdentity=ObjectIdentity
slSonetOh=_SlSonetOh_ObjectIdentity((1,3,6,1,4,1,4515,1,6,2))
_SlSonetOhTrace_ObjectIdentity=ObjectIdentity
slSonetOhTrace=_SlSonetOhTrace_ObjectIdentity((1,3,6,1,4,1,4515,1,6,2,1))
_SlSonetTraceTable_Object=MibTable
slSonetTraceTable=_SlSonetTraceTable_Object((1,3,6,1,4,1,4515,1,6,2,1,1))
if mibBuilder.loadTexts:slSonetTraceTable.setStatus(_A)
_SlSonetTraceEntry_Object=MibTableRow
slSonetTraceEntry=_SlSonetTraceEntry_Object((1,3,6,1,4,1,4515,1,6,2,1,1,1))
slSonetTraceEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:slSonetTraceEntry.setStatus(_A)
class _SlSonetTraceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),('monitoring',3)))
_SlSonetTraceMode_Type.__name__=_C
_SlSonetTraceMode_Object=MibTableColumn
slSonetTraceMode=_SlSonetTraceMode_Object((1,3,6,1,4,1,4515,1,6,2,1,1,1,1),_SlSonetTraceMode_Type())
slSonetTraceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetTraceMode.setStatus(_A)
class _SlSonetTraceToTransmit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,62))
_SlSonetTraceToTransmit_Type.__name__=_G
_SlSonetTraceToTransmit_Object=MibTableColumn
slSonetTraceToTransmit=_SlSonetTraceToTransmit_Object((1,3,6,1,4,1,4515,1,6,2,1,1,1,2),_SlSonetTraceToTransmit_Type())
slSonetTraceToTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetTraceToTransmit.setStatus(_A)
class _SlSonetTraceToExpect_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,62))
_SlSonetTraceToExpect_Type.__name__=_G
_SlSonetTraceToExpect_Object=MibTableColumn
slSonetTraceToExpect=_SlSonetTraceToExpect_Object((1,3,6,1,4,1,4515,1,6,2,1,1,1,3),_SlSonetTraceToExpect_Type())
slSonetTraceToExpect.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetTraceToExpect.setStatus(_A)
_SlSonetTraceFailure_Type=TruthValue
_SlSonetTraceFailure_Object=MibTableColumn
slSonetTraceFailure=_SlSonetTraceFailure_Object((1,3,6,1,4,1,4515,1,6,2,1,1,1,4),_SlSonetTraceFailure_Type())
slSonetTraceFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetTraceFailure.setStatus(_A)
class _SlSonetTraceReceived_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,62))
_SlSonetTraceReceived_Type.__name__=_G
_SlSonetTraceReceived_Object=MibTableColumn
slSonetTraceReceived=_SlSonetTraceReceived_Object((1,3,6,1,4,1,4515,1,6,2,1,1,1,5),_SlSonetTraceReceived_Type())
slSonetTraceReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetTraceReceived.setStatus(_A)
_SlSonetOhSl_ObjectIdentity=ObjectIdentity
slSonetOhSl=_SlSonetOhSl_ObjectIdentity((1,3,6,1,4,1,4515,1,6,2,2))
_SlSonetSlTable_Object=MibTable
slSonetSlTable=_SlSonetSlTable_Object((1,3,6,1,4,1,4515,1,6,2,2,1))
if mibBuilder.loadTexts:slSonetSlTable.setStatus(_A)
_SlSonetSlEntry_Object=MibTableRow
slSonetSlEntry=_SlSonetSlEntry_Object((1,3,6,1,4,1,4515,1,6,2,2,1,1))
slSonetSlEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:slSonetSlEntry.setStatus(_A)
_SlSonetSlToTransmit_Type=SignalLabel
_SlSonetSlToTransmit_Object=MibTableColumn
slSonetSlToTransmit=_SlSonetSlToTransmit_Object((1,3,6,1,4,1,4515,1,6,2,2,1,1,2),_SlSonetSlToTransmit_Type())
slSonetSlToTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetSlToTransmit.setStatus(_A)
_SlSonetSlToExpect_Type=SignalLabel
_SlSonetSlToExpect_Object=MibTableColumn
slSonetSlToExpect=_SlSonetSlToExpect_Object((1,3,6,1,4,1,4515,1,6,2,2,1,1,3),_SlSonetSlToExpect_Type())
slSonetSlToExpect.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetSlToExpect.setStatus(_A)
_SlSonetSlFailure_Type=TruthValue
_SlSonetSlFailure_Object=MibTableColumn
slSonetSlFailure=_SlSonetSlFailure_Object((1,3,6,1,4,1,4515,1,6,2,2,1,1,4),_SlSonetSlFailure_Type())
slSonetSlFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetSlFailure.setStatus(_A)
class _SlSonetSlReceived_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SlSonetSlReceived_Type.__name__=_C
_SlSonetSlReceived_Object=MibTableColumn
slSonetSlReceived=_SlSonetSlReceived_Object((1,3,6,1,4,1,4515,1,6,2,2,1,1,5),_SlSonetSlReceived_Type())
slSonetSlReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetSlReceived.setStatus(_A)
_SlSonetOhTraps_ObjectIdentity=ObjectIdentity
slSonetOhTraps=_SlSonetOhTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,6,2,3))
_SlSonetPos_ObjectIdentity=ObjectIdentity
slSonetPos=_SlSonetPos_ObjectIdentity((1,3,6,1,4,1,4515,1,6,6))
_SlSonetPosTable_Object=MibTable
slSonetPosTable=_SlSonetPosTable_Object((1,3,6,1,4,1,4515,1,6,6,1))
if mibBuilder.loadTexts:slSonetPosTable.setStatus(_A)
_SlSonetPosEntry_Object=MibTableRow
slSonetPosEntry=_SlSonetPosEntry_Object((1,3,6,1,4,1,4515,1,6,6,1,1))
slSonetPosEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:slSonetPosEntry.setStatus(_A)
_SlSonetPosFcs_Type=Gauge32
_SlSonetPosFcs_Object=MibTableColumn
slSonetPosFcs=_SlSonetPosFcs_Object((1,3,6,1,4,1,4515,1,6,6,1,1,1),_SlSonetPosFcs_Type())
slSonetPosFcs.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetPosFcs.setStatus(_A)
_SlSonetPosAbort_Type=Gauge32
_SlSonetPosAbort_Object=MibTableColumn
slSonetPosAbort=_SlSonetPosAbort_Object((1,3,6,1,4,1,4515,1,6,6,1,1,2),_SlSonetPosAbort_Type())
slSonetPosAbort.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetPosAbort.setStatus(_A)
_SlSonetPosMinViolation_Type=Gauge32
_SlSonetPosMinViolation_Object=MibTableColumn
slSonetPosMinViolation=_SlSonetPosMinViolation_Object((1,3,6,1,4,1,4515,1,6,6,1,1,3),_SlSonetPosMinViolation_Type())
slSonetPosMinViolation.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetPosMinViolation.setStatus(_A)
_SlSonetPosMaxViolation_Type=Gauge32
_SlSonetPosMaxViolation_Object=MibTableColumn
slSonetPosMaxViolation=_SlSonetPosMaxViolation_Object((1,3,6,1,4,1,4515,1,6,6,1,1,4),_SlSonetPosMaxViolation_Type())
slSonetPosMaxViolation.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetPosMaxViolation.setStatus(_A)
_SlSonetPosRxfifoDiscard_Type=Gauge32
_SlSonetPosRxfifoDiscard_Object=MibTableColumn
slSonetPosRxfifoDiscard=_SlSonetPosRxfifoDiscard_Object((1,3,6,1,4,1,4515,1,6,6,1,1,5),_SlSonetPosRxfifoDiscard_Type())
slSonetPosRxfifoDiscard.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetPosRxfifoDiscard.setStatus(_A)
_SlSonetPosPacketReceived_Type=Counter64
_SlSonetPosPacketReceived_Object=MibTableColumn
slSonetPosPacketReceived=_SlSonetPosPacketReceived_Object((1,3,6,1,4,1,4515,1,6,6,1,1,6),_SlSonetPosPacketReceived_Type())
slSonetPosPacketReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetPosPacketReceived.setStatus(_A)
_SlSonetPosPacketReceivedOk_Type=Counter64
_SlSonetPosPacketReceivedOk_Object=MibTableColumn
slSonetPosPacketReceivedOk=_SlSonetPosPacketReceivedOk_Object((1,3,6,1,4,1,4515,1,6,6,1,1,7),_SlSonetPosPacketReceivedOk_Type())
slSonetPosPacketReceivedOk.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetPosPacketReceivedOk.setStatus(_A)
_SlSonetAls_ObjectIdentity=ObjectIdentity
slSonetAls=_SlSonetAls_ObjectIdentity((1,3,6,1,4,1,4515,1,6,7))
_SlSonetAlsTable_Object=MibTable
slSonetAlsTable=_SlSonetAlsTable_Object((1,3,6,1,4,1,4515,1,6,7,1))
if mibBuilder.loadTexts:slSonetAlsTable.setStatus(_A)
_SlSonetAlsEntry_Object=MibTableRow
slSonetAlsEntry=_SlSonetAlsEntry_Object((1,3,6,1,4,1,4515,1,6,7,1,1))
slSonetAlsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:slSonetAlsEntry.setStatus(_A)
class _SlSonetAlsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_SlSonetAlsMode_Type.__name__=_C
_SlSonetAlsMode_Object=MibTableColumn
slSonetAlsMode=_SlSonetAlsMode_Object((1,3,6,1,4,1,4515,1,6,7,1,1,1),_SlSonetAlsMode_Type())
slSonetAlsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetAlsMode.setStatus(_A)
class _SlSonetLosDeclareTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ms500',1),('ms550',2),('ms600',3)))
_SlSonetLosDeclareTime_Type.__name__=_C
_SlSonetLosDeclareTime_Object=MibTableColumn
slSonetLosDeclareTime=_SlSonetLosDeclareTime_Object((1,3,6,1,4,1,4515,1,6,7,1,1,2),_SlSonetLosDeclareTime_Type())
slSonetLosDeclareTime.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetLosDeclareTime.setStatus(_A)
class _SlSonetTestPulseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('s80',1),('s90',2),('s100',3)))
_SlSonetTestPulseTime_Type.__name__=_C
_SlSonetTestPulseTime_Object=MibTableColumn
slSonetTestPulseTime=_SlSonetTestPulseTime_Object((1,3,6,1,4,1,4515,1,6,7,1,1,3),_SlSonetTestPulseTime_Type())
slSonetTestPulseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetTestPulseTime.setStatus(_A)
class _SlSonetManualPulseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3)))
_SlSonetManualPulseTime_Type.__name__=_C
_SlSonetManualPulseTime_Object=MibTableColumn
slSonetManualPulseTime=_SlSonetManualPulseTime_Object((1,3,6,1,4,1,4515,1,6,7,1,1,4),_SlSonetManualPulseTime_Type())
slSonetManualPulseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetManualPulseTime.setStatus(_A)
class _SlSonetAutomaticPulseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3)))
_SlSonetAutomaticPulseTime_Type.__name__=_C
_SlSonetAutomaticPulseTime_Object=MibTableColumn
slSonetAutomaticPulseTime=_SlSonetAutomaticPulseTime_Object((1,3,6,1,4,1,4515,1,6,7,1,1,5),_SlSonetAutomaticPulseTime_Type())
slSonetAutomaticPulseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetAutomaticPulseTime.setStatus(_A)
class _SlSonetAutomaticDelayTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,300))
_SlSonetAutomaticDelayTime_Type.__name__=_C
_SlSonetAutomaticDelayTime_Object=MibTableColumn
slSonetAutomaticDelayTime=_SlSonetAutomaticDelayTime_Object((1,3,6,1,4,1,4515,1,6,7,1,1,6),_SlSonetAutomaticDelayTime_Type())
slSonetAutomaticDelayTime.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetAutomaticDelayTime.setStatus(_A)
class _SlSonetLaserTestActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_S,1))
_SlSonetLaserTestActivate_Type.__name__=_C
_SlSonetLaserTestActivate_Object=MibTableColumn
slSonetLaserTestActivate=_SlSonetLaserTestActivate_Object((1,3,6,1,4,1,4515,1,6,7,1,1,7),_SlSonetLaserTestActivate_Type())
slSonetLaserTestActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetLaserTestActivate.setStatus(_A)
class _SlSonetLaserManualActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_S,1))
_SlSonetLaserManualActivate_Type.__name__=_C
_SlSonetLaserManualActivate_Object=MibTableColumn
slSonetLaserManualActivate=_SlSonetLaserManualActivate_Object((1,3,6,1,4,1,4515,1,6,7,1,1,8),_SlSonetLaserManualActivate_Type())
slSonetLaserManualActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetLaserManualActivate.setStatus(_A)
_SlSonetFs_ObjectIdentity=ObjectIdentity
slSonetFs=_SlSonetFs_ObjectIdentity((1,3,6,1,4,1,4515,1,6,8))
_SlSonetFsTable_Object=MibTable
slSonetFsTable=_SlSonetFsTable_Object((1,3,6,1,4,1,4515,1,6,8,1))
if mibBuilder.loadTexts:slSonetFsTable.setStatus(_A)
_SlSonetFsEntry_Object=MibTableRow
slSonetFsEntry=_SlSonetFsEntry_Object((1,3,6,1,4,1,4515,1,6,8,1,1))
slSonetFsEntry.setIndexNames((0,_H,_K),(0,_H,_T))
if mibBuilder.loadTexts:slSonetFsEntry.setStatus(_A)
_SlSonetFsIfIndex_Type=InterfaceIndex
_SlSonetFsIfIndex_Object=MibTableColumn
slSonetFsIfIndex=_SlSonetFsIfIndex_Object((1,3,6,1,4,1,4515,1,6,8,1,1,1),_SlSonetFsIfIndex_Type())
slSonetFsIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetFsIfIndex.setStatus(_A)
_SlSonetFsSts_Type=Integer32
_SlSonetFsSts_Object=MibTableColumn
slSonetFsSts=_SlSonetFsSts_Object((1,3,6,1,4,1,4515,1,6,8,1,1,2),_SlSonetFsSts_Type())
slSonetFsSts.setMaxAccess(_D)
if mibBuilder.loadTexts:slSonetFsSts.setStatus(_A)
_SlSonetFsWidth_Type=Integer32
_SlSonetFsWidth_Object=MibTableColumn
slSonetFsWidth=_SlSonetFsWidth_Object((1,3,6,1,4,1,4515,1,6,8,1,1,3),_SlSonetFsWidth_Type())
slSonetFsWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetFsWidth.setStatus(_A)
_SlSonetFsFullPathTermination_Type=TruthValue
_SlSonetFsFullPathTermination_Object=MibTableColumn
slSonetFsFullPathTermination=_SlSonetFsFullPathTermination_Object((1,3,6,1,4,1,4515,1,6,8,1,1,4),_SlSonetFsFullPathTermination_Type())
slSonetFsFullPathTermination.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetFsFullPathTermination.setStatus(_A)
class _SlSonetFsGranularity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vc4',1),('vc3',2)))
_SlSonetFsGranularity_Type.__name__=_C
_SlSonetFsGranularity_Object=MibTableColumn
slSonetFsGranularity=_SlSonetFsGranularity_Object((1,3,6,1,4,1,4515,1,6,8,1,1,5),_SlSonetFsGranularity_Type())
slSonetFsGranularity.setMaxAccess(_B)
if mibBuilder.loadTexts:slSonetFsGranularity.setStatus(_A)
_SlSonetTraps_ObjectIdentity=ObjectIdentity
slSonetTraps=_SlSonetTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,6,11))
slSonetFsTableChange=NotificationType((1,3,6,1,4,1,4515,1,6,11,1))
slSonetFsTableChange.setObjects((_H,_K))
if mibBuilder.loadTexts:slSonetFsTableChange.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'SignalLabel':SignalLabel,'slSonetMib':slSonetMib,'slSonetConfig':slSonetConfig,'slSonetConfigTable':slSonetConfigTable,'slSonetConfigEntry':slSonetConfigEntry,'slSonetConfigFrameScramble':slSonetConfigFrameScramble,'slSonetConfigType':slSonetConfigType,'slSonetConfigDccSelection':slSonetConfigDccSelection,'slSonetResetAllCounters':slSonetResetAllCounters,'slSonetPortThresholdTrapEnable':slSonetPortThresholdTrapEnable,'slSonetConfigSdThreshold':slSonetConfigSdThreshold,'slSonetConfigSfThreshold':slSonetConfigSfThreshold,'slSonetCompression':slSonetCompression,'slSonetOverheadTunneling':slSonetOverheadTunneling,'slSonetLopBitmask':slSonetLopBitmask,'slSonetTdmTrunk':slSonetTdmTrunk,'slSonetFsApply':slSonetFsApply,'slSonetTxLte':slSonetTxLte,'slSonetReceivedLte':slSonetReceivedLte,'slSonetResetPmThreshold':slSonetResetPmThreshold,'slSonetResetAlsParams':slSonetResetAlsParams,'slSonetTransceiverType':slSonetTransceiverType,'slSonetTransceiverMedia':slSonetTransceiverMedia,'slSonetOh':slSonetOh,'slSonetOhTrace':slSonetOhTrace,'slSonetTraceTable':slSonetTraceTable,'slSonetTraceEntry':slSonetTraceEntry,'slSonetTraceMode':slSonetTraceMode,'slSonetTraceToTransmit':slSonetTraceToTransmit,'slSonetTraceToExpect':slSonetTraceToExpect,'slSonetTraceFailure':slSonetTraceFailure,'slSonetTraceReceived':slSonetTraceReceived,'slSonetOhSl':slSonetOhSl,'slSonetSlTable':slSonetSlTable,'slSonetSlEntry':slSonetSlEntry,'slSonetSlToTransmit':slSonetSlToTransmit,'slSonetSlToExpect':slSonetSlToExpect,'slSonetSlFailure':slSonetSlFailure,'slSonetSlReceived':slSonetSlReceived,'slSonetOhTraps':slSonetOhTraps,'slSonetPos':slSonetPos,'slSonetPosTable':slSonetPosTable,'slSonetPosEntry':slSonetPosEntry,'slSonetPosFcs':slSonetPosFcs,'slSonetPosAbort':slSonetPosAbort,'slSonetPosMinViolation':slSonetPosMinViolation,'slSonetPosMaxViolation':slSonetPosMaxViolation,'slSonetPosRxfifoDiscard':slSonetPosRxfifoDiscard,'slSonetPosPacketReceived':slSonetPosPacketReceived,'slSonetPosPacketReceivedOk':slSonetPosPacketReceivedOk,'slSonetAls':slSonetAls,'slSonetAlsTable':slSonetAlsTable,'slSonetAlsEntry':slSonetAlsEntry,'slSonetAlsMode':slSonetAlsMode,'slSonetLosDeclareTime':slSonetLosDeclareTime,'slSonetTestPulseTime':slSonetTestPulseTime,'slSonetManualPulseTime':slSonetManualPulseTime,'slSonetAutomaticPulseTime':slSonetAutomaticPulseTime,'slSonetAutomaticDelayTime':slSonetAutomaticDelayTime,'slSonetLaserTestActivate':slSonetLaserTestActivate,'slSonetLaserManualActivate':slSonetLaserManualActivate,'slSonetFs':slSonetFs,'slSonetFsTable':slSonetFsTable,'slSonetFsEntry':slSonetFsEntry,_K:slSonetFsIfIndex,_T:slSonetFsSts,'slSonetFsWidth':slSonetFsWidth,'slSonetFsFullPathTermination':slSonetFsFullPathTermination,'slSonetFsGranularity':slSonetFsGranularity,'slSonetTraps':slSonetTraps,'slSonetFsTableChange':slSonetFsTableChange})