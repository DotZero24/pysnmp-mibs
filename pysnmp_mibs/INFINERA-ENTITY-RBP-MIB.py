#
# PySNMP MIB module INFINERA-ENTITY-RBP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-RBP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:15 2025
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
mibBuilder.exportSymbols("INFINERA-ENTITY-RBP-MIB", rbpCompliances=rbpCompliances, rbpEntry=rbpEntry, rbpMIB=rbpMIB, rbpProvEqptType=rbpProvEqptType, PYSNMP_MODULE_ID=rbpMIB, rbpGroups=rbpGroups, rbpTable=rbpTable, rbpProvSerialNumber=rbpProvSerialNumber, rbpGroup=rbpGroup, rbpCompliance=rbpCompliance, rbpMoId=rbpMoId, rbpConformance=rbpConformance)
