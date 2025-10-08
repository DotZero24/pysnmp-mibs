#
# PySNMP MIB module INFINERA-ENTITY-OTXM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-OTXM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
otxmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32))
if mibBuilder.loadTexts: otxmMIB.setLastUpdated('201110200000Z')
if mibBuilder.loadTexts: otxmMIB.setOrganization('INFINERA')
otxmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 3))
otxmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 3, 1))
otxmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 3, 2))
otxmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 1), )
if mibBuilder.loadTexts: otxmTable.setStatus('current')
otxmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: otxmEntry.setStatus('current')
otxmMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: otxmMoId.setStatus('current')
otxmProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: otxmProvEqptType.setStatus('current')
otxmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: otxmRowStatus.setStatus('current')
otxmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 3, 1, 1)).setObjects(("INFINERA-ENTITY-OTXM-MIB", "otxmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    otxmCompliance = otxmCompliance.setStatus('current')
otxmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 32, 3, 2, 1)).setObjects(("INFINERA-ENTITY-OTXM-MIB", "otxmMoId"), ("INFINERA-ENTITY-OTXM-MIB", "otxmProvEqptType"), ("INFINERA-ENTITY-OTXM-MIB", "otxmRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    otxmGroup = otxmGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-OTXM-MIB", otxmGroup=otxmGroup, otxmMIB=otxmMIB, otxmTable=otxmTable, otxmProvEqptType=otxmProvEqptType, PYSNMP_MODULE_ID=otxmMIB, otxmMoId=otxmMoId, otxmRowStatus=otxmRowStatus, otxmConformance=otxmConformance, otxmEntry=otxmEntry, otxmCompliances=otxmCompliances, otxmCompliance=otxmCompliance, otxmGroups=otxmGroups)
