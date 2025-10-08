#
# PySNMP MIB module IPV6-LOOPBACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/quanta/IPV6-LOOPBACK-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressPrefixLength, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength")
Ipv6AddressPrefix, = mibBuilder.importSymbols("IPV6-TC", "Ipv6AddressPrefix")
agentLoopbackID, = mibBuilder.importSymbols("LOOPBACK-MIB", "agentLoopbackID")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
RowStatus, TextualConvention, PhysAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "PhysAddress", "TruthValue", "DisplayString")
ipv6Loopback = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 23))
if mibBuilder.loadTexts: ipv6Loopback.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: ipv6Loopback.setOrganization('QCI')
agentLoopbackIpv6Group = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 23, 1))
agentLoopbackIpv6PrefixTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 23, 1, 1), )
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixTable.setStatus('current')
agentLoopbackIpv6PrefixEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 23, 1, 1, 1), ).setIndexNames((0, "LOOPBACK-MIB", "agentLoopbackID"), (0, "IPV6-LOOPBACK-MIB", "agentLoopbackIpv6PrefixPrefix"), (0, "IPV6-LOOPBACK-MIB", "agentLoopbackIpv6PrefixPrefixLen"))
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixEntry.setStatus('current')
agentLoopbackIpv6PrefixPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 23, 1, 1, 1, 1), Ipv6AddressPrefix())
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixPrefix.setStatus('current')
agentLoopbackIpv6PrefixPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 23, 1, 1, 1, 2), InetAddressPrefixLength())
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixPrefixLen.setStatus('current')
agentLoopbackIpv6PrefixStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 23, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixStatus.setStatus('current')
mibBuilder.exportSymbols("IPV6-LOOPBACK-MIB", agentLoopbackIpv6PrefixStatus=agentLoopbackIpv6PrefixStatus, PYSNMP_MODULE_ID=ipv6Loopback, agentLoopbackIpv6Group=agentLoopbackIpv6Group, ipv6Loopback=ipv6Loopback, agentLoopbackIpv6PrefixPrefix=agentLoopbackIpv6PrefixPrefix, agentLoopbackIpv6PrefixTable=agentLoopbackIpv6PrefixTable, agentLoopbackIpv6PrefixPrefixLen=agentLoopbackIpv6PrefixPrefixLen, agentLoopbackIpv6PrefixEntry=agentLoopbackIpv6PrefixEntry)
