#
# PySNMP MIB module INFINERA-ENTITY-OTM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-OTM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:21 2025
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
otmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24))
if mibBuilder.loadTexts: otmMIB.setLastUpdated('201110200000Z')
if mibBuilder.loadTexts: otmMIB.setOrganization('INFINERA')
otmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 3))
otmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 3, 1))
otmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 3, 2))
otmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 1), )
if mibBuilder.loadTexts: otmTable.setStatus('current')
otmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: otmEntry.setStatus('current')
otmMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: otmMoId.setStatus('current')
otmProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: otmProvEqptType.setStatus('current')
otmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: otmRowStatus.setStatus('current')
actvTimingSource = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: actvTimingSource.setStatus('current')
otmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 3, 1, 1)).setObjects(("INFINERA-ENTITY-OTM-MIB", "otmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    otmCompliance = otmCompliance.setStatus('current')
otmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 3, 2, 1)).setObjects(("INFINERA-ENTITY-OTM-MIB", "otmMoId"), ("INFINERA-ENTITY-OTM-MIB", "otmProvEqptType"), ("INFINERA-ENTITY-OTM-MIB", "otmRowStatus"), ("INFINERA-ENTITY-OTM-MIB", "actvTimingSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    otmGroup = otmGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-OTM-MIB", otmGroups=otmGroups, otmConformance=otmConformance, actvTimingSource=actvTimingSource, otmProvEqptType=otmProvEqptType, otmGroup=otmGroup, otmCompliance=otmCompliance, otmEntry=otmEntry, otmMoId=otmMoId, PYSNMP_MODULE_ID=otmMIB, otmCompliances=otmCompliances, otmMIB=otmMIB, otmRowStatus=otmRowStatus, otmTable=otmTable)
