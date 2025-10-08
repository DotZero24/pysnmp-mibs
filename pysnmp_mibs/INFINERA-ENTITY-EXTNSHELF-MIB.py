#
# PySNMP MIB module INFINERA-ENTITY-EXTNSHELF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-EXTNSHELF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:26 2025
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
extnShelfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53))
if mibBuilder.loadTexts: extnShelfMIB.setLastUpdated('201505100000Z')
if mibBuilder.loadTexts: extnShelfMIB.setOrganization('Infinera')
extnShelfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 3))
extnShelfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 3, 1))
extnShelfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 3, 2))
extnShelfTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 1), )
if mibBuilder.loadTexts: extnShelfTable.setStatus('current')
extnShelfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: extnShelfEntry.setStatus('current')
extnShelfMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extnShelfMoId.setStatus('current')
extnShelfProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 1, 1, 2), InfnEqptType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extnShelfProvEqptType.setStatus('current')
extnShelfProvSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extnShelfProvSerialNumber.setStatus('current')
extnShelfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 3, 1, 1)).setObjects(("INFINERA-ENTITY-EXTNSHELF-MIB", "extnShelfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    extnShelfCompliance = extnShelfCompliance.setStatus('current')
extnShelfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 53, 3, 2, 1)).setObjects(("INFINERA-ENTITY-EXTNSHELF-MIB", "extnShelfMoId"), ("INFINERA-ENTITY-EXTNSHELF-MIB", "extnShelfProvEqptType"), ("INFINERA-ENTITY-EXTNSHELF-MIB", "extnShelfProvSerialNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    extnShelfGroup = extnShelfGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-EXTNSHELF-MIB", extnShelfProvEqptType=extnShelfProvEqptType, extnShelfMIB=extnShelfMIB, extnShelfMoId=extnShelfMoId, extnShelfTable=extnShelfTable, PYSNMP_MODULE_ID=extnShelfMIB, extnShelfGroups=extnShelfGroups, extnShelfEntry=extnShelfEntry, extnShelfProvSerialNumber=extnShelfProvSerialNumber, extnShelfCompliances=extnShelfCompliances, extnShelfCompliance=extnShelfCompliance, extnShelfGroup=extnShelfGroup, extnShelfConformance=extnShelfConformance)
