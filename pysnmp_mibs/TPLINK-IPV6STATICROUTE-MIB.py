#
# PySNMP MIB module TPLINK-IPV6STATICROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-IPV6STATICROUTE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("TPLINK-IPV6STATICROUTE-MIB", PYSNMP_MODULE_ID=tplinkIPv6StaticRouteMIB, tpIPv6StaticRouteItemStatus=tpIPv6StaticRouteItemStatus, tpIPv6StaticRouteItemInterfaceName=tpIPv6StaticRouteItemInterfaceName, tplinkIPv6StaticRouteMIB=tplinkIPv6StaticRouteMIB, MacAddress=MacAddress, tpIPv6StaticRouteItemDistance=tpIPv6StaticRouteItemDistance, tpIPv6StaticRouteItemDesIp=tpIPv6StaticRouteItemDesIp, tpIPv6StaticRouteItemNexthop=tpIPv6StaticRouteItemNexthop, tpIPv6StaticRouteConfigTable=tpIPv6StaticRouteConfigTable, tpIPv6StaticRouteItemPrefixLen=tpIPv6StaticRouteItemPrefixLen, tplinkIPv6StaticRouteNotifications=tplinkIPv6StaticRouteNotifications, tpIPv6StaticRouteConfigEntry=tpIPv6StaticRouteConfigEntry, tpIPv6StaticRouteConfig=tpIPv6StaticRouteConfig, tplinkIPv6StaticRouteMIBObjects=tplinkIPv6StaticRouteMIBObjects)
