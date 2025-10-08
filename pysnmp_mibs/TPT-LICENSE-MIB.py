#
# PySNMP MIB module TPT-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trendmicro/TPT-LICENSE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_tpa_objs, = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs")
tpt_license_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15)).setLabel("tpt-license-objs")
tpt_license_objs.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_license_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_license_objs.setOrganization('Trend Micro, Inc.')
class LicenseStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("info", 0), ("ok", 1), ("warning", 2), ("error", 3))

class LicenseAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("allow", 0), ("deny", 1))

licenseTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1), )
if mibBuilder.loadTexts: licenseTable.setStatus('current')
licenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1), ).setIndexNames((0, "TPT-LICENSE-MIB", "licenseEntryIndex"))
if mibBuilder.loadTexts: licenseEntry.setStatus('current')
licenseEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: licenseEntryIndex.setStatus('current')
licenseEntryFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseEntryFeature.setStatus('current')
licenseEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 3), LicenseStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseEntryStatus.setStatus('current')
licenseEntryAction = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 4), LicenseAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseEntryAction.setStatus('current')
licenseEntryExpiry = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseEntryExpiry.setStatus('current')
licenseEntryDetails = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseEntryDetails.setStatus('current')
mibBuilder.exportSymbols("TPT-LICENSE-MIB", PYSNMP_MODULE_ID=tpt_license_objs, licenseEntryFeature=licenseEntryFeature, licenseEntryExpiry=licenseEntryExpiry, licenseEntryDetails=licenseEntryDetails, licenseEntryIndex=licenseEntryIndex, licenseEntry=licenseEntry, LicenseStatus=LicenseStatus, licenseEntryStatus=licenseEntryStatus, tpt_license_objs=tpt_license_objs, LicenseAction=LicenseAction, licenseTable=licenseTable, licenseEntryAction=licenseEntryAction)
