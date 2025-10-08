#
# PySNMP MIB module ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:53:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
adGenAOSConformance, adGenAOSMef = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSMef")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
HCPerfTimeElapsed, HCPerfCurrentCount, HCPerfInvalidIntervals, HCPerfIntervalCount, HCPerfValidIntervals, HCPerfTotalCount = mibBuilder.importSymbols("HC-PerfHist-TC-MIB", "HCPerfTimeElapsed", "HCPerfCurrentCount", "HCPerfInvalidIntervals", "HCPerfIntervalCount", "HCPerfValidIntervals", "HCPerfTotalCount")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB", adGenAosMefPerUniTotalCountCompliances=adGenAosMefPerUniTotalCountCompliances, adMefPerUniTotalIngressGreenOctets=adMefPerUniTotalIngressGreenOctets, adGenAosMefPerUniTotalCountCompliance=adGenAosMefPerUniTotalCountCompliance, adMefPerUniTcEntry=adMefPerUniTcEntry, adMefPerUniTotalIngressRedFrames=adMefPerUniTotalIngressRedFrames, PYSNMP_MODULE_ID=adGenAosMefPerUniTotalCountMib, adGenAosMefPerUniTotalCount=adGenAosMefPerUniTotalCount, adMefPerUniTotalIngressYellowFrames=adMefPerUniTotalIngressYellowFrames, adMefPerUniTotalCountGroups=adMefPerUniTotalCountGroups, adGenAosMefPerUniTotalCountMib=adGenAosMefPerUniTotalCountMib, adMefPerUniTotalCountGroup=adMefPerUniTotalCountGroup, adMefPerUniTotalIngressGreenFrames=adMefPerUniTotalIngressGreenFrames, adMefPerUniTotalIngressYellowOctets=adMefPerUniTotalIngressYellowOctets, adGenAosMefPerUniTotalCountConformance=adGenAosMefPerUniTotalCountConformance, adMefPerUniTcTable=adMefPerUniTcTable)
