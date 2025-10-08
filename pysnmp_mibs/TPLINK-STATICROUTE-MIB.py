#
# PySNMP MIB module TPLINK-STATICROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-STATICROUTE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("TPLINK-STATICROUTE-MIB", tpStaticRouteItemInterfaceName=tpStaticRouteItemInterfaceName, PYSNMP_MODULE_ID=tplinkStaticRouteMIB, MacAddress=MacAddress, tpStaticRouteItemDesIp=tpStaticRouteItemDesIp, tpStaticRouteConfigTable=tpStaticRouteConfigTable, tpStaticRouteItemNextIp=tpStaticRouteItemNextIp, tplinkStaticRouteMIBObjects=tplinkStaticRouteMIBObjects, tpStaticRouteItemDistance=tpStaticRouteItemDistance, tpStaticRouteConfigEntry=tpStaticRouteConfigEntry, tplinkStaticRouteNotifications=tplinkStaticRouteNotifications, tpStaticRouteConfig=tpStaticRouteConfig, tpStaticRouteItemMask=tpStaticRouteItemMask, tpStaticRouteItemStatus=tpStaticRouteItemStatus, tplinkStaticRouteMIB=tplinkStaticRouteMIB)
