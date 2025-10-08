#
# PySNMP MIB module DLINKPRIME-PACKET-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINKPRIME-PACKET-MONITOR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
ifIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndexOrZero")
PortList, VlanId = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList", "VlanId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
dlinkPrimePktMonitorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 15, 10))
dlinkPrimePktMonitorMIB.setRevisions(('2014-06-03 00:00',))
if mibBuilder.loadTexts: dlinkPrimePktMonitorMIB.setLastUpdated('201406030000Z')
if mibBuilder.loadTexts: dlinkPrimePktMonitorMIB.setOrganization('D-Link Corp.')
dpPktMonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 10, 0))
dpPktMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 10, 1))
dpPktMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 10, 2))
dpPktMonDstPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 10, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpPktMonDstPort.setStatus('current')
dpPktMonMirrorType = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("disable", 0), ("rx", 1), ("tx", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpPktMonMirrorType.setStatus('current')
dpPktMonSrcPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 10, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpPktMonSrcPort.setStatus('current')
dpPktMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 10, 2, 1))
mibBuilder.exportSymbols("DLINKPRIME-PACKET-MONITOR-MIB", dpPktMonMIBCompliances=dpPktMonMIBCompliances, dpPktMonSrcPort=dpPktMonSrcPort, dpPktMonMIBConformance=dpPktMonMIBConformance, dlinkPrimePktMonitorMIB=dlinkPrimePktMonitorMIB, dpPktMonMIBObjects=dpPktMonMIBObjects, dpPktMonDstPort=dpPktMonDstPort, dpPktMonMIBNotifications=dpPktMonMIBNotifications, dpPktMonMirrorType=dpPktMonMirrorType, PYSNMP_MODULE_ID=dlinkPrimePktMonitorMIB)
