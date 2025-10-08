#
# PySNMP MIB module RBN-BULKSTATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ericsson/RBN-BULKSTATS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
vacmContextName, = mibBuilder.importSymbols("SNMP-VIEW-BASED-ACM-MIB", "vacmContextName")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnBulkStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 21))
rbnBulkStatsMIB.setRevisions(('2003-02-28 00:00', '2002-05-03 00:00',))
if mibBuilder.loadTexts: rbnBulkStatsMIB.setLastUpdated('200302280000Z')
if mibBuilder.loadTexts: rbnBulkStatsMIB.setOrganization('RedBack Networks, Inc.')
rbnBulkStatsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 21, 0))
rbnBulkStatsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 21, 1))
rbnBulkStatsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 21, 2))
rbnBulkStatsLastTrfr = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1))
rbnBulkStatsLastTrfrIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBulkStatsLastTrfrIpAddrType.setStatus('obsolete')
rbnBulkStatsLastTrfrIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBulkStatsLastTrfrIpAddr.setStatus('obsolete')
rbnBulkStatsLastTrfrStatus = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("success", 2), ("genError", 3), ("loginFailed", 4), ("badFilename", 5), ("remoteHostFailed", 6), ("other", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBulkStatsLastTrfrStatus.setStatus('obsolete')
rbnBulkStatsLastTrfrTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 4), )
if mibBuilder.loadTexts: rbnBulkStatsLastTrfrTable.setStatus('current')
rbnBulkStatsLastTrfrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 4, 1), ).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmContextName"), (0, "RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrPolicy"))
if mibBuilder.loadTexts: rbnBulkStatsLastTrfrEntry.setStatus('current')
rbnBulkStatsLastTrfrPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 20)))
if mibBuilder.loadTexts: rbnBulkStatsLastTrfrPolicy.setStatus('current')
rbnBulkStatsLastTrfrIpAddrType2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 4, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBulkStatsLastTrfrIpAddrType2.setStatus('current')
rbnBulkStatsLastTrfrIpAddr2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 4, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBulkStatsLastTrfrIpAddr2.setStatus('current')
rbnBulkStatsLastTrfrStatus2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("success", 2), ("genError", 3), ("loginFailed", 4), ("badFilename", 5), ("remoteHostFailed", 6), ("other", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBulkStatsLastTrfrStatus2.setStatus('current')
rbnBulkStatsTrfrFail = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 21, 0, 1)).setObjects(("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddrType"), ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddr"), ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrStatus"))
if mibBuilder.loadTexts: rbnBulkStatsTrfrFail.setStatus('obsolete')
rbnBulkStatsTrfrFail2 = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 21, 0, 2)).setObjects(("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddrType2"), ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddr2"), ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrStatus2"))
if mibBuilder.loadTexts: rbnBulkStatsTrfrFail2.setStatus('current')
rbnBulkStatsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 1))
rbnBulkStatsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 2))
rbnBulkStatsMIBObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 1, 1)).setObjects(("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddrType"), ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddr"), ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBulkStatsMIBObjectGroup = rbnBulkStatsMIBObjectGroup.setStatus('obsolete')
rbnBulkStatsMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 1, 2)).setObjects(("RBN-BULKSTATS-MIB", "rbnBulkStatsTrfrFail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBulkStatsMIBNotificationGroup = rbnBulkStatsMIBNotificationGroup.setStatus('obsolete')
rbnBulkStatsMIBObjectGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 1, 3)).setObjects(("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddrType2"), ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddr2"), ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrStatus2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBulkStatsMIBObjectGroup2 = rbnBulkStatsMIBObjectGroup2.setStatus('current')
rbnBulkStatsMIBNotificationGroup2 = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 1, 4)).setObjects(("RBN-BULKSTATS-MIB", "rbnBulkStatsTrfrFail2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBulkStatsMIBNotificationGroup2 = rbnBulkStatsMIBNotificationGroup2.setStatus('current')
rbnBulkStatsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 2, 1)).setObjects(("RBN-BULKSTATS-MIB", "rbnBulkStatsMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBulkStatsMIBCompliance = rbnBulkStatsMIBCompliance.setStatus('obsolete')
rbnBulkStatsMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 2, 2)).setObjects(("RBN-BULKSTATS-MIB", "rbnBulkStatsMIBNotificationGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBulkStatsMIBCompliance2 = rbnBulkStatsMIBCompliance2.setStatus('current')
mibBuilder.exportSymbols("RBN-BULKSTATS-MIB", rbnBulkStatsMIBObjects=rbnBulkStatsMIBObjects, rbnBulkStatsMIBGroups=rbnBulkStatsMIBGroups, rbnBulkStatsMIBCompliances=rbnBulkStatsMIBCompliances, rbnBulkStatsTrfrFail=rbnBulkStatsTrfrFail, rbnBulkStatsMIBNotificationGroup2=rbnBulkStatsMIBNotificationGroup2, rbnBulkStatsLastTrfrIpAddr2=rbnBulkStatsLastTrfrIpAddr2, rbnBulkStatsLastTrfrEntry=rbnBulkStatsLastTrfrEntry, rbnBulkStatsMIBNotificationGroup=rbnBulkStatsMIBNotificationGroup, rbnBulkStatsLastTrfrTable=rbnBulkStatsLastTrfrTable, rbnBulkStatsMIBCompliance=rbnBulkStatsMIBCompliance, rbnBulkStatsMIBNotifications=rbnBulkStatsMIBNotifications, rbnBulkStatsLastTrfrStatus2=rbnBulkStatsLastTrfrStatus2, rbnBulkStatsLastTrfrIpAddrType=rbnBulkStatsLastTrfrIpAddrType, rbnBulkStatsMIBCompliance2=rbnBulkStatsMIBCompliance2, rbnBulkStatsLastTrfrIpAddr=rbnBulkStatsLastTrfrIpAddr, rbnBulkStatsMIB=rbnBulkStatsMIB, rbnBulkStatsLastTrfr=rbnBulkStatsLastTrfr, rbnBulkStatsMIBObjectGroup=rbnBulkStatsMIBObjectGroup, rbnBulkStatsMIBObjectGroup2=rbnBulkStatsMIBObjectGroup2, rbnBulkStatsLastTrfrPolicy=rbnBulkStatsLastTrfrPolicy, PYSNMP_MODULE_ID=rbnBulkStatsMIB, rbnBulkStatsLastTrfrStatus=rbnBulkStatsLastTrfrStatus, rbnBulkStatsMIBConformance=rbnBulkStatsMIBConformance, rbnBulkStatsTrfrFail2=rbnBulkStatsTrfrFail2, rbnBulkStatsLastTrfrIpAddrType2=rbnBulkStatsLastTrfrIpAddrType2)
