#
# PySNMP MIB module ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:52:44 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
adGenAOSConformance, adGenAOSMef = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSMef")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
HCPerfTimeElapsed, HCPerfCurrentCount, HCPerfInvalidIntervals, HCPerfIntervalCount, HCPerfValidIntervals, HCPerfTotalCount = mibBuilder.importSymbols("HC-PerfHist-TC-MIB", "HCPerfTimeElapsed", "HCPerfCurrentCount", "HCPerfInvalidIntervals", "HCPerfIntervalCount", "HCPerfValidIntervals", "HCPerfTotalCount")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAosMefPerEvcTotalCountMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 7))
adGenAosMefPerEvcTotalCountMib.setRevisions(('2017-10-14 00:00',))
if mibBuilder.loadTexts: adGenAosMefPerEvcTotalCountMib.setLastUpdated('201710140000Z')
if mibBuilder.loadTexts: adGenAosMefPerEvcTotalCountMib.setOrganization('ADTRAN Inc.')
adGenAosMefPerEvcTotalCount = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7))
adMefPerEvcTcTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1), )
if mibBuilder.loadTexts: adMefPerEvcTcTable.setStatus('current')
adMefPerEvcTcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1, 1), ).setIndexNames((0, "ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB", "adMefPerEvcTcEvcNameFixedLen"))
if mibBuilder.loadTexts: adMefPerEvcTcEntry.setStatus('current')
adMefPerEvcTcEvcNameFixedLen = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50))
if mibBuilder.loadTexts: adMefPerEvcTcEvcNameFixedLen.setStatus('current')
adMefPerEvcTotalIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1, 1, 2), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcTotalIngressGreenOctets.setStatus('current')
adMefPerEvcTotalIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1, 1, 3), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcTotalIngressGreenFrames.setStatus('current')
adMefPerEvcTotalIngressYellowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1, 1, 4), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcTotalIngressYellowOctets.setStatus('current')
adMefPerEvcTotalIngressYellowFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1, 1, 5), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcTotalIngressYellowFrames.setStatus('current')
adMefPerEvcTotalIngressRedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1, 1, 6), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcTotalIngressRedFrames.setStatus('current')
adGenAosMefPerEvcTotalCountConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 29))
adMefPerEvcTotalCountGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 29, 1))
adGenAosMefPerEvcTotalCountCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 29, 2))
adGenAosMefPerEvcTotalCountCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 29, 2, 1)).setObjects(("ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB", "adMefPerEvcTotalCountGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAosMefPerEvcTotalCountCompliance = adGenAosMefPerEvcTotalCountCompliance.setStatus('current')
adMefPerEvcTotalCountGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 29, 1, 1)).setObjects(("ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB", "adMefPerEvcTotalIngressGreenOctets"), ("ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB", "adMefPerEvcTotalIngressGreenFrames"), ("ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB", "adMefPerEvcTotalIngressYellowOctets"), ("ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB", "adMefPerEvcTotalIngressYellowFrames"), ("ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB", "adMefPerEvcTotalIngressRedFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerEvcTotalCountGroup = adMefPerEvcTotalCountGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB", adGenAosMefPerEvcTotalCountCompliances=adGenAosMefPerEvcTotalCountCompliances, adMefPerEvcTotalIngressGreenOctets=adMefPerEvcTotalIngressGreenOctets, adMefPerEvcTotalIngressYellowFrames=adMefPerEvcTotalIngressYellowFrames, adGenAosMefPerEvcTotalCountConformance=adGenAosMefPerEvcTotalCountConformance, adMefPerEvcTotalCountGroups=adMefPerEvcTotalCountGroups, adMefPerEvcTcTable=adMefPerEvcTcTable, adMefPerEvcTcEvcNameFixedLen=adMefPerEvcTcEvcNameFixedLen, adMefPerEvcTcEntry=adMefPerEvcTcEntry, PYSNMP_MODULE_ID=adGenAosMefPerEvcTotalCountMib, adMefPerEvcTotalIngressGreenFrames=adMefPerEvcTotalIngressGreenFrames, adMefPerEvcTotalIngressYellowOctets=adMefPerEvcTotalIngressYellowOctets, adGenAosMefPerEvcTotalCount=adGenAosMefPerEvcTotalCount, adGenAosMefPerEvcTotalCountCompliance=adGenAosMefPerEvcTotalCountCompliance, adMefPerEvcTotalIngressRedFrames=adMefPerEvcTotalIngressRedFrames, adMefPerEvcTotalCountGroup=adMefPerEvcTotalCountGroup, adGenAosMefPerEvcTotalCountMib=adGenAosMefPerEvcTotalCountMib)
