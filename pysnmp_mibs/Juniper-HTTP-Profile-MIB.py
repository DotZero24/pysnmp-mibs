#
# PySNMP MIB module Juniper-HTTP-Profile-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/junose/Juniper-HTTP-Profile-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniSetMap, = mibBuilder.importSymbols("Juniper-TC", "JuniSetMap")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniHttpProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79))
juniHttpProfileMIB.setRevisions(('2005-08-19 14:21',))
if mibBuilder.loadTexts: juniHttpProfileMIB.setLastUpdated('200508191421Z')
if mibBuilder.loadTexts: juniHttpProfileMIB.setOrganization('Juniper Networks, Inc.')
juniHttpProfileObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1))
juniHttpProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1))
juniHttpProfileTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1), )
if mibBuilder.loadTexts: juniHttpProfileTable.setStatus('current')
juniHttpProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-HTTP-Profile-MIB", "juniHttpProfileId"))
if mibBuilder.loadTexts: juniHttpProfileEntry.setStatus('current')
juniHttpProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniHttpProfileId.setStatus('current')
juniHttpProfileSetMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1, 2), JuniSetMap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniHttpProfileSetMap.setStatus('current')
juniHttpProfileRedirectUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniHttpProfileRedirectUrl.setStatus('current')
juniHttpProfileConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4))
juniHttpProfileCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 1))
juniHttpProfileGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 2))
juniHttpProfileCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 1, 1)).setObjects(("Juniper-HTTP-Profile-MIB", "juniHttpProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHttpProfileCompliance = juniHttpProfileCompliance.setStatus('current')
juniHttpProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 2, 1)).setObjects(("Juniper-HTTP-Profile-MIB", "juniHttpProfileSetMap"), ("Juniper-HTTP-Profile-MIB", "juniHttpProfileRedirectUrl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHttpProfileGroup = juniHttpProfileGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-HTTP-Profile-MIB", juniHttpProfileSetMap=juniHttpProfileSetMap, juniHttpProfileRedirectUrl=juniHttpProfileRedirectUrl, juniHttpProfileTable=juniHttpProfileTable, juniHttpProfileConformance=juniHttpProfileConformance, juniHttpProfileCompliance=juniHttpProfileCompliance, juniHttpProfileMIB=juniHttpProfileMIB, juniHttpProfileGroup=juniHttpProfileGroup, juniHttpProfileEntry=juniHttpProfileEntry, juniHttpProfileObjects=juniHttpProfileObjects, juniHttpProfileGroups=juniHttpProfileGroups, PYSNMP_MODULE_ID=juniHttpProfileMIB, juniHttpProfile=juniHttpProfile, juniHttpProfileCompliances=juniHttpProfileCompliances, juniHttpProfileId=juniHttpProfileId)
