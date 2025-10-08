#
# PySNMP MIB module WWP-DHCP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/WWP-DHCP-CLIENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("WWP-DHCP-CLIENT-MIB", wwpDhcpClientMIBNotificationPrefix=wwpDhcpClientMIBNotificationPrefix, wwpDhcpClientMIBCompliances=wwpDhcpClientMIBCompliances, wwpDhcpClientMIBObjects=wwpDhcpClientMIBObjects, wwpDhcpIfName=wwpDhcpIfName, wwpDhcpActivate=wwpDhcpActivate, wwpDhcpClientMIBConformance=wwpDhcpClientMIBConformance, wwpDhcpClientMIB=wwpDhcpClientMIB, wwpDhcpLeaseTime=wwpDhcpLeaseTime, wwpDhcpClientMIBGroups=wwpDhcpClientMIBGroups, wwpDhcpClient=wwpDhcpClient, PYSNMP_MODULE_ID=wwpDhcpClientMIB, wwpDhcpClientMIBNotifications=wwpDhcpClientMIBNotifications, wwpDhcpDiscoveryMsgInterval=wwpDhcpDiscoveryMsgInterval)
