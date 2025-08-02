_Y='transcoderSubtIndex'
_X='transcoderStatusIndex'
_W='edgeEnhancement'
_V='mosquito'
_U='deBlock'
_T='sixteenByNineFullWidth'
_S='fourByThreeFullHeight'
_R='fourteenByNine'
_Q='fourByThreePillarBox'
_P='fourByThreeLetterBox'
_O='autoAFD'
_N='sixteenNinth'
_M='fourThird'
_L='iFrameSync'
_K='transcoderCfgIndex'
_J='DisplayString'
_I='ccSCTE20'
_H='ccCEA708'
_G='CISCO-DMN-DSG-TRANSCODE-MIB'
_F='auto'
_E='none'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
ciscoDSGTranscode=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,37))
if mibBuilder.loadTexts:ciscoDSGTranscode.setRevisions(('2013-07-10 12:20','2012-03-20 18:00','2010-10-13 08:00','2010-08-24 07:00'))
_TranscoderInfo_ObjectIdentity=ObjectIdentity
transcoderInfo=_TranscoderInfo_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,37,1))
class _TranscoderLOIAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('blackOutput',1),('noOutput',2)))
_TranscoderLOIAction_Type.__name__=_B
_TranscoderLOIAction_Object=MibScalar
transcoderLOIAction=_TranscoderLOIAction_Object((1,3,6,1,4,1,1429,2,2,5,37,1,1),_TranscoderLOIAction_Type())
transcoderLOIAction.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderLOIAction.setStatus(_A)
_TranscoderTable_ObjectIdentity=ObjectIdentity
transcoderTable=_TranscoderTable_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,37,2))
_TranscoderCfgTable_Object=MibTable
transcoderCfgTable=_TranscoderCfgTable_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1))
if mibBuilder.loadTexts:transcoderCfgTable.setStatus(_A)
_TranscoderCfgEntry_Object=MibTableRow
transcoderCfgEntry=_TranscoderCfgEntry_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1))
transcoderCfgEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:transcoderCfgEntry.setStatus(_A)
class _TranscoderCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TranscoderCfgIndex_Type.__name__=_B
_TranscoderCfgIndex_Object=MibTableColumn
transcoderCfgIndex=_TranscoderCfgIndex_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,1),_TranscoderCfgIndex_Type())
transcoderCfgIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:transcoderCfgIndex.setStatus(_A)
class _TranscoderCfgApplyInband_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_TranscoderCfgApplyInband_Type.__name__=_B
_TranscoderCfgApplyInband_Object=MibTableColumn
transcoderCfgApplyInband=_TranscoderCfgApplyInband_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,2),_TranscoderCfgApplyInband_Type())
transcoderCfgApplyInband.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgApplyInband.setStatus(_A)
class _TranscoderCfgVRes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5)));namedValues=NamedValues(*((_F,1),('hdOut',4),('sdOut',5)))
_TranscoderCfgVRes_Type.__name__=_B
_TranscoderCfgVRes_Object=MibTableColumn
transcoderCfgVRes=_TranscoderCfgVRes_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,3),_TranscoderCfgVRes_Type())
transcoderCfgVRes.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgVRes.setStatus(_A)
class _TranscoderCfgCCPkt1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_H,2),(_I,3)))
_TranscoderCfgCCPkt1_Type.__name__=_B
_TranscoderCfgCCPkt1_Object=MibTableColumn
transcoderCfgCCPkt1=_TranscoderCfgCCPkt1_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,4),_TranscoderCfgCCPkt1_Type())
transcoderCfgCCPkt1.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgCCPkt1.setStatus(_A)
class _TranscoderCfgCCPkt2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_H,2),(_I,3)))
_TranscoderCfgCCPkt2_Type.__name__=_B
_TranscoderCfgCCPkt2_Object=MibTableColumn
transcoderCfgCCPkt2=_TranscoderCfgCCPkt2_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,5),_TranscoderCfgCCPkt2_Type())
transcoderCfgCCPkt2.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgCCPkt2.setStatus(_A)
class _TranscoderCfgCCPkt3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_H,2),(_I,3)))
_TranscoderCfgCCPkt3_Type.__name__=_B
_TranscoderCfgCCPkt3_Object=MibTableColumn
transcoderCfgCCPkt3=_TranscoderCfgCCPkt3_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,6),_TranscoderCfgCCPkt3_Type())
transcoderCfgCCPkt3.setMaxAccess(_D)
if mibBuilder.loadTexts:transcoderCfgCCPkt3.setStatus(_A)
class _TranscoderCfgPCRRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_TranscoderCfgPCRRate_Type.__name__=_B
_TranscoderCfgPCRRate_Object=MibTableColumn
transcoderCfgPCRRate=_TranscoderCfgPCRRate_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,7),_TranscoderCfgPCRRate_Type())
transcoderCfgPCRRate.setMaxAccess(_D)
if mibBuilder.loadTexts:transcoderCfgPCRRate.setStatus(_A)
class _TranscoderCfgHDHRes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1440,1920)));namedValues=NamedValues(*(('threeQuarter',1440),('full',1920)))
_TranscoderCfgHDHRes_Type.__name__=_B
_TranscoderCfgHDHRes_Object=MibTableColumn
transcoderCfgHDHRes=_TranscoderCfgHDHRes_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,8),_TranscoderCfgHDHRes_Type())
transcoderCfgHDHRes.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgHDHRes.setStatus(_A)
class _TranscoderCfgHDBitrateMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cbr',1),('vbr',2)))
_TranscoderCfgHDBitrateMode_Type.__name__=_B
_TranscoderCfgHDBitrateMode_Object=MibTableColumn
transcoderCfgHDBitrateMode=_TranscoderCfgHDBitrateMode_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,9),_TranscoderCfgHDBitrateMode_Type())
transcoderCfgHDBitrateMode.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgHDBitrateMode.setStatus(_A)
class _TranscoderCfgHDBitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8000000,25000000))
_TranscoderCfgHDBitRate_Type.__name__=_B
_TranscoderCfgHDBitRate_Object=MibTableColumn
transcoderCfgHDBitRate=_TranscoderCfgHDBitRate_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,10),_TranscoderCfgHDBitRate_Type())
transcoderCfgHDBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgHDBitRate.setStatus(_A)
class _TranscoderCfgHDGOP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('userGop',2)))
_TranscoderCfgHDGOP_Type.__name__=_B
_TranscoderCfgHDGOP_Object=MibTableColumn
transcoderCfgHDGOP=_TranscoderCfgHDGOP_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,11),_TranscoderCfgHDGOP_Type())
transcoderCfgHDGOP.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgHDGOP.setStatus(_A)
class _TranscoderCfgHDManualGOP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,122,152,242,302)));namedValues=NamedValues(*(('manualGOP10',10),('manualGOP122',122),('manualGOP152',152),('manualGOP242',242),('manualGOP302',302)))
_TranscoderCfgHDManualGOP_Type.__name__=_B
_TranscoderCfgHDManualGOP_Object=MibTableColumn
transcoderCfgHDManualGOP=_TranscoderCfgHDManualGOP_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,12),_TranscoderCfgHDManualGOP_Type())
transcoderCfgHDManualGOP.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgHDManualGOP.setStatus(_A)
class _TranscoderCfgHD32PullDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_TranscoderCfgHD32PullDown_Type.__name__=_B
_TranscoderCfgHD32PullDown_Object=MibTableColumn
transcoderCfgHD32PullDown=_TranscoderCfgHD32PullDown_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,13),_TranscoderCfgHD32PullDown_Type())
transcoderCfgHD32PullDown.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgHD32PullDown.setStatus(_A)
class _TranscoderCfgHDAspectRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_TranscoderCfgHDAspectRatio_Type.__name__=_B
_TranscoderCfgHDAspectRatio_Object=MibTableColumn
transcoderCfgHDAspectRatio=_TranscoderCfgHDAspectRatio_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,14),_TranscoderCfgHDAspectRatio_Type())
transcoderCfgHDAspectRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:transcoderCfgHDAspectRatio.setStatus(_A)
class _TranscoderCfgHDARConversion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),(_F,2),(_O,3),(_P,4),(_Q,5),(_R,6),(_S,7),(_T,8)))
_TranscoderCfgHDARConversion_Type.__name__=_B
_TranscoderCfgHDARConversion_Object=MibTableColumn
transcoderCfgHDARConversion=_TranscoderCfgHDARConversion_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,15),_TranscoderCfgHDARConversion_Type())
transcoderCfgHDARConversion.setMaxAccess(_D)
if mibBuilder.loadTexts:transcoderCfgHDARConversion.setStatus(_A)
class _TranscoderCfgHDVideoPreproc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_U,2),(_V,3),(_W,4)))
_TranscoderCfgHDVideoPreproc_Type.__name__=_B
_TranscoderCfgHDVideoPreproc_Object=MibTableColumn
transcoderCfgHDVideoPreproc=_TranscoderCfgHDVideoPreproc_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,16),_TranscoderCfgHDVideoPreproc_Type())
transcoderCfgHDVideoPreproc.setMaxAccess(_D)
if mibBuilder.loadTexts:transcoderCfgHDVideoPreproc.setStatus(_A)
class _TranscoderCfgSDHRes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(352,480,528,544,704,720)));namedValues=NamedValues(*(('threeHundredAndFiftyTwo',352),('fourHundredAndEighty',480),('fiveHundredAndTwentyEight',528),('fiveHundredAndFourtyFour',544),('sevenHundredAndFour',704),('sevenHundredAndTwenty',720)))
_TranscoderCfgSDHRes_Type.__name__=_B
_TranscoderCfgSDHRes_Object=MibTableColumn
transcoderCfgSDHRes=_TranscoderCfgSDHRes_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,17),_TranscoderCfgSDHRes_Type())
transcoderCfgSDHRes.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgSDHRes.setStatus(_A)
class _TranscoderCfgSDBitRateMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cbr',1),('vbr',2)))
_TranscoderCfgSDBitRateMode_Type.__name__=_B
_TranscoderCfgSDBitRateMode_Object=MibTableColumn
transcoderCfgSDBitRateMode=_TranscoderCfgSDBitRateMode_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,18),_TranscoderCfgSDBitRateMode_Type())
transcoderCfgSDBitRateMode.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgSDBitRateMode.setStatus(_A)
class _TranscoderCfgSDBitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000000,15000000))
_TranscoderCfgSDBitRate_Type.__name__=_B
_TranscoderCfgSDBitRate_Object=MibTableColumn
transcoderCfgSDBitRate=_TranscoderCfgSDBitRate_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,19),_TranscoderCfgSDBitRate_Type())
transcoderCfgSDBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgSDBitRate.setStatus(_A)
class _TranscoderCfgSDGOP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('userGOPmn',2)))
_TranscoderCfgSDGOP_Type.__name__=_B
_TranscoderCfgSDGOP_Object=MibTableColumn
transcoderCfgSDGOP=_TranscoderCfgSDGOP_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,20),_TranscoderCfgSDGOP_Type())
transcoderCfgSDGOP.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgSDGOP.setStatus(_A)
class _TranscoderCfgSDManualGOP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,122,152,242,302)));namedValues=NamedValues(*(('manualgop10',10),('manualgop122',122),('manualgop152',152),('manualgop242',242),('manualgop302',302)))
_TranscoderCfgSDManualGOP_Type.__name__=_B
_TranscoderCfgSDManualGOP_Object=MibTableColumn
transcoderCfgSDManualGOP=_TranscoderCfgSDManualGOP_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,21),_TranscoderCfgSDManualGOP_Type())
transcoderCfgSDManualGOP.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgSDManualGOP.setStatus(_A)
class _TranscoderCfgSD32PullDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_TranscoderCfgSD32PullDown_Type.__name__=_B
_TranscoderCfgSD32PullDown_Object=MibTableColumn
transcoderCfgSD32PullDown=_TranscoderCfgSD32PullDown_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,22),_TranscoderCfgSD32PullDown_Type())
transcoderCfgSD32PullDown.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgSD32PullDown.setStatus(_A)
class _TranscoderCfgSDAspectRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_TranscoderCfgSDAspectRatio_Type.__name__=_B
_TranscoderCfgSDAspectRatio_Object=MibTableColumn
transcoderCfgSDAspectRatio=_TranscoderCfgSDAspectRatio_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,23),_TranscoderCfgSDAspectRatio_Type())
transcoderCfgSDAspectRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgSDAspectRatio.setStatus(_A)
class _TranscoderCfgSDARConversion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),(_F,2),(_O,3),(_P,4),(_Q,5),(_R,6),(_S,7),(_T,8)))
_TranscoderCfgSDARConversion_Type.__name__=_B
_TranscoderCfgSDARConversion_Object=MibTableColumn
transcoderCfgSDARConversion=_TranscoderCfgSDARConversion_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,24),_TranscoderCfgSDARConversion_Type())
transcoderCfgSDARConversion.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderCfgSDARConversion.setStatus(_A)
class _TranscoderCfgSDVideoPreproc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_U,2),(_V,3),(_W,4)))
_TranscoderCfgSDVideoPreproc_Type.__name__=_B
_TranscoderCfgSDVideoPreproc_Object=MibTableColumn
transcoderCfgSDVideoPreproc=_TranscoderCfgSDVideoPreproc_Object((1,3,6,1,4,1,1429,2,2,5,37,2,1,1,25),_TranscoderCfgSDVideoPreproc_Type())
transcoderCfgSDVideoPreproc.setMaxAccess(_D)
if mibBuilder.loadTexts:transcoderCfgSDVideoPreproc.setStatus(_A)
_TranscoderStatusTable_Object=MibTable
transcoderStatusTable=_TranscoderStatusTable_Object((1,3,6,1,4,1,1429,2,2,5,37,2,2))
if mibBuilder.loadTexts:transcoderStatusTable.setStatus(_A)
_TranscoderStatusEntry_Object=MibTableRow
transcoderStatusEntry=_TranscoderStatusEntry_Object((1,3,6,1,4,1,1429,2,2,5,37,2,2,1))
transcoderStatusEntry.setIndexNames((0,_G,_X))
if mibBuilder.loadTexts:transcoderStatusEntry.setStatus(_A)
class _TranscoderStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TranscoderStatusIndex_Type.__name__=_B
_TranscoderStatusIndex_Object=MibTableColumn
transcoderStatusIndex=_TranscoderStatusIndex_Object((1,3,6,1,4,1,1429,2,2,5,37,2,2,1,1),_TranscoderStatusIndex_Type())
transcoderStatusIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:transcoderStatusIndex.setStatus(_A)
class _TranscoderStatusVideoStream_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('unknown',1),('sd480i2997',2),('sd480i3000',3),('sd576i2500',4),('hd720p5000',5),('hd720p5994',6),('hd720p6000',7),('hd1080i2500',8),('hd1080i2997',9),('hd1080i3000',10),('unsupported',11)))
_TranscoderStatusVideoStream_Type.__name__=_B
_TranscoderStatusVideoStream_Object=MibTableColumn
transcoderStatusVideoStream=_TranscoderStatusVideoStream_Object((1,3,6,1,4,1,1429,2,2,5,37,2,2,1,2),_TranscoderStatusVideoStream_Type())
transcoderStatusVideoStream.setMaxAccess(_D)
if mibBuilder.loadTexts:transcoderStatusVideoStream.setStatus(_A)
_TranscoderSubtTable_Object=MibTable
transcoderSubtTable=_TranscoderSubtTable_Object((1,3,6,1,4,1,1429,2,2,5,37,2,3))
if mibBuilder.loadTexts:transcoderSubtTable.setStatus(_A)
_TranscoderSubtEntry_Object=MibTableRow
transcoderSubtEntry=_TranscoderSubtEntry_Object((1,3,6,1,4,1,1429,2,2,5,37,2,3,1))
transcoderSubtEntry.setIndexNames((0,_G,_Y))
if mibBuilder.loadTexts:transcoderSubtEntry.setStatus(_A)
class _TranscoderSubtIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TranscoderSubtIndex_Type.__name__=_B
_TranscoderSubtIndex_Object=MibTableColumn
transcoderSubtIndex=_TranscoderSubtIndex_Object((1,3,6,1,4,1,1429,2,2,5,37,2,3,1,1),_TranscoderSubtIndex_Type())
transcoderSubtIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:transcoderSubtIndex.setStatus(_A)
class _TranscoderSubtOpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('on',2),('imiText',3),('dvb',4)))
_TranscoderSubtOpMode_Type.__name__=_B
_TranscoderSubtOpMode_Object=MibTableColumn
transcoderSubtOpMode=_TranscoderSubtOpMode_Object((1,3,6,1,4,1,1429,2,2,5,37,2,3,1,2),_TranscoderSubtOpMode_Type())
transcoderSubtOpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderSubtOpMode.setStatus(_A)
class _TranscoderSubtLangMenu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('languageList',1),('languageEntry',2),('pmtOrder',3)))
_TranscoderSubtLangMenu_Type.__name__=_B
_TranscoderSubtLangMenu_Object=MibTableColumn
transcoderSubtLangMenu=_TranscoderSubtLangMenu_Object((1,3,6,1,4,1,1429,2,2,5,37,2,3,1,3),_TranscoderSubtLangMenu_Type())
transcoderSubtLangMenu.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderSubtLangMenu.setStatus(_A)
class _TranscoderSubtLangList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43)));namedValues=NamedValues(*(('ara',1),('btk',2),('ben',3),('bul',4),('chi',5),('cze',6),('dan',7),('dut',8),('eng',9),('fin',10),('fre',11),('ger',12),('gre',13),('heb',14),('hin',15),('hun',16),('ice',17),('ind',18),('ita',19),('jpn',20),('kor',21),('may',22),('mul',23),('nor',24),('per',25),('pol',26),('por',27),('rum',28),('rus',29),('san',30),('scc',31),('sin',32),('slo',33),('som',35),('spa',36),('swe',37),('tai',38),('tam',39),('tha',40),('tur',41),('ukr',42),('vie',43)))
_TranscoderSubtLangList_Type.__name__=_B
_TranscoderSubtLangList_Object=MibTableColumn
transcoderSubtLangList=_TranscoderSubtLangList_Object((1,3,6,1,4,1,1429,2,2,5,37,2,3,1,4),_TranscoderSubtLangList_Type())
transcoderSubtLangList.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderSubtLangList.setStatus(_A)
class _TranscoderSubtPMTOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('first',1),('second',2),('third',3),('fourth',4),('fifth',5),('sixth',6),('seventh',7),('eighth',8)))
_TranscoderSubtPMTOrder_Type.__name__=_B
_TranscoderSubtPMTOrder_Object=MibTableColumn
transcoderSubtPMTOrder=_TranscoderSubtPMTOrder_Object((1,3,6,1,4,1,1429,2,2,5,37,2,3,1,5),_TranscoderSubtPMTOrder_Type())
transcoderSubtPMTOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderSubtPMTOrder.setStatus(_A)
class _TranscoderSubtManualEntry_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_TranscoderSubtManualEntry_Type.__name__=_J
_TranscoderSubtManualEntry_Object=MibTableColumn
transcoderSubtManualEntry=_TranscoderSubtManualEntry_Object((1,3,6,1,4,1,1429,2,2,5,37,2,3,1,6),_TranscoderSubtManualEntry_Type())
transcoderSubtManualEntry.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderSubtManualEntry.setStatus(_A)
class _TranscoderSubtImitextPos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('standard',1),('extended',2)))
_TranscoderSubtImitextPos_Type.__name__=_B
_TranscoderSubtImitextPos_Object=MibTableColumn
transcoderSubtImitextPos=_TranscoderSubtImitextPos_Object((1,3,6,1,4,1,1429,2,2,5,37,2,3,1,7),_TranscoderSubtImitextPos_Type())
transcoderSubtImitextPos.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderSubtImitextPos.setStatus(_A)
class _TranscoderSubtForeGround_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('yellow',2),('white',3)))
_TranscoderSubtForeGround_Type.__name__=_B
_TranscoderSubtForeGround_Object=MibTableColumn
transcoderSubtForeGround=_TranscoderSubtForeGround_Object((1,3,6,1,4,1,1429,2,2,5,37,2,3,1,8),_TranscoderSubtForeGround_Type())
transcoderSubtForeGround.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderSubtForeGround.setStatus(_A)
class _TranscoderSubtBackGround_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),('shadow',3),('opaque',4),('semi',5)))
_TranscoderSubtBackGround_Type.__name__=_B
_TranscoderSubtBackGround_Object=MibTableColumn
transcoderSubtBackGround=_TranscoderSubtBackGround_Object((1,3,6,1,4,1,1429,2,2,5,37,2,3,1,9),_TranscoderSubtBackGround_Type())
transcoderSubtBackGround.setMaxAccess(_C)
if mibBuilder.loadTexts:transcoderSubtBackGround.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'ciscoDSGTranscode':ciscoDSGTranscode,'transcoderInfo':transcoderInfo,'transcoderLOIAction':transcoderLOIAction,'transcoderTable':transcoderTable,'transcoderCfgTable':transcoderCfgTable,'transcoderCfgEntry':transcoderCfgEntry,_K:transcoderCfgIndex,'transcoderCfgApplyInband':transcoderCfgApplyInband,'transcoderCfgVRes':transcoderCfgVRes,'transcoderCfgCCPkt1':transcoderCfgCCPkt1,'transcoderCfgCCPkt2':transcoderCfgCCPkt2,'transcoderCfgCCPkt3':transcoderCfgCCPkt3,'transcoderCfgPCRRate':transcoderCfgPCRRate,'transcoderCfgHDHRes':transcoderCfgHDHRes,'transcoderCfgHDBitrateMode':transcoderCfgHDBitrateMode,'transcoderCfgHDBitRate':transcoderCfgHDBitRate,'transcoderCfgHDGOP':transcoderCfgHDGOP,'transcoderCfgHDManualGOP':transcoderCfgHDManualGOP,'transcoderCfgHD32PullDown':transcoderCfgHD32PullDown,'transcoderCfgHDAspectRatio':transcoderCfgHDAspectRatio,'transcoderCfgHDARConversion':transcoderCfgHDARConversion,'transcoderCfgHDVideoPreproc':transcoderCfgHDVideoPreproc,'transcoderCfgSDHRes':transcoderCfgSDHRes,'transcoderCfgSDBitRateMode':transcoderCfgSDBitRateMode,'transcoderCfgSDBitRate':transcoderCfgSDBitRate,'transcoderCfgSDGOP':transcoderCfgSDGOP,'transcoderCfgSDManualGOP':transcoderCfgSDManualGOP,'transcoderCfgSD32PullDown':transcoderCfgSD32PullDown,'transcoderCfgSDAspectRatio':transcoderCfgSDAspectRatio,'transcoderCfgSDARConversion':transcoderCfgSDARConversion,'transcoderCfgSDVideoPreproc':transcoderCfgSDVideoPreproc,'transcoderStatusTable':transcoderStatusTable,'transcoderStatusEntry':transcoderStatusEntry,_X:transcoderStatusIndex,'transcoderStatusVideoStream':transcoderStatusVideoStream,'transcoderSubtTable':transcoderSubtTable,'transcoderSubtEntry':transcoderSubtEntry,_Y:transcoderSubtIndex,'transcoderSubtOpMode':transcoderSubtOpMode,'transcoderSubtLangMenu':transcoderSubtLangMenu,'transcoderSubtLangList':transcoderSubtLangList,'transcoderSubtPMTOrder':transcoderSubtPMTOrder,'transcoderSubtManualEntry':transcoderSubtManualEntry,'transcoderSubtImitextPos':transcoderSubtImitextPos,'transcoderSubtForeGround':transcoderSubtForeGround,'transcoderSubtBackGround':transcoderSubtBackGround})