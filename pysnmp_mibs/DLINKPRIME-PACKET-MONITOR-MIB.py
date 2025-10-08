#
# PySNMP MIB module DLINKPRIME-PACKET-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINKPRIME-PACKET-MONITOR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:14 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
PortList, VlanId = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList", "VlanId")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DLINKPRIME-PACKET-MONITOR-MIB", dpPktMonMIBNotifications=dpPktMonMIBNotifications, dpPktMonMIBConformance=dpPktMonMIBConformance, dpPktMonMirrorType=dpPktMonMirrorType, dpPktMonMIBObjects=dpPktMonMIBObjects, dpPktMonMIBCompliances=dpPktMonMIBCompliances, dpPktMonDstPort=dpPktMonDstPort, dlinkPrimePktMonitorMIB=dlinkPrimePktMonitorMIB, PYSNMP_MODULE_ID=dlinkPrimePktMonitorMIB, dpPktMonSrcPort=dpPktMonSrcPort)
