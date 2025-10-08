#
# PySNMP MIB module INFINERA-ENTITY-ASEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-ASEM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-ENTITY-ASEM-MIB", asemGroups=asemGroups, asemProvEqptType=asemProvEqptType, asemConformance=asemConformance, asemCompliances=asemCompliances, asemTable=asemTable, asemEntry=asemEntry, asemCompliance=asemCompliance, asemMIB=asemMIB, asemMoId=asemMoId, PYSNMP_MODULE_ID=asemMIB, asemGroup=asemGroup)
