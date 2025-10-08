#
# PySNMP MIB module INFINERA-ENTITY-OPSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-OPSM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:30 2025
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
opsmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43))
if mibBuilder.loadTexts: opsmMIB.setLastUpdated('201505100000Z')
if mibBuilder.loadTexts: opsmMIB.setOrganization('Infinera')
opsmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 3))
opsmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 3, 1))
opsmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 3, 2))
opsmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 1), )
if mibBuilder.loadTexts: opsmTable.setStatus('current')
opsmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: opsmEntry.setStatus('current')
opsmMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: opsmMoId.setStatus('current')
opsmProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 1, 1, 2), InfnEqptType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: opsmProvEqptType.setStatus('current')
opsmNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: opsmNodeId.setStatus('current')
opsmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 3, 1, 1)).setObjects(("INFINERA-ENTITY-OPSM-MIB", "opsmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    opsmCompliance = opsmCompliance.setStatus('current')
opsmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 43, 3, 2, 1)).setObjects(("INFINERA-ENTITY-OPSM-MIB", "opsmMoId"), ("INFINERA-ENTITY-OPSM-MIB", "opsmProvEqptType"), ("INFINERA-ENTITY-OPSM-MIB", "opsmNodeId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    opsmGroup = opsmGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-OPSM-MIB", opsmProvEqptType=opsmProvEqptType, PYSNMP_MODULE_ID=opsmMIB, opsmMoId=opsmMoId, opsmTable=opsmTable, opsmCompliance=opsmCompliance, opsmMIB=opsmMIB, opsmGroups=opsmGroups, opsmEntry=opsmEntry, opsmNodeId=opsmNodeId, opsmGroup=opsmGroup, opsmConformance=opsmConformance, opsmCompliances=opsmCompliances)
