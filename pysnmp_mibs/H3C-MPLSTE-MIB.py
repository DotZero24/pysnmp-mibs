_I='h3cMplsTeRsvpIndex'
_H='not-accessible'
_G='h3cMplsTeIndex'
_F='read-write'
_E='H3C-MPLSTE-MIB'
_D='TruthValue'
_C='Unsigned32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_D)
h3cMplsTe=ModuleIdentity((1,3,6,1,4,1,2011,10,2,143))
if mibBuilder.loadTexts:h3cMplsTe.setRevisions(('2013-06-13 18:00',))
_H3cMplsTeObjects_ObjectIdentity=ObjectIdentity
h3cMplsTeObjects=_H3cMplsTeObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,143,1))
_H3cMplsTeScalarGroup_ObjectIdentity=ObjectIdentity
h3cMplsTeScalarGroup=_H3cMplsTeScalarGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,143,1,1))
_H3cMplsTeStatus_Type=TruthValue
_H3cMplsTeStatus_Object=MibScalar
h3cMplsTeStatus=_H3cMplsTeStatus_Object((1,3,6,1,4,1,2011,10,2,143,1,1,1),_H3cMplsTeStatus_Type())
h3cMplsTeStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cMplsTeStatus.setStatus(_A)
_H3cMplsTeRsvpStatus_Type=TruthValue
_H3cMplsTeRsvpStatus_Object=MibScalar
h3cMplsTeRsvpStatus=_H3cMplsTeRsvpStatus_Object((1,3,6,1,4,1,2011,10,2,143,1,1,2),_H3cMplsTeRsvpStatus_Type())
h3cMplsTeRsvpStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cMplsTeRsvpStatus.setStatus(_A)
_H3cMplsTeTable_Object=MibTable
h3cMplsTeTable=_H3cMplsTeTable_Object((1,3,6,1,4,1,2011,10,2,143,1,2))
if mibBuilder.loadTexts:h3cMplsTeTable.setStatus(_A)
_H3cMplsTeEntry_Object=MibTableRow
h3cMplsTeEntry=_H3cMplsTeEntry_Object((1,3,6,1,4,1,2011,10,2,143,1,2,1))
h3cMplsTeEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:h3cMplsTeEntry.setStatus(_A)
class _H3cMplsTeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cMplsTeIndex_Type.__name__=_C
_H3cMplsTeIndex_Object=MibTableColumn
h3cMplsTeIndex=_H3cMplsTeIndex_Object((1,3,6,1,4,1,2011,10,2,143,1,2,1,1),_H3cMplsTeIndex_Type())
h3cMplsTeIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cMplsTeIndex.setStatus(_A)
class _H3cMplsTeCapability_Type(TruthValue):defaultValue=2
_H3cMplsTeCapability_Type.__name__=_D
_H3cMplsTeCapability_Object=MibTableColumn
h3cMplsTeCapability=_H3cMplsTeCapability_Object((1,3,6,1,4,1,2011,10,2,143,1,2,1,2),_H3cMplsTeCapability_Type())
h3cMplsTeCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsTeCapability.setStatus(_A)
_H3cMplsTeRowStatus_Type=RowStatus
_H3cMplsTeRowStatus_Object=MibTableColumn
h3cMplsTeRowStatus=_H3cMplsTeRowStatus_Object((1,3,6,1,4,1,2011,10,2,143,1,2,1,3),_H3cMplsTeRowStatus_Type())
h3cMplsTeRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsTeRowStatus.setStatus(_A)
_H3cMplsTeRsvpTable_Object=MibTable
h3cMplsTeRsvpTable=_H3cMplsTeRsvpTable_Object((1,3,6,1,4,1,2011,10,2,143,1,3))
if mibBuilder.loadTexts:h3cMplsTeRsvpTable.setStatus(_A)
_H3cMplsTeRsvpEntry_Object=MibTableRow
h3cMplsTeRsvpEntry=_H3cMplsTeRsvpEntry_Object((1,3,6,1,4,1,2011,10,2,143,1,3,1))
h3cMplsTeRsvpEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:h3cMplsTeRsvpEntry.setStatus(_A)
class _H3cMplsTeRsvpIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cMplsTeRsvpIndex_Type.__name__=_C
_H3cMplsTeRsvpIndex_Object=MibTableColumn
h3cMplsTeRsvpIndex=_H3cMplsTeRsvpIndex_Object((1,3,6,1,4,1,2011,10,2,143,1,3,1,1),_H3cMplsTeRsvpIndex_Type())
h3cMplsTeRsvpIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cMplsTeRsvpIndex.setStatus(_A)
class _H3cMplsTeRsvpCapability_Type(TruthValue):defaultValue=2
_H3cMplsTeRsvpCapability_Type.__name__=_D
_H3cMplsTeRsvpCapability_Object=MibTableColumn
h3cMplsTeRsvpCapability=_H3cMplsTeRsvpCapability_Object((1,3,6,1,4,1,2011,10,2,143,1,3,1,2),_H3cMplsTeRsvpCapability_Type())
h3cMplsTeRsvpCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsTeRsvpCapability.setStatus(_A)
_H3cMplsTeRsvpRowStatus_Type=RowStatus
_H3cMplsTeRsvpRowStatus_Object=MibTableColumn
h3cMplsTeRsvpRowStatus=_H3cMplsTeRsvpRowStatus_Object((1,3,6,1,4,1,2011,10,2,143,1,3,1,3),_H3cMplsTeRsvpRowStatus_Type())
h3cMplsTeRsvpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsTeRsvpRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'h3cMplsTe':h3cMplsTe,'h3cMplsTeObjects':h3cMplsTeObjects,'h3cMplsTeScalarGroup':h3cMplsTeScalarGroup,'h3cMplsTeStatus':h3cMplsTeStatus,'h3cMplsTeRsvpStatus':h3cMplsTeRsvpStatus,'h3cMplsTeTable':h3cMplsTeTable,'h3cMplsTeEntry':h3cMplsTeEntry,_G:h3cMplsTeIndex,'h3cMplsTeCapability':h3cMplsTeCapability,'h3cMplsTeRowStatus':h3cMplsTeRowStatus,'h3cMplsTeRsvpTable':h3cMplsTeRsvpTable,'h3cMplsTeRsvpEntry':h3cMplsTeRsvpEntry,_I:h3cMplsTeRsvpIndex,'h3cMplsTeRsvpCapability':h3cMplsTeRsvpCapability,'h3cMplsTeRsvpRowStatus':h3cMplsTeRsvpRowStatus})