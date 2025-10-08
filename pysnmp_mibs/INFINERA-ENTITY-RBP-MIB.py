#
# PySNMP MIB module INFINERA-ENTITY-RBP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-RBP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:54 2025
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
rbpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49))
if mibBuilder.loadTexts: rbpMIB.setLastUpdated('201501080000Z')
if mibBuilder.loadTexts: rbpMIB.setOrganization('INFINERA')
rbpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 3))
rbpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 3, 1))
rbpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 3, 2))
rbpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 1), )
if mibBuilder.loadTexts: rbpTable.setStatus('current')
rbpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: rbpEntry.setStatus('current')
rbpMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbpMoId.setStatus('current')
rbpProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbpProvEqptType.setStatus('current')
rbpProvSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbpProvSerialNumber.setStatus('current')
rbpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 3, 1, 1)).setObjects(("INFINERA-ENTITY-RBP-MIB", "rbpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbpCompliance = rbpCompliance.setStatus('current')
rbpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 49, 3, 2, 1)).setObjects(("INFINERA-ENTITY-RBP-MIB", "rbpMoId"), ("INFINERA-ENTITY-RBP-MIB", "rbpProvEqptType"), ("INFINERA-ENTITY-RBP-MIB", "rbpProvSerialNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbpGroup = rbpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-RBP-MIB", rbpMoId=rbpMoId, rbpProvSerialNumber=rbpProvSerialNumber, rbpProvEqptType=rbpProvEqptType, rbpTable=rbpTable, rbpCompliance=rbpCompliance, PYSNMP_MODULE_ID=rbpMIB, rbpConformance=rbpConformance, rbpGroups=rbpGroups, rbpEntry=rbpEntry, rbpMIB=rbpMIB, rbpCompliances=rbpCompliances, rbpGroup=rbpGroup)
