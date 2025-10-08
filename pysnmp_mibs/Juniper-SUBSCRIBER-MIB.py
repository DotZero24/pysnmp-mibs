#
# PySNMP MIB module Juniper-SUBSCRIBER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/junose/JUNIPER-SUBSCRIBER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:31:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniEnable, = mibBuilder.importSymbols("Juniper-TC", "JuniEnable")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniSubscriberMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49))
juniSubscriberMIB.setRevisions(('2002-09-16 21:44', '2002-05-10 19:53', '2000-11-16 00:00',))
if mibBuilder.loadTexts: juniSubscriberMIB.setLastUpdated('200209162144Z')
if mibBuilder.loadTexts: juniSubscriberMIB.setOrganization('Juniper Networks, Inc.')
class JuniSubscrEncaps(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 19))
    namedValues = NamedValues(("ip", 0), ("bridgedEthernet", 19))

juniSubscrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1))
juniSubscrLocal = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1))
juniSubscrLocalTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1), )
if mibBuilder.loadTexts: juniSubscrLocalTable.setStatus('current')
juniSubscrLocalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-SUBSCRIBER-MIB", "juniSubscrLocalIfIndex"), (0, "Juniper-SUBSCRIBER-MIB", "juniSubscrLocalEncaps"))
if mibBuilder.loadTexts: juniSubscrLocalEntry.setStatus('current')
juniSubscrLocalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniSubscrLocalIfIndex.setStatus('current')
juniSubscrLocalEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 2), JuniSubscrEncaps())
if mibBuilder.loadTexts: juniSubscrLocalEncaps.setStatus('current')
juniSubscrLocalControl = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ok", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalControl.setStatus('current')
juniSubscrLocalNamePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 4), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalNamePrefix.setStatus('current')
juniSubscrLocalName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalName.setStatus('current')
juniSubscrLocalPasswordPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 6), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalPasswordPrefix.setStatus('current')
juniSubscrLocalPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalPassword.setStatus('current')
juniSubscrLocalDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalDomain.setStatus('current')
juniSubscrLocalAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 9), JuniEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalAuthentication.setStatus('current')
juniSubscriberMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4))
juniSubscriberMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1))
juniSubscriberMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2))
juniSubscriberCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1, 1)).setObjects(("Juniper-SUBSCRIBER-MIB", "juniSubscriberLocalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberCompliance = juniSubscriberCompliance.setStatus('obsolete')
juniSubscriberCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1, 2)).setObjects(("Juniper-SUBSCRIBER-MIB", "juniSubscriberLocalGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberCompliance2 = juniSubscriberCompliance2.setStatus('current')
juniSubscriberLocalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2, 1)).setObjects(("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalControl"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalNamePrefix"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalName"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPasswordPrefix"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPassword"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberLocalGroup = juniSubscriberLocalGroup.setStatus('obsolete')
juniSubscriberLocalGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2, 2)).setObjects(("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalControl"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalNamePrefix"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalName"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPasswordPrefix"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPassword"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalDomain"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalAuthentication"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberLocalGroup2 = juniSubscriberLocalGroup2.setStatus('current')
mibBuilder.exportSymbols("Juniper-SUBSCRIBER-MIB", juniSubscrLocalDomain=juniSubscrLocalDomain, juniSubscrLocalEntry=juniSubscrLocalEntry, juniSubscriberLocalGroup2=juniSubscriberLocalGroup2, juniSubscrLocalNamePrefix=juniSubscrLocalNamePrefix, JuniSubscrEncaps=JuniSubscrEncaps, juniSubscrLocalControl=juniSubscrLocalControl, juniSubscrLocalPasswordPrefix=juniSubscrLocalPasswordPrefix, juniSubscriberMIBConformance=juniSubscriberMIBConformance, juniSubscriberCompliance2=juniSubscriberCompliance2, juniSubscriberMIB=juniSubscriberMIB, juniSubscrLocal=juniSubscrLocal, juniSubscrLocalEncaps=juniSubscrLocalEncaps, juniSubscrLocalName=juniSubscrLocalName, juniSubscrObjects=juniSubscrObjects, juniSubscrLocalIfIndex=juniSubscrLocalIfIndex, juniSubscriberCompliance=juniSubscriberCompliance, juniSubscrLocalAuthentication=juniSubscrLocalAuthentication, juniSubscrLocalTable=juniSubscrLocalTable, PYSNMP_MODULE_ID=juniSubscriberMIB, juniSubscrLocalPassword=juniSubscrLocalPassword, juniSubscriberMIBCompliances=juniSubscriberMIBCompliances, juniSubscriberLocalGroup=juniSubscriberLocalGroup, juniSubscriberMIBGroups=juniSubscriberMIBGroups)
