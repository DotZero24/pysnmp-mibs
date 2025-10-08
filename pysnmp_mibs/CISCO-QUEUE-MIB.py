#
# PySNMP MIB module CISCO-QUEUE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-QUEUE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoQueueMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 37))
ciscoQueueMIB.setRevisions(('1995-08-21 00:00',))
if mibBuilder.loadTexts: ciscoQueueMIB.setLastUpdated('9505310000Z')
if mibBuilder.loadTexts: ciscoQueueMIB.setOrganization('Cisco Systems, Inc.')
ciscoQueueObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 37, 1))
ciscoQueueTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 37, 2))
ciscoQueueConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 37, 3))
class CQAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("fifo", 1), ("priority", 2), ("custom", 3), ("weightedFair", 4))

cQIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1), )
if mibBuilder.loadTexts: cQIfTable.setStatus('current')
cQIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cQIfEntry.setStatus('current')
cQIfQType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1, 1), CQAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQIfQType.setStatus('current')
cQIfTxLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQIfTxLimit.setStatus('current')
cQIfSubqueues = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQIfSubqueues.setStatus('current')
cQStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2), )
if mibBuilder.loadTexts: cQStatsTable.setStatus('current')
cQStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QUEUE-MIB", "cQStatsQNumber"))
if mibBuilder.loadTexts: cQStatsEntry.setStatus('current')
cQStatsQNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cQStatsQNumber.setStatus('current')
cQStatsDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQStatsDepth.setStatus('current')
cQStatsMaxDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQStatsMaxDepth.setStatus('current')
cQStatsDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQStatsDiscards.setStatus('current')
cQRotationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 3), )
if mibBuilder.loadTexts: cQRotationTable.setStatus('current')
cQRotationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QUEUE-MIB", "cQStatsQNumber"))
if mibBuilder.loadTexts: cQRotationEntry.setStatus('current')
cQRotationOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQRotationOctets.setStatus('current')
cQCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 1))
cQGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2))
cQCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 1, 1)).setObjects(("CISCO-QUEUE-MIB", "cQIfGroup"), ("CISCO-QUEUE-MIB", "cQStatsGroup"), ("CISCO-QUEUE-MIB", "cQRotationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cQCompliance = cQCompliance.setStatus('current')
cQIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2, 1)).setObjects(("CISCO-QUEUE-MIB", "cQIfQType"), ("CISCO-QUEUE-MIB", "cQIfTxLimit"), ("CISCO-QUEUE-MIB", "cQIfSubqueues"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cQIfGroup = cQIfGroup.setStatus('current')
cQStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2, 2)).setObjects(("CISCO-QUEUE-MIB", "cQStatsDepth"), ("CISCO-QUEUE-MIB", "cQStatsMaxDepth"), ("CISCO-QUEUE-MIB", "cQStatsDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cQStatsGroup = cQStatsGroup.setStatus('current')
cQRotationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2, 3)).setObjects(("CISCO-QUEUE-MIB", "cQRotationOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cQRotationGroup = cQRotationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-QUEUE-MIB", cQStatsQNumber=cQStatsQNumber, PYSNMP_MODULE_ID=ciscoQueueMIB, cQRotationEntry=cQRotationEntry, cQCompliance=cQCompliance, CQAlgorithm=CQAlgorithm, cQIfGroup=cQIfGroup, cQRotationOctets=cQRotationOctets, ciscoQueueObjects=ciscoQueueObjects, cQGroups=cQGroups, cQStatsGroup=cQStatsGroup, cQStatsDepth=cQStatsDepth, cQIfTable=cQIfTable, cQCompliances=cQCompliances, cQStatsMaxDepth=cQStatsMaxDepth, cQStatsEntry=cQStatsEntry, cQIfTxLimit=cQIfTxLimit, cQStatsDiscards=cQStatsDiscards, cQIfQType=cQIfQType, cQRotationGroup=cQRotationGroup, ciscoQueueMIB=ciscoQueueMIB, cQIfEntry=cQIfEntry, cQRotationTable=cQRotationTable, cQStatsTable=cQStatsTable, ciscoQueueConformance=ciscoQueueConformance, ciscoQueueTraps=ciscoQueueTraps, cQIfSubqueues=cQIfSubqueues)
