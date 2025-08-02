_H='read-only'
_G='hpnicfSessionStatCPUID'
_F='hpnicfSessionStatSlot'
_E='hpnicfSessionStatChassis'
_D='not-accessible'
_C='HPN-ICF-SESSION-MIB'
_B='Unsigned32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_B,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfSession=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,149))
if mibBuilder.loadTexts:hpnicfSession.setRevisions(('2013-12-20 00:00',))
_HpnicfSessionTables_ObjectIdentity=ObjectIdentity
hpnicfSessionTables=_HpnicfSessionTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,149,1))
_HpnicfSessionStatTable_Object=MibTable
hpnicfSessionStatTable=_HpnicfSessionStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,149,1,1))
if mibBuilder.loadTexts:hpnicfSessionStatTable.setStatus(_A)
_HpnicfSessionStatEntry_Object=MibTableRow
hpnicfSessionStatEntry=_HpnicfSessionStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,149,1,1,1))
hpnicfSessionStatEntry.setIndexNames((0,_C,_E),(0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:hpnicfSessionStatEntry.setStatus(_A)
class _HpnicfSessionStatChassis_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_HpnicfSessionStatChassis_Type.__name__=_B
_HpnicfSessionStatChassis_Object=MibTableColumn
hpnicfSessionStatChassis=_HpnicfSessionStatChassis_Object((1,3,6,1,4,1,11,2,14,11,15,2,149,1,1,1,1),_HpnicfSessionStatChassis_Type())
hpnicfSessionStatChassis.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSessionStatChassis.setStatus(_A)
class _HpnicfSessionStatSlot_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_HpnicfSessionStatSlot_Type.__name__=_B
_HpnicfSessionStatSlot_Object=MibTableColumn
hpnicfSessionStatSlot=_HpnicfSessionStatSlot_Object((1,3,6,1,4,1,11,2,14,11,15,2,149,1,1,1,2),_HpnicfSessionStatSlot_Type())
hpnicfSessionStatSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSessionStatSlot.setStatus(_A)
class _HpnicfSessionStatCPUID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfSessionStatCPUID_Type.__name__=_B
_HpnicfSessionStatCPUID_Object=MibTableColumn
hpnicfSessionStatCPUID=_HpnicfSessionStatCPUID_Object((1,3,6,1,4,1,11,2,14,11,15,2,149,1,1,1,3),_HpnicfSessionStatCPUID_Type())
hpnicfSessionStatCPUID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSessionStatCPUID.setStatus(_A)
_HpnicfSessionStatCount_Type=Unsigned32
_HpnicfSessionStatCount_Object=MibTableColumn
hpnicfSessionStatCount=_HpnicfSessionStatCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,149,1,1,1,4),_HpnicfSessionStatCount_Type())
hpnicfSessionStatCount.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSessionStatCount.setStatus(_A)
_HpnicfSessionStatCreateRate_Type=Unsigned32
_HpnicfSessionStatCreateRate_Object=MibTableColumn
hpnicfSessionStatCreateRate=_HpnicfSessionStatCreateRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,149,1,1,1,5),_HpnicfSessionStatCreateRate_Type())
hpnicfSessionStatCreateRate.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSessionStatCreateRate.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfSession':hpnicfSession,'hpnicfSessionTables':hpnicfSessionTables,'hpnicfSessionStatTable':hpnicfSessionStatTable,'hpnicfSessionStatEntry':hpnicfSessionStatEntry,_E:hpnicfSessionStatChassis,_F:hpnicfSessionStatSlot,_G:hpnicfSessionStatCPUID,'hpnicfSessionStatCount':hpnicfSessionStatCount,'hpnicfSessionStatCreateRate':hpnicfSessionStatCreateRate})