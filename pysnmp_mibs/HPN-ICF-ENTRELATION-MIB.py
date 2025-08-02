_G='hpnicfEntRelationGroup'
_F='not-accessible'
_E='hpnicfEntityIndex'
_D='hpnicfEntRelationType'
_C='hpnicfRelatedEntityIndex'
_B='HPN-ICF-ENTRELATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfEntityRelation=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,15))
class HpnicfEntRelationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stackport',1),('comboport',2)))
_HpnicfEntRelationObjects_ObjectIdentity=ObjectIdentity
hpnicfEntRelationObjects=_HpnicfEntRelationObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,15,1))
_HpnicfEntRelation_ObjectIdentity=ObjectIdentity
hpnicfEntRelation=_HpnicfEntRelation_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,15,1,1))
_HpnicfEntRelationTable_Object=MibTable
hpnicfEntRelationTable=_HpnicfEntRelationTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,15,1,1,1))
if mibBuilder.loadTexts:hpnicfEntRelationTable.setStatus(_A)
_HpnicfEntRelationEntry_Object=MibTableRow
hpnicfEntRelationEntry=_HpnicfEntRelationEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,15,1,1,1,1))
hpnicfEntRelationEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_C))
if mibBuilder.loadTexts:hpnicfEntRelationEntry.setStatus(_A)
_HpnicfEntRelationType_Type=HpnicfEntRelationType
_HpnicfEntRelationType_Object=MibTableColumn
hpnicfEntRelationType=_HpnicfEntRelationType_Object((1,3,6,1,4,1,11,2,14,11,15,2,15,1,1,1,1,1),_HpnicfEntRelationType_Type())
hpnicfEntRelationType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfEntRelationType.setStatus(_A)
_HpnicfEntityIndex_Type=PhysicalIndex
_HpnicfEntityIndex_Object=MibTableColumn
hpnicfEntityIndex=_HpnicfEntityIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,15,1,1,1,1,2),_HpnicfEntityIndex_Type())
hpnicfEntityIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfEntityIndex.setStatus(_A)
_HpnicfRelatedEntityIndex_Type=PhysicalIndex
_HpnicfRelatedEntityIndex_Object=MibTableColumn
hpnicfRelatedEntityIndex=_HpnicfRelatedEntityIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,15,1,1,1,1,3),_HpnicfRelatedEntityIndex_Type())
hpnicfRelatedEntityIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfRelatedEntityIndex.setStatus(_A)
_HpnicfEntRelationConformance_ObjectIdentity=ObjectIdentity
hpnicfEntRelationConformance=_HpnicfEntRelationConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,15,2))
_HpnicfEntRelationCompliances_ObjectIdentity=ObjectIdentity
hpnicfEntRelationCompliances=_HpnicfEntRelationCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,15,2,1))
_HpnicfEntRelationGroups_ObjectIdentity=ObjectIdentity
hpnicfEntRelationGroups=_HpnicfEntRelationGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,15,2,2))
hpnicfEntRelationGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,15,2,2,1))
hpnicfEntRelationGroup.setObjects((_B,_C))
if mibBuilder.loadTexts:hpnicfEntRelationGroup.setStatus(_A)
hpnicfEntRelationCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,15,2,1,1))
hpnicfEntRelationCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:hpnicfEntRelationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HpnicfEntRelationType':HpnicfEntRelationType,'hpnicfEntityRelation':hpnicfEntityRelation,'hpnicfEntRelationObjects':hpnicfEntRelationObjects,'hpnicfEntRelation':hpnicfEntRelation,'hpnicfEntRelationTable':hpnicfEntRelationTable,'hpnicfEntRelationEntry':hpnicfEntRelationEntry,_D:hpnicfEntRelationType,_E:hpnicfEntityIndex,_C:hpnicfRelatedEntityIndex,'hpnicfEntRelationConformance':hpnicfEntRelationConformance,'hpnicfEntRelationCompliances':hpnicfEntRelationCompliances,'hpnicfEntRelationCompliance':hpnicfEntRelationCompliance,'hpnicfEntRelationGroups':hpnicfEntRelationGroups,_G:hpnicfEntRelationGroup})