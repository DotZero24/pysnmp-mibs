#
# PySNMP MIB module TPLINK-PROXYARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-PROXYARP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:48 2025
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
tplinkProxyArpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 37))
tplinkProxyArpMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkProxyArpMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkProxyArpMIB.setOrganization('TPLINK')
tplinkProxyArpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1))
tplinkProxyArpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 37, 2))
tpProxyArpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1))
tpProxyArpTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1), )
if mibBuilder.loadTexts: tpProxyArpTable.setStatus('current')
tpProxyArpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1), ).setIndexNames((0, "TPLINK-PROXYARP-MIB", "tpProxyArpInterface"))
if mibBuilder.loadTexts: tpProxyArpEntry.setStatus('current')
tpProxyArpInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpProxyArpInterface.setStatus('current')
tpProxyArpIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpProxyArpIpAddr.setStatus('current')
tpProxyArpIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpProxyArpIpMask.setStatus('current')
tpProxyArpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpProxyArpEnable.setStatus('current')
mibBuilder.exportSymbols("TPLINK-PROXYARP-MIB", tplinkProxyArpMIBObjects=tplinkProxyArpMIBObjects, tpProxyArpTable=tpProxyArpTable, tpProxyArpConfig=tpProxyArpConfig, tpProxyArpIpAddr=tpProxyArpIpAddr, tplinkProxyArpMIB=tplinkProxyArpMIB, tplinkProxyArpNotifications=tplinkProxyArpNotifications, tpProxyArpIpMask=tpProxyArpIpMask, tpProxyArpEnable=tpProxyArpEnable, PYSNMP_MODULE_ID=tplinkProxyArpMIB, tpProxyArpEntry=tpProxyArpEntry, tpProxyArpInterface=tpProxyArpInterface)
