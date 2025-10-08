#
# PySNMP MIB module ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:29:59 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adGenAOSConformance, adGenAOSMef = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSMef")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
HCPerfTotalCount, HCPerfValidIntervals, HCPerfInvalidIntervals, HCPerfTimeElapsed, HCPerfIntervalCount, HCPerfCurrentCount = mibBuilder.importSymbols("HC-PerfHist-TC-MIB", "HCPerfTotalCount", "HCPerfValidIntervals", "HCPerfInvalidIntervals", "HCPerfTimeElapsed", "HCPerfIntervalCount", "HCPerfCurrentCount")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAosMefPerUniTotalCountMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 5))
adGenAosMefPerUniTotalCountMib.setRevisions(('2017-10-14 00:00',))
if mibBuilder.loadTexts: adGenAosMefPerUniTotalCountMib.setLastUpdated('201710140000Z')
if mibBuilder.loadTexts: adGenAosMefPerUniTotalCountMib.setOrganization('ADTRAN Inc.')
adGenAosMefPerUniTotalCount = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5))
adMefPerUniTcTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5, 1), )
if mibBuilder.loadTexts: adMefPerUniTcTable.setStatus('current')
adMefPerUniTcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adMefPerUniTcEntry.setStatus('current')
adMefPerUniTotalIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5, 1, 1, 1), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniTotalIngressGreenOctets.setStatus('current')
adMefPerUniTotalIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5, 1, 1, 2), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniTotalIngressGreenFrames.setStatus('current')
adMefPerUniTotalIngressYellowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5, 1, 1, 3), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniTotalIngressYellowOctets.setStatus('current')
adMefPerUniTotalIngressYellowFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5, 1, 1, 4), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniTotalIngressYellowFrames.setStatus('current')
adMefPerUniTotalIngressRedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5, 1, 1, 5), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniTotalIngressRedFrames.setStatus('current')
adGenAosMefPerUniTotalCountConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 27))
adMefPerUniTotalCountGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 27, 1))
adGenAosMefPerUniTotalCountCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 27, 2))
adGenAosMefPerUniTotalCountCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 27, 2, 1)).setObjects(("ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB", "adMefPerUniTotalCountGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAosMefPerUniTotalCountCompliance = adGenAosMefPerUniTotalCountCompliance.setStatus('current')
adMefPerUniTotalCountGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 27, 1, 1)).setObjects(("ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB", "adMefPerUniTotalIngressGreenOctets"), ("ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB", "adMefPerUniTotalIngressGreenFrames"), ("ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB", "adMefPerUniTotalIngressYellowOctets"), ("ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB", "adMefPerUniTotalIngressYellowFrames"), ("ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB", "adMefPerUniTotalIngressRedFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerUniTotalCountGroup = adMefPerUniTotalCountGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB", adMefPerUniTotalIngressRedFrames=adMefPerUniTotalIngressRedFrames, adGenAosMefPerUniTotalCountCompliance=adGenAosMefPerUniTotalCountCompliance, adMefPerUniTotalIngressYellowFrames=adMefPerUniTotalIngressYellowFrames, adMefPerUniTotalCountGroup=adMefPerUniTotalCountGroup, adMefPerUniTotalIngressGreenFrames=adMefPerUniTotalIngressGreenFrames, adGenAosMefPerUniTotalCountCompliances=adGenAosMefPerUniTotalCountCompliances, adMefPerUniTotalIngressGreenOctets=adMefPerUniTotalIngressGreenOctets, adMefPerUniTcEntry=adMefPerUniTcEntry, adGenAosMefPerUniTotalCountMib=adGenAosMefPerUniTotalCountMib, adGenAosMefPerUniTotalCountConformance=adGenAosMefPerUniTotalCountConformance, adMefPerUniTotalCountGroups=adMefPerUniTotalCountGroups, PYSNMP_MODULE_ID=adGenAosMefPerUniTotalCountMib, adMefPerUniTcTable=adMefPerUniTcTable, adGenAosMefPerUniTotalCount=adGenAosMefPerUniTotalCount, adMefPerUniTotalIngressYellowOctets=adMefPerUniTotalIngressYellowOctets)
