#
# PySNMP MIB module CISCO-VLAN-BRIDGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-VLAN-BRIDGING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:26:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoPortList, = mibBuilder.importSymbols("CISCO-TC", "CiscoPortList")
vtpVlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "vtpVlanIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-VLAN-BRIDGING-MIB", PYSNMP_MODULE_ID=ciscoVlanBridgingMIB, cvbStpForwardingMap2k=cvbStpForwardingMap2k, ciscoVlanBridgingMIBCompliance=ciscoVlanBridgingMIBCompliance, ciscoVlanBridgingMIB=ciscoVlanBridgingMIB, ciscoVlanBridgingMIBCompliances=ciscoVlanBridgingMIBCompliances, ciscoVlanBridgingMIBObjects=ciscoVlanBridgingMIBObjects, cvbStpForwardingMap=cvbStpForwardingMap, ciscoVlanBridgingMIBGroups=ciscoVlanBridgingMIBGroups, ciscoVlanBridgingMIBGroup=ciscoVlanBridgingMIBGroup, cvbStp=cvbStp, ciscoVlanBridgingMIBCompliance2=ciscoVlanBridgingMIBCompliance2, ciscoVlanBridgingMIBConformance=ciscoVlanBridgingMIBConformance, ciscoVlanBridgingMIBGroup2=ciscoVlanBridgingMIBGroup2, cvbStpEntry=cvbStpEntry, cvbStpTable=cvbStpTable)
