#
# PySNMP MIB module ARISTA-BRIDGE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/arista/ARISTA-BRIDGE-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:28 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1qTpFdbAddress, dot1qTpFdbPort, dot1qFdbId = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qTpFdbAddress", "dot1qTpFdbPort", "dot1qFdbId")
TimeFilter, = mibBuilder.importSymbols("RMON2-MIB", "TimeFilter")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aristaBridgeExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 2))
aristaBridgeExtMIB.setRevisions(('2020-09-29 00:00', '2019-09-15 00:00', '2014-08-15 00:00', '2011-03-31 13:00', '2010-05-03 00:00',))
if mibBuilder.loadTexts: aristaBridgeExtMIB.setLastUpdated('202009290000Z')
if mibBuilder.loadTexts: aristaBridgeExtMIB.setOrganization('Arista Networks, Inc.')
aristaBridgeExtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 2, 0))
aristaDot1qTpFdbTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 2, 1), )
if mibBuilder.loadTexts: aristaDot1qTpFdbTable.setStatus('current')
aristaDot1qTpFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1), ).setIndexNames((0, "ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbTimeMark"), (0, "Q-BRIDGE-MIB", "dot1qFdbId"), (0, "Q-BRIDGE-MIB", "dot1qTpFdbAddress"))
if mibBuilder.loadTexts: aristaDot1qTpFdbEntry.setStatus('current')
aristaDot1qTpFdbTimeMark = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1, 1), TimeFilter())
if mibBuilder.loadTexts: aristaDot1qTpFdbTimeMark.setStatus('current')
aristaDot1qTpFdbNumMoves = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaDot1qTpFdbNumMoves.setStatus('current')
aristaDot1qTpFdbLastMove = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaDot1qTpFdbLastMove.setStatus('current')
aristaMacStatsTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 2, 3), )
if mibBuilder.loadTexts: aristaMacStatsTable.setStatus('current')
aristaMacStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 2, 3, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qFdbId"), (0, "ARISTA-BRIDGE-EXT-MIB", "aristaMacStatsEntryType"))
if mibBuilder.loadTexts: aristaMacStatsEntry.setStatus('current')
aristaMacStatsEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2))))
if mibBuilder.loadTexts: aristaMacStatsEntryType.setStatus('current')
aristaMacStatsEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 2, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaMacStatsEntries.setStatus('current')
aristaMacMove = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 2, 0, 1)).setObjects(("ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbNumMoves"), ("Q-BRIDGE-MIB", "dot1qTpFdbPort"))
if mibBuilder.loadTexts: aristaMacMove.setStatus('current')
aristaMacLearn = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 2, 0, 2)).setObjects(("Q-BRIDGE-MIB", "dot1qTpFdbPort"))
if mibBuilder.loadTexts: aristaMacLearn.setStatus('current')
aristaMacAge = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 2, 0, 3)).setObjects(("Q-BRIDGE-MIB", "dot1qTpFdbPort"))
if mibBuilder.loadTexts: aristaMacAge.setStatus('current')
aristaBridgeExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2))
aristaBridgeExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 1))
aristaBridgeExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 2))
aristaBridgeExtBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 1, 1)).setObjects(("ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbNumMoves"), ("ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbLastMove"), ("ARISTA-BRIDGE-EXT-MIB", "aristaMacStatsEntries"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBridgeExtBaseGroup = aristaBridgeExtBaseGroup.setStatus('current')
aristaBridgeExtNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 1, 2)).setObjects(("ARISTA-BRIDGE-EXT-MIB", "aristaMacMove"), ("ARISTA-BRIDGE-EXT-MIB", "aristaMacLearn"), ("ARISTA-BRIDGE-EXT-MIB", "aristaMacAge"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBridgeExtNotificationGroup = aristaBridgeExtNotificationGroup.setStatus('current')
aristaBridgeExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 2, 1)).setObjects(("ARISTA-BRIDGE-EXT-MIB", "aristaBridgeExtBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBridgeExtCompliance = aristaBridgeExtCompliance.setStatus('current')
aristaBridgeExtNotificationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 2, 2)).setObjects(("ARISTA-BRIDGE-EXT-MIB", "aristaBridgeExtNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBridgeExtNotificationCompliance = aristaBridgeExtNotificationCompliance.setStatus('current')
mibBuilder.exportSymbols("ARISTA-BRIDGE-EXT-MIB", aristaMacLearn=aristaMacLearn, aristaDot1qTpFdbTable=aristaDot1qTpFdbTable, aristaBridgeExtBaseGroup=aristaBridgeExtBaseGroup, PYSNMP_MODULE_ID=aristaBridgeExtMIB, aristaDot1qTpFdbEntry=aristaDot1qTpFdbEntry, aristaMacStatsEntry=aristaMacStatsEntry, aristaBridgeExtCompliance=aristaBridgeExtCompliance, aristaMacStatsEntries=aristaMacStatsEntries, aristaDot1qTpFdbLastMove=aristaDot1qTpFdbLastMove, aristaDot1qTpFdbTimeMark=aristaDot1qTpFdbTimeMark, aristaMacStatsTable=aristaMacStatsTable, aristaDot1qTpFdbNumMoves=aristaDot1qTpFdbNumMoves, aristaBridgeExtNotifications=aristaBridgeExtNotifications, aristaBridgeExtNotificationCompliance=aristaBridgeExtNotificationCompliance, aristaBridgeExtGroups=aristaBridgeExtGroups, aristaMacStatsEntryType=aristaMacStatsEntryType, aristaBridgeExtConformance=aristaBridgeExtConformance, aristaBridgeExtNotificationGroup=aristaBridgeExtNotificationGroup, aristaMacMove=aristaMacMove, aristaBridgeExtCompliances=aristaBridgeExtCompliances, aristaBridgeExtMIB=aristaBridgeExtMIB, aristaMacAge=aristaMacAge)
