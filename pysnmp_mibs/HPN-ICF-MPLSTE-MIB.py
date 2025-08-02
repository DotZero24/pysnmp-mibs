_I='hpnicfMplsTeRsvpIndex'
_H='not-accessible'
_G='hpnicfMplsTeIndex'
_F='read-write'
_E='HPN-ICF-MPLSTE-MIB'
_D='TruthValue'
_C='Unsigned32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_D)
hpnicfMplsTe=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,143))
if mibBuilder.loadTexts:hpnicfMplsTe.setRevisions(('2013-06-13 18:00',))
_HpnicfMplsTeObjects_ObjectIdentity=ObjectIdentity
hpnicfMplsTeObjects=_HpnicfMplsTeObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,143,1))
_HpnicfMplsTeScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfMplsTeScalarGroup=_HpnicfMplsTeScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,143,1,1))
_HpnicfMplsTeStatus_Type=TruthValue
_HpnicfMplsTeStatus_Object=MibScalar
hpnicfMplsTeStatus=_HpnicfMplsTeStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,143,1,1,1),_HpnicfMplsTeStatus_Type())
hpnicfMplsTeStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsTeStatus.setStatus(_A)
_HpnicfMplsTeRsvpStatus_Type=TruthValue
_HpnicfMplsTeRsvpStatus_Object=MibScalar
hpnicfMplsTeRsvpStatus=_HpnicfMplsTeRsvpStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,143,1,1,2),_HpnicfMplsTeRsvpStatus_Type())
hpnicfMplsTeRsvpStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsTeRsvpStatus.setStatus(_A)
_HpnicfMplsTeTable_Object=MibTable
hpnicfMplsTeTable=_HpnicfMplsTeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,143,1,2))
if mibBuilder.loadTexts:hpnicfMplsTeTable.setStatus(_A)
_HpnicfMplsTeEntry_Object=MibTableRow
hpnicfMplsTeEntry=_HpnicfMplsTeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,143,1,2,1))
hpnicfMplsTeEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:hpnicfMplsTeEntry.setStatus(_A)
class _HpnicfMplsTeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfMplsTeIndex_Type.__name__=_C
_HpnicfMplsTeIndex_Object=MibTableColumn
hpnicfMplsTeIndex=_HpnicfMplsTeIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,143,1,2,1,1),_HpnicfMplsTeIndex_Type())
hpnicfMplsTeIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfMplsTeIndex.setStatus(_A)
class _HpnicfMplsTeCapability_Type(TruthValue):defaultValue=2
_HpnicfMplsTeCapability_Type.__name__=_D
_HpnicfMplsTeCapability_Object=MibTableColumn
hpnicfMplsTeCapability=_HpnicfMplsTeCapability_Object((1,3,6,1,4,1,11,2,14,11,15,2,143,1,2,1,2),_HpnicfMplsTeCapability_Type())
hpnicfMplsTeCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsTeCapability.setStatus(_A)
_HpnicfMplsTeRowStatus_Type=RowStatus
_HpnicfMplsTeRowStatus_Object=MibTableColumn
hpnicfMplsTeRowStatus=_HpnicfMplsTeRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,143,1,2,1,3),_HpnicfMplsTeRowStatus_Type())
hpnicfMplsTeRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsTeRowStatus.setStatus(_A)
_HpnicfMplsTeRsvpTable_Object=MibTable
hpnicfMplsTeRsvpTable=_HpnicfMplsTeRsvpTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,143,1,3))
if mibBuilder.loadTexts:hpnicfMplsTeRsvpTable.setStatus(_A)
_HpnicfMplsTeRsvpEntry_Object=MibTableRow
hpnicfMplsTeRsvpEntry=_HpnicfMplsTeRsvpEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,143,1,3,1))
hpnicfMplsTeRsvpEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:hpnicfMplsTeRsvpEntry.setStatus(_A)
class _HpnicfMplsTeRsvpIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfMplsTeRsvpIndex_Type.__name__=_C
_HpnicfMplsTeRsvpIndex_Object=MibTableColumn
hpnicfMplsTeRsvpIndex=_HpnicfMplsTeRsvpIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,143,1,3,1,1),_HpnicfMplsTeRsvpIndex_Type())
hpnicfMplsTeRsvpIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfMplsTeRsvpIndex.setStatus(_A)
class _HpnicfMplsTeRsvpCapability_Type(TruthValue):defaultValue=2
_HpnicfMplsTeRsvpCapability_Type.__name__=_D
_HpnicfMplsTeRsvpCapability_Object=MibTableColumn
hpnicfMplsTeRsvpCapability=_HpnicfMplsTeRsvpCapability_Object((1,3,6,1,4,1,11,2,14,11,15,2,143,1,3,1,2),_HpnicfMplsTeRsvpCapability_Type())
hpnicfMplsTeRsvpCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsTeRsvpCapability.setStatus(_A)
_HpnicfMplsTeRsvpRowStatus_Type=RowStatus
_HpnicfMplsTeRsvpRowStatus_Object=MibTableColumn
hpnicfMplsTeRsvpRowStatus=_HpnicfMplsTeRsvpRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,143,1,3,1,3),_HpnicfMplsTeRsvpRowStatus_Type())
hpnicfMplsTeRsvpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsTeRsvpRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hpnicfMplsTe':hpnicfMplsTe,'hpnicfMplsTeObjects':hpnicfMplsTeObjects,'hpnicfMplsTeScalarGroup':hpnicfMplsTeScalarGroup,'hpnicfMplsTeStatus':hpnicfMplsTeStatus,'hpnicfMplsTeRsvpStatus':hpnicfMplsTeRsvpStatus,'hpnicfMplsTeTable':hpnicfMplsTeTable,'hpnicfMplsTeEntry':hpnicfMplsTeEntry,_G:hpnicfMplsTeIndex,'hpnicfMplsTeCapability':hpnicfMplsTeCapability,'hpnicfMplsTeRowStatus':hpnicfMplsTeRowStatus,'hpnicfMplsTeRsvpTable':hpnicfMplsTeRsvpTable,'hpnicfMplsTeRsvpEntry':hpnicfMplsTeRsvpEntry,_I:hpnicfMplsTeRsvpIndex,'hpnicfMplsTeRsvpCapability':hpnicfMplsTeRsvpCapability,'hpnicfMplsTeRsvpRowStatus':hpnicfMplsTeRsvpRowStatus})