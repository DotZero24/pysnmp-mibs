#
# PySNMP MIB module INFINERA-TP-FLEXCARRIERCTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-FLEXCARRIERCTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
InfnPmHistStatsControl, FloatHundredths, InfnModulation, FloatTenths = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnPmHistStatsControl", "FloatHundredths", "InfnModulation", "FloatTenths")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
flexCarrierCtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59))
if mibBuilder.loadTexts: flexCarrierCtpMIB.setLastUpdated('201506170000Z')
if mibBuilder.loadTexts: flexCarrierCtpMIB.setOrganization('INFINERA')
flexCarrierCtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 1), )
if mibBuilder.loadTexts: flexCarrierCtpTable.setStatus('current')
flexCarrierCtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: flexCarrierCtpEntry.setStatus('current')
flexCarrierCtpPmHistStatsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 1, 1, 1), InfnPmHistStatsControl()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flexCarrierCtpPmHistStatsEnable.setStatus('current')
flexCarrierCtpFreqSlotList = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flexCarrierCtpFreqSlotList.setStatus('current')
flexCarrierCtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 59))
flexCarrierCtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 59, 1))
flexCarrierCtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 59, 2))
flexCarrierCtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 59, 1, 1)).setObjects(("INFINERA-TP-FLEXCARRIERCTP-MIB", "flexCarrierCtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    flexCarrierCtpCompliance = flexCarrierCtpCompliance.setStatus('current')
flexCarrierCtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 59, 2, 1)).setObjects(("INFINERA-TP-FLEXCARRIERCTP-MIB", "flexCarrierCtpPmHistStatsEnable"), ("INFINERA-TP-FLEXCARRIERCTP-MIB", "flexCarrierCtpFreqSlotList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    flexCarrierCtpGroup = flexCarrierCtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-FLEXCARRIERCTP-MIB", flexCarrierCtpConformance=flexCarrierCtpConformance, PYSNMP_MODULE_ID=flexCarrierCtpMIB, flexCarrierCtpCompliances=flexCarrierCtpCompliances, flexCarrierCtpGroups=flexCarrierCtpGroups, flexCarrierCtpTable=flexCarrierCtpTable, flexCarrierCtpCompliance=flexCarrierCtpCompliance, flexCarrierCtpGroup=flexCarrierCtpGroup, flexCarrierCtpFreqSlotList=flexCarrierCtpFreqSlotList, flexCarrierCtpEntry=flexCarrierCtpEntry, flexCarrierCtpPmHistStatsEnable=flexCarrierCtpPmHistStatsEnable, flexCarrierCtpMIB=flexCarrierCtpMIB)
