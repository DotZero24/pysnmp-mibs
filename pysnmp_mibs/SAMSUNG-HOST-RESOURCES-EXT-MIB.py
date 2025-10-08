#
# PySNMP MIB module SAMSUNG-HOST-RESOURCES-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/samsung/SAMSUNG-HOST-RESOURCES-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:19:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hrDeviceIndex, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrDeviceIndex")
samsungCommonMIB, = mibBuilder.importSymbols("SAMSUNG-COMMON-MIB", "samsungCommonMIB")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
scmHrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53))
if mibBuilder.loadTexts: scmHrMIB.setLastUpdated('190407170000Z')
if mibBuilder.loadTexts: scmHrMIB.setOrganization('Samsung Corporation - SCMI Working Group')
class ScmHrDevCountJobTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 11, 12, 21))
    namedValues = NamedValues(("print", 1), ("copy", 2), ("faxIn", 3), ("faxOut", 4), ("scan", 5), ("report", 6), ("digitalSend", 11), ("digitalRecieve", 12), ("localStorage", 21))

class ScmHrDevCountMediaSizeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32))
    namedValues = NamedValues(("small", 1), ("large", 2), ("letter", 3), ("legal", 4), ("a4", 5), ("executive", 6), ("jisB5", 7), ("isoB5", 8), ("com10", 9), ("monarch", 10), ("dl", 11), ("c5", 12), ("postA6", 13), ("c6", 14), ("folio", 15), ("a5", 16), ("statement", 17), ("a6", 18), ("ledger", 19), ("a3", 20), ("jisB4", 21), ("jpost", 22), ("jpostd", 23), ("custom", 24), ("letterP", 25), ("a4P", 26), ("jisB5P", 27), ("a5P", 28), ("executiveP", 29), ("statementP", 30), ("a3Over", 31), ("b5Envelope", 32))

class ScmHrDevCountUnitTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("tenThousandthsOfInches", 3), ("micrometers", 4), ("impressions", 7), ("sheets", 8), ("hours", 11), ("thousandthsOfOunces", 12), ("tenthsOfGrams", 13), ("hundrethsOfFluidOunces", 14), ("tenthsOfMilliliters", 15), ("feet", 16), ("meters", 17), ("items", 18), ("percent", 19))

class ScmHrDevCountDuplexTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("simplex", 1), ("duplex", 2), ("duplexSingle", 3))

class ScmHrDevCountColorTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("fullColor", 1), ("singleColor", 2), ("monoColor", 3))

scmHrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 2))
scmHrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 2, 2))
scmHrDevInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 2, 2, 3)).setObjects(("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountIndex"), ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountJobType"), ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountMediaSize"), ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountUnit"), ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountDuplex"), ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountColor"), ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    scmHrDevInfoGroup = scmHrDevInfoGroup.setStatus('current')
scmHrDevCount = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11))
scmHrDevCountSimple = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 1))
scmHrDevCountTable = MibTable((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2), )
if mibBuilder.loadTexts: scmHrDevCountTable.setStatus('current')
scmHrDevCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountIndex"))
if mibBuilder.loadTexts: scmHrDevCountEntry.setStatus('current')
scmHrDevCountIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmHrDevCountIndex.setStatus('current')
scmHrDevCountJobType = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 2), ScmHrDevCountJobTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmHrDevCountJobType.setStatus('current')
scmHrDevCountMediaSize = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 3), ScmHrDevCountMediaSizeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmHrDevCountMediaSize.setStatus('current')
scmHrDevCountUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 4), ScmHrDevCountUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmHrDevCountUnit.setStatus('current')
scmHrDevCountDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 5), ScmHrDevCountDuplexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmHrDevCountDuplex.setStatus('current')
scmHrDevCountColor = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 6), ScmHrDevCountColorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmHrDevCountColor.setStatus('current')
scmHrDevCountValue = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmHrDevCountValue.setStatus('current')
mibBuilder.exportSymbols("SAMSUNG-HOST-RESOURCES-EXT-MIB", scmHrDevCountTable=scmHrDevCountTable, scmHrDevCountDuplex=scmHrDevCountDuplex, ScmHrDevCountMediaSizeTC=ScmHrDevCountMediaSizeTC, scmHrDevCountUnit=scmHrDevCountUnit, PYSNMP_MODULE_ID=scmHrMIB, scmHrDevCountValue=scmHrDevCountValue, scmHrDevCountEntry=scmHrDevCountEntry, scmHrDevCountMediaSize=scmHrDevCountMediaSize, scmHrDevCountColor=scmHrDevCountColor, scmHrMIBGroups=scmHrMIBGroups, scmHrDevCountIndex=scmHrDevCountIndex, scmHrDevCount=scmHrDevCount, ScmHrDevCountJobTypeTC=ScmHrDevCountJobTypeTC, scmHrMIB=scmHrMIB, scmHrDevCountSimple=scmHrDevCountSimple, scmHrDevCountJobType=scmHrDevCountJobType, scmHrDevInfoGroup=scmHrDevInfoGroup, scmHrMIBConformance=scmHrMIBConformance, ScmHrDevCountUnitTC=ScmHrDevCountUnitTC, ScmHrDevCountDuplexTC=ScmHrDevCountDuplexTC, ScmHrDevCountColorTC=ScmHrDevCountColorTC)
