#
# PySNMP MIB module NETSCREEN-SET-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netscreen/NETSCREEN-SET-DHCP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
netscreenSetting, netscreenSettingMibModule = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSetting", "netscreenSettingMibModule")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netscreenSetDhcpMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 7, 0, 5))
netscreenSetDhcpMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-10 00:00', '2001-12-12 00:00', '2001-09-28 00:00', '2001-05-27 00:00',))
if mibBuilder.loadTexts: netscreenSetDhcpMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenSetDhcpMibModule.setOrganization('Juniper Networks, Inc.')
nsSetDHCP = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 5))
nsSetDhcpTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 7, 5, 1), )
if mibBuilder.loadTexts: nsSetDhcpTable.setStatus('current')
nsSetDhcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1), ).setIndexNames((0, "NETSCREEN-SET-DHCP-MIB", "nsSetDhcpIfIdx"))
if mibBuilder.loadTexts: nsSetDhcpEntry.setStatus('current')
nsSetDhcpIfIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetDhcpIfIdx.setStatus('current')
nsSetDHCPService = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("dhcp-relay-agent", 1), ("dhcp-server", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetDHCPService.setStatus('current')
nsSetDHCPRelayServer = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetDHCPRelayServer.setStatus('current')
nsSetDHCPVpnEncryp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetDHCPVpnEncryp.setStatus('current')
nsSetDhcpIfInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetDhcpIfInfo.setStatus('current')
mibBuilder.exportSymbols("NETSCREEN-SET-DHCP-MIB", nsSetDHCPRelayServer=nsSetDHCPRelayServer, nsSetDHCP=nsSetDHCP, PYSNMP_MODULE_ID=netscreenSetDhcpMibModule, nsSetDhcpEntry=nsSetDhcpEntry, nsSetDHCPVpnEncryp=nsSetDHCPVpnEncryp, nsSetDhcpIfInfo=nsSetDhcpIfInfo, nsSetDhcpIfIdx=nsSetDhcpIfIdx, nsSetDHCPService=nsSetDHCPService, netscreenSetDhcpMibModule=netscreenSetDhcpMibModule, nsSetDhcpTable=nsSetDhcpTable)
