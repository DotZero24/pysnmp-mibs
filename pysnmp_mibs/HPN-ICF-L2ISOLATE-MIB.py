_F='hpnicfL2IsoLatePermitMAC'
_E='not-accessible'
_D='Integer32'
_C='hpnicfL2IsolateVLANIndex'
_B='HPN-ICF-L2ISOLATE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfL2Isolate=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,103))
if mibBuilder.loadTexts:hpnicfL2Isolate.setRevisions(('2009-05-06 00:00',))
_HpnicfL2IsolateObject_ObjectIdentity=ObjectIdentity
hpnicfL2IsolateObject=_HpnicfL2IsolateObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,103,1))
_HpnicfL2IsolateEnableTable_Object=MibTable
hpnicfL2IsolateEnableTable=_HpnicfL2IsolateEnableTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,103,1,1))
if mibBuilder.loadTexts:hpnicfL2IsolateEnableTable.setStatus(_A)
_HpnicfL2IsolateEnableEntry_Object=MibTableRow
hpnicfL2IsolateEnableEntry=_HpnicfL2IsolateEnableEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,103,1,1,1))
hpnicfL2IsolateEnableEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:hpnicfL2IsolateEnableEntry.setStatus(_A)
class _HpnicfL2IsolateVLANIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfL2IsolateVLANIndex_Type.__name__=_D
_HpnicfL2IsolateVLANIndex_Object=MibTableColumn
hpnicfL2IsolateVLANIndex=_HpnicfL2IsolateVLANIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,103,1,1,1,1),_HpnicfL2IsolateVLANIndex_Type())
hpnicfL2IsolateVLANIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfL2IsolateVLANIndex.setStatus(_A)
_HpnicfL2IsolateEnable_Type=TruthValue
_HpnicfL2IsolateEnable_Object=MibTableColumn
hpnicfL2IsolateEnable=_HpnicfL2IsolateEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,103,1,1,1,2),_HpnicfL2IsolateEnable_Type())
hpnicfL2IsolateEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfL2IsolateEnable.setStatus(_A)
_HpnicfL2IsolatePermitMACTable_Object=MibTable
hpnicfL2IsolatePermitMACTable=_HpnicfL2IsolatePermitMACTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,103,1,2))
if mibBuilder.loadTexts:hpnicfL2IsolatePermitMACTable.setStatus(_A)
_HpnicfL2IsolatePermitMACEntry_Object=MibTableRow
hpnicfL2IsolatePermitMACEntry=_HpnicfL2IsolatePermitMACEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,103,1,2,1))
hpnicfL2IsolatePermitMACEntry.setIndexNames((0,_B,_C),(0,_B,_F))
if mibBuilder.loadTexts:hpnicfL2IsolatePermitMACEntry.setStatus(_A)
_HpnicfL2IsoLatePermitMAC_Type=MacAddress
_HpnicfL2IsoLatePermitMAC_Object=MibTableColumn
hpnicfL2IsoLatePermitMAC=_HpnicfL2IsoLatePermitMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,103,1,2,1,1),_HpnicfL2IsoLatePermitMAC_Type())
hpnicfL2IsoLatePermitMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfL2IsoLatePermitMAC.setStatus(_A)
_HpnicfL2IsoLatePermitMACRowStatus_Type=RowStatus
_HpnicfL2IsoLatePermitMACRowStatus_Object=MibTableColumn
hpnicfL2IsoLatePermitMACRowStatus=_HpnicfL2IsoLatePermitMACRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,103,1,2,1,2),_HpnicfL2IsoLatePermitMACRowStatus_Type())
hpnicfL2IsoLatePermitMACRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hpnicfL2IsoLatePermitMACRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfL2Isolate':hpnicfL2Isolate,'hpnicfL2IsolateObject':hpnicfL2IsolateObject,'hpnicfL2IsolateEnableTable':hpnicfL2IsolateEnableTable,'hpnicfL2IsolateEnableEntry':hpnicfL2IsolateEnableEntry,_C:hpnicfL2IsolateVLANIndex,'hpnicfL2IsolateEnable':hpnicfL2IsolateEnable,'hpnicfL2IsolatePermitMACTable':hpnicfL2IsolatePermitMACTable,'hpnicfL2IsolatePermitMACEntry':hpnicfL2IsolatePermitMACEntry,_F:hpnicfL2IsoLatePermitMAC,'hpnicfL2IsoLatePermitMACRowStatus':hpnicfL2IsoLatePermitMACRowStatus})