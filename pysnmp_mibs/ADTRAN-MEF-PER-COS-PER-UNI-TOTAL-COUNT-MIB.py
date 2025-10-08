#
# PySNMP MIB module ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:53:26 2025
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
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", adMefPerCosPerUniTotalIngressGreenFrames=adMefPerCosPerUniTotalIngressGreenFrames, adMefPerCosPerUniTotalCountGroups=adMefPerCosPerUniTotalCountGroups, adGenAosMefPerCosPerUniTotalCountCompliances=adGenAosMefPerCosPerUniTotalCountCompliances, adGenAosMefPerUniTotalCountCompliance=adGenAosMefPerUniTotalCountCompliance, adMefPerCosPerUniTcTable=adMefPerCosPerUniTcTable, adGenAosMefPerCosPerUniTotalCountConformance=adGenAosMefPerCosPerUniTotalCountConformance, adMefPerCosPerUniTcQueueNumber=adMefPerCosPerUniTcQueueNumber, PYSNMP_MODULE_ID=adGenAosMefPerCosPerUniTotalCountMib, adMefPerCosPerUniTotalIngressGreenOctets=adMefPerCosPerUniTotalIngressGreenOctets, adMefPerCosPerUniTotalIngressYellowOctets=adMefPerCosPerUniTotalIngressYellowOctets, adMefPerCosPerUniTotalIngressRedFrames=adMefPerCosPerUniTotalIngressRedFrames, adMefPerCosPerUniTotalIngressYellowFrames=adMefPerCosPerUniTotalIngressYellowFrames, adMefPerCosPerUniTcEntry=adMefPerCosPerUniTcEntry, adGenAosMefPerCosPerUniTotalCountMib=adGenAosMefPerCosPerUniTotalCountMib, adMefPerCosPerUniTotalCountGroup=adMefPerCosPerUniTotalCountGroup, adGenAosMefPerCosPerUniTotalCount=adGenAosMefPerCosPerUniTotalCount)
