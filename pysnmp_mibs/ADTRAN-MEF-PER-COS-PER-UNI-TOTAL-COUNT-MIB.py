#
# PySNMP MIB module ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:29:57 2025
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
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAosMefPerCosPerUniTotalCountMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 6))
adGenAosMefPerCosPerUniTotalCountMib.setRevisions(('2017-10-14 00:00',))
if mibBuilder.loadTexts: adGenAosMefPerCosPerUniTotalCountMib.setLastUpdated('201710140000Z')
if mibBuilder.loadTexts: adGenAosMefPerCosPerUniTotalCountMib.setOrganization('ADTRAN Inc.')
adGenAosMefPerCosPerUniTotalCount = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6))
adMefPerCosPerUniTcTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1), )
if mibBuilder.loadTexts: adMefPerCosPerUniTcTable.setStatus('current')
adMefPerCosPerUniTcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", "adMefPerCosPerUniTcQueueNumber"))
if mibBuilder.loadTexts: adMefPerCosPerUniTcEntry.setStatus('current')
adMefPerCosPerUniTcQueueNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: adMefPerCosPerUniTcQueueNumber.setStatus('current')
adMefPerCosPerUniTotalIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1, 1, 2), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniTotalIngressGreenOctets.setStatus('current')
adMefPerCosPerUniTotalIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1, 1, 3), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniTotalIngressGreenFrames.setStatus('current')
adMefPerCosPerUniTotalIngressYellowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1, 1, 4), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniTotalIngressYellowOctets.setStatus('current')
adMefPerCosPerUniTotalIngressYellowFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1, 1, 5), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniTotalIngressYellowFrames.setStatus('current')
adMefPerCosPerUniTotalIngressRedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1, 1, 6), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniTotalIngressRedFrames.setStatus('current')
adGenAosMefPerCosPerUniTotalCountConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 28))
adMefPerCosPerUniTotalCountGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 28, 1))
adGenAosMefPerCosPerUniTotalCountCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 28, 2))
adGenAosMefPerUniTotalCountCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 28, 2, 1)).setObjects(("ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", "adMefPerCosPerUniTotalCountGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAosMefPerUniTotalCountCompliance = adGenAosMefPerUniTotalCountCompliance.setStatus('current')
adMefPerCosPerUniTotalCountGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 28, 1, 1)).setObjects(("ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", "adMefPerCosPerUniTotalIngressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", "adMefPerCosPerUniTotalIngressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", "adMefPerCosPerUniTotalIngressYellowOctets"), ("ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", "adMefPerCosPerUniTotalIngressYellowFrames"), ("ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", "adMefPerCosPerUniTotalIngressRedFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerCosPerUniTotalCountGroup = adMefPerCosPerUniTotalCountGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", adGenAosMefPerUniTotalCountCompliance=adGenAosMefPerUniTotalCountCompliance, adMefPerCosPerUniTotalCountGroups=adMefPerCosPerUniTotalCountGroups, PYSNMP_MODULE_ID=adGenAosMefPerCosPerUniTotalCountMib, adGenAosMefPerCosPerUniTotalCountConformance=adGenAosMefPerCosPerUniTotalCountConformance, adMefPerCosPerUniTotalIngressRedFrames=adMefPerCosPerUniTotalIngressRedFrames, adGenAosMefPerCosPerUniTotalCount=adGenAosMefPerCosPerUniTotalCount, adMefPerCosPerUniTcTable=adMefPerCosPerUniTcTable, adMefPerCosPerUniTotalIngressYellowFrames=adMefPerCosPerUniTotalIngressYellowFrames, adGenAosMefPerCosPerUniTotalCountCompliances=adGenAosMefPerCosPerUniTotalCountCompliances, adMefPerCosPerUniTotalCountGroup=adMefPerCosPerUniTotalCountGroup, adMefPerCosPerUniTotalIngressYellowOctets=adMefPerCosPerUniTotalIngressYellowOctets, adGenAosMefPerCosPerUniTotalCountMib=adGenAosMefPerCosPerUniTotalCountMib, adMefPerCosPerUniTcEntry=adMefPerCosPerUniTcEntry, adMefPerCosPerUniTotalIngressGreenOctets=adMefPerCosPerUniTotalIngressGreenOctets, adMefPerCosPerUniTcQueueNumber=adMefPerCosPerUniTcQueueNumber, adMefPerCosPerUniTotalIngressGreenFrames=adMefPerCosPerUniTotalIngressGreenFrames)
