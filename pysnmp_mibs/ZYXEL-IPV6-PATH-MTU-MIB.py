#
# PySNMP MIB module ZYXEL-IPV6-PATH-MTU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-IPV6-PATH-MTU-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:37:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ZYXEL-IPV6-PATH-MTU-MIB", zyxelIpv6PathMtu=zyxelIpv6PathMtu, zyxelPathMtuDiscoveryStatus=zyxelPathMtuDiscoveryStatus, zyPathMtuDiscoveryMtu=zyPathMtuDiscoveryMtu, zyPathMtuDiscoveryDestinationIpAddress=zyPathMtuDiscoveryDestinationIpAddress, PYSNMP_MODULE_ID=zyxelIpv6PathMtu, zyxelPathMtuDiscoveryEntry=zyxelPathMtuDiscoveryEntry, zyxelPathMtuDiscoveryTable=zyxelPathMtuDiscoveryTable, zyPathMtuDiscoveryExpiredTime=zyPathMtuDiscoveryExpiredTime, zyPathMtuDiscoveryDestinationIpAddressType=zyPathMtuDiscoveryDestinationIpAddressType)
