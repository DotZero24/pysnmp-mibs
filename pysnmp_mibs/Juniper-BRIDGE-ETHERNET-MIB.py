#
# PySNMP MIB module Juniper-BRIDGE-ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/junose/Juniper-BRIDGE-ETHERNET-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniNextIfIndex, = mibBuilder.importSymbols("Juniper-TC", "JuniNextIfIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("Juniper-BRIDGE-ETHERNET-MIB", juniBridgedEthernetIfLayer=juniBridgedEthernetIfLayer, juniBridgeEthernetConformance=juniBridgeEthernetConformance, juniBridgedEthernetIfLowerIfIndex=juniBridgedEthernetIfLowerIfIndex, juniBridgeEthernetGroups=juniBridgeEthernetGroups, juniBridgedEthernetProxyArp=juniBridgedEthernetProxyArp, juniBridgedEthernetIfEntry=juniBridgedEthernetIfEntry, juniBridgedEthernetGroup=juniBridgedEthernetGroup, juniBridgeEthernetCompliances=juniBridgeEthernetCompliances, juniBridgeEthernetMIB=juniBridgeEthernetMIB, juniBridgedEthernetIfTable=juniBridgedEthernetIfTable, juniBridgedEthernetGroup2=juniBridgedEthernetGroup2, juniBridgedEthernetCompliance=juniBridgedEthernetCompliance, juniBridgedEthernetCompliance2=juniBridgedEthernetCompliance2, juniBridgedEthernetIfMtu=juniBridgedEthernetIfMtu, juniBridgedEthernetIfRowStatus=juniBridgedEthernetIfRowStatus, juniBridgedEthernetGroup3=juniBridgedEthernetGroup3, juniBridgedEthernetObjects=juniBridgedEthernetObjects, juniBridgedEthernetIfIfIndex=juniBridgedEthernetIfIfIndex, PYSNMP_MODULE_ID=juniBridgeEthernetMIB, juniBridgedEthernetNextIfIndex=juniBridgedEthernetNextIfIndex)
