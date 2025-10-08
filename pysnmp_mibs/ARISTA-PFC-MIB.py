#
# PySNMP MIB module ARISTA-PFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/arista/ARISTA-PFC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
PacketType, = mibBuilder.importSymbols("ARISTA-QUEUE-MIB", "PacketType")
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aristaPfcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 11))
aristaPfcMIB.setRevisions(('2017-01-17 00:00', '2014-08-15 00:00', '2013-02-28 00:00',))
if mibBuilder.loadTexts: aristaPfcMIB.setLastUpdated('201701170000Z')
if mibBuilder.loadTexts: aristaPfcMIB.setOrganization('Arista Networks, Inc.')
aristaPfc = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1))
aristaPfcConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 11, 2))
class AristaPfcCOSIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

aristaPfcPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1), )
if mibBuilder.loadTexts: aristaPfcPriorityTable.setStatus('current')
aristaPfcPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1), ).setIndexNames((0, "ARISTA-PFC-MIB", "aristaPfcIfIndex"), (0, "ARISTA-PFC-MIB", "aristaPfcPriorityIndex"))
if mibBuilder.loadTexts: aristaPfcPriorityEntry.setStatus('current')
aristaPfcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: aristaPfcIfIndex.setStatus('current')
aristaPfcPriorityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 2), AristaPfcCOSIndex())
if mibBuilder.loadTexts: aristaPfcPriorityIndex.setStatus('current')
aristaPfcPriorityRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 3), Counter64()).setUnits('Requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPfcPriorityRequests.setStatus('current')
aristaPfcPriorityIndications = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 4), Counter64()).setUnits('Indications').setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPfcPriorityIndications.setStatus('current')
aristaPfcWatchdogTxQueueTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 2), )
if mibBuilder.loadTexts: aristaPfcWatchdogTxQueueTable.setStatus('current')
aristaPfcWatchdogTxQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 2, 1), ).setIndexNames((0, "ARISTA-PFC-MIB", "aristaPfcWatchdogIfIndex"), (0, "ARISTA-PFC-MIB", "aristaPfcWatchdogTxQueueType"), (0, "ARISTA-PFC-MIB", "aristaPfcWatchdogTxQueueId"))
if mibBuilder.loadTexts: aristaPfcWatchdogTxQueueEntry.setStatus('current')
aristaPfcWatchdogIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: aristaPfcWatchdogIfIndex.setStatus('current')
aristaPfcWatchdogTxQueueType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 2, 1, 2), PacketType())
if mibBuilder.loadTexts: aristaPfcWatchdogTxQueueType.setStatus('current')
aristaPfcWatchdogTxQueueId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: aristaPfcWatchdogTxQueueId.setStatus('current')
aristaPfcWatchdogTxQueueStuckCount = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPfcWatchdogTxQueueStuckCount.setStatus('current')
aristaPfcWatchdogTxQueueRecoveredCount = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPfcWatchdogTxQueueRecoveredCount.setStatus('current')
aristaPfcCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 1))
aristaPfcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 2))
aristaPfcCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 1, 1)).setObjects(("ARISTA-PFC-MIB", "aristaPfcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaPfcCompliance = aristaPfcCompliance.setStatus('current')
aristaPfcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 2, 1)).setObjects(("ARISTA-PFC-MIB", "aristaPfcPriorityRequests"), ("ARISTA-PFC-MIB", "aristaPfcPriorityIndications"), ("ARISTA-PFC-MIB", "aristaPfcWatchdogTxQueueStuckCount"), ("ARISTA-PFC-MIB", "aristaPfcWatchdogTxQueueRecoveredCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaPfcGroup = aristaPfcGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-PFC-MIB", aristaPfcIfIndex=aristaPfcIfIndex, aristaPfcWatchdogTxQueueTable=aristaPfcWatchdogTxQueueTable, aristaPfcGroups=aristaPfcGroups, aristaPfcCompliance=aristaPfcCompliance, aristaPfcPriorityIndications=aristaPfcPriorityIndications, aristaPfcWatchdogTxQueueEntry=aristaPfcWatchdogTxQueueEntry, aristaPfcPriorityRequests=aristaPfcPriorityRequests, aristaPfcWatchdogTxQueueRecoveredCount=aristaPfcWatchdogTxQueueRecoveredCount, AristaPfcCOSIndex=AristaPfcCOSIndex, aristaPfcWatchdogTxQueueStuckCount=aristaPfcWatchdogTxQueueStuckCount, aristaPfc=aristaPfc, PYSNMP_MODULE_ID=aristaPfcMIB, aristaPfcMIB=aristaPfcMIB, aristaPfcWatchdogTxQueueType=aristaPfcWatchdogTxQueueType, aristaPfcConformance=aristaPfcConformance, aristaPfcCompliances=aristaPfcCompliances, aristaPfcPriorityTable=aristaPfcPriorityTable, aristaPfcPriorityEntry=aristaPfcPriorityEntry, aristaPfcWatchdogTxQueueId=aristaPfcWatchdogTxQueueId, aristaPfcPriorityIndex=aristaPfcPriorityIndex, aristaPfcWatchdogIfIndex=aristaPfcWatchdogIfIndex, aristaPfcGroup=aristaPfcGroup)
