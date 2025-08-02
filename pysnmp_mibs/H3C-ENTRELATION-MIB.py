_G='h3cEntRelationGroup'
_F='not-accessible'
_E='h3cEntityIndex'
_D='h3cEntRelationType'
_C='h3cRelatedEntityIndex'
_B='H3C-ENTRELATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cEntityRelation=ModuleIdentity((1,3,6,1,4,1,2011,10,2,15))
class H3cEntRelationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stackport',1),('comboport',2)))
_H3cEntRelationObjects_ObjectIdentity=ObjectIdentity
h3cEntRelationObjects=_H3cEntRelationObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,15,1))
_H3cEntRelation_ObjectIdentity=ObjectIdentity
h3cEntRelation=_H3cEntRelation_ObjectIdentity((1,3,6,1,4,1,2011,10,2,15,1,1))
_H3cEntRelationTable_Object=MibTable
h3cEntRelationTable=_H3cEntRelationTable_Object((1,3,6,1,4,1,2011,10,2,15,1,1,1))
if mibBuilder.loadTexts:h3cEntRelationTable.setStatus(_A)
_H3cEntRelationEntry_Object=MibTableRow
h3cEntRelationEntry=_H3cEntRelationEntry_Object((1,3,6,1,4,1,2011,10,2,15,1,1,1,1))
h3cEntRelationEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_C))
if mibBuilder.loadTexts:h3cEntRelationEntry.setStatus(_A)
_H3cEntRelationType_Type=H3cEntRelationType
_H3cEntRelationType_Object=MibTableColumn
h3cEntRelationType=_H3cEntRelationType_Object((1,3,6,1,4,1,2011,10,2,15,1,1,1,1,1),_H3cEntRelationType_Type())
h3cEntRelationType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEntRelationType.setStatus(_A)
_H3cEntityIndex_Type=PhysicalIndex
_H3cEntityIndex_Object=MibTableColumn
h3cEntityIndex=_H3cEntityIndex_Object((1,3,6,1,4,1,2011,10,2,15,1,1,1,1,2),_H3cEntityIndex_Type())
h3cEntityIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEntityIndex.setStatus(_A)
_H3cRelatedEntityIndex_Type=PhysicalIndex
_H3cRelatedEntityIndex_Object=MibTableColumn
h3cRelatedEntityIndex=_H3cRelatedEntityIndex_Object((1,3,6,1,4,1,2011,10,2,15,1,1,1,1,3),_H3cRelatedEntityIndex_Type())
h3cRelatedEntityIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cRelatedEntityIndex.setStatus(_A)
_H3cEntRelationConformance_ObjectIdentity=ObjectIdentity
h3cEntRelationConformance=_H3cEntRelationConformance_ObjectIdentity((1,3,6,1,4,1,2011,10,2,15,2))
_H3cEntRelationCompliances_ObjectIdentity=ObjectIdentity
h3cEntRelationCompliances=_H3cEntRelationCompliances_ObjectIdentity((1,3,6,1,4,1,2011,10,2,15,2,1))
_H3cEntRelationGroups_ObjectIdentity=ObjectIdentity
h3cEntRelationGroups=_H3cEntRelationGroups_ObjectIdentity((1,3,6,1,4,1,2011,10,2,15,2,2))
h3cEntRelationGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,15,2,2,1))
h3cEntRelationGroup.setObjects((_B,_C))
if mibBuilder.loadTexts:h3cEntRelationGroup.setStatus(_A)
h3cEntRelationCompliance=ModuleCompliance((1,3,6,1,4,1,2011,10,2,15,2,1,1))
h3cEntRelationCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:h3cEntRelationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'H3cEntRelationType':H3cEntRelationType,'h3cEntityRelation':h3cEntityRelation,'h3cEntRelationObjects':h3cEntRelationObjects,'h3cEntRelation':h3cEntRelation,'h3cEntRelationTable':h3cEntRelationTable,'h3cEntRelationEntry':h3cEntRelationEntry,_D:h3cEntRelationType,_E:h3cEntityIndex,_C:h3cRelatedEntityIndex,'h3cEntRelationConformance':h3cEntRelationConformance,'h3cEntRelationCompliances':h3cEntRelationCompliances,'h3cEntRelationCompliance':h3cEntRelationCompliance,'h3cEntRelationGroups':h3cEntRelationGroups,_G:h3cEntRelationGroup})