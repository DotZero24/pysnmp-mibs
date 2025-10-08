#
# PySNMP MIB module EXTREME-ACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/extreme/EXTREME-ACL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
extremeAclDirection, = mibBuilder.importSymbols("EXTREME-CLEARFLOW-MIB", "extremeAclDirection")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("EXTREME-ACL-MIB", extremeAclStatsPortIfIndex=extremeAclStatsPortIfIndex, aclStatistics=aclStatistics, extremeAclStatsCounterName=extremeAclStatsCounterName, extremeAclStatsPktCount=extremeAclStatsPktCount, extremeAclStatsByteCount=extremeAclStatsByteCount, extremeAclObjects=extremeAclObjects, extremeAclStatsTable=extremeAclStatsTable, extremeAclStatsEntry=extremeAclStatsEntry, extremeAclDirection=extremeAclDirection, aclCounterStatsGroup=aclCounterStatsGroup, aclGroups=aclGroups, aclConformance=aclConformance, extremeAclStatsVlanIfIndex=extremeAclStatsVlanIfIndex, extremeAcl=extremeAcl, PYSNMP_MODULE_ID=extremeAcl, aclCompliances=aclCompliances)
