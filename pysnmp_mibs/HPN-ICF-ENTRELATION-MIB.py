#
# PySNMP MIB module HPN-ICF-ENTRELATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-ENTRELATION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("HPN-ICF-ENTRELATION-MIB", hpnicfEntRelation=hpnicfEntRelation, hpnicfEntRelationCompliances=hpnicfEntRelationCompliances, hpnicfEntityIndex=hpnicfEntityIndex, hpnicfEntRelationTable=hpnicfEntRelationTable, hpnicfEntRelationConformance=hpnicfEntRelationConformance, hpnicfEntityRelation=hpnicfEntityRelation, hpnicfEntRelationType=hpnicfEntRelationType, hpnicfEntRelationCompliance=hpnicfEntRelationCompliance, hpnicfEntRelationEntry=hpnicfEntRelationEntry, HpnicfEntRelationType=HpnicfEntRelationType, hpnicfRelatedEntityIndex=hpnicfRelatedEntityIndex, hpnicfEntRelationGroup=hpnicfEntRelationGroup, hpnicfEntRelationObjects=hpnicfEntRelationObjects, PYSNMP_MODULE_ID=hpnicfEntityRelation, hpnicfEntRelationGroups=hpnicfEntRelationGroups)
