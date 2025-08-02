_G='disable'
_F='enable'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cGre=ModuleIdentity((1,3,6,1,4,1,2011,10,2,54))
if mibBuilder.loadTexts:h3cGre.setRevisions(('2005-06-04 00:00',))
_H3cGreObjects_ObjectIdentity=ObjectIdentity
h3cGreObjects=_H3cGreObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,54,1))
_H3cGreTable_Object=MibTable
h3cGreTable=_H3cGreTable_Object((1,3,6,1,4,1,2011,10,2,54,1,1))
if mibBuilder.loadTexts:h3cGreTable.setStatus(_A)
_H3cGreEntry_Object=MibTableRow
h3cGreEntry=_H3cGreEntry_Object((1,3,6,1,4,1,2011,10,2,54,1,1,1))
h3cGreEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cGreEntry.setStatus(_A)
_H3cGreKeyValue_Type=Unsigned32
_H3cGreKeyValue_Object=MibTableColumn
h3cGreKeyValue=_H3cGreKeyValue_Object((1,3,6,1,4,1,2011,10,2,54,1,1,1,1),_H3cGreKeyValue_Type())
h3cGreKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cGreKeyValue.setStatus(_A)
class _H3cGreKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_H3cGreKey_Type.__name__=_B
_H3cGreKey_Object=MibTableColumn
h3cGreKey=_H3cGreKey_Object((1,3,6,1,4,1,2011,10,2,54,1,1,1,2),_H3cGreKey_Type())
h3cGreKey.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cGreKey.setStatus(_A)
class _H3cGreChecksum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_H3cGreChecksum_Type.__name__=_B
_H3cGreChecksum_Object=MibTableColumn
h3cGreChecksum=_H3cGreChecksum_Object((1,3,6,1,4,1,2011,10,2,54,1,1,1,3),_H3cGreChecksum_Type())
h3cGreChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cGreChecksum.setStatus(_A)
mibBuilder.exportSymbols('H3C-GRE-MIB',**{'h3cGre':h3cGre,'h3cGreObjects':h3cGreObjects,'h3cGreTable':h3cGreTable,'h3cGreEntry':h3cGreEntry,'h3cGreKeyValue':h3cGreKeyValue,'h3cGreKey':h3cGreKey,'h3cGreChecksum':h3cGreChecksum})