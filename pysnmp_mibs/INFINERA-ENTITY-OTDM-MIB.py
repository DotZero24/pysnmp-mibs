#
# PySNMP MIB module INFINERA-ENTITY-OTDM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-OTDM-MIB
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
otdmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46))
if mibBuilder.loadTexts: otdmMIB.setLastUpdated('201505100000Z')
if mibBuilder.loadTexts: otdmMIB.setOrganization('Infinera')
otdmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 3))
otdmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 3, 1))
otdmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 3, 2))
otdmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 1), )
if mibBuilder.loadTexts: otdmTable.setStatus('current')
otdmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: otdmEntry.setStatus('current')
otdmMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otdmMoId.setStatus('current')
otdmProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 1, 1, 2), InfnEqptType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otdmProvEqptType.setStatus('current')
otdmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 3, 1, 1)).setObjects(("INFINERA-ENTITY-OTDM-MIB", "otdmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    otdmCompliance = otdmCompliance.setStatus('current')
otdmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 46, 3, 2, 1)).setObjects(("INFINERA-ENTITY-OTDM-MIB", "otdmMoId"), ("INFINERA-ENTITY-OTDM-MIB", "otdmProvEqptType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    otdmGroup = otdmGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-OTDM-MIB", otdmConformance=otdmConformance, otdmMIB=otdmMIB, otdmGroup=otdmGroup, PYSNMP_MODULE_ID=otdmMIB, otdmTable=otdmTable, otdmGroups=otdmGroups, otdmEntry=otdmEntry, otdmCompliances=otdmCompliances, otdmProvEqptType=otdmProvEqptType, otdmMoId=otdmMoId, otdmCompliance=otdmCompliance)
