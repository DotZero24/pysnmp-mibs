#
# PySNMP MIB module INFINERA-ENTITY-ASEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-ASEM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:28 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
asemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56))
if mibBuilder.loadTexts: asemMIB.setLastUpdated('201703210000Z')
if mibBuilder.loadTexts: asemMIB.setOrganization('Infinera')
asemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 3))
asemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 3, 1))
asemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 3, 2))
asemTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 1), )
if mibBuilder.loadTexts: asemTable.setStatus('current')
asemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: asemEntry.setStatus('current')
asemMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asemMoId.setStatus('current')
asemProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 1, 1, 2), InfnEqptType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asemProvEqptType.setStatus('current')
asemCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 3, 1, 1)).setObjects(("INFINERA-ENTITY-ASEM-MIB", "asemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    asemCompliance = asemCompliance.setStatus('current')
asemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 56, 3, 2, 1)).setObjects(("INFINERA-ENTITY-ASEM-MIB", "asemMoId"), ("INFINERA-ENTITY-ASEM-MIB", "asemProvEqptType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    asemGroup = asemGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-ASEM-MIB", asemConformance=asemConformance, asemTable=asemTable, asemGroup=asemGroup, asemCompliance=asemCompliance, asemGroups=asemGroups, asemMIB=asemMIB, asemEntry=asemEntry, asemProvEqptType=asemProvEqptType, asemCompliances=asemCompliances, asemMoId=asemMoId, PYSNMP_MODULE_ID=asemMIB)
