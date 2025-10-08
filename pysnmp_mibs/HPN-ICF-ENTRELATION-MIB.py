#
# PySNMP MIB module HPN-ICF-ENTRELATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-ENTRELATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfEntityRelation = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15))
if mibBuilder.loadTexts: hpnicfEntityRelation.setLastUpdated('200408190000Z')
if mibBuilder.loadTexts: hpnicfEntityRelation.setOrganization('')
class HpnicfEntRelationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stackport", 1), ("comboport", 2))

hpnicfEntRelationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1))
hpnicfEntRelation = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1))
hpnicfEntRelationTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1), )
if mibBuilder.loadTexts: hpnicfEntRelationTable.setStatus('current')
hpnicfEntRelationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-ENTRELATION-MIB", "hpnicfEntRelationType"), (0, "HPN-ICF-ENTRELATION-MIB", "hpnicfEntityIndex"), (0, "HPN-ICF-ENTRELATION-MIB", "hpnicfRelatedEntityIndex"))
if mibBuilder.loadTexts: hpnicfEntRelationEntry.setStatus('current')
hpnicfEntRelationType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1, 1), HpnicfEntRelationType())
if mibBuilder.loadTexts: hpnicfEntRelationType.setStatus('current')
hpnicfEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1, 2), PhysicalIndex())
if mibBuilder.loadTexts: hpnicfEntityIndex.setStatus('current')
hpnicfRelatedEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1, 3), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRelatedEntityIndex.setStatus('current')
hpnicfEntRelationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2))
hpnicfEntRelationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 1))
hpnicfEntRelationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 1, 1)).setObjects(("HPN-ICF-ENTRELATION-MIB", "hpnicfEntRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfEntRelationCompliance = hpnicfEntRelationCompliance.setStatus('current')
hpnicfEntRelationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 2))
hpnicfEntRelationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 2, 1)).setObjects(("HPN-ICF-ENTRELATION-MIB", "hpnicfRelatedEntityIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfEntRelationGroup = hpnicfEntRelationGroup.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-ENTRELATION-MIB", hpnicfEntityIndex=hpnicfEntityIndex, hpnicfEntRelationConformance=hpnicfEntRelationConformance, hpnicfEntRelationGroups=hpnicfEntRelationGroups, hpnicfRelatedEntityIndex=hpnicfRelatedEntityIndex, hpnicfEntRelationType=hpnicfEntRelationType, hpnicfEntRelationTable=hpnicfEntRelationTable, hpnicfEntRelationObjects=hpnicfEntRelationObjects, hpnicfEntityRelation=hpnicfEntityRelation, hpnicfEntRelationEntry=hpnicfEntRelationEntry, hpnicfEntRelationCompliances=hpnicfEntRelationCompliances, hpnicfEntRelationGroup=hpnicfEntRelationGroup, hpnicfEntRelationCompliance=hpnicfEntRelationCompliance, HpnicfEntRelationType=HpnicfEntRelationType, hpnicfEntRelation=hpnicfEntRelation, PYSNMP_MODULE_ID=hpnicfEntityRelation)
