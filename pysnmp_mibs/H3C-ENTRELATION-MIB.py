#
# PySNMP MIB module H3C-ENTRELATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-ENTRELATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:41 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cEntityRelation = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15))
if mibBuilder.loadTexts: h3cEntityRelation.setLastUpdated('200408190000Z')
if mibBuilder.loadTexts: h3cEntityRelation.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class H3cEntRelationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stackport", 1), ("comboport", 2))

h3cEntRelationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1))
h3cEntRelation = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1))
h3cEntRelationTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1, 1), )
if mibBuilder.loadTexts: h3cEntRelationTable.setStatus('current')
h3cEntRelationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1, 1, 1), ).setIndexNames((0, "H3C-ENTRELATION-MIB", "h3cEntRelationType"), (0, "H3C-ENTRELATION-MIB", "h3cEntityIndex"), (0, "H3C-ENTRELATION-MIB", "h3cRelatedEntityIndex"))
if mibBuilder.loadTexts: h3cEntRelationEntry.setStatus('current')
h3cEntRelationType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1, 1, 1, 1), H3cEntRelationType())
if mibBuilder.loadTexts: h3cEntRelationType.setStatus('current')
h3cEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1, 1, 1, 2), PhysicalIndex())
if mibBuilder.loadTexts: h3cEntityIndex.setStatus('current')
h3cRelatedEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1, 1, 1, 3), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRelatedEntityIndex.setStatus('current')
h3cEntRelationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 2))
h3cEntRelationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 2, 1))
h3cEntRelationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 2, 1, 1)).setObjects(("H3C-ENTRELATION-MIB", "h3cEntRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cEntRelationCompliance = h3cEntRelationCompliance.setStatus('current')
h3cEntRelationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 2, 2))
h3cEntRelationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 2, 2, 1)).setObjects(("H3C-ENTRELATION-MIB", "h3cRelatedEntityIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cEntRelationGroup = h3cEntRelationGroup.setStatus('current')
mibBuilder.exportSymbols("H3C-ENTRELATION-MIB", PYSNMP_MODULE_ID=h3cEntityRelation, h3cEntRelationGroup=h3cEntRelationGroup, h3cEntRelationObjects=h3cEntRelationObjects, h3cEntRelationGroups=h3cEntRelationGroups, h3cEntRelationTable=h3cEntRelationTable, h3cEntRelationCompliance=h3cEntRelationCompliance, h3cEntRelationType=h3cEntRelationType, h3cEntRelationEntry=h3cEntRelationEntry, h3cEntRelation=h3cEntRelation, h3cEntRelationConformance=h3cEntRelationConformance, h3cRelatedEntityIndex=h3cRelatedEntityIndex, H3cEntRelationType=H3cEntRelationType, h3cEntityRelation=h3cEntityRelation, h3cEntityIndex=h3cEntityIndex, h3cEntRelationCompliances=h3cEntRelationCompliances)
