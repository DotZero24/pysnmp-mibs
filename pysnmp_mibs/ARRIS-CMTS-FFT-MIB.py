_J='dcxFftPayloadIndex'
_I='ARRIS-CMTS-FFT-MIB'
_H='TruthValue'
_G='read-only'
_F='ifIndex'
_E='IF-MIB'
_D='Unsigned32'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cmtsCommon,=mibBuilder.importSymbols('ARRIS-MIB','cmtsCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_H)
cmtsFftMIB=ModuleIdentity((1,3,6,1,4,1,4115,1,4,5,1))
if mibBuilder.loadTexts:cmtsFftMIB.setRevisions(('2014-08-12 00:00','2006-01-23 00:00'))
class DcxFftPayloadBuffer(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_DcxFftObjects_ObjectIdentity=ObjectIdentity
dcxFftObjects=_DcxFftObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,4,5,1,1))
_DcxFftUpstreamChannelTable_Object=MibTable
dcxFftUpstreamChannelTable=_DcxFftUpstreamChannelTable_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1))
if mibBuilder.loadTexts:dcxFftUpstreamChannelTable.setStatus(_A)
_DcxFftUpstreamChannelEntry_Object=MibTableRow
dcxFftUpstreamChannelEntry=_DcxFftUpstreamChannelEntry_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1))
dcxFftUpstreamChannelEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dcxFftUpstreamChannelEntry.setStatus(_A)
class _DcxFftSize_Type(Unsigned32):defaultValue=2048;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,256),ValueRangeConstraint(512,512),ValueRangeConstraint(1024,1024),ValueRangeConstraint(2048,2048),ValueRangeConstraint(4096,4096))
_DcxFftSize_Type.__name__=_D
_DcxFftSize_Object=MibTableColumn
dcxFftSize=_DcxFftSize_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,1),_DcxFftSize_Type())
dcxFftSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxFftSize.setStatus(_A)
class _DcxFftSampleRate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('adcRate',1),('halfAdcRate',2),('quarterAdcRate',3),('quadrupleSymbolRate',4),('reserved5',5),('reserved6',6),('reserved7',7),('reserved8',8)))
_DcxFftSampleRate_Type.__name__=_C
_DcxFftSampleRate_Object=MibTableColumn
dcxFftSampleRate=_DcxFftSampleRate_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,2),_DcxFftSampleRate_Type())
dcxFftSampleRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxFftSampleRate.setStatus(_A)
class _DcxFftCentreFrequency_Type(Integer32):defaultValue=40960000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-81920000,81920000))
_DcxFftCentreFrequency_Type.__name__=_C
_DcxFftCentreFrequency_Object=MibTableColumn
dcxFftCentreFrequency=_DcxFftCentreFrequency_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,3),_DcxFftCentreFrequency_Type())
dcxFftCentreFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxFftCentreFrequency.setStatus(_A)
if mibBuilder.loadTexts:dcxFftCentreFrequency.setUnits('hertz')
class _DcxFftWindowing_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('rectangular',1),('hanning',2),('hamming',3),('blackman',4),('blackmanHarris',5)))
_DcxFftWindowing_Type.__name__=_C
_DcxFftWindowing_Object=MibTableColumn
dcxFftWindowing=_DcxFftWindowing_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,4),_DcxFftWindowing_Type())
dcxFftWindowing.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxFftWindowing.setStatus(_A)
class _DcxFftLogAveragingTimeConstant_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_DcxFftLogAveragingTimeConstant_Type.__name__=_D
_DcxFftLogAveragingTimeConstant_Object=MibTableColumn
dcxFftLogAveragingTimeConstant=_DcxFftLogAveragingTimeConstant_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,5),_DcxFftLogAveragingTimeConstant_Type())
dcxFftLogAveragingTimeConstant.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxFftLogAveragingTimeConstant.setStatus(_A)
class _DcxFftOutputFormat_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('raw',1),('fftIQ',2),('fftPower',3),('fftAmplitude',4)))
_DcxFftOutputFormat_Type.__name__=_C
_DcxFftOutputFormat_Object=MibTableColumn
dcxFftOutputFormat=_DcxFftOutputFormat_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,6),_DcxFftOutputFormat_Type())
dcxFftOutputFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxFftOutputFormat.setStatus(_A)
class _DcxFftOperatingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('baseSpectrum',1),('burstSpectrum',2),('periodicSpectrum',3)))
_DcxFftOperatingMode_Type.__name__=_C
_DcxFftOperatingMode_Object=MibTableColumn
dcxFftOperatingMode=_DcxFftOperatingMode_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,7),_DcxFftOperatingMode_Type())
dcxFftOperatingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxFftOperatingMode.setStatus(_A)
class _DcxFftIdleInterval_Type(Unsigned32):defaultValue=50000
_DcxFftIdleInterval_Type.__name__=_D
_DcxFftIdleInterval_Object=MibTableColumn
dcxFftIdleInterval=_DcxFftIdleInterval_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,8),_DcxFftIdleInterval_Type())
dcxFftIdleInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxFftIdleInterval.setStatus(_A)
class _DcxFftBurstSid_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
_DcxFftBurstSid_Type.__name__=_D
_DcxFftBurstSid_Object=MibTableColumn
dcxFftBurstSid=_DcxFftBurstSid_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,9),_DcxFftBurstSid_Type())
dcxFftBurstSid.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxFftBurstSid.setStatus(_A)
class _DcxFftBurstIUC_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_DcxFftBurstIUC_Type.__name__=_C
_DcxFftBurstIUC_Object=MibTableColumn
dcxFftBurstIUC=_DcxFftBurstIUC_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,10),_DcxFftBurstIUC_Type())
dcxFftBurstIUC.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxFftBurstIUC.setStatus(_A)
class _DcxFftLogicalChannel_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,3))
_DcxFftLogicalChannel_Type.__name__=_C
_DcxFftLogicalChannel_Object=MibTableColumn
dcxFftLogicalChannel=_DcxFftLogicalChannel_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,11),_DcxFftLogicalChannel_Type())
dcxFftLogicalChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxFftLogicalChannel.setStatus(_A)
class _DcxFftTriggerCount_Type(Unsigned32):defaultValue=1
_DcxFftTriggerCount_Type.__name__=_D
_DcxFftTriggerCount_Object=MibTableColumn
dcxFftTriggerCount=_DcxFftTriggerCount_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,12),_DcxFftTriggerCount_Type())
dcxFftTriggerCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxFftTriggerCount.setStatus(_A)
class _DcxFftEnable_Type(TruthValue):defaultValue=2
_DcxFftEnable_Type.__name__=_H
_DcxFftEnable_Object=MibTableColumn
dcxFftEnable=_DcxFftEnable_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,13),_DcxFftEnable_Type())
dcxFftEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxFftEnable.setStatus(_A)
_DcxFftApplyConfig_Type=TruthValue
_DcxFftApplyConfig_Object=MibTableColumn
dcxFftApplyConfig=_DcxFftApplyConfig_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,14),_DcxFftApplyConfig_Type())
dcxFftApplyConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxFftApplyConfig.setStatus(_A)
_DcxFftInProgress_Type=TruthValue
_DcxFftInProgress_Object=MibTableColumn
dcxFftInProgress=_DcxFftInProgress_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,15),_DcxFftInProgress_Type())
dcxFftInProgress.setMaxAccess(_G)
if mibBuilder.loadTexts:dcxFftInProgress.setStatus(_A)
_DcxFftCurrentTriggers_Type=Unsigned32
_DcxFftCurrentTriggers_Object=MibTableColumn
dcxFftCurrentTriggers=_DcxFftCurrentTriggers_Object((1,3,6,1,4,1,4115,1,4,5,1,1,1,1,16),_DcxFftCurrentTriggers_Type())
dcxFftCurrentTriggers.setMaxAccess(_G)
if mibBuilder.loadTexts:dcxFftCurrentTriggers.setStatus(_A)
_DcxFftPayloadTable_Object=MibTable
dcxFftPayloadTable=_DcxFftPayloadTable_Object((1,3,6,1,4,1,4115,1,4,5,1,1,2))
if mibBuilder.loadTexts:dcxFftPayloadTable.setStatus(_A)
_DcxFftPayloadEntry_Object=MibTableRow
dcxFftPayloadEntry=_DcxFftPayloadEntry_Object((1,3,6,1,4,1,4115,1,4,5,1,1,2,1))
dcxFftPayloadEntry.setIndexNames((0,_E,_F),(0,_I,_J))
if mibBuilder.loadTexts:dcxFftPayloadEntry.setStatus(_A)
_DcxFftPayloadIndex_Type=Unsigned32
_DcxFftPayloadIndex_Object=MibTableColumn
dcxFftPayloadIndex=_DcxFftPayloadIndex_Object((1,3,6,1,4,1,4115,1,4,5,1,1,2,1,1),_DcxFftPayloadIndex_Type())
dcxFftPayloadIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dcxFftPayloadIndex.setStatus(_A)
_DcxFftPayloadData_Type=DcxFftPayloadBuffer
_DcxFftPayloadData_Object=MibTableColumn
dcxFftPayloadData=_DcxFftPayloadData_Object((1,3,6,1,4,1,4115,1,4,5,1,1,2,1,2),_DcxFftPayloadData_Type())
dcxFftPayloadData.setMaxAccess(_G)
if mibBuilder.loadTexts:dcxFftPayloadData.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'DcxFftPayloadBuffer':DcxFftPayloadBuffer,'cmtsFftMIB':cmtsFftMIB,'dcxFftObjects':dcxFftObjects,'dcxFftUpstreamChannelTable':dcxFftUpstreamChannelTable,'dcxFftUpstreamChannelEntry':dcxFftUpstreamChannelEntry,'dcxFftSize':dcxFftSize,'dcxFftSampleRate':dcxFftSampleRate,'dcxFftCentreFrequency':dcxFftCentreFrequency,'dcxFftWindowing':dcxFftWindowing,'dcxFftLogAveragingTimeConstant':dcxFftLogAveragingTimeConstant,'dcxFftOutputFormat':dcxFftOutputFormat,'dcxFftOperatingMode':dcxFftOperatingMode,'dcxFftIdleInterval':dcxFftIdleInterval,'dcxFftBurstSid':dcxFftBurstSid,'dcxFftBurstIUC':dcxFftBurstIUC,'dcxFftLogicalChannel':dcxFftLogicalChannel,'dcxFftTriggerCount':dcxFftTriggerCount,'dcxFftEnable':dcxFftEnable,'dcxFftApplyConfig':dcxFftApplyConfig,'dcxFftInProgress':dcxFftInProgress,'dcxFftCurrentTriggers':dcxFftCurrentTriggers,'dcxFftPayloadTable':dcxFftPayloadTable,'dcxFftPayloadEntry':dcxFftPayloadEntry,_J:dcxFftPayloadIndex,'dcxFftPayloadData':dcxFftPayloadData})