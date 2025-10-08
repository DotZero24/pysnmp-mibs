#
# PySNMP MIB module MARVELL-ROUTEMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/radlan/MARVELL-ROUTEMAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:04 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
InetAddressIPv6, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressType", "InetAddress")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("MARVELL-ROUTEMAP-MIB", rlRouteMapPbrRouteMapSectionId=rlRouteMapPbrRouteMapSectionId, rlRouteMapPbrActionNexthopInetAddressType=rlRouteMapPbrActionNexthopInetAddressType, rlRouteMapPbrRowStatus=rlRouteMapPbrRowStatus, RlRouteMapInetType=RlRouteMapInetType, rlRouteMapPbrTable=rlRouteMapPbrTable, rlRouteMapPbrEntry=rlRouteMapPbrEntry, PYSNMP_MODULE_ID=rlRouteMap, rlRouteMapPbrRouteMapName=rlRouteMapPbrRouteMapName, rlRouteMapPbrActionNexthopInetAddress=rlRouteMapPbrActionNexthopInetAddress, rlRouteMapPbrInetType=rlRouteMapPbrInetType, rlRouteMap=rlRouteMap, rlRouteMapPbrMatchAccessListName=rlRouteMapPbrMatchAccessListName, rlRouteMapPbrActionNexthopIfIndex=rlRouteMapPbrActionNexthopIfIndex)
