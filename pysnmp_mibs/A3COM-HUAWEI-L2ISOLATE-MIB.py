_F='h3cL2IsoLatePermitMAC'
_E='not-accessible'
_D='Integer32'
_C='h3cL2IsolateVLANIndex'
_B='A3COM-HUAWEI-L2ISOLATE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cL2Isolate=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,103))
if mibBuilder.loadTexts:h3cL2Isolate.setRevisions(('2009-05-06 00:00',))
_H3cL2IsolateObject_ObjectIdentity=ObjectIdentity
h3cL2IsolateObject=_H3cL2IsolateObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,103,1))
_H3cL2IsolateEnableTable_Object=MibTable
h3cL2IsolateEnableTable=_H3cL2IsolateEnableTable_Object((1,3,6,1,4,1,43,45,1,10,2,103,1,1))
if mibBuilder.loadTexts:h3cL2IsolateEnableTable.setStatus(_A)
_H3cL2IsolateEnableEntry_Object=MibTableRow
h3cL2IsolateEnableEntry=_H3cL2IsolateEnableEntry_Object((1,3,6,1,4,1,43,45,1,10,2,103,1,1,1))
h3cL2IsolateEnableEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:h3cL2IsolateEnableEntry.setStatus(_A)
class _H3cL2IsolateVLANIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cL2IsolateVLANIndex_Type.__name__=_D
_H3cL2IsolateVLANIndex_Object=MibTableColumn
h3cL2IsolateVLANIndex=_H3cL2IsolateVLANIndex_Object((1,3,6,1,4,1,43,45,1,10,2,103,1,1,1,1),_H3cL2IsolateVLANIndex_Type())
h3cL2IsolateVLANIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cL2IsolateVLANIndex.setStatus(_A)
_H3cL2IsolateEnable_Type=TruthValue
_H3cL2IsolateEnable_Object=MibTableColumn
h3cL2IsolateEnable=_H3cL2IsolateEnable_Object((1,3,6,1,4,1,43,45,1,10,2,103,1,1,1,2),_H3cL2IsolateEnable_Type())
h3cL2IsolateEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cL2IsolateEnable.setStatus(_A)
_H3cL2IsolatePermitMACTable_Object=MibTable
h3cL2IsolatePermitMACTable=_H3cL2IsolatePermitMACTable_Object((1,3,6,1,4,1,43,45,1,10,2,103,1,2))
if mibBuilder.loadTexts:h3cL2IsolatePermitMACTable.setStatus(_A)
_H3cL2IsolatePermitMACEntry_Object=MibTableRow
h3cL2IsolatePermitMACEntry=_H3cL2IsolatePermitMACEntry_Object((1,3,6,1,4,1,43,45,1,10,2,103,1,2,1))
h3cL2IsolatePermitMACEntry.setIndexNames((0,_B,_C),(0,_B,_F))
if mibBuilder.loadTexts:h3cL2IsolatePermitMACEntry.setStatus(_A)
_H3cL2IsoLatePermitMAC_Type=MacAddress
_H3cL2IsoLatePermitMAC_Object=MibTableColumn
h3cL2IsoLatePermitMAC=_H3cL2IsoLatePermitMAC_Object((1,3,6,1,4,1,43,45,1,10,2,103,1,2,1,1),_H3cL2IsoLatePermitMAC_Type())
h3cL2IsoLatePermitMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cL2IsoLatePermitMAC.setStatus(_A)
_H3cL2IsoLatePermitMACRowStatus_Type=RowStatus
_H3cL2IsoLatePermitMACRowStatus_Object=MibTableColumn
h3cL2IsoLatePermitMACRowStatus=_H3cL2IsoLatePermitMACRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,103,1,2,1,2),_H3cL2IsoLatePermitMACRowStatus_Type())
h3cL2IsoLatePermitMACRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:h3cL2IsoLatePermitMACRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cL2Isolate':h3cL2Isolate,'h3cL2IsolateObject':h3cL2IsolateObject,'h3cL2IsolateEnableTable':h3cL2IsolateEnableTable,'h3cL2IsolateEnableEntry':h3cL2IsolateEnableEntry,_C:h3cL2IsolateVLANIndex,'h3cL2IsolateEnable':h3cL2IsolateEnable,'h3cL2IsolatePermitMACTable':h3cL2IsolatePermitMACTable,'h3cL2IsolatePermitMACEntry':h3cL2IsolatePermitMACEntry,_F:h3cL2IsoLatePermitMAC,'h3cL2IsoLatePermitMACRowStatus':h3cL2IsoLatePermitMACRowStatus})