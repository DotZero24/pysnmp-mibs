_U='pdhLogPrtStatisIndex'
_T='remove'
_S='trSwitchLoopDetect'
_R='vcgLcasMembersLinkIndex'
_Q='vcgLcasMembersVcgIndex'
_P='pdhLogPrtStatusIndex'
_O='pdhLogPrtIndex'
_N='pdhLogPrtCnfgIdx'
_M='dnu'
_L='norm'
_K='add'
_J='illegal'
_I='idle'
_H='ok'
_G='fail'
_F='not-accessible'
_E='RAD-PDH-MIB'
_D='notApplicable'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
diverseIfWanGen,=mibBuilder.importSymbols('RAD-SMI-MIB','diverseIfWanGen')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdhInterface=ModuleIdentity((1,3,6,1,4,1,164,3,1,6,16))
_PdhIfConfig_ObjectIdentity=ObjectIdentity
pdhIfConfig=_PdhIfConfig_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,16,1))
_PdhLogPrtConfigTable_Object=MibTable
pdhLogPrtConfigTable=_PdhLogPrtConfigTable_Object((1,3,6,1,4,1,164,3,1,6,16,1,1))
if mibBuilder.loadTexts:pdhLogPrtConfigTable.setStatus(_A)
_PdhLogPrtConfigEntry_Object=MibTableRow
pdhLogPrtConfigEntry=_PdhLogPrtConfigEntry_Object((1,3,6,1,4,1,164,3,1,6,16,1,1,1))
pdhLogPrtConfigEntry.setIndexNames((0,_E,_N),(0,_E,_O))
if mibBuilder.loadTexts:pdhLogPrtConfigEntry.setStatus(_A)
class _PdhLogPrtCnfgIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PdhLogPrtCnfgIdx_Type.__name__=_C
_PdhLogPrtCnfgIdx_Object=MibTableColumn
pdhLogPrtCnfgIdx=_PdhLogPrtCnfgIdx_Object((1,3,6,1,4,1,164,3,1,6,16,1,1,1,1),_PdhLogPrtCnfgIdx_Type())
pdhLogPrtCnfgIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:pdhLogPrtCnfgIdx.setStatus(_A)
_PdhLogPrtIndex_Type=Unsigned32
_PdhLogPrtIndex_Object=MibTableColumn
pdhLogPrtIndex=_PdhLogPrtIndex_Object((1,3,6,1,4,1,164,3,1,6,16,1,1,1,2),_PdhLogPrtIndex_Type())
pdhLogPrtIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pdhLogPrtIndex.setStatus(_A)
_PdhLogPrtMaxDiffDelay_Type=Unsigned32
_PdhLogPrtMaxDiffDelay_Object=MibTableColumn
pdhLogPrtMaxDiffDelay=_PdhLogPrtMaxDiffDelay_Object((1,3,6,1,4,1,164,3,1,6,16,1,1,1,3),_PdhLogPrtMaxDiffDelay_Type())
pdhLogPrtMaxDiffDelay.setMaxAccess('read-write')
if mibBuilder.loadTexts:pdhLogPrtMaxDiffDelay.setStatus(_A)
_PdhIfStatus_ObjectIdentity=ObjectIdentity
pdhIfStatus=_PdhIfStatus_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,16,2))
_PdhLogPrtStatusTable_Object=MibTable
pdhLogPrtStatusTable=_PdhLogPrtStatusTable_Object((1,3,6,1,4,1,164,3,1,6,16,2,1))
if mibBuilder.loadTexts:pdhLogPrtStatusTable.setStatus(_A)
_PdhLogPrtStatusEntry_Object=MibTableRow
pdhLogPrtStatusEntry=_PdhLogPrtStatusEntry_Object((1,3,6,1,4,1,164,3,1,6,16,2,1,1))
pdhLogPrtStatusEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:pdhLogPrtStatusEntry.setStatus(_A)
_PdhLogPrtStatusIndex_Type=Unsigned32
_PdhLogPrtStatusIndex_Object=MibTableColumn
pdhLogPrtStatusIndex=_PdhLogPrtStatusIndex_Object((1,3,6,1,4,1,164,3,1,6,16,2,1,1,1),_PdhLogPrtStatusIndex_Type())
pdhLogPrtStatusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pdhLogPrtStatusIndex.setStatus(_A)
class _PdhLogPrtFrameDelineation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('notDelineated',2),('delineated',3)))
_PdhLogPrtFrameDelineation_Type.__name__=_C
_PdhLogPrtFrameDelineation_Object=MibTableColumn
pdhLogPrtFrameDelineation=_PdhLogPrtFrameDelineation_Object((1,3,6,1,4,1,164,3,1,6,16,2,1,1,2),_PdhLogPrtFrameDelineation_Type())
pdhLogPrtFrameDelineation.setMaxAccess(_B)
if mibBuilder.loadTexts:pdhLogPrtFrameDelineation.setStatus(_A)
_PdhLogPrtDiffDelay_Type=Unsigned32
_PdhLogPrtDiffDelay_Object=MibTableColumn
pdhLogPrtDiffDelay=_PdhLogPrtDiffDelay_Object((1,3,6,1,4,1,164,3,1,6,16,2,1,1,3),_PdhLogPrtDiffDelay_Type())
pdhLogPrtDiffDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:pdhLogPrtDiffDelay.setStatus(_A)
_VcgLcasMembersStatusTable_Object=MibTable
vcgLcasMembersStatusTable=_VcgLcasMembersStatusTable_Object((1,3,6,1,4,1,164,3,1,6,16,2,2))
if mibBuilder.loadTexts:vcgLcasMembersStatusTable.setStatus(_A)
_VcgLcasMembersStatusEntry_Object=MibTableRow
vcgLcasMembersStatusEntry=_VcgLcasMembersStatusEntry_Object((1,3,6,1,4,1,164,3,1,6,16,2,2,1))
vcgLcasMembersStatusEntry.setIndexNames((0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:vcgLcasMembersStatusEntry.setStatus(_A)
_VcgLcasMembersVcgIndex_Type=Unsigned32
_VcgLcasMembersVcgIndex_Object=MibTableColumn
vcgLcasMembersVcgIndex=_VcgLcasMembersVcgIndex_Object((1,3,6,1,4,1,164,3,1,6,16,2,2,1,1),_VcgLcasMembersVcgIndex_Type())
vcgLcasMembersVcgIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:vcgLcasMembersVcgIndex.setStatus(_A)
_VcgLcasMembersLinkIndex_Type=Unsigned32
_VcgLcasMembersLinkIndex_Object=MibTableColumn
vcgLcasMembersLinkIndex=_VcgLcasMembersLinkIndex_Object((1,3,6,1,4,1,164,3,1,6,16,2,2,1,2),_VcgLcasMembersLinkIndex_Type())
vcgLcasMembersLinkIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:vcgLcasMembersLinkIndex.setStatus(_A)
class _VcgLcasMembersSourceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3),('fixed',4),(_K,5),(_L,6),('eos',7),(_I,8),(_S,9),(_M,10),(_J,11)))
_VcgLcasMembersSourceStatus_Type.__name__=_C
_VcgLcasMembersSourceStatus_Object=MibTableColumn
vcgLcasMembersSourceStatus=_VcgLcasMembersSourceStatus_Object((1,3,6,1,4,1,164,3,1,6,16,2,2,1,3),_VcgLcasMembersSourceStatus_Type())
vcgLcasMembersSourceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLcasMembersSourceStatus.setStatus(_A)
class _VcgLcasMembersSinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3),('fixed',4),(_K,5),(_L,6),('eos',7),(_I,8),(_S,9),(_M,10),(_J,11)))
_VcgLcasMembersSinkStatus_Type.__name__=_C
_VcgLcasMembersSinkStatus_Object=MibTableColumn
vcgLcasMembersSinkStatus=_VcgLcasMembersSinkStatus_Object((1,3,6,1,4,1,164,3,1,6,16,2,2,1,4),_VcgLcasMembersSinkStatus_Type())
vcgLcasMembersSinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLcasMembersSinkStatus.setStatus(_A)
class _VcgLcasMembersLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('noLoop',2),('loop',3)))
_VcgLcasMembersLoopStatus_Type.__name__=_C
_VcgLcasMembersLoopStatus_Object=MibTableColumn
vcgLcasMembersLoopStatus=_VcgLcasMembersLoopStatus_Object((1,3,6,1,4,1,164,3,1,6,16,2,2,1,5),_VcgLcasMembersLoopStatus_Type())
vcgLcasMembersLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLcasMembersLoopStatus.setStatus(_A)
class _VcgLcasMembersTxStateMachineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_I,1),(_K,2),(_L,3),(_M,4),(_T,5),(_J,6)))
_VcgLcasMembersTxStateMachineStatus_Type.__name__=_C
_VcgLcasMembersTxStateMachineStatus_Object=MibTableColumn
vcgLcasMembersTxStateMachineStatus=_VcgLcasMembersTxStateMachineStatus_Object((1,3,6,1,4,1,164,3,1,6,16,2,2,1,6),_VcgLcasMembersTxStateMachineStatus_Type())
vcgLcasMembersTxStateMachineStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLcasMembersTxStateMachineStatus.setStatus(_A)
class _VcgLcasMembersRxStateMachineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),(_G,2),(_H,3),('wtrFail',4),('wtrOk',5),('ho',6),(_T,7),(_J,8)))
_VcgLcasMembersRxStateMachineStatus_Type.__name__=_C
_VcgLcasMembersRxStateMachineStatus_Object=MibTableColumn
vcgLcasMembersRxStateMachineStatus=_VcgLcasMembersRxStateMachineStatus_Object((1,3,6,1,4,1,164,3,1,6,16,2,2,1,7),_VcgLcasMembersRxStateMachineStatus_Type())
vcgLcasMembersRxStateMachineStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLcasMembersRxStateMachineStatus.setStatus(_A)
class _VcgLcasMembersStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_VcgLcasMembersStatus_Type.__name__=_C
_VcgLcasMembersStatus_Object=MibTableColumn
vcgLcasMembersStatus=_VcgLcasMembersStatus_Object((1,3,6,1,4,1,164,3,1,6,16,2,2,1,8),_VcgLcasMembersStatus_Type())
vcgLcasMembersStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLcasMembersStatus.setStatus(_A)
class _VcgLcasMembersSignalUnavailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('no',2),('yes',3)))
_VcgLcasMembersSignalUnavailable_Type.__name__=_C
_VcgLcasMembersSignalUnavailable_Object=MibTableColumn
vcgLcasMembersSignalUnavailable=_VcgLcasMembersSignalUnavailable_Object((1,3,6,1,4,1,164,3,1,6,16,2,2,1,9),_VcgLcasMembersSignalUnavailable_Type())
vcgLcasMembersSignalUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLcasMembersSignalUnavailable.setStatus(_A)
class _VcgLcasMembersTrailSignalDegrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('no',2),('yes',3)))
_VcgLcasMembersTrailSignalDegrade_Type.__name__=_C
_VcgLcasMembersTrailSignalDegrade_Object=MibTableColumn
vcgLcasMembersTrailSignalDegrade=_VcgLcasMembersTrailSignalDegrade_Object((1,3,6,1,4,1,164,3,1,6,16,2,2,1,10),_VcgLcasMembersTrailSignalDegrade_Type())
vcgLcasMembersTrailSignalDegrade.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLcasMembersTrailSignalDegrade.setStatus(_A)
_VcgLcasMembersMfiDiffDelay_Type=Unsigned32
_VcgLcasMembersMfiDiffDelay_Object=MibTableColumn
vcgLcasMembersMfiDiffDelay=_VcgLcasMembersMfiDiffDelay_Object((1,3,6,1,4,1,164,3,1,6,16,2,2,1,11),_VcgLcasMembersMfiDiffDelay_Type())
vcgLcasMembersMfiDiffDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLcasMembersMfiDiffDelay.setStatus(_A)
class _VcgLcasMembersVcLoMF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('off',2),('on',3)))
_VcgLcasMembersVcLoMF_Type.__name__=_C
_VcgLcasMembersVcLoMF_Object=MibTableColumn
vcgLcasMembersVcLoMF=_VcgLcasMembersVcLoMF_Object((1,3,6,1,4,1,164,3,1,6,16,2,2,1,12),_VcgLcasMembersVcLoMF_Type())
vcgLcasMembersVcLoMF.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLcasMembersVcLoMF.setStatus(_A)
_VcgLcasMembersTxSeqNumber_Type=Unsigned32
_VcgLcasMembersTxSeqNumber_Object=MibTableColumn
vcgLcasMembersTxSeqNumber=_VcgLcasMembersTxSeqNumber_Object((1,3,6,1,4,1,164,3,1,6,16,2,2,1,13),_VcgLcasMembersTxSeqNumber_Type())
vcgLcasMembersTxSeqNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLcasMembersTxSeqNumber.setStatus(_A)
_VcgLcasMembersRxSeqNumber_Type=Unsigned32
_VcgLcasMembersRxSeqNumber_Object=MibTableColumn
vcgLcasMembersRxSeqNumber=_VcgLcasMembersRxSeqNumber_Object((1,3,6,1,4,1,164,3,1,6,16,2,2,1,14),_VcgLcasMembersRxSeqNumber_Type())
vcgLcasMembersRxSeqNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:vcgLcasMembersRxSeqNumber.setStatus(_A)
_PdhIfStatis_ObjectIdentity=ObjectIdentity
pdhIfStatis=_PdhIfStatis_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,16,3))
_PdhLogPrtStatisTable_Object=MibTable
pdhLogPrtStatisTable=_PdhLogPrtStatisTable_Object((1,3,6,1,4,1,164,3,1,6,16,3,1))
if mibBuilder.loadTexts:pdhLogPrtStatisTable.setStatus(_A)
_PdhLogPrtStatisEntry_Object=MibTableRow
pdhLogPrtStatisEntry=_PdhLogPrtStatisEntry_Object((1,3,6,1,4,1,164,3,1,6,16,3,1,1))
pdhLogPrtStatisEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:pdhLogPrtStatisEntry.setStatus(_A)
_PdhLogPrtStatisIndex_Type=Unsigned32
_PdhLogPrtStatisIndex_Object=MibTableColumn
pdhLogPrtStatisIndex=_PdhLogPrtStatisIndex_Object((1,3,6,1,4,1,164,3,1,6,16,3,1,1,1),_PdhLogPrtStatisIndex_Type())
pdhLogPrtStatisIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pdhLogPrtStatisIndex.setStatus(_A)
_PdhLogPrtStatisRxCorrFrames_Type=Counter32
_PdhLogPrtStatisRxCorrFrames_Object=MibTableColumn
pdhLogPrtStatisRxCorrFrames=_PdhLogPrtStatisRxCorrFrames_Object((1,3,6,1,4,1,164,3,1,6,16,3,1,1,2),_PdhLogPrtStatisRxCorrFrames_Type())
pdhLogPrtStatisRxCorrFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:pdhLogPrtStatisRxCorrFrames.setStatus(_A)
_PdhLogPrtStatisRxCorrOctets_Type=Counter32
_PdhLogPrtStatisRxCorrOctets_Object=MibTableColumn
pdhLogPrtStatisRxCorrOctets=_PdhLogPrtStatisRxCorrOctets_Object((1,3,6,1,4,1,164,3,1,6,16,3,1,1,3),_PdhLogPrtStatisRxCorrOctets_Type())
pdhLogPrtStatisRxCorrOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pdhLogPrtStatisRxCorrOctets.setStatus(_A)
_PdhLogPrtStatisRxCHecErrors_Type=Counter32
_PdhLogPrtStatisRxCHecErrors_Object=MibTableColumn
pdhLogPrtStatisRxCHecErrors=_PdhLogPrtStatisRxCHecErrors_Object((1,3,6,1,4,1,164,3,1,6,16,3,1,1,4),_PdhLogPrtStatisRxCHecErrors_Type())
pdhLogPrtStatisRxCHecErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:pdhLogPrtStatisRxCHecErrors.setStatus(_A)
_PdhLogPrtStatisRxTHecErrors_Type=Counter32
_PdhLogPrtStatisRxTHecErrors_Object=MibTableColumn
pdhLogPrtStatisRxTHecErrors=_PdhLogPrtStatisRxTHecErrors_Object((1,3,6,1,4,1,164,3,1,6,16,3,1,1,5),_PdhLogPrtStatisRxTHecErrors_Type())
pdhLogPrtStatisRxTHecErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:pdhLogPrtStatisRxTHecErrors.setStatus(_A)
_PdhLogPrtStatisRxFcsErrors_Type=Counter32
_PdhLogPrtStatisRxFcsErrors_Object=MibTableColumn
pdhLogPrtStatisRxFcsErrors=_PdhLogPrtStatisRxFcsErrors_Object((1,3,6,1,4,1,164,3,1,6,16,3,1,1,6),_PdhLogPrtStatisRxFcsErrors_Type())
pdhLogPrtStatisRxFcsErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:pdhLogPrtStatisRxFcsErrors.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'pdhInterface':pdhInterface,'pdhIfConfig':pdhIfConfig,'pdhLogPrtConfigTable':pdhLogPrtConfigTable,'pdhLogPrtConfigEntry':pdhLogPrtConfigEntry,_N:pdhLogPrtCnfgIdx,_O:pdhLogPrtIndex,'pdhLogPrtMaxDiffDelay':pdhLogPrtMaxDiffDelay,'pdhIfStatus':pdhIfStatus,'pdhLogPrtStatusTable':pdhLogPrtStatusTable,'pdhLogPrtStatusEntry':pdhLogPrtStatusEntry,_P:pdhLogPrtStatusIndex,'pdhLogPrtFrameDelineation':pdhLogPrtFrameDelineation,'pdhLogPrtDiffDelay':pdhLogPrtDiffDelay,'vcgLcasMembersStatusTable':vcgLcasMembersStatusTable,'vcgLcasMembersStatusEntry':vcgLcasMembersStatusEntry,_Q:vcgLcasMembersVcgIndex,_R:vcgLcasMembersLinkIndex,'vcgLcasMembersSourceStatus':vcgLcasMembersSourceStatus,'vcgLcasMembersSinkStatus':vcgLcasMembersSinkStatus,'vcgLcasMembersLoopStatus':vcgLcasMembersLoopStatus,'vcgLcasMembersTxStateMachineStatus':vcgLcasMembersTxStateMachineStatus,'vcgLcasMembersRxStateMachineStatus':vcgLcasMembersRxStateMachineStatus,'vcgLcasMembersStatus':vcgLcasMembersStatus,'vcgLcasMembersSignalUnavailable':vcgLcasMembersSignalUnavailable,'vcgLcasMembersTrailSignalDegrade':vcgLcasMembersTrailSignalDegrade,'vcgLcasMembersMfiDiffDelay':vcgLcasMembersMfiDiffDelay,'vcgLcasMembersVcLoMF':vcgLcasMembersVcLoMF,'vcgLcasMembersTxSeqNumber':vcgLcasMembersTxSeqNumber,'vcgLcasMembersRxSeqNumber':vcgLcasMembersRxSeqNumber,'pdhIfStatis':pdhIfStatis,'pdhLogPrtStatisTable':pdhLogPrtStatisTable,'pdhLogPrtStatisEntry':pdhLogPrtStatisEntry,_U:pdhLogPrtStatisIndex,'pdhLogPrtStatisRxCorrFrames':pdhLogPrtStatisRxCorrFrames,'pdhLogPrtStatisRxCorrOctets':pdhLogPrtStatisRxCorrOctets,'pdhLogPrtStatisRxCHecErrors':pdhLogPrtStatisRxCHecErrors,'pdhLogPrtStatisRxTHecErrors':pdhLogPrtStatisRxTHecErrors,'pdhLogPrtStatisRxFcsErrors':pdhLogPrtStatisRxFcsErrors})