#
# PySNMP MIB module TPLINK-LOCALPROXYARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-LOCALPROXYARP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:46 2025
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
mibBuilder.exportSymbols("TPLINK-LOCALPROXYARP-MIB", tpLocalProxyArpEnable=tpLocalProxyArpEnable, tpLocalProxyArpConfig=tpLocalProxyArpConfig, tpLocalProxyArpEntry=tpLocalProxyArpEntry, tpLocalProxyArpIpAddr=tpLocalProxyArpIpAddr, tpLocalProxyArpIpMask=tpLocalProxyArpIpMask, tplinkLocalProxyArpMIB=tplinkLocalProxyArpMIB, tpLocalProxyArpTable=tpLocalProxyArpTable, tplinkLocalProxyArpMIBObjects=tplinkLocalProxyArpMIBObjects, PYSNMP_MODULE_ID=tplinkLocalProxyArpMIB, tpLocalProxyArpInterface=tpLocalProxyArpInterface, tplinkLocalProxyArpNotifications=tplinkLocalProxyArpNotifications)
