#
# PySNMP MIB module Juniper-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/junose/JUNIPER-LICENSE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:55:03 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76))
juniLicenseMIB.setRevisions(('2004-09-14 19:24',))
if mibBuilder.loadTexts: juniLicenseMIB.setLastUpdated('200409141924Z')
if mibBuilder.loadTexts: juniLicenseMIB.setOrganization('Juniper Networks, Inc.')
juniLicenseObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 1))
juniLicenseLineModuleIfLimitKey = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniLicenseLineModuleIfLimitKey.setStatus('current')
juniLicenseLineModuleIfLimitValue = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLicenseLineModuleIfLimitValue.setStatus('current')
juniLicenseMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2))
juniLicenseMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 1))
juniLicenseMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 2))
juniLicenseCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 1, 1)).setObjects(("Juniper-LICENSE-MIB", "juniLicenseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLicenseCompliance = juniLicenseCompliance.setStatus('current')
juniLicenseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 2, 1)).setObjects(("Juniper-LICENSE-MIB", "juniLicenseLineModuleIfLimitKey"), ("Juniper-LICENSE-MIB", "juniLicenseLineModuleIfLimitValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLicenseGroup = juniLicenseGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-LICENSE-MIB", juniLicenseGroup=juniLicenseGroup, juniLicenseMIBGroups=juniLicenseMIBGroups, juniLicenseCompliance=juniLicenseCompliance, juniLicenseLineModuleIfLimitKey=juniLicenseLineModuleIfLimitKey, juniLicenseLineModuleIfLimitValue=juniLicenseLineModuleIfLimitValue, PYSNMP_MODULE_ID=juniLicenseMIB, juniLicenseMIB=juniLicenseMIB, juniLicenseMIBCompliances=juniLicenseMIBCompliances, juniLicenseMIBConformance=juniLicenseMIBConformance, juniLicenseObjects=juniLicenseObjects)
