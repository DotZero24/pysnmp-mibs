#
# PySNMP MIB module CISCO-VLAN-BRIDGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-VLAN-BRIDGING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoPortList, = mibBuilder.importSymbols("CISCO-TC", "CiscoPortList")
vtpVlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "vtpVlanIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVlanBridgingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 56))
ciscoVlanBridgingMIB.setRevisions(('2003-08-22 00:00', '1996-09-12 00:00',))
if mibBuilder.loadTexts: ciscoVlanBridgingMIB.setLastUpdated('200308220000Z')
if mibBuilder.loadTexts: ciscoVlanBridgingMIB.setOrganization('Cisco Systems, Inc.')
ciscoVlanBridgingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 56, 1))
cvbStp = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1))
cvbStpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1), )
if mibBuilder.loadTexts: cvbStpTable.setStatus('current')
cvbStpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VTP-MIB", "vtpVlanIndex"))
if mibBuilder.loadTexts: cvbStpEntry.setStatus('current')
cvbStpForwardingMap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvbStpForwardingMap.setStatus('deprecated')
cvbStpForwardingMap2k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1, 1, 3), CiscoPortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvbStpForwardingMap2k.setStatus('current')
ciscoVlanBridgingMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 56, 3))
ciscoVlanBridgingMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 1))
ciscoVlanBridgingMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 2))
ciscoVlanBridgingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 1, 1)).setObjects(("CISCO-VLAN-BRIDGING-MIB", "ciscoVlanBridgingMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanBridgingMIBCompliance = ciscoVlanBridgingMIBCompliance.setStatus('deprecated')
ciscoVlanBridgingMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 1, 2)).setObjects(("CISCO-VLAN-BRIDGING-MIB", "ciscoVlanBridgingMIBGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanBridgingMIBCompliance2 = ciscoVlanBridgingMIBCompliance2.setStatus('current')
ciscoVlanBridgingMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 2, 1)).setObjects(("CISCO-VLAN-BRIDGING-MIB", "cvbStpForwardingMap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanBridgingMIBGroup = ciscoVlanBridgingMIBGroup.setStatus('deprecated')
ciscoVlanBridgingMIBGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 2, 2)).setObjects(("CISCO-VLAN-BRIDGING-MIB", "cvbStpForwardingMap2k"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanBridgingMIBGroup2 = ciscoVlanBridgingMIBGroup2.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-BRIDGING-MIB", cvbStp=cvbStp, cvbStpEntry=cvbStpEntry, cvbStpForwardingMap=cvbStpForwardingMap, cvbStpForwardingMap2k=cvbStpForwardingMap2k, ciscoVlanBridgingMIBGroups=ciscoVlanBridgingMIBGroups, ciscoVlanBridgingMIBCompliances=ciscoVlanBridgingMIBCompliances, ciscoVlanBridgingMIBCompliance2=ciscoVlanBridgingMIBCompliance2, PYSNMP_MODULE_ID=ciscoVlanBridgingMIB, ciscoVlanBridgingMIBConformance=ciscoVlanBridgingMIBConformance, ciscoVlanBridgingMIBCompliance=ciscoVlanBridgingMIBCompliance, cvbStpTable=cvbStpTable, ciscoVlanBridgingMIBObjects=ciscoVlanBridgingMIBObjects, ciscoVlanBridgingMIBGroup=ciscoVlanBridgingMIBGroup, ciscoVlanBridgingMIBGroup2=ciscoVlanBridgingMIBGroup2, ciscoVlanBridgingMIB=ciscoVlanBridgingMIB)
