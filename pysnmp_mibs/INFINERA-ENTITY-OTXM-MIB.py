#
# PySNMP MIB module INFINERA-ENTITY-OTXM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-OTXM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:55 2025
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
mibBuilder.exportSymbols("INFINERA-ENTITY-OTXM-MIB", otxmEntry=otxmEntry, otxmProvEqptType=otxmProvEqptType, otxmMoId=otxmMoId, otxmRowStatus=otxmRowStatus, otxmTable=otxmTable, otxmConformance=otxmConformance, PYSNMP_MODULE_ID=otxmMIB, otxmGroups=otxmGroups, otxmMIB=otxmMIB, otxmCompliance=otxmCompliance, otxmGroup=otxmGroup, otxmCompliances=otxmCompliances)
