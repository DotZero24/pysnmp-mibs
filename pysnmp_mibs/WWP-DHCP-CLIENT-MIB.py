#
# PySNMP MIB module WWP-DHCP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/WWP-DHCP-CLIENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpDhcpClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 18))
wwpDhcpClientMIB.setRevisions(('2001-04-03 17:00',))
if mibBuilder.loadTexts: wwpDhcpClientMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpDhcpClientMIB.setOrganization('World Wide Packets, Inc')
wwpDhcpClientMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 18, 1))
wwpDhcpClient = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 18, 1, 1))
wwpDhcpClientMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 18, 2))
wwpDhcpClientMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 18, 2, 0))
wwpDhcpClientMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 18, 3))
wwpDhcpClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 18, 3, 1))
wwpDhcpClientMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 18, 3, 2))
wwpDhcpActivate = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 18, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpDhcpActivate.setStatus('current')
wwpDhcpIfName = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 18, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('mgmt')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpDhcpIfName.setStatus('current')
wwpDhcpDiscoveryMsgInterval = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 18, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(125)).setUnits('miliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpDhcpDiscoveryMsgInterval.setStatus('current')
wwpDhcpLeaseTime = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 18, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(24)).setUnits('Hours').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpDhcpLeaseTime.setStatus('current')
mibBuilder.exportSymbols("WWP-DHCP-CLIENT-MIB", wwpDhcpDiscoveryMsgInterval=wwpDhcpDiscoveryMsgInterval, wwpDhcpIfName=wwpDhcpIfName, wwpDhcpClientMIBCompliances=wwpDhcpClientMIBCompliances, wwpDhcpClientMIBNotifications=wwpDhcpClientMIBNotifications, PYSNMP_MODULE_ID=wwpDhcpClientMIB, wwpDhcpClientMIB=wwpDhcpClientMIB, wwpDhcpClientMIBGroups=wwpDhcpClientMIBGroups, wwpDhcpClientMIBConformance=wwpDhcpClientMIBConformance, wwpDhcpActivate=wwpDhcpActivate, wwpDhcpClient=wwpDhcpClient, wwpDhcpLeaseTime=wwpDhcpLeaseTime, wwpDhcpClientMIBObjects=wwpDhcpClientMIBObjects, wwpDhcpClientMIBNotificationPrefix=wwpDhcpClientMIBNotificationPrefix)
