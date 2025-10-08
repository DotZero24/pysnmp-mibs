#
# PySNMP MIB module EXTREME-ACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/extreme/EXTREME-ACL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
extremeAclDirection, = mibBuilder.importSymbols("EXTREME-CLEARFLOW-MIB", "extremeAclDirection")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
extremeAcl = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 48))
extremeAcl.setRevisions(('2015-12-11 00:00',))
if mibBuilder.loadTexts: extremeAcl.setLastUpdated('201512110000Z')
if mibBuilder.loadTexts: extremeAcl.setOrganization('Extreme Networks, Inc.')
extremeAclObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 48, 1))
extremeAclStatsTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1), )
if mibBuilder.loadTexts: extremeAclStatsTable.setStatus('current')
extremeAclStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1, 1), ).setIndexNames((0, "EXTREME-ACL-MIB", "extremeAclStatsVlanIfIndex"), (0, "EXTREME-ACL-MIB", "extremeAclStatsPortIfIndex"), (0, "EXTREME-CLEARFLOW-MIB", "extremeAclDirection"), (0, "EXTREME-ACL-MIB", "extremeAclStatsCounterName"))
if mibBuilder.loadTexts: extremeAclStatsEntry.setStatus('current')
extremeAclStatsVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: extremeAclStatsVlanIfIndex.setStatus('current')
extremeAclStatsPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1, 1, 2), InterfaceIndexOrZero())
if mibBuilder.loadTexts: extremeAclStatsPortIfIndex.setStatus('current')
extremeAclDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
if mibBuilder.loadTexts: extremeAclDirection.setStatus('current')
extremeAclStatsCounterName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: extremeAclStatsCounterName.setStatus('current')
extremeAclStatsPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeAclStatsPktCount.setStatus('current')
extremeAclStatsByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 48, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeAclStatsByteCount.setStatus('current')
aclConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 48, 9))
aclGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 48, 9, 1))
aclCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 48, 9, 2))
aclStatistics = ModuleCompliance((1, 3, 6, 1, 4, 1, 1916, 1, 48, 9, 2, 1)).setObjects(("EXTREME-ACL-MIB", "aclCounterStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aclStatistics = aclStatistics.setStatus('current')
aclCounterStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1916, 1, 48, 9, 1, 1)).setObjects(("EXTREME-ACL-MIB", "extremeAclStatsPktCount"), ("EXTREME-ACL-MIB", "extremeAclStatsByteCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aclCounterStatsGroup = aclCounterStatsGroup.setStatus('current')
mibBuilder.exportSymbols("EXTREME-ACL-MIB", extremeAclStatsVlanIfIndex=extremeAclStatsVlanIfIndex, extremeAclObjects=extremeAclObjects, extremeAclStatsPktCount=extremeAclStatsPktCount, PYSNMP_MODULE_ID=extremeAcl, extremeAclStatsTable=extremeAclStatsTable, aclConformance=aclConformance, extremeAcl=extremeAcl, extremeAclStatsByteCount=extremeAclStatsByteCount, extremeAclStatsPortIfIndex=extremeAclStatsPortIfIndex, aclStatistics=aclStatistics, aclGroups=aclGroups, aclCounterStatsGroup=aclCounterStatsGroup, aclCompliances=aclCompliances, extremeAclStatsEntry=extremeAclStatsEntry, extremeAclStatsCounterName=extremeAclStatsCounterName, extremeAclDirection=extremeAclDirection)
