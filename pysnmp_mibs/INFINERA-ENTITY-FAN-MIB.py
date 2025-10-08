#
# PySNMP MIB module INFINERA-ENTITY-FAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-FAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:14 2025
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
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14))
if mibBuilder.loadTexts: fanMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: fanMIB.setOrganization('INFINERA')
fanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 3))
fanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 3, 1))
fanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 3, 2))
fanTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 1), )
if mibBuilder.loadTexts: fanTable.setStatus('current')
fanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: fanEntry.setStatus('current')
fanMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanMoId.setStatus('current')
fanProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 1, 1, 2), InfnEqptType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanProvEqptType.setStatus('current')
fanCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 3, 1, 1)).setObjects(("INFINERA-ENTITY-FAN-MIB", "fanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fanCompliance = fanCompliance.setStatus('current')
fanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 14, 3, 2, 1)).setObjects(("INFINERA-ENTITY-FAN-MIB", "fanMoId"), ("INFINERA-ENTITY-FAN-MIB", "fanProvEqptType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fanGroup = fanGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-FAN-MIB", fanProvEqptType=fanProvEqptType, PYSNMP_MODULE_ID=fanMIB, fanCompliances=fanCompliances, fanGroups=fanGroups, fanTable=fanTable, fanEntry=fanEntry, fanCompliance=fanCompliance, fanGroup=fanGroup, fanConformance=fanConformance, fanMoId=fanMoId, fanMIB=fanMIB)
