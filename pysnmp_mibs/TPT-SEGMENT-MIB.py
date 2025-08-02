_E='segmentIndex'
_D='slotIndex'
_C='TPT-SEGMENT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_tpa_objs,=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-objs')
tpt_segment_objs=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,19))
if mibBuilder.loadTexts:tpt_segment_objs.setRevisions(('2016-05-25 18:54',))
class SegmentSflowStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('disable',0),('enable',1),('error',2),('not-applicable',3)))
_SegmentTable_Object=MibTable
segmentTable=_SegmentTable_Object((1,3,6,1,4,1,10734,3,3,2,19,1))
if mibBuilder.loadTexts:segmentTable.setStatus(_A)
_SegmentEntry_Object=MibTableRow
segmentEntry=_SegmentEntry_Object((1,3,6,1,4,1,10734,3,3,2,19,1,1))
segmentEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:segmentEntry.setStatus(_A)
_SlotIndex_Type=Unsigned32
_SlotIndex_Object=MibTableColumn
slotIndex=_SlotIndex_Object((1,3,6,1,4,1,10734,3,3,2,19,1,1,1),_SlotIndex_Type())
slotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slotIndex.setStatus(_A)
_SegmentIndex_Type=Unsigned32
_SegmentIndex_Object=MibTableColumn
segmentIndex=_SegmentIndex_Object((1,3,6,1,4,1,10734,3,3,2,19,1,1,2),_SegmentIndex_Type())
segmentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:segmentIndex.setStatus(_A)
_SegmentSflowStatus_Type=SegmentSflowStatus
_SegmentSflowStatus_Object=MibTableColumn
segmentSflowStatus=_SegmentSflowStatus_Object((1,3,6,1,4,1,10734,3,3,2,19,1,1,3),_SegmentSflowStatus_Type())
segmentSflowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:segmentSflowStatus.setStatus(_A)
_SFlowDivisor_Type=Unsigned32
_SFlowDivisor_Object=MibTableColumn
sFlowDivisor=_SFlowDivisor_Object((1,3,6,1,4,1,10734,3,3,2,19,1,1,4),_SFlowDivisor_Type())
sFlowDivisor.setMaxAccess(_B)
if mibBuilder.loadTexts:sFlowDivisor.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'SegmentSflowStatus':SegmentSflowStatus,'tpt-segment-objs':tpt_segment_objs,'segmentTable':segmentTable,'segmentEntry':segmentEntry,_D:slotIndex,_E:segmentIndex,'segmentSflowStatus':segmentSflowStatus,'sFlowDivisor':sFlowDivisor})