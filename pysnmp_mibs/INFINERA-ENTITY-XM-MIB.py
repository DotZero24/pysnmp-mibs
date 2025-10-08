#
# PySNMP MIB module INFINERA-ENTITY-XM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-XM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, InfnOxmCardRedundancyStatus, InfnOxmEccStatus = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType", "InfnOxmCardRedundancyStatus", "InfnOxmEccStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
xmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20))
if mibBuilder.loadTexts: xmMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: xmMIB.setOrganization('INFINERA')
xmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 3))
xmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 3, 1))
xmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 3, 2))
xmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1), )
if mibBuilder.loadTexts: xmTable.setStatus('current')
xmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: xmEntry.setStatus('current')
xmMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmMoId.setStatus('current')
cardRedundancyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1, 1, 2), InfnOxmCardRedundancyStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardRedundancyStatus.setStatus('current')
xmProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1, 1, 3), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xmProvEqptType.setStatus('current')
xmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xmRowStatus.setStatus('current')
actvTimingSource = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: actvTimingSource.setStatus('current')
xmEccStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1, 1, 6), InfnOxmEccStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmEccStatus.setStatus('current')
xmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 3, 1, 1)).setObjects(("INFINERA-ENTITY-XM-MIB", "xmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xmCompliance = xmCompliance.setStatus('current')
xmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 3, 2, 1)).setObjects(("INFINERA-ENTITY-XM-MIB", "xmMoId"), ("INFINERA-ENTITY-XM-MIB", "cardRedundancyStatus"), ("INFINERA-ENTITY-XM-MIB", "xmProvEqptType"), ("INFINERA-ENTITY-XM-MIB", "xmRowStatus"), ("INFINERA-ENTITY-XM-MIB", "actvTimingSource"), ("INFINERA-ENTITY-XM-MIB", "xmEccStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xmGroup = xmGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-XM-MIB", xmMIB=xmMIB, xmEccStatus=xmEccStatus, PYSNMP_MODULE_ID=xmMIB, xmTable=xmTable, xmRowStatus=xmRowStatus, xmCompliances=xmCompliances, actvTimingSource=actvTimingSource, cardRedundancyStatus=cardRedundancyStatus, xmMoId=xmMoId, xmCompliance=xmCompliance, xmConformance=xmConformance, xmGroups=xmGroups, xmGroup=xmGroup, xmProvEqptType=xmProvEqptType, xmEntry=xmEntry)
