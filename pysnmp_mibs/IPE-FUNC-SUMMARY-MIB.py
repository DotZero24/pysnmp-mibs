#
# PySNMP MIB module IPE-FUNC-SUMMARY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nec/IPE-FUNC-SUMMARY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:45 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Opaque, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Opaque", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
nec = MibIdentifier((1, 3, 6, 1, 4, 1, 119))
nec_mib = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2)).setLabel("nec-mib")
necProductDepend = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3))
radioEquipment = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3, 69))
pasoNeoIpe_common = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501)).setLabel("pasoNeoIpe-common")
summaryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1))
maintSummaryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1, 2))
maintFuncSummaryTable = MibTable((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1, 2, 2), )
if mibBuilder.loadTexts: maintFuncSummaryTable.setStatus('current')
maintFuncSummaryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1, 2, 2, 1), ).setIndexNames((0, "IPE-FUNC-SUMMARY-MIB", "maintFuncSummaryCategory"))
if mibBuilder.loadTexts: maintFuncSummaryEntry.setStatus('current')
maintFuncSummaryCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17))).clone(namedValues=NamedValues(("modemLb", 1), ("modemMaint", 2), ("modemSwgMaint", 3), ("e1Lb1", 4), ("e1Lb2", 5), ("stm1Lb1", 6), ("stm1Lb2", 7), ("sncpControl", 8), ("timingSourceControl", 9), ("laserShutdownControl", 10), ("fileUpdate", 11), ("etherring", 12), ("aps", 13), ("dot3ah", 14), ("modemL2Lb1", 16), ("modemL2Lb2", 17))))
if mibBuilder.loadTexts: maintFuncSummaryCategory.setStatus('current')
maintFuncSummaryNEAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1, 2, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: maintFuncSummaryNEAddress.setStatus('current')
maintFuncSummary = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("invalid", 0), ("none", 1), ("executed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: maintFuncSummary.setStatus('current')
maintFuncSummaryLastUpdated = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1, 2, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maintFuncSummaryLastUpdated.setStatus('current')
mibBuilder.exportSymbols("IPE-FUNC-SUMMARY-MIB", maintFuncSummaryCategory=maintFuncSummaryCategory, necProductDepend=necProductDepend, maintSummaryGroup=maintSummaryGroup, summaryGroup=summaryGroup, maintFuncSummary=maintFuncSummary, nec_mib=nec_mib, radioEquipment=radioEquipment, pasoNeoIpe_common=pasoNeoIpe_common, maintFuncSummaryTable=maintFuncSummaryTable, maintFuncSummaryNEAddress=maintFuncSummaryNEAddress, maintFuncSummaryLastUpdated=maintFuncSummaryLastUpdated, nec=nec, maintFuncSummaryEntry=maintFuncSummaryEntry)
