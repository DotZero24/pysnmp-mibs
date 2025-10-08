#
# PySNMP MIB module WWP-SYSTEM-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/WWP-SYSTEM-CONTROL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1dStpPort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dStpPort")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpSysCtrlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 30))
wwpSysCtrlMIB.setRevisions(('2001-04-03 17:00',))
if mibBuilder.loadTexts: wwpSysCtrlMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpSysCtrlMIB.setOrganization('World Wide Packets, Inc')
wwpSysCtrlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 1))
wwpSysCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 1, 1))
wwpSysCtrlMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 2))
wwpSysCtrlMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 2, 0))
wwpSysCtrlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 3))
wwpSysCtrlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 3, 1))
wwpSysCtrlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 3, 2))
wwpSysCtrlBridgeRSTPEnable = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 30, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpSysCtrlBridgeRSTPEnable.setStatus('current')
wwpSysCtrlLacpEnable = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 30, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpSysCtrlLacpEnable.setStatus('current')
wwpPvstBpduReceived = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 30, 2, 0, 1)).setObjects(("BRIDGE-MIB", "dot1dStpPort"))
if mibBuilder.loadTexts: wwpPvstBpduReceived.setStatus('current')
mibBuilder.exportSymbols("WWP-SYSTEM-CONTROL-MIB", wwpSysCtrlMIBCompliances=wwpSysCtrlMIBCompliances, wwpSysCtrlMIBGroups=wwpSysCtrlMIBGroups, wwpSysCtrl=wwpSysCtrl, PYSNMP_MODULE_ID=wwpSysCtrlMIB, wwpSysCtrlMIBObjects=wwpSysCtrlMIBObjects, wwpSysCtrlLacpEnable=wwpSysCtrlLacpEnable, wwpSysCtrlMIB=wwpSysCtrlMIB, wwpSysCtrlMIBConformance=wwpSysCtrlMIBConformance, wwpSysCtrlMIBNotifications=wwpSysCtrlMIBNotifications, wwpSysCtrlMIBNotificationPrefix=wwpSysCtrlMIBNotificationPrefix, wwpSysCtrlBridgeRSTPEnable=wwpSysCtrlBridgeRSTPEnable, wwpPvstBpduReceived=wwpPvstBpduReceived)
