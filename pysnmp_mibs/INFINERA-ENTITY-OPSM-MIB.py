#
# PySNMP MIB module INFINERA-ENTITY-OPSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-OPSM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:01 2025
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
mibBuilder.exportSymbols("INFINERA-ENTITY-OPSM-MIB", opsmNodeId=opsmNodeId, PYSNMP_MODULE_ID=opsmMIB, opsmGroups=opsmGroups, opsmConformance=opsmConformance, opsmMoId=opsmMoId, opsmProvEqptType=opsmProvEqptType, opsmTable=opsmTable, opsmMIB=opsmMIB, opsmCompliance=opsmCompliance, opsmEntry=opsmEntry, opsmGroup=opsmGroup, opsmCompliances=opsmCompliances)
