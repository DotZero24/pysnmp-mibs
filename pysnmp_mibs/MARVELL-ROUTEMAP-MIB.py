#
# PySNMP MIB module MARVELL-ROUTEMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/radlan/MARVELL-ROUTEMAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
InetAddressIPv6, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressType", "InetAddress")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
rlRouteMap = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 227))
rlRouteMap.setRevisions(('2015-06-08 00:00',))
if mibBuilder.loadTexts: rlRouteMap.setLastUpdated('201506080000Z')
if mibBuilder.loadTexts: rlRouteMap.setOrganization('Marvell Computer Communications Ltd.')
class RlRouteMapInetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

rlRouteMapPbrTable = MibTable((1, 3, 6, 1, 4, 1, 89, 227, 1), )
if mibBuilder.loadTexts: rlRouteMapPbrTable.setStatus('current')
rlRouteMapPbrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 227, 1, 1), ).setIndexNames((0, "MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName"), (0, "MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapSectionId"), (0, "MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrInetType"))
if mibBuilder.loadTexts: rlRouteMapPbrEntry.setStatus('current')
rlRouteMapPbrRouteMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlRouteMapPbrRouteMapName.setStatus('current')
rlRouteMapPbrRouteMapSectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: rlRouteMapPbrRouteMapSectionId.setStatus('current')
rlRouteMapPbrInetType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 3), RlRouteMapInetType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrInetType.setStatus('current')
rlRouteMapPbrMatchAccessListName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrMatchAccessListName.setStatus('current')
rlRouteMapPbrActionNexthopInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 5), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopInetAddressType.setStatus('current')
rlRouteMapPbrActionNexthopInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 6), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopInetAddress.setStatus('current')
rlRouteMapPbrActionNexthopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopIfIndex.setStatus('current')
rlRouteMapPbrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrRowStatus.setStatus('current')
mibBuilder.exportSymbols("MARVELL-ROUTEMAP-MIB", rlRouteMapPbrEntry=rlRouteMapPbrEntry, RlRouteMapInetType=RlRouteMapInetType, rlRouteMapPbrRouteMapSectionId=rlRouteMapPbrRouteMapSectionId, rlRouteMapPbrMatchAccessListName=rlRouteMapPbrMatchAccessListName, PYSNMP_MODULE_ID=rlRouteMap, rlRouteMapPbrInetType=rlRouteMapPbrInetType, rlRouteMapPbrActionNexthopInetAddressType=rlRouteMapPbrActionNexthopInetAddressType, rlRouteMapPbrActionNexthopInetAddress=rlRouteMapPbrActionNexthopInetAddress, rlRouteMapPbrTable=rlRouteMapPbrTable, rlRouteMapPbrRouteMapName=rlRouteMapPbrRouteMapName, rlRouteMapPbrRowStatus=rlRouteMapPbrRowStatus, rlRouteMap=rlRouteMap, rlRouteMapPbrActionNexthopIfIndex=rlRouteMapPbrActionNexthopIfIndex)
