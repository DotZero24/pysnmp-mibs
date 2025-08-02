_D='h3cAAANasIdName'
_C='A3COM-HUAWEI-AAA-NASID-MIB'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cAAANasId=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,114))
if mibBuilder.loadTexts:h3cAAANasId.setRevisions(('2011-03-09 09:45',))
_H3cAAANasIdObjects_ObjectIdentity=ObjectIdentity
h3cAAANasIdObjects=_H3cAAANasIdObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,114,1))
_H3cAAANasIdTable_Object=MibTable
h3cAAANasIdTable=_H3cAAANasIdTable_Object((1,3,6,1,4,1,43,45,1,10,2,114,1,1))
if mibBuilder.loadTexts:h3cAAANasIdTable.setStatus(_A)
_H3cAAANasIdEntry_Object=MibTableRow
h3cAAANasIdEntry=_H3cAAANasIdEntry_Object((1,3,6,1,4,1,43,45,1,10,2,114,1,1,1))
h3cAAANasIdEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:h3cAAANasIdEntry.setStatus(_A)
class _H3cAAANasIdName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cAAANasIdName_Type.__name__=_B
_H3cAAANasIdName_Object=MibTableColumn
h3cAAANasIdName=_H3cAAANasIdName_Object((1,3,6,1,4,1,43,45,1,10,2,114,1,1,1,1),_H3cAAANasIdName_Type())
h3cAAANasIdName.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cAAANasIdName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cAAANasId':h3cAAANasId,'h3cAAANasIdObjects':h3cAAANasIdObjects,'h3cAAANasIdTable':h3cAAANasIdTable,'h3cAAANasIdEntry':h3cAAANasIdEntry,_D:h3cAAANasIdName})