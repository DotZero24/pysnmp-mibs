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
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfE1=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,28))
if mibBuilder.loadTexts:hpnicfE1.setRevisions(('2012-07-16 17:41','2010-04-08 18:55','2009-06-08 17:41','2004-12-01 14:36'))
class HpnicfE1TimeSlot(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_Hpnicfe1InterfaceStatusTable_Object=MibTable
hpnicfe1InterfaceStatusTable=_Hpnicfe1InterfaceStatusTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1))
if mibBuilder.loadTexts:hpnicfe1InterfaceStatusTable.setStatus(_A)
_Hpnicfe1InterfaceStatusEntry_Object=MibTableRow
hpnicfe1InterfaceStatusEntry=_Hpnicfe1InterfaceStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1,1))
hpnicfe1InterfaceStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfe1InterfaceStatusEntry.setStatus(_A)
_Hpnicfe1InterfaceInErrs_Type=Counter32
_Hpnicfe1InterfaceInErrs_Object=MibTableColumn
hpnicfe1InterfaceInErrs=_Hpnicfe1InterfaceInErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1,1,1),_Hpnicfe1InterfaceInErrs_Type())
hpnicfe1InterfaceInErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1InterfaceInErrs.setStatus(_A)
_Hpnicfe1InterfaceInRuntsErrs_Type=Counter32
_Hpnicfe1InterfaceInRuntsErrs_Object=MibTableColumn
hpnicfe1InterfaceInRuntsErrs=_Hpnicfe1InterfaceInRuntsErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1,1,2),_Hpnicfe1InterfaceInRuntsErrs_Type())
hpnicfe1InterfaceInRuntsErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1InterfaceInRuntsErrs.setStatus(_A)
_Hpnicfe1InterfaceInGiantsErrs_Type=Counter32
_Hpnicfe1InterfaceInGiantsErrs_Object=MibTableColumn
hpnicfe1InterfaceInGiantsErrs=_Hpnicfe1InterfaceInGiantsErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1,1,3),_Hpnicfe1InterfaceInGiantsErrs_Type())
hpnicfe1InterfaceInGiantsErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1InterfaceInGiantsErrs.setStatus(_A)
_Hpnicfe1InterfaceInCrcErrs_Type=Counter32
_Hpnicfe1InterfaceInCrcErrs_Object=MibTableColumn
hpnicfe1InterfaceInCrcErrs=_Hpnicfe1InterfaceInCrcErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1,1,4),_Hpnicfe1InterfaceInCrcErrs_Type())
hpnicfe1InterfaceInCrcErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1InterfaceInCrcErrs.setStatus(_A)
_Hpnicfe1InterfaceInAlignErrs_Type=Counter32
_Hpnicfe1InterfaceInAlignErrs_Object=MibTableColumn
hpnicfe1InterfaceInAlignErrs=_Hpnicfe1InterfaceInAlignErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1,1,5),_Hpnicfe1InterfaceInAlignErrs_Type())
hpnicfe1InterfaceInAlignErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1InterfaceInAlignErrs.setStatus(_A)
_Hpnicfe1InterfaceInOverRunsErrs_Type=Counter32
_Hpnicfe1InterfaceInOverRunsErrs_Object=MibTableColumn
hpnicfe1InterfaceInOverRunsErrs=_Hpnicfe1InterfaceInOverRunsErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1,1,6),_Hpnicfe1InterfaceInOverRunsErrs_Type())
hpnicfe1InterfaceInOverRunsErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1InterfaceInOverRunsErrs.setStatus(_A)
_Hpnicfe1InterfaceInDribblesErrs_Type=Counter32
_Hpnicfe1InterfaceInDribblesErrs_Object=MibTableColumn
hpnicfe1InterfaceInDribblesErrs=_Hpnicfe1InterfaceInDribblesErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1,1,7),_Hpnicfe1InterfaceInDribblesErrs_Type())
hpnicfe1InterfaceInDribblesErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1InterfaceInDribblesErrs.setStatus(_A)
_Hpnicfe1InterfaceInAbortedSeqErrs_Type=Counter32
_Hpnicfe1InterfaceInAbortedSeqErrs_Object=MibTableColumn
hpnicfe1InterfaceInAbortedSeqErrs=_Hpnicfe1InterfaceInAbortedSeqErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1,1,8),_Hpnicfe1InterfaceInAbortedSeqErrs_Type())
hpnicfe1InterfaceInAbortedSeqErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1InterfaceInAbortedSeqErrs.setStatus(_A)
_Hpnicfe1InterfaceInNoBufferErrs_Type=Counter32
_Hpnicfe1InterfaceInNoBufferErrs_Object=MibTableColumn
hpnicfe1InterfaceInNoBufferErrs=_Hpnicfe1InterfaceInNoBufferErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1,1,9),_Hpnicfe1InterfaceInNoBufferErrs_Type())
hpnicfe1InterfaceInNoBufferErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1InterfaceInNoBufferErrs.setStatus(_A)
_Hpnicfe1InterfaceInFramingErrs_Type=Counter32
_Hpnicfe1InterfaceInFramingErrs_Object=MibTableColumn
hpnicfe1InterfaceInFramingErrs=_Hpnicfe1InterfaceInFramingErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1,1,10),_Hpnicfe1InterfaceInFramingErrs_Type())
hpnicfe1InterfaceInFramingErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1InterfaceInFramingErrs.setStatus(_A)
_Hpnicfe1InterfaceOutputErrs_Type=Counter32
_Hpnicfe1InterfaceOutputErrs_Object=MibTableColumn
hpnicfe1InterfaceOutputErrs=_Hpnicfe1InterfaceOutputErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1,1,11),_Hpnicfe1InterfaceOutputErrs_Type())
hpnicfe1InterfaceOutputErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1InterfaceOutputErrs.setStatus(_A)
_Hpnicfe1InterfaceOutUnderRunErrs_Type=Counter32
_Hpnicfe1InterfaceOutUnderRunErrs_Object=MibTableColumn
hpnicfe1InterfaceOutUnderRunErrs=_Hpnicfe1InterfaceOutUnderRunErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1,1,12),_Hpnicfe1InterfaceOutUnderRunErrs_Type())
hpnicfe1InterfaceOutUnderRunErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1InterfaceOutUnderRunErrs.setStatus(_A)
_Hpnicfe1InterfaceOutCollisonsErrs_Type=Counter32
_Hpnicfe1InterfaceOutCollisonsErrs_Object=MibTableColumn
hpnicfe1InterfaceOutCollisonsErrs=_Hpnicfe1InterfaceOutCollisonsErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1,1,13),_Hpnicfe1InterfaceOutCollisonsErrs_Type())
hpnicfe1InterfaceOutCollisonsErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1InterfaceOutCollisonsErrs.setStatus(_A)
_Hpnicfe1InterfaceOutDeferedErrs_Type=Counter32
_Hpnicfe1InterfaceOutDeferedErrs_Object=MibTableColumn
hpnicfe1InterfaceOutDeferedErrs=_Hpnicfe1InterfaceOutDeferedErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,1,1,14),_Hpnicfe1InterfaceOutDeferedErrs_Type())
hpnicfe1InterfaceOutDeferedErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1InterfaceOutDeferedErrs.setStatus(_A)
_Hpnicfe1Table_Object=MibTable
hpnicfe1Table=_Hpnicfe1Table_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,2))
if mibBuilder.loadTexts:hpnicfe1Table.setStatus(_A)
_Hpnicfe1Entry_Object=MibTableRow
hpnicfe1Entry=_Hpnicfe1Entry_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,2,1))
hpnicfe1Entry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfe1Entry.setStatus(_A)
class _Hpnicfe1Type_Type(Bits):namedValues=NamedValues(*(('voice',0),('pos',1)))
_Hpnicfe1Type_Type.__name__='Bits'
_Hpnicfe1Type_Object=MibTableColumn
hpnicfe1Type=_Hpnicfe1Type_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,2,1,1),_Hpnicfe1Type_Type())
hpnicfe1Type.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1Type.setStatus(_A)
class _Hpnicfe1Clock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('slave',1),('master',2),('internal',3),('line',4),('linePri',5)))
_Hpnicfe1Clock_Type.__name__=_C
_Hpnicfe1Clock_Object=MibTableColumn
hpnicfe1Clock=_Hpnicfe1Clock_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,2,1,2),_Hpnicfe1Clock_Type())
hpnicfe1Clock.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfe1Clock.setStatus(_A)
class _Hpnicfe1FrameFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('crc4',1),('nocrc4',2)))
_Hpnicfe1FrameFormat_Type.__name__=_C
_Hpnicfe1FrameFormat_Object=MibTableColumn
hpnicfe1FrameFormat=_Hpnicfe1FrameFormat_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,2,1,3),_Hpnicfe1FrameFormat_Type())
hpnicfe1FrameFormat.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfe1FrameFormat.setStatus(_A)
class _Hpnicfe1LineCode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*(('ami',1),('hdb3',3)))
_Hpnicfe1LineCode_Type.__name__=_C
_Hpnicfe1LineCode_Object=MibTableColumn
hpnicfe1LineCode=_Hpnicfe1LineCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,2,1,4),_Hpnicfe1LineCode_Type())
hpnicfe1LineCode.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfe1LineCode.setStatus(_A)
_Hpnicfe1PriSetTimeSlot_Type=HpnicfE1TimeSlot
_Hpnicfe1PriSetTimeSlot_Object=MibTableColumn
hpnicfe1PriSetTimeSlot=_Hpnicfe1PriSetTimeSlot_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,2,1,5),_Hpnicfe1PriSetTimeSlot_Type())
hpnicfe1PriSetTimeSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfe1PriSetTimeSlot.setStatus(_A)
_Hpnicfe1DChannelIndex_Type=Integer32
_Hpnicfe1DChannelIndex_Object=MibTableColumn
hpnicfe1DChannelIndex=_Hpnicfe1DChannelIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,2,1,6),_Hpnicfe1DChannelIndex_Type())
hpnicfe1DChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1DChannelIndex.setStatus(_A)
_Hpnicfe1SubScribLineChannelIndex_Type=Integer32
_Hpnicfe1SubScribLineChannelIndex_Object=MibTableColumn
hpnicfe1SubScribLineChannelIndex=_Hpnicfe1SubScribLineChannelIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,2,1,7),_Hpnicfe1SubScribLineChannelIndex_Type())
hpnicfe1SubScribLineChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1SubScribLineChannelIndex.setStatus(_A)
_Hpnicfe1FcmChannelIndex_Type=Integer32
_Hpnicfe1FcmChannelIndex_Object=MibTableColumn
hpnicfe1FcmChannelIndex=_Hpnicfe1FcmChannelIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,2,1,8),_Hpnicfe1FcmChannelIndex_Type())
hpnicfe1FcmChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1FcmChannelIndex.setStatus(_A)
_Hpnicfe1InterfaceTable_Object=MibTable
hpnicfe1InterfaceTable=_Hpnicfe1InterfaceTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,3))
if mibBuilder.loadTexts:hpnicfe1InterfaceTable.setStatus(_A)
_Hpnicfe1InterfaceEntry_Object=MibTableRow
hpnicfe1InterfaceEntry=_Hpnicfe1InterfaceEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,3,1))
hpnicfe1InterfaceEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfe1InterfaceEntry.setStatus(_A)
_Hpnicfe1ControllerIndex_Type=Integer32
_Hpnicfe1ControllerIndex_Object=MibTableColumn
hpnicfe1ControllerIndex=_Hpnicfe1ControllerIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,3,1,1),_Hpnicfe1ControllerIndex_Type())
hpnicfe1ControllerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfe1ControllerIndex.setStatus(_A)
_Hpnicfe1TimeSlotSetTable_Object=MibTable
hpnicfe1TimeSlotSetTable=_Hpnicfe1TimeSlotSetTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,4))
if mibBuilder.loadTexts:hpnicfe1TimeSlotSetTable.setStatus(_A)
_Hpnicfe1TimeSlotSetEntry_Object=MibTableRow
hpnicfe1TimeSlotSetEntry=_Hpnicfe1TimeSlotSetEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,4,1))
hpnicfe1TimeSlotSetEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfe1TimeSlotSetEntry.setStatus(_A)
class _Hpnicfe1TimeSlotSetGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_Hpnicfe1TimeSlotSetGroupId_Type.__name__=_C
_Hpnicfe1TimeSlotSetGroupId_Object=MibTableColumn
hpnicfe1TimeSlotSetGroupId=_Hpnicfe1TimeSlotSetGroupId_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,4,1,1),_Hpnicfe1TimeSlotSetGroupId_Type())
hpnicfe1TimeSlotSetGroupId.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfe1TimeSlotSetGroupId.setStatus(_A)
class _Hpnicfe1TimeSlotSetSignalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('unkown',1),('em-delay',2),('em-immediate',3),('em-wink',4),('fxo-ground',5),('fxo-loop',6),('fxs-ground',7),('fxs-loop',8),('r2',9)))
_Hpnicfe1TimeSlotSetSignalType_Type.__name__=_C
_Hpnicfe1TimeSlotSetSignalType_Object=MibTableColumn
hpnicfe1TimeSlotSetSignalType=_Hpnicfe1TimeSlotSetSignalType_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,4,1,2),_Hpnicfe1TimeSlotSetSignalType_Type())
hpnicfe1TimeSlotSetSignalType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfe1TimeSlotSetSignalType.setStatus(_A)
_Hpnicfe1TimeSlotSetList_Type=HpnicfE1TimeSlot
_Hpnicfe1TimeSlotSetList_Object=MibTableColumn
hpnicfe1TimeSlotSetList=_Hpnicfe1TimeSlotSetList_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,4,1,3),_Hpnicfe1TimeSlotSetList_Type())
hpnicfe1TimeSlotSetList.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfe1TimeSlotSetList.setStatus(_A)
_Hpnicfe1TimeSlotSetRowStatus_Type=RowStatus
_Hpnicfe1TimeSlotSetRowStatus_Object=MibTableColumn
hpnicfe1TimeSlotSetRowStatus=_Hpnicfe1TimeSlotSetRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,28,4,1,4),_Hpnicfe1TimeSlotSetRowStatus_Type())
hpnicfe1TimeSlotSetRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfe1TimeSlotSetRowStatus.setStatus(_A)
mibBuilder.exportSymbols('HPN-ICF-E1-MIB',**{'HpnicfE1TimeSlot':HpnicfE1TimeSlot,'hpnicfE1':hpnicfE1,'hpnicfe1InterfaceStatusTable':hpnicfe1InterfaceStatusTable,'hpnicfe1InterfaceStatusEntry':hpnicfe1InterfaceStatusEntry,'hpnicfe1InterfaceInErrs':hpnicfe1InterfaceInErrs,'hpnicfe1InterfaceInRuntsErrs':hpnicfe1InterfaceInRuntsErrs,'hpnicfe1InterfaceInGiantsErrs':hpnicfe1InterfaceInGiantsErrs,'hpnicfe1InterfaceInCrcErrs':hpnicfe1InterfaceInCrcErrs,'hpnicfe1InterfaceInAlignErrs':hpnicfe1InterfaceInAlignErrs,'hpnicfe1InterfaceInOverRunsErrs':hpnicfe1InterfaceInOverRunsErrs,'hpnicfe1InterfaceInDribblesErrs':hpnicfe1InterfaceInDribblesErrs,'hpnicfe1InterfaceInAbortedSeqErrs':hpnicfe1InterfaceInAbortedSeqErrs,'hpnicfe1InterfaceInNoBufferErrs':hpnicfe1InterfaceInNoBufferErrs,'hpnicfe1InterfaceInFramingErrs':hpnicfe1InterfaceInFramingErrs,'hpnicfe1InterfaceOutputErrs':hpnicfe1InterfaceOutputErrs,'hpnicfe1InterfaceOutUnderRunErrs':hpnicfe1InterfaceOutUnderRunErrs,'hpnicfe1InterfaceOutCollisonsErrs':hpnicfe1InterfaceOutCollisonsErrs,'hpnicfe1InterfaceOutDeferedErrs':hpnicfe1InterfaceOutDeferedErrs,'hpnicfe1Table':hpnicfe1Table,'hpnicfe1Entry':hpnicfe1Entry,'hpnicfe1Type':hpnicfe1Type,'hpnicfe1Clock':hpnicfe1Clock,'hpnicfe1FrameFormat':hpnicfe1FrameFormat,'hpnicfe1LineCode':hpnicfe1LineCode,'hpnicfe1PriSetTimeSlot':hpnicfe1PriSetTimeSlot,'hpnicfe1DChannelIndex':hpnicfe1DChannelIndex,'hpnicfe1SubScribLineChannelIndex':hpnicfe1SubScribLineChannelIndex,'hpnicfe1FcmChannelIndex':hpnicfe1FcmChannelIndex,'hpnicfe1InterfaceTable':hpnicfe1InterfaceTable,'hpnicfe1InterfaceEntry':hpnicfe1InterfaceEntry,'hpnicfe1ControllerIndex':hpnicfe1ControllerIndex,'hpnicfe1TimeSlotSetTable':hpnicfe1TimeSlotSetTable,'hpnicfe1TimeSlotSetEntry':hpnicfe1TimeSlotSetEntry,'hpnicfe1TimeSlotSetGroupId':hpnicfe1TimeSlotSetGroupId,'hpnicfe1TimeSlotSetSignalType':hpnicfe1TimeSlotSetSignalType,'hpnicfe1TimeSlotSetList':hpnicfe1TimeSlotSetList,'hpnicfe1TimeSlotSetRowStatus':hpnicfe1TimeSlotSetRowStatus})