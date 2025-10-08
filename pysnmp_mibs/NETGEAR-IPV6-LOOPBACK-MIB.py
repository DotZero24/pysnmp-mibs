#
# PySNMP MIB module NETGEAR-IPV6-LOOPBACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netgear/NETGEAR-IPV6-LOOPBACK-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:28:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressPrefixLength, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength")
Ipv6AddressPrefix, = mibBuilder.importSymbols("IPV6-TC", "Ipv6AddressPrefix")
agentLoopbackID, = mibBuilder.importSymbols("NETGEAR-LOOPBACK-MIB", "agentLoopbackID")
ng7000managedswitch, = mibBuilder.importSymbols("NETGEAR-REF-MIB", "ng7000managedswitch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
fastPathIpv6Loopback = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 10, 23))
fastPathIpv6Loopback.setRevisions(('2011-01-26 00:00', '2007-05-23 00:00',))
if mibBuilder.loadTexts: fastPathIpv6Loopback.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathIpv6Loopback.setOrganization('Netgear Inc')
agentLoopbackIpv6Group = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 10, 23, 1))
agentLoopbackIpv6PrefixTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 10, 23, 1, 1), )
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixTable.setStatus('current')
agentLoopbackIpv6PrefixEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 10, 23, 1, 1, 1), ).setIndexNames((0, "NETGEAR-LOOPBACK-MIB", "agentLoopbackID"), (0, "NETGEAR-IPV6-LOOPBACK-MIB", "agentLoopbackIpv6PrefixPrefix"), (0, "NETGEAR-IPV6-LOOPBACK-MIB", "agentLoopbackIpv6PrefixPrefixLen"))
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixEntry.setStatus('current')
agentLoopbackIpv6PrefixPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 23, 1, 1, 1, 1), Ipv6AddressPrefix())
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixPrefix.setStatus('current')
agentLoopbackIpv6PrefixPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 23, 1, 1, 1, 2), InetAddressPrefixLength())
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixPrefixLen.setStatus('current')
agentLoopbackIpv6PrefixStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 23, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixStatus.setStatus('current')
mibBuilder.exportSymbols("NETGEAR-IPV6-LOOPBACK-MIB", agentLoopbackIpv6PrefixStatus=agentLoopbackIpv6PrefixStatus, PYSNMP_MODULE_ID=fastPathIpv6Loopback, agentLoopbackIpv6PrefixEntry=agentLoopbackIpv6PrefixEntry, agentLoopbackIpv6PrefixPrefixLen=agentLoopbackIpv6PrefixPrefixLen, agentLoopbackIpv6Group=agentLoopbackIpv6Group, fastPathIpv6Loopback=fastPathIpv6Loopback, agentLoopbackIpv6PrefixPrefix=agentLoopbackIpv6PrefixPrefix, agentLoopbackIpv6PrefixTable=agentLoopbackIpv6PrefixTable)
