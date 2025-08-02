_G='read-create'
_F='read-write'
_E='ifIndex'
_D='IF-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cE1=ModuleIdentity((1,3,6,1,4,1,2011,10,2,28))
if mibBuilder.loadTexts:h3cE1.setRevisions(('2012-07-16 17:41','2010-04-08 18:55','2009-06-08 17:41','2004-12-01 14:36'))
class H3cE1TimeSlot(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_E1InterfaceStatusTable_Object=MibTable
e1InterfaceStatusTable=_E1InterfaceStatusTable_Object((1,3,6,1,4,1,2011,10,2,28,1))
if mibBuilder.loadTexts:e1InterfaceStatusTable.setStatus(_A)
_E1InterfaceStatusEntry_Object=MibTableRow
e1InterfaceStatusEntry=_E1InterfaceStatusEntry_Object((1,3,6,1,4,1,2011,10,2,28,1,1))
e1InterfaceStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:e1InterfaceStatusEntry.setStatus(_A)
_E1InterfaceInErrs_Type=Counter32
_E1InterfaceInErrs_Object=MibTableColumn
e1InterfaceInErrs=_E1InterfaceInErrs_Object((1,3,6,1,4,1,2011,10,2,28,1,1,1),_E1InterfaceInErrs_Type())
e1InterfaceInErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:e1InterfaceInErrs.setStatus(_A)
_E1InterfaceInRuntsErrs_Type=Counter32
_E1InterfaceInRuntsErrs_Object=MibTableColumn
e1InterfaceInRuntsErrs=_E1InterfaceInRuntsErrs_Object((1,3,6,1,4,1,2011,10,2,28,1,1,2),_E1InterfaceInRuntsErrs_Type())
e1InterfaceInRuntsErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:e1InterfaceInRuntsErrs.setStatus(_A)
_E1InterfaceInGiantsErrs_Type=Counter32
_E1InterfaceInGiantsErrs_Object=MibTableColumn
e1InterfaceInGiantsErrs=_E1InterfaceInGiantsErrs_Object((1,3,6,1,4,1,2011,10,2,28,1,1,3),_E1InterfaceInGiantsErrs_Type())
e1InterfaceInGiantsErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:e1InterfaceInGiantsErrs.setStatus(_A)
_E1InterfaceInCrcErrs_Type=Counter32
_E1InterfaceInCrcErrs_Object=MibTableColumn
e1InterfaceInCrcErrs=_E1InterfaceInCrcErrs_Object((1,3,6,1,4,1,2011,10,2,28,1,1,4),_E1InterfaceInCrcErrs_Type())
e1InterfaceInCrcErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:e1InterfaceInCrcErrs.setStatus(_A)
_E1InterfaceInAlignErrs_Type=Counter32
_E1InterfaceInAlignErrs_Object=MibTableColumn
e1InterfaceInAlignErrs=_E1InterfaceInAlignErrs_Object((1,3,6,1,4,1,2011,10,2,28,1,1,5),_E1InterfaceInAlignErrs_Type())
e1InterfaceInAlignErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:e1InterfaceInAlignErrs.setStatus(_A)
_E1InterfaceInOverRunsErrs_Type=Counter32
_E1InterfaceInOverRunsErrs_Object=MibTableColumn
e1InterfaceInOverRunsErrs=_E1InterfaceInOverRunsErrs_Object((1,3,6,1,4,1,2011,10,2,28,1,1,6),_E1InterfaceInOverRunsErrs_Type())
e1InterfaceInOverRunsErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:e1InterfaceInOverRunsErrs.setStatus(_A)
_E1InterfaceInDribblesErrs_Type=Counter32
_E1InterfaceInDribblesErrs_Object=MibTableColumn
e1InterfaceInDribblesErrs=_E1InterfaceInDribblesErrs_Object((1,3,6,1,4,1,2011,10,2,28,1,1,7),_E1InterfaceInDribblesErrs_Type())
e1InterfaceInDribblesErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:e1InterfaceInDribblesErrs.setStatus(_A)
_E1InterfaceInAbortedSeqErrs_Type=Counter32
_E1InterfaceInAbortedSeqErrs_Object=MibTableColumn
e1InterfaceInAbortedSeqErrs=_E1InterfaceInAbortedSeqErrs_Object((1,3,6,1,4,1,2011,10,2,28,1,1,8),_E1InterfaceInAbortedSeqErrs_Type())
e1InterfaceInAbortedSeqErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:e1InterfaceInAbortedSeqErrs.setStatus(_A)
_E1InterfaceInNoBufferErrs_Type=Counter32
_E1InterfaceInNoBufferErrs_Object=MibTableColumn
e1InterfaceInNoBufferErrs=_E1InterfaceInNoBufferErrs_Object((1,3,6,1,4,1,2011,10,2,28,1,1,9),_E1InterfaceInNoBufferErrs_Type())
e1InterfaceInNoBufferErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:e1InterfaceInNoBufferErrs.setStatus(_A)
_E1InterfaceInFramingErrs_Type=Counter32
_E1InterfaceInFramingErrs_Object=MibTableColumn
e1InterfaceInFramingErrs=_E1InterfaceInFramingErrs_Object((1,3,6,1,4,1,2011,10,2,28,1,1,10),_E1InterfaceInFramingErrs_Type())
e1InterfaceInFramingErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:e1InterfaceInFramingErrs.setStatus(_A)
_E1InterfaceOutputErrs_Type=Counter32
_E1InterfaceOutputErrs_Object=MibTableColumn
e1InterfaceOutputErrs=_E1InterfaceOutputErrs_Object((1,3,6,1,4,1,2011,10,2,28,1,1,11),_E1InterfaceOutputErrs_Type())
e1InterfaceOutputErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:e1InterfaceOutputErrs.setStatus(_A)
_E1InterfaceOutUnderRunErrs_Type=Counter32
_E1InterfaceOutUnderRunErrs_Object=MibTableColumn
e1InterfaceOutUnderRunErrs=_E1InterfaceOutUnderRunErrs_Object((1,3,6,1,4,1,2011,10,2,28,1,1,12),_E1InterfaceOutUnderRunErrs_Type())
e1InterfaceOutUnderRunErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:e1InterfaceOutUnderRunErrs.setStatus(_A)
_E1InterfaceOutCollisonsErrs_Type=Counter32
_E1InterfaceOutCollisonsErrs_Object=MibTableColumn
e1InterfaceOutCollisonsErrs=_E1InterfaceOutCollisonsErrs_Object((1,3,6,1,4,1,2011,10,2,28,1,1,13),_E1InterfaceOutCollisonsErrs_Type())
e1InterfaceOutCollisonsErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:e1InterfaceOutCollisonsErrs.setStatus(_A)
_E1InterfaceOutDeferedErrs_Type=Counter32
_E1InterfaceOutDeferedErrs_Object=MibTableColumn
e1InterfaceOutDeferedErrs=_E1InterfaceOutDeferedErrs_Object((1,3,6,1,4,1,2011,10,2,28,1,1,14),_E1InterfaceOutDeferedErrs_Type())
e1InterfaceOutDeferedErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:e1InterfaceOutDeferedErrs.setStatus(_A)
_H3ce1Table_Object=MibTable
h3ce1Table=_H3ce1Table_Object((1,3,6,1,4,1,2011,10,2,28,2))
if mibBuilder.loadTexts:h3ce1Table.setStatus(_A)
_H3ce1Entry_Object=MibTableRow
h3ce1Entry=_H3ce1Entry_Object((1,3,6,1,4,1,2011,10,2,28,2,1))
h3ce1Entry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3ce1Entry.setStatus(_A)
class _H3ce1Type_Type(Bits):namedValues=NamedValues(*(('voice',0),('pos',1)))
_H3ce1Type_Type.__name__='Bits'
_H3ce1Type_Object=MibTableColumn
h3ce1Type=_H3ce1Type_Object((1,3,6,1,4,1,2011,10,2,28,2,1,1),_H3ce1Type_Type())
h3ce1Type.setMaxAccess(_B)
if mibBuilder.loadTexts:h3ce1Type.setStatus(_A)
class _H3ce1Clock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('slave',1),('master',2),('internal',3),('line',4),('linePri',5)))
_H3ce1Clock_Type.__name__=_C
_H3ce1Clock_Object=MibTableColumn
h3ce1Clock=_H3ce1Clock_Object((1,3,6,1,4,1,2011,10,2,28,2,1,2),_H3ce1Clock_Type())
h3ce1Clock.setMaxAccess(_F)
if mibBuilder.loadTexts:h3ce1Clock.setStatus(_A)
class _H3ce1FrameFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('crc4',1),('nocrc4',2)))
_H3ce1FrameFormat_Type.__name__=_C
_H3ce1FrameFormat_Object=MibTableColumn
h3ce1FrameFormat=_H3ce1FrameFormat_Object((1,3,6,1,4,1,2011,10,2,28,2,1,3),_H3ce1FrameFormat_Type())
h3ce1FrameFormat.setMaxAccess(_F)
if mibBuilder.loadTexts:h3ce1FrameFormat.setStatus(_A)
class _H3ce1LineCode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*(('ami',1),('hdb3',3)))
_H3ce1LineCode_Type.__name__=_C
_H3ce1LineCode_Object=MibTableColumn
h3ce1LineCode=_H3ce1LineCode_Object((1,3,6,1,4,1,2011,10,2,28,2,1,4),_H3ce1LineCode_Type())
h3ce1LineCode.setMaxAccess(_F)
if mibBuilder.loadTexts:h3ce1LineCode.setStatus(_A)
_H3ce1PriSetTimeSlot_Type=H3cE1TimeSlot
_H3ce1PriSetTimeSlot_Object=MibTableColumn
h3ce1PriSetTimeSlot=_H3ce1PriSetTimeSlot_Object((1,3,6,1,4,1,2011,10,2,28,2,1,5),_H3ce1PriSetTimeSlot_Type())
h3ce1PriSetTimeSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:h3ce1PriSetTimeSlot.setStatus(_A)
_H3ce1DChannelIndex_Type=Integer32
_H3ce1DChannelIndex_Object=MibTableColumn
h3ce1DChannelIndex=_H3ce1DChannelIndex_Object((1,3,6,1,4,1,2011,10,2,28,2,1,6),_H3ce1DChannelIndex_Type())
h3ce1DChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3ce1DChannelIndex.setStatus(_A)
_H3ce1SubScribLineChannelIndex_Type=Integer32
_H3ce1SubScribLineChannelIndex_Object=MibTableColumn
h3ce1SubScribLineChannelIndex=_H3ce1SubScribLineChannelIndex_Object((1,3,6,1,4,1,2011,10,2,28,2,1,7),_H3ce1SubScribLineChannelIndex_Type())
h3ce1SubScribLineChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3ce1SubScribLineChannelIndex.setStatus(_A)
_H3ce1FcmChannelIndex_Type=Integer32
_H3ce1FcmChannelIndex_Object=MibTableColumn
h3ce1FcmChannelIndex=_H3ce1FcmChannelIndex_Object((1,3,6,1,4,1,2011,10,2,28,2,1,8),_H3ce1FcmChannelIndex_Type())
h3ce1FcmChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3ce1FcmChannelIndex.setStatus(_A)
_H3ce1InterfaceTable_Object=MibTable
h3ce1InterfaceTable=_H3ce1InterfaceTable_Object((1,3,6,1,4,1,2011,10,2,28,3))
if mibBuilder.loadTexts:h3ce1InterfaceTable.setStatus(_A)
_H3ce1InterfaceEntry_Object=MibTableRow
h3ce1InterfaceEntry=_H3ce1InterfaceEntry_Object((1,3,6,1,4,1,2011,10,2,28,3,1))
h3ce1InterfaceEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3ce1InterfaceEntry.setStatus(_A)
_H3ce1ControllerIndex_Type=Integer32
_H3ce1ControllerIndex_Object=MibTableColumn
h3ce1ControllerIndex=_H3ce1ControllerIndex_Object((1,3,6,1,4,1,2011,10,2,28,3,1,1),_H3ce1ControllerIndex_Type())
h3ce1ControllerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3ce1ControllerIndex.setStatus(_A)
_H3ce1TimeSlotSetTable_Object=MibTable
h3ce1TimeSlotSetTable=_H3ce1TimeSlotSetTable_Object((1,3,6,1,4,1,2011,10,2,28,4))
if mibBuilder.loadTexts:h3ce1TimeSlotSetTable.setStatus(_A)
_H3ce1TimeSlotSetEntry_Object=MibTableRow
h3ce1TimeSlotSetEntry=_H3ce1TimeSlotSetEntry_Object((1,3,6,1,4,1,2011,10,2,28,4,1))
h3ce1TimeSlotSetEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3ce1TimeSlotSetEntry.setStatus(_A)
class _H3ce1TimeSlotSetGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_H3ce1TimeSlotSetGroupId_Type.__name__=_C
_H3ce1TimeSlotSetGroupId_Object=MibTableColumn
h3ce1TimeSlotSetGroupId=_H3ce1TimeSlotSetGroupId_Object((1,3,6,1,4,1,2011,10,2,28,4,1,1),_H3ce1TimeSlotSetGroupId_Type())
h3ce1TimeSlotSetGroupId.setMaxAccess(_G)
if mibBuilder.loadTexts:h3ce1TimeSlotSetGroupId.setStatus(_A)
class _H3ce1TimeSlotSetSignalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('unkown',1),('em-delay',2),('em-immediate',3),('em-wink',4),('fxo-ground',5),('fxo-loop',6),('fxs-ground',7),('fxs-loop',8),('r2',9)))
_H3ce1TimeSlotSetSignalType_Type.__name__=_C
_H3ce1TimeSlotSetSignalType_Object=MibTableColumn
h3ce1TimeSlotSetSignalType=_H3ce1TimeSlotSetSignalType_Object((1,3,6,1,4,1,2011,10,2,28,4,1,2),_H3ce1TimeSlotSetSignalType_Type())
h3ce1TimeSlotSetSignalType.setMaxAccess(_G)
if mibBuilder.loadTexts:h3ce1TimeSlotSetSignalType.setStatus(_A)
_H3ce1TimeSlotSetList_Type=H3cE1TimeSlot
_H3ce1TimeSlotSetList_Object=MibTableColumn
h3ce1TimeSlotSetList=_H3ce1TimeSlotSetList_Object((1,3,6,1,4,1,2011,10,2,28,4,1,3),_H3ce1TimeSlotSetList_Type())
h3ce1TimeSlotSetList.setMaxAccess(_G)
if mibBuilder.loadTexts:h3ce1TimeSlotSetList.setStatus(_A)
_H3ce1TimeSlotSetRowStatus_Type=RowStatus
_H3ce1TimeSlotSetRowStatus_Object=MibTableColumn
h3ce1TimeSlotSetRowStatus=_H3ce1TimeSlotSetRowStatus_Object((1,3,6,1,4,1,2011,10,2,28,4,1,4),_H3ce1TimeSlotSetRowStatus_Type())
h3ce1TimeSlotSetRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3ce1TimeSlotSetRowStatus.setStatus(_A)
mibBuilder.exportSymbols('H3C-E1-MIB',**{'H3cE1TimeSlot':H3cE1TimeSlot,'h3cE1':h3cE1,'e1InterfaceStatusTable':e1InterfaceStatusTable,'e1InterfaceStatusEntry':e1InterfaceStatusEntry,'e1InterfaceInErrs':e1InterfaceInErrs,'e1InterfaceInRuntsErrs':e1InterfaceInRuntsErrs,'e1InterfaceInGiantsErrs':e1InterfaceInGiantsErrs,'e1InterfaceInCrcErrs':e1InterfaceInCrcErrs,'e1InterfaceInAlignErrs':e1InterfaceInAlignErrs,'e1InterfaceInOverRunsErrs':e1InterfaceInOverRunsErrs,'e1InterfaceInDribblesErrs':e1InterfaceInDribblesErrs,'e1InterfaceInAbortedSeqErrs':e1InterfaceInAbortedSeqErrs,'e1InterfaceInNoBufferErrs':e1InterfaceInNoBufferErrs,'e1InterfaceInFramingErrs':e1InterfaceInFramingErrs,'e1InterfaceOutputErrs':e1InterfaceOutputErrs,'e1InterfaceOutUnderRunErrs':e1InterfaceOutUnderRunErrs,'e1InterfaceOutCollisonsErrs':e1InterfaceOutCollisonsErrs,'e1InterfaceOutDeferedErrs':e1InterfaceOutDeferedErrs,'h3ce1Table':h3ce1Table,'h3ce1Entry':h3ce1Entry,'h3ce1Type':h3ce1Type,'h3ce1Clock':h3ce1Clock,'h3ce1FrameFormat':h3ce1FrameFormat,'h3ce1LineCode':h3ce1LineCode,'h3ce1PriSetTimeSlot':h3ce1PriSetTimeSlot,'h3ce1DChannelIndex':h3ce1DChannelIndex,'h3ce1SubScribLineChannelIndex':h3ce1SubScribLineChannelIndex,'h3ce1FcmChannelIndex':h3ce1FcmChannelIndex,'h3ce1InterfaceTable':h3ce1InterfaceTable,'h3ce1InterfaceEntry':h3ce1InterfaceEntry,'h3ce1ControllerIndex':h3ce1ControllerIndex,'h3ce1TimeSlotSetTable':h3ce1TimeSlotSetTable,'h3ce1TimeSlotSetEntry':h3ce1TimeSlotSetEntry,'h3ce1TimeSlotSetGroupId':h3ce1TimeSlotSetGroupId,'h3ce1TimeSlotSetSignalType':h3ce1TimeSlotSetSignalType,'h3ce1TimeSlotSetList':h3ce1TimeSlotSetList,'h3ce1TimeSlotSetRowStatus':h3ce1TimeSlotSetRowStatus})