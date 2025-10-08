#
# PySNMP MIB module MX-H323-ALIASES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-H323-ALIASES-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:04 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
h323, = mibBuilder.importSymbols("MX-H323-MIB", "h323")
groupIndex, = mibBuilder.importSymbols("MX-LINE-GROUPING-MIB", "groupIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h323AliasesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15))
h323AliasesMIB.setRevisions(('1903-03-03 00:00',))
if mibBuilder.loadTexts: h323AliasesMIB.setLastUpdated('0303030000Z')
if mibBuilder.loadTexts: h323AliasesMIB.setOrganization('Mediatrix Telecom, Inc.')
h323AliasesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1))
h323AliasesConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 2))
h323AliasesIfAliasesTable = MibTable((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 5), )
if mibBuilder.loadTexts: h323AliasesIfAliasesTable.setStatus('current')
h323AliasesIfAliasesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h323AliasesIfAliasesEntry.setStatus('current')
h323AliasesGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 5, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h323AliasesGroupIndex.setStatus('current')
h323AliasesConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 5, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h323AliasesConfigured.setStatus('current')
h323AliasesCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 5, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h323AliasesCurrent.setStatus('current')
h323AliasesGroupAliasesTable = MibTable((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 10), )
if mibBuilder.loadTexts: h323AliasesGroupAliasesTable.setStatus('current')
h323AliasesGroupAliasesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 10, 1), ).setIndexNames((0, "MX-LINE-GROUPING-MIB", "groupIndex"))
if mibBuilder.loadTexts: h323AliasesGroupAliasesEntry.setStatus('current')
h323GroupAliasesConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 10, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h323GroupAliasesConfigured.setStatus('current')
h323GroupAliasesCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 10, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h323GroupAliasesCurrent.setStatus('current')
h323AliasesCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 2, 1))
h323AliasesBasicComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 2, 1, 5)).setObjects(("MX-H323-ALIASES-MIB", "h323AliasesLineAliasesGroupVer1"), ("MX-H323-ALIASES-MIB", "h323AliasesGroupAliasesGroupVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h323AliasesBasicComplVer1 = h323AliasesBasicComplVer1.setStatus('current')
h323AliasesGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 2, 2))
h323AliasesLineAliasesGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 2, 2, 5)).setObjects(("MX-H323-ALIASES-MIB", "h323AliasesConfigured"), ("MX-H323-ALIASES-MIB", "h323AliasesCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h323AliasesLineAliasesGroupVer1 = h323AliasesLineAliasesGroupVer1.setStatus('current')
h323AliasesGroupAliasesGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 2, 2, 10)).setObjects(("MX-H323-ALIASES-MIB", "h323GroupAliasesConfigured"), ("MX-H323-ALIASES-MIB", "h323GroupAliasesCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h323AliasesGroupAliasesGroupVer1 = h323AliasesGroupAliasesGroupVer1.setStatus('current')
mibBuilder.exportSymbols("MX-H323-ALIASES-MIB", h323AliasesMIB=h323AliasesMIB, h323AliasesIfAliasesTable=h323AliasesIfAliasesTable, h323AliasesCurrent=h323AliasesCurrent, h323AliasesMIBObjects=h323AliasesMIBObjects, h323AliasesCompliances=h323AliasesCompliances, h323AliasesBasicComplVer1=h323AliasesBasicComplVer1, h323AliasesGroups=h323AliasesGroups, PYSNMP_MODULE_ID=h323AliasesMIB, h323AliasesGroupAliasesGroupVer1=h323AliasesGroupAliasesGroupVer1, h323AliasesConformance=h323AliasesConformance, h323AliasesLineAliasesGroupVer1=h323AliasesLineAliasesGroupVer1, h323GroupAliasesConfigured=h323GroupAliasesConfigured, h323AliasesIfAliasesEntry=h323AliasesIfAliasesEntry, h323AliasesConfigured=h323AliasesConfigured, h323AliasesGroupAliasesTable=h323AliasesGroupAliasesTable, h323AliasesGroupIndex=h323AliasesGroupIndex, h323AliasesGroupAliasesEntry=h323AliasesGroupAliasesEntry, h323GroupAliasesCurrent=h323GroupAliasesCurrent)
