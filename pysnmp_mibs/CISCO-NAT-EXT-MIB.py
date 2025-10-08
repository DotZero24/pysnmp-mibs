#
# PySNMP MIB module CISCO-NAT-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-NAT-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:25:08 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoNATExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 532))
ciscoNATExtMIB.setRevisions(('2006-06-05 00:00',))
if mibBuilder.loadTexts: ciscoNATExtMIB.setLastUpdated('200606050000Z')
if mibBuilder.loadTexts: ciscoNATExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoNatExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 0))
ciscoNatExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 1))
ciscoNatExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 2))
cneAddrTranslationStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1), )
if mibBuilder.loadTexts: cneAddrTranslationStatsTable.setStatus('current')
cneAddrTranslationStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cneAddrTranslationStatsEntry.setStatus('current')
cneAddrTranslationNumActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 1), Gauge32()).setUnits('Number of address translation entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslationNumActive.setStatus('current')
cneAddrTranslationNumPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 2), Unsigned32()).setUnits('Number of address translation entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslationNumPeak.setStatus('current')
cneAddrTranslation1min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 3), Gauge32()).setUnits('Address translation entries per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslation1min.setStatus('current')
cneAddrTranslation5min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 4), Gauge32()).setUnits('Address translation entries per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslation5min.setStatus('current')
ciscoNatExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 1))
ciscoNatExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 2))
ciscoNatExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 1, 1)).setObjects(("CISCO-NAT-EXT-MIB", "ciscoNatExtAddrTransStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNatExtMIBCompliance = ciscoNatExtMIBCompliance.setStatus('current')
ciscoNatExtAddrTransStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 2, 1)).setObjects(("CISCO-NAT-EXT-MIB", "cneAddrTranslationNumActive"), ("CISCO-NAT-EXT-MIB", "cneAddrTranslationNumPeak"), ("CISCO-NAT-EXT-MIB", "cneAddrTranslation1min"), ("CISCO-NAT-EXT-MIB", "cneAddrTranslation5min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNatExtAddrTransStatsGroup = ciscoNatExtAddrTransStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-NAT-EXT-MIB", ciscoNATExtMIB=ciscoNATExtMIB, ciscoNatExtMIBConformance=ciscoNatExtMIBConformance, cneAddrTranslationStatsTable=cneAddrTranslationStatsTable, cneAddrTranslation1min=cneAddrTranslation1min, cneAddrTranslation5min=cneAddrTranslation5min, ciscoNatExtMIBObjects=ciscoNatExtMIBObjects, ciscoNatExtMIBCompliances=ciscoNatExtMIBCompliances, ciscoNatExtMIBCompliance=ciscoNatExtMIBCompliance, ciscoNatExtMIBNotifs=ciscoNatExtMIBNotifs, PYSNMP_MODULE_ID=ciscoNATExtMIB, cneAddrTranslationStatsEntry=cneAddrTranslationStatsEntry, ciscoNatExtMIBGroups=ciscoNatExtMIBGroups, ciscoNatExtAddrTransStatsGroup=ciscoNatExtAddrTransStatsGroup, cneAddrTranslationNumActive=cneAddrTranslationNumActive, cneAddrTranslationNumPeak=cneAddrTranslationNumPeak)
