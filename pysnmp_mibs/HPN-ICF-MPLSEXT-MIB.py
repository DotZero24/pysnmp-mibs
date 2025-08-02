_J='hpnicfMplsExtLdpIndex'
_I='not-accessible'
_H='hpnicfMplsExtIndex'
_G='read-write'
_F='OctetString'
_E='HPN-ICF-MPLSEXT-MIB'
_D='TruthValue'
_C='Unsigned32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_D)
hpnicfMplsExt=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,142))
if mibBuilder.loadTexts:hpnicfMplsExt.setRevisions(('2013-06-13 18:00',))
_HpnicfMplsExtObjects_ObjectIdentity=ObjectIdentity
hpnicfMplsExtObjects=_HpnicfMplsExtObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,142,1))
_HpnicfMplsExtScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfMplsExtScalarGroup=_HpnicfMplsExtScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,142,1,1))
class _HpnicfMplsExtLsrID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfMplsExtLsrID_Type.__name__=_F
_HpnicfMplsExtLsrID_Object=MibScalar
hpnicfMplsExtLsrID=_HpnicfMplsExtLsrID_Object((1,3,6,1,4,1,11,2,14,11,15,2,142,1,1,1),_HpnicfMplsExtLsrID_Type())
hpnicfMplsExtLsrID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsExtLsrID.setStatus(_A)
_HpnicfMplsExtLdpStatus_Type=TruthValue
_HpnicfMplsExtLdpStatus_Object=MibScalar
hpnicfMplsExtLdpStatus=_HpnicfMplsExtLdpStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,142,1,1,2),_HpnicfMplsExtLdpStatus_Type())
hpnicfMplsExtLdpStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsExtLdpStatus.setStatus(_A)
_HpnicfMplsExtTable_Object=MibTable
hpnicfMplsExtTable=_HpnicfMplsExtTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,142,1,2))
if mibBuilder.loadTexts:hpnicfMplsExtTable.setStatus(_A)
_HpnicfMplsExtEntry_Object=MibTableRow
hpnicfMplsExtEntry=_HpnicfMplsExtEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,142,1,2,1))
hpnicfMplsExtEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:hpnicfMplsExtEntry.setStatus(_A)
class _HpnicfMplsExtIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfMplsExtIndex_Type.__name__=_C
_HpnicfMplsExtIndex_Object=MibTableColumn
hpnicfMplsExtIndex=_HpnicfMplsExtIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,142,1,2,1,1),_HpnicfMplsExtIndex_Type())
hpnicfMplsExtIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfMplsExtIndex.setStatus(_A)
class _HpnicfMplsExtCapability_Type(TruthValue):defaultValue=2
_HpnicfMplsExtCapability_Type.__name__=_D
_HpnicfMplsExtCapability_Object=MibTableColumn
hpnicfMplsExtCapability=_HpnicfMplsExtCapability_Object((1,3,6,1,4,1,11,2,14,11,15,2,142,1,2,1,2),_HpnicfMplsExtCapability_Type())
hpnicfMplsExtCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsExtCapability.setStatus(_A)
class _HpnicfMplsExtMtu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(46,65535))
_HpnicfMplsExtMtu_Type.__name__=_C
_HpnicfMplsExtMtu_Object=MibTableColumn
hpnicfMplsExtMtu=_HpnicfMplsExtMtu_Object((1,3,6,1,4,1,11,2,14,11,15,2,142,1,2,1,3),_HpnicfMplsExtMtu_Type())
hpnicfMplsExtMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsExtMtu.setStatus(_A)
_HpnicfMplsExtRowStatus_Type=RowStatus
_HpnicfMplsExtRowStatus_Object=MibTableColumn
hpnicfMplsExtRowStatus=_HpnicfMplsExtRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,142,1,2,1,4),_HpnicfMplsExtRowStatus_Type())
hpnicfMplsExtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsExtRowStatus.setStatus(_A)
_HpnicfMplsExtLdpTable_Object=MibTable
hpnicfMplsExtLdpTable=_HpnicfMplsExtLdpTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,142,1,3))
if mibBuilder.loadTexts:hpnicfMplsExtLdpTable.setStatus(_A)
_HpnicfMplsExtLdpEntry_Object=MibTableRow
hpnicfMplsExtLdpEntry=_HpnicfMplsExtLdpEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,142,1,3,1))
hpnicfMplsExtLdpEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:hpnicfMplsExtLdpEntry.setStatus(_A)
class _HpnicfMplsExtLdpIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfMplsExtLdpIndex_Type.__name__=_C
_HpnicfMplsExtLdpIndex_Object=MibTableColumn
hpnicfMplsExtLdpIndex=_HpnicfMplsExtLdpIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,142,1,3,1,1),_HpnicfMplsExtLdpIndex_Type())
hpnicfMplsExtLdpIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfMplsExtLdpIndex.setStatus(_A)
class _HpnicfMplsExtLdpCapability_Type(TruthValue):defaultValue=2
_HpnicfMplsExtLdpCapability_Type.__name__=_D
_HpnicfMplsExtLdpCapability_Object=MibTableColumn
hpnicfMplsExtLdpCapability=_HpnicfMplsExtLdpCapability_Object((1,3,6,1,4,1,11,2,14,11,15,2,142,1,3,1,2),_HpnicfMplsExtLdpCapability_Type())
hpnicfMplsExtLdpCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsExtLdpCapability.setStatus(_A)
_HpnicfMplsExtLdpRowStatus_Type=RowStatus
_HpnicfMplsExtLdpRowStatus_Object=MibTableColumn
hpnicfMplsExtLdpRowStatus=_HpnicfMplsExtLdpRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,142,1,3,1,3),_HpnicfMplsExtLdpRowStatus_Type())
hpnicfMplsExtLdpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMplsExtLdpRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hpnicfMplsExt':hpnicfMplsExt,'hpnicfMplsExtObjects':hpnicfMplsExtObjects,'hpnicfMplsExtScalarGroup':hpnicfMplsExtScalarGroup,'hpnicfMplsExtLsrID':hpnicfMplsExtLsrID,'hpnicfMplsExtLdpStatus':hpnicfMplsExtLdpStatus,'hpnicfMplsExtTable':hpnicfMplsExtTable,'hpnicfMplsExtEntry':hpnicfMplsExtEntry,_H:hpnicfMplsExtIndex,'hpnicfMplsExtCapability':hpnicfMplsExtCapability,'hpnicfMplsExtMtu':hpnicfMplsExtMtu,'hpnicfMplsExtRowStatus':hpnicfMplsExtRowStatus,'hpnicfMplsExtLdpTable':hpnicfMplsExtLdpTable,'hpnicfMplsExtLdpEntry':hpnicfMplsExtLdpEntry,_J:hpnicfMplsExtLdpIndex,'hpnicfMplsExtLdpCapability':hpnicfMplsExtLdpCapability,'hpnicfMplsExtLdpRowStatus':hpnicfMplsExtLdpRowStatus})