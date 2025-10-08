#
# PySNMP MIB module ZYXEL-IPV6-PATH-MTU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-IPV6-PATH-MTU-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:03:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelIpv6PathMtu = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36))
if mibBuilder.loadTexts: zyxelIpv6PathMtu.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelIpv6PathMtu.setOrganization('Enterprise Solution ZyXEL')
zyxelPathMtuDiscoveryStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36, 1))
zyxelPathMtuDiscoveryTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36, 1, 1), )
if mibBuilder.loadTexts: zyxelPathMtuDiscoveryTable.setStatus('current')
zyxelPathMtuDiscoveryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36, 1, 1, 1), ).setIndexNames((0, "ZYXEL-IPV6-PATH-MTU-MIB", "zyPathMtuDiscoveryDestinationIpAddressType"), (0, "ZYXEL-IPV6-PATH-MTU-MIB", "zyPathMtuDiscoveryDestinationIpAddress"))
if mibBuilder.loadTexts: zyxelPathMtuDiscoveryEntry.setStatus('current')
zyPathMtuDiscoveryDestinationIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36, 1, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: zyPathMtuDiscoveryDestinationIpAddressType.setStatus('current')
zyPathMtuDiscoveryDestinationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36, 1, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: zyPathMtuDiscoveryDestinationIpAddress.setStatus('current')
zyPathMtuDiscoveryMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPathMtuDiscoveryMtu.setStatus('current')
zyPathMtuDiscoveryExpiredTime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPathMtuDiscoveryExpiredTime.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-IPV6-PATH-MTU-MIB", zyPathMtuDiscoveryDestinationIpAddress=zyPathMtuDiscoveryDestinationIpAddress, PYSNMP_MODULE_ID=zyxelIpv6PathMtu, zyxelPathMtuDiscoveryEntry=zyxelPathMtuDiscoveryEntry, zyxelPathMtuDiscoveryTable=zyxelPathMtuDiscoveryTable, zyPathMtuDiscoveryMtu=zyPathMtuDiscoveryMtu, zyxelIpv6PathMtu=zyxelIpv6PathMtu, zyPathMtuDiscoveryExpiredTime=zyPathMtuDiscoveryExpiredTime, zyPathMtuDiscoveryDestinationIpAddressType=zyPathMtuDiscoveryDestinationIpAddressType, zyxelPathMtuDiscoveryStatus=zyxelPathMtuDiscoveryStatus)
