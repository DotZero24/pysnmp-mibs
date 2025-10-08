#
# PySNMP MIB module INFINERA-ENTITY-EXTNSHELF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-EXTNSHELF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:26 2025
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
mibBuilder.exportSymbols("INFINERA-ENTITY-EXTNSHELF-MIB", PYSNMP_MODULE_ID=extnShelfMIB, extnShelfEntry=extnShelfEntry, extnShelfProvSerialNumber=extnShelfProvSerialNumber, extnShelfCompliances=extnShelfCompliances, extnShelfProvEqptType=extnShelfProvEqptType, extnShelfConformance=extnShelfConformance, extnShelfTable=extnShelfTable, extnShelfGroups=extnShelfGroups, extnShelfCompliance=extnShelfCompliance, extnShelfMIB=extnShelfMIB, extnShelfGroup=extnShelfGroup, extnShelfMoId=extnShelfMoId)
