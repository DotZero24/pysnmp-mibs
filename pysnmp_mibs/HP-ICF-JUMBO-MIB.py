_H='hpicfJumboStatsGroup'
_G='hpJumboStatsPkts4096to9216Octets'
_F='hpJumboStatsPkts2048to4095Octets'
_E='hpJumboStatsPkts1523to2047Octets'
_D='hpJumboStatsIndex'
_C='read-only'
_B='HP-ICF-JUMBO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpicfObjectModules,=mibBuilder.importSymbols('HP-ICF-OID','hpicfObjectModules')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpicfJumboMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,10,2,13))
if mibBuilder.loadTexts:hpicfJumboMIB.setRevisions(('2004-08-22 10:30',))
_HpicfJumboObjects_ObjectIdentity=ObjectIdentity
hpicfJumboObjects=_HpicfJumboObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,13,1))
_HpJumboStats_ObjectIdentity=ObjectIdentity
hpJumboStats=_HpJumboStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,13,1,1))
_HpJumboStatsTable_Object=MibTable
hpJumboStatsTable=_HpJumboStatsTable_Object((1,3,6,1,4,1,11,2,14,10,2,13,1,1,1))
if mibBuilder.loadTexts:hpJumboStatsTable.setStatus(_A)
_HpJumboStatsEntry_Object=MibTableRow
hpJumboStatsEntry=_HpJumboStatsEntry_Object((1,3,6,1,4,1,11,2,14,10,2,13,1,1,1,1))
hpJumboStatsEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:hpJumboStatsEntry.setStatus(_A)
_HpJumboStatsIndex_Type=InterfaceIndex
_HpJumboStatsIndex_Object=MibTableColumn
hpJumboStatsIndex=_HpJumboStatsIndex_Object((1,3,6,1,4,1,11,2,14,10,2,13,1,1,1,1,1),_HpJumboStatsIndex_Type())
hpJumboStatsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpJumboStatsIndex.setStatus(_A)
_HpJumboStatsPkts1523to2047Octets_Type=Counter32
_HpJumboStatsPkts1523to2047Octets_Object=MibTableColumn
hpJumboStatsPkts1523to2047Octets=_HpJumboStatsPkts1523to2047Octets_Object((1,3,6,1,4,1,11,2,14,10,2,13,1,1,1,1,2),_HpJumboStatsPkts1523to2047Octets_Type())
hpJumboStatsPkts1523to2047Octets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpJumboStatsPkts1523to2047Octets.setStatus(_A)
_HpJumboStatsPkts2048to4095Octets_Type=Counter32
_HpJumboStatsPkts2048to4095Octets_Object=MibTableColumn
hpJumboStatsPkts2048to4095Octets=_HpJumboStatsPkts2048to4095Octets_Object((1,3,6,1,4,1,11,2,14,10,2,13,1,1,1,1,3),_HpJumboStatsPkts2048to4095Octets_Type())
hpJumboStatsPkts2048to4095Octets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpJumboStatsPkts2048to4095Octets.setStatus(_A)
_HpJumboStatsPkts4096to9216Octets_Type=Counter32
_HpJumboStatsPkts4096to9216Octets_Object=MibTableColumn
hpJumboStatsPkts4096to9216Octets=_HpJumboStatsPkts4096to9216Octets_Object((1,3,6,1,4,1,11,2,14,10,2,13,1,1,1,1,4),_HpJumboStatsPkts4096to9216Octets_Type())
hpJumboStatsPkts4096to9216Octets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpJumboStatsPkts4096to9216Octets.setStatus(_A)
_HpicfJumboConformance_ObjectIdentity=ObjectIdentity
hpicfJumboConformance=_HpicfJumboConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,13,2))
_HpicfJumboGroups_ObjectIdentity=ObjectIdentity
hpicfJumboGroups=_HpicfJumboGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,13,2,1))
_HpicfJumboCompliances_ObjectIdentity=ObjectIdentity
hpicfJumboCompliances=_HpicfJumboCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,13,2,2))
hpicfJumboStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,13,2,1,1))
hpicfJumboStatsGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:hpicfJumboStatsGroup.setStatus(_A)
hpicfJumboCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,10,2,13,2,2,1))
hpicfJumboCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:hpicfJumboCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfJumboMIB':hpicfJumboMIB,'hpicfJumboObjects':hpicfJumboObjects,'hpJumboStats':hpJumboStats,'hpJumboStatsTable':hpJumboStatsTable,'hpJumboStatsEntry':hpJumboStatsEntry,_D:hpJumboStatsIndex,_E:hpJumboStatsPkts1523to2047Octets,_F:hpJumboStatsPkts2048to4095Octets,_G:hpJumboStatsPkts4096to9216Octets,'hpicfJumboConformance':hpicfJumboConformance,'hpicfJumboGroups':hpicfJumboGroups,_H:hpicfJumboStatsGroup,'hpicfJumboCompliances':hpicfJumboCompliances,'hpicfJumboCompliance':hpicfJumboCompliance})