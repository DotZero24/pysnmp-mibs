#
# PySNMP MIB module INFINERA-TP-FLEXCARRIERCTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-FLEXCARRIERCTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:24 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
InfnPmHistStatsControl, FloatHundredths, InfnModulation, FloatTenths = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnPmHistStatsControl", "FloatHundredths", "InfnModulation", "FloatTenths")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-TP-FLEXCARRIERCTP-MIB", flexCarrierCtpFreqSlotList=flexCarrierCtpFreqSlotList, flexCarrierCtpPmHistStatsEnable=flexCarrierCtpPmHistStatsEnable, PYSNMP_MODULE_ID=flexCarrierCtpMIB, flexCarrierCtpGroup=flexCarrierCtpGroup, flexCarrierCtpTable=flexCarrierCtpTable, flexCarrierCtpMIB=flexCarrierCtpMIB, flexCarrierCtpEntry=flexCarrierCtpEntry, flexCarrierCtpCompliances=flexCarrierCtpCompliances, flexCarrierCtpGroups=flexCarrierCtpGroups, flexCarrierCtpConformance=flexCarrierCtpConformance, flexCarrierCtpCompliance=flexCarrierCtpCompliance)
