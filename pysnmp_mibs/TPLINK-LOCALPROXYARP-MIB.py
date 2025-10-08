#
# PySNMP MIB module TPLINK-LOCALPROXYARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-LOCALPROXYARP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:22 2025
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
tplinkLocalProxyArpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 46))
tplinkLocalProxyArpMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkLocalProxyArpMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkLocalProxyArpMIB.setOrganization('TPLINK')
tplinkLocalProxyArpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 46, 1))
tplinkLocalProxyArpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 46, 2))
tpLocalProxyArpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 46, 1))
tpLocalProxyArpTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 46, 1, 1), )
if mibBuilder.loadTexts: tpLocalProxyArpTable.setStatus('current')
tpLocalProxyArpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 46, 1, 1, 1), ).setIndexNames((0, "TPLINK-LOCALPROXYARP-MIB", "tpLocalProxyArpInterface"))
if mibBuilder.loadTexts: tpLocalProxyArpEntry.setStatus('current')
tpLocalProxyArpInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 46, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpLocalProxyArpInterface.setStatus('current')
tpLocalProxyArpIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 46, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpLocalProxyArpIpAddr.setStatus('current')
tpLocalProxyArpIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 46, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpLocalProxyArpIpMask.setStatus('current')
tpLocalProxyArpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 46, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpLocalProxyArpEnable.setStatus('current')
mibBuilder.exportSymbols("TPLINK-LOCALPROXYARP-MIB", tpLocalProxyArpIpAddr=tpLocalProxyArpIpAddr, tplinkLocalProxyArpMIBObjects=tplinkLocalProxyArpMIBObjects, tplinkLocalProxyArpMIB=tplinkLocalProxyArpMIB, tpLocalProxyArpEnable=tpLocalProxyArpEnable, tpLocalProxyArpEntry=tpLocalProxyArpEntry, tpLocalProxyArpConfig=tpLocalProxyArpConfig, tplinkLocalProxyArpNotifications=tplinkLocalProxyArpNotifications, tpLocalProxyArpIpMask=tpLocalProxyArpIpMask, PYSNMP_MODULE_ID=tplinkLocalProxyArpMIB, tpLocalProxyArpTable=tpLocalProxyArpTable, tpLocalProxyArpInterface=tpLocalProxyArpInterface)
