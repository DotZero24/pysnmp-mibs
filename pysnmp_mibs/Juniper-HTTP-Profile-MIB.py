#
# PySNMP MIB module Juniper-HTTP-Profile-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/junose/Juniper-HTTP-Profile-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniSetMap, = mibBuilder.importSymbols("Juniper-TC", "JuniSetMap")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("Juniper-HTTP-Profile-MIB", juniHttpProfileRedirectUrl=juniHttpProfileRedirectUrl, juniHttpProfileId=juniHttpProfileId, juniHttpProfileGroup=juniHttpProfileGroup, juniHttpProfileMIB=juniHttpProfileMIB, juniHttpProfileObjects=juniHttpProfileObjects, juniHttpProfileEntry=juniHttpProfileEntry, PYSNMP_MODULE_ID=juniHttpProfileMIB, juniHttpProfileCompliance=juniHttpProfileCompliance, juniHttpProfileSetMap=juniHttpProfileSetMap, juniHttpProfileTable=juniHttpProfileTable, juniHttpProfileConformance=juniHttpProfileConformance, juniHttpProfileCompliances=juniHttpProfileCompliances, juniHttpProfile=juniHttpProfile, juniHttpProfileGroups=juniHttpProfileGroups)
