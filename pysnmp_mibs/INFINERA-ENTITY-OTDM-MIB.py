#
# PySNMP MIB module INFINERA-ENTITY-OTDM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-OTDM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:25 2025
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
mibBuilder.exportSymbols("INFINERA-ENTITY-OTDM-MIB", otdmGroups=otdmGroups, PYSNMP_MODULE_ID=otdmMIB, otdmCompliance=otdmCompliance, otdmConformance=otdmConformance, otdmEntry=otdmEntry, otdmMoId=otdmMoId, otdmMIB=otdmMIB, otdmGroup=otdmGroup, otdmTable=otdmTable, otdmProvEqptType=otdmProvEqptType, otdmCompliances=otdmCompliances)
