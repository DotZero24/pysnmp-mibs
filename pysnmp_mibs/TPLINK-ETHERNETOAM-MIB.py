#
# PySNMP MIB module TPLINK-ETHERNETOAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-ETHERNETOAM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkEthernetOam = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 60))
tplinkEthernetOam.setRevisions(('2015-07-06 10:30',))
if mibBuilder.loadTexts: tplinkEthernetOam.setLastUpdated('201507061030Z')
if mibBuilder.loadTexts: tplinkEthernetOam.setOrganization('TPLINK')
tplinkEthernetOamMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1))
tplinkEthernetOamMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 2))
ethernetOamBasicConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1))
ethernetOamLinkMonConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2))
ethernetOamRfiConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3))
ethernetOamRmtLbConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4))
ethernetOamDiscoveryInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5))
ethernetOamStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6))
ethernetOamEventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7))
mibBuilder.exportSymbols("TPLINK-ETHERNETOAM-MIB", tplinkEthernetOamMIBNotifications=tplinkEthernetOamMIBNotifications, ethernetOamRfiConfig=ethernetOamRfiConfig, tplinkEthernetOam=tplinkEthernetOam, ethernetOamEventLog=ethernetOamEventLog, PYSNMP_MODULE_ID=tplinkEthernetOam, tplinkEthernetOamMIBObjects=tplinkEthernetOamMIBObjects, ethernetOamDiscoveryInfo=ethernetOamDiscoveryInfo, ethernetOamStatistics=ethernetOamStatistics, ethernetOamLinkMonConfig=ethernetOamLinkMonConfig, ethernetOamBasicConfig=ethernetOamBasicConfig, ethernetOamRmtLbConfig=ethernetOamRmtLbConfig)
