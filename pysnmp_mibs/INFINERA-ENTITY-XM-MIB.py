#
# PySNMP MIB module INFINERA-ENTITY-XM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-XM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, InfnOxmCardRedundancyStatus, InfnOxmEccStatus = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType", "InfnOxmCardRedundancyStatus", "InfnOxmEccStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-ENTITY-XM-MIB", xmMIB=xmMIB, xmGroup=xmGroup, actvTimingSource=actvTimingSource, xmCompliances=xmCompliances, xmEccStatus=xmEccStatus, xmTable=xmTable, PYSNMP_MODULE_ID=xmMIB, xmGroups=xmGroups, xmConformance=xmConformance, xmEntry=xmEntry, cardRedundancyStatus=cardRedundancyStatus, xmMoId=xmMoId, xmCompliance=xmCompliance, xmRowStatus=xmRowStatus, xmProvEqptType=xmProvEqptType)
