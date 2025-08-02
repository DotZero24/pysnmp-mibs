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
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfGre=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,54))
if mibBuilder.loadTexts:hpnicfGre.setRevisions(('2005-06-04 00:00',))
_HpnicfGreObjects_ObjectIdentity=ObjectIdentity
hpnicfGreObjects=_HpnicfGreObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,54,1))
_HpnicfGreTable_Object=MibTable
hpnicfGreTable=_HpnicfGreTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,54,1,1))
if mibBuilder.loadTexts:hpnicfGreTable.setStatus(_A)
_HpnicfGreEntry_Object=MibTableRow
hpnicfGreEntry=_HpnicfGreEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,54,1,1,1))
hpnicfGreEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfGreEntry.setStatus(_A)
_HpnicfGreKeyValue_Type=Unsigned32
_HpnicfGreKeyValue_Object=MibTableColumn
hpnicfGreKeyValue=_HpnicfGreKeyValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,54,1,1,1,1),_HpnicfGreKeyValue_Type())
hpnicfGreKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfGreKeyValue.setStatus(_A)
class _HpnicfGreKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HpnicfGreKey_Type.__name__=_B
_HpnicfGreKey_Object=MibTableColumn
hpnicfGreKey=_HpnicfGreKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,54,1,1,1,2),_HpnicfGreKey_Type())
hpnicfGreKey.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfGreKey.setStatus(_A)
class _HpnicfGreChecksum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HpnicfGreChecksum_Type.__name__=_B
_HpnicfGreChecksum_Object=MibTableColumn
hpnicfGreChecksum=_HpnicfGreChecksum_Object((1,3,6,1,4,1,11,2,14,11,15,2,54,1,1,1,3),_HpnicfGreChecksum_Type())
hpnicfGreChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfGreChecksum.setStatus(_A)
mibBuilder.exportSymbols('HPN-ICF-GRE-MIB',**{'hpnicfGre':hpnicfGre,'hpnicfGreObjects':hpnicfGreObjects,'hpnicfGreTable':hpnicfGreTable,'hpnicfGreEntry':hpnicfGreEntry,'hpnicfGreKeyValue':hpnicfGreKeyValue,'hpnicfGreKey':hpnicfGreKey,'hpnicfGreChecksum':hpnicfGreChecksum})