#
# PySNMP MIB module TPLINK-STATICROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-STATICROUTE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

tplinkStaticRouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 36))
tplinkStaticRouteMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkStaticRouteMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkStaticRouteMIB.setOrganization('TPLINK')
tplinkStaticRouteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1))
tplinkStaticRouteNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 36, 2))
tpStaticRouteConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1))
tpStaticRouteConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1), )
if mibBuilder.loadTexts: tpStaticRouteConfigTable.setStatus('current')
tpStaticRouteConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1), ).setIndexNames((0, "TPLINK-STATICROUTE-MIB", "tpStaticRouteItemDesIp"), (0, "TPLINK-STATICROUTE-MIB", "tpStaticRouteItemMask"), (0, "TPLINK-STATICROUTE-MIB", "tpStaticRouteItemNextIp"))
if mibBuilder.loadTexts: tpStaticRouteConfigEntry.setStatus('current')
tpStaticRouteItemDesIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStaticRouteItemDesIp.setStatus('current')
tpStaticRouteItemMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStaticRouteItemMask.setStatus('current')
tpStaticRouteItemNextIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStaticRouteItemNextIp.setStatus('current')
tpStaticRouteItemDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStaticRouteItemDistance.setStatus('current')
tpStaticRouteItemInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStaticRouteItemInterfaceName.setStatus('current')
tpStaticRouteItemStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 6), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStaticRouteItemStatus.setStatus('current')
mibBuilder.exportSymbols("TPLINK-STATICROUTE-MIB", tpStaticRouteItemDistance=tpStaticRouteItemDistance, tplinkStaticRouteNotifications=tplinkStaticRouteNotifications, tpStaticRouteItemInterfaceName=tpStaticRouteItemInterfaceName, tpStaticRouteConfigEntry=tpStaticRouteConfigEntry, tpStaticRouteItemNextIp=tpStaticRouteItemNextIp, PYSNMP_MODULE_ID=tplinkStaticRouteMIB, tpStaticRouteItemMask=tpStaticRouteItemMask, tpStaticRouteConfig=tpStaticRouteConfig, tplinkStaticRouteMIB=tplinkStaticRouteMIB, tplinkStaticRouteMIBObjects=tplinkStaticRouteMIBObjects, tpStaticRouteItemStatus=tpStaticRouteItemStatus, MacAddress=MacAddress, tpStaticRouteConfigTable=tpStaticRouteConfigTable, tpStaticRouteItemDesIp=tpStaticRouteItemDesIp)
