#
# PySNMP MIB module TPLINK-IPV6STATICROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-IPV6STATICROUTE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

tplinkIPv6StaticRouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 53))
tplinkIPv6StaticRouteMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkIPv6StaticRouteMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkIPv6StaticRouteMIB.setOrganization('TPLINK')
tplinkIPv6StaticRouteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1))
tplinkIPv6StaticRouteNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 53, 2))
tpIPv6StaticRouteConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1))
tpIPv6StaticRouteConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1), )
if mibBuilder.loadTexts: tpIPv6StaticRouteConfigTable.setStatus('current')
tpIPv6StaticRouteConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1), ).setIndexNames((0, "TPLINK-IPV6STATICROUTE-MIB", "tpIPv6StaticRouteItemDesIp"), (0, "TPLINK-IPV6STATICROUTE-MIB", "tpIPv6StaticRouteItemPrefixLen"), (0, "TPLINK-IPV6STATICROUTE-MIB", "tpIPv6StaticRouteItemNexthop"))
if mibBuilder.loadTexts: tpIPv6StaticRouteConfigEntry.setStatus('current')
tpIPv6StaticRouteItemDesIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 1), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemDesIp.setStatus('current')
tpIPv6StaticRouteItemPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemPrefixLen.setStatus('current')
tpIPv6StaticRouteItemNexthop = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemNexthop.setStatus('current')
tpIPv6StaticRouteItemDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemDistance.setStatus('current')
tpIPv6StaticRouteItemInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemInterfaceName.setStatus('current')
tpIPv6StaticRouteItemStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 6), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemStatus.setStatus('current')
mibBuilder.exportSymbols("TPLINK-IPV6STATICROUTE-MIB", tpIPv6StaticRouteConfigTable=tpIPv6StaticRouteConfigTable, tpIPv6StaticRouteConfigEntry=tpIPv6StaticRouteConfigEntry, tplinkIPv6StaticRouteMIB=tplinkIPv6StaticRouteMIB, PYSNMP_MODULE_ID=tplinkIPv6StaticRouteMIB, tpIPv6StaticRouteItemDistance=tpIPv6StaticRouteItemDistance, tpIPv6StaticRouteItemDesIp=tpIPv6StaticRouteItemDesIp, MacAddress=MacAddress, tpIPv6StaticRouteItemNexthop=tpIPv6StaticRouteItemNexthop, tpIPv6StaticRouteItemInterfaceName=tpIPv6StaticRouteItemInterfaceName, tpIPv6StaticRouteItemStatus=tpIPv6StaticRouteItemStatus, tpIPv6StaticRouteConfig=tpIPv6StaticRouteConfig, tpIPv6StaticRouteItemPrefixLen=tpIPv6StaticRouteItemPrefixLen, tplinkIPv6StaticRouteMIBObjects=tplinkIPv6StaticRouteMIBObjects, tplinkIPv6StaticRouteNotifications=tplinkIPv6StaticRouteNotifications)
