#
# PySNMP MIB module INFINERA-ENTITY-BPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-BPP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
bppMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48))
if mibBuilder.loadTexts: bppMIB.setLastUpdated('201501080000Z')
if mibBuilder.loadTexts: bppMIB.setOrganization('INFINERA')
bppConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 3))
bppCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 3, 1))
bppGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 3, 2))
bppTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 1), )
if mibBuilder.loadTexts: bppTable.setStatus('current')
bppEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: bppEntry.setStatus('current')
bppMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bppMoId.setStatus('current')
bppProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bppProvEqptType.setStatus('current')
bppProvSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bppProvSerialNumber.setStatus('current')
bppCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 3, 1, 1)).setObjects(("INFINERA-ENTITY-BPP-MIB", "bppGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bppCompliance = bppCompliance.setStatus('current')
bppGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 48, 3, 2, 1)).setObjects(("INFINERA-ENTITY-BPP-MIB", "bppMoId"), ("INFINERA-ENTITY-BPP-MIB", "bppProvEqptType"), ("INFINERA-ENTITY-BPP-MIB", "bppProvSerialNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bppGroup = bppGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-BPP-MIB", bppMoId=bppMoId, bppTable=bppTable, bppMIB=bppMIB, bppGroup=bppGroup, PYSNMP_MODULE_ID=bppMIB, bppCompliances=bppCompliances, bppConformance=bppConformance, bppEntry=bppEntry, bppCompliance=bppCompliance, bppGroups=bppGroups, bppProvSerialNumber=bppProvSerialNumber, bppProvEqptType=bppProvEqptType)
