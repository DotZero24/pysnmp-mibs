#
# PySNMP MIB module Juniper-AUTOCONFIGURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/junose/Juniper-AUTOCONFIGURE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:04 2025
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
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
juniAutoConfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48))
juniAutoConfMIB.setRevisions(('2004-07-26 19:54', '2002-11-22 16:08', '2002-11-22 15:24', '2000-11-16 00:00',))
if mibBuilder.loadTexts: juniAutoConfMIB.setLastUpdated('200407261954Z')
if mibBuilder.loadTexts: juniAutoConfMIB.setOrganization('Juniper Networks')
class JuniAutoConfEncaps(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 17, 19))
    namedValues = NamedValues(("ip", 0), ("ppp", 1), ("pppoe", 17), ("bridgedEthernet", 19))

juniAutoConfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1))
juniAutoConf = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1))
juniAutoConfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1), )
if mibBuilder.loadTexts: juniAutoConfTable.setStatus('current')
juniAutoConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-AUTOCONFIGURE-MIB", "juniAutoConfIfIndex"), (0, "Juniper-AUTOCONFIGURE-MIB", "juniAutoConfEncaps"))
if mibBuilder.loadTexts: juniAutoConfEntry.setStatus('current')
juniAutoConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniAutoConfIfIndex.setStatus('current')
juniAutoConfEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 2), JuniAutoConfEncaps())
if mibBuilder.loadTexts: juniAutoConfEncaps.setStatus('current')
juniAutoConfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 3), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAutoConfEnable.setStatus('current')
juniAutoConfLockoutSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAutoConfLockoutSupported.setStatus('current')
juniAutoConfLockoutMin = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAutoConfLockoutMin.setStatus('current')
juniAutoConfLockoutMax = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAutoConfLockoutMax.setStatus('current')
juniAutoConfLockoutTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAutoConfLockoutTime.setStatus('current')
juniAutoConfLockoutElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAutoConfLockoutElapsedTime.setStatus('current')
juniAutoConfNextLockoutTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAutoConfNextLockoutTime.setStatus('current')
juniAutoConfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4))
juniAutoConfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1))
juniAutoConfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2))
juniAutoConfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1, 1)).setObjects(("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfCompliance = juniAutoConfCompliance.setStatus('obsolete')
juniAutoConfCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1, 2)).setObjects(("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfCompliance2 = juniAutoConfCompliance2.setStatus('current')
juniAutoConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2, 1)).setObjects(("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfGroup = juniAutoConfGroup.setStatus('obsolete')
juniAutoConfGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2, 2)).setObjects(("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutSupported"), ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutMin"), ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutMax"), ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutTime"), ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutElapsedTime"), ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfNextLockoutTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfGroup2 = juniAutoConfGroup2.setStatus('current')
mibBuilder.exportSymbols("Juniper-AUTOCONFIGURE-MIB", juniAutoConfLockoutElapsedTime=juniAutoConfLockoutElapsedTime, juniAutoConfIfIndex=juniAutoConfIfIndex, juniAutoConfMIBCompliances=juniAutoConfMIBCompliances, juniAutoConfEnable=juniAutoConfEnable, juniAutoConfMIBConformance=juniAutoConfMIBConformance, juniAutoConfLockoutMin=juniAutoConfLockoutMin, PYSNMP_MODULE_ID=juniAutoConfMIB, juniAutoConfGroup=juniAutoConfGroup, juniAutoConfLockoutTime=juniAutoConfLockoutTime, juniAutoConfLockoutMax=juniAutoConfLockoutMax, juniAutoConfObjects=juniAutoConfObjects, juniAutoConfEncaps=juniAutoConfEncaps, juniAutoConfEntry=juniAutoConfEntry, juniAutoConfMIBGroups=juniAutoConfMIBGroups, juniAutoConfLockoutSupported=juniAutoConfLockoutSupported, juniAutoConf=juniAutoConf, juniAutoConfTable=juniAutoConfTable, juniAutoConfCompliance=juniAutoConfCompliance, juniAutoConfNextLockoutTime=juniAutoConfNextLockoutTime, JuniAutoConfEncaps=JuniAutoConfEncaps, juniAutoConfMIB=juniAutoConfMIB, juniAutoConfCompliance2=juniAutoConfCompliance2, juniAutoConfGroup2=juniAutoConfGroup2)
