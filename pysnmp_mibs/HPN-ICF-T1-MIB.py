_F='read-write'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfT1=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,29))
if mibBuilder.loadTexts:hpnicfT1.setRevisions(('2012-07-16 17:41','2009-06-08 17:41','2004-12-01 14:36'))
class HpnicfT1TimeSlot(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_Hpnicft1InterfaceStatusTable_Object=MibTable
hpnicft1InterfaceStatusTable=_Hpnicft1InterfaceStatusTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1))
if mibBuilder.loadTexts:hpnicft1InterfaceStatusTable.setStatus(_A)
_Hpnicft1InterfaceStatusEntry_Object=MibTableRow
hpnicft1InterfaceStatusEntry=_Hpnicft1InterfaceStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1,1))
hpnicft1InterfaceStatusEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:hpnicft1InterfaceStatusEntry.setStatus(_A)
_Hpnicft1InterfaceInErrs_Type=Counter32
_Hpnicft1InterfaceInErrs_Object=MibTableColumn
hpnicft1InterfaceInErrs=_Hpnicft1InterfaceInErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1,1,1),_Hpnicft1InterfaceInErrs_Type())
hpnicft1InterfaceInErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1InterfaceInErrs.setStatus(_A)
_Hpnicft1InterfaceInRuntsErrs_Type=Counter32
_Hpnicft1InterfaceInRuntsErrs_Object=MibTableColumn
hpnicft1InterfaceInRuntsErrs=_Hpnicft1InterfaceInRuntsErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1,1,2),_Hpnicft1InterfaceInRuntsErrs_Type())
hpnicft1InterfaceInRuntsErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1InterfaceInRuntsErrs.setStatus(_A)
_Hpnicft1InterfaceInGiantsErrs_Type=Counter32
_Hpnicft1InterfaceInGiantsErrs_Object=MibTableColumn
hpnicft1InterfaceInGiantsErrs=_Hpnicft1InterfaceInGiantsErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1,1,3),_Hpnicft1InterfaceInGiantsErrs_Type())
hpnicft1InterfaceInGiantsErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1InterfaceInGiantsErrs.setStatus(_A)
_Hpnicft1InterfaceInCrcErrs_Type=Counter32
_Hpnicft1InterfaceInCrcErrs_Object=MibTableColumn
hpnicft1InterfaceInCrcErrs=_Hpnicft1InterfaceInCrcErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1,1,4),_Hpnicft1InterfaceInCrcErrs_Type())
hpnicft1InterfaceInCrcErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1InterfaceInCrcErrs.setStatus(_A)
_Hpnicft1InterfaceInAlignErrs_Type=Counter32
_Hpnicft1InterfaceInAlignErrs_Object=MibTableColumn
hpnicft1InterfaceInAlignErrs=_Hpnicft1InterfaceInAlignErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1,1,5),_Hpnicft1InterfaceInAlignErrs_Type())
hpnicft1InterfaceInAlignErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1InterfaceInAlignErrs.setStatus(_A)
_Hpnicft1InterfaceInOverRunsErrs_Type=Counter32
_Hpnicft1InterfaceInOverRunsErrs_Object=MibTableColumn
hpnicft1InterfaceInOverRunsErrs=_Hpnicft1InterfaceInOverRunsErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1,1,6),_Hpnicft1InterfaceInOverRunsErrs_Type())
hpnicft1InterfaceInOverRunsErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1InterfaceInOverRunsErrs.setStatus(_A)
_Hpnicft1InterfaceInDribblesErrs_Type=Counter32
_Hpnicft1InterfaceInDribblesErrs_Object=MibTableColumn
hpnicft1InterfaceInDribblesErrs=_Hpnicft1InterfaceInDribblesErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1,1,7),_Hpnicft1InterfaceInDribblesErrs_Type())
hpnicft1InterfaceInDribblesErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1InterfaceInDribblesErrs.setStatus(_A)
_Hpnicft1InterfaceInAbortedSeqErrs_Type=Counter32
_Hpnicft1InterfaceInAbortedSeqErrs_Object=MibTableColumn
hpnicft1InterfaceInAbortedSeqErrs=_Hpnicft1InterfaceInAbortedSeqErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1,1,8),_Hpnicft1InterfaceInAbortedSeqErrs_Type())
hpnicft1InterfaceInAbortedSeqErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1InterfaceInAbortedSeqErrs.setStatus(_A)
_Hpnicft1InterfaceInNoBufferErrs_Type=Counter32
_Hpnicft1InterfaceInNoBufferErrs_Object=MibTableColumn
hpnicft1InterfaceInNoBufferErrs=_Hpnicft1InterfaceInNoBufferErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1,1,9),_Hpnicft1InterfaceInNoBufferErrs_Type())
hpnicft1InterfaceInNoBufferErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1InterfaceInNoBufferErrs.setStatus(_A)
_Hpnicft1InterfaceInFramingErrs_Type=Counter32
_Hpnicft1InterfaceInFramingErrs_Object=MibTableColumn
hpnicft1InterfaceInFramingErrs=_Hpnicft1InterfaceInFramingErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1,1,10),_Hpnicft1InterfaceInFramingErrs_Type())
hpnicft1InterfaceInFramingErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1InterfaceInFramingErrs.setStatus(_A)
_Hpnicft1InterfaceOutputErrs_Type=Counter32
_Hpnicft1InterfaceOutputErrs_Object=MibTableColumn
hpnicft1InterfaceOutputErrs=_Hpnicft1InterfaceOutputErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1,1,11),_Hpnicft1InterfaceOutputErrs_Type())
hpnicft1InterfaceOutputErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1InterfaceOutputErrs.setStatus(_A)
_Hpnicft1InterfaceOutUnderRunErrs_Type=Counter32
_Hpnicft1InterfaceOutUnderRunErrs_Object=MibTableColumn
hpnicft1InterfaceOutUnderRunErrs=_Hpnicft1InterfaceOutUnderRunErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1,1,12),_Hpnicft1InterfaceOutUnderRunErrs_Type())
hpnicft1InterfaceOutUnderRunErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1InterfaceOutUnderRunErrs.setStatus(_A)
_Hpnicft1InterfaceOutCollisonsErrs_Type=Counter32
_Hpnicft1InterfaceOutCollisonsErrs_Object=MibTableColumn
hpnicft1InterfaceOutCollisonsErrs=_Hpnicft1InterfaceOutCollisonsErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1,1,13),_Hpnicft1InterfaceOutCollisonsErrs_Type())
hpnicft1InterfaceOutCollisonsErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1InterfaceOutCollisonsErrs.setStatus(_A)
_Hpnicft1InterfaceOutDeferedErrs_Type=Counter32
_Hpnicft1InterfaceOutDeferedErrs_Object=MibTableColumn
hpnicft1InterfaceOutDeferedErrs=_Hpnicft1InterfaceOutDeferedErrs_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,1,1,14),_Hpnicft1InterfaceOutDeferedErrs_Type())
hpnicft1InterfaceOutDeferedErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1InterfaceOutDeferedErrs.setStatus(_A)
_Hpnicft1Table_Object=MibTable
hpnicft1Table=_Hpnicft1Table_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,2))
if mibBuilder.loadTexts:hpnicft1Table.setStatus(_A)
_Hpnicft1Entry_Object=MibTableRow
hpnicft1Entry=_Hpnicft1Entry_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,2,1))
hpnicft1Entry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:hpnicft1Entry.setStatus(_A)
class _Hpnicft1Type_Type(Bits):namedValues=NamedValues(('voice',0))
_Hpnicft1Type_Type.__name__='Bits'
_Hpnicft1Type_Object=MibTableColumn
hpnicft1Type=_Hpnicft1Type_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,2,1,1),_Hpnicft1Type_Type())
hpnicft1Type.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1Type.setStatus(_A)
class _Hpnicft1Clock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('slave',1),('master',2),('internal',3),('line',4),('linePri',5)))
_Hpnicft1Clock_Type.__name__=_E
_Hpnicft1Clock_Object=MibTableColumn
hpnicft1Clock=_Hpnicft1Clock_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,2,1,2),_Hpnicft1Clock_Type())
hpnicft1Clock.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicft1Clock.setStatus(_A)
class _Hpnicft1FrameFormat_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sf',1),('esf',2)))
_Hpnicft1FrameFormat_Type.__name__=_E
_Hpnicft1FrameFormat_Object=MibTableColumn
hpnicft1FrameFormat=_Hpnicft1FrameFormat_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,2,1,3),_Hpnicft1FrameFormat_Type())
hpnicft1FrameFormat.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicft1FrameFormat.setStatus(_A)
class _Hpnicft1LineCode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ami',1),('b8zs',2)))
_Hpnicft1LineCode_Type.__name__=_E
_Hpnicft1LineCode_Object=MibTableColumn
hpnicft1LineCode=_Hpnicft1LineCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,2,1,4),_Hpnicft1LineCode_Type())
hpnicft1LineCode.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicft1LineCode.setStatus(_A)
_Hpnicft1PriSetTimeSlot_Type=HpnicfT1TimeSlot
_Hpnicft1PriSetTimeSlot_Object=MibTableColumn
hpnicft1PriSetTimeSlot=_Hpnicft1PriSetTimeSlot_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,2,1,5),_Hpnicft1PriSetTimeSlot_Type())
hpnicft1PriSetTimeSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicft1PriSetTimeSlot.setStatus(_A)
_Hpnicft1DChannelIndex_Type=Integer32
_Hpnicft1DChannelIndex_Object=MibTableColumn
hpnicft1DChannelIndex=_Hpnicft1DChannelIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,2,1,6),_Hpnicft1DChannelIndex_Type())
hpnicft1DChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1DChannelIndex.setStatus(_A)
_Hpnicft1SubScribLineChannelIndex_Type=Integer32
_Hpnicft1SubScribLineChannelIndex_Object=MibTableColumn
hpnicft1SubScribLineChannelIndex=_Hpnicft1SubScribLineChannelIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,2,1,7),_Hpnicft1SubScribLineChannelIndex_Type())
hpnicft1SubScribLineChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1SubScribLineChannelIndex.setStatus(_A)
_Hpnicft1InterfaceTable_Object=MibTable
hpnicft1InterfaceTable=_Hpnicft1InterfaceTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,3))
if mibBuilder.loadTexts:hpnicft1InterfaceTable.setStatus(_A)
_Hpnicft1InterfaceEntry_Object=MibTableRow
hpnicft1InterfaceEntry=_Hpnicft1InterfaceEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,3,1))
hpnicft1InterfaceEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:hpnicft1InterfaceEntry.setStatus(_A)
_Hpnicft1ControllerIndex_Type=Integer32
_Hpnicft1ControllerIndex_Object=MibTableColumn
hpnicft1ControllerIndex=_Hpnicft1ControllerIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,29,3,1,1),_Hpnicft1ControllerIndex_Type())
hpnicft1ControllerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicft1ControllerIndex.setStatus(_A)
mibBuilder.exportSymbols('HPN-ICF-T1-MIB',**{'HpnicfT1TimeSlot':HpnicfT1TimeSlot,'hpnicfT1':hpnicfT1,'hpnicft1InterfaceStatusTable':hpnicft1InterfaceStatusTable,'hpnicft1InterfaceStatusEntry':hpnicft1InterfaceStatusEntry,'hpnicft1InterfaceInErrs':hpnicft1InterfaceInErrs,'hpnicft1InterfaceInRuntsErrs':hpnicft1InterfaceInRuntsErrs,'hpnicft1InterfaceInGiantsErrs':hpnicft1InterfaceInGiantsErrs,'hpnicft1InterfaceInCrcErrs':hpnicft1InterfaceInCrcErrs,'hpnicft1InterfaceInAlignErrs':hpnicft1InterfaceInAlignErrs,'hpnicft1InterfaceInOverRunsErrs':hpnicft1InterfaceInOverRunsErrs,'hpnicft1InterfaceInDribblesErrs':hpnicft1InterfaceInDribblesErrs,'hpnicft1InterfaceInAbortedSeqErrs':hpnicft1InterfaceInAbortedSeqErrs,'hpnicft1InterfaceInNoBufferErrs':hpnicft1InterfaceInNoBufferErrs,'hpnicft1InterfaceInFramingErrs':hpnicft1InterfaceInFramingErrs,'hpnicft1InterfaceOutputErrs':hpnicft1InterfaceOutputErrs,'hpnicft1InterfaceOutUnderRunErrs':hpnicft1InterfaceOutUnderRunErrs,'hpnicft1InterfaceOutCollisonsErrs':hpnicft1InterfaceOutCollisonsErrs,'hpnicft1InterfaceOutDeferedErrs':hpnicft1InterfaceOutDeferedErrs,'hpnicft1Table':hpnicft1Table,'hpnicft1Entry':hpnicft1Entry,'hpnicft1Type':hpnicft1Type,'hpnicft1Clock':hpnicft1Clock,'hpnicft1FrameFormat':hpnicft1FrameFormat,'hpnicft1LineCode':hpnicft1LineCode,'hpnicft1PriSetTimeSlot':hpnicft1PriSetTimeSlot,'hpnicft1DChannelIndex':hpnicft1DChannelIndex,'hpnicft1SubScribLineChannelIndex':hpnicft1SubScribLineChannelIndex,'hpnicft1InterfaceTable':hpnicft1InterfaceTable,'hpnicft1InterfaceEntry':hpnicft1InterfaceEntry,'hpnicft1ControllerIndex':hpnicft1ControllerIndex})