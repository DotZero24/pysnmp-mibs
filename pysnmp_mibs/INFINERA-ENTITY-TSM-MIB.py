#
# PySNMP MIB module INFINERA-ENTITY-TSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-TSM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:28 2025
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
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
tsmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22))
if mibBuilder.loadTexts: tsmMIB.setLastUpdated('201110200000Z')
if mibBuilder.loadTexts: tsmMIB.setOrganization('INFINERA')
tsmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 3))
tsmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 3, 1))
tsmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 3, 2))
tsmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 1), )
if mibBuilder.loadTexts: tsmTable.setStatus('current')
tsmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: tsmEntry.setStatus('current')
tsmMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tsmMoId.setStatus('current')
tsmProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tsmProvEqptType.setStatus('current')
tsmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tsmRowStatus.setStatus('current')
cardRedundancyState = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("active", 2), ("standby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardRedundancyState.setStatus('current')
tsmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 3, 1, 1)).setObjects(("INFINERA-ENTITY-TSM-MIB", "tsmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tsmCompliance = tsmCompliance.setStatus('current')
tsmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 22, 3, 2, 1)).setObjects(("INFINERA-ENTITY-TSM-MIB", "tsmMoId"), ("INFINERA-ENTITY-TSM-MIB", "tsmProvEqptType"), ("INFINERA-ENTITY-TSM-MIB", "tsmRowStatus"), ("INFINERA-ENTITY-TSM-MIB", "cardRedundancyState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tsmGroup = tsmGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-TSM-MIB", tsmTable=tsmTable, tsmConformance=tsmConformance, tsmRowStatus=tsmRowStatus, tsmCompliances=tsmCompliances, tsmGroup=tsmGroup, tsmCompliance=tsmCompliance, tsmEntry=tsmEntry, tsmMoId=tsmMoId, PYSNMP_MODULE_ID=tsmMIB, tsmGroups=tsmGroups, cardRedundancyState=cardRedundancyState, tsmProvEqptType=tsmProvEqptType, tsmMIB=tsmMIB)
