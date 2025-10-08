#
# PySNMP MIB module CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:59 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "InterfaceIndexOrZero")
VlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "VlanIndex")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVlanIfTableRelationshipMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 128))
ciscoVlanIfTableRelationshipMIB.setRevisions(('2013-07-15 00:00',))
if mibBuilder.loadTexts: ciscoVlanIfTableRelationshipMIB.setLastUpdated('9904010530Z')
if mibBuilder.loadTexts: ciscoVlanIfTableRelationshipMIB.setOrganization('Cisco Systems, Inc.')
cviMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1))
cviGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1))
cviVlanInterfaceIndexTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1), )
if mibBuilder.loadTexts: cviVlanInterfaceIndexTable.setStatus('current')
cviVlanInterfaceIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviVlanId"), (0, "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviPhysicalIfIndex"))
if mibBuilder.loadTexts: cviVlanInterfaceIndexEntry.setStatus('current')
cviVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1, 1), VlanIndex())
if mibBuilder.loadTexts: cviVlanId.setStatus('current')
cviPhysicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1, 2), InterfaceIndexOrZero())
if mibBuilder.loadTexts: cviPhysicalIfIndex.setStatus('current')
cviRoutedVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cviRoutedVlanIfIndex.setStatus('current')
cviMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3))
cviMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 1))
cviMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 2))
cviMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 1, 1)).setObjects(("CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cviMIBCompliance = cviMIBCompliance.setStatus('current')
cviMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 2, 1)).setObjects(("CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviRoutedVlanIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cviMIBGroup = cviMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", cviMIBGroup=cviMIBGroup, cviMIBObjects=cviMIBObjects, cviPhysicalIfIndex=cviPhysicalIfIndex, PYSNMP_MODULE_ID=ciscoVlanIfTableRelationshipMIB, cviMIBCompliance=cviMIBCompliance, ciscoVlanIfTableRelationshipMIB=ciscoVlanIfTableRelationshipMIB, cviRoutedVlanIfIndex=cviRoutedVlanIfIndex, cviMIBCompliances=cviMIBCompliances, cviMIBGroups=cviMIBGroups, cviVlanInterfaceIndexEntry=cviVlanInterfaceIndexEntry, cviMIBConformance=cviMIBConformance, cviGlobals=cviGlobals, cviVlanId=cviVlanId, cviVlanInterfaceIndexTable=cviVlanInterfaceIndexTable)
