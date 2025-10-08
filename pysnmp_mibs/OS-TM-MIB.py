#
# PySNMP MIB module OS-TM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mrv/OS-TM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
oaOptiSwitch, = mibBuilder.importSymbols("OS-COMMON-TC-MIB", "oaOptiSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
osTm = ModuleIdentity((1, 3, 6, 1, 4, 1, 6926, 2, 38))
osTm.setRevisions(('2016-11-06 00:00',))
if mibBuilder.loadTexts: osTm.setLastUpdated('201611060000Z')
if mibBuilder.loadTexts: osTm.setOrganization('MRV Communications, Inc.')
osTmCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 38, 1))
osTmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 38, 100))
osTmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 38, 100, 1))
osTmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 38, 100, 2))
class TmPortIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class TmNodeId(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class TmSlQueueId(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

osTmSupport = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 38, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notSupported", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: osTmSupport.setStatus('current')
osTmCountTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 38, 20), )
if mibBuilder.loadTexts: osTmCountTable.setStatus('current')
osTmCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1), ).setIndexNames((0, "OS-TM-MIB", "osTmCountPort"), (0, "OS-TM-MIB", "osTmCountServNode"), (0, "OS-TM-MIB", "osTmCountBNode"), (0, "OS-TM-MIB", "osTmCountCNode"), (0, "OS-TM-MIB", "osTmCountSlQueue"))
if mibBuilder.loadTexts: osTmCountEntry.setStatus('current')
osTmCountPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 1), TmPortIndex())
if mibBuilder.loadTexts: osTmCountPort.setStatus('current')
osTmCountServNode = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 2), TmNodeId())
if mibBuilder.loadTexts: osTmCountServNode.setStatus('current')
osTmCountBNode = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 3), TmNodeId())
if mibBuilder.loadTexts: osTmCountBNode.setStatus('current')
osTmCountCNode = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 4), TmNodeId())
if mibBuilder.loadTexts: osTmCountCNode.setStatus('current')
osTmCountSlQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 5), TmSlQueueId())
if mibBuilder.loadTexts: osTmCountSlQueue.setStatus('current')
osTmCountClear = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osTmCountClear.setStatus('current')
osTmCountPacketsPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osTmCountPacketsPassed.setStatus('current')
osTmCountPacketsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osTmCountPacketsDropped.setStatus('current')
osTmCountBytesPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osTmCountBytesPassed.setStatus('current')
osTmCountBytesDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osTmCountBytesDropped.setStatus('current')
osTmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6926, 2, 38, 100, 1, 1)).setObjects(("OS-TM-MIB", "osTmMandatoryGroup"), ("OS-TM-MIB", "osTmOptGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osTmMIBCompliance = osTmMIBCompliance.setStatus('current')
osTmMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6926, 2, 38, 100, 2, 1)).setObjects(("OS-TM-MIB", "osTmSupport"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osTmMandatoryGroup = osTmMandatoryGroup.setStatus('current')
osTmOptGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6926, 2, 38, 100, 2, 2)).setObjects(("OS-TM-MIB", "osTmCountClear"), ("OS-TM-MIB", "osTmCountPacketsPassed"), ("OS-TM-MIB", "osTmCountPacketsDropped"), ("OS-TM-MIB", "osTmCountBytesPassed"), ("OS-TM-MIB", "osTmCountBytesDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osTmOptGroup = osTmOptGroup.setStatus('current')
mibBuilder.exportSymbols("OS-TM-MIB", PYSNMP_MODULE_ID=osTm, osTmMandatoryGroup=osTmMandatoryGroup, osTmCountCNode=osTmCountCNode, osTmCountEntry=osTmCountEntry, osTmSupport=osTmSupport, TmPortIndex=TmPortIndex, TmNodeId=TmNodeId, osTmMIBCompliance=osTmMIBCompliance, osTmCountServNode=osTmCountServNode, osTmCountTable=osTmCountTable, osTmCountBytesDropped=osTmCountBytesDropped, osTmOptGroup=osTmOptGroup, osTmCountSlQueue=osTmCountSlQueue, osTm=osTm, osTmCountBNode=osTmCountBNode, osTmCapabilities=osTmCapabilities, osTmCountPacketsPassed=osTmCountPacketsPassed, osTmCountPacketsDropped=osTmCountPacketsDropped, osTmCountBytesPassed=osTmCountBytesPassed, osTmMIBGroups=osTmMIBGroups, osTmCountPort=osTmCountPort, osTmConformance=osTmConformance, osTmCountClear=osTmCountClear, osTmMIBCompliances=osTmMIBCompliances, TmSlQueueId=TmSlQueueId)
