#
# PySNMP MIB module Juniper-BRIDGE-ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/junose/Juniper-BRIDGE-ETHERNET-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniNextIfIndex, = mibBuilder.importSymbols("Juniper-TC", "JuniNextIfIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
juniBridgeEthernetMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31))
juniBridgeEthernetMIB.setRevisions(('2005-12-14 17:10', '2002-09-16 21:44', '2000-09-26 14:43', '2000-03-27 23:45', '1999-12-10 18:30',))
if mibBuilder.loadTexts: juniBridgeEthernetMIB.setLastUpdated('200512141710Z')
if mibBuilder.loadTexts: juniBridgeEthernetMIB.setOrganization('Juniper Networks, Inc.')
juniBridgedEthernetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1))
juniBridgedEthernetIfLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1))
juniBridgedEthernetNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 1), JuniNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniBridgedEthernetNextIfIndex.setStatus('current')
juniBridgedEthernetIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2), )
if mibBuilder.loadTexts: juniBridgedEthernetIfTable.setStatus('current')
juniBridgedEthernetIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1), ).setIndexNames((0, "Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfIfIndex"))
if mibBuilder.loadTexts: juniBridgedEthernetIfEntry.setStatus('current')
juniBridgedEthernetIfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniBridgedEthernetIfIfIndex.setStatus('current')
juniBridgedEthernetProxyArp = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enableRestricted", 1), ("enableUnrestricted", 2), ("disable", 3))).clone('enableRestricted')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgedEthernetProxyArp.setStatus('obsolete')
juniBridgedEthernetIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgedEthernetIfLowerIfIndex.setStatus('current')
juniBridgedEthernetIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgedEthernetIfRowStatus.setStatus('current')
juniBridgedEthernetIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 9180)).clone(1518)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgedEthernetIfMtu.setStatus('current')
juniBridgeEthernetConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4))
juniBridgeEthernetCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 1))
juniBridgeEthernetGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 2))
juniBridgedEthernetCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 1, 1)).setObjects(("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgedEthernetCompliance = juniBridgedEthernetCompliance.setStatus('deprecated')
juniBridgedEthernetCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 1, 2)).setObjects(("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgedEthernetCompliance2 = juniBridgedEthernetCompliance2.setStatus('current')
juniBridgedEthernetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 2, 1)).setObjects(("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetNextIfIndex"), ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfIfIndex"), ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetProxyArp"), ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfLowerIfIndex"), ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgedEthernetGroup = juniBridgedEthernetGroup.setStatus('obsolete')
juniBridgedEthernetGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 2, 2)).setObjects(("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetNextIfIndex"), ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfIfIndex"), ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfLowerIfIndex"), ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgedEthernetGroup2 = juniBridgedEthernetGroup2.setStatus('deprecated')
juniBridgedEthernetGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 2, 3)).setObjects(("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetNextIfIndex"), ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfIfIndex"), ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfLowerIfIndex"), ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfRowStatus"), ("Juniper-BRIDGE-ETHERNET-MIB", "juniBridgedEthernetIfMtu"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgedEthernetGroup3 = juniBridgedEthernetGroup3.setStatus('current')
mibBuilder.exportSymbols("Juniper-BRIDGE-ETHERNET-MIB", juniBridgedEthernetGroup3=juniBridgedEthernetGroup3, juniBridgedEthernetCompliance=juniBridgedEthernetCompliance, juniBridgeEthernetCompliances=juniBridgeEthernetCompliances, juniBridgedEthernetProxyArp=juniBridgedEthernetProxyArp, juniBridgedEthernetNextIfIndex=juniBridgedEthernetNextIfIndex, juniBridgedEthernetIfEntry=juniBridgedEthernetIfEntry, juniBridgedEthernetIfLayer=juniBridgedEthernetIfLayer, juniBridgedEthernetIfLowerIfIndex=juniBridgedEthernetIfLowerIfIndex, juniBridgedEthernetObjects=juniBridgedEthernetObjects, juniBridgedEthernetIfIfIndex=juniBridgedEthernetIfIfIndex, juniBridgedEthernetIfRowStatus=juniBridgedEthernetIfRowStatus, juniBridgedEthernetCompliance2=juniBridgedEthernetCompliance2, juniBridgeEthernetConformance=juniBridgeEthernetConformance, juniBridgeEthernetMIB=juniBridgeEthernetMIB, juniBridgedEthernetGroup=juniBridgedEthernetGroup, PYSNMP_MODULE_ID=juniBridgeEthernetMIB, juniBridgeEthernetGroups=juniBridgeEthernetGroups, juniBridgedEthernetIfTable=juniBridgedEthernetIfTable, juniBridgedEthernetIfMtu=juniBridgedEthernetIfMtu, juniBridgedEthernetGroup2=juniBridgedEthernetGroup2)
