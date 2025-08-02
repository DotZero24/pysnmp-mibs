_V='unknown'
_U='videoStatusInstance'
_T='dvs157'
_S='reserved'
_R='type4ATSC'
_Q='type4SA'
_P='eia708'
_O='saCustom'
_N='fourByThreeCCO'
_M='fourByThreePillarBox'
_L='palNAR'
_K='hd720p'
_J='hd1080i'
_I='not-accessible'
_H='videoCtrlInstance'
_G='CISCO-DMN-DSG-VIDEO-MIB'
_F='DisplayString'
_E='auto'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
ciscoDSGVideo=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,14))
if mibBuilder.loadTexts:ciscoDSGVideo.setRevisions(('2010-10-13 08:00','2010-08-30 11:00','2010-03-22 05:00','2010-02-12 12:00','2009-12-07 12:00'))
_VideoCtrlTable_Object=MibTable
videoCtrlTable=_VideoCtrlTable_Object((1,3,6,1,4,1,1429,2,2,5,14,1))
if mibBuilder.loadTexts:videoCtrlTable.setStatus(_A)
_VideoCtrlEntry_Object=MibTableRow
videoCtrlEntry=_VideoCtrlEntry_Object((1,3,6,1,4,1,1429,2,2,5,14,1,1))
videoCtrlEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:videoCtrlEntry.setStatus(_A)
class _VideoCtrlInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_VideoCtrlInstance_Type.__name__=_B
_VideoCtrlInstance_Object=MibTableColumn
videoCtrlInstance=_VideoCtrlInstance_Object((1,3,6,1,4,1,1429,2,2,5,14,1,1,1),_VideoCtrlInstance_Type())
videoCtrlInstance.setMaxAccess(_I)
if mibBuilder.loadTexts:videoCtrlInstance.setStatus(_A)
class _VideoPVFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_J,2),(_K,3),('sd',4)))
_VideoPVFormat_Type.__name__=_B
_VideoPVFormat_Object=MibTableColumn
videoPVFormat=_VideoPVFormat_Object((1,3,6,1,4,1,1429,2,2,5,14,1,1,2),_VideoPVFormat_Type())
videoPVFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:videoPVFormat.setStatus(_A)
class _VideoSDFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),('ntsc',2),('palBG',3),('palD',4),('palI',5),('palM',6),(_L,7),('ntscJ',8)))
_VideoSDFormat_Type.__name__=_B
_VideoSDFormat_Object=MibTableColumn
videoSDFormat=_VideoSDFormat_Object((1,3,6,1,4,1,1429,2,2,5,14,1,1,3),_VideoSDFormat_Type())
videoSDFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:videoSDFormat.setStatus(_A)
class _VideoTriSynch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_VideoTriSynch_Type.__name__=_B
_VideoTriSynch_Object=MibTableColumn
videoTriSynch=_VideoTriSynch_Object((1,3,6,1,4,1,1429,2,2,5,14,1,1,4),_VideoTriSynch_Type())
videoTriSynch.setMaxAccess(_D)
if mibBuilder.loadTexts:videoTriSynch.setStatus(_A)
class _VideoCutoff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_VideoCutoff_Type.__name__=_B
_VideoCutoff_Object=MibTableColumn
videoCutoff=_VideoCutoff_Object((1,3,6,1,4,1,1429,2,2,5,14,1,1,5),_VideoCutoff_Type())
videoCutoff.setMaxAccess(_D)
if mibBuilder.loadTexts:videoCutoff.setStatus(_A)
class _AspectRatioSD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fourThird',1),('sixteenNinth',2)))
_AspectRatioSD_Type.__name__=_B
_AspectRatioSD_Object=MibTableColumn
aspectRatioSD=_AspectRatioSD_Object((1,3,6,1,4,1,1429,2,2,5,14,1,1,6),_AspectRatioSD_Type())
aspectRatioSD.setMaxAccess(_D)
if mibBuilder.loadTexts:aspectRatioSD.setStatus(_A)
class _AspectRatioSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('none',1),(_E,2),('autoAFD',3),('sixteenByNineLetterBox',4),(_M,5),('fourteenByNine',6),(_N,7),('sixteenByNineSCALE',8)))
_AspectRatioSelection_Type.__name__=_B
_AspectRatioSelection_Object=MibTableColumn
aspectRatioSelection=_AspectRatioSelection_Object((1,3,6,1,4,1,1429,2,2,5,14,1,1,7),_AspectRatioSelection_Type())
aspectRatioSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:aspectRatioSelection.setStatus(_A)
class _ClosedCaptionPrefMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),(_O,2),(_P,3),('type3',4),(_Q,5),(_R,6),(_S,7),(_T,8)))
_ClosedCaptionPrefMode_Type.__name__=_B
_ClosedCaptionPrefMode_Object=MibTableColumn
closedCaptionPrefMode=_ClosedCaptionPrefMode_Object((1,3,6,1,4,1,1429,2,2,5,14,1,1,8),_ClosedCaptionPrefMode_Type())
closedCaptionPrefMode.setMaxAccess(_D)
if mibBuilder.loadTexts:closedCaptionPrefMode.setStatus(_A)
_VideoStatusTable_Object=MibTable
videoStatusTable=_VideoStatusTable_Object((1,3,6,1,4,1,1429,2,2,5,14,2))
if mibBuilder.loadTexts:videoStatusTable.setStatus(_A)
_VideoStatusEntry_Object=MibTableRow
videoStatusEntry=_VideoStatusEntry_Object((1,3,6,1,4,1,1429,2,2,5,14,2,1))
videoStatusEntry.setIndexNames((0,_G,_U))
if mibBuilder.loadTexts:videoStatusEntry.setStatus(_A)
class _VideoStatusInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_VideoStatusInstance_Type.__name__=_B
_VideoStatusInstance_Object=MibTableColumn
videoStatusInstance=_VideoStatusInstance_Object((1,3,6,1,4,1,1429,2,2,5,14,2,1,1),_VideoStatusInstance_Type())
videoStatusInstance.setMaxAccess(_I)
if mibBuilder.loadTexts:videoStatusInstance.setStatus(_A)
class _VideoStream_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('sd480i2997',1),('sd480i3000',2),('sd576i2500',3),('hd720p5000',4),('hd720p5994',5),('hd720p6000',6),('hd1080i2500',7),('hd1080i2997',8),('hd1080i3000',9),(_V,10),('unsupported',11)))
_VideoStream_Type.__name__=_B
_VideoStream_Object=MibTableColumn
videoStream=_VideoStream_Object((1,3,6,1,4,1,1429,2,2,5,14,2,1,2),_VideoStream_Type())
videoStream.setMaxAccess(_C)
if mibBuilder.loadTexts:videoStream.setStatus(_A)
class _VideoPVOutput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_VideoPVOutput_Type.__name__=_B
_VideoPVOutput_Object=MibTableColumn
videoPVOutput=_VideoPVOutput_Object((1,3,6,1,4,1,1429,2,2,5,14,2,1,3),_VideoPVOutput_Type())
videoPVOutput.setMaxAccess(_C)
if mibBuilder.loadTexts:videoPVOutput.setStatus(_A)
class _VideoSDOutput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ntsc',1),('palBG',2),('palD',3),('palI',4),('palM',5),(_L,6),('ntscJ',7)))
_VideoSDOutput_Type.__name__=_B
_VideoSDOutput_Object=MibTableColumn
videoSDOutput=_VideoSDOutput_Object((1,3,6,1,4,1,1429,2,2,5,14,2,1,4),_VideoSDOutput_Type())
videoSDOutput.setMaxAccess(_C)
if mibBuilder.loadTexts:videoSDOutput.setStatus(_A)
class _VideoBitRate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VideoBitRate_Type.__name__=_F
_VideoBitRate_Object=MibTableColumn
videoBitRate=_VideoBitRate_Object((1,3,6,1,4,1,1429,2,2,5,14,2,1,5),_VideoBitRate_Type())
videoBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:videoBitRate.setStatus(_A)
class _Video32PullDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('yes',1),('no',2),('recent',3)))
_Video32PullDown_Type.__name__=_B
_Video32PullDown_Object=MibTableColumn
video32PullDown=_Video32PullDown_Object((1,3,6,1,4,1,1429,2,2,5,14,2,1,6),_Video32PullDown_Type())
video32PullDown.setMaxAccess(_C)
if mibBuilder.loadTexts:video32PullDown.setStatus(_A)
class _VideoFPS_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VideoFPS_Type.__name__=_F
_VideoFPS_Object=MibTableColumn
videoFPS=_VideoFPS_Object((1,3,6,1,4,1,1429,2,2,5,14,2,1,7),_VideoFPS_Type())
videoFPS.setMaxAccess(_C)
if mibBuilder.loadTexts:videoFPS.setStatus(_A)
class _VideoSynchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('manual',2)))
_VideoSynchMode_Type.__name__=_B
_VideoSynchMode_Object=MibTableColumn
videoSynchMode=_VideoSynchMode_Object((1,3,6,1,4,1,1429,2,2,5,14,2,1,8),_VideoSynchMode_Type())
videoSynchMode.setMaxAccess(_C)
if mibBuilder.loadTexts:videoSynchMode.setStatus(_A)
class _VideoEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_V,1),('mpeg1',2),('mpeg2',3),('h264',4),('vc1',5),('mpeg4p2',6)))
_VideoEncoding_Type.__name__=_B
_VideoEncoding_Object=MibTableColumn
videoEncoding=_VideoEncoding_Object((1,3,6,1,4,1,1429,2,2,5,14,2,1,9),_VideoEncoding_Type())
videoEncoding.setMaxAccess(_C)
if mibBuilder.loadTexts:videoEncoding.setStatus(_A)
class _AspectRatioConversion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('none',1),('fourByThreeLetterBox',2),(_M,3),('fourteenByNineLetterBox',4),('fourteenByNinePillarBox',5),(_N,6),('sixteenByNineCCO',7),('sixteenByNineLBToFourteenByNineLB',8),('fourByThreePBToFourteenByNinePB',9)))
_AspectRatioConversion_Type.__name__=_B
_AspectRatioConversion_Object=MibTableColumn
aspectRatioConversion=_AspectRatioConversion_Object((1,3,6,1,4,1,1429,2,2,5,14,2,1,10),_AspectRatioConversion_Type())
aspectRatioConversion.setMaxAccess(_C)
if mibBuilder.loadTexts:aspectRatioConversion.setStatus(_A)
class _AspectRatioStreamAR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('fourByThree',1),('sixteenByNine',2),('twoTwentyOneByHundred',3),('square',4),('unavailable',5)))
_AspectRatioStreamAR_Type.__name__=_B
_AspectRatioStreamAR_Object=MibTableColumn
aspectRatioStreamAR=_AspectRatioStreamAR_Object((1,3,6,1,4,1,1429,2,2,5,14,2,1,11),_AspectRatioStreamAR_Type())
aspectRatioStreamAR.setMaxAccess(_C)
if mibBuilder.loadTexts:aspectRatioStreamAR.setStatus(_A)
class _AspectRatioWSSMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('passthrough',1),('suppress',2),('autoModify',3),('autoCreate',4)))
_AspectRatioWSSMode_Type.__name__=_B
_AspectRatioWSSMode_Object=MibTableColumn
aspectRatioWSSMode=_AspectRatioWSSMode_Object((1,3,6,1,4,1,1429,2,2,5,14,2,1,12),_AspectRatioWSSMode_Type())
aspectRatioWSSMode.setMaxAccess(_D)
if mibBuilder.loadTexts:aspectRatioWSSMode.setStatus(_A)
class _AspectRatioWSSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('fourByThreeFullFormat',1),('sixteenByNineLetterBoxCentre',2),('sixteenByNineLetterBoxTop',3),('greaterThanSixteenByNineLetterBoxCentre',4),('fourteenByNineLetterBoxCentre',5),('fourteenByNineLetterBoxTop',6),('fourteenByNineFullFormatCentre',7),('sixteenByNineFullFormat',8),('undefined',9)))
_AspectRatioWSSStatus_Type.__name__=_B
_AspectRatioWSSStatus_Object=MibTableColumn
aspectRatioWSSStatus=_AspectRatioWSSStatus_Object((1,3,6,1,4,1,1429,2,2,5,14,2,1,13),_AspectRatioWSSStatus_Type())
aspectRatioWSSStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aspectRatioWSSStatus.setStatus(_A)
class _ClosedCaptionActOP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),(_O,2),(_P,3),('type3',4),(_Q,5),(_R,6),(_S,7),(_T,8)))
_ClosedCaptionActOP_Type.__name__=_B
_ClosedCaptionActOP_Object=MibTableColumn
closedCaptionActOP=_ClosedCaptionActOP_Object((1,3,6,1,4,1,1429,2,2,5,14,2,1,14),_ClosedCaptionActOP_Type())
closedCaptionActOP.setMaxAccess(_C)
if mibBuilder.loadTexts:closedCaptionActOP.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'ciscoDSGVideo':ciscoDSGVideo,'videoCtrlTable':videoCtrlTable,'videoCtrlEntry':videoCtrlEntry,_H:videoCtrlInstance,'videoPVFormat':videoPVFormat,'videoSDFormat':videoSDFormat,'videoTriSynch':videoTriSynch,'videoCutoff':videoCutoff,'aspectRatioSD':aspectRatioSD,'aspectRatioSelection':aspectRatioSelection,'closedCaptionPrefMode':closedCaptionPrefMode,'videoStatusTable':videoStatusTable,'videoStatusEntry':videoStatusEntry,_U:videoStatusInstance,'videoStream':videoStream,'videoPVOutput':videoPVOutput,'videoSDOutput':videoSDOutput,'videoBitRate':videoBitRate,'video32PullDown':video32PullDown,'videoFPS':videoFPS,'videoSynchMode':videoSynchMode,'videoEncoding':videoEncoding,'aspectRatioConversion':aspectRatioConversion,'aspectRatioStreamAR':aspectRatioStreamAR,'aspectRatioWSSMode':aspectRatioWSSMode,'aspectRatioWSSStatus':aspectRatioWSSStatus,'closedCaptionActOP':closedCaptionActOP})