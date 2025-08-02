_AM='cadUpchannelGroup'
_AL='cadUnicastFastPollTimeout'
_AK='cadUnicastFastPollInterval'
_AJ='cadUnicastSlowPollInterval'
_AI='cadUpchannelFreqRange'
_AH='cadIfUpChannelPCPreemptionAllowed'
_AG='cadIfUpChannelIngressCancellationSize'
_AF='cadIfUpChannelIngressCancellationInterval'
_AE='cadIfUpChannelType'
_AD='cadIfUpChannelScdmaHoppingSeed'
_AC='cadIfUpChannelScdmaFrameSize'
_AB='cadIfUpChannelScdmaCodesPerSlot'
_AA='cadIfUpChannelScdmaActiveCodes'
_A9='cadIfUpChannelPCTotalAllowedUsage'
_A8='cadIfUpChannelPCEmerResUsage'
_A7='cadIfUpChannelPCEmerAllowedUsage'
_A6='cadIfUpChannelPCNormResUsage'
_A5='cadIfUpChannelPCNormAllowedUsage'
_A4='cadIfUpChannelPreEqEnable'
_A3='cadIfUpChannelZeroTimingAdjust'
_A2='cadIfUpChannelZeroFreqAdjust'
_A1='cadIfUpChannelZeroPowerAdjust'
_A0='cadIfUpChannelThresholdPowerOffset'
_z='cadIfUpChannelMaxPowerAdjust'
_y='cadIfUpChannelMapSize'
_x='cadIfUpChannelTxBackoffEnd'
_w='cadIfUpChannelTxBackoffStart'
_v='cadIfUpChannelRangingBackoffEnd'
_u='cadIfUpChannelRangingBackoffStart'
_t='cadIfUpChannelSlotSize'
_s='cadIfUpChannelPowerDesired'
_r='cadIfUpChannelModulationProfile'
_q='cadIfUpChannelWidth'
_p='cadIfUpChannelFrequency'
_o='cadIfCmtsModChannelType'
_n='cadIfCmtsModScdmaSubframeCodes'
_m='cadIfCmtsModScdmaSpreaderEnable'
_l='cadIfCmtsModScdmaInterleaverStepSize'
_k='cadIfCmtsModTcmErrorCorrectionOn'
_j='cadIfCmtsModPreambleType'
_i='cadIfCmtsModByteInterleaverBlockSize'
_h='cadIfCmtsModByteInterleaverDepth'
_g='cadIfCmtsModBroadcomUwMismatchThreshold'
_f='cadIfCmtsModBroadcomUwDetectionWindow'
_e='cadIfCmtsModBroadcomUwPattern'
_d='cadIfCmtsModBroadcomUwLength'
_c='cadIfCmtsModPreambleValueOffset'
_b='cadIfCmtsModScrambler'
_a='cadIfCmtsModLastCodewordShortened'
_Z='cadIfCmtsModGuardTimeSize'
_Y='cadIfCmtsModMaxBurstSize'
_X='cadIfCmtsModScramblerSeed'
_W='cadIfCmtsModFECCodewordLength'
_V='cadIfCmtsModFECErrorCorrection'
_U='cadIfCmtsModDifferentialEncoding'
_T='cadIfCmtsModPreambleLen'
_S='cadIfCmtsModType'
_R='cadIfCmtsModControl'
_Q='cadUnicastPriority'
_P='cadIfUpChannelIfIndex'
_O='cadIfCmtsModIntervalUsageCode'
_N='cadIfCmtsModIndex'
_M='tens of milliseconds'
_L='DocsisUpstreamType'
_K='OctetString'
_J='percent'
_I='not-accessible'
_H='read-only'
_G='Unsigned32'
_F='TruthValue'
_E='read-create'
_D='Integer32'
_C='read-write'
_B='CADANT-CMTS-UPCHANNEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cadSpectrum,=mibBuilder.importSymbols('CADANT-PRODUCTS-MIB','cadSpectrum')
CardId,=mibBuilder.importSymbols('CADANT-TC','CardId')
DocsisUpstreamType,=mibBuilder.importSymbols('DOCS-IF-MIB',_L)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention',_F)
cadUpchannelMib=ModuleIdentity((1,3,6,1,4,1,4998,1,1,15,3))
if mibBuilder.loadTexts:cadUpchannelMib.setRevisions(('2014-04-25 00:00','2014-02-24 00:00','2014-02-07 00:00','2013-10-22 00:00','2013-09-26 00:00','2013-04-25 00:00','2013-01-15 00:00','2012-11-29 00:00','2012-09-18 00:00','2012-05-22 00:00','2008-06-26 00:00','2008-04-08 00:00','2008-03-31 00:00','2007-04-04 00:00','2007-02-05 00:00','2007-01-16 00:00','2006-09-11 00:00','2006-03-02 00:00','2005-11-29 00:00','2005-11-10 00:00','2005-10-04 00:00','2005-08-19 00:00','2005-02-24 00:00','2004-06-11 00:00','2004-03-04 00:00','2004-02-18 00:00','2004-02-15 00:00','2004-02-06 00:00','2003-09-26 00:00','2003-07-31 00:00','2003-06-23 00:00','2003-05-21 00:00','2003-03-05 00:00','2003-02-18 00:00','2002-12-03 00:00','2002-12-02 00:00'))
_CadIfCmtsModulationTable_Object=MibTable
cadIfCmtsModulationTable=_CadIfCmtsModulationTable_Object((1,3,6,1,4,1,4998,1,1,15,3,1))
if mibBuilder.loadTexts:cadIfCmtsModulationTable.setStatus(_A)
_CadIfCmtsModulationEntry_Object=MibTableRow
cadIfCmtsModulationEntry=_CadIfCmtsModulationEntry_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1))
cadIfCmtsModulationEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:cadIfCmtsModulationEntry.setStatus(_A)
class _CadIfCmtsModIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CadIfCmtsModIndex_Type.__name__=_D
_CadIfCmtsModIndex_Object=MibTableColumn
cadIfCmtsModIndex=_CadIfCmtsModIndex_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,1),_CadIfCmtsModIndex_Type())
cadIfCmtsModIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cadIfCmtsModIndex.setStatus(_A)
class _CadIfCmtsModIntervalUsageCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,9,10,11)));namedValues=NamedValues(*(('request',1),('requestData',2),('initialRanging',3),('periodicRanging',4),('shortData',5),('longData',6),('advPhyShortData',9),('advPhyLongData',10),('ugs',11)))
_CadIfCmtsModIntervalUsageCode_Type.__name__=_D
_CadIfCmtsModIntervalUsageCode_Object=MibTableColumn
cadIfCmtsModIntervalUsageCode=_CadIfCmtsModIntervalUsageCode_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,2),_CadIfCmtsModIntervalUsageCode_Type())
cadIfCmtsModIntervalUsageCode.setMaxAccess(_I)
if mibBuilder.loadTexts:cadIfCmtsModIntervalUsageCode.setStatus(_A)
_CadIfCmtsModControl_Type=RowStatus
_CadIfCmtsModControl_Object=MibTableColumn
cadIfCmtsModControl=_CadIfCmtsModControl_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,3),_CadIfCmtsModControl_Type())
cadIfCmtsModControl.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModControl.setStatus(_A)
class _CadIfCmtsModType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('qpsk',2),('qam16',3),('qam8',4),('qam32',5),('qam64',6),('qam128',7)))
_CadIfCmtsModType_Type.__name__=_D
_CadIfCmtsModType_Object=MibTableColumn
cadIfCmtsModType=_CadIfCmtsModType_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,4),_CadIfCmtsModType_Type())
cadIfCmtsModType.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModType.setStatus(_A)
class _CadIfCmtsModPreambleLen_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1536))
_CadIfCmtsModPreambleLen_Type.__name__=_D
_CadIfCmtsModPreambleLen_Object=MibTableColumn
cadIfCmtsModPreambleLen=_CadIfCmtsModPreambleLen_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,5),_CadIfCmtsModPreambleLen_Type())
cadIfCmtsModPreambleLen.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModPreambleLen.setStatus(_A)
class _CadIfCmtsModDifferentialEncoding_Type(TruthValue):defaultValue=2
_CadIfCmtsModDifferentialEncoding_Type.__name__=_F
_CadIfCmtsModDifferentialEncoding_Object=MibTableColumn
cadIfCmtsModDifferentialEncoding=_CadIfCmtsModDifferentialEncoding_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,6),_CadIfCmtsModDifferentialEncoding_Type())
cadIfCmtsModDifferentialEncoding.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModDifferentialEncoding.setStatus(_A)
class _CadIfCmtsModFECErrorCorrection_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CadIfCmtsModFECErrorCorrection_Type.__name__=_D
_CadIfCmtsModFECErrorCorrection_Object=MibTableColumn
cadIfCmtsModFECErrorCorrection=_CadIfCmtsModFECErrorCorrection_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,7),_CadIfCmtsModFECErrorCorrection_Type())
cadIfCmtsModFECErrorCorrection.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModFECErrorCorrection.setStatus(_A)
class _CadIfCmtsModFECCodewordLength_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,253))
_CadIfCmtsModFECCodewordLength_Type.__name__=_D
_CadIfCmtsModFECCodewordLength_Object=MibTableColumn
cadIfCmtsModFECCodewordLength=_CadIfCmtsModFECCodewordLength_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,8),_CadIfCmtsModFECCodewordLength_Type())
cadIfCmtsModFECCodewordLength.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModFECCodewordLength.setStatus(_A)
class _CadIfCmtsModScramblerSeed_Type(Integer32):defaultValue=338;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_CadIfCmtsModScramblerSeed_Type.__name__=_D
_CadIfCmtsModScramblerSeed_Object=MibTableColumn
cadIfCmtsModScramblerSeed=_CadIfCmtsModScramblerSeed_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,9),_CadIfCmtsModScramblerSeed_Type())
cadIfCmtsModScramblerSeed.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModScramblerSeed.setStatus(_A)
class _CadIfCmtsModMaxBurstSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CadIfCmtsModMaxBurstSize_Type.__name__=_D
_CadIfCmtsModMaxBurstSize_Object=MibTableColumn
cadIfCmtsModMaxBurstSize=_CadIfCmtsModMaxBurstSize_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,10),_CadIfCmtsModMaxBurstSize_Type())
cadIfCmtsModMaxBurstSize.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModMaxBurstSize.setStatus(_A)
class _CadIfCmtsModGuardTimeSize_Type(Unsigned32):defaultValue=8;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(8,96))
_CadIfCmtsModGuardTimeSize_Type.__name__=_G
_CadIfCmtsModGuardTimeSize_Object=MibTableColumn
cadIfCmtsModGuardTimeSize=_CadIfCmtsModGuardTimeSize_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,11),_CadIfCmtsModGuardTimeSize_Type())
cadIfCmtsModGuardTimeSize.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModGuardTimeSize.setStatus(_A)
class _CadIfCmtsModLastCodewordShortened_Type(TruthValue):defaultValue=1
_CadIfCmtsModLastCodewordShortened_Type.__name__=_F
_CadIfCmtsModLastCodewordShortened_Object=MibTableColumn
cadIfCmtsModLastCodewordShortened=_CadIfCmtsModLastCodewordShortened_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,12),_CadIfCmtsModLastCodewordShortened_Type())
cadIfCmtsModLastCodewordShortened.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModLastCodewordShortened.setStatus(_A)
class _CadIfCmtsModScrambler_Type(TruthValue):defaultValue=1
_CadIfCmtsModScrambler_Type.__name__=_F
_CadIfCmtsModScrambler_Object=MibTableColumn
cadIfCmtsModScrambler=_CadIfCmtsModScrambler_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,13),_CadIfCmtsModScrambler_Type())
cadIfCmtsModScrambler.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModScrambler.setStatus(_A)
class _CadIfCmtsModPreambleValueOffset_Type(Integer32):defaultValue=0
_CadIfCmtsModPreambleValueOffset_Type.__name__=_D
_CadIfCmtsModPreambleValueOffset_Object=MibTableColumn
cadIfCmtsModPreambleValueOffset=_CadIfCmtsModPreambleValueOffset_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,14),_CadIfCmtsModPreambleValueOffset_Type())
cadIfCmtsModPreambleValueOffset.setMaxAccess(_H)
if mibBuilder.loadTexts:cadIfCmtsModPreambleValueOffset.setStatus(_A)
class _CadIfCmtsModBroadcomUwLength_Type(Integer32):defaultValue=2
_CadIfCmtsModBroadcomUwLength_Type.__name__=_D
_CadIfCmtsModBroadcomUwLength_Object=MibTableColumn
cadIfCmtsModBroadcomUwLength=_CadIfCmtsModBroadcomUwLength_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,15),_CadIfCmtsModBroadcomUwLength_Type())
cadIfCmtsModBroadcomUwLength.setMaxAccess(_H)
if mibBuilder.loadTexts:cadIfCmtsModBroadcomUwLength.setStatus(_A)
class _CadIfCmtsModBroadcomUwPattern_Type(OctetString):defaultHexValue='0d0d00';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_CadIfCmtsModBroadcomUwPattern_Type.__name__=_K
_CadIfCmtsModBroadcomUwPattern_Object=MibTableColumn
cadIfCmtsModBroadcomUwPattern=_CadIfCmtsModBroadcomUwPattern_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,16),_CadIfCmtsModBroadcomUwPattern_Type())
cadIfCmtsModBroadcomUwPattern.setMaxAccess(_H)
if mibBuilder.loadTexts:cadIfCmtsModBroadcomUwPattern.setStatus(_A)
class _CadIfCmtsModBroadcomUwDetectionWindow_Type(OctetString):defaultHexValue='04';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CadIfCmtsModBroadcomUwDetectionWindow_Type.__name__=_K
_CadIfCmtsModBroadcomUwDetectionWindow_Object=MibTableColumn
cadIfCmtsModBroadcomUwDetectionWindow=_CadIfCmtsModBroadcomUwDetectionWindow_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,17),_CadIfCmtsModBroadcomUwDetectionWindow_Type())
cadIfCmtsModBroadcomUwDetectionWindow.setMaxAccess(_H)
if mibBuilder.loadTexts:cadIfCmtsModBroadcomUwDetectionWindow.setStatus(_A)
class _CadIfCmtsModBroadcomUwMismatchThreshold_Type(OctetString):defaultHexValue='01';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CadIfCmtsModBroadcomUwMismatchThreshold_Type.__name__=_K
_CadIfCmtsModBroadcomUwMismatchThreshold_Object=MibTableColumn
cadIfCmtsModBroadcomUwMismatchThreshold=_CadIfCmtsModBroadcomUwMismatchThreshold_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,18),_CadIfCmtsModBroadcomUwMismatchThreshold_Type())
cadIfCmtsModBroadcomUwMismatchThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:cadIfCmtsModBroadcomUwMismatchThreshold.setStatus(_A)
class _CadIfCmtsModByteInterleaverDepth_Type(Unsigned32):defaultValue=1
_CadIfCmtsModByteInterleaverDepth_Type.__name__=_G
_CadIfCmtsModByteInterleaverDepth_Object=MibTableColumn
cadIfCmtsModByteInterleaverDepth=_CadIfCmtsModByteInterleaverDepth_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,19),_CadIfCmtsModByteInterleaverDepth_Type())
cadIfCmtsModByteInterleaverDepth.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModByteInterleaverDepth.setStatus(_A)
class _CadIfCmtsModByteInterleaverBlockSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(36,2048))
_CadIfCmtsModByteInterleaverBlockSize_Type.__name__=_G
_CadIfCmtsModByteInterleaverBlockSize_Object=MibTableColumn
cadIfCmtsModByteInterleaverBlockSize=_CadIfCmtsModByteInterleaverBlockSize_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,20),_CadIfCmtsModByteInterleaverBlockSize_Type())
cadIfCmtsModByteInterleaverBlockSize.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModByteInterleaverBlockSize.setStatus(_A)
class _CadIfCmtsModPreambleType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('qpsk0',1),('qpsk1',2)))
_CadIfCmtsModPreambleType_Type.__name__=_D
_CadIfCmtsModPreambleType_Object=MibTableColumn
cadIfCmtsModPreambleType=_CadIfCmtsModPreambleType_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,21),_CadIfCmtsModPreambleType_Type())
cadIfCmtsModPreambleType.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModPreambleType.setStatus(_A)
class _CadIfCmtsModTcmErrorCorrectionOn_Type(TruthValue):defaultValue=2
_CadIfCmtsModTcmErrorCorrectionOn_Type.__name__=_F
_CadIfCmtsModTcmErrorCorrectionOn_Object=MibTableColumn
cadIfCmtsModTcmErrorCorrectionOn=_CadIfCmtsModTcmErrorCorrectionOn_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,22),_CadIfCmtsModTcmErrorCorrectionOn_Type())
cadIfCmtsModTcmErrorCorrectionOn.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModTcmErrorCorrectionOn.setStatus(_A)
class _CadIfCmtsModScdmaInterleaverStepSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,32))
_CadIfCmtsModScdmaInterleaverStepSize_Type.__name__=_G
_CadIfCmtsModScdmaInterleaverStepSize_Object=MibTableColumn
cadIfCmtsModScdmaInterleaverStepSize=_CadIfCmtsModScdmaInterleaverStepSize_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,23),_CadIfCmtsModScdmaInterleaverStepSize_Type())
cadIfCmtsModScdmaInterleaverStepSize.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModScdmaInterleaverStepSize.setStatus(_A)
class _CadIfCmtsModScdmaSpreaderEnable_Type(TruthValue):defaultValue=2
_CadIfCmtsModScdmaSpreaderEnable_Type.__name__=_F
_CadIfCmtsModScdmaSpreaderEnable_Object=MibTableColumn
cadIfCmtsModScdmaSpreaderEnable=_CadIfCmtsModScdmaSpreaderEnable_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,24),_CadIfCmtsModScdmaSpreaderEnable_Type())
cadIfCmtsModScdmaSpreaderEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModScdmaSpreaderEnable.setStatus(_A)
class _CadIfCmtsModScdmaSubframeCodes_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,128))
_CadIfCmtsModScdmaSubframeCodes_Type.__name__=_G
_CadIfCmtsModScdmaSubframeCodes_Object=MibTableColumn
cadIfCmtsModScdmaSubframeCodes=_CadIfCmtsModScdmaSubframeCodes_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,25),_CadIfCmtsModScdmaSubframeCodes_Type())
cadIfCmtsModScdmaSubframeCodes.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModScdmaSubframeCodes.setStatus(_A)
class _CadIfCmtsModChannelType_Type(DocsisUpstreamType):defaultValue=1
_CadIfCmtsModChannelType_Type.__name__=_L
_CadIfCmtsModChannelType_Object=MibTableColumn
cadIfCmtsModChannelType=_CadIfCmtsModChannelType_Object((1,3,6,1,4,1,4998,1,1,15,3,1,1,26),_CadIfCmtsModChannelType_Type())
cadIfCmtsModChannelType.setMaxAccess(_E)
if mibBuilder.loadTexts:cadIfCmtsModChannelType.setStatus(_A)
_CadIfUpstreamChannelTable_Object=MibTable
cadIfUpstreamChannelTable=_CadIfUpstreamChannelTable_Object((1,3,6,1,4,1,4998,1,1,15,3,2))
if mibBuilder.loadTexts:cadIfUpstreamChannelTable.setStatus(_A)
_CadIfUpstreamChannelEntry_Object=MibTableRow
cadIfUpstreamChannelEntry=_CadIfUpstreamChannelEntry_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1))
cadIfUpstreamChannelEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:cadIfUpstreamChannelEntry.setStatus(_A)
_CadIfUpChannelCardNumber_Type=CardId
_CadIfUpChannelCardNumber_Object=MibTableColumn
cadIfUpChannelCardNumber=_CadIfUpChannelCardNumber_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,1),_CadIfUpChannelCardNumber_Type())
cadIfUpChannelCardNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:cadIfUpChannelCardNumber.setStatus(_A)
class _CadIfUpChannelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CadIfUpChannelId_Type.__name__=_D
_CadIfUpChannelId_Object=MibTableColumn
cadIfUpChannelId=_CadIfUpChannelId_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,2),_CadIfUpChannelId_Type())
cadIfUpChannelId.setMaxAccess(_H)
if mibBuilder.loadTexts:cadIfUpChannelId.setStatus(_A)
class _CadIfUpChannelFrequency_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,85000000))
_CadIfUpChannelFrequency_Type.__name__=_D
_CadIfUpChannelFrequency_Object=MibTableColumn
cadIfUpChannelFrequency=_CadIfUpChannelFrequency_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,4),_CadIfUpChannelFrequency_Type())
cadIfUpChannelFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelFrequency.setStatus(_A)
if mibBuilder.loadTexts:cadIfUpChannelFrequency.setUnits('hertz')
class _CadIfUpChannelWidth_Type(Integer32):defaultValue=3200000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(200000,200000),ValueRangeConstraint(400000,400000),ValueRangeConstraint(800000,800000),ValueRangeConstraint(1600000,1600000),ValueRangeConstraint(3200000,3200000),ValueRangeConstraint(6400000,6400000))
_CadIfUpChannelWidth_Type.__name__=_D
_CadIfUpChannelWidth_Object=MibTableColumn
cadIfUpChannelWidth=_CadIfUpChannelWidth_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,5),_CadIfUpChannelWidth_Type())
cadIfUpChannelWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelWidth.setStatus(_A)
if mibBuilder.loadTexts:cadIfUpChannelWidth.setUnits('hertz')
class _CadIfUpChannelModulationProfile_Type(Integer32):defaultValue=0
_CadIfUpChannelModulationProfile_Type.__name__=_D
_CadIfUpChannelModulationProfile_Object=MibTableColumn
cadIfUpChannelModulationProfile=_CadIfUpChannelModulationProfile_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,6),_CadIfUpChannelModulationProfile_Type())
cadIfUpChannelModulationProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelModulationProfile.setStatus(_A)
class _CadIfUpChannelPowerDesired_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-16,29))
_CadIfUpChannelPowerDesired_Type.__name__=_D
_CadIfUpChannelPowerDesired_Object=MibTableColumn
cadIfUpChannelPowerDesired=_CadIfUpChannelPowerDesired_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,7),_CadIfUpChannelPowerDesired_Type())
cadIfUpChannelPowerDesired.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelPowerDesired.setStatus(_A)
if mibBuilder.loadTexts:cadIfUpChannelPowerDesired.setUnits('dBmV')
class _CadIfUpChannelSlotSize_Type(Unsigned32):defaultValue=4
_CadIfUpChannelSlotSize_Type.__name__=_G
_CadIfUpChannelSlotSize_Object=MibTableColumn
cadIfUpChannelSlotSize=_CadIfUpChannelSlotSize_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,8),_CadIfUpChannelSlotSize_Type())
cadIfUpChannelSlotSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelSlotSize.setStatus(_A)
class _CadIfUpChannelRangingBackoffStart_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CadIfUpChannelRangingBackoffStart_Type.__name__=_D
_CadIfUpChannelRangingBackoffStart_Object=MibTableColumn
cadIfUpChannelRangingBackoffStart=_CadIfUpChannelRangingBackoffStart_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,9),_CadIfUpChannelRangingBackoffStart_Type())
cadIfUpChannelRangingBackoffStart.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelRangingBackoffStart.setStatus(_A)
class _CadIfUpChannelRangingBackoffEnd_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CadIfUpChannelRangingBackoffEnd_Type.__name__=_D
_CadIfUpChannelRangingBackoffEnd_Object=MibTableColumn
cadIfUpChannelRangingBackoffEnd=_CadIfUpChannelRangingBackoffEnd_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,10),_CadIfUpChannelRangingBackoffEnd_Type())
cadIfUpChannelRangingBackoffEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelRangingBackoffEnd.setStatus(_A)
class _CadIfUpChannelTxBackoffStart_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CadIfUpChannelTxBackoffStart_Type.__name__=_D
_CadIfUpChannelTxBackoffStart_Object=MibTableColumn
cadIfUpChannelTxBackoffStart=_CadIfUpChannelTxBackoffStart_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,11),_CadIfUpChannelTxBackoffStart_Type())
cadIfUpChannelTxBackoffStart.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelTxBackoffStart.setStatus(_A)
class _CadIfUpChannelTxBackoffEnd_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CadIfUpChannelTxBackoffEnd_Type.__name__=_D
_CadIfUpChannelTxBackoffEnd_Object=MibTableColumn
cadIfUpChannelTxBackoffEnd=_CadIfUpChannelTxBackoffEnd_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,12),_CadIfUpChannelTxBackoffEnd_Type())
cadIfUpChannelTxBackoffEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelTxBackoffEnd.setStatus(_A)
class _CadIfUpChannelMapSize_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,13))
_CadIfUpChannelMapSize_Type.__name__=_D
_CadIfUpChannelMapSize_Object=MibTableColumn
cadIfUpChannelMapSize=_CadIfUpChannelMapSize_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,13),_CadIfUpChannelMapSize_Type())
cadIfUpChannelMapSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelMapSize.setStatus(_A)
if mibBuilder.loadTexts:cadIfUpChannelMapSize.setUnits('800microsecondTicks')
class _CadIfUpChannelMaxPowerAdjust_Type(Integer32):defaultValue=24;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_CadIfUpChannelMaxPowerAdjust_Type.__name__=_D
_CadIfUpChannelMaxPowerAdjust_Object=MibTableColumn
cadIfUpChannelMaxPowerAdjust=_CadIfUpChannelMaxPowerAdjust_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,17),_CadIfUpChannelMaxPowerAdjust_Type())
cadIfUpChannelMaxPowerAdjust.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelMaxPowerAdjust.setStatus(_A)
class _CadIfUpChannelThresholdPowerOffset_Type(Integer32):defaultValue=24;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,48))
_CadIfUpChannelThresholdPowerOffset_Type.__name__=_D
_CadIfUpChannelThresholdPowerOffset_Object=MibTableColumn
cadIfUpChannelThresholdPowerOffset=_CadIfUpChannelThresholdPowerOffset_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,18),_CadIfUpChannelThresholdPowerOffset_Type())
cadIfUpChannelThresholdPowerOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelThresholdPowerOffset.setStatus(_A)
class _CadIfUpChannelZeroPowerAdjust_Type(TruthValue):defaultValue=2
_CadIfUpChannelZeroPowerAdjust_Type.__name__=_F
_CadIfUpChannelZeroPowerAdjust_Object=MibTableColumn
cadIfUpChannelZeroPowerAdjust=_CadIfUpChannelZeroPowerAdjust_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,19),_CadIfUpChannelZeroPowerAdjust_Type())
cadIfUpChannelZeroPowerAdjust.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelZeroPowerAdjust.setStatus(_A)
class _CadIfUpChannelZeroFreqAdjust_Type(TruthValue):defaultValue=2
_CadIfUpChannelZeroFreqAdjust_Type.__name__=_F
_CadIfUpChannelZeroFreqAdjust_Object=MibTableColumn
cadIfUpChannelZeroFreqAdjust=_CadIfUpChannelZeroFreqAdjust_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,20),_CadIfUpChannelZeroFreqAdjust_Type())
cadIfUpChannelZeroFreqAdjust.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelZeroFreqAdjust.setStatus(_A)
class _CadIfUpChannelZeroTimingAdjust_Type(TruthValue):defaultValue=2
_CadIfUpChannelZeroTimingAdjust_Type.__name__=_F
_CadIfUpChannelZeroTimingAdjust_Object=MibTableColumn
cadIfUpChannelZeroTimingAdjust=_CadIfUpChannelZeroTimingAdjust_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,21),_CadIfUpChannelZeroTimingAdjust_Type())
cadIfUpChannelZeroTimingAdjust.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelZeroTimingAdjust.setStatus(_A)
class _CadIfUpChannelPreEqEnable_Type(TruthValue):defaultValue=2
_CadIfUpChannelPreEqEnable_Type.__name__=_F
_CadIfUpChannelPreEqEnable_Object=MibTableColumn
cadIfUpChannelPreEqEnable=_CadIfUpChannelPreEqEnable_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,22),_CadIfUpChannelPreEqEnable_Type())
cadIfUpChannelPreEqEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelPreEqEnable.setStatus(_A)
class _CadIfUpChannelPCNormAllowedUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIfUpChannelPCNormAllowedUsage_Type.__name__=_D
_CadIfUpChannelPCNormAllowedUsage_Object=MibTableColumn
cadIfUpChannelPCNormAllowedUsage=_CadIfUpChannelPCNormAllowedUsage_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,52),_CadIfUpChannelPCNormAllowedUsage_Type())
cadIfUpChannelPCNormAllowedUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelPCNormAllowedUsage.setStatus(_A)
if mibBuilder.loadTexts:cadIfUpChannelPCNormAllowedUsage.setUnits(_J)
class _CadIfUpChannelPCNormResUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIfUpChannelPCNormResUsage_Type.__name__=_D
_CadIfUpChannelPCNormResUsage_Object=MibTableColumn
cadIfUpChannelPCNormResUsage=_CadIfUpChannelPCNormResUsage_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,53),_CadIfUpChannelPCNormResUsage_Type())
cadIfUpChannelPCNormResUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelPCNormResUsage.setStatus(_A)
if mibBuilder.loadTexts:cadIfUpChannelPCNormResUsage.setUnits(_J)
class _CadIfUpChannelPCEmerAllowedUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIfUpChannelPCEmerAllowedUsage_Type.__name__=_D
_CadIfUpChannelPCEmerAllowedUsage_Object=MibTableColumn
cadIfUpChannelPCEmerAllowedUsage=_CadIfUpChannelPCEmerAllowedUsage_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,54),_CadIfUpChannelPCEmerAllowedUsage_Type())
cadIfUpChannelPCEmerAllowedUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelPCEmerAllowedUsage.setStatus(_A)
if mibBuilder.loadTexts:cadIfUpChannelPCEmerAllowedUsage.setUnits(_J)
class _CadIfUpChannelPCEmerResUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIfUpChannelPCEmerResUsage_Type.__name__=_D
_CadIfUpChannelPCEmerResUsage_Object=MibTableColumn
cadIfUpChannelPCEmerResUsage=_CadIfUpChannelPCEmerResUsage_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,55),_CadIfUpChannelPCEmerResUsage_Type())
cadIfUpChannelPCEmerResUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelPCEmerResUsage.setStatus(_A)
if mibBuilder.loadTexts:cadIfUpChannelPCEmerResUsage.setUnits(_J)
class _CadIfUpChannelPCTotalAllowedUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIfUpChannelPCTotalAllowedUsage_Type.__name__=_D
_CadIfUpChannelPCTotalAllowedUsage_Object=MibTableColumn
cadIfUpChannelPCTotalAllowedUsage=_CadIfUpChannelPCTotalAllowedUsage_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,56),_CadIfUpChannelPCTotalAllowedUsage_Type())
cadIfUpChannelPCTotalAllowedUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelPCTotalAllowedUsage.setStatus(_A)
if mibBuilder.loadTexts:cadIfUpChannelPCTotalAllowedUsage.setUnits(_J)
_CadIfUpChannelIfIndex_Type=InterfaceIndex
_CadIfUpChannelIfIndex_Object=MibTableColumn
cadIfUpChannelIfIndex=_CadIfUpChannelIfIndex_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,57),_CadIfUpChannelIfIndex_Type())
cadIfUpChannelIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cadIfUpChannelIfIndex.setStatus(_A)
class _CadIfUpChannelScdmaActiveCodes_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,128))
_CadIfUpChannelScdmaActiveCodes_Type.__name__=_G
_CadIfUpChannelScdmaActiveCodes_Object=MibTableColumn
cadIfUpChannelScdmaActiveCodes=_CadIfUpChannelScdmaActiveCodes_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,58),_CadIfUpChannelScdmaActiveCodes_Type())
cadIfUpChannelScdmaActiveCodes.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelScdmaActiveCodes.setStatus(_A)
class _CadIfUpChannelScdmaCodesPerSlot_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,32))
_CadIfUpChannelScdmaCodesPerSlot_Type.__name__=_D
_CadIfUpChannelScdmaCodesPerSlot_Object=MibTableColumn
cadIfUpChannelScdmaCodesPerSlot=_CadIfUpChannelScdmaCodesPerSlot_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,59),_CadIfUpChannelScdmaCodesPerSlot_Type())
cadIfUpChannelScdmaCodesPerSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelScdmaCodesPerSlot.setStatus(_A)
class _CadIfUpChannelScdmaFrameSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_CadIfUpChannelScdmaFrameSize_Type.__name__=_G
_CadIfUpChannelScdmaFrameSize_Object=MibTableColumn
cadIfUpChannelScdmaFrameSize=_CadIfUpChannelScdmaFrameSize_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,60),_CadIfUpChannelScdmaFrameSize_Type())
cadIfUpChannelScdmaFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelScdmaFrameSize.setStatus(_A)
class _CadIfUpChannelScdmaHoppingSeed_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_CadIfUpChannelScdmaHoppingSeed_Type.__name__=_G
_CadIfUpChannelScdmaHoppingSeed_Object=MibTableColumn
cadIfUpChannelScdmaHoppingSeed=_CadIfUpChannelScdmaHoppingSeed_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,61),_CadIfUpChannelScdmaHoppingSeed_Type())
cadIfUpChannelScdmaHoppingSeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelScdmaHoppingSeed.setStatus(_A)
class _CadIfUpChannelType_Type(DocsisUpstreamType):defaultValue=1
_CadIfUpChannelType_Type.__name__=_L
_CadIfUpChannelType_Object=MibTableColumn
cadIfUpChannelType=_CadIfUpChannelType_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,62),_CadIfUpChannelType_Type())
cadIfUpChannelType.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelType.setStatus(_A)
class _CadIfUpChannelCMKeepSpectralDensity_Type(TruthValue):defaultValue=2
_CadIfUpChannelCMKeepSpectralDensity_Type.__name__=_F
_CadIfUpChannelCMKeepSpectralDensity_Object=MibTableColumn
cadIfUpChannelCMKeepSpectralDensity=_CadIfUpChannelCMKeepSpectralDensity_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,63),_CadIfUpChannelCMKeepSpectralDensity_Type())
cadIfUpChannelCMKeepSpectralDensity.setMaxAccess(_I)
if mibBuilder.loadTexts:cadIfUpChannelCMKeepSpectralDensity.setStatus(_A)
class _CadIfUpChannelIngressCancellationInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CadIfUpChannelIngressCancellationInterval_Type.__name__=_G
_CadIfUpChannelIngressCancellationInterval_Object=MibTableColumn
cadIfUpChannelIngressCancellationInterval=_CadIfUpChannelIngressCancellationInterval_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,64),_CadIfUpChannelIngressCancellationInterval_Type())
cadIfUpChannelIngressCancellationInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelIngressCancellationInterval.setStatus(_A)
if mibBuilder.loadTexts:cadIfUpChannelIngressCancellationInterval.setUnits('milliseconds')
class _CadIfUpChannelIngressCancellationSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_CadIfUpChannelIngressCancellationSize_Type.__name__=_G
_CadIfUpChannelIngressCancellationSize_Object=MibTableColumn
cadIfUpChannelIngressCancellationSize=_CadIfUpChannelIngressCancellationSize_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,65),_CadIfUpChannelIngressCancellationSize_Type())
cadIfUpChannelIngressCancellationSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelIngressCancellationSize.setStatus(_A)
if mibBuilder.loadTexts:cadIfUpChannelIngressCancellationSize.setUnits('minislots')
_CadIfUpChannelPCPreemptionAllowed_Type=TruthValue
_CadIfUpChannelPCPreemptionAllowed_Object=MibTableColumn
cadIfUpChannelPCPreemptionAllowed=_CadIfUpChannelPCPreemptionAllowed_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,66),_CadIfUpChannelPCPreemptionAllowed_Type())
cadIfUpChannelPCPreemptionAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelPCPreemptionAllowed.setStatus(_A)
class _CadIfUpChannelSpGroupIndex_Type(Integer32):defaultValue=0
_CadIfUpChannelSpGroupIndex_Type.__name__=_D
_CadIfUpChannelSpGroupIndex_Object=MibTableColumn
cadIfUpChannelSpGroupIndex=_CadIfUpChannelSpGroupIndex_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,69),_CadIfUpChannelSpGroupIndex_Type())
cadIfUpChannelSpGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelSpGroupIndex.setStatus(_A)
class _CadIfUpChannelNumberEqTaps_Type(Unsigned32):defaultValue=24;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,5),ValueRangeConstraint(24,24))
_CadIfUpChannelNumberEqTaps_Type.__name__=_G
_CadIfUpChannelNumberEqTaps_Object=MibTableColumn
cadIfUpChannelNumberEqTaps=_CadIfUpChannelNumberEqTaps_Object((1,3,6,1,4,1,4998,1,1,15,3,2,1,70),_CadIfUpChannelNumberEqTaps_Type())
cadIfUpChannelNumberEqTaps.setMaxAccess(_C)
if mibBuilder.loadTexts:cadIfUpChannelNumberEqTaps.setStatus(_A)
_CadUpchannelParams_ObjectIdentity=ObjectIdentity
cadUpchannelParams=_CadUpchannelParams_ObjectIdentity((1,3,6,1,4,1,4998,1,1,15,3,5))
class _CadUpchannelFreqRange_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),('european',1),('japanese',2),('northAmerican',3),('extendedRange',4)))
_CadUpchannelFreqRange_Type.__name__=_D
_CadUpchannelFreqRange_Object=MibScalar
cadUpchannelFreqRange=_CadUpchannelFreqRange_Object((1,3,6,1,4,1,4998,1,1,15,3,5,6),_CadUpchannelFreqRange_Type())
cadUpchannelFreqRange.setMaxAccess(_C)
if mibBuilder.loadTexts:cadUpchannelFreqRange.setStatus(_A)
class _CadUpchannelRtpsPiggybackEnable_Type(TruthValue):defaultValue=2
_CadUpchannelRtpsPiggybackEnable_Type.__name__=_F
_CadUpchannelRtpsPiggybackEnable_Object=MibScalar
cadUpchannelRtpsPiggybackEnable=_CadUpchannelRtpsPiggybackEnable_Object((1,3,6,1,4,1,4998,1,1,15,3,5,7),_CadUpchannelRtpsPiggybackEnable_Type())
cadUpchannelRtpsPiggybackEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cadUpchannelRtpsPiggybackEnable.setStatus(_A)
class _CadUpchannelCaCertDropEnable_Type(TruthValue):defaultValue=2
_CadUpchannelCaCertDropEnable_Type.__name__=_F
_CadUpchannelCaCertDropEnable_Object=MibScalar
cadUpchannelCaCertDropEnable=_CadUpchannelCaCertDropEnable_Object((1,3,6,1,4,1,4998,1,1,15,3,5,8),_CadUpchannelCaCertDropEnable_Type())
cadUpchannelCaCertDropEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cadUpchannelCaCertDropEnable.setStatus(_A)
class _CadUpchannelRangingTimingOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-512,512))
_CadUpchannelRangingTimingOffset_Type.__name__=_D
_CadUpchannelRangingTimingOffset_Object=MibScalar
cadUpchannelRangingTimingOffset=_CadUpchannelRangingTimingOffset_Object((1,3,6,1,4,1,4998,1,1,15,3,5,9),_CadUpchannelRangingTimingOffset_Type())
cadUpchannelRangingTimingOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:cadUpchannelRangingTimingOffset.setStatus(_A)
class _CadUpchannelRecoverImpairedOnAck_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('attemptIndefiniteRecovery',1)))
_CadUpchannelRecoverImpairedOnAck_Type.__name__=_D
_CadUpchannelRecoverImpairedOnAck_Object=MibScalar
cadUpchannelRecoverImpairedOnAck=_CadUpchannelRecoverImpairedOnAck_Object((1,3,6,1,4,1,4998,1,1,15,3,5,10),_CadUpchannelRecoverImpairedOnAck_Type())
cadUpchannelRecoverImpairedOnAck.setMaxAccess(_C)
if mibBuilder.loadTexts:cadUpchannelRecoverImpairedOnAck.setStatus(_A)
class _CadUpchannelDsaRspSidTlvOverride_Type(TruthValue):defaultValue=2
_CadUpchannelDsaRspSidTlvOverride_Type.__name__=_F
_CadUpchannelDsaRspSidTlvOverride_Object=MibScalar
cadUpchannelDsaRspSidTlvOverride=_CadUpchannelDsaRspSidTlvOverride_Object((1,3,6,1,4,1,4998,1,1,15,3,5,11),_CadUpchannelDsaRspSidTlvOverride_Type())
cadUpchannelDsaRspSidTlvOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:cadUpchannelDsaRspSidTlvOverride.setStatus(_A)
_CadUnicastPollingTable_Object=MibTable
cadUnicastPollingTable=_CadUnicastPollingTable_Object((1,3,6,1,4,1,4998,1,1,15,3,6))
if mibBuilder.loadTexts:cadUnicastPollingTable.setStatus(_A)
_CadUnicastPollingEntry_Object=MibTableRow
cadUnicastPollingEntry=_CadUnicastPollingEntry_Object((1,3,6,1,4,1,4998,1,1,15,3,6,1))
cadUnicastPollingEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:cadUnicastPollingEntry.setStatus(_A)
class _CadUnicastPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CadUnicastPriority_Type.__name__=_D
_CadUnicastPriority_Object=MibTableColumn
cadUnicastPriority=_CadUnicastPriority_Object((1,3,6,1,4,1,4998,1,1,15,3,6,1,1),_CadUnicastPriority_Type())
cadUnicastPriority.setMaxAccess(_I)
if mibBuilder.loadTexts:cadUnicastPriority.setStatus(_A)
class _CadUnicastSlowPollInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,1000))
_CadUnicastSlowPollInterval_Type.__name__=_D
_CadUnicastSlowPollInterval_Object=MibTableColumn
cadUnicastSlowPollInterval=_CadUnicastSlowPollInterval_Object((1,3,6,1,4,1,4998,1,1,15,3,6,1,2),_CadUnicastSlowPollInterval_Type())
cadUnicastSlowPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cadUnicastSlowPollInterval.setStatus(_A)
if mibBuilder.loadTexts:cadUnicastSlowPollInterval.setUnits(_M)
class _CadUnicastFastPollInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,1000))
_CadUnicastFastPollInterval_Type.__name__=_D
_CadUnicastFastPollInterval_Object=MibTableColumn
cadUnicastFastPollInterval=_CadUnicastFastPollInterval_Object((1,3,6,1,4,1,4998,1,1,15,3,6,1,3),_CadUnicastFastPollInterval_Type())
cadUnicastFastPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cadUnicastFastPollInterval.setStatus(_A)
if mibBuilder.loadTexts:cadUnicastFastPollInterval.setUnits(_M)
class _CadUnicastFastPollTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,5000))
_CadUnicastFastPollTimeout_Type.__name__=_D
_CadUnicastFastPollTimeout_Object=MibTableColumn
cadUnicastFastPollTimeout=_CadUnicastFastPollTimeout_Object((1,3,6,1,4,1,4998,1,1,15,3,6,1,4),_CadUnicastFastPollTimeout_Type())
cadUnicastFastPollTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cadUnicastFastPollTimeout.setStatus(_A)
if mibBuilder.loadTexts:cadUnicastFastPollTimeout.setUnits(_M)
_CadUpchannelConformance_ObjectIdentity=ObjectIdentity
cadUpchannelConformance=_CadUpchannelConformance_ObjectIdentity((1,3,6,1,4,1,4998,1,1,15,3,7))
_CadUpchannelCompliances_ObjectIdentity=ObjectIdentity
cadUpchannelCompliances=_CadUpchannelCompliances_ObjectIdentity((1,3,6,1,4,1,4998,1,1,15,3,7,1))
_CadUpchannelGroups_ObjectIdentity=ObjectIdentity
cadUpchannelGroups=_CadUpchannelGroups_ObjectIdentity((1,3,6,1,4,1,4998,1,1,15,3,7,2))
cadUpchannelGroup=ObjectGroup((1,3,6,1,4,1,4998,1,1,15,3,7,2,1))
cadUpchannelGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:cadUpchannelGroup.setStatus(_A)
cadUpchannelCompliance=ModuleCompliance((1,3,6,1,4,1,4998,1,1,15,3,7,1,1))
cadUpchannelCompliance.setObjects((_B,_AM))
if mibBuilder.loadTexts:cadUpchannelCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cadUpchannelMib':cadUpchannelMib,'cadIfCmtsModulationTable':cadIfCmtsModulationTable,'cadIfCmtsModulationEntry':cadIfCmtsModulationEntry,_N:cadIfCmtsModIndex,_O:cadIfCmtsModIntervalUsageCode,_R:cadIfCmtsModControl,_S:cadIfCmtsModType,_T:cadIfCmtsModPreambleLen,_U:cadIfCmtsModDifferentialEncoding,_V:cadIfCmtsModFECErrorCorrection,_W:cadIfCmtsModFECCodewordLength,_X:cadIfCmtsModScramblerSeed,_Y:cadIfCmtsModMaxBurstSize,_Z:cadIfCmtsModGuardTimeSize,_a:cadIfCmtsModLastCodewordShortened,_b:cadIfCmtsModScrambler,_c:cadIfCmtsModPreambleValueOffset,_d:cadIfCmtsModBroadcomUwLength,_e:cadIfCmtsModBroadcomUwPattern,_f:cadIfCmtsModBroadcomUwDetectionWindow,_g:cadIfCmtsModBroadcomUwMismatchThreshold,_h:cadIfCmtsModByteInterleaverDepth,_i:cadIfCmtsModByteInterleaverBlockSize,_j:cadIfCmtsModPreambleType,_k:cadIfCmtsModTcmErrorCorrectionOn,_l:cadIfCmtsModScdmaInterleaverStepSize,_m:cadIfCmtsModScdmaSpreaderEnable,_n:cadIfCmtsModScdmaSubframeCodes,_o:cadIfCmtsModChannelType,'cadIfUpstreamChannelTable':cadIfUpstreamChannelTable,'cadIfUpstreamChannelEntry':cadIfUpstreamChannelEntry,'cadIfUpChannelCardNumber':cadIfUpChannelCardNumber,'cadIfUpChannelId':cadIfUpChannelId,_p:cadIfUpChannelFrequency,_q:cadIfUpChannelWidth,_r:cadIfUpChannelModulationProfile,_s:cadIfUpChannelPowerDesired,_t:cadIfUpChannelSlotSize,_u:cadIfUpChannelRangingBackoffStart,_v:cadIfUpChannelRangingBackoffEnd,_w:cadIfUpChannelTxBackoffStart,_x:cadIfUpChannelTxBackoffEnd,_y:cadIfUpChannelMapSize,_z:cadIfUpChannelMaxPowerAdjust,_A0:cadIfUpChannelThresholdPowerOffset,_A1:cadIfUpChannelZeroPowerAdjust,_A2:cadIfUpChannelZeroFreqAdjust,_A3:cadIfUpChannelZeroTimingAdjust,_A4:cadIfUpChannelPreEqEnable,_A5:cadIfUpChannelPCNormAllowedUsage,_A6:cadIfUpChannelPCNormResUsage,_A7:cadIfUpChannelPCEmerAllowedUsage,_A8:cadIfUpChannelPCEmerResUsage,_A9:cadIfUpChannelPCTotalAllowedUsage,_P:cadIfUpChannelIfIndex,_AA:cadIfUpChannelScdmaActiveCodes,_AB:cadIfUpChannelScdmaCodesPerSlot,_AC:cadIfUpChannelScdmaFrameSize,_AD:cadIfUpChannelScdmaHoppingSeed,_AE:cadIfUpChannelType,'cadIfUpChannelCMKeepSpectralDensity':cadIfUpChannelCMKeepSpectralDensity,_AF:cadIfUpChannelIngressCancellationInterval,_AG:cadIfUpChannelIngressCancellationSize,_AH:cadIfUpChannelPCPreemptionAllowed,'cadIfUpChannelSpGroupIndex':cadIfUpChannelSpGroupIndex,'cadIfUpChannelNumberEqTaps':cadIfUpChannelNumberEqTaps,'cadUpchannelParams':cadUpchannelParams,_AI:cadUpchannelFreqRange,'cadUpchannelRtpsPiggybackEnable':cadUpchannelRtpsPiggybackEnable,'cadUpchannelCaCertDropEnable':cadUpchannelCaCertDropEnable,'cadUpchannelRangingTimingOffset':cadUpchannelRangingTimingOffset,'cadUpchannelRecoverImpairedOnAck':cadUpchannelRecoverImpairedOnAck,'cadUpchannelDsaRspSidTlvOverride':cadUpchannelDsaRspSidTlvOverride,'cadUnicastPollingTable':cadUnicastPollingTable,'cadUnicastPollingEntry':cadUnicastPollingEntry,_Q:cadUnicastPriority,_AJ:cadUnicastSlowPollInterval,_AK:cadUnicastFastPollInterval,_AL:cadUnicastFastPollTimeout,'cadUpchannelConformance':cadUpchannelConformance,'cadUpchannelCompliances':cadUpchannelCompliances,'cadUpchannelCompliance':cadUpchannelCompliance,'cadUpchannelGroups':cadUpchannelGroups,_AM:cadUpchannelGroup})