#
# PySNMP MIB module FS-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-LICENSE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("FS-LICENSE-MIB", PYSNMP_MODULE_ID=fsLicenseMIB, fsLicenseValue=fsLicenseValue, fsLicenseMIBCompliances=fsLicenseMIBCompliances, fsLicenseEntry=fsLicenseEntry, fsLicenseString=fsLicenseString, fsLicenseMIB=fsLicenseMIB, fsLicenseMIBCompliance=fsLicenseMIBCompliance, fsLicenseMIBObjects=fsLicenseMIBObjects, fsShowLicense=fsShowLicense, fsLicenseMIBGroups=fsLicenseMIBGroups, fsLicenseTable=fsLicenseTable, fsLicenseMIBConformance=fsLicenseMIBConformance, fsLicenseIndex=fsLicenseIndex, fsLicenseMIBGroup=fsLicenseMIBGroup)
