_D='hpnicfAAANasIdName'
_C='HPN-ICF-AAA-NASID-MIB'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfAAANasId=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,114))
if mibBuilder.loadTexts:hpnicfAAANasId.setRevisions(('2011-03-09 09:45',))
_HpnicfAAANasIdObjects_ObjectIdentity=ObjectIdentity
hpnicfAAANasIdObjects=_HpnicfAAANasIdObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,114,1))
_HpnicfAAANasIdTable_Object=MibTable
hpnicfAAANasIdTable=_HpnicfAAANasIdTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,114,1,1))
if mibBuilder.loadTexts:hpnicfAAANasIdTable.setStatus(_A)
_HpnicfAAANasIdEntry_Object=MibTableRow
hpnicfAAANasIdEntry=_HpnicfAAANasIdEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,114,1,1,1))
hpnicfAAANasIdEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:hpnicfAAANasIdEntry.setStatus(_A)
class _HpnicfAAANasIdName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfAAANasIdName_Type.__name__=_B
_HpnicfAAANasIdName_Object=MibTableColumn
hpnicfAAANasIdName=_HpnicfAAANasIdName_Object((1,3,6,1,4,1,11,2,14,11,15,2,114,1,1,1,1),_HpnicfAAANasIdName_Type())
hpnicfAAANasIdName.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfAAANasIdName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfAAANasId':hpnicfAAANasId,'hpnicfAAANasIdObjects':hpnicfAAANasIdObjects,'hpnicfAAANasIdTable':hpnicfAAANasIdTable,'hpnicfAAANasIdEntry':hpnicfAAANasIdEntry,_D:hpnicfAAANasIdName})