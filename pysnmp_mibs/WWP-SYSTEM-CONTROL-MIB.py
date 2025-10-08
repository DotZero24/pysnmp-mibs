#
# PySNMP MIB module WWP-SYSTEM-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/WWP-SYSTEM-CONTROL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:03 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1dStpPort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dStpPort")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("WWP-SYSTEM-CONTROL-MIB", wwpSysCtrl=wwpSysCtrl, wwpSysCtrlBridgeRSTPEnable=wwpSysCtrlBridgeRSTPEnable, wwpSysCtrlMIBCompliances=wwpSysCtrlMIBCompliances, wwpSysCtrlMIB=wwpSysCtrlMIB, wwpSysCtrlMIBObjects=wwpSysCtrlMIBObjects, PYSNMP_MODULE_ID=wwpSysCtrlMIB, wwpSysCtrlMIBGroups=wwpSysCtrlMIBGroups, wwpSysCtrlLacpEnable=wwpSysCtrlLacpEnable, wwpPvstBpduReceived=wwpPvstBpduReceived, wwpSysCtrlMIBNotifications=wwpSysCtrlMIBNotifications, wwpSysCtrlMIBNotificationPrefix=wwpSysCtrlMIBNotificationPrefix, wwpSysCtrlMIBConformance=wwpSysCtrlMIBConformance)
