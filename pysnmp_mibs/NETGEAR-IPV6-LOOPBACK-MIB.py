#
# PySNMP MIB module NETGEAR-IPV6-LOOPBACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netgear/NETGEAR-IPV6-LOOPBACK-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:51:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressPrefixLength, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength")
Ipv6AddressPrefix, = mibBuilder.importSymbols("IPV6-TC", "Ipv6AddressPrefix")
agentLoopbackID, = mibBuilder.importSymbols("NETGEAR-LOOPBACK-MIB", "agentLoopbackID")
ng7000managedswitch, = mibBuilder.importSymbols("NETGEAR-REF-MIB", "ng7000managedswitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NETGEAR-IPV6-LOOPBACK-MIB", fastPathIpv6Loopback=fastPathIpv6Loopback, agentLoopbackIpv6PrefixStatus=agentLoopbackIpv6PrefixStatus, agentLoopbackIpv6Group=agentLoopbackIpv6Group, agentLoopbackIpv6PrefixPrefix=agentLoopbackIpv6PrefixPrefix, PYSNMP_MODULE_ID=fastPathIpv6Loopback, agentLoopbackIpv6PrefixTable=agentLoopbackIpv6PrefixTable, agentLoopbackIpv6PrefixPrefixLen=agentLoopbackIpv6PrefixPrefixLen, agentLoopbackIpv6PrefixEntry=agentLoopbackIpv6PrefixEntry)
