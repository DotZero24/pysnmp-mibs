#
# PySNMP MIB module Juniper-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/junose/JUNIPER-LICENSE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:31:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("Juniper-LICENSE-MIB", PYSNMP_MODULE_ID=juniLicenseMIB, juniLicenseMIBGroups=juniLicenseMIBGroups, juniLicenseMIB=juniLicenseMIB, juniLicenseMIBCompliances=juniLicenseMIBCompliances, juniLicenseLineModuleIfLimitKey=juniLicenseLineModuleIfLimitKey, juniLicenseLineModuleIfLimitValue=juniLicenseLineModuleIfLimitValue, juniLicenseObjects=juniLicenseObjects, juniLicenseCompliance=juniLicenseCompliance, juniLicenseMIBConformance=juniLicenseMIBConformance, juniLicenseGroup=juniLicenseGroup)
