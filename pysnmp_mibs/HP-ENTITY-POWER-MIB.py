_J='hpEntPowerGroup'
_I='hpEntPowerCurrentPowerUsage'
_H='hpEntPowerMinPowerUsage'
_G='hpEntPowerMaxPowerUsage'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='Watts'
_C='read-only'
_B='HP-ENTITY-POWER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpEntityPowerMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,71))
if mibBuilder.loadTexts:hpEntityPowerMIB.setRevisions(('2010-04-11 00:00',))
_HpEntPowerObjects_ObjectIdentity=ObjectIdentity
hpEntPowerObjects=_HpEntPowerObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,71,1))
_HpEntPowerTable_Object=MibTable
hpEntPowerTable=_HpEntPowerTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,71,1,1))
if mibBuilder.loadTexts:hpEntPowerTable.setStatus(_A)
_HpEntPowerEntry_Object=MibTableRow
hpEntPowerEntry=_HpEntPowerEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,71,1,1,1))
hpEntPowerEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpEntPowerEntry.setStatus(_A)
_HpEntPowerMaxPowerUsage_Type=Unsigned32
_HpEntPowerMaxPowerUsage_Object=MibTableColumn
hpEntPowerMaxPowerUsage=_HpEntPowerMaxPowerUsage_Object((1,3,6,1,4,1,11,2,14,11,5,1,71,1,1,1,1),_HpEntPowerMaxPowerUsage_Type())
hpEntPowerMaxPowerUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntPowerMaxPowerUsage.setStatus(_A)
if mibBuilder.loadTexts:hpEntPowerMaxPowerUsage.setUnits(_D)
_HpEntPowerMinPowerUsage_Type=Unsigned32
_HpEntPowerMinPowerUsage_Object=MibTableColumn
hpEntPowerMinPowerUsage=_HpEntPowerMinPowerUsage_Object((1,3,6,1,4,1,11,2,14,11,5,1,71,1,1,1,2),_HpEntPowerMinPowerUsage_Type())
hpEntPowerMinPowerUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntPowerMinPowerUsage.setStatus(_A)
if mibBuilder.loadTexts:hpEntPowerMinPowerUsage.setUnits(_D)
_HpEntPowerCurrentPowerUsage_Type=Unsigned32
_HpEntPowerCurrentPowerUsage_Object=MibTableColumn
hpEntPowerCurrentPowerUsage=_HpEntPowerCurrentPowerUsage_Object((1,3,6,1,4,1,11,2,14,11,5,1,71,1,1,1,3),_HpEntPowerCurrentPowerUsage_Type())
hpEntPowerCurrentPowerUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntPowerCurrentPowerUsage.setStatus(_A)
if mibBuilder.loadTexts:hpEntPowerCurrentPowerUsage.setUnits(_D)
_HpEntPowerConformance_ObjectIdentity=ObjectIdentity
hpEntPowerConformance=_HpEntPowerConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,71,2))
_HpEntPowerCompliances_ObjectIdentity=ObjectIdentity
hpEntPowerCompliances=_HpEntPowerCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,71,2,1))
_HpEntPowerGroups_ObjectIdentity=ObjectIdentity
hpEntPowerGroups=_HpEntPowerGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,71,2,2))
hpEntPowerGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,71,2,2,1))
hpEntPowerGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:hpEntPowerGroup.setStatus(_A)
hpEntPowerCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,71,2,1,1))
hpEntPowerCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:hpEntPowerCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpEntityPowerMIB':hpEntityPowerMIB,'hpEntPowerObjects':hpEntPowerObjects,'hpEntPowerTable':hpEntPowerTable,'hpEntPowerEntry':hpEntPowerEntry,_G:hpEntPowerMaxPowerUsage,_H:hpEntPowerMinPowerUsage,_I:hpEntPowerCurrentPowerUsage,'hpEntPowerConformance':hpEntPowerConformance,'hpEntPowerCompliances':hpEntPowerCompliances,'hpEntPowerCompliance':hpEntPowerCompliance,'hpEntPowerGroups':hpEntPowerGroups,_J:hpEntPowerGroup})