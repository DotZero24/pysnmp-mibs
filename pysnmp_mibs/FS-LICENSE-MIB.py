#
# PySNMP MIB module FS-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-LICENSE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fsLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57))
fsLicenseMIB.setRevisions(('2009-09-18 00:00',))
if mibBuilder.loadTexts: fsLicenseMIB.setLastUpdated('200909180000Z')
if mibBuilder.loadTexts: fsLicenseMIB.setOrganization('FS.COM Inc..')
fsLicenseMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 1))
fsShowLicense = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsShowLicense.setStatus('current')
fsLicenseTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 1, 2), )
if mibBuilder.loadTexts: fsLicenseTable.setStatus('current')
fsLicenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 1, 2, 1), ).setIndexNames((0, "FS-LICENSE-MIB", "fsLicenseIndex"))
if mibBuilder.loadTexts: fsLicenseEntry.setStatus('current')
fsLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: fsLicenseIndex.setStatus('current')
fsLicenseString = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 1, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsLicenseString.setStatus('current')
fsLicenseValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsLicenseValue.setStatus('current')
fsLicenseMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 2))
fsLicenseMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 2, 1))
fsLicenseMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 2, 2))
fsLicenseMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 2, 1, 1)).setObjects(("FS-LICENSE-MIB", "fsLicenseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsLicenseMIBCompliance = fsLicenseMIBCompliance.setStatus('current')
fsLicenseMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 2, 2, 1)).setObjects(("FS-LICENSE-MIB", "fsShowLicense"), ("FS-LICENSE-MIB", "fsLicenseString"), ("FS-LICENSE-MIB", "fsLicenseValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsLicenseMIBGroup = fsLicenseMIBGroup.setStatus('current')
mibBuilder.exportSymbols("FS-LICENSE-MIB", fsLicenseMIBObjects=fsLicenseMIBObjects, fsLicenseMIBConformance=fsLicenseMIBConformance, fsLicenseMIBCompliances=fsLicenseMIBCompliances, PYSNMP_MODULE_ID=fsLicenseMIB, fsShowLicense=fsShowLicense, fsLicenseEntry=fsLicenseEntry, fsLicenseMIBGroups=fsLicenseMIBGroups, fsLicenseMIBCompliance=fsLicenseMIBCompliance, fsLicenseMIBGroup=fsLicenseMIBGroup, fsLicenseValue=fsLicenseValue, fsLicenseIndex=fsLicenseIndex, fsLicenseTable=fsLicenseTable, fsLicenseMIB=fsLicenseMIB, fsLicenseString=fsLicenseString)
